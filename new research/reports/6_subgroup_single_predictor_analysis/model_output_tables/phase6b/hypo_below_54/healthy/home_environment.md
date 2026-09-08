# Phase 6b model output tables - Hypoglycaemia exposure: at least one reading < 54 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Home environment

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 400; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **400**, R² = **0.1761**, Adj R² = **0.1484**, F-statistic = **6.35** (p = **6.68e-11**), Residual SE = **0.933** on **386** df, AIC = **1093.8**, BIC = **1149.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8890** | 0.3852 | ±0.7705 | **+7.499** | **6.42e-14** | *** |
| Education: graduate level (vs college) | -0.0911 | 0.0947 | ±0.1893 | -0.962 | 0.3359 |  |
| **Education: high school or below (vs college)** | **+0.7685** | 0.3301 | ±0.6602 | **+2.328** | **0.0199** | * |
| Site: UCSD (vs UAB) | +0.0428 | 0.1414 | ±0.2829 | +0.303 | 0.7620 |  |
| **Site: UW (vs UAB)** | **-0.3886** | 0.1168 | ±0.2337 | **-3.326** | **8.81e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3775** | 0.1283 | ±0.2566 | **-2.943** | **0.0033** | ** |
| Season: summer (vs autumn) | -0.2246 | 0.1497 | ±0.2994 | -1.501 | 0.1335 |  |
| Season: winter (vs autumn) | -0.0570 | 0.1432 | ±0.2865 | -0.398 | 0.6906 |  |
| **Age (years)** | **-0.0182** | 0.0047 | ±0.0095 | **-3.828** | **1.29e-04** | *** |
| BMI (kg/m2) | +0.0104 | 0.0075 | ±0.0149 | +1.393 | 0.1637 |  |
| Hypertension | +0.0920 | 0.1172 | ±0.2344 | +0.785 | 0.4324 |  |
| High cholesterol | -0.0664 | 0.1010 | ±0.2019 | -0.657 | 0.5109 |  |
| Kidney disease | -0.0066 | 0.1696 | ±0.3393 | -0.039 | 0.9688 |  |
| Circulatory disease | +0.0820 | 0.1689 | ±0.3379 | +0.485 | 0.6274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **400**, R² = **0.1763**, Adj R² = **0.1464**, F-statistic = **5.89** (p = **1.67e-10**), Residual SE = **0.935** on **385** df, AIC = **1095.7**, BIC = **1155.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.7066** | 0.7362 | ±1.4724 | **+3.676** | **2.37e-04** | *** |
| Education: graduate level (vs college) | -0.0900 | 0.0946 | ±0.1893 | -0.951 | 0.3415 |  |
| **Education: high school or below (vs college)** | **+0.7634** | 0.3322 | ±0.6643 | **+2.298** | **0.0216** | * |
| Site: UCSD (vs UAB) | +0.0374 | 0.1388 | ±0.2776 | +0.269 | 0.7877 |  |
| **Site: UW (vs UAB)** | **-0.3900** | 0.1171 | ±0.2343 | **-3.329** | **8.71e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3721** | 0.1317 | ±0.2635 | **-2.825** | **0.0047** | ** |
| Season: summer (vs autumn) | -0.2238 | 0.1506 | ±0.3011 | -1.486 | 0.1372 |  |
| Season: winter (vs autumn) | -0.0547 | 0.1447 | ±0.2894 | -0.378 | 0.7056 |  |
| **Age (years)** | **-0.0184** | 0.0048 | ±0.0095 | **-3.871** | **1.08e-04** | *** |
| BMI (kg/m2) | +0.0101 | 0.0077 | ±0.0153 | +1.311 | 0.1897 |  |
| Hypertension | +0.0925 | 0.1177 | ±0.2355 | +0.786 | 0.4321 |  |
| High cholesterol | -0.0714 | 0.1027 | ±0.2054 | -0.695 | 0.4868 |  |
| Kidney disease | -0.0085 | 0.1704 | ±0.3408 | -0.050 | 0.9603 |  |
| Circulatory disease | +0.0841 | 0.1688 | ±0.3377 | +0.498 | 0.6186 |  |
| HbA1c (%) | +0.0368 | 0.1228 | ±0.2457 | +0.299 | 0.7648 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **400**, R² = **0.1882**, Adj R² = **0.1587**, F-statistic = **6.38** (p = **1.49e-11**), Residual SE = **0.928** on **385** df, AIC = **1089.9**, BIC = **1149.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7487** | 0.5552 | ±1.1103 | **+6.752** | **1.45e-11** | *** |
| Education: graduate level (vs college) | -0.0756 | 0.0939 | ±0.1878 | -0.805 | 0.4207 |  |
| **Education: high school or below (vs college)** | **+0.7994** | 0.3295 | ±0.6590 | **+2.426** | **0.0153** | * |
| Site: UCSD (vs UAB) | +0.0501 | 0.1416 | ±0.2831 | +0.354 | 0.7233 |  |
| **Site: UW (vs UAB)** | **-0.3609** | 0.1177 | ±0.2355 | **-3.065** | **0.0022** | ** |
| **Season: spring (vs autumn)** | **-0.3979** | 0.1286 | ±0.2572 | **-3.094** | **0.0020** | ** |
| Season: summer (vs autumn) | -0.2451 | 0.1524 | ±0.3048 | -1.608 | 0.1078 |  |
| Season: winter (vs autumn) | -0.0970 | 0.1460 | ±0.2919 | -0.665 | 0.5063 |  |
| **Age (years)** | **-0.0174** | 0.0048 | ±0.0096 | **-3.619** | **2.96e-04** | *** |
| BMI (kg/m2) | +0.0110 | 0.0074 | ±0.0148 | +1.495 | 0.1349 |  |
| Hypertension | +0.1175 | 0.1180 | ±0.2360 | +0.996 | 0.3192 |  |
| High cholesterol | -0.0407 | 0.1016 | ±0.2032 | -0.400 | 0.6888 |  |
| Kidney disease | +0.0410 | 0.1702 | ±0.3404 | +0.241 | 0.8095 |  |
| Circulatory disease | +0.0752 | 0.1682 | ±0.3364 | +0.447 | 0.6550 |  |
| **Mean glucose (mg/dL)** | **-0.0083** | 0.0036 | ±0.0071 | **-2.322** | **0.0202** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **400**, R² = **0.1882**, Adj R² = **0.1587**, F-statistic = **6.38** (p = **1.49e-11**), Residual SE = **0.928** on **385** df, AIC = **1089.9**, BIC = **1149.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+4.8916** | 0.9707 | ±1.9415 | **+5.039** | **4.68e-07** | *** |
| Education: graduate level (vs college) | -0.0756 | 0.0939 | ±0.1878 | -0.805 | 0.4207 |  |
| **Education: high school or below (vs college)** | **+0.7994** | 0.3295 | ±0.6590 | **+2.426** | **0.0153** | * |
| Site: UCSD (vs UAB) | +0.0501 | 0.1416 | ±0.2831 | +0.354 | 0.7233 |  |
| **Site: UW (vs UAB)** | **-0.3609** | 0.1177 | ±0.2355 | **-3.065** | **0.0022** | ** |
| **Season: spring (vs autumn)** | **-0.3979** | 0.1286 | ±0.2572 | **-3.094** | **0.0020** | ** |
| Season: summer (vs autumn) | -0.2451 | 0.1524 | ±0.3048 | -1.608 | 0.1078 |  |
| Season: winter (vs autumn) | -0.0970 | 0.1460 | ±0.2919 | -0.665 | 0.5063 |  |
| **Age (years)** | **-0.0174** | 0.0048 | ±0.0096 | **-3.619** | **2.96e-04** | *** |
| BMI (kg/m2) | +0.0110 | 0.0074 | ±0.0148 | +1.495 | 0.1349 |  |
| Hypertension | +0.1175 | 0.1180 | ±0.2360 | +0.996 | 0.3192 |  |
| High cholesterol | -0.0407 | 0.1016 | ±0.2032 | -0.400 | 0.6888 |  |
| Kidney disease | +0.0410 | 0.1702 | ±0.3404 | +0.241 | 0.8095 |  |
| Circulatory disease | +0.0752 | 0.1682 | ±0.3364 | +0.447 | 0.6550 |  |
| **GMI (%)** | **-0.3453** | 0.1487 | ±0.2974 | **-2.322** | **0.0202** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **400**, R² = **0.1823**, Adj R² = **0.1526**, F-statistic = **6.13** (p = **5.01e-11**), Residual SE = **0.931** on **385** df, AIC = **1092.8**, BIC = **1152.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4398** | 0.5390 | ±1.0780 | **+6.382** | **1.75e-10** | *** |
| Education: graduate level (vs college) | -0.0849 | 0.0945 | ±0.1891 | -0.898 | 0.3692 |  |
| **Education: high school or below (vs college)** | **+0.7938** | 0.3314 | ±0.6627 | **+2.396** | **0.0166** | * |
| Site: UCSD (vs UAB) | +0.0528 | 0.1426 | ±0.2851 | +0.370 | 0.7111 |  |
| **Site: UW (vs UAB)** | **-0.3740** | 0.1171 | ±0.2342 | **-3.194** | **0.0014** | ** |
| **Season: spring (vs autumn)** | **-0.3852** | 0.1282 | ±0.2565 | **-3.004** | **0.0027** | ** |
| Season: summer (vs autumn) | -0.2407 | 0.1524 | ±0.3048 | -1.579 | 0.1142 |  |
| Season: winter (vs autumn) | -0.0743 | 0.1441 | ±0.2883 | -0.516 | 0.6061 |  |
| **Age (years)** | **-0.0183** | 0.0048 | ±0.0096 | **-3.802** | **1.44e-04** | *** |
| BMI (kg/m2) | +0.0120 | 0.0075 | ±0.0149 | +1.616 | 0.1060 |  |
| Hypertension | +0.1086 | 0.1189 | ±0.2379 | +0.913 | 0.3613 |  |
| High cholesterol | -0.0444 | 0.1028 | ±0.2056 | -0.432 | 0.6656 |  |
| Kidney disease | -0.0004 | 0.1689 | ±0.3379 | -0.002 | 0.9983 |  |
| Circulatory disease | +0.0711 | 0.1700 | ±0.3400 | +0.418 | 0.6758 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0054 | 0.0032 | ±0.0064 | -1.669 | 0.0952 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **400**, R² = **0.1798**, Adj R² = **0.1499**, F-statistic = **6.03** (p = **8.35e-11**), Residual SE = **0.933** on **385** df, AIC = **1094.0**, BIC = **1153.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0399** | 0.3922 | ±0.7843 | **+7.752** | **9.06e-15** | *** |
| Education: graduate level (vs college) | -0.0860 | 0.0945 | ±0.1890 | -0.910 | 0.3627 |  |
| **Education: high school or below (vs college)** | **+0.7691** | 0.3318 | ±0.6636 | **+2.318** | **0.0205** | * |
| Site: UCSD (vs UAB) | +0.0518 | 0.1416 | ±0.2833 | +0.366 | 0.7145 |  |
| **Site: UW (vs UAB)** | **-0.3848** | 0.1171 | ±0.2343 | **-3.285** | **0.0010** | ** |
| **Season: spring (vs autumn)** | **-0.3834** | 0.1282 | ±0.2564 | **-2.990** | **0.0028** | ** |
| Season: summer (vs autumn) | -0.2292 | 0.1512 | ±0.3023 | -1.517 | 0.1294 |  |
| Season: winter (vs autumn) | -0.0678 | 0.1443 | ±0.2886 | -0.470 | 0.6383 |  |
| **Age (years)** | **-0.0172** | 0.0049 | ±0.0098 | **-3.508** | **4.52e-04** | *** |
| BMI (kg/m2) | +0.0106 | 0.0075 | ±0.0150 | +1.414 | 0.1572 |  |
| Hypertension | +0.1003 | 0.1175 | ±0.2351 | +0.853 | 0.3935 |  |
| High cholesterol | -0.0709 | 0.1011 | ±0.2021 | -0.702 | 0.4826 |  |
| Kidney disease | +0.0324 | 0.1711 | ±0.3422 | +0.189 | 0.8497 |  |
| Circulatory disease | +0.0786 | 0.1682 | ±0.3363 | +0.467 | 0.6403 |  |
| Glucose SD, pooled (mg/dL) | -0.0098 | 0.0074 | ±0.0147 | -1.327 | 0.1847 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **400**, R² = **0.1793**, Adj R² = **0.1495**, F-statistic = **6.01** (p = **9.14e-11**), Residual SE = **0.933** on **385** df, AIC = **1094.3**, BIC = **1154.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0177** | 0.3920 | ±0.7840 | **+7.699** | **1.38e-14** | *** |
| Education: graduate level (vs college) | -0.0879 | 0.0946 | ±0.1891 | -0.929 | 0.3528 |  |
| **Education: high school or below (vs college)** | **+0.7736** | 0.3323 | ±0.6646 | **+2.328** | **0.0199** | * |
| Site: UCSD (vs UAB) | +0.0531 | 0.1417 | ±0.2834 | +0.375 | 0.7078 |  |
| **Site: UW (vs UAB)** | **-0.3835** | 0.1175 | ±0.2350 | **-3.263** | **0.0011** | ** |
| **Season: spring (vs autumn)** | **-0.3845** | 0.1285 | ±0.2570 | **-2.993** | **0.0028** | ** |
| Season: summer (vs autumn) | -0.2340 | 0.1526 | ±0.3052 | -1.533 | 0.1252 |  |
| Season: winter (vs autumn) | -0.0679 | 0.1446 | ±0.2891 | -0.469 | 0.6388 |  |
| **Age (years)** | **-0.0172** | 0.0050 | ±0.0099 | **-3.472** | **5.17e-04** | *** |
| BMI (kg/m2) | +0.0107 | 0.0075 | ±0.0150 | +1.422 | 0.1550 |  |
| Hypertension | +0.0988 | 0.1176 | ±0.2353 | +0.840 | 0.4010 |  |
| High cholesterol | -0.0690 | 0.1010 | ±0.2020 | -0.683 | 0.4947 |  |
| Kidney disease | +0.0328 | 0.1708 | ±0.3415 | +0.192 | 0.8476 |  |
| Circulatory disease | +0.0777 | 0.1682 | ±0.3364 | +0.462 | 0.6443 |  |
| Avg. daily SD (mg/dL) | -0.0100 | 0.0087 | ±0.0173 | -1.155 | 0.2480 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **400**, R² = **0.1766**, Adj R² = **0.1466**, F-statistic = **5.90** (p = **1.59e-10**), Residual SE = **0.934** on **385** df, AIC = **1095.6**, BIC = **1155.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9627** | 0.3908 | ±0.7815 | **+7.582** | **3.41e-14** | *** |
| Education: graduate level (vs college) | -0.0906 | 0.0948 | ±0.1896 | -0.955 | 0.3394 |  |
| **Education: high school or below (vs college)** | **+0.7658** | 0.3312 | ±0.6625 | **+2.312** | **0.0208** | * |
| Site: UCSD (vs UAB) | +0.0457 | 0.1414 | ±0.2828 | +0.323 | 0.7465 |  |
| **Site: UW (vs UAB)** | **-0.3901** | 0.1166 | ±0.2332 | **-3.345** | **8.22e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3781** | 0.1284 | ±0.2569 | **-2.943** | **0.0032** | ** |
| Season: summer (vs autumn) | -0.2245 | 0.1503 | ±0.3006 | -1.494 | 0.1352 |  |
| Season: winter (vs autumn) | -0.0571 | 0.1436 | ±0.2872 | -0.398 | 0.6910 |  |
| **Age (years)** | **-0.0179** | 0.0049 | ±0.0098 | **-3.635** | **2.78e-04** | *** |
| BMI (kg/m2) | +0.0104 | 0.0075 | ±0.0150 | +1.391 | 0.1643 |  |
| Hypertension | +0.0929 | 0.1174 | ±0.2348 | +0.791 | 0.4289 |  |
| High cholesterol | -0.0708 | 0.1021 | ±0.2042 | -0.694 | 0.4879 |  |
| Kidney disease | +0.0045 | 0.1708 | ±0.3416 | +0.026 | 0.9789 |  |
| Circulatory disease | +0.0811 | 0.1689 | ±0.3379 | +0.480 | 0.6311 |  |
| CV (%) | -0.0048 | 0.0099 | ±0.0197 | -0.488 | 0.6256 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **400**, R² = **0.1762**, Adj R² = **0.1462**, F-statistic = **5.88** (p = **1.72e-10**), Residual SE = **0.935** on **385** df, AIC = **1095.8**, BIC = **1155.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8393** | 0.5251 | ±1.0502 | **+5.407** | **6.40e-08** | *** |
| Education: graduate level (vs college) | -0.0902 | 0.0951 | ±0.1901 | -0.949 | 0.3426 |  |
| **Education: high school or below (vs college)** | **+0.7682** | 0.3309 | ±0.6619 | **+2.321** | **0.0203** | * |
| Site: UCSD (vs UAB) | +0.0441 | 0.1413 | ±0.2826 | +0.312 | 0.7550 |  |
| **Site: UW (vs UAB)** | **-0.3885** | 0.1172 | ±0.2345 | **-3.314** | **9.21e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3781** | 0.1284 | ±0.2567 | **-2.946** | **0.0032** | ** |
| Season: summer (vs autumn) | -0.2248 | 0.1502 | ±0.3003 | -1.497 | 0.1344 |  |
| Season: winter (vs autumn) | -0.0572 | 0.1436 | ±0.2872 | -0.399 | 0.6902 |  |
| **Age (years)** | **-0.0180** | 0.0050 | ±0.0100 | **-3.623** | **2.91e-04** | *** |
| BMI (kg/m2) | +0.0104 | 0.0075 | ±0.0150 | +1.389 | 0.1647 |  |
| Hypertension | +0.0923 | 0.1173 | ±0.2346 | +0.787 | 0.4314 |  |
| High cholesterol | -0.0675 | 0.1020 | ±0.2039 | -0.662 | 0.5080 |  |
| Kidney disease | -0.0029 | 0.1709 | ±0.3419 | -0.017 | 0.9865 |  |
| Circulatory disease | +0.0819 | 0.1693 | ±0.3386 | +0.484 | 0.6285 |  |
| Mean / SD ratio | +0.0075 | 0.0414 | ±0.0829 | +0.181 | 0.8565 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **400**, R² = **0.1762**, Adj R² = **0.1462**, F-statistic = **5.88** (p = **1.73e-10**), Residual SE = **0.935** on **385** df, AIC = **1095.8**, BIC = **1155.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9234** | 0.5149 | ±1.0297 | **+5.678** | **1.36e-08** | *** |
| Education: graduate level (vs college) | -0.0917 | 0.0953 | ±0.1905 | -0.963 | 0.3357 |  |
| **Education: high school or below (vs college)** | **+0.7676** | 0.3308 | ±0.6616 | **+2.321** | **0.0203** | * |
| Site: UCSD (vs UAB) | +0.0415 | 0.1416 | ±0.2832 | +0.293 | 0.7694 |  |
| **Site: UW (vs UAB)** | **-0.3889** | 0.1175 | ±0.2350 | **-3.309** | **9.35e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3775** | 0.1285 | ±0.2570 | **-2.937** | **0.0033** | ** |
| Season: summer (vs autumn) | -0.2238 | 0.1502 | ±0.3005 | -1.490 | 0.1363 |  |
| Season: winter (vs autumn) | -0.0571 | 0.1436 | ±0.2871 | -0.398 | 0.6910 |  |
| **Age (years)** | **-0.0183** | 0.0050 | ±0.0100 | **-3.668** | **2.45e-04** | *** |
| BMI (kg/m2) | +0.0103 | 0.0075 | ±0.0150 | +1.379 | 0.1679 |  |
| Hypertension | +0.0920 | 0.1174 | ±0.2348 | +0.784 | 0.4333 |  |
| High cholesterol | -0.0659 | 0.1018 | ±0.2035 | -0.647 | 0.5174 |  |
| Kidney disease | -0.0098 | 0.1707 | ±0.3414 | -0.058 | 0.9541 |  |
| Circulatory disease | +0.0823 | 0.1693 | ±0.3386 | +0.486 | 0.6271 |  |
| Avg. daily mean/SD | -0.0042 | 0.0326 | ±0.0653 | -0.128 | 0.8979 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **400**, R² = **0.1777**, Adj R² = **0.1478**, F-statistic = **5.94** (p = **1.27e-10**), Residual SE = **0.934** on **385** df, AIC = **1095.1**, BIC = **1154.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.6778** | 0.4389 | ±0.8778 | **+6.101** | **1.05e-09** | *** |
| Education: graduate level (vs college) | -0.0915 | 0.0949 | ±0.1897 | -0.965 | 0.3347 |  |
| **Education: high school or below (vs college)** | **+0.7703** | 0.3289 | ±0.6577 | **+2.342** | **0.0192** | * |
| Site: UCSD (vs UAB) | +0.0392 | 0.1421 | ±0.2841 | +0.276 | 0.7827 |  |
| **Site: UW (vs UAB)** | **-0.3781** | 0.1169 | ±0.2339 | **-3.233** | **0.0012** | ** |
| **Season: spring (vs autumn)** | **-0.3727** | 0.1278 | ±0.2556 | **-2.917** | **0.0035** | ** |
| Season: summer (vs autumn) | -0.2218 | 0.1494 | ±0.2988 | -1.485 | 0.1375 |  |
| Season: winter (vs autumn) | -0.0538 | 0.1432 | ±0.2864 | -0.376 | 0.7069 |  |
| **Age (years)** | **-0.0181** | 0.0047 | ±0.0095 | **-3.830** | **1.28e-04** | *** |
| BMI (kg/m2) | +0.0103 | 0.0074 | ±0.0148 | +1.396 | 0.1627 |  |
| Hypertension | +0.0884 | 0.1172 | ±0.2343 | +0.754 | 0.4507 |  |
| High cholesterol | -0.0573 | 0.1019 | ±0.2037 | -0.562 | 0.5738 |  |
| Kidney disease | -0.0086 | 0.1702 | ±0.3404 | -0.051 | 0.9597 |  |
| Circulatory disease | +0.0832 | 0.1691 | ±0.3381 | +0.492 | 0.6227 |  |
| MAG (mg/dL/h) | +0.0050 | 0.0058 | ±0.0116 | +0.867 | 0.3859 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **400**, R² = **0.1777**, Adj R² = **0.1478**, F-statistic = **5.94** (p = **1.27e-10**), Residual SE = **0.934** on **385** df, AIC = **1095.1**, BIC = **1154.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0182** | 0.4049 | ±0.8097 | **+7.455** | **8.99e-14** | *** |
| Education: graduate level (vs college) | -0.0906 | 0.0947 | ±0.1894 | -0.957 | 0.3386 |  |
| **Education: high school or below (vs college)** | **+0.7721** | 0.3325 | ±0.6649 | **+2.322** | **0.0202** | * |
| Site: UCSD (vs UAB) | +0.0490 | 0.1419 | ±0.2839 | +0.345 | 0.7299 |  |
| **Site: UW (vs UAB)** | **-0.3874** | 0.1173 | ±0.2347 | **-3.302** | **9.60e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3826** | 0.1286 | ±0.2572 | **-2.975** | **0.0029** | ** |
| Season: summer (vs autumn) | -0.2309 | 0.1518 | ±0.3037 | -1.521 | 0.1283 |  |
| Season: winter (vs autumn) | -0.0623 | 0.1443 | ±0.2886 | -0.432 | 0.6660 |  |
| **Age (years)** | **-0.0176** | 0.0049 | ±0.0098 | **-3.569** | **3.58e-04** | *** |
| BMI (kg/m2) | +0.0101 | 0.0075 | ±0.0150 | +1.353 | 0.1761 |  |
| Hypertension | +0.0951 | 0.1175 | ±0.2351 | +0.809 | 0.4186 |  |
| High cholesterol | -0.0712 | 0.1015 | ±0.2030 | -0.702 | 0.4828 |  |
| Kidney disease | +0.0147 | 0.1695 | ±0.3389 | +0.087 | 0.9309 |  |
| Circulatory disease | +0.0796 | 0.1685 | ±0.3371 | +0.472 | 0.6366 |  |
| Avg. daily range (mg/dL) | -0.0015 | 0.0020 | ±0.0040 | -0.760 | 0.4470 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **400**, R² = **0.1785**, Adj R² = **0.1486**, F-statistic = **5.97** (p = **1.08e-10**), Residual SE = **0.933** on **385** df, AIC = **1094.7**, BIC = **1154.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9559** | 0.3864 | ±0.7728 | **+7.650** | **2.01e-14** | *** |
| Education: graduate level (vs college) | -0.0841 | 0.0946 | ±0.1891 | -0.890 | 0.3735 |  |
| **Education: high school or below (vs college)** | **+0.7554** | 0.3325 | ±0.6649 | **+2.272** | **0.0231** | * |
| Site: UCSD (vs UAB) | +0.0405 | 0.1420 | ±0.2839 | +0.285 | 0.7754 |  |
| **Site: UW (vs UAB)** | **-0.3889** | 0.1167 | ±0.2335 | **-3.331** | **8.65e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3725** | 0.1291 | ±0.2582 | **-2.885** | **0.0039** | ** |
| Season: summer (vs autumn) | -0.2185 | 0.1503 | ±0.3006 | -1.454 | 0.1460 |  |
| Season: winter (vs autumn) | -0.0618 | 0.1434 | ±0.2867 | -0.431 | 0.6663 |  |
| **Age (years)** | **-0.0180** | 0.0048 | ±0.0095 | **-3.776** | **1.59e-04** | *** |
| BMI (kg/m2) | +0.0109 | 0.0075 | ±0.0151 | +1.450 | 0.1470 |  |
| Hypertension | +0.0933 | 0.1176 | ±0.2351 | +0.793 | 0.4277 |  |
| High cholesterol | -0.0652 | 0.1009 | ±0.2018 | -0.646 | 0.5183 |  |
| Kidney disease | +0.0003 | 0.1707 | ±0.3414 | +0.002 | 0.9985 |  |
| Circulatory disease | +0.0836 | 0.1691 | ±0.3382 | +0.494 | 0.6210 |  |
| SD of daily means (mg/dL) | -0.0131 | 0.0101 | ±0.0203 | -1.290 | 0.1969 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **400**, R² = **0.1828**, Adj R² = **0.1530**, F-statistic = **6.15** (p = **4.55e-11**), Residual SE = **0.931** on **385** df, AIC = **1092.6**, BIC = **1152.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.3020 | 0.8377 | ±1.6754 | +1.554 | 0.1201 |  |
| Education: graduate level (vs college) | -0.0911 | 0.0943 | ±0.1887 | -0.965 | 0.3344 |  |
| **Education: high school or below (vs college)** | **+0.7654** | 0.3321 | ±0.6641 | **+2.305** | **0.0212** | * |
| Site: UCSD (vs UAB) | +0.0322 | 0.1422 | ±0.2845 | +0.226 | 0.8212 |  |
| **Site: UW (vs UAB)** | **-0.3985** | 0.1164 | ±0.2329 | **-3.423** | **6.20e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3950** | 0.1283 | ±0.2566 | **-3.078** | **0.0021** | ** |
| Season: summer (vs autumn) | -0.2399 | 0.1501 | ±0.3002 | -1.598 | 0.1099 |  |
| Season: winter (vs autumn) | -0.0734 | 0.1438 | ±0.2877 | -0.511 | 0.6097 |  |
| **Age (years)** | **-0.0175** | 0.0048 | ±0.0096 | **-3.652** | **2.60e-04** | *** |
| BMI (kg/m2) | +0.0106 | 0.0074 | ±0.0149 | +1.425 | 0.1540 |  |
| Hypertension | +0.0953 | 0.1172 | ±0.2345 | +0.813 | 0.4163 |  |
| High cholesterol | -0.0716 | 0.1008 | ±0.2016 | -0.711 | 0.4773 |  |
| Kidney disease | +0.0464 | 0.1703 | ±0.3405 | +0.272 | 0.7854 |  |
| Circulatory disease | +0.0670 | 0.1669 | ±0.3338 | +0.402 | 0.6880 |  |
| **Time in range 70-180, pooled (%)** | **+0.0163** | 0.0075 | ±0.0150 | **+2.174** | **0.0297** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **400**, R² = **0.1823**, Adj R² = **0.1525**, F-statistic = **6.13** (p = **5.04e-11**), Residual SE = **0.931** on **385** df, AIC = **1092.8**, BIC = **1152.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.3980 | 0.8554 | ±1.7108 | +1.634 | 0.1022 |  |
| Education: graduate level (vs college) | -0.0921 | 0.0943 | ±0.1887 | -0.977 | 0.3287 |  |
| **Education: high school or below (vs college)** | **+0.7632** | 0.3330 | ±0.6660 | **+2.292** | **0.0219** | * |
| Site: UCSD (vs UAB) | +0.0350 | 0.1420 | ±0.2840 | +0.247 | 0.8051 |  |
| **Site: UW (vs UAB)** | **-0.3979** | 0.1165 | ±0.2329 | **-3.416** | **6.35e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3927** | 0.1282 | ±0.2564 | **-3.063** | **0.0022** | ** |
| Season: summer (vs autumn) | -0.2422 | 0.1505 | ±0.3010 | -1.609 | 0.1076 |  |
| Season: winter (vs autumn) | -0.0725 | 0.1441 | ±0.2882 | -0.503 | 0.6149 |  |
| **Age (years)** | **-0.0174** | 0.0048 | ±0.0096 | **-3.630** | **2.83e-04** | *** |
| BMI (kg/m2) | +0.0108 | 0.0075 | ±0.0149 | +1.442 | 0.1494 |  |
| Hypertension | +0.0950 | 0.1172 | ±0.2345 | +0.810 | 0.4180 |  |
| High cholesterol | -0.0692 | 0.1008 | ±0.2015 | -0.687 | 0.4920 |  |
| Kidney disease | +0.0437 | 0.1700 | ±0.3400 | +0.257 | 0.7973 |  |
| Circulatory disease | +0.0681 | 0.1672 | ±0.3343 | +0.407 | 0.6838 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.0151** | 0.0076 | ±0.0151 | **+1.999** | **0.0456** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **400**, R² = **0.1766**, Adj R² = **0.1466**, F-statistic = **5.90** (p = **1.59e-10**), Residual SE = **0.934** on **385** df, AIC = **1095.6**, BIC = **1155.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9094** | 0.3868 | ±0.7736 | **+7.522** | **5.39e-14** | *** |
| Education: graduate level (vs college) | -0.0918 | 0.0947 | ±0.1893 | -0.970 | 0.3322 |  |
| **Education: high school or below (vs college)** | **+0.7644** | 0.3297 | ±0.6593 | **+2.319** | **0.0204** | * |
| Site: UCSD (vs UAB) | +0.0342 | 0.1431 | ±0.2863 | +0.239 | 0.8111 |  |
| **Site: UW (vs UAB)** | **-0.3956** | 0.1180 | ±0.2361 | **-3.351** | **8.04e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3787** | 0.1284 | ±0.2568 | **-2.950** | **0.0032** | ** |
| Season: summer (vs autumn) | -0.2205 | 0.1505 | ±0.3010 | -1.465 | 0.1430 |  |
| Season: winter (vs autumn) | -0.0547 | 0.1439 | ±0.2878 | -0.380 | 0.7039 |  |
| **Age (years)** | **-0.0181** | 0.0047 | ±0.0095 | **-3.822** | **1.32e-04** | *** |
| BMI (kg/m2) | +0.0103 | 0.0075 | ±0.0149 | +1.374 | 0.1695 |  |
| Hypertension | +0.0889 | 0.1171 | ±0.2343 | +0.759 | 0.4481 |  |
| High cholesterol | -0.0710 | 0.1020 | ±0.2039 | -0.696 | 0.4864 |  |
| Kidney disease | -0.0044 | 0.1702 | ±0.3405 | -0.026 | 0.9794 |  |
| Circulatory disease | +0.0797 | 0.1687 | ±0.3375 | +0.472 | 0.6366 |  |
| Time < 54 (%) | -0.0235 | 0.0318 | ±0.0635 | -0.741 | 0.4588 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **400**, R² = **0.1765**, Adj R² = **0.1466**, F-statistic = **5.89** (p = **1.61e-10**), Residual SE = **0.934** on **385** df, AIC = **1095.6**, BIC = **1155.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9001** | 0.3853 | ±0.7706 | **+7.527** | **5.21e-14** | *** |
| Education: graduate level (vs college) | -0.0928 | 0.0947 | ±0.1893 | -0.981 | 0.3267 |  |
| **Education: high school or below (vs college)** | **+0.7641** | 0.3303 | ±0.6605 | **+2.314** | **0.0207** | * |
| Site: UCSD (vs UAB) | +0.0361 | 0.1426 | ±0.2853 | +0.253 | 0.8003 |  |
| **Site: UW (vs UAB)** | **-0.3966** | 0.1187 | ±0.2375 | **-3.340** | **8.39e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3774** | 0.1284 | ±0.2568 | **-2.939** | **0.0033** | ** |
| Season: summer (vs autumn) | -0.2206 | 0.1504 | ±0.3009 | -1.467 | 0.1425 |  |
| Season: winter (vs autumn) | -0.0530 | 0.1439 | ±0.2877 | -0.368 | 0.7128 |  |
| **Age (years)** | **-0.0181** | 0.0048 | ±0.0095 | **-3.789** | **1.51e-04** | *** |
| BMI (kg/m2) | +0.0103 | 0.0075 | ±0.0149 | +1.382 | 0.1670 |  |
| Hypertension | +0.0878 | 0.1183 | ±0.2366 | +0.742 | 0.4580 |  |
| High cholesterol | -0.0703 | 0.1015 | ±0.2031 | -0.693 | 0.4885 |  |
| Kidney disease | -0.0041 | 0.1698 | ±0.3396 | -0.024 | 0.9806 |  |
| Circulatory disease | +0.0795 | 0.1692 | ±0.3383 | +0.470 | 0.6385 |  |
| Avg. daily time < 54 (%) | -0.0284 | 0.0433 | ±0.0867 | -0.656 | 0.5116 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **400**, R² = **0.1762**, Adj R² = **0.1462**, F-statistic = **5.88** (p = **1.72e-10**), Residual SE = **0.935** on **385** df, AIC = **1095.8**, BIC = **1155.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8962** | 0.3869 | ±0.7737 | **+7.486** | **7.09e-14** | *** |
| Education: graduate level (vs college) | -0.0918 | 0.0947 | ±0.1895 | -0.969 | 0.3324 |  |
| **Education: high school or below (vs college)** | **+0.7660** | 0.3326 | ±0.6653 | **+2.303** | **0.0213** | * |
| Site: UCSD (vs UAB) | +0.0412 | 0.1429 | ±0.2857 | +0.288 | 0.7730 |  |
| **Site: UW (vs UAB)** | **-0.3911** | 0.1183 | ±0.2366 | **-3.307** | **9.45e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3770** | 0.1290 | ±0.2580 | **-2.922** | **0.0035** | ** |
| Season: summer (vs autumn) | -0.2237 | 0.1509 | ±0.3017 | -1.483 | 0.1381 |  |
| Season: winter (vs autumn) | -0.0545 | 0.1452 | ±0.2905 | -0.376 | 0.7073 |  |
| **Age (years)** | **-0.0182** | 0.0048 | ±0.0095 | **-3.825** | **1.31e-04** | *** |
| BMI (kg/m2) | +0.0104 | 0.0075 | ±0.0150 | +1.395 | 0.1630 |  |
| Hypertension | +0.0903 | 0.1184 | ±0.2367 | +0.763 | 0.4457 |  |
| High cholesterol | -0.0678 | 0.1009 | ±0.2017 | -0.672 | 0.5014 |  |
| Kidney disease | -0.0066 | 0.1698 | ±0.3397 | -0.039 | 0.9692 |  |
| Circulatory disease | +0.0812 | 0.1684 | ±0.3367 | +0.482 | 0.6298 |  |
| Time 54-69, pooled (%) | -0.0041 | 0.0204 | ±0.0408 | -0.200 | 0.8412 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **400**, R² = **0.1762**, Adj R² = **0.1462**, F-statistic = **5.88** (p = **1.73e-10**), Residual SE = **0.935** on **385** df, AIC = **1095.8**, BIC = **1155.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8924** | 0.3863 | ±0.7726 | **+7.488** | **7.00e-14** | *** |
| Education: graduate level (vs college) | -0.0917 | 0.0949 | ±0.1898 | -0.967 | 0.3338 |  |
| **Education: high school or below (vs college)** | **+0.7666** | 0.3335 | ±0.6669 | **+2.299** | **0.0215** | * |
| Site: UCSD (vs UAB) | +0.0420 | 0.1425 | ±0.2850 | +0.295 | 0.7680 |  |
| **Site: UW (vs UAB)** | **-0.3903** | 0.1187 | ±0.2374 | **-3.289** | **0.0010** | ** |
| **Season: spring (vs autumn)** | **-0.3771** | 0.1292 | ±0.2584 | **-2.918** | **0.0035** | ** |
| Season: summer (vs autumn) | -0.2243 | 0.1505 | ±0.3009 | -1.491 | 0.1361 |  |
| Season: winter (vs autumn) | -0.0553 | 0.1452 | ±0.2904 | -0.381 | 0.7035 |  |
| **Age (years)** | **-0.0182** | 0.0047 | ±0.0095 | **-3.823** | **1.32e-04** | *** |
| BMI (kg/m2) | +0.0104 | 0.0075 | ±0.0150 | +1.393 | 0.1635 |  |
| Hypertension | +0.0908 | 0.1189 | ±0.2378 | +0.763 | 0.4453 |  |
| High cholesterol | -0.0673 | 0.1007 | ±0.2014 | -0.668 | 0.5040 |  |
| Kidney disease | -0.0067 | 0.1698 | ±0.3396 | -0.039 | 0.9688 |  |
| Circulatory disease | +0.0816 | 0.1686 | ±0.3371 | +0.484 | 0.6284 |  |
| Avg. daily time 54-69 (%) | -0.0027 | 0.0209 | ±0.0418 | -0.127 | 0.8990 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **400**, R² = **0.1763**, Adj R² = **0.1464**, F-statistic = **5.89** (p = **1.67e-10**), Residual SE = **0.935** on **385** df, AIC = **1095.7**, BIC = **1155.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9033** | 0.3874 | ±0.7749 | **+7.494** | **6.70e-14** | *** |
| Education: graduate level (vs college) | -0.0922 | 0.0946 | ±0.1893 | -0.974 | 0.3298 |  |
| **Education: high school or below (vs college)** | **+0.7642** | 0.3320 | ±0.6641 | **+2.301** | **0.0214** | * |
| Site: UCSD (vs UAB) | +0.0387 | 0.1436 | ±0.2871 | +0.269 | 0.7877 |  |
| **Site: UW (vs UAB)** | **-0.3935** | 0.1187 | ±0.2373 | **-3.316** | **9.12e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3771** | 0.1287 | ±0.2575 | **-2.929** | **0.0034** | ** |
| Season: summer (vs autumn) | -0.2225 | 0.1512 | ±0.3024 | -1.471 | 0.1412 |  |
| Season: winter (vs autumn) | -0.0532 | 0.1452 | ±0.2905 | -0.366 | 0.7144 |  |
| **Age (years)** | **-0.0182** | 0.0047 | ±0.0095 | **-3.827** | **1.30e-04** | *** |
| BMI (kg/m2) | +0.0104 | 0.0075 | ±0.0149 | +1.396 | 0.1628 |  |
| Hypertension | +0.0889 | 0.1181 | ±0.2363 | +0.753 | 0.4516 |  |
| High cholesterol | -0.0694 | 0.1012 | ±0.2024 | -0.685 | 0.4932 |  |
| Kidney disease | -0.0060 | 0.1699 | ±0.3398 | -0.035 | 0.9718 |  |
| Circulatory disease | +0.0803 | 0.1683 | ±0.3366 | +0.477 | 0.6331 |  |
| Time < 70 (%) | -0.0055 | 0.0149 | ±0.0298 | -0.367 | 0.7139 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **400**, R² = **0.1762**, Adj R² = **0.1463**, F-statistic = **5.88** (p = **1.71e-10**), Residual SE = **0.935** on **385** df, AIC = **1095.8**, BIC = **1155.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8956** | 0.3862 | ±0.7724 | **+7.497** | **6.51e-14** | *** |
| Education: graduate level (vs college) | -0.0923 | 0.0948 | ±0.1897 | -0.973 | 0.3306 |  |
| **Education: high school or below (vs college)** | **+0.7650** | 0.3330 | ±0.6660 | **+2.297** | **0.0216** | * |
| Site: UCSD (vs UAB) | +0.0407 | 0.1428 | ±0.2857 | +0.285 | 0.7756 |  |
| **Site: UW (vs UAB)** | **-0.3923** | 0.1191 | ±0.2383 | **-3.292** | **9.94e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3768** | 0.1290 | ±0.2580 | **-2.921** | **0.0035** | ** |
| Season: summer (vs autumn) | -0.2236 | 0.1508 | ±0.3015 | -1.483 | 0.1381 |  |
| Season: winter (vs autumn) | -0.0539 | 0.1451 | ±0.2903 | -0.371 | 0.7106 |  |
| **Age (years)** | **-0.0181** | 0.0048 | ±0.0095 | **-3.820** | **1.34e-04** | *** |
| BMI (kg/m2) | +0.0104 | 0.0075 | ±0.0149 | +1.396 | 0.1628 |  |
| Hypertension | +0.0896 | 0.1191 | ±0.2382 | +0.752 | 0.4519 |  |
| High cholesterol | -0.0683 | 0.1008 | ±0.2017 | -0.677 | 0.4985 |  |
| Kidney disease | -0.0063 | 0.1697 | ±0.3395 | -0.037 | 0.9704 |  |
| Circulatory disease | +0.0810 | 0.1685 | ±0.3371 | +0.481 | 0.6308 |  |
| Avg. daily time < 70 (%) | -0.0039 | 0.0164 | ±0.0328 | -0.239 | 0.8114 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **400**, R² = **0.1782**, Adj R² = **0.1483**, F-statistic = **5.96** (p = **1.15e-10**), Residual SE = **0.934** on **385** df, AIC = **1094.8**, BIC = **1154.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9553 | 3.1115 | ±6.2230 | -0.307 | 0.7588 |  |
| Education: graduate level (vs college) | -0.0924 | 0.0946 | ±0.1892 | -0.977 | 0.3285 |  |
| **Education: high school or below (vs college)** | **+0.7616** | 0.3304 | ±0.6609 | **+2.305** | **0.0212** | * |
| Site: UCSD (vs UAB) | +0.0284 | 0.1427 | ±0.2854 | +0.199 | 0.8424 |  |
| **Site: UW (vs UAB)** | **-0.4021** | 0.1174 | ±0.2349 | **-3.424** | **6.17e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3790** | 0.1282 | ±0.2564 | **-2.955** | **0.0031** | ** |
| Season: summer (vs autumn) | -0.2208 | 0.1496 | ±0.2993 | -1.475 | 0.1401 |  |
| Season: winter (vs autumn) | -0.0574 | 0.1434 | ±0.2869 | -0.400 | 0.6890 |  |
| **Age (years)** | **-0.0179** | 0.0048 | ±0.0095 | **-3.761** | **1.69e-04** | *** |
| BMI (kg/m2) | +0.0102 | 0.0075 | ±0.0149 | +1.363 | 0.1730 |  |
| Hypertension | +0.0887 | 0.1171 | ±0.2341 | +0.758 | 0.4486 |  |
| High cholesterol | -0.0766 | 0.1020 | ±0.2040 | -0.751 | 0.4528 |  |
| Kidney disease | +0.0183 | 0.1709 | ±0.3417 | +0.107 | 0.9146 |  |
| Circulatory disease | +0.0745 | 0.1684 | ±0.3368 | +0.442 | 0.6582 |  |
| Time 54-250, pooled (%) | +0.0387 | 0.0309 | ±0.0618 | +1.254 | 0.2098 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **400**, R² = **0.1780**, Adj R² = **0.1481**, F-statistic = **5.96** (p = **1.19e-10**), Residual SE = **0.934** on **385** df, AIC = **1094.9**, BIC = **1154.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3131 | 3.3285 | ±6.6570 | -0.394 | 0.6932 |  |
| Education: graduate level (vs college) | -0.0942 | 0.0945 | ±0.1890 | -0.997 | 0.3188 |  |
| **Education: high school or below (vs college)** | **+0.7611** | 0.3316 | ±0.6633 | **+2.295** | **0.0217** | * |
| Site: UCSD (vs UAB) | +0.0316 | 0.1423 | ±0.2847 | +0.222 | 0.8240 |  |
| **Site: UW (vs UAB)** | **-0.4023** | 0.1174 | ±0.2349 | **-3.425** | **6.14e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3766** | 0.1282 | ±0.2564 | **-2.937** | **0.0033** | ** |
| Season: summer (vs autumn) | -0.2217 | 0.1496 | ±0.2991 | -1.483 | 0.1382 |  |
| Season: winter (vs autumn) | -0.0559 | 0.1434 | ±0.2868 | -0.390 | 0.6966 |  |
| **Age (years)** | **-0.0178** | 0.0048 | ±0.0096 | **-3.700** | **2.15e-04** | *** |
| BMI (kg/m2) | +0.0103 | 0.0075 | ±0.0149 | +1.383 | 0.1666 |  |
| Hypertension | +0.0874 | 0.1175 | ±0.2349 | +0.744 | 0.4568 |  |
| High cholesterol | -0.0741 | 0.1015 | ±0.2030 | -0.730 | 0.4656 |  |
| Kidney disease | +0.0217 | 0.1714 | ±0.3427 | +0.126 | 0.8994 |  |
| Circulatory disease | +0.0736 | 0.1690 | ±0.3380 | +0.436 | 0.6631 |  |
| Avg. daily time 54-250 (%) | +0.0421 | 0.0327 | ±0.0654 | +1.288 | 0.1978 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **400**, R² = **0.1832**, Adj R² = **0.1535**, F-statistic = **6.17** (p = **4.14e-11**), Residual SE = **0.931** on **385** df, AIC = **1092.4**, BIC = **1152.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8893** | 0.3878 | ±0.7756 | **+7.450** | **9.32e-14** | *** |
| Education: graduate level (vs college) | -0.0866 | 0.0944 | ±0.1888 | -0.917 | 0.3591 |  |
| **Education: high school or below (vs college)** | **+0.7812** | 0.3314 | ±0.6627 | **+2.358** | **0.0184** | * |
| Site: UCSD (vs UAB) | +0.0453 | 0.1414 | ±0.2828 | +0.320 | 0.7489 |  |
| **Site: UW (vs UAB)** | **-0.3815** | 0.1169 | ±0.2338 | **-3.263** | **0.0011** | ** |
| **Season: spring (vs autumn)** | **-0.4021** | 0.1298 | ±0.2596 | **-3.098** | **0.0019** | ** |
| Season: summer (vs autumn) | -0.2511 | 0.1530 | ±0.3061 | -1.641 | 0.1008 |  |
| Season: winter (vs autumn) | -0.0908 | 0.1464 | ±0.2927 | -0.621 | 0.5349 |  |
| **Age (years)** | **-0.0174** | 0.0048 | ±0.0096 | **-3.602** | **3.16e-04** | *** |
| BMI (kg/m2) | +0.0105 | 0.0074 | ±0.0148 | +1.418 | 0.1563 |  |
| Hypertension | +0.1070 | 0.1176 | ±0.2353 | +0.910 | 0.3628 |  |
| High cholesterol | -0.0603 | 0.1008 | ±0.2016 | -0.598 | 0.5497 |  |
| Kidney disease | +0.0479 | 0.1708 | ±0.3416 | +0.281 | 0.7790 |  |
| Circulatory disease | +0.0711 | 0.1676 | ±0.3352 | +0.424 | 0.6715 |  |
| **Time 181-250, pooled (%)** | **-0.0211** | 0.0099 | ±0.0199 | **-2.119** | **0.0341** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **400**, R² = **0.1831**, Adj R² = **0.1534**, F-statistic = **6.16** (p = **4.22e-11**), Residual SE = **0.931** on **385** df, AIC = **1092.4**, BIC = **1152.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8865** | 0.3881 | ±0.7761 | **+7.438** | **1.02e-13** | *** |
| Education: graduate level (vs college) | -0.0862 | 0.0944 | ±0.1889 | -0.913 | 0.3613 |  |
| **Education: high school or below (vs college)** | **+0.7794** | 0.3316 | ±0.6632 | **+2.351** | **0.0187** | * |
| Site: UCSD (vs UAB) | +0.0439 | 0.1415 | ±0.2830 | +0.311 | 0.7562 |  |
| **Site: UW (vs UAB)** | **-0.3814** | 0.1170 | ±0.2339 | **-3.261** | **0.0011** | ** |
| **Season: spring (vs autumn)** | **-0.4015** | 0.1298 | ±0.2596 | **-3.092** | **0.0020** | ** |
| Season: summer (vs autumn) | -0.2520 | 0.1532 | ±0.3064 | -1.645 | 0.0999 | . |
| Season: winter (vs autumn) | -0.0915 | 0.1467 | ±0.2934 | -0.624 | 0.5328 |  |
| **Age (years)** | **-0.0174** | 0.0048 | ±0.0096 | **-3.612** | **3.04e-04** | *** |
| BMI (kg/m2) | +0.0106 | 0.0074 | ±0.0148 | +1.428 | 0.1534 |  |
| Hypertension | +0.1075 | 0.1177 | ±0.2355 | +0.913 | 0.3613 |  |
| High cholesterol | -0.0597 | 0.1008 | ±0.2016 | -0.593 | 0.5535 |  |
| Kidney disease | +0.0467 | 0.1708 | ±0.3415 | +0.274 | 0.7843 |  |
| Circulatory disease | +0.0708 | 0.1675 | ±0.3350 | +0.423 | 0.6724 |  |
| **Avg. daily time 181-250 (%)** | **-0.0201** | 0.0099 | ±0.0198 | **-2.031** | **0.0423** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **400**, R² = **0.1828**, Adj R² = **0.1531**, F-statistic = **6.15** (p = **4.50e-11**), Residual SE = **0.931** on **385** df, AIC = **1092.6**, BIC = **1152.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8873** | 0.3879 | ±0.7759 | **+7.443** | **9.87e-14** | *** |
| Education: graduate level (vs college) | -0.0873 | 0.0944 | ±0.1889 | -0.925 | 0.3552 |  |
| **Education: high school or below (vs college)** | **+0.7793** | 0.3314 | ±0.6628 | **+2.351** | **0.0187** | * |
| Site: UCSD (vs UAB) | +0.0448 | 0.1415 | ±0.2830 | +0.317 | 0.7516 |  |
| **Site: UW (vs UAB)** | **-0.3834** | 0.1169 | ±0.2338 | **-3.280** | **0.0010** | ** |
| **Season: spring (vs autumn)** | **-0.3983** | 0.1294 | ±0.2588 | **-3.078** | **0.0021** | ** |
| Season: summer (vs autumn) | -0.2488 | 0.1527 | ±0.3055 | -1.629 | 0.1033 |  |
| Season: winter (vs autumn) | -0.0880 | 0.1461 | ±0.2922 | -0.602 | 0.5471 |  |
| **Age (years)** | **-0.0174** | 0.0048 | ±0.0096 | **-3.606** | **3.11e-04** | *** |
| BMI (kg/m2) | +0.0105 | 0.0074 | ±0.0148 | +1.413 | 0.1577 |  |
| Hypertension | +0.1058 | 0.1176 | ±0.2352 | +0.899 | 0.3684 |  |
| High cholesterol | -0.0624 | 0.1008 | ±0.2016 | -0.619 | 0.5358 |  |
| Kidney disease | +0.0501 | 0.1709 | ±0.3418 | +0.293 | 0.7696 |  |
| Circulatory disease | +0.0709 | 0.1677 | ±0.3353 | +0.423 | 0.6724 |  |
| **Time > 180 (%)** | **-0.0180** | 0.0090 | ±0.0181 | **-1.996** | **0.0459** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **400**, R² = **0.1826**, Adj R² = **0.1528**, F-statistic = **6.14** (p = **4.73e-11**), Residual SE = **0.931** on **385** df, AIC = **1092.7**, BIC = **1152.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8838** | 0.3882 | ±0.7763 | **+7.429** | **1.09e-13** | *** |
| Education: graduate level (vs college) | -0.0872 | 0.0945 | ±0.1889 | -0.923 | 0.3561 |  |
| **Education: high school or below (vs college)** | **+0.7774** | 0.3317 | ±0.6634 | **+2.344** | **0.0191** | * |
| Site: UCSD (vs UAB) | +0.0433 | 0.1416 | ±0.2832 | +0.306 | 0.7599 |  |
| **Site: UW (vs UAB)** | **-0.3833** | 0.1170 | ±0.2340 | **-3.276** | **0.0011** | ** |
| **Season: spring (vs autumn)** | **-0.3975** | 0.1295 | ±0.2590 | **-3.070** | **0.0021** | ** |
| Season: summer (vs autumn) | -0.2490 | 0.1528 | ±0.3056 | -1.629 | 0.1032 |  |
| Season: winter (vs autumn) | -0.0881 | 0.1464 | ±0.2928 | -0.602 | 0.5475 |  |
| **Age (years)** | **-0.0174** | 0.0048 | ±0.0096 | **-3.618** | **2.97e-04** | *** |
| BMI (kg/m2) | +0.0106 | 0.0074 | ±0.0148 | +1.424 | 0.1545 |  |
| Hypertension | +0.1057 | 0.1177 | ±0.2354 | +0.899 | 0.3689 |  |
| High cholesterol | -0.0615 | 0.1008 | ±0.2016 | -0.610 | 0.5418 |  |
| Kidney disease | +0.0483 | 0.1710 | ±0.3421 | +0.282 | 0.7777 |  |
| Circulatory disease | +0.0707 | 0.1676 | ±0.3353 | +0.422 | 0.6730 |  |
| Avg. daily time > 180 (%) | -0.0169 | 0.0091 | ±0.0183 | -1.854 | 0.0638 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **400**, R² = **0.1807**, Adj R² = **0.1509**, F-statistic = **6.07** (p = **6.88e-11**), Residual SE = **0.932** on **385** df, AIC = **1093.6**, BIC = **1153.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8732** | 0.3877 | ±0.7753 | **+7.411** | **1.25e-13** | *** |
| Education: graduate level (vs college) | -0.0975 | 0.0947 | ±0.1895 | -1.029 | 0.3033 |  |
| **Education: high school or below (vs college)** | **+0.7814** | 0.3318 | ±0.6636 | **+2.355** | **0.0185** | * |
| Site: UCSD (vs UAB) | +0.0397 | 0.1418 | ±0.2836 | +0.280 | 0.7793 |  |
| **Site: UW (vs UAB)** | **-0.3880** | 0.1168 | ±0.2335 | **-3.323** | **8.92e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3890** | 0.1285 | ±0.2570 | **-3.027** | **0.0025** | ** |
| Season: summer (vs autumn) | -0.2498 | 0.1530 | ±0.3060 | -1.633 | 0.1026 |  |
| Season: winter (vs autumn) | -0.0727 | 0.1446 | ±0.2893 | -0.502 | 0.6155 |  |
| **Age (years)** | **-0.0178** | 0.0048 | ±0.0096 | **-3.715** | **2.03e-04** | *** |
| BMI (kg/m2) | +0.0112 | 0.0075 | ±0.0150 | +1.492 | 0.1357 |  |
| Hypertension | +0.1042 | 0.1178 | ±0.2357 | +0.885 | 0.3764 |  |
| High cholesterol | -0.0668 | 0.1008 | ±0.2017 | -0.663 | 0.5076 |  |
| Kidney disease | -0.0054 | 0.1689 | ±0.3378 | -0.032 | 0.9744 |  |
| Circulatory disease | +0.0650 | 0.1685 | ±0.3370 | +0.386 | 0.6997 |  |
| Nocturnal time > 180 (%) | -0.0153 | 0.0082 | ±0.0163 | -1.871 | 0.0614 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **400**, R² = **0.1783**, Adj R² = **0.1485**, F-statistic = **5.97** (p = **1.12e-10**), Residual SE = **0.933** on **385** df, AIC = **1094.7**, BIC = **1154.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9029** | 0.3861 | ±0.7722 | **+7.518** | **5.55e-14** | *** |
| Education: graduate level (vs college) | -0.0951 | 0.0948 | ±0.1896 | -1.003 | 0.3157 |  |
| **Education: high school or below (vs college)** | **+0.7662** | 0.3314 | ±0.6627 | **+2.312** | **0.0208** | * |
| Site: UCSD (vs UAB) | +0.0515 | 0.1422 | ±0.2844 | +0.362 | 0.7173 |  |
| **Site: UW (vs UAB)** | **-0.3886** | 0.1172 | ±0.2343 | **-3.317** | **9.11e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3871** | 0.1286 | ±0.2573 | **-3.009** | **0.0026** | ** |
| Season: summer (vs autumn) | -0.2336 | 0.1518 | ±0.3035 | -1.540 | 0.1236 |  |
| Season: winter (vs autumn) | -0.0656 | 0.1449 | ±0.2897 | -0.453 | 0.6507 |  |
| **Age (years)** | **-0.0178** | 0.0048 | ±0.0096 | **-3.703** | **2.13e-04** | *** |
| BMI (kg/m2) | +0.0100 | 0.0074 | ±0.0149 | +1.345 | 0.1786 |  |
| Hypertension | +0.0975 | 0.1181 | ±0.2362 | +0.826 | 0.4090 |  |
| High cholesterol | -0.0690 | 0.1016 | ±0.2033 | -0.679 | 0.4972 |  |
| Kidney disease | +0.0087 | 0.1687 | ±0.3373 | +0.052 | 0.9588 |  |
| Circulatory disease | +0.0761 | 0.1678 | ±0.3355 | +0.454 | 0.6502 |  |
| Any reading > 250 during wear (0/1) | -0.1320 | 0.1249 | ±0.2498 | -1.057 | 0.2907 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **400**, R² = **0.1785**, Adj R² = **0.1487**, F-statistic = **5.98** (p = **1.07e-10**), Residual SE = **0.933** on **385** df, AIC = **1094.7**, BIC = **1154.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8810** | 0.3876 | ±0.7753 | **+7.432** | **1.07e-13** | *** |
| Education: graduate level (vs college) | -0.0914 | 0.0947 | ±0.1894 | -0.965 | 0.3344 |  |
| **Education: high school or below (vs college)** | **+0.7682** | 0.3316 | ±0.6631 | **+2.317** | **0.0205** | * |
| Site: UCSD (vs UAB) | +0.0424 | 0.1420 | ±0.2839 | +0.299 | 0.7652 |  |
| **Site: UW (vs UAB)** | **-0.3924** | 0.1168 | ±0.2336 | **-3.359** | **7.81e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3765** | 0.1281 | ±0.2562 | **-2.939** | **0.0033** | ** |
| Season: summer (vs autumn) | -0.2303 | 0.1504 | ±0.3009 | -1.531 | 0.1258 |  |
| Season: winter (vs autumn) | -0.0649 | 0.1440 | ±0.2879 | -0.451 | 0.6521 |  |
| **Age (years)** | **-0.0178** | 0.0048 | ±0.0096 | **-3.708** | **2.09e-04** | *** |
| BMI (kg/m2) | +0.0103 | 0.0075 | ±0.0149 | +1.387 | 0.1655 |  |
| Hypertension | +0.0954 | 0.1173 | ±0.2347 | +0.813 | 0.4160 |  |
| High cholesterol | -0.0713 | 0.1014 | ±0.2028 | -0.703 | 0.4819 |  |
| Kidney disease | +0.0329 | 0.1719 | ±0.3439 | +0.191 | 0.8482 |  |
| Circulatory disease | +0.0750 | 0.1686 | ±0.3372 | +0.445 | 0.6563 |  |
| Time > 250 (%) | -0.0720 | 0.0652 | ±0.1304 | -1.104 | 0.2695 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 400)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **400**, R² = **0.1779**, Adj R² = **0.1480**, F-statistic = **5.95** (p = **1.21e-10**), Residual SE = **0.934** on **385** df, AIC = **1094.9**, BIC = **1154.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8787** | 0.3880 | ±0.7760 | **+7.420** | **1.18e-13** | *** |
| Education: graduate level (vs college) | -0.0918 | 0.0948 | ±0.1896 | -0.968 | 0.3328 |  |
| **Education: high school or below (vs college)** | **+0.7673** | 0.3318 | ±0.6635 | **+2.313** | **0.0207** | * |
| Site: UCSD (vs UAB) | +0.0412 | 0.1420 | ±0.2839 | +0.290 | 0.7717 |  |
| **Site: UW (vs UAB)** | **-0.3913** | 0.1169 | ±0.2337 | **-3.348** | **8.13e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3766** | 0.1282 | ±0.2564 | **-2.937** | **0.0033** | ** |
| Season: summer (vs autumn) | -0.2289 | 0.1503 | ±0.3007 | -1.523 | 0.1279 |  |
| Season: winter (vs autumn) | -0.0638 | 0.1440 | ±0.2881 | -0.443 | 0.6578 |  |
| **Age (years)** | **-0.0178** | 0.0048 | ±0.0096 | **-3.719** | **2.00e-04** | *** |
| BMI (kg/m2) | +0.0104 | 0.0075 | ±0.0149 | +1.396 | 0.1626 |  |
| Hypertension | +0.0943 | 0.1173 | ±0.2347 | +0.804 | 0.4216 |  |
| High cholesterol | -0.0689 | 0.1013 | ±0.2026 | -0.680 | 0.4963 |  |
| Kidney disease | +0.0273 | 0.1727 | ±0.3454 | +0.158 | 0.8744 |  |
| Circulatory disease | +0.0756 | 0.1688 | ±0.3376 | +0.448 | 0.6541 |  |
| Avg. daily time > 250 (%) | -0.0582 | 0.0647 | ±0.1294 | -0.899 | 0.3685 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 400; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **400**, R² = **0.2783**, Adj R² = **0.2540**, F-statistic = **11.45** (p = **6.13e-21**), Residual SE = **1.980** on **386** df, AIC = **1695.3**, BIC = **1751.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8323** | 0.7739 | ±1.5479 | **+30.793** | **3.20e-208** | *** |
| Education: graduate level (vs college) | -0.0805 | 0.2177 | ±0.4353 | -0.370 | 0.7114 |  |
| Education: high school or below (vs college) | +0.4124 | 0.4272 | ±0.8543 | +0.965 | 0.3343 |  |
| Site: UCSD (vs UAB) | -0.0816 | 0.2634 | ±0.5269 | -0.310 | 0.7567 |  |
| **Site: UW (vs UAB)** | **-0.7177** | 0.2315 | ±0.4630 | **-3.100** | **0.0019** | ** |
| Season: spring (vs autumn) | -0.2613 | 0.2674 | ±0.5348 | -0.977 | 0.3284 |  |
| **Season: summer (vs autumn)** | **+2.0643** | 0.3492 | ±0.6984 | **+5.911** | **3.40e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2042** | 0.2650 | ±0.5300 | **-4.544** | **5.51e-06** | *** |
| Age (years) | +0.0181 | 0.0097 | ±0.0194 | +1.875 | 0.0608 | . |
| BMI (kg/m2) | -0.0119 | 0.0145 | ±0.0290 | -0.825 | 0.4096 |  |
| Hypertension | +0.0805 | 0.2181 | ±0.4362 | +0.369 | 0.7120 |  |
| High cholesterol | -0.1794 | 0.2171 | ±0.4342 | -0.826 | 0.4087 |  |
| **Kidney disease** | **+1.1254** | 0.4089 | ±0.8178 | **+2.752** | **0.0059** | ** |
| Circulatory disease | +0.0276 | 0.3108 | ±0.6217 | +0.089 | 0.9292 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **400**, R² = **0.2787**, Adj R² = **0.2524**, F-statistic = **10.62** (p = **1.97e-20**), Residual SE = **1.982** on **385** df, AIC = **1697.1**, BIC = **1756.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3402** | 1.5539 | ±3.1079 | **+15.664** | **2.68e-55** | *** |
| Education: graduate level (vs college) | -0.0836 | 0.2179 | ±0.4358 | -0.383 | 0.7014 |  |
| Education: high school or below (vs college) | +0.4266 | 0.4332 | ±0.8665 | +0.985 | 0.3247 |  |
| Site: UCSD (vs UAB) | -0.0664 | 0.2700 | ±0.5399 | -0.246 | 0.8057 |  |
| **Site: UW (vs UAB)** | **-0.7139** | 0.2332 | ±0.4663 | **-3.062** | **0.0022** | ** |
| Season: spring (vs autumn) | -0.2763 | 0.2696 | ±0.5393 | -1.025 | 0.3055 |  |
| **Season: summer (vs autumn)** | **+2.0620** | 0.3502 | ±0.7004 | **+5.889** | **3.90e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2107** | 0.2669 | ±0.5339 | **-4.535** | **5.75e-06** | *** |
| Age (years) | +0.0188 | 0.0100 | ±0.0200 | +1.884 | 0.0596 | . |
| BMI (kg/m2) | -0.0111 | 0.0146 | ±0.0292 | -0.758 | 0.4484 |  |
| Hypertension | +0.0791 | 0.2194 | ±0.4388 | +0.361 | 0.7183 |  |
| High cholesterol | -0.1653 | 0.2211 | ±0.4421 | -0.748 | 0.4545 |  |
| **Kidney disease** | **+1.1305** | 0.4118 | ±0.8236 | **+2.745** | **0.0060** | ** |
| Circulatory disease | +0.0219 | 0.3120 | ±0.6240 | +0.070 | 0.9440 |  |
| HbA1c (%) | -0.1023 | 0.2821 | ±0.5641 | -0.363 | 0.7168 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **400**, R² = **0.2801**, Adj R² = **0.2539**, F-statistic = **10.70** (p = **1.39e-20**), Residual SE = **1.980** on **385** df, AIC = **1696.3**, BIC = **1756.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5691** | 1.1008 | ±2.2016 | **+22.319** | **2.43e-110** | *** |
| Education: graduate level (vs college) | -0.0672 | 0.2190 | ±0.4381 | -0.307 | 0.7589 |  |
| Education: high school or below (vs college) | +0.4389 | 0.4268 | ±0.8536 | +1.028 | 0.3038 |  |
| Site: UCSD (vs UAB) | -0.0754 | 0.2650 | ±0.5300 | -0.284 | 0.7761 |  |
| **Site: UW (vs UAB)** | **-0.6939** | 0.2375 | ±0.4750 | **-2.921** | **0.0035** | ** |
| Season: spring (vs autumn) | -0.2788 | 0.2698 | ±0.5396 | -1.034 | 0.3014 |  |
| **Season: summer (vs autumn)** | **+2.0468** | 0.3522 | ±0.7045 | **+5.811** | **6.21e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2384** | 0.2686 | ±0.5372 | **-4.610** | **4.02e-06** | *** |
| Age (years) | +0.0188 | 0.0097 | ±0.0194 | +1.939 | 0.0525 | . |
| BMI (kg/m2) | -0.0114 | 0.0143 | ±0.0287 | -0.794 | 0.4271 |  |
| Hypertension | +0.1024 | 0.2190 | ±0.4381 | +0.468 | 0.6401 |  |
| High cholesterol | -0.1573 | 0.2210 | ±0.4421 | -0.712 | 0.4766 |  |
| **Kidney disease** | **+1.1662** | 0.4176 | ±0.8352 | **+2.793** | **0.0052** | ** |
| Circulatory disease | +0.0217 | 0.3093 | ±0.6185 | +0.070 | 0.9439 |  |
| Mean glucose (mg/dL) | -0.0071 | 0.0074 | ±0.0148 | -0.954 | 0.3403 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **400**, R² = **0.2801**, Adj R² = **0.2539**, F-statistic = **10.70** (p = **1.39e-20**), Residual SE = **1.980** on **385** df, AIC = **1696.3**, BIC = **1756.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.5486** | 1.9691 | ±3.9381 | **+12.975** | **1.70e-38** | *** |
| Education: graduate level (vs college) | -0.0672 | 0.2190 | ±0.4381 | -0.307 | 0.7589 |  |
| Education: high school or below (vs college) | +0.4389 | 0.4268 | ±0.8536 | +1.028 | 0.3038 |  |
| Site: UCSD (vs UAB) | -0.0754 | 0.2650 | ±0.5300 | -0.284 | 0.7761 |  |
| **Site: UW (vs UAB)** | **-0.6939** | 0.2375 | ±0.4750 | **-2.921** | **0.0035** | ** |
| Season: spring (vs autumn) | -0.2788 | 0.2698 | ±0.5396 | -1.034 | 0.3014 |  |
| **Season: summer (vs autumn)** | **+2.0468** | 0.3522 | ±0.7045 | **+5.811** | **6.21e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2384** | 0.2686 | ±0.5372 | **-4.610** | **4.02e-06** | *** |
| Age (years) | +0.0188 | 0.0097 | ±0.0194 | +1.939 | 0.0525 | . |
| BMI (kg/m2) | -0.0114 | 0.0143 | ±0.0287 | -0.794 | 0.4271 |  |
| Hypertension | +0.1024 | 0.2190 | ±0.4381 | +0.468 | 0.6401 |  |
| High cholesterol | -0.1573 | 0.2210 | ±0.4421 | -0.712 | 0.4766 |  |
| **Kidney disease** | **+1.1662** | 0.4176 | ±0.8352 | **+2.793** | **0.0052** | ** |
| Circulatory disease | +0.0217 | 0.3093 | ±0.6185 | +0.070 | 0.9439 |  |
| GMI (%) | -0.2959 | 0.3103 | ±0.6206 | -0.954 | 0.3403 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **400**, R² = **0.2830**, Adj R² = **0.2569**, F-statistic = **10.85** (p = **6.81e-21**), Residual SE = **1.976** on **385** df, AIC = **1694.7**, BIC = **1754.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9136** | 1.0305 | ±2.0610 | **+24.176** | **3.99e-129** | *** |
| Education: graduate level (vs college) | -0.0683 | 0.2190 | ±0.4380 | -0.312 | 0.7550 |  |
| Education: high school or below (vs college) | +0.4621 | 0.4249 | ±0.8498 | +1.088 | 0.2768 |  |
| Site: UCSD (vs UAB) | -0.0620 | 0.2659 | ±0.5318 | -0.233 | 0.8155 |  |
| **Site: UW (vs UAB)** | **-0.6889** | 0.2360 | ±0.4721 | **-2.919** | **0.0035** | ** |
| Season: spring (vs autumn) | -0.2764 | 0.2673 | ±0.5347 | -1.034 | 0.3012 |  |
| **Season: summer (vs autumn)** | **+2.0327** | 0.3518 | ±0.7036 | **+5.778** | **7.56e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2381** | 0.2664 | ±0.5328 | **-4.647** | **3.36e-06** | *** |
| Age (years) | +0.0178 | 0.0097 | ±0.0194 | +1.842 | 0.0655 | . |
| BMI (kg/m2) | -0.0087 | 0.0144 | ±0.0289 | -0.600 | 0.5486 |  |
| Hypertension | +0.1130 | 0.2185 | ±0.4370 | +0.517 | 0.6050 |  |
| High cholesterol | -0.1363 | 0.2220 | ±0.4440 | -0.614 | 0.5394 |  |
| **Kidney disease** | **+1.1377** | 0.4094 | ±0.8188 | **+2.779** | **0.0055** | ** |
| Circulatory disease | +0.0062 | 0.3072 | ±0.6143 | +0.020 | 0.9839 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0105 | 0.0067 | ±0.0133 | -1.578 | 0.1145 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **400**, R² = **0.2784**, Adj R² = **0.2522**, F-statistic = **10.61** (p = **2.10e-20**), Residual SE = **1.982** on **385** df, AIC = **1697.2**, BIC = **1757.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8760** | 0.8220 | ±1.6440 | **+29.047** | **1.68e-185** | *** |
| Education: graduate level (vs college) | -0.0790 | 0.2187 | ±0.4374 | -0.361 | 0.7178 |  |
| Education: high school or below (vs college) | +0.4126 | 0.4273 | ±0.8547 | +0.965 | 0.3343 |  |
| Site: UCSD (vs UAB) | -0.0790 | 0.2663 | ±0.5327 | -0.297 | 0.7667 |  |
| **Site: UW (vs UAB)** | **-0.7166** | 0.2334 | ±0.4668 | **-3.070** | **0.0021** | ** |
| Season: spring (vs autumn) | -0.2630 | 0.2689 | ±0.5379 | -0.978 | 0.3281 |  |
| **Season: summer (vs autumn)** | **+2.0630** | 0.3507 | ±0.7014 | **+5.882** | **4.04e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2073** | 0.2689 | ±0.5379 | **-4.489** | **7.15e-06** | *** |
| Age (years) | +0.0184 | 0.0097 | ±0.0194 | +1.898 | 0.0576 | . |
| BMI (kg/m2) | -0.0119 | 0.0145 | ±0.0291 | -0.816 | 0.4144 |  |
| Hypertension | +0.0829 | 0.2191 | ±0.4381 | +0.379 | 0.7051 |  |
| High cholesterol | -0.1807 | 0.2173 | ±0.4346 | -0.832 | 0.4057 |  |
| **Kidney disease** | **+1.1367** | 0.4242 | ±0.8485 | **+2.679** | **0.0074** | ** |
| Circulatory disease | +0.0266 | 0.3109 | ±0.6217 | +0.086 | 0.9317 |  |
| Glucose SD, pooled (mg/dL) | -0.0028 | 0.0174 | ±0.0349 | -0.162 | 0.8710 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **400**, R² = **0.2785**, Adj R² = **0.2523**, F-statistic = **10.62** (p = **2.04e-20**), Residual SE = **1.982** on **385** df, AIC = **1697.1**, BIC = **1757.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9027** | 0.8136 | ±1.6272 | **+29.378** | **1.04e-189** | *** |
| Education: graduate level (vs college) | -0.0788 | 0.2185 | ±0.4371 | -0.360 | 0.7186 |  |
| Education: high school or below (vs college) | +0.4152 | 0.4278 | ±0.8556 | +0.971 | 0.3318 |  |
| Site: UCSD (vs UAB) | -0.0760 | 0.2661 | ±0.5322 | -0.286 | 0.7752 |  |
| **Site: UW (vs UAB)** | **-0.7149** | 0.2336 | ±0.4672 | **-3.060** | **0.0022** | ** |
| Season: spring (vs autumn) | -0.2652 | 0.2693 | ±0.5385 | -0.985 | 0.3248 |  |
| **Season: summer (vs autumn)** | **+2.0592** | 0.3524 | ±0.7049 | **+5.843** | **5.13e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2101** | 0.2685 | ±0.5371 | **-4.506** | **6.60e-06** | *** |
| Age (years) | +0.0187 | 0.0097 | ±0.0195 | +1.917 | 0.0553 | . |
| BMI (kg/m2) | -0.0118 | 0.0145 | ±0.0291 | -0.810 | 0.4179 |  |
| Hypertension | +0.0842 | 0.2187 | ±0.4374 | +0.385 | 0.7002 |  |
| High cholesterol | -0.1808 | 0.2173 | ±0.4346 | -0.832 | 0.4055 |  |
| **Kidney disease** | **+1.1470** | 0.4250 | ±0.8500 | **+2.699** | **0.0070** | ** |
| Circulatory disease | +0.0252 | 0.3106 | ±0.6211 | +0.081 | 0.9352 |  |
| Avg. daily SD (mg/dL) | -0.0055 | 0.0190 | ±0.0379 | -0.289 | 0.7729 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **400**, R² = **0.2787**, Adj R² = **0.2525**, F-statistic = **10.63** (p = **1.95e-20**), Residual SE = **1.982** on **385** df, AIC = **1697.1**, BIC = **1756.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6846** | 0.8531 | ±1.7062 | **+27.763** | **1.23e-169** | *** |
| Education: graduate level (vs college) | -0.0816 | 0.2181 | ±0.4362 | -0.374 | 0.7083 |  |
| Education: high school or below (vs college) | +0.4178 | 0.4278 | ±0.8556 | +0.977 | 0.3288 |  |
| Site: UCSD (vs UAB) | -0.0874 | 0.2649 | ±0.5298 | -0.330 | 0.7416 |  |
| **Site: UW (vs UAB)** | **-0.7147** | 0.2315 | ±0.4630 | **-3.087** | **0.0020** | ** |
| Season: spring (vs autumn) | -0.2602 | 0.2682 | ±0.5365 | -0.970 | 0.3320 |  |
| **Season: summer (vs autumn)** | **+2.0641** | 0.3502 | ±0.7005 | **+5.893** | **3.79e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2040** | 0.2653 | ±0.5306 | **-4.538** | **5.68e-06** | *** |
| Age (years) | +0.0175 | 0.0097 | ±0.0195 | +1.801 | 0.0717 | . |
| BMI (kg/m2) | -0.0120 | 0.0146 | ±0.0291 | -0.824 | 0.4098 |  |
| Hypertension | +0.0788 | 0.2188 | ±0.4376 | +0.360 | 0.7188 |  |
| High cholesterol | -0.1705 | 0.2180 | ±0.4361 | -0.782 | 0.4343 |  |
| **Kidney disease** | **+1.1030** | 0.4179 | ±0.8359 | **+2.639** | **0.0083** | ** |
| Circulatory disease | +0.0294 | 0.3119 | ±0.6238 | +0.094 | 0.9249 |  |
| CV (%) | +0.0096 | 0.0231 | ±0.0462 | +0.418 | 0.6762 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **400**, R² = **0.2783**, Adj R² = **0.2521**, F-statistic = **10.61** (p = **2.13e-20**), Residual SE = **1.982** on **385** df, AIC = **1697.2**, BIC = **1757.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7935** | 0.9870 | ±1.9740 | **+24.107** | **2.12e-128** | *** |
| Education: graduate level (vs college) | -0.0798 | 0.2185 | ±0.4370 | -0.365 | 0.7148 |  |
| Education: high school or below (vs college) | +0.4122 | 0.4277 | ±0.8553 | +0.964 | 0.3351 |  |
| Site: UCSD (vs UAB) | -0.0806 | 0.2656 | ±0.5312 | -0.304 | 0.7614 |  |
| **Site: UW (vs UAB)** | **-0.7176** | 0.2323 | ±0.4646 | **-3.089** | **0.0020** | ** |
| Season: spring (vs autumn) | -0.2618 | 0.2684 | ±0.5368 | -0.975 | 0.3294 |  |
| **Season: summer (vs autumn)** | **+2.0642** | 0.3502 | ±0.7003 | **+5.895** | **3.75e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2043** | 0.2660 | ±0.5320 | **-4.527** | **5.97e-06** | *** |
| Age (years) | +0.0182 | 0.0098 | ±0.0195 | +1.869 | 0.0616 | . |
| BMI (kg/m2) | -0.0119 | 0.0145 | ±0.0291 | -0.819 | 0.4126 |  |
| Hypertension | +0.0808 | 0.2186 | ±0.4373 | +0.369 | 0.7119 |  |
| High cholesterol | -0.1802 | 0.2174 | ±0.4349 | -0.829 | 0.4071 |  |
| **Kidney disease** | **+1.1283** | 0.4142 | ±0.8285 | **+2.724** | **0.0065** | ** |
| Circulatory disease | +0.0275 | 0.3114 | ±0.6228 | +0.088 | 0.9295 |  |
| Mean / SD ratio | +0.0059 | 0.0915 | ±0.1830 | +0.064 | 0.9490 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **400**, R² = **0.2788**, Adj R² = **0.2525**, F-statistic = **10.63** (p = **1.92e-20**), Residual SE = **1.982** on **385** df, AIC = **1697.0**, BIC = **1756.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5511** | 1.0305 | ±2.0609 | **+22.855** | **1.31e-115** | *** |
| Education: graduate level (vs college) | -0.0757 | 0.2185 | ±0.4370 | -0.346 | 0.7290 |  |
| Education: high school or below (vs college) | +0.4191 | 0.4285 | ±0.8570 | +0.978 | 0.3280 |  |
| Site: UCSD (vs UAB) | -0.0708 | 0.2669 | ±0.5338 | -0.265 | 0.7909 |  |
| **Site: UW (vs UAB)** | **-0.7154** | 0.2324 | ±0.4649 | **-3.078** | **0.0021** | ** |
| Season: spring (vs autumn) | -0.2617 | 0.2680 | ±0.5361 | -0.976 | 0.3289 |  |
| **Season: summer (vs autumn)** | **+2.0576** | 0.3509 | ±0.7017 | **+5.864** | **4.51e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2037** | 0.2660 | ±0.5319 | **-4.526** | **6.01e-06** | *** |
| Age (years) | +0.0189 | 0.0099 | ±0.0197 | +1.922 | 0.0546 | . |
| BMI (kg/m2) | -0.0116 | 0.0146 | ±0.0292 | -0.792 | 0.4285 |  |
| Hypertension | +0.0806 | 0.2183 | ±0.4367 | +0.369 | 0.7121 |  |
| High cholesterol | -0.1835 | 0.2171 | ±0.4342 | -0.845 | 0.3980 |  |
| **Kidney disease** | **+1.1514** | 0.4155 | ±0.8310 | **+2.771** | **0.0056** | ** |
| Circulatory disease | +0.0256 | 0.3107 | ±0.6215 | +0.082 | 0.9344 |  |
| Avg. daily mean/SD | +0.0342 | 0.0787 | ±0.1574 | +0.435 | 0.6635 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **400**, R² = **0.2789**, Adj R² = **0.2526**, F-statistic = **10.63** (p = **1.88e-20**), Residual SE = **1.982** on **385** df, AIC = **1697.0**, BIC = **1756.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5558** | 0.9292 | ±1.8583 | **+25.352** | **8.60e-142** | *** |
| Education: graduate level (vs college) | -0.0811 | 0.2178 | ±0.4356 | -0.372 | 0.7097 |  |
| Education: high school or below (vs college) | +0.4148 | 0.4313 | ±0.8625 | +0.962 | 0.3361 |  |
| Site: UCSD (vs UAB) | -0.0864 | 0.2636 | ±0.5273 | -0.328 | 0.7432 |  |
| **Site: UW (vs UAB)** | **-0.7039** | 0.2317 | ±0.4635 | **-3.038** | **0.0024** | ** |
| Season: spring (vs autumn) | -0.2551 | 0.2687 | ±0.5373 | -0.949 | 0.3424 |  |
| **Season: summer (vs autumn)** | **+2.0680** | 0.3505 | ±0.7009 | **+5.901** | **3.62e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2000** | 0.2656 | ±0.5312 | **-4.518** | **6.23e-06** | *** |
| Age (years) | +0.0182 | 0.0097 | ±0.0195 | +1.874 | 0.0610 | . |
| BMI (kg/m2) | -0.0120 | 0.0146 | ±0.0291 | -0.824 | 0.4098 |  |
| Hypertension | +0.0758 | 0.2193 | ±0.4386 | +0.345 | 0.7298 |  |
| High cholesterol | -0.1675 | 0.2169 | ±0.4339 | -0.772 | 0.4401 |  |
| **Kidney disease** | **+1.1228** | 0.4094 | ±0.8187 | **+2.743** | **0.0061** | ** |
| Circulatory disease | +0.0292 | 0.3130 | ±0.6259 | +0.093 | 0.9258 |  |
| MAG (mg/dL/h) | +0.0066 | 0.0126 | ±0.0252 | +0.520 | 0.6032 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **400**, R² = **0.2787**, Adj R² = **0.2524**, F-statistic = **10.62** (p = **1.96e-20**), Residual SE = **1.982** on **385** df, AIC = **1697.1**, BIC = **1756.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9689** | 0.8465 | ±1.6929 | **+28.317** | **2.15e-176** | *** |
| Education: graduate level (vs college) | -0.0800 | 0.2185 | ±0.4371 | -0.366 | 0.7142 |  |
| Education: high school or below (vs college) | +0.4162 | 0.4268 | ±0.8536 | +0.975 | 0.3295 |  |
| Site: UCSD (vs UAB) | -0.0751 | 0.2658 | ±0.5316 | -0.283 | 0.7775 |  |
| **Site: UW (vs UAB)** | **-0.7164** | 0.2324 | ±0.4648 | **-3.083** | **0.0021** | ** |
| Season: spring (vs autumn) | -0.2667 | 0.2695 | ±0.5390 | -0.990 | 0.3223 |  |
| **Season: summer (vs autumn)** | **+2.0576** | 0.3522 | ±0.7044 | **+5.842** | **5.16e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2097** | 0.2674 | ±0.5348 | **-4.524** | **6.06e-06** | *** |
| Age (years) | +0.0188 | 0.0097 | ±0.0194 | +1.938 | 0.0527 | . |
| BMI (kg/m2) | -0.0122 | 0.0144 | ±0.0289 | -0.846 | 0.3974 |  |
| Hypertension | +0.0838 | 0.2184 | ±0.4369 | +0.384 | 0.7013 |  |
| High cholesterol | -0.1845 | 0.2168 | ±0.4337 | -0.851 | 0.3949 |  |
| **Kidney disease** | **+1.1479** | 0.4192 | ±0.8383 | **+2.739** | **0.0062** | ** |
| Circulatory disease | +0.0251 | 0.3101 | ±0.6201 | +0.081 | 0.9355 |  |
| Avg. daily range (mg/dL) | -0.0016 | 0.0041 | ±0.0081 | -0.400 | 0.6893 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **400**, R² = **0.2789**, Adj R² = **0.2527**, F-statistic = **10.64** (p = **1.85e-20**), Residual SE = **1.981** on **385** df, AIC = **1696.9**, BIC = **1756.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9069** | 0.7820 | ±1.5639 | **+30.573** | **2.77e-205** | *** |
| Education: graduate level (vs college) | -0.0728 | 0.2200 | ±0.4400 | -0.331 | 0.7408 |  |
| Education: high school or below (vs college) | +0.3978 | 0.4271 | ±0.8541 | +0.931 | 0.3516 |  |
| Site: UCSD (vs UAB) | -0.0842 | 0.2642 | ±0.5285 | -0.319 | 0.7500 |  |
| **Site: UW (vs UAB)** | **-0.7180** | 0.2323 | ±0.4646 | **-3.091** | **0.0020** | ** |
| Season: spring (vs autumn) | -0.2557 | 0.2680 | ±0.5360 | -0.954 | 0.3400 |  |
| **Season: summer (vs autumn)** | **+2.0712** | 0.3506 | ±0.7012 | **+5.908** | **3.47e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2095** | 0.2684 | ±0.5367 | **-4.507** | **6.58e-06** | *** |
| Age (years) | +0.0183 | 0.0097 | ±0.0194 | +1.890 | 0.0587 | . |
| BMI (kg/m2) | -0.0113 | 0.0146 | ±0.0292 | -0.776 | 0.4379 |  |
| Hypertension | +0.0819 | 0.2189 | ±0.4378 | +0.374 | 0.7083 |  |
| High cholesterol | -0.1780 | 0.2178 | ±0.4357 | -0.817 | 0.4138 |  |
| **Kidney disease** | **+1.1331** | 0.4106 | ±0.8211 | **+2.760** | **0.0058** | ** |
| Circulatory disease | +0.0294 | 0.3114 | ±0.6229 | +0.094 | 0.9248 |  |
| SD of daily means (mg/dL) | -0.0146 | 0.0300 | ±0.0601 | -0.485 | 0.6278 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **400**, R² = **0.2788**, Adj R² = **0.2525**, F-statistic = **10.63** (p = **1.92e-20**), Residual SE = **1.982** on **385** df, AIC = **1697.0**, BIC = **1756.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.7344** | 2.0760 | ±4.1520 | **+11.915** | **9.93e-33** | *** |
| Education: graduate level (vs college) | -0.0805 | 0.2182 | ±0.4363 | -0.369 | 0.7120 |  |
| Education: high school or below (vs college) | +0.4142 | 0.4275 | ±0.8549 | +0.969 | 0.3326 |  |
| Site: UCSD (vs UAB) | -0.0755 | 0.2635 | ±0.5270 | -0.287 | 0.7743 |  |
| **Site: UW (vs UAB)** | **-0.7121** | 0.2313 | ±0.4626 | **-3.079** | **0.0021** | ** |
| Season: spring (vs autumn) | -0.2514 | 0.2698 | ±0.5395 | -0.932 | 0.3514 |  |
| **Season: summer (vs autumn)** | **+2.0730** | 0.3506 | ±0.7013 | **+5.912** | **3.38e-09** | *** |
| **Season: winter (vs autumn)** | **-1.1948** | 0.2681 | ±0.5361 | **-4.457** | **8.31e-06** | *** |
| Age (years) | +0.0178 | 0.0096 | ±0.0193 | +1.840 | 0.0657 | . |
| BMI (kg/m2) | -0.0121 | 0.0145 | ±0.0291 | -0.830 | 0.4065 |  |
| Hypertension | +0.0786 | 0.2184 | ±0.4368 | +0.360 | 0.7188 |  |
| High cholesterol | -0.1764 | 0.2173 | ±0.4346 | -0.812 | 0.4170 |  |
| **Kidney disease** | **+1.0953** | 0.4229 | ±0.8458 | **+2.590** | **0.0096** | ** |
| Circulatory disease | +0.0361 | 0.3115 | ±0.6231 | +0.116 | 0.9077 |  |
| Time in range 70-180, pooled (%) | -0.0093 | 0.0200 | ±0.0400 | -0.462 | 0.6438 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **400**, R² = **0.2786**, Adj R² = **0.2524**, F-statistic = **10.62** (p = **1.98e-20**), Residual SE = **1.982** on **385** df, AIC = **1697.1**, BIC = **1757.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5704** | 1.9999 | ±3.9997 | **+12.286** | **1.08e-34** | *** |
| Education: graduate level (vs college) | -0.0800 | 0.2182 | ±0.4364 | -0.367 | 0.7139 |  |
| Education: high school or below (vs college) | +0.4150 | 0.4275 | ±0.8550 | +0.971 | 0.3316 |  |
| Site: UCSD (vs UAB) | -0.0777 | 0.2636 | ±0.5272 | -0.295 | 0.7681 |  |
| **Site: UW (vs UAB)** | **-0.7131** | 0.2313 | ±0.4626 | **-3.083** | **0.0020** | ** |
| Season: spring (vs autumn) | -0.2538 | 0.2694 | ±0.5387 | -0.942 | 0.3461 |  |
| **Season: summer (vs autumn)** | **+2.0730** | 0.3510 | ±0.7021 | **+5.905** | **3.53e-09** | *** |
| **Season: winter (vs autumn)** | **-1.1965** | 0.2677 | ±0.5355 | **-4.469** | **7.86e-06** | *** |
| Age (years) | +0.0178 | 0.0097 | ±0.0193 | +1.840 | 0.0657 | . |
| BMI (kg/m2) | -0.0121 | 0.0146 | ±0.0291 | -0.833 | 0.4047 |  |
| Hypertension | +0.0791 | 0.2185 | ±0.4370 | +0.362 | 0.7175 |  |
| High cholesterol | -0.1780 | 0.2174 | ±0.4348 | -0.819 | 0.4130 |  |
| **Kidney disease** | **+1.1005** | 0.4219 | ±0.8439 | **+2.608** | **0.0091** | ** |
| Circulatory disease | +0.0345 | 0.3116 | ±0.6232 | +0.111 | 0.9118 |  |
| Avg. daily time in range 70-180 (%) | -0.0075 | 0.0189 | ±0.0377 | -0.397 | 0.6916 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **400**, R² = **0.2872**, Adj R² = **0.2613**, F-statistic = **11.08** (p = **2.36e-21**), Residual SE = **1.970** on **385** df, AIC = **1692.3**, BIC = **1752.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6289** | 0.7837 | ±1.5675 | **+30.149** | **1.09e-199** | *** |
| Education: graduate level (vs college) | -0.0736 | 0.2170 | ±0.4339 | -0.339 | 0.7346 |  |
| Education: high school or below (vs college) | +0.4532 | 0.4261 | ±0.8522 | +1.064 | 0.2875 |  |
| Site: UCSD (vs UAB) | +0.0046 | 0.2630 | ±0.5261 | +0.017 | 0.9862 |  |
| **Site: UW (vs UAB)** | **-0.6482** | 0.2324 | ±0.4647 | **-2.789** | **0.0053** | ** |
| Season: spring (vs autumn) | -0.2491 | 0.2669 | ±0.5337 | -0.933 | 0.3506 |  |
| **Season: summer (vs autumn)** | **+2.0225** | 0.3506 | ±0.7012 | **+5.769** | **7.98e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2275** | 0.2611 | ±0.5221 | **-4.702** | **2.58e-06** | *** |
| Age (years) | +0.0180 | 0.0097 | ±0.0193 | +1.859 | 0.0631 | . |
| BMI (kg/m2) | -0.0107 | 0.0143 | ±0.0285 | -0.752 | 0.4523 |  |
| Hypertension | +0.1117 | 0.2162 | ±0.4325 | +0.517 | 0.6054 |  |
| High cholesterol | -0.1337 | 0.2164 | ±0.4329 | -0.618 | 0.5368 |  |
| **Kidney disease** | **+1.1030** | 0.4072 | ±0.8144 | **+2.709** | **0.0068** | ** |
| Circulatory disease | +0.0503 | 0.3089 | ±0.6178 | +0.163 | 0.8706 |  |
| **Time < 54 (%)** | **+0.2347** | 0.0977 | ±0.1953 | **+2.404** | **0.0162** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **400**, R² = **0.2853**, Adj R² = **0.2593**, F-statistic = **10.98** (p = **3.81e-21**), Residual SE = **1.973** on **385** df, AIC = **1693.4**, BIC = **1753.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7258** | 0.7816 | ±1.5633 | **+30.354** | **2.23e-202** | *** |
| Education: graduate level (vs college) | -0.0637 | 0.2176 | ±0.4351 | -0.293 | 0.7696 |  |
| Education: high school or below (vs college) | +0.4550 | 0.4256 | ±0.8511 | +1.069 | 0.2850 |  |
| Site: UCSD (vs UAB) | -0.0164 | 0.2620 | ±0.5240 | -0.062 | 0.9502 |  |
| **Site: UW (vs UAB)** | **-0.6411** | 0.2322 | ±0.4645 | **-2.761** | **0.0058** | ** |
| Season: spring (vs autumn) | -0.2628 | 0.2666 | ±0.5333 | -0.986 | 0.3243 |  |
| **Season: summer (vs autumn)** | **+2.0253** | 0.3528 | ±0.7057 | **+5.740** | **9.47e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2434** | 0.2613 | ±0.5226 | **-4.759** | **1.95e-06** | *** |
| Age (years) | +0.0173 | 0.0097 | ±0.0195 | +1.773 | 0.0762 | . |
| BMI (kg/m2) | -0.0113 | 0.0144 | ±0.0287 | -0.789 | 0.4302 |  |
| Hypertension | +0.1214 | 0.2175 | ±0.4349 | +0.558 | 0.5768 |  |
| High cholesterol | -0.1413 | 0.2167 | ±0.4333 | -0.652 | 0.5144 |  |
| **Kidney disease** | **+1.1010** | 0.4040 | ±0.8080 | **+2.725** | **0.0064** | ** |
| Circulatory disease | +0.0522 | 0.3091 | ±0.6182 | +0.169 | 0.8660 |  |
| Avg. daily time < 54 (%) | +0.2746 | 0.1689 | ±0.3377 | +1.626 | 0.1040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **400**, R² = **0.2820**, Adj R² = **0.2559**, F-statistic = **10.80** (p = **8.54e-21**), Residual SE = **1.977** on **385** df, AIC = **1695.2**, BIC = **1755.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7154** | 0.7822 | ±1.5643 | **+30.320** | **6.26e-202** | *** |
| Education: graduate level (vs college) | -0.0686 | 0.2186 | ±0.4372 | -0.314 | 0.7536 |  |
| Education: high school or below (vs college) | +0.4537 | 0.4267 | ±0.8534 | +1.063 | 0.2877 |  |
| Site: UCSD (vs UAB) | -0.0550 | 0.2646 | ±0.5293 | -0.208 | 0.8355 |  |
| **Site: UW (vs UAB)** | **-0.6775** | 0.2330 | ±0.4660 | **-2.908** | **0.0036** | ** |
| Season: spring (vs autumn) | -0.2702 | 0.2674 | ±0.5348 | -1.011 | 0.3122 |  |
| **Season: summer (vs autumn)** | **+2.0495** | 0.3498 | ±0.6995 | **+5.860** | **4.63e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2448** | 0.2655 | ±0.5310 | **-4.688** | **2.76e-06** | *** |
| Age (years) | +0.0183 | 0.0097 | ±0.0194 | +1.889 | 0.0588 | . |
| BMI (kg/m2) | -0.0128 | 0.0144 | ±0.0288 | -0.891 | 0.3728 |  |
| Hypertension | +0.1091 | 0.2181 | ±0.4362 | +0.500 | 0.6170 |  |
| High cholesterol | -0.1560 | 0.2182 | ±0.4364 | -0.715 | 0.4745 |  |
| **Kidney disease** | **+1.1241** | 0.4039 | ±0.8079 | **+2.783** | **0.0054** | ** |
| Circulatory disease | +0.0415 | 0.3100 | ±0.6200 | +0.134 | 0.8935 |  |
| Time 54-69, pooled (%) | +0.0670 | 0.0355 | ±0.0709 | +1.889 | 0.0589 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **400**, R² = **0.2829**, Adj R² = **0.2568**, F-statistic = **10.85** (p = **6.96e-21**), Residual SE = **1.976** on **385** df, AIC = **1694.7**, BIC = **1754.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7397** | 0.7781 | ±1.5562 | **+30.509** | **1.96e-204** | *** |
| Education: graduate level (vs college) | -0.0632 | 0.2186 | ±0.4373 | -0.289 | 0.7725 |  |
| Education: high school or below (vs college) | +0.4647 | 0.4269 | ±0.8538 | +1.089 | 0.2763 |  |
| Site: UCSD (vs UAB) | -0.0595 | 0.2640 | ±0.5280 | -0.225 | 0.8217 |  |
| **Site: UW (vs UAB)** | **-0.6709** | 0.2327 | ±0.4653 | **-2.884** | **0.0039** | ** |
| Season: spring (vs autumn) | -0.2735 | 0.2671 | ±0.5342 | -1.024 | 0.3058 |  |
| **Season: summer (vs autumn)** | **+2.0545** | 0.3493 | ±0.6986 | **+5.882** | **4.06e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2524** | 0.2655 | ±0.5310 | **-4.717** | **2.39e-06** | *** |
| Age (years) | +0.0181 | 0.0097 | ±0.0194 | +1.863 | 0.0624 | . |
| BMI (kg/m2) | -0.0131 | 0.0144 | ±0.0289 | -0.906 | 0.3649 |  |
| Hypertension | +0.1143 | 0.2181 | ±0.4362 | +0.524 | 0.6002 |  |
| High cholesterol | -0.1550 | 0.2177 | ±0.4355 | -0.712 | 0.4767 |  |
| **Kidney disease** | **+1.1257** | 0.4035 | ±0.8069 | **+2.790** | **0.0053** | ** |
| Circulatory disease | +0.0396 | 0.3096 | ±0.6193 | +0.128 | 0.8982 |  |
| **Avg. daily time 54-69 (%)** | **+0.0724** | 0.0358 | ±0.0716 | **+2.021** | **0.0433** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **400**, R² = **0.2850**, Adj R² = **0.2590**, F-statistic = **10.96** (p = **4.14e-21**), Residual SE = **1.973** on **385** df, AIC = **1693.6**, BIC = **1753.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6467** | 0.7840 | ±1.5680 | **+30.161** | **7.62e-200** | *** |
| Education: graduate level (vs college) | -0.0658 | 0.2179 | ±0.4359 | -0.302 | 0.7627 |  |
| Education: high school or below (vs college) | +0.4686 | 0.4258 | ±0.8516 | +1.100 | 0.2712 |  |
| Site: UCSD (vs UAB) | -0.0272 | 0.2638 | ±0.5276 | -0.103 | 0.9178 |  |
| **Site: UW (vs UAB)** | **-0.6540** | 0.2323 | ±0.4645 | **-2.816** | **0.0049** | ** |
| Season: spring (vs autumn) | -0.2671 | 0.2670 | ±0.5339 | -1.000 | 0.3171 |  |
| **Season: summer (vs autumn)** | **+2.0360** | 0.3503 | ±0.7006 | **+5.812** | **6.18e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2544** | 0.2631 | ±0.5262 | **-4.767** | **1.87e-06** | *** |
| Age (years) | +0.0183 | 0.0097 | ±0.0194 | +1.887 | 0.0592 | . |
| BMI (kg/m2) | -0.0125 | 0.0143 | ±0.0286 | -0.875 | 0.3814 |  |
| Hypertension | +0.1203 | 0.2173 | ±0.4346 | +0.554 | 0.5799 |  |
| High cholesterol | -0.1408 | 0.2176 | ±0.4353 | -0.647 | 0.5177 |  |
| **Kidney disease** | **+1.1172** | 0.4027 | ±0.8055 | **+2.774** | **0.0055** | ** |
| Circulatory disease | +0.0492 | 0.3092 | ±0.6183 | +0.159 | 0.8734 |  |
| **Time < 70 (%)** | **+0.0711** | 0.0328 | ±0.0657 | **+2.165** | **0.0304** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **400**, R² = **0.2845**, Adj R² = **0.2585**, F-statistic = **10.93** (p = **4.65e-21**), Residual SE = **1.974** on **385** df, AIC = **1693.8**, BIC = **1753.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7155** | 0.7789 | ±1.5579 | **+30.446** | **1.34e-203** | *** |
| Education: graduate level (vs college) | -0.0595 | 0.2182 | ±0.4363 | -0.273 | 0.7851 |  |
| Education: high school or below (vs college) | +0.4739 | 0.4263 | ±0.8526 | +1.112 | 0.2663 |  |
| Site: UCSD (vs UAB) | -0.0436 | 0.2633 | ±0.5267 | -0.165 | 0.8686 |  |
| **Site: UW (vs UAB)** | **-0.6529** | 0.2319 | ±0.4639 | **-2.815** | **0.0049** | ** |
| Season: spring (vs autumn) | -0.2735 | 0.2668 | ±0.5335 | -1.025 | 0.3052 |  |
| **Season: summer (vs autumn)** | **+2.0448** | 0.3504 | ±0.7009 | **+5.835** | **5.38e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2608** | 0.2636 | ±0.5273 | **-4.782** | **1.73e-06** | *** |
| Age (years) | +0.0178 | 0.0097 | ±0.0194 | +1.841 | 0.0656 | . |
| BMI (kg/m2) | -0.0129 | 0.0144 | ±0.0288 | -0.895 | 0.3708 |  |
| Hypertension | +0.1236 | 0.2177 | ±0.4354 | +0.568 | 0.5701 |  |
| High cholesterol | -0.1460 | 0.2173 | ±0.4347 | -0.672 | 0.5017 |  |
| **Kidney disease** | **+1.1194** | 0.4020 | ±0.8040 | **+2.785** | **0.0054** | ** |
| Circulatory disease | +0.0455 | 0.3091 | ±0.6182 | +0.147 | 0.8830 |  |
| **Avg. daily time < 70 (%)** | **+0.0700** | 0.0338 | ±0.0677 | **+2.069** | **0.0385** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **400**, R² = **0.2828**, Adj R² = **0.2567**, F-statistic = **10.84** (p = **7.17e-21**), Residual SE = **1.976** on **385** df, AIC = **1694.8**, BIC = **1754.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+36.6288** | 10.4823 | ±20.9646 | **+3.494** | **4.75e-04** | *** |
| Education: graduate level (vs college) | -0.0761 | 0.2175 | ±0.4350 | -0.350 | 0.7263 |  |
| Education: high school or below (vs college) | +0.4353 | 0.4273 | ±0.8546 | +1.019 | 0.3083 |  |
| Site: UCSD (vs UAB) | -0.0335 | 0.2637 | ±0.5275 | -0.127 | 0.8989 |  |
| **Site: UW (vs UAB)** | **-0.6727** | 0.2322 | ±0.4644 | **-2.897** | **0.0038** | ** |
| Season: spring (vs autumn) | -0.2565 | 0.2681 | ±0.5361 | -0.957 | 0.3386 |  |
| **Season: summer (vs autumn)** | **+2.0514** | 0.3499 | ±0.6997 | **+5.864** | **4.53e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2029** | 0.2638 | ±0.5276 | **-4.560** | **5.11e-06** | *** |
| Age (years) | +0.0173 | 0.0097 | ±0.0193 | +1.790 | 0.0734 | . |
| BMI (kg/m2) | -0.0112 | 0.0144 | ±0.0289 | -0.777 | 0.4371 |  |
| Hypertension | +0.0915 | 0.2173 | ±0.4346 | +0.421 | 0.6737 |  |
| High cholesterol | -0.1455 | 0.2170 | ±0.4340 | -0.670 | 0.5026 |  |
| **Kidney disease** | **+1.0423** | 0.4196 | ±0.8391 | **+2.484** | **0.0130** | * |
| Circulatory disease | +0.0526 | 0.3108 | ±0.6217 | +0.169 | 0.8657 |  |
| Time 54-250, pooled (%) | -0.1289 | 0.1050 | ±0.2099 | -1.228 | 0.2193 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **400**, R² = **0.2807**, Adj R² = **0.2545**, F-statistic = **10.73** (p = **1.21e-20**), Residual SE = **1.979** on **385** df, AIC = **1696.0**, BIC = **1755.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+34.3823** | 12.0236 | ±24.0472 | **+2.860** | **0.0042** | ** |
| Education: graduate level (vs college) | -0.0727 | 0.2177 | ±0.4354 | -0.334 | 0.7383 |  |
| Education: high school or below (vs college) | +0.4310 | 0.4277 | ±0.8555 | +1.008 | 0.3137 |  |
| Site: UCSD (vs UAB) | -0.0535 | 0.2635 | ±0.5269 | -0.203 | 0.8390 |  |
| **Site: UW (vs UAB)** | **-0.6834** | 0.2317 | ±0.4635 | **-2.949** | **0.0032** | ** |
| Season: spring (vs autumn) | -0.2636 | 0.2682 | ±0.5365 | -0.983 | 0.3258 |  |
| **Season: summer (vs autumn)** | **+2.0570** | 0.3507 | ±0.7013 | **+5.866** | **4.46e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2069** | 0.2645 | ±0.5289 | **-4.564** | **5.03e-06** | *** |
| Age (years) | +0.0172 | 0.0097 | ±0.0194 | +1.769 | 0.0769 | . |
| BMI (kg/m2) | -0.0118 | 0.0145 | ±0.0291 | -0.812 | 0.4169 |  |
| Hypertension | +0.0921 | 0.2176 | ±0.4352 | +0.423 | 0.6723 |  |
| High cholesterol | -0.1601 | 0.2170 | ±0.4339 | -0.738 | 0.4606 |  |
| **Kidney disease** | **+1.0543** | 0.4231 | ±0.8462 | **+2.492** | **0.0127** | * |
| Circulatory disease | +0.0487 | 0.3117 | ±0.6233 | +0.156 | 0.8759 |  |
| Avg. daily time 54-250 (%) | -0.1057 | 0.1196 | ±0.2393 | -0.884 | 0.3768 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **400**, R² = **0.2790**, Adj R² = **0.2528**, F-statistic = **10.64** (p = **1.82e-20**), Residual SE = **1.981** on **385** df, AIC = **1696.9**, BIC = **1756.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8325** | 0.7747 | ±1.5494 | **+30.764** | **8.06e-208** | *** |
| Education: graduate level (vs college) | -0.0775 | 0.2183 | ±0.4366 | -0.355 | 0.7227 |  |
| Education: high school or below (vs college) | +0.4210 | 0.4286 | ±0.8573 | +0.982 | 0.3260 |  |
| Site: UCSD (vs UAB) | -0.0800 | 0.2649 | ±0.5297 | -0.302 | 0.7627 |  |
| **Site: UW (vs UAB)** | **-0.7128** | 0.2334 | ±0.4668 | **-3.054** | **0.0023** | ** |
| Season: spring (vs autumn) | -0.2780 | 0.2725 | ±0.5451 | -1.020 | 0.3077 |  |
| **Season: summer (vs autumn)** | **+2.0463** | 0.3540 | ±0.7079 | **+5.781** | **7.42e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2271** | 0.2728 | ±0.5456 | **-4.498** | **6.85e-06** | *** |
| Age (years) | +0.0187 | 0.0097 | ±0.0193 | +1.934 | 0.0531 | . |
| BMI (kg/m2) | -0.0118 | 0.0144 | ±0.0289 | -0.820 | 0.4121 |  |
| Hypertension | +0.0907 | 0.2186 | ±0.4373 | +0.415 | 0.6782 |  |
| High cholesterol | -0.1752 | 0.2179 | ±0.4358 | -0.804 | 0.4213 |  |
| **Kidney disease** | **+1.1624** | 0.4255 | ±0.8509 | **+2.732** | **0.0063** | ** |
| Circulatory disease | +0.0202 | 0.3097 | ±0.6194 | +0.065 | 0.9480 |  |
| Time 181-250, pooled (%) | -0.0143 | 0.0255 | ±0.0510 | -0.560 | 0.5758 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **400**, R² = **0.2789**, Adj R² = **0.2527**, F-statistic = **10.64** (p = **1.83e-20**), Residual SE = **1.981** on **385** df, AIC = **1696.9**, BIC = **1756.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8306** | 0.7745 | ±1.5489 | **+30.770** | **6.58e-208** | *** |
| Education: graduate level (vs college) | -0.0772 | 0.2183 | ±0.4367 | -0.354 | 0.7235 |  |
| Education: high school or below (vs college) | +0.4198 | 0.4282 | ±0.8564 | +0.980 | 0.3270 |  |
| Site: UCSD (vs UAB) | -0.0809 | 0.2647 | ±0.5295 | -0.306 | 0.7600 |  |
| **Site: UW (vs UAB)** | **-0.7129** | 0.2334 | ±0.4668 | **-3.054** | **0.0023** | ** |
| Season: spring (vs autumn) | -0.2774 | 0.2724 | ±0.5448 | -1.018 | 0.3086 |  |
| **Season: summer (vs autumn)** | **+2.0459** | 0.3543 | ±0.7085 | **+5.775** | **7.69e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2272** | 0.2728 | ±0.5455 | **-4.499** | **6.82e-06** | *** |
| Age (years) | +0.0187 | 0.0097 | ±0.0193 | +1.932 | 0.0534 | . |
| BMI (kg/m2) | -0.0118 | 0.0144 | ±0.0289 | -0.816 | 0.4143 |  |
| Hypertension | +0.0909 | 0.2189 | ±0.4377 | +0.415 | 0.6780 |  |
| High cholesterol | -0.1749 | 0.2179 | ±0.4358 | -0.803 | 0.4222 |  |
| **Kidney disease** | **+1.1611** | 0.4251 | ±0.8501 | **+2.732** | **0.0063** | ** |
| Circulatory disease | +0.0201 | 0.3097 | ±0.6194 | +0.065 | 0.9481 |  |
| Avg. daily time 181-250 (%) | -0.0134 | 0.0246 | ±0.0493 | -0.546 | 0.5854 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **400**, R² = **0.2789**, Adj R² = **0.2527**, F-statistic = **10.64** (p = **1.85e-20**), Residual SE = **1.981** on **385** df, AIC = **1696.9**, BIC = **1756.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8311** | 0.7749 | ±1.5498 | **+30.754** | **1.08e-207** | *** |
| Education: graduate level (vs college) | -0.0780 | 0.2184 | ±0.4368 | -0.357 | 0.7210 |  |
| Education: high school or below (vs college) | +0.4196 | 0.4283 | ±0.8566 | +0.980 | 0.3272 |  |
| Site: UCSD (vs UAB) | -0.0803 | 0.2649 | ±0.5298 | -0.303 | 0.7618 |  |
| **Site: UW (vs UAB)** | **-0.7142** | 0.2332 | ±0.4663 | **-3.063** | **0.0022** | ** |
| Season: spring (vs autumn) | -0.2752 | 0.2717 | ±0.5435 | -1.013 | 0.3112 |  |
| **Season: summer (vs autumn)** | **+2.0482** | 0.3536 | ±0.7071 | **+5.793** | **6.91e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2248** | 0.2721 | ±0.5443 | **-4.501** | **6.77e-06** | *** |
| Age (years) | +0.0187 | 0.0097 | ±0.0193 | +1.932 | 0.0534 | . |
| BMI (kg/m2) | -0.0119 | 0.0145 | ±0.0289 | -0.821 | 0.4115 |  |
| Hypertension | +0.0897 | 0.2186 | ±0.4372 | +0.410 | 0.6816 |  |
| High cholesterol | -0.1767 | 0.2177 | ±0.4354 | -0.812 | 0.4170 |  |
| **Kidney disease** | **+1.1632** | 0.4271 | ±0.8542 | **+2.723** | **0.0065** | ** |
| Circulatory disease | +0.0202 | 0.3099 | ±0.6198 | +0.065 | 0.9480 |  |
| Time > 180 (%) | -0.0120 | 0.0231 | ±0.0462 | -0.521 | 0.6024 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **400**, R² = **0.2789**, Adj R² = **0.2527**, F-statistic = **10.64** (p = **1.86e-20**), Residual SE = **1.982** on **385** df, AIC = **1696.9**, BIC = **1756.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8289** | 0.7747 | ±1.5493 | **+30.760** | **8.94e-208** | *** |
| Education: graduate level (vs college) | -0.0779 | 0.2184 | ±0.4369 | -0.357 | 0.7213 |  |
| Education: high school or below (vs college) | +0.4183 | 0.4278 | ±0.8557 | +0.978 | 0.3282 |  |
| Site: UCSD (vs UAB) | -0.0813 | 0.2647 | ±0.5295 | -0.307 | 0.7587 |  |
| **Site: UW (vs UAB)** | **-0.7142** | 0.2332 | ±0.4665 | **-3.062** | **0.0022** | ** |
| Season: spring (vs autumn) | -0.2745 | 0.2717 | ±0.5433 | -1.011 | 0.3122 |  |
| **Season: summer (vs autumn)** | **+2.0482** | 0.3538 | ±0.7076 | **+5.789** | **7.06e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2247** | 0.2722 | ±0.5443 | **-4.500** | **6.80e-06** | *** |
| Age (years) | +0.0186 | 0.0097 | ±0.0193 | +1.930 | 0.0536 | . |
| BMI (kg/m2) | -0.0118 | 0.0145 | ±0.0289 | -0.817 | 0.4140 |  |
| Hypertension | +0.0896 | 0.2189 | ±0.4377 | +0.409 | 0.6822 |  |
| High cholesterol | -0.1761 | 0.2177 | ±0.4355 | -0.809 | 0.4186 |  |
| **Kidney disease** | **+1.1617** | 0.4266 | ±0.8531 | **+2.723** | **0.0065** | ** |
| Circulatory disease | +0.0202 | 0.3099 | ±0.6198 | +0.065 | 0.9481 |  |
| Avg. daily time > 180 (%) | -0.0112 | 0.0225 | ±0.0450 | -0.498 | 0.6188 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **400**, R² = **0.2804**, Adj R² = **0.2542**, F-statistic = **10.72** (p = **1.28e-20**), Residual SE = **1.979** on **385** df, AIC = **1696.1**, BIC = **1756.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8083** | 0.7712 | ±1.5423 | **+30.873** | **2.74e-209** | *** |
| Education: graduate level (vs college) | -0.0903 | 0.2189 | ±0.4378 | -0.412 | 0.6800 |  |
| Education: high school or below (vs college) | +0.4320 | 0.4298 | ±0.8595 | +1.005 | 0.3148 |  |
| Site: UCSD (vs UAB) | -0.0863 | 0.2646 | ±0.5293 | -0.326 | 0.7443 |  |
| **Site: UW (vs UAB)** | **-0.7167** | 0.2323 | ±0.4647 | **-3.085** | **0.0020** | ** |
| Season: spring (vs autumn) | -0.2788 | 0.2696 | ±0.5392 | -1.034 | 0.3012 |  |
| **Season: summer (vs autumn)** | **+2.0262** | 0.3540 | ±0.7080 | **+5.724** | **1.04e-08** | *** |
| **Season: winter (vs autumn)** | **-1.2279** | 0.2702 | ±0.5404 | **-4.544** | **5.51e-06** | *** |
| Age (years) | +0.0188 | 0.0096 | ±0.0192 | +1.950 | 0.0511 | . |
| BMI (kg/m2) | -0.0107 | 0.0145 | ±0.0290 | -0.739 | 0.4597 |  |
| Hypertension | +0.0991 | 0.2185 | ±0.4371 | +0.453 | 0.6503 |  |
| High cholesterol | -0.1800 | 0.2171 | ±0.4343 | -0.829 | 0.4071 |  |
| **Kidney disease** | **+1.1272** | 0.4118 | ±0.8235 | **+2.738** | **0.0062** | ** |
| Circulatory disease | +0.0018 | 0.3097 | ±0.6193 | +0.006 | 0.9953 |  |
| Nocturnal time > 180 (%) | -0.0231 | 0.0243 | ±0.0487 | -0.951 | 0.3417 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **400**, R² = **0.2785**, Adj R² = **0.2523**, F-statistic = **10.61** (p = **2.05e-20**), Residual SE = **1.982** on **385** df, AIC = **1697.2**, BIC = **1757.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8405** | 0.7796 | ±1.5592 | **+30.580** | **2.25e-205** | *** |
| Education: graduate level (vs college) | -0.0829 | 0.2190 | ±0.4380 | -0.379 | 0.7050 |  |
| Education: high school or below (vs college) | +0.4110 | 0.4272 | ±0.8544 | +0.962 | 0.3360 |  |
| Site: UCSD (vs UAB) | -0.0765 | 0.2651 | ±0.5302 | -0.289 | 0.7729 |  |
| **Site: UW (vs UAB)** | **-0.7177** | 0.2320 | ±0.4640 | **-3.094** | **0.0020** | ** |
| Season: spring (vs autumn) | -0.2670 | 0.2719 | ±0.5437 | -0.982 | 0.3261 |  |
| **Season: summer (vs autumn)** | **+2.0590** | 0.3540 | ±0.7080 | **+5.816** | **6.01e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2092** | 0.2695 | ±0.5389 | **-4.488** | **7.20e-06** | *** |
| Age (years) | +0.0184 | 0.0096 | ±0.0192 | +1.914 | 0.0556 | . |
| BMI (kg/m2) | -0.0122 | 0.0145 | ±0.0290 | -0.839 | 0.4016 |  |
| Hypertension | +0.0838 | 0.2179 | ±0.4359 | +0.384 | 0.7007 |  |
| High cholesterol | -0.1809 | 0.2174 | ±0.4349 | -0.832 | 0.4054 |  |
| **Kidney disease** | **+1.1345** | 0.4157 | ±0.8315 | **+2.729** | **0.0064** | ** |
| Circulatory disease | +0.0241 | 0.3107 | ±0.6214 | +0.078 | 0.9381 |  |
| Any reading > 250 during wear (0/1) | -0.0781 | 0.2996 | ±0.5991 | -0.261 | 0.7944 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **400**, R² = **0.2785**, Adj R² = **0.2522**, F-statistic = **10.61** (p = **2.06e-20**), Residual SE = **1.982** on **385** df, AIC = **1697.2**, BIC = **1757.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8279** | 0.7768 | ±1.5536 | **+30.675** | **1.22e-206** | *** |
| Education: graduate level (vs college) | -0.0807 | 0.2189 | ±0.4378 | -0.369 | 0.7124 |  |
| Education: high school or below (vs college) | +0.4122 | 0.4271 | ±0.8543 | +0.965 | 0.3345 |  |
| Site: UCSD (vs UAB) | -0.0819 | 0.2647 | ±0.5295 | -0.309 | 0.7572 |  |
| **Site: UW (vs UAB)** | **-0.7198** | 0.2319 | ±0.4637 | **-3.104** | **0.0019** | ** |
| Season: spring (vs autumn) | -0.2607 | 0.2683 | ±0.5366 | -0.972 | 0.3311 |  |
| **Season: summer (vs autumn)** | **+2.0612** | 0.3504 | ±0.7009 | **+5.882** | **4.06e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2085** | 0.2669 | ±0.5337 | **-4.528** | **5.94e-06** | *** |
| Age (years) | +0.0184 | 0.0097 | ±0.0194 | +1.895 | 0.0581 | . |
| BMI (kg/m2) | -0.0120 | 0.0145 | ±0.0290 | -0.825 | 0.4096 |  |
| Hypertension | +0.0824 | 0.2183 | ±0.4367 | +0.377 | 0.7058 |  |
| High cholesterol | -0.1821 | 0.2183 | ±0.4366 | -0.834 | 0.4043 |  |
| **Kidney disease** | **+1.1472** | 0.4289 | ±0.8579 | **+2.675** | **0.0075** | ** |
| Circulatory disease | +0.0238 | 0.3114 | ±0.6227 | +0.076 | 0.9392 |  |
| Time > 250 (%) | -0.0398 | 0.1728 | ±0.3456 | -0.230 | 0.8179 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 400)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **400**, R² = **0.2785**, Adj R² = **0.2522**, F-statistic = **10.61** (p = **2.07e-20**), Residual SE = **1.982** on **385** df, AIC = **1697.2**, BIC = **1757.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8264** | 0.7769 | ±1.5539 | **+30.667** | **1.58e-206** | *** |
| Education: graduate level (vs college) | -0.0809 | 0.2193 | ±0.4385 | -0.369 | 0.7120 |  |
| Education: high school or below (vs college) | +0.4117 | 0.4271 | ±0.8541 | +0.964 | 0.3350 |  |
| Site: UCSD (vs UAB) | -0.0825 | 0.2645 | ±0.5291 | -0.312 | 0.7550 |  |
| **Site: UW (vs UAB)** | **-0.7192** | 0.2321 | ±0.4641 | **-3.099** | **0.0019** | ** |
| Season: spring (vs autumn) | -0.2608 | 0.2684 | ±0.5368 | -0.972 | 0.3312 |  |
| **Season: summer (vs autumn)** | **+2.0619** | 0.3503 | ±0.7005 | **+5.887** | **3.94e-09** | *** |
| **Season: winter (vs autumn)** | **-1.2080** | 0.2669 | ±0.5337 | **-4.527** | **5.99e-06** | *** |
| Age (years) | +0.0184 | 0.0097 | ±0.0194 | +1.893 | 0.0583 | . |
| BMI (kg/m2) | -0.0119 | 0.0145 | ±0.0290 | -0.821 | 0.4116 |  |
| Hypertension | +0.0818 | 0.2184 | ±0.4369 | +0.375 | 0.7079 |  |
| High cholesterol | -0.1808 | 0.2184 | ±0.4367 | -0.828 | 0.4076 |  |
| **Kidney disease** | **+1.1448** | 0.4275 | ±0.8551 | **+2.678** | **0.0074** | ** |
| Circulatory disease | +0.0240 | 0.3114 | ±0.6228 | +0.077 | 0.9386 |  |
| Avg. daily time > 250 (%) | -0.0332 | 0.1787 | ±0.3575 | -0.186 | 0.8527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 400; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **400**, R² = **0.2722**, Adj R² = **0.2477**, F-statistic = **11.11** (p = **2.76e-20**), Residual SE = **5.953** on **386** df, AIC = **2576.1**, BIC = **2631.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4654** | 2.4938 | ±4.9876 | **+19.835** | **1.48e-87** | *** |
| Education: graduate level (vs college) | +0.7688 | 0.6584 | ±1.3168 | +1.168 | 0.2429 |  |
| Education: high school or below (vs college) | +1.9284 | 1.4450 | ±2.8901 | +1.334 | 0.1820 |  |
| **Site: UCSD (vs UAB)** | **+2.0236** | 0.8837 | ±1.7673 | **+2.290** | **0.0220** | * |
| **Site: UW (vs UAB)** | **-2.2782** | 0.6897 | ±1.3793 | **-3.303** | **9.56e-04** | *** |
| **Season: spring (vs autumn)** | **-2.7772** | 0.8363 | ±1.6727 | **-3.321** | **8.98e-04** | *** |
| Season: summer (vs autumn) | +1.1489 | 0.9613 | ±1.9226 | +1.195 | 0.2320 |  |
| **Season: winter (vs autumn)** | **-6.5171** | 0.8861 | ±1.7722 | **-7.355** | **1.91e-13** | *** |
| Age (years) | -0.0489 | 0.0294 | ±0.0588 | -1.663 | 0.0963 | . |
| BMI (kg/m2) | -0.0080 | 0.0496 | ±0.0991 | -0.160 | 0.8725 |  |
| Hypertension | +0.6279 | 0.6771 | ±1.3542 | +0.927 | 0.3538 |  |
| High cholesterol | -0.4175 | 0.6443 | ±1.2886 | -0.648 | 0.5170 |  |
| Kidney disease | +0.1452 | 1.2236 | ±2.4472 | +0.119 | 0.9056 |  |
| **Circulatory disease** | **+1.9641** | 0.9091 | ±1.8182 | **+2.161** | **0.0307** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **400**, R² = **0.2795**, Adj R² = **0.2533**, F-statistic = **10.67** (p = **1.60e-20**), Residual SE = **5.931** on **385** df, AIC = **2574.0**, BIC = **2633.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.1658** | 4.4845 | ±8.9691 | **+9.402** | **5.33e-21** | *** |
| Education: graduate level (vs college) | +0.8125 | 0.6574 | ±1.3149 | +1.236 | 0.2165 |  |
| Education: high school or below (vs college) | +1.7238 | 1.4589 | ±2.9178 | +1.182 | 0.2374 |  |
| **Site: UCSD (vs UAB)** | **+1.8050** | 0.8923 | ±1.7846 | **+2.023** | **0.0431** | * |
| **Site: UW (vs UAB)** | **-2.3321** | 0.6904 | ±1.3808 | **-3.378** | **7.30e-04** | *** |
| **Season: spring (vs autumn)** | **-2.5621** | 0.8424 | ±1.6848 | **-3.041** | **0.0024** | ** |
| Season: summer (vs autumn) | +1.1815 | 0.9544 | ±1.9089 | +1.238 | 0.2158 |  |
| **Season: winter (vs autumn)** | **-6.4227** | 0.8816 | ±1.7632 | **-7.285** | **3.21e-13** | *** |
| **Age (years)** | **-0.0587** | 0.0295 | ±0.0591 | **-1.986** | **0.0471** | * |
| BMI (kg/m2) | -0.0206 | 0.0489 | ±0.0979 | -0.420 | 0.6744 |  |
| Hypertension | +0.6476 | 0.6781 | ±1.3563 | +0.955 | 0.3396 |  |
| High cholesterol | -0.6191 | 0.6539 | ±1.3078 | -0.947 | 0.3437 |  |
| Kidney disease | +0.0715 | 1.2601 | ±2.5203 | +0.057 | 0.9548 |  |
| **Circulatory disease** | **+2.0461** | 0.9025 | ±1.8050 | **+2.267** | **0.0234** | * |
| HbA1c (%) | +1.4706 | 0.7630 | ±1.5259 | +1.927 | 0.0539 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **400**, R² = **0.2724**, Adj R² = **0.2459**, F-statistic = **10.29** (p = **9.12e-20**), Residual SE = **5.960** on **385** df, AIC = **2578.0**, BIC = **2637.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1248** | 3.4003 | ±6.8005 | **+14.742** | **3.49e-49** | *** |
| Education: graduate level (vs college) | +0.7807 | 0.6596 | ±1.3192 | +1.184 | 0.2366 |  |
| Education: high school or below (vs college) | +1.9521 | 1.4564 | ±2.9127 | +1.340 | 0.1801 |  |
| **Site: UCSD (vs UAB)** | **+2.0292** | 0.8867 | ±1.7733 | **+2.289** | **0.0221** | * |
| **Site: UW (vs UAB)** | **-2.2569** | 0.6994 | ±1.3988 | **-3.227** | **0.0013** | ** |
| **Season: spring (vs autumn)** | **-2.7929** | 0.8411 | ±1.6822 | **-3.321** | **8.98e-04** | *** |
| Season: summer (vs autumn) | +1.1332 | 0.9616 | ±1.9233 | +1.178 | 0.2386 |  |
| **Season: winter (vs autumn)** | **-6.5478** | 0.8828 | ±1.7656 | **-7.417** | **1.20e-13** | *** |
| Age (years) | -0.0483 | 0.0296 | ±0.0592 | -1.633 | 0.1024 |  |
| BMI (kg/m2) | -0.0075 | 0.0498 | ±0.0997 | -0.150 | 0.8811 |  |
| Hypertension | +0.6475 | 0.6912 | ±1.3823 | +0.937 | 0.3488 |  |
| High cholesterol | -0.3978 | 0.6575 | ±1.3150 | -0.605 | 0.5452 |  |
| Kidney disease | +0.1817 | 1.2326 | ±2.4652 | +0.147 | 0.8828 |  |
| **Circulatory disease** | **+1.9588** | 0.9129 | ±1.8258 | **+2.146** | **0.0319** | * |
| Mean glucose (mg/dL) | -0.0063 | 0.0234 | ±0.0467 | -0.271 | 0.7862 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **400**, R² = **0.2724**, Adj R² = **0.2459**, F-statistic = **10.29** (p = **9.12e-20**), Residual SE = **5.960** on **385** df, AIC = **2578.0**, BIC = **2637.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0016** | 6.0732 | ±12.1464 | **+8.398** | **4.55e-17** | *** |
| Education: graduate level (vs college) | +0.7807 | 0.6596 | ±1.3192 | +1.184 | 0.2366 |  |
| Education: high school or below (vs college) | +1.9521 | 1.4564 | ±2.9127 | +1.340 | 0.1801 |  |
| **Site: UCSD (vs UAB)** | **+2.0292** | 0.8867 | ±1.7733 | **+2.289** | **0.0221** | * |
| **Site: UW (vs UAB)** | **-2.2569** | 0.6994 | ±1.3988 | **-3.227** | **0.0013** | ** |
| **Season: spring (vs autumn)** | **-2.7929** | 0.8411 | ±1.6822 | **-3.321** | **8.98e-04** | *** |
| Season: summer (vs autumn) | +1.1332 | 0.9616 | ±1.9233 | +1.178 | 0.2386 |  |
| **Season: winter (vs autumn)** | **-6.5478** | 0.8828 | ±1.7656 | **-7.417** | **1.20e-13** | *** |
| Age (years) | -0.0483 | 0.0296 | ±0.0592 | -1.633 | 0.1024 |  |
| BMI (kg/m2) | -0.0075 | 0.0498 | ±0.0997 | -0.150 | 0.8811 |  |
| Hypertension | +0.6475 | 0.6912 | ±1.3823 | +0.937 | 0.3488 |  |
| High cholesterol | -0.3978 | 0.6575 | ±1.3150 | -0.605 | 0.5452 |  |
| Kidney disease | +0.1817 | 1.2326 | ±2.4652 | +0.147 | 0.8828 |  |
| **Circulatory disease** | **+1.9588** | 0.9129 | ±1.8258 | **+2.146** | **0.0319** | * |
| GMI (%) | -0.2649 | 0.9763 | ±1.9527 | -0.271 | 0.7862 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **400**, R² = **0.2723**, Adj R² = **0.2458**, F-statistic = **10.29** (p = **9.36e-20**), Residual SE = **5.961** on **385** df, AIC = **2578.0**, BIC = **2637.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1376** | 3.2886 | ±6.5771 | **+14.942** | **1.76e-50** | *** |
| Education: graduate level (vs college) | +0.7651 | 0.6600 | ±1.3201 | +1.159 | 0.2464 |  |
| Education: high school or below (vs college) | +1.9133 | 1.4580 | ±2.9159 | +1.312 | 0.1894 |  |
| **Site: UCSD (vs UAB)** | **+2.0177** | 0.8881 | ±1.7762 | **+2.272** | **0.0231** | * |
| **Site: UW (vs UAB)** | **-2.2869** | 0.6948 | ±1.3895 | **-3.292** | **9.96e-04** | *** |
| **Season: spring (vs autumn)** | **-2.7727** | 0.8409 | ±1.6818 | **-3.297** | **9.77e-04** | *** |
| Season: summer (vs autumn) | +1.1584 | 0.9630 | ±1.9260 | +1.203 | 0.2290 |  |
| **Season: winter (vs autumn)** | **-6.5068** | 0.8877 | ±1.7755 | **-7.330** | **2.31e-13** | *** |
| Age (years) | -0.0488 | 0.0295 | ±0.0590 | -1.655 | 0.0980 | . |
| BMI (kg/m2) | -0.0089 | 0.0502 | ±0.1004 | -0.178 | 0.8586 |  |
| Hypertension | +0.6180 | 0.6903 | ±1.3807 | +0.895 | 0.3706 |  |
| High cholesterol | -0.4306 | 0.6582 | ±1.3164 | -0.654 | 0.5130 |  |
| Kidney disease | +0.1414 | 1.2303 | ±2.4606 | +0.115 | 0.9085 |  |
| **Circulatory disease** | **+1.9706** | 0.9140 | ±1.8279 | **+2.156** | **0.0311** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.0032 | 0.0213 | ±0.0426 | +0.150 | 0.8811 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **400**, R² = **0.2769**, Adj R² = **0.2506**, F-statistic = **10.53** (p = **3.01e-20**), Residual SE = **5.942** on **385** df, AIC = **2575.5**, BIC = **2635.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.6283** | 2.5516 | ±5.1031 | **+19.842** | **1.29e-87** | *** |
| Education: graduate level (vs college) | +0.8082 | 0.6576 | ±1.3152 | +1.229 | 0.2191 |  |
| Education: high school or below (vs college) | +1.9330 | 1.4563 | ±2.9127 | +1.327 | 0.1844 |  |
| **Site: UCSD (vs UAB)** | **+2.0928** | 0.8839 | ±1.7679 | **+2.368** | **0.0179** | * |
| **Site: UW (vs UAB)** | **-2.2489** | 0.6904 | ±1.3808 | **-3.258** | **0.0011** | ** |
| **Season: spring (vs autumn)** | **-2.8224** | 0.8369 | ±1.6737 | **-3.373** | **7.45e-04** | *** |
| Season: summer (vs autumn) | +1.1135 | 0.9643 | ±1.9286 | +1.155 | 0.2482 |  |
| **Season: winter (vs autumn)** | **-6.6005** | 0.8806 | ±1.7612 | **-7.496** | **6.60e-14** | *** |
| Age (years) | -0.0418 | 0.0301 | ±0.0602 | -1.388 | 0.1652 |  |
| BMI (kg/m2) | -0.0062 | 0.0499 | ±0.0999 | -0.125 | 0.9009 |  |
| Hypertension | +0.6918 | 0.6784 | ±1.3568 | +1.020 | 0.3078 |  |
| High cholesterol | -0.4527 | 0.6437 | ±1.2874 | -0.703 | 0.4819 |  |
| Kidney disease | +0.4463 | 1.2288 | ±2.4576 | +0.363 | 0.7165 |  |
| **Circulatory disease** | **+1.9377** | 0.9059 | ±1.8119 | **+2.139** | **0.0324** | * |
| Glucose SD, pooled (mg/dL) | -0.0753 | 0.0505 | ±0.1010 | -1.491 | 0.1359 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **400**, R² = **0.2776**, Adj R² = **0.2513**, F-statistic = **10.57** (p = **2.57e-20**), Residual SE = **5.939** on **385** df, AIC = **2575.1**, BIC = **2635.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.5934** | 2.5122 | ±5.0244 | **+20.139** | **3.35e-90** | *** |
| Education: graduate level (vs college) | +0.7971 | 0.6570 | ±1.3140 | +1.213 | 0.2250 |  |
| Education: high school or below (vs college) | +1.9736 | 1.4605 | ±2.9210 | +1.351 | 0.1766 |  |
| **Site: UCSD (vs UAB)** | **+2.1138** | 0.8820 | ±1.7640 | **+2.396** | **0.0166** | * |
| **Site: UW (vs UAB)** | **-2.2332** | 0.6935 | ±1.3869 | **-3.220** | **0.0013** | ** |
| **Season: spring (vs autumn)** | **-2.8386** | 0.8335 | ±1.6670 | **-3.406** | **6.60e-04** | *** |
| Season: summer (vs autumn) | +1.0672 | 0.9653 | ±1.9305 | +1.106 | 0.2689 |  |
| **Season: winter (vs autumn)** | **-6.6121** | 0.8818 | ±1.7636 | **-7.498** | **6.46e-14** | *** |
| Age (years) | -0.0404 | 0.0303 | ±0.0607 | -1.331 | 0.1831 |  |
| BMI (kg/m2) | -0.0053 | 0.0499 | ±0.0998 | -0.107 | 0.9147 |  |
| Hypertension | +0.6875 | 0.6779 | ±1.3557 | +1.014 | 0.3105 |  |
| High cholesterol | -0.4402 | 0.6433 | ±1.2866 | -0.684 | 0.4938 |  |
| Kidney disease | +0.4910 | 1.2314 | ±2.4628 | +0.399 | 0.6901 |  |
| **Circulatory disease** | **+1.9260** | 0.9072 | ±1.8144 | **+2.123** | **0.0338** | * |
| Avg. daily SD (mg/dL) | -0.0878 | 0.0550 | ±0.1099 | -1.596 | 0.1104 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **400**, R² = **0.2782**, Adj R² = **0.2520**, F-statistic = **10.60** (p = **2.18e-20**), Residual SE = **5.936** on **385** df, AIC = **2574.7**, BIC = **2634.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2729** | 2.6302 | ±5.2603 | **+19.494** | **1.23e-84** | *** |
| Education: graduate level (vs college) | +0.7818 | 0.6552 | ±1.3104 | +1.193 | 0.2327 |  |
| Education: high school or below (vs college) | +1.8628 | 1.4535 | ±2.9070 | +1.282 | 0.2000 |  |
| **Site: UCSD (vs UAB)** | **+2.0941** | 0.8826 | ±1.7651 | **+2.373** | **0.0177** | * |
| **Site: UW (vs UAB)** | **-2.3148** | 0.6887 | ±1.3774 | **-3.361** | **7.76e-04** | *** |
| **Season: spring (vs autumn)** | **-2.7906** | 0.8378 | ±1.6756 | **-3.331** | **8.66e-04** | *** |
| Season: summer (vs autumn) | +1.1516 | 0.9667 | ±1.9335 | +1.191 | 0.2335 |  |
| **Season: winter (vs autumn)** | **-6.5188** | 0.8865 | ±1.7731 | **-7.353** | **1.94e-13** | *** |
| Age (years) | -0.0412 | 0.0300 | ±0.0599 | -1.377 | 0.1686 |  |
| BMI (kg/m2) | -0.0071 | 0.0495 | ±0.0991 | -0.143 | 0.8864 |  |
| Hypertension | +0.6493 | 0.6764 | ±1.3528 | +0.960 | 0.3371 |  |
| High cholesterol | -0.5261 | 0.6476 | ±1.2952 | -0.812 | 0.4166 |  |
| Kidney disease | +0.4189 | 1.2245 | ±2.4490 | +0.342 | 0.7323 |  |
| **Circulatory disease** | **+1.9423** | 0.9016 | ±1.8031 | **+2.154** | **0.0312** | * |
| CV (%) | -0.1180 | 0.0699 | ±0.1398 | -1.688 | 0.0915 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **400**, R² = **0.2804**, Adj R² = **0.2542**, F-statistic = **10.72** (p = **1.28e-20**), Residual SE = **5.928** on **385** df, AIC = **2573.5**, BIC = **2633.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.7117** | 3.3045 | ±6.6090 | **+13.833** | **1.61e-43** | *** |
| Education: graduate level (vs college) | +0.8353 | 0.6538 | ±1.3076 | +1.278 | 0.2014 |  |
| Education: high school or below (vs college) | +1.9104 | 1.4589 | ±2.9178 | +1.309 | 0.1904 |  |
| **Site: UCSD (vs UAB)** | **+2.1180** | 0.8806 | ±1.7613 | **+2.405** | **0.0162** | * |
| **Site: UW (vs UAB)** | **-2.2650** | 0.6894 | ±1.3787 | **-3.286** | **0.0010** | ** |
| **Season: spring (vs autumn)** | **-2.8206** | 0.8339 | ±1.6678 | **-3.382** | **7.19e-04** | *** |
| Season: summer (vs autumn) | +1.1376 | 0.9670 | ±1.9339 | +1.176 | 0.2394 |  |
| **Season: winter (vs autumn)** | **-6.5332** | 0.8825 | ±1.7649 | **-7.403** | **1.33e-13** | *** |
| Age (years) | -0.0394 | 0.0300 | ±0.0600 | -1.312 | 0.1894 |  |
| BMI (kg/m2) | -0.0055 | 0.0495 | ±0.0989 | -0.111 | 0.9117 |  |
| Hypertension | +0.6508 | 0.6749 | ±1.3498 | +0.964 | 0.3349 |  |
| High cholesterol | -0.5015 | 0.6447 | ±1.2893 | -0.778 | 0.4366 |  |
| Kidney disease | +0.4285 | 1.2094 | ±2.4188 | +0.354 | 0.7231 |  |
| **Circulatory disease** | **+1.9570** | 0.9003 | ±1.8006 | **+2.174** | **0.0297** | * |
| **Mean / SD ratio** | **+0.5653** | 0.2740 | ±0.5480 | **+2.063** | **0.0391** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **400**, R² = **0.2797**, Adj R² = **0.2536**, F-statistic = **10.68** (p = **1.51e-20**), Residual SE = **5.930** on **385** df, AIC = **2573.9**, BIC = **2633.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.8996** | 3.3612 | ±6.7224 | **+13.656** | **1.87e-42** | *** |
| Education: graduate level (vs college) | +0.8302 | 0.6534 | ±1.3067 | +1.271 | 0.2039 |  |
| Education: high school or below (vs college) | +2.0137 | 1.4601 | ±2.9202 | +1.379 | 0.1679 |  |
| **Site: UCSD (vs UAB)** | **+2.1610** | 0.8799 | ±1.7598 | **+2.456** | **0.0140** | * |
| **Site: UW (vs UAB)** | **-2.2487** | 0.6926 | ±1.3852 | **-3.247** | **0.0012** | ** |
| **Season: spring (vs autumn)** | **-2.7821** | 0.8325 | ±1.6650 | **-3.342** | **8.32e-04** | *** |
| Season: summer (vs autumn) | +1.0644 | 0.9659 | ±1.9317 | +1.102 | 0.2704 |  |
| **Season: winter (vs autumn)** | **-6.5119** | 0.8849 | ±1.7698 | **-7.359** | **1.85e-13** | *** |
| Age (years) | -0.0388 | 0.0302 | ±0.0605 | -1.285 | 0.1989 |  |
| BMI (kg/m2) | -0.0032 | 0.0495 | ±0.0990 | -0.065 | 0.9479 |  |
| Hypertension | +0.6288 | 0.6749 | ±1.3498 | +0.932 | 0.3515 |  |
| High cholesterol | -0.4699 | 0.6443 | ±1.2886 | -0.729 | 0.4658 |  |
| Kidney disease | +0.4744 | 1.2216 | ±2.4433 | +0.388 | 0.6977 |  |
| **Circulatory disease** | **+1.9384** | 0.9040 | ±1.8080 | **+2.144** | **0.0320** | * |
| Avg. daily mean/SD | +0.4342 | 0.2325 | ±0.4651 | +1.867 | 0.0619 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **400**, R² = **0.2724**, Adj R² = **0.2459**, F-statistic = **10.29** (p = **9.11e-20**), Residual SE = **5.960** on **385** df, AIC = **2578.0**, BIC = **2637.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.9213** | 2.8060 | ±5.6119 | **+17.791** | **8.27e-71** | *** |
| Education: graduate level (vs college) | +0.7698 | 0.6594 | ±1.3188 | +1.167 | 0.2431 |  |
| Education: high school or below (vs college) | +1.9244 | 1.4539 | ±2.9077 | +1.324 | 0.1856 |  |
| **Site: UCSD (vs UAB)** | **+2.0315** | 0.8851 | ±1.7703 | **+2.295** | **0.0217** | * |
| **Site: UW (vs UAB)** | **-2.3009** | 0.6973 | ±1.3945 | **-3.300** | **9.67e-04** | *** |
| **Season: spring (vs autumn)** | **-2.7875** | 0.8374 | ±1.6749 | **-3.329** | **8.73e-04** | *** |
| Season: summer (vs autumn) | +1.1428 | 0.9632 | ±1.9263 | +1.187 | 0.2354 |  |
| **Season: winter (vs autumn)** | **-6.5240** | 0.8859 | ±1.7718 | **-7.364** | **1.78e-13** | *** |
| Age (years) | -0.0490 | 0.0294 | ±0.0589 | -1.666 | 0.0957 | . |
| BMI (kg/m2) | -0.0078 | 0.0497 | ±0.0994 | -0.158 | 0.8745 |  |
| Hypertension | +0.6357 | 0.6789 | ±1.3578 | +0.936 | 0.3490 |  |
| High cholesterol | -0.4372 | 0.6491 | ±1.2982 | -0.673 | 0.5006 |  |
| Kidney disease | +0.1494 | 1.2231 | ±2.4462 | +0.122 | 0.9028 |  |
| **Circulatory disease** | **+1.9615** | 0.9106 | ±1.8212 | **+2.154** | **0.0312** | * |
| MAG (mg/dL/h) | -0.0108 | 0.0368 | ±0.0736 | -0.294 | 0.7688 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **400**, R² = **0.2750**, Adj R² = **0.2486**, F-statistic = **10.43** (p = **4.85e-20**), Residual SE = **5.950** on **385** df, AIC = **2576.5**, BIC = **2636.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.6255** | 2.5595 | ±5.1190 | **+19.779** | **4.49e-87** | *** |
| Education: graduate level (vs college) | +0.7731 | 0.6577 | ±1.3153 | +1.176 | 0.2398 |  |
| Education: high school or below (vs college) | +1.9610 | 1.4639 | ±2.9278 | +1.340 | 0.1804 |  |
| **Site: UCSD (vs UAB)** | **+2.0790** | 0.8820 | ±1.7640 | **+2.357** | **0.0184** | * |
| **Site: UW (vs UAB)** | **-2.2675** | 0.6922 | ±1.3845 | **-3.276** | **0.0011** | ** |
| **Season: spring (vs autumn)** | **-2.8231** | 0.8342 | ±1.6684 | **-3.384** | **7.14e-04** | *** |
| Season: summer (vs autumn) | +1.0922 | 0.9632 | ±1.9265 | +1.134 | 0.2568 |  |
| **Season: winter (vs autumn)** | **-6.5644** | 0.8836 | ±1.7673 | **-7.429** | **1.09e-13** | *** |
| Age (years) | -0.0436 | 0.0301 | ±0.0603 | -1.446 | 0.1482 |  |
| BMI (kg/m2) | -0.0103 | 0.0497 | ±0.0994 | -0.207 | 0.8358 |  |
| Hypertension | +0.6556 | 0.6789 | ±1.3578 | +0.966 | 0.3342 |  |
| High cholesterol | -0.4609 | 0.6444 | ±1.2887 | -0.715 | 0.4744 |  |
| Kidney disease | +0.3368 | 1.2351 | ±2.4702 | +0.273 | 0.7851 |  |
| **Circulatory disease** | **+1.9427** | 0.9086 | ±1.8171 | **+2.138** | **0.0325** | * |
| Avg. daily range (mg/dL) | -0.0138 | 0.0116 | ±0.0233 | -1.186 | 0.2355 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **400**, R² = **0.2724**, Adj R² = **0.2460**, F-statistic = **10.30** (p = **9.06e-20**), Residual SE = **5.960** on **385** df, AIC = **2578.0**, BIC = **2637.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5909** | 2.5565 | ±5.1129 | **+19.398** | **7.99e-84** | *** |
| Education: graduate level (vs college) | +0.7819 | 0.6640 | ±1.3280 | +1.178 | 0.2390 |  |
| Education: high school or below (vs college) | +1.9038 | 1.4570 | ±2.9140 | +1.307 | 0.1913 |  |
| **Site: UCSD (vs UAB)** | **+2.0193** | 0.8916 | ±1.7833 | **+2.265** | **0.0235** | * |
| **Site: UW (vs UAB)** | **-2.2787** | 0.6915 | ±1.3830 | **-3.295** | **9.83e-04** | *** |
| **Season: spring (vs autumn)** | **-2.7678** | 0.8415 | ±1.6831 | **-3.289** | **0.0010** | ** |
| Season: summer (vs autumn) | +1.1604 | 0.9691 | ±1.9383 | +1.197 | 0.2312 |  |
| **Season: winter (vs autumn)** | **-6.5262** | 0.8842 | ±1.7684 | **-7.381** | **1.57e-13** | *** |
| Age (years) | -0.0486 | 0.0294 | ±0.0589 | -1.651 | 0.0987 | . |
| BMI (kg/m2) | -0.0069 | 0.0498 | ±0.0996 | -0.139 | 0.8891 |  |
| Hypertension | +0.6303 | 0.6795 | ±1.3591 | +0.927 | 0.3537 |  |
| High cholesterol | -0.4153 | 0.6472 | ±1.2944 | -0.642 | 0.5211 |  |
| Kidney disease | +0.1582 | 1.2294 | ±2.4588 | +0.129 | 0.8976 |  |
| **Circulatory disease** | **+1.9671** | 0.9110 | ±1.8220 | **+2.159** | **0.0308** | * |
| SD of daily means (mg/dL) | -0.0245 | 0.0914 | ±0.1829 | -0.268 | 0.7885 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **400**, R² = **0.2746**, Adj R² = **0.2482**, F-statistic = **10.41** (p = **5.38e-20**), Residual SE = **5.952** on **385** df, AIC = **2576.8**, BIC = **2636.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.0929** | 7.3435 | ±14.6870 | **+5.868** | **4.41e-09** | *** |
| Education: graduate level (vs college) | +0.7690 | 0.6599 | ±1.3197 | +1.165 | 0.2439 |  |
| Education: high school or below (vs college) | +1.9160 | 1.4511 | ±2.9022 | +1.320 | 0.1867 |  |
| **Site: UCSD (vs UAB)** | **+1.9807** | 0.8859 | ±1.7719 | **+2.236** | **0.0254** | * |
| **Site: UW (vs UAB)** | **-2.3180** | 0.6945 | ±1.3890 | **-3.338** | **8.45e-04** | *** |
| **Season: spring (vs autumn)** | **-2.8474** | 0.8375 | ±1.6749 | **-3.400** | **6.74e-04** | *** |
| Season: summer (vs autumn) | +1.0875 | 0.9632 | ±1.9264 | +1.129 | 0.2589 |  |
| **Season: winter (vs autumn)** | **-6.5830** | 0.8847 | ±1.7694 | **-7.441** | **1.00e-13** | *** |
| Age (years) | -0.0461 | 0.0297 | ±0.0593 | -1.556 | 0.1198 |  |
| BMI (kg/m2) | -0.0070 | 0.0497 | ±0.0994 | -0.142 | 0.8874 |  |
| Hypertension | +0.6412 | 0.6765 | ±1.3530 | +0.948 | 0.3433 |  |
| High cholesterol | -0.4386 | 0.6433 | ±1.2866 | -0.682 | 0.4954 |  |
| Kidney disease | +0.3580 | 1.2406 | ±2.4812 | +0.289 | 0.7729 |  |
| **Circulatory disease** | **+1.9039** | 0.9120 | ±1.8240 | **+2.088** | **0.0368** | * |
| Time in range 70-180, pooled (%) | +0.0654 | 0.0678 | ±0.1356 | +0.964 | 0.3351 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **400**, R² = **0.2742**, Adj R² = **0.2478**, F-statistic = **10.39** (p = **5.87e-20**), Residual SE = **5.953** on **385** df, AIC = **2577.0**, BIC = **2636.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7342** | 7.1333 | ±14.2665 | **+6.131** | **8.73e-10** | *** |
| Education: graduate level (vs college) | +0.7648 | 0.6596 | ±1.3193 | +1.159 | 0.2463 |  |
| Education: high school or below (vs college) | +1.9080 | 1.4507 | ±2.9015 | +1.315 | 0.1885 |  |
| **Site: UCSD (vs UAB)** | **+1.9936** | 0.8851 | ±1.7703 | **+2.252** | **0.0243** | * |
| **Site: UW (vs UAB)** | **-2.3137** | 0.6945 | ±1.3890 | **-3.331** | **8.64e-04** | *** |
| **Season: spring (vs autumn)** | **-2.8356** | 0.8375 | ±1.6749 | **-3.386** | **7.09e-04** | *** |
| Season: summer (vs autumn) | +1.0814 | 0.9630 | ±1.9259 | +1.123 | 0.2614 |  |
| **Season: winter (vs autumn)** | **-6.5767** | 0.8847 | ±1.7695 | **-7.434** | **1.06e-13** | *** |
| Age (years) | -0.0460 | 0.0297 | ±0.0594 | -1.550 | 0.1212 |  |
| BMI (kg/m2) | -0.0065 | 0.0498 | ±0.0995 | -0.131 | 0.8959 |  |
| Hypertension | +0.6393 | 0.6768 | ±1.3537 | +0.944 | 0.3449 |  |
| High cholesterol | -0.4284 | 0.6434 | ±1.2868 | -0.666 | 0.5055 |  |
| Kidney disease | +0.3385 | 1.2424 | ±2.4848 | +0.272 | 0.7853 |  |
| **Circulatory disease** | **+1.9106** | 0.9112 | ±1.8224 | **+2.097** | **0.0360** | * |
| Avg. daily time in range 70-180 (%) | +0.0581 | 0.0647 | ±0.1294 | +0.898 | 0.3691 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **400**, R² = **0.2755**, Adj R² = **0.2491**, F-statistic = **10.46** (p = **4.30e-20**), Residual SE = **5.948** on **385** df, AIC = **2576.3**, BIC = **2636.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8331** | 2.4955 | ±4.9910 | **+19.969** | **1.02e-88** | *** |
| Education: graduate level (vs college) | +0.7563 | 0.6564 | ±1.3128 | +1.152 | 0.2493 |  |
| Education: high school or below (vs college) | +1.8546 | 1.4503 | ±2.9006 | +1.279 | 0.2010 |  |
| **Site: UCSD (vs UAB)** | **+1.8678** | 0.8916 | ±1.7832 | **+2.095** | **0.0362** | * |
| **Site: UW (vs UAB)** | **-2.4038** | 0.6982 | ±1.3965 | **-3.443** | **5.76e-04** | *** |
| **Season: spring (vs autumn)** | **-2.7993** | 0.8365 | ±1.6729 | **-3.347** | **8.18e-04** | *** |
| Season: summer (vs autumn) | +1.2244 | 0.9625 | ±1.9250 | +1.272 | 0.2033 |  |
| **Season: winter (vs autumn)** | **-6.4749** | 0.8899 | ±1.7797 | **-7.276** | **3.43e-13** | *** |
| Age (years) | -0.0486 | 0.0294 | ±0.0588 | -1.652 | 0.0986 | . |
| BMI (kg/m2) | -0.0102 | 0.0493 | ±0.0986 | -0.206 | 0.8368 |  |
| Hypertension | +0.5715 | 0.6827 | ±1.3653 | +0.837 | 0.4025 |  |
| High cholesterol | -0.5001 | 0.6492 | ±1.2984 | -0.770 | 0.4411 |  |
| Kidney disease | +0.1857 | 1.2149 | ±2.4298 | +0.153 | 0.8785 |  |
| **Circulatory disease** | **+1.9230** | 0.9089 | ±1.8179 | **+2.116** | **0.0344** | * |
| **Time < 54 (%)** | **-0.4244** | 0.1928 | ±0.3855 | **-2.202** | **0.0277** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **400**, R² = **0.2767**, Adj R² = **0.2504**, F-statistic = **10.52** (p = **3.16e-20**), Residual SE = **5.943** on **385** df, AIC = **2575.6**, BIC = **2635.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.7219** | 2.4791 | ±4.9582 | **+20.056** | **1.78e-89** | *** |
| Education: graduate level (vs college) | +0.7284 | 0.6565 | ±1.3131 | +1.109 | 0.2672 |  |
| Education: high school or below (vs college) | +1.8259 | 1.4433 | ±2.8867 | +1.265 | 0.2059 |  |
| **Site: UCSD (vs UAB)** | **+1.8665** | 0.8881 | ±1.7762 | **+2.102** | **0.0356** | * |
| **Site: UW (vs UAB)** | **-2.4626** | 0.7013 | ±1.4026 | **-3.512** | **4.46e-04** | *** |
| **Season: spring (vs autumn)** | **-2.7736** | 0.8354 | ±1.6708 | **-3.320** | **9.00e-04** | *** |
| Season: summer (vs autumn) | +1.2428 | 0.9653 | ±1.9306 | +1.288 | 0.1979 |  |
| **Season: winter (vs autumn)** | **-6.4226** | 0.8932 | ±1.7865 | **-7.190** | **6.46e-13** | *** |
| Age (years) | -0.0468 | 0.0293 | ±0.0587 | -1.595 | 0.1107 |  |
| BMI (kg/m2) | -0.0094 | 0.0490 | ±0.0981 | -0.192 | 0.8476 |  |
| Hypertension | +0.5296 | 0.6838 | ±1.3677 | +0.774 | 0.4387 |  |
| High cholesterol | -0.5093 | 0.6482 | ±1.2965 | -0.786 | 0.4321 |  |
| Kidney disease | +0.2038 | 1.2140 | ±2.4280 | +0.168 | 0.8667 |  |
| **Circulatory disease** | **+1.9050** | 0.9020 | ±1.8041 | **+2.112** | **0.0347** | * |
| **Avg. daily time < 54 (%)** | **-0.6613** | 0.2553 | ±0.5106 | **-2.590** | **0.0096** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **400**, R² = **0.2736**, Adj R² = **0.2472**, F-statistic = **10.36** (p = **6.79e-20**), Residual SE = **5.955** on **385** df, AIC = **2577.3**, BIC = **2637.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.6778** | 2.5022 | ±5.0045 | **+19.853** | **1.03e-87** | *** |
| Education: graduate level (vs college) | +0.7472 | 0.6581 | ±1.3161 | +1.136 | 0.2562 |  |
| Education: high school or below (vs college) | +1.8534 | 1.4524 | ±2.9048 | +1.276 | 0.2019 |  |
| **Site: UCSD (vs UAB)** | **+1.9752** | 0.8899 | ±1.7797 | **+2.220** | **0.0264** | * |
| **Site: UW (vs UAB)** | **-2.3512** | 0.6961 | ±1.3922 | **-3.378** | **7.31e-04** | *** |
| **Season: spring (vs autumn)** | **-2.7611** | 0.8394 | ±1.6788 | **-3.289** | **0.0010** | ** |
| Season: summer (vs autumn) | +1.1757 | 0.9633 | ±1.9265 | +1.221 | 0.2223 |  |
| **Season: winter (vs autumn)** | **-6.4432** | 0.8910 | ±1.7821 | **-7.231** | **4.79e-13** | *** |
| Age (years) | -0.0492 | 0.0294 | ±0.0588 | -1.675 | 0.0939 | . |
| BMI (kg/m2) | -0.0063 | 0.0495 | ±0.0991 | -0.127 | 0.8987 |  |
| Hypertension | +0.5760 | 0.6846 | ±1.3693 | +0.841 | 0.4002 |  |
| High cholesterol | -0.4599 | 0.6502 | ±1.3004 | -0.707 | 0.4793 |  |
| Kidney disease | +0.1476 | 1.2273 | ±2.4547 | +0.120 | 0.9043 |  |
| **Circulatory disease** | **+1.9388** | 0.9069 | ±1.8137 | **+2.138** | **0.0325** | * |
| Time 54-69, pooled (%) | -0.1218 | 0.1186 | ±0.2373 | -1.026 | 0.3048 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **400**, R² = **0.2733**, Adj R² = **0.2469**, F-statistic = **10.34** (p = **7.27e-20**), Residual SE = **5.957** on **385** df, AIC = **2577.5**, BIC = **2637.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.6012** | 2.4965 | ±4.9930 | **+19.868** | **7.65e-88** | *** |
| Education: graduate level (vs college) | +0.7434 | 0.6586 | ±1.3171 | +1.129 | 0.2590 |  |
| Education: high school or below (vs college) | +1.8516 | 1.4522 | ±2.9045 | +1.275 | 0.2023 |  |
| **Site: UCSD (vs UAB)** | **+1.9912** | 0.8887 | ±1.7773 | **+2.241** | **0.0250** | * |
| **Site: UW (vs UAB)** | **-2.3468** | 0.6962 | ±1.3924 | **-3.371** | **7.49e-04** | *** |
| **Season: spring (vs autumn)** | **-2.7593** | 0.8391 | ±1.6781 | **-3.289** | **0.0010** | ** |
| Season: summer (vs autumn) | +1.1633 | 0.9624 | ±1.9248 | +1.209 | 0.2268 |  |
| **Season: winter (vs autumn)** | **-6.4464** | 0.8914 | ±1.7829 | **-7.232** | **4.78e-13** | *** |
| Age (years) | -0.0488 | 0.0294 | ±0.0587 | -1.661 | 0.0967 | . |
| BMI (kg/m2) | -0.0063 | 0.0495 | ±0.0991 | -0.127 | 0.8990 |  |
| Hypertension | +0.5783 | 0.6845 | ±1.3690 | +0.845 | 0.3982 |  |
| High cholesterol | -0.4533 | 0.6494 | ±1.2988 | -0.698 | 0.4851 |  |
| Kidney disease | +0.1448 | 1.2269 | ±2.4538 | +0.118 | 0.9061 |  |
| **Circulatory disease** | **+1.9465** | 0.9069 | ±1.8138 | **+2.146** | **0.0319** | * |
| Avg. daily time 54-69 (%) | -0.1062 | 0.1165 | ±0.2329 | -0.912 | 0.3618 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **400**, R² = **0.2747**, Adj R² = **0.2483**, F-statistic = **10.41** (p = **5.24e-20**), Residual SE = **5.951** on **385** df, AIC = **2576.7**, BIC = **2636.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8020** | 2.5021 | ±5.0042 | **+19.904** | **3.76e-88** | *** |
| Education: graduate level (vs college) | +0.7421 | 0.6568 | ±1.3136 | +1.130 | 0.2585 |  |
| Education: high school or below (vs college) | +1.8266 | 1.4536 | ±2.9072 | +1.257 | 0.2089 |  |
| **Site: UCSD (vs UAB)** | **+1.9250** | 0.8923 | ±1.7845 | **+2.157** | **0.0310** | * |
| **Site: UW (vs UAB)** | **-2.3937** | 0.6983 | ±1.3965 | **-3.428** | **6.08e-04** | *** |
| **Season: spring (vs autumn)** | **-2.7668** | 0.8391 | ±1.6781 | **-3.298** | **9.75e-04** | *** |
| Season: summer (vs autumn) | +1.2002 | 0.9639 | ±1.9279 | +1.245 | 0.2131 |  |
| **Season: winter (vs autumn)** | **-6.4261** | 0.8925 | ±1.7849 | **-7.200** | **6.01e-13** | *** |
| Age (years) | -0.0491 | 0.0294 | ±0.0587 | -1.674 | 0.0942 | . |
| BMI (kg/m2) | -0.0069 | 0.0493 | ±0.0986 | -0.140 | 0.8890 |  |
| Hypertension | +0.5558 | 0.6857 | ±1.3714 | +0.811 | 0.4176 |  |
| High cholesterol | -0.4875 | 0.6514 | ±1.3028 | -0.748 | 0.4542 |  |
| Kidney disease | +0.1600 | 1.2246 | ±2.4492 | +0.131 | 0.8960 |  |
| **Circulatory disease** | **+1.9249** | 0.9064 | ±1.8127 | **+2.124** | **0.0337** | * |
| Time < 70 (%) | -0.1289 | 0.0959 | ±0.1918 | -1.344 | 0.1790 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **400**, R² = **0.2743**, Adj R² = **0.2479**, F-statistic = **10.39** (p = **5.71e-20**), Residual SE = **5.953** on **385** df, AIC = **2576.9**, BIC = **2636.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.6684** | 2.4913 | ±4.9825 | **+19.937** | **1.94e-88** | *** |
| Education: graduate level (vs college) | +0.7322 | 0.6576 | ±1.3152 | +1.114 | 0.2655 |  |
| Education: high school or below (vs college) | +1.8215 | 1.4515 | ±2.9030 | +1.255 | 0.2095 |  |
| **Site: UCSD (vs UAB)** | **+1.9575** | 0.8896 | ±1.7792 | **+2.200** | **0.0278** | * |
| **Site: UW (vs UAB)** | **-2.3908** | 0.6984 | ±1.3967 | **-3.423** | **6.18e-04** | *** |
| **Season: spring (vs autumn)** | **-2.7560** | 0.8390 | ±1.6780 | **-3.285** | **0.0010** | ** |
| Season: summer (vs autumn) | +1.1827 | 0.9632 | ±1.9264 | +1.228 | 0.2195 |  |
| **Season: winter (vs autumn)** | **-6.4186** | 0.8938 | ±1.7876 | **-7.181** | **6.90e-13** | *** |
| Age (years) | -0.0483 | 0.0293 | ±0.0586 | -1.649 | 0.0991 | . |
| BMI (kg/m2) | -0.0063 | 0.0493 | ±0.0986 | -0.128 | 0.8980 |  |
| Hypertension | +0.5529 | 0.6855 | ±1.3710 | +0.807 | 0.4199 |  |
| High cholesterol | -0.4755 | 0.6499 | ±1.2998 | -0.732 | 0.4644 |  |
| Kidney disease | +0.1555 | 1.2253 | ±2.4506 | +0.127 | 0.8990 |  |
| **Circulatory disease** | **+1.9330** | 0.9050 | ±1.8099 | **+2.136** | **0.0327** | * |
| Avg. daily time < 70 (%) | -0.1218 | 0.1005 | ±0.2010 | -1.212 | 0.2256 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **400**, R² = **0.2738**, Adj R² = **0.2474**, F-statistic = **10.37** (p = **6.47e-20**), Residual SE = **5.955** on **385** df, AIC = **2577.2**, BIC = **2637.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +26.6515 | 24.8769 | ±49.7537 | +1.071 | 0.2840 |  |
| Education: graduate level (vs college) | +0.7610 | 0.6579 | ±1.3158 | +1.157 | 0.2474 |  |
| Education: high school or below (vs college) | +1.8875 | 1.4492 | ±2.8984 | +1.302 | 0.1928 |  |
| **Site: UCSD (vs UAB)** | **+1.9379** | 0.8935 | ±1.7871 | **+2.169** | **0.0301** | * |
| **Site: UW (vs UAB)** | **-2.3583** | 0.7039 | ±1.4079 | **-3.350** | **8.08e-04** | *** |
| **Season: spring (vs autumn)** | **-2.7858** | 0.8390 | ±1.6779 | **-3.321** | **8.98e-04** | *** |
| Season: summer (vs autumn) | +1.1717 | 0.9650 | ±1.9299 | +1.214 | 0.2246 |  |
| **Season: winter (vs autumn)** | **-6.5195** | 0.8885 | ±1.7770 | **-7.338** | **2.17e-13** | *** |
| Age (years) | -0.0474 | 0.0295 | ±0.0590 | -1.607 | 0.1081 |  |
| BMI (kg/m2) | -0.0092 | 0.0496 | ±0.0992 | -0.187 | 0.8520 |  |
| Hypertension | +0.6083 | 0.6799 | ±1.3599 | +0.895 | 0.3710 |  |
| High cholesterol | -0.4779 | 0.6478 | ±1.2957 | -0.738 | 0.4607 |  |
| Kidney disease | +0.2934 | 1.2395 | ±2.4789 | +0.237 | 0.8129 |  |
| **Circulatory disease** | **+1.9196** | 0.9101 | ±1.8202 | **+2.109** | **0.0349** | * |
| Time 54-250, pooled (%) | +0.2299 | 0.2480 | ±0.4960 | +0.927 | 0.3540 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **400**, R² = **0.2734**, Adj R² = **0.2470**, F-statistic = **10.35** (p = **7.08e-20**), Residual SE = **5.956** on **385** df, AIC = **2577.4**, BIC = **2637.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +26.7256 | 30.1007 | ±60.2014 | +0.888 | 0.3746 |  |
| Education: graduate level (vs college) | +0.7521 | 0.6573 | ±1.3146 | +1.144 | 0.2526 |  |
| Education: high school or below (vs college) | +1.8884 | 1.4472 | ±2.8944 | +1.305 | 0.1919 |  |
| **Site: UCSD (vs UAB)** | **+1.9631** | 0.8930 | ±1.7860 | **+2.198** | **0.0279** | * |
| **Site: UW (vs UAB)** | **-2.3521** | 0.7071 | ±1.4142 | **-3.326** | **8.80e-04** | *** |
| **Season: spring (vs autumn)** | **-2.7724** | 0.8406 | ±1.6813 | **-3.298** | **9.74e-04** | *** |
| Season: summer (vs autumn) | +1.1645 | 0.9663 | ±1.9326 | +1.205 | 0.2282 |  |
| **Season: winter (vs autumn)** | **-6.5112** | 0.8896 | ±1.7791 | **-7.319** | **2.49e-13** | *** |
| Age (years) | -0.0468 | 0.0296 | ±0.0592 | -1.580 | 0.1142 |  |
| BMI (kg/m2) | -0.0083 | 0.0496 | ±0.0991 | -0.167 | 0.8676 |  |
| Hypertension | +0.6030 | 0.6802 | ±1.3604 | +0.887 | 0.3753 |  |
| High cholesterol | -0.4591 | 0.6456 | ±1.2913 | -0.711 | 0.4771 |  |
| Kidney disease | +0.2984 | 1.2554 | ±2.5108 | +0.238 | 0.8121 |  |
| **Circulatory disease** | **+1.9187** | 0.9084 | ±1.8169 | **+2.112** | **0.0347** | * |
| Avg. daily time 54-250 (%) | +0.2279 | 0.2988 | ±0.5975 | +0.763 | 0.4456 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **400**, R² = **0.2731**, Adj R² = **0.2467**, F-statistic = **10.33** (p = **7.65e-20**), Residual SE = **5.957** on **385** df, AIC = **2577.6**, BIC = **2637.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4661** | 2.5086 | ±5.0173 | **+19.718** | **1.50e-86** | *** |
| Education: graduate level (vs college) | +0.7796 | 0.6627 | ±1.3254 | +1.176 | 0.2394 |  |
| Education: high school or below (vs college) | +1.9588 | 1.4537 | ±2.9073 | +1.347 | 0.1778 |  |
| **Site: UCSD (vs UAB)** | **+2.0294** | 0.8840 | ±1.7679 | **+2.296** | **0.0217** | * |
| **Site: UW (vs UAB)** | **-2.2611** | 0.6904 | ±1.3807 | **-3.275** | **0.0011** | ** |
| **Season: spring (vs autumn)** | **-2.8360** | 0.8403 | ±1.6806 | **-3.375** | **7.38e-04** | *** |
| Season: summer (vs autumn) | +1.0856 | 0.9659 | ±1.9317 | +1.124 | 0.2610 |  |
| **Season: winter (vs autumn)** | **-6.5979** | 0.8847 | ±1.7693 | **-7.458** | **8.78e-14** | *** |
| Age (years) | -0.0470 | 0.0298 | ±0.0597 | -1.574 | 0.1155 |  |
| BMI (kg/m2) | -0.0076 | 0.0498 | ±0.0996 | -0.154 | 0.8779 |  |
| Hypertension | +0.6638 | 0.6845 | ±1.3690 | +0.970 | 0.3322 |  |
| High cholesterol | -0.4030 | 0.6469 | ±1.2938 | -0.623 | 0.5333 |  |
| Kidney disease | +0.2755 | 1.2417 | ±2.4834 | +0.222 | 0.8244 |  |
| **Circulatory disease** | **+1.9380** | 0.9135 | ±1.8269 | **+2.122** | **0.0339** | * |
| Time 181-250, pooled (%) | -0.0503 | 0.0866 | ±0.1733 | -0.581 | 0.5616 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **400**, R² = **0.2731**, Adj R² = **0.2467**, F-statistic = **10.33** (p = **7.63e-20**), Residual SE = **5.957** on **385** df, AIC = **2577.6**, BIC = **2637.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4591** | 2.5100 | ±5.0200 | **+19.705** | **1.95e-86** | *** |
| Education: graduate level (vs college) | +0.7807 | 0.6628 | ±1.3255 | +1.178 | 0.2388 |  |
| Education: high school or below (vs college) | +1.9549 | 1.4531 | ±2.9063 | +1.345 | 0.1785 |  |
| **Site: UCSD (vs UAB)** | **+2.0263** | 0.8837 | ±1.7673 | **+2.293** | **0.0218** | * |
| **Site: UW (vs UAB)** | **-2.2608** | 0.6902 | ±1.3805 | **-3.275** | **0.0011** | ** |
| **Season: spring (vs autumn)** | **-2.8352** | 0.8398 | ±1.6795 | **-3.376** | **7.35e-04** | *** |
| Season: summer (vs autumn) | +1.0826 | 0.9658 | ±1.9316 | +1.121 | 0.2623 |  |
| **Season: winter (vs autumn)** | **-6.6005** | 0.8849 | ±1.7699 | **-7.459** | **8.74e-14** | *** |
| Age (years) | -0.0470 | 0.0298 | ±0.0596 | -1.577 | 0.1147 |  |
| BMI (kg/m2) | -0.0074 | 0.0498 | ±0.0997 | -0.149 | 0.8813 |  |
| Hypertension | +0.6654 | 0.6848 | ±1.3695 | +0.972 | 0.3312 |  |
| High cholesterol | -0.4014 | 0.6474 | ±1.2947 | -0.620 | 0.5352 |  |
| Kidney disease | +0.2743 | 1.2418 | ±2.4837 | +0.221 | 0.8252 |  |
| **Circulatory disease** | **+1.9371** | 0.9134 | ±1.8267 | **+2.121** | **0.0339** | * |
| Avg. daily time 181-250 (%) | -0.0486 | 0.0822 | ±0.1644 | -0.591 | 0.5547 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **400**, R² = **0.2729**, Adj R² = **0.2464**, F-statistic = **10.32** (p = **8.14e-20**), Residual SE = **5.959** on **385** df, AIC = **2577.7**, BIC = **2637.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4617** | 2.5098 | ±5.0196 | **+19.707** | **1.86e-86** | *** |
| Education: graduate level (vs college) | +0.7767 | 0.6628 | ±1.3256 | +1.172 | 0.2413 |  |
| Education: high school or below (vs college) | +1.9508 | 1.4526 | ±2.9051 | +1.343 | 0.1793 |  |
| **Site: UCSD (vs UAB)** | **+2.0277** | 0.8843 | ±1.7686 | **+2.293** | **0.0218** | * |
| **Site: UW (vs UAB)** | **-2.2675** | 0.6904 | ±1.3808 | **-3.284** | **0.0010** | ** |
| **Season: spring (vs autumn)** | **-2.8204** | 0.8395 | ±1.6790 | **-3.360** | **7.81e-04** | *** |
| Season: summer (vs autumn) | +1.0989 | 0.9646 | ±1.9291 | +1.139 | 0.2546 |  |
| **Season: winter (vs autumn)** | **-6.5813** | 0.8846 | ±1.7691 | **-7.440** | **1.01e-13** | *** |
| Age (years) | -0.0473 | 0.0299 | ±0.0597 | -1.583 | 0.1135 |  |
| BMI (kg/m2) | -0.0077 | 0.0498 | ±0.0996 | -0.156 | 0.8764 |  |
| Hypertension | +0.6564 | 0.6839 | ±1.3678 | +0.960 | 0.3372 |  |
| High cholesterol | -0.4093 | 0.6462 | ±1.2924 | -0.633 | 0.5265 |  |
| Kidney disease | +0.2626 | 1.2511 | ±2.5023 | +0.210 | 0.8337 |  |
| **Circulatory disease** | **+1.9411** | 0.9134 | ±1.8268 | **+2.125** | **0.0336** | * |
| Time > 180 (%) | -0.0374 | 0.0780 | ±0.1561 | -0.479 | 0.6319 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **400**, R² = **0.2728**, Adj R² = **0.2464**, F-statistic = **10.32** (p = **8.23e-20**), Residual SE = **5.959** on **385** df, AIC = **2577.7**, BIC = **2637.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4548** | 2.5115 | ±5.0230 | **+19.691** | **2.56e-86** | *** |
| Education: graduate level (vs college) | +0.7768 | 0.6628 | ±1.3256 | +1.172 | 0.2412 |  |
| Education: high school or below (vs college) | +1.9465 | 1.4520 | ±2.9040 | +1.341 | 0.1801 |  |
| **Site: UCSD (vs UAB)** | **+2.0246** | 0.8842 | ±1.7684 | **+2.290** | **0.0220** | * |
| **Site: UW (vs UAB)** | **-2.2674** | 0.6904 | ±1.3807 | **-3.284** | **0.0010** | ** |
| **Season: spring (vs autumn)** | **-2.8178** | 0.8392 | ±1.6784 | **-3.358** | **7.86e-04** | *** |
| Season: summer (vs autumn) | +1.0994 | 0.9644 | ±1.9287 | +1.140 | 0.2543 |  |
| **Season: winter (vs autumn)** | **-6.5803** | 0.8848 | ±1.7696 | **-7.437** | **1.03e-13** | *** |
| Age (years) | -0.0474 | 0.0298 | ±0.0597 | -1.588 | 0.1123 |  |
| BMI (kg/m2) | -0.0076 | 0.0498 | ±0.0996 | -0.152 | 0.8793 |  |
| Hypertension | +0.6558 | 0.6840 | ±1.3680 | +0.959 | 0.3376 |  |
| High cholesterol | -0.4076 | 0.6468 | ±1.2935 | -0.630 | 0.5285 |  |
| Kidney disease | +0.2568 | 1.2518 | ±2.5035 | +0.205 | 0.8375 |  |
| **Circulatory disease** | **+1.9412** | 0.9135 | ±1.8270 | **+2.125** | **0.0336** | * |
| Avg. daily time > 180 (%) | -0.0344 | 0.0739 | ±0.1478 | -0.466 | 0.6415 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **400**, R² = **0.2728**, Adj R² = **0.2463**, F-statistic = **10.32** (p = **8.28e-20**), Residual SE = **5.959** on **385** df, AIC = **2577.8**, BIC = **2637.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4281** | 2.5227 | ±5.0453 | **+19.594** | **1.75e-85** | *** |
| Education: graduate level (vs college) | +0.7537 | 0.6583 | ±1.3166 | +1.145 | 0.2522 |  |
| Education: high school or below (vs college) | +1.9588 | 1.4541 | ±2.9081 | +1.347 | 0.1779 |  |
| **Site: UCSD (vs UAB)** | **+2.0164** | 0.8865 | ±1.7729 | **+2.275** | **0.0229** | * |
| **Site: UW (vs UAB)** | **-2.2767** | 0.6912 | ±1.3824 | **-3.294** | **9.88e-04** | *** |
| **Season: spring (vs autumn)** | **-2.8042** | 0.8415 | ±1.6831 | **-3.332** | **8.61e-04** | *** |
| Season: summer (vs autumn) | +1.0898 | 0.9659 | ±1.9318 | +1.128 | 0.2592 |  |
| **Season: winter (vs autumn)** | **-6.5539** | 0.8876 | ±1.7752 | **-7.384** | **1.54e-13** | *** |
| Age (years) | -0.0480 | 0.0297 | ±0.0593 | -1.617 | 0.1060 |  |
| BMI (kg/m2) | -0.0061 | 0.0503 | ±0.1007 | -0.121 | 0.9037 |  |
| Hypertension | +0.6567 | 0.6873 | ±1.3746 | +0.955 | 0.3393 |  |
| High cholesterol | -0.4185 | 0.6450 | ±1.2900 | -0.649 | 0.5165 |  |
| Kidney disease | +0.1480 | 1.2197 | ±2.4394 | +0.121 | 0.9034 |  |
| **Circulatory disease** | **+1.9241** | 0.9171 | ±1.8343 | **+2.098** | **0.0359** | * |
| Nocturnal time > 180 (%) | -0.0359 | 0.0937 | ±0.1874 | -0.383 | 0.7020 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **400**, R² = **0.2730**, Adj R² = **0.2465**, F-statistic = **10.33** (p = **7.90e-20**), Residual SE = **5.958** on **385** df, AIC = **2577.7**, BIC = **2637.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5200** | 2.4917 | ±4.9834 | **+19.874** | **6.85e-88** | *** |
| Education: graduate level (vs college) | +0.7530 | 0.6596 | ±1.3192 | +1.142 | 0.2536 |  |
| Education: high school or below (vs college) | +1.9193 | 1.4450 | ±2.8900 | +1.328 | 0.1841 |  |
| **Site: UCSD (vs UAB)** | **+2.0577** | 0.8889 | ±1.7778 | **+2.315** | **0.0206** | * |
| **Site: UW (vs UAB)** | **-2.2782** | 0.6907 | ±1.3815 | **-3.298** | **9.73e-04** | *** |
| **Season: spring (vs autumn)** | **-2.8150** | 0.8413 | ±1.6827 | **-3.346** | **8.20e-04** | *** |
| Season: summer (vs autumn) | +1.1134 | 0.9629 | ±1.9257 | +1.156 | 0.2476 |  |
| **Season: winter (vs autumn)** | **-6.5510** | 0.8837 | ±1.7675 | **-7.413** | **1.24e-13** | *** |
| Age (years) | -0.0473 | 0.0297 | ±0.0594 | -1.593 | 0.1111 |  |
| BMI (kg/m2) | -0.0094 | 0.0496 | ±0.0992 | -0.189 | 0.8500 |  |
| Hypertension | +0.6496 | 0.6800 | ±1.3600 | +0.955 | 0.3394 |  |
| High cholesterol | -0.4279 | 0.6440 | ±1.2880 | -0.664 | 0.5064 |  |
| Kidney disease | +0.2057 | 1.2288 | ±2.4577 | +0.167 | 0.8670 |  |
| **Circulatory disease** | **+1.9408** | 0.9174 | ±1.8348 | **+2.115** | **0.0344** | * |
| Any reading > 250 during wear (0/1) | -0.5203 | 0.8667 | ±1.7335 | -0.600 | 0.5483 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **400**, R² = **0.2723**, Adj R² = **0.2458**, F-statistic = **10.29** (p = **9.32e-20**), Residual SE = **5.961** on **385** df, AIC = **2578.0**, BIC = **2637.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4745** | 2.5110 | ±5.0219 | **+19.703** | **2.01e-86** | *** |
| Education: graduate level (vs college) | +0.7692 | 0.6622 | ±1.3245 | +1.161 | 0.2454 |  |
| Education: high school or below (vs college) | +1.9287 | 1.4457 | ±2.8914 | +1.334 | 0.1822 |  |
| **Site: UCSD (vs UAB)** | **+2.0241** | 0.8875 | ±1.7751 | **+2.281** | **0.0226** | * |
| **Site: UW (vs UAB)** | **-2.2739** | 0.6950 | ±1.3901 | **-3.272** | **0.0011** | ** |
| **Season: spring (vs autumn)** | **-2.7784** | 0.8415 | ±1.6831 | **-3.302** | **9.61e-04** | *** |
| Season: summer (vs autumn) | +1.1552 | 0.9615 | ±1.9230 | +1.202 | 0.2296 |  |
| **Season: winter (vs autumn)** | **-6.5082** | 0.8866 | ±1.7731 | **-7.341** | **2.12e-13** | *** |
| Age (years) | -0.0494 | 0.0297 | ±0.0594 | -1.663 | 0.0963 | . |
| BMI (kg/m2) | -0.0079 | 0.0497 | ±0.0994 | -0.159 | 0.8734 |  |
| Hypertension | +0.6240 | 0.6784 | ±1.3567 | +0.920 | 0.3576 |  |
| High cholesterol | -0.4120 | 0.6474 | ±1.2947 | -0.636 | 0.5245 |  |
| Kidney disease | +0.1004 | 1.2891 | ±2.5781 | +0.078 | 0.9379 |  |
| **Circulatory disease** | **+1.9720** | 0.9118 | ±1.8236 | **+2.163** | **0.0306** | * |
| Time > 250 (%) | +0.0815 | 0.5808 | ±1.1616 | +0.140 | 0.8884 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 400)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **400**, R² = **0.2724**, Adj R² = **0.2460**, F-statistic = **10.30** (p = **9.01e-20**), Residual SE = **5.960** on **385** df, AIC = **2577.9**, BIC = **2637.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4890** | 2.5125 | ±5.0251 | **+19.697** | **2.30e-86** | *** |
| Education: graduate level (vs college) | +0.7705 | 0.6638 | ±1.3276 | +1.161 | 0.2458 |  |
| Education: high school or below (vs college) | +1.9311 | 1.4446 | ±2.8892 | +1.337 | 0.1813 |  |
| **Site: UCSD (vs UAB)** | **+2.0274** | 0.8875 | ±1.7751 | **+2.284** | **0.0224** | * |
| **Site: UW (vs UAB)** | **-2.2722** | 0.6951 | ±1.3902 | **-3.269** | **0.0011** | ** |
| **Season: spring (vs autumn)** | **-2.7793** | 0.8415 | ±1.6831 | **-3.303** | **9.58e-04** | *** |
| Season: summer (vs autumn) | +1.1586 | 0.9613 | ±1.9225 | +1.205 | 0.2281 |  |
| **Season: winter (vs autumn)** | **-6.5016** | 0.8868 | ±1.7737 | **-7.331** | **2.28e-13** | *** |
| Age (years) | -0.0497 | 0.0297 | ±0.0593 | -1.676 | 0.0938 | . |
| BMI (kg/m2) | -0.0081 | 0.0497 | ±0.0994 | -0.162 | 0.8709 |  |
| Hypertension | +0.6227 | 0.6779 | ±1.3559 | +0.918 | 0.3584 |  |
| High cholesterol | -0.4118 | 0.6482 | ±1.2963 | -0.635 | 0.5253 |  |
| Kidney disease | +0.0676 | 1.2871 | ±2.5741 | +0.053 | 0.9581 |  |
| **Circulatory disease** | **+1.9786** | 0.9119 | ±1.8239 | **+2.170** | **0.0300** | * |
| Avg. daily time > 250 (%) | +0.1328 | 0.6159 | ±1.2319 | +0.216 | 0.8293 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 400; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **400**, R² = **0.0594**, Adj R² = **0.0277**, F-statistic = **1.88** (p = **0.0314**), Residual SE = **15.296** on **386** df, AIC = **3331.0**, BIC = **3386.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.1844** | 6.1042 | ±12.2084 | **+20.017** | **3.95e-89** | *** |
| Education: graduate level (vs college) | +2.5628 | 1.6032 | ±3.2065 | +1.599 | 0.1099 |  |
| Education: high school or below (vs college) | +5.5589 | 4.1738 | ±8.3476 | +1.332 | 0.1829 |  |
| Site: UCSD (vs UAB) | +2.9775 | 2.3709 | ±4.7417 | +1.256 | 0.2092 |  |
| Site: UW (vs UAB) | -1.6942 | 1.8172 | ±3.6344 | -0.932 | 0.3512 |  |
| Season: spring (vs autumn) | +2.3848 | 1.9633 | ±3.9265 | +1.215 | 0.2245 |  |
| Season: summer (vs autumn) | +0.2965 | 2.4667 | ±4.9334 | +0.120 | 0.9043 |  |
| Season: winter (vs autumn) | +4.1831 | 2.2146 | ±4.4291 | +1.889 | 0.0589 | . |
| Age (years) | -0.0948 | 0.0681 | ±0.1363 | -1.391 | 0.1642 |  |
| BMI (kg/m2) | +0.1620 | 0.1196 | ±0.2392 | +1.355 | 0.1755 |  |
| Hypertension | +3.2854 | 1.7365 | ±3.4730 | +1.892 | 0.0585 | . |
| High cholesterol | -1.8427 | 1.6185 | ±3.2371 | -1.138 | 0.2549 |  |
| Kidney disease | +0.4304 | 3.5009 | ±7.0018 | +0.123 | 0.9022 |  |
| Circulatory disease | +1.4643 | 2.3013 | ±4.6025 | +0.636 | 0.5246 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **400**, R² = **0.0602**, Adj R² = **0.0260**, F-statistic = **1.76** (p = **0.0425**), Residual SE = **15.309** on **385** df, AIC = **3332.6**, BIC = **3392.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+116.7167** | 11.0427 | ±22.0853 | **+10.570** | **4.12e-26** | *** |
| Education: graduate level (vs college) | +2.5955 | 1.6050 | ±3.2100 | +1.617 | 0.1058 |  |
| Education: high school or below (vs college) | +5.4057 | 4.1652 | ±8.3304 | +1.298 | 0.1944 |  |
| Site: UCSD (vs UAB) | +2.8137 | 2.3842 | ±4.7684 | +1.180 | 0.2379 |  |
| Site: UW (vs UAB) | -1.7346 | 1.8112 | ±3.6224 | -0.958 | 0.3382 |  |
| Season: spring (vs autumn) | +2.5459 | 1.9875 | ±3.9751 | +1.281 | 0.2002 |  |
| Season: summer (vs autumn) | +0.3210 | 2.4744 | ±4.9488 | +0.130 | 0.8968 |  |
| Season: winter (vs autumn) | +4.2539 | 2.2191 | ±4.4382 | +1.917 | 0.0552 | . |
| Age (years) | -0.1021 | 0.0700 | ±0.1400 | -1.458 | 0.1447 |  |
| BMI (kg/m2) | +0.1526 | 0.1218 | ±0.2437 | +1.252 | 0.2105 |  |
| Hypertension | +3.3001 | 1.7397 | ±3.4795 | +1.897 | 0.0578 | . |
| High cholesterol | -1.9937 | 1.6117 | ±3.2233 | -1.237 | 0.2161 |  |
| Kidney disease | +0.3752 | 3.4982 | ±6.9965 | +0.107 | 0.9146 |  |
| Circulatory disease | +1.5257 | 2.3127 | ±4.6254 | +0.660 | 0.5094 |  |
| HbA1c (%) | +1.1015 | 1.9050 | ±3.8100 | +0.578 | 0.5631 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **400**, R² = **0.0601**, Adj R² = **0.0259**, F-statistic = **1.76** (p = **0.0430**), Residual SE = **15.310** on **385** df, AIC = **3332.7**, BIC = **3392.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3208** | 8.0625 | ±16.1251 | **+15.544** | **1.76e-54** | *** |
| Education: graduate level (vs college) | +2.6194 | 1.6111 | ±3.2221 | +1.626 | 0.1040 |  |
| Education: high school or below (vs college) | +5.6717 | 4.1816 | ±8.3632 | +1.356 | 0.1750 |  |
| Site: UCSD (vs UAB) | +3.0040 | 2.3880 | ±4.7760 | +1.258 | 0.2084 |  |
| Site: UW (vs UAB) | -1.5929 | 1.8399 | ±3.6798 | -0.866 | 0.3866 |  |
| Season: spring (vs autumn) | +2.3103 | 1.9818 | ±3.9635 | +1.166 | 0.2437 |  |
| Season: summer (vs autumn) | +0.2220 | 2.4735 | ±4.9470 | +0.090 | 0.9285 |  |
| Season: winter (vs autumn) | +4.0372 | 2.2843 | ±4.5686 | +1.767 | 0.0772 | . |
| Age (years) | -0.0921 | 0.0695 | ±0.1391 | -1.325 | 0.1853 |  |
| BMI (kg/m2) | +0.1644 | 0.1212 | ±0.2424 | +1.356 | 0.1750 |  |
| Hypertension | +3.3786 | 1.7339 | ±3.4679 | +1.948 | 0.0514 | . |
| High cholesterol | -1.7489 | 1.6273 | ±3.2546 | -1.075 | 0.2825 |  |
| Kidney disease | +0.6043 | 3.5114 | ±7.0227 | +0.172 | 0.8634 |  |
| Circulatory disease | +1.4393 | 2.3185 | ±4.6370 | +0.621 | 0.5347 |  |
| Mean glucose (mg/dL) | -0.0301 | 0.0611 | ±0.1223 | -0.493 | 0.6221 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **400**, R² = **0.0601**, Adj R² = **0.0259**, F-statistic = **1.76** (p = **0.0430**), Residual SE = **15.310** on **385** df, AIC = **3332.7**, BIC = **3392.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.4907** | 15.0437 | ±30.0873 | **+8.608** | **7.46e-18** | *** |
| Education: graduate level (vs college) | +2.6194 | 1.6111 | ±3.2221 | +1.626 | 0.1040 |  |
| Education: high school or below (vs college) | +5.6717 | 4.1816 | ±8.3632 | +1.356 | 0.1750 |  |
| Site: UCSD (vs UAB) | +3.0040 | 2.3880 | ±4.7760 | +1.258 | 0.2084 |  |
| Site: UW (vs UAB) | -1.5929 | 1.8399 | ±3.6798 | -0.866 | 0.3866 |  |
| Season: spring (vs autumn) | +2.3103 | 1.9818 | ±3.9635 | +1.166 | 0.2437 |  |
| Season: summer (vs autumn) | +0.2220 | 2.4735 | ±4.9470 | +0.090 | 0.9285 |  |
| Season: winter (vs autumn) | +4.0372 | 2.2843 | ±4.5686 | +1.767 | 0.0772 | . |
| Age (years) | -0.0921 | 0.0695 | ±0.1391 | -1.325 | 0.1853 |  |
| BMI (kg/m2) | +0.1644 | 0.1212 | ±0.2424 | +1.356 | 0.1750 |  |
| Hypertension | +3.3786 | 1.7339 | ±3.4679 | +1.948 | 0.0514 | . |
| High cholesterol | -1.7489 | 1.6273 | ±3.2546 | -1.075 | 0.2825 |  |
| Kidney disease | +0.6043 | 3.5114 | ±7.0227 | +0.172 | 0.8634 |  |
| Circulatory disease | +1.4393 | 2.3185 | ±4.6370 | +0.621 | 0.5347 |  |
| GMI (%) | -1.2598 | 2.5556 | ±5.1113 | -0.493 | 0.6221 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **400**, R² = **0.0594**, Adj R² = **0.0252**, F-statistic = **1.74** (p = **0.0464**), Residual SE = **15.316** on **385** df, AIC = **3333.0**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.7771** | 7.5353 | ±15.0707 | **+16.294** | **1.10e-59** | *** |
| Education: graduate level (vs college) | +2.5695 | 1.6071 | ±3.2142 | +1.599 | 0.1098 |  |
| Education: high school or below (vs college) | +5.5862 | 4.1420 | ±8.2840 | +1.349 | 0.1774 |  |
| Site: UCSD (vs UAB) | +2.9882 | 2.3841 | ±4.7682 | +1.253 | 0.2101 |  |
| Site: UW (vs UAB) | -1.6784 | 1.8248 | ±3.6496 | -0.920 | 0.3577 |  |
| Season: spring (vs autumn) | +2.3765 | 1.9749 | ±3.9499 | +1.203 | 0.2289 |  |
| Season: summer (vs autumn) | +0.2792 | 2.4763 | ±4.9525 | +0.113 | 0.9102 |  |
| Season: winter (vs autumn) | +4.1645 | 2.2515 | ±4.5030 | +1.850 | 0.0644 | . |
| Age (years) | -0.0949 | 0.0682 | ±0.1365 | -1.391 | 0.1641 |  |
| BMI (kg/m2) | +0.1638 | 0.1244 | ±0.2487 | +1.317 | 0.1877 |  |
| Hypertension | +3.3032 | 1.7402 | ±3.4804 | +1.898 | 0.0577 | . |
| High cholesterol | -1.8191 | 1.6343 | ±3.2686 | -1.113 | 0.2657 |  |
| Kidney disease | +0.4371 | 3.5070 | ±7.0141 | +0.125 | 0.9008 |  |
| Circulatory disease | +1.4525 | 2.3056 | ±4.6113 | +0.630 | 0.5287 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0058 | 0.0523 | ±0.1045 | -0.110 | 0.9122 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **400**, R² = **0.0595**, Adj R² = **0.0253**, F-statistic = **1.74** (p = **0.0459**), Residual SE = **15.315** on **385** df, AIC = **3332.9**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.6151** | 6.2268 | ±12.4536 | **+19.691** | **2.55e-86** | *** |
| Education: graduate level (vs college) | +2.5774 | 1.6097 | ±3.2193 | +1.601 | 0.1093 |  |
| Education: high school or below (vs college) | +5.5606 | 4.2269 | ±8.4538 | +1.316 | 0.1883 |  |
| Site: UCSD (vs UAB) | +3.0031 | 2.3854 | ±4.7707 | +1.259 | 0.2080 |  |
| Site: UW (vs UAB) | -1.6834 | 1.8243 | ±3.6486 | -0.923 | 0.3561 |  |
| Season: spring (vs autumn) | +2.3680 | 1.9725 | ±3.9450 | +1.201 | 0.2299 |  |
| Season: summer (vs autumn) | +0.2834 | 2.4693 | ±4.9386 | +0.115 | 0.9086 |  |
| Season: winter (vs autumn) | +4.1523 | 2.2471 | ±4.4943 | +1.848 | 0.0646 | . |
| Age (years) | -0.0922 | 0.0716 | ±0.1433 | -1.286 | 0.1983 |  |
| BMI (kg/m2) | +0.1627 | 0.1206 | ±0.2413 | +1.348 | 0.1775 |  |
| Hypertension | +3.3090 | 1.7423 | ±3.4847 | +1.899 | 0.0575 | . |
| High cholesterol | -1.8557 | 1.6283 | ±3.2566 | -1.140 | 0.2544 |  |
| Kidney disease | +0.5418 | 3.5066 | ±7.0132 | +0.155 | 0.8772 |  |
| Circulatory disease | +1.4545 | 2.3110 | ±4.6220 | +0.629 | 0.5291 |  |
| Glucose SD, pooled (mg/dL) | -0.0279 | 0.1364 | ±0.2728 | -0.204 | 0.8380 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **400**, R² = **0.0599**, Adj R² = **0.0257**, F-statistic = **1.75** (p = **0.0439**), Residual SE = **15.312** on **385** df, AIC = **3332.8**, BIC = **3392.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.9810** | 6.1471 | ±12.2942 | **+20.006** | **4.85e-89** | *** |
| Education: graduate level (vs college) | +2.5828 | 1.6068 | ±3.2136 | +1.607 | 0.1080 |  |
| Education: high school or below (vs college) | +5.5908 | 4.2402 | ±8.4804 | +1.319 | 0.1873 |  |
| Site: UCSD (vs UAB) | +3.0411 | 2.3912 | ±4.7825 | +1.272 | 0.2035 |  |
| Site: UW (vs UAB) | -1.6624 | 1.8281 | ±3.6562 | -0.909 | 0.3632 |  |
| Season: spring (vs autumn) | +2.3414 | 1.9728 | ±3.9455 | +1.187 | 0.2353 |  |
| Season: summer (vs autumn) | +0.2388 | 2.4650 | ±4.9301 | +0.097 | 0.9228 |  |
| Season: winter (vs autumn) | +4.1161 | 2.2548 | ±4.5095 | +1.826 | 0.0679 | . |
| Age (years) | -0.0888 | 0.0730 | ±0.1460 | -1.216 | 0.2239 |  |
| BMI (kg/m2) | +0.1639 | 0.1212 | ±0.2424 | +1.352 | 0.1763 |  |
| Hypertension | +3.3274 | 1.7397 | ±3.4795 | +1.913 | 0.0558 | . |
| High cholesterol | -1.8587 | 1.6254 | ±3.2509 | -1.144 | 0.2528 |  |
| Kidney disease | +0.6746 | 3.5057 | ±7.0113 | +0.192 | 0.8474 |  |
| Circulatory disease | +1.4374 | 2.3124 | ±4.6248 | +0.622 | 0.5342 |  |
| Avg. daily SD (mg/dL) | -0.0620 | 0.1565 | ±0.3131 | -0.396 | 0.6922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **400**, R² = **0.0596**, Adj R² = **0.0254**, F-statistic = **1.74** (p = **0.0456**), Residual SE = **15.315** on **385** df, AIC = **3332.9**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.8926** | 6.5847 | ±13.1694 | **+18.663** | **9.85e-78** | *** |
| Education: graduate level (vs college) | +2.5679 | 1.6064 | ±3.2128 | +1.599 | 0.1099 |  |
| Education: high school or below (vs college) | +5.5332 | 4.2288 | ±8.4576 | +1.308 | 0.1907 |  |
| Site: UCSD (vs UAB) | +3.0051 | 2.3782 | ±4.7565 | +1.264 | 0.2064 |  |
| Site: UW (vs UAB) | -1.7086 | 1.8247 | ±3.6493 | -0.936 | 0.3491 |  |
| Season: spring (vs autumn) | +2.3795 | 1.9688 | ±3.9376 | +1.209 | 0.2268 |  |
| Season: summer (vs autumn) | +0.2976 | 2.4710 | ±4.9420 | +0.120 | 0.9041 |  |
| Season: winter (vs autumn) | +4.1825 | 2.2192 | ±4.4384 | +1.885 | 0.0595 | . |
| Age (years) | -0.0918 | 0.0705 | ±0.1411 | -1.301 | 0.1932 |  |
| BMI (kg/m2) | +0.1624 | 0.1201 | ±0.2403 | +1.351 | 0.1765 |  |
| Hypertension | +3.2938 | 1.7414 | ±3.4828 | +1.891 | 0.0586 | . |
| High cholesterol | -1.8852 | 1.6423 | ±3.2846 | -1.148 | 0.2510 |  |
| Kidney disease | +0.5376 | 3.5056 | ±7.0112 | +0.153 | 0.8781 |  |
| Circulatory disease | +1.4557 | 2.3083 | ±4.6166 | +0.631 | 0.5283 |  |
| CV (%) | -0.0462 | 0.1761 | ±0.3522 | -0.262 | 0.7930 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **400**, R² = **0.0594**, Adj R² = **0.0252**, F-statistic = **1.74** (p = **0.0463**), Residual SE = **15.316** on **385** df, AIC = **3333.0**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+121.5396** | 7.8104 | ±15.6207 | **+15.561** | **1.33e-54** | *** |
| Education: graduate level (vs college) | +2.5742 | 1.6054 | ±3.2109 | +1.603 | 0.1088 |  |
| Education: high school or below (vs college) | +5.5558 | 4.2055 | ±8.4111 | +1.321 | 0.1865 |  |
| Site: UCSD (vs UAB) | +2.9937 | 2.3739 | ±4.7479 | +1.261 | 0.2073 |  |
| Site: UW (vs UAB) | -1.6920 | 1.8219 | ±3.6439 | -0.929 | 0.3531 |  |
| Season: spring (vs autumn) | +2.3773 | 1.9666 | ±3.9332 | +1.209 | 0.2267 |  |
| Season: summer (vs autumn) | +0.2946 | 2.4712 | ±4.9423 | +0.119 | 0.9051 |  |
| Season: winter (vs autumn) | +4.1804 | 2.2213 | ±4.4425 | +1.882 | 0.0598 | . |
| Age (years) | -0.0931 | 0.0706 | ±0.1412 | -1.319 | 0.1871 |  |
| BMI (kg/m2) | +0.1625 | 0.1199 | ±0.2399 | +1.355 | 0.1756 |  |
| Hypertension | +3.2893 | 1.7421 | ±3.4841 | +1.888 | 0.0590 | . |
| High cholesterol | -1.8571 | 1.6354 | ±3.2709 | -1.136 | 0.2561 |  |
| Kidney disease | +0.4790 | 3.5070 | ±7.0139 | +0.137 | 0.8913 |  |
| Circulatory disease | +1.4630 | 2.3070 | ±4.6140 | +0.634 | 0.5260 |  |
| Mean / SD ratio | +0.0971 | 0.7063 | ±1.4126 | +0.137 | 0.8906 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **400**, R² = **0.0598**, Adj R² = **0.0256**, F-statistic = **1.75** (p = **0.0444**), Residual SE = **15.313** on **385** df, AIC = **3332.8**, BIC = **3392.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+120.2866** | 7.9728 | ±15.9456 | **+15.087** | **1.97e-51** | *** |
| Education: graduate level (vs college) | +2.5955 | 1.6022 | ±3.2044 | +1.620 | 0.1052 |  |
| Education: high school or below (vs college) | +5.6043 | 4.1953 | ±8.3907 | +1.336 | 0.1816 |  |
| Site: UCSD (vs UAB) | +3.0506 | 2.3748 | ±4.7496 | +1.285 | 0.1989 |  |
| Site: UW (vs UAB) | -1.6785 | 1.8216 | ±3.6432 | -0.921 | 0.3568 |  |
| Season: spring (vs autumn) | +2.3822 | 1.9677 | ±3.9355 | +1.211 | 0.2260 |  |
| Season: summer (vs autumn) | +0.2516 | 2.4604 | ±4.9209 | +0.102 | 0.9186 |  |
| Season: winter (vs autumn) | +4.1859 | 2.2167 | ±4.4334 | +1.888 | 0.0590 | . |
| Age (years) | -0.0894 | 0.0715 | ±0.1430 | -1.251 | 0.2109 |  |
| BMI (kg/m2) | +0.1645 | 0.1200 | ±0.2399 | +1.372 | 0.1702 |  |
| Hypertension | +3.2858 | 1.7402 | ±3.4804 | +1.888 | 0.0590 | . |
| High cholesterol | -1.8706 | 1.6292 | ±3.2584 | -1.148 | 0.2509 |  |
| Kidney disease | +0.6056 | 3.5068 | ±7.0136 | +0.173 | 0.8629 |  |
| Circulatory disease | +1.4506 | 2.3070 | ±4.6140 | +0.629 | 0.5295 |  |
| Avg. daily mean/SD | +0.2311 | 0.5911 | ±1.1822 | +0.391 | 0.6958 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **400**, R² = **0.0595**, Adj R² = **0.0253**, F-statistic = **1.74** (p = **0.0459**), Residual SE = **15.315** on **385** df, AIC = **3332.9**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+121.2549** | 6.9804 | ±13.9609 | **+17.371** | **1.38e-67** | *** |
| Education: graduate level (vs college) | +2.5610 | 1.6085 | ±3.2169 | +1.592 | 0.1113 |  |
| Education: high school or below (vs college) | +5.5671 | 4.1871 | ±8.3741 | +1.330 | 0.1837 |  |
| Site: UCSD (vs UAB) | +2.9614 | 2.3863 | ±4.7727 | +1.241 | 0.2146 |  |
| Site: UW (vs UAB) | -1.6480 | 1.8210 | ±3.6420 | -0.905 | 0.3655 |  |
| Season: spring (vs autumn) | +2.4057 | 1.9744 | ±3.9489 | +1.218 | 0.2231 |  |
| Season: summer (vs autumn) | +0.3088 | 2.4712 | ±4.9423 | +0.125 | 0.9005 |  |
| Season: winter (vs autumn) | +4.1971 | 2.2219 | ±4.4437 | +1.889 | 0.0589 | . |
| Age (years) | -0.0945 | 0.0681 | ±0.1361 | -1.388 | 0.1651 |  |
| BMI (kg/m2) | +0.1618 | 0.1200 | ±0.2399 | +1.349 | 0.1774 |  |
| Hypertension | +3.2694 | 1.7364 | ±3.4728 | +1.883 | 0.0597 | . |
| High cholesterol | -1.8027 | 1.6473 | ±3.2945 | -1.094 | 0.2738 |  |
| Kidney disease | +0.4217 | 3.5148 | ±7.0295 | +0.120 | 0.9045 |  |
| Circulatory disease | +1.4695 | 2.3079 | ±4.6158 | +0.637 | 0.5243 |  |
| MAG (mg/dL/h) | +0.0221 | 0.1024 | ±0.2048 | +0.215 | 0.8295 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **400**, R² = **0.0603**, Adj R² = **0.0261**, F-statistic = **1.76** (p = **0.0419**), Residual SE = **15.309** on **385** df, AIC = **3332.6**, BIC = **3392.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.6871** | 6.3170 | ±12.6340 | **+19.580** | **2.29e-85** | *** |
| Education: graduate level (vs college) | +2.5684 | 1.6025 | ±3.2049 | +1.603 | 0.1090 |  |
| Education: high school or below (vs college) | +5.6011 | 4.2747 | ±8.5494 | +1.310 | 0.1901 |  |
| Site: UCSD (vs UAB) | +3.0491 | 2.3977 | ±4.7953 | +1.272 | 0.2035 |  |
| Site: UW (vs UAB) | -1.6804 | 1.8274 | ±3.6547 | -0.920 | 0.3578 |  |
| Season: spring (vs autumn) | +2.3254 | 1.9773 | ±3.9546 | +1.176 | 0.2396 |  |
| Season: summer (vs autumn) | +0.2231 | 2.4594 | ±4.9188 | +0.091 | 0.9277 |  |
| Season: winter (vs autumn) | +4.1219 | 2.2431 | ±4.4862 | +1.838 | 0.0661 | . |
| Age (years) | -0.0879 | 0.0725 | ±0.1449 | -1.213 | 0.2252 |  |
| BMI (kg/m2) | +0.1590 | 0.1199 | ±0.2399 | +1.326 | 0.1850 |  |
| Hypertension | +3.3212 | 1.7400 | ±3.4799 | +1.909 | 0.0563 | . |
| High cholesterol | -1.8989 | 1.6324 | ±3.2648 | -1.163 | 0.2447 |  |
| Kidney disease | +0.6786 | 3.4864 | ±6.9727 | +0.195 | 0.8457 |  |
| Circulatory disease | +1.4365 | 2.3094 | ±4.6188 | +0.622 | 0.5339 |  |
| Avg. daily range (mg/dL) | -0.0179 | 0.0364 | ±0.0728 | -0.492 | 0.6229 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **400**, R² = **0.0595**, Adj R² = **0.0253**, F-statistic = **1.74** (p = **0.0461**), Residual SE = **15.315** on **385** df, AIC = **3332.9**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+121.9785** | 6.1581 | ±12.3162 | **+19.808** | **2.55e-87** | *** |
| Education: graduate level (vs college) | +2.5414 | 1.6069 | ±3.2138 | +1.582 | 0.1137 |  |
| Education: high school or below (vs college) | +5.5993 | 4.2045 | ±8.4091 | +1.332 | 0.1829 |  |
| Site: UCSD (vs UAB) | +2.9846 | 2.3728 | ±4.7455 | +1.258 | 0.2084 |  |
| Site: UW (vs UAB) | -1.6933 | 1.8220 | ±3.6440 | -0.929 | 0.3527 |  |
| Season: spring (vs autumn) | +2.3692 | 1.9729 | ±3.9458 | +1.201 | 0.2298 |  |
| Season: summer (vs autumn) | +0.2775 | 2.4786 | ±4.9573 | +0.112 | 0.9109 |  |
| Season: winter (vs autumn) | +4.1979 | 2.2230 | ±4.4460 | +1.888 | 0.0590 | . |
| Age (years) | -0.0953 | 0.0684 | ±0.1369 | -1.392 | 0.1640 |  |
| BMI (kg/m2) | +0.1604 | 0.1203 | ±0.2406 | +1.333 | 0.1825 |  |
| Hypertension | +3.2815 | 1.7426 | ±3.4853 | +1.883 | 0.0597 | . |
| High cholesterol | -1.8464 | 1.6199 | ±3.2398 | -1.140 | 0.2544 |  |
| Kidney disease | +0.4089 | 3.5007 | ±7.0015 | +0.117 | 0.9070 |  |
| Circulatory disease | +1.4593 | 2.3041 | ±4.6083 | +0.633 | 0.5265 |  |
| SD of daily means (mg/dL) | +0.0402 | 0.1990 | ±0.3981 | +0.202 | 0.8398 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **400**, R² = **0.0596**, Adj R² = **0.0254**, F-statistic = **1.74** (p = **0.0455**), Residual SE = **15.314** on **385** df, AIC = **3332.9**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.4911** | 18.6150 | ±37.2300 | **+6.795** | **1.08e-11** | *** |
| Education: graduate level (vs college) | +2.5627 | 1.6098 | ±3.2196 | +1.592 | 0.1114 |  |
| Education: high school or below (vs college) | +5.5673 | 4.1774 | ±8.3548 | +1.333 | 0.1826 |  |
| Site: UCSD (vs UAB) | +3.0065 | 2.3765 | ±4.7531 | +1.265 | 0.2059 |  |
| Site: UW (vs UAB) | -1.6673 | 1.8206 | ±3.6413 | -0.916 | 0.3598 |  |
| Season: spring (vs autumn) | +2.4322 | 1.9781 | ±3.9563 | +1.230 | 0.2189 |  |
| Season: summer (vs autumn) | +0.3380 | 2.4758 | ±4.9515 | +0.137 | 0.8914 |  |
| Season: winter (vs autumn) | +4.2277 | 2.2445 | ±4.4890 | +1.884 | 0.0596 | . |
| Age (years) | -0.0967 | 0.0692 | ±0.1385 | -1.396 | 0.1628 |  |
| BMI (kg/m2) | +0.1614 | 0.1199 | ±0.2398 | +1.346 | 0.1783 |  |
| Hypertension | +3.2764 | 1.7427 | ±3.4854 | +1.880 | 0.0601 | . |
| High cholesterol | -1.8285 | 1.6270 | ±3.2540 | -1.124 | 0.2611 |  |
| Kidney disease | +0.2865 | 3.5012 | ±7.0023 | +0.082 | 0.9348 |  |
| Circulatory disease | +1.5049 | 2.3029 | ±4.6057 | +0.653 | 0.5134 |  |
| Time in range 70-180, pooled (%) | -0.0442 | 0.1732 | ±0.3464 | -0.255 | 0.7987 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **400**, R² = **0.0595**, Adj R² = **0.0254**, F-statistic = **1.74** (p = **0.0458**), Residual SE = **15.315** on **385** df, AIC = **3332.9**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7586** | 19.0283 | ±38.0565 | **+6.609** | **3.87e-11** | *** |
| Education: graduate level (vs college) | +2.5653 | 1.6102 | ±3.2203 | +1.593 | 0.1111 |  |
| Education: high school or below (vs college) | +5.5716 | 4.1890 | ±8.3779 | +1.330 | 0.1835 |  |
| Site: UCSD (vs UAB) | +2.9962 | 2.3768 | ±4.7536 | +1.261 | 0.2075 |  |
| Site: UW (vs UAB) | -1.6721 | 1.8194 | ±3.6388 | -0.919 | 0.3581 |  |
| Season: spring (vs autumn) | +2.4211 | 1.9790 | ±3.9579 | +1.223 | 0.2212 |  |
| Season: summer (vs autumn) | +0.3386 | 2.4772 | ±4.9544 | +0.137 | 0.8913 |  |
| Season: winter (vs autumn) | +4.2203 | 2.2491 | ±4.4983 | +1.876 | 0.0606 | . |
| Age (years) | -0.0966 | 0.0696 | ±0.1393 | -1.387 | 0.1655 |  |
| BMI (kg/m2) | +0.1611 | 0.1202 | ±0.2405 | +1.340 | 0.1802 |  |
| Hypertension | +3.2783 | 1.7431 | ±3.4861 | +1.881 | 0.0600 | . |
| High cholesterol | -1.8359 | 1.6251 | ±3.2501 | -1.130 | 0.2586 |  |
| Kidney disease | +0.3098 | 3.5085 | ±7.0171 | +0.088 | 0.9296 |  |
| Circulatory disease | +1.4976 | 2.3021 | ±4.6043 | +0.651 | 0.5153 |  |
| Avg. daily time in range 70-180 (%) | -0.0362 | 0.1751 | ±0.3502 | -0.207 | 0.8361 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **400**, R² = **0.0595**, Adj R² = **0.0253**, F-statistic = **1.74** (p = **0.0461**), Residual SE = **15.315** on **385** df, AIC = **3332.9**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.0515** | 6.1993 | ±12.3986 | **+19.688** | **2.74e-86** | *** |
| Education: graduate level (vs college) | +2.5674 | 1.6077 | ±3.2155 | +1.597 | 0.1103 |  |
| Education: high school or below (vs college) | +5.5856 | 4.1639 | ±8.3279 | +1.341 | 0.1798 |  |
| Site: UCSD (vs UAB) | +3.0338 | 2.3818 | ±4.7635 | +1.274 | 0.2027 |  |
| Site: UW (vs UAB) | -1.6488 | 1.8375 | ±3.6751 | -0.897 | 0.3696 |  |
| Season: spring (vs autumn) | +2.3927 | 1.9653 | ±3.9306 | +1.218 | 0.2234 |  |
| Season: summer (vs autumn) | +0.2692 | 2.4690 | ±4.9379 | +0.109 | 0.9132 |  |
| Season: winter (vs autumn) | +4.1679 | 2.2279 | ±4.4558 | +1.871 | 0.0614 | . |
| Age (years) | -0.0949 | 0.0683 | ±0.1365 | -1.390 | 0.1644 |  |
| BMI (kg/m2) | +0.1628 | 0.1204 | ±0.2408 | +1.352 | 0.1763 |  |
| Hypertension | +3.3058 | 1.7371 | ±3.4743 | +1.903 | 0.0570 | . |
| High cholesterol | -1.8128 | 1.6298 | ±3.2595 | -1.112 | 0.2660 |  |
| Kidney disease | +0.4157 | 3.5117 | ±7.0234 | +0.118 | 0.9058 |  |
| Circulatory disease | +1.4791 | 2.3072 | ±4.6144 | +0.641 | 0.5215 |  |
| Time < 54 (%) | +0.1534 | 0.9289 | ±1.8577 | +0.165 | 0.8688 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **400**, R² = **0.0594**, Adj R² = **0.0252**, F-statistic = **1.74** (p = **0.0465**), Residual SE = **15.316** on **385** df, AIC = **3333.0**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.1475** | 6.1547 | ±12.3094 | **+19.846** | **1.19e-87** | *** |
| Education: graduate level (vs college) | +2.5687 | 1.6041 | ±3.2082 | +1.601 | 0.1093 |  |
| Education: high school or below (vs college) | +5.5737 | 4.1638 | ±8.3276 | +1.339 | 0.1807 |  |
| Site: UCSD (vs UAB) | +3.0001 | 2.3845 | ±4.7690 | +1.258 | 0.2083 |  |
| Site: UW (vs UAB) | -1.6676 | 1.8415 | ±3.6830 | -0.906 | 0.3652 |  |
| Season: spring (vs autumn) | +2.3842 | 1.9649 | ±3.9297 | +1.213 | 0.2250 |  |
| Season: summer (vs autumn) | +0.2830 | 2.4796 | ±4.9593 | +0.114 | 0.9091 |  |
| Season: winter (vs autumn) | +4.1695 | 2.2357 | ±4.4714 | +1.865 | 0.0622 | . |
| Age (years) | -0.0951 | 0.0685 | ±0.1370 | -1.389 | 0.1649 |  |
| BMI (kg/m2) | +0.1622 | 0.1204 | ±0.2408 | +1.347 | 0.1778 |  |
| Hypertension | +3.2995 | 1.7340 | ±3.4680 | +1.903 | 0.0571 | . |
| High cholesterol | -1.8295 | 1.6274 | ±3.2547 | -1.124 | 0.2609 |  |
| Kidney disease | +0.4219 | 3.5066 | ±7.0133 | +0.120 | 0.9042 |  |
| Circulatory disease | +1.4728 | 2.3084 | ±4.6168 | +0.638 | 0.5235 |  |
| Avg. daily time < 54 (%) | +0.0953 | 1.1963 | ±2.3927 | +0.080 | 0.9365 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **400**, R² = **0.0594**, Adj R² = **0.0252**, F-statistic = **1.74** (p = **0.0466**), Residual SE = **15.316** on **385** df, AIC = **3333.0**, BIC = **3392.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.1810** | 6.1796 | ±12.3592 | **+19.772** | **5.22e-87** | *** |
| Education: graduate level (vs college) | +2.5632 | 1.6089 | ±3.2178 | +1.593 | 0.1111 |  |
| Education: high school or below (vs college) | +5.5601 | 4.1620 | ±8.3240 | +1.336 | 0.1816 |  |
| Site: UCSD (vs UAB) | +2.9783 | 2.3898 | ±4.7795 | +1.246 | 0.2127 |  |
| Site: UW (vs UAB) | -1.6930 | 1.8164 | ±3.6328 | -0.932 | 0.3513 |  |
| Season: spring (vs autumn) | +2.3845 | 1.9707 | ±3.9414 | +1.210 | 0.2263 |  |
| Season: summer (vs autumn) | +0.2961 | 2.4765 | ±4.9531 | +0.120 | 0.9048 |  |
| Season: winter (vs autumn) | +4.1819 | 2.2267 | ±4.4534 | +1.878 | 0.0604 | . |
| Age (years) | -0.0948 | 0.0683 | ±0.1366 | -1.388 | 0.1652 |  |
| BMI (kg/m2) | +0.1620 | 0.1195 | ±0.2390 | +1.355 | 0.1753 |  |
| Hypertension | +3.2862 | 1.7205 | ±3.4410 | +1.910 | 0.0561 | . |
| High cholesterol | -1.8420 | 1.6256 | ±3.2513 | -1.133 | 0.2572 |  |
| Kidney disease | +0.4303 | 3.5070 | ±7.0139 | +0.123 | 0.9023 |  |
| Circulatory disease | +1.4647 | 2.3040 | ±4.6079 | +0.636 | 0.5250 |  |
| Time 54-69, pooled (%) | +0.0020 | 0.3786 | ±0.7572 | +0.005 | 0.9958 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **400**, R² = **0.0594**, Adj R² = **0.0252**, F-statistic = **1.74** (p = **0.0465**), Residual SE = **15.316** on **385** df, AIC = **3333.0**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.2268** | 6.1537 | ±12.3073 | **+19.862** | **8.60e-88** | *** |
| Education: graduate level (vs college) | +2.5549 | 1.6127 | ±3.2254 | +1.584 | 0.1131 |  |
| Education: high school or below (vs college) | +5.5350 | 4.1664 | ±8.3327 | +1.328 | 0.1840 |  |
| Site: UCSD (vs UAB) | +2.9674 | 2.3894 | ±4.7788 | +1.242 | 0.2143 |  |
| Site: UW (vs UAB) | -1.7156 | 1.8171 | ±3.6341 | -0.944 | 0.3451 |  |
| Season: spring (vs autumn) | +2.3903 | 1.9725 | ±3.9449 | +1.212 | 0.2256 |  |
| Season: summer (vs autumn) | +0.3010 | 2.4782 | ±4.9564 | +0.121 | 0.9033 |  |
| Season: winter (vs autumn) | +4.2052 | 2.2223 | ±4.4445 | +1.892 | 0.0585 | . |
| Age (years) | -0.0947 | 0.0683 | ±0.1366 | -1.388 | 0.1653 |  |
| BMI (kg/m2) | +0.1625 | 0.1195 | ±0.2391 | +1.360 | 0.1738 |  |
| Hypertension | +3.2699 | 1.7175 | ±3.4350 | +1.904 | 0.0569 | . |
| High cholesterol | -1.8538 | 1.6248 | ±3.2497 | -1.141 | 0.2539 |  |
| Kidney disease | +0.4302 | 3.5048 | ±7.0095 | +0.123 | 0.9023 |  |
| Circulatory disease | +1.4588 | 2.3028 | ±4.6056 | +0.633 | 0.5264 |  |
| Avg. daily time 54-69 (%) | -0.0331 | 0.3871 | ±0.7743 | -0.085 | 0.9319 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **400**, R² = **0.0594**, Adj R² = **0.0252**, F-statistic = **1.74** (p = **0.0465**), Residual SE = **15.316** on **385** df, AIC = **3333.0**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.1319** | 6.2101 | ±12.4202 | **+19.667** | **4.16e-86** | *** |
| Education: graduate level (vs college) | +2.5670 | 1.6078 | ±3.2156 | +1.597 | 0.1104 |  |
| Education: high school or below (vs college) | +5.5748 | 4.1584 | ±8.3169 | +1.341 | 0.1801 |  |
| Site: UCSD (vs UAB) | +2.9929 | 2.3954 | ±4.7908 | +1.249 | 0.2115 |  |
| Site: UW (vs UAB) | -1.6762 | 1.8243 | ±3.6486 | -0.919 | 0.3582 |  |
| Season: spring (vs autumn) | +2.3831 | 1.9676 | ±3.9351 | +1.211 | 0.2258 |  |
| Season: summer (vs autumn) | +0.2885 | 2.4762 | ±4.9524 | +0.117 | 0.9072 |  |
| Season: winter (vs autumn) | +4.1689 | 2.2323 | ±4.4645 | +1.868 | 0.0618 | . |
| Age (years) | -0.0947 | 0.0683 | ±0.1366 | -1.388 | 0.1652 |  |
| BMI (kg/m2) | +0.1619 | 0.1197 | ±0.2394 | +1.352 | 0.1764 |  |
| Hypertension | +3.2966 | 1.7233 | ±3.4466 | +1.913 | 0.0558 | . |
| High cholesterol | -1.8318 | 1.6294 | ±3.2588 | -1.124 | 0.2609 |  |
| Kidney disease | +0.4280 | 3.5094 | ±7.0187 | +0.122 | 0.9029 |  |
| Circulatory disease | +1.4704 | 2.3061 | ±4.6122 | +0.638 | 0.5237 |  |
| Time < 70 (%) | +0.0201 | 0.2958 | ±0.5917 | +0.068 | 0.9458 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **400**, R² = **0.0594**, Adj R² = **0.0252**, F-statistic = **1.74** (p = **0.0465**), Residual SE = **15.316** on **385** df, AIC = **3333.0**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.2108** | 6.1633 | ±12.3265 | **+19.829** | **1.68e-87** | *** |
| Education: graduate level (vs college) | +2.5581 | 1.6109 | ±3.2218 | +1.588 | 0.1123 |  |
| Education: high school or below (vs college) | +5.5450 | 4.1631 | ±8.3262 | +1.332 | 0.1829 |  |
| Site: UCSD (vs UAB) | +2.9689 | 2.3941 | ±4.7883 | +1.240 | 0.2149 |  |
| Site: UW (vs UAB) | -1.7088 | 1.8233 | ±3.6465 | -0.937 | 0.3486 |  |
| Season: spring (vs autumn) | +2.3875 | 1.9706 | ±3.9412 | +1.212 | 0.2257 |  |
| Season: summer (vs autumn) | +0.3009 | 2.4804 | ±4.9609 | +0.121 | 0.9034 |  |
| Season: winter (vs autumn) | +4.1959 | 2.2293 | ±4.4587 | +1.882 | 0.0598 | . |
| Age (years) | -0.0947 | 0.0683 | ±0.1366 | -1.386 | 0.1656 |  |
| BMI (kg/m2) | +0.1622 | 0.1197 | ±0.2394 | +1.355 | 0.1753 |  |
| Hypertension | +3.2756 | 1.7183 | ±3.4366 | +1.906 | 0.0566 | . |
| High cholesterol | -1.8502 | 1.6268 | ±3.2536 | -1.137 | 0.2554 |  |
| Kidney disease | +0.4317 | 3.5054 | ±7.0108 | +0.123 | 0.9020 |  |
| Circulatory disease | +1.4602 | 2.3042 | ±4.6085 | +0.634 | 0.5263 |  |
| Avg. daily time < 70 (%) | -0.0158 | 0.3209 | ±0.6417 | -0.049 | 0.9607 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **400**, R² = **0.0596**, Adj R² = **0.0254**, F-statistic = **1.74** (p = **0.0454**), Residual SE = **15.314** on **385** df, AIC = **3332.9**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+141.8826** | 69.5286 | ±139.0572 | **+2.041** | **0.0413** | * |
| Education: graduate level (vs college) | +2.5696 | 1.6081 | ±3.2161 | +1.598 | 0.1101 |  |
| Education: high school or below (vs college) | +5.5942 | 4.1720 | ±8.3440 | +1.341 | 0.1800 |  |
| Site: UCSD (vs UAB) | +3.0515 | 2.3739 | ±4.7477 | +1.285 | 0.1986 |  |
| Site: UW (vs UAB) | -1.6250 | 1.8261 | ±3.6523 | -0.890 | 0.3735 |  |
| Season: spring (vs autumn) | +2.3922 | 1.9690 | ±3.9381 | +1.215 | 0.2244 |  |
| Season: summer (vs autumn) | +0.2767 | 2.4671 | ±4.9343 | +0.112 | 0.9107 |  |
| Season: winter (vs autumn) | +4.1851 | 2.2224 | ±4.4447 | +1.883 | 0.0597 | . |
| Age (years) | -0.0961 | 0.0683 | ±0.1367 | -1.406 | 0.1597 |  |
| BMI (kg/m2) | +0.1631 | 0.1198 | ±0.2397 | +1.361 | 0.1734 |  |
| Hypertension | +3.3023 | 1.7378 | ±3.4757 | +1.900 | 0.0574 | . |
| High cholesterol | -1.7905 | 1.6354 | ±3.2708 | -1.095 | 0.2736 |  |
| Kidney disease | +0.3024 | 3.5065 | ±7.0129 | +0.086 | 0.9313 |  |
| Circulatory disease | +1.5027 | 2.3099 | ±4.6198 | +0.651 | 0.5153 |  |
| Time 54-250, pooled (%) | -0.1985 | 0.6959 | ±1.3918 | -0.285 | 0.7755 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **400**, R² = **0.0598**, Adj R² = **0.0256**, F-statistic = **1.75** (p = **0.0447**), Residual SE = **15.313** on **385** df, AIC = **3332.8**, BIC = **3392.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +150.1421 | 83.7612 | ±167.5223 | +1.793 | 0.0731 | . |
| Education: graduate level (vs college) | +2.5835 | 1.6083 | ±3.2167 | +1.606 | 0.1082 |  |
| Education: high school or below (vs college) | +5.6081 | 4.1784 | ±8.3568 | +1.342 | 0.1795 |  |
| Site: UCSD (vs UAB) | +3.0519 | 2.3729 | ±4.7458 | +1.286 | 0.1984 |  |
| Site: UW (vs UAB) | -1.6034 | 1.8214 | ±3.6428 | -0.880 | 0.3787 |  |
| Season: spring (vs autumn) | +2.3789 | 1.9700 | ±3.9400 | +1.208 | 0.2272 |  |
| Season: summer (vs autumn) | +0.2773 | 2.4697 | ±4.9394 | +0.112 | 0.9106 |  |
| Season: winter (vs autumn) | +4.1758 | 2.2218 | ±4.4436 | +1.879 | 0.0602 | . |
| Age (years) | -0.0974 | 0.0689 | ±0.1378 | -1.414 | 0.1574 |  |
| BMI (kg/m2) | +0.1624 | 0.1198 | ±0.2395 | +1.356 | 0.1751 |  |
| Hypertension | +3.3160 | 1.7367 | ±3.4735 | +1.909 | 0.0562 | . |
| High cholesterol | -1.7916 | 1.6319 | ±3.2639 | -1.098 | 0.2723 |  |
| Kidney disease | +0.2420 | 3.5084 | ±7.0167 | +0.069 | 0.9450 |  |
| Circulatory disease | +1.5200 | 2.3101 | ±4.6203 | +0.658 | 0.5106 |  |
| Avg. daily time 54-250 (%) | -0.2802 | 0.8334 | ±1.6669 | -0.336 | 0.7368 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **400**, R² = **0.0596**, Adj R² = **0.0254**, F-statistic = **1.74** (p = **0.0456**), Residual SE = **15.315** on **385** df, AIC = **3332.9**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.1837** | 6.1230 | ±12.2460 | **+19.955** | **1.36e-88** | *** |
| Education: graduate level (vs college) | +2.5518 | 1.6144 | ±3.2287 | +1.581 | 0.1140 |  |
| Education: high school or below (vs college) | +5.5277 | 4.1518 | ±8.3037 | +1.331 | 0.1831 |  |
| Site: UCSD (vs UAB) | +2.9716 | 2.3755 | ±4.7510 | +1.251 | 0.2110 |  |
| Site: UW (vs UAB) | -1.7117 | 1.8286 | ±3.6571 | -0.936 | 0.3492 |  |
| Season: spring (vs autumn) | +2.4451 | 1.9935 | ±3.9870 | +1.227 | 0.2200 |  |
| Season: summer (vs autumn) | +0.3614 | 2.4881 | ±4.9761 | +0.145 | 0.8845 |  |
| Season: winter (vs autumn) | +4.2660 | 2.2855 | ±4.5711 | +1.867 | 0.0620 | . |
| Age (years) | -0.0968 | 0.0698 | ±0.1397 | -1.386 | 0.1658 |  |
| BMI (kg/m2) | +0.1617 | 0.1200 | ±0.2399 | +1.348 | 0.1777 |  |
| Hypertension | +3.2485 | 1.7418 | ±3.4835 | +1.865 | 0.0622 | . |
| High cholesterol | -1.8576 | 1.6192 | ±3.2384 | -1.147 | 0.2513 |  |
| Kidney disease | +0.2966 | 3.5171 | ±7.0342 | +0.084 | 0.9328 |  |
| Circulatory disease | +1.4910 | 2.3003 | ±4.6007 | +0.648 | 0.5169 |  |
| Time 181-250, pooled (%) | +0.0516 | 0.2291 | ±0.4582 | +0.225 | 0.8218 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **400**, R² = **0.0596**, Adj R² = **0.0254**, F-statistic = **1.74** (p = **0.0457**), Residual SE = **15.315** on **385** df, AIC = **3332.9**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.1905** | 6.1314 | ±12.2629 | **+19.928** | **2.30e-88** | *** |
| Education: graduate level (vs college) | +2.5513 | 1.6149 | ±3.2297 | +1.580 | 0.1141 |  |
| Education: high school or below (vs college) | +5.5331 | 4.1559 | ±8.3117 | +1.331 | 0.1831 |  |
| Site: UCSD (vs UAB) | +2.9749 | 2.3756 | ±4.7512 | +1.252 | 0.2105 |  |
| Site: UW (vs UAB) | -1.7112 | 1.8304 | ±3.6607 | -0.935 | 0.3498 |  |
| Season: spring (vs autumn) | +2.4412 | 1.9958 | ±3.9916 | +1.223 | 0.2213 |  |
| Season: summer (vs autumn) | +0.3610 | 2.4892 | ±4.9785 | +0.145 | 0.8847 |  |
| Season: winter (vs autumn) | +4.2643 | 2.2933 | ±4.5865 | +1.859 | 0.0630 | . |
| Age (years) | -0.0966 | 0.0698 | ±0.1396 | -1.384 | 0.1663 |  |
| BMI (kg/m2) | +0.1615 | 0.1202 | ±0.2403 | +1.344 | 0.1789 |  |
| Hypertension | +3.2489 | 1.7437 | ±3.4873 | +1.863 | 0.0624 | . |
| High cholesterol | -1.8584 | 1.6198 | ±3.2396 | -1.147 | 0.2513 |  |
| Kidney disease | +0.3047 | 3.5177 | ±7.0353 | +0.087 | 0.9310 |  |
| Circulatory disease | +1.4905 | 2.2999 | ±4.5998 | +0.648 | 0.5169 |  |
| Avg. daily time 181-250 (%) | +0.0473 | 0.2243 | ±0.4486 | +0.211 | 0.8332 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **400**, R² = **0.0596**, Adj R² = **0.0254**, F-statistic = **1.74** (p = **0.0455**), Residual SE = **15.314** on **385** df, AIC = **3332.9**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.1891** | 6.1279 | ±12.2559 | **+19.940** | **1.84e-88** | *** |
| Education: graduate level (vs college) | +2.5529 | 1.6143 | ±3.2285 | +1.581 | 0.1138 |  |
| Education: high school or below (vs college) | +5.5305 | 4.1537 | ±8.3074 | +1.331 | 0.1830 |  |
| Site: UCSD (vs UAB) | +2.9723 | 2.3755 | ±4.7511 | +1.251 | 0.2109 |  |
| Site: UW (vs UAB) | -1.7078 | 1.8282 | ±3.6564 | -0.934 | 0.3502 |  |
| Season: spring (vs autumn) | +2.4393 | 1.9919 | ±3.9838 | +1.225 | 0.2207 |  |
| Season: summer (vs autumn) | +0.3597 | 2.4865 | ±4.9731 | +0.145 | 0.8850 |  |
| Season: winter (vs autumn) | +4.2642 | 2.2805 | ±4.5610 | +1.870 | 0.0615 | . |
| Age (years) | -0.0969 | 0.0698 | ±0.1397 | -1.387 | 0.1654 |  |
| BMI (kg/m2) | +0.1618 | 0.1199 | ±0.2399 | +1.349 | 0.1774 |  |
| Hypertension | +3.2494 | 1.7422 | ±3.4844 | +1.865 | 0.0622 | . |
| High cholesterol | -1.8531 | 1.6202 | ±3.2403 | -1.144 | 0.2527 |  |
| Kidney disease | +0.2819 | 3.5210 | ±7.0420 | +0.080 | 0.9362 |  |
| Circulatory disease | +1.4934 | 2.3009 | ±4.6019 | +0.649 | 0.5163 |  |
| Time > 180 (%) | +0.0472 | 0.2076 | ±0.4152 | +0.228 | 0.8200 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **400**, R² = **0.0596**, Adj R² = **0.0254**, F-statistic = **1.74** (p = **0.0454**), Residual SE = **15.314** on **385** df, AIC = **3332.9**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.1991** | 6.1366 | ±12.2732 | **+19.913** | **3.13e-88** | *** |
| Education: graduate level (vs college) | +2.5518 | 1.6147 | ±3.2293 | +1.580 | 0.1140 |  |
| Education: high school or below (vs college) | +5.5337 | 4.1559 | ±8.3117 | +1.332 | 0.1830 |  |
| Site: UCSD (vs UAB) | +2.9762 | 2.3751 | ±4.7502 | +1.253 | 0.2102 |  |
| Site: UW (vs UAB) | -1.7092 | 1.8300 | ±3.6601 | -0.934 | 0.3503 |  |
| Season: spring (vs autumn) | +2.4411 | 1.9942 | ±3.9884 | +1.224 | 0.2209 |  |
| Season: summer (vs autumn) | +0.3653 | 2.4878 | ±4.9757 | +0.147 | 0.8833 |  |
| Season: winter (vs autumn) | +4.2709 | 2.2878 | ±4.5757 | +1.867 | 0.0619 | . |
| Age (years) | -0.0969 | 0.0698 | ±0.1396 | -1.389 | 0.1649 |  |
| BMI (kg/m2) | +0.1615 | 0.1201 | ±0.2402 | +1.344 | 0.1788 |  |
| Hypertension | +3.2466 | 1.7441 | ±3.4882 | +1.861 | 0.0627 | . |
| High cholesterol | -1.8565 | 1.6203 | ±3.2406 | -1.146 | 0.2519 |  |
| Kidney disease | +0.2752 | 3.5216 | ±7.0432 | +0.078 | 0.9377 |  |
| Circulatory disease | +1.4961 | 2.2998 | ±4.5995 | +0.651 | 0.5153 |  |
| Avg. daily time > 180 (%) | +0.0478 | 0.2044 | ±0.4087 | +0.234 | 0.8149 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **400**, R² = **0.0595**, Adj R² = **0.0253**, F-statistic = **1.74** (p = **0.0462**), Residual SE = **15.315** on **385** df, AIC = **3332.9**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.2158** | 6.1634 | ±12.3267 | **+19.829** | **1.66e-87** | *** |
| Education: graduate level (vs college) | +2.5756 | 1.6054 | ±3.2108 | +1.604 | 0.1086 |  |
| Education: high school or below (vs college) | +5.5333 | 4.1531 | ±8.3061 | +1.332 | 0.1827 |  |
| Site: UCSD (vs UAB) | +2.9836 | 2.3730 | ±4.7459 | +1.257 | 0.2086 |  |
| Site: UW (vs UAB) | -1.6955 | 1.8245 | ±3.6489 | -0.929 | 0.3527 |  |
| Season: spring (vs autumn) | +2.4075 | 1.9732 | ±3.9463 | +1.220 | 0.2224 |  |
| Season: summer (vs autumn) | +0.3462 | 2.4782 | ±4.9563 | +0.140 | 0.8889 |  |
| Season: winter (vs autumn) | +4.2140 | 2.2484 | ±4.4967 | +1.874 | 0.0609 | . |
| Age (years) | -0.0956 | 0.0689 | ±0.1378 | -1.387 | 0.1655 |  |
| BMI (kg/m2) | +0.1605 | 0.1217 | ±0.2434 | +1.319 | 0.1873 |  |
| Hypertension | +3.2612 | 1.7509 | ±3.5019 | +1.863 | 0.0625 | . |
| High cholesterol | -1.8419 | 1.6230 | ±3.2460 | -1.135 | 0.2564 |  |
| Kidney disease | +0.4279 | 3.5072 | ±7.0145 | +0.122 | 0.9029 |  |
| Circulatory disease | +1.4979 | 2.2983 | ±4.5966 | +0.652 | 0.5146 |  |
| Nocturnal time > 180 (%) | +0.0302 | 0.2067 | ±0.4134 | +0.146 | 0.8840 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **400**, R² = **0.0599**, Adj R² = **0.0257**, F-statistic = **1.75** (p = **0.0441**), Residual SE = **15.312** on **385** df, AIC = **3332.8**, BIC = **3392.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.0856** | 6.0609 | ±12.1219 | **+20.143** | **3.10e-90** | *** |
| Education: graduate level (vs college) | +2.5914 | 1.6050 | ±3.2099 | +1.615 | 0.1064 |  |
| Education: high school or below (vs college) | +5.5752 | 4.1718 | ±8.3436 | +1.336 | 0.1814 |  |
| Site: UCSD (vs UAB) | +2.9160 | 2.3900 | ±4.7801 | +1.220 | 0.2224 |  |
| Site: UW (vs UAB) | -1.6942 | 1.8218 | ±3.6436 | -0.930 | 0.3524 |  |
| Season: spring (vs autumn) | +2.4530 | 1.9750 | ±3.9501 | +1.242 | 0.2142 |  |
| Season: summer (vs autumn) | +0.3606 | 2.4705 | ±4.9411 | +0.146 | 0.8839 |  |
| Season: winter (vs autumn) | +4.2443 | 2.2330 | ±4.4659 | +1.901 | 0.0573 | . |
| Age (years) | -0.0976 | 0.0694 | ±0.1388 | -1.407 | 0.1595 |  |
| BMI (kg/m2) | +0.1646 | 0.1189 | ±0.2378 | +1.384 | 0.1662 |  |
| Hypertension | +3.2461 | 1.7428 | ±3.4856 | +1.863 | 0.0625 | . |
| High cholesterol | -1.8240 | 1.6244 | ±3.2488 | -1.123 | 0.2615 |  |
| Kidney disease | +0.3209 | 3.5009 | ±7.0018 | +0.092 | 0.9270 |  |
| Circulatory disease | +1.5064 | 2.2926 | ±4.5852 | +0.657 | 0.5111 |  |
| Any reading > 250 during wear (0/1) | +0.9403 | 2.2585 | ±4.5169 | +0.416 | 0.6772 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **400**, R² = **0.0596**, Adj R² = **0.0254**, F-statistic = **1.74** (p = **0.0456**), Residual SE = **15.314** on **385** df, AIC = **3332.9**, BIC = **3392.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.2192** | 6.1467 | ±12.2934 | **+19.884** | **5.64e-88** | *** |
| Education: graduate level (vs college) | +2.5642 | 1.6157 | ±3.2315 | +1.587 | 0.1125 |  |
| Education: high school or below (vs college) | +5.5602 | 4.1739 | ±8.3478 | +1.332 | 0.1828 |  |
| Site: UCSD (vs UAB) | +2.9794 | 2.3782 | ±4.7564 | +1.253 | 0.2103 |  |
| Site: UW (vs UAB) | -1.6779 | 1.8220 | ±3.6439 | -0.921 | 0.3571 |  |
| Season: spring (vs autumn) | +2.3802 | 1.9761 | ±3.9523 | +1.204 | 0.2284 |  |
| Season: summer (vs autumn) | +0.3209 | 2.4740 | ±4.9481 | +0.130 | 0.8968 |  |
| Season: winter (vs autumn) | +4.2171 | 2.2346 | ±4.4692 | +1.887 | 0.0591 | . |
| Age (years) | -0.0966 | 0.0692 | ±0.1383 | -1.396 | 0.1627 |  |
| BMI (kg/m2) | +0.1622 | 0.1198 | ±0.2396 | +1.354 | 0.1758 |  |
| Hypertension | +3.2705 | 1.7406 | ±3.4811 | +1.879 | 0.0602 | . |
| High cholesterol | -1.8215 | 1.6346 | ±3.2691 | -1.114 | 0.2651 |  |
| Kidney disease | +0.2600 | 3.5299 | ±7.0597 | +0.074 | 0.9413 |  |
| Circulatory disease | +1.4943 | 2.3088 | ±4.6176 | +0.647 | 0.5175 |  |
| Time > 250 (%) | +0.3103 | 1.6177 | ±3.2354 | +0.192 | 0.8479 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 400)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **400**, R² = **0.0599**, Adj R² = **0.0257**, F-statistic = **1.75** (p = **0.0439**), Residual SE = **15.312** on **385** df, AIC = **3332.8**, BIC = **3392.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.2681** | 6.1498 | ±12.2996 | **+19.882** | **5.87e-88** | *** |
| Education: graduate level (vs college) | +2.5687 | 1.6165 | ±3.2329 | +1.589 | 0.1120 |  |
| Education: high school or below (vs college) | +5.5685 | 4.1713 | ±8.3427 | +1.335 | 0.1819 |  |
| Site: UCSD (vs UAB) | +2.9907 | 2.3738 | ±4.7475 | +1.260 | 0.2077 |  |
| Site: UW (vs UAB) | -1.6729 | 1.8222 | ±3.6445 | -0.918 | 0.3586 |  |
| Season: spring (vs autumn) | +2.3774 | 1.9777 | ±3.9554 | +1.202 | 0.2293 |  |
| Season: summer (vs autumn) | +0.3310 | 2.4754 | ±4.9509 | +0.134 | 0.8936 |  |
| Season: winter (vs autumn) | +4.2380 | 2.2366 | ±4.4732 | +1.895 | 0.0581 | . |
| Age (years) | -0.0977 | 0.0691 | ±0.1383 | -1.413 | 0.1577 |  |
| BMI (kg/m2) | +0.1616 | 0.1198 | ±0.2396 | +1.349 | 0.1773 |  |
| Hypertension | +3.2668 | 1.7409 | ±3.4819 | +1.876 | 0.0606 | . |
| High cholesterol | -1.8223 | 1.6290 | ±3.2579 | -1.119 | 0.2633 |  |
| Kidney disease | +0.1561 | 3.5352 | ±7.0703 | +0.044 | 0.9648 |  |
| Circulatory disease | +1.5158 | 2.3052 | ±4.6103 | +0.658 | 0.5108 |  |
| Avg. daily time > 250 (%) | +0.4698 | 1.5657 | ±3.1315 | +0.300 | 0.7641 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Healthy group (no diabetes + pre-diabetes / lifestyle) - Home environment

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 120 single-predictor tests; 14 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 400): best single predictor out of sample is **GMI** (CV R² 0.086 vs 0.081 for covariates alone, gain +0.005; -0.116 per SD, p = 0.020). Raw p < 0.05 (FDR not applicable here): Mean glucose (p = 0.020), GMI (p = 0.020), TIR 70-180 (pooled) (p = 0.030), %181-250 (pooled) (p = 0.034), %181-250 (daily avg) (p = 0.042).
- **Indoor temperature, mean (deg C)** (n = 400): best single predictor out of sample is **%<54 (pooled)** (CV R² 0.220 vs 0.213 for covariates alone, gain +0.006; +0.222 per SD, p = 0.016). Raw p < 0.05 (FDR not applicable here): %<54 (pooled) (p = 0.016), %<70 (pooled) (p = 0.030), %<70 (daily avg) (p = 0.039), %54-69 (daily avg) (p = 0.043).
- **Indoor relative humidity, mean (%)** (n = 400): best single predictor out of sample is **%<54 (daily avg)** (CV R² 0.202 vs 0.198 for covariates alone, gain +0.004; -0.476 per SD, p = 0.010). Raw p < 0.05 (FDR not applicable here): %<54 (daily avg) (p = 0.010), %<54 (pooled) (p = 0.028), Mean/SD (p = 0.039).
- **Indoor VOC index, mean** (n = 400): best single predictor out of sample is **%54-250 (daily avg)** (CV R² -0.056 vs -0.055 for covariates alone, gain -0.001; -0.301 per SD, p = 0.737). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.

**Most predictable outcomes (largest out-of-sample gain over covariates):** Indoor temperature, mean (deg C) (+0.006, via %<54 (pooled)); Indoor PM2.5, log(1 + mean ug/m3) (+0.005, via GMI); Indoor relative humidity, mean (%) (+0.004, via %<54 (daily avg)); Indoor VOC index, mean (-0.001, via %54-250 (daily avg)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band < 54 (0 FDR-significant / 3 raw-significant of 8); CGM level (0 FDR-significant / 2 raw-significant of 12); Range 70-180 (0 FDR-significant / 2 raw-significant of 8).
Level metrics: 0 FDR-significant (2 raw); variability metrics: 0 FDR-significant (1 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Indoor PM2.5, log(1 + mean ug/m3) (Mean glucose, ΔAIC -5.8); Indoor temperature, mean (%<54 (pooled), ΔAIC -4.8).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
