import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import GroupKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score, average_precision_score, accuracy_score, recall_score, f1_score, brier_score_loss, roc_curve

# Set paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
FIG_DIR = os.path.join(BASE_DIR, "figures")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

def train_and_evaluate_models():
    parquet_path = os.path.join(DATA_DIR, "cgm_sliding_window_features.parquet")
    if not os.path.exists(parquet_path):
        print("Sliding window dataset not found yet. Run 02_extract_sliding_windows.py first.")
        return
        
    print("Loading sliding window features...")
    df = pd.read_parquet(parquet_path)
    print(f"Loaded dataset with {len(df)} total samples across {df['person_id'].nunique()} patients.")
    
    # Feature columns
    feature_cols = [
        'g_current', 'z_current', 'g_lag5', 'g_lag10', 'g_lag15', 'g_lag30', 'g_lag60',
        'vel_15', 'vel_30', 'vel_60', 'acc_15',
        'roll_mean_30', 'roll_std_30', 'roll_min_30', 'roll_max_30',
        'roll_mean_60', 'roll_std_60', 'roll_min_60', 'roll_max_60',
        'hour', 'is_weekend', 'sin_hour', 'cos_hour',
        'patient_mean', 'patient_sd', 'age', 'bmi', 'years_of_education', 'is_diabetic'
    ]
    
    # Clean NaNs
    df_clean = df.dropna(subset=feature_cols).copy()
    
    # Subsample 150,000 balanced samples across patient groups for fast training
    if len(df_clean) > 150000:
        df_sub = df_clean.sample(n=150000, random_state=42).sort_values('time').reset_index(drop=True)
    else:
        df_sub = df_clean
        
    groups = df_sub['person_id'].values
    
    # Target configurations
    target_configs = [
        ("Absolute (>140 mg/dL)", "target_140_15m", 15),
        ("Absolute (>140 mg/dL)", "target_140_30m", 30),
        ("Absolute (>140 mg/dL)", "target_140_60m", 60),
        ("Personalized (>2 SD)", "target_2sd_15m", 15),
        ("Personalized (>2 SD)", "target_2sd_30m", 30),
        ("Personalized (>2 SD)", "target_2sd_60m", 60),
    ]
    
    models_dict = {
        'Logistic Regression': lambda: LogisticRegression(max_iter=500, random_state=42),
        'Random Forest': lambda: RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1),
        'Hist Gradient Boosting': lambda: HistGradientBoostingClassifier(max_iter=100, max_depth=6, learning_rate=0.1, random_state=42)
    }
    
    results = []
    roc_curves_data = []
    
    gkf = GroupKFold(n_splits=5)
    
    for t_label, t_col, horizon in target_configs:
        print(f"\n--- Training Models for Target: {t_label} | Horizon: {horizon} min ---")
        y = df_sub[t_col].values
        pos_rate = float(np.mean(y) * 100.0)
        print(f"Class Balance: Positive Spikes = {pos_rate:.2f}%")
        
        for m_name, m_factory in models_dict.items():
            oof_preds = np.zeros(len(df_sub))
            oof_probs = np.zeros(len(df_sub))
            
            for train_idx, val_idx in gkf.split(df_sub, y, groups):
                X_train, y_train = df_sub.iloc[train_idx][feature_cols], y[train_idx]
                X_val, y_val = df_sub.iloc[val_idx][feature_cols], y[val_idx]
                
                model = m_factory()
                if m_name == 'Logistic Regression':
                    scaler = StandardScaler()
                    X_train_scaled = scaler.fit_transform(X_train)
                    X_val_scaled = scaler.transform(X_val)
                    model.fit(X_train_scaled, y_train)
                    probs = model.predict_proba(X_val_scaled)[:, 1]
                else:
                    model.fit(X_train, y_train)
                    probs = model.predict_proba(X_val)[:, 1]
                    
                oof_probs[val_idx] = probs
                oof_preds[val_idx] = (probs >= 0.5).astype(int)
                
            roc_auc = float(roc_auc_score(y, oof_probs))
            pr_auc = float(average_precision_score(y, oof_probs))
            acc = float(accuracy_score(y, oof_preds))
            rec = float(recall_score(y, oof_preds))
            f1 = float(f1_score(y, oof_preds))
            brier = float(brier_score_loss(y, oof_probs))
            
            tn_mask = (y == 0)
            spec = float(np.sum((oof_preds == 0) & tn_mask) / np.sum(tn_mask)) if np.sum(tn_mask) > 0 else 0.0
            
            results.append({
                'Spike_Definition': t_label,
                'Horizon_Minutes': horizon,
                'Model': m_name,
                'ROC_AUC': roc_auc,
                'PR_AUC': pr_auc,
                'Accuracy': acc,
                'Sensitivity': rec,
                'Specificity': spec,
                'F1_Score': f1,
                'Brier_Score': brier,
                'Positive_Rate_Pct': pos_rate
            })
            
            if horizon == 30 and m_name in ['Hist Gradient Boosting', 'Random Forest']:
                fpr, tpr, _ = roc_curve(y, oof_probs)
                roc_curves_data.append({
                    'Label': f"{t_label} - {m_name} (AUC={roc_auc:.3f})",
                    'fpr': fpr,
                    'tpr': tpr
                })
            print(f"[{m_name}] Horizon={horizon}m | ROC-AUC={roc_auc:.4f} | PR-AUC={pr_auc:.4f} | F1={f1:.4f}")

    df_res = pd.DataFrame(results)
    print("\n" + "="*80)
    print("MODEL EVALUATION SUMMARY Across Spike Definitions and Forecasting Horizons")
    print("="*80)
    print(df_res.to_string(index=False))
    
    df_res.to_csv(os.path.join(DATA_DIR, "model_evaluation_results.csv"), index=False)
    print(f"Saved evaluation metrics to model_evaluation_results.csv")
    
    # ─── VISUALIZATION ──────────────────────────────────────────────────
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    sns.barplot(data=df_res, x='Horizon_Minutes', y='ROC_AUC', hue='Model', ax=axes[0], palette='Blues_d')
    axes[0].set_title('Predictive Performance (ROC-AUC) by Horizon', fontsize=13, fontweight='bold')
    axes[0].set_ylabel('ROC-AUC Score', fontsize=11)
    axes[0].set_ylim(0.70, 1.0)
    
    for rdata in roc_curves_data:
        axes[1].plot(rdata['fpr'], rdata['tpr'], label=rdata['Label'], linewidth=2)
    axes[1].plot([0, 1], [0, 1], 'k--', alpha=0.6, label='Random Chance')
    axes[1].set_title('ROC Curves (30-Minute Spike Forecasting)', fontsize=13, fontweight='bold')
    axes[1].set_xlabel('False Positive Rate', fontsize=11)
    axes[1].set_ylabel('True Positive Rate', fontsize=11)
    axes[1].legend(loc='lower right', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig3_predictive_model_performance.png"), dpi=300)
    plt.close()
    print("Saved figure: fig3_predictive_model_performance.png")

if __name__ == "__main__":
    train_and_evaluate_models()
