import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

OUTPUT_DIR = os.path.abspath("./research_q3_ml_classification")
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv("./research_cleaned_data/master_research_dataset.csv")

# Define features for the ML model (Ambient Wearable Data only)
# Sleep, HRV, CGM
features = [
    'night_sleep_hrs', 'day_sleep_hrs', 'overall_sleep_hrs',
    'raw_SDNN_ms', 'raw_RMSSD_ms',
    'mean_glucose', 'std_glucose', 'time_above_180_pct', 'rapid_glucose_changes'
]

target = 'meta_study_group'

# Drop NaNs
df_clean = df.dropna(subset=features + [target])

print(f"Data available for Q3 ML Classification: {len(df_clean)} rows.")

if len(df_clean) > 0:
    X = df_clean[features]
    y = df_clean[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    print("Training Random Forest Classifier...")
    rf = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42, class_weight='balanced')
    rf.fit(X_train, y_train)
    
    y_pred = rf.predict(X_test)
    
    # 1. Classification Report
    report = classification_report(y_test, y_pred)
    print(report)
    with open(os.path.join(OUTPUT_DIR, "q3_ml_classification_report.txt"), "w") as f:
        f.write("Random Forest Classification Report\n")
        f.write("===================================\n")
        f.write(report)
        
    # 2. Confusion Matrix Plot
    fig, ax = plt.subplots(figsize=(10, 8))
    cm = confusion_matrix(y_test, y_pred, labels=rf.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=rf.classes_)
    disp.plot(cmap='Blues', ax=ax, xticks_rotation=45)
    plt.title("Diabetes Stage Classification Confusion Matrix")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "q3_confusion_matrix.png"))
    plt.close()
    
    # 3. Feature Importance Plot
    importances = rf.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=importances[indices], y=np.array(features)[indices], palette='viridis')
    plt.title("Feature Importance for Diabetes Stage Prediction")
    plt.xlabel("Gini Importance")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "q3_feature_importance.png"))
    plt.close()

print("Q3 ML Analysis Complete.")
