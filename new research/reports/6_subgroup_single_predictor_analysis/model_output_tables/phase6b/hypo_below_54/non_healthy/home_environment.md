# Phase 6b model output tables - Hypoglycaemia exposure: at least one reading < 54 - Non-healthy group (T2D non-insulin + T2D insulin) - Home environment

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 228; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **228**, R² = **0.1753**, Adj R² = **0.1252**, F-statistic = **3.50** (p = **5.88e-05**), Residual SE = **1.038** on **214** df, AIC = **677.7**, BIC = **725.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1714** | 0.7188 | ±1.4377 | **+4.412** | **1.03e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4525** | 0.1497 | ±0.2994 | **-3.022** | **0.0025** | ** |
| Education: high school or below (vs college) | +0.3675 | 0.2414 | ±0.4829 | +1.522 | 0.1279 |  |
| Site: UCSD (vs UAB) | +0.1899 | 0.1630 | ±0.3260 | +1.165 | 0.2441 |  |
| Site: UW (vs UAB) | -0.3509 | 0.1966 | ±0.3932 | -1.785 | 0.0743 | . |
| **Season: spring (vs autumn)** | **-0.4284** | 0.1937 | ±0.3875 | **-2.211** | **0.0270** | * |
| Season: summer (vs autumn) | +0.0342 | 0.2153 | ±0.4305 | +0.159 | 0.8737 |  |
| Season: winter (vs autumn) | -0.0137 | 0.2386 | ±0.4772 | -0.057 | 0.9543 |  |
| **Age (years)** | **-0.0165** | 0.0068 | ±0.0136 | **-2.427** | **0.0152** | * |
| BMI (kg/m2) | +0.0044 | 0.0120 | ±0.0239 | +0.368 | 0.7129 |  |
| Hypertension | +0.1587 | 0.1563 | ±0.3127 | +1.015 | 0.3102 |  |
| High cholesterol | +0.0412 | 0.1550 | ±0.3101 | +0.266 | 0.7905 |  |
| Kidney disease | -0.0180 | 0.2294 | ±0.4588 | -0.078 | 0.9375 |  |
| Circulatory disease | -0.1277 | 0.1744 | ±0.3487 | -0.732 | 0.4641 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **228**, R² = **0.1918**, Adj R² = **0.1387**, F-statistic = **3.61** (p = **2.24e-05**), Residual SE = **1.030** on **213** df, AIC = **675.1**, BIC = **726.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4538** | 0.7657 | ±1.5314 | **+3.205** | **0.0014** | ** |
| **Education: graduate level (vs college)** | **-0.4093** | 0.1486 | ±0.2971 | **-2.755** | **0.0059** | ** |
| Education: high school or below (vs college) | +0.3306 | 0.2347 | ±0.4694 | +1.409 | 0.1590 |  |
| Site: UCSD (vs UAB) | +0.1945 | 0.1643 | ±0.3286 | +1.184 | 0.2363 |  |
| Site: UW (vs UAB) | -0.3368 | 0.1957 | ±0.3913 | -1.721 | 0.0852 | . |
| **Season: spring (vs autumn)** | **-0.4552** | 0.1950 | ±0.3901 | **-2.334** | **0.0196** | * |
| Season: summer (vs autumn) | +0.0469 | 0.2156 | ±0.4311 | +0.218 | 0.8278 |  |
| Season: winter (vs autumn) | -0.0343 | 0.2365 | ±0.4730 | -0.145 | 0.8847 |  |
| **Age (years)** | **-0.0185** | 0.0069 | ±0.0138 | **-2.674** | **0.0075** | ** |
| BMI (kg/m2) | +0.0041 | 0.0117 | ±0.0234 | +0.346 | 0.7296 |  |
| Hypertension | +0.1390 | 0.1564 | ±0.3128 | +0.889 | 0.3741 |  |
| High cholesterol | +0.0604 | 0.1559 | ±0.3119 | +0.387 | 0.6987 |  |
| Kidney disease | -0.0311 | 0.2186 | ±0.4372 | -0.142 | 0.8870 |  |
| Circulatory disease | -0.1304 | 0.1738 | ±0.3476 | -0.751 | 0.4529 |  |
| HbA1c (%) | +0.1321 | 0.0733 | ±0.1466 | +1.803 | 0.0715 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **228**, R² = **0.1753**, Adj R² = **0.1211**, F-statistic = **3.23** (p = **1.15e-04**), Residual SE = **1.041** on **213** df, AIC = **679.7**, BIC = **731.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1601** | 0.7509 | ±1.5018 | **+4.209** | **2.57e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4522** | 0.1507 | ±0.3013 | **-3.002** | **0.0027** | ** |
| Education: high school or below (vs college) | +0.3670 | 0.2434 | ±0.4868 | +1.508 | 0.1316 |  |
| Site: UCSD (vs UAB) | +0.1899 | 0.1635 | ±0.3270 | +1.161 | 0.2456 |  |
| Site: UW (vs UAB) | -0.3507 | 0.1966 | ±0.3933 | -1.783 | 0.0745 | . |
| **Season: spring (vs autumn)** | **-0.4294** | 0.1969 | ±0.3937 | **-2.181** | **0.0292** | * |
| Season: summer (vs autumn) | +0.0342 | 0.2160 | ±0.4319 | +0.158 | 0.8743 |  |
| Season: winter (vs autumn) | -0.0145 | 0.2412 | ±0.4824 | -0.060 | 0.9522 |  |
| **Age (years)** | **-0.0165** | 0.0068 | ±0.0137 | **-2.415** | **0.0157** | * |
| BMI (kg/m2) | +0.0044 | 0.0120 | ±0.0240 | +0.367 | 0.7134 |  |
| Hypertension | +0.1585 | 0.1584 | ±0.3167 | +1.001 | 0.3170 |  |
| High cholesterol | +0.0415 | 0.1563 | ±0.3125 | +0.265 | 0.7907 |  |
| Kidney disease | -0.0188 | 0.2264 | ±0.4529 | -0.083 | 0.9339 |  |
| Circulatory disease | -0.1279 | 0.1762 | ±0.3523 | -0.726 | 0.4677 |  |
| Mean glucose (mg/dL) | +0.0001 | 0.0021 | ±0.0043 | +0.040 | 0.9680 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **228**, R² = **0.1753**, Adj R² = **0.1211**, F-statistic = **3.23** (p = **1.15e-04**), Residual SE = **1.041** on **213** df, AIC = **679.7**, BIC = **731.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1483** | 0.8824 | ±1.7648 | **+3.568** | **3.60e-04** | *** |
| **Education: graduate level (vs college)** | **-0.4522** | 0.1507 | ±0.3013 | **-3.002** | **0.0027** | ** |
| Education: high school or below (vs college) | +0.3670 | 0.2434 | ±0.4868 | +1.508 | 0.1316 |  |
| Site: UCSD (vs UAB) | +0.1899 | 0.1635 | ±0.3270 | +1.161 | 0.2456 |  |
| Site: UW (vs UAB) | -0.3507 | 0.1966 | ±0.3933 | -1.783 | 0.0745 | . |
| **Season: spring (vs autumn)** | **-0.4294** | 0.1969 | ±0.3937 | **-2.181** | **0.0292** | * |
| Season: summer (vs autumn) | +0.0342 | 0.2160 | ±0.4319 | +0.158 | 0.8743 |  |
| Season: winter (vs autumn) | -0.0145 | 0.2412 | ±0.4824 | -0.060 | 0.9522 |  |
| **Age (years)** | **-0.0165** | 0.0068 | ±0.0137 | **-2.415** | **0.0157** | * |
| BMI (kg/m2) | +0.0044 | 0.0120 | ±0.0240 | +0.367 | 0.7134 |  |
| Hypertension | +0.1585 | 0.1584 | ±0.3167 | +1.001 | 0.3170 |  |
| High cholesterol | +0.0415 | 0.1563 | ±0.3125 | +0.265 | 0.7907 |  |
| Kidney disease | -0.0188 | 0.2264 | ±0.4529 | -0.083 | 0.9339 |  |
| Circulatory disease | -0.1279 | 0.1762 | ±0.3523 | -0.726 | 0.4677 |  |
| GMI (%) | +0.0036 | 0.0891 | ±0.1781 | +0.040 | 0.9680 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **228**, R² = **0.1755**, Adj R² = **0.1213**, F-statistic = **3.24** (p = **1.14e-04**), Residual SE = **1.041** on **213** df, AIC = **679.7**, BIC = **731.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1139** | 0.7343 | ±1.4685 | **+4.241** | **2.23e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4523** | 0.1503 | ±0.3006 | **-3.010** | **0.0026** | ** |
| Education: high school or below (vs college) | +0.3648 | 0.2424 | ±0.4848 | +1.505 | 0.1323 |  |
| Site: UCSD (vs UAB) | +0.1897 | 0.1637 | ±0.3274 | +1.159 | 0.2465 |  |
| Site: UW (vs UAB) | -0.3504 | 0.1973 | ±0.3946 | -1.776 | 0.0757 | . |
| **Season: spring (vs autumn)** | **-0.4337** | 0.1989 | ±0.3978 | **-2.181** | **0.0292** | * |
| Season: summer (vs autumn) | +0.0348 | 0.2161 | ±0.4323 | +0.161 | 0.8722 |  |
| Season: winter (vs autumn) | -0.0177 | 0.2426 | ±0.4853 | -0.073 | 0.9419 |  |
| **Age (years)** | **-0.0165** | 0.0068 | ±0.0136 | **-2.425** | **0.0153** | * |
| BMI (kg/m2) | +0.0044 | 0.0120 | ±0.0240 | +0.368 | 0.7127 |  |
| Hypertension | +0.1567 | 0.1594 | ±0.3188 | +0.983 | 0.3255 |  |
| High cholesterol | +0.0415 | 0.1560 | ±0.3121 | +0.266 | 0.7901 |  |
| Kidney disease | -0.0189 | 0.2286 | ±0.4572 | -0.082 | 0.9343 |  |
| Circulatory disease | -0.1292 | 0.1770 | ±0.3540 | -0.730 | 0.4655 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0004 | 0.0023 | ±0.0047 | +0.186 | 0.8521 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1763**, Adj R² = **0.1221**, F-statistic = **3.26** (p = **1.05e-04**), Residual SE = **1.040** on **213** df, AIC = **679.5**, BIC = **730.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1136** | 0.7436 | ±1.4872 | **+4.187** | **2.82e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4428** | 0.1491 | ±0.2983 | **-2.969** | **0.0030** | ** |
| Education: high school or below (vs college) | +0.3514 | 0.2485 | ±0.4970 | +1.414 | 0.1574 |  |
| Site: UCSD (vs UAB) | +0.1921 | 0.1630 | ±0.3261 | +1.178 | 0.2387 |  |
| Site: UW (vs UAB) | -0.3454 | 0.1968 | ±0.3935 | -1.755 | 0.0792 | . |
| **Season: spring (vs autumn)** | **-0.4335** | 0.1949 | ±0.3897 | **-2.225** | **0.0261** | * |
| Season: summer (vs autumn) | +0.0374 | 0.2164 | ±0.4328 | +0.173 | 0.8630 |  |
| Season: winter (vs autumn) | -0.0189 | 0.2395 | ±0.4790 | -0.079 | 0.9370 |  |
| **Age (years)** | **-0.0170** | 0.0069 | ±0.0137 | **-2.481** | **0.0131** | * |
| BMI (kg/m2) | +0.0047 | 0.0122 | ±0.0243 | +0.386 | 0.6995 |  |
| Hypertension | +0.1568 | 0.1578 | ±0.3157 | +0.993 | 0.3205 |  |
| High cholesterol | +0.0458 | 0.1572 | ±0.3144 | +0.291 | 0.7707 |  |
| Kidney disease | -0.0413 | 0.2241 | ±0.4482 | -0.184 | 0.8539 |  |
| Circulatory disease | -0.1271 | 0.1750 | ±0.3500 | -0.726 | 0.4676 |  |
| Glucose SD, pooled (mg/dL) | +0.0023 | 0.0047 | ±0.0094 | +0.497 | 0.6189 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1756**, Adj R² = **0.1214**, F-statistic = **3.24** (p = **1.12e-04**), Residual SE = **1.041** on **213** df, AIC = **679.6**, BIC = **731.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1357** | 0.7439 | ±1.4878 | **+4.215** | **2.50e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4468** | 0.1493 | ±0.2986 | **-2.993** | **0.0028** | ** |
| Education: high school or below (vs college) | +0.3565 | 0.2515 | ±0.5031 | +1.417 | 0.1564 |  |
| Site: UCSD (vs UAB) | +0.1910 | 0.1630 | ±0.3259 | +1.172 | 0.2413 |  |
| Site: UW (vs UAB) | -0.3483 | 0.1969 | ±0.3937 | -1.769 | 0.0769 | . |
| **Season: spring (vs autumn)** | **-0.4330** | 0.1948 | ±0.3895 | **-2.223** | **0.0262** | * |
| Season: summer (vs autumn) | +0.0357 | 0.2164 | ±0.4328 | +0.165 | 0.8690 |  |
| Season: winter (vs autumn) | -0.0160 | 0.2395 | ±0.4790 | -0.067 | 0.9466 |  |
| **Age (years)** | **-0.0168** | 0.0069 | ±0.0137 | **-2.452** | **0.0142** | * |
| BMI (kg/m2) | +0.0046 | 0.0122 | ±0.0244 | +0.378 | 0.7057 |  |
| Hypertension | +0.1584 | 0.1571 | ±0.3142 | +1.008 | 0.3133 |  |
| High cholesterol | +0.0437 | 0.1567 | ±0.3133 | +0.279 | 0.7801 |  |
| Kidney disease | -0.0317 | 0.2231 | ±0.4462 | -0.142 | 0.8868 |  |
| Circulatory disease | -0.1268 | 0.1747 | ±0.3494 | -0.726 | 0.4680 |  |
| Avg. daily SD (mg/dL) | +0.0016 | 0.0053 | ±0.0106 | +0.299 | 0.7647 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **228**, R² = **0.1785**, Adj R² = **0.1245**, F-statistic = **3.31** (p = **8.49e-05**), Residual SE = **1.039** on **213** df, AIC = **678.8**, BIC = **730.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0075** | 0.7850 | ±1.5700 | **+3.831** | **1.27e-04** | *** |
| **Education: graduate level (vs college)** | **-0.4309** | 0.1472 | ±0.2945 | **-2.926** | **0.0034** | ** |
| Education: high school or below (vs college) | +0.3319 | 0.2537 | ±0.5075 | +1.308 | 0.1908 |  |
| Site: UCSD (vs UAB) | +0.1961 | 0.1631 | ±0.3261 | +1.202 | 0.2292 |  |
| Site: UW (vs UAB) | -0.3395 | 0.1979 | ±0.3957 | -1.716 | 0.0862 | . |
| **Season: spring (vs autumn)** | **-0.4281** | 0.1955 | ±0.3910 | **-2.190** | **0.0285** | * |
| Season: summer (vs autumn) | +0.0362 | 0.2165 | ±0.4330 | +0.167 | 0.8673 |  |
| Season: winter (vs autumn) | -0.0162 | 0.2393 | ±0.4787 | -0.068 | 0.9459 |  |
| **Age (years)** | **-0.0182** | 0.0069 | ±0.0139 | **-2.619** | **0.0088** | ** |
| BMI (kg/m2) | +0.0050 | 0.0122 | ±0.0244 | +0.412 | 0.6803 |  |
| Hypertension | +0.1589 | 0.1570 | ±0.3140 | +1.012 | 0.3114 |  |
| High cholesterol | +0.0478 | 0.1577 | ±0.3155 | +0.303 | 0.7617 |  |
| Kidney disease | -0.0700 | 0.2296 | ±0.4592 | -0.305 | 0.7604 |  |
| Circulatory disease | -0.1237 | 0.1750 | ±0.3500 | -0.707 | 0.4794 |  |
| CV (%) | +0.0099 | 0.0124 | ±0.0248 | +0.798 | 0.4246 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **228**, R² = **0.1782**, Adj R² = **0.1242**, F-statistic = **3.30** (p = **8.69e-05**), Residual SE = **1.039** on **213** df, AIC = **678.9**, BIC = **730.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4817** | 0.7621 | ±1.5242 | **+4.569** | **4.91e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4321** | 0.1469 | ±0.2937 | **-2.942** | **0.0033** | ** |
| Education: high school or below (vs college) | +0.3326 | 0.2499 | ±0.4999 | +1.331 | 0.1833 |  |
| Site: UCSD (vs UAB) | +0.1908 | 0.1640 | ±0.3280 | +1.163 | 0.2447 |  |
| Site: UW (vs UAB) | -0.3437 | 0.1975 | ±0.3950 | -1.740 | 0.0818 | . |
| **Season: spring (vs autumn)** | **-0.4334** | 0.1946 | ±0.3891 | **-2.227** | **0.0259** | * |
| Season: summer (vs autumn) | +0.0307 | 0.2161 | ±0.4322 | +0.142 | 0.8872 |  |
| Season: winter (vs autumn) | -0.0176 | 0.2387 | ±0.4775 | -0.074 | 0.9414 |  |
| **Age (years)** | **-0.0183** | 0.0071 | ±0.0141 | **-2.593** | **0.0095** | ** |
| BMI (kg/m2) | +0.0047 | 0.0120 | ±0.0240 | +0.395 | 0.6928 |  |
| Hypertension | +0.1627 | 0.1555 | ±0.3111 | +1.046 | 0.2954 |  |
| High cholesterol | +0.0486 | 0.1575 | ±0.3150 | +0.309 | 0.7574 |  |
| Kidney disease | -0.0541 | 0.2258 | ±0.4517 | -0.239 | 0.8108 |  |
| Circulatory disease | -0.1309 | 0.1754 | ±0.3508 | -0.746 | 0.4555 |  |
| Mean / SD ratio | -0.0484 | 0.0544 | ±0.1087 | -0.891 | 0.3728 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1780**, Adj R² = **0.1240**, F-statistic = **3.29** (p = **8.88e-05**), Residual SE = **1.039** on **213** df, AIC = **679.0**, BIC = **730.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4589** | 0.7584 | ±1.5169 | **+4.560** | **5.10e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4308** | 0.1478 | ±0.2955 | **-2.916** | **0.0035** | ** |
| Education: high school or below (vs college) | +0.3330 | 0.2505 | ±0.5010 | +1.329 | 0.1837 |  |
| Site: UCSD (vs UAB) | +0.1872 | 0.1654 | ±0.3309 | +1.132 | 0.2578 |  |
| Site: UW (vs UAB) | -0.3468 | 0.1974 | ±0.3948 | -1.757 | 0.0790 | . |
| **Season: spring (vs autumn)** | **-0.4314** | 0.1943 | ±0.3886 | **-2.220** | **0.0264** | * |
| Season: summer (vs autumn) | +0.0338 | 0.2161 | ±0.4322 | +0.156 | 0.8757 |  |
| Season: winter (vs autumn) | -0.0115 | 0.2392 | ±0.4785 | -0.048 | 0.9618 |  |
| **Age (years)** | **-0.0183** | 0.0070 | ±0.0140 | **-2.610** | **0.0091** | ** |
| BMI (kg/m2) | +0.0048 | 0.0120 | ±0.0241 | +0.400 | 0.6893 |  |
| Hypertension | +0.1669 | 0.1548 | ±0.3097 | +1.078 | 0.2810 |  |
| High cholesterol | +0.0452 | 0.1563 | ±0.3126 | +0.289 | 0.7726 |  |
| Kidney disease | -0.0438 | 0.2258 | ±0.4515 | -0.194 | 0.8463 |  |
| Circulatory disease | -0.1277 | 0.1755 | ±0.3511 | -0.727 | 0.4670 |  |
| Avg. daily mean/SD | -0.0382 | 0.0436 | ±0.0872 | -0.876 | 0.3813 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **228**, R² = **0.1786**, Adj R² = **0.1246**, F-statistic = **3.31** (p = **8.38e-05**), Residual SE = **1.039** on **213** df, AIC = **678.8**, BIC = **730.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4075** | 0.7407 | ±1.4815 | **+4.600** | **4.22e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4653** | 0.1509 | ±0.3018 | **-3.084** | **0.0020** | ** |
| Education: high school or below (vs college) | +0.4019 | 0.2482 | ±0.4964 | +1.619 | 0.1053 |  |
| Site: UCSD (vs UAB) | +0.1979 | 0.1641 | ±0.3281 | +1.206 | 0.2277 |  |
| Site: UW (vs UAB) | -0.3652 | 0.1969 | ±0.3939 | -1.855 | 0.0636 | . |
| **Season: spring (vs autumn)** | **-0.4199** | 0.1941 | ±0.3882 | **-2.164** | **0.0305** | * |
| Season: summer (vs autumn) | +0.0279 | 0.2158 | ±0.4315 | +0.129 | 0.8971 |  |
| Season: winter (vs autumn) | -0.0173 | 0.2389 | ±0.4778 | -0.072 | 0.9423 |  |
| **Age (years)** | **-0.0162** | 0.0069 | ±0.0137 | **-2.357** | **0.0184** | * |
| BMI (kg/m2) | +0.0050 | 0.0119 | ±0.0239 | +0.418 | 0.6761 |  |
| Hypertension | +0.1539 | 0.1561 | ±0.3123 | +0.986 | 0.3243 |  |
| High cholesterol | +0.0403 | 0.1555 | ±0.3110 | +0.259 | 0.7953 |  |
| Kidney disease | -0.0166 | 0.2286 | ±0.4571 | -0.073 | 0.9421 |  |
| Circulatory disease | -0.1284 | 0.1737 | ±0.3474 | -0.739 | 0.4599 |  |
| MAG (mg/dL/h) | -0.0061 | 0.0056 | ±0.0112 | -1.086 | 0.2776 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **228**, R² = **0.1753**, Adj R² = **0.1211**, F-statistic = **3.23** (p = **1.15e-04**), Residual SE = **1.041** on **213** df, AIC = **679.7**, BIC = **731.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1683** | 0.7657 | ±1.5315 | **+4.138** | **3.51e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4521** | 0.1501 | ±0.3001 | **-3.013** | **0.0026** | ** |
| Education: high school or below (vs college) | +0.3668 | 0.2526 | ±0.5052 | +1.452 | 0.1465 |  |
| Site: UCSD (vs UAB) | +0.1899 | 0.1628 | ±0.3257 | +1.166 | 0.2435 |  |
| Site: UW (vs UAB) | -0.3507 | 0.1970 | ±0.3941 | -1.780 | 0.0751 | . |
| **Season: spring (vs autumn)** | **-0.4287** | 0.1942 | ±0.3884 | **-2.208** | **0.0273** | * |
| Season: summer (vs autumn) | +0.0342 | 0.2159 | ±0.4318 | +0.158 | 0.8742 |  |
| Season: winter (vs autumn) | -0.0138 | 0.2392 | ±0.4785 | -0.058 | 0.9540 |  |
| **Age (years)** | **-0.0166** | 0.0068 | ±0.0137 | **-2.423** | **0.0154** | * |
| BMI (kg/m2) | +0.0044 | 0.0123 | ±0.0245 | +0.360 | 0.7192 |  |
| Hypertension | +0.1587 | 0.1556 | ±0.3113 | +1.020 | 0.3078 |  |
| High cholesterol | +0.0413 | 0.1559 | ±0.3118 | +0.265 | 0.7911 |  |
| Kidney disease | -0.0188 | 0.2240 | ±0.4480 | -0.084 | 0.9330 |  |
| Circulatory disease | -0.1277 | 0.1752 | ±0.3504 | -0.729 | 0.4661 |  |
| Avg. daily range (mg/dL) | +0.0000 | 0.0015 | ±0.0029 | +0.019 | 0.9850 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **228**, R² = **0.1795**, Adj R² = **0.1256**, F-statistic = **3.33** (p = **7.66e-05**), Residual SE = **1.038** on **213** df, AIC = **678.6**, BIC = **730.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1029** | 0.7197 | ±1.4393 | **+4.312** | **1.62e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4330** | 0.1488 | ±0.2976 | **-2.910** | **0.0036** | ** |
| Education: high school or below (vs college) | +0.3610 | 0.2415 | ±0.4829 | +1.495 | 0.1349 |  |
| Site: UCSD (vs UAB) | +0.1925 | 0.1644 | ±0.3288 | +1.171 | 0.2418 |  |
| Site: UW (vs UAB) | -0.3397 | 0.1958 | ±0.3917 | -1.735 | 0.0828 | . |
| **Season: spring (vs autumn)** | **-0.4234** | 0.1939 | ±0.3877 | **-2.184** | **0.0289** | * |
| Season: summer (vs autumn) | +0.0366 | 0.2149 | ±0.4299 | +0.170 | 0.8647 |  |
| Season: winter (vs autumn) | -0.0341 | 0.2403 | ±0.4806 | -0.142 | 0.8870 |  |
| **Age (years)** | **-0.0171** | 0.0069 | ±0.0137 | **-2.490** | **0.0128** | * |
| BMI (kg/m2) | +0.0049 | 0.0120 | ±0.0239 | +0.407 | 0.6840 |  |
| Hypertension | +0.1424 | 0.1599 | ±0.3198 | +0.890 | 0.3733 |  |
| High cholesterol | +0.0463 | 0.1563 | ±0.3126 | +0.296 | 0.7671 |  |
| Kidney disease | -0.0527 | 0.2248 | ±0.4495 | -0.234 | 0.8148 |  |
| Circulatory disease | -0.1388 | 0.1779 | ±0.3558 | -0.780 | 0.4351 |  |
| SD of daily means (mg/dL) | +0.0078 | 0.0082 | ±0.0164 | +0.952 | 0.3412 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **228**, R² = **0.1802**, Adj R² = **0.1264**, F-statistic = **3.35** (p = **7.13e-05**), Residual SE = **1.038** on **213** df, AIC = **678.4**, BIC = **729.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.5647** | 0.7946 | ±1.5892 | **+4.486** | **7.26e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4301** | 0.1482 | ±0.2963 | **-2.903** | **0.0037** | ** |
| Education: high school or below (vs college) | +0.3498 | 0.2418 | ±0.4835 | +1.447 | 0.1480 |  |
| Site: UCSD (vs UAB) | +0.1946 | 0.1637 | ±0.3275 | +1.188 | 0.2347 |  |
| Site: UW (vs UAB) | -0.3409 | 0.1962 | ±0.3925 | -1.737 | 0.0824 | . |
| **Season: spring (vs autumn)** | **-0.4461** | 0.1963 | ±0.3925 | **-2.273** | **0.0230** | * |
| Season: summer (vs autumn) | +0.0398 | 0.2149 | ±0.4298 | +0.185 | 0.8531 |  |
| Season: winter (vs autumn) | -0.0394 | 0.2391 | ±0.4781 | -0.165 | 0.8691 |  |
| **Age (years)** | **-0.0170** | 0.0068 | ±0.0136 | **-2.496** | **0.0125** | * |
| BMI (kg/m2) | +0.0049 | 0.0119 | ±0.0238 | +0.416 | 0.6776 |  |
| Hypertension | +0.1577 | 0.1566 | ±0.3132 | +1.007 | 0.3139 |  |
| High cholesterol | +0.0419 | 0.1558 | ±0.3116 | +0.269 | 0.7880 |  |
| Kidney disease | -0.0546 | 0.2230 | ±0.4461 | -0.245 | 0.8066 |  |
| Circulatory disease | -0.1386 | 0.1764 | ±0.3527 | -0.786 | 0.4320 |  |
| Time in range 70-180, pooled (%) | -0.0045 | 0.0037 | ±0.0074 | -1.210 | 0.2262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **228**, R² = **0.1809**, Adj R² = **0.1271**, F-statistic = **3.36** (p = **6.68e-05**), Residual SE = **1.037** on **213** df, AIC = **678.2**, BIC = **729.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.5909** | 0.7980 | ±1.5959 | **+4.500** | **6.79e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4287** | 0.1478 | ±0.2956 | **-2.900** | **0.0037** | ** |
| Education: high school or below (vs college) | +0.3466 | 0.2417 | ±0.4834 | +1.434 | 0.1516 |  |
| Site: UCSD (vs UAB) | +0.1958 | 0.1636 | ±0.3272 | +1.196 | 0.2315 |  |
| Site: UW (vs UAB) | -0.3394 | 0.1962 | ±0.3923 | -1.730 | 0.0836 | . |
| **Season: spring (vs autumn)** | **-0.4487** | 0.1964 | ±0.3929 | **-2.284** | **0.0224** | * |
| Season: summer (vs autumn) | +0.0381 | 0.2147 | ±0.4294 | +0.178 | 0.8590 |  |
| Season: winter (vs autumn) | -0.0439 | 0.2391 | ±0.4783 | -0.183 | 0.8545 |  |
| **Age (years)** | **-0.0170** | 0.0068 | ±0.0136 | **-2.503** | **0.0123** | * |
| BMI (kg/m2) | +0.0051 | 0.0119 | ±0.0238 | +0.425 | 0.6708 |  |
| Hypertension | +0.1588 | 0.1565 | ±0.3130 | +1.015 | 0.3101 |  |
| High cholesterol | +0.0417 | 0.1557 | ±0.3114 | +0.268 | 0.7888 |  |
| Kidney disease | -0.0587 | 0.2214 | ±0.4429 | -0.265 | 0.7911 |  |
| Circulatory disease | -0.1394 | 0.1765 | ±0.3529 | -0.790 | 0.4294 |  |
| Avg. daily time in range 70-180 (%) | -0.0048 | 0.0037 | ±0.0074 | -1.290 | 0.1969 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.2000**, Adj R² = **0.1474**, F-statistic = **3.80** (p = **9.58e-06**), Residual SE = **1.025** on **213** df, AIC = **672.8**, BIC = **724.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0786** | 0.7186 | ±1.4371 | **+4.284** | **1.83e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4303** | 0.1477 | ±0.2954 | **-2.914** | **0.0036** | ** |
| Education: high school or below (vs college) | +0.4018 | 0.2467 | ±0.4933 | +1.629 | 0.1033 |  |
| Site: UCSD (vs UAB) | +0.2516 | 0.1631 | ±0.3263 | +1.542 | 0.1231 |  |
| Site: UW (vs UAB) | -0.2768 | 0.1995 | ±0.3990 | -1.387 | 0.1653 |  |
| **Season: spring (vs autumn)** | **-0.3957** | 0.1971 | ±0.3941 | **-2.008** | **0.0447** | * |
| Season: summer (vs autumn) | +0.0421 | 0.2097 | ±0.4194 | +0.201 | 0.8410 |  |
| Season: winter (vs autumn) | -0.0023 | 0.2368 | ±0.4735 | -0.010 | 0.9922 |  |
| **Age (years)** | **-0.0170** | 0.0068 | ±0.0135 | **-2.513** | **0.0120** | * |
| BMI (kg/m2) | +0.0039 | 0.0115 | ±0.0230 | +0.340 | 0.7340 |  |
| Hypertension | +0.1502 | 0.1600 | ±0.3200 | +0.939 | 0.3479 |  |
| High cholesterol | +0.0312 | 0.1537 | ±0.3074 | +0.203 | 0.8390 |  |
| Kidney disease | -0.0043 | 0.2258 | ±0.4516 | -0.019 | 0.9847 |  |
| Circulatory disease | -0.1636 | 0.1713 | ±0.3426 | -0.955 | 0.3396 |  |
| **Time < 54 (%)** | **+0.2428** | 0.1102 | ±0.2205 | **+2.202** | **0.0276** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **228**, R² = **0.2038**, Adj R² = **0.1514**, F-statistic = **3.89** (p = **6.42e-06**), Residual SE = **1.023** on **213** df, AIC = **671.7**, BIC = **723.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1381** | 0.7051 | ±1.4101 | **+4.451** | **8.55e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4182** | 0.1448 | ±0.2895 | **-2.889** | **0.0039** | ** |
| Education: high school or below (vs college) | +0.4019 | 0.2451 | ±0.4902 | +1.639 | 0.1011 |  |
| Site: UCSD (vs UAB) | +0.2448 | 0.1611 | ±0.3222 | +1.520 | 0.1286 |  |
| Site: UW (vs UAB) | -0.2920 | 0.1958 | ±0.3917 | -1.491 | 0.1360 |  |
| Season: spring (vs autumn) | -0.3828 | 0.1964 | ±0.3928 | -1.949 | 0.0513 | . |
| Season: summer (vs autumn) | +0.0411 | 0.2133 | ±0.4265 | +0.193 | 0.8471 |  |
| Season: winter (vs autumn) | -0.0089 | 0.2401 | ±0.4802 | -0.037 | 0.9705 |  |
| **Age (years)** | **-0.0179** | 0.0068 | ±0.0136 | **-2.634** | **0.0084** | ** |
| BMI (kg/m2) | +0.0042 | 0.0116 | ±0.0232 | +0.366 | 0.7143 |  |
| Hypertension | +0.1572 | 0.1585 | ±0.3169 | +0.992 | 0.3213 |  |
| High cholesterol | +0.0465 | 0.1541 | ±0.3083 | +0.302 | 0.7629 |  |
| Kidney disease | -0.0208 | 0.2241 | ±0.4482 | -0.093 | 0.9259 |  |
| Circulatory disease | -0.1616 | 0.1746 | ±0.3492 | -0.925 | 0.3548 |  |
| Avg. daily time < 54 (%) | +0.2365 | 0.1576 | ±0.3153 | +1.500 | 0.1336 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.2098**, Adj R² = **0.1579**, F-statistic = **4.04** (p = **3.36e-06**), Residual SE = **1.019** on **213** df, AIC = **670.0**, BIC = **721.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1365** | 0.7103 | ±1.4206 | **+4.416** | **1.01e-05** | *** |
| **Education: graduate level (vs college)** | **-0.3824** | 0.1449 | ±0.2899 | **-2.639** | **0.0083** | ** |
| Education: high school or below (vs college) | +0.3471 | 0.2498 | ±0.4996 | +1.390 | 0.1646 |  |
| Site: UCSD (vs UAB) | +0.2233 | 0.1632 | ±0.3263 | +1.369 | 0.1710 |  |
| Site: UW (vs UAB) | -0.3269 | 0.1925 | ±0.3849 | -1.699 | 0.0894 | . |
| Season: spring (vs autumn) | -0.3706 | 0.1957 | ±0.3914 | -1.894 | 0.0583 | . |
| Season: summer (vs autumn) | +0.0556 | 0.2069 | ±0.4139 | +0.269 | 0.7883 |  |
| Season: winter (vs autumn) | +0.0096 | 0.2344 | ±0.4689 | +0.041 | 0.9674 |  |
| **Age (years)** | **-0.0194** | 0.0067 | ±0.0133 | **-2.907** | **0.0037** | ** |
| BMI (kg/m2) | +0.0048 | 0.0117 | ±0.0233 | +0.408 | 0.6835 |  |
| Hypertension | +0.1789 | 0.1608 | ±0.3216 | +1.112 | 0.2659 |  |
| High cholesterol | +0.0112 | 0.1518 | ±0.3037 | +0.074 | 0.9411 |  |
| Kidney disease | -0.0353 | 0.2281 | ±0.4563 | -0.155 | 0.8769 |  |
| Circulatory disease | -0.1316 | 0.1704 | ±0.3408 | -0.772 | 0.4399 |  |
| **Time 54-69, pooled (%)** | **+0.0849** | 0.0380 | ±0.0761 | **+2.233** | **0.0255** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **228**, R² = **0.2122**, Adj R² = **0.1604**, F-statistic = **4.10** (p = **2.60e-06**), Residual SE = **1.017** on **213** df, AIC = **669.3**, BIC = **720.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1809** | 0.7055 | ±1.4110 | **+4.509** | **6.52e-06** | *** |
| **Education: graduate level (vs college)** | **-0.3797** | 0.1439 | ±0.2877 | **-2.640** | **0.0083** | ** |
| Education: high school or below (vs college) | +0.3391 | 0.2501 | ±0.5001 | +1.356 | 0.1750 |  |
| Site: UCSD (vs UAB) | +0.2231 | 0.1630 | ±0.3261 | +1.369 | 0.1711 |  |
| Site: UW (vs UAB) | -0.3244 | 0.1917 | ±0.3834 | -1.692 | 0.0906 | . |
| Season: spring (vs autumn) | -0.3725 | 0.1954 | ±0.3908 | -1.906 | 0.0566 | . |
| Season: summer (vs autumn) | +0.0488 | 0.2073 | ±0.4146 | +0.235 | 0.8140 |  |
| Season: winter (vs autumn) | +0.0054 | 0.2342 | ±0.4684 | +0.023 | 0.9817 |  |
| **Age (years)** | **-0.0199** | 0.0067 | ±0.0133 | **-2.991** | **0.0028** | ** |
| BMI (kg/m2) | +0.0046 | 0.0116 | ±0.0233 | +0.394 | 0.6933 |  |
| Hypertension | +0.1809 | 0.1607 | ±0.3214 | +1.126 | 0.2602 |  |
| High cholesterol | +0.0148 | 0.1519 | ±0.3038 | +0.097 | 0.9226 |  |
| Kidney disease | -0.0325 | 0.2258 | ±0.4515 | -0.144 | 0.8856 |  |
| Circulatory disease | -0.1258 | 0.1703 | ±0.3407 | -0.738 | 0.4603 |  |
| **Avg. daily time 54-69 (%)** | **+0.0838** | 0.0369 | ±0.0739 | **+2.269** | **0.0233** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **228**, R² = **0.2125**, Adj R² = **0.1607**, F-statistic = **4.10** (p = **2.53e-06**), Residual SE = **1.017** on **213** df, AIC = **669.2**, BIC = **720.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1134** | 0.7096 | ±1.4192 | **+4.387** | **1.15e-05** | *** |
| **Education: graduate level (vs college)** | **-0.3855** | 0.1445 | ±0.2891 | **-2.667** | **0.0077** | ** |
| Education: high school or below (vs college) | +0.3603 | 0.2503 | ±0.5005 | +1.440 | 0.1500 |  |
| Site: UCSD (vs UAB) | +0.2373 | 0.1629 | ±0.3258 | +1.456 | 0.1453 |  |
| Site: UW (vs UAB) | -0.3079 | 0.1937 | ±0.3874 | -1.590 | 0.1119 |  |
| Season: spring (vs autumn) | -0.3688 | 0.1963 | ±0.3925 | -1.879 | 0.0603 | . |
| Season: summer (vs autumn) | +0.0550 | 0.2060 | ±0.4120 | +0.267 | 0.7895 |  |
| Season: winter (vs autumn) | +0.0098 | 0.2342 | ±0.4683 | +0.042 | 0.9667 |  |
| **Age (years)** | **-0.0191** | 0.0066 | ±0.0133 | **-2.875** | **0.0040** | ** |
| BMI (kg/m2) | +0.0046 | 0.0116 | ±0.0231 | +0.394 | 0.6937 |  |
| Hypertension | +0.1735 | 0.1608 | ±0.3216 | +1.079 | 0.2805 |  |
| High cholesterol | +0.0124 | 0.1518 | ±0.3036 | +0.082 | 0.9350 |  |
| Kidney disease | -0.0288 | 0.2265 | ±0.4530 | -0.127 | 0.8988 |  |
| Circulatory disease | -0.1419 | 0.1694 | ±0.3387 | -0.838 | 0.4023 |  |
| **Time < 70 (%)** | **+0.0731** | 0.0297 | ±0.0595 | **+2.459** | **0.0139** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **228**, R² = **0.2155**, Adj R² = **0.1640**, F-statistic = **4.18** (p = **1.81e-06**), Residual SE = **1.015** on **213** df, AIC = **668.3**, BIC = **719.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1694** | 0.7022 | ±1.4044 | **+4.514** | **6.37e-06** | *** |
| **Education: graduate level (vs college)** | **-0.3799** | 0.1427 | ±0.2855 | **-2.661** | **0.0078** | ** |
| Education: high school or below (vs college) | +0.3537 | 0.2503 | ±0.5006 | +1.413 | 0.1577 |  |
| Site: UCSD (vs UAB) | +0.2350 | 0.1621 | ±0.3243 | +1.449 | 0.1473 |  |
| Site: UW (vs UAB) | -0.3104 | 0.1920 | ±0.3840 | -1.617 | 0.1060 |  |
| Season: spring (vs autumn) | -0.3667 | 0.1957 | ±0.3913 | -1.874 | 0.0609 | . |
| Season: summer (vs autumn) | +0.0488 | 0.2068 | ±0.4136 | +0.236 | 0.8135 |  |
| Season: winter (vs autumn) | +0.0041 | 0.2343 | ±0.4686 | +0.017 | 0.9861 |  |
| **Age (years)** | **-0.0199** | 0.0067 | ±0.0133 | **-2.977** | **0.0029** | ** |
| BMI (kg/m2) | +0.0045 | 0.0116 | ±0.0231 | +0.391 | 0.6961 |  |
| Hypertension | +0.1773 | 0.1604 | ±0.3207 | +1.105 | 0.2690 |  |
| High cholesterol | +0.0202 | 0.1521 | ±0.3042 | +0.133 | 0.8944 |  |
| Kidney disease | -0.0313 | 0.2241 | ±0.4482 | -0.139 | 0.8891 |  |
| Circulatory disease | -0.1363 | 0.1695 | ±0.3390 | -0.804 | 0.4212 |  |
| **Avg. daily time < 70 (%)** | **+0.0717** | 0.0298 | ±0.0597 | **+2.403** | **0.0162** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.1757**, Adj R² = **0.1216**, F-statistic = **3.24** (p = **1.11e-04**), Residual SE = **1.040** on **213** df, AIC = **679.6**, BIC = **731.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4073** | 0.8003 | ±1.6006 | **+4.257** | **2.07e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4479** | 0.1497 | ±0.2994 | **-2.993** | **0.0028** | ** |
| Education: high school or below (vs college) | +0.3614 | 0.2443 | ±0.4885 | +1.480 | 0.1390 |  |
| Site: UCSD (vs UAB) | +0.1911 | 0.1630 | ±0.3261 | +1.172 | 0.2410 |  |
| Site: UW (vs UAB) | -0.3456 | 0.1973 | ±0.3946 | -1.752 | 0.0799 | . |
| **Season: spring (vs autumn)** | **-0.4319** | 0.1949 | ±0.3898 | **-2.216** | **0.0267** | * |
| Season: summer (vs autumn) | +0.0403 | 0.2178 | ±0.4355 | +0.185 | 0.8533 |  |
| Season: winter (vs autumn) | -0.0160 | 0.2390 | ±0.4780 | -0.067 | 0.9468 |  |
| **Age (years)** | **-0.0165** | 0.0069 | ±0.0137 | **-2.404** | **0.0162** | * |
| BMI (kg/m2) | +0.0046 | 0.0121 | ±0.0241 | +0.378 | 0.7052 |  |
| Hypertension | +0.1561 | 0.1579 | ±0.3158 | +0.989 | 0.3228 |  |
| High cholesterol | +0.0449 | 0.1557 | ±0.3114 | +0.288 | 0.7730 |  |
| Kidney disease | -0.0225 | 0.2279 | ±0.4558 | -0.099 | 0.9215 |  |
| Circulatory disease | -0.1311 | 0.1772 | ±0.3545 | -0.740 | 0.4594 |  |
| Time 54-250, pooled (%) | -0.0026 | 0.0058 | ±0.0116 | -0.442 | 0.6583 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.1765**, Adj R² = **0.1224**, F-statistic = **3.26** (p = **1.03e-04**), Residual SE = **1.040** on **213** df, AIC = **679.4**, BIC = **730.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6285** | 0.8764 | ±1.7529 | **+4.140** | **3.47e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4440** | 0.1495 | ±0.2990 | **-2.970** | **0.0030** | ** |
| Education: high school or below (vs college) | +0.3550 | 0.2452 | ±0.4903 | +1.448 | 0.1475 |  |
| Site: UCSD (vs UAB) | +0.1913 | 0.1632 | ±0.3265 | +1.172 | 0.2411 |  |
| Site: UW (vs UAB) | -0.3430 | 0.1971 | ±0.3943 | -1.740 | 0.0819 | . |
| **Season: spring (vs autumn)** | **-0.4370** | 0.1953 | ±0.3906 | **-2.237** | **0.0253** | * |
| Season: summer (vs autumn) | +0.0430 | 0.2172 | ±0.4344 | +0.198 | 0.8431 |  |
| Season: winter (vs autumn) | -0.0206 | 0.2388 | ±0.4777 | -0.086 | 0.9312 |  |
| **Age (years)** | **-0.0165** | 0.0068 | ±0.0137 | **-2.411** | **0.0159** | * |
| BMI (kg/m2) | +0.0048 | 0.0121 | ±0.0242 | +0.395 | 0.6929 |  |
| Hypertension | +0.1541 | 0.1581 | ±0.3162 | +0.975 | 0.3297 |  |
| High cholesterol | +0.0477 | 0.1557 | ±0.3115 | +0.306 | 0.7596 |  |
| Kidney disease | -0.0280 | 0.2264 | ±0.4528 | -0.123 | 0.9017 |  |
| Circulatory disease | -0.1353 | 0.1783 | ±0.3567 | -0.758 | 0.4482 |  |
| Avg. daily time 54-250 (%) | -0.0049 | 0.0069 | ±0.0138 | -0.709 | 0.4781 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.1778**, Adj R² = **0.1238**, F-statistic = **3.29** (p = **9.03e-05**), Residual SE = **1.039** on **213** df, AIC = **679.0**, BIC = **730.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1528** | 0.7089 | ±1.4178 | **+4.447** | **8.69e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4411** | 0.1498 | ±0.2995 | **-2.945** | **0.0032** | ** |
| Education: high school or below (vs college) | +0.3612 | 0.2409 | ±0.4818 | +1.499 | 0.1338 |  |
| Site: UCSD (vs UAB) | +0.1906 | 0.1644 | ±0.3288 | +1.159 | 0.2463 |  |
| Site: UW (vs UAB) | -0.3514 | 0.1983 | ±0.3966 | -1.772 | 0.0764 | . |
| **Season: spring (vs autumn)** | **-0.4441** | 0.1971 | ±0.3942 | **-2.253** | **0.0243** | * |
| Season: summer (vs autumn) | +0.0277 | 0.2167 | ±0.4333 | +0.128 | 0.8983 |  |
| Season: winter (vs autumn) | -0.0380 | 0.2426 | ±0.4852 | -0.157 | 0.8754 |  |
| **Age (years)** | **-0.0170** | 0.0070 | ±0.0139 | **-2.444** | **0.0145** | * |
| BMI (kg/m2) | +0.0046 | 0.0119 | ±0.0238 | +0.390 | 0.6963 |  |
| Hypertension | +0.1613 | 0.1556 | ±0.3112 | +1.036 | 0.3000 |  |
| High cholesterol | +0.0367 | 0.1553 | ±0.3106 | +0.236 | 0.8132 |  |
| Kidney disease | -0.0476 | 0.2242 | ±0.4483 | -0.212 | 0.8319 |  |
| Circulatory disease | -0.1326 | 0.1759 | ±0.3517 | -0.754 | 0.4509 |  |
| Time 181-250, pooled (%) | +0.0047 | 0.0065 | ±0.0130 | +0.732 | 0.4641 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **228**, R² = **0.1773**, Adj R² = **0.1232**, F-statistic = **3.28** (p = **9.55e-05**), Residual SE = **1.039** on **213** df, AIC = **679.2**, BIC = **730.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1481** | 0.7089 | ±1.4177 | **+4.441** | **8.95e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4429** | 0.1496 | ±0.2992 | **-2.961** | **0.0031** | ** |
| Education: high school or below (vs college) | +0.3615 | 0.2412 | ±0.4823 | +1.499 | 0.1339 |  |
| Site: UCSD (vs UAB) | +0.1920 | 0.1638 | ±0.3276 | +1.172 | 0.2411 |  |
| Site: UW (vs UAB) | -0.3490 | 0.1974 | ±0.3949 | -1.768 | 0.0771 | . |
| **Season: spring (vs autumn)** | **-0.4412** | 0.1970 | ±0.3939 | **-2.240** | **0.0251** | * |
| Season: summer (vs autumn) | +0.0296 | 0.2166 | ±0.4332 | +0.137 | 0.8913 |  |
| Season: winter (vs autumn) | -0.0344 | 0.2425 | ±0.4850 | -0.142 | 0.8871 |  |
| **Age (years)** | **-0.0168** | 0.0069 | ±0.0138 | **-2.436** | **0.0149** | * |
| BMI (kg/m2) | +0.0046 | 0.0119 | ±0.0238 | +0.389 | 0.6975 |  |
| Hypertension | +0.1615 | 0.1557 | ±0.3114 | +1.037 | 0.2996 |  |
| High cholesterol | +0.0375 | 0.1554 | ±0.3107 | +0.242 | 0.8091 |  |
| Kidney disease | -0.0435 | 0.2238 | ±0.4476 | -0.194 | 0.8459 |  |
| Circulatory disease | -0.1314 | 0.1757 | ±0.3514 | -0.748 | 0.4544 |  |
| Avg. daily time 181-250 (%) | +0.0040 | 0.0061 | ±0.0122 | +0.660 | 0.5094 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **228**, R² = **0.1767**, Adj R² = **0.1226**, F-statistic = **3.27** (p = **1.01e-04**), Residual SE = **1.040** on **213** df, AIC = **679.3**, BIC = **730.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1451** | 0.7138 | ±1.4276 | **+4.406** | **1.05e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4430** | 0.1497 | ±0.2994 | **-2.959** | **0.0031** | ** |
| Education: high school or below (vs college) | +0.3586 | 0.2424 | ±0.4847 | +1.479 | 0.1390 |  |
| Site: UCSD (vs UAB) | +0.1908 | 0.1638 | ±0.3276 | +1.165 | 0.2441 |  |
| Site: UW (vs UAB) | -0.3471 | 0.1966 | ±0.3933 | -1.765 | 0.0776 | . |
| **Season: spring (vs autumn)** | **-0.4395** | 0.1965 | ±0.3930 | **-2.237** | **0.0253** | * |
| Season: summer (vs autumn) | +0.0364 | 0.2157 | ±0.4314 | +0.169 | 0.8659 |  |
| Season: winter (vs autumn) | -0.0277 | 0.2407 | ±0.4815 | -0.115 | 0.9083 |  |
| **Age (years)** | **-0.0167** | 0.0068 | ±0.0137 | **-2.438** | **0.0148** | * |
| BMI (kg/m2) | +0.0047 | 0.0120 | ±0.0239 | +0.391 | 0.6960 |  |
| Hypertension | +0.1577 | 0.1570 | ±0.3139 | +1.005 | 0.3150 |  |
| High cholesterol | +0.0425 | 0.1561 | ±0.3121 | +0.272 | 0.7856 |  |
| Kidney disease | -0.0366 | 0.2244 | ±0.4487 | -0.163 | 0.8704 |  |
| Circulatory disease | -0.1329 | 0.1768 | ±0.3537 | -0.751 | 0.4525 |  |
| Time > 180 (%) | +0.0023 | 0.0037 | ±0.0073 | +0.631 | 0.5278 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **228**, R² = **0.1768**, Adj R² = **0.1227**, F-statistic = **3.27** (p = **1.00e-04**), Residual SE = **1.040** on **213** df, AIC = **679.3**, BIC = **730.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1425** | 0.7130 | ±1.4259 | **+4.408** | **1.04e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4429** | 0.1496 | ±0.2992 | **-2.960** | **0.0031** | ** |
| Education: high school or below (vs college) | +0.3574 | 0.2425 | ±0.4850 | +1.474 | 0.1405 |  |
| Site: UCSD (vs UAB) | +0.1913 | 0.1637 | ±0.3273 | +1.169 | 0.2424 |  |
| Site: UW (vs UAB) | -0.3464 | 0.1966 | ±0.3931 | -1.762 | 0.0780 | . |
| **Season: spring (vs autumn)** | **-0.4408** | 0.1969 | ±0.3938 | **-2.239** | **0.0252** | * |
| Season: summer (vs autumn) | +0.0357 | 0.2157 | ±0.4313 | +0.166 | 0.8684 |  |
| Season: winter (vs autumn) | -0.0296 | 0.2412 | ±0.4825 | -0.123 | 0.9023 |  |
| **Age (years)** | **-0.0167** | 0.0068 | ±0.0137 | **-2.437** | **0.0148** | * |
| BMI (kg/m2) | +0.0047 | 0.0120 | ±0.0239 | +0.395 | 0.6928 |  |
| Hypertension | +0.1581 | 0.1568 | ±0.3137 | +1.008 | 0.3133 |  |
| High cholesterol | +0.0422 | 0.1560 | ±0.3119 | +0.270 | 0.7869 |  |
| Kidney disease | -0.0382 | 0.2233 | ±0.4466 | -0.171 | 0.8642 |  |
| Circulatory disease | -0.1333 | 0.1770 | ±0.3540 | -0.753 | 0.4512 |  |
| Avg. daily time > 180 (%) | +0.0024 | 0.0037 | ±0.0074 | +0.655 | 0.5122 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **228**, R² = **0.1806**, Adj R² = **0.1268**, F-statistic = **3.35** (p = **6.85e-05**), Residual SE = **1.037** on **213** df, AIC = **678.2**, BIC = **729.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1209** | 0.7049 | ±1.4098 | **+4.428** | **9.53e-06** | *** |
| **Education: graduate level (vs college)** | **-0.4360** | 0.1491 | ±0.2982 | **-2.924** | **0.0035** | ** |
| Education: high school or below (vs college) | +0.3575 | 0.2400 | ±0.4800 | +1.490 | 0.1363 |  |
| Site: UCSD (vs UAB) | +0.1933 | 0.1638 | ±0.3276 | +1.180 | 0.2380 |  |
| Site: UW (vs UAB) | -0.3435 | 0.1969 | ±0.3938 | -1.745 | 0.0810 | . |
| **Season: spring (vs autumn)** | **-0.4463** | 0.1965 | ±0.3930 | **-2.271** | **0.0231** | * |
| Season: summer (vs autumn) | +0.0486 | 0.2148 | ±0.4297 | +0.226 | 0.8210 |  |
| Season: winter (vs autumn) | -0.0400 | 0.2396 | ±0.4792 | -0.167 | 0.8674 |  |
| **Age (years)** | **-0.0164** | 0.0068 | ±0.0135 | **-2.427** | **0.0152** | * |
| BMI (kg/m2) | +0.0048 | 0.0119 | ±0.0237 | +0.403 | 0.6871 |  |
| Hypertension | +0.1485 | 0.1576 | ±0.3152 | +0.942 | 0.3461 |  |
| High cholesterol | +0.0380 | 0.1555 | ±0.3110 | +0.244 | 0.8069 |  |
| Kidney disease | -0.0326 | 0.2236 | ±0.4471 | -0.146 | 0.8842 |  |
| Circulatory disease | -0.1429 | 0.1785 | ±0.3571 | -0.800 | 0.4235 |  |
| Nocturnal time > 180 (%) | +0.0046 | 0.0041 | ±0.0082 | +1.125 | 0.2607 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.1760**, Adj R² = **0.1218**, F-statistic = **3.25** (p = **1.08e-04**), Residual SE = **1.040** on **213** df, AIC = **679.5**, BIC = **731.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1864** | 0.7297 | ±1.4595 | **+4.367** | **1.26e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4597** | 0.1508 | ±0.3016 | **-3.049** | **0.0023** | ** |
| Education: high school or below (vs college) | +0.3737 | 0.2446 | ±0.4892 | +1.528 | 0.1265 |  |
| Site: UCSD (vs UAB) | +0.1892 | 0.1633 | ±0.3266 | +1.159 | 0.2466 |  |
| Site: UW (vs UAB) | -0.3459 | 0.1982 | ±0.3964 | -1.745 | 0.0809 | . |
| **Season: spring (vs autumn)** | **-0.4231** | 0.1936 | ±0.3872 | **-2.185** | **0.0289** | * |
| Season: summer (vs autumn) | +0.0384 | 0.2156 | ±0.4311 | +0.178 | 0.8586 |  |
| Season: winter (vs autumn) | -0.0126 | 0.2399 | ±0.4798 | -0.052 | 0.9583 |  |
| **Age (years)** | **-0.0161** | 0.0070 | ±0.0140 | **-2.296** | **0.0217** | * |
| BMI (kg/m2) | +0.0039 | 0.0123 | ±0.0247 | +0.320 | 0.7491 |  |
| Hypertension | +0.1596 | 0.1587 | ±0.3173 | +1.006 | 0.3144 |  |
| High cholesterol | +0.0386 | 0.1563 | ±0.3127 | +0.247 | 0.8052 |  |
| Kidney disease | -0.0022 | 0.2281 | ±0.4562 | -0.010 | 0.9922 |  |
| Circulatory disease | -0.1262 | 0.1752 | ±0.3505 | -0.720 | 0.4713 |  |
| Any reading > 250 during wear (0/1) | -0.0602 | 0.1569 | ±0.3138 | -0.384 | 0.7012 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.1754**, Adj R² = **0.1212**, F-statistic = **3.24** (p = **1.15e-04**), Residual SE = **1.041** on **213** df, AIC = **679.7**, BIC = **731.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1643** | 0.7289 | ±1.4579 | **+4.341** | **1.42e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4509** | 0.1501 | ±0.3001 | **-3.004** | **0.0027** | ** |
| Education: high school or below (vs college) | +0.3651 | 0.2440 | ±0.4881 | +1.496 | 0.1346 |  |
| Site: UCSD (vs UAB) | +0.1901 | 0.1631 | ±0.3263 | +1.165 | 0.2439 |  |
| Site: UW (vs UAB) | -0.3492 | 0.1972 | ±0.3945 | -1.770 | 0.0767 | . |
| **Season: spring (vs autumn)** | **-0.4298** | 0.1946 | ±0.3893 | **-2.208** | **0.0272** | * |
| Season: summer (vs autumn) | +0.0364 | 0.2173 | ±0.4346 | +0.168 | 0.8668 |  |
| Season: winter (vs autumn) | -0.0146 | 0.2391 | ±0.4783 | -0.061 | 0.9514 |  |
| **Age (years)** | **-0.0165** | 0.0069 | ±0.0137 | **-2.410** | **0.0160** | * |
| BMI (kg/m2) | +0.0045 | 0.0121 | ±0.0242 | +0.370 | 0.7117 |  |
| Hypertension | +0.1577 | 0.1578 | ±0.3156 | +0.999 | 0.3176 |  |
| High cholesterol | +0.0426 | 0.1554 | ±0.3109 | +0.274 | 0.7840 |  |
| Kidney disease | -0.0197 | 0.2280 | ±0.4561 | -0.086 | 0.9311 |  |
| Circulatory disease | -0.1288 | 0.1771 | ±0.3542 | -0.727 | 0.4670 |  |
| Time > 250 (%) | +0.0010 | 0.0053 | ±0.0106 | +0.179 | 0.8577 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 228)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.1756**, Adj R² = **0.1215**, F-statistic = **3.24** (p = **1.12e-04**), Residual SE = **1.041** on **213** df, AIC = **679.6**, BIC = **731.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1555** | 0.7269 | ±1.4538 | **+4.341** | **1.42e-05** | *** |
| **Education: graduate level (vs college)** | **-0.4484** | 0.1500 | ±0.3001 | **-2.989** | **0.0028** | ** |
| Education: high school or below (vs college) | +0.3606 | 0.2449 | ±0.4897 | +1.473 | 0.1409 |  |
| Site: UCSD (vs UAB) | +0.1900 | 0.1633 | ±0.3266 | +1.164 | 0.2446 |  |
| Site: UW (vs UAB) | -0.3473 | 0.1971 | ±0.3942 | -1.762 | 0.0780 | . |
| **Season: spring (vs autumn)** | **-0.4334** | 0.1952 | ±0.3905 | **-2.220** | **0.0264** | * |
| Season: summer (vs autumn) | +0.0388 | 0.2169 | ±0.4338 | +0.179 | 0.8581 |  |
| Season: winter (vs autumn) | -0.0174 | 0.2393 | ±0.4786 | -0.073 | 0.9420 |  |
| **Age (years)** | **-0.0165** | 0.0068 | ±0.0137 | **-2.411** | **0.0159** | * |
| BMI (kg/m2) | +0.0046 | 0.0121 | ±0.0242 | +0.380 | 0.7038 |  |
| Hypertension | +0.1563 | 0.1580 | ±0.3161 | +0.989 | 0.3228 |  |
| High cholesterol | +0.0446 | 0.1554 | ±0.3109 | +0.287 | 0.7744 |  |
| Kidney disease | -0.0232 | 0.2268 | ±0.4536 | -0.102 | 0.9184 |  |
| Circulatory disease | -0.1313 | 0.1783 | ±0.3565 | -0.737 | 0.4614 |  |
| Avg. daily time > 250 (%) | +0.0026 | 0.0063 | ±0.0127 | +0.408 | 0.6833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 228; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **228**, R² = **0.3144**, Adj R² = **0.2728**, F-statistic = **7.55** (p = **3.30e-12**), Residual SE = **2.120** on **214** df, AIC = **1003.2**, BIC = **1051.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6380** | 1.1535 | ±2.3069 | **+20.493** | **2.49e-93** | *** |
| Education: graduate level (vs college) | +0.3810 | 0.3248 | ±0.6496 | +1.173 | 0.2408 |  |
| Education: high school or below (vs college) | -0.0532 | 0.4537 | ±0.9073 | -0.117 | 0.9066 |  |
| Site: UCSD (vs UAB) | -0.2180 | 0.3695 | ±0.7389 | -0.590 | 0.5552 |  |
| **Site: UW (vs UAB)** | **-1.5972** | 0.3454 | ±0.6908 | **-4.624** | **3.76e-06** | *** |
| Season: spring (vs autumn) | +0.1233 | 0.3765 | ±0.7531 | +0.327 | 0.7433 |  |
| **Season: summer (vs autumn)** | **+2.5673** | 0.4004 | ±0.8009 | **+6.411** | **1.44e-10** | *** |
| Season: winter (vs autumn) | -0.8393 | 0.4631 | ±0.9262 | -1.812 | 0.0699 | . |
| Age (years) | +0.0093 | 0.0141 | ±0.0281 | +0.660 | 0.5091 |  |
| BMI (kg/m2) | +0.0194 | 0.0201 | ±0.0402 | +0.966 | 0.3343 |  |
| Hypertension | +0.5178 | 0.3586 | ±0.7172 | +1.444 | 0.1488 |  |
| High cholesterol | -0.5689 | 0.3154 | ±0.6309 | -1.804 | 0.0713 | . |
| Kidney disease | -0.3449 | 0.3841 | ±0.7682 | -0.898 | 0.3692 |  |
| Circulatory disease | +0.0920 | 0.3648 | ±0.7297 | +0.252 | 0.8009 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **228**, R² = **0.3180**, Adj R² = **0.2732**, F-statistic = **7.09** (p = **5.71e-12**), Residual SE = **2.119** on **213** df, AIC = **1004.0**, BIC = **1055.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3903** | 1.3777 | ±2.7553 | **+17.704** | **3.90e-70** | *** |
| Education: graduate level (vs college) | +0.3358 | 0.3291 | ±0.6581 | +1.020 | 0.3075 |  |
| Education: high school or below (vs college) | -0.0145 | 0.4555 | ±0.9110 | -0.032 | 0.9746 |  |
| Site: UCSD (vs UAB) | -0.2229 | 0.3757 | ±0.7515 | -0.593 | 0.5530 |  |
| **Site: UW (vs UAB)** | **-1.6120** | 0.3455 | ±0.6909 | **-4.666** | **3.07e-06** | *** |
| Season: spring (vs autumn) | +0.1514 | 0.3742 | ±0.7484 | +0.405 | 0.6858 |  |
| **Season: summer (vs autumn)** | **+2.5540** | 0.3991 | ±0.7982 | **+6.400** | **1.56e-10** | *** |
| Season: winter (vs autumn) | -0.8176 | 0.4676 | ±0.9352 | -1.749 | 0.0803 | . |
| Age (years) | +0.0113 | 0.0142 | ±0.0284 | +0.798 | 0.4247 |  |
| BMI (kg/m2) | +0.0198 | 0.0204 | ±0.0408 | +0.971 | 0.3316 |  |
| Hypertension | +0.5384 | 0.3598 | ±0.7197 | +1.496 | 0.1346 |  |
| High cholesterol | -0.5890 | 0.3166 | ±0.6333 | -1.860 | 0.0629 | . |
| Kidney disease | -0.3312 | 0.3869 | ±0.7738 | -0.856 | 0.3920 |  |
| Circulatory disease | +0.0949 | 0.3672 | ±0.7344 | +0.258 | 0.7961 |  |
| HbA1c (%) | -0.1385 | 0.1310 | ±0.2620 | -1.058 | 0.2902 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **228**, R² = **0.3207**, Adj R² = **0.2760**, F-statistic = **7.18** (p = **3.95e-12**), Residual SE = **2.115** on **213** df, AIC = **1003.1**, BIC = **1054.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.4802** | 1.3818 | ±2.7637 | **+17.716** | **3.18e-70** | *** |
| Education: graduate level (vs college) | +0.3600 | 0.3252 | ±0.6504 | +1.107 | 0.2682 |  |
| Education: high school or below (vs college) | -0.0104 | 0.4511 | ±0.9023 | -0.023 | 0.9816 |  |
| Site: UCSD (vs UAB) | -0.2180 | 0.3776 | ±0.7551 | -0.577 | 0.5636 |  |
| **Site: UW (vs UAB)** | **-1.6105** | 0.3443 | ±0.6886 | **-4.678** | **2.90e-06** | *** |
| Season: spring (vs autumn) | +0.1971 | 0.3770 | ±0.7539 | +0.523 | 0.6010 |  |
| **Season: summer (vs autumn)** | **+2.5709** | 0.3965 | ±0.7931 | **+6.483** | **8.98e-11** | *** |
| Season: winter (vs autumn) | -0.7811 | 0.4725 | ±0.9449 | -1.653 | 0.0983 | . |
| Age (years) | +0.0094 | 0.0141 | ±0.0281 | +0.668 | 0.5038 |  |
| BMI (kg/m2) | +0.0189 | 0.0207 | ±0.0413 | +0.912 | 0.3616 |  |
| Hypertension | +0.5330 | 0.3605 | ±0.7210 | +1.478 | 0.1393 |  |
| High cholesterol | -0.5898 | 0.3178 | ±0.6355 | -1.856 | 0.0634 | . |
| Kidney disease | -0.2854 | 0.3890 | ±0.7779 | -0.734 | 0.4632 |  |
| Circulatory disease | +0.1132 | 0.3682 | ±0.7364 | +0.307 | 0.7585 |  |
| Mean glucose (mg/dL) | -0.0064 | 0.0054 | ±0.0108 | -1.188 | 0.2350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **228**, R² = **0.3207**, Adj R² = **0.2760**, F-statistic = **7.18** (p = **3.95e-12**), Residual SE = **2.115** on **213** df, AIC = **1003.1**, BIC = **1054.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.3687** | 1.8945 | ±3.7890 | **+13.391** | **6.85e-41** | *** |
| Education: graduate level (vs college) | +0.3600 | 0.3252 | ±0.6504 | +1.107 | 0.2682 |  |
| Education: high school or below (vs college) | -0.0104 | 0.4511 | ±0.9023 | -0.023 | 0.9816 |  |
| Site: UCSD (vs UAB) | -0.2180 | 0.3776 | ±0.7551 | -0.577 | 0.5636 |  |
| **Site: UW (vs UAB)** | **-1.6105** | 0.3443 | ±0.6886 | **-4.678** | **2.90e-06** | *** |
| Season: spring (vs autumn) | +0.1971 | 0.3770 | ±0.7539 | +0.523 | 0.6010 |  |
| **Season: summer (vs autumn)** | **+2.5709** | 0.3965 | ±0.7931 | **+6.483** | **8.98e-11** | *** |
| Season: winter (vs autumn) | -0.7811 | 0.4725 | ±0.9449 | -1.653 | 0.0983 | . |
| Age (years) | +0.0094 | 0.0141 | ±0.0281 | +0.668 | 0.5038 |  |
| BMI (kg/m2) | +0.0189 | 0.0207 | ±0.0413 | +0.912 | 0.3616 |  |
| Hypertension | +0.5330 | 0.3605 | ±0.7210 | +1.478 | 0.1393 |  |
| High cholesterol | -0.5898 | 0.3178 | ±0.6355 | -1.856 | 0.0634 | . |
| Kidney disease | -0.2854 | 0.3890 | ±0.7779 | -0.734 | 0.4632 |  |
| Circulatory disease | +0.1132 | 0.3682 | ±0.7364 | +0.307 | 0.7585 |  |
| GMI (%) | -0.2684 | 0.2260 | ±0.4520 | -1.188 | 0.2350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **228**, R² = **0.3179**, Adj R² = **0.2731**, F-statistic = **7.09** (p = **5.78e-12**), Residual SE = **2.119** on **213** df, AIC = **1004.0**, BIC = **1055.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.2622** | 1.3757 | ±2.7515 | **+17.636** | **1.31e-69** | *** |
| Education: graduate level (vs college) | +0.3795 | 0.3257 | ±0.6515 | +1.165 | 0.2440 |  |
| Education: high school or below (vs college) | -0.0238 | 0.4544 | ±0.9088 | -0.052 | 0.9583 |  |
| Site: UCSD (vs UAB) | -0.2163 | 0.3791 | ±0.7582 | -0.571 | 0.5682 |  |
| **Site: UW (vs UAB)** | **-1.6020** | 0.3445 | ±0.6890 | **-4.650** | **3.31e-06** | *** |
| Season: spring (vs autumn) | +0.1808 | 0.3769 | ±0.7539 | +0.480 | 0.6315 |  |
| **Season: summer (vs autumn)** | **+2.5615** | 0.3984 | ±0.7967 | **+6.430** | **1.28e-10** | *** |
| Season: winter (vs autumn) | -0.7957 | 0.4698 | ±0.9395 | -1.694 | 0.0903 | . |
| Age (years) | +0.0085 | 0.0140 | ±0.0280 | +0.609 | 0.5425 |  |
| BMI (kg/m2) | +0.0193 | 0.0207 | ±0.0414 | +0.930 | 0.3522 |  |
| Hypertension | +0.5389 | 0.3576 | ±0.7152 | +1.507 | 0.1318 |  |
| High cholesterol | -0.5728 | 0.3181 | ±0.6362 | -1.801 | 0.0718 | . |
| Kidney disease | -0.3356 | 0.3846 | ±0.7692 | -0.873 | 0.3829 |  |
| Circulatory disease | +0.1087 | 0.3704 | ±0.7407 | +0.293 | 0.7692 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0047 | 0.0060 | ±0.0119 | -0.793 | 0.4276 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **228**, R² = **0.3183**, Adj R² = **0.2735**, F-statistic = **7.10** (p = **5.47e-12**), Residual SE = **2.119** on **213** df, AIC = **1003.9**, BIC = **1055.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9014** | 1.2189 | ±2.4378 | **+19.609** | **1.29e-85** | *** |
| Education: graduate level (vs college) | +0.3368 | 0.3257 | ±0.6514 | +1.034 | 0.3012 |  |
| Education: high school or below (vs college) | +0.0205 | 0.4646 | ±0.9292 | +0.044 | 0.9648 |  |
| Site: UCSD (vs UAB) | -0.2283 | 0.3767 | ±0.7534 | -0.606 | 0.5444 |  |
| **Site: UW (vs UAB)** | **-1.6221** | 0.3467 | ±0.6933 | **-4.679** | **2.88e-06** | *** |
| Season: spring (vs autumn) | +0.1465 | 0.3772 | ±0.7545 | +0.388 | 0.6977 |  |
| **Season: summer (vs autumn)** | **+2.5530** | 0.4000 | ±0.8000 | **+6.382** | **1.74e-10** | *** |
| Season: winter (vs autumn) | -0.8153 | 0.4697 | ±0.9395 | -1.736 | 0.0826 | . |
| Age (years) | +0.0116 | 0.0142 | ±0.0285 | +0.814 | 0.4158 |  |
| BMI (kg/m2) | +0.0181 | 0.0203 | ±0.0406 | +0.890 | 0.3733 |  |
| Hypertension | +0.5262 | 0.3631 | ±0.7262 | +1.449 | 0.1473 |  |
| High cholesterol | -0.5901 | 0.3192 | ±0.6384 | -1.849 | 0.0645 | . |
| Kidney disease | -0.2387 | 0.4089 | ±0.8177 | -0.584 | 0.5594 |  |
| Circulatory disease | +0.0895 | 0.3692 | ±0.7384 | +0.242 | 0.8085 |  |
| Glucose SD, pooled (mg/dL) | -0.0107 | 0.0110 | ±0.0219 | -0.976 | 0.3289 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **228**, R² = **0.3214**, Adj R² = **0.2768**, F-statistic = **7.20** (p = **3.59e-12**), Residual SE = **2.114** on **213** df, AIC = **1002.9**, BIC = **1054.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0162** | 1.2411 | ±2.4822 | **+19.350** | **2.02e-83** | *** |
| Education: graduate level (vs college) | +0.3205 | 0.3256 | ±0.6512 | +0.984 | 0.3249 |  |
| Education: high school or below (vs college) | +0.0640 | 0.4604 | ±0.9208 | +0.139 | 0.8894 |  |
| Site: UCSD (vs UAB) | -0.2297 | 0.3732 | ±0.7464 | -0.616 | 0.5382 |  |
| **Site: UW (vs UAB)** | **-1.6248** | 0.3442 | ±0.6884 | **-4.721** | **2.35e-06** | *** |
| Season: spring (vs autumn) | +0.1720 | 0.3802 | ±0.7605 | +0.452 | 0.6510 |  |
| **Season: summer (vs autumn)** | **+2.5515** | 0.3994 | ±0.7988 | **+6.388** | **1.68e-10** | *** |
| Season: winter (vs autumn) | -0.8142 | 0.4677 | ±0.9353 | -1.741 | 0.0817 | . |
| Age (years) | +0.0124 | 0.0141 | ±0.0282 | +0.879 | 0.3793 |  |
| BMI (kg/m2) | +0.0172 | 0.0204 | ±0.0409 | +0.843 | 0.3991 |  |
| Hypertension | +0.5206 | 0.3624 | ±0.7248 | +1.437 | 0.1508 |  |
| High cholesterol | -0.5960 | 0.3197 | ±0.6394 | -1.864 | 0.0623 | . |
| Kidney disease | -0.1989 | 0.4097 | ±0.8194 | -0.485 | 0.6273 |  |
| Circulatory disease | +0.0825 | 0.3661 | ±0.7321 | +0.225 | 0.8216 |  |
| Avg. daily SD (mg/dL) | -0.0169 | 0.0117 | ±0.0235 | -1.440 | 0.1498 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **228**, R² = **0.3147**, Adj R² = **0.2697**, F-statistic = **6.99** (p = **8.97e-12**), Residual SE = **2.124** on **213** df, AIC = **1005.1**, BIC = **1056.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7546** | 1.2682 | ±2.5364 | **+18.731** | **2.75e-78** | *** |
| Education: graduate level (vs college) | +0.3656 | 0.3268 | ±0.6536 | +1.119 | 0.2632 |  |
| Education: high school or below (vs college) | -0.0278 | 0.4699 | ±0.9399 | -0.059 | 0.9528 |  |
| Site: UCSD (vs UAB) | -0.2224 | 0.3733 | ±0.7467 | -0.596 | 0.5513 |  |
| **Site: UW (vs UAB)** | **-1.6053** | 0.3473 | ±0.6946 | **-4.622** | **3.80e-06** | *** |
| Season: spring (vs autumn) | +0.1231 | 0.3786 | ±0.7572 | +0.325 | 0.7451 |  |
| **Season: summer (vs autumn)** | **+2.5659** | 0.4026 | ±0.8052 | **+6.373** | **1.85e-10** | *** |
| Season: winter (vs autumn) | -0.8374 | 0.4672 | ±0.9345 | -1.792 | 0.0731 | . |
| Age (years) | +0.0105 | 0.0145 | ±0.0291 | +0.721 | 0.4711 |  |
| BMI (kg/m2) | +0.0190 | 0.0204 | ±0.0408 | +0.930 | 0.3526 |  |
| Hypertension | +0.5176 | 0.3613 | ±0.7226 | +1.433 | 0.1520 |  |
| High cholesterol | -0.5736 | 0.3196 | ±0.6392 | -1.795 | 0.0727 | . |
| Kidney disease | -0.3079 | 0.4235 | ±0.8470 | -0.727 | 0.4672 |  |
| Circulatory disease | +0.0892 | 0.3679 | ±0.7358 | +0.242 | 0.8084 |  |
| CV (%) | -0.0071 | 0.0252 | ±0.0505 | -0.280 | 0.7798 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **228**, R² = **0.3150**, Adj R² = **0.2700**, F-statistic = **7.00** (p = **8.65e-12**), Residual SE = **2.124** on **213** df, AIC = **1005.0**, BIC = **1056.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3265** | 1.3609 | ±2.7219 | **+17.140** | **7.46e-66** | *** |
| Education: graduate level (vs college) | +0.3606 | 0.3276 | ±0.6552 | +1.101 | 0.2710 |  |
| Education: high school or below (vs college) | -0.0181 | 0.4667 | ±0.9333 | -0.039 | 0.9690 |  |
| Site: UCSD (vs UAB) | -0.2190 | 0.3719 | ±0.7439 | -0.589 | 0.5561 |  |
| **Site: UW (vs UAB)** | **-1.6044** | 0.3460 | ±0.6920 | **-4.637** | **3.53e-06** | *** |
| Season: spring (vs autumn) | +0.1283 | 0.3799 | ±0.7597 | +0.338 | 0.7356 |  |
| **Season: summer (vs autumn)** | **+2.5709** | 0.4017 | ±0.8035 | **+6.400** | **1.56e-10** | *** |
| Season: winter (vs autumn) | -0.8354 | 0.4682 | ±0.9364 | -1.784 | 0.0744 | . |
| Age (years) | +0.0110 | 0.0145 | ±0.0290 | +0.761 | 0.4469 |  |
| BMI (kg/m2) | +0.0191 | 0.0203 | ±0.0405 | +0.941 | 0.3465 |  |
| Hypertension | +0.5137 | 0.3588 | ±0.7177 | +1.432 | 0.1523 |  |
| High cholesterol | -0.5764 | 0.3216 | ±0.6432 | -1.792 | 0.0731 | . |
| Kidney disease | -0.3088 | 0.4147 | ±0.8295 | -0.744 | 0.4566 |  |
| Circulatory disease | +0.0952 | 0.3657 | ±0.7314 | +0.260 | 0.7946 |  |
| Mean / SD ratio | +0.0486 | 0.1362 | ±0.2724 | +0.357 | 0.7212 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **228**, R² = **0.3168**, Adj R² = **0.2719**, F-statistic = **7.06** (p = **6.72e-12**), Residual SE = **2.121** on **213** df, AIC = **1004.4**, BIC = **1055.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.0260** | 1.3204 | ±2.6409 | **+17.438** | **4.24e-68** | *** |
| Education: graduate level (vs college) | +0.3349 | 0.3282 | ±0.6564 | +1.021 | 0.3075 |  |
| Education: high school or below (vs college) | +0.0203 | 0.4611 | ±0.9222 | +0.044 | 0.9649 |  |
| Site: UCSD (vs UAB) | -0.2124 | 0.3710 | ±0.7421 | -0.572 | 0.5671 |  |
| **Site: UW (vs UAB)** | **-1.6059** | 0.3452 | ±0.6903 | **-4.653** | **3.27e-06** | *** |
| Season: spring (vs autumn) | +0.1297 | 0.3801 | ±0.7603 | +0.341 | 0.7330 |  |
| **Season: summer (vs autumn)** | **+2.5682** | 0.4020 | ±0.8039 | **+6.389** | **1.67e-10** | *** |
| Season: winter (vs autumn) | -0.8440 | 0.4632 | ±0.9264 | -1.822 | 0.0685 | . |
| Age (years) | +0.0129 | 0.0144 | ±0.0288 | +0.899 | 0.3687 |  |
| BMI (kg/m2) | +0.0185 | 0.0203 | ±0.0405 | +0.915 | 0.3601 |  |
| Hypertension | +0.5002 | 0.3560 | ±0.7120 | +1.405 | 0.1600 |  |
| High cholesterol | -0.5774 | 0.3203 | ±0.6407 | -1.803 | 0.0715 | . |
| Kidney disease | -0.2901 | 0.4113 | ±0.8225 | -0.705 | 0.4806 |  |
| Circulatory disease | +0.0921 | 0.3657 | ±0.7314 | +0.252 | 0.8012 |  |
| Avg. daily mean/SD | +0.0812 | 0.1111 | ±0.2221 | +0.731 | 0.4645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **228**, R² = **0.3177**, Adj R² = **0.2728**, F-statistic = **7.08** (p = **5.97e-12**), Residual SE = **2.120** on **213** df, AIC = **1004.1**, BIC = **1055.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1661** | 1.3220 | ±2.6441 | **+18.280** | **1.20e-74** | *** |
| Education: graduate level (vs college) | +0.3523 | 0.3316 | ±0.6632 | +1.062 | 0.2880 |  |
| Education: high school or below (vs college) | +0.0237 | 0.4501 | ±0.9001 | +0.053 | 0.9580 |  |
| Site: UCSD (vs UAB) | -0.2000 | 0.3723 | ±0.7445 | -0.537 | 0.5911 |  |
| **Site: UW (vs UAB)** | **-1.6294** | 0.3433 | ±0.6867 | **-4.746** | **2.08e-06** | *** |
| Season: spring (vs autumn) | +0.1423 | 0.3808 | ±0.7615 | +0.374 | 0.7086 |  |
| **Season: summer (vs autumn)** | **+2.5532** | 0.4026 | ±0.8051 | **+6.342** | **2.26e-10** | *** |
| Season: winter (vs autumn) | -0.8473 | 0.4648 | ±0.9296 | -1.823 | 0.0683 | . |
| Age (years) | +0.0100 | 0.0141 | ±0.0282 | +0.712 | 0.4764 |  |
| BMI (kg/m2) | +0.0207 | 0.0200 | ±0.0400 | +1.036 | 0.3000 |  |
| Hypertension | +0.5071 | 0.3588 | ±0.7176 | +1.413 | 0.1575 |  |
| High cholesterol | -0.5708 | 0.3161 | ±0.6321 | -1.806 | 0.0709 | . |
| Kidney disease | -0.3418 | 0.3888 | ±0.7777 | -0.879 | 0.3794 |  |
| Circulatory disease | +0.0904 | 0.3668 | ±0.7336 | +0.246 | 0.8053 |  |
| MAG (mg/dL/h) | -0.0136 | 0.0131 | ±0.0262 | -1.037 | 0.2999 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **228**, R² = **0.3210**, Adj R² = **0.2764**, F-statistic = **7.19** (p = **3.76e-12**), Residual SE = **2.114** on **213** df, AIC = **1003.0**, BIC = **1054.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1618** | 1.2833 | ±2.5666 | **+18.828** | **4.45e-79** | *** |
| Education: graduate level (vs college) | +0.3199 | 0.3273 | ±0.6545 | +0.978 | 0.3283 |  |
| Education: high school or below (vs college) | +0.0743 | 0.4593 | ±0.9186 | +0.162 | 0.8715 |  |
| Site: UCSD (vs UAB) | -0.2304 | 0.3721 | ±0.7442 | -0.619 | 0.5358 |  |
| **Site: UW (vs UAB)** | **-1.6173** | 0.3437 | ±0.6874 | **-4.705** | **2.53e-06** | *** |
| Season: spring (vs autumn) | +0.1775 | 0.3828 | ±0.7657 | +0.464 | 0.6430 |  |
| **Season: summer (vs autumn)** | **+2.5702** | 0.3988 | ±0.7976 | **+6.445** | **1.16e-10** | *** |
| Season: winter (vs autumn) | -0.8192 | 0.4684 | ±0.9367 | -1.749 | 0.0803 | . |
| Age (years) | +0.0122 | 0.0141 | ±0.0282 | +0.864 | 0.3876 |  |
| BMI (kg/m2) | +0.0170 | 0.0206 | ±0.0411 | +0.828 | 0.4076 |  |
| Hypertension | +0.5062 | 0.3605 | ±0.7211 | +1.404 | 0.1603 |  |
| High cholesterol | -0.5882 | 0.3194 | ±0.6388 | -1.841 | 0.0656 | . |
| Kidney disease | -0.2053 | 0.4124 | ±0.8247 | -0.498 | 0.6185 |  |
| Circulatory disease | +0.0989 | 0.3653 | ±0.7307 | +0.271 | 0.7866 |  |
| Avg. daily range (mg/dL) | -0.0047 | 0.0033 | ±0.0067 | -1.404 | 0.1603 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **228**, R² = **0.3145**, Adj R² = **0.2695**, F-statistic = **6.98** (p = **9.22e-12**), Residual SE = **2.125** on **213** df, AIC = **1005.2**, BIC = **1056.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6632** | 1.1666 | ±2.3331 | **+20.284** | **1.76e-91** | *** |
| Education: graduate level (vs college) | +0.3739 | 0.3260 | ±0.6520 | +1.147 | 0.2515 |  |
| Education: high school or below (vs college) | -0.0508 | 0.4607 | ±0.9213 | -0.110 | 0.9122 |  |
| Site: UCSD (vs UAB) | -0.2190 | 0.3810 | ±0.7620 | -0.575 | 0.5655 |  |
| **Site: UW (vs UAB)** | **-1.6013** | 0.3521 | ±0.7042 | **-4.548** | **5.42e-06** | *** |
| Season: spring (vs autumn) | +0.1215 | 0.3782 | ±0.7564 | +0.321 | 0.7481 |  |
| **Season: summer (vs autumn)** | **+2.5664** | 0.4017 | ±0.8034 | **+6.389** | **1.67e-10** | *** |
| Season: winter (vs autumn) | -0.8317 | 0.4689 | ±0.9377 | -1.774 | 0.0761 | . |
| Age (years) | +0.0095 | 0.0143 | ±0.0287 | +0.662 | 0.5077 |  |
| BMI (kg/m2) | +0.0192 | 0.0202 | ±0.0403 | +0.954 | 0.3399 |  |
| Hypertension | +0.5238 | 0.3592 | ±0.7183 | +1.458 | 0.1447 |  |
| High cholesterol | -0.5708 | 0.3177 | ±0.6354 | -1.797 | 0.0724 | . |
| Kidney disease | -0.3321 | 0.4035 | ±0.8070 | -0.823 | 0.4104 |  |
| Circulatory disease | +0.0961 | 0.3656 | ±0.7312 | +0.263 | 0.7926 |  |
| SD of daily means (mg/dL) | -0.0029 | 0.0232 | ±0.0464 | -0.124 | 0.9014 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **228**, R² = **0.3180**, Adj R² = **0.2732**, F-statistic = **7.09** (p = **5.74e-12**), Residual SE = **2.119** on **213** df, AIC = **1004.0**, BIC = **1055.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8875** | 1.3863 | ±2.7727 | **+16.509** | **3.14e-61** | *** |
| Education: graduate level (vs college) | +0.3383 | 0.3249 | ±0.6498 | +1.041 | 0.2977 |  |
| Education: high school or below (vs college) | -0.0193 | 0.4573 | ±0.9146 | -0.042 | 0.9664 |  |
| Site: UCSD (vs UAB) | -0.2270 | 0.3779 | ±0.7558 | -0.601 | 0.5481 |  |
| **Site: UW (vs UAB)** | **-1.6162** | 0.3462 | ±0.6923 | **-4.669** | **3.03e-06** | *** |
| Season: spring (vs autumn) | +0.1571 | 0.3784 | ±0.7567 | +0.415 | 0.6781 |  |
| **Season: summer (vs autumn)** | **+2.5567** | 0.4000 | ±0.8000 | **+6.392** | **1.64e-10** | *** |
| Season: winter (vs autumn) | -0.7902 | 0.4725 | ±0.9451 | -1.672 | 0.0945 | . |
| Age (years) | +0.0102 | 0.0142 | ±0.0284 | +0.716 | 0.4739 |  |
| BMI (kg/m2) | +0.0184 | 0.0204 | ±0.0407 | +0.902 | 0.3669 |  |
| Hypertension | +0.5195 | 0.3615 | ±0.7230 | +1.437 | 0.1507 |  |
| High cholesterol | -0.5702 | 0.3176 | ±0.6351 | -1.796 | 0.0725 | . |
| Kidney disease | -0.2751 | 0.3938 | ±0.7877 | -0.698 | 0.4849 |  |
| Circulatory disease | +0.1129 | 0.3655 | ±0.7311 | +0.309 | 0.7575 |  |
| Time in range 70-180, pooled (%) | +0.0085 | 0.0090 | ±0.0181 | +0.946 | 0.3441 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **228**, R² = **0.3175**, Adj R² = **0.2726**, F-statistic = **7.08** (p = **6.13e-12**), Residual SE = **2.120** on **213** df, AIC = **1004.2**, BIC = **1055.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9388** | 1.3843 | ±2.7686 | **+16.570** | **1.14e-61** | *** |
| Education: graduate level (vs college) | +0.3415 | 0.3248 | ±0.6495 | +1.051 | 0.2931 |  |
| Education: high school or below (vs college) | -0.0183 | 0.4588 | ±0.9175 | -0.040 | 0.9682 |  |
| Site: UCSD (vs UAB) | -0.2278 | 0.3781 | ±0.7562 | -0.603 | 0.5468 |  |
| **Site: UW (vs UAB)** | **-1.6162** | 0.3466 | ±0.6933 | **-4.662** | **3.12e-06** | *** |
| Season: spring (vs autumn) | +0.1571 | 0.3791 | ±0.7583 | +0.414 | 0.6786 |  |
| **Season: summer (vs autumn)** | **+2.5608** | 0.4001 | ±0.8002 | **+6.400** | **1.55e-10** | *** |
| Season: winter (vs autumn) | -0.7890 | 0.4735 | ±0.9469 | -1.666 | 0.0956 | . |
| Age (years) | +0.0101 | 0.0142 | ±0.0284 | +0.713 | 0.4758 |  |
| BMI (kg/m2) | +0.0183 | 0.0204 | ±0.0407 | +0.900 | 0.3679 |  |
| Hypertension | +0.5175 | 0.3617 | ±0.7233 | +1.431 | 0.1525 |  |
| High cholesterol | -0.5698 | 0.3176 | ±0.6351 | -1.794 | 0.0728 | . |
| Kidney disease | -0.2772 | 0.3946 | ±0.7893 | -0.702 | 0.4825 |  |
| Circulatory disease | +0.1116 | 0.3654 | ±0.7308 | +0.306 | 0.7600 |  |
| Avg. daily time in range 70-180 (%) | +0.0079 | 0.0090 | ±0.0181 | +0.878 | 0.3799 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.3154**, Adj R² = **0.2704**, F-statistic = **7.01** (p = **8.22e-12**), Residual SE = **2.123** on **213** df, AIC = **1004.9**, BIC = **1056.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5972** | 1.1440 | ±2.2881 | **+20.626** | **1.59e-94** | *** |
| Education: graduate level (vs college) | +0.3908 | 0.3261 | ±0.6521 | +1.198 | 0.2307 |  |
| Education: high school or below (vs college) | -0.0381 | 0.4515 | ±0.9031 | -0.084 | 0.9327 |  |
| Site: UCSD (vs UAB) | -0.1909 | 0.3691 | ±0.7383 | -0.517 | 0.6051 |  |
| **Site: UW (vs UAB)** | **-1.5647** | 0.3469 | ±0.6938 | **-4.510** | **6.48e-06** | *** |
| Season: spring (vs autumn) | +0.1377 | 0.3784 | ±0.7568 | +0.364 | 0.7160 |  |
| **Season: summer (vs autumn)** | **+2.5708** | 0.4008 | ±0.8016 | **+6.414** | **1.41e-10** | *** |
| Season: winter (vs autumn) | -0.8343 | 0.4675 | ±0.9351 | -1.784 | 0.0744 | . |
| Age (years) | +0.0091 | 0.0141 | ±0.0283 | +0.642 | 0.5212 |  |
| BMI (kg/m2) | +0.0192 | 0.0204 | ±0.0408 | +0.943 | 0.3459 |  |
| Hypertension | +0.5141 | 0.3607 | ±0.7215 | +1.425 | 0.1541 |  |
| High cholesterol | -0.5733 | 0.3170 | ±0.6341 | -1.808 | 0.0706 | . |
| Kidney disease | -0.3389 | 0.3857 | ±0.7713 | -0.879 | 0.3795 |  |
| Circulatory disease | +0.0762 | 0.3644 | ±0.7288 | +0.209 | 0.8343 |  |
| Time < 54 (%) | +0.1067 | 0.1800 | ±0.3599 | +0.593 | 0.5533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **228**, R² = **0.3155**, Adj R² = **0.2705**, F-statistic = **7.01** (p = **8.08e-12**), Residual SE = **2.123** on **213** df, AIC = **1004.8**, BIC = **1056.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6235** | 1.1507 | ±2.3014 | **+20.529** | **1.18e-93** | *** |
| Education: graduate level (vs college) | +0.3959 | 0.3239 | ±0.6478 | +1.222 | 0.2216 |  |
| Education: high school or below (vs college) | -0.0383 | 0.4506 | ±0.9012 | -0.085 | 0.9323 |  |
| Site: UCSD (vs UAB) | -0.1941 | 0.3707 | ±0.7413 | -0.524 | 0.6005 |  |
| **Site: UW (vs UAB)** | **-1.5716** | 0.3483 | ±0.6966 | **-4.512** | **6.42e-06** | *** |
| Season: spring (vs autumn) | +0.1431 | 0.3793 | ±0.7587 | +0.377 | 0.7059 |  |
| **Season: summer (vs autumn)** | **+2.5703** | 0.4034 | ±0.8067 | **+6.372** | **1.86e-10** | *** |
| Season: winter (vs autumn) | -0.8372 | 0.4690 | ±0.9381 | -1.785 | 0.0743 | . |
| Age (years) | +0.0087 | 0.0143 | ±0.0285 | +0.608 | 0.5432 |  |
| BMI (kg/m2) | +0.0193 | 0.0202 | ±0.0404 | +0.958 | 0.3382 |  |
| Hypertension | +0.5171 | 0.3599 | ±0.7198 | +1.437 | 0.1507 |  |
| High cholesterol | -0.5666 | 0.3167 | ±0.6334 | -1.789 | 0.0736 | . |
| Kidney disease | -0.3462 | 0.3847 | ±0.7694 | -0.900 | 0.3682 |  |
| Circulatory disease | +0.0773 | 0.3664 | ±0.7329 | +0.211 | 0.8330 |  |
| Avg. daily time < 54 (%) | +0.1028 | 0.2290 | ±0.4579 | +0.449 | 0.6534 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.3238**, Adj R² = **0.2794**, F-statistic = **7.29** (p = **2.55e-12**), Residual SE = **2.110** on **213** df, AIC = **1002.0**, BIC = **1053.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5972** | 1.1315 | ±2.2630 | **+20.855** | **1.38e-96** | *** |
| Education: graduate level (vs college) | +0.4630 | 0.3237 | ±0.6475 | +1.430 | 0.1527 |  |
| Education: high school or below (vs college) | -0.0771 | 0.4488 | ±0.8976 | -0.172 | 0.8636 |  |
| Site: UCSD (vs UAB) | -0.1788 | 0.3695 | ±0.7390 | -0.484 | 0.6284 |  |
| **Site: UW (vs UAB)** | **-1.5692** | 0.3426 | ±0.6851 | **-4.581** | **4.64e-06** | *** |
| Season: spring (vs autumn) | +0.1910 | 0.3696 | ±0.7392 | +0.517 | 0.6054 |  |
| **Season: summer (vs autumn)** | **+2.5923** | 0.3938 | ±0.7876 | **+6.583** | **4.62e-11** | *** |
| Season: winter (vs autumn) | -0.8120 | 0.4666 | ±0.9332 | -1.740 | 0.0818 | . |
| Age (years) | +0.0060 | 0.0139 | ±0.0278 | +0.430 | 0.6672 |  |
| BMI (kg/m2) | +0.0198 | 0.0209 | ±0.0418 | +0.948 | 0.3431 |  |
| Hypertension | +0.5414 | 0.3534 | ±0.7069 | +1.532 | 0.1256 |  |
| High cholesterol | -0.6040 | 0.3145 | ±0.6289 | -1.921 | 0.0548 | . |
| Kidney disease | -0.3652 | 0.3867 | ±0.7733 | -0.945 | 0.3449 |  |
| Circulatory disease | +0.0874 | 0.3647 | ±0.7294 | +0.240 | 0.8107 |  |
| Time 54-69, pooled (%) | +0.0994 | 0.0574 | ±0.1148 | +1.731 | 0.0835 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **228**, R² = **0.3255**, Adj R² = **0.2812**, F-statistic = **7.34** (p = **2.02e-12**), Residual SE = **2.108** on **213** df, AIC = **1001.5**, BIC = **1052.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6497** | 1.1300 | ±2.2600 | **+20.929** | **2.90e-97** | *** |
| Education: graduate level (vs college) | +0.4703 | 0.3214 | ±0.6428 | +1.463 | 0.1434 |  |
| Education: high school or below (vs college) | -0.0881 | 0.4507 | ±0.9015 | -0.195 | 0.8451 |  |
| Site: UCSD (vs UAB) | -0.1772 | 0.3693 | ±0.7385 | -0.480 | 0.6314 |  |
| **Site: UW (vs UAB)** | **-1.5647** | 0.3415 | ±0.6829 | **-4.582** | **4.59e-06** | *** |
| Season: spring (vs autumn) | +0.1920 | 0.3691 | ±0.7381 | +0.520 | 0.6029 |  |
| **Season: summer (vs autumn)** | **+2.5852** | 0.3937 | ±0.7875 | **+6.566** | **5.17e-11** | *** |
| Season: winter (vs autumn) | -0.8159 | 0.4660 | ±0.9319 | -1.751 | 0.0800 | . |
| Age (years) | +0.0051 | 0.0139 | ±0.0277 | +0.370 | 0.7112 |  |
| BMI (kg/m2) | +0.0197 | 0.0207 | ±0.0414 | +0.949 | 0.3427 |  |
| Hypertension | +0.5451 | 0.3518 | ±0.7037 | +1.549 | 0.1213 |  |
| High cholesterol | -0.6014 | 0.3146 | ±0.6292 | -1.911 | 0.0560 | . |
| Kidney disease | -0.3627 | 0.3841 | ±0.7683 | -0.944 | 0.3450 |  |
| Circulatory disease | +0.0943 | 0.3635 | ±0.7270 | +0.259 | 0.7953 |  |
| Avg. daily time 54-69 (%) | +0.1029 | 0.0539 | ±0.1078 | +1.908 | 0.0563 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **228**, R² = **0.3222**, Adj R² = **0.2776**, F-statistic = **7.23** (p = **3.21e-12**), Residual SE = **2.113** on **213** df, AIC = **1002.6**, BIC = **1054.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5786** | 1.1343 | ±2.2687 | **+20.786** | **5.74e-96** | *** |
| Education: graduate level (vs college) | +0.4496 | 0.3245 | ±0.6490 | +1.386 | 0.1658 |  |
| Education: high school or below (vs college) | -0.0606 | 0.4482 | ±0.8964 | -0.135 | 0.8924 |  |
| Site: UCSD (vs UAB) | -0.1694 | 0.3687 | ±0.7374 | -0.460 | 0.6459 |  |
| **Site: UW (vs UAB)** | **-1.5533** | 0.3430 | ±0.6860 | **-4.529** | **5.94e-06** | *** |
| Season: spring (vs autumn) | +0.1844 | 0.3720 | ±0.7440 | +0.496 | 0.6201 |  |
| **Season: summer (vs autumn)** | **+2.5886** | 0.3959 | ±0.7917 | **+6.539** | **6.19e-11** | *** |
| Season: winter (vs autumn) | -0.8152 | 0.4669 | ±0.9339 | -1.746 | 0.0808 | . |
| Age (years) | +0.0066 | 0.0140 | ±0.0280 | +0.475 | 0.6349 |  |
| BMI (kg/m2) | +0.0196 | 0.0209 | ±0.0418 | +0.937 | 0.3486 |  |
| Hypertension | +0.5330 | 0.3544 | ±0.7088 | +1.504 | 0.1326 |  |
| High cholesterol | -0.5984 | 0.3153 | ±0.6306 | -1.898 | 0.0577 | . |
| Kidney disease | -0.3560 | 0.3869 | ±0.7738 | -0.920 | 0.3575 |  |
| Circulatory disease | +0.0774 | 0.3643 | ±0.7286 | +0.213 | 0.8317 |  |
| Time < 70 (%) | +0.0749 | 0.0487 | ±0.0974 | +1.537 | 0.1243 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **228**, R² = **0.3234**, Adj R² = **0.2789**, F-statistic = **7.27** (p = **2.71e-12**), Residual SE = **2.111** on **213** df, AIC = **1002.2**, BIC = **1053.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6359** | 1.1341 | ±2.2682 | **+20.842** | **1.82e-96** | *** |
| Education: graduate level (vs college) | +0.4578 | 0.3219 | ±0.6438 | +1.422 | 0.1550 |  |
| Education: high school or below (vs college) | -0.0679 | 0.4500 | ±0.9001 | -0.151 | 0.8801 |  |
| Site: UCSD (vs UAB) | -0.1703 | 0.3690 | ±0.7381 | -0.461 | 0.6445 |  |
| **Site: UW (vs UAB)** | **-1.5544** | 0.3422 | ±0.6844 | **-4.542** | **5.56e-06** | *** |
| Season: spring (vs autumn) | +0.1885 | 0.3715 | ±0.7430 | +0.507 | 0.6118 |  |
| **Season: summer (vs autumn)** | **+2.5827** | 0.3963 | ±0.7926 | **+6.517** | **7.18e-11** | *** |
| Season: winter (vs autumn) | -0.8205 | 0.4664 | ±0.9327 | -1.759 | 0.0785 | . |
| Age (years) | +0.0058 | 0.0140 | ±0.0280 | +0.413 | 0.6798 |  |
| BMI (kg/m2) | +0.0195 | 0.0206 | ±0.0412 | +0.949 | 0.3428 |  |
| Hypertension | +0.5375 | 0.3530 | ±0.7059 | +1.523 | 0.1278 |  |
| High cholesterol | -0.5911 | 0.3159 | ±0.6317 | -1.871 | 0.0613 | . |
| Kidney disease | -0.3590 | 0.3841 | ±0.7681 | -0.935 | 0.3500 |  |
| Circulatory disease | +0.0828 | 0.3638 | ±0.7276 | +0.228 | 0.8199 |  |
| Avg. daily time < 70 (%) | +0.0758 | 0.0481 | ±0.0963 | +1.575 | 0.1153 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.3159**, Adj R² = **0.2709**, F-statistic = **7.02** (p = **7.68e-12**), Residual SE = **2.123** on **213** df, AIC = **1004.7**, BIC = **1056.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.6465** | 2.4059 | ±4.8118 | **+9.413** | **4.82e-21** | *** |
| Education: graduate level (vs college) | +0.3619 | 0.3246 | ±0.6493 | +1.115 | 0.2649 |  |
| Education: high school or below (vs college) | -0.0275 | 0.4656 | ±0.9312 | -0.059 | 0.9529 |  |
| Site: UCSD (vs UAB) | -0.2234 | 0.3819 | ±0.7638 | -0.585 | 0.5586 |  |
| **Site: UW (vs UAB)** | **-1.6194** | 0.3531 | ±0.7063 | **-4.586** | **4.53e-06** | *** |
| Season: spring (vs autumn) | +0.1377 | 0.3769 | ±0.7539 | +0.365 | 0.7149 |  |
| **Season: summer (vs autumn)** | **+2.5418** | 0.4024 | ±0.8048 | **+6.317** | **2.68e-10** | *** |
| Season: winter (vs autumn) | -0.8297 | 0.4692 | ±0.9383 | -1.769 | 0.0770 | . |
| Age (years) | +0.0090 | 0.0141 | ±0.0282 | +0.638 | 0.5235 |  |
| BMI (kg/m2) | +0.0187 | 0.0202 | ±0.0403 | +0.928 | 0.3535 |  |
| Hypertension | +0.5285 | 0.3603 | ±0.7206 | +1.467 | 0.1425 |  |
| High cholesterol | -0.5845 | 0.3159 | ±0.6317 | -1.851 | 0.0642 | . |
| Kidney disease | -0.3262 | 0.3854 | ±0.7709 | -0.846 | 0.3974 |  |
| Circulatory disease | +0.1066 | 0.3684 | ±0.7368 | +0.289 | 0.7722 |  |
| Time 54-250, pooled (%) | +0.0108 | 0.0219 | ±0.0438 | +0.491 | 0.6235 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.3156**, Adj R² = **0.2706**, F-statistic = **7.02** (p = **7.98e-12**), Residual SE = **2.123** on **213** df, AIC = **1004.8**, BIC = **1056.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.6340** | 2.7360 | ±5.4720 | **+8.273** | **1.31e-16** | *** |
| Education: graduate level (vs college) | +0.3625 | 0.3246 | ±0.6492 | +1.117 | 0.2641 |  |
| Education: high school or below (vs college) | -0.0258 | 0.4701 | ±0.9402 | -0.055 | 0.9563 |  |
| Site: UCSD (vs UAB) | -0.2213 | 0.3816 | ±0.7632 | -0.580 | 0.5620 |  |
| **Site: UW (vs UAB)** | **-1.6145** | 0.3524 | ±0.7049 | **-4.581** | **4.63e-06** | *** |
| Season: spring (vs autumn) | +0.1421 | 0.3786 | ±0.7573 | +0.375 | 0.7075 |  |
| **Season: summer (vs autumn)** | **+2.5481** | 0.4020 | ±0.8041 | **+6.338** | **2.33e-10** | *** |
| Season: winter (vs autumn) | -0.8240 | 0.4674 | ±0.9348 | -1.763 | 0.0779 | . |
| Age (years) | +0.0092 | 0.0141 | ±0.0282 | +0.649 | 0.5163 |  |
| BMI (kg/m2) | +0.0186 | 0.0201 | ±0.0402 | +0.924 | 0.3556 |  |
| Hypertension | +0.5278 | 0.3602 | ±0.7205 | +1.465 | 0.1429 |  |
| High cholesterol | -0.5831 | 0.3159 | ±0.6318 | -1.846 | 0.0649 | . |
| Kidney disease | -0.3231 | 0.3873 | ±0.7747 | -0.834 | 0.4042 |  |
| Circulatory disease | +0.1087 | 0.3667 | ±0.7335 | +0.296 | 0.7670 |  |
| Avg. daily time 54-250 (%) | +0.0107 | 0.0254 | ±0.0508 | +0.422 | 0.6732 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.3208**, Adj R² = **0.2762**, F-statistic = **7.19** (p = **3.87e-12**), Residual SE = **2.115** on **213** df, AIC = **1003.1**, BIC = **1054.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7043** | 1.1771 | ±2.3542 | **+20.138** | **3.44e-90** | *** |
| Education: graduate level (vs college) | +0.3404 | 0.3246 | ±0.6492 | +1.049 | 0.2943 |  |
| Education: high school or below (vs college) | -0.0305 | 0.4487 | ±0.8974 | -0.068 | 0.9458 |  |
| Site: UCSD (vs UAB) | -0.2206 | 0.3733 | ±0.7466 | -0.591 | 0.5544 |  |
| **Site: UW (vs UAB)** | **-1.5953** | 0.3414 | ±0.6828 | **-4.673** | **2.97e-06** | *** |
| Season: spring (vs autumn) | +0.1791 | 0.3782 | ±0.7565 | +0.474 | 0.6358 |  |
| **Season: summer (vs autumn)** | **+2.5907** | 0.3959 | ±0.7918 | **+6.543** | **6.01e-11** | *** |
| Season: winter (vs autumn) | -0.7523 | 0.4807 | ±0.9613 | -1.565 | 0.1175 |  |
| Age (years) | +0.0109 | 0.0141 | ±0.0283 | +0.772 | 0.4403 |  |
| BMI (kg/m2) | +0.0185 | 0.0206 | ±0.0412 | +0.900 | 0.3682 |  |
| Hypertension | +0.5085 | 0.3597 | ±0.7193 | +1.414 | 0.1574 |  |
| High cholesterol | -0.5529 | 0.3179 | ±0.6358 | -1.739 | 0.0820 | . |
| Kidney disease | -0.2394 | 0.3972 | ±0.7945 | -0.603 | 0.5468 |  |
| Circulatory disease | +0.1095 | 0.3634 | ±0.7268 | +0.301 | 0.7631 |  |
| Time 181-250, pooled (%) | -0.0169 | 0.0118 | ±0.0237 | -1.432 | 0.1521 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **228**, R² = **0.3207**, Adj R² = **0.2761**, F-statistic = **7.18** (p = **3.92e-12**), Residual SE = **2.115** on **213** df, AIC = **1003.1**, BIC = **1054.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7319** | 1.1813 | ±2.3626 | **+20.090** | **9.11e-90** | *** |
| Education: graduate level (vs college) | +0.3421 | 0.3243 | ±0.6487 | +1.055 | 0.2915 |  |
| Education: high school or below (vs college) | -0.0288 | 0.4491 | ±0.8982 | -0.064 | 0.9489 |  |
| Site: UCSD (vs UAB) | -0.2268 | 0.3741 | ±0.7482 | -0.606 | 0.5444 |  |
| **Site: UW (vs UAB)** | **-1.6049** | 0.3417 | ±0.6834 | **-4.697** | **2.64e-06** | *** |
| Season: spring (vs autumn) | +0.1751 | 0.3778 | ±0.7556 | +0.463 | 0.6431 |  |
| **Season: summer (vs autumn)** | **+2.5860** | 0.3962 | ±0.7924 | **+6.527** | **6.71e-11** | *** |
| Season: winter (vs autumn) | -0.7555 | 0.4799 | ±0.9597 | -1.574 | 0.1154 |  |
| Age (years) | +0.0105 | 0.0141 | ±0.0283 | +0.744 | 0.4566 |  |
| BMI (kg/m2) | +0.0185 | 0.0206 | ±0.0411 | +0.899 | 0.3687 |  |
| Hypertension | +0.5063 | 0.3601 | ±0.7202 | +1.406 | 0.1597 |  |
| High cholesterol | -0.5542 | 0.3178 | ±0.6356 | -1.744 | 0.0812 | . |
| Kidney disease | -0.2419 | 0.3966 | ±0.7931 | -0.610 | 0.5418 |  |
| Circulatory disease | +0.1073 | 0.3636 | ±0.7273 | +0.295 | 0.7680 |  |
| Avg. daily time 181-250 (%) | -0.0163 | 0.0114 | ±0.0229 | -1.425 | 0.1543 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **228**, R² = **0.3198**, Adj R² = **0.2751**, F-statistic = **7.15** (p = **4.48e-12**), Residual SE = **2.116** on **213** df, AIC = **1003.4**, BIC = **1054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7542** | 1.1764 | ±2.3528 | **+20.193** | **1.14e-90** | *** |
| Education: graduate level (vs college) | +0.3391 | 0.3244 | ±0.6488 | +1.045 | 0.2958 |  |
| Education: high school or below (vs college) | -0.0134 | 0.4542 | ±0.9084 | -0.030 | 0.9764 |  |
| Site: UCSD (vs UAB) | -0.2221 | 0.3769 | ±0.7538 | -0.589 | 0.5556 |  |
| **Site: UW (vs UAB)** | **-1.6140** | 0.3444 | ±0.6888 | **-4.687** | **2.78e-06** | *** |
| Season: spring (vs autumn) | +0.1723 | 0.3775 | ±0.7550 | +0.456 | 0.6482 |  |
| **Season: summer (vs autumn)** | **+2.5575** | 0.3984 | ±0.7969 | **+6.419** | **1.38e-10** | *** |
| Season: winter (vs autumn) | -0.7770 | 0.4728 | ±0.9455 | -1.644 | 0.1003 |  |
| Age (years) | +0.0100 | 0.0142 | ±0.0283 | +0.705 | 0.4805 |  |
| BMI (kg/m2) | +0.0182 | 0.0205 | ±0.0409 | +0.889 | 0.3742 |  |
| Hypertension | +0.5220 | 0.3610 | ±0.7220 | +1.446 | 0.1482 |  |
| High cholesterol | -0.5746 | 0.3174 | ±0.6348 | -1.810 | 0.0703 | . |
| Kidney disease | -0.2625 | 0.3934 | ±0.7869 | -0.667 | 0.5046 |  |
| Circulatory disease | +0.1151 | 0.3662 | ±0.7325 | +0.314 | 0.7534 |  |
| Time > 180 (%) | -0.0103 | 0.0089 | ±0.0178 | -1.150 | 0.2501 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **228**, R² = **0.3195**, Adj R² = **0.2748**, F-statistic = **7.14** (p = **4.63e-12**), Residual SE = **2.117** on **213** df, AIC = **1003.5**, BIC = **1054.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7582** | 1.1781 | ±2.3562 | **+20.167** | **1.92e-90** | *** |
| Education: graduate level (vs college) | +0.3410 | 0.3242 | ±0.6483 | +1.052 | 0.2929 |  |
| Education: high school or below (vs college) | -0.0108 | 0.4551 | ±0.9101 | -0.024 | 0.9811 |  |
| Site: UCSD (vs UAB) | -0.2242 | 0.3774 | ±0.7547 | -0.594 | 0.5525 |  |
| **Site: UW (vs UAB)** | **-1.6157** | 0.3444 | ±0.6888 | **-4.691** | **2.72e-06** | *** |
| Season: spring (vs autumn) | +0.1750 | 0.3784 | ±0.7568 | +0.462 | 0.6438 |  |
| **Season: summer (vs autumn)** | **+2.5611** | 0.3983 | ±0.7966 | **+6.430** | **1.28e-10** | *** |
| Season: winter (vs autumn) | -0.7728 | 0.4738 | ±0.9476 | -1.631 | 0.1029 |  |
| Age (years) | +0.0099 | 0.0142 | ±0.0283 | +0.698 | 0.4854 |  |
| BMI (kg/m2) | +0.0181 | 0.0204 | ±0.0409 | +0.883 | 0.3773 |  |
| Hypertension | +0.5200 | 0.3612 | ±0.7223 | +1.440 | 0.1499 |  |
| High cholesterol | -0.5730 | 0.3174 | ±0.6349 | -1.805 | 0.0711 | . |
| Kidney disease | -0.2607 | 0.3942 | ±0.7885 | -0.661 | 0.5085 |  |
| Circulatory disease | +0.1157 | 0.3661 | ±0.7321 | +0.316 | 0.7519 |  |
| Avg. daily time > 180 (%) | -0.0101 | 0.0090 | ±0.0180 | -1.121 | 0.2623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **228**, R² = **0.3171**, Adj R² = **0.2722**, F-statistic = **7.07** (p = **6.46e-12**), Residual SE = **2.121** on **213** df, AIC = **1004.3**, BIC = **1055.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7185** | 1.1657 | ±2.3314 | **+20.347** | **4.96e-92** | *** |
| Education: graduate level (vs college) | +0.3548 | 0.3244 | ±0.6489 | +1.093 | 0.2742 |  |
| Education: high school or below (vs college) | -0.0372 | 0.4551 | ±0.9103 | -0.082 | 0.9348 |  |
| Site: UCSD (vs UAB) | -0.2234 | 0.3805 | ±0.7609 | -0.587 | 0.5570 |  |
| **Site: UW (vs UAB)** | **-1.6090** | 0.3461 | ±0.6921 | **-4.649** | **3.33e-06** | *** |
| Season: spring (vs autumn) | +0.1519 | 0.3765 | ±0.7531 | +0.403 | 0.6867 |  |
| **Season: summer (vs autumn)** | **+2.5444** | 0.4013 | ±0.8026 | **+6.340** | **2.30e-10** | *** |
| Season: winter (vs autumn) | -0.7972 | 0.4702 | ±0.9403 | -1.696 | 0.0900 | . |
| Age (years) | +0.0091 | 0.0141 | ±0.0282 | +0.646 | 0.5182 |  |
| BMI (kg/m2) | +0.0188 | 0.0204 | ±0.0409 | +0.920 | 0.3573 |  |
| Hypertension | +0.5340 | 0.3575 | ±0.7150 | +1.494 | 0.1353 |  |
| High cholesterol | -0.5638 | 0.3186 | ±0.6373 | -1.769 | 0.0768 | . |
| Kidney disease | -0.3217 | 0.3845 | ±0.7690 | -0.837 | 0.4028 |  |
| Circulatory disease | +0.1164 | 0.3660 | ±0.7321 | +0.318 | 0.7506 |  |
| Nocturnal time > 180 (%) | -0.0073 | 0.0102 | ±0.0204 | -0.722 | 0.4705 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.3161**, Adj R² = **0.2711**, F-statistic = **7.03** (p = **7.43e-12**), Residual SE = **2.122** on **213** df, AIC = **1004.6**, BIC = **1056.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6920** | 1.1823 | ±2.3646 | **+20.039** | **2.54e-89** | *** |
| Education: graduate level (vs college) | +0.3550 | 0.3282 | ±0.6563 | +1.082 | 0.2794 |  |
| Education: high school or below (vs college) | -0.0310 | 0.4529 | ±0.9057 | -0.068 | 0.9455 |  |
| Site: UCSD (vs UAB) | -0.2204 | 0.3720 | ±0.7440 | -0.593 | 0.5534 |  |
| **Site: UW (vs UAB)** | **-1.5796** | 0.3456 | ±0.6912 | **-4.571** | **4.86e-06** | *** |
| Season: spring (vs autumn) | +0.1424 | 0.3819 | ±0.7638 | +0.373 | 0.7092 |  |
| **Season: summer (vs autumn)** | **+2.5823** | 0.3984 | ±0.7968 | **+6.482** | **9.08e-11** | *** |
| Season: winter (vs autumn) | -0.8352 | 0.4669 | ±0.9339 | -1.789 | 0.0737 | . |
| Age (years) | +0.0109 | 0.0141 | ±0.0283 | +0.771 | 0.4406 |  |
| BMI (kg/m2) | +0.0178 | 0.0207 | ±0.0414 | +0.859 | 0.3903 |  |
| Hypertension | +0.5212 | 0.3600 | ±0.7199 | +1.448 | 0.1476 |  |
| High cholesterol | -0.5783 | 0.3179 | ±0.6358 | -1.819 | 0.0689 | . |
| Kidney disease | -0.2883 | 0.3968 | ±0.7937 | -0.727 | 0.4675 |  |
| Circulatory disease | +0.0971 | 0.3651 | ±0.7303 | +0.266 | 0.7903 |  |
| Any reading > 250 during wear (0/1) | -0.2161 | 0.3054 | ±0.6108 | -0.708 | 0.4792 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.3161**, Adj R² = **0.2711**, F-statistic = **7.03** (p = **7.45e-12**), Residual SE = **2.122** on **213** df, AIC = **1004.6**, BIC = **1056.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7240** | 1.1626 | ±2.3252 | **+20.406** | **1.49e-92** | *** |
| Education: graduate level (vs college) | +0.3615 | 0.3246 | ±0.6492 | +1.114 | 0.2655 |  |
| Education: high school or below (vs college) | -0.0238 | 0.4664 | ±0.9328 | -0.051 | 0.9593 |  |
| Site: UCSD (vs UAB) | -0.2209 | 0.3805 | ±0.7610 | -0.580 | 0.5616 |  |
| **Site: UW (vs UAB)** | **-1.6176** | 0.3519 | ±0.7037 | **-4.597** | **4.28e-06** | *** |
| Season: spring (vs autumn) | +0.1404 | 0.3770 | ±0.7541 | +0.372 | 0.7096 |  |
| **Season: summer (vs autumn)** | **+2.5402** | 0.4027 | ±0.8054 | **+6.308** | **2.83e-10** | *** |
| Season: winter (vs autumn) | -0.8284 | 0.4694 | ±0.9388 | -1.765 | 0.0776 | . |
| Age (years) | +0.0090 | 0.0141 | ±0.0282 | +0.635 | 0.5257 |  |
| BMI (kg/m2) | +0.0186 | 0.0202 | ±0.0404 | +0.923 | 0.3558 |  |
| Hypertension | +0.5289 | 0.3602 | ±0.7204 | +1.468 | 0.1420 |  |
| High cholesterol | -0.5862 | 0.3159 | ±0.6318 | -1.856 | 0.0635 | . |
| Kidney disease | -0.3240 | 0.3856 | ±0.7712 | -0.840 | 0.4007 |  |
| Circulatory disease | +0.1061 | 0.3694 | ±0.7388 | +0.287 | 0.7740 |  |
| Time > 250 (%) | -0.0116 | 0.0224 | ±0.0448 | -0.518 | 0.6047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 228)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.3158**, Adj R² = **0.2709**, F-statistic = **7.02** (p = **7.69e-12**), Residual SE = **2.123** on **213** df, AIC = **1004.7**, BIC = **1056.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7120** | 1.1614 | ±2.3227 | **+20.417** | **1.17e-92** | *** |
| Education: graduate level (vs college) | +0.3620 | 0.3246 | ±0.6492 | +1.115 | 0.2648 |  |
| Education: high school or below (vs college) | -0.0206 | 0.4715 | ±0.9430 | -0.044 | 0.9651 |  |
| Site: UCSD (vs UAB) | -0.2189 | 0.3804 | ±0.7607 | -0.575 | 0.5650 |  |
| **Site: UW (vs UAB)** | **-1.6136** | 0.3511 | ±0.7023 | **-4.595** | **4.32e-06** | *** |
| Season: spring (vs autumn) | +0.1467 | 0.3793 | ±0.7586 | +0.387 | 0.6989 |  |
| **Season: summer (vs autumn)** | **+2.5461** | 0.4019 | ±0.8037 | **+6.336** | **2.36e-10** | *** |
| Season: winter (vs autumn) | -0.8219 | 0.4679 | ±0.9357 | -1.757 | 0.0790 | . |
| Age (years) | +0.0091 | 0.0141 | ±0.0282 | +0.643 | 0.5202 |  |
| BMI (kg/m2) | +0.0185 | 0.0201 | ±0.0403 | +0.918 | 0.3586 |  |
| Hypertension | +0.5290 | 0.3599 | ±0.7199 | +1.470 | 0.1417 |  |
| High cholesterol | -0.5846 | 0.3159 | ±0.6319 | -1.850 | 0.0642 | . |
| Kidney disease | -0.3205 | 0.3874 | ±0.7748 | -0.827 | 0.4080 |  |
| Circulatory disease | +0.1090 | 0.3681 | ±0.7361 | +0.296 | 0.7671 |  |
| Avg. daily time > 250 (%) | -0.0120 | 0.0265 | ±0.0530 | -0.455 | 0.6495 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 228; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **228**, R² = **0.1865**, Adj R² = **0.1371**, F-statistic = **3.77** (p = **1.87e-05**), Residual SE = **6.678** on **214** df, AIC = **1526.5**, BIC = **1574.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5096** | 3.8285 | ±7.6570 | **+12.671** | **8.60e-37** | *** |
| Education: graduate level (vs college) | -0.6613 | 1.0542 | ±2.1083 | -0.627 | 0.5304 |  |
| Education: high school or below (vs college) | -0.3239 | 1.4081 | ±2.8162 | -0.230 | 0.8181 |  |
| **Site: UCSD (vs UAB)** | **+3.7523** | 1.1584 | ±2.3168 | **+3.239** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8900 | 1.0155 | ±2.0310 | -0.876 | 0.3808 |  |
| Season: spring (vs autumn) | -1.2987 | 1.2064 | ±2.4127 | -1.077 | 0.2817 |  |
| Season: summer (vs autumn) | +1.5588 | 1.1603 | ±2.3206 | +1.343 | 0.1791 |  |
| **Season: winter (vs autumn)** | **-5.8431** | 1.5066 | ±3.0132 | **-3.878** | **1.05e-04** | *** |
| Age (years) | -0.0646 | 0.0411 | ±0.0823 | -1.569 | 0.1166 |  |
| BMI (kg/m2) | +0.0198 | 0.0726 | ±0.1451 | +0.272 | 0.7853 |  |
| Hypertension | +0.5231 | 1.1662 | ±2.3323 | +0.449 | 0.6538 |  |
| High cholesterol | -0.2123 | 0.9893 | ±1.9787 | -0.215 | 0.8301 |  |
| Kidney disease | +0.8095 | 1.2537 | ±2.5073 | +0.646 | 0.5185 |  |
| Circulatory disease | +0.2229 | 1.0598 | ±2.1195 | +0.210 | 0.8334 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **228**, R² = **0.1904**, Adj R² = **0.1372**, F-statistic = **3.58** (p = **2.57e-05**), Residual SE = **6.678** on **213** df, AIC = **1527.4**, BIC = **1578.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.2534** | 4.7920 | ±9.5840 | **+9.652** | **4.81e-22** | *** |
| Education: graduate level (vs college) | -0.5257 | 1.0815 | ±2.1631 | -0.486 | 0.6269 |  |
| Education: high school or below (vs college) | -0.4399 | 1.4099 | ±2.8199 | -0.312 | 0.7550 |  |
| **Site: UCSD (vs UAB)** | **+3.7670** | 1.1649 | ±2.3297 | **+3.234** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8457 | 1.0090 | ±2.0180 | -0.838 | 0.4019 |  |
| Season: spring (vs autumn) | -1.3830 | 1.2078 | ±2.4155 | -1.145 | 0.2522 |  |
| Season: summer (vs autumn) | +1.5987 | 1.1649 | ±2.3297 | +1.372 | 0.1699 |  |
| **Season: winter (vs autumn)** | **-5.9079** | 1.5245 | ±3.0489 | **-3.875** | **1.06e-04** | *** |
| Age (years) | -0.0707 | 0.0411 | ±0.0822 | -1.720 | 0.0854 | . |
| BMI (kg/m2) | +0.0187 | 0.0732 | ±0.1463 | +0.255 | 0.7986 |  |
| Hypertension | +0.4613 | 1.1611 | ±2.3223 | +0.397 | 0.6912 |  |
| High cholesterol | -0.1520 | 1.0030 | ±2.0060 | -0.152 | 0.8796 |  |
| Kidney disease | +0.7684 | 1.2485 | ±2.4970 | +0.615 | 0.5382 |  |
| Circulatory disease | +0.2142 | 1.0642 | ±2.1285 | +0.201 | 0.8405 |  |
| HbA1c (%) | +0.4154 | 0.4366 | ±0.8732 | +0.952 | 0.3413 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **228**, R² = **0.1924**, Adj R² = **0.1394**, F-statistic = **3.63** (p = **2.09e-05**), Residual SE = **6.670** on **213** df, AIC = **1526.8**, BIC = **1578.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.1463** | 4.3777 | ±8.7554 | **+10.541** | **5.58e-26** | *** |
| Education: graduate level (vs college) | -0.6024 | 1.0552 | ±2.1103 | -0.571 | 0.5681 |  |
| Education: high school or below (vs college) | -0.4440 | 1.4069 | ±2.8138 | -0.316 | 0.7523 |  |
| **Site: UCSD (vs UAB)** | **+3.7524** | 1.1581 | ±2.3161 | **+3.240** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8528 | 1.0146 | ±2.0292 | -0.840 | 0.4006 |  |
| Season: spring (vs autumn) | -1.5059 | 1.2089 | ±2.4178 | -1.246 | 0.2129 |  |
| Season: summer (vs autumn) | +1.5488 | 1.1621 | ±2.3241 | +1.333 | 0.1826 |  |
| **Season: winter (vs autumn)** | **-6.0063** | 1.5329 | ±3.0657 | **-3.918** | **8.91e-05** | *** |
| Age (years) | -0.0649 | 0.0408 | ±0.0816 | -1.590 | 0.1119 |  |
| BMI (kg/m2) | +0.0214 | 0.0736 | ±0.1472 | +0.290 | 0.7717 |  |
| Hypertension | +0.4804 | 1.1600 | ±2.3200 | +0.414 | 0.6788 |  |
| High cholesterol | -0.1536 | 0.9984 | ±1.9969 | -0.154 | 0.8778 |  |
| Kidney disease | +0.6424 | 1.2418 | ±2.4836 | +0.517 | 0.6050 |  |
| Circulatory disease | +0.1634 | 1.0663 | ±2.1326 | +0.153 | 0.8782 |  |
| Mean glucose (mg/dL) | +0.0180 | 0.0141 | ±0.0282 | +1.279 | 0.2009 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **228**, R² = **0.1924**, Adj R² = **0.1394**, F-statistic = **3.63** (p = **2.09e-05**), Residual SE = **6.670** on **213** df, AIC = **1526.8**, BIC = **1578.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6534** | 5.5906 | ±11.1813 | **+7.808** | **5.80e-15** | *** |
| Education: graduate level (vs college) | -0.6024 | 1.0552 | ±2.1103 | -0.571 | 0.5681 |  |
| Education: high school or below (vs college) | -0.4440 | 1.4069 | ±2.8138 | -0.316 | 0.7523 |  |
| **Site: UCSD (vs UAB)** | **+3.7524** | 1.1581 | ±2.3161 | **+3.240** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8528 | 1.0146 | ±2.0292 | -0.840 | 0.4006 |  |
| Season: spring (vs autumn) | -1.5059 | 1.2089 | ±2.4178 | -1.246 | 0.2129 |  |
| Season: summer (vs autumn) | +1.5488 | 1.1621 | ±2.3241 | +1.333 | 0.1826 |  |
| **Season: winter (vs autumn)** | **-6.0063** | 1.5329 | ±3.0657 | **-3.918** | **8.91e-05** | *** |
| Age (years) | -0.0649 | 0.0408 | ±0.0816 | -1.590 | 0.1119 |  |
| BMI (kg/m2) | +0.0214 | 0.0736 | ±0.1472 | +0.290 | 0.7717 |  |
| Hypertension | +0.4804 | 1.1600 | ±2.3200 | +0.414 | 0.6788 |  |
| High cholesterol | -0.1536 | 0.9984 | ±1.9969 | -0.154 | 0.8778 |  |
| Kidney disease | +0.6424 | 1.2418 | ±2.4836 | +0.517 | 0.6050 |  |
| Circulatory disease | +0.1634 | 1.0663 | ±2.1326 | +0.153 | 0.8782 |  |
| GMI (%) | +0.7531 | 0.5889 | ±1.1778 | +1.279 | 0.2009 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **228**, R² = **0.1872**, Adj R² = **0.1338**, F-statistic = **3.50** (p = **3.56e-05**), Residual SE = **6.691** on **213** df, AIC = **1528.3**, BIC = **1579.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.7173** | 4.3362 | ±8.6724 | **+11.004** | **3.64e-28** | *** |
| Education: graduate level (vs college) | -0.6594 | 1.0563 | ±2.1126 | -0.624 | 0.5324 |  |
| Education: high school or below (vs college) | -0.3613 | 1.4084 | ±2.8167 | -0.257 | 0.7976 |  |
| **Site: UCSD (vs UAB)** | **+3.7502** | 1.1623 | ±2.3247 | **+3.226** | **0.0013** | ** |
| Site: UW (vs UAB) | -0.8839 | 1.0184 | ±2.0369 | -0.868 | 0.3854 |  |
| Season: spring (vs autumn) | -1.3717 | 1.2148 | ±2.4295 | -1.129 | 0.2588 |  |
| Season: summer (vs autumn) | +1.5663 | 1.1644 | ±2.3288 | +1.345 | 0.1786 |  |
| **Season: winter (vs autumn)** | **-5.8984** | 1.5379 | ±3.0758 | **-3.835** | **1.25e-04** | *** |
| Age (years) | -0.0636 | 0.0412 | ±0.0823 | -1.545 | 0.1223 |  |
| BMI (kg/m2) | +0.0200 | 0.0731 | ±0.1462 | +0.273 | 0.7848 |  |
| Hypertension | +0.4963 | 1.1607 | ±2.3213 | +0.428 | 0.6689 |  |
| High cholesterol | -0.2074 | 0.9941 | ±1.9882 | -0.209 | 0.8348 |  |
| Kidney disease | +0.7977 | 1.2585 | ±2.5170 | +0.634 | 0.5262 |  |
| Circulatory disease | +0.2018 | 1.0723 | ±2.1446 | +0.188 | 0.8507 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0060 | 0.0137 | ±0.0275 | +0.438 | 0.6617 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1891**, Adj R² = **0.1358**, F-statistic = **3.55** (p = **2.93e-05**), Residual SE = **6.683** on **213** df, AIC = **1527.7**, BIC = **1579.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8914** | 4.1056 | ±8.2113 | **+11.665** | **1.93e-31** | *** |
| Education: graduate level (vs college) | -0.5574 | 1.0589 | ±2.1178 | -0.526 | 0.5986 |  |
| Education: high school or below (vs college) | -0.4969 | 1.4291 | ±2.8581 | -0.348 | 0.7281 |  |
| **Site: UCSD (vs UAB)** | **+3.7765** | 1.1604 | ±2.3208 | **+3.255** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8317 | 1.0242 | ±2.0485 | -0.812 | 0.4168 |  |
| Season: spring (vs autumn) | -1.3532 | 1.2126 | ±2.4252 | -1.116 | 0.2645 |  |
| Season: summer (vs autumn) | +1.5924 | 1.1596 | ±2.3193 | +1.373 | 0.1697 |  |
| **Season: winter (vs autumn)** | **-5.8992** | 1.5185 | ±3.0370 | **-3.885** | **1.02e-04** | *** |
| Age (years) | -0.0700 | 0.0410 | ±0.0821 | -1.705 | 0.0882 | . |
| BMI (kg/m2) | +0.0229 | 0.0745 | ±0.1491 | +0.308 | 0.7583 |  |
| Hypertension | +0.5032 | 1.1665 | ±2.3330 | +0.431 | 0.6662 |  |
| High cholesterol | -0.1626 | 1.0041 | ±2.0082 | -0.162 | 0.8714 |  |
| Kidney disease | +0.5602 | 1.2450 | ±2.4899 | +0.450 | 0.6527 |  |
| Circulatory disease | +0.2289 | 1.0616 | ±2.1233 | +0.216 | 0.8293 |  |
| Glucose SD, pooled (mg/dL) | +0.0251 | 0.0296 | ±0.0592 | +0.849 | 0.3962 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1913**, Adj R² = **0.1382**, F-statistic = **3.60** (p = **2.35e-05**), Residual SE = **6.674** on **213** df, AIC = **1527.1**, BIC = **1578.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6030** | 4.0903 | ±8.1807 | **+11.638** | **2.64e-31** | *** |
| Education: graduate level (vs college) | -0.5163 | 1.0571 | ±2.1141 | -0.488 | 0.6252 |  |
| Education: high school or below (vs college) | -0.6049 | 1.4268 | ±2.8535 | -0.424 | 0.6716 |  |
| **Site: UCSD (vs UAB)** | **+3.7804** | 1.1558 | ±2.3115 | **+3.271** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8240 | 1.0229 | ±2.0459 | -0.806 | 0.4205 |  |
| Season: spring (vs autumn) | -1.4155 | 1.2172 | ±2.4344 | -1.163 | 0.2449 |  |
| Season: summer (vs autumn) | +1.5967 | 1.1583 | ±2.3165 | +1.378 | 0.1681 |  |
| **Season: winter (vs autumn)** | **-5.9032** | 1.5109 | ±3.0218 | **-3.907** | **9.34e-05** | *** |
| Age (years) | -0.0720 | 0.0411 | ±0.0822 | -1.752 | 0.0798 | . |
| BMI (kg/m2) | +0.0250 | 0.0746 | ±0.1491 | +0.335 | 0.7372 |  |
| Hypertension | +0.5163 | 1.1658 | ±2.3315 | +0.443 | 0.6579 |  |
| High cholesterol | -0.1474 | 1.0027 | ±2.0054 | -0.147 | 0.8831 |  |
| Kidney disease | +0.4595 | 1.2376 | ±2.4752 | +0.371 | 0.7104 |  |
| Circulatory disease | +0.2456 | 1.0577 | ±2.1153 | +0.232 | 0.8163 |  |
| Avg. daily SD (mg/dL) | +0.0405 | 0.0335 | ±0.0669 | +1.212 | 0.2257 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **228**, R² = **0.1869**, Adj R² = **0.1334**, F-statistic = **3.50** (p = **3.68e-05**), Residual SE = **6.692** on **213** df, AIC = **1528.4**, BIC = **1579.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.1583** | 4.3860 | ±8.7720 | **+10.980** | **4.77e-28** | *** |
| Education: graduate level (vs college) | -0.6150 | 1.0595 | ±2.1189 | -0.581 | 0.5616 |  |
| Education: high school or below (vs college) | -0.4002 | 1.4563 | ±2.9126 | -0.275 | 0.7834 |  |
| **Site: UCSD (vs UAB)** | **+3.7656** | 1.1637 | ±2.3274 | **+3.236** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8656 | 1.0278 | ±2.0555 | -0.842 | 0.3997 |  |
| Season: spring (vs autumn) | -1.2981 | 1.2103 | ±2.4205 | -1.073 | 0.2835 |  |
| Season: summer (vs autumn) | +1.5630 | 1.1626 | ±2.3253 | +1.344 | 0.1788 |  |
| **Season: winter (vs autumn)** | **-5.8486** | 1.5167 | ±3.0335 | **-3.856** | **1.15e-04** | *** |
| Age (years) | -0.0681 | 0.0418 | ±0.0836 | -1.630 | 0.1031 |  |
| BMI (kg/m2) | +0.0211 | 0.0751 | ±0.1503 | +0.281 | 0.7785 |  |
| Hypertension | +0.5237 | 1.1706 | ±2.3412 | +0.447 | 0.6546 |  |
| High cholesterol | -0.1980 | 1.0016 | ±2.0031 | -0.198 | 0.8433 |  |
| Kidney disease | +0.6980 | 1.2968 | ±2.5936 | +0.538 | 0.5904 |  |
| Circulatory disease | +0.2313 | 1.0647 | ±2.1294 | +0.217 | 0.8280 |  |
| CV (%) | +0.0212 | 0.0757 | ±0.1515 | +0.280 | 0.7791 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **228**, R² = **0.1869**, Adj R² = **0.1335**, F-statistic = **3.50** (p = **3.65e-05**), Residual SE = **6.692** on **213** df, AIC = **1528.4**, BIC = **1579.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.2629** | 3.9733 | ±7.9467 | **+12.398** | **2.67e-35** | *** |
| Education: graduate level (vs college) | -0.6120 | 1.0722 | ±2.1443 | -0.571 | 0.5681 |  |
| Education: high school or below (vs college) | -0.4087 | 1.4406 | ±2.8812 | -0.284 | 0.7766 |  |
| **Site: UCSD (vs UAB)** | **+3.7546** | 1.1624 | ±2.3247 | **+3.230** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8727 | 1.0238 | ±2.0475 | -0.852 | 0.3940 |  |
| Season: spring (vs autumn) | -1.3107 | 1.2142 | ±2.4284 | -1.079 | 0.2804 |  |
| Season: summer (vs autumn) | +1.5502 | 1.1642 | ±2.3285 | +1.331 | 0.1830 |  |
| **Season: winter (vs autumn)** | **-5.8524** | 1.5171 | ±3.0343 | **-3.858** | **1.15e-04** | *** |
| Age (years) | -0.0688 | 0.0417 | ±0.0833 | -1.652 | 0.0986 | . |
| BMI (kg/m2) | +0.0206 | 0.0738 | ±0.1475 | +0.279 | 0.7799 |  |
| Hypertension | +0.5330 | 1.1709 | ±2.3418 | +0.455 | 0.6490 |  |
| High cholesterol | -0.1942 | 1.0012 | ±2.0025 | -0.194 | 0.8462 |  |
| Kidney disease | +0.7220 | 1.2751 | ±2.5502 | +0.566 | 0.5712 |  |
| Circulatory disease | +0.2151 | 1.0684 | ±2.1368 | +0.201 | 0.8404 |  |
| Mean / SD ratio | -0.1176 | 0.3774 | ±0.7547 | -0.312 | 0.7553 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1881**, Adj R² = **0.1347**, F-statistic = **3.52** (p = **3.26e-05**), Residual SE = **6.688** on **213** df, AIC = **1528.0**, BIC = **1579.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.9220** | 3.9776 | ±7.9552 | **+12.551** | **3.94e-36** | *** |
| Education: graduate level (vs college) | -0.5550 | 1.0714 | ±2.1429 | -0.518 | 0.6045 |  |
| Education: high school or below (vs college) | -0.4935 | 1.4276 | ±2.8553 | -0.346 | 0.7296 |  |
| **Site: UCSD (vs UAB)** | **+3.7393** | 1.1584 | ±2.3168 | **+3.228** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8700 | 1.0217 | ±2.0434 | -0.852 | 0.3945 |  |
| Season: spring (vs autumn) | -1.3135 | 1.2138 | ±2.4276 | -1.082 | 0.2792 |  |
| Season: summer (vs autumn) | +1.5568 | 1.1599 | ±2.3199 | +1.342 | 0.1795 |  |
| **Season: winter (vs autumn)** | **-5.8322** | 1.5065 | ±3.0130 | **-3.871** | **1.08e-04** | *** |
| Age (years) | -0.0730 | 0.0420 | ±0.0841 | -1.737 | 0.0824 | . |
| BMI (kg/m2) | +0.0218 | 0.0739 | ±0.1477 | +0.295 | 0.7680 |  |
| Hypertension | +0.5637 | 1.1674 | ±2.3348 | +0.483 | 0.6292 |  |
| High cholesterol | -0.1927 | 0.9972 | ±1.9944 | -0.193 | 0.8468 |  |
| Kidney disease | +0.6829 | 1.2493 | ±2.4986 | +0.547 | 0.5846 |  |
| Circulatory disease | +0.2228 | 1.0668 | ±2.1336 | +0.209 | 0.8346 |  |
| Avg. daily mean/SD | -0.1875 | 0.2819 | ±0.5638 | -0.665 | 0.5059 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **228**, R² = **0.1867**, Adj R² = **0.1333**, F-statistic = **3.49** (p = **3.73e-05**), Residual SE = **6.693** on **213** df, AIC = **1528.4**, BIC = **1579.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.1315** | 4.1725 | ±8.3451 | **+11.535** | **8.76e-31** | *** |
| Education: graduate level (vs college) | -0.6408 | 1.0769 | ±2.1538 | -0.595 | 0.5518 |  |
| Education: high school or below (vs college) | -0.3789 | 1.3931 | ±2.7862 | -0.272 | 0.7856 |  |
| **Site: UCSD (vs UAB)** | **+3.7394** | 1.1564 | ±2.3129 | **+3.234** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8670 | 1.0286 | ±2.0571 | -0.843 | 0.3993 |  |
| Season: spring (vs autumn) | -1.3123 | 1.2156 | ±2.4312 | -1.080 | 0.2803 |  |
| Season: summer (vs autumn) | +1.5689 | 1.1644 | ±2.3289 | +1.347 | 0.1779 |  |
| **Season: winter (vs autumn)** | **-5.8373** | 1.5090 | ±3.0179 | **-3.868** | **1.10e-04** | *** |
| Age (years) | -0.0651 | 0.0416 | ±0.0831 | -1.566 | 0.1173 |  |
| BMI (kg/m2) | +0.0188 | 0.0724 | ±0.1448 | +0.260 | 0.7949 |  |
| Hypertension | +0.5307 | 1.1682 | ±2.3364 | +0.454 | 0.6496 |  |
| High cholesterol | -0.2109 | 0.9928 | ±1.9856 | -0.212 | 0.8318 |  |
| Kidney disease | +0.8073 | 1.2601 | ±2.5203 | +0.641 | 0.5218 |  |
| Circulatory disease | +0.2241 | 1.0651 | ±2.1301 | +0.210 | 0.8334 |  |
| MAG (mg/dL/h) | +0.0097 | 0.0380 | ±0.0760 | +0.256 | 0.7983 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **228**, R² = **0.1899**, Adj R² = **0.1367**, F-statistic = **3.57** (p = **2.71e-05**), Residual SE = **6.680** on **213** df, AIC = **1527.5**, BIC = **1579.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4313** | 4.1514 | ±8.3028 | **+11.425** | **3.12e-30** | *** |
| Education: graduate level (vs college) | -0.5355 | 1.0638 | ±2.1276 | -0.503 | 0.6147 |  |
| Education: high school or below (vs college) | -0.5863 | 1.4318 | ±2.8635 | -0.410 | 0.6822 |  |
| **Site: UCSD (vs UAB)** | **+3.7778** | 1.1584 | ±2.3169 | **+3.261** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8488 | 1.0245 | ±2.0491 | -0.828 | 0.4074 |  |
| Season: spring (vs autumn) | -1.4102 | 1.2223 | ±2.4447 | -1.154 | 0.2486 |  |
| Season: summer (vs autumn) | +1.5528 | 1.1593 | ±2.3185 | +1.339 | 0.1804 |  |
| **Season: winter (vs autumn)** | **-5.8844** | 1.5126 | ±3.0252 | **-3.890** | **1.00e-04** | *** |
| Age (years) | -0.0706 | 0.0415 | ±0.0830 | -1.699 | 0.0893 | . |
| BMI (kg/m2) | +0.0247 | 0.0744 | ±0.1488 | +0.332 | 0.7401 |  |
| Hypertension | +0.5469 | 1.1675 | ±2.3351 | +0.468 | 0.6395 |  |
| High cholesterol | -0.1726 | 1.0002 | ±2.0004 | -0.173 | 0.8630 |  |
| Kidney disease | +0.5221 | 1.2389 | ±2.4778 | +0.421 | 0.6734 |  |
| Circulatory disease | +0.2087 | 1.0616 | ±2.1233 | +0.197 | 0.8442 |  |
| Avg. daily range (mg/dL) | +0.0096 | 0.0094 | ±0.0189 | +1.019 | 0.3080 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **228**, R² = **0.1866**, Adj R² = **0.1332**, F-statistic = **3.49** (p = **3.78e-05**), Residual SE = **6.694** on **213** df, AIC = **1528.4**, BIC = **1579.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4503** | 3.9771 | ±7.9541 | **+12.182** | **3.86e-34** | *** |
| Education: graduate level (vs college) | -0.6445 | 1.0625 | ±2.1250 | -0.607 | 0.5441 |  |
| Education: high school or below (vs college) | -0.3296 | 1.4212 | ±2.8424 | -0.232 | 0.8166 |  |
| **Site: UCSD (vs UAB)** | **+3.7545** | 1.1635 | ±2.3270 | **+3.227** | **0.0013** | ** |
| Site: UW (vs UAB) | -0.8804 | 1.0217 | ±2.0435 | -0.862 | 0.3889 |  |
| Season: spring (vs autumn) | -1.2944 | 1.2097 | ±2.4194 | -1.070 | 0.2846 |  |
| Season: summer (vs autumn) | +1.5609 | 1.1644 | ±2.3288 | +1.341 | 0.1801 |  |
| **Season: winter (vs autumn)** | **-5.8608** | 1.5354 | ±3.0708 | **-3.817** | **1.35e-04** | *** |
| Age (years) | -0.0650 | 0.0411 | ±0.0821 | -1.584 | 0.1131 |  |
| BMI (kg/m2) | +0.0202 | 0.0739 | ±0.1478 | +0.273 | 0.7848 |  |
| Hypertension | +0.5090 | 1.1695 | ±2.3390 | +0.435 | 0.6634 |  |
| High cholesterol | -0.2078 | 0.9978 | ±1.9955 | -0.208 | 0.8350 |  |
| Kidney disease | +0.7795 | 1.2539 | ±2.5078 | +0.622 | 0.5342 |  |
| Circulatory disease | +0.2133 | 1.0795 | ±2.1589 | +0.198 | 0.8434 |  |
| SD of daily means (mg/dL) | +0.0067 | 0.0498 | ±0.0996 | +0.136 | 0.8922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **228**, R² = **0.1928**, Adj R² = **0.1398**, F-statistic = **3.63** (p = **2.01e-05**), Residual SE = **6.668** on **213** df, AIC = **1526.7**, BIC = **1578.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.3873** | 4.2360 | ±8.4720 | **+12.131** | **7.23e-34** | *** |
| Education: graduate level (vs college) | -0.4976 | 1.0618 | ±2.1237 | -0.469 | 0.6393 |  |
| Education: high school or below (vs college) | -0.4540 | 1.4117 | ±2.8234 | -0.322 | 0.7478 |  |
| **Site: UCSD (vs UAB)** | **+3.7867** | 1.1604 | ±2.3207 | **+3.263** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8172 | 1.0106 | ±2.0211 | -0.809 | 0.4187 |  |
| Season: spring (vs autumn) | -1.4282 | 1.2112 | ±2.4225 | -1.179 | 0.2383 |  |
| Season: summer (vs autumn) | +1.5996 | 1.1584 | ±2.3168 | +1.381 | 0.1673 |  |
| **Season: winter (vs autumn)** | **-6.0311** | 1.5294 | ±3.0589 | **-3.943** | **8.03e-05** | *** |
| Age (years) | -0.0679 | 0.0410 | ±0.0820 | -1.658 | 0.0973 | . |
| BMI (kg/m2) | +0.0238 | 0.0738 | ±0.1475 | +0.322 | 0.7473 |  |
| Hypertension | +0.5164 | 1.1614 | ±2.3228 | +0.445 | 0.6566 |  |
| High cholesterol | -0.2072 | 0.9961 | ±1.9922 | -0.208 | 0.8353 |  |
| Kidney disease | +0.5416 | 1.2414 | ±2.4829 | +0.436 | 0.6626 |  |
| Circulatory disease | +0.1429 | 1.0705 | ±2.1410 | +0.134 | 0.8938 |  |
| Time in range 70-180, pooled (%) | -0.0327 | 0.0256 | ±0.0512 | -1.279 | 0.2010 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **228**, R² = **0.1926**, Adj R² = **0.1396**, F-statistic = **3.63** (p = **2.05e-05**), Residual SE = **6.669** on **213** df, AIC = **1526.7**, BIC = **1578.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.3523** | 4.2898 | ±8.5797 | **+11.971** | **5.06e-33** | *** |
| Education: graduate level (vs college) | -0.5005 | 1.0622 | ±2.1244 | -0.471 | 0.6375 |  |
| Education: high school or below (vs college) | -0.4658 | 1.4137 | ±2.8275 | -0.329 | 0.7418 |  |
| **Site: UCSD (vs UAB)** | **+3.7923** | 1.1622 | ±2.3244 | **+3.263** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8128 | 1.0099 | ±2.0197 | -0.805 | 0.4209 |  |
| Season: spring (vs autumn) | -1.4362 | 1.2133 | ±2.4266 | -1.184 | 0.2365 |  |
| Season: summer (vs autumn) | +1.5854 | 1.1595 | ±2.3189 | +1.367 | 0.1715 |  |
| **Season: winter (vs autumn)** | **-6.0475** | 1.5363 | ±3.0725 | **-3.936** | **8.27e-05** | *** |
| Age (years) | -0.0680 | 0.0410 | ±0.0821 | -1.656 | 0.0977 | . |
| BMI (kg/m2) | +0.0242 | 0.0739 | ±0.1477 | +0.328 | 0.7432 |  |
| Hypertension | +0.5243 | 1.1614 | ±2.3227 | +0.451 | 0.6517 |  |
| High cholesterol | -0.2087 | 0.9964 | ±1.9929 | -0.209 | 0.8341 |  |
| Kidney disease | +0.5340 | 1.2400 | ±2.4800 | +0.431 | 0.6667 |  |
| Circulatory disease | +0.1431 | 1.0717 | ±2.1433 | +0.134 | 0.8938 |  |
| Avg. daily time in range 70-180 (%) | -0.0323 | 0.0262 | ±0.0525 | -1.231 | 0.2185 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.1884**, Adj R² = **0.1351**, F-statistic = **3.53** (p = **3.15e-05**), Residual SE = **6.686** on **213** df, AIC = **1527.9**, BIC = **1579.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.6749** | 3.8569 | ±7.7138 | **+12.620** | **1.63e-36** | *** |
| Education: graduate level (vs college) | -0.7009 | 1.0563 | ±2.1126 | -0.664 | 0.5070 |  |
| Education: high school or below (vs college) | -0.3850 | 1.4065 | ±2.8130 | -0.274 | 0.7843 |  |
| **Site: UCSD (vs UAB)** | **+3.6423** | 1.1728 | ±2.3457 | **+3.106** | **0.0019** | ** |
| Site: UW (vs UAB) | -1.0220 | 1.0337 | ±2.0673 | -0.989 | 0.3228 |  |
| Season: spring (vs autumn) | -1.3571 | 1.2191 | ±2.4382 | -1.113 | 0.2656 |  |
| Season: summer (vs autumn) | +1.5448 | 1.1974 | ±2.3947 | +1.290 | 0.1970 |  |
| **Season: winter (vs autumn)** | **-5.8633** | 1.5195 | ±3.0391 | **-3.859** | **1.14e-04** | *** |
| Age (years) | -0.0637 | 0.0412 | ±0.0824 | -1.547 | 0.1219 |  |
| BMI (kg/m2) | +0.0206 | 0.0734 | ±0.1469 | +0.281 | 0.7787 |  |
| Hypertension | +0.5382 | 1.1643 | ±2.3285 | +0.462 | 0.6439 |  |
| High cholesterol | -0.1945 | 0.9919 | ±1.9838 | -0.196 | 0.8445 |  |
| Kidney disease | +0.7852 | 1.2602 | ±2.5204 | +0.623 | 0.5332 |  |
| Circulatory disease | +0.2870 | 1.0657 | ±2.1313 | +0.269 | 0.7877 |  |
| Time < 54 (%) | -0.4329 | 1.0072 | ±2.0144 | -0.430 | 0.6674 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **228**, R² = **0.1889**, Adj R² = **0.1356**, F-statistic = **3.54** (p = **3.00e-05**), Residual SE = **6.684** on **213** df, AIC = **1527.8**, BIC = **1579.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5717** | 3.8185 | ±7.6370 | **+12.720** | **4.57e-37** | *** |
| Education: graduate level (vs college) | -0.7253 | 1.0575 | ±2.1150 | -0.686 | 0.4928 |  |
| Education: high school or below (vs college) | -0.3880 | 1.4037 | ±2.8075 | -0.276 | 0.7822 |  |
| **Site: UCSD (vs UAB)** | **+3.6496** | 1.1610 | ±2.3221 | **+3.143** | **0.0017** | ** |
| Site: UW (vs UAB) | -1.0000 | 1.0237 | ±2.0475 | -0.977 | 0.3287 |  |
| Season: spring (vs autumn) | -1.3839 | 1.2177 | ±2.4354 | -1.137 | 0.2557 |  |
| Season: summer (vs autumn) | +1.5459 | 1.1847 | ±2.3695 | +1.305 | 0.1919 |  |
| **Season: winter (vs autumn)** | **-5.8520** | 1.5136 | ±3.0273 | **-3.866** | **1.11e-04** | *** |
| Age (years) | -0.0620 | 0.0412 | ±0.0825 | -1.502 | 0.1330 |  |
| BMI (kg/m2) | +0.0201 | 0.0725 | ±0.1449 | +0.277 | 0.7818 |  |
| Hypertension | +0.5258 | 1.1648 | ±2.3296 | +0.451 | 0.6517 |  |
| High cholesterol | -0.2222 | 0.9948 | ±1.9896 | -0.223 | 0.8233 |  |
| Kidney disease | +0.8149 | 1.2614 | ±2.5229 | +0.646 | 0.5183 |  |
| Circulatory disease | +0.2863 | 1.0629 | ±2.1258 | +0.269 | 0.7877 |  |
| Avg. daily time < 54 (%) | -0.4418 | 0.7535 | ±1.5069 | -0.586 | 0.5577 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.1866**, Adj R² = **0.1331**, F-statistic = **3.49** (p = **3.79e-05**), Residual SE = **6.694** on **213** df, AIC = **1528.5**, BIC = **1579.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5169** | 3.8530 | ±7.7060 | **+12.592** | **2.34e-36** | *** |
| Education: graduate level (vs college) | -0.6761 | 1.0612 | ±2.1224 | -0.637 | 0.5241 |  |
| Education: high school or below (vs college) | -0.3196 | 1.4211 | ±2.8422 | -0.225 | 0.8221 |  |
| **Site: UCSD (vs UAB)** | **+3.7452** | 1.1685 | ±2.3370 | **+3.205** | **0.0013** | ** |
| Site: UW (vs UAB) | -0.8951 | 1.0149 | ±2.0299 | -0.882 | 0.3778 |  |
| Season: spring (vs autumn) | -1.3109 | 1.2071 | ±2.4142 | -1.086 | 0.2775 |  |
| Season: summer (vs autumn) | +1.5543 | 1.1710 | ±2.3420 | +1.327 | 0.1844 |  |
| **Season: winter (vs autumn)** | **-5.8480** | 1.5208 | ±3.0417 | **-3.845** | **1.20e-04** | *** |
| Age (years) | -0.0640 | 0.0417 | ±0.0835 | -1.533 | 0.1253 |  |
| BMI (kg/m2) | +0.0197 | 0.0732 | ±0.1463 | +0.269 | 0.7878 |  |
| Hypertension | +0.5188 | 1.1691 | ±2.3382 | +0.444 | 0.6572 |  |
| High cholesterol | -0.2059 | 0.9950 | ±1.9900 | -0.207 | 0.8360 |  |
| Kidney disease | +0.8132 | 1.2633 | ±2.5265 | +0.644 | 0.5198 |  |
| Circulatory disease | +0.2238 | 1.0672 | ±2.1343 | +0.210 | 0.8339 |  |
| Time 54-69, pooled (%) | -0.0179 | 0.2101 | ±0.4202 | -0.085 | 0.9321 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **228**, R² = **0.1868**, Adj R² = **0.1334**, F-statistic = **3.50** (p = **3.69e-05**), Residual SE = **6.693** on **213** df, AIC = **1528.4**, BIC = **1579.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5039** | 3.8415 | ±7.6831 | **+12.626** | **1.52e-36** | *** |
| Education: graduate level (vs college) | -0.7045 | 1.0626 | ±2.1253 | -0.663 | 0.5073 |  |
| Education: high school or below (vs college) | -0.3070 | 1.4226 | ±2.8451 | -0.216 | 0.8291 |  |
| **Site: UCSD (vs UAB)** | **+3.7325** | 1.1677 | ±2.3354 | **+3.197** | **0.0014** | ** |
| Site: UW (vs UAB) | -0.9058 | 1.0158 | ±2.0316 | -0.892 | 0.3726 |  |
| Season: spring (vs autumn) | -1.3319 | 1.2095 | ±2.4190 | -1.101 | 0.2708 |  |
| Season: summer (vs autumn) | +1.5502 | 1.1702 | ±2.3405 | +1.325 | 0.1853 |  |
| **Season: winter (vs autumn)** | **-5.8544** | 1.5218 | ±3.0436 | **-3.847** | **1.20e-04** | *** |
| Age (years) | -0.0626 | 0.0418 | ±0.0835 | -1.498 | 0.1342 |  |
| BMI (kg/m2) | +0.0197 | 0.0730 | ±0.1460 | +0.269 | 0.7878 |  |
| Hypertension | +0.5099 | 1.1669 | ±2.3338 | +0.437 | 0.6622 |  |
| High cholesterol | -0.1966 | 0.9945 | ±1.9890 | -0.198 | 0.8433 |  |
| Kidney disease | +0.8181 | 1.2604 | ±2.5208 | +0.649 | 0.5163 |  |
| Circulatory disease | +0.2218 | 1.0675 | ±2.1350 | +0.208 | 0.8354 |  |
| Avg. daily time 54-69 (%) | -0.0498 | 0.1964 | ±0.3928 | -0.254 | 0.7999 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **228**, R² = **0.1868**, Adj R² = **0.1333**, F-statistic = **3.49** (p = **3.71e-05**), Residual SE = **6.693** on **213** df, AIC = **1528.4**, BIC = **1579.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5400** | 3.8518 | ±7.7035 | **+12.602** | **2.06e-36** | *** |
| Education: graduate level (vs college) | -0.6965 | 1.0604 | ±2.1207 | -0.657 | 0.5113 |  |
| Education: high school or below (vs college) | -0.3201 | 1.4138 | ±2.8276 | -0.226 | 0.8209 |  |
| **Site: UCSD (vs UAB)** | **+3.7274** | 1.1704 | ±2.3408 | **+3.185** | **0.0014** | ** |
| Site: UW (vs UAB) | -0.9126 | 1.0144 | ±2.0288 | -0.900 | 0.3683 |  |
| Season: spring (vs autumn) | -1.3300 | 1.2090 | ±2.4180 | -1.100 | 0.2713 |  |
| Season: summer (vs autumn) | +1.5479 | 1.1697 | ±2.3393 | +1.323 | 0.1857 |  |
| **Season: winter (vs autumn)** | **-5.8554** | 1.5226 | ±3.0452 | **-3.846** | **1.20e-04** | *** |
| Age (years) | -0.0632 | 0.0416 | ±0.0832 | -1.519 | 0.1288 |  |
| BMI (kg/m2) | +0.0197 | 0.0733 | ±0.1466 | +0.269 | 0.7882 |  |
| Hypertension | +0.5153 | 1.1685 | ±2.3370 | +0.441 | 0.6592 |  |
| High cholesterol | -0.1971 | 0.9931 | ±1.9863 | -0.199 | 0.8427 |  |
| Kidney disease | +0.8152 | 1.2622 | ±2.5243 | +0.646 | 0.5183 |  |
| Circulatory disease | +0.2304 | 1.0663 | ±2.1326 | +0.216 | 0.8289 |  |
| Time < 70 (%) | -0.0384 | 0.1703 | ±0.3407 | -0.225 | 0.8217 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **228**, R² = **0.1873**, Adj R² = **0.1338**, F-statistic = **3.51** (p = **3.54e-05**), Residual SE = **6.691** on **213** df, AIC = **1528.3**, BIC = **1579.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5113** | 3.8350 | ±7.6700 | **+12.650** | **1.12e-36** | *** |
| Education: graduate level (vs college) | -0.7243 | 1.0605 | ±2.1210 | -0.683 | 0.4946 |  |
| Education: high school or below (vs college) | -0.3118 | 1.4142 | ±2.8285 | -0.220 | 0.8255 |  |
| **Site: UCSD (vs UAB)** | **+3.7131** | 1.1674 | ±2.3347 | **+3.181** | **0.0015** | ** |
| Site: UW (vs UAB) | -0.9252 | 1.0162 | ±2.0324 | -0.910 | 0.3626 |  |
| Season: spring (vs autumn) | -1.3522 | 1.2111 | ±2.4221 | -1.117 | 0.2642 |  |
| Season: summer (vs autumn) | +1.5462 | 1.1694 | ±2.3387 | +1.322 | 0.1861 |  |
| **Season: winter (vs autumn)** | **-5.8585** | 1.5218 | ±3.0436 | **-3.850** | **1.18e-04** | *** |
| Age (years) | -0.0617 | 0.0416 | ±0.0832 | -1.483 | 0.1381 |  |
| BMI (kg/m2) | +0.0197 | 0.0729 | ±0.1459 | +0.270 | 0.7874 |  |
| Hypertension | +0.5069 | 1.1652 | ±2.3304 | +0.435 | 0.6635 |  |
| High cholesterol | -0.1940 | 0.9930 | ±1.9860 | -0.195 | 0.8451 |  |
| Kidney disease | +0.8210 | 1.2597 | ±2.5194 | +0.652 | 0.5146 |  |
| Circulatory disease | +0.2305 | 1.0653 | ±2.1306 | +0.216 | 0.8287 |  |
| Avg. daily time < 70 (%) | -0.0622 | 0.1547 | ±0.3095 | -0.402 | 0.6877 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.1887**, Adj R² = **0.1354**, F-statistic = **3.54** (p = **3.05e-05**), Residual SE = **6.685** on **213** df, AIC = **1527.9**, BIC = **1579.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.0298** | 5.1471 | ±10.2942 | **+10.109** | **5.06e-24** | *** |
| Education: graduate level (vs college) | -0.5935 | 1.0565 | ±2.1130 | -0.562 | 0.5743 |  |
| Education: high school or below (vs college) | -0.4152 | 1.4138 | ±2.8275 | -0.294 | 0.7690 |  |
| **Site: UCSD (vs UAB)** | **+3.7714** | 1.1570 | ±2.3141 | **+3.260** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8115 | 1.0240 | ±2.0481 | -0.792 | 0.4281 |  |
| Season: spring (vs autumn) | -1.3498 | 1.2107 | ±2.4215 | -1.115 | 0.2649 |  |
| Season: summer (vs autumn) | +1.6493 | 1.1662 | ±2.3324 | +1.414 | 0.1573 |  |
| **Season: winter (vs autumn)** | **-5.8769** | 1.5111 | ±3.0222 | **-3.889** | **1.01e-04** | *** |
| Age (years) | -0.0636 | 0.0413 | ±0.0826 | -1.539 | 0.1237 |  |
| BMI (kg/m2) | +0.0223 | 0.0733 | ±0.1467 | +0.304 | 0.7613 |  |
| Hypertension | +0.4852 | 1.1683 | ±2.3366 | +0.415 | 0.6779 |  |
| High cholesterol | -0.1568 | 1.0069 | ±2.0137 | -0.156 | 0.8762 |  |
| Kidney disease | +0.7429 | 1.2482 | ±2.4965 | +0.595 | 0.5517 |  |
| Circulatory disease | +0.1710 | 1.0750 | ±2.1501 | +0.159 | 0.8736 |  |
| Time 54-250, pooled (%) | -0.0382 | 0.0420 | ±0.0841 | -0.908 | 0.3638 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.1894**, Adj R² = **0.1361**, F-statistic = **3.55** (p = **2.86e-05**), Residual SE = **6.682** on **213** df, AIC = **1527.7**, BIC = **1579.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.0256** | 6.0110 | ±12.0220 | **+8.821** | **1.13e-18** | *** |
| Education: graduate level (vs college) | -0.5780 | 1.0566 | ±2.1132 | -0.547 | 0.5844 |  |
| Education: high school or below (vs college) | -0.4472 | 1.4166 | ±2.8332 | -0.316 | 0.7522 |  |
| **Site: UCSD (vs UAB)** | **+3.7670** | 1.1562 | ±2.3124 | **+3.258** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8125 | 1.0218 | ±2.0435 | -0.795 | 0.4265 |  |
| Season: spring (vs autumn) | -1.3831 | 1.2158 | ±2.4316 | -1.138 | 0.2553 |  |
| Season: summer (vs autumn) | +1.6454 | 1.1640 | ±2.3279 | +1.414 | 0.1575 |  |
| **Season: winter (vs autumn)** | **-5.9116** | 1.5179 | ±3.0359 | **-3.894** | **9.84e-05** | *** |
| Age (years) | -0.0640 | 0.0413 | ±0.0825 | -1.551 | 0.1209 |  |
| BMI (kg/m2) | +0.0235 | 0.0736 | ±0.1472 | +0.319 | 0.7496 |  |
| Hypertension | +0.4781 | 1.1683 | ±2.3365 | +0.409 | 0.6824 |  |
| High cholesterol | -0.1483 | 1.0070 | ±2.0141 | -0.147 | 0.8829 |  |
| Kidney disease | +0.7111 | 1.2478 | ±2.4956 | +0.570 | 0.5687 |  |
| Circulatory disease | +0.1479 | 1.0818 | ±2.1635 | +0.137 | 0.8913 |  |
| Avg. daily time 54-250 (%) | -0.0482 | 0.0526 | ±0.1053 | -0.915 | 0.3600 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.1935**, Adj R² = **0.1405**, F-statistic = **3.65** (p = **1.87e-05**), Residual SE = **6.665** on **213** df, AIC = **1526.5**, BIC = **1577.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.3093** | 3.8628 | ±7.7256 | **+12.506** | **6.90e-36** | *** |
| Education: graduate level (vs college) | -0.5387 | 1.0588 | ±2.1176 | -0.509 | 0.6109 |  |
| Education: high school or below (vs college) | -0.3924 | 1.4014 | ±2.8028 | -0.280 | 0.7794 |  |
| **Site: UCSD (vs UAB)** | **+3.7603** | 1.1626 | ±2.3252 | **+3.234** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8960 | 1.0041 | ±2.0081 | -0.892 | 0.3722 |  |
| Season: spring (vs autumn) | -1.4673 | 1.2095 | ±2.4191 | -1.213 | 0.2251 |  |
| Season: summer (vs autumn) | +1.4884 | 1.1638 | ±2.3277 | +1.279 | 0.2009 |  |
| **Season: winter (vs autumn)** | **-6.1055** | 1.5484 | ±3.0968 | **-3.943** | **8.04e-05** | *** |
| Age (years) | -0.0695 | 0.0408 | ±0.0817 | -1.701 | 0.0890 | . |
| BMI (kg/m2) | +0.0224 | 0.0737 | ±0.1475 | +0.304 | 0.7609 |  |
| Hypertension | +0.5512 | 1.1617 | ±2.3234 | +0.474 | 0.6352 |  |
| High cholesterol | -0.2605 | 0.9970 | ±1.9940 | -0.261 | 0.7939 |  |
| Kidney disease | +0.4908 | 1.2478 | ±2.4957 | +0.393 | 0.6941 |  |
| Circulatory disease | +0.1700 | 1.0638 | ±2.1276 | +0.160 | 0.8731 |  |
| Time 181-250, pooled (%) | +0.0511 | 0.0410 | ±0.0820 | +1.248 | 0.2119 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **228**, R² = **0.1931**, Adj R² = **0.1401**, F-statistic = **3.64** (p = **1.95e-05**), Residual SE = **6.667** on **213** df, AIC = **1526.6**, BIC = **1578.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.2326** | 3.8718 | ±7.7436 | **+12.457** | **1.28e-35** | *** |
| Education: graduate level (vs college) | -0.5467 | 1.0586 | ±2.1171 | -0.516 | 0.6056 |  |
| Education: high school or below (vs college) | -0.3958 | 1.4037 | ±2.8075 | -0.282 | 0.7780 |  |
| **Site: UCSD (vs UAB)** | **+3.7781** | 1.1658 | ±2.3316 | **+3.241** | **0.0012** | ** |
| Site: UW (vs UAB) | -0.8675 | 1.0042 | ±2.0083 | -0.864 | 0.3877 |  |
| Season: spring (vs autumn) | -1.4514 | 1.2094 | ±2.4187 | -1.200 | 0.2301 |  |
| Season: summer (vs autumn) | +1.5037 | 1.1631 | ±2.3263 | +1.293 | 0.1961 |  |
| **Season: winter (vs autumn)** | **-6.0901** | 1.5474 | ±3.0948 | **-3.936** | **8.30e-05** | *** |
| Age (years) | -0.0682 | 0.0408 | ±0.0816 | -1.672 | 0.0946 | . |
| BMI (kg/m2) | +0.0225 | 0.0737 | ±0.1474 | +0.306 | 0.7597 |  |
| Hypertension | +0.5570 | 1.1627 | ±2.3254 | +0.479 | 0.6319 |  |
| High cholesterol | -0.2557 | 0.9968 | ±1.9936 | -0.256 | 0.7976 |  |
| Kidney disease | +0.5057 | 1.2457 | ±2.4915 | +0.406 | 0.6848 |  |
| Circulatory disease | +0.1778 | 1.0633 | ±2.1267 | +0.167 | 0.8672 |  |
| Avg. daily time 181-250 (%) | +0.0481 | 0.0397 | ±0.0794 | +1.211 | 0.2260 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **228**, R² = **0.1930**, Adj R² = **0.1399**, F-statistic = **3.64** (p = **1.98e-05**), Residual SE = **6.667** on **213** df, AIC = **1526.7**, BIC = **1578.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.1406** | 3.8884 | ±7.7769 | **+12.380** | **3.33e-35** | *** |
| Education: graduate level (vs college) | -0.5283 | 1.0585 | ±2.1170 | -0.499 | 0.6177 |  |
| Education: high school or below (vs college) | -0.4501 | 1.4074 | ±2.8147 | -0.320 | 0.7491 |  |
| **Site: UCSD (vs UAB)** | **+3.7654** | 1.1573 | ±2.3147 | **+3.254** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8367 | 1.0106 | ±2.0213 | -0.828 | 0.4077 |  |
| Season: spring (vs autumn) | -1.4541 | 1.2118 | ±2.4236 | -1.200 | 0.2302 |  |
| Season: summer (vs autumn) | +1.5901 | 1.1581 | ±2.3162 | +1.373 | 0.1697 |  |
| **Season: winter (vs autumn)** | **-6.0406** | 1.5337 | ±3.0675 | **-3.938** | **8.20e-05** | *** |
| Age (years) | -0.0668 | 0.0409 | ±0.0818 | -1.633 | 0.1024 |  |
| BMI (kg/m2) | +0.0237 | 0.0738 | ±0.1476 | +0.321 | 0.7483 |  |
| Hypertension | +0.5098 | 1.1597 | ±2.3195 | +0.440 | 0.6603 |  |
| High cholesterol | -0.1943 | 0.9970 | ±1.9940 | -0.195 | 0.8454 |  |
| Kidney disease | +0.5479 | 1.2410 | ±2.4820 | +0.441 | 0.6589 |  |
| Circulatory disease | +0.1497 | 1.0703 | ±2.1406 | +0.140 | 0.8888 |  |
| Time > 180 (%) | +0.0326 | 0.0252 | ±0.0505 | +1.290 | 0.1969 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **228**, R² = **0.1932**, Adj R² = **0.1402**, F-statistic = **3.64** (p = **1.93e-05**), Residual SE = **6.666** on **213** df, AIC = **1526.6**, BIC = **1578.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.1118** | 3.8899 | ±7.7798 | **+12.368** | **3.87e-35** | *** |
| Education: graduate level (vs college) | -0.5288 | 1.0580 | ±2.1161 | -0.500 | 0.6173 |  |
| Education: high school or below (vs college) | -0.4642 | 1.4086 | ±2.8173 | -0.330 | 0.7417 |  |
| **Site: UCSD (vs UAB)** | **+3.7727** | 1.1592 | ±2.3184 | **+3.255** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8289 | 1.0093 | ±2.0185 | -0.821 | 0.4115 |  |
| Season: spring (vs autumn) | -1.4697 | 1.2143 | ±2.4286 | -1.210 | 0.2261 |  |
| Season: summer (vs autumn) | +1.5796 | 1.1585 | ±2.3170 | +1.363 | 0.1727 |  |
| **Season: winter (vs autumn)** | **-6.0628** | 1.5406 | ±3.0812 | **-3.935** | **8.31e-05** | *** |
| Age (years) | -0.0665 | 0.0409 | ±0.0818 | -1.626 | 0.1039 |  |
| BMI (kg/m2) | +0.0243 | 0.0738 | ±0.1476 | +0.329 | 0.7421 |  |
| Hypertension | +0.5157 | 1.1592 | ±2.3183 | +0.445 | 0.6564 |  |
| High cholesterol | -0.1988 | 0.9971 | ±1.9941 | -0.199 | 0.8419 |  |
| Kidney disease | +0.5307 | 1.2406 | ±2.4813 | +0.428 | 0.6688 |  |
| Circulatory disease | +0.1443 | 1.0712 | ±2.1423 | +0.135 | 0.8928 |  |
| Avg. daily time > 180 (%) | +0.0334 | 0.0261 | ±0.0522 | +1.281 | 0.2003 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **228**, R² = **0.1866**, Adj R² = **0.1331**, F-statistic = **3.49** (p = **3.79e-05**), Residual SE = **6.694** on **213** df, AIC = **1528.5**, BIC = **1579.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4811** | 3.8838 | ±7.7677 | **+12.483** | **9.27e-36** | *** |
| Education: graduate level (vs college) | -0.6520 | 1.0621 | ±2.1243 | -0.614 | 0.5393 |  |
| Education: high school or below (vs college) | -0.3295 | 1.4137 | ±2.8275 | -0.233 | 0.8157 |  |
| **Site: UCSD (vs UAB)** | **+3.7542** | 1.1653 | ±2.3306 | **+3.222** | **0.0013** | ** |
| Site: UW (vs UAB) | -0.8859 | 1.0222 | ±2.0445 | -0.867 | 0.3862 |  |
| Season: spring (vs autumn) | -1.3088 | 1.2150 | ±2.4300 | -1.077 | 0.2814 |  |
| Season: summer (vs autumn) | +1.5670 | 1.1615 | ±2.3230 | +1.349 | 0.1773 |  |
| **Season: winter (vs autumn)** | **-5.8580** | 1.5419 | ±3.0839 | **-3.799** | **1.45e-04** | *** |
| Age (years) | -0.0645 | 0.0413 | ±0.0826 | -1.562 | 0.1182 |  |
| BMI (kg/m2) | +0.0200 | 0.0732 | ±0.1463 | +0.273 | 0.7848 |  |
| Hypertension | +0.5173 | 1.1663 | ±2.3326 | +0.444 | 0.6574 |  |
| High cholesterol | -0.2141 | 0.9934 | ±1.9867 | -0.215 | 0.8294 |  |
| Kidney disease | +0.8013 | 1.2534 | ±2.5069 | +0.639 | 0.5226 |  |
| Circulatory disease | +0.2143 | 1.0817 | ±2.1633 | +0.198 | 0.8429 |  |
| Nocturnal time > 180 (%) | +0.0026 | 0.0254 | ±0.0508 | +0.102 | 0.9184 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.1866**, Adj R² = **0.1332**, F-statistic = **3.49** (p = **3.77e-05**), Residual SE = **6.694** on **213** df, AIC = **1528.4**, BIC = **1579.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4731** | 3.8990 | ±7.7979 | **+12.432** | **1.75e-35** | *** |
| Education: graduate level (vs college) | -0.6437 | 1.0608 | ±2.1217 | -0.607 | 0.5440 |  |
| Education: high school or below (vs college) | -0.3389 | 1.4222 | ±2.8444 | -0.238 | 0.8117 |  |
| **Site: UCSD (vs UAB)** | **+3.7539** | 1.1648 | ±2.3296 | **+3.223** | **0.0013** | ** |
| Site: UW (vs UAB) | -0.9019 | 1.0163 | ±2.0327 | -0.887 | 0.3748 |  |
| Season: spring (vs autumn) | -1.3116 | 1.2174 | ±2.4347 | -1.077 | 0.2813 |  |
| Season: summer (vs autumn) | +1.5487 | 1.1729 | ±2.3458 | +1.320 | 0.1867 |  |
| **Season: winter (vs autumn)** | **-5.8458** | 1.5138 | ±3.0276 | **-3.862** | **1.13e-04** | *** |
| Age (years) | -0.0657 | 0.0410 | ±0.0820 | -1.602 | 0.1092 |  |
| BMI (kg/m2) | +0.0209 | 0.0742 | ±0.1483 | +0.281 | 0.7784 |  |
| Hypertension | +0.5207 | 1.1686 | ±2.3373 | +0.446 | 0.6559 |  |
| High cholesterol | -0.2059 | 0.9953 | ±1.9906 | -0.207 | 0.8361 |  |
| Kidney disease | +0.7713 | 1.2592 | ±2.5184 | +0.613 | 0.5402 |  |
| Circulatory disease | +0.2195 | 1.0673 | ±2.1346 | +0.206 | 0.8371 |  |
| Any reading > 250 during wear (0/1) | +0.1460 | 0.9490 | ±1.8980 | +0.154 | 0.8777 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.1891**, Adj R² = **0.1358**, F-statistic = **3.55** (p = **2.94e-05**), Residual SE = **6.683** on **213** df, AIC = **1527.7**, BIC = **1579.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.2016** | 3.8912 | ±7.7823 | **+12.387** | **3.06e-35** | *** |
| Education: graduate level (vs college) | -0.5912 | 1.0553 | ±2.1107 | -0.560 | 0.5753 |  |
| Education: high school or below (vs college) | -0.4292 | 1.4136 | ±2.8272 | -0.304 | 0.7614 |  |
| **Site: UCSD (vs UAB)** | **+3.7625** | 1.1553 | ±2.3106 | **+3.257** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8172 | 1.0225 | ±2.0451 | -0.799 | 0.4242 |  |
| Season: spring (vs autumn) | -1.3600 | 1.2114 | ±2.4229 | -1.123 | 0.2616 |  |
| Season: summer (vs autumn) | +1.6560 | 1.1670 | ±2.3340 | +1.419 | 0.1559 |  |
| **Season: winter (vs autumn)** | **-5.8818** | 1.5118 | ±3.0236 | **-3.891** | **1.00e-04** | *** |
| Age (years) | -0.0634 | 0.0413 | ±0.0826 | -1.535 | 0.1247 |  |
| BMI (kg/m2) | +0.0226 | 0.0733 | ±0.1467 | +0.308 | 0.7581 |  |
| Hypertension | +0.4833 | 1.1677 | ±2.3355 | +0.414 | 0.6790 |  |
| High cholesterol | -0.1502 | 1.0073 | ±2.0147 | -0.149 | 0.8815 |  |
| Kidney disease | +0.7347 | 1.2481 | ±2.4961 | +0.589 | 0.5561 |  |
| Circulatory disease | +0.1725 | 1.0743 | ±2.1485 | +0.161 | 0.8724 |  |
| Time > 250 (%) | +0.0416 | 0.0433 | ±0.0865 | +0.961 | 0.3367 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 228)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.1900**, Adj R² = **0.1367**, F-statistic = **3.57** (p = **2.69e-05**), Residual SE = **6.680** on **213** df, AIC = **1527.5**, BIC = **1578.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.1781** | 3.8850 | ±7.7700 | **+12.401** | **2.58e-35** | *** |
| Education: graduate level (vs college) | -0.5759 | 1.0552 | ±2.1105 | -0.546 | 0.5852 |  |
| Education: high school or below (vs college) | -0.4697 | 1.4171 | ±2.8342 | -0.331 | 0.7403 |  |
| **Site: UCSD (vs UAB)** | **+3.7562** | 1.1547 | ±2.3094 | **+3.253** | **0.0011** | ** |
| Site: UW (vs UAB) | -0.8167 | 1.0200 | ±2.0400 | -0.801 | 0.4233 |  |
| Season: spring (vs autumn) | -1.4036 | 1.2175 | ±2.4350 | -1.153 | 0.2490 |  |
| Season: summer (vs autumn) | +1.6542 | 1.1634 | ±2.3267 | +1.422 | 0.1551 |  |
| **Season: winter (vs autumn)** | **-5.9208** | 1.5191 | ±3.0381 | **-3.898** | **9.71e-05** | *** |
| Age (years) | -0.0636 | 0.0413 | ±0.0825 | -1.542 | 0.1231 |  |
| BMI (kg/m2) | +0.0240 | 0.0735 | ±0.1470 | +0.326 | 0.7444 |  |
| Hypertension | +0.4730 | 1.1669 | ±2.3338 | +0.405 | 0.6852 |  |
| High cholesterol | -0.1419 | 1.0071 | ±2.0143 | -0.141 | 0.8880 |  |
| Kidney disease | +0.7001 | 1.2487 | ±2.4973 | +0.561 | 0.5750 |  |
| Circulatory disease | +0.1467 | 1.0807 | ±2.1613 | +0.136 | 0.8921 |  |
| Avg. daily time > 250 (%) | +0.0539 | 0.0553 | ±0.1105 | +0.976 | 0.3293 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 228; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **228**, R² = **0.1054**, Adj R² = **0.0511**, F-statistic = **1.94** (p = **0.0273**), Residual SE = **19.089** on **214** df, AIC = **2005.4**, BIC = **2053.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.9682** | 13.2243 | ±26.4486 | **+9.450** | **3.39e-21** | *** |
| **Education: graduate level (vs college)** | **-9.4747** | 2.9636 | ±5.9272 | **-3.197** | **0.0014** | ** |
| Education: high school or below (vs college) | +1.3253 | 3.8884 | ±7.7768 | +0.341 | 0.7332 |  |
| Site: UCSD (vs UAB) | +1.7175 | 3.5086 | ±7.0171 | +0.490 | 0.6245 |  |
| Site: UW (vs UAB) | +0.4106 | 2.9515 | ±5.9029 | +0.139 | 0.8894 |  |
| Season: spring (vs autumn) | +3.0557 | 3.4063 | ±6.8126 | +0.897 | 0.3697 |  |
| Season: summer (vs autumn) | +1.8966 | 3.4814 | ±6.9629 | +0.545 | 0.5859 |  |
| **Season: winter (vs autumn)** | **+10.0481** | 4.7962 | ±9.5924 | **+2.095** | **0.0362** | * |
| Age (years) | -0.0502 | 0.1244 | ±0.2487 | -0.404 | 0.6862 |  |
| BMI (kg/m2) | +0.1719 | 0.1842 | ±0.3683 | +0.933 | 0.3507 |  |
| Hypertension | -2.5776 | 3.2962 | ±6.5925 | -0.782 | 0.4342 |  |
| High cholesterol | +2.4388 | 3.1116 | ±6.2232 | +0.784 | 0.4332 |  |
| Kidney disease | +1.5802 | 3.8039 | ±7.6078 | +0.415 | 0.6778 |  |
| Circulatory disease | -4.1215 | 3.5007 | ±7.0015 | -1.177 | 0.2391 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **228**, R² = **0.1167**, Adj R² = **0.0587**, F-statistic = **2.01** (p = **0.0183**), Residual SE = **19.012** on **213** df, AIC = **2004.5**, BIC = **2055.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.4781** | 11.7793 | ±23.5585 | **+11.501** | **1.30e-30** | *** |
| **Education: graduate level (vs college)** | **-10.1066** | 2.8675 | ±5.7351 | **-3.524** | **4.24e-04** | *** |
| Education: high school or below (vs college) | +1.8658 | 3.9142 | ±7.8284 | +0.477 | 0.6336 |  |
| Site: UCSD (vs UAB) | +1.6489 | 3.4836 | ±6.9672 | +0.473 | 0.6360 |  |
| Site: UW (vs UAB) | +0.2041 | 2.9938 | ±5.9876 | +0.068 | 0.9456 |  |
| Season: spring (vs autumn) | +3.4482 | 3.4198 | ±6.8396 | +1.008 | 0.3133 |  |
| Season: summer (vs autumn) | +1.7109 | 3.4664 | ±6.9329 | +0.494 | 0.6216 |  |
| **Season: winter (vs autumn)** | **+10.3500** | 4.6956 | ±9.3911 | **+2.204** | **0.0275** | * |
| Age (years) | -0.0215 | 0.1460 | ±0.2920 | -0.147 | 0.8828 |  |
| BMI (kg/m2) | +0.1770 | 0.1870 | ±0.3741 | +0.946 | 0.3440 |  |
| Hypertension | -2.2897 | 3.3986 | ±6.7972 | -0.674 | 0.5005 |  |
| High cholesterol | +2.1579 | 3.1495 | ±6.2990 | +0.685 | 0.4932 |  |
| Kidney disease | +1.7718 | 3.7054 | ±7.4107 | +0.478 | 0.6325 |  |
| Circulatory disease | -4.0807 | 3.4409 | ±6.8819 | -1.186 | 0.2356 |  |
| HbA1c (%) | -1.9352 | 1.9902 | ±3.9804 | -0.972 | 0.3309 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **228**, R² = **0.1107**, Adj R² = **0.0522**, F-statistic = **1.89** (p = **0.0285**), Residual SE = **19.077** on **213** df, AIC = **2006.0**, BIC = **2057.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+131.0482** | 11.9762 | ±23.9524 | **+10.942** | **7.23e-28** | *** |
| **Education: graduate level (vs college)** | **-9.6263** | 2.9324 | ±5.8648 | **-3.283** | **0.0010** | ** |
| Education: high school or below (vs college) | +1.6342 | 4.0412 | ±8.0824 | +0.404 | 0.6859 |  |
| Site: UCSD (vs UAB) | +1.7172 | 3.5463 | ±7.0927 | +0.484 | 0.6282 |  |
| Site: UW (vs UAB) | +0.3147 | 2.9743 | ±5.9486 | +0.106 | 0.9157 |  |
| Season: spring (vs autumn) | +3.5887 | 3.4924 | ±6.9848 | +1.028 | 0.3041 |  |
| Season: summer (vs autumn) | +1.9224 | 3.5125 | ±7.0249 | +0.547 | 0.5842 |  |
| **Season: winter (vs autumn)** | **+10.4681** | 4.5953 | ±9.1906 | **+2.278** | **0.0227** | * |
| Age (years) | -0.0494 | 0.1278 | ±0.2556 | -0.386 | 0.6991 |  |
| BMI (kg/m2) | +0.1678 | 0.1840 | ±0.3679 | +0.912 | 0.3618 |  |
| Hypertension | -2.4678 | 3.3716 | ±6.7433 | -0.732 | 0.4642 |  |
| High cholesterol | +2.2878 | 3.1482 | ±6.2965 | +0.727 | 0.4674 |  |
| Kidney disease | +2.0103 | 3.7746 | ±7.5492 | +0.533 | 0.5943 |  |
| Circulatory disease | -3.9683 | 3.4646 | ±6.9292 | -1.145 | 0.2520 |  |
| Mean glucose (mg/dL) | -0.0463 | 0.0680 | ±0.1359 | -0.682 | 0.4953 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **228**, R² = **0.1107**, Adj R² = **0.0522**, F-statistic = **1.89** (p = **0.0285**), Residual SE = **19.077** on **213** df, AIC = **2006.0**, BIC = **2057.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+137.4616** | 16.5062 | ±33.0124 | **+8.328** | **8.23e-17** | *** |
| **Education: graduate level (vs college)** | **-9.6263** | 2.9324 | ±5.8648 | **-3.283** | **0.0010** | ** |
| Education: high school or below (vs college) | +1.6342 | 4.0412 | ±8.0824 | +0.404 | 0.6859 |  |
| Site: UCSD (vs UAB) | +1.7172 | 3.5463 | ±7.0927 | +0.484 | 0.6282 |  |
| Site: UW (vs UAB) | +0.3147 | 2.9743 | ±5.9486 | +0.106 | 0.9157 |  |
| Season: spring (vs autumn) | +3.5887 | 3.4924 | ±6.9848 | +1.028 | 0.3041 |  |
| Season: summer (vs autumn) | +1.9224 | 3.5125 | ±7.0249 | +0.547 | 0.5842 |  |
| **Season: winter (vs autumn)** | **+10.4681** | 4.5953 | ±9.1906 | **+2.278** | **0.0227** | * |
| Age (years) | -0.0494 | 0.1278 | ±0.2556 | -0.386 | 0.6991 |  |
| BMI (kg/m2) | +0.1678 | 0.1840 | ±0.3679 | +0.912 | 0.3618 |  |
| Hypertension | -2.4678 | 3.3716 | ±6.7433 | -0.732 | 0.4642 |  |
| High cholesterol | +2.2878 | 3.1482 | ±6.2965 | +0.727 | 0.4674 |  |
| Kidney disease | +2.0103 | 3.7746 | ±7.5492 | +0.533 | 0.5943 |  |
| Circulatory disease | -3.9683 | 3.4646 | ±6.9292 | -1.145 | 0.2520 |  |
| GMI (%) | -1.9376 | 2.8415 | ±5.6831 | -0.682 | 0.4953 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **228**, R² = **0.1209**, Adj R² = **0.0631**, F-statistic = **2.09** (p = **0.0133**), Residual SE = **18.967** on **213** df, AIC = **2003.4**, BIC = **2054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.3072** | 12.4336 | ±24.8672 | **+10.882** | **1.40e-27** | *** |
| **Education: graduate level (vs college)** | **-9.4998** | 2.9934 | ±5.9869 | **-3.174** | **0.0015** | ** |
| Education: high school or below (vs college) | +1.8130 | 3.9855 | ±7.9711 | +0.455 | 0.6492 |  |
| Site: UCSD (vs UAB) | +1.7447 | 3.5397 | ±7.0794 | +0.493 | 0.6221 |  |
| Site: UW (vs UAB) | +0.3310 | 2.9734 | ±5.9469 | +0.111 | 0.9114 |  |
| Season: spring (vs autumn) | +4.0081 | 3.5396 | ±7.0792 | +1.132 | 0.2575 |  |
| Season: summer (vs autumn) | +1.7993 | 3.4911 | ±6.9822 | +0.515 | 0.6063 |  |
| **Season: winter (vs autumn)** | **+10.7703** | 4.5836 | ±9.1672 | **+2.350** | **0.0188** | * |
| Age (years) | -0.0626 | 0.1238 | ±0.2476 | -0.505 | 0.6132 |  |
| BMI (kg/m2) | +0.1692 | 0.1866 | ±0.3732 | +0.907 | 0.3644 |  |
| Hypertension | -2.2282 | 3.3968 | ±6.7937 | -0.656 | 0.5118 |  |
| High cholesterol | +2.3749 | 3.1342 | ±6.2684 | +0.758 | 0.4486 |  |
| Kidney disease | +1.7346 | 3.7023 | ±7.4045 | +0.469 | 0.6394 |  |
| Circulatory disease | -3.8455 | 3.3964 | ±6.7928 | -1.132 | 0.2575 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0784 | 0.0759 | ±0.1519 | -1.033 | 0.3017 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1103**, Adj R² = **0.0519**, F-statistic = **1.89** (p = **0.0291**), Residual SE = **19.080** on **213** df, AIC = **2006.1**, BIC = **2057.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.3001** | 12.5658 | ±25.1317 | **+10.131** | **4.04e-24** | *** |
| **Education: graduate level (vs college)** | **-9.8666** | 2.9115 | ±5.8230 | **-3.389** | **7.02e-04** | *** |
| Education: high school or below (vs college) | +1.9780 | 4.0720 | ±8.1440 | +0.486 | 0.6271 |  |
| Site: UCSD (vs UAB) | +1.6259 | 3.5724 | ±7.1448 | +0.455 | 0.6490 |  |
| Site: UW (vs UAB) | +0.1904 | 2.9699 | ±5.9399 | +0.064 | 0.9489 |  |
| Season: spring (vs autumn) | +3.2612 | 3.4068 | ±6.8136 | +0.957 | 0.3384 |  |
| Season: summer (vs autumn) | +1.7698 | 3.4863 | ±6.9726 | +0.508 | 0.6117 |  |
| **Season: winter (vs autumn)** | **+10.2599** | 4.7301 | ±9.4602 | **+2.169** | **0.0301** | * |
| Age (years) | -0.0298 | 0.1360 | ±0.2720 | -0.219 | 0.8263 |  |
| BMI (kg/m2) | +0.1599 | 0.1780 | ±0.3560 | +0.898 | 0.3689 |  |
| Hypertension | -2.5028 | 3.3198 | ±6.6396 | -0.754 | 0.4509 |  |
| High cholesterol | +2.2513 | 3.1042 | ±6.2084 | +0.725 | 0.4683 |  |
| Kidney disease | +2.5209 | 3.8693 | ±7.7385 | +0.652 | 0.5147 |  |
| Circulatory disease | -4.1439 | 3.5092 | ±7.0185 | -1.181 | 0.2377 |  |
| Glucose SD, pooled (mg/dL) | -0.0948 | 0.1157 | ±0.2314 | -0.819 | 0.4126 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1059**, Adj R² = **0.0471**, F-statistic = **1.80** (p = **0.0398**), Residual SE = **19.128** on **213** df, AIC = **2007.2**, BIC = **2058.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7724** | 12.8114 | ±25.6229 | **+9.817** | **9.50e-23** | *** |
| **Education: graduate level (vs college)** | **-9.6033** | 2.9343 | ±5.8687 | **-3.273** | **0.0011** | ** |
| Education: high school or below (vs college) | +1.5745 | 4.0304 | ±8.0609 | +0.391 | 0.6960 |  |
| Site: UCSD (vs UAB) | +1.6925 | 3.5459 | ±7.0919 | +0.477 | 0.6331 |  |
| Site: UW (vs UAB) | +0.3520 | 2.9598 | ±5.9195 | +0.119 | 0.9053 |  |
| Season: spring (vs autumn) | +3.1593 | 3.4256 | ±6.8512 | +0.922 | 0.3564 |  |
| Season: summer (vs autumn) | +1.8631 | 3.4895 | ±6.9789 | +0.534 | 0.5934 |  |
| **Season: winter (vs autumn)** | **+10.1014** | 4.7738 | ±9.5476 | **+2.116** | **0.0343** | * |
| Age (years) | -0.0436 | 0.1310 | ±0.2620 | -0.333 | 0.7392 |  |
| BMI (kg/m2) | +0.1672 | 0.1807 | ±0.3614 | +0.925 | 0.3547 |  |
| Hypertension | -2.5716 | 3.3126 | ±6.6252 | -0.776 | 0.4376 |  |
| High cholesterol | +2.3813 | 3.1211 | ±6.2422 | +0.763 | 0.4455 |  |
| Kidney disease | +1.8908 | 3.8864 | ±7.7728 | +0.487 | 0.6266 |  |
| Circulatory disease | -4.1416 | 3.5209 | ±7.0418 | -1.176 | 0.2395 |  |
| Avg. daily SD (mg/dL) | -0.0360 | 0.1034 | ±0.2068 | -0.348 | 0.7281 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **228**, R² = **0.1055**, Adj R² = **0.0467**, F-statistic = **1.79** (p = **0.0410**), Residual SE = **19.133** on **213** df, AIC = **2007.4**, BIC = **2058.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3267** | 13.0921 | ±26.1842 | **+9.573** | **1.04e-21** | *** |
| **Education: graduate level (vs college)** | **-9.5219** | 2.9759 | ±5.9517 | **-3.200** | **0.0014** | ** |
| Education: high school or below (vs college) | +1.4032 | 4.0041 | ±8.0082 | +0.350 | 0.7260 |  |
| Site: UCSD (vs UAB) | +1.7039 | 3.5574 | ±7.1148 | +0.479 | 0.6320 |  |
| Site: UW (vs UAB) | +0.3856 | 2.9596 | ±5.9191 | +0.130 | 0.8963 |  |
| Season: spring (vs autumn) | +3.0551 | 3.4207 | ±6.8414 | +0.893 | 0.3718 |  |
| Season: summer (vs autumn) | +1.8924 | 3.4912 | ±6.9825 | +0.542 | 0.5878 |  |
| **Season: winter (vs autumn)** | **+10.0537** | 4.8107 | ±9.6213 | **+2.090** | **0.0366** | * |
| Age (years) | -0.0466 | 0.1339 | ±0.2679 | -0.348 | 0.7279 |  |
| BMI (kg/m2) | +0.1705 | 0.1828 | ±0.3656 | +0.933 | 0.3510 |  |
| Hypertension | -2.5783 | 3.3086 | ±6.6172 | -0.779 | 0.4358 |  |
| High cholesterol | +2.4243 | 3.1130 | ±6.2260 | +0.779 | 0.4361 |  |
| Kidney disease | +1.6941 | 3.9037 | ±7.8074 | +0.434 | 0.6643 |  |
| Circulatory disease | -4.1300 | 3.5257 | ±7.0513 | -1.171 | 0.2414 |  |
| CV (%) | -0.0217 | 0.2029 | ±0.4057 | -0.107 | 0.9149 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **228**, R² = **0.1056**, Adj R² = **0.0468**, F-statistic = **1.80** (p = **0.0407**), Residual SE = **19.131** on **213** df, AIC = **2007.3**, BIC = **2058.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.3209** | 16.2357 | ±32.4714 | **+7.780** | **7.23e-15** | *** |
| **Education: graduate level (vs college)** | **-9.3860** | 2.9803 | ±5.9607 | **-3.149** | **0.0016** | ** |
| Education: high school or below (vs college) | +1.1729 | 4.0236 | ±8.0473 | +0.291 | 0.7707 |  |
| Site: UCSD (vs UAB) | +1.7216 | 3.5235 | ±7.0470 | +0.489 | 0.6251 |  |
| Site: UW (vs UAB) | +0.4417 | 2.9503 | ±5.9006 | +0.150 | 0.8810 |  |
| Season: spring (vs autumn) | +3.0341 | 3.4462 | ±6.8923 | +0.880 | 0.3786 |  |
| Season: summer (vs autumn) | +1.8811 | 3.5043 | ±7.0085 | +0.537 | 0.5914 |  |
| **Season: winter (vs autumn)** | **+10.0312** | 4.8118 | ±9.6236 | **+2.085** | **0.0371** | * |
| Age (years) | -0.0579 | 0.1375 | ±0.2749 | -0.421 | 0.6738 |  |
| BMI (kg/m2) | +0.1734 | 0.1836 | ±0.3671 | +0.945 | 0.3449 |  |
| Hypertension | -2.5598 | 3.3144 | ±6.6289 | -0.772 | 0.4399 |  |
| High cholesterol | +2.4713 | 3.1255 | ±6.2510 | +0.791 | 0.4291 |  |
| Kidney disease | +1.4231 | 3.9154 | ±7.8307 | +0.363 | 0.7163 |  |
| Circulatory disease | -4.1355 | 3.5094 | ±7.0188 | -1.178 | 0.2386 |  |
| Mean / SD ratio | -0.2112 | 1.0134 | ±2.0269 | -0.208 | 0.8350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **228**, R² = **0.1083**, Adj R² = **0.0497**, F-statistic = **1.85** (p = **0.0338**), Residual SE = **19.103** on **213** df, AIC = **2006.6**, BIC = **2058.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.2075** | 14.5490 | ±29.0981 | **+8.950** | **3.57e-19** | *** |
| **Education: graduate level (vs college)** | **-9.0801** | 3.0432 | ±6.0863 | **-2.984** | **0.0028** | ** |
| Education: high school or below (vs college) | +0.6960 | 3.9248 | ±7.8497 | +0.177 | 0.8592 |  |
| Site: UCSD (vs UAB) | +1.6693 | 3.5030 | ±7.0060 | +0.477 | 0.6337 |  |
| Site: UW (vs UAB) | +0.4850 | 2.9577 | ±5.9154 | +0.164 | 0.8698 |  |
| Season: spring (vs autumn) | +3.0007 | 3.4415 | ±6.8830 | +0.872 | 0.3832 |  |
| Season: summer (vs autumn) | +1.8892 | 3.4740 | ±6.9479 | +0.544 | 0.5866 |  |
| **Season: winter (vs autumn)** | **+10.0884** | 4.8220 | ±9.6441 | **+2.092** | **0.0364** | * |
| Age (years) | -0.0816 | 0.1294 | ±0.2588 | -0.631 | 0.5283 |  |
| BMI (kg/m2) | +0.1794 | 0.1858 | ±0.3717 | +0.965 | 0.3345 |  |
| Hypertension | -2.4268 | 3.3003 | ±6.6007 | -0.735 | 0.4621 |  |
| High cholesterol | +2.5115 | 3.1184 | ±6.2369 | +0.805 | 0.4206 |  |
| Kidney disease | +1.1107 | 3.8919 | ±7.7838 | +0.285 | 0.7754 |  |
| Circulatory disease | -4.1220 | 3.4961 | ±6.9922 | -1.179 | 0.2384 |  |
| Avg. daily mean/SD | -0.6956 | 0.7804 | ±1.5607 | -0.891 | 0.3727 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **228**, R² = **0.1119**, Adj R² = **0.0535**, F-statistic = **1.92** (p = **0.0261**), Residual SE = **19.064** on **213** df, AIC = **2005.7**, BIC = **2057.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+119.1075** | 12.0520 | ±24.1040 | **+9.883** | **4.94e-23** | *** |
| **Education: graduate level (vs college)** | **-9.1561** | 2.9104 | ±5.8208 | **-3.146** | **0.0017** | ** |
| Education: high school or below (vs college) | +0.4721 | 3.9050 | ±7.8100 | +0.121 | 0.9038 |  |
| Site: UCSD (vs UAB) | +1.5174 | 3.5274 | ±7.0548 | +0.430 | 0.6671 |  |
| Site: UW (vs UAB) | +0.7677 | 2.8723 | ±5.7446 | +0.267 | 0.7893 |  |
| Season: spring (vs autumn) | +2.8445 | 3.4810 | ±6.9620 | +0.817 | 0.4138 |  |
| Season: summer (vs autumn) | +2.0534 | 3.4992 | ±6.9984 | +0.587 | 0.5573 |  |
| **Season: winter (vs autumn)** | **+10.1375** | 4.7979 | ±9.5959 | **+2.113** | **0.0346** | * |
| Age (years) | -0.0586 | 0.1272 | ±0.2545 | -0.461 | 0.6449 |  |
| BMI (kg/m2) | +0.1571 | 0.1862 | ±0.3724 | +0.844 | 0.3987 |  |
| Hypertension | -2.4595 | 3.2406 | ±6.4812 | -0.759 | 0.4479 |  |
| High cholesterol | +2.4597 | 3.1271 | ±6.2542 | +0.787 | 0.4315 |  |
| Kidney disease | +1.5455 | 3.8207 | ±7.6415 | +0.405 | 0.6858 |  |
| Circulatory disease | -4.1038 | 3.4875 | ±6.9750 | -1.177 | 0.2393 |  |
| MAG (mg/dL/h) | +0.1506 | 0.1331 | ±0.2661 | +1.132 | 0.2578 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **228**, R² = **0.1061**, Adj R² = **0.0474**, F-statistic = **1.81** (p = **0.0392**), Residual SE = **19.126** on **213** df, AIC = **2007.2**, BIC = **2058.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.6003** | 12.6285 | ±25.2570 | **+9.787** | **1.28e-22** | *** |
| **Education: graduate level (vs college)** | **-9.3150** | 2.9211 | ±5.8421 | **-3.189** | **0.0014** | ** |
| Education: high school or below (vs college) | +0.9923 | 4.0281 | ±8.0562 | +0.246 | 0.8054 |  |
| Site: UCSD (vs UAB) | +1.7499 | 3.5331 | ±7.0662 | +0.495 | 0.6204 |  |
| Site: UW (vs UAB) | +0.4629 | 2.9468 | ±5.8936 | +0.157 | 0.8752 |  |
| Season: spring (vs autumn) | +2.9142 | 3.4732 | ±6.9464 | +0.839 | 0.4014 |  |
| Season: summer (vs autumn) | +1.8890 | 3.4883 | ±6.9766 | +0.542 | 0.5881 |  |
| **Season: winter (vs autumn)** | **+9.9956** | 4.8016 | ±9.6031 | **+2.082** | **0.0374** | * |
| Age (years) | -0.0579 | 0.1303 | ±0.2607 | -0.444 | 0.6571 |  |
| BMI (kg/m2) | +0.1781 | 0.1813 | ±0.3625 | +0.982 | 0.3259 |  |
| Hypertension | -2.5474 | 3.3064 | ±6.6129 | -0.770 | 0.4410 |  |
| High cholesterol | +2.4891 | 3.1247 | ±6.2495 | +0.797 | 0.4257 |  |
| Kidney disease | +1.2156 | 3.8283 | ±7.6566 | +0.318 | 0.7508 |  |
| Circulatory disease | -4.1395 | 3.5207 | ±7.0415 | -1.176 | 0.2397 |  |
| Avg. daily range (mg/dL) | +0.0122 | 0.0300 | ±0.0600 | +0.407 | 0.6838 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **228**, R² = **0.1394**, Adj R² = **0.0828**, F-statistic = **2.46** (p = **0.0030**), Residual SE = **18.766** on **213** df, AIC = **1998.5**, BIC = **2050.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.4080** | 12.7918 | ±25.5836 | **+10.038** | **1.03e-23** | *** |
| **Education: graduate level (vs college)** | **-10.4510** | 2.9274 | ±5.8547 | **-3.570** | **3.57e-04** | *** |
| Education: high school or below (vs college) | +1.6555 | 3.8308 | ±7.6615 | +0.432 | 0.6656 |  |
| Site: UCSD (vs UAB) | +1.5866 | 3.5161 | ±7.0322 | +0.451 | 0.6518 |  |
| Site: UW (vs UAB) | -0.1472 | 2.9772 | ±5.9544 | -0.049 | 0.9606 |  |
| Season: spring (vs autumn) | +2.8054 | 3.2845 | ±6.5690 | +0.854 | 0.3930 |  |
| Season: summer (vs autumn) | +1.7751 | 3.4704 | ±6.9408 | +0.511 | 0.6090 |  |
| **Season: winter (vs autumn)** | **+11.0759** | 4.5820 | ±9.1640 | **+2.417** | **0.0156** | * |
| Age (years) | -0.0220 | 0.1394 | ±0.2788 | -0.158 | 0.8747 |  |
| BMI (kg/m2) | +0.1480 | 0.1734 | ±0.3468 | +0.854 | 0.3933 |  |
| Hypertension | -1.7592 | 3.3522 | ±6.7044 | -0.525 | 0.5997 |  |
| High cholesterol | +2.1820 | 3.1001 | ±6.2003 | +0.704 | 0.4815 |  |
| Kidney disease | +3.3214 | 3.7143 | ±7.4286 | +0.894 | 0.3712 |  |
| Circulatory disease | -3.5594 | 3.3226 | ±6.6453 | -1.071 | 0.2840 |  |
| SD of daily means (mg/dL) | -0.3916 | 0.2876 | ±0.5751 | -1.362 | 0.1733 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **228**, R² = **0.1069**, Adj R² = **0.0482**, F-statistic = **1.82** (p = **0.0371**), Residual SE = **19.117** on **213** df, AIC = **2007.0**, BIC = **2058.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+121.1196** | 22.0632 | ±44.1265 | **+5.490** | **4.03e-08** | *** |
| **Education: graduate level (vs college)** | **-9.6936** | 2.8254 | ±5.6508 | **-3.431** | **6.02e-04** | *** |
| Education: high school or below (vs college) | +1.4993 | 4.0725 | ±8.1451 | +0.368 | 0.7128 |  |
| Site: UCSD (vs UAB) | +1.6714 | 3.5854 | ±7.1707 | +0.466 | 0.6411 |  |
| Site: UW (vs UAB) | +0.3132 | 2.9508 | ±5.9017 | +0.106 | 0.9155 |  |
| Season: spring (vs autumn) | +3.2289 | 3.4506 | ±6.9013 | +0.936 | 0.3494 |  |
| Season: summer (vs autumn) | +1.8421 | 3.4819 | ±6.9638 | +0.529 | 0.5968 |  |
| **Season: winter (vs autumn)** | **+10.2995** | 4.5619 | ±9.1237 | **+2.258** | **0.0240** | * |
| Age (years) | -0.0457 | 0.1351 | ±0.2702 | -0.338 | 0.7351 |  |
| BMI (kg/m2) | +0.1665 | 0.1791 | ±0.3582 | +0.930 | 0.3525 |  |
| Hypertension | -2.5687 | 3.3781 | ±6.7562 | -0.760 | 0.4470 |  |
| High cholesterol | +2.4320 | 3.1670 | ±6.3340 | +0.768 | 0.4425 |  |
| Kidney disease | +1.9385 | 3.8584 | ±7.7168 | +0.502 | 0.6154 |  |
| Circulatory disease | -4.0145 | 3.4919 | ±6.9839 | -1.150 | 0.2503 |  |
| Time in range 70-180, pooled (%) | +0.0438 | 0.1278 | ±0.2556 | +0.343 | 0.7319 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **228**, R² = **0.1076**, Adj R² = **0.0489**, F-statistic = **1.83** (p = **0.0354**), Residual SE = **19.110** on **213** df, AIC = **2006.8**, BIC = **2058.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+120.3501** | 22.0898 | ±44.1795 | **+5.448** | **5.09e-08** | *** |
| **Education: graduate level (vs college)** | **-9.7359** | 2.8318 | ±5.6637 | **-3.438** | **5.86e-04** | *** |
| Education: high school or below (vs college) | +1.5557 | 4.0762 | ±8.1524 | +0.382 | 0.7027 |  |
| Site: UCSD (vs UAB) | +1.6524 | 3.5860 | ±7.1719 | +0.461 | 0.6449 |  |
| Site: UW (vs UAB) | +0.2851 | 2.9470 | ±5.8940 | +0.097 | 0.9229 |  |
| Season: spring (vs autumn) | +3.2791 | 3.4616 | ±6.9231 | +0.947 | 0.3435 |  |
| Season: summer (vs autumn) | +1.8534 | 3.4890 | ±6.9780 | +0.531 | 0.5953 |  |
| **Season: winter (vs autumn)** | **+10.3801** | 4.5486 | ±9.0972 | **+2.282** | **0.0225** | * |
| Age (years) | -0.0447 | 0.1355 | ±0.2709 | -0.330 | 0.7413 |  |
| BMI (kg/m2) | +0.1647 | 0.1784 | ±0.3569 | +0.923 | 0.3561 |  |
| Hypertension | -2.5796 | 3.3782 | ±6.7565 | -0.764 | 0.4451 |  |
| High cholesterol | +2.4331 | 3.1665 | ±6.3330 | +0.768 | 0.4423 |  |
| Kidney disease | +2.0277 | 3.8424 | ±7.6849 | +0.528 | 0.5977 |  |
| Circulatory disease | -3.9917 | 3.4900 | ±6.9799 | -1.144 | 0.2527 |  |
| Avg. daily time in range 70-180 (%) | +0.0524 | 0.1282 | ±0.2564 | +0.409 | 0.6825 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.1072**, Adj R² = **0.0486**, F-statistic = **1.83** (p = **0.0363**), Residual SE = **19.114** on **213** df, AIC = **2006.9**, BIC = **2058.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.5212** | 13.4157 | ±26.8315 | **+9.282** | **1.67e-20** | *** |
| **Education: graduate level (vs college)** | **-9.3677** | 2.9891 | ±5.9783 | **-3.134** | **0.0017** | ** |
| Education: high school or below (vs college) | +1.4906 | 3.8928 | ±7.7855 | +0.383 | 0.7018 |  |
| Site: UCSD (vs UAB) | +2.0149 | 3.5497 | ±7.0994 | +0.568 | 0.5703 |  |
| Site: UW (vs UAB) | +0.7676 | 3.0625 | ±6.1249 | +0.251 | 0.8021 |  |
| Season: spring (vs autumn) | +3.2135 | 3.4455 | ±6.8910 | +0.933 | 0.3510 |  |
| Season: summer (vs autumn) | +1.9345 | 3.4862 | ±6.9723 | +0.555 | 0.5789 |  |
| **Season: winter (vs autumn)** | **+10.1028** | 4.7977 | ±9.5954 | **+2.106** | **0.0352** | * |
| Age (years) | -0.0526 | 0.1243 | ±0.2485 | -0.423 | 0.6722 |  |
| BMI (kg/m2) | +0.1695 | 0.1854 | ±0.3709 | +0.914 | 0.3606 |  |
| Hypertension | -2.6184 | 3.2919 | ±6.5839 | -0.795 | 0.4264 |  |
| High cholesterol | +2.3908 | 3.1190 | ±6.2381 | +0.767 | 0.4434 |  |
| Kidney disease | +1.6460 | 3.8001 | ±7.6002 | +0.433 | 0.6649 |  |
| Circulatory disease | -4.2947 | 3.5248 | ±7.0496 | -1.218 | 0.2231 |  |
| Time < 54 (%) | +1.1706 | 1.1956 | ±2.3912 | +0.979 | 0.3275 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **228**, R² = **0.1087**, Adj R² = **0.0501**, F-statistic = **1.86** (p = **0.0327**), Residual SE = **19.098** on **213** df, AIC = **2006.5**, BIC = **2058.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.7685** | 13.2818 | ±26.5637 | **+9.394** | **5.78e-21** | *** |
| **Education: graduate level (vs college)** | **-9.2689** | 2.9799 | ±5.9599 | **-3.110** | **0.0019** | ** |
| Education: high school or below (vs college) | +1.5314 | 3.8956 | ±7.7911 | +0.393 | 0.6942 |  |
| Site: UCSD (vs UAB) | +2.0474 | 3.5266 | ±7.0532 | +0.581 | 0.5615 |  |
| Site: UW (vs UAB) | +0.7640 | 3.0221 | ±6.0443 | +0.253 | 0.8004 |  |
| Season: spring (vs autumn) | +3.3297 | 3.4417 | ±6.8835 | +0.967 | 0.3333 |  |
| Season: summer (vs autumn) | +1.9382 | 3.4923 | ±6.9845 | +0.555 | 0.5789 |  |
| **Season: winter (vs autumn)** | **+10.0769** | 4.7974 | ±9.5948 | **+2.100** | **0.0357** | * |
| Age (years) | -0.0586 | 0.1235 | ±0.2470 | -0.475 | 0.6350 |  |
| BMI (kg/m2) | +0.1709 | 0.1850 | ±0.3699 | +0.924 | 0.3555 |  |
| Hypertension | -2.5865 | 3.2859 | ±6.5718 | -0.787 | 0.4312 |  |
| High cholesterol | +2.4708 | 3.1101 | ±6.2202 | +0.794 | 0.4269 |  |
| Kidney disease | +1.5631 | 3.7987 | ±7.5974 | +0.411 | 0.6807 |  |
| Circulatory disease | -4.3251 | 3.5285 | ±7.0571 | -1.226 | 0.2203 |  |
| Avg. daily time < 54 (%) | +1.4200 | 1.2212 | ±2.4423 | +1.163 | 0.2449 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **228**, R² = **0.1092**, Adj R² = **0.0506**, F-statistic = **1.86** (p = **0.0317**), Residual SE = **19.093** on **213** df, AIC = **2006.4**, BIC = **2057.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.7648** | 13.3278 | ±26.6557 | **+9.361** | **7.88e-21** | *** |
| **Education: graduate level (vs college)** | **-9.0660** | 3.0320 | ±6.0640 | **-2.990** | **0.0028** | ** |
| Education: high school or below (vs college) | +1.2061 | 3.9239 | ±7.8479 | +0.307 | 0.7586 |  |
| Site: UCSD (vs UAB) | +1.9128 | 3.5154 | ±7.0309 | +0.544 | 0.5864 |  |
| Site: UW (vs UAB) | +0.5502 | 3.0108 | ±6.0215 | +0.183 | 0.8550 |  |
| Season: spring (vs autumn) | +3.3930 | 3.4561 | ±6.9123 | +0.982 | 0.3262 |  |
| Season: summer (vs autumn) | +2.0213 | 3.4768 | ±6.9535 | +0.581 | 0.5610 |  |
| **Season: winter (vs autumn)** | **+10.1838** | 4.7747 | ±9.5494 | **+2.133** | **0.0329** | * |
| Age (years) | -0.0667 | 0.1223 | ±0.2447 | -0.545 | 0.5854 |  |
| BMI (kg/m2) | +0.1739 | 0.1870 | ±0.3739 | +0.930 | 0.3522 |  |
| Hypertension | -2.4597 | 3.3091 | ±6.6183 | -0.743 | 0.4573 |  |
| High cholesterol | +2.2640 | 3.1161 | ±6.2323 | +0.727 | 0.4675 |  |
| Kidney disease | +1.4791 | 3.8028 | ±7.6056 | +0.389 | 0.6973 |  |
| Circulatory disease | -4.1445 | 3.4963 | ±6.9927 | -1.185 | 0.2359 |  |
| Time 54-69, pooled (%) | +0.4954 | 0.4425 | ±0.8849 | +1.120 | 0.2629 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **228**, R² = **0.1081**, Adj R² = **0.0495**, F-statistic = **1.84** (p = **0.0342**), Residual SE = **19.105** on **213** df, AIC = **2006.7**, BIC = **2058.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0135** | 13.2464 | ±26.4928 | **+9.438** | **3.82e-21** | *** |
| **Education: graduate level (vs college)** | **-9.1282** | 3.0181 | ±6.0362 | **-3.024** | **0.0025** | ** |
| Education: high school or below (vs college) | +1.1900 | 3.9224 | ±7.8448 | +0.303 | 0.7616 |  |
| Site: UCSD (vs UAB) | +1.8759 | 3.5155 | ±7.0310 | +0.534 | 0.5936 |  |
| Site: UW (vs UAB) | +0.5367 | 3.0149 | ±6.0297 | +0.178 | 0.8587 |  |
| Season: spring (vs autumn) | +3.3222 | 3.4517 | ±6.9034 | +0.962 | 0.3358 |  |
| Season: summer (vs autumn) | +1.9660 | 3.4827 | ±6.9654 | +0.565 | 0.5724 |  |
| **Season: winter (vs autumn)** | **+10.1389** | 4.7800 | ±9.5600 | **+2.121** | **0.0339** | * |
| Age (years) | -0.0664 | 0.1224 | ±0.2448 | -0.542 | 0.5877 |  |
| BMI (kg/m2) | +0.1728 | 0.1859 | ±0.3717 | +0.930 | 0.3525 |  |
| Hypertension | -2.4716 | 3.3050 | ±6.6100 | -0.748 | 0.4546 |  |
| High cholesterol | +2.3129 | 3.1126 | ±6.2253 | +0.743 | 0.4574 |  |
| Kidney disease | +1.5112 | 3.8054 | ±7.6109 | +0.397 | 0.6913 |  |
| Circulatory disease | -4.1125 | 3.4983 | ±6.9966 | -1.176 | 0.2398 |  |
| Avg. daily time 54-69 (%) | +0.3992 | 0.4093 | ±0.8186 | +0.975 | 0.3294 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **228**, R² = **0.1092**, Adj R² = **0.0506**, F-statistic = **1.86** (p = **0.0316**), Residual SE = **19.093** on **213** df, AIC = **2006.4**, BIC = **2057.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.6419** | 13.3647 | ±26.7294 | **+9.326** | **1.10e-20** | *** |
| **Education: graduate level (vs college)** | **-9.0974** | 3.0281 | ±6.0562 | **-3.004** | **0.0027** | ** |
| Education: high school or below (vs college) | +1.2844 | 3.9179 | ±7.8357 | +0.328 | 0.7430 |  |
| Site: UCSD (vs UAB) | +1.9845 | 3.5231 | ±7.0462 | +0.563 | 0.5732 |  |
| Site: UW (vs UAB) | +0.6523 | 3.0320 | ±6.0640 | +0.215 | 0.8297 |  |
| Season: spring (vs autumn) | +3.3916 | 3.4569 | ±6.9138 | +0.981 | 0.3265 |  |
| Season: summer (vs autumn) | +2.0136 | 3.4780 | ±6.9560 | +0.579 | 0.5626 |  |
| **Season: winter (vs autumn)** | **+10.1801** | 4.7771 | ±9.5542 | **+2.131** | **0.0331** | * |
| Age (years) | -0.0648 | 0.1225 | ±0.2449 | -0.529 | 0.5969 |  |
| BMI (kg/m2) | +0.1728 | 0.1869 | ±0.3739 | +0.924 | 0.3554 |  |
| Hypertension | -2.4940 | 3.3029 | ±6.6057 | -0.755 | 0.4502 |  |
| High cholesterol | +2.2766 | 3.1178 | ±6.2356 | +0.730 | 0.4653 |  |
| Kidney disease | +1.5193 | 3.7990 | ±7.5980 | +0.400 | 0.6892 |  |
| Circulatory disease | -4.2015 | 3.4987 | ±6.9973 | -1.201 | 0.2298 |  |
| Time < 70 (%) | +0.4118 | 0.3478 | ±0.6955 | +1.184 | 0.2364 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **228**, R² = **0.1087**, Adj R² = **0.0501**, F-statistic = **1.85** (p = **0.0328**), Residual SE = **19.098** on **213** df, AIC = **2006.5**, BIC = **2058.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.9584** | 13.2575 | ±26.5150 | **+9.425** | **4.28e-21** | *** |
| **Education: graduate level (vs college)** | **-9.1094** | 3.0124 | ±6.0249 | **-3.024** | **0.0025** | ** |
| Education: high school or below (vs college) | +1.2554 | 3.9198 | ±7.8395 | +0.320 | 0.7488 |  |
| Site: UCSD (vs UAB) | +1.9443 | 3.5182 | ±7.0364 | +0.553 | 0.5805 |  |
| Site: UW (vs UAB) | +0.6143 | 3.0267 | ±6.0535 | +0.203 | 0.8392 |  |
| Season: spring (vs autumn) | +3.3661 | 3.4528 | ±6.9057 | +0.975 | 0.3296 |  |
| Season: summer (vs autumn) | +1.9699 | 3.4826 | ±6.9652 | +0.566 | 0.5716 |  |
| **Season: winter (vs autumn)** | **+10.1374** | 4.7816 | ±9.5632 | **+2.120** | **0.0340** | * |
| Age (years) | -0.0669 | 0.1222 | ±0.2444 | -0.548 | 0.5840 |  |
| BMI (kg/m2) | +0.1725 | 0.1858 | ±0.3715 | +0.928 | 0.3532 |  |
| Hypertension | -2.4841 | 3.2976 | ±6.5952 | -0.753 | 0.4513 |  |
| High cholesterol | +2.3332 | 3.1118 | ±6.2237 | +0.750 | 0.4534 |  |
| Kidney disease | +1.5135 | 3.8006 | ±7.6013 | +0.398 | 0.6905 |  |
| Circulatory disease | -4.1651 | 3.4980 | ±6.9961 | -1.191 | 0.2338 |  |
| Avg. daily time < 70 (%) | +0.3606 | 0.3130 | ±0.6261 | +1.152 | 0.2493 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.1263**, Adj R² = **0.0688**, F-statistic = **2.20** (p = **0.0088**), Residual SE = **18.909** on **213** df, AIC = **2002.0**, BIC = **2053.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+95.3096** | 32.6024 | ±65.2048 | **+2.923** | **0.0035** | ** |
| **Education: graduate level (vs college)** | **-10.0465** | 2.9335 | ±5.8669 | **-3.425** | **6.15e-04** | *** |
| Education: high school or below (vs college) | +2.0948 | 4.0905 | ±8.1809 | +0.512 | 0.6086 |  |
| Site: UCSD (vs UAB) | +1.5564 | 3.5525 | ±7.1050 | +0.438 | 0.6613 |  |
| Site: UW (vs UAB) | -0.2513 | 3.0458 | ±6.0917 | -0.083 | 0.9342 |  |
| Season: spring (vs autumn) | +3.4866 | 3.3822 | ±6.7644 | +1.031 | 0.3026 |  |
| Season: summer (vs autumn) | +1.1342 | 3.4454 | ±6.8909 | +0.329 | 0.7420 |  |
| **Season: winter (vs autumn)** | **+10.3328** | 4.7188 | ±9.4377 | **+2.190** | **0.0285** | * |
| Age (years) | -0.0586 | 0.1257 | ±0.2514 | -0.466 | 0.6412 |  |
| BMI (kg/m2) | +0.1507 | 0.1777 | ±0.3554 | +0.848 | 0.3963 |  |
| Hypertension | -2.2585 | 3.3432 | ±6.6863 | -0.676 | 0.4993 |  |
| High cholesterol | +1.9715 | 3.0741 | ±6.1482 | +0.641 | 0.5213 |  |
| Kidney disease | +2.1416 | 3.7730 | ±7.5461 | +0.568 | 0.5703 |  |
| Circulatory disease | -3.6836 | 3.3509 | ±6.7017 | -1.099 | 0.2716 |  |
| Time 54-250, pooled (%) | +0.3217 | 0.2829 | ±0.5658 | +1.137 | 0.2556 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **228**, R² = **0.1296**, Adj R² = **0.0724**, F-statistic = **2.27** (p = **0.0067**), Residual SE = **18.872** on **213** df, AIC = **2001.1**, BIC = **2052.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+88.9074** | 36.3101 | ±72.6202 | **+2.449** | **0.0143** | * |
| **Education: graduate level (vs college)** | **-10.1401** | 2.9366 | ±5.8733 | **-3.453** | **5.54e-04** | *** |
| Education: high school or below (vs college) | +2.3103 | 4.0953 | ±8.1905 | +0.564 | 0.5727 |  |
| Site: UCSD (vs UAB) | +1.5999 | 3.5357 | ±7.0715 | +0.453 | 0.6509 |  |
| Site: UW (vs UAB) | -0.2083 | 3.0342 | ±6.0683 | -0.069 | 0.9453 |  |
| Season: spring (vs autumn) | +3.7300 | 3.3891 | ±6.7782 | +1.101 | 0.2711 |  |
| Season: summer (vs autumn) | +1.2050 | 3.4285 | ±6.8569 | +0.351 | 0.7252 |  |
| **Season: winter (vs autumn)** | **+10.5950** | 4.6622 | ±9.3244 | **+2.273** | **0.0231** | * |
| Age (years) | -0.0547 | 0.1270 | ±0.2541 | -0.431 | 0.6666 |  |
| BMI (kg/m2) | +0.1422 | 0.1762 | ±0.3525 | +0.807 | 0.4198 |  |
| Hypertension | -2.2182 | 3.3426 | ±6.6852 | -0.664 | 0.5069 |  |
| High cholesterol | +1.9280 | 3.0690 | ±6.1380 | +0.628 | 0.5299 |  |
| Kidney disease | +2.3660 | 3.7552 | ±7.5104 | +0.630 | 0.5287 |  |
| Circulatory disease | -3.5219 | 3.3262 | ±6.6524 | -1.059 | 0.2897 |  |
| Avg. daily time 54-250 (%) | +0.3848 | 0.3200 | ±0.6400 | +1.203 | 0.2291 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.1068**, Adj R² = **0.0481**, F-statistic = **1.82** (p = **0.0373**), Residual SE = **19.118** on **213** df, AIC = **2007.0**, BIC = **2058.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.7205** | 13.0508 | ±26.1016 | **+9.557** | **1.22e-21** | *** |
| **Education: graduate level (vs college)** | **-9.3231** | 2.8462 | ±5.6924 | **-3.276** | **0.0011** | ** |
| Education: high school or below (vs college) | +1.2405 | 3.9743 | ±7.9486 | +0.312 | 0.7549 |  |
| Site: UCSD (vs UAB) | +1.7274 | 3.5415 | ±7.0830 | +0.488 | 0.6257 |  |
| Site: UW (vs UAB) | +0.4032 | 2.9787 | ±5.9574 | +0.135 | 0.8923 |  |
| Season: spring (vs autumn) | +2.8472 | 3.5516 | ±7.1033 | +0.802 | 0.4228 |  |
| Season: summer (vs autumn) | +1.8096 | 3.5175 | ±7.0349 | +0.514 | 0.6069 |  |
| **Season: winter (vs autumn)** | **+9.7236** | 4.5163 | ±9.0326 | **+2.153** | **0.0313** | * |
| Age (years) | -0.0563 | 0.1385 | ±0.2769 | -0.407 | 0.6842 |  |
| BMI (kg/m2) | +0.1752 | 0.1826 | ±0.3652 | +0.959 | 0.3374 |  |
| Hypertension | -2.5429 | 3.3151 | ±6.6303 | -0.767 | 0.4430 |  |
| High cholesterol | +2.3791 | 3.1086 | ±6.2172 | +0.765 | 0.4441 |  |
| Kidney disease | +1.1862 | 3.9400 | ±7.8800 | +0.301 | 0.7634 |  |
| Circulatory disease | -4.1870 | 3.5457 | ±7.0914 | -1.181 | 0.2377 |  |
| Time 181-250, pooled (%) | +0.0632 | 0.1898 | ±0.3797 | +0.333 | 0.7391 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **228**, R² = **0.1060**, Adj R² = **0.0472**, F-statistic = **1.80** (p = **0.0396**), Residual SE = **19.127** on **213** df, AIC = **2007.2**, BIC = **2058.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.7445** | 12.9026 | ±25.8052 | **+9.668** | **4.12e-22** | *** |
| **Education: graduate level (vs college)** | **-9.3821** | 2.8553 | ±5.7106 | **-3.286** | **0.0010** | ** |
| Education: high school or below (vs college) | +1.2672 | 3.9768 | ±7.9537 | +0.319 | 0.7500 |  |
| Site: UCSD (vs UAB) | +1.7383 | 3.5356 | ±7.0712 | +0.492 | 0.6230 |  |
| Site: UW (vs UAB) | +0.4288 | 2.9528 | ±5.9055 | +0.145 | 0.8845 |  |
| Season: spring (vs autumn) | +2.9324 | 3.5315 | ±7.0630 | +0.830 | 0.4063 |  |
| Season: summer (vs autumn) | +1.8522 | 3.5146 | ±7.0292 | +0.527 | 0.5982 |  |
| **Season: winter (vs autumn)** | **+9.8486** | 4.5350 | ±9.0701 | **+2.172** | **0.0299** | * |
| Age (years) | -0.0532 | 0.1354 | ±0.2708 | -0.393 | 0.6943 |  |
| BMI (kg/m2) | +0.1741 | 0.1823 | ±0.3647 | +0.955 | 0.3396 |  |
| Hypertension | -2.5503 | 3.3135 | ±6.6270 | -0.770 | 0.4415 |  |
| High cholesterol | +2.4038 | 3.1185 | ±6.2371 | +0.771 | 0.4408 |  |
| Kidney disease | +1.3350 | 3.9089 | ±7.8178 | +0.342 | 0.7327 |  |
| Circulatory disease | -4.1579 | 3.5394 | ±7.0787 | -1.175 | 0.2401 |  |
| Avg. daily time 181-250 (%) | +0.0388 | 0.1777 | ±0.3553 | +0.218 | 0.8271 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **228**, R² = **0.1077**, Adj R² = **0.0491**, F-statistic = **1.84** (p = **0.0350**), Residual SE = **19.108** on **213** df, AIC = **2006.8**, BIC = **2058.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.5730** | 12.8826 | ±25.7652 | **+9.747** | **1.89e-22** | *** |
| **Education: graduate level (vs college)** | **-9.6926** | 2.8505 | ±5.7010 | **-3.400** | **6.73e-04** | *** |
| Education: high school or below (vs college) | +1.5321 | 4.0718 | ±8.1437 | +0.376 | 0.7067 |  |
| Site: UCSD (vs UAB) | +1.6959 | 3.5697 | ±7.1394 | +0.475 | 0.6347 |  |
| Site: UW (vs UAB) | +0.3232 | 2.9550 | ±5.9100 | +0.109 | 0.9129 |  |
| Season: spring (vs autumn) | +3.3104 | 3.4686 | ±6.9372 | +0.954 | 0.3399 |  |
| Season: summer (vs autumn) | +1.8453 | 3.4849 | ±6.9698 | +0.530 | 0.5965 |  |
| **Season: winter (vs autumn)** | **+10.3717** | 4.5457 | ±9.0915 | **+2.282** | **0.0225** | * |
| Age (years) | -0.0466 | 0.1328 | ±0.2656 | -0.351 | 0.7256 |  |
| BMI (kg/m2) | +0.1655 | 0.1794 | ±0.3587 | +0.922 | 0.3563 |  |
| Hypertension | -2.5558 | 3.3857 | ±6.7715 | -0.755 | 0.4503 |  |
| High cholesterol | +2.4095 | 3.1740 | ±6.3479 | +0.759 | 0.4478 |  |
| Kidney disease | +2.0091 | 3.8421 | ±7.6842 | +0.523 | 0.6010 |  |
| Circulatory disease | -4.0014 | 3.4868 | ±6.9737 | -1.148 | 0.2511 |  |
| Time > 180 (%) | -0.0534 | 0.1268 | ±0.2536 | -0.421 | 0.6737 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **228**, R² = **0.1085**, Adj R² = **0.0500**, F-statistic = **1.85** (p = **0.0331**), Residual SE = **19.100** on **213** df, AIC = **2006.6**, BIC = **2058.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7103** | 12.8646 | ±25.7292 | **+9.772** | **1.49e-22** | *** |
| **Education: graduate level (vs college)** | **-9.7220** | 2.8582 | ±5.7164 | **-3.401** | **6.70e-04** | *** |
| Education: high school or below (vs college) | +1.5871 | 4.0765 | ±8.1531 | +0.389 | 0.6970 |  |
| Site: UCSD (vs UAB) | +1.6794 | 3.5709 | ±7.1418 | +0.470 | 0.6381 |  |
| Site: UW (vs UAB) | +0.2966 | 2.9507 | ±5.9015 | +0.101 | 0.9199 |  |
| Season: spring (vs autumn) | +3.3747 | 3.4847 | ±6.9694 | +0.968 | 0.3328 |  |
| Season: summer (vs autumn) | +1.8579 | 3.4912 | ±6.9825 | +0.532 | 0.5946 |  |
| **Season: winter (vs autumn)** | **+10.4581** | 4.5337 | ±9.0674 | **+2.307** | **0.0211** | * |
| Age (years) | -0.0466 | 0.1324 | ±0.2648 | -0.352 | 0.7250 |  |
| BMI (kg/m2) | +0.1634 | 0.1786 | ±0.3571 | +0.915 | 0.3601 |  |
| Hypertension | -2.5638 | 3.3852 | ±6.7703 | -0.757 | 0.4488 |  |
| High cholesterol | +2.4137 | 3.1711 | ±6.3422 | +0.761 | 0.4466 |  |
| Kidney disease | +2.1005 | 3.8270 | ±7.6541 | +0.549 | 0.5831 |  |
| Circulatory disease | -3.9749 | 3.4825 | ±6.9650 | -1.141 | 0.2537 |  |
| Avg. daily time > 180 (%) | -0.0623 | 0.1284 | ±0.2567 | -0.485 | 0.6274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **228**, R² = **0.1116**, Adj R² = **0.0532**, F-statistic = **1.91** (p = **0.0267**), Residual SE = **19.067** on **213** df, AIC = **2005.8**, BIC = **2057.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.9274** | 13.0102 | ±26.0204 | **+9.679** | **3.70e-22** | *** |
| **Education: graduate level (vs college)** | **-9.7875** | 2.8427 | ±5.6855 | **-3.443** | **5.75e-04** | *** |
| Education: high school or below (vs college) | +1.5154 | 4.0173 | ±8.0345 | +0.377 | 0.7060 |  |
| Site: UCSD (vs UAB) | +1.6526 | 3.6178 | ±7.2356 | +0.457 | 0.6478 |  |
| Site: UW (vs UAB) | +0.2710 | 2.9609 | ±5.9219 | +0.092 | 0.9271 |  |
| Season: spring (vs autumn) | +3.3962 | 3.4614 | ±6.9227 | +0.981 | 0.3265 |  |
| Season: summer (vs autumn) | +1.6230 | 3.4555 | ±6.9111 | +0.470 | 0.6386 |  |
| **Season: winter (vs autumn)** | **+10.5489** | 4.5404 | ±9.0808 | **+2.323** | **0.0202** | * |
| Age (years) | -0.0524 | 0.1283 | ±0.2565 | -0.409 | 0.6827 |  |
| BMI (kg/m2) | +0.1646 | 0.1820 | ±0.3641 | +0.904 | 0.3658 |  |
| Hypertension | -2.3843 | 3.4703 | ±6.9406 | -0.687 | 0.4920 |  |
| High cholesterol | +2.4992 | 3.1787 | ±6.3574 | +0.786 | 0.4317 |  |
| Kidney disease | +1.8574 | 3.7453 | ±7.4907 | +0.496 | 0.6199 |  |
| Circulatory disease | -3.8314 | 3.4371 | ±6.8742 | -1.115 | 0.2650 |  |
| Nocturnal time > 180 (%) | -0.0875 | 0.1545 | ±0.3090 | -0.566 | 0.5713 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.1094**, Adj R² = **0.0509**, F-statistic = **1.87** (p = **0.0312**), Residual SE = **19.091** on **213** df, AIC = **2006.4**, BIC = **2057.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.3128** | 12.8941 | ±25.7883 | **+9.641** | **5.36e-22** | *** |
| **Education: graduate level (vs college)** | **-9.1590** | 2.9271 | ±5.8542 | **-3.129** | **0.0018** | ** |
| Education: high school or below (vs college) | +1.0558 | 3.9112 | ±7.8224 | +0.270 | 0.7872 |  |
| Site: UCSD (vs UAB) | +1.7470 | 3.5158 | ±7.0317 | +0.497 | 0.6193 |  |
| Site: UW (vs UAB) | +0.1968 | 3.0257 | ±6.0513 | +0.065 | 0.9481 |  |
| Season: spring (vs autumn) | +2.8239 | 3.4864 | ±6.9728 | +0.810 | 0.4179 |  |
| Season: summer (vs autumn) | +1.7148 | 3.4991 | ±6.9983 | +0.490 | 0.6241 |  |
| **Season: winter (vs autumn)** | **+9.9989** | 4.8063 | ±9.6126 | **+2.080** | **0.0375** | * |
| Age (years) | -0.0700 | 0.1348 | ±0.2696 | -0.519 | 0.6037 |  |
| BMI (kg/m2) | +0.1915 | 0.1780 | ±0.3559 | +1.076 | 0.2818 |  |
| Hypertension | -2.6195 | 3.3040 | ±6.6080 | -0.793 | 0.4279 |  |
| High cholesterol | +2.5529 | 3.1452 | ±6.2904 | +0.812 | 0.4170 |  |
| Kidney disease | +0.8939 | 3.8302 | ±7.6604 | +0.233 | 0.8155 |  |
| Circulatory disease | -4.1835 | 3.5225 | ±7.0451 | -1.188 | 0.2350 |  |
| Any reading > 250 during wear (0/1) | +2.6199 | 2.9014 | ±5.8027 | +0.903 | 0.3665 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **228**, R² = **0.1275**, Adj R² = **0.0702**, F-statistic = **2.22** (p = **0.0080**), Residual SE = **18.895** on **213** df, AIC = **2001.7**, BIC = **2053.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.4395** | 13.0547 | ±26.1093 | **+9.762** | **1.64e-22** | *** |
| **Education: graduate level (vs college)** | **-10.0370** | 2.9333 | ±5.8666 | **-3.422** | **6.22e-04** | *** |
| Education: high school or below (vs college) | +2.1700 | 4.0975 | ±8.1950 | +0.530 | 0.5964 |  |
| Site: UCSD (vs UAB) | +1.6352 | 3.5244 | ±7.0487 | +0.464 | 0.6427 |  |
| Site: UW (vs UAB) | -0.1738 | 3.0296 | ±6.0592 | -0.057 | 0.9542 |  |
| Season: spring (vs autumn) | +3.5473 | 3.3864 | ±6.7727 | +1.048 | 0.2949 |  |
| Season: summer (vs autumn) | +1.1171 | 3.4391 | ±6.8782 | +0.325 | 0.7453 |  |
| **Season: winter (vs autumn)** | **+10.3588** | 4.7100 | ±9.4199 | **+2.199** | **0.0279** | * |
| Age (years) | -0.0595 | 0.1257 | ±0.2514 | -0.474 | 0.6357 |  |
| BMI (kg/m2) | +0.1493 | 0.1776 | ±0.3552 | +0.841 | 0.4006 |  |
| Hypertension | -2.2584 | 3.3487 | ±6.6973 | -0.674 | 0.5000 |  |
| High cholesterol | +1.9408 | 3.0778 | ±6.1556 | +0.631 | 0.5283 |  |
| Kidney disease | +2.1809 | 3.7721 | ±7.5442 | +0.578 | 0.5631 |  |
| Circulatory disease | -3.7169 | 3.3515 | ±6.7030 | -1.109 | 0.2674 |  |
| Time > 250 (%) | -0.3334 | 0.2874 | ±0.5749 | -1.160 | 0.2461 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 228)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **228**, R² = **0.1321**, Adj R² = **0.0751**, F-statistic = **2.32** (p = **0.0055**), Residual SE = **18.846** on **213** df, AIC = **2000.5**, BIC = **2051.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.4828** | 13.0901 | ±26.1802 | **+9.739** | **2.06e-22** | *** |
| **Education: graduate level (vs college)** | **-10.1228** | 2.9369 | ±5.8738 | **-3.447** | **5.67e-04** | *** |
| Education: high school or below (vs college) | +2.4316 | 4.1102 | ±8.2204 | +0.592 | 0.5541 |  |
| Site: UCSD (vs UAB) | +1.6876 | 3.5049 | ±7.0099 | +0.481 | 0.6302 |  |
| Site: UW (vs UAB) | -0.1454 | 3.0216 | ±6.0432 | -0.048 | 0.9616 |  |
| Season: spring (vs autumn) | +3.8513 | 3.3975 | ±6.7950 | +1.134 | 0.2570 |  |
| Season: summer (vs autumn) | +1.1734 | 3.4181 | ±6.8362 | +0.343 | 0.7314 |  |
| **Season: winter (vs autumn)** | **+10.6377** | 4.6488 | ±9.2976 | **+2.288** | **0.0221** | * |
| Age (years) | -0.0574 | 0.1267 | ±0.2535 | -0.453 | 0.6505 |  |
| BMI (kg/m2) | +0.1400 | 0.1759 | ±0.3518 | +0.796 | 0.4259 |  |
| Hypertension | -2.1981 | 3.3473 | ±6.6946 | -0.657 | 0.5114 |  |
| High cholesterol | +1.9051 | 3.0718 | ±6.1436 | +0.620 | 0.5351 |  |
| Kidney disease | +2.4105 | 3.7505 | ±7.5010 | +0.643 | 0.5204 |  |
| Circulatory disease | -3.5428 | 3.3208 | ±6.6417 | -1.067 | 0.2860 |  |
| Avg. daily time > 250 (%) | -0.4090 | 0.3297 | ±0.6595 | -1.240 | 0.2148 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Non-healthy group (T2D non-insulin + T2D insulin) - Home environment

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 120 single-predictor tests; 5 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 228): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.026 vs -0.001 for covariates alone, gain +0.027; +0.23 per SD, p = 0.016). Raw p < 0.05 (FDR not applicable here): %<70 (pooled) (p = 0.014), %<70 (daily avg) (p = 0.016), %54-69 (daily avg) (p = 0.023), %54-69 (pooled) (p = 0.026), %<54 (pooled) (p = 0.028).
- **Indoor temperature, mean (deg C)** (n = 228): best single predictor out of sample is **%181-250 (pooled)** (CV R² 0.192 vs 0.188 for covariates alone, gain +0.004; -0.206 per SD, p = 0.152). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Indoor relative humidity, mean (%)** (n = 228): best single predictor out of sample is **SD (daily avg)** (CV R² -0.000 vs -0.000 for covariates alone, gain -0.000; +0.54 per SD, p = 0.226). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor VOC index, mean** (n = 228): best single predictor out of sample is **Any >250 (0/1)** (CV R² -0.059 vs -0.056 for covariates alone, gain -0.002; +1.31 per SD, p = 0.367). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.

**Most predictable outcomes (largest out-of-sample gain over covariates):** Indoor PM2.5, log(1 + mean ug/m3) (+0.027, via %<70 (daily avg)); Indoor temperature, mean (deg C) (+0.004, via %181-250 (pooled)); Indoor relative humidity, mean (%) (-0.000, via SD (daily avg)); Indoor VOC index, mean (-0.002, via Any >250 (0/1)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band 54-69 (0 FDR-significant / 2 raw-significant of 8); Band < 70 (0 FDR-significant / 2 raw-significant of 8); Band < 54 (0 FDR-significant / 1 raw-significant of 8).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (0 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Indoor PM2.5, log(1 + mean ug/m3) (%<70 (daily avg), ΔAIC -6.8); Indoor temperature, mean (%54-69 (daily avg), ΔAIC -2.5); Indoor VOC index, mean (SD of daily means, ΔAIC -5.9).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
