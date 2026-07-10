import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import f_oneway, chi2_contingency
import os

OUTPUT_DIR = os.path.abspath(".")

def format_p(p_val):
    if pd.isna(p_val):
        return "NaN"
    if p_val < 0.001:
        return "**<0.001** ⭐"
    elif p_val < 0.05:
        return f"**{p_val:.3f}** ⭐"
    else:
        return f"{p_val:.3f}"

def generate_side_by_side_report():
    df = pd.read_csv("master_cgm_moca_dataset.csv")
    
    # Map groups
    group_map = {
        'healthy': '1_Controls',
        'pre_diabetes_lifestyle_controlled': '2_Pre-diabetes',
        'oral_medication_and_or_non_insulin_injectable_medication_controlled': '3_Medication-controlled',
        'insulin_dependent': '4_Insulin-dependent'
    }
    df['group'] = df['study_group'].map(group_map)
    df.dropna(subset=['group', 'moca_total'], inplace=True)
    
    # Impute missing values with median/mode to keep the sample size up
    for col in ['age', 'bmi', 'gmi', 'mean_glucose', 'tir', 'hba1c']:
        df[col] = df[col].fillna(df[col].median())
    for col in ['education_level']:
        df[col] = df[col].fillna(df[col].mode()[0])
        
    df['cognitive_impairment'] = (df['moca_total'] < 26).astype(int)
    
    groups = sorted(df['group'].unique())
    
    report = []
    report.append("# Side-by-Side Comparison: CGM (GMI) vs HbA1c")
    report.append("\nThis report compares multivariable models adjusting for GMI alongside models adjusting for HbA1c to predict cognitive impairment.\n")
    
    # Table 2: MoCA Total and Domain Scores
    report.append("## Table 2: Adjusted MoCA Total and Domain Scores (GMI vs HbA1c)\n")
    report.append("| Cognitive Domain | Unadjusted Mean | Adj Mean (GMI) | p-value (GMI) | Adj Mean (HbA1c) | p-value (HbA1c) |")
    report.append("| --- | --- | --- | --- | --- | --- |")
    
    domains = {'Total Score': 'moca_total', 'Memory': 'moca_memory', 'Orientation': 'moca_orientation', 'Abstraction': 'moca_abstraction'}
    
    for label, col in domains.items():
        if df[col].isnull().all():
            continue
            
        # Unadjusted
        means = df.groupby('group')[col].mean()
        unadj_str = ", ".join([f"{g[:3]}: {means[g]:.1f}" for g in groups])
        
        # GMI Model
        form_gmi = f"{col} ~ C(group, Treatment('1_Controls')) + age + C(education_level) + bmi + gmi + hypertension + high_cholesterol + kidney_disease + circulatory_problems + neurodegenerative"
        try:
            model_g = smf.ols(form_gmi, data=df).fit()
            anova_g = sm.stats.anova_lm(model_g, typ=2)
            p_adj_g = anova_g.loc["C(group, Treatment('1_Controls'))", "PR(>F)"]
            int_g = model_g.params.get('Intercept', np.nan)
            adj_means_g = [f"Con: {int_g:.1f}"]
            for g in groups[1:]:
                key = [k for k in model_g.params.keys() if g in k]
                if key:
                    adj_means_g.append(f"{g[:3]}: {int_g + model_g.params[key[0]]:.1f}")
            adj_str_g = ", ".join(adj_means_g)
        except Exception as e:
            p_adj_g = np.nan
            adj_str_g = "Error"
            
        # HbA1c Model
        form_hba1c = f"{col} ~ C(group, Treatment('1_Controls')) + age + C(education_level) + bmi + hba1c + hypertension + high_cholesterol + kidney_disease + circulatory_problems + neurodegenerative"
        try:
            model_h = smf.ols(form_hba1c, data=df).fit()
            anova_h = sm.stats.anova_lm(model_h, typ=2)
            p_adj_h = anova_h.loc["C(group, Treatment('1_Controls'))", "PR(>F)"]
            int_h = model_h.params.get('Intercept', np.nan)
            adj_means_h = [f"Con: {int_h:.1f}"]
            for g in groups[1:]:
                key = [k for k in model_h.params.keys() if g in k]
                if key:
                    adj_means_h.append(f"{g[:3]}: {int_h + model_h.params[key[0]]:.1f}")
            adj_str_h = ", ".join(adj_means_h)
        except Exception as e:
            p_adj_h = np.nan
            adj_str_h = "Error"
            
        report.append(f"| {label} | {unadj_str} | {adj_str_g} | {format_p(p_adj_g)} | {adj_str_h} | {format_p(p_adj_h)} |")
        
    # Table 3
    report.append("\n## Table 3: Association with Cognitive Impairment (MoCA < 26) - Multivariable OR\n")
    report.append("| Glycaemic Status | OR (GMI) (95% CI) | p-value (GMI) | OR (HbA1c) (95% CI) | p-value (HbA1c) |")
    report.append("| --- | --- | --- | --- | --- |")
    
    form_multi_gmi = "cognitive_impairment ~ C(group, Treatment('1_Controls')) + age + C(education_level) + bmi + gmi + hypertension + high_cholesterol + kidney_disease + circulatory_problems + neurodegenerative"
    model_multi_g = smf.glm(form_multi_gmi, data=df, family=sm.families.Binomial()).fit()
    multi_params_g = np.exp(model_multi_g.params)
    multi_conf_g = np.exp(model_multi_g.conf_int())
    multi_pvals_g = model_multi_g.pvalues
    
    form_multi_hba1c = "cognitive_impairment ~ C(group, Treatment('1_Controls')) + age + C(education_level) + bmi + hba1c + hypertension + high_cholesterol + kidney_disease + circulatory_problems + neurodegenerative"
    model_multi_h = smf.glm(form_multi_hba1c, data=df, family=sm.families.Binomial()).fit()
    multi_params_h = np.exp(model_multi_h.params)
    multi_conf_h = np.exp(model_multi_h.conf_int())
    multi_pvals_h = model_multi_h.pvalues
    
    for g in groups[1:]: # Skip controls
        term = f"C(group, Treatment('1_Controls'))[T.{g}]"
        
        # GMI
        if term in multi_params_g:
            str_g = f"{multi_params_g[term]:.2f} ({multi_conf_g.loc[term, 0]:.2f} - {multi_conf_g.loc[term, 1]:.2f})"
            p_g = multi_pvals_g[term]
        else:
            str_g, p_g = "-", np.nan
            
        # HbA1c
        if term in multi_params_h:
            str_h = f"{multi_params_h[term]:.2f} ({multi_conf_h.loc[term, 0]:.2f} - {multi_conf_h.loc[term, 1]:.2f})"
            p_h = multi_pvals_h[term]
        else:
            str_h, p_h = "-", np.nan
            
        report.append(f"| {g} | {str_g} | {format_p(p_g)} | {str_h} | {format_p(p_h)} |")
        
    with open("report_side_by_side.md", "w") as f:
        f.write("\n".join(report))
        
    print("Report generated successfully as report_side_by_side.md")

if __name__ == "__main__":
    generate_side_by_side_report()
