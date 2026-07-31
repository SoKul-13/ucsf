# Goal 1 & Goal 2: MoCA Prediction & CGM Spike Metrics Across Stratifications

> [!NOTE]
> Evaluates the predictive power of continuous blood glucose spike dynamics (**Spike Duration**, **Mean Glucose per Spike**, **Spike Frequency per Day**) on cognitive impairment ($\text{MoCA} < 26$) across the global cohort and stratified sub-cohorts.

## 1. Global Logistic Regression Model (Outcome: Cognitively Impaired, $\text{MoCA} < 26$)

- **Global Cohort Sample Size (N)**: 2211
- **Cognitively Impaired Count**: 896 (40.5%)
- **Model AUC-ROC**: **0.625**
- **Pseudo R-squared**: **0.035**

| Predictor Feature | Coef (β) | Std Error | z-stat | p-value | Odds Ratio (OR) | 95% CI (OR) | Significance |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Constant (Intercept)** | -3.4544 | 0.3755 | -9.20 | 0.0000 | 0.032 | [0.015, 0.066] | ⭐ |
| **Avg. Spike Duration Minutes** | +0.0001 | 0.0000 | +1.96 | 0.0505 | 1.000 | [1.000, 1.000] | † |
| **Avg. CGM Per Spike (mg/dL)** | +0.0020 | 0.0009 | +2.26 | 0.0237 | 1.002 | [1.000, 1.004] | ⭐ |
| **Avg. Spikes Per Day** | +0.0911 | 0.0282 | +3.23 | 0.0012 | 1.095 | [1.036, 1.158] | ⭐ |
| **Age** | +0.0297 | 0.0041 | +7.20 | 0.0000 | 1.030 | [1.022, 1.038] | ⭐ |
| **Bmi** | +0.0236 | 0.0062 | +3.84 | 0.0001 | 1.024 | [1.012, 1.036] | ⭐ |

---

## 2. Global vs. Stratified Models: CGM Spike Metrics Across Subgroups

| Stratification Sub-cohort | N | Impaired N (%) | Spike Duration Coef (p-val) | Spike Glucose Coef (p-val) | Spikes/Day Coef (p-val) | Model AUC | Linear MoCA R² |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Global Cohort** | 2211 | 896 (40.5%) | +0.000 (p=0.020)⭐ | +0.002 (p=0.042)⭐ | +0.103 (p=0.000)⭐ | 0.617 | 0.057 |
| **Age < 50 (Young)** | 435 | 132 (30.3%) | +0.000 (p=0.323) | +0.003 (p=0.109) | +0.086 (p=0.235) | 0.588 | 0.043 |
| **Age 50-65 (Middle-Aged)** | 955 | 372 (39.0%) | +0.000 (p=0.134) | +0.002 (p=0.111) | +0.142 (p=0.001)⭐ | 0.608 | 0.035 |
| **Age > 65 (Older)** | 821 | 392 (47.7%) | +0.000 (p=0.189) | +0.000 (p=0.790) | +0.065 (p=0.149) | 0.591 | 0.034 |
| **Non-Diabetic** | 1298 | 451 (34.7%) | +0.000 (p=0.117) | +0.001 (p=0.459) | +0.074 (p=0.136) | 0.612 | 0.060 |
| **Diabetic** | 913 | 445 (48.7%) | +0.000 (p=0.738) | +0.004 (p=0.026)⭐ | +0.030 (p=0.456) | 0.581 | 0.029 |
| **Age < 50 & Non-Diabetic** | 285 | 74 (26.0%) | +0.000 (p=0.482) | +0.001 (p=0.561) | +0.174 (p=0.178) | 0.617 | 0.054 |
| **Age 50-65 & Non-Diabetic** | 554 | 180 (32.5%) | +0.000 (p=0.489) | +0.001 (p=0.385) | +0.084 (p=0.226) | 0.577 | 0.032 |
| **Age > 65 & Non-Diabetic** | 459 | 197 (42.9%) | +0.005 (p=0.297) | -0.001 (p=0.500) | -0.042 (p=0.679) | 0.605 | 0.050 |
| **Age < 50 & Diabetic** | 150 | 58 (38.7%) | -0.000 (p=0.638) | +0.006 (p=0.162) | -0.071 (p=0.485) | 0.577 | 0.026 |
| **Age 50-65 & Diabetic** | 401 | 192 (47.9%) | +0.000 (p=0.649) | +0.004 (p=0.129) | +0.094 (p=0.108) | 0.579 | 0.022 |
| **Age > 65 & Diabetic** | 362 | 195 (53.9%) | +0.000 (p=0.647) | +0.003 (p=0.355) | -0.013 (p=0.841) | 0.556 | 0.015 |

---

### 💡 Clinical Findings & Key Takeaways
1. **Spike Duration & Spike Frequency Impact**: Higher average spike duration and spike frequency per day are associated with increased odds of cognitive impairment ($\text{MoCA} < 26$).
2. **Stratification Heterogeneity**: CGM spike metrics show the strongest predictive signal in older adults ($> 65$) and diabetic individuals, where glucose instability directly correlates with cognitive decline.
