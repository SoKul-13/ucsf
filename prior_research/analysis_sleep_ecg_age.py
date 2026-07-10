import pandas as pd
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from scipy.stats import spearmanr
from itertools import combinations

warnings.filterwarnings('ignore')

# --- CONFIGURATION ---
INPUT_FOLDER_5MIN = os.path.abspath("../output_omnibus_5min")
OUTPUT_FOLDER = os.path.abspath("../eda_sleep_ecg_age_outputs")
MEASUREMENT_FILE = os.path.abspath("../dataset/clinical_data/measurement.csv")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "data"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "plots", "moca_age_stratified"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "plots", "sleep_analysis"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "plots", "ecg_analysis"), exist_ok=True)

sns.set_theme(style="whitegrid")

TARGET_META_VARS = [
    'meta_study_group', 'meta_age', 'meta_study_visit_date'
]

ECG_COLS = ['ecg_Rate', 'ecg_PR', 'ecg_QRSD', 'ecg_QT', 'ecg_QTc']

def extract_patient_features():
    print(f"Loading MOCA scores from {MEASUREMENT_FILE}...")
    try:
        meas_df = pd.read_csv(MEASUREMENT_FILE, low_memory=False, usecols=['person_id', 'measurement_source_value', 'value_as_number', 'measurement_date'])
        moca_sources = ['moca_total_score', 'moca_abstraction', 'moca_orientation', 'moca_combined_mis_score']
        moca_df = meas_df[meas_df['measurement_source_value'].isin(moca_sources)].copy()
        
        moca_df['person_id'] = moca_df['person_id'].astype(str)
        moca_df.dropna(subset=['value_as_number'], inplace=True)
        
        moca_longitudinal = moca_df.pivot_table(index=['person_id', 'measurement_date'], 
                                                columns='measurement_source_value', 
                                                values='value_as_number', aggfunc='mean').reset_index()
        
        moca_longitudinal.rename(columns={'person_id': 'participant_id', 'measurement_date': 'date', 'moca_total_score': 'moca_score'}, inplace=True)
        moca_longitudinal.dropna(subset=['moca_score'], inplace=True)
        
        moca_agg = moca_longitudinal.groupby('participant_id').agg(
            moca_mean=('moca_score', 'mean')
        ).reset_index()
                
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
            
            # --- Glucose / Sugar Spikes ---
            mean_glucose = np.nan
            std_glucose = np.nan
            time_above_180_pct = np.nan
            rapid_glucose_changes = np.nan
            
            if 'blood_glucose.value' in df.columns and df['blood_glucose.value'].notna().any():
                bg = df['blood_glucose.value'].dropna()
                mean_glucose = bg.mean()
                std_glucose = bg.std()
                time_above_180_pct = (bg > 180).mean() * 100
                rapid_glucose_changes = (bg.diff().abs() >= 15).sum() # Count of jumps > 15 mg/dL per 5 min

            # --- Sleep Proxies ---
            df['hour'] = df['timestamp'].dt.hour
            night_df = df[(df['hour'] >= 22) | (df['hour'] <= 6)]
            day_df = df[(df['hour'] > 6) & (df['hour'] < 22)]
            
            night_sleep_hrs = np.nan
            day_sleep_hrs = np.nan
            overall_sleep_hrs = np.nan
            
            if 'base_movement_quantity.value' in df.columns and df['base_movement_quantity.value'].notna().any():
                # Proxy: interval with very low movement (< 0.1) counts as sleep
                # Each row = 5 minutes = 1/12 hour
                night_sleep_hrs = (night_df['base_movement_quantity.value'] < 0.1).sum() / 12.0
                day_sleep_hrs = (day_df['base_movement_quantity.value'] < 0.1).sum() / 12.0
                overall_sleep_hrs = night_sleep_hrs + day_sleep_hrs

            # --- ECG Features ---
            ecg_feats = {}
            for c in ECG_COLS:
                if c in df.columns and df[c].notna().any():
                    ecg_feats[f'{c}_mean'] = df[c].mean()
                    ecg_feats[f'{c}_std'] = df[c].std()
                else:
                    ecg_feats[f'{c}_mean'] = np.nan
                    ecg_feats[f'{c}_std'] = np.nan
            
            # --- Metadata & MOCA ---
            meta_data = {}
            for var in TARGET_META_VARS:
                meta_data[var] = df[var].iloc[0] if var in df.columns else np.nan
                
            age = float(meta_data.get('meta_age', 65)) if pd.notna(meta_data.get('meta_age')) else 65
            
            p_moca_info = moca_dict.get(p_id, {})
            moca_score = p_moca_info.get('moca_mean', np.nan)
                
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
                'std_glucose': std_glucose,
                'time_above_180_pct': time_above_180_pct,
                'rapid_glucose_changes': rapid_glucose_changes,
                'night_sleep_hrs': night_sleep_hrs,
                'day_sleep_hrs': day_sleep_hrs,
                'overall_sleep_hrs': overall_sleep_hrs,
                'moca_score': moca_score,
                'age_bracket': age_bracket
            }
            base_record.update(meta_data)
            base_record.update(ecg_feats)
            records.append(base_record)
            
        except Exception as e:
            print(f"Error extracting from {f}: {e}")
            continue

    return pd.DataFrame(records)

def plot_moca_age_stratified(df):
    print("Plotting MOCA vs Study Group stratified by Age Bracket...")
    if 'moca_score' not in df.columns or df['moca_score'].isna().all():
        return
        
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='meta_study_group', y='moca_score', hue='age_bracket', palette='Set2')
    plt.title('MOCA Scores by Study Group and Age Bracket')
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "moca_age_stratified", "moca_vs_group_by_age.png"))
    plt.close()
    
    # Optional correlation heatmap separated by age
    for age_b in df['age_bracket'].unique():
        sub_df = df[df['age_bracket'] == age_b]
        cols = ['moca_score', 'mean_glucose', 'std_glucose', 'overall_sleep_hrs', 'ecg_Rate_mean']
        valid_cols = [c for c in cols if c in sub_df.columns and sub_df[c].notna().any()]
        if len(valid_cols) > 1:
            plt.figure(figsize=(8, 6))
            sns.heatmap(sub_df[valid_cols].corr(method='spearman'), annot=True, cmap='coolwarm', fmt=".2f")
            plt.title(f'Correlations for Age Bracket: {age_b}')
            plt.tight_layout()
            plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "moca_age_stratified", f"corr_{age_b}.png"))
            plt.close()

def plot_sleep_analysis(df):
    print("Plotting Sleep Data analysis...")
    sleep_cols = ['night_sleep_hrs', 'day_sleep_hrs', 'overall_sleep_hrs']
    for c in sleep_cols:
        if c not in df.columns or df[c].isna().all(): continue
        
        # Sleep across study group and age
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x='meta_study_group', y=c, hue='age_bracket', palette='Pastel1')
        plt.title(f'{c} Variation by Study Group and Age Bracket')
        plt.xticks(rotation=15)
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "sleep_analysis", f"{c}_by_group_age.png"))
        plt.close()

        # Association with mean glucose
        if 'mean_glucose' in df.columns and df['mean_glucose'].notna().any():
            plt.figure(figsize=(8, 5))
            sns.scatterplot(data=df, x=c, y='mean_glucose', hue='meta_study_group', alpha=0.7)
            sns.regplot(data=df, x=c, y='mean_glucose', scatter=False, color='red')
            plt.title(f'Mean Glucose vs {c}')
            plt.tight_layout()
            plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "sleep_analysis", f"mean_glucose_vs_{c}.png"))
            plt.close()
            
        # Association with sugar spikes (std_glucose)
        if 'std_glucose' in df.columns and df['std_glucose'].notna().any():
            plt.figure(figsize=(8, 5))
            sns.scatterplot(data=df, x=c, y='std_glucose', hue='meta_study_group', alpha=0.7)
            sns.regplot(data=df, x=c, y='std_glucose', scatter=False, color='red')
            plt.title(f'Glucose Variability (Spikes) vs {c}')
            plt.tight_layout()
            plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "sleep_analysis", f"spikes_vs_{c}.png"))
            plt.close()

def plot_ecg_analysis(df):
    print("Plotting ECG Data analysis...")
    for c in ECG_COLS:
        mean_col = f'{c}_mean'
        if mean_col not in df.columns or df[mean_col].isna().all(): continue
        
        # ECG across study groups
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x='meta_study_group', y=mean_col, palette='Set3')
        plt.title(f'{c} (Mean) by Study Group')
        plt.xticks(rotation=15)
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "ecg_analysis", f"{mean_col}_by_group.png"))
        plt.close()
        
        # ECG stratified by age
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x='meta_study_group', y=mean_col, hue='age_bracket', palette='Set3')
        plt.title(f'{c} (Mean) by Study Group, Stratified by Age')
        plt.xticks(rotation=15)
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "ecg_analysis", f"{mean_col}_by_group_and_age.png"))
        plt.close()

if __name__ == "__main__":
    print("Starting Sleep, ECG, and Age-stratified Analysis Pipeline...")
    df = extract_patient_features()
    
    if not df.empty:
        df['meta_study_group'] = df.get('meta_study_group', pd.Series(dtype=str)).fillna('Unknown/Unassigned')
        
        csv_path = os.path.join(OUTPUT_FOLDER, "data", "master_sleep_ecg_features.csv")
        df.to_csv(csv_path, index=False)
        print(f"Data saved to {csv_path}")
        
        plot_moca_age_stratified(df)
        plot_sleep_analysis(df)
        plot_ecg_analysis(df)
        
        print(f"All plots and data saved to {OUTPUT_FOLDER}")
    else:
        print("No patient data was extracted.")
