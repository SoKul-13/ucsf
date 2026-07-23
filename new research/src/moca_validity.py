import pandas as pd
import numpy as np
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, "..", "dataset"))
CLINICAL_DIR = os.path.join(BASE_DIR, "clinical_data")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports", "1_baseline_replication")
os.makedirs(REPORTS_DIR, exist_ok=True)

def format_p(p_val):
    if pd.isna(p_val):
        return "NaN"
    if p_val < 0.001:
        return "**<0.001** ⭐"
    elif p_val < 0.05:
        return f"**{p_val:.4f}** ⭐"
    else:
        return f"{p_val:.4f}"

def bootstrap_test(df, group_col, target_col, iters=10000):
    group_1 = df[df[group_col] == 1][target_col].dropna().values
    group_0 = df[df[group_col] == 0][target_col].dropna().values
    
    if len(group_1) < 2 or len(group_0) < 2:
        return np.nan, len(group_1), len(group_0), np.nan, np.nan
        
    mean_diff_obs = group_0.mean() - group_1.mean()
    combined = np.concatenate([group_1, group_0])
    
    count = 0
    for _ in range(iters):
        np.random.shuffle(combined)
        g1_sim = combined[:len(group_1)]
        g0_sim = combined[len(group_1):]
        diff_sim = g0_sim.mean() - g1_sim.mean()
        if diff_sim >= mean_diff_obs:
            count += 1
            
    p_value = count / iters
    return p_value, len(group_1), len(group_0), group_1.mean(), group_0.mean()

def run_analysis(df, condition_col, report, title_suffix):
    report.append(f"\n# {title_suffix}")
    
    def get_interpretation(p_val):
        if pd.isna(p_val):
            return "N/A"
        if p_val < 0.05:
            return "Significant (Valid MoCA)"
        else:
            return "Not Significant"

    # Start the table
    report.append("\n| Stratification | Condition N | Mean MoCA (Cond) | No Condition N | Mean MoCA (No Cond) | P-value (1-sided) | Interpretation |")
    report.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")

    # Overall
    p, n1, n0, m1, m0 = bootstrap_test(df, condition_col, 'moca_total')
    interp = get_interpretation(p)
    m1_str = f"{m1:.2f}" if not pd.isna(m1) else "N/A"
    m0_str = f"{m0:.2f}" if not pd.isna(m0) else "N/A"
    report.append(f"| **Overall** | {n1} | {m1_str} | {n0} | {m0_str} | {format_p(p)} | {interp} |")
    
    # Stratified by Age
    median_age = df['age'].median()
    report.append("| **By Age** | - | - | - | - | - | - |")
    for label, sub_df in [('Below Median Age', df[df['age'] <= median_age]), ('Above Median Age', df[df['age'] > median_age])]:
        p, n1, n0, m1, m0 = bootstrap_test(sub_df, condition_col, 'moca_total')
        interp = get_interpretation(p)
        m1_str = f"{m1:.2f}" if not pd.isna(m1) else "N/A"
        m0_str = f"{m0:.2f}" if not pd.isna(m0) else "N/A"
        report.append(f"| {label} | {n1} | {m1_str} | {n0} | {m0_str} | {format_p(p)} | {interp} |")
        
    # Stratified by Diabetes Status
    report.append("| **By Diabetes Status** | - | - | - | - | - | - |")
    for group in sorted(df['group'].unique()):
        sub_df = df[df['group'] == group]
        p, n1, n0, m1, m0 = bootstrap_test(sub_df, condition_col, 'moca_total')
        interp = get_interpretation(p)
        m1_str = f"{m1:.2f}" if not pd.isna(m1) else "N/A"
        m0_str = f"{m0:.2f}" if not pd.isna(m0) else "N/A"
        report.append(f"| {group} | {n1} | {m1_str} | {n0} | {m0_str} | {format_p(p)} | {interp} |")
            
    # Stratified by Age and Diabetes Status
    report.append("| **By Age and Diabetes Status** | - | - | - | - | - | - |")
    for group in sorted(df['group'].unique()):
        for label, sub_df in [('Below Median Age', df[(df['group'] == group) & (df['age'] <= median_age)]), 
                              ('Above Median Age', df[(df['group'] == group) & (df['age'] > median_age)])]:
            p, n1, n0, m1, m0 = bootstrap_test(sub_df, condition_col, 'moca_total')
            interp = get_interpretation(p)
            m1_str = f"{m1:.2f}" if not pd.isna(m1) else "N/A"
            m0_str = f"{m0:.2f}" if not pd.isna(m0) else "N/A"
            report.append(f"| {group} - {label} | {n1} | {m1_str} | {n0} | {m0_str} | {format_p(p)} | {interp} |")

def main():
    print("Loading data...")
    df_cond = pd.read_csv(os.path.join(CLINICAL_DIR, "condition_occurrence.csv"), low_memory=False)
    df = pd.read_csv(os.path.join(DATA_DIR, "master_cgm_moca_dataset.csv"))
    
    # GROUP 1: The AI-READI Specific `mhoccur` Strings
    cog_codes = ['mhoccur_pd', 'mhoccur_ad', 'mhoccur_cogn', 'mhoccur_ms', 'mhoccur_cns']
    pattern = '|'.join(cog_codes)
    cond_df_ai = df_cond[df_cond['condition_source_value'].str.contains(pattern, case=False, na=False)]
    cog_ids_ai = cond_df_ai['person_id'].unique()
    
    # GROUP 2: The Exhaustive OMOP Concept IDs
    exhaustive_concepts = [
        378419,    # Alzheimer's
        381270,    # Parkinson's
        4182210,   # Dementia
        435308,    # Mild cognitive impairment
        443793,    # Dementia, unspecified type
        37311061,  # Mild neurocognitive disorder
        37311060,  # Major neurocognitive disorder
        4113999,   # Multiple sclerosis
        438727     # Encephalopathy
    ]
    cond_df_omop = df_cond[df_cond['condition_concept_id'].isin(exhaustive_concepts)]
    cog_ids_omop = cond_df_omop['person_id'].unique()
    
    df['has_cog_disease_ai_readi'] = df['person_id'].isin(cog_ids_ai).astype(int)
    df['has_cog_disease_exhaustive'] = df['person_id'].isin(cog_ids_omop).astype(int)
    df.dropna(subset=['moca_total'], inplace=True)
    
    group_map = {
        'healthy': '1_Controls',
        'pre_diabetes_lifestyle_controlled': '2_Pre-diabetes',
        'oral_medication_and_or_non_insulin_injectable_medication_controlled': '3_Medication-controlled',
        'insulin_dependent': '4_Insulin-dependent'
    }
    df['group'] = df['study_group'].map(group_map)
    
    report = []
    report.append("# MoCA Validity Analysis: Comparison of Cohort Definitions\n")
    report.append("## Understanding This Report")
    report.append("- **Condition N**: Number of unique patients identified as having a cognitive or neurodegenerative disease (e.g., Alzheimer's, Parkinson's).")
    report.append("- **No Condition N**: Number of unique patients without a documented cognitive disease.")
    report.append("- **Mean MoCA**: The average MoCA Total Score (`moca_total`) for the respective group. Lower scores indicate worse cognitive function (Maximum 30, Impairment < 26).")
    report.append("- **Permutation P-value (1-sided)**: We are testing the hypothesis that patients *without* the condition have significantly *higher* MoCA scores than patients *with* the condition. A significant p-value (p < 0.05 ⭐) proves that MoCA accurately reflects cognitive decline in that specific sub-population.\n")
    
    report.append(f"### Cohort Extraction Results")
    report.append(f"- AI-READI Strings (`has_cog_disease_ai_readi`) identified {len(df[df['has_cog_disease_ai_readi']==1])} patients with MoCA data.")
    report.append(f"- Exhaustive OMOP Concepts (`has_cog_disease_exhaustive`) identified {len(df[df['has_cog_disease_exhaustive']==1])} patients with MoCA data.\n")
    
    run_analysis(df, 'has_cog_disease_ai_readi', report, "Version A: AI-READI Specific (mhoccur strings)")
    report.append("\n---\n")
    run_analysis(df, 'has_cog_disease_exhaustive', report, "Version B: Exhaustive OMOP Concept IDs")

    out_file = os.path.join(REPORTS_DIR, "moca_validity_results.md")
    with open(out_file, "w") as f:
        f.write("\n".join(report))
        
    print(f"Report generated successfully as {out_file}")

if __name__ == "__main__":
    main()
