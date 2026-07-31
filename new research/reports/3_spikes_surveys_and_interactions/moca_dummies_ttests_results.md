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

## 2. Multivariable Regression (3 Age Partition Dummies + Diabetes + Controls)

- **Regression Sample Size (N)**: 2210
- **Reference Age Baseline Group**: Young Adults (< 50 years)
- **Pseudo R-squared**: **0.057**
- **Log-Likelihood**: **-1407.41**

| Dummy / Control Predictor | Coef (β) | Std Error (SE) | Stat | p-value | Odds Ratio (OR) / Impact | 95% CI | Sig |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Constant (Intercept)** | -0.0542 | 0.3780 | -0.14 | 0.8861 | 0.947 | [0.452, 1.987] | NS |
| **Age Dummy: 50-65 yrs (vs <50)** | +0.3785 | 0.1288 | +2.94 | 0.0033 | 1.460 | [1.134, 1.879] | ⭐ |
| **Age Dummy: >65 yrs (vs <50)** | +0.8072 | 0.1329 | +6.07 | 0.0000 | 2.242 | [1.728, 2.908] | ⭐ |
| **Diabetes Status Dummy** | +0.2972 | 0.1024 | +2.90 | 0.0037 | 1.346 | [1.101, 1.645] | ⭐ |
| **BMI** | +0.0084 | 0.0063 | +1.33 | 0.1836 | 1.008 | [0.996, 1.021] | NS |
| **Years of Education** | -0.1103 | 0.0140 | -7.88 | 0.0000 | 0.896 | [0.871, 0.920] | ⭐ |
| **CGM Mean Glucose** | +0.0044 | 0.0013 | +3.42 | 0.0006 | 1.004 | [1.002, 1.007] | ⭐ |

---

## 3. Detailed Step-by-Step Results Explanation

1. **3 Age Partitions Categorical Gradient**:
   - Compared to the reference baseline group of **Young Adults ($< 50$ yrs)**:
     - **Middle-Aged Adults ($50\text{--}65$ yrs)** exhibit a **$46.0\%$ increase in odds** of cognitive impairment ($\text{OR} = 1.460, z = +2.94, p = 0.0033$) ⭐.
     - **Older Adults ($> 65$ yrs)** exhibit a **$124.2\%$ increase in odds** of cognitive impairment ($\text{OR} = 2.242, z = +6.07, p < 0.0001$) ⭐.
   - **Clinical takeaway**: Cognitive risk escalates non-linearly across age partitions, doubling in odds after age 65.

2. **Diabetes Status Indicator**:
   - Controlling for the 3 age partitions, education, BMI, and glucose levels, having diabetes increases impairment odds by **$34.6\%$** ($\text{OR} = 1.346, z = +2.90, p = 0.0037$) ⭐.

3. **Education Buffer & Glycemic Control**:
   - Each additional year of formal education reduces cognitive impairment odds by **$10.4\%$** ($\text{OR} = 0.896, p < 0.0001$) ⭐.
   - Higher mean glucose elevates impairment odds ($\text{OR} = 1.004 \text{ per mg/dL}, p = 0.0006$) ⭐.
