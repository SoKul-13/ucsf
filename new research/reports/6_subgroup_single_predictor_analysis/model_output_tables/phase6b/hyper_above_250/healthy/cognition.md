# Phase 6b model output tables - Hyperglycaemia exposure: at least one reading > 250 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Cognition

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 244; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **244**, R² = **0.0897**, Adj R² = **0.0506**, F-statistic = **2.30** (p = **0.0138**), Residual SE = **3.255** on **233** df, AIC = **1279.1**, BIC = **1317.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.6733** | 1.6107 | ±3.2213 | **+15.940** | **3.36e-57** | *** |
| Education: graduate level (vs college) | +0.3143 | 0.4544 | ±0.9089 | +0.692 | 0.4892 |  |
| Education: high school or below (vs college) | -1.8861 | 1.0716 | ±2.1432 | -1.760 | 0.0784 | . |
| Site: UCSD (vs UAB) | +0.3248 | 0.6954 | ±1.3908 | +0.467 | 0.6404 |  |
| Site: UW (vs UAB) | +0.8864 | 0.5762 | ±1.1524 | +1.538 | 0.1239 |  |
| Age (years) | -0.0305 | 0.0190 | ±0.0380 | -1.605 | 0.1085 |  |
| BMI (kg/m2) | +0.0548 | 0.0318 | ±0.0636 | +1.724 | 0.0846 | . |
| Hypertension | -0.5031 | 0.4748 | ±0.9495 | -1.060 | 0.2892 |  |
| High cholesterol | +0.2373 | 0.4359 | ±0.8717 | +0.544 | 0.5861 |  |
| Kidney disease | +0.7455 | 0.8243 | ±1.6487 | +0.904 | 0.3658 |  |
| Circulatory disease | -0.6638 | 0.6426 | ±1.2853 | -1.033 | 0.3016 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **244**, R² = **0.1078**, Adj R² = **0.0655**, F-statistic = **2.55** (p = **0.0047**), Residual SE = **3.230** on **232** df, AIC = **1276.2**, BIC = **1318.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.4480** | 2.1948 | ±4.3896 | **+12.961** | **2.02e-38** | *** |
| Education: graduate level (vs college) | +0.3199 | 0.4586 | ±0.9172 | +0.697 | 0.4855 |  |
| Education: high school or below (vs college) | -1.6041 | 1.0405 | ±2.0811 | -1.542 | 0.1232 |  |
| Site: UCSD (vs UAB) | +0.3245 | 0.6891 | ±1.3782 | +0.471 | 0.6377 |  |
| Site: UW (vs UAB) | +0.9241 | 0.5726 | ±1.1453 | +1.614 | 0.1066 |  |
| Age (years) | -0.0299 | 0.0190 | ±0.0380 | -1.572 | 0.1160 |  |
| BMI (kg/m2) | +0.0612 | 0.0322 | ±0.0644 | +1.902 | 0.0571 | . |
| Hypertension | -0.4897 | 0.4708 | ±0.9415 | -1.040 | 0.2982 |  |
| High cholesterol | +0.2985 | 0.4362 | ±0.8724 | +0.684 | 0.4938 |  |
| Kidney disease | +0.6579 | 0.8061 | ±1.6122 | +0.816 | 0.4144 |  |
| Circulatory disease | -0.4095 | 0.6072 | ±1.2143 | -0.674 | 0.5000 |  |
| HbA1c (%) | -0.5165 | 0.3067 | ±0.6134 | -1.684 | 0.0922 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **244**, R² = **0.1269**, Adj R² = **0.0855**, F-statistic = **3.06** (p = **7.42e-04**), Residual SE = **3.195** on **232** df, AIC = **1271.0**, BIC = **1312.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.3733** | 1.9325 | ±3.8649 | **+14.682** | **8.35e-49** | *** |
| Education: graduate level (vs college) | +0.4475 | 0.4645 | ±0.9289 | +0.963 | 0.3353 |  |
| Education: high school or below (vs college) | -1.4513 | 0.9861 | ±1.9722 | -1.472 | 0.1411 |  |
| Site: UCSD (vs UAB) | +0.2514 | 0.6840 | ±1.3679 | +0.368 | 0.7132 |  |
| Site: UW (vs UAB) | +0.9427 | 0.5641 | ±1.1281 | +1.671 | 0.0947 | . |
| Age (years) | -0.0313 | 0.0188 | ±0.0377 | -1.664 | 0.0960 | . |
| **BMI (kg/m2)** | **+0.0684** | 0.0324 | ±0.0647 | **+2.115** | **0.0344** | * |
| Hypertension | -0.4318 | 0.4691 | ±0.9382 | -0.921 | 0.3573 |  |
| High cholesterol | +0.2899 | 0.4237 | ±0.8474 | +0.684 | 0.4939 |  |
| Kidney disease | +0.7796 | 0.7681 | ±1.5363 | +1.015 | 0.3101 |  |
| Circulatory disease | -0.3938 | 0.5769 | ±1.1539 | -0.683 | 0.4948 |  |
| **Mean glucose (mg/dL)** | **-0.0230** | 0.0093 | ±0.0186 | **-2.463** | **0.0138** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **244**, R² = **0.1269**, Adj R² = **0.0855**, F-statistic = **3.06** (p = **7.42e-04**), Residual SE = **3.195** on **232** df, AIC = **1271.0**, BIC = **1312.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.5509** | 2.8605 | ±5.7211 | **+11.030** | **2.75e-28** | *** |
| Education: graduate level (vs college) | +0.4475 | 0.4645 | ±0.9289 | +0.963 | 0.3353 |  |
| Education: high school or below (vs college) | -1.4513 | 0.9861 | ±1.9722 | -1.472 | 0.1411 |  |
| Site: UCSD (vs UAB) | +0.2514 | 0.6840 | ±1.3679 | +0.368 | 0.7132 |  |
| Site: UW (vs UAB) | +0.9427 | 0.5641 | ±1.1281 | +1.671 | 0.0947 | . |
| Age (years) | -0.0313 | 0.0188 | ±0.0377 | -1.664 | 0.0960 | . |
| **BMI (kg/m2)** | **+0.0684** | 0.0324 | ±0.0647 | **+2.115** | **0.0344** | * |
| Hypertension | -0.4318 | 0.4691 | ±0.9382 | -0.921 | 0.3573 |  |
| High cholesterol | +0.2899 | 0.4237 | ±0.8474 | +0.684 | 0.4939 |  |
| Kidney disease | +0.7796 | 0.7681 | ±1.5363 | +1.015 | 0.3101 |  |
| Circulatory disease | -0.3938 | 0.5769 | ±1.1539 | -0.683 | 0.4948 |  |
| **GMI (%)** | **-0.9600** | 0.3898 | ±0.7796 | **-2.463** | **0.0138** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **244**, R² = **0.1166**, Adj R² = **0.0747**, F-statistic = **2.78** (p = **0.0020**), Residual SE = **3.214** on **232** df, AIC = **1273.8**, BIC = **1315.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.6610** | 1.8925 | ±3.7850 | **+14.616** | **2.22e-48** | *** |
| Education: graduate level (vs college) | +0.3887 | 0.4624 | ±0.9249 | +0.840 | 0.4007 |  |
| Education: high school or below (vs college) | -1.5599 | 1.0028 | ±2.0056 | -1.556 | 0.1198 |  |
| Site: UCSD (vs UAB) | +0.3123 | 0.6900 | ±1.3799 | +0.453 | 0.6508 |  |
| Site: UW (vs UAB) | +0.9219 | 0.5707 | ±1.1414 | +1.615 | 0.1062 |  |
| Age (years) | -0.0329 | 0.0191 | ±0.0382 | -1.720 | 0.0854 | . |
| **BMI (kg/m2)** | **+0.0694** | 0.0327 | ±0.0654 | **+2.123** | **0.0337** | * |
| Hypertension | -0.4445 | 0.4724 | ±0.9447 | -0.941 | 0.3467 |  |
| High cholesterol | +0.2893 | 0.4299 | ±0.8597 | +0.673 | 0.5010 |  |
| Kidney disease | +0.6297 | 0.7922 | ±1.5844 | +0.795 | 0.4267 |  |
| Circulatory disease | -0.4785 | 0.5873 | ±1.1746 | -0.815 | 0.4152 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0176** | 0.0083 | ±0.0166 | **-2.129** | **0.0333** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **244**, R² = **0.0966**, Adj R² = **0.0538**, F-statistic = **2.26** (p = **0.0126**), Residual SE = **3.250** on **232** df, AIC = **1279.3**, BIC = **1321.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6160** | 1.8821 | ±3.7641 | **+14.142** | **2.10e-45** | *** |
| Education: graduate level (vs college) | +0.3240 | 0.4573 | ±0.9145 | +0.709 | 0.4786 |  |
| Education: high school or below (vs college) | -1.8708 | 1.0422 | ±2.0844 | -1.795 | 0.0726 | . |
| Site: UCSD (vs UAB) | +0.2608 | 0.7033 | ±1.4066 | +0.371 | 0.7108 |  |
| Site: UW (vs UAB) | +0.8643 | 0.5771 | ±1.1541 | +1.498 | 0.1342 |  |
| Age (years) | -0.0293 | 0.0189 | ±0.0378 | -1.551 | 0.1209 |  |
| BMI (kg/m2) | +0.0610 | 0.0325 | ±0.0649 | +1.878 | 0.0603 | . |
| Hypertension | -0.4628 | 0.4773 | ±0.9546 | -0.970 | 0.3323 |  |
| High cholesterol | +0.1621 | 0.4318 | ±0.8636 | +0.375 | 0.7073 |  |
| Kidney disease | +0.9193 | 0.7952 | ±1.5903 | +1.156 | 0.2476 |  |
| Circulatory disease | -0.5463 | 0.6201 | ±1.2401 | -0.881 | 0.3783 |  |
| Glucose SD, pooled (mg/dL) | -0.0385 | 0.0324 | ±0.0648 | -1.188 | 0.2350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **244**, R² = **0.0985**, Adj R² = **0.0557**, F-statistic = **2.30** (p = **0.0107**), Residual SE = **3.246** on **232** df, AIC = **1278.8**, BIC = **1320.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6586** | 1.8181 | ±3.6361 | **+14.663** | **1.11e-48** | *** |
| Education: graduate level (vs college) | +0.3405 | 0.4566 | ±0.9133 | +0.746 | 0.4559 |  |
| Education: high school or below (vs college) | -1.8919 | 1.0468 | ±2.0937 | -1.807 | 0.0707 | . |
| Site: UCSD (vs UAB) | +0.2535 | 0.7005 | ±1.4010 | +0.362 | 0.7175 |  |
| Site: UW (vs UAB) | +0.8651 | 0.5754 | ±1.1509 | +1.503 | 0.1327 |  |
| Age (years) | -0.0294 | 0.0189 | ±0.0378 | -1.555 | 0.1200 |  |
| BMI (kg/m2) | +0.0628 | 0.0322 | ±0.0645 | +1.947 | 0.0515 | . |
| Hypertension | -0.4500 | 0.4785 | ±0.9570 | -0.941 | 0.3469 |  |
| High cholesterol | +0.1547 | 0.4337 | ±0.8674 | +0.357 | 0.7214 |  |
| Kidney disease | +0.9332 | 0.7876 | ±1.5752 | +1.185 | 0.2361 |  |
| Circulatory disease | -0.5275 | 0.6309 | ±1.2619 | -0.836 | 0.4031 |  |
| Avg. daily SD (mg/dL) | -0.0459 | 0.0308 | ±0.0615 | -1.490 | 0.1361 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **244**, R² = **0.0953**, Adj R² = **0.0524**, F-statistic = **2.22** (p = **0.0142**), Residual SE = **3.252** on **232** df, AIC = **1279.6**, BIC = **1321.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5473** | 1.9733 | ±3.9466 | **+12.440** | **1.59e-35** | *** |
| Education: graduate level (vs college) | +0.3620 | 0.4569 | ±0.9139 | +0.792 | 0.4282 |  |
| Education: high school or below (vs college) | -1.7666 | 1.0661 | ±2.1322 | -1.657 | 0.0975 | . |
| Site: UCSD (vs UAB) | +0.3783 | 0.7068 | ±1.4137 | +0.535 | 0.5926 |  |
| Site: UW (vs UAB) | +0.9457 | 0.5840 | ±1.1680 | +1.619 | 0.1054 |  |
| Age (years) | -0.0323 | 0.0190 | ±0.0380 | -1.701 | 0.0890 | . |
| BMI (kg/m2) | +0.0533 | 0.0319 | ±0.0637 | +1.672 | 0.0946 | . |
| Hypertension | -0.5085 | 0.4765 | ±0.9531 | -1.067 | 0.2859 |  |
| High cholesterol | +0.3453 | 0.4531 | ±0.9063 | +0.762 | 0.4460 |  |
| Kidney disease | +0.5988 | 0.8250 | ±1.6500 | +0.726 | 0.4680 |  |
| Circulatory disease | -0.6866 | 0.6409 | ±1.2818 | -1.071 | 0.2840 |  |
| CV (%) | +0.0531 | 0.0435 | ±0.0870 | +1.221 | 0.2220 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **244**, R² = **0.0954**, Adj R² = **0.0526**, F-statistic = **2.23** (p = **0.0140**), Residual SE = **3.252** on **232** df, AIC = **1279.6**, BIC = **1321.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.0021** | 1.8205 | ±3.6409 | **+14.833** | **9.02e-50** | *** |
| Education: graduate level (vs college) | +0.3381 | 0.4561 | ±0.9122 | +0.741 | 0.4585 |  |
| Education: high school or below (vs college) | -1.7952 | 1.0636 | ±2.1271 | -1.688 | 0.0914 | . |
| Site: UCSD (vs UAB) | +0.3690 | 0.7055 | ±1.4109 | +0.523 | 0.6009 |  |
| Site: UW (vs UAB) | +0.9435 | 0.5838 | ±1.1676 | +1.616 | 0.1061 |  |
| Age (years) | -0.0319 | 0.0190 | ±0.0379 | -1.682 | 0.0926 | . |
| BMI (kg/m2) | +0.0543 | 0.0322 | ±0.0643 | +1.687 | 0.0916 | . |
| Hypertension | -0.5264 | 0.4782 | ±0.9565 | -1.101 | 0.2710 |  |
| High cholesterol | +0.3274 | 0.4474 | ±0.8949 | +0.732 | 0.4644 |  |
| Kidney disease | +0.6149 | 0.8218 | ±1.6436 | +0.748 | 0.4543 |  |
| Circulatory disease | -0.6849 | 0.6379 | ±1.2758 | -1.074 | 0.2830 |  |
| Mean / SD ratio | -0.2756 | 0.2306 | ±0.4613 | -1.195 | 0.2321 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **244**, R² = **0.0922**, Adj R² = **0.0492**, F-statistic = **2.14** (p = **0.0184**), Residual SE = **3.258** on **232** df, AIC = **1280.5**, BIC = **1322.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.5004** | 1.8205 | ±3.6411 | **+14.556** | **5.32e-48** | *** |
| Education: graduate level (vs college) | +0.3198 | 0.4566 | ±0.9133 | +0.700 | 0.4837 |  |
| Education: high school or below (vs college) | -1.8235 | 1.0621 | ±2.1242 | -1.717 | 0.0860 | . |
| Site: UCSD (vs UAB) | +0.3490 | 0.7041 | ±1.4083 | +0.496 | 0.6201 |  |
| Site: UW (vs UAB) | +0.9278 | 0.5868 | ±1.1735 | +1.581 | 0.1138 |  |
| Age (years) | -0.0316 | 0.0189 | ±0.0379 | -1.668 | 0.0953 | . |
| BMI (kg/m2) | +0.0537 | 0.0321 | ±0.0642 | +1.672 | 0.0945 | . |
| Hypertension | -0.5223 | 0.4811 | ±0.9621 | -1.086 | 0.2776 |  |
| High cholesterol | +0.2938 | 0.4503 | ±0.9006 | +0.652 | 0.5141 |  |
| Kidney disease | +0.6577 | 0.8211 | ±1.6422 | +0.801 | 0.4232 |  |
| Circulatory disease | -0.6708 | 0.6405 | ±1.2810 | -1.047 | 0.2950 |  |
| Avg. daily mean/SD | -0.1402 | 0.1891 | ±0.3783 | -0.741 | 0.4586 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **244**, R² = **0.0897**, Adj R² = **0.0466**, F-statistic = **2.08** (p = **0.0226**), Residual SE = **3.262** on **232** df, AIC = **1281.1**, BIC = **1323.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.7807** | 2.0433 | ±4.0866 | **+12.617** | **1.70e-36** | *** |
| Education: graduate level (vs college) | +0.3098 | 0.4569 | ±0.9137 | +0.678 | 0.4977 |  |
| Education: high school or below (vs college) | -1.8903 | 1.0837 | ±2.1675 | -1.744 | 0.0811 | . |
| Site: UCSD (vs UAB) | +0.3170 | 0.7082 | ±1.4165 | +0.448 | 0.6544 |  |
| Site: UW (vs UAB) | +0.8757 | 0.5990 | ±1.1979 | +1.462 | 0.1437 |  |
| Age (years) | -0.0305 | 0.0191 | ±0.0382 | -1.597 | 0.1102 |  |
| BMI (kg/m2) | +0.0554 | 0.0317 | ±0.0635 | +1.746 | 0.0808 | . |
| Hypertension | -0.5088 | 0.4725 | ±0.9451 | -1.077 | 0.2816 |  |
| High cholesterol | +0.2281 | 0.4413 | ±0.8826 | +0.517 | 0.6053 |  |
| Kidney disease | +0.7453 | 0.8292 | ±1.6585 | +0.899 | 0.3688 |  |
| Circulatory disease | -0.6600 | 0.6463 | ±1.2927 | -1.021 | 0.3072 |  |
| MAG (mg/dL/h) | -0.0025 | 0.0254 | ±0.0508 | -0.097 | 0.9227 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **244**, R² = **0.0912**, Adj R² = **0.0482**, F-statistic = **2.12** (p = **0.0200**), Residual SE = **3.259** on **232** df, AIC = **1280.7**, BIC = **1322.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.2952** | 2.0648 | ±4.1297 | **+12.735** | **3.79e-37** | *** |
| Education: graduate level (vs college) | +0.3202 | 0.4570 | ±0.9139 | +0.701 | 0.4835 |  |
| Education: high school or below (vs college) | -1.8848 | 1.0631 | ±2.1263 | -1.773 | 0.0762 | . |
| Site: UCSD (vs UAB) | +0.2809 | 0.7117 | ±1.4234 | +0.395 | 0.6931 |  |
| Site: UW (vs UAB) | +0.8569 | 0.5828 | ±1.1656 | +1.470 | 0.1415 |  |
| Age (years) | -0.0304 | 0.0191 | ±0.0381 | -1.594 | 0.1108 |  |
| BMI (kg/m2) | +0.0575 | 0.0318 | ±0.0636 | +1.806 | 0.0709 | . |
| Hypertension | -0.4959 | 0.4775 | ±0.9551 | -1.038 | 0.2991 |  |
| High cholesterol | +0.1837 | 0.4499 | ±0.8997 | +0.408 | 0.6830 |  |
| Kidney disease | +0.7977 | 0.8137 | ±1.6274 | +0.980 | 0.3269 |  |
| Circulatory disease | -0.6185 | 0.6449 | ±1.2897 | -0.959 | 0.3375 |  |
| Avg. daily range (mg/dL) | -0.0050 | 0.0081 | ±0.0163 | -0.614 | 0.5392 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **244**, R² = **0.0948**, Adj R² = **0.0519**, F-statistic = **2.21** (p = **0.0147**), Residual SE = **3.253** on **232** df, AIC = **1279.8**, BIC = **1321.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.4244** | 1.6481 | ±3.2962 | **+15.426** | **1.09e-53** | *** |
| Education: graduate level (vs college) | +0.3398 | 0.4482 | ±0.8964 | +0.758 | 0.4483 |  |
| Education: high school or below (vs college) | -1.9325 | 1.1203 | ±2.2406 | -1.725 | 0.0845 | . |
| Site: UCSD (vs UAB) | +0.3416 | 0.6947 | ±1.3895 | +0.492 | 0.6229 |  |
| Site: UW (vs UAB) | +0.8742 | 0.5776 | ±1.1553 | +1.513 | 0.1302 |  |
| Age (years) | -0.0323 | 0.0190 | ±0.0380 | -1.698 | 0.0895 | . |
| BMI (kg/m2) | +0.0509 | 0.0322 | ±0.0644 | +1.581 | 0.1138 |  |
| Hypertension | -0.5007 | 0.4779 | ±0.9558 | -1.048 | 0.2947 |  |
| High cholesterol | +0.2578 | 0.4411 | ±0.8822 | +0.585 | 0.5588 |  |
| Kidney disease | +0.7008 | 0.8364 | ±1.6729 | +0.838 | 0.4021 |  |
| Circulatory disease | -0.6865 | 0.6656 | ±1.3311 | -1.031 | 0.3024 |  |
| SD of daily means (mg/dL) | +0.0516 | 0.0660 | ±0.1320 | +0.782 | 0.4344 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **244**, R² = **0.1181**, Adj R² = **0.0763**, F-statistic = **2.83** (p = **0.0018**), Residual SE = **3.211** on **232** df, AIC = **1273.4**, BIC = **1315.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.1223** | 2.2585 | ±4.5169 | **+9.795** | **1.18e-22** | *** |
| Education: graduate level (vs college) | +0.3891 | 0.4610 | ±0.9221 | +0.844 | 0.3987 |  |
| Education: high school or below (vs college) | -1.6189 | 0.9826 | ±1.9652 | -1.648 | 0.0994 | . |
| Site: UCSD (vs UAB) | +0.2376 | 0.6895 | ±1.3790 | +0.345 | 0.7304 |  |
| Site: UW (vs UAB) | +0.8819 | 0.5680 | ±1.1360 | +1.553 | 0.1205 |  |
| Age (years) | -0.0311 | 0.0189 | ±0.0379 | -1.641 | 0.1007 |  |
| **BMI (kg/m2)** | **+0.0700** | 0.0330 | ±0.0661 | **+2.118** | **0.0342** | * |
| Hypertension | -0.4612 | 0.4700 | ±0.9399 | -0.981 | 0.3265 |  |
| High cholesterol | +0.2431 | 0.4238 | ±0.8475 | +0.574 | 0.5662 |  |
| Kidney disease | +0.8983 | 0.7617 | ±1.5233 | +1.179 | 0.2382 |  |
| Circulatory disease | -0.4996 | 0.5936 | ±1.1871 | -0.842 | 0.3999 |  |
| **Time in range 70-180, pooled (%)** | **+0.0357** | 0.0161 | ±0.0323 | **+2.210** | **0.0271** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **244**, R² = **0.1168**, Adj R² = **0.0750**, F-statistic = **2.79** (p = **0.0020**), Residual SE = **3.213** on **232** df, AIC = **1273.8**, BIC = **1315.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.2149** | 2.2528 | ±4.5056 | **+9.861** | **6.15e-23** | *** |
| Education: graduate level (vs college) | +0.3923 | 0.4616 | ±0.9231 | +0.850 | 0.3953 |  |
| Education: high school or below (vs college) | -1.6383 | 0.9854 | ±1.9708 | -1.663 | 0.0964 | . |
| Site: UCSD (vs UAB) | +0.2302 | 0.6905 | ±1.3811 | +0.333 | 0.7389 |  |
| Site: UW (vs UAB) | +0.8765 | 0.5686 | ±1.1371 | +1.542 | 0.1232 |  |
| Age (years) | -0.0309 | 0.0189 | ±0.0379 | -1.631 | 0.1030 |  |
| **BMI (kg/m2)** | **+0.0698** | 0.0331 | ±0.0662 | **+2.109** | **0.0349** | * |
| Hypertension | -0.4598 | 0.4703 | ±0.9407 | -0.978 | 0.3282 |  |
| High cholesterol | +0.2436 | 0.4244 | ±0.8488 | +0.574 | 0.5660 |  |
| Kidney disease | +0.9004 | 0.7655 | ±1.5310 | +1.176 | 0.2395 |  |
| Circulatory disease | -0.5100 | 0.5954 | ±1.1908 | -0.857 | 0.3916 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.0345** | 0.0160 | ±0.0319 | **+2.160** | **0.0308** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **244**, R² = **0.0964**, Adj R² = **0.0536**, F-statistic = **2.25** (p = **0.0129**), Residual SE = **3.250** on **232** df, AIC = **1279.3**, BIC = **1321.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.5842** | 1.6052 | ±3.2103 | **+15.939** | **3.41e-57** | *** |
| Education: graduate level (vs college) | +0.3712 | 0.4532 | ±0.9063 | +0.819 | 0.4127 |  |
| Education: high school or below (vs college) | -1.7958 | 1.0561 | ±2.1122 | -1.700 | 0.0891 | . |
| Site: UCSD (vs UAB) | +0.3272 | 0.6951 | ±1.3903 | +0.471 | 0.6378 |  |
| Site: UW (vs UAB) | +0.9254 | 0.5796 | ±1.1591 | +1.597 | 0.1103 |  |
| Age (years) | -0.0315 | 0.0192 | ±0.0383 | -1.644 | 0.1003 |  |
| BMI (kg/m2) | +0.0515 | 0.0314 | ±0.0628 | +1.639 | 0.1013 |  |
| Hypertension | -0.4910 | 0.4771 | ±0.9542 | -1.029 | 0.3034 |  |
| High cholesterol | +0.2842 | 0.4374 | ±0.8747 | +0.650 | 0.5158 |  |
| Kidney disease | +0.6903 | 0.8286 | ±1.6571 | +0.833 | 0.4047 |  |
| Circulatory disease | -0.6777 | 0.6346 | ±1.2693 | -1.068 | 0.2856 |  |
| Any reading < 54 during wear (0/1) | +0.6265 | 0.4519 | ±0.9039 | +1.386 | 0.1657 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **244**, R² = **0.0962**, Adj R² = **0.0534**, F-statistic = **2.25** (p = **0.0130**), Residual SE = **3.250** on **232** df, AIC = **1279.4**, BIC = **1321.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.4937** | 1.6146 | ±3.2291 | **+15.790** | **3.65e-56** | *** |
| Education: graduate level (vs college) | +0.3741 | 0.4540 | ±0.9079 | +0.824 | 0.4099 |  |
| Education: high school or below (vs college) | -1.8132 | 1.0770 | ±2.1539 | -1.684 | 0.0922 | . |
| Site: UCSD (vs UAB) | +0.3940 | 0.7016 | ±1.4033 | +0.562 | 0.5744 |  |
| Site: UW (vs UAB) | +0.9820 | 0.5838 | ±1.1676 | +1.682 | 0.0926 | . |
| Age (years) | -0.0324 | 0.0191 | ±0.0382 | -1.699 | 0.0894 | . |
| BMI (kg/m2) | +0.0589 | 0.0321 | ±0.0642 | +1.835 | 0.0665 | . |
| Hypertension | -0.4696 | 0.4742 | ±0.9484 | -0.990 | 0.3220 |  |
| High cholesterol | +0.2873 | 0.4392 | ±0.8785 | +0.654 | 0.5131 |  |
| Kidney disease | +0.7542 | 0.8290 | ±1.6580 | +0.910 | 0.3630 |  |
| Circulatory disease | -0.6499 | 0.6450 | ±1.2900 | -1.008 | 0.3136 |  |
| Time < 54 (%) | +0.2925 | 0.1583 | ±0.3167 | +1.847 | 0.0647 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **244**, R² = **0.0953**, Adj R² = **0.0525**, F-statistic = **2.22** (p = **0.0141**), Residual SE = **3.252** on **232** df, AIC = **1279.6**, BIC = **1321.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.5191** | 1.6138 | ±3.2275 | **+15.813** | **2.51e-56** | *** |
| Education: graduate level (vs college) | +0.3670 | 0.4544 | ±0.9089 | +0.808 | 0.4193 |  |
| Education: high school or below (vs college) | -1.8153 | 1.0774 | ±2.1548 | -1.685 | 0.0920 | . |
| Site: UCSD (vs UAB) | +0.3898 | 0.7017 | ±1.4034 | +0.555 | 0.5786 |  |
| Site: UW (vs UAB) | +0.9871 | 0.5865 | ±1.1729 | +1.683 | 0.0924 | . |
| Age (years) | -0.0323 | 0.0191 | ±0.0382 | -1.691 | 0.0908 | . |
| BMI (kg/m2) | +0.0579 | 0.0320 | ±0.0640 | +1.809 | 0.0705 | . |
| Hypertension | -0.4701 | 0.4748 | ±0.9497 | -0.990 | 0.3222 |  |
| High cholesterol | +0.2944 | 0.4410 | ±0.8820 | +0.668 | 0.5045 |  |
| Kidney disease | +0.7507 | 0.8288 | ±1.6576 | +0.906 | 0.3651 |  |
| Circulatory disease | -0.6545 | 0.6455 | ±1.2911 | -1.014 | 0.3106 |  |
| **Avg. daily time < 54 (%)** | **+0.3585** | 0.1594 | ±0.3187 | **+2.249** | **0.0245** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **244**, R² = **0.0916**, Adj R² = **0.0485**, F-statistic = **2.13** (p = **0.0194**), Residual SE = **3.259** on **232** df, AIC = **1280.6**, BIC = **1322.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.6449** | 1.6086 | ±3.2172 | **+15.942** | **3.21e-57** | *** |
| Education: graduate level (vs college) | +0.3543 | 0.4589 | ±0.9177 | +0.772 | 0.4401 |  |
| Education: high school or below (vs college) | -1.8320 | 1.0751 | ±2.1503 | -1.704 | 0.0884 | . |
| Site: UCSD (vs UAB) | +0.3474 | 0.7006 | ±1.4012 | +0.496 | 0.6200 |  |
| Site: UW (vs UAB) | +0.9314 | 0.5845 | ±1.1689 | +1.594 | 0.1110 |  |
| Age (years) | -0.0311 | 0.0191 | ±0.0381 | -1.634 | 0.1022 |  |
| BMI (kg/m2) | +0.0527 | 0.0317 | ±0.0634 | +1.664 | 0.0961 | . |
| Hypertension | -0.4875 | 0.4751 | ±0.9502 | -1.026 | 0.3049 |  |
| High cholesterol | +0.2812 | 0.4467 | ±0.8935 | +0.629 | 0.5291 |  |
| Kidney disease | +0.7349 | 0.8280 | ±1.6560 | +0.888 | 0.3748 |  |
| Circulatory disease | -0.6511 | 0.6417 | ±1.2834 | -1.015 | 0.3103 |  |
| Time 54-69, pooled (%) | +0.1167 | 0.2833 | ±0.5666 | +0.412 | 0.6805 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **244**, R² = **0.0914**, Adj R² = **0.0483**, F-statistic = **2.12** (p = **0.0198**), Residual SE = **3.259** on **232** df, AIC = **1280.7**, BIC = **1322.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.6450** | 1.6097 | ±3.2194 | **+15.932** | **3.83e-57** | *** |
| Education: graduate level (vs college) | +0.3526 | 0.4595 | ±0.9190 | +0.767 | 0.4428 |  |
| Education: high school or below (vs college) | -1.8321 | 1.0781 | ±2.1561 | -1.699 | 0.0892 | . |
| Site: UCSD (vs UAB) | +0.3477 | 0.7005 | ±1.4009 | +0.496 | 0.6196 |  |
| Site: UW (vs UAB) | +0.9336 | 0.5861 | ±1.1722 | +1.593 | 0.1112 |  |
| Age (years) | -0.0312 | 0.0191 | ±0.0381 | -1.637 | 0.1016 |  |
| BMI (kg/m2) | +0.0531 | 0.0317 | ±0.0634 | +1.677 | 0.0935 | . |
| Hypertension | -0.4874 | 0.4756 | ±0.9512 | -1.025 | 0.3054 |  |
| High cholesterol | +0.2808 | 0.4487 | ±0.8973 | +0.626 | 0.5314 |  |
| Kidney disease | +0.7360 | 0.8275 | ±1.6550 | +0.889 | 0.3738 |  |
| Circulatory disease | -0.6494 | 0.6427 | ±1.2855 | -1.010 | 0.3123 |  |
| Avg. daily time 54-69 (%) | +0.1047 | 0.2686 | ±0.5373 | +0.390 | 0.6967 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **244**, R² = **0.0945**, Adj R² = **0.0516**, F-statistic = **2.20** (p = **0.0151**), Residual SE = **3.253** on **232** df, AIC = **1279.8**, BIC = **1321.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.5653** | 1.6092 | ±3.2184 | **+15.887** | **7.82e-57** | *** |
| Education: graduate level (vs college) | +0.3832 | 0.4565 | ±0.9130 | +0.839 | 0.4012 |  |
| Education: high school or below (vs college) | -1.7964 | 1.0765 | ±2.1530 | -1.669 | 0.0952 | . |
| Site: UCSD (vs UAB) | +0.3790 | 0.7023 | ±1.4046 | +0.540 | 0.5894 |  |
| Site: UW (vs UAB) | +0.9761 | 0.5867 | ±1.1734 | +1.664 | 0.0962 | . |
| Age (years) | -0.0320 | 0.0191 | ±0.0382 | -1.678 | 0.0934 | . |
| BMI (kg/m2) | +0.0543 | 0.0317 | ±0.0633 | +1.716 | 0.0861 | . |
| Hypertension | -0.4718 | 0.4745 | ±0.9489 | -0.994 | 0.3200 |  |
| High cholesterol | +0.3062 | 0.4440 | ±0.8880 | +0.690 | 0.4904 |  |
| Kidney disease | +0.7378 | 0.8291 | ±1.6582 | +0.890 | 0.3735 |  |
| Circulatory disease | -0.6441 | 0.6426 | ±1.2853 | -1.002 | 0.3162 |  |
| Time < 70 (%) | +0.1260 | 0.1290 | ±0.2580 | +0.976 | 0.3289 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **244**, R² = **0.0932**, Adj R² = **0.0502**, F-statistic = **2.17** (p = **0.0170**), Residual SE = **3.256** on **232** df, AIC = **1280.2**, BIC = **1322.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.5968** | 1.6104 | ±3.2207 | **+15.895** | **6.86e-57** | *** |
| Education: graduate level (vs college) | +0.3703 | 0.4573 | ±0.9147 | +0.810 | 0.4181 |  |
| Education: high school or below (vs college) | -1.8083 | 1.0785 | ±2.1570 | -1.677 | 0.0936 | . |
| Site: UCSD (vs UAB) | +0.3685 | 0.7015 | ±1.4030 | +0.525 | 0.5994 |  |
| Site: UW (vs UAB) | +0.9662 | 0.5880 | ±1.1761 | +1.643 | 0.1004 |  |
| Age (years) | -0.0318 | 0.0191 | ±0.0381 | -1.666 | 0.0958 | . |
| BMI (kg/m2) | +0.0540 | 0.0317 | ±0.0634 | +1.703 | 0.0885 | . |
| Hypertension | -0.4767 | 0.4753 | ±0.9506 | -1.003 | 0.3159 |  |
| High cholesterol | +0.3000 | 0.4464 | ±0.8929 | +0.672 | 0.5015 |  |
| Kidney disease | +0.7372 | 0.8282 | ±1.6563 | +0.890 | 0.3734 |  |
| Circulatory disease | -0.6459 | 0.6434 | ±1.2867 | -1.004 | 0.3154 |  |
| Avg. daily time < 70 (%) | +0.1092 | 0.1498 | ±0.2997 | +0.728 | 0.4663 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **244**, R² = **0.1157**, Adj R² = **0.0738**, F-statistic = **2.76** (p = **0.0022**), Residual SE = **3.215** on **232** df, AIC = **1274.1**, BIC = **1316.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20.7143** | 3.5027 | ±7.0054 | **+5.914** | **3.34e-09** | *** |
| Education: graduate level (vs college) | +0.3122 | 0.4608 | ±0.9216 | +0.677 | 0.4981 |  |
| Education: high school or below (vs college) | -1.5356 | 0.9994 | ±1.9988 | -1.536 | 0.1244 |  |
| Site: UCSD (vs UAB) | +0.2588 | 0.6890 | ±1.3780 | +0.376 | 0.7072 |  |
| Site: UW (vs UAB) | +0.8477 | 0.5728 | ±1.1456 | +1.480 | 0.1389 |  |
| Age (years) | -0.0321 | 0.0190 | ±0.0380 | -1.691 | 0.0908 | . |
| BMI (kg/m2) | +0.0574 | 0.0317 | ±0.0634 | +1.811 | 0.0701 | . |
| Hypertension | -0.5271 | 0.4727 | ±0.9455 | -1.115 | 0.2648 |  |
| High cholesterol | +0.1783 | 0.4195 | ±0.8390 | +0.425 | 0.6708 |  |
| Kidney disease | +0.7061 | 0.7971 | ±1.5942 | +0.886 | 0.3757 |  |
| Circulatory disease | -0.4066 | 0.5994 | ±1.1987 | -0.678 | 0.4975 |  |
| Time 54-250, pooled (%) | +0.0515 | 0.0314 | ±0.0627 | +1.640 | 0.1009 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **244**, R² = **0.1167**, Adj R² = **0.0748**, F-statistic = **2.79** (p = **0.0020**), Residual SE = **3.213** on **232** df, AIC = **1273.8**, BIC = **1315.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20.4808** | 3.6268 | ±7.2535 | **+5.647** | **1.63e-08** | *** |
| Education: graduate level (vs college) | +0.3161 | 0.4611 | ±0.9223 | +0.686 | 0.4930 |  |
| Education: high school or below (vs college) | -1.5213 | 0.9977 | ±1.9955 | -1.525 | 0.1273 |  |
| Site: UCSD (vs UAB) | +0.2579 | 0.6890 | ±1.3781 | +0.374 | 0.7082 |  |
| Site: UW (vs UAB) | +0.8528 | 0.5721 | ±1.1441 | +1.491 | 0.1360 |  |
| Age (years) | -0.0322 | 0.0190 | ±0.0381 | -1.691 | 0.0908 | . |
| BMI (kg/m2) | +0.0582 | 0.0316 | ±0.0632 | +1.841 | 0.0657 | . |
| Hypertension | -0.5244 | 0.4725 | ±0.9450 | -1.110 | 0.2670 |  |
| High cholesterol | +0.1745 | 0.4188 | ±0.8376 | +0.417 | 0.6769 |  |
| Kidney disease | +0.6995 | 0.7983 | ±1.5967 | +0.876 | 0.3809 |  |
| Circulatory disease | -0.3949 | 0.5983 | ±1.1965 | -0.660 | 0.5092 |  |
| Avg. daily time 54-250 (%) | +0.0535 | 0.0326 | ±0.0651 | +1.643 | 0.1004 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **244**, R² = **0.1013**, Adj R² = **0.0586**, F-statistic = **2.38** (p = **0.0084**), Residual SE = **3.241** on **232** df, AIC = **1278.0**, BIC = **1320.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.5439** | 1.5960 | ±3.1919 | **+16.005** | **1.17e-57** | *** |
| Education: graduate level (vs college) | +0.4075 | 0.4635 | ±0.9269 | +0.879 | 0.3793 |  |
| Education: high school or below (vs college) | -1.8432 | 1.0585 | ±2.1170 | -1.741 | 0.0816 | . |
| Site: UCSD (vs UAB) | +0.2885 | 0.6972 | ±1.3943 | +0.414 | 0.6790 |  |
| Site: UW (vs UAB) | +0.9244 | 0.5713 | ±1.1426 | +1.618 | 0.1056 |  |
| Age (years) | -0.0301 | 0.0189 | ±0.0377 | -1.597 | 0.1104 |  |
| **BMI (kg/m2)** | **+0.0682** | 0.0331 | ±0.0662 | **+2.059** | **0.0395** | * |
| Hypertension | -0.4364 | 0.4786 | ±0.9572 | -0.912 | 0.3618 |  |
| High cholesterol | +0.3005 | 0.4376 | ±0.8752 | +0.687 | 0.4922 |  |
| Kidney disease | +0.9317 | 0.7586 | ±1.5172 | +1.228 | 0.2194 |  |
| Circulatory disease | -0.6745 | 0.6300 | ±1.2600 | -1.071 | 0.2843 |  |
| Time 181-250, pooled (%) | -0.0375 | 0.0202 | ±0.0405 | -1.855 | 0.0636 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **244**, R² = **0.1000**, Adj R² = **0.0573**, F-statistic = **2.34** (p = **0.0094**), Residual SE = **3.244** on **232** df, AIC = **1278.4**, BIC = **1320.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.5507** | 1.5986 | ±3.1972 | **+15.983** | **1.68e-57** | *** |
| Education: graduate level (vs college) | +0.4039 | 0.4644 | ±0.9289 | +0.870 | 0.3845 |  |
| Education: high school or below (vs college) | -1.8555 | 1.0593 | ±2.1185 | -1.752 | 0.0798 | . |
| Site: UCSD (vs UAB) | +0.2808 | 0.6984 | ±1.3969 | +0.402 | 0.6877 |  |
| Site: UW (vs UAB) | +0.9137 | 0.5721 | ±1.1442 | +1.597 | 0.1103 |  |
| Age (years) | -0.0300 | 0.0188 | ±0.0377 | -1.594 | 0.1110 |  |
| **BMI (kg/m2)** | **+0.0671** | 0.0331 | ±0.0662 | **+2.026** | **0.0427** | * |
| Hypertension | -0.4408 | 0.4794 | ±0.9588 | -0.920 | 0.3578 |  |
| High cholesterol | +0.2985 | 0.4380 | ±0.8760 | +0.681 | 0.4956 |  |
| Kidney disease | +0.9272 | 0.7600 | ±1.5199 | +1.220 | 0.2225 |  |
| Circulatory disease | -0.6786 | 0.6323 | ±1.2647 | -1.073 | 0.2832 |  |
| Avg. daily time 181-250 (%) | -0.0345 | 0.0197 | ±0.0394 | -1.752 | 0.0798 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **244**, R² = **0.1206**, Adj R² = **0.0789**, F-statistic = **2.89** (p = **0.0014**), Residual SE = **3.206** on **232** df, AIC = **1272.7**, BIC = **1314.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.6578** | 1.5983 | ±3.1966 | **+16.053** | **5.42e-58** | *** |
| Education: graduate level (vs college) | +0.4120 | 0.4618 | ±0.9237 | +0.892 | 0.3724 |  |
| Education: high school or below (vs college) | -1.5832 | 0.9833 | ±1.9666 | -1.610 | 0.1074 |  |
| Site: UCSD (vs UAB) | +0.2504 | 0.6873 | ±1.3746 | +0.364 | 0.7156 |  |
| Site: UW (vs UAB) | +0.9081 | 0.5657 | ±1.1315 | +1.605 | 0.1085 |  |
| Age (years) | -0.0315 | 0.0189 | ±0.0379 | -1.666 | 0.0958 | . |
| **BMI (kg/m2)** | **+0.0704** | 0.0328 | ±0.0657 | **+2.142** | **0.0322** | * |
| Hypertension | -0.4505 | 0.4700 | ±0.9400 | -0.958 | 0.3378 |  |
| High cholesterol | +0.2635 | 0.4248 | ±0.8497 | +0.620 | 0.5351 |  |
| Kidney disease | +0.9015 | 0.7615 | ±1.5231 | +1.184 | 0.2365 |  |
| Circulatory disease | -0.4880 | 0.5930 | ±1.1860 | -0.823 | 0.4105 |  |
| **Time > 180 (%)** | **-0.0369** | 0.0161 | ±0.0321 | **-2.300** | **0.0214** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **244**, R² = **0.1188**, Adj R² = **0.0770**, F-statistic = **2.84** (p = **0.0016**), Residual SE = **3.210** on **232** df, AIC = **1273.2**, BIC = **1315.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.6375** | 1.6017 | ±3.2034 | **+16.006** | **1.15e-57** | *** |
| Education: graduate level (vs college) | +0.4128 | 0.4625 | ±0.9251 | +0.892 | 0.3721 |  |
| Education: high school or below (vs college) | -1.6058 | 0.9868 | ±1.9735 | -1.627 | 0.1037 |  |
| Site: UCSD (vs UAB) | +0.2416 | 0.6886 | ±1.3773 | +0.351 | 0.7257 |  |
| Site: UW (vs UAB) | +0.9021 | 0.5668 | ±1.1336 | +1.592 | 0.1115 |  |
| Age (years) | -0.0313 | 0.0189 | ±0.0379 | -1.653 | 0.0984 | . |
| **BMI (kg/m2)** | **+0.0700** | 0.0329 | ±0.0658 | **+2.125** | **0.0336** | * |
| Hypertension | -0.4500 | 0.4705 | ±0.9411 | -0.956 | 0.3389 |  |
| High cholesterol | +0.2642 | 0.4258 | ±0.8516 | +0.620 | 0.5350 |  |
| Kidney disease | +0.9022 | 0.7655 | ±1.5310 | +1.178 | 0.2386 |  |
| Circulatory disease | -0.4997 | 0.5949 | ±1.1899 | -0.840 | 0.4009 |  |
| **Avg. daily time > 180 (%)** | **-0.0355** | 0.0159 | ±0.0318 | **-2.232** | **0.0256** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **244**, R² = **0.1117**, Adj R² = **0.0696**, F-statistic = **2.65** (p = **0.0032**), Residual SE = **3.222** on **232** df, AIC = **1275.2**, BIC = **1317.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.5384** | 1.6051 | ±3.2103 | **+15.910** | **5.37e-57** | *** |
| Education: graduate level (vs college) | +0.3340 | 0.4575 | ±0.9150 | +0.730 | 0.4653 |  |
| Education: high school or below (vs college) | -1.7252 | 1.0160 | ±2.0321 | -1.698 | 0.0895 | . |
| Site: UCSD (vs UAB) | +0.2919 | 0.6921 | ±1.3843 | +0.422 | 0.6732 |  |
| Site: UW (vs UAB) | +0.8989 | 0.5742 | ±1.1484 | +1.566 | 0.1175 |  |
| Age (years) | -0.0326 | 0.0192 | ±0.0385 | -1.693 | 0.0904 | . |
| **BMI (kg/m2)** | **+0.0706** | 0.0332 | ±0.0665 | **+2.124** | **0.0336** | * |
| Hypertension | -0.4853 | 0.4717 | ±0.9435 | -1.029 | 0.3036 |  |
| High cholesterol | +0.2848 | 0.4329 | ±0.8658 | +0.658 | 0.5106 |  |
| Kidney disease | +0.6903 | 0.7881 | ±1.5763 | +0.876 | 0.3811 |  |
| Circulatory disease | -0.5612 | 0.6053 | ±1.2105 | -0.927 | 0.3538 |  |
| Nocturnal time > 180 (%) | -0.0297 | 0.0154 | ±0.0309 | -1.921 | 0.0548 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **244**, R² = **0.1182**, Adj R² = **0.0764**, F-statistic = **2.83** (p = **0.0017**), Residual SE = **3.211** on **232** df, AIC = **1273.4**, BIC = **1315.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.8368** | 1.5982 | ±3.1963 | **+16.166** | **8.70e-59** | *** |
| Education: graduate level (vs college) | +0.3231 | 0.4610 | ±0.9219 | +0.701 | 0.4833 |  |
| Education: high school or below (vs college) | -1.5046 | 1.0025 | ±2.0051 | -1.501 | 0.1334 |  |
| Site: UCSD (vs UAB) | +0.2682 | 0.6871 | ±1.3741 | +0.390 | 0.6962 |  |
| Site: UW (vs UAB) | +0.8634 | 0.5702 | ±1.1404 | +1.514 | 0.1300 |  |
| Age (years) | -0.0326 | 0.0190 | ±0.0380 | -1.716 | 0.0862 | . |
| BMI (kg/m2) | +0.0583 | 0.0315 | ±0.0631 | +1.847 | 0.0647 | . |
| Hypertension | -0.5221 | 0.4727 | ±0.9454 | -1.104 | 0.2694 |  |
| High cholesterol | +0.1846 | 0.4193 | ±0.8386 | +0.440 | 0.6597 |  |
| Kidney disease | +0.7058 | 0.7968 | ±1.5937 | +0.886 | 0.3758 |  |
| Circulatory disease | -0.3912 | 0.6006 | ±1.2013 | -0.651 | 0.5149 |  |
| Time > 250 (%) | -0.0540 | 0.0318 | ±0.0637 | -1.697 | 0.0897 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 244)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **244**, R² = **0.1185**, Adj R² = **0.0767**, F-statistic = **2.83** (p = **0.0017**), Residual SE = **3.210** on **232** df, AIC = **1273.3**, BIC = **1315.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.8140** | 1.5981 | ±3.1962 | **+16.153** | **1.08e-58** | *** |
| Education: graduate level (vs college) | +0.3243 | 0.4613 | ±0.9225 | +0.703 | 0.4820 |  |
| Education: high school or below (vs college) | -1.4980 | 1.0004 | ±2.0009 | -1.497 | 0.1343 |  |
| Site: UCSD (vs UAB) | +0.2657 | 0.6876 | ±1.3751 | +0.386 | 0.6992 |  |
| Site: UW (vs UAB) | +0.8672 | 0.5701 | ±1.1402 | +1.521 | 0.1282 |  |
| Age (years) | -0.0325 | 0.0190 | ±0.0380 | -1.710 | 0.0873 | . |
| BMI (kg/m2) | +0.0588 | 0.0315 | ±0.0631 | +1.865 | 0.0622 | . |
| Hypertension | -0.5201 | 0.4725 | ±0.9449 | -1.101 | 0.2710 |  |
| High cholesterol | +0.1812 | 0.4188 | ±0.8375 | +0.433 | 0.6652 |  |
| Kidney disease | +0.6987 | 0.7983 | ±1.5966 | +0.875 | 0.3814 |  |
| Circulatory disease | -0.3844 | 0.5994 | ±1.1987 | -0.641 | 0.5213 |  |
| Avg. daily time > 250 (%) | -0.0553 | 0.0328 | ±0.0656 | -1.686 | 0.0917 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 244; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0659**, LLR χ² = **21.23** (p = **0.0195**), AUC = **0.6856**, AIC = **323.1**, BIC = **361.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6660 | 1.1837 | ±2.3673 | -0.563 | 0.5737 | 0.5138 |  |
| Education: graduate level (vs college) | -0.3028 | 0.2947 | ±0.5894 | -1.028 | 0.3041 | 0.7387 |  |
| Education: high school or below (vs college) | +0.8078 | 0.5355 | ±1.0709 | +1.509 | 0.1314 | 2.2429 |  |
| Site: UCSD (vs UAB) | +0.0269 | 0.3777 | ±0.7554 | +0.071 | 0.9432 | 1.0273 |  |
| Site: UW (vs UAB) | -0.4297 | 0.3470 | ±0.6940 | -1.238 | 0.2156 | 0.6507 |  |
| Age (years) | +0.0253 | 0.0138 | ±0.0275 | +1.840 | 0.0658 | 1.0256 | . |
| **BMI (kg/m2)** | **-0.0473** | 0.0234 | ±0.0468 | **-2.020** | **0.0434** | 0.9538 | * |
| Hypertension | +0.2192 | 0.3190 | ±0.6379 | +0.687 | 0.4920 | 1.2450 |  |
| High cholesterol | +0.1396 | 0.2903 | ±0.5805 | +0.481 | 0.6305 | 1.1498 |  |
| Kidney disease | -0.7987 | 0.6092 | ±1.2183 | -1.311 | 0.1898 | 0.4499 |  |
| Circulatory disease | +0.2961 | 0.4370 | ±0.8739 | +0.678 | 0.4979 | 1.3447 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0662**, LLR χ² = **21.35** (p = **0.0299**), AUC = **0.6840**, AIC = **325.0**, BIC = **366.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9693 | 1.4809 | ±2.9617 | -0.655 | 0.5127 | 0.3793 |  |
| Education: graduate level (vs college) | -0.3037 | 0.2946 | ±0.5892 | -1.031 | 0.3026 | 0.7381 |  |
| Education: high school or below (vs college) | +0.7799 | 0.5425 | ±1.0849 | +1.438 | 0.1505 | 2.1813 |  |
| Site: UCSD (vs UAB) | +0.0263 | 0.3778 | ±0.7555 | +0.070 | 0.9445 | 1.0266 |  |
| Site: UW (vs UAB) | -0.4350 | 0.3477 | ±0.6955 | -1.251 | 0.2110 | 0.6473 |  |
| Age (years) | +0.0252 | 0.0138 | ±0.0275 | +1.834 | 0.0666 | 1.0256 | . |
| **BMI (kg/m2)** | **-0.0480** | 0.0235 | ±0.0470 | **-2.041** | **0.0412** | 0.9532 | * |
| Hypertension | +0.2173 | 0.3192 | ±0.6385 | +0.681 | 0.4960 | 1.2427 |  |
| High cholesterol | +0.1337 | 0.2909 | ±0.5818 | +0.460 | 0.6457 | 1.1431 |  |
| Kidney disease | -0.7907 | 0.6094 | ±1.2188 | -1.298 | 0.1944 | 0.4535 |  |
| Circulatory disease | +0.2690 | 0.4442 | ±0.8883 | +0.606 | 0.5447 | 1.3087 |  |
| HbA1c (%) | +0.0566 | 0.1660 | ±0.3320 | +0.341 | 0.7333 | 1.0582 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0702**, LLR χ² = **22.62** (p = **0.0200**), AUC = **0.6819**, AIC = **323.7**, BIC = **365.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3856 | 1.3357 | ±2.6714 | -1.037 | 0.2995 | 0.2502 |  |
| Education: graduate level (vs college) | -0.3370 | 0.2964 | ±0.5927 | -1.137 | 0.2554 | 0.7139 |  |
| Education: high school or below (vs college) | +0.7143 | 0.5466 | ±1.0932 | +1.307 | 0.1913 | 2.0427 |  |
| Site: UCSD (vs UAB) | +0.0398 | 0.3785 | ±0.7571 | +0.105 | 0.9164 | 1.0406 |  |
| Site: UW (vs UAB) | -0.4566 | 0.3501 | ±0.7002 | -1.304 | 0.1922 | 0.6334 |  |
| Age (years) | +0.0257 | 0.0138 | ±0.0276 | +1.866 | 0.0621 | 1.0261 | . |
| **BMI (kg/m2)** | **-0.0511** | 0.0237 | ±0.0474 | **-2.158** | **0.0310** | 0.9502 | * |
| Hypertension | +0.1976 | 0.3208 | ±0.6415 | +0.616 | 0.5380 | 1.2184 |  |
| High cholesterol | +0.1317 | 0.2916 | ±0.5833 | +0.451 | 0.6517 | 1.1407 |  |
| Kidney disease | -0.8275 | 0.6133 | ±1.2267 | -1.349 | 0.1773 | 0.4372 |  |
| Circulatory disease | +0.2329 | 0.4415 | ±0.8831 | +0.528 | 0.5978 | 1.2623 |  |
| Mean glucose (mg/dL) | +0.0061 | 0.0053 | ±0.0105 | +1.159 | 0.2465 | 1.0061 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0702**, LLR χ² = **22.62** (p = **0.0200**), AUC = **0.6819**, AIC = **323.7**, BIC = **365.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.2291 | 1.7926 | ±3.5852 | -1.243 | 0.2137 | 0.1076 |  |
| Education: graduate level (vs college) | -0.3370 | 0.2964 | ±0.5927 | -1.137 | 0.2554 | 0.7139 |  |
| Education: high school or below (vs college) | +0.7143 | 0.5466 | ±1.0932 | +1.307 | 0.1913 | 2.0427 |  |
| Site: UCSD (vs UAB) | +0.0398 | 0.3785 | ±0.7571 | +0.105 | 0.9164 | 1.0406 |  |
| Site: UW (vs UAB) | -0.4566 | 0.3501 | ±0.7002 | -1.304 | 0.1922 | 0.6334 |  |
| Age (years) | +0.0257 | 0.0138 | ±0.0276 | +1.866 | 0.0621 | 1.0261 | . |
| **BMI (kg/m2)** | **-0.0511** | 0.0237 | ±0.0474 | **-2.158** | **0.0310** | 0.9502 | * |
| Hypertension | +0.1976 | 0.3208 | ±0.6415 | +0.616 | 0.5380 | 1.2184 |  |
| High cholesterol | +0.1317 | 0.2916 | ±0.5833 | +0.451 | 0.6517 | 1.1407 |  |
| Kidney disease | -0.8275 | 0.6133 | ±1.2267 | -1.349 | 0.1773 | 0.4372 |  |
| Circulatory disease | +0.2329 | 0.4415 | ±0.8831 | +0.528 | 0.5978 | 1.2623 |  |
| GMI (%) | +0.2548 | 0.2199 | ±0.4397 | +1.159 | 0.2465 | 1.2902 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0667**, LLR χ² = **21.51** (p = **0.0285**), AUC = **0.6837**, AIC = **324.8**, BIC = **366.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9409 | 1.2954 | ±2.5909 | -0.726 | 0.4676 | 0.3903 |  |
| Education: graduate level (vs college) | -0.3128 | 0.2952 | ±0.5904 | -1.060 | 0.2893 | 0.7314 |  |
| Education: high school or below (vs college) | +0.7661 | 0.5430 | ±1.0860 | +1.411 | 0.1583 | 2.1514 |  |
| Site: UCSD (vs UAB) | +0.0279 | 0.3778 | ±0.7557 | +0.074 | 0.9411 | 1.0283 |  |
| Site: UW (vs UAB) | -0.4371 | 0.3480 | ±0.6960 | -1.256 | 0.2091 | 0.6459 |  |
| Age (years) | +0.0257 | 0.0138 | ±0.0276 | +1.863 | 0.0625 | 1.0260 | . |
| **BMI (kg/m2)** | **-0.0492** | 0.0237 | ±0.0474 | **-2.075** | **0.0379** | 0.9520 | * |
| Hypertension | +0.2104 | 0.3197 | ±0.6393 | +0.658 | 0.5104 | 1.2342 |  |
| High cholesterol | +0.1351 | 0.2907 | ±0.5814 | +0.465 | 0.6420 | 1.1447 |  |
| Kidney disease | -0.7913 | 0.6104 | ±1.2208 | -1.296 | 0.1949 | 0.4533 |  |
| Circulatory disease | +0.2732 | 0.4392 | ±0.8785 | +0.622 | 0.5339 | 1.3142 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0024 | 0.0046 | ±0.0093 | +0.520 | 0.6029 | 1.0024 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0672**, LLR χ² = **21.66** (p = **0.0272**), AUC = **0.6819**, AIC = **324.7**, BIC = **366.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9866 | 1.2833 | ±2.5665 | -0.769 | 0.4420 | 0.3728 |  |
| Education: graduate level (vs college) | -0.3048 | 0.2948 | ±0.5897 | -1.034 | 0.3012 | 0.7372 |  |
| Education: high school or below (vs college) | +0.8033 | 0.5377 | ±1.0754 | +1.494 | 0.1352 | 2.2328 |  |
| Site: UCSD (vs UAB) | +0.0482 | 0.3794 | ±0.7587 | +0.127 | 0.8990 | 1.0494 |  |
| Site: UW (vs UAB) | -0.4224 | 0.3479 | ±0.6959 | -1.214 | 0.2248 | 0.6555 |  |
| Age (years) | +0.0249 | 0.0138 | ±0.0276 | +1.806 | 0.0709 | 1.0252 | . |
| **BMI (kg/m2)** | **-0.0489** | 0.0235 | ±0.0470 | **-2.084** | **0.0372** | 0.9522 | * |
| Hypertension | +0.2015 | 0.3207 | ±0.6414 | +0.628 | 0.5299 | 1.2232 |  |
| High cholesterol | +0.1676 | 0.2938 | ±0.5875 | +0.571 | 0.5682 | 1.1825 |  |
| Kidney disease | -0.8619 | 0.6184 | ±1.2368 | -1.394 | 0.1634 | 0.4224 |  |
| Circulatory disease | +0.2625 | 0.4409 | ±0.8818 | +0.595 | 0.5516 | 1.3001 |  |
| Glucose SD, pooled (mg/dL) | +0.0127 | 0.0194 | ±0.0389 | +0.651 | 0.5151 | 1.0127 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0690**, LLR χ² = **22.25** (p = **0.0225**), AUC = **0.6805**, AIC = **324.1**, BIC = **366.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.1287 | 1.2738 | ±2.5477 | -0.886 | 0.3756 | 0.3235 |  |
| Education: graduate level (vs college) | -0.3136 | 0.2953 | ±0.5906 | -1.062 | 0.2882 | 0.7308 |  |
| Education: high school or below (vs college) | +0.8118 | 0.5390 | ±1.0779 | +1.506 | 0.1320 | 2.2519 |  |
| Site: UCSD (vs UAB) | +0.0602 | 0.3798 | ±0.7596 | +0.158 | 0.8742 | 1.0620 |  |
| Site: UW (vs UAB) | -0.4212 | 0.3484 | ±0.6969 | -1.209 | 0.2268 | 0.6563 |  |
| Age (years) | +0.0248 | 0.0138 | ±0.0276 | +1.797 | 0.0724 | 1.0251 | . |
| **BMI (kg/m2)** | **-0.0503** | 0.0235 | ±0.0470 | **-2.139** | **0.0324** | 0.9509 | * |
| Hypertension | +0.1887 | 0.3212 | ±0.6423 | +0.588 | 0.5568 | 1.2077 |  |
| High cholesterol | +0.1812 | 0.2939 | ±0.5877 | +0.616 | 0.5376 | 1.1986 |  |
| Kidney disease | -0.8954 | 0.6204 | ±1.2409 | -1.443 | 0.1490 | 0.4085 |  |
| Circulatory disease | +0.2427 | 0.4416 | ±0.8832 | +0.550 | 0.5826 | 1.2747 |  |
| Avg. daily SD (mg/dL) | +0.0207 | 0.0206 | ±0.0412 | +1.005 | 0.3147 | 1.0209 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0661**, LLR χ² = **21.32** (p = **0.0302**), AUC = **0.6865**, AIC = **325.0**, BIC = **367.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4812 | 1.3463 | ±2.6925 | -0.357 | 0.7207 | 0.6180 |  |
| Education: graduate level (vs college) | -0.3107 | 0.2959 | ±0.5919 | -1.050 | 0.2937 | 0.7329 |  |
| Education: high school or below (vs college) | +0.7884 | 0.5395 | ±1.0790 | +1.461 | 0.1439 | 2.2000 |  |
| Site: UCSD (vs UAB) | +0.0181 | 0.3789 | ±0.7579 | +0.048 | 0.9619 | 1.0183 |  |
| Site: UW (vs UAB) | -0.4407 | 0.3492 | ±0.6983 | -1.262 | 0.2069 | 0.6436 |  |
| Age (years) | +0.0256 | 0.0138 | ±0.0276 | +1.857 | 0.0633 | 1.0260 | . |
| **BMI (kg/m2)** | **-0.0472** | 0.0234 | ±0.0469 | **-2.013** | **0.0441** | 0.9539 | * |
| Hypertension | +0.2217 | 0.3190 | ±0.6381 | +0.695 | 0.4871 | 1.2482 |  |
| High cholesterol | +0.1218 | 0.2968 | ±0.5936 | +0.410 | 0.6815 | 1.1295 |  |
| Kidney disease | -0.7769 | 0.6142 | ±1.2285 | -1.265 | 0.2059 | 0.4598 |  |
| Circulatory disease | +0.2996 | 0.4368 | ±0.8736 | +0.686 | 0.4928 | 1.3493 |  |
| CV (%) | -0.0086 | 0.0298 | ±0.0596 | -0.288 | 0.7733 | 0.9915 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0668**, LLR χ² = **21.53** (p = **0.0282**), AUC = **0.6849**, AIC = **324.8**, BIC = **366.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0592 | 1.3845 | ±2.7689 | -0.765 | 0.4442 | 0.3467 |  |
| Education: graduate level (vs college) | -0.3104 | 0.2951 | ±0.5903 | -1.052 | 0.2929 | 0.7331 |  |
| Education: high school or below (vs college) | +0.7810 | 0.5378 | ±1.0757 | +1.452 | 0.1465 | 2.1837 |  |
| Site: UCSD (vs UAB) | +0.0138 | 0.3785 | ±0.7571 | +0.037 | 0.9709 | 1.0139 |  |
| Site: UW (vs UAB) | -0.4501 | 0.3494 | ±0.6988 | -1.288 | 0.1976 | 0.6375 |  |
| Age (years) | +0.0258 | 0.0138 | ±0.0276 | +1.868 | 0.0617 | 1.0261 | . |
| **BMI (kg/m2)** | **-0.0475** | 0.0235 | ±0.0469 | **-2.023** | **0.0431** | 0.9537 | * |
| Hypertension | +0.2300 | 0.3196 | ±0.6392 | +0.720 | 0.4717 | 1.2586 |  |
| High cholesterol | +0.1122 | 0.2948 | ±0.5896 | +0.381 | 0.7035 | 1.1187 |  |
| Kidney disease | -0.7673 | 0.6138 | ±1.2275 | -1.250 | 0.2113 | 0.4643 |  |
| Circulatory disease | +0.3029 | 0.4367 | ±0.8734 | +0.694 | 0.4879 | 1.3538 |  |
| Mean / SD ratio | +0.0830 | 0.1516 | ±0.3032 | +0.548 | 0.5839 | 1.0866 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0659**, LLR χ² = **21.24** (p = **0.0309**), AUC = **0.6859**, AIC = **325.1**, BIC = **367.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7343 | 1.3639 | ±2.7277 | -0.538 | 0.5903 | 0.4799 |  |
| Education: graduate level (vs college) | -0.3033 | 0.2947 | ±0.5894 | -1.029 | 0.3034 | 0.7384 |  |
| Education: high school or below (vs college) | +0.8024 | 0.5381 | ±1.0762 | +1.491 | 0.1359 | 2.2310 |  |
| Site: UCSD (vs UAB) | +0.0248 | 0.3783 | ±0.7565 | +0.066 | 0.9477 | 1.0251 |  |
| Site: UW (vs UAB) | -0.4335 | 0.3492 | ±0.6983 | -1.242 | 0.2144 | 0.6482 |  |
| Age (years) | +0.0254 | 0.0138 | ±0.0276 | +1.843 | 0.0654 | 1.0257 | . |
| **BMI (kg/m2)** | **-0.0472** | 0.0234 | ±0.0468 | **-2.017** | **0.0436** | 0.9539 | * |
| Hypertension | +0.2214 | 0.3198 | ±0.6395 | +0.692 | 0.4887 | 1.2478 |  |
| High cholesterol | +0.1349 | 0.2940 | ±0.5881 | +0.459 | 0.6464 | 1.1444 |  |
| Kidney disease | -0.7923 | 0.6127 | ±1.2253 | -1.293 | 0.1959 | 0.4528 |  |
| Circulatory disease | +0.2966 | 0.4369 | ±0.8739 | +0.679 | 0.4973 | 1.3453 |  |
| Avg. daily mean/SD | +0.0118 | 0.1168 | ±0.2336 | +0.101 | 0.9197 | 1.0118 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0659**, LLR χ² = **21.24** (p = **0.0309**), AUC = **0.6854**, AIC = **325.1**, BIC = **367.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5970 | 1.3955 | ±2.7909 | -0.428 | 0.6688 | 0.5505 |  |
| Education: graduate level (vs college) | -0.3061 | 0.2968 | ±0.5935 | -1.031 | 0.3023 | 0.7363 |  |
| Education: high school or below (vs college) | +0.8049 | 0.5362 | ±1.0724 | +1.501 | 0.1334 | 2.2364 |  |
| Site: UCSD (vs UAB) | +0.0219 | 0.3814 | ±0.7628 | +0.058 | 0.9541 | 1.0222 |  |
| Site: UW (vs UAB) | -0.4368 | 0.3553 | ±0.7105 | -1.229 | 0.2189 | 0.6461 |  |
| Age (years) | +0.0253 | 0.0138 | ±0.0275 | +1.840 | 0.0658 | 1.0256 | . |
| **BMI (kg/m2)** | **-0.0469** | 0.0237 | ±0.0474 | **-1.978** | **0.0479** | 0.9542 | * |
| Hypertension | +0.2158 | 0.3210 | ±0.6420 | +0.672 | 0.5014 | 1.2409 |  |
| High cholesterol | +0.1339 | 0.2966 | ±0.5932 | +0.451 | 0.6517 | 1.1433 |  |
| Kidney disease | -0.7981 | 0.6093 | ±1.2186 | -1.310 | 0.1902 | 0.4502 |  |
| Circulatory disease | +0.2978 | 0.4374 | ±0.8747 | +0.681 | 0.4960 | 1.3469 |  |
| MAG (mg/dL/h) | -0.0016 | 0.0167 | ±0.0333 | -0.093 | 0.9256 | 0.9984 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0665**, LLR χ² = **21.43** (p = **0.0292**), AUC = **0.6837**, AIC = **324.9**, BIC = **366.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9670 | 1.3648 | ±2.7297 | -0.708 | 0.4787 | 0.3802 |  |
| Education: graduate level (vs college) | -0.3044 | 0.2948 | ±0.5896 | -1.033 | 0.3018 | 0.7375 |  |
| Education: high school or below (vs college) | +0.8059 | 0.5364 | ±1.0728 | +1.502 | 0.1330 | 2.2387 |  |
| Site: UCSD (vs UAB) | +0.0479 | 0.3809 | ±0.7617 | +0.126 | 0.8999 | 1.0491 |  |
| Site: UW (vs UAB) | -0.4153 | 0.3489 | ±0.6978 | -1.190 | 0.2339 | 0.6602 |  |
| Age (years) | +0.0252 | 0.0138 | ±0.0276 | +1.831 | 0.0671 | 1.0255 | . |
| **BMI (kg/m2)** | **-0.0483** | 0.0235 | ±0.0470 | **-2.057** | **0.0397** | 0.9529 | * |
| Hypertension | +0.2131 | 0.3194 | ±0.6389 | +0.667 | 0.5047 | 1.2375 |  |
| High cholesterol | +0.1659 | 0.2964 | ±0.5929 | +0.560 | 0.5757 | 1.1805 |  |
| Kidney disease | -0.8281 | 0.6136 | ±1.2271 | -1.350 | 0.1771 | 0.4369 |  |
| Circulatory disease | +0.2776 | 0.4389 | ±0.8779 | +0.632 | 0.5271 | 1.3199 |  |
| Avg. daily range (mg/dL) | +0.0024 | 0.0053 | ±0.0107 | +0.445 | 0.6562 | 1.0024 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0778**, LLR χ² = **25.08** (p = **0.0089**), AUC = **0.6947**, AIC = **321.2**, BIC = **363.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3067 | 1.2130 | ±2.4259 | -0.253 | 0.8004 | 0.7359 |  |
| Education: graduate level (vs college) | -0.3333 | 0.2974 | ±0.5949 | -1.121 | 0.2625 | 0.7166 |  |
| Education: high school or below (vs college) | +0.8998 | 0.5404 | ±1.0807 | +1.665 | 0.0959 | 2.4590 | . |
| Site: UCSD (vs UAB) | -0.0022 | 0.3822 | ±0.7644 | -0.006 | 0.9954 | 0.9978 |  |
| Site: UW (vs UAB) | -0.4241 | 0.3494 | ±0.6988 | -1.214 | 0.2248 | 0.6543 |  |
| **Age (years)** | **+0.0274** | 0.0139 | ±0.0277 | **+1.976** | **0.0482** | 1.0278 | * |
| BMI (kg/m2) | -0.0450 | 0.0238 | ±0.0477 | -1.888 | 0.0590 | 0.9560 | . |
| Hypertension | +0.2213 | 0.3199 | ±0.6399 | +0.692 | 0.4891 | 1.2477 |  |
| High cholesterol | +0.1070 | 0.2929 | ±0.5857 | +0.365 | 0.7150 | 1.1129 |  |
| Kidney disease | -0.7464 | 0.6160 | ±1.2320 | -1.212 | 0.2257 | 0.4741 |  |
| Circulatory disease | +0.3294 | 0.4384 | ±0.8768 | +0.751 | 0.4524 | 1.3901 |  |
| SD of daily means (mg/dL) | -0.0620 | 0.0327 | ±0.0654 | -1.894 | 0.0583 | 0.9399 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0686**, LLR χ² = **22.12** (p = **0.0234**), AUC = **0.6814**, AIC = **324.2**, BIC = **366.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1694 | 1.4783 | ±2.9565 | +0.115 | 0.9088 | 1.1846 |  |
| Education: graduate level (vs college) | -0.3215 | 0.2955 | ±0.5910 | -1.088 | 0.2767 | 0.7251 |  |
| Education: high school or below (vs college) | +0.7527 | 0.5429 | ±1.0858 | +1.386 | 0.1656 | 2.1228 |  |
| Site: UCSD (vs UAB) | +0.0458 | 0.3786 | ±0.7573 | +0.121 | 0.9036 | 1.0469 |  |
| Site: UW (vs UAB) | -0.4348 | 0.3486 | ±0.6971 | -1.247 | 0.2123 | 0.6474 |  |
| Age (years) | +0.0255 | 0.0138 | ±0.0276 | +1.853 | 0.0639 | 1.0259 | . |
| **BMI (kg/m2)** | **-0.0508** | 0.0237 | ±0.0474 | **-2.144** | **0.0320** | 0.9505 | * |
| Hypertension | +0.2083 | 0.3201 | ±0.6402 | +0.651 | 0.5151 | 1.2316 |  |
| High cholesterol | +0.1442 | 0.2911 | ±0.5821 | +0.495 | 0.6203 | 1.1551 |  |
| Kidney disease | -0.8534 | 0.6157 | ±1.2314 | -1.386 | 0.1657 | 0.4259 |  |
| Circulatory disease | +0.2635 | 0.4392 | ±0.8783 | +0.600 | 0.5485 | 1.3015 |  |
| Time in range 70-180, pooled (%) | -0.0085 | 0.0090 | ±0.0179 | -0.945 | 0.3448 | 0.9916 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0683**, LLR χ² = **22.02** (p = **0.0242**), AUC = **0.6815**, AIC = **324.3**, BIC = **366.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1171 | 1.4772 | ±2.9544 | +0.079 | 0.9368 | 1.1243 |  |
| Education: graduate level (vs college) | -0.3215 | 0.2956 | ±0.5911 | -1.088 | 0.2767 | 0.7251 |  |
| Education: high school or below (vs college) | +0.7584 | 0.5423 | ±1.0847 | +1.398 | 0.1620 | 2.1348 |  |
| Site: UCSD (vs UAB) | +0.0468 | 0.3787 | ±0.7573 | +0.124 | 0.9015 | 1.0480 |  |
| Site: UW (vs UAB) | -0.4336 | 0.3484 | ±0.6969 | -1.244 | 0.2133 | 0.6482 |  |
| Age (years) | +0.0255 | 0.0138 | ±0.0275 | +1.849 | 0.0644 | 1.0258 | . |
| **BMI (kg/m2)** | **-0.0506** | 0.0237 | ±0.0474 | **-2.136** | **0.0327** | 0.9506 | * |
| Hypertension | +0.2088 | 0.3200 | ±0.6400 | +0.652 | 0.5141 | 1.2322 |  |
| High cholesterol | +0.1435 | 0.2910 | ±0.5820 | +0.493 | 0.6220 | 1.1543 |  |
| Kidney disease | -0.8518 | 0.6155 | ±1.2311 | -1.384 | 0.1664 | 0.4266 |  |
| Circulatory disease | +0.2671 | 0.4389 | ±0.8778 | +0.608 | 0.5429 | 1.3061 |  |
| Avg. daily time in range 70-180 (%) | -0.0079 | 0.0089 | ±0.0177 | -0.887 | 0.3749 | 0.9922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0786**, LLR χ² = **25.33** (p = **0.0081**), AUC = **0.7056**, AIC = **321.0**, BIC = **363.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6111 | 1.1903 | ±2.3806 | -0.513 | 0.6077 | 0.5428 |  |
| Education: graduate level (vs college) | -0.3680 | 0.2991 | ±0.5982 | -1.230 | 0.2186 | 0.6921 |  |
| Education: high school or below (vs college) | +0.7346 | 0.5388 | ±1.0777 | +1.363 | 0.1728 | 2.0847 |  |
| Site: UCSD (vs UAB) | +0.0282 | 0.3810 | ±0.7620 | +0.074 | 0.9410 | 1.0286 |  |
| Site: UW (vs UAB) | -0.4786 | 0.3506 | ±0.7012 | -1.365 | 0.1722 | 0.6197 |  |
| Age (years) | +0.0268 | 0.0140 | ±0.0279 | +1.919 | 0.0549 | 1.0271 | . |
| BMI (kg/m2) | -0.0436 | 0.0233 | ±0.0466 | -1.871 | 0.0614 | 0.9574 | . |
| Hypertension | +0.2022 | 0.3195 | ±0.6389 | +0.633 | 0.5268 | 1.2241 |  |
| High cholesterol | +0.0982 | 0.2934 | ±0.5868 | +0.335 | 0.7378 | 1.1032 |  |
| Kidney disease | -0.7877 | 0.6207 | ±1.2415 | -1.269 | 0.2045 | 0.4549 |  |
| Circulatory disease | +0.3269 | 0.4396 | ±0.8792 | +0.744 | 0.4571 | 1.3866 |  |
| **Any reading < 54 during wear (0/1)** | **-0.6651** | 0.3358 | ±0.6717 | **-1.980** | **0.0477** | 0.5142 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0720**, LLR χ² = **23.21** (p = **0.0165**), AUC = **0.6967**, AIC = **323.1**, BIC = **365.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5607 | 1.1875 | ±2.3751 | -0.472 | 0.6368 | 0.5708 |  |
| Education: graduate level (vs college) | -0.3456 | 0.2966 | ±0.5932 | -1.165 | 0.2439 | 0.7078 |  |
| Education: high school or below (vs college) | +0.7556 | 0.5390 | ±1.0781 | +1.402 | 0.1610 | 2.1289 |  |
| Site: UCSD (vs UAB) | -0.0144 | 0.3804 | ±0.7609 | -0.038 | 0.9699 | 0.9857 |  |
| Site: UW (vs UAB) | -0.4977 | 0.3511 | ±0.7022 | -1.418 | 0.1563 | 0.6079 |  |
| Age (years) | +0.0269 | 0.0139 | ±0.0277 | +1.944 | 0.0519 | 1.0273 | . |
| **BMI (kg/m2)** | **-0.0498** | 0.0237 | ±0.0474 | **-2.102** | **0.0355** | 0.9514 | * |
| Hypertension | +0.1961 | 0.3200 | ±0.6400 | +0.613 | 0.5400 | 1.2167 |  |
| High cholesterol | +0.0992 | 0.2926 | ±0.5852 | +0.339 | 0.7346 | 1.1043 |  |
| Kidney disease | -0.8022 | 0.6083 | ±1.2165 | -1.319 | 0.1872 | 0.4483 |  |
| Circulatory disease | +0.2860 | 0.4371 | ±0.8741 | +0.654 | 0.5129 | 1.3311 |  |
| Time < 54 (%) | -0.2875 | 0.3140 | ±0.6281 | -0.915 | 0.3600 | 0.7502 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0686**, LLR χ² = **22.10** (p = **0.0236**), AUC = **0.6909**, AIC = **324.2**, BIC = **366.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5861 | 1.1863 | ±2.3725 | -0.494 | 0.6212 | 0.5565 |  |
| Education: graduate level (vs college) | -0.3296 | 0.2962 | ±0.5924 | -1.113 | 0.2658 | 0.7192 |  |
| Education: high school or below (vs college) | +0.7756 | 0.5380 | ±1.0760 | +1.442 | 0.1494 | 2.1718 |  |
| Site: UCSD (vs UAB) | -0.0061 | 0.3797 | ±0.7595 | -0.016 | 0.9871 | 0.9939 |  |
| Site: UW (vs UAB) | -0.4822 | 0.3518 | ±0.7035 | -1.371 | 0.1704 | 0.6174 |  |
| Age (years) | +0.0263 | 0.0138 | ±0.0276 | +1.903 | 0.0570 | 1.0267 | . |
| **BMI (kg/m2)** | **-0.0491** | 0.0236 | ±0.0472 | **-2.082** | **0.0373** | 0.9521 | * |
| Hypertension | +0.2036 | 0.3198 | ±0.6397 | +0.637 | 0.5244 | 1.2258 |  |
| High cholesterol | +0.1083 | 0.2927 | ±0.5854 | +0.370 | 0.7115 | 1.1143 |  |
| Kidney disease | -0.7987 | 0.6084 | ±1.2168 | -1.313 | 0.1893 | 0.4499 |  |
| Circulatory disease | +0.2915 | 0.4371 | ±0.8742 | +0.667 | 0.5049 | 1.3384 |  |
| Avg. daily time < 54 (%) | -0.1870 | 0.2224 | ±0.4448 | -0.841 | 0.4004 | 0.8294 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0659**, LLR χ² = **21.24** (p = **0.0310**), AUC = **0.6856**, AIC = **325.1**, BIC = **367.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6672 | 1.1841 | ±2.3682 | -0.563 | 0.5731 | 0.5131 |  |
| Education: graduate level (vs college) | -0.2999 | 0.2970 | ±0.5940 | -1.010 | 0.3127 | 0.7409 |  |
| Education: high school or below (vs college) | +0.8120 | 0.5381 | ±1.0762 | +1.509 | 0.1313 | 2.2525 |  |
| Site: UCSD (vs UAB) | +0.0287 | 0.3784 | ±0.7568 | +0.076 | 0.9396 | 1.0291 |  |
| Site: UW (vs UAB) | -0.4260 | 0.3501 | ±0.7003 | -1.217 | 0.2237 | 0.6531 |  |
| Age (years) | +0.0253 | 0.0138 | ±0.0276 | +1.834 | 0.0666 | 1.0256 | . |
| **BMI (kg/m2)** | **-0.0475** | 0.0236 | ±0.0471 | **-2.016** | **0.0439** | 0.9536 | * |
| Hypertension | +0.2207 | 0.3196 | ±0.6391 | +0.691 | 0.4899 | 1.2469 |  |
| High cholesterol | +0.1430 | 0.2933 | ±0.5867 | +0.488 | 0.6259 | 1.1537 |  |
| Kidney disease | -0.7995 | 0.6093 | ±1.2187 | -1.312 | 0.1895 | 0.4495 |  |
| Circulatory disease | +0.2971 | 0.4372 | ±0.8743 | +0.680 | 0.4968 | 1.3459 |  |
| Time 54-69, pooled (%) | +0.0089 | 0.1109 | ±0.2218 | +0.081 | 0.9358 | 1.0090 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0660**, LLR χ² = **21.27** (p = **0.0307**), AUC = **0.6857**, AIC = **325.1**, BIC = **367.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6699 | 1.1846 | ±2.3693 | -0.566 | 0.5717 | 0.5117 |  |
| Education: graduate level (vs college) | -0.2958 | 0.2971 | ±0.5942 | -0.996 | 0.3194 | 0.7439 |  |
| Education: high school or below (vs college) | +0.8182 | 0.5385 | ±1.0769 | +1.520 | 0.1286 | 2.2665 |  |
| Site: UCSD (vs UAB) | +0.0315 | 0.3786 | ±0.7572 | +0.083 | 0.9337 | 1.0320 |  |
| Site: UW (vs UAB) | -0.4201 | 0.3509 | ±0.7018 | -1.197 | 0.2312 | 0.6570 |  |
| Age (years) | +0.0252 | 0.0138 | ±0.0276 | +1.828 | 0.0675 | 1.0255 | . |
| **BMI (kg/m2)** | **-0.0477** | 0.0235 | ±0.0471 | **-2.026** | **0.0427** | 0.9534 | * |
| Hypertension | +0.2228 | 0.3196 | ±0.6393 | +0.697 | 0.4857 | 1.2496 |  |
| High cholesterol | +0.1480 | 0.2937 | ±0.5874 | +0.504 | 0.6142 | 1.1596 |  |
| Kidney disease | -0.8007 | 0.6095 | ±1.2191 | -1.314 | 0.1890 | 0.4490 |  |
| Circulatory disease | +0.2988 | 0.4373 | ±0.8746 | +0.683 | 0.4944 | 1.3483 |  |
| Avg. daily time 54-69 (%) | +0.0197 | 0.1035 | ±0.2070 | +0.190 | 0.8493 | 1.0199 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0672**, LLR χ² = **21.65** (p = **0.0273**), AUC = **0.6908**, AIC = **324.7**, BIC = **366.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6257 | 1.1839 | ±2.3677 | -0.529 | 0.5971 | 0.5349 |  |
| Education: graduate level (vs college) | -0.3285 | 0.2973 | ±0.5946 | -1.105 | 0.2691 | 0.7200 |  |
| Education: high school or below (vs college) | +0.7755 | 0.5383 | ±1.0765 | +1.441 | 0.1497 | 2.1716 |  |
| Site: UCSD (vs UAB) | +0.0063 | 0.3790 | ±0.7581 | +0.017 | 0.9867 | 1.0063 |  |
| Site: UW (vs UAB) | -0.4657 | 0.3514 | ±0.7027 | -1.325 | 0.1851 | 0.6277 |  |
| Age (years) | +0.0260 | 0.0138 | ±0.0276 | +1.881 | 0.0600 | 1.0263 | . |
| **BMI (kg/m2)** | **-0.0472** | 0.0234 | ±0.0468 | **-2.017** | **0.0437** | 0.9539 | * |
| Hypertension | +0.2066 | 0.3196 | ±0.6393 | +0.646 | 0.5181 | 1.2295 |  |
| High cholesterol | +0.1127 | 0.2935 | ±0.5870 | +0.384 | 0.7011 | 1.1193 |  |
| Kidney disease | -0.7957 | 0.6088 | ±1.2175 | -1.307 | 0.1912 | 0.4513 |  |
| Circulatory disease | +0.2894 | 0.4370 | ±0.8741 | +0.662 | 0.5079 | 1.3356 |  |
| Time < 70 (%) | -0.0497 | 0.0804 | ±0.1608 | -0.619 | 0.5362 | 0.9515 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0661**, LLR χ² = **21.29** (p = **0.0305**), AUC = **0.6861**, AIC = **325.0**, BIC = **367.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6533 | 1.1840 | ±2.3680 | -0.552 | 0.5811 | 0.5203 |  |
| Education: graduate level (vs college) | -0.3120 | 0.2971 | ±0.5942 | -1.050 | 0.2936 | 0.7320 |  |
| Education: high school or below (vs college) | +0.7951 | 0.5382 | ±1.0763 | +1.477 | 0.1396 | 2.2146 |  |
| Site: UCSD (vs UAB) | +0.0194 | 0.3789 | ±0.7578 | +0.051 | 0.9591 | 1.0196 |  |
| Site: UW (vs UAB) | -0.4439 | 0.3519 | ±0.7038 | -1.261 | 0.2072 | 0.6416 |  |
| Age (years) | +0.0255 | 0.0138 | ±0.0276 | +1.852 | 0.0641 | 1.0259 | . |
| **BMI (kg/m2)** | **-0.0471** | 0.0234 | ±0.0468 | **-2.015** | **0.0439** | 0.9540 | * |
| Hypertension | +0.2143 | 0.3196 | ±0.6392 | +0.671 | 0.5025 | 1.2390 |  |
| High cholesterol | +0.1286 | 0.2939 | ±0.5878 | +0.438 | 0.6616 | 1.1373 |  |
| Kidney disease | -0.7970 | 0.6089 | ±1.2178 | -1.309 | 0.1906 | 0.4507 |  |
| Circulatory disease | +0.2932 | 0.4371 | ±0.8742 | +0.671 | 0.5023 | 1.3407 |  |
| Avg. daily time < 70 (%) | -0.0186 | 0.0787 | ±0.1575 | -0.236 | 0.8132 | 0.9816 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0662**, LLR χ² = **21.34** (p = **0.0300**), AUC = **0.6841**, AIC = **325.0**, BIC = **366.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2256 | 1.7837 | ±3.5675 | -0.126 | 0.8993 | 0.7980 |  |
| Education: graduate level (vs college) | -0.3025 | 0.2946 | ±0.5892 | -1.027 | 0.3045 | 0.7390 |  |
| Education: high school or below (vs college) | +0.7801 | 0.5427 | ±1.0854 | +1.437 | 0.1506 | 2.1817 |  |
| Site: UCSD (vs UAB) | +0.0321 | 0.3780 | ±0.7560 | +0.085 | 0.9323 | 1.0326 |  |
| Site: UW (vs UAB) | -0.4269 | 0.3474 | ±0.6948 | -1.229 | 0.2192 | 0.6525 |  |
| Age (years) | +0.0254 | 0.0138 | ±0.0275 | +1.848 | 0.0647 | 1.0258 | . |
| **BMI (kg/m2)** | **-0.0474** | 0.0234 | ±0.0468 | **-2.027** | **0.0427** | 0.9537 | * |
| Hypertension | +0.2208 | 0.3191 | ±0.6383 | +0.692 | 0.4890 | 1.2471 |  |
| High cholesterol | +0.1455 | 0.2910 | ±0.5821 | +0.500 | 0.6171 | 1.1566 |  |
| Kidney disease | -0.7961 | 0.6089 | ±1.2177 | -1.308 | 0.1910 | 0.4511 |  |
| Circulatory disease | +0.2742 | 0.4419 | ±0.8837 | +0.621 | 0.5348 | 1.3155 |  |
| Time 54-250, pooled (%) | -0.0046 | 0.0138 | ±0.0277 | -0.330 | 0.7411 | 0.9954 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0663**, LLR χ² = **21.36** (p = **0.0299**), AUC = **0.6841**, AIC = **325.0**, BIC = **366.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1898 | 1.8133 | ±3.6265 | -0.105 | 0.9166 | 0.8271 |  |
| Education: graduate level (vs college) | -0.3028 | 0.2946 | ±0.5892 | -1.028 | 0.3039 | 0.7387 |  |
| Education: high school or below (vs college) | +0.7781 | 0.5430 | ±1.0861 | +1.433 | 0.1519 | 2.1773 |  |
| Site: UCSD (vs UAB) | +0.0322 | 0.3780 | ±0.7559 | +0.085 | 0.9320 | 1.0328 |  |
| Site: UW (vs UAB) | -0.4274 | 0.3474 | ±0.6948 | -1.230 | 0.2186 | 0.6522 |  |
| Age (years) | +0.0254 | 0.0138 | ±0.0275 | +1.848 | 0.0646 | 1.0258 | . |
| **BMI (kg/m2)** | **-0.0475** | 0.0234 | ±0.0468 | **-2.030** | **0.0424** | 0.9536 | * |
| Hypertension | +0.2206 | 0.3191 | ±0.6383 | +0.691 | 0.4894 | 1.2469 |  |
| High cholesterol | +0.1460 | 0.2911 | ±0.5822 | +0.502 | 0.6160 | 1.1572 |  |
| Kidney disease | -0.7955 | 0.6088 | ±1.2177 | -1.307 | 0.1913 | 0.4513 |  |
| Circulatory disease | +0.2726 | 0.4421 | ±0.8842 | +0.616 | 0.5376 | 1.3133 |  |
| Avg. daily time 54-250 (%) | -0.0049 | 0.0141 | ±0.0283 | -0.347 | 0.7285 | 0.9951 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0701**, LLR χ² = **22.60** (p = **0.0201**), AUC = **0.6842**, AIC = **323.7**, BIC = **365.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6235 | 1.1827 | ±2.3655 | -0.527 | 0.5981 | 0.5361 |  |
| Education: graduate level (vs college) | -0.3466 | 0.2977 | ±0.5954 | -1.164 | 0.2443 | 0.7071 |  |
| Education: high school or below (vs college) | +0.7823 | 0.5382 | ±1.0764 | +1.453 | 0.1461 | 2.1864 |  |
| Site: UCSD (vs UAB) | +0.0472 | 0.3789 | ±0.7577 | +0.125 | 0.9008 | 1.0483 |  |
| Site: UW (vs UAB) | -0.4537 | 0.3493 | ±0.6985 | -1.299 | 0.1939 | 0.6352 |  |
| Age (years) | +0.0253 | 0.0138 | ±0.0276 | +1.835 | 0.0666 | 1.0256 | . |
| **BMI (kg/m2)** | **-0.0532** | 0.0239 | ±0.0478 | **-2.227** | **0.0259** | 0.9481 | * |
| Hypertension | +0.1906 | 0.3210 | ±0.6419 | +0.594 | 0.5527 | 1.2099 |  |
| High cholesterol | +0.1189 | 0.2919 | ±0.5839 | +0.407 | 0.6838 | 1.1263 |  |
| Kidney disease | -0.9204 | 0.6276 | ±1.2552 | -1.467 | 0.1425 | 0.3983 |  |
| Circulatory disease | +0.3121 | 0.4390 | ±0.8781 | +0.711 | 0.4772 | 1.3663 |  |
| Time 181-250, pooled (%) | +0.0169 | 0.0144 | ±0.0287 | +1.175 | 0.2401 | 1.0170 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0692**, LLR χ² = **22.31** (p = **0.0221**), AUC = **0.6838**, AIC = **324.0**, BIC = **366.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6243 | 1.1832 | ±2.3663 | -0.528 | 0.5977 | 0.5356 |  |
| Education: graduate level (vs college) | -0.3422 | 0.2976 | ±0.5952 | -1.150 | 0.2501 | 0.7102 |  |
| Education: high school or below (vs college) | +0.7894 | 0.5377 | ±1.0755 | +1.468 | 0.1421 | 2.2022 |  |
| Site: UCSD (vs UAB) | +0.0485 | 0.3789 | ±0.7578 | +0.128 | 0.8981 | 1.0497 |  |
| Site: UW (vs UAB) | -0.4482 | 0.3489 | ±0.6978 | -1.285 | 0.1989 | 0.6388 |  |
| Age (years) | +0.0252 | 0.0138 | ±0.0276 | +1.832 | 0.0669 | 1.0256 | . |
| **BMI (kg/m2)** | **-0.0525** | 0.0239 | ±0.0478 | **-2.195** | **0.0282** | 0.9489 | * |
| Hypertension | +0.1944 | 0.3208 | ±0.6416 | +0.606 | 0.5446 | 1.2146 |  |
| High cholesterol | +0.1203 | 0.2918 | ±0.5836 | +0.412 | 0.6802 | 1.1278 |  |
| Kidney disease | -0.9084 | 0.6263 | ±1.2527 | -1.450 | 0.1470 | 0.4032 |  |
| Circulatory disease | +0.3119 | 0.4386 | ±0.8773 | +0.711 | 0.4771 | 1.3660 |  |
| Avg. daily time 181-250 (%) | +0.0146 | 0.0140 | ±0.0279 | +1.043 | 0.2968 | 1.0147 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0691**, LLR χ² = **22.26** (p = **0.0224**), AUC = **0.6810**, AIC = **324.1**, BIC = **366.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6700 | 1.1828 | ±2.3656 | -0.566 | 0.5711 | 0.5117 |  |
| Education: graduate level (vs college) | -0.3277 | 0.2959 | ±0.5918 | -1.107 | 0.2681 | 0.7206 |  |
| Education: high school or below (vs college) | +0.7439 | 0.5438 | ±1.0877 | +1.368 | 0.1713 | 2.1041 |  |
| Site: UCSD (vs UAB) | +0.0428 | 0.3785 | ±0.7570 | +0.113 | 0.9100 | 1.0437 |  |
| Site: UW (vs UAB) | -0.4423 | 0.3489 | ±0.6978 | -1.268 | 0.2049 | 0.6425 |  |
| Age (years) | +0.0257 | 0.0138 | ±0.0276 | +1.863 | 0.0625 | 1.0260 | . |
| **BMI (kg/m2)** | **-0.0510** | 0.0237 | ±0.0473 | **-2.155** | **0.0312** | 0.9503 | * |
| Hypertension | +0.2050 | 0.3203 | ±0.6406 | +0.640 | 0.5221 | 1.2275 |  |
| High cholesterol | +0.1394 | 0.2912 | ±0.5823 | +0.479 | 0.6321 | 1.1496 |  |
| Kidney disease | -0.8568 | 0.6159 | ±1.2318 | -1.391 | 0.1642 | 0.4245 |  |
| Circulatory disease | +0.2600 | 0.4394 | ±0.8788 | +0.592 | 0.5540 | 1.2969 |  |
| Time > 180 (%) | +0.0090 | 0.0089 | ±0.0178 | +1.015 | 0.3103 | 1.0091 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0684**, LLR χ² = **22.06** (p = **0.0239**), AUC = **0.6812**, AIC = **324.3**, BIC = **366.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6633 | 1.1829 | ±2.3658 | -0.561 | 0.5750 | 0.5151 |  |
| Education: graduate level (vs college) | -0.3259 | 0.2959 | ±0.5918 | -1.101 | 0.2708 | 0.7219 |  |
| Education: high school or below (vs college) | +0.7522 | 0.5429 | ±1.0859 | +1.385 | 0.1660 | 2.1216 |  |
| Site: UCSD (vs UAB) | +0.0438 | 0.3785 | ±0.7569 | +0.116 | 0.9078 | 1.0448 |  |
| Site: UW (vs UAB) | -0.4400 | 0.3487 | ±0.6973 | -1.262 | 0.2069 | 0.6440 |  |
| Age (years) | +0.0256 | 0.0138 | ±0.0275 | +1.856 | 0.0634 | 1.0259 | . |
| **BMI (kg/m2)** | **-0.0506** | 0.0237 | ±0.0474 | **-2.138** | **0.0325** | 0.9506 | * |
| Hypertension | +0.2064 | 0.3202 | ±0.6403 | +0.645 | 0.5191 | 1.2292 |  |
| High cholesterol | +0.1387 | 0.2910 | ±0.5821 | +0.477 | 0.6336 | 1.1488 |  |
| Kidney disease | -0.8522 | 0.6154 | ±1.2308 | -1.385 | 0.1661 | 0.4265 |  |
| Circulatory disease | +0.2652 | 0.4390 | ±0.8781 | +0.604 | 0.5458 | 1.3037 |  |
| Avg. daily time > 180 (%) | +0.0080 | 0.0088 | ±0.0176 | +0.910 | 0.3626 | 1.0081 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0659**, LLR χ² = **21.24** (p = **0.0310**), AUC = **0.6852**, AIC = **325.1**, BIC = **367.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6666 | 1.1839 | ±2.3677 | -0.563 | 0.5734 | 0.5134 |  |
| Education: graduate level (vs college) | -0.3024 | 0.2948 | ±0.5897 | -1.026 | 0.3050 | 0.7390 |  |
| Education: high school or below (vs college) | +0.8099 | 0.5376 | ±1.0753 | +1.506 | 0.1320 | 2.2476 |  |
| Site: UCSD (vs UAB) | +0.0263 | 0.3780 | ±0.7559 | +0.070 | 0.9445 | 1.0267 |  |
| Site: UW (vs UAB) | -0.4296 | 0.3470 | ±0.6940 | -1.238 | 0.2157 | 0.6508 |  |
| Age (years) | +0.0253 | 0.0138 | ±0.0276 | +1.836 | 0.0663 | 1.0256 | . |
| **BMI (kg/m2)** | **-0.0471** | 0.0237 | ±0.0474 | **-1.988** | **0.0468** | 0.9540 | * |
| Hypertension | +0.2195 | 0.3191 | ±0.6381 | +0.688 | 0.4915 | 1.2454 |  |
| High cholesterol | +0.1399 | 0.2903 | ±0.5807 | +0.482 | 0.6300 | 1.1501 |  |
| Kidney disease | -0.7986 | 0.6091 | ±1.2181 | -1.311 | 0.1898 | 0.4499 |  |
| Circulatory disease | +0.2973 | 0.4379 | ±0.8758 | +0.679 | 0.4971 | 1.3463 |  |
| Nocturnal time > 180 (%) | -0.0004 | 0.0087 | ±0.0174 | -0.042 | 0.9667 | 0.9996 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0665**, LLR χ² = **21.45** (p = **0.0290**), AUC = **0.6828**, AIC = **324.9**, BIC = **366.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6851 | 1.1844 | ±2.3688 | -0.578 | 0.5630 | 0.5040 |  |
| Education: graduate level (vs college) | -0.3038 | 0.2946 | ±0.5891 | -1.031 | 0.3025 | 0.7380 |  |
| Education: high school or below (vs college) | +0.7695 | 0.5433 | ±1.0866 | +1.416 | 0.1567 | 2.1587 |  |
| Site: UCSD (vs UAB) | +0.0319 | 0.3779 | ±0.7558 | +0.084 | 0.9328 | 1.0324 |  |
| Site: UW (vs UAB) | -0.4286 | 0.3475 | ±0.6950 | -1.233 | 0.2175 | 0.6514 |  |
| Age (years) | +0.0255 | 0.0138 | ±0.0276 | +1.855 | 0.0636 | 1.0259 | . |
| **BMI (kg/m2)** | **-0.0476** | 0.0234 | ±0.0468 | **-2.034** | **0.0419** | 0.9535 | * |
| Hypertension | +0.2205 | 0.3192 | ±0.6384 | +0.691 | 0.4897 | 1.2467 |  |
| High cholesterol | +0.1468 | 0.2910 | ±0.5821 | +0.504 | 0.6140 | 1.1581 |  |
| Kidney disease | -0.7951 | 0.6088 | ±1.2175 | -1.306 | 0.1915 | 0.4515 |  |
| Circulatory disease | +0.2650 | 0.4422 | ±0.8844 | +0.599 | 0.5489 | 1.3035 |  |
| Time > 250 (%) | +0.0064 | 0.0140 | ±0.0280 | +0.457 | 0.6476 | 1.0064 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 244)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **244**, events = **91**, McFadden pseudo-R² = **0.0664**, LLR χ² = **21.41** (p = **0.0294**), AUC = **0.6833**, AIC = **324.9**, BIC = **366.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6811 | 1.1842 | ±2.3683 | -0.575 | 0.5652 | 0.5061 |  |
| Education: graduate level (vs college) | -0.3038 | 0.2946 | ±0.5891 | -1.031 | 0.3024 | 0.7380 |  |
| Education: high school or below (vs college) | +0.7719 | 0.5434 | ±1.0869 | +1.420 | 0.1555 | 2.1638 |  |
| Site: UCSD (vs UAB) | +0.0319 | 0.3779 | ±0.7557 | +0.084 | 0.9328 | 1.0324 |  |
| Site: UW (vs UAB) | -0.4290 | 0.3475 | ±0.6949 | -1.235 | 0.2170 | 0.6512 |  |
| Age (years) | +0.0255 | 0.0138 | ±0.0275 | +1.852 | 0.0640 | 1.0258 | . |
| **BMI (kg/m2)** | **-0.0476** | 0.0234 | ±0.0468 | **-2.034** | **0.0419** | 0.9535 | * |
| Hypertension | +0.2203 | 0.3192 | ±0.6383 | +0.690 | 0.4901 | 1.2465 |  |
| High cholesterol | +0.1463 | 0.2910 | ±0.5820 | +0.503 | 0.6151 | 1.1576 |  |
| Kidney disease | -0.7948 | 0.6087 | ±1.2175 | -1.306 | 0.1917 | 0.4517 |  |
| Circulatory disease | +0.2675 | 0.4423 | ±0.8846 | +0.605 | 0.5453 | 1.3067 |  |
| Avg. daily time > 250 (%) | +0.0059 | 0.0142 | ±0.0285 | +0.415 | 0.6778 | 1.0059 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 244; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **244**, R² = **0.0817**, Adj R² = **0.0422**, F-statistic = **2.07** (p = **0.0275**), Residual SE = **2.743** on **233** df, AIC = **1195.7**, BIC = **1234.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.3898** | 1.3505 | ±2.7011 | **+10.655** | **1.65e-26** | *** |
| Education: graduate level (vs college) | -0.2180 | 0.3777 | ±0.7554 | -0.577 | 0.5639 |  |
| Education: high school or below (vs college) | -1.1506 | 0.9186 | ±1.8373 | -1.253 | 0.2104 |  |
| Site: UCSD (vs UAB) | +0.9766 | 0.5526 | ±1.1051 | +1.767 | 0.0771 | . |
| Site: UW (vs UAB) | +1.0135 | 0.5359 | ±1.0719 | +1.891 | 0.0586 | . |
| **Age (years)** | **-0.0415** | 0.0169 | ±0.0339 | **-2.449** | **0.0143** | * |
| BMI (kg/m2) | +0.0155 | 0.0274 | ±0.0549 | +0.566 | 0.5712 |  |
| Hypertension | -0.4224 | 0.4069 | ±0.8137 | -1.038 | 0.2992 |  |
| High cholesterol | +0.0816 | 0.3587 | ±0.7174 | +0.228 | 0.8200 |  |
| Kidney disease | +0.3075 | 0.5271 | ±1.0542 | +0.583 | 0.5596 |  |
| Circulatory disease | -0.0028 | 0.5085 | ±1.0169 | -0.005 | 0.9957 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **244**, R² = **0.0978**, Adj R² = **0.0550**, F-statistic = **2.29** (p = **0.0114**), Residual SE = **2.725** on **232** df, AIC = **1193.3**, BIC = **1235.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.5863** | 1.5222 | ±3.0443 | **+10.897** | **1.20e-27** | *** |
| Education: graduate level (vs college) | -0.2135 | 0.3784 | ±0.7568 | -0.564 | 0.5725 |  |
| Education: high school or below (vs college) | -0.9274 | 0.9143 | ±1.8286 | -1.014 | 0.3104 |  |
| Site: UCSD (vs UAB) | +0.9764 | 0.5487 | ±1.0974 | +1.779 | 0.0752 | . |
| Site: UW (vs UAB) | +1.0433 | 0.5331 | ±1.0663 | +1.957 | 0.0504 | . |
| **Age (years)** | **-0.0410** | 0.0169 | ±0.0337 | **-2.430** | **0.0151** | * |
| BMI (kg/m2) | +0.0206 | 0.0283 | ±0.0566 | +0.729 | 0.4662 |  |
| Hypertension | -0.4117 | 0.4020 | ±0.8040 | -1.024 | 0.3057 |  |
| High cholesterol | +0.1301 | 0.3542 | ±0.7084 | +0.367 | 0.7135 |  |
| Kidney disease | +0.2382 | 0.5075 | ±1.0149 | +0.469 | 0.6389 |  |
| Circulatory disease | +0.1985 | 0.4909 | ±0.9818 | +0.404 | 0.6859 |  |
| **HbA1c (%)** | **-0.4089** | 0.1789 | ±0.3579 | **-2.285** | **0.0223** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **244**, R² = **0.1117**, Adj R² = **0.0696**, F-statistic = **2.65** (p = **0.0032**), Residual SE = **2.704** on **232** df, AIC = **1189.5**, BIC = **1231.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4259** | 1.3783 | ±2.7565 | **+11.918** | **9.55e-33** | *** |
| Education: graduate level (vs college) | -0.1175 | 0.3776 | ±0.7551 | -0.311 | 0.7557 |  |
| Education: high school or below (vs college) | -0.8228 | 0.8931 | ±1.7861 | -0.921 | 0.3569 |  |
| Site: UCSD (vs UAB) | +0.9212 | 0.5394 | ±1.0789 | +1.708 | 0.0877 | . |
| **Site: UW (vs UAB)** | **+1.0559** | 0.5295 | ±1.0590 | **+1.994** | **0.0461** | * |
| **Age (years)** | **-0.0421** | 0.0169 | ±0.0339 | **-2.488** | **0.0128** | * |
| BMI (kg/m2) | +0.0258 | 0.0286 | ±0.0572 | +0.903 | 0.3665 |  |
| Hypertension | -0.3686 | 0.4029 | ±0.8057 | -0.915 | 0.3602 |  |
| High cholesterol | +0.1213 | 0.3519 | ±0.7038 | +0.345 | 0.7304 |  |
| Kidney disease | +0.3332 | 0.4867 | ±0.9734 | +0.685 | 0.4935 |  |
| Circulatory disease | +0.2008 | 0.4863 | ±0.9726 | +0.413 | 0.6796 |  |
| **Mean glucose (mg/dL)** | **-0.0173** | 0.0049 | ±0.0098 | **-3.549** | **3.87e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **244**, R² = **0.1117**, Adj R² = **0.0696**, F-statistic = **2.65** (p = **0.0032**), Residual SE = **2.704** on **232** df, AIC = **1189.5**, BIC = **1231.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.8221** | 1.6719 | ±3.3437 | **+11.258** | **2.11e-29** | *** |
| Education: graduate level (vs college) | -0.1175 | 0.3776 | ±0.7551 | -0.311 | 0.7557 |  |
| Education: high school or below (vs college) | -0.8228 | 0.8931 | ±1.7861 | -0.921 | 0.3569 |  |
| Site: UCSD (vs UAB) | +0.9212 | 0.5394 | ±1.0789 | +1.708 | 0.0877 | . |
| **Site: UW (vs UAB)** | **+1.0559** | 0.5295 | ±1.0590 | **+1.994** | **0.0461** | * |
| **Age (years)** | **-0.0421** | 0.0169 | ±0.0339 | **-2.488** | **0.0128** | * |
| BMI (kg/m2) | +0.0258 | 0.0286 | ±0.0572 | +0.903 | 0.3665 |  |
| Hypertension | -0.3686 | 0.4029 | ±0.8057 | -0.915 | 0.3602 |  |
| High cholesterol | +0.1213 | 0.3519 | ±0.7038 | +0.345 | 0.7304 |  |
| Kidney disease | +0.3332 | 0.4867 | ±0.9734 | +0.685 | 0.4935 |  |
| Circulatory disease | +0.2008 | 0.4863 | ±0.9726 | +0.413 | 0.6796 |  |
| **GMI (%)** | **-0.7239** | 0.2040 | ±0.4080 | **-3.549** | **3.87e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **244**, R² = **0.1105**, Adj R² = **0.0683**, F-statistic = **2.62** (p = **0.0036**), Residual SE = **2.706** on **232** df, AIC = **1189.9**, BIC = **1231.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1171** | 1.3508 | ±2.7017 | **+11.931** | **8.14e-33** | *** |
| Education: graduate level (vs college) | -0.1533 | 0.3771 | ±0.7542 | -0.407 | 0.6843 |  |
| Education: high school or below (vs college) | -0.8672 | 0.8942 | ±1.7884 | -0.970 | 0.3322 |  |
| Site: UCSD (vs UAB) | +0.9657 | 0.5435 | ±1.0870 | +1.777 | 0.0756 | . |
| **Site: UW (vs UAB)** | **+1.0443** | 0.5296 | ±1.0592 | **+1.972** | **0.0486** | * |
| **Age (years)** | **-0.0435** | 0.0170 | ±0.0340 | **-2.560** | **0.0105** | * |
| BMI (kg/m2) | +0.0282 | 0.0290 | ±0.0579 | +0.974 | 0.3299 |  |
| Hypertension | -0.3714 | 0.4051 | ±0.8101 | -0.917 | 0.3591 |  |
| High cholesterol | +0.1268 | 0.3545 | ±0.7090 | +0.358 | 0.7206 |  |
| Kidney disease | +0.2069 | 0.4945 | ±0.9890 | +0.418 | 0.6757 |  |
| Circulatory disease | +0.1582 | 0.4845 | ±0.9690 | +0.327 | 0.7439 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0153** | 0.0046 | ±0.0091 | **-3.352** | **8.04e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **244**, R² = **0.0871**, Adj R² = **0.0438**, F-statistic = **2.01** (p = **0.0281**), Residual SE = **2.741** on **232** df, AIC = **1196.2**, BIC = **1238.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.0932** | 1.4594 | ±2.9189 | **+10.342** | **4.56e-25** | *** |
| Education: graduate level (vs college) | -0.2107 | 0.3769 | ±0.7537 | -0.559 | 0.5761 |  |
| Education: high school or below (vs college) | -1.1393 | 0.9014 | ±1.8028 | -1.264 | 0.2063 |  |
| Site: UCSD (vs UAB) | +0.9288 | 0.5511 | ±1.1022 | +1.685 | 0.0919 | . |
| Site: UW (vs UAB) | +0.9970 | 0.5358 | ±1.0717 | +1.861 | 0.0628 | . |
| **Age (years)** | **-0.0406** | 0.0170 | ±0.0341 | **-2.384** | **0.0171** | * |
| BMI (kg/m2) | +0.0201 | 0.0283 | ±0.0566 | +0.712 | 0.4767 |  |
| Hypertension | -0.3923 | 0.4070 | ±0.8140 | -0.964 | 0.3352 |  |
| High cholesterol | +0.0255 | 0.3584 | ±0.7168 | +0.071 | 0.9432 |  |
| Kidney disease | +0.4372 | 0.5241 | ±1.0483 | +0.834 | 0.4042 |  |
| Circulatory disease | +0.0849 | 0.5071 | ±1.0141 | +0.167 | 0.8670 |  |
| Glucose SD, pooled (mg/dL) | -0.0287 | 0.0234 | ±0.0468 | -1.227 | 0.2199 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **244**, R² = **0.0889**, Adj R² = **0.0458**, F-statistic = **2.06** (p = **0.0242**), Residual SE = **2.738** on **232** df, AIC = **1195.7**, BIC = **1237.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.1429** | 1.4429 | ±2.8859 | **+10.494** | **9.17e-26** | *** |
| Education: graduate level (vs college) | -0.1980 | 0.3745 | ±0.7490 | -0.529 | 0.5971 |  |
| Education: high school or below (vs college) | -1.1551 | 0.9031 | ±1.8061 | -1.279 | 0.2009 |  |
| Site: UCSD (vs UAB) | +0.9221 | 0.5471 | ±1.0941 | +1.686 | 0.0919 | . |
| Site: UW (vs UAB) | +0.9972 | 0.5346 | ±1.0692 | +1.865 | 0.0621 | . |
| **Age (years)** | **-0.0406** | 0.0170 | ±0.0340 | **-2.389** | **0.0169** | * |
| BMI (kg/m2) | +0.0216 | 0.0285 | ±0.0571 | +0.758 | 0.4484 |  |
| Hypertension | -0.3818 | 0.4077 | ±0.8154 | -0.936 | 0.3491 |  |
| High cholesterol | +0.0185 | 0.3577 | ±0.7155 | +0.052 | 0.9588 |  |
| Kidney disease | +0.4510 | 0.5250 | ±1.0500 | +0.859 | 0.3903 |  |
| Circulatory disease | +0.1015 | 0.5106 | ±1.0213 | +0.199 | 0.8425 |  |
| Avg. daily SD (mg/dL) | -0.0350 | 0.0256 | ±0.0512 | -1.370 | 0.1708 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **244**, R² = **0.0852**, Adj R² = **0.0418**, F-statistic = **1.96** (p = **0.0329**), Residual SE = **2.744** on **232** df, AIC = **1196.7**, BIC = **1238.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13.6381** | 1.6104 | ±3.2208 | **+8.469** | **2.48e-17** | *** |
| Education: graduate level (vs college) | -0.1861 | 0.3866 | ±0.7731 | -0.481 | 0.6302 |  |
| Education: high school or below (vs college) | -1.0709 | 0.9286 | ±1.8573 | -1.153 | 0.2488 |  |
| Site: UCSD (vs UAB) | +1.0123 | 0.5585 | ±1.1171 | +1.812 | 0.0699 | . |
| Site: UW (vs UAB) | +1.0531 | 0.5434 | ±1.0868 | +1.938 | 0.0526 | . |
| **Age (years)** | **-0.0427** | 0.0171 | ±0.0343 | **-2.491** | **0.0128** | * |
| BMI (kg/m2) | +0.0145 | 0.0274 | ±0.0548 | +0.530 | 0.5962 |  |
| Hypertension | -0.4260 | 0.4073 | ±0.8146 | -1.046 | 0.2956 |  |
| High cholesterol | +0.1537 | 0.3712 | ±0.7425 | +0.414 | 0.6788 |  |
| Kidney disease | +0.2096 | 0.5356 | ±1.0712 | +0.391 | 0.6956 |  |
| Circulatory disease | -0.0180 | 0.5100 | ±1.0200 | -0.035 | 0.9719 |  |
| CV (%) | +0.0355 | 0.0354 | ±0.0709 | +1.000 | 0.3171 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **244**, R² = **0.0883**, Adj R² = **0.0451**, F-statistic = **2.04** (p = **0.0255**), Residual SE = **2.739** on **232** df, AIC = **1195.9**, BIC = **1237.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.5910** | 1.5594 | ±3.1188 | **+9.998** | **1.56e-23** | *** |
| Education: graduate level (vs college) | -0.1964 | 0.3826 | ±0.7653 | -0.513 | 0.6077 |  |
| Education: high school or below (vs college) | -1.0685 | 0.9249 | ±1.8498 | -1.155 | 0.2480 |  |
| Site: UCSD (vs UAB) | +1.0166 | 0.5560 | ±1.1120 | +1.828 | 0.0675 | . |
| **Site: UW (vs UAB)** | **+1.0651** | 0.5424 | ±1.0847 | **+1.964** | **0.0495** | * |
| **Age (years)** | **-0.0427** | 0.0171 | ±0.0341 | **-2.503** | **0.0123** | * |
| BMI (kg/m2) | +0.0150 | 0.0274 | ±0.0548 | +0.548 | 0.5834 |  |
| Hypertension | -0.4434 | 0.4051 | ±0.8103 | -1.094 | 0.2738 |  |
| High cholesterol | +0.1631 | 0.3652 | ±0.7304 | +0.446 | 0.6552 |  |
| Kidney disease | +0.1895 | 0.5336 | ±1.0672 | +0.355 | 0.7225 |  |
| Circulatory disease | -0.0218 | 0.5086 | ±1.0171 | -0.043 | 0.9658 |  |
| Mean / SD ratio | -0.2491 | 0.1919 | ±0.3838 | -1.298 | 0.1942 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **244**, R² = **0.0839**, Adj R² = **0.0404**, F-statistic = **1.93** (p = **0.0365**), Residual SE = **2.746** on **232** df, AIC = **1197.1**, BIC = **1239.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.0430** | 1.5608 | ±3.1215 | **+9.638** | **5.51e-22** | *** |
| Education: graduate level (vs college) | -0.2136 | 0.3809 | ±0.7617 | -0.561 | 0.5749 |  |
| Education: high school or below (vs college) | -1.1013 | 0.9258 | ±1.8516 | -1.190 | 0.2342 |  |
| Site: UCSD (vs UAB) | +0.9957 | 0.5539 | ±1.1078 | +1.798 | 0.0722 | . |
| Site: UW (vs UAB) | +1.0462 | 0.5421 | ±1.0842 | +1.930 | 0.0536 | . |
| **Age (years)** | **-0.0424** | 0.0171 | ±0.0341 | **-2.483** | **0.0130** | * |
| BMI (kg/m2) | +0.0146 | 0.0274 | ±0.0549 | +0.534 | 0.5937 |  |
| Hypertension | -0.4375 | 0.4061 | ±0.8122 | -1.077 | 0.2813 |  |
| High cholesterol | +0.1263 | 0.3624 | ±0.7249 | +0.348 | 0.7276 |  |
| Kidney disease | +0.2382 | 0.5330 | ±1.0661 | +0.447 | 0.6550 |  |
| Circulatory disease | -0.0082 | 0.5093 | ±1.0186 | -0.016 | 0.9871 |  |
| Avg. daily mean/SD | -0.1107 | 0.1513 | ±0.3025 | -0.732 | 0.4642 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **244**, R² = **0.0868**, Adj R² = **0.0435**, F-statistic = **2.00** (p = **0.0289**), Residual SE = **2.742** on **232** df, AIC = **1196.3**, BIC = **1238.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.4282** | 1.7229 | ±3.4459 | **+8.955** | **3.41e-19** | *** |
| Education: graduate level (vs college) | -0.2617 | 0.3913 | ±0.7826 | -0.669 | 0.5036 |  |
| Education: high school or below (vs college) | -1.1913 | 0.8997 | ±1.7993 | -1.324 | 0.1855 |  |
| Site: UCSD (vs UAB) | +0.9011 | 0.5517 | ±1.1033 | +1.633 | 0.1024 |  |
| Site: UW (vs UAB) | +0.9098 | 0.5390 | ±1.0781 | +1.688 | 0.0914 | . |
| **Age (years)** | **-0.0414** | 0.0170 | ±0.0340 | **-2.439** | **0.0147** | * |
| BMI (kg/m2) | +0.0214 | 0.0274 | ±0.0548 | +0.780 | 0.4355 |  |
| Hypertension | -0.4770 | 0.4142 | ±0.8284 | -1.151 | 0.2495 |  |
| High cholesterol | -0.0077 | 0.3643 | ±0.7286 | -0.021 | 0.9832 |  |
| Kidney disease | +0.3058 | 0.5386 | ±1.0771 | +0.568 | 0.5701 |  |
| Circulatory disease | +0.0339 | 0.5174 | ±1.0348 | +0.065 | 0.9478 |  |
| MAG (mg/dL/h) | -0.0238 | 0.0237 | ±0.0475 | -1.004 | 0.3156 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **244**, R² = **0.0838**, Adj R² = **0.0404**, F-statistic = **1.93** (p = **0.0366**), Residual SE = **2.746** on **232** df, AIC = **1197.1**, BIC = **1239.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.0094** | 1.6324 | ±3.2649 | **+9.194** | **3.77e-20** | *** |
| Education: graduate level (vs college) | -0.2121 | 0.3767 | ±0.7533 | -0.563 | 0.5734 |  |
| Education: high school or below (vs college) | -1.1494 | 0.9105 | ±1.8210 | -1.262 | 0.2068 |  |
| Site: UCSD (vs UAB) | +0.9328 | 0.5496 | ±1.0991 | +1.697 | 0.0896 | . |
| Site: UW (vs UAB) | +0.9841 | 0.5354 | ±1.0708 | +1.838 | 0.0661 | . |
| **Age (years)** | **-0.0414** | 0.0170 | ±0.0340 | **-2.431** | **0.0151** | * |
| BMI (kg/m2) | +0.0182 | 0.0279 | ±0.0557 | +0.652 | 0.5141 |  |
| Hypertension | -0.4151 | 0.4086 | ±0.8172 | -1.016 | 0.3097 |  |
| High cholesterol | +0.0282 | 0.3632 | ±0.7264 | +0.078 | 0.9380 |  |
| Kidney disease | +0.3595 | 0.5333 | ±1.0665 | +0.674 | 0.5002 |  |
| Circulatory disease | +0.0424 | 0.5168 | ±1.0337 | +0.082 | 0.9347 |  |
| Avg. daily range (mg/dL) | -0.0050 | 0.0073 | ±0.0147 | -0.678 | 0.4976 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **244**, R² = **0.0820**, Adj R² = **0.0384**, F-statistic = **1.88** (p = **0.0424**), Residual SE = **2.749** on **232** df, AIC = **1197.6**, BIC = **1239.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.3378** | 1.3561 | ±2.7123 | **+10.573** | **4.00e-26** | *** |
| Education: graduate level (vs college) | -0.2126 | 0.3765 | ±0.7530 | -0.565 | 0.5722 |  |
| Education: high school or below (vs college) | -1.1603 | 0.9318 | ±1.8635 | -1.245 | 0.2130 |  |
| Site: UCSD (vs UAB) | +0.9801 | 0.5552 | ±1.1105 | +1.765 | 0.0775 | . |
| Site: UW (vs UAB) | +1.0110 | 0.5364 | ±1.0728 | +1.885 | 0.0595 | . |
| **Age (years)** | **-0.0419** | 0.0171 | ±0.0342 | **-2.447** | **0.0144** | * |
| BMI (kg/m2) | +0.0147 | 0.0279 | ±0.0557 | +0.529 | 0.5969 |  |
| Hypertension | -0.4219 | 0.4086 | ±0.8171 | -1.033 | 0.3018 |  |
| High cholesterol | +0.0859 | 0.3608 | ±0.7216 | +0.238 | 0.8118 |  |
| Kidney disease | +0.2982 | 0.5293 | ±1.0586 | +0.563 | 0.5732 |  |
| Circulatory disease | -0.0075 | 0.5127 | ±1.0253 | -0.015 | 0.9883 |  |
| SD of daily means (mg/dL) | +0.0108 | 0.0381 | ±0.0761 | +0.283 | 0.7771 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **244**, R² = **0.1044**, Adj R² = **0.0620**, F-statistic = **2.46** (p = **0.0063**), Residual SE = **2.715** on **232** df, AIC = **1191.5**, BIC = **1233.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7236** | 1.7144 | ±3.4287 | **+6.838** | **8.01e-12** | *** |
| Education: graduate level (vs college) | -0.1618 | 0.3765 | ±0.7531 | -0.430 | 0.6674 |  |
| Education: high school or below (vs college) | -0.9501 | 0.8844 | ±1.7688 | -1.074 | 0.2827 |  |
| Site: UCSD (vs UAB) | +0.9111 | 0.5440 | ±1.0881 | +1.675 | 0.0940 | . |
| Site: UW (vs UAB) | +1.0101 | 0.5318 | ±1.0636 | +1.900 | 0.0575 | . |
| **Age (years)** | **-0.0419** | 0.0169 | ±0.0339 | **-2.474** | **0.0133** | * |
| BMI (kg/m2) | +0.0269 | 0.0291 | ±0.0583 | +0.924 | 0.3557 |  |
| Hypertension | -0.3908 | 0.4021 | ±0.8041 | -0.972 | 0.3310 |  |
| High cholesterol | +0.0860 | 0.3519 | ±0.7038 | +0.244 | 0.8070 |  |
| Kidney disease | +0.4223 | 0.4803 | ±0.9606 | +0.879 | 0.3793 |  |
| Circulatory disease | +0.1205 | 0.4873 | ±0.9746 | +0.247 | 0.8046 |  |
| **Time in range 70-180, pooled (%)** | **+0.0268** | 0.0090 | ±0.0180 | **+2.969** | **0.0030** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **244**, R² = **0.1041**, Adj R² = **0.0616**, F-statistic = **2.45** (p = **0.0065**), Residual SE = **2.715** on **232** df, AIC = **1191.6**, BIC = **1233.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7523** | 1.7236 | ±3.4473 | **+6.818** | **9.21e-12** | *** |
| Education: graduate level (vs college) | -0.1584 | 0.3767 | ±0.7533 | -0.421 | 0.6740 |  |
| Education: high school or below (vs college) | -0.9617 | 0.8853 | ±1.7706 | -1.086 | 0.2774 |  |
| Site: UCSD (vs UAB) | +0.9044 | 0.5446 | ±1.0891 | +1.661 | 0.0967 | . |
| Site: UW (vs UAB) | +1.0059 | 0.5319 | ±1.0637 | +1.891 | 0.0586 | . |
| **Age (years)** | **-0.0418** | 0.0169 | ±0.0339 | **-2.465** | **0.0137** | * |
| BMI (kg/m2) | +0.0270 | 0.0291 | ±0.0582 | +0.926 | 0.3547 |  |
| Hypertension | -0.3894 | 0.4023 | ±0.8046 | -0.968 | 0.3331 |  |
| High cholesterol | +0.0864 | 0.3520 | ±0.7040 | +0.246 | 0.8060 |  |
| Kidney disease | +0.4256 | 0.4810 | ±0.9620 | +0.885 | 0.3762 |  |
| Circulatory disease | +0.1145 | 0.4869 | ±0.9739 | +0.235 | 0.8141 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.0263** | 0.0090 | ±0.0180 | **+2.928** | **0.0034** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **244**, R² = **0.0886**, Adj R² = **0.0454**, F-statistic = **2.05** (p = **0.0248**), Residual SE = **2.739** on **232** df, AIC = **1195.8**, BIC = **1237.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.3136** | 1.3590 | ±2.7181 | **+10.532** | **6.14e-26** | *** |
| Education: graduate level (vs college) | -0.1693 | 0.3753 | ±0.7506 | -0.451 | 0.6520 |  |
| Education: high school or below (vs college) | -1.0734 | 0.9093 | ±1.8185 | -1.181 | 0.2378 |  |
| Site: UCSD (vs UAB) | +0.9787 | 0.5525 | ±1.1050 | +1.771 | 0.0765 | . |
| Site: UW (vs UAB) | +1.0469 | 0.5438 | ±1.0875 | +1.925 | 0.0542 | . |
| **Age (years)** | **-0.0423** | 0.0170 | ±0.0341 | **-2.486** | **0.0129** | * |
| BMI (kg/m2) | +0.0127 | 0.0276 | ±0.0552 | +0.460 | 0.6455 |  |
| Hypertension | -0.4120 | 0.4112 | ±0.8225 | -1.002 | 0.3164 |  |
| High cholesterol | +0.1218 | 0.3604 | ±0.7208 | +0.338 | 0.7355 |  |
| Kidney disease | +0.2603 | 0.5268 | ±1.0536 | +0.494 | 0.6212 |  |
| Circulatory disease | -0.0146 | 0.4992 | ±0.9984 | -0.029 | 0.9766 |  |
| Any reading < 54 during wear (0/1) | +0.5359 | 0.3884 | ±0.7767 | +1.380 | 0.1676 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **244**, R² = **0.0822**, Adj R² = **0.0387**, F-statistic = **1.89** (p = **0.0417**), Residual SE = **2.748** on **232** df, AIC = **1197.5**, BIC = **1239.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.3474** | 1.3640 | ±2.7280 | **+10.519** | **7.09e-26** | *** |
| Education: graduate level (vs college) | -0.2038 | 0.3791 | ±0.7583 | -0.538 | 0.5908 |  |
| Education: high school or below (vs college) | -1.1334 | 0.9237 | ±1.8474 | -1.227 | 0.2198 |  |
| Site: UCSD (vs UAB) | +0.9930 | 0.5632 | ±1.1264 | +1.763 | 0.0779 | . |
| Site: UW (vs UAB) | +1.0361 | 0.5488 | ±1.0976 | +1.888 | 0.0590 | . |
| **Age (years)** | **-0.0420** | 0.0171 | ±0.0342 | **-2.454** | **0.0141** | * |
| BMI (kg/m2) | +0.0165 | 0.0279 | ±0.0558 | +0.591 | 0.5543 |  |
| Hypertension | -0.4145 | 0.4087 | ±0.8175 | -1.014 | 0.3106 |  |
| High cholesterol | +0.0934 | 0.3629 | ±0.7258 | +0.257 | 0.7968 |  |
| Kidney disease | +0.3096 | 0.5284 | ±1.0568 | +0.586 | 0.5580 |  |
| Circulatory disease | +0.0005 | 0.5095 | ±1.0190 | +0.001 | 0.9992 |  |
| Time < 54 (%) | +0.0691 | 0.3449 | ±0.6897 | +0.200 | 0.8413 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **244**, R² = **0.0821**, Adj R² = **0.0385**, F-statistic = **1.89** (p = **0.0421**), Residual SE = **2.749** on **232** df, AIC = **1197.6**, BIC = **1239.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.3554** | 1.3609 | ±2.7218 | **+10.548** | **5.17e-26** | *** |
| Education: graduate level (vs college) | -0.2062 | 0.3788 | ±0.7577 | -0.544 | 0.5863 |  |
| Education: high school or below (vs college) | -1.1348 | 0.9234 | ±1.8467 | -1.229 | 0.2191 |  |
| Site: UCSD (vs UAB) | +0.9911 | 0.5629 | ±1.1258 | +1.761 | 0.0783 | . |
| Site: UW (vs UAB) | +1.0360 | 0.5510 | ±1.1021 | +1.880 | 0.0601 | . |
| **Age (years)** | **-0.0419** | 0.0171 | ±0.0342 | **-2.449** | **0.0143** | * |
| BMI (kg/m2) | +0.0162 | 0.0277 | ±0.0555 | +0.585 | 0.5586 |  |
| Hypertension | -0.4150 | 0.4091 | ±0.8182 | -1.014 | 0.3104 |  |
| High cholesterol | +0.0944 | 0.3640 | ±0.7280 | +0.259 | 0.7954 |  |
| Kidney disease | +0.3087 | 0.5284 | ±1.0568 | +0.584 | 0.5591 |  |
| Circulatory disease | -0.0007 | 0.5097 | ±1.0193 | -0.001 | 0.9989 |  |
| Avg. daily time < 54 (%) | +0.0801 | 0.1845 | ±0.3689 | +0.434 | 0.6642 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **244**, R² = **0.0844**, Adj R² = **0.0410**, F-statistic = **1.94** (p = **0.0349**), Residual SE = **2.745** on **232** df, AIC = **1196.9**, BIC = **1238.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.3609** | 1.3531 | ±2.7061 | **+10.614** | **2.58e-26** | *** |
| Education: graduate level (vs college) | -0.1772 | 0.3793 | ±0.7586 | -0.467 | 0.6403 |  |
| Education: high school or below (vs college) | -1.0956 | 0.9260 | ±1.8521 | -1.183 | 0.2368 |  |
| Site: UCSD (vs UAB) | +0.9996 | 0.5591 | ±1.1182 | +1.788 | 0.0738 | . |
| Site: UW (vs UAB) | +1.0593 | 0.5468 | ±1.0935 | +1.937 | 0.0527 | . |
| **Age (years)** | **-0.0421** | 0.0170 | ±0.0340 | **-2.479** | **0.0132** | * |
| BMI (kg/m2) | +0.0134 | 0.0276 | ±0.0552 | +0.486 | 0.6267 |  |
| Hypertension | -0.4065 | 0.4091 | ±0.8182 | -0.993 | 0.3205 |  |
| High cholesterol | +0.1263 | 0.3663 | ±0.7327 | +0.345 | 0.7302 |  |
| Kidney disease | +0.2967 | 0.5300 | ±1.0599 | +0.560 | 0.5755 |  |
| Circulatory disease | +0.0102 | 0.5089 | ±1.0177 | +0.020 | 0.9840 |  |
| Time 54-69, pooled (%) | +0.1188 | 0.0715 | ±0.1430 | +1.662 | 0.0965 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **244**, R² = **0.0837**, Adj R² = **0.0402**, F-statistic = **1.93** (p = **0.0371**), Residual SE = **2.746** on **232** df, AIC = **1197.1**, BIC = **1239.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.3637** | 1.3537 | ±2.7073 | **+10.611** | **2.65e-26** | *** |
| Education: graduate level (vs college) | -0.1826 | 0.3793 | ±0.7585 | -0.481 | 0.6302 |  |
| Education: high school or below (vs college) | -1.1009 | 0.9279 | ±1.8558 | -1.186 | 0.2355 |  |
| Site: UCSD (vs UAB) | +0.9977 | 0.5598 | ±1.1195 | +1.782 | 0.0747 | . |
| Site: UW (vs UAB) | +1.0570 | 0.5490 | ±1.0980 | +1.925 | 0.0542 | . |
| **Age (years)** | **-0.0421** | 0.0170 | ±0.0340 | **-2.476** | **0.0133** | * |
| BMI (kg/m2) | +0.0140 | 0.0276 | ±0.0552 | +0.508 | 0.6116 |  |
| Hypertension | -0.4079 | 0.4095 | ±0.8191 | -0.996 | 0.3193 |  |
| High cholesterol | +0.1218 | 0.3675 | ±0.7350 | +0.331 | 0.7403 |  |
| Kidney disease | +0.2987 | 0.5291 | ±1.0582 | +0.565 | 0.5723 |  |
| Circulatory disease | +0.0106 | 0.5098 | ±1.0196 | +0.021 | 0.9835 |  |
| Avg. daily time 54-69 (%) | +0.0967 | 0.0599 | ±0.1199 | +1.613 | 0.1068 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **244**, R² = **0.0838**, Adj R² = **0.0404**, F-statistic = **1.93** (p = **0.0366**), Residual SE = **2.746** on **232** df, AIC = **1197.1**, BIC = **1239.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.3290** | 1.3597 | ±2.7195 | **+10.538** | **5.77e-26** | *** |
| Education: graduate level (vs college) | -0.1791 | 0.3798 | ±0.7596 | -0.472 | 0.6371 |  |
| Education: high school or below (vs college) | -1.1001 | 0.9270 | ±1.8540 | -1.187 | 0.2353 |  |
| Site: UCSD (vs UAB) | +1.0071 | 0.5640 | ±1.1280 | +1.786 | 0.0741 | . |
| Site: UW (vs UAB) | +1.0640 | 0.5521 | ±1.1041 | +1.927 | 0.0539 | . |
| **Age (years)** | **-0.0423** | 0.0171 | ±0.0341 | **-2.483** | **0.0130** | * |
| BMI (kg/m2) | +0.0153 | 0.0276 | ±0.0551 | +0.554 | 0.5796 |  |
| Hypertension | -0.4047 | 0.4095 | ±0.8191 | -0.988 | 0.3230 |  |
| High cholesterol | +0.1204 | 0.3668 | ±0.7335 | +0.328 | 0.7426 |  |
| Kidney disease | +0.3032 | 0.5299 | ±1.0598 | +0.572 | 0.5672 |  |
| Circulatory disease | +0.0083 | 0.5096 | ±1.0193 | +0.016 | 0.9869 |  |
| Time < 70 (%) | +0.0710 | 0.0504 | ±0.1008 | +1.407 | 0.1594 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **244**, R² = **0.0833**, Adj R² = **0.0398**, F-statistic = **1.92** (p = **0.0382**), Residual SE = **2.747** on **232** df, AIC = **1197.2**, BIC = **1239.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.3459** | 1.3571 | ±2.7142 | **+10.571** | **4.07e-26** | *** |
| Education: graduate level (vs college) | -0.1858 | 0.3795 | ±0.7590 | -0.490 | 0.6245 |  |
| Education: high school or below (vs college) | -1.1060 | 0.9279 | ±1.8559 | -1.192 | 0.2333 |  |
| Site: UCSD (vs UAB) | +1.0017 | 0.5630 | ±1.1260 | +1.779 | 0.0752 | . |
| Site: UW (vs UAB) | +1.0594 | 0.5531 | ±1.1062 | +1.915 | 0.0555 | . |
| **Age (years)** | **-0.0422** | 0.0171 | ±0.0341 | **-2.474** | **0.0134** | * |
| BMI (kg/m2) | +0.0151 | 0.0275 | ±0.0550 | +0.548 | 0.5834 |  |
| Hypertension | -0.4072 | 0.4099 | ±0.8198 | -0.993 | 0.3205 |  |
| High cholesterol | +0.1177 | 0.3680 | ±0.7359 | +0.320 | 0.7491 |  |
| Kidney disease | +0.3027 | 0.5293 | ±1.0585 | +0.572 | 0.5673 |  |
| Circulatory disease | +0.0075 | 0.5102 | ±1.0204 | +0.015 | 0.9883 |  |
| Avg. daily time < 70 (%) | +0.0627 | 0.0463 | ±0.0927 | +1.354 | 0.1759 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **244**, R² = **0.1048**, Adj R² = **0.0624**, F-statistic = **2.47** (p = **0.0061**), Residual SE = **2.714** on **232** df, AIC = **1191.4**, BIC = **1233.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4654** | 1.8280 | ±3.6560 | **+5.725** | **1.03e-08** | *** |
| Education: graduate level (vs college) | -0.2196 | 0.3766 | ±0.7531 | -0.583 | 0.5597 |  |
| Education: high school or below (vs college) | -0.8733 | 0.8917 | ±1.7834 | -0.979 | 0.3274 |  |
| Site: UCSD (vs UAB) | +0.9243 | 0.5440 | ±1.0881 | +1.699 | 0.0893 | . |
| Site: UW (vs UAB) | +0.9829 | 0.5332 | ±1.0665 | +1.843 | 0.0653 | . |
| **Age (years)** | **-0.0428** | 0.0168 | ±0.0337 | **-2.541** | **0.0110** | * |
| BMI (kg/m2) | +0.0176 | 0.0274 | ±0.0548 | +0.641 | 0.5213 |  |
| Hypertension | -0.4413 | 0.3993 | ±0.7986 | -1.105 | 0.2690 |  |
| High cholesterol | +0.0350 | 0.3496 | ±0.6992 | +0.100 | 0.9203 |  |
| Kidney disease | +0.2764 | 0.5021 | ±1.0042 | +0.550 | 0.5820 |  |
| Circulatory disease | +0.2008 | 0.4974 | ±0.9948 | +0.404 | 0.6864 |  |
| **Time 54-250, pooled (%)** | **+0.0407** | 0.0118 | ±0.0235 | **+3.462** | **5.36e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **244**, R² = **0.1051**, Adj R² = **0.0627**, F-statistic = **2.48** (p = **0.0059**), Residual SE = **2.714** on **232** df, AIC = **1191.3**, BIC = **1233.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.3276** | 1.8518 | ±3.7036 | **+5.577** | **2.45e-08** | *** |
| Education: graduate level (vs college) | -0.2165 | 0.3765 | ±0.7530 | -0.575 | 0.5652 |  |
| Education: high school or below (vs college) | -0.8652 | 0.8925 | ±1.7850 | -0.969 | 0.3323 |  |
| Site: UCSD (vs UAB) | +0.9243 | 0.5441 | ±1.0881 | +1.699 | 0.0894 | . |
| Site: UW (vs UAB) | +0.9872 | 0.5330 | ±1.0660 | +1.852 | 0.0640 | . |
| **Age (years)** | **-0.0428** | 0.0168 | ±0.0337 | **-2.542** | **0.0110** | * |
| BMI (kg/m2) | +0.0182 | 0.0274 | ±0.0549 | +0.663 | 0.5074 |  |
| Hypertension | -0.4390 | 0.3993 | ±0.7986 | -1.100 | 0.2715 |  |
| High cholesterol | +0.0325 | 0.3495 | ±0.6989 | +0.093 | 0.9259 |  |
| Kidney disease | +0.2715 | 0.5028 | ±1.0056 | +0.540 | 0.5892 |  |
| Circulatory disease | +0.2076 | 0.4975 | ±0.9949 | +0.417 | 0.6764 |  |
| **Avg. daily time 54-250 (%)** | **+0.0419** | 0.0120 | ±0.0239 | **+3.499** | **4.68e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **244**, R² = **0.0897**, Adj R² = **0.0465**, F-statistic = **2.08** (p = **0.0228**), Residual SE = **2.737** on **232** df, AIC = **1195.5**, BIC = **1237.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.2995** | 1.3706 | ±2.7413 | **+10.433** | **1.76e-25** | *** |
| Education: graduate level (vs college) | -0.1529 | 0.3802 | ±0.7604 | -0.402 | 0.6875 |  |
| Education: high school or below (vs college) | -1.1207 | 0.9192 | ±1.8385 | -1.219 | 0.2228 |  |
| Site: UCSD (vs UAB) | +0.9513 | 0.5509 | ±1.1018 | +1.727 | 0.0842 | . |
| Site: UW (vs UAB) | +1.0400 | 0.5349 | ±1.0698 | +1.944 | 0.0518 | . |
| **Age (years)** | **-0.0412** | 0.0170 | ±0.0340 | **-2.425** | **0.0153** | * |
| BMI (kg/m2) | +0.0249 | 0.0295 | ±0.0590 | +0.843 | 0.3991 |  |
| Hypertension | -0.3758 | 0.4086 | ±0.8172 | -0.920 | 0.3577 |  |
| High cholesterol | +0.1258 | 0.3628 | ±0.7255 | +0.347 | 0.7288 |  |
| Kidney disease | +0.4375 | 0.4976 | ±0.9952 | +0.879 | 0.3793 |  |
| Circulatory disease | -0.0102 | 0.4991 | ±0.9981 | -0.021 | 0.9836 |  |
| Time 181-250, pooled (%) | -0.0262 | 0.0158 | ±0.0316 | -1.657 | 0.0976 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **244**, R² = **0.0896**, Adj R² = **0.0465**, F-statistic = **2.08** (p = **0.0228**), Residual SE = **2.737** on **232** df, AIC = **1195.5**, BIC = **1237.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.2993** | 1.3703 | ±2.7405 | **+10.435** | **1.71e-25** | *** |
| Education: graduate level (vs college) | -0.1518 | 0.3804 | ±0.7608 | -0.399 | 0.6898 |  |
| Education: high school or below (vs college) | -1.1281 | 0.9183 | ±1.8367 | -1.228 | 0.2193 |  |
| Site: UCSD (vs UAB) | +0.9441 | 0.5508 | ±1.1016 | +1.714 | 0.0865 | . |
| Site: UW (vs UAB) | +1.0336 | 0.5348 | ±1.0696 | +1.933 | 0.0533 | . |
| **Age (years)** | **-0.0411** | 0.0170 | ±0.0340 | **-2.421** | **0.0155** | * |
| BMI (kg/m2) | +0.0246 | 0.0294 | ±0.0588 | +0.836 | 0.4033 |  |
| Hypertension | -0.3764 | 0.4088 | ±0.8177 | -0.921 | 0.3572 |  |
| High cholesterol | +0.1268 | 0.3628 | ±0.7256 | +0.349 | 0.7268 |  |
| Kidney disease | +0.4416 | 0.4969 | ±0.9938 | +0.889 | 0.3742 |  |
| Circulatory disease | -0.0137 | 0.4994 | ±0.9988 | -0.027 | 0.9782 |  |
| Avg. daily time 181-250 (%) | -0.0255 | 0.0154 | ±0.0307 | -1.658 | 0.0974 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **244**, R² = **0.1058**, Adj R² = **0.0634**, F-statistic = **2.50** (p = **0.0056**), Residual SE = **2.713** on **232** df, AIC = **1191.2**, BIC = **1233.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.3783** | 1.3698 | ±2.7396 | **+10.497** | **8.96e-26** | *** |
| Education: graduate level (vs college) | -0.1455 | 0.3768 | ±0.7536 | -0.386 | 0.6994 |  |
| Education: high school or below (vs college) | -0.9258 | 0.8873 | ±1.7746 | -1.043 | 0.2967 |  |
| Site: UCSD (vs UAB) | +0.9214 | 0.5433 | ±1.0866 | +1.696 | 0.0899 | . |
| Site: UW (vs UAB) | +1.0296 | 0.5310 | ±1.0620 | +1.939 | 0.0525 | . |
| **Age (years)** | **-0.0423** | 0.0169 | ±0.0339 | **-2.494** | **0.0126** | * |
| BMI (kg/m2) | +0.0271 | 0.0292 | ±0.0584 | +0.928 | 0.3535 |  |
| Hypertension | -0.3833 | 0.4023 | ±0.8046 | -0.953 | 0.3407 |  |
| High cholesterol | +0.1011 | 0.3523 | ±0.7046 | +0.287 | 0.7742 |  |
| Kidney disease | +0.4233 | 0.4812 | ±0.9625 | +0.880 | 0.3791 |  |
| Circulatory disease | +0.1277 | 0.4877 | ±0.9753 | +0.262 | 0.7934 |  |
| **Time > 180 (%)** | **-0.0274** | 0.0089 | ±0.0179 | **-3.066** | **0.0022** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **244**, R² = **0.1052**, Adj R² = **0.0628**, F-statistic = **2.48** (p = **0.0059**), Residual SE = **2.714** on **232** df, AIC = **1191.3**, BIC = **1233.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.3628** | 1.3698 | ±2.7396 | **+10.485** | **1.01e-25** | *** |
| Education: graduate level (vs college) | -0.1435 | 0.3769 | ±0.7538 | -0.381 | 0.7033 |  |
| Education: high school or below (vs college) | -0.9389 | 0.8886 | ±1.7773 | -1.057 | 0.2907 |  |
| Site: UCSD (vs UAB) | +0.9137 | 0.5438 | ±1.0875 | +1.680 | 0.0929 | . |
| Site: UW (vs UAB) | +1.0253 | 0.5311 | ±1.0622 | +1.931 | 0.0535 | . |
| **Age (years)** | **-0.0421** | 0.0169 | ±0.0339 | **-2.484** | **0.0130** | * |
| BMI (kg/m2) | +0.0270 | 0.0291 | ±0.0583 | +0.926 | 0.3544 |  |
| Hypertension | -0.3822 | 0.4026 | ±0.8052 | -0.949 | 0.3424 |  |
| High cholesterol | +0.1019 | 0.3525 | ±0.7050 | +0.289 | 0.7725 |  |
| Kidney disease | +0.4259 | 0.4819 | ±0.9639 | +0.884 | 0.3769 |  |
| Circulatory disease | +0.1212 | 0.4876 | ±0.9752 | +0.249 | 0.8037 |  |
| **Avg. daily time > 180 (%)** | **-0.0268** | 0.0089 | ±0.0178 | **-3.008** | **0.0026** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **244**, R² = **0.1004**, Adj R² = **0.0578**, F-statistic = **2.36** (p = **0.0090**), Residual SE = **2.721** on **232** df, AIC = **1192.6**, BIC = **1234.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.2852** | 1.3787 | ±2.7573 | **+10.362** | **3.71e-25** | *** |
| Education: graduate level (vs college) | -0.2027 | 0.3757 | ±0.7514 | -0.539 | 0.5896 |  |
| Education: high school or below (vs college) | -1.0259 | 0.9028 | ±1.8056 | -1.136 | 0.2558 |  |
| Site: UCSD (vs UAB) | +0.9511 | 0.5478 | ±1.0955 | +1.736 | 0.0825 | . |
| Site: UW (vs UAB) | +1.0232 | 0.5338 | ±1.0676 | +1.917 | 0.0553 | . |
| **Age (years)** | **-0.0431** | 0.0171 | ±0.0342 | **-2.524** | **0.0116** | * |
| BMI (kg/m2) | +0.0278 | 0.0298 | ±0.0596 | +0.933 | 0.3507 |  |
| Hypertension | -0.4085 | 0.4047 | ±0.8094 | -1.010 | 0.3127 |  |
| High cholesterol | +0.1185 | 0.3565 | ±0.7130 | +0.332 | 0.7396 |  |
| Kidney disease | +0.2647 | 0.4967 | ±0.9935 | +0.533 | 0.5941 |  |
| Circulatory disease | +0.0768 | 0.4915 | ±0.9831 | +0.156 | 0.8759 |  |
| **Nocturnal time > 180 (%)** | **-0.0230** | 0.0085 | ±0.0170 | **-2.707** | **0.0068** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **244**, R² = **0.1055**, Adj R² = **0.0631**, F-statistic = **2.49** (p = **0.0057**), Residual SE = **2.713** on **232** df, AIC = **1191.2**, BIC = **1233.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.5153** | 1.3508 | ±2.7015 | **+10.746** | **6.19e-27** | *** |
| Education: graduate level (vs college) | -0.2112 | 0.3766 | ±0.7532 | -0.561 | 0.5750 |  |
| Education: high school or below (vs college) | -0.8578 | 0.8949 | ±1.7898 | -0.959 | 0.3378 |  |
| Site: UCSD (vs UAB) | +0.9332 | 0.5434 | ±1.0867 | +1.717 | 0.0859 | . |
| Site: UW (vs UAB) | +0.9958 | 0.5322 | ±1.0645 | +1.871 | 0.0613 | . |
| **Age (years)** | **-0.0431** | 0.0168 | ±0.0337 | **-2.560** | **0.0105** | * |
| BMI (kg/m2) | +0.0182 | 0.0274 | ±0.0549 | +0.664 | 0.5069 |  |
| Hypertension | -0.4369 | 0.3992 | ±0.7984 | -1.094 | 0.2738 |  |
| High cholesterol | +0.0412 | 0.3493 | ±0.6987 | +0.118 | 0.9062 |  |
| Kidney disease | +0.2770 | 0.5023 | ±1.0047 | +0.551 | 0.5813 |  |
| Circulatory disease | +0.2066 | 0.4981 | ±0.9962 | +0.415 | 0.6784 |  |
| **Time > 250 (%)** | **-0.0415** | 0.0119 | ±0.0238 | **-3.485** | **4.93e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 244)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **244**, R² = **0.1056**, Adj R² = **0.0632**, F-statistic = **2.49** (p = **0.0057**), Residual SE = **2.713** on **232** df, AIC = **1191.2**, BIC = **1233.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.4975** | 1.3515 | ±2.7031 | **+10.727** | **7.63e-27** | *** |
| Education: graduate level (vs college) | -0.2103 | 0.3765 | ±0.7530 | -0.559 | 0.5765 |  |
| Education: high school or below (vs college) | -0.8536 | 0.8951 | ±1.7902 | -0.954 | 0.3403 |  |
| Site: UCSD (vs UAB) | +0.9313 | 0.5436 | ±1.0871 | +1.713 | 0.0866 | . |
| Site: UW (vs UAB) | +0.9988 | 0.5322 | ±1.0644 | +1.877 | 0.0606 | . |
| **Age (years)** | **-0.0430** | 0.0168 | ±0.0337 | **-2.555** | **0.0106** | * |
| BMI (kg/m2) | +0.0186 | 0.0275 | ±0.0549 | +0.677 | 0.4985 |  |
| Hypertension | -0.4353 | 0.3993 | ±0.7985 | -1.090 | 0.2756 |  |
| High cholesterol | +0.0387 | 0.3493 | ±0.6985 | +0.111 | 0.9118 |  |
| Kidney disease | +0.2717 | 0.5031 | ±1.0062 | +0.540 | 0.5891 |  |
| Circulatory disease | +0.2111 | 0.4981 | ±0.9962 | +0.424 | 0.6717 |  |
| **Avg. daily time > 250 (%)** | **-0.0423** | 0.0120 | ±0.0241 | **-3.515** | **4.40e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Healthy group (no diabetes + pre-diabetes / lifestyle) - Cognition

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 90 single-predictor tests; 22 with raw p < 0.05 (about 4 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 244): best single predictor out of sample is **Mean glucose** (CV R² -0.003 vs -0.038 for covariates alone, gain +0.036; -0.676 per SD, p = 0.014). Raw p < 0.05 (FDR not applicable here): GMI (p = 0.014), Mean glucose (p = 0.014), %>180 (pooled) (p = 0.021), %<54 (daily avg) (p = 0.024), %>180 (daily avg) (p = 0.026).
- **Cognitive impairment (MoCA < 26)** (n = 244): best single predictor out of sample is **Any <54 (0/1)** (CV AUC 0.628 vs 0.616 for covariates alone, gain +0.012; OR 0.74 per SD, p = 0.048). Raw p < 0.05 (FDR not applicable here): Any <54 (0/1) (p = 0.048).
- **MoCA memory index score (0-15)** (n = 244): best single predictor out of sample is **Mean glucose** (CV R² -0.002 vs -0.039 for covariates alone, gain +0.037; -0.51 per SD, p = 3.9e-04). Raw p < 0.05 (FDR not applicable here): GMI (p = 3.9e-04), Mean glucose (p = 3.9e-04), %>250 (daily avg) (p = 4.4e-04), %54-250 (daily avg) (p = 4.7e-04), %>250 (pooled) (p = 4.9e-04).

**Most predictable outcomes (largest out-of-sample gain over covariates):** MoCA memory index score (0-15) (+0.037, via Mean glucose); MoCA total score (0-30) (+0.036, via Mean glucose); Cognitive impairment (MoCA < 26) (+0.012, via Any <54 (0/1)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM level (0 FDR-significant / 6 raw-significant of 9); Band > 180 (0 FDR-significant / 5 raw-significant of 9); Range 70-180 (0 FDR-significant / 4 raw-significant of 6).
Level metrics: 0 FDR-significant (6 raw); variability metrics: 0 FDR-significant (0 raw); HbA1c alone: 0 FDR-significant (1 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** MoCA total score (Mean glucose, ΔAIC -5.3); Cognitive impairment (Any <54 (0/1), ΔAIC -4.0); MoCA memory index score (Mean glucose, ΔAIC -3.8).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
