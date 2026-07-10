import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import wfdb
from scipy.signal import find_peaks

sns.set_theme(style="whitegrid")
OUTPUT_FOLDER = os.path.abspath("../eda_ecg_indepth_outputs")
os.makedirs(os.path.join(OUTPUT_FOLDER, "data"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "plots"), exist_ok=True)

print("1. Loading Data...")
parts_df = pd.read_csv('../dataset/participants.tsv', sep='\t')
manifest_df = pd.read_csv('../dataset/cardiac_ecg/manifest.tsv', sep='\t')

# Merge
df = pd.merge(manifest_df, parts_df, on='person_id', how='inner')

print("2. Extracting Raw Signal Features (HRV: SDNN, RMSSD) from WFDB files...")
sdnn_list = []
rmssd_list = []

for idx, row in df.iterrows():
    try:
        sample_file = row['wfdb_hea_filepath']
        sample_path = os.path.join('../dataset', sample_file.lstrip('/'))
        sample_path_base = sample_path.replace('.hea', '')
        
        record = wfdb.rdrecord(sample_path_base)
        sig_names = record.sig_name
        
        if 'II' in sig_names:
            lead_idx = sig_names.index('II')
            sig = record.p_signal[:, lead_idx]
            fs = record.fs
            
            # Remove NaNs
            sig_clean = sig[~np.isnan(sig)]
            if len(sig_clean) == 0:
                raise ValueError("Empty signal")
            
            # R-peak detection
            thresh = np.mean(sig_clean) + 1.5 * np.std(sig_clean)
            peaks, _ = find_peaks(sig_clean, distance=fs*0.5, height=thresh)
            
            if len(peaks) > 1:
                rr_intervals = np.diff(peaks) / fs * 1000 # in ms
                sdnn = np.nanstd(rr_intervals)
                rmssd = np.sqrt(np.nanmean(np.square(np.diff(rr_intervals))))
            else:
                sdnn = np.nan
                rmssd = np.nan
        else:
            sdnn = np.nan
            rmssd = np.nan
    except Exception as e:
        sdnn = np.nan
        rmssd = np.nan
        
    sdnn_list.append(sdnn)
    rmssd_list.append(rmssd)

df['raw_SDNN_ms'] = sdnn_list
df['raw_RMSSD_ms'] = rmssd_list

print("3. Creating Age Brackets...")
def get_age_bracket(age):
    if pd.isna(age): return 'Unknown'
    if age < 40: return '<40'
    elif age <= 55: return '40-55'
    else: return '>55'

df['age_bracket'] = df['age'].apply(get_age_bracket)

# Save data
print("Saving merged dataset...")
df.to_csv(os.path.join(OUTPUT_FOLDER, "data", "master_indepth_ecg_features.csv"), index=False)

print("4. Plotting ECG metrics across study groups and stratifying by age...")
ecg_metrics = ['Rate', 'PR', 'QRSD', 'QT', 'QTc', 'P', 'QRS', 'T', 'raw_SDNN_ms', 'raw_RMSSD_ms']

for metric in ecg_metrics:
    if metric not in df.columns: continue
    
    # Ensure numeric
    df[metric] = pd.to_numeric(df[metric], errors='coerce')
    
    if df[metric].isna().all(): continue
    
    # By Study Group
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='study_group', y=metric, palette='Set2')
    plt.title(f'{metric} by Study Group')
    plt.xticks(rotation=15, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", f"{metric}_by_group.png"))
    plt.close()
    
    # Stratified by Age
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='study_group', y=metric, hue='age_bracket', palette='Set2')
    plt.title(f'{metric} by Study Group, Stratified by Age Bracket')
    plt.xticks(rotation=15, ha='right')
    plt.legend(title='Age Bracket', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", f"{metric}_by_group_and_age.png"))
    plt.close()

print("Indepth ECG analysis complete. Plots and data saved to:", OUTPUT_FOLDER)
