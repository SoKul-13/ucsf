import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr

def format_p(p_val):
    if pd.isna(p_val):
        return "NaN"
    if p_val < 0.001:
        return "**<0.001** ⭐"
    elif p_val < 0.05:
        return f"**{p_val:.3f}** ⭐"
    else:
        return f"{p_val:.3f}"

def calculate_correlations(df, var1, var2):
    # drop nas for these two
    sub = df[[var1, var2]].dropna()
    if len(sub) < 3:
        return np.nan, np.nan, np.nan, np.nan, len(sub)
        
    p_corr, p_pval = pearsonr(sub[var1], sub[var2])
    s_corr, s_pval = spearmanr(sub[var1], sub[var2])
    
    return p_corr, p_pval, s_corr, s_pval, len(sub)

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports", "2_advanced_causal_and_survey")
os.makedirs(REPORTS_DIR, exist_ok=True)

def run_correlation_analysis():
    df = pd.read_csv(os.path.join(DATA_DIR, "master_extended_dataset.csv"))
    
    df['is_diabetic'] = df['study_group'] != 'healthy'
    df['age_over_65'] = df['age'] > 65
    
    comparisons = [
        ('moca_total', 'hba1c', 'MoCA vs HbA1c'),
        ('moca_total', 'mean_glucose', 'MoCA vs Mean Glucose')
    ]
    
    report = ["# Correlation Analysis"]
    report.append("\nThis report evaluates the direct linear (Pearson) and monotonic (Spearman) correlation between cognitive impairment and glycaemic metrics, stratified by sub-cohorts.\n")
    
    for v1, v2, label in comparisons:
        report.append(f"## {label}")
        report.append("| Stratification | N | Pearson *r* | Pearson p-value | Spearman *rho* | Spearman p-value |")
        report.append("| --- | --- | --- | --- | --- | --- |")
        
        # Overall
        p_c, p_p, s_c, s_p, n = calculate_correlations(df, v1, v2)
        report.append(f"| **Overall Cohort** | {n} | {p_c:.3f} | {format_p(p_p)} | {s_c:.3f} | {format_p(s_p)} |")
        
        # Age
        for is_over_65 in [False, True]:
            sub = df[df['age_over_65'] == is_over_65]
            lbl = "Age > 65" if is_over_65 else "Age <= 65"
            p_c, p_p, s_c, s_p, n = calculate_correlations(sub, v1, v2)
            report.append(f"| {lbl} | {n} | {p_c:.3f} | {format_p(p_p)} | {s_c:.3f} | {format_p(s_p)} |")
            
        # Diabetes
        for is_diab in [False, True]:
            sub = df[df['is_diabetic'] == is_diab]
            lbl = "Diabetic" if is_diab else "Healthy (Non-Diab)"
            p_c, p_p, s_c, s_p, n = calculate_correlations(sub, v1, v2)
            report.append(f"| {lbl} | {n} | {p_c:.3f} | {format_p(p_p)} | {s_c:.3f} | {format_p(s_p)} |")
            
        report.append("\n")
        
    out_file = os.path.join(REPORTS_DIR, "correlation_results.md")
    with open(out_file, "w") as f:
        f.write("\n".join(report))
        
    print(f"Saved {out_file}")

if __name__ == "__main__":
    run_correlation_analysis()
