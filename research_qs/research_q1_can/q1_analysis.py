import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr
import statsmodels.api as sm

OUTPUT_DIR = os.path.abspath("./research_q1_can")
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv("./research_cleaned_data/master_research_dataset.csv")

# Ensure required columns are numeric
cols_to_check = ['night_sleep_hrs', 'std_glucose', 'QTc', 'Rate', 'meta_age']
for c in cols_to_check:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors='coerce')

# Drop missing values for this analysis
df_clean = df.dropna(subset=['night_sleep_hrs', 'std_glucose', 'QTc', 'Rate', 'meta_age'])

print(f"Data available for Q1: {len(df_clean)} rows.")

if len(df_clean) > 0:
    # 1. Correlogram (ECG vs CGM & Sleep)
    corr_cols = ['QTc', 'Rate', 'mean_glucose', 'std_glucose', 'night_sleep_hrs', 'overall_sleep_hrs', 'raw_SDNN_ms']
    avail_cols = [c for c in corr_cols if c in df_clean.columns]
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_clean[avail_cols].corr(method='spearman'), annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt=".2f")
    plt.title("Spearman Correlation: Cardiac Autonomic Neuropathy vs Glycemia/Sleep")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "q1_ecg_cgm_sleep_correlogram.png"))
    plt.close()

    # 2. Linear Regression to predict QTc using age, glucose spikes, and sleep
    print("Linear Regression predicting QTc:")
    X = df_clean[['meta_age', 'std_glucose', 'night_sleep_hrs']]
    X = sm.add_constant(X)
    y = df_clean['QTc']
    model = sm.OLS(y, X).fit()
    print(model.summary().tables[1])
    
    # Save regression summary text
    with open(os.path.join(OUTPUT_DIR, "q1_qtc_regression_summary.txt"), "w") as f:
        f.write(str(model.summary()))

    # 3. Partial Regression / Interaction plots
    # We want to see QTc vs std_glucose
    plt.figure(figsize=(8, 6))
    sns.regplot(data=df_clean, x='std_glucose', y='QTc', scatter_kws={'alpha':0.3})
    plt.title("QTc Prolongation vs Glucose Variability (Spikes)")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "q1_qtc_vs_glucose_spikes.png"))
    plt.close()

    # Rate vs std_glucose
    plt.figure(figsize=(8, 6))
    sns.regplot(data=df_clean, x='std_glucose', y='Rate', scatter_kws={'alpha':0.3, 'color':'orange'})
    plt.title("Resting Heart Rate vs Glucose Variability")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "q1_rate_vs_glucose_spikes.png"))
    plt.close()

print("Q1 Analysis Complete.")
