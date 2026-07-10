import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

OUTPUT_DIR = os.path.abspath("./research_q2_cognition")
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv("./research_cleaned_data/master_research_dataset.csv")

# Ensure required columns are numeric
glucose_vars = ['mean_glucose', 'std_glucose', 'time_above_180_pct', 'rapid_glucose_changes', 'sleep_deprivation_x_glucose_spike']
target = 'moca_score'

for c in glucose_vars + [target]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors='coerce')

df_clean = df.dropna(subset=glucose_vars + [target])
print(f"Data available for Q2: {len(df_clean)} rows.")

if len(df_clean) > 0:
    # 1. Correlogram (MoCA vs all glucose aggregates)
    plt.figure(figsize=(8, 6))
    sns.heatmap(df_clean[glucose_vars + [target]].corr(method='spearman'), annot=True, cmap='viridis', vmin=-1, vmax=1, fmt=".2f")
    plt.title("Spearman Correlation: Cognition (MoCA) vs Glucose Aggregates")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "q2_moca_glucose_correlogram.png"))
    plt.close()

    # 2. Linear Regression (Predicting MoCA from Glucose Aggregates & Interaction)
    print("Linear Regression predicting MoCA:")
    X = df_clean[glucose_vars]
    X = sm.add_constant(X)
    y = df_clean[target]
    model = sm.OLS(y, X).fit()
    print(model.summary().tables[1])
    
    with open(os.path.join(OUTPUT_DIR, "q2_moca_regression_summary.txt"), "w") as f:
        f.write(str(model.summary()))

    # 3. Individual Scatter/Reg plots for each variation
    for var in glucose_vars:
        plt.figure(figsize=(8, 6))
        sns.regplot(data=df_clean, x=var, y=target, scatter_kws={'alpha':0.3}, line_kws={'color': 'red'})
        plt.title(f"MoCA Score vs {var}")
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_DIR, f"q2_moca_vs_{var}.png"))
        plt.close()
        
    # 4. Boxplot of MoCA by rapid glucose changes quartiles
    df_clean['rapid_changes_quartile'] = pd.qcut(df_clean['rapid_glucose_changes'], q=4, labels=['Q1 (Low)', 'Q2', 'Q3', 'Q4 (High)'], duplicates='drop')
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df_clean, x='rapid_changes_quartile', y=target, palette='Set3')
    plt.title("MoCA Score by Quartiles of Rapid Glucose Changes")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "q2_moca_by_rapid_changes_quartile.png"))
    plt.close()

print("Q2 Analysis Complete.")
