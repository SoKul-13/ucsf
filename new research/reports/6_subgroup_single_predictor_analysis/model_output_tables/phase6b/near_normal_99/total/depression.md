# Phase 6b model output tables - Near-normal substitute: >= 99% of readings within 70-180 - Total analysis base - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 454; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **454**, R² = **0.0815**, Adj R² = **0.0607**, F-statistic = **3.93** (p = **3.82e-05**), Residual SE = **4.589** on **443** df, AIC = **2682.7**, BIC = **2728.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4901** | 1.6991 | ±3.3981 | **+4.408** | **1.04e-05** | *** |
| Education: graduate level (vs college) | -0.7258 | 0.4561 | ±0.9122 | -1.591 | 0.1116 |  |
| Education: high school or below (vs college) | +1.4795 | 0.9883 | ±1.9766 | +1.497 | 0.1344 |  |
| Site: UCSD (vs UAB) | -0.3813 | 0.5508 | ±1.1015 | -0.692 | 0.4888 |  |
| Site: UW (vs UAB) | +0.2832 | 0.5811 | ±1.1622 | +0.487 | 0.6260 |  |
| **Age (years)** | **-0.0692** | 0.0199 | ±0.0399 | **-3.474** | **5.12e-04** | *** |
| **BMI (kg/m2)** | **+0.0675** | 0.0335 | ±0.0669 | **+2.017** | **0.0437** | * |
| Hypertension | +0.3715 | 0.5106 | ±1.0212 | +0.728 | 0.4668 |  |
| High cholesterol | +0.7434 | 0.4680 | ±0.9360 | +1.589 | 0.1122 |  |
| Kidney disease | +1.1321 | 0.9230 | ±1.8459 | +1.227 | 0.2200 |  |
| Circulatory disease | +0.7761 | 0.7968 | ±1.5935 | +0.974 | 0.3300 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **454**, R² = **0.0815**, Adj R² = **0.0586**, F-statistic = **3.56** (p = **8.00e-05**), Residual SE = **4.594** on **442** df, AIC = **2684.7**, BIC = **2734.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +7.5527 | 4.3235 | ±8.6469 | +1.747 | 0.0807 | . |
| Education: graduate level (vs college) | -0.7260 | 0.4558 | ±0.9116 | -1.593 | 0.1112 |  |
| Education: high school or below (vs college) | +1.4804 | 0.9890 | ±1.9780 | +1.497 | 0.1344 |  |
| Site: UCSD (vs UAB) | -0.3814 | 0.5529 | ±1.1058 | -0.690 | 0.4903 |  |
| Site: UW (vs UAB) | +0.2829 | 0.5845 | ±1.1689 | +0.484 | 0.6284 |  |
| **Age (years)** | **-0.0692** | 0.0201 | ±0.0402 | **-3.445** | **5.70e-04** | *** |
| **BMI (kg/m2)** | **+0.0675** | 0.0337 | ±0.0674 | **+2.003** | **0.0452** | * |
| Hypertension | +0.3723 | 0.5084 | ±1.0169 | +0.732 | 0.4640 |  |
| High cholesterol | +0.7449 | 0.4852 | ±0.9703 | +1.535 | 0.1247 |  |
| Kidney disease | +1.1312 | 0.9282 | ±1.8564 | +1.219 | 0.2229 |  |
| Circulatory disease | +0.7759 | 0.8003 | ±1.6006 | +0.970 | 0.3323 |  |
| HbA1c (%) | -0.0120 | 0.7614 | ±1.5228 | -0.016 | 0.9874 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **454**, R² = **0.0815**, Adj R² = **0.0587**, F-statistic = **3.57** (p = **7.93e-05**), Residual SE = **4.594** on **442** df, AIC = **2684.7**, BIC = **2734.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.9567** | 3.4248 | ±6.8496 | **+2.323** | **0.0202** | * |
| Education: graduate level (vs college) | -0.7251 | 0.4576 | ±0.9151 | -1.585 | 0.1131 |  |
| Education: high school or below (vs college) | +1.4759 | 0.9878 | ±1.9757 | +1.494 | 0.1351 |  |
| Site: UCSD (vs UAB) | -0.3775 | 0.5550 | ±1.1099 | -0.680 | 0.4964 |  |
| Site: UW (vs UAB) | +0.2878 | 0.5891 | ±1.1782 | +0.489 | 0.6251 |  |
| **Age (years)** | **-0.0693** | 0.0199 | ±0.0398 | **-3.485** | **4.92e-04** | *** |
| **BMI (kg/m2)** | **+0.0677** | 0.0335 | ±0.0670 | **+2.023** | **0.0431** | * |
| Hypertension | +0.3756 | 0.5106 | ±1.0212 | +0.736 | 0.4620 |  |
| High cholesterol | +0.7405 | 0.4699 | ±0.9397 | +1.576 | 0.1150 |  |
| Kidney disease | +1.1362 | 0.9232 | ±1.8465 | +1.231 | 0.2184 |  |
| Circulatory disease | +0.7788 | 0.7966 | ±1.5932 | +0.978 | 0.3282 |  |
| Mean glucose (mg/dL) | -0.0041 | 0.0283 | ±0.0567 | -0.146 | 0.8837 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **454**, R² = **0.0815**, Adj R² = **0.0587**, F-statistic = **3.57** (p = **7.93e-05**), Residual SE = **4.594** on **442** df, AIC = **2684.7**, BIC = **2734.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +8.5300 | 7.1033 | ±14.2066 | +1.201 | 0.2298 |  |
| Education: graduate level (vs college) | -0.7251 | 0.4576 | ±0.9151 | -1.585 | 0.1131 |  |
| Education: high school or below (vs college) | +1.4759 | 0.9878 | ±1.9757 | +1.494 | 0.1351 |  |
| Site: UCSD (vs UAB) | -0.3775 | 0.5550 | ±1.1099 | -0.680 | 0.4964 |  |
| Site: UW (vs UAB) | +0.2878 | 0.5891 | ±1.1782 | +0.489 | 0.6251 |  |
| **Age (years)** | **-0.0693** | 0.0199 | ±0.0398 | **-3.485** | **4.92e-04** | *** |
| **BMI (kg/m2)** | **+0.0677** | 0.0335 | ±0.0670 | **+2.023** | **0.0431** | * |
| Hypertension | +0.3756 | 0.5106 | ±1.0212 | +0.736 | 0.4620 |  |
| High cholesterol | +0.7405 | 0.4699 | ±0.9397 | +1.576 | 0.1150 |  |
| Kidney disease | +1.1362 | 0.9232 | ±1.8465 | +1.231 | 0.2184 |  |
| Circulatory disease | +0.7788 | 0.7966 | ±1.5932 | +0.978 | 0.3282 |  |
| GMI (%) | -0.1732 | 1.1844 | ±2.3688 | -0.146 | 0.8837 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **454**, R² = **0.0815**, Adj R² = **0.0587**, F-statistic = **3.57** (p = **7.91e-05**), Residual SE = **4.594** on **442** df, AIC = **2684.7**, BIC = **2734.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.9343** | 2.9760 | ±5.9519 | **+2.666** | **0.0077** | ** |
| Education: graduate level (vs college) | -0.7277 | 0.4565 | ±0.9131 | -1.594 | 0.1109 |  |
| Education: high school or below (vs college) | +1.4743 | 0.9872 | ±1.9743 | +1.493 | 0.1353 |  |
| Site: UCSD (vs UAB) | -0.3730 | 0.5559 | ±1.1119 | -0.671 | 0.5023 |  |
| Site: UW (vs UAB) | +0.2909 | 0.5916 | ±1.1832 | +0.492 | 0.6229 |  |
| **Age (years)** | **-0.0697** | 0.0198 | ±0.0395 | **-3.527** | **4.20e-04** | *** |
| **BMI (kg/m2)** | **+0.0683** | 0.0337 | ±0.0674 | **+2.025** | **0.0428** | * |
| Hypertension | +0.3762 | 0.5088 | ±1.0176 | +0.739 | 0.4596 |  |
| High cholesterol | +0.7422 | 0.4693 | ±0.9385 | +1.582 | 0.1137 |  |
| Kidney disease | +1.1295 | 0.9266 | ±1.8531 | +1.219 | 0.2228 |  |
| Circulatory disease | +0.7773 | 0.7978 | ±1.5955 | +0.974 | 0.3299 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0039 | 0.0225 | ±0.0450 | -0.172 | 0.8637 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **454**, R² = **0.0850**, Adj R² = **0.0622**, F-statistic = **3.73** (p = **4.09e-05**), Residual SE = **4.585** on **442** df, AIC = **2682.9**, BIC = **2732.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.5084** | 2.2907 | ±4.5814 | **+2.405** | **0.0162** | * |
| Education: graduate level (vs college) | -0.6852 | 0.4569 | ±0.9138 | -1.500 | 0.1337 |  |
| Education: high school or below (vs college) | +1.4681 | 0.9955 | ±1.9910 | +1.475 | 0.1403 |  |
| Site: UCSD (vs UAB) | -0.3460 | 0.5529 | ±1.1058 | -0.626 | 0.5314 |  |
| Site: UW (vs UAB) | +0.3234 | 0.5807 | ±1.1615 | +0.557 | 0.5776 |  |
| **Age (years)** | **-0.0696** | 0.0200 | ±0.0399 | **-3.490** | **4.83e-04** | *** |
| **BMI (kg/m2)** | **+0.0658** | 0.0334 | ±0.0669 | **+1.969** | **0.0490** | * |
| Hypertension | +0.3309 | 0.5052 | ±1.0104 | +0.655 | 0.5125 |  |
| High cholesterol | +0.7810 | 0.4696 | ±0.9393 | +1.663 | 0.0963 | . |
| Kidney disease | +1.0118 | 0.9043 | ±1.8086 | +1.119 | 0.2632 |  |
| Circulatory disease | +0.7444 | 0.7936 | ±1.5872 | +0.938 | 0.3483 |  |
| Glucose SD, pooled (mg/dL) | +0.1205 | 0.0966 | ±0.1931 | +1.248 | 0.2121 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **454**, R² = **0.0843**, Adj R² = **0.0615**, F-statistic = **3.70** (p = **4.71e-05**), Residual SE = **4.587** on **442** df, AIC = **2683.3**, BIC = **2732.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.9376** | 2.1586 | ±4.3171 | **+2.751** | **0.0059** | ** |
| Education: graduate level (vs college) | -0.6867 | 0.4556 | ±0.9111 | -1.507 | 0.1317 |  |
| Education: high school or below (vs college) | +1.4844 | 0.9906 | ±1.9812 | +1.499 | 0.1340 |  |
| Site: UCSD (vs UAB) | -0.3559 | 0.5522 | ±1.1045 | -0.644 | 0.5193 |  |
| Site: UW (vs UAB) | +0.3141 | 0.5798 | ±1.1596 | +0.542 | 0.5880 |  |
| **Age (years)** | **-0.0699** | 0.0200 | ±0.0399 | **-3.501** | **4.63e-04** | *** |
| BMI (kg/m2) | +0.0649 | 0.0334 | ±0.0668 | +1.943 | 0.0520 | . |
| Hypertension | +0.3492 | 0.5082 | ±1.0164 | +0.687 | 0.4920 |  |
| High cholesterol | +0.7737 | 0.4703 | ±0.9405 | +1.645 | 0.0999 | . |
| Kidney disease | +1.0297 | 0.9091 | ±1.8182 | +1.133 | 0.2573 |  |
| Circulatory disease | +0.7660 | 0.7918 | ±1.5836 | +0.967 | 0.3333 |  |
| Avg. daily SD (mg/dL) | +0.1063 | 0.0989 | ±0.1978 | +1.075 | 0.2824 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **454**, R² = **0.0850**, Adj R² = **0.0623**, F-statistic = **3.73** (p = **4.07e-05**), Residual SE = **4.585** on **442** df, AIC = **2682.9**, BIC = **2732.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.5351** | 2.2948 | ±4.5895 | **+2.412** | **0.0159** | * |
| Education: graduate level (vs college) | -0.6830 | 0.4577 | ±0.9155 | -1.492 | 0.1357 |  |
| Education: high school or below (vs college) | +1.4552 | 0.9911 | ±1.9821 | +1.468 | 0.1420 |  |
| Site: UCSD (vs UAB) | -0.3320 | 0.5555 | ±1.1110 | -0.598 | 0.5501 |  |
| Site: UW (vs UAB) | +0.3416 | 0.5852 | ±1.1705 | +0.584 | 0.5594 |  |
| **Age (years)** | **-0.0699** | 0.0199 | ±0.0399 | **-3.505** | **4.57e-04** | *** |
| **BMI (kg/m2)** | **+0.0670** | 0.0333 | ±0.0665 | **+2.015** | **0.0439** | * |
| Hypertension | +0.3499 | 0.5077 | ±1.0154 | +0.689 | 0.4908 |  |
| High cholesterol | +0.7697 | 0.4684 | ±0.9367 | +1.643 | 0.1003 |  |
| Kidney disease | +1.0341 | 0.9076 | ±1.8152 | +1.139 | 0.2545 |  |
| Circulatory disease | +0.7544 | 0.7953 | ±1.5906 | +0.949 | 0.3428 |  |
| CV (%) | +0.1331 | 0.1021 | ±0.2041 | +1.304 | 0.1922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **454**, R² = **0.0854**, Adj R² = **0.0627**, F-statistic = **3.75** (p = **3.78e-05**), Residual SE = **4.584** on **442** df, AIC = **2682.7**, BIC = **2732.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.4561** | 2.1634 | ±4.3267 | **+4.371** | **1.24e-05** | *** |
| Education: graduate level (vs college) | -0.6744 | 0.4586 | ±0.9173 | -1.471 | 0.1414 |  |
| Education: high school or below (vs college) | +1.4497 | 0.9900 | ±1.9799 | +1.464 | 0.1431 |  |
| Site: UCSD (vs UAB) | -0.3422 | 0.5534 | ±1.1068 | -0.618 | 0.5364 |  |
| Site: UW (vs UAB) | +0.3328 | 0.5828 | ±1.1655 | +0.571 | 0.5680 |  |
| **Age (years)** | **-0.0697** | 0.0199 | ±0.0399 | **-3.493** | **4.78e-04** | *** |
| **BMI (kg/m2)** | **+0.0671** | 0.0333 | ±0.0666 | **+2.015** | **0.0440** | * |
| Hypertension | +0.3469 | 0.5074 | ±1.0148 | +0.684 | 0.4943 |  |
| High cholesterol | +0.7750 | 0.4686 | ±0.9372 | +1.654 | 0.0982 | . |
| Kidney disease | +1.0546 | 0.9064 | ±1.8127 | +1.164 | 0.2446 |  |
| Circulatory disease | +0.7627 | 0.7928 | ±1.5856 | +0.962 | 0.3360 |  |
| Mean / SD ratio | -0.2848 | 0.1988 | ±0.3977 | -1.432 | 0.1521 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **454**, R² = **0.0841**, Adj R² = **0.0613**, F-statistic = **3.69** (p = **4.84e-05**), Residual SE = **4.587** on **442** df, AIC = **2683.4**, BIC = **2732.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.9635** | 2.2114 | ±4.4228 | **+4.053** | **5.05e-05** | *** |
| Education: graduate level (vs college) | -0.6823 | 0.4574 | ±0.9148 | -1.492 | 0.1358 |  |
| Education: high school or below (vs college) | +1.4662 | 0.9867 | ±1.9734 | +1.486 | 0.1373 |  |
| Site: UCSD (vs UAB) | -0.3558 | 0.5520 | ±1.1041 | -0.644 | 0.5193 |  |
| Site: UW (vs UAB) | +0.3182 | 0.5812 | ±1.1624 | +0.547 | 0.5841 |  |
| **Age (years)** | **-0.0700** | 0.0200 | ±0.0399 | **-3.506** | **4.55e-04** | *** |
| **BMI (kg/m2)** | **+0.0659** | 0.0334 | ±0.0667 | **+1.974** | **0.0483** | * |
| Hypertension | +0.3646 | 0.5107 | ±1.0215 | +0.714 | 0.4753 |  |
| High cholesterol | +0.7621 | 0.4695 | ±0.9389 | +1.623 | 0.1045 |  |
| Kidney disease | +1.0679 | 0.9135 | ±1.8271 | +1.169 | 0.2424 |  |
| Circulatory disease | +0.7889 | 0.7911 | ±1.5821 | +0.997 | 0.3186 |  |
| Avg. daily mean/SD | -0.1807 | 0.1664 | ±0.3329 | -1.086 | 0.2775 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **454**, R² = **0.0983**, Adj R² = **0.0758**, F-statistic = **4.38** (p = **3.00e-06**), Residual SE = **4.552** on **442** df, AIC = **2676.3**, BIC = **2725.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.3873 | 2.1457 | ±4.2913 | +1.579 | 0.1144 |  |
| Education: graduate level (vs college) | -0.7277 | 0.4562 | ±0.9123 | -1.595 | 0.1107 |  |
| Education: high school or below (vs college) | +1.3113 | 0.9682 | ±1.9364 | +1.354 | 0.1756 |  |
| Site: UCSD (vs UAB) | -0.3392 | 0.5408 | ±1.0817 | -0.627 | 0.5306 |  |
| Site: UW (vs UAB) | +0.4287 | 0.5672 | ±1.1345 | +0.756 | 0.4498 |  |
| **Age (years)** | **-0.0643** | 0.0199 | ±0.0399 | **-3.225** | **0.0013** | ** |
| **BMI (kg/m2)** | **+0.0720** | 0.0322 | ±0.0645 | **+2.234** | **0.0255** | * |
| Hypertension | +0.4147 | 0.5076 | ±1.0151 | +0.817 | 0.4139 |  |
| High cholesterol | +0.7024 | 0.4687 | ±0.9375 | +1.498 | 0.1340 |  |
| Kidney disease | +1.0071 | 0.8942 | ±1.7884 | +1.126 | 0.2601 |  |
| Circulatory disease | +0.8406 | 0.7737 | ±1.5474 | +1.087 | 0.2772 |  |
| **MAG (mg/dL/h)** | **+0.1064** | 0.0382 | ±0.0765 | **+2.783** | **0.0054** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **454**, R² = **0.0867**, Adj R² = **0.0639**, F-statistic = **3.81** (p = **2.96e-05**), Residual SE = **4.581** on **442** df, AIC = **2682.1**, BIC = **2731.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+4.9376** | 2.2795 | ±4.5590 | **+2.166** | **0.0303** | * |
| Education: graduate level (vs college) | -0.6935 | 0.4556 | ±0.9112 | -1.522 | 0.1280 |  |
| Education: high school or below (vs college) | +1.4746 | 0.9799 | ±1.9599 | +1.505 | 0.1324 |  |
| Site: UCSD (vs UAB) | -0.3460 | 0.5504 | ±1.1009 | -0.629 | 0.5296 |  |
| Site: UW (vs UAB) | +0.3289 | 0.5769 | ±1.1539 | +0.570 | 0.5687 |  |
| **Age (years)** | **-0.0699** | 0.0200 | ±0.0400 | **-3.494** | **4.76e-04** | *** |
| **BMI (kg/m2)** | **+0.0712** | 0.0338 | ±0.0677 | **+2.103** | **0.0355** | * |
| Hypertension | +0.3915 | 0.5113 | ±1.0225 | +0.766 | 0.4438 |  |
| High cholesterol | +0.7466 | 0.4689 | ±0.9378 | +1.592 | 0.1113 |  |
| Kidney disease | +1.0516 | 0.8936 | ±1.7872 | +1.177 | 0.2393 |  |
| Circulatory disease | +0.7743 | 0.7889 | ±1.5778 | +0.981 | 0.3264 |  |
| Avg. daily range (mg/dL) | +0.0307 | 0.0196 | ±0.0393 | +1.561 | 0.1186 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **454**, R² = **0.0835**, Adj R² = **0.0607**, F-statistic = **3.66** (p = **5.47e-05**), Residual SE = **4.589** on **442** df, AIC = **2683.7**, BIC = **2733.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.9137** | 1.8080 | ±3.6160 | **+3.824** | **1.31e-04** | *** |
| Education: graduate level (vs college) | -0.7384 | 0.4551 | ±0.9102 | -1.622 | 0.1047 |  |
| Education: high school or below (vs college) | +1.4277 | 1.0106 | ±2.0211 | +1.413 | 0.1577 |  |
| Site: UCSD (vs UAB) | -0.3592 | 0.5520 | ±1.1040 | -0.651 | 0.5152 |  |
| Site: UW (vs UAB) | +0.2747 | 0.5826 | ±1.1652 | +0.472 | 0.6373 |  |
| **Age (years)** | **-0.0688** | 0.0201 | ±0.0402 | **-3.426** | **6.13e-04** | *** |
| **BMI (kg/m2)** | **+0.0671** | 0.0335 | ±0.0670 | **+2.004** | **0.0450** | * |
| Hypertension | +0.3327 | 0.5051 | ±1.0103 | +0.659 | 0.5102 |  |
| High cholesterol | +0.7251 | 0.4709 | ±0.9418 | +1.540 | 0.1236 |  |
| Kidney disease | +1.1302 | 0.9236 | ±1.8472 | +1.224 | 0.2211 |  |
| Circulatory disease | +0.7245 | 0.7991 | ±1.5983 | +0.907 | 0.3646 |  |
| SD of daily means (mg/dL) | +0.1153 | 0.1285 | ±0.2569 | +0.897 | 0.3695 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **454**, R² = **0.0818**, Adj R² = **0.0590**, F-statistic = **3.58** (p = **7.48e-05**), Residual SE = **4.593** on **442** df, AIC = **2684.5**, BIC = **2733.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +37.0349 | 65.3169 | ±130.6337 | +0.567 | 0.5707 |  |
| Education: graduate level (vs college) | -0.7187 | 0.4557 | ±0.9115 | -1.577 | 0.1148 |  |
| Education: high school or below (vs college) | +1.4859 | 0.9872 | ±1.9744 | +1.505 | 0.1323 |  |
| Site: UCSD (vs UAB) | -0.3706 | 0.5517 | ±1.1034 | -0.672 | 0.5018 |  |
| Site: UW (vs UAB) | +0.2927 | 0.5821 | ±1.1643 | +0.503 | 0.6151 |  |
| **Age (years)** | **-0.0690** | 0.0200 | ±0.0399 | **-3.456** | **5.49e-04** | *** |
| **BMI (kg/m2)** | **+0.0681** | 0.0339 | ±0.0678 | **+2.010** | **0.0444** | * |
| Hypertension | +0.3675 | 0.5106 | ±1.0211 | +0.720 | 0.4716 |  |
| High cholesterol | +0.7377 | 0.4697 | ±0.9394 | +1.570 | 0.1163 |  |
| Kidney disease | +1.1086 | 0.9150 | ±1.8301 | +1.211 | 0.2257 |  |
| Circulatory disease | +0.7804 | 0.7975 | ±1.5950 | +0.978 | 0.3278 |  |
| Time in range 70-180, pooled (%) | -0.2972 | 0.6568 | ±1.3135 | -0.452 | 0.6509 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **454**, R² = **0.0824**, Adj R² = **0.0596**, F-statistic = **3.61** (p = **6.70e-05**), Residual SE = **4.592** on **442** df, AIC = **2684.2**, BIC = **2733.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +54.3649 | 67.2073 | ±134.4146 | +0.809 | 0.4186 |  |
| Education: graduate level (vs college) | -0.7116 | 0.4540 | ±0.9079 | -1.567 | 0.1170 |  |
| Education: high school or below (vs college) | +1.4933 | 0.9861 | ±1.9723 | +1.514 | 0.1300 |  |
| Site: UCSD (vs UAB) | -0.3776 | 0.5523 | ±1.1046 | -0.684 | 0.4942 |  |
| Site: UW (vs UAB) | +0.2824 | 0.5809 | ±1.1617 | +0.486 | 0.6269 |  |
| **Age (years)** | **-0.0688** | 0.0199 | ±0.0399 | **-3.451** | **5.58e-04** | *** |
| **BMI (kg/m2)** | **+0.0679** | 0.0336 | ±0.0671 | **+2.022** | **0.0432** | * |
| Hypertension | +0.3817 | 0.5133 | ±1.0265 | +0.744 | 0.4571 |  |
| High cholesterol | +0.7276 | 0.4710 | ±0.9421 | +1.545 | 0.1224 |  |
| Kidney disease | +1.1150 | 0.9118 | ±1.8236 | +1.223 | 0.2214 |  |
| Circulatory disease | +0.7702 | 0.7950 | ±1.5899 | +0.969 | 0.3327 |  |
| Avg. daily time in range 70-180 (%) | -0.4710 | 0.6745 | ±1.3491 | -0.698 | 0.4850 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **454**, R² = **0.0869**, Adj R² = **0.0641**, F-statistic = **3.82** (p = **2.86e-05**), Residual SE = **4.580** on **442** df, AIC = **2682.0**, BIC = **2731.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.7566** | 1.7051 | ±3.4101 | **+4.549** | **5.39e-06** | *** |
| Education: graduate level (vs college) | -0.7387 | 0.4559 | ±0.9117 | -1.621 | 0.1051 |  |
| Education: high school or below (vs college) | +1.4243 | 0.9969 | ±1.9939 | +1.429 | 0.1531 |  |
| Site: UCSD (vs UAB) | -0.5339 | 0.5603 | ±1.1205 | -0.953 | 0.3406 |  |
| Site: UW (vs UAB) | +0.1938 | 0.5835 | ±1.1670 | +0.332 | 0.7397 |  |
| **Age (years)** | **-0.0698** | 0.0199 | ±0.0398 | **-3.511** | **4.46e-04** | *** |
| **BMI (kg/m2)** | **+0.0677** | 0.0335 | ±0.0671 | **+2.020** | **0.0434** | * |
| Hypertension | +0.4223 | 0.5110 | ±1.0221 | +0.826 | 0.4086 |  |
| High cholesterol | +0.7468 | 0.4667 | ±0.9334 | +1.600 | 0.1095 |  |
| Kidney disease | +1.0255 | 0.9211 | ±1.8423 | +1.113 | 0.2656 |  |
| Circulatory disease | +0.8039 | 0.7992 | ±1.5984 | +1.006 | 0.3145 |  |
| Any reading < 54 during wear (0/1) | -0.9512 | 0.5628 | ±1.1257 | -1.690 | 0.0910 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **454**, R² = **0.0884**, Adj R² = **0.0657**, F-statistic = **3.90** (p = **2.13e-05**), Residual SE = **4.577** on **442** df, AIC = **2681.3**, BIC = **2730.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.7123** | 1.7243 | ±3.4487 | **+4.473** | **7.73e-06** | *** |
| Education: graduate level (vs college) | -0.7350 | 0.4548 | ±0.9096 | -1.616 | 0.1061 |  |
| Education: high school or below (vs college) | +1.3744 | 0.9905 | ±1.9810 | +1.388 | 0.1653 |  |
| Site: UCSD (vs UAB) | -0.5175 | 0.5558 | ±1.1117 | -0.931 | 0.3518 |  |
| Site: UW (vs UAB) | +0.2169 | 0.5809 | ±1.1618 | +0.373 | 0.7089 |  |
| **Age (years)** | **-0.0718** | 0.0200 | ±0.0400 | **-3.590** | **3.31e-04** | *** |
| **BMI (kg/m2)** | **+0.0720** | 0.0341 | ±0.0682 | **+2.112** | **0.0347** | * |
| Hypertension | +0.4520 | 0.5131 | ±1.0262 | +0.881 | 0.3784 |  |
| High cholesterol | +0.7180 | 0.4658 | ±0.9317 | +1.541 | 0.1233 |  |
| Kidney disease | +1.0444 | 0.9197 | ±1.8394 | +1.136 | 0.2561 |  |
| Circulatory disease | +0.8365 | 0.8051 | ±1.6101 | +1.039 | 0.2988 |  |
| **Time < 54 (%)** | **-7.5735** | 3.5157 | ±7.0313 | **-2.154** | **0.0312** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **454**, R² = **0.0850**, Adj R² = **0.0623**, F-statistic = **3.74** (p = **4.05e-05**), Residual SE = **4.585** on **442** df, AIC = **2682.9**, BIC = **2732.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.5551** | 1.7060 | ±3.4120 | **+4.429** | **9.49e-06** | *** |
| Education: graduate level (vs college) | -0.7310 | 0.4555 | ±0.9111 | -1.605 | 0.1086 |  |
| Education: high school or below (vs college) | +1.4413 | 0.9876 | ±1.9752 | +1.459 | 0.1445 |  |
| Site: UCSD (vs UAB) | -0.4231 | 0.5496 | ±1.0992 | -0.770 | 0.4414 |  |
| Site: UW (vs UAB) | +0.2763 | 0.5817 | ±1.1633 | +0.475 | 0.6347 |  |
| **Age (years)** | **-0.0697** | 0.0199 | ±0.0398 | **-3.502** | **4.62e-04** | *** |
| **BMI (kg/m2)** | **+0.0689** | 0.0336 | ±0.0673 | **+2.049** | **0.0405** | * |
| Hypertension | +0.3889 | 0.5112 | ±1.0223 | +0.761 | 0.4468 |  |
| High cholesterol | +0.7438 | 0.4675 | ±0.9351 | +1.591 | 0.1116 |  |
| Kidney disease | +1.0852 | 0.9222 | ±1.8443 | +1.177 | 0.2393 |  |
| Circulatory disease | +0.8464 | 0.8101 | ±1.6202 | +1.045 | 0.2961 |  |
| Avg. daily time < 54 (%) | -7.1025 | 5.5763 | ±11.1527 | -1.274 | 0.2028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **454**, R² = **0.0827**, Adj R² = **0.0599**, F-statistic = **3.62** (p = **6.33e-05**), Residual SE = **4.591** on **442** df, AIC = **2684.1**, BIC = **2733.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3345** | 1.7220 | ±3.4440 | **+4.259** | **2.05e-05** | *** |
| Education: graduate level (vs college) | -0.7111 | 0.4570 | ±0.9139 | -1.556 | 0.1197 |  |
| Education: high school or below (vs college) | +1.4440 | 0.9860 | ±1.9719 | +1.465 | 0.1430 |  |
| Site: UCSD (vs UAB) | -0.3591 | 0.5529 | ±1.1057 | -0.649 | 0.5160 |  |
| Site: UW (vs UAB) | +0.3146 | 0.5857 | ±1.1714 | +0.537 | 0.5912 |  |
| **Age (years)** | **-0.0692** | 0.0200 | ±0.0399 | **-3.465** | **5.31e-04** | *** |
| **BMI (kg/m2)** | **+0.0676** | 0.0333 | ±0.0665 | **+2.033** | **0.0420** | * |
| Hypertension | +0.3943 | 0.5113 | ±1.0226 | +0.771 | 0.4406 |  |
| High cholesterol | +0.7085 | 0.4720 | ±0.9440 | +1.501 | 0.1333 |  |
| Kidney disease | +1.1767 | 0.9230 | ±1.8461 | +1.275 | 0.2024 |  |
| Circulatory disease | +0.7881 | 0.7963 | ±1.5926 | +0.990 | 0.3223 |  |
| Time 54-69, pooled (%) | +0.9260 | 1.2035 | ±2.4069 | +0.769 | 0.4416 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **454**, R² = **0.0823**, Adj R² = **0.0595**, F-statistic = **3.60** (p = **6.82e-05**), Residual SE = **4.592** on **442** df, AIC = **2684.3**, BIC = **2733.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3929** | 1.7129 | ±3.4257 | **+4.316** | **1.59e-05** | *** |
| Education: graduate level (vs college) | -0.7065 | 0.4560 | ±0.9121 | -1.549 | 0.1213 |  |
| Education: high school or below (vs college) | +1.4510 | 0.9878 | ±1.9756 | +1.469 | 0.1418 |  |
| Site: UCSD (vs UAB) | -0.3749 | 0.5524 | ±1.1048 | -0.679 | 0.4973 |  |
| Site: UW (vs UAB) | +0.2955 | 0.5835 | ±1.1670 | +0.506 | 0.6125 |  |
| **Age (years)** | **-0.0695** | 0.0199 | ±0.0398 | **-3.487** | **4.89e-04** | *** |
| **BMI (kg/m2)** | **+0.0675** | 0.0333 | ±0.0667 | **+2.026** | **0.0427** | * |
| Hypertension | +0.4085 | 0.5146 | ±1.0293 | +0.794 | 0.4274 |  |
| High cholesterol | +0.7181 | 0.4727 | ±0.9455 | +1.519 | 0.1287 |  |
| Kidney disease | +1.1659 | 0.9220 | ±1.8440 | +1.265 | 0.2060 |  |
| Circulatory disease | +0.7731 | 0.7974 | ±1.5948 | +0.970 | 0.3323 |  |
| Avg. daily time 54-69 (%) | +0.7791 | 1.2581 | ±2.5161 | +0.619 | 0.5357 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **454**, R² = **0.0816**, Adj R² = **0.0587**, F-statistic = **3.57** (p = **7.85e-05**), Residual SE = **4.594** on **442** df, AIC = **2684.6**, BIC = **2734.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4447** | 1.7284 | ±3.4567 | **+4.307** | **1.65e-05** | *** |
| Education: graduate level (vs college) | -0.7219 | 0.4577 | ±0.9154 | -1.577 | 0.1148 |  |
| Education: high school or below (vs college) | +1.4739 | 0.9896 | ±1.9793 | +1.489 | 0.1364 |  |
| Site: UCSD (vs UAB) | -0.3716 | 0.5533 | ±1.1067 | -0.672 | 0.5019 |  |
| Site: UW (vs UAB) | +0.2930 | 0.5868 | ±1.1735 | +0.499 | 0.6175 |  |
| **Age (years)** | **-0.0691** | 0.0200 | ±0.0400 | **-3.456** | **5.48e-04** | *** |
| **BMI (kg/m2)** | **+0.0674** | 0.0334 | ±0.0668 | **+2.016** | **0.0438** | * |
| Hypertension | +0.3747 | 0.5116 | ±1.0231 | +0.733 | 0.4638 |  |
| High cholesterol | +0.7355 | 0.4715 | ±0.9431 | +1.560 | 0.1188 |  |
| Kidney disease | +1.1458 | 0.9271 | ±1.8542 | +1.236 | 0.2165 |  |
| Circulatory disease | +0.7773 | 0.7975 | ±1.5951 | +0.975 | 0.3298 |  |
| Time < 70 (%) | +0.2302 | 1.0556 | ±2.1112 | +0.218 | 0.8274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **454**, R² = **0.0817**, Adj R² = **0.0588**, F-statistic = **3.57** (p = **7.70e-05**), Residual SE = **4.593** on **442** df, AIC = **2684.6**, BIC = **2734.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4439** | 1.7150 | ±3.4299 | **+4.341** | **1.42e-05** | *** |
| Education: graduate level (vs college) | -0.7170 | 0.4572 | ±0.9143 | -1.568 | 0.1168 |  |
| Education: high school or below (vs college) | +1.4687 | 0.9898 | ±1.9797 | +1.484 | 0.1379 |  |
| Site: UCSD (vs UAB) | -0.3764 | 0.5519 | ±1.1038 | -0.682 | 0.4952 |  |
| Site: UW (vs UAB) | +0.2890 | 0.5840 | ±1.1679 | +0.495 | 0.6207 |  |
| **Age (years)** | **-0.0693** | 0.0199 | ±0.0399 | **-3.475** | **5.11e-04** | *** |
| **BMI (kg/m2)** | **+0.0674** | 0.0334 | ±0.0669 | **+2.017** | **0.0437** | * |
| Hypertension | +0.3871 | 0.5143 | ±1.0286 | +0.753 | 0.4517 |  |
| High cholesterol | +0.7322 | 0.4731 | ±0.9462 | +1.548 | 0.1217 |  |
| Kidney disease | +1.1493 | 0.9257 | ±1.8513 | +1.242 | 0.2144 |  |
| Circulatory disease | +0.7714 | 0.7985 | ±1.5969 | +0.966 | 0.3340 |  |
| Avg. daily time < 70 (%) | +0.3454 | 1.1415 | ±2.2831 | +0.303 | 0.7622 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **454**, R² = **0.0883**, Adj R² = **0.0656**, F-statistic = **3.89** (p = **2.17e-05**), Residual SE = **4.577** on **442** df, AIC = **2681.3**, BIC = **2730.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-726.0633** | 338.4206 | ±676.8412 | **-2.145** | **0.0319** | * |
| Education: graduate level (vs college) | -0.7342 | 0.4548 | ±0.9095 | -1.614 | 0.1064 |  |
| Education: high school or below (vs college) | +1.3738 | 0.9906 | ±1.9813 | +1.387 | 0.1655 |  |
| Site: UCSD (vs UAB) | -0.5227 | 0.5567 | ±1.1134 | -0.939 | 0.3478 |  |
| Site: UW (vs UAB) | +0.2117 | 0.5813 | ±1.1626 | +0.364 | 0.7157 |  |
| **Age (years)** | **-0.0722** | 0.0200 | ±0.0401 | **-3.602** | **3.16e-04** | *** |
| **BMI (kg/m2)** | **+0.0714** | 0.0340 | ±0.0679 | **+2.103** | **0.0355** | * |
| Hypertension | +0.4454 | 0.5122 | ±1.0245 | +0.870 | 0.3845 |  |
| High cholesterol | +0.7209 | 0.4658 | ±0.9316 | +1.548 | 0.1217 |  |
| Kidney disease | +1.0474 | 0.9194 | ±1.8388 | +1.139 | 0.2546 |  |
| Circulatory disease | +0.8347 | 0.8048 | ±1.6096 | +1.037 | 0.2997 |  |
| **Time 54-250, pooled (%)** | **+7.3382** | 3.3866 | ±6.7732 | **+2.167** | **0.0302** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **454**, R² = **0.0851**, Adj R² = **0.0624**, F-statistic = **3.74** (p = **4.00e-05**), Residual SE = **4.585** on **442** df, AIC = **2682.9**, BIC = **2732.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -694.7327 | 531.1671 | ±1062.3343 | -1.308 | 0.1909 |  |
| Education: graduate level (vs college) | -0.7304 | 0.4554 | ±0.9107 | -1.604 | 0.1087 |  |
| Education: high school or below (vs college) | +1.4377 | 0.9878 | ±1.9756 | +1.455 | 0.1455 |  |
| Site: UCSD (vs UAB) | -0.4325 | 0.5501 | ±1.1002 | -0.786 | 0.4317 |  |
| Site: UW (vs UAB) | +0.2689 | 0.5816 | ±1.1633 | +0.462 | 0.6439 |  |
| **Age (years)** | **-0.0701** | 0.0199 | ±0.0399 | **-3.519** | **4.34e-04** | *** |
| **BMI (kg/m2)** | **+0.0685** | 0.0336 | ±0.0671 | **+2.039** | **0.0414** | * |
| Hypertension | +0.3844 | 0.5107 | ±1.0214 | +0.753 | 0.4516 |  |
| High cholesterol | +0.7462 | 0.4676 | ±0.9352 | +1.596 | 0.1106 |  |
| Kidney disease | +1.0860 | 0.9218 | ±1.8436 | +1.178 | 0.2387 |  |
| Circulatory disease | +0.8456 | 0.8098 | ±1.6197 | +1.044 | 0.2964 |  |
| Avg. daily time 54-250 (%) | +7.0234 | 5.3137 | ±10.6273 | +1.322 | 0.1862 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **454**, R² = **0.0817**, Adj R² = **0.0588**, F-statistic = **3.57** (p = **7.74e-05**), Residual SE = **4.593** on **442** df, AIC = **2684.6**, BIC = **2734.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4044** | 1.7201 | ±3.4402 | **+4.305** | **1.67e-05** | *** |
| Education: graduate level (vs college) | -0.7242 | 0.4566 | ±0.9132 | -1.586 | 0.1127 |  |
| Education: high school or below (vs college) | +1.4898 | 0.9881 | ±1.9763 | +1.508 | 0.1316 |  |
| Site: UCSD (vs UAB) | -0.3829 | 0.5524 | ±1.1049 | -0.693 | 0.4882 |  |
| Site: UW (vs UAB) | +0.2805 | 0.5826 | ±1.1652 | +0.482 | 0.6301 |  |
| **Age (years)** | **-0.0692** | 0.0200 | ±0.0399 | **-3.466** | **5.29e-04** | *** |
| **BMI (kg/m2)** | **+0.0680** | 0.0339 | ±0.0678 | **+2.008** | **0.0447** | * |
| Hypertension | +0.3652 | 0.5090 | ±1.0181 | +0.717 | 0.4731 |  |
| High cholesterol | +0.7469 | 0.4691 | ±0.9382 | +1.592 | 0.1113 |  |
| Kidney disease | +1.1005 | 0.9202 | ±1.8404 | +1.196 | 0.2317 |  |
| Circulatory disease | +0.7782 | 0.7984 | ±1.5967 | +0.975 | 0.3297 |  |
| Time 181-250, pooled (%) | +0.2273 | 0.7351 | ±1.4703 | +0.309 | 0.7572 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **454**, R² = **0.0821**, Adj R² = **0.0592**, F-statistic = **3.59** (p = **7.15e-05**), Residual SE = **4.592** on **442** df, AIC = **2684.4**, BIC = **2733.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3517** | 1.7054 | ±3.4109 | **+4.311** | **1.63e-05** | *** |
| Education: graduate level (vs college) | -0.7238 | 0.4564 | ±0.9129 | -1.586 | 0.1128 |  |
| Education: high school or below (vs college) | +1.5043 | 0.9882 | ±1.9763 | +1.522 | 0.1279 |  |
| Site: UCSD (vs UAB) | -0.3844 | 0.5524 | ±1.1047 | -0.696 | 0.4865 |  |
| Site: UW (vs UAB) | +0.2751 | 0.5823 | ±1.1647 | +0.472 | 0.6367 |  |
| **Age (years)** | **-0.0688** | 0.0199 | ±0.0398 | **-3.457** | **5.46e-04** | *** |
| **BMI (kg/m2)** | **+0.0679** | 0.0337 | ±0.0673 | **+2.015** | **0.0439** | * |
| Hypertension | +0.3616 | 0.5081 | ±1.0163 | +0.712 | 0.4767 |  |
| High cholesterol | +0.7431 | 0.4693 | ±0.9386 | +1.584 | 0.1133 |  |
| Kidney disease | +1.0964 | 0.9153 | ±1.8306 | +1.198 | 0.2310 |  |
| Circulatory disease | +0.7766 | 0.7970 | ±1.5941 | +0.974 | 0.3299 |  |
| Avg. daily time 181-250 (%) | +0.4139 | 0.7510 | ±1.5019 | +0.551 | 0.5816 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **454**, R² = **0.0816**, Adj R² = **0.0588**, F-statistic = **3.57** (p = **7.75e-05**), Residual SE = **4.593** on **442** df, AIC = **2684.6**, BIC = **2734.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4047** | 1.7212 | ±3.4425 | **+4.302** | **1.69e-05** | *** |
| Education: graduate level (vs college) | -0.7243 | 0.4566 | ±0.9132 | -1.586 | 0.1127 |  |
| Education: high school or below (vs college) | +1.4897 | 0.9881 | ±1.9762 | +1.508 | 0.1316 |  |
| Site: UCSD (vs UAB) | -0.3826 | 0.5524 | ±1.1047 | -0.693 | 0.4885 |  |
| Site: UW (vs UAB) | +0.2808 | 0.5825 | ±1.1650 | +0.482 | 0.6298 |  |
| **Age (years)** | **-0.0692** | 0.0200 | ±0.0399 | **-3.465** | **5.29e-04** | *** |
| **BMI (kg/m2)** | **+0.0680** | 0.0339 | ±0.0678 | **+2.008** | **0.0447** | * |
| Hypertension | +0.3654 | 0.5091 | ±1.0181 | +0.718 | 0.4728 |  |
| High cholesterol | +0.7468 | 0.4691 | ±0.9382 | +1.592 | 0.1114 |  |
| Kidney disease | +1.1012 | 0.9203 | ±1.8406 | +1.197 | 0.2315 |  |
| Circulatory disease | +0.7782 | 0.7984 | ±1.5967 | +0.975 | 0.3297 |  |
| Time > 180 (%) | +0.2223 | 0.7328 | ±1.4656 | +0.303 | 0.7616 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **454**, R² = **0.0821**, Adj R² = **0.0592**, F-statistic = **3.59** (p = **7.17e-05**), Residual SE = **4.592** on **442** df, AIC = **2684.4**, BIC = **2733.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3509** | 1.7066 | ±3.4132 | **+4.307** | **1.65e-05** | *** |
| Education: graduate level (vs college) | -0.7238 | 0.4564 | ±0.9129 | -1.586 | 0.1128 |  |
| Education: high school or below (vs college) | +1.5041 | 0.9881 | ±1.9763 | +1.522 | 0.1280 |  |
| Site: UCSD (vs UAB) | -0.3838 | 0.5523 | ±1.1046 | -0.695 | 0.4871 |  |
| Site: UW (vs UAB) | +0.2757 | 0.5823 | ±1.1646 | +0.473 | 0.6359 |  |
| **Age (years)** | **-0.0688** | 0.0199 | ±0.0398 | **-3.456** | **5.48e-04** | *** |
| **BMI (kg/m2)** | **+0.0679** | 0.0337 | ±0.0673 | **+2.016** | **0.0438** | * |
| Hypertension | +0.3620 | 0.5082 | ±1.0164 | +0.712 | 0.4762 |  |
| High cholesterol | +0.7430 | 0.4693 | ±0.9386 | +1.583 | 0.1134 |  |
| Kidney disease | +1.0970 | 0.9154 | ±1.8308 | +1.198 | 0.2308 |  |
| Circulatory disease | +0.7766 | 0.7970 | ±1.5941 | +0.974 | 0.3299 |  |
| Avg. daily time > 180 (%) | +0.4073 | 0.7474 | ±1.4948 | +0.545 | 0.5858 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **454**, R² = **0.0999**, Adj R² = **0.0775**, F-statistic = **4.46** (p = **2.15e-06**), Residual SE = **4.548** on **442** df, AIC = **2675.5**, BIC = **2724.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.9564** | 1.6840 | ±3.3680 | **+4.131** | **3.61e-05** | *** |
| Education: graduate level (vs college) | -0.6454 | 0.4504 | ±0.9008 | -1.433 | 0.1519 |  |
| Education: high school or below (vs college) | +1.5083 | 1.0000 | ±1.9999 | +1.508 | 0.1315 |  |
| Site: UCSD (vs UAB) | -0.3864 | 0.5495 | ±1.0990 | -0.703 | 0.4820 |  |
| Site: UW (vs UAB) | +0.2202 | 0.5807 | ±1.1615 | +0.379 | 0.7045 |  |
| **Age (years)** | **-0.0597** | 0.0195 | ±0.0390 | **-3.064** | **0.0022** | ** |
| BMI (kg/m2) | +0.0607 | 0.0340 | ±0.0679 | +1.788 | 0.0738 | . |
| Hypertension | +0.2479 | 0.5000 | ±1.0001 | +0.496 | 0.6201 |  |
| High cholesterol | +0.6973 | 0.4647 | ±0.9294 | +1.501 | 0.1335 |  |
| Kidney disease | +1.0565 | 0.9185 | ±1.8369 | +1.150 | 0.2500 |  |
| Circulatory disease | +0.8756 | 0.7822 | ±1.5645 | +1.119 | 0.2630 |  |
| **Nocturnal time > 180 (%)** | **+1.8489** | 0.7902 | ±1.5804 | **+2.340** | **0.0193** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 454; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0727**, LLR χ² = **31.17** (p = **5.49e-04**), AUC = **0.6723**, AIC = **419.7**, BIC = **465.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6675 | 0.9584 | ±1.9167 | -0.696 | 0.4861 | 0.5130 |  |
| Education: graduate level (vs college) | -0.3484 | 0.2760 | ±0.5519 | -1.263 | 0.2068 | 0.7058 |  |
| Education: high school or below (vs college) | +0.3263 | 0.4186 | ±0.8373 | +0.779 | 0.4357 | 1.3858 |  |
| Site: UCSD (vs UAB) | -0.0232 | 0.3406 | ±0.6813 | -0.068 | 0.9457 | 0.9771 |  |
| Site: UW (vs UAB) | +0.3928 | 0.3257 | ±0.6515 | +1.206 | 0.2279 | 1.4811 |  |
| **Age (years)** | **-0.0408** | 0.0128 | ±0.0257 | **-3.183** | **0.0015** | 0.9600 | ** |
| **BMI (kg/m2)** | **+0.0367** | 0.0167 | ±0.0335 | **+2.196** | **0.0281** | 1.0374 | * |
| Hypertension | +0.1940 | 0.2818 | ±0.5637 | +0.688 | 0.4912 | 1.2141 |  |
| High cholesterol | +0.4526 | 0.2693 | ±0.5386 | +1.681 | 0.0928 | 1.5724 | . |
| Kidney disease | +0.5026 | 0.5155 | ±1.0310 | +0.975 | 0.3296 | 1.6529 |  |
| Circulatory disease | +0.5851 | 0.3833 | ±0.7665 | +1.527 | 0.1269 | 1.7951 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0730**, LLR χ² = **31.30** (p = **9.88e-04**), AUC = **0.6715**, AIC = **421.6**, BIC = **471.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4200 | 2.3442 | ±4.6884 | -0.606 | 0.5447 | 0.2417 |  |
| Education: graduate level (vs college) | -0.3423 | 0.2764 | ±0.5528 | -1.238 | 0.2156 | 0.7101 |  |
| Education: high school or below (vs college) | +0.3149 | 0.4205 | ±0.8411 | +0.749 | 0.4539 | 1.3702 |  |
| Site: UCSD (vs UAB) | -0.0150 | 0.3416 | ±0.6832 | -0.044 | 0.9649 | 0.9851 |  |
| Site: UW (vs UAB) | +0.3987 | 0.3265 | ±0.6531 | +1.221 | 0.2221 | 1.4899 |  |
| **Age (years)** | **-0.0412** | 0.0129 | ±0.0257 | **-3.198** | **0.0014** | 0.9597 | ** |
| **BMI (kg/m2)** | **+0.0360** | 0.0169 | ±0.0338 | **+2.127** | **0.0334** | 1.0366 | * |
| Hypertension | +0.1839 | 0.2833 | ±0.5667 | +0.649 | 0.5162 | 1.2019 |  |
| High cholesterol | +0.4344 | 0.2743 | ±0.5487 | +1.583 | 0.1133 | 1.5440 |  |
| Kidney disease | +0.5093 | 0.5169 | ±1.0337 | +0.985 | 0.3245 | 1.6641 |  |
| Circulatory disease | +0.5895 | 0.3839 | ±0.7677 | +1.536 | 0.1246 | 1.8031 |  |
| HbA1c (%) | +0.1437 | 0.4082 | ±0.8165 | +0.352 | 0.7248 | 1.1546 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0728**, LLR χ² = **31.23** (p = **0.0010**), AUC = **0.6732**, AIC = **421.6**, BIC = **471.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.1340 | 2.1404 | ±4.2807 | -0.530 | 0.5962 | 0.3217 |  |
| Education: graduate level (vs college) | -0.3473 | 0.2760 | ±0.5520 | -1.259 | 0.2082 | 0.7066 |  |
| Education: high school or below (vs college) | +0.3314 | 0.4192 | ±0.8384 | +0.791 | 0.4291 | 1.3930 |  |
| Site: UCSD (vs UAB) | -0.0233 | 0.3407 | ±0.6814 | -0.068 | 0.9455 | 0.9770 |  |
| Site: UW (vs UAB) | +0.3897 | 0.3261 | ±0.6523 | +1.195 | 0.2321 | 1.4765 |  |
| **Age (years)** | **-0.0407** | 0.0128 | ±0.0257 | **-3.172** | **0.0015** | 0.9601 | ** |
| **BMI (kg/m2)** | **+0.0365** | 0.0168 | ±0.0335 | **+2.177** | **0.0294** | 1.0372 | * |
| Hypertension | +0.1909 | 0.2822 | ±0.5644 | +0.676 | 0.4988 | 1.2103 |  |
| High cholesterol | +0.4548 | 0.2696 | ±0.5391 | +1.687 | 0.0916 | 1.5759 | . |
| Kidney disease | +0.4951 | 0.5165 | ±1.0330 | +0.959 | 0.3377 | 1.6407 |  |
| Circulatory disease | +0.5841 | 0.3832 | ±0.7663 | +1.524 | 0.1274 | 1.7933 |  |
| Mean glucose (mg/dL) | +0.0041 | 0.0168 | ±0.0335 | +0.244 | 0.8073 | 1.0041 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0728**, LLR χ² = **31.23** (p = **0.0010**), AUC = **0.6732**, AIC = **421.6**, BIC = **471.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6997 | 4.3402 | ±8.6803 | -0.392 | 0.6953 | 0.1827 |  |
| Education: graduate level (vs college) | -0.3473 | 0.2760 | ±0.5520 | -1.259 | 0.2082 | 0.7066 |  |
| Education: high school or below (vs college) | +0.3314 | 0.4192 | ±0.8384 | +0.791 | 0.4291 | 1.3930 |  |
| Site: UCSD (vs UAB) | -0.0233 | 0.3407 | ±0.6814 | -0.068 | 0.9455 | 0.9770 |  |
| Site: UW (vs UAB) | +0.3897 | 0.3261 | ±0.6523 | +1.195 | 0.2321 | 1.4765 |  |
| **Age (years)** | **-0.0407** | 0.0128 | ±0.0257 | **-3.172** | **0.0015** | 0.9601 | ** |
| **BMI (kg/m2)** | **+0.0365** | 0.0168 | ±0.0335 | **+2.177** | **0.0294** | 1.0372 | * |
| Hypertension | +0.1909 | 0.2822 | ±0.5644 | +0.676 | 0.4988 | 1.2103 |  |
| High cholesterol | +0.4548 | 0.2696 | ±0.5391 | +1.687 | 0.0916 | 1.5759 | . |
| Kidney disease | +0.4951 | 0.5165 | ±1.0330 | +0.959 | 0.3377 | 1.6407 |  |
| Circulatory disease | +0.5841 | 0.3832 | ±0.7663 | +1.524 | 0.1274 | 1.7933 |  |
| GMI (%) | +0.1709 | 0.7006 | ±1.4013 | +0.244 | 0.8073 | 1.1864 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0731**, LLR χ² = **31.35** (p = **9.70e-04**), AUC = **0.6739**, AIC = **421.5**, BIC = **470.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3256 | 1.8396 | ±3.6792 | -0.721 | 0.4712 | 0.2656 |  |
| Education: graduate level (vs college) | -0.3443 | 0.2761 | ±0.5521 | -1.247 | 0.2123 | 0.7087 |  |
| Education: high school or below (vs college) | +0.3339 | 0.4195 | ±0.8390 | +0.796 | 0.4261 | 1.3964 |  |
| Site: UCSD (vs UAB) | -0.0286 | 0.3411 | ±0.6822 | -0.084 | 0.9332 | 0.9718 |  |
| Site: UW (vs UAB) | +0.3853 | 0.3266 | ±0.6532 | +1.180 | 0.2381 | 1.4700 |  |
| **Age (years)** | **-0.0400** | 0.0130 | ±0.0260 | **-3.075** | **0.0021** | 0.9608 | ** |
| **BMI (kg/m2)** | **+0.0358** | 0.0169 | ±0.0338 | **+2.117** | **0.0343** | 1.0364 | * |
| Hypertension | +0.1862 | 0.2826 | ±0.5651 | +0.659 | 0.5098 | 1.2047 |  |
| High cholesterol | +0.4531 | 0.2695 | ±0.5390 | +1.681 | 0.0927 | 1.5731 | . |
| Kidney disease | +0.5026 | 0.5157 | ±1.0314 | +0.975 | 0.3298 | 1.6530 |  |
| Circulatory disease | +0.5875 | 0.3829 | ±0.7659 | +1.534 | 0.1250 | 1.7995 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0055 | 0.0132 | ±0.0263 | +0.420 | 0.6745 | 1.0055 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0777**, LLR χ² = **33.33** (p = **4.65e-04**), AUC = **0.6792**, AIC = **419.5**, BIC = **469.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.0293 | 1.3382 | ±2.6763 | -1.517 | 0.1294 | 0.1314 |  |
| Education: graduate level (vs college) | -0.3201 | 0.2768 | ±0.5536 | -1.157 | 0.2474 | 0.7261 |  |
| Education: high school or below (vs college) | +0.3168 | 0.4215 | ±0.8431 | +0.752 | 0.4523 | 1.3727 |  |
| Site: UCSD (vs UAB) | +0.0157 | 0.3428 | ±0.6856 | +0.046 | 0.9635 | 1.0158 |  |
| Site: UW (vs UAB) | +0.4435 | 0.3292 | ±0.6584 | +1.347 | 0.1779 | 1.5581 |  |
| **Age (years)** | **-0.0412** | 0.0128 | ±0.0256 | **-3.215** | **0.0013** | 0.9596 | ** |
| **BMI (kg/m2)** | **+0.0362** | 0.0168 | ±0.0337 | **+2.147** | **0.0318** | 1.0368 | * |
| Hypertension | +0.1610 | 0.2843 | ±0.5686 | +0.566 | 0.5711 | 1.1747 |  |
| High cholesterol | +0.4747 | 0.2710 | ±0.5420 | +1.752 | 0.0798 | 1.6075 | . |
| Kidney disease | +0.3885 | 0.5299 | ±1.0598 | +0.733 | 0.4635 | 1.4747 |  |
| Circulatory disease | +0.5859 | 0.3845 | ±0.7690 | +1.524 | 0.1275 | 1.7967 |  |
| Glucose SD, pooled (mg/dL) | +0.0808 | 0.0553 | ±0.1106 | +1.462 | 0.1438 | 1.0842 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0783**, LLR χ² = **33.59** (p = **4.22e-04**), AUC = **0.6790**, AIC = **419.3**, BIC = **468.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.9462 | 1.2690 | ±2.5380 | -1.534 | 0.1251 | 0.1428 |  |
| Education: graduate level (vs college) | -0.3157 | 0.2769 | ±0.5539 | -1.140 | 0.2543 | 0.7293 |  |
| Education: high school or below (vs college) | +0.3325 | 0.4212 | ±0.8424 | +0.789 | 0.4298 | 1.3945 |  |
| Site: UCSD (vs UAB) | +0.0057 | 0.3421 | ±0.6841 | +0.017 | 0.9867 | 1.0057 |  |
| Site: UW (vs UAB) | +0.4380 | 0.3285 | ±0.6570 | +1.333 | 0.1824 | 1.5496 |  |
| **Age (years)** | **-0.0416** | 0.0129 | ±0.0257 | **-3.237** | **0.0012** | 0.9592 | ** |
| **BMI (kg/m2)** | **+0.0353** | 0.0169 | ±0.0339 | **+2.082** | **0.0373** | 1.0359 | * |
| Hypertension | +0.1719 | 0.2838 | ±0.5675 | +0.606 | 0.5447 | 1.1875 |  |
| High cholesterol | +0.4773 | 0.2714 | ±0.5428 | +1.759 | 0.0786 | 1.6117 | . |
| Kidney disease | +0.3854 | 0.5301 | ±1.0603 | +0.727 | 0.4672 | 1.4703 |  |
| Circulatory disease | +0.6011 | 0.3844 | ±0.7687 | +1.564 | 0.1179 | 1.8240 |  |
| Avg. daily SD (mg/dL) | +0.0855 | 0.0553 | ±0.1106 | +1.546 | 0.1221 | 1.0893 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0769**, LLR χ² = **32.96** (p = **5.33e-04**), AUC = **0.6763**, AIC = **419.9**, BIC = **469.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.8671 | 1.3166 | ±2.6331 | -1.418 | 0.1561 | 0.1546 |  |
| Education: graduate level (vs college) | -0.3245 | 0.2767 | ±0.5535 | -1.173 | 0.2410 | 0.7229 |  |
| Education: high school or below (vs college) | +0.3067 | 0.4213 | ±0.8426 | +0.728 | 0.4666 | 1.3589 |  |
| Site: UCSD (vs UAB) | +0.0113 | 0.3425 | ±0.6850 | +0.033 | 0.9738 | 1.0113 |  |
| Site: UW (vs UAB) | +0.4451 | 0.3292 | ±0.6584 | +1.352 | 0.1763 | 1.5607 |  |
| **Age (years)** | **-0.0414** | 0.0128 | ±0.0257 | **-3.224** | **0.0013** | 0.9594 | ** |
| **BMI (kg/m2)** | **+0.0369** | 0.0168 | ±0.0337 | **+2.189** | **0.0286** | 1.0375 | * |
| Hypertension | +0.1746 | 0.2834 | ±0.5669 | +0.616 | 0.5380 | 1.1907 |  |
| High cholesterol | +0.4678 | 0.2704 | ±0.5408 | +1.730 | 0.0836 | 1.5965 | . |
| Kidney disease | +0.4213 | 0.5266 | ±1.0533 | +0.800 | 0.4237 | 1.5240 |  |
| Circulatory disease | +0.5872 | 0.3847 | ±0.7693 | +1.526 | 0.1269 | 1.7989 |  |
| CV (%) | +0.0806 | 0.0604 | ±0.1207 | +1.336 | 0.1817 | 1.0840 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0764**, LLR χ² = **32.78** (p = **5.72e-04**), AUC = **0.6756**, AIC = **420.1**, BIC = **469.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.4295 | 1.2977 | ±2.5954 | +0.331 | 0.7407 | 1.5365 |  |
| Education: graduate level (vs college) | -0.3246 | 0.2767 | ±0.5534 | -1.173 | 0.2407 | 0.7228 |  |
| Education: high school or below (vs college) | +0.3023 | 0.4214 | ±0.8428 | +0.717 | 0.4731 | 1.3530 |  |
| Site: UCSD (vs UAB) | -0.0010 | 0.3416 | ±0.6832 | -0.003 | 0.9978 | 0.9990 |  |
| Site: UW (vs UAB) | +0.4324 | 0.3280 | ±0.6560 | +1.318 | 0.1874 | 1.5410 |  |
| **Age (years)** | **-0.0413** | 0.0128 | ±0.0257 | **-3.216** | **0.0013** | 0.9596 | ** |
| **BMI (kg/m2)** | **+0.0369** | 0.0168 | ±0.0336 | **+2.196** | **0.0281** | 1.0376 | * |
| Hypertension | +0.1766 | 0.2832 | ±0.5664 | +0.624 | 0.5329 | 1.1932 |  |
| High cholesterol | +0.4662 | 0.2702 | ±0.5403 | +1.726 | 0.0844 | 1.5939 | . |
| Kidney disease | +0.4454 | 0.5236 | ±1.0471 | +0.851 | 0.3949 | 1.5612 |  |
| Circulatory disease | +0.5923 | 0.3845 | ±0.7690 | +1.540 | 0.1235 | 1.8081 |  |
| Mean / SD ratio | -0.1601 | 0.1281 | ±0.2562 | -1.250 | 0.2113 | 0.8521 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0763**, LLR χ² = **32.73** (p = **5.83e-04**), AUC = **0.6759**, AIC = **420.1**, BIC = **469.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3294 | 1.2585 | ±2.5170 | +0.262 | 0.7935 | 1.3902 |  |
| Education: graduate level (vs college) | -0.3226 | 0.2768 | ±0.5535 | -1.166 | 0.2438 | 0.7243 |  |
| Education: high school or below (vs college) | +0.3127 | 0.4207 | ±0.8413 | +0.743 | 0.4572 | 1.3671 |  |
| Site: UCSD (vs UAB) | -0.0123 | 0.3411 | ±0.6822 | -0.036 | 0.9713 | 0.9878 |  |
| Site: UW (vs UAB) | +0.4248 | 0.3272 | ±0.6545 | +1.298 | 0.1942 | 1.5293 |  |
| **Age (years)** | **-0.0416** | 0.0129 | ±0.0257 | **-3.233** | **0.0012** | 0.9593 | ** |
| **BMI (kg/m2)** | **+0.0361** | 0.0168 | ±0.0337 | **+2.141** | **0.0322** | 1.0367 | * |
| Hypertension | +0.1879 | 0.2829 | ±0.5658 | +0.664 | 0.5065 | 1.2068 |  |
| High cholesterol | +0.4631 | 0.2703 | ±0.5405 | +1.713 | 0.0866 | 1.5890 | . |
| Kidney disease | +0.4472 | 0.5228 | ±1.0457 | +0.855 | 0.3924 | 1.5639 |  |
| Circulatory disease | +0.6100 | 0.3844 | ±0.7689 | +1.587 | 0.1126 | 1.8404 |  |
| Avg. daily mean/SD | -0.1235 | 0.1012 | ±0.2023 | -1.221 | 0.2222 | 0.8838 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0983**, LLR χ² = **42.15** (p = **1.53e-05**), AUC = **0.7015**, AIC = **410.7**, BIC = **460.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.5854** | 1.3207 | ±2.6413 | **-2.715** | **0.0066** | 0.0277 | ** |
| Education: graduate level (vs college) | -0.3337 | 0.2797 | ±0.5595 | -1.193 | 0.2328 | 0.7162 |  |
| Education: high school or below (vs college) | +0.2176 | 0.4286 | ±0.8571 | +0.508 | 0.6117 | 1.2431 |  |
| Site: UCSD (vs UAB) | +0.0128 | 0.3444 | ±0.6889 | +0.037 | 0.9703 | 1.0129 |  |
| Site: UW (vs UAB) | +0.5094 | 0.3323 | ±0.6646 | +1.533 | 0.1253 | 1.6643 |  |
| **Age (years)** | **-0.0380** | 0.0129 | ±0.0257 | **-2.954** | **0.0031** | 0.9627 | ** |
| **BMI (kg/m2)** | **+0.0416** | 0.0173 | ±0.0345 | **+2.410** | **0.0159** | 1.0425 | * |
| Hypertension | +0.2476 | 0.2863 | ±0.5726 | +0.865 | 0.3871 | 1.2810 |  |
| High cholesterol | +0.4337 | 0.2730 | ±0.5459 | +1.589 | 0.1121 | 1.5429 |  |
| Kidney disease | +0.4400 | 0.5252 | ±1.0503 | +0.838 | 0.4021 | 1.5528 |  |
| Circulatory disease | +0.6625 | 0.3904 | ±0.7808 | +1.697 | 0.0897 | 1.9397 | . |
| **MAG (mg/dL/h)** | **+0.0728** | 0.0222 | ±0.0444 | **+3.283** | **0.0010** | 1.0755 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0813**, LLR χ² = **34.86** (p = **2.62e-04**), AUC = **0.6821**, AIC = **418.0**, BIC = **467.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.5277 | 1.3675 | ±2.7349 | -1.849 | 0.0645 | 0.0798 | . |
| Education: graduate level (vs college) | -0.3294 | 0.2770 | ±0.5540 | -1.189 | 0.2344 | 0.7194 |  |
| Education: high school or below (vs college) | +0.3109 | 0.4232 | ±0.8465 | +0.735 | 0.4626 | 1.3647 |  |
| Site: UCSD (vs UAB) | +0.0125 | 0.3423 | ±0.6847 | +0.037 | 0.9708 | 1.0126 |  |
| Site: UW (vs UAB) | +0.4466 | 0.3287 | ±0.6574 | +1.359 | 0.1743 | 1.5629 |  |
| **Age (years)** | **-0.0424** | 0.0129 | ±0.0259 | **-3.277** | **0.0010** | 0.9585 | ** |
| **BMI (kg/m2)** | **+0.0395** | 0.0168 | ±0.0336 | **+2.351** | **0.0187** | 1.0403 | * |
| Hypertension | +0.2147 | 0.2843 | ±0.5686 | +0.755 | 0.4502 | 1.2395 |  |
| High cholesterol | +0.4585 | 0.2715 | ±0.5429 | +1.689 | 0.0912 | 1.5818 | . |
| Kidney disease | +0.4237 | 0.5256 | ±1.0512 | +0.806 | 0.4202 | 1.5276 |  |
| Circulatory disease | +0.6095 | 0.3853 | ±0.7705 | +1.582 | 0.1136 | 1.8395 |  |
| Avg. daily range (mg/dL) | +0.0227 | 0.0119 | ±0.0239 | +1.900 | 0.0575 | 1.0229 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0750**, LLR χ² = **32.17** (p = **7.17e-04**), AUC = **0.6769**, AIC = **420.7**, BIC = **470.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0396 | 1.0290 | ±2.0579 | -1.010 | 0.3124 | 0.3536 |  |
| Education: graduate level (vs college) | -0.3501 | 0.2763 | ±0.5526 | -1.267 | 0.2051 | 0.7046 |  |
| Education: high school or below (vs college) | +0.2991 | 0.4207 | ±0.8414 | +0.711 | 0.4771 | 1.3487 |  |
| Site: UCSD (vs UAB) | +0.0000 | 0.3422 | ±0.6845 | +0.000 | 0.9999 | 1.0000 |  |
| Site: UW (vs UAB) | +0.3961 | 0.3270 | ±0.6541 | +1.211 | 0.2258 | 1.4860 |  |
| **Age (years)** | **-0.0403** | 0.0128 | ±0.0256 | **-3.147** | **0.0016** | 0.9605 | ** |
| **BMI (kg/m2)** | **+0.0369** | 0.0168 | ±0.0335 | **+2.203** | **0.0276** | 1.0376 | * |
| Hypertension | +0.1654 | 0.2843 | ±0.5686 | +0.582 | 0.5608 | 1.1798 |  |
| High cholesterol | +0.4378 | 0.2701 | ±0.5401 | +1.621 | 0.1050 | 1.5493 |  |
| Kidney disease | +0.4905 | 0.5181 | ±1.0362 | +0.947 | 0.3438 | 1.6331 |  |
| Circulatory disease | +0.5665 | 0.3846 | ±0.7693 | +1.473 | 0.1408 | 1.7621 |  |
| SD of daily means (mg/dL) | +0.0666 | 0.0663 | ±0.1325 | +1.005 | 0.3149 | 1.0689 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0730**, LLR χ² = **31.31** (p = **9.84e-04**), AUC = **0.6727**, AIC = **421.6**, BIC = **471.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -16.2666 | 42.5670 | ±85.1340 | -0.382 | 0.7024 | 0.0000 |  |
| Education: graduate level (vs college) | -0.3520 | 0.2762 | ±0.5524 | -1.274 | 0.2025 | 0.7033 |  |
| Education: high school or below (vs college) | +0.3218 | 0.4191 | ±0.8383 | +0.768 | 0.4426 | 1.3796 |  |
| Site: UCSD (vs UAB) | -0.0300 | 0.3412 | ±0.6825 | -0.088 | 0.9300 | 0.9705 |  |
| Site: UW (vs UAB) | +0.3873 | 0.3264 | ±0.6527 | +1.187 | 0.2353 | 1.4730 |  |
| **Age (years)** | **-0.0408** | 0.0128 | ±0.0257 | **-3.180** | **0.0015** | 0.9600 | ** |
| **BMI (kg/m2)** | **+0.0365** | 0.0168 | ±0.0336 | **+2.177** | **0.0295** | 1.0372 | * |
| Hypertension | +0.1958 | 0.2819 | ±0.5638 | +0.695 | 0.4873 | 1.2163 |  |
| High cholesterol | +0.4549 | 0.2694 | ±0.5388 | +1.689 | 0.0913 | 1.5760 | . |
| Kidney disease | +0.5178 | 0.5169 | ±1.0338 | +1.002 | 0.3165 | 1.6783 |  |
| Circulatory disease | +0.5784 | 0.3838 | ±0.7676 | +1.507 | 0.1318 | 1.7832 |  |
| Time in range 70-180, pooled (%) | +0.1568 | 0.4277 | ±0.8555 | +0.367 | 0.7139 | 1.1697 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0732**, LLR χ² = **31.39** (p = **9.54e-04**), AUC = **0.6723**, AIC = **421.5**, BIC = **470.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +18.4090 | 40.5270 | ±81.0540 | +0.454 | 0.6497 | 98837030.4365 |  |
| Education: graduate level (vs college) | -0.3427 | 0.2762 | ±0.5525 | -1.241 | 0.2147 | 0.7099 |  |
| Education: high school or below (vs college) | +0.3318 | 0.4189 | ±0.8377 | +0.792 | 0.4283 | 1.3934 |  |
| Site: UCSD (vs UAB) | -0.0187 | 0.3407 | ±0.6815 | -0.055 | 0.9562 | 0.9815 |  |
| Site: UW (vs UAB) | +0.3951 | 0.3257 | ±0.6513 | +1.213 | 0.2250 | 1.4845 |  |
| **Age (years)** | **-0.0409** | 0.0128 | ±0.0257 | **-3.184** | **0.0015** | 0.9599 | ** |
| **BMI (kg/m2)** | **+0.0370** | 0.0167 | ±0.0335 | **+2.210** | **0.0271** | 1.0377 | * |
| Hypertension | +0.2005 | 0.2823 | ±0.5646 | +0.710 | 0.4776 | 1.2220 |  |
| High cholesterol | +0.4484 | 0.2696 | ±0.5392 | +1.663 | 0.0963 | 1.5658 | . |
| Kidney disease | +0.4911 | 0.5167 | ±1.0334 | +0.950 | 0.3419 | 1.6341 |  |
| Circulatory disease | +0.5884 | 0.3834 | ±0.7668 | +1.535 | 0.1249 | 1.8011 |  |
| Avg. daily time in range 70-180 (%) | -0.1916 | 0.4070 | ±0.8141 | -0.471 | 0.6378 | 0.8256 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0755**, LLR χ² = **32.39** (p = **6.61e-04**), AUC = **0.6782**, AIC = **420.5**, BIC = **469.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5665 | 0.9630 | ±1.9260 | -0.588 | 0.5564 | 0.5675 |  |
| Education: graduate level (vs college) | -0.3563 | 0.2765 | ±0.5530 | -1.289 | 0.1975 | 0.7003 |  |
| Education: high school or below (vs college) | +0.2950 | 0.4216 | ±0.8431 | +0.700 | 0.4841 | 1.3431 |  |
| Site: UCSD (vs UAB) | -0.0755 | 0.3444 | ±0.6888 | -0.219 | 0.8265 | 0.9273 |  |
| Site: UW (vs UAB) | +0.3649 | 0.3277 | ±0.6554 | +1.113 | 0.2656 | 1.4403 |  |
| **Age (years)** | **-0.0412** | 0.0129 | ±0.0257 | **-3.205** | **0.0014** | 0.9596 | ** |
| **BMI (kg/m2)** | **+0.0369** | 0.0167 | ±0.0334 | **+2.213** | **0.0269** | 1.0376 | * |
| Hypertension | +0.2207 | 0.2836 | ±0.5672 | +0.778 | 0.4365 | 1.2469 |  |
| High cholesterol | +0.4544 | 0.2702 | ±0.5404 | +1.682 | 0.0926 | 1.5752 | . |
| Kidney disease | +0.4605 | 0.5179 | ±1.0358 | +0.889 | 0.3739 | 1.5849 |  |
| Circulatory disease | +0.5935 | 0.3841 | ±0.7683 | +1.545 | 0.1224 | 1.8103 |  |
| Any reading < 54 during wear (0/1) | -0.3968 | 0.3700 | ±0.7400 | -1.073 | 0.2835 | 0.6724 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0774**, LLR χ² = **33.19** (p = **4.90e-04**), AUC = **0.6797**, AIC = **419.7**, BIC = **469.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5712 | 0.9584 | ±1.9167 | -0.596 | 0.5511 | 0.5648 |  |
| Education: graduate level (vs college) | -0.3576 | 0.2770 | ±0.5539 | -1.291 | 0.1967 | 0.6994 |  |
| Education: high school or below (vs college) | +0.2719 | 0.4223 | ±0.8446 | +0.644 | 0.5196 | 1.3125 |  |
| Site: UCSD (vs UAB) | -0.0788 | 0.3428 | ±0.6856 | -0.230 | 0.8181 | 0.9242 |  |
| Site: UW (vs UAB) | +0.3736 | 0.3273 | ±0.6545 | +1.142 | 0.2536 | 1.4530 |  |
| **Age (years)** | **-0.0420** | 0.0129 | ±0.0258 | **-3.258** | **0.0011** | 0.9589 | ** |
| **BMI (kg/m2)** | **+0.0385** | 0.0167 | ±0.0334 | **+2.302** | **0.0214** | 1.0392 | * |
| Hypertension | +0.2339 | 0.2843 | ±0.5685 | +0.823 | 0.4107 | 1.2635 |  |
| High cholesterol | +0.4401 | 0.2701 | ±0.5402 | +1.629 | 0.1032 | 1.5529 |  |
| Kidney disease | +0.4649 | 0.5179 | ±1.0358 | +0.898 | 0.3694 | 1.5919 |  |
| Circulatory disease | +0.6104 | 0.3846 | ±0.7692 | +1.587 | 0.1125 | 1.8412 |  |
| Time < 54 (%) | -3.6716 | 2.8489 | ±5.6977 | -1.289 | 0.1975 | 0.0254 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0733**, LLR χ² = **31.44** (p = **9.37e-04**), AUC = **0.6731**, AIC = **421.4**, BIC = **470.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6568 | 0.9578 | ±1.9156 | -0.686 | 0.4929 | 0.5185 |  |
| Education: graduate level (vs college) | -0.3491 | 0.2762 | ±0.5524 | -1.264 | 0.2063 | 0.7054 |  |
| Education: high school or below (vs college) | +0.3159 | 0.4196 | ±0.8392 | +0.753 | 0.4515 | 1.3715 |  |
| Site: UCSD (vs UAB) | -0.0319 | 0.3411 | ±0.6822 | -0.093 | 0.9256 | 0.9686 |  |
| Site: UW (vs UAB) | +0.3934 | 0.3262 | ±0.6523 | +1.206 | 0.2277 | 1.4820 |  |
| **Age (years)** | **-0.0409** | 0.0128 | ±0.0257 | **-3.186** | **0.0014** | 0.9599 | ** |
| **BMI (kg/m2)** | **+0.0371** | 0.0167 | ±0.0335 | **+2.217** | **0.0266** | 1.0378 | * |
| Hypertension | +0.1966 | 0.2822 | ±0.5643 | +0.697 | 0.4859 | 1.2173 |  |
| High cholesterol | +0.4509 | 0.2695 | ±0.5390 | +1.673 | 0.0943 | 1.5697 | . |
| Kidney disease | +0.4924 | 0.5162 | ±1.0325 | +0.954 | 0.3401 | 1.6363 |  |
| Circulatory disease | +0.6008 | 0.3845 | ±0.7690 | +1.563 | 0.1181 | 1.8236 |  |
| Avg. daily time < 54 (%) | -1.6434 | 3.3372 | ±6.6745 | -0.492 | 0.6224 | 0.1933 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0762**, LLR χ² = **32.67** (p = **5.95e-04**), AUC = **0.6802**, AIC = **420.2**, BIC = **469.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7946 | 0.9673 | ±1.9345 | -0.821 | 0.4114 | 0.4518 |  |
| Education: graduate level (vs college) | -0.3405 | 0.2765 | ±0.5531 | -1.231 | 0.2182 | 0.7114 |  |
| Education: high school or below (vs college) | +0.2904 | 0.4212 | ±0.8424 | +0.690 | 0.4905 | 1.3370 |  |
| Site: UCSD (vs UAB) | -0.0121 | 0.3410 | ±0.6819 | -0.035 | 0.9717 | 0.9880 |  |
| Site: UW (vs UAB) | +0.4218 | 0.3271 | ±0.6542 | +1.289 | 0.1972 | 1.5247 |  |
| **Age (years)** | **-0.0412** | 0.0129 | ±0.0257 | **-3.202** | **0.0014** | 0.9596 | ** |
| **BMI (kg/m2)** | **+0.0371** | 0.0168 | ±0.0337 | **+2.204** | **0.0275** | 1.0378 | * |
| Hypertension | +0.2163 | 0.2831 | ±0.5662 | +0.764 | 0.4450 | 1.2414 |  |
| High cholesterol | +0.4244 | 0.2706 | ±0.5413 | +1.568 | 0.1169 | 1.5286 |  |
| Kidney disease | +0.5455 | 0.5200 | ±1.0400 | +1.049 | 0.2942 | 1.7255 |  |
| Circulatory disease | +0.6002 | 0.3843 | ±0.7685 | +1.562 | 0.1183 | 1.8224 |  |
| Time 54-69, pooled (%) | +0.8272 | 0.6639 | ±1.3278 | +1.246 | 0.2128 | 2.2868 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0754**, LLR χ² = **32.33** (p = **6.75e-04**), AUC = **0.6768**, AIC = **420.5**, BIC = **470.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7471 | 0.9627 | ±1.9255 | -0.776 | 0.4378 | 0.4737 |  |
| Education: graduate level (vs college) | -0.3381 | 0.2765 | ±0.5530 | -1.223 | 0.2213 | 0.7131 |  |
| Education: high school or below (vs college) | +0.2890 | 0.4214 | ±0.8429 | +0.686 | 0.4929 | 1.3351 |  |
| Site: UCSD (vs UAB) | -0.0217 | 0.3408 | ±0.6816 | -0.064 | 0.9492 | 0.9785 |  |
| Site: UW (vs UAB) | +0.4096 | 0.3265 | ±0.6530 | +1.255 | 0.2096 | 1.5062 |  |
| **Age (years)** | **-0.0415** | 0.0129 | ±0.0258 | **-3.223** | **0.0013** | 0.9593 | ** |
| **BMI (kg/m2)** | **+0.0370** | 0.0168 | ±0.0336 | **+2.205** | **0.0274** | 1.0377 | * |
| Hypertension | +0.2353 | 0.2853 | ±0.5706 | +0.825 | 0.4094 | 1.2653 |  |
| High cholesterol | +0.4314 | 0.2704 | ±0.5407 | +1.596 | 0.1106 | 1.5395 |  |
| Kidney disease | +0.5390 | 0.5184 | ±1.0368 | +1.040 | 0.2985 | 1.7144 |  |
| Circulatory disease | +0.5842 | 0.3839 | ±0.7679 | +1.522 | 0.1281 | 1.7936 |  |
| Avg. daily time 54-69 (%) | +0.7435 | 0.6789 | ±1.3578 | +1.095 | 0.2735 | 2.1033 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0739**, LLR χ² = **31.68** (p = **8.59e-04**), AUC = **0.6757**, AIC = **421.2**, BIC = **470.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7453 | 0.9668 | ±1.9335 | -0.771 | 0.4407 | 0.4746 |  |
| Education: graduate level (vs college) | -0.3437 | 0.2762 | ±0.5524 | -1.244 | 0.2134 | 0.7091 |  |
| Education: high school or below (vs college) | +0.3164 | 0.4191 | ±0.8382 | +0.755 | 0.4504 | 1.3721 |  |
| Site: UCSD (vs UAB) | -0.0086 | 0.3413 | ±0.6826 | -0.025 | 0.9798 | 0.9914 |  |
| Site: UW (vs UAB) | +0.4107 | 0.3269 | ±0.6538 | +1.256 | 0.2090 | 1.5079 |  |
| **Age (years)** | **-0.0408** | 0.0128 | ±0.0257 | **-3.179** | **0.0015** | 0.9600 | ** |
| **BMI (kg/m2)** | **+0.0366** | 0.0168 | ±0.0336 | **+2.180** | **0.0292** | 1.0373 | * |
| Hypertension | +0.1985 | 0.2821 | ±0.5642 | +0.704 | 0.4815 | 1.2196 |  |
| High cholesterol | +0.4405 | 0.2699 | ±0.5398 | +1.632 | 0.1027 | 1.5535 |  |
| Kidney disease | +0.5283 | 0.5181 | ±1.0362 | +1.020 | 0.3079 | 1.6961 |  |
| Circulatory disease | +0.5896 | 0.3836 | ±0.7672 | +1.537 | 0.1243 | 1.8032 |  |
| Time < 70 (%) | +0.4260 | 0.5922 | ±1.1844 | +0.719 | 0.4719 | 1.5312 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0744**, LLR χ² = **31.92** (p = **7.85e-04**), AUC = **0.6756**, AIC = **421.0**, BIC = **470.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7291 | 0.9624 | ±1.9249 | -0.758 | 0.4487 | 0.4824 |  |
| Education: graduate level (vs college) | -0.3414 | 0.2763 | ±0.5526 | -1.235 | 0.2167 | 0.7108 |  |
| Education: high school or below (vs college) | +0.3035 | 0.4201 | ±0.8402 | +0.722 | 0.4700 | 1.3546 |  |
| Site: UCSD (vs UAB) | -0.0182 | 0.3408 | ±0.6815 | -0.053 | 0.9575 | 0.9820 |  |
| Site: UW (vs UAB) | +0.4051 | 0.3263 | ±0.6525 | +1.242 | 0.2143 | 1.4995 |  |
| **Age (years)** | **-0.0413** | 0.0129 | ±0.0257 | **-3.209** | **0.0013** | 0.9595 | ** |
| **BMI (kg/m2)** | **+0.0368** | 0.0168 | ±0.0336 | **+2.192** | **0.0284** | 1.0375 | * |
| Hypertension | +0.2222 | 0.2842 | ±0.5684 | +0.782 | 0.4343 | 1.2488 |  |
| High cholesterol | +0.4380 | 0.2700 | ±0.5400 | +1.622 | 0.1048 | 1.5496 |  |
| Kidney disease | +0.5323 | 0.5178 | ±1.0355 | +1.028 | 0.3039 | 1.7029 |  |
| Circulatory disease | +0.5785 | 0.3838 | ±0.7677 | +1.507 | 0.1318 | 1.7834 |  |
| Avg. daily time < 70 (%) | +0.5432 | 0.6183 | ±1.2365 | +0.879 | 0.3796 | 1.7215 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0781**, LLR χ² = **33.49** (p = **4.39e-04**), AUC = **0.6805**, AIC = **419.4**, BIC = **468.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -392.0423 | 285.9276 | ±571.8551 | -1.371 | 0.1703 | 0.0000 |  |
| Education: graduate level (vs college) | -0.3608 | 0.2773 | ±0.5545 | -1.301 | 0.1932 | 0.6971 |  |
| Education: high school or below (vs college) | +0.2661 | 0.4226 | ±0.8451 | +0.630 | 0.5288 | 1.3049 |  |
| Site: UCSD (vs UAB) | -0.0840 | 0.3430 | ±0.6859 | -0.245 | 0.8066 | 0.9195 |  |
| Site: UW (vs UAB) | +0.3732 | 0.3276 | ±0.6551 | +1.139 | 0.2546 | 1.4524 |  |
| **Age (years)** | **-0.0422** | 0.0129 | ±0.0258 | **-3.274** | **0.0011** | 0.9587 | ** |
| **BMI (kg/m2)** | **+0.0384** | 0.0167 | ±0.0334 | **+2.295** | **0.0218** | 1.0391 | * |
| Hypertension | +0.2337 | 0.2842 | ±0.5684 | +0.822 | 0.4109 | 1.2633 |  |
| High cholesterol | +0.4432 | 0.2703 | ±0.5406 | +1.640 | 0.1011 | 1.5576 |  |
| Kidney disease | +0.4625 | 0.5180 | ±1.0360 | +0.893 | 0.3719 | 1.5880 |  |
| Circulatory disease | +0.6116 | 0.3847 | ±0.7694 | +1.590 | 0.1119 | 1.8435 |  |
| Time 54-250, pooled (%) | +3.9150 | 2.8599 | ±5.7199 | +1.369 | 0.1710 | 50.1472 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0738**, LLR χ² = **31.64** (p = **8.72e-04**), AUC = **0.6738**, AIC = **421.2**, BIC = **470.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -218.7709 | 342.3242 | ±684.6483 | -0.639 | 0.5228 | 0.0000 |  |
| Education: graduate level (vs college) | -0.3508 | 0.2765 | ±0.5530 | -1.269 | 0.2045 | 0.7041 |  |
| Education: high school or below (vs college) | +0.3110 | 0.4199 | ±0.8397 | +0.741 | 0.4588 | 1.3649 |  |
| Site: UCSD (vs UAB) | -0.0364 | 0.3413 | ±0.6826 | -0.107 | 0.9152 | 0.9643 |  |
| Site: UW (vs UAB) | +0.3933 | 0.3265 | ±0.6530 | +1.205 | 0.2284 | 1.4818 |  |
| **Age (years)** | **-0.0410** | 0.0128 | ±0.0257 | **-3.196** | **0.0014** | 0.9598 | ** |
| **BMI (kg/m2)** | **+0.0370** | 0.0167 | ±0.0335 | **+2.214** | **0.0268** | 1.0377 | * |
| Hypertension | +0.1955 | 0.2822 | ±0.5645 | +0.693 | 0.4885 | 1.2159 |  |
| High cholesterol | +0.4523 | 0.2696 | ±0.5393 | +1.677 | 0.0935 | 1.5719 | . |
| Kidney disease | +0.4895 | 0.5163 | ±1.0326 | +0.948 | 0.3432 | 1.6314 |  |
| Circulatory disease | +0.6054 | 0.3845 | ±0.7690 | +1.574 | 0.1154 | 1.8319 |  |
| Avg. daily time 54-250 (%) | +2.1813 | 3.4236 | ±6.8472 | +0.637 | 0.5240 | 8.8580 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0747**, LLR χ² = **32.02** (p = **7.58e-04**), AUC = **0.6782**, AIC = **420.9**, BIC = **470.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5280 | 0.9807 | ±1.9613 | -0.538 | 0.5903 | 0.5898 |  |
| Education: graduate level (vs college) | -0.3541 | 0.2763 | ±0.5526 | -1.281 | 0.2001 | 0.7018 |  |
| Education: high school or below (vs college) | +0.3054 | 0.4202 | ±0.8404 | +0.727 | 0.4673 | 1.3572 |  |
| Site: UCSD (vs UAB) | -0.0270 | 0.3410 | ±0.6819 | -0.079 | 0.9370 | 0.9734 |  |
| Site: UW (vs UAB) | +0.3951 | 0.3266 | ±0.6532 | +1.210 | 0.2264 | 1.4845 |  |
| **Age (years)** | **-0.0408** | 0.0129 | ±0.0257 | **-3.172** | **0.0015** | 0.9601 | ** |
| **BMI (kg/m2)** | **+0.0361** | 0.0169 | ±0.0339 | **+2.128** | **0.0333** | 1.0367 | * |
| Hypertension | +0.2039 | 0.2823 | ±0.5645 | +0.722 | 0.4701 | 1.2262 |  |
| High cholesterol | +0.4468 | 0.2695 | ±0.5389 | +1.658 | 0.0973 | 1.5633 | . |
| Kidney disease | +0.5676 | 0.5210 | ±1.0421 | +1.089 | 0.2760 | 1.7641 |  |
| Circulatory disease | +0.5717 | 0.3841 | ±0.7683 | +1.488 | 0.1367 | 1.7712 |  |
| Time 181-250, pooled (%) | -0.4291 | 0.4705 | ±0.9410 | -0.912 | 0.3618 | 0.6511 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0727**, LLR χ² = **31.18** (p = **0.0010**), AUC = **0.6725**, AIC = **421.7**, BIC = **471.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6571 | 0.9711 | ±1.9421 | -0.677 | 0.4986 | 0.5184 |  |
| Education: graduate level (vs college) | -0.3489 | 0.2761 | ±0.5522 | -1.264 | 0.2063 | 0.7055 |  |
| Education: high school or below (vs college) | +0.3243 | 0.4197 | ±0.8394 | +0.773 | 0.4396 | 1.3831 |  |
| Site: UCSD (vs UAB) | -0.0236 | 0.3407 | ±0.6814 | -0.069 | 0.9449 | 0.9767 |  |
| Site: UW (vs UAB) | +0.3930 | 0.3258 | ±0.6516 | +1.206 | 0.2277 | 1.4815 |  |
| **Age (years)** | **-0.0409** | 0.0128 | ±0.0257 | **-3.183** | **0.0015** | 0.9600 | ** |
| **BMI (kg/m2)** | **+0.0367** | 0.0167 | ±0.0335 | **+2.192** | **0.0284** | 1.0374 | * |
| Hypertension | +0.1945 | 0.2819 | ±0.5639 | +0.690 | 0.4902 | 1.2147 |  |
| High cholesterol | +0.4525 | 0.2693 | ±0.5386 | +1.680 | 0.0929 | 1.5722 | . |
| Kidney disease | +0.5059 | 0.5178 | ±1.0357 | +0.977 | 0.3286 | 1.6585 |  |
| Circulatory disease | +0.5842 | 0.3835 | ±0.7670 | +1.523 | 0.1277 | 1.7935 |  |
| Avg. daily time 181-250 (%) | -0.0306 | 0.4548 | ±0.9097 | -0.067 | 0.9463 | 0.9698 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0747**, LLR χ² = **32.06** (p = **7.47e-04**), AUC = **0.6780**, AIC = **420.8**, BIC = **470.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5222 | 0.9815 | ±1.9630 | -0.532 | 0.5947 | 0.5932 |  |
| Education: graduate level (vs college) | -0.3544 | 0.2763 | ±0.5527 | -1.282 | 0.1997 | 0.7016 |  |
| Education: high school or below (vs college) | +0.3046 | 0.4202 | ±0.8405 | +0.725 | 0.4685 | 1.3561 |  |
| Site: UCSD (vs UAB) | -0.0275 | 0.3410 | ±0.6820 | -0.081 | 0.9357 | 0.9729 |  |
| Site: UW (vs UAB) | +0.3950 | 0.3266 | ±0.6533 | +1.209 | 0.2266 | 1.4843 |  |
| **Age (years)** | **-0.0408** | 0.0129 | ±0.0257 | **-3.174** | **0.0015** | 0.9600 | ** |
| **BMI (kg/m2)** | **+0.0360** | 0.0170 | ±0.0339 | **+2.125** | **0.0336** | 1.0367 | * |
| Hypertension | +0.2038 | 0.2822 | ±0.5645 | +0.722 | 0.4702 | 1.2261 |  |
| High cholesterol | +0.4470 | 0.2695 | ±0.5389 | +1.659 | 0.0972 | 1.5636 | . |
| Kidney disease | +0.5690 | 0.5211 | ±1.0421 | +1.092 | 0.2748 | 1.7666 |  |
| Circulatory disease | +0.5714 | 0.3842 | ±0.7683 | +1.487 | 0.1369 | 1.7707 |  |
| Time > 180 (%) | -0.4384 | 0.4698 | ±0.9397 | -0.933 | 0.3508 | 0.6451 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0727**, LLR χ² = **31.18** (p = **0.0010**), AUC = **0.6726**, AIC = **421.7**, BIC = **471.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6530 | 0.9717 | ±1.9433 | -0.672 | 0.5016 | 0.5205 |  |
| Education: graduate level (vs college) | -0.3491 | 0.2761 | ±0.5522 | -1.265 | 0.2061 | 0.7053 |  |
| Education: high school or below (vs college) | +0.3236 | 0.4197 | ±0.8394 | +0.771 | 0.4407 | 1.3821 |  |
| Site: UCSD (vs UAB) | -0.0237 | 0.3407 | ±0.6814 | -0.070 | 0.9445 | 0.9765 |  |
| Site: UW (vs UAB) | +0.3931 | 0.3258 | ±0.6516 | +1.207 | 0.2276 | 1.4816 |  |
| **Age (years)** | **-0.0409** | 0.0128 | ±0.0257 | **-3.184** | **0.0015** | 0.9600 | ** |
| **BMI (kg/m2)** | **+0.0367** | 0.0167 | ±0.0335 | **+2.191** | **0.0284** | 1.0374 | * |
| Hypertension | +0.1947 | 0.2819 | ±0.5639 | +0.691 | 0.4899 | 1.2149 |  |
| High cholesterol | +0.4524 | 0.2693 | ±0.5385 | +1.680 | 0.0929 | 1.5722 | . |
| Kidney disease | +0.5071 | 0.5178 | ±1.0356 | +0.979 | 0.3274 | 1.6605 |  |
| Circulatory disease | +0.5838 | 0.3835 | ±0.7671 | +1.522 | 0.1280 | 1.7929 |  |
| Avg. daily time > 180 (%) | -0.0418 | 0.4540 | ±0.9079 | -0.092 | 0.9265 | 0.9590 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0787**, LLR χ² = **33.75** (p = **3.98e-04**), AUC = **0.6815**, AIC = **419.1**, BIC = **468.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8933 | 0.9719 | ±1.9437 | -0.919 | 0.3580 | 0.4093 |  |
| Education: graduate level (vs college) | -0.3301 | 0.2776 | ±0.5552 | -1.189 | 0.2344 | 0.7188 |  |
| Education: high school or below (vs college) | +0.3345 | 0.4218 | ±0.8435 | +0.793 | 0.4277 | 1.3973 |  |
| Site: UCSD (vs UAB) | -0.0214 | 0.3415 | ±0.6831 | -0.063 | 0.9500 | 0.9788 |  |
| Site: UW (vs UAB) | +0.3823 | 0.3276 | ±0.6552 | +1.167 | 0.2432 | 1.4657 |  |
| **Age (years)** | **-0.0370** | 0.0130 | ±0.0260 | **-2.853** | **0.0043** | 0.9637 | ** |
| **BMI (kg/m2)** | **+0.0352** | 0.0169 | ±0.0337 | **+2.089** | **0.0367** | 1.0358 | * |
| Hypertension | +0.1494 | 0.2842 | ±0.5684 | +0.526 | 0.5991 | 1.1611 |  |
| High cholesterol | +0.4348 | 0.2701 | ±0.5403 | +1.609 | 0.1075 | 1.5446 |  |
| Kidney disease | +0.4667 | 0.5201 | ±1.0403 | +0.897 | 0.3695 | 1.5948 |  |
| Circulatory disease | +0.6224 | 0.3848 | ±0.7696 | +1.617 | 0.1058 | 1.8633 |  |
| Nocturnal time > 180 (%) | +0.4865 | 0.2969 | ±0.5938 | +1.639 | 0.1013 | 1.6266 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Total analysis base - Depression

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 56 single-predictor tests; 5 with raw p < 0.05 (about 3 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **CES-D-10 depressive symptoms (0-30)** (n = 454): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.017 vs -0.001 for covariates alone, gain +0.018; +0.661 per SD, p = 0.019). Raw p < 0.05 (FDR not applicable here): MAG (p = 0.005), %>180 nocturnal (p = 0.019), %54-250 (pooled) (p = 0.030), %<54 (pooled) (p = 0.031).
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 454): best single predictor out of sample is **MAG** (CV AUC 0.644 vs 0.607 for covariates alone, gain +0.037; OR 1.53 per SD, p = 0.001). Raw p < 0.05 (FDR not applicable here): MAG (p = 0.001).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Clinically relevant depressive symptoms (CES-D-10 >= 10) (+0.037, via MAG); CES-D-10 depressive symptoms (0-30) (+0.018, via %>180 nocturnal). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (0 FDR-significant / 2 raw-significant of 16); Band < 54 (0 FDR-significant / 1 raw-significant of 6); Band 54-250 (0 FDR-significant / 1 raw-significant of 4).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (2 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** CES-D-10 depressive symptoms (%>180 nocturnal, ΔAIC -9.2); Clinically relevant depressive symptoms (MAG, ΔAIC -10.9).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
