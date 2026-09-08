# Phase 6b model output tables - Hypoglycaemia exposure: at least one reading < 54 - Non-healthy group (T2D non-insulin + T2D insulin) - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 229; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **229**, R² = **0.1608**, Adj R² = **0.1223**, F-statistic = **4.18** (p = **2.64e-05**), Residual SE = **4.486** on **218** df, AIC = **1348.1**, BIC = **1385.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5522** | 2.5509 | ±5.1018 | **+3.353** | **8.01e-04** | *** |
| Education: graduate level (vs college) | -0.8676 | 0.6531 | ±1.3061 | -1.329 | 0.1840 |  |
| Education: high school or below (vs college) | +1.9976 | 1.0742 | ±2.1484 | +1.860 | 0.0629 | . |
| Site: UCSD (vs UAB) | +1.5738 | 0.8626 | ±1.7253 | +1.824 | 0.0681 | . |
| Site: UW (vs UAB) | -1.3343 | 0.6873 | ±1.3747 | -1.941 | 0.0522 | . |
| **Age (years)** | **-0.0841** | 0.0278 | ±0.0556 | **-3.025** | **0.0025** | ** |
| BMI (kg/m2) | +0.0675 | 0.0399 | ±0.0798 | +1.692 | 0.0906 | . |
| Hypertension | -0.3056 | 0.7533 | ±1.5065 | -0.406 | 0.6850 |  |
| High cholesterol | +1.0335 | 0.6424 | ±1.2847 | +1.609 | 0.1076 |  |
| Kidney disease | +1.8051 | 0.9734 | ±1.9467 | +1.855 | 0.0637 | . |
| Circulatory disease | +0.3732 | 0.7063 | ±1.4126 | +0.528 | 0.5972 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **229**, R² = **0.1749**, Adj R² = **0.1330**, F-statistic = **4.18** (p = **1.30e-05**), Residual SE = **4.459** on **217** df, AIC = **1346.2**, BIC = **1387.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.7464 | 2.9367 | ±5.8734 | +1.957 | 0.0504 | . |
| Education: graduate level (vs college) | -0.7091 | 0.6628 | ±1.3255 | -1.070 | 0.2846 |  |
| Education: high school or below (vs college) | +1.8303 | 1.0515 | ±2.1030 | +1.741 | 0.0817 | . |
| Site: UCSD (vs UAB) | +1.6018 | 0.8496 | ±1.6992 | +1.885 | 0.0594 | . |
| Site: UW (vs UAB) | -1.2711 | 0.6927 | ±1.3853 | -1.835 | 0.0665 | . |
| **Age (years)** | **-0.0925** | 0.0291 | ±0.0582 | **-3.179** | **0.0015** | ** |
| BMI (kg/m2) | +0.0650 | 0.0402 | ±0.0804 | +1.617 | 0.1059 |  |
| Hypertension | -0.3687 | 0.7489 | ±1.4979 | -0.492 | 0.6225 |  |
| High cholesterol | +1.0854 | 0.6377 | ±1.2755 | +1.702 | 0.0888 | . |
| Kidney disease | +1.7622 | 0.9897 | ±1.9793 | +1.781 | 0.0750 | . |
| Circulatory disease | +0.3653 | 0.7012 | ±1.4023 | +0.521 | 0.6023 |  |
| HbA1c (%) | +0.5242 | 0.3200 | ±0.6400 | +1.638 | 0.1013 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **229**, R² = **0.1765**, Adj R² = **0.1348**, F-statistic = **4.23** (p = **1.09e-05**), Residual SE = **4.454** on **217** df, AIC = **1345.7**, BIC = **1386.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.9832** | 2.7438 | ±5.4876 | **+2.181** | **0.0292** | * |
| Education: graduate level (vs college) | -0.8216 | 0.6583 | ±1.3167 | -1.248 | 0.2120 |  |
| Education: high school or below (vs college) | +1.8407 | 1.0535 | ±2.1070 | +1.747 | 0.0806 | . |
| Site: UCSD (vs UAB) | +1.5767 | 0.8504 | ±1.7009 | +1.854 | 0.0637 | . |
| Site: UW (vs UAB) | -1.2718 | 0.6966 | ±1.3932 | -1.826 | 0.0679 | . |
| **Age (years)** | **-0.0845** | 0.0281 | ±0.0561 | **-3.010** | **0.0026** | ** |
| BMI (kg/m2) | +0.0679 | 0.0396 | ±0.0793 | +1.712 | 0.0870 | . |
| Hypertension | -0.3486 | 0.7444 | ±1.4888 | -0.468 | 0.6395 |  |
| High cholesterol | +1.0576 | 0.6347 | ±1.2695 | +1.666 | 0.0957 | . |
| Kidney disease | +1.6497 | 1.0058 | ±2.0117 | +1.640 | 0.1010 |  |
| Circulatory disease | +0.3197 | 0.6942 | ±1.3884 | +0.460 | 0.6452 |  |
| **Mean glucose (mg/dL)** | **+0.0193** | 0.0097 | ±0.0194 | **+1.989** | **0.0467** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **229**, R² = **0.1765**, Adj R² = **0.1348**, F-statistic = **4.23** (p = **1.09e-05**), Residual SE = **4.454** on **217** df, AIC = **1345.7**, BIC = **1386.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.3109 | 3.4847 | ±6.9694 | +0.950 | 0.3420 |  |
| Education: graduate level (vs college) | -0.8216 | 0.6583 | ±1.3167 | -1.248 | 0.2120 |  |
| Education: high school or below (vs college) | +1.8407 | 1.0535 | ±2.1070 | +1.747 | 0.0806 | . |
| Site: UCSD (vs UAB) | +1.5767 | 0.8504 | ±1.7009 | +1.854 | 0.0637 | . |
| Site: UW (vs UAB) | -1.2718 | 0.6966 | ±1.3932 | -1.826 | 0.0679 | . |
| **Age (years)** | **-0.0845** | 0.0281 | ±0.0561 | **-3.010** | **0.0026** | ** |
| BMI (kg/m2) | +0.0679 | 0.0396 | ±0.0793 | +1.712 | 0.0870 | . |
| Hypertension | -0.3486 | 0.7444 | ±1.4888 | -0.468 | 0.6395 |  |
| High cholesterol | +1.0576 | 0.6347 | ±1.2695 | +1.666 | 0.0957 | . |
| Kidney disease | +1.6497 | 1.0058 | ±2.0117 | +1.640 | 0.1010 |  |
| Circulatory disease | +0.3197 | 0.6942 | ±1.3884 | +0.460 | 0.6452 |  |
| **GMI (%)** | **+0.8073** | 0.4060 | ±0.8119 | **+1.989** | **0.0467** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **229**, R² = **0.1972**, Adj R² = **0.1565**, F-statistic = **4.85** (p = **1.10e-06**), Residual SE = **4.398** on **217** df, AIC = **1339.9**, BIC = **1381.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.7106 | 2.7313 | ±5.4626 | +1.725 | 0.0846 | . |
| Education: graduate level (vs college) | -0.8917 | 0.6483 | ±1.2966 | -1.376 | 0.1690 |  |
| Education: high school or below (vs college) | +1.7787 | 1.0329 | ±2.0658 | +1.722 | 0.0851 | . |
| Site: UCSD (vs UAB) | +1.5764 | 0.8276 | ±1.6552 | +1.905 | 0.0568 | . |
| Site: UW (vs UAB) | -1.2638 | 0.6986 | ±1.3973 | -1.809 | 0.0705 | . |
| **Age (years)** | **-0.0797** | 0.0281 | ±0.0562 | **-2.838** | **0.0045** | ** |
| BMI (kg/m2) | +0.0661 | 0.0394 | ±0.0789 | +1.676 | 0.0938 | . |
| Hypertension | -0.4214 | 0.7352 | ±1.4705 | -0.573 | 0.5665 |  |
| High cholesterol | +0.9933 | 0.6225 | ±1.2449 | +1.596 | 0.1105 |  |
| Kidney disease | +1.7786 | 0.9924 | ±1.9848 | +1.792 | 0.0731 | . |
| Circulatory disease | +0.2916 | 0.6869 | ±1.3738 | +0.424 | 0.6712 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0289** | 0.0088 | ±0.0177 | **+3.271** | **0.0011** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **229**, R² = **0.1831**, Adj R² = **0.1417**, F-statistic = **4.42** (p = **5.32e-06**), Residual SE = **4.436** on **217** df, AIC = **1343.9**, BIC = **1385.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3904** | 2.6034 | ±5.2067 | **+2.839** | **0.0045** | ** |
| Education: graduate level (vs college) | -0.6924 | 0.6585 | ±1.3170 | -1.051 | 0.2931 |  |
| Education: high school or below (vs college) | +1.6329 | 1.0683 | ±2.1366 | +1.529 | 0.1264 |  |
| Site: UCSD (vs UAB) | +1.6189 | 0.8499 | ±1.6999 | +1.905 | 0.0568 | . |
| Site: UW (vs UAB) | -1.2113 | 0.6876 | ±1.3752 | -1.762 | 0.0781 | . |
| **Age (years)** | **-0.0947** | 0.0286 | ±0.0572 | **-3.314** | **9.20e-04** | *** |
| BMI (kg/m2) | +0.0725 | 0.0408 | ±0.0816 | +1.778 | 0.0754 | . |
| Hypertension | -0.3425 | 0.7365 | ±1.4729 | -0.465 | 0.6419 |  |
| High cholesterol | +1.0969 | 0.6362 | ±1.2724 | +1.724 | 0.0847 | . |
| Kidney disease | +1.3303 | 1.0426 | ±2.0852 | +1.276 | 0.2020 |  |
| Circulatory disease | +0.3845 | 0.6948 | ±1.3896 | +0.553 | 0.5800 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0488** | 0.0218 | ±0.0436 | **+2.238** | **0.0252** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **229**, R² = **0.1760**, Adj R² = **0.1342**, F-statistic = **4.21** (p = **1.15e-05**), Residual SE = **4.456** on **217** df, AIC = **1345.9**, BIC = **1387.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.5069** | 2.5984 | ±5.1969 | **+2.889** | **0.0039** | ** |
| Education: graduate level (vs college) | -0.7168 | 0.6602 | ±1.3204 | -1.086 | 0.2776 |  |
| Education: high school or below (vs college) | +1.6486 | 1.0874 | ±2.1747 | +1.516 | 0.1295 |  |
| Site: UCSD (vs UAB) | +1.6090 | 0.8560 | ±1.7119 | +1.880 | 0.0601 | . |
| Site: UW (vs UAB) | -1.2487 | 0.6895 | ±1.3789 | -1.811 | 0.0701 | . |
| **Age (years)** | **-0.0930** | 0.0285 | ±0.0569 | **-3.266** | **0.0011** | ** |
| BMI (kg/m2) | +0.0728 | 0.0406 | ±0.0812 | +1.792 | 0.0732 | . |
| Hypertension | -0.3115 | 0.7406 | ±1.4812 | -0.421 | 0.6740 |  |
| High cholesterol | +1.0741 | 0.6401 | ±1.2803 | +1.678 | 0.0933 | . |
| Kidney disease | +1.3989 | 1.0600 | ±2.1200 | +1.320 | 0.1869 |  |
| Circulatory disease | +0.4032 | 0.6986 | ±1.3972 | +0.577 | 0.5638 |  |
| Avg. daily SD (mg/dL) | +0.0476 | 0.0257 | ±0.0514 | +1.851 | 0.0642 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **229**, R² = **0.1713**, Adj R² = **0.1293**, F-statistic = **4.08** (p = **1.90e-05**), Residual SE = **4.468** on **217** df, AIC = **1347.2**, BIC = **1388.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.2919** | 2.7322 | ±5.4645 | **+2.669** | **0.0076** | ** |
| Education: graduate level (vs college) | -0.7118 | 0.6563 | ±1.3127 | -1.085 | 0.2781 |  |
| Education: high school or below (vs college) | +1.7066 | 1.1043 | ±2.2085 | +1.545 | 0.1222 |  |
| Site: UCSD (vs UAB) | +1.6094 | 0.8597 | ±1.7194 | +1.872 | 0.0612 | . |
| Site: UW (vs UAB) | -1.2495 | 0.6831 | ±1.3662 | -1.829 | 0.0674 | . |
| **Age (years)** | **-0.0969** | 0.0290 | ±0.0580 | **-3.345** | **8.24e-04** | *** |
| BMI (kg/m2) | +0.0724 | 0.0414 | ±0.0828 | +1.749 | 0.0803 | . |
| Hypertension | -0.3106 | 0.7449 | ±1.4898 | -0.417 | 0.6767 |  |
| High cholesterol | +1.0726 | 0.6443 | ±1.2887 | +1.665 | 0.0960 | . |
| Kidney disease | +1.3982 | 1.0691 | ±2.1381 | +1.308 | 0.1909 |  |
| Circulatory disease | +0.3972 | 0.7074 | ±1.4149 | +0.561 | 0.5745 |  |
| CV (%) | +0.0775 | 0.0530 | ±0.1061 | +1.461 | 0.1439 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **229**, R² = **0.1685**, Adj R² = **0.1264**, F-statistic = **4.00** (p = **2.55e-05**), Residual SE = **4.476** on **217** df, AIC = **1348.0**, BIC = **1389.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.7116** | 3.0177 | ±6.0354 | **+3.550** | **3.86e-04** | *** |
| Education: graduate level (vs college) | -0.7338 | 0.6613 | ±1.3226 | -1.110 | 0.2672 |  |
| Education: high school or below (vs college) | +1.7409 | 1.0989 | ±2.1977 | +1.584 | 0.1131 |  |
| Site: UCSD (vs UAB) | +1.5655 | 0.8604 | ±1.7208 | +1.820 | 0.0688 | . |
| Site: UW (vs UAB) | -1.2900 | 0.6876 | ±1.3752 | -1.876 | 0.0606 | . |
| **Age (years)** | **-0.0961** | 0.0287 | ±0.0574 | **-3.347** | **8.18e-04** | *** |
| BMI (kg/m2) | +0.0699 | 0.0404 | ±0.0808 | +1.730 | 0.0836 | . |
| Hypertension | -0.2859 | 0.7466 | ±1.4932 | -0.383 | 0.7018 |  |
| High cholesterol | +1.0690 | 0.6454 | ±1.2908 | +1.656 | 0.0976 | . |
| Kidney disease | +1.5581 | 1.0542 | ±2.1084 | +1.478 | 0.1394 |  |
| Circulatory disease | +0.3452 | 0.7128 | ±1.4256 | +0.484 | 0.6282 |  |
| Mean / SD ratio | -0.3374 | 0.2608 | ±0.5215 | -1.294 | 0.1957 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **229**, R² = **0.1622**, Adj R² = **0.1197**, F-statistic = **3.82** (p = **4.93e-05**), Residual SE = **4.493** on **217** df, AIC = **1349.7**, BIC = **1390.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.4421** | 2.9707 | ±5.9414 | **+3.178** | **0.0015** | ** |
| Education: graduate level (vs college) | -0.8041 | 0.6625 | ±1.3251 | -1.214 | 0.2248 |  |
| Education: high school or below (vs college) | +1.8880 | 1.1064 | ±2.2128 | +1.706 | 0.0879 | . |
| Site: UCSD (vs UAB) | +1.5608 | 0.8665 | ±1.7331 | +1.801 | 0.0717 | . |
| Site: UW (vs UAB) | -1.3259 | 0.6895 | ±1.3791 | -1.923 | 0.0545 | . |
| **Age (years)** | **-0.0893** | 0.0286 | ±0.0573 | **-3.120** | **0.0018** | ** |
| BMI (kg/m2) | +0.0688 | 0.0404 | ±0.0807 | +1.705 | 0.0883 | . |
| Hypertension | -0.2838 | 0.7513 | ±1.5026 | -0.378 | 0.7056 |  |
| High cholesterol | +1.0387 | 0.6466 | ±1.2933 | +1.606 | 0.1082 |  |
| Kidney disease | +1.7246 | 1.0271 | ±2.0542 | +1.679 | 0.0931 | . |
| Circulatory disease | +0.3705 | 0.7117 | ±1.4233 | +0.521 | 0.6026 |  |
| Avg. daily mean/SD | -0.1173 | 0.2071 | ±0.4143 | -0.566 | 0.5711 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **229**, R² = **0.1721**, Adj R² = **0.1301**, F-statistic = **4.10** (p = **1.75e-05**), Residual SE = **4.466** on **217** df, AIC = **1347.0**, BIC = **1388.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.7872** | 2.7437 | ±5.4874 | **+2.474** | **0.0134** | * |
| Education: graduate level (vs college) | -0.7709 | 0.6612 | ±1.3224 | -1.166 | 0.2436 |  |
| Education: high school or below (vs college) | +1.6935 | 1.0645 | ±2.1290 | +1.591 | 0.1116 |  |
| Site: UCSD (vs UAB) | +1.5123 | 0.8601 | ±1.7202 | +1.758 | 0.0787 | . |
| Site: UW (vs UAB) | -1.2472 | 0.6951 | ±1.3902 | -1.794 | 0.0728 | . |
| **Age (years)** | **-0.0879** | 0.0276 | ±0.0553 | **-3.178** | **0.0015** | ** |
| BMI (kg/m2) | +0.0621 | 0.0403 | ±0.0807 | +1.540 | 0.1236 |  |
| Hypertension | -0.2604 | 0.7498 | ±1.4997 | -0.347 | 0.7284 |  |
| High cholesterol | +1.0082 | 0.6381 | ±1.2762 | +1.580 | 0.1141 |  |
| Kidney disease | +1.7942 | 0.9792 | ±1.9583 | +1.832 | 0.0669 | . |
| Circulatory disease | +0.3656 | 0.7052 | ±1.4103 | +0.519 | 0.6041 |  |
| MAG (mg/dL/h) | +0.0483 | 0.0300 | ±0.0601 | +1.607 | 0.1081 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **229**, R² = **0.1767**, Adj R² = **0.1350**, F-statistic = **4.23** (p = **1.06e-05**), Residual SE = **4.454** on **217** df, AIC = **1345.7**, BIC = **1386.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.0140** | 2.6560 | ±5.3120 | **+2.641** | **0.0083** | ** |
| Education: graduate level (vs college) | -0.6994 | 0.6620 | ±1.3241 | -1.056 | 0.2907 |  |
| Education: high school or below (vs college) | +1.5964 | 1.0912 | ±2.1824 | +1.463 | 0.1435 |  |
| Site: UCSD (vs UAB) | +1.6051 | 0.8554 | ±1.7108 | +1.876 | 0.0606 | . |
| Site: UW (vs UAB) | -1.2778 | 0.6894 | ±1.3789 | -1.853 | 0.0638 | . |
| **Age (years)** | **-0.0928** | 0.0282 | ±0.0563 | **-3.296** | **9.80e-04** | *** |
| BMI (kg/m2) | +0.0739 | 0.0404 | ±0.0809 | +1.827 | 0.0678 | . |
| Hypertension | -0.2755 | 0.7407 | ±1.4814 | -0.372 | 0.7099 |  |
| High cholesterol | +1.0499 | 0.6394 | ±1.2789 | +1.642 | 0.1006 |  |
| Kidney disease | +1.4018 | 1.0651 | ±2.1302 | +1.316 | 0.1881 |  |
| Circulatory disease | +0.3516 | 0.7008 | ±1.4017 | +0.502 | 0.6159 |  |
| Avg. daily range (mg/dL) | +0.0138 | 0.0074 | ±0.0148 | +1.870 | 0.0615 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **229**, R² = **0.1948**, Adj R² = **0.1540**, F-statistic = **4.77** (p = **1.44e-06**), Residual SE = **4.404** on **217** df, AIC = **1340.6**, BIC = **1381.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.7645** | 2.5995 | ±5.1991 | **+2.987** | **0.0028** | ** |
| Education: graduate level (vs college) | -0.6573 | 0.6464 | ±1.2927 | -1.017 | 0.3092 |  |
| Education: high school or below (vs college) | +1.8647 | 1.0319 | ±2.0638 | +1.807 | 0.0708 | . |
| Site: UCSD (vs UAB) | +1.5842 | 0.8391 | ±1.6782 | +1.888 | 0.0590 | . |
| Site: UW (vs UAB) | -1.1858 | 0.6816 | ±1.3633 | -1.740 | 0.0819 | . |
| **Age (years)** | **-0.0913** | 0.0290 | ±0.0580 | **-3.147** | **0.0017** | ** |
| BMI (kg/m2) | +0.0719 | 0.0409 | ±0.0817 | +1.761 | 0.0783 | . |
| Hypertension | -0.5047 | 0.7419 | ±1.4838 | -0.680 | 0.4963 |  |
| High cholesterol | +1.1001 | 0.6274 | ±1.2548 | +1.753 | 0.0795 | . |
| Kidney disease | +1.4192 | 0.9679 | ±1.9358 | +1.466 | 0.1426 |  |
| Circulatory disease | +0.2239 | 0.7027 | ±1.4055 | +0.319 | 0.7500 |  |
| **SD of daily means (mg/dL)** | **+0.0952** | 0.0358 | ±0.0716 | **+2.658** | **0.0079** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **229**, R² = **0.1793**, Adj R² = **0.1377**, F-statistic = **4.31** (p = **8.03e-06**), Residual SE = **4.447** on **217** df, AIC = **1345.0**, BIC = **1386.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.8239** | 3.0680 | ±6.1359 | **+3.854** | **1.16e-04** | *** |
| Education: graduate level (vs college) | -0.7104 | 0.6563 | ±1.3126 | -1.082 | 0.2791 |  |
| Education: high school or below (vs college) | +1.8109 | 1.0612 | ±2.1223 | +1.707 | 0.0879 | . |
| Site: UCSD (vs UAB) | +1.6129 | 0.8472 | ±1.6943 | +1.904 | 0.0569 | . |
| Site: UW (vs UAB) | -1.2288 | 0.6918 | ±1.3836 | -1.776 | 0.0757 | . |
| **Age (years)** | **-0.0882** | 0.0281 | ±0.0563 | **-3.134** | **0.0017** | ** |
| BMI (kg/m2) | +0.0703 | 0.0398 | ±0.0795 | +1.768 | 0.0770 | . |
| Hypertension | -0.3049 | 0.7422 | ±1.4844 | -0.411 | 0.6812 |  |
| High cholesterol | +1.0077 | 0.6328 | ±1.2656 | +1.592 | 0.1113 |  |
| Kidney disease | +1.5286 | 1.0109 | ±2.0219 | +1.512 | 0.1305 |  |
| Circulatory disease | +0.2871 | 0.6979 | ±1.3958 | +0.411 | 0.6808 |  |
| **Time in range 70-180, pooled (%)** | **-0.0370** | 0.0172 | ±0.0343 | **-2.157** | **0.0310** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **229**, R² = **0.1793**, Adj R² = **0.1377**, F-statistic = **4.31** (p = **8.03e-06**), Residual SE = **4.447** on **217** df, AIC = **1345.0**, BIC = **1386.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.8151** | 3.0789 | ±6.1577 | **+3.838** | **1.24e-04** | *** |
| Education: graduate level (vs college) | -0.7111 | 0.6554 | ±1.3107 | -1.085 | 0.2779 |  |
| Education: high school or below (vs college) | +1.7924 | 1.0606 | ±2.1212 | +1.690 | 0.0910 | . |
| Site: UCSD (vs UAB) | +1.6175 | 0.8466 | ±1.6933 | +1.910 | 0.0561 | . |
| Site: UW (vs UAB) | -1.2214 | 0.6921 | ±1.3842 | -1.765 | 0.0776 | . |
| **Age (years)** | **-0.0882** | 0.0281 | ±0.0562 | **-3.138** | **0.0017** | ** |
| BMI (kg/m2) | +0.0708 | 0.0399 | ±0.0797 | +1.775 | 0.0758 | . |
| Hypertension | -0.2970 | 0.7423 | ±1.4846 | -0.400 | 0.6890 |  |
| High cholesterol | +1.0052 | 0.6325 | ±1.2650 | +1.589 | 0.1120 |  |
| Kidney disease | +1.5203 | 1.0078 | ±2.0156 | +1.508 | 0.1314 |  |
| Circulatory disease | +0.2861 | 0.6980 | ±1.3959 | +0.410 | 0.6819 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0370** | 0.0172 | ±0.0344 | **-2.149** | **0.0316** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **229**, R² = **0.1624**, Adj R² = **0.1199**, F-statistic = **3.82** (p = **4.84e-05**), Residual SE = **4.492** on **217** df, AIC = **1349.6**, BIC = **1390.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.6334** | 2.5531 | ±5.1061 | **+3.382** | **7.21e-04** | *** |
| Education: graduate level (vs college) | -0.8906 | 0.6580 | ±1.3160 | -1.354 | 0.1759 |  |
| Education: high school or below (vs college) | +1.9636 | 1.0695 | ±2.1390 | +1.836 | 0.0664 | . |
| Site: UCSD (vs UAB) | +1.5105 | 0.8727 | ±1.7453 | +1.731 | 0.0835 | . |
| **Site: UW (vs UAB)** | **-1.4089** | 0.7030 | ±1.4060 | **-2.004** | **0.0451** | * |
| **Age (years)** | **-0.0835** | 0.0278 | ±0.0556 | **-3.003** | **0.0027** | ** |
| BMI (kg/m2) | +0.0679 | 0.0398 | ±0.0796 | +1.707 | 0.0878 | . |
| Hypertension | -0.2938 | 0.7517 | ±1.5034 | -0.391 | 0.6959 |  |
| High cholesterol | +1.0418 | 0.6450 | ±1.2900 | +1.615 | 0.1063 |  |
| Kidney disease | +1.7913 | 0.9720 | ±1.9440 | +1.843 | 0.0653 | . |
| Circulatory disease | +0.4170 | 0.7183 | ±1.4367 | +0.581 | 0.5616 |  |
| Time < 54 (%) | -0.2639 | 0.4016 | ±0.8032 | -0.657 | 0.5111 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **229**, R² = **0.1610**, Adj R² = **0.1185**, F-statistic = **3.79** (p = **5.57e-05**), Residual SE = **4.496** on **217** df, AIC = **1350.0**, BIC = **1391.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5579** | 2.5529 | ±5.1058 | **+3.352** | **8.02e-04** | *** |
| Education: graduate level (vs college) | -0.8796 | 0.6556 | ±1.3113 | -1.342 | 0.1797 |  |
| Education: high school or below (vs college) | +1.9863 | 1.0715 | ±2.1430 | +1.854 | 0.0638 | . |
| Site: UCSD (vs UAB) | +1.5555 | 0.8649 | ±1.7297 | +1.799 | 0.0721 | . |
| Site: UW (vs UAB) | -1.3542 | 0.6965 | ±1.3930 | -1.944 | 0.0519 | . |
| **Age (years)** | **-0.0836** | 0.0282 | ±0.0564 | **-2.965** | **0.0030** | ** |
| BMI (kg/m2) | +0.0675 | 0.0401 | ±0.0802 | +1.685 | 0.0920 | . |
| Hypertension | -0.3038 | 0.7547 | ±1.5093 | -0.403 | 0.6872 |  |
| High cholesterol | +1.0299 | 0.6472 | ±1.2945 | +1.591 | 0.1116 |  |
| Kidney disease | +1.8062 | 0.9747 | ±1.9494 | +1.853 | 0.0639 | . |
| Circulatory disease | +0.3877 | 0.7319 | ±1.4639 | +0.530 | 0.5963 |  |
| Avg. daily time < 54 (%) | -0.0876 | 0.6516 | ±1.3031 | -0.134 | 0.8930 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **229**, R² = **0.1625**, Adj R² = **0.1201**, F-statistic = **3.83** (p = **4.77e-05**), Residual SE = **4.492** on **217** df, AIC = **1349.6**, BIC = **1390.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5492** | 2.5599 | ±5.1197 | **+3.340** | **8.39e-04** | *** |
| Education: graduate level (vs college) | -0.8016 | 0.6608 | ±1.3217 | -1.213 | 0.2251 |  |
| Education: high school or below (vs college) | +1.9760 | 1.0855 | ±2.1710 | +1.820 | 0.0687 | . |
| Site: UCSD (vs UAB) | +1.6034 | 0.8625 | ±1.7251 | +1.859 | 0.0630 | . |
| Site: UW (vs UAB) | -1.3184 | 0.6866 | ±1.3731 | -1.920 | 0.0548 | . |
| **Age (years)** | **-0.0869** | 0.0277 | ±0.0554 | **-3.138** | **0.0017** | ** |
| BMI (kg/m2) | +0.0680 | 0.0401 | ±0.0801 | +1.696 | 0.0899 | . |
| Hypertension | -0.2870 | 0.7591 | ±1.5181 | -0.378 | 0.7053 |  |
| High cholesterol | +1.0104 | 0.6463 | ±1.2926 | +1.563 | 0.1180 |  |
| Kidney disease | +1.7856 | 0.9743 | ±1.9485 | +1.833 | 0.0668 | . |
| Circulatory disease | +0.3640 | 0.7169 | ±1.4337 | +0.508 | 0.6116 |  |
| Time 54-69, pooled (%) | +0.0813 | 0.1244 | ±0.2489 | +0.654 | 0.5133 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **229**, R² = **0.1633**, Adj R² = **0.1209**, F-statistic = **3.85** (p = **4.39e-05**), Residual SE = **4.490** on **217** df, AIC = **1349.4**, BIC = **1390.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5922** | 2.5600 | ±5.1201 | **+3.356** | **7.90e-04** | *** |
| Education: graduate level (vs college) | -0.7872 | 0.6604 | ±1.3209 | -1.192 | 0.2333 |  |
| Education: high school or below (vs college) | +1.9630 | 1.0881 | ±2.1762 | +1.804 | 0.0712 | . |
| Site: UCSD (vs UAB) | +1.6065 | 0.8615 | ±1.7231 | +1.865 | 0.0622 | . |
| Site: UW (vs UAB) | -1.3124 | 0.6853 | ±1.3705 | -1.915 | 0.0555 | . |
| **Age (years)** | **-0.0880** | 0.0278 | ±0.0556 | **-3.166** | **0.0015** | ** |
| BMI (kg/m2) | +0.0679 | 0.0401 | ±0.0802 | +1.693 | 0.0905 | . |
| Hypertension | -0.2830 | 0.7593 | ±1.5186 | -0.373 | 0.7093 |  |
| High cholesterol | +1.0101 | 0.6478 | ±1.2956 | +1.559 | 0.1189 |  |
| Kidney disease | +1.7863 | 0.9721 | ±1.9442 | +1.838 | 0.0661 | . |
| Circulatory disease | +0.3688 | 0.7157 | ±1.4314 | +0.515 | 0.6063 |  |
| Avg. daily time 54-69 (%) | +0.0941 | 0.1224 | ±0.2448 | +0.769 | 0.4420 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **229**, R² = **0.1614**, Adj R² = **0.1189**, F-statistic = **3.80** (p = **5.35e-05**), Residual SE = **4.495** on **217** df, AIC = **1349.9**, BIC = **1391.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5383** | 2.5607 | ±5.1213 | **+3.334** | **8.55e-04** | *** |
| Education: graduate level (vs college) | -0.8314 | 0.6600 | ±1.3200 | -1.260 | 0.2078 |  |
| Education: high school or below (vs college) | +1.9921 | 1.0813 | ±2.1626 | +1.842 | 0.0654 | . |
| Site: UCSD (vs UAB) | +1.5981 | 0.8638 | ±1.7276 | +1.850 | 0.0643 | . |
| Site: UW (vs UAB) | -1.3151 | 0.6883 | ±1.3765 | -1.911 | 0.0560 | . |
| **Age (years)** | **-0.0856** | 0.0278 | ±0.0555 | **-3.085** | **0.0020** | ** |
| BMI (kg/m2) | +0.0677 | 0.0401 | ±0.0802 | +1.687 | 0.0915 | . |
| Hypertension | -0.2982 | 0.7578 | ±1.5155 | -0.394 | 0.6939 |  |
| High cholesterol | +1.0208 | 0.6458 | ±1.2916 | +1.581 | 0.1140 |  |
| Kidney disease | +1.7976 | 0.9763 | ±1.9526 | +1.841 | 0.0656 | . |
| Circulatory disease | +0.3620 | 0.7192 | ±1.4385 | +0.503 | 0.6148 |  |
| Time < 70 (%) | +0.0402 | 0.1096 | ±0.2193 | +0.367 | 0.7137 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **229**, R² = **0.1622**, Adj R² = **0.1197**, F-statistic = **3.82** (p = **4.93e-05**), Residual SE = **4.493** on **217** df, AIC = **1349.7**, BIC = **1390.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5728** | 2.5605 | ±5.1209 | **+3.348** | **8.13e-04** | *** |
| Education: graduate level (vs college) | -0.8107 | 0.6592 | ±1.3185 | -1.230 | 0.2188 |  |
| Education: high school or below (vs college) | +1.9839 | 1.0837 | ±2.1674 | +1.831 | 0.0671 | . |
| Site: UCSD (vs UAB) | +1.6057 | 0.8615 | ±1.7231 | +1.864 | 0.0623 | . |
| Site: UW (vs UAB) | -1.3079 | 0.6862 | ±1.3723 | -1.906 | 0.0566 | . |
| **Age (years)** | **-0.0868** | 0.0279 | ±0.0558 | **-3.110** | **0.0019** | ** |
| BMI (kg/m2) | +0.0677 | 0.0402 | ±0.0803 | +1.686 | 0.0918 | . |
| Hypertension | -0.2930 | 0.7584 | ±1.5168 | -0.386 | 0.6993 |  |
| High cholesterol | +1.0216 | 0.6472 | ±1.2944 | +1.578 | 0.1145 |  |
| Kidney disease | +1.7929 | 0.9747 | ±1.9493 | +1.840 | 0.0658 | . |
| Circulatory disease | +0.3610 | 0.7187 | ±1.4374 | +0.502 | 0.6154 |  |
| Avg. daily time < 70 (%) | +0.0574 | 0.1101 | ±0.2202 | +0.521 | 0.6021 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **229**, R² = **0.2007**, Adj R² = **0.1601**, F-statistic = **4.95** (p = **7.42e-07**), Residual SE = **4.388** on **217** df, AIC = **1338.9**, BIC = **1380.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.6472** | 3.3273 | ±6.6545 | **+5.604** | **2.09e-08** | *** |
| Education: graduate level (vs college) | -0.7154 | 0.6531 | ±1.3062 | -1.095 | 0.2734 |  |
| Education: high school or below (vs college) | +1.7042 | 1.0275 | ±2.0549 | +1.659 | 0.0972 | . |
| **Site: UCSD (vs UAB)** | **+1.6658** | 0.8345 | ±1.6690 | **+1.996** | **0.0459** | * |
| Site: UW (vs UAB) | -1.0983 | 0.6870 | ±1.3739 | -1.599 | 0.1099 |  |
| **Age (years)** | **-0.0828** | 0.0274 | ±0.0547 | **-3.027** | **0.0025** | ** |
| BMI (kg/m2) | +0.0722 | 0.0398 | ±0.0795 | +1.815 | 0.0696 | . |
| Hypertension | -0.3801 | 0.7291 | ±1.4581 | -0.521 | 0.6022 |  |
| High cholesterol | +1.1457 | 0.6212 | ±1.2424 | +1.844 | 0.0651 | . |
| Kidney disease | +1.6182 | 0.9855 | ±1.9710 | +1.642 | 0.1006 |  |
| Circulatory disease | +0.2323 | 0.6886 | ±1.3772 | +0.337 | 0.7358 |  |
| **Time 54-250, pooled (%)** | **-0.1076** | 0.0250 | ±0.0500 | **-4.309** | **1.64e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **229**, R² = **0.1981**, Adj R² = **0.1575**, F-statistic = **4.87** (p = **9.92e-07**), Residual SE = **4.395** on **217** df, AIC = **1339.6**, BIC = **1380.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19.4982** | 3.8473 | ±7.6946 | **+5.068** | **4.02e-07** | *** |
| Education: graduate level (vs college) | -0.7061 | 0.6540 | ±1.3081 | -1.080 | 0.2803 |  |
| Education: high school or below (vs college) | +1.6579 | 1.0295 | ±2.0589 | +1.610 | 0.1073 |  |
| **Site: UCSD (vs UAB)** | **+1.6432** | 0.8341 | ±1.6681 | **+1.970** | **0.0488** | * |
| Site: UW (vs UAB) | -1.1277 | 0.6862 | ±1.3725 | -1.643 | 0.1003 |  |
| **Age (years)** | **-0.0842** | 0.0273 | ±0.0547 | **-3.079** | **0.0021** | ** |
| BMI (kg/m2) | +0.0737 | 0.0399 | ±0.0797 | +1.849 | 0.0645 | . |
| Hypertension | -0.3818 | 0.7315 | ±1.4629 | -0.522 | 0.6017 |  |
| High cholesterol | +1.1373 | 0.6220 | ±1.2441 | +1.828 | 0.0675 | . |
| Kidney disease | +1.5831 | 0.9815 | ±1.9630 | +1.613 | 0.1068 |  |
| Circulatory disease | +0.2017 | 0.6927 | ±1.3854 | +0.291 | 0.7709 |  |
| **Avg. daily time 54-250 (%)** | **-0.1154** | 0.0317 | ±0.0635 | **-3.635** | **2.78e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **229**, R² = **0.1627**, Adj R² = **0.1203**, F-statistic = **3.83** (p = **4.67e-05**), Residual SE = **4.491** on **217** df, AIC = **1349.5**, BIC = **1390.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4570** | 2.5522 | ±5.1044 | **+3.314** | **9.21e-04** | *** |
| Education: graduate level (vs college) | -0.8321 | 0.6552 | ±1.3105 | -1.270 | 0.2041 |  |
| Education: high school or below (vs college) | +1.9616 | 1.0774 | ±2.1549 | +1.821 | 0.0687 | . |
| Site: UCSD (vs UAB) | +1.5709 | 0.8639 | ±1.7278 | +1.818 | 0.0690 | . |
| Site: UW (vs UAB) | -1.3262 | 0.6916 | ±1.3831 | -1.918 | 0.0551 | . |
| **Age (years)** | **-0.0857** | 0.0283 | ±0.0566 | **-3.030** | **0.0024** | ** |
| BMI (kg/m2) | +0.0680 | 0.0399 | ±0.0799 | +1.703 | 0.0887 | . |
| Hypertension | -0.2971 | 0.7531 | ±1.5063 | -0.394 | 0.6933 |  |
| High cholesterol | +1.0079 | 0.6430 | ±1.2859 | +1.568 | 0.1170 |  |
| Kidney disease | +1.7086 | 0.9995 | ±1.9990 | +1.709 | 0.0874 | . |
| Circulatory disease | +0.3574 | 0.7060 | ±1.4120 | +0.506 | 0.6127 |  |
| Time 181-250, pooled (%) | +0.0176 | 0.0252 | ±0.0505 | +0.697 | 0.4859 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **229**, R² = **0.1642**, Adj R² = **0.1219**, F-statistic = **3.88** (p = **3.99e-05**), Residual SE = **4.487** on **217** df, AIC = **1349.1**, BIC = **1390.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.3909** | 2.5497 | ±5.0994 | **+3.291** | **9.99e-04** | *** |
| Education: graduate level (vs college) | -0.8223 | 0.6549 | ±1.3098 | -1.256 | 0.2092 |  |
| Education: high school or below (vs college) | +1.9464 | 1.0756 | ±2.1512 | +1.810 | 0.0704 | . |
| Site: UCSD (vs UAB) | +1.5791 | 0.8617 | ±1.7234 | +1.833 | 0.0669 | . |
| Site: UW (vs UAB) | -1.3107 | 0.6918 | ±1.3836 | -1.895 | 0.0582 | . |
| **Age (years)** | **-0.0857** | 0.0282 | ±0.0565 | **-3.037** | **0.0024** | ** |
| BMI (kg/m2) | +0.0682 | 0.0399 | ±0.0799 | +1.708 | 0.0876 | . |
| Hypertension | -0.2906 | 0.7518 | ±1.5036 | -0.387 | 0.6991 |  |
| High cholesterol | +1.0011 | 0.6420 | ±1.2839 | +1.559 | 0.1189 |  |
| Kidney disease | +1.6774 | 1.0022 | ±2.0045 | +1.674 | 0.0942 | . |
| Circulatory disease | +0.3544 | 0.7049 | ±1.4099 | +0.503 | 0.6152 |  |
| Avg. daily time 181-250 (%) | +0.0229 | 0.0251 | ±0.0501 | +0.914 | 0.3609 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **229**, R² = **0.1775**, Adj R² = **0.1358**, F-statistic = **4.26** (p = **9.73e-06**), Residual SE = **4.452** on **217** df, AIC = **1345.5**, BIC = **1386.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.1620** | 2.5367 | ±5.0734 | **+3.218** | **0.0013** | ** |
| Education: graduate level (vs college) | -0.7521 | 0.6567 | ±1.3135 | -1.145 | 0.2521 |  |
| Education: high school or below (vs college) | +1.8283 | 1.0591 | ±2.1183 | +1.726 | 0.0843 | . |
| Site: UCSD (vs UAB) | +1.5894 | 0.8500 | ±1.7000 | +1.870 | 0.0615 | . |
| Site: UW (vs UAB) | -1.2525 | 0.6932 | ±1.3863 | -1.807 | 0.0708 | . |
| **Age (years)** | **-0.0867** | 0.0281 | ±0.0561 | **-3.087** | **0.0020** | ** |
| BMI (kg/m2) | +0.0700 | 0.0397 | ±0.0794 | +1.763 | 0.0779 | . |
| Hypertension | -0.3113 | 0.7430 | ±1.4861 | -0.419 | 0.6753 |  |
| High cholesterol | +1.0203 | 0.6335 | ±1.2669 | +1.611 | 0.1072 |  |
| Kidney disease | +1.5538 | 1.0108 | ±2.0216 | +1.537 | 0.1242 |  |
| Circulatory disease | +0.3026 | 0.6947 | ±1.3894 | +0.436 | 0.6631 |  |
| **Time > 180 (%)** | **+0.0345** | 0.0169 | ±0.0337 | **+2.048** | **0.0406** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **229**, R² = **0.1771**, Adj R² = **0.1354**, F-statistic = **4.25** (p = **1.02e-05**), Residual SE = **4.453** on **217** df, AIC = **1345.6**, BIC = **1386.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.1383** | 2.5369 | ±5.0737 | **+3.208** | **0.0013** | ** |
| Education: graduate level (vs college) | -0.7567 | 0.6559 | ±1.3118 | -1.154 | 0.2487 |  |
| Education: high school or below (vs college) | +1.8158 | 1.0584 | ±2.1168 | +1.716 | 0.0862 | . |
| Site: UCSD (vs UAB) | +1.5952 | 0.8495 | ±1.6991 | +1.878 | 0.0604 | . |
| Site: UW (vs UAB) | -1.2455 | 0.6938 | ±1.3877 | -1.795 | 0.0726 | . |
| **Age (years)** | **-0.0863** | 0.0280 | ±0.0560 | **-3.082** | **0.0021** | ** |
| BMI (kg/m2) | +0.0704 | 0.0398 | ±0.0796 | +1.770 | 0.0767 | . |
| Hypertension | -0.3052 | 0.7432 | ±1.4864 | -0.411 | 0.6814 |  |
| High cholesterol | +1.0145 | 0.6333 | ±1.2665 | +1.602 | 0.1092 |  |
| Kidney disease | +1.5487 | 1.0078 | ±2.0157 | +1.537 | 0.1244 |  |
| Circulatory disease | +0.2998 | 0.6953 | ±1.3906 | +0.431 | 0.6663 |  |
| **Avg. daily time > 180 (%)** | **+0.0342** | 0.0169 | ±0.0338 | **+2.024** | **0.0430** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **229**, R² = **0.1978**, Adj R² = **0.1571**, F-statistic = **4.86** (p = **1.03e-06**), Residual SE = **4.396** on **217** df, AIC = **1339.8**, BIC = **1381.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.0492** | 2.5434 | ±5.0869 | **+3.165** | **0.0016** | ** |
| Education: graduate level (vs college) | -0.7306 | 0.6481 | ±1.2963 | -1.127 | 0.2596 |  |
| Education: high school or below (vs college) | +1.8377 | 1.0384 | ±2.0768 | +1.770 | 0.0768 | . |
| **Site: UCSD (vs UAB)** | **+1.6320** | 0.8271 | ±1.6543 | **+1.973** | **0.0485** | * |
| Site: UW (vs UAB) | -1.2073 | 0.6881 | ±1.3762 | -1.755 | 0.0793 | . |
| **Age (years)** | **-0.0835** | 0.0279 | ±0.0558 | **-2.992** | **0.0028** | ** |
| BMI (kg/m2) | +0.0688 | 0.0397 | ±0.0793 | +1.735 | 0.0827 | . |
| Hypertension | -0.3931 | 0.7368 | ±1.4737 | -0.534 | 0.5937 |  |
| High cholesterol | +0.9560 | 0.6223 | ±1.2446 | +1.536 | 0.1245 |  |
| Kidney disease | +1.6711 | 0.9933 | ±1.9867 | +1.682 | 0.0925 | . |
| Circulatory disease | +0.2162 | 0.6913 | ±1.3825 | +0.313 | 0.7545 |  |
| **Nocturnal time > 180 (%)** | **+0.0515** | 0.0151 | ±0.0303 | **+3.402** | **6.69e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **229**, R² = **0.1757**, Adj R² = **0.1339**, F-statistic = **4.21** (p = **1.18e-05**), Residual SE = **4.456** on **217** df, AIC = **1346.0**, BIC = **1387.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.1806** | 2.5366 | ±5.0733 | **+3.225** | **0.0013** | ** |
| Education: graduate level (vs college) | -0.7202 | 0.6482 | ±1.2964 | -1.111 | 0.2665 |  |
| Education: high school or below (vs college) | +1.8679 | 1.0641 | ±2.1282 | +1.755 | 0.0792 | . |
| Site: UCSD (vs UAB) | +1.5718 | 0.8630 | ±1.7259 | +1.821 | 0.0685 | . |
| **Site: UW (vs UAB)** | **-1.4349** | 0.6918 | ±1.3836 | **-2.074** | **0.0381** | * |
| **Age (years)** | **-0.0928** | 0.0280 | ±0.0561 | **-3.310** | **9.34e-04** | *** |
| BMI (kg/m2) | +0.0769 | 0.0398 | ±0.0796 | +1.932 | 0.0533 | . |
| Hypertension | -0.3357 | 0.7433 | ±1.4867 | -0.452 | 0.6515 |  |
| High cholesterol | +1.0632 | 0.6378 | ±1.2757 | +1.667 | 0.0955 | . |
| Kidney disease | +1.4865 | 1.0102 | ±2.0205 | +1.471 | 0.1412 |  |
| Circulatory disease | +0.3458 | 0.6960 | ±1.3919 | +0.497 | 0.6193 |  |
| Any reading > 250 during wear (0/1) | +1.2309 | 0.6483 | ±1.2967 | +1.899 | 0.0576 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **229**, R² = **0.2024**, Adj R² = **0.1620**, F-statistic = **5.01** (p = **6.08e-07**), Residual SE = **4.384** on **217** df, AIC = **1338.4**, BIC = **1379.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.9008** | 2.5006 | ±5.0012 | **+3.160** | **0.0016** | ** |
| Education: graduate level (vs college) | -0.7209 | 0.6532 | ±1.3064 | -1.104 | 0.2697 |  |
| Education: high school or below (vs college) | +1.6819 | 1.0254 | ±2.0509 | +1.640 | 0.1010 |  |
| **Site: UCSD (vs UAB)** | **+1.6418** | 0.8345 | ±1.6690 | **+1.967** | **0.0491** | * |
| Site: UW (vs UAB) | -1.1232 | 0.6859 | ±1.3719 | -1.637 | 0.1015 |  |
| **Age (years)** | **-0.0825** | 0.0273 | ±0.0547 | **-3.018** | **0.0025** | ** |
| BMI (kg/m2) | +0.0725 | 0.0396 | ±0.0792 | +1.829 | 0.0675 | . |
| Hypertension | -0.3772 | 0.7284 | ±1.4567 | -0.518 | 0.6046 |  |
| High cholesterol | +1.1522 | 0.6202 | ±1.2405 | +1.858 | 0.0632 | . |
| Kidney disease | +1.6073 | 0.9846 | ±1.9692 | +1.632 | 0.1026 |  |
| Circulatory disease | +0.2469 | 0.6849 | ±1.3698 | +0.360 | 0.7185 |  |
| **Time > 250 (%)** | **+0.1105** | 0.0254 | ±0.0509 | **+4.346** | **1.38e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **229**, R² = **0.1995**, Adj R² = **0.1590**, F-statistic = **4.92** (p = **8.44e-07**), Residual SE = **4.392** on **217** df, AIC = **1339.2**, BIC = **1380.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.9521** | 2.4986 | ±4.9972 | **+3.183** | **0.0015** | ** |
| Education: graduate level (vs college) | -0.7175 | 0.6536 | ±1.3072 | -1.098 | 0.2723 |  |
| Education: high school or below (vs college) | +1.6323 | 1.0284 | ±2.0568 | +1.587 | 0.1125 |  |
| Site: UCSD (vs UAB) | +1.6204 | 0.8343 | ±1.6687 | +1.942 | 0.0521 | . |
| Site: UW (vs UAB) | -1.1484 | 0.6858 | ±1.3716 | -1.675 | 0.0940 | . |
| **Age (years)** | **-0.0835** | 0.0273 | ±0.0546 | **-3.057** | **0.0022** | ** |
| BMI (kg/m2) | +0.0739 | 0.0397 | ±0.0794 | +1.862 | 0.0626 | . |
| Hypertension | -0.3818 | 0.7306 | ±1.4612 | -0.523 | 0.6013 |  |
| High cholesterol | +1.1356 | 0.6211 | ±1.2422 | +1.828 | 0.0675 | . |
| Kidney disease | +1.5779 | 0.9806 | ±1.9612 | +1.609 | 0.1076 |  |
| Circulatory disease | +0.2162 | 0.6893 | ±1.3785 | +0.314 | 0.7538 |  |
| **Avg. daily time > 250 (%)** | **+0.1189** | 0.0328 | ±0.0657 | **+3.618** | **2.97e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 229; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1019**, LLR χ² = **25.95** (p = **0.0038**), AUC = **0.7113**, AIC = **250.8**, BIC = **288.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0527 | 1.3876 | ±2.7753 | -0.759 | 0.4481 | 0.3490 |  |
| Education: graduate level (vs college) | -0.3714 | 0.4181 | ±0.8361 | -0.888 | 0.3744 | 0.6898 |  |
| Education: high school or below (vs college) | +0.6189 | 0.4473 | ±0.8947 | +1.383 | 0.1665 | 1.8568 |  |
| Site: UCSD (vs UAB) | +0.7697 | 0.3940 | ±0.7880 | +1.953 | 0.0508 | 2.1590 | . |
| Site: UW (vs UAB) | -0.6204 | 0.4810 | ±0.9620 | -1.290 | 0.1971 | 0.5377 |  |
| Age (years) | -0.0288 | 0.0177 | ±0.0354 | -1.629 | 0.1033 | 0.9716 |  |
| BMI (kg/m2) | +0.0287 | 0.0207 | ±0.0415 | +1.383 | 0.1666 | 1.0291 |  |
| Hypertension | +0.0053 | 0.4048 | ±0.8096 | +0.013 | 0.9895 | 1.0053 |  |
| High cholesterol | +0.4538 | 0.3579 | ±0.7159 | +1.268 | 0.2049 | 1.5743 |  |
| **Kidney disease** | **+1.0962** | 0.4280 | ±0.8560 | **+2.561** | **0.0104** | 2.9929 | * |
| Circulatory disease | +0.3929 | 0.3698 | ±0.7396 | +1.062 | 0.2881 | 1.4813 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1304**, LLR χ² = **33.23** (p = **4.82e-04**), AUC = **0.7395**, AIC = **245.5**, BIC = **286.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2440** | 1.6445 | ±3.2890 | **-1.973** | **0.0485** | 0.0390 | * |
| Education: graduate level (vs college) | -0.2963 | 0.4286 | ±0.8572 | -0.691 | 0.4894 | 0.7436 |  |
| Education: high school or below (vs college) | +0.4953 | 0.4660 | ±0.9321 | +1.063 | 0.2879 | 1.6410 |  |
| **Site: UCSD (vs UAB)** | **+0.8043** | 0.4025 | ±0.8051 | **+1.998** | **0.0457** | 2.2350 | * |
| Site: UW (vs UAB) | -0.5178 | 0.4851 | ±0.9703 | -1.067 | 0.2858 | 0.5958 |  |
| Age (years) | -0.0329 | 0.0178 | ±0.0357 | -1.844 | 0.0652 | 0.9676 | . |
| BMI (kg/m2) | +0.0280 | 0.0211 | ±0.0421 | +1.329 | 0.1837 | 1.0284 |  |
| Hypertension | -0.1194 | 0.4126 | ±0.8252 | -0.289 | 0.7723 | 0.8874 |  |
| High cholesterol | +0.5180 | 0.3686 | ±0.7372 | +1.405 | 0.1599 | 1.6787 |  |
| **Kidney disease** | **+1.1214** | 0.4402 | ±0.8804 | **+2.547** | **0.0109** | 3.0693 | * |
| Circulatory disease | +0.3772 | 0.3774 | ±0.7549 | +0.999 | 0.3176 | 1.4582 |  |
| **HbA1c (%)** | **+0.3802** | 0.1426 | ±0.2851 | **+2.667** | **0.0076** | 1.4626 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1390**, LLR χ² = **35.41** (p = **2.12e-04**), AUC = **0.7382**, AIC = **243.4**, BIC = **284.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2165** | 1.5976 | ±3.1953 | **-2.013** | **0.0441** | 0.0401 | * |
| Education: graduate level (vs college) | -0.3721 | 0.4286 | ±0.8572 | -0.868 | 0.3853 | 0.6893 |  |
| Education: high school or below (vs college) | +0.5114 | 0.4674 | ±0.9347 | +1.094 | 0.2739 | 1.6676 |  |
| Site: UCSD (vs UAB) | +0.7849 | 0.4058 | ±0.8117 | +1.934 | 0.0531 | 2.1922 | . |
| Site: UW (vs UAB) | -0.5805 | 0.4907 | ±0.9814 | -1.183 | 0.2368 | 0.5596 |  |
| Age (years) | -0.0282 | 0.0180 | ±0.0359 | -1.569 | 0.1165 | 0.9722 |  |
| BMI (kg/m2) | +0.0306 | 0.0212 | ±0.0423 | +1.446 | 0.1481 | 1.0311 |  |
| Hypertension | -0.0819 | 0.4168 | ±0.8337 | -0.196 | 0.8442 | 0.9214 |  |
| High cholesterol | +0.5461 | 0.3745 | ±0.7490 | +1.458 | 0.1448 | 1.7264 |  |
| **Kidney disease** | **+1.0328** | 0.4374 | ±0.8747 | **+2.362** | **0.0182** | 2.8090 | * |
| Circulatory disease | +0.3150 | 0.3838 | ±0.7676 | +0.821 | 0.4118 | 1.3703 |  |
| **Mean glucose (mg/dL)** | **+0.0151** | 0.0050 | ±0.0101 | **+2.998** | **0.0027** | 1.0152 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1390**, LLR χ² = **35.41** (p = **2.12e-04**), AUC = **0.7382**, AIC = **243.4**, BIC = **284.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-5.3088** | 2.0129 | ±4.0258 | **-2.637** | **0.0084** | 0.0049 | ** |
| Education: graduate level (vs college) | -0.3721 | 0.4286 | ±0.8572 | -0.868 | 0.3853 | 0.6893 |  |
| Education: high school or below (vs college) | +0.5114 | 0.4674 | ±0.9347 | +1.094 | 0.2739 | 1.6676 |  |
| Site: UCSD (vs UAB) | +0.7849 | 0.4058 | ±0.8117 | +1.934 | 0.0531 | 2.1922 | . |
| Site: UW (vs UAB) | -0.5805 | 0.4907 | ±0.9814 | -1.183 | 0.2368 | 0.5596 |  |
| Age (years) | -0.0282 | 0.0180 | ±0.0359 | -1.569 | 0.1165 | 0.9722 |  |
| BMI (kg/m2) | +0.0306 | 0.0212 | ±0.0423 | +1.446 | 0.1481 | 1.0311 |  |
| Hypertension | -0.0819 | 0.4168 | ±0.8337 | -0.196 | 0.8442 | 0.9214 |  |
| High cholesterol | +0.5461 | 0.3745 | ±0.7490 | +1.458 | 0.1448 | 1.7264 |  |
| **Kidney disease** | **+1.0328** | 0.4374 | ±0.8747 | **+2.362** | **0.0182** | 2.8090 | * |
| Circulatory disease | +0.3150 | 0.3838 | ±0.7676 | +0.821 | 0.4118 | 1.3703 |  |
| **GMI (%)** | **+0.6321** | 0.2108 | ±0.4216 | **+2.998** | **0.0027** | 1.8816 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1629**, LLR χ² = **41.49** (p = **1.98e-05**), AUC = **0.7615**, AIC = **237.3**, BIC = **278.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.8587** | 1.6330 | ±3.2661 | **-2.363** | **0.0181** | 0.0211 | * |
| Education: graduate level (vs college) | -0.4085 | 0.4337 | ±0.8674 | -0.942 | 0.3462 | 0.6646 |  |
| Education: high school or below (vs college) | +0.5132 | 0.4734 | ±0.9469 | +1.084 | 0.2784 | 1.6706 |  |
| **Site: UCSD (vs UAB)** | **+0.8302** | 0.4145 | ±0.8291 | **+2.003** | **0.0452** | 2.2937 | * |
| Site: UW (vs UAB) | -0.5962 | 0.4980 | ±0.9959 | -1.197 | 0.2312 | 0.5509 |  |
| Age (years) | -0.0259 | 0.0183 | ±0.0366 | -1.414 | 0.1574 | 0.9744 |  |
| BMI (kg/m2) | +0.0308 | 0.0215 | ±0.0429 | +1.436 | 0.1511 | 1.0313 |  |
| Hypertension | -0.1182 | 0.4232 | ±0.8465 | -0.279 | 0.7801 | 0.8886 |  |
| High cholesterol | +0.5167 | 0.3812 | ±0.7624 | +1.355 | 0.1753 | 1.6764 |  |
| **Kidney disease** | **+1.1547** | 0.4445 | ±0.8889 | **+2.598** | **0.0094** | 3.1732 | ** |
| Circulatory disease | +0.3020 | 0.3923 | ±0.7846 | +0.770 | 0.4414 | 1.3526 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0195** | 0.0053 | ±0.0106 | **+3.690** | **2.25e-04** | 1.0197 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1391**, LLR χ² = **35.43** (p = **2.11e-04**), AUC = **0.7462**, AIC = **243.3**, BIC = **284.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.9769 | 1.4589 | ±2.9178 | -1.355 | 0.1754 | 0.1385 |  |
| Education: graduate level (vs college) | -0.2938 | 0.4300 | ±0.8600 | -0.683 | 0.4944 | 0.7454 |  |
| Education: high school or below (vs college) | +0.3775 | 0.4719 | ±0.9437 | +0.800 | 0.4237 | 1.4587 |  |
| **Site: UCSD (vs UAB)** | **+0.8080** | 0.4031 | ±0.8061 | **+2.004** | **0.0450** | 2.2433 | * |
| Site: UW (vs UAB) | -0.5440 | 0.4929 | ±0.9859 | -1.104 | 0.2697 | 0.5804 |  |
| Age (years) | -0.0345 | 0.0180 | ±0.0361 | -1.912 | 0.0558 | 0.9661 | . |
| BMI (kg/m2) | +0.0329 | 0.0213 | ±0.0425 | +1.550 | 0.1212 | 1.0335 |  |
| Hypertension | -0.1004 | 0.4146 | ±0.8291 | -0.242 | 0.8087 | 0.9045 |  |
| High cholesterol | +0.5697 | 0.3755 | ±0.7509 | +1.517 | 0.1292 | 1.7677 |  |
| Kidney disease | +0.8246 | 0.4465 | ±0.8931 | +1.847 | 0.0648 | 2.2809 | . |
| Circulatory disease | +0.4153 | 0.3788 | ±0.7575 | +1.096 | 0.2729 | 1.5148 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0327** | 0.0109 | ±0.0217 | **+3.005** | **0.0027** | 1.0332 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1263**, LLR χ² = **32.19** (p = **7.12e-04**), AUC = **0.7347**, AIC = **246.6**, BIC = **287.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.8262 | 1.4517 | ±2.9034 | -1.258 | 0.2084 | 0.1610 |  |
| Education: graduate level (vs college) | -0.3008 | 0.4263 | ±0.8526 | -0.706 | 0.4804 | 0.7402 |  |
| Education: high school or below (vs college) | +0.3857 | 0.4695 | ±0.9390 | +0.821 | 0.4114 | 1.4706 |  |
| **Site: UCSD (vs UAB)** | **+0.7975** | 0.4001 | ±0.8002 | **+1.993** | **0.0462** | 2.2200 | * |
| Site: UW (vs UAB) | -0.5679 | 0.4889 | ±0.9777 | -1.162 | 0.2453 | 0.5667 |  |
| Age (years) | -0.0337 | 0.0180 | ±0.0361 | -1.869 | 0.0616 | 0.9668 | . |
| BMI (kg/m2) | +0.0325 | 0.0211 | ±0.0422 | +1.542 | 0.1232 | 1.0330 |  |
| Hypertension | -0.0539 | 0.4109 | ±0.8218 | -0.131 | 0.8957 | 0.9475 |  |
| High cholesterol | +0.5397 | 0.3704 | ±0.7408 | +1.457 | 0.1451 | 1.7155 |  |
| Kidney disease | +0.8615 | 0.4442 | ±0.8885 | +1.939 | 0.0525 | 2.3668 | . |
| Circulatory disease | +0.4330 | 0.3751 | ±0.7501 | +1.155 | 0.2483 | 1.5419 |  |
| **Avg. daily SD (mg/dL)** | **+0.0310** | 0.0126 | ±0.0252 | **+2.465** | **0.0137** | 1.0315 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1162**, LLR χ² = **29.61** (p = **0.0018**), AUC = **0.7335**, AIC = **249.2**, BIC = **290.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.9075 | 1.4788 | ±2.9576 | -1.290 | 0.1971 | 0.1485 |  |
| Education: graduate level (vs college) | -0.3012 | 0.4254 | ±0.8508 | -0.708 | 0.4790 | 0.7400 |  |
| Education: high school or below (vs college) | +0.4291 | 0.4628 | ±0.9255 | +0.927 | 0.3537 | 1.5359 |  |
| **Site: UCSD (vs UAB)** | **+0.7899** | 0.3959 | ±0.7918 | **+1.995** | **0.0460** | 2.2031 | * |
| Site: UW (vs UAB) | -0.5721 | 0.4875 | ±0.9750 | -1.174 | 0.2406 | 0.5644 |  |
| **Age (years)** | **-0.0358** | 0.0182 | ±0.0363 | **-1.971** | **0.0487** | 0.9648 | * |
| BMI (kg/m2) | +0.0317 | 0.0210 | ±0.0420 | +1.509 | 0.1312 | 1.0322 |  |
| Hypertension | -0.0452 | 0.4068 | ±0.8135 | -0.111 | 0.9115 | 0.9558 |  |
| High cholesterol | +0.5065 | 0.3653 | ±0.7306 | +1.387 | 0.1656 | 1.6594 |  |
| Kidney disease | +0.8584 | 0.4489 | ±0.8979 | +1.912 | 0.0559 | 2.3594 | . |
| Circulatory disease | +0.4294 | 0.3732 | ±0.7463 | +1.151 | 0.2498 | 1.5364 |  |
| CV (%) | +0.0486 | 0.0254 | ±0.0508 | +1.912 | 0.0558 | 1.0498 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1143**, LLR χ² = **29.12** (p = **0.0022**), AUC = **0.7286**, AIC = **249.6**, BIC = **290.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.4393 | 1.6299 | ±3.2597 | +0.270 | 0.7875 | 1.5516 |  |
| Education: graduate level (vs college) | -0.3197 | 0.4252 | ±0.8505 | -0.752 | 0.4522 | 0.7264 |  |
| Education: high school or below (vs college) | +0.4325 | 0.4613 | ±0.9227 | +0.937 | 0.3485 | 1.5411 |  |
| Site: UCSD (vs UAB) | +0.7706 | 0.3957 | ±0.7915 | +1.947 | 0.0515 | 2.1612 | . |
| Site: UW (vs UAB) | -0.5951 | 0.4851 | ±0.9702 | -1.227 | 0.2199 | 0.5515 |  |
| **Age (years)** | **-0.0364** | 0.0183 | ±0.0366 | **-1.989** | **0.0467** | 0.9642 | * |
| BMI (kg/m2) | +0.0304 | 0.0209 | ±0.0418 | +1.453 | 0.1461 | 1.0308 |  |
| Hypertension | -0.0231 | 0.4058 | ±0.8116 | -0.057 | 0.9546 | 0.9772 |  |
| High cholesterol | +0.5063 | 0.3650 | ±0.7299 | +1.387 | 0.1654 | 1.6592 |  |
| **Kidney disease** | **+0.9393** | 0.4423 | ±0.8847 | **+2.123** | **0.0337** | 2.5582 | * |
| Circulatory disease | +0.3892 | 0.3724 | ±0.7449 | +1.045 | 0.2960 | 1.4759 |  |
| Mean / SD ratio | -0.2424 | 0.1405 | ±0.2810 | -1.725 | 0.0845 | 0.7848 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1039**, LLR χ² = **26.47** (p = **0.0055**), AUC = **0.7158**, AIC = **252.3**, BIC = **293.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4735 | 1.6044 | ±3.2088 | -0.295 | 0.7679 | 0.6228 |  |
| Education: graduate level (vs college) | -0.3438 | 0.4213 | ±0.8425 | -0.816 | 0.4145 | 0.7091 |  |
| Education: high school or below (vs college) | +0.5423 | 0.4598 | ±0.9197 | +1.179 | 0.2383 | 1.7199 |  |
| Site: UCSD (vs UAB) | +0.7620 | 0.3942 | ±0.7885 | +1.933 | 0.0533 | 2.1425 | . |
| Site: UW (vs UAB) | -0.6163 | 0.4815 | ±0.9630 | -1.280 | 0.2005 | 0.5399 |  |
| Age (years) | -0.0321 | 0.0183 | ±0.0366 | -1.754 | 0.0795 | 0.9684 | . |
| BMI (kg/m2) | +0.0294 | 0.0208 | ±0.0415 | +1.414 | 0.1575 | 1.0298 |  |
| Hypertension | +0.0109 | 0.4048 | ±0.8097 | +0.027 | 0.9786 | 1.0109 |  |
| High cholesterol | +0.4681 | 0.3601 | ±0.7201 | +1.300 | 0.1936 | 1.5969 |  |
| **Kidney disease** | **+1.0475** | 0.4340 | ±0.8679 | **+2.414** | **0.0158** | 2.8506 | * |
| Circulatory disease | +0.3964 | 0.3702 | ±0.7404 | +1.071 | 0.2842 | 1.4865 |  |
| Avg. daily mean/SD | -0.0773 | 0.1085 | ±0.2170 | -0.712 | 0.4763 | 0.9256 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1077**, LLR χ² = **27.44** (p = **0.0039**), AUC = **0.7159**, AIC = **251.3**, BIC = **292.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.7253 | 1.5019 | ±3.0038 | -1.149 | 0.2507 | 0.1781 |  |
| Education: graduate level (vs college) | -0.3449 | 0.4217 | ±0.8433 | -0.818 | 0.4133 | 0.7083 |  |
| Education: high school or below (vs college) | +0.4852 | 0.4637 | ±0.9274 | +1.046 | 0.2954 | 1.6246 |  |
| Site: UCSD (vs UAB) | +0.7440 | 0.3959 | ±0.7918 | +1.879 | 0.0602 | 2.1044 | . |
| Site: UW (vs UAB) | -0.5773 | 0.4833 | ±0.9667 | -1.194 | 0.2323 | 0.5614 |  |
| Age (years) | -0.0301 | 0.0178 | ±0.0357 | -1.688 | 0.0915 | 0.9703 | . |
| BMI (kg/m2) | +0.0264 | 0.0209 | ±0.0418 | +1.263 | 0.2065 | 1.0267 |  |
| Hypertension | +0.0284 | 0.4075 | ±0.8151 | +0.070 | 0.9444 | 1.0288 |  |
| High cholesterol | +0.4611 | 0.3605 | ±0.7209 | +1.279 | 0.2008 | 1.5858 |  |
| **Kidney disease** | **+1.0989** | 0.4314 | ±0.8629 | **+2.547** | **0.0109** | 3.0007 | * |
| Circulatory disease | +0.3839 | 0.3727 | ±0.7455 | +1.030 | 0.3030 | 1.4681 |  |
| MAG (mg/dL/h) | +0.0181 | 0.0147 | ±0.0295 | +1.225 | 0.2207 | 1.0182 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1229**, LLR χ² = **31.32** (p = **9.80e-04**), AUC = **0.7365**, AIC = **247.4**, BIC = **288.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.0340 | 1.4812 | ±2.9624 | -1.373 | 0.1697 | 0.1308 |  |
| Education: graduate level (vs college) | -0.2901 | 0.4260 | ±0.8520 | -0.681 | 0.4959 | 0.7482 |  |
| Education: high school or below (vs college) | +0.3647 | 0.4717 | ±0.9434 | +0.773 | 0.4394 | 1.4401 |  |
| **Site: UCSD (vs UAB)** | **+0.7942** | 0.3992 | ±0.7984 | **+1.990** | **0.0466** | 2.2127 | * |
| Site: UW (vs UAB) | -0.5886 | 0.4881 | ±0.9762 | -1.206 | 0.2278 | 0.5551 |  |
| Age (years) | -0.0335 | 0.0181 | ±0.0362 | -1.851 | 0.0641 | 0.9670 | . |
| BMI (kg/m2) | +0.0326 | 0.0210 | ±0.0421 | +1.550 | 0.1210 | 1.0332 |  |
| Hypertension | -0.0160 | 0.4105 | ±0.8209 | -0.039 | 0.9689 | 0.9841 |  |
| High cholesterol | +0.5198 | 0.3687 | ±0.7373 | +1.410 | 0.1585 | 1.6817 |  |
| **Kidney disease** | **+0.8738** | 0.4454 | ±0.8908 | **+1.962** | **0.0498** | 2.3960 | * |
| Circulatory disease | +0.3927 | 0.3753 | ±0.7506 | +1.046 | 0.2954 | 1.4810 |  |
| **Avg. daily range (mg/dL)** | **+0.0082** | 0.0036 | ±0.0072 | **+2.299** | **0.0215** | 1.0083 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1586**, LLR χ² = **40.41** (p = **3.05e-05**), AUC = **0.7689**, AIC = **238.4**, BIC = **279.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6953 | 1.4428 | ±2.8857 | -1.175 | 0.2400 | 0.1835 |  |
| Education: graduate level (vs college) | -0.2694 | 0.4345 | ±0.8690 | -0.620 | 0.5352 | 0.7638 |  |
| Education: high school or below (vs college) | +0.5561 | 0.4721 | ±0.9441 | +1.178 | 0.2388 | 1.7438 |  |
| Site: UCSD (vs UAB) | +0.8017 | 0.4104 | ±0.8209 | +1.953 | 0.0508 | 2.2294 | . |
| Site: UW (vs UAB) | -0.5437 | 0.4974 | ±0.9947 | -1.093 | 0.2743 | 0.5806 |  |
| Age (years) | -0.0329 | 0.0180 | ±0.0359 | -1.829 | 0.0674 | 0.9677 | . |
| BMI (kg/m2) | +0.0324 | 0.0216 | ±0.0432 | +1.500 | 0.1336 | 1.0329 |  |
| Hypertension | -0.2233 | 0.4204 | ±0.8407 | -0.531 | 0.5952 | 0.7999 |  |
| High cholesterol | +0.5579 | 0.3787 | ±0.7575 | +1.473 | 0.1407 | 1.7471 |  |
| **Kidney disease** | **+0.9024** | 0.4505 | ±0.9010 | **+2.003** | **0.0452** | 2.4654 | * |
| Circulatory disease | +0.2966 | 0.3899 | ±0.7797 | +0.761 | 0.4468 | 1.3453 |  |
| **SD of daily means (mg/dL)** | **+0.0653** | 0.0183 | ±0.0365 | **+3.576** | **3.49e-04** | 1.0675 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1425**, LLR χ² = **36.31** (p = **1.50e-04**), AUC = **0.7467**, AIC = **242.5**, BIC = **283.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.1832 | 1.5965 | ±3.1929 | +0.741 | 0.4586 | 3.2648 |  |
| Education: graduate level (vs college) | -0.2844 | 0.4319 | ±0.8637 | -0.659 | 0.5102 | 0.7525 |  |
| Education: high school or below (vs college) | +0.5080 | 0.4671 | ±0.9342 | +1.088 | 0.2768 | 1.6620 |  |
| **Site: UCSD (vs UAB)** | **+0.8182** | 0.4077 | ±0.8153 | **+2.007** | **0.0447** | 2.2665 | * |
| Site: UW (vs UAB) | -0.5359 | 0.4908 | ±0.9816 | -1.092 | 0.2749 | 0.5851 |  |
| Age (years) | -0.0303 | 0.0180 | ±0.0359 | -1.689 | 0.0911 | 0.9701 | . |
| BMI (kg/m2) | +0.0319 | 0.0214 | ±0.0427 | +1.494 | 0.1353 | 1.0324 |  |
| Hypertension | -0.0509 | 0.4161 | ±0.8323 | -0.122 | 0.9026 | 0.9504 |  |
| High cholesterol | +0.4982 | 0.3731 | ±0.7463 | +1.335 | 0.1818 | 1.6458 |  |
| **Kidney disease** | **+0.9482** | 0.4402 | ±0.8805 | **+2.154** | **0.0313** | 2.5811 | * |
| Circulatory disease | +0.3264 | 0.3824 | ±0.7648 | +0.854 | 0.3933 | 1.3860 |  |
| **Time in range 70-180, pooled (%)** | **-0.0273** | 0.0086 | ±0.0173 | **-3.162** | **0.0016** | 0.9730 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1419**, LLR χ² = **36.16** (p = **1.59e-04**), AUC = **0.7469**, AIC = **242.6**, BIC = **283.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.1630 | 1.5938 | ±3.1876 | +0.730 | 0.4656 | 3.1994 |  |
| Education: graduate level (vs college) | -0.2858 | 0.4318 | ±0.8637 | -0.662 | 0.5080 | 0.7514 |  |
| Education: high school or below (vs college) | +0.4930 | 0.4674 | ±0.9348 | +1.055 | 0.2915 | 1.6372 |  |
| **Site: UCSD (vs UAB)** | **+0.8191** | 0.4076 | ±0.8152 | **+2.010** | **0.0445** | 2.2685 | * |
| Site: UW (vs UAB) | -0.5280 | 0.4904 | ±0.9808 | -1.077 | 0.2816 | 0.5898 |  |
| Age (years) | -0.0304 | 0.0180 | ±0.0359 | -1.692 | 0.0906 | 0.9700 | . |
| BMI (kg/m2) | +0.0322 | 0.0214 | ±0.0427 | +1.508 | 0.1316 | 1.0327 |  |
| Hypertension | -0.0397 | 0.4159 | ±0.8319 | -0.096 | 0.9239 | 0.9611 |  |
| High cholesterol | +0.4966 | 0.3728 | ±0.7456 | +1.332 | 0.1828 | 1.6432 |  |
| **Kidney disease** | **+0.9381** | 0.4411 | ±0.8822 | **+2.127** | **0.0334** | 2.5552 | * |
| Circulatory disease | +0.3252 | 0.3823 | ±0.7646 | +0.851 | 0.3950 | 1.3843 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0271** | 0.0086 | ±0.0172 | **-3.144** | **0.0017** | 0.9733 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1042**, LLR χ² = **26.54** (p = **0.0054**), AUC = **0.7121**, AIC = **252.2**, BIC = **293.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9872 | 1.3903 | ±2.7807 | -0.710 | 0.4777 | 0.3726 |  |
| Education: graduate level (vs college) | -0.3816 | 0.4175 | ±0.8349 | -0.914 | 0.3606 | 0.6827 |  |
| Education: high school or below (vs college) | +0.5946 | 0.4492 | ±0.8983 | +1.324 | 0.1856 | 1.8123 |  |
| Site: UCSD (vs UAB) | +0.7212 | 0.3984 | ±0.7968 | +1.810 | 0.0702 | 2.0570 | . |
| Site: UW (vs UAB) | -0.6735 | 0.4856 | ±0.9713 | -1.387 | 0.1655 | 0.5099 |  |
| Age (years) | -0.0286 | 0.0177 | ±0.0355 | -1.615 | 0.1063 | 0.9718 |  |
| BMI (kg/m2) | +0.0294 | 0.0208 | ±0.0416 | +1.412 | 0.1581 | 1.0298 |  |
| Hypertension | +0.0072 | 0.4046 | ±0.8092 | +0.018 | 0.9859 | 1.0072 |  |
| High cholesterol | +0.4605 | 0.3585 | ±0.7169 | +1.285 | 0.1989 | 1.5848 |  |
| **Kidney disease** | **+1.0870** | 0.4289 | ±0.8578 | **+2.534** | **0.0113** | 2.9652 | * |
| Circulatory disease | +0.4065 | 0.3716 | ±0.7431 | +1.094 | 0.2739 | 1.5016 |  |
| Time < 54 (%) | -0.2021 | 0.2875 | ±0.5751 | -0.703 | 0.4821 | 0.8170 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1019**, LLR χ² = **25.95** (p = **0.0066**), AUC = **0.7115**, AIC = **252.8**, BIC = **294.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0539 | 1.3880 | ±2.7760 | -0.759 | 0.4477 | 0.3486 |  |
| Education: graduate level (vs college) | -0.3700 | 0.4192 | ±0.8384 | -0.883 | 0.3775 | 0.6908 |  |
| Education: high school or below (vs college) | +0.6203 | 0.4484 | ±0.8968 | +1.383 | 0.1666 | 1.8595 |  |
| Site: UCSD (vs UAB) | +0.7720 | 0.3971 | ±0.7943 | +1.944 | 0.0519 | 2.1640 | . |
| Site: UW (vs UAB) | -0.6183 | 0.4831 | ±0.9662 | -1.280 | 0.2006 | 0.5389 |  |
| Age (years) | -0.0289 | 0.0178 | ±0.0355 | -1.628 | 0.1035 | 0.9715 |  |
| BMI (kg/m2) | +0.0287 | 0.0207 | ±0.0415 | +1.383 | 0.1665 | 1.0291 |  |
| Hypertension | +0.0052 | 0.4049 | ±0.8097 | +0.013 | 0.9897 | 1.0052 |  |
| High cholesterol | +0.4544 | 0.3582 | ±0.7163 | +1.269 | 0.2046 | 1.5752 |  |
| **Kidney disease** | **+1.0964** | 0.4280 | ±0.8560 | **+2.562** | **0.0104** | 2.9933 | * |
| Circulatory disease | +0.3917 | 0.3707 | ±0.7414 | +1.057 | 0.2907 | 1.4794 |  |
| Avg. daily time < 54 (%) | +0.0094 | 0.1999 | ±0.3997 | +0.047 | 0.9624 | 1.0095 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1019**, LLR χ² = **25.96** (p = **0.0066**), AUC = **0.7100**, AIC = **252.8**, BIC = **294.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0526 | 1.3881 | ±2.7761 | -0.758 | 0.4482 | 0.3490 |  |
| Education: graduate level (vs college) | -0.3647 | 0.4225 | ±0.8450 | -0.863 | 0.3880 | 0.6944 |  |
| Education: high school or below (vs college) | +0.6179 | 0.4473 | ±0.8946 | +1.381 | 0.1672 | 1.8550 |  |
| Site: UCSD (vs UAB) | +0.7733 | 0.3954 | ±0.7908 | +1.956 | 0.0505 | 2.1670 | . |
| Site: UW (vs UAB) | -0.6201 | 0.4811 | ±0.9623 | -1.289 | 0.1974 | 0.5379 |  |
| Age (years) | -0.0291 | 0.0179 | ±0.0357 | -1.629 | 0.1032 | 0.9713 |  |
| BMI (kg/m2) | +0.0287 | 0.0207 | ±0.0415 | +1.384 | 0.1665 | 1.0291 |  |
| Hypertension | +0.0065 | 0.4049 | ±0.8099 | +0.016 | 0.9872 | 1.0065 |  |
| High cholesterol | +0.4507 | 0.3590 | ±0.7180 | +1.255 | 0.2093 | 1.5694 |  |
| **Kidney disease** | **+1.0952** | 0.4281 | ±0.8561 | **+2.558** | **0.0105** | 2.9896 | * |
| Circulatory disease | +0.3936 | 0.3697 | ±0.7394 | +1.065 | 0.2871 | 1.4822 |  |
| Time 54-69, pooled (%) | +0.0073 | 0.0661 | ±0.1322 | +0.111 | 0.9119 | 1.0073 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1022**, LLR χ² = **26.04** (p = **0.0064**), AUC = **0.7112**, AIC = **252.7**, BIC = **293.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0449 | 1.3890 | ±2.7780 | -0.752 | 0.4519 | 0.3517 |  |
| Education: graduate level (vs college) | -0.3520 | 0.4232 | ±0.8465 | -0.832 | 0.4056 | 0.7033 |  |
| Education: high school or below (vs college) | +0.6144 | 0.4474 | ±0.8949 | +1.373 | 0.1697 | 1.8486 |  |
| **Site: UCSD (vs UAB)** | **+0.7793** | 0.3953 | ±0.7907 | **+1.971** | **0.0487** | 2.1799 | * |
| Site: UW (vs UAB) | -0.6193 | 0.4814 | ±0.9628 | -1.286 | 0.1983 | 0.5383 |  |
| Age (years) | -0.0296 | 0.0179 | ±0.0358 | -1.655 | 0.0979 | 0.9708 | . |
| BMI (kg/m2) | +0.0288 | 0.0208 | ±0.0415 | +1.385 | 0.1661 | 1.0292 |  |
| Hypertension | +0.0088 | 0.4051 | ±0.8101 | +0.022 | 0.9827 | 1.0088 |  |
| High cholesterol | +0.4467 | 0.3586 | ±0.7172 | +1.246 | 0.2129 | 1.5632 |  |
| **Kidney disease** | **+1.0939** | 0.4280 | ±0.8561 | **+2.556** | **0.0106** | 2.9859 | * |
| Circulatory disease | +0.3958 | 0.3696 | ±0.7391 | +1.071 | 0.2842 | 1.4855 |  |
| Avg. daily time 54-69 (%) | +0.0193 | 0.0628 | ±0.1256 | +0.308 | 0.7582 | 1.0195 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1019**, LLR χ² = **25.96** (p = **0.0066**), AUC = **0.7120**, AIC = **252.8**, BIC = **294.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0510 | 1.3875 | ±2.7750 | -0.757 | 0.4488 | 0.3496 |  |
| Education: graduate level (vs college) | -0.3759 | 0.4214 | ±0.8428 | -0.892 | 0.3724 | 0.6867 |  |
| Education: high school or below (vs college) | +0.6188 | 0.4474 | ±0.8948 | +1.383 | 0.1667 | 1.8567 |  |
| Site: UCSD (vs UAB) | +0.7660 | 0.3963 | ±0.7926 | +1.933 | 0.0532 | 2.1512 | . |
| Site: UW (vs UAB) | -0.6220 | 0.4813 | ±0.9626 | -1.292 | 0.1962 | 0.5369 |  |
| Age (years) | -0.0287 | 0.0178 | ±0.0356 | -1.610 | 0.1073 | 0.9717 |  |
| BMI (kg/m2) | +0.0287 | 0.0207 | ±0.0415 | +1.384 | 0.1665 | 1.0291 |  |
| Hypertension | +0.0047 | 0.4049 | ±0.8098 | +0.012 | 0.9908 | 1.0047 |  |
| High cholesterol | +0.4560 | 0.3589 | ±0.7178 | +1.271 | 0.2039 | 1.5777 |  |
| **Kidney disease** | **+1.0967** | 0.4281 | ±0.8561 | **+2.562** | **0.0104** | 2.9942 | * |
| Circulatory disease | +0.3929 | 0.3700 | ±0.7399 | +1.062 | 0.2882 | 1.4813 |  |
| Time < 70 (%) | -0.0047 | 0.0558 | ±0.1117 | -0.085 | 0.9326 | 0.9953 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1021**, LLR χ² = **26.02** (p = **0.0064**), AUC = **0.7111**, AIC = **252.7**, BIC = **294.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0493 | 1.3886 | ±2.7772 | -0.756 | 0.4499 | 0.3502 |  |
| Education: graduate level (vs college) | -0.3559 | 0.4226 | ±0.8453 | -0.842 | 0.3997 | 0.7005 |  |
| Education: high school or below (vs college) | +0.6180 | 0.4473 | ±0.8945 | +1.382 | 0.1671 | 1.8551 |  |
| **Site: UCSD (vs UAB)** | **+0.7797** | 0.3960 | ±0.7921 | **+1.969** | **0.0490** | 2.1809 | * |
| Site: UW (vs UAB) | -0.6165 | 0.4815 | ±0.9631 | -1.280 | 0.2005 | 0.5398 |  |
| Age (years) | -0.0295 | 0.0179 | ±0.0358 | -1.648 | 0.0993 | 0.9709 | . |
| BMI (kg/m2) | +0.0287 | 0.0208 | ±0.0415 | +1.385 | 0.1662 | 1.0292 |  |
| Hypertension | +0.0075 | 0.4050 | ±0.8100 | +0.019 | 0.9852 | 1.0075 |  |
| High cholesterol | +0.4497 | 0.3583 | ±0.7165 | +1.255 | 0.2094 | 1.5678 |  |
| **Kidney disease** | **+1.0948** | 0.4280 | ±0.8559 | **+2.558** | **0.0105** | 2.9886 | * |
| Circulatory disease | +0.3930 | 0.3695 | ±0.7390 | +1.064 | 0.2875 | 1.4815 |  |
| Avg. daily time < 70 (%) | +0.0134 | 0.0510 | ±0.1019 | +0.263 | 0.7929 | 1.0135 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1586**, LLR χ² = **40.41** (p = **3.05e-05**), AUC = **0.7494**, AIC = **238.4**, BIC = **279.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.5345** | 2.7642 | ±5.5285 | **+2.002** | **0.0453** | 253.2712 | * |
| Education: graduate level (vs college) | -0.3021 | 0.4299 | ±0.8599 | -0.703 | 0.4822 | 0.7392 |  |
| Education: high school or below (vs college) | +0.4536 | 0.4833 | ±0.9666 | +0.938 | 0.3480 | 1.5739 |  |
| **Site: UCSD (vs UAB)** | **+0.8573** | 0.4105 | ±0.8209 | **+2.089** | **0.0367** | 2.3569 | * |
| Site: UW (vs UAB) | -0.4645 | 0.4947 | ±0.9895 | -0.939 | 0.3478 | 0.6284 |  |
| Age (years) | -0.0278 | 0.0182 | ±0.0363 | -1.530 | 0.1261 | 0.9726 |  |
| BMI (kg/m2) | +0.0329 | 0.0214 | ±0.0427 | +1.538 | 0.1240 | 1.0334 |  |
| Hypertension | -0.1086 | 0.4225 | ±0.8450 | -0.257 | 0.7971 | 0.8971 |  |
| High cholesterol | +0.5932 | 0.3826 | ±0.7653 | +1.550 | 0.1211 | 1.8097 |  |
| **Kidney disease** | **+1.0111** | 0.4405 | ±0.8809 | **+2.296** | **0.0217** | 2.7487 | * |
| Circulatory disease | +0.3218 | 0.3875 | ±0.7749 | +0.830 | 0.4063 | 1.3796 |  |
| **Time 54-250, pooled (%)** | **-0.0710** | 0.0243 | ±0.0486 | **-2.921** | **0.0035** | 0.9314 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1585**, LLR χ² = **40.37** (p = **3.09e-05**), AUC = **0.7481**, AIC = **238.4**, BIC = **279.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.3151** | 2.9231 | ±5.8463 | **+2.160** | **0.0307** | 552.8610 | * |
| Education: graduate level (vs college) | -0.2858 | 0.4293 | ±0.8585 | -0.666 | 0.5055 | 0.7514 |  |
| Education: high school or below (vs college) | +0.4123 | 0.4878 | ±0.9755 | +0.845 | 0.3980 | 1.5103 |  |
| **Site: UCSD (vs UAB)** | **+0.8486** | 0.4115 | ±0.8230 | **+2.062** | **0.0392** | 2.3364 | * |
| Site: UW (vs UAB) | -0.4782 | 0.4939 | ±0.9878 | -0.968 | 0.3329 | 0.6199 |  |
| Age (years) | -0.0287 | 0.0182 | ±0.0364 | -1.580 | 0.1141 | 0.9717 |  |
| BMI (kg/m2) | +0.0337 | 0.0214 | ±0.0427 | +1.578 | 0.1145 | 1.0343 |  |
| Hypertension | -0.1072 | 0.4221 | ±0.8441 | -0.254 | 0.7994 | 0.8983 |  |
| High cholesterol | +0.5878 | 0.3825 | ±0.7649 | +1.537 | 0.1243 | 1.8001 |  |
| **Kidney disease** | **+0.9844** | 0.4424 | ±0.8848 | **+2.225** | **0.0261** | 2.6763 | * |
| Circulatory disease | +0.3109 | 0.3883 | ±0.7766 | +0.801 | 0.4234 | 1.3646 |  |
| **Avg. daily time 54-250 (%)** | **-0.0784** | 0.0261 | ±0.0522 | **-3.005** | **0.0027** | 0.9246 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1157**, LLR χ² = **29.48** (p = **0.0019**), AUC = **0.7296**, AIC = **249.3**, BIC = **290.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.2650 | 1.4050 | ±2.8101 | -0.900 | 0.3680 | 0.2823 |  |
| Education: graduate level (vs college) | -0.3425 | 0.4232 | ±0.8465 | -0.809 | 0.4183 | 0.7100 |  |
| Education: high school or below (vs college) | +0.5763 | 0.4528 | ±0.9057 | +1.273 | 0.2032 | 1.7794 |  |
| Site: UCSD (vs UAB) | +0.7609 | 0.3990 | ±0.7980 | +1.907 | 0.0565 | 2.1402 | . |
| Site: UW (vs UAB) | -0.6068 | 0.4831 | ±0.9663 | -1.256 | 0.2091 | 0.5451 |  |
| Age (years) | -0.0299 | 0.0177 | ±0.0354 | -1.686 | 0.0919 | 0.9706 | . |
| BMI (kg/m2) | +0.0296 | 0.0210 | ±0.0419 | +1.413 | 0.1577 | 1.0301 |  |
| Hypertension | -0.0117 | 0.4072 | ±0.8144 | -0.029 | 0.9770 | 0.9883 |  |
| High cholesterol | +0.4463 | 0.3632 | ±0.7264 | +1.229 | 0.2191 | 1.5625 |  |
| **Kidney disease** | **+0.9901** | 0.4350 | ±0.8700 | **+2.276** | **0.0228** | 2.6915 | * |
| Circulatory disease | +0.3592 | 0.3756 | ±0.7512 | +0.956 | 0.3390 | 1.4321 |  |
| Time 181-250, pooled (%) | +0.0240 | 0.0127 | ±0.0255 | +1.888 | 0.0590 | 1.0243 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1182**, LLR χ² = **30.12** (p = **0.0015**), AUC = **0.7323**, AIC = **248.6**, BIC = **289.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3223 | 1.4106 | ±2.8213 | -0.937 | 0.3486 | 0.2665 |  |
| Education: graduate level (vs college) | -0.3463 | 0.4243 | ±0.8486 | -0.816 | 0.4144 | 0.7073 |  |
| Education: high school or below (vs college) | +0.5696 | 0.4536 | ±0.9071 | +1.256 | 0.2092 | 1.7676 |  |
| Site: UCSD (vs UAB) | +0.7727 | 0.3998 | ±0.7996 | +1.933 | 0.0533 | 2.1656 | . |
| Site: UW (vs UAB) | -0.5886 | 0.4838 | ±0.9676 | -1.217 | 0.2237 | 0.5551 |  |
| Age (years) | -0.0295 | 0.0177 | ±0.0355 | -1.661 | 0.0968 | 0.9710 | . |
| BMI (kg/m2) | +0.0298 | 0.0210 | ±0.0420 | +1.418 | 0.1561 | 1.0302 |  |
| Hypertension | -0.0046 | 0.4080 | ±0.8160 | -0.011 | 0.9911 | 0.9954 |  |
| High cholesterol | +0.4487 | 0.3639 | ±0.7277 | +1.233 | 0.2175 | 1.5663 |  |
| **Kidney disease** | **+0.9818** | 0.4358 | ±0.8717 | **+2.253** | **0.0243** | 2.6693 | * |
| Circulatory disease | +0.3596 | 0.3762 | ±0.7524 | +0.956 | 0.3392 | 1.4327 |  |
| **Avg. daily time 181-250 (%)** | **+0.0253** | 0.0123 | ±0.0246 | **+2.052** | **0.0402** | 1.0256 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1413**, LLR χ² = **35.99** (p = **1.70e-04**), AUC = **0.7446**, AIC = **242.8**, BIC = **284.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5223 | 1.4370 | ±2.8739 | -1.059 | 0.2894 | 0.2182 |  |
| Education: graduate level (vs college) | -0.3126 | 0.4305 | ±0.8610 | -0.726 | 0.4677 | 0.7315 |  |
| Education: high school or below (vs college) | +0.5096 | 0.4673 | ±0.9346 | +1.091 | 0.2755 | 1.6646 |  |
| Site: UCSD (vs UAB) | +0.7951 | 0.4069 | ±0.8137 | +1.954 | 0.0507 | 2.2147 | . |
| Site: UW (vs UAB) | -0.5517 | 0.4900 | ±0.9801 | -1.126 | 0.2602 | 0.5760 |  |
| Age (years) | -0.0294 | 0.0180 | ±0.0359 | -1.637 | 0.1016 | 0.9710 |  |
| BMI (kg/m2) | +0.0319 | 0.0213 | ±0.0426 | +1.497 | 0.1344 | 1.0324 |  |
| Hypertension | -0.0514 | 0.4159 | ±0.8318 | -0.124 | 0.9016 | 0.9499 |  |
| High cholesterol | +0.5071 | 0.3729 | ±0.7458 | +1.360 | 0.1739 | 1.6605 |  |
| **Kidney disease** | **+0.9577** | 0.4399 | ±0.8798 | **+2.177** | **0.0295** | 2.6058 | * |
| Circulatory disease | +0.3255 | 0.3831 | ±0.7662 | +0.850 | 0.3955 | 1.3847 |  |
| **Time > 180 (%)** | **+0.0264** | 0.0085 | ±0.0169 | **+3.119** | **0.0018** | 1.0267 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1398**, LLR χ² = **35.62** (p = **1.96e-04**), AUC = **0.7432**, AIC = **243.1**, BIC = **284.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5269 | 1.4366 | ±2.8733 | -1.063 | 0.2879 | 0.2172 |  |
| Education: graduate level (vs college) | -0.3186 | 0.4302 | ±0.8603 | -0.741 | 0.4589 | 0.7272 |  |
| Education: high school or below (vs college) | +0.4962 | 0.4673 | ±0.9347 | +1.062 | 0.2884 | 1.6424 |  |
| Site: UCSD (vs UAB) | +0.7964 | 0.4065 | ±0.8131 | +1.959 | 0.0501 | 2.2175 | . |
| Site: UW (vs UAB) | -0.5445 | 0.4895 | ±0.9790 | -1.112 | 0.2660 | 0.5802 |  |
| Age (years) | -0.0292 | 0.0180 | ±0.0359 | -1.627 | 0.1036 | 0.9712 |  |
| BMI (kg/m2) | +0.0321 | 0.0213 | ±0.0426 | +1.508 | 0.1315 | 1.0326 |  |
| Hypertension | -0.0398 | 0.4154 | ±0.8307 | -0.096 | 0.9238 | 0.9610 |  |
| High cholesterol | +0.4989 | 0.3720 | ±0.7440 | +1.341 | 0.1799 | 1.6469 |  |
| **Kidney disease** | **+0.9498** | 0.4405 | ±0.8810 | **+2.156** | **0.0311** | 2.5851 | * |
| Circulatory disease | +0.3223 | 0.3828 | ±0.7657 | +0.842 | 0.3998 | 1.3804 |  |
| **Avg. daily time > 180 (%)** | **+0.0260** | 0.0085 | ±0.0170 | **+3.064** | **0.0022** | 1.0263 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1668**, LLR χ² = **42.50** (p = **1.33e-05**), AUC = **0.7698**, AIC = **236.3**, BIC = **277.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6000 | 1.4644 | ±2.9287 | -1.093 | 0.2746 | 0.2019 |  |
| Education: graduate level (vs college) | -0.2798 | 0.4366 | ±0.8731 | -0.641 | 0.5215 | 0.7559 |  |
| Education: high school or below (vs college) | +0.5590 | 0.4721 | ±0.9441 | +1.184 | 0.2364 | 1.7489 |  |
| **Site: UCSD (vs UAB)** | **+0.8723** | 0.4170 | ±0.8340 | **+2.092** | **0.0365** | 2.3924 | * |
| Site: UW (vs UAB) | -0.5423 | 0.5000 | ±1.0000 | -1.085 | 0.2781 | 0.5814 |  |
| Age (years) | -0.0282 | 0.0184 | ±0.0367 | -1.533 | 0.1254 | 0.9722 |  |
| BMI (kg/m2) | +0.0321 | 0.0217 | ±0.0434 | +1.479 | 0.1392 | 1.0326 |  |
| Hypertension | -0.0917 | 0.4240 | ±0.8480 | -0.216 | 0.8288 | 0.9124 |  |
| High cholesterol | +0.4802 | 0.3811 | ±0.7622 | +1.260 | 0.2076 | 1.6165 |  |
| **Kidney disease** | **+1.0770** | 0.4428 | ±0.8856 | **+2.432** | **0.0150** | 2.9359 | * |
| Circulatory disease | +0.2916 | 0.3930 | ±0.7859 | +0.742 | 0.4580 | 1.3386 |  |
| **Nocturnal time > 180 (%)** | **+0.0341** | 0.0089 | ±0.0178 | **+3.832** | **1.27e-04** | 1.0347 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1307**, LLR χ² = **33.30** (p = **4.71e-04**), AUC = **0.7382**, AIC = **245.5**, BIC = **286.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3336 | 1.4360 | ±2.8720 | -0.929 | 0.3530 | 0.2635 |  |
| Education: graduate level (vs college) | -0.2999 | 0.4287 | ±0.8575 | -0.699 | 0.4843 | 0.7409 |  |
| Education: high school or below (vs college) | +0.5187 | 0.4579 | ±0.9158 | +1.133 | 0.2574 | 1.6798 |  |
| Site: UCSD (vs UAB) | +0.7802 | 0.4016 | ±0.8032 | +1.943 | 0.0521 | 2.1818 | . |
| Site: UW (vs UAB) | -0.7327 | 0.4886 | ±0.9771 | -1.500 | 0.1337 | 0.4806 |  |
| **Age (years)** | **-0.0365** | 0.0186 | ±0.0372 | **-1.962** | **0.0498** | 0.9641 | * |
| BMI (kg/m2) | +0.0359 | 0.0214 | ±0.0428 | +1.677 | 0.0936 | 1.0365 | . |
| Hypertension | -0.0682 | 0.4128 | ±0.8255 | -0.165 | 0.8688 | 0.9341 |  |
| High cholesterol | +0.5486 | 0.3718 | ±0.7437 | +1.475 | 0.1401 | 1.7309 |  |
| **Kidney disease** | **+0.8944** | 0.4408 | ±0.8817 | **+2.029** | **0.0425** | 2.4458 | * |
| Circulatory disease | +0.3663 | 0.3800 | ±0.7600 | +0.964 | 0.3351 | 1.4424 |  |
| **Any reading > 250 during wear (0/1)** | **+0.9626** | 0.3637 | ±0.7274 | **+2.647** | **0.0081** | 2.6185 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1612**, LLR χ² = **41.06** (p = **2.35e-05**), AUC = **0.7513**, AIC = **237.7**, BIC = **278.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5520 | 1.4450 | ±2.8900 | -1.074 | 0.2828 | 0.2118 |  |
| Education: graduate level (vs college) | -0.3050 | 0.4300 | ±0.8601 | -0.709 | 0.4781 | 0.7371 |  |
| Education: high school or below (vs college) | +0.4375 | 0.4856 | ±0.9711 | +0.901 | 0.3675 | 1.5489 |  |
| **Site: UCSD (vs UAB)** | **+0.8399** | 0.4109 | ±0.8217 | **+2.044** | **0.0409** | 2.3162 | * |
| Site: UW (vs UAB) | -0.4833 | 0.4946 | ±0.9893 | -0.977 | 0.3285 | 0.6167 |  |
| Age (years) | -0.0277 | 0.0182 | ±0.0364 | -1.524 | 0.1274 | 0.9727 |  |
| BMI (kg/m2) | +0.0331 | 0.0214 | ±0.0427 | +1.547 | 0.1219 | 1.0336 |  |
| Hypertension | -0.1103 | 0.4230 | ±0.8461 | -0.261 | 0.7943 | 0.8955 |  |
| High cholesterol | +0.5999 | 0.3836 | ±0.7672 | +1.564 | 0.1178 | 1.8220 |  |
| **Kidney disease** | **+1.0009** | 0.4416 | ±0.8833 | **+2.266** | **0.0234** | 2.7208 | * |
| Circulatory disease | +0.3303 | 0.3890 | ±0.7781 | +0.849 | 0.3959 | 1.3913 |  |
| **Time > 250 (%)** | **+0.0742** | 0.0252 | ±0.0504 | **+2.946** | **0.0032** | 1.0770 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 229)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **229**, events = **56**, McFadden pseudo-R² = **0.1602**, LLR χ² = **40.81** (p = **2.60e-05**), AUC = **0.7504**, AIC = **238.0**, BIC = **279.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5205 | 1.4446 | ±2.8892 | -1.053 | 0.2925 | 0.2186 |  |
| Education: graduate level (vs college) | -0.2951 | 0.4291 | ±0.8581 | -0.688 | 0.4916 | 0.7444 |  |
| Education: high school or below (vs college) | +0.3886 | 0.4906 | ±0.9811 | +0.792 | 0.4283 | 1.4749 |  |
| **Site: UCSD (vs UAB)** | **+0.8318** | 0.4118 | ±0.8236 | **+2.020** | **0.0434** | 2.2975 | * |
| Site: UW (vs UAB) | -0.4949 | 0.4938 | ±0.9876 | -1.002 | 0.3162 | 0.6096 |  |
| Age (years) | -0.0284 | 0.0182 | ±0.0364 | -1.560 | 0.1189 | 0.9720 |  |
| BMI (kg/m2) | +0.0338 | 0.0214 | ±0.0428 | +1.580 | 0.1141 | 1.0344 |  |
| Hypertension | -0.1073 | 0.4223 | ±0.8445 | -0.254 | 0.7994 | 0.8983 |  |
| High cholesterol | +0.5827 | 0.3825 | ±0.7650 | +1.523 | 0.1276 | 1.7909 |  |
| **Kidney disease** | **+0.9764** | 0.4435 | ±0.8871 | **+2.201** | **0.0277** | 2.6548 | * |
| Circulatory disease | +0.3210 | 0.3899 | ±0.7798 | +0.823 | 0.4103 | 1.3786 |  |
| **Avg. daily time > 250 (%)** | **+0.0826** | 0.0275 | ±0.0550 | **+3.004** | **0.0027** | 1.0861 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Non-healthy group (T2D non-insulin + T2D insulin) - Depression

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 60 single-predictor tests; 33 with raw p < 0.05 (about 3 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **CES-D-10 depressive symptoms (0-30)** (n = 229): best single predictor out of sample is **%>250 (pooled)** (CV R² 0.073 vs 0.029 for covariates alone, gain +0.044; +0.999 per SD, p = 1.4e-05). Raw p < 0.05 (FDR not applicable here): %>250 (pooled) (p = 1.4e-05), %54-250 (pooled) (p = 1.6e-05), %54-250 (daily avg) (p = 2.8e-04), %>250 (daily avg) (p = 3.0e-04), %>180 nocturnal (p = 6.7e-04).
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 229): best single predictor out of sample is **%>180 nocturnal** (CV AUC 0.707 vs 0.650 for covariates alone, gain +0.057; OR 1.86 per SD, p = 1.3e-04). Raw p < 0.05 (FDR not applicable here): %>180 nocturnal (p = 1.3e-04), Nocturnal mean (p = 2.2e-04), SD of daily means (p = 3.5e-04), TIR 70-180 (pooled) (p = 0.002), TIR 70-180 (daily avg) (p = 0.002).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Clinically relevant depressive symptoms (CES-D-10 >= 10) (+0.057, via %>180 nocturnal); CES-D-10 depressive symptoms (0-30) (+0.044, via %>250 (pooled)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM level (0 FDR-significant / 6 raw-significant of 6); CGM variability (0 FDR-significant / 6 raw-significant of 16); Band > 180 (0 FDR-significant / 6 raw-significant of 6).
Level metrics: 0 FDR-significant (6 raw); variability metrics: 0 FDR-significant (6 raw); HbA1c alone: 0 FDR-significant (1 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** CES-D-10 depressive symptoms (%>250 (pooled), ΔAIC -7.8); Clinically relevant depressive symptoms (%>180 nocturnal, ΔAIC -9.3).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
