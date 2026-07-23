import pandas as pd
import numpy as np

def bootstrap_test(val_true, val_false, iterations=10000):
    val_true = val_true.dropna()
    val_false = val_false.dropna()
    
    n_true = len(val_true)
    n_false = len(val_false)
    
    if n_true < 5 or n_false < 5:
        return np.nan, np.nan, np.nan
        
    actual_diff = val_false.mean() - val_true.mean()
    pooled = np.concatenate([val_true.values, val_false.values])
    
    count_greater = 0
    for _ in range(iterations):
        np.random.shuffle(pooled)
        sim_false = pooled[:n_false]
        sim_true = pooled[n_false:]
        sim_diff = sim_false.mean() - sim_true.mean()
        if sim_diff >= actual_diff:
            count_greater += 1
            
    p_val = count_greater / iterations
    return val_true.mean(), val_false.mean(), p_val

def format_p(p_val):
    if pd.isna(p_val):
        return "NaN"
    if p_val < 0.001:
        return "**<0.001** ⭐"
    elif p_val < 0.05:
        return f"**{p_val:.3f}** ⭐"
    else:
        return f"{p_val:.3f}"

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports", "2_advanced_causal_and_survey")
os.makedirs(REPORTS_DIR, exist_ok=True)

def run_survey_bootstrap():
    df = pd.read_csv(os.path.join(DATA_DIR, "master_extended_dataset.csv"))
    df.dropna(subset=['moca_total'], inplace=True)
    
    # 777 usually means refused/don't know in NHANES/AIREADI
    for col in ['smoked_100_cigs', 'consumed_alcohol', 'used_marijuana', 'used_vape']:
        df[col] = df[col].replace(777, np.nan)
        
    df['depression_high'] = df['depression_score'] >= 10
    
    diet_median = df['diet_score'].median()
    df['diet_healthy'] = df['diet_score'] > diet_median
    
    # Stratifications
    df['is_diabetic'] = df['study_group'] != 'healthy'
    df['age_over_65'] = df['age'] > 65
    
    survey_cols = {
        'depression_high': 'CESD-10 (Depression >= 10)',
        'diet_healthy': f'Diet Score (>{diet_median:.0f})',
        'smoked_100_cigs': 'Smoked >= 100 Cigs',
        'consumed_alcohol': 'Consumed Alcohol',
        'used_marijuana': 'Used Marijuana',
        'used_vape': 'Used Vape'
    }
    
    report = []
    report.append("# Survey Outcomes: Stratified Bootstrap Analysis (MoCA)")
    report.append("\nThis runs a 10,000-iteration difference in means permutation test comparing MoCA scores between survey responses, stratified by Age and Diabetes status.\n")
    
    for col, label in survey_cols.items():
        report.append(f"## {label}")
        report.append("| Stratification | N (Yes) | MoCA Mean (Yes) | N (No) | MoCA Mean (No) | p-value |")
        report.append("| --- | --- | --- | --- | --- | --- |")
        
        # Base cohort
        moca_yes = df[df[col] == 1]['moca_total']
        moca_no = df[df[col] == 0]['moca_total']
        m_y, m_n, p = bootstrap_test(moca_yes, moca_no)
        report.append(f"| **Overall Cohort** | {len(moca_yes)} | {m_y:.2f} | {len(moca_no)} | {m_n:.2f} | {format_p(p)} |")
        
        # Stratify by Diabetes
        for is_diab in [False, True]:
            sub = df[df['is_diabetic'] == is_diab]
            lbl = "Diabetic" if is_diab else "Healthy (Non-Diab)"
            moca_yes = sub[sub[col] == 1]['moca_total']
            moca_no = sub[sub[col] == 0]['moca_total']
            m_y, m_n, p = bootstrap_test(moca_yes, moca_no)
            if not pd.isna(p):
                report.append(f"| {lbl} | {len(moca_yes)} | {m_y:.2f} | {len(moca_no)} | {m_n:.2f} | {format_p(p)} |")
                
        # Stratify by Age
        for is_over_65 in [False, True]:
            sub = df[df['age_over_65'] == is_over_65]
            lbl = "Age > 65" if is_over_65 else "Age <= 65"
            moca_yes = sub[sub[col] == 1]['moca_total']
            moca_no = sub[sub[col] == 0]['moca_total']
            m_y, m_n, p = bootstrap_test(moca_yes, moca_no)
            if not pd.isna(p):
                report.append(f"| {lbl} | {len(moca_yes)} | {m_y:.2f} | {len(moca_no)} | {m_n:.2f} | {format_p(p)} |")
                
        report.append("\n")
        
    out_file = os.path.join(REPORTS_DIR, "survey_bootstrap_results.md")
    with open(out_file, "w") as f:
        f.write("\n".join(report))
        
    print(f"Saved {out_file}")

if __name__ == "__main__":
    run_survey_bootstrap()
