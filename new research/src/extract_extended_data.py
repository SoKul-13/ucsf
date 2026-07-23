import os
import pandas as pd
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, "..", "dataset"))
CLINICAL_DIR = os.path.join(BASE_DIR, "clinical_data")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
os.makedirs(DATA_DIR, exist_ok=True)

def extract_extended_data():
    print("Loading existing master dataset...")
    df_master = pd.read_csv(os.path.join(DATA_DIR, "master_cgm_moca_dataset.csv"))
    
    print("Loading participants.tsv for clinical_site...")
    df_parts = pd.read_csv(os.path.join(BASE_DIR, "participants.tsv"), sep="\t")
    df_parts = df_parts[['person_id', 'clinical_site']]
    
    print("Loading observation.csv for survey data...")
    df_obs = pd.read_csv(os.path.join(CLINICAL_DIR, "observation.csv"), low_memory=False)
    
    survey_vars = {
        'cestl': 'depression_score',
        'dietscore': 'diet_score',
        'susmkncf': 'smoked_100_cigs',
        'sualckncf': 'consumed_alcohol',
        'sumrjkncf': 'used_marijuana',
        'suvpkncf1': 'used_vape',
        'via1': 'vision_difficulty_distance',
        'via2': 'vision_difficulty_near',
        'via3': 'vision_difficulty_overall',
        'via6': 'last_eye_exam'
    }
    
    # Filter observations
    # observation_source_value has formats like "cestl, CESD-10 Score"
    pivot_df = pd.DataFrame({'person_id': df_master['person_id'].unique()})
    
    for obs_code, col_name in survey_vars.items():
        sub = df_obs[df_obs['observation_source_value'].astype(str).str.contains(obs_code, case=False, na=False)]
        
        # Determine if it's primarily numeric or string
        # Some surveys answer with numbers, some with strings ("Yes", "No")
        if sub['value_as_number'].notna().sum() > sub['value_as_string'].notna().sum():
            val_df = sub.groupby('person_id')['value_as_number'].max().reset_index()
            val_df.rename(columns={'value_as_number': col_name}, inplace=True)
        else:
            val_df = sub.groupby('person_id')['value_as_string'].first().reset_index()
            val_df.rename(columns={'value_as_string': col_name}, inplace=True)
            
        pivot_df = pivot_df.merge(val_df, on='person_id', how='left')
        
    # Merge with master
    df_extended = df_master.merge(df_parts, on='person_id', how='left')
    df_extended = df_extended.merge(pivot_df, on='person_id', how='left')
    
    # Save
    out_path = os.path.join(DATA_DIR, "master_extended_dataset.csv")
    df_extended.to_csv(out_path, index=False)
    print(f"Saved extended dataset with {len(df_extended)} rows to {out_path}")

if __name__ == "__main__":
    extract_extended_data()
