import pandas as pd
import numpy as np
import os

OUTPUT_DIR = os.path.abspath("../research_cleaned_data")
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Loading Sleep/CGM data...")
sleep_df = pd.read_csv("../eda_sleep_ecg_age_outputs/data/master_sleep_ecg_features.csv")

print("Loading In-depth ECG data...")
ecg_df = pd.read_csv("../eda_ecg_indepth_outputs/data/master_indepth_ecg_features.csv")

# Ensure participant_id formats match. 
# sleep_df has 'participant_id' as strings (e.g. '1001')
# ecg_df has 'person_id' as integers
ecg_df.rename(columns={'person_id': 'participant_id'}, inplace=True)
ecg_df['participant_id'] = ecg_df['participant_id'].astype(str)
sleep_df['participant_id'] = sleep_df['participant_id'].astype(str)

print("Merging datasets...")
# Only keep necessary columns from ecg_df to avoid duplicates
ecg_cols = ['participant_id', 'Rate', 'PR', 'QRSD', 'QT', 'QTc', 'raw_SDNN_ms', 'raw_RMSSD_ms']
df = pd.merge(sleep_df, ecg_df[ecg_cols], on='participant_id', how='inner')

print("Cleaning outliers...")
# The healthy group has a massive outlier in std_glucose (2.8e13). Let's drop unrealistic values.
# Realistically, std_glucose should be < 200 mg/dL.
outliers = df['std_glucose'] > 300
if outliers.sum() > 0:
    print(f"Dropping {outliers.sum()} anomalous std_glucose rows.")
    df.loc[outliers, 'std_glucose'] = np.nan

# Compute Interaction terms
# e.g., Sleep Fragmentation (lower sleep) * Glucose Spikes
# Higher interaction = worse health proxy
if 'night_sleep_hrs' in df.columns and 'std_glucose' in df.columns:
    # Inverse sleep (max sleep - current sleep) * std_glucose
    max_sleep = df['night_sleep_hrs'].max()
    df['sleep_deprivation_x_glucose_spike'] = (max_sleep - df['night_sleep_hrs']) * df['std_glucose']

df.to_csv(os.path.join(OUTPUT_DIR, "master_research_dataset.csv"), index=False)
print("Data preparation complete. Shape:", df.shape)
