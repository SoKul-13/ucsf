import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import f_oneway, chi2_contingency

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports", "1_baseline_replication")
os.makedirs(REPORTS_DIR, exist_ok=True)

def format_p(p_val):
    if pd.isna(p_val):
        return "NaN"
    if p_val < 0.001:
        return "**<0.001** ⭐"
    elif p_val < 0.05:
        return f"**{p_val:.3f}** ⭐"
    else:
        return f"{p_val:.3f}"

def generate_report():
    df = pd.read_csv(os.path.join(DATA_DIR, "master_cgm_moca_dataset.csv"))
    
    # Map groups
    group_map = {
        'healthy': '1_Controls',
        'pre_diabetes_lifestyle_controlled': '2_Pre-diabetes',
        'oral_medication_and_or_non_insulin_injectable_medication_controlled': '3_Medication-controlled',
        'insulin_dependent': '4_Insulin-dependent'
    }
    df['group'] = df['study_group'].map(group_map)
    df.dropna(subset=['group', 'moca_total'], inplace=True)
    
    # Impute missing values with median/mode to keep the sample size up if any (for covariates)
    for col in ['age', 'bmi', 'gmi', 'mean_glucose', 'tir']:
        df[col] = df[col].fillna(df[col].median())
    for col in ['education_level']:
        df[col] = df[col].fillna(df[col].mode()[0])
        
    df['cognitive_impairment'] = (df['moca_total'] < 26).astype(int)
    
    groups = sorted(df['group'].unique())
    
    report = []
    report.append("# Statistical Analysis Replication: Cognitive Impairment and CGM Metrics")
    report.append("\nThis report replicates the findings of the AI-READI paper using CGM metrics (GMI) instead of HbA1c.\n")
    
    # Table 1
    report.append("## Table 1: Participant Characteristics\n")
    report.append("| Characteristic | " + " | ".join(groups) + " | p-value |")
    report.append("| --- | " + " | ".join(["---"] * len(groups)) + " | --- |")
    
    # N
    counts = df.groupby('group').size()
    report.append("| N | " + " | ".join(map(str, [counts[g] for g in groups])) + " | - |")
    
    # Continuous vars
    cont_vars = {'Age (years)': 'age', 'BMI': 'bmi', 'GMI (%)': 'gmi', 'Mean Glucose (mg/dL)': 'mean_glucose', 'Time in Range (%)': 'tir'}
    for label, col in cont_vars.items():
        means = df.groupby('group')[col].mean()
        stds = df.groupby('group')[col].std()
        
        f_val, p_val = f_oneway(*[df[df['group'] == g][col] for g in groups])
        
        row_vals = [f"{means[g]:.1f} ({stds[g]:.1f})" for g in groups]
        report.append(f"| {label} | " + " | ".join(row_vals) + f" | {format_p(p_val)} |")
        
    # Categorical vars
    cat_vars = {'Hypertension (%)': 'hypertension', 'High Cholesterol (%)': 'high_cholesterol', 'Kidney Disease (%)': 'kidney_disease', 'Circulatory Problems (%)': 'circulatory_problems', 'Neurodegenerative (%)': 'neurodegenerative'}
    for label, col in cat_vars.items():
        props = df.groupby('group')[col].mean() * 100
        cross = pd.crosstab(df['group'], df[col])
        _, p_val, _, _ = chi2_contingency(cross)
        
        row_vals = [f"{props[g]:.1f}%" for g in groups]
        report.append(f"| {label} | " + " | ".join(row_vals) + f" | {format_p(p_val)} |")
        
    # Table 2
    report.append("\n## Table 2: MoCA Total and Domain Scores\n")
    report.append("| Cognitive Domain | Unadjusted Mean | p-value (Unadj) | Adjusted Mean (approx) | p-value (Adj) |")
    report.append("| --- | --- | --- | --- | --- |")
    
    domains = {'Total Score': 'moca_total', 'Memory': 'moca_memory', 'Orientation': 'moca_orientation', 'Abstraction': 'moca_abstraction'}
    
    for label, col in domains.items():
        if df[col].isnull().all():
            continue
            
        # Unadjusted
        means = df.groupby('group')[col].mean()
        f_val, p_unadj = f_oneway(*[df[df['group'] == g][col].dropna() for g in groups])
        
        # Adjusted
        formula = f"{col} ~ C(group, Treatment('1_Controls')) + age + C(education_level) + bmi + gmi + hypertension + high_cholesterol + kidney_disease + circulatory_problems + neurodegenerative"
        try:
            model = smf.ols(formula, data=df).fit()
            anova_res = sm.stats.anova_lm(model, typ=2)
            p_adj = anova_res.loc["C(group, Treatment('1_Controls'))", "PR(>F)"]
            
            # Extract adjusted means approx by adding back baseline
            intercept = model.params.get('Intercept', np.nan)
            adj_means = [f"Cont: {intercept:.1f}"]
            
            for g in groups[1:]:
                # find key matching the group
                key = [k for k in model.params.keys() if g in k]
                if key:
                    adj_means.append(f"{g[:3]}: {intercept + model.params[key[0]]:.1f}")
            adj_str = ", ".join(adj_means)
        except Exception as e:
            p_adj = np.nan
            adj_str = f"Error: {e}"
            
        unadj_str = ", ".join([f"{g[:3]}: {means[g]:.1f}" for g in groups])
        report.append(f"| {label} | {unadj_str} | {format_p(p_unadj)} | {adj_str} | {format_p(p_adj)} |")
        
    # Table 3
    report.append("\n## Table 3: Association with Cognitive Impairment (MoCA < 26)\n")
    report.append("| Glycaemic Status | Univariable OR (95% CI) | p-value | Multivariable OR (95% CI) | p-value |")
    report.append("| --- | --- | --- | --- | --- |")
    
    # Univariable
    model_uni = smf.glm("cognitive_impairment ~ C(group, Treatment('1_Controls'))", data=df, family=sm.families.Binomial()).fit()
    uni_params = np.exp(model_uni.params)
    uni_conf = np.exp(model_uni.conf_int())
    uni_pvals = model_uni.pvalues
    
    # Multivariable
    formula_multi = "cognitive_impairment ~ C(group, Treatment('1_Controls')) + age + C(education_level) + bmi + gmi + hypertension + high_cholesterol + kidney_disease + circulatory_problems + neurodegenerative"
    model_multi = smf.glm(formula_multi, data=df, family=sm.families.Binomial()).fit()
    multi_params = np.exp(model_multi.params)
    multi_conf = np.exp(model_multi.conf_int())
    multi_pvals = model_multi.pvalues
    
    for g in groups[1:]: # Skip controls
        term = f"C(group, Treatment('1_Controls'))[T.{g}]"
        
        if term in uni_params:
            uni_str = f"{uni_params[term]:.2f} ({uni_conf.loc[term, 0]:.2f} - {uni_conf.loc[term, 1]:.2f})"
            uni_p = uni_pvals[term]
        else:
            uni_str = "-"
            uni_p = np.nan
            
        if term in multi_params:
            multi_str = f"{multi_params[term]:.2f} ({multi_conf.loc[term, 0]:.2f} - {multi_conf.loc[term, 1]:.2f})"
            multi_p = multi_pvals[term]
        else:
            multi_str = "-"
            multi_p = np.nan
            
        report.append(f"| {g} | {uni_str} | {format_p(uni_p)} | {multi_str} | {format_p(multi_p)} |")

    out_file = os.path.join(REPORTS_DIR, "report.md")
    with open(out_file, "w") as f:
        f.write("\n".join(report))
        
    print(f"Report generated successfully as {out_file}")

if __name__ == "__main__":
    generate_report()
