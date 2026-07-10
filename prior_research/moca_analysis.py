import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
import warnings
from itertools import combinations

warnings.filterwarnings('ignore')

# --- CONFIGURATION ---
INPUT_FOLDER = os.path.abspath("../eda_advanced_outputs")
OUTPUT_FOLDER = os.path.abspath("../eda_advanced_outputs")

os.makedirs(os.path.join(OUTPUT_FOLDER, "bootstraps"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "plots", "base"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "plots", "correlations"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "plots", "moca_subscores"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "plots", "longitudinal"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, "summary_tables"), exist_ok=True)

sns.set_theme(style="whitegrid")

def factorial_bootstrap_comparisons(df, target_vars, n_iterations=2000):
    group_map = {
        'healthy': 'Healthy', 
        'insulin_dependent': 'Insulin', 
        'oral_medication_and_or_non_insulin_injectable_medication_controlled': 'Oral', 
        'pre_diabetes_lifestyle_controlled': 'Pre-Diabetes'
    }
    
    non_healthy = [
        'insulin_dependent', 
        'oral_medication_and_or_non_insulin_injectable_medication_controlled', 
        'pre_diabetes_lifestyle_controlled'
    ]
    healthy = ['healthy']
    
    pairs = []
    
    # 1. "everything being against healthy"
    # All combinations of non-healthy groups (sizes 1 to 3) vs Healthy
    for r in range(1, len(non_healthy) + 1):
        for c in combinations(non_healthy, r):
            pairs.append((list(c), healthy))
            
    # 2. "one by one being included with healthy against the rest"
    # For each individual non-healthy group, combine it with Healthy and compare to the rest
    for g in non_healthy:
        subset1 = healthy + [g]
        subset2 = [x for x in non_healthy if x != g]
        pairs.append((subset1, subset2))
        
    # 3. "two by two being included with healthy against the rest (single class)"
    # For each pair of non-healthy groups, combine them with Healthy and compare to the remaining one
    for c in combinations(non_healthy, 2):
        subset1 = healthy + list(c)
        subset2 = [x for x in non_healthy if x not in c]
        pairs.append((subset1, subset2))

    for target_var in target_vars:
        if target_var not in df.columns or df[target_var].isna().all():
            continue
            
        print(f"\n--- Factorial Bootstrapping Mean Differences for {target_var} ---")
        results = []
        for s1, s2 in pairs:
            data1 = df[df['meta_study_group'].isin(s1)][target_var].dropna().values
            data2 = df[df['meta_study_group'].isin(s2)][target_var].dropna().values
            
            if len(data1) < 2 or len(data2) < 2: continue
            
            diffs = []
            for _ in range(n_iterations):
                sample1 = np.random.choice(data1, size=len(data1), replace=True)
                sample2 = np.random.choice(data2, size=len(data2), replace=True)
                diffs.append(np.mean(sample1) - np.mean(sample2))
                
            mean_diff = np.mean(diffs)
            ci_lower = np.percentile(diffs, 2.5)
            ci_upper = np.percentile(diffs, 97.5)
            
            name1 = " + ".join([group_map.get(x, x) for x in s1])
            name2 = " + ".join([group_map.get(x, x) for x in s2])
            
            results.append({
                'Group 1': name1, 'Group 2': name2, 
                'Mean Diff': mean_diff, '2.5% CI': ci_lower, '97.5% CI': ci_upper
            })
            
        if results:
            res_df = pd.DataFrame(results)
            print(res_df.to_string(index=False))
            output_file = os.path.join(OUTPUT_FOLDER, "bootstraps", f"factorial_bootstrap_{target_var}.csv")
            res_df.to_csv(output_file, index=False)

def main():
    print("Loading master patient features...")
    df_path = os.path.join(INPUT_FOLDER, "data", "master_patient_features.csv")
    if not os.path.exists(df_path):
        print(f"Error: {df_path} not found. Please run compiler_eda_advanced.py first.")
        return
        
    df = pd.read_csv(df_path)
    
    longitudinal_path = os.path.join(INPUT_FOLDER, "data", "moca_longitudinal.csv")
    long_df = None
    if os.path.exists(longitudinal_path):
        long_df = pd.read_csv(longitudinal_path)
        long_df['date'] = pd.to_datetime(long_df['date'])
        long_df.sort_values(by=['participant_id', 'date'], inplace=True)

    print("\n" + "="*60)
    print("MOCA EDA & ANALYSIS REPORT")
    print("="*60)
    
    # 1. Descriptive Stats
    print("\nDescriptive MOCA Statistics by Group:")
    stats_df = df.groupby('meta_study_group')['moca_score'].describe().reset_index()
    print(stats_df.to_string())
    stats_df.to_csv(os.path.join(OUTPUT_FOLDER, "summary_tables", "moca_descriptive_stats.csv"), index=False)

    # 2. Factorial Bootstrapping
    target_vars = [
        'moca_score', 'mean_glucose', 'moca_abstraction', 'moca_orientation', 
        'moca_combined_mis_score', 'total_movement', 'night_movement', 
        'day_hr', 'night_mean_hr', 'min_spo2', 'meta_age'
    ]
    factorial_bootstrap_comparisons(df, target_vars)
    
    # 3. Base Plots
    print("\nGenerating Base Plots...")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='age_bracket', y='moca_score', hue='meta_study_group', palette='Set2')
    plt.title('MOCA Scores Stratified by Age and Diabetes Class')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "base", "stratified_cognition.png"))
    plt.close()
    
    corr_vars = ['moca_score', 'moca_abstraction', 'moca_orientation', 'moca_combined_mis_score', 'night_movement', 'night_mean_hr', 'total_movement', 'day_hr', 'mean_glucose']
    avail_vars = [v for v in corr_vars if v in df.columns and df[v].notna().any()]
    if len(avail_vars) > 1:
        plt.figure(figsize=(10, 8))
        sns.heatmap(df[avail_vars].corr(method='spearman'), annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlations: Cognition vs Physical Activity & Sleep')
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "correlations", "correlation_heatmap.png"))
        plt.close()
        
    sub_moca_vars = ['moca_score', 'moca_abstraction', 'moca_orientation', 'moca_combined_mis_score']
    avail_sub_vars = [v for v in sub_moca_vars if v in df.columns and df[v].notna().any()]
    if len(avail_sub_vars) > 1:
        plt.figure(figsize=(6, 5))
        sns.heatmap(df[avail_sub_vars].corr(method='spearman'), annot=True, cmap='viridis', fmt=".2f")
        plt.title('Correlations: MOCA Subcategories')
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "correlations", "moca_subcategories_correlation.png"))
        plt.close()
        
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='meta_study_group', palette='Set3')
    plt.title('Class Balance across Study Groups')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "base", "diabetes_class_balance.png"))
    plt.close()

    # 4. MOCA Subscores EDA (Age / Glucose / Activity / Sleep)
    print("\nGenerating MOCA Subscore EDA plots...")
    sub_moca_vars = ['moca_abstraction', 'moca_orientation', 'moca_combined_mis_score']
    features = ['meta_age', 'mean_glucose', 'total_movement', 'night_movement', 'day_hr', 'night_mean_hr', 'min_spo2']
    
    avail_subs = [v for v in sub_moca_vars if v in df.columns and df[v].notna().any()]
    avail_feats = [v for v in features if v in df.columns and df[v].notna().any()]
    
    if avail_subs and avail_feats:
        corr_matrix = df[avail_subs + avail_feats].corr(method='spearman').loc[avail_subs, avail_feats]
        plt.figure(figsize=(10, 5))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Spearman Correlation: MOCA Subscores vs Key Health Metrics')
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "correlations", "subscores_vs_features_heatmap.png"))
        plt.close()
        
        for sub in avail_subs:
            for feat in ['meta_age', 'mean_glucose', 'total_movement', 'night_movement']:
                if feat in avail_feats:
                    plt.figure(figsize=(7, 5))
                    sns.regplot(data=df, x=feat, y=sub, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
                    plt.title(f'{sub} vs {feat}')
                    plt.tight_layout()
                    plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "moca_subscores", f"{sub}_vs_{feat}.png"))
                    plt.close()

    # 5. Longitudinal / Variance Analysis
    if long_df is not None and not long_df.empty:
        print("\n--- Longitudinal MOCA Analysis ---")
        group_map = df.set_index('participant_id')['meta_study_group'].to_dict()
        long_df['meta_study_group'] = long_df['participant_id'].astype(str).map(group_map).fillna('Unknown/Unassigned')
        
        patient_counts = long_df['participant_id'].value_counts()
        multi_test_patients = patient_counts[patient_counts > 1].index.tolist()
        
        print(f"Total participants with multiple MOCA tests: {len(multi_test_patients)}")
        
        with open(os.path.join(OUTPUT_FOLDER, "summary_tables", "moca_longitudinal_summary.txt"), 'w') as f:
            f.write(f"Total participants with MOCA tests: {df['moca_score'].notna().sum()}\n")
            f.write(f"Total participants with multiple MOCA tests: {len(multi_test_patients)}\n\n")
            
            if len(multi_test_patients) > 0:
                multi_df = long_df[long_df['participant_id'].isin(multi_test_patients)]
                variance_by_group = multi_df.groupby('meta_study_group')['moca_score'].var()
                f.write("Variance in MOCA scores by Study Group (among those with >1 test):\n")
                f.write(variance_by_group.to_string() + "\n")
                
                print("Variance in MOCA scores by Study Group:")
                print(variance_by_group.to_string())

                plt.figure(figsize=(12, 7))
                sns.lineplot(data=multi_df, x='date', y='moca_score', hue='participant_id', 
                             marker='o', palette='tab20', legend=False, alpha=0.7)
                plt.title('Longitudinal MOCA Scores for Patients with Multiple Tests')
                plt.xlabel('Date')
                plt.ylabel('MOCA Total Score')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "longitudinal", "moca_spaghetti_plot.png"))
                plt.close()
                
                var_df = long_df.groupby('participant_id').agg(
                    moca_variance=('moca_score', 'var'),
                    meta_study_group=('meta_study_group', 'first')
                ).reset_index()
                var_df = var_df[var_df['moca_variance'] > 0]
                
                plt.figure(figsize=(10, 6))
                sns.boxplot(data=var_df, x='meta_study_group', y='moca_variance', palette='Pastel1')
                sns.stripplot(data=var_df, x='meta_study_group', y='moca_variance', color=".25", size=5, alpha=0.6)
                plt.title('Distribution of MOCA Variance by Study Group')
                plt.ylabel('Variance in MOCA Score')
                plt.xticks(rotation=15)
                plt.tight_layout()
                plt.savefig(os.path.join(OUTPUT_FOLDER, "plots", "longitudinal", "moca_variance_distribution.png"))
                plt.close()

    print(f"\nAll outputs generated in {OUTPUT_FOLDER}")

if __name__ == "__main__":
    main()
