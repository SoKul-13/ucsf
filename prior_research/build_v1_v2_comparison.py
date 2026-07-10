import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn
import torch.optim as optim

sns.set_theme(style="whitegrid")
BASE_DIR = os.path.abspath("../research_v1_vs_v2")
os.makedirs(BASE_DIR, exist_ok=True)

# Define Subdirectories
Q1_DIR = os.path.join(BASE_DIR, "Q1_CAN_Prediction")
Q2_DIR = os.path.join(BASE_DIR, "Q2_Cognition_Prediction")
Q3_DIR = os.path.join(BASE_DIR, "Q3_Diabetes_Stage_Classification")

for d in [Q1_DIR, Q2_DIR, Q3_DIR]:
    os.makedirs(os.path.join(d, "v1_traditional"), exist_ok=True)
    os.makedirs(os.path.join(d, "v2_deep_learning"), exist_ok=True)

df = pd.read_csv("../research_cleaned_data/master_research_dataset.csv")

# -----------------
# DNN Architectures
# -----------------
class RegressionDNN(nn.Module):
    def __init__(self, input_dim):
        super(RegressionDNN, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )
    def forward(self, x):
        return self.net(x)

class ClassificationDNN(nn.Module):
    def __init__(self, input_dim, num_classes):
        super(ClassificationDNN, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, num_classes)
        )
    def forward(self, x):
        return self.net(x)

def train_regression_dnn(X_train, y_train, X_test, y_test, epochs=300):
    model = RegressionDNN(X_train.shape[1])
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.005)
    
    X_tr = torch.tensor(X_train, dtype=torch.float32)
    y_tr = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)
    X_te = torch.tensor(X_test, dtype=torch.float32)
    
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        out = model(X_tr)
        loss = criterion(out, y_tr)
        loss.backward()
        optimizer.step()
        
    model.eval()
    with torch.no_grad():
        preds = model(X_te).numpy().flatten()
    return preds

def train_classification_dnn(X_train, y_train, X_test, y_test, num_classes, epochs=300):
    model = ClassificationDNN(X_train.shape[1], num_classes)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    X_tr = torch.tensor(X_train, dtype=torch.float32)
    y_tr = torch.tensor(y_train, dtype=torch.long)
    X_te = torch.tensor(X_test, dtype=torch.float32)
    
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        out = model(X_tr)
        loss = criterion(out, y_tr)
        loss.backward()
        optimizer.step()
        
    model.eval()
    with torch.no_grad():
        preds = model(X_te)
        _, predicted_classes = torch.max(preds.data, 1)
    return predicted_classes.numpy()


# --- Q1: CAN (Predicting QTc) ---
print("Running Q1 Comparison...")
features_q1 = ['meta_age', 'std_glucose', 'night_sleep_hrs', 'raw_SDNN_ms']
df_q1 = df.dropna(subset=features_q1 + ['QTc'])
X_q1 = df_q1[features_q1].values
y_q1 = df_q1['QTc'].values

scaler = StandardScaler()
X_q1 = scaler.fit_transform(X_q1)
X_tr, X_te, y_tr, y_te = train_test_split(X_q1, y_q1, test_size=0.2, random_state=42)

# V1: Linear Regression
lr = LinearRegression()
lr.fit(X_tr, y_tr)
preds_v1_q1 = lr.predict(X_te)
rmse_v1_q1 = np.sqrt(mean_squared_error(y_te, preds_v1_q1))

# V2: DNN
preds_v2_q1 = train_regression_dnn(X_tr, y_tr, X_te, y_te)
rmse_v2_q1 = np.sqrt(mean_squared_error(y_te, preds_v2_q1))

plt.figure(figsize=(8, 6))
sns.barplot(x=['V1 (Linear Regression)', 'V2 (Deep Neural Net)'], y=[rmse_v1_q1, rmse_v2_q1], palette='coolwarm')
plt.title("Q1: Predicting QTc (Lower RMSE is Better)")
plt.ylabel("Root Mean Squared Error (RMSE)")
plt.tight_layout()
plt.savefig(os.path.join(Q1_DIR, "Q1_V1_vs_V2_Comparison.png"))
plt.close()

with open(os.path.join(Q1_DIR, "results.txt"), "w") as f:
    f.write(f"V1 Linear Regression RMSE: {rmse_v1_q1:.2f}\n")
    f.write(f"V2 PyTorch DNN RMSE: {rmse_v2_q1:.2f}\n")


# --- Q2: Cognition (Predicting MoCA) ---
print("Running Q2 Comparison...")
features_q2 = ['mean_glucose', 'std_glucose', 'time_above_180_pct', 'rapid_glucose_changes', 'sleep_deprivation_x_glucose_spike', 'overall_sleep_hrs']
df_q2 = df.dropna(subset=features_q2 + ['moca_score'])
X_q2 = df_q2[features_q2].values
y_q2 = df_q2['moca_score'].values

X_q2 = scaler.fit_transform(X_q2)
X_tr, X_te, y_tr, y_te = train_test_split(X_q2, y_q2, test_size=0.2, random_state=42)

# V1: Linear Regression
lr = LinearRegression()
lr.fit(X_tr, y_tr)
preds_v1_q2 = lr.predict(X_te)
rmse_v1_q2 = np.sqrt(mean_squared_error(y_te, preds_v1_q2))

# V2: DNN
preds_v2_q2 = train_regression_dnn(X_tr, y_tr, X_te, y_te)
rmse_v2_q2 = np.sqrt(mean_squared_error(y_te, preds_v2_q2))

plt.figure(figsize=(8, 6))
sns.barplot(x=['V1 (Linear Regression)', 'V2 (Deep Neural Net)'], y=[rmse_v1_q2, rmse_v2_q2], palette='coolwarm')
plt.title("Q2: Predicting MoCA Score (Lower RMSE is Better)")
plt.ylabel("Root Mean Squared Error (RMSE)")
plt.tight_layout()
plt.savefig(os.path.join(Q2_DIR, "Q2_V1_vs_V2_Comparison.png"))
plt.close()

with open(os.path.join(Q2_DIR, "results.txt"), "w") as f:
    f.write(f"V1 Linear Regression RMSE: {rmse_v1_q2:.2f}\n")
    f.write(f"V2 PyTorch DNN RMSE: {rmse_v2_q2:.2f}\n")


# --- Q3: Diabetes Classification ---
print("Running Q3 Comparison...")
features_q3 = ['night_sleep_hrs', 'day_sleep_hrs', 'overall_sleep_hrs', 'raw_SDNN_ms', 'raw_RMSSD_ms', 'mean_glucose', 'std_glucose', 'time_above_180_pct', 'rapid_glucose_changes']
target_q3 = 'meta_study_group'
df_q3 = df.dropna(subset=features_q3 + [target_q3])

class_mapping = {label: idx for idx, label in enumerate(df_q3[target_q3].unique())}
y_q3 = df_q3[target_q3].map(class_mapping).values
X_q3 = df_q3[features_q3].values

X_q3 = scaler.fit_transform(X_q3)
X_tr, X_te, y_tr, y_te = train_test_split(X_q3, y_q3, test_size=0.2, random_state=42, stratify=y_q3)

# V1: Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
rf.fit(X_tr, y_tr)
preds_v1_q3 = rf.predict(X_te)
acc_v1 = accuracy_score(y_te, preds_v1_q3)

# V2: DNN
preds_v2_q3 = train_classification_dnn(X_tr, y_tr, X_te, y_te, num_classes=len(class_mapping), epochs=500)
acc_v2 = accuracy_score(y_te, preds_v2_q3)

plt.figure(figsize=(8, 6))
sns.barplot(x=['V1 (Random Forest)', 'V2 (PyTorch DNN)'], y=[acc_v1, acc_v2], palette='viridis')
plt.title("Q3: Predicting Diabetes Stage (Higher Accuracy is Better)")
plt.ylabel("Accuracy Score")
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig(os.path.join(Q3_DIR, "Q3_V1_vs_V2_Comparison.png"))
plt.close()

with open(os.path.join(Q3_DIR, "results.txt"), "w") as f:
    f.write(f"V1 Random Forest Accuracy: {acc_v1:.2f}\n")
    f.write(f"V2 PyTorch DNN Accuracy: {acc_v2:.2f}\n")

print("Deep Learning V1 vs V2 Comparison Script Complete.")
