# Phase 6b model output tables - Hyperglycaemia exposure: at least one reading > 250 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Depression

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 243; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **243**, R² = **0.1959**, Adj R² = **0.1613**, F-statistic = **5.65** (p = **1.44e-07**), Residual SE = **4.585** on **232** df, AIC = **1440.4**, BIC = **1478.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3234** | 2.5766 | ±5.1533 | **+2.842** | **0.0045** | ** |
| Education: graduate level (vs college) | -0.1601 | 0.6199 | ±1.2397 | -0.258 | 0.7962 |  |
| **Education: high school or below (vs college)** | **+3.2197** | 1.4711 | ±2.9422 | **+2.189** | **0.0286** | * |
| Site: UCSD (vs UAB) | -1.2627 | 0.9241 | ±1.8482 | -1.366 | 0.1718 |  |
| Site: UW (vs UAB) | -1.3345 | 0.7807 | ±1.5613 | -1.709 | 0.0874 | . |
| **Age (years)** | **-0.0943** | 0.0296 | ±0.0593 | **-3.182** | **0.0015** | ** |
| **BMI (kg/m2)** | **+0.1350** | 0.0618 | ±0.1235 | **+2.187** | **0.0288** | * |
| Hypertension | +0.7339 | 0.7135 | ±1.4270 | +1.029 | 0.3036 |  |
| High cholesterol | +0.7469 | 0.6027 | ±1.2054 | +1.239 | 0.2152 |  |
| Kidney disease | +2.0894 | 1.5087 | ±3.0174 | +1.385 | 0.1661 |  |
| Circulatory disease | +0.5911 | 1.0049 | ±2.0098 | +0.588 | 0.5564 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **243**, R² = **0.1972**, Adj R² = **0.1589**, F-statistic = **5.16** (p = **3.09e-07**), Residual SE = **4.591** on **231** df, AIC = **1442.0**, BIC = **1483.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4066** | 3.3416 | ±6.6833 | **+2.516** | **0.0119** | * |
| Education: graduate level (vs college) | -0.1579 | 0.6219 | ±1.2437 | -0.254 | 0.7995 |  |
| **Education: high school or below (vs college)** | **+3.3290** | 1.5243 | ±3.0486 | **+2.184** | **0.0290** | * |
| Site: UCSD (vs UAB) | -1.2628 | 0.9253 | ±1.8506 | -1.365 | 0.1723 |  |
| Site: UW (vs UAB) | -1.3200 | 0.7820 | ±1.5639 | -1.688 | 0.0914 | . |
| **Age (years)** | **-0.0940** | 0.0297 | ±0.0594 | **-3.164** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1375** | 0.0614 | ±0.1229 | **+2.238** | **0.0252** | * |
| Hypertension | +0.7390 | 0.7142 | ±1.4285 | +1.035 | 0.3008 |  |
| High cholesterol | +0.7710 | 0.6050 | ±1.2101 | +1.274 | 0.2026 |  |
| Kidney disease | +2.0551 | 1.5089 | ±3.0177 | +1.362 | 0.1732 |  |
| Circulatory disease | +0.6906 | 1.0203 | ±2.0405 | +0.677 | 0.4985 |  |
| HbA1c (%) | -0.2016 | 0.3690 | ±0.7381 | -0.546 | 0.5849 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **243**, R² = **0.1961**, Adj R² = **0.1578**, F-statistic = **5.12** (p = **3.53e-07**), Residual SE = **4.594** on **231** df, AIC = **1442.3**, BIC = **1484.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.5715** | 3.1395 | ±6.2791 | **+2.412** | **0.0159** | * |
| Education: graduate level (vs college) | -0.1479 | 0.6309 | ±1.2619 | -0.234 | 0.8147 |  |
| **Education: high school or below (vs college)** | **+3.2551** | 1.5380 | ±3.0761 | **+2.116** | **0.0343** | * |
| Site: UCSD (vs UAB) | -1.2695 | 0.9342 | ±1.8684 | -1.359 | 0.1742 |  |
| Site: UW (vs UAB) | -1.3306 | 0.7804 | ±1.5607 | -1.705 | 0.0882 | . |
| **Age (years)** | **-0.0944** | 0.0298 | ±0.0596 | **-3.168** | **0.0015** | ** |
| **BMI (kg/m2)** | **+0.1363** | 0.0611 | ±0.1221 | **+2.232** | **0.0256** | * |
| Hypertension | +0.7395 | 0.7207 | ±1.4414 | +1.026 | 0.3048 |  |
| High cholesterol | +0.7527 | 0.6070 | ±1.2141 | +1.240 | 0.2150 |  |
| Kidney disease | +2.0923 | 1.5141 | ±3.0282 | +1.382 | 0.1670 |  |
| Circulatory disease | +0.6169 | 1.0378 | ±2.0755 | +0.594 | 0.5522 |  |
| Mean glucose (mg/dL) | -0.0021 | 0.0127 | ±0.0253 | -0.166 | 0.8685 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **243**, R² = **0.1961**, Adj R² = **0.1578**, F-statistic = **5.12** (p = **3.53e-07**), Residual SE = **4.594** on **231** df, AIC = **1442.3**, BIC = **1484.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +7.8619 | 4.3919 | ±8.7838 | +1.790 | 0.0734 | . |
| Education: graduate level (vs college) | -0.1479 | 0.6309 | ±1.2619 | -0.234 | 0.8147 |  |
| **Education: high school or below (vs college)** | **+3.2551** | 1.5380 | ±3.0761 | **+2.116** | **0.0343** | * |
| Site: UCSD (vs UAB) | -1.2695 | 0.9342 | ±1.8684 | -1.359 | 0.1742 |  |
| Site: UW (vs UAB) | -1.3306 | 0.7804 | ±1.5607 | -1.705 | 0.0882 | . |
| **Age (years)** | **-0.0944** | 0.0298 | ±0.0596 | **-3.168** | **0.0015** | ** |
| **BMI (kg/m2)** | **+0.1363** | 0.0611 | ±0.1221 | **+2.232** | **0.0256** | * |
| Hypertension | +0.7395 | 0.7207 | ±1.4414 | +1.026 | 0.3048 |  |
| High cholesterol | +0.7527 | 0.6070 | ±1.2141 | +1.240 | 0.2150 |  |
| Kidney disease | +2.0923 | 1.5141 | ±3.0282 | +1.382 | 0.1670 |  |
| Circulatory disease | +0.6169 | 1.0378 | ±2.0755 | +0.594 | 0.5522 |  |
| GMI (%) | -0.0877 | 0.5297 | ±1.0595 | -0.166 | 0.8685 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **243**, R² = **0.1961**, Adj R² = **0.1578**, F-statistic = **5.12** (p = **3.55e-07**), Residual SE = **4.594** on **231** df, AIC = **1442.4**, BIC = **1484.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.1362** | 3.0288 | ±6.0577 | **+2.356** | **0.0185** | * |
| Education: graduate level (vs college) | -0.1671 | 0.6290 | ±1.2579 | -0.266 | 0.7904 |  |
| **Education: high school or below (vs college)** | **+3.1907** | 1.5249 | ±3.0498 | **+2.092** | **0.0364** | * |
| Site: UCSD (vs UAB) | -1.2614 | 0.9310 | ±1.8620 | -1.355 | 0.1755 |  |
| Site: UW (vs UAB) | -1.3373 | 0.7812 | ±1.5623 | -1.712 | 0.0869 | . |
| **Age (years)** | **-0.0940** | 0.0298 | ±0.0596 | **-3.157** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1336** | 0.0615 | ±0.1230 | **+2.173** | **0.0298** | * |
| Hypertension | +0.7288 | 0.7230 | ±1.4460 | +1.008 | 0.3135 |  |
| High cholesterol | +0.7417 | 0.6066 | ±1.2131 | +1.223 | 0.2214 |  |
| Kidney disease | +2.1003 | 1.5112 | ±3.0223 | +1.390 | 0.1646 |  |
| Circulatory disease | +0.5733 | 1.0344 | ±2.0689 | +0.554 | 0.5794 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0017 | 0.0120 | ±0.0241 | +0.138 | 0.8905 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **243**, R² = **0.2015**, Adj R² = **0.1635**, F-statistic = **5.30** (p = **1.81e-07**), Residual SE = **4.579** on **231** df, AIC = **1440.7**, BIC = **1482.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.6093** | 2.8809 | ±5.7619 | **+2.988** | **0.0028** | ** |
| Education: graduate level (vs college) | -0.1465 | 0.6189 | ±1.2378 | -0.237 | 0.8129 |  |
| **Education: high school or below (vs college)** | **+3.2072** | 1.4940 | ±2.9879 | **+2.147** | **0.0318** | * |
| Site: UCSD (vs UAB) | -1.3503 | 0.9256 | ±1.8511 | -1.459 | 0.1446 |  |
| Site: UW (vs UAB) | -1.3739 | 0.7844 | ±1.5688 | -1.751 | 0.0799 | . |
| **Age (years)** | **-0.0928** | 0.0297 | ±0.0593 | **-3.130** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1435** | 0.0598 | ±0.1195 | **+2.402** | **0.0163** | * |
| Hypertension | +0.7815 | 0.7188 | ±1.4377 | +1.087 | 0.2770 |  |
| High cholesterol | +0.6529 | 0.6094 | ±1.2188 | +1.071 | 0.2840 |  |
| Kidney disease | +2.3230 | 1.5187 | ±3.0373 | +1.530 | 0.1261 |  |
| Circulatory disease | +0.7585 | 1.0057 | ±2.0113 | +0.754 | 0.4507 |  |
| Glucose SD, pooled (mg/dL) | -0.0520 | 0.0418 | ±0.0835 | -1.246 | 0.2126 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **243**, R² = **0.2032**, Adj R² = **0.1653**, F-statistic = **5.36** (p = **1.47e-07**), Residual SE = **4.574** on **231** df, AIC = **1440.2**, BIC = **1482.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.6922** | 2.8141 | ±5.6283 | **+3.089** | **0.0020** | ** |
| Education: graduate level (vs college) | -0.1234 | 0.6213 | ±1.2426 | -0.199 | 0.8425 |  |
| **Education: high school or below (vs college)** | **+3.1611** | 1.4978 | ±2.9956 | **+2.110** | **0.0348** | * |
| Site: UCSD (vs UAB) | -1.3621 | 0.9239 | ±1.8478 | -1.474 | 0.1404 |  |
| Site: UW (vs UAB) | -1.3782 | 0.7828 | ±1.5656 | -1.761 | 0.0783 | . |
| **Age (years)** | **-0.0930** | 0.0297 | ±0.0595 | **-3.129** | **0.0018** | ** |
| **BMI (kg/m2)** | **+0.1462** | 0.0594 | ±0.1188 | **+2.461** | **0.0138** | * |
| Hypertension | +0.7960 | 0.7198 | ±1.4396 | +1.106 | 0.2688 |  |
| High cholesterol | +0.6452 | 0.6050 | ±1.2100 | +1.066 | 0.2863 |  |
| Kidney disease | +2.3447 | 1.5179 | ±3.0358 | +1.545 | 0.1224 |  |
| Circulatory disease | +0.7911 | 1.0022 | ±2.0045 | +0.789 | 0.4299 |  |
| Avg. daily SD (mg/dL) | -0.0629 | 0.0458 | ±0.0915 | -1.375 | 0.1690 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **243**, R² = **0.2031**, Adj R² = **0.1651**, F-statistic = **5.35** (p = **1.49e-07**), Residual SE = **4.574** on **231** df, AIC = **1440.2**, BIC = **1482.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.2360** | 2.8610 | ±5.7221 | **+3.228** | **0.0012** | ** |
| Education: graduate level (vs college) | -0.2409 | 0.6183 | ±1.2365 | -0.390 | 0.6968 |  |
| **Education: high school or below (vs college)** | **+3.0100** | 1.5186 | ±3.0372 | **+1.982** | **0.0475** | * |
| Site: UCSD (vs UAB) | -1.3535 | 0.9217 | ±1.8434 | -1.468 | 0.1420 |  |
| Site: UW (vs UAB) | -1.4370 | 0.7794 | ±1.5588 | -1.844 | 0.0652 | . |
| **Age (years)** | **-0.0913** | 0.0296 | ±0.0592 | **-3.085** | **0.0020** | ** |
| **BMI (kg/m2)** | **+0.1377** | 0.0608 | ±0.1217 | **+2.262** | **0.0237** | * |
| Hypertension | +0.7415 | 0.7116 | ±1.4231 | +1.042 | 0.2974 |  |
| High cholesterol | +0.5653 | 0.6144 | ±1.2287 | +0.920 | 0.3575 |  |
| Kidney disease | +2.3380 | 1.5102 | ±3.0203 | +1.548 | 0.1216 |  |
| Circulatory disease | +0.6316 | 1.0058 | ±2.0117 | +0.628 | 0.5300 |  |
| CV (%) | -0.0901 | 0.0556 | ±0.1112 | -1.621 | 0.1050 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **243**, R² = **0.2019**, Adj R² = **0.1639**, F-statistic = **5.31** (p = **1.73e-07**), Residual SE = **4.577** on **231** df, AIC = **1440.6**, BIC = **1482.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +5.2991 | 2.9418 | ±5.8836 | +1.801 | 0.0717 | . |
| Education: graduate level (vs college) | -0.1963 | 0.6176 | ±1.2351 | -0.318 | 0.7506 |  |
| **Education: high school or below (vs college)** | **+3.0707** | 1.5178 | ±3.0356 | **+2.023** | **0.0431** | * |
| Site: UCSD (vs UAB) | -1.3304 | 0.9180 | ±1.8361 | -1.449 | 0.1473 |  |
| Site: UW (vs UAB) | -1.4245 | 0.7758 | ±1.5516 | -1.836 | 0.0663 | . |
| **Age (years)** | **-0.0922** | 0.0296 | ±0.0593 | **-3.114** | **0.0018** | ** |
| **BMI (kg/m2)** | **+0.1359** | 0.0607 | ±0.1214 | **+2.239** | **0.0252** | * |
| Hypertension | +0.7672 | 0.7170 | ±1.4340 | +1.070 | 0.2846 |  |
| High cholesterol | +0.6119 | 0.6107 | ±1.2214 | +1.002 | 0.3164 |  |
| Kidney disease | +2.2882 | 1.5073 | ±3.0147 | +1.518 | 0.1290 |  |
| Circulatory disease | +0.6259 | 1.0088 | ±2.0177 | +0.620 | 0.5350 |  |
| Mean / SD ratio | +0.4205 | 0.2998 | ±0.5997 | +1.402 | 0.1608 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **243**, R² = **0.2051**, Adj R² = **0.1673**, F-statistic = **5.42** (p = **1.16e-07**), Residual SE = **4.568** on **231** df, AIC = **1439.6**, BIC = **1481.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.9603 | 3.0486 | ±6.0972 | +1.627 | 0.1037 |  |
| Education: graduate level (vs college) | -0.1756 | 0.6179 | ±1.2357 | -0.284 | 0.7763 |  |
| **Education: high school or below (vs college)** | **+3.0120** | 1.5295 | ±3.0590 | **+1.969** | **0.0489** | * |
| Site: UCSD (vs UAB) | -1.3328 | 0.9219 | ±1.8437 | -1.446 | 0.1482 |  |
| Site: UW (vs UAB) | -1.4612 | 0.7743 | ±1.5485 | -1.887 | 0.0591 | . |
| **Age (years)** | **-0.0913** | 0.0298 | ±0.0596 | **-3.066** | **0.0022** | ** |
| **BMI (kg/m2)** | **+0.1384** | 0.0602 | ±0.1204 | **+2.299** | **0.0215** | * |
| Hypertension | +0.7829 | 0.7137 | ±1.4275 | +1.097 | 0.2727 |  |
| High cholesterol | +0.5914 | 0.6060 | ±1.2120 | +0.976 | 0.3291 |  |
| Kidney disease | +2.3400 | 1.5177 | ±3.0355 | +1.542 | 0.1231 |  |
| Circulatory disease | +0.6182 | 1.0100 | ±2.0200 | +0.612 | 0.5405 |  |
| Avg. daily mean/SD | +0.4021 | 0.2510 | ±0.5020 | +1.602 | 0.1092 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **243**, R² = **0.1998**, Adj R² = **0.1617**, F-statistic = **5.24** (p = **2.25e-07**), Residual SE = **4.584** on **231** df, AIC = **1441.2**, BIC = **1483.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.9286** | 3.1600 | ±6.3200 | **+2.826** | **0.0047** | ** |
| Education: graduate level (vs college) | -0.2275 | 0.6181 | ±1.2362 | -0.368 | 0.7128 |  |
| **Education: high school or below (vs college)** | **+3.1476** | 1.4753 | ±2.9506 | **+2.134** | **0.0329** | * |
| Site: UCSD (vs UAB) | -1.3795 | 0.9584 | ±1.9168 | -1.439 | 0.1500 |  |
| Site: UW (vs UAB) | -1.4972 | 0.8195 | ±1.6390 | -1.827 | 0.0677 | . |
| **Age (years)** | **-0.0942** | 0.0296 | ±0.0591 | **-3.186** | **0.0014** | ** |
| **BMI (kg/m2)** | **+0.1441** | 0.0612 | ±0.1223 | **+2.355** | **0.0185** | * |
| Hypertension | +0.6477 | 0.7173 | ±1.4346 | +0.903 | 0.3665 |  |
| High cholesterol | +0.6113 | 0.6262 | ±1.2524 | +0.976 | 0.3289 |  |
| Kidney disease | +2.0863 | 1.5033 | ±3.0066 | +1.388 | 0.1652 |  |
| Circulatory disease | +0.6501 | 0.9924 | ±1.9847 | +0.655 | 0.5124 |  |
| MAG (mg/dL/h) | -0.0368 | 0.0389 | ±0.0778 | -0.946 | 0.3443 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **243**, R² = **0.2030**, Adj R² = **0.1650**, F-statistic = **5.35** (p = **1.52e-07**), Residual SE = **4.574** on **231** df, AIC = **1440.3**, BIC = **1482.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.3332** | 3.0270 | ±6.0541 | **+3.083** | **0.0020** | ** |
| Education: graduate level (vs college) | -0.1405 | 0.6217 | ±1.2434 | -0.226 | 0.8212 |  |
| **Education: high school or below (vs college)** | **+3.1809** | 1.4967 | ±2.9935 | **+2.125** | **0.0336** | * |
| Site: UCSD (vs UAB) | -1.4051 | 0.9356 | ±1.8711 | -1.502 | 0.1331 |  |
| Site: UW (vs UAB) | -1.4416 | 0.7929 | ±1.5859 | -1.818 | 0.0691 | . |
| **Age (years)** | **-0.0941** | 0.0298 | ±0.0596 | **-3.157** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1438** | 0.0599 | ±0.1199 | **+2.399** | **0.0165** | * |
| Hypertension | +0.7482 | 0.7088 | ±1.4177 | +1.056 | 0.2912 |  |
| High cholesterol | +0.5848 | 0.6073 | ±1.2147 | +0.963 | 0.3356 |  |
| Kidney disease | +2.2549 | 1.5077 | ±3.0153 | +1.496 | 0.1347 |  |
| Circulatory disease | +0.7473 | 0.9850 | ±1.9699 | +0.759 | 0.4480 |  |
| Avg. daily range (mg/dL) | -0.0160 | 0.0121 | ±0.0242 | -1.324 | 0.1855 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **243**, R² = **0.1960**, Adj R² = **0.1577**, F-statistic = **5.12** (p = **3.59e-07**), Residual SE = **4.595** on **231** df, AIC = **1442.4**, BIC = **1484.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3087** | 2.6479 | ±5.2959 | **+2.760** | **0.0058** | ** |
| Education: graduate level (vs college) | -0.1586 | 0.6214 | ±1.2427 | -0.255 | 0.7985 |  |
| **Education: high school or below (vs college)** | **+3.2164** | 1.4810 | ±2.9621 | **+2.172** | **0.0299** | * |
| Site: UCSD (vs UAB) | -1.2617 | 0.9297 | ±1.8594 | -1.357 | 0.1748 |  |
| Site: UW (vs UAB) | -1.3354 | 0.7793 | ±1.5587 | -1.713 | 0.0866 | . |
| **Age (years)** | **-0.0944** | 0.0296 | ±0.0592 | **-3.190** | **0.0014** | ** |
| **BMI (kg/m2)** | **+0.1348** | 0.0620 | ±0.1240 | **+2.174** | **0.0297** | * |
| Hypertension | +0.7340 | 0.7163 | ±1.4327 | +1.025 | 0.3056 |  |
| High cholesterol | +0.7483 | 0.6082 | ±1.2163 | +1.230 | 0.2186 |  |
| Kidney disease | +2.0867 | 1.5252 | ±3.0503 | +1.368 | 0.1713 |  |
| Circulatory disease | +0.5899 | 1.0104 | ±2.0208 | +0.584 | 0.5593 |  |
| SD of daily means (mg/dL) | +0.0031 | 0.0581 | ±0.1162 | +0.053 | 0.9576 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **243**, R² = **0.1963**, Adj R² = **0.1580**, F-statistic = **5.13** (p = **3.46e-07**), Residual SE = **4.594** on **231** df, AIC = **1442.3**, BIC = **1484.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.7609** | 3.4364 | ±6.8729 | **+1.967** | **0.0491** | * |
| Education: graduate level (vs college) | -0.1481 | 0.6273 | ±1.2546 | -0.236 | 0.8134 |  |
| **Education: high school or below (vs college)** | **+3.2527** | 1.5136 | ±3.0272 | **+2.149** | **0.0316** | * |
| Site: UCSD (vs UAB) | -1.2768 | 0.9347 | ±1.8693 | -1.366 | 0.1719 |  |
| Site: UW (vs UAB) | -1.3379 | 0.7883 | ±1.5767 | -1.697 | 0.0897 | . |
| **Age (years)** | **-0.0944** | 0.0300 | ±0.0599 | **-3.151** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1375** | 0.0610 | ±0.1220 | **+2.254** | **0.0242** | * |
| Hypertension | +0.7386 | 0.7190 | ±1.4380 | +1.027 | 0.3043 |  |
| High cholesterol | +0.7501 | 0.6078 | ±1.2155 | +1.234 | 0.2171 |  |
| Kidney disease | +2.1133 | 1.5212 | ±3.0424 | +1.389 | 0.1648 |  |
| Circulatory disease | +0.6197 | 1.0296 | ±2.0593 | +0.602 | 0.5473 |  |
| Time in range 70-180, pooled (%) | +0.0057 | 0.0278 | ±0.0556 | +0.204 | 0.8381 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **243**, R² = **0.1961**, Adj R² = **0.1579**, F-statistic = **5.12** (p = **3.51e-07**), Residual SE = **4.594** on **231** df, AIC = **1442.3**, BIC = **1484.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8813** | 3.4469 | ±6.8938 | **+1.996** | **0.0459** | * |
| Education: graduate level (vs college) | -0.1500 | 0.6282 | ±1.2563 | -0.239 | 0.8113 |  |
| **Education: high school or below (vs college)** | **+3.2440** | 1.5100 | ±3.0201 | **+2.148** | **0.0317** | * |
| Site: UCSD (vs UAB) | -1.2750 | 0.9364 | ±1.8727 | -1.362 | 0.1733 |  |
| Site: UW (vs UAB) | -1.3379 | 0.7891 | ±1.5781 | -1.696 | 0.0900 | . |
| **Age (years)** | **-0.0944** | 0.0300 | ±0.0599 | **-3.151** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1370** | 0.0611 | ±0.1223 | **+2.241** | **0.0250** | * |
| Hypertension | +0.7379 | 0.7196 | ±1.4392 | +1.025 | 0.3052 |  |
| High cholesterol | +0.7495 | 0.6079 | ±1.2158 | +1.233 | 0.2176 |  |
| Kidney disease | +2.1089 | 1.5230 | ±3.0460 | +1.385 | 0.1661 |  |
| Circulatory disease | +0.6128 | 1.0295 | ±2.0589 | +0.595 | 0.5517 |  |
| Avg. daily time in range 70-180 (%) | +0.0044 | 0.0274 | ±0.0548 | +0.162 | 0.8714 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **243**, R² = **0.1966**, Adj R² = **0.1584**, F-statistic = **5.14** (p = **3.31e-07**), Residual SE = **4.593** on **231** df, AIC = **1442.2**, BIC = **1484.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.2820** | 2.5788 | ±5.1576 | **+2.824** | **0.0047** | ** |
| Education: graduate level (vs college) | -0.1330 | 0.6156 | ±1.2311 | -0.216 | 0.8289 |  |
| **Education: high school or below (vs college)** | **+3.2596** | 1.4984 | ±2.9969 | **+2.175** | **0.0296** | * |
| Site: UCSD (vs UAB) | -1.2616 | 0.9292 | ±1.8585 | -1.358 | 0.1746 |  |
| Site: UW (vs UAB) | -1.3168 | 0.7851 | ±1.5702 | -1.677 | 0.0935 | . |
| **Age (years)** | **-0.0948** | 0.0295 | ±0.0591 | **-3.209** | **0.0013** | ** |
| **BMI (kg/m2)** | **+0.1335** | 0.0621 | ±0.1243 | **+2.148** | **0.0317** | * |
| Hypertension | +0.7391 | 0.7153 | ±1.4305 | +1.033 | 0.3015 |  |
| High cholesterol | +0.7699 | 0.6036 | ±1.2072 | +1.276 | 0.2021 |  |
| Kidney disease | +2.0630 | 1.5081 | ±3.0161 | +1.368 | 0.1713 |  |
| Circulatory disease | +0.5853 | 1.0155 | ±2.0310 | +0.576 | 0.5644 |  |
| Any reading < 54 during wear (0/1) | +0.2978 | 0.7344 | ±1.4687 | +0.406 | 0.6851 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **243**, R² = **0.1961**, Adj R² = **0.1578**, F-statistic = **5.12** (p = **3.54e-07**), Residual SE = **4.594** on **231** df, AIC = **1442.3**, BIC = **1484.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3614** | 2.5925 | ±5.1850 | **+2.840** | **0.0045** | ** |
| Education: graduate level (vs college) | -0.1728 | 0.6219 | ±1.2439 | -0.278 | 0.7812 |  |
| **Education: high school or below (vs college)** | **+3.2043** | 1.4732 | ±2.9464 | **+2.175** | **0.0296** | * |
| Site: UCSD (vs UAB) | -1.2773 | 0.9319 | ±1.8639 | -1.371 | 0.1705 |  |
| Site: UW (vs UAB) | -1.3546 | 0.7938 | ±1.5877 | -1.706 | 0.0879 | . |
| **Age (years)** | **-0.0939** | 0.0297 | ±0.0594 | **-3.161** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1342** | 0.0621 | ±0.1242 | **+2.160** | **0.0308** | * |
| Hypertension | +0.7268 | 0.7146 | ±1.4291 | +1.017 | 0.3091 |  |
| High cholesterol | +0.7364 | 0.6054 | ±1.2107 | +1.216 | 0.2238 |  |
| Kidney disease | +2.0875 | 1.5091 | ±3.0182 | +1.383 | 0.1666 |  |
| Circulatory disease | +0.5882 | 1.0053 | ±2.0107 | +0.585 | 0.5585 |  |
| Time < 54 (%) | -0.0618 | 0.5007 | ±1.0014 | -0.123 | 0.9018 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **243**, R² = **0.1963**, Adj R² = **0.1581**, F-statistic = **5.13** (p = **3.42e-07**), Residual SE = **4.593** on **231** df, AIC = **1442.3**, BIC = **1484.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3847** | 2.5887 | ±5.1773 | **+2.853** | **0.0043** | ** |
| Education: graduate level (vs college) | -0.1810 | 0.6219 | ±1.2437 | -0.291 | 0.7710 |  |
| **Education: high school or below (vs college)** | **+3.1914** | 1.4734 | ±2.9468 | **+2.166** | **0.0303** | * |
| Site: UCSD (vs UAB) | -1.2884 | 0.9316 | ±1.8632 | -1.383 | 0.1667 |  |
| Site: UW (vs UAB) | -1.3744 | 0.7947 | ±1.5893 | -1.730 | 0.0837 | . |
| **Age (years)** | **-0.0936** | 0.0297 | ±0.0594 | **-3.152** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1338** | 0.0620 | ±0.1240 | **+2.157** | **0.0310** | * |
| Hypertension | +0.7208 | 0.7148 | ±1.4296 | +1.008 | 0.3133 |  |
| High cholesterol | +0.7243 | 0.6074 | ±1.2148 | +1.193 | 0.2331 |  |
| Kidney disease | +2.0873 | 1.5094 | ±3.0188 | +1.383 | 0.1667 |  |
| Circulatory disease | +0.5875 | 1.0054 | ±2.0109 | +0.584 | 0.5590 |  |
| Avg. daily time < 54 (%) | -0.1423 | 0.4948 | ±0.9895 | -0.288 | 0.7737 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **243**, R² = **0.1998**, Adj R² = **0.1617**, F-statistic = **5.24** (p = **2.25e-07**), Residual SE = **4.584** on **231** df, AIC = **1441.2**, BIC = **1483.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3835** | 2.5838 | ±5.1676 | **+2.858** | **0.0043** | ** |
| Education: graduate level (vs college) | -0.2455 | 0.6260 | ±1.2519 | -0.392 | 0.6949 |  |
| **Education: high school or below (vs college)** | **+3.1060** | 1.4917 | ±2.9834 | **+2.082** | **0.0373** | * |
| Site: UCSD (vs UAB) | -1.3108 | 0.9263 | ±1.8527 | -1.415 | 0.1571 |  |
| Site: UW (vs UAB) | -1.4299 | 0.7914 | ±1.5827 | -1.807 | 0.0708 | . |
| **Age (years)** | **-0.0929** | 0.0295 | ±0.0590 | **-3.152** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1395** | 0.0630 | ±0.1260 | **+2.214** | **0.0268** | * |
| Hypertension | +0.7009 | 0.7142 | ±1.4284 | +0.981 | 0.3264 |  |
| High cholesterol | +0.6529 | 0.6097 | ±1.2193 | +1.071 | 0.2842 |  |
| Kidney disease | +2.1120 | 1.4997 | ±2.9995 | +1.408 | 0.1591 |  |
| Circulatory disease | +0.5635 | 1.0049 | ±2.0097 | +0.561 | 0.5749 |  |
| Time 54-69, pooled (%) | -0.2490 | 0.2379 | ±0.4757 | -1.047 | 0.2952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **243**, R² = **0.1995**, Adj R² = **0.1613**, F-statistic = **5.23** (p = **2.34e-07**), Residual SE = **4.584** on **231** df, AIC = **1441.3**, BIC = **1483.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3849** | 2.5823 | ±5.1647 | **+2.860** | **0.0042** | ** |
| Education: graduate level (vs college) | -0.2435 | 0.6267 | ±1.2534 | -0.389 | 0.6976 |  |
| **Education: high school or below (vs college)** | **+3.1028** | 1.4881 | ±2.9762 | **+2.085** | **0.0371** | * |
| Site: UCSD (vs UAB) | -1.3124 | 0.9274 | ±1.8548 | -1.415 | 0.1570 |  |
| Site: UW (vs UAB) | -1.4369 | 0.7937 | ±1.5875 | -1.810 | 0.0703 | . |
| **Age (years)** | **-0.0928** | 0.0295 | ±0.0590 | **-3.146** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1386** | 0.0628 | ±0.1255 | **+2.209** | **0.0272** | * |
| Hypertension | +0.6998 | 0.7147 | ±1.4295 | +0.979 | 0.3275 |  |
| High cholesterol | +0.6522 | 0.6115 | ±1.2229 | +1.067 | 0.2862 |  |
| Kidney disease | +2.1101 | 1.5010 | ±3.0019 | +1.406 | 0.1598 |  |
| Circulatory disease | +0.5596 | 1.0053 | ±2.0107 | +0.557 | 0.5778 |  |
| Avg. daily time 54-69 (%) | -0.2279 | 0.2182 | ±0.4364 | -1.044 | 0.2963 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **243**, R² = **0.1982**, Adj R² = **0.1600**, F-statistic = **5.19** (p = **2.73e-07**), Residual SE = **4.588** on **231** df, AIC = **1441.7**, BIC = **1483.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4328** | 2.5831 | ±5.1661 | **+2.878** | **0.0040** | ** |
| Education: graduate level (vs college) | -0.2301 | 0.6251 | ±1.2502 | -0.368 | 0.7128 |  |
| **Education: high school or below (vs college)** | **+3.1295** | 1.4839 | ±2.9677 | **+2.109** | **0.0349** | * |
| Site: UCSD (vs UAB) | -1.3176 | 0.9302 | ±1.8604 | -1.416 | 0.1566 |  |
| Site: UW (vs UAB) | -1.4253 | 0.7968 | ±1.5936 | -1.789 | 0.0737 | . |
| **Age (years)** | **-0.0927** | 0.0295 | ±0.0591 | **-3.140** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1355** | 0.0620 | ±0.1240 | **+2.186** | **0.0288** | * |
| Hypertension | +0.7023 | 0.7145 | ±1.4290 | +0.983 | 0.3257 |  |
| High cholesterol | +0.6767 | 0.6075 | ±1.2150 | +1.114 | 0.2653 |  |
| Kidney disease | +2.0972 | 1.5041 | ±3.0082 | +1.394 | 0.1632 |  |
| Circulatory disease | +0.5708 | 1.0052 | ±2.0105 | +0.568 | 0.5701 |  |
| Time < 70 (%) | -0.1279 | 0.0942 | ±0.1884 | -1.358 | 0.1744 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **243**, R² = **0.1985**, Adj R² = **0.1603**, F-statistic = **5.20** (p = **2.63e-07**), Residual SE = **4.587** on **231** df, AIC = **1441.6**, BIC = **1483.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4220** | 2.5807 | ±5.1613 | **+2.876** | **0.0040** | ** |
| Education: graduate level (vs college) | -0.2324 | 0.6255 | ±1.2511 | -0.371 | 0.7103 |  |
| **Education: high school or below (vs college)** | **+3.1195** | 1.4831 | ±2.9663 | **+2.103** | **0.0354** | * |
| Site: UCSD (vs UAB) | -1.3189 | 0.9300 | ±1.8600 | -1.418 | 0.1561 |  |
| Site: UW (vs UAB) | -1.4373 | 0.7972 | ±1.5945 | -1.803 | 0.0714 | . |
| **Age (years)** | **-0.0926** | 0.0295 | ±0.0590 | **-3.138** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1360** | 0.0621 | ±0.1241 | **+2.192** | **0.0284** | * |
| Hypertension | +0.6998 | 0.7150 | ±1.4300 | +0.979 | 0.3277 |  |
| High cholesterol | +0.6660 | 0.6098 | ±1.2196 | +1.092 | 0.2748 |  |
| Kidney disease | +2.1001 | 1.5038 | ±3.0076 | +1.397 | 0.1626 |  |
| Circulatory disease | +0.5680 | 1.0055 | ±2.0109 | +0.565 | 0.5721 |  |
| Avg. daily time < 70 (%) | -0.1408 | 0.0899 | ±0.1797 | -1.567 | 0.1171 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **243**, R² = **0.2052**, Adj R² = **0.1673**, F-statistic = **5.42** (p = **1.16e-07**), Residual SE = **4.568** on **231** df, AIC = **1439.6**, BIC = **1481.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2.9102 | 3.2021 | ±6.4041 | +0.909 | 0.3634 |  |
| Education: graduate level (vs college) | -0.1619 | 0.6144 | ±1.2288 | -0.263 | 0.7922 |  |
| **Education: high school or below (vs college)** | **+3.5225** | 1.5385 | ±3.0770 | **+2.290** | **0.0220** | * |
| Site: UCSD (vs UAB) | -1.3218 | 0.9231 | ±1.8462 | -1.432 | 0.1522 |  |
| Site: UW (vs UAB) | -1.3716 | 0.7815 | ±1.5631 | -1.755 | 0.0793 | . |
| **Age (years)** | **-0.0958** | 0.0295 | ±0.0589 | **-3.251** | **0.0011** | ** |
| **BMI (kg/m2)** | **+0.1374** | 0.0610 | ±0.1219 | **+2.254** | **0.0242** | * |
| Hypertension | +0.7106 | 0.7070 | ±1.4140 | +1.005 | 0.3149 |  |
| High cholesterol | +0.6965 | 0.6045 | ±1.2091 | +1.152 | 0.2492 |  |
| Kidney disease | +2.0539 | 1.4987 | ±2.9974 | +1.370 | 0.1705 |  |
| Circulatory disease | +0.8225 | 1.0100 | ±2.0199 | +0.814 | 0.4154 |  |
| Time 54-250, pooled (%) | +0.0458 | 0.0251 | ±0.0502 | +1.824 | 0.0681 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **243**, R² = **0.2053**, Adj R² = **0.1675**, F-statistic = **5.43** (p = **1.13e-07**), Residual SE = **4.568** on **231** df, AIC = **1439.5**, BIC = **1481.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2.7467 | 3.3207 | ±6.6413 | +0.827 | 0.4082 |  |
| Education: graduate level (vs college) | -0.1584 | 0.6143 | ±1.2285 | -0.258 | 0.7966 |  |
| **Education: high school or below (vs college)** | **+3.5311** | 1.5406 | ±3.0813 | **+2.292** | **0.0219** | * |
| Site: UCSD (vs UAB) | -1.3220 | 0.9235 | ±1.8469 | -1.432 | 0.1523 |  |
| Site: UW (vs UAB) | -1.3671 | 0.7808 | ±1.5615 | -1.751 | 0.0799 | . |
| **Age (years)** | **-0.0958** | 0.0294 | ±0.0589 | **-3.255** | **0.0011** | ** |
| **BMI (kg/m2)** | **+0.1381** | 0.0608 | ±0.1216 | **+2.270** | **0.0232** | * |
| Hypertension | +0.7129 | 0.7069 | ±1.4137 | +1.009 | 0.3132 |  |
| High cholesterol | +0.6940 | 0.6047 | ±1.2094 | +1.148 | 0.2511 |  |
| Kidney disease | +2.0483 | 1.4979 | ±2.9958 | +1.367 | 0.1715 |  |
| Circulatory disease | +0.8310 | 1.0116 | ±2.0232 | +0.821 | 0.4114 |  |
| Avg. daily time 54-250 (%) | +0.0472 | 0.0264 | ±0.0528 | +1.788 | 0.0738 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **243**, R² = **0.2032**, Adj R² = **0.1653**, F-statistic = **5.36** (p = **1.48e-07**), Residual SE = **4.574** on **231** df, AIC = **1440.2**, BIC = **1482.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4574** | 2.6278 | ±5.2555 | **+2.838** | **0.0045** | ** |
| Education: graduate level (vs college) | -0.2732 | 0.6417 | ±1.2833 | -0.426 | 0.6702 |  |
| **Education: high school or below (vs college)** | **+3.2353** | 1.4680 | ±2.9359 | **+2.204** | **0.0275** | * |
| Site: UCSD (vs UAB) | -1.2170 | 0.9389 | ±1.8778 | -1.296 | 0.1949 |  |
| Site: UW (vs UAB) | -1.3610 | 0.7825 | ±1.5649 | -1.739 | 0.0820 | . |
| **Age (years)** | **-0.0944** | 0.0299 | ±0.0598 | **-3.153** | **0.0016** | ** |
| BMI (kg/m2) | +0.1186 | 0.0634 | ±0.1269 | +1.869 | 0.0616 | . |
| Hypertension | +0.6681 | 0.7400 | ±1.4800 | +0.903 | 0.3666 |  |
| High cholesterol | +0.6554 | 0.6094 | ±1.2189 | +1.075 | 0.2822 |  |
| Kidney disease | +1.8685 | 1.5733 | ±3.1467 | +1.188 | 0.2350 |  |
| Circulatory disease | +0.5869 | 1.0089 | ±2.0178 | +0.582 | 0.5607 |  |
| Time 181-250, pooled (%) | +0.0451 | 0.0499 | ±0.0997 | +0.905 | 0.3654 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **243**, R² = **0.2036**, Adj R² = **0.1657**, F-statistic = **5.37** (p = **1.40e-07**), Residual SE = **4.573** on **231** df, AIC = **1440.1**, BIC = **1482.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4621** | 2.6222 | ±5.2444 | **+2.846** | **0.0044** | ** |
| Education: graduate level (vs college) | -0.2784 | 0.6418 | ±1.2836 | -0.434 | 0.6645 |  |
| **Education: high school or below (vs college)** | **+3.2470** | 1.4666 | ±2.9332 | **+2.214** | **0.0268** | * |
| Site: UCSD (vs UAB) | -1.2030 | 0.9396 | ±1.8792 | -1.280 | 0.2004 |  |
| Site: UW (vs UAB) | -1.3509 | 0.7825 | ±1.5650 | -1.726 | 0.0843 | . |
| **Age (years)** | **-0.0945** | 0.0299 | ±0.0598 | **-3.160** | **0.0016** | ** |
| BMI (kg/m2) | +0.1187 | 0.0633 | ±0.1266 | +1.875 | 0.0608 | . |
| Hypertension | +0.6669 | 0.7380 | ±1.4760 | +0.904 | 0.3662 |  |
| High cholesterol | +0.6514 | 0.6101 | ±1.2203 | +1.068 | 0.2857 |  |
| Kidney disease | +1.8549 | 1.5817 | ±3.1635 | +1.173 | 0.2409 |  |
| Circulatory disease | +0.5933 | 1.0108 | ±2.0217 | +0.587 | 0.5572 |  |
| Avg. daily time 181-250 (%) | +0.0451 | 0.0484 | ±0.0967 | +0.933 | 0.3507 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **243**, R² = **0.1961**, Adj R² = **0.1578**, F-statistic = **5.12** (p = **3.53e-07**), Residual SE = **4.594** on **231** df, AIC = **1442.3**, BIC = **1484.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3239** | 2.5873 | ±5.1745 | **+2.831** | **0.0046** | ** |
| Education: graduate level (vs college) | -0.1498 | 0.6299 | ±1.2597 | -0.238 | 0.8120 |  |
| **Education: high school or below (vs college)** | **+3.2448** | 1.5200 | ±3.0400 | **+2.135** | **0.0328** | * |
| Site: UCSD (vs UAB) | -1.2706 | 0.9336 | ±1.8671 | -1.361 | 0.1735 |  |
| Site: UW (vs UAB) | -1.3341 | 0.7850 | ±1.5700 | -1.699 | 0.0892 | . |
| **Age (years)** | **-0.0944** | 0.0300 | ±0.0600 | **-3.148** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1367** | 0.0610 | ±0.1219 | **+2.242** | **0.0250** | * |
| Hypertension | +0.7380 | 0.7209 | ±1.4419 | +1.024 | 0.3060 |  |
| High cholesterol | +0.7512 | 0.6084 | ±1.2168 | +1.235 | 0.2169 |  |
| Kidney disease | +2.1054 | 1.5223 | ±3.0447 | +1.383 | 0.1667 |  |
| Circulatory disease | +0.6112 | 1.0321 | ±2.0643 | +0.592 | 0.5538 |  |
| Time > 180 (%) | -0.0039 | 0.0278 | ±0.0555 | -0.139 | 0.8894 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **243**, R² = **0.1960**, Adj R² = **0.1577**, F-statistic = **5.12** (p = **3.56e-07**), Residual SE = **4.594** on **231** df, AIC = **1442.4**, BIC = **1484.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3222** | 2.5861 | ±5.1722 | **+2.831** | **0.0046** | ** |
| Education: graduate level (vs college) | -0.1529 | 0.6307 | ±1.2614 | -0.242 | 0.8085 |  |
| **Education: high school or below (vs college)** | **+3.2357** | 1.5163 | ±3.0325 | **+2.134** | **0.0328** | * |
| Site: UCSD (vs UAB) | -1.2689 | 0.9353 | ±1.8707 | -1.357 | 0.1749 |  |
| Site: UW (vs UAB) | -1.3346 | 0.7856 | ±1.5713 | -1.699 | 0.0894 | . |
| **Age (years)** | **-0.0944** | 0.0300 | ±0.0600 | **-3.148** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1362** | 0.0611 | ±0.1222 | **+2.229** | **0.0258** | * |
| Hypertension | +0.7369 | 0.7215 | ±1.4430 | +1.021 | 0.3071 |  |
| High cholesterol | +0.7499 | 0.6087 | ±1.2173 | +1.232 | 0.2179 |  |
| Kidney disease | +2.1006 | 1.5244 | ±3.0489 | +1.378 | 0.1682 |  |
| Circulatory disease | +0.6042 | 1.0321 | ±2.0641 | +0.585 | 0.5582 |  |
| Avg. daily time > 180 (%) | -0.0026 | 0.0274 | ±0.0548 | -0.095 | 0.9246 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **243**, R² = **0.1965**, Adj R² = **0.1583**, F-statistic = **5.14** (p = **3.35e-07**), Residual SE = **4.593** on **231** df, AIC = **1442.2**, BIC = **1484.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3565** | 2.5988 | ±5.1977 | **+2.831** | **0.0046** | ** |
| Education: graduate level (vs college) | -0.1649 | 0.6275 | ±1.2550 | -0.263 | 0.7927 |  |
| **Education: high school or below (vs college)** | **+3.1796** | 1.5104 | ±3.0208 | **+2.105** | **0.0353** | * |
| Site: UCSD (vs UAB) | -1.2547 | 0.9367 | ±1.8734 | -1.339 | 0.1804 |  |
| Site: UW (vs UAB) | -1.3378 | 0.7855 | ±1.5709 | -1.703 | 0.0885 | . |
| **Age (years)** | **-0.0938** | 0.0300 | ±0.0600 | **-3.124** | **0.0018** | ** |
| **BMI (kg/m2)** | **+0.1312** | 0.0618 | ±0.1236 | **+2.123** | **0.0338** | * |
| Hypertension | +0.7294 | 0.7276 | ±1.4553 | +1.002 | 0.3161 |  |
| High cholesterol | +0.7356 | 0.6099 | ±1.2198 | +1.206 | 0.2278 |  |
| Kidney disease | +2.1027 | 1.5220 | ±3.0440 | +1.382 | 0.1671 |  |
| Circulatory disease | +0.5664 | 1.0376 | ±2.0751 | +0.546 | 0.5851 |  |
| Nocturnal time > 180 (%) | +0.0072 | 0.0286 | ±0.0573 | +0.252 | 0.8010 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **243**, R² = **0.2050**, Adj R² = **0.1672**, F-statistic = **5.42** (p = **1.18e-07**), Residual SE = **4.569** on **231** df, AIC = **1439.6**, BIC = **1481.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4643** | 2.5521 | ±5.1043 | **+2.925** | **0.0034** | ** |
| Education: graduate level (vs college) | -0.1525 | 0.6145 | ±1.2291 | -0.248 | 0.8040 |  |
| **Education: high school or below (vs college)** | **+3.5323** | 1.5420 | ±3.0839 | **+2.291** | **0.0220** | * |
| Site: UCSD (vs UAB) | -1.3107 | 0.9221 | ±1.8441 | -1.421 | 0.1552 |  |
| Site: UW (vs UAB) | -1.3565 | 0.7799 | ±1.5598 | -1.739 | 0.0820 | . |
| **Age (years)** | **-0.0961** | 0.0295 | ±0.0590 | **-3.259** | **0.0011** | ** |
| **BMI (kg/m2)** | **+0.1380** | 0.0609 | ±0.1219 | **+2.264** | **0.0235** | * |
| Hypertension | +0.7160 | 0.7072 | ±1.4143 | +1.012 | 0.3113 |  |
| High cholesterol | +0.7046 | 0.6044 | ±1.2087 | +1.166 | 0.2437 |  |
| Kidney disease | +2.0554 | 1.4986 | ±2.9973 | +1.372 | 0.1702 |  |
| Circulatory disease | +0.8235 | 1.0108 | ±2.0216 | +0.815 | 0.4152 |  |
| Time > 250 (%) | -0.0456 | 0.0253 | ±0.0506 | -1.802 | 0.0715 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **243**, R² = **0.2051**, Adj R² = **0.1672**, F-statistic = **5.42** (p = **1.17e-07**), Residual SE = **4.568** on **231** df, AIC = **1439.6**, BIC = **1481.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4454** | 2.5475 | ±5.0949 | **+2.923** | **0.0035** | ** |
| Education: graduate level (vs college) | -0.1515 | 0.6145 | ±1.2290 | -0.247 | 0.8052 |  |
| **Education: high school or below (vs college)** | **+3.5367** | 1.5433 | ±3.0867 | **+2.292** | **0.0219** | * |
| Site: UCSD (vs UAB) | -1.3129 | 0.9227 | ±1.8455 | -1.423 | 0.1548 |  |
| Site: UW (vs UAB) | -1.3536 | 0.7795 | ±1.5590 | -1.737 | 0.0825 | . |
| **Age (years)** | **-0.0960** | 0.0295 | ±0.0589 | **-3.260** | **0.0011** | ** |
| **BMI (kg/m2)** | **+0.1384** | 0.0608 | ±0.1216 | **+2.276** | **0.0228** | * |
| Hypertension | +0.7175 | 0.7070 | ±1.4140 | +1.015 | 0.3102 |  |
| High cholesterol | +0.7020 | 0.6045 | ±1.2090 | +1.161 | 0.2455 |  |
| Kidney disease | +2.0495 | 1.4979 | ±2.9958 | +1.368 | 0.1712 |  |
| Circulatory disease | +0.8294 | 1.0122 | ±2.0243 | +0.819 | 0.4126 |  |
| Avg. daily time > 250 (%) | -0.0467 | 0.0265 | ±0.0530 | -1.759 | 0.0785 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 243; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1431**, LLR χ² = **34.16** (p = **1.74e-04**), AUC = **0.7390**, AIC = **226.5**, BIC = **265.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6125 | 1.4814 | ±2.9629 | -1.088 | 0.2764 | 0.1994 |  |
| Education: graduate level (vs college) | +0.0272 | 0.3880 | ±0.7761 | +0.070 | 0.9440 | 1.0276 |  |
| Education: high school or below (vs college) | +0.4108 | 0.5980 | ±1.1960 | +0.687 | 0.4921 | 1.5081 |  |
| Site: UCSD (vs UAB) | -0.5578 | 0.4606 | ±0.9211 | -1.211 | 0.2259 | 0.5725 |  |
| **Site: UW (vs UAB)** | **-0.8610** | 0.4289 | ±0.8579 | **-2.007** | **0.0447** | 0.4228 | * |
| Age (years) | -0.0343 | 0.0184 | ±0.0369 | -1.863 | 0.0624 | 0.9662 | . |
| **BMI (kg/m2)** | **+0.0739** | 0.0255 | ±0.0510 | **+2.896** | **0.0038** | 1.0767 | ** |
| Hypertension | +0.2124 | 0.4177 | ±0.8353 | +0.508 | 0.6111 | 1.2366 |  |
| High cholesterol | +0.3930 | 0.3879 | ±0.7758 | +1.013 | 0.3110 | 1.4814 |  |
| Kidney disease | +0.5772 | 0.5872 | ±1.1744 | +0.983 | 0.3256 | 1.7811 |  |
| Circulatory disease | +0.9472 | 0.4881 | ±0.9763 | +1.940 | 0.0523 | 2.5785 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1434**, LLR χ² = **34.24** (p = **3.31e-04**), AUC = **0.7395**, AIC = **228.5**, BIC = **270.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.8781 | 1.7504 | ±3.5007 | -1.073 | 0.2833 | 0.1529 |  |
| Education: graduate level (vs college) | +0.0291 | 0.3882 | ±0.7763 | +0.075 | 0.9403 | 1.0295 |  |
| Education: high school or below (vs college) | +0.3859 | 0.6036 | ±1.2072 | +0.639 | 0.5226 | 1.4710 |  |
| Site: UCSD (vs UAB) | -0.5569 | 0.4604 | ±0.9208 | -1.210 | 0.2264 | 0.5730 |  |
| **Site: UW (vs UAB)** | **-0.8654** | 0.4293 | ±0.8587 | **-2.016** | **0.0438** | 0.4209 | * |
| Age (years) | -0.0344 | 0.0184 | ±0.0369 | -1.866 | 0.0620 | 0.9662 | . |
| **BMI (kg/m2)** | **+0.0735** | 0.0256 | ±0.0511 | **+2.873** | **0.0041** | 1.0762 | ** |
| Hypertension | +0.2122 | 0.4174 | ±0.8348 | +0.508 | 0.6111 | 1.2365 |  |
| High cholesterol | +0.3872 | 0.3885 | ±0.7769 | +0.997 | 0.3189 | 1.4729 |  |
| Kidney disease | +0.5871 | 0.5880 | ±1.1760 | +0.998 | 0.3181 | 1.7987 |  |
| Circulatory disease | +0.9209 | 0.4962 | ±0.9924 | +1.856 | 0.0635 | 2.5114 | . |
| HbA1c (%) | +0.0482 | 0.1682 | ±0.3365 | +0.287 | 0.7743 | 1.0494 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1452**, LLR χ² = **34.66** (p = **2.81e-04**), AUC = **0.7400**, AIC = **228.0**, BIC = **269.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.0614 | 1.6129 | ±3.2258 | -1.278 | 0.2012 | 0.1273 |  |
| Education: graduate level (vs college) | +0.0034 | 0.3895 | ±0.7791 | +0.009 | 0.9930 | 1.0034 |  |
| Education: high school or below (vs college) | +0.3431 | 0.6054 | ±1.2108 | +0.567 | 0.5709 | 1.4094 |  |
| Site: UCSD (vs UAB) | -0.5552 | 0.4612 | ±0.9223 | -1.204 | 0.2287 | 0.5740 |  |
| **Site: UW (vs UAB)** | **-0.8648** | 0.4294 | ±0.8588 | **-2.014** | **0.0440** | 0.4212 | * |
| Age (years) | -0.0342 | 0.0185 | ±0.0369 | -1.852 | 0.0641 | 0.9664 | . |
| **BMI (kg/m2)** | **+0.0717** | 0.0257 | ±0.0515 | **+2.786** | **0.0053** | 1.0743 | ** |
| Hypertension | +0.2115 | 0.4174 | ±0.8349 | +0.507 | 0.6124 | 1.2355 |  |
| High cholesterol | +0.3746 | 0.3890 | ±0.7780 | +0.963 | 0.3356 | 1.4544 |  |
| Kidney disease | +0.5700 | 0.5893 | ±1.1786 | +0.967 | 0.3334 | 1.7683 |  |
| Circulatory disease | +0.8935 | 0.4943 | ±0.9886 | +1.808 | 0.0707 | 2.4437 | . |
| Mean glucose (mg/dL) | +0.0038 | 0.0053 | ±0.0105 | +0.721 | 0.4706 | 1.0038 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1452**, LLR χ² = **34.66** (p = **2.81e-04**), AUC = **0.7400**, AIC = **228.0**, BIC = **269.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.5864 | 2.0116 | ±4.0232 | -1.286 | 0.1985 | 0.0753 |  |
| Education: graduate level (vs college) | +0.0034 | 0.3895 | ±0.7791 | +0.009 | 0.9930 | 1.0034 |  |
| Education: high school or below (vs college) | +0.3431 | 0.6054 | ±1.2108 | +0.567 | 0.5709 | 1.4094 |  |
| Site: UCSD (vs UAB) | -0.5552 | 0.4612 | ±0.9223 | -1.204 | 0.2287 | 0.5740 |  |
| **Site: UW (vs UAB)** | **-0.8648** | 0.4294 | ±0.8588 | **-2.014** | **0.0440** | 0.4212 | * |
| Age (years) | -0.0342 | 0.0185 | ±0.0369 | -1.852 | 0.0641 | 0.9664 | . |
| **BMI (kg/m2)** | **+0.0717** | 0.0257 | ±0.0515 | **+2.786** | **0.0053** | 1.0743 | ** |
| Hypertension | +0.2115 | 0.4174 | ±0.8349 | +0.507 | 0.6124 | 1.2355 |  |
| High cholesterol | +0.3746 | 0.3890 | ±0.7780 | +0.963 | 0.3356 | 1.4544 |  |
| Kidney disease | +0.5700 | 0.5893 | ±1.1786 | +0.967 | 0.3334 | 1.7683 |  |
| Circulatory disease | +0.8935 | 0.4943 | ±0.9886 | +1.808 | 0.0707 | 2.4437 | . |
| GMI (%) | +0.1586 | 0.2198 | ±0.4396 | +0.721 | 0.4706 | 1.1719 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1491**, LLR χ² = **35.60** (p = **1.97e-04**), AUC = **0.7435**, AIC = **227.1**, BIC = **269.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.2771 | 1.5912 | ±3.1825 | -1.431 | 0.1524 | 0.1026 |  |
| Education: graduate level (vs college) | +0.0016 | 0.3893 | ±0.7787 | +0.004 | 0.9968 | 1.0016 |  |
| Education: high school or below (vs college) | +0.2994 | 0.6085 | ±1.2170 | +0.492 | 0.6227 | 1.3491 |  |
| Site: UCSD (vs UAB) | -0.5698 | 0.4626 | ±0.9253 | -1.232 | 0.2181 | 0.5656 |  |
| **Site: UW (vs UAB)** | **-0.8665** | 0.4303 | ±0.8607 | **-2.014** | **0.0441** | 0.4204 | * |
| Age (years) | -0.0337 | 0.0185 | ±0.0371 | -1.816 | 0.0694 | 0.9669 | . |
| **BMI (kg/m2)** | **+0.0698** | 0.0259 | ±0.0518 | **+2.694** | **0.0071** | 1.0723 | ** |
| Hypertension | +0.2131 | 0.4183 | ±0.8366 | +0.510 | 0.6104 | 1.2376 |  |
| High cholesterol | +0.3597 | 0.3904 | ±0.7808 | +0.921 | 0.3568 | 1.4329 |  |
| Kidney disease | +0.6219 | 0.5896 | ±1.1793 | +1.055 | 0.2915 | 1.8625 |  |
| Circulatory disease | +0.8730 | 0.4935 | ±0.9870 | +1.769 | 0.0769 | 2.3940 | . |
| Nocturnal mean 00-06h (mg/dL) | +0.0057 | 0.0047 | ±0.0095 | +1.210 | 0.2262 | 1.0057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1481**, LLR χ² = **35.36** (p = **2.16e-04**), AUC = **0.7438**, AIC = **227.3**, BIC = **269.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0501 | 1.5695 | ±3.1390 | -0.669 | 0.5034 | 0.3499 |  |
| Education: graduate level (vs college) | +0.0317 | 0.3888 | ±0.7776 | +0.082 | 0.9350 | 1.0322 |  |
| Education: high school or below (vs college) | +0.3941 | 0.6058 | ±1.2117 | +0.650 | 0.5154 | 1.4830 |  |
| Site: UCSD (vs UAB) | -0.5757 | 0.4630 | ±0.9261 | -1.243 | 0.2137 | 0.5623 |  |
| **Site: UW (vs UAB)** | **-0.8795** | 0.4306 | ±0.8612 | **-2.042** | **0.0411** | 0.4150 | * |
| Age (years) | -0.0335 | 0.0185 | ±0.0369 | -1.814 | 0.0696 | 0.9671 | . |
| **BMI (kg/m2)** | **+0.0802** | 0.0264 | ±0.0528 | **+3.038** | **0.0024** | 1.0835 | ** |
| Hypertension | +0.2290 | 0.4173 | ±0.8345 | +0.549 | 0.5831 | 1.2574 |  |
| High cholesterol | +0.3627 | 0.3900 | ±0.7800 | +0.930 | 0.3524 | 1.4372 |  |
| Kidney disease | +0.6958 | 0.5986 | ±1.1972 | +1.162 | 0.2451 | 2.0054 |  |
| **Circulatory disease** | **+1.0333** | 0.4945 | ±0.9889 | **+2.090** | **0.0366** | 2.8103 | * |
| Glucose SD, pooled (mg/dL) | -0.0262 | 0.0244 | ±0.0487 | -1.076 | 0.2818 | 0.9741 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1529**, LLR χ² = **36.49** (p = **1.40e-04**), AUC = **0.7497**, AIC = **226.2**, BIC = **268.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8469 | 1.5668 | ±3.1337 | -0.541 | 0.5888 | 0.4287 |  |
| Education: graduate level (vs college) | +0.0501 | 0.3904 | ±0.7809 | +0.128 | 0.8979 | 1.0514 |  |
| Education: high school or below (vs college) | +0.3605 | 0.6113 | ±1.2226 | +0.590 | 0.5554 | 1.4340 |  |
| Site: UCSD (vs UAB) | -0.5913 | 0.4645 | ±0.9289 | -1.273 | 0.2030 | 0.5536 |  |
| **Site: UW (vs UAB)** | **-0.8965** | 0.4327 | ±0.8654 | **-2.072** | **0.0383** | 0.4080 | * |
| Age (years) | -0.0338 | 0.0185 | ±0.0370 | -1.823 | 0.0683 | 0.9668 | . |
| **BMI (kg/m2)** | **+0.0837** | 0.0267 | ±0.0535 | **+3.130** | **0.0017** | 1.0873 | ** |
| Hypertension | +0.2318 | 0.4186 | ±0.8373 | +0.554 | 0.5798 | 1.2608 |  |
| High cholesterol | +0.3586 | 0.3913 | ±0.7826 | +0.916 | 0.3594 | 1.4314 |  |
| Kidney disease | +0.7442 | 0.5998 | ±1.1996 | +1.241 | 0.2147 | 2.1047 |  |
| **Circulatory disease** | **+1.0767** | 0.4968 | ±0.9937 | **+2.167** | **0.0302** | 2.9351 | * |
| Avg. daily SD (mg/dL) | -0.0396 | 0.0266 | ±0.0532 | -1.490 | 0.1362 | 0.9612 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1640**, LLR χ² = **39.14** (p = **5.01e-05**), AUC = **0.7528**, AIC = **223.5**, BIC = **265.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.1815 | 1.7228 | ±3.4455 | +0.105 | 0.9161 | 1.1991 |  |
| Education: graduate level (vs college) | -0.0506 | 0.3911 | ±0.7822 | -0.129 | 0.8971 | 0.9507 |  |
| Education: high school or below (vs college) | +0.1972 | 0.6149 | ±1.2297 | +0.321 | 0.7484 | 1.2180 |  |
| Site: UCSD (vs UAB) | -0.6292 | 0.4693 | ±0.9387 | -1.341 | 0.1800 | 0.5330 |  |
| **Site: UW (vs UAB)** | **-0.9579** | 0.4356 | ±0.8711 | **-2.199** | **0.0279** | 0.3837 | * |
| Age (years) | -0.0324 | 0.0186 | ±0.0372 | -1.740 | 0.0819 | 0.9681 | . |
| **BMI (kg/m2)** | **+0.0807** | 0.0263 | ±0.0525 | **+3.074** | **0.0021** | 1.0841 | ** |
| Hypertension | +0.2469 | 0.4163 | ±0.8327 | +0.593 | 0.5532 | 1.2800 |  |
| High cholesterol | +0.2429 | 0.3940 | ±0.7879 | +0.617 | 0.5375 | 1.2749 |  |
| Kidney disease | +0.7990 | 0.6065 | ±1.2130 | +1.317 | 0.1877 | 2.2234 |  |
| **Circulatory disease** | **+0.9964** | 0.4884 | ±0.9769 | **+2.040** | **0.0414** | 2.7084 | * |
| **CV (%)** | **-0.0914** | 0.0434 | ±0.0868 | **-2.105** | **0.0353** | 0.9127 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1629**, LLR χ² = **38.87** (p = **5.57e-05**), AUC = **0.7566**, AIC = **223.8**, BIC = **265.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.7677** | 1.8157 | ±3.6313 | **-2.075** | **0.0380** | 0.0231 | * |
| Education: graduate level (vs college) | -0.0126 | 0.3913 | ±0.7825 | -0.032 | 0.9743 | 0.9875 |  |
| Education: high school or below (vs college) | +0.2436 | 0.6126 | ±1.2251 | +0.398 | 0.6908 | 1.2759 |  |
| Site: UCSD (vs UAB) | -0.6247 | 0.4683 | ±0.9366 | -1.334 | 0.1822 | 0.5354 |  |
| **Site: UW (vs UAB)** | **-0.9662** | 0.4374 | ±0.8748 | **-2.209** | **0.0272** | 0.3805 | * |
| Age (years) | -0.0336 | 0.0186 | ±0.0373 | -1.800 | 0.0719 | 0.9670 | . |
| **BMI (kg/m2)** | **+0.0790** | 0.0261 | ±0.0523 | **+3.021** | **0.0025** | 1.0822 | ** |
| Hypertension | +0.2702 | 0.4172 | ±0.8343 | +0.648 | 0.5172 | 1.3102 |  |
| High cholesterol | +0.2794 | 0.3933 | ±0.7867 | +0.710 | 0.4774 | 1.3224 |  |
| Kidney disease | +0.7672 | 0.6040 | ±1.2081 | +1.270 | 0.2040 | 2.1538 |  |
| **Circulatory disease** | **+1.0059** | 0.4910 | ±0.9821 | **+2.049** | **0.0405** | 2.7345 | * |
| **Mean / SD ratio** | **+0.4249** | 0.1976 | ±0.3952 | **+2.151** | **0.0315** | 1.5295 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1705**, LLR χ² = **40.70** (p = **2.71e-05**), AUC = **0.7635**, AIC = **222.0**, BIC = **263.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.9814** | 1.7911 | ±3.5823 | **-2.223** | **0.0262** | 0.0187 | * |
| Education: graduate level (vs college) | +0.0258 | 0.3927 | ±0.7854 | +0.066 | 0.9476 | 1.0261 |  |
| Education: high school or below (vs college) | +0.2012 | 0.6210 | ±1.2420 | +0.324 | 0.7459 | 1.2229 |  |
| Site: UCSD (vs UAB) | -0.6206 | 0.4686 | ±0.9372 | -1.324 | 0.1854 | 0.5376 |  |
| **Site: UW (vs UAB)** | **-1.0195** | 0.4428 | ±0.8857 | **-2.302** | **0.0213** | 0.3608 | * |
| Age (years) | -0.0336 | 0.0188 | ±0.0376 | -1.788 | 0.0738 | 0.9670 | . |
| **BMI (kg/m2)** | **+0.0830** | 0.0265 | ±0.0531 | **+3.126** | **0.0018** | 1.0865 | ** |
| Hypertension | +0.2595 | 0.4217 | ±0.8433 | +0.615 | 0.5383 | 1.2963 |  |
| High cholesterol | +0.2786 | 0.3970 | ±0.7941 | +0.702 | 0.4829 | 1.3212 |  |
| Kidney disease | +0.8186 | 0.6046 | ±1.2093 | +1.354 | 0.1758 | 2.2672 |  |
| **Circulatory disease** | **+1.0168** | 0.4942 | ±0.9884 | **+2.057** | **0.0396** | 2.7642 | * |
| **Avg. daily mean/SD** | **+0.3819** | 0.1508 | ±0.3015 | **+2.533** | **0.0113** | 1.4651 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1474**, LLR χ² = **35.17** (p = **2.32e-04**), AUC = **0.7398**, AIC = **227.5**, BIC = **269.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7343 | 1.7205 | ±3.4410 | -0.427 | 0.6695 | 0.4798 |  |
| Education: graduate level (vs college) | -0.0128 | 0.3902 | ±0.7804 | -0.033 | 0.9739 | 0.9873 |  |
| Education: high school or below (vs college) | +0.3585 | 0.6055 | ±1.2109 | +0.592 | 0.5537 | 1.4312 |  |
| Site: UCSD (vs UAB) | -0.6111 | 0.4646 | ±0.9292 | -1.315 | 0.1884 | 0.5428 |  |
| **Site: UW (vs UAB)** | **-0.9591** | 0.4407 | ±0.8815 | **-2.176** | **0.0295** | 0.3832 | * |
| Age (years) | -0.0346 | 0.0185 | ±0.0370 | -1.872 | 0.0613 | 0.9660 | . |
| **BMI (kg/m2)** | **+0.0799** | 0.0263 | ±0.0527 | **+3.035** | **0.0024** | 1.0832 | ** |
| Hypertension | +0.1776 | 0.4201 | ±0.8402 | +0.423 | 0.6725 | 1.1943 |  |
| High cholesterol | +0.3149 | 0.3960 | ±0.7920 | +0.795 | 0.4265 | 1.3702 |  |
| Kidney disease | +0.5500 | 0.5941 | ±1.1882 | +0.926 | 0.3545 | 1.7333 |  |
| **Circulatory disease** | **+0.9998** | 0.4902 | ±0.9803 | **+2.040** | **0.0414** | 2.7178 | * |
| MAG (mg/dL/h) | -0.0207 | 0.0207 | ±0.0413 | -0.999 | 0.3176 | 0.9796 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1547**, LLR χ² = **36.92** (p = **1.19e-04**), AUC = **0.7498**, AIC = **225.8**, BIC = **267.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2793 | 1.6851 | ±3.3703 | -0.166 | 0.8684 | 0.7563 |  |
| Education: graduate level (vs college) | +0.0409 | 0.3903 | ±0.7807 | +0.105 | 0.9166 | 1.0417 |  |
| Education: high school or below (vs college) | +0.3560 | 0.6124 | ±1.2248 | +0.581 | 0.5610 | 1.4276 |  |
| Site: UCSD (vs UAB) | -0.6287 | 0.4656 | ±0.9313 | -1.350 | 0.1770 | 0.5333 |  |
| **Site: UW (vs UAB)** | **-0.9483** | 0.4362 | ±0.8723 | **-2.174** | **0.0297** | 0.3874 | * |
| Age (years) | -0.0350 | 0.0185 | ±0.0370 | -1.890 | 0.0587 | 0.9656 | . |
| **BMI (kg/m2)** | **+0.0831** | 0.0266 | ±0.0531 | **+3.130** | **0.0018** | 1.0867 | ** |
| Hypertension | +0.2094 | 0.4200 | ±0.8400 | +0.499 | 0.6180 | 1.2330 |  |
| High cholesterol | +0.3060 | 0.3941 | ±0.7882 | +0.776 | 0.4375 | 1.3580 |  |
| Kidney disease | +0.6686 | 0.5971 | ±1.1943 | +1.120 | 0.2628 | 1.9516 |  |
| **Circulatory disease** | **+1.0845** | 0.4964 | ±0.9927 | **+2.185** | **0.0289** | 2.9580 | * |
| Avg. daily range (mg/dL) | -0.0113 | 0.0069 | ±0.0139 | -1.622 | 0.1048 | 0.9888 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1450**, LLR χ² = **34.60** (p = **2.88e-04**), AUC = **0.7388**, AIC = **228.1**, BIC = **270.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6654 | 1.4849 | ±2.9699 | -1.122 | 0.2621 | 0.1891 |  |
| Education: graduate level (vs college) | +0.0440 | 0.3900 | ±0.7800 | +0.113 | 0.9101 | 1.0450 |  |
| Education: high school or below (vs college) | +0.3886 | 0.5987 | ±1.1973 | +0.649 | 0.5163 | 1.4749 |  |
| Site: UCSD (vs UAB) | -0.5574 | 0.4614 | ±0.9228 | -1.208 | 0.2270 | 0.5727 |  |
| **Site: UW (vs UAB)** | **-0.8671** | 0.4302 | ±0.8604 | **-2.015** | **0.0439** | 0.4202 | * |
| Age (years) | -0.0359 | 0.0187 | ±0.0374 | -1.924 | 0.0544 | 0.9647 | . |
| **BMI (kg/m2)** | **+0.0716** | 0.0257 | ±0.0515 | **+2.781** | **0.0054** | 1.0742 | ** |
| Hypertension | +0.2133 | 0.4196 | ±0.8392 | +0.508 | 0.6113 | 1.2377 |  |
| High cholesterol | +0.4013 | 0.3893 | ±0.7786 | +1.031 | 0.3026 | 1.4938 |  |
| Kidney disease | +0.5570 | 0.5893 | ±1.1787 | +0.945 | 0.3446 | 1.7455 |  |
| Circulatory disease | +0.9432 | 0.4891 | ±0.9783 | +1.928 | 0.0538 | 2.5682 | . |
| SD of daily means (mg/dL) | +0.0236 | 0.0350 | ±0.0701 | +0.673 | 0.5012 | 1.0238 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1431**, LLR χ² = **34.17** (p = **3.40e-04**), AUC = **0.7387**, AIC = **228.5**, BIC = **270.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5175 | 1.7928 | ±3.5855 | -0.846 | 0.3973 | 0.2193 |  |
| Education: graduate level (vs college) | +0.0253 | 0.3886 | ±0.7772 | +0.065 | 0.9481 | 1.0256 |  |
| Education: high school or below (vs college) | +0.4058 | 0.6001 | ±1.2001 | +0.676 | 0.4989 | 1.5005 |  |
| Site: UCSD (vs UAB) | -0.5569 | 0.4606 | ±0.9213 | -1.209 | 0.2267 | 0.5730 |  |
| **Site: UW (vs UAB)** | **-0.8603** | 0.4290 | ±0.8581 | **-2.005** | **0.0449** | 0.4230 | * |
| Age (years) | -0.0343 | 0.0184 | ±0.0369 | -1.862 | 0.0626 | 0.9663 | . |
| **BMI (kg/m2)** | **+0.0734** | 0.0260 | ±0.0520 | **+2.827** | **0.0047** | 1.0762 | ** |
| Hypertension | +0.2119 | 0.4176 | ±0.8353 | +0.507 | 0.6118 | 1.2361 |  |
| High cholesterol | +0.3913 | 0.3883 | ±0.7765 | +1.008 | 0.3136 | 1.4789 |  |
| Kidney disease | +0.5728 | 0.5892 | ±1.1784 | +0.972 | 0.3310 | 1.7733 |  |
| Circulatory disease | +0.9416 | 0.4917 | ±0.9833 | +1.915 | 0.0555 | 2.5642 | . |
| Time in range 70-180, pooled (%) | -0.0009 | 0.0099 | ±0.0198 | -0.094 | 0.9251 | 0.9991 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1432**, LLR χ² = **34.17** (p = **3.39e-04**), AUC = **0.7388**, AIC = **228.5**, BIC = **270.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4940 | 1.7887 | ±3.5773 | -0.835 | 0.4036 | 0.2245 |  |
| Education: graduate level (vs college) | +0.0245 | 0.3887 | ±0.7774 | +0.063 | 0.9498 | 1.0248 |  |
| Education: high school or below (vs college) | +0.4048 | 0.5997 | ±1.1995 | +0.675 | 0.4997 | 1.4991 |  |
| Site: UCSD (vs UAB) | -0.5561 | 0.4608 | ±0.9215 | -1.207 | 0.2275 | 0.5735 |  |
| **Site: UW (vs UAB)** | **-0.8597** | 0.4291 | ±0.8582 | **-2.003** | **0.0451** | 0.4233 | * |
| Age (years) | -0.0343 | 0.0184 | ±0.0369 | -1.862 | 0.0625 | 0.9663 | . |
| **BMI (kg/m2)** | **+0.0733** | 0.0260 | ±0.0519 | **+2.824** | **0.0047** | 1.0761 | ** |
| Hypertension | +0.2118 | 0.4176 | ±0.8353 | +0.507 | 0.6121 | 1.2358 |  |
| High cholesterol | +0.3909 | 0.3882 | ±0.7765 | +1.007 | 0.3140 | 1.4783 |  |
| Kidney disease | +0.5715 | 0.5894 | ±1.1789 | +0.969 | 0.3323 | 1.7708 |  |
| Circulatory disease | +0.9405 | 0.4913 | ±0.9826 | +1.914 | 0.0556 | 2.5613 | . |
| Avg. daily time in range 70-180 (%) | -0.0012 | 0.0098 | ±0.0196 | -0.118 | 0.9060 | 0.9988 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1490**, LLR χ² = **35.57** (p = **2.00e-04**), AUC = **0.7434**, AIC = **227.1**, BIC = **269.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6939 | 1.4853 | ±2.9705 | -1.140 | 0.2541 | 0.1838 |  |
| Education: graduate level (vs college) | +0.0838 | 0.3939 | ±0.7877 | +0.213 | 0.8314 | 1.0875 |  |
| Education: high school or below (vs college) | +0.4841 | 0.6030 | ±1.2059 | +0.803 | 0.4220 | 1.6227 |  |
| Site: UCSD (vs UAB) | -0.5486 | 0.4618 | ±0.9237 | -1.188 | 0.2349 | 0.5778 |  |
| Site: UW (vs UAB) | -0.8352 | 0.4313 | ±0.8625 | -1.937 | 0.0528 | 0.4338 | . |
| Age (years) | -0.0355 | 0.0185 | ±0.0370 | -1.919 | 0.0550 | 0.9651 | . |
| **BMI (kg/m2)** | **+0.0725** | 0.0256 | ±0.0512 | **+2.833** | **0.0046** | 1.0752 | ** |
| Hypertension | +0.2004 | 0.4237 | ±0.8473 | +0.473 | 0.6362 | 1.2219 |  |
| High cholesterol | +0.4252 | 0.3914 | ±0.7829 | +1.086 | 0.2774 | 1.5299 |  |
| Kidney disease | +0.5477 | 0.5928 | ±1.1855 | +0.924 | 0.3555 | 1.7293 |  |
| Circulatory disease | +0.9496 | 0.4888 | ±0.9776 | +1.943 | 0.0521 | 2.5848 | . |
| Any reading < 54 during wear (0/1) | +0.4615 | 0.3847 | ±0.7693 | +1.200 | 0.2303 | 1.5864 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1455**, LLR χ² = **34.73** (p = **2.75e-04**), AUC = **0.7412**, AIC = **228.0**, BIC = **269.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5858 | 1.4796 | ±2.9591 | -1.072 | 0.2838 | 0.2048 |  |
| Education: graduate level (vs college) | -0.0113 | 0.3907 | ±0.7815 | -0.029 | 0.9769 | 0.9887 |  |
| Education: high school or below (vs college) | +0.3549 | 0.6027 | ±1.2053 | +0.589 | 0.5559 | 1.4261 |  |
| Site: UCSD (vs UAB) | -0.5660 | 0.4606 | ±0.9212 | -1.229 | 0.2191 | 0.5678 |  |
| **Site: UW (vs UAB)** | **-0.8886** | 0.4293 | ±0.8586 | **-2.070** | **0.0385** | 0.4112 | * |
| Age (years) | -0.0332 | 0.0184 | ±0.0369 | -1.801 | 0.0717 | 0.9673 | . |
| **BMI (kg/m2)** | **+0.0741** | 0.0256 | ±0.0512 | **+2.899** | **0.0037** | 1.0770 | ** |
| Hypertension | +0.2125 | 0.4169 | ±0.8338 | +0.510 | 0.6102 | 1.2368 |  |
| High cholesterol | +0.3527 | 0.3907 | ±0.7814 | +0.903 | 0.3667 | 1.4229 |  |
| Kidney disease | +0.5739 | 0.5862 | ±1.1724 | +0.979 | 0.3276 | 1.7751 |  |
| Circulatory disease | +0.9348 | 0.4880 | ±0.9760 | +1.916 | 0.0554 | 2.5468 | . |
| Time < 54 (%) | -0.4103 | 0.6567 | ±1.3135 | -0.625 | 0.5321 | 0.6634 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1527**, LLR χ² = **36.44** (p = **1.43e-04**), AUC = **0.7478**, AIC = **226.3**, BIC = **268.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5858 | 1.4785 | ±2.9569 | -1.073 | 0.2834 | 0.2048 |  |
| Education: graduate level (vs college) | -0.0454 | 0.3896 | ±0.7792 | -0.116 | 0.9073 | 0.9557 |  |
| Education: high school or below (vs college) | +0.2969 | 0.6042 | ±1.2085 | +0.491 | 0.6232 | 1.3456 |  |
| Site: UCSD (vs UAB) | -0.5801 | 0.4612 | ±0.9223 | -1.258 | 0.2084 | 0.5598 |  |
| **Site: UW (vs UAB)** | **-0.9298** | 0.4291 | ±0.8581 | **-2.167** | **0.0302** | 0.3946 | * |
| Age (years) | -0.0326 | 0.0184 | ±0.0369 | -1.766 | 0.0774 | 0.9680 | . |
| **BMI (kg/m2)** | **+0.0758** | 0.0256 | ±0.0513 | **+2.957** | **0.0031** | 1.0788 | ** |
| Hypertension | +0.2239 | 0.4180 | ±0.8360 | +0.536 | 0.5922 | 1.2509 |  |
| High cholesterol | +0.2993 | 0.3919 | ±0.7839 | +0.764 | 0.4451 | 1.3489 |  |
| Kidney disease | +0.5917 | 0.5866 | ±1.1732 | +1.009 | 0.3131 | 1.8071 |  |
| Circulatory disease | +0.9351 | 0.4889 | ±0.9777 | +1.913 | 0.0558 | 2.5475 | . |
| Avg. daily time < 54 (%) | -1.3449 | 1.3147 | ±2.6293 | -1.023 | 0.3063 | 0.2606 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1546**, LLR χ² = **36.91** (p = **1.19e-04**), AUC = **0.7474**, AIC = **225.8**, BIC = **267.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5505 | 1.4860 | ±2.9719 | -1.043 | 0.2968 | 0.2121 |  |
| Education: graduate level (vs college) | -0.0906 | 0.3933 | ±0.7866 | -0.230 | 0.8179 | 0.9134 |  |
| Education: high school or below (vs college) | +0.3016 | 0.6004 | ±1.2008 | +0.502 | 0.6155 | 1.3520 |  |
| Site: UCSD (vs UAB) | -0.5739 | 0.4634 | ±0.9268 | -1.238 | 0.2156 | 0.5634 |  |
| **Site: UW (vs UAB)** | **-0.9021** | 0.4301 | ±0.8601 | **-2.098** | **0.0359** | 0.4057 | * |
| Age (years) | -0.0326 | 0.0184 | ±0.0369 | -1.769 | 0.0768 | 0.9679 | . |
| **BMI (kg/m2)** | **+0.0774** | 0.0258 | ±0.0516 | **+2.998** | **0.0027** | 1.0804 | ** |
| Hypertension | +0.2379 | 0.4186 | ±0.8371 | +0.568 | 0.5697 | 1.2686 |  |
| High cholesterol | +0.2535 | 0.3957 | ±0.7915 | +0.641 | 0.5218 | 1.2885 |  |
| Kidney disease | +0.6181 | 0.5935 | ±1.1870 | +1.041 | 0.2976 | 1.8555 |  |
| Circulatory disease | +0.9190 | 0.4894 | ±0.9789 | +1.878 | 0.0604 | 2.5069 | . |
| Time 54-69, pooled (%) | -0.3932 | 0.3129 | ±0.6257 | -1.257 | 0.2088 | 0.6749 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1554**, LLR χ² = **37.09** (p = **1.11e-04**), AUC = **0.7451**, AIC = **225.6**, BIC = **267.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5459 | 1.4876 | ±2.9751 | -1.039 | 0.2987 | 0.2131 |  |
| Education: graduate level (vs college) | -0.0991 | 0.3938 | ±0.7875 | -0.252 | 0.8013 | 0.9056 |  |
| Education: high school or below (vs college) | +0.2767 | 0.6039 | ±1.2078 | +0.458 | 0.6469 | 1.3187 |  |
| Site: UCSD (vs UAB) | -0.5676 | 0.4638 | ±0.9276 | -1.224 | 0.2210 | 0.5669 |  |
| **Site: UW (vs UAB)** | **-0.9140** | 0.4303 | ±0.8607 | **-2.124** | **0.0337** | 0.4009 | * |
| Age (years) | -0.0324 | 0.0184 | ±0.0368 | -1.758 | 0.0787 | 0.9682 | . |
| **BMI (kg/m2)** | **+0.0769** | 0.0258 | ±0.0517 | **+2.975** | **0.0029** | 1.0799 | ** |
| Hypertension | +0.2404 | 0.4191 | ±0.8382 | +0.574 | 0.5662 | 1.2718 |  |
| High cholesterol | +0.2390 | 0.3968 | ±0.7937 | +0.602 | 0.5471 | 1.2699 |  |
| Kidney disease | +0.6247 | 0.5932 | ±1.1864 | +1.053 | 0.2923 | 1.8677 |  |
| Circulatory disease | +0.9061 | 0.4904 | ±0.9807 | +1.848 | 0.0646 | 2.4747 | . |
| Avg. daily time 54-69 (%) | -0.4327 | 0.3462 | ±0.6925 | -1.250 | 0.2114 | 0.6488 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1521**, LLR χ² = **36.31** (p = **1.50e-04**), AUC = **0.7465**, AIC = **226.4**, BIC = **268.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5586 | 1.4826 | ±2.9652 | -1.051 | 0.2931 | 0.2104 |  |
| Education: graduate level (vs college) | -0.0720 | 0.3928 | ±0.7856 | -0.183 | 0.8545 | 0.9305 |  |
| Education: high school or below (vs college) | +0.3067 | 0.6012 | ±1.2024 | +0.510 | 0.6099 | 1.3590 |  |
| Site: UCSD (vs UAB) | -0.5726 | 0.4624 | ±0.9247 | -1.238 | 0.2156 | 0.5640 |  |
| **Site: UW (vs UAB)** | **-0.9022** | 0.4293 | ±0.8586 | **-2.101** | **0.0356** | 0.4057 | * |
| Age (years) | -0.0326 | 0.0184 | ±0.0369 | -1.769 | 0.0769 | 0.9679 | . |
| **BMI (kg/m2)** | **+0.0764** | 0.0257 | ±0.0515 | **+2.967** | **0.0030** | 1.0793 | ** |
| Hypertension | +0.2307 | 0.4180 | ±0.8361 | +0.552 | 0.5811 | 1.2594 |  |
| High cholesterol | +0.2784 | 0.3947 | ±0.7894 | +0.705 | 0.4807 | 1.3210 |  |
| Kidney disease | +0.6028 | 0.5903 | ±1.1806 | +1.021 | 0.3072 | 1.8272 |  |
| Circulatory disease | +0.9208 | 0.4887 | ±0.9775 | +1.884 | 0.0596 | 2.5112 | . |
| Time < 70 (%) | -0.2490 | 0.2272 | ±0.4544 | -1.096 | 0.2731 | 0.7796 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1555**, LLR χ² = **37.12** (p = **1.10e-04**), AUC = **0.7463**, AIC = **225.6**, BIC = **267.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5495 | 1.4859 | ±2.9718 | -1.043 | 0.2971 | 0.2124 |  |
| Education: graduate level (vs college) | -0.0957 | 0.3934 | ±0.7868 | -0.243 | 0.8079 | 0.9088 |  |
| Education: high school or below (vs college) | +0.2714 | 0.6046 | ±1.2092 | +0.449 | 0.6535 | 1.3118 |  |
| Site: UCSD (vs UAB) | -0.5675 | 0.4634 | ±0.9269 | -1.225 | 0.2207 | 0.5669 |  |
| **Site: UW (vs UAB)** | **-0.9196** | 0.4298 | ±0.8597 | **-2.139** | **0.0324** | 0.3987 | * |
| Age (years) | -0.0323 | 0.0184 | ±0.0368 | -1.754 | 0.0795 | 0.9682 | . |
| **BMI (kg/m2)** | **+0.0768** | 0.0258 | ±0.0517 | **+2.973** | **0.0030** | 1.0798 | ** |
| Hypertension | +0.2387 | 0.4188 | ±0.8376 | +0.570 | 0.5687 | 1.2696 |  |
| High cholesterol | +0.2432 | 0.3963 | ±0.7925 | +0.614 | 0.5394 | 1.2753 |  |
| Kidney disease | +0.6216 | 0.5918 | ±1.1837 | +1.050 | 0.2936 | 1.8618 |  |
| Circulatory disease | +0.9111 | 0.4900 | ±0.9801 | +1.859 | 0.0630 | 2.4871 | . |
| Avg. daily time < 70 (%) | -0.3601 | 0.2978 | ±0.5956 | -1.209 | 0.2266 | 0.6976 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1436**, LLR χ² = **34.28** (p = **3.25e-04**), AUC = **0.7399**, AIC = **228.4**, BIC = **270.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.1219 | 2.0849 | ±4.1699 | -1.018 | 0.3088 | 0.1198 |  |
| Education: graduate level (vs college) | +0.0262 | 0.3882 | ±0.7765 | +0.067 | 0.9462 | 1.0265 |  |
| Education: high school or below (vs college) | +0.4426 | 0.6058 | ±1.2116 | +0.731 | 0.4651 | 1.5567 |  |
| Site: UCSD (vs UAB) | -0.5613 | 0.4611 | ±0.9222 | -1.217 | 0.2235 | 0.5705 |  |
| **Site: UW (vs UAB)** | **-0.8624** | 0.4290 | ±0.8580 | **-2.010** | **0.0444** | 0.4222 | * |
| Age (years) | -0.0345 | 0.0184 | ±0.0368 | -1.871 | 0.0614 | 0.9661 | . |
| **BMI (kg/m2)** | **+0.0742** | 0.0255 | ±0.0510 | **+2.908** | **0.0036** | 1.0770 | ** |
| Hypertension | +0.2125 | 0.4183 | ±0.8367 | +0.508 | 0.6116 | 1.2367 |  |
| High cholesterol | +0.3822 | 0.3894 | ±0.7789 | +0.981 | 0.3264 | 1.4655 |  |
| Kidney disease | +0.5708 | 0.5879 | ±1.1758 | +0.971 | 0.3316 | 1.7697 |  |
| **Circulatory disease** | **+0.9777** | 0.4964 | ±0.9928 | **+1.969** | **0.0489** | 2.6582 | * |
| Time 54-250, pooled (%) | +0.0052 | 0.0151 | ±0.0301 | +0.348 | 0.7278 | 1.0053 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1436**, LLR χ² = **34.27** (p = **3.26e-04**), AUC = **0.7397**, AIC = **228.4**, BIC = **270.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.1103 | 2.0990 | ±4.1980 | -1.005 | 0.3147 | 0.1212 |  |
| Education: graduate level (vs college) | +0.0268 | 0.3882 | ±0.7764 | +0.069 | 0.9450 | 1.0271 |  |
| Education: high school or below (vs college) | +0.4424 | 0.6062 | ±1.2123 | +0.730 | 0.4655 | 1.5565 |  |
| Site: UCSD (vs UAB) | -0.5619 | 0.4611 | ±0.9223 | -1.218 | 0.2231 | 0.5701 |  |
| **Site: UW (vs UAB)** | **-0.8622** | 0.4289 | ±0.8579 | **-2.010** | **0.0444** | 0.4222 | * |
| Age (years) | -0.0344 | 0.0184 | ±0.0368 | -1.870 | 0.0615 | 0.9662 | . |
| **BMI (kg/m2)** | **+0.0742** | 0.0255 | ±0.0510 | **+2.909** | **0.0036** | 1.0771 | ** |
| Hypertension | +0.2127 | 0.4183 | ±0.8366 | +0.509 | 0.6111 | 1.2370 |  |
| High cholesterol | +0.3822 | 0.3895 | ±0.7790 | +0.981 | 0.3265 | 1.4655 |  |
| Kidney disease | +0.5707 | 0.5879 | ±1.1758 | +0.971 | 0.3317 | 1.7695 |  |
| **Circulatory disease** | **+0.9767** | 0.4965 | ±0.9929 | **+1.967** | **0.0491** | 2.6557 | * |
| Avg. daily time 54-250 (%) | +0.0051 | 0.0152 | ±0.0303 | +0.336 | 0.7372 | 1.0051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1459**, LLR χ² = **34.83** (p = **2.64e-04**), AUC = **0.7429**, AIC = **227.9**, BIC = **269.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5329 | 1.4795 | ±2.9589 | -1.036 | 0.3001 | 0.2159 |  |
| Education: graduate level (vs college) | -0.0175 | 0.3926 | ±0.7853 | -0.045 | 0.9645 | 0.9827 |  |
| Education: high school or below (vs college) | +0.4185 | 0.5966 | ±1.1932 | +0.701 | 0.4830 | 1.5196 |  |
| Site: UCSD (vs UAB) | -0.5572 | 0.4617 | ±0.9235 | -1.207 | 0.2275 | 0.5728 |  |
| **Site: UW (vs UAB)** | **-0.8641** | 0.4300 | ±0.8600 | **-2.010** | **0.0445** | 0.4214 | * |
| Age (years) | -0.0344 | 0.0184 | ±0.0368 | -1.869 | 0.0616 | 0.9662 | . |
| **BMI (kg/m2)** | **+0.0679** | 0.0265 | ±0.0530 | **+2.564** | **0.0103** | 1.0703 | * |
| Hypertension | +0.2043 | 0.4193 | ±0.8385 | +0.487 | 0.6261 | 1.2267 |  |
| High cholesterol | +0.3285 | 0.3956 | ±0.7912 | +0.830 | 0.4063 | 1.3889 |  |
| Kidney disease | +0.4846 | 0.6037 | ±1.2075 | +0.803 | 0.4222 | 1.6235 |  |
| Circulatory disease | +0.9495 | 0.4893 | ±0.9786 | +1.941 | 0.0523 | 2.5845 | . |
| Time 181-250, pooled (%) | +0.0148 | 0.0179 | ±0.0358 | +0.829 | 0.4069 | 1.0149 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1460**, LLR χ² = **34.84** (p = **2.63e-04**), AUC = **0.7429**, AIC = **227.8**, BIC = **269.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5357 | 1.4790 | ±2.9580 | -1.038 | 0.2991 | 0.2153 |  |
| Education: graduate level (vs college) | -0.0196 | 0.3929 | ±0.7858 | -0.050 | 0.9602 | 0.9806 |  |
| Education: high school or below (vs college) | +0.4224 | 0.5964 | ±1.1928 | +0.708 | 0.4787 | 1.5257 |  |
| Site: UCSD (vs UAB) | -0.5519 | 0.4619 | ±0.9237 | -1.195 | 0.2321 | 0.5758 |  |
| **Site: UW (vs UAB)** | **-0.8585** | 0.4298 | ±0.8596 | **-1.998** | **0.0458** | 0.4238 | * |
| Age (years) | -0.0345 | 0.0184 | ±0.0368 | -1.872 | 0.0612 | 0.9661 | . |
| **BMI (kg/m2)** | **+0.0681** | 0.0264 | ±0.0528 | **+2.583** | **0.0098** | 1.0705 | ** |
| Hypertension | +0.2045 | 0.4191 | ±0.8382 | +0.488 | 0.6256 | 1.2269 |  |
| High cholesterol | +0.3279 | 0.3956 | ±0.7911 | +0.829 | 0.4071 | 1.3881 |  |
| Kidney disease | +0.4812 | 0.6042 | ±1.2084 | +0.796 | 0.4258 | 1.6179 |  |
| Circulatory disease | +0.9520 | 0.4891 | ±0.9783 | +1.946 | 0.0516 | 2.5908 | . |
| Avg. daily time 181-250 (%) | +0.0146 | 0.0174 | ±0.0348 | +0.839 | 0.4016 | 1.0147 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1433**, LLR χ² = **34.20** (p = **3.35e-04**), AUC = **0.7387**, AIC = **228.5**, BIC = **270.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6074 | 1.4816 | ±2.9632 | -1.085 | 0.2780 | 0.2004 |  |
| Education: graduate level (vs college) | +0.0214 | 0.3890 | ±0.7779 | +0.055 | 0.9561 | 1.0216 |  |
| Education: high school or below (vs college) | +0.3978 | 0.6004 | ±1.2008 | +0.663 | 0.5076 | 1.4886 |  |
| Site: UCSD (vs UAB) | -0.5564 | 0.4606 | ±0.9212 | -1.208 | 0.2271 | 0.5733 |  |
| **Site: UW (vs UAB)** | **-0.8605** | 0.4290 | ±0.8581 | **-2.006** | **0.0449** | 0.4230 | * |
| Age (years) | -0.0343 | 0.0184 | ±0.0369 | -1.859 | 0.0630 | 0.9663 | . |
| **BMI (kg/m2)** | **+0.0729** | 0.0259 | ±0.0519 | **+2.810** | **0.0050** | 1.0756 | ** |
| Hypertension | +0.2114 | 0.4176 | ±0.8352 | +0.506 | 0.6128 | 1.2354 |  |
| High cholesterol | +0.3877 | 0.3886 | ±0.7772 | +0.998 | 0.3184 | 1.4736 |  |
| Kidney disease | +0.5674 | 0.5894 | ±1.1788 | +0.963 | 0.3357 | 1.7637 |  |
| Circulatory disease | +0.9341 | 0.4918 | ±0.9835 | +1.900 | 0.0575 | 2.5450 | . |
| Time > 180 (%) | +0.0021 | 0.0097 | ±0.0195 | +0.216 | 0.8291 | 1.0021 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1434**, LLR χ² = **34.22** (p = **3.33e-04**), AUC = **0.7388**, AIC = **228.5**, BIC = **270.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6055 | 1.4817 | ±2.9633 | -1.084 | 0.2786 | 0.2008 |  |
| Education: graduate level (vs college) | +0.0198 | 0.3891 | ±0.7782 | +0.051 | 0.9594 | 1.0200 |  |
| Education: high school or below (vs college) | +0.3962 | 0.6001 | ±1.2002 | +0.660 | 0.5091 | 1.4862 |  |
| Site: UCSD (vs UAB) | -0.5550 | 0.4607 | ±0.9215 | -1.205 | 0.2284 | 0.5741 |  |
| **Site: UW (vs UAB)** | **-0.8596** | 0.4291 | ±0.8582 | **-2.003** | **0.0451** | 0.4234 | * |
| Age (years) | -0.0343 | 0.0184 | ±0.0369 | -1.860 | 0.0629 | 0.9663 | . |
| **BMI (kg/m2)** | **+0.0727** | 0.0259 | ±0.0519 | **+2.805** | **0.0050** | 1.0755 | ** |
| Hypertension | +0.2110 | 0.4176 | ±0.8352 | +0.505 | 0.6133 | 1.2350 |  |
| High cholesterol | +0.3869 | 0.3886 | ±0.7771 | +0.996 | 0.3195 | 1.4723 |  |
| Kidney disease | +0.5652 | 0.5896 | ±1.1793 | +0.959 | 0.3378 | 1.7598 |  |
| Circulatory disease | +0.9326 | 0.4914 | ±0.9828 | +1.898 | 0.0577 | 2.5410 | . |
| Avg. daily time > 180 (%) | +0.0024 | 0.0096 | ±0.0192 | +0.253 | 0.8006 | 1.0024 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1467**, LLR χ² = **35.02** (p = **2.46e-04**), AUC = **0.7454**, AIC = **227.7**, BIC = **269.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5686 | 1.4866 | ±2.9731 | -1.055 | 0.2913 | 0.2083 |  |
| Education: graduate level (vs college) | +0.0274 | 0.3888 | ±0.7776 | +0.071 | 0.9438 | 1.0278 |  |
| Education: high school or below (vs college) | +0.3694 | 0.6000 | ±1.2000 | +0.616 | 0.5381 | 1.4469 |  |
| Site: UCSD (vs UAB) | -0.5607 | 0.4619 | ±0.9238 | -1.214 | 0.2248 | 0.5708 |  |
| **Site: UW (vs UAB)** | **-0.8628** | 0.4304 | ±0.8609 | **-2.004** | **0.0450** | 0.4220 | * |
| Age (years) | -0.0338 | 0.0185 | ±0.0369 | -1.830 | 0.0673 | 0.9668 | . |
| **BMI (kg/m2)** | **+0.0694** | 0.0261 | ±0.0523 | **+2.656** | **0.0079** | 1.0719 | ** |
| Hypertension | +0.2110 | 0.4190 | ±0.8381 | +0.503 | 0.6146 | 1.2349 |  |
| High cholesterol | +0.3681 | 0.3900 | ±0.7800 | +0.944 | 0.3453 | 1.4450 |  |
| Kidney disease | +0.6002 | 0.5877 | ±1.1753 | +1.021 | 0.3071 | 1.8226 |  |
| Circulatory disease | +0.9042 | 0.4906 | ±0.9813 | +1.843 | 0.0653 | 2.4699 | . |
| Nocturnal time > 180 (%) | +0.0083 | 0.0088 | ±0.0176 | +0.939 | 0.3475 | 1.0083 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1436**, LLR χ² = **34.26** (p = **3.27e-04**), AUC = **0.7397**, AIC = **228.4**, BIC = **270.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5998 | 1.4799 | ±2.9599 | -1.081 | 0.2797 | 0.2019 |  |
| Education: graduate level (vs college) | +0.0270 | 0.3882 | ±0.7764 | +0.070 | 0.9445 | 1.0274 |  |
| Education: high school or below (vs college) | +0.4409 | 0.6061 | ±1.2122 | +0.727 | 0.4669 | 1.5542 |  |
| Site: UCSD (vs UAB) | -0.5606 | 0.4610 | ±0.9221 | -1.216 | 0.2240 | 0.5709 |  |
| **Site: UW (vs UAB)** | **-0.8617** | 0.4290 | ±0.8579 | **-2.009** | **0.0446** | 0.4225 | * |
| Age (years) | -0.0345 | 0.0184 | ±0.0368 | -1.871 | 0.0613 | 0.9661 | . |
| **BMI (kg/m2)** | **+0.0742** | 0.0255 | ±0.0510 | **+2.908** | **0.0036** | 1.0770 | ** |
| Hypertension | +0.2126 | 0.4183 | ±0.8366 | +0.508 | 0.6113 | 1.2368 |  |
| High cholesterol | +0.3838 | 0.3892 | ±0.7785 | +0.986 | 0.3241 | 1.4679 |  |
| Kidney disease | +0.5714 | 0.5879 | ±1.1757 | +0.972 | 0.3311 | 1.7707 |  |
| **Circulatory disease** | **+0.9754** | 0.4965 | ±0.9929 | **+1.965** | **0.0494** | 2.6523 | * |
| Time > 250 (%) | -0.0048 | 0.0150 | ±0.0299 | -0.321 | 0.7484 | 0.9952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 243)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **243**, events = **47**, McFadden pseudo-R² = **0.1435**, LLR χ² = **34.25** (p = **3.30e-04**), AUC = **0.7397**, AIC = **228.4**, BIC = **270.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6033 | 1.4799 | ±2.9599 | -1.083 | 0.2786 | 0.2012 |  |
| Education: graduate level (vs college) | +0.0274 | 0.3882 | ±0.7764 | +0.071 | 0.9438 | 1.0278 |  |
| Education: high school or below (vs college) | +0.4392 | 0.6064 | ±1.2128 | +0.724 | 0.4689 | 1.5515 |  |
| Site: UCSD (vs UAB) | -0.5610 | 0.4610 | ±0.9221 | -1.217 | 0.2237 | 0.5706 |  |
| **Site: UW (vs UAB)** | **-0.8615** | 0.4289 | ±0.8579 | **-2.008** | **0.0446** | 0.4225 | * |
| Age (years) | -0.0344 | 0.0184 | ±0.0368 | -1.870 | 0.0615 | 0.9661 | . |
| **BMI (kg/m2)** | **+0.0742** | 0.0255 | ±0.0510 | **+2.907** | **0.0036** | 1.0770 | ** |
| Hypertension | +0.2127 | 0.4182 | ±0.8364 | +0.509 | 0.6110 | 1.2371 |  |
| High cholesterol | +0.3842 | 0.3893 | ±0.7786 | +0.987 | 0.3236 | 1.4685 |  |
| Kidney disease | +0.5715 | 0.5879 | ±1.1757 | +0.972 | 0.3310 | 1.7709 |  |
| **Circulatory disease** | **+0.9731** | 0.4964 | ±0.9928 | **+1.960** | **0.0500** | 2.6462 | * |
| Avg. daily time > 250 (%) | -0.0044 | 0.0150 | ±0.0300 | -0.294 | 0.7685 | 0.9956 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Healthy group (no diabetes + pre-diabetes / lifestyle) - Depression

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 60 single-predictor tests; 3 with raw p < 0.05 (about 3 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **CES-D-10 depressive symptoms (0-30)** (n = 243): best single predictor out of sample is **Mean/SD (daily avg)** (CV R² 0.068 vs 0.063 for covariates alone, gain +0.005; +0.498 per SD, p = 0.109). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Clinically relevant depressive symptoms (CES-D-10 >= 10)** (n = 243): best single predictor out of sample is **Mean/SD (daily avg)** (CV AUC 0.692 vs 0.666 for covariates alone, gain +0.026; OR 1.61 per SD, p = 0.011). Raw p < 0.05 (FDR not applicable here): Mean/SD (daily avg) (p = 0.011), Mean/SD (p = 0.032), CV (p = 0.035).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Clinically relevant depressive symptoms (CES-D-10 >= 10) (+0.026, via Mean/SD (daily avg)); CES-D-10 depressive symptoms (0-30) (+0.005, via Mean/SD (daily avg)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (0 FDR-significant / 3 raw-significant of 16); HbA1c (0 FDR-significant / 0 raw-significant of 2); CGM level (0 FDR-significant / 0 raw-significant of 6).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (3 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** CES-D-10 depressive symptoms (%54-250 (daily avg), ΔAIC -2.5); Clinically relevant depressive symptoms (Mean/SD (daily avg), ΔAIC -6.5).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
