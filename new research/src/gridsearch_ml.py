import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, make_scorer
from scipy.stats import ttest_rel

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports", "1_baseline_replication")
os.makedirs(REPORTS_DIR, exist_ok=True)

def run_ml_gridsearch():
    df = pd.read_csv(os.path.join(DATA_DIR, "master_cgm_moca_dataset.csv"))
    
    # Map study groups as in original gridsearch
    group_map = {
        'healthy': '1_Controls',
        'pre_diabetes_lifestyle_controlled': '2_Pre-diabetes',
        'oral_medication_and_or_non_insulin_injectable_medication_controlled': '3_Medication-controlled',
        'insulin_dependent': '4_Insulin-dependent'
    }
    df['group'] = df['study_group'].map(group_map)
    
    # We require moca_total, group, and both hba1c and gmi to compare fairly
    df.dropna(subset=['group', 'moca_total', 'hba1c'], inplace=True)
    
    # Impute missing values
    for col in ['age', 'bmi', 'gmi', 'mean_glucose', 'tir']:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())
    for col in ['education_level']:
        df[col] = df[col].fillna(df[col].mode()[0])
        
    df['cognitive_impairment'] = (df['moca_total'] < 26).astype(int)
    
    # Features
    categorical_features = ['group', 'education_level']
    numeric_base_features = ['age', 'bmi', 'hypertension', 'high_cholesterol', 
                             'kidney_disease', 'circulatory_problems', 'neurodegenerative']
    
    metrics = ['hba1c', 'gmi', 'mean_glucose', 'tir']
    
    results_summary = []
    
    # Setup for scikit-learn ML evaluation
    X_base = df[categorical_features + numeric_base_features]
    y = df['cognitive_impairment']
    
    # CV strategy
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    print(f"Total samples for ML: {len(df)}")
    print(f"Positive cases (Cognitive Impairment): {y.sum()}")
    print("-" * 50)
    
    models = {
        'LogisticRegression': (LogisticRegression(max_iter=1000, random_state=42), {
            'classifier__C': [0.1, 1.0, 10.0],
            'classifier__penalty': ['l2']
        }),
        'RandomForest': (RandomForestClassifier(random_state=42), {
            'classifier__n_estimators': [50, 100],
            'classifier__max_depth': [None, 5, 10]
        })
    }
    
    metric_results = {}
    
    for metric in metrics:
        print(f"Evaluating {metric.upper()}...")
        
        # 1. Statistical Significance using statsmodels Logistic Regression
        formula_multi = f"cognitive_impairment ~ C(group, Treatment('1_Controls')) + age + C(education_level) + bmi + {metric} + hypertension + high_cholesterol + kidney_disease + circulatory_problems + neurodegenerative"
        model_sm = smf.glm(formula_multi, data=df, family=sm.families.Binomial()).fit()
        pval = model_sm.pvalues.get(metric, np.nan)
        coef = model_sm.params.get(metric, np.nan)
        
        metric_results[metric] = {
            'stat_sig_pvalue': pval,
            'stat_sig_coef': coef
        }
        
        # 2. ML GridSearch for Accuracy / AUC
        X = df[categorical_features + numeric_base_features + [metric]]
        
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numeric_base_features + [metric]),
                ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_features)
            ])
            
        for model_name, (model, params) in models.items():
            pipe = Pipeline(steps=[('preprocessor', preprocessor),
                                   ('classifier', model)])
            
            grid = GridSearchCV(pipe, param_grid=params, cv=cv, scoring={'accuracy': 'accuracy', 'roc_auc': 'roc_auc'}, refit='roc_auc', n_jobs=-1)
            grid.fit(X, y)
            
            best_auc = grid.cv_results_['mean_test_roc_auc'][grid.best_index_]
            best_acc = grid.cv_results_['mean_test_accuracy'][grid.best_index_]
            
            metric_results[metric][f'{model_name}_auc'] = best_auc
            metric_results[metric][f'{model_name}_acc'] = best_acc
    
    # Generate Output Report
    report = []
    report.append("# Grid Search and Metric Comparison: HbA1c vs CGM Metrics\n")
    
    report.append("## Statistical Significance (Logistic Regression)")
    report.append("Evaluates if the metric is independently associated with cognitive impairment after adjusting for covariates.")
    report.append("| Metric | Coefficient | p-value | Significant (p<0.05)? |")
    report.append("|--------|-------------|---------|------------------------|")
    for m in metrics:
        p = metric_results[m]['stat_sig_pvalue']
        c = metric_results[m]['stat_sig_coef']
        sig = "**Yes** ⭐" if p < 0.05 else "No"
        report.append(f"| {m.upper()} | {c:.4f} | {p:.4f} | {sig} |")
        
    report.append("\n## Machine Learning Accuracy & AUC (5-fold CV)")
    report.append("Evaluates the predictive power of adding the metric to the base model.")
    report.append("| Metric | LogReg Accuracy | LogReg AUC | RandomForest Accuracy | RandomForest AUC |")
    report.append("|--------|-----------------|------------|-----------------------|------------------|")
    
    # Sort metrics by RandomForest AUC for ranking
    ranked_metrics = sorted(metrics, key=lambda m: metric_results[m]['RandomForest_auc'], reverse=True)
    
    for m in ranked_metrics:
        lr_acc = metric_results[m]['LogisticRegression_acc']
        lr_auc = metric_results[m]['LogisticRegression_auc']
        rf_acc = metric_results[m]['RandomForest_acc']
        rf_auc = metric_results[m]['RandomForest_auc']
        report.append(f"| {m.upper()} | {lr_acc:.4f} | {lr_auc:.4f} | {rf_acc:.4f} | {rf_auc:.4f} |")
        
    report.append("\n## Ranking and Conclusion")
    report.append("Ranked by Random Forest AUC (predictive performance):")
    for i, m in enumerate(ranked_metrics):
        report.append(f"{i+1}. {m.upper()} (AUC: {metric_results[m]['RandomForest_auc']:.4f})")
        
    out_file = os.path.join(REPORTS_DIR, "comparison_results.md")
    with open(out_file, "w") as f:
        f.write("\n".join(report))
        
    print(f"Results written to {out_file}")

if __name__ == "__main__":
    run_ml_gridsearch()
