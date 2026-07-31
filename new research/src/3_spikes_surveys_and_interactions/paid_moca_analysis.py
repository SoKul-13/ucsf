import os
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, "..", "dataset"))
CLINICAL_DIR = os.path.join(BASE_DIR, "clinical_data")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports", "3_spikes_surveys_and_interactions")
os.makedirs(REPORTS_DIR, exist_ok=True)

def run_paid_moca_analysis():
    print("Loading observation.csv for PAID-5 items...")
    df_obs = pd.read_csv(os.path.join(CLINICAL_DIR, "observation.csv"), low_memory=False)
    
    paid_vars = {
        'paid_dpr': 'PAID Q1 (Feeling Depressed)',
        'paid_scrd': 'PAID Q2 (Feeling Scared)',
        'paid_wr': 'PAID Q3 (Worrying About Complications)',
        'paid_eng': 'PAID Q4 (Takes Up Mental/Physical Energy)',
        'paid_cml': 'PAID Q5 (Coping With Complications)'
    }
    
    # Extract each PAID item
    paid_dfs = []
    for code, label in paid_vars.items():
        sub = df_obs[df_obs['observation_source_value'].astype(str).str.contains(code, case=False, na=False)].copy()
        if not sub.empty:
            item_val = sub.groupby('person_id')['value_as_number'].max().reset_index()
            item_val.rename(columns={'value_as_number': code}, inplace=True)
            paid_dfs.append(item_val)
            
    # Also total paidscore
    sub_tot = df_obs[df_obs['observation_source_value'].astype(str).str.contains('paidscore', case=False, na=False)].copy()
    if not sub_tot.empty:
        tot_val = sub_tot.groupby('person_id')['value_as_number'].max().reset_index()
        tot_val.rename(columns={'value_as_number': 'paidscore'}, inplace=True)
        paid_dfs.append(tot_val)
        
    # Merge all PAID items
    df_paid = paid_dfs[0]
    for d in paid_dfs[1:]:
        df_paid = df_paid.merge(d, on='person_id', how='outer')
        
    print(f"Extracted PAID items for {len(df_paid)} participants.")
    
    # Merge with MoCA total and master dataset
    master_path = os.path.join(DATA_DIR, "master_cgm_spikes_dataset.csv")
    if os.path.exists(master_path):
        df_master = pd.read_csv(master_path)
    else:
        df_master = pd.read_csv(os.path.join(DATA_DIR, "master_extended_dataset.csv"))
        
    df_analysis = df_master.merge(df_paid, on='person_id', how='inner')
    df_analysis = df_analysis.dropna(subset=['moca_total']).copy()
    print(f"Complete cases with MoCA and PAID survey data: {len(df_analysis)}")
    
    report_md = "# Goal 4: PAID-5 Diabetes Distress Survey Items vs. MoCA Scores\n\n"
    report_md += "> [!NOTE]\n"
    report_md += "> Evaluates the connection between diabetes distress (Problem Areas In Diabetes - PAID-5) and cognitive function ($\text{MoCA}$ total score). Each of the 5 survey questions is analyzed separately to compare differences in mean MoCA scores across distress levels.\n\n"
    
    report_md += "## 1. Item-Level PAID-5 Analysis (MoCA Score Differences Across Distress Levels)\n\n"
    
    # Iterate through each question
    for code, label in paid_vars.items():
        if code not in df_analysis.columns:
            continue
            
        sub_item = df_analysis.dropna(subset=[code, 'moca_total']).copy()
        if sub_item.empty:
            continue
            
        report_md += f"### 📌 {label} (`{code}`)\n\n"
        
        # Summary table by Likert response score (0 = No problem, 1 = Minor, 2 = Moderate, 3 = Somewhat serious, 4 = Serious)
        grp = sub_item.groupby(code)['moca_total'].agg(['count', 'mean', 'std', 'sem']).reset_index()
        
        report_md += "| Response Score (0-4) | Response Meaning | N | MoCA Mean | Std Dev | Std Error (SE) |\n"
        report_md += "| :---: | :--- | :---: | :---: | :---: | :---: |\n"
        
        score_labels = {
            0: "Not a problem (0)",
            1: "Minor problem (1)",
            2: "Moderate problem (2)",
            3: "Somewhat serious problem (3)",
            4: "Serious problem (4)"
        }
        
        for _, row in grp.iterrows():
            score_val = int(row[code])
            lbl = score_labels.get(score_val, f"Score {score_val}")
            report_md += f"| {score_val} | {lbl} | {int(row['count'])} | {row['mean']:.2f} | {row['std']:.2f} | {row['sem']:.2f} |\n"
            
        # Low Distress (0-1) vs High Distress (2-4) Welch's T-Test
        low_dist = sub_item[sub_item[code] <= 1]['moca_total']
        high_dist = sub_item[sub_item[code] >= 2]['moca_total']
        
        if len(low_dist) > 2 and len(high_dist) > 2:
            m_low = np.mean(low_dist)
            se_low = stats.sem(low_dist)
            m_high = np.mean(high_dist)
            se_high = stats.sem(high_dist)
            diff_m = m_low - m_high # Difference (Low distress MoCA - High distress MoCA)
            
            t_res = stats.ttest_ind(low_dist, high_dist, equal_var=False)
            spear_r, spear_p = stats.spearmanr(sub_item[code], sub_item['moca_total'])
            
            report_md += f"\n**Contrast Analysis: Low Distress (Score 0-1) vs. High Distress (Score 2-4)**\n"
            report_md += f"- **Low Distress MoCA Mean**: {m_low:.2f} (SE: {se_low:.2f}, N = {len(low_dist)})\n"
            report_md += f"- **High Distress MoCA Mean**: {m_high:.2f} (SE: {se_high:.2f}, N = {len(high_dist)})\n"
            report_md += f"- **Mean Difference (Low Distress - High Distress)**: **{diff_m:+.2f} points**\n"
            report_md += f"- **Welch's t-statistic**: {t_res.statistic:+.2f} (p-value: **{t_res.pvalue:.4f}**" + (" ⭐" if t_res.pvalue < 0.05 else "") + ")\n"
            report_md += f"- **Spearman Correlation**: ρ = {spear_r:.3f} (p-value: **{spear_p:.4f}**" + (" ⭐" if spear_p < 0.05 else "") + ")\n\n"
            
        report_md += "---\n\n"
        
    # 2. Overall PAID Score Summary
    if 'paidscore' in df_analysis.columns:
        sub_tot = df_analysis.dropna(subset=['paidscore', 'moca_total'])
        r_pear, p_pear = stats.pearsonr(sub_tot['paidscore'], sub_tot['moca_total'])
        r_spear, p_spear = stats.spearmanr(sub_tot['paidscore'], sub_tot['moca_total'])
        
        report_md += "## 2. Total PAID Score vs. MoCA Cognitive Score\n\n"
        report_md += f"- **Total Participants Analyzed**: N = {len(sub_tot)}\n"
        report_md += f"- **Pearson Correlation (r)**: **{r_pear:.3f}** (p-value: **{p_pear:.4f}**" + (" ⭐" if p_pear < 0.05 else "") + ")\n"
        report_md += f"- **Spearman Rank Correlation (ρ)**: **{r_spear:.3f}** (p-value: **{p_spear:.4f}**" + (" ⭐" if p_spear < 0.05 else "") + ")\n\n"
        
    out_file = os.path.join(REPORTS_DIR, "paid_moca_item_analysis.md")
    with open(out_file, 'w') as f:
        f.write(report_md)
    print(f"Saved Goal 4 report to {out_file}")

if __name__ == "__main__":
    run_paid_moca_analysis()
