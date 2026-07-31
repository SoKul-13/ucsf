# Goal 5: Interaction Term Analysis & 4-Quadrant Stratified Linear Models

> [!NOTE]
> Evaluates the main effects of **Age Indicator** ($\text{Age} > 65$), **Diabetes Status Indicator** ($\text{Diabetic}$), and their interaction term ($\text{Age}_{>65} \times \text{Diabetic}$) on continuous MoCA cognitive scores. Includes side-by-side multivariable linear models for all 4 stratified sub-cohorts.

## 1. Global Interaction Term OLS Linear Model (Outcome: MoCA Total Score)

- **Model Sample Size (N)**: 2210
- **R-squared ($R^2$)**: **0.086** (Adjusted $R^2$: **0.083**)
- **F-statistic**: **34.39** (p-value: **6.7893e-40**)

| Term / Predictor | Coef (β) | Std Error (SE) | t-statistic | p-value | 95% Confidence Interval | Sig |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Constant (Intercept)** | +24.8389 | 0.5126 | +48.45 | 0.0000 | [+23.834, +25.844] | ⭐ |
| **Age Indicator by Itself (Age > 65)** | -0.9607 | 0.1770 | -5.43 | 0.0000 | [-1.308, -0.614] | ⭐ |
| **Diabetes Indicator by Itself (Diabetic)** | -0.5570 | 0.1824 | -3.05 | 0.0023 | [-0.915, -0.199] | ⭐ |
| **Interaction Term (Age > 65 × Diabetic)** | +0.1432 | 0.2721 | +0.53 | 0.5987 | [-0.390, +0.677] | NS |
| **BMI Control** | -0.0013 | 0.0091 | -0.14 | 0.8849 | [-0.019, +0.017] | NS |
| **Years of Education Control** | +0.1611 | 0.0188 | +8.59 | 0.0000 | [+0.124, +0.198] | ⭐ |
| **CGM Mean Glucose Control** | -0.0090 | 0.0018 | -4.86 | 0.0000 | [-0.013, -0.005] | ⭐ |

---

## 2. 4-Quadrant Stratified Linear Regression Models

Stratification Categories:
1. **Above 65 & Diabetes** ($\text{Age} > 65, \text{Diabetic} = 1$)
2. **Lower 65 & Diabetes** ($\text{Age} \le 65, \text{Diabetic} = 1$)
3. **Above 65 & No Diabetes** ($\text{Age} > 65, \text{Diabetic} = 0$)
4. **Lower 65 & No Diabetes** ($\text{Age} \le 65, \text{Diabetic} = 0$)

### 📊 Sub-cohort: Above 65 & Diabetes (N = 362)

- **Model R²**: **0.023** (Adjusted $R^2$: 0.015)
- **F-statistic**: 2.78 (p-value: 0.0409)

| Predictor | Coef (β) | Std Error | t-stat | p-value | 95% CI | Sig |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | +23.0737 | 1.5200 | +15.18 | 0.0000 | [+20.084, +26.063] | ⭐ |
| **BMI** | +0.0145 | 0.0311 | +0.47 | 0.6420 | [-0.047, +0.076] | NS |
| **Years of Education** | +0.1290 | 0.0532 | +2.42 | 0.0158 | [+0.024, +0.234] | ⭐ |
| **CGM Mean Glucose** | -0.0061 | 0.0046 | -1.33 | 0.1852 | [-0.015, +0.003] | NS |

---

### 📊 Sub-cohort: Lower 65 & Diabetes (N = 550)

- **Model R²**: **0.081** (Adjusted $R^2$: 0.076)
- **F-statistic**: 16.05 (p-value: 0.0000)

| Predictor | Coef (β) | Std Error | t-stat | p-value | 95% CI | Sig |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | +21.8781 | 1.0596 | +20.65 | 0.0000 | [+19.797, +23.960] | ⭐ |
| **BMI** | +0.0038 | 0.0173 | +0.22 | 0.8242 | [-0.030, +0.038] | NS |
| **Years of Education** | +0.2563 | 0.0407 | +6.29 | 0.0000 | [+0.176, +0.336] | ⭐ |
| **CGM Mean Glucose** | -0.0042 | 0.0026 | -1.58 | 0.1144 | [-0.009, +0.001] | NS |

---

### 📊 Sub-cohort: Above 65 & No Diabetes (N = 459)

- **Model R²**: **0.080** (Adjusted $R^2$: 0.074)
- **F-statistic**: 13.20 (p-value: 0.0000)

| Predictor | Coef (β) | Std Error | t-stat | p-value | 95% CI | Sig |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | +24.2890 | 1.3216 | +18.38 | 0.0000 | [+21.692, +26.886] | ⭐ |
| **BMI** | -0.0129 | 0.0209 | -0.62 | 0.5386 | [-0.054, +0.028] | NS |
| **Years of Education** | +0.2359 | 0.0432 | +5.47 | 0.0000 | [+0.151, +0.321] | ⭐ |
| **CGM Mean Glucose** | -0.0200 | 0.0073 | -2.75 | 0.0062 | [-0.034, -0.006] | ⭐ |

---

### 📊 Sub-cohort: Lower 65 & No Diabetes (N = 839)

- **Model R²**: **0.050** (Adjusted $R^2$: 0.046)
- **F-statistic**: 14.62 (p-value: 0.0000)

| Predictor | Coef (β) | Std Error | t-stat | p-value | 95% CI | Sig |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | +27.5810 | 0.7860 | +35.09 | 0.0000 | [+26.038, +29.124] | ⭐ |
| **BMI** | -0.0026 | 0.0131 | -0.20 | 0.8404 | [-0.028, +0.023] | NS |
| **Years of Education** | +0.0966 | 0.0259 | +3.73 | 0.0002 | [+0.046, +0.148] | ⭐ |
| **CGM Mean Glucose** | -0.0224 | 0.0042 | -5.37 | 0.0000 | [-0.031, -0.014] | ⭐ |

---

