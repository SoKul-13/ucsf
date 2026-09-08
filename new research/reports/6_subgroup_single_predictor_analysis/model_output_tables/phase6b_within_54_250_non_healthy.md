# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Non-healthy group (T2D non-insulin + T2D insulin)

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models.


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


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 204; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0889**, F-statistic = **2.98** (p = **0.0016**), Residual SE = **5.232** on **193** df, AIC = **1264.8**, BIC = **1301.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4499** | 3.3562 | ±6.7123 | **+3.412** | **6.46e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8250** | 0.7884 | ±1.5769 | **-2.315** | **0.0206** | * |
| Education: high school or below (vs college) | +1.3506 | 1.3850 | ±2.7699 | +0.975 | 0.3295 |  |
| Site: UCSD (vs UAB) | +0.0057 | 0.9806 | ±1.9611 | +0.006 | 0.9953 |  |
| Site: UW (vs UAB) | +1.1732 | 1.0358 | ±2.0715 | +1.133 | 0.2573 |  |
| **Age (years)** | **-0.1111** | 0.0396 | ±0.0791 | **-2.807** | **0.0050** | ** |
| BMI (kg/m2) | +0.0598 | 0.0565 | ±0.1130 | +1.059 | 0.2897 |  |
| Hypertension | -0.8462 | 0.9094 | ±1.8187 | -0.931 | 0.3521 |  |
| High cholesterol | +0.3900 | 0.7715 | ±1.5429 | +0.506 | 0.6132 |  |
| Kidney disease | +1.3666 | 1.2799 | ±2.5599 | +1.068 | 0.2856 |  |
| Circulatory disease | +0.6361 | 1.0940 | ±2.1880 | +0.581 | 0.5609 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **204**, R² = **0.1456**, Adj R² = **0.0966**, F-statistic = **2.97** (p = **0.0011**), Residual SE = **5.210** on **192** df, AIC = **1264.0**, BIC = **1303.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.7504** | 5.0864 | ±10.1729 | **+3.490** | **4.83e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8840** | 0.7836 | ±1.5671 | **-2.404** | **0.0162** | * |
| Education: high school or below (vs college) | +1.4072 | 1.3883 | ±2.7767 | +1.014 | 0.3108 |  |
| Site: UCSD (vs UAB) | -0.0300 | 0.9806 | ±1.9612 | -0.031 | 0.9756 |  |
| Site: UW (vs UAB) | +1.1514 | 1.0412 | ±2.0824 | +1.106 | 0.2688 |  |
| **Age (years)** | **-0.1088** | 0.0396 | ±0.0792 | **-2.749** | **0.0060** | ** |
| BMI (kg/m2) | +0.0786 | 0.0566 | ±0.1132 | +1.388 | 0.1650 |  |
| Hypertension | -0.7592 | 0.9119 | ±1.8238 | -0.833 | 0.4051 |  |
| High cholesterol | +0.5196 | 0.7618 | ±1.5236 | +0.682 | 0.4952 |  |
| Kidney disease | +1.1943 | 1.2402 | ±2.4805 | +0.963 | 0.3355 |  |
| Circulatory disease | +0.8402 | 1.0908 | ±2.1815 | +0.770 | 0.4411 |  |
| HbA1c (%) | -1.1925 | 0.7234 | ±1.4467 | -1.648 | 0.0993 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **204**, R² = **0.1430**, Adj R² = **0.0939**, F-statistic = **2.91** (p = **0.0014**), Residual SE = **5.217** on **192** df, AIC = **1264.6**, BIC = **1304.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.5058** | 4.3995 | ±8.7990 | **+3.752** | **1.76e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8500** | 0.7912 | ±1.5823 | **-2.338** | **0.0194** | * |
| Education: high school or below (vs college) | +1.2525 | 1.3661 | ±2.7321 | +0.917 | 0.3592 |  |
| Site: UCSD (vs UAB) | -0.0143 | 0.9797 | ±1.9593 | -0.015 | 0.9884 |  |
| Site: UW (vs UAB) | +1.1224 | 1.0275 | ±2.0551 | +1.092 | 0.2747 |  |
| **Age (years)** | **-0.1113** | 0.0394 | ±0.0788 | **-2.824** | **0.0047** | ** |
| BMI (kg/m2) | +0.0672 | 0.0564 | ±0.1129 | +1.190 | 0.2340 |  |
| Hypertension | -0.7903 | 0.9153 | ±1.8305 | -0.864 | 0.3878 |  |
| High cholesterol | +0.3544 | 0.7694 | ±1.5387 | +0.461 | 0.6450 |  |
| Kidney disease | +1.5169 | 1.2619 | ±2.5238 | +1.202 | 0.2293 |  |
| Circulatory disease | +0.6846 | 1.0928 | ±2.1856 | +0.626 | 0.5310 |  |
| Mean glucose (mg/dL) | -0.0415 | 0.0263 | ±0.0526 | -1.575 | 0.1152 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **204**, R² = **0.1430**, Adj R² = **0.0939**, F-statistic = **2.91** (p = **0.0014**), Residual SE = **5.217** on **192** df, AIC = **1264.6**, BIC = **1304.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.2426** | 7.3136 | ±14.6272 | **+3.041** | **0.0024** | ** |
| **Education: graduate level (vs college)** | **-1.8500** | 0.7912 | ±1.5823 | **-2.338** | **0.0194** | * |
| Education: high school or below (vs college) | +1.2525 | 1.3661 | ±2.7321 | +0.917 | 0.3592 |  |
| Site: UCSD (vs UAB) | -0.0143 | 0.9797 | ±1.9593 | -0.015 | 0.9884 |  |
| Site: UW (vs UAB) | +1.1224 | 1.0275 | ±2.0551 | +1.092 | 0.2747 |  |
| **Age (years)** | **-0.1113** | 0.0394 | ±0.0788 | **-2.824** | **0.0047** | ** |
| BMI (kg/m2) | +0.0672 | 0.0564 | ±0.1129 | +1.190 | 0.2340 |  |
| Hypertension | -0.7903 | 0.9153 | ±1.8305 | -0.864 | 0.3878 |  |
| High cholesterol | +0.3544 | 0.7694 | ±1.5387 | +0.461 | 0.6450 |  |
| Kidney disease | +1.5169 | 1.2619 | ±2.5238 | +1.202 | 0.2293 |  |
| Circulatory disease | +0.6846 | 1.0928 | ±2.1856 | +0.626 | 0.5310 |  |
| GMI (%) | -1.7332 | 1.1003 | ±2.2007 | -1.575 | 0.1152 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **204**, R² = **0.1344**, Adj R² = **0.0848**, F-statistic = **2.71** (p = **0.0029**), Residual SE = **5.244** on **192** df, AIC = **1266.6**, BIC = **1306.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.6297** | 4.4411 | ±8.8822 | **+2.844** | **0.0045** | ** |
| **Education: graduate level (vs college)** | **-1.8203** | 0.7935 | ±1.5871 | **-2.294** | **0.0218** | * |
| Education: high school or below (vs college) | +1.3329 | 1.3864 | ±2.7727 | +0.961 | 0.3363 |  |
| Site: UCSD (vs UAB) | +0.0089 | 0.9869 | ±1.9738 | +0.009 | 0.9928 |  |
| Site: UW (vs UAB) | +1.1698 | 1.0381 | ±2.0761 | +1.127 | 0.2598 |  |
| **Age (years)** | **-0.1122** | 0.0398 | ±0.0796 | **-2.821** | **0.0048** | ** |
| BMI (kg/m2) | +0.0622 | 0.0573 | ±0.1145 | +1.087 | 0.2772 |  |
| Hypertension | -0.8437 | 0.9150 | ±1.8299 | -0.922 | 0.3565 |  |
| High cholesterol | +0.3939 | 0.7730 | ±1.5460 | +0.510 | 0.6103 |  |
| Kidney disease | +1.3759 | 1.2835 | ±2.5669 | +1.072 | 0.2837 |  |
| Circulatory disease | +0.6620 | 1.1060 | ±2.2119 | +0.599 | 0.5494 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0094 | 0.0243 | ±0.0487 | -0.386 | 0.6994 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **204**, R² = **0.1365**, Adj R² = **0.0870**, F-statistic = **2.76** (p = **0.0024**), Residual SE = **5.237** on **192** df, AIC = **1266.1**, BIC = **1305.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.7466** | 3.6623 | ±7.3245 | **+3.481** | **5.00e-04** | *** |
| **Education: graduate level (vs college)** | **-1.7843** | 0.8000 | ±1.6000 | **-2.230** | **0.0257** | * |
| Education: high school or below (vs college) | +1.5029 | 1.4329 | ±2.8658 | +1.049 | 0.2942 |  |
| Site: UCSD (vs UAB) | -0.0475 | 0.9831 | ±1.9663 | -0.048 | 0.9615 |  |
| Site: UW (vs UAB) | +1.0606 | 1.0613 | ±2.1227 | +0.999 | 0.3176 |  |
| **Age (years)** | **-0.1089** | 0.0397 | ±0.0793 | **-2.745** | **0.0060** | ** |
| BMI (kg/m2) | +0.0591 | 0.0563 | ±0.1125 | +1.050 | 0.2938 |  |
| Hypertension | -0.7487 | 0.9343 | ±1.8687 | -0.801 | 0.4229 |  |
| High cholesterol | +0.3444 | 0.7832 | ±1.5664 | +0.440 | 0.6601 |  |
| Kidney disease | +1.5064 | 1.2869 | ±2.5738 | +1.171 | 0.2418 |  |
| Circulatory disease | +0.6994 | 1.1120 | ±2.2239 | +0.629 | 0.5294 |  |
| Glucose SD, pooled (mg/dL) | -0.0665 | 0.0809 | ±0.1617 | -0.823 | 0.4108 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **204**, R² = **0.1353**, Adj R² = **0.0858**, F-statistic = **2.73** (p = **0.0027**), Residual SE = **5.241** on **192** df, AIC = **1266.4**, BIC = **1306.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.3322** | 3.6166 | ±7.2331 | **+3.410** | **6.50e-04** | *** |
| **Education: graduate level (vs college)** | **-1.7987** | 0.7983 | ±1.5966 | **-2.253** | **0.0243** | * |
| Education: high school or below (vs college) | +1.4409 | 1.4228 | ±2.8456 | +1.013 | 0.3112 |  |
| Site: UCSD (vs UAB) | -0.0057 | 0.9850 | ±1.9700 | -0.006 | 0.9954 |  |
| Site: UW (vs UAB) | +1.1135 | 1.0537 | ±2.1074 | +1.057 | 0.2906 |  |
| **Age (years)** | **-0.1093** | 0.0396 | ±0.0793 | **-2.756** | **0.0058** | ** |
| BMI (kg/m2) | +0.0593 | 0.0564 | ±0.1127 | +1.052 | 0.2929 |  |
| Hypertension | -0.7540 | 0.9423 | ±1.8847 | -0.800 | 0.4236 |  |
| High cholesterol | +0.3530 | 0.7847 | ±1.5694 | +0.450 | 0.6529 |  |
| Kidney disease | +1.4388 | 1.2800 | ±2.5600 | +1.124 | 0.2610 |  |
| Circulatory disease | +0.6610 | 1.1075 | ±2.2150 | +0.597 | 0.5506 |  |
| Avg. daily SD (mg/dL) | -0.0507 | 0.0816 | ±0.1633 | -0.621 | 0.5343 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0842**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.7**, BIC = **1306.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.6899** | 3.8420 | ±7.6840 | **+3.043** | **0.0023** | ** |
| **Education: graduate level (vs college)** | **-1.8168** | 0.8008 | ±1.6016 | **-2.269** | **0.0233** | * |
| Education: high school or below (vs college) | +1.3836 | 1.4618 | ±2.9236 | +0.947 | 0.3439 |  |
| Site: UCSD (vs UAB) | -0.0030 | 0.9842 | ±1.9684 | -0.003 | 0.9975 |  |
| Site: UW (vs UAB) | +1.1553 | 1.0727 | ±2.1453 | +1.077 | 0.2814 |  |
| **Age (years)** | **-0.1107** | 0.0395 | ±0.0791 | **-2.799** | **0.0051** | ** |
| BMI (kg/m2) | +0.0593 | 0.0565 | ±0.1130 | +1.051 | 0.2935 |  |
| Hypertension | -0.8313 | 0.9252 | ±1.8504 | -0.899 | 0.3689 |  |
| High cholesterol | +0.3838 | 0.7793 | ±1.5586 | +0.492 | 0.6224 |  |
| Kidney disease | +1.3847 | 1.3000 | ±2.6000 | +1.065 | 0.2868 |  |
| Circulatory disease | +0.6441 | 1.1051 | ±2.2101 | +0.583 | 0.5600 |  |
| CV (%) | -0.0151 | 0.1144 | ±0.2289 | -0.132 | 0.8954 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **204**, R² = **0.1339**, Adj R² = **0.0843**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.7**, BIC = **1306.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.8610** | 4.0417 | ±8.0833 | **+2.935** | **0.0033** | ** |
| **Education: graduate level (vs college)** | **-1.8355** | 0.7990 | ±1.5980 | **-2.297** | **0.0216** | * |
| Education: high school or below (vs college) | +1.3061 | 1.4459 | ±2.8918 | +0.903 | 0.3664 |  |
| Site: UCSD (vs UAB) | +0.0154 | 0.9831 | ±1.9662 | +0.016 | 0.9875 |  |
| Site: UW (vs UAB) | +1.1976 | 1.0694 | ±2.1387 | +1.120 | 0.2627 |  |
| **Age (years)** | **-0.1117** | 0.0397 | ±0.0794 | **-2.815** | **0.0049** | ** |
| BMI (kg/m2) | +0.0601 | 0.0568 | ±0.1135 | +1.059 | 0.2894 |  |
| Hypertension | -0.8702 | 0.9235 | ±1.8470 | -0.942 | 0.3461 |  |
| High cholesterol | +0.3964 | 0.7778 | ±1.5556 | +0.510 | 0.6103 |  |
| Kidney disease | +1.3399 | 1.3008 | ±2.6015 | +1.030 | 0.3029 |  |
| Circulatory disease | +0.6277 | 1.1010 | ±2.2019 | +0.570 | 0.5686 |  |
| Mean / SD ratio | -0.0604 | 0.3109 | ±0.6219 | -0.194 | 0.8459 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **204**, R² = **0.1350**, Adj R² = **0.0854**, F-statistic = **2.72** (p = **0.0027**), Residual SE = **5.242** on **192** df, AIC = **1266.5**, BIC = **1306.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.5349** | 4.0024 | ±8.0049 | **+3.132** | **0.0017** | ** |
| **Education: graduate level (vs college)** | **-1.8434** | 0.7956 | ±1.5911 | **-2.317** | **0.0205** | * |
| Education: high school or below (vs college) | +1.2563 | 1.4186 | ±2.8373 | +0.886 | 0.3759 |  |
| Site: UCSD (vs UAB) | -0.0022 | 0.9789 | ±1.9578 | -0.002 | 0.9982 |  |
| Site: UW (vs UAB) | +1.2245 | 1.0601 | ±2.1202 | +1.155 | 0.2481 |  |
| **Age (years)** | **-0.1132** | 0.0398 | ±0.0795 | **-2.847** | **0.0044** | ** |
| BMI (kg/m2) | +0.0602 | 0.0571 | ±0.1142 | +1.055 | 0.2913 |  |
| Hypertension | -0.9357 | 0.9333 | ±1.8666 | -1.003 | 0.3160 |  |
| High cholesterol | +0.3998 | 0.7756 | ±1.5511 | +0.516 | 0.6062 |  |
| Kidney disease | +1.3161 | 1.2931 | ±2.5861 | +1.018 | 0.3088 |  |
| Circulatory disease | +0.6458 | 1.0961 | ±2.1923 | +0.589 | 0.5557 |  |
| Avg. daily mean/SD | -0.1327 | 0.2497 | ±0.4994 | -0.531 | 0.5952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **204**, R² = **0.1556**, Adj R² = **0.1072**, F-statistic = **3.22** (p = **4.84e-04**), Residual SE = **5.179** on **192** df, AIC = **1261.5**, BIC = **1301.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +6.9734 | 3.8959 | ±7.7918 | +1.790 | 0.0735 | . |
| **Education: graduate level (vs college)** | **-1.8693** | 0.7891 | ±1.5781 | **-2.369** | **0.0178** | * |
| Education: high school or below (vs college) | +1.1795 | 1.3409 | ±2.6818 | +0.880 | 0.3791 |  |
| Site: UCSD (vs UAB) | -0.0025 | 0.9548 | ±1.9097 | -0.003 | 0.9979 |  |
| Site: UW (vs UAB) | +1.2962 | 1.0140 | ±2.0280 | +1.278 | 0.2011 |  |
| **Age (years)** | **-0.1085** | 0.0392 | ±0.0785 | **-2.765** | **0.0057** | ** |
| BMI (kg/m2) | +0.0541 | 0.0573 | ±0.1146 | +0.944 | 0.3452 |  |
| Hypertension | -0.9214 | 0.9030 | ±1.8060 | -1.020 | 0.3076 |  |
| High cholesterol | +0.2862 | 0.7754 | ±1.5508 | +0.369 | 0.7121 |  |
| Kidney disease | +1.3889 | 1.2860 | ±2.5720 | +1.080 | 0.2801 |  |
| Circulatory disease | +0.7160 | 1.0894 | ±2.1787 | +0.657 | 0.5110 |  |
| **MAG (mg/dL/h)** | **+0.1266** | 0.0547 | ±0.1093 | **+2.315** | **0.0206** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0841**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.8**, BIC = **1306.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.3997** | 3.7671 | ±7.5341 | **+3.026** | **0.0025** | ** |
| **Education: graduate level (vs college)** | **-1.8256** | 0.7942 | ±1.5884 | **-2.299** | **0.0215** | * |
| Education: high school or below (vs college) | +1.3475 | 1.4150 | ±2.8300 | +0.952 | 0.3409 |  |
| Site: UCSD (vs UAB) | +0.0068 | 0.9809 | ±1.9618 | +0.007 | 0.9945 |  |
| Site: UW (vs UAB) | +1.1757 | 1.0506 | ±2.1012 | +1.119 | 0.2631 |  |
| **Age (years)** | **-0.1112** | 0.0398 | ±0.0795 | **-2.795** | **0.0052** | ** |
| BMI (kg/m2) | +0.0599 | 0.0568 | ±0.1135 | +1.056 | 0.2910 |  |
| Hypertension | -0.8491 | 0.9253 | ±1.8507 | -0.918 | 0.3588 |  |
| High cholesterol | +0.3908 | 0.7764 | ±1.5528 | +0.503 | 0.6147 |  |
| Kidney disease | +1.3647 | 1.2853 | ±2.5706 | +1.062 | 0.2883 |  |
| Circulatory disease | +0.6358 | 1.1019 | ±2.2037 | +0.577 | 0.5639 |  |
| Avg. daily range (mg/dL) | +0.0006 | 0.0201 | ±0.0402 | +0.027 | 0.9781 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0842**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.7**, BIC = **1306.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.5562** | 3.4988 | ±6.9976 | **+3.303** | **9.57e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8219** | 0.7955 | ±1.5909 | **-2.290** | **0.0220** | * |
| Education: high school or below (vs college) | +1.3756 | 1.4511 | ±2.9021 | +0.948 | 0.3431 |  |
| Site: UCSD (vs UAB) | -0.0113 | 0.9856 | ±1.9713 | -0.011 | 0.9909 |  |
| Site: UW (vs UAB) | +1.1549 | 1.0647 | ±2.1294 | +1.085 | 0.2780 |  |
| **Age (years)** | **-0.1109** | 0.0398 | ±0.0796 | **-2.788** | **0.0053** | ** |
| BMI (kg/m2) | +0.0599 | 0.0568 | ±0.1136 | +1.053 | 0.2921 |  |
| Hypertension | -0.8541 | 0.9196 | ±1.8392 | -0.929 | 0.3530 |  |
| High cholesterol | +0.3935 | 0.7762 | ±1.5524 | +0.507 | 0.6122 |  |
| Kidney disease | +1.3920 | 1.3289 | ±2.6577 | +1.048 | 0.2949 |  |
| Circulatory disease | +0.6587 | 1.0899 | ±2.1798 | +0.604 | 0.5456 |  |
| SD of daily means (mg/dL) | -0.0170 | 0.1613 | ±0.3225 | -0.105 | 0.9163 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **204**, R² = **0.1503**, Adj R² = **0.1016**, F-statistic = **3.09** (p = **7.68e-04**), Residual SE = **5.195** on **192** df, AIC = **1262.8**, BIC = **1302.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -3.9228 | 8.7946 | ±17.5891 | -0.446 | 0.6556 |  |
| **Education: graduate level (vs college)** | **-1.7540** | 0.7885 | ±1.5769 | **-2.225** | **0.0261** | * |
| Education: high school or below (vs college) | +1.5205 | 1.3862 | ±2.7723 | +1.097 | 0.2727 |  |
| Site: UCSD (vs UAB) | -0.1389 | 0.9724 | ±1.9448 | -0.143 | 0.8864 |  |
| Site: UW (vs UAB) | +1.0151 | 1.0229 | ±2.0458 | +0.992 | 0.3210 |  |
| **Age (years)** | **-0.1029** | 0.0402 | ±0.0805 | **-2.557** | **0.0105** | * |
| BMI (kg/m2) | +0.0640 | 0.0555 | ±0.1111 | +1.153 | 0.2489 |  |
| Hypertension | -0.7993 | 0.9164 | ±1.8329 | -0.872 | 0.3831 |  |
| High cholesterol | +0.3128 | 0.7701 | ±1.5403 | +0.406 | 0.6846 |  |
| Kidney disease | +1.6896 | 1.2364 | ±2.4727 | +1.367 | 0.1717 |  |
| Circulatory disease | +0.7515 | 1.0930 | ±2.1860 | +0.688 | 0.4917 |  |
| **Time in range 70-180, pooled (%)** | **+0.1538** | 0.0760 | ±0.1519 | **+2.024** | **0.0429** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **204**, R² = **0.1500**, Adj R² = **0.1014**, F-statistic = **3.08** (p = **7.82e-04**), Residual SE = **5.196** on **192** df, AIC = **1262.9**, BIC = **1302.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -4.1524 | 8.8587 | ±17.7175 | -0.469 | 0.6393 |  |
| **Education: graduate level (vs college)** | **-1.7656** | 0.7874 | ±1.5748 | **-2.242** | **0.0249** | * |
| Education: high school or below (vs college) | +1.4913 | 1.3836 | ±2.7671 | +1.078 | 0.2811 |  |
| Site: UCSD (vs UAB) | -0.1338 | 0.9737 | ±1.9475 | -0.137 | 0.8907 |  |
| Site: UW (vs UAB) | +1.0431 | 1.0230 | ±2.0459 | +1.020 | 0.3079 |  |
| **Age (years)** | **-0.1027** | 0.0403 | ±0.0805 | **-2.549** | **0.0108** | * |
| BMI (kg/m2) | +0.0632 | 0.0554 | ±0.1108 | +1.140 | 0.2543 |  |
| Hypertension | -0.7836 | 0.9183 | ±1.8365 | -0.853 | 0.3935 |  |
| High cholesterol | +0.3194 | 0.7696 | ±1.5392 | +0.415 | 0.6781 |  |
| Kidney disease | +1.6942 | 1.2365 | ±2.4730 | +1.370 | 0.1707 |  |
| Circulatory disease | +0.7515 | 1.0929 | ±2.1858 | +0.688 | 0.4917 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.1559** | 0.0770 | ±0.1540 | **+2.024** | **0.0429** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0842**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.7**, BIC = **1306.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4321** | 3.3765 | ±6.7531 | **+3.386** | **7.10e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8179** | 0.7962 | ±1.5925 | **-2.283** | **0.0224** | * |
| Education: high school or below (vs college) | +1.3646 | 1.3898 | ±2.7797 | +0.982 | 0.3262 |  |
| Site: UCSD (vs UAB) | +0.0021 | 0.9817 | ±1.9634 | +0.002 | 0.9983 |  |
| Site: UW (vs UAB) | +1.1715 | 1.0400 | ±2.0800 | +1.126 | 0.2600 |  |
| **Age (years)** | **-0.1105** | 0.0401 | ±0.0803 | **-2.754** | **0.0059** | ** |
| BMI (kg/m2) | +0.0596 | 0.0569 | ±0.1137 | +1.049 | 0.2942 |  |
| Hypertension | -0.8462 | 0.9113 | ±1.8226 | -0.929 | 0.3531 |  |
| High cholesterol | +0.3965 | 0.7820 | ±1.5640 | +0.507 | 0.6122 |  |
| Kidney disease | +1.3598 | 1.2822 | ±2.5645 | +1.060 | 0.2889 |  |
| Circulatory disease | +0.6427 | 1.1001 | ±2.2003 | +0.584 | 0.5591 |  |
| Time 54-69, pooled (%) | -0.1211 | 1.0901 | ±2.1801 | -0.111 | 0.9115 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0841**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.8**, BIC = **1306.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4501** | 3.3683 | ±6.7365 | **+3.399** | **6.75e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8250** | 0.7970 | ±1.5941 | **-2.290** | **0.0220** | * |
| Education: high school or below (vs college) | +1.3505 | 1.3876 | ±2.7752 | +0.973 | 0.3304 |  |
| Site: UCSD (vs UAB) | +0.0057 | 0.9825 | ±1.9650 | +0.006 | 0.9953 |  |
| Site: UW (vs UAB) | +1.1732 | 1.0385 | ±2.0771 | +1.130 | 0.2586 |  |
| **Age (years)** | **-0.1111** | 0.0401 | ±0.0801 | **-2.772** | **0.0056** | ** |
| BMI (kg/m2) | +0.0598 | 0.0569 | ±0.1137 | +1.052 | 0.2926 |  |
| Hypertension | -0.8462 | 0.9114 | ±1.8227 | -0.929 | 0.3531 |  |
| High cholesterol | +0.3900 | 0.7808 | ±1.5616 | +0.499 | 0.6175 |  |
| Kidney disease | +1.3667 | 1.2833 | ±2.5666 | +1.065 | 0.2869 |  |
| Circulatory disease | +0.6361 | 1.0974 | ±2.1949 | +0.580 | 0.5622 |  |
| Avg. daily time 54-69 (%) | +0.0007 | 0.9072 | ±1.8144 | +0.001 | 0.9994 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0842**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.7**, BIC = **1306.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4321** | 3.3765 | ±6.7531 | **+3.386** | **7.10e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8179** | 0.7962 | ±1.5925 | **-2.283** | **0.0224** | * |
| Education: high school or below (vs college) | +1.3646 | 1.3898 | ±2.7797 | +0.982 | 0.3262 |  |
| Site: UCSD (vs UAB) | +0.0021 | 0.9817 | ±1.9634 | +0.002 | 0.9983 |  |
| Site: UW (vs UAB) | +1.1715 | 1.0400 | ±2.0800 | +1.126 | 0.2600 |  |
| **Age (years)** | **-0.1105** | 0.0401 | ±0.0803 | **-2.754** | **0.0059** | ** |
| BMI (kg/m2) | +0.0596 | 0.0569 | ±0.1137 | +1.049 | 0.2942 |  |
| Hypertension | -0.8462 | 0.9113 | ±1.8226 | -0.929 | 0.3531 |  |
| High cholesterol | +0.3965 | 0.7820 | ±1.5640 | +0.507 | 0.6122 |  |
| Kidney disease | +1.3598 | 1.2822 | ±2.5645 | +1.060 | 0.2889 |  |
| Circulatory disease | +0.6427 | 1.1001 | ±2.2003 | +0.584 | 0.5591 |  |
| Time < 70 (%) | -0.1211 | 1.0901 | ±2.1801 | -0.111 | 0.9115 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **204**, R² = **0.1338**, Adj R² = **0.0841**, F-statistic = **2.70** (p = **0.0030**), Residual SE = **5.245** on **192** df, AIC = **1266.8**, BIC = **1306.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4501** | 3.3683 | ±6.7365 | **+3.399** | **6.75e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8250** | 0.7970 | ±1.5941 | **-2.290** | **0.0220** | * |
| Education: high school or below (vs college) | +1.3505 | 1.3876 | ±2.7752 | +0.973 | 0.3304 |  |
| Site: UCSD (vs UAB) | +0.0057 | 0.9825 | ±1.9650 | +0.006 | 0.9953 |  |
| Site: UW (vs UAB) | +1.1732 | 1.0385 | ±2.0771 | +1.130 | 0.2586 |  |
| **Age (years)** | **-0.1111** | 0.0401 | ±0.0801 | **-2.772** | **0.0056** | ** |
| BMI (kg/m2) | +0.0598 | 0.0569 | ±0.1137 | +1.052 | 0.2926 |  |
| Hypertension | -0.8462 | 0.9114 | ±1.8227 | -0.929 | 0.3531 |  |
| High cholesterol | +0.3900 | 0.7808 | ±1.5616 | +0.499 | 0.6175 |  |
| Kidney disease | +1.3667 | 1.2833 | ±2.5666 | +1.065 | 0.2869 |  |
| Circulatory disease | +0.6361 | 1.0974 | ±2.1949 | +0.580 | 0.5622 |  |
| Avg. daily time < 70 (%) | +0.0007 | 0.9072 | ±1.8144 | +0.001 | 0.9994 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **204**, R² = **0.1499**, Adj R² = **0.1012**, F-statistic = **3.08** (p = **7.92e-04**), Residual SE = **5.196** on **192** df, AIC = **1262.9**, BIC = **1302.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4760** | 3.3610 | ±6.7220 | **+3.414** | **6.39e-04** | *** |
| **Education: graduate level (vs college)** | **-1.7641** | 0.7881 | ±1.5762 | **-2.239** | **0.0252** | * |
| Education: high school or below (vs college) | +1.4998 | 1.3851 | ±2.7701 | +1.083 | 0.2789 |  |
| Site: UCSD (vs UAB) | -0.1317 | 0.9730 | ±1.9460 | -0.135 | 0.8923 |  |
| Site: UW (vs UAB) | +1.0202 | 1.0227 | ±2.0454 | +0.998 | 0.3185 |  |
| **Age (years)** | **-0.1037** | 0.0402 | ±0.0803 | **-2.583** | **0.0098** | ** |
| BMI (kg/m2) | +0.0642 | 0.0556 | ±0.1112 | +1.155 | 0.2480 |  |
| Hypertension | -0.8002 | 0.9165 | ±1.8330 | -0.873 | 0.3826 |  |
| High cholesterol | +0.3062 | 0.7708 | ±1.5416 | +0.397 | 0.6911 |  |
| Kidney disease | +1.6920 | 1.2389 | ±2.4778 | +1.366 | 0.1720 |  |
| Circulatory disease | +0.7412 | 1.0928 | ±2.1855 | +0.678 | 0.4976 |  |
| **Time 181-250, pooled (%)** | **-0.1508** | 0.0753 | ±0.1505 | **-2.004** | **0.0450** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **204**, R² = **0.1497**, Adj R² = **0.1010**, F-statistic = **3.07** (p = **8.04e-04**), Residual SE = **5.197** on **192** df, AIC = **1263.0**, BIC = **1302.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4669** | 3.3619 | ±6.7239 | **+3.411** | **6.48e-04** | *** |
| **Education: graduate level (vs college)** | **-1.7756** | 0.7870 | ±1.5741 | **-2.256** | **0.0241** | * |
| Education: high school or below (vs college) | +1.4722 | 1.3825 | ±2.7649 | +1.065 | 0.2869 |  |
| Site: UCSD (vs UAB) | -0.1305 | 0.9742 | ±1.9484 | -0.134 | 0.8934 |  |
| Site: UW (vs UAB) | +1.0451 | 1.0226 | ±2.0452 | +1.022 | 0.3068 |  |
| **Age (years)** | **-0.1036** | 0.0402 | ±0.0803 | **-2.578** | **0.0099** | ** |
| BMI (kg/m2) | +0.0634 | 0.0555 | ±0.1109 | +1.143 | 0.2532 |  |
| Hypertension | -0.7864 | 0.9180 | ±1.8360 | -0.857 | 0.3916 |  |
| High cholesterol | +0.3128 | 0.7701 | ±1.5402 | +0.406 | 0.6846 |  |
| Kidney disease | +1.6996 | 1.2394 | ±2.4789 | +1.371 | 0.1703 |  |
| Circulatory disease | +0.7432 | 1.0926 | ±2.1852 | +0.680 | 0.4964 |  |
| **Avg. daily time 181-250 (%)** | **-0.1528** | 0.0760 | ±0.1521 | **-2.010** | **0.0444** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **204**, R² = **0.1499**, Adj R² = **0.1012**, F-statistic = **3.08** (p = **7.92e-04**), Residual SE = **5.196** on **192** df, AIC = **1262.9**, BIC = **1302.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4760** | 3.3610 | ±6.7220 | **+3.414** | **6.39e-04** | *** |
| **Education: graduate level (vs college)** | **-1.7641** | 0.7881 | ±1.5762 | **-2.239** | **0.0252** | * |
| Education: high school or below (vs college) | +1.4998 | 1.3851 | ±2.7701 | +1.083 | 0.2789 |  |
| Site: UCSD (vs UAB) | -0.1317 | 0.9730 | ±1.9460 | -0.135 | 0.8923 |  |
| Site: UW (vs UAB) | +1.0202 | 1.0227 | ±2.0454 | +0.998 | 0.3185 |  |
| **Age (years)** | **-0.1037** | 0.0402 | ±0.0803 | **-2.583** | **0.0098** | ** |
| BMI (kg/m2) | +0.0642 | 0.0556 | ±0.1112 | +1.155 | 0.2480 |  |
| Hypertension | -0.8002 | 0.9165 | ±1.8330 | -0.873 | 0.3826 |  |
| High cholesterol | +0.3062 | 0.7708 | ±1.5416 | +0.397 | 0.6911 |  |
| Kidney disease | +1.6920 | 1.2389 | ±2.4778 | +1.366 | 0.1720 |  |
| Circulatory disease | +0.7412 | 1.0928 | ±2.1855 | +0.678 | 0.4976 |  |
| **Time > 180 (%)** | **-0.1508** | 0.0753 | ±0.1505 | **-2.004** | **0.0450** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **204**, R² = **0.1497**, Adj R² = **0.1010**, F-statistic = **3.07** (p = **8.04e-04**), Residual SE = **5.197** on **192** df, AIC = **1263.0**, BIC = **1302.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4669** | 3.3619 | ±6.7239 | **+3.411** | **6.48e-04** | *** |
| **Education: graduate level (vs college)** | **-1.7756** | 0.7870 | ±1.5741 | **-2.256** | **0.0241** | * |
| Education: high school or below (vs college) | +1.4722 | 1.3825 | ±2.7649 | +1.065 | 0.2869 |  |
| Site: UCSD (vs UAB) | -0.1305 | 0.9742 | ±1.9484 | -0.134 | 0.8934 |  |
| Site: UW (vs UAB) | +1.0451 | 1.0226 | ±2.0452 | +1.022 | 0.3068 |  |
| **Age (years)** | **-0.1036** | 0.0402 | ±0.0803 | **-2.578** | **0.0099** | ** |
| BMI (kg/m2) | +0.0634 | 0.0555 | ±0.1109 | +1.143 | 0.2532 |  |
| Hypertension | -0.7864 | 0.9180 | ±1.8360 | -0.857 | 0.3916 |  |
| High cholesterol | +0.3128 | 0.7701 | ±1.5402 | +0.406 | 0.6846 |  |
| Kidney disease | +1.6996 | 1.2394 | ±2.4789 | +1.371 | 0.1703 |  |
| Circulatory disease | +0.7432 | 1.0926 | ±2.1852 | +0.680 | 0.4964 |  |
| **Avg. daily time > 180 (%)** | **-0.1528** | 0.0760 | ±0.1521 | **-2.010** | **0.0444** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **204**, R² = **0.1346**, Adj R² = **0.0850**, F-statistic = **2.71** (p = **0.0028**), Residual SE = **5.243** on **192** df, AIC = **1266.6**, BIC = **1306.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.4475** | 3.3749 | ±6.7499 | **+3.392** | **6.94e-04** | *** |
| **Education: graduate level (vs college)** | **-1.8224** | 0.7916 | ±1.5832 | **-2.302** | **0.0213** | * |
| Education: high school or below (vs college) | +1.4136 | 1.4136 | ±2.8271 | +1.000 | 0.3173 |  |
| Site: UCSD (vs UAB) | -0.0549 | 0.9795 | ±1.9590 | -0.056 | 0.9553 |  |
| Site: UW (vs UAB) | +1.1161 | 1.0250 | ±2.0501 | +1.089 | 0.2762 |  |
| **Age (years)** | **-0.1104** | 0.0397 | ±0.0793 | **-2.784** | **0.0054** | ** |
| BMI (kg/m2) | +0.0624 | 0.0576 | ±0.1152 | +1.084 | 0.2785 |  |
| Hypertension | -0.8869 | 0.9166 | ±1.8331 | -0.968 | 0.3332 |  |
| High cholesterol | +0.3971 | 0.7731 | ±1.5463 | +0.514 | 0.6076 |  |
| Kidney disease | +1.4450 | 1.3125 | ±2.6251 | +1.101 | 0.2709 |  |
| Circulatory disease | +0.6741 | 1.1205 | ±2.2411 | +0.602 | 0.5474 |  |
| Nocturnal time > 180 (%) | -0.0316 | 0.0892 | ±0.1785 | -0.354 | 0.7233 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 204; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0517**, LLR χ² = **11.75** (p = **0.3023**), AUC = **0.6397**, AIC = **237.5**, BIC = **274.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3393 | 1.5605 | ±3.1210 | +0.217 | 0.8279 | 1.4039 |  |
| Education: graduate level (vs college) | -0.2927 | 0.3823 | ±0.7646 | -0.766 | 0.4439 | 0.7463 |  |
| Education: high school or below (vs college) | +0.4893 | 0.4778 | ±0.9556 | +1.024 | 0.3059 | 1.6311 |  |
| Site: UCSD (vs UAB) | -0.2192 | 0.4452 | ±0.8903 | -0.492 | 0.6225 | 0.8032 |  |
| Site: UW (vs UAB) | +0.4211 | 0.4214 | ±0.8429 | +0.999 | 0.3177 | 1.5236 |  |
| Age (years) | -0.0280 | 0.0188 | ±0.0376 | -1.490 | 0.1363 | 0.9724 |  |
| BMI (kg/m2) | +0.0100 | 0.0247 | ±0.0495 | +0.406 | 0.6850 | 1.0101 |  |
| Hypertension | -0.4013 | 0.3896 | ±0.7793 | -1.030 | 0.3030 | 0.6694 |  |
| High cholesterol | +0.0404 | 0.3623 | ±0.7245 | +0.112 | 0.9111 | 1.0413 |  |
| Kidney disease | +0.6027 | 0.5045 | ±1.0090 | +1.195 | 0.2322 | 1.8270 |  |
| Circulatory disease | +0.0583 | 0.4345 | ±0.8690 | +0.134 | 0.8932 | 1.0601 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0610**, LLR χ² = **13.86** (p = **0.2408**), AUC = **0.6649**, AIC = **237.3**, BIC = **277.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.0374 | 2.4750 | ±4.9500 | +1.227 | 0.2197 | 20.8516 |  |
| Education: graduate level (vs college) | -0.3050 | 0.3852 | ±0.7704 | -0.792 | 0.4285 | 0.7371 |  |
| Education: high school or below (vs college) | +0.5300 | 0.4808 | ±0.9615 | +1.102 | 0.2703 | 1.6989 |  |
| Site: UCSD (vs UAB) | -0.2176 | 0.4463 | ±0.8926 | -0.488 | 0.6259 | 0.8045 |  |
| Site: UW (vs UAB) | +0.4463 | 0.4215 | ±0.8431 | +1.059 | 0.2898 | 1.5625 |  |
| Age (years) | -0.0276 | 0.0190 | ±0.0381 | -1.448 | 0.1476 | 0.9728 |  |
| BMI (kg/m2) | +0.0176 | 0.0254 | ±0.0507 | +0.694 | 0.4879 | 1.0178 |  |
| Hypertension | -0.3607 | 0.3888 | ±0.7776 | -0.928 | 0.3536 | 0.6972 |  |
| High cholesterol | +0.1197 | 0.3695 | ±0.7391 | +0.324 | 0.7460 | 1.1272 |  |
| Kidney disease | +0.5171 | 0.5118 | ±1.0237 | +1.010 | 0.3124 | 1.6771 |  |
| Circulatory disease | +0.1574 | 0.4393 | ±0.8787 | +0.358 | 0.7201 | 1.1705 |  |
| HbA1c (%) | -0.5128 | 0.3656 | ±0.7312 | -1.403 | 0.1607 | 0.5988 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0517**, LLR χ² = **11.75** (p = **0.3829**), AUC = **0.6394**, AIC = **239.5**, BIC = **279.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3650 | 2.2429 | ±4.4859 | +0.163 | 0.8707 | 1.4406 |  |
| Education: graduate level (vs college) | -0.2929 | 0.3825 | ±0.7650 | -0.766 | 0.4439 | 0.7461 |  |
| Education: high school or below (vs college) | +0.4885 | 0.4799 | ±0.9599 | +1.018 | 0.3087 | 1.6300 |  |
| Site: UCSD (vs UAB) | -0.2192 | 0.4452 | ±0.8903 | -0.492 | 0.6224 | 0.8031 |  |
| Site: UW (vs UAB) | +0.4209 | 0.4216 | ±0.8432 | +0.998 | 0.3181 | 1.5233 |  |
| Age (years) | -0.0280 | 0.0188 | ±0.0376 | -1.490 | 0.1363 | 0.9724 |  |
| BMI (kg/m2) | +0.0101 | 0.0249 | ±0.0497 | +0.405 | 0.6853 | 1.0101 |  |
| Hypertension | -0.4010 | 0.3901 | ±0.7802 | -1.028 | 0.3039 | 0.6696 |  |
| High cholesterol | +0.0404 | 0.3623 | ±0.7245 | +0.112 | 0.9111 | 1.0413 |  |
| Kidney disease | +0.6031 | 0.5052 | ±1.0104 | +1.194 | 0.2326 | 1.8277 |  |
| Circulatory disease | +0.0586 | 0.4348 | ±0.8696 | +0.135 | 0.8928 | 1.0603 |  |
| Mean glucose (mg/dL) | -0.0002 | 0.0132 | ±0.0264 | -0.016 | 0.9872 | 0.9998 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0517**, LLR χ² = **11.75** (p = **0.3829**), AUC = **0.6394**, AIC = **239.5**, BIC = **279.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3943 | 3.7757 | ±7.5514 | +0.104 | 0.9168 | 1.4833 |  |
| Education: graduate level (vs college) | -0.2929 | 0.3825 | ±0.7650 | -0.766 | 0.4439 | 0.7461 |  |
| Education: high school or below (vs college) | +0.4885 | 0.4799 | ±0.9599 | +1.018 | 0.3087 | 1.6300 |  |
| Site: UCSD (vs UAB) | -0.2192 | 0.4452 | ±0.8903 | -0.492 | 0.6224 | 0.8031 |  |
| Site: UW (vs UAB) | +0.4209 | 0.4216 | ±0.8432 | +0.998 | 0.3181 | 1.5233 |  |
| Age (years) | -0.0280 | 0.0188 | ±0.0376 | -1.490 | 0.1363 | 0.9724 |  |
| BMI (kg/m2) | +0.0101 | 0.0249 | ±0.0497 | +0.405 | 0.6853 | 1.0101 |  |
| Hypertension | -0.4010 | 0.3901 | ±0.7802 | -1.028 | 0.3039 | 0.6696 |  |
| High cholesterol | +0.0404 | 0.3623 | ±0.7245 | +0.112 | 0.9111 | 1.0413 |  |
| Kidney disease | +0.6031 | 0.5052 | ±1.0104 | +1.194 | 0.2326 | 1.8277 |  |
| Circulatory disease | +0.0586 | 0.4348 | ±0.8696 | +0.135 | 0.8928 | 1.0603 |  |
| GMI (%) | -0.0088 | 0.5520 | ±1.1039 | -0.016 | 0.9872 | 0.9912 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0546**, LLR χ² = **12.40** (p = **0.3343**), AUC = **0.6469**, AIC = **238.8**, BIC = **278.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8248 | 2.1256 | ±4.2512 | -0.388 | 0.6980 | 0.4383 |  |
| Education: graduate level (vs college) | -0.2940 | 0.3832 | ±0.7664 | -0.767 | 0.4429 | 0.7453 |  |
| Education: high school or below (vs college) | +0.5136 | 0.4787 | ±0.9574 | +1.073 | 0.2833 | 1.6713 |  |
| Site: UCSD (vs UAB) | -0.2164 | 0.4463 | ±0.8927 | -0.485 | 0.6279 | 0.8055 |  |
| Site: UW (vs UAB) | +0.4273 | 0.4216 | ±0.8432 | +1.014 | 0.3108 | 1.5331 |  |
| Age (years) | -0.0271 | 0.0188 | ±0.0377 | -1.438 | 0.1504 | 0.9733 |  |
| BMI (kg/m2) | +0.0074 | 0.0250 | ±0.0499 | +0.297 | 0.7664 | 1.0074 |  |
| Hypertension | -0.4020 | 0.3898 | ±0.7796 | -1.031 | 0.3023 | 0.6690 |  |
| High cholesterol | +0.0317 | 0.3629 | ±0.7258 | +0.087 | 0.9303 | 1.0322 |  |
| Kidney disease | +0.6048 | 0.5033 | ±1.0067 | +1.202 | 0.2295 | 1.8309 |  |
| Circulatory disease | +0.0328 | 0.4365 | ±0.8730 | +0.075 | 0.9401 | 1.0334 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0094 | 0.0116 | ±0.0232 | +0.807 | 0.4198 | 1.0094 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0519**, LLR χ² = **11.80** (p = **0.3792**), AUC = **0.6388**, AIC = **239.4**, BIC = **279.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.5012 | 1.7272 | ±3.4543 | +0.290 | 0.7717 | 1.6507 |  |
| Education: graduate level (vs college) | -0.2891 | 0.3827 | ±0.7653 | -0.756 | 0.4499 | 0.7489 |  |
| Education: high school or below (vs college) | +0.5063 | 0.4846 | ±0.9693 | +1.045 | 0.2962 | 1.6591 |  |
| Site: UCSD (vs UAB) | -0.2264 | 0.4467 | ±0.8934 | -0.507 | 0.6124 | 0.7974 |  |
| Site: UW (vs UAB) | +0.4078 | 0.4259 | ±0.8518 | +0.957 | 0.3383 | 1.5035 |  |
| Age (years) | -0.0277 | 0.0189 | ±0.0377 | -1.471 | 0.1414 | 0.9726 |  |
| BMI (kg/m2) | +0.0101 | 0.0248 | ±0.0495 | +0.407 | 0.6840 | 1.0101 |  |
| Hypertension | -0.3907 | 0.3927 | ±0.7854 | -0.995 | 0.3197 | 0.6766 |  |
| High cholesterol | +0.0380 | 0.3626 | ±0.7253 | +0.105 | 0.9166 | 1.0387 |  |
| Kidney disease | +0.6179 | 0.5101 | ±1.0202 | +1.211 | 0.2258 | 1.8550 |  |
| Circulatory disease | +0.0653 | 0.4359 | ±0.8718 | +0.150 | 0.8808 | 1.0675 |  |
| Glucose SD, pooled (mg/dL) | -0.0085 | 0.0389 | ±0.0778 | -0.219 | 0.8268 | 0.9915 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0518**, LLR χ² = **11.76** (p = **0.3818**), AUC = **0.6394**, AIC = **239.4**, BIC = **279.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.4197 | 1.6966 | ±3.3932 | +0.247 | 0.8046 | 1.5214 |  |
| Education: graduate level (vs college) | -0.2910 | 0.3826 | ±0.7651 | -0.761 | 0.4468 | 0.7475 |  |
| Education: high school or below (vs college) | +0.4965 | 0.4818 | ±0.9636 | +1.031 | 0.3027 | 1.6430 |  |
| Site: UCSD (vs UAB) | -0.2203 | 0.4454 | ±0.8909 | -0.495 | 0.6209 | 0.8023 |  |
| Site: UW (vs UAB) | +0.4162 | 0.4234 | ±0.8469 | +0.983 | 0.3256 | 1.5162 |  |
| Age (years) | -0.0279 | 0.0189 | ±0.0377 | -1.477 | 0.1397 | 0.9725 |  |
| BMI (kg/m2) | +0.0101 | 0.0248 | ±0.0495 | +0.407 | 0.6838 | 1.0101 |  |
| Hypertension | -0.3936 | 0.3949 | ±0.7897 | -0.997 | 0.3188 | 0.6746 |  |
| High cholesterol | +0.0388 | 0.3626 | ±0.7253 | +0.107 | 0.9148 | 1.0395 |  |
| Kidney disease | +0.6082 | 0.5070 | ±1.0139 | +1.200 | 0.2303 | 1.8371 |  |
| Circulatory disease | +0.0598 | 0.4348 | ±0.8696 | +0.138 | 0.8905 | 1.0617 |  |
| Avg. daily SD (mg/dL) | -0.0048 | 0.0395 | ±0.0789 | -0.121 | 0.9039 | 0.9952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0519**, LLR χ² = **11.80** (p = **0.3786**), AUC = **0.6391**, AIC = **239.4**, BIC = **279.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.5541 | 1.8068 | ±3.6136 | +0.307 | 0.7591 | 1.7403 |  |
| Education: graduate level (vs college) | -0.2869 | 0.3831 | ±0.7663 | -0.749 | 0.4540 | 0.7506 |  |
| Education: high school or below (vs college) | +0.5179 | 0.4933 | ±0.9866 | +1.050 | 0.2938 | 1.6785 |  |
| Site: UCSD (vs UAB) | -0.2274 | 0.4470 | ±0.8939 | -0.509 | 0.6109 | 0.7966 |  |
| Site: UW (vs UAB) | +0.4057 | 0.4263 | ±0.8526 | +0.952 | 0.3412 | 1.5004 |  |
| Age (years) | -0.0276 | 0.0189 | ±0.0378 | -1.463 | 0.1434 | 0.9727 |  |
| BMI (kg/m2) | +0.0097 | 0.0248 | ±0.0496 | +0.392 | 0.6948 | 1.0098 |  |
| Hypertension | -0.3898 | 0.3927 | ±0.7854 | -0.993 | 0.3209 | 0.6772 |  |
| High cholesterol | +0.0375 | 0.3627 | ±0.7253 | +0.103 | 0.9176 | 1.0382 |  |
| Kidney disease | +0.6191 | 0.5098 | ±1.0196 | +1.214 | 0.2246 | 1.8572 |  |
| Circulatory disease | +0.0645 | 0.4356 | ±0.8713 | +0.148 | 0.8823 | 1.0666 |  |
| CV (%) | -0.0138 | 0.0583 | ±0.1167 | -0.236 | 0.8135 | 0.9863 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0520**, LLR χ² = **11.81** (p = **0.3781**), AUC = **0.6403**, AIC = **239.4**, BIC = **279.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.6025 | 1.8816 | ±3.7632 | +0.320 | 0.7488 | 1.8267 |  |
| Education: graduate level (vs college) | -0.2984 | 0.3830 | ±0.7660 | -0.779 | 0.4359 | 0.7420 |  |
| Education: high school or below (vs college) | +0.4627 | 0.4892 | ±0.9785 | +0.946 | 0.3442 | 1.5884 |  |
| Site: UCSD (vs UAB) | -0.2130 | 0.4455 | ±0.8909 | -0.478 | 0.6325 | 0.8081 |  |
| Site: UW (vs UAB) | +0.4359 | 0.4257 | ±0.8513 | +1.024 | 0.3058 | 1.5464 |  |
| Age (years) | -0.0285 | 0.0189 | ±0.0378 | -1.507 | 0.1318 | 0.9719 |  |
| BMI (kg/m2) | +0.0101 | 0.0247 | ±0.0495 | +0.408 | 0.6830 | 1.0102 |  |
| Hypertension | -0.4140 | 0.3929 | ±0.7858 | -1.054 | 0.2920 | 0.6610 |  |
| High cholesterol | +0.0417 | 0.3622 | ±0.7244 | +0.115 | 0.9084 | 1.0426 |  |
| Kidney disease | +0.5866 | 0.5082 | ±1.0165 | +1.154 | 0.2484 | 1.7979 |  |
| Circulatory disease | +0.0538 | 0.4348 | ±0.8696 | +0.124 | 0.9014 | 1.0553 |  |
| Mean / SD ratio | -0.0379 | 0.1515 | ±0.3031 | -0.250 | 0.8027 | 0.9628 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0522**, LLR χ² = **11.86** (p = **0.3741**), AUC = **0.6391**, AIC = **239.3**, BIC = **279.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.6606 | 1.8273 | ±3.6545 | +0.362 | 0.7177 | 1.9359 |  |
| Education: graduate level (vs college) | -0.2969 | 0.3825 | ±0.7650 | -0.776 | 0.4376 | 0.7431 |  |
| Education: high school or below (vs college) | +0.4635 | 0.4838 | ±0.9676 | +0.958 | 0.3380 | 1.5897 |  |
| Site: UCSD (vs UAB) | -0.2218 | 0.4448 | ±0.8896 | -0.499 | 0.6180 | 0.8011 |  |
| Site: UW (vs UAB) | +0.4346 | 0.4233 | ±0.8466 | +1.027 | 0.3045 | 1.5444 |  |
| Age (years) | -0.0286 | 0.0189 | ±0.0378 | -1.517 | 0.1293 | 0.9718 |  |
| BMI (kg/m2) | +0.0100 | 0.0247 | ±0.0495 | +0.403 | 0.6873 | 1.0100 |  |
| Hypertension | -0.4248 | 0.3957 | ±0.7913 | -1.074 | 0.2830 | 0.6539 |  |
| High cholesterol | +0.0400 | 0.3622 | ±0.7244 | +0.110 | 0.9120 | 1.0408 |  |
| Kidney disease | +0.5883 | 0.5060 | ±1.0120 | +1.163 | 0.2450 | 1.8010 |  |
| Circulatory disease | +0.0625 | 0.4346 | ±0.8692 | +0.144 | 0.8856 | 1.0645 |  |
| Avg. daily mean/SD | -0.0385 | 0.1148 | ±0.2295 | -0.336 | 0.7369 | 0.9622 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0972**, LLR χ² = **22.09** (p = **0.0237**), AUC = **0.6977**, AIC = **229.1**, BIC = **268.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.6974 | 1.9043 | ±3.8087 | -1.416 | 0.1566 | 0.0674 |  |
| Education: graduate level (vs college) | -0.3542 | 0.3961 | ±0.7921 | -0.894 | 0.3712 | 0.7018 |  |
| Education: high school or below (vs college) | +0.4185 | 0.4946 | ±0.9893 | +0.846 | 0.3975 | 1.5197 |  |
| Site: UCSD (vs UAB) | -0.1799 | 0.4567 | ±0.9134 | -0.394 | 0.6936 | 0.8353 |  |
| Site: UW (vs UAB) | +0.5325 | 0.4363 | ±0.8727 | +1.220 | 0.2223 | 1.7032 |  |
| Age (years) | -0.0277 | 0.0193 | ±0.0386 | -1.435 | 0.1513 | 0.9727 |  |
| BMI (kg/m2) | +0.0048 | 0.0259 | ±0.0518 | +0.185 | 0.8530 | 1.0048 |  |
| Hypertension | -0.4682 | 0.3985 | ±0.7971 | -1.175 | 0.2401 | 0.6261 |  |
| High cholesterol | -0.0273 | 0.3750 | ±0.7499 | -0.073 | 0.9419 | 0.9730 |  |
| Kidney disease | +0.6626 | 0.5155 | ±1.0310 | +1.285 | 0.1987 | 1.9397 |  |
| Circulatory disease | +0.0949 | 0.4493 | ±0.8987 | +0.211 | 0.8327 | 1.0995 |  |
| **MAG (mg/dL/h)** | **+0.0871** | 0.0283 | ±0.0566 | **+3.077** | **0.0021** | 1.0910 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0533**, LLR χ² = **12.10** (p = **0.3560**), AUC = **0.6436**, AIC = **239.1**, BIC = **278.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1898 | 1.7982 | ±3.5964 | -0.106 | 0.9160 | 0.8272 |  |
| Education: graduate level (vs college) | -0.2973 | 0.3827 | ±0.7654 | -0.777 | 0.4373 | 0.7429 |  |
| Education: high school or below (vs college) | +0.4622 | 0.4795 | ±0.9591 | +0.964 | 0.3351 | 1.5876 |  |
| Site: UCSD (vs UAB) | -0.2091 | 0.4453 | ±0.8907 | -0.469 | 0.6387 | 0.8113 |  |
| Site: UW (vs UAB) | +0.4437 | 0.4232 | ±0.8465 | +1.048 | 0.2945 | 1.5584 |  |
| Age (years) | -0.0288 | 0.0188 | ±0.0376 | -1.531 | 0.1258 | 0.9716 |  |
| BMI (kg/m2) | +0.0107 | 0.0247 | ±0.0494 | +0.433 | 0.6650 | 1.0108 |  |
| Hypertension | -0.4306 | 0.3931 | ±0.7862 | -1.095 | 0.2734 | 0.6501 |  |
| High cholesterol | +0.0427 | 0.3624 | ±0.7247 | +0.118 | 0.9061 | 1.0436 |  |
| Kidney disease | +0.5876 | 0.5040 | ±1.0081 | +1.166 | 0.2437 | 1.7997 |  |
| Circulatory disease | +0.0545 | 0.4349 | ±0.8698 | +0.125 | 0.9003 | 1.0560 |  |
| Avg. daily range (mg/dL) | +0.0059 | 0.0099 | ±0.0197 | +0.594 | 0.5525 | 1.0059 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0517**, LLR χ² = **11.75** (p = **0.3828**), AUC = **0.6404**, AIC = **239.5**, BIC = **279.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3541 | 1.6295 | ±3.2590 | +0.217 | 0.8280 | 1.4249 |  |
| Education: graduate level (vs college) | -0.2925 | 0.3823 | ±0.7646 | -0.765 | 0.4442 | 0.7464 |  |
| Education: high school or below (vs college) | +0.4923 | 0.4873 | ±0.9747 | +1.010 | 0.3124 | 1.6361 |  |
| Site: UCSD (vs UAB) | -0.2215 | 0.4514 | ±0.9028 | -0.491 | 0.6236 | 0.8013 |  |
| Site: UW (vs UAB) | +0.4186 | 0.4285 | ±0.8570 | +0.977 | 0.3286 | 1.5199 |  |
| Age (years) | -0.0280 | 0.0188 | ±0.0376 | -1.488 | 0.1367 | 0.9724 |  |
| BMI (kg/m2) | +0.0100 | 0.0248 | ±0.0495 | +0.405 | 0.6853 | 1.0101 |  |
| Hypertension | -0.4027 | 0.3919 | ±0.7837 | -1.028 | 0.3042 | 0.6685 |  |
| High cholesterol | +0.0409 | 0.3625 | ±0.7250 | +0.113 | 0.9102 | 1.0417 |  |
| Kidney disease | +0.6058 | 0.5141 | ±1.0281 | +1.178 | 0.2386 | 1.8327 |  |
| Circulatory disease | +0.0616 | 0.4469 | ±0.8938 | +0.138 | 0.8903 | 1.0636 |  |
| SD of daily means (mg/dL) | -0.0023 | 0.0711 | ±0.1422 | -0.032 | 0.9747 | 0.9978 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0606**, LLR χ² = **13.76** (p = **0.2466**), AUC = **0.6501**, AIC = **237.5**, BIC = **277.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -5.3007 | 4.4830 | ±8.9659 | -1.182 | 0.2370 | 0.0050 |  |
| Education: graduate level (vs college) | -0.2835 | 0.3842 | ±0.7684 | -0.738 | 0.4605 | 0.7531 |  |
| Education: high school or below (vs college) | +0.5278 | 0.4855 | ±0.9709 | +1.087 | 0.2769 | 1.6953 |  |
| Site: UCSD (vs UAB) | -0.2809 | 0.4513 | ±0.9026 | -0.622 | 0.5337 | 0.7551 |  |
| Site: UW (vs UAB) | +0.3635 | 0.4284 | ±0.8568 | +0.849 | 0.3961 | 1.4384 |  |
| Age (years) | -0.0254 | 0.0190 | ±0.0381 | -1.332 | 0.1828 | 0.9749 |  |
| BMI (kg/m2) | +0.0119 | 0.0249 | ±0.0499 | +0.476 | 0.6338 | 1.0120 |  |
| Hypertension | -0.3967 | 0.3935 | ±0.7870 | -1.008 | 0.3134 | 0.6725 |  |
| High cholesterol | +0.0368 | 0.3656 | ±0.7311 | +0.101 | 0.9198 | 1.0375 |  |
| Kidney disease | +0.6759 | 0.5165 | ±1.0331 | +1.308 | 0.1907 | 1.9657 |  |
| Circulatory disease | +0.0869 | 0.4384 | ±0.8768 | +0.198 | 0.8429 | 1.0908 |  |
| Time in range 70-180, pooled (%) | +0.0565 | 0.0424 | ±0.0847 | +1.335 | 0.1819 | 1.0582 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0614**, LLR χ² = **13.95** (p = **0.2359**), AUC = **0.6518**, AIC = **237.3**, BIC = **277.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -5.7016 | 4.5909 | ±9.1818 | -1.242 | 0.2143 | 0.0033 |  |
| Education: graduate level (vs college) | -0.2876 | 0.3845 | ±0.7690 | -0.748 | 0.4545 | 0.7501 |  |
| Education: high school or below (vs college) | +0.5224 | 0.4856 | ±0.9711 | +1.076 | 0.2820 | 1.6860 |  |
| Site: UCSD (vs UAB) | -0.2792 | 0.4512 | ±0.9025 | -0.619 | 0.5361 | 0.7564 |  |
| Site: UW (vs UAB) | +0.3711 | 0.4285 | ±0.8570 | +0.866 | 0.3865 | 1.4493 |  |
| Age (years) | -0.0251 | 0.0191 | ±0.0381 | -1.320 | 0.1869 | 0.9752 |  |
| BMI (kg/m2) | +0.0118 | 0.0249 | ±0.0499 | +0.474 | 0.6357 | 1.0119 |  |
| Hypertension | -0.3909 | 0.3939 | ±0.7878 | -0.992 | 0.3210 | 0.6765 |  |
| High cholesterol | +0.0377 | 0.3658 | ±0.7316 | +0.103 | 0.9178 | 1.0385 |  |
| Kidney disease | +0.6812 | 0.5175 | ±1.0351 | +1.316 | 0.1881 | 1.9762 |  |
| Circulatory disease | +0.0904 | 0.4386 | ±0.8772 | +0.206 | 0.8368 | 1.0946 |  |
| Avg. daily time in range 70-180 (%) | +0.0604 | 0.0434 | ±0.0868 | +1.393 | 0.1637 | 1.0623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0567**, LLR χ² = **12.89** (p = **0.3004**), AUC = **0.6435**, AIC = **238.3**, BIC = **278.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3229 | 1.5738 | ±3.1476 | +0.205 | 0.8374 | 1.3811 |  |
| Education: graduate level (vs college) | -0.2748 | 0.3836 | ±0.7672 | -0.716 | 0.4737 | 0.7597 |  |
| Education: high school or below (vs college) | +0.5729 | 0.4856 | ±0.9712 | +1.180 | 0.2380 | 1.7735 |  |
| Site: UCSD (vs UAB) | -0.2533 | 0.4484 | ±0.8969 | -0.565 | 0.5721 | 0.7762 |  |
| Site: UW (vs UAB) | +0.3846 | 0.4243 | ±0.8487 | +0.906 | 0.3648 | 1.4690 |  |
| Age (years) | -0.0255 | 0.0191 | ±0.0381 | -1.340 | 0.1801 | 0.9748 |  |
| BMI (kg/m2) | +0.0084 | 0.0249 | ±0.0497 | +0.337 | 0.7361 | 1.0084 |  |
| Hypertension | -0.4180 | 0.3922 | ±0.7845 | -1.066 | 0.2865 | 0.6583 |  |
| High cholesterol | +0.0686 | 0.3630 | ±0.7260 | +0.189 | 0.8502 | 1.0710 |  |
| Kidney disease | +0.5876 | 0.5062 | ±1.0124 | +1.161 | 0.2458 | 1.7996 |  |
| Circulatory disease | +0.0934 | 0.4386 | ±0.8771 | +0.213 | 0.8313 | 1.0979 |  |
| Time 54-69, pooled (%) | -0.8187 | 0.8522 | ±1.7044 | -0.961 | 0.3367 | 0.4410 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0577**, LLR χ² = **13.12** (p = **0.2859**), AUC = **0.6453**, AIC = **238.1**, BIC = **277.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3185 | 1.5771 | ±3.1541 | +0.202 | 0.8399 | 1.3751 |  |
| Education: graduate level (vs college) | -0.2791 | 0.3840 | ±0.7680 | -0.727 | 0.4674 | 0.7565 |  |
| Education: high school or below (vs college) | +0.5806 | 0.4857 | ±0.9714 | +1.195 | 0.2319 | 1.7872 |  |
| Site: UCSD (vs UAB) | -0.2326 | 0.4474 | ±0.8949 | -0.520 | 0.6032 | 0.7925 |  |
| Site: UW (vs UAB) | +0.3943 | 0.4237 | ±0.8474 | +0.931 | 0.3520 | 1.4833 |  |
| Age (years) | -0.0254 | 0.0191 | ±0.0381 | -1.334 | 0.1821 | 0.9749 |  |
| BMI (kg/m2) | +0.0081 | 0.0249 | ±0.0498 | +0.324 | 0.7457 | 1.0081 |  |
| Hypertension | -0.4128 | 0.3920 | ±0.7840 | -1.053 | 0.2924 | 0.6618 |  |
| High cholesterol | +0.0654 | 0.3628 | ±0.7255 | +0.180 | 0.8568 | 1.0676 |  |
| Kidney disease | +0.5751 | 0.5064 | ±1.0128 | +1.136 | 0.2561 | 1.7773 |  |
| Circulatory disease | +0.0825 | 0.4388 | ±0.8776 | +0.188 | 0.8509 | 1.0860 |  |
| Avg. daily time 54-69 (%) | -0.9362 | 0.9101 | ±1.8202 | -1.029 | 0.3036 | 0.3921 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0567**, LLR χ² = **12.89** (p = **0.3004**), AUC = **0.6435**, AIC = **238.3**, BIC = **278.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3229 | 1.5738 | ±3.1476 | +0.205 | 0.8374 | 1.3811 |  |
| Education: graduate level (vs college) | -0.2748 | 0.3836 | ±0.7672 | -0.716 | 0.4737 | 0.7597 |  |
| Education: high school or below (vs college) | +0.5729 | 0.4856 | ±0.9712 | +1.180 | 0.2380 | 1.7735 |  |
| Site: UCSD (vs UAB) | -0.2533 | 0.4484 | ±0.8969 | -0.565 | 0.5721 | 0.7762 |  |
| Site: UW (vs UAB) | +0.3846 | 0.4243 | ±0.8487 | +0.906 | 0.3648 | 1.4690 |  |
| Age (years) | -0.0255 | 0.0191 | ±0.0381 | -1.340 | 0.1801 | 0.9748 |  |
| BMI (kg/m2) | +0.0084 | 0.0249 | ±0.0497 | +0.337 | 0.7361 | 1.0084 |  |
| Hypertension | -0.4180 | 0.3922 | ±0.7845 | -1.066 | 0.2865 | 0.6583 |  |
| High cholesterol | +0.0686 | 0.3630 | ±0.7260 | +0.189 | 0.8502 | 1.0710 |  |
| Kidney disease | +0.5876 | 0.5062 | ±1.0124 | +1.161 | 0.2458 | 1.7996 |  |
| Circulatory disease | +0.0934 | 0.4386 | ±0.8771 | +0.213 | 0.8313 | 1.0979 |  |
| Time < 70 (%) | -0.8187 | 0.8522 | ±1.7044 | -0.961 | 0.3367 | 0.4410 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0577**, LLR χ² = **13.12** (p = **0.2859**), AUC = **0.6453**, AIC = **238.1**, BIC = **277.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3185 | 1.5771 | ±3.1541 | +0.202 | 0.8399 | 1.3751 |  |
| Education: graduate level (vs college) | -0.2791 | 0.3840 | ±0.7680 | -0.727 | 0.4674 | 0.7565 |  |
| Education: high school or below (vs college) | +0.5806 | 0.4857 | ±0.9714 | +1.195 | 0.2319 | 1.7872 |  |
| Site: UCSD (vs UAB) | -0.2326 | 0.4474 | ±0.8949 | -0.520 | 0.6032 | 0.7925 |  |
| Site: UW (vs UAB) | +0.3943 | 0.4237 | ±0.8474 | +0.931 | 0.3520 | 1.4833 |  |
| Age (years) | -0.0254 | 0.0191 | ±0.0381 | -1.334 | 0.1821 | 0.9749 |  |
| BMI (kg/m2) | +0.0081 | 0.0249 | ±0.0498 | +0.324 | 0.7457 | 1.0081 |  |
| Hypertension | -0.4128 | 0.3920 | ±0.7840 | -1.053 | 0.2924 | 0.6618 |  |
| High cholesterol | +0.0654 | 0.3628 | ±0.7255 | +0.180 | 0.8568 | 1.0676 |  |
| Kidney disease | +0.5751 | 0.5064 | ±1.0128 | +1.136 | 0.2561 | 1.7773 |  |
| Circulatory disease | +0.0825 | 0.4388 | ±0.8776 | +0.188 | 0.8509 | 1.0860 |  |
| Avg. daily time < 70 (%) | -0.9362 | 0.9101 | ±1.8202 | -1.029 | 0.3036 | 0.3921 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0597**, LLR χ² = **13.56** (p = **0.2583**), AUC = **0.6500**, AIC = **237.6**, BIC = **277.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3557 | 1.5712 | ±3.1424 | +0.226 | 0.8209 | 1.4271 |  |
| Education: graduate level (vs college) | -0.2865 | 0.3840 | ±0.7679 | -0.746 | 0.4555 | 0.7509 |  |
| Education: high school or below (vs college) | +0.5192 | 0.4847 | ±0.9694 | +1.071 | 0.2840 | 1.6807 |  |
| Site: UCSD (vs UAB) | -0.2749 | 0.4507 | ±0.9014 | -0.610 | 0.5419 | 0.7597 |  |
| Site: UW (vs UAB) | +0.3690 | 0.4278 | ±0.8555 | +0.863 | 0.3883 | 1.4463 |  |
| Age (years) | -0.0257 | 0.0190 | ±0.0380 | -1.354 | 0.1757 | 0.9746 |  |
| BMI (kg/m2) | +0.0119 | 0.0249 | ±0.0499 | +0.477 | 0.6331 | 1.0120 |  |
| Hypertension | -0.3966 | 0.3931 | ±0.7863 | -1.009 | 0.3131 | 0.6726 |  |
| High cholesterol | +0.0346 | 0.3653 | ±0.7307 | +0.095 | 0.9246 | 1.0352 |  |
| Kidney disease | +0.6739 | 0.5159 | ±1.0319 | +1.306 | 0.1915 | 1.9618 |  |
| Circulatory disease | +0.0820 | 0.4379 | ±0.8758 | +0.187 | 0.8515 | 1.0854 |  |
| Time 181-250, pooled (%) | -0.0529 | 0.0416 | ±0.0832 | -1.272 | 0.2033 | 0.9484 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0604**, LLR χ² = **13.71** (p = **0.2493**), AUC = **0.6504**, AIC = **237.5**, BIC = **277.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3472 | 1.5696 | ±3.1392 | +0.221 | 0.8249 | 1.4151 |  |
| Education: graduate level (vs college) | -0.2903 | 0.3842 | ±0.7685 | -0.756 | 0.4499 | 0.7480 |  |
| Education: high school or below (vs college) | +0.5139 | 0.4848 | ±0.9695 | +1.060 | 0.2891 | 1.6717 |  |
| Site: UCSD (vs UAB) | -0.2745 | 0.4508 | ±0.9015 | -0.609 | 0.5425 | 0.7599 |  |
| Site: UW (vs UAB) | +0.3755 | 0.4279 | ±0.8557 | +0.878 | 0.3801 | 1.4558 |  |
| Age (years) | -0.0256 | 0.0190 | ±0.0380 | -1.346 | 0.1784 | 0.9747 |  |
| BMI (kg/m2) | +0.0118 | 0.0249 | ±0.0499 | +0.475 | 0.6350 | 1.0119 |  |
| Hypertension | -0.3917 | 0.3934 | ±0.7869 | -0.996 | 0.3195 | 0.6759 |  |
| High cholesterol | +0.0355 | 0.3656 | ±0.7311 | +0.097 | 0.9226 | 1.0362 |  |
| Kidney disease | +0.6791 | 0.5169 | ±1.0337 | +1.314 | 0.1889 | 1.9721 |  |
| Circulatory disease | +0.0858 | 0.4380 | ±0.8760 | +0.196 | 0.8448 | 1.0895 |  |
| Avg. daily time 181-250 (%) | -0.0561 | 0.0425 | ±0.0849 | -1.322 | 0.1860 | 0.9454 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0597**, LLR χ² = **13.56** (p = **0.2583**), AUC = **0.6500**, AIC = **237.6**, BIC = **277.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3557 | 1.5712 | ±3.1424 | +0.226 | 0.8209 | 1.4271 |  |
| Education: graduate level (vs college) | -0.2865 | 0.3840 | ±0.7679 | -0.746 | 0.4555 | 0.7509 |  |
| Education: high school or below (vs college) | +0.5192 | 0.4847 | ±0.9694 | +1.071 | 0.2840 | 1.6807 |  |
| Site: UCSD (vs UAB) | -0.2749 | 0.4507 | ±0.9014 | -0.610 | 0.5419 | 0.7597 |  |
| Site: UW (vs UAB) | +0.3690 | 0.4278 | ±0.8555 | +0.863 | 0.3883 | 1.4463 |  |
| Age (years) | -0.0257 | 0.0190 | ±0.0380 | -1.354 | 0.1757 | 0.9746 |  |
| BMI (kg/m2) | +0.0119 | 0.0249 | ±0.0499 | +0.477 | 0.6331 | 1.0120 |  |
| Hypertension | -0.3966 | 0.3931 | ±0.7863 | -1.009 | 0.3131 | 0.6726 |  |
| High cholesterol | +0.0346 | 0.3653 | ±0.7307 | +0.095 | 0.9246 | 1.0352 |  |
| Kidney disease | +0.6739 | 0.5159 | ±1.0319 | +1.306 | 0.1915 | 1.9618 |  |
| Circulatory disease | +0.0820 | 0.4379 | ±0.8758 | +0.187 | 0.8515 | 1.0854 |  |
| Time > 180 (%) | -0.0529 | 0.0416 | ±0.0832 | -1.272 | 0.2033 | 0.9484 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0604**, LLR χ² = **13.71** (p = **0.2493**), AUC = **0.6504**, AIC = **237.5**, BIC = **277.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3472 | 1.5696 | ±3.1392 | +0.221 | 0.8249 | 1.4151 |  |
| Education: graduate level (vs college) | -0.2903 | 0.3842 | ±0.7685 | -0.756 | 0.4499 | 0.7480 |  |
| Education: high school or below (vs college) | +0.5139 | 0.4848 | ±0.9695 | +1.060 | 0.2891 | 1.6717 |  |
| Site: UCSD (vs UAB) | -0.2745 | 0.4508 | ±0.9015 | -0.609 | 0.5425 | 0.7599 |  |
| Site: UW (vs UAB) | +0.3755 | 0.4279 | ±0.8557 | +0.878 | 0.3801 | 1.4558 |  |
| Age (years) | -0.0256 | 0.0190 | ±0.0380 | -1.346 | 0.1784 | 0.9747 |  |
| BMI (kg/m2) | +0.0118 | 0.0249 | ±0.0499 | +0.475 | 0.6350 | 1.0119 |  |
| Hypertension | -0.3917 | 0.3934 | ±0.7869 | -0.996 | 0.3195 | 0.6759 |  |
| High cholesterol | +0.0355 | 0.3656 | ±0.7311 | +0.097 | 0.9226 | 1.0362 |  |
| Kidney disease | +0.6791 | 0.5169 | ±1.0337 | +1.314 | 0.1889 | 1.9721 |  |
| Circulatory disease | +0.0858 | 0.4380 | ±0.8760 | +0.196 | 0.8448 | 1.0895 |  |
| Avg. daily time > 180 (%) | -0.0561 | 0.0425 | ±0.0849 | -1.322 | 0.1860 | 0.9454 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 204)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **204**, events = **50**, McFadden pseudo-R² = **0.0521**, LLR χ² = **11.84** (p = **0.3754**), AUC = **0.6405**, AIC = **239.4**, BIC = **279.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3285 | 1.5615 | ±3.1231 | +0.210 | 0.8334 | 1.3889 |  |
| Education: graduate level (vs college) | -0.2938 | 0.3823 | ±0.7646 | -0.769 | 0.4421 | 0.7454 |  |
| Education: high school or below (vs college) | +0.5080 | 0.4824 | ±0.9648 | +1.053 | 0.2923 | 1.6620 |  |
| Site: UCSD (vs UAB) | -0.2433 | 0.4522 | ±0.9044 | -0.538 | 0.5906 | 0.7840 |  |
| Site: UW (vs UAB) | +0.4003 | 0.4268 | ±0.8536 | +0.938 | 0.3483 | 1.4922 |  |
| Age (years) | -0.0276 | 0.0189 | ±0.0377 | -1.466 | 0.1425 | 0.9727 |  |
| BMI (kg/m2) | +0.0110 | 0.0250 | ±0.0499 | +0.442 | 0.6585 | 1.0111 |  |
| Hypertension | -0.4186 | 0.3940 | ±0.7881 | -1.062 | 0.2880 | 0.6579 |  |
| High cholesterol | +0.0451 | 0.3627 | ±0.7253 | +0.124 | 0.9011 | 1.0461 |  |
| Kidney disease | +0.6227 | 0.5096 | ±1.0193 | +1.222 | 0.2218 | 1.8639 |  |
| Circulatory disease | +0.0681 | 0.4359 | ±0.8718 | +0.156 | 0.8758 | 1.0705 |  |
| Nocturnal time > 180 (%) | -0.0102 | 0.0331 | ±0.0661 | -0.308 | 0.7578 | 0.9899 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 198; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **198**, R² = **0.1493**, Adj R² = **0.0891**, F-statistic = **2.48** (p = **0.0038**), Residual SE = **0.836** on **184** df, AIC = **504.4**, BIC = **550.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7859** | 0.5826 | ±1.1651 | **+3.066** | **0.0022** | ** |
| **Education: graduate level (vs college)** | **-0.2419** | 0.1222 | ±0.2443 | **-1.980** | **0.0477** | * |
| **Education: high school or below (vs college)** | **+0.4842** | 0.2466 | ±0.4931 | **+1.964** | **0.0496** | * |
| Site: UCSD (vs UAB) | +0.1612 | 0.1639 | ±0.3277 | +0.984 | 0.3252 |  |
| Site: UW (vs UAB) | -0.0740 | 0.1579 | ±0.3157 | -0.469 | 0.6393 |  |
| Season: spring (vs autumn) | +0.0746 | 0.1737 | ±0.3475 | +0.429 | 0.6676 |  |
| Season: summer (vs autumn) | +0.0553 | 0.1658 | ±0.3315 | +0.334 | 0.7388 |  |
| Season: winter (vs autumn) | +0.0259 | 0.1502 | ±0.3004 | +0.173 | 0.8630 |  |
| Age (years) | -0.0084 | 0.0067 | ±0.0134 | -1.264 | 0.2064 |  |
| BMI (kg/m2) | +0.0192 | 0.0106 | ±0.0211 | +1.815 | 0.0695 | . |
| Hypertension | +0.1426 | 0.1418 | ±0.2836 | +1.006 | 0.3144 |  |
| High cholesterol | -0.0802 | 0.1253 | ±0.2506 | -0.640 | 0.5219 |  |
| Kidney disease | -0.0778 | 0.1869 | ±0.3737 | -0.417 | 0.6770 |  |
| Circulatory disease | -0.0159 | 0.1670 | ±0.3340 | -0.095 | 0.9241 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **198**, R² = **0.1495**, Adj R² = **0.0845**, F-statistic = **2.30** (p = **0.0063**), Residual SE = **0.838** on **183** df, AIC = **506.3**, BIC = **555.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6261** | 0.7716 | ±1.5431 | **+2.108** | **0.0351** | * |
| Education: graduate level (vs college) | -0.2408 | 0.1231 | ±0.2462 | -1.956 | 0.0505 | . |
| Education: high school or below (vs college) | +0.4829 | 0.2464 | ±0.4928 | +1.960 | 0.0500 | . |
| Site: UCSD (vs UAB) | +0.1615 | 0.1643 | ±0.3287 | +0.983 | 0.3257 |  |
| Site: UW (vs UAB) | -0.0735 | 0.1584 | ±0.3167 | -0.464 | 0.6427 |  |
| Season: spring (vs autumn) | +0.0755 | 0.1742 | ±0.3483 | +0.434 | 0.6645 |  |
| Season: summer (vs autumn) | +0.0516 | 0.1663 | ±0.3325 | +0.311 | 0.7561 |  |
| Season: winter (vs autumn) | +0.0237 | 0.1510 | ±0.3021 | +0.157 | 0.8754 |  |
| Age (years) | -0.0085 | 0.0067 | ±0.0134 | -1.268 | 0.2048 |  |
| BMI (kg/m2) | +0.0187 | 0.0111 | ±0.0221 | +1.691 | 0.0909 | . |
| Hypertension | +0.1417 | 0.1425 | ±0.2850 | +0.994 | 0.3202 |  |
| High cholesterol | -0.0833 | 0.1256 | ±0.2512 | -0.663 | 0.5071 |  |
| Kidney disease | -0.0732 | 0.1866 | ±0.3732 | -0.392 | 0.6949 |  |
| Circulatory disease | -0.0225 | 0.1707 | ±0.3413 | -0.132 | 0.8951 |  |
| HbA1c (%) | +0.0301 | 0.1069 | ±0.2138 | +0.282 | 0.7780 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **198**, R² = **0.1506**, Adj R² = **0.0856**, F-statistic = **2.32** (p = **0.0059**), Residual SE = **0.837** on **183** df, AIC = **506.1**, BIC = **555.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0988** | 0.7522 | ±1.5044 | **+2.790** | **0.0053** | ** |
| **Education: graduate level (vs college)** | **-0.2419** | 0.1227 | ±0.2454 | **-1.971** | **0.0487** | * |
| Education: high school or below (vs college) | +0.4781 | 0.2482 | ±0.4965 | +1.926 | 0.0541 | . |
| Site: UCSD (vs UAB) | +0.1607 | 0.1641 | ±0.3282 | +0.979 | 0.3276 |  |
| Site: UW (vs UAB) | -0.0768 | 0.1589 | ±0.3178 | -0.483 | 0.6288 |  |
| Season: spring (vs autumn) | +0.0771 | 0.1754 | ±0.3509 | +0.440 | 0.6602 |  |
| Season: summer (vs autumn) | +0.0653 | 0.1681 | ±0.3362 | +0.388 | 0.6977 |  |
| Season: winter (vs autumn) | +0.0302 | 0.1524 | ±0.3048 | +0.198 | 0.8430 |  |
| Age (years) | -0.0085 | 0.0067 | ±0.0135 | -1.262 | 0.2068 |  |
| BMI (kg/m2) | +0.0196 | 0.0108 | ±0.0216 | +1.812 | 0.0700 | . |
| Hypertension | +0.1470 | 0.1424 | ±0.2848 | +1.032 | 0.3019 |  |
| High cholesterol | -0.0828 | 0.1257 | ±0.2513 | -0.659 | 0.5097 |  |
| Kidney disease | -0.0699 | 0.1889 | ±0.3778 | -0.370 | 0.7113 |  |
| Circulatory disease | -0.0122 | 0.1676 | ±0.3353 | -0.073 | 0.9421 |  |
| Mean glucose (mg/dL) | -0.0026 | 0.0048 | ±0.0096 | -0.537 | 0.5915 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **198**, R² = **0.1506**, Adj R² = **0.0856**, F-statistic = **2.32** (p = **0.0059**), Residual SE = **0.837** on **183** df, AIC = **506.1**, BIC = **555.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2.4557 | 1.2846 | ±2.5692 | +1.912 | 0.0559 | . |
| **Education: graduate level (vs college)** | **-0.2419** | 0.1227 | ±0.2454 | **-1.971** | **0.0487** | * |
| Education: high school or below (vs college) | +0.4781 | 0.2482 | ±0.4965 | +1.926 | 0.0541 | . |
| Site: UCSD (vs UAB) | +0.1607 | 0.1641 | ±0.3282 | +0.979 | 0.3276 |  |
| Site: UW (vs UAB) | -0.0768 | 0.1589 | ±0.3178 | -0.483 | 0.6288 |  |
| Season: spring (vs autumn) | +0.0771 | 0.1754 | ±0.3509 | +0.440 | 0.6602 |  |
| Season: summer (vs autumn) | +0.0653 | 0.1681 | ±0.3362 | +0.388 | 0.6977 |  |
| Season: winter (vs autumn) | +0.0302 | 0.1524 | ±0.3048 | +0.198 | 0.8430 |  |
| Age (years) | -0.0085 | 0.0067 | ±0.0135 | -1.262 | 0.2068 |  |
| BMI (kg/m2) | +0.0196 | 0.0108 | ±0.0216 | +1.812 | 0.0700 | . |
| Hypertension | +0.1470 | 0.1424 | ±0.2848 | +1.032 | 0.3019 |  |
| High cholesterol | -0.0828 | 0.1257 | ±0.2513 | -0.659 | 0.5097 |  |
| Kidney disease | -0.0699 | 0.1889 | ±0.3778 | -0.370 | 0.7113 |  |
| Circulatory disease | -0.0122 | 0.1676 | ±0.3353 | -0.073 | 0.9421 |  |
| GMI (%) | -0.1078 | 0.2009 | ±0.4018 | -0.537 | 0.5915 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **198**, R² = **0.1504**, Adj R² = **0.0854**, F-statistic = **2.31** (p = **0.0060**), Residual SE = **0.838** on **183** df, AIC = **506.1**, BIC = **555.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0459** | 0.6840 | ±1.3679 | **+2.991** | **0.0028** | ** |
| Education: graduate level (vs college) | -0.2396 | 0.1231 | ±0.2462 | -1.947 | 0.0516 | . |
| Education: high school or below (vs college) | +0.4805 | 0.2488 | ±0.4976 | +1.931 | 0.0535 | . |
| Site: UCSD (vs UAB) | +0.1626 | 0.1650 | ±0.3300 | +0.986 | 0.3243 |  |
| Site: UW (vs UAB) | -0.0747 | 0.1591 | ±0.3182 | -0.470 | 0.6386 |  |
| Season: spring (vs autumn) | +0.0750 | 0.1747 | ±0.3494 | +0.429 | 0.6676 |  |
| Season: summer (vs autumn) | +0.0618 | 0.1666 | ±0.3333 | +0.371 | 0.7107 |  |
| Season: winter (vs autumn) | +0.0262 | 0.1514 | ±0.3027 | +0.173 | 0.8625 |  |
| Age (years) | -0.0087 | 0.0067 | ±0.0135 | -1.299 | 0.1940 |  |
| BMI (kg/m2) | +0.0197 | 0.0109 | ±0.0219 | +1.796 | 0.0724 | . |
| Hypertension | +0.1441 | 0.1420 | ±0.2841 | +1.015 | 0.3103 |  |
| High cholesterol | -0.0794 | 0.1257 | ±0.2514 | -0.631 | 0.5277 |  |
| Kidney disease | -0.0769 | 0.1874 | ±0.3748 | -0.410 | 0.6815 |  |
| Circulatory disease | -0.0104 | 0.1683 | ±0.3365 | -0.062 | 0.9505 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0021 | 0.0044 | ±0.0088 | -0.472 | 0.6370 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **198**, R² = **0.1603**, Adj R² = **0.0960**, F-statistic = **2.49** (p = **0.0029**), Residual SE = **0.833** on **183** df, AIC = **503.8**, BIC = **553.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.3737** | 0.5927 | ±1.1854 | **+2.318** | **0.0205** | * |
| **Education: graduate level (vs college)** | **-0.2556** | 0.1208 | ±0.2415 | **-2.116** | **0.0343** | * |
| Education: high school or below (vs college) | +0.4305 | 0.2462 | ±0.4925 | +1.748 | 0.0804 | . |
| Site: UCSD (vs UAB) | +0.1801 | 0.1627 | ±0.3254 | +1.107 | 0.2684 |  |
| Site: UW (vs UAB) | -0.0364 | 0.1564 | ±0.3128 | -0.233 | 0.8158 |  |
| Season: spring (vs autumn) | +0.0757 | 0.1727 | ±0.3454 | +0.439 | 0.6610 |  |
| Season: summer (vs autumn) | +0.0576 | 0.1640 | ±0.3280 | +0.351 | 0.7257 |  |
| Season: winter (vs autumn) | +0.0269 | 0.1491 | ±0.2983 | +0.180 | 0.8571 |  |
| Age (years) | -0.0092 | 0.0067 | ±0.0133 | -1.385 | 0.1661 |  |
| BMI (kg/m2) | +0.0194 | 0.0104 | ±0.0208 | +1.861 | 0.0628 | . |
| Hypertension | +0.1079 | 0.1449 | ±0.2898 | +0.745 | 0.4563 |  |
| High cholesterol | -0.0659 | 0.1255 | ±0.2510 | -0.525 | 0.5995 |  |
| Kidney disease | -0.1212 | 0.1900 | ±0.3800 | -0.638 | 0.5236 |  |
| Circulatory disease | -0.0313 | 0.1638 | ±0.3275 | -0.191 | 0.8485 |  |
| Glucose SD, pooled (mg/dL) | +0.0214 | 0.0127 | ±0.0255 | +1.678 | 0.0934 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **198**, R² = **0.1559**, Adj R² = **0.0913**, F-statistic = **2.41** (p = **0.0040**), Residual SE = **0.835** on **183** df, AIC = **504.8**, BIC = **554.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.4931** | 0.5915 | ±1.1830 | **+2.524** | **0.0116** | * |
| **Education: graduate level (vs college)** | **-0.2508** | 0.1213 | ±0.2425 | **-2.068** | **0.0386** | * |
| Education: high school or below (vs college) | +0.4500 | 0.2470 | ±0.4939 | +1.822 | 0.0684 | . |
| Site: UCSD (vs UAB) | +0.1665 | 0.1636 | ±0.3272 | +1.018 | 0.3088 |  |
| Site: UW (vs UAB) | -0.0533 | 0.1574 | ±0.3149 | -0.339 | 0.7348 |  |
| Season: spring (vs autumn) | +0.0810 | 0.1726 | ±0.3452 | +0.469 | 0.6387 |  |
| Season: summer (vs autumn) | +0.0630 | 0.1655 | ±0.3310 | +0.381 | 0.7035 |  |
| Season: winter (vs autumn) | +0.0301 | 0.1495 | ±0.2991 | +0.201 | 0.8407 |  |
| Age (years) | -0.0091 | 0.0067 | ±0.0134 | -1.356 | 0.1752 |  |
| BMI (kg/m2) | +0.0193 | 0.0104 | ±0.0209 | +1.853 | 0.0640 | . |
| Hypertension | +0.1090 | 0.1447 | ±0.2894 | +0.753 | 0.4512 |  |
| High cholesterol | -0.0686 | 0.1265 | ±0.2530 | -0.543 | 0.5875 |  |
| Kidney disease | -0.1016 | 0.1869 | ±0.3737 | -0.544 | 0.5865 |  |
| Circulatory disease | -0.0195 | 0.1658 | ±0.3316 | -0.117 | 0.9065 |  |
| Avg. daily SD (mg/dL) | +0.0168 | 0.0122 | ±0.0243 | +1.379 | 0.1678 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **198**, R² = **0.1723**, Adj R² = **0.1090**, F-statistic = **2.72** (p = **0.0012**), Residual SE = **0.827** on **183** df, AIC = **500.9**, BIC = **550.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0552 | 0.6253 | ±1.2506 | +1.688 | 0.0915 | . |
| **Education: graduate level (vs college)** | **-0.2639** | 0.1188 | ±0.2376 | **-2.221** | **0.0263** | * |
| Education: high school or below (vs college) | +0.3744 | 0.2481 | ±0.4961 | +1.509 | 0.1312 |  |
| Site: UCSD (vs UAB) | +0.1933 | 0.1625 | ±0.3249 | +1.190 | 0.2340 |  |
| Site: UW (vs UAB) | -0.0162 | 0.1562 | ±0.3124 | -0.104 | 0.9173 |  |
| Season: spring (vs autumn) | +0.0815 | 0.1721 | ±0.3441 | +0.473 | 0.6359 |  |
| Season: summer (vs autumn) | +0.0830 | 0.1656 | ±0.3312 | +0.501 | 0.6164 |  |
| Season: winter (vs autumn) | +0.0335 | 0.1490 | ±0.2981 | +0.225 | 0.8222 |  |
| Age (years) | -0.0099 | 0.0067 | ±0.0133 | -1.490 | 0.1362 |  |
| **BMI (kg/m2)** | **+0.0205** | 0.0103 | ±0.0205 | **+1.996** | **0.0459** | * |
| Hypertension | +0.0933 | 0.1429 | ±0.2859 | +0.653 | 0.5138 |  |
| High cholesterol | -0.0621 | 0.1236 | ±0.2473 | -0.503 | 0.6152 |  |
| Kidney disease | -0.1343 | 0.1856 | ±0.3713 | -0.723 | 0.4694 |  |
| Circulatory disease | -0.0296 | 0.1601 | ±0.3202 | -0.185 | 0.8531 |  |
| **CV (%)** | **+0.0462** | 0.0194 | ±0.0388 | **+2.378** | **0.0174** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **198**, R² = **0.1681**, Adj R² = **0.1045**, F-statistic = **2.64** (p = **0.0016**), Residual SE = **0.829** on **183** df, AIC = **501.9**, BIC = **551.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5297** | 0.6592 | ±1.3183 | **+3.838** | **1.24e-04** | *** |
| **Education: graduate level (vs college)** | **-0.2580** | 0.1204 | ±0.2409 | **-2.143** | **0.0321** | * |
| Education: high school or below (vs college) | +0.3967 | 0.2469 | ±0.4938 | +1.607 | 0.1081 |  |
| Site: UCSD (vs UAB) | +0.1835 | 0.1630 | ±0.3259 | +1.126 | 0.2601 |  |
| Site: UW (vs UAB) | -0.0283 | 0.1560 | ±0.3121 | -0.181 | 0.8561 |  |
| Season: spring (vs autumn) | +0.0801 | 0.1718 | ±0.3436 | +0.466 | 0.6409 |  |
| Season: summer (vs autumn) | +0.0776 | 0.1655 | ±0.3311 | +0.469 | 0.6392 |  |
| Season: winter (vs autumn) | +0.0302 | 0.1491 | ±0.2983 | +0.202 | 0.8397 |  |
| Age (years) | -0.0098 | 0.0066 | ±0.0133 | -1.479 | 0.1391 |  |
| BMI (kg/m2) | +0.0196 | 0.0104 | ±0.0207 | +1.891 | 0.0587 | . |
| Hypertension | +0.0956 | 0.1422 | ±0.2845 | +0.672 | 0.5017 |  |
| High cholesterol | -0.0695 | 0.1235 | ±0.2471 | -0.563 | 0.5737 |  |
| Kidney disease | -0.1268 | 0.1854 | ±0.3709 | -0.684 | 0.4940 |  |
| Circulatory disease | -0.0209 | 0.1612 | ±0.3223 | -0.129 | 0.8970 |  |
| **Mean / SD ratio** | **-0.1085** | 0.0467 | ±0.0933 | **-2.326** | **0.0200** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **198**, R² = **0.1612**, Adj R² = **0.0971**, F-statistic = **2.51** (p = **0.0027**), Residual SE = **0.832** on **183** df, AIC = **503.6**, BIC = **552.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.3261** | 0.6549 | ±1.3098 | **+3.552** | **3.83e-04** | *** |
| **Education: graduate level (vs college)** | **-0.2484** | 0.1215 | ±0.2430 | **-2.045** | **0.0409** | * |
| Education: high school or below (vs college) | +0.4304 | 0.2472 | ±0.4944 | +1.741 | 0.0816 | . |
| Site: UCSD (vs UAB) | +0.1594 | 0.1630 | ±0.3259 | +0.978 | 0.3280 |  |
| Site: UW (vs UAB) | -0.0489 | 0.1567 | ±0.3133 | -0.312 | 0.7551 |  |
| Season: spring (vs autumn) | +0.0824 | 0.1722 | ±0.3444 | +0.479 | 0.6323 |  |
| Season: summer (vs autumn) | +0.0780 | 0.1667 | ±0.3334 | +0.468 | 0.6401 |  |
| Season: winter (vs autumn) | +0.0380 | 0.1502 | ±0.3005 | +0.253 | 0.8005 |  |
| Age (years) | -0.0096 | 0.0067 | ±0.0134 | -1.435 | 0.1513 |  |
| BMI (kg/m2) | +0.0193 | 0.0104 | ±0.0208 | +1.862 | 0.0626 | . |
| Hypertension | +0.0931 | 0.1427 | ±0.2853 | +0.653 | 0.5140 |  |
| High cholesterol | -0.0763 | 0.1245 | ±0.2491 | -0.613 | 0.5401 |  |
| Kidney disease | -0.1055 | 0.1842 | ±0.3683 | -0.573 | 0.5668 |  |
| Circulatory disease | -0.0023 | 0.1647 | ±0.3294 | -0.014 | 0.9891 |  |
| Avg. daily mean/SD | -0.0661 | 0.0366 | ±0.0733 | -1.805 | 0.0710 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **198**, R² = **0.1553**, Adj R² = **0.0907**, F-statistic = **2.40** (p = **0.0042**), Residual SE = **0.835** on **183** df, AIC = **504.9**, BIC = **554.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.4050** | 0.5938 | ±1.1875 | **+2.366** | **0.0180** | * |
| **Education: graduate level (vs college)** | **-0.2446** | 0.1218 | ±0.2436 | **-2.009** | **0.0446** | * |
| Education: high school or below (vs college) | +0.4661 | 0.2490 | ±0.4980 | +1.872 | 0.0612 | . |
| Site: UCSD (vs UAB) | +0.1606 | 0.1645 | ±0.3289 | +0.976 | 0.3289 |  |
| Site: UW (vs UAB) | -0.0645 | 0.1575 | ±0.3150 | -0.409 | 0.6822 |  |
| Season: spring (vs autumn) | +0.0777 | 0.1733 | ±0.3466 | +0.448 | 0.6540 |  |
| Season: summer (vs autumn) | +0.0580 | 0.1637 | ±0.3274 | +0.354 | 0.7230 |  |
| Season: winter (vs autumn) | +0.0306 | 0.1511 | ±0.3023 | +0.203 | 0.8393 |  |
| Age (years) | -0.0083 | 0.0066 | ±0.0133 | -1.247 | 0.2124 |  |
| BMI (kg/m2) | +0.0188 | 0.0106 | ±0.0213 | +1.770 | 0.0767 | . |
| Hypertension | +0.1331 | 0.1430 | ±0.2859 | +0.931 | 0.3520 |  |
| High cholesterol | -0.0866 | 0.1246 | ±0.2492 | -0.695 | 0.4873 |  |
| Kidney disease | -0.0769 | 0.1875 | ±0.3750 | -0.410 | 0.6819 |  |
| Circulatory disease | -0.0038 | 0.1679 | ±0.3358 | -0.023 | 0.9818 |  |
| MAG (mg/dL/h) | +0.0106 | 0.0076 | ±0.0152 | +1.402 | 0.1608 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **198**, R² = **0.1603**, Adj R² = **0.0960**, F-statistic = **2.50** (p = **0.0029**), Residual SE = **0.833** on **183** df, AIC = **503.8**, BIC = **553.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.2989** | 0.6104 | ±1.2209 | **+2.128** | **0.0334** | * |
| **Education: graduate level (vs college)** | **-0.2479** | 0.1210 | ±0.2420 | **-2.049** | **0.0405** | * |
| Education: high school or below (vs college) | +0.4490 | 0.2480 | ±0.4960 | +1.811 | 0.0702 | . |
| Site: UCSD (vs UAB) | +0.1739 | 0.1631 | ±0.3262 | +1.066 | 0.2865 |  |
| Site: UW (vs UAB) | -0.0487 | 0.1568 | ±0.3137 | -0.310 | 0.7562 |  |
| Season: spring (vs autumn) | +0.0786 | 0.1729 | ±0.3457 | +0.455 | 0.6494 |  |
| Season: summer (vs autumn) | +0.0682 | 0.1638 | ±0.3277 | +0.416 | 0.6774 |  |
| Season: winter (vs autumn) | +0.0346 | 0.1495 | ±0.2991 | +0.231 | 0.8171 |  |
| Age (years) | -0.0093 | 0.0066 | ±0.0133 | -1.404 | 0.1604 |  |
| BMI (kg/m2) | +0.0201 | 0.0103 | ±0.0207 | +1.940 | 0.0524 | . |
| Hypertension | +0.1109 | 0.1435 | ±0.2870 | +0.773 | 0.4396 |  |
| High cholesterol | -0.0735 | 0.1250 | ±0.2500 | -0.588 | 0.5566 |  |
| Kidney disease | -0.0969 | 0.1850 | ±0.3699 | -0.524 | 0.6004 |  |
| Circulatory disease | -0.0145 | 0.1665 | ±0.3331 | -0.087 | 0.9307 |  |
| Avg. daily range (mg/dL) | +0.0054 | 0.0029 | ±0.0058 | +1.837 | 0.0662 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **198**, R² = **0.1678**, Adj R² = **0.1041**, F-statistic = **2.64** (p = **0.0016**), Residual SE = **0.829** on **183** df, AIC = **502.0**, BIC = **551.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.4751** | 0.5852 | ±1.1705 | **+2.521** | **0.0117** | * |
| **Education: graduate level (vs college)** | **-0.2567** | 0.1214 | ±0.2428 | **-2.114** | **0.0345** | * |
| Education: high school or below (vs college) | +0.4154 | 0.2366 | ±0.4732 | +1.756 | 0.0791 | . |
| Site: UCSD (vs UAB) | +0.2145 | 0.1572 | ±0.3144 | +1.365 | 0.1724 |  |
| Site: UW (vs UAB) | -0.0129 | 0.1522 | ±0.3043 | -0.085 | 0.9326 |  |
| Season: spring (vs autumn) | +0.0507 | 0.1724 | ±0.3447 | +0.294 | 0.7686 |  |
| Season: summer (vs autumn) | +0.0077 | 0.1629 | ±0.3258 | +0.047 | 0.9622 |  |
| Season: winter (vs autumn) | +0.0230 | 0.1495 | ±0.2989 | +0.154 | 0.8777 |  |
| Age (years) | -0.0088 | 0.0066 | ±0.0131 | -1.333 | 0.1825 |  |
| BMI (kg/m2) | +0.0190 | 0.0105 | ±0.0210 | +1.809 | 0.0705 | . |
| Hypertension | +0.1639 | 0.1440 | ±0.2881 | +1.138 | 0.2551 |  |
| High cholesterol | -0.0878 | 0.1247 | ±0.2493 | -0.705 | 0.4811 |  |
| Kidney disease | -0.1447 | 0.2062 | ±0.4124 | -0.702 | 0.4827 |  |
| Circulatory disease | -0.0862 | 0.1577 | ±0.3154 | -0.546 | 0.5848 |  |
| SD of daily means (mg/dL) | +0.0515 | 0.0317 | ±0.0634 | +1.626 | 0.1040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **198**, R² = **0.1495**, Adj R² = **0.0845**, F-statistic = **2.30** (p = **0.0063**), Residual SE = **0.838** on **183** df, AIC = **506.3**, BIC = **555.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.4659 | 1.4994 | ±2.9989 | +0.978 | 0.3283 |  |
| Education: graduate level (vs college) | -0.2400 | 0.1229 | ±0.2458 | -1.953 | 0.0508 | . |
| **Education: high school or below (vs college)** | **+0.4882** | 0.2477 | ±0.4953 | **+1.971** | **0.0487** | * |
| Site: UCSD (vs UAB) | +0.1584 | 0.1633 | ±0.3266 | +0.970 | 0.3322 |  |
| Site: UW (vs UAB) | -0.0769 | 0.1595 | ±0.3189 | -0.482 | 0.6295 |  |
| Season: spring (vs autumn) | +0.0743 | 0.1746 | ±0.3491 | +0.425 | 0.6706 |  |
| Season: summer (vs autumn) | +0.0576 | 0.1672 | ±0.3344 | +0.344 | 0.7305 |  |
| Season: winter (vs autumn) | +0.0272 | 0.1520 | ±0.3039 | +0.179 | 0.8580 |  |
| Age (years) | -0.0083 | 0.0068 | ±0.0136 | -1.219 | 0.2227 |  |
| BMI (kg/m2) | +0.0192 | 0.0106 | ±0.0213 | +1.807 | 0.0708 | . |
| Hypertension | +0.1445 | 0.1424 | ±0.2849 | +1.014 | 0.3105 |  |
| High cholesterol | -0.0821 | 0.1270 | ±0.2540 | -0.647 | 0.5177 |  |
| Kidney disease | -0.0713 | 0.1927 | ±0.3854 | -0.370 | 0.7113 |  |
| Circulatory disease | -0.0141 | 0.1677 | ±0.3354 | -0.084 | 0.9330 |  |
| Time in range 70-180, pooled (%) | +0.0032 | 0.0128 | ±0.0257 | +0.250 | 0.8029 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **198**, R² = **0.1494**, Adj R² = **0.0843**, F-statistic = **2.30** (p = **0.0064**), Residual SE = **0.838** on **183** df, AIC = **506.3**, BIC = **555.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.5317 | 1.5583 | ±3.1166 | +0.983 | 0.3256 |  |
| Education: graduate level (vs college) | -0.2406 | 0.1229 | ±0.2457 | -1.958 | 0.0502 | . |
| **Education: high school or below (vs college)** | **+0.4868** | 0.2474 | ±0.4947 | **+1.968** | **0.0491** | * |
| Site: UCSD (vs UAB) | +0.1590 | 0.1632 | ±0.3264 | +0.974 | 0.3299 |  |
| Site: UW (vs UAB) | -0.0759 | 0.1594 | ±0.3187 | -0.476 | 0.6341 |  |
| Season: spring (vs autumn) | +0.0742 | 0.1744 | ±0.3489 | +0.425 | 0.6706 |  |
| Season: summer (vs autumn) | +0.0572 | 0.1672 | ±0.3344 | +0.342 | 0.7324 |  |
| Season: winter (vs autumn) | +0.0270 | 0.1520 | ±0.3039 | +0.177 | 0.8591 |  |
| Age (years) | -0.0083 | 0.0068 | ±0.0136 | -1.222 | 0.2218 |  |
| BMI (kg/m2) | +0.0192 | 0.0106 | ±0.0212 | +1.808 | 0.0707 | . |
| Hypertension | +0.1444 | 0.1425 | ±0.2850 | +1.013 | 0.3108 |  |
| High cholesterol | -0.0816 | 0.1271 | ±0.2541 | -0.642 | 0.5206 |  |
| Kidney disease | -0.0727 | 0.1930 | ±0.3860 | -0.376 | 0.7066 |  |
| Circulatory disease | -0.0146 | 0.1678 | ±0.3355 | -0.087 | 0.9309 |  |
| Avg. daily time in range 70-180 (%) | +0.0025 | 0.0135 | ±0.0270 | +0.189 | 0.8504 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **198**, R² = **0.1651**, Adj R² = **0.1012**, F-statistic = **2.58** (p = **0.0020**), Residual SE = **0.830** on **183** df, AIC = **502.6**, BIC = **552.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8165** | 0.6040 | ±1.2081 | **+3.007** | **0.0026** | ** |
| **Education: graduate level (vs college)** | **-0.2575** | 0.1211 | ±0.2422 | **-2.127** | **0.0335** | * |
| Education: high school or below (vs college) | +0.4341 | 0.2448 | ±0.4896 | +1.773 | 0.0761 | . |
| Site: UCSD (vs UAB) | +0.1813 | 0.1625 | ±0.3251 | +1.116 | 0.2646 |  |
| Site: UW (vs UAB) | -0.0683 | 0.1655 | ±0.3310 | -0.413 | 0.6799 |  |
| Season: spring (vs autumn) | +0.1051 | 0.1738 | ±0.3476 | +0.605 | 0.5452 |  |
| Season: summer (vs autumn) | +0.0728 | 0.1733 | ±0.3465 | +0.420 | 0.6745 |  |
| Season: winter (vs autumn) | +0.0600 | 0.1539 | ±0.3079 | +0.390 | 0.6966 |  |
| Age (years) | -0.0103 | 0.0073 | ±0.0145 | -1.413 | 0.1577 |  |
| BMI (kg/m2) | +0.0201 | 0.0105 | ±0.0210 | +1.909 | 0.0562 | . |
| Hypertension | +0.1320 | 0.1430 | ±0.2861 | +0.923 | 0.3562 |  |
| High cholesterol | -0.0949 | 0.1248 | ±0.2496 | -0.761 | 0.4469 |  |
| Kidney disease | -0.0608 | 0.1886 | ±0.3771 | -0.322 | 0.7472 |  |
| Circulatory disease | -0.0178 | 0.1681 | ±0.3363 | -0.106 | 0.9157 |  |
| Time 54-69, pooled (%) | +0.4201 | 0.5556 | ±1.1113 | +0.756 | 0.4497 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **198**, R² = **0.1579**, Adj R² = **0.0934**, F-statistic = **2.45** (p = **0.0035**), Residual SE = **0.834** on **183** df, AIC = **504.3**, BIC = **553.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8215** | 0.6066 | ±1.2133 | **+3.003** | **0.0027** | ** |
| **Education: graduate level (vs college)** | **-0.2530** | 0.1210 | ±0.2419 | **-2.092** | **0.0365** | * |
| Education: high school or below (vs college) | +0.4486 | 0.2475 | ±0.4951 | +1.812 | 0.0700 | . |
| Site: UCSD (vs UAB) | +0.1689 | 0.1630 | ±0.3260 | +1.036 | 0.3002 |  |
| Site: UW (vs UAB) | -0.0754 | 0.1649 | ±0.3298 | -0.457 | 0.6475 |  |
| Season: spring (vs autumn) | +0.0974 | 0.1735 | ±0.3470 | +0.561 | 0.5746 |  |
| Season: summer (vs autumn) | +0.0758 | 0.1748 | ±0.3496 | +0.433 | 0.6647 |  |
| Season: winter (vs autumn) | +0.0499 | 0.1536 | ±0.3073 | +0.325 | 0.7455 |  |
| Age (years) | -0.0099 | 0.0072 | ±0.0145 | -1.364 | 0.1725 |  |
| BMI (kg/m2) | +0.0198 | 0.0105 | ±0.0211 | +1.878 | 0.0604 | . |
| Hypertension | +0.1306 | 0.1429 | ±0.2858 | +0.914 | 0.3606 |  |
| High cholesterol | -0.0910 | 0.1251 | ±0.2501 | -0.727 | 0.4670 |  |
| Kidney disease | -0.0605 | 0.1874 | ±0.3748 | -0.323 | 0.7470 |  |
| Circulatory disease | -0.0098 | 0.1707 | ±0.3414 | -0.058 | 0.9541 |  |
| Avg. daily time 54-69 (%) | +0.3017 | 0.5277 | ±1.0554 | +0.572 | 0.5675 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **198**, R² = **0.1651**, Adj R² = **0.1012**, F-statistic = **2.58** (p = **0.0020**), Residual SE = **0.830** on **183** df, AIC = **502.6**, BIC = **552.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8165** | 0.6040 | ±1.2081 | **+3.007** | **0.0026** | ** |
| **Education: graduate level (vs college)** | **-0.2575** | 0.1211 | ±0.2422 | **-2.127** | **0.0335** | * |
| Education: high school or below (vs college) | +0.4341 | 0.2448 | ±0.4896 | +1.773 | 0.0761 | . |
| Site: UCSD (vs UAB) | +0.1813 | 0.1625 | ±0.3251 | +1.116 | 0.2646 |  |
| Site: UW (vs UAB) | -0.0683 | 0.1655 | ±0.3310 | -0.413 | 0.6799 |  |
| Season: spring (vs autumn) | +0.1051 | 0.1738 | ±0.3476 | +0.605 | 0.5452 |  |
| Season: summer (vs autumn) | +0.0728 | 0.1733 | ±0.3465 | +0.420 | 0.6745 |  |
| Season: winter (vs autumn) | +0.0600 | 0.1539 | ±0.3079 | +0.390 | 0.6966 |  |
| Age (years) | -0.0103 | 0.0073 | ±0.0145 | -1.413 | 0.1577 |  |
| BMI (kg/m2) | +0.0201 | 0.0105 | ±0.0210 | +1.909 | 0.0562 | . |
| Hypertension | +0.1320 | 0.1430 | ±0.2861 | +0.923 | 0.3562 |  |
| High cholesterol | -0.0949 | 0.1248 | ±0.2496 | -0.761 | 0.4469 |  |
| Kidney disease | -0.0608 | 0.1886 | ±0.3771 | -0.322 | 0.7472 |  |
| Circulatory disease | -0.0178 | 0.1681 | ±0.3363 | -0.106 | 0.9157 |  |
| Time < 70 (%) | +0.4201 | 0.5556 | ±1.1113 | +0.756 | 0.4497 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **198**, R² = **0.1579**, Adj R² = **0.0934**, F-statistic = **2.45** (p = **0.0035**), Residual SE = **0.834** on **183** df, AIC = **504.3**, BIC = **553.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8215** | 0.6066 | ±1.2133 | **+3.003** | **0.0027** | ** |
| **Education: graduate level (vs college)** | **-0.2530** | 0.1210 | ±0.2419 | **-2.092** | **0.0365** | * |
| Education: high school or below (vs college) | +0.4486 | 0.2475 | ±0.4951 | +1.812 | 0.0700 | . |
| Site: UCSD (vs UAB) | +0.1689 | 0.1630 | ±0.3260 | +1.036 | 0.3002 |  |
| Site: UW (vs UAB) | -0.0754 | 0.1649 | ±0.3298 | -0.457 | 0.6475 |  |
| Season: spring (vs autumn) | +0.0974 | 0.1735 | ±0.3470 | +0.561 | 0.5746 |  |
| Season: summer (vs autumn) | +0.0758 | 0.1748 | ±0.3496 | +0.433 | 0.6647 |  |
| Season: winter (vs autumn) | +0.0499 | 0.1536 | ±0.3073 | +0.325 | 0.7455 |  |
| Age (years) | -0.0099 | 0.0072 | ±0.0145 | -1.364 | 0.1725 |  |
| BMI (kg/m2) | +0.0198 | 0.0105 | ±0.0211 | +1.878 | 0.0604 | . |
| Hypertension | +0.1306 | 0.1429 | ±0.2858 | +0.914 | 0.3606 |  |
| High cholesterol | -0.0910 | 0.1251 | ±0.2501 | -0.727 | 0.4670 |  |
| Kidney disease | -0.0605 | 0.1874 | ±0.3748 | -0.323 | 0.7470 |  |
| Circulatory disease | -0.0098 | 0.1707 | ±0.3414 | -0.058 | 0.9541 |  |
| Avg. daily time < 70 (%) | +0.3017 | 0.5277 | ±1.0554 | +0.572 | 0.5675 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **198**, R² = **0.1498**, Adj R² = **0.0848**, F-statistic = **2.30** (p = **0.0062**), Residual SE = **0.838** on **183** df, AIC = **506.2**, BIC = **555.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7866** | 0.5850 | ±1.1700 | **+3.054** | **0.0023** | ** |
| Education: graduate level (vs college) | -0.2394 | 0.1230 | ±0.2459 | -1.946 | 0.0516 | . |
| **Education: high school or below (vs college)** | **+0.4894** | 0.2479 | ±0.4957 | **+1.975** | **0.0483** | * |
| Site: UCSD (vs UAB) | +0.1574 | 0.1635 | ±0.3269 | +0.963 | 0.3357 |  |
| Site: UW (vs UAB) | -0.0781 | 0.1598 | ±0.3196 | -0.489 | 0.6249 |  |
| Season: spring (vs autumn) | +0.0744 | 0.1748 | ±0.3496 | +0.426 | 0.6702 |  |
| Season: summer (vs autumn) | +0.0587 | 0.1677 | ±0.3354 | +0.350 | 0.7261 |  |
| Season: winter (vs autumn) | +0.0281 | 0.1523 | ±0.3047 | +0.184 | 0.8537 |  |
| Age (years) | -0.0082 | 0.0068 | ±0.0135 | -1.217 | 0.2237 |  |
| BMI (kg/m2) | +0.0192 | 0.0106 | ±0.0213 | +1.810 | 0.0703 | . |
| Hypertension | +0.1451 | 0.1423 | ±0.2845 | +1.020 | 0.3077 |  |
| High cholesterol | -0.0831 | 0.1270 | ±0.2541 | -0.654 | 0.5130 |  |
| Kidney disease | -0.0684 | 0.1922 | ±0.3845 | -0.356 | 0.7221 |  |
| Circulatory disease | -0.0134 | 0.1679 | ±0.3358 | -0.080 | 0.9366 |  |
| Time 181-250, pooled (%) | -0.0046 | 0.0126 | ±0.0252 | -0.362 | 0.7174 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **198**, R² = **0.1496**, Adj R² = **0.0845**, F-statistic = **2.30** (p = **0.0063**), Residual SE = **0.838** on **183** df, AIC = **506.3**, BIC = **555.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7863** | 0.5850 | ±1.1701 | **+3.053** | **0.0023** | ** |
| Education: graduate level (vs college) | -0.2401 | 0.1229 | ±0.2459 | -1.953 | 0.0508 | . |
| **Education: high school or below (vs college)** | **+0.4875** | 0.2475 | ±0.4950 | **+1.970** | **0.0489** | * |
| Site: UCSD (vs UAB) | +0.1582 | 0.1633 | ±0.3267 | +0.968 | 0.3329 |  |
| Site: UW (vs UAB) | -0.0766 | 0.1596 | ±0.3192 | -0.480 | 0.6311 |  |
| Season: spring (vs autumn) | +0.0743 | 0.1747 | ±0.3493 | +0.425 | 0.6706 |  |
| Season: summer (vs autumn) | +0.0582 | 0.1676 | ±0.3353 | +0.347 | 0.7285 |  |
| Season: winter (vs autumn) | +0.0277 | 0.1523 | ±0.3046 | +0.182 | 0.8557 |  |
| Age (years) | -0.0083 | 0.0068 | ±0.0136 | -1.221 | 0.2222 |  |
| BMI (kg/m2) | +0.0192 | 0.0106 | ±0.0212 | +1.809 | 0.0704 | . |
| Hypertension | +0.1450 | 0.1424 | ±0.2847 | +1.019 | 0.3083 |  |
| High cholesterol | -0.0823 | 0.1271 | ±0.2542 | -0.648 | 0.5172 |  |
| Kidney disease | -0.0703 | 0.1927 | ±0.3854 | -0.365 | 0.7153 |  |
| Circulatory disease | -0.0139 | 0.1680 | ±0.3359 | -0.083 | 0.9339 |  |
| Avg. daily time 181-250 (%) | -0.0036 | 0.0132 | ±0.0264 | -0.273 | 0.7849 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **198**, R² = **0.1498**, Adj R² = **0.0848**, F-statistic = **2.30** (p = **0.0062**), Residual SE = **0.838** on **183** df, AIC = **506.2**, BIC = **555.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7866** | 0.5850 | ±1.1700 | **+3.054** | **0.0023** | ** |
| Education: graduate level (vs college) | -0.2394 | 0.1230 | ±0.2459 | -1.946 | 0.0516 | . |
| **Education: high school or below (vs college)** | **+0.4894** | 0.2479 | ±0.4957 | **+1.975** | **0.0483** | * |
| Site: UCSD (vs UAB) | +0.1574 | 0.1635 | ±0.3269 | +0.963 | 0.3357 |  |
| Site: UW (vs UAB) | -0.0781 | 0.1598 | ±0.3196 | -0.489 | 0.6249 |  |
| Season: spring (vs autumn) | +0.0744 | 0.1748 | ±0.3496 | +0.426 | 0.6702 |  |
| Season: summer (vs autumn) | +0.0587 | 0.1677 | ±0.3354 | +0.350 | 0.7261 |  |
| Season: winter (vs autumn) | +0.0281 | 0.1523 | ±0.3047 | +0.184 | 0.8537 |  |
| Age (years) | -0.0082 | 0.0068 | ±0.0135 | -1.217 | 0.2237 |  |
| BMI (kg/m2) | +0.0192 | 0.0106 | ±0.0213 | +1.810 | 0.0703 | . |
| Hypertension | +0.1451 | 0.1423 | ±0.2845 | +1.020 | 0.3077 |  |
| High cholesterol | -0.0831 | 0.1270 | ±0.2541 | -0.654 | 0.5130 |  |
| Kidney disease | -0.0684 | 0.1922 | ±0.3845 | -0.356 | 0.7221 |  |
| Circulatory disease | -0.0134 | 0.1679 | ±0.3358 | -0.080 | 0.9366 |  |
| Time > 180 (%) | -0.0046 | 0.0126 | ±0.0252 | -0.362 | 0.7174 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **198**, R² = **0.1496**, Adj R² = **0.0845**, F-statistic = **2.30** (p = **0.0063**), Residual SE = **0.838** on **183** df, AIC = **506.3**, BIC = **555.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7863** | 0.5850 | ±1.1701 | **+3.053** | **0.0023** | ** |
| Education: graduate level (vs college) | -0.2401 | 0.1229 | ±0.2459 | -1.953 | 0.0508 | . |
| **Education: high school or below (vs college)** | **+0.4875** | 0.2475 | ±0.4950 | **+1.970** | **0.0489** | * |
| Site: UCSD (vs UAB) | +0.1582 | 0.1633 | ±0.3267 | +0.968 | 0.3329 |  |
| Site: UW (vs UAB) | -0.0766 | 0.1596 | ±0.3192 | -0.480 | 0.6311 |  |
| Season: spring (vs autumn) | +0.0743 | 0.1747 | ±0.3493 | +0.425 | 0.6706 |  |
| Season: summer (vs autumn) | +0.0582 | 0.1676 | ±0.3353 | +0.347 | 0.7285 |  |
| Season: winter (vs autumn) | +0.0277 | 0.1523 | ±0.3046 | +0.182 | 0.8557 |  |
| Age (years) | -0.0083 | 0.0068 | ±0.0136 | -1.221 | 0.2222 |  |
| BMI (kg/m2) | +0.0192 | 0.0106 | ±0.0212 | +1.809 | 0.0704 | . |
| Hypertension | +0.1450 | 0.1424 | ±0.2847 | +1.019 | 0.3083 |  |
| High cholesterol | -0.0823 | 0.1271 | ±0.2542 | -0.648 | 0.5172 |  |
| Kidney disease | -0.0703 | 0.1927 | ±0.3854 | -0.365 | 0.7153 |  |
| Circulatory disease | -0.0139 | 0.1680 | ±0.3359 | -0.083 | 0.9339 |  |
| Avg. daily time > 180 (%) | -0.0036 | 0.0132 | ±0.0264 | -0.273 | 0.7849 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 198)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **198**, R² = **0.1504**, Adj R² = **0.0854**, F-statistic = **2.31** (p = **0.0060**), Residual SE = **0.838** on **183** df, AIC = **506.1**, BIC = **555.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7841** | 0.5887 | ±1.1773 | **+3.031** | **0.0024** | ** |
| Education: graduate level (vs college) | -0.2401 | 0.1225 | ±0.2451 | -1.960 | 0.0500 | . |
| **Education: high school or below (vs college)** | **+0.4970** | 0.2472 | ±0.4944 | **+2.010** | **0.0444** | * |
| Site: UCSD (vs UAB) | +0.1506 | 0.1620 | ±0.3240 | +0.930 | 0.3525 |  |
| Site: UW (vs UAB) | -0.0841 | 0.1582 | ±0.3165 | -0.531 | 0.5953 |  |
| Season: spring (vs autumn) | +0.0778 | 0.1753 | ±0.3506 | +0.444 | 0.6571 |  |
| Season: summer (vs autumn) | +0.0628 | 0.1665 | ±0.3331 | +0.377 | 0.7059 |  |
| Season: winter (vs autumn) | +0.0280 | 0.1519 | ±0.3037 | +0.184 | 0.8539 |  |
| Age (years) | -0.0083 | 0.0068 | ±0.0136 | -1.230 | 0.2186 |  |
| BMI (kg/m2) | +0.0196 | 0.0108 | ±0.0217 | +1.806 | 0.0709 | . |
| Hypertension | +0.1372 | 0.1419 | ±0.2837 | +0.967 | 0.3336 |  |
| High cholesterol | -0.0799 | 0.1257 | ±0.2515 | -0.635 | 0.5254 |  |
| Kidney disease | -0.0639 | 0.1923 | ±0.3847 | -0.332 | 0.7396 |  |
| Circulatory disease | -0.0107 | 0.1671 | ±0.3342 | -0.064 | 0.9491 |  |
| Nocturnal time > 180 (%) | -0.0060 | 0.0125 | ±0.0250 | -0.482 | 0.6299 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 198; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **198**, R² = **0.2980**, Adj R² = **0.2484**, F-statistic = **6.01** (p = **2.88e-09**), Residual SE = **2.178** on **184** df, AIC = **883.6**, BIC = **929.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6150** | 1.6023 | ±3.2046 | **+16.610** | **5.87e-62** | *** |
| Education: graduate level (vs college) | -0.2084 | 0.3448 | ±0.6897 | -0.604 | 0.5457 |  |
| Education: high school or below (vs college) | +0.2547 | 0.5604 | ±1.1207 | +0.455 | 0.6494 |  |
| Site: UCSD (vs UAB) | -0.4989 | 0.3962 | ±0.7924 | -1.259 | 0.2079 |  |
| **Site: UW (vs UAB)** | **-1.9201** | 0.4689 | ±0.9378 | **-4.095** | **4.22e-05** | *** |
| Season: spring (vs autumn) | -0.8118 | 0.4526 | ±0.9053 | -1.793 | 0.0729 | . |
| Season: summer (vs autumn) | +0.6945 | 0.5145 | ±1.0291 | +1.350 | 0.1771 |  |
| **Season: winter (vs autumn)** | **-2.3175** | 0.4997 | ±0.9994 | **-4.638** | **3.52e-06** | *** |
| Age (years) | -0.0121 | 0.0153 | ±0.0306 | -0.789 | 0.4301 |  |
| BMI (kg/m2) | +0.0001 | 0.0236 | ±0.0473 | +0.004 | 0.9967 |  |
| Hypertension | +0.4953 | 0.3824 | ±0.7648 | +1.295 | 0.1952 |  |
| High cholesterol | +0.0309 | 0.3335 | ±0.6670 | +0.093 | 0.9261 |  |
| Kidney disease | +0.1632 | 0.4678 | ±0.9355 | +0.349 | 0.7272 |  |
| Circulatory disease | +0.0199 | 0.4591 | ±0.9181 | +0.043 | 0.9654 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **198**, R² = **0.2985**, Adj R² = **0.2448**, F-statistic = **5.56** (p = **6.94e-09**), Residual SE = **2.183** on **183** df, AIC = **885.4**, BIC = **934.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.2234** | 2.4556 | ±4.9112 | **+11.086** | **1.46e-28** | *** |
| Education: graduate level (vs college) | -0.2127 | 0.3456 | ±0.6912 | -0.615 | 0.5383 |  |
| Education: high school or below (vs college) | +0.2596 | 0.5639 | ±1.1277 | +0.460 | 0.6453 |  |
| Site: UCSD (vs UAB) | -0.5000 | 0.3981 | ±0.7962 | -1.256 | 0.2091 |  |
| **Site: UW (vs UAB)** | **-1.9221** | 0.4712 | ±0.9424 | **-4.079** | **4.52e-05** | *** |
| Season: spring (vs autumn) | -0.8153 | 0.4520 | ±0.9040 | -1.804 | 0.0713 | . |
| Season: summer (vs autumn) | +0.7084 | 0.5260 | ±1.0520 | +1.347 | 0.1780 |  |
| **Season: winter (vs autumn)** | **-2.3090** | 0.5043 | ±1.0086 | **-4.579** | **4.68e-06** | *** |
| Age (years) | -0.0120 | 0.0156 | ±0.0311 | -0.768 | 0.4422 |  |
| BMI (kg/m2) | +0.0019 | 0.0246 | ±0.0493 | +0.077 | 0.9383 |  |
| Hypertension | +0.4991 | 0.3846 | ±0.7692 | +1.298 | 0.1944 |  |
| High cholesterol | +0.0427 | 0.3412 | ±0.6823 | +0.125 | 0.9003 |  |
| Kidney disease | +0.1455 | 0.4711 | ±0.9422 | +0.309 | 0.7575 |  |
| Circulatory disease | +0.0450 | 0.4797 | ±0.9593 | +0.094 | 0.9252 |  |
| HbA1c (%) | -0.1148 | 0.3919 | ±0.7838 | -0.293 | 0.7697 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **198**, R² = **0.3017**, Adj R² = **0.2483**, F-statistic = **5.65** (p = **4.82e-09**), Residual SE = **2.178** on **183** df, AIC = **884.5**, BIC = **933.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.1160** | 2.1437 | ±4.2873 | **+13.116** | **2.67e-39** | *** |
| Education: graduate level (vs college) | -0.2081 | 0.3457 | ±0.6914 | -0.602 | 0.5471 |  |
| Education: high school or below (vs college) | +0.2252 | 0.5580 | ±1.1160 | +0.404 | 0.6865 |  |
| Site: UCSD (vs UAB) | -0.5016 | 0.3972 | ±0.7944 | -1.263 | 0.2066 |  |
| **Site: UW (vs UAB)** | **-1.9336** | 0.4746 | ±0.9492 | **-4.074** | **4.62e-05** | *** |
| Season: spring (vs autumn) | -0.7997 | 0.4550 | ±0.9100 | -1.758 | 0.0788 | . |
| Season: summer (vs autumn) | +0.7426 | 0.5264 | ±1.0527 | +1.411 | 0.1583 |  |
| **Season: winter (vs autumn)** | **-2.2970** | 0.5050 | ±1.0101 | **-4.548** | **5.41e-06** | *** |
| Age (years) | -0.0123 | 0.0155 | ±0.0310 | -0.795 | 0.4269 |  |
| BMI (kg/m2) | +0.0021 | 0.0240 | ±0.0479 | +0.086 | 0.9312 |  |
| Hypertension | +0.5164 | 0.3884 | ±0.7768 | +1.329 | 0.1837 |  |
| High cholesterol | +0.0185 | 0.3329 | ±0.6658 | +0.056 | 0.9557 |  |
| Kidney disease | +0.2011 | 0.4591 | ±0.9181 | +0.438 | 0.6613 |  |
| Circulatory disease | +0.0378 | 0.4603 | ±0.9206 | +0.082 | 0.9346 |  |
| Mean glucose (mg/dL) | -0.0124 | 0.0131 | ±0.0262 | -0.945 | 0.3446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **198**, R² = **0.3017**, Adj R² = **0.2483**, F-statistic = **5.65** (p = **4.82e-09**), Residual SE = **2.178** on **183** df, AIC = **884.5**, BIC = **933.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.8283** | 3.6091 | ±7.2181 | **+8.265** | **1.40e-16** | *** |
| Education: graduate level (vs college) | -0.2081 | 0.3457 | ±0.6914 | -0.602 | 0.5471 |  |
| Education: high school or below (vs college) | +0.2252 | 0.5580 | ±1.1160 | +0.404 | 0.6865 |  |
| Site: UCSD (vs UAB) | -0.5016 | 0.3972 | ±0.7944 | -1.263 | 0.2066 |  |
| **Site: UW (vs UAB)** | **-1.9336** | 0.4746 | ±0.9492 | **-4.074** | **4.62e-05** | *** |
| Season: spring (vs autumn) | -0.7997 | 0.4550 | ±0.9100 | -1.758 | 0.0788 | . |
| Season: summer (vs autumn) | +0.7426 | 0.5264 | ±1.0527 | +1.411 | 0.1583 |  |
| **Season: winter (vs autumn)** | **-2.2970** | 0.5050 | ±1.0101 | **-4.548** | **5.41e-06** | *** |
| Age (years) | -0.0123 | 0.0155 | ±0.0310 | -0.795 | 0.4269 |  |
| BMI (kg/m2) | +0.0021 | 0.0240 | ±0.0479 | +0.086 | 0.9312 |  |
| Hypertension | +0.5164 | 0.3884 | ±0.7768 | +1.329 | 0.1837 |  |
| High cholesterol | +0.0185 | 0.3329 | ±0.6658 | +0.056 | 0.9557 |  |
| Kidney disease | +0.2011 | 0.4591 | ±0.9181 | +0.438 | 0.6613 |  |
| Circulatory disease | +0.0378 | 0.4603 | ±0.9206 | +0.082 | 0.9346 |  |
| GMI (%) | -0.5173 | 0.5473 | ±1.0946 | -0.945 | 0.3446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **198**, R² = **0.3051**, Adj R² = **0.2520**, F-statistic = **5.74** (p = **3.29e-09**), Residual SE = **2.172** on **183** df, AIC = **883.5**, BIC = **932.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5052** | 2.0048 | ±4.0095 | **+14.219** | **7.02e-46** | *** |
| Education: graduate level (vs college) | -0.1918 | 0.3459 | ±0.6917 | -0.555 | 0.5791 |  |
| Education: high school or below (vs college) | +0.2277 | 0.5616 | ±1.1233 | +0.405 | 0.6852 |  |
| Site: UCSD (vs UAB) | -0.4888 | 0.3961 | ±0.7921 | -1.234 | 0.2171 |  |
| **Site: UW (vs UAB)** | **-1.9253** | 0.4706 | ±0.9412 | **-4.091** | **4.29e-05** | *** |
| Season: spring (vs autumn) | -0.8086 | 0.4521 | ±0.9042 | -1.789 | 0.0737 | . |
| Season: summer (vs autumn) | +0.7420 | 0.5229 | ±1.0459 | +1.419 | 0.1559 |  |
| **Season: winter (vs autumn)** | **-2.3153** | 0.5024 | ±1.0048 | **-4.608** | **4.06e-06** | *** |
| Age (years) | -0.0142 | 0.0154 | ±0.0309 | -0.918 | 0.3584 |  |
| BMI (kg/m2) | +0.0037 | 0.0239 | ±0.0479 | +0.156 | 0.8757 |  |
| Hypertension | +0.5059 | 0.3898 | ±0.7796 | +1.298 | 0.1943 |  |
| High cholesterol | +0.0372 | 0.3310 | ±0.6620 | +0.113 | 0.9104 |  |
| Kidney disease | +0.1699 | 0.4560 | ±0.9120 | +0.373 | 0.7094 |  |
| Circulatory disease | +0.0596 | 0.4599 | ±0.9197 | +0.130 | 0.8969 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0151 | 0.0113 | ±0.0227 | -1.328 | 0.1840 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **198**, R² = **0.2980**, Adj R² = **0.2443**, F-statistic = **5.55** (p = **7.31e-09**), Residual SE = **2.184** on **183** df, AIC = **885.6**, BIC = **934.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6698** | 1.8937 | ±3.7874 | **+14.083** | **4.81e-45** | *** |
| Education: graduate level (vs college) | -0.2065 | 0.3475 | ±0.6949 | -0.594 | 0.5522 |  |
| Education: high school or below (vs college) | +0.2618 | 0.5626 | ±1.1253 | +0.465 | 0.6416 |  |
| Site: UCSD (vs UAB) | -0.5015 | 0.3986 | ±0.7971 | -1.258 | 0.2083 |  |
| **Site: UW (vs UAB)** | **-1.9251** | 0.4789 | ±0.9578 | **-4.020** | **5.82e-05** | *** |
| Season: spring (vs autumn) | -0.8119 | 0.4554 | ±0.9109 | -1.783 | 0.0746 | . |
| Season: summer (vs autumn) | +0.6942 | 0.5169 | ±1.0338 | +1.343 | 0.1792 |  |
| **Season: winter (vs autumn)** | **-2.3176** | 0.5022 | ±1.0043 | **-4.615** | **3.93e-06** | *** |
| Age (years) | -0.0120 | 0.0151 | ±0.0302 | -0.792 | 0.4283 |  |
| BMI (kg/m2) | +0.0001 | 0.0239 | ±0.0477 | +0.003 | 0.9977 |  |
| Hypertension | +0.5000 | 0.3906 | ±0.7812 | +1.280 | 0.2005 |  |
| High cholesterol | +0.0290 | 0.3325 | ±0.6650 | +0.087 | 0.9304 |  |
| Kidney disease | +0.1689 | 0.4752 | ±0.9505 | +0.355 | 0.7223 |  |
| Circulatory disease | +0.0219 | 0.4629 | ±0.9258 | +0.047 | 0.9622 |  |
| Glucose SD, pooled (mg/dL) | -0.0028 | 0.0355 | ±0.0709 | -0.080 | 0.9362 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **198**, R² = **0.2982**, Adj R² = **0.2445**, F-statistic = **5.55** (p = **7.17e-09**), Residual SE = **2.183** on **183** df, AIC = **885.5**, BIC = **934.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.4724** | 1.8634 | ±3.7268 | **+14.206** | **8.36e-46** | *** |
| Education: graduate level (vs college) | -0.2127 | 0.3465 | ±0.6930 | -0.614 | 0.5393 |  |
| Education: high school or below (vs college) | +0.2381 | 0.5614 | ±1.1229 | +0.424 | 0.6716 |  |
| Site: UCSD (vs UAB) | -0.4964 | 0.3974 | ±0.7948 | -1.249 | 0.2116 |  |
| **Site: UW (vs UAB)** | **-1.9101** | 0.4755 | ±0.9511 | **-4.017** | **5.90e-05** | *** |
| Season: spring (vs autumn) | -0.8086 | 0.4577 | ±0.9154 | -1.767 | 0.0773 | . |
| Season: summer (vs autumn) | +0.6983 | 0.5188 | ±1.0377 | +1.346 | 0.1783 |  |
| **Season: winter (vs autumn)** | **-2.3155** | 0.5040 | ±1.0081 | **-4.594** | **4.35e-06** | *** |
| Age (years) | -0.0124 | 0.0151 | ±0.0303 | -0.818 | 0.4134 |  |
| BMI (kg/m2) | +0.0002 | 0.0238 | ±0.0476 | +0.008 | 0.9940 |  |
| Hypertension | +0.4790 | 0.3884 | ±0.7768 | +1.233 | 0.2175 |  |
| High cholesterol | +0.0366 | 0.3328 | ±0.6655 | +0.110 | 0.9124 |  |
| Kidney disease | +0.1516 | 0.4741 | ±0.9482 | +0.320 | 0.7492 |  |
| Circulatory disease | +0.0181 | 0.4627 | ±0.9253 | +0.039 | 0.9687 |  |
| Avg. daily SD (mg/dL) | +0.0082 | 0.0352 | ±0.0703 | +0.233 | 0.8161 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **198**, R² = **0.2991**, Adj R² = **0.2454**, F-statistic = **5.58** (p = **6.48e-09**), Residual SE = **2.182** on **183** df, AIC = **885.3**, BIC = **934.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.1569** | 2.0819 | ±4.1637 | **+12.564** | **3.32e-36** | *** |
| Education: graduate level (vs college) | -0.2222 | 0.3445 | ±0.6891 | -0.645 | 0.5190 |  |
| Education: high school or below (vs college) | +0.1859 | 0.5684 | ±1.1368 | +0.327 | 0.7436 |  |
| Site: UCSD (vs UAB) | -0.4788 | 0.3965 | ±0.7930 | -1.208 | 0.2272 |  |
| **Site: UW (vs UAB)** | **-1.8839** | 0.4738 | ±0.9476 | **-3.976** | **7.00e-05** | *** |
| Season: spring (vs autumn) | -0.8075 | 0.4574 | ±0.9148 | -1.765 | 0.0775 | . |
| Season: summer (vs autumn) | +0.7119 | 0.5226 | ±1.0453 | +1.362 | 0.1732 |  |
| **Season: winter (vs autumn)** | **-2.3127** | 0.5050 | ±1.0100 | **-4.580** | **4.65e-06** | *** |
| Age (years) | -0.0130 | 0.0150 | ±0.0301 | -0.865 | 0.3872 |  |
| BMI (kg/m2) | +0.0009 | 0.0241 | ±0.0481 | +0.038 | 0.9697 |  |
| Hypertension | +0.4644 | 0.3932 | ±0.7864 | +1.181 | 0.2375 |  |
| High cholesterol | +0.0423 | 0.3329 | ±0.6657 | +0.127 | 0.8989 |  |
| Kidney disease | +0.1278 | 0.4796 | ±0.9592 | +0.266 | 0.7899 |  |
| Circulatory disease | +0.0113 | 0.4633 | ±0.9267 | +0.024 | 0.9806 |  |
| CV (%) | +0.0289 | 0.0583 | ±0.1166 | +0.496 | 0.6197 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **198**, R² = **0.2987**, Adj R² = **0.2451**, F-statistic = **5.57** (p = **6.75e-09**), Residual SE = **2.182** on **183** df, AIC = **885.4**, BIC = **934.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.0366** | 1.6536 | ±3.3071 | **+16.351** | **4.30e-60** | *** |
| Education: graduate level (vs college) | -0.2175 | 0.3442 | ±0.6883 | -0.632 | 0.5274 |  |
| Education: high school or below (vs college) | +0.2051 | 0.5637 | ±1.1274 | +0.364 | 0.7160 |  |
| Site: UCSD (vs UAB) | -0.4863 | 0.3974 | ±0.7949 | -1.224 | 0.2211 |  |
| **Site: UW (vs UAB)** | **-1.8942** | 0.4702 | ±0.9403 | **-4.029** | **5.60e-05** | *** |
| Season: spring (vs autumn) | -0.8086 | 0.4588 | ±0.9176 | -1.763 | 0.0780 | . |
| Season: summer (vs autumn) | +0.7072 | 0.5252 | ±1.0504 | +1.346 | 0.1781 |  |
| **Season: winter (vs autumn)** | **-2.3151** | 0.5055 | ±1.0110 | **-4.580** | **4.65e-06** | *** |
| Age (years) | -0.0129 | 0.0150 | ±0.0300 | -0.856 | 0.3920 |  |
| BMI (kg/m2) | +0.0003 | 0.0240 | ±0.0479 | +0.014 | 0.9891 |  |
| Hypertension | +0.4687 | 0.3903 | ±0.7806 | +1.201 | 0.2298 |  |
| High cholesterol | +0.0370 | 0.3342 | ±0.6683 | +0.111 | 0.9118 |  |
| Kidney disease | +0.1354 | 0.4813 | ±0.9627 | +0.281 | 0.7785 |  |
| Circulatory disease | +0.0171 | 0.4645 | ±0.9290 | +0.037 | 0.9707 |  |
| Mean / SD ratio | -0.0615 | 0.1747 | ±0.3494 | -0.352 | 0.7247 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **198**, R² = **0.2995**, Adj R² = **0.2459**, F-statistic = **5.59** (p = **6.20e-09**), Residual SE = **2.181** on **183** df, AIC = **885.1**, BIC = **934.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.1629** | 1.6414 | ±3.2828 | **+16.549** | **1.63e-61** | *** |
| Education: graduate level (vs college) | -0.2150 | 0.3455 | ±0.6911 | -0.622 | 0.5338 |  |
| Education: high school or below (vs college) | +0.2002 | 0.5621 | ±1.1241 | +0.356 | 0.7217 |  |
| Site: UCSD (vs UAB) | -0.5008 | 0.3957 | ±0.7915 | -1.265 | 0.2057 |  |
| **Site: UW (vs UAB)** | **-1.8946** | 0.4682 | ±0.9364 | **-4.047** | **5.19e-05** | *** |
| Season: spring (vs autumn) | -0.8039 | 0.4616 | ±0.9233 | -1.741 | 0.0816 | . |
| Season: summer (vs autumn) | +0.7175 | 0.5310 | ±1.0620 | +1.351 | 0.1766 |  |
| **Season: winter (vs autumn)** | **-2.3053** | 0.5123 | ±1.0247 | **-4.499** | **6.81e-06** | *** |
| Age (years) | -0.0133 | 0.0150 | ±0.0301 | -0.882 | 0.3779 |  |
| BMI (kg/m2) | +0.0003 | 0.0239 | ±0.0479 | +0.012 | 0.9905 |  |
| Hypertension | +0.4451 | 0.3903 | ±0.7806 | +1.140 | 0.2542 |  |
| High cholesterol | +0.0349 | 0.3351 | ±0.6701 | +0.104 | 0.9169 |  |
| Kidney disease | +0.1351 | 0.4775 | ±0.9550 | +0.283 | 0.7772 |  |
| Circulatory disease | +0.0337 | 0.4687 | ±0.9373 | +0.072 | 0.9426 |  |
| Avg. daily mean/SD | -0.0671 | 0.1461 | ±0.2922 | -0.459 | 0.6461 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **198**, R² = **0.2991**, Adj R² = **0.2455**, F-statistic = **5.58** (p = **6.46e-09**), Residual SE = **2.182** on **183** df, AIC = **885.3**, BIC = **934.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.0861** | 2.1094 | ±4.2188 | **+12.841** | **9.72e-38** | *** |
| Education: graduate level (vs college) | -0.2050 | 0.3473 | ±0.6947 | -0.590 | 0.5551 |  |
| Education: high school or below (vs college) | +0.2771 | 0.5659 | ±1.1317 | +0.490 | 0.6243 |  |
| Site: UCSD (vs UAB) | -0.4981 | 0.3974 | ±0.7947 | -1.254 | 0.2100 |  |
| **Site: UW (vs UAB)** | **-1.9319** | 0.4695 | ±0.9390 | **-4.115** | **3.88e-05** | *** |
| Season: spring (vs autumn) | -0.8155 | 0.4578 | ±0.9156 | -1.782 | 0.0748 | . |
| Season: summer (vs autumn) | +0.6911 | 0.5196 | ±1.0392 | +1.330 | 0.1835 |  |
| **Season: winter (vs autumn)** | **-2.3233** | 0.5043 | ±1.0086 | **-4.607** | **4.08e-06** | *** |
| Age (years) | -0.0123 | 0.0154 | ±0.0307 | -0.801 | 0.4231 |  |
| BMI (kg/m2) | +0.0005 | 0.0236 | ±0.0473 | +0.023 | 0.9819 |  |
| Hypertension | +0.5072 | 0.3832 | ±0.7664 | +1.324 | 0.1856 |  |
| High cholesterol | +0.0388 | 0.3372 | ±0.6745 | +0.115 | 0.9085 |  |
| Kidney disease | +0.1619 | 0.4657 | ±0.9314 | +0.348 | 0.7280 |  |
| Circulatory disease | +0.0049 | 0.4626 | ±0.9251 | +0.011 | 0.9915 |  |
| MAG (mg/dL/h) | -0.0132 | 0.0271 | ±0.0541 | -0.486 | 0.6267 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **198**, R² = **0.2980**, Adj R² = **0.2443**, F-statistic = **5.55** (p = **7.33e-09**), Residual SE = **2.184** on **183** df, AIC = **885.6**, BIC = **934.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6091** | 2.0042 | ±4.0083 | **+13.277** | **3.15e-40** | *** |
| Education: graduate level (vs college) | -0.2084 | 0.3469 | ±0.6938 | -0.601 | 0.5480 |  |
| Education: high school or below (vs college) | +0.2543 | 0.5640 | ±1.1280 | +0.451 | 0.6521 |  |
| Site: UCSD (vs UAB) | -0.4988 | 0.3978 | ±0.7956 | -1.254 | 0.2099 |  |
| **Site: UW (vs UAB)** | **-1.9198** | 0.4747 | ±0.9494 | **-4.044** | **5.25e-05** | *** |
| Season: spring (vs autumn) | -0.8117 | 0.4568 | ±0.9136 | -1.777 | 0.0756 | . |
| Season: summer (vs autumn) | +0.6947 | 0.5204 | ±1.0409 | +1.335 | 0.1819 |  |
| **Season: winter (vs autumn)** | **-2.3174** | 0.5052 | ±1.0104 | **-4.587** | **4.49e-06** | *** |
| Age (years) | -0.0121 | 0.0151 | ±0.0302 | -0.802 | 0.4227 |  |
| BMI (kg/m2) | +0.0001 | 0.0242 | ±0.0484 | +0.004 | 0.9965 |  |
| Hypertension | +0.4950 | 0.3846 | ±0.7693 | +1.287 | 0.1982 |  |
| High cholesterol | +0.0310 | 0.3339 | ±0.6678 | +0.093 | 0.9260 |  |
| Kidney disease | +0.1629 | 0.4709 | ±0.9418 | +0.346 | 0.7293 |  |
| Circulatory disease | +0.0199 | 0.4614 | ±0.9228 | +0.043 | 0.9656 |  |
| Avg. daily range (mg/dL) | +0.0001 | 0.0088 | ±0.0176 | +0.007 | 0.9941 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **198**, R² = **0.3067**, Adj R² = **0.2537**, F-statistic = **5.78** (p = **2.75e-09**), Residual SE = **2.170** on **183** df, AIC = **883.1**, BIC = **932.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+27.2280** | 1.6562 | ±3.3123 | **+16.440** | **9.82e-61** | *** |
| Education: graduate level (vs college) | -0.1791 | 0.3435 | ±0.6870 | -0.521 | 0.6020 |  |
| Education: high school or below (vs college) | +0.3905 | 0.5661 | ±1.1322 | +0.690 | 0.4904 |  |
| Site: UCSD (vs UAB) | -0.6040 | 0.3999 | ±0.7998 | -1.510 | 0.1310 |  |
| **Site: UW (vs UAB)** | **-2.0407** | 0.4731 | ±0.9461 | **-4.314** | **1.61e-05** | *** |
| Season: spring (vs autumn) | -0.7646 | 0.4474 | ±0.8948 | -1.709 | 0.0874 | . |
| Season: summer (vs autumn) | +0.7883 | 0.5229 | ±1.0457 | +1.508 | 0.1316 |  |
| **Season: winter (vs autumn)** | **-2.3117** | 0.4971 | ±0.9942 | **-4.650** | **3.32e-06** | *** |
| Age (years) | -0.0115 | 0.0150 | ±0.0299 | -0.767 | 0.4432 |  |
| BMI (kg/m2) | +0.0004 | 0.0237 | ±0.0475 | +0.017 | 0.9864 |  |
| Hypertension | +0.4534 | 0.3786 | ±0.7572 | +1.198 | 0.2311 |  |
| High cholesterol | +0.0459 | 0.3355 | ±0.6710 | +0.137 | 0.8911 |  |
| Kidney disease | +0.2951 | 0.4803 | ±0.9606 | +0.614 | 0.5389 |  |
| Circulatory disease | +0.1585 | 0.4723 | ±0.9445 | +0.336 | 0.7372 |  |
| SD of daily means (mg/dL) | -0.1016 | 0.0723 | ±0.1447 | -1.404 | 0.1602 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **198**, R² = **0.2993**, Adj R² = **0.2457**, F-statistic = **5.58** (p = **6.32e-09**), Residual SE = **2.182** on **183** df, AIC = **885.2**, BIC = **934.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5796** | 3.7379 | ±7.4758 | **+6.576** | **4.84e-11** | *** |
| Education: graduate level (vs college) | -0.1962 | 0.3492 | ±0.6983 | -0.562 | 0.5741 |  |
| Education: high school or below (vs college) | +0.2804 | 0.5621 | ±1.1242 | +0.499 | 0.6179 |  |
| Site: UCSD (vs UAB) | -0.5171 | 0.3989 | ±0.7979 | -1.296 | 0.1949 |  |
| **Site: UW (vs UAB)** | **-1.9388** | 0.4775 | ±0.9549 | **-4.061** | **4.89e-05** | *** |
| Season: spring (vs autumn) | -0.8140 | 0.4530 | ±0.9061 | -1.797 | 0.0724 | . |
| Season: summer (vs autumn) | +0.7092 | 0.5164 | ±1.0328 | +1.373 | 0.1697 |  |
| **Season: winter (vs autumn)** | **-2.3094** | 0.5006 | ±1.0011 | **-4.614** | **3.96e-06** | *** |
| Age (years) | -0.0111 | 0.0155 | ±0.0309 | -0.715 | 0.4745 |  |
| BMI (kg/m2) | +0.0004 | 0.0238 | ±0.0476 | +0.017 | 0.9861 |  |
| Hypertension | +0.5069 | 0.3876 | ±0.7751 | +1.308 | 0.1909 |  |
| High cholesterol | +0.0189 | 0.3323 | ±0.6647 | +0.057 | 0.9547 |  |
| Kidney disease | +0.2047 | 0.4616 | ±0.9232 | +0.443 | 0.6574 |  |
| Circulatory disease | +0.0314 | 0.4604 | ±0.9207 | +0.068 | 0.9457 |  |
| Time in range 70-180, pooled (%) | +0.0204 | 0.0342 | ±0.0683 | +0.596 | 0.5511 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **198**, R² = **0.2995**, Adj R² = **0.2459**, F-statistic = **5.59** (p = **6.19e-09**), Residual SE = **2.181** on **183** df, AIC = **885.1**, BIC = **934.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3922** | 3.8625 | ±7.7249 | **+6.315** | **2.70e-10** | *** |
| Education: graduate level (vs college) | -0.1967 | 0.3487 | ±0.6975 | -0.564 | 0.5727 |  |
| Education: high school or below (vs college) | +0.2776 | 0.5605 | ±1.1209 | +0.495 | 0.6204 |  |
| Site: UCSD (vs UAB) | -0.5184 | 0.3989 | ±0.7979 | -1.299 | 0.1938 |  |
| **Site: UW (vs UAB)** | **-1.9363** | 0.4768 | ±0.9536 | **-4.061** | **4.88e-05** | *** |
| Season: spring (vs autumn) | -0.8154 | 0.4529 | ±0.9058 | -1.800 | 0.0718 | . |
| Season: summer (vs autumn) | +0.7109 | 0.5161 | ±1.0322 | +1.378 | 0.1683 |  |
| **Season: winter (vs autumn)** | **-2.3083** | 0.5004 | ±1.0008 | **-4.613** | **3.97e-06** | *** |
| Age (years) | -0.0109 | 0.0154 | ±0.0309 | -0.709 | 0.4785 |  |
| BMI (kg/m2) | +0.0003 | 0.0238 | ±0.0476 | +0.013 | 0.9899 |  |
| Hypertension | +0.5108 | 0.3878 | ±0.7756 | +1.317 | 0.1878 |  |
| High cholesterol | +0.0189 | 0.3321 | ±0.6642 | +0.057 | 0.9546 |  |
| Kidney disease | +0.2085 | 0.4605 | ±0.9211 | +0.453 | 0.6507 |  |
| Circulatory disease | +0.0317 | 0.4603 | ±0.9207 | +0.069 | 0.9452 |  |
| Avg. daily time in range 70-180 (%) | +0.0222 | 0.0357 | ±0.0715 | +0.622 | 0.5340 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **198**, R² = **0.3035**, Adj R² = **0.2502**, F-statistic = **5.69** (p = **3.97e-09**), Residual SE = **2.175** on **183** df, AIC = **884.0**, BIC = **933.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.5634** | 1.5946 | ±3.1891 | **+16.659** | **2.61e-62** | *** |
| Education: graduate level (vs college) | -0.1820 | 0.3449 | ±0.6898 | -0.528 | 0.5977 |  |
| Education: high school or below (vs college) | +0.3393 | 0.5618 | ±1.1235 | +0.604 | 0.5458 |  |
| Site: UCSD (vs UAB) | -0.5329 | 0.3951 | ±0.7903 | -1.349 | 0.1775 |  |
| **Site: UW (vs UAB)** | **-1.9298** | 0.4703 | ±0.9406 | **-4.103** | **4.07e-05** | *** |
| Season: spring (vs autumn) | -0.8633 | 0.4635 | ±0.9270 | -1.863 | 0.0625 | . |
| Season: summer (vs autumn) | +0.6650 | 0.5169 | ±1.0338 | +1.286 | 0.1983 |  |
| **Season: winter (vs autumn)** | **-2.3751** | 0.5073 | ±1.0146 | **-4.682** | **2.84e-06** | *** |
| Age (years) | -0.0090 | 0.0151 | ±0.0301 | -0.599 | 0.5494 |  |
| BMI (kg/m2) | -0.0014 | 0.0237 | ±0.0475 | -0.060 | 0.9519 |  |
| Hypertension | +0.5134 | 0.3829 | ±0.7657 | +1.341 | 0.1800 |  |
| High cholesterol | +0.0557 | 0.3376 | ±0.6752 | +0.165 | 0.8689 |  |
| Kidney disease | +0.1344 | 0.4663 | ±0.9327 | +0.288 | 0.7733 |  |
| Circulatory disease | +0.0231 | 0.4609 | ±0.9218 | +0.050 | 0.9601 |  |
| Time 54-69, pooled (%) | -0.7097 | 0.5364 | ±1.0727 | -1.323 | 0.1858 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **198**, R² = **0.3007**, Adj R² = **0.2472**, F-statistic = **5.62** (p = **5.38e-09**), Residual SE = **2.179** on **183** df, AIC = **884.8**, BIC = **934.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.5572** | 1.5939 | ±3.1878 | **+16.662** | **2.50e-62** | *** |
| Education: graduate level (vs college) | -0.1903 | 0.3449 | ±0.6898 | -0.552 | 0.5812 |  |
| Education: high school or below (vs college) | +0.3126 | 0.5616 | ±1.1231 | +0.557 | 0.5777 |  |
| Site: UCSD (vs UAB) | -0.5114 | 0.3963 | ±0.7925 | -1.291 | 0.1969 |  |
| **Site: UW (vs UAB)** | **-1.9178** | 0.4709 | ±0.9417 | **-4.073** | **4.64e-05** | *** |
| Season: spring (vs autumn) | -0.8488 | 0.4660 | ±0.9321 | -1.821 | 0.0686 | . |
| Season: summer (vs autumn) | +0.6612 | 0.5209 | ±1.0417 | +1.269 | 0.2043 |  |
| **Season: winter (vs autumn)** | **-2.3565** | 0.5092 | ±1.0184 | **-4.628** | **3.70e-06** | *** |
| Age (years) | -0.0098 | 0.0151 | ±0.0303 | -0.646 | 0.5186 |  |
| BMI (kg/m2) | -0.0009 | 0.0238 | ±0.0475 | -0.039 | 0.9692 |  |
| Hypertension | +0.5149 | 0.3856 | ±0.7713 | +1.335 | 0.1818 |  |
| High cholesterol | +0.0484 | 0.3386 | ±0.6773 | +0.143 | 0.8864 |  |
| Kidney disease | +0.1349 | 0.4688 | ±0.9375 | +0.288 | 0.7735 |  |
| Circulatory disease | +0.0100 | 0.4612 | ±0.9224 | +0.022 | 0.9827 |  |
| Avg. daily time 54-69 (%) | -0.4909 | 0.5074 | ±1.0147 | -0.967 | 0.3333 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **198**, R² = **0.3035**, Adj R² = **0.2502**, F-statistic = **5.69** (p = **3.97e-09**), Residual SE = **2.175** on **183** df, AIC = **884.0**, BIC = **933.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.5634** | 1.5946 | ±3.1891 | **+16.659** | **2.61e-62** | *** |
| Education: graduate level (vs college) | -0.1820 | 0.3449 | ±0.6898 | -0.528 | 0.5977 |  |
| Education: high school or below (vs college) | +0.3393 | 0.5618 | ±1.1235 | +0.604 | 0.5458 |  |
| Site: UCSD (vs UAB) | -0.5329 | 0.3951 | ±0.7903 | -1.349 | 0.1775 |  |
| **Site: UW (vs UAB)** | **-1.9298** | 0.4703 | ±0.9406 | **-4.103** | **4.07e-05** | *** |
| Season: spring (vs autumn) | -0.8633 | 0.4635 | ±0.9270 | -1.863 | 0.0625 | . |
| Season: summer (vs autumn) | +0.6650 | 0.5169 | ±1.0338 | +1.286 | 0.1983 |  |
| **Season: winter (vs autumn)** | **-2.3751** | 0.5073 | ±1.0146 | **-4.682** | **2.84e-06** | *** |
| Age (years) | -0.0090 | 0.0151 | ±0.0301 | -0.599 | 0.5494 |  |
| BMI (kg/m2) | -0.0014 | 0.0237 | ±0.0475 | -0.060 | 0.9519 |  |
| Hypertension | +0.5134 | 0.3829 | ±0.7657 | +1.341 | 0.1800 |  |
| High cholesterol | +0.0557 | 0.3376 | ±0.6752 | +0.165 | 0.8689 |  |
| Kidney disease | +0.1344 | 0.4663 | ±0.9327 | +0.288 | 0.7733 |  |
| Circulatory disease | +0.0231 | 0.4609 | ±0.9218 | +0.050 | 0.9601 |  |
| Time < 70 (%) | -0.7097 | 0.5364 | ±1.0727 | -1.323 | 0.1858 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **198**, R² = **0.3007**, Adj R² = **0.2472**, F-statistic = **5.62** (p = **5.38e-09**), Residual SE = **2.179** on **183** df, AIC = **884.8**, BIC = **934.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.5572** | 1.5939 | ±3.1878 | **+16.662** | **2.50e-62** | *** |
| Education: graduate level (vs college) | -0.1903 | 0.3449 | ±0.6898 | -0.552 | 0.5812 |  |
| Education: high school or below (vs college) | +0.3126 | 0.5616 | ±1.1231 | +0.557 | 0.5777 |  |
| Site: UCSD (vs UAB) | -0.5114 | 0.3963 | ±0.7925 | -1.291 | 0.1969 |  |
| **Site: UW (vs UAB)** | **-1.9178** | 0.4709 | ±0.9417 | **-4.073** | **4.64e-05** | *** |
| Season: spring (vs autumn) | -0.8488 | 0.4660 | ±0.9321 | -1.821 | 0.0686 | . |
| Season: summer (vs autumn) | +0.6612 | 0.5209 | ±1.0417 | +1.269 | 0.2043 |  |
| **Season: winter (vs autumn)** | **-2.3565** | 0.5092 | ±1.0184 | **-4.628** | **3.70e-06** | *** |
| Age (years) | -0.0098 | 0.0151 | ±0.0303 | -0.646 | 0.5186 |  |
| BMI (kg/m2) | -0.0009 | 0.0238 | ±0.0475 | -0.039 | 0.9692 |  |
| Hypertension | +0.5149 | 0.3856 | ±0.7713 | +1.335 | 0.1818 |  |
| High cholesterol | +0.0484 | 0.3386 | ±0.6773 | +0.143 | 0.8864 |  |
| Kidney disease | +0.1349 | 0.4688 | ±0.9375 | +0.288 | 0.7735 |  |
| Circulatory disease | +0.0100 | 0.4612 | ±0.9224 | +0.022 | 0.9827 |  |
| Avg. daily time < 70 (%) | -0.4909 | 0.5074 | ±1.0147 | -0.967 | 0.3333 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **198**, R² = **0.2990**, Adj R² = **0.2454**, F-statistic = **5.58** (p = **6.54e-09**), Residual SE = **2.182** on **183** df, AIC = **885.3**, BIC = **934.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6176** | 1.6134 | ±3.2268 | **+16.498** | **3.79e-61** | *** |
| Education: graduate level (vs college) | -0.1985 | 0.3489 | ±0.6978 | -0.569 | 0.5695 |  |
| Education: high school or below (vs college) | +0.2749 | 0.5623 | ±1.1245 | +0.489 | 0.6248 |  |
| Site: UCSD (vs UAB) | -0.5139 | 0.3988 | ±0.7976 | -1.289 | 0.1976 |  |
| **Site: UW (vs UAB)** | **-1.9361** | 0.4773 | ±0.9547 | **-4.056** | **4.99e-05** | *** |
| Season: spring (vs autumn) | -0.8124 | 0.4531 | ±0.9062 | -1.793 | 0.0730 | . |
| Season: summer (vs autumn) | +0.7080 | 0.5168 | ±1.0336 | +1.370 | 0.1707 |  |
| **Season: winter (vs autumn)** | **-2.3090** | 0.5008 | ±1.0016 | **-4.610** | **4.02e-06** | *** |
| Age (years) | -0.0113 | 0.0154 | ±0.0309 | -0.729 | 0.4660 |  |
| BMI (kg/m2) | +0.0004 | 0.0238 | ±0.0476 | +0.017 | 0.9862 |  |
| Hypertension | +0.5050 | 0.3871 | ±0.7742 | +1.305 | 0.1920 |  |
| High cholesterol | +0.0198 | 0.3326 | ±0.6653 | +0.060 | 0.9525 |  |
| Kidney disease | +0.2000 | 0.4632 | ±0.9265 | +0.432 | 0.6659 |  |
| Circulatory disease | +0.0298 | 0.4607 | ±0.9214 | +0.065 | 0.9484 |  |
| Time 181-250, pooled (%) | -0.0177 | 0.0336 | ±0.0673 | -0.527 | 0.5985 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **198**, R² = **0.2992**, Adj R² = **0.2456**, F-statistic = **5.58** (p = **6.37e-09**), Residual SE = **2.182** on **183** df, AIC = **885.2**, BIC = **934.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6173** | 1.6129 | ±3.2258 | **+16.503** | **3.51e-61** | *** |
| Education: graduate level (vs college) | -0.1986 | 0.3485 | ±0.6971 | -0.570 | 0.5688 |  |
| Education: high school or below (vs college) | +0.2730 | 0.5608 | ±1.1216 | +0.487 | 0.6264 |  |
| Site: UCSD (vs UAB) | -0.5159 | 0.3989 | ±0.7978 | -1.293 | 0.1959 |  |
| **Site: UW (vs UAB)** | **-1.9348** | 0.4768 | ±0.9536 | **-4.058** | **4.95e-05** | *** |
| Season: spring (vs autumn) | -0.8135 | 0.4528 | ±0.9057 | -1.796 | 0.0724 | . |
| Season: summer (vs autumn) | +0.7107 | 0.5165 | ±1.0330 | +1.376 | 0.1688 |  |
| **Season: winter (vs autumn)** | **-2.3076** | 0.5006 | ±1.0012 | **-4.610** | **4.03e-06** | *** |
| Age (years) | -0.0112 | 0.0154 | ±0.0309 | -0.722 | 0.4702 |  |
| BMI (kg/m2) | +0.0003 | 0.0238 | ±0.0476 | +0.014 | 0.9892 |  |
| Hypertension | +0.5085 | 0.3873 | ±0.7746 | +1.313 | 0.1892 |  |
| High cholesterol | +0.0194 | 0.3324 | ±0.6647 | +0.058 | 0.9535 |  |
| Kidney disease | +0.2052 | 0.4620 | ±0.9241 | +0.444 | 0.6570 |  |
| Circulatory disease | +0.0309 | 0.4607 | ±0.9214 | +0.067 | 0.9465 |  |
| Avg. daily time 181-250 (%) | -0.0200 | 0.0352 | ±0.0704 | -0.569 | 0.5694 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **198**, R² = **0.2990**, Adj R² = **0.2454**, F-statistic = **5.58** (p = **6.54e-09**), Residual SE = **2.182** on **183** df, AIC = **885.3**, BIC = **934.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6176** | 1.6134 | ±3.2268 | **+16.498** | **3.79e-61** | *** |
| Education: graduate level (vs college) | -0.1985 | 0.3489 | ±0.6978 | -0.569 | 0.5695 |  |
| Education: high school or below (vs college) | +0.2749 | 0.5623 | ±1.1245 | +0.489 | 0.6248 |  |
| Site: UCSD (vs UAB) | -0.5139 | 0.3988 | ±0.7976 | -1.289 | 0.1976 |  |
| **Site: UW (vs UAB)** | **-1.9361** | 0.4773 | ±0.9547 | **-4.056** | **4.99e-05** | *** |
| Season: spring (vs autumn) | -0.8124 | 0.4531 | ±0.9062 | -1.793 | 0.0730 | . |
| Season: summer (vs autumn) | +0.7080 | 0.5168 | ±1.0336 | +1.370 | 0.1707 |  |
| **Season: winter (vs autumn)** | **-2.3090** | 0.5008 | ±1.0016 | **-4.610** | **4.02e-06** | *** |
| Age (years) | -0.0113 | 0.0154 | ±0.0309 | -0.729 | 0.4660 |  |
| BMI (kg/m2) | +0.0004 | 0.0238 | ±0.0476 | +0.017 | 0.9862 |  |
| Hypertension | +0.5050 | 0.3871 | ±0.7742 | +1.305 | 0.1920 |  |
| High cholesterol | +0.0198 | 0.3326 | ±0.6653 | +0.060 | 0.9525 |  |
| Kidney disease | +0.2000 | 0.4632 | ±0.9265 | +0.432 | 0.6659 |  |
| Circulatory disease | +0.0298 | 0.4607 | ±0.9214 | +0.065 | 0.9484 |  |
| Time > 180 (%) | -0.0177 | 0.0336 | ±0.0673 | -0.527 | 0.5985 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **198**, R² = **0.2992**, Adj R² = **0.2456**, F-statistic = **5.58** (p = **6.37e-09**), Residual SE = **2.182** on **183** df, AIC = **885.2**, BIC = **934.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6173** | 1.6129 | ±3.2258 | **+16.503** | **3.51e-61** | *** |
| Education: graduate level (vs college) | -0.1986 | 0.3485 | ±0.6971 | -0.570 | 0.5688 |  |
| Education: high school or below (vs college) | +0.2730 | 0.5608 | ±1.1216 | +0.487 | 0.6264 |  |
| Site: UCSD (vs UAB) | -0.5159 | 0.3989 | ±0.7978 | -1.293 | 0.1959 |  |
| **Site: UW (vs UAB)** | **-1.9348** | 0.4768 | ±0.9536 | **-4.058** | **4.95e-05** | *** |
| Season: spring (vs autumn) | -0.8135 | 0.4528 | ±0.9057 | -1.796 | 0.0724 | . |
| Season: summer (vs autumn) | +0.7107 | 0.5165 | ±1.0330 | +1.376 | 0.1688 |  |
| **Season: winter (vs autumn)** | **-2.3076** | 0.5006 | ±1.0012 | **-4.610** | **4.03e-06** | *** |
| Age (years) | -0.0112 | 0.0154 | ±0.0309 | -0.722 | 0.4702 |  |
| BMI (kg/m2) | +0.0003 | 0.0238 | ±0.0476 | +0.014 | 0.9892 |  |
| Hypertension | +0.5085 | 0.3873 | ±0.7746 | +1.313 | 0.1892 |  |
| High cholesterol | +0.0194 | 0.3324 | ±0.6647 | +0.058 | 0.9535 |  |
| Kidney disease | +0.2052 | 0.4620 | ±0.9241 | +0.444 | 0.6570 |  |
| Circulatory disease | +0.0309 | 0.4607 | ±0.9214 | +0.067 | 0.9465 |  |
| Avg. daily time > 180 (%) | -0.0200 | 0.0352 | ±0.0704 | -0.569 | 0.5694 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 198)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **198**, R² = **0.3017**, Adj R² = **0.2482**, F-statistic = **5.65** (p = **4.86e-09**), Residual SE = **2.178** on **183** df, AIC = **884.5**, BIC = **933.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.6055** | 1.6189 | ±3.2378 | **+16.434** | **1.09e-60** | *** |
| Education: graduate level (vs college) | -0.1992 | 0.3446 | ±0.6892 | -0.578 | 0.5633 |  |
| Education: high school or below (vs college) | +0.3216 | 0.5594 | ±1.1188 | +0.575 | 0.5653 |  |
| Site: UCSD (vs UAB) | -0.5544 | 0.4000 | ±0.8000 | -1.386 | 0.1657 |  |
| **Site: UW (vs UAB)** | **-1.9728** | 0.4743 | ±0.9487 | **-4.159** | **3.20e-05** | *** |
| Season: spring (vs autumn) | -0.7949 | 0.4518 | ±0.9037 | -1.759 | 0.0785 | . |
| Season: summer (vs autumn) | +0.7341 | 0.5172 | ±1.0344 | +1.419 | 0.1558 |  |
| **Season: winter (vs autumn)** | **-2.3068** | 0.4990 | ±0.9981 | **-4.623** | **3.79e-06** | *** |
| Age (years) | -0.0115 | 0.0155 | ±0.0309 | -0.743 | 0.4577 |  |
| BMI (kg/m2) | +0.0021 | 0.0238 | ±0.0477 | +0.090 | 0.9282 |  |
| Hypertension | +0.4666 | 0.3852 | ±0.7704 | +1.211 | 0.2258 |  |
| High cholesterol | +0.0330 | 0.3334 | ±0.6668 | +0.099 | 0.9213 |  |
| Kidney disease | +0.2361 | 0.4606 | ±0.9212 | +0.513 | 0.6083 |  |
| Circulatory disease | +0.0473 | 0.4595 | ±0.9189 | +0.103 | 0.9179 |  |
| Nocturnal time > 180 (%) | -0.0316 | 0.0374 | ±0.0748 | -0.845 | 0.3982 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 198; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **198**, R² = **0.2033**, Adj R² = **0.1471**, F-statistic = **3.61** (p = **4.41e-05**), Residual SE = **6.052** on **184** df, AIC = **1288.3**, BIC = **1334.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5249** | 4.4140 | ±8.8279 | **+10.540** | **5.63e-26** | *** |
| Education: graduate level (vs college) | +0.8800 | 0.9510 | ±1.9019 | +0.925 | 0.3548 |  |
| Education: high school or below (vs college) | +1.9575 | 1.5702 | ±3.1404 | +1.247 | 0.2125 |  |
| **Site: UCSD (vs UAB)** | **+3.3000** | 1.1410 | ±2.2820 | **+2.892** | **0.0038** | ** |
| Site: UW (vs UAB) | -0.1772 | 1.1973 | ±2.3947 | -0.148 | 0.8824 |  |
| Season: spring (vs autumn) | -1.6612 | 1.3032 | ±2.6065 | -1.275 | 0.2024 |  |
| Season: summer (vs autumn) | +0.9150 | 1.3015 | ±2.6031 | +0.703 | 0.4820 |  |
| **Season: winter (vs autumn)** | **-5.0494** | 1.4693 | ±2.9386 | **-3.437** | **5.89e-04** | *** |
| Age (years) | +0.0296 | 0.0485 | ±0.0969 | +0.611 | 0.5410 |  |
| BMI (kg/m2) | -0.0545 | 0.0619 | ±0.1239 | -0.880 | 0.3788 |  |
| Hypertension | +0.3463 | 1.0546 | ±2.1091 | +0.328 | 0.7426 |  |
| **High cholesterol** | **-2.0735** | 0.9908 | ±1.9816 | **-2.093** | **0.0364** | * |
| Kidney disease | +1.5245 | 1.3547 | ±2.7093 | +1.125 | 0.2604 |  |
| Circulatory disease | -0.2756 | 1.2153 | ±2.4307 | -0.227 | 0.8206 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **198**, R² = **0.2036**, Adj R² = **0.1426**, F-statistic = **3.34** (p = **8.63e-05**), Residual SE = **6.068** on **183** df, AIC = **1290.3**, BIC = **1339.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5578** | 6.8209 | ±13.6417 | **+6.972** | **3.12e-12** | *** |
| Education: graduate level (vs college) | +0.8726 | 0.9590 | ±1.9179 | +0.910 | 0.3628 |  |
| Education: high school or below (vs college) | +1.9658 | 1.5793 | ±3.1586 | +1.245 | 0.2132 |  |
| **Site: UCSD (vs UAB)** | **+3.2981** | 1.1482 | ±2.2963 | **+2.873** | **0.0041** | ** |
| Site: UW (vs UAB) | -0.1806 | 1.2036 | ±2.4072 | -0.150 | 0.8807 |  |
| Season: spring (vs autumn) | -1.6673 | 1.3103 | ±2.6207 | -1.272 | 0.2032 |  |
| Season: summer (vs autumn) | +0.9386 | 1.3060 | ±2.6120 | +0.719 | 0.4723 |  |
| **Season: winter (vs autumn)** | **-5.0349** | 1.4768 | ±2.9536 | **-3.409** | **6.51e-04** | *** |
| Age (years) | +0.0298 | 0.0491 | ±0.0983 | +0.607 | 0.5437 |  |
| BMI (kg/m2) | -0.0514 | 0.0658 | ±0.1316 | -0.782 | 0.4345 |  |
| Hypertension | +0.3528 | 1.0573 | ±2.1147 | +0.334 | 0.7387 |  |
| **High cholesterol** | **-2.0535** | 1.0084 | ±2.0169 | **-2.036** | **0.0417** | * |
| Kidney disease | +1.4944 | 1.3790 | ±2.7579 | +1.084 | 0.2785 |  |
| Circulatory disease | -0.2329 | 1.2344 | ±2.4688 | -0.189 | 0.8504 |  |
| HbA1c (%) | -0.1948 | 1.0888 | ±2.1775 | -0.179 | 0.8580 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **198**, R² = **0.2111**, Adj R² = **0.1507**, F-statistic = **3.50** (p = **4.44e-05**), Residual SE = **6.039** on **183** df, AIC = **1288.4**, BIC = **1337.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.9091** | 6.5000 | ±12.9999 | **+6.294** | **3.10e-10** | *** |
| Education: graduate level (vs college) | +0.8791 | 0.9556 | ±1.9111 | +0.920 | 0.3576 |  |
| Education: high school or below (vs college) | +2.0679 | 1.5547 | ±3.1093 | +1.330 | 0.1835 |  |
| **Site: UCSD (vs UAB)** | **+3.3101** | 1.1321 | ±2.2641 | **+2.924** | **0.0035** | ** |
| Site: UW (vs UAB) | -0.1269 | 1.1969 | ±2.3938 | -0.106 | 0.9156 |  |
| Season: spring (vs autumn) | -1.7064 | 1.3047 | ±2.6094 | -1.308 | 0.1909 |  |
| Season: summer (vs autumn) | +0.7350 | 1.2979 | ±2.5959 | +0.566 | 0.5712 |  |
| **Season: winter (vs autumn)** | **-5.1261** | 1.4569 | ±2.9138 | **-3.518** | **4.34e-04** | *** |
| Age (years) | +0.0305 | 0.0488 | ±0.0976 | +0.625 | 0.5318 |  |
| BMI (kg/m2) | -0.0619 | 0.0625 | ±0.1251 | -0.990 | 0.3222 |  |
| Hypertension | +0.2676 | 1.0844 | ±2.1688 | +0.247 | 0.8051 |  |
| **High cholesterol** | **-2.0269** | 0.9884 | ±1.9768 | **-2.051** | **0.0403** | * |
| Kidney disease | +1.3824 | 1.3249 | ±2.6498 | +1.043 | 0.2968 |  |
| Circulatory disease | -0.3426 | 1.1936 | ±2.3872 | -0.287 | 0.7741 |  |
| Mean glucose (mg/dL) | +0.0463 | 0.0381 | ±0.0762 | +1.215 | 0.2244 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **198**, R² = **0.2111**, Adj R² = **0.1507**, F-statistic = **3.50** (p = **4.44e-05**), Residual SE = **6.039** on **183** df, AIC = **1288.4**, BIC = **1337.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+34.5026** | 10.9649 | ±21.9298 | **+3.147** | **0.0017** | ** |
| Education: graduate level (vs college) | +0.8791 | 0.9556 | ±1.9111 | +0.920 | 0.3576 |  |
| Education: high school or below (vs college) | +2.0679 | 1.5547 | ±3.1093 | +1.330 | 0.1835 |  |
| **Site: UCSD (vs UAB)** | **+3.3101** | 1.1321 | ±2.2641 | **+2.924** | **0.0035** | ** |
| Site: UW (vs UAB) | -0.1269 | 1.1969 | ±2.3938 | -0.106 | 0.9156 |  |
| Season: spring (vs autumn) | -1.7064 | 1.3047 | ±2.6094 | -1.308 | 0.1909 |  |
| Season: summer (vs autumn) | +0.7350 | 1.2979 | ±2.5959 | +0.566 | 0.5712 |  |
| **Season: winter (vs autumn)** | **-5.1261** | 1.4569 | ±2.9138 | **-3.518** | **4.34e-04** | *** |
| Age (years) | +0.0305 | 0.0488 | ±0.0976 | +0.625 | 0.5318 |  |
| BMI (kg/m2) | -0.0619 | 0.0625 | ±0.1251 | -0.990 | 0.3222 |  |
| Hypertension | +0.2676 | 1.0844 | ±2.1688 | +0.247 | 0.8051 |  |
| **High cholesterol** | **-2.0269** | 0.9884 | ±1.9768 | **-2.051** | **0.0403** | * |
| Kidney disease | +1.3824 | 1.3249 | ±2.6498 | +1.043 | 0.2968 |  |
| Circulatory disease | -0.3426 | 1.1936 | ±2.3872 | -0.287 | 0.7741 |  |
| GMI (%) | +1.9355 | 1.5931 | ±3.1863 | +1.215 | 0.2244 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **198**, R² = **0.2090**, Adj R² = **0.1484**, F-statistic = **3.45** (p = **5.37e-05**), Residual SE = **6.047** on **183** df, AIC = **1288.9**, BIC = **1338.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.1632** | 5.8859 | ±11.7718 | **+7.163** | **7.87e-13** | *** |
| Education: graduate level (vs college) | +0.8418 | 0.9579 | ±1.9157 | +0.879 | 0.3795 |  |
| Education: high school or below (vs college) | +2.0199 | 1.5629 | ±3.1257 | +1.292 | 0.1962 |  |
| **Site: UCSD (vs UAB)** | **+3.2767** | 1.1402 | ±2.2804 | **+2.874** | **0.0041** | ** |
| Site: UW (vs UAB) | -0.1652 | 1.1974 | ±2.3949 | -0.138 | 0.8903 |  |
| Season: spring (vs autumn) | -1.6684 | 1.3030 | ±2.6060 | -1.280 | 0.2004 |  |
| Season: summer (vs autumn) | +0.8055 | 1.2961 | ±2.5922 | +0.621 | 0.5343 |  |
| **Season: winter (vs autumn)** | **-5.0543** | 1.4656 | ±2.9312 | **-3.449** | **5.63e-04** | *** |
| Age (years) | +0.0345 | 0.0491 | ±0.0983 | +0.702 | 0.4829 |  |
| BMI (kg/m2) | -0.0629 | 0.0639 | ±0.1278 | -0.985 | 0.3248 |  |
| Hypertension | +0.3219 | 1.0719 | ±2.1439 | +0.300 | 0.7640 |  |
| **High cholesterol** | **-2.0880** | 0.9841 | ±1.9682 | **-2.122** | **0.0339** | * |
| Kidney disease | +1.5089 | 1.3370 | ±2.6740 | +1.129 | 0.2591 |  |
| Circulatory disease | -0.3672 | 1.2076 | ±2.4153 | -0.304 | 0.7611 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0348 | 0.0333 | ±0.0667 | +1.043 | 0.2969 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **198**, R² = **0.2174**, Adj R² = **0.1575**, F-statistic = **3.63** (p = **2.52e-05**), Residual SE = **6.015** on **183** df, AIC = **1286.8**, BIC = **1336.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.0448** | 4.7457 | ±9.4914 | **+9.070** | **1.19e-19** | *** |
| Education: graduate level (vs college) | +0.7644 | 0.9490 | ±1.8980 | +0.806 | 0.4205 |  |
| Education: high school or below (vs college) | +1.5041 | 1.5662 | ±3.1323 | +0.960 | 0.3368 |  |
| **Site: UCSD (vs UAB)** | **+3.4594** | 1.1360 | ±2.2720 | **+3.045** | **0.0023** | ** |
| Site: UW (vs UAB) | +0.1400 | 1.2049 | ±2.4098 | +0.116 | 0.9075 |  |
| Season: spring (vs autumn) | -1.6517 | 1.2982 | ±2.5964 | -1.272 | 0.2033 |  |
| Season: summer (vs autumn) | +0.9342 | 1.2793 | ±2.5586 | +0.730 | 0.4652 |  |
| **Season: winter (vs autumn)** | **-5.0415** | 1.4551 | ±2.9103 | **-3.465** | **5.31e-04** | *** |
| Age (years) | +0.0232 | 0.0482 | ±0.0964 | +0.481 | 0.6305 |  |
| BMI (kg/m2) | -0.0528 | 0.0626 | ±0.1253 | -0.844 | 0.3989 |  |
| Hypertension | +0.0534 | 1.0761 | ±2.1522 | +0.050 | 0.9604 |  |
| **High cholesterol** | **-1.9525** | 0.9896 | ±1.9792 | **-1.973** | **0.0485** | * |
| Kidney disease | +1.1586 | 1.2859 | ±2.5718 | +0.901 | 0.3676 |  |
| Circulatory disease | -0.4055 | 1.1764 | ±2.3529 | -0.345 | 0.7303 |  |
| Glucose SD, pooled (mg/dL) | +0.1804 | 0.0934 | ±0.1867 | +1.932 | 0.0534 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **198**, R² = **0.2137**, Adj R² = **0.1536**, F-statistic = **3.55** (p = **3.50e-05**), Residual SE = **6.029** on **183** df, AIC = **1287.7**, BIC = **1337.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7804** | 4.7393 | ±9.4785 | **+9.238** | **2.52e-20** | *** |
| Education: graduate level (vs college) | +0.7963 | 0.9511 | ±1.9022 | +0.837 | 0.4025 |  |
| Education: high school or below (vs college) | +1.6369 | 1.5644 | ±3.1288 | +1.046 | 0.2954 |  |
| **Site: UCSD (vs UAB)** | **+3.3493** | 1.1345 | ±2.2691 | **+2.952** | **0.0032** | ** |
| Site: UW (vs UAB) | +0.0165 | 1.2042 | ±2.4084 | +0.014 | 0.9891 |  |
| Season: spring (vs autumn) | -1.6011 | 1.3008 | ±2.6015 | -1.231 | 0.2184 |  |
| Season: summer (vs autumn) | +0.9872 | 1.2900 | ±2.5800 | +0.765 | 0.4441 |  |
| **Season: winter (vs autumn)** | **-5.0106** | 1.4577 | ±2.9153 | **-3.437** | **5.87e-04** | *** |
| Age (years) | +0.0237 | 0.0482 | ±0.0964 | +0.492 | 0.6228 |  |
| BMI (kg/m2) | -0.0529 | 0.0626 | ±0.1251 | -0.846 | 0.3975 |  |
| Hypertension | +0.0313 | 1.0793 | ±2.1586 | +0.029 | 0.9768 |  |
| **High cholesterol** | **-1.9646** | 0.9920 | ±1.9840 | **-1.981** | **0.0476** | * |
| Kidney disease | +1.3014 | 1.3020 | ±2.6041 | +1.000 | 0.3176 |  |
| Circulatory disease | -0.3090 | 1.1961 | ±2.3922 | -0.258 | 0.7961 |  |
| Avg. daily SD (mg/dL) | +0.1573 | 0.0944 | ±0.1888 | +1.666 | 0.0956 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **198**, R² = **0.2100**, Adj R² = **0.1495**, F-statistic = **3.47** (p = **4.91e-05**), Residual SE = **6.043** on **183** df, AIC = **1288.7**, BIC = **1338.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.5967** | 5.0953 | ±10.1906 | **+8.556** | **1.17e-17** | *** |
| Education: graduate level (vs college) | +0.7916 | 0.9496 | ±1.8991 | +0.834 | 0.4044 |  |
| Education: high school or below (vs college) | +1.5176 | 1.6561 | ±3.3121 | +0.916 | 0.3594 |  |
| **Site: UCSD (vs UAB)** | **+3.4287** | 1.1563 | ±2.3127 | **+2.965** | **0.0030** | ** |
| Site: UW (vs UAB) | +0.0544 | 1.2217 | ±2.4433 | +0.045 | 0.9645 |  |
| Season: spring (vs autumn) | -1.6337 | 1.3022 | ±2.6043 | -1.255 | 0.2096 |  |
| Season: summer (vs autumn) | +1.0260 | 1.2941 | ±2.5882 | +0.793 | 0.4279 |  |
| **Season: winter (vs autumn)** | **-5.0190** | 1.4679 | ±2.9357 | **-3.419** | **6.28e-04** | *** |
| Age (years) | +0.0238 | 0.0485 | ±0.0970 | +0.490 | 0.6242 |  |
| BMI (kg/m2) | -0.0493 | 0.0631 | ±0.1261 | -0.781 | 0.4345 |  |
| Hypertension | +0.1487 | 1.0607 | ±2.1213 | +0.140 | 0.8885 |  |
| **High cholesterol** | **-2.0010** | 0.9994 | ±1.9988 | **-2.002** | **0.0453** | * |
| Kidney disease | +1.2983 | 1.3318 | ±2.6636 | +0.975 | 0.3296 |  |
| Circulatory disease | -0.3306 | 1.2033 | ±2.4065 | -0.275 | 0.7835 |  |
| CV (%) | +0.1849 | 0.1493 | ±0.2986 | +1.239 | 0.2155 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **198**, R² = **0.2071**, Adj R² = **0.1465**, F-statistic = **3.41** (p = **6.30e-05**), Residual SE = **6.054** on **183** df, AIC = **1289.4**, BIC = **1338.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.0202** | 4.9441 | ±9.8883 | **+9.915** | **3.59e-23** | *** |
| Education: graduate level (vs college) | +0.8259 | 0.9508 | ±1.9015 | +0.869 | 0.3850 |  |
| Education: high school or below (vs college) | +1.6640 | 1.6411 | ±3.2822 | +1.014 | 0.3106 |  |
| **Site: UCSD (vs UAB)** | **+3.3747** | 1.1530 | ±2.3059 | **+2.927** | **0.0034** | ** |
| Site: UW (vs UAB) | -0.0238 | 1.2163 | ±2.4326 | -0.020 | 0.9844 |  |
| Season: spring (vs autumn) | -1.6427 | 1.3087 | ±2.6174 | -1.255 | 0.2094 |  |
| Season: summer (vs autumn) | +0.9899 | 1.3023 | ±2.6046 | +0.760 | 0.4472 |  |
| **Season: winter (vs autumn)** | **-5.0352** | 1.4715 | ±2.9429 | **-3.422** | **6.22e-04** | *** |
| Age (years) | +0.0250 | 0.0485 | ±0.0970 | +0.516 | 0.6057 |  |
| BMI (kg/m2) | -0.0531 | 0.0627 | ±0.1255 | -0.847 | 0.3970 |  |
| Hypertension | +0.1884 | 1.0647 | ±2.1295 | +0.177 | 0.8596 |  |
| **High cholesterol** | **-2.0375** | 0.9978 | ±1.9957 | **-2.042** | **0.0412** | * |
| Kidney disease | +1.3601 | 1.3462 | ±2.6924 | +1.010 | 0.3123 |  |
| Circulatory disease | -0.2922 | 1.2068 | ±2.4137 | -0.242 | 0.8087 |  |
| Mean / SD ratio | -0.3641 | 0.3773 | ±0.7546 | -0.965 | 0.3346 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **198**, R² = **0.2051**, Adj R² = **0.1443**, F-statistic = **3.37** (p = **7.55e-05**), Residual SE = **6.062** on **183** df, AIC = **1289.9**, BIC = **1339.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.0590** | 4.8382 | ±9.6764 | **+9.933** | **2.98e-23** | *** |
| Education: graduate level (vs college) | +0.8614 | 0.9534 | ±1.9068 | +0.904 | 0.3662 |  |
| Education: high school or below (vs college) | +1.8048 | 1.6104 | ±3.2208 | +1.121 | 0.2624 |  |
| **Site: UCSD (vs UAB)** | **+3.2948** | 1.1406 | ±2.2811 | **+2.889** | **0.0039** | ** |
| Site: UW (vs UAB) | -0.1058 | 1.2114 | ±2.4227 | -0.087 | 0.9304 |  |
| Season: spring (vs autumn) | -1.6391 | 1.3119 | ±2.6239 | -1.249 | 0.2115 |  |
| Season: summer (vs autumn) | +0.9794 | 1.3124 | ±2.6248 | +0.746 | 0.4555 |  |
| **Season: winter (vs autumn)** | **-5.0152** | 1.4744 | ±2.9488 | **-3.402** | **6.70e-04** | *** |
| Age (years) | +0.0263 | 0.0488 | ±0.0976 | +0.539 | 0.5901 |  |
| BMI (kg/m2) | -0.0540 | 0.0627 | ±0.1255 | -0.861 | 0.3895 |  |
| Hypertension | +0.2056 | 1.0698 | ±2.1396 | +0.192 | 0.8476 |  |
| **High cholesterol** | **-2.0623** | 0.9951 | ±1.9902 | **-2.072** | **0.0382** | * |
| Kidney disease | +1.4460 | 1.3529 | ±2.7058 | +1.069 | 0.2851 |  |
| Circulatory disease | -0.2368 | 1.2287 | ±2.4575 | -0.193 | 0.8472 |  |
| Avg. daily mean/SD | -0.1878 | 0.2856 | ±0.5712 | -0.658 | 0.5107 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **198**, R² = **0.2130**, Adj R² = **0.1528**, F-statistic = **3.54** (p = **3.73e-05**), Residual SE = **6.032** on **183** df, AIC = **1287.9**, BIC = **1337.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.9232** | 5.2165 | ±10.4329 | **+8.228** | **1.90e-16** | *** |
| Education: graduate level (vs college) | +0.8543 | 0.9508 | ±1.9016 | +0.898 | 0.3689 |  |
| Education: high school or below (vs college) | +1.7862 | 1.5447 | ±3.0893 | +1.156 | 0.2475 |  |
| **Site: UCSD (vs UAB)** | **+3.2937** | 1.1299 | ±2.2599 | **+2.915** | **0.0036** | ** |
| Site: UW (vs UAB) | -0.0872 | 1.1926 | ±2.3851 | -0.073 | 0.9417 |  |
| Season: spring (vs autumn) | -1.6322 | 1.3110 | ±2.6219 | -1.245 | 0.2131 |  |
| Season: summer (vs autumn) | +0.9409 | 1.2984 | ±2.5968 | +0.725 | 0.4687 |  |
| **Season: winter (vs autumn)** | **-5.0047** | 1.4707 | ±2.9414 | **-3.403** | **6.67e-04** | *** |
| Age (years) | +0.0314 | 0.0479 | ±0.0957 | +0.656 | 0.5118 |  |
| BMI (kg/m2) | -0.0579 | 0.0619 | ±0.1238 | -0.935 | 0.3499 |  |
| Hypertension | +0.2557 | 1.0601 | ±2.1203 | +0.241 | 0.8094 |  |
| **High cholesterol** | **-2.1333** | 0.9812 | ±1.9625 | **-2.174** | **0.0297** | * |
| Kidney disease | +1.5339 | 1.3405 | ±2.6810 | +1.144 | 0.2525 |  |
| Circulatory disease | -0.1614 | 1.2228 | ±2.4457 | -0.132 | 0.8950 |  |
| MAG (mg/dL/h) | +0.1006 | 0.0709 | ±0.1417 | +1.420 | 0.1557 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **198**, R² = **0.2129**, Adj R² = **0.1527**, F-statistic = **3.54** (p = **3.78e-05**), Residual SE = **6.032** on **183** df, AIC = **1288.0**, BIC = **1337.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.1376** | 5.0318 | ±10.0636 | **+8.573** | **1.01e-17** | *** |
| Education: graduate level (vs college) | +0.8383 | 0.9518 | ±1.9035 | +0.881 | 0.3784 |  |
| Education: high school or below (vs college) | +1.7129 | 1.5622 | ±3.1243 | +1.096 | 0.2729 |  |
| **Site: UCSD (vs UAB)** | **+3.3878** | 1.1377 | ±2.2753 | **+2.978** | **0.0029** | ** |
| Site: UW (vs UAB) | -0.0011 | 1.2076 | ±2.4151 | -0.001 | 0.9993 |  |
| Season: spring (vs autumn) | -1.6337 | 1.3031 | ±2.6061 | -1.254 | 0.2099 |  |
| Season: summer (vs autumn) | +1.0046 | 1.2895 | ±2.5791 | +0.779 | 0.4359 |  |
| **Season: winter (vs autumn)** | **-4.9892** | 1.4619 | ±2.9238 | **-3.413** | **6.43e-04** | *** |
| Age (years) | +0.0235 | 0.0480 | ±0.0959 | +0.489 | 0.6245 |  |
| BMI (kg/m2) | -0.0483 | 0.0634 | ±0.1268 | -0.761 | 0.4464 |  |
| Hypertension | +0.1254 | 1.0583 | ±2.1166 | +0.118 | 0.9057 |  |
| **High cholesterol** | **-2.0264** | 0.9875 | ±1.9750 | **-2.052** | **0.0402** | * |
| Kidney disease | +1.3921 | 1.3152 | ±2.6304 | +1.058 | 0.2899 |  |
| Circulatory disease | -0.2657 | 1.2021 | ±2.4043 | -0.221 | 0.8251 |  |
| Avg. daily range (mg/dL) | +0.0372 | 0.0230 | ±0.0460 | +1.617 | 0.1058 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **198**, R² = **0.2080**, Adj R² = **0.1474**, F-statistic = **3.43** (p = **5.86e-05**), Residual SE = **6.051** on **183** df, AIC = **1289.2**, BIC = **1338.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.3633** | 4.4103 | ±8.8206 | **+10.286** | **8.17e-25** | *** |
| Education: graduate level (vs college) | +0.8246 | 0.9555 | ±1.9110 | +0.863 | 0.3881 |  |
| Education: high school or below (vs college) | +1.7003 | 1.5877 | ±3.1754 | +1.071 | 0.2842 |  |
| **Site: UCSD (vs UAB)** | **+3.4990** | 1.1319 | ±2.2638 | **+3.091** | **0.0020** | ** |
| Site: UW (vs UAB) | +0.0513 | 1.1707 | ±2.3414 | +0.044 | 0.9650 |  |
| Season: spring (vs autumn) | -1.7506 | 1.2970 | ±2.5940 | -1.350 | 0.1771 |  |
| Season: summer (vs autumn) | +0.7372 | 1.2872 | ±2.5743 | +0.573 | 0.5668 |  |
| **Season: winter (vs autumn)** | **-5.0604** | 1.4731 | ±2.9461 | **-3.435** | **5.92e-04** | *** |
| Age (years) | +0.0285 | 0.0490 | ±0.0980 | +0.581 | 0.5611 |  |
| BMI (kg/m2) | -0.0551 | 0.0626 | ±0.1252 | -0.880 | 0.3789 |  |
| Hypertension | +0.4258 | 1.0554 | ±2.1107 | +0.403 | 0.6866 |  |
| **High cholesterol** | **-2.1019** | 0.9885 | ±1.9770 | **-2.126** | **0.0335** | * |
| Kidney disease | +1.2745 | 1.3360 | ±2.6720 | +0.954 | 0.3401 |  |
| Circulatory disease | -0.5382 | 1.1967 | ±2.3934 | -0.450 | 0.6529 |  |
| SD of daily means (mg/dL) | +0.1925 | 0.2040 | ±0.4079 | +0.944 | 0.3452 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **198**, R² = **0.2093**, Adj R² = **0.1488**, F-statistic = **3.46** (p = **5.21e-05**), Residual SE = **6.046** on **183** df, AIC = **1288.9**, BIC = **1338.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.7244** | 12.5329 | ±25.0659 | **+4.606** | **4.11e-06** | *** |
| Education: graduate level (vs college) | +0.8132 | 0.9537 | ±1.9074 | +0.853 | 0.3938 |  |
| Education: high school or below (vs college) | +1.8162 | 1.5576 | ±3.1151 | +1.166 | 0.2436 |  |
| **Site: UCSD (vs UAB)** | **+3.4000** | 1.1511 | ±2.3022 | **+2.954** | **0.0031** | ** |
| Site: UW (vs UAB) | -0.0743 | 1.1986 | ±2.3972 | -0.062 | 0.9506 |  |
| Season: spring (vs autumn) | -1.6487 | 1.3012 | ±2.6024 | -1.267 | 0.2051 |  |
| Season: summer (vs autumn) | +0.8344 | 1.2889 | ±2.5777 | +0.647 | 0.5174 |  |
| **Season: winter (vs autumn)** | **-5.0939** | 1.4579 | ±2.9157 | **-3.494** | **4.76e-04** | *** |
| Age (years) | +0.0240 | 0.0489 | ±0.0978 | +0.490 | 0.6243 |  |
| BMI (kg/m2) | -0.0563 | 0.0627 | ±0.1253 | -0.898 | 0.3691 |  |
| Hypertension | +0.2826 | 1.0939 | ±2.1879 | +0.258 | 0.7962 |  |
| **High cholesterol** | **-2.0071** | 0.9920 | ±1.9840 | **-2.023** | **0.0430** | * |
| Kidney disease | +1.2960 | 1.3361 | ±2.6723 | +0.970 | 0.3321 |  |
| Circulatory disease | -0.3387 | 1.1952 | ±2.3904 | -0.283 | 0.7769 |  |
| Time in range 70-180, pooled (%) | -0.1121 | 0.1226 | ±0.2452 | -0.914 | 0.3607 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **198**, R² = **0.2104**, Adj R² = **0.1500**, F-statistic = **3.48** (p = **4.73e-05**), Residual SE = **6.042** on **183** df, AIC = **1288.6**, BIC = **1337.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.9925** | 12.3697 | ±24.7394 | **+4.769** | **1.85e-06** | *** |
| Education: graduate level (vs college) | +0.8147 | 0.9532 | ±1.9064 | +0.855 | 0.3927 |  |
| Education: high school or below (vs college) | +1.8291 | 1.5562 | ±3.1125 | +1.175 | 0.2399 |  |
| **Site: UCSD (vs UAB)** | **+3.4090** | 1.1480 | ±2.2960 | **+2.970** | **0.0030** | ** |
| Site: UW (vs UAB) | -0.0863 | 1.1969 | ±2.3937 | -0.072 | 0.9425 |  |
| Season: spring (vs autumn) | -1.6411 | 1.2989 | ±2.5978 | -1.263 | 0.2064 |  |
| Season: summer (vs autumn) | +0.8229 | 1.2877 | ±2.5753 | +0.639 | 0.5228 |  |
| **Season: winter (vs autumn)** | **-5.1010** | 1.4568 | ±2.9137 | **-3.501** | **4.63e-04** | *** |
| Age (years) | +0.0233 | 0.0490 | ±0.0979 | +0.475 | 0.6345 |  |
| BMI (kg/m2) | -0.0557 | 0.0626 | ±0.1252 | -0.889 | 0.3738 |  |
| Hypertension | +0.2595 | 1.0948 | ±2.1896 | +0.237 | 0.8126 |  |
| **High cholesterol** | **-2.0059** | 0.9890 | ±1.9780 | **-2.028** | **0.0425** | * |
| Kidney disease | +1.2701 | 1.3277 | ±2.6554 | +0.957 | 0.3388 |  |
| Circulatory disease | -0.3417 | 1.1926 | ±2.3853 | -0.286 | 0.7745 |  |
| Avg. daily time in range 70-180 (%) | -0.1247 | 0.1201 | ±0.2403 | -1.038 | 0.2994 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **198**, R² = **0.2036**, Adj R² = **0.1426**, F-statistic = **3.34** (p = **8.62e-05**), Residual SE = **6.068** on **183** df, AIC = **1290.3**, BIC = **1339.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5513** | 4.4921 | ±8.9843 | **+10.363** | **3.66e-25** | *** |
| Education: graduate level (vs college) | +0.8665 | 0.9553 | ±1.9106 | +0.907 | 0.3644 |  |
| Education: high school or below (vs college) | +1.9142 | 1.5812 | ±3.1625 | +1.211 | 0.2261 |  |
| **Site: UCSD (vs UAB)** | **+3.3173** | 1.1455 | ±2.2911 | **+2.896** | **0.0038** | ** |
| Site: UW (vs UAB) | -0.1722 | 1.2040 | ±2.4081 | -0.143 | 0.8863 |  |
| Season: spring (vs autumn) | -1.6349 | 1.3194 | ±2.6389 | -1.239 | 0.2153 |  |
| Season: summer (vs autumn) | +0.9301 | 1.3379 | ±2.6757 | +0.695 | 0.4869 |  |
| **Season: winter (vs autumn)** | **-5.0199** | 1.4895 | ±2.9790 | **-3.370** | **7.51e-04** | *** |
| Age (years) | +0.0281 | 0.0515 | ±0.1031 | +0.544 | 0.5861 |  |
| BMI (kg/m2) | -0.0537 | 0.0619 | ±0.1237 | -0.869 | 0.3851 |  |
| Hypertension | +0.3371 | 1.0571 | ±2.1143 | +0.319 | 0.7498 |  |
| **High cholesterol** | **-2.0862** | 0.9906 | ±1.9811 | **-2.106** | **0.0352** | * |
| Kidney disease | +1.5392 | 1.3597 | ±2.7194 | +1.132 | 0.2576 |  |
| Circulatory disease | -0.2772 | 1.2413 | ±2.4827 | -0.223 | 0.8233 |  |
| Time 54-69, pooled (%) | +0.3632 | 2.0561 | ±4.1121 | +0.177 | 0.8598 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **198**, R² = **0.2034**, Adj R² = **0.1424**, F-statistic = **3.34** (p = **8.76e-05**), Residual SE = **6.068** on **183** df, AIC = **1290.3**, BIC = **1339.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5075** | 4.4746 | ±8.9492 | **+10.394** | **2.65e-25** | *** |
| Education: graduate level (vs college) | +0.8854 | 0.9558 | ±1.9116 | +0.926 | 0.3543 |  |
| Education: high school or below (vs college) | +1.9749 | 1.5854 | ±3.1709 | +1.246 | 0.2129 |  |
| **Site: UCSD (vs UAB)** | **+3.2962** | 1.1486 | ±2.2971 | **+2.870** | **0.0041** | ** |
| Site: UW (vs UAB) | -0.1765 | 1.2033 | ±2.4066 | -0.147 | 0.8834 |  |
| Season: spring (vs autumn) | -1.6723 | 1.3189 | ±2.6377 | -1.268 | 0.2048 |  |
| Season: summer (vs autumn) | +0.9050 | 1.3308 | ±2.6616 | +0.680 | 0.4965 |  |
| **Season: winter (vs autumn)** | **-5.0611** | 1.4838 | ±2.9676 | **-3.411** | **6.47e-04** | *** |
| Age (years) | +0.0303 | 0.0508 | ±0.1016 | +0.597 | 0.5504 |  |
| BMI (kg/m2) | -0.0548 | 0.0617 | ±0.1235 | -0.888 | 0.3746 |  |
| Hypertension | +0.3522 | 1.0585 | ±2.1171 | +0.333 | 0.7394 |  |
| **High cholesterol** | **-2.0683** | 0.9890 | ±1.9780 | **-2.091** | **0.0365** | * |
| Kidney disease | +1.5160 | 1.3632 | ±2.7264 | +1.112 | 0.2661 |  |
| Circulatory disease | -0.2785 | 1.2312 | ±2.4625 | -0.226 | 0.8210 |  |
| Avg. daily time 54-69 (%) | -0.1469 | 1.6214 | ±3.2429 | -0.091 | 0.9278 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **198**, R² = **0.2036**, Adj R² = **0.1426**, F-statistic = **3.34** (p = **8.62e-05**), Residual SE = **6.068** on **183** df, AIC = **1290.3**, BIC = **1339.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5513** | 4.4921 | ±8.9843 | **+10.363** | **3.66e-25** | *** |
| Education: graduate level (vs college) | +0.8665 | 0.9553 | ±1.9106 | +0.907 | 0.3644 |  |
| Education: high school or below (vs college) | +1.9142 | 1.5812 | ±3.1625 | +1.211 | 0.2261 |  |
| **Site: UCSD (vs UAB)** | **+3.3173** | 1.1455 | ±2.2911 | **+2.896** | **0.0038** | ** |
| Site: UW (vs UAB) | -0.1722 | 1.2040 | ±2.4081 | -0.143 | 0.8863 |  |
| Season: spring (vs autumn) | -1.6349 | 1.3194 | ±2.6389 | -1.239 | 0.2153 |  |
| Season: summer (vs autumn) | +0.9301 | 1.3379 | ±2.6757 | +0.695 | 0.4869 |  |
| **Season: winter (vs autumn)** | **-5.0199** | 1.4895 | ±2.9790 | **-3.370** | **7.51e-04** | *** |
| Age (years) | +0.0281 | 0.0515 | ±0.1031 | +0.544 | 0.5861 |  |
| BMI (kg/m2) | -0.0537 | 0.0619 | ±0.1237 | -0.869 | 0.3851 |  |
| Hypertension | +0.3371 | 1.0571 | ±2.1143 | +0.319 | 0.7498 |  |
| **High cholesterol** | **-2.0862** | 0.9906 | ±1.9811 | **-2.106** | **0.0352** | * |
| Kidney disease | +1.5392 | 1.3597 | ±2.7194 | +1.132 | 0.2576 |  |
| Circulatory disease | -0.2772 | 1.2413 | ±2.4827 | -0.223 | 0.8233 |  |
| Time < 70 (%) | +0.3632 | 2.0561 | ±4.1121 | +0.177 | 0.8598 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **198**, R² = **0.2034**, Adj R² = **0.1424**, F-statistic = **3.34** (p = **8.76e-05**), Residual SE = **6.068** on **183** df, AIC = **1290.3**, BIC = **1339.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5075** | 4.4746 | ±8.9492 | **+10.394** | **2.65e-25** | *** |
| Education: graduate level (vs college) | +0.8854 | 0.9558 | ±1.9116 | +0.926 | 0.3543 |  |
| Education: high school or below (vs college) | +1.9749 | 1.5854 | ±3.1709 | +1.246 | 0.2129 |  |
| **Site: UCSD (vs UAB)** | **+3.2962** | 1.1486 | ±2.2971 | **+2.870** | **0.0041** | ** |
| Site: UW (vs UAB) | -0.1765 | 1.2033 | ±2.4066 | -0.147 | 0.8834 |  |
| Season: spring (vs autumn) | -1.6723 | 1.3189 | ±2.6377 | -1.268 | 0.2048 |  |
| Season: summer (vs autumn) | +0.9050 | 1.3308 | ±2.6616 | +0.680 | 0.4965 |  |
| **Season: winter (vs autumn)** | **-5.0611** | 1.4838 | ±2.9676 | **-3.411** | **6.47e-04** | *** |
| Age (years) | +0.0303 | 0.0508 | ±0.1016 | +0.597 | 0.5504 |  |
| BMI (kg/m2) | -0.0548 | 0.0617 | ±0.1235 | -0.888 | 0.3746 |  |
| Hypertension | +0.3522 | 1.0585 | ±2.1171 | +0.333 | 0.7394 |  |
| **High cholesterol** | **-2.0683** | 0.9890 | ±1.9780 | **-2.091** | **0.0365** | * |
| Kidney disease | +1.5160 | 1.3632 | ±2.7264 | +1.112 | 0.2661 |  |
| Circulatory disease | -0.2785 | 1.2312 | ±2.4625 | -0.226 | 0.8210 |  |
| Avg. daily time < 70 (%) | -0.1469 | 1.6214 | ±3.2429 | -0.091 | 0.9278 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **198**, R² = **0.2091**, Adj R² = **0.1486**, F-statistic = **3.46** (p = **5.30e-05**), Residual SE = **6.047** on **183** df, AIC = **1288.9**, BIC = **1338.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5089** | 4.4797 | ±8.9595 | **+10.382** | **2.99e-25** | *** |
| Education: graduate level (vs college) | +0.8189 | 0.9537 | ±1.9073 | +0.859 | 0.3905 |  |
| Education: high school or below (vs college) | +1.8328 | 1.5595 | ±3.1190 | +1.175 | 0.2399 |  |
| **Site: UCSD (vs UAB)** | **+3.3923** | 1.1506 | ±2.3012 | **+2.948** | **0.0032** | ** |
| Site: UW (vs UAB) | -0.0783 | 1.1989 | ±2.3978 | -0.065 | 0.9479 |  |
| Season: spring (vs autumn) | -1.6570 | 1.3018 | ±2.6036 | -1.273 | 0.2031 |  |
| Season: summer (vs autumn) | +0.8318 | 1.2890 | ±2.5780 | +0.645 | 0.5187 |  |
| **Season: winter (vs autumn)** | **-5.1017** | 1.4586 | ±2.9173 | **-3.498** | **4.69e-04** | *** |
| Age (years) | +0.0246 | 0.0488 | ±0.0977 | +0.503 | 0.6149 |  |
| BMI (kg/m2) | -0.0565 | 0.0626 | ±0.1252 | -0.902 | 0.3671 |  |
| Hypertension | +0.2869 | 1.0930 | ±2.1859 | +0.262 | 0.7929 |  |
| **High cholesterol** | **-2.0049** | 0.9926 | ±1.9853 | **-2.020** | **0.0434** | * |
| Kidney disease | +1.2972 | 1.3391 | ±2.6783 | +0.969 | 0.3327 |  |
| Circulatory disease | -0.3367 | 1.1950 | ±2.3899 | -0.282 | 0.7781 |  |
| Time 181-250, pooled (%) | +0.1093 | 0.1215 | ±0.2430 | +0.900 | 0.3683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **198**, R² = **0.2103**, Adj R² = **0.1499**, F-statistic = **3.48** (p = **4.76e-05**), Residual SE = **6.042** on **183** df, AIC = **1288.6**, BIC = **1337.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5106** | 4.4713 | ±8.9426 | **+10.402** | **2.43e-25** | *** |
| Education: graduate level (vs college) | +0.8201 | 0.9531 | ±1.9062 | +0.861 | 0.3895 |  |
| Education: high school or below (vs college) | +1.8453 | 1.5573 | ±3.1146 | +1.185 | 0.2360 |  |
| **Site: UCSD (vs UAB)** | **+3.4044** | 1.1477 | ±2.2953 | **+2.966** | **0.0030** | ** |
| Site: UW (vs UAB) | -0.0870 | 1.1969 | ±2.3939 | -0.073 | 0.9421 |  |
| Season: spring (vs autumn) | -1.6506 | 1.2994 | ±2.5988 | -1.270 | 0.2040 |  |
| Season: summer (vs autumn) | +0.8158 | 1.2872 | ±2.5744 | +0.634 | 0.5262 |  |
| **Season: winter (vs autumn)** | **-5.1101** | 1.4572 | ±2.9145 | **-3.507** | **4.54e-04** | *** |
| Age (years) | +0.0239 | 0.0489 | ±0.0977 | +0.490 | 0.6242 |  |
| BMI (kg/m2) | -0.0559 | 0.0625 | ±0.1251 | -0.894 | 0.3714 |  |
| Hypertension | +0.2656 | 1.0936 | ±2.1872 | +0.243 | 0.8081 |  |
| **High cholesterol** | **-2.0025** | 0.9892 | ±1.9785 | **-2.024** | **0.0429** | * |
| Kidney disease | +1.2664 | 1.3303 | ±2.6605 | +0.952 | 0.3411 |  |
| Circulatory disease | -0.3433 | 1.1921 | ±2.3842 | -0.288 | 0.7734 |  |
| Avg. daily time 181-250 (%) | +0.1230 | 0.1190 | ±0.2380 | +1.034 | 0.3013 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **198**, R² = **0.2091**, Adj R² = **0.1486**, F-statistic = **3.46** (p = **5.30e-05**), Residual SE = **6.047** on **183** df, AIC = **1288.9**, BIC = **1338.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5089** | 4.4797 | ±8.9595 | **+10.382** | **2.99e-25** | *** |
| Education: graduate level (vs college) | +0.8189 | 0.9537 | ±1.9073 | +0.859 | 0.3905 |  |
| Education: high school or below (vs college) | +1.8328 | 1.5595 | ±3.1190 | +1.175 | 0.2399 |  |
| **Site: UCSD (vs UAB)** | **+3.3923** | 1.1506 | ±2.3012 | **+2.948** | **0.0032** | ** |
| Site: UW (vs UAB) | -0.0783 | 1.1989 | ±2.3978 | -0.065 | 0.9479 |  |
| Season: spring (vs autumn) | -1.6570 | 1.3018 | ±2.6036 | -1.273 | 0.2031 |  |
| Season: summer (vs autumn) | +0.8318 | 1.2890 | ±2.5780 | +0.645 | 0.5187 |  |
| **Season: winter (vs autumn)** | **-5.1017** | 1.4586 | ±2.9173 | **-3.498** | **4.69e-04** | *** |
| Age (years) | +0.0246 | 0.0488 | ±0.0977 | +0.503 | 0.6149 |  |
| BMI (kg/m2) | -0.0565 | 0.0626 | ±0.1252 | -0.902 | 0.3671 |  |
| Hypertension | +0.2869 | 1.0930 | ±2.1859 | +0.262 | 0.7929 |  |
| **High cholesterol** | **-2.0049** | 0.9926 | ±1.9853 | **-2.020** | **0.0434** | * |
| Kidney disease | +1.2972 | 1.3391 | ±2.6783 | +0.969 | 0.3327 |  |
| Circulatory disease | -0.3367 | 1.1950 | ±2.3899 | -0.282 | 0.7781 |  |
| Time > 180 (%) | +0.1093 | 0.1215 | ±0.2430 | +0.900 | 0.3683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **198**, R² = **0.2103**, Adj R² = **0.1499**, F-statistic = **3.48** (p = **4.76e-05**), Residual SE = **6.042** on **183** df, AIC = **1288.6**, BIC = **1337.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5106** | 4.4713 | ±8.9426 | **+10.402** | **2.43e-25** | *** |
| Education: graduate level (vs college) | +0.8201 | 0.9531 | ±1.9062 | +0.861 | 0.3895 |  |
| Education: high school or below (vs college) | +1.8453 | 1.5573 | ±3.1146 | +1.185 | 0.2360 |  |
| **Site: UCSD (vs UAB)** | **+3.4044** | 1.1477 | ±2.2953 | **+2.966** | **0.0030** | ** |
| Site: UW (vs UAB) | -0.0870 | 1.1969 | ±2.3939 | -0.073 | 0.9421 |  |
| Season: spring (vs autumn) | -1.6506 | 1.2994 | ±2.5988 | -1.270 | 0.2040 |  |
| Season: summer (vs autumn) | +0.8158 | 1.2872 | ±2.5744 | +0.634 | 0.5262 |  |
| **Season: winter (vs autumn)** | **-5.1101** | 1.4572 | ±2.9145 | **-3.507** | **4.54e-04** | *** |
| Age (years) | +0.0239 | 0.0489 | ±0.0977 | +0.490 | 0.6242 |  |
| BMI (kg/m2) | -0.0559 | 0.0625 | ±0.1251 | -0.894 | 0.3714 |  |
| Hypertension | +0.2656 | 1.0936 | ±2.1872 | +0.243 | 0.8081 |  |
| **High cholesterol** | **-2.0025** | 0.9892 | ±1.9785 | **-2.024** | **0.0429** | * |
| Kidney disease | +1.2664 | 1.3303 | ±2.6605 | +0.952 | 0.3411 |  |
| Circulatory disease | -0.3433 | 1.1921 | ±2.3842 | -0.288 | 0.7734 |  |
| Avg. daily time > 180 (%) | +0.1230 | 0.1190 | ±0.2380 | +1.034 | 0.3013 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 198)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **198**, R² = **0.2075**, Adj R² = **0.1468**, F-statistic = **3.42** (p = **6.13e-05**), Residual SE = **6.053** on **183** df, AIC = **1289.3**, BIC = **1338.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5512** | 4.4483 | ±8.8966 | **+10.465** | **1.25e-25** | *** |
| Education: graduate level (vs college) | +0.8547 | 0.9546 | ±1.9092 | +0.895 | 0.3706 |  |
| Education: high school or below (vs college) | +1.7734 | 1.5744 | ±3.1489 | +1.126 | 0.2600 |  |
| **Site: UCSD (vs UAB)** | **+3.4526** | 1.1692 | ±2.3384 | **+2.953** | **0.0031** | ** |
| Site: UW (vs UAB) | -0.0322 | 1.1982 | ±2.3963 | -0.027 | 0.9786 |  |
| Season: spring (vs autumn) | -1.7076 | 1.3036 | ±2.6072 | -1.310 | 0.1902 |  |
| Season: summer (vs autumn) | +0.8060 | 1.2831 | ±2.5662 | +0.628 | 0.5299 |  |
| **Season: winter (vs autumn)** | **-5.0788** | 1.4548 | ±2.9095 | **-3.491** | **4.81e-04** | *** |
| Age (years) | +0.0280 | 0.0488 | ±0.0976 | +0.574 | 0.5661 |  |
| BMI (kg/m2) | -0.0602 | 0.0620 | ±0.1241 | -0.970 | 0.3322 |  |
| Hypertension | +0.4254 | 1.0651 | ±2.1302 | +0.399 | 0.6896 |  |
| **High cholesterol** | **-2.0790** | 0.9847 | ±1.9694 | **-2.111** | **0.0347** | * |
| Kidney disease | +1.3238 | 1.3471 | ±2.6941 | +0.983 | 0.3257 |  |
| Circulatory disease | -0.3512 | 1.2138 | ±2.4276 | -0.289 | 0.7724 |  |
| Nocturnal time > 180 (%) | +0.0869 | 0.1265 | ±0.2531 | +0.687 | 0.4922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 198; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **198**, R² = **0.1205**, Adj R² = **0.0584**, F-statistic = **1.94** (p = **0.0283**), Residual SE = **16.521** on **184** df, AIC = **1686.0**, BIC = **1732.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.5849** | 11.1530 | ±22.3061 | **+12.157** | **5.28e-34** | *** |
| **Education: graduate level (vs college)** | **-5.6870** | 2.4925 | ±4.9850 | **-2.282** | **0.0225** | * |
| Education: high school or below (vs college) | +7.3691 | 4.4314 | ±8.8628 | +1.663 | 0.0963 | . |
| Site: UCSD (vs UAB) | +3.0172 | 3.1864 | ±6.3728 | +0.947 | 0.3437 |  |
| Site: UW (vs UAB) | -0.2211 | 3.2829 | ±6.5658 | -0.067 | 0.9463 |  |
| Season: spring (vs autumn) | -0.1182 | 3.5615 | ±7.1231 | -0.033 | 0.9735 |  |
| Season: summer (vs autumn) | +0.8371 | 3.8640 | ±7.7280 | +0.217 | 0.8285 |  |
| Season: winter (vs autumn) | +4.7515 | 4.0906 | ±8.1812 | +1.162 | 0.2454 |  |
| Age (years) | -0.2303 | 0.1284 | ±0.2567 | -1.794 | 0.0728 | . |
| BMI (kg/m2) | +0.1509 | 0.1792 | ±0.3583 | +0.842 | 0.3998 |  |
| Hypertension | +0.7651 | 2.6569 | ±5.3139 | +0.288 | 0.7734 |  |
| High cholesterol | -0.8232 | 2.5495 | ±5.0990 | -0.323 | 0.7468 |  |
| Kidney disease | -4.2389 | 3.6895 | ±7.3791 | -1.149 | 0.2506 |  |
| Circulatory disease | -0.2007 | 3.2430 | ±6.4860 | -0.062 | 0.9506 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **198**, R² = **0.1207**, Adj R² = **0.0534**, F-statistic = **1.79** (p = **0.0422**), Residual SE = **16.564** on **183** df, AIC = **1688.0**, BIC = **1737.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+133.0881** | 21.0413 | ±42.0825 | **+6.325** | **2.53e-10** | *** |
| **Education: graduate level (vs college)** | **-5.6692** | 2.4911 | ±4.9823 | **-2.276** | **0.0229** | * |
| Education: high school or below (vs college) | +7.3492 | 4.5119 | ±9.0238 | +1.629 | 0.1033 |  |
| Site: UCSD (vs UAB) | +3.0216 | 3.2038 | ±6.4077 | +0.943 | 0.3456 |  |
| Site: UW (vs UAB) | -0.2128 | 3.3124 | ±6.6247 | -0.064 | 0.9488 |  |
| Season: spring (vs autumn) | -0.1035 | 3.5530 | ±7.1059 | -0.029 | 0.9768 |  |
| Season: summer (vs autumn) | +0.7801 | 4.1221 | ±8.2441 | +0.189 | 0.8499 |  |
| Season: winter (vs autumn) | +4.7166 | 4.2469 | ±8.4938 | +1.111 | 0.2667 |  |
| Age (years) | -0.2308 | 0.1290 | ±0.2579 | -1.790 | 0.0735 | . |
| BMI (kg/m2) | +0.1434 | 0.1667 | ±0.3334 | +0.860 | 0.3896 |  |
| Hypertension | +0.7496 | 2.6780 | ±5.3560 | +0.280 | 0.7796 |  |
| High cholesterol | -0.8715 | 2.4740 | ±4.9481 | -0.352 | 0.7246 |  |
| Kidney disease | -4.1663 | 3.7045 | ±7.4089 | -1.125 | 0.2607 |  |
| Circulatory disease | -0.3039 | 3.5633 | ±7.1266 | -0.085 | 0.9320 |  |
| HbA1c (%) | +0.4709 | 3.2948 | ±6.5897 | +0.143 | 0.8864 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **198**, R² = **0.1244**, Adj R² = **0.0575**, F-statistic = **1.86** (p = **0.0336**), Residual SE = **16.529** on **183** df, AIC = **1687.1**, BIC = **1736.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1537** | 15.3413 | ±30.6827 | **+8.158** | **3.41e-16** | *** |
| **Education: graduate level (vs college)** | **-5.6887** | 2.5132 | ±5.0263 | **-2.264** | **0.0236** | * |
| Education: high school or below (vs college) | +7.5741 | 4.3785 | ±8.7570 | +1.730 | 0.0837 | . |
| Site: UCSD (vs UAB) | +3.0359 | 3.2036 | ±6.4071 | +0.948 | 0.3433 |  |
| Site: UW (vs UAB) | -0.1277 | 3.3168 | ±6.6336 | -0.039 | 0.9693 |  |
| Season: spring (vs autumn) | -0.2020 | 3.6016 | ±7.2032 | -0.056 | 0.9553 |  |
| Season: summer (vs autumn) | +0.5028 | 4.0486 | ±8.0972 | +0.124 | 0.9012 |  |
| Season: winter (vs autumn) | +4.6091 | 4.1715 | ±8.3430 | +1.105 | 0.2692 |  |
| Age (years) | -0.2286 | 0.1290 | ±0.2580 | -1.773 | 0.0763 | . |
| BMI (kg/m2) | +0.1371 | 0.1777 | ±0.3553 | +0.772 | 0.4402 |  |
| Hypertension | +0.6189 | 2.6347 | ±5.2695 | +0.235 | 0.8143 |  |
| High cholesterol | -0.7367 | 2.5814 | ±5.1629 | -0.285 | 0.7754 |  |
| Kidney disease | -4.5028 | 3.7298 | ±7.4597 | -1.207 | 0.2273 |  |
| Circulatory disease | -0.3251 | 3.2826 | ±6.5651 | -0.099 | 0.9211 |  |
| Mean glucose (mg/dL) | +0.0860 | 0.1046 | ±0.2092 | +0.822 | 0.4109 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **198**, R² = **0.1244**, Adj R² = **0.0575**, F-statistic = **1.86** (p = **0.0336**), Residual SE = **16.529** on **183** df, AIC = **1687.1**, BIC = **1736.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+113.2540** | 27.4362 | ±54.8725 | **+4.128** | **3.66e-05** | *** |
| **Education: graduate level (vs college)** | **-5.6887** | 2.5132 | ±5.0263 | **-2.264** | **0.0236** | * |
| Education: high school or below (vs college) | +7.5741 | 4.3785 | ±8.7570 | +1.730 | 0.0837 | . |
| Site: UCSD (vs UAB) | +3.0359 | 3.2036 | ±6.4071 | +0.948 | 0.3433 |  |
| Site: UW (vs UAB) | -0.1277 | 3.3168 | ±6.6336 | -0.039 | 0.9693 |  |
| Season: spring (vs autumn) | -0.2020 | 3.6016 | ±7.2032 | -0.056 | 0.9553 |  |
| Season: summer (vs autumn) | +0.5028 | 4.0486 | ±8.0972 | +0.124 | 0.9012 |  |
| Season: winter (vs autumn) | +4.6091 | 4.1715 | ±8.3430 | +1.105 | 0.2692 |  |
| Age (years) | -0.2286 | 0.1290 | ±0.2580 | -1.773 | 0.0763 | . |
| BMI (kg/m2) | +0.1371 | 0.1777 | ±0.3553 | +0.772 | 0.4402 |  |
| Hypertension | +0.6189 | 2.6347 | ±5.2695 | +0.235 | 0.8143 |  |
| High cholesterol | -0.7367 | 2.5814 | ±5.1629 | -0.285 | 0.7754 |  |
| Kidney disease | -4.5028 | 3.7298 | ±7.4597 | -1.207 | 0.2273 |  |
| Circulatory disease | -0.3251 | 3.2826 | ±6.5651 | -0.099 | 0.9211 |  |
| GMI (%) | +3.5951 | 4.3724 | ±8.7448 | +0.822 | 0.4109 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **198**, R² = **0.1209**, Adj R² = **0.0536**, F-statistic = **1.80** (p = **0.0417**), Residual SE = **16.562** on **183** df, AIC = **1687.9**, BIC = **1737.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.6290** | 15.4452 | ±30.8903 | **+8.587** | **8.92e-18** | *** |
| **Education: graduate level (vs college)** | **-5.7129** | 2.5270 | ±5.0540 | **-2.261** | **0.0238** | * |
| Education: high school or below (vs college) | +7.4114 | 4.4091 | ±8.8182 | +1.681 | 0.0928 | . |
| Site: UCSD (vs UAB) | +3.0014 | 3.2125 | ±6.4251 | +0.934 | 0.3502 |  |
| Site: UW (vs UAB) | -0.2130 | 3.3085 | ±6.6171 | -0.064 | 0.9487 |  |
| Season: spring (vs autumn) | -0.1230 | 3.5893 | ±7.1785 | -0.034 | 0.9727 |  |
| Season: summer (vs autumn) | +0.7629 | 4.0060 | ±8.0120 | +0.190 | 0.8490 |  |
| Season: winter (vs autumn) | +4.7482 | 4.1173 | ±8.2347 | +1.153 | 0.2488 |  |
| Age (years) | -0.2270 | 0.1296 | ±0.2591 | -1.752 | 0.0797 | . |
| BMI (kg/m2) | +0.1451 | 0.1807 | ±0.3614 | +0.803 | 0.4218 |  |
| Hypertension | +0.7486 | 2.6594 | ±5.3189 | +0.281 | 0.7783 |  |
| High cholesterol | -0.8330 | 2.5637 | ±5.1273 | -0.325 | 0.7452 |  |
| Kidney disease | -4.2494 | 3.7081 | ±7.4163 | -1.146 | 0.2518 |  |
| Circulatory disease | -0.2628 | 3.2600 | ±6.5200 | -0.081 | 0.9358 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0236 | 0.0922 | ±0.1844 | +0.256 | 0.7982 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **198**, R² = **0.1265**, Adj R² = **0.0597**, F-statistic = **1.89** (p = **0.0295**), Residual SE = **16.509** on **183** df, AIC = **1686.6**, BIC = **1736.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.6635** | 10.6649 | ±21.3297 | **+12.158** | **5.20e-34** | *** |
| **Education: graduate level (vs college)** | **-5.8837** | 2.5388 | ±5.0775 | **-2.318** | **0.0205** | * |
| Education: high school or below (vs college) | +6.5977 | 4.7201 | ±9.4402 | +1.398 | 0.1622 |  |
| Site: UCSD (vs UAB) | +3.2884 | 3.2695 | ±6.5390 | +1.006 | 0.3145 |  |
| Site: UW (vs UAB) | +0.3185 | 3.3736 | ±6.7472 | +0.094 | 0.9248 |  |
| Season: spring (vs autumn) | -0.1019 | 3.5340 | ±7.0681 | -0.029 | 0.9770 |  |
| Season: summer (vs autumn) | +0.8698 | 3.8727 | ±7.7455 | +0.225 | 0.8223 |  |
| Season: winter (vs autumn) | +4.7649 | 4.0812 | ±8.1623 | +1.168 | 0.2430 |  |
| Age (years) | -0.2413 | 0.1334 | ±0.2668 | -1.809 | 0.0705 | . |
| BMI (kg/m2) | +0.1537 | 0.1803 | ±0.3606 | +0.853 | 0.3939 |  |
| Hypertension | +0.2667 | 2.6108 | ±5.2217 | +0.102 | 0.9186 |  |
| High cholesterol | -0.6173 | 2.5673 | ±5.1347 | -0.240 | 0.8100 |  |
| Kidney disease | -4.8615 | 3.7119 | ±7.4238 | -1.310 | 0.1903 |  |
| Circulatory disease | -0.4218 | 3.2884 | ±6.5768 | -0.128 | 0.8979 |  |
| Glucose SD, pooled (mg/dL) | +0.3069 | 0.2993 | ±0.5987 | +1.025 | 0.3053 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **198**, R² = **0.1276**, Adj R² = **0.0609**, F-statistic = **1.91** (p = **0.0276**), Residual SE = **16.499** on **183** df, AIC = **1686.4**, BIC = **1735.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.6827** | 10.3636 | ±20.7272 | **+12.513** | **6.31e-36** | *** |
| **Education: graduate level (vs college)** | **-5.8671** | 2.5250 | ±5.0501 | **-2.324** | **0.0201** | * |
| Education: high school or below (vs college) | +6.6796 | 4.5789 | ±9.1579 | +1.459 | 0.1446 |  |
| Site: UCSD (vs UAB) | +3.1233 | 3.2193 | ±6.4385 | +0.970 | 0.3320 |  |
| Site: UW (vs UAB) | +0.1954 | 3.3381 | ±6.6763 | +0.059 | 0.9533 |  |
| Season: spring (vs autumn) | +0.0111 | 3.4973 | ±6.9946 | +0.003 | 0.9975 |  |
| Season: summer (vs autumn) | +0.9925 | 3.8282 | ±7.6564 | +0.259 | 0.7954 |  |
| Season: winter (vs autumn) | +4.8351 | 4.0592 | ±8.1184 | +1.191 | 0.2336 |  |
| Age (years) | -0.2430 | 0.1337 | ±0.2674 | -1.818 | 0.0691 | . |
| BMI (kg/m2) | +0.1543 | 0.1799 | ±0.3597 | +0.858 | 0.3911 |  |
| Hypertension | +0.0877 | 2.6017 | ±5.2033 | +0.034 | 0.9731 |  |
| High cholesterol | -0.5891 | 2.5660 | ±5.1319 | -0.230 | 0.8184 |  |
| Kidney disease | -4.7186 | 3.6785 | ±7.3569 | -1.283 | 0.1996 |  |
| Circulatory disease | -0.2727 | 3.2550 | ±6.5101 | -0.084 | 0.9332 |  |
| Avg. daily SD (mg/dL) | +0.3383 | 0.2845 | ±0.5689 | +1.189 | 0.2344 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **198**, R² = **0.1236**, Adj R² = **0.0566**, F-statistic = **1.84** (p = **0.0354**), Residual SE = **16.537** on **183** df, AIC = **1687.3**, BIC = **1736.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.3668** | 10.6387 | ±21.2774 | **+12.254** | **1.60e-34** | *** |
| **Education: graduate level (vs college)** | **-5.8445** | 2.5233 | ±5.0466 | **-2.316** | **0.0205** | * |
| Education: high school or below (vs college) | +6.5852 | 4.7352 | ±9.4705 | +1.391 | 0.1643 |  |
| Site: UCSD (vs UAB) | +3.2466 | 3.2848 | ±6.5695 | +0.988 | 0.3230 |  |
| Site: UW (vs UAB) | +0.1915 | 3.3615 | ±6.7229 | +0.057 | 0.9546 |  |
| Season: spring (vs autumn) | -0.0692 | 3.5311 | ±7.0622 | -0.020 | 0.9844 |  |
| Season: summer (vs autumn) | +1.0349 | 3.8401 | ±7.6802 | +0.269 | 0.7876 |  |
| Season: winter (vs autumn) | +4.8057 | 4.0713 | ±8.1426 | +1.180 | 0.2379 |  |
| Age (years) | -0.2408 | 0.1332 | ±0.2664 | -1.808 | 0.0707 | . |
| BMI (kg/m2) | +0.1602 | 0.1797 | ±0.3593 | +0.892 | 0.3727 |  |
| Hypertension | +0.4129 | 2.6490 | ±5.2979 | +0.156 | 0.8761 |  |
| High cholesterol | -0.6940 | 2.5443 | ±5.0886 | -0.273 | 0.7850 |  |
| Kidney disease | -4.6419 | 3.6767 | ±7.3534 | -1.263 | 0.2068 |  |
| Circulatory disease | -0.2988 | 3.2618 | ±6.5235 | -0.092 | 0.9270 |  |
| CV (%) | +0.3296 | 0.3743 | ±0.7486 | +0.880 | 0.3786 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **198**, R² = **0.1284**, Adj R² = **0.0617**, F-statistic = **1.93** (p = **0.0262**), Residual SE = **16.491** on **183** df, AIC = **1686.2**, BIC = **1735.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+144.9412** | 14.8741 | ±29.7482 | **+9.745** | **1.95e-22** | *** |
| **Education: graduate level (vs college)** | **-5.8900** | 2.5180 | ±5.0361 | **-2.339** | **0.0193** | * |
| Education: high school or below (vs college) | +6.2683 | 4.6556 | ±9.3112 | +1.346 | 0.1782 |  |
| Site: UCSD (vs UAB) | +3.2974 | 3.2354 | ±6.4708 | +1.019 | 0.3081 |  |
| Site: UW (vs UAB) | +0.3538 | 3.3501 | ±6.7001 | +0.106 | 0.9159 |  |
| Season: spring (vs autumn) | -0.0485 | 3.5164 | ±7.0327 | -0.014 | 0.9890 |  |
| Season: summer (vs autumn) | +1.1181 | 3.8611 | ±7.7223 | +0.290 | 0.7721 |  |
| Season: winter (vs autumn) | +4.8048 | 4.0653 | ±8.1305 | +1.182 | 0.2372 |  |
| Age (years) | -0.2475 | 0.1323 | ±0.2646 | -1.870 | 0.0614 | . |
| BMI (kg/m2) | +0.1560 | 0.1798 | ±0.3596 | +0.868 | 0.3856 |  |
| Hypertension | +0.1728 | 2.6309 | ±5.2617 | +0.066 | 0.9476 |  |
| High cholesterol | -0.6880 | 2.5367 | ±5.0734 | -0.271 | 0.7862 |  |
| Kidney disease | -4.8552 | 3.6727 | ±7.3454 | -1.322 | 0.1862 |  |
| Circulatory disease | -0.2630 | 3.2480 | ±6.4961 | -0.081 | 0.9355 |  |
| Mean / SD ratio | -1.3653 | 0.9275 | ±1.8550 | -1.472 | 0.1410 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **198**, R² = **0.1298**, Adj R² = **0.0632**, F-statistic = **1.95** (p = **0.0240**), Residual SE = **16.478** on **183** df, AIC = **1685.9**, BIC = **1735.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+144.8233** | 14.1236 | ±28.2473 | **+10.254** | **1.14e-24** | *** |
| **Education: graduate level (vs college)** | **-5.7987** | 2.5041 | ±5.0082 | **-2.316** | **0.0206** | * |
| Education: high school or below (vs college) | +6.4496 | 4.5141 | ±9.0283 | +1.429 | 0.1531 |  |
| Site: UCSD (vs UAB) | +2.9858 | 3.1840 | ±6.3681 | +0.938 | 0.3484 |  |
| Site: UW (vs UAB) | +0.2088 | 3.3150 | ±6.6300 | +0.063 | 0.9498 |  |
| Season: spring (vs autumn) | +0.0151 | 3.5159 | ±7.0318 | +0.004 | 0.9966 |  |
| Season: summer (vs autumn) | +1.2249 | 3.8520 | ±7.7040 | +0.318 | 0.7505 |  |
| Season: winter (vs autumn) | +4.9576 | 4.0504 | ±8.1008 | +1.224 | 0.2210 |  |
| Age (years) | -0.2503 | 0.1322 | ±0.2643 | -1.894 | 0.0582 | . |
| BMI (kg/m2) | +0.1540 | 0.1791 | ±0.3582 | +0.860 | 0.3899 |  |
| Hypertension | -0.0824 | 2.6343 | ±5.2685 | -0.031 | 0.9750 |  |
| High cholesterol | -0.7558 | 2.5343 | ±5.0686 | -0.298 | 0.7655 |  |
| Kidney disease | -4.7114 | 3.6687 | ±7.3374 | -1.284 | 0.1991 |  |
| Circulatory disease | +0.0327 | 3.2284 | ±6.4568 | +0.010 | 0.9919 |  |
| Avg. daily mean/SD | -1.1312 | 0.6498 | ±1.2996 | -1.741 | 0.0817 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **198**, R² = **0.1214**, Adj R² = **0.0542**, F-statistic = **1.81** (p = **0.0404**), Residual SE = **16.557** on **183** df, AIC = **1687.8**, BIC = **1737.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.6769** | 13.4891 | ±26.9783 | **+9.836** | **7.89e-23** | *** |
| **Education: graduate level (vs college)** | **-5.7078** | 2.5149 | ±5.0297 | **-2.270** | **0.0232** | * |
| Education: high school or below (vs college) | +7.2308 | 4.5468 | ±9.0936 | +1.590 | 0.1118 |  |
| Site: UCSD (vs UAB) | +3.0121 | 3.2054 | ±6.4107 | +0.940 | 0.3474 |  |
| Site: UW (vs UAB) | -0.1485 | 3.2778 | ±6.5556 | -0.045 | 0.9639 |  |
| Season: spring (vs autumn) | -0.0947 | 3.5541 | ±7.1082 | -0.027 | 0.9787 |  |
| Season: summer (vs autumn) | +0.8580 | 3.8531 | ±7.7062 | +0.223 | 0.8238 |  |
| Season: winter (vs autumn) | +4.7876 | 4.0810 | ±8.1621 | +1.173 | 0.2407 |  |
| Age (years) | -0.2289 | 0.1289 | ±0.2578 | -1.776 | 0.0758 | . |
| BMI (kg/m2) | +0.1481 | 0.1784 | ±0.3568 | +0.830 | 0.4063 |  |
| Hypertension | +0.6920 | 2.6833 | ±5.3666 | +0.258 | 0.7965 |  |
| High cholesterol | -0.8714 | 2.5282 | ±5.0563 | -0.345 | 0.7303 |  |
| Kidney disease | -4.2313 | 3.7045 | ±7.4089 | -1.142 | 0.2534 |  |
| Circulatory disease | -0.1085 | 3.2168 | ±6.4335 | -0.034 | 0.9731 |  |
| MAG (mg/dL/h) | +0.0812 | 0.2016 | ±0.4032 | +0.403 | 0.6870 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **198**, R² = **0.1219**, Adj R² = **0.0547**, F-statistic = **1.81** (p = **0.0392**), Residual SE = **16.552** on **183** df, AIC = **1687.7**, BIC = **1737.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.1885** | 11.0434 | ±22.0868 | **+11.970** | **5.11e-33** | *** |
| **Education: graduate level (vs college)** | **-5.7289** | 2.5179 | ±5.0357 | **-2.275** | **0.0229** | * |
| Education: high school or below (vs college) | +7.1238 | 4.5532 | ±9.1064 | +1.565 | 0.1177 |  |
| Site: UCSD (vs UAB) | +3.1052 | 3.2392 | ±6.4784 | +0.959 | 0.3377 |  |
| Site: UW (vs UAB) | -0.0446 | 3.2989 | ±6.5978 | -0.014 | 0.9892 |  |
| Season: spring (vs autumn) | -0.0905 | 3.5501 | ±7.1003 | -0.026 | 0.9797 |  |
| Season: summer (vs autumn) | +0.9270 | 3.8070 | ±7.6139 | +0.244 | 0.8076 |  |
| Season: winter (vs autumn) | +4.8119 | 4.0625 | ±8.1251 | +1.184 | 0.2362 |  |
| Age (years) | -0.2365 | 0.1340 | ±0.2679 | -1.765 | 0.0775 | . |
| BMI (kg/m2) | +0.1571 | 0.1818 | ±0.3635 | +0.864 | 0.3874 |  |
| Hypertension | +0.5436 | 2.6461 | ±5.2921 | +0.205 | 0.8372 |  |
| High cholesterol | -0.7760 | 2.5771 | ±5.1541 | -0.301 | 0.7633 |  |
| Kidney disease | -4.3716 | 3.7015 | ±7.4030 | -1.181 | 0.2376 |  |
| Circulatory disease | -0.1908 | 3.2603 | ±6.5206 | -0.059 | 0.9533 |  |
| Avg. daily range (mg/dL) | +0.0373 | 0.0704 | ±0.1408 | +0.530 | 0.5960 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **198**, R² = **0.1301**, Adj R² = **0.0636**, F-statistic = **1.96** (p = **0.0235**), Residual SE = **16.475** on **183** df, AIC = **1685.8**, BIC = **1735.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+131.2293** | 11.5171 | ±23.0342 | **+11.394** | **4.47e-30** | *** |
| **Education: graduate level (vs college)** | **-5.8948** | 2.5502 | ±5.1003 | **-2.312** | **0.0208** | * |
| Education: high school or below (vs college) | +6.4044 | 4.9685 | ±9.9370 | +1.289 | 0.1974 |  |
| Site: UCSD (vs UAB) | +3.7634 | 3.3089 | ±6.6179 | +1.137 | 0.2554 |  |
| Site: UW (vs UAB) | +0.6355 | 3.4419 | ±6.8838 | +0.185 | 0.8535 |  |
| Season: spring (vs autumn) | -0.4531 | 3.6165 | ±7.2330 | -0.125 | 0.9003 |  |
| Season: summer (vs autumn) | +0.1705 | 4.1957 | ±8.3915 | +0.041 | 0.9676 |  |
| Season: winter (vs autumn) | +4.7105 | 4.0697 | ±8.1393 | +1.157 | 0.2471 |  |
| Age (years) | -0.2346 | 0.1290 | ±0.2580 | -1.819 | 0.0690 | . |
| BMI (kg/m2) | +0.1487 | 0.1790 | ±0.3580 | +0.831 | 0.4062 |  |
| Hypertension | +1.0632 | 2.6750 | ±5.3500 | +0.397 | 0.6910 |  |
| High cholesterol | -0.9296 | 2.5201 | ±5.0402 | -0.369 | 0.7122 |  |
| Kidney disease | -5.1763 | 3.8434 | ±7.6868 | -1.347 | 0.1780 |  |
| Circulatory disease | -1.1855 | 3.3426 | ±6.6853 | -0.355 | 0.7228 |  |
| SD of daily means (mg/dL) | +0.7219 | 0.6744 | ±1.3489 | +1.070 | 0.2844 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **198**, R² = **0.1229**, Adj R² = **0.0558**, F-statistic = **1.83** (p = **0.0369**), Residual SE = **16.543** on **183** df, AIC = **1687.5**, BIC = **1736.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+154.0705** | 40.2900 | ±80.5801 | **+3.824** | **1.31e-04** | *** |
| **Education: graduate level (vs college)** | **-5.7973** | 2.5611 | ±5.1222 | **-2.264** | **0.0236** | * |
| Education: high school or below (vs college) | +7.1359 | 4.5859 | ±9.1718 | +1.556 | 0.1197 |  |
| Site: UCSD (vs UAB) | +3.1823 | 3.2875 | ±6.5751 | +0.968 | 0.3331 |  |
| Site: UW (vs UAB) | -0.0513 | 3.3602 | ±6.7204 | -0.015 | 0.9878 |  |
| Season: spring (vs autumn) | -0.0975 | 3.5607 | ±7.1214 | -0.027 | 0.9782 |  |
| Season: summer (vs autumn) | +0.7040 | 4.0192 | ±8.0383 | +0.175 | 0.8609 |  |
| Season: winter (vs autumn) | +4.6781 | 4.1898 | ±8.3797 | +1.117 | 0.2642 |  |
| Age (years) | -0.2397 | 0.1368 | ±0.2737 | -1.751 | 0.0799 | . |
| BMI (kg/m2) | +0.1480 | 0.1802 | ±0.3604 | +0.821 | 0.4116 |  |
| Hypertension | +0.6599 | 2.6398 | ±5.2796 | +0.250 | 0.8026 |  |
| High cholesterol | -0.7136 | 2.5933 | ±5.1866 | -0.275 | 0.7832 |  |
| Kidney disease | -4.6160 | 3.8388 | ±7.6776 | -1.202 | 0.2292 |  |
| Circulatory disease | -0.3050 | 3.3065 | ±6.6131 | -0.092 | 0.9265 |  |
| Time in range 70-180, pooled (%) | -0.1850 | 0.3538 | ±0.7077 | -0.523 | 0.6011 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **198**, R² = **0.1226**, Adj R² = **0.0555**, F-statistic = **1.83** (p = **0.0375**), Residual SE = **16.546** on **183** df, AIC = **1687.5**, BIC = **1736.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+153.4531** | 41.0295 | ±82.0589 | **+3.740** | **1.84e-04** | *** |
| **Education: graduate level (vs college)** | **-5.7805** | 2.5580 | ±5.1160 | **-2.260** | **0.0238** | * |
| Education: high school or below (vs college) | +7.1850 | 4.5511 | ±9.1021 | +1.579 | 0.1144 |  |
| Site: UCSD (vs UAB) | +3.1734 | 3.2874 | ±6.5749 | +0.965 | 0.3344 |  |
| Site: UW (vs UAB) | -0.0909 | 3.3614 | ±6.7227 | -0.027 | 0.9784 |  |
| Season: spring (vs autumn) | -0.0892 | 3.5519 | ±7.1038 | -0.025 | 0.9800 |  |
| Season: summer (vs autumn) | +0.7052 | 4.0197 | ±8.0393 | +0.175 | 0.8607 |  |
| Season: winter (vs autumn) | +4.6775 | 4.1940 | ±8.3880 | +1.115 | 0.2647 |  |
| Age (years) | -0.2394 | 0.1372 | ±0.2743 | -1.745 | 0.0809 | . |
| BMI (kg/m2) | +0.1492 | 0.1803 | ±0.3606 | +0.827 | 0.4080 |  |
| Hypertension | +0.6407 | 2.6271 | ±5.2541 | +0.244 | 0.8073 |  |
| High cholesterol | -0.7263 | 2.5934 | ±5.1869 | -0.280 | 0.7794 |  |
| Kidney disease | -4.6035 | 3.8448 | ±7.6896 | -1.197 | 0.2312 |  |
| Circulatory disease | -0.2955 | 3.3046 | ±6.6092 | -0.089 | 0.9288 |  |
| Avg. daily time in range 70-180 (%) | -0.1787 | 0.3609 | ±0.7219 | -0.495 | 0.6206 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **198**, R² = **0.1211**, Adj R² = **0.0538**, F-statistic = **1.80** (p = **0.0412**), Residual SE = **16.560** on **183** df, AIC = **1687.9**, BIC = **1737.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.4705** | 11.2172 | ±22.4345 | **+12.077** | **1.40e-33** | *** |
| **Education: graduate level (vs college)** | **-5.6287** | 2.5005 | ±5.0010 | **-2.251** | **0.0244** | * |
| Education: high school or below (vs college) | +7.5566 | 4.4579 | ±8.9158 | +1.695 | 0.0901 | . |
| Site: UCSD (vs UAB) | +2.9419 | 3.2290 | ±6.4580 | +0.911 | 0.3622 |  |
| Site: UW (vs UAB) | -0.2426 | 3.3038 | ±6.6076 | -0.073 | 0.9415 |  |
| Season: spring (vs autumn) | -0.2324 | 3.6269 | ±7.2537 | -0.064 | 0.9489 |  |
| Season: summer (vs autumn) | +0.7717 | 3.8975 | ±7.7950 | +0.198 | 0.8431 |  |
| Season: winter (vs autumn) | +4.6239 | 4.1499 | ±8.2997 | +1.114 | 0.2652 |  |
| Age (years) | -0.2235 | 0.1313 | ±0.2626 | -1.702 | 0.0887 | . |
| BMI (kg/m2) | +0.1475 | 0.1794 | ±0.3588 | +0.822 | 0.4111 |  |
| Hypertension | +0.8051 | 2.6778 | ±5.3557 | +0.301 | 0.7637 |  |
| High cholesterol | -0.7683 | 2.5702 | ±5.1405 | -0.299 | 0.7650 |  |
| Kidney disease | -4.3027 | 3.7081 | ±7.4163 | -1.160 | 0.2459 |  |
| Circulatory disease | -0.1937 | 3.2516 | ±6.5032 | -0.060 | 0.9525 |  |
| Time 54-69, pooled (%) | -1.5724 | 4.1474 | ±8.2947 | -0.379 | 0.7046 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **198**, R² = **0.1206**, Adj R² = **0.0534**, F-statistic = **1.79** (p = **0.0423**), Residual SE = **16.564** on **183** df, AIC = **1688.0**, BIC = **1737.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.4959** | 11.2107 | ±22.4215 | **+12.086** | **1.25e-33** | *** |
| **Education: graduate level (vs college)** | **-5.6593** | 2.5031 | ±5.0062 | **-2.261** | **0.0238** | * |
| Education: high school or below (vs college) | +7.4582 | 4.4386 | ±8.8772 | +1.680 | 0.0929 | . |
| Site: UCSD (vs UAB) | +2.9980 | 3.2083 | ±6.4166 | +0.934 | 0.3501 |  |
| Site: UW (vs UAB) | -0.2176 | 3.2962 | ±6.5924 | -0.066 | 0.9474 |  |
| Season: spring (vs autumn) | -0.1751 | 3.6145 | ±7.2290 | -0.048 | 0.9614 |  |
| Season: summer (vs autumn) | +0.7859 | 3.9234 | ±7.8469 | +0.200 | 0.8412 |  |
| Season: winter (vs autumn) | +4.6916 | 4.1439 | ±8.2877 | +1.132 | 0.2576 |  |
| Age (years) | -0.2268 | 0.1314 | ±0.2629 | -1.725 | 0.0845 | . |
| BMI (kg/m2) | +0.1493 | 0.1796 | ±0.3591 | +0.831 | 0.4057 |  |
| Hypertension | +0.7952 | 2.6814 | ±5.3628 | +0.297 | 0.7668 |  |
| High cholesterol | -0.7964 | 2.5649 | ±5.1298 | -0.310 | 0.7562 |  |
| Kidney disease | -4.2823 | 3.7205 | ±7.4410 | -1.151 | 0.2497 |  |
| Circulatory disease | -0.2159 | 3.2672 | ±6.5344 | -0.066 | 0.9473 |  |
| Avg. daily time 54-69 (%) | -0.7546 | 3.6930 | ±7.3860 | -0.204 | 0.8381 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **198**, R² = **0.1211**, Adj R² = **0.0538**, F-statistic = **1.80** (p = **0.0412**), Residual SE = **16.560** on **183** df, AIC = **1687.9**, BIC = **1737.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.4705** | 11.2172 | ±22.4345 | **+12.077** | **1.40e-33** | *** |
| **Education: graduate level (vs college)** | **-5.6287** | 2.5005 | ±5.0010 | **-2.251** | **0.0244** | * |
| Education: high school or below (vs college) | +7.5566 | 4.4579 | ±8.9158 | +1.695 | 0.0901 | . |
| Site: UCSD (vs UAB) | +2.9419 | 3.2290 | ±6.4580 | +0.911 | 0.3622 |  |
| Site: UW (vs UAB) | -0.2426 | 3.3038 | ±6.6076 | -0.073 | 0.9415 |  |
| Season: spring (vs autumn) | -0.2324 | 3.6269 | ±7.2537 | -0.064 | 0.9489 |  |
| Season: summer (vs autumn) | +0.7717 | 3.8975 | ±7.7950 | +0.198 | 0.8431 |  |
| Season: winter (vs autumn) | +4.6239 | 4.1499 | ±8.2997 | +1.114 | 0.2652 |  |
| Age (years) | -0.2235 | 0.1313 | ±0.2626 | -1.702 | 0.0887 | . |
| BMI (kg/m2) | +0.1475 | 0.1794 | ±0.3588 | +0.822 | 0.4111 |  |
| Hypertension | +0.8051 | 2.6778 | ±5.3557 | +0.301 | 0.7637 |  |
| High cholesterol | -0.7683 | 2.5702 | ±5.1405 | -0.299 | 0.7650 |  |
| Kidney disease | -4.3027 | 3.7081 | ±7.4163 | -1.160 | 0.2459 |  |
| Circulatory disease | -0.1937 | 3.2516 | ±6.5032 | -0.060 | 0.9525 |  |
| Time < 70 (%) | -1.5724 | 4.1474 | ±8.2947 | -0.379 | 0.7046 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **198**, R² = **0.1206**, Adj R² = **0.0534**, F-statistic = **1.79** (p = **0.0423**), Residual SE = **16.564** on **183** df, AIC = **1688.0**, BIC = **1737.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.4959** | 11.2107 | ±22.4215 | **+12.086** | **1.25e-33** | *** |
| **Education: graduate level (vs college)** | **-5.6593** | 2.5031 | ±5.0062 | **-2.261** | **0.0238** | * |
| Education: high school or below (vs college) | +7.4582 | 4.4386 | ±8.8772 | +1.680 | 0.0929 | . |
| Site: UCSD (vs UAB) | +2.9980 | 3.2083 | ±6.4166 | +0.934 | 0.3501 |  |
| Site: UW (vs UAB) | -0.2176 | 3.2962 | ±6.5924 | -0.066 | 0.9474 |  |
| Season: spring (vs autumn) | -0.1751 | 3.6145 | ±7.2290 | -0.048 | 0.9614 |  |
| Season: summer (vs autumn) | +0.7859 | 3.9234 | ±7.8469 | +0.200 | 0.8412 |  |
| Season: winter (vs autumn) | +4.6916 | 4.1439 | ±8.2877 | +1.132 | 0.2576 |  |
| Age (years) | -0.2268 | 0.1314 | ±0.2629 | -1.725 | 0.0845 | . |
| BMI (kg/m2) | +0.1493 | 0.1796 | ±0.3591 | +0.831 | 0.4057 |  |
| Hypertension | +0.7952 | 2.6814 | ±5.3628 | +0.297 | 0.7668 |  |
| High cholesterol | -0.7964 | 2.5649 | ±5.1298 | -0.310 | 0.7562 |  |
| Kidney disease | -4.2823 | 3.7205 | ±7.4410 | -1.151 | 0.2497 |  |
| Circulatory disease | -0.2159 | 3.2672 | ±6.5344 | -0.066 | 0.9473 |  |
| Avg. daily time < 70 (%) | -0.7546 | 3.6930 | ±7.3860 | -0.204 | 0.8381 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **198**, R² = **0.1230**, Adj R² = **0.0559**, F-statistic = **1.83** (p = **0.0367**), Residual SE = **16.542** on **183** df, AIC = **1687.4**, BIC = **1736.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.5575** | 11.2787 | ±22.5575 | **+12.019** | **2.83e-33** | *** |
| **Education: graduate level (vs college)** | **-5.7919** | 2.5590 | ±5.1181 | **-2.263** | **0.0236** | * |
| Education: high school or below (vs college) | +7.1549 | 4.5670 | ±9.1341 | +1.567 | 0.1172 |  |
| Site: UCSD (vs UAB) | +3.1757 | 3.2806 | ±6.5612 | +0.968 | 0.3330 |  |
| Site: UW (vs UAB) | -0.0514 | 3.3602 | ±6.7204 | -0.015 | 0.9878 |  |
| Season: spring (vs autumn) | -0.1109 | 3.5730 | ±7.1461 | -0.031 | 0.9753 |  |
| Season: summer (vs autumn) | +0.6943 | 4.0252 | ±8.0504 | +0.172 | 0.8631 |  |
| Season: winter (vs autumn) | +4.6618 | 4.2039 | ±8.4078 | +1.109 | 0.2675 |  |
| Age (years) | -0.2390 | 0.1360 | ±0.2721 | -1.757 | 0.0790 | . |
| BMI (kg/m2) | +0.1475 | 0.1801 | ±0.3602 | +0.819 | 0.4128 |  |
| Hypertension | +0.6631 | 2.6417 | ±5.2833 | +0.251 | 0.8018 |  |
| High cholesterol | -0.7054 | 2.5956 | ±5.1912 | -0.272 | 0.7858 |  |
| Kidney disease | -4.6291 | 3.8425 | ±7.6849 | -1.205 | 0.2283 |  |
| Circulatory disease | -0.3057 | 3.3052 | ±6.6105 | -0.092 | 0.9263 |  |
| Time 181-250, pooled (%) | +0.1877 | 0.3516 | ±0.7032 | +0.534 | 0.5935 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **198**, R² = **0.1227**, Adj R² = **0.0555**, F-statistic = **1.83** (p = **0.0375**), Residual SE = **16.545** on **183** df, AIC = **1687.5**, BIC = **1736.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.5642** | 11.2700 | ±22.5399 | **+12.029** | **2.51e-33** | *** |
| **Education: graduate level (vs college)** | **-5.7738** | 2.5554 | ±5.1108 | **-2.259** | **0.0239** | * |
| Education: high school or below (vs college) | +7.2064 | 4.5344 | ±9.0687 | +1.589 | 0.1120 |  |
| Site: UCSD (vs UAB) | +3.1685 | 3.2824 | ±6.5647 | +0.965 | 0.3344 |  |
| Site: UW (vs UAB) | -0.0904 | 3.3615 | ±6.7230 | -0.027 | 0.9785 |  |
| Season: spring (vs autumn) | -0.1027 | 3.5648 | ±7.1296 | -0.029 | 0.9770 |  |
| Season: summer (vs autumn) | +0.6933 | 4.0305 | ±8.0609 | +0.172 | 0.8634 |  |
| Season: winter (vs autumn) | +4.6636 | 4.2076 | ±8.4152 | +1.108 | 0.2677 |  |
| Age (years) | -0.2386 | 0.1362 | ±0.2725 | -1.751 | 0.0799 | . |
| BMI (kg/m2) | +0.1488 | 0.1802 | ±0.3604 | +0.826 | 0.4089 |  |
| Hypertension | +0.6481 | 2.6302 | ±5.2604 | +0.246 | 0.8054 |  |
| High cholesterol | -0.7202 | 2.5954 | ±5.1908 | -0.278 | 0.7814 |  |
| Kidney disease | -4.6129 | 3.8483 | ±7.6965 | -1.199 | 0.2306 |  |
| Circulatory disease | -0.2988 | 3.3053 | ±6.6105 | -0.090 | 0.9280 |  |
| Avg. daily time 181-250 (%) | +0.1783 | 0.3577 | ±0.7154 | +0.498 | 0.6182 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **198**, R² = **0.1230**, Adj R² = **0.0559**, F-statistic = **1.83** (p = **0.0367**), Residual SE = **16.542** on **183** df, AIC = **1687.4**, BIC = **1736.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.5575** | 11.2787 | ±22.5575 | **+12.019** | **2.83e-33** | *** |
| **Education: graduate level (vs college)** | **-5.7919** | 2.5590 | ±5.1181 | **-2.263** | **0.0236** | * |
| Education: high school or below (vs college) | +7.1549 | 4.5670 | ±9.1341 | +1.567 | 0.1172 |  |
| Site: UCSD (vs UAB) | +3.1757 | 3.2806 | ±6.5612 | +0.968 | 0.3330 |  |
| Site: UW (vs UAB) | -0.0514 | 3.3602 | ±6.7204 | -0.015 | 0.9878 |  |
| Season: spring (vs autumn) | -0.1109 | 3.5730 | ±7.1461 | -0.031 | 0.9753 |  |
| Season: summer (vs autumn) | +0.6943 | 4.0252 | ±8.0504 | +0.172 | 0.8631 |  |
| Season: winter (vs autumn) | +4.6618 | 4.2039 | ±8.4078 | +1.109 | 0.2675 |  |
| Age (years) | -0.2390 | 0.1360 | ±0.2721 | -1.757 | 0.0790 | . |
| BMI (kg/m2) | +0.1475 | 0.1801 | ±0.3602 | +0.819 | 0.4128 |  |
| Hypertension | +0.6631 | 2.6417 | ±5.2833 | +0.251 | 0.8018 |  |
| High cholesterol | -0.7054 | 2.5956 | ±5.1912 | -0.272 | 0.7858 |  |
| Kidney disease | -4.6291 | 3.8425 | ±7.6849 | -1.205 | 0.2283 |  |
| Circulatory disease | -0.3057 | 3.3052 | ±6.6105 | -0.092 | 0.9263 |  |
| Time > 180 (%) | +0.1877 | 0.3516 | ±0.7032 | +0.534 | 0.5935 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **198**, R² = **0.1227**, Adj R² = **0.0555**, F-statistic = **1.83** (p = **0.0375**), Residual SE = **16.545** on **183** df, AIC = **1687.5**, BIC = **1736.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.5642** | 11.2700 | ±22.5399 | **+12.029** | **2.51e-33** | *** |
| **Education: graduate level (vs college)** | **-5.7738** | 2.5554 | ±5.1108 | **-2.259** | **0.0239** | * |
| Education: high school or below (vs college) | +7.2064 | 4.5344 | ±9.0687 | +1.589 | 0.1120 |  |
| Site: UCSD (vs UAB) | +3.1685 | 3.2824 | ±6.5647 | +0.965 | 0.3344 |  |
| Site: UW (vs UAB) | -0.0904 | 3.3615 | ±6.7230 | -0.027 | 0.9785 |  |
| Season: spring (vs autumn) | -0.1027 | 3.5648 | ±7.1296 | -0.029 | 0.9770 |  |
| Season: summer (vs autumn) | +0.6933 | 4.0305 | ±8.0609 | +0.172 | 0.8634 |  |
| Season: winter (vs autumn) | +4.6636 | 4.2076 | ±8.4152 | +1.108 | 0.2677 |  |
| Age (years) | -0.2386 | 0.1362 | ±0.2725 | -1.751 | 0.0799 | . |
| BMI (kg/m2) | +0.1488 | 0.1802 | ±0.3604 | +0.826 | 0.4089 |  |
| Hypertension | +0.6481 | 2.6302 | ±5.2604 | +0.246 | 0.8054 |  |
| High cholesterol | -0.7202 | 2.5954 | ±5.1908 | -0.278 | 0.7814 |  |
| Kidney disease | -4.6129 | 3.8483 | ±7.6965 | -1.199 | 0.2306 |  |
| Circulatory disease | -0.2988 | 3.3053 | ±6.6105 | -0.090 | 0.9280 |  |
| Avg. daily time > 180 (%) | +0.1783 | 0.3577 | ±0.7154 | +0.498 | 0.6182 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 198)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **198**, R² = **0.1209**, Adj R² = **0.0536**, F-statistic = **1.80** (p = **0.0417**), Residual SE = **16.562** on **183** df, AIC = **1687.9**, BIC = **1737.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.5640** | 11.2799 | ±22.5598 | **+12.018** | **2.85e-33** | *** |
| **Education: graduate level (vs college)** | **-5.6670** | 2.5095 | ±5.0189 | **-2.258** | **0.0239** | * |
| Education: high school or below (vs college) | +7.5154 | 4.6878 | ±9.3756 | +1.603 | 0.1089 |  |
| Site: UCSD (vs UAB) | +2.8959 | 3.3825 | ±6.7649 | +0.856 | 0.3919 |  |
| Site: UW (vs UAB) | -0.3363 | 3.4553 | ±6.9106 | -0.097 | 0.9225 |  |
| Season: spring (vs autumn) | -0.0813 | 3.6111 | ±7.2222 | -0.023 | 0.9820 |  |
| Season: summer (vs autumn) | +0.9237 | 4.0004 | ±8.0008 | +0.231 | 0.8174 |  |
| Season: winter (vs autumn) | +4.7749 | 4.1307 | ±8.2614 | +1.156 | 0.2477 |  |
| Age (years) | -0.2290 | 0.1305 | ±0.2609 | -1.755 | 0.0792 | . |
| BMI (kg/m2) | +0.1553 | 0.1827 | ±0.3653 | +0.850 | 0.3951 |  |
| Hypertension | +0.7023 | 2.7336 | ±5.4672 | +0.257 | 0.7972 |  |
| High cholesterol | -0.8188 | 2.5676 | ±5.1353 | -0.319 | 0.7498 |  |
| Kidney disease | -4.0795 | 3.8070 | ±7.6141 | -1.072 | 0.2839 |  |
| Circulatory disease | -0.1407 | 3.2407 | ±6.4813 | -0.043 | 0.9654 |  |
| Nocturnal time > 180 (%) | -0.0690 | 0.2624 | ±0.5249 | -0.263 | 0.7925 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 178; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **178**, R² = **0.1606**, Adj R² = **0.1104**, F-statistic = **3.20** (p = **8.81e-04**), Residual SE = **4727.096** on **167** df, AIC = **3527.9**, BIC = **3562.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19149.5784** | 3837.4555 | ±7674.9111 | **+4.990** | **6.03e-07** | *** |
| **Education: graduate level (vs college)** | **-2405.1759** | 797.8611 | ±1595.7223 | **-3.015** | **0.0026** | ** |
| Education: high school or below (vs college) | -577.5979 | 1277.7398 | ±2555.4795 | -0.452 | 0.6512 |  |
| Site: UCSD (vs UAB) | +616.3652 | 978.2886 | ±1956.5772 | +0.630 | 0.5287 |  |
| Site: UW (vs UAB) | +975.2728 | 994.3411 | ±1988.6821 | +0.981 | 0.3267 |  |
| **Age (years)** | **-151.5931** | 48.6109 | ±97.2218 | **-3.118** | **0.0018** | ** |
| BMI (kg/m2) | +24.4758 | 64.6193 | ±129.2386 | +0.379 | 0.7049 |  |
| Hypertension | +899.1291 | 838.2152 | ±1676.4304 | +1.073 | 0.2834 |  |
| High cholesterol | -268.9596 | 763.5564 | ±1527.1129 | -0.352 | 0.7247 |  |
| Kidney disease | +229.7934 | 1329.2332 | ±2658.4664 | +0.173 | 0.8627 |  |
| Circulatory disease | -1285.2118 | 899.5281 | ±1799.0561 | -1.429 | 0.1531 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **178**, R² = **0.1613**, Adj R² = **0.1058**, F-statistic = **2.90** (p = **0.0016**), Residual SE = **4739.312** on **166** df, AIC = **3529.8**, BIC = **3568.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17713.3614** | 5020.3351 | ±10040.6703 | **+3.528** | **4.18e-04** | *** |
| **Education: graduate level (vs college)** | **-2392.6068** | 809.0551 | ±1618.1102 | **-2.957** | **0.0031** | ** |
| Education: high school or below (vs college) | -593.4636 | 1280.1873 | ±2560.3745 | -0.464 | 0.6430 |  |
| Site: UCSD (vs UAB) | +617.0316 | 979.9453 | ±1959.8906 | +0.630 | 0.5289 |  |
| Site: UW (vs UAB) | +981.0610 | 997.4329 | ±1994.8657 | +0.984 | 0.3253 |  |
| **Age (years)** | **-151.7249** | 48.8125 | ±97.6249 | **-3.108** | **0.0019** | ** |
| BMI (kg/m2) | +20.8062 | 64.6936 | ±129.3873 | +0.322 | 0.7477 |  |
| Hypertension | +872.6109 | 852.2424 | ±1704.4848 | +1.024 | 0.3059 |  |
| High cholesterol | -303.4039 | 751.8787 | ±1503.7575 | -0.404 | 0.6866 |  |
| Kidney disease | +285.7445 | 1366.3393 | ±2732.6786 | +0.209 | 0.8343 |  |
| Circulatory disease | -1334.8402 | 903.3490 | ±1806.6981 | -1.478 | 0.1395 |  |
| HbA1c (%) | +267.8141 | 631.3275 | ±1262.6549 | +0.424 | 0.6714 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **178**, R² = **0.1650**, Adj R² = **0.1097**, F-statistic = **2.98** (p = **0.0012**), Residual SE = **4728.892** on **166** df, AIC = **3529.0**, BIC = **3567.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16026.1227** | 5210.9305 | ±10421.8610 | **+3.075** | **0.0021** | ** |
| **Education: graduate level (vs college)** | **-2389.0896** | 805.7743 | ±1611.5485 | **-2.965** | **0.0030** | ** |
| Education: high school or below (vs college) | -505.2159 | 1284.9296 | ±2569.8593 | -0.393 | 0.6942 |  |
| Site: UCSD (vs UAB) | +580.0215 | 988.0389 | ±1976.0778 | +0.587 | 0.5572 |  |
| Site: UW (vs UAB) | +964.7312 | 996.7543 | ±1993.5085 | +0.968 | 0.3331 |  |
| **Age (years)** | **-151.2298** | 48.9617 | ±97.9233 | **-3.089** | **0.0020** | ** |
| BMI (kg/m2) | +20.9364 | 65.3928 | ±130.7856 | +0.320 | 0.7488 |  |
| Hypertension | +857.8647 | 839.9703 | ±1679.9405 | +1.021 | 0.3071 |  |
| High cholesterol | -257.8261 | 773.9917 | ±1547.9834 | -0.333 | 0.7390 |  |
| Kidney disease | +118.2300 | 1339.9149 | ±2679.8298 | +0.088 | 0.9297 |  |
| Circulatory disease | -1359.7530 | 908.2412 | ±1816.4824 | -1.497 | 0.1344 |  |
| Mean glucose (mg/dL) | +25.7424 | 29.8352 | ±59.6705 | +0.863 | 0.3882 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **178**, R² = **0.1650**, Adj R² = **0.1097**, F-statistic = **2.98** (p = **0.0012**), Residual SE = **4728.892** on **166** df, AIC = **3529.0**, BIC = **3567.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +12463.9374 | 8542.0985 | ±17084.1970 | +1.459 | 0.1445 |  |
| **Education: graduate level (vs college)** | **-2389.0896** | 805.7743 | ±1611.5485 | **-2.965** | **0.0030** | ** |
| Education: high school or below (vs college) | -505.2159 | 1284.9296 | ±2569.8593 | -0.393 | 0.6942 |  |
| Site: UCSD (vs UAB) | +580.0215 | 988.0389 | ±1976.0778 | +0.587 | 0.5572 |  |
| Site: UW (vs UAB) | +964.7312 | 996.7543 | ±1993.5085 | +0.968 | 0.3331 |  |
| **Age (years)** | **-151.2298** | 48.9617 | ±97.9233 | **-3.089** | **0.0020** | ** |
| BMI (kg/m2) | +20.9364 | 65.3928 | ±130.7856 | +0.320 | 0.7488 |  |
| Hypertension | +857.8647 | 839.9703 | ±1679.9405 | +1.021 | 0.3071 |  |
| High cholesterol | -257.8261 | 773.9917 | ±1547.9834 | -0.333 | 0.7390 |  |
| Kidney disease | +118.2300 | 1339.9149 | ±2679.8298 | +0.088 | 0.9297 |  |
| Circulatory disease | -1359.7530 | 908.2412 | ±1816.4824 | -1.497 | 0.1344 |  |
| GMI (%) | +1076.1889 | 1247.2929 | ±2494.5858 | +0.863 | 0.3882 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **178**, R² = **0.1750**, Adj R² = **0.1204**, F-statistic = **3.20** (p = **5.69e-04**), Residual SE = **4700.409** on **166** df, AIC = **3526.8**, BIC = **3565.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13961.9304** | 4937.6165 | ±9875.2329 | **+2.828** | **0.0047** | ** |
| **Education: graduate level (vs college)** | **-2412.9715** | 800.0017 | ±1600.0034 | **-3.016** | **0.0026** | ** |
| Education: high school or below (vs college) | -502.4193 | 1259.1623 | ±2518.3246 | -0.399 | 0.6899 |  |
| Site: UCSD (vs UAB) | +519.1473 | 984.1564 | ±1968.3127 | +0.528 | 0.5978 |  |
| Site: UW (vs UAB) | +928.2613 | 981.5185 | ±1963.0371 | +0.946 | 0.3443 |  |
| **Age (years)** | **-147.2569** | 48.7380 | ±97.4760 | **-3.021** | **0.0025** | ** |
| BMI (kg/m2) | +17.2820 | 64.8134 | ±129.6268 | +0.267 | 0.7897 |  |
| Hypertension | +827.5272 | 827.6829 | ±1655.3657 | +1.000 | 0.3174 |  |
| High cholesterol | -282.1590 | 767.9040 | ±1535.8081 | -0.367 | 0.7133 |  |
| Kidney disease | +213.1038 | 1297.0208 | ±2594.0417 | +0.164 | 0.8695 |  |
| Circulatory disease | -1472.4765 | 895.0329 | ±1790.0658 | -1.645 | 0.0999 | . |
| Nocturnal mean 00-06h (mg/dL) | +41.8241 | 24.5246 | ±49.0492 | +1.705 | 0.0881 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1611**, Adj R² = **0.1055**, F-statistic = **2.90** (p = **0.0016**), Residual SE = **4740.081** on **166** df, AIC = **3529.8**, BIC = **3568.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18696.1611** | 4236.2260 | ±8472.4520 | **+4.413** | **1.02e-05** | *** |
| **Education: graduate level (vs college)** | **-2419.3664** | 795.5618 | ±1591.1236 | **-3.041** | **0.0024** | ** |
| Education: high school or below (vs college) | -632.5813 | 1298.7389 | ±2597.4779 | -0.487 | 0.6262 |  |
| Site: UCSD (vs UAB) | +628.9506 | 984.4360 | ±1968.8721 | +0.639 | 0.5229 |  |
| Site: UW (vs UAB) | +1011.7674 | 1020.0129 | ±2040.0258 | +0.992 | 0.3212 |  |
| **Age (years)** | **-152.1765** | 48.8413 | ±97.6826 | **-3.116** | **0.0018** | ** |
| BMI (kg/m2) | +24.6807 | 64.8791 | ±129.7582 | +0.380 | 0.7036 |  |
| Hypertension | +857.0480 | 844.7100 | ±1689.4201 | +1.015 | 0.3103 |  |
| High cholesterol | -256.2115 | 769.5576 | ±1539.1152 | -0.333 | 0.7392 |  |
| Kidney disease | +176.5226 | 1349.6066 | ±2699.2132 | +0.131 | 0.8959 |  |
| Circulatory disease | -1310.6130 | 896.4448 | ±1792.8895 | -1.462 | 0.1437 |  |
| Glucose SD, pooled (mg/dL) | +23.4949 | 75.0619 | ±150.1238 | +0.313 | 0.7543 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1611**, Adj R² = **0.1055**, F-statistic = **2.90** (p = **0.0016**), Residual SE = **4739.933** on **166** df, AIC = **3529.8**, BIC = **3568.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18703.1846** | 4155.8109 | ±8311.6217 | **+4.500** | **6.78e-06** | *** |
| **Education: graduate level (vs college)** | **-2419.7094** | 794.2264 | ±1588.4528 | **-3.047** | **0.0023** | ** |
| Education: high school or below (vs college) | -621.5559 | 1295.4885 | ±2590.9771 | -0.480 | 0.6314 |  |
| Site: UCSD (vs UAB) | +616.2010 | 983.6210 | ±1967.2420 | +0.626 | 0.5310 |  |
| Site: UW (vs UAB) | +999.8289 | 1012.1002 | ±2024.2003 | +0.988 | 0.3232 |  |
| **Age (years)** | **-152.2608** | 48.9731 | ±97.9462 | **-3.109** | **0.0019** | ** |
| BMI (kg/m2) | +24.9098 | 64.8949 | ±129.7897 | +0.384 | 0.7011 |  |
| Hypertension | +845.7544 | 840.0251 | ±1680.0503 | +1.007 | 0.3140 |  |
| High cholesterol | -252.5667 | 770.8291 | ±1541.6583 | -0.328 | 0.7432 |  |
| Kidney disease | +188.3610 | 1337.9194 | ±2675.8388 | +0.141 | 0.8880 |  |
| Circulatory disease | -1305.1388 | 895.9222 | ±1791.8443 | -1.457 | 0.1452 |  |
| Avg. daily SD (mg/dL) | +25.4350 | 76.9779 | ±153.9558 | +0.330 | 0.7411 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **178**, R² = **0.1609**, Adj R² = **0.1053**, F-statistic = **2.89** (p = **0.0017**), Residual SE = **4740.613** on **166** df, AIC = **3529.9**, BIC = **3568.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19565.6229** | 4485.9303 | ±8971.8606 | **+4.362** | **1.29e-05** | *** |
| **Education: graduate level (vs college)** | **-2391.5060** | 792.3217 | ±1584.6433 | **-3.018** | **0.0025** | ** |
| Education: high school or below (vs college) | -516.6836 | 1349.8512 | ±2699.7024 | -0.383 | 0.7019 |  |
| Site: UCSD (vs UAB) | +600.1978 | 989.0444 | ±1978.0888 | +0.607 | 0.5440 |  |
| Site: UW (vs UAB) | +941.1995 | 1039.9829 | ±2079.9657 | +0.905 | 0.3655 |  |
| **Age (years)** | **-151.0033** | 48.8983 | ±97.7967 | **-3.088** | **0.0020** | ** |
| BMI (kg/m2) | +23.8026 | 66.6201 | ±133.2403 | +0.357 | 0.7209 |  |
| Hypertension | +931.2217 | 846.0240 | ±1692.0480 | +1.101 | 0.2710 |  |
| High cholesterol | -278.3968 | 763.8414 | ±1527.6828 | -0.364 | 0.7155 |  |
| Kidney disease | +261.9820 | 1331.5300 | ±2663.0599 | +0.197 | 0.8440 |  |
| Circulatory disease | -1274.9849 | 902.3257 | ±1804.6513 | -1.413 | 0.1577 |  |
| CV (%) | -26.2110 | 106.1421 | ±212.2842 | -0.247 | 0.8050 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **178**, R² = **0.1608**, Adj R² = **0.1051**, F-statistic = **2.89** (p = **0.0017**), Residual SE = **4740.932** on **166** df, AIC = **3529.9**, BIC = **3568.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19494.6448** | 4027.0838 | ±8054.1677 | **+4.841** | **1.29e-06** | *** |
| **Education: graduate level (vs college)** | **-2412.4168** | 793.3928 | ±1586.7856 | **-3.041** | **0.0024** | ** |
| Education: high school or below (vs college) | -617.0220 | 1326.4930 | ±2652.9861 | -0.465 | 0.6418 |  |
| Site: UCSD (vs UAB) | +624.7704 | 987.7162 | ±1975.4324 | +0.633 | 0.5270 |  |
| Site: UW (vs UAB) | +997.2314 | 1035.4481 | ±2070.8962 | +0.963 | 0.3355 |  |
| **Age (years)** | **-152.0594** | 48.8012 | ±97.6024 | **-3.116** | **0.0018** | ** |
| BMI (kg/m2) | +24.5958 | 65.0049 | ±130.0097 | +0.378 | 0.7052 |  |
| Hypertension | +874.6127 | 836.5225 | ±1673.0449 | +1.046 | 0.2958 |  |
| High cholesterol | -265.5494 | 765.9498 | ±1531.8997 | -0.347 | 0.7288 |  |
| Kidney disease | +207.3859 | 1332.8824 | ±2665.7648 | +0.156 | 0.8764 |  |
| Circulatory disease | -1289.3262 | 898.3926 | ±1796.7852 | -1.435 | 0.1512 |  |
| Mean / SD ratio | -50.2076 | 262.1276 | ±524.2552 | -0.192 | 0.8481 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1616**, Adj R² = **0.1061**, F-statistic = **2.91** (p = **0.0016**), Residual SE = **4738.449** on **166** df, AIC = **3529.7**, BIC = **3567.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20015.0916** | 4005.8768 | ±8011.7537 | **+4.996** | **5.84e-07** | *** |
| **Education: graduate level (vs college)** | **-2419.7053** | 793.4337 | ±1586.8673 | **-3.050** | **0.0023** | ** |
| Education: high school or below (vs college) | -657.0748 | 1314.8143 | ±2629.6286 | -0.500 | 0.6173 |  |
| Site: UCSD (vs UAB) | +610.8266 | 980.9443 | ±1961.8885 | +0.623 | 0.5335 |  |
| Site: UW (vs UAB) | +1016.1299 | 1020.0291 | ±2040.0582 | +0.996 | 0.3192 |  |
| **Age (years)** | **-153.1541** | 48.8418 | ±97.6835 | **-3.136** | **0.0017** | ** |
| BMI (kg/m2) | +24.8951 | 64.6214 | ±129.2429 | +0.385 | 0.7001 |  |
| Hypertension | +818.4550 | 827.6036 | ±1655.2073 | +0.989 | 0.3227 |  |
| High cholesterol | -263.0757 | 766.5792 | ±1533.1585 | -0.343 | 0.7315 |  |
| Kidney disease | +188.7485 | 1332.6887 | ±2665.3775 | +0.142 | 0.8874 |  |
| Circulatory disease | -1278.9587 | 899.3863 | ±1798.7727 | -1.422 | 0.1550 |  |
| Avg. daily mean/SD | -105.7075 | 199.1247 | ±398.2494 | -0.531 | 0.5955 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **178**, R² = **0.1663**, Adj R² = **0.1110**, F-statistic = **3.01** (p = **0.0011**), Residual SE = **4725.322** on **166** df, AIC = **3528.7**, BIC = **3566.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17236.1774** | 4390.8386 | ±8781.6773 | **+3.925** | **8.66e-05** | *** |
| **Education: graduate level (vs college)** | **-2426.2631** | 793.6668 | ±1587.3337 | **-3.057** | **0.0022** | ** |
| Education: high school or below (vs college) | -660.8586 | 1281.8812 | ±2563.7624 | -0.516 | 0.6062 |  |
| Site: UCSD (vs UAB) | +580.9377 | 983.7802 | ±1967.5605 | +0.591 | 0.5548 |  |
| Site: UW (vs UAB) | +1014.8974 | 996.4034 | ±1992.8067 | +1.019 | 0.3084 |  |
| **Age (years)** | **-151.6554** | 48.2783 | ±96.5566 | **-3.141** | **0.0017** | ** |
| BMI (kg/m2) | +21.1104 | 66.5114 | ±133.0228 | +0.317 | 0.7509 |  |
| Hypertension | +865.5028 | 828.3125 | ±1656.6250 | +1.045 | 0.2961 |  |
| High cholesterol | -304.6983 | 775.2724 | ±1550.5449 | -0.393 | 0.6943 |  |
| Kidney disease | +242.7381 | 1338.2147 | ±2676.4295 | +0.181 | 0.8561 |  |
| Circulatory disease | -1281.0712 | 901.1194 | ±1802.2389 | -1.422 | 0.1551 |  |
| MAG (mg/dL/h) | +57.2671 | 50.4798 | ±100.9597 | +1.134 | 0.2566 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **178**, R² = **0.1609**, Adj R² = **0.1053**, F-statistic = **2.89** (p = **0.0017**), Residual SE = **4740.600** on **166** df, AIC = **3529.9**, BIC = **3568.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18733.6082** | 4319.4615 | ±8638.9231 | **+4.337** | **1.44e-05** | *** |
| **Education: graduate level (vs college)** | **-2411.3539** | 795.0274 | ±1590.0549 | **-3.033** | **0.0024** | ** |
| Education: high school or below (vs college) | -605.9445 | 1301.3671 | ±2602.7341 | -0.466 | 0.6415 |  |
| Site: UCSD (vs UAB) | +622.9549 | 986.3909 | ±1972.7818 | +0.632 | 0.5277 |  |
| Site: UW (vs UAB) | +993.6306 | 1014.6396 | ±2029.2792 | +0.979 | 0.3274 |  |
| **Age (years)** | **-152.1176** | 49.2147 | ±98.4295 | **-3.091** | **0.0020** | ** |
| BMI (kg/m2) | +25.3333 | 65.6904 | ±131.3809 | +0.386 | 0.6998 |  |
| Hypertension | +872.8862 | 839.6415 | ±1679.2830 | +1.040 | 0.2985 |  |
| High cholesterol | -261.7282 | 771.8471 | ±1543.6943 | -0.339 | 0.7345 |  |
| Kidney disease | +209.3650 | 1324.7246 | ±2649.4492 | +0.158 | 0.8744 |  |
| Circulatory disease | -1295.9740 | 898.4080 | ±1796.8159 | -1.443 | 0.1492 |  |
| Avg. daily range (mg/dL) | +4.5084 | 19.4643 | ±38.9286 | +0.232 | 0.8168 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **178**, R² = **0.1609**, Adj R² = **0.1053**, F-statistic = **2.89** (p = **0.0017**), Residual SE = **4740.630** on **166** df, AIC = **3529.9**, BIC = **3568.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19323.7622** | 4061.0322 | ±8122.0643 | **+4.758** | **1.95e-06** | *** |
| **Education: graduate level (vs college)** | **-2398.4894** | 807.4603 | ±1614.9205 | **-2.970** | **0.0030** | ** |
| Education: high school or below (vs college) | -524.0588 | 1277.1820 | ±2554.3640 | -0.410 | 0.6816 |  |
| Site: UCSD (vs UAB) | +585.9635 | 945.9885 | ±1891.9769 | +0.619 | 0.5356 |  |
| Site: UW (vs UAB) | +937.5211 | 974.0746 | ±1948.1491 | +0.962 | 0.3358 |  |
| **Age (years)** | **-150.9970** | 48.5180 | ±97.0360 | **-3.112** | **0.0019** | ** |
| BMI (kg/m2) | +24.6740 | 65.3262 | ±130.6524 | +0.378 | 0.7057 |  |
| Hypertension | +891.2842 | 839.5942 | ±1679.1884 | +1.062 | 0.2884 |  |
| High cholesterol | -264.7969 | 764.6391 | ±1529.2781 | -0.346 | 0.7291 |  |
| Kidney disease | +277.0599 | 1448.7383 | ±2897.4765 | +0.191 | 0.8483 |  |
| Circulatory disease | -1248.4353 | 929.1795 | ±1858.3589 | -1.344 | 0.1791 |  |
| SD of daily means (mg/dL) | -32.3132 | 163.6310 | ±327.2620 | -0.197 | 0.8435 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **178**, R² = **0.1614**, Adj R² = **0.1058**, F-statistic = **2.90** (p = **0.0016**), Residual SE = **4739.227** on **166** df, AIC = **3529.8**, BIC = **3568.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +16195.9622 | 9224.1234 | ±18448.2469 | +1.756 | 0.0791 | . |
| **Education: graduate level (vs college)** | **-2380.2750** | 813.7383 | ±1627.4766 | **-2.925** | **0.0034** | ** |
| Education: high school or below (vs college) | -551.6219 | 1285.0332 | ±2570.0664 | -0.429 | 0.6677 |  |
| Site: UCSD (vs UAB) | +603.4786 | 977.6018 | ±1955.2037 | +0.617 | 0.5370 |  |
| Site: UW (vs UAB) | +960.0792 | 1009.0997 | ±2018.1994 | +0.951 | 0.3414 |  |
| **Age (years)** | **-150.0843** | 48.8069 | ±97.6137 | **-3.075** | **0.0021** | ** |
| BMI (kg/m2) | +25.5522 | 65.3762 | ±130.7523 | +0.391 | 0.6959 |  |
| Hypertension | +912.5736 | 843.4410 | ±1686.8820 | +1.082 | 0.2793 |  |
| High cholesterol | -288.4023 | 766.0345 | ±1532.0691 | -0.376 | 0.7066 |  |
| Kidney disease | +306.2584 | 1398.6704 | ±2797.3407 | +0.219 | 0.8267 |  |
| Circulatory disease | -1245.7599 | 915.6430 | ±1831.2861 | -1.361 | 0.1737 |  |
| Time in range 70-180, pooled (%) | +29.2979 | 82.1818 | ±164.3635 | +0.357 | 0.7215 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **178**, R² = **0.1611**, Adj R² = **0.1055**, F-statistic = **2.90** (p = **0.0016**), Residual SE = **4740.033** on **166** df, AIC = **3529.8**, BIC = **3568.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +16782.9742 | 9665.3629 | ±19330.7257 | +1.736 | 0.0825 | . |
| **Education: graduate level (vs college)** | **-2387.3699** | 814.1489 | ±1628.2977 | **-2.932** | **0.0034** | ** |
| Education: high school or below (vs college) | -561.9855 | 1284.1380 | ±2568.2759 | -0.438 | 0.6616 |  |
| Site: UCSD (vs UAB) | +606.5810 | 978.1152 | ±1956.2304 | +0.620 | 0.5352 |  |
| Site: UW (vs UAB) | +967.8660 | 1008.8301 | ±2017.6602 | +0.959 | 0.3374 |  |
| **Age (years)** | **-150.3338** | 48.8491 | ±97.6983 | **-3.078** | **0.0021** | ** |
| BMI (kg/m2) | +25.1538 | 65.2954 | ±130.5908 | +0.385 | 0.7001 |  |
| Hypertension | +913.2698 | 843.0741 | ±1686.1483 | +1.083 | 0.2787 |  |
| High cholesterol | -284.9248 | 766.7357 | ±1533.4713 | -0.372 | 0.7102 |  |
| Kidney disease | +291.6162 | 1402.5633 | ±2805.1266 | +0.208 | 0.8353 |  |
| Circulatory disease | -1252.9958 | 917.5154 | ±1835.0309 | -1.366 | 0.1721 |  |
| Avg. daily time in range 70-180 (%) | +23.4492 | 86.8830 | ±173.7659 | +0.270 | 0.7872 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **178**, R² = **0.1678**, Adj R² = **0.1126**, F-statistic = **3.04** (p = **9.89e-04**), Residual SE = **4721.061** on **166** df, AIC = **3528.4**, BIC = **3566.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18863.9488** | 3842.0389 | ±7684.0777 | **+4.910** | **9.11e-07** | *** |
| **Education: graduate level (vs college)** | **-2290.6821** | 799.7933 | ±1599.5866 | **-2.864** | **0.0042** | ** |
| Education: high school or below (vs college) | -384.9944 | 1303.4872 | ±2606.9745 | -0.295 | 0.7677 |  |
| Site: UCSD (vs UAB) | +557.8203 | 976.9686 | ±1953.9372 | +0.571 | 0.5680 |  |
| Site: UW (vs UAB) | +941.3417 | 989.8756 | ±1979.7512 | +0.951 | 0.3416 |  |
| **Age (years)** | **-144.1000** | 48.7583 | ±97.5165 | **-2.955** | **0.0031** | ** |
| BMI (kg/m2) | +22.5309 | 65.3803 | ±130.7607 | +0.345 | 0.7304 |  |
| Hypertension | +890.6150 | 837.1433 | ±1674.2866 | +1.064 | 0.2874 |  |
| High cholesterol | -202.9383 | 765.4867 | ±1530.9735 | -0.265 | 0.7909 |  |
| Kidney disease | +160.7665 | 1329.6462 | ±2659.2923 | +0.121 | 0.9038 |  |
| Circulatory disease | -1191.0297 | 922.2869 | ±1844.5737 | -1.291 | 0.1966 |  |
| Time 54-69, pooled (%) | -1439.0991 | 1069.3678 | ±2138.7355 | -1.346 | 0.1784 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **178**, R² = **0.1722**, Adj R² = **0.1174**, F-statistic = **3.14** (p = **7.07e-04**), Residual SE = **4708.443** on **166** df, AIC = **3527.5**, BIC = **3565.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18718.4211** | 3841.1485 | ±7682.2970 | **+4.873** | **1.10e-06** | *** |
| **Education: graduate level (vs college)** | **-2267.6349** | 799.1261 | ±1598.2522 | **-2.838** | **0.0045** | ** |
| Education: high school or below (vs college) | -360.3082 | 1295.4246 | ±2590.8491 | -0.278 | 0.7809 |  |
| Site: UCSD (vs UAB) | +594.7354 | 975.2873 | ±1950.5746 | +0.610 | 0.5420 |  |
| Site: UW (vs UAB) | +966.1005 | 987.2956 | ±1974.5913 | +0.979 | 0.3278 |  |
| **Age (years)** | **-141.5779** | 48.8255 | ±97.6511 | **-2.900** | **0.0037** | ** |
| BMI (kg/m2) | +21.7161 | 65.6073 | ±131.2147 | +0.331 | 0.7406 |  |
| Hypertension | +908.2729 | 838.6042 | ±1677.2083 | +1.083 | 0.2788 |  |
| High cholesterol | -189.6931 | 764.0367 | ±1528.0734 | -0.248 | 0.8039 |  |
| Kidney disease | +100.0648 | 1325.1856 | ±2650.3712 | +0.076 | 0.9398 |  |
| Circulatory disease | -1193.8821 | 924.9294 | ±1849.8589 | -1.291 | 0.1968 |  |
| Avg. daily time 54-69 (%) | -1758.2371 | 1018.8077 | ±2037.6155 | -1.726 | 0.0844 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **178**, R² = **0.1678**, Adj R² = **0.1126**, F-statistic = **3.04** (p = **9.89e-04**), Residual SE = **4721.061** on **166** df, AIC = **3528.4**, BIC = **3566.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18863.9488** | 3842.0389 | ±7684.0777 | **+4.910** | **9.11e-07** | *** |
| **Education: graduate level (vs college)** | **-2290.6821** | 799.7933 | ±1599.5866 | **-2.864** | **0.0042** | ** |
| Education: high school or below (vs college) | -384.9944 | 1303.4872 | ±2606.9745 | -0.295 | 0.7677 |  |
| Site: UCSD (vs UAB) | +557.8203 | 976.9686 | ±1953.9372 | +0.571 | 0.5680 |  |
| Site: UW (vs UAB) | +941.3417 | 989.8756 | ±1979.7512 | +0.951 | 0.3416 |  |
| **Age (years)** | **-144.1000** | 48.7583 | ±97.5165 | **-2.955** | **0.0031** | ** |
| BMI (kg/m2) | +22.5309 | 65.3803 | ±130.7607 | +0.345 | 0.7304 |  |
| Hypertension | +890.6150 | 837.1433 | ±1674.2866 | +1.064 | 0.2874 |  |
| High cholesterol | -202.9383 | 765.4867 | ±1530.9735 | -0.265 | 0.7909 |  |
| Kidney disease | +160.7665 | 1329.6462 | ±2659.2923 | +0.121 | 0.9038 |  |
| Circulatory disease | -1191.0297 | 922.2869 | ±1844.5737 | -1.291 | 0.1966 |  |
| Time < 70 (%) | -1439.0991 | 1069.3678 | ±2138.7355 | -1.346 | 0.1784 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **178**, R² = **0.1722**, Adj R² = **0.1174**, F-statistic = **3.14** (p = **7.07e-04**), Residual SE = **4708.443** on **166** df, AIC = **3527.5**, BIC = **3565.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18718.4211** | 3841.1485 | ±7682.2970 | **+4.873** | **1.10e-06** | *** |
| **Education: graduate level (vs college)** | **-2267.6349** | 799.1261 | ±1598.2522 | **-2.838** | **0.0045** | ** |
| Education: high school or below (vs college) | -360.3082 | 1295.4246 | ±2590.8491 | -0.278 | 0.7809 |  |
| Site: UCSD (vs UAB) | +594.7354 | 975.2873 | ±1950.5746 | +0.610 | 0.5420 |  |
| Site: UW (vs UAB) | +966.1005 | 987.2956 | ±1974.5913 | +0.979 | 0.3278 |  |
| **Age (years)** | **-141.5779** | 48.8255 | ±97.6511 | **-2.900** | **0.0037** | ** |
| BMI (kg/m2) | +21.7161 | 65.6073 | ±131.2147 | +0.331 | 0.7406 |  |
| Hypertension | +908.2729 | 838.6042 | ±1677.2083 | +1.083 | 0.2788 |  |
| High cholesterol | -189.6931 | 764.0367 | ±1528.0734 | -0.248 | 0.8039 |  |
| Kidney disease | +100.0648 | 1325.1856 | ±2650.3712 | +0.076 | 0.9398 |  |
| Circulatory disease | -1193.8821 | 924.9294 | ±1849.8589 | -1.291 | 0.1968 |  |
| Avg. daily time < 70 (%) | -1758.2371 | 1018.8077 | ±2037.6155 | -1.726 | 0.0844 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **178**, R² = **0.1611**, Adj R² = **0.1055**, F-statistic = **2.90** (p = **0.0016**), Residual SE = **4739.990** on **166** df, AIC = **3529.8**, BIC = **3568.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19135.3508** | 3852.7456 | ±7705.4912 | **+4.967** | **6.81e-07** | *** |
| **Education: graduate level (vs college)** | **-2387.3500** | 812.4438 | ±1624.8876 | **-2.938** | **0.0033** | ** |
| Education: high school or below (vs college) | -560.1788 | 1283.9921 | ±2567.9842 | -0.436 | 0.6626 |  |
| Site: UCSD (vs UAB) | +607.1287 | 978.5005 | ±1957.0009 | +0.620 | 0.5349 |  |
| Site: UW (vs UAB) | +963.8184 | 1008.2625 | ±2016.5251 | +0.956 | 0.3391 |  |
| **Age (years)** | **-150.5219** | 48.8468 | ±97.6935 | **-3.082** | **0.0021** | ** |
| BMI (kg/m2) | +25.3572 | 65.3476 | ±130.6953 | +0.388 | 0.6980 |  |
| Hypertension | +909.8845 | 843.5293 | ±1687.0586 | +1.079 | 0.2807 |  |
| High cholesterol | -285.3771 | 766.5676 | ±1533.1352 | -0.372 | 0.7097 |  |
| Kidney disease | +291.2957 | 1399.0770 | ±2798.1540 | +0.208 | 0.8351 |  |
| Circulatory disease | -1255.5668 | 913.9697 | ±1827.9395 | -1.374 | 0.1695 |  |
| Time 181-250, pooled (%) | -23.1396 | 81.6050 | ±163.2101 | -0.284 | 0.7768 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **178**, R² = **0.1608**, Adj R² = **0.1052**, F-statistic = **2.89** (p = **0.0017**), Residual SE = **4740.769** on **166** df, AIC = **3529.9**, BIC = **3568.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19139.2948** | 3853.4888 | ±7706.9775 | **+4.967** | **6.81e-07** | *** |
| **Education: graduate level (vs college)** | **-2394.8707** | 812.8105 | ±1625.6211 | **-2.946** | **0.0032** | ** |
| Education: high school or below (vs college) | -569.3943 | 1283.1861 | ±2566.3722 | -0.444 | 0.6572 |  |
| Site: UCSD (vs UAB) | +610.2384 | 979.0058 | ±1958.0117 | +0.623 | 0.5331 |  |
| Site: UW (vs UAB) | +970.5727 | 1007.8694 | ±2015.7389 | +0.963 | 0.3356 |  |
| **Age (years)** | **-150.8668** | 48.8870 | ±97.7741 | **-3.086** | **0.0020** | ** |
| BMI (kg/m2) | +24.9370 | 65.2502 | ±130.5003 | +0.382 | 0.7023 |  |
| Hypertension | +908.1743 | 843.1997 | ±1686.3994 | +1.077 | 0.2815 |  |
| High cholesterol | -279.9428 | 767.4102 | ±1534.8203 | -0.365 | 0.7153 |  |
| Kidney disease | +270.7989 | 1403.2719 | ±2806.5437 | +0.193 | 0.8470 |  |
| Circulatory disease | -1265.2114 | 916.0140 | ±1832.0281 | -1.381 | 0.1672 |  |
| Avg. daily time 181-250 (%) | -15.1298 | 86.1420 | ±172.2841 | -0.176 | 0.8606 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **178**, R² = **0.1611**, Adj R² = **0.1055**, F-statistic = **2.90** (p = **0.0016**), Residual SE = **4739.990** on **166** df, AIC = **3529.8**, BIC = **3568.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19135.3508** | 3852.7456 | ±7705.4912 | **+4.967** | **6.81e-07** | *** |
| **Education: graduate level (vs college)** | **-2387.3500** | 812.4438 | ±1624.8876 | **-2.938** | **0.0033** | ** |
| Education: high school or below (vs college) | -560.1788 | 1283.9921 | ±2567.9842 | -0.436 | 0.6626 |  |
| Site: UCSD (vs UAB) | +607.1287 | 978.5005 | ±1957.0009 | +0.620 | 0.5349 |  |
| Site: UW (vs UAB) | +963.8184 | 1008.2625 | ±2016.5251 | +0.956 | 0.3391 |  |
| **Age (years)** | **-150.5219** | 48.8468 | ±97.6935 | **-3.082** | **0.0021** | ** |
| BMI (kg/m2) | +25.3572 | 65.3476 | ±130.6953 | +0.388 | 0.6980 |  |
| Hypertension | +909.8845 | 843.5293 | ±1687.0586 | +1.079 | 0.2807 |  |
| High cholesterol | -285.3771 | 766.5676 | ±1533.1352 | -0.372 | 0.7097 |  |
| Kidney disease | +291.2957 | 1399.0770 | ±2798.1540 | +0.208 | 0.8351 |  |
| Circulatory disease | -1255.5668 | 913.9697 | ±1827.9395 | -1.374 | 0.1695 |  |
| Time > 180 (%) | -23.1396 | 81.6050 | ±163.2101 | -0.284 | 0.7768 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **178**, R² = **0.1608**, Adj R² = **0.1052**, F-statistic = **2.89** (p = **0.0017**), Residual SE = **4740.769** on **166** df, AIC = **3529.9**, BIC = **3568.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19139.2948** | 3853.4888 | ±7706.9775 | **+4.967** | **6.81e-07** | *** |
| **Education: graduate level (vs college)** | **-2394.8707** | 812.8105 | ±1625.6211 | **-2.946** | **0.0032** | ** |
| Education: high school or below (vs college) | -569.3943 | 1283.1861 | ±2566.3722 | -0.444 | 0.6572 |  |
| Site: UCSD (vs UAB) | +610.2384 | 979.0058 | ±1958.0117 | +0.623 | 0.5331 |  |
| Site: UW (vs UAB) | +970.5727 | 1007.8694 | ±2015.7389 | +0.963 | 0.3356 |  |
| **Age (years)** | **-150.8668** | 48.8870 | ±97.7741 | **-3.086** | **0.0020** | ** |
| BMI (kg/m2) | +24.9370 | 65.2502 | ±130.5003 | +0.382 | 0.7023 |  |
| Hypertension | +908.1743 | 843.1997 | ±1686.3994 | +1.077 | 0.2815 |  |
| High cholesterol | -279.9428 | 767.4102 | ±1534.8203 | -0.365 | 0.7153 |  |
| Kidney disease | +270.7989 | 1403.2719 | ±2806.5437 | +0.193 | 0.8470 |  |
| Circulatory disease | -1265.2114 | 916.0140 | ±1832.0281 | -1.381 | 0.1672 |  |
| Avg. daily time > 180 (%) | -15.1298 | 86.1420 | ±172.2841 | -0.176 | 0.8606 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 178)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **178**, R² = **0.1617**, Adj R² = **0.1061**, F-statistic = **2.91** (p = **0.0016**), Residual SE = **4738.275** on **166** df, AIC = **3529.7**, BIC = **3567.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19228.5095** | 3867.1984 | ±7734.3968 | **+4.972** | **6.62e-07** | *** |
| **Education: graduate level (vs college)** | **-2416.7269** | 801.9250 | ±1603.8501 | **-3.014** | **0.0026** | ** |
| Education: high school or below (vs college) | -636.7166 | 1269.0908 | ±2538.1816 | -0.502 | 0.6159 |  |
| Site: UCSD (vs UAB) | +661.5990 | 980.2501 | ±1960.5002 | +0.675 | 0.4997 |  |
| Site: UW (vs UAB) | +1015.3458 | 992.4434 | ±1984.8869 | +1.023 | 0.3063 |  |
| **Age (years)** | **-152.8780** | 48.7806 | ±97.5613 | **-3.134** | **0.0017** | ** |
| BMI (kg/m2) | +21.2759 | 65.5960 | ±131.1920 | +0.324 | 0.7457 |  |
| Hypertension | +922.3182 | 850.7696 | ±1701.5391 | +1.084 | 0.2783 |  |
| High cholesterol | -262.8456 | 767.4595 | ±1534.9189 | -0.342 | 0.7320 |  |
| Kidney disease | +135.5237 | 1385.6018 | ±2771.2036 | +0.098 | 0.9221 |  |
| Circulatory disease | -1346.5467 | 916.6399 | ±1833.2798 | -1.469 | 0.1418 |  |
| Nocturnal time > 180 (%) | +34.2332 | 77.0663 | ±154.1326 | +0.444 | 0.6569 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 178; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **178**, R² = **0.1971**, Adj R² = **0.1490**, F-statistic = **4.10** (p = **4.60e-05**), Residual SE = **13.609** on **167** df, AIC = **1445.2**, BIC = **1480.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.5621** | 11.1678 | ±22.3356 | **+3.901** | **9.59e-05** | *** |
| **Education: graduate level (vs college)** | **-6.4973** | 2.2573 | ±4.5145 | **-2.878** | **0.0040** | ** |
| Education: high school or below (vs college) | -1.1003 | 3.8989 | ±7.7979 | -0.282 | 0.7778 |  |
| Site: UCSD (vs UAB) | +0.8730 | 2.7864 | ±5.5727 | +0.313 | 0.7540 |  |
| Site: UW (vs UAB) | +1.9945 | 2.7207 | ±5.4415 | +0.733 | 0.4635 |  |
| **Age (years)** | **-0.4422** | 0.1211 | ±0.2423 | **-3.651** | **2.61e-04** | *** |
| BMI (kg/m2) | +0.3475 | 0.2224 | ±0.4447 | +1.563 | 0.1181 |  |
| Hypertension | +1.5684 | 2.3833 | ±4.7666 | +0.658 | 0.5105 |  |
| High cholesterol | -0.1847 | 2.0547 | ±4.1094 | -0.090 | 0.9284 |  |
| Kidney disease | +1.4043 | 3.6991 | ±7.3981 | +0.380 | 0.7042 |  |
| Circulatory disease | -4.0232 | 2.5629 | ±5.1257 | -1.570 | 0.1165 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **178**, R² = **0.1998**, Adj R² = **0.1468**, F-statistic = **3.77** (p = **7.88e-05**), Residual SE = **13.627** on **166** df, AIC = **1446.6**, BIC = **1484.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+35.3124** | 15.8653 | ±31.7307 | **+2.226** | **0.0260** | * |
| **Education: graduate level (vs college)** | **-6.4251** | 2.2905 | ±4.5810 | **-2.805** | **0.0050** | ** |
| Education: high school or below (vs college) | -1.1914 | 3.8980 | ±7.7959 | -0.306 | 0.7599 |  |
| Site: UCSD (vs UAB) | +0.8768 | 2.7819 | ±5.5638 | +0.315 | 0.7526 |  |
| Site: UW (vs UAB) | +2.0277 | 2.7312 | ±5.4625 | +0.742 | 0.4578 |  |
| **Age (years)** | **-0.4430** | 0.1215 | ±0.2430 | **-3.646** | **2.66e-04** | *** |
| BMI (kg/m2) | +0.3264 | 0.2180 | ±0.4360 | +1.497 | 0.1343 |  |
| Hypertension | +1.4160 | 2.4106 | ±4.8212 | +0.587 | 0.5569 |  |
| High cholesterol | -0.3826 | 2.0462 | ±4.0924 | -0.187 | 0.8517 |  |
| Kidney disease | +1.7257 | 3.7276 | ±7.4552 | +0.463 | 0.6434 |  |
| Circulatory disease | -4.3083 | 2.6165 | ±5.2330 | -1.647 | 0.0996 | . |
| HbA1c (%) | +1.5383 | 1.8884 | ±3.7768 | +0.815 | 0.4153 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **178**, R² = **0.2020**, Adj R² = **0.1491**, F-statistic = **3.82** (p = **6.59e-05**), Residual SE = **13.608** on **166** df, AIC = **1446.1**, BIC = **1484.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.8965** | 15.7384 | ±31.4768 | **+2.154** | **0.0313** | * |
| **Education: graduate level (vs college)** | **-6.4475** | 2.2809 | ±4.5618 | **-2.827** | **0.0047** | ** |
| Education: high school or below (vs college) | -0.8763 | 3.9242 | ±7.8484 | -0.223 | 0.8233 |  |
| Site: UCSD (vs UAB) | +0.7605 | 2.8089 | ±5.6177 | +0.271 | 0.7866 |  |
| Site: UW (vs UAB) | +1.9618 | 2.7188 | ±5.4375 | +0.722 | 0.4705 |  |
| **Age (years)** | **-0.4411** | 0.1219 | ±0.2437 | **-3.620** | **2.95e-04** | *** |
| BMI (kg/m2) | +0.3366 | 0.2240 | ±0.4479 | +1.503 | 0.1329 |  |
| Hypertension | +1.4407 | 2.3827 | ±4.7654 | +0.605 | 0.5454 |  |
| High cholesterol | -0.1503 | 2.0762 | ±4.1525 | -0.072 | 0.9423 |  |
| Kidney disease | +1.0591 | 3.7488 | ±7.4977 | +0.283 | 0.7776 |  |
| Circulatory disease | -4.2539 | 2.5804 | ±5.1609 | -1.649 | 0.0992 | . |
| Mean glucose (mg/dL) | +0.0797 | 0.0837 | ±0.1674 | +0.952 | 0.3413 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **178**, R² = **0.2020**, Adj R² = **0.1491**, F-statistic = **3.82** (p = **6.59e-05**), Residual SE = **13.608** on **166** df, AIC = **1446.1**, BIC = **1484.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +22.8732 | 25.2414 | ±50.4829 | +0.906 | 0.3648 |  |
| **Education: graduate level (vs college)** | **-6.4475** | 2.2809 | ±4.5618 | **-2.827** | **0.0047** | ** |
| Education: high school or below (vs college) | -0.8763 | 3.9242 | ±7.8484 | -0.223 | 0.8233 |  |
| Site: UCSD (vs UAB) | +0.7605 | 2.8089 | ±5.6177 | +0.271 | 0.7866 |  |
| Site: UW (vs UAB) | +1.9618 | 2.7188 | ±5.4375 | +0.722 | 0.4705 |  |
| **Age (years)** | **-0.4411** | 0.1219 | ±0.2437 | **-3.620** | **2.95e-04** | *** |
| BMI (kg/m2) | +0.3366 | 0.2240 | ±0.4479 | +1.503 | 0.1329 |  |
| Hypertension | +1.4407 | 2.3827 | ±4.7654 | +0.605 | 0.5454 |  |
| High cholesterol | -0.1503 | 2.0762 | ±4.1525 | -0.072 | 0.9423 |  |
| Kidney disease | +1.0591 | 3.7488 | ±7.4977 | +0.283 | 0.7776 |  |
| Circulatory disease | -4.2539 | 2.5804 | ±5.1609 | -1.649 | 0.0992 | . |
| GMI (%) | +3.3303 | 3.4998 | ±6.9996 | +0.952 | 0.3413 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **178**, R² = **0.2114**, Adj R² = **0.1591**, F-statistic = **4.04** (p = **2.99e-05**), Residual SE = **13.528** on **166** df, AIC = **1444.0**, BIC = **1482.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +28.3870 | 14.9769 | ±29.9539 | +1.895 | 0.0580 | . |
| **Education: graduate level (vs college)** | **-6.5201** | 2.2629 | ±4.5259 | **-2.881** | **0.0040** | ** |
| Education: high school or below (vs college) | -0.8804 | 3.8387 | ±7.6774 | -0.229 | 0.8186 |  |
| Site: UCSD (vs UAB) | +0.5886 | 2.7947 | ±5.5894 | +0.211 | 0.8332 |  |
| Site: UW (vs UAB) | +1.8569 | 2.6910 | ±5.3820 | +0.690 | 0.4902 |  |
| **Age (years)** | **-0.4295** | 0.1222 | ±0.2443 | **-3.516** | **4.38e-04** | *** |
| BMI (kg/m2) | +0.3265 | 0.2219 | ±0.4439 | +1.471 | 0.1413 |  |
| Hypertension | +1.3589 | 2.3723 | ±4.7446 | +0.573 | 0.5668 |  |
| High cholesterol | -0.2233 | 2.0656 | ±4.1311 | -0.108 | 0.9139 |  |
| Kidney disease | +1.3555 | 3.5934 | ±7.1868 | +0.377 | 0.7060 |  |
| Circulatory disease | -4.5710 | 2.5398 | ±5.0797 | -1.800 | 0.0719 | . |
| Nocturnal mean 00-06h (mg/dL) | +0.1223 | 0.0734 | ±0.1468 | +1.667 | 0.0954 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1972**, Adj R² = **0.1440**, F-statistic = **3.71** (p = **9.75e-05**), Residual SE = **13.648** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.8684** | 12.9079 | ±25.8159 | **+3.321** | **8.97e-04** | *** |
| **Education: graduate level (vs college)** | **-6.5190** | 2.2461 | ±4.4922 | **-2.902** | **0.0037** | ** |
| Education: high school or below (vs college) | -1.1844 | 3.9634 | ±7.9268 | -0.299 | 0.7651 |  |
| Site: UCSD (vs UAB) | +0.8923 | 2.7956 | ±5.5911 | +0.319 | 0.7496 |  |
| Site: UW (vs UAB) | +2.0503 | 2.7735 | ±5.5469 | +0.739 | 0.4598 |  |
| **Age (years)** | **-0.4431** | 0.1215 | ±0.2431 | **-3.646** | **2.66e-04** | *** |
| BMI (kg/m2) | +0.3478 | 0.2246 | ±0.4491 | +1.549 | 0.1214 |  |
| Hypertension | +1.5040 | 2.4494 | ±4.8987 | +0.614 | 0.5392 |  |
| High cholesterol | -0.1652 | 2.0802 | ±4.1604 | -0.079 | 0.9367 |  |
| Kidney disease | +1.3228 | 3.7613 | ±7.5225 | +0.352 | 0.7251 |  |
| Circulatory disease | -4.0621 | 2.5865 | ±5.1730 | -1.570 | 0.1163 |  |
| Glucose SD, pooled (mg/dL) | +0.0359 | 0.2220 | ±0.4440 | +0.162 | 0.8714 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1972**, Adj R² = **0.1440**, F-statistic = **3.71** (p = **9.79e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.0855** | 12.6079 | ±25.2159 | **+3.417** | **6.32e-04** | *** |
| **Education: graduate level (vs college)** | **-6.5128** | 2.2433 | ±4.4866 | **-2.903** | **0.0037** | ** |
| Education: high school or below (vs college) | -1.1472 | 3.9546 | ±7.9092 | -0.290 | 0.7717 |  |
| Site: UCSD (vs UAB) | +0.8728 | 2.8000 | ±5.6001 | +0.312 | 0.7552 |  |
| Site: UW (vs UAB) | +2.0207 | 2.7561 | ±5.5122 | +0.733 | 0.4635 |  |
| **Age (years)** | **-0.4429** | 0.1219 | ±0.2437 | **-3.635** | **2.78e-04** | *** |
| BMI (kg/m2) | +0.3480 | 0.2251 | ±0.4502 | +1.546 | 0.1221 |  |
| Hypertension | +1.5114 | 2.4524 | ±4.9048 | +0.616 | 0.5377 |  |
| High cholesterol | -0.1672 | 2.0839 | ±4.1678 | -0.080 | 0.9360 |  |
| Kidney disease | +1.3601 | 3.7281 | ±7.4562 | +0.365 | 0.7152 |  |
| Circulatory disease | -4.0445 | 2.5805 | ±5.1609 | -1.567 | 0.1170 |  |
| Avg. daily SD (mg/dL) | +0.0272 | 0.2222 | ±0.4443 | +0.122 | 0.9027 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **178**, R² = **0.1983**, Adj R² = **0.1452**, F-statistic = **3.73** (p = **8.90e-05**), Residual SE = **13.639** on **166** df, AIC = **1446.9**, BIC = **1485.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.2821** | 13.7106 | ±27.4213 | **+3.376** | **7.36e-04** | *** |
| **Education: graduate level (vs college)** | **-6.4079** | 2.2464 | ±4.4929 | **-2.852** | **0.0043** | ** |
| Education: high school or below (vs college) | -0.7020 | 4.1200 | ±8.2399 | -0.170 | 0.8647 |  |
| Site: UCSD (vs UAB) | +0.7673 | 2.8009 | ±5.6017 | +0.274 | 0.7841 |  |
| Site: UW (vs UAB) | +1.7717 | 2.8134 | ±5.6267 | +0.630 | 0.5289 |  |
| **Age (years)** | **-0.4384** | 0.1222 | ±0.2443 | **-3.588** | **3.33e-04** | *** |
| BMI (kg/m2) | +0.3431 | 0.2327 | ±0.4655 | +1.474 | 0.1404 |  |
| Hypertension | +1.7782 | 2.4711 | ±4.9423 | +0.720 | 0.4718 |  |
| High cholesterol | -0.2464 | 2.0699 | ±4.1398 | -0.119 | 0.9052 |  |
| Kidney disease | +1.6148 | 3.6871 | ±7.3742 | +0.438 | 0.6614 |  |
| Circulatory disease | -3.9564 | 2.5975 | ±5.1951 | -1.523 | 0.1277 |  |
| CV (%) | -0.1714 | 0.3318 | ±0.6636 | -0.516 | 0.6055 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **178**, R² = **0.1973**, Adj R² = **0.1441**, F-statistic = **3.71** (p = **9.73e-05**), Residual SE = **13.648** on **166** df, AIC = **1447.2**, BIC = **1485.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.5222** | 11.6222 | ±23.2444 | **+3.659** | **2.53e-04** | *** |
| **Education: graduate level (vs college)** | **-6.4755** | 2.2519 | ±4.5038 | **-2.876** | **0.0040** | ** |
| Education: high school or below (vs college) | -0.9815 | 4.0465 | ±8.0930 | -0.243 | 0.8084 |  |
| Site: UCSD (vs UAB) | +0.8477 | 2.8023 | ±5.6046 | +0.302 | 0.7623 |  |
| Site: UW (vs UAB) | +1.9283 | 2.8024 | ±5.6047 | +0.688 | 0.4914 |  |
| **Age (years)** | **-0.4408** | 0.1220 | ±0.2441 | **-3.612** | **3.04e-04** | *** |
| BMI (kg/m2) | +0.3472 | 0.2256 | ±0.4513 | +1.538 | 0.1239 |  |
| Hypertension | +1.6422 | 2.4543 | ±4.9086 | +0.669 | 0.5034 |  |
| High cholesterol | -0.1950 | 2.0692 | ±4.1384 | -0.094 | 0.9249 |  |
| Kidney disease | +1.4719 | 3.6906 | ±7.3813 | +0.399 | 0.6900 |  |
| Circulatory disease | -4.0108 | 2.5817 | ±5.1634 | -1.554 | 0.1203 |  |
| Mean / SD ratio | +0.1513 | 0.7818 | ±1.5635 | +0.194 | 0.8465 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1972**, Adj R² = **0.1440**, F-statistic = **3.71** (p = **9.78e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.2436** | 11.5168 | ±23.0337 | **+3.842** | **1.22e-04** | *** |
| **Education: graduate level (vs college)** | **-6.5088** | 2.2518 | ±4.5036 | **-2.890** | **0.0038** | ** |
| Education: high school or below (vs college) | -1.1629 | 4.0109 | ±8.0218 | -0.290 | 0.7719 |  |
| Site: UCSD (vs UAB) | +0.8687 | 2.7955 | ±5.5910 | +0.311 | 0.7560 |  |
| Site: UW (vs UAB) | +2.0266 | 2.7650 | ±5.5301 | +0.733 | 0.4636 |  |
| **Age (years)** | **-0.4434** | 0.1223 | ±0.2446 | **-3.626** | **2.87e-04** | *** |
| BMI (kg/m2) | +0.3478 | 0.2242 | ±0.4483 | +1.552 | 0.1207 |  |
| Hypertension | +1.5048 | 2.4531 | ±4.9062 | +0.613 | 0.5396 |  |
| High cholesterol | -0.1801 | 2.0704 | ±4.1409 | -0.087 | 0.9307 |  |
| Kidney disease | +1.3720 | 3.6964 | ±7.3929 | +0.371 | 0.7105 |  |
| Circulatory disease | -4.0183 | 2.5740 | ±5.1480 | -1.561 | 0.1185 |  |
| Avg. daily mean/SD | -0.0832 | 0.5850 | ±1.1699 | -0.142 | 0.8868 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **178**, R² = **0.1997**, Adj R² = **0.1467**, F-statistic = **3.77** (p = **7.92e-05**), Residual SE = **13.627** on **166** df, AIC = **1446.6**, BIC = **1484.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.7191** | 11.8744 | ±23.7488 | **+3.345** | **8.23e-04** | *** |
| **Education: graduate level (vs college)** | **-6.5397** | 2.2649 | ±4.5299 | **-2.887** | **0.0039** | ** |
| Education: high school or below (vs college) | -1.2675 | 3.9167 | ±7.8335 | -0.324 | 0.7462 |  |
| Site: UCSD (vs UAB) | +0.8019 | 2.8069 | ±5.6138 | +0.286 | 0.7751 |  |
| Site: UW (vs UAB) | +2.0740 | 2.7121 | ±5.4243 | +0.765 | 0.4444 |  |
| **Age (years)** | **-0.4423** | 0.1209 | ±0.2418 | **-3.659** | **2.53e-04** | *** |
| BMI (kg/m2) | +0.3408 | 0.2272 | ±0.4544 | +1.500 | 0.1337 |  |
| Hypertension | +1.5008 | 2.3794 | ±4.7589 | +0.631 | 0.5282 |  |
| High cholesterol | -0.2565 | 2.0727 | ±4.1453 | -0.124 | 0.9015 |  |
| Kidney disease | +1.4303 | 3.7356 | ±7.4712 | +0.383 | 0.7018 |  |
| Circulatory disease | -4.0149 | 2.5657 | ±5.1313 | -1.565 | 0.1176 |  |
| MAG (mg/dL/h) | +0.1150 | 0.1385 | ±0.2770 | +0.830 | 0.4063 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **178**, R² = **0.1971**, Adj R² = **0.1439**, F-statistic = **3.71** (p = **9.84e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.5872** | 13.5021 | ±27.0041 | **+3.228** | **0.0012** | ** |
| **Education: graduate level (vs college)** | **-6.4969** | 2.2521 | ±4.5042 | **-2.885** | **0.0039** | ** |
| Education: high school or below (vs college) | -1.0986 | 3.9717 | ±7.9434 | -0.277 | 0.7821 |  |
| Site: UCSD (vs UAB) | +0.8726 | 2.8029 | ±5.6057 | +0.311 | 0.7555 |  |
| Site: UW (vs UAB) | +1.9933 | 2.7643 | ±5.5286 | +0.721 | 0.4708 |  |
| **Age (years)** | **-0.4422** | 0.1223 | ±0.2446 | **-3.615** | **3.01e-04** | *** |
| BMI (kg/m2) | +0.3475 | 0.2293 | ±0.4587 | +1.515 | 0.1298 |  |
| Hypertension | +1.5699 | 2.4265 | ±4.8530 | +0.647 | 0.5176 |  |
| High cholesterol | -0.1852 | 2.0806 | ±4.1613 | -0.089 | 0.9291 |  |
| Kidney disease | +1.4056 | 3.6922 | ±7.3843 | +0.381 | 0.7034 |  |
| Circulatory disease | -4.0226 | 2.5873 | ±5.1747 | -1.555 | 0.1200 |  |
| Avg. daily range (mg/dL) | -0.0003 | 0.0583 | ±0.1166 | -0.005 | 0.9963 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **178**, R² = **0.1971**, Adj R² = **0.1439**, F-statistic = **3.71** (p = **9.84e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6324** | 12.1403 | ±24.2806 | **+3.594** | **3.26e-04** | *** |
| **Education: graduate level (vs college)** | **-6.4946** | 2.2799 | ±4.5598 | **-2.849** | **0.0044** | ** |
| Education: high school or below (vs college) | -1.0787 | 3.8743 | ±7.7486 | -0.278 | 0.7807 |  |
| Site: UCSD (vs UAB) | +0.8607 | 2.6752 | ±5.3505 | +0.322 | 0.7476 |  |
| Site: UW (vs UAB) | +1.9792 | 2.6909 | ±5.3819 | +0.736 | 0.4620 |  |
| **Age (years)** | **-0.4420** | 0.1197 | ±0.2394 | **-3.693** | **2.22e-04** | *** |
| BMI (kg/m2) | +0.3476 | 0.2239 | ±0.4478 | +1.553 | 0.1205 |  |
| Hypertension | +1.5652 | 2.3887 | ±4.7774 | +0.655 | 0.5123 |  |
| High cholesterol | -0.1830 | 2.0641 | ±4.1281 | -0.089 | 0.9293 |  |
| Kidney disease | +1.4234 | 4.0706 | ±8.1413 | +0.350 | 0.7266 |  |
| Circulatory disease | -4.0084 | 2.6696 | ±5.3393 | -1.501 | 0.1332 |  |
| SD of daily means (mg/dL) | -0.0130 | 0.4890 | ±0.9779 | -0.027 | 0.9787 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **178**, R² = **0.1973**, Adj R² = **0.1441**, F-statistic = **3.71** (p = **9.69e-05**), Residual SE = **13.648** on **166** df, AIC = **1447.2**, BIC = **1485.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +39.1123 | 23.7927 | ±47.5853 | +1.644 | 0.1002 |  |
| **Education: graduate level (vs college)** | **-6.4598** | 2.2749 | ±4.5498 | **-2.840** | **0.0045** | ** |
| Education: high school or below (vs college) | -1.0611 | 3.9079 | ±7.8158 | -0.272 | 0.7860 |  |
| Site: UCSD (vs UAB) | +0.8536 | 2.7866 | ±5.5732 | +0.306 | 0.7594 |  |
| Site: UW (vs UAB) | +1.9716 | 2.7488 | ±5.4976 | +0.717 | 0.4732 |  |
| **Age (years)** | **-0.4399** | 0.1209 | ±0.2418 | **-3.639** | **2.74e-04** | *** |
| BMI (kg/m2) | +0.3491 | 0.2231 | ±0.4462 | +1.565 | 0.1176 |  |
| Hypertension | +1.5886 | 2.3999 | ±4.7998 | +0.662 | 0.5080 |  |
| High cholesterol | -0.2140 | 2.0618 | ±4.1237 | -0.104 | 0.9173 |  |
| Kidney disease | +1.5195 | 3.8781 | ±7.7562 | +0.392 | 0.6952 |  |
| Circulatory disease | -3.9638 | 2.6145 | ±5.2290 | -1.516 | 0.1295 |  |
| Time in range 70-180, pooled (%) | +0.0441 | 0.2198 | ±0.4395 | +0.201 | 0.8408 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **178**, R² = **0.1972**, Adj R² = **0.1440**, F-statistic = **3.71** (p = **9.80e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +41.2458 | 24.4872 | ±48.9745 | +1.684 | 0.0921 | . |
| **Education: graduate level (vs college)** | **-6.4799** | 2.2750 | ±4.5500 | **-2.848** | **0.0044** | ** |
| Education: high school or below (vs college) | -1.0850 | 3.9068 | ±7.8137 | -0.278 | 0.7812 |  |
| Site: UCSD (vs UAB) | +0.8634 | 2.7876 | ±5.5751 | +0.310 | 0.7568 |  |
| Site: UW (vs UAB) | +1.9872 | 2.7461 | ±5.4921 | +0.724 | 0.4693 |  |
| **Age (years)** | **-0.4410** | 0.1209 | ±0.2418 | **-3.648** | **2.65e-04** | *** |
| BMI (kg/m2) | +0.3482 | 0.2230 | ±0.4460 | +1.561 | 0.1184 |  |
| Hypertension | +1.5822 | 2.3998 | ±4.7996 | +0.659 | 0.5097 |  |
| High cholesterol | -0.2003 | 2.0627 | ±4.1255 | -0.097 | 0.9226 |  |
| Kidney disease | +1.4648 | 3.8864 | ±7.7728 | +0.377 | 0.7062 |  |
| Circulatory disease | -3.9917 | 2.6150 | ±5.2301 | -1.526 | 0.1269 |  |
| Avg. daily time in range 70-180 (%) | +0.0230 | 0.2269 | ±0.4539 | +0.101 | 0.9194 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **178**, R² = **0.2041**, Adj R² = **0.1514**, F-statistic = **3.87** (p = **5.51e-05**), Residual SE = **13.590** on **166** df, AIC = **1445.6**, BIC = **1483.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.7309** | 11.3132 | ±22.6263 | **+3.777** | **1.59e-04** | *** |
| **Education: graduate level (vs college)** | **-6.1641** | 2.2562 | ±4.5124 | **-2.732** | **0.0063** | ** |
| Education: high school or below (vs college) | -0.5398 | 3.9697 | ±7.9393 | -0.136 | 0.8918 |  |
| Site: UCSD (vs UAB) | +0.7027 | 2.7690 | ±5.5381 | +0.254 | 0.7997 |  |
| Site: UW (vs UAB) | +1.8957 | 2.7120 | ±5.4239 | +0.699 | 0.4845 |  |
| **Age (years)** | **-0.4204** | 0.1243 | ±0.2485 | **-3.383** | **7.17e-04** | *** |
| BMI (kg/m2) | +0.3419 | 0.2253 | ±0.4506 | +1.517 | 0.1292 |  |
| Hypertension | +1.5436 | 2.3680 | ±4.7360 | +0.652 | 0.5145 |  |
| High cholesterol | +0.0074 | 2.0514 | ±4.1028 | +0.004 | 0.9971 |  |
| Kidney disease | +1.2035 | 3.7003 | ±7.4005 | +0.325 | 0.7450 |  |
| Circulatory disease | -3.7492 | 2.6192 | ±5.2385 | -1.431 | 0.1523 |  |
| Time 54-69, pooled (%) | -4.1876 | 3.2870 | ±6.5740 | -1.274 | 0.2027 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **178**, R² = **0.2105**, Adj R² = **0.1582**, F-statistic = **4.02** (p = **3.21e-05**), Residual SE = **13.535** on **166** df, AIC = **1444.2**, BIC = **1482.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.1973** | 11.3114 | ±22.6227 | **+3.731** | **1.91e-04** | *** |
| **Education: graduate level (vs college)** | **-6.0620** | 2.2500 | ±4.4999 | **-2.694** | **0.0071** | ** |
| Education: high school or below (vs college) | -0.4125 | 3.9406 | ±7.8812 | -0.105 | 0.9166 |  |
| Site: UCSD (vs UAB) | +0.8045 | 2.7610 | ±5.5220 | +0.291 | 0.7707 |  |
| Site: UW (vs UAB) | +1.9654 | 2.7065 | ±5.4129 | +0.726 | 0.4677 |  |
| **Age (years)** | **-0.4105** | 0.1239 | ±0.2478 | **-3.314** | **9.21e-04** | *** |
| BMI (kg/m2) | +0.3388 | 0.2265 | ±0.4529 | +1.496 | 0.1346 |  |
| Hypertension | +1.5973 | 2.3628 | ±4.7255 | +0.676 | 0.4990 |  |
| High cholesterol | +0.0662 | 2.0396 | ±4.0792 | +0.032 | 0.9741 |  |
| Kidney disease | +0.9937 | 3.6705 | ±7.3411 | +0.271 | 0.7866 |  |
| Circulatory disease | -3.7341 | 2.6286 | ±5.2572 | -1.421 | 0.1554 |  |
| Avg. daily time 54-69 (%) | -5.5654 | 2.9333 | ±5.8666 | -1.897 | 0.0578 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **178**, R² = **0.2041**, Adj R² = **0.1514**, F-statistic = **3.87** (p = **5.51e-05**), Residual SE = **13.590** on **166** df, AIC = **1445.6**, BIC = **1483.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.7309** | 11.3132 | ±22.6263 | **+3.777** | **1.59e-04** | *** |
| **Education: graduate level (vs college)** | **-6.1641** | 2.2562 | ±4.5124 | **-2.732** | **0.0063** | ** |
| Education: high school or below (vs college) | -0.5398 | 3.9697 | ±7.9393 | -0.136 | 0.8918 |  |
| Site: UCSD (vs UAB) | +0.7027 | 2.7690 | ±5.5381 | +0.254 | 0.7997 |  |
| Site: UW (vs UAB) | +1.8957 | 2.7120 | ±5.4239 | +0.699 | 0.4845 |  |
| **Age (years)** | **-0.4204** | 0.1243 | ±0.2485 | **-3.383** | **7.17e-04** | *** |
| BMI (kg/m2) | +0.3419 | 0.2253 | ±0.4506 | +1.517 | 0.1292 |  |
| Hypertension | +1.5436 | 2.3680 | ±4.7360 | +0.652 | 0.5145 |  |
| High cholesterol | +0.0074 | 2.0514 | ±4.1028 | +0.004 | 0.9971 |  |
| Kidney disease | +1.2035 | 3.7003 | ±7.4005 | +0.325 | 0.7450 |  |
| Circulatory disease | -3.7492 | 2.6192 | ±5.2385 | -1.431 | 0.1523 |  |
| Time < 70 (%) | -4.1876 | 3.2870 | ±6.5740 | -1.274 | 0.2027 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **178**, R² = **0.2105**, Adj R² = **0.1582**, F-statistic = **4.02** (p = **3.21e-05**), Residual SE = **13.535** on **166** df, AIC = **1444.2**, BIC = **1482.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.1973** | 11.3114 | ±22.6227 | **+3.731** | **1.91e-04** | *** |
| **Education: graduate level (vs college)** | **-6.0620** | 2.2500 | ±4.4999 | **-2.694** | **0.0071** | ** |
| Education: high school or below (vs college) | -0.4125 | 3.9406 | ±7.8812 | -0.105 | 0.9166 |  |
| Site: UCSD (vs UAB) | +0.8045 | 2.7610 | ±5.5220 | +0.291 | 0.7707 |  |
| Site: UW (vs UAB) | +1.9654 | 2.7065 | ±5.4129 | +0.726 | 0.4677 |  |
| **Age (years)** | **-0.4105** | 0.1239 | ±0.2478 | **-3.314** | **9.21e-04** | *** |
| BMI (kg/m2) | +0.3388 | 0.2265 | ±0.4529 | +1.496 | 0.1346 |  |
| Hypertension | +1.5973 | 2.3628 | ±4.7255 | +0.676 | 0.4990 |  |
| High cholesterol | +0.0662 | 2.0396 | ±4.0792 | +0.032 | 0.9741 |  |
| Kidney disease | +0.9937 | 3.6705 | ±7.3411 | +0.271 | 0.7866 |  |
| Circulatory disease | -3.7341 | 2.6286 | ±5.2572 | -1.421 | 0.1554 |  |
| Avg. daily time < 70 (%) | -5.5654 | 2.9333 | ±5.8666 | -1.897 | 0.0578 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **178**, R² = **0.1972**, Adj R² = **0.1440**, F-statistic = **3.71** (p = **9.78e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.5455** | 11.2095 | ±22.4189 | **+3.885** | **1.02e-04** | *** |
| **Education: graduate level (vs college)** | **-6.4766** | 2.2739 | ±4.5478 | **-2.848** | **0.0044** | ** |
| Education: high school or below (vs college) | -1.0800 | 3.9071 | ±7.8143 | -0.276 | 0.7822 |  |
| Site: UCSD (vs UAB) | +0.8623 | 2.7892 | ±5.5783 | +0.309 | 0.7572 |  |
| Site: UW (vs UAB) | +1.9812 | 2.7464 | ±5.4927 | +0.721 | 0.4707 |  |
| **Age (years)** | **-0.4410** | 0.1210 | ±0.2420 | **-3.644** | **2.68e-04** | *** |
| BMI (kg/m2) | +0.3485 | 0.2230 | ±0.4460 | +1.563 | 0.1180 |  |
| Hypertension | +1.5808 | 2.4004 | ±4.8008 | +0.659 | 0.5102 |  |
| High cholesterol | -0.2038 | 2.0634 | ±4.1267 | -0.099 | 0.9213 |  |
| Kidney disease | +1.4758 | 3.8807 | ±7.7615 | +0.380 | 0.7037 |  |
| Circulatory disease | -3.9888 | 2.6100 | ±5.2200 | -1.528 | 0.1264 |  |
| Time 181-250, pooled (%) | -0.0269 | 0.2184 | ±0.4368 | -0.123 | 0.9020 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **178**, R² = **0.1971**, Adj R² = **0.1439**, F-statistic = **3.71** (p = **9.84e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.5637** | 11.2031 | ±22.4062 | **+3.889** | **1.01e-04** | *** |
| **Education: graduate level (vs college)** | **-6.4989** | 2.2742 | ±4.5484 | **-2.858** | **0.0043** | ** |
| Education: high school or below (vs college) | -1.1015 | 3.9058 | ±7.8116 | -0.282 | 0.7779 |  |
| Site: UCSD (vs UAB) | +0.8740 | 2.7900 | ±5.5801 | +0.313 | 0.7541 |  |
| Site: UW (vs UAB) | +1.9952 | 2.7431 | ±5.4861 | +0.727 | 0.4670 |  |
| **Age (years)** | **-0.4423** | 0.1210 | ±0.2420 | **-3.656** | **2.56e-04** | *** |
| BMI (kg/m2) | +0.3474 | 0.2228 | ±0.4456 | +1.559 | 0.1189 |  |
| Hypertension | +1.5670 | 2.4003 | ±4.8005 | +0.653 | 0.5139 |  |
| High cholesterol | -0.1830 | 2.0646 | ±4.1291 | -0.089 | 0.9294 |  |
| Kidney disease | +1.3980 | 3.8900 | ±7.7801 | +0.359 | 0.7193 |  |
| Circulatory disease | -4.0263 | 2.6107 | ±5.2213 | -1.542 | 0.1230 |  |
| Avg. daily time 181-250 (%) | +0.0023 | 0.2256 | ±0.4512 | +0.010 | 0.9917 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **178**, R² = **0.1972**, Adj R² = **0.1440**, F-statistic = **3.71** (p = **9.78e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.5455** | 11.2095 | ±22.4189 | **+3.885** | **1.02e-04** | *** |
| **Education: graduate level (vs college)** | **-6.4766** | 2.2739 | ±4.5478 | **-2.848** | **0.0044** | ** |
| Education: high school or below (vs college) | -1.0800 | 3.9071 | ±7.8143 | -0.276 | 0.7822 |  |
| Site: UCSD (vs UAB) | +0.8623 | 2.7892 | ±5.5783 | +0.309 | 0.7572 |  |
| Site: UW (vs UAB) | +1.9812 | 2.7464 | ±5.4927 | +0.721 | 0.4707 |  |
| **Age (years)** | **-0.4410** | 0.1210 | ±0.2420 | **-3.644** | **2.68e-04** | *** |
| BMI (kg/m2) | +0.3485 | 0.2230 | ±0.4460 | +1.563 | 0.1180 |  |
| Hypertension | +1.5808 | 2.4004 | ±4.8008 | +0.659 | 0.5102 |  |
| High cholesterol | -0.2038 | 2.0634 | ±4.1267 | -0.099 | 0.9213 |  |
| Kidney disease | +1.4758 | 3.8807 | ±7.7615 | +0.380 | 0.7037 |  |
| Circulatory disease | -3.9888 | 2.6100 | ±5.2200 | -1.528 | 0.1264 |  |
| Time > 180 (%) | -0.0269 | 0.2184 | ±0.4368 | -0.123 | 0.9020 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **178**, R² = **0.1971**, Adj R² = **0.1439**, F-statistic = **3.71** (p = **9.84e-05**), Residual SE = **13.649** on **166** df, AIC = **1447.2**, BIC = **1485.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.5637** | 11.2031 | ±22.4062 | **+3.889** | **1.01e-04** | *** |
| **Education: graduate level (vs college)** | **-6.4989** | 2.2742 | ±4.5484 | **-2.858** | **0.0043** | ** |
| Education: high school or below (vs college) | -1.1015 | 3.9058 | ±7.8116 | -0.282 | 0.7779 |  |
| Site: UCSD (vs UAB) | +0.8740 | 2.7900 | ±5.5801 | +0.313 | 0.7541 |  |
| Site: UW (vs UAB) | +1.9952 | 2.7431 | ±5.4861 | +0.727 | 0.4670 |  |
| **Age (years)** | **-0.4423** | 0.1210 | ±0.2420 | **-3.656** | **2.56e-04** | *** |
| BMI (kg/m2) | +0.3474 | 0.2228 | ±0.4456 | +1.559 | 0.1189 |  |
| Hypertension | +1.5670 | 2.4003 | ±4.8005 | +0.653 | 0.5139 |  |
| High cholesterol | -0.1830 | 2.0646 | ±4.1291 | -0.089 | 0.9294 |  |
| Kidney disease | +1.3980 | 3.8900 | ±7.7801 | +0.359 | 0.7193 |  |
| Circulatory disease | -4.0263 | 2.6107 | ±5.2213 | -1.542 | 0.1230 |  |
| Avg. daily time > 180 (%) | +0.0023 | 0.2256 | ±0.4512 | +0.010 | 0.9917 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 178)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **178**, R² = **0.2014**, Adj R² = **0.1485**, F-statistic = **3.81** (p = **6.91e-05**), Residual SE = **13.613** on **166** df, AIC = **1446.2**, BIC = **1484.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.0260** | 11.2865 | ±22.5730 | **+3.901** | **9.59e-05** | *** |
| **Education: graduate level (vs college)** | **-6.5652** | 2.2652 | ±4.5305 | **-2.898** | **0.0038** | ** |
| Education: high school or below (vs college) | -1.4478 | 3.8529 | ±7.7058 | -0.376 | 0.7071 |  |
| Site: UCSD (vs UAB) | +1.1389 | 2.8139 | ±5.6277 | +0.405 | 0.6857 |  |
| Site: UW (vs UAB) | +2.2300 | 2.6927 | ±5.3855 | +0.828 | 0.4076 |  |
| **Age (years)** | **-0.4498** | 0.1222 | ±0.2443 | **-3.682** | **2.32e-04** | *** |
| BMI (kg/m2) | +0.3287 | 0.2249 | ±0.4498 | +1.462 | 0.1439 |  |
| Hypertension | +1.7047 | 2.4280 | ±4.8560 | +0.702 | 0.4826 |  |
| High cholesterol | -0.1488 | 2.0750 | ±4.1501 | -0.072 | 0.9428 |  |
| Kidney disease | +0.8502 | 3.8579 | ±7.7158 | +0.220 | 0.8256 |  |
| Circulatory disease | -4.3837 | 2.5942 | ±5.1884 | -1.690 | 0.0911 | . |
| Nocturnal time > 180 (%) | +0.2012 | 0.2503 | ±0.5007 | +0.804 | 0.4215 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 177; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2077**, F-statistic = **5.61** (p = **3.30e-07**), Residual SE = **8.026** on **166** df, AIC = **1250.2**, BIC = **1285.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.5749** | 5.9627 | ±11.9255 | **+12.842** | **9.51e-38** | *** |
| **Education: graduate level (vs college)** | **-3.4460** | 1.3908 | ±2.7815 | **-2.478** | **0.0132** | * |
| **Education: high school or below (vs college)** | **-4.0112** | 2.0130 | ±4.0260 | **-1.993** | **0.0463** | * |
| Site: UCSD (vs UAB) | -1.4843 | 1.7025 | ±3.4049 | -0.872 | 0.3833 |  |
| Site: UW (vs UAB) | -0.8727 | 1.6431 | ±3.2862 | -0.531 | 0.5953 |  |
| **Age (years)** | **-0.2794** | 0.0749 | ±0.1499 | **-3.728** | **1.93e-04** | *** |
| **BMI (kg/m2)** | **+0.1894** | 0.0962 | ±0.1925 | **+1.968** | **0.0490** | * |
| Hypertension | +1.4911 | 1.5123 | ±3.0246 | +0.986 | 0.3241 |  |
| High cholesterol | +0.3730 | 1.2943 | ±2.5885 | +0.288 | 0.7732 |  |
| **Kidney disease** | **+6.7713** | 1.8211 | ±3.6421 | **+3.718** | **2.01e-04** | *** |
| Circulatory disease | -0.3238 | 1.8606 | ±3.7212 | -0.174 | 0.8618 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **177**, R² = **0.2533**, Adj R² = **0.2035**, F-statistic = **5.09** (p = **7.82e-07**), Residual SE = **8.048** on **165** df, AIC = **1252.1**, BIC = **1290.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.3842** | 8.6535 | ±17.3070 | **+8.596** | **8.27e-18** | *** |
| **Education: graduate level (vs college)** | **-3.4269** | 1.4101 | ±2.8202 | **-2.430** | **0.0151** | * |
| **Education: high school or below (vs college)** | **-4.0355** | 2.0173 | ±4.0345 | **-2.000** | **0.0455** | * |
| Site: UCSD (vs UAB) | -1.4831 | 1.7067 | ±3.4135 | -0.869 | 0.3849 |  |
| Site: UW (vs UAB) | -0.8638 | 1.6557 | ±3.3113 | -0.522 | 0.6019 |  |
| **Age (years)** | **-0.2796** | 0.0753 | ±0.1505 | **-3.714** | **2.04e-04** | *** |
| BMI (kg/m2) | +0.1838 | 0.0988 | ±0.1976 | +1.861 | 0.0628 | . |
| Hypertension | +1.4506 | 1.5262 | ±3.0523 | +0.951 | 0.3419 |  |
| High cholesterol | +0.3206 | 1.3245 | ±2.6490 | +0.242 | 0.8088 |  |
| **Kidney disease** | **+6.8563** | 1.8363 | ±3.6726 | **+3.734** | **1.89e-04** | *** |
| Circulatory disease | -0.3995 | 1.8643 | ±3.7287 | -0.214 | 0.8303 |  |
| HbA1c (%) | +0.4085 | 1.2964 | ±2.5927 | +0.315 | 0.7527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **177**, R² = **0.2598**, Adj R² = **0.2104**, F-statistic = **5.26** (p = **4.22e-07**), Residual SE = **8.013** on **165** df, AIC = **1250.6**, BIC = **1288.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4529** | 8.2139 | ±16.4277 | **+8.456** | **2.78e-17** | *** |
| **Education: graduate level (vs college)** | **-3.3827** | 1.4059 | ±2.8118 | **-2.406** | **0.0161** | * |
| Education: high school or below (vs college) | -3.8330 | 2.0302 | ±4.0604 | -1.888 | 0.0590 | . |
| Site: UCSD (vs UAB) | -1.6001 | 1.7033 | ±3.4067 | -0.939 | 0.3475 |  |
| Site: UW (vs UAB) | -0.9175 | 1.6379 | ±3.2758 | -0.560 | 0.5754 |  |
| **Age (years)** | **-0.2782** | 0.0752 | ±0.1504 | **-3.700** | **2.15e-04** | *** |
| BMI (kg/m2) | +0.1806 | 0.0974 | ±0.1948 | +1.854 | 0.0637 | . |
| Hypertension | +1.3938 | 1.4950 | ±2.9900 | +0.932 | 0.3512 |  |
| High cholesterol | +0.3676 | 1.3020 | ±2.6041 | +0.282 | 0.7777 |  |
| **Kidney disease** | **+6.5856** | 1.8243 | ±3.6486 | **+3.610** | **3.06e-04** | *** |
| Circulatory disease | -0.5045 | 1.8391 | ±3.6783 | -0.274 | 0.7839 |  |
| Mean glucose (mg/dL) | +0.0589 | 0.0477 | ±0.0953 | +1.237 | 0.2163 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **177**, R² = **0.2598**, Adj R² = **0.2104**, F-statistic = **5.26** (p = **4.22e-07**), Residual SE = **8.013** on **165** df, AIC = **1250.6**, BIC = **1288.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.2962** | 13.5700 | ±27.1400 | **+4.517** | **6.27e-06** | *** |
| **Education: graduate level (vs college)** | **-3.3827** | 1.4059 | ±2.8118 | **-2.406** | **0.0161** | * |
| Education: high school or below (vs college) | -3.8330 | 2.0302 | ±4.0604 | -1.888 | 0.0590 | . |
| Site: UCSD (vs UAB) | -1.6001 | 1.7033 | ±3.4067 | -0.939 | 0.3475 |  |
| Site: UW (vs UAB) | -0.9175 | 1.6379 | ±3.2758 | -0.560 | 0.5754 |  |
| **Age (years)** | **-0.2782** | 0.0752 | ±0.1504 | **-3.700** | **2.15e-04** | *** |
| BMI (kg/m2) | +0.1806 | 0.0974 | ±0.1948 | +1.854 | 0.0637 | . |
| Hypertension | +1.3938 | 1.4950 | ±2.9900 | +0.932 | 0.3512 |  |
| High cholesterol | +0.3676 | 1.3020 | ±2.6041 | +0.282 | 0.7777 |  |
| **Kidney disease** | **+6.5856** | 1.8243 | ±3.6486 | **+3.610** | **3.06e-04** | *** |
| Circulatory disease | -0.5045 | 1.8391 | ±3.6783 | -0.274 | 0.7839 |  |
| GMI (%) | +2.4643 | 1.9929 | ±3.9858 | +1.237 | 0.2163 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **177**, R² = **0.2574**, Adj R² = **0.2079**, F-statistic = **5.20** (p = **5.30e-07**), Residual SE = **8.026** on **165** df, AIC = **1251.1**, BIC = **1289.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+71.2904** | 7.0019 | ±14.0037 | **+10.182** | **2.39e-24** | *** |
| **Education: graduate level (vs college)** | **-3.4387** | 1.3958 | ±2.7915 | **-2.464** | **0.0138** | * |
| Education: high school or below (vs college) | -3.9271 | 2.0345 | ±4.0690 | -1.930 | 0.0536 | . |
| Site: UCSD (vs UAB) | -1.6025 | 1.7053 | ±3.4105 | -0.940 | 0.3474 |  |
| Site: UW (vs UAB) | -0.9327 | 1.6449 | ±3.2899 | -0.567 | 0.5707 |  |
| **Age (years)** | **-0.2747** | 0.0747 | ±0.1493 | **-3.680** | **2.33e-04** | *** |
| BMI (kg/m2) | +0.1816 | 0.0984 | ±0.1968 | +1.846 | 0.0648 | . |
| Hypertension | +1.4163 | 1.5046 | ±3.0091 | +0.941 | 0.3465 |  |
| High cholesterol | +0.3417 | 1.3049 | ±2.6098 | +0.262 | 0.7935 |  |
| **Kidney disease** | **+6.7945** | 1.7934 | ±3.5867 | **+3.789** | **1.51e-04** | *** |
| Circulatory disease | -0.5210 | 1.8397 | ±3.6793 | -0.283 | 0.7770 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0427 | 0.0423 | ±0.0846 | +1.010 | 0.3125 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2030**, F-statistic = **5.07** (p = **8.19e-07**), Residual SE = **8.051** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.4244** | 6.1574 | ±12.3149 | **+12.412** | **2.26e-35** | *** |
| **Education: graduate level (vs college)** | **-3.4497** | 1.3889 | ±2.7778 | **-2.484** | **0.0130** | * |
| **Education: high school or below (vs college)** | **-4.0291** | 2.0195 | ±4.0391 | **-1.995** | **0.0460** | * |
| Site: UCSD (vs UAB) | -1.4813 | 1.7131 | ±3.4262 | -0.865 | 0.3872 |  |
| Site: UW (vs UAB) | -0.8613 | 1.6962 | ±3.3924 | -0.508 | 0.6116 |  |
| **Age (years)** | **-0.2795** | 0.0759 | ±0.1518 | **-3.683** | **2.30e-04** | *** |
| BMI (kg/m2) | +0.1894 | 0.0967 | ±0.1933 | +1.960 | 0.0500 | . |
| Hypertension | +1.4769 | 1.5343 | ±3.0686 | +0.963 | 0.3358 |  |
| High cholesterol | +0.3761 | 1.2961 | ±2.5923 | +0.290 | 0.7717 |  |
| **Kidney disease** | **+6.7561** | 1.8265 | ±3.6529 | **+3.699** | **2.16e-04** | *** |
| Circulatory disease | -0.3327 | 1.8595 | ±3.7190 | -0.179 | 0.8580 |  |
| Glucose SD, pooled (mg/dL) | +0.0079 | 0.1316 | ±0.2632 | +0.060 | 0.9524 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2030**, F-statistic = **5.08** (p = **8.15e-07**), Residual SE = **8.050** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.2768** | 6.0625 | ±12.1250 | **+12.582** | **2.66e-36** | *** |
| **Education: graduate level (vs college)** | **-3.4535** | 1.3878 | ±2.7757 | **-2.488** | **0.0128** | * |
| **Education: high school or below (vs college)** | **-4.0397** | 2.0223 | ±4.0446 | **-1.998** | **0.0458** | * |
| Site: UCSD (vs UAB) | -1.4873 | 1.7096 | ±3.4193 | -0.870 | 0.3843 |  |
| Site: UW (vs UAB) | -0.8580 | 1.6784 | ±3.3567 | -0.511 | 0.6092 |  |
| **Age (years)** | **-0.2798** | 0.0761 | ±0.1522 | **-3.675** | **2.37e-04** | *** |
| **BMI (kg/m2)** | **+0.1896** | 0.0966 | ±0.1932 | **+1.963** | **0.0496** | * |
| Hypertension | +1.4549 | 1.5268 | ±3.0536 | +0.953 | 0.3406 |  |
| High cholesterol | +0.3813 | 1.2974 | ±2.5947 | +0.294 | 0.7688 |  |
| **Kidney disease** | **+6.7495** | 1.8213 | ±3.6425 | **+3.706** | **2.11e-04** | *** |
| Circulatory disease | -0.3381 | 1.8560 | ±3.7120 | -0.182 | 0.8554 |  |
| Avg. daily SD (mg/dL) | +0.0171 | 0.1333 | ±0.2667 | +0.129 | 0.8977 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **177**, R² = **0.2548**, Adj R² = **0.2051**, F-statistic = **5.13** (p = **6.78e-07**), Residual SE = **8.040** on **165** df, AIC = **1251.8**, BIC = **1289.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+78.7158** | 6.3584 | ±12.7167 | **+12.380** | **3.36e-35** | *** |
| **Education: graduate level (vs college)** | **-3.3789** | 1.3864 | ±2.7729 | **-2.437** | **0.0148** | * |
| Education: high school or below (vs college) | -3.6988 | 2.0445 | ±4.0890 | -1.809 | 0.0704 | . |
| Site: UCSD (vs UAB) | -1.5635 | 1.7166 | ±3.4331 | -0.911 | 0.3624 |  |
| Site: UW (vs UAB) | -1.0457 | 1.6956 | ±3.3913 | -0.617 | 0.5374 |  |
| **Age (years)** | **-0.2764** | 0.0760 | ±0.1520 | **-3.636** | **2.77e-04** | *** |
| BMI (kg/m2) | +0.1860 | 0.0965 | ±0.1930 | +1.928 | 0.0539 | . |
| Hypertension | +1.6569 | 1.5416 | ±3.0831 | +1.075 | 0.2825 |  |
| High cholesterol | +0.3282 | 1.2922 | ±2.5843 | +0.254 | 0.7995 |  |
| **Kidney disease** | **+6.9283** | 1.8117 | ±3.6233 | **+3.824** | **1.31e-04** | *** |
| Circulatory disease | -0.2699 | 1.8736 | ±3.7473 | -0.144 | 0.8855 |  |
| CV (%) | -0.1351 | 0.1870 | ±0.3740 | -0.722 | 0.4700 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **177**, R² = **0.2531**, Adj R² = **0.2034**, F-statistic = **5.08** (p = **7.91e-07**), Residual SE = **8.049** on **165** df, AIC = **1252.1**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.5118** | 7.3131 | ±14.6261 | **+10.326** | **5.40e-25** | *** |
| **Education: graduate level (vs college)** | **-3.4252** | 1.3897 | ±2.7794 | **-2.465** | **0.0137** | * |
| Education: high school or below (vs college) | -3.8906 | 2.0431 | ±4.0861 | -1.904 | 0.0569 | . |
| Site: UCSD (vs UAB) | -1.5083 | 1.7132 | ±3.4265 | -0.880 | 0.3786 |  |
| Site: UW (vs UAB) | -0.9391 | 1.6868 | ±3.3737 | -0.557 | 0.5777 |  |
| **Age (years)** | **-0.2779** | 0.0763 | ±0.1527 | **-3.641** | **2.72e-04** | *** |
| BMI (kg/m2) | +0.1891 | 0.0969 | ±0.1937 | +1.952 | 0.0510 | . |
| Hypertension | +1.5666 | 1.5330 | ±3.0659 | +1.022 | 0.3068 |  |
| High cholesterol | +0.3642 | 1.2970 | ±2.5941 | +0.281 | 0.7789 |  |
| **Kidney disease** | **+6.8363** | 1.8183 | ±3.6366 | **+3.760** | **1.70e-04** | *** |
| Circulatory disease | -0.3106 | 1.8713 | ±3.7425 | -0.166 | 0.8682 |  |
| Mean / SD ratio | +0.1544 | 0.4956 | ±0.9912 | +0.312 | 0.7553 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2030**, F-statistic = **5.07** (p = **8.19e-07**), Residual SE = **8.051** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.3545** | 7.2285 | ±14.4569 | **+10.563** | **4.42e-26** | *** |
| **Education: graduate level (vs college)** | **-3.4427** | 1.3908 | ±2.7816 | **-2.475** | **0.0133** | * |
| Education: high school or below (vs college) | -3.9912 | 2.0417 | ±4.0834 | -1.955 | 0.0506 | . |
| Site: UCSD (vs UAB) | -1.4824 | 1.7064 | ±3.4128 | -0.869 | 0.3850 |  |
| Site: UW (vs UAB) | -0.8828 | 1.6738 | ±3.3476 | -0.527 | 0.5979 |  |
| **Age (years)** | **-0.2790** | 0.0769 | ±0.1537 | **-3.630** | **2.84e-04** | *** |
| BMI (kg/m2) | +0.1893 | 0.0969 | ±0.1939 | +1.953 | 0.0508 | . |
| Hypertension | +1.5116 | 1.5294 | ±3.0588 | +0.988 | 0.3230 |  |
| High cholesterol | +0.3719 | 1.3004 | ±2.6008 | +0.286 | 0.7749 |  |
| **Kidney disease** | **+6.7806** | 1.8209 | ±3.6418 | **+3.724** | **1.96e-04** | *** |
| Circulatory disease | -0.3253 | 1.8781 | ±3.7562 | -0.173 | 0.8625 |  |
| Avg. daily mean/SD | +0.0269 | 0.3884 | ±0.7768 | +0.069 | 0.9449 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **177**, R² = **0.2592**, Adj R² = **0.2098**, F-statistic = **5.25** (p = **4.47e-07**), Residual SE = **8.016** on **165** df, AIC = **1250.7**, BIC = **1288.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+72.9142** | 6.2660 | ±12.5321 | **+11.636** | **2.69e-31** | *** |
| **Education: graduate level (vs college)** | **-3.4778** | 1.3925 | ±2.7851 | **-2.497** | **0.0125** | * |
| **Education: high school or below (vs college)** | **-4.1668** | 1.9981 | ±3.9961 | **-2.085** | **0.0370** | * |
| Site: UCSD (vs UAB) | -1.5629 | 1.7027 | ±3.4055 | -0.918 | 0.3587 |  |
| Site: UW (vs UAB) | -0.8034 | 1.6332 | ±3.2665 | -0.492 | 0.6228 |  |
| **Age (years)** | **-0.2794** | 0.0748 | ±0.1496 | **-3.734** | **1.88e-04** | *** |
| BMI (kg/m2) | +0.1827 | 0.0970 | ±0.1940 | +1.883 | 0.0597 | . |
| Hypertension | +1.4257 | 1.5077 | ±3.0155 | +0.946 | 0.3444 |  |
| High cholesterol | +0.2943 | 1.3073 | ±2.6147 | +0.225 | 0.8219 |  |
| **Kidney disease** | **+6.8189** | 1.8246 | ±3.6493 | **+3.737** | **1.86e-04** | *** |
| Circulatory disease | -0.3191 | 1.8332 | ±3.6664 | -0.174 | 0.8618 |  |
| MAG (mg/dL/h) | +0.1099 | 0.0909 | ±0.1819 | +1.208 | 0.2271 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **177**, R² = **0.2541**, Adj R² = **0.2044**, F-statistic = **5.11** (p = **7.21e-07**), Residual SE = **8.043** on **165** df, AIC = **1251.9**, BIC = **1290.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.8283** | 6.0299 | ±12.0597 | **+12.410** | **2.32e-35** | *** |
| **Education: graduate level (vs college)** | **-3.4637** | 1.3890 | ±2.7781 | **-2.494** | **0.0126** | * |
| **Education: high school or below (vs college)** | **-4.1269** | 2.0357 | ±4.0714 | **-2.027** | **0.0426** | * |
| Site: UCSD (vs UAB) | -1.4668 | 1.7133 | ±3.4266 | -0.856 | 0.3919 |  |
| Site: UW (vs UAB) | -0.8017 | 1.6776 | ±3.3552 | -0.478 | 0.6327 |  |
| **Age (years)** | **-0.2815** | 0.0768 | ±0.1536 | **-3.666** | **2.47e-04** | *** |
| **BMI (kg/m2)** | **+0.1928** | 0.0963 | ±0.1927 | **+2.001** | **0.0453** | * |
| Hypertension | +1.3794 | 1.5094 | ±3.0189 | +0.914 | 0.3608 |  |
| High cholesterol | +0.3937 | 1.3028 | ±2.6056 | +0.302 | 0.7625 |  |
| **Kidney disease** | **+6.7072** | 1.8232 | ±3.6464 | **+3.679** | **2.34e-04** | *** |
| Circulatory disease | -0.3724 | 1.8380 | ±3.6760 | -0.203 | 0.8394 |  |
| Avg. daily range (mg/dL) | +0.0190 | 0.0351 | ±0.0701 | +0.543 | 0.5871 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **177**, R² = **0.2537**, Adj R² = **0.2040**, F-statistic = **5.10** (p = **7.50e-07**), Residual SE = **8.045** on **165** df, AIC = **1252.0**, BIC = **1290.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.1966** | 6.1224 | ±12.2447 | **+12.609** | **1.88e-36** | *** |
| **Education: graduate level (vs college)** | **-3.4226** | 1.4013 | ±2.8027 | **-2.442** | **0.0146** | * |
| Education: high school or below (vs college) | -3.8201 | 1.9799 | ±3.9598 | -1.929 | 0.0537 | . |
| Site: UCSD (vs UAB) | -1.5923 | 1.7176 | ±3.4352 | -0.927 | 0.3539 |  |
| Site: UW (vs UAB) | -1.0072 | 1.6864 | ±3.3727 | -0.597 | 0.5503 |  |
| **Age (years)** | **-0.2772** | 0.0756 | ±0.1511 | **-3.668** | **2.44e-04** | *** |
| **BMI (kg/m2)** | **+0.1901** | 0.0967 | ±0.1934 | **+1.966** | **0.0494** | * |
| Hypertension | +1.4631 | 1.5129 | ±3.0259 | +0.967 | 0.3335 |  |
| High cholesterol | +0.3884 | 1.3059 | ±2.6117 | +0.297 | 0.7661 |  |
| **Kidney disease** | **+6.9388** | 1.8591 | ±3.7181 | **+3.732** | **1.90e-04** | *** |
| Circulatory disease | -0.1923 | 1.9013 | ±3.8025 | -0.101 | 0.9195 |  |
| SD of daily means (mg/dL) | -0.1155 | 0.2648 | ±0.5297 | -0.436 | 0.6629 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2030**, F-statistic = **5.08** (p = **8.16e-07**), Residual SE = **8.050** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.1210** | 15.8690 | ±31.7380 | **+4.734** | **2.20e-06** | *** |
| **Education: graduate level (vs college)** | **-3.4375** | 1.4035 | ±2.8069 | **-2.449** | **0.0143** | * |
| **Education: high school or below (vs college)** | **-4.0002** | 2.0232 | ±4.0465 | **-1.977** | **0.0480** | * |
| Site: UCSD (vs UAB) | -1.4860 | 1.7109 | ±3.4218 | -0.869 | 0.3851 |  |
| Site: UW (vs UAB) | -0.8772 | 1.6682 | ±3.3364 | -0.526 | 0.5990 |  |
| **Age (years)** | **-0.2787** | 0.0754 | ±0.1508 | **-3.695** | **2.20e-04** | *** |
| BMI (kg/m2) | +0.1900 | 0.0978 | ±0.1955 | +1.944 | 0.0519 | . |
| Hypertension | +1.4981 | 1.5166 | ±3.0331 | +0.988 | 0.3232 |  |
| High cholesterol | +0.3678 | 1.2972 | ±2.5944 | +0.284 | 0.7768 |  |
| **Kidney disease** | **+6.7989** | 1.8524 | ±3.7048 | **+3.670** | **2.42e-04** | *** |
| Circulatory disease | -0.3031 | 1.8942 | ±3.7884 | -0.160 | 0.8729 |  |
| Time in range 70-180, pooled (%) | +0.0144 | 0.1431 | ±0.2863 | +0.100 | 0.9200 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2029**, F-statistic = **5.07** (p = **8.20e-07**), Residual SE = **8.051** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.9252** | 16.3474 | ±32.6947 | **+4.644** | **3.41e-06** | *** |
| **Education: graduate level (vs college)** | **-3.4429** | 1.4037 | ±2.8074 | **-2.453** | **0.0142** | * |
| **Education: high school or below (vs college)** | **-4.0078** | 2.0217 | ±4.0433 | **-1.982** | **0.0474** | * |
| Site: UCSD (vs UAB) | -1.4848 | 1.7104 | ±3.4209 | -0.868 | 0.3853 |  |
| Site: UW (vs UAB) | -0.8734 | 1.6639 | ±3.3278 | -0.525 | 0.5997 |  |
| **Age (years)** | **-0.2790** | 0.0754 | ±0.1509 | **-3.699** | **2.16e-04** | *** |
| BMI (kg/m2) | +0.1896 | 0.0976 | ±0.1952 | +1.943 | 0.0520 | . |
| Hypertension | +1.4951 | 1.5143 | ±3.0285 | +0.987 | 0.3235 |  |
| High cholesterol | +0.3706 | 1.2976 | ±2.5952 | +0.286 | 0.7752 |  |
| **Kidney disease** | **+6.7836** | 1.8553 | ±3.7105 | **+3.656** | **2.56e-04** | *** |
| Circulatory disease | -0.3144 | 1.8973 | ±3.7945 | -0.166 | 0.8684 |  |
| Avg. daily time in range 70-180 (%) | +0.0064 | 0.1486 | ±0.2972 | +0.043 | 0.9655 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **177**, R² = **0.2746**, Adj R² = **0.2263**, F-statistic = **5.68** (p = **1.01e-07**), Residual SE = **7.932** on **165** df, AIC = **1247.0**, BIC = **1285.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.6936** | 5.9855 | ±11.9709 | **+12.646** | **1.17e-36** | *** |
| **Education: graduate level (vs college)** | **-3.0733** | 1.4021 | ±2.8043 | **-2.192** | **0.0284** | * |
| Education: high school or below (vs college) | -3.4004 | 1.9598 | ±3.9196 | -1.735 | 0.0827 | . |
| Site: UCSD (vs UAB) | -1.6845 | 1.6790 | ±3.3579 | -1.003 | 0.3157 |  |
| Site: UW (vs UAB) | -0.9896 | 1.6343 | ±3.2686 | -0.606 | 0.5448 |  |
| **Age (years)** | **-0.2557** | 0.0748 | ±0.1496 | **-3.418** | **6.32e-04** | *** |
| BMI (kg/m2) | +0.1829 | 0.0955 | ±0.1911 | +1.915 | 0.0555 | . |
| Hypertension | +1.4630 | 1.4575 | ±2.9151 | +1.004 | 0.3155 |  |
| High cholesterol | +0.5646 | 1.2879 | ±2.5758 | +0.438 | 0.6611 |  |
| **Kidney disease** | **+6.5899** | 1.8155 | ±3.6310 | **+3.630** | **2.84e-04** | *** |
| Circulatory disease | -0.0333 | 1.8570 | ±3.7139 | -0.018 | 0.9857 |  |
| **Time 54-69, pooled (%)** | **-4.5166** | 1.6904 | ±3.3807 | **-2.672** | **0.0075** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **177**, R² = **0.2744**, Adj R² = **0.2260**, F-statistic = **5.67** (p = **1.03e-07**), Residual SE = **7.933** on **165** df, AIC = **1247.0**, BIC = **1285.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.5279** | 6.0035 | ±12.0070 | **+12.581** | **2.70e-36** | *** |
| **Education: graduate level (vs college)** | **-3.0993** | 1.4051 | ±2.8102 | **-2.206** | **0.0274** | * |
| Education: high school or below (vs college) | -3.4739 | 1.9450 | ±3.8899 | -1.786 | 0.0741 | . |
| Site: UCSD (vs UAB) | -1.5488 | 1.6817 | ±3.3634 | -0.921 | 0.3571 |  |
| Site: UW (vs UAB) | -0.9024 | 1.6361 | ±3.2722 | -0.552 | 0.5812 |  |
| **Age (years)** | **-0.2547** | 0.0750 | ±0.1500 | **-3.395** | **6.85e-04** | *** |
| BMI (kg/m2) | +0.1824 | 0.0958 | ±0.1916 | +1.904 | 0.0569 | . |
| Hypertension | +1.5125 | 1.4579 | ±2.9157 | +1.037 | 0.2995 |  |
| High cholesterol | +0.5565 | 1.2891 | ±2.5782 | +0.432 | 0.6659 |  |
| **Kidney disease** | **+6.4776** | 1.8276 | ±3.6552 | **+3.544** | **3.94e-04** | *** |
| Circulatory disease | -0.1033 | 1.8432 | ±3.6865 | -0.056 | 0.9553 |  |
| **Avg. daily time 54-69 (%)** | **-4.3124** | 1.8551 | ±3.7103 | **-2.325** | **0.0201** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **177**, R² = **0.2746**, Adj R² = **0.2263**, F-statistic = **5.68** (p = **1.01e-07**), Residual SE = **7.932** on **165** df, AIC = **1247.0**, BIC = **1285.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.6936** | 5.9855 | ±11.9709 | **+12.646** | **1.17e-36** | *** |
| **Education: graduate level (vs college)** | **-3.0733** | 1.4021 | ±2.8043 | **-2.192** | **0.0284** | * |
| Education: high school or below (vs college) | -3.4004 | 1.9598 | ±3.9196 | -1.735 | 0.0827 | . |
| Site: UCSD (vs UAB) | -1.6845 | 1.6790 | ±3.3579 | -1.003 | 0.3157 |  |
| Site: UW (vs UAB) | -0.9896 | 1.6343 | ±3.2686 | -0.606 | 0.5448 |  |
| **Age (years)** | **-0.2557** | 0.0748 | ±0.1496 | **-3.418** | **6.32e-04** | *** |
| BMI (kg/m2) | +0.1829 | 0.0955 | ±0.1911 | +1.915 | 0.0555 | . |
| Hypertension | +1.4630 | 1.4575 | ±2.9151 | +1.004 | 0.3155 |  |
| High cholesterol | +0.5646 | 1.2879 | ±2.5758 | +0.438 | 0.6611 |  |
| **Kidney disease** | **+6.5899** | 1.8155 | ±3.6310 | **+3.630** | **2.84e-04** | *** |
| Circulatory disease | -0.0333 | 1.8570 | ±3.7139 | -0.018 | 0.9857 |  |
| **Time < 70 (%)** | **-4.5166** | 1.6904 | ±3.3807 | **-2.672** | **0.0075** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **177**, R² = **0.2744**, Adj R² = **0.2260**, F-statistic = **5.67** (p = **1.03e-07**), Residual SE = **7.933** on **165** df, AIC = **1247.0**, BIC = **1285.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.5279** | 6.0035 | ±12.0070 | **+12.581** | **2.70e-36** | *** |
| **Education: graduate level (vs college)** | **-3.0993** | 1.4051 | ±2.8102 | **-2.206** | **0.0274** | * |
| Education: high school or below (vs college) | -3.4739 | 1.9450 | ±3.8899 | -1.786 | 0.0741 | . |
| Site: UCSD (vs UAB) | -1.5488 | 1.6817 | ±3.3634 | -0.921 | 0.3571 |  |
| Site: UW (vs UAB) | -0.9024 | 1.6361 | ±3.2722 | -0.552 | 0.5812 |  |
| **Age (years)** | **-0.2547** | 0.0750 | ±0.1500 | **-3.395** | **6.85e-04** | *** |
| BMI (kg/m2) | +0.1824 | 0.0958 | ±0.1916 | +1.904 | 0.0569 | . |
| Hypertension | +1.5125 | 1.4579 | ±2.9157 | +1.037 | 0.2995 |  |
| High cholesterol | +0.5565 | 1.2891 | ±2.5782 | +0.432 | 0.6659 |  |
| **Kidney disease** | **+6.4776** | 1.8276 | ±3.6552 | **+3.544** | **3.94e-04** | *** |
| Circulatory disease | -0.1033 | 1.8432 | ±3.6865 | -0.056 | 0.9553 |  |
| **Avg. daily time < 70 (%)** | **-4.3124** | 1.8551 | ±3.7103 | **-2.325** | **0.0201** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2029**, F-statistic = **5.07** (p = **8.20e-07**), Residual SE = **8.051** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.5789** | 6.0043 | ±12.0086 | **+12.754** | **2.96e-37** | *** |
| **Education: graduate level (vs college)** | **-3.4482** | 1.4027 | ±2.8054 | **-2.458** | **0.0140** | * |
| **Education: high school or below (vs college)** | **-4.0140** | 2.0230 | ±4.0460 | **-1.984** | **0.0472** | * |
| Site: UCSD (vs UAB) | -1.4840 | 1.7112 | ±3.4224 | -0.867 | 0.3858 |  |
| Site: UW (vs UAB) | -0.8714 | 1.6655 | ±3.3310 | -0.523 | 0.6008 |  |
| **Age (years)** | **-0.2795** | 0.0754 | ±0.1509 | **-3.705** | **2.11e-04** | *** |
| BMI (kg/m2) | +0.1892 | 0.0978 | ±0.1956 | +1.935 | 0.0530 | . |
| Hypertension | +1.4889 | 1.5161 | ±3.0322 | +0.982 | 0.3261 |  |
| High cholesterol | +0.3747 | 1.2968 | ±2.5935 | +0.289 | 0.7726 |  |
| **Kidney disease** | **+6.7626** | 1.8534 | ±3.7067 | **+3.649** | **2.63e-04** | *** |
| Circulatory disease | -0.3299 | 1.8898 | ±3.7795 | -0.175 | 0.8614 |  |
| Time 181-250, pooled (%) | +0.0044 | 0.1429 | ±0.2859 | +0.031 | 0.9753 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2030**, F-statistic = **5.07** (p = **8.17e-07**), Residual SE = **8.050** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.5886** | 6.0044 | ±12.0088 | **+12.755** | **2.91e-37** | *** |
| **Education: graduate level (vs college)** | **-3.4516** | 1.4028 | ±2.8056 | **-2.461** | **0.0139** | * |
| **Education: high school or below (vs college)** | **-4.0169** | 2.0219 | ±4.0438 | **-1.987** | **0.0470** | * |
| Site: UCSD (vs UAB) | -1.4834 | 1.7105 | ±3.4211 | -0.867 | 0.3858 |  |
| Site: UW (vs UAB) | -0.8714 | 1.6618 | ±3.3235 | -0.524 | 0.6000 |  |
| **Age (years)** | **-0.2800** | 0.0754 | ±0.1509 | **-3.711** | **2.06e-04** | *** |
| BMI (kg/m2) | +0.1889 | 0.0976 | ±0.1952 | +1.935 | 0.0530 | . |
| Hypertension | +1.4824 | 1.5136 | ±3.0271 | +0.979 | 0.3274 |  |
| High cholesterol | +0.3786 | 1.2970 | ±2.5940 | +0.292 | 0.7704 |  |
| **Kidney disease** | **+6.7437** | 1.8566 | ±3.7131 | **+3.632** | **2.81e-04** | *** |
| Circulatory disease | -0.3436 | 1.8928 | ±3.7856 | -0.182 | 0.8560 |  |
| Avg. daily time 181-250 (%) | +0.0139 | 0.1473 | ±0.2946 | +0.094 | 0.9251 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2029**, F-statistic = **5.07** (p = **8.20e-07**), Residual SE = **8.051** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.5789** | 6.0043 | ±12.0086 | **+12.754** | **2.96e-37** | *** |
| **Education: graduate level (vs college)** | **-3.4482** | 1.4027 | ±2.8054 | **-2.458** | **0.0140** | * |
| **Education: high school or below (vs college)** | **-4.0140** | 2.0230 | ±4.0460 | **-1.984** | **0.0472** | * |
| Site: UCSD (vs UAB) | -1.4840 | 1.7112 | ±3.4224 | -0.867 | 0.3858 |  |
| Site: UW (vs UAB) | -0.8714 | 1.6655 | ±3.3310 | -0.523 | 0.6008 |  |
| **Age (years)** | **-0.2795** | 0.0754 | ±0.1509 | **-3.705** | **2.11e-04** | *** |
| BMI (kg/m2) | +0.1892 | 0.0978 | ±0.1956 | +1.935 | 0.0530 | . |
| Hypertension | +1.4889 | 1.5161 | ±3.0322 | +0.982 | 0.3261 |  |
| High cholesterol | +0.3747 | 1.2968 | ±2.5935 | +0.289 | 0.7726 |  |
| **Kidney disease** | **+6.7626** | 1.8534 | ±3.7067 | **+3.649** | **2.63e-04** | *** |
| Circulatory disease | -0.3299 | 1.8898 | ±3.7795 | -0.175 | 0.8614 |  |
| Time > 180 (%) | +0.0044 | 0.1429 | ±0.2859 | +0.031 | 0.9753 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **177**, R² = **0.2528**, Adj R² = **0.2030**, F-statistic = **5.07** (p = **8.17e-07**), Residual SE = **8.050** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.5886** | 6.0044 | ±12.0088 | **+12.755** | **2.91e-37** | *** |
| **Education: graduate level (vs college)** | **-3.4516** | 1.4028 | ±2.8056 | **-2.461** | **0.0139** | * |
| **Education: high school or below (vs college)** | **-4.0169** | 2.0219 | ±4.0438 | **-1.987** | **0.0470** | * |
| Site: UCSD (vs UAB) | -1.4834 | 1.7105 | ±3.4211 | -0.867 | 0.3858 |  |
| Site: UW (vs UAB) | -0.8714 | 1.6618 | ±3.3235 | -0.524 | 0.6000 |  |
| **Age (years)** | **-0.2800** | 0.0754 | ±0.1509 | **-3.711** | **2.06e-04** | *** |
| BMI (kg/m2) | +0.1889 | 0.0976 | ±0.1952 | +1.935 | 0.0530 | . |
| Hypertension | +1.4824 | 1.5136 | ±3.0271 | +0.979 | 0.3274 |  |
| High cholesterol | +0.3786 | 1.2970 | ±2.5940 | +0.292 | 0.7704 |  |
| **Kidney disease** | **+6.7437** | 1.8566 | ±3.7131 | **+3.632** | **2.81e-04** | *** |
| Circulatory disease | -0.3436 | 1.8928 | ±3.7856 | -0.182 | 0.8560 |  |
| Avg. daily time > 180 (%) | +0.0139 | 0.1473 | ±0.2946 | +0.094 | 0.9251 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 177)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **177**, R² = **0.2531**, Adj R² = **0.2033**, F-statistic = **5.08** (p = **7.96e-07**), Residual SE = **8.049** on **165** df, AIC = **1252.2**, BIC = **1290.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.4930** | 6.0317 | ±12.0633 | **+12.682** | **7.45e-37** | *** |
| **Education: graduate level (vs college)** | **-3.4380** | 1.3941 | ±2.7882 | **-2.466** | **0.0137** | * |
| **Education: high school or below (vs college)** | **-3.9545** | 2.0089 | ±4.0177 | **-1.969** | **0.0490** | * |
| Site: UCSD (vs UAB) | -1.5247 | 1.7155 | ±3.4309 | -0.889 | 0.3741 |  |
| Site: UW (vs UAB) | -0.9096 | 1.6512 | ±3.3025 | -0.551 | 0.5817 |  |
| **Age (years)** | **-0.2781** | 0.0755 | ±0.1510 | **-3.684** | **2.30e-04** | *** |
| BMI (kg/m2) | +0.1926 | 0.0991 | ±0.1981 | +1.945 | 0.0518 | . |
| Hypertension | +1.4685 | 1.5204 | ±3.0408 | +0.966 | 0.3341 |  |
| High cholesterol | +0.3709 | 1.2962 | ±2.5923 | +0.286 | 0.7748 |  |
| **Kidney disease** | **+6.8553** | 1.8806 | ±3.7613 | **+3.645** | **2.67e-04** | *** |
| Circulatory disease | -0.2620 | 1.9129 | ±3.8259 | -0.137 | 0.8911 |  |
| Nocturnal time > 180 (%) | -0.0338 | 0.1017 | ±0.2035 | -0.332 | 0.7397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 178; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **178**, R² = **0.1152**, Adj R² = **0.0623**, F-statistic = **2.18** (p = **0.0216**), Residual SE = **71.380** on **167** df, AIC = **2035.2**, BIC = **2070.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+366.0457** | 48.0780 | ±96.1560 | **+7.614** | **2.67e-14** | *** |
| Education: graduate level (vs college) | +17.1206 | 11.5506 | ±23.1013 | +1.482 | 0.1383 |  |
| Education: high school or below (vs college) | -2.1903 | 17.9742 | ±35.9485 | -0.122 | 0.9030 |  |
| **Site: UCSD (vs UAB)** | **-28.5363** | 13.8605 | ±27.7210 | **-2.059** | **0.0395** | * |
| Site: UW (vs UAB) | -5.0337 | 13.9517 | ±27.9033 | -0.361 | 0.7183 |  |
| Age (years) | +1.1124 | 0.6107 | ±1.2214 | +1.822 | 0.0685 | . |
| BMI (kg/m2) | -1.4447 | 0.7412 | ±1.4823 | -1.949 | 0.0513 | . |
| **Hypertension** | **-34.6500** | 13.5104 | ±27.0208 | **-2.565** | **0.0103** | * |
| High cholesterol | -3.5576 | 11.2899 | ±22.5798 | -0.315 | 0.7527 |  |
| Kidney disease | +1.6589 | 20.0899 | ±40.1797 | +0.083 | 0.9342 |  |
| Circulatory disease | -0.7041 | 14.1888 | ±28.3776 | -0.050 | 0.9604 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **178**, R² = **0.1170**, Adj R² = **0.0584**, F-statistic = **2.00** (p = **0.0314**), Residual SE = **71.525** on **166** df, AIC = **2036.9**, BIC = **2075.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.5859** | 72.7463 | ±145.4926 | **+5.479** | **4.27e-08** | *** |
| Education: graduate level (vs college) | +16.7821 | 11.7041 | ±23.4083 | +1.434 | 0.1516 |  |
| Education: high school or below (vs college) | -1.6868 | 18.1628 | ±36.3256 | -0.093 | 0.9260 |  |
| **Site: UCSD (vs UAB)** | **-28.5733** | 13.8728 | ±27.7456 | **-2.060** | **0.0394** | * |
| Site: UW (vs UAB) | -5.0585 | 14.0189 | ±28.0377 | -0.361 | 0.7182 |  |
| Age (years) | +1.1187 | 0.6154 | ±1.2308 | +1.818 | 0.0691 | . |
| BMI (kg/m2) | -1.3543 | 0.7420 | ±1.4840 | -1.825 | 0.0680 | . |
| **Hypertension** | **-33.8936** | 13.4774 | ±26.9548 | **-2.515** | **0.0119** | * |
| High cholesterol | -2.8135 | 11.5144 | ±23.0288 | -0.244 | 0.8070 |  |
| Kidney disease | +0.2389 | 20.1334 | ±40.2668 | +0.012 | 0.9905 |  |
| Circulatory disease | +0.2983 | 14.4453 | ±28.8906 | +0.021 | 0.9835 |  |
| HbA1c (%) | -6.1513 | 10.1664 | ±20.3329 | -0.605 | 0.5451 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **178**, R² = **0.1290**, Adj R² = **0.0713**, F-statistic = **2.23** (p = **0.0148**), Residual SE = **71.036** on **166** df, AIC = **2034.4**, BIC = **2072.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+445.6348** | 77.3786 | ±154.7572 | **+5.759** | **8.45e-09** | *** |
| Education: graduate level (vs college) | +16.6110 | 11.6067 | ±23.2133 | +1.431 | 0.1524 |  |
| Education: high school or below (vs college) | -3.8545 | 18.0396 | ±36.0792 | -0.214 | 0.8308 |  |
| **Site: UCSD (vs UAB)** | **-27.9128** | 13.7052 | ±27.4104 | **-2.037** | **0.0417** | * |
| Site: UW (vs UAB) | -4.5433 | 14.0077 | ±28.0155 | -0.324 | 0.7457 |  |
| Age (years) | +1.1161 | 0.6054 | ±1.2108 | +1.844 | 0.0652 | . |
| BMI (kg/m2) | -1.3194 | 0.7454 | ±1.4908 | -1.770 | 0.0767 | . |
| **Hypertension** | **-33.5783** | 13.0756 | ±26.1511 | **-2.568** | **0.0102** | * |
| High cholesterol | -3.8208 | 11.3663 | ±22.7325 | -0.336 | 0.7368 |  |
| Kidney disease | +5.1317 | 20.4478 | ±40.8956 | +0.251 | 0.8018 |  |
| Circulatory disease | +1.0676 | 14.4101 | ±28.8201 | +0.074 | 0.9409 |  |
| Mean glucose (mg/dL) | -0.6717 | 0.4969 | ±0.9938 | -1.352 | 0.1764 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **178**, R² = **0.1290**, Adj R² = **0.0713**, F-statistic = **2.23** (p = **0.0148**), Residual SE = **71.036** on **166** df, AIC = **2034.4**, BIC = **2072.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+538.5838** | 137.9447 | ±275.8894 | **+3.904** | **9.45e-05** | *** |
| Education: graduate level (vs college) | +16.6110 | 11.6067 | ±23.2133 | +1.431 | 0.1524 |  |
| Education: high school or below (vs college) | -3.8545 | 18.0396 | ±36.0792 | -0.214 | 0.8308 |  |
| **Site: UCSD (vs UAB)** | **-27.9128** | 13.7052 | ±27.4104 | **-2.037** | **0.0417** | * |
| Site: UW (vs UAB) | -4.5433 | 14.0077 | ±28.0155 | -0.324 | 0.7457 |  |
| Age (years) | +1.1161 | 0.6054 | ±1.2108 | +1.844 | 0.0652 | . |
| BMI (kg/m2) | -1.3194 | 0.7454 | ±1.4908 | -1.770 | 0.0767 | . |
| **Hypertension** | **-33.5783** | 13.0756 | ±26.1511 | **-2.568** | **0.0102** | * |
| High cholesterol | -3.8208 | 11.3663 | ±22.7325 | -0.336 | 0.7368 |  |
| Kidney disease | +5.1317 | 20.4478 | ±40.8956 | +0.251 | 0.8018 |  |
| Circulatory disease | +1.0676 | 14.4101 | ±28.8201 | +0.074 | 0.9409 |  |
| GMI (%) | -28.0813 | 20.7728 | ±41.5456 | -1.352 | 0.1764 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **178**, R² = **0.1258**, Adj R² = **0.0678**, F-statistic = **2.17** (p = **0.0182**), Residual SE = **71.168** on **166** df, AIC = **2035.1**, BIC = **2073.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+430.2091** | 75.4196 | ±150.8393 | **+5.704** | **1.17e-08** | *** |
| Education: graduate level (vs college) | +17.0670 | 11.5834 | ±23.1667 | +1.473 | 0.1406 |  |
| Education: high school or below (vs college) | -3.0559 | 17.9633 | ±35.9265 | -0.170 | 0.8649 |  |
| Site: UCSD (vs UAB) | -27.3152 | 13.9762 | ±27.9525 | -1.954 | 0.0507 | . |
| Site: UW (vs UAB) | -4.1620 | 13.9016 | ±27.8032 | -0.299 | 0.7646 |  |
| Age (years) | +1.0656 | 0.6052 | ±1.2103 | +1.761 | 0.0783 | . |
| BMI (kg/m2) | -1.3260 | 0.7471 | ±1.4941 | -1.775 | 0.0759 | . |
| **Hypertension** | **-33.6981** | 13.1356 | ±26.2712 | **-2.565** | **0.0103** | * |
| High cholesterol | -3.2666 | 11.3168 | ±22.6335 | -0.289 | 0.7728 |  |
| Kidney disease | +2.3340 | 20.4500 | ±40.9000 | +0.114 | 0.9091 |  |
| Circulatory disease | +1.5645 | 14.3407 | ±28.6814 | +0.109 | 0.9131 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.5295 | 0.4682 | ±0.9365 | -1.131 | 0.2581 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1215**, Adj R² = **0.0633**, F-statistic = **2.09** (p = **0.0238**), Residual SE = **71.340** on **166** df, AIC = **2035.9**, BIC = **2074.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+390.2629** | 54.6889 | ±109.3778 | **+7.136** | **9.60e-13** | *** |
| Education: graduate level (vs college) | +17.7717 | 11.4782 | ±22.9563 | +1.548 | 0.1215 |  |
| Education: high school or below (vs college) | +0.9422 | 18.1632 | ±36.3264 | +0.052 | 0.9586 |  |
| **Site: UCSD (vs UAB)** | **-29.3034** | 13.7049 | ±27.4097 | **-2.138** | **0.0325** | * |
| Site: UW (vs UAB) | -7.0434 | 14.3579 | ±28.7159 | -0.491 | 0.6237 |  |
| Age (years) | +1.1550 | 0.6305 | ±1.2609 | +1.832 | 0.0669 | . |
| BMI (kg/m2) | -1.4455 | 0.7397 | ±1.4794 | -1.954 | 0.0507 | . |
| **Hypertension** | **-32.2901** | 12.9291 | ±25.8582 | **-2.497** | **0.0125** | * |
| High cholesterol | -4.2295 | 11.3843 | ±22.7687 | -0.372 | 0.7102 |  |
| Kidney disease | +4.9138 | 20.0051 | ±40.0102 | +0.246 | 0.8060 |  |
| Circulatory disease | +0.6297 | 14.1839 | ±28.3678 | +0.044 | 0.9646 |  |
| Glucose SD, pooled (mg/dL) | -1.3059 | 1.4402 | ±2.8804 | -0.907 | 0.3645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1261**, Adj R² = **0.0682**, F-statistic = **2.18** (p = **0.0179**), Residual SE = **71.155** on **166** df, AIC = **2035.0**, BIC = **2073.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.7546** | 52.9981 | ±105.9961 | **+7.467** | **8.18e-14** | *** |
| Education: graduate level (vs college) | +17.9381 | 11.4614 | ±22.9229 | +1.565 | 0.1176 |  |
| Education: high school or below (vs college) | +0.9221 | 17.7289 | ±35.4578 | +0.052 | 0.9585 |  |
| **Site: UCSD (vs UAB)** | **-28.5918** | 13.7300 | ±27.4600 | **-2.082** | **0.0373** | * |
| Site: UW (vs UAB) | -6.6427 | 14.1446 | ±28.2891 | -0.470 | 0.6386 |  |
| Age (years) | +1.1709 | 0.6320 | ±1.2641 | +1.853 | 0.0639 | . |
| **BMI (kg/m2)** | **-1.4644** | 0.7368 | ±1.4736 | **-1.988** | **0.0469** | * |
| **Hypertension** | **-30.9404** | 12.8257 | ±25.6514 | **-2.412** | **0.0158** | * |
| High cholesterol | -4.6503 | 11.4146 | ±22.8293 | -0.407 | 0.6837 |  |
| Kidney disease | +5.0545 | 19.8336 | ±39.6671 | +0.255 | 0.7988 |  |
| Circulatory disease | +0.5784 | 14.1727 | ±28.3455 | +0.041 | 0.9674 |  |
| Avg. daily SD (mg/dL) | -1.7568 | 1.3722 | ±2.7444 | -1.280 | 0.2005 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **178**, R² = **0.1160**, Adj R² = **0.0575**, F-statistic = **1.98** (p = **0.0332**), Residual SE = **71.562** on **166** df, AIC = **2037.0**, BIC = **2075.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+376.8782** | 56.8539 | ±113.7079 | **+6.629** | **3.38e-11** | *** |
| Education: graduate level (vs college) | +17.4461 | 11.4541 | ±22.9082 | +1.523 | 0.1277 |  |
| Education: high school or below (vs college) | -0.5677 | 18.6057 | ±37.2114 | -0.031 | 0.9757 |  |
| **Site: UCSD (vs UAB)** | **-28.9558** | 13.7981 | ±27.5962 | **-2.099** | **0.0359** | * |
| Site: UW (vs UAB) | -5.9647 | 14.5028 | ±29.0056 | -0.411 | 0.6809 |  |
| Age (years) | +1.1308 | 0.6316 | ±1.2631 | +1.790 | 0.0734 | . |
| **BMI (kg/m2)** | **-1.4623** | 0.7430 | ±1.4859 | **-1.968** | **0.0490** | * |
| **Hypertension** | **-33.7977** | 13.2182 | ±26.4363 | **-2.557** | **0.0106** | * |
| High cholesterol | -3.7978 | 11.3781 | ±22.7562 | -0.334 | 0.7385 |  |
| Kidney disease | +2.5423 | 19.9342 | ±39.8684 | +0.128 | 0.8985 |  |
| Circulatory disease | -0.4352 | 14.2411 | ±28.4821 | -0.031 | 0.9756 |  |
| CV (%) | -0.6935 | 2.1160 | ±4.2319 | -0.328 | 0.7431 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **178**, R² = **0.1158**, Adj R² = **0.0572**, F-statistic = **1.98** (p = **0.0336**), Residual SE = **71.571** on **166** df, AIC = **2037.1**, BIC = **2075.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+355.1251** | 66.6714 | ±133.3429 | **+5.326** | **1.00e-07** | *** |
| Education: graduate level (vs college) | +17.3172 | 11.5148 | ±23.0296 | +1.504 | 0.1326 |  |
| Education: high school or below (vs college) | -0.9803 | 18.3976 | ±36.7951 | -0.053 | 0.9575 |  |
| **Site: UCSD (vs UAB)** | **-28.7686** | 13.8052 | ±27.6104 | **-2.084** | **0.0372** | * |
| Site: UW (vs UAB) | -5.7562 | 14.5244 | ±29.0488 | -0.396 | 0.6919 |  |
| Age (years) | +1.1300 | 0.6409 | ±1.2818 | +1.763 | 0.0779 | . |
| BMI (kg/m2) | -1.4473 | 0.7438 | ±1.4876 | -1.946 | 0.0517 | . |
| **Hypertension** | **-33.8846** | 13.1456 | ±26.2911 | **-2.578** | **0.0099** | ** |
| High cholesterol | -3.6528 | 11.4103 | ±22.8206 | -0.320 | 0.7489 |  |
| Kidney disease | +2.3604 | 19.8900 | ±39.7800 | +0.119 | 0.9055 |  |
| Circulatory disease | -0.5590 | 14.2806 | ±28.5613 | -0.039 | 0.9688 |  |
| Mean / SD ratio | +1.5551 | 5.8688 | ±11.7376 | +0.265 | 0.7910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **178**, R² = **0.1189**, Adj R² = **0.0605**, F-statistic = **2.04** (p = **0.0279**), Residual SE = **71.446** on **166** df, AIC = **2036.5**, BIC = **2074.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+341.1126** | 62.5984 | ±125.1968 | **+5.449** | **5.06e-08** | *** |
| Education: graduate level (vs college) | +17.4570 | 11.5531 | ±23.1062 | +1.511 | 0.1308 |  |
| Education: high school or below (vs college) | +0.0293 | 17.9051 | ±35.8101 | +0.002 | 0.9987 |  |
| **Site: UCSD (vs UAB)** | **-28.2864** | 13.9358 | ±27.8716 | **-2.030** | **0.0424** | * |
| Site: UW (vs UAB) | -6.2538 | 14.2199 | ±28.4399 | -0.440 | 0.6601 |  |
| Age (years) | +1.1645 | 0.6452 | ±1.2904 | +1.805 | 0.0711 | . |
| **BMI (kg/m2)** | **-1.4544** | 0.7362 | ±1.4725 | **-1.975** | **0.0482** | * |
| **Hypertension** | **-32.3516** | 13.1848 | ±26.3695 | **-2.454** | **0.0141** | * |
| High cholesterol | -3.6907 | 11.3909 | ±22.7818 | -0.324 | 0.7459 |  |
| Kidney disease | +2.9167 | 19.8414 | ±39.6828 | +0.147 | 0.8831 |  |
| Circulatory disease | -0.8311 | 14.1872 | ±28.3744 | -0.059 | 0.9533 |  |
| Avg. daily mean/SD | +2.9707 | 4.0230 | ±8.0460 | +0.738 | 0.4603 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **178**, R² = **0.1494**, Adj R² = **0.0930**, F-statistic = **2.65** (p = **0.0038**), Residual SE = **70.201** on **166** df, AIC = **2030.2**, BIC = **2068.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+432.1665** | 50.7666 | ±101.5331 | **+8.513** | **1.70e-17** | *** |
| Education: graduate level (vs college) | +17.9629 | 11.3525 | ±22.7050 | +1.582 | 0.1136 |  |
| Education: high school or below (vs college) | +1.9592 | 16.9729 | ±33.9459 | +0.115 | 0.9081 |  |
| **Site: UCSD (vs UAB)** | **-27.6463** | 13.5458 | ±27.0916 | **-2.041** | **0.0413** | * |
| Site: UW (vs UAB) | -6.8337 | 13.5464 | ±27.0928 | -0.504 | 0.6139 |  |
| Age (years) | +1.1454 | 0.6129 | ±1.2259 | +1.869 | 0.0617 | . |
| BMI (kg/m2) | -1.2926 | 0.7591 | ±1.5181 | -1.703 | 0.0886 | . |
| **Hypertension** | **-33.0148** | 12.9251 | ±25.8501 | **-2.554** | **0.0106** | * |
| High cholesterol | -2.4377 | 11.1407 | ±22.2815 | -0.219 | 0.8268 |  |
| Kidney disease | +0.7746 | 20.1008 | ±40.2015 | +0.039 | 0.9693 |  |
| Circulatory disease | -1.1343 | 14.1218 | ±28.2436 | -0.080 | 0.9360 |  |
| **MAG (mg/dL/h)** | **-2.0728** | 0.7655 | ±1.5310 | **-2.708** | **0.0068** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **178**, R² = **0.1204**, Adj R² = **0.0621**, F-statistic = **2.07** (p = **0.0255**), Residual SE = **71.387** on **166** df, AIC = **2036.2**, BIC = **2074.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.2750** | 57.2250 | ±114.4500 | **+6.855** | **7.13e-12** | *** |
| Education: graduate level (vs college) | +17.3832 | 11.5446 | ±23.0893 | +1.506 | 0.1321 |  |
| Education: high school or below (vs college) | -0.3645 | 17.7576 | ±35.5152 | -0.021 | 0.9836 |  |
| **Site: UCSD (vs UAB)** | **-28.9939** | 13.8008 | ±27.6015 | **-2.101** | **0.0357** | * |
| Site: UW (vs UAB) | -6.3804 | 14.2933 | ±28.5866 | -0.446 | 0.6553 |  |
| Age (years) | +1.1625 | 0.6355 | ±1.2709 | +1.829 | 0.0674 | . |
| **BMI (kg/m2)** | **-1.4888** | 0.7481 | ±1.4963 | **-1.990** | **0.0466** | * |
| **Hypertension** | **-32.8961** | 12.9212 | ±25.8425 | **-2.546** | **0.0109** | * |
| High cholesterol | -4.0519 | 11.4389 | ±22.8778 | -0.354 | 0.7232 |  |
| Kidney disease | +3.2055 | 19.8346 | ±39.6691 | +0.162 | 0.8716 |  |
| Circulatory disease | +0.0068 | 14.3282 | ±28.6563 | +0.000 | 0.9996 |  |
| Avg. daily range (mg/dL) | -0.2984 | 0.3462 | ±0.6924 | -0.862 | 0.3887 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **178**, R² = **0.1155**, Adj R² = **0.0569**, F-statistic = **1.97** (p = **0.0343**), Residual SE = **71.585** on **166** df, AIC = **2037.2**, BIC = **2075.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+363.7480** | 48.7389 | ±97.4779 | **+7.463** | **8.45e-14** | *** |
| Education: graduate level (vs college) | +17.0432 | 11.5485 | ±23.0971 | +1.476 | 0.1400 |  |
| Education: high school or below (vs college) | -2.9511 | 18.9958 | ±37.9915 | -0.155 | 0.8765 |  |
| **Site: UCSD (vs UAB)** | **-28.0811** | 13.8579 | ±27.7157 | **-2.026** | **0.0427** | * |
| Site: UW (vs UAB) | -4.4668 | 14.2415 | ±28.4830 | -0.314 | 0.7538 |  |
| Age (years) | +1.1034 | 0.6248 | ±1.2497 | +1.766 | 0.0774 | . |
| BMI (kg/m2) | -1.4516 | 0.7532 | ±1.5065 | -1.927 | 0.0540 | . |
| **Hypertension** | **-34.5342** | 13.7558 | ±27.5117 | **-2.511** | **0.0121** | * |
| High cholesterol | -3.6750 | 11.4672 | ±22.9345 | -0.320 | 0.7486 |  |
| Kidney disease | +1.0179 | 20.1165 | ±40.2329 | +0.051 | 0.9596 |  |
| Circulatory disease | -1.2164 | 14.5812 | ±29.1624 | -0.083 | 0.9335 |  |
| SD of daily means (mg/dL) | +0.4611 | 2.4929 | ±4.9859 | +0.185 | 0.8533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **178**, R² = **0.1158**, Adj R² = **0.0572**, F-statistic = **1.98** (p = **0.0336**), Residual SE = **71.572** on **166** df, AIC = **2037.1**, BIC = **2075.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+327.9608** | 122.5213 | ±245.0426 | **+2.677** | **0.0074** | ** |
| Education: graduate level (vs college) | +17.3754 | 11.6048 | ±23.2096 | +1.497 | 0.1343 |  |
| Education: high school or below (vs college) | -1.8385 | 18.0945 | ±36.1890 | -0.102 | 0.9191 |  |
| **Site: UCSD (vs UAB)** | **-28.7101** | 13.8294 | ±27.6589 | **-2.076** | **0.0379** | * |
| Site: UW (vs UAB) | -5.1799 | 14.0339 | ±28.0678 | -0.369 | 0.7121 |  |
| Age (years) | +1.1323 | 0.6219 | ±1.2438 | +1.821 | 0.0687 | . |
| BMI (kg/m2) | -1.4270 | 0.7403 | ±1.4806 | -1.928 | 0.0539 | . |
| **Hypertension** | **-34.4474** | 13.4871 | ±26.9741 | **-2.554** | **0.0106** | * |
| High cholesterol | -3.7742 | 11.3586 | ±22.7172 | -0.332 | 0.7397 |  |
| Kidney disease | +2.7730 | 20.7061 | ±41.4122 | +0.134 | 0.8935 |  |
| Circulatory disease | -0.2710 | 14.2553 | ±28.5106 | -0.019 | 0.9848 |  |
| Time in range 70-180, pooled (%) | +0.3759 | 1.1410 | ±2.2820 | +0.329 | 0.7418 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **178**, R² = **0.1161**, Adj R² = **0.0575**, F-statistic = **1.98** (p = **0.0331**), Residual SE = **71.561** on **166** df, AIC = **2037.0**, BIC = **2075.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+318.4931** | 122.8436 | ±245.6873 | **+2.593** | **0.0095** | ** |
| Education: graduate level (vs college) | +17.4020 | 11.5996 | ±23.1992 | +1.500 | 0.1336 |  |
| Education: high school or below (vs college) | -1.8579 | 18.0571 | ±36.1141 | -0.103 | 0.9180 |  |
| **Site: UCSD (vs UAB)** | **-28.7514** | 13.8178 | ±27.6357 | **-2.081** | **0.0375** | * |
| Site: UW (vs UAB) | -5.1153 | 14.0357 | ±28.0715 | -0.364 | 0.7155 |  |
| Age (years) | +1.1378 | 0.6218 | ±1.2436 | +1.830 | 0.0673 | . |
| BMI (kg/m2) | -1.4265 | 0.7412 | ±1.4824 | -1.925 | 0.0543 | . |
| **Hypertension** | **-34.3363** | 13.4705 | ±26.9411 | **-2.549** | **0.0108** | * |
| High cholesterol | -3.8331 | 11.3632 | ±22.7264 | -0.337 | 0.7359 |  |
| Kidney disease | +3.0725 | 20.7463 | ±41.4926 | +0.148 | 0.8823 |  |
| Circulatory disease | -0.1496 | 14.2614 | ±28.5228 | -0.010 | 0.9916 |  |
| Avg. daily time in range 70-180 (%) | +0.4692 | 1.1432 | ±2.2864 | +0.410 | 0.6815 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **178**, R² = **0.1227**, Adj R² = **0.0646**, F-statistic = **2.11** (p = **0.0221**), Residual SE = **71.292** on **166** df, AIC = **2035.7**, BIC = **2073.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+370.2083** | 48.3286 | ±96.6571 | **+7.660** | **1.86e-14** | *** |
| Education: graduate level (vs college) | +15.6591 | 11.5341 | ±23.0682 | +1.358 | 0.1746 |  |
| Education: high school or below (vs college) | -5.2673 | 18.3978 | ±36.7956 | -0.286 | 0.7746 |  |
| **Site: UCSD (vs UAB)** | **-27.9331** | 13.8766 | ±27.7532 | **-2.013** | **0.0441** | * |
| Site: UW (vs UAB) | -4.6883 | 13.8254 | ±27.6508 | -0.339 | 0.7345 |  |
| Age (years) | +1.0057 | 0.6240 | ±1.2481 | +1.612 | 0.1071 |  |
| BMI (kg/m2) | -1.4147 | 0.7396 | ±1.4792 | -1.913 | 0.0558 | . |
| **Hypertension** | **-34.8756** | 13.6787 | ±27.3575 | **-2.550** | **0.0108** | * |
| High cholesterol | -4.6687 | 11.1806 | ±22.3611 | -0.418 | 0.6763 |  |
| Kidney disease | +2.9659 | 20.1668 | ±40.3337 | +0.147 | 0.8831 |  |
| Circulatory disease | -1.7661 | 14.7569 | ±29.5138 | -0.120 | 0.9047 |  |
| Time 54-69, pooled (%) | +21.4511 | 24.6594 | ±49.3189 | +0.870 | 0.3844 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **178**, R² = **0.1207**, Adj R² = **0.0624**, F-statistic = **2.07** (p = **0.0250**), Residual SE = **71.374** on **166** df, AIC = **2036.1**, BIC = **2074.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+370.3134** | 48.6127 | ±97.2255 | **+7.618** | **2.58e-14** | *** |
| Education: graduate level (vs college) | +15.9612 | 11.5192 | ±23.0384 | +1.386 | 0.1659 |  |
| Education: high school or below (vs college) | -4.5048 | 18.2855 | ±36.5711 | -0.246 | 0.8054 |  |
| **Site: UCSD (vs UAB)** | **-28.5451** | 13.8944 | ±27.7889 | **-2.054** | **0.0399** | * |
| Site: UW (vs UAB) | -5.0863 | 13.9220 | ±27.8440 | -0.365 | 0.7149 |  |
| Age (years) | +1.0165 | 0.6264 | ±1.2528 | +1.623 | 0.1046 |  |
| BMI (kg/m2) | -1.4172 | 0.7394 | ±1.4789 | -1.917 | 0.0553 | . |
| **Hypertension** | **-35.0308** | 13.7929 | ±27.5858 | **-2.540** | **0.0111** | * |
| High cholesterol | -4.4736 | 11.1962 | ±22.3924 | -0.400 | 0.6895 |  |
| Kidney disease | +3.1571 | 20.2423 | ±40.4847 | +0.156 | 0.8761 |  |
| Circulatory disease | -1.3324 | 14.9062 | ±29.8124 | -0.089 | 0.9288 |  |
| Avg. daily time 54-69 (%) | +17.5579 | 25.0491 | ±50.0983 | +0.701 | 0.4833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **178**, R² = **0.1227**, Adj R² = **0.0646**, F-statistic = **2.11** (p = **0.0221**), Residual SE = **71.292** on **166** df, AIC = **2035.7**, BIC = **2073.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+370.2083** | 48.3286 | ±96.6571 | **+7.660** | **1.86e-14** | *** |
| Education: graduate level (vs college) | +15.6591 | 11.5341 | ±23.0682 | +1.358 | 0.1746 |  |
| Education: high school or below (vs college) | -5.2673 | 18.3978 | ±36.7956 | -0.286 | 0.7746 |  |
| **Site: UCSD (vs UAB)** | **-27.9331** | 13.8766 | ±27.7532 | **-2.013** | **0.0441** | * |
| Site: UW (vs UAB) | -4.6883 | 13.8254 | ±27.6508 | -0.339 | 0.7345 |  |
| Age (years) | +1.0057 | 0.6240 | ±1.2481 | +1.612 | 0.1071 |  |
| BMI (kg/m2) | -1.4147 | 0.7396 | ±1.4792 | -1.913 | 0.0558 | . |
| **Hypertension** | **-34.8756** | 13.6787 | ±27.3575 | **-2.550** | **0.0108** | * |
| High cholesterol | -4.6687 | 11.1806 | ±22.3611 | -0.418 | 0.6763 |  |
| Kidney disease | +2.9659 | 20.1668 | ±40.3337 | +0.147 | 0.8831 |  |
| Circulatory disease | -1.7661 | 14.7569 | ±29.5138 | -0.120 | 0.9047 |  |
| Time < 70 (%) | +21.4511 | 24.6594 | ±49.3189 | +0.870 | 0.3844 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **178**, R² = **0.1207**, Adj R² = **0.0624**, F-statistic = **2.07** (p = **0.0250**), Residual SE = **71.374** on **166** df, AIC = **2036.1**, BIC = **2074.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+370.3134** | 48.6127 | ±97.2255 | **+7.618** | **2.58e-14** | *** |
| Education: graduate level (vs college) | +15.9612 | 11.5192 | ±23.0384 | +1.386 | 0.1659 |  |
| Education: high school or below (vs college) | -4.5048 | 18.2855 | ±36.5711 | -0.246 | 0.8054 |  |
| **Site: UCSD (vs UAB)** | **-28.5451** | 13.8944 | ±27.7889 | **-2.054** | **0.0399** | * |
| Site: UW (vs UAB) | -5.0863 | 13.9220 | ±27.8440 | -0.365 | 0.7149 |  |
| Age (years) | +1.0165 | 0.6264 | ±1.2528 | +1.623 | 0.1046 |  |
| BMI (kg/m2) | -1.4172 | 0.7394 | ±1.4789 | -1.917 | 0.0553 | . |
| **Hypertension** | **-35.0308** | 13.7929 | ±27.5858 | **-2.540** | **0.0111** | * |
| High cholesterol | -4.4736 | 11.1962 | ±22.3924 | -0.400 | 0.6895 |  |
| Kidney disease | +3.1571 | 20.2423 | ±40.4847 | +0.156 | 0.8761 |  |
| Circulatory disease | -1.3324 | 14.9062 | ±29.8124 | -0.089 | 0.9288 |  |
| Avg. daily time < 70 (%) | +17.5579 | 25.0491 | ±50.0983 | +0.701 | 0.4833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **178**, R² = **0.1161**, Adj R² = **0.0575**, F-statistic = **1.98** (p = **0.0331**), Residual SE = **71.561** on **166** df, AIC = **2037.0**, BIC = **2075.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+365.5325** | 48.4092 | ±96.8183 | **+7.551** | **4.32e-14** | *** |
| Education: graduate level (vs college) | +17.3985 | 11.6043 | ±23.2087 | +1.499 | 0.1338 |  |
| Education: high school or below (vs college) | -1.8290 | 18.0824 | ±36.1648 | -0.101 | 0.9194 |  |
| **Site: UCSD (vs UAB)** | **-28.7343** | 13.8310 | ±27.6621 | **-2.078** | **0.0378** | * |
| Site: UW (vs UAB) | -5.2037 | 14.0340 | ±28.0681 | -0.371 | 0.7108 |  |
| Age (years) | +1.1343 | 0.6209 | ±1.2418 | +1.827 | 0.0677 | . |
| BMI (kg/m2) | -1.4226 | 0.7404 | ±1.4808 | -1.921 | 0.0547 | . |
| **Hypertension** | **-34.4090** | 13.4785 | ±26.9571 | **-2.553** | **0.0107** | * |
| High cholesterol | -3.8440 | 11.3562 | ±22.7124 | -0.338 | 0.7350 |  |
| Kidney disease | +3.0381 | 20.7105 | ±41.4210 | +0.147 | 0.8834 |  |
| Circulatory disease | -0.2014 | 14.2800 | ±28.5599 | -0.014 | 0.9887 |  |
| Time 181-250, pooled (%) | -0.4559 | 1.1339 | ±2.2677 | -0.402 | 0.6876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **178**, R² = **0.1164**, Adj R² = **0.0578**, F-statistic = **1.99** (p = **0.0325**), Residual SE = **71.549** on **166** df, AIC = **2037.0**, BIC = **2075.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+365.4463** | 48.3957 | ±96.7913 | **+7.551** | **4.31e-14** | *** |
| Education: graduate level (vs college) | +17.4085 | 11.6013 | ±23.2026 | +1.501 | 0.1335 |  |
| Education: high school or below (vs college) | -1.8793 | 18.0522 | ±36.1043 | -0.104 | 0.9171 |  |
| **Site: UCSD (vs UAB)** | **-28.7838** | 13.8165 | ±27.6330 | **-2.083** | **0.0372** | * |
| Site: UW (vs UAB) | -5.1291 | 14.0352 | ±28.0705 | -0.365 | 0.7148 |  |
| Age (years) | +1.1387 | 0.6205 | ±1.2410 | +1.835 | 0.0665 | . |
| BMI (kg/m2) | -1.4230 | 0.7411 | ±1.4821 | -1.920 | 0.0548 | . |
| **Hypertension** | **-34.3011** | 13.4604 | ±26.9208 | **-2.548** | **0.0108** | * |
| High cholesterol | -3.9024 | 11.3601 | ±22.7202 | -0.344 | 0.7312 |  |
| Kidney disease | +3.3299 | 20.7487 | ±41.4973 | +0.160 | 0.8725 |  |
| Circulatory disease | -0.0860 | 14.2902 | ±28.5803 | -0.006 | 0.9952 |  |
| Avg. daily time 181-250 (%) | -0.5393 | 1.1405 | ±2.2810 | -0.473 | 0.6363 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **178**, R² = **0.1161**, Adj R² = **0.0575**, F-statistic = **1.98** (p = **0.0331**), Residual SE = **71.561** on **166** df, AIC = **2037.0**, BIC = **2075.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+365.5325** | 48.4092 | ±96.8183 | **+7.551** | **4.32e-14** | *** |
| Education: graduate level (vs college) | +17.3985 | 11.6043 | ±23.2087 | +1.499 | 0.1338 |  |
| Education: high school or below (vs college) | -1.8290 | 18.0824 | ±36.1648 | -0.101 | 0.9194 |  |
| **Site: UCSD (vs UAB)** | **-28.7343** | 13.8310 | ±27.6621 | **-2.078** | **0.0378** | * |
| Site: UW (vs UAB) | -5.2037 | 14.0340 | ±28.0681 | -0.371 | 0.7108 |  |
| Age (years) | +1.1343 | 0.6209 | ±1.2418 | +1.827 | 0.0677 | . |
| BMI (kg/m2) | -1.4226 | 0.7404 | ±1.4808 | -1.921 | 0.0547 | . |
| **Hypertension** | **-34.4090** | 13.4785 | ±26.9571 | **-2.553** | **0.0107** | * |
| High cholesterol | -3.8440 | 11.3562 | ±22.7124 | -0.338 | 0.7350 |  |
| Kidney disease | +3.0381 | 20.7105 | ±41.4210 | +0.147 | 0.8834 |  |
| Circulatory disease | -0.2014 | 14.2800 | ±28.5599 | -0.014 | 0.9887 |  |
| Time > 180 (%) | -0.4559 | 1.1339 | ±2.2677 | -0.402 | 0.6876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **178**, R² = **0.1164**, Adj R² = **0.0578**, F-statistic = **1.99** (p = **0.0325**), Residual SE = **71.549** on **166** df, AIC = **2037.0**, BIC = **2075.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+365.4463** | 48.3957 | ±96.7913 | **+7.551** | **4.31e-14** | *** |
| Education: graduate level (vs college) | +17.4085 | 11.6013 | ±23.2026 | +1.501 | 0.1335 |  |
| Education: high school or below (vs college) | -1.8793 | 18.0522 | ±36.1043 | -0.104 | 0.9171 |  |
| **Site: UCSD (vs UAB)** | **-28.7838** | 13.8165 | ±27.6330 | **-2.083** | **0.0372** | * |
| Site: UW (vs UAB) | -5.1291 | 14.0352 | ±28.0705 | -0.365 | 0.7148 |  |
| Age (years) | +1.1387 | 0.6205 | ±1.2410 | +1.835 | 0.0665 | . |
| BMI (kg/m2) | -1.4230 | 0.7411 | ±1.4821 | -1.920 | 0.0548 | . |
| **Hypertension** | **-34.3011** | 13.4604 | ±26.9208 | **-2.548** | **0.0108** | * |
| High cholesterol | -3.9024 | 11.3601 | ±22.7202 | -0.344 | 0.7312 |  |
| Kidney disease | +3.3299 | 20.7487 | ±41.4973 | +0.160 | 0.8725 |  |
| Circulatory disease | -0.0860 | 14.2902 | ±28.5803 | -0.006 | 0.9952 |  |
| Avg. daily time > 180 (%) | -0.5393 | 1.1405 | ±2.2810 | -0.473 | 0.6363 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 178)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **178**, R² = **0.1165**, Adj R² = **0.0579**, F-statistic = **1.99** (p = **0.0323**), Residual SE = **71.544** on **166** df, AIC = **2036.9**, BIC = **2075.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+367.5027** | 47.9618 | ±95.9236 | **+7.662** | **1.82e-14** | *** |
| Education: graduate level (vs college) | +17.0125 | 11.6310 | ±23.2620 | +1.463 | 0.1436 |  |
| Education: high school or below (vs college) | -3.1627 | 19.0072 | ±38.0144 | -0.166 | 0.8678 |  |
| **Site: UCSD (vs UAB)** | **-27.8724** | 13.7824 | ±27.5648 | **-2.022** | **0.0431** | * |
| Site: UW (vs UAB) | -4.4741 | 14.1277 | ±28.2555 | -0.317 | 0.7515 |  |
| Age (years) | +1.0921 | 0.6134 | ±1.2269 | +1.780 | 0.0750 | . |
| **BMI (kg/m2)** | **-1.4994** | 0.7362 | ±1.4724 | **-2.037** | **0.0417** | * |
| **Hypertension** | **-34.3532** | 13.6831 | ±27.3662 | **-2.511** | **0.0121** | * |
| High cholesterol | -3.5182 | 11.3598 | ±22.7196 | -0.310 | 0.7568 |  |
| Kidney disease | +0.0266 | 20.2930 | ±40.5859 | +0.001 | 0.9990 |  |
| Circulatory disease | -1.6060 | 14.2416 | ±28.4833 | -0.113 | 0.9102 |  |
| Nocturnal time > 180 (%) | +0.5457 | 1.6657 | ±3.3314 | +0.328 | 0.7432 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 177; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **177**, R² = **0.2618**, Adj R² = **0.2173**, F-statistic = **5.89** (p = **1.37e-07**), Residual SE = **17.041** on **166** df, AIC = **1516.8**, BIC = **1551.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.8966** | 11.2249 | ±22.4497 | **+7.296** | **2.96e-13** | *** |
| **Education: graduate level (vs college)** | **-11.4577** | 2.9128 | ±5.8256 | **-3.934** | **8.37e-05** | *** |
| **Education: high school or below (vs college)** | **-8.8835** | 4.1657 | ±8.3315 | **-2.133** | **0.0330** | * |
| Site: UCSD (vs UAB) | +5.2193 | 3.5231 | ±7.0461 | +1.481 | 0.1385 |  |
| Site: UW (vs UAB) | +2.3350 | 3.3520 | ±6.7040 | +0.697 | 0.4861 |  |
| **Age (years)** | **-0.6347** | 0.1392 | ±0.2784 | **-4.559** | **5.13e-06** | *** |
| **BMI (kg/m2)** | **+0.3868** | 0.1921 | ±0.3841 | **+2.014** | **0.0441** | * |
| Hypertension | +2.4090 | 3.3493 | ±6.6986 | +0.719 | 0.4720 |  |
| High cholesterol | +0.8607 | 2.6988 | ±5.3975 | +0.319 | 0.7498 |  |
| **Kidney disease** | **+12.7271** | 3.6397 | ±7.2794 | **+3.497** | **4.71e-04** | *** |
| Circulatory disease | -2.1897 | 3.6840 | ±7.3681 | -0.594 | 0.5523 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **177**, R² = **0.2619**, Adj R² = **0.2126**, F-statistic = **5.32** (p = **3.47e-07**), Residual SE = **17.092** on **165** df, AIC = **1518.7**, BIC = **1556.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+83.4101** | 17.6539 | ±35.3078 | **+4.725** | **2.30e-06** | *** |
| **Education: graduate level (vs college)** | **-11.4709** | 2.9339 | ±5.8678 | **-3.910** | **9.24e-05** | *** |
| **Education: high school or below (vs college)** | **-8.8668** | 4.1742 | ±8.3484 | **-2.124** | **0.0337** | * |
| Site: UCSD (vs UAB) | +5.2185 | 3.5407 | ±7.0813 | +1.474 | 0.1405 |  |
| Site: UW (vs UAB) | +2.3289 | 3.3740 | ±6.7481 | +0.690 | 0.4900 |  |
| **Age (years)** | **-0.6345** | 0.1402 | ±0.2804 | **-4.526** | **6.01e-06** | *** |
| **BMI (kg/m2)** | **+0.3906** | 0.1973 | ±0.3946 | **+1.980** | **0.0477** | * |
| Hypertension | +2.4370 | 3.3632 | ±6.7264 | +0.725 | 0.4687 |  |
| High cholesterol | +0.8969 | 2.7502 | ±5.5004 | +0.326 | 0.7443 |  |
| **Kidney disease** | **+12.6684** | 3.6948 | ±7.3897 | **+3.429** | **6.07e-04** | *** |
| Circulatory disease | -2.1374 | 3.7103 | ±7.4205 | -0.576 | 0.5646 |  |
| HbA1c (%) | -0.2822 | 2.6315 | ±5.2630 | -0.107 | 0.9146 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **177**, R² = **0.2621**, Adj R² = **0.2129**, F-statistic = **5.33** (p = **3.41e-07**), Residual SE = **17.090** on **165** df, AIC = **1518.7**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.0038** | 16.1176 | ±32.2353 | **+4.902** | **9.50e-07** | *** |
| **Education: graduate level (vs college)** | **-11.4320** | 2.9338 | ±5.8675 | **-3.897** | **9.75e-05** | *** |
| **Education: high school or below (vs college)** | **-8.8111** | 4.2332 | ±8.4664 | **-2.081** | **0.0374** | * |
| Site: UCSD (vs UAB) | +5.1723 | 3.5382 | ±7.0763 | +1.462 | 0.1438 |  |
| Site: UW (vs UAB) | +2.3168 | 3.3725 | ±6.7451 | +0.687 | 0.4921 |  |
| **Age (years)** | **-0.6342** | 0.1397 | ±0.2794 | **-4.540** | **5.63e-06** | *** |
| **BMI (kg/m2)** | **+0.3832** | 0.1940 | ±0.3880 | **+1.975** | **0.0482** | * |
| Hypertension | +2.3695 | 3.3604 | ±6.7209 | +0.705 | 0.4807 |  |
| High cholesterol | +0.8585 | 2.7155 | ±5.4310 | +0.316 | 0.7519 |  |
| **Kidney disease** | **+12.6517** | 3.6732 | ±7.3464 | **+3.444** | **5.72e-04** | *** |
| Circulatory disease | -2.2631 | 3.6896 | ±7.3792 | -0.613 | 0.5396 |  |
| Mean glucose (mg/dL) | +0.0239 | 0.0988 | ±0.1976 | +0.242 | 0.8085 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **177**, R² = **0.2621**, Adj R² = **0.2129**, F-statistic = **5.33** (p = **3.41e-07**), Residual SE = **17.090** on **165** df, AIC = **1518.7**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.6907** | 27.5878 | ±55.1755 | **+2.744** | **0.0061** | ** |
| **Education: graduate level (vs college)** | **-11.4320** | 2.9338 | ±5.8675 | **-3.897** | **9.75e-05** | *** |
| **Education: high school or below (vs college)** | **-8.8111** | 4.2332 | ±8.4664 | **-2.081** | **0.0374** | * |
| Site: UCSD (vs UAB) | +5.1723 | 3.5382 | ±7.0763 | +1.462 | 0.1438 |  |
| Site: UW (vs UAB) | +2.3168 | 3.3725 | ±6.7451 | +0.687 | 0.4921 |  |
| **Age (years)** | **-0.6342** | 0.1397 | ±0.2794 | **-4.540** | **5.63e-06** | *** |
| **BMI (kg/m2)** | **+0.3832** | 0.1940 | ±0.3880 | **+1.975** | **0.0482** | * |
| Hypertension | +2.3695 | 3.3604 | ±6.7209 | +0.705 | 0.4807 |  |
| High cholesterol | +0.8585 | 2.7155 | ±5.4310 | +0.316 | 0.7519 |  |
| **Kidney disease** | **+12.6517** | 3.6732 | ±7.3464 | **+3.444** | **5.72e-04** | *** |
| Circulatory disease | -2.2631 | 3.6896 | ±7.3792 | -0.613 | 0.5396 |  |
| GMI (%) | +1.0009 | 4.1301 | ±8.2603 | +0.242 | 0.8085 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **177**, R² = **0.2618**, Adj R² = **0.2126**, F-statistic = **5.32** (p = **3.49e-07**), Residual SE = **17.093** on **165** df, AIC = **1518.8**, BIC = **1556.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.9498** | 15.0413 | ±30.0827 | **+5.448** | **5.09e-08** | *** |
| **Education: graduate level (vs college)** | **-11.4578** | 2.9281 | ±5.8561 | **-3.913** | **9.11e-05** | *** |
| **Education: high school or below (vs college)** | **-8.8844** | 4.1966 | ±8.3932 | **-2.117** | **0.0343** | * |
| Site: UCSD (vs UAB) | +5.2205 | 3.5325 | ±7.0651 | +1.478 | 0.1394 |  |
| Site: UW (vs UAB) | +2.3356 | 3.3654 | ±6.7308 | +0.694 | 0.4877 |  |
| **Age (years)** | **-0.6347** | 0.1397 | ±0.2793 | **-4.545** | **5.49e-06** | *** |
| **BMI (kg/m2)** | **+0.3868** | 0.1947 | ±0.3895 | **+1.987** | **0.0470** | * |
| Hypertension | +2.4098 | 3.3637 | ±6.7274 | +0.716 | 0.4737 |  |
| High cholesterol | +0.8610 | 2.7151 | ±5.4301 | +0.317 | 0.7511 |  |
| **Kidney disease** | **+12.7269** | 3.6609 | ±7.3219 | **+3.476** | **5.08e-04** | *** |
| Circulatory disease | -2.1877 | 3.7050 | ±7.4100 | -0.590 | 0.5549 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0004 | 0.0884 | ±0.1767 | -0.005 | 0.9961 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **177**, R² = **0.2620**, Adj R² = **0.2128**, F-statistic = **5.32** (p = **3.44e-07**), Residual SE = **17.091** on **165** df, AIC = **1518.7**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+82.9550** | 12.1483 | ±24.2966 | **+6.829** | **8.58e-12** | *** |
| **Education: graduate level (vs college)** | **-11.4314** | 2.9128 | ±5.8257 | **-3.924** | **8.69e-05** | *** |
| **Education: high school or below (vs college)** | **-8.7575** | 4.2302 | ±8.4604 | **-2.070** | **0.0384** | * |
| Site: UCSD (vs UAB) | +5.1984 | 3.5497 | ±7.0995 | +1.464 | 0.1431 |  |
| Site: UW (vs UAB) | +2.2546 | 3.3804 | ±6.7608 | +0.667 | 0.5048 |  |
| **Age (years)** | **-0.6334** | 0.1407 | ±0.2815 | **-4.501** | **6.78e-06** | *** |
| **BMI (kg/m2)** | **+0.3865** | 0.1930 | ±0.3859 | **+2.003** | **0.0452** | * |
| Hypertension | +2.5087 | 3.3695 | ±6.7390 | +0.745 | 0.4566 |  |
| High cholesterol | +0.8389 | 2.7063 | ±5.4127 | +0.310 | 0.7566 |  |
| **Kidney disease** | **+12.8340** | 3.7929 | ±7.5859 | **+3.384** | **7.15e-04** | *** |
| Circulatory disease | -2.1273 | 3.7108 | ±7.4215 | -0.573 | 0.5664 |  |
| Glucose SD, pooled (mg/dL) | -0.0553 | 0.2838 | ±0.5676 | -0.195 | 0.8456 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **177**, R² = **0.2621**, Adj R² = **0.2129**, F-statistic = **5.33** (p = **3.40e-07**), Residual SE = **17.089** on **165** df, AIC = **1518.7**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+83.1927** | 11.8998 | ±23.7996 | **+6.991** | **2.73e-12** | *** |
| **Education: graduate level (vs college)** | **-11.4253** | 2.9090 | ±5.8180 | **-3.928** | **8.58e-05** | *** |
| **Education: high school or below (vs college)** | **-8.7595** | 4.1940 | ±8.3880 | **-2.089** | **0.0367** | * |
| Site: UCSD (vs UAB) | +5.2323 | 3.5439 | ±7.0877 | +1.476 | 0.1398 |  |
| Site: UW (vs UAB) | +2.2710 | 3.3714 | ±6.7429 | +0.674 | 0.5006 |  |
| **Age (years)** | **-0.6329** | 0.1410 | ±0.2821 | **-4.487** | **7.21e-06** | *** |
| **BMI (kg/m2)** | **+0.3857** | 0.1927 | ±0.3854 | **+2.002** | **0.0453** | * |
| Hypertension | +2.5664 | 3.3678 | ±6.7357 | +0.762 | 0.4460 |  |
| High cholesterol | +0.8245 | 2.7105 | ±5.4209 | +0.304 | 0.7610 |  |
| **Kidney disease** | **+12.8219** | 3.7372 | ±7.4745 | **+3.431** | **6.02e-04** | *** |
| Circulatory disease | -2.1275 | 3.7047 | ±7.4094 | -0.574 | 0.5658 |  |
| Avg. daily SD (mg/dL) | -0.0745 | 0.2868 | ±0.5736 | -0.260 | 0.7950 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **177**, R² = **0.2623**, Adj R² = **0.2131**, F-statistic = **5.33** (p = **3.33e-07**), Residual SE = **17.087** on **165** df, AIC = **1518.6**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+84.1792** | 12.6666 | ±25.3331 | **+6.646** | **3.02e-11** | *** |
| **Education: graduate level (vs college)** | **-11.3862** | 2.9079 | ±5.8158 | **-3.916** | **9.02e-05** | *** |
| **Education: high school or below (vs college)** | **-8.5504** | 4.3225 | ±8.6450 | **-1.978** | **0.0479** | * |
| Site: UCSD (vs UAB) | +5.1349 | 3.5512 | ±7.1023 | +1.446 | 0.1482 |  |
| Site: UW (vs UAB) | +2.1505 | 3.3912 | ±6.7824 | +0.634 | 0.5260 |  |
| **Age (years)** | **-0.6315** | 0.1405 | ±0.2810 | **-4.495** | **6.96e-06** | *** |
| **BMI (kg/m2)** | **+0.3831** | 0.1927 | ±0.3854 | **+1.989** | **0.0467** | * |
| Hypertension | +2.5858 | 3.3739 | ±6.7478 | +0.766 | 0.4434 |  |
| High cholesterol | +0.8130 | 2.7089 | ±5.4177 | +0.300 | 0.7641 |  |
| **Kidney disease** | **+12.8946** | 3.7758 | ±7.5517 | **+3.415** | **6.38e-04** | *** |
| Circulatory disease | -2.1321 | 3.7183 | ±7.4367 | -0.573 | 0.5664 |  |
| CV (%) | -0.1441 | 0.4017 | ±0.8035 | -0.359 | 0.7199 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **177**, R² = **0.2622**, Adj R² = **0.2130**, F-statistic = **5.33** (p = **3.37e-07**), Residual SE = **17.088** on **165** df, AIC = **1518.7**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.7310** | 13.5345 | ±27.0689 | **+5.891** | **3.84e-09** | *** |
| **Education: graduate level (vs college)** | **-11.4154** | 2.9142 | ±5.8283 | **-3.917** | **8.96e-05** | *** |
| **Education: high school or below (vs college)** | **-8.6379** | 4.2829 | ±8.5658 | **-2.017** | **0.0437** | * |
| Site: UCSD (vs UAB) | +5.1703 | 3.5447 | ±7.0894 | +1.459 | 0.1447 |  |
| Site: UW (vs UAB) | +2.1998 | 3.3851 | ±6.7703 | +0.650 | 0.5158 |  |
| **Age (years)** | **-0.6318** | 0.1405 | ±0.2811 | **-4.496** | **6.93e-06** | *** |
| **BMI (kg/m2)** | **+0.3861** | 0.1933 | ±0.3866 | **+1.997** | **0.0458** | * |
| Hypertension | +2.5629 | 3.3760 | ±6.7520 | +0.759 | 0.4478 |  |
| High cholesterol | +0.8428 | 2.7087 | ±5.4173 | +0.311 | 0.7557 |  |
| **Kidney disease** | **+12.8597** | 3.7418 | ±7.4835 | **+3.437** | **5.89e-04** | *** |
| Circulatory disease | -2.1628 | 3.7207 | ±7.4414 | -0.581 | 0.5610 |  |
| Mean / SD ratio | +0.3146 | 1.0403 | ±2.0807 | +0.302 | 0.7623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **177**, R² = **0.2619**, Adj R² = **0.2127**, F-statistic = **5.32** (p = **3.46e-07**), Residual SE = **17.092** on **165** df, AIC = **1518.7**, BIC = **1556.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+80.9084** | 13.3671 | ±26.7341 | **+6.053** | **1.42e-09** | *** |
| **Education: graduate level (vs college)** | **-11.4430** | 2.9133 | ±5.8265 | **-3.928** | **8.57e-05** | *** |
| **Education: high school or below (vs college)** | **-8.7938** | 4.2092 | ±8.4185 | **-2.089** | **0.0367** | * |
| Site: UCSD (vs UAB) | +5.2279 | 3.5345 | ±7.0690 | +1.479 | 0.1391 |  |
| Site: UW (vs UAB) | +2.2899 | 3.3709 | ±6.7419 | +0.679 | 0.4969 |  |
| **Age (years)** | **-0.6329** | 0.1414 | ±0.2829 | **-4.475** | **7.63e-06** | *** |
| **BMI (kg/m2)** | **+0.3863** | 0.1935 | ±0.3871 | **+1.996** | **0.0459** | * |
| Hypertension | +2.5011 | 3.3919 | ±6.7838 | +0.737 | 0.4609 |  |
| High cholesterol | +0.8561 | 2.7128 | ±5.4256 | +0.316 | 0.7523 |  |
| **Kidney disease** | **+12.7691** | 3.6938 | ±7.3875 | **+3.457** | **5.46e-04** | *** |
| Circulatory disease | -2.1961 | 3.7266 | ±7.4531 | -0.589 | 0.5556 |  |
| Avg. daily mean/SD | +0.1204 | 0.7994 | ±1.5988 | +0.151 | 0.8802 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **177**, R² = **0.2622**, Adj R² = **0.2130**, F-statistic = **5.33** (p = **3.37e-07**), Residual SE = **17.088** on **165** df, AIC = **1518.7**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+80.0051** | 13.2429 | ±26.4859 | **+6.041** | **1.53e-09** | *** |
| **Education: graduate level (vs college)** | **-11.4742** | 2.9258 | ±5.8515 | **-3.922** | **8.79e-05** | *** |
| **Education: high school or below (vs college)** | **-8.9639** | 4.1864 | ±8.3728 | **-2.141** | **0.0323** | * |
| Site: UCSD (vs UAB) | +5.1787 | 3.5569 | ±7.1138 | +1.456 | 0.1454 |  |
| Site: UW (vs UAB) | +2.3708 | 3.3561 | ±6.7121 | +0.706 | 0.4799 |  |
| **Age (years)** | **-0.6347** | 0.1402 | ±0.2804 | **-4.526** | **6.00e-06** | *** |
| **BMI (kg/m2)** | **+0.3833** | 0.1937 | ±0.3874 | **+1.979** | **0.0478** | * |
| Hypertension | +2.3752 | 3.3789 | ±6.7577 | +0.703 | 0.4821 |  |
| High cholesterol | +0.8201 | 2.7124 | ±5.4249 | +0.302 | 0.7624 |  |
| **Kidney disease** | **+12.7517** | 3.6601 | ±7.3202 | **+3.484** | **4.94e-04** | *** |
| Circulatory disease | -2.1873 | 3.6939 | ±7.3877 | -0.592 | 0.5538 |  |
| MAG (mg/dL/h) | +0.0568 | 0.2148 | ±0.4297 | +0.264 | 0.7916 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **177**, R² = **0.2619**, Adj R² = **0.2127**, F-statistic = **5.32** (p = **3.44e-07**), Residual SE = **17.091** on **165** df, AIC = **1518.7**, BIC = **1556.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+83.1060** | 12.5871 | ±25.1743 | **+6.602** | **4.04e-11** | *** |
| **Education: graduate level (vs college)** | **-11.4455** | 2.9206 | ±5.8413 | **-3.919** | **8.90e-05** | *** |
| **Education: high school or below (vs college)** | **-8.8034** | 4.1958 | ±8.3916 | **-2.098** | **0.0359** | * |
| Site: UCSD (vs UAB) | +5.2072 | 3.5496 | ±7.0992 | +1.467 | 0.1424 |  |
| Site: UW (vs UAB) | +2.2859 | 3.3902 | ±6.7805 | +0.674 | 0.5001 |  |
| **Age (years)** | **-0.6332** | 0.1420 | ±0.2840 | **-4.459** | **8.24e-06** | *** |
| **BMI (kg/m2)** | **+0.3844** | 0.1931 | ±0.3863 | **+1.990** | **0.0466** | * |
| Hypertension | +2.4863 | 3.3399 | ±6.6798 | +0.744 | 0.4566 |  |
| High cholesterol | +0.8464 | 2.7104 | ±5.4208 | +0.312 | 0.7548 |  |
| **Kidney disease** | **+12.7715** | 3.6926 | ±7.3851 | **+3.459** | **5.43e-04** | *** |
| Circulatory disease | -2.1561 | 3.7058 | ±7.4116 | -0.582 | 0.5607 |  |
| Avg. daily range (mg/dL) | -0.0132 | 0.0757 | ±0.1515 | -0.174 | 0.8618 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **177**, R² = **0.2619**, Adj R² = **0.2126**, F-statistic = **5.32** (p = **3.47e-07**), Residual SE = **17.092** on **165** df, AIC = **1518.7**, BIC = **1556.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+82.2173** | 11.6769 | ±23.3538 | **+7.041** | **1.91e-12** | *** |
| **Education: graduate level (vs college)** | **-11.4457** | 2.9350 | ±5.8700 | **-3.900** | **9.63e-05** | *** |
| **Education: high school or below (vs college)** | **-8.7850** | 4.3497 | ±8.6995 | **-2.020** | **0.0434** | * |
| Site: UCSD (vs UAB) | +5.1636 | 3.5400 | ±7.0800 | +1.459 | 0.1447 |  |
| Site: UW (vs UAB) | +2.2657 | 3.3987 | ±6.7974 | +0.667 | 0.5050 |  |
| **Age (years)** | **-0.6336** | 0.1393 | ±0.2787 | **-4.547** | **5.44e-06** | *** |
| **BMI (kg/m2)** | **+0.3871** | 0.1931 | ±0.3861 | **+2.005** | **0.0450** | * |
| Hypertension | +2.3946 | 3.3575 | ±6.7151 | +0.713 | 0.4757 |  |
| High cholesterol | +0.8687 | 2.7156 | ±5.4312 | +0.320 | 0.7491 |  |
| **Kidney disease** | **+12.8135** | 3.7786 | ±7.5572 | **+3.391** | **6.96e-04** | *** |
| Circulatory disease | -2.1218 | 3.7895 | ±7.5791 | -0.560 | 0.5755 |  |
| SD of daily means (mg/dL) | -0.0595 | 0.5122 | ±1.0245 | -0.116 | 0.9075 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **177**, R² = **0.2656**, Adj R² = **0.2167**, F-statistic = **5.43** (p = **2.41e-07**), Residual SE = **17.048** on **165** df, AIC = **1517.8**, BIC = **1555.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.4316** | 28.1804 | ±56.3607 | **+1.967** | **0.0492** | * |
| **Education: graduate level (vs college)** | **-11.3037** | 2.9164 | ±5.8328 | **-3.876** | **1.06e-04** | *** |
| **Education: high school or below (vs college)** | **-8.6838** | 4.1858 | ±8.3715 | **-2.075** | **0.0380** | * |
| Site: UCSD (vs UAB) | +5.1885 | 3.5444 | ±7.0888 | +1.464 | 0.1432 |  |
| Site: UW (vs UAB) | +2.2526 | 3.3577 | ±6.7154 | +0.671 | 0.5023 |  |
| **Age (years)** | **-0.6220** | 0.1404 | ±0.2809 | **-4.429** | **9.47e-06** | *** |
| **BMI (kg/m2)** | **+0.3982** | 0.1920 | ±0.3840 | **+2.074** | **0.0381** | * |
| Hypertension | +2.5362 | 3.3363 | ±6.6725 | +0.760 | 0.4471 |  |
| High cholesterol | +0.7667 | 2.6885 | ±5.3771 | +0.285 | 0.7755 |  |
| **Kidney disease** | **+13.2300** | 3.8259 | ±7.6519 | **+3.458** | **5.44e-04** | *** |
| Circulatory disease | -1.8116 | 3.7607 | ±7.5214 | -0.482 | 0.6300 |  |
| Time in range 70-180, pooled (%) | +0.2617 | 0.2494 | ±0.4987 | +1.050 | 0.2939 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **177**, R² = **0.2656**, Adj R² = **0.2166**, F-statistic = **5.42** (p = **2.43e-07**), Residual SE = **17.049** on **165** df, AIC = **1517.9**, BIC = **1556.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +55.0116 | 28.3938 | ±56.7876 | +1.937 | 0.0527 | . |
| **Education: graduate level (vs college)** | **-11.3284** | 2.9181 | ±5.8361 | **-3.882** | **1.04e-04** | *** |
| **Education: high school or below (vs college)** | **-8.7408** | 4.1778 | ±8.3556 | **-2.092** | **0.0364** | * |
| Site: UCSD (vs UAB) | +5.1976 | 3.5459 | ±7.0917 | +1.466 | 0.1427 |  |
| Site: UW (vs UAB) | +2.3074 | 3.3584 | ±6.7169 | +0.687 | 0.4920 |  |
| **Age (years)** | **-0.6213** | 0.1404 | ±0.2808 | **-4.426** | **9.62e-06** | *** |
| **BMI (kg/m2)** | **+0.3963** | 0.1918 | ±0.3835 | **+2.067** | **0.0388** | * |
| Hypertension | +2.5767 | 3.3369 | ±6.6738 | +0.772 | 0.4400 |  |
| High cholesterol | +0.7641 | 2.6905 | ±5.3809 | +0.284 | 0.7764 |  |
| **Kidney disease** | **+13.2368** | 3.8203 | ±7.6406 | **+3.465** | **5.30e-04** | *** |
| Circulatory disease | -1.7977 | 3.7514 | ±7.5028 | -0.479 | 0.6318 |  |
| Avg. daily time in range 70-180 (%) | +0.2656 | 0.2531 | ±0.5062 | +1.049 | 0.2940 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **177**, R² = **0.2800**, Adj R² = **0.2320**, F-statistic = **5.83** (p = **5.96e-08**), Residual SE = **16.881** on **165** df, AIC = **1514.3**, BIC = **1552.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+80.1805** | 11.2192 | ±22.4384 | **+7.147** | **8.89e-13** | *** |
| **Education: graduate level (vs college)** | **-10.7319** | 2.8938 | ±5.7876 | **-3.709** | **2.08e-04** | *** |
| Education: high school or below (vs college) | -7.6941 | 4.2020 | ±8.4041 | -1.831 | 0.0671 | . |
| Site: UCSD (vs UAB) | +4.8294 | 3.4648 | ±6.9297 | +1.394 | 0.1634 |  |
| Site: UW (vs UAB) | +2.1074 | 3.3351 | ±6.6702 | +0.632 | 0.5275 |  |
| **Age (years)** | **-0.5886** | 0.1400 | ±0.2801 | **-4.203** | **2.63e-05** | *** |
| **BMI (kg/m2)** | **+0.3742** | 0.1902 | ±0.3804 | **+1.967** | **0.0491** | * |
| Hypertension | +2.3543 | 3.2671 | ±6.5342 | +0.721 | 0.4712 |  |
| High cholesterol | +1.2339 | 2.6803 | ±5.3605 | +0.460 | 0.6453 |  |
| **Kidney disease** | **+12.3739** | 3.6290 | ±7.2579 | **+3.410** | **6.50e-04** | *** |
| Circulatory disease | -1.6239 | 3.7015 | ±7.4031 | -0.439 | 0.6609 |  |
| **Time 54-69, pooled (%)** | **-8.7954** | 3.4685 | ±6.9370 | **-2.536** | **0.0112** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **177**, R² = **0.2805**, Adj R² = **0.2326**, F-statistic = **5.85** (p = **5.63e-08**), Residual SE = **16.874** on **165** df, AIC = **1514.2**, BIC = **1552.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.8164** | 11.2079 | ±22.4158 | **+7.121** | **1.07e-12** | *** |
| **Education: graduate level (vs college)** | **-10.7690** | 2.8948 | ±5.7897 | **-3.720** | **1.99e-04** | *** |
| Education: high school or below (vs college) | -7.8159 | 4.1606 | ±8.3212 | -1.879 | 0.0603 | . |
| Site: UCSD (vs UAB) | +5.0912 | 3.4656 | ±6.9313 | +1.469 | 0.1418 |  |
| Site: UW (vs UAB) | +2.2759 | 3.3397 | ±6.6794 | +0.681 | 0.4956 |  |
| **Age (years)** | **-0.5857** | 0.1397 | ±0.2794 | **-4.192** | **2.77e-05** | *** |
| **BMI (kg/m2)** | **+0.3728** | 0.1897 | ±0.3793 | **+1.966** | **0.0493** | * |
| Hypertension | +2.4517 | 3.2642 | ±6.5284 | +0.751 | 0.4526 |  |
| High cholesterol | +1.2255 | 2.6862 | ±5.3724 | +0.456 | 0.6482 |  |
| **Kidney disease** | **+12.1436** | 3.6163 | ±7.2326 | **+3.358** | **7.85e-04** | *** |
| Circulatory disease | -1.7515 | 3.6671 | ±7.3342 | -0.478 | 0.6329 |  |
| **Avg. daily time 54-69 (%)** | **-8.5686** | 3.6355 | ±7.2710 | **-2.357** | **0.0184** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **177**, R² = **0.2800**, Adj R² = **0.2320**, F-statistic = **5.83** (p = **5.96e-08**), Residual SE = **16.881** on **165** df, AIC = **1514.3**, BIC = **1552.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+80.1805** | 11.2192 | ±22.4384 | **+7.147** | **8.89e-13** | *** |
| **Education: graduate level (vs college)** | **-10.7319** | 2.8938 | ±5.7876 | **-3.709** | **2.08e-04** | *** |
| Education: high school or below (vs college) | -7.6941 | 4.2020 | ±8.4041 | -1.831 | 0.0671 | . |
| Site: UCSD (vs UAB) | +4.8294 | 3.4648 | ±6.9297 | +1.394 | 0.1634 |  |
| Site: UW (vs UAB) | +2.1074 | 3.3351 | ±6.6702 | +0.632 | 0.5275 |  |
| **Age (years)** | **-0.5886** | 0.1400 | ±0.2801 | **-4.203** | **2.63e-05** | *** |
| **BMI (kg/m2)** | **+0.3742** | 0.1902 | ±0.3804 | **+1.967** | **0.0491** | * |
| Hypertension | +2.3543 | 3.2671 | ±6.5342 | +0.721 | 0.4712 |  |
| High cholesterol | +1.2339 | 2.6803 | ±5.3605 | +0.460 | 0.6453 |  |
| **Kidney disease** | **+12.3739** | 3.6290 | ±7.2579 | **+3.410** | **6.50e-04** | *** |
| Circulatory disease | -1.6239 | 3.7015 | ±7.4031 | -0.439 | 0.6609 |  |
| **Time < 70 (%)** | **-8.7954** | 3.4685 | ±6.9370 | **-2.536** | **0.0112** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **177**, R² = **0.2805**, Adj R² = **0.2326**, F-statistic = **5.85** (p = **5.63e-08**), Residual SE = **16.874** on **165** df, AIC = **1514.2**, BIC = **1552.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.8164** | 11.2079 | ±22.4158 | **+7.121** | **1.07e-12** | *** |
| **Education: graduate level (vs college)** | **-10.7690** | 2.8948 | ±5.7897 | **-3.720** | **1.99e-04** | *** |
| Education: high school or below (vs college) | -7.8159 | 4.1606 | ±8.3212 | -1.879 | 0.0603 | . |
| Site: UCSD (vs UAB) | +5.0912 | 3.4656 | ±6.9313 | +1.469 | 0.1418 |  |
| Site: UW (vs UAB) | +2.2759 | 3.3397 | ±6.6794 | +0.681 | 0.4956 |  |
| **Age (years)** | **-0.5857** | 0.1397 | ±0.2794 | **-4.192** | **2.77e-05** | *** |
| **BMI (kg/m2)** | **+0.3728** | 0.1897 | ±0.3793 | **+1.966** | **0.0493** | * |
| Hypertension | +2.4517 | 3.2642 | ±6.5284 | +0.751 | 0.4526 |  |
| High cholesterol | +1.2255 | 2.6862 | ±5.3724 | +0.456 | 0.6482 |  |
| **Kidney disease** | **+12.1436** | 3.6163 | ±7.2326 | **+3.358** | **7.85e-04** | *** |
| Circulatory disease | -1.7515 | 3.6671 | ±7.3342 | -0.478 | 0.6329 |  |
| **Avg. daily time < 70 (%)** | **-8.5686** | 3.6355 | ±7.2710 | **-2.357** | **0.0184** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **177**, R² = **0.2646**, Adj R² = **0.2156**, F-statistic = **5.40** (p = **2.67e-07**), Residual SE = **17.060** on **165** df, AIC = **1518.1**, BIC = **1556.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.6940** | 11.2200 | ±22.4401 | **+7.281** | **3.31e-13** | *** |
| **Education: graduate level (vs college)** | **-11.3457** | 2.9183 | ±5.8365 | **-3.888** | **1.01e-04** | *** |
| **Education: high school or below (vs college)** | **-8.7445** | 4.1864 | ±8.3729 | **-2.089** | **0.0367** | * |
| Site: UCSD (vs UAB) | +5.2031 | 3.5462 | ±7.0923 | +1.467 | 0.1423 |  |
| Site: UW (vs UAB) | +2.2710 | 3.3597 | ±6.7194 | +0.676 | 0.4991 |  |
| **Age (years)** | **-0.6251** | 0.1405 | ±0.2810 | **-4.450** | **8.58e-06** | *** |
| **BMI (kg/m2)** | **+0.3967** | 0.1923 | ±0.3847 | **+2.063** | **0.0392** | * |
| Hypertension | +2.5180 | 3.3432 | ±6.6863 | +0.753 | 0.4513 |  |
| High cholesterol | +0.7718 | 2.6919 | ±5.3838 | +0.287 | 0.7743 |  |
| **Kidney disease** | **+13.1614** | 3.8136 | ±7.6273 | **+3.451** | **5.58e-04** | *** |
| Circulatory disease | -1.8841 | 3.7535 | ±7.5070 | -0.502 | 0.6157 |  |
| Time 181-250, pooled (%) | -0.2214 | 0.2508 | ±0.5017 | -0.883 | 0.3774 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **177**, R² = **0.2644**, Adj R² = **0.2154**, F-statistic = **5.39** (p = **2.71e-07**), Residual SE = **17.062** on **165** df, AIC = **1518.1**, BIC = **1556.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.6784** | 11.2254 | ±22.4507 | **+7.276** | **3.43e-13** | *** |
| **Education: graduate level (vs college)** | **-11.3682** | 2.9198 | ±5.8397 | **-3.893** | **9.88e-05** | *** |
| **Education: high school or below (vs college)** | **-8.7927** | 4.1812 | ±8.3625 | **-2.103** | **0.0355** | * |
| Site: UCSD (vs UAB) | +5.2046 | 3.5466 | ±7.0933 | +1.467 | 0.1422 |  |
| Site: UW (vs UAB) | +2.3137 | 3.3607 | ±6.7214 | +0.688 | 0.4912 |  |
| **Age (years)** | **-0.6249** | 0.1404 | ±0.2808 | **-4.450** | **8.58e-06** | *** |
| **BMI (kg/m2)** | **+0.3950** | 0.1922 | ±0.3843 | **+2.056** | **0.0398** | * |
| Hypertension | +2.5469 | 3.3443 | ±6.6885 | +0.762 | 0.4463 |  |
| High cholesterol | +0.7713 | 2.6939 | ±5.3878 | +0.286 | 0.7746 |  |
| **Kidney disease** | **+13.1645** | 3.8095 | ±7.6191 | **+3.456** | **5.49e-04** | *** |
| Circulatory disease | -1.8761 | 3.7452 | ±7.4903 | -0.501 | 0.6164 |  |
| Avg. daily time 181-250 (%) | -0.2201 | 0.2536 | ±0.5071 | -0.868 | 0.3854 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **177**, R² = **0.2646**, Adj R² = **0.2156**, F-statistic = **5.40** (p = **2.67e-07**), Residual SE = **17.060** on **165** df, AIC = **1518.1**, BIC = **1556.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.6940** | 11.2200 | ±22.4401 | **+7.281** | **3.31e-13** | *** |
| **Education: graduate level (vs college)** | **-11.3457** | 2.9183 | ±5.8365 | **-3.888** | **1.01e-04** | *** |
| **Education: high school or below (vs college)** | **-8.7445** | 4.1864 | ±8.3729 | **-2.089** | **0.0367** | * |
| Site: UCSD (vs UAB) | +5.2031 | 3.5462 | ±7.0923 | +1.467 | 0.1423 |  |
| Site: UW (vs UAB) | +2.2710 | 3.3597 | ±6.7194 | +0.676 | 0.4991 |  |
| **Age (years)** | **-0.6251** | 0.1405 | ±0.2810 | **-4.450** | **8.58e-06** | *** |
| **BMI (kg/m2)** | **+0.3967** | 0.1923 | ±0.3847 | **+2.063** | **0.0392** | * |
| Hypertension | +2.5180 | 3.3432 | ±6.6863 | +0.753 | 0.4513 |  |
| High cholesterol | +0.7718 | 2.6919 | ±5.3838 | +0.287 | 0.7743 |  |
| **Kidney disease** | **+13.1614** | 3.8136 | ±7.6273 | **+3.451** | **5.58e-04** | *** |
| Circulatory disease | -1.8841 | 3.7535 | ±7.5070 | -0.502 | 0.6157 |  |
| Time > 180 (%) | -0.2214 | 0.2508 | ±0.5017 | -0.883 | 0.3774 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **177**, R² = **0.2644**, Adj R² = **0.2154**, F-statistic = **5.39** (p = **2.71e-07**), Residual SE = **17.062** on **165** df, AIC = **1518.1**, BIC = **1556.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.6784** | 11.2254 | ±22.4507 | **+7.276** | **3.43e-13** | *** |
| **Education: graduate level (vs college)** | **-11.3682** | 2.9198 | ±5.8397 | **-3.893** | **9.88e-05** | *** |
| **Education: high school or below (vs college)** | **-8.7927** | 4.1812 | ±8.3625 | **-2.103** | **0.0355** | * |
| Site: UCSD (vs UAB) | +5.2046 | 3.5466 | ±7.0933 | +1.467 | 0.1422 |  |
| Site: UW (vs UAB) | +2.3137 | 3.3607 | ±6.7214 | +0.688 | 0.4912 |  |
| **Age (years)** | **-0.6249** | 0.1404 | ±0.2808 | **-4.450** | **8.58e-06** | *** |
| **BMI (kg/m2)** | **+0.3950** | 0.1922 | ±0.3843 | **+2.056** | **0.0398** | * |
| Hypertension | +2.5469 | 3.3443 | ±6.6885 | +0.762 | 0.4463 |  |
| High cholesterol | +0.7713 | 2.6939 | ±5.3878 | +0.286 | 0.7746 |  |
| **Kidney disease** | **+13.1645** | 3.8095 | ±7.6191 | **+3.456** | **5.49e-04** | *** |
| Circulatory disease | -1.8761 | 3.7452 | ±7.4903 | -0.501 | 0.6164 |  |
| Avg. daily time > 180 (%) | -0.2201 | 0.2536 | ±0.5071 | -0.868 | 0.3854 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 177)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **177**, R² = **0.2626**, Adj R² = **0.2134**, F-statistic = **5.34** (p = **3.25e-07**), Residual SE = **17.084** on **165** df, AIC = **1518.6**, BIC = **1556.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+81.6277** | 11.3507 | ±22.7014 | **+7.191** | **6.41e-13** | *** |
| **Education: graduate level (vs college)** | **-11.4315** | 2.9213 | ±5.8425 | **-3.913** | **9.11e-05** | *** |
| **Education: high school or below (vs college)** | **-8.6971** | 4.2448 | ±8.4896 | **-2.049** | **0.0405** | * |
| Site: UCSD (vs UAB) | +5.0865 | 3.5676 | ±7.1352 | +1.426 | 0.1539 |  |
| Site: UW (vs UAB) | +2.2138 | 3.3586 | ±6.7172 | +0.659 | 0.5098 |  |
| **Age (years)** | **-0.6307** | 0.1404 | ±0.2808 | **-4.492** | **7.07e-06** | *** |
| **BMI (kg/m2)** | **+0.3974** | 0.1972 | ±0.3944 | **+2.015** | **0.0439** | * |
| Hypertension | +2.3350 | 3.3750 | ±6.7499 | +0.692 | 0.4890 |  |
| High cholesterol | +0.8540 | 2.7035 | ±5.4070 | +0.316 | 0.7521 |  |
| **Kidney disease** | **+13.0033** | 3.8709 | ±7.7419 | **+3.359** | **7.82e-04** | *** |
| Circulatory disease | -1.9865 | 3.7699 | ±7.5398 | -0.527 | 0.5982 |  |
| Nocturnal time > 180 (%) | -0.1110 | 0.2727 | ±0.5454 | -0.407 | 0.6838 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
