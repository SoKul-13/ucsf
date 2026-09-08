# Phase 6b model output tables - Near-normal substitute: >= 99% of readings within 70-180 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Home environment

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 384; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **384**, R² = **0.1418**, Adj R² = **0.1116**, F-statistic = **4.70** (p = **1.52e-07**), Residual SE = **0.869** on **370** df, AIC = **995.6**, BIC = **1050.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7434** | 0.2892 | ±0.5785 | **+6.027** | **1.67e-09** | *** |
| Education: graduate level (vs college) | -0.0865 | 0.0966 | ±0.1931 | -0.895 | 0.3706 |  |
| Education: high school or below (vs college) | +0.3106 | 0.1965 | ±0.3929 | +1.581 | 0.1139 |  |
| Site: UCSD (vs UAB) | +0.0137 | 0.1167 | ±0.2335 | +0.117 | 0.9067 |  |
| **Site: UW (vs UAB)** | **-0.3611** | 0.1259 | ±0.2517 | **-2.869** | **0.0041** | ** |
| Season: spring (vs autumn) | -0.1346 | 0.1240 | ±0.2479 | -1.086 | 0.2774 |  |
| Season: summer (vs autumn) | +0.1862 | 0.1481 | ±0.2963 | +1.257 | 0.2086 |  |
| Season: winter (vs autumn) | -0.0393 | 0.1307 | ±0.2614 | -0.301 | 0.7637 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0074 | **-2.011** | **0.0443** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0070 | ±0.0139 | **+3.333** | **8.60e-04** | *** |
| Hypertension | +0.1148 | 0.1094 | ±0.2187 | +1.050 | 0.2939 |  |
| High cholesterol | -0.0403 | 0.0902 | ±0.1803 | -0.447 | 0.6546 |  |
| Kidney disease | -0.1015 | 0.1579 | ±0.3159 | -0.642 | 0.5207 |  |
| Circulatory disease | +0.3080 | 0.1872 | ±0.3743 | +1.646 | 0.0998 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **384**, R² = **0.1436**, Adj R² = **0.1111**, F-statistic = **4.42** (p = **2.50e-07**), Residual SE = **0.869** on **369** df, AIC = **996.8**, BIC = **1056.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0032 | 1.0107 | ±2.0214 | +0.993 | 0.3209 |  |
| Education: graduate level (vs college) | -0.0858 | 0.0968 | ±0.1935 | -0.886 | 0.3754 |  |
| Education: high school or below (vs college) | +0.3057 | 0.1955 | ±0.3911 | +1.563 | 0.1180 |  |
| Site: UCSD (vs UAB) | +0.0142 | 0.1171 | ±0.2343 | +0.121 | 0.9034 |  |
| **Site: UW (vs UAB)** | **-0.3578** | 0.1262 | ±0.2524 | **-2.836** | **0.0046** | ** |
| Season: spring (vs autumn) | -0.1162 | 0.1229 | ±0.2458 | -0.945 | 0.3446 |  |
| Season: summer (vs autumn) | +0.1776 | 0.1501 | ±0.3003 | +1.183 | 0.2367 |  |
| Season: winter (vs autumn) | -0.0337 | 0.1305 | ±0.2610 | -0.259 | 0.7959 |  |
| **Age (years)** | **-0.0079** | 0.0038 | ±0.0076 | **-2.072** | **0.0383** | * |
| **BMI (kg/m2)** | **+0.0227** | 0.0070 | ±0.0139 | **+3.267** | **0.0011** | ** |
| Hypertension | +0.1072 | 0.1112 | ±0.2223 | +0.964 | 0.3349 |  |
| High cholesterol | -0.0582 | 0.0935 | ±0.1869 | -0.623 | 0.5334 |  |
| Kidney disease | -0.0895 | 0.1593 | ±0.3185 | -0.562 | 0.5743 |  |
| Circulatory disease | +0.3202 | 0.1887 | ±0.3773 | +1.697 | 0.0896 | . |
| HbA1c (%) | +0.1416 | 0.1870 | ±0.3740 | +0.757 | 0.4489 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **384**, R² = **0.1477**, Adj R² = **0.1154**, F-statistic = **4.57** (p = **1.21e-07**), Residual SE = **0.867** on **369** df, AIC = **995.0**, BIC = **1054.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8228** | 0.7919 | ±1.5839 | **+3.565** | **3.65e-04** | *** |
| Education: graduate level (vs college) | -0.0828 | 0.0966 | ±0.1932 | -0.857 | 0.3914 |  |
| Education: high school or below (vs college) | +0.3048 | 0.1951 | ±0.3903 | +1.562 | 0.1182 |  |
| Site: UCSD (vs UAB) | +0.0235 | 0.1175 | ±0.2351 | +0.200 | 0.8417 |  |
| **Site: UW (vs UAB)** | **-0.3496** | 0.1261 | ±0.2523 | **-2.771** | **0.0056** | ** |
| Season: spring (vs autumn) | -0.1435 | 0.1239 | ±0.2477 | -1.158 | 0.2468 |  |
| Season: summer (vs autumn) | +0.1872 | 0.1476 | ±0.2953 | +1.268 | 0.2048 |  |
| Season: winter (vs autumn) | -0.0434 | 0.1313 | ±0.2627 | -0.330 | 0.7413 |  |
| **Age (years)** | **-0.0077** | 0.0038 | ±0.0076 | **-2.038** | **0.0416** | * |
| **BMI (kg/m2)** | **+0.0240** | 0.0069 | ±0.0138 | **+3.468** | **5.24e-04** | *** |
| Hypertension | +0.1259 | 0.1106 | ±0.2212 | +1.138 | 0.2551 |  |
| High cholesterol | -0.0470 | 0.0903 | ±0.1807 | -0.520 | 0.6031 |  |
| Kidney disease | -0.0906 | 0.1617 | ±0.3233 | -0.561 | 0.5751 |  |
| Circulatory disease | +0.3040 | 0.1884 | ±0.3767 | +1.614 | 0.1066 |  |
| Mean glucose (mg/dL) | -0.0096 | 0.0060 | ±0.0120 | -1.596 | 0.1106 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **384**, R² = **0.1477**, Adj R² = **0.1154**, F-statistic = **4.57** (p = **1.21e-07**), Residual SE = **0.867** on **369** df, AIC = **995.0**, BIC = **1054.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+4.1454** | 1.5935 | ±3.1871 | **+2.601** | **0.0093** | ** |
| Education: graduate level (vs college) | -0.0828 | 0.0966 | ±0.1932 | -0.857 | 0.3914 |  |
| Education: high school or below (vs college) | +0.3048 | 0.1951 | ±0.3903 | +1.562 | 0.1182 |  |
| Site: UCSD (vs UAB) | +0.0235 | 0.1175 | ±0.2351 | +0.200 | 0.8417 |  |
| **Site: UW (vs UAB)** | **-0.3496** | 0.1261 | ±0.2523 | **-2.771** | **0.0056** | ** |
| Season: spring (vs autumn) | -0.1435 | 0.1239 | ±0.2477 | -1.158 | 0.2468 |  |
| Season: summer (vs autumn) | +0.1872 | 0.1476 | ±0.2953 | +1.268 | 0.2048 |  |
| Season: winter (vs autumn) | -0.0434 | 0.1313 | ±0.2627 | -0.330 | 0.7413 |  |
| **Age (years)** | **-0.0077** | 0.0038 | ±0.0076 | **-2.038** | **0.0416** | * |
| **BMI (kg/m2)** | **+0.0240** | 0.0069 | ±0.0138 | **+3.468** | **5.24e-04** | *** |
| Hypertension | +0.1259 | 0.1106 | ±0.2212 | +1.138 | 0.2551 |  |
| High cholesterol | -0.0470 | 0.0903 | ±0.1807 | -0.520 | 0.6031 |  |
| Kidney disease | -0.0906 | 0.1617 | ±0.3233 | -0.561 | 0.5751 |  |
| Circulatory disease | +0.3040 | 0.1884 | ±0.3767 | +1.614 | 0.1066 |  |
| GMI (%) | -0.3996 | 0.2504 | ±0.5008 | -1.596 | 0.1106 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **384**, R² = **0.1433**, Adj R² = **0.1108**, F-statistic = **4.41** (p = **2.64e-07**), Residual SE = **0.869** on **369** df, AIC = **996.9**, BIC = **1056.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1897** | 0.6537 | ±1.3075 | **+3.350** | **8.09e-04** | *** |
| Education: graduate level (vs college) | -0.0896 | 0.0975 | ±0.1950 | -0.919 | 0.3583 |  |
| Education: high school or below (vs college) | +0.3043 | 0.1972 | ±0.3944 | +1.543 | 0.1227 |  |
| Site: UCSD (vs UAB) | +0.0235 | 0.1190 | ±0.2381 | +0.197 | 0.8435 |  |
| **Site: UW (vs UAB)** | **-0.3527** | 0.1271 | ±0.2541 | **-2.776** | **0.0055** | ** |
| Season: spring (vs autumn) | -0.1353 | 0.1245 | ±0.2489 | -1.087 | 0.2769 |  |
| Season: summer (vs autumn) | +0.1890 | 0.1486 | ±0.2972 | +1.272 | 0.2035 |  |
| Season: winter (vs autumn) | -0.0392 | 0.1313 | ±0.2627 | -0.298 | 0.7654 |  |
| **Age (years)** | **-0.0080** | 0.0039 | ±0.0078 | **-2.029** | **0.0424** | * |
| **BMI (kg/m2)** | **+0.0241** | 0.0070 | ±0.0140 | **+3.452** | **5.57e-04** | *** |
| Hypertension | +0.1182 | 0.1102 | ±0.2204 | +1.072 | 0.2836 |  |
| High cholesterol | -0.0409 | 0.0904 | ±0.1808 | -0.452 | 0.6510 |  |
| Kidney disease | -0.1041 | 0.1611 | ±0.3221 | -0.646 | 0.5181 |  |
| Circulatory disease | +0.3047 | 0.1896 | ±0.3792 | +1.607 | 0.1081 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0039 | 0.0046 | ±0.0093 | -0.843 | 0.3992 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **384**, R² = **0.1426**, Adj R² = **0.1101**, F-statistic = **4.38** (p = **2.98e-07**), Residual SE = **0.870** on **369** df, AIC = **997.2**, BIC = **1056.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9406** | 0.4433 | ±0.8865 | **+4.378** | **1.20e-05** | *** |
| Education: graduate level (vs college) | -0.0896 | 0.0974 | ±0.1947 | -0.921 | 0.3572 |  |
| Education: high school or below (vs college) | +0.3114 | 0.1964 | ±0.3929 | +1.585 | 0.1129 |  |
| Site: UCSD (vs UAB) | +0.0073 | 0.1165 | ±0.2329 | +0.062 | 0.9503 |  |
| **Site: UW (vs UAB)** | **-0.3650** | 0.1257 | ±0.2513 | **-2.905** | **0.0037** | ** |
| Season: spring (vs autumn) | -0.1289 | 0.1250 | ±0.2500 | -1.032 | 0.3023 |  |
| Season: summer (vs autumn) | +0.1900 | 0.1487 | ±0.2973 | +1.278 | 0.2012 |  |
| Season: winter (vs autumn) | -0.0332 | 0.1334 | ±0.2669 | -0.249 | 0.8033 |  |
| **Age (years)** | **-0.0074** | 0.0037 | ±0.0075 | **-1.999** | **0.0456** | * |
| **BMI (kg/m2)** | **+0.0234** | 0.0070 | ±0.0139 | **+3.362** | **7.74e-04** | *** |
| Hypertension | +0.1150 | 0.1095 | ±0.2190 | +1.050 | 0.2937 |  |
| High cholesterol | -0.0431 | 0.0907 | ±0.1815 | -0.475 | 0.6344 |  |
| Kidney disease | -0.0965 | 0.1601 | ±0.3203 | -0.603 | 0.5468 |  |
| Circulatory disease | +0.3104 | 0.1867 | ±0.3733 | +1.663 | 0.0963 | . |
| Glucose SD, pooled (mg/dL) | -0.0121 | 0.0198 | ±0.0396 | -0.610 | 0.5419 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **384**, R² = **0.1425**, Adj R² = **0.1100**, F-statistic = **4.38** (p = **3.04e-07**), Residual SE = **0.870** on **369** df, AIC = **997.3**, BIC = **1056.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9065** | 0.4120 | ±0.8241 | **+4.627** | **3.71e-06** | *** |
| Education: graduate level (vs college) | -0.0898 | 0.0976 | ±0.1952 | -0.920 | 0.3576 |  |
| Education: high school or below (vs college) | +0.3097 | 0.1960 | ±0.3921 | +1.580 | 0.1142 |  |
| Site: UCSD (vs UAB) | +0.0074 | 0.1170 | ±0.2339 | +0.063 | 0.9494 |  |
| **Site: UW (vs UAB)** | **-0.3649** | 0.1256 | ±0.2513 | **-2.904** | **0.0037** | ** |
| Season: spring (vs autumn) | -0.1302 | 0.1251 | ±0.2502 | -1.041 | 0.2981 |  |
| Season: summer (vs autumn) | +0.1886 | 0.1490 | ±0.2979 | +1.266 | 0.2054 |  |
| Season: winter (vs autumn) | -0.0361 | 0.1325 | ±0.2650 | -0.273 | 0.7851 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-2.001** | **0.0454** | * |
| **BMI (kg/m2)** | **+0.0235** | 0.0069 | ±0.0139 | **+3.397** | **6.82e-04** | *** |
| Hypertension | +0.1139 | 0.1093 | ±0.2186 | +1.042 | 0.2974 |  |
| High cholesterol | -0.0423 | 0.0907 | ±0.1813 | -0.467 | 0.6406 |  |
| Kidney disease | -0.0968 | 0.1598 | ±0.3195 | -0.606 | 0.5447 |  |
| Circulatory disease | +0.3086 | 0.1870 | ±0.3740 | +1.650 | 0.0989 | . |
| Avg. daily SD (mg/dL) | -0.0110 | 0.0189 | ±0.0378 | -0.584 | 0.5592 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **384**, R² = **0.1419**, Adj R² = **0.1093**, F-statistic = **4.36** (p = **3.40e-07**), Residual SE = **0.870** on **369** df, AIC = **997.6**, BIC = **1056.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6917** | 0.4147 | ±0.8293 | **+4.080** | **4.51e-05** | *** |
| Education: graduate level (vs college) | -0.0854 | 0.0973 | ±0.1945 | -0.878 | 0.3797 |  |
| Education: high school or below (vs college) | +0.3101 | 0.1969 | ±0.3937 | +1.575 | 0.1152 |  |
| Site: UCSD (vs UAB) | +0.0158 | 0.1175 | ±0.2349 | +0.135 | 0.8930 |  |
| **Site: UW (vs UAB)** | **-0.3595** | 0.1261 | ±0.2523 | **-2.850** | **0.0044** | ** |
| Season: spring (vs autumn) | -0.1366 | 0.1245 | ±0.2489 | -1.097 | 0.2725 |  |
| Season: summer (vs autumn) | +0.1852 | 0.1481 | ±0.2963 | +1.250 | 0.2113 |  |
| Season: winter (vs autumn) | -0.0411 | 0.1330 | ±0.2659 | -0.309 | 0.7573 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-2.000** | **0.0455** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0070 | ±0.0140 | **+3.327** | **8.78e-04** | *** |
| Hypertension | +0.1153 | 0.1098 | ±0.2196 | +1.050 | 0.2938 |  |
| High cholesterol | -0.0399 | 0.0906 | ±0.1812 | -0.440 | 0.6600 |  |
| Kidney disease | -0.1021 | 0.1582 | ±0.3163 | -0.646 | 0.5184 |  |
| Circulatory disease | +0.3072 | 0.1875 | ±0.3751 | +1.638 | 0.1014 |  |
| CV (%) | +0.0036 | 0.0217 | ±0.0433 | +0.164 | 0.8694 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **384**, R² = **0.1418**, Adj R² = **0.1092**, F-statistic = **4.35** (p = **3.44e-07**), Residual SE = **0.870** on **369** df, AIC = **997.6**, BIC = **1056.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7424** | 0.4332 | ±0.8664 | **+4.022** | **5.76e-05** | *** |
| Education: graduate level (vs college) | -0.0865 | 0.0974 | ±0.1947 | -0.888 | 0.3744 |  |
| Education: high school or below (vs college) | +0.3106 | 0.1968 | ±0.3936 | +1.578 | 0.1145 |  |
| Site: UCSD (vs UAB) | +0.0136 | 0.1174 | ±0.2348 | +0.116 | 0.9074 |  |
| **Site: UW (vs UAB)** | **-0.3611** | 0.1262 | ±0.2523 | **-2.862** | **0.0042** | ** |
| Season: spring (vs autumn) | -0.1346 | 0.1246 | ±0.2492 | -1.080 | 0.2800 |  |
| Season: summer (vs autumn) | +0.1863 | 0.1483 | ±0.2966 | +1.256 | 0.2091 |  |
| Season: winter (vs autumn) | -0.0393 | 0.1328 | ±0.2656 | -0.296 | 0.7675 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-2.002** | **0.0453** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0070 | ±0.0140 | **+3.326** | **8.80e-04** | *** |
| Hypertension | +0.1148 | 0.1097 | ±0.2194 | +1.047 | 0.2952 |  |
| High cholesterol | -0.0403 | 0.0905 | ±0.1811 | -0.446 | 0.6559 |  |
| Kidney disease | -0.1014 | 0.1584 | ±0.3168 | -0.640 | 0.5219 |  |
| Circulatory disease | +0.3081 | 0.1873 | ±0.3745 | +1.645 | 0.1000 | . |
| Mean / SD ratio | +0.0001 | 0.0436 | ±0.0873 | +0.003 | 0.9973 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **384**, R² = **0.1419**, Adj R² = **0.1093**, F-statistic = **4.36** (p = **3.37e-07**), Residual SE = **0.870** on **369** df, AIC = **997.6**, BIC = **1056.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8062** | 0.4139 | ±0.8278 | **+4.364** | **1.28e-05** | *** |
| Education: graduate level (vs college) | -0.0848 | 0.0976 | ±0.1952 | -0.868 | 0.3851 |  |
| Education: high school or below (vs college) | +0.3105 | 0.1969 | ±0.3939 | +1.577 | 0.1148 |  |
| Site: UCSD (vs UAB) | +0.0162 | 0.1177 | ±0.2354 | +0.137 | 0.8908 |  |
| **Site: UW (vs UAB)** | **-0.3595** | 0.1261 | ±0.2521 | **-2.852** | **0.0043** | ** |
| Season: spring (vs autumn) | -0.1373 | 0.1247 | ±0.2494 | -1.101 | 0.2709 |  |
| Season: summer (vs autumn) | +0.1852 | 0.1485 | ±0.2969 | +1.247 | 0.2123 |  |
| Season: winter (vs autumn) | -0.0410 | 0.1323 | ±0.2646 | -0.310 | 0.7569 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-2.005** | **0.0450** | * |
| **BMI (kg/m2)** | **+0.0231** | 0.0070 | ±0.0139 | **+3.325** | **8.85e-04** | *** |
| Hypertension | +0.1156 | 0.1097 | ±0.2193 | +1.054 | 0.2917 |  |
| High cholesterol | -0.0400 | 0.0905 | ±0.1809 | -0.442 | 0.6587 |  |
| Kidney disease | -0.1023 | 0.1580 | ±0.3160 | -0.647 | 0.5175 |  |
| Circulatory disease | +0.3076 | 0.1874 | ±0.3748 | +1.641 | 0.1007 |  |
| Avg. daily mean/SD | -0.0077 | 0.0343 | ±0.0687 | -0.224 | 0.8225 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **384**, R² = **0.1436**, Adj R² = **0.1111**, F-statistic = **4.42** (p = **2.51e-07**), Residual SE = **0.869** on **369** df, AIC = **996.8**, BIC = **1056.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.4650** | 0.4251 | ±0.8502 | **+3.446** | **5.68e-04** | *** |
| Education: graduate level (vs college) | -0.0885 | 0.0965 | ±0.1930 | -0.917 | 0.3591 |  |
| Education: high school or below (vs college) | +0.2991 | 0.1980 | ±0.3960 | +1.511 | 0.1309 |  |
| Site: UCSD (vs UAB) | +0.0216 | 0.1170 | ±0.2340 | +0.185 | 0.8532 |  |
| **Site: UW (vs UAB)** | **-0.3483** | 0.1276 | ±0.2552 | **-2.729** | **0.0064** | ** |
| Season: spring (vs autumn) | -0.1401 | 0.1238 | ±0.2476 | -1.132 | 0.2578 |  |
| Season: summer (vs autumn) | +0.1868 | 0.1488 | ±0.2975 | +1.256 | 0.2092 |  |
| Season: winter (vs autumn) | -0.0450 | 0.1307 | ±0.2613 | -0.345 | 0.7303 |  |
| Age (years) | -0.0070 | 0.0038 | ±0.0076 | -1.850 | 0.0643 | . |
| **BMI (kg/m2)** | **+0.0236** | 0.0070 | ±0.0139 | **+3.396** | **6.83e-04** | *** |
| Hypertension | +0.1180 | 0.1093 | ±0.2186 | +1.080 | 0.2803 |  |
| High cholesterol | -0.0452 | 0.0903 | ±0.1805 | -0.501 | 0.6165 |  |
| Kidney disease | -0.1104 | 0.1539 | ±0.3077 | -0.717 | 0.4732 |  |
| Circulatory disease | +0.3081 | 0.1867 | ±0.3734 | +1.650 | 0.0989 | . |
| MAG (mg/dL/h) | +0.0069 | 0.0075 | ±0.0150 | +0.925 | 0.3552 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **384**, R² = **0.1431**, Adj R² = **0.1106**, F-statistic = **4.40** (p = **2.72e-07**), Residual SE = **0.869** on **369** df, AIC = **997.0**, BIC = **1056.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0086** | 0.4598 | ±0.9197 | **+4.368** | **1.25e-05** | *** |
| Education: graduate level (vs college) | -0.0876 | 0.0969 | ±0.1937 | -0.904 | 0.3658 |  |
| Education: high school or below (vs college) | +0.3106 | 0.1963 | ±0.3927 | +1.582 | 0.1136 |  |
| Site: UCSD (vs UAB) | +0.0055 | 0.1172 | ±0.2344 | +0.047 | 0.9626 |  |
| **Site: UW (vs UAB)** | **-0.3670** | 0.1259 | ±0.2518 | **-2.914** | **0.0036** | ** |
| Season: spring (vs autumn) | -0.1280 | 0.1249 | ±0.2497 | -1.025 | 0.3053 |  |
| Season: summer (vs autumn) | +0.1888 | 0.1486 | ±0.2972 | +1.270 | 0.2039 |  |
| Season: winter (vs autumn) | -0.0330 | 0.1334 | ±0.2667 | -0.247 | 0.8045 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-2.019** | **0.0435** | * |
| **BMI (kg/m2)** | **+0.0229** | 0.0070 | ±0.0141 | **+3.252** | **0.0011** | ** |
| Hypertension | +0.1110 | 0.1089 | ±0.2178 | +1.020 | 0.3079 |  |
| High cholesterol | -0.0396 | 0.0903 | ±0.1806 | -0.439 | 0.6606 |  |
| Kidney disease | -0.0977 | 0.1608 | ±0.3216 | -0.608 | 0.5435 |  |
| Circulatory disease | +0.3103 | 0.1866 | ±0.3732 | +1.663 | 0.0963 | . |
| Avg. daily range (mg/dL) | -0.0031 | 0.0041 | ±0.0081 | -0.770 | 0.4413 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **384**, R² = **0.1442**, Adj R² = **0.1117**, F-statistic = **4.44** (p = **2.26e-07**), Residual SE = **0.869** on **369** df, AIC = **996.5**, BIC = **1055.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6310** | 0.3166 | ±0.6332 | **+5.152** | **2.58e-07** | *** |
| Education: graduate level (vs college) | -0.0906 | 0.0968 | ±0.1937 | -0.935 | 0.3496 |  |
| Education: high school or below (vs college) | +0.3000 | 0.1946 | ±0.3892 | +1.542 | 0.1231 |  |
| Site: UCSD (vs UAB) | +0.0167 | 0.1166 | ±0.2333 | +0.143 | 0.8864 |  |
| **Site: UW (vs UAB)** | **-0.3659** | 0.1259 | ±0.2518 | **-2.906** | **0.0037** | ** |
| Season: spring (vs autumn) | -0.1435 | 0.1236 | ±0.2471 | -1.161 | 0.2456 |  |
| Season: summer (vs autumn) | +0.1766 | 0.1502 | ±0.3005 | +1.175 | 0.2399 |  |
| Season: winter (vs autumn) | -0.0529 | 0.1317 | ±0.2634 | -0.402 | 0.6878 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-2.022** | **0.0432** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0070 | ±0.0139 | **+3.333** | **8.61e-04** | *** |
| Hypertension | +0.1084 | 0.1099 | ±0.2198 | +0.987 | 0.3238 |  |
| High cholesterol | -0.0423 | 0.0906 | ±0.1811 | -0.467 | 0.6406 |  |
| Kidney disease | -0.0901 | 0.1569 | ±0.3138 | -0.574 | 0.5657 |  |
| Circulatory disease | +0.2996 | 0.1861 | ±0.3721 | +1.610 | 0.1074 |  |
| SD of daily means (mg/dL) | +0.0262 | 0.0274 | ±0.0548 | +0.956 | 0.3390 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **384**, R² = **0.1418**, Adj R² = **0.1093**, F-statistic = **4.36** (p = **3.40e-07**), Residual SE = **0.870** on **369** df, AIC = **997.6**, BIC = **1056.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5507 | 15.8108 | ±31.6215 | -0.035 | 0.9722 |  |
| Education: graduate level (vs college) | -0.0865 | 0.0968 | ±0.1936 | -0.893 | 0.3717 |  |
| Education: high school or below (vs college) | +0.3108 | 0.1969 | ±0.3939 | +1.578 | 0.1145 |  |
| Site: UCSD (vs UAB) | +0.0125 | 0.1182 | ±0.2364 | +0.105 | 0.9161 |  |
| **Site: UW (vs UAB)** | **-0.3620** | 0.1272 | ±0.2543 | **-2.846** | **0.0044** | ** |
| Season: spring (vs autumn) | -0.1337 | 0.1244 | ±0.2489 | -1.075 | 0.2826 |  |
| Season: summer (vs autumn) | +0.1876 | 0.1496 | ±0.2991 | +1.254 | 0.2097 |  |
| Season: winter (vs autumn) | -0.0380 | 0.1333 | ±0.2667 | -0.285 | 0.7758 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-2.006** | **0.0448** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0070 | ±0.0140 | **+3.315** | **9.17e-04** | *** |
| Hypertension | +0.1147 | 0.1096 | ±0.2192 | +1.047 | 0.2950 |  |
| High cholesterol | -0.0397 | 0.0904 | ±0.1808 | -0.439 | 0.6608 |  |
| Kidney disease | -0.1003 | 0.1588 | ±0.3177 | -0.632 | 0.5277 |  |
| Circulatory disease | +0.3086 | 0.1873 | ±0.3745 | +1.648 | 0.0994 | . |
| Time in range 70-180, pooled (%) | +0.0231 | 0.1590 | ±0.3181 | +0.145 | 0.8846 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **384**, R² = **0.1418**, Adj R² = **0.1092**, F-statistic = **4.35** (p = **3.43e-07**), Residual SE = **0.870** on **369** df, AIC = **997.6**, BIC = **1056.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0613 | 15.5192 | ±31.0384 | +0.068 | 0.9455 |  |
| Education: graduate level (vs college) | -0.0865 | 0.0968 | ±0.1936 | -0.893 | 0.3719 |  |
| Education: high school or below (vs college) | +0.3105 | 0.1974 | ±0.3947 | +1.574 | 0.1156 |  |
| Site: UCSD (vs UAB) | +0.0134 | 0.1180 | ±0.2360 | +0.114 | 0.9094 |  |
| **Site: UW (vs UAB)** | **-0.3612** | 0.1264 | ±0.2528 | **-2.857** | **0.0043** | ** |
| Season: spring (vs autumn) | -0.1344 | 0.1244 | ±0.2488 | -1.081 | 0.2798 |  |
| Season: summer (vs autumn) | +0.1864 | 0.1490 | ±0.2980 | +1.251 | 0.2110 |  |
| Season: winter (vs autumn) | -0.0390 | 0.1327 | ±0.2653 | -0.294 | 0.7689 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-1.998** | **0.0458** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0070 | ±0.0140 | **+3.324** | **8.88e-04** | *** |
| Hypertension | +0.1146 | 0.1092 | ±0.2185 | +1.049 | 0.2941 |  |
| High cholesterol | -0.0401 | 0.0904 | ±0.1808 | -0.443 | 0.6576 |  |
| Kidney disease | -0.1014 | 0.1586 | ±0.3173 | -0.639 | 0.5228 |  |
| Circulatory disease | +0.3083 | 0.1879 | ±0.3758 | +1.641 | 0.1008 |  |
| Avg. daily time in range 70-180 (%) | +0.0069 | 0.1560 | ±0.3120 | +0.044 | 0.9649 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.1448**, Adj R² = **0.1124**, F-statistic = **4.46** (p = **2.03e-07**), Residual SE = **0.869** on **369** df, AIC = **996.3**, BIC = **1055.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7187** | 0.2958 | ±0.5916 | **+5.810** | **6.23e-09** | *** |
| Education: graduate level (vs college) | -0.0843 | 0.0963 | ±0.1925 | -0.876 | 0.3812 |  |
| Education: high school or below (vs college) | +0.3134 | 0.1986 | ±0.3972 | +1.578 | 0.1145 |  |
| Site: UCSD (vs UAB) | +0.0383 | 0.1212 | ±0.2424 | +0.316 | 0.7517 |  |
| **Site: UW (vs UAB)** | **-0.3452** | 0.1291 | ±0.2582 | **-2.673** | **0.0075** | ** |
| Season: spring (vs autumn) | -0.1531 | 0.1262 | ±0.2524 | -1.213 | 0.2252 |  |
| Season: summer (vs autumn) | +0.1771 | 0.1487 | ±0.2973 | +1.191 | 0.2336 |  |
| Season: winter (vs autumn) | -0.0520 | 0.1312 | ±0.2625 | -0.396 | 0.6918 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0074 | **-2.013** | **0.0442** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0070 | ±0.0139 | **+3.334** | **8.57e-04** | *** |
| Hypertension | +0.1055 | 0.1099 | ±0.2198 | +0.960 | 0.3371 |  |
| High cholesterol | -0.0402 | 0.0908 | ±0.1815 | -0.442 | 0.6583 |  |
| Kidney disease | -0.0865 | 0.1600 | ±0.3200 | -0.541 | 0.5887 |  |
| Circulatory disease | +0.2999 | 0.1872 | ±0.3744 | +1.602 | 0.1092 |  |
| Any reading < 54 during wear (0/1) | +0.1420 | 0.1498 | ±0.2996 | +0.948 | 0.3431 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.1508**, Adj R² = **0.1186**, F-statistic = **4.68** (p = **6.95e-08**), Residual SE = **0.866** on **369** df, AIC = **993.5**, BIC = **1052.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7046** | 0.2933 | ±0.5866 | **+5.811** | **6.20e-09** | *** |
| Education: graduate level (vs college) | -0.0851 | 0.0961 | ±0.1923 | -0.885 | 0.3761 |  |
| Education: high school or below (vs college) | +0.3279 | 0.1975 | ±0.3951 | +1.660 | 0.0969 | . |
| Site: UCSD (vs UAB) | +0.0437 | 0.1201 | ±0.2402 | +0.364 | 0.7157 |  |
| **Site: UW (vs UAB)** | **-0.3461** | 0.1274 | ±0.2548 | **-2.716** | **0.0066** | ** |
| Season: spring (vs autumn) | -0.1306 | 0.1236 | ±0.2472 | -1.057 | 0.2907 |  |
| Season: summer (vs autumn) | +0.1841 | 0.1482 | ±0.2965 | +1.242 | 0.2142 |  |
| Season: winter (vs autumn) | -0.0379 | 0.1290 | ±0.2581 | -0.294 | 0.7691 |  |
| Age (years) | -0.0071 | 0.0037 | ±0.0075 | -1.902 | 0.0572 | . |
| **BMI (kg/m2)** | **+0.0223** | 0.0070 | ±0.0139 | **+3.216** | **0.0013** | ** |
| Hypertension | +0.0996 | 0.1087 | ±0.2174 | +0.916 | 0.3597 |  |
| High cholesterol | -0.0382 | 0.0908 | ±0.1817 | -0.421 | 0.6738 |  |
| Kidney disease | -0.0848 | 0.1594 | ±0.3187 | -0.532 | 0.5948 |  |
| Circulatory disease | +0.2900 | 0.1848 | ±0.3695 | +1.570 | 0.1165 |  |
| Time < 54 (%) | +1.7790 | 1.1129 | ±2.2258 | +1.598 | 0.1099 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.1521**, Adj R² = **0.1199**, F-statistic = **4.73** (p = **5.56e-08**), Residual SE = **0.865** on **369** df, AIC = **993.0**, BIC = **1052.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7093** | 0.2908 | ±0.5816 | **+5.878** | **4.16e-09** | *** |
| Education: graduate level (vs college) | -0.0920 | 0.0975 | ±0.1950 | -0.943 | 0.3455 |  |
| Education: high school or below (vs college) | +0.3183 | 0.1958 | ±0.3916 | +1.625 | 0.1041 |  |
| Site: UCSD (vs UAB) | +0.0320 | 0.1195 | ±0.2389 | +0.268 | 0.7890 |  |
| **Site: UW (vs UAB)** | **-0.3540** | 0.1268 | ±0.2535 | **-2.793** | **0.0052** | ** |
| Season: spring (vs autumn) | -0.1281 | 0.1247 | ±0.2494 | -1.027 | 0.3043 |  |
| Season: summer (vs autumn) | +0.2071 | 0.1484 | ±0.2968 | +1.396 | 0.1628 |  |
| Season: winter (vs autumn) | -0.0347 | 0.1308 | ±0.2615 | -0.265 | 0.7907 |  |
| Age (years) | -0.0072 | 0.0037 | ±0.0075 | -1.910 | 0.0562 | . |
| **BMI (kg/m2)** | **+0.0227** | 0.0070 | ±0.0140 | **+3.235** | **0.0012** | ** |
| Hypertension | +0.1050 | 0.1078 | ±0.2157 | +0.973 | 0.3304 |  |
| High cholesterol | -0.0371 | 0.0910 | ±0.1819 | -0.408 | 0.6833 |  |
| Kidney disease | -0.0953 | 0.1602 | ±0.3205 | -0.595 | 0.5522 |  |
| Circulatory disease | +0.2811 | 0.1876 | ±0.3753 | +1.498 | 0.1341 |  |
| Avg. daily time < 54 (%) | +2.2870 | 1.5469 | ±3.0938 | +1.478 | 0.1393 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.1494**, Adj R² = **0.1171**, F-statistic = **4.63** (p = **8.99e-08**), Residual SE = **0.866** on **369** df, AIC = **994.2**, BIC = **1053.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6736** | 0.2916 | ±0.5833 | **+5.739** | **9.54e-09** | *** |
| Education: graduate level (vs college) | -0.0807 | 0.0960 | ±0.1919 | -0.842 | 0.4000 |  |
| Education: high school or below (vs college) | +0.2981 | 0.1969 | ±0.3937 | +1.514 | 0.1299 |  |
| Site: UCSD (vs UAB) | +0.0301 | 0.1184 | ±0.2368 | +0.254 | 0.7994 |  |
| **Site: UW (vs UAB)** | **-0.3418** | 0.1268 | ±0.2536 | **-2.695** | **0.0070** | ** |
| Season: spring (vs autumn) | -0.1435 | 0.1229 | ±0.2459 | -1.167 | 0.2431 |  |
| Season: summer (vs autumn) | +0.1832 | 0.1493 | ±0.2986 | +1.227 | 0.2198 |  |
| Season: winter (vs autumn) | -0.0533 | 0.1317 | ±0.2634 | -0.405 | 0.6858 |  |
| **Age (years)** | **-0.0076** | 0.0038 | ±0.0075 | **-2.013** | **0.0441** | * |
| **BMI (kg/m2)** | **+0.0235** | 0.0069 | ±0.0138 | **+3.392** | **6.95e-04** | *** |
| Hypertension | +0.1315 | 0.1098 | ±0.2195 | +1.198 | 0.2310 |  |
| High cholesterol | -0.0580 | 0.0902 | ±0.1803 | -0.643 | 0.5204 |  |
| Kidney disease | -0.0720 | 0.1557 | ±0.3114 | -0.463 | 0.6437 |  |
| Circulatory disease | +0.3062 | 0.1892 | ±0.3784 | +1.618 | 0.1056 |  |
| Time 54-69, pooled (%) | +0.4595 | 0.2854 | ±0.5707 | +1.610 | 0.1073 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **384**, R² = **0.1485**, Adj R² = **0.1162**, F-statistic = **4.60** (p = **1.05e-07**), Residual SE = **0.867** on **369** df, AIC = **994.6**, BIC = **1053.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6803** | 0.2910 | ±0.5820 | **+5.775** | **7.70e-09** | *** |
| Education: graduate level (vs college) | -0.0788 | 0.0959 | ±0.1919 | -0.821 | 0.4114 |  |
| Education: high school or below (vs college) | +0.2968 | 0.1961 | ±0.3923 | +1.513 | 0.1303 |  |
| Site: UCSD (vs UAB) | +0.0225 | 0.1178 | ±0.2356 | +0.191 | 0.8484 |  |
| **Site: UW (vs UAB)** | **-0.3521** | 0.1261 | ±0.2522 | **-2.792** | **0.0052** | ** |
| Season: spring (vs autumn) | -0.1314 | 0.1236 | ±0.2471 | -1.064 | 0.2874 |  |
| Season: summer (vs autumn) | +0.1937 | 0.1498 | ±0.2996 | +1.293 | 0.1961 |  |
| Season: winter (vs autumn) | -0.0483 | 0.1313 | ±0.2626 | -0.368 | 0.7130 |  |
| **Age (years)** | **-0.0075** | 0.0038 | ±0.0075 | **-2.006** | **0.0448** | * |
| **BMI (kg/m2)** | **+0.0234** | 0.0069 | ±0.0138 | **+3.381** | **7.21e-04** | *** |
| Hypertension | +0.1402 | 0.1118 | ±0.2236 | +1.254 | 0.2098 |  |
| High cholesterol | -0.0524 | 0.0904 | ±0.1808 | -0.580 | 0.5617 |  |
| Kidney disease | -0.0819 | 0.1558 | ±0.3116 | -0.525 | 0.5992 |  |
| Circulatory disease | +0.3014 | 0.1898 | ±0.3796 | +1.588 | 0.1123 |  |
| Avg. daily time 54-69 (%) | +0.4359 | 0.2967 | ±0.5934 | +1.469 | 0.1418 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **384**, R² = **0.1521**, Adj R² = **0.1199**, F-statistic = **4.73** (p = **5.51e-08**), Residual SE = **0.865** on **369** df, AIC = **993.0**, BIC = **1052.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6604** | 0.2939 | ±0.5877 | **+5.650** | **1.60e-08** | *** |
| Education: graduate level (vs college) | -0.0802 | 0.0956 | ±0.1913 | -0.838 | 0.4020 |  |
| Education: high school or below (vs college) | +0.3023 | 0.1975 | ±0.3950 | +1.530 | 0.1259 |  |
| Site: UCSD (vs UAB) | +0.0388 | 0.1192 | ±0.2384 | +0.326 | 0.7447 |  |
| **Site: UW (vs UAB)** | **-0.3370** | 0.1272 | ±0.2544 | **-2.649** | **0.0081** | ** |
| Season: spring (vs autumn) | -0.1428 | 0.1228 | ±0.2455 | -1.163 | 0.2448 |  |
| Season: summer (vs autumn) | +0.1825 | 0.1492 | ±0.2983 | +1.224 | 0.2211 |  |
| Season: winter (vs autumn) | -0.0535 | 0.1309 | ±0.2617 | -0.409 | 0.6828 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-1.995** | **0.0460** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0069 | ±0.0138 | **+3.375** | **7.38e-04** | *** |
| Hypertension | +0.1280 | 0.1089 | ±0.2178 | +1.176 | 0.2396 |  |
| High cholesterol | -0.0581 | 0.0901 | ±0.1803 | -0.645 | 0.5192 |  |
| Kidney disease | -0.0664 | 0.1560 | ±0.3120 | -0.425 | 0.6706 |  |
| Circulatory disease | +0.3013 | 0.1884 | ±0.3768 | +1.599 | 0.1098 |  |
| Time < 70 (%) | +0.4779 | 0.2622 | ±0.5244 | +1.822 | 0.0684 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **384**, R² = **0.1510**, Adj R² = **0.1188**, F-statistic = **4.69** (p = **6.73e-08**), Residual SE = **0.865** on **369** df, AIC = **993.5**, BIC = **1052.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6698** | 0.2916 | ±0.5832 | **+5.727** | **1.02e-08** | *** |
| Education: graduate level (vs college) | -0.0795 | 0.0957 | ±0.1915 | -0.830 | 0.4064 |  |
| Education: high school or below (vs college) | +0.2975 | 0.1964 | ±0.3928 | +1.515 | 0.1298 |  |
| Site: UCSD (vs UAB) | +0.0267 | 0.1183 | ±0.2365 | +0.226 | 0.8212 |  |
| **Site: UW (vs UAB)** | **-0.3501** | 0.1263 | ±0.2525 | **-2.773** | **0.0056** | ** |
| Season: spring (vs autumn) | -0.1299 | 0.1235 | ±0.2470 | -1.052 | 0.2927 |  |
| Season: summer (vs autumn) | +0.1983 | 0.1498 | ±0.2995 | +1.324 | 0.1854 |  |
| Season: winter (vs autumn) | -0.0479 | 0.1309 | ±0.2619 | -0.366 | 0.7145 |  |
| **Age (years)** | **-0.0075** | 0.0038 | ±0.0075 | **-1.992** | **0.0464** | * |
| **BMI (kg/m2)** | **+0.0233** | 0.0069 | ±0.0138 | **+3.373** | **7.43e-04** | *** |
| Hypertension | +0.1397 | 0.1112 | ±0.2225 | +1.256 | 0.2091 |  |
| High cholesterol | -0.0525 | 0.0903 | ±0.1806 | -0.581 | 0.5610 |  |
| Kidney disease | -0.0795 | 0.1561 | ±0.3122 | -0.509 | 0.6106 |  |
| Circulatory disease | +0.2955 | 0.1897 | ±0.3795 | +1.558 | 0.1193 |  |
| Avg. daily time < 70 (%) | +0.4613 | 0.2793 | ±0.5587 | +1.651 | 0.0987 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.1501**, Adj R² = **0.1179**, F-statistic = **4.66** (p = **7.87e-08**), Residual SE = **0.866** on **369** df, AIC = **993.9**, BIC = **1053.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +171.8998 | 110.0403 | ±220.0807 | +1.562 | 0.1183 |  |
| Education: graduate level (vs college) | -0.0840 | 0.0961 | ±0.1921 | -0.874 | 0.3819 |  |
| Education: high school or below (vs college) | +0.3281 | 0.1976 | ±0.3952 | +1.660 | 0.0969 | . |
| Site: UCSD (vs UAB) | +0.0425 | 0.1200 | ±0.2400 | +0.354 | 0.7230 |  |
| **Site: UW (vs UAB)** | **-0.3476** | 0.1273 | ±0.2546 | **-2.731** | **0.0063** | ** |
| Season: spring (vs autumn) | -0.1307 | 0.1236 | ±0.2471 | -1.057 | 0.2903 |  |
| Season: summer (vs autumn) | +0.1841 | 0.1482 | ±0.2964 | +1.242 | 0.2142 |  |
| Season: winter (vs autumn) | -0.0393 | 0.1291 | ±0.2583 | -0.305 | 0.7607 |  |
| Age (years) | -0.0071 | 0.0038 | ±0.0075 | -1.884 | 0.0595 | . |
| **BMI (kg/m2)** | **+0.0225** | 0.0069 | ±0.0139 | **+3.233** | **0.0012** | ** |
| Hypertension | +0.1007 | 0.1088 | ±0.2175 | +0.925 | 0.3547 |  |
| High cholesterol | -0.0399 | 0.0908 | ±0.1816 | -0.439 | 0.6607 |  |
| Kidney disease | -0.0851 | 0.1594 | ±0.3187 | -0.534 | 0.5933 |  |
| Circulatory disease | +0.2910 | 0.1848 | ±0.3697 | +1.574 | 0.1154 |  |
| Time 54-250, pooled (%) | -1.7020 | 1.1009 | ±2.2018 | -1.546 | 0.1221 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.1510**, Adj R² = **0.1188**, F-statistic = **4.69** (p = **6.71e-08**), Residual SE = **0.865** on **369** df, AIC = **993.5**, BIC = **1052.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +216.5489 | 148.3761 | ±296.7522 | +1.459 | 0.1444 |  |
| Education: graduate level (vs college) | -0.0900 | 0.0973 | ±0.1946 | -0.926 | 0.3547 |  |
| Education: high school or below (vs college) | +0.3191 | 0.1959 | ±0.3919 | +1.629 | 0.1034 |  |
| Site: UCSD (vs UAB) | +0.0310 | 0.1193 | ±0.2387 | +0.260 | 0.7950 |  |
| **Site: UW (vs UAB)** | **-0.3557** | 0.1265 | ±0.2531 | **-2.811** | **0.0049** | ** |
| Season: spring (vs autumn) | -0.1284 | 0.1246 | ±0.2491 | -1.031 | 0.3027 |  |
| Season: summer (vs autumn) | +0.2057 | 0.1483 | ±0.2966 | +1.387 | 0.1656 |  |
| Season: winter (vs autumn) | -0.0369 | 0.1307 | ±0.2614 | -0.283 | 0.7775 |  |
| Age (years) | -0.0071 | 0.0038 | ±0.0075 | -1.890 | 0.0588 | . |
| **BMI (kg/m2)** | **+0.0228** | 0.0070 | ±0.0140 | **+3.259** | **0.0011** | ** |
| Hypertension | +0.1061 | 0.1079 | ±0.2158 | +0.984 | 0.3253 |  |
| High cholesterol | -0.0394 | 0.0909 | ±0.1818 | -0.434 | 0.6643 |  |
| Kidney disease | -0.0951 | 0.1601 | ±0.3203 | -0.594 | 0.5527 |  |
| Circulatory disease | +0.2830 | 0.1875 | ±0.3750 | +1.509 | 0.1312 |  |
| Avg. daily time 54-250 (%) | -2.1484 | 1.4839 | ±2.9678 | -1.448 | 0.1477 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **384**, R² = **0.1480**, Adj R² = **0.1157**, F-statistic = **4.58** (p = **1.15e-07**), Residual SE = **0.867** on **369** df, AIC = **994.8**, BIC = **1054.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8457** | 0.3032 | ±0.6063 | **+6.088** | **1.14e-09** | *** |
| Education: graduate level (vs college) | -0.0832 | 0.0962 | ±0.1925 | -0.864 | 0.3876 |  |
| Education: high school or below (vs college) | +0.3084 | 0.1966 | ±0.3932 | +1.569 | 0.1167 |  |
| Site: UCSD (vs UAB) | +0.0135 | 0.1159 | ±0.2319 | +0.116 | 0.9075 |  |
| **Site: UW (vs UAB)** | **-0.3579** | 0.1246 | ±0.2491 | **-2.874** | **0.0041** | ** |
| Season: spring (vs autumn) | -0.1286 | 0.1244 | ±0.2488 | -1.034 | 0.3012 |  |
| Season: summer (vs autumn) | +0.1995 | 0.1495 | ±0.2990 | +1.335 | 0.1820 |  |
| Season: winter (vs autumn) | -0.0324 | 0.1315 | ±0.2631 | -0.246 | 0.8056 |  |
| **Age (years)** | **-0.0077** | 0.0037 | ±0.0075 | **-2.068** | **0.0386** | * |
| **BMI (kg/m2)** | **+0.0226** | 0.0070 | ±0.0140 | **+3.223** | **0.0013** | ** |
| Hypertension | +0.1214 | 0.1094 | ±0.2189 | +1.109 | 0.2673 |  |
| High cholesterol | -0.0427 | 0.0903 | ±0.1806 | -0.473 | 0.6362 |  |
| Kidney disease | -0.0693 | 0.1656 | ±0.3313 | -0.418 | 0.6756 |  |
| Circulatory disease | +0.3102 | 0.1843 | ±0.3687 | +1.683 | 0.0924 | . |
| Time 181-250, pooled (%) | -0.2616 | 0.1619 | ±0.3239 | -1.616 | 0.1062 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **384**, R² = **0.1464**, Adj R² = **0.1140**, F-statistic = **4.52** (p = **1.54e-07**), Residual SE = **0.868** on **369** df, AIC = **995.6**, BIC = **1054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8256** | 0.3018 | ±0.6037 | **+6.048** | **1.47e-09** | *** |
| Education: graduate level (vs college) | -0.0832 | 0.0963 | ±0.1926 | -0.865 | 0.3872 |  |
| Education: high school or below (vs college) | +0.3027 | 0.1962 | ±0.3924 | +1.543 | 0.1229 |  |
| Site: UCSD (vs UAB) | +0.0113 | 0.1165 | ±0.2329 | +0.097 | 0.9224 |  |
| **Site: UW (vs UAB)** | **-0.3582** | 0.1250 | ±0.2499 | **-2.866** | **0.0042** | ** |
| Season: spring (vs autumn) | -0.1256 | 0.1253 | ±0.2506 | -1.002 | 0.3162 |  |
| Season: summer (vs autumn) | +0.1965 | 0.1502 | ±0.3003 | +1.308 | 0.1908 |  |
| Season: winter (vs autumn) | -0.0335 | 0.1320 | ±0.2640 | -0.254 | 0.7995 |  |
| **Age (years)** | **-0.0079** | 0.0038 | ±0.0075 | **-2.109** | **0.0349** | * |
| **BMI (kg/m2)** | **+0.0230** | 0.0069 | ±0.0138 | **+3.327** | **8.78e-04** | *** |
| Hypertension | +0.1205 | 0.1096 | ±0.2193 | +1.099 | 0.2716 |  |
| High cholesterol | -0.0380 | 0.0903 | ±0.1807 | -0.420 | 0.6742 |  |
| Kidney disease | -0.0883 | 0.1656 | ±0.3311 | -0.533 | 0.5938 |  |
| Circulatory disease | +0.3118 | 0.1846 | ±0.3692 | +1.689 | 0.0912 | . |
| Avg. daily time 181-250 (%) | -0.2230 | 0.1577 | ±0.3154 | -1.414 | 0.1574 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **384**, R² = **0.1481**, Adj R² = **0.1158**, F-statistic = **4.58** (p = **1.13e-07**), Residual SE = **0.867** on **369** df, AIC = **994.8**, BIC = **1054.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8471** | 0.3034 | ±0.6068 | **+6.088** | **1.14e-09** | *** |
| Education: graduate level (vs college) | -0.0833 | 0.0962 | ±0.1925 | -0.866 | 0.3867 |  |
| Education: high school or below (vs college) | +0.3083 | 0.1966 | ±0.3932 | +1.568 | 0.1169 |  |
| Site: UCSD (vs UAB) | +0.0135 | 0.1159 | ±0.2319 | +0.116 | 0.9076 |  |
| **Site: UW (vs UAB)** | **-0.3578** | 0.1245 | ±0.2491 | **-2.873** | **0.0041** | ** |
| Season: spring (vs autumn) | -0.1286 | 0.1244 | ±0.2488 | -1.034 | 0.3013 |  |
| Season: summer (vs autumn) | +0.1996 | 0.1495 | ±0.2990 | +1.335 | 0.1818 |  |
| Season: winter (vs autumn) | -0.0321 | 0.1315 | ±0.2631 | -0.244 | 0.8071 |  |
| **Age (years)** | **-0.0077** | 0.0037 | ±0.0075 | **-2.071** | **0.0384** | * |
| **BMI (kg/m2)** | **+0.0225** | 0.0070 | ±0.0140 | **+3.220** | **0.0013** | ** |
| Hypertension | +0.1214 | 0.1094 | ±0.2189 | +1.109 | 0.2674 |  |
| High cholesterol | -0.0425 | 0.0903 | ±0.1805 | -0.471 | 0.6379 |  |
| Kidney disease | -0.0692 | 0.1657 | ±0.3314 | -0.418 | 0.6763 |  |
| Circulatory disease | +0.3102 | 0.1843 | ±0.3686 | +1.683 | 0.0924 | . |
| Time > 180 (%) | -0.2631 | 0.1618 | ±0.3236 | -1.626 | 0.1039 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **384**, R² = **0.1464**, Adj R² = **0.1141**, F-statistic = **4.52** (p = **1.52e-07**), Residual SE = **0.868** on **369** df, AIC = **995.5**, BIC = **1054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8270** | 0.3020 | ±0.6040 | **+6.049** | **1.46e-09** | *** |
| Education: graduate level (vs college) | -0.0834 | 0.0963 | ±0.1926 | -0.866 | 0.3864 |  |
| Education: high school or below (vs college) | +0.3025 | 0.1962 | ±0.3923 | +1.542 | 0.1231 |  |
| Site: UCSD (vs UAB) | +0.0113 | 0.1165 | ±0.2329 | +0.097 | 0.9226 |  |
| **Site: UW (vs UAB)** | **-0.3580** | 0.1250 | ±0.2499 | **-2.865** | **0.0042** | ** |
| Season: spring (vs autumn) | -0.1255 | 0.1253 | ±0.2506 | -1.002 | 0.3164 |  |
| Season: summer (vs autumn) | +0.1966 | 0.1502 | ±0.3003 | +1.309 | 0.1905 |  |
| Season: winter (vs autumn) | -0.0333 | 0.1320 | ±0.2641 | -0.252 | 0.8010 |  |
| **Age (years)** | **-0.0080** | 0.0038 | ±0.0075 | **-2.112** | **0.0347** | * |
| **BMI (kg/m2)** | **+0.0230** | 0.0069 | ±0.0138 | **+3.325** | **8.83e-04** | *** |
| Hypertension | +0.1205 | 0.1096 | ±0.2193 | +1.099 | 0.2716 |  |
| High cholesterol | -0.0377 | 0.0903 | ±0.1806 | -0.418 | 0.6761 |  |
| Kidney disease | -0.0883 | 0.1656 | ±0.3313 | -0.533 | 0.5941 |  |
| Circulatory disease | +0.3118 | 0.1846 | ±0.3691 | +1.689 | 0.0911 | . |
| Avg. daily time > 180 (%) | -0.2246 | 0.1575 | ±0.3150 | -1.426 | 0.1538 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **384**, R² = **0.1509**, Adj R² = **0.1187**, F-statistic = **4.69** (p = **6.81e-08**), Residual SE = **0.865** on **369** df, AIC = **993.5**, BIC = **1052.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8194** | 0.2916 | ±0.5832 | **+6.240** | **4.39e-10** | *** |
| Education: graduate level (vs college) | -0.0974 | 0.0976 | ±0.1952 | -0.998 | 0.3183 |  |
| Education: high school or below (vs college) | +0.3072 | 0.1944 | ±0.3889 | +1.580 | 0.1142 |  |
| Site: UCSD (vs UAB) | +0.0035 | 0.1171 | ±0.2342 | +0.030 | 0.9759 |  |
| **Site: UW (vs UAB)** | **-0.3560** | 0.1247 | ±0.2494 | **-2.855** | **0.0043** | ** |
| Season: spring (vs autumn) | -0.1255 | 0.1240 | ±0.2481 | -1.012 | 0.3116 |  |
| Season: summer (vs autumn) | +0.1886 | 0.1464 | ±0.2928 | +1.288 | 0.1976 |  |
| Season: winter (vs autumn) | -0.0167 | 0.1319 | ±0.2637 | -0.127 | 0.8990 |  |
| **Age (years)** | **-0.0091** | 0.0038 | ±0.0076 | **-2.389** | **0.0169** | * |
| **BMI (kg/m2)** | **+0.0245** | 0.0069 | ±0.0138 | **+3.558** | **3.73e-04** | *** |
| Hypertension | +0.1268 | 0.1090 | ±0.2180 | +1.164 | 0.2446 |  |
| High cholesterol | -0.0302 | 0.0895 | ±0.1791 | -0.337 | 0.7360 |  |
| Kidney disease | -0.0949 | 0.1801 | ±0.3603 | -0.527 | 0.5983 |  |
| Circulatory disease | +0.3078 | 0.1855 | ±0.3709 | +1.660 | 0.0969 | . |
| Nocturnal time > 180 (%) | -0.2724 | 0.1523 | ±0.3047 | -1.788 | 0.0738 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 384; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **384**, R² = **0.3432**, Adj R² = **0.3201**, F-statistic = **14.87** (p = **5.60e-27**), Residual SE = **1.860** on **370** df, AIC = **1580.3**, BIC = **1635.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1018** | 0.8617 | ±1.7234 | **+27.970** | **3.77e-172** | *** |
| Education: graduate level (vs college) | +0.0429 | 0.2062 | ±0.4124 | +0.208 | 0.8351 |  |
| Education: high school or below (vs college) | +0.3652 | 0.3892 | ±0.7784 | +0.938 | 0.3480 |  |
| Site: UCSD (vs UAB) | -0.3276 | 0.2574 | ±0.5149 | -1.272 | 0.2032 |  |
| **Site: UW (vs UAB)** | **-1.0869** | 0.2500 | ±0.4999 | **-4.348** | **1.37e-05** | *** |
| Season: spring (vs autumn) | -0.2866 | 0.2929 | ±0.5858 | -0.979 | 0.3278 |  |
| **Season: summer (vs autumn)** | **+1.7933** | 0.3505 | ±0.7009 | **+5.117** | **3.11e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5176** | 0.2914 | ±0.5829 | **-5.207** | **1.92e-07** | *** |
| Age (years) | +0.0070 | 0.0090 | ±0.0180 | +0.784 | 0.4331 |  |
| BMI (kg/m2) | +0.0189 | 0.0165 | ±0.0330 | +1.143 | 0.2532 |  |
| Hypertension | -0.1757 | 0.2315 | ±0.4630 | -0.759 | 0.4480 |  |
| High cholesterol | -0.2933 | 0.2068 | ±0.4136 | -1.418 | 0.1561 |  |
| **Kidney disease** | **+0.7553** | 0.3599 | ±0.7199 | **+2.098** | **0.0359** | * |
| Circulatory disease | +0.6409 | 0.3905 | ±0.7811 | +1.641 | 0.1008 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **384**, R² = **0.3436**, Adj R² = **0.3187**, F-statistic = **13.80** (p = **1.99e-26**), Residual SE = **1.862** on **369** df, AIC = **1582.0**, BIC = **1641.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.2430** | 2.0743 | ±4.1486 | **+11.205** | **3.85e-29** | *** |
| Education: graduate level (vs college) | +0.0437 | 0.2064 | ±0.4129 | +0.212 | 0.8322 |  |
| Education: high school or below (vs college) | +0.3596 | 0.3936 | ±0.7872 | +0.914 | 0.3610 |  |
| Site: UCSD (vs UAB) | -0.3270 | 0.2584 | ±0.5168 | -1.265 | 0.2057 |  |
| **Site: UW (vs UAB)** | **-1.0831** | 0.2502 | ±0.5005 | **-4.328** | **1.50e-05** | *** |
| Season: spring (vs autumn) | -0.2652 | 0.2967 | ±0.5934 | -0.894 | 0.3715 |  |
| **Season: summer (vs autumn)** | **+1.7833** | 0.3501 | ±0.7002 | **+5.094** | **3.52e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5111** | 0.2922 | ±0.5843 | **-5.172** | **2.31e-07** | *** |
| Age (years) | +0.0065 | 0.0092 | ±0.0184 | +0.708 | 0.4786 |  |
| BMI (kg/m2) | +0.0183 | 0.0164 | ±0.0328 | +1.116 | 0.2646 |  |
| Hypertension | -0.1845 | 0.2340 | ±0.4680 | -0.788 | 0.4304 |  |
| High cholesterol | -0.3141 | 0.2185 | ±0.4371 | -1.437 | 0.1507 |  |
| **Kidney disease** | **+0.7692** | 0.3611 | ±0.7222 | **+2.130** | **0.0332** | * |
| Circulatory disease | +0.6551 | 0.3933 | ±0.7867 | +1.665 | 0.0958 | . |
| HbA1c (%) | +0.1643 | 0.3775 | ±0.7551 | +0.435 | 0.6635 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **384**, R² = **0.3432**, Adj R² = **0.3183**, F-statistic = **13.77** (p = **2.20e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.2**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8960** | 1.6177 | ±3.2355 | **+14.771** | **2.24e-49** | *** |
| Education: graduate level (vs college) | +0.0422 | 0.2062 | ±0.4123 | +0.205 | 0.8377 |  |
| Education: high school or below (vs college) | +0.3663 | 0.3897 | ±0.7795 | +0.940 | 0.3472 |  |
| Site: UCSD (vs UAB) | -0.3294 | 0.2584 | ±0.5168 | -1.275 | 0.2023 |  |
| **Site: UW (vs UAB)** | **-1.0891** | 0.2512 | ±0.5024 | **-4.336** | **1.45e-05** | *** |
| Season: spring (vs autumn) | -0.2849 | 0.2925 | ±0.5850 | -0.974 | 0.3300 |  |
| **Season: summer (vs autumn)** | **+1.7931** | 0.3513 | ±0.7026 | **+5.104** | **3.33e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5168** | 0.2922 | ±0.5843 | **-5.192** | **2.08e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0180 | +0.786 | 0.4316 |  |
| BMI (kg/m2) | +0.0187 | 0.0166 | ±0.0332 | +1.129 | 0.2590 |  |
| Hypertension | -0.1778 | 0.2322 | ±0.4645 | -0.766 | 0.4439 |  |
| High cholesterol | -0.2921 | 0.2068 | ±0.4136 | -1.412 | 0.1578 |  |
| **Kidney disease** | **+0.7532** | 0.3600 | ±0.7200 | **+2.092** | **0.0364** | * |
| Circulatory disease | +0.6417 | 0.3911 | ±0.7823 | +1.641 | 0.1009 |  |
| Mean glucose (mg/dL) | +0.0018 | 0.0122 | ±0.0243 | +0.150 | 0.8809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **384**, R² = **0.3432**, Adj R² = **0.3183**, F-statistic = **13.77** (p = **2.20e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.2**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6439** | 3.1706 | ±6.3411 | **+7.457** | **8.83e-14** | *** |
| Education: graduate level (vs college) | +0.0422 | 0.2062 | ±0.4123 | +0.205 | 0.8377 |  |
| Education: high school or below (vs college) | +0.3663 | 0.3897 | ±0.7795 | +0.940 | 0.3472 |  |
| Site: UCSD (vs UAB) | -0.3294 | 0.2584 | ±0.5168 | -1.275 | 0.2023 |  |
| **Site: UW (vs UAB)** | **-1.0891** | 0.2512 | ±0.5024 | **-4.336** | **1.45e-05** | *** |
| Season: spring (vs autumn) | -0.2849 | 0.2925 | ±0.5850 | -0.974 | 0.3300 |  |
| **Season: summer (vs autumn)** | **+1.7931** | 0.3513 | ±0.7026 | **+5.104** | **3.33e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5168** | 0.2922 | ±0.5843 | **-5.192** | **2.08e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0180 | +0.786 | 0.4316 |  |
| BMI (kg/m2) | +0.0187 | 0.0166 | ±0.0332 | +1.129 | 0.2590 |  |
| Hypertension | -0.1778 | 0.2322 | ±0.4645 | -0.766 | 0.4439 |  |
| High cholesterol | -0.2921 | 0.2068 | ±0.4136 | -1.412 | 0.1578 |  |
| **Kidney disease** | **+0.7532** | 0.3600 | ±0.7200 | **+2.092** | **0.0364** | * |
| Circulatory disease | +0.6417 | 0.3911 | ±0.7823 | +1.641 | 0.1009 |  |
| GMI (%) | +0.0762 | 0.5083 | ±1.0166 | +0.150 | 0.8809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **384**, R² = **0.3442**, Adj R² = **0.3193**, F-statistic = **13.83** (p = **1.70e-26**), Residual SE = **1.862** on **369** df, AIC = **1581.7**, BIC = **1640.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9906** | 1.4099 | ±2.8197 | **+17.726** | **2.66e-70** | *** |
| Education: graduate level (vs college) | +0.0367 | 0.2075 | ±0.4149 | +0.177 | 0.8595 |  |
| Education: high school or below (vs college) | +0.3528 | 0.3937 | ±0.7875 | +0.896 | 0.3703 |  |
| Site: UCSD (vs UAB) | -0.3080 | 0.2612 | ±0.5223 | -1.179 | 0.2382 |  |
| **Site: UW (vs UAB)** | **-1.0703** | 0.2523 | ±0.5045 | **-4.242** | **2.21e-05** | *** |
| Season: spring (vs autumn) | -0.2880 | 0.2934 | ±0.5868 | -0.982 | 0.3263 |  |
| **Season: summer (vs autumn)** | **+1.7988** | 0.3513 | ±0.7026 | **+5.120** | **3.05e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5174** | 0.2917 | ±0.5833 | **-5.202** | **1.97e-07** | *** |
| Age (years) | +0.0061 | 0.0091 | ±0.0183 | +0.666 | 0.5053 |  |
| BMI (kg/m2) | +0.0207 | 0.0173 | ±0.0347 | +1.191 | 0.2336 |  |
| Hypertension | -0.1690 | 0.2321 | ±0.4642 | -0.728 | 0.4665 |  |
| High cholesterol | -0.2945 | 0.2067 | ±0.4134 | -1.424 | 0.1543 |  |
| **Kidney disease** | **+0.7500** | 0.3584 | ±0.7167 | **+2.093** | **0.0364** | * |
| Circulatory disease | +0.6342 | 0.3898 | ±0.7797 | +1.627 | 0.1038 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0078 | 0.0098 | ±0.0195 | -0.795 | 0.4264 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **384**, R² = **0.3515**, Adj R² = **0.3269**, F-statistic = **14.29** (p = **2.45e-27**), Residual SE = **1.851** on **369** df, AIC = **1577.4**, BIC = **1636.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.6380** | 1.1050 | ±2.2100 | **+23.202** | **4.35e-119** | *** |
| Education: graduate level (vs college) | +0.0181 | 0.2063 | ±0.4125 | +0.088 | 0.9301 |  |
| Education: high school or below (vs college) | +0.3714 | 0.3855 | ±0.7711 | +0.963 | 0.3354 |  |
| Site: UCSD (vs UAB) | -0.3776 | 0.2543 | ±0.5086 | -1.485 | 0.1375 |  |
| **Site: UW (vs UAB)** | **-1.1176** | 0.2504 | ±0.5008 | **-4.464** | **8.06e-06** | *** |
| Season: spring (vs autumn) | -0.2422 | 0.2922 | ±0.5843 | -0.829 | 0.4071 |  |
| **Season: summer (vs autumn)** | **+1.8227** | 0.3467 | ±0.6935 | **+5.257** | **1.47e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4704** | 0.2907 | ±0.5814 | **-5.058** | **4.23e-07** | *** |
| Age (years) | +0.0072 | 0.0089 | ±0.0178 | +0.810 | 0.4179 |  |
| BMI (kg/m2) | +0.0202 | 0.0167 | ±0.0335 | +1.208 | 0.2271 |  |
| Hypertension | -0.1741 | 0.2313 | ±0.4626 | -0.753 | 0.4516 |  |
| High cholesterol | -0.3152 | 0.2062 | ±0.4124 | -1.529 | 0.1264 |  |
| **Kidney disease** | **+0.7940** | 0.3778 | ±0.7555 | **+2.102** | **0.0356** | * |
| Circulatory disease | +0.6594 | 0.3969 | ±0.7938 | +1.661 | 0.0966 | . |
| **Glucose SD, pooled (mg/dL)** | **-0.0940** | 0.0430 | ±0.0860 | **-2.186** | **0.0288** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **384**, R² = **0.3554**, Adj R² = **0.3309**, F-statistic = **14.53** (p = **8.64e-28**), Residual SE = **1.846** on **369** df, AIC = **1575.1**, BIC = **1634.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.7686** | 1.0834 | ±2.1668 | **+23.785** | **4.77e-125** | *** |
| Education: graduate level (vs college) | +0.0089 | 0.2058 | ±0.4115 | +0.043 | 0.9653 |  |
| Education: high school or below (vs college) | +0.3557 | 0.3933 | ±0.7865 | +0.905 | 0.3657 |  |
| Site: UCSD (vs UAB) | -0.3916 | 0.2531 | ±0.5062 | -1.547 | 0.1218 |  |
| **Site: UW (vs UAB)** | **-1.1257** | 0.2484 | ±0.4969 | **-4.531** | **5.87e-06** | *** |
| Season: spring (vs autumn) | -0.2412 | 0.2914 | ±0.5827 | -0.828 | 0.4078 |  |
| **Season: summer (vs autumn)** | **+1.8177** | 0.3462 | ±0.6925 | **+5.250** | **1.52e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4852** | 0.2862 | ±0.5724 | **-5.189** | **2.11e-07** | *** |
| Age (years) | +0.0072 | 0.0089 | ±0.0177 | +0.814 | 0.4155 |  |
| BMI (kg/m2) | +0.0219 | 0.0172 | ±0.0344 | +1.275 | 0.2024 |  |
| Hypertension | -0.1849 | 0.2312 | ±0.4624 | -0.800 | 0.4239 |  |
| High cholesterol | -0.3137 | 0.2059 | ±0.4117 | -1.524 | 0.1275 |  |
| **Kidney disease** | **+0.8032** | 0.3818 | ±0.7635 | **+2.104** | **0.0354** | * |
| Circulatory disease | +0.6464 | 0.3950 | ±0.7900 | +1.637 | 0.1017 |  |
| **Avg. daily SD (mg/dL)** | **-0.1127** | 0.0436 | ±0.0873 | **-2.583** | **0.0098** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **384**, R² = **0.3514**, Adj R² = **0.3268**, F-statistic = **14.28** (p = **2.50e-27**), Residual SE = **1.851** on **369** df, AIC = **1577.4**, BIC = **1636.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.5749** | 1.0817 | ±2.1634 | **+23.644** | **1.38e-123** | *** |
| Education: graduate level (vs college) | +0.0142 | 0.2061 | ±0.4122 | +0.069 | 0.9450 |  |
| Education: high school or below (vs college) | +0.3790 | 0.3817 | ±0.7634 | +0.993 | 0.3207 |  |
| Site: UCSD (vs UAB) | -0.3879 | 0.2549 | ±0.5098 | -1.522 | 0.1280 |  |
| **Site: UW (vs UAB)** | **-1.1322** | 0.2504 | ±0.5008 | **-4.522** | **6.13e-06** | *** |
| Season: spring (vs autumn) | -0.2315 | 0.2916 | ±0.5832 | -0.794 | 0.4272 |  |
| **Season: summer (vs autumn)** | **+1.8241** | 0.3470 | ±0.6940 | **+5.256** | **1.47e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4664** | 0.2913 | ±0.5825 | **-5.035** | **4.79e-07** | *** |
| Age (years) | +0.0075 | 0.0089 | ±0.0178 | +0.842 | 0.3996 |  |
| BMI (kg/m2) | +0.0192 | 0.0166 | ±0.0333 | +1.152 | 0.2493 |  |
| Hypertension | -0.1894 | 0.2317 | ±0.4634 | -0.817 | 0.4138 |  |
| High cholesterol | -0.3069 | 0.2069 | ±0.4139 | -1.483 | 0.1381 |  |
| **Kidney disease** | **+0.7751** | 0.3763 | ±0.7527 | **+2.059** | **0.0395** | * |
| Circulatory disease | +0.6655 | 0.3978 | ±0.7957 | +1.673 | 0.0944 | . |
| **CV (%)** | **-0.1015** | 0.0459 | ±0.0917 | **-2.212** | **0.0270** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **384**, R² = **0.3501**, Adj R² = **0.3255**, F-statistic = **14.20** (p = **3.52e-27**), Residual SE = **1.853** on **369** df, AIC = **1578.2**, BIC = **1637.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.7636** | 1.0808 | ±2.1616 | **+21.061** | **1.79e-98** | *** |
| Education: graduate level (vs college) | +0.0131 | 0.2059 | ±0.4118 | +0.064 | 0.9493 |  |
| Education: high school or below (vs college) | +0.3783 | 0.3829 | ±0.7657 | +0.988 | 0.3231 |  |
| Site: UCSD (vs UAB) | -0.3735 | 0.2547 | ±0.5094 | -1.466 | 0.1426 |  |
| **Site: UW (vs UAB)** | **-1.1197** | 0.2497 | ±0.4995 | **-4.483** | **7.36e-06** | *** |
| Season: spring (vs autumn) | -0.2325 | 0.2922 | ±0.5844 | -0.796 | 0.4262 |  |
| **Season: summer (vs autumn)** | **+1.8185** | 0.3477 | ±0.6955 | **+5.229** | **1.70e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4710** | 0.2916 | ±0.5831 | **-5.045** | **4.53e-07** | *** |
| Age (years) | +0.0073 | 0.0089 | ±0.0178 | +0.817 | 0.4139 |  |
| BMI (kg/m2) | +0.0191 | 0.0165 | ±0.0330 | +1.155 | 0.2482 |  |
| Hypertension | -0.1810 | 0.2314 | ±0.4627 | -0.782 | 0.4341 |  |
| High cholesterol | -0.3067 | 0.2069 | ±0.4139 | -1.482 | 0.1383 |  |
| **Kidney disease** | **+0.7636** | 0.3734 | ±0.7469 | **+2.045** | **0.0409** | * |
| Circulatory disease | +0.6615 | 0.3974 | ±0.7948 | +1.665 | 0.0960 | . |
| **Mean / SD ratio** | **+0.1913** | 0.0922 | ±0.1844 | **+2.075** | **0.0380** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **384**, R² = **0.3534**, Adj R² = **0.3289**, F-statistic = **14.41** (p = **1.47e-27**), Residual SE = **1.848** on **369** df, AIC = **1576.2**, BIC = **1635.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.5856** | 1.0579 | ±2.1158 | **+21.350** | **3.92e-101** | *** |
| Education: graduate level (vs college) | +0.0022 | 0.2059 | ±0.4117 | +0.011 | 0.9914 |  |
| Education: high school or below (vs college) | +0.3665 | 0.3883 | ±0.7766 | +0.944 | 0.3452 |  |
| Site: UCSD (vs UAB) | -0.3873 | 0.2535 | ±0.5070 | -1.528 | 0.1266 |  |
| **Site: UW (vs UAB)** | **-1.1242** | 0.2475 | ±0.4950 | **-4.542** | **5.57e-06** | *** |
| Season: spring (vs autumn) | -0.2223 | 0.2924 | ±0.5847 | -0.760 | 0.4471 |  |
| **Season: summer (vs autumn)** | **+1.8189** | 0.3473 | ±0.6946 | **+5.237** | **1.63e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4772** | 0.2880 | ±0.5760 | **-5.129** | **2.91e-07** | *** |
| Age (years) | +0.0074 | 0.0088 | ±0.0177 | +0.833 | 0.4051 |  |
| BMI (kg/m2) | +0.0211 | 0.0169 | ±0.0337 | +1.251 | 0.2110 |  |
| Hypertension | -0.1959 | 0.2307 | ±0.4613 | -0.849 | 0.3957 |  |
| High cholesterol | -0.3023 | 0.2067 | ±0.4135 | -1.462 | 0.1436 |  |
| **Kidney disease** | **+0.7749** | 0.3742 | ±0.7484 | **+2.071** | **0.0384** | * |
| Circulatory disease | +0.6523 | 0.3930 | ±0.7859 | +1.660 | 0.0969 | . |
| **Avg. daily mean/SD** | **+0.1861** | 0.0747 | ±0.1494 | **+2.492** | **0.0127** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **384**, R² = **0.3467**, Adj R² = **0.3219**, F-statistic = **13.99** (p = **8.73e-27**), Residual SE = **1.858** on **369** df, AIC = **1580.2**, BIC = **1639.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0548** | 1.1100 | ±2.2201 | **+22.571** | **8.33e-113** | *** |
| Education: graduate level (vs college) | +0.0500 | 0.2059 | ±0.4118 | +0.243 | 0.8082 |  |
| Education: high school or below (vs college) | +0.4047 | 0.3941 | ±0.7882 | +1.027 | 0.3044 |  |
| Site: UCSD (vs UAB) | -0.3548 | 0.2583 | ±0.5166 | -1.374 | 0.1695 |  |
| **Site: UW (vs UAB)** | **-1.1307** | 0.2532 | ±0.5063 | **-4.466** | **7.96e-06** | *** |
| Season: spring (vs autumn) | -0.2679 | 0.2927 | ±0.5855 | -0.915 | 0.3601 |  |
| **Season: summer (vs autumn)** | **+1.7912** | 0.3519 | ±0.7039 | **+5.090** | **3.59e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4979** | 0.2920 | ±0.5841 | **-5.129** | **2.91e-07** | *** |
| Age (years) | +0.0054 | 0.0090 | ±0.0181 | +0.597 | 0.5506 |  |
| BMI (kg/m2) | +0.0175 | 0.0168 | ±0.0336 | +1.039 | 0.2990 |  |
| Hypertension | -0.1867 | 0.2313 | ±0.4625 | -0.807 | 0.4194 |  |
| High cholesterol | -0.2766 | 0.2082 | ±0.4165 | -1.328 | 0.1840 |  |
| **Kidney disease** | **+0.7858** | 0.3659 | ±0.7318 | **+2.148** | **0.0318** | * |
| Circulatory disease | +0.6407 | 0.3912 | ±0.7825 | +1.638 | 0.1015 |  |
| MAG (mg/dL/h) | -0.0237 | 0.0170 | ±0.0340 | -1.394 | 0.1633 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **384**, R² = **0.3571**, Adj R² = **0.3327**, F-statistic = **14.64** (p = **5.36e-28**), Residual SE = **1.843** on **369** df, AIC = **1574.0**, BIC = **1633.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.2030** | 1.1181 | ±2.2362 | **+23.435** | **1.88e-121** | *** |
| Education: graduate level (vs college) | +0.0339 | 0.2038 | ±0.4076 | +0.166 | 0.8681 |  |
| Education: high school or below (vs college) | +0.3656 | 0.4001 | ±0.8003 | +0.914 | 0.3609 |  |
| Site: UCSD (vs UAB) | -0.3924 | 0.2531 | ±0.5061 | -1.551 | 0.1210 |  |
| **Site: UW (vs UAB)** | **-1.1333** | 0.2485 | ±0.4970 | **-4.561** | **5.10e-06** | *** |
| Season: spring (vs autumn) | -0.2340 | 0.2905 | ±0.5809 | -0.805 | 0.4206 |  |
| **Season: summer (vs autumn)** | **+1.8135** | 0.3469 | ±0.6938 | **+5.227** | **1.72e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4677** | 0.2862 | ±0.5724 | **-5.128** | **2.92e-07** | *** |
| Age (years) | +0.0066 | 0.0088 | ±0.0175 | +0.750 | 0.4531 |  |
| BMI (kg/m2) | +0.0159 | 0.0158 | ±0.0316 | +1.005 | 0.3149 |  |
| Hypertension | -0.2055 | 0.2314 | ±0.4628 | -0.888 | 0.3746 |  |
| High cholesterol | -0.2878 | 0.2056 | ±0.4112 | -1.400 | 0.1616 |  |
| **Kidney disease** | **+0.7850** | 0.3776 | ±0.7551 | **+2.079** | **0.0376** | * |
| Circulatory disease | +0.6590 | 0.3925 | ±0.7851 | +1.679 | 0.0932 | . |
| **Avg. daily range (mg/dL)** | **-0.0248** | 0.0088 | ±0.0177 | **-2.800** | **0.0051** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **384**, R² = **0.3474**, Adj R² = **0.3227**, F-statistic = **14.03** (p = **7.24e-27**), Residual SE = **1.857** on **369** df, AIC = **1579.8**, BIC = **1639.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7368** | 0.8851 | ±1.7703 | **+26.817** | **2.05e-158** | *** |
| Education: graduate level (vs college) | +0.0295 | 0.2055 | ±0.4110 | +0.144 | 0.8857 |  |
| Education: high school or below (vs college) | +0.3310 | 0.3947 | ±0.7894 | +0.839 | 0.4017 |  |
| Site: UCSD (vs UAB) | -0.3179 | 0.2562 | ±0.5124 | -1.241 | 0.2147 |  |
| **Site: UW (vs UAB)** | **-1.1024** | 0.2495 | ±0.4990 | **-4.419** | **9.94e-06** | *** |
| Season: spring (vs autumn) | -0.3153 | 0.2918 | ±0.5836 | -1.081 | 0.2799 |  |
| **Season: summer (vs autumn)** | **+1.7619** | 0.3517 | ±0.7035 | **+5.009** | **5.46e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5618** | 0.2920 | ±0.5840 | **-5.348** | **8.88e-08** | *** |
| Age (years) | +0.0068 | 0.0089 | ±0.0179 | +0.760 | 0.4471 |  |
| BMI (kg/m2) | +0.0188 | 0.0164 | ±0.0327 | +1.147 | 0.2515 |  |
| Hypertension | -0.1963 | 0.2321 | ±0.4643 | -0.846 | 0.3977 |  |
| High cholesterol | -0.2997 | 0.2065 | ±0.4130 | -1.451 | 0.1467 |  |
| **Kidney disease** | **+0.7920** | 0.3668 | ±0.7336 | **+2.159** | **0.0308** | * |
| Circulatory disease | +0.6134 | 0.3869 | ±0.7738 | +1.585 | 0.1129 |  |
| SD of daily means (mg/dL) | +0.0851 | 0.0516 | ±0.1032 | +1.649 | 0.0991 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **384**, R² = **0.3460**, Adj R² = **0.3212**, F-statistic = **13.94** (p = **1.06e-26**), Residual SE = **1.859** on **369** df, AIC = **1580.6**, BIC = **1639.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -16.4064 | 32.9168 | ±65.8336 | -0.498 | 0.6182 |  |
| Education: graduate level (vs college) | +0.0424 | 0.2062 | ±0.4124 | +0.206 | 0.8370 |  |
| Education: high school or below (vs college) | +0.3687 | 0.3907 | ±0.7814 | +0.944 | 0.3453 |  |
| Site: UCSD (vs UAB) | -0.3494 | 0.2568 | ±0.5136 | -1.360 | 0.1737 |  |
| **Site: UW (vs UAB)** | **-1.1023** | 0.2518 | ±0.5035 | **-4.378** | **1.20e-05** | *** |
| Season: spring (vs autumn) | -0.2703 | 0.2954 | ±0.5908 | -0.915 | 0.3602 |  |
| **Season: summer (vs autumn)** | **+1.8172** | 0.3548 | ±0.7096 | **+5.122** | **3.03e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4944** | 0.2934 | ±0.5868 | **-5.093** | **3.52e-07** | *** |
| Age (years) | +0.0066 | 0.0090 | ±0.0179 | +0.738 | 0.4608 |  |
| BMI (kg/m2) | +0.0178 | 0.0160 | ±0.0319 | +1.115 | 0.2649 |  |
| Hypertension | -0.1768 | 0.2329 | ±0.4659 | -0.759 | 0.4478 |  |
| High cholesterol | -0.2815 | 0.2086 | ±0.4172 | -1.350 | 0.1771 |  |
| **Kidney disease** | **+0.7754** | 0.3711 | ±0.7422 | **+2.089** | **0.0367** | * |
| Circulatory disease | +0.6500 | 0.3958 | ±0.7916 | +1.642 | 0.1005 |  |
| Time in range 70-180, pooled (%) | +0.4074 | 0.3305 | ±0.6609 | +1.233 | 0.2177 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **384**, R² = **0.3445**, Adj R² = **0.3196**, F-statistic = **13.85** (p = **1.57e-26**), Residual SE = **1.861** on **369** df, AIC = **1581.5**, BIC = **1640.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.6805 | 32.5214 | ±65.0428 | -0.082 | 0.9343 |  |
| Education: graduate level (vs college) | +0.0425 | 0.2066 | ±0.4132 | +0.206 | 0.8369 |  |
| Education: high school or below (vs college) | +0.3631 | 0.3911 | ±0.7822 | +0.928 | 0.3532 |  |
| Site: UCSD (vs UAB) | -0.3380 | 0.2572 | ±0.5144 | -1.314 | 0.1888 |  |
| **Site: UW (vs UAB)** | **-1.0896** | 0.2509 | ±0.5018 | **-4.343** | **1.41e-05** | *** |
| Season: spring (vs autumn) | -0.2785 | 0.2950 | ±0.5900 | -0.944 | 0.3452 |  |
| **Season: summer (vs autumn)** | **+1.7986** | 0.3531 | ±0.7062 | **+5.094** | **3.51e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5053** | 0.2937 | ±0.5873 | **-5.126** | **2.96e-07** | *** |
| Age (years) | +0.0065 | 0.0090 | ±0.0181 | +0.715 | 0.4744 |  |
| BMI (kg/m2) | +0.0186 | 0.0165 | ±0.0330 | +1.127 | 0.2596 |  |
| Hypertension | -0.1834 | 0.2337 | ±0.4674 | -0.785 | 0.4326 |  |
| High cholesterol | -0.2831 | 0.2097 | ±0.4194 | -1.350 | 0.1770 |  |
| **Kidney disease** | **+0.7583** | 0.3703 | ±0.7405 | **+2.048** | **0.0406** | * |
| Circulatory disease | +0.6528 | 0.3970 | ±0.7939 | +1.644 | 0.1001 |  |
| Avg. daily time in range 70-180 (%) | +0.2693 | 0.3265 | ±0.6530 | +0.825 | 0.4095 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.3435**, Adj R² = **0.3186**, F-statistic = **13.79** (p = **2.04e-26**), Residual SE = **1.862** on **369** df, AIC = **1582.1**, BIC = **1641.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1212** | 0.8658 | ±1.7316 | **+27.861** | **8.01e-171** | *** |
| Education: graduate level (vs college) | +0.0412 | 0.2061 | ±0.4123 | +0.200 | 0.8414 |  |
| Education: high school or below (vs college) | +0.3631 | 0.3885 | ±0.7770 | +0.934 | 0.3500 |  |
| Site: UCSD (vs UAB) | -0.3470 | 0.2651 | ±0.5302 | -1.309 | 0.1907 |  |
| **Site: UW (vs UAB)** | **-1.0994** | 0.2571 | ±0.5143 | **-4.276** | **1.91e-05** | *** |
| Season: spring (vs autumn) | -0.2721 | 0.2951 | ±0.5903 | -0.922 | 0.3566 |  |
| **Season: summer (vs autumn)** | **+1.8005** | 0.3498 | ±0.6997 | **+5.147** | **2.65e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5076** | 0.2930 | ±0.5861 | **-5.145** | **2.68e-07** | *** |
| Age (years) | +0.0070 | 0.0090 | ±0.0180 | +0.784 | 0.4332 |  |
| BMI (kg/m2) | +0.0189 | 0.0166 | ±0.0332 | +1.136 | 0.2559 |  |
| Hypertension | -0.1684 | 0.2294 | ±0.4589 | -0.734 | 0.4631 |  |
| High cholesterol | -0.2935 | 0.2074 | ±0.4149 | -1.415 | 0.1571 |  |
| **Kidney disease** | **+0.7435** | 0.3614 | ±0.7228 | **+2.057** | **0.0397** | * |
| Circulatory disease | +0.6474 | 0.3931 | ±0.7862 | +1.647 | 0.0996 | . |
| Any reading < 54 during wear (0/1) | -0.1117 | 0.2839 | ±0.5678 | -0.393 | 0.6941 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.3432**, Adj R² = **0.3183**, F-statistic = **13.77** (p = **2.20e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.2**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0965** | 0.8626 | ±1.7253 | **+27.933** | **1.05e-171** | *** |
| Education: graduate level (vs college) | +0.0431 | 0.2069 | ±0.4137 | +0.208 | 0.8349 |  |
| Education: high school or below (vs college) | +0.3676 | 0.3890 | ±0.7780 | +0.945 | 0.3446 |  |
| Site: UCSD (vs UAB) | -0.3235 | 0.2601 | ±0.5201 | -1.244 | 0.2135 |  |
| **Site: UW (vs UAB)** | **-1.0848** | 0.2523 | ±0.5046 | **-4.299** | **1.71e-05** | *** |
| Season: spring (vs autumn) | -0.2861 | 0.2941 | ±0.5881 | -0.973 | 0.3307 |  |
| **Season: summer (vs autumn)** | **+1.7930** | 0.3522 | ±0.7045 | **+5.090** | **3.58e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5174** | 0.2925 | ±0.5849 | **-5.188** | **2.12e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0180 | +0.787 | 0.4312 |  |
| BMI (kg/m2) | +0.0188 | 0.0166 | ±0.0332 | +1.129 | 0.2587 |  |
| Hypertension | -0.1778 | 0.2305 | ±0.4611 | -0.771 | 0.4406 |  |
| High cholesterol | -0.2930 | 0.2074 | ±0.4147 | -1.413 | 0.1576 |  |
| **Kidney disease** | **+0.7576** | 0.3605 | ±0.7209 | **+2.102** | **0.0356** | * |
| Circulatory disease | +0.6385 | 0.3921 | ±0.7842 | +1.628 | 0.1035 |  |
| Time < 54 (%) | +0.2422 | 2.1258 | ±4.2515 | +0.114 | 0.9093 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.3432**, Adj R² = **0.3183**, F-statistic = **13.77** (p = **2.19e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.2**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0965** | 0.8627 | ±1.7254 | **+27.931** | **1.12e-171** | *** |
| Education: graduate level (vs college) | +0.0421 | 0.2074 | ±0.4148 | +0.203 | 0.8393 |  |
| Education: high school or below (vs college) | +0.3664 | 0.3891 | ±0.7781 | +0.942 | 0.3463 |  |
| Site: UCSD (vs UAB) | -0.3247 | 0.2589 | ±0.5179 | -1.254 | 0.2098 |  |
| **Site: UW (vs UAB)** | **-1.0858** | 0.2515 | ±0.5031 | **-4.316** | **1.59e-05** | *** |
| Season: spring (vs autumn) | -0.2856 | 0.2946 | ±0.5892 | -0.969 | 0.3323 |  |
| **Season: summer (vs autumn)** | **+1.7965** | 0.3516 | ±0.7033 | **+5.109** | **3.23e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5169** | 0.2929 | ±0.5858 | **-5.179** | **2.23e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0180 | +0.787 | 0.4315 |  |
| BMI (kg/m2) | +0.0188 | 0.0166 | ±0.0331 | +1.136 | 0.2562 |  |
| Hypertension | -0.1772 | 0.2322 | ±0.4645 | -0.763 | 0.4454 |  |
| High cholesterol | -0.2928 | 0.2071 | ±0.4142 | -1.414 | 0.1574 |  |
| **Kidney disease** | **+0.7563** | 0.3602 | ±0.7204 | **+2.100** | **0.0358** | * |
| Circulatory disease | +0.6367 | 0.3931 | ±0.7862 | +1.620 | 0.1053 |  |
| Avg. daily time < 54 (%) | +0.3578 | 2.7475 | ±5.4949 | +0.130 | 0.8964 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.3473**, Adj R² = **0.3225**, F-statistic = **14.02** (p = **7.54e-27**), Residual SE = **1.857** on **369** df, AIC = **1579.9**, BIC = **1639.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.2269** | 0.8680 | ±1.7360 | **+27.911** | **1.98e-171** | *** |
| Education: graduate level (vs college) | +0.0327 | 0.2060 | ±0.4121 | +0.159 | 0.8739 |  |
| Education: high school or below (vs college) | +0.3876 | 0.3864 | ±0.7728 | +1.003 | 0.3158 |  |
| Site: UCSD (vs UAB) | -0.3570 | 0.2588 | ±0.5176 | -1.379 | 0.1678 |  |
| **Site: UW (vs UAB)** | **-1.1215** | 0.2503 | ±0.5007 | **-4.480** | **7.47e-06** | *** |
| Season: spring (vs autumn) | -0.2707 | 0.2953 | ±0.5905 | -0.917 | 0.3592 |  |
| **Season: summer (vs autumn)** | **+1.7988** | 0.3532 | ±0.7064 | **+5.093** | **3.52e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4925** | 0.2942 | ±0.5884 | **-5.073** | **3.91e-07** | *** |
| Age (years) | +0.0072 | 0.0090 | ±0.0179 | +0.803 | 0.4222 |  |
| BMI (kg/m2) | +0.0185 | 0.0168 | ±0.0336 | +1.101 | 0.2708 |  |
| Hypertension | -0.2056 | 0.2335 | ±0.4671 | -0.880 | 0.3788 |  |
| High cholesterol | -0.2618 | 0.2065 | ±0.4130 | -1.268 | 0.2049 |  |
| Kidney disease | +0.7026 | 0.3643 | ±0.7286 | +1.928 | 0.0538 | . |
| Circulatory disease | +0.6442 | 0.3921 | ±0.7841 | +1.643 | 0.1004 |  |
| Time 54-69, pooled (%) | -0.8235 | 0.5593 | ±1.1186 | -1.472 | 0.1409 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **384**, R² = **0.3457**, Adj R² = **0.3208**, F-statistic = **13.92** (p = **1.15e-26**), Residual SE = **1.859** on **369** df, AIC = **1580.8**, BIC = **1640.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1953** | 0.8637 | ±1.7275 | **+28.012** | **1.16e-172** | *** |
| Education: graduate level (vs college) | +0.0316 | 0.2066 | ±0.4132 | +0.153 | 0.8784 |  |
| Education: high school or below (vs college) | +0.3857 | 0.3860 | ±0.7719 | +0.999 | 0.3176 |  |
| Site: UCSD (vs UAB) | -0.3407 | 0.2577 | ±0.5153 | -1.322 | 0.1861 |  |
| **Site: UW (vs UAB)** | **-1.1003** | 0.2492 | ±0.4985 | **-4.414** | **1.01e-05** | *** |
| Season: spring (vs autumn) | -0.2913 | 0.2936 | ±0.5871 | -0.992 | 0.3210 |  |
| **Season: summer (vs autumn)** | **+1.7823** | 0.3520 | ±0.7039 | **+5.064** | **4.11e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5042** | 0.2941 | ±0.5882 | **-5.115** | **3.14e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0179 | +0.797 | 0.4255 |  |
| BMI (kg/m2) | +0.0186 | 0.0167 | ±0.0333 | +1.119 | 0.2629 |  |
| Hypertension | -0.2134 | 0.2339 | ±0.4678 | -0.912 | 0.3616 |  |
| High cholesterol | -0.2754 | 0.2079 | ±0.4159 | -1.324 | 0.1854 |  |
| **Kidney disease** | **+0.7263** | 0.3644 | ±0.7287 | **+1.993** | **0.0462** | * |
| Circulatory disease | +0.6509 | 0.3922 | ±0.7844 | +1.660 | 0.0970 | . |
| Avg. daily time 54-69 (%) | -0.6462 | 0.5429 | ±1.0857 | -1.190 | 0.2339 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **384**, R² = **0.3463**, Adj R² = **0.3215**, F-statistic = **13.96** (p = **9.79e-27**), Residual SE = **1.859** on **369** df, AIC = **1580.4**, BIC = **1639.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.2129** | 0.8698 | ±1.7396 | **+27.837** | **1.56e-170** | *** |
| Education: graduate level (vs college) | +0.0345 | 0.2063 | ±0.4126 | +0.167 | 0.8672 |  |
| Education: high school or below (vs college) | +0.3764 | 0.3864 | ±0.7728 | +0.974 | 0.3300 |  |
| Site: UCSD (vs UAB) | -0.3612 | 0.2591 | ±0.5182 | -1.394 | 0.1633 |  |
| **Site: UW (vs UAB)** | **-1.1192** | 0.2515 | ±0.5030 | **-4.450** | **8.60e-06** | *** |
| Season: spring (vs autumn) | -0.2757 | 0.2952 | ±0.5904 | -0.934 | 0.3503 |  |
| **Season: summer (vs autumn)** | **+1.7983** | 0.3534 | ±0.7068 | **+5.088** | **3.61e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4986** | 0.2941 | ±0.5881 | **-5.096** | **3.46e-07** | *** |
| Age (years) | +0.0070 | 0.0090 | ±0.0180 | +0.782 | 0.4341 |  |
| BMI (kg/m2) | +0.0189 | 0.0168 | ±0.0337 | +1.122 | 0.2617 |  |
| Hypertension | -0.1934 | 0.2337 | ±0.4674 | -0.828 | 0.4079 |  |
| High cholesterol | -0.2696 | 0.2068 | ±0.4135 | -1.304 | 0.1923 |  |
| Kidney disease | +0.7083 | 0.3637 | ±0.7275 | +1.947 | 0.0515 | . |
| Circulatory disease | +0.6500 | 0.3929 | ±0.7857 | +1.655 | 0.0980 | . |
| Time < 70 (%) | -0.6397 | 0.5008 | ±1.0017 | -1.277 | 0.2015 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **384**, R² = **0.3451**, Adj R² = **0.3203**, F-statistic = **13.89** (p = **1.34e-26**), Residual SE = **1.860** on **369** df, AIC = **1581.1**, BIC = **1640.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1838** | 0.8646 | ±1.7293 | **+27.970** | **3.74e-172** | *** |
| Education: graduate level (vs college) | +0.0352 | 0.2067 | ±0.4134 | +0.170 | 0.8649 |  |
| Education: high school or below (vs college) | +0.3798 | 0.3868 | ±0.7737 | +0.982 | 0.3262 |  |
| Site: UCSD (vs UAB) | -0.3421 | 0.2577 | ±0.5154 | -1.328 | 0.1843 |  |
| **Site: UW (vs UAB)** | **-1.0991** | 0.2498 | ±0.4995 | **-4.401** | **1.08e-05** | *** |
| Season: spring (vs autumn) | -0.2918 | 0.2937 | ±0.5875 | -0.994 | 0.3204 |  |
| **Season: summer (vs autumn)** | **+1.7798** | 0.3521 | ±0.7042 | **+5.055** | **4.30e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5080** | 0.2937 | ±0.5873 | **-5.135** | **2.82e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0180 | +0.785 | 0.4325 |  |
| BMI (kg/m2) | +0.0188 | 0.0167 | ±0.0333 | +1.129 | 0.2590 |  |
| Hypertension | -0.2034 | 0.2339 | ±0.4679 | -0.870 | 0.3845 |  |
| High cholesterol | -0.2798 | 0.2081 | ±0.4161 | -1.345 | 0.1787 |  |
| **Kidney disease** | **+0.7308** | 0.3642 | ±0.7284 | **+2.007** | **0.0448** | * |
| Circulatory disease | +0.6549 | 0.3930 | ±0.7859 | +1.667 | 0.0956 | . |
| Avg. daily time < 70 (%) | -0.5138 | 0.4878 | ±0.9757 | -1.053 | 0.2922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.3432**, Adj R² = **0.3183**, F-statistic = **13.77** (p = **2.21e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.3**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +42.0935 | 211.8386 | ±423.6772 | +0.199 | 0.8425 |  |
| Education: graduate level (vs college) | +0.0432 | 0.2068 | ±0.4136 | +0.209 | 0.8345 |  |
| Education: high school or below (vs college) | +0.3671 | 0.3890 | ±0.7779 | +0.944 | 0.3453 |  |
| Site: UCSD (vs UAB) | -0.3245 | 0.2600 | ±0.5200 | -1.248 | 0.2120 |  |
| **Site: UW (vs UAB)** | **-1.0855** | 0.2522 | ±0.5044 | **-4.304** | **1.68e-05** | *** |
| Season: spring (vs autumn) | -0.2862 | 0.2941 | ±0.5882 | -0.973 | 0.3305 |  |
| **Season: summer (vs autumn)** | **+1.7931** | 0.3523 | ±0.7046 | **+5.090** | **3.59e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5176** | 0.2925 | ±0.5851 | **-5.188** | **2.13e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0180 | +0.786 | 0.4319 |  |
| BMI (kg/m2) | +0.0188 | 0.0166 | ±0.0332 | +1.132 | 0.2576 |  |
| Hypertension | -0.1772 | 0.2305 | ±0.4611 | -0.769 | 0.4422 |  |
| High cholesterol | -0.2933 | 0.2073 | ±0.4146 | -1.415 | 0.1572 |  |
| **Kidney disease** | **+0.7570** | 0.3605 | ±0.7210 | **+2.100** | **0.0357** | * |
| Circulatory disease | +0.6391 | 0.3921 | ±0.7842 | +1.630 | 0.1031 |  |
| Time 54-250, pooled (%) | -0.1800 | 2.1187 | ±4.2374 | -0.085 | 0.9323 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.3432**, Adj R² = **0.3183**, F-statistic = **13.77** (p = **2.20e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.2**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +49.6526 | 273.3871 | ±546.7742 | +0.182 | 0.8559 |  |
| Education: graduate level (vs college) | +0.0425 | 0.2073 | ±0.4146 | +0.205 | 0.8375 |  |
| Education: high school or below (vs college) | +0.3663 | 0.3890 | ±0.7781 | +0.941 | 0.3465 |  |
| Site: UCSD (vs UAB) | -0.3255 | 0.2589 | ±0.5178 | -1.257 | 0.2086 |  |
| **Site: UW (vs UAB)** | **-1.0862** | 0.2515 | ±0.5031 | **-4.318** | **1.57e-05** | *** |
| Season: spring (vs autumn) | -0.2859 | 0.2946 | ±0.5893 | -0.970 | 0.3319 |  |
| **Season: summer (vs autumn)** | **+1.7956** | 0.3516 | ±0.7033 | **+5.106** | **3.28e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5173** | 0.2930 | ±0.5860 | **-5.178** | **2.24e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0180 | +0.786 | 0.4319 |  |
| BMI (kg/m2) | +0.0188 | 0.0166 | ±0.0331 | +1.138 | 0.2553 |  |
| Hypertension | -0.1767 | 0.2323 | ±0.4645 | -0.761 | 0.4467 |  |
| High cholesterol | -0.2932 | 0.2072 | ±0.4145 | -1.415 | 0.1571 |  |
| **Kidney disease** | **+0.7561** | 0.3603 | ±0.7206 | **+2.098** | **0.0359** | * |
| Circulatory disease | +0.6380 | 0.3931 | ±0.7862 | +1.623 | 0.1046 |  |
| Avg. daily time 54-250 (%) | -0.2556 | 2.7341 | ±5.4682 | -0.093 | 0.9255 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **384**, R² = **0.3435**, Adj R² = **0.3186**, F-statistic = **13.79** (p = **2.06e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.1**, BIC = **1641.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1541** | 0.8657 | ±1.7313 | **+27.903** | **2.48e-171** | *** |
| Education: graduate level (vs college) | +0.0446 | 0.2063 | ±0.4125 | +0.216 | 0.8287 |  |
| Education: high school or below (vs college) | +0.3641 | 0.3914 | ±0.7827 | +0.930 | 0.3521 |  |
| Site: UCSD (vs UAB) | -0.3277 | 0.2577 | ±0.5153 | -1.272 | 0.2035 |  |
| **Site: UW (vs UAB)** | **-1.0853** | 0.2508 | ±0.5016 | **-4.327** | **1.51e-05** | *** |
| Season: spring (vs autumn) | -0.2835 | 0.2944 | ±0.5888 | -0.963 | 0.3355 |  |
| **Season: summer (vs autumn)** | **+1.8001** | 0.3540 | ±0.7080 | **+5.085** | **3.67e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5140** | 0.2925 | ±0.5850 | **-5.176** | **2.27e-07** | *** |
| Age (years) | +0.0069 | 0.0090 | ±0.0180 | +0.766 | 0.4437 |  |
| BMI (kg/m2) | +0.0185 | 0.0164 | ±0.0328 | +1.130 | 0.2584 |  |
| Hypertension | -0.1723 | 0.2311 | ±0.4622 | -0.746 | 0.4559 |  |
| High cholesterol | -0.2945 | 0.2066 | ±0.4132 | -1.426 | 0.1540 |  |
| **Kidney disease** | **+0.7718** | 0.3632 | ±0.7265 | **+2.125** | **0.0336** | * |
| Circulatory disease | +0.6420 | 0.3924 | ±0.7848 | +1.636 | 0.1018 |  |
| Time 181-250, pooled (%) | -0.1339 | 0.3512 | ±0.7023 | -0.381 | 0.7030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **384**, R² = **0.3433**, Adj R² = **0.3183**, F-statistic = **13.78** (p = **2.17e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.2**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1276** | 0.8703 | ±1.7405 | **+27.724** | **3.55e-169** | *** |
| Education: graduate level (vs college) | +0.0439 | 0.2063 | ±0.4127 | +0.213 | 0.8314 |  |
| Education: high school or below (vs college) | +0.3627 | 0.3915 | ±0.7830 | +0.927 | 0.3542 |  |
| Site: UCSD (vs UAB) | -0.3283 | 0.2579 | ±0.5158 | -1.273 | 0.2031 |  |
| **Site: UW (vs UAB)** | **-1.0860** | 0.2507 | ±0.5014 | **-4.332** | **1.48e-05** | *** |
| Season: spring (vs autumn) | -0.2838 | 0.2954 | ±0.5907 | -0.961 | 0.3367 |  |
| **Season: summer (vs autumn)** | **+1.7965** | 0.3532 | ±0.7063 | **+5.087** | **3.64e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5158** | 0.2926 | ±0.5853 | **-5.180** | **2.22e-07** | *** |
| Age (years) | +0.0069 | 0.0091 | ±0.0182 | +0.759 | 0.4478 |  |
| BMI (kg/m2) | +0.0188 | 0.0165 | ±0.0330 | +1.139 | 0.2546 |  |
| Hypertension | -0.1739 | 0.2316 | ±0.4632 | -0.751 | 0.4528 |  |
| High cholesterol | -0.2926 | 0.2080 | ±0.4160 | -1.407 | 0.1595 |  |
| **Kidney disease** | **+0.7594** | 0.3631 | ±0.7263 | **+2.091** | **0.0365** | * |
| Circulatory disease | +0.6421 | 0.3930 | ±0.7859 | +1.634 | 0.1022 |  |
| Avg. daily time 181-250 (%) | -0.0700 | 0.3504 | ±0.7008 | -0.200 | 0.8416 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **384**, R² = **0.3435**, Adj R² = **0.3186**, F-statistic = **13.79** (p = **2.06e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.1**, BIC = **1641.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1552** | 0.8658 | ±1.7316 | **+27.899** | **2.75e-171** | *** |
| Education: graduate level (vs college) | +0.0445 | 0.2063 | ±0.4125 | +0.216 | 0.8290 |  |
| Education: high school or below (vs college) | +0.3640 | 0.3914 | ±0.7828 | +0.930 | 0.3523 |  |
| Site: UCSD (vs UAB) | -0.3277 | 0.2577 | ±0.5153 | -1.272 | 0.2034 |  |
| **Site: UW (vs UAB)** | **-1.0852** | 0.2508 | ±0.5016 | **-4.327** | **1.51e-05** | *** |
| Season: spring (vs autumn) | -0.2835 | 0.2944 | ±0.5888 | -0.963 | 0.3356 |  |
| **Season: summer (vs autumn)** | **+1.8002** | 0.3540 | ±0.7080 | **+5.085** | **3.67e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5139** | 0.2925 | ±0.5851 | **-5.175** | **2.28e-07** | *** |
| Age (years) | +0.0069 | 0.0090 | ±0.0180 | +0.765 | 0.4442 |  |
| BMI (kg/m2) | +0.0185 | 0.0164 | ±0.0328 | +1.130 | 0.2585 |  |
| Hypertension | -0.1723 | 0.2311 | ±0.4622 | -0.746 | 0.4559 |  |
| High cholesterol | -0.2944 | 0.2067 | ±0.4133 | -1.425 | 0.1542 |  |
| **Kidney disease** | **+0.7719** | 0.3633 | ±0.7265 | **+2.125** | **0.0336** | * |
| Circulatory disease | +0.6420 | 0.3924 | ±0.7848 | +1.636 | 0.1018 |  |
| Time > 180 (%) | -0.1356 | 0.3507 | ±0.7014 | -0.387 | 0.6991 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **384**, R² = **0.3433**, Adj R² = **0.3184**, F-statistic = **13.78** (p = **2.17e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.2**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1286** | 0.8705 | ±1.7410 | **+27.717** | **4.32e-169** | *** |
| Education: graduate level (vs college) | +0.0439 | 0.2063 | ±0.4127 | +0.213 | 0.8315 |  |
| Education: high school or below (vs college) | +0.3626 | 0.3915 | ±0.7831 | +0.926 | 0.3544 |  |
| Site: UCSD (vs UAB) | -0.3283 | 0.2579 | ±0.5158 | -1.273 | 0.2030 |  |
| **Site: UW (vs UAB)** | **-1.0859** | 0.2507 | ±0.5014 | **-4.332** | **1.48e-05** | *** |
| Season: spring (vs autumn) | -0.2837 | 0.2954 | ±0.5907 | -0.961 | 0.3368 |  |
| **Season: summer (vs autumn)** | **+1.7966** | 0.3532 | ±0.7063 | **+5.087** | **3.64e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5156** | 0.2927 | ±0.5853 | **-5.179** | **2.24e-07** | *** |
| Age (years) | +0.0069 | 0.0091 | ±0.0182 | +0.758 | 0.4483 |  |
| BMI (kg/m2) | +0.0188 | 0.0165 | ±0.0330 | +1.139 | 0.2547 |  |
| Hypertension | -0.1739 | 0.2316 | ±0.4632 | -0.751 | 0.4529 |  |
| High cholesterol | -0.2925 | 0.2081 | ±0.4162 | -1.406 | 0.1598 |  |
| **Kidney disease** | **+0.7595** | 0.3632 | ±0.7264 | **+2.091** | **0.0365** | * |
| Circulatory disease | +0.6421 | 0.3930 | ±0.7859 | +1.634 | 0.1022 |  |
| Avg. daily time > 180 (%) | -0.0719 | 0.3497 | ±0.6995 | -0.206 | 0.8370 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **384**, R² = **0.3449**, Adj R² = **0.3201**, F-statistic = **13.88** (p = **1.41e-26**), Residual SE = **1.861** on **369** df, AIC = **1581.3**, BIC = **1640.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0213** | 0.8628 | ±1.7257 | **+27.840** | **1.44e-170** | *** |
| Education: graduate level (vs college) | +0.0545 | 0.2074 | ±0.4147 | +0.263 | 0.7925 |  |
| Education: high school or below (vs college) | +0.3689 | 0.3853 | ±0.7706 | +0.957 | 0.3384 |  |
| Site: UCSD (vs UAB) | -0.3168 | 0.2576 | ±0.5152 | -1.230 | 0.2188 |  |
| **Site: UW (vs UAB)** | **-1.0923** | 0.2505 | ±0.5011 | **-4.359** | **1.30e-05** | *** |
| Season: spring (vs autumn) | -0.2963 | 0.2929 | ±0.5859 | -1.011 | 0.3118 |  |
| **Season: summer (vs autumn)** | **+1.7908** | 0.3503 | ±0.7007 | **+5.112** | **3.19e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5415** | 0.2931 | ±0.5863 | **-5.259** | **1.45e-07** | *** |
| Age (years) | +0.0088 | 0.0093 | ±0.0185 | +0.945 | 0.3449 |  |
| BMI (kg/m2) | +0.0175 | 0.0165 | ±0.0329 | +1.062 | 0.2884 |  |
| Hypertension | -0.1884 | 0.2323 | ±0.4646 | -0.811 | 0.4173 |  |
| High cholesterol | -0.3041 | 0.2075 | ±0.4150 | -1.466 | 0.1427 |  |
| **Kidney disease** | **+0.7483** | 0.3617 | ±0.7234 | **+2.069** | **0.0386** | * |
| Circulatory disease | +0.6412 | 0.3885 | ±0.7769 | +1.651 | 0.0988 | . |
| Nocturnal time > 180 (%) | +0.2889 | 0.2596 | ±0.5192 | +1.113 | 0.2658 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 384; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **384**, R² = **0.3083**, Adj R² = **0.2840**, F-statistic = **12.69** (p = **4.52e-23**), Residual SE = **5.674** on **370** df, AIC = **2436.7**, BIC = **2492.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5680** | 2.0759 | ±4.1518 | **+22.914** | **3.34e-116** | *** |
| Education: graduate level (vs college) | +0.7740 | 0.6166 | ±1.2331 | +1.255 | 0.2094 |  |
| Education: high school or below (vs college) | -1.1445 | 1.1983 | ±2.3965 | -0.955 | 0.3395 |  |
| **Site: UCSD (vs UAB)** | **+4.5169** | 0.7799 | ±1.5597 | **+5.792** | **6.96e-09** | *** |
| Site: UW (vs UAB) | -0.8223 | 0.7583 | ±1.5165 | -1.084 | 0.2782 |  |
| Season: spring (vs autumn) | -0.9710 | 0.8341 | ±1.6682 | -1.164 | 0.2444 |  |
| **Season: summer (vs autumn)** | **+3.9692** | 0.9180 | ±1.8360 | **+4.324** | **1.53e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9848** | 0.8908 | ±1.7816 | **-4.473** | **7.70e-06** | *** |
| Age (years) | -0.0376 | 0.0262 | ±0.0525 | -1.432 | 0.1521 |  |
| BMI (kg/m2) | -0.0372 | 0.0406 | ±0.0812 | -0.916 | 0.3595 |  |
| Hypertension | +0.4303 | 0.6921 | ±1.3841 | +0.622 | 0.5341 |  |
| High cholesterol | -0.4429 | 0.6408 | ±1.2816 | -0.691 | 0.4894 |  |
| Kidney disease | -1.1481 | 1.2801 | ±2.5602 | -0.897 | 0.3698 |  |
| Circulatory disease | -0.3590 | 0.9495 | ±1.8990 | -0.378 | 0.7054 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **384**, R² = **0.3103**, Adj R² = **0.2841**, F-statistic = **11.86** (p = **1.00e-22**), Residual SE = **5.674** on **369** df, AIC = **2437.6**, BIC = **2496.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.9019** | 5.5076 | ±11.0152 | **+7.608** | **2.78e-14** | *** |
| Education: graduate level (vs college) | +0.7792 | 0.6170 | ±1.2340 | +1.263 | 0.2066 |  |
| Education: high school or below (vs college) | -1.1820 | 1.1892 | ±2.3784 | -0.994 | 0.3203 |  |
| **Site: UCSD (vs UAB)** | **+4.5210** | 0.7794 | ±1.5588 | **+5.801** | **6.60e-09** | *** |
| Site: UW (vs UAB) | -0.7971 | 0.7561 | ±1.5122 | -1.054 | 0.2918 |  |
| Season: spring (vs autumn) | -0.8296 | 0.8342 | ±1.6685 | -0.994 | 0.3200 |  |
| **Season: summer (vs autumn)** | **+3.9034** | 0.9216 | ±1.8432 | **+4.235** | **2.28e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9423** | 0.8864 | ±1.7729 | **-4.447** | **8.69e-06** | *** |
| Age (years) | -0.0410 | 0.0271 | ±0.0542 | -1.511 | 0.1308 |  |
| BMI (kg/m2) | -0.0412 | 0.0410 | ±0.0819 | -1.006 | 0.3145 |  |
| Hypertension | +0.3721 | 0.6969 | ±1.3937 | +0.534 | 0.5934 |  |
| High cholesterol | -0.5797 | 0.6500 | ±1.3000 | -0.892 | 0.3725 |  |
| Kidney disease | -1.0563 | 1.2982 | ±2.5963 | -0.814 | 0.4158 |  |
| Circulatory disease | -0.2657 | 0.9501 | ±1.9002 | -0.280 | 0.7798 |  |
| HbA1c (%) | +1.0837 | 1.0105 | ±2.0210 | +1.072 | 0.2835 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **384**, R² = **0.3094**, Adj R² = **0.2832**, F-statistic = **11.81** (p = **1.24e-22**), Residual SE = **5.677** on **369** df, AIC = **2438.1**, BIC = **2497.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.1116** | 5.1188 | ±10.2376 | **+8.618** | **6.84e-18** | *** |
| Education: graduate level (vs college) | +0.7623 | 0.6152 | ±1.2304 | +1.239 | 0.2153 |  |
| Education: high school or below (vs college) | -1.1260 | 1.2146 | ±2.4292 | -0.927 | 0.3539 |  |
| **Site: UCSD (vs UAB)** | **+4.4856** | 0.7814 | ±1.5628 | **+5.740** | **9.45e-09** | *** |
| Site: UW (vs UAB) | -0.8592 | 0.7604 | ±1.5207 | -1.130 | 0.2585 |  |
| Season: spring (vs autumn) | -0.9427 | 0.8365 | ±1.6730 | -1.127 | 0.2598 |  |
| **Season: summer (vs autumn)** | **+3.9662** | 0.9227 | ±1.8455 | **+4.298** | **1.72e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9717** | 0.8922 | ±1.7843 | **-4.452** | **8.52e-06** | *** |
| Age (years) | -0.0368 | 0.0263 | ±0.0526 | -1.398 | 0.1621 |  |
| BMI (kg/m2) | -0.0396 | 0.0406 | ±0.0812 | -0.975 | 0.3296 |  |
| Hypertension | +0.3949 | 0.7011 | ±1.4022 | +0.563 | 0.5733 |  |
| High cholesterol | -0.4217 | 0.6436 | ±1.2873 | -0.655 | 0.5124 |  |
| Kidney disease | -1.1828 | 1.2815 | ±2.5630 | -0.923 | 0.3560 |  |
| Circulatory disease | -0.3460 | 0.9503 | ±1.9005 | -0.364 | 0.7157 |  |
| Mean glucose (mg/dL) | +0.0306 | 0.0390 | ±0.0780 | +0.785 | 0.4324 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **384**, R² = **0.3094**, Adj R² = **0.2832**, F-statistic = **11.81** (p = **1.24e-22**), Residual SE = **5.677** on **369** df, AIC = **2438.1**, BIC = **2497.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.8764** | 10.2883 | ±20.5765 | **+3.876** | **1.06e-04** | *** |
| Education: graduate level (vs college) | +0.7623 | 0.6152 | ±1.2304 | +1.239 | 0.2153 |  |
| Education: high school or below (vs college) | -1.1260 | 1.2146 | ±2.4292 | -0.927 | 0.3539 |  |
| **Site: UCSD (vs UAB)** | **+4.4856** | 0.7814 | ±1.5628 | **+5.740** | **9.45e-09** | *** |
| Site: UW (vs UAB) | -0.8592 | 0.7604 | ±1.5207 | -1.130 | 0.2585 |  |
| Season: spring (vs autumn) | -0.9427 | 0.8365 | ±1.6730 | -1.127 | 0.2598 |  |
| **Season: summer (vs autumn)** | **+3.9662** | 0.9227 | ±1.8455 | **+4.298** | **1.72e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9717** | 0.8922 | ±1.7843 | **-4.452** | **8.52e-06** | *** |
| Age (years) | -0.0368 | 0.0263 | ±0.0526 | -1.398 | 0.1621 |  |
| BMI (kg/m2) | -0.0396 | 0.0406 | ±0.0812 | -0.975 | 0.3296 |  |
| Hypertension | +0.3949 | 0.7011 | ±1.4022 | +0.563 | 0.5733 |  |
| High cholesterol | -0.4217 | 0.6436 | ±1.2873 | -0.655 | 0.5124 |  |
| Kidney disease | -1.1828 | 1.2815 | ±2.5630 | -0.923 | 0.3560 |  |
| Circulatory disease | -0.3460 | 0.9503 | ±1.9005 | -0.364 | 0.7157 |  |
| GMI (%) | +1.2795 | 1.6296 | ±3.2592 | +0.785 | 0.4324 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **384**, R² = **0.3117**, Adj R² = **0.2856**, F-statistic = **11.94** (p = **7.03e-23**), Residual SE = **5.668** on **369** df, AIC = **2436.8**, BIC = **2496.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.6731** | 4.4617 | ±8.9235 | **+9.564** | **1.13e-21** | *** |
| Education: graduate level (vs college) | +0.8082 | 0.6200 | ±1.2400 | +1.304 | 0.1924 |  |
| Education: high school or below (vs college) | -1.0757 | 1.2240 | ±2.4480 | -0.879 | 0.3795 |  |
| **Site: UCSD (vs UAB)** | **+4.4093** | 0.7831 | ±1.5662 | **+5.631** | **1.80e-08** | *** |
| Site: UW (vs UAB) | -0.9139 | 0.7590 | ±1.5179 | -1.204 | 0.2286 |  |
| Season: spring (vs autumn) | -0.9633 | 0.8358 | ±1.6717 | -1.153 | 0.2491 |  |
| **Season: summer (vs autumn)** | **+3.9391** | 0.9248 | ±1.8496 | **+4.259** | **2.05e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9858** | 0.8935 | ±1.7869 | **-4.461** | **8.16e-06** | *** |
| Age (years) | -0.0323 | 0.0269 | ±0.0537 | -1.203 | 0.2290 |  |
| BMI (kg/m2) | -0.0469 | 0.0412 | ±0.0824 | -1.140 | 0.2543 |  |
| Hypertension | +0.3933 | 0.6966 | ±1.3932 | +0.565 | 0.5723 |  |
| High cholesterol | -0.4367 | 0.6415 | ±1.2830 | -0.681 | 0.4960 |  |
| Kidney disease | -1.1190 | 1.2869 | ±2.5739 | -0.870 | 0.3846 |  |
| Circulatory disease | -0.3220 | 0.9416 | ±1.8832 | -0.342 | 0.7324 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0428 | 0.0315 | ±0.0630 | +1.359 | 0.1742 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **384**, R² = **0.3083**, Adj R² = **0.2821**, F-statistic = **11.75** (p = **1.65e-22**), Residual SE = **5.682** on **369** df, AIC = **2438.7**, BIC = **2498.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.7160** | 3.0216 | ±6.0431 | **+15.792** | **3.54e-56** | *** |
| Education: graduate level (vs college) | +0.7716 | 0.6200 | ±1.2401 | +1.244 | 0.2134 |  |
| Education: high school or below (vs college) | -1.1439 | 1.2010 | ±2.4019 | -0.952 | 0.3408 |  |
| **Site: UCSD (vs UAB)** | **+4.5121** | 0.7814 | ±1.5628 | **+5.774** | **7.73e-09** | *** |
| Site: UW (vs UAB) | -0.8252 | 0.7618 | ±1.5235 | -1.083 | 0.2787 |  |
| Season: spring (vs autumn) | -0.9667 | 0.8413 | ±1.6825 | -1.149 | 0.2505 |  |
| **Season: summer (vs autumn)** | **+3.9721** | 0.9240 | ±1.8480 | **+4.299** | **1.72e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9802** | 0.9035 | ±1.8070 | **-4.405** | **1.06e-05** | *** |
| Age (years) | -0.0376 | 0.0263 | ±0.0527 | -1.426 | 0.1537 |  |
| BMI (kg/m2) | -0.0371 | 0.0407 | ±0.0815 | -0.910 | 0.3630 |  |
| Hypertension | +0.4304 | 0.6942 | ±1.3885 | +0.620 | 0.5353 |  |
| High cholesterol | -0.4450 | 0.6458 | ±1.2916 | -0.689 | 0.4908 |  |
| Kidney disease | -1.1444 | 1.2839 | ±2.5677 | -0.891 | 0.3727 |  |
| Circulatory disease | -0.3572 | 0.9495 | ±1.8989 | -0.376 | 0.7067 |  |
| Glucose SD, pooled (mg/dL) | -0.0091 | 0.1407 | ±0.2815 | -0.064 | 0.9487 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **384**, R² = **0.3088**, Adj R² = **0.2826**, F-statistic = **11.78** (p = **1.44e-22**), Residual SE = **5.680** on **369** df, AIC = **2438.4**, BIC = **2497.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5176** | 2.9345 | ±5.8691 | **+15.852** | **1.37e-56** | *** |
| Education: graduate level (vs college) | +0.7954 | 0.6191 | ±1.2383 | +1.285 | 0.1989 |  |
| Education: high school or below (vs college) | -1.1385 | 1.2102 | ±2.4204 | -0.941 | 0.3468 |  |
| **Site: UCSD (vs UAB)** | **+4.5573** | 0.7774 | ±1.5548 | **+5.862** | **4.56e-09** | *** |
| Site: UW (vs UAB) | -0.7978 | 0.7580 | ±1.5159 | -1.053 | 0.2925 |  |
| Season: spring (vs autumn) | -0.9996 | 0.8380 | ±1.6760 | -1.193 | 0.2329 |  |
| **Season: summer (vs autumn)** | **+3.9538** | 0.9226 | ±1.8453 | **+4.285** | **1.82e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0052** | 0.8990 | ±1.7980 | **-4.455** | **8.39e-06** | *** |
| Age (years) | -0.0377 | 0.0262 | ±0.0525 | -1.436 | 0.1510 |  |
| BMI (kg/m2) | -0.0391 | 0.0410 | ±0.0821 | -0.953 | 0.3407 |  |
| Hypertension | +0.4361 | 0.6910 | ±1.3820 | +0.631 | 0.5280 |  |
| High cholesterol | -0.4301 | 0.6454 | ±1.2908 | -0.666 | 0.5052 |  |
| Kidney disease | -1.1783 | 1.2717 | ±2.5434 | -0.927 | 0.3542 |  |
| Circulatory disease | -0.3625 | 0.9467 | ±1.8935 | -0.383 | 0.7018 |  |
| Avg. daily SD (mg/dL) | +0.0710 | 0.1442 | ±0.2884 | +0.492 | 0.6224 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **384**, R² = **0.3086**, Adj R² = **0.2823**, F-statistic = **11.76** (p = **1.55e-22**), Residual SE = **5.681** on **369** df, AIC = **2438.6**, BIC = **2497.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.3544** | 2.9184 | ±5.8369 | **+16.569** | **1.17e-61** | *** |
| Education: graduate level (vs college) | +0.7586 | 0.6180 | ±1.2359 | +1.228 | 0.2196 |  |
| Education: high school or below (vs college) | -1.1372 | 1.2000 | ±2.4000 | -0.948 | 0.3433 |  |
| **Site: UCSD (vs UAB)** | **+4.4847** | 0.7824 | ±1.5649 | **+5.732** | **9.94e-09** | *** |
| Site: UW (vs UAB) | -0.8465 | 0.7647 | ±1.5294 | -1.107 | 0.2683 |  |
| Season: spring (vs autumn) | -0.9416 | 0.8425 | ±1.6850 | -1.118 | 0.2638 |  |
| **Season: summer (vs autumn)** | **+3.9857** | 0.9245 | ±1.8491 | **+4.311** | **1.62e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9574** | 0.9012 | ±1.8025 | **-4.391** | **1.13e-05** | *** |
| Age (years) | -0.0373 | 0.0264 | ±0.0528 | -1.414 | 0.1573 |  |
| BMI (kg/m2) | -0.0370 | 0.0407 | ±0.0815 | -0.909 | 0.3633 |  |
| Hypertension | +0.4230 | 0.6946 | ±1.3892 | +0.609 | 0.5426 |  |
| High cholesterol | -0.4501 | 0.6442 | ±1.2885 | -0.699 | 0.4847 |  |
| Kidney disease | -1.1376 | 1.2927 | ±2.5853 | -0.880 | 0.3789 |  |
| Circulatory disease | -0.3459 | 0.9510 | ±1.9019 | -0.364 | 0.7161 |  |
| CV (%) | -0.0542 | 0.1571 | ±0.3142 | -0.345 | 0.7303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **384**, R² = **0.3087**, Adj R² = **0.2825**, F-statistic = **11.77** (p = **1.49e-22**), Residual SE = **5.680** on **369** df, AIC = **2438.5**, BIC = **2497.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5997** | 3.1959 | ±6.3917 | **+14.581** | **3.70e-48** | *** |
| Education: graduate level (vs college) | +0.7524 | 0.6179 | ±1.2358 | +1.218 | 0.2234 |  |
| Education: high school or below (vs college) | -1.1351 | 1.1992 | ±2.3983 | -0.947 | 0.3439 |  |
| **Site: UCSD (vs UAB)** | **+4.4837** | 0.7835 | ±1.5671 | **+5.722** | **1.05e-08** | *** |
| Site: UW (vs UAB) | -0.8460 | 0.7644 | ±1.5288 | -1.107 | 0.2684 |  |
| Season: spring (vs autumn) | -0.9318 | 0.8419 | ±1.6837 | -1.107 | 0.2683 |  |
| **Season: summer (vs autumn)** | **+3.9874** | 0.9233 | ±1.8466 | **+4.319** | **1.57e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9511** | 0.9006 | ±1.8013 | **-4.387** | **1.15e-05** | *** |
| Age (years) | -0.0374 | 0.0264 | ±0.0527 | -1.419 | 0.1560 |  |
| BMI (kg/m2) | -0.0370 | 0.0407 | ±0.0815 | -0.909 | 0.3632 |  |
| Hypertension | +0.4265 | 0.6952 | ±1.3904 | +0.613 | 0.5396 |  |
| High cholesterol | -0.4526 | 0.6440 | ±1.2881 | -0.703 | 0.4822 |  |
| Kidney disease | -1.1421 | 1.2884 | ±2.5768 | -0.886 | 0.3754 |  |
| Circulatory disease | -0.3441 | 0.9510 | ±1.9020 | -0.362 | 0.7175 |  |
| Mean / SD ratio | +0.1385 | 0.3208 | ±0.6417 | +0.432 | 0.6661 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **384**, R² = **0.3088**, Adj R² = **0.2826**, F-statistic = **11.77** (p = **1.46e-22**), Residual SE = **5.680** on **369** df, AIC = **2438.4**, BIC = **2497.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5599** | 3.1038 | ±6.2077 | **+15.645** | **3.59e-55** | *** |
| Education: graduate level (vs college) | +0.8006 | 0.6170 | ±1.2339 | +1.298 | 0.1944 |  |
| Education: high school or below (vs college) | -1.1454 | 1.2059 | ±2.4117 | -0.950 | 0.3422 |  |
| **Site: UCSD (vs UAB)** | **+4.5560** | 0.7773 | ±1.5547 | **+5.861** | **4.60e-09** | *** |
| Site: UW (vs UAB) | -0.7979 | 0.7601 | ±1.5202 | -1.050 | 0.2939 |  |
| Season: spring (vs autumn) | -1.0131 | 0.8339 | ±1.6679 | -1.215 | 0.2244 |  |
| **Season: summer (vs autumn)** | **+3.9525** | 0.9212 | ±1.8424 | **+4.291** | **1.78e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0112** | 0.8967 | ±1.7933 | **-4.473** | **7.70e-06** | *** |
| Age (years) | -0.0378 | 0.0263 | ±0.0526 | -1.438 | 0.1505 |  |
| BMI (kg/m2) | -0.0386 | 0.0411 | ±0.0821 | -0.941 | 0.3469 |  |
| Hypertension | +0.4435 | 0.6898 | ±1.3796 | +0.643 | 0.5203 |  |
| High cholesterol | -0.4370 | 0.6442 | ±1.2884 | -0.678 | 0.4975 |  |
| Kidney disease | -1.1609 | 1.2776 | ±2.5553 | -0.909 | 0.3635 |  |
| Circulatory disease | -0.3664 | 0.9466 | ±1.8932 | -0.387 | 0.6987 |  |
| Avg. daily mean/SD | -0.1217 | 0.2706 | ±0.5412 | -0.450 | 0.6528 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **384**, R² = **0.3089**, Adj R² = **0.2827**, F-statistic = **11.78** (p = **1.42e-22**), Residual SE = **5.680** on **369** df, AIC = **2438.4**, BIC = **2497.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.3941** | 3.0650 | ±6.1301 | **+15.137** | **9.30e-52** | *** |
| Education: graduate level (vs college) | +0.7653 | 0.6173 | ±1.2346 | +1.240 | 0.2151 |  |
| Education: high school or below (vs college) | -1.1931 | 1.2111 | ±2.4222 | -0.985 | 0.3245 |  |
| **Site: UCSD (vs UAB)** | **+4.5505** | 0.7815 | ±1.5630 | **+5.823** | **5.79e-09** | *** |
| Site: UW (vs UAB) | -0.7682 | 0.7654 | ±1.5308 | -1.004 | 0.3155 |  |
| Season: spring (vs autumn) | -0.9940 | 0.8310 | ±1.6620 | -1.196 | 0.2316 |  |
| **Season: summer (vs autumn)** | **+3.9717** | 0.9221 | ±1.8441 | **+4.307** | **1.65e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0090** | 0.8966 | ±1.7932 | **-4.471** | **7.77e-06** | *** |
| Age (years) | -0.0355 | 0.0268 | ±0.0536 | -1.326 | 0.1849 |  |
| BMI (kg/m2) | -0.0354 | 0.0407 | ±0.0815 | -0.870 | 0.3841 |  |
| Hypertension | +0.4438 | 0.6919 | ±1.3839 | +0.641 | 0.5212 |  |
| High cholesterol | -0.4635 | 0.6434 | ±1.2868 | -0.720 | 0.4713 |  |
| Kidney disease | -1.1856 | 1.2846 | ±2.5693 | -0.923 | 0.3560 |  |
| Circulatory disease | -0.3587 | 0.9495 | ±1.8990 | -0.378 | 0.7056 |  |
| MAG (mg/dL/h) | +0.0292 | 0.0537 | ±0.1074 | +0.544 | 0.5867 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **384**, R² = **0.3086**, Adj R² = **0.2824**, F-statistic = **11.76** (p = **1.54e-22**), Residual SE = **5.681** on **369** df, AIC = **2438.5**, BIC = **2497.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.6621** | 3.2481 | ±6.4962 | **+14.366** | **8.46e-47** | *** |
| Education: graduate level (vs college) | +0.7779 | 0.6187 | ±1.2374 | +1.257 | 0.2087 |  |
| Education: high school or below (vs college) | -1.1446 | 1.2055 | ±2.4111 | -0.949 | 0.3424 |  |
| **Site: UCSD (vs UAB)** | **+4.5449** | 0.7780 | ±1.5561 | **+5.841** | **5.18e-09** | *** |
| Site: UW (vs UAB) | -0.8023 | 0.7565 | ±1.5130 | -1.060 | 0.2889 |  |
| Season: spring (vs autumn) | -0.9937 | 0.8382 | ±1.6763 | -1.186 | 0.2358 |  |
| **Season: summer (vs autumn)** | **+3.9605** | 0.9229 | ±1.8459 | **+4.291** | **1.78e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0062** | 0.9008 | ±1.8015 | **-4.448** | **8.69e-06** | *** |
| Age (years) | -0.0374 | 0.0263 | ±0.0526 | -1.421 | 0.1553 |  |
| BMI (kg/m2) | -0.0359 | 0.0406 | ±0.0812 | -0.884 | 0.3765 |  |
| Hypertension | +0.4431 | 0.6900 | ±1.3800 | +0.642 | 0.5207 |  |
| High cholesterol | -0.4453 | 0.6429 | ±1.2858 | -0.693 | 0.4885 |  |
| Kidney disease | -1.1609 | 1.2751 | ±2.5501 | -0.910 | 0.3626 |  |
| Circulatory disease | -0.3668 | 0.9464 | ±1.8929 | -0.388 | 0.6984 |  |
| Avg. daily range (mg/dL) | +0.0107 | 0.0311 | ±0.0621 | +0.344 | 0.7310 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **384**, R² = **0.3083**, Adj R² = **0.2821**, F-statistic = **11.75** (p = **1.65e-22**), Residual SE = **5.682** on **369** df, AIC = **2438.7**, BIC = **2498.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5228** | 2.1401 | ±4.2803 | **+22.206** | **3.04e-109** | *** |
| Education: graduate level (vs college) | +0.7723 | 0.6207 | ±1.2414 | +1.244 | 0.2134 |  |
| Education: high school or below (vs college) | -1.1487 | 1.2078 | ±2.4156 | -0.951 | 0.3416 |  |
| **Site: UCSD (vs UAB)** | **+4.5181** | 0.7839 | ±1.5677 | **+5.764** | **8.22e-09** | *** |
| Site: UW (vs UAB) | -0.8242 | 0.7564 | ±1.5129 | -1.090 | 0.2759 |  |
| Season: spring (vs autumn) | -0.9745 | 0.8442 | ±1.6884 | -1.154 | 0.2484 |  |
| **Season: summer (vs autumn)** | **+3.9653** | 0.9246 | ±1.8492 | **+4.289** | **1.80e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9902** | 0.9102 | ±1.8205 | **-4.384** | **1.17e-05** | *** |
| Age (years) | -0.0376 | 0.0264 | ±0.0527 | -1.426 | 0.1539 |  |
| BMI (kg/m2) | -0.0372 | 0.0407 | ±0.0814 | -0.914 | 0.3606 |  |
| Hypertension | +0.4277 | 0.6904 | ±1.3807 | +0.620 | 0.5356 |  |
| High cholesterol | -0.4437 | 0.6422 | ±1.2843 | -0.691 | 0.4896 |  |
| Kidney disease | -1.1435 | 1.2857 | ±2.5715 | -0.889 | 0.3738 |  |
| Circulatory disease | -0.3624 | 0.9568 | ±1.9136 | -0.379 | 0.7049 |  |
| SD of daily means (mg/dL) | +0.0105 | 0.1732 | ±0.3464 | +0.061 | 0.9515 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **384**, R² = **0.3102**, Adj R² = **0.2841**, F-statistic = **11.86** (p = **1.02e-22**), Residual SE = **5.674** on **369** df, AIC = **2437.6**, BIC = **2496.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +147.8247 | 98.2035 | ±196.4071 | +1.505 | 0.1322 |  |
| Education: graduate level (vs college) | +0.7752 | 0.6176 | ±1.2352 | +1.255 | 0.2094 |  |
| Education: high school or below (vs college) | -1.1532 | 1.2023 | ±2.4045 | -0.959 | 0.3375 |  |
| **Site: UCSD (vs UAB)** | **+4.5709** | 0.7793 | ±1.5586 | **+5.865** | **4.48e-09** | *** |
| Site: UW (vs UAB) | -0.7841 | 0.7615 | ±1.5230 | -1.030 | 0.3032 |  |
| Season: spring (vs autumn) | -1.0114 | 0.8277 | ±1.6554 | -1.222 | 0.2217 |  |
| **Season: summer (vs autumn)** | **+3.9100** | 0.9208 | ±1.8416 | **+4.246** | **2.17e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0422** | 0.8966 | ±1.7932 | **-4.508** | **6.54e-06** | *** |
| Age (years) | -0.0365 | 0.0262 | ±0.0523 | -1.396 | 0.1628 |  |
| BMI (kg/m2) | -0.0345 | 0.0405 | ±0.0810 | -0.853 | 0.3937 |  |
| Hypertension | +0.4330 | 0.6904 | ±1.3808 | +0.627 | 0.5305 |  |
| High cholesterol | -0.4721 | 0.6412 | ±1.2824 | -0.736 | 0.4615 |  |
| Kidney disease | -1.1977 | 1.2748 | ±2.5497 | -0.940 | 0.3475 |  |
| Circulatory disease | -0.3814 | 0.9390 | ±1.8780 | -0.406 | 0.6846 |  |
| Time in range 70-180, pooled (%) | -1.0083 | 0.9862 | ±1.9724 | -1.022 | 0.3066 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **384**, R² = **0.3109**, Adj R² = **0.2848**, F-statistic = **11.89** (p = **8.67e-23**), Residual SE = **5.671** on **369** df, AIC = **2437.3**, BIC = **2496.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +160.1843 | 99.9365 | ±199.8730 | +1.603 | 0.1090 |  |
| Education: graduate level (vs college) | +0.7757 | 0.6175 | ±1.2350 | +1.256 | 0.2091 |  |
| Education: high school or below (vs college) | -1.1356 | 1.2092 | ±2.4183 | -0.939 | 0.3476 |  |
| **Site: UCSD (vs UAB)** | **+4.5609** | 0.7788 | ±1.5575 | **+5.857** | **4.73e-09** | *** |
| Site: UW (vs UAB) | -0.8109 | 0.7609 | ±1.5218 | -1.066 | 0.2865 |  |
| Season: spring (vs autumn) | -1.0053 | 0.8279 | ±1.6557 | -1.214 | 0.2246 |  |
| **Season: summer (vs autumn)** | **+3.9469** | 0.9232 | ±1.8464 | **+4.275** | **1.91e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0362** | 0.8959 | ±1.7918 | **-4.505** | **6.63e-06** | *** |
| Age (years) | -0.0352 | 0.0262 | ±0.0524 | -1.342 | 0.1797 |  |
| BMI (kg/m2) | -0.0360 | 0.0408 | ±0.0816 | -0.882 | 0.3776 |  |
| Hypertension | +0.4626 | 0.6911 | ±1.3821 | +0.669 | 0.5032 |  |
| High cholesterol | -0.4859 | 0.6426 | ±1.2852 | -0.756 | 0.4496 |  |
| Kidney disease | -1.1606 | 1.2779 | ±2.5558 | -0.908 | 0.3637 |  |
| Circulatory disease | -0.4088 | 0.9324 | ±1.8648 | -0.438 | 0.6611 |  |
| Avg. daily time in range 70-180 (%) | -1.1322 | 1.0032 | ±2.0064 | -1.129 | 0.2591 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.3090**, Adj R² = **0.2828**, F-statistic = **11.78** (p = **1.40e-22**), Residual SE = **5.679** on **369** df, AIC = **2438.3**, BIC = **2497.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4831** | 2.0971 | ±4.1942 | **+22.642** | **1.67e-113** | *** |
| Education: graduate level (vs college) | +0.7813 | 0.6178 | ±1.2356 | +1.265 | 0.2060 |  |
| Education: high school or below (vs college) | -1.1350 | 1.2013 | ±2.4025 | -0.945 | 0.3448 |  |
| **Site: UCSD (vs UAB)** | **+4.6016** | 0.7924 | ±1.5847 | **+5.808** | **6.34e-09** | *** |
| Site: UW (vs UAB) | -0.7675 | 0.7675 | ±1.5350 | -1.000 | 0.3173 |  |
| Season: spring (vs autumn) | -1.0344 | 0.8319 | ±1.6639 | -1.243 | 0.2138 |  |
| **Season: summer (vs autumn)** | **+3.9377** | 0.9203 | ±1.8406 | **+4.279** | **1.88e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0285** | 0.8938 | ±1.7876 | **-4.507** | **6.57e-06** | *** |
| Age (years) | -0.0376 | 0.0262 | ±0.0525 | -1.433 | 0.1519 |  |
| BMI (kg/m2) | -0.0372 | 0.0407 | ±0.0815 | -0.912 | 0.3617 |  |
| Hypertension | +0.3982 | 0.6900 | ±1.3799 | +0.577 | 0.5638 |  |
| High cholesterol | -0.4423 | 0.6424 | ±1.2849 | -0.688 | 0.4912 |  |
| Kidney disease | -1.0967 | 1.2898 | ±2.5796 | -0.850 | 0.3952 |  |
| Circulatory disease | -0.3872 | 0.9450 | ±1.8900 | -0.410 | 0.6820 |  |
| Any reading < 54 during wear (0/1) | +0.4880 | 0.8538 | ±1.7076 | +0.572 | 0.5676 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.3091**, Adj R² = **0.2829**, F-statistic = **11.79** (p = **1.36e-22**), Residual SE = **5.679** on **369** df, AIC = **2438.3**, BIC = **2497.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4852** | 2.0870 | ±4.1739 | **+22.753** | **1.33e-114** | *** |
| Education: graduate level (vs college) | +0.7768 | 0.6190 | ±1.2379 | +1.255 | 0.2095 |  |
| Education: high school or below (vs college) | -1.1076 | 1.1994 | ±2.3988 | -0.923 | 0.3558 |  |
| **Site: UCSD (vs UAB)** | **+4.5810** | 0.7836 | ±1.5672 | **+5.846** | **5.04e-09** | *** |
| Site: UW (vs UAB) | -0.7903 | 0.7621 | ±1.5242 | -1.037 | 0.2998 |  |
| Season: spring (vs autumn) | -0.9623 | 0.8397 | ±1.6794 | -1.146 | 0.2518 |  |
| **Season: summer (vs autumn)** | **+3.9647** | 0.9256 | ±1.8512 | **+4.283** | **1.84e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9817** | 0.8954 | ±1.7908 | **-4.447** | **8.72e-06** | *** |
| Age (years) | -0.0368 | 0.0264 | ±0.0528 | -1.395 | 0.1632 |  |
| BMI (kg/m2) | -0.0391 | 0.0410 | ±0.0821 | -0.952 | 0.3412 |  |
| Hypertension | +0.3978 | 0.6896 | ±1.3791 | +0.577 | 0.5640 |  |
| High cholesterol | -0.4385 | 0.6414 | ±1.2829 | -0.684 | 0.4942 |  |
| Kidney disease | -1.1126 | 1.2856 | ±2.5712 | -0.865 | 0.3868 |  |
| Circulatory disease | -0.3975 | 0.9481 | ±1.8961 | -0.419 | 0.6750 |  |
| Time < 54 (%) | +3.7900 | 6.3030 | ±12.6059 | +0.601 | 0.5476 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.3087**, Adj R² = **0.2825**, F-statistic = **11.77** (p = **1.50e-22**), Residual SE = **5.681** on **369** df, AIC = **2438.5**, BIC = **2497.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5200** | 2.0836 | ±4.1671 | **+22.807** | **3.91e-115** | *** |
| Education: graduate level (vs college) | +0.7662 | 0.6209 | ±1.2417 | +1.234 | 0.2172 |  |
| Education: high school or below (vs college) | -1.1337 | 1.2008 | ±2.4015 | -0.944 | 0.3451 |  |
| **Site: UCSD (vs UAB)** | **+4.5427** | 0.7846 | ±1.5692 | **+5.790** | **7.04e-09** | *** |
| Site: UW (vs UAB) | -0.8123 | 0.7634 | ±1.5268 | -1.064 | 0.2873 |  |
| Season: spring (vs autumn) | -0.9618 | 0.8409 | ±1.6818 | -1.144 | 0.2527 |  |
| **Season: summer (vs autumn)** | **+3.9986** | 0.9257 | ±1.8514 | **+4.320** | **1.56e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9783** | 0.8956 | ±1.7913 | **-4.442** | **8.92e-06** | *** |
| Age (years) | -0.0371 | 0.0264 | ±0.0527 | -1.408 | 0.1592 |  |
| BMI (kg/m2) | -0.0380 | 0.0409 | ±0.0817 | -0.930 | 0.3524 |  |
| Hypertension | +0.4164 | 0.6952 | ±1.3905 | +0.599 | 0.5492 |  |
| High cholesterol | -0.4384 | 0.6419 | ±1.2839 | -0.683 | 0.4947 |  |
| Kidney disease | -1.1394 | 1.2844 | ±2.5688 | -0.887 | 0.3750 |  |
| Circulatory disease | -0.3969 | 0.9518 | ±1.9037 | -0.417 | 0.6767 |  |
| Avg. daily time < 54 (%) | +3.2192 | 8.5892 | ±17.1785 | +0.375 | 0.7078 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.3086**, Adj R² = **0.2823**, F-statistic = **11.76** (p = **1.54e-22**), Residual SE = **5.681** on **369** df, AIC = **2438.6**, BIC = **2497.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4700** | 2.0936 | ±4.1871 | **+22.674** | **8.02e-114** | *** |
| Education: graduate level (vs college) | +0.7820 | 0.6170 | ±1.2340 | +1.267 | 0.2050 |  |
| Education: high school or below (vs college) | -1.1620 | 1.2091 | ±2.4182 | -0.961 | 0.3365 |  |
| **Site: UCSD (vs UAB)** | **+4.5400** | 0.7891 | ±1.5783 | **+5.753** | **8.76e-09** | *** |
| Site: UW (vs UAB) | -0.7952 | 0.7752 | ±1.5503 | -1.026 | 0.3050 |  |
| Season: spring (vs autumn) | -0.9834 | 0.8354 | ±1.6709 | -1.177 | 0.2391 |  |
| **Season: summer (vs autumn)** | **+3.9649** | 0.9193 | ±1.8386 | **+4.313** | **1.61e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0044** | 0.8940 | ±1.7879 | **-4.479** | **7.49e-06** | *** |
| Age (years) | -0.0377 | 0.0264 | ±0.0527 | -1.430 | 0.1526 |  |
| BMI (kg/m2) | -0.0369 | 0.0406 | ±0.0813 | -0.908 | 0.3641 |  |
| Hypertension | +0.4537 | 0.7032 | ±1.4063 | +0.645 | 0.5188 |  |
| High cholesterol | -0.4677 | 0.6465 | ±1.2930 | -0.723 | 0.4695 |  |
| Kidney disease | -1.1068 | 1.2865 | ±2.5730 | -0.860 | 0.3896 |  |
| Circulatory disease | -0.3616 | 0.9507 | ±1.9014 | -0.380 | 0.7037 |  |
| Time 54-69, pooled (%) | +0.6452 | 1.7865 | ±3.5730 | +0.361 | 0.7180 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **384**, R² = **0.3083**, Adj R² = **0.2821**, F-statistic = **11.75** (p = **1.65e-22**), Residual SE = **5.682** on **369** df, AIC = **2438.7**, BIC = **2498.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5585** | 2.0838 | ±4.1676 | **+22.823** | **2.71e-115** | *** |
| Education: graduate level (vs college) | +0.7751 | 0.6192 | ±1.2384 | +1.252 | 0.2107 |  |
| Education: high school or below (vs college) | -1.1466 | 1.2081 | ±2.4161 | -0.949 | 0.3426 |  |
| **Site: UCSD (vs UAB)** | **+4.5183** | 0.7853 | ±1.5706 | **+5.754** | **8.73e-09** | *** |
| Site: UW (vs UAB) | -0.8209 | 0.7639 | ±1.5277 | -1.075 | 0.2825 |  |
| Season: spring (vs autumn) | -0.9705 | 0.8377 | ±1.6753 | -1.159 | 0.2466 |  |
| **Season: summer (vs autumn)** | **+3.9704** | 0.9206 | ±1.8413 | **+4.313** | **1.61e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9861** | 0.8937 | ±1.7875 | **-4.460** | **8.20e-06** | *** |
| Age (years) | -0.0376 | 0.0264 | ±0.0527 | -1.426 | 0.1538 |  |
| BMI (kg/m2) | -0.0372 | 0.0407 | ±0.0813 | -0.914 | 0.3608 |  |
| Hypertension | +0.4341 | 0.7027 | ±1.4053 | +0.618 | 0.5367 |  |
| High cholesterol | -0.4447 | 0.6448 | ±1.2895 | -0.690 | 0.4903 |  |
| Kidney disease | -1.1451 | 1.2841 | ±2.5682 | -0.892 | 0.3725 |  |
| Circulatory disease | -0.3600 | 0.9511 | ±1.9021 | -0.379 | 0.7050 |  |
| Avg. daily time 54-69 (%) | +0.0658 | 1.8120 | ±3.6240 | +0.036 | 0.9710 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **384**, R² = **0.3088**, Adj R² = **0.2826**, F-statistic = **11.77** (p = **1.47e-22**), Residual SE = **5.680** on **369** df, AIC = **2438.4**, BIC = **2497.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4373** | 2.0966 | ±4.1933 | **+22.625** | **2.43e-113** | *** |
| Education: graduate level (vs college) | +0.7839 | 0.6168 | ±1.2335 | +1.271 | 0.2038 |  |
| Education: high school or below (vs college) | -1.1576 | 1.2072 | ±2.4144 | -0.959 | 0.3376 |  |
| **Site: UCSD (vs UAB)** | **+4.5565** | 0.7911 | ±1.5823 | **+5.759** | **8.44e-09** | *** |
| Site: UW (vs UAB) | -0.7843 | 0.7753 | ±1.5506 | -1.012 | 0.3117 |  |
| Season: spring (vs autumn) | -0.9838 | 0.8355 | ±1.6709 | -1.178 | 0.2390 |  |
| **Season: summer (vs autumn)** | **+3.9633** | 0.9198 | ±1.8396 | **+4.309** | **1.64e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0071** | 0.8941 | ±1.7882 | **-4.482** | **7.40e-06** | *** |
| Age (years) | -0.0376 | 0.0263 | ±0.0527 | -1.427 | 0.1537 |  |
| BMI (kg/m2) | -0.0372 | 0.0406 | ±0.0813 | -0.915 | 0.3601 |  |
| Hypertension | +0.4511 | 0.6991 | ±1.3982 | +0.645 | 0.5188 |  |
| High cholesterol | -0.4709 | 0.6459 | ±1.2918 | -0.729 | 0.4660 |  |
| Kidney disease | -1.0928 | 1.2875 | ±2.5751 | -0.849 | 0.3960 |  |
| Circulatory disease | -0.3696 | 0.9497 | ±1.8994 | -0.389 | 0.6971 |  |
| Time < 70 (%) | +0.7526 | 1.5922 | ±3.1845 | +0.473 | 0.6364 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **384**, R² = **0.3083**, Adj R² = **0.2821**, F-statistic = **11.75** (p = **1.64e-22**), Residual SE = **5.682** on **369** df, AIC = **2438.7**, BIC = **2497.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5361** | 2.0853 | ±4.1707 | **+22.795** | **5.10e-115** | *** |
| Education: graduate level (vs college) | +0.7770 | 0.6184 | ±1.2369 | +1.256 | 0.2090 |  |
| Education: high school or below (vs college) | -1.1502 | 1.2075 | ±2.4150 | -0.953 | 0.3408 |  |
| **Site: UCSD (vs UAB)** | **+4.5226** | 0.7863 | ±1.5727 | **+5.752** | **8.85e-09** | *** |
| Site: UW (vs UAB) | -0.8175 | 0.7646 | ±1.5291 | -1.069 | 0.2849 |  |
| Season: spring (vs autumn) | -0.9689 | 0.8380 | ±1.6759 | -1.156 | 0.2476 |  |
| **Season: summer (vs autumn)** | **+3.9745** | 0.9215 | ±1.8430 | **+4.313** | **1.61e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9885** | 0.8941 | ±1.7883 | **-4.461** | **8.17e-06** | *** |
| Age (years) | -0.0376 | 0.0263 | ±0.0527 | -1.427 | 0.1536 |  |
| BMI (kg/m2) | -0.0372 | 0.0407 | ±0.0814 | -0.913 | 0.3610 |  |
| Hypertension | +0.4411 | 0.6996 | ±1.3991 | +0.631 | 0.5284 |  |
| High cholesterol | -0.4482 | 0.6444 | ±1.2888 | -0.696 | 0.4867 |  |
| Kidney disease | -1.1386 | 1.2845 | ±2.5690 | -0.886 | 0.3754 |  |
| Circulatory disease | -0.3644 | 0.9505 | ±1.9010 | -0.383 | 0.7014 |  |
| Avg. daily time < 70 (%) | +0.2000 | 1.6469 | ±3.2937 | +0.121 | 0.9033 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.3093**, Adj R² = **0.2831**, F-statistic = **11.80** (p = **1.30e-22**), Residual SE = **5.678** on **369** df, AIC = **2438.2**, BIC = **2497.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +467.1467 | 633.5871 | ±1267.1742 | +0.737 | 0.4609 |  |
| Education: graduate level (vs college) | +0.7800 | 0.6189 | ±1.2378 | +1.260 | 0.2076 |  |
| Education: high school or below (vs college) | -1.1013 | 1.1997 | ±2.3993 | -0.918 | 0.3586 |  |
| **Site: UCSD (vs UAB)** | **+4.5881** | 0.7836 | ±1.5672 | **+5.855** | **4.76e-09** | *** |
| Site: UW (vs UAB) | -0.7891 | 0.7618 | ±1.5236 | -1.036 | 0.3003 |  |
| Season: spring (vs autumn) | -0.9612 | 0.8401 | ±1.6802 | -1.144 | 0.2526 |  |
| **Season: summer (vs autumn)** | **+3.9639** | 0.9262 | ±1.8524 | **+4.280** | **1.87e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9849** | 0.8957 | ±1.7915 | **-4.449** | **8.64e-06** | *** |
| Age (years) | -0.0366 | 0.0264 | ±0.0528 | -1.385 | 0.1659 |  |
| BMI (kg/m2) | -0.0391 | 0.0410 | ±0.0820 | -0.954 | 0.3403 |  |
| Hypertension | +0.3954 | 0.6892 | ±1.3784 | +0.574 | 0.5662 |  |
| High cholesterol | -0.4417 | 0.6415 | ±1.2831 | -0.689 | 0.4911 |  |
| Kidney disease | -1.1078 | 1.2862 | ±2.5723 | -0.861 | 0.3891 |  |
| Circulatory disease | -0.4011 | 0.9474 | ±1.8949 | -0.423 | 0.6720 |  |
| Time 54-250, pooled (%) | -4.1968 | 6.3365 | ±12.6729 | -0.662 | 0.5078 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.3089**, Adj R² = **0.2826**, F-statistic = **11.78** (p = **1.44e-22**), Residual SE = **5.680** on **369** df, AIC = **2438.4**, BIC = **2497.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +433.7557 | 867.0902 | ±1734.1804 | +0.500 | 0.6169 |  |
| Education: graduate level (vs college) | +0.7675 | 0.6204 | ±1.2408 | +1.237 | 0.2161 |  |
| Education: high school or below (vs college) | -1.1292 | 1.2010 | ±2.4021 | -0.940 | 0.3471 |  |
| **Site: UCSD (vs UAB)** | **+4.5481** | 0.7846 | ±1.5692 | **+5.797** | **6.77e-09** | *** |
| Site: UW (vs UAB) | -0.8126 | 0.7634 | ±1.5268 | -1.064 | 0.2871 |  |
| Season: spring (vs autumn) | -0.9598 | 0.8416 | ±1.6831 | -1.140 | 0.2541 |  |
| **Season: summer (vs autumn)** | **+4.0041** | 0.9259 | ±1.8517 | **+4.325** | **1.53e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9805** | 0.8965 | ±1.7929 | **-4.440** | **8.99e-06** | *** |
| Age (years) | -0.0369 | 0.0264 | ±0.0528 | -1.399 | 0.1619 |  |
| BMI (kg/m2) | -0.0380 | 0.0408 | ±0.0817 | -0.930 | 0.3524 |  |
| Hypertension | +0.4147 | 0.6949 | ±1.3898 | +0.597 | 0.5507 |  |
| High cholesterol | -0.4413 | 0.6422 | ±1.2844 | -0.687 | 0.4920 |  |
| Kidney disease | -1.1366 | 1.2852 | ±2.5704 | -0.884 | 0.3765 |  |
| Circulatory disease | -0.4040 | 0.9512 | ±1.9024 | -0.425 | 0.6710 |  |
| Avg. daily time 54-250 (%) | -3.8626 | 8.6708 | ±17.3417 | -0.445 | 0.6560 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **384**, R² = **0.3092**, Adj R² = **0.2830**, F-statistic = **11.80** (p = **1.31e-22**), Residual SE = **5.678** on **369** df, AIC = **2438.2**, BIC = **2497.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.2805** | 2.0976 | ±4.1951 | **+22.541** | **1.66e-112** | *** |
| Education: graduate level (vs college) | +0.7647 | 0.6179 | ±1.2357 | +1.238 | 0.2159 |  |
| Education: high school or below (vs college) | -1.1384 | 1.2004 | ±2.4008 | -0.948 | 0.3429 |  |
| **Site: UCSD (vs UAB)** | **+4.5175** | 0.7801 | ±1.5602 | **+5.791** | **7.01e-09** | *** |
| Site: UW (vs UAB) | -0.8312 | 0.7634 | ±1.5267 | -1.089 | 0.2762 |  |
| Season: spring (vs autumn) | -0.9880 | 0.8314 | ±1.6627 | -1.188 | 0.2347 |  |
| **Season: summer (vs autumn)** | **+3.9319** | 0.9210 | ±1.8420 | **+4.269** | **1.96e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0042** | 0.8942 | ±1.7883 | **-4.478** | **7.53e-06** | *** |
| Age (years) | -0.0368 | 0.0262 | ±0.0524 | -1.406 | 0.1598 |  |
| BMI (kg/m2) | -0.0353 | 0.0407 | ±0.0814 | -0.867 | 0.3859 |  |
| Hypertension | +0.4117 | 0.6948 | ±1.3895 | +0.593 | 0.5534 |  |
| High cholesterol | -0.4362 | 0.6425 | ±1.2850 | -0.679 | 0.4972 |  |
| Kidney disease | -1.2385 | 1.2785 | ±2.5569 | -0.969 | 0.3327 |  |
| Circulatory disease | -0.3650 | 0.9467 | ±1.8934 | -0.386 | 0.6998 |  |
| Time 181-250, pooled (%) | +0.7356 | 1.0392 | ±2.0785 | +0.708 | 0.4790 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **384**, R² = **0.3109**, Adj R² = **0.2847**, F-statistic = **11.89** (p = **8.78e-23**), Residual SE = **5.672** on **369** df, AIC = **2437.3**, BIC = **2496.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.1219** | 2.1063 | ±4.2127 | **+22.371** | **7.47e-111** | *** |
| Education: graduate level (vs college) | +0.7566 | 0.6183 | ±1.2366 | +1.224 | 0.2211 |  |
| Education: high school or below (vs college) | -1.1014 | 1.2083 | ±2.4165 | -0.912 | 0.3620 |  |
| **Site: UCSD (vs UAB)** | **+4.5296** | 0.7781 | ±1.5561 | **+5.822** | **5.82e-09** | *** |
| Site: UW (vs UAB) | -0.8382 | 0.7624 | ±1.5247 | -1.100 | 0.2715 |  |
| Season: spring (vs autumn) | -1.0200 | 0.8298 | ±1.6596 | -1.229 | 0.2190 |  |
| **Season: summer (vs autumn)** | **+3.9138** | 0.9263 | ±1.8527 | **+4.225** | **2.39e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0161** | 0.8933 | ±1.7866 | **-4.496** | **6.93e-06** | *** |
| Age (years) | -0.0350 | 0.0263 | ±0.0525 | -1.333 | 0.1824 |  |
| BMI (kg/m2) | -0.0361 | 0.0410 | ±0.0820 | -0.881 | 0.3783 |  |
| Hypertension | +0.3991 | 0.6937 | ±1.3874 | +0.575 | 0.5651 |  |
| High cholesterol | -0.4557 | 0.6413 | ±1.2825 | -0.711 | 0.4773 |  |
| Kidney disease | -1.2195 | 1.2732 | ±2.5463 | -0.958 | 0.3381 |  |
| Circulatory disease | -0.3795 | 0.9395 | ±1.8789 | -0.404 | 0.6862 |  |
| Avg. daily time 181-250 (%) | +1.2107 | 1.0935 | ±2.1871 | +1.107 | 0.2682 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **384**, R² = **0.3093**, Adj R² = **0.2831**, F-statistic = **11.80** (p = **1.30e-22**), Residual SE = **5.678** on **369** df, AIC = **2438.2**, BIC = **2497.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.2732** | 2.0980 | ±4.1959 | **+22.533** | **1.97e-112** | *** |
| Education: graduate level (vs college) | +0.7650 | 0.6179 | ±1.2357 | +1.238 | 0.2156 |  |
| Education: high school or below (vs college) | -1.1379 | 1.2004 | ±2.4008 | -0.948 | 0.3432 |  |
| **Site: UCSD (vs UAB)** | **+4.5176** | 0.7801 | ±1.5602 | **+5.791** | **6.99e-09** | *** |
| Site: UW (vs UAB) | -0.8317 | 0.7635 | ±1.5270 | -1.089 | 0.2760 |  |
| Season: spring (vs autumn) | -0.9882 | 0.8313 | ±1.6626 | -1.189 | 0.2345 |  |
| **Season: summer (vs autumn)** | **+3.9312** | 0.9210 | ±1.8420 | **+4.268** | **1.97e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0051** | 0.8943 | ±1.7885 | **-4.479** | **7.51e-06** | *** |
| Age (years) | -0.0368 | 0.0262 | ±0.0524 | -1.405 | 0.1602 |  |
| BMI (kg/m2) | -0.0352 | 0.0407 | ±0.0814 | -0.865 | 0.3868 |  |
| Hypertension | +0.4116 | 0.6947 | ±1.3894 | +0.592 | 0.5535 |  |
| High cholesterol | -0.4368 | 0.6424 | ±1.2848 | -0.680 | 0.4965 |  |
| Kidney disease | -1.2399 | 1.2783 | ±2.5567 | -0.970 | 0.3321 |  |
| Circulatory disease | -0.3650 | 0.9466 | ±1.8932 | -0.386 | 0.6998 |  |
| Time > 180 (%) | +0.7483 | 1.0382 | ±2.0764 | +0.721 | 0.4710 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **384**, R² = **0.3109**, Adj R² = **0.2848**, F-statistic = **11.89** (p = **8.65e-23**), Residual SE = **5.671** on **369** df, AIC = **2437.3**, BIC = **2496.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.1131** | 2.1068 | ±4.2136 | **+22.363** | **9.10e-111** | *** |
| Education: graduate level (vs college) | +0.7573 | 0.6182 | ±1.2364 | +1.225 | 0.2206 |  |
| Education: high school or below (vs college) | -1.1002 | 1.2084 | ±2.4168 | -0.910 | 0.3626 |  |
| **Site: UCSD (vs UAB)** | **+4.5298** | 0.7780 | ±1.5560 | **+5.822** | **5.80e-09** | *** |
| Site: UW (vs UAB) | -0.8391 | 0.7625 | ±1.5249 | -1.101 | 0.2711 |  |
| Season: spring (vs autumn) | -1.0205 | 0.8297 | ±1.6595 | -1.230 | 0.2187 |  |
| **Season: summer (vs autumn)** | **+3.9131** | 0.9264 | ±1.8528 | **+4.224** | **2.40e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0175** | 0.8934 | ±1.7868 | **-4.497** | **6.89e-06** | *** |
| Age (years) | -0.0349 | 0.0263 | ±0.0525 | -1.331 | 0.1833 |  |
| BMI (kg/m2) | -0.0360 | 0.0410 | ±0.0820 | -0.879 | 0.3793 |  |
| Hypertension | +0.3991 | 0.6937 | ±1.3874 | +0.575 | 0.5650 |  |
| High cholesterol | -0.4571 | 0.6412 | ±1.2824 | -0.713 | 0.4760 |  |
| Kidney disease | -1.2199 | 1.2731 | ±2.5461 | -0.958 | 0.3379 |  |
| Circulatory disease | -0.3796 | 0.9394 | ±1.8787 | -0.404 | 0.6862 |  |
| Avg. daily time > 180 (%) | +1.2231 | 1.0917 | ±2.1834 | +1.120 | 0.2626 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **384**, R² = **0.3097**, Adj R² = **0.2836**, F-statistic = **11.83** (p = **1.16e-22**), Residual SE = **5.676** on **369** df, AIC = **2437.9**, BIC = **2497.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.7877** | 2.1214 | ±4.2429 | **+22.526** | **2.30e-112** | *** |
| Education: graduate level (vs college) | +0.7423 | 0.6235 | ±1.2471 | +1.190 | 0.2339 |  |
| Education: high school or below (vs college) | -1.1545 | 1.1920 | ±2.3840 | -0.968 | 0.3328 |  |
| **Site: UCSD (vs UAB)** | **+4.4876** | 0.7823 | ±1.5646 | **+5.736** | **9.68e-09** | *** |
| Site: UW (vs UAB) | -0.8076 | 0.7587 | ±1.5174 | -1.064 | 0.2871 |  |
| Season: spring (vs autumn) | -0.9446 | 0.8334 | ±1.6668 | -1.133 | 0.2570 |  |
| **Season: summer (vs autumn)** | **+3.9760** | 0.9101 | ±1.8201 | **+4.369** | **1.25e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9195** | 0.8939 | ±1.7878 | **-4.385** | **1.16e-05** | *** |
| Age (years) | -0.0423 | 0.0268 | ±0.0536 | -1.576 | 0.1151 |  |
| BMI (kg/m2) | -0.0334 | 0.0395 | ±0.0791 | -0.844 | 0.3984 |  |
| Hypertension | +0.4650 | 0.6969 | ±1.3939 | +0.667 | 0.5047 |  |
| High cholesterol | -0.4136 | 0.6395 | ±1.2790 | -0.647 | 0.5178 |  |
| Kidney disease | -1.1291 | 1.2729 | ±2.5458 | -0.887 | 0.3751 |  |
| Circulatory disease | -0.3596 | 0.9513 | ±1.9027 | -0.378 | 0.7054 |  |
| Nocturnal time > 180 (%) | -0.7879 | 0.8696 | ±1.7392 | -0.906 | 0.3649 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 384; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **384**, R² = **0.0369**, Adj R² = **0.0030**, F-statistic = **1.09** (p = **0.3660**), Residual SE = **14.230** on **370** df, AIC = **3142.8**, BIC = **3198.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1843** | 6.0667 | ±12.1334 | **+20.635** | **1.34e-94** | *** |
| Education: graduate level (vs college) | -0.0316 | 1.5544 | ±3.1088 | -0.020 | 0.9838 |  |
| Education: high school or below (vs college) | +4.3297 | 2.9401 | ±5.8802 | +1.473 | 0.1408 |  |
| Site: UCSD (vs UAB) | -0.3830 | 1.9948 | ±3.9896 | -0.192 | 0.8477 |  |
| Site: UW (vs UAB) | +0.8781 | 1.9828 | ±3.9656 | +0.443 | 0.6579 |  |
| Season: spring (vs autumn) | +1.1125 | 2.1626 | ±4.3252 | +0.514 | 0.6069 |  |
| Season: summer (vs autumn) | +2.0181 | 2.2023 | ±4.4045 | +0.916 | 0.3595 |  |
| Season: winter (vs autumn) | +3.3276 | 2.1687 | ±4.3374 | +1.534 | 0.1249 |  |
| Age (years) | -0.0899 | 0.0752 | ±0.1504 | -1.196 | 0.2319 |  |
| BMI (kg/m2) | +0.1555 | 0.1078 | ±0.2155 | +1.443 | 0.1489 |  |
| Hypertension | +1.7134 | 1.7861 | ±3.5722 | +0.959 | 0.3374 |  |
| High cholesterol | +1.1137 | 1.6851 | ±3.3701 | +0.661 | 0.5087 |  |
| Kidney disease | -1.1039 | 2.3550 | ±4.7101 | -0.469 | 0.6393 |  |
| Circulatory disease | -0.8413 | 2.3008 | ±4.6016 | -0.366 | 0.7146 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **384**, R² = **0.0461**, Adj R² = **0.0099**, F-statistic = **1.27** (p = **0.2206**), Residual SE = **14.181** on **369** df, AIC = **3141.1**, BIC = **3200.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+150.9357** | 16.1466 | ±32.2933 | **+9.348** | **8.95e-21** | *** |
| Education: graduate level (vs college) | -0.0556 | 1.5617 | ±3.1233 | -0.036 | 0.9716 |  |
| Education: high school or below (vs college) | +4.5000 | 2.9369 | ±5.8738 | +1.532 | 0.1255 |  |
| Site: UCSD (vs UAB) | -0.4016 | 1.9930 | ±3.9861 | -0.202 | 0.8403 |  |
| Site: UW (vs UAB) | +0.7635 | 1.9906 | ±3.9812 | +0.384 | 0.7013 |  |
| Season: spring (vs autumn) | +0.4700 | 2.2050 | ±4.4100 | +0.213 | 0.8312 |  |
| Season: summer (vs autumn) | +2.3174 | 2.1889 | ±4.3777 | +1.059 | 0.2897 |  |
| Season: winter (vs autumn) | +3.1348 | 2.1884 | ±4.3769 | +1.432 | 0.1520 |  |
| Age (years) | -0.0745 | 0.0762 | ±0.1524 | -0.977 | 0.3285 |  |
| BMI (kg/m2) | +0.1737 | 0.1047 | ±0.2094 | +1.659 | 0.0971 | . |
| Hypertension | +1.9778 | 1.7680 | ±3.5360 | +1.119 | 0.2633 |  |
| High cholesterol | +1.7354 | 1.7609 | ±3.5218 | +0.986 | 0.3244 |  |
| Kidney disease | -1.5212 | 2.4366 | ±4.8731 | -0.624 | 0.5324 |  |
| Circulatory disease | -1.2655 | 2.3933 | ±4.7867 | -0.529 | 0.5970 |  |
| HbA1c (%) | -4.9252 | 2.8750 | ±5.7499 | -1.713 | 0.0867 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **384**, R² = **0.0482**, Adj R² = **0.0121**, F-statistic = **1.33** (p = **0.1844**), Residual SE = **14.166** on **369** df, AIC = **3140.3**, BIC = **3199.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+148.2311** | 13.0731 | ±26.1462 | **+11.339** | **8.45e-30** | *** |
| Education: graduate level (vs college) | +0.0461 | 1.5414 | ±3.0827 | +0.030 | 0.9761 |  |
| Education: high school or below (vs college) | +4.2063 | 2.9264 | ±5.8528 | +1.437 | 0.1506 |  |
| Site: UCSD (vs UAB) | -0.1741 | 1.9918 | ±3.9836 | -0.087 | 0.9304 |  |
| Site: UW (vs UAB) | +1.1244 | 2.0007 | ±4.0014 | +0.562 | 0.5741 |  |
| Season: spring (vs autumn) | +0.9242 | 2.1421 | ±4.2842 | +0.431 | 0.6661 |  |
| Season: summer (vs autumn) | +2.0383 | 2.2137 | ±4.4275 | +0.921 | 0.3572 |  |
| Season: winter (vs autumn) | +3.2408 | 2.1923 | ±4.3845 | +1.478 | 0.1393 |  |
| Age (years) | -0.0953 | 0.0753 | ±0.1505 | -1.266 | 0.2054 |  |
| BMI (kg/m2) | +0.1716 | 0.1064 | ±0.2129 | +1.612 | 0.1069 |  |
| Hypertension | +1.9494 | 1.7633 | ±3.5267 | +1.105 | 0.2690 |  |
| High cholesterol | +0.9720 | 1.6867 | ±3.3734 | +0.576 | 0.5644 |  |
| Kidney disease | -0.8728 | 2.4019 | ±4.8038 | -0.363 | 0.7163 |  |
| Circulatory disease | -0.9276 | 2.3394 | ±4.6787 | -0.397 | 0.6917 |  |
| **Mean glucose (mg/dL)** | **-0.2041** | 0.1017 | ±0.2034 | **-2.006** | **0.0448** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **384**, R² = **0.0482**, Adj R² = **0.0121**, F-statistic = **1.33** (p = **0.1844**), Residual SE = **14.166** on **369** df, AIC = **3140.3**, BIC = **3199.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+176.4700** | 26.3852 | ±52.7703 | **+6.688** | **2.26e-11** | *** |
| Education: graduate level (vs college) | +0.0461 | 1.5414 | ±3.0827 | +0.030 | 0.9761 |  |
| Education: high school or below (vs college) | +4.2063 | 2.9264 | ±5.8528 | +1.437 | 0.1506 |  |
| Site: UCSD (vs UAB) | -0.1741 | 1.9918 | ±3.9836 | -0.087 | 0.9304 |  |
| Site: UW (vs UAB) | +1.1244 | 2.0007 | ±4.0014 | +0.562 | 0.5741 |  |
| Season: spring (vs autumn) | +0.9242 | 2.1421 | ±4.2842 | +0.431 | 0.6661 |  |
| Season: summer (vs autumn) | +2.0383 | 2.2137 | ±4.4275 | +0.921 | 0.3572 |  |
| Season: winter (vs autumn) | +3.2408 | 2.1923 | ±4.3845 | +1.478 | 0.1393 |  |
| Age (years) | -0.0953 | 0.0753 | ±0.1505 | -1.266 | 0.2054 |  |
| BMI (kg/m2) | +0.1716 | 0.1064 | ±0.2129 | +1.612 | 0.1069 |  |
| Hypertension | +1.9494 | 1.7633 | ±3.5267 | +1.105 | 0.2690 |  |
| High cholesterol | +0.9720 | 1.6867 | ±3.3734 | +0.576 | 0.5644 |  |
| Kidney disease | -0.8728 | 2.4019 | ±4.8038 | -0.363 | 0.7163 |  |
| Circulatory disease | -0.9276 | 2.3394 | ±4.6787 | -0.397 | 0.6917 |  |
| **GMI (%)** | **-8.5314** | 4.2525 | ±8.5051 | **-2.006** | **0.0448** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **384**, R² = **0.0410**, Adj R² = **0.0046**, F-statistic = **1.13** (p = **0.3316**), Residual SE = **14.219** on **369** df, AIC = **3143.2**, BIC = **3202.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+136.5828** | 10.8933 | ±21.7867 | **+12.538** | **4.61e-36** | *** |
| Education: graduate level (vs college) | -0.1113 | 1.5648 | ±3.1297 | -0.071 | 0.9433 |  |
| Education: high school or below (vs college) | +4.1695 | 2.9510 | ±5.9019 | +1.413 | 0.1577 |  |
| Site: UCSD (vs UAB) | -0.1323 | 2.0205 | ±4.0410 | -0.065 | 0.9478 |  |
| Site: UW (vs UAB) | +1.0913 | 2.0127 | ±4.0253 | +0.542 | 0.5877 |  |
| Season: spring (vs autumn) | +1.0947 | 2.1606 | ±4.3211 | +0.507 | 0.6124 |  |
| Season: summer (vs autumn) | +2.0883 | 2.2192 | ±4.4384 | +0.941 | 0.3467 |  |
| Season: winter (vs autumn) | +3.3301 | 2.1845 | ±4.3689 | +1.524 | 0.1274 |  |
| Age (years) | -0.1021 | 0.0764 | ±0.1529 | -1.336 | 0.1815 |  |
| BMI (kg/m2) | +0.1783 | 0.1045 | ±0.2089 | +1.706 | 0.0879 | . |
| Hypertension | +1.7994 | 1.7797 | ±3.5594 | +1.011 | 0.3120 |  |
| High cholesterol | +1.0993 | 1.6889 | ±3.3778 | +0.651 | 0.5151 |  |
| Kidney disease | -1.1716 | 2.3897 | ±4.7794 | -0.490 | 0.6239 |  |
| Circulatory disease | -0.9275 | 2.3253 | ±4.6505 | -0.399 | 0.6900 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0997 | 0.0771 | ±0.1542 | -1.293 | 0.1960 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **384**, R² = **0.0418**, Adj R² = **0.0055**, F-statistic = **1.15** (p = **0.3125**), Residual SE = **14.213** on **369** df, AIC = **3142.8**, BIC = **3202.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.6598** | 8.0950 | ±16.1900 | **+16.388** | **2.33e-60** | *** |
| Education: graduate level (vs college) | -0.1524 | 1.5602 | ±3.1205 | -0.098 | 0.9222 |  |
| Education: high school or below (vs college) | +4.3596 | 2.9683 | ±5.9365 | +1.469 | 0.1419 |  |
| Site: UCSD (vs UAB) | -0.6265 | 1.9844 | ±3.9687 | -0.316 | 0.7522 |  |
| Site: UW (vs UAB) | +0.7287 | 1.9796 | ±3.9592 | +0.368 | 0.7128 |  |
| Season: spring (vs autumn) | +1.3286 | 2.1920 | ±4.3839 | +0.606 | 0.5444 |  |
| Season: summer (vs autumn) | +2.1614 | 2.2076 | ±4.4151 | +0.979 | 0.3275 |  |
| Season: winter (vs autumn) | +3.5571 | 2.1807 | ±4.3613 | +1.631 | 0.1028 |  |
| Age (years) | -0.0890 | 0.0755 | ±0.1510 | -1.179 | 0.2384 |  |
| BMI (kg/m2) | +0.1620 | 0.1068 | ±0.2136 | +1.516 | 0.1294 |  |
| Hypertension | +1.7210 | 1.7807 | ±3.5613 | +0.967 | 0.3338 |  |
| High cholesterol | +1.0071 | 1.6791 | ±3.3582 | +0.600 | 0.5486 |  |
| Kidney disease | -0.9156 | 2.4266 | ±4.8532 | -0.377 | 0.7059 |  |
| Circulatory disease | -0.7514 | 2.2984 | ±4.5967 | -0.327 | 0.7437 |  |
| Glucose SD, pooled (mg/dL) | -0.4576 | 0.3493 | ±0.6985 | -1.310 | 0.1901 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **384**, R² = **0.0428**, Adj R² = **0.0065**, F-statistic = **1.18** (p = **0.2888**), Residual SE = **14.206** on **369** df, AIC = **3142.4**, BIC = **3201.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.5422** | 7.6899 | ±15.3797 | **+17.236** | **1.43e-66** | *** |
| Education: graduate level (vs college) | -0.1816 | 1.5645 | ±3.1291 | -0.116 | 0.9076 |  |
| Education: high school or below (vs college) | +4.2876 | 2.9571 | ±5.9141 | +1.450 | 0.1471 |  |
| Site: UCSD (vs UAB) | -0.6657 | 1.9827 | ±3.9654 | -0.336 | 0.7371 |  |
| Site: UW (vs UAB) | +0.7068 | 1.9778 | ±3.9555 | +0.357 | 0.7208 |  |
| Season: spring (vs autumn) | +1.3131 | 2.1872 | ±4.3745 | +0.600 | 0.5483 |  |
| Season: summer (vs autumn) | +2.1260 | 2.2069 | ±4.4139 | +0.963 | 0.3354 |  |
| Season: winter (vs autumn) | +3.4706 | 2.1762 | ±4.3523 | +1.595 | 0.1108 |  |
| Age (years) | -0.0891 | 0.0756 | ±0.1512 | -1.179 | 0.2383 |  |
| BMI (kg/m2) | +0.1689 | 0.1053 | ±0.2106 | +1.604 | 0.1087 |  |
| Hypertension | +1.6727 | 1.7829 | ±3.5658 | +0.938 | 0.3482 |  |
| High cholesterol | +1.0236 | 1.6768 | ±3.3537 | +0.610 | 0.5416 |  |
| Kidney disease | -0.8925 | 2.4058 | ±4.8117 | -0.371 | 0.7107 |  |
| Circulatory disease | -0.8169 | 2.2739 | ±4.5478 | -0.359 | 0.7194 |  |
| Avg. daily SD (mg/dL) | -0.4975 | 0.3552 | ±0.7103 | -1.401 | 0.1613 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **384**, R² = **0.0372**, Adj R² = **0.0007**, F-statistic = **1.02** (p = **0.4332**), Residual SE = **14.247** on **369** df, AIC = **3144.7**, BIC = **3203.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.0580** | 8.0539 | ±16.1078 | **+15.776** | **4.56e-56** | *** |
| Education: graduate level (vs college) | -0.0681 | 1.5610 | ±3.1219 | -0.044 | 0.9652 |  |
| Education: high school or below (vs college) | +4.3472 | 2.9486 | ±5.8972 | +1.474 | 0.1404 |  |
| Site: UCSD (vs UAB) | -0.4598 | 2.0130 | ±4.0260 | -0.228 | 0.8193 |  |
| Site: UW (vs UAB) | +0.8204 | 2.0022 | ±4.0044 | +0.410 | 0.6820 |  |
| Season: spring (vs autumn) | +1.1826 | 2.1975 | ±4.3950 | +0.538 | 0.5905 |  |
| Season: summer (vs autumn) | +2.0573 | 2.2036 | ±4.4073 | +0.934 | 0.3505 |  |
| Season: winter (vs autumn) | +3.3927 | 2.1857 | ±4.3715 | +1.552 | 0.1206 |  |
| Age (years) | -0.0893 | 0.0757 | ±0.1514 | -1.179 | 0.2383 |  |
| BMI (kg/m2) | +0.1559 | 0.1079 | ±0.2158 | +1.445 | 0.1486 |  |
| Hypertension | +1.6960 | 1.7878 | ±3.5756 | +0.949 | 0.3428 |  |
| High cholesterol | +1.0965 | 1.6857 | ±3.3715 | +0.650 | 0.5154 |  |
| Kidney disease | -1.0787 | 2.3749 | ±4.7498 | -0.454 | 0.6497 |  |
| Circulatory disease | -0.8100 | 2.3143 | ±4.6287 | -0.350 | 0.7263 |  |
| CV (%) | -0.1290 | 0.3884 | ±0.7767 | -0.332 | 0.7397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **384**, R² = **0.0375**, Adj R² = **0.0010**, F-statistic = **1.03** (p = **0.4258**), Residual SE = **14.245** on **369** df, AIC = **3144.6**, BIC = **3203.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.7062** | 8.4894 | ±16.9787 | **+14.454** | **2.36e-47** | *** |
| Education: graduate level (vs college) | -0.0869 | 1.5602 | ±3.1204 | -0.056 | 0.9556 |  |
| Education: high school or below (vs college) | +4.3539 | 2.9496 | ±5.8993 | +1.476 | 0.1399 |  |
| Site: UCSD (vs UAB) | -0.4680 | 2.0085 | ±4.0169 | -0.233 | 0.8158 |  |
| Site: UW (vs UAB) | +0.8174 | 1.9983 | ±3.9966 | +0.409 | 0.6825 |  |
| Season: spring (vs autumn) | +1.2127 | 2.2002 | ±4.4004 | +0.551 | 0.5815 |  |
| Season: summer (vs autumn) | +2.0647 | 2.2045 | ±4.4090 | +0.937 | 0.3490 |  |
| Season: winter (vs autumn) | +3.4138 | 2.1863 | ±4.3726 | +1.561 | 0.1184 |  |
| Age (years) | -0.0894 | 0.0756 | ±0.1511 | -1.184 | 0.2365 |  |
| BMI (kg/m2) | +0.1559 | 0.1079 | ±0.2158 | +1.445 | 0.1485 |  |
| Hypertension | +1.7037 | 1.7882 | ±3.5763 | +0.953 | 0.3407 |  |
| High cholesterol | +1.0889 | 1.6839 | ±3.3678 | +0.647 | 0.5179 |  |
| Kidney disease | -1.0885 | 2.3819 | ±4.7638 | -0.457 | 0.6477 |  |
| Circulatory disease | -0.8031 | 2.3146 | ±4.6292 | -0.347 | 0.7286 |  |
| Mean / SD ratio | +0.3543 | 0.8040 | ±1.6079 | +0.441 | 0.6594 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **384**, R² = **0.0378**, Adj R² = **0.0013**, F-statistic = **1.03** (p = **0.4173**), Residual SE = **14.243** on **369** df, AIC = **3144.5**, BIC = **3203.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.3474** | 8.5238 | ±17.0475 | **+14.354** | **1.01e-46** | *** |
| Education: graduate level (vs college) | -0.1078 | 1.5635 | ±3.1270 | -0.069 | 0.9450 |  |
| Education: high school or below (vs college) | +4.3321 | 2.9515 | ±5.9029 | +1.468 | 0.1422 |  |
| Site: UCSD (vs UAB) | -0.4948 | 2.0053 | ±4.0105 | -0.247 | 0.8051 |  |
| Site: UW (vs UAB) | +0.8083 | 1.9947 | ±3.9895 | +0.405 | 0.6853 |  |
| Season: spring (vs autumn) | +1.2329 | 2.2025 | ±4.4049 | +0.560 | 0.5756 |  |
| Season: summer (vs autumn) | +2.0660 | 2.2079 | ±4.4157 | +0.936 | 0.3494 |  |
| Season: winter (vs autumn) | +3.4032 | 2.1831 | ±4.3662 | +1.559 | 0.1190 |  |
| Age (years) | -0.0893 | 0.0757 | ±0.1514 | -1.179 | 0.2383 |  |
| BMI (kg/m2) | +0.1596 | 0.1072 | ±0.2144 | +1.489 | 0.1364 |  |
| Hypertension | +1.6756 | 1.7932 | ±3.5865 | +0.934 | 0.3501 |  |
| High cholesterol | +1.0968 | 1.6844 | ±3.3687 | +0.651 | 0.5149 |  |
| Kidney disease | -1.0672 | 2.3694 | ±4.7388 | -0.450 | 0.6524 |  |
| Circulatory disease | -0.8200 | 2.2971 | ±4.5942 | -0.357 | 0.7211 |  |
| Avg. daily mean/SD | +0.3482 | 0.6683 | ±1.3367 | +0.521 | 0.6024 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **384**, R² = **0.0410**, Adj R² = **0.0046**, F-statistic = **1.13** (p = **0.3326**), Residual SE = **14.219** on **369** df, AIC = **3143.2**, BIC = **3202.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+118.6917** | 8.2137 | ±16.4274 | **+14.450** | **2.49e-47** | *** |
| Education: graduate level (vs college) | -0.0797 | 1.5567 | ±3.1134 | -0.051 | 0.9592 |  |
| Education: high school or below (vs college) | +4.0607 | 2.9309 | ±5.8618 | +1.385 | 0.1659 |  |
| Site: UCSD (vs UAB) | -0.1974 | 1.9886 | ±3.9772 | -0.099 | 0.9209 |  |
| Site: UW (vs UAB) | +1.1770 | 1.9710 | ±3.9420 | +0.597 | 0.5504 |  |
| Season: spring (vs autumn) | +0.9849 | 2.1765 | ±4.3530 | +0.453 | 0.6509 |  |
| Season: summer (vs autumn) | +2.0320 | 2.1838 | ±4.3676 | +0.930 | 0.3521 |  |
| Season: winter (vs autumn) | +3.1936 | 2.1584 | ±4.3169 | +1.480 | 0.1390 |  |
| Age (years) | -0.0786 | 0.0756 | ±0.1512 | -1.040 | 0.2982 |  |
| BMI (kg/m2) | +0.1652 | 0.1082 | ±0.2163 | +1.527 | 0.1268 |  |
| Hypertension | +1.7885 | 1.8096 | ±3.6193 | +0.988 | 0.3230 |  |
| High cholesterol | +0.9999 | 1.7035 | ±3.4071 | +0.587 | 0.5572 |  |
| Kidney disease | -1.3115 | 2.3088 | ±4.6176 | -0.568 | 0.5700 |  |
| Circulatory disease | -0.8399 | 2.3048 | ±4.6095 | -0.364 | 0.7156 |  |
| MAG (mg/dL/h) | +0.1615 | 0.1441 | ±0.2883 | +1.120 | 0.2626 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **384**, R² = **0.0374**, Adj R² = **0.0009**, F-statistic = **1.02** (p = **0.4274**), Residual SE = **14.246** on **369** df, AIC = **3144.6**, BIC = **3203.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.7944** | 8.5262 | ±17.0523 | **+14.988** | **8.73e-51** | *** |
| Education: graduate level (vs college) | -0.0429 | 1.5592 | ±3.1185 | -0.027 | 0.9781 |  |
| Education: high school or below (vs college) | +4.3301 | 2.9552 | ±5.9104 | +1.465 | 0.1429 |  |
| Site: UCSD (vs UAB) | -0.4635 | 1.9920 | ±3.9840 | -0.233 | 0.8160 |  |
| Site: UW (vs UAB) | +0.8204 | 1.9913 | ±3.9825 | +0.412 | 0.6804 |  |
| Season: spring (vs autumn) | +1.1779 | 2.2023 | ±4.4045 | +0.535 | 0.5927 |  |
| Season: summer (vs autumn) | +2.0432 | 2.2157 | ±4.4314 | +0.922 | 0.3564 |  |
| Season: winter (vs autumn) | +3.3895 | 2.1867 | ±4.3734 | +1.550 | 0.1211 |  |
| Age (years) | -0.0905 | 0.0754 | ±0.1508 | -1.200 | 0.2302 |  |
| BMI (kg/m2) | +0.1518 | 0.1096 | ±0.2193 | +1.385 | 0.1662 |  |
| Hypertension | +1.6764 | 1.8034 | ±3.6067 | +0.930 | 0.3526 |  |
| High cholesterol | +1.1205 | 1.6935 | ±3.3871 | +0.662 | 0.5082 |  |
| Kidney disease | -1.0670 | 2.3662 | ±4.7324 | -0.451 | 0.6520 |  |
| Circulatory disease | -0.8189 | 2.3056 | ±4.6112 | -0.355 | 0.7225 |  |
| Avg. daily range (mg/dL) | -0.0308 | 0.0789 | ±0.1577 | -0.390 | 0.6964 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **384**, R² = **0.0379**, Adj R² = **0.0014**, F-statistic = **1.04** (p = **0.4146**), Residual SE = **14.242** on **369** df, AIC = **3144.4**, BIC = **3203.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.3023** | 6.2995 | ±12.5990 | **+20.050** | **2.03e-89** | *** |
| Education: graduate level (vs college) | +0.0094 | 1.5609 | ±3.1218 | +0.006 | 0.9952 |  |
| Education: high school or below (vs college) | +4.4346 | 2.9431 | ±5.8861 | +1.507 | 0.1319 |  |
| Site: UCSD (vs UAB) | -0.4126 | 1.9987 | ±3.9974 | -0.206 | 0.8364 |  |
| Site: UW (vs UAB) | +0.9257 | 1.9892 | ±3.9784 | +0.465 | 0.6417 |  |
| Season: spring (vs autumn) | +1.2003 | 2.1911 | ±4.3823 | +0.548 | 0.5838 |  |
| Season: summer (vs autumn) | +2.1142 | 2.2123 | ±4.4246 | +0.956 | 0.3392 |  |
| Season: winter (vs autumn) | +3.4631 | 2.1990 | ±4.3980 | +1.575 | 0.1153 |  |
| Age (years) | -0.0891 | 0.0751 | ±0.1502 | -1.187 | 0.2353 |  |
| BMI (kg/m2) | +0.1559 | 0.1080 | ±0.2161 | +1.443 | 0.1490 |  |
| Hypertension | +1.7766 | 1.8058 | ±3.6117 | +0.984 | 0.3252 |  |
| High cholesterol | +1.1331 | 1.6892 | ±3.3785 | +0.671 | 0.5024 |  |
| Kidney disease | -1.2164 | 2.4176 | ±4.8351 | -0.503 | 0.6149 |  |
| Circulatory disease | -0.7569 | 2.3031 | ±4.6062 | -0.329 | 0.7424 |  |
| SD of daily means (mg/dL) | -0.2606 | 0.3944 | ±0.7888 | -0.661 | 0.5087 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **384**, R² = **0.0371**, Adj R² = **0.0005**, F-statistic = **1.01** (p = **0.4373**), Residual SE = **14.248** on **369** df, AIC = **3144.7**, BIC = **3204.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +58.6111 | 265.8494 | ±531.6988 | +0.220 | 0.8255 |  |
| Education: graduate level (vs college) | -0.0324 | 1.5589 | ±3.1178 | -0.021 | 0.9834 |  |
| Education: high school or below (vs college) | +4.3354 | 2.9494 | ±5.8987 | +1.470 | 0.1416 |  |
| Site: UCSD (vs UAB) | -0.4188 | 2.0060 | ±4.0120 | -0.209 | 0.8346 |  |
| Site: UW (vs UAB) | +0.8527 | 1.9944 | ±3.9889 | +0.428 | 0.6690 |  |
| Season: spring (vs autumn) | +1.1394 | 2.1831 | ±4.3661 | +0.522 | 0.6017 |  |
| Season: summer (vs autumn) | +2.0574 | 2.2267 | ±4.4533 | +0.924 | 0.3555 |  |
| Season: winter (vs autumn) | +3.3658 | 2.1886 | ±4.3773 | +1.538 | 0.1241 |  |
| Age (years) | -0.0906 | 0.0753 | ±0.1507 | -1.203 | 0.2292 |  |
| BMI (kg/m2) | +0.1538 | 0.1094 | ±0.2188 | +1.406 | 0.1599 |  |
| Hypertension | +1.7116 | 1.7897 | ±3.5794 | +0.956 | 0.3389 |  |
| High cholesterol | +1.1331 | 1.7036 | ±3.4071 | +0.665 | 0.5060 |  |
| Kidney disease | -1.0709 | 2.3684 | ±4.7368 | -0.452 | 0.6512 |  |
| Circulatory disease | -0.8264 | 2.3128 | ±4.6256 | -0.357 | 0.7209 |  |
| Time in range 70-180, pooled (%) | +0.6695 | 2.6679 | ±5.3358 | +0.251 | 0.8018 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **384**, R² = **0.0372**, Adj R² = **0.0007**, F-statistic = **1.02** (p = **0.4327**), Residual SE = **14.247** on **369** df, AIC = **3144.7**, BIC = **3203.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +37.0839 | 265.3609 | ±530.7218 | +0.140 | 0.8889 |  |
| Education: graduate level (vs college) | -0.0329 | 1.5586 | ±3.1172 | -0.021 | 0.9831 |  |
| Education: high school or below (vs college) | +4.3227 | 2.9511 | ±5.9021 | +1.465 | 0.1430 |  |
| Site: UCSD (vs UAB) | -0.4174 | 1.9997 | ±3.9993 | -0.209 | 0.8347 |  |
| Site: UW (vs UAB) | +0.8692 | 1.9899 | ±3.9798 | +0.437 | 0.6623 |  |
| Season: spring (vs autumn) | +1.1393 | 2.1794 | ±4.3588 | +0.523 | 0.6011 |  |
| Season: summer (vs autumn) | +2.0356 | 2.2178 | ±4.4356 | +0.918 | 0.3587 |  |
| Season: winter (vs autumn) | +3.3679 | 2.1884 | ±4.3767 | +1.539 | 0.1238 |  |
| Age (years) | -0.0918 | 0.0754 | ±0.1509 | -1.216 | 0.2238 |  |
| BMI (kg/m2) | +0.1546 | 0.1083 | ±0.2166 | +1.427 | 0.1534 |  |
| Hypertension | +1.6881 | 1.7971 | ±3.5941 | +0.939 | 0.3475 |  |
| High cholesterol | +1.1473 | 1.7098 | ±3.4195 | +0.671 | 0.5022 |  |
| Kidney disease | -1.0940 | 2.3823 | ±4.7646 | -0.459 | 0.6461 |  |
| Circulatory disease | -0.8023 | 2.3176 | ±4.6351 | -0.346 | 0.7292 |  |
| Avg. daily time in range 70-180 (%) | +0.8857 | 2.6634 | ±5.3269 | +0.333 | 0.7395 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.0369**, Adj R² = **0.0004**, F-statistic = **1.01** (p = **0.4425**), Residual SE = **14.250** on **369** df, AIC = **3144.8**, BIC = **3204.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.2080** | 6.0222 | ±12.0443 | **+20.791** | **5.20e-96** | *** |
| Education: graduate level (vs college) | -0.0337 | 1.5544 | ±3.1087 | -0.022 | 0.9827 |  |
| Education: high school or below (vs college) | +4.3270 | 2.9497 | ±5.8993 | +1.467 | 0.1424 |  |
| Site: UCSD (vs UAB) | -0.4066 | 1.9980 | ±3.9960 | -0.204 | 0.8387 |  |
| Site: UW (vs UAB) | +0.8628 | 1.9814 | ±3.9629 | +0.435 | 0.6632 |  |
| Season: spring (vs autumn) | +1.1302 | 2.1833 | ±4.3666 | +0.518 | 0.6047 |  |
| Season: summer (vs autumn) | +2.0269 | 2.2051 | ±4.4102 | +0.919 | 0.3580 |  |
| Season: winter (vs autumn) | +3.3398 | 2.1853 | ±4.3707 | +1.528 | 0.1264 |  |
| Age (years) | -0.0899 | 0.0754 | ±0.1508 | -1.192 | 0.2332 |  |
| BMI (kg/m2) | +0.1555 | 0.1079 | ±0.2158 | +1.441 | 0.1495 |  |
| Hypertension | +1.7223 | 1.7960 | ±3.5920 | +0.959 | 0.3376 |  |
| High cholesterol | +1.1135 | 1.6888 | ±3.3777 | +0.659 | 0.5097 |  |
| Kidney disease | -1.1182 | 2.3716 | ±4.7431 | -0.471 | 0.6373 |  |
| Circulatory disease | -0.8334 | 2.3124 | ±4.6249 | -0.360 | 0.7185 |  |
| Any reading < 54 during wear (0/1) | -0.1361 | 2.0109 | ±4.0217 | -0.068 | 0.9460 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.0390**, Adj R² = **0.0026**, F-statistic = **1.07** (p = **0.3834**), Residual SE = **14.234** on **369** df, AIC = **3144.0**, BIC = **3203.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.8927** | 6.0830 | ±12.1660 | **+20.531** | **1.13e-93** | *** |
| Education: graduate level (vs college) | -0.0215 | 1.5576 | ±3.1152 | -0.014 | 0.9890 |  |
| Education: high school or below (vs college) | +4.4597 | 2.9495 | ±5.8989 | +1.512 | 0.1305 |  |
| Site: UCSD (vs UAB) | -0.1575 | 2.0118 | ±4.0235 | -0.078 | 0.9376 |  |
| Site: UW (vs UAB) | +0.9909 | 1.9856 | ±3.9712 | +0.499 | 0.6177 |  |
| Season: spring (vs autumn) | +1.1430 | 2.1643 | ±4.3286 | +0.528 | 0.5974 |  |
| Season: summer (vs autumn) | +2.0023 | 2.1995 | ±4.3991 | +0.910 | 0.3627 |  |
| Season: winter (vs autumn) | +3.3383 | 2.1673 | ±4.3346 | +1.540 | 0.1235 |  |
| Age (years) | -0.0872 | 0.0750 | ±0.1501 | -1.162 | 0.2452 |  |
| BMI (kg/m2) | +0.1489 | 0.1093 | ±0.2187 | +1.362 | 0.1732 |  |
| Hypertension | +1.5991 | 1.7969 | ±3.5939 | +0.890 | 0.3735 |  |
| High cholesterol | +1.1294 | 1.6907 | ±3.3815 | +0.668 | 0.5042 |  |
| Kidney disease | -0.9787 | 2.3646 | ±4.7292 | -0.414 | 0.6790 |  |
| Circulatory disease | -0.9767 | 2.2764 | ±4.5527 | -0.429 | 0.6679 |  |
| Time < 54 (%) | +13.3508 | 14.3664 | ±28.7328 | +0.929 | 0.3527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.0422**, Adj R² = **0.0059**, F-statistic = **1.16** (p = **0.3029**), Residual SE = **14.210** on **369** df, AIC = **3142.7**, BIC = **3201.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.8045** | 6.0826 | ±12.1652 | **+20.518** | **1.48e-93** | *** |
| Education: graduate level (vs college) | -0.0933 | 1.5569 | ±3.1138 | -0.060 | 0.9522 |  |
| Education: high school or below (vs college) | +4.4149 | 2.9508 | ±5.9015 | +1.496 | 0.1346 |  |
| Site: UCSD (vs UAB) | -0.1796 | 1.9950 | ±3.9899 | -0.090 | 0.9283 |  |
| Site: UW (vs UAB) | +0.9569 | 1.9748 | ±3.9497 | +0.485 | 0.6280 |  |
| Season: spring (vs autumn) | +1.1852 | 2.1551 | ±4.3102 | +0.550 | 0.5824 |  |
| Season: summer (vs autumn) | +2.2503 | 2.1841 | ±4.3682 | +1.030 | 0.3029 |  |
| Season: winter (vs autumn) | +3.3787 | 2.1596 | ±4.3191 | +1.565 | 0.1177 |  |
| Age (years) | -0.0864 | 0.0751 | ±0.1502 | -1.150 | 0.2501 |  |
| BMI (kg/m2) | +0.1492 | 0.1086 | ±0.2172 | +1.374 | 0.1694 |  |
| Hypertension | +1.6038 | 1.7810 | ±3.5620 | +0.901 | 0.3679 |  |
| High cholesterol | +1.1495 | 1.6912 | ±3.3823 | +0.680 | 0.4967 |  |
| Kidney disease | -1.0350 | 2.3622 | ±4.7245 | -0.438 | 0.6613 |  |
| Circulatory disease | -1.1410 | 2.2740 | ±4.5480 | -0.502 | 0.6158 |  |
| Avg. daily time < 54 (%) | +25.4487 | 16.1985 | ±32.3970 | +1.571 | 0.1162 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.0384**, Adj R² = **0.0019**, F-statistic = **1.05** (p = **0.4005**), Residual SE = **14.239** on **369** df, AIC = **3144.2**, BIC = **3203.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.7046** | 6.0550 | ±12.1100 | **+20.595** | **3.02e-94** | *** |
| Education: graduate level (vs college) | +0.0076 | 1.5487 | ±3.0974 | +0.005 | 0.9961 |  |
| Education: high school or below (vs college) | +4.2440 | 2.9588 | ±5.9176 | +1.434 | 0.1515 |  |
| Site: UCSD (vs UAB) | -0.2702 | 2.0027 | ±4.0055 | -0.135 | 0.8927 |  |
| Site: UW (vs UAB) | +1.0109 | 1.9913 | ±3.9827 | +0.508 | 0.6117 |  |
| Season: spring (vs autumn) | +1.0515 | 2.1655 | ±4.3311 | +0.486 | 0.6273 |  |
| Season: summer (vs autumn) | +1.9971 | 2.2049 | ±4.4099 | +0.906 | 0.3651 |  |
| Season: winter (vs autumn) | +3.2314 | 2.1849 | ±4.3698 | +1.479 | 0.1391 |  |
| Age (years) | -0.0905 | 0.0755 | ±0.1511 | -1.198 | 0.2309 |  |
| BMI (kg/m2) | +0.1571 | 0.1079 | ±0.2158 | +1.456 | 0.1455 |  |
| Hypertension | +1.8279 | 1.7873 | ±3.5746 | +1.023 | 0.3064 |  |
| High cholesterol | +0.9926 | 1.7251 | ±3.4502 | +0.575 | 0.5650 |  |
| Kidney disease | -0.9016 | 2.3758 | ±4.7515 | -0.379 | 0.7043 |  |
| Circulatory disease | -0.8539 | 2.3111 | ±4.6223 | -0.369 | 0.7118 |  |
| Time 54-69, pooled (%) | +3.1584 | 4.3095 | ±8.6190 | +0.733 | 0.4636 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **384**, R² = **0.0386**, Adj R² = **0.0021**, F-statistic = **1.06** (p = **0.3959**), Residual SE = **14.237** on **369** df, AIC = **3144.1**, BIC = **3203.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.6996** | 6.0481 | ±12.0961 | **+20.618** | **1.89e-94** | *** |
| Education: graduate level (vs college) | +0.0271 | 1.5458 | ±3.0915 | +0.018 | 0.9860 |  |
| Education: high school or below (vs college) | +4.2235 | 2.9574 | ±5.9147 | +1.428 | 0.1533 |  |
| Site: UCSD (vs UAB) | -0.3151 | 1.9962 | ±3.9924 | -0.158 | 0.8746 |  |
| Site: UW (vs UAB) | +0.9474 | 1.9798 | ±3.9596 | +0.479 | 0.6323 |  |
| Season: spring (vs autumn) | +1.1370 | 2.1598 | ±4.3196 | +0.526 | 0.5986 |  |
| Season: summer (vs autumn) | +2.0751 | 2.2080 | ±4.4160 | +0.940 | 0.3473 |  |
| Season: winter (vs autumn) | +3.2585 | 2.1826 | ±4.3651 | +1.493 | 0.1355 |  |
| Age (years) | -0.0904 | 0.0756 | ±0.1512 | -1.196 | 0.2315 |  |
| BMI (kg/m2) | +0.1568 | 0.1077 | ±0.2155 | +1.455 | 0.1456 |  |
| Hypertension | +1.9088 | 1.7999 | ±3.5997 | +1.061 | 0.2889 |  |
| High cholesterol | +1.0206 | 1.7144 | ±3.4287 | +0.595 | 0.5516 |  |
| Kidney disease | -0.9534 | 2.3577 | ±4.7154 | -0.404 | 0.6859 |  |
| Circulatory disease | -0.8927 | 2.3100 | ±4.6201 | -0.386 | 0.6992 |  |
| Avg. daily time 54-69 (%) | +3.3492 | 4.1073 | ±8.2147 | +0.815 | 0.4148 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **384**, R² = **0.0390**, Adj R² = **0.0026**, F-statistic = **1.07** (p = **0.3834**), Residual SE = **14.234** on **369** df, AIC = **3144.0**, BIC = **3203.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.6014** | 6.0520 | ±12.1041 | **+20.588** | **3.49e-94** | *** |
| Education: graduate level (vs college) | +0.0126 | 1.5493 | ±3.0985 | +0.008 | 0.9935 |  |
| Education: high school or below (vs college) | +4.2713 | 2.9589 | ±5.9178 | +1.444 | 0.1489 |  |
| Site: UCSD (vs UAB) | -0.2065 | 2.0058 | ±4.0117 | -0.103 | 0.9180 |  |
| Site: UW (vs UAB) | +1.0475 | 1.9904 | ±3.9808 | +0.526 | 0.5987 |  |
| Season: spring (vs autumn) | +1.0554 | 2.1622 | ±4.3245 | +0.488 | 0.6255 |  |
| Season: summer (vs autumn) | +1.9918 | 2.2018 | ±4.4036 | +0.905 | 0.3657 |  |
| Season: winter (vs autumn) | +3.2281 | 2.1817 | ±4.3635 | +1.480 | 0.1390 |  |
| Age (years) | -0.0899 | 0.0755 | ±0.1509 | -1.191 | 0.2338 |  |
| BMI (kg/m2) | +0.1555 | 0.1081 | ±0.2162 | +1.439 | 0.1503 |  |
| Hypertension | +1.8064 | 1.7854 | ±3.5707 | +1.012 | 0.3117 |  |
| High cholesterol | +0.9889 | 1.7195 | ±3.4390 | +0.575 | 0.5652 |  |
| Kidney disease | -0.8575 | 2.3755 | ±4.7510 | -0.361 | 0.7181 |  |
| Circulatory disease | -0.8887 | 2.3037 | ±4.6073 | -0.386 | 0.6997 |  |
| Time < 70 (%) | +3.3556 | 3.8211 | ±7.6423 | +0.878 | 0.3799 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **384**, R² = **0.0396**, Adj R² = **0.0032**, F-statistic = **1.09** (p = **0.3667**), Residual SE = **14.229** on **369** df, AIC = **3143.7**, BIC = **3203.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.5614** | 6.0409 | ±12.0818 | **+20.620** | **1.83e-94** | *** |
| Education: graduate level (vs college) | +0.0274 | 1.5465 | ±3.0931 | +0.018 | 0.9859 |  |
| Education: high school or below (vs college) | +4.2190 | 2.9586 | ±5.9172 | +1.426 | 0.1539 |  |
| Site: UCSD (vs UAB) | -0.2727 | 1.9943 | ±3.9886 | -0.137 | 0.8912 |  |
| Site: UW (vs UAB) | +0.9710 | 1.9763 | ±3.9526 | +0.491 | 0.6232 |  |
| Season: spring (vs autumn) | +1.1522 | 2.1564 | ±4.3128 | +0.534 | 0.5931 |  |
| Season: summer (vs autumn) | +2.1201 | 2.2036 | ±4.4072 | +0.962 | 0.3360 |  |
| Season: winter (vs autumn) | +3.2549 | 2.1803 | ±4.3607 | +1.493 | 0.1355 |  |
| Age (years) | -0.0900 | 0.0756 | ±0.1512 | -1.191 | 0.2338 |  |
| BMI (kg/m2) | +0.1560 | 0.1078 | ±0.2155 | +1.448 | 0.1477 |  |
| Hypertension | +1.9242 | 1.7922 | ±3.5844 | +1.074 | 0.2830 |  |
| High cholesterol | +1.0107 | 1.7109 | ±3.4219 | +0.591 | 0.5547 |  |
| Kidney disease | -0.9180 | 2.3547 | ±4.7095 | -0.390 | 0.6967 |  |
| Circulatory disease | -0.9471 | 2.3055 | ±4.6109 | -0.411 | 0.6812 |  |
| Avg. daily time < 70 (%) | +3.9018 | 3.7271 | ±7.4542 | +1.047 | 0.2952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.0384**, Adj R² = **0.0019**, F-statistic = **1.05** (p = **0.4003**), Residual SE = **14.238** on **369** df, AIC = **3144.2**, BIC = **3203.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1243.3989 | 1484.9720 | ±2969.9440 | +0.837 | 0.4024 |  |
| Education: graduate level (vs college) | -0.0155 | 1.5587 | ±3.1174 | -0.010 | 0.9921 |  |
| Education: high school or below (vs college) | +4.4447 | 2.9491 | ±5.8983 | +1.507 | 0.1318 |  |
| Site: UCSD (vs UAB) | -0.1934 | 2.0120 | ±4.0240 | -0.096 | 0.9234 |  |
| Site: UW (vs UAB) | +0.9667 | 1.9864 | ±3.9728 | +0.487 | 0.6265 |  |
| Season: spring (vs autumn) | +1.1386 | 2.1657 | ±4.3315 | +0.526 | 0.5991 |  |
| Season: summer (vs autumn) | +2.0039 | 2.2035 | ±4.4070 | +0.909 | 0.3631 |  |
| Season: winter (vs autumn) | +3.3274 | 2.1705 | ±4.3409 | +1.533 | 0.1253 |  |
| Age (years) | -0.0873 | 0.0750 | ±0.1501 | -1.163 | 0.2449 |  |
| BMI (kg/m2) | +0.1504 | 0.1091 | ±0.2182 | +1.379 | 0.1678 |  |
| Hypertension | +1.6204 | 1.7965 | ±3.5930 | +0.902 | 0.3671 |  |
| High cholesterol | +1.1168 | 1.6916 | ±3.3832 | +0.660 | 0.5091 |  |
| Kidney disease | -0.9964 | 2.3651 | ±4.7301 | -0.421 | 0.6735 |  |
| Circulatory disease | -0.9535 | 2.2816 | ±4.5632 | -0.418 | 0.6760 |  |
| Time 54-250, pooled (%) | -11.1849 | 14.8479 | ±29.6959 | -0.753 | 0.4513 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.0408**, Adj R² = **0.0045**, F-statistic = **1.12** (p = **0.3361**), Residual SE = **14.220** on **369** df, AIC = **3143.2**, BIC = **3202.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2298.0656 | 1750.9408 | ±3501.8815 | +1.312 | 0.1894 |  |
| Education: graduate level (vs college) | -0.0679 | 1.5579 | ±3.1158 | -0.044 | 0.9652 |  |
| Education: high school or below (vs college) | +4.4156 | 2.9501 | ±5.9002 | +1.497 | 0.1345 |  |
| Site: UCSD (vs UAB) | -0.2078 | 1.9950 | ±3.9901 | -0.104 | 0.9170 |  |
| Site: UW (vs UAB) | +0.9326 | 1.9771 | ±3.9542 | +0.472 | 0.6371 |  |
| Season: spring (vs autumn) | +1.1757 | 2.1573 | ±4.3147 | +0.545 | 0.5858 |  |
| Season: summer (vs autumn) | +2.2144 | 2.1870 | ±4.3740 | +1.013 | 0.3113 |  |
| Season: winter (vs autumn) | +3.3514 | 2.1639 | ±4.3278 | +1.549 | 0.1214 |  |
| Age (years) | -0.0861 | 0.0751 | ±0.1503 | -1.146 | 0.2519 |  |
| BMI (kg/m2) | +0.1511 | 0.1084 | ±0.2167 | +1.395 | 0.1631 |  |
| Hypertension | +1.6257 | 1.7819 | ±3.5638 | +0.912 | 0.3616 |  |
| High cholesterol | +1.1227 | 1.6928 | ±3.3856 | +0.663 | 0.5072 |  |
| Kidney disease | -1.0394 | 2.3611 | ±4.7221 | -0.440 | 0.6598 |  |
| Circulatory disease | -1.0945 | 2.2806 | ±4.5611 | -0.480 | 0.6313 |  |
| Avg. daily time 54-250 (%) | -21.7328 | 17.5077 | ±35.0154 | -1.241 | 0.2145 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **384**, R² = **0.0390**, Adj R² = **0.0025**, F-statistic = **1.07** (p = **0.3842**), Residual SE = **14.234** on **369** df, AIC = **3144.0**, BIC = **3203.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.1033** | 6.2629 | ±12.5257 | **+20.135** | **3.64e-90** | *** |
| Education: graduate level (vs college) | -0.0020 | 1.5472 | ±3.0943 | -0.001 | 0.9990 |  |
| Education: high school or below (vs college) | +4.3103 | 2.9497 | ±5.8993 | +1.461 | 0.1439 |  |
| Site: UCSD (vs UAB) | -0.3849 | 1.9886 | ±3.9772 | -0.194 | 0.8465 |  |
| Site: UW (vs UAB) | +0.9065 | 1.9834 | ±3.9668 | +0.457 | 0.6476 |  |
| Season: spring (vs autumn) | +1.1669 | 2.1682 | ±4.3364 | +0.538 | 0.5905 |  |
| Season: summer (vs autumn) | +2.1375 | 2.2292 | ±4.4585 | +0.959 | 0.3376 |  |
| Season: winter (vs autumn) | +3.3898 | 2.1774 | ±4.3548 | +1.557 | 0.1195 |  |
| Age (years) | -0.0922 | 0.0755 | ±0.1510 | -1.222 | 0.2219 |  |
| BMI (kg/m2) | +0.1494 | 0.1125 | ±0.2251 | +1.328 | 0.1843 |  |
| Hypertension | +1.7726 | 1.7796 | ±3.5592 | +0.996 | 0.3192 |  |
| High cholesterol | +1.0923 | 1.6914 | ±3.3828 | +0.646 | 0.5184 |  |
| Kidney disease | -0.8149 | 2.4140 | ±4.8279 | -0.338 | 0.7357 |  |
| Circulatory disease | -0.8220 | 2.2999 | ±4.5998 | -0.357 | 0.7208 |  |
| Time 181-250, pooled (%) | -2.3514 | 2.8056 | ±5.6112 | -0.838 | 0.4020 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **384**, R² = **0.0399**, Adj R² = **0.0035**, F-statistic = **1.10** (p = **0.3600**), Residual SE = **14.227** on **369** df, AIC = **3143.6**, BIC = **3202.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2153** | 6.1729 | ±12.3458 | **+20.447** | **6.44e-93** | *** |
| Education: graduate level (vs college) | +0.0086 | 1.5433 | ±3.0866 | +0.006 | 0.9956 |  |
| Education: high school or below (vs college) | +4.2300 | 2.9552 | ±5.9105 | +1.431 | 0.1523 |  |
| Site: UCSD (vs UAB) | -0.4123 | 1.9815 | ±3.9629 | -0.208 | 0.8352 |  |
| Site: UW (vs UAB) | +0.9149 | 1.9808 | ±3.9616 | +0.462 | 0.6442 |  |
| Season: spring (vs autumn) | +1.2259 | 2.1781 | ±4.3562 | +0.563 | 0.5736 |  |
| Season: summer (vs autumn) | +2.1463 | 2.2308 | ±4.4616 | +0.962 | 0.3360 |  |
| Season: winter (vs autumn) | +3.4001 | 2.1806 | ±4.3612 | +1.559 | 0.1189 |  |
| Age (years) | -0.0958 | 0.0757 | ±0.1513 | -1.266 | 0.2054 |  |
| BMI (kg/m2) | +0.1530 | 0.1089 | ±0.2179 | +1.405 | 0.1601 |  |
| Hypertension | +1.7853 | 1.7800 | ±3.5600 | +1.003 | 0.3159 |  |
| High cholesterol | +1.1433 | 1.6969 | ±3.3938 | +0.674 | 0.5005 |  |
| Kidney disease | -0.9388 | 2.4114 | ±4.8229 | -0.389 | 0.6970 |  |
| Circulatory disease | -0.7939 | 2.2829 | ±4.5657 | -0.348 | 0.7280 |  |
| Avg. daily time 181-250 (%) | -2.7980 | 2.9185 | ±5.8370 | -0.959 | 0.3377 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **384**, R² = **0.0391**, Adj R² = **0.0026**, F-statistic = **1.07** (p = **0.3811**), Residual SE = **14.233** on **369** df, AIC = **3143.9**, BIC = **3203.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.1348** | 6.2671 | ±12.5342 | **+20.126** | **4.33e-90** | *** |
| Education: graduate level (vs college) | -0.0029 | 1.5475 | ±3.0949 | -0.002 | 0.9985 |  |
| Education: high school or below (vs college) | +4.3085 | 2.9497 | ±5.8995 | +1.461 | 0.1441 |  |
| Site: UCSD (vs UAB) | -0.3851 | 1.9884 | ±3.9767 | -0.194 | 0.8464 |  |
| Site: UW (vs UAB) | +0.9086 | 1.9833 | ±3.9665 | +0.458 | 0.6469 |  |
| Season: spring (vs autumn) | +1.1682 | 2.1680 | ±4.3360 | +0.539 | 0.5900 |  |
| Season: summer (vs autumn) | +2.1408 | 2.2294 | ±4.4589 | +0.960 | 0.3369 |  |
| Season: winter (vs autumn) | +3.3934 | 2.1774 | ±4.3549 | +1.558 | 0.1191 |  |
| Age (years) | -0.0924 | 0.0755 | ±0.1510 | -1.223 | 0.2212 |  |
| BMI (kg/m2) | +0.1491 | 0.1127 | ±0.2253 | +1.324 | 0.1856 |  |
| Hypertension | +1.7736 | 1.7794 | ±3.5588 | +0.997 | 0.3189 |  |
| High cholesterol | +1.0939 | 1.6914 | ±3.3829 | +0.647 | 0.5178 |  |
| Kidney disease | -0.8079 | 2.4157 | ±4.8313 | -0.334 | 0.7380 |  |
| Circulatory disease | -0.8218 | 2.2997 | ±4.5994 | -0.357 | 0.7208 |  |
| Time > 180 (%) | -2.4127 | 2.8048 | ±5.6095 | -0.860 | 0.3897 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **384**, R² = **0.0401**, Adj R² = **0.0036**, F-statistic = **1.10** (p = **0.3561**), Residual SE = **14.226** on **369** df, AIC = **3143.5**, BIC = **3202.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2491** | 6.1743 | ±12.3485 | **+20.448** | **6.30e-93** | *** |
| Education: graduate level (vs college) | +0.0074 | 1.5436 | ±3.0873 | +0.005 | 0.9962 |  |
| Education: high school or below (vs college) | +4.2260 | 2.9554 | ±5.9108 | +1.430 | 0.1527 |  |
| Site: UCSD (vs UAB) | -0.4132 | 1.9811 | ±3.9622 | -0.209 | 0.8348 |  |
| Site: UW (vs UAB) | +0.9175 | 1.9806 | ±3.9612 | +0.463 | 0.6432 |  |
| Season: spring (vs autumn) | +1.2284 | 2.1780 | ±4.3559 | +0.564 | 0.5728 |  |
| Season: summer (vs autumn) | +2.1495 | 2.2310 | ±4.4620 | +0.963 | 0.3353 |  |
| Season: winter (vs autumn) | +3.4043 | 2.1807 | ±4.3613 | +1.561 | 0.1185 |  |
| Age (years) | -0.0960 | 0.0757 | ±0.1513 | -1.269 | 0.2043 |  |
| BMI (kg/m2) | +0.1529 | 0.1090 | ±0.2180 | +1.403 | 0.1607 |  |
| Hypertension | +1.7862 | 1.7798 | ±3.5597 | +1.004 | 0.3156 |  |
| High cholesterol | +1.1468 | 1.6970 | ±3.3940 | +0.676 | 0.4992 |  |
| Kidney disease | -0.9358 | 2.4130 | ±4.8260 | -0.388 | 0.6982 |  |
| Circulatory disease | -0.7931 | 2.2822 | ±4.5644 | -0.348 | 0.7282 |  |
| Avg. daily time > 180 (%) | -2.8627 | 2.9162 | ±5.8324 | -0.982 | 0.3263 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **384**, R² = **0.0378**, Adj R² = **0.0013**, F-statistic = **1.03** (p = **0.4175**), Residual SE = **14.243** on **369** df, AIC = **3144.5**, BIC = **3203.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.8187** | 6.1997 | ±12.3993 | **+20.133** | **3.78e-90** | *** |
| Education: graduate level (vs college) | +0.0211 | 1.5633 | ±3.1266 | +0.014 | 0.9892 |  |
| Education: high school or below (vs college) | +4.3463 | 2.9368 | ±5.8736 | +1.480 | 0.1389 |  |
| Site: UCSD (vs UAB) | -0.3341 | 2.0073 | ±4.0147 | -0.166 | 0.8678 |  |
| Site: UW (vs UAB) | +0.8537 | 1.9837 | ±3.9674 | +0.430 | 0.6670 |  |
| Season: spring (vs autumn) | +1.0686 | 2.1661 | ±4.3321 | +0.493 | 0.6218 |  |
| Season: summer (vs autumn) | +2.0067 | 2.1994 | ±4.3988 | +0.912 | 0.3616 |  |
| Season: winter (vs autumn) | +3.2190 | 2.1625 | ±4.3251 | +1.489 | 0.1366 |  |
| Age (years) | -0.0821 | 0.0765 | ±0.1530 | -1.073 | 0.2831 |  |
| BMI (kg/m2) | +0.1492 | 0.1097 | ±0.2193 | +1.361 | 0.1736 |  |
| Hypertension | +1.6556 | 1.7941 | ±3.5882 | +0.923 | 0.3561 |  |
| High cholesterol | +1.0648 | 1.6813 | ±3.3627 | +0.633 | 0.5265 |  |
| Kidney disease | -1.1354 | 2.3606 | ±4.7213 | -0.481 | 0.6305 |  |
| Circulatory disease | -0.8402 | 2.3112 | ±4.6224 | -0.364 | 0.7162 |  |
| Nocturnal time > 180 (%) | +1.3116 | 2.1243 | ±4.2487 | +0.617 | 0.5370 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Healthy group (no diabetes + pre-diabetes / lifestyle) - Home environment

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 112 single-predictor tests; 8 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 384): best single predictor out of sample is **%<54 (daily avg)** (CV R² 0.049 vs 0.047 for covariates alone, gain +0.002; +0.0947 per SD, p = 0.139). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Indoor temperature, mean (deg C)** (n = 384): best single predictor out of sample is **Daily range** (CV R² 0.298 vs 0.284 for covariates alone, gain +0.014; -0.27 per SD, p = 0.005). Raw p < 0.05 (FDR not applicable here): Daily range (p = 0.005), SD (daily avg) (p = 0.010), Mean/SD (daily avg) (p = 0.013), CV (p = 0.027), SD (pooled) (p = 0.029).
- **Indoor relative humidity, mean (%)** (n = 384): best single predictor out of sample is **TIR 70-180 (daily avg)** (CV R² 0.249 vs 0.250 for covariates alone, gain -0.001; -0.345 per SD, p = 0.259). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor VOC index, mean** (n = 384): best single predictor out of sample is **%<54 (daily avg)** (CV R² -0.066 vs -0.071 for covariates alone, gain +0.004; +1.05 per SD, p = 0.116). Raw p < 0.05 (FDR not applicable here): GMI (p = 0.045), Mean glucose (p = 0.045).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Indoor temperature, mean (deg C) (+0.014, via Daily range); Indoor VOC index, mean (+0.004, via %<54 (daily avg)); Indoor PM2.5, log(1 + mean ug/m3) (+0.002, via %<54 (daily avg)); Indoor relative humidity, mean (%) (-0.001, via TIR 70-180 (daily avg)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (0 FDR-significant / 6 raw-significant of 32); CGM level (0 FDR-significant / 2 raw-significant of 12); HbA1c (0 FDR-significant / 0 raw-significant of 4).
Level metrics: 0 FDR-significant (2 raw); variability metrics: 0 FDR-significant (6 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Indoor PM2.5, log(1 + mean ug/m3) (%<70 (pooled), ΔAIC -3.8); Indoor temperature, mean (Daily range, ΔAIC -8.0).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
