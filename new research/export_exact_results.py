import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import os

BASE_DIR = os.path.abspath("../dataset")
CLINICAL_DIR = os.path.join(BASE_DIR, "clinical_data")
OUTPUT_DIR = os.path.abspath(".")

def run_regression_and_extract(df, formula, family=None, model_name="", metric=""):
    try:
        if family == 'binomial':
            model = smf.glm(formula, data=df, family=sm.families.Binomial()).fit()
            is_logistic = True
        else:
            model = smf.ols(formula, data=df).fit()
            is_logistic = False
            
        params = model.params
        bse = model.bse
        pvals = model.pvalues
        conf_int = model.conf_int()
        
        results = []
        for term in params.index:
            coef = params[term]
            se = bse[term]
            p = pvals[term]
            ci_low = conf_int.loc[term, 0]
            ci_high = conf_int.loc[term, 1]
            
            row = {
                'model_name': model_name,
                'metric': metric,
                'term': term,
                'coef_beta': coef,
                'standard_error': se,
                'p_value': p,
                'ci_lower_bound': ci_low,
                'ci_upper_bound': ci_high
            }
            
            if is_logistic:
                row['odds_ratio'] = np.exp(coef)
                row['or_ci_lower'] = np.exp(ci_low)
                row['or_ci_upper'] = np.exp(ci_high)
            else:
                row['odds_ratio'] = np.nan
                row['or_ci_lower'] = np.nan
                row['or_ci_upper'] = np.nan
                
            results.append(row)
            
        return pd.DataFrame(results)
    except Exception as e:
        print(f"Error fitting {model_name} with {metric}: {e}")
        return pd.DataFrame()

def main():
    print("Loading datasets...")
    df = pd.read_csv("master_cgm_moca_dataset.csv")
    df_cond = pd.read_csv(os.path.join(CLINICAL_DIR, "condition_occurrence.csv"), low_memory=False)
    
    # Map groups
    group_map = {
        'healthy': '1_Controls',
        'pre_diabetes_lifestyle_controlled': '2_Pre-diabetes',
        'oral_medication_and_or_non_insulin_injectable_medication_controlled': '3_Medication-controlled',
        'insulin_dependent': '4_Insulin-dependent'
    }
    df['group'] = df['study_group'].map(group_map)
    df.dropna(subset=['group', 'moca_total'], inplace=True)
    
    # Impute missing values with median/mode
    for col in ['age', 'bmi', 'gmi', 'mean_glucose', 'tir', 'hba1c']:
        df[col] = df[col].fillna(df[col].median())
    for col in ['education_level']:
        df[col] = df[col].fillna(df[col].mode()[0])
        
    df['cognitive_impairment_moca'] = (df['moca_total'] < 26).astype(int)
    
    # Extract specific cognitive diseases
    cog_conditions = {
        'alzheimers': 'mhoccur_ad',
        'parkinsons': 'mhoccur_pd',
        'cognitive_impairment_clinical': 'mhoccur_cogn',
        'multiple_sclerosis': 'mhoccur_ms',
        'cns_disease': 'mhoccur_cns'
    }
    
    for col_name, pattern in cog_conditions.items():
        cond_subset = df_cond[df_cond['condition_source_value'].str.contains(pattern, case=False, na=False)]
        pids = cond_subset['person_id'].unique()
        df[col_name] = df['person_id'].isin(pids).astype(int)
        
    all_results = []
    
    # Define models
    targets = [
        ('cognitive_impairment_moca', 'Total Cognitive Impairment (MoCA < 26)'),
        ('alzheimers', "Alzheimer's Disease"),
        ('parkinsons', "Parkinson's Disease"),
        ('cognitive_impairment_clinical', "Clinical Cognitive Impairment"),
        ('multiple_sclerosis', "Multiple Sclerosis"),
        ('cns_disease', "CNS Disease")
    ]
    
    for target_col, model_desc in targets:
        # We predict the target using group (diabetes severity) + covariates
        
        # 1. GMI as covariate
        formula_gmi = f"{target_col} ~ C(group, Treatment('1_Controls')) + age + C(education_level) + bmi + gmi + hypertension + high_cholesterol + kidney_disease + circulatory_problems"
        res_gmi = run_regression_and_extract(df, formula_gmi, family='binomial', model_name=model_desc, metric='GMI')
        all_results.append(res_gmi)
        
        # 2. HbA1c as covariate
        formula_hba1c = f"{target_col} ~ C(group, Treatment('1_Controls')) + age + C(education_level) + bmi + hba1c + hypertension + high_cholesterol + kidney_disease + circulatory_problems"
        res_hba1c = run_regression_and_extract(df, formula_hba1c, family='binomial', model_name=model_desc, metric='HbA1c')
        all_results.append(res_hba1c)
        
    final_df = pd.concat(all_results, ignore_index=True)
    
    # Separate outputs
    moca_df = final_df[final_df['model_name'] == 'Total Cognitive Impairment (MoCA < 26)']
    specific_df = final_df[final_df['model_name'] != 'Total Cognitive Impairment (MoCA < 26)']
    
    moca_df.to_csv("regression_results_total_moca.csv", index=False)
    specific_df.to_csv("regression_results_specific_impairments.csv", index=False)
    
    print("Exported exact regression results to CSVs.")
    
if __name__ == "__main__":
    main()
