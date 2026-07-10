import pandas as pd
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from scipy.stats import spearmanr

warnings.filterwarnings('ignore')

# --- CONFIGURATION ---
INPUT_FOLDER_5MIN = os.path.abspath("../output_omnibus_5min")
INPUT_FOLDER_HOURLY = os.path.abspath("../output_omnibus_hourly")
OUTPUT_FOLDER = os.path.abspath("../eda_advanced_outputs")
MEASUREMENT_FILE = os.path.abspath("../dataset/clinical_data/measurement.csv")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "data"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "summary_tables"), exist_ok=True)

sns.set_theme(style="whitegrid")

TARGET_META_VARS = [
    'meta_study_group', 'meta_age', 'meta_study_visit_date',
    'meta_recommended_split', 'meta_clinical_data'
]

# --- BRAINSTORMING ---
print("="*60)
print("BRAINSTORM: Cognitive Ways to Investigate Cognition vs Diabetes Management")
print("="*60)
print("1. Peripheral Neuropathy Monofilament Testing: Diminished sensation limits physical activity and increases mental toll, correlating with accelerated cognitive decline.")
print("2. CGM Data Upload/Maintenance Frequency: A robust proxy for executive function and adherence. Lower cognition patients may have higher gap rates in CGM/Activity wearing.")
print("3. Hypo/Hyperglycemia Reactivity Time: Time taken to correct blood glucose extremities (using CGM timestamps) acts as an objective continuous cognitive execution test.")
print("4. Dietary Intake Logs Compliance: Tracking consistency and detail of nutritional logging over time as an indirect metric for working memory and planning.")
print("="*60)


def extract_patient_features():
    print(f"Loading MOCA scores from {MEASUREMENT_FILE}...")
    try:
        meas_df = pd.read_csv(MEASUREMENT_FILE, low_memory=False, usecols=['person_id', 'measurement_source_value', 'value_as_number', 'measurement_date'])
        
        moca_sources = ['moca_total_score', 'moca_abstraction', 'moca_orientation', 'moca_combined_mis_score']
        moca_df = meas_df[meas_df['measurement_source_value'].isin(moca_sources)].copy()
        
        # Prepare longitudinal MOCA data
        moca_df['person_id'] = moca_df['person_id'].astype(str)
        moca_df.dropna(subset=['value_as_number'], inplace=True)
        
        moca_longitudinal = moca_df.pivot_table(index=['person_id', 'measurement_date'], 
                                                columns='measurement_source_value', 
                                                values='value_as_number', aggfunc='mean').reset_index()
        
        moca_longitudinal.rename(columns={'person_id': 'participant_id', 'measurement_date': 'date', 'moca_total_score': 'moca_score'}, inplace=True)
        moca_longitudinal.dropna(subset=['moca_score'], inplace=True)
        
        # Save longitudinal data
        moca_longitudinal.to_csv(os.path.join(OUTPUT_FOLDER, "data", "moca_longitudinal.csv"), index=False)
        print(f"Saved longitudinal MOCA scores for {moca_longitudinal['participant_id'].nunique()} patients.")
        
        # Aggregate per patient
        moca_agg = moca_longitudinal.groupby('participant_id').agg(
            moca_mean=('moca_score', 'mean'),
            moca_variance=('moca_score', 'var'),
            moca_tests_taken=('moca_score', 'count')
        ).reset_index()
        moca_agg['moca_variance'].fillna(0, inplace=True) # Fill variance with 0 if only 1 test taken
        
        for sub_col in ['moca_abstraction', 'moca_orientation', 'moca_combined_mis_score']:
            if sub_col in moca_longitudinal.columns:
                sub_means = moca_longitudinal.groupby('participant_id')[sub_col].mean().reset_index()
                moca_agg = moca_agg.merge(sub_means, on='participant_id', how='left')
                
        moca_dict = moca_agg.set_index('participant_id').to_dict('index')
    except Exception as e:
        print(f"Failed to load or parse measurements: {e}")
        moca_dict = {}

    print(f"Loading files from {INPUT_FOLDER_5MIN} for patient feature extraction...")
    files = glob.glob(os.path.join(INPUT_FOLDER_5MIN, "*_OMNIBUS_5MIN.csv"))
    
    records = []
    
    for f in files:
        try:
            df = pd.read_csv(f, low_memory=False, parse_dates=['timestamp'])
            if df.empty: continue
            
            p_id = os.path.basename(f).split('_')[1].replace('P', '')
            
            # --- Objective Physiological Extraction ---
            mean_glucose = df['blood_glucose.value'].mean() if 'blood_glucose.value' in df.columns else np.nan
            
            df['hour'] = df['timestamp'].dt.hour
            night_df = df[(df['hour'] >= 22) | (df['hour'] <= 6)]
            day_df = df[(df['hour'] > 6) & (df['hour'] < 22)]
            
            night_mean_hr = night_df['heart_rate.value'].mean() if 'heart_rate.value' in night_df.columns and not night_df.empty else np.nan
            night_movement = night_df['base_movement_quantity.value'].sum() if 'base_movement_quantity.value' in night_df.columns and not night_df.empty else np.nan
            min_spo2 = df['oxygen_saturation.value'].min() if 'oxygen_saturation.value' in df.columns else np.nan
            
            # Physical activity proxies
            day_hr = day_df['heart_rate.value'].mean() if 'heart_rate.value' in day_df.columns and not day_df.empty else np.nan
            total_movement = df['base_movement_quantity.value'].sum() if 'base_movement_quantity.value' in df.columns else np.nan
            
            # Metadata
            meta_data = {}
            for var in TARGET_META_VARS:
                if var in df.columns:
                    meta_data[var] = df[var].iloc[0]
                else:
                    meta_data[var] = np.nan
                    
            # MOCA check / validation - Extract from measurement.csv aggregated dictionary
            age = float(meta_data.get('meta_age', 65)) if pd.notna(meta_data.get('meta_age')) else 65
            
            p_moca_info = moca_dict.get(p_id, {})
            moca_score = p_moca_info.get('moca_mean', np.nan)
            moca_variance = p_moca_info.get('moca_variance', 0)
            moca_tests_taken = p_moca_info.get('moca_tests_taken', 0)
            moca_abstraction = p_moca_info.get('moca_abstraction', np.nan)
            moca_orientation = p_moca_info.get('moca_orientation', np.nan)
            moca_combined_mis_score = p_moca_info.get('moca_combined_mis_score', np.nan)
                
            # Stratify Cognition
            if moca_score >= 26:
                cog_status = "Healthy (26-30)"
            elif moca_score >= 18:
                cog_status = "MCI (18-25)"
            else:
                cog_status = "Severe (<18)"
                
            # Age Brackets
            if age < 40:
                age_bracket = '<40'
            elif age <= 55:
                age_bracket = '40-55'
            else:
                age_bracket = '>55'

            base_record = {
                'participant_id': p_id,
                'mean_glucose': mean_glucose,
                'night_mean_hr': night_mean_hr,
                'night_movement': night_movement,
                'min_spo2': min_spo2,
                'day_hr': day_hr,
                'total_movement': total_movement,
                'moca_score': moca_score,
                'moca_abstraction': moca_abstraction,
                'moca_orientation': moca_orientation,
                'moca_combined_mis_score': moca_combined_mis_score,
                'moca_variance': moca_variance,
                'moca_tests_taken': moca_tests_taken,
                'cog_status': cog_status,
                'age_bracket': age_bracket
            }
            base_record.update(meta_data)
            records.append(base_record)
            
        except Exception as e:
            print(f"Error extracting patient features from {f}: {e}")
            continue

    return pd.DataFrame(records)

def create_summary_tables():
    """Generates 5-minute and hourly summary tables for all patients by aggregating existing datasets"""
    print("Generating 5-minute summary tables...")
    files_5m = glob.glob(os.path.join(INPUT_FOLDER_5MIN, "*_OMNIBUS_5MIN.csv"))
    summary_5m = []
    
    for f in files_5m: # Process all files
        df = pd.read_csv(f, low_memory=False)
        p_id = os.path.basename(f).split('_')[1]
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            means = df[numeric_cols].mean().to_dict()
            means['participant_id'] = p_id
            summary_5m.append(means)
            
    if summary_5m:
        df_5m = pd.DataFrame(summary_5m)
        df_5m.to_csv(os.path.join(OUTPUT_FOLDER, "summary_tables", "all_patients_5min_summary.csv"), index=False)
        
    print("Generating hourly summary tables...")
    files_hr = glob.glob(os.path.join(INPUT_FOLDER_HOURLY, "*_OMNIBUS_*.csv"))
    if not files_hr: files_hr = glob.glob(os.path.join(INPUT_FOLDER_5MIN, "*_OMNIBUS_5MIN.csv"))
    summary_hr = []
    for f in files_hr:
        df = pd.read_csv(f, low_memory=False)
        p_id = os.path.basename(f).split('_')[1]
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            means = df[numeric_cols].mean().to_dict()
            means['participant_id'] = p_id
            summary_hr.append(means)
            
    if summary_hr:
        df_hr = pd.DataFrame(summary_hr)
        df_hr.to_csv(os.path.join(OUTPUT_FOLDER, "summary_tables", "all_patients_hourly_summary.csv"), index=False)

def bootstrap_mean_diff(df, target_var, group_col='meta_study_group', n_iterations=2000):
    if group_col not in df.columns or target_var not in df.columns:
        print(f"Missing {group_col} or {target_var} for bootstrapping.")
        return
        
    groups = df[group_col].dropna().unique()
    if len(groups) < 2:
        return
        
    results = []
    for i in range(len(groups)):
        for j in range(i+1, len(groups)):
            g1, g2 = groups[i], groups[j]
            data1 = df[df[group_col] == g1][target_var].dropna().values
            data2 = df[df[group_col] == g2][target_var].dropna().values
            
            if len(data1) < 2 or len(data2) < 2: continue
            
            diffs = []
            for _ in range(n_iterations):
                sample1 = np.random.choice(data1, size=len(data1), replace=True)
                sample2 = np.random.choice(data2, size=len(data2), replace=True)
                diffs.append(np.mean(sample1) - np.mean(sample2))
                
            mean_diff = np.mean(diffs)
            ci_lower = np.percentile(diffs, 2.5)
            ci_upper = np.percentile(diffs, 97.5)
            
            results.append({
                'Group 1': g1, 'Group 2': g2, 
                'Mean Diff': mean_diff, '2.5% CI': ci_lower, '97.5% CI': cid_upper if 'cid_upper' in locals() else ci_upper
            })
            
    res_df = pd.DataFrame(results)
    res_df.to_csv(os.path.join(OUTPUT_FOLDER, f"bootstrap_diff_{target_var}.csv"), index=False)
    print(f"\nBootstrap Mean Differences for {target_var}:")
    print(res_df)


if __name__ == "__main__":
    df = extract_patient_features()
    if not df.empty:
        # Simulated class assignment if missing (use 'Unknown/Unassigned' instead of dropping or random)
        if 'meta_study_group' not in df.columns or df['meta_study_group'].isna().all():
            df['meta_study_group'] = 'Unknown/Unassigned'
        else:
            df['meta_study_group'] = df['meta_study_group'].fillna('Unknown/Unassigned')
            
        df.to_csv(os.path.join(OUTPUT_FOLDER, "data", "master_patient_features.csv"), index=False)
        
        create_summary_tables()
        
        print(f"Patient extraction complete. Results in {OUTPUT_FOLDER}. Proceed to run moca_analysis.py for further analysis.")
    else:
        print("No patient data compiled.")
