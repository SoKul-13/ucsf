import os
import json
import glob
import pandas as pd
import numpy as np
from scipy import stats
from scipy.signal import find_peaks
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
from multiprocessing import Pool, cpu_count

# Set paths relative to new research structure
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
WORKSPACE_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, ".."))
CGM_DIR = os.path.join(WORKSPACE_ROOT, "dataset", "wearable_blood_glucose", "continuous_glucose_monitoring", "dexcom_g6")
CLINICAL_EXT_PATH = os.path.join(PROJECT_ROOT, "data", "master_extended_dataset.csv")

REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports", "4_personalized_spike_analysis")
DATA_OUT_DIR = os.path.join(REPORTS_DIR, "data")
FIG_OUT_DIR = os.path.join(REPORTS_DIR, "figures")

os.makedirs(DATA_OUT_DIR, exist_ok=True)
os.makedirs(FIG_OUT_DIR, exist_ok=True)

def parse_glucose_val(raw_val):
    if raw_val is None:
        return None
    if isinstance(raw_val, (int, float)):
        return float(raw_val)
    val_str = str(raw_val).strip()
    if val_str.lower() == 'high':
        return 400.0
    if val_str.lower() == 'low':
        return 40.0
    try:
        return float(val_str)
    except ValueError:
        return None

def compute_15_metric_battery(g_vals):
    """Computes a 15-metric clinical battery for a given array of glucose readings."""
    defaults = {
        'mean_glucose': np.nan,
        'sd_glucose': np.nan,
        'cv_glucose': np.nan,
        'tir_70_180': np.nan,
        'tar1_181_250': np.nan,
        'tar2_over_250': np.nan,
        'tbr1_54_69': np.nan,
        'tbr2_under_54': np.nan,
        'mag_change': np.nan,
        'lbgi': np.nan,
        'hbgi': np.nan,
        'mage': np.nan,
        'conga1': np.nan,
        'conga2': np.nan
    }
    if g_vals is None or len(g_vals) == 0:
        return defaults
    
    mu = float(np.mean(g_vals))
    sd = float(np.std(g_vals, ddof=1)) if len(g_vals) > 1 else 0.001
    cv = sd / mu if mu > 0 else 0.0
    
    n_tot = len(g_vals)
    tir = float(np.sum((g_vals >= 70) & (g_vals <= 180)) / n_tot * 100.0)
    tar1 = float(np.sum((g_vals > 180) & (g_vals <= 250)) / n_tot * 100.0)
    tar2 = float(np.sum(g_vals > 250) / n_tot * 100.0)
    tbr1 = float(np.sum((g_vals >= 54) & (g_vals < 70)) / n_tot * 100.0)
    tbr2 = float(np.sum(g_vals < 54) / n_tot * 100.0)
    
    mag = float(np.mean(np.abs(np.diff(g_vals)))) if len(g_vals) > 1 else 0.0
    
    with np.errstate(divide='ignore', invalid='ignore'):
        g_safe = np.maximum(g_vals, 1.0)
        f_g = 1.509 * (np.power(np.log(g_safe), 1.084) - 5.381)
        r_g = 10.0 * (f_g ** 2)
        rl = np.where(f_g < 0, r_g, 0.0)
        rh = np.where(f_g > 0, r_g, 0.0)
        lbgi = float(np.nanmean(rl)) if len(rl) > 0 else 0.0
        hbgi = float(np.nanmean(rh)) if len(rh) > 0 else 0.0
        
    peaks, _ = find_peaks(g_vals, prominence=sd)
    troughs, _ = find_peaks(-g_vals, prominence=sd)
    excursions = []
    for p in peaks:
        nearest_troughs = troughs[troughs < p]
        if len(nearest_troughs) > 0:
            tr = nearest_troughs[-1]
            amp = g_vals[p] - g_vals[tr]
            if amp > sd:
                excursions.append(amp)
    mage = float(np.mean(excursions)) if len(excursions) > 0 else sd
    
    conga1 = float(np.std(g_vals[12:] - g_vals[:-12], ddof=1)) if len(g_vals) > 12 else sd
    conga2 = float(np.std(g_vals[24:] - g_vals[:-24], ddof=1)) if len(g_vals) > 24 else sd
    
    return {
        'mean_glucose': mu,
        'sd_glucose': sd,
        'cv_glucose': cv,
        'tir_70_180': tir,
        'tar1_181_250': tar1,
        'tar2_over_250': tar2,
        'tbr1_54_69': tbr1,
        'tbr2_under_54': tbr2,
        'mag_change': mag,
        'lbgi': lbgi,
        'hbgi': hbgi,
        'mage': mage,
        'conga1': conga1,
        'conga2': conga2
    }

def process_patient_diurnal_advanced(args):
    pdir, person_meta = args
    pid = int(pdir.replace('AIREADI-', '')) if 'AIREADI-' in pdir else int(pdir)
    if pid not in person_meta:
        return [], None, None
        
    p_info = person_meta[pid]
    json_files = glob.glob(os.path.join(CGM_DIR, pdir, "*.json"))
    if not json_files:
        return [], None, None
        
    try:
        with open(json_files[0], 'r') as f:
            data = json.load(f)
        readings = data.get('body', {}).get('cgm', [])
        if not readings:
            return [], None, None
            
        records = []
        for r in readings:
            v = parse_glucose_val(r.get('blood_glucose', {}).get('value'))
            t_str = r.get('effective_time_frame', {}).get('time_interval', {}).get('start_date_time') or r.get('effective_time_frame', {}).get('time_interval', {}).get('start_time') or r.get('start_time')
            if v is not None and t_str is not None:
                records.append({'time': pd.to_datetime(t_str), 'glucose': v})
                
        if len(records) < 864:
            return [], None, None
            
        df_p = pd.DataFrame(records).sort_values('time').drop_duplicates(subset=['time']).reset_index(drop=True)
        
        # Resample onto clean 5-minute grid
        df_p.set_index('time', inplace=True)
        df_p = df_p.resample('5min').mean()
        df_p['glucose'] = df_p['glucose'].interpolate(method='linear', limit=3)
        df_p.dropna(subset=['glucose'], inplace=True)
        df_p.reset_index(inplace=True)
        
        df_p['hour'] = df_p['time'].dt.hour
        df_p['day_of_week'] = df_p['time'].dt.dayofweek
        df_p['is_weekend'] = df_p['day_of_week'].isin([5, 6]).astype(int)
        df_p['date'] = df_p['time'].dt.date
        
        g_all = df_p['glucose'].values
        p_mean = float(np.mean(g_all))
        p_sd = float(np.std(g_all, ddof=1)) if len(g_all) > 1 else 1.0
        thresh_2sd = p_mean + 2.0 * p_sd
        
        df_p['is_spike_140'] = (df_p['glucose'] >= 140.0).astype(int)
        df_p['is_spike_2sd'] = (df_p['glucose'] >= thresh_2sd).astype(int)
        
        # Hourly 168-grid records
        h_records = []
        for (dow, hr), grp in df_p.groupby(['day_of_week', 'hour']):
            h_records.append({
                'person_id': pid,
                'study_group': p_info.get('study_group', 'healthy'),
                'is_diabetic': p_info.get('is_diabetic', 0),
                'day_of_week': dow,
                'hour': hr,
                'is_weekend': int(dow in [5, 6]),
                'mean_glucose': float(grp['glucose'].mean()),
                'spike_prob_140': float(grp['is_spike_140'].mean()),
                'spike_prob_2sd': float(grp['is_spike_2sd'].mean()),
            })
            
        df_wd = df_p[df_p['is_weekend'] == 0]
        df_we = df_p[df_p['is_weekend'] == 1]
        
        if len(df_wd) < 50 or len(df_we) < 20:
            return h_records, None, None
            
        # 15-Metric Battery overall, weekday, weekend
        batt_overall = compute_15_metric_battery(g_all)
        batt_wd = compute_15_metric_battery(df_wd['glucose'].values)
        batt_we = compute_15_metric_battery(df_we['glucose'].values)
        
        # Friday/Saturday Night Hypoglycemia (10 PM - 6 AM)
        df_frisat_night = df_p[(df_p['day_of_week'].isin([4, 5])) & (df_p['hour'].isin([22, 23, 0, 1, 2, 3, 4, 5]))]
        df_monwed_night = df_p[(df_p['day_of_week'].isin([0, 1, 2])) & (df_p['hour'].isin([22, 23, 0, 1, 2, 3, 4, 5]))]
        
        tbr1_frisat_night = float(np.sum((df_frisat_night['glucose'] >= 54) & (df_frisat_night['glucose'] < 70)) / len(df_frisat_night) * 100.0) if len(df_frisat_night) > 0 else 0.0
        tbr1_monwed_night = float(np.sum((df_monwed_night['glucose'] >= 54) & (df_monwed_night['glucose'] < 70)) / len(df_monwed_night) * 100.0) if len(df_monwed_night) > 0 else 0.0
        
        # Dawn Phenomenon Magnitude (6 AM - 9 AM mean minus 1 AM - 5 AM baseline)
        hourly_means = df_p.groupby('hour')['glucose'].mean()
        dawn_val = float(hourly_means.loc[6:8].mean() - hourly_means.loc[1:4].mean()) if (6 in hourly_means.index and 1 in hourly_means.index) else 0.0
        
        # Algorithmic Meal Peak & Eating Pattern Classifier
        daily_peak_counts = []
        clearance_rates = []
        
        for d, d_grp in df_p.groupby('date'):
            if len(d_grp) < 150:
                continue
            d_vals = d_grp['glucose'].values
            peaks, props = find_peaks(d_vals, prominence=15.0, distance=18)
            daily_peak_counts.append(len(peaks))
            
            for p in peaks:
                if p + 12 < len(d_vals):
                    decay_segment = d_vals[p:p+12]
                    if decay_segment[0] > decay_segment[-1] and decay_segment[-1] > 0:
                        rel_decay = decay_segment / decay_segment[0]
                        times_min = np.arange(len(rel_decay)) * 5.0
                        log_rel = np.log(np.maximum(rel_decay, 1e-3))
                        slope, _, _, _, _ = stats.linregress(times_min, log_rel)
                        if slope < 0:
                            clearance_rates.append(-slope)
                            
        avg_daily_peaks = float(np.mean(daily_peak_counts)) if len(daily_peak_counts) > 0 else 0.0
        avg_clearance_k = float(np.mean(clearance_rates)) if len(clearance_rates) > 0 else 0.015
        
        if avg_daily_peaks < 1.5:
            eating_pattern_label = "Intermittent/OAD"
        elif avg_daily_peaks < 2.5:
            eating_pattern_label = "2-Meal Eater"
        elif avg_daily_peaks <= 3.5:
            eating_pattern_label = "3-Meal Eater"
        else:
            eating_pattern_label = "Frequent Snacker"
            
        breakfast_peak = float(hourly_means.loc[7:9].max()) if 7 in hourly_means.index else p_mean
        lunch_peak = float(hourly_means.loc[12:14].max()) if 12 in hourly_means.index else p_mean
        dinner_peak = float(hourly_means.loc[18:20].max()) if 18 in hourly_means.index else p_mean
        overnight_baseline = float(hourly_means.loc[1:5].mean()) if 1 in hourly_means.index else p_mean
        meal_prominence = ((breakfast_peak - overnight_baseline) + (lunch_peak - overnight_baseline) + (dinner_peak - overnight_baseline)) / 3.0

        p_weekly = {
            'person_id': pid,
            'study_group': p_info.get('study_group', 'healthy'),
            'is_diabetic': p_info.get('is_diabetic', 0),
            'age': p_info.get('age', 60),
            'years_of_education': p_info.get('years_of_education', 14),
            'is_retired': int(p_info.get('age', 60) >= 65),
            'diet_score': p_info.get('diet_score', np.nan),
            'alcohol_freq': p_info.get('alcohol_freq', np.nan),
            'exercise_freq': p_info.get('exercise_freq', np.nan),
            'sleep_hours': p_info.get('sleep_hours', np.nan),
            'food_insecure': p_info.get('food_insecure', np.nan),
            'paid_distress': p_info.get('paid_distress', np.nan),
            
            # Overall 15-metric battery
            'mean_overall': batt_overall.get('mean_glucose', np.nan),
            'sd_overall': batt_overall.get('sd_glucose', np.nan),
            'cv_overall': batt_overall.get('cv_glucose', np.nan),
            'tir_overall': batt_overall.get('tir_70_180', np.nan),
            'tar1_overall': batt_overall.get('tar1_181_250', np.nan),
            'tar2_overall': batt_overall.get('tar2_over_250', np.nan),
            'tbr1_overall': batt_overall.get('tbr1_54_69', np.nan),
            'tbr2_overall': batt_overall.get('tbr2_under_54', np.nan),
            'mage_overall': batt_overall.get('mage', np.nan),
            'mag_overall': batt_overall.get('mag_change', np.nan),
            'hbgi_overall': batt_overall.get('hbgi', np.nan),
            'lbgi_overall': batt_overall.get('lbgi', np.nan),
            'conga1_overall': batt_overall.get('conga1', np.nan),
            
            # Weekday metrics
            'cv_weekday': batt_wd.get('cv_glucose', np.nan),
            'sd_weekday': batt_wd.get('sd_glucose', np.nan),
            'tir_weekday': batt_wd.get('tir_70_180', np.nan),
            'tar1_weekday': batt_wd.get('tar1_181_250', np.nan),
            'tbr1_weekday': batt_wd.get('tbr1_54_69', np.nan),
            
            # Weekend metrics
            'cv_weekend': batt_we.get('cv_glucose', np.nan),
            'sd_weekend': batt_we.get('sd_glucose', np.nan),
            'tir_weekend': batt_we.get('tir_70_180', np.nan),
            'tar1_weekend': batt_we.get('tar1_181_250', np.nan),
            'tbr1_weekend': batt_we.get('tbr1_54_69', np.nan),
            
            # Differences (Weekend minus Weekday)
            'delta_cv_weekend': batt_we.get('cv_glucose', 0.0) - batt_wd.get('cv_glucose', 0.0),
            'delta_sd_weekend': batt_we.get('sd_glucose', 0.0) - batt_wd.get('sd_glucose', 0.0),
            'delta_tir_weekend': batt_we.get('tir_70_180', 0.0) - batt_wd.get('tir_70_180', 0.0),
            
            # Special dynamic metrics
            'tbr1_frisat_night': tbr1_frisat_night,
            'tbr1_monwed_night': tbr1_monwed_night,
            'dawn_phenomenon_rise': dawn_val,
            'avg_daily_peaks': avg_daily_peaks,
            'clearance_rate_k': avg_clearance_k,
            'eating_pattern_label': eating_pattern_label,
            'meal_prominence': meal_prominence,
            'is_regular_3meal': int(eating_pattern_label == '3-Meal Eater')
        }
        return h_records, p_weekly, None
    except Exception as e:
        return [], None, None

def run_advanced_diurnal_weekly_analysis():
    print("Parallel extracting advanced diurnal & weekly 15-metric battery...")
    df_ext = pd.read_csv(CLINICAL_EXT_PATH)
    def is_diabetic_fn(sg):
        sg_l = str(sg).lower()
        if 'oral' in sg_l or 'insulin' in sg_l:
            return 1
        return 0
    df_ext['is_diabetic'] = df_ext['study_group'].apply(is_diabetic_fn)
    person_meta = df_ext.set_index('person_id').to_dict(orient='index')
    
    person_dirs = [d for d in os.listdir(CGM_DIR) if os.path.isdir(os.path.join(CGM_DIR, d))]
    tasks = [(pdir, person_meta) for pdir in person_dirs]
    
    n_workers = min(cpu_count(), 8)
    with Pool(n_workers) as pool:
        results = pool.map(process_patient_diurnal_advanced, tasks)
        
    hourly_records = []
    patient_weekly_records = []
    for h_recs, p_wk, _ in results:
        if h_recs:
            hourly_records.extend(h_recs)
        if p_wk:
            patient_weekly_records.append(p_wk)
            
    df_hourly = pd.DataFrame(hourly_records)
    df_weekly = pd.DataFrame(patient_weekly_records)
    
    df_hourly.to_csv(os.path.join(DATA_OUT_DIR, "diurnal_hourly_grid.csv"), index=False)
    df_weekly.to_csv(os.path.join(DATA_OUT_DIR, "weekday_vs_weekend_patient_summary.csv"), index=False)
    print(f"Extracted diurnal hourly grid ({len(df_hourly)} rows) & weekly patient summaries ({len(df_weekly)} patients).")
    
    # ─── 1. WEEKDAY vs WEEKEND PAIRED TESTS ─────────────────────────────
    print("\n" + "="*70)
    print(f"WEEKDAY vs WEEKEND GLYCEMIC MANAGEMENT (N={len(df_weekly)} PARTICIPANTS)")
    print("="*70)
    
    if len(df_weekly) > 0:
        t_cv, p_cv = stats.ttest_rel(df_weekly['cv_weekend'], df_weekly['cv_weekday'])
        w_cv, pw_cv = stats.wilcoxon(df_weekly['cv_weekend'], df_weekly['cv_weekday'])
        t_tir, p_tir = stats.ttest_rel(df_weekly['tir_weekend'], df_weekly['tir_weekday'])
        t_tar1, p_tar1 = stats.ttest_rel(df_weekly['tar1_weekend'], df_weekly['tar1_weekday'])
        
        print(f"Glucose CV:  Weekday={df_weekly['cv_weekday'].mean():.4f} vs Weekend={df_weekly['cv_weekend'].mean():.4f} | Paired t={t_cv:.3f}, p={p_cv:.2e} | Wilcoxon p={pw_cv:.2e}")
        print(f"TIR (70-180): Weekday={df_weekly['tir_weekday'].mean():.2f}% vs Weekend={df_weekly['tir_weekend'].mean():.2f}% | Paired t={t_tir:.3f}, p={p_tir:.2e}")
        print(f"TAR1 (181-250): Weekday={df_weekly['tar1_weekday'].mean():.2f}% vs Weekend={df_weekly['tar1_weekend'].mean():.2f}% | Paired t={t_tar1:.3f}, p={p_tar1:.2e}")
        
        # Stratified by Employment Status (Retired Age >= 65 vs Working Age < 65)
        print("\n" + "="*70)
        print("STRATIFIED WEEKDAY vs WEEKEND: WORKING AGE (<65) vs RETIRED AGE (>=65)")
        print("="*70)
        df_work = df_weekly[df_weekly['is_retired'] == 0]
        df_ret = df_weekly[df_weekly['is_retired'] == 1]
        
        t_work, p_work = stats.ttest_rel(df_work['cv_weekend'], df_work['cv_weekday'])
        t_ret, p_ret = stats.ttest_rel(df_ret['cv_weekend'], df_ret['cv_weekday'])
        
        print(f"Working Age (<65, N={len(df_work)}): Weekday CV={df_work['cv_weekday'].mean():.4f} vs Weekend CV={df_work['cv_weekend'].mean():.4f} | Paired t={t_work:.3f}, p={p_work:.2e}")
        print(f"Retired Age (>=65, N={len(df_ret)}): Working CV={df_ret['cv_weekday'].mean():.4f} vs Weekend CV={df_ret['cv_weekend'].mean():.4f} | Paired t={t_ret:.3f}, p={p_ret:.2e}")

        # ─── 2. MEAL TAXONOMY & DIET SCORE ───────────────────────────────────
        print("\n" + "="*70)
        print("INFERRED MEAL TAXONOMY & QUESTIONNAIRE DIET SCORE")
        print("="*70)
        tax_counts = df_weekly['eating_pattern_label'].value_counts()
        print("Inferred Eating Pattern Distribution:")
        print(tax_counts)
        
        df_diet = df_weekly.dropna(subset=['diet_score'])
        if len(df_diet) > 0:
            corr_pk_diet, p_pk_diet = stats.spearmanr(df_diet['avg_daily_peaks'], df_diet['diet_score'])
            corr_clr_diet, p_clr_diet = stats.spearmanr(df_diet['clearance_rate_k'], df_diet['diet_score'])
            print(f"Spearman Correlation: Daily Peaks vs Diet Score: rho={corr_pk_diet:.3f}, p={p_pk_diet:.4f}")
            print(f"Spearman Correlation: Postprandial Clearance (k) vs Diet Score: rho={corr_clr_diet:.3f}, p={p_clr_diet:.4f}")

    # ─── VISUALIZATIONS ──────────────────────────────────────────────────
    sns.set_theme(style="whitegrid")
    
    # Fig 4: Diurnal Trajectory & Meal Prominence
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    diurnal_profile = df_hourly.groupby(['hour', 'is_diabetic'])['mean_glucose'].mean().reset_index()
    sns.lineplot(data=diurnal_profile, x='hour', y='mean_glucose', hue='is_diabetic', ax=ax1, linewidth=2.5, palette=['#2ecc71', '#e74c3c'])
    ax1.set_title('Diurnal Glycemic Trajectory (24-Hour Profile)', fontsize=13, fontweight='bold')
    ax1.set_xlabel('Hour of Day (0-23)', fontsize=11)
    ax1.set_ylabel('Mean Glucose (mg/dL)', fontsize=11)
    ax1.set_xticks(range(0, 24, 2))
    ax1.axvspan(7, 9, color='gold', alpha=0.2, label='Breakfast Peak')
    ax1.axvspan(12, 14, color='orange', alpha=0.2, label='Lunch Peak')
    ax1.axvspan(18, 20, color='red', alpha=0.15, label='Dinner Peak')
    ax1.legend(loc='upper left', fontsize=9)
    
    if 'eating_pattern_label' in df_weekly.columns and len(df_weekly.dropna(subset=['diet_score'])) > 0:
        sns.boxplot(data=df_weekly.dropna(subset=['diet_score']), x='eating_pattern_label', y='diet_score', ax=ax2, palette='Set2')
        ax2.set_title('Diet Quality Score across Inferred Eating Taxonomy', fontsize=13, fontweight='bold')
        ax2.set_xlabel('Inferred Eating Pattern', fontsize=11)
        ax2.set_ylabel('Self-Reported Diet Quality Score', fontsize=11)
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_OUT_DIR, "fig4_inferred_meal_times_and_diet.png"), dpi=300)
    plt.close()

    # Fig 5: Weekday vs Weekend Volatility Stratified by Work Status
    if len(df_weekly) > 0:
        plt.figure(figsize=(10, 6))
        df_ww_plot = pd.melt(df_weekly, id_vars=['person_id', 'is_retired'], value_vars=['cv_weekday', 'cv_weekend'], var_name='Period', value_name='Glucose CV')
        df_ww_plot['Period'] = df_ww_plot['Period'].map({'cv_weekday': 'Weekday (Mon-Fri)', 'cv_weekend': 'Weekend (Sat-Sun)'})
        df_ww_plot['Employment Status'] = df_ww_plot['is_retired'].map({0: 'Working Age (<65)', 1: 'Retired Age (>=65)'})
        
        sns.boxplot(data=df_ww_plot, x='Period', y='Glucose CV', hue='Employment Status', palette=['#3498db', '#e67e22'])
        plt.title('Glycemic Volatility (CV) Weekday vs. Weekend by Work Status', fontsize=13, fontweight='bold')
        plt.ylabel('Glucose CV (SD / Mean)', fontsize=11)
        plt.tight_layout()
        plt.savefig(os.path.join(FIG_OUT_DIR, "fig5_weekday_vs_weekend_variability.png"), dpi=300)
        plt.close()

    # Fig 6: 168-Hour Weekly Grid Heatmap
    plt.figure(figsize=(12, 6))
    pivot_heatmap = df_hourly.pivot_table(index='day_of_week', columns='hour', values='mean_glucose', aggfunc='mean')
    dow_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    pivot_heatmap.index = dow_names
    sns.heatmap(pivot_heatmap, cmap='YlOrRd', annot=False, cbar_kws={'label': 'Mean Glucose (mg/dL)'})
    plt.title('168-Hour Weekly Glycemic Management Grid (Day of Week x Hour of Day)', fontsize=13, fontweight='bold')
    plt.xlabel('Hour of Day (0-23)', fontsize=11)
    plt.ylabel('Day of Week', fontsize=11)
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_OUT_DIR, "fig6_heatmap_day_hour_glycemia.png"), dpi=300)
    plt.close()
    print("Successfully saved all updated diurnal & weekly management figures.")

if __name__ == "__main__":
    run_advanced_diurnal_weekly_analysis()
