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

def run_gridsearch():
    df = pd.read_csv(os.path.join(DATA_DIR, "master_cgm_moca_dataset.csv"))
    group_map = {
        'healthy': '1_Controls',
        'pre_diabetes_lifestyle_controlled': '2_Pre-diabetes',
        'oral_medication_and_or_non_insulin_injectable_medication_controlled': '3_Medication-controlled',
        'insulin_dependent': '4_Insulin-dependent'
    }
    df['group'] = df['study_group'].map(group_map)
    df.dropna(subset=['group', 'moca_total'], inplace=True)
    
    for col in ['age', 'bmi', 'gmi', 'mean_glucose', 'tir']:
        df[col] = df[col].fillna(df[col].median())
    for col in ['education_level']:
        df[col] = df[col].fillna(df[col].mode()[0])
        
    df['cognitive_impairment'] = (df['moca_total'] < 26).astype(int)
    groups = sorted(df['group'].unique())
    
    metrics = ['gmi', 'mean_glucose', 'tir']
    results = []
    
    for metric in metrics:
        results.append(f"### Results Adjusted for {metric.upper()}\n")
        
        # Table 2 for MoCA Total Score ONLY (for brevity)
        col = 'moca_total'
        formula = f"{col} ~ C(group, Treatment('1_Controls')) + age + C(education_level) + bmi + {metric} + hypertension + high_cholesterol + kidney_disease + circulatory_problems + neurodegenerative"
        
        model = smf.ols(formula, data=df).fit()
        anova_res = sm.stats.anova_lm(model, typ=2)
        p_adj = anova_res.loc["C(group, Treatment('1_Controls'))", "PR(>F)"]
        
        intercept = model.params.get('Intercept', np.nan)
        adj_means = [f"Cont: {intercept:.1f}"]
        for g in groups[1:]:
            key = [k for k in model.params.keys() if g in k]
            if key:
                adj_means.append(f"{g[:3]}: {intercept + model.params[key[0]]:.1f}")
        
        results.append("**Table 2: MoCA Total Score Adjusted Means**")
        results.append(f"- Means: {', '.join(adj_means)}")
        results.append(f"- Omnibus p-value for group effect: {p_adj:.3f}\n")
        
        # Table 3
        results.append("**Table 3: Association with Cognitive Impairment (OR)**")
        formula_multi = f"cognitive_impairment ~ C(group, Treatment('1_Controls')) + age + C(education_level) + bmi + {metric} + hypertension + high_cholesterol + kidney_disease + circulatory_problems + neurodegenerative"
        model_multi = smf.glm(formula_multi, data=df, family=sm.families.Binomial()).fit()
        multi_params = np.exp(model_multi.params)
        multi_conf = np.exp(model_multi.conf_int())
        multi_pvals = model_multi.pvalues
        
        results.append("| Glycaemic Status | Multivariable OR (95% CI) | p-value |")
        results.append("| --- | --- | --- |")
        for g in groups[1:]:
            term = f"C(group, Treatment('1_Controls'))[T.{g}]"
            if term in multi_params:
                m_str = f"{multi_params[term]:.2f} ({multi_conf.loc[term, 0]:.2f} - {multi_conf.loc[term, 1]:.2f})"
                m_p = multi_pvals[term]
                results.append(f"| {g} | {m_str} | {m_p:.3f} |")
        results.append("\n")
        
    out_file = os.path.join(REPORTS_DIR, "gridsearch_results.txt")
    with open(out_file, "w") as f:
        f.write("\n".join(results))
    print(f"Done, written to {out_file}")

if __name__ == "__main__":
    run_gridsearch()
