import os
import json
import pandas as pd
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, "..", "dataset"))
CLINICAL_DIR = os.path.join(BASE_DIR, "clinical_data")
CGM_DIR = os.path.join(BASE_DIR, "wearable_blood_glucose", "continuous_glucose_monitoring", "dexcom_g6")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "data")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_cgm_metrics():
    print("Extracting CGM metrics...")
    cgm_data = []
    
    if not os.path.exists(CGM_DIR):
        print("CGM dir not found")
        return pd.DataFrame()
        
    for person_id in os.listdir(CGM_DIR):
        person_path = os.path.join(CGM_DIR, person_id)
        if not os.path.isdir(person_path):
            continue
            
        json_files = [f for f in os.listdir(person_path) if f.endswith(".json")]
        if not json_files:
            continue
            
        json_file = os.path.join(person_path, json_files[0])
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                
            readings = data.get('body', {}).get('cgm', [])
            glucose_values = [r.get('blood_glucose', {}).get('value') for r in readings if 'blood_glucose' in r and r['blood_glucose'].get('value') is not None]
            
            # Minimum 3 days of readings (1 reading / 5 min -> 288 readings / day -> 864 readings)
            if len(glucose_values) < 864:
                continue
                
            mean_glucose = np.mean(glucose_values)
            gmi = 3.31 + 0.02392 * mean_glucose
            
            # Time in range (70 - 180 mg/dL)
            in_range = [v for v in glucose_values if 70 <= v <= 180]
            tir = len(in_range) / len(glucose_values) * 100
            
            cgm_data.append({
                'person_id': int(person_id.replace('AIREADI-', '') if 'AIREADI-' in person_id else person_id),
                'mean_glucose': mean_glucose,
                'gmi': gmi,
                'tir': tir,
                'cgm_readings_count': len(glucose_values)
            })
        except Exception as e:
            print(f"Error parsing {json_file}: {e}")
            
    return pd.DataFrame(cgm_data)

def extract_clinical_data():
    print("Extracting clinical data...")
    # Participants
    df_parts = pd.read_csv(os.path.join(BASE_DIR, "participants.tsv"), sep="\t")
    df_parts = df_parts[['person_id', 'age', 'study_group']]
    
    # Measurements (BMI, MoCA)
    df_meas = pd.read_csv(os.path.join(CLINICAL_DIR, "measurement.csv"), low_memory=False)
    
    # BMI
    bmi_df = df_meas[df_meas['measurement_source_value'] == 'bmi_vsorres, BMI'].groupby('person_id')['value_as_number'].mean().reset_index()
    bmi_df.rename(columns={'value_as_number': 'bmi'}, inplace=True)
    
    # MoCA Total
    moca_total = df_meas[df_meas['measurement_source_value'] == 'moca_total_score'].groupby('person_id')['value_as_number'].max().reset_index()
    moca_total.rename(columns={'value_as_number': 'moca_total'}, inplace=True)
    
    # MoCA Memory
    moca_mem = df_meas[df_meas['measurement_source_value'] == 'moca_combined_mis_score'].groupby('person_id')['value_as_number'].max().reset_index()
    moca_mem.rename(columns={'value_as_number': 'moca_memory'}, inplace=True)
    
    moca_ori = df_meas[df_meas['measurement_source_value'] == 'moca_orientation'].groupby('person_id')['value_as_number'].max().reset_index()
    moca_ori.rename(columns={'value_as_number': 'moca_orientation'}, inplace=True)

    # Abstraction might be 'abstraction'
    moca_abs = df_meas[df_meas['measurement_source_value'] == 'moca_abstraction'].groupby('person_id')['value_as_number'].max().reset_index()
    moca_abs.rename(columns={'value_as_number': 'moca_abstraction'}, inplace=True)
    
    # HbA1c
    hba1c_df = df_meas[df_meas['measurement_source_value'].astype(str).str.contains('import_hba1c', case=False, na=False)].groupby('person_id')['value_as_number'].mean().reset_index()
    hba1c_df.rename(columns={'value_as_number': 'hba1c'}, inplace=True)
    
    # Conditions
    df_cond = pd.read_csv(os.path.join(CLINICAL_DIR, "condition_occurrence.csv"), low_memory=False)
    
    def get_condition_status(condition_codes):
        pattern = '|'.join(condition_codes)
        cond_df = df_cond[df_cond['condition_source_value'].str.contains(pattern, case=False, na=False)]
        return cond_df['person_id'].unique()
        
    htn_ids = get_condition_status(['mhoccur_hbp'])
    chol_ids = get_condition_status(['mhoccur_clsh'])
    kidney_ids = get_condition_status(['mhoccur_rnl'])
    circ_ids = get_condition_status(['mhoccur_circ', 'mhoccur_strk', 'mhoccur_mi'])
    neuro_ids = get_condition_status(['mhoccur_pd', 'mhoccur_ad', 'mhoccur_cogn', 'mhoccur_ms', 'mhoccur_cns'])
    
    # Observations (Education)
    df_obs = pd.read_csv(os.path.join(CLINICAL_DIR, "observation.csv"), low_memory=False)
    edu_df = df_obs[df_obs['observation_source_value'] == 'years_of_education'].groupby('person_id')['value_as_number'].max().reset_index()
    edu_df.rename(columns={'value_as_number': 'years_of_education'}, inplace=True)
    
    # Merge
    df = df_parts.copy()
    df = df.merge(bmi_df, on='person_id', how='left')
    df = df.merge(moca_total, on='person_id', how='left')
    df = df.merge(moca_mem, on='person_id', how='left')
    df = df.merge(moca_ori, on='person_id', how='left')
    df = df.merge(moca_abs, on='person_id', how='left')
    df = df.merge(edu_df, on='person_id', how='left')
    df = df.merge(hba1c_df, on='person_id', how='left')
    
    df['hypertension'] = df['person_id'].isin(htn_ids).astype(int)
    df['high_cholesterol'] = df['person_id'].isin(chol_ids).astype(int)
    df['kidney_disease'] = df['person_id'].isin(kidney_ids).astype(int)
    df['circulatory_problems'] = df['person_id'].isin(circ_ids).astype(int)
    df['neurodegenerative'] = df['person_id'].isin(neuro_ids).astype(int)
    
    # Education categorical
    def map_edu(years):
        if pd.isna(years):
            return np.nan
        if years <= 12:
            return 'High school or below'
        elif years <= 16:
            return 'College level'
        else:
            return 'Graduate level'
            
    df['education_level'] = df['years_of_education'].apply(map_edu)
    
    return df

if __name__ == "__main__":
    cgm_df = extract_cgm_metrics()
    print(f"Extracted CGM data for {len(cgm_df)} participants")
    
    clin_df = extract_clinical_data()
    print(f"Extracted clinical data for {len(clin_df)} participants")
    
    master_df = clin_df.merge(cgm_df, on='person_id', how='inner')
    print(f"Master dataset has {len(master_df)} participants with both clinical and >3 days CGM data.")
    
    master_df.to_csv(os.path.join(OUTPUT_DIR, "master_cgm_moca_dataset.csv"), index=False)
    print("Saved to master_cgm_moca_dataset.csv")
