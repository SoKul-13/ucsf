# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Non-healthy group (T2D non-insulin + T2D insulin) - Cognition

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 205; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **205**, R² = **0.1486**, Adj R² = **0.1047**, F-statistic = **3.39** (p = **4.24e-04**), Residual SE = **2.894** on **194** df, AIC = **1028.2**, BIC = **1064.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5027** | 1.9923 | ±3.9846 | **+14.307** | **1.99e-46** | *** |
| **Education: graduate level (vs college)** | **+1.4177** | 0.4401 | ±0.8803 | **+3.221** | **0.0013** | ** |
| Education: high school or below (vs college) | -1.4240 | 0.8010 | ±1.6020 | -1.778 | 0.0754 | . |
| Site: UCSD (vs UAB) | -0.1475 | 0.5212 | ±1.0424 | -0.283 | 0.7771 |  |
| Site: UW (vs UAB) | +0.4590 | 0.5500 | ±1.1000 | +0.835 | 0.4039 |  |
| Age (years) | -0.0292 | 0.0245 | ±0.0490 | -1.193 | 0.2329 |  |
| BMI (kg/m2) | -0.0588 | 0.0365 | ±0.0730 | -1.611 | 0.1072 |  |
| Hypertension | -0.1629 | 0.4960 | ±0.9920 | -0.328 | 0.7425 |  |
| High cholesterol | +0.3107 | 0.4610 | ±0.9219 | +0.674 | 0.5003 |  |
| Kidney disease | -0.4185 | 0.6741 | ±1.3483 | -0.621 | 0.5348 |  |
| Circulatory disease | +0.4681 | 0.6292 | ±1.2584 | +0.744 | 0.4570 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **205**, R² = **0.1556**, Adj R² = **0.1074**, F-statistic = **3.23** (p = **4.57e-04**), Residual SE = **2.890** on **193** df, AIC = **1028.5**, BIC = **1068.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.1990** | 3.1074 | ±6.2148 | **+10.040** | **1.01e-23** | *** |
| **Education: graduate level (vs college)** | **+1.3922** | 0.4415 | ±0.8830 | **+3.153** | **0.0016** | ** |
| Education: high school or below (vs college) | -1.3958 | 0.7955 | ±1.5910 | -1.755 | 0.0793 | . |
| Site: UCSD (vs UAB) | -0.1615 | 0.5197 | ±1.0393 | -0.311 | 0.7560 |  |
| Site: UW (vs UAB) | +0.4493 | 0.5495 | ±1.0989 | +0.818 | 0.4136 |  |
| Age (years) | -0.0283 | 0.0247 | ±0.0495 | -1.143 | 0.2531 |  |
| BMI (kg/m2) | -0.0506 | 0.0366 | ±0.0732 | -1.382 | 0.1668 |  |
| Hypertension | -0.1275 | 0.4923 | ±0.9845 | -0.259 | 0.7956 |  |
| High cholesterol | +0.3672 | 0.4630 | ±0.9259 | +0.793 | 0.4277 |  |
| Kidney disease | -0.4931 | 0.6638 | ±1.3275 | -0.743 | 0.4575 |  |
| Circulatory disease | +0.5543 | 0.6298 | ±1.2596 | +0.880 | 0.3788 |  |
| HbA1c (%) | -0.5110 | 0.4545 | ±0.9090 | -1.124 | 0.2608 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **205**, R² = **0.1736**, Adj R² = **0.1265**, F-statistic = **3.69** (p = **8.98e-05**), Residual SE = **2.859** on **193** df, AIC = **1024.1**, BIC = **1063.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.1445** | 2.6693 | ±5.3386 | **+12.417** | **2.12e-35** | *** |
| **Education: graduate level (vs college)** | **+1.3943** | 0.4330 | ±0.8659 | **+3.220** | **0.0013** | ** |
| Education: high school or below (vs college) | -1.5061 | 0.8090 | ±1.6179 | -1.862 | 0.0626 | . |
| Site: UCSD (vs UAB) | -0.1630 | 0.5178 | ±1.0356 | -0.315 | 0.7529 |  |
| Site: UW (vs UAB) | +0.4115 | 0.5454 | ±1.0908 | +0.754 | 0.4506 |  |
| Age (years) | -0.0294 | 0.0238 | ±0.0476 | -1.235 | 0.2168 |  |
| BMI (kg/m2) | -0.0518 | 0.0363 | ±0.0725 | -1.429 | 0.1531 |  |
| Hypertension | -0.1154 | 0.4889 | ±0.9779 | -0.236 | 0.8134 |  |
| High cholesterol | +0.2799 | 0.4616 | ±0.9231 | +0.606 | 0.5443 |  |
| Kidney disease | -0.2820 | 0.6947 | ±1.3894 | -0.406 | 0.6847 |  |
| Circulatory disease | +0.5102 | 0.6269 | ±1.2538 | +0.814 | 0.4158 |  |
| **Mean glucose (mg/dL)** | **-0.0381** | 0.0149 | ±0.0299 | **-2.553** | **0.0107** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **205**, R² = **0.1736**, Adj R² = **0.1265**, F-statistic = **3.69** (p = **8.98e-05**), Residual SE = **2.859** on **193** df, AIC = **1024.1**, BIC = **1063.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+38.4208** | 4.3564 | ±8.7127 | **+8.819** | **1.15e-18** | *** |
| **Education: graduate level (vs college)** | **+1.3943** | 0.4330 | ±0.8659 | **+3.220** | **0.0013** | ** |
| Education: high school or below (vs college) | -1.5061 | 0.8090 | ±1.6179 | -1.862 | 0.0626 | . |
| Site: UCSD (vs UAB) | -0.1630 | 0.5178 | ±1.0356 | -0.315 | 0.7529 |  |
| Site: UW (vs UAB) | +0.4115 | 0.5454 | ±1.0908 | +0.754 | 0.4506 |  |
| Age (years) | -0.0294 | 0.0238 | ±0.0476 | -1.235 | 0.2168 |  |
| BMI (kg/m2) | -0.0518 | 0.0363 | ±0.0725 | -1.429 | 0.1531 |  |
| Hypertension | -0.1154 | 0.4889 | ±0.9779 | -0.236 | 0.8134 |  |
| High cholesterol | +0.2799 | 0.4616 | ±0.9231 | +0.606 | 0.5443 |  |
| Kidney disease | -0.2820 | 0.6947 | ±1.3894 | -0.406 | 0.6847 |  |
| Circulatory disease | +0.5102 | 0.6269 | ±1.2538 | +0.814 | 0.4158 |  |
| **GMI (%)** | **-1.5940** | 0.6245 | ±1.2490 | **-2.553** | **0.0107** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **205**, R² = **0.2046**, Adj R² = **0.1592**, F-statistic = **4.51** (p = **4.51e-06**), Residual SE = **2.805** on **193** df, AIC = **1016.2**, BIC = **1056.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+34.8940** | 2.5948 | ±5.1896 | **+13.448** | **3.18e-41** | *** |
| **Education: graduate level (vs college)** | **+1.4423** | 0.4279 | ±0.8558 | **+3.371** | **7.50e-04** | *** |
| Education: high school or below (vs college) | -1.5027 | 0.7876 | ±1.5753 | -1.908 | 0.0564 | . |
| Site: UCSD (vs UAB) | -0.1241 | 0.5129 | ±1.0259 | -0.242 | 0.8088 |  |
| Site: UW (vs UAB) | +0.4389 | 0.5324 | ±1.0647 | +0.824 | 0.4097 |  |
| Age (years) | -0.0355 | 0.0232 | ±0.0463 | -1.533 | 0.1254 |  |
| BMI (kg/m2) | -0.0453 | 0.0364 | ±0.0728 | -1.246 | 0.2128 |  |
| Hypertension | -0.1575 | 0.4722 | ±0.9444 | -0.334 | 0.7387 |  |
| High cholesterol | +0.3360 | 0.4531 | ±0.9062 | +0.741 | 0.4584 |  |
| Kidney disease | -0.3717 | 0.6944 | ±1.3887 | -0.535 | 0.5925 |  |
| Circulatory disease | +0.6036 | 0.6092 | ±1.2184 | +0.991 | 0.3217 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0511** | 0.0144 | ±0.0288 | **-3.544** | **3.94e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **205**, R² = **0.1769**, Adj R² = **0.1300**, F-statistic = **3.77** (p = **6.59e-05**), Residual SE = **2.853** on **193** df, AIC = **1023.2**, BIC = **1063.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.8090** | 2.2467 | ±4.4935 | **+13.713** | **8.51e-43** | *** |
| **Education: graduate level (vs college)** | **+1.4896** | 0.4398 | ±0.8796 | **+3.387** | **7.07e-04** | *** |
| Education: high school or below (vs college) | -1.1319 | 0.7820 | ±1.5640 | -1.447 | 0.1478 |  |
| Site: UCSD (vs UAB) | -0.2362 | 0.5145 | ±1.0291 | -0.459 | 0.6462 |  |
| Site: UW (vs UAB) | +0.2552 | 0.5510 | ±1.1021 | +0.463 | 0.6433 |  |
| Age (years) | -0.0252 | 0.0242 | ±0.0483 | -1.044 | 0.2967 |  |
| BMI (kg/m2) | -0.0596 | 0.0371 | ±0.0742 | -1.607 | 0.1081 |  |
| Hypertension | +0.0030 | 0.4909 | ±0.9819 | +0.006 | 0.9952 |  |
| High cholesterol | +0.2334 | 0.4607 | ±0.9215 | +0.507 | 0.6125 |  |
| Kidney disease | -0.1720 | 0.7008 | ±1.4016 | -0.245 | 0.8061 |  |
| Circulatory disease | +0.5757 | 0.6130 | ±1.2260 | +0.939 | 0.3476 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.1193** | 0.0472 | ±0.0943 | **-2.529** | **0.0114** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **205**, R² = **0.1734**, Adj R² = **0.1262**, F-statistic = **3.68** (p = **9.21e-05**), Residual SE = **2.859** on **193** df, AIC = **1024.1**, BIC = **1064.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.4564** | 2.2111 | ±4.4222 | **+13.774** | **3.64e-43** | *** |
| **Education: graduate level (vs college)** | **+1.4756** | 0.4365 | ±0.8731 | **+3.380** | **7.25e-04** | *** |
| Education: high school or below (vs college) | -1.2087 | 0.7961 | ±1.5922 | -1.518 | 0.1289 |  |
| Site: UCSD (vs UAB) | -0.1680 | 0.5131 | ±1.0263 | -0.327 | 0.7433 |  |
| Site: UW (vs UAB) | +0.3243 | 0.5536 | ±1.1071 | +0.586 | 0.5579 |  |
| Age (years) | -0.0251 | 0.0241 | ±0.0482 | -1.044 | 0.2967 |  |
| BMI (kg/m2) | -0.0596 | 0.0370 | ±0.0739 | -1.612 | 0.1069 |  |
| Hypertension | +0.0361 | 0.4966 | ±0.9932 | +0.073 | 0.9420 |  |
| High cholesterol | +0.2313 | 0.4581 | ±0.9162 | +0.505 | 0.6137 |  |
| Kidney disease | -0.2606 | 0.6908 | ±1.3817 | -0.377 | 0.7060 |  |
| Circulatory disease | +0.5194 | 0.6150 | ±1.2300 | +0.845 | 0.3983 |  |
| **Avg. daily SD (mg/dL)** | **-0.1131** | 0.0488 | ±0.0975 | **-2.320** | **0.0203** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **205**, R² = **0.1608**, Adj R² = **0.1130**, F-statistic = **3.36** (p = **2.87e-04**), Residual SE = **2.881** on **193** df, AIC = **1027.2**, BIC = **1067.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.3609** | 2.4309 | ±4.8617 | **+12.490** | **8.49e-36** | *** |
| **Education: graduate level (vs college)** | **+1.4806** | 0.4465 | ±0.8931 | **+3.316** | **9.14e-04** | *** |
| Education: high school or below (vs college) | -1.1563 | 0.7883 | ±1.5765 | -1.467 | 0.1424 |  |
| Site: UCSD (vs UAB) | -0.2119 | 0.5209 | ±1.0418 | -0.407 | 0.6842 |  |
| Site: UW (vs UAB) | +0.3187 | 0.5618 | ±1.1236 | +0.567 | 0.5705 |  |
| Age (years) | -0.0260 | 0.0246 | ±0.0492 | -1.055 | 0.2914 |  |
| BMI (kg/m2) | -0.0623 | 0.0375 | ±0.0749 | -1.662 | 0.0965 | . |
| Hypertension | -0.0520 | 0.5006 | ±1.0011 | -0.104 | 0.9173 |  |
| High cholesterol | +0.2644 | 0.4615 | ±0.9231 | +0.573 | 0.5667 |  |
| Kidney disease | -0.2801 | 0.6932 | ±1.3864 | -0.404 | 0.6862 |  |
| Circulatory disease | +0.5272 | 0.6216 | ±1.2433 | +0.848 | 0.3963 |  |
| CV (%) | -0.1172 | 0.0744 | ±0.1488 | -1.575 | 0.1153 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **205**, R² = **0.1624**, Adj R² = **0.1147**, F-statistic = **3.40** (p = **2.48e-04**), Residual SE = **2.878** on **193** df, AIC = **1026.8**, BIC = **1066.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.2906** | 2.3507 | ±4.7015 | **+11.184** | **4.89e-29** | *** |
| **Education: graduate level (vs college)** | **+1.4735** | 0.4474 | ±0.8949 | **+3.293** | **9.90e-04** | *** |
| Education: high school or below (vs college) | -1.1754 | 0.7887 | ±1.5774 | -1.490 | 0.1361 |  |
| Site: UCSD (vs UAB) | -0.1958 | 0.5184 | ±1.0369 | -0.378 | 0.7056 |  |
| Site: UW (vs UAB) | +0.3273 | 0.5567 | ±1.1133 | +0.588 | 0.5565 |  |
| Age (years) | -0.0256 | 0.0248 | ±0.0496 | -1.035 | 0.3008 |  |
| BMI (kg/m2) | -0.0601 | 0.0370 | ±0.0740 | -1.626 | 0.1041 |  |
| Hypertension | -0.0393 | 0.5005 | ±1.0009 | -0.079 | 0.9374 |  |
| High cholesterol | +0.2790 | 0.4581 | ±0.9163 | +0.609 | 0.5426 |  |
| Kidney disease | -0.2775 | 0.6882 | ±1.3765 | -0.403 | 0.6868 |  |
| Circulatory disease | +0.5101 | 0.6135 | ±1.2271 | +0.831 | 0.4057 |  |
| Mean / SD ratio | +0.3238 | 0.1945 | ±0.3891 | +1.665 | 0.0960 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **205**, R² = **0.1625**, Adj R² = **0.1148**, F-statistic = **3.41** (p = **2.46e-04**), Residual SE = **2.878** on **193** df, AIC = **1026.8**, BIC = **1066.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.4520** | 2.2609 | ±4.5217 | **+11.700** | **1.27e-31** | *** |
| **Education: graduate level (vs college)** | **+1.4518** | 0.4411 | ±0.8822 | **+3.291** | **9.97e-04** | *** |
| Education: high school or below (vs college) | -1.2378 | 0.7946 | ±1.5893 | -1.558 | 0.1193 |  |
| Site: UCSD (vs UAB) | -0.1296 | 0.5142 | ±1.0283 | -0.252 | 0.8009 |  |
| Site: UW (vs UAB) | +0.3616 | 0.5553 | ±1.1106 | +0.651 | 0.5149 |  |
| Age (years) | -0.0252 | 0.0246 | ±0.0491 | -1.026 | 0.3049 |  |
| BMI (kg/m2) | -0.0593 | 0.0368 | ±0.0735 | -1.612 | 0.1069 |  |
| Hypertension | +0.0016 | 0.5038 | ±1.0075 | +0.003 | 0.9975 |  |
| High cholesterol | +0.2942 | 0.4568 | ±0.9136 | +0.644 | 0.5195 |  |
| Kidney disease | -0.3252 | 0.6790 | ±1.3581 | -0.479 | 0.6320 |  |
| Circulatory disease | +0.4472 | 0.6144 | ±1.2288 | +0.728 | 0.4667 |  |
| Avg. daily mean/SD | +0.2497 | 0.1447 | ±0.2895 | +1.725 | 0.0845 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **205**, R² = **0.1527**, Adj R² = **0.1044**, F-statistic = **3.16** (p = **5.85e-04**), Residual SE = **2.895** on **193** df, AIC = **1029.2**, BIC = **1069.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5791** | 2.4190 | ±4.8381 | **+12.228** | **2.21e-34** | *** |
| **Education: graduate level (vs college)** | **+1.4282** | 0.4397 | ±0.8794 | **+3.248** | **0.0012** | ** |
| Education: high school or below (vs college) | -1.3779 | 0.8013 | ±1.6026 | -1.720 | 0.0855 | . |
| Site: UCSD (vs UAB) | -0.1439 | 0.5213 | ±1.0426 | -0.276 | 0.7826 |  |
| Site: UW (vs UAB) | +0.4289 | 0.5622 | ±1.1244 | +0.763 | 0.4456 |  |
| Age (years) | -0.0298 | 0.0245 | ±0.0490 | -1.217 | 0.2238 |  |
| BMI (kg/m2) | -0.0572 | 0.0366 | ±0.0732 | -1.563 | 0.1180 |  |
| Hypertension | -0.1470 | 0.4953 | ±0.9907 | -0.297 | 0.7666 |  |
| High cholesterol | +0.3369 | 0.4721 | ±0.9442 | +0.714 | 0.4755 |  |
| Kidney disease | -0.4248 | 0.6892 | ±1.3785 | -0.616 | 0.5376 |  |
| Circulatory disease | +0.4473 | 0.6326 | ±1.2652 | +0.707 | 0.4795 |  |
| MAG (mg/dL/h) | -0.0306 | 0.0364 | ±0.0727 | -0.841 | 0.4006 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **205**, R² = **0.1649**, Adj R² = **0.1173**, F-statistic = **3.46** (p = **2.00e-04**), Residual SE = **2.874** on **193** df, AIC = **1026.2**, BIC = **1066.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.5518** | 2.3129 | ±4.6259 | **+13.209** | **7.78e-40** | *** |
| **Education: graduate level (vs college)** | **+1.4418** | 0.4408 | ±0.8816 | **+3.271** | **0.0011** | ** |
| Education: high school or below (vs college) | -1.2854 | 0.7944 | ±1.5887 | -1.618 | 0.1056 |  |
| Site: UCSD (vs UAB) | -0.1883 | 0.5189 | ±1.0378 | -0.363 | 0.7167 |  |
| Site: UW (vs UAB) | +0.3563 | 0.5588 | ±1.1177 | +0.638 | 0.5237 |  |
| Age (years) | -0.0257 | 0.0242 | ±0.0484 | -1.061 | 0.2889 |  |
| BMI (kg/m2) | -0.0624 | 0.0373 | ±0.0745 | -1.675 | 0.0938 | . |
| Hypertension | -0.0518 | 0.4952 | ±0.9905 | -0.105 | 0.9167 |  |
| High cholesterol | +0.2793 | 0.4594 | ±0.9187 | +0.608 | 0.5431 |  |
| Kidney disease | -0.3402 | 0.6936 | ±1.3873 | -0.490 | 0.6238 |  |
| Circulatory disease | +0.4793 | 0.6184 | ±1.2368 | +0.775 | 0.4383 |  |
| Avg. daily range (mg/dL) | -0.0226 | 0.0124 | ±0.0247 | -1.829 | 0.0675 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **205**, R² = **0.1664**, Adj R² = **0.1189**, F-statistic = **3.50** (p = **1.73e-04**), Residual SE = **2.871** on **193** df, AIC = **1025.8**, BIC = **1065.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5798** | 2.0598 | ±4.1196 | **+14.360** | **9.17e-47** | *** |
| **Education: graduate level (vs college)** | **+1.4491** | 0.4491 | ±0.8982 | **+3.227** | **0.0013** | ** |
| Education: high school or below (vs college) | -1.1573 | 0.7741 | ±1.5482 | -1.495 | 0.1349 |  |
| Site: UCSD (vs UAB) | -0.3177 | 0.5142 | ±1.0285 | -0.618 | 0.5367 |  |
| Site: UW (vs UAB) | +0.2704 | 0.5390 | ±1.0780 | +0.502 | 0.6159 |  |
| Age (years) | -0.0279 | 0.0245 | ±0.0490 | -1.140 | 0.2544 |  |
| BMI (kg/m2) | -0.0583 | 0.0372 | ±0.0743 | -1.568 | 0.1168 |  |
| Hypertension | -0.2491 | 0.4845 | ±0.9690 | -0.514 | 0.6071 |  |
| High cholesterol | +0.3491 | 0.4598 | ±0.9196 | +0.759 | 0.4477 |  |
| Kidney disease | -0.1608 | 0.7047 | ±1.4094 | -0.228 | 0.8195 |  |
| Circulatory disease | +0.6954 | 0.6282 | ±1.2565 | +1.107 | 0.2683 |  |
| **SD of daily means (mg/dL)** | **-0.1736** | 0.0834 | ±0.1668 | **-2.081** | **0.0374** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **205**, R² = **0.1543**, Adj R² = **0.1061**, F-statistic = **3.20** (p = **5.09e-04**), Residual SE = **2.892** on **193** df, AIC = **1028.8**, BIC = **1068.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4569** | 4.7020 | ±9.4041 | **+4.989** | **6.08e-07** | *** |
| **Education: graduate level (vs college)** | **+1.4409** | 0.4417 | ±0.8834 | **+3.262** | **0.0011** | ** |
| Education: high school or below (vs college) | -1.3660 | 0.8043 | ±1.6086 | -1.698 | 0.0894 | . |
| Site: UCSD (vs UAB) | -0.1942 | 0.5231 | ±1.0462 | -0.371 | 0.7105 |  |
| Site: UW (vs UAB) | +0.4069 | 0.5482 | ±1.0964 | +0.742 | 0.4579 |  |
| Age (years) | -0.0265 | 0.0244 | ±0.0488 | -1.088 | 0.2767 |  |
| BMI (kg/m2) | -0.0573 | 0.0369 | ±0.0739 | -1.552 | 0.1206 |  |
| Hypertension | -0.1486 | 0.4960 | ±0.9920 | -0.300 | 0.7645 |  |
| High cholesterol | +0.2859 | 0.4654 | ±0.9308 | +0.614 | 0.5390 |  |
| Kidney disease | -0.3130 | 0.6910 | ±1.3821 | -0.453 | 0.6506 |  |
| Circulatory disease | +0.5052 | 0.6280 | ±1.2560 | +0.805 | 0.4211 |  |
| Time in range 70-180, pooled (%) | +0.0504 | 0.0433 | ±0.0865 | +1.166 | 0.2434 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **205**, R² = **0.1533**, Adj R² = **0.1050**, F-statistic = **3.18** (p = **5.58e-04**), Residual SE = **2.894** on **193** df, AIC = **1029.1**, BIC = **1068.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8487** | 4.8052 | ±9.6103 | **+4.963** | **6.94e-07** | *** |
| **Education: graduate level (vs college)** | **+1.4354** | 0.4418 | ±0.8835 | **+3.249** | **0.0012** | ** |
| Education: high school or below (vs college) | -1.3815 | 0.8057 | ±1.6113 | -1.715 | 0.0864 | . |
| Site: UCSD (vs UAB) | -0.1890 | 0.5224 | ±1.0449 | -0.362 | 0.7176 |  |
| Site: UW (vs UAB) | +0.4202 | 0.5493 | ±1.0986 | +0.765 | 0.4443 |  |
| Age (years) | -0.0267 | 0.0244 | ±0.0489 | -1.093 | 0.2743 |  |
| BMI (kg/m2) | -0.0578 | 0.0370 | ±0.0739 | -1.563 | 0.1181 |  |
| Hypertension | -0.1445 | 0.4977 | ±0.9955 | -0.290 | 0.7716 |  |
| High cholesterol | +0.2898 | 0.4651 | ±0.9301 | +0.623 | 0.5332 |  |
| Kidney disease | -0.3209 | 0.6895 | ±1.3790 | -0.465 | 0.6416 |  |
| Circulatory disease | +0.5023 | 0.6276 | ±1.2552 | +0.800 | 0.4235 |  |
| Avg. daily time in range 70-180 (%) | +0.0465 | 0.0437 | ±0.0874 | +1.064 | 0.2875 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **205**, R² = **0.1545**, Adj R² = **0.1063**, F-statistic = **3.21** (p = **5.01e-04**), Residual SE = **2.892** on **193** df, AIC = **1028.8**, BIC = **1068.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.6209** | 1.9992 | ±3.9983 | **+14.316** | **1.73e-46** | *** |
| **Education: graduate level (vs college)** | **+1.3689** | 0.4406 | ±0.8811 | **+3.107** | **0.0019** | ** |
| Education: high school or below (vs college) | -1.5155 | 0.8160 | ±1.6320 | -1.857 | 0.0633 | . |
| Site: UCSD (vs UAB) | -0.1213 | 0.5207 | ±1.0414 | -0.233 | 0.8159 |  |
| Site: UW (vs UAB) | +0.4701 | 0.5485 | ±1.0970 | +0.857 | 0.3914 |  |
| Age (years) | -0.0328 | 0.0248 | ±0.0496 | -1.322 | 0.1860 |  |
| BMI (kg/m2) | -0.0572 | 0.0363 | ±0.0726 | -1.577 | 0.1149 |  |
| Hypertension | -0.1653 | 0.4958 | ±0.9916 | -0.333 | 0.7389 |  |
| High cholesterol | +0.2674 | 0.4613 | ±0.9226 | +0.580 | 0.5622 |  |
| Kidney disease | -0.3724 | 0.6807 | ±1.3614 | -0.547 | 0.5843 |  |
| Circulatory disease | +0.4216 | 0.6348 | ±1.2696 | +0.664 | 0.5066 |  |
| Time 54-69, pooled (%) | +0.8327 | 0.4488 | ±0.8976 | +1.855 | 0.0635 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **205**, R² = **0.1521**, Adj R² = **0.1038**, F-statistic = **3.15** (p = **6.15e-04**), Residual SE = **2.896** on **193** df, AIC = **1029.3**, BIC = **1069.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.6185** | 2.0011 | ±4.0023 | **+14.301** | **2.15e-46** | *** |
| **Education: graduate level (vs college)** | **+1.3817** | 0.4419 | ±0.8839 | **+3.127** | **0.0018** | ** |
| Education: high school or below (vs college) | -1.4869 | 0.8137 | ±1.6273 | -1.827 | 0.0676 | . |
| Site: UCSD (vs UAB) | -0.1440 | 0.5211 | ±1.0422 | -0.276 | 0.7823 |  |
| Site: UW (vs UAB) | +0.4566 | 0.5484 | ±1.0967 | +0.833 | 0.4050 |  |
| Age (years) | -0.0322 | 0.0249 | ±0.0498 | -1.291 | 0.1966 |  |
| BMI (kg/m2) | -0.0576 | 0.0363 | ±0.0727 | -1.586 | 0.1127 |  |
| Hypertension | -0.1710 | 0.4960 | ±0.9920 | -0.345 | 0.7303 |  |
| High cholesterol | +0.2791 | 0.4615 | ±0.9230 | +0.605 | 0.5453 |  |
| Kidney disease | -0.3712 | 0.6830 | ±1.3660 | -0.543 | 0.5868 |  |
| Circulatory disease | +0.4425 | 0.6317 | ±1.2634 | +0.701 | 0.4836 |  |
| Avg. daily time 54-69 (%) | +0.6190 | 0.4121 | ±0.8242 | +1.502 | 0.1331 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **205**, R² = **0.1545**, Adj R² = **0.1063**, F-statistic = **3.21** (p = **5.01e-04**), Residual SE = **2.892** on **193** df, AIC = **1028.8**, BIC = **1068.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.6209** | 1.9992 | ±3.9983 | **+14.316** | **1.73e-46** | *** |
| **Education: graduate level (vs college)** | **+1.3689** | 0.4406 | ±0.8811 | **+3.107** | **0.0019** | ** |
| Education: high school or below (vs college) | -1.5155 | 0.8160 | ±1.6320 | -1.857 | 0.0633 | . |
| Site: UCSD (vs UAB) | -0.1213 | 0.5207 | ±1.0414 | -0.233 | 0.8159 |  |
| Site: UW (vs UAB) | +0.4701 | 0.5485 | ±1.0970 | +0.857 | 0.3914 |  |
| Age (years) | -0.0328 | 0.0248 | ±0.0496 | -1.322 | 0.1860 |  |
| BMI (kg/m2) | -0.0572 | 0.0363 | ±0.0726 | -1.577 | 0.1149 |  |
| Hypertension | -0.1653 | 0.4958 | ±0.9916 | -0.333 | 0.7389 |  |
| High cholesterol | +0.2674 | 0.4613 | ±0.9226 | +0.580 | 0.5622 |  |
| Kidney disease | -0.3724 | 0.6807 | ±1.3614 | -0.547 | 0.5843 |  |
| Circulatory disease | +0.4216 | 0.6348 | ±1.2696 | +0.664 | 0.5066 |  |
| Time < 70 (%) | +0.8327 | 0.4488 | ±0.8976 | +1.855 | 0.0635 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **205**, R² = **0.1521**, Adj R² = **0.1038**, F-statistic = **3.15** (p = **6.15e-04**), Residual SE = **2.896** on **193** df, AIC = **1029.3**, BIC = **1069.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.6185** | 2.0011 | ±4.0023 | **+14.301** | **2.15e-46** | *** |
| **Education: graduate level (vs college)** | **+1.3817** | 0.4419 | ±0.8839 | **+3.127** | **0.0018** | ** |
| Education: high school or below (vs college) | -1.4869 | 0.8137 | ±1.6273 | -1.827 | 0.0676 | . |
| Site: UCSD (vs UAB) | -0.1440 | 0.5211 | ±1.0422 | -0.276 | 0.7823 |  |
| Site: UW (vs UAB) | +0.4566 | 0.5484 | ±1.0967 | +0.833 | 0.4050 |  |
| Age (years) | -0.0322 | 0.0249 | ±0.0498 | -1.291 | 0.1966 |  |
| BMI (kg/m2) | -0.0576 | 0.0363 | ±0.0727 | -1.586 | 0.1127 |  |
| Hypertension | -0.1710 | 0.4960 | ±0.9920 | -0.345 | 0.7303 |  |
| High cholesterol | +0.2791 | 0.4615 | ±0.9230 | +0.605 | 0.5453 |  |
| Kidney disease | -0.3712 | 0.6830 | ±1.3660 | -0.543 | 0.5868 |  |
| Circulatory disease | +0.4425 | 0.6317 | ±1.2634 | +0.701 | 0.4836 |  |
| Avg. daily time < 70 (%) | +0.6190 | 0.4121 | ±0.8242 | +1.502 | 0.1331 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **205**, R² = **0.1549**, Adj R² = **0.1068**, F-statistic = **3.22** (p = **4.82e-04**), Residual SE = **2.891** on **193** df, AIC = **1028.7**, BIC = **1068.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5092** | 1.9873 | ±3.9746 | **+14.346** | **1.13e-46** | *** |
| **Education: graduate level (vs college)** | **+1.4389** | 0.4414 | ±0.8828 | **+3.260** | **0.0011** | ** |
| Education: high school or below (vs college) | -1.3692 | 0.8039 | ±1.6077 | -1.703 | 0.0885 | . |
| Site: UCSD (vs UAB) | -0.1946 | 0.5229 | ±1.0459 | -0.372 | 0.7097 |  |
| Site: UW (vs UAB) | +0.4053 | 0.5480 | ±1.0959 | +0.740 | 0.4595 |  |
| Age (years) | -0.0266 | 0.0244 | ±0.0487 | -1.094 | 0.2740 |  |
| BMI (kg/m2) | -0.0572 | 0.0369 | ±0.0739 | -1.548 | 0.1216 |  |
| Hypertension | -0.1481 | 0.4958 | ±0.9916 | -0.299 | 0.7652 |  |
| High cholesterol | +0.2820 | 0.4656 | ±0.9312 | +0.606 | 0.5447 |  |
| Kidney disease | -0.3053 | 0.6920 | ±1.3841 | -0.441 | 0.6591 |  |
| Circulatory disease | +0.5040 | 0.6278 | ±1.2557 | +0.803 | 0.4221 |  |
| Time 181-250, pooled (%) | -0.0527 | 0.0429 | ±0.0859 | -1.229 | 0.2192 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **205**, R² = **0.1537**, Adj R² = **0.1055**, F-statistic = **3.19** (p = **5.37e-04**), Residual SE = **2.893** on **193** df, AIC = **1029.0**, BIC = **1068.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5072** | 1.9864 | ±3.9729 | **+14.351** | **1.05e-46** | *** |
| **Education: graduate level (vs college)** | **+1.4333** | 0.4414 | ±0.8829 | **+3.247** | **0.0012** | ** |
| Education: high school or below (vs college) | -1.3848 | 0.8053 | ±1.6105 | -1.720 | 0.0855 | . |
| Site: UCSD (vs UAB) | -0.1902 | 0.5223 | ±1.0446 | -0.364 | 0.7158 |  |
| Site: UW (vs UAB) | +0.4186 | 0.5490 | ±1.0981 | +0.762 | 0.4458 |  |
| Age (years) | -0.0269 | 0.0244 | ±0.0488 | -1.101 | 0.2709 |  |
| BMI (kg/m2) | -0.0576 | 0.0370 | ±0.0739 | -1.560 | 0.1189 |  |
| Hypertension | -0.1445 | 0.4975 | ±0.9950 | -0.290 | 0.7715 |  |
| High cholesterol | +0.2866 | 0.4652 | ±0.9304 | +0.616 | 0.5379 |  |
| Kidney disease | -0.3137 | 0.6906 | ±1.3812 | -0.454 | 0.6497 |  |
| Circulatory disease | +0.5016 | 0.6275 | ±1.2549 | +0.799 | 0.4241 |  |
| Avg. daily time 181-250 (%) | -0.0482 | 0.0431 | ±0.0863 | -1.117 | 0.2642 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **205**, R² = **0.1549**, Adj R² = **0.1068**, F-statistic = **3.22** (p = **4.82e-04**), Residual SE = **2.891** on **193** df, AIC = **1028.7**, BIC = **1068.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5092** | 1.9873 | ±3.9746 | **+14.346** | **1.13e-46** | *** |
| **Education: graduate level (vs college)** | **+1.4389** | 0.4414 | ±0.8828 | **+3.260** | **0.0011** | ** |
| Education: high school or below (vs college) | -1.3692 | 0.8039 | ±1.6077 | -1.703 | 0.0885 | . |
| Site: UCSD (vs UAB) | -0.1946 | 0.5229 | ±1.0459 | -0.372 | 0.7097 |  |
| Site: UW (vs UAB) | +0.4053 | 0.5480 | ±1.0959 | +0.740 | 0.4595 |  |
| Age (years) | -0.0266 | 0.0244 | ±0.0487 | -1.094 | 0.2740 |  |
| BMI (kg/m2) | -0.0572 | 0.0369 | ±0.0739 | -1.548 | 0.1216 |  |
| Hypertension | -0.1481 | 0.4958 | ±0.9916 | -0.299 | 0.7652 |  |
| High cholesterol | +0.2820 | 0.4656 | ±0.9312 | +0.606 | 0.5447 |  |
| Kidney disease | -0.3053 | 0.6920 | ±1.3841 | -0.441 | 0.6591 |  |
| Circulatory disease | +0.5040 | 0.6278 | ±1.2557 | +0.803 | 0.4221 |  |
| Time > 180 (%) | -0.0527 | 0.0429 | ±0.0859 | -1.229 | 0.2192 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **205**, R² = **0.1537**, Adj R² = **0.1055**, F-statistic = **3.19** (p = **5.37e-04**), Residual SE = **2.893** on **193** df, AIC = **1029.0**, BIC = **1068.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5072** | 1.9864 | ±3.9729 | **+14.351** | **1.05e-46** | *** |
| **Education: graduate level (vs college)** | **+1.4333** | 0.4414 | ±0.8829 | **+3.247** | **0.0012** | ** |
| Education: high school or below (vs college) | -1.3848 | 0.8053 | ±1.6105 | -1.720 | 0.0855 | . |
| Site: UCSD (vs UAB) | -0.1902 | 0.5223 | ±1.0446 | -0.364 | 0.7158 |  |
| Site: UW (vs UAB) | +0.4186 | 0.5490 | ±1.0981 | +0.762 | 0.4458 |  |
| Age (years) | -0.0269 | 0.0244 | ±0.0488 | -1.101 | 0.2709 |  |
| BMI (kg/m2) | -0.0576 | 0.0370 | ±0.0739 | -1.560 | 0.1189 |  |
| Hypertension | -0.1445 | 0.4975 | ±0.9950 | -0.290 | 0.7715 |  |
| High cholesterol | +0.2866 | 0.4652 | ±0.9304 | +0.616 | 0.5379 |  |
| Kidney disease | -0.3137 | 0.6906 | ±1.3812 | -0.454 | 0.6497 |  |
| Circulatory disease | +0.5016 | 0.6275 | ±1.2549 | +0.799 | 0.4241 |  |
| Avg. daily time > 180 (%) | -0.0482 | 0.0431 | ±0.0863 | -1.117 | 0.2642 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 205)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **205**, R² = **0.1652**, Adj R² = **0.1176**, F-statistic = **3.47** (p = **1.94e-04**), Residual SE = **2.873** on **193** df, AIC = **1026.1**, BIC = **1066.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.4888** | 1.9515 | ±3.9029 | **+14.599** | **2.86e-48** | *** |
| **Education: graduate level (vs college)** | **+1.4240** | 0.4386 | ±0.8773 | **+3.246** | **0.0012** | ** |
| Education: high school or below (vs college) | -1.2558 | 0.8133 | ±1.6266 | -1.544 | 0.1226 |  |
| Site: UCSD (vs UAB) | -0.2991 | 0.5165 | ±1.0330 | -0.579 | 0.5626 |  |
| Site: UW (vs UAB) | +0.3127 | 0.5467 | ±1.0935 | +0.572 | 0.5673 |  |
| Age (years) | -0.0276 | 0.0239 | ±0.0479 | -1.155 | 0.2481 |  |
| BMI (kg/m2) | -0.0520 | 0.0367 | ±0.0734 | -1.417 | 0.1565 |  |
| Hypertension | -0.2703 | 0.4861 | ±0.9722 | -0.556 | 0.5782 |  |
| High cholesterol | +0.3305 | 0.4609 | ±0.9218 | +0.717 | 0.4734 |  |
| Kidney disease | -0.2206 | 0.6877 | ±1.3755 | -0.321 | 0.7483 |  |
| Circulatory disease | +0.5624 | 0.6275 | ±1.2550 | +0.896 | 0.3701 |  |
| Nocturnal time > 180 (%) | -0.0804 | 0.0487 | ±0.0973 | -1.653 | 0.0983 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 205; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.0987**, LLR χ² = **27.91** (p = **0.0019**), AUC = **0.7130**, AIC = **276.9**, BIC = **313.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3154 | 1.4382 | ±2.8765 | -0.915 | 0.3604 | 0.2684 |  |
| **Education: graduate level (vs college)** | **-1.1943** | 0.3330 | ±0.6661 | **-3.586** | **3.36e-04** | 0.3029 | *** |
| Education: high school or below (vs college) | +0.6075 | 0.4635 | ±0.9270 | +1.311 | 0.1900 | 1.8358 |  |
| Site: UCSD (vs UAB) | +0.0064 | 0.3807 | ±0.7615 | +0.017 | 0.9866 | 1.0064 |  |
| Site: UW (vs UAB) | -0.2916 | 0.3940 | ±0.7880 | -0.740 | 0.4592 | 0.7471 |  |
| Age (years) | +0.0182 | 0.0167 | ±0.0335 | +1.089 | 0.2763 | 1.0184 |  |
| BMI (kg/m2) | +0.0249 | 0.0229 | ±0.0457 | +1.088 | 0.2767 | 1.0252 |  |
| Hypertension | +0.0665 | 0.3583 | ±0.7166 | +0.185 | 0.8529 | 1.0687 |  |
| High cholesterol | -0.5088 | 0.3235 | ±0.6471 | -1.573 | 0.1158 | 0.6012 |  |
| Kidney disease | +0.4204 | 0.4780 | ±0.9560 | +0.880 | 0.3791 | 1.5226 |  |
| Circulatory disease | -0.3015 | 0.4015 | ±0.8029 | -0.751 | 0.4526 | 0.7397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1067**, LLR χ² = **30.18** (p = **0.0015**), AUC = **0.7200**, AIC = **276.6**, BIC = **316.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -3.7475 | 2.1909 | ±4.3818 | -1.710 | 0.0872 | 0.0236 | . |
| **Education: graduate level (vs college)** | **-1.1923** | 0.3353 | ±0.6706 | **-3.556** | **3.77e-04** | 0.3035 | *** |
| Education: high school or below (vs college) | +0.5762 | 0.4641 | ±0.9282 | +1.242 | 0.2144 | 1.7793 |  |
| Site: UCSD (vs UAB) | +0.0208 | 0.3829 | ±0.7658 | +0.054 | 0.9567 | 1.0210 |  |
| Site: UW (vs UAB) | -0.2826 | 0.3962 | ±0.7924 | -0.713 | 0.4757 | 0.7538 |  |
| Age (years) | +0.0172 | 0.0169 | ±0.0337 | +1.018 | 0.3089 | 1.0173 |  |
| BMI (kg/m2) | +0.0178 | 0.0234 | ±0.0468 | +0.763 | 0.4454 | 1.0180 |  |
| Hypertension | +0.0374 | 0.3609 | ±0.7219 | +0.104 | 0.9174 | 1.0381 |  |
| High cholesterol | -0.5791 | 0.3302 | ±0.6604 | -1.754 | 0.0795 | 0.5604 | . |
| Kidney disease | +0.5088 | 0.4845 | ±0.9689 | +1.050 | 0.2936 | 1.6633 |  |
| Circulatory disease | -0.3863 | 0.4082 | ±0.8164 | -0.946 | 0.3440 | 0.6796 |  |
| HbA1c (%) | +0.4639 | 0.3160 | ±0.6320 | +1.468 | 0.1420 | 1.5903 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1218**, LLR χ² = **34.46** (p = **3.04e-04**), AUC = **0.7303**, AIC = **272.3**, BIC = **312.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-5.1167** | 2.1110 | ±4.2220 | **-2.424** | **0.0154** | 0.0060 | * |
| **Education: graduate level (vs college)** | **-1.2315** | 0.3406 | ±0.6812 | **-3.616** | **3.00e-04** | 0.2919 | *** |
| Education: high school or below (vs college) | +0.7121 | 0.4764 | ±0.9528 | +1.495 | 0.1350 | 2.0384 |  |
| Site: UCSD (vs UAB) | +0.0199 | 0.3870 | ±0.7740 | +0.051 | 0.9589 | 1.0201 |  |
| Site: UW (vs UAB) | -0.2845 | 0.4021 | ±0.8041 | -0.708 | 0.4792 | 0.7524 |  |
| Age (years) | +0.0186 | 0.0170 | ±0.0340 | +1.093 | 0.2743 | 1.0188 |  |
| BMI (kg/m2) | +0.0199 | 0.0231 | ±0.0463 | +0.861 | 0.3890 | 1.0201 |  |
| Hypertension | +0.0208 | 0.3675 | ±0.7350 | +0.057 | 0.9549 | 1.0210 |  |
| High cholesterol | -0.5078 | 0.3295 | ±0.6590 | -1.541 | 0.1233 | 0.6018 |  |
| Kidney disease | +0.3208 | 0.4811 | ±0.9622 | +0.667 | 0.5049 | 1.3782 |  |
| Circulatory disease | -0.3685 | 0.4111 | ±0.8221 | -0.897 | 0.3699 | 0.6917 |  |
| **Mean glucose (mg/dL)** | **+0.0312** | 0.0125 | ±0.0250 | **+2.498** | **0.0125** | 1.0317 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1218**, LLR χ² = **34.46** (p = **3.04e-04**), AUC = **0.7303**, AIC = **272.3**, BIC = **312.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-9.4386** | 3.5721 | ±7.1443 | **-2.642** | **0.0082** | 0.0001 | ** |
| **Education: graduate level (vs college)** | **-1.2315** | 0.3406 | ±0.6812 | **-3.616** | **3.00e-04** | 0.2919 | *** |
| Education: high school or below (vs college) | +0.7121 | 0.4764 | ±0.9528 | +1.495 | 0.1350 | 2.0384 |  |
| Site: UCSD (vs UAB) | +0.0199 | 0.3870 | ±0.7740 | +0.051 | 0.9589 | 1.0201 |  |
| Site: UW (vs UAB) | -0.2845 | 0.4021 | ±0.8041 | -0.708 | 0.4792 | 0.7524 |  |
| Age (years) | +0.0186 | 0.0170 | ±0.0340 | +1.093 | 0.2743 | 1.0188 |  |
| BMI (kg/m2) | +0.0199 | 0.0231 | ±0.0463 | +0.861 | 0.3890 | 1.0201 |  |
| Hypertension | +0.0208 | 0.3675 | ±0.7350 | +0.057 | 0.9549 | 1.0210 |  |
| High cholesterol | -0.5078 | 0.3295 | ±0.6590 | -1.541 | 0.1233 | 0.6018 |  |
| Kidney disease | +0.3208 | 0.4811 | ±0.9622 | +0.667 | 0.5049 | 1.3782 |  |
| Circulatory disease | -0.3685 | 0.4111 | ±0.8221 | -0.897 | 0.3699 | 0.6917 |  |
| **GMI (%)** | **+1.3057** | 0.5228 | ±1.0455 | **+2.498** | **0.0125** | 3.6904 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1448**, LLR χ² = **40.95** (p = **2.46e-05**), AUC = **0.7447**, AIC = **265.8**, BIC = **305.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-6.4499** | 2.1128 | ±4.2256 | **-3.053** | **0.0023** | 0.0016 | ** |
| **Education: graduate level (vs college)** | **-1.3181** | 0.3499 | ±0.6997 | **-3.767** | **1.65e-04** | 0.2676 | *** |
| Education: high school or below (vs college) | +0.7327 | 0.4873 | ±0.9747 | +1.503 | 0.1327 | 2.0807 |  |
| Site: UCSD (vs UAB) | +0.0048 | 0.3947 | ±0.7893 | +0.012 | 0.9902 | 1.0048 |  |
| Site: UW (vs UAB) | -0.3342 | 0.4114 | ±0.8228 | -0.812 | 0.4166 | 0.7159 |  |
| Age (years) | +0.0238 | 0.0173 | ±0.0346 | +1.377 | 0.1686 | 1.0241 |  |
| BMI (kg/m2) | +0.0165 | 0.0236 | ±0.0472 | +0.700 | 0.4840 | 1.0167 |  |
| Hypertension | +0.0508 | 0.3735 | ±0.7469 | +0.136 | 0.8918 | 1.0521 |  |
| High cholesterol | -0.5641 | 0.3344 | ±0.6688 | -1.687 | 0.0916 | 0.5689 | . |
| Kidney disease | +0.4399 | 0.4922 | ±0.9843 | +0.894 | 0.3714 | 1.5526 |  |
| Circulatory disease | -0.4304 | 0.4149 | ±0.8298 | -1.037 | 0.2996 | 0.6503 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0406** | 0.0118 | ±0.0236 | **+3.433** | **5.98e-04** | 1.0414 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1160**, LLR χ² = **32.79** (p = **5.68e-04**), AUC = **0.7265**, AIC = **274.0**, BIC = **313.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.9010 | 1.6433 | ±3.2866 | -1.765 | 0.0775 | 0.0550 | . |
| **Education: graduate level (vs college)** | **-1.2804** | 0.3412 | ±0.6823 | **-3.753** | **1.75e-04** | 0.2779 | *** |
| Education: high school or below (vs college) | +0.4335 | 0.4753 | ±0.9505 | +0.912 | 0.3616 | 1.5427 |  |
| Site: UCSD (vs UAB) | +0.0641 | 0.3857 | ±0.7714 | +0.166 | 0.8681 | 1.0662 |  |
| Site: UW (vs UAB) | -0.1736 | 0.4042 | ±0.8084 | -0.429 | 0.6676 | 0.8406 |  |
| Age (years) | +0.0164 | 0.0170 | ±0.0340 | +0.968 | 0.3330 | 1.0166 |  |
| BMI (kg/m2) | +0.0267 | 0.0231 | ±0.0463 | +1.155 | 0.2480 | 1.0271 |  |
| Hypertension | -0.0463 | 0.3688 | ±0.7375 | -0.126 | 0.9001 | 0.9547 |  |
| High cholesterol | -0.4833 | 0.3275 | ±0.6550 | -1.476 | 0.1400 | 0.6168 |  |
| Kidney disease | +0.2658 | 0.4826 | ±0.9651 | +0.551 | 0.5818 | 1.3044 |  |
| Circulatory disease | -0.3734 | 0.4069 | ±0.8138 | -0.918 | 0.3589 | 0.6884 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0784** | 0.0360 | ±0.0719 | **+2.181** | **0.0292** | 1.0816 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1147**, LLR χ² = **32.42** (p = **6.52e-04**), AUC = **0.7224**, AIC = **274.4**, BIC = **314.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.7013 | 1.6115 | ±3.2231 | -1.676 | 0.0937 | 0.0671 | . |
| **Education: graduate level (vs college)** | **-1.2694** | 0.3404 | ±0.6807 | **-3.730** | **1.92e-04** | 0.2810 | *** |
| Education: high school or below (vs college) | +0.4771 | 0.4720 | ±0.9439 | +1.011 | 0.3121 | 1.6114 |  |
| Site: UCSD (vs UAB) | +0.0218 | 0.3845 | ±0.7690 | +0.057 | 0.9547 | 1.0221 |  |
| Site: UW (vs UAB) | -0.2177 | 0.4019 | ±0.8039 | -0.542 | 0.5881 | 0.8044 |  |
| Age (years) | +0.0161 | 0.0170 | ±0.0339 | +0.951 | 0.3414 | 1.0163 |  |
| BMI (kg/m2) | +0.0268 | 0.0231 | ±0.0462 | +1.158 | 0.2471 | 1.0271 |  |
| Hypertension | -0.0682 | 0.3700 | ±0.7400 | -0.184 | 0.8537 | 0.9340 |  |
| High cholesterol | -0.4761 | 0.3276 | ±0.6553 | -1.453 | 0.1462 | 0.6212 |  |
| Kidney disease | +0.3158 | 0.4799 | ±0.9597 | +0.658 | 0.5104 | 1.3714 |  |
| Circulatory disease | -0.3341 | 0.4050 | ±0.8100 | -0.825 | 0.4094 | 0.7160 |  |
| **Avg. daily SD (mg/dL)** | **+0.0765** | 0.0365 | ±0.0730 | **+2.098** | **0.0359** | 1.0795 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1039**, LLR χ² = **29.38** (p = **0.0020**), AUC = **0.7156**, AIC = **277.4**, BIC = **317.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.3628 | 1.6945 | ±3.3890 | -1.394 | 0.1632 | 0.0942 |  |
| **Education: graduate level (vs college)** | **-1.2394** | 0.3372 | ±0.6743 | **-3.676** | **2.37e-04** | 0.2896 | *** |
| Education: high school or below (vs college) | +0.4661 | 0.4786 | ±0.9571 | +0.974 | 0.3301 | 1.5937 |  |
| Site: UCSD (vs UAB) | +0.0430 | 0.3830 | ±0.7661 | +0.112 | 0.9105 | 1.0440 |  |
| Site: UW (vs UAB) | -0.2186 | 0.4007 | ±0.8014 | -0.545 | 0.5855 | 0.8037 |  |
| Age (years) | +0.0168 | 0.0169 | ±0.0337 | +0.994 | 0.3201 | 1.0169 |  |
| BMI (kg/m2) | +0.0272 | 0.0230 | ±0.0461 | +1.182 | 0.2373 | 1.0276 |  |
| Hypertension | +0.0050 | 0.3637 | ±0.7274 | +0.014 | 0.9890 | 1.0050 |  |
| High cholesterol | -0.4924 | 0.3245 | ±0.6490 | -1.517 | 0.1292 | 0.6112 |  |
| Kidney disease | +0.3446 | 0.4823 | ±0.9645 | +0.715 | 0.4748 | 1.4115 |  |
| Circulatory disease | -0.3287 | 0.4020 | ±0.8041 | -0.818 | 0.4136 | 0.7199 |  |
| CV (%) | +0.0643 | 0.0533 | ±0.1067 | +1.206 | 0.2279 | 1.0664 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1037**, LLR χ² = **29.33** (p = **0.0020**), AUC = **0.7177**, AIC = **277.5**, BIC = **317.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2015 | 1.7223 | ±3.4445 | -0.117 | 0.9068 | 0.8175 |  |
| **Education: graduate level (vs college)** | **-1.2328** | 0.3365 | ±0.6730 | **-3.664** | **2.49e-04** | 0.2915 | *** |
| Education: high school or below (vs college) | +0.4818 | 0.4757 | ±0.9513 | +1.013 | 0.3111 | 1.6189 |  |
| Site: UCSD (vs UAB) | +0.0311 | 0.3821 | ±0.7642 | +0.081 | 0.9351 | 1.0316 |  |
| Site: UW (vs UAB) | -0.2315 | 0.3991 | ±0.7983 | -0.580 | 0.5620 | 0.7934 |  |
| Age (years) | +0.0167 | 0.0169 | ±0.0337 | +0.987 | 0.3235 | 1.0168 |  |
| BMI (kg/m2) | +0.0262 | 0.0230 | ±0.0460 | +1.141 | 0.2538 | 1.0266 |  |
| Hypertension | +0.0030 | 0.3639 | ±0.7279 | +0.008 | 0.9934 | 1.0030 |  |
| High cholesterol | -0.5022 | 0.3243 | ±0.6487 | -1.548 | 0.1215 | 0.6052 |  |
| Kidney disease | +0.3475 | 0.4812 | ±0.9623 | +0.722 | 0.4702 | 1.4155 |  |
| Circulatory disease | -0.3158 | 0.4013 | ±0.8026 | -0.787 | 0.4313 | 0.7292 |  |
| Mean / SD ratio | -0.1680 | 0.1429 | ±0.2857 | -1.176 | 0.2395 | 0.8453 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1064**, LLR χ² = **30.10** (p = **0.0015**), AUC = **0.7207**, AIC = **276.7**, BIC = **316.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0400 | 1.6864 | ±3.3727 | -0.024 | 0.9811 | 0.9608 |  |
| **Education: graduate level (vs college)** | **-1.2293** | 0.3363 | ±0.6725 | **-3.656** | **2.56e-04** | 0.2925 | *** |
| Education: high school or below (vs college) | +0.4900 | 0.4706 | ±0.9412 | +1.041 | 0.2978 | 1.6323 |  |
| Site: UCSD (vs UAB) | -0.0006 | 0.3820 | ±0.7640 | -0.001 | 0.9988 | 0.9994 |  |
| Site: UW (vs UAB) | -0.2432 | 0.3982 | ±0.7965 | -0.611 | 0.5414 | 0.7841 |  |
| Age (years) | +0.0160 | 0.0169 | ±0.0338 | +0.945 | 0.3447 | 1.0161 |  |
| BMI (kg/m2) | +0.0262 | 0.0230 | ±0.0461 | +1.139 | 0.2549 | 1.0266 |  |
| Hypertension | -0.0310 | 0.3665 | ±0.7329 | -0.085 | 0.9326 | 0.9695 |  |
| High cholesterol | -0.5078 | 0.3253 | ±0.6505 | -1.561 | 0.1185 | 0.6018 |  |
| Kidney disease | +0.3574 | 0.4794 | ±0.9587 | +0.746 | 0.4559 | 1.4296 |  |
| Circulatory disease | -0.2739 | 0.4015 | ±0.8029 | -0.682 | 0.4951 | 0.7604 |  |
| Avg. daily mean/SD | -0.1624 | 0.1126 | ±0.2253 | -1.442 | 0.1494 | 0.8501 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.0987**, LLR χ² = **27.91** (p = **0.0033**), AUC = **0.7133**, AIC = **278.9**, BIC = **318.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.2488 | 1.6769 | ±3.3538 | -0.745 | 0.4564 | 0.2869 |  |
| **Education: graduate level (vs college)** | **-1.1938** | 0.3331 | ±0.6661 | **-3.584** | **3.38e-04** | 0.3031 | *** |
| Education: high school or below (vs college) | +0.6100 | 0.4646 | ±0.9292 | +1.313 | 0.1892 | 1.8404 |  |
| Site: UCSD (vs UAB) | +0.0062 | 0.3807 | ±0.7615 | +0.016 | 0.9871 | 1.0062 |  |
| Site: UW (vs UAB) | -0.2936 | 0.3948 | ±0.7896 | -0.744 | 0.4571 | 0.7456 |  |
| Age (years) | +0.0182 | 0.0167 | ±0.0335 | +1.086 | 0.2773 | 1.0184 |  |
| BMI (kg/m2) | +0.0249 | 0.0229 | ±0.0457 | +1.090 | 0.2757 | 1.0252 |  |
| Hypertension | +0.0671 | 0.3584 | ±0.7168 | +0.187 | 0.8515 | 1.0694 |  |
| High cholesterol | -0.5072 | 0.3242 | ±0.6484 | -1.564 | 0.1177 | 0.6022 |  |
| Kidney disease | +0.4203 | 0.4780 | ±0.9560 | +0.879 | 0.3793 | 1.5224 |  |
| Circulatory disease | -0.3026 | 0.4017 | ±0.8034 | -0.753 | 0.4513 | 0.7389 |  |
| MAG (mg/dL/h) | -0.0019 | 0.0242 | ±0.0483 | -0.077 | 0.9385 | 0.9981 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1068**, LLR χ² = **30.20** (p = **0.0015**), AUC = **0.7194**, AIC = **276.6**, BIC = **316.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.5648 | 1.6793 | ±3.3586 | -1.527 | 0.1267 | 0.0769 |  |
| **Education: graduate level (vs college)** | **-1.2280** | 0.3366 | ±0.6733 | **-3.648** | **2.64e-04** | 0.2929 | *** |
| Education: high school or below (vs college) | +0.5299 | 0.4681 | ±0.9362 | +1.132 | 0.2576 | 1.6988 |  |
| Site: UCSD (vs UAB) | +0.0330 | 0.3832 | ±0.7665 | +0.086 | 0.9314 | 1.0335 |  |
| Site: UW (vs UAB) | -0.2400 | 0.3983 | ±0.7966 | -0.603 | 0.5467 | 0.7866 |  |
| Age (years) | +0.0164 | 0.0169 | ±0.0337 | +0.970 | 0.3318 | 1.0165 |  |
| BMI (kg/m2) | +0.0278 | 0.0231 | ±0.0461 | +1.208 | 0.2271 | 1.0282 |  |
| Hypertension | +0.0019 | 0.3644 | ±0.7289 | +0.005 | 0.9957 | 1.0020 |  |
| High cholesterol | -0.5013 | 0.3253 | ±0.6506 | -1.541 | 0.1233 | 0.6057 |  |
| Kidney disease | +0.3710 | 0.4779 | ±0.9558 | +0.776 | 0.4376 | 1.4491 |  |
| Circulatory disease | -0.3085 | 0.4034 | ±0.8067 | -0.765 | 0.4444 | 0.7346 |  |
| Avg. daily range (mg/dL) | +0.0134 | 0.0089 | ±0.0179 | +1.503 | 0.1327 | 1.0135 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1070**, LLR χ² = **30.25** (p = **0.0014**), AUC = **0.7170**, AIC = **276.5**, BIC = **316.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.9627 | 1.5128 | ±3.0257 | -1.297 | 0.1945 | 0.1405 |  |
| **Education: graduate level (vs college)** | **-1.2350** | 0.3373 | ±0.6745 | **-3.662** | **2.51e-04** | 0.2908 | *** |
| Education: high school or below (vs college) | +0.4727 | 0.4744 | ±0.9488 | +0.996 | 0.3191 | 1.6043 |  |
| Site: UCSD (vs UAB) | +0.1048 | 0.3882 | ±0.7764 | +0.270 | 0.7872 | 1.1105 |  |
| Site: UW (vs UAB) | -0.1798 | 0.4043 | ±0.8085 | -0.445 | 0.6564 | 0.8354 |  |
| Age (years) | +0.0181 | 0.0169 | ±0.0338 | +1.073 | 0.2834 | 1.0183 |  |
| BMI (kg/m2) | +0.0247 | 0.0229 | ±0.0458 | +1.079 | 0.2804 | 1.0250 |  |
| Hypertension | +0.1150 | 0.3624 | ±0.7247 | +0.317 | 0.7510 | 1.1219 |  |
| High cholesterol | -0.5470 | 0.3260 | ±0.6521 | -1.678 | 0.0934 | 0.5787 | . |
| Kidney disease | +0.2857 | 0.4893 | ±0.9786 | +0.584 | 0.5593 | 1.3307 |  |
| Circulatory disease | -0.4486 | 0.4182 | ±0.8364 | -1.073 | 0.2834 | 0.6385 |  |
| SD of daily means (mg/dL) | +0.0993 | 0.0656 | ±0.1311 | +1.514 | 0.1300 | 1.1044 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1063**, LLR χ² = **30.05** (p = **0.0016**), AUC = **0.7164**, AIC = **276.7**, BIC = **316.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.5321 | 3.6529 | ±7.3059 | +0.967 | 0.3336 | 34.1971 |  |
| **Education: graduate level (vs college)** | **-1.2348** | 0.3368 | ±0.6737 | **-3.666** | **2.46e-04** | 0.2909 | *** |
| Education: high school or below (vs college) | +0.5679 | 0.4672 | ±0.9343 | +1.216 | 0.2241 | 1.7646 |  |
| Site: UCSD (vs UAB) | +0.0535 | 0.3835 | ±0.7670 | +0.139 | 0.8891 | 1.0549 |  |
| Site: UW (vs UAB) | -0.2485 | 0.3982 | ±0.7964 | -0.624 | 0.5326 | 0.7800 |  |
| Age (years) | +0.0161 | 0.0169 | ±0.0337 | +0.956 | 0.3392 | 1.0162 |  |
| BMI (kg/m2) | +0.0240 | 0.0230 | ±0.0459 | +1.047 | 0.2950 | 1.0243 |  |
| Hypertension | +0.0473 | 0.3628 | ±0.7256 | +0.130 | 0.8963 | 1.0484 |  |
| High cholesterol | -0.4902 | 0.3253 | ±0.6506 | -1.507 | 0.1318 | 0.6125 |  |
| Kidney disease | +0.3109 | 0.4832 | ±0.9665 | +0.643 | 0.5200 | 1.3646 |  |
| Circulatory disease | -0.3512 | 0.4058 | ±0.8115 | -0.866 | 0.3867 | 0.7038 |  |
| Time in range 70-180, pooled (%) | -0.0488 | 0.0340 | ±0.0680 | -1.436 | 0.1509 | 0.9524 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1060**, LLR χ² = **29.99** (p = **0.0016**), AUC = **0.7161**, AIC = **276.8**, BIC = **316.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.5390 | 3.7018 | ±7.4037 | +0.956 | 0.3391 | 34.4311 |  |
| **Education: graduate level (vs college)** | **-1.2310** | 0.3366 | ±0.6732 | **-3.657** | **2.55e-04** | 0.2920 | *** |
| Education: high school or below (vs college) | +0.5768 | 0.4668 | ±0.9335 | +1.236 | 0.2165 | 1.7804 |  |
| Site: UCSD (vs UAB) | +0.0519 | 0.3832 | ±0.7664 | +0.135 | 0.8924 | 1.0532 |  |
| Site: UW (vs UAB) | -0.2584 | 0.3981 | ±0.7962 | -0.649 | 0.5163 | 0.7723 |  |
| Age (years) | +0.0160 | 0.0169 | ±0.0337 | +0.951 | 0.3417 | 1.0162 |  |
| BMI (kg/m2) | +0.0244 | 0.0230 | ±0.0459 | +1.061 | 0.2885 | 1.0247 |  |
| Hypertension | +0.0430 | 0.3628 | ±0.7255 | +0.118 | 0.9057 | 1.0439 |  |
| High cholesterol | -0.4931 | 0.3252 | ±0.6504 | -1.516 | 0.1295 | 0.6107 |  |
| Kidney disease | +0.3111 | 0.4835 | ±0.9671 | +0.643 | 0.5199 | 1.3650 |  |
| Circulatory disease | -0.3510 | 0.4059 | ±0.8117 | -0.865 | 0.3871 | 0.7040 |  |
| Avg. daily time in range 70-180 (%) | -0.0488 | 0.0344 | ±0.0689 | -1.417 | 0.1564 | 0.9524 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1032**, LLR χ² = **29.17** (p = **0.0021**), AUC = **0.7141**, AIC = **277.6**, BIC = **317.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3193 | 1.4432 | ±2.8864 | -0.914 | 0.3606 | 0.2673 |  |
| **Education: graduate level (vs college)** | **-1.1678** | 0.3341 | ±0.6682 | **-3.495** | **4.74e-04** | 0.3111 | *** |
| Education: high school or below (vs college) | +0.6885 | 0.4728 | ±0.9455 | +1.456 | 0.1453 | 1.9908 |  |
| Site: UCSD (vs UAB) | -0.0178 | 0.3824 | ±0.7648 | -0.047 | 0.9628 | 0.9823 |  |
| Site: UW (vs UAB) | -0.3128 | 0.3967 | ±0.7934 | -0.789 | 0.4304 | 0.7314 |  |
| Age (years) | +0.0201 | 0.0169 | ±0.0338 | +1.189 | 0.2346 | 1.0203 |  |
| BMI (kg/m2) | +0.0232 | 0.0229 | ±0.0458 | +1.012 | 0.3115 | 1.0235 |  |
| Hypertension | +0.0638 | 0.3593 | ±0.7187 | +0.178 | 0.8591 | 1.0659 |  |
| High cholesterol | -0.4811 | 0.3250 | ±0.6499 | -1.481 | 0.1387 | 0.6181 |  |
| Kidney disease | +0.3960 | 0.4770 | ±0.9539 | +0.830 | 0.4064 | 1.4858 |  |
| Circulatory disease | -0.2675 | 0.4057 | ±0.8113 | -0.659 | 0.5096 | 0.7653 |  |
| Time 54-69, pooled (%) | -0.7046 | 0.6731 | ±1.3462 | -1.047 | 0.2952 | 0.4943 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1029**, LLR χ² = **29.10** (p = **0.0022**), AUC = **0.7141**, AIC = **277.7**, BIC = **317.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3403 | 1.4433 | ±2.8865 | -0.929 | 0.3531 | 0.2618 |  |
| **Education: graduate level (vs college)** | **-1.1709** | 0.3341 | ±0.6681 | **-3.505** | **4.57e-04** | 0.3101 | *** |
| Education: high school or below (vs college) | +0.6804 | 0.4718 | ±0.9437 | +1.442 | 0.1493 | 1.9746 |  |
| Site: UCSD (vs UAB) | -0.0007 | 0.3818 | ±0.7636 | -0.002 | 0.9985 | 0.9993 |  |
| Site: UW (vs UAB) | -0.3021 | 0.3961 | ±0.7922 | -0.763 | 0.4456 | 0.7392 |  |
| Age (years) | +0.0202 | 0.0169 | ±0.0338 | +1.195 | 0.2321 | 1.0204 |  |
| BMI (kg/m2) | +0.0232 | 0.0229 | ±0.0458 | +1.011 | 0.3118 | 1.0235 |  |
| Hypertension | +0.0702 | 0.3592 | ±0.7184 | +0.195 | 0.8451 | 1.0727 |  |
| High cholesterol | -0.4838 | 0.3248 | ±0.6497 | -1.489 | 0.1364 | 0.6164 |  |
| Kidney disease | +0.3817 | 0.4773 | ±0.9546 | +0.800 | 0.4239 | 1.4648 |  |
| Circulatory disease | -0.2779 | 0.4049 | ±0.8098 | -0.686 | 0.4926 | 0.7574 |  |
| Avg. daily time 54-69 (%) | -0.6839 | 0.6778 | ±1.3556 | -1.009 | 0.3130 | 0.5047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1032**, LLR χ² = **29.17** (p = **0.0021**), AUC = **0.7141**, AIC = **277.6**, BIC = **317.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3193 | 1.4432 | ±2.8864 | -0.914 | 0.3606 | 0.2673 |  |
| **Education: graduate level (vs college)** | **-1.1678** | 0.3341 | ±0.6682 | **-3.495** | **4.74e-04** | 0.3111 | *** |
| Education: high school or below (vs college) | +0.6885 | 0.4728 | ±0.9455 | +1.456 | 0.1453 | 1.9908 |  |
| Site: UCSD (vs UAB) | -0.0178 | 0.3824 | ±0.7648 | -0.047 | 0.9628 | 0.9823 |  |
| Site: UW (vs UAB) | -0.3128 | 0.3967 | ±0.7934 | -0.789 | 0.4304 | 0.7314 |  |
| Age (years) | +0.0201 | 0.0169 | ±0.0338 | +1.189 | 0.2346 | 1.0203 |  |
| BMI (kg/m2) | +0.0232 | 0.0229 | ±0.0458 | +1.012 | 0.3115 | 1.0235 |  |
| Hypertension | +0.0638 | 0.3593 | ±0.7187 | +0.178 | 0.8591 | 1.0659 |  |
| High cholesterol | -0.4811 | 0.3250 | ±0.6499 | -1.481 | 0.1387 | 0.6181 |  |
| Kidney disease | +0.3960 | 0.4770 | ±0.9539 | +0.830 | 0.4064 | 1.4858 |  |
| Circulatory disease | -0.2675 | 0.4057 | ±0.8113 | -0.659 | 0.5096 | 0.7653 |  |
| Time < 70 (%) | -0.7046 | 0.6731 | ±1.3462 | -1.047 | 0.2952 | 0.4943 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1029**, LLR χ² = **29.10** (p = **0.0022**), AUC = **0.7141**, AIC = **277.7**, BIC = **317.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3403 | 1.4433 | ±2.8865 | -0.929 | 0.3531 | 0.2618 |  |
| **Education: graduate level (vs college)** | **-1.1709** | 0.3341 | ±0.6681 | **-3.505** | **4.57e-04** | 0.3101 | *** |
| Education: high school or below (vs college) | +0.6804 | 0.4718 | ±0.9437 | +1.442 | 0.1493 | 1.9746 |  |
| Site: UCSD (vs UAB) | -0.0007 | 0.3818 | ±0.7636 | -0.002 | 0.9985 | 0.9993 |  |
| Site: UW (vs UAB) | -0.3021 | 0.3961 | ±0.7922 | -0.763 | 0.4456 | 0.7392 |  |
| Age (years) | +0.0202 | 0.0169 | ±0.0338 | +1.195 | 0.2321 | 1.0204 |  |
| BMI (kg/m2) | +0.0232 | 0.0229 | ±0.0458 | +1.011 | 0.3118 | 1.0235 |  |
| Hypertension | +0.0702 | 0.3592 | ±0.7184 | +0.195 | 0.8451 | 1.0727 |  |
| High cholesterol | -0.4838 | 0.3248 | ±0.6497 | -1.489 | 0.1364 | 0.6164 |  |
| Kidney disease | +0.3817 | 0.4773 | ±0.9546 | +0.800 | 0.4239 | 1.4648 |  |
| Circulatory disease | -0.2779 | 0.4049 | ±0.8098 | -0.686 | 0.4926 | 0.7574 |  |
| Avg. daily time < 70 (%) | -0.6839 | 0.6778 | ±1.3556 | -1.009 | 0.3130 | 0.5047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1068**, LLR χ² = **30.20** (p = **0.0015**), AUC = **0.7159**, AIC = **276.6**, BIC = **316.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3524 | 1.4442 | ±2.8885 | -0.936 | 0.3491 | 0.2586 |  |
| **Education: graduate level (vs college)** | **-1.2335** | 0.3368 | ±0.6736 | **-3.662** | **2.50e-04** | 0.2913 | *** |
| Education: high school or below (vs college) | +0.5733 | 0.4672 | ±0.9345 | +1.227 | 0.2198 | 1.7741 |  |
| Site: UCSD (vs UAB) | +0.0532 | 0.3835 | ±0.7671 | +0.139 | 0.8897 | 1.0546 |  |
| Site: UW (vs UAB) | -0.2483 | 0.3984 | ±0.7968 | -0.623 | 0.5332 | 0.7802 |  |
| Age (years) | +0.0162 | 0.0169 | ±0.0337 | +0.962 | 0.3359 | 1.0164 |  |
| BMI (kg/m2) | +0.0239 | 0.0230 | ±0.0459 | +1.041 | 0.2978 | 1.0242 |  |
| Hypertension | +0.0466 | 0.3630 | ±0.7261 | +0.128 | 0.8980 | 1.0477 |  |
| High cholesterol | -0.4871 | 0.3255 | ±0.6510 | -1.497 | 0.1345 | 0.6144 |  |
| Kidney disease | +0.3052 | 0.4834 | ±0.9668 | +0.631 | 0.5278 | 1.3569 |  |
| Circulatory disease | -0.3505 | 0.4059 | ±0.8119 | -0.863 | 0.3879 | 0.7043 |  |
| Time 181-250, pooled (%) | +0.0502 | 0.0338 | ±0.0676 | +1.486 | 0.1373 | 1.0515 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1066**, LLR χ² = **30.13** (p = **0.0015**), AUC = **0.7166**, AIC = **276.6**, BIC = **316.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3482 | 1.4444 | ±2.8888 | -0.933 | 0.3506 | 0.2597 |  |
| **Education: graduate level (vs college)** | **-1.2296** | 0.3366 | ±0.6732 | **-3.653** | **2.59e-04** | 0.2924 | *** |
| Education: high school or below (vs college) | +0.5818 | 0.4669 | ±0.9337 | +1.246 | 0.2127 | 1.7893 |  |
| Site: UCSD (vs UAB) | +0.0526 | 0.3832 | ±0.7665 | +0.137 | 0.8909 | 1.0540 |  |
| Site: UW (vs UAB) | -0.2577 | 0.3984 | ±0.7967 | -0.647 | 0.5177 | 0.7728 |  |
| Age (years) | +0.0162 | 0.0169 | ±0.0337 | +0.959 | 0.3376 | 1.0163 |  |
| BMI (kg/m2) | +0.0243 | 0.0230 | ±0.0459 | +1.056 | 0.2910 | 1.0246 |  |
| Hypertension | +0.0427 | 0.3629 | ±0.7259 | +0.118 | 0.9063 | 1.0436 |  |
| High cholesterol | -0.4902 | 0.3254 | ±0.6508 | -1.507 | 0.1319 | 0.6125 |  |
| Kidney disease | +0.3048 | 0.4837 | ±0.9675 | +0.630 | 0.5286 | 1.3564 |  |
| Circulatory disease | -0.3507 | 0.4061 | ±0.8121 | -0.864 | 0.3878 | 0.7042 |  |
| Avg. daily time 181-250 (%) | +0.0501 | 0.0342 | ±0.0684 | +1.465 | 0.1430 | 1.0514 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1068**, LLR χ² = **30.20** (p = **0.0015**), AUC = **0.7159**, AIC = **276.6**, BIC = **316.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3524 | 1.4442 | ±2.8885 | -0.936 | 0.3491 | 0.2586 |  |
| **Education: graduate level (vs college)** | **-1.2335** | 0.3368 | ±0.6736 | **-3.662** | **2.50e-04** | 0.2913 | *** |
| Education: high school or below (vs college) | +0.5733 | 0.4672 | ±0.9345 | +1.227 | 0.2198 | 1.7741 |  |
| Site: UCSD (vs UAB) | +0.0532 | 0.3835 | ±0.7671 | +0.139 | 0.8897 | 1.0546 |  |
| Site: UW (vs UAB) | -0.2483 | 0.3984 | ±0.7968 | -0.623 | 0.5332 | 0.7802 |  |
| Age (years) | +0.0162 | 0.0169 | ±0.0337 | +0.962 | 0.3359 | 1.0164 |  |
| BMI (kg/m2) | +0.0239 | 0.0230 | ±0.0459 | +1.041 | 0.2978 | 1.0242 |  |
| Hypertension | +0.0466 | 0.3630 | ±0.7261 | +0.128 | 0.8980 | 1.0477 |  |
| High cholesterol | -0.4871 | 0.3255 | ±0.6510 | -1.497 | 0.1345 | 0.6144 |  |
| Kidney disease | +0.3052 | 0.4834 | ±0.9668 | +0.631 | 0.5278 | 1.3569 |  |
| Circulatory disease | -0.3505 | 0.4059 | ±0.8119 | -0.863 | 0.3879 | 0.7043 |  |
| Time > 180 (%) | +0.0502 | 0.0338 | ±0.0676 | +1.486 | 0.1373 | 1.0515 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1066**, LLR χ² = **30.13** (p = **0.0015**), AUC = **0.7166**, AIC = **276.6**, BIC = **316.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3482 | 1.4444 | ±2.8888 | -0.933 | 0.3506 | 0.2597 |  |
| **Education: graduate level (vs college)** | **-1.2296** | 0.3366 | ±0.6732 | **-3.653** | **2.59e-04** | 0.2924 | *** |
| Education: high school or below (vs college) | +0.5818 | 0.4669 | ±0.9337 | +1.246 | 0.2127 | 1.7893 |  |
| Site: UCSD (vs UAB) | +0.0526 | 0.3832 | ±0.7665 | +0.137 | 0.8909 | 1.0540 |  |
| Site: UW (vs UAB) | -0.2577 | 0.3984 | ±0.7967 | -0.647 | 0.5177 | 0.7728 |  |
| Age (years) | +0.0162 | 0.0169 | ±0.0337 | +0.959 | 0.3376 | 1.0163 |  |
| BMI (kg/m2) | +0.0243 | 0.0230 | ±0.0459 | +1.056 | 0.2910 | 1.0246 |  |
| Hypertension | +0.0427 | 0.3629 | ±0.7259 | +0.118 | 0.9063 | 1.0436 |  |
| High cholesterol | -0.4902 | 0.3254 | ±0.6508 | -1.507 | 0.1319 | 0.6125 |  |
| Kidney disease | +0.3048 | 0.4837 | ±0.9675 | +0.630 | 0.5286 | 1.3564 |  |
| Circulatory disease | -0.3507 | 0.4061 | ±0.8121 | -0.864 | 0.3878 | 0.7042 |  |
| Avg. daily time > 180 (%) | +0.0501 | 0.0342 | ±0.0684 | +1.465 | 0.1430 | 1.0514 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 205)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **205**, events = **94**, McFadden pseudo-R² = **0.1144**, LLR χ² = **32.35** (p = **6.70e-04**), AUC = **0.7233**, AIC = **274.4**, BIC = **314.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4222 | 1.4577 | ±2.9154 | -0.976 | 0.3293 | 0.2412 |  |
| **Education: graduate level (vs college)** | **-1.2335** | 0.3375 | ±0.6751 | **-3.654** | **2.58e-04** | 0.2913 | *** |
| Education: high school or below (vs college) | +0.4957 | 0.4757 | ±0.9514 | +1.042 | 0.2974 | 1.6416 |  |
| Site: UCSD (vs UAB) | +0.1318 | 0.3880 | ±0.7760 | +0.340 | 0.7340 | 1.1409 |  |
| Site: UW (vs UAB) | -0.1823 | 0.4022 | ±0.8044 | -0.453 | 0.6503 | 0.8333 |  |
| Age (years) | +0.0181 | 0.0169 | ±0.0338 | +1.071 | 0.2841 | 1.0183 |  |
| BMI (kg/m2) | +0.0214 | 0.0232 | ±0.0464 | +0.920 | 0.3573 | 1.0216 |  |
| Hypertension | +0.1321 | 0.3670 | ±0.7339 | +0.360 | 0.7188 | 1.1413 |  |
| High cholesterol | -0.5250 | 0.3257 | ±0.6514 | -1.612 | 0.1070 | 0.5915 |  |
| Kidney disease | +0.2652 | 0.4855 | ±0.9711 | +0.546 | 0.5849 | 1.3037 |  |
| Circulatory disease | -0.4019 | 0.4110 | ±0.8220 | -0.978 | 0.3281 | 0.6690 |  |
| Nocturnal time > 180 (%) | +0.0750 | 0.0391 | ±0.0782 | +1.919 | 0.0549 | 1.0779 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 205; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **205**, R² = **0.0629**, Adj R² = **0.0146**, F-statistic = **1.30** (p = **0.2312**), Residual SE = **2.482** on **194** df, AIC = **965.2**, BIC = **1001.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7932** | 1.6596 | ±3.3193 | **+9.516** | **1.80e-21** | *** |
| Education: graduate level (vs college) | +0.4353 | 0.4056 | ±0.8113 | +1.073 | 0.2832 |  |
| Education: high school or below (vs college) | -0.5682 | 0.6239 | ±1.2478 | -0.911 | 0.3624 |  |
| Site: UCSD (vs UAB) | +0.3764 | 0.5117 | ±1.0235 | +0.735 | 0.4620 |  |
| Site: UW (vs UAB) | +0.7030 | 0.4113 | ±0.8226 | +1.709 | 0.0874 | . |
| Age (years) | -0.0391 | 0.0223 | ±0.0446 | -1.753 | 0.0796 | . |
| BMI (kg/m2) | -0.0355 | 0.0257 | ±0.0513 | -1.384 | 0.1664 |  |
| Hypertension | +0.0015 | 0.4038 | ±0.8076 | +0.004 | 0.9970 |  |
| High cholesterol | -0.0177 | 0.3824 | ±0.7648 | -0.046 | 0.9631 |  |
| Kidney disease | +0.0552 | 0.6630 | ±1.3261 | +0.083 | 0.9336 |  |
| Circulatory disease | +0.0558 | 0.5527 | ±1.1054 | +0.101 | 0.9196 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **205**, R² = **0.0700**, Adj R² = **0.0170**, F-statistic = **1.32** (p = **0.2158**), Residual SE = **2.479** on **193** df, AIC = **965.7**, BIC = **1005.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.0131** | 2.6470 | ±5.2940 | **+6.805** | **1.01e-11** | *** |
| Education: graduate level (vs college) | +0.4143 | 0.4101 | ±0.8202 | +1.010 | 0.3124 |  |
| Education: high school or below (vs college) | -0.5450 | 0.6198 | ±1.2396 | -0.879 | 0.3792 |  |
| Site: UCSD (vs UAB) | +0.3649 | 0.5113 | ±1.0225 | +0.714 | 0.4754 |  |
| Site: UW (vs UAB) | +0.6950 | 0.4121 | ±0.8241 | +1.687 | 0.0917 | . |
| Age (years) | -0.0383 | 0.0223 | ±0.0446 | -1.716 | 0.0862 | . |
| BMI (kg/m2) | -0.0288 | 0.0260 | ±0.0521 | -1.107 | 0.2685 |  |
| Hypertension | +0.0307 | 0.3997 | ±0.7995 | +0.077 | 0.9388 |  |
| High cholesterol | +0.0288 | 0.3938 | ±0.7876 | +0.073 | 0.9417 |  |
| Kidney disease | -0.0062 | 0.6714 | ±1.3428 | -0.009 | 0.9926 |  |
| Circulatory disease | +0.1268 | 0.5345 | ±1.0689 | +0.237 | 0.8124 |  |
| HbA1c (%) | -0.4207 | 0.3836 | ±0.7672 | -1.097 | 0.2727 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **205**, R² = **0.0672**, Adj R² = **0.0140**, F-statistic = **1.26** (p = **0.2478**), Residual SE = **2.483** on **193** df, AIC = **966.3**, BIC = **1006.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.3634** | 2.8524 | ±5.7048 | **+6.087** | **1.15e-09** | *** |
| Education: graduate level (vs college) | +0.4273 | 0.4100 | ±0.8200 | +1.042 | 0.2972 |  |
| Education: high school or below (vs college) | -0.5960 | 0.6275 | ±1.2551 | -0.950 | 0.3423 |  |
| Site: UCSD (vs UAB) | +0.3711 | 0.5142 | ±1.0285 | +0.722 | 0.4705 |  |
| Site: UW (vs UAB) | +0.6869 | 0.4104 | ±0.8208 | +1.674 | 0.0942 | . |
| Age (years) | -0.0392 | 0.0222 | ±0.0444 | -1.766 | 0.0774 | . |
| BMI (kg/m2) | -0.0332 | 0.0257 | ±0.0514 | -1.291 | 0.1967 |  |
| Hypertension | +0.0176 | 0.4057 | ±0.8115 | +0.043 | 0.9654 |  |
| High cholesterol | -0.0281 | 0.3819 | ±0.7639 | -0.074 | 0.9413 |  |
| Kidney disease | +0.1014 | 0.6552 | ±1.3105 | +0.155 | 0.8770 |  |
| Circulatory disease | +0.0701 | 0.5470 | ±1.0940 | +0.128 | 0.8981 |  |
| Mean glucose (mg/dL) | -0.0129 | 0.0164 | ±0.0327 | -0.789 | 0.4303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **205**, R² = **0.0672**, Adj R² = **0.0140**, F-statistic = **1.26** (p = **0.2478**), Residual SE = **2.483** on **193** df, AIC = **966.3**, BIC = **1006.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19.1482** | 4.8919 | ±9.7839 | **+3.914** | **9.07e-05** | *** |
| Education: graduate level (vs college) | +0.4273 | 0.4100 | ±0.8200 | +1.042 | 0.2972 |  |
| Education: high school or below (vs college) | -0.5960 | 0.6275 | ±1.2551 | -0.950 | 0.3423 |  |
| Site: UCSD (vs UAB) | +0.3711 | 0.5142 | ±1.0285 | +0.722 | 0.4705 |  |
| Site: UW (vs UAB) | +0.6869 | 0.4104 | ±0.8208 | +1.674 | 0.0942 | . |
| Age (years) | -0.0392 | 0.0222 | ±0.0444 | -1.766 | 0.0774 | . |
| BMI (kg/m2) | -0.0332 | 0.0257 | ±0.0514 | -1.291 | 0.1967 |  |
| Hypertension | +0.0176 | 0.4057 | ±0.8115 | +0.043 | 0.9654 |  |
| High cholesterol | -0.0281 | 0.3819 | ±0.7639 | -0.074 | 0.9413 |  |
| Kidney disease | +0.1014 | 0.6552 | ±1.3105 | +0.155 | 0.8770 |  |
| Circulatory disease | +0.0701 | 0.5470 | ±1.0940 | +0.128 | 0.8981 |  |
| GMI (%) | -0.5392 | 0.6838 | ±1.3675 | -0.789 | 0.4303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **205**, R² = **0.0811**, Adj R² = **0.0287**, F-statistic = **1.55** (p = **0.1173**), Residual SE = **2.465** on **193** df, AIC = **963.2**, BIC = **1003.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.7680** | 2.6240 | ±5.2480 | **+7.152** | **8.53e-13** | *** |
| Education: graduate level (vs college) | +0.4467 | 0.4015 | ±0.8030 | +1.113 | 0.2659 |  |
| Education: high school or below (vs college) | -0.6049 | 0.6242 | ±1.2484 | -0.969 | 0.3325 |  |
| Site: UCSD (vs UAB) | +0.3873 | 0.5104 | ±1.0209 | +0.759 | 0.4480 |  |
| Site: UW (vs UAB) | +0.6936 | 0.4161 | ±0.8323 | +1.667 | 0.0956 | . |
| Age (years) | -0.0420 | 0.0222 | ±0.0445 | -1.889 | 0.0589 | . |
| BMI (kg/m2) | -0.0293 | 0.0258 | ±0.0517 | -1.133 | 0.2571 |  |
| Hypertension | +0.0040 | 0.4044 | ±0.8087 | +0.010 | 0.9921 |  |
| High cholesterol | -0.0059 | 0.3820 | ±0.7639 | -0.016 | 0.9876 |  |
| Kidney disease | +0.0770 | 0.6577 | ±1.3154 | +0.117 | 0.9068 |  |
| Circulatory disease | +0.1189 | 0.5282 | ±1.0564 | +0.225 | 0.8219 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0238 | 0.0144 | ±0.0288 | -1.650 | 0.0989 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **205**, R² = **0.0658**, Adj R² = **0.0126**, F-statistic = **1.24** (p = **0.2655**), Residual SE = **2.485** on **193** df, AIC = **966.6**, BIC = **1006.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3936** | 1.8732 | ±3.7463 | **+8.752** | **2.10e-18** | *** |
| Education: graduate level (vs college) | +0.4540 | 0.4035 | ±0.8069 | +1.125 | 0.2605 |  |
| Education: high school or below (vs college) | -0.4922 | 0.6495 | ±1.2989 | -0.758 | 0.4486 |  |
| Site: UCSD (vs UAB) | +0.3533 | 0.5189 | ±1.0378 | +0.681 | 0.4960 |  |
| Site: UW (vs UAB) | +0.6499 | 0.4103 | ±0.8206 | +1.584 | 0.1132 |  |
| Age (years) | -0.0381 | 0.0223 | ±0.0446 | -1.707 | 0.0879 | . |
| BMI (kg/m2) | -0.0357 | 0.0257 | ±0.0514 | -1.391 | 0.1643 |  |
| Hypertension | +0.0447 | 0.4049 | ±0.8097 | +0.110 | 0.9121 |  |
| High cholesterol | -0.0378 | 0.3771 | ±0.7542 | -0.100 | 0.9201 |  |
| Kidney disease | +0.1194 | 0.6733 | ±1.3466 | +0.177 | 0.8592 |  |
| Circulatory disease | +0.0838 | 0.5434 | ±1.0868 | +0.154 | 0.8774 |  |
| Glucose SD, pooled (mg/dL) | -0.0310 | 0.0433 | ±0.0866 | -0.717 | 0.4736 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **205**, R² = **0.0670**, Adj R² = **0.0139**, F-statistic = **1.26** (p = **0.2501**), Residual SE = **2.483** on **193** df, AIC = **966.3**, BIC = **1006.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4431** | 1.8325 | ±3.6650 | **+8.973** | **2.88e-19** | *** |
| Education: graduate level (vs college) | +0.4545 | 0.4032 | ±0.8064 | +1.127 | 0.2596 |  |
| Education: high school or below (vs college) | -0.4966 | 0.6454 | ±1.2908 | -0.769 | 0.4416 |  |
| Site: UCSD (vs UAB) | +0.3696 | 0.5153 | ±1.0306 | +0.717 | 0.4733 |  |
| Site: UW (vs UAB) | +0.6582 | 0.4121 | ±0.8242 | +1.597 | 0.1102 |  |
| Age (years) | -0.0377 | 0.0223 | ±0.0445 | -1.696 | 0.0900 | . |
| BMI (kg/m2) | -0.0358 | 0.0257 | ±0.0513 | -1.396 | 0.1628 |  |
| Hypertension | +0.0677 | 0.4071 | ±0.8142 | +0.166 | 0.8679 |  |
| High cholesterol | -0.0441 | 0.3750 | ±0.7499 | -0.118 | 0.9063 |  |
| Kidney disease | +0.1078 | 0.6701 | ±1.3402 | +0.161 | 0.8722 |  |
| Circulatory disease | +0.0729 | 0.5461 | ±1.0922 | +0.133 | 0.8938 |  |
| Avg. daily SD (mg/dL) | -0.0376 | 0.0439 | ±0.0877 | -0.858 | 0.3909 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **205**, R² = **0.0634**, Adj R² = **0.0100**, F-statistic = **1.19** (p = **0.2984**), Residual SE = **2.488** on **193** df, AIC = **967.1**, BIC = **1007.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0750** | 1.8129 | ±3.6258 | **+8.867** | **7.51e-19** | *** |
| Education: graduate level (vs college) | +0.4448 | 0.4111 | ±0.8221 | +1.082 | 0.2792 |  |
| Education: high school or below (vs college) | -0.5276 | 0.6524 | ±1.3047 | -0.809 | 0.4187 |  |
| Site: UCSD (vs UAB) | +0.3666 | 0.5210 | ±1.0419 | +0.704 | 0.4816 |  |
| Site: UW (vs UAB) | +0.6817 | 0.4213 | ±0.8425 | +1.618 | 0.1056 |  |
| Age (years) | -0.0386 | 0.0227 | ±0.0454 | -1.701 | 0.0889 | . |
| BMI (kg/m2) | -0.0361 | 0.0257 | ±0.0515 | -1.400 | 0.1614 |  |
| Hypertension | +0.0183 | 0.4055 | ±0.8110 | +0.045 | 0.9639 |  |
| High cholesterol | -0.0247 | 0.3799 | ±0.7597 | -0.065 | 0.9481 |  |
| Kidney disease | +0.0762 | 0.6810 | ±1.3619 | +0.112 | 0.9109 |  |
| Circulatory disease | +0.0648 | 0.5535 | ±1.1071 | +0.117 | 0.9068 |  |
| CV (%) | -0.0178 | 0.0615 | ±0.1230 | -0.289 | 0.7726 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **205**, R² = **0.0646**, Adj R² = **0.0112**, F-statistic = **1.21** (p = **0.2820**), Residual SE = **2.487** on **193** df, AIC = **966.9**, BIC = **1006.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.1742** | 2.0832 | ±4.1664 | **+7.284** | **3.24e-13** | *** |
| Education: graduate level (vs college) | +0.4509 | 0.4093 | ±0.8187 | +1.102 | 0.2707 |  |
| Education: high school or below (vs college) | -0.4987 | 0.6442 | ±1.2883 | -0.774 | 0.4389 |  |
| Site: UCSD (vs UAB) | +0.3629 | 0.5167 | ±1.0333 | +0.702 | 0.4825 |  |
| Site: UW (vs UAB) | +0.6662 | 0.4179 | ±0.8359 | +1.594 | 0.1110 |  |
| Age (years) | -0.0381 | 0.0228 | ±0.0455 | -1.673 | 0.0942 | . |
| BMI (kg/m2) | -0.0359 | 0.0256 | ±0.0512 | -1.402 | 0.1609 |  |
| Hypertension | +0.0361 | 0.4054 | ±0.8109 | +0.089 | 0.9290 |  |
| High cholesterol | -0.0266 | 0.3803 | ±0.7606 | -0.070 | 0.9443 |  |
| Kidney disease | +0.0947 | 0.6773 | ±1.3546 | +0.140 | 0.8888 |  |
| Circulatory disease | +0.0676 | 0.5505 | ±1.1010 | +0.123 | 0.9023 |  |
| Mean / SD ratio | +0.0906 | 0.1487 | ±0.2974 | +0.609 | 0.5422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **205**, R² = **0.0690**, Adj R² = **0.0159**, F-statistic = **1.30** (p = **0.2271**), Residual SE = **2.481** on **193** df, AIC = **965.9**, BIC = **1005.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.6901** | 1.9957 | ±3.9915 | **+7.361** | **1.83e-13** | *** |
| Education: graduate level (vs college) | +0.4536 | 0.4074 | ±0.8148 | +1.113 | 0.2655 |  |
| Education: high school or below (vs college) | -0.4681 | 0.6339 | ±1.2679 | -0.738 | 0.4603 |  |
| Site: UCSD (vs UAB) | +0.3860 | 0.5115 | ±1.0230 | +0.755 | 0.4505 |  |
| Site: UW (vs UAB) | +0.6506 | 0.4163 | ±0.8325 | +1.563 | 0.1181 |  |
| Age (years) | -0.0369 | 0.0227 | ±0.0455 | -1.624 | 0.1044 |  |
| BMI (kg/m2) | -0.0358 | 0.0255 | ±0.0509 | -1.406 | 0.1598 |  |
| Hypertension | +0.0900 | 0.4094 | ±0.8188 | +0.220 | 0.8260 |  |
| High cholesterol | -0.0266 | 0.3799 | ±0.7598 | -0.070 | 0.9442 |  |
| Kidney disease | +0.1054 | 0.6728 | ±1.3457 | +0.157 | 0.8755 |  |
| Circulatory disease | +0.0446 | 0.5485 | ±1.0971 | +0.081 | 0.9352 |  |
| Avg. daily mean/SD | +0.1343 | 0.1050 | ±0.2100 | +1.279 | 0.2008 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **205**, R² = **0.0632**, Adj R² = **0.0099**, F-statistic = **1.18** (p = **0.2999**), Residual SE = **2.488** on **193** df, AIC = **967.2**, BIC = **1007.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0348** | 1.8527 | ±3.7054 | **+8.655** | **4.93e-18** | *** |
| Education: graduate level (vs college) | +0.4376 | 0.4087 | ±0.8173 | +1.071 | 0.2842 |  |
| Education: high school or below (vs college) | -0.5579 | 0.6291 | ±1.2582 | -0.887 | 0.3752 |  |
| Site: UCSD (vs UAB) | +0.3772 | 0.5133 | ±1.0265 | +0.735 | 0.4624 |  |
| Site: UW (vs UAB) | +0.6962 | 0.4172 | ±0.8343 | +1.669 | 0.0951 | . |
| Age (years) | -0.0392 | 0.0224 | ±0.0447 | -1.756 | 0.0791 | . |
| BMI (kg/m2) | -0.0352 | 0.0259 | ±0.0517 | -1.361 | 0.1736 |  |
| Hypertension | +0.0051 | 0.4044 | ±0.8088 | +0.013 | 0.9900 |  |
| High cholesterol | -0.0118 | 0.3887 | ±0.7774 | -0.030 | 0.9757 |  |
| Kidney disease | +0.0538 | 0.6662 | ±1.3324 | +0.081 | 0.9356 |  |
| Circulatory disease | +0.0512 | 0.5587 | ±1.1175 | +0.092 | 0.9270 |  |
| MAG (mg/dL/h) | -0.0069 | 0.0265 | ±0.0529 | -0.259 | 0.7954 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **205**, R² = **0.0651**, Adj R² = **0.0118**, F-statistic = **1.22** (p = **0.2744**), Residual SE = **2.486** on **193** df, AIC = **966.8**, BIC = **1006.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4081** | 1.9077 | ±3.8153 | **+8.601** | **7.89e-18** | *** |
| Education: graduate level (vs college) | +0.4425 | 0.4060 | ±0.8120 | +1.090 | 0.2758 |  |
| Education: high school or below (vs college) | -0.5266 | 0.6394 | ±1.2788 | -0.824 | 0.4102 |  |
| Site: UCSD (vs UAB) | +0.3641 | 0.5185 | ±1.0370 | +0.702 | 0.4825 |  |
| Site: UW (vs UAB) | +0.6722 | 0.4167 | ±0.8334 | +1.613 | 0.1067 |  |
| Age (years) | -0.0380 | 0.0224 | ±0.0447 | -1.701 | 0.0889 | . |
| BMI (kg/m2) | -0.0366 | 0.0258 | ±0.0515 | -1.421 | 0.1552 |  |
| Hypertension | +0.0349 | 0.4038 | ±0.8075 | +0.086 | 0.9312 |  |
| High cholesterol | -0.0271 | 0.3796 | ±0.7591 | -0.071 | 0.9431 |  |
| Kidney disease | +0.0787 | 0.6705 | ±1.3410 | +0.117 | 0.9065 |  |
| Circulatory disease | +0.0592 | 0.5515 | ±1.1030 | +0.107 | 0.9145 |  |
| Avg. daily range (mg/dL) | -0.0068 | 0.0107 | ±0.0214 | -0.635 | 0.5253 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **205**, R² = **0.0647**, Adj R² = **0.0114**, F-statistic = **1.21** (p = **0.2794**), Residual SE = **2.486** on **193** df, AIC = **966.8**, BIC = **1006.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0739** | 1.7075 | ±3.4149 | **+9.414** | **4.78e-21** | *** |
| Education: graduate level (vs college) | +0.4435 | 0.4089 | ±0.8177 | +1.085 | 0.2781 |  |
| Education: high school or below (vs college) | -0.4987 | 0.6499 | ±1.2999 | -0.767 | 0.4429 |  |
| Site: UCSD (vs UAB) | +0.3320 | 0.5132 | ±1.0265 | +0.647 | 0.5177 |  |
| Site: UW (vs UAB) | +0.6538 | 0.4006 | ±0.8011 | +1.632 | 0.1026 |  |
| Age (years) | -0.0388 | 0.0224 | ±0.0449 | -1.728 | 0.0840 | . |
| BMI (kg/m2) | -0.0354 | 0.0260 | ±0.0519 | -1.363 | 0.1729 |  |
| Hypertension | -0.0210 | 0.4056 | ±0.8112 | -0.052 | 0.9588 |  |
| High cholesterol | -0.0077 | 0.3846 | ±0.7693 | -0.020 | 0.9841 |  |
| Kidney disease | +0.1224 | 0.6681 | ±1.3362 | +0.183 | 0.8546 |  |
| Circulatory disease | +0.1151 | 0.5484 | ±1.0968 | +0.210 | 0.8338 |  |
| SD of daily means (mg/dL) | -0.0452 | 0.0803 | ±0.1607 | -0.563 | 0.5734 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **205**, R² = **0.0647**, Adj R² = **0.0114**, F-statistic = **1.21** (p = **0.2797**), Residual SE = **2.486** on **193** df, AIC = **966.8**, BIC = **1006.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13.4773** | 4.6982 | ±9.3964 | **+2.869** | **0.0041** | ** |
| Education: graduate level (vs college) | +0.4459 | 0.4007 | ±0.8015 | +1.113 | 0.2658 |  |
| Education: high school or below (vs college) | -0.5416 | 0.6349 | ±1.2697 | -0.853 | 0.3936 |  |
| Site: UCSD (vs UAB) | +0.3550 | 0.5155 | ±1.0309 | +0.689 | 0.4911 |  |
| Site: UW (vs UAB) | +0.6791 | 0.4075 | ±0.8151 | +1.666 | 0.0956 | . |
| Age (years) | -0.0379 | 0.0219 | ±0.0437 | -1.732 | 0.0833 | . |
| BMI (kg/m2) | -0.0349 | 0.0257 | ±0.0515 | -1.354 | 0.1757 |  |
| Hypertension | +0.0081 | 0.4067 | ±0.8135 | +0.020 | 0.9841 |  |
| High cholesterol | -0.0291 | 0.3818 | ±0.7637 | -0.076 | 0.9393 |  |
| Kidney disease | +0.1037 | 0.6518 | ±1.3037 | +0.159 | 0.8736 |  |
| Circulatory disease | +0.0729 | 0.5447 | ±1.0893 | +0.134 | 0.8935 |  |
| Time in range 70-180, pooled (%) | +0.0232 | 0.0477 | ±0.0954 | +0.486 | 0.6272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **205**, R² = **0.0644**, Adj R² = **0.0111**, F-statistic = **1.21** (p = **0.2843**), Residual SE = **2.487** on **193** df, AIC = **966.9**, BIC = **1006.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13.6661** | 4.8805 | ±9.7610 | **+2.800** | **0.0051** | ** |
| Education: graduate level (vs college) | +0.4434 | 0.4020 | ±0.8041 | +1.103 | 0.2701 |  |
| Education: high school or below (vs college) | -0.5488 | 0.6345 | ±1.2689 | -0.865 | 0.3871 |  |
| Site: UCSD (vs UAB) | +0.3574 | 0.5144 | ±1.0289 | +0.695 | 0.4872 |  |
| Site: UW (vs UAB) | +0.6852 | 0.4085 | ±0.8169 | +1.678 | 0.0934 | . |
| Age (years) | -0.0380 | 0.0219 | ±0.0438 | -1.734 | 0.0829 | . |
| BMI (kg/m2) | -0.0351 | 0.0258 | ±0.0516 | -1.360 | 0.1739 |  |
| Hypertension | +0.0099 | 0.4080 | ±0.8159 | +0.024 | 0.9806 |  |
| High cholesterol | -0.0273 | 0.3822 | ±0.7644 | -0.071 | 0.9432 |  |
| Kidney disease | +0.0998 | 0.6492 | ±1.2984 | +0.154 | 0.8778 |  |
| Circulatory disease | +0.0715 | 0.5443 | ±1.0886 | +0.131 | 0.8955 |  |
| Avg. daily time in range 70-180 (%) | +0.0213 | 0.0493 | ±0.0987 | +0.431 | 0.6667 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **205**, R² = **0.0663**, Adj R² = **0.0131**, F-statistic = **1.25** (p = **0.2589**), Residual SE = **2.484** on **193** df, AIC = **966.5**, BIC = **1006.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8667** | 1.6920 | ±3.3839 | **+9.378** | **6.74e-21** | *** |
| Education: graduate level (vs college) | +0.4050 | 0.4128 | ±0.8257 | +0.981 | 0.3266 |  |
| Education: high school or below (vs college) | -0.6251 | 0.6309 | ±1.2618 | -0.991 | 0.3218 |  |
| Site: UCSD (vs UAB) | +0.3927 | 0.5120 | ±1.0241 | +0.767 | 0.4431 |  |
| Site: UW (vs UAB) | +0.7099 | 0.4139 | ±0.8278 | +1.715 | 0.0863 | . |
| Age (years) | -0.0413 | 0.0232 | ±0.0463 | -1.785 | 0.0743 | . |
| BMI (kg/m2) | -0.0346 | 0.0255 | ±0.0510 | -1.356 | 0.1753 |  |
| Hypertension | +0.0001 | 0.4042 | ±0.8085 | +0.000 | 0.9999 |  |
| High cholesterol | -0.0446 | 0.3815 | ±0.7630 | -0.117 | 0.9069 |  |
| Kidney disease | +0.0838 | 0.6614 | ±1.3228 | +0.127 | 0.8991 |  |
| Circulatory disease | +0.0269 | 0.5601 | ±1.1202 | +0.048 | 0.9616 |  |
| Time 54-69, pooled (%) | +0.5174 | 0.6080 | ±1.2159 | +0.851 | 0.3947 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **205**, R² = **0.0670**, Adj R² = **0.0138**, F-statistic = **1.26** (p = **0.2503**), Residual SE = **2.483** on **193** df, AIC = **966.3**, BIC = **1006.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8954** | 1.6880 | ±3.3761 | **+9.417** | **4.66e-21** | *** |
| Education: graduate level (vs college) | +0.4035 | 0.4117 | ±0.8234 | +0.980 | 0.3270 |  |
| Education: high school or below (vs college) | -0.6237 | 0.6311 | ±1.2621 | -0.988 | 0.3230 |  |
| Site: UCSD (vs UAB) | +0.3795 | 0.5116 | ±1.0232 | +0.742 | 0.4582 |  |
| Site: UW (vs UAB) | +0.7009 | 0.4115 | ±0.8229 | +1.703 | 0.0885 | . |
| Age (years) | -0.0417 | 0.0230 | ±0.0460 | -1.814 | 0.0698 | . |
| BMI (kg/m2) | -0.0345 | 0.0254 | ±0.0509 | -1.356 | 0.1750 |  |
| Hypertension | -0.0056 | 0.4038 | ±0.8075 | -0.014 | 0.9890 |  |
| High cholesterol | -0.0456 | 0.3817 | ±0.7635 | -0.119 | 0.9050 |  |
| Kidney disease | +0.0970 | 0.6639 | ±1.3277 | +0.146 | 0.8839 |  |
| Circulatory disease | +0.0333 | 0.5557 | ±1.1115 | +0.060 | 0.9522 |  |
| Avg. daily time 54-69 (%) | +0.5461 | 0.4967 | ±0.9934 | +1.099 | 0.2716 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **205**, R² = **0.0663**, Adj R² = **0.0131**, F-statistic = **1.25** (p = **0.2589**), Residual SE = **2.484** on **193** df, AIC = **966.5**, BIC = **1006.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8667** | 1.6920 | ±3.3839 | **+9.378** | **6.74e-21** | *** |
| Education: graduate level (vs college) | +0.4050 | 0.4128 | ±0.8257 | +0.981 | 0.3266 |  |
| Education: high school or below (vs college) | -0.6251 | 0.6309 | ±1.2618 | -0.991 | 0.3218 |  |
| Site: UCSD (vs UAB) | +0.3927 | 0.5120 | ±1.0241 | +0.767 | 0.4431 |  |
| Site: UW (vs UAB) | +0.7099 | 0.4139 | ±0.8278 | +1.715 | 0.0863 | . |
| Age (years) | -0.0413 | 0.0232 | ±0.0463 | -1.785 | 0.0743 | . |
| BMI (kg/m2) | -0.0346 | 0.0255 | ±0.0510 | -1.356 | 0.1753 |  |
| Hypertension | +0.0001 | 0.4042 | ±0.8085 | +0.000 | 0.9999 |  |
| High cholesterol | -0.0446 | 0.3815 | ±0.7630 | -0.117 | 0.9069 |  |
| Kidney disease | +0.0838 | 0.6614 | ±1.3228 | +0.127 | 0.8991 |  |
| Circulatory disease | +0.0269 | 0.5601 | ±1.1202 | +0.048 | 0.9616 |  |
| Time < 70 (%) | +0.5174 | 0.6080 | ±1.2159 | +0.851 | 0.3947 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **205**, R² = **0.0670**, Adj R² = **0.0138**, F-statistic = **1.26** (p = **0.2503**), Residual SE = **2.483** on **193** df, AIC = **966.3**, BIC = **1006.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8954** | 1.6880 | ±3.3761 | **+9.417** | **4.66e-21** | *** |
| Education: graduate level (vs college) | +0.4035 | 0.4117 | ±0.8234 | +0.980 | 0.3270 |  |
| Education: high school or below (vs college) | -0.6237 | 0.6311 | ±1.2621 | -0.988 | 0.3230 |  |
| Site: UCSD (vs UAB) | +0.3795 | 0.5116 | ±1.0232 | +0.742 | 0.4582 |  |
| Site: UW (vs UAB) | +0.7009 | 0.4115 | ±0.8229 | +1.703 | 0.0885 | . |
| Age (years) | -0.0417 | 0.0230 | ±0.0460 | -1.814 | 0.0698 | . |
| BMI (kg/m2) | -0.0345 | 0.0254 | ±0.0509 | -1.356 | 0.1750 |  |
| Hypertension | -0.0056 | 0.4038 | ±0.8075 | -0.014 | 0.9890 |  |
| High cholesterol | -0.0456 | 0.3817 | ±0.7635 | -0.119 | 0.9050 |  |
| Kidney disease | +0.0970 | 0.6639 | ±1.3277 | +0.146 | 0.8839 |  |
| Circulatory disease | +0.0333 | 0.5557 | ±1.1115 | +0.060 | 0.9522 |  |
| Avg. daily time < 70 (%) | +0.5461 | 0.4967 | ±0.9934 | +1.099 | 0.2716 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **205**, R² = **0.0650**, Adj R² = **0.0117**, F-statistic = **1.22** (p = **0.2759**), Residual SE = **2.486** on **193** df, AIC = **966.8**, BIC = **1006.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7963** | 1.6620 | ±3.3240 | **+9.504** | **2.01e-21** | *** |
| Education: graduate level (vs college) | +0.4452 | 0.4015 | ±0.8030 | +1.109 | 0.2675 |  |
| Education: high school or below (vs college) | -0.5425 | 0.6341 | ±1.2683 | -0.856 | 0.3923 |  |
| Site: UCSD (vs UAB) | +0.3543 | 0.5154 | ±1.0308 | +0.687 | 0.4918 |  |
| Site: UW (vs UAB) | +0.6778 | 0.4075 | ±0.8151 | +1.663 | 0.0963 | . |
| Age (years) | -0.0379 | 0.0219 | ±0.0437 | -1.733 | 0.0832 | . |
| BMI (kg/m2) | -0.0348 | 0.0257 | ±0.0515 | -1.351 | 0.1766 |  |
| Hypertension | +0.0085 | 0.4066 | ±0.8132 | +0.021 | 0.9834 |  |
| High cholesterol | -0.0311 | 0.3816 | ±0.7632 | -0.082 | 0.9350 |  |
| Kidney disease | +0.1083 | 0.6517 | ±1.3035 | +0.166 | 0.8680 |  |
| Circulatory disease | +0.0727 | 0.5452 | ±1.0904 | +0.133 | 0.8940 |  |
| Time 181-250, pooled (%) | -0.0247 | 0.0475 | ±0.0950 | -0.520 | 0.6030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **205**, R² = **0.0647**, Adj R² = **0.0114**, F-statistic = **1.21** (p = **0.2803**), Residual SE = **2.486** on **193** df, AIC = **966.9**, BIC = **1006.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7954** | 1.6627 | ±3.3253 | **+9.500** | **2.10e-21** | *** |
| Education: graduate level (vs college) | +0.4427 | 0.4028 | ±0.8057 | +1.099 | 0.2718 |  |
| Education: high school or below (vs college) | -0.5494 | 0.6336 | ±1.2671 | -0.867 | 0.3859 |  |
| Site: UCSD (vs UAB) | +0.3559 | 0.5145 | ±1.0289 | +0.692 | 0.4891 |  |
| Site: UW (vs UAB) | +0.6836 | 0.4085 | ±0.8170 | +1.673 | 0.0943 | . |
| Age (years) | -0.0380 | 0.0219 | ±0.0438 | -1.735 | 0.0828 | . |
| BMI (kg/m2) | -0.0350 | 0.0258 | ±0.0516 | -1.357 | 0.1748 |  |
| Hypertension | +0.0104 | 0.4077 | ±0.8154 | +0.025 | 0.9797 |  |
| High cholesterol | -0.0293 | 0.3820 | ±0.7639 | -0.077 | 0.9389 |  |
| Kidney disease | +0.1055 | 0.6492 | ±1.2984 | +0.163 | 0.8709 |  |
| Circulatory disease | +0.0719 | 0.5446 | ±1.0893 | +0.132 | 0.8950 |  |
| Avg. daily time 181-250 (%) | -0.0231 | 0.0489 | ±0.0979 | -0.472 | 0.6367 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **205**, R² = **0.0650**, Adj R² = **0.0117**, F-statistic = **1.22** (p = **0.2759**), Residual SE = **2.486** on **193** df, AIC = **966.8**, BIC = **1006.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7963** | 1.6620 | ±3.3240 | **+9.504** | **2.01e-21** | *** |
| Education: graduate level (vs college) | +0.4452 | 0.4015 | ±0.8030 | +1.109 | 0.2675 |  |
| Education: high school or below (vs college) | -0.5425 | 0.6341 | ±1.2683 | -0.856 | 0.3923 |  |
| Site: UCSD (vs UAB) | +0.3543 | 0.5154 | ±1.0308 | +0.687 | 0.4918 |  |
| Site: UW (vs UAB) | +0.6778 | 0.4075 | ±0.8151 | +1.663 | 0.0963 | . |
| Age (years) | -0.0379 | 0.0219 | ±0.0437 | -1.733 | 0.0832 | . |
| BMI (kg/m2) | -0.0348 | 0.0257 | ±0.0515 | -1.351 | 0.1766 |  |
| Hypertension | +0.0085 | 0.4066 | ±0.8132 | +0.021 | 0.9834 |  |
| High cholesterol | -0.0311 | 0.3816 | ±0.7632 | -0.082 | 0.9350 |  |
| Kidney disease | +0.1083 | 0.6517 | ±1.3035 | +0.166 | 0.8680 |  |
| Circulatory disease | +0.0727 | 0.5452 | ±1.0904 | +0.133 | 0.8940 |  |
| Time > 180 (%) | -0.0247 | 0.0475 | ±0.0950 | -0.520 | 0.6030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **205**, R² = **0.0647**, Adj R² = **0.0114**, F-statistic = **1.21** (p = **0.2803**), Residual SE = **2.486** on **193** df, AIC = **966.9**, BIC = **1006.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7954** | 1.6627 | ±3.3253 | **+9.500** | **2.10e-21** | *** |
| Education: graduate level (vs college) | +0.4427 | 0.4028 | ±0.8057 | +1.099 | 0.2718 |  |
| Education: high school or below (vs college) | -0.5494 | 0.6336 | ±1.2671 | -0.867 | 0.3859 |  |
| Site: UCSD (vs UAB) | +0.3559 | 0.5145 | ±1.0289 | +0.692 | 0.4891 |  |
| Site: UW (vs UAB) | +0.6836 | 0.4085 | ±0.8170 | +1.673 | 0.0943 | . |
| Age (years) | -0.0380 | 0.0219 | ±0.0438 | -1.735 | 0.0828 | . |
| BMI (kg/m2) | -0.0350 | 0.0258 | ±0.0516 | -1.357 | 0.1748 |  |
| Hypertension | +0.0104 | 0.4077 | ±0.8154 | +0.025 | 0.9797 |  |
| High cholesterol | -0.0293 | 0.3820 | ±0.7639 | -0.077 | 0.9389 |  |
| Kidney disease | +0.1055 | 0.6492 | ±1.2984 | +0.163 | 0.8709 |  |
| Circulatory disease | +0.0719 | 0.5446 | ±1.0893 | +0.132 | 0.8950 |  |
| Avg. daily time > 180 (%) | -0.0231 | 0.0489 | ±0.0979 | -0.472 | 0.6367 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 205)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **205**, R² = **0.0721**, Adj R² = **0.0192**, F-statistic = **1.36** (p = **0.1935**), Residual SE = **2.477** on **193** df, AIC = **965.2**, BIC = **1005.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7848** | 1.6351 | ±3.2702 | **+9.654** | **4.74e-22** | *** |
| Education: graduate level (vs college) | +0.4391 | 0.4040 | ±0.8080 | +1.087 | 0.2771 |  |
| Education: high school or below (vs college) | -0.4662 | 0.6536 | ±1.3072 | -0.713 | 0.4756 |  |
| Site: UCSD (vs UAB) | +0.2845 | 0.5088 | ±1.0176 | +0.559 | 0.5760 |  |
| Site: UW (vs UAB) | +0.6143 | 0.4043 | ±0.8086 | +1.519 | 0.1287 |  |
| Age (years) | -0.0381 | 0.0219 | ±0.0438 | -1.740 | 0.0818 | . |
| BMI (kg/m2) | -0.0314 | 0.0255 | ±0.0510 | -1.234 | 0.2173 |  |
| Hypertension | -0.0636 | 0.4042 | ±0.8085 | -0.157 | 0.8751 |  |
| High cholesterol | -0.0057 | 0.3837 | ±0.7674 | -0.015 | 0.9881 |  |
| Kidney disease | +0.1752 | 0.6471 | ±1.2941 | +0.271 | 0.7866 |  |
| Circulatory disease | +0.1130 | 0.5355 | ±1.0710 | +0.211 | 0.8328 |  |
| Nocturnal time > 180 (%) | -0.0488 | 0.0475 | ±0.0949 | -1.028 | 0.3042 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
