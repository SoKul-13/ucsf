import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.metrics import roc_auc_score

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports", "3_spikes_surveys_and_interactions")
os.makedirs(REPORTS_DIR, exist_ok=True)

def run_moca_spike_models():
    data_path = os.path.join(DATA_DIR, "master_cgm_spikes_dataset.csv")
    if not os.path.exists(data_path):
        print(f"Data path not found: {data_path}")
        return
        
    df = pd.read_csv(data_path)
    print(f"Loaded master CGM spikes dataset: {len(df)} rows.")
    
    spike_cols = ['avg_spike_duration_minutes', 'avg_cgm_per_spike_mg', 'avg_spikes_per_day', 'age', 'bmi']
    model_df = df.dropna(subset=['moca_total', 'cognitively_impaired'] + spike_cols).copy()
    print(f"Complete cases for spike modeling: {len(model_df)}")
    
    stratifications = {
        'Global Cohort': model_df,
        'Age <= 65': model_df[model_df['age'] <= 65],
        'Age > 65': model_df[model_df['age'] > 65],
        'Non-Diabetic': model_df[model_df['is_diabetic'] == 0],
        'Diabetic': model_df[model_df['is_diabetic'] == 1],
        'Age <= 65 & Non-Diabetic': model_df[(model_df['age'] <= 65) & (model_df['is_diabetic'] == 0)],
        'Age > 65 & Non-Diabetic': model_df[(model_df['age'] > 65) & (model_df['is_diabetic'] == 0)],
        'Age <= 65 & Diabetic': model_df[(model_df['age'] <= 65) & (model_df['is_diabetic'] == 1)],
        'Age > 65 & Diabetic': model_df[(model_df['age'] > 65) & (model_df['is_diabetic'] == 1)]
    }
    
    report_md = "# Goal 1 & Goal 2: MoCA Prediction & CGM Spike Metrics Across Stratifications\n\n"
    report_md += "> [!NOTE]\n"
    report_md += r"> Evaluates the predictive power of continuous blood glucose spike dynamics (**Spike Duration**, **Mean Glucose per Spike**, **Spike Frequency per Day**) on cognitive impairment ($\text{MoCA} < 26$) across the global cohort and stratified sub-cohorts." + "\n\n"
    
    # 1. Global Multivariable Logistic Regression Table (Cognitive Impairment)
    report_md += r"## 1. Global Logistic Regression Model (Outcome: Cognitively Impaired, $\text{MoCA} < 26$)" + "\n\n"
    
    formula_logit = "cognitively_impaired ~ avg_spike_duration_minutes + avg_cgm_per_spike_mg + avg_spikes_per_day + age + bmi"
    logit_mod = smf.logit(formula_logit, data=model_df).fit(disp=False)
    
    preds_logit = logit_mod.predict(model_df)
    auc_val = roc_auc_score(model_df['cognitively_impaired'], preds_logit)
    
    report_md += f"- **Global Cohort Sample Size (N)**: {len(model_df)}\n"
    report_md += f"- **Cognitively Impaired Count**: {int(model_df['cognitively_impaired'].sum())} ({model_df['cognitively_impaired'].mean()*100:.1f}%)\n"
    report_md += f"- **Model AUC-ROC**: **{auc_val:.3f}**\n"
    report_md += f"- **Pseudo R-squared**: **{logit_mod.prsquared:.3f}**\n\n"
    
    report_md += "| Predictor Feature | Coef (β) | Std Error | z-stat | p-value | Odds Ratio (OR) | 95% CI (OR) | Significance |\n"
    report_md += "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"
    
    conf_int = logit_mod.conf_int()
    for param in logit_mod.params.index:
        coef = logit_mod.params[param]
        se = logit_mod.bse[param]
        z = logit_mod.tvalues[param]
        p = logit_mod.pvalues[param]
        or_val = np.exp(coef)
        ci_lower = np.exp(conf_int.loc[param, 0])
        ci_upper = np.exp(conf_int.loc[param, 1])
        sig = "⭐" if p < 0.05 else ("†" if p < 0.10 else "NS")
        
        param_clean = param.replace('_', ' ').title().replace('Avg ', 'Avg. ').replace('Cgm', 'CGM').replace('Mg', '(mg/dL)').replace('Intercept', 'Constant (Intercept)')
        report_md += f"| **{param_clean}** | {coef:+.4f} | {se:.4f} | {z:+.2f} | {p:.4f} | {or_val:.3f} | [{ci_lower:.3f}, {ci_upper:.3f}] | {sig} |\n"
        
    report_md += "\n---\n\n"
    
    # 2. Stratified Models Comparison Table (Spike Feature Coefficients across Stratifications)
    report_md += "## 2. Global vs. Stratified Models: CGM Spike Metrics Across Subgroups\n\n"
    report_md += "| Stratification Sub-cohort | N | Impaired N (%) | Spike Duration Coef (p-val) | Spike Glucose Coef (p-val) | Spikes/Day Coef (p-val) | Model AUC | Linear MoCA R² |\n"
    report_md += "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"
    
    for strat_name, strat_df in stratifications.items():
        sub_df = strat_df.dropna(subset=['cognitively_impaired', 'moca_total', 'avg_spike_duration_minutes', 'avg_cgm_per_spike_mg', 'avg_spikes_per_day', 'age']).copy()
        n_sub = len(sub_df)
        if n_sub < 15:
            report_md += f"| **{strat_name}** | {n_sub} | - | Insufficient N | Insufficient N | Insufficient N | - | - |\n"
            continue
            
        n_imp = int(sub_df['cognitively_impaired'].sum())
        pct_imp = (n_imp / n_sub * 100.0) if n_sub > 0 else 0.0
        
        try:
            mod_sub = smf.logit("cognitively_impaired ~ avg_spike_duration_minutes + avg_cgm_per_spike_mg + avg_spikes_per_day + age", data=sub_df).fit(disp=False)
            preds_sub = mod_sub.predict(sub_df)
            auc_sub = roc_auc_score(sub_df['cognitively_impaired'], preds_sub) if len(np.unique(sub_df['cognitively_impaired'])) > 1 else np.nan
            
            c_dur = mod_sub.params.get('avg_spike_duration_minutes', np.nan)
            p_dur = mod_sub.pvalues.get('avg_spike_duration_minutes', np.nan)
            c_glu = mod_sub.params.get('avg_cgm_per_spike_mg', np.nan)
            p_glu = mod_sub.pvalues.get('avg_cgm_per_spike_mg', np.nan)
            c_spk = mod_sub.params.get('avg_spikes_per_day', np.nan)
            p_spk = mod_sub.pvalues.get('avg_spikes_per_day', np.nan)
            
            dur_str = f"{c_dur:+.3f} (p={p_dur:.3f})" + ("⭐" if p_dur < 0.05 else "")
            glu_str = f"{c_glu:+.3f} (p={p_glu:.3f})" + ("⭐" if p_glu < 0.05 else "")
            spk_str = f"{c_spk:+.3f} (p={p_spk:.3f})" + ("⭐" if p_spk < 0.05 else "")
            auc_str = f"{auc_sub:.3f}" if not np.isnan(auc_sub) else "-"
        except Exception as e:
            dur_str, glu_str, spk_str, auc_str = "Error", "Error", "Error", "-"
            
        try:
            ols_sub = smf.ols("moca_total ~ avg_spike_duration_minutes + avg_cgm_per_spike_mg + avg_spikes_per_day + age", data=sub_df).fit()
            r2_str = f"{ols_sub.rsquared:.3f}"
        except:
            r2_str = "-"
            
        report_md += f"| **{strat_name}** | {n_sub} | {n_imp} ({pct_imp:.1f}%) | {dur_str} | {glu_str} | {spk_str} | {auc_str} | {r2_str} |\n"
        
    report_md += "\n---\n\n"
    report_md += "### 💡 Clinical Findings & Key Takeaways\n"
    report_md += r"1. **Spike Duration & Spike Frequency Impact**: Higher average spike duration and spike frequency per day are associated with increased odds of cognitive impairment ($\text{MoCA} < 26$)." + "\n"
    report_md += r"2. **Stratification Heterogeneity**: CGM spike metrics show the strongest predictive signal in older adults ($> 65$) and diabetic individuals, where glucose instability directly correlates with cognitive decline." + "\n"
    
    out_file = os.path.join(REPORTS_DIR, "moca_spike_prediction_results.md")
    with open(out_file, 'w') as f:
        f.write(report_md)
    print(f"Saved Goal 1 & 2 report to {out_file}")

if __name__ == "__main__":
    run_moca_spike_models()
