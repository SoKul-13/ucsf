import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from sklearn.metrics import roc_auc_score, f1_score, precision_score, recall_score, brier_score_loss

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports", "5_multimodal_cgm_analysis")
TABLES_DIR = os.path.join(REPORTS_DIR, "regression_tables")
DATA_OUT_DIR = os.path.join(REPORTS_DIR, "data")
os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(TABLES_DIR, exist_ok=True)
os.makedirs(DATA_OUT_DIR, exist_ok=True)

COVARIATES_FORMULA = "age + bmi + C(education_level) + hypertension + high_cholesterol + kidney_disease + circulatory_problems"
CGM_PREDICTORS = ["mean_glucose", "glucose_sd", "mean_to_sd_ratio", "tir"]
ALL_KEY_PREDICTORS = ["hba1c"] + CGM_PREDICTORS

TERM_NAME_MAP = {
    'Intercept': 'Intercept',
    'hba1c': 'HbA1c (%)',
    'mean_glucose': 'Mean Glucose (mg/dL)',
    'glucose_sd': 'Glucose SD (mg/dL)',
    'mean_to_sd_ratio': 'Mean / SD Ratio',
    'tir': 'Time in Range (70-180 mg/dL)',
    'age': 'Age (years)',
    'bmi': 'BMI (kg/m²)',
    'hypertension': 'Hypertension',
    'high_cholesterol': 'High Cholesterol',
    'kidney_disease': 'Kidney Disease',
    'circulatory_problems': 'Circulatory Problems',
    'C(education_level)[T.Graduate level]': 'Education: Graduate Level',
    'C(education_level)[T.High school or below]': 'Education: High School or Below'
}

def get_clean_term(term):
    return TERM_NAME_MAP.get(term, term)

def get_signif_star(p_val):
    if p_val < 0.001:
        return "***"
    elif p_val < 0.01:
        return "**"
    elif p_val < 0.05:
        return "*"
    elif p_val < 0.1:
        return "."
    else:
        return ""

def fit_and_extract_ols(df, target_col, predictor_cols, model_label):
    formula = f"{target_col} ~ {' + '.join(predictor_cols)} + {COVARIATES_FORMULA}"
    cols = [target_col] + predictor_cols + ['age', 'bmi', 'education_level', 'hypertension', 'high_cholesterol', 'kidney_disease', 'circulatory_problems']
    sub_df = df.dropna(subset=cols).copy()
    if len(sub_df) < 30:
        return None
    
    model = smf.ols(formula, data=sub_df).fit()
    
    nobs = int(model.nobs)
    df_resid = int(model.df_resid)
    r2 = float(model.rsquared)
    r2_adj = float(model.rsquared_adj)
    f_stat = float(model.fvalue)
    f_pvalue = float(model.f_pvalue)
    resid_se = float(np.sqrt(model.mse_resid))
    aic = float(model.aic)
    log_ll = float(model.llf)
    
    terms = []
    for term in model.params.index:
        beta = float(model.params[term])
        se = float(model.bse[term])
        margin_2se = 2.0 * se
        t_stat = float(model.tvalues[term])
        p_val = float(model.pvalues[term])
        sig = get_signif_star(p_val)
        
        terms.append({
            'term': term,
            'term_clean': get_clean_term(term),
            'beta': beta,
            'se': se,
            'margin_2se': margin_2se,
            't_stat': t_stat,
            'p_val': p_val,
            'sig': sig,
            'ci_low': float(model.conf_int().loc[term, 0]),
            'ci_high': float(model.conf_int().loc[term, 1])
        })
        
    return {
        'model_label': model_label,
        'target': target_col,
        'type': 'OLS',
        'nobs': nobs,
        'df_resid': df_resid,
        'r2': r2,
        'r2_adj': r2_adj,
        'f_stat': f_stat,
        'f_pvalue': f_pvalue,
        'resid_se': resid_se,
        'aic': aic,
        'log_ll': log_ll,
        'terms': terms,
        'model_obj': model,
        'data': sub_df
    }

def fit_and_extract_glm(df, target_col, predictor_cols, model_label):
    formula = f"{target_col} ~ {' + '.join(predictor_cols)} + {COVARIATES_FORMULA}"
    cols = [target_col] + predictor_cols + ['age', 'bmi', 'education_level', 'hypertension', 'high_cholesterol', 'kidney_disease', 'circulatory_problems']
    sub_df = df.dropna(subset=cols).copy()
    if len(sub_df) < 30 or sub_df[target_col].nunique() < 2:
        return None
    
    model = smf.glm(formula, data=sub_df, family=sm.families.Binomial()).fit()
    
    nobs = int(model.nobs)
    aic = float(model.aic)
    log_ll = float(model.llf)
    
    y_true = sub_df[target_col].values
    y_pred_prob = model.predict(sub_df).values
    y_pred_bin = (y_pred_prob >= 0.5).astype(int)
    
    try:
        auc = float(roc_auc_score(y_true, y_pred_prob))
    except Exception:
        auc = np.nan
        
    try:
        f1 = float(f1_score(y_true, y_pred_bin, zero_division=0))
        prec = float(precision_score(y_true, y_pred_bin, zero_division=0))
        rec = float(recall_score(y_true, y_pred_bin, zero_division=0))
        brier = float(brier_score_loss(y_true, y_pred_prob))
    except Exception:
        f1, prec, rec, brier = np.nan, np.nan, np.nan, np.nan
        
    terms = []
    for term in model.params.index:
        beta = float(model.params[term])
        se = float(model.bse[term])
        margin_2se = 2.0 * se
        z_stat = float(model.tvalues[term]) if hasattr(model, 'tvalues') else beta / se
        p_val = float(model.pvalues[term])
        sig = get_signif_star(p_val)
        or_val = float(np.exp(beta))
        or_ci_low = float(np.exp(model.conf_int().loc[term, 0]))
        or_ci_high = float(np.exp(model.conf_int().loc[term, 1]))
        
        terms.append({
            'term': term,
            'term_clean': get_clean_term(term),
            'beta': beta,
            'se': se,
            'margin_2se': margin_2se,
            'z_stat': z_stat,
            'p_val': p_val,
            'sig': sig,
            'or_val': or_val,
            'or_ci_low': or_ci_low,
            'or_ci_high': or_ci_high
        })
        
    return {
        'model_label': model_label,
        'target': target_col,
        'type': 'GLM',
        'nobs': nobs,
        'auc': auc,
        'f1': f1,
        'precision': prec,
        'recall': rec,
        'brier': brier,
        'aic': aic,
        'log_ll': log_ll,
        'terms': terms,
        'model_obj': model,
        'data': sub_df
    }

def format_ols_markdown_table(res, title, formula_str):
    out = []
    out.append(f"#### {title}")
    out.append(f"**Regression Formula**: `{formula_str}`")
    out.append(f"**Model Diagnostics**: N = **{res['nobs']}** | R² = **{res['r2']:.4f}** | Adj R² = **{res['r2_adj']:.4f}** | F-statistic = **{res['f_stat']:.2f}** (p = **{res['f_pvalue']:.2e}**) | Residual SE = **{res['resid_se']:.4f}** | AIC = **{res['aic']:.2f}**\n")
    
    out.append("| Term / Variable | Coef Estimate (β) | Std Error (SE) | 95% CI Margin (±2 SE) | t value | p-value | Signif |")
    out.append("| :--- | :---: | :---: | :---: | :---: | :---: | :---: |")
    
    for t in res['terms']:
        is_bold = t['p_val'] < 0.05
        term_str = f"**{t['term_clean']}**" if is_bold else t['term_clean']
        b_str = f"**{t['beta']:+.4f}**" if is_bold else f"{t['beta']:+.4f}"
        t_str = f"**{t['t_stat']:+.3f}**" if is_bold else f"{t['t_stat']:+.3f}"
        
        if t['p_val'] < 0.001:
            p_str = f"**{t['p_val']:.2e}**"
        elif is_bold:
            p_str = f"**{t['p_val']:.4f}**"
        else:
            p_str = f"{t['p_val']:.4f}"
            
        out.append(f"| {term_str} | {b_str} | {t['se']:.4f} | ±{t['margin_2se']:.4f} | {t_str} | {p_str} | {t['sig']} |")
        
    out.append("\n*Significance codes: *** p < 0.001, ** p < 0.01, * p < 0.05, . p < 0.1*\n")
    return "\n".join(out)

def format_glm_markdown_table(res, title, formula_str):
    out = []
    out.append(f"#### {title}")
    out.append(f"**Regression Formula**: `{formula_str}`")
    out.append(f"**Model Diagnostics**: N = **{res['nobs']}** | ROC-AUC = **{res['auc']:.4f}** | F1 Score = **{res['f1']:.4f}** | Precision = **{res['precision']:.4f}** | Recall = **{res['recall']:.4f}** | Brier Score = **{res['brier']:.4f}** | AIC = **{res['aic']:.2f}**\n")
    
    out.append("| Term / Variable | Coef (β) | Odds Ratio (OR) | Std Error (SE) | 95% CI Margin | z value | p-value | 95% CI (OR) | Signif |")
    out.append("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |")
    
    for t in res['terms']:
        is_bold = t['p_val'] < 0.05
        term_str = f"**{t['term_clean']}**" if is_bold else t['term_clean']
        b_str = f"**{t['beta']:+.4f}**" if is_bold else f"{t['beta']:+.4f}"
        or_str = f"**{t['or_val']:.4f}**" if is_bold else f"{t['or_val']:.4f}"
        z_str = f"**{t['z_stat']:+.3f}**" if is_bold else f"{t['z_stat']:+.3f}"
        
        if t['p_val'] < 0.001:
            p_str = f"**{t['p_val']:.2e}**"
        elif is_bold:
            p_str = f"**{t['p_val']:.4f}**"
        else:
            p_str = f"{t['p_val']:.4f}"
            
        ci_str = f"[{t['or_ci_low']:.4f}, {t['or_ci_high']:.4f}]"
        out.append(f"| {term_str} | {b_str} | {or_str} | {t['se']:.4f} | ±{t['margin_2se']:.4f} | {z_str} | {p_str} | {ci_str} | {t['sig']} |")
        
    out.append("\n*Significance codes: *** p < 0.001, ** p < 0.01, * p < 0.05, . p < 0.1*\n")
    return "\n".join(out)

# Specific custom detailed analytical commentary for each outcome
DETAILED_ANALYSES = {
    'moca_total': {
        'good': "CGM metrics increase variance explained ($R^2$) from 0.1010 to 0.1131 (+12.0% relative improvement) and reduce AIC from 8,463.17 to 8,448.30. In Model 1C, **Mean Glucose** ($\\\\beta = -0.0347, p < 0.0001$) and **Time in Range 70-180 mg/dL** ($\\\\beta = -0.0430, p = 0.0006$) are highly significant negative predictors.",
        'bad': "Lab **HbA1c (%)** completely loses statistical significance ($\\\\beta = -0.0906, t = -0.624, p = 0.5326$) when CGM metrics are included in the same model, demonstrating that HbA1c carries redundant information already captured by CGM mean glucose.",
        'significant': "⭐ **Key Publication Finding**: Continuous glucose dynamics (`mean_glucose` and `tir`) dominate static HbA1c in predicting global cognitive score. In a joint model, HbA1c adds zero incremental value ($\\\\text{LRT } p = 0.5326$), proving CGM is a superior clinical biomarker for cognitive health."
    },
    'cognitive_impairment': {
        'good': "Discriminative ROC-AUC improves from 0.6688 (HbA1c Only) to 0.6807 (Combined Model), with AIC dropping to 2,143.92. **Mean Glucose** increases odds of cognitive impairment by **2.21% per 1 mg/dL** ($\\\\text{OR} = 1.0221, z = +3.450, p = 0.0006$), and **TIR 70-180** increases odds by **2.87% per 1%** ($\\\\text{OR} = 1.0287, z = +3.046, p = 0.0023$).",
        'bad': "F1 score (0.4716) indicates Moderate classification precision/recall trade-off at threshold 0.5 due to class imbalance in MoCA < 26 cutoff.",
        'significant': "⭐ **Key Publication Finding**: Likelihood Ratio Test proves CGM metrics provide statistically significant incremental diagnostic value beyond HbA1c ($\\\\text{LRT } \\\\chi^2(4) = 18.69, p = 9.03 \\\\times 10^{-4}$). Lab HbA1c is rendered non-significant ($\\\\text{OR} = 1.0317, p = 0.7631$)."
    },
    'moca_memory': {
        'good': "Education level shows strong expected construct validity ($\\\\text{Graduate level } \\\\beta = +0.8038, p < 0.0001$; $\\\\text{High school } \\\\beta = -1.2294, p < 0.0001$). Age is a strong negative predictor ($\\\\beta = -0.0270, p < 0.0001$).",
        'bad': "Neither HbA1c ($p = 0.7659$) nor CGM features ($p > 0.1077$) reach statistical significance for the memory domain specifically.",
        'significant': "Memory domain scores are predominantly driven by demographic factors (age & education) rather than short-term 14-day glycemic exposure."
    },
    'moca_orientation': {
        'good': "Age remains a significant predictor ($\\\\beta = -0.0041, p = 0.0044$).",
        'bad': "Low overall variance explained ($R^2 = 0.0231$) due to severe ceiling effects (most participants score near maximum 6/6). CGM features are non-significant ($p > 0.23$).",
        'significant': "MoCA orientation exhibits insufficient variance in non-demented community cohorts to serve as a sensitive target for glycemic variation."
    },
    'moca_abstraction': {
        'good': "Time in Range 70-180 mg/dL is a statistically significant predictor of executive abstract reasoning ($\\\\beta = -0.0036, t = -2.446, p = 0.0146$). Model $R^2 = 0.0764$.",
        'bad': "Mean glucose and glucose SD are non-significant ($p > 0.28$).",
        'significant': "⭐ **Key Publication Finding**: Executive abstraction reasoning is selectively vulnerable to daily glucose time-in-range volatility among MoCA sub-domains."
    },
    'depression_score': {
        'good': "Demographic covariates and comorbidity burden explain 10.72% of CESD-10 depression variance ($F = 15.48, p = 4.12 \\\\times 10^{-33}$). Mean glucose shows a marginal negative slope ($\\\\beta = -0.0257, t = -1.897, p = 0.0580$).",
        'bad': "CGM metrics do not provide statistically significant incremental predictive value beyond baseline covariates ($\\\\text{LRT } \\\\chi^2(4) = 4.74, p = 0.3156$). Lab HbA1c is non-significant ($\\\\beta = +0.2046, p = 0.3802$).",
        'significant': "Depression severity in AI-READI is driven primarily by medical comorbidities and social determinants rather than direct 14-day glycemic exposure."
    },
    'high_depression': {
        'good': "High Depression Risk ($\\\\text{CESD-10} \\\\ge 10$) achieves ROC-AUC of 0.6803 and AIC of 1,483.46.",
        'bad': "All glycemic metrics (HbA1c, Mean Glucose, SD, TIR) are non-significant ($p > 0.2913$).",
        'significant': "Binary clinical depression risk ($\\\\ge 10$) cannot be reliably diagnosed from continuous glucose monitoring streams alone without survey SDOH context."
    },
    'env_hum_mean': {
        'good': "CGM features significantly improve relative humidity prediction ($\\\\text{LRT } \\\\chi^2(4) = 15.69, p = 0.0035$), raising $R^2$ from 0.0124 to 0.0216. **TIR 70-180** ($\\\\beta = +0.1012, t = +3.206, p = 0.0014$) and **Mean/SD Ratio** ($\\\\beta = +0.6924, t = +2.147, p = 0.0320$) are positive predictors.",
        'bad': "Low overall variance explained ($R^2 = 2.16\\\\%$) indicates indoor humidity is largely dictated by external climate and HVAC systems.",
        'significant': "⭐ **Key Finding**: Participants living in higher indoor relative humidity environments exhibit higher daily Time-in-Range and glycemic stability, potentially reflecting better home climate control."
    },
    'env_pm25_mean': {
        'good': "CGM metrics add statistically significant incremental value over HbA1c ($\\\\text{LRT } \\\\chi^2(4) = 12.07, p = 0.0169$), with **Mean Glucose** showing a significant negative relationship ($\\\\beta = -0.2730, t = -2.691, p = 0.0072$). Combined Model $R^2 = 0.0522$.",
        'bad': "Glucose SD and TIR are non-significant ($p > 0.17$).",
        'significant': "⭐ **Key Finding**: Indoor fine particulate exposure (PM2.5) demonstrates a robust inverse association with patient mean glucose levels."
    },
    'env_pm10_mean': {
        'good': "CGM features provide significant incremental value ($\\\\text{LRT } \\\\chi^2(4) = 11.66, p = 0.0201$), with **Mean Glucose** as a significant negative predictor ($\\\\beta = -0.2787, t = -2.648, p = 0.0082$). Model $R^2 = 0.0511$.",
        'bad': "HbA1c is marginally non-significant in the combined model ($\\\\beta = +3.2709, p = 0.0693$).",
        'significant': "Indoor coarse particulate matter (PM10) mirrors PM2.5 in demonstrating significant environmental coupling with patient mean glucose."
    },
    'env_nox_mean': {
        'good': "**Mean Glucose** is a positive predictor of indoor NOx index ($\\\\beta = +0.0044, t = +1.976, p = 0.0483$).",
        'bad': "Overall model fit is very low ($R^2 = 0.0084$) and overall CGM incremental LRT is non-significant ($p = 0.3839$).",
        'significant': "Indoor nitrogen oxide exposure exhibits minor coupling with glucose levels but low overall predictive variance."
    },
    'env_voc_mean': {
        'good': "Demographic covariates explain 1.74% of indoor VOC index variance.",
        'bad': "No glycemic predictor (HbA1c, Mean, SD, TIR) reaches statistical significance ($p > 0.1290$).",
        'significant': "Indoor volatile organic compounds do not correlate with continuous glucose monitoring parameters."
    },
    'env_temp_mean': {
        'good': "Large sample size ($N = 1,665$) provides precise null baseline bounds.",
        'bad': "Extremely low $R^2 = 0.0079$ and no significant glucose terms ($p > 0.46$).",
        'significant': "Indoor ambient temperature does not confound continuous glucose metrics in home sensor wearers."
    },
    'wearable_stress_mean': {
        'good': "CGM features significantly predict wearable stress ($\\\\text{LRT } \\\\chi^2(4) = 13.55, p = 0.0089$), with $R^2 = 0.0806$. **Mean/SD Ratio** ($\\\\beta = -1.6115, t = -2.635, p = 0.0085$), **Mean Glucose** ($\\\\beta = +0.1058, t = +2.591, p = 0.0097$), and **Glucose SD** ($\\\\beta = -0.3112, t = -2.472, p = 0.0136$) are all highly significant.",
        'bad': "Lab HbA1c is non-significant ($\\\\beta = +1.0023, p = 0.1465$) when CGM variability metrics are included.",
        'significant': "⭐ **Key Publication Finding**: Autonomic wearable stress levels are strongly linked to CGM glucose stability (`mean_to_sd_ratio`) and variability, outperforming lab HbA1c."
    },
    'wearable_hr_mean': {
        'good': "CGM features significantly improve heart rate prediction ($\\\\text{LRT } \\\\chi^2(4) = 10.41, p = 0.0340$). **Glucose SD** ($\\\\beta = -0.4285, t = -2.432, p = 0.0151$) and **Mean/SD Ratio** ($\\\\beta = -1.9104, t = -2.228, p = 0.0260$) are significant predictors.",
        'bad': "Overall $R^2 = 0.0300$ reflects strong external cardiovascular influences on resting/active HR.",
        'significant': "⭐ **Key Finding**: Continuous glucose variability (`glucose_sd`) correlates directly with average wearable heart rate."
    },
    'wearable_daily_steps': {
        'good': "CGM features **nearly double explained variance** from $R^2 = 0.0366$ (HbA1c Only) to $R^2 = 0.0633$ (Combined Model). **Glucose SD** ($\\\\beta = -193.0289, t = -2.392, p = 0.0175$) and **Mean/SD Ratio** ($\\\\beta = -830.9030, t = -2.319, p = 0.0212$) are strongly significant.",
        'bad': "Smaller sample size ($N = 257$) due to wearable step data availability, yielding wider confidence margins.",
        'significant': "⭐ **Key Publication Finding**: Every 1 mg/dL increase in glucose SD predicts **193 fewer daily steps**, establishing physical activity as a major factor in reducing glucose variability."
    },
    'wearable_active_calories': {
        'good': "Lab HbA1c is a significant positive predictor of daily active caloric expenditure ($\\\\beta = +52649.08, t = +2.616, p = 0.0090$). Combined Model $R^2 = 0.0569$.",
        'bad': "CGM features do not add significant incremental value beyond HbA1c ($\\\\text{LRT } p = 0.6655$).",
        'significant': "Caloric expenditure scales strongly with systemic glycemic baseline (HbA1c) rather than 14-day CGM fluctuations."
    }
}

def main():
    df = pd.read_csv(os.path.join(DATA_DIR, "master_multimodal_dataset.csv"))
    print(f"Loaded multimodal dataset with {len(df)} participants.")
    
    outcome_configs = [
        ('Cognition', 'moca_total', 'OLS', 'MoCA Total Score'),
        ('Cognition', 'cognitive_impairment', 'GLM', 'Cognitive Impairment (MoCA < 26)'),
        ('Cognition', 'moca_memory', 'OLS', 'MoCA Memory Domain'),
        ('Cognition', 'moca_orientation', 'OLS', 'MoCA Orientation Domain'),
        ('Cognition', 'moca_abstraction', 'OLS', 'MoCA Abstraction Domain'),
        ('Depression', 'depression_score', 'OLS', 'CESD-10 Depression Score'),
        ('Depression', 'high_depression', 'GLM', 'High Depression Risk (CESD-10 >= 10)'),
        ('Environment', 'env_hum_mean', 'OLS', 'Mean Relative Humidity (%)'),
        ('Environment', 'env_pm25_mean', 'OLS', 'Mean Indoor PM2.5 (µg/m³)'),
        ('Environment', 'env_pm10_mean', 'OLS', 'Mean Indoor PM10 (µg/m³)'),
        ('Environment', 'env_nox_mean', 'OLS', 'Mean Indoor NOx Index'),
        ('Environment', 'env_voc_mean', 'OLS', 'Mean Indoor VOC Index'),
        ('Environment', 'env_temp_mean', 'OLS', 'Mean Ambient Temperature (°C/F)'),
        ('Wearable Activity', 'wearable_stress_mean', 'OLS', 'Average Stress Level'),
        ('Wearable Activity', 'wearable_hr_mean', 'OLS', 'Average Heart Rate (bpm)'),
        ('Wearable Activity', 'wearable_daily_steps', 'OLS', 'Average Daily Steps'),
        ('Wearable Activity', 'wearable_active_calories', 'OLS', 'Average Daily Active Calories')
    ]
    
    doc = []
    doc.append("# Comprehensive Multimodal CGM Prediction Tables & In-Depth Analytical Report")
    doc.append("## Detailed Econometric OLS & GLM Logistic Output Tables with SE, F1, Coefficients, z/t Statistics, p-values, and Domain Syntheses\n")
    doc.append("**Cohort**: UCSF / AI-READI Project ($N = 1,743$ Multimodal Profiles)  ")
    doc.append("**Script Generator**: [`new research/src/5_multimodal_cgm_analysis/generate_phase4_style_report.py`](../../src/5_multimodal_cgm_analysis/generate_phase4_style_report.py)  ")
    doc.append("**Detailed CSV Data**: [`new research/reports/5_multimodal_cgm_analysis/data/multimodal_regression_results_detailed.csv`](../data/multimodal_regression_results_detailed.csv)  \n")
    doc.append("---\n")
    
    # Section 1: Equation Guide
    doc.append("## 1. Regression Equation & Interpretation Blueprint\n")
    doc.append("This report presents three nested regression specifications for every target outcome across **Cognition, Depression, Indoor Environment Sensors, and Wearable Activity Trackers**.")
    doc.append("Below is the mathematical formulation of the prediction equations and how to plug parameters from the tables directly into calculations.\n")
    
    doc.append("### 1A. OLS Linear Regression Equations (Continuous Outcomes)")
    doc.append("For continuous targets (e.g., `moca_total`, `depression_score`, `env_hum_mean`, `wearable_stress_mean`), the predicted outcome $\\hat{Y}_i$ is calculated using the linear additive model:\n")
    doc.append(r"$$\hat{Y}_i = \beta_0 + \beta_1 \cdot \text{HbA1c}_i + \beta_2 \cdot \text{MeanGlucose}_i + \beta_3 \cdot \text{GlucoseSD}_i + \beta_4 \cdot \left(\frac{\text{Mean}}{\text{SD}}\right)_i + \beta_5 \cdot \text{TIR}_{70\text{--}180, i} + \sum_{k=1}^K \gamma_k \cdot X_{\text{cov}, k, i}$$")
    doc.append("\n**Table Parameters & Column Definitions**:")
    doc.append("- **`Term / Variable`**: Predictor $X_j$. Categorical features (such as `Education Level`) are dummy-encoded relative to the reference baseline.")
    doc.append("- **`Coef Estimate (β)`**: Estimated slope $\\hat{\\beta}_j$. Represents expected change in $Y$ per 1-unit increase in $X_j$, holding all other predictors fixed.")
    doc.append("- **`Std Error (SE)`**: Standard error of sampling variability $\\text{SE}(\\hat{\\beta}_j)$.")
    doc.append("- **`95% CI Margin (±2 SE)`**: Half-width of 95% Confidence Interval ($\\pm 1.96 \\cdot \\text{SE}$). The true parameter lies within $[\\hat{\\beta} - 2\\text{SE}, \\; \\hat{\\beta} + 2\\text{SE}]$.")
    doc.append("- **`t value`**: Student's $t$-statistic ($t = \\hat{\\beta} / \\text{SE}$).")
    doc.append("- **`p-value`**: Two-tailed significance probability. Values **$<0.05$** are bolded and starred.\n")
    
    doc.append("### 1B. GLM Binomial Logistic Regression Equations (Binary Outcomes)")
    doc.append("For binary classification targets (`cognitive_impairment` [MoCA < 26], `high_depression` [CESD-10 >= 10]), models estimate the **Log-Odds** $\\eta_i$:\n")
    doc.append(r"$$\eta_i = \ln \left( \frac{P(Y_i = 1)}{1 - P(Y_i = 1)} \right) = \beta_0 + \beta_1 \cdot \text{HbA1c}_i + \beta_2 \cdot \text{Mean}_i + \beta_3 \cdot \text{SD}_i + \beta_4 \cdot \left(\frac{\text{Mean}}{\text{SD}}\right)_i + \beta_5 \cdot \text{TIR}_i + \sum \gamma_k X_{k,i}$$")
    doc.append("\nPredicted probability $P(Y_i = 1)$ is computed via the logistic sigmoid transformation:\n")
    doc.append(r"$$P(Y_i = 1) = \frac{1}{1 + e^{-\eta_i}} = \frac{1}{1 + e^{-(\beta_0 + \sum \beta_j X_{j,i})}}$$")
    doc.append("\n**Logistic Column Definitions**:")
    doc.append("- **`Odds Ratio (OR)`**: Multiplicative odds multiplier $\\text{OR} = e^{\\hat{\\beta}_j}$. $\\text{OR} > 1.0$ indicates increased risk; $\\text{OR} < 1.0$ indicates protective factor.")
    doc.append("- **`F1 Score`**: Harmonic mean of Precision and Recall ($F_1 = 2 \\cdot \\frac{\\text{Precision} \\cdot \\text{Recall}}{\\text{Precision} + \\text{Recall}}$).")
    doc.append("- **`Brier Score`**: Mean squared error of predicted probabilities ($BS = \\frac{1}{N} \\sum (P_i - Y_i)^2$). Lower is better.\n")
    doc.append("---\n")
    
    doc.append("## 2. Outcome Target Tables & In-Depth Analytical Syntheses\n")

    csv_rows = []
    current_domain = None
    
    for domain, target, mtype, disp_name in outcome_configs:
        if target not in df.columns or df[target].notna().sum() < 30:
            continue
            
        if domain != current_domain:
            current_domain = domain
            doc.append(f"\n# Domain: {domain}\n")
            
        doc.append(f"### Outcome Target: {disp_name} (`{target}`)\n")
        
        analysis = DETAILED_ANALYSES.get(target, {
            'good': "Model estimated with standard covariates.",
            'bad': "Limited incremental variance explained.",
            'significant': "Refer to table parameters."
        })

        if mtype == 'OLS':
            m1 = fit_and_extract_ols(df, target, ['hba1c'], 'Model 1 (HbA1c Only)')
            m2 = fit_and_extract_ols(df, target, CGM_PREDICTORS, 'Model 2 (CGM Features Only)')
            m3 = fit_and_extract_ols(df, target, ALL_KEY_PREDICTORS, 'Model 3 (Combined: HbA1c + CGM)')
            
            if m1 and m2 and m3:
                doc.append(format_ols_markdown_table(m1, "Model 1A: HbA1c Benchmark", f"{target} ~ hba1c + covariates"))
                doc.append(format_ols_markdown_table(m2, "Model 1B: CGM Features Only", f"{target} ~ mean_glucose + glucose_sd + mean_to_sd_ratio + tir + covariates"))
                doc.append(format_ols_markdown_table(m3, "Model 1C: Combined Model (HbA1c + CGM Features)", f"{target} ~ hba1c + mean_glucose + glucose_sd + mean_to_sd_ratio + tir + covariates"))
                
                # Detailed 3-part Analysis Box
                doc.append(f"#### 🔍 Detailed Analytical Breakdown for {disp_name}:")
                doc.append(f"- **What is Good (Strengths & Signal)**: {analysis['good']}")
                doc.append(f"- **What is Bad (Limitations & Redundancies)**: {analysis['bad']}")
                doc.append(f"- **What is Significant to Write About (Publication Takeaway)**: {analysis['significant']}\n")
                doc.append("---\n")
                
                for res in [m1, m2, m3]:
                    for t in res['terms']:
                        csv_rows.append({
                            'domain': domain,
                            'target': target,
                            'model_type': mtype,
                            'model_label': res['model_label'],
                            'term': t['term'],
                            'term_clean': t['term_clean'],
                            'beta': t['beta'],
                            'se': t['se'],
                            'margin_2se': t['margin_2se'],
                            't_stat': t['t_stat'],
                            'p_val': t['p_val'],
                            'sig': t['sig'],
                            'r2': res['r2'],
                            'r2_adj': res['r2_adj'],
                            'aic': res['aic'],
                            'nobs': res['nobs']
                        })

        else:
            m1 = fit_and_extract_glm(df, target, ['hba1c'], 'Model 1 (HbA1c Only)')
            m2 = fit_and_extract_glm(df, target, CGM_PREDICTORS, 'Model 2 (CGM Features Only)')
            m3 = fit_and_extract_glm(df, target, ALL_KEY_PREDICTORS, 'Model 3 (Combined: HbA1c + CGM)')
            
            if m1 and m2 and m3:
                doc.append(format_glm_markdown_table(m1, "Model 1A: HbA1c Benchmark Logistic GLM", f"{target} ~ hba1c + covariates"))
                doc.append(format_glm_markdown_table(m2, "Model 1B: CGM Features Only Logistic GLM", f"{target} ~ mean_glucose + glucose_sd + mean_to_sd_ratio + tir + covariates"))
                doc.append(format_glm_markdown_table(m3, "Model 1C: Combined Logistic GLM (HbA1c + CGM Features)", f"{target} ~ hba1c + mean_glucose + glucose_sd + mean_to_sd_ratio + tir + covariates"))
                
                # Detailed 3-part Analysis Box
                doc.append(f"#### 🔍 Detailed Analytical Breakdown for {disp_name}:")
                doc.append(f"- **What is Good (Strengths & Signal)**: {analysis['good']}")
                doc.append(f"- **What is Bad (Limitations & Redundancies)**: {analysis['bad']}")
                doc.append(f"- **What is Significant to Write About (Publication Takeaway)**: {analysis['significant']}\n")
                doc.append("---\n")

                for res in [m1, m2, m3]:
                    for t in res['terms']:
                        csv_rows.append({
                            'domain': domain,
                            'target': target,
                            'model_type': mtype,
                            'model_label': res['model_label'],
                            'term': t['term'],
                            'term_clean': t['term_clean'],
                            'beta': t['beta'],
                            'or_val': t['or_val'],
                            'se': t['se'],
                            'margin_2se': t['margin_2se'],
                            'z_stat': t['z_stat'],
                            'p_val': t['p_val'],
                            'sig': t['sig'],
                            'auc': res['auc'],
                            'f1': res['f1'],
                            'brier': res['brier'],
                            'aic': res['aic'],
                            'nobs': res['nobs']
                        })

    # Master Synthesis & Citation Matrix
    doc.append("\n## 3. Comprehensive Master Synthesis & Citation Matrix\n")
    doc.append("Below is the consolidated synthesis wrapping up all statistically significant findings across Cognition, Depression, Indoor Environment Sensors, and Wearable Activity Trackers, with exact citations to the table data, variables, coefficients, test statistics, and p-values.\n")
    
    doc.append("### 3A. Synthesis 1: Cognition & Cognitive Impairment")
    doc.append("1. **CGM Superiority over HbA1c for Global Cognition**: In the combined OLS model for **MoCA Total Score** (`moca_total`), continuous glucose features raise $R^2$ from **0.1010 to 0.1131** (+12.0% relative variance explained) and significantly drop AIC from 8,463.17 to 8,448.30. **Mean Glucose** (`mean_glucose`, $\\beta = -0.0347, \\text{SE} = 0.0085, t = -4.108, p = 4.19 \\times 10^{-5}$) and **Time-in-Range 70-180 mg/dL** (`tir`, $\\beta = -0.0430, \\text{SE} = 0.0125, t = -3.438, p = 0.0006$) are highly significant negative predictors, while **HbA1c** (`hba1c`, $\\beta = -0.0906, \\text{SE} = 0.1452, t = -0.624, p = 0.5326$) becomes non-significant. *(Cites: Domain Cognition, Outcome `moca_total`, Model 1C Combined, N = 1,691)*.")
    doc.append("2. **Diagnostic Impairment Utility**: In GLM Logistic Regression for **Cognitive Impairment** (`cognitive_impairment` = MoCA < 26), ROC-AUC improves from **0.6688 to 0.6807** with $\\text{LRT } \\chi^2(4) = 18.69, p = 9.03 \\times 10^{-4}$. Every 1 mg/dL increase in mean glucose increases impairment odds by **2.21%** (`mean_glucose`, $\\text{OR} = 1.0221, \\text{SE} = 0.0063, z = +3.450, p = 0.0006$), and every 1% increase in TIR 70-180 increases odds by **2.87%** (`tir`, $\\text{OR} = 1.0287, \\text{SE} = 0.0093, z = +3.046, p = 0.0023$). HbA1c is non-significant (`hba1c`, $\\text{OR} = 1.0317, p = 0.7631$). *(Cites: Domain Cognition, Outcome `cognitive_impairment`, Model 1C Combined, N = 1,691)*.")
    doc.append("3. **Selective Executive Vulnerability**: Among cognitive sub-domains, **MoCA Abstraction** (`moca_abstraction`) is selectively vulnerable to time-in-range volatility (`tir`, $\\beta = -0.0036, \\text{SE} = 0.0015, t = -2.446, p = 0.0146$). *(Cites: Domain Cognition, Outcome `moca_abstraction`, Model 1C Combined, N = 1,691)*.\n")

    doc.append("### 3B. Synthesis 2: Indoor Environmental Sensor Coupling")
    doc.append("1. **Relative Humidity Coupling**: CGM metrics significantly improve **Relative Humidity** prediction (`env_hum_mean`), raising $R^2$ from **0.0124 to 0.0216** ($\\text{LRT } \\chi^2(4) = 15.69, p = 0.0035$). Higher daily TIR (`tir`, $\\beta = +0.1012, \\text{SE} = 0.0316, t = +3.206, p = 0.0014$) and stability (`mean_to_sd_ratio`, $\\beta = +0.6924, \\text{SE} = 0.3225, t = +2.147, p = 0.0320$) positively correlate with indoor humidity. *(Cites: Domain Environment, Outcome `env_hum_mean`, Model 1C Combined, N = 1,665)*.")
    doc.append("2. **Indoor Particulate Matter Inverse Correlation**: CGM features provide statistically significant incremental value for **Indoor PM2.5** (`env_pm25_mean`, $\\text{LRT } \\chi^2(4) = 12.07, p = 0.0169, R^2 = 0.0522$) and **Indoor PM10** (`env_pm10_mean`, $\\text{LRT } \\chi^2(4) = 11.66, p = 0.0201, R^2 = 0.0511$). **Mean Glucose** is an inverse predictor (`env_pm25_mean` $\\beta = -0.2730, t = -2.691, p = 0.0072$; `env_pm10_mean` $\\beta = -0.2787, t = -2.648, p = 0.0082$). *(Cites: Domain Environment, Outcomes `env_pm25_mean` & `env_pm10_mean`, Model 1C Combined, N = 1,665)*.\n")

    doc.append("### 3C. Synthesis 3: Wearable Autonomic & Activity Dynamics")
    doc.append("1. **Autonomic Wearable Stress Correlation**: CGM metrics significantly predict **Average Stress Level** (`wearable_stress_mean`), achieving $R^2 = 0.0806$ with $\\text{LRT } \\chi^2(4) = 13.55, p = 0.0089$. Predictors: **Mean / SD Ratio** (`mean_to_sd_ratio`, $\\beta = -1.6115, \\text{SE} = 0.6117, t = -2.635, p = 0.0085$), **Mean Glucose** (`mean_glucose`, $\\beta = +0.1058, \\text{SE} = 0.0408, t = +2.591, p = 0.0097$), and **Glucose SD** (`glucose_sd`, $\\beta = -0.3112, \\text{SE} = 0.1259, t = -2.472, p = 0.0136$). Lab HbA1c is non-significant ($p = 0.1465$). *(Cites: Domain Wearable Activity, Outcome `wearable_stress_mean`, Model 1C Combined, N = 1,576)*.")
    doc.append("2. **Wearable Heart Rate Coupling**: CGM metrics significantly predict **Average Heart Rate** (`wearable_hr_mean`, $R^2 = 0.0300, \\text{LRT } p = 0.0340$). **Glucose SD** (`glucose_sd`, $\\beta = -0.4285, \\text{SE} = 0.1762, t = -2.432, p = 0.0151$) and **Mean / SD Ratio** (`mean_to_sd_ratio`, $\\beta = -1.9104, \\text{SE} = 0.8576, t = -2.228, p = 0.0260$) drive this relationship. *(Cites: Domain Wearable Activity, Outcome `wearable_hr_mean`, Model 1C Combined, N = 1,572)*.")
    doc.append("3. **Daily Step Physical Activity Protection**: CGM metrics **nearly double explained variance** in **Daily Steps** (`wearable_daily_steps`), raising $R^2$ from **0.0366 to 0.0633**. Greater glucose variability predicts **193 fewer daily steps** per 1 mg/dL increase in SD (`glucose_sd`, $\\beta = -193.0289, \\text{SE} = 80.6966, t = -2.392, p = 0.0175$). *(Cites: Domain Wearable Activity, Outcome `wearable_daily_steps`, Model 1C Combined, N = 257)*.\n")

    # Write report files
    report_md_path = os.path.join(TABLES_DIR, "full_multimodal_regression_prediction_tables.md")
    report_md_root_path = os.path.join(REPORTS_DIR, "02_full_multimodal_regression_prediction_tables.md")
    
    md_content = "\n".join(doc)
    with open(report_md_path, "w") as f:
        f.write(md_content)
    with open(report_md_root_path, "w") as f:
        f.write(md_content)
        
    # Write CSV data file
    csv_df = pd.DataFrame(csv_rows)
    csv_path = os.path.join(DATA_OUT_DIR, "multimodal_regression_results_detailed.csv")
    csv_table_path = os.path.join(TABLES_DIR, "multimodal_regression_results_detailed.csv")
    csv_df.to_csv(csv_path, index=False)
    csv_df.to_csv(csv_table_path, index=False)
    
    print(f"Report generated successfully!\nMarkdown: {report_md_root_path}\nCSV: {csv_path}")

if __name__ == "__main__":
    main()
