import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors

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

def run_causal_inference():
    df = pd.read_csv(os.path.join(DATA_DIR, "master_extended_dataset.csv"))
    
    # Impute basic missing values
    for col in ['age', 'bmi', 'gmi', 'hba1c']:
        df[col] = df[col].fillna(df[col].median())
    df['education_level'] = df['education_level'].fillna(df['education_level'].mode()[0])
    
    # Drop rows missing moca or clinical site
    df.dropna(subset=['moca_total', 'clinical_site'], inplace=True)
    
    covariates_str = "age + C(education_level) + bmi + hypertension + high_cholesterol + kidney_disease + circulatory_problems + neurodegenerative"
    
    report = ["# Advanced Econometric & Causal Inference Analysis on MoCA"]
    report.append("\nThis report applies rigorous causal inference methods to isolate the marginal effect of variables on cognitive impairment.\n")
    
    # ==========================================
    # 1. Frisch-Waugh-Lovell (FWL) Theorem
    # ==========================================
    report.append("## 1. Frisch-Waugh-Lovell (FWL) Theorem (Partialing Out)")
    report.append("By the FWL theorem, regressing MoCA on GMI and Covariates yields the exact same coefficient for GMI as regressing the *residuals* of MoCA on the *residuals* of GMI. This isolates the pure, marginal variation in GMI independent of confounders.\n")
    
    # Standard OLS
    mod_standard = smf.ols(f"moca_total ~ gmi + {covariates_str}", data=df).fit()
    beta_gmi_std = mod_standard.params['gmi']
    
    # FWL Step 1: Regress MoCA on Covariates -> Residuals
    mod_moca = smf.ols(f"moca_total ~ {covariates_str}", data=df).fit()
    df['moca_res'] = mod_moca.resid
    
    # FWL Step 2: Regress GMI on Covariates -> Residuals
    mod_gmi = smf.ols(f"gmi ~ {covariates_str}", data=df).fit()
    df['gmi_res'] = mod_gmi.resid
    
    # FWL Step 3: Regress moca_res on gmi_res (without intercept to match FWL strictly, or with intercept which is ~0)
    mod_fwl = smf.ols("moca_res ~ gmi_res - 1", data=df).fit()
    beta_gmi_fwl = mod_fwl.params['gmi_res']
    
    report.append(f"- **Standard Multivariable GMI Coefficient**: {beta_gmi_std:.5f}")
    report.append(f"- **FWL Theorem Isolated Marginal Effect**: {beta_gmi_fwl:.5f}")
    report.append("- *Notice they are exactly identical, proving the confounding effects have been perfectly partialled out.*")
    
    # ==========================================
    # 2. Fixed Effects (Clinical Site)
    # ==========================================
    report.append("\n## 2. Fixed Effects (Absorbing Spatial Heterogeneity)")
    report.append("We add fixed effects for `clinical_site` to control for unobserved variables related to the specific hospital/geography where the patient was treated.\n")
    
    mod_fe = smf.ols(f"moca_total ~ gmi + {covariates_str} + C(clinical_site)", data=df).fit()
    beta_fe = mod_fe.params['gmi']
    pval_fe = mod_fe.pvalues['gmi']
    report.append(f"- **Fixed Effects GMI Coefficient**: {beta_fe:.5f} (p-value: {format_p(pval_fe)})")
    
    # ==========================================
    # 3. Propensity Score Matching (PSM)
    # ==========================================
    report.append("\n## 3. Propensity Score Matching (PSM)")
    report.append("We evaluate the Average Treatment Effect on the Treated (ATT) of being Diabetic (Treatment) on MoCA (Outcome), by matching Diabetic patients to Healthy patients with nearly identical Propensity Scores.\n")
    
    df['treated'] = (df['study_group'] != 'healthy').astype(int)
    
    # Predict propensity score
    X_psm = df[['age', 'bmi', 'hypertension', 'high_cholesterol', 'kidney_disease']]
    y_psm = df['treated']
    
    # We must drop NAs for PSM
    psm_mask = X_psm.notna().all(axis=1)
    df_psm = df[psm_mask].copy()
    X_psm = df_psm[['age', 'bmi', 'hypertension', 'high_cholesterol', 'kidney_disease']]
    y_psm = df_psm['treated']
    
    psm_model = LogisticRegression(solver='liblinear')
    psm_model.fit(X_psm, y_psm)
    df_psm['propensity_score'] = psm_model.predict_proba(X_psm)[:, 1]
    
    treated_idx = df_psm[df_psm['treated'] == 1].index
    control_idx = df_psm[df_psm['treated'] == 0].index
    
    nn = NearestNeighbors(n_neighbors=1)
    nn.fit(df_psm.loc[control_idx, ['propensity_score']])
    
    distances, indices = nn.kneighbors(df_psm.loc[treated_idx, ['propensity_score']])
    
    matched_control_idx = control_idx[indices.flatten()]
    
    treated_moca = df_psm.loc[treated_idx, 'moca_total'].values
    matched_control_moca = df_psm.loc[matched_control_idx, 'moca_total'].values
    
    att = np.mean(treated_moca - matched_control_moca)
    
    report.append(f"- **Treated N (Diabetic)**: {len(treated_idx)}")
    report.append(f"- **Matched Control N (Healthy)**: {len(matched_control_idx)}")
    report.append(f"- **ATT (Average Treatment Effect on Treated)**: {att:.4f} MoCA points")
    if att < 0:
        report.append(f"  *(Diabetic patients score {abs(att):.4f} points lower on MoCA than their exact propensity-matched healthy twins)*")
        
    # ==========================================
    # 4. Instrumental Variables (2SLS)
    # ==========================================
    report.append("\n## 4. Instrumental Variables (2SLS Framework)")
    report.append("We test various potentially exogenous instruments for GMI to eliminate endogeneity bias. The First Stage regresses GMI on the Instrument + Covariates. The Second Stage regresses MoCA on the predicted GMI + Covariates.\n")
    report.append("| Instrument | First-Stage F-stat (Strength) | 2SLS GMI Coef | 2SLS p-value |")
    report.append("| --- | --- | --- | --- |")
    
    instruments = ['age', 'C(education_level)', 'C(clinical_site)', 'hypertension', 'bmi']
    
    for inst in instruments:
        try:
            # Stage 1: Endogenous (GMI) ~ Instrument + Covariates
            stage1_formula = f"gmi ~ {inst} + {covariates_str}"
            stage1_mod = smf.ols(stage1_formula, data=df).fit()
            
            # F-test for instrument strength
            # To test if instrument is strong, we do an F-test on the instrument's coefficient(s)
            # Find the names of the instrument params
            inst_params = [p for p in stage1_mod.params.index if inst.split('(')[0] in p or inst in p]
            # Exclude covariates that might share substrings
            inst_params = [p for p in inst_params if p not in ['age', 'bmi', 'hypertension'] or p == inst]
            
            if len(inst_params) > 0:
                f_test = stage1_mod.f_test(f" = ".join(inst_params) + " = 0")
                f_stat = f_test.fvalue
            else:
                f_stat = np.nan
                
            df['gmi_hat'] = stage1_mod.fittedvalues
            
            # Stage 2: Outcome (MoCA) ~ Predicted Endogenous + Covariates
            stage2_formula = f"moca_total ~ gmi_hat + {covariates_str}"
            stage2_mod = smf.ols(stage2_formula, data=df).fit()
            
            iv_coef = stage2_mod.params['gmi_hat']
            iv_pval = stage2_mod.pvalues['gmi_hat']
            
            report.append(f"| {inst} | {f_stat:.2f} | {iv_coef:.4f} | {format_p(iv_pval)} |")
        except Exception as e:
            report.append(f"| {inst} | Error | Error | Error |")
            
    out_file = os.path.join(REPORTS_DIR, "causal_inference_results.md")
    with open(out_file, "w") as f:
        f.write("\n".join(report))
        
    print(f"Saved {out_file}")

if __name__ == "__main__":
    run_causal_inference()
