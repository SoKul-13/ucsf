import os
import json
import glob
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns

# Set paths relative to new research structure
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
WORKSPACE_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, ".."))
CGM_DIR = os.path.join(WORKSPACE_ROOT, "dataset", "wearable_blood_glucose", "continuous_glucose_monitoring", "dexcom_g6")
CLINICAL_EXT_PATH = os.path.join(PROJECT_ROOT, "data", "master_extended_dataset.csv")
MASTER_DATA_DIR = os.path.join(PROJECT_ROOT, "data")

REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports", "4_personalized_spike_analysis")
DATA_OUT_DIR = os.path.join(REPORTS_DIR, "data")
FIG_OUT_DIR = os.path.join(REPORTS_DIR, "figures")

os.makedirs(MASTER_DATA_DIR, exist_ok=True)
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

def extract_patient_personalized_spikes():
    print("Extracting raw CGM time-series & calculating personalized spike metrics...")
    
    person_dirs = [d for d in os.listdir(CGM_DIR) if os.path.isdir(os.path.join(CGM_DIR, d))]
    print(f"Found {len(person_dirs)} participant directories.")
    
    patient_records = []
    
    for pdir in person_dirs:
        person_path = os.path.join(CGM_DIR, pdir)
        json_files = [f for f in os.listdir(person_path) if f.endswith(".json")]
        if not json_files:
            continue
            
        json_file = os.path.join(person_path, json_files[0])
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                
            readings = data.get('body', {}).get('cgm', [])
            if not readings:
                continue
                
            vals = []
            times = []
            for r in readings:
                v = parse_glucose_val(r.get('blood_glucose', {}).get('value'))
                t = r.get('effective_time_frame', {}).get('time_interval', {}).get('start_date_time') or r.get('effective_time_frame', {}).get('time_interval', {}).get('start_time') or r.get('start_time')
                if v is not None and t is not None:
                    vals.append(v)
                    times.append(t)
                    
            if len(vals) < 864:  # Minimum 3 days of 5-min readings
                continue
                
            vals = np.array(vals)
            n_readings = len(vals)
            cgm_days = n_readings * 5.0 / 1440.0
            
            # Baseline stats
            mu = float(np.mean(vals))
            sigma = float(np.std(vals, ddof=1)) if len(vals) > 1 else 0.001
            cv = sigma / mu if mu > 0 else 0.0
            
            # Standardization Z_t = (G_t - mu) / sigma
            z_scores = (vals - mu) / sigma if sigma > 0 else np.zeros_like(vals)
            
            # Helper for contiguous spike run extraction
            def count_spikes_and_runs(threshold_condition):
                runs = []
                curr_run = []
                for idx, v in enumerate(vals):
                    if threshold_condition[idx]:
                        curr_run.append(v)
                    else:
                        if len(curr_run) > 0:
                            runs.append(curr_run)
                            curr_run = []
                if len(curr_run) > 0:
                    runs.append(curr_run)
                
                n_spikes = len(runs)
                spikes_per_day = n_spikes / cgm_days if cgm_days > 0 else 0.0
                pct_time = np.sum(threshold_condition) / n_readings * 100.0
                peaks = [np.max(r) for r in runs] if n_spikes > 0 else [0.0]
                avg_peak = float(np.mean(peaks))
                return n_spikes, spikes_per_day, pct_time, avg_peak

            # 1. Traditional >140 mg/dL
            spikes_140, rate_140, pct_140, peak_140 = count_spikes_and_runs(vals >= 140.0)
            
            # 2. Personalized > 2 SD (Z >= 2.0)
            thresh_2sd = mu + 2.0 * sigma
            spikes_2sd, rate_2sd, pct_2sd, peak_2sd = count_spikes_and_runs(vals >= thresh_2sd)
            
            # 3. Personalized > 1.5 SD (Z >= 1.5)
            thresh_1_5sd = mu + 1.5 * sigma
            spikes_1_5sd, rate_1_5sd, pct_1_5sd, peak_1_5sd = count_spikes_and_runs(vals >= thresh_1_5sd)
            
            # 4. Personalized > 2.5 SD (Z >= 2.5)
            thresh_2_5sd = mu + 2.5 * sigma
            spikes_2_5sd, rate_2_5sd, pct_2_5sd, peak_2_5sd = count_spikes_and_runs(vals >= thresh_2_5sd)

            pid = int(pdir.replace('AIREADI-', '')) if 'AIREADI-' in pdir else int(pdir)
            
            patient_records.append({
                'person_id': pid,
                'total_readings': n_readings,
                'cgm_days': cgm_days,
                'mean_glucose': mu,
                'sd_glucose': sigma,
                'cv_glucose': cv,
                'thresh_2sd_mg': thresh_2sd,
                # >140 mg/dL metrics
                'spikes_140_count': spikes_140,
                'spikes_140_per_day': rate_140,
                'pct_time_above_140': pct_140,
                'avg_peak_above_140': peak_140,
                'has_spike_140': int(spikes_140 > 0),
                # >2 SD metrics
                'spikes_2sd_count': spikes_2sd,
                'spikes_2sd_per_day': rate_2sd,
                'pct_time_above_2sd': pct_2sd,
                'avg_peak_above_2sd': peak_2sd,
                'has_spike_2sd': int(spikes_2sd > 0),
                # Sensitivity levels
                'spikes_1_5sd_per_day': rate_1_5sd,
                'pct_time_above_1_5sd': pct_1_5sd,
                'spikes_2_5sd_per_day': rate_2_5sd,
                'pct_time_above_2_5sd': pct_2_5sd,
            })
        except Exception as e:
            print(f"Error parsing {pdir}: {e}")
            
    df_spikes = pd.DataFrame(patient_records)
    print(f"Successfully calculated metrics for {len(df_spikes)} patients.")
    return df_spikes

def analyze_coverage_and_correlations():
    df_spikes = extract_patient_personalized_spikes()
    df_ext = pd.read_csv(CLINICAL_EXT_PATH)
    
    # Merge with clinical data
    df_merged = df_ext.merge(df_spikes, on='person_id', how='inner')
    
    # Define diabetic status binary flag
    def is_diabetic_fn(sg):
        sg_l = str(sg).lower()
        if 'oral' in sg_l or 'insulin' in sg_l:
            return 1
        return 0
        
    df_merged['is_diabetic'] = df_merged['study_group'].apply(is_diabetic_fn)
    df_merged['cognitively_impaired'] = (df_merged['moca_total'] < 26).astype(float)
    df_merged['elevated_depression'] = (df_merged['depression_score'] >= 10).astype(float)
    
    # Save master dataset with personalized spikes
    df_merged.to_csv(os.path.join(DATA_OUT_DIR, "personalized_spike_metrics.csv"), index=False)
    df_merged.to_csv(os.path.join(MASTER_DATA_DIR, "personalized_spike_metrics.csv"), index=False)
    print(f"Saved merged dataset ({len(df_merged)} rows) to personalized_spike_metrics.csv")
    
    # ─── 1. COVERAGE ANALYSIS ───────────────────────────────────────────
    print("\n" + "="*70)
    print("COVERAGE EVALUATION: ABSOLUTE (>140 mg/dL) vs PERSONALIZED (>2 SD)")
    print("="*70)
    
    groups = df_merged['study_group'].unique()
    coverage_rows = []
    
    for grp in groups:
        sub = df_merged[df_merged['study_group'] == grp]
        n_grp = len(sub)
        
        cov_140 = np.mean(sub['has_spike_140']) * 100.0
        cov_2sd = np.mean(sub['has_spike_2sd']) * 100.0
        
        rate_140_mean = sub['spikes_140_per_day'].mean()
        rate_2sd_mean = sub['spikes_2sd_per_day'].mean()
        
        pct_140_mean = sub['pct_time_above_140'].mean()
        pct_2sd_mean = sub['pct_time_above_2sd'].mean()
        
        cv_mean = sub['cv_glucose'].mean()
        
        coverage_rows.append({
            'study_group': grp,
            'N': n_grp,
            'coverage_pct_140': cov_140,
            'coverage_pct_2sd': cov_2sd,
            'spikes_140_per_day': rate_140_mean,
            'spikes_2sd_per_day': rate_2sd_mean,
            'pct_time_140': pct_140_mean,
            'pct_time_2sd': pct_2sd_mean,
            'mean_cv': cv_mean
        })
        
    df_cov = pd.DataFrame(coverage_rows)
    print(df_cov.to_string(index=False))
    
    # Save coverage summary CSV
    df_cov.to_csv(os.path.join(DATA_OUT_DIR, "coverage_comparison_summary.csv"), index=False)
    
    # Plot Coverage comparison
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="whitegrid")
    
    group_order = ['healthy', 'pre_diabetes_lifestyle_controlled', 'oral_medication_and_or_non_insulin_injectable_medication_controlled', 'insulin_dependent']
    group_labels = ['Healthy', 'Pre-Diabetes', 'T2D (Oral/Inj)', 'Insulin Dependent']
    
    cov_plot_df = []
    for g, l in zip(group_order, group_labels):
        sub = df_merged[df_merged['study_group'] == g]
        cov_plot_df.append({'Cohort': l, 'Definition': 'Traditional (>140 mg/dL)', 'Spikes / Day': sub['spikes_140_per_day'].mean(), 'Coverage %': (sub['has_spike_140'].mean()*100)})
        cov_plot_df.append({'Cohort': l, 'Definition': 'Personalized (>2 SD)', 'Spikes / Day': sub['spikes_2sd_per_day'].mean(), 'Coverage %': (sub['has_spike_2sd'].mean()*100)})
    df_cov_plot = pd.DataFrame(cov_plot_df)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    sns.barplot(data=df_cov_plot, x='Cohort', y='Coverage %', hue='Definition', ax=ax1, palette=['#e74c3c', '#2ecc71'])
    ax1.set_title('Patient Coverage (% Patients with >= 1 Spike)', fontsize=13, fontweight='bold')
    ax1.set_ylabel('% Patients Flagged with Spikes', fontsize=11)
    ax1.set_ylim(0, 110)
    for p in ax1.patches:
        height = p.get_height()
        if height > 0:
            ax1.annotate(f'{height:.1f}%', (p.get_x() + p.get_width() / 2., height / 2.),
                         ha='center', va='center', fontsize=9, color='white', fontweight='bold')
                         
    sns.barplot(data=df_cov_plot, x='Cohort', y='Spikes / Day', hue='Definition', ax=ax2, palette=['#e74c3c', '#2ecc71'])
    ax2.set_title('Average Spike Events / Day Across Cohorts', fontsize=13, fontweight='bold')
    ax2.set_ylabel('Mean Spikes per Day', fontsize=11)
    
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_OUT_DIR, "fig1_spike_definition_coverage.png"), dpi=300)
    plt.close()
    print("Saved figure: fig1_spike_definition_coverage.png")

    # ─── 2. CLINICAL & PSYCHOLOGICAL CORRELATIONS & DETAILED OLS REGRESSIONS ────
    print("\n" + "="*70)
    print("CORRELATION ANALYSIS & DETAILED OLS REGRESSION MODELS")
    print("="*70)
    
    targets = {
        'Diabetic Status': 'is_diabetic',
        'MoCA Total Score': 'moca_total',
        'Depression CESD-10': 'depression_score'
    }
    
    predictors = [
        ('Traditional Spikes / Day (>140 mg/dL)', 'spikes_140_per_day'),
        ('Traditional % Time >140 mg/dL', 'pct_time_above_140'),
        ('Personalized Spikes / Day (>2 SD)', 'spikes_2sd_per_day'),
        ('Personalized % Time >2 SD', 'pct_time_above_2sd'),
        ('Glucose Variability CV (SD/Mean)', 'cv_glucose')
    ]
    
    corr_results = []
    ols_table_rows = []
    
    for t_name, t_col in targets.items():
        sub_df = df_merged.dropna(subset=[t_col])
        for p_name, p_col in predictors:
            sub_clean = sub_df.dropna(subset=[p_col])
            
            # Pearson & Spearman
            r_p, p_val_p = stats.pearsonr(sub_clean[p_col], sub_clean[t_col])
            r_s, p_val_s = stats.spearmanr(sub_clean[p_col], sub_clean[t_col])
            
            # 1. Unadjusted Model
            formula_unadj = f"{t_col} ~ {p_col}"
            try:
                mod_unadj = smf.ols(formula_unadj, data=sub_clean).fit()
                for var in mod_unadj.params.index:
                    coef = mod_unadj.params[var]
                    se = mod_unadj.bse[var]
                    pval = mod_unadj.pvalues[var]
                    sig = '***' if pval < 0.001 else ('**' if pval < 0.01 else ('*' if pval < 0.05 else ('.' if pval < 0.1 else '')))
                    ols_table_rows.append({
                        'Outcome': t_name,
                        'Model_Type': 'Unadjusted (Simple Regression)',
                        'Predictor_Label': p_name,
                        'Predictor_Col': p_col,
                        'Term': var,
                        'Coefficient': coef,
                        'Std_Error': se,
                        'Margin_2SE': 2.0 * se,
                        't_value': mod_unadj.tvalues[var],
                        'p_value': pval,
                        'Significance': sig,
                        'N_obs': mod_unadj.nobs,
                        'R_squared': mod_unadj.rsquared,
                        'Adj_R_squared': mod_unadj.rsquared_adj,
                        'F_stat': mod_unadj.fvalue,
                        'F_pvalue': mod_unadj.f_pvalue,
                        'RSE': np.sqrt(mod_unadj.mse_resid),
                        'df_resid': mod_unadj.df_resid
                    })
            except Exception as e:
                pass
                
            # 2. Adjusted Model (controlling for Age, BMI, Education)
            formula_adj = f"{t_col} ~ {p_col} + age + bmi + years_of_education"
            sub_adj = sub_clean.dropna(subset=['age', 'bmi', 'years_of_education'])
            try:
                mod_adj = smf.ols(formula_adj, data=sub_adj).fit()
                beta = mod_adj.params[p_col]
                beta_p = mod_adj.pvalues[p_col]
                r2 = mod_adj.rsquared
                
                for var in mod_adj.params.index:
                    coef = mod_adj.params[var]
                    se = mod_adj.bse[var]
                    pval = mod_adj.pvalues[var]
                    sig = '***' if pval < 0.001 else ('**' if pval < 0.01 else ('*' if pval < 0.05 else ('.' if pval < 0.1 else '')))
                    ols_table_rows.append({
                        'Outcome': t_name,
                        'Model_Type': 'Adjusted (+ Age, BMI, Education)',
                        'Predictor_Label': p_name,
                        'Predictor_Col': p_col,
                        'Term': var,
                        'Coefficient': coef,
                        'Std_Error': se,
                        'Margin_2SE': 2.0 * se,
                        't_value': mod_adj.tvalues[var],
                        'p_value': pval,
                        'Significance': sig,
                        'N_obs': mod_adj.nobs,
                        'R_squared': mod_adj.rsquared,
                        'Adj_R_squared': mod_adj.rsquared_adj,
                        'F_stat': mod_adj.fvalue,
                        'F_pvalue': mod_adj.f_pvalue,
                        'RSE': np.sqrt(mod_adj.mse_resid),
                        'df_resid': mod_adj.df_resid
                    })
            except Exception as e:
                beta, beta_p, r2 = np.nan, np.nan, np.nan
                
            corr_results.append({
                'Target': t_name,
                'Predictor': p_name,
                'Pearson_r': r_p,
                'Pearson_pval': p_val_p,
                'Spearman_rho': r_s,
                'Spearman_pval': p_val_s,
                'Adjusted_Beta': beta,
                'Adjusted_Beta_pval': beta_p,
                'Model_R2': r2
            })
            
    df_corr = pd.DataFrame(corr_results)
    df_ols = pd.DataFrame(ols_table_rows)
    
    print("Exporting full OLS regression results CSV...")
    df_corr.to_csv(os.path.join(DATA_OUT_DIR, "clinical_correlations_summary.csv"), index=False)
    df_ols.to_csv(os.path.join(DATA_OUT_DIR, "full_ols_regression_results.csv"), index=False)
    print(f"Exported {len(df_ols)} detailed OLS regression term rows to full_ols_regression_results.csv.")
    
    # Heatmap of Pearson Correlations
    plt.figure(figsize=(10, 6))
    pivot_corr = df_corr.pivot(index='Predictor', columns='Target', values='Pearson_r')
    sns.heatmap(pivot_corr, annot=True, fmt=".3f", cmap="coolwarm", cbar=True, linewidths=0.5)
    plt.title("Pearson Correlation ($r$) of Glycemic Spike Metrics with Health Outcomes", fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_OUT_DIR, "fig2_clinical_correlation_comparison.png"), dpi=300)
    plt.close()
    print("Saved figure: fig2_clinical_correlation_comparison.png")

if __name__ == "__main__":
    analyze_coverage_and_correlations()
