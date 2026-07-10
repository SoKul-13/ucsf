import pandas as pd
import numpy as np
from scipy.stats import kruskal, spearmanr

print("--- SLEEP & GLUCOSE ---")
try:
    df_sleep = pd.read_csv('/Users/guardian/Documents/ucsf/eda_sleep_ecg_age_outputs/data/master_sleep_ecg_features.csv')
    print("Columns:", df_sleep.columns.tolist())
    
    print("\nMean Glucose by Study Group:")
    print(df_sleep.groupby('meta_study_group')['mean_glucose'].mean())
    
    print("\nStd Glucose (Spikes) by Study Group:")
    print(df_sleep.groupby('meta_study_group')['std_glucose'].mean())
    
    print("\nOverall Sleep Hrs by Study Group:")
    print(df_sleep.groupby('meta_study_group')['overall_sleep_hrs'].mean())
    
    print("\nCorrelation: Mean Glucose vs Overall Sleep")
    df_clean = df_sleep.dropna(subset=['mean_glucose', 'overall_sleep_hrs'])
    if len(df_clean) > 0:
        corr, p = spearmanr(df_clean['mean_glucose'], df_clean['overall_sleep_hrs'])
        print(f"Spearman r: {corr:.3f}, p-value: {p:.4f}")
        
    print("\nCorrelation: Glucose Spikes (std_glucose) vs Night Sleep")
    df_clean2 = df_sleep.dropna(subset=['std_glucose', 'night_sleep_hrs'])
    if len(df_clean2) > 0:
        corr, p = spearmanr(df_clean2['std_glucose'], df_clean2['night_sleep_hrs'])
        print(f"Spearman r: {corr:.3f}, p-value: {p:.4f}")
        
    print("\nMoCA Score by Study Group:")
    print(df_sleep.groupby('meta_study_group')['moca_score'].mean())
    
except Exception as e:
    print("Error loading sleep/glucose data:", e)

print("\n--- IN-DEPTH ECG ---")
try:
    df_ecg = pd.read_csv('/Users/guardian/Documents/ucsf/eda_ecg_indepth_outputs/data/master_indepth_ecg_features.csv')
    print("Columns:", df_ecg.columns.tolist())
    
    metrics = ['Rate', 'QTc', 'raw_SDNN_ms', 'raw_RMSSD_ms']
    for m in metrics:
        if m in df_ecg.columns:
            print(f"\n{m} by Study Group:")
            print(df_ecg.groupby('study_group')[m].mean())
            
            # Kruskal-Wallis
            groups = [group[m].dropna() for name, group in df_ecg.groupby('study_group')]
            if len(groups) > 1:
                stat, p = kruskal(*groups)
                print(f"Kruskal-Wallis p-value for {m}: {p:.4e}")
except Exception as e:
    print("Error loading ECG data:", e)
