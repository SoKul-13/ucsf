# Goal 3: Dummy Variables, Control Variables & Feature Level T-Tests + SE

> [!NOTE]
> Compares feature distributions between Cognitively Impaired ($\text{MoCA} < 26$) vs Non-Impaired ($\text{MoCA} \ge 26$) cohorts using two-sample Welch's t-tests with Standard Errors ($\text{SE}$), followed by multivariable dummy variable regression models.

## 1. Feature Level Two-Sample Welch's T-Tests & Standard Errors

- **Cognitively Impaired Group (MoCA < 26)**: N = 900
- **Non-Impaired Control Group (MoCA ≥ 26)**: N = 1315

| Feature / Predictor | Impaired Mean (SE) | Non-Impaired Mean (SE) | Mean Diff (Δ) | SE of Diff (SE_Δ) | Welch's t-stat | df | p-value | Sig |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Age (years)** | 62.96 (0.37) | 59.41 (0.30) | +3.54 | 0.48 | +7.36 | 1914.4 | 0.0000 | ⭐ |
| **Body Mass Index (BMI)** | 30.66 (0.26) | 29.70 (0.20) | +0.96 | 0.33 | +2.93 | 1828.7 | 0.0035 | ⭐ |
| **Lab HbA1c (%)** | 6.31 (0.04) | 5.97 (0.03) | +0.34 | 0.05 | +6.78 | 1535.8 | 0.0000 | ⭐ |
| **CGM Mean Glucose (mg/dL)** | 142.90 (1.50) | 131.58 (0.94) | +11.32 | 1.77 | +6.39 | 1572.0 | 0.0000 | ⭐ |
| **Glucose Management Indicator (GMI)** | 6.73 (0.04) | 6.46 (0.02) | +0.27 | 0.04 | +6.39 | 1572.0 | 0.0000 | ⭐ |
| **Time In Range 70-180 mg/dL (%)** | 83.40 (0.81) | 89.26 (0.51) | -5.86 | 0.96 | -6.11 | 1590.8 | 0.0000 | ⭐ |
| **Spike Duration (minutes)** | 247.66 (46.04) | 117.79 (20.91) | +129.86 | 50.57 | +2.57 | 1271.1 | 0.0103 | ⭐ |
| **Spike Glucose Mean (mg/dL)** | 184.89 (1.77) | 172.29 (1.75) | +12.60 | 2.49 | +5.06 | 2126.4 | 0.0000 | ⭐ |
| **Spike Glucose Peak (mg/dL)** | 196.50 (2.01) | 181.21 (1.91) | +15.29 | 2.77 | +5.52 | 2089.1 | 0.0000 | ⭐ |
| **Spikes per Day (count)** | 1.97 (0.06) | 1.57 (0.05) | +0.40 | 0.07 | +5.39 | 1840.3 | 0.0000 | ⭐ |
| **Years of Education** | 15.51 (0.12) | 16.89 (0.09) | -1.38 | 0.15 | -9.10 | 1856.3 | 0.0000 | ⭐ |

---

## 2. Multivariable Regression (Age & Diabetes Dummies + Controls)

- **Regression Sample Size (N)**: 2210
- **Pseudo R-squared**: **0.054**
- **Log-Likelihood**: **-1411.81**

| Dummy / Control Predictor | Coef (β) | Std Error (SE) | Stat | p-value | Odds Ratio (OR) / Impact | 95% CI | Sig |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Constant (Intercept)** | +0.2646 | 0.3612 | +0.73 | 0.4638 | 1.303 | [0.642, 2.645] | NS |
| **Age Dummy (>65 yrs)** | +0.5362 | 0.0940 | +5.70 | 0.0000 | 1.709 | [1.422, 2.055] | ⭐ |
| **Diabetes Status Dummy** | +0.3169 | 0.1020 | +3.11 | 0.0019 | 1.373 | [1.124, 1.677] | ⭐ |
| **BMI** | +0.0068 | 0.0063 | +1.07 | 0.2824 | 1.007 | [0.994, 1.019] | NS |
| **Years of Education** | -0.1104 | 0.0140 | -7.90 | 0.0000 | 0.895 | [0.871, 0.920] | ⭐ |
| **CGM Mean Glucose** | +0.0044 | 0.0013 | +3.38 | 0.0007 | 1.004 | [1.002, 1.007] | ⭐ |

---

### 💡 Key Observations
1. **Age > 65 Dummy**: Age remains the strongest single demographic predictor for cognitive impairment.
2. **Control Variable Stability**: Body mass index (BMI) and glucose metrics show distinct risk profiles when controlling for age and diabetes status.
