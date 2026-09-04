import os
import pandas as pd
import numpy as np

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports", "4_personalized_spike_analysis")
DATA_DIR = os.path.join(REPORTS_DIR, "data")
OLS_CSV = os.path.join(DATA_DIR, "full_ols_regression_results.csv")

df_ols = pd.read_csv(OLS_CSV)

def generate_markdown_table_for_model(outcome, model_type, pred_col, title, formula):
    sub = df_ols[(df_ols['Outcome'] == outcome) & (df_ols['Model_Type'] == model_type) & (df_ols['Predictor_Col'] == pred_col)]
    if len(sub) == 0:
        return ""
        
    r0 = sub.iloc[0]
    n_obs = int(r0['N_obs'])
    r2 = r0['R_squared']
    adj_r2 = r0['Adj_R_squared']
    f_stat = r0['F_stat']
    f_p = r0['F_pvalue']
    rse = r0['RSE']
    df_res = int(r0['df_resid'])
    
    lines = []
    lines.append(f"### {title}")
    lines.append(f"**Regression Call / Formula**: `{formula}`  ")
    lines.append(f"**Model Diagnostics**: N = **{n_obs}**, R² = **{r2:.4f}**, Adj R² = **{adj_r2:.4f}**, F-statistic = **{f_stat:.2f}** (p = **{f_p:.2e}**), Residual SE = **{rse:.3f}** on **{df_res}** df\n")
    lines.append("| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>|t|) | Signif |")
    lines.append("| :--- | :---: | :---: | :---: | :---: | :---: | :---: |")
    
    for _, r in sub.iterrows():
        term = r['Term']
        coef = r['Coefficient']
        se = r['Std_Error']
        m2se = r['Margin_2SE']
        tval = r['t_value']
        pval = r['p_value']
        sig = r['Significance'] if pd.notna(r['Significance']) else ''
        
        is_sig = pval < 0.05
        c_str = f"**{coef:+.4f}**" if is_sig else f"{coef:+.4f}"
        p_str = f"**{pval:.2e}**" if is_sig else f"{pval:.2e}"
        t_str = f"**{tval:+.3f}**" if is_sig else f"{tval:+.3f}"
        sig_str = f"**{sig}**" if is_sig else sig
        
        lines.append(f"| `{term}` | {c_str} | {se:.4f} | ±{m2se:.4f} | {t_str} | {p_str} | {sig_str} |")
        
    lines.append("\n*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*\n")
    return "\n".join(lines)

print("Generated helper function for markdown formatting.")
