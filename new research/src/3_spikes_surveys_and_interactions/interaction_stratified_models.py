import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports", "3_spikes_surveys_and_interactions")
os.makedirs(REPORTS_DIR, exist_ok=True)

def run_interaction_stratified_models():
    master_path = os.path.join(DATA_DIR, "master_cgm_spikes_dataset.csv")
    if not os.path.exists(master_path):
        master_path = os.path.join(DATA_DIR, "master_extended_dataset.csv")
        
    df = pd.read_csv(master_path)
    print(f"Loaded dataset for Goal 5: {len(df)} rows.")
    
    df_clean = df.dropna(subset=['moca_total', 'age', 'is_diabetic', 'bmi', 'years_of_education']).copy()
    df_clean['age_50_65'] = ((df_clean['age'] >= 50) & (df_clean['age'] <= 65)).astype(float)
    df_clean['age_over_65'] = (df_clean['age'] > 65).astype(float)
    
    print(f"Complete cases for linear & interaction models: {len(df_clean)}")
    
    report_md = "# Goal 5: Interaction Term Analysis & 3-Age Partition Stratified Linear Models\n\n"
    report_md += "> [!NOTE]\n"
    report_md += r"> Evaluates the main effects of **3 Age Partitions** ($<50$, $50\text{--}65$, $>65$), **Diabetes Status Indicator** ($\text{Diabetic}$), and their interaction terms on continuous MoCA cognitive scores. Includes side-by-side multivariable linear models across all 6 stratified sub-cohorts." + "\n\n"
    
    # 1. Interaction Term OLS Model across 3 Age Partitions
    report_md += "## 1. Global Interaction Term OLS Linear Model (Outcome: MoCA Total Score)\n\n"
    report_md += "- **Reference Age Baseline Group**: Young Adults (< 50 years)\n\n"
    formula_inter = "moca_total ~ age_50_65 + age_over_65 + is_diabetic + age_50_65:is_diabetic + age_over_65:is_diabetic + bmi + years_of_education + mean_glucose"
    ols_inter = smf.ols(formula_inter, data=df_clean).fit()
    
    report_md += f"- **Model Sample Size (N)**: {len(df_clean)}\n"
    report_md += f"- **R-squared ($R^2$)**: **{ols_inter.rsquared:.3f}** (Adjusted $R^2$: **{ols_inter.rsquared_adj:.3f}**)\n"
    report_md += f"- **F-statistic**: **{ols_inter.fvalue:.2f}** (p-value: **{ols_inter.f_pvalue:.4e}**)\n\n"
    
    report_md += "| Term / Predictor | Coef (β) | Std Error (SE) | t-statistic | p-value | 95% Confidence Interval | Sig |\n"
    report_md += "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |\n"
    
    conf = ols_inter.conf_int()
    param_map = {
        'Intercept': 'Constant (Intercept)',
        'age_50_65': 'Age 50-65 Main Effect (vs <50)',
        'age_over_65': 'Age >65 Main Effect (vs <50)',
        'is_diabetic': 'Diabetes Main Effect (Diabetic)',
        'age_50_65:is_diabetic': r'Interaction Term (Age 50-65 × Diabetic)',
        'age_over_65:is_diabetic': r'Interaction Term (Age >65 × Diabetic)',
        'bmi': 'BMI Control',
        'years_of_education': 'Years of Education Control',
        'mean_glucose': 'CGM Mean Glucose Control'
    }
    
    for param in ols_inter.params.index:
        coef = ols_inter.params[param]
        se = ols_inter.bse[param]
        t = ols_inter.tvalues[param]
        p = ols_inter.pvalues[param]
        ci_l = conf.loc[param, 0]
        ci_u = conf.loc[param, 1]
        sig = "⭐" if p < 0.05 else ("†" if p < 0.10 else "NS")
        
        p_label = param_map.get(param, param)
        report_md += f"| **{p_label}** | {coef:+.4f} | {se:.4f} | {t:+.2f} | {p:.4f} | [{ci_l:+.3f}, {ci_u:+.3f}] | {sig} |\n"
        
    report_md += "\n---\n\n"
    
    # 2. 6-Subcohort Stratified OLS Linear Models (3 Age Partitions x 2 Diabetes Status)
    report_md += "## 2. 6-Subcohort Stratified Linear Regression Models (3 Age Partitions × Diabetes Status)\n\n"
    report_md += "Stratification Categories:\n"
    report_md += r"1. **Young (<50) & Diabetes** ($\text{Age} < 50, \text{Diabetic} = 1$)" + "\n"
    report_md += r"2. **Middle-Aged (50-65) & Diabetes** ($50 \le \text{Age} \le 65, \text{Diabetic} = 1$)" + "\n"
    report_md += r"3. **Older (>65) & Diabetes** ($\text{Age} > 65, \text{Diabetic} = 1$)" + "\n"
    report_md += r"4. **Young (<50) & No Diabetes** ($\text{Age} < 50, \text{Diabetic} = 0$)" + "\n"
    report_md += r"5. **Middle-Aged (50-65) & No Diabetes** ($50 \le \text{Age} \le 65, \text{Diabetic} = 0$)" + "\n"
    report_md += r"6. **Older (>65) & No Diabetes** ($\text{Age} > 65, \text{Diabetic} = 0$)" + "\n\n"
    
    stratified_groups = {
        'Young (<50) & Diabetes': df_clean[(df_clean['age'] < 50) & (df_clean['is_diabetic'] == 1)],
        'Middle-Aged (50-65) & Diabetes': df_clean[(df_clean['age'] >= 50) & (df_clean['age'] <= 65) & (df_clean['is_diabetic'] == 1)],
        'Older (>65) & Diabetes': df_clean[(df_clean['age'] > 65) & (df_clean['is_diabetic'] == 1)],
        'Young (<50) & No Diabetes': df_clean[(df_clean['age'] < 50) & (df_clean['is_diabetic'] == 0)],
        'Middle-Aged (50-65) & No Diabetes': df_clean[(df_clean['age'] >= 50) & (df_clean['age'] <= 65) & (df_clean['is_diabetic'] == 0)],
        'Older (>65) & No Diabetes': df_clean[(df_clean['age'] > 65) & (df_clean['is_diabetic'] == 0)]
    }
    
    for name, sdf in stratified_groups.items():
        report_md += f"### 📊 Sub-cohort: {name} (N = {len(sdf)})\n\n"
        if len(sdf) < 10:
            report_md += "Insufficient sample size to fit multivariable OLS model.\n\n---\n\n"
            continue
            
        formula_sub = "moca_total ~ bmi + years_of_education + mean_glucose"
        ols_sub = smf.ols(formula_sub, data=sdf).fit()
        
        report_md += f"- **Model R²**: **{ols_sub.rsquared:.3f}** (Adjusted $R^2$: {ols_sub.rsquared_adj:.3f})\n"
        report_md += f"- **F-statistic**: {ols_sub.fvalue:.2f} (p-value: {ols_sub.f_pvalue:.4f})\n\n"
        
        report_md += "| Predictor | Coef (β) | Std Error | t-stat | p-value | 95% CI | Sig |\n"
        report_md += "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |\n"
        
        c_sub = ols_sub.conf_int()
        for p_sub in ols_sub.params.index:
            coef = ols_sub.params[p_sub]
            se = ols_sub.bse[p_sub]
            t = ols_sub.tvalues[p_sub]
            p = ols_sub.pvalues[p_sub]
            ci_l = c_sub.loc[p_sub, 0]
            ci_u = c_sub.loc[p_sub, 1]
            sig = "⭐" if p < 0.05 else ("†" if p < 0.10 else "NS")
            
            p_clean = p_sub.replace('bmi', 'BMI').replace('years_of_education', 'Years of Education').replace('mean_glucose', 'CGM Mean Glucose').replace('Intercept', 'Intercept')
            report_md += f"| **{p_clean}** | {coef:+.4f} | {se:.4f} | {t:+.2f} | {p:.4f} | [{ci_l:+.3f}, {ci_u:+.3f}] | {sig} |\n"
            
        report_md += "\n---\n\n"
        
    out_file = os.path.join(REPORTS_DIR, "interaction_and_stratified_models.md")
    with open(out_file, 'w') as f:
        f.write(report_md)
    print(f"Saved Goal 5 report to {out_file}")

if __name__ == "__main__":
    run_interaction_stratified_models()
