import os
import json
import pandas as pd
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, "..", "dataset"))
CLINICAL_DIR = os.path.join(BASE_DIR, "clinical_data")
CGM_DIR = os.path.join(BASE_DIR, "wearable_blood_glucose", "continuous_glucose_monitoring", "dexcom_g6")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
os.makedirs(DATA_DIR, exist_ok=True)

def parse_glucose_val(raw_val):
    if raw_val is None:
        return None
    if isinstance(raw_val, (int, float)):
        return float(raw_val)
    val_str = str(raw_val).strip()
    if val_str.lower() == 'high':
        return 400.0
    if val_str.lower() == 'low':
        return 40.0
    try:
        return float(val_str)
    except ValueError:
        return None

def extract_cgm_spikes():
    print("Extracting CGM spike metrics from Dexcom G6 JSON files...")
    cgm_records = []
    
    if not os.path.exists(CGM_DIR):
        print(f"CGM Directory not found: {CGM_DIR}")
        return pd.DataFrame()
        
    person_dirs = [d for d in os.listdir(CGM_DIR) if os.path.isdir(os.path.join(CGM_DIR, d))]
    print(f"Found {len(person_dirs)} participant directories in Dexcom G6 folder.")
    
    for pdir in person_dirs:
        person_path = os.path.join(CGM_DIR, pdir)
        json_files = [f for f in os.listdir(person_path) if f.endswith(".json")]
        if not json_files:
            continue
            
        json_file = os.path.join(person_path, json_files[0])
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                
            readings = data.get('body', {}).get('cgm', [])
            if not readings:
                continue
                
            valid_readings = []
            for r in readings:
                val = parse_glucose_val(r.get('blood_glucose', {}).get('value'))
                t_str = r.get('effective_time_frame', {}).get('time_interval', {}).get('start_time') or r.get('start_time')
                if val is not None:
                    valid_readings.append({'value': val, 'time': t_str})
                    
            if len(valid_readings) < 864:
                continue
                
            glucose_vals = np.array([r['value'] for r in valid_readings])
            total_readings = len(glucose_vals)
            total_days = total_readings * 5.0 / 1440.0
            
            # Spike runs (glucose >= 180 mg/dL)
            spike_runs = []
            current_run = []
            for v in glucose_vals:
                if v >= 180.0:
                    current_run.append(v)
                else:
                    if len(current_run) > 0:
                        spike_runs.append(current_run)
                        current_run = []
            if len(current_run) > 0:
                spike_runs.append(current_run)
                
            num_spikes = len(spike_runs)
            avg_spikes_per_day = num_spikes / total_days if total_days > 0 else 0.0
            
            if num_spikes > 0:
                durations_min = [len(run) * 5.0 for run in spike_runs]
                avg_spike_duration_minutes = float(np.mean(durations_min))
                means_per_spike = [np.mean(run) for run in spike_runs]
                avg_cgm_per_spike_mg = float(np.mean(means_per_spike))
                peaks_per_spike = [np.max(run) for run in spike_runs]
                avg_peak_cgm_per_spike_mg = float(np.mean(peaks_per_spike))
            else:
                avg_spike_duration_minutes = 0.0
                avg_cgm_per_spike_mg = 0.0
                avg_peak_cgm_per_spike_mg = 0.0
                
            pid_clean = int(pdir.replace('AIREADI-', '')) if 'AIREADI-' in pdir else int(pdir)
            
            cgm_records.append({
                'person_id': pid_clean,
                'mean_glucose': float(np.mean(glucose_vals)),
                'gmi': 3.31 + 0.02392 * float(np.mean(glucose_vals)),
                'tir': float(np.sum((glucose_vals >= 70) & (glucose_vals <= 180)) / total_readings * 100.0),
                'cgm_days': total_days,
                'total_spikes': num_spikes,
                'avg_spikes_per_day': avg_spikes_per_day,
                'avg_spike_duration_minutes': avg_spike_duration_minutes,
                'avg_cgm_per_spike_mg': avg_cgm_per_spike_mg,
                'avg_peak_cgm_per_spike_mg': avg_peak_cgm_per_spike_mg
            })
            
        except Exception as e:
            print(f"Error reading {pdir}: {e}")
            
    df_cgm = pd.DataFrame(cgm_records)
    print(f"Processed {len(df_cgm)} participants with valid CGM spike metrics.")
    return df_cgm

def build_master_spike_dataset():
    df_cgm = extract_cgm_spikes()
    if df_cgm.empty:
        print("No CGM data extracted.")
        return
        
    print("Loading clinical participants.tsv...")
    df_parts = pd.read_csv(os.path.join(BASE_DIR, "participants.tsv"), sep="\t")
    
    print("Loading person.csv...")
    df_person = pd.read_csv(os.path.join(CLINICAL_DIR, "person.csv"), low_memory=False)
    df_person_clean = df_person[['person_id', 'gender_source_value', 'race_source_value', 'ethnicity_source_value']].copy()
    df_person_clean.rename(columns={
        'gender_source_value': 'sex',
        'race_source_value': 'race',
        'ethnicity_source_value': 'ethnicity'
    }, inplace=True)
    
    print("Loading measurement.csv...")
    df_meas = pd.read_csv(os.path.join(CLINICAL_DIR, "measurement.csv"), low_memory=False)
    
    # BMI
    bmi_df = df_meas[df_meas['measurement_source_value'] == 'bmi_vsorres, BMI'].groupby('person_id')['value_as_number'].mean().reset_index()
    bmi_df.rename(columns={'value_as_number': 'bmi'}, inplace=True)
    
    # MoCA total
    moca_df = df_meas[df_meas['measurement_source_value'] == 'moca_total_score'].groupby('person_id')['value_as_number'].max().reset_index()
    moca_df.rename(columns={'value_as_number': 'moca_total'}, inplace=True)
    
    # HbA1c
    hba1c_df = df_meas[df_meas['measurement_source_value'].astype(str).str.contains('import_hba1c', case=False, na=False)].groupby('person_id')['value_as_number'].mean().reset_index()
    hba1c_df.rename(columns={'value_as_number': 'hba1c'}, inplace=True)
    
    # Years of education
    df_obs = pd.read_csv(os.path.join(CLINICAL_DIR, "observation.csv"), low_memory=False)
    edu_df = df_obs[df_obs['observation_source_value'] == 'years_of_education'].groupby('person_id')['value_as_number'].max().reset_index()
    edu_df.rename(columns={'value_as_number': 'years_of_education'}, inplace=True)
    
    # Merge
    master = df_cgm.merge(df_parts[['person_id', 'age', 'study_group', 'clinical_site']], on='person_id', how='left')
    master = master.merge(df_person_clean, on='person_id', how='left')
    master = master.merge(moca_df, on='person_id', how='left')
    master = master.merge(bmi_df, on='person_id', how='left')
    master = master.merge(hba1c_df, on='person_id', how='left')
    master = master.merge(edu_df, on='person_id', how='left')
    
    # Binary Cognitive Impairment indicator
    master['cognitively_impaired'] = (master['moca_total'] < 26).astype(float)
    master.loc[master['moca_total'].isna(), 'cognitively_impaired'] = np.nan
    
    # Age indicator
    master['age_gt_65'] = (master['age'] > 65).astype(float)
    
    # Exact Diabetes Classification based on study_group values:
    def assign_diabetes_status(sg):
        sg_str = str(sg).lower()
        if 'oral' in sg_str or 'insulin' in sg_str:
            return 1.0
        return 0.0

    def assign_diabetes_type(sg):
        sg_str = str(sg).lower()
        if 'oral' in sg_str:
            return 'Type 2 Diabetes (Oral/Injectable)'
        elif 'insulin' in sg_str:
            return 'Insulin-Dependent Diabetes'
        elif 'pre' in sg_str:
            return 'Pre-Diabetes'
        elif 'healthy' in sg_str:
            return 'Healthy Control'
        else:
            return 'Healthy Control'
            
    master['is_diabetic'] = master['study_group'].apply(assign_diabetes_status)
    master['diabetes_type'] = master['study_group'].apply(assign_diabetes_type)
    
    out_path = os.path.join(DATA_DIR, "master_cgm_spikes_dataset.csv")
    master.to_csv(out_path, index=False)
    print(f"Successfully updated master CGM spike dataset at {out_path} with {len(master)} rows.")
    print("Study Group Value Counts in Master:")
    print(master['study_group'].value_counts(dropna=False))
    print("Is Diabetic Counts:")
    print(master['is_diabetic'].value_counts(dropna=False))

if __name__ == "__main__":
    build_master_spike_dataset()
