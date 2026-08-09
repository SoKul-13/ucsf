import os
import json
import glob
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from multiprocessing import Pool, cpu_count

# Set paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
CGM_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "dataset", "wearable_blood_glucose", "continuous_glucose_monitoring", "dexcom_g6"))
CLINICAL_EXT_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "new research", "data", "master_extended_dataset.csv"))
DATA_OUT_DIR = os.path.join(BASE_DIR, "data")
FIG_OUT_DIR = os.path.join(BASE_DIR, "figures")

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

def process_patient_diurnal(args):
    pdir, person_meta = args
    pid = int(pdir.replace('AIREADI-', '')) if 'AIREADI-' in pdir else int(pdir)
    if pid not in person_meta:
        return [], None
        
    p_info = person_meta[pid]
    json_files = glob.glob(os.path.join(CGM_DIR, pdir, "*.json"))
    if not json_files:
        return [], None
        
    try:
        with open(json_files[0], 'r') as f:
            data = json.load(f)
        readings = data.get('body', {}).get('cgm', [])
        if not readings:
            return [], None
            
        records = []
        for r in readings:
            v = parse_glucose_val(r.get('blood_glucose', {}).get('value'))
            t_str = r.get('effective_time_frame', {}).get('time_interval', {}).get('start_date_time') or r.get('effective_time_frame', {}).get('time_interval', {}).get('start_time') or r.get('start_time')
            if v is not None and t_str is not None:
                records.append({'time': pd.to_datetime(t_str), 'glucose': v})
                
        if len(records) < 864:
            return [], None
            
        df_p = pd.DataFrame(records).sort_values('time').drop_duplicates(subset=['time']).reset_index(drop=True)
        df_p['hour'] = df_p['time'].dt.hour
        df_p['day_of_week'] = df_p['time'].dt.dayofweek
        df_p['is_weekend'] = df_p['day_of_week'].isin([5, 6]).astype(int)
        
        p_mean = float(df_p['glucose'].mean())
        p_sd = float(df_p['glucose'].std()) if len(df_p) > 1 else 1.0
        thresh_2sd = p_mean + 2.0 * p_sd
        
        df_p['is_spike_140'] = (df_p['glucose'] >= 140.0).astype(int)
        df_p['is_spike_2sd'] = (df_p['glucose'] >= thresh_2sd).astype(int)
        
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
        
        p_weekly = None
        if len(df_wd) > 100 and len(df_we) > 50:
            mean_wd = float(df_wd['glucose'].mean())
            sd_wd = float(df_wd['glucose'].std())
            cv_wd = sd_wd / mean_wd if mean_wd > 0 else 0
            pct_140_wd = float(df_wd['is_spike_140'].mean() * 100.0)
            pct_2sd_wd = float(df_wd['is_spike_2sd'].mean() * 100.0)
            
            mean_we = float(df_we['glucose'].mean())
            sd_we = float(df_we['glucose'].std())
            cv_we = sd_we / mean_we if mean_we > 0 else 0
            pct_140_we = float(df_we['is_spike_140'].mean() * 100.0)
            pct_2sd_we = float(df_we['is_spike_2sd'].mean() * 100.0)
            
            hourly_means = df_p.groupby('hour')['glucose'].mean()
            breakfast_peak = float(hourly_means.loc[7:9].max()) if 7 in hourly_means.index else p_mean
            lunch_peak = float(hourly_means.loc[12:14].max()) if 12 in hourly_means.index else p_mean
            dinner_peak = float(hourly_means.loc[18:20].max()) if 18 in hourly_means.index else p_mean
            overnight_baseline = float(hourly_means.loc[1:5].mean()) if 1 in hourly_means.index else p_mean
            
            meal_prominence = ((breakfast_peak - overnight_baseline) + (lunch_peak - overnight_baseline) + (dinner_peak - overnight_baseline)) / 3.0
            
            p_weekly = {
                'person_id': pid,
                'study_group': p_info.get('study_group', 'healthy'),
                'is_diabetic': p_info.get('is_diabetic', 0),
                'diet_score': p_info.get('diet_score', np.nan),
                'mean_weekday': mean_wd,
                'sd_weekday': sd_wd,
                'cv_weekday': cv_wd,
                'pct_140_weekday': pct_140_wd,
                'pct_2sd_weekday': pct_2sd_wd,
                'mean_weekend': mean_we,
                'sd_weekend': sd_we,
                'cv_weekend': cv_we,
                'pct_140_weekend': pct_140_we,
                'pct_2sd_weekend': pct_2sd_we,
                'delta_cv_weekend': cv_we - cv_wd,
                'delta_sd_weekend': sd_we - sd_wd,
                'meal_prominence': meal_prominence,
                'is_regular_3meal': int(meal_prominence >= 15.0)
            }
        return h_records, p_weekly
    except Exception as e:
        return [], None

def analyze_diurnal_and_weekly_parallel():
    print("Parallel extracting diurnal & weekly CGM metrics...")
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
        results = pool.map(process_patient_diurnal, tasks)
        
    hourly_records = []
    patient_weekly_records = []
    for h_recs, p_wk in results:
        if h_recs:
            hourly_records.extend(h_recs)
        if p_wk:
            patient_weekly_records.append(p_wk)
            
    df_hourly = pd.DataFrame(hourly_records)
    df_weekly = pd.DataFrame(patient_weekly_records)
    
    df_hourly.to_csv(os.path.join(DATA_OUT_DIR, "diurnal_hourly_grid.csv"), index=False)
    df_weekly.to_csv(os.path.join(DATA_OUT_DIR, "weekday_vs_weekend_patient_summary.csv"), index=False)
    print(f"Extracted diurnal hourly grid ({len(df_hourly)} rows) & weekly patient summaries ({len(df_weekly)} patients).")
    
    # ─── 1. WEEKDAY vs WEEKEND STATISTICAL TESTS ───────────────────────
    print("\n" + "="*70)
    print("STATISTICAL ANALYSIS: WEEKDAY vs WEEKEND GLYCEMIC MANAGEMENT")
    print("="*70)
    
    t_cv, p_cv = stats.ttest_rel(df_weekly['cv_weekend'], df_weekly['cv_weekday'])
    w_cv, pw_cv = stats.wilcoxon(df_weekly['cv_weekend'], df_weekly['cv_weekday'])
    t_sd, p_sd = stats.ttest_rel(df_weekly['sd_weekend'], df_weekly['sd_weekday'])
    t_140, p_140 = stats.ttest_rel(df_weekly['pct_140_weekend'], df_weekly['pct_140_weekday'])
    t_2sd, p_2sd = stats.ttest_rel(df_weekly['pct_2sd_weekend'], df_weekly['pct_2sd_weekday'])
    
    print(f"Glucose CV (SD/Mean):  Weekday={df_weekly['cv_weekday'].mean():.4f} vs Weekend={df_weekly['cv_weekend'].mean():.4f} | Paired t-stat={t_cv:.3f}, p={p_cv:.2e} | Wilcoxon p={pw_cv:.2e}")
    print(f"Glucose SD (mg/dL):   Weekday={df_weekly['sd_weekday'].mean():.2f} vs Weekend={df_weekly['sd_weekend'].mean():.2f} | Paired t-stat={t_sd:.3f}, p={p_sd:.2e}")
    print(f"% Time >140 mg/dL:     Weekday={df_weekly['pct_140_weekday'].mean():.2f}% vs Weekend={df_weekly['pct_140_weekend'].mean():.2f}% | Paired t-stat={t_140:.3f}, p={p_140:.2e}")
    print(f"% Time >2 SD:          Weekday={df_weekly['pct_2sd_weekday'].mean():.2f}% vs Weekend={df_weekly['pct_2sd_weekend'].mean():.2f}% | Paired t-stat={t_2sd:.3f}, p={p_2sd:.2e}")

    # ─── 2. MEAL PATTERN vs SELF-REPORTED DIET ──────────────────────────
    print("\n" + "="*70)
    print("INFERRED MEAL REGULARITY vs QUESTIONNAIRE DIET SCORE")
    print("="*70)
    
    df_diet_clean = df_weekly.dropna(subset=['diet_score'])
    corr_meal_diet, p_diet = stats.spearmanr(df_diet_clean['meal_prominence'], df_diet_clean['diet_score'])
    print(f"Correlation between Inferred Meal Prominence and Questionnaire Diet Score: Spearman rho={corr_meal_diet:.3f}, p={p_diet:.4f}")
    
    mean_diet_reg = df_diet_clean[df_diet_clean['is_regular_3meal'] == 1]['diet_score'].mean()
    mean_diet_snack = df_diet_clean[df_diet_clean['is_regular_3meal'] == 0]['diet_score'].mean()
    t_diet, p_diet_t = stats.ttest_ind(df_diet_clean[df_diet_clean['is_regular_3meal'] == 1]['diet_score'],
                                        df_diet_clean[df_diet_clean['is_regular_3meal'] == 0]['diet_score'])
    print(f"Diet Score: Regular 3-Meal Eaters={mean_diet_reg:.2f} vs Frequent Snackers={mean_diet_snack:.2f} | t={t_diet:.3f}, p={p_diet_t:.4f}")

    # ─── VISUALIZATIONS ────────────────────────────────────────────────
    sns.set_theme(style="whitegrid")
    
    # Fig 4: Inferred Meal Times & Diet
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
    
    sns.boxplot(data=df_diet_clean, x='is_regular_3meal', y='diet_score', ax=ax2, palette=['#e67e22', '#3498db'])
    ax2.set_title('Questionnaire Diet Score by Inferred Meal Pattern', fontsize=13, fontweight='bold')
    ax2.set_xticklabels(['Frequent/Irregular Snacker', 'Regular 3-Meal Eater'])
    ax2.set_ylabel('Self-Reported Diet Quality Score', fontsize=11)
    
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_OUT_DIR, "fig4_inferred_meal_times_and_diet.png"), dpi=300)
    plt.close()
    print("Saved figure: fig4_inferred_meal_times_and_diet.png")

    # Fig 5: Weekday vs Weekend Variability
    plt.figure(figsize=(10, 6))
    df_ww_plot = pd.melt(df_weekly, id_vars=['person_id', 'is_diabetic'], value_vars=['cv_weekday', 'cv_weekend'], var_name='Period', value_name='Glucose CV')
    df_ww_plot['Period'] = df_ww_plot['Period'].map({'cv_weekday': 'Weekday (Mon-Fri)', 'cv_weekend': 'Weekend (Sat-Sun)'})
    
    sns.boxplot(data=df_ww_plot, x='Period', y='Glucose CV', hue='is_diabetic', palette=['#2ecc71', '#e74c3c'])
    plt.title('Glycemic Volatility (Glucose CV) Weekday vs. Weekend', fontsize=13, fontweight='bold')
    plt.ylabel('Glucose CV (SD / Mean)', fontsize=11)
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_OUT_DIR, "fig5_weekday_vs_weekend_variability.png"), dpi=300)
    plt.close()
    print("Saved figure: fig5_weekday_vs_weekend_variability.png")

    # Fig 6: 2D Heatmap of Day of Week x Hour of Day
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
    print("Saved figure: fig6_heatmap_day_hour_glycemia.png")

if __name__ == "__main__":
    analyze_diurnal_and_weekly_parallel()
