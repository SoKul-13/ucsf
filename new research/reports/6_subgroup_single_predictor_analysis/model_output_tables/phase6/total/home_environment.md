# Phase 6 model output tables - All (analysis base) - Total analysis base - Home environment

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models. [Index of all model-output files](../../README.md)


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 2,100; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **2100**, R² = **0.1564**, Adj R² = **0.1512**, F-statistic = **29.76** (p = **4.62e-68**), Residual SE = **0.887** on **2086** df, AIC = **5469.4**, BIC = **5548.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5351** | 0.1632 | ±0.3264 | **+15.532** | **2.10e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1093** | 0.0397 | ±0.0794 | **-2.751** | **0.0059** | ** |
| **Education: high school or below (vs college)** | **+0.4907** | 0.0817 | ±0.1633 | **+6.008** | **1.88e-09** | *** |
| Site: UCSD (vs UAB) | +0.0353 | 0.0490 | ±0.0980 | +0.721 | 0.4712 |  |
| **Site: UW (vs UAB)** | **-0.3550** | 0.0504 | ±0.1008 | **-7.043** | **1.88e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1664** | 0.0530 | ±0.1061 | **-3.137** | **0.0017** | ** |
| Season: summer (vs autumn) | +0.0083 | 0.0564 | ±0.1129 | +0.147 | 0.8827 |  |
| Season: winter (vs autumn) | -0.0301 | 0.0564 | ±0.1128 | -0.534 | 0.5934 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.719** | **2.81e-18** | *** |
| **BMI (kg/m2)** | **+0.0147** | 0.0031 | ±0.0062 | **+4.711** | **2.46e-06** | *** |
| **Hypertension** | **+0.1158** | 0.0418 | ±0.0837 | **+2.768** | **0.0056** | ** |
| High cholesterol | -0.0450 | 0.0393 | ±0.0786 | -1.145 | 0.2522 |  |
| Kidney disease | -0.0587 | 0.0587 | ±0.1174 | -1.000 | 0.3175 |  |
| Circulatory disease | +0.1159 | 0.0593 | ±0.1185 | +1.956 | 0.0504 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **2100**, R² = **0.1616**, Adj R² = **0.1560**, F-statistic = **28.71** (p = **5.13e-70**), Residual SE = **0.884** on **2085** df, AIC = **5458.5**, BIC = **5543.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1789** | 0.1990 | ±0.3980 | **+10.949** | **6.73e-28** | *** |
| **Education: graduate level (vs college)** | **-0.1011** | 0.0398 | ±0.0796 | **-2.540** | **0.0111** | * |
| **Education: high school or below (vs college)** | **+0.4620** | 0.0806 | ±0.1612 | **+5.731** | **1.00e-08** | *** |
| Site: UCSD (vs UAB) | +0.0429 | 0.0490 | ±0.0979 | +0.876 | 0.3813 |  |
| **Site: UW (vs UAB)** | **-0.3459** | 0.0502 | ±0.1004 | **-6.890** | **5.57e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1569** | 0.0529 | ±0.1058 | **-2.965** | **0.0030** | ** |
| Season: summer (vs autumn) | +0.0121 | 0.0563 | ±0.1126 | +0.215 | 0.8298 |  |
| Season: winter (vs autumn) | -0.0255 | 0.0562 | ±0.1125 | -0.453 | 0.6507 |  |
| **Age (years)** | **-0.0162** | 0.0018 | ±0.0036 | **-8.930** | **4.28e-19** | *** |
| **BMI (kg/m2)** | **+0.0134** | 0.0032 | ±0.0064 | **+4.201** | **2.66e-05** | *** |
| **Hypertension** | **+0.1012** | 0.0418 | ±0.0837 | **+2.419** | **0.0156** | * |
| High cholesterol | -0.0579 | 0.0392 | ±0.0784 | -1.475 | 0.1401 |  |
| Kidney disease | -0.0712 | 0.0585 | ±0.1169 | -1.217 | 0.2235 |  |
| Circulatory disease | +0.1096 | 0.0595 | ±0.1190 | +1.841 | 0.0656 | . |
| **HbA1c (%)** | **+0.0693** | 0.0236 | ±0.0473 | **+2.933** | **0.0034** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **2100**, R² = **0.1570**, Adj R² = **0.1514**, F-statistic = **27.75** (p = **1.27e-67**), Residual SE = **0.887** on **2085** df, AIC = **5470.0**, BIC = **5554.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4567** | 0.1790 | ±0.3581 | **+13.722** | **7.54e-43** | *** |
| **Education: graduate level (vs college)** | **-0.1076** | 0.0398 | ±0.0796 | **-2.703** | **0.0069** | ** |
| **Education: high school or below (vs college)** | **+0.4819** | 0.0813 | ±0.1625 | **+5.930** | **3.03e-09** | *** |
| Site: UCSD (vs UAB) | +0.0389 | 0.0490 | ±0.0979 | +0.794 | 0.4274 |  |
| **Site: UW (vs UAB)** | **-0.3531** | 0.0504 | ±0.1007 | **-7.010** | **2.39e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1658** | 0.0531 | ±0.1062 | **-3.123** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0097 | 0.0565 | ±0.1129 | +0.171 | 0.8639 |  |
| Season: winter (vs autumn) | -0.0289 | 0.0564 | ±0.1129 | -0.512 | 0.6089 |  |
| **Age (years)** | **-0.0159** | 0.0018 | ±0.0036 | **-8.762** | **1.91e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.571** | **4.85e-06** | *** |
| **Hypertension** | **+0.1109** | 0.0424 | ±0.0847 | **+2.618** | **0.0089** | ** |
| High cholesterol | -0.0479 | 0.0393 | ±0.0785 | -1.219 | 0.2228 |  |
| Kidney disease | -0.0667 | 0.0587 | ±0.1175 | -1.136 | 0.2560 |  |
| Circulatory disease | +0.1138 | 0.0596 | ±0.1192 | +1.910 | 0.0561 | . |
| Mean glucose (mg/dL) | +0.0007 | 0.0007 | ±0.0014 | +1.011 | 0.3121 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **2100**, R² = **0.1570**, Adj R² = **0.1514**, F-statistic = **27.75** (p = **1.27e-67**), Residual SE = **0.887** on **2085** df, AIC = **5470.0**, BIC = **5554.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.3573** | 0.2369 | ±0.4739 | **+9.949** | **2.56e-23** | *** |
| **Education: graduate level (vs college)** | **-0.1076** | 0.0398 | ±0.0796 | **-2.703** | **0.0069** | ** |
| **Education: high school or below (vs college)** | **+0.4819** | 0.0813 | ±0.1625 | **+5.930** | **3.03e-09** | *** |
| Site: UCSD (vs UAB) | +0.0389 | 0.0490 | ±0.0979 | +0.794 | 0.4274 |  |
| **Site: UW (vs UAB)** | **-0.3531** | 0.0504 | ±0.1007 | **-7.010** | **2.39e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1658** | 0.0531 | ±0.1062 | **-3.123** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0097 | 0.0565 | ±0.1129 | +0.171 | 0.8639 |  |
| Season: winter (vs autumn) | -0.0289 | 0.0564 | ±0.1129 | -0.512 | 0.6089 |  |
| **Age (years)** | **-0.0159** | 0.0018 | ±0.0036 | **-8.762** | **1.91e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.571** | **4.85e-06** | *** |
| **Hypertension** | **+0.1109** | 0.0424 | ±0.0847 | **+2.618** | **0.0089** | ** |
| High cholesterol | -0.0479 | 0.0393 | ±0.0785 | -1.219 | 0.2228 |  |
| Kidney disease | -0.0667 | 0.0587 | ±0.1175 | -1.136 | 0.2560 |  |
| Circulatory disease | +0.1138 | 0.0596 | ±0.1192 | +1.910 | 0.0561 | . |
| GMI (%) | +0.0300 | 0.0297 | ±0.0594 | +1.011 | 0.3121 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **2100**, R² = **0.1575**, Adj R² = **0.1518**, F-statistic = **27.84** (p = **7.31e-68**), Residual SE = **0.887** on **2085** df, AIC = **5468.8**, BIC = **5553.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4309** | 0.1781 | ±0.3562 | **+13.649** | **2.05e-42** | *** |
| **Education: graduate level (vs college)** | **-0.1067** | 0.0398 | ±0.0796 | **-2.681** | **0.0073** | ** |
| **Education: high school or below (vs college)** | **+0.4796** | 0.0811 | ±0.1623 | **+5.910** | **3.41e-09** | *** |
| Site: UCSD (vs UAB) | +0.0389 | 0.0489 | ±0.0979 | +0.794 | 0.4271 |  |
| **Site: UW (vs UAB)** | **-0.3535** | 0.0504 | ±0.1008 | **-7.016** | **2.28e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1670** | 0.0531 | ±0.1061 | **-3.148** | **0.0016** | ** |
| Season: summer (vs autumn) | +0.0101 | 0.0564 | ±0.1128 | +0.178 | 0.8584 |  |
| Season: winter (vs autumn) | -0.0299 | 0.0564 | ±0.1128 | -0.530 | 0.5960 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.726** | **2.64e-18** | *** |
| **BMI (kg/m2)** | **+0.0141** | 0.0032 | ±0.0064 | **+4.420** | **9.87e-06** | *** |
| **Hypertension** | **+0.1105** | 0.0422 | ±0.0845 | **+2.617** | **0.0089** | ** |
| High cholesterol | -0.0491 | 0.0393 | ±0.0786 | -1.249 | 0.2115 |  |
| Kidney disease | -0.0659 | 0.0583 | ±0.1167 | -1.129 | 0.2587 |  |
| Circulatory disease | +0.1137 | 0.0595 | ±0.1190 | +1.912 | 0.0559 | . |
| Nocturnal mean 00-06h (mg/dL) | +0.0010 | 0.0007 | ±0.0014 | +1.328 | 0.1841 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.1577**, Adj R² = **0.1520**, F-statistic = **27.88** (p = **5.92e-68**), Residual SE = **0.886** on **2085** df, AIC = **5468.4**, BIC = **5553.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4836** | 0.1650 | ±0.3299 | **+15.054** | **3.23e-51** | *** |
| **Education: graduate level (vs college)** | **-0.1052** | 0.0398 | ±0.0796 | **-2.641** | **0.0083** | ** |
| **Education: high school or below (vs college)** | **+0.4794** | 0.0816 | ±0.1633 | **+5.872** | **4.30e-09** | *** |
| Site: UCSD (vs UAB) | +0.0420 | 0.0490 | ±0.0980 | +0.858 | 0.3908 |  |
| **Site: UW (vs UAB)** | **-0.3495** | 0.0503 | ±0.1006 | **-6.950** | **3.65e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1651** | 0.0531 | ±0.1062 | **-3.108** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0098 | 0.0564 | ±0.1128 | +0.174 | 0.8620 |  |
| Season: winter (vs autumn) | -0.0283 | 0.0564 | ±0.1128 | -0.502 | 0.6158 |  |
| **Age (years)** | **-0.0161** | 0.0018 | ±0.0037 | **-8.813** | **1.21e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.593** | **4.37e-06** | *** |
| **Hypertension** | **+0.1077** | 0.0422 | ±0.0844 | **+2.554** | **0.0107** | * |
| High cholesterol | -0.0480 | 0.0393 | ±0.0786 | -1.222 | 0.2216 |  |
| Kidney disease | -0.0780 | 0.0584 | ±0.1168 | -1.335 | 0.1818 |  |
| Circulatory disease | +0.1125 | 0.0596 | ±0.1192 | +1.887 | 0.0592 | . |
| Glucose SD, pooled (mg/dL) | +0.0030 | 0.0018 | ±0.0036 | +1.654 | 0.0981 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.1572**, Adj R² = **0.1515**, F-statistic = **27.78** (p = **1.04e-67**), Residual SE = **0.887** on **2085** df, AIC = **5469.6**, BIC = **5554.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4940** | 0.1652 | ±0.3303 | **+15.101** | **1.60e-51** | *** |
| **Education: graduate level (vs college)** | **-0.1064** | 0.0398 | ±0.0796 | **-2.673** | **0.0075** | ** |
| **Education: high school or below (vs college)** | **+0.4815** | 0.0818 | ±0.1637 | **+5.883** | **4.02e-09** | *** |
| Site: UCSD (vs UAB) | +0.0403 | 0.0490 | ±0.0980 | +0.823 | 0.4105 |  |
| **Site: UW (vs UAB)** | **-0.3512** | 0.0503 | ±0.1007 | **-6.978** | **3.00e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1651** | 0.0531 | ±0.1062 | **-3.108** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0100 | 0.0565 | ±0.1129 | +0.178 | 0.8588 |  |
| Season: winter (vs autumn) | -0.0281 | 0.0565 | ±0.1129 | -0.498 | 0.6186 |  |
| **Age (years)** | **-0.0161** | 0.0018 | ±0.0037 | **-8.795** | **1.43e-18** | *** |
| **BMI (kg/m2)** | **+0.0145** | 0.0031 | ±0.0063 | **+4.630** | **3.66e-06** | *** |
| **Hypertension** | **+0.1095** | 0.0422 | ±0.0844 | **+2.594** | **0.0095** | ** |
| High cholesterol | -0.0474 | 0.0393 | ±0.0786 | -1.206 | 0.2277 |  |
| Kidney disease | -0.0741 | 0.0584 | ±0.1168 | -1.269 | 0.2043 |  |
| Circulatory disease | +0.1137 | 0.0596 | ±0.1191 | +1.909 | 0.0563 | . |
| Avg. daily SD (mg/dL) | +0.0026 | 0.0020 | ±0.0040 | +1.328 | 0.1840 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **2100**, R² = **0.1576**, Adj R² = **0.1519**, F-statistic = **27.86** (p = **6.45e-68**), Residual SE = **0.887** on **2085** df, AIC = **5468.6**, BIC = **5553.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4324** | 0.1727 | ±0.3455 | **+14.081** | **4.94e-45** | *** |
| **Education: graduate level (vs college)** | **-0.1054** | 0.0398 | ±0.0795 | **-2.650** | **0.0080** | ** |
| **Education: high school or below (vs college)** | **+0.4847** | 0.0819 | ±0.1637 | **+5.921** | **3.19e-09** | *** |
| Site: UCSD (vs UAB) | +0.0416 | 0.0491 | ±0.0981 | +0.848 | 0.3966 |  |
| **Site: UW (vs UAB)** | **-0.3494** | 0.0503 | ±0.1006 | **-6.942** | **3.86e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1646** | 0.0531 | ±0.1062 | **-3.099** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0084 | 0.0564 | ±0.1128 | +0.148 | 0.8821 |  |
| Season: winter (vs autumn) | -0.0289 | 0.0564 | ±0.1128 | -0.513 | 0.6081 |  |
| **Age (years)** | **-0.0161** | 0.0018 | ±0.0037 | **-8.810** | **1.25e-18** | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0031 | ±0.0062 | **+4.686** | **2.79e-06** | *** |
| **Hypertension** | **+0.1094** | 0.0418 | ±0.0836 | **+2.615** | **0.0089** | ** |
| High cholesterol | -0.0457 | 0.0393 | ±0.0786 | -1.164 | 0.2444 |  |
| Kidney disease | -0.0761 | 0.0586 | ±0.1171 | -1.300 | 0.1936 |  |
| Circulatory disease | +0.1134 | 0.0595 | ±0.1189 | +1.906 | 0.0566 | . |
| CV (%) | +0.0064 | 0.0039 | ±0.0078 | +1.642 | 0.1005 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2100**, R² = **0.1576**, Adj R² = **0.1520**, F-statistic = **27.86** (p = **6.40e-68**), Residual SE = **0.887** on **2085** df, AIC = **5468.5**, BIC = **5553.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.6947** | 0.1916 | ±0.3831 | **+14.066** | **6.12e-45** | *** |
| **Education: graduate level (vs college)** | **-0.1054** | 0.0398 | ±0.0795 | **-2.651** | **0.0080** | ** |
| **Education: high school or below (vs college)** | **+0.4844** | 0.0818 | ±0.1636 | **+5.923** | **3.17e-09** | *** |
| Site: UCSD (vs UAB) | +0.0408 | 0.0491 | ±0.0982 | +0.830 | 0.4065 |  |
| **Site: UW (vs UAB)** | **-0.3511** | 0.0504 | ±0.1007 | **-6.970** | **3.16e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1655** | 0.0531 | ±0.1061 | **-3.120** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0076 | 0.0564 | ±0.1128 | +0.134 | 0.8934 |  |
| Season: winter (vs autumn) | -0.0301 | 0.0564 | ±0.1128 | -0.534 | 0.5935 |  |
| **Age (years)** | **-0.0161** | 0.0018 | ±0.0037 | **-8.806** | **1.29e-18** | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0031 | ±0.0062 | **+4.681** | **2.85e-06** | *** |
| **Hypertension** | **+0.1092** | 0.0418 | ±0.0836 | **+2.612** | **0.0090** | ** |
| High cholesterol | -0.0462 | 0.0393 | ±0.0786 | -1.176 | 0.2394 |  |
| Kidney disease | -0.0721 | 0.0586 | ±0.1173 | -1.230 | 0.2186 |  |
| Circulatory disease | +0.1133 | 0.0594 | ±0.1189 | +1.906 | 0.0567 | . |
| Mean / SD ratio | -0.0249 | 0.0143 | ±0.0285 | -1.747 | 0.0807 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.1575**, Adj R² = **0.1519**, F-statistic = **27.85** (p = **7.11e-68**), Residual SE = **0.887** on **2085** df, AIC = **5468.8**, BIC = **5553.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.6863** | 0.1894 | ±0.3788 | **+14.181** | **1.20e-45** | *** |
| **Education: graduate level (vs college)** | **-0.1061** | 0.0398 | ±0.0795 | **-2.667** | **0.0076** | ** |
| **Education: high school or below (vs college)** | **+0.4843** | 0.0819 | ±0.1638 | **+5.913** | **3.35e-09** | *** |
| Site: UCSD (vs UAB) | +0.0390 | 0.0490 | ±0.0981 | +0.795 | 0.4269 |  |
| **Site: UW (vs UAB)** | **-0.3521** | 0.0504 | ±0.1008 | **-6.988** | **2.79e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1650** | 0.0531 | ±0.1061 | **-3.110** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0090 | 0.0564 | ±0.1128 | +0.159 | 0.8738 |  |
| Season: winter (vs autumn) | -0.0292 | 0.0564 | ±0.1128 | -0.518 | 0.6043 |  |
| **Age (years)** | **-0.0162** | 0.0018 | ±0.0037 | **-8.816** | **1.18e-18** | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0031 | ±0.0062 | **+4.687** | **2.77e-06** | *** |
| **Hypertension** | **+0.1102** | 0.0419 | ±0.0837 | **+2.631** | **0.0085** | ** |
| High cholesterol | -0.0459 | 0.0393 | ±0.0786 | -1.167 | 0.2431 |  |
| Kidney disease | -0.0710 | 0.0587 | ±0.1174 | -1.210 | 0.2261 |  |
| Circulatory disease | +0.1150 | 0.0594 | ±0.1187 | +1.937 | 0.0527 | . |
| Avg. daily mean/SD | -0.0201 | 0.0119 | ±0.0238 | -1.685 | 0.0919 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2100**, R² = **0.1583**, Adj R² = **0.1527**, F-statistic = **28.01** (p = **2.76e-68**), Residual SE = **0.886** on **2085** df, AIC = **5466.8**, BIC = **5551.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.3412** | 0.1796 | ±0.3592 | **+13.036** | **7.68e-39** | *** |
| **Education: graduate level (vs college)** | **-0.1043** | 0.0397 | ±0.0795 | **-2.625** | **0.0087** | ** |
| **Education: high school or below (vs college)** | **+0.4820** | 0.0814 | ±0.1627 | **+5.923** | **3.16e-09** | *** |
| Site: UCSD (vs UAB) | +0.0432 | 0.0489 | ±0.0978 | +0.883 | 0.3771 |  |
| **Site: UW (vs UAB)** | **-0.3438** | 0.0506 | ±0.1011 | **-6.800** | **1.05e-11** | *** |
| **Season: spring (vs autumn)** | **-0.1647** | 0.0530 | ±0.1059 | **-3.110** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0125 | 0.0562 | ±0.1125 | +0.223 | 0.8237 |  |
| Season: winter (vs autumn) | -0.0268 | 0.0562 | ±0.1125 | -0.477 | 0.6332 |  |
| **Age (years)** | **-0.0157** | 0.0018 | ±0.0036 | **-8.701** | **3.28e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.617** | **3.89e-06** | *** |
| **Hypertension** | **+0.1132** | 0.0418 | ±0.0836 | **+2.709** | **0.0068** | ** |
| High cholesterol | -0.0443 | 0.0393 | ±0.0787 | -1.127 | 0.2597 |  |
| Kidney disease | -0.0706 | 0.0591 | ±0.1182 | -1.195 | 0.2319 |  |
| Circulatory disease | +0.1148 | 0.0592 | ±0.1185 | +1.937 | 0.0527 | . |
| **MAG (mg/dL/h)** | **+0.0047** | 0.0022 | ±0.0044 | **+2.148** | **0.0317** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **2100**, R² = **0.1571**, Adj R² = **0.1515**, F-statistic = **27.76** (p = **1.16e-67**), Residual SE = **0.887** on **2085** df, AIC = **5469.8**, BIC = **5554.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4736** | 0.1690 | ±0.3381 | **+14.633** | **1.74e-48** | *** |
| **Education: graduate level (vs college)** | **-0.1066** | 0.0398 | ±0.0796 | **-2.679** | **0.0074** | ** |
| **Education: high school or below (vs college)** | **+0.4824** | 0.0818 | ±0.1635 | **+5.900** | **3.64e-09** | *** |
| Site: UCSD (vs UAB) | +0.0403 | 0.0490 | ±0.0979 | +0.823 | 0.4103 |  |
| **Site: UW (vs UAB)** | **-0.3513** | 0.0503 | ±0.1006 | **-6.981** | **2.94e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1655** | 0.0531 | ±0.1062 | **-3.117** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0094 | 0.0564 | ±0.1129 | +0.167 | 0.8670 |  |
| Season: winter (vs autumn) | -0.0284 | 0.0564 | ±0.1129 | -0.503 | 0.6148 |  |
| **Age (years)** | **-0.0160** | 0.0018 | ±0.0036 | **-8.796** | **1.42e-18** | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0031 | ±0.0062 | **+4.684** | **2.82e-06** | *** |
| **Hypertension** | **+0.1109** | 0.0421 | ±0.0843 | **+2.632** | **0.0085** | ** |
| High cholesterol | -0.0470 | 0.0393 | ±0.0786 | -1.196 | 0.2317 |  |
| Kidney disease | -0.0723 | 0.0583 | ±0.1166 | -1.239 | 0.2153 |  |
| Circulatory disease | +0.1135 | 0.0596 | ±0.1192 | +1.905 | 0.0568 | . |
| Avg. daily range (mg/dL) | +0.0007 | 0.0005 | ±0.0011 | +1.256 | 0.2092 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **2100**, R² = **0.1603**, Adj R² = **0.1547**, F-statistic = **28.43** (p = **2.55e-69**), Residual SE = **0.885** on **2085** df, AIC = **5461.8**, BIC = **5546.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4832** | 0.1621 | ±0.3243 | **+15.315** | **6.11e-53** | *** |
| **Education: graduate level (vs college)** | **-0.1008** | 0.0398 | ±0.0796 | **-2.533** | **0.0113** | * |
| **Education: high school or below (vs college)** | **+0.4782** | 0.0808 | ±0.1616 | **+5.917** | **3.27e-09** | *** |
| Site: UCSD (vs UAB) | +0.0454 | 0.0487 | ±0.0974 | +0.933 | 0.3510 |  |
| **Site: UW (vs UAB)** | **-0.3458** | 0.0501 | ±0.1002 | **-6.905** | **5.03e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1680** | 0.0531 | ±0.1061 | **-3.167** | **0.0015** | ** |
| Season: summer (vs autumn) | +0.0043 | 0.0565 | ±0.1130 | +0.076 | 0.9395 |  |
| Season: winter (vs autumn) | -0.0322 | 0.0563 | ±0.1125 | -0.572 | 0.5674 |  |
| **Age (years)** | **-0.0159** | 0.0018 | ±0.0036 | **-8.758** | **1.98e-18** | *** |
| **BMI (kg/m2)** | **+0.0138** | 0.0031 | ±0.0063 | **+4.401** | **1.08e-05** | *** |
| **Hypertension** | **+0.1059** | 0.0419 | ±0.0838 | **+2.527** | **0.0115** | * |
| High cholesterol | -0.0503 | 0.0392 | ±0.0784 | -1.284 | 0.1990 |  |
| Kidney disease | -0.0797 | 0.0579 | ±0.1159 | -1.376 | 0.1690 |  |
| Circulatory disease | +0.1054 | 0.0595 | ±0.1191 | +1.770 | 0.0768 | . |
| **SD of daily means (mg/dL)** | **+0.0098** | 0.0036 | ±0.0072 | **+2.702** | **0.0069** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **2100**, R² = **0.1584**, Adj R² = **0.1528**, F-statistic = **28.04** (p = **2.41e-68**), Residual SE = **0.886** on **2085** df, AIC = **5466.5**, BIC = **5551.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.7585** | 0.2060 | ±0.4120 | **+13.391** | **6.80e-41** | *** |
| **Education: graduate level (vs college)** | **-0.1048** | 0.0398 | ±0.0796 | **-2.634** | **0.0084** | ** |
| **Education: high school or below (vs college)** | **+0.4755** | 0.0810 | ±0.1621 | **+5.868** | **4.41e-09** | *** |
| Site: UCSD (vs UAB) | +0.0446 | 0.0489 | ±0.0979 | +0.912 | 0.3619 |  |
| **Site: UW (vs UAB)** | **-0.3484** | 0.0503 | ±0.1007 | **-6.923** | **4.42e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1650** | 0.0530 | ±0.1061 | **-3.111** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0109 | 0.0563 | ±0.1127 | +0.194 | 0.8464 |  |
| Season: winter (vs autumn) | -0.0290 | 0.0563 | ±0.1126 | -0.515 | 0.6063 |  |
| **Age (years)** | **-0.0160** | 0.0018 | ±0.0036 | **-8.817** | **1.18e-18** | *** |
| **BMI (kg/m2)** | **+0.0142** | 0.0032 | ±0.0063 | **+4.490** | **7.12e-06** | *** |
| **Hypertension** | **+0.1092** | 0.0420 | ±0.0840 | **+2.600** | **0.0093** | ** |
| High cholesterol | -0.0488 | 0.0392 | ±0.0785 | -1.244 | 0.2135 |  |
| Kidney disease | -0.0753 | 0.0587 | ±0.1173 | -1.284 | 0.1993 |  |
| Circulatory disease | +0.1118 | 0.0596 | ±0.1191 | +1.877 | 0.0606 | . |
| Time in range 70-180, pooled (%) | -0.0022 | 0.0012 | ±0.0023 | -1.914 | 0.0556 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **2100**, R² = **0.1584**, Adj R² = **0.1528**, F-statistic = **28.03** (p = **2.45e-68**), Residual SE = **0.886** on **2085** df, AIC = **5466.5**, BIC = **5551.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.7584** | 0.2064 | ±0.4128 | **+13.365** | **9.73e-41** | *** |
| **Education: graduate level (vs college)** | **-0.1050** | 0.0398 | ±0.0796 | **-2.638** | **0.0083** | ** |
| **Education: high school or below (vs college)** | **+0.4754** | 0.0810 | ±0.1621 | **+5.868** | **4.42e-09** | *** |
| Site: UCSD (vs UAB) | +0.0447 | 0.0489 | ±0.0979 | +0.913 | 0.3610 |  |
| **Site: UW (vs UAB)** | **-0.3484** | 0.0503 | ±0.1007 | **-6.923** | **4.43e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1653** | 0.0530 | ±0.1061 | **-3.116** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0106 | 0.0563 | ±0.1126 | +0.189 | 0.8502 |  |
| Season: winter (vs autumn) | -0.0294 | 0.0563 | ±0.1126 | -0.522 | 0.6017 |  |
| **Age (years)** | **-0.0160** | 0.0018 | ±0.0036 | **-8.819** | **1.16e-18** | *** |
| **BMI (kg/m2)** | **+0.0142** | 0.0032 | ±0.0063 | **+4.485** | **7.28e-06** | *** |
| **Hypertension** | **+0.1094** | 0.0420 | ±0.0840 | **+2.605** | **0.0092** | ** |
| High cholesterol | -0.0489 | 0.0392 | ±0.0785 | -1.246 | 0.2127 |  |
| Kidney disease | -0.0755 | 0.0586 | ±0.1172 | -1.288 | 0.1976 |  |
| Circulatory disease | +0.1118 | 0.0596 | ±0.1191 | +1.877 | 0.0605 | . |
| Avg. daily time in range 70-180 (%) | -0.0022 | 0.0012 | ±0.0023 | -1.907 | 0.0565 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.1568**, Adj R² = **0.1512**, F-statistic = **27.70** (p = **1.66e-67**), Residual SE = **0.887** on **2085** df, AIC = **5470.5**, BIC = **5555.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5139** | 0.1625 | ±0.3249 | **+15.473** | **5.28e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1084** | 0.0397 | ±0.0793 | **-2.732** | **0.0063** | ** |
| **Education: high school or below (vs college)** | **+0.4947** | 0.0819 | ±0.1638 | **+6.042** | **1.52e-09** | *** |
| Site: UCSD (vs UAB) | +0.0401 | 0.0491 | ±0.0982 | +0.817 | 0.4140 |  |
| **Site: UW (vs UAB)** | **-0.3523** | 0.0503 | ±0.1006 | **-7.007** | **2.43e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1662** | 0.0531 | ±0.1061 | **-3.133** | **0.0017** | ** |
| Season: summer (vs autumn) | +0.0094 | 0.0564 | ±0.1127 | +0.167 | 0.8673 |  |
| Season: winter (vs autumn) | -0.0287 | 0.0563 | ±0.1127 | -0.509 | 0.6106 |  |
| **Age (years)** | **-0.0157** | 0.0018 | ±0.0036 | **-8.643** | **5.47e-18** | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0031 | ±0.0062 | **+4.663** | **3.11e-06** | *** |
| **Hypertension** | **+0.1155** | 0.0418 | ±0.0836 | **+2.762** | **0.0058** | ** |
| High cholesterol | -0.0426 | 0.0395 | ±0.0789 | -1.079 | 0.2804 |  |
| Kidney disease | -0.0577 | 0.0588 | ±0.1175 | -0.981 | 0.3265 |  |
| Circulatory disease | +0.1129 | 0.0593 | ±0.1186 | +1.905 | 0.0568 | . |
| Any reading < 54 during wear (0/1) | +0.0410 | 0.0456 | ±0.0912 | +0.899 | 0.3685 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.1572**, Adj R² = **0.1515**, F-statistic = **27.78** (p = **1.05e-67**), Residual SE = **0.887** on **2085** df, AIC = **5469.6**, BIC = **5554.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5174** | 0.1639 | ±0.3279 | **+15.355** | **3.28e-53** | *** |
| **Education: graduate level (vs college)** | **-0.1083** | 0.0397 | ±0.0793 | **-2.730** | **0.0063** | ** |
| **Education: high school or below (vs college)** | **+0.4952** | 0.0816 | ±0.1633 | **+6.066** | **1.31e-09** | *** |
| Site: UCSD (vs UAB) | +0.0431 | 0.0492 | ±0.0984 | +0.877 | 0.3807 |  |
| **Site: UW (vs UAB)** | **-0.3486** | 0.0504 | ±0.1009 | **-6.912** | **4.80e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1651** | 0.0530 | ±0.1060 | **-3.115** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0077 | 0.0564 | ±0.1129 | +0.136 | 0.8915 |  |
| Season: winter (vs autumn) | -0.0300 | 0.0564 | ±0.1127 | -0.533 | 0.5939 |  |
| **Age (years)** | **-0.0157** | 0.0018 | ±0.0036 | **-8.669** | **4.35e-18** | *** |
| **BMI (kg/m2)** | **+0.0147** | 0.0031 | ±0.0062 | **+4.715** | **2.42e-06** | *** |
| **Hypertension** | **+0.1170** | 0.0419 | ±0.0838 | **+2.792** | **0.0052** | ** |
| High cholesterol | -0.0419 | 0.0396 | ±0.0792 | -1.059 | 0.2897 |  |
| Kidney disease | -0.0585 | 0.0586 | ±0.1173 | -0.998 | 0.3181 |  |
| Circulatory disease | +0.1142 | 0.0591 | ±0.1183 | +1.930 | 0.0535 | . |
| Time < 54 (%) | +0.0516 | 0.0538 | ±0.1076 | +0.960 | 0.3373 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.1582**, Adj R² = **0.1526**, F-statistic = **27.99** (p = **3.04e-68**), Residual SE = **0.886** on **2085** df, AIC = **5467.0**, BIC = **5551.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5177** | 0.1631 | ±0.3262 | **+15.435** | **9.51e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1068** | 0.0396 | ±0.0793 | **-2.694** | **0.0070** | ** |
| **Education: high school or below (vs college)** | **+0.4971** | 0.0816 | ±0.1633 | **+6.090** | **1.13e-09** | *** |
| Site: UCSD (vs UAB) | +0.0456 | 0.0490 | ±0.0980 | +0.930 | 0.3523 |  |
| **Site: UW (vs UAB)** | **-0.3447** | 0.0505 | ±0.1009 | **-6.832** | **8.37e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1641** | 0.0530 | ±0.1060 | **-3.094** | **0.0020** | ** |
| Season: summer (vs autumn) | +0.0074 | 0.0564 | ±0.1128 | +0.131 | 0.8957 |  |
| Season: winter (vs autumn) | -0.0310 | 0.0563 | ±0.1126 | -0.550 | 0.5820 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.718** | **2.84e-18** | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0031 | ±0.0062 | **+4.719** | **2.37e-06** | *** |
| **Hypertension** | **+0.1180** | 0.0420 | ±0.0839 | **+2.811** | **0.0049** | ** |
| High cholesterol | -0.0408 | 0.0395 | ±0.0789 | -1.033 | 0.3017 |  |
| Kidney disease | -0.0593 | 0.0585 | ±0.1170 | -1.013 | 0.3108 |  |
| Circulatory disease | +0.1132 | 0.0590 | ±0.1181 | +1.918 | 0.0552 | . |
| Avg. daily time < 54 (%) | +0.0953 | 0.0712 | ±0.1424 | +1.339 | 0.1806 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.1591**, Adj R² = **0.1535**, F-statistic = **28.18** (p = **1.06e-68**), Residual SE = **0.886** on **2085** df, AIC = **5464.8**, BIC = **5549.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5043** | 0.1629 | ±0.3258 | **+15.373** | **2.50e-53** | *** |
| **Education: graduate level (vs college)** | **-0.1045** | 0.0396 | ±0.0792 | **-2.638** | **0.0083** | ** |
| **Education: high school or below (vs college)** | **+0.4974** | 0.0818 | ±0.1636 | **+6.081** | **1.20e-09** | *** |
| Site: UCSD (vs UAB) | +0.0456 | 0.0490 | ±0.0980 | +0.929 | 0.3527 |  |
| **Site: UW (vs UAB)** | **-0.3448** | 0.0506 | ±0.1011 | **-6.819** | **9.17e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1643** | 0.0529 | ±0.1059 | **-3.105** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0092 | 0.0562 | ±0.1124 | +0.163 | 0.8702 |  |
| Season: winter (vs autumn) | -0.0313 | 0.0562 | ±0.1125 | -0.557 | 0.5778 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.691** | **3.59e-18** | *** |
| **BMI (kg/m2)** | **+0.0145** | 0.0031 | ±0.0062 | **+4.683** | **2.83e-06** | *** |
| **Hypertension** | **+0.1189** | 0.0420 | ±0.0839 | **+2.833** | **0.0046** | ** |
| High cholesterol | -0.0409 | 0.0393 | ±0.0787 | -1.040 | 0.2982 |  |
| Kidney disease | -0.0589 | 0.0585 | ±0.1171 | -1.006 | 0.3145 |  |
| Circulatory disease | +0.1141 | 0.0591 | ±0.1182 | +1.931 | 0.0535 | . |
| Time 54-69, pooled (%) | +0.0348 | 0.0191 | ±0.0382 | +1.826 | 0.0678 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2100**, R² = **0.1594**, Adj R² = **0.1538**, F-statistic = **28.25** (p = **7.18e-69**), Residual SE = **0.886** on **2085** df, AIC = **5464.0**, BIC = **5548.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5103** | 0.1627 | ±0.3254 | **+15.427** | **1.08e-53** | *** |
| **Education: graduate level (vs college)** | **-0.1036** | 0.0396 | ±0.0792 | **-2.617** | **0.0089** | ** |
| **Education: high school or below (vs college)** | **+0.4973** | 0.0818 | ±0.1636 | **+6.079** | **1.21e-09** | *** |
| Site: UCSD (vs UAB) | +0.0444 | 0.0490 | ±0.0979 | +0.907 | 0.3646 |  |
| **Site: UW (vs UAB)** | **-0.3442** | 0.0506 | ±0.1012 | **-6.801** | **1.04e-11** | *** |
| **Season: spring (vs autumn)** | **-0.1643** | 0.0529 | ±0.1058 | **-3.106** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0094 | 0.0562 | ±0.1123 | +0.168 | 0.8665 |  |
| Season: winter (vs autumn) | -0.0322 | 0.0562 | ±0.1125 | -0.573 | 0.5667 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.731** | **2.52e-18** | *** |
| **BMI (kg/m2)** | **+0.0145** | 0.0031 | ±0.0062 | **+4.680** | **2.87e-06** | *** |
| **Hypertension** | **+0.1191** | 0.0420 | ±0.0839 | **+2.837** | **0.0046** | ** |
| High cholesterol | -0.0412 | 0.0393 | ±0.0786 | -1.047 | 0.2950 |  |
| Kidney disease | -0.0587 | 0.0584 | ±0.1169 | -1.004 | 0.3155 |  |
| Circulatory disease | +0.1145 | 0.0591 | ±0.1182 | +1.938 | 0.0527 | . |
| Avg. daily time 54-69 (%) | +0.0364 | 0.0195 | ±0.0389 | +1.871 | 0.0613 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **2100**, R² = **0.1589**, Adj R² = **0.1533**, F-statistic = **28.14** (p = **1.34e-68**), Residual SE = **0.886** on **2085** df, AIC = **5465.3**, BIC = **5550.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5019** | 0.1632 | ±0.3263 | **+15.333** | **4.62e-53** | *** |
| **Education: graduate level (vs college)** | **-0.1051** | 0.0396 | ±0.0792 | **-2.653** | **0.0080** | ** |
| **Education: high school or below (vs college)** | **+0.4983** | 0.0818 | ±0.1636 | **+6.090** | **1.13e-09** | *** |
| Site: UCSD (vs UAB) | +0.0474 | 0.0491 | ±0.0982 | +0.965 | 0.3347 |  |
| **Site: UW (vs UAB)** | **-0.3437** | 0.0506 | ±0.1012 | **-6.793** | **1.10e-11** | *** |
| **Season: spring (vs autumn)** | **-0.1641** | 0.0529 | ±0.1059 | **-3.101** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0087 | 0.0563 | ±0.1125 | +0.154 | 0.8776 |  |
| Season: winter (vs autumn) | -0.0310 | 0.0562 | ±0.1125 | -0.551 | 0.5814 |  |
| **Age (years)** | **-0.0157** | 0.0018 | ±0.0036 | **-8.677** | **4.07e-18** | *** |
| **BMI (kg/m2)** | **+0.0146** | 0.0031 | ±0.0062 | **+4.695** | **2.67e-06** | *** |
| **Hypertension** | **+0.1188** | 0.0420 | ±0.0839 | **+2.831** | **0.0046** | ** |
| High cholesterol | -0.0402 | 0.0394 | ±0.0788 | -1.020 | 0.3076 |  |
| Kidney disease | -0.0588 | 0.0585 | ±0.1171 | -1.004 | 0.3154 |  |
| Circulatory disease | +0.1136 | 0.0591 | ±0.1181 | +1.923 | 0.0545 | . |
| Time < 70 (%) | +0.0271 | 0.0152 | ±0.0304 | +1.779 | 0.0753 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **2100**, R² = **0.1596**, Adj R² = **0.1539**, F-statistic = **28.28** (p = **6.10e-69**), Residual SE = **0.885** on **2085** df, AIC = **5463.7**, BIC = **5548.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5083** | 0.1627 | ±0.3255 | **+15.412** | **1.35e-53** | *** |
| **Education: graduate level (vs college)** | **-0.1037** | 0.0396 | ±0.0792 | **-2.619** | **0.0088** | ** |
| **Education: high school or below (vs college)** | **+0.4984** | 0.0818 | ±0.1636 | **+6.093** | **1.11e-09** | *** |
| Site: UCSD (vs UAB) | +0.0464 | 0.0490 | ±0.0979 | +0.947 | 0.3436 |  |
| **Site: UW (vs UAB)** | **-0.3424** | 0.0506 | ±0.1012 | **-6.765** | **1.33e-11** | *** |
| **Season: spring (vs autumn)** | **-0.1639** | 0.0529 | ±0.1058 | **-3.097** | **0.0020** | ** |
| Season: summer (vs autumn) | +0.0090 | 0.0562 | ±0.1124 | +0.160 | 0.8731 |  |
| Season: winter (vs autumn) | -0.0322 | 0.0562 | ±0.1124 | -0.573 | 0.5669 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.730** | **2.55e-18** | *** |
| **BMI (kg/m2)** | **+0.0145** | 0.0031 | ±0.0062 | **+4.691** | **2.72e-06** | *** |
| **Hypertension** | **+0.1193** | 0.0420 | ±0.0840 | **+2.841** | **0.0045** | ** |
| High cholesterol | -0.0404 | 0.0393 | ±0.0787 | -1.026 | 0.3049 |  |
| Kidney disease | -0.0589 | 0.0584 | ±0.1168 | -1.008 | 0.3135 |  |
| Circulatory disease | +0.1138 | 0.0590 | ±0.1181 | +1.928 | 0.0539 | . |
| Avg. daily time < 70 (%) | +0.0310 | 0.0163 | ±0.0326 | +1.905 | 0.0568 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.1583**, Adj R² = **0.1527**, F-statistic = **28.01** (p = **2.76e-68**), Residual SE = **0.886** on **2085** df, AIC = **5466.8**, BIC = **5551.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9112** | 0.2838 | ±0.5676 | **+10.258** | **1.09e-24** | *** |
| **Education: graduate level (vs college)** | **-0.1043** | 0.0399 | ±0.0798 | **-2.612** | **0.0090** | ** |
| **Education: high school or below (vs college)** | **+0.4773** | 0.0806 | ±0.1612 | **+5.923** | **3.16e-09** | *** |
| Site: UCSD (vs UAB) | +0.0426 | 0.0489 | ±0.0978 | +0.872 | 0.3833 |  |
| **Site: UW (vs UAB)** | **-0.3475** | 0.0503 | ±0.1005 | **-6.913** | **4.76e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1649** | 0.0531 | ±0.1062 | **-3.106** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0142 | 0.0564 | ±0.1127 | +0.252 | 0.8007 |  |
| Season: winter (vs autumn) | -0.0291 | 0.0563 | ±0.1127 | -0.516 | 0.6059 |  |
| **Age (years)** | **-0.0157** | 0.0018 | ±0.0036 | **-8.690** | **3.61e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.585** | **4.53e-06** | *** |
| **Hypertension** | **+0.1112** | 0.0418 | ±0.0837 | **+2.656** | **0.0079** | ** |
| High cholesterol | -0.0460 | 0.0393 | ±0.0786 | -1.172 | 0.2411 |  |
| Kidney disease | -0.0689 | 0.0588 | ±0.1177 | -1.171 | 0.2414 |  |
| Circulatory disease | +0.1120 | 0.0596 | ±0.1191 | +1.880 | 0.0601 | . |
| Time 54-250, pooled (%) | -0.0039 | 0.0023 | ±0.0047 | -1.645 | 0.1000 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.1583**, Adj R² = **0.1527**, F-statistic = **28.02** (p = **2.67e-68**), Residual SE = **0.886** on **2085** df, AIC = **5466.7**, BIC = **5551.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9211** | 0.2867 | ±0.5734 | **+10.189** | **2.23e-24** | *** |
| **Education: graduate level (vs college)** | **-0.1043** | 0.0399 | ±0.0798 | **-2.612** | **0.0090** | ** |
| **Education: high school or below (vs college)** | **+0.4772** | 0.0806 | ±0.1612 | **+5.921** | **3.19e-09** | *** |
| Site: UCSD (vs UAB) | +0.0426 | 0.0489 | ±0.0978 | +0.872 | 0.3833 |  |
| **Site: UW (vs UAB)** | **-0.3476** | 0.0503 | ±0.1005 | **-6.917** | **4.61e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1651** | 0.0531 | ±0.1062 | **-3.111** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0139 | 0.0563 | ±0.1127 | +0.247 | 0.8049 |  |
| Season: winter (vs autumn) | -0.0293 | 0.0563 | ±0.1127 | -0.520 | 0.6028 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.703** | **3.22e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.581** | **4.62e-06** | *** |
| **Hypertension** | **+0.1113** | 0.0418 | ±0.0837 | **+2.660** | **0.0078** | ** |
| High cholesterol | -0.0461 | 0.0393 | ±0.0786 | -1.173 | 0.2408 |  |
| Kidney disease | -0.0695 | 0.0588 | ±0.1176 | -1.181 | 0.2375 |  |
| Circulatory disease | +0.1117 | 0.0596 | ±0.1192 | +1.874 | 0.0609 | . |
| Avg. daily time 54-250 (%) | -0.0039 | 0.0024 | ±0.0047 | -1.661 | 0.0967 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.1571**, Adj R² = **0.1515**, F-statistic = **27.76** (p = **1.14e-67**), Residual SE = **0.887** on **2085** df, AIC = **5469.7**, BIC = **5554.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5441** | 0.1639 | ±0.3278 | **+15.522** | **2.45e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1081** | 0.0397 | ±0.0794 | **-2.721** | **0.0065** | ** |
| **Education: high school or below (vs college)** | **+0.4834** | 0.0819 | ±0.1638 | **+5.901** | **3.60e-09** | *** |
| Site: UCSD (vs UAB) | +0.0394 | 0.0490 | ±0.0981 | +0.803 | 0.4217 |  |
| **Site: UW (vs UAB)** | **-0.3535** | 0.0504 | ±0.1009 | **-7.009** | **2.40e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1660** | 0.0530 | ±0.1061 | **-3.130** | **0.0017** | ** |
| Season: summer (vs autumn) | +0.0075 | 0.0565 | ±0.1129 | +0.134 | 0.8936 |  |
| Season: winter (vs autumn) | -0.0296 | 0.0564 | ±0.1128 | -0.525 | 0.5997 |  |
| **Age (years)** | **-0.0160** | 0.0018 | ±0.0037 | **-8.773** | **1.74e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.564** | **5.02e-06** | *** |
| **Hypertension** | **+0.1121** | 0.0422 | ±0.0843 | **+2.658** | **0.0079** | ** |
| High cholesterol | -0.0482 | 0.0393 | ±0.0787 | -1.225 | 0.2208 |  |
| Kidney disease | -0.0685 | 0.0585 | ±0.1171 | -1.171 | 0.2418 |  |
| Circulatory disease | +0.1143 | 0.0594 | ±0.1188 | +1.924 | 0.0544 | . |
| Time 181-250, pooled (%) | +0.0020 | 0.0017 | ±0.0033 | +1.221 | 0.2221 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2100**, R² = **0.1571**, Adj R² = **0.1514**, F-statistic = **27.76** (p = **1.18e-67**), Residual SE = **0.887** on **2085** df, AIC = **5469.8**, BIC = **5554.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5438** | 0.1639 | ±0.3278 | **+15.518** | **2.61e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1082** | 0.0397 | ±0.0794 | **-2.724** | **0.0064** | ** |
| **Education: high school or below (vs college)** | **+0.4834** | 0.0819 | ±0.1638 | **+5.903** | **3.56e-09** | *** |
| Site: UCSD (vs UAB) | +0.0396 | 0.0490 | ±0.0981 | +0.807 | 0.4197 |  |
| **Site: UW (vs UAB)** | **-0.3534** | 0.0504 | ±0.1009 | **-7.006** | **2.45e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1662** | 0.0530 | ±0.1061 | **-3.132** | **0.0017** | ** |
| Season: summer (vs autumn) | +0.0075 | 0.0565 | ±0.1129 | +0.134 | 0.8937 |  |
| Season: winter (vs autumn) | -0.0297 | 0.0564 | ±0.1128 | -0.528 | 0.5978 |  |
| **Age (years)** | **-0.0160** | 0.0018 | ±0.0037 | **-8.769** | **1.80e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.562** | **5.08e-06** | *** |
| **Hypertension** | **+0.1122** | 0.0422 | ±0.0843 | **+2.661** | **0.0078** | ** |
| High cholesterol | -0.0481 | 0.0393 | ±0.0787 | -1.224 | 0.2209 |  |
| Kidney disease | -0.0684 | 0.0585 | ±0.1170 | -1.168 | 0.2426 |  |
| Circulatory disease | +0.1144 | 0.0594 | ±0.1188 | +1.926 | 0.0541 | . |
| Avg. daily time 181-250 (%) | +0.0020 | 0.0016 | ±0.0033 | +1.200 | 0.2302 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **2100**, R² = **0.1580**, Adj R² = **0.1524**, F-statistic = **27.95** (p = **3.94e-68**), Residual SE = **0.886** on **2085** df, AIC = **5467.5**, BIC = **5552.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5393** | 0.1634 | ±0.3269 | **+15.536** | **1.97e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1056** | 0.0398 | ±0.0796 | **-2.654** | **0.0080** | ** |
| **Education: high school or below (vs college)** | **+0.4768** | 0.0811 | ±0.1622 | **+5.878** | **4.14e-09** | *** |
| Site: UCSD (vs UAB) | +0.0427 | 0.0490 | ±0.0979 | +0.871 | 0.3836 |  |
| **Site: UW (vs UAB)** | **-0.3500** | 0.0503 | ±0.1007 | **-6.952** | **3.60e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1653** | 0.0531 | ±0.1061 | **-3.116** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0106 | 0.0564 | ±0.1127 | +0.188 | 0.8511 |  |
| Season: winter (vs autumn) | -0.0291 | 0.0563 | ±0.1127 | -0.516 | 0.6057 |  |
| **Age (years)** | **-0.0160** | 0.0018 | ±0.0036 | **-8.803** | **1.33e-18** | *** |
| **BMI (kg/m2)** | **+0.0142** | 0.0032 | ±0.0063 | **+4.515** | **6.34e-06** | *** |
| **Hypertension** | **+0.1098** | 0.0421 | ±0.0841 | **+2.610** | **0.0090** | ** |
| High cholesterol | -0.0487 | 0.0392 | ±0.0785 | -1.241 | 0.2147 |  |
| Kidney disease | -0.0733 | 0.0587 | ±0.1174 | -1.249 | 0.2115 |  |
| Circulatory disease | +0.1124 | 0.0596 | ±0.1191 | +1.887 | 0.0591 | . |
| Time > 180 (%) | +0.0020 | 0.0012 | ±0.0023 | +1.697 | 0.0898 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.1580**, Adj R² = **0.1523**, F-statistic = **27.94** (p = **4.15e-68**), Residual SE = **0.886** on **2085** df, AIC = **5467.6**, BIC = **5552.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5400** | 0.1635 | ±0.3270 | **+15.535** | **2.00e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1058** | 0.0398 | ±0.0796 | **-2.660** | **0.0078** | ** |
| **Education: high school or below (vs college)** | **+0.4769** | 0.0811 | ±0.1622 | **+5.880** | **4.11e-09** | *** |
| Site: UCSD (vs UAB) | +0.0428 | 0.0490 | ±0.0979 | +0.875 | 0.3816 |  |
| **Site: UW (vs UAB)** | **-0.3500** | 0.0503 | ±0.1007 | **-6.953** | **3.59e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1656** | 0.0531 | ±0.1061 | **-3.121** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0103 | 0.0564 | ±0.1127 | +0.183 | 0.8549 |  |
| Season: winter (vs autumn) | -0.0294 | 0.0563 | ±0.1127 | -0.521 | 0.6024 |  |
| **Age (years)** | **-0.0160** | 0.0018 | ±0.0036 | **-8.802** | **1.35e-18** | *** |
| **BMI (kg/m2)** | **+0.0142** | 0.0032 | ±0.0063 | **+4.512** | **6.43e-06** | *** |
| **Hypertension** | **+0.1100** | 0.0421 | ±0.0841 | **+2.615** | **0.0089** | ** |
| High cholesterol | -0.0487 | 0.0392 | ±0.0785 | -1.241 | 0.2148 |  |
| Kidney disease | -0.0734 | 0.0587 | ±0.1173 | -1.251 | 0.2108 |  |
| Circulatory disease | +0.1124 | 0.0596 | ±0.1191 | +1.887 | 0.0591 | . |
| Avg. daily time > 180 (%) | +0.0019 | 0.0011 | ±0.0023 | +1.672 | 0.0944 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.1586**, Adj R² = **0.1530**, F-statistic = **28.08** (p = **1.87e-68**), Residual SE = **0.886** on **2085** df, AIC = **5466.0**, BIC = **5550.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5418** | 0.1636 | ±0.3271 | **+15.539** | **1.89e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1034** | 0.0398 | ±0.0797 | **-2.596** | **0.0094** | ** |
| **Education: high school or below (vs college)** | **+0.4754** | 0.0809 | ±0.1618 | **+5.875** | **4.22e-09** | *** |
| Site: UCSD (vs UAB) | +0.0441 | 0.0489 | ±0.0978 | +0.901 | 0.3674 |  |
| **Site: UW (vs UAB)** | **-0.3498** | 0.0503 | ±0.1006 | **-6.955** | **3.52e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1671** | 0.0531 | ±0.1061 | **-3.149** | **0.0016** | ** |
| Season: summer (vs autumn) | +0.0113 | 0.0563 | ±0.1126 | +0.200 | 0.8414 |  |
| Season: winter (vs autumn) | -0.0310 | 0.0563 | ±0.1126 | -0.550 | 0.5826 |  |
| **Age (years)** | **-0.0159** | 0.0018 | ±0.0036 | **-8.753** | **2.07e-18** | *** |
| **BMI (kg/m2)** | **+0.0139** | 0.0032 | ±0.0064 | **+4.378** | **1.20e-05** | *** |
| **Hypertension** | **+0.1111** | 0.0419 | ±0.0838 | **+2.650** | **0.0080** | ** |
| High cholesterol | -0.0487 | 0.0392 | ±0.0784 | -1.241 | 0.2147 |  |
| Kidney disease | -0.0719 | 0.0584 | ±0.1169 | -1.230 | 0.2185 |  |
| Circulatory disease | +0.1124 | 0.0595 | ±0.1190 | +1.890 | 0.0588 | . |
| **Nocturnal time > 180 (%)** | **+0.0023** | 0.0012 | ±0.0023 | **+1.979** | **0.0478** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.1565**, Adj R² = **0.1508**, F-statistic = **27.63** (p = **2.45e-67**), Residual SE = **0.887** on **2085** df, AIC = **5471.3**, BIC = **5556.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5336** | 0.1633 | ±0.3266 | **+15.513** | **2.84e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1085** | 0.0398 | ±0.0796 | **-2.725** | **0.0064** | ** |
| **Education: high school or below (vs college)** | **+0.4896** | 0.0818 | ±0.1636 | **+5.986** | **2.15e-09** | *** |
| Site: UCSD (vs UAB) | +0.0360 | 0.0490 | ±0.0980 | +0.735 | 0.4625 |  |
| **Site: UW (vs UAB)** | **-0.3547** | 0.0504 | ±0.1008 | **-7.037** | **1.97e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1656** | 0.0531 | ±0.1062 | **-3.119** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0084 | 0.0565 | ±0.1129 | +0.149 | 0.8812 |  |
| Season: winter (vs autumn) | -0.0293 | 0.0565 | ±0.1130 | -0.519 | 0.6035 |  |
| **Age (years)** | **-0.0159** | 0.0018 | ±0.0036 | **-8.713** | **2.95e-18** | *** |
| **BMI (kg/m2)** | **+0.0147** | 0.0031 | ±0.0062 | **+4.709** | **2.49e-06** | *** |
| **Hypertension** | **+0.1146** | 0.0423 | ±0.0846 | **+2.711** | **0.0067** | ** |
| High cholesterol | -0.0458 | 0.0393 | ±0.0787 | -1.164 | 0.2444 |  |
| Kidney disease | -0.0607 | 0.0587 | ±0.1174 | -1.034 | 0.3011 |  |
| Circulatory disease | +0.1159 | 0.0593 | ±0.1186 | +1.954 | 0.0507 | . |
| Any reading > 250 during wear (0/1) | +0.0134 | 0.0419 | ±0.0838 | +0.321 | 0.7484 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.1582**, Adj R² = **0.1525**, F-statistic = **27.99** (p = **3.17e-68**), Residual SE = **0.886** on **2085** df, AIC = **5467.1**, BIC = **5551.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5265** | 0.1635 | ±0.3269 | **+15.456** | **6.85e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1045** | 0.0399 | ±0.0799 | **-2.617** | **0.0089** | ** |
| **Education: high school or below (vs college)** | **+0.4774** | 0.0806 | ±0.1611 | **+5.926** | **3.11e-09** | *** |
| Site: UCSD (vs UAB) | +0.0419 | 0.0489 | ±0.0978 | +0.855 | 0.3923 |  |
| **Site: UW (vs UAB)** | **-0.3482** | 0.0503 | ±0.1005 | **-6.925** | **4.35e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1650** | 0.0531 | ±0.1062 | **-3.109** | **0.0019** | ** |
| Season: summer (vs autumn) | +0.0141 | 0.0564 | ±0.1127 | +0.250 | 0.8027 |  |
| Season: winter (vs autumn) | -0.0291 | 0.0564 | ±0.1127 | -0.517 | 0.6055 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.694** | **3.50e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.588** | **4.48e-06** | *** |
| **Hypertension** | **+0.1112** | 0.0419 | ±0.0837 | **+2.657** | **0.0079** | ** |
| High cholesterol | -0.0462 | 0.0393 | ±0.0786 | -1.177 | 0.2391 |  |
| Kidney disease | -0.0686 | 0.0588 | ±0.1177 | -1.166 | 0.2437 |  |
| Circulatory disease | +0.1122 | 0.0596 | ±0.1192 | +1.884 | 0.0596 | . |
| Time > 250 (%) | +0.0037 | 0.0023 | ±0.0047 | +1.592 | 0.1114 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,100)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.1582**, Adj R² = **0.1525**, F-statistic = **27.99** (p = **3.18e-68**), Residual SE = **0.886** on **2085** df, AIC = **5467.1**, BIC = **5551.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5280** | 0.1635 | ±0.3270 | **+15.464** | **6.06e-54** | *** |
| **Education: graduate level (vs college)** | **-0.1046** | 0.0399 | ±0.0798 | **-2.619** | **0.0088** | ** |
| **Education: high school or below (vs college)** | **+0.4775** | 0.0806 | ±0.1611 | **+5.926** | **3.11e-09** | *** |
| Site: UCSD (vs UAB) | +0.0419 | 0.0489 | ±0.0978 | +0.857 | 0.3912 |  |
| **Site: UW (vs UAB)** | **-0.3483** | 0.0503 | ±0.1005 | **-6.930** | **4.22e-12** | *** |
| **Season: spring (vs autumn)** | **-0.1653** | 0.0531 | ±0.1062 | **-3.114** | **0.0018** | ** |
| Season: summer (vs autumn) | +0.0137 | 0.0564 | ±0.1127 | +0.244 | 0.8074 |  |
| Season: winter (vs autumn) | -0.0293 | 0.0564 | ±0.1127 | -0.520 | 0.6029 |  |
| **Age (years)** | **-0.0158** | 0.0018 | ±0.0036 | **-8.703** | **3.22e-18** | *** |
| **BMI (kg/m2)** | **+0.0144** | 0.0031 | ±0.0063 | **+4.585** | **4.54e-06** | *** |
| **Hypertension** | **+0.1114** | 0.0419 | ±0.0837 | **+2.662** | **0.0078** | ** |
| High cholesterol | -0.0462 | 0.0393 | ±0.0786 | -1.176 | 0.2395 |  |
| Kidney disease | -0.0690 | 0.0588 | ±0.1176 | -1.173 | 0.2407 |  |
| Circulatory disease | +0.1120 | 0.0596 | ±0.1192 | +1.879 | 0.0603 | . |
| Avg. daily time > 250 (%) | +0.0038 | 0.0024 | ±0.0047 | +1.594 | 0.1109 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 2,100; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **2100**, R² = **0.3025**, Adj R² = **0.2982**, F-statistic = **69.61** (p = **1.22e-152**), Residual SE = **1.986** on **2086** df, AIC = **8854.6**, BIC = **8933.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9397** | 0.3610 | ±0.7219 | **+66.323** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1210 | 0.0921 | ±0.1842 | -1.314 | 0.1888 |  |
| Education: high school or below (vs college) | +0.1977 | 0.1564 | ±0.3127 | +1.264 | 0.2062 |  |
| Site: UCSD (vs UAB) | -0.1209 | 0.1103 | ±0.2207 | -1.096 | 0.2731 |  |
| **Site: UW (vs UAB)** | **-1.1222** | 0.1075 | ±0.2149 | **-10.444** | **1.56e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3635** | 0.1199 | ±0.2397 | **-3.033** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8926** | 0.1384 | ±0.2768 | **+13.677** | **1.38e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3136** | 0.1231 | ±0.2463 | **-10.668** | **1.44e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.501** | **0.0124** | * |
| BMI (kg/m2) | +0.0105 | 0.0066 | ±0.0131 | +1.595 | 0.1106 |  |
| **Hypertension** | **+0.2913** | 0.0962 | ±0.1923 | **+3.030** | **0.0024** | ** |
| High cholesterol | -0.0858 | 0.0920 | ±0.1840 | -0.933 | 0.3509 |  |
| Kidney disease | +0.1246 | 0.1379 | ±0.2758 | +0.903 | 0.3664 |  |
| **Circulatory disease** | **+0.2754** | 0.1290 | ±0.2579 | **+2.136** | **0.0327** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **2100**, R² = **0.3027**, Adj R² = **0.2980**, F-statistic = **64.65** (p = **8.18e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.1**, BIC = **8940.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7855** | 0.4509 | ±0.9018 | **+52.751** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1175 | 0.0924 | ±0.1849 | -1.271 | 0.2039 |  |
| Education: high school or below (vs college) | +0.1853 | 0.1576 | ±0.3151 | +1.176 | 0.2397 |  |
| Site: UCSD (vs UAB) | -0.1177 | 0.1108 | ±0.2215 | -1.062 | 0.2881 |  |
| **Site: UW (vs UAB)** | **-1.1183** | 0.1077 | ±0.2154 | **-10.383** | **2.95e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3594** | 0.1205 | ±0.2411 | **-2.981** | **0.0029** | ** |
| **Season: summer (vs autumn)** | **+1.8943** | 0.1386 | ±0.2772 | **+13.668** | **1.57e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3116** | 0.1232 | ±0.2463 | **-10.649** | **1.76e-26** | *** |
| **Age (years)** | **+0.0103** | 0.0042 | ±0.0084 | **+2.451** | **0.0143** | * |
| BMI (kg/m2) | +0.0099 | 0.0067 | ±0.0133 | +1.491 | 0.1361 |  |
| **Hypertension** | **+0.2850** | 0.0960 | ±0.1921 | **+2.968** | **0.0030** | ** |
| High cholesterol | -0.0914 | 0.0929 | ±0.1858 | -0.984 | 0.3251 |  |
| Kidney disease | +0.1192 | 0.1383 | ±0.2767 | +0.861 | 0.3891 |  |
| **Circulatory disease** | **+0.2727** | 0.1293 | ±0.2587 | **+2.108** | **0.0350** | * |
| HbA1c (%) | +0.0300 | 0.0548 | ±0.1096 | +0.548 | 0.5840 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **1.00e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9020** | 0.3893 | ±0.7786 | **+61.400** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1202 | 0.0922 | ±0.1843 | -1.304 | 0.1921 |  |
| Education: high school or below (vs college) | +0.1935 | 0.1574 | ±0.3148 | +1.229 | 0.2191 |  |
| Site: UCSD (vs UAB) | -0.1192 | 0.1108 | ±0.2215 | -1.076 | 0.2818 |  |
| **Site: UW (vs UAB)** | **-1.1213** | 0.1077 | ±0.2155 | **-10.407** | **2.30e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3632** | 0.1200 | ±0.2399 | **-3.028** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8933** | 0.1385 | ±0.2771 | **+13.666** | **1.61e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3130** | 0.1232 | ±0.2463 | **-10.662** | **1.53e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.479** | **0.0132** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.565 | 0.1177 |  |
| **Hypertension** | **+0.2890** | 0.0958 | ±0.1917 | **+3.015** | **0.0026** | ** |
| High cholesterol | -0.0872 | 0.0920 | ±0.1840 | -0.948 | 0.3432 |  |
| Kidney disease | +0.1207 | 0.1384 | ±0.2767 | +0.872 | 0.3829 |  |
| **Circulatory disease** | **+0.2744** | 0.1292 | ±0.2585 | **+2.123** | **0.0337** | * |
| Mean glucose (mg/dL) | +0.0003 | 0.0014 | ±0.0028 | +0.244 | 0.8073 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **1.00e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8543** | 0.4968 | ±0.9937 | **+48.013** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1202 | 0.0922 | ±0.1843 | -1.304 | 0.1921 |  |
| Education: high school or below (vs college) | +0.1935 | 0.1574 | ±0.3148 | +1.229 | 0.2191 |  |
| Site: UCSD (vs UAB) | -0.1192 | 0.1108 | ±0.2215 | -1.076 | 0.2818 |  |
| **Site: UW (vs UAB)** | **-1.1213** | 0.1077 | ±0.2155 | **-10.407** | **2.30e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3632** | 0.1200 | ±0.2399 | **-3.028** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8933** | 0.1385 | ±0.2771 | **+13.666** | **1.61e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3130** | 0.1232 | ±0.2463 | **-10.662** | **1.53e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.479** | **0.0132** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.565 | 0.1177 |  |
| **Hypertension** | **+0.2890** | 0.0958 | ±0.1917 | **+3.015** | **0.0026** | ** |
| High cholesterol | -0.0872 | 0.0920 | ±0.1840 | -0.948 | 0.3432 |  |
| Kidney disease | +0.1207 | 0.1384 | ±0.2767 | +0.872 | 0.3829 |  |
| **Circulatory disease** | **+0.2744** | 0.1292 | ±0.2585 | **+2.123** | **0.0337** | * |
| GMI (%) | +0.0144 | 0.0591 | ±0.1181 | +0.244 | 0.8073 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **2100**, R² = **0.3025**, Adj R² = **0.2979**, F-statistic = **64.60** (p = **1.04e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9361** | 0.3887 | ±0.7775 | **+61.574** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1209 | 0.0922 | ±0.1844 | -1.311 | 0.1898 |  |
| Education: high school or below (vs college) | +0.1973 | 0.1573 | ±0.3145 | +1.255 | 0.2097 |  |
| Site: UCSD (vs UAB) | -0.1208 | 0.1106 | ±0.2213 | -1.092 | 0.2749 |  |
| **Site: UW (vs UAB)** | **-1.1222** | 0.1077 | ±0.2154 | **-10.422** | **1.97e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3635** | 0.1199 | ±0.2398 | **-3.031** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8927** | 0.1385 | ±0.2770 | **+13.664** | **1.66e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3136** | 0.1232 | ±0.2464 | **-10.662** | **1.53e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.500** | **0.0124** | * |
| BMI (kg/m2) | +0.0105 | 0.0067 | ±0.0134 | +1.566 | 0.1174 |  |
| **Hypertension** | **+0.2912** | 0.0958 | ±0.1916 | **+3.039** | **0.0024** | ** |
| High cholesterol | -0.0860 | 0.0920 | ±0.1841 | -0.934 | 0.3503 |  |
| Kidney disease | +0.1243 | 0.1379 | ±0.2759 | +0.901 | 0.3675 |  |
| **Circulatory disease** | **+0.2753** | 0.1292 | ±0.2584 | **+2.131** | **0.0331** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.0000 | 0.0014 | ±0.0028 | +0.023 | 0.9817 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **1.01e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9237** | 0.3680 | ±0.7359 | **+65.016** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1197 | 0.0923 | ±0.1845 | -1.298 | 0.1943 |  |
| Education: high school or below (vs college) | +0.1942 | 0.1572 | ±0.3145 | +1.235 | 0.2169 |  |
| Site: UCSD (vs UAB) | -0.1188 | 0.1108 | ±0.2216 | -1.072 | 0.2835 |  |
| **Site: UW (vs UAB)** | **-1.1205** | 0.1079 | ±0.2157 | **-10.390** | **2.76e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3631** | 0.1200 | ±0.2400 | **-3.026** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8931** | 0.1385 | ±0.2771 | **+13.665** | **1.65e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3131** | 0.1233 | ±0.2465 | **-10.654** | **1.68e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.467** | **0.0136** | * |
| BMI (kg/m2) | +0.0104 | 0.0066 | ±0.0132 | +1.578 | 0.1146 |  |
| **Hypertension** | **+0.2888** | 0.0964 | ±0.1927 | **+2.997** | **0.0027** | ** |
| High cholesterol | -0.0868 | 0.0921 | ±0.1841 | -0.943 | 0.3459 |  |
| Kidney disease | +0.1186 | 0.1403 | ±0.2805 | +0.845 | 0.3979 |  |
| **Circulatory disease** | **+0.2743** | 0.1291 | ±0.2582 | **+2.125** | **0.0336** | * |
| Glucose SD, pooled (mg/dL) | +0.0009 | 0.0041 | ±0.0082 | +0.226 | 0.8211 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.3025**, Adj R² = **0.2979**, F-statistic = **64.60** (p = **1.04e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9377** | 0.3683 | ±0.7366 | **+64.992** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1209 | 0.0923 | ±0.1846 | -1.310 | 0.1903 |  |
| Education: high school or below (vs college) | +0.1972 | 0.1571 | ±0.3143 | +1.255 | 0.2094 |  |
| Site: UCSD (vs UAB) | -0.1207 | 0.1107 | ±0.2213 | -1.090 | 0.2755 |  |
| **Site: UW (vs UAB)** | **-1.1221** | 0.1077 | ±0.2154 | **-10.417** | **2.06e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3634** | 0.1200 | ±0.2399 | **-3.029** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8927** | 0.1386 | ±0.2771 | **+13.660** | **1.75e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3135** | 0.1232 | ±0.2465 | **-10.660** | **1.57e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.485** | **0.0130** | * |
| BMI (kg/m2) | +0.0105 | 0.0066 | ±0.0132 | +1.591 | 0.1116 |  |
| **Hypertension** | **+0.2910** | 0.0965 | ±0.1929 | **+3.017** | **0.0026** | ** |
| High cholesterol | -0.0859 | 0.0920 | ±0.1840 | -0.934 | 0.3503 |  |
| Kidney disease | +0.1238 | 0.1401 | ±0.2802 | +0.884 | 0.3767 |  |
| **Circulatory disease** | **+0.2753** | 0.1291 | ±0.2582 | **+2.133** | **0.0329** | * |
| Avg. daily SD (mg/dL) | +0.0001 | 0.0045 | ±0.0089 | +0.028 | 0.9779 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **9.89e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.5**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8981** | 0.3896 | ±0.7791 | **+61.346** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1194 | 0.0922 | ±0.1844 | -1.295 | 0.1952 |  |
| Education: high school or below (vs college) | +0.1953 | 0.1567 | ±0.3133 | +1.246 | 0.2126 |  |
| Site: UCSD (vs UAB) | -0.1184 | 0.1105 | ±0.2210 | -1.071 | 0.2840 |  |
| **Site: UW (vs UAB)** | **-1.1200** | 0.1076 | ±0.2152 | **-10.408** | **2.28e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3628** | 0.1200 | ±0.2400 | **-3.023** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8926** | 0.1385 | ±0.2769 | **+13.669** | **1.55e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3132** | 0.1233 | ±0.2466 | **-10.652** | **1.72e-26** | *** |
| **Age (years)** | **+0.0103** | 0.0042 | ±0.0084 | **+2.464** | **0.0137** | * |
| BMI (kg/m2) | +0.0104 | 0.0066 | ±0.0131 | +1.590 | 0.1118 |  |
| **Hypertension** | **+0.2887** | 0.0967 | ±0.1935 | **+2.984** | **0.0028** | ** |
| High cholesterol | -0.0861 | 0.0921 | ±0.1841 | -0.936 | 0.3494 |  |
| Kidney disease | +0.1175 | 0.1404 | ±0.2808 | +0.837 | 0.4027 |  |
| **Circulatory disease** | **+0.2744** | 0.1290 | ±0.2579 | **+2.128** | **0.0334** | * |
| CV (%) | +0.0026 | 0.0086 | ±0.0171 | +0.301 | 0.7633 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.60** (p = **1.03e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9643** | 0.4125 | ±0.8250 | **+58.096** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1204 | 0.0922 | ±0.1845 | -1.305 | 0.1918 |  |
| Education: high school or below (vs college) | +0.1967 | 0.1564 | ±0.3129 | +1.257 | 0.2087 |  |
| Site: UCSD (vs UAB) | -0.1201 | 0.1104 | ±0.2208 | -1.088 | 0.2768 |  |
| **Site: UW (vs UAB)** | **-1.1216** | 0.1075 | ±0.2149 | **-10.437** | **1.69e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3634** | 0.1200 | ±0.2399 | **-3.029** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8925** | 0.1384 | ±0.2769 | **+13.671** | **1.50e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3136** | 0.1232 | ±0.2464 | **-10.661** | **1.54e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.485** | **0.0130** | * |
| BMI (kg/m2) | +0.0105 | 0.0066 | ±0.0131 | +1.593 | 0.1112 |  |
| **Hypertension** | **+0.2903** | 0.0966 | ±0.1933 | **+3.004** | **0.0027** | ** |
| High cholesterol | -0.0860 | 0.0921 | ±0.1842 | -0.934 | 0.3502 |  |
| Kidney disease | +0.1225 | 0.1395 | ±0.2790 | +0.878 | 0.3799 |  |
| **Circulatory disease** | **+0.2750** | 0.1290 | ±0.2579 | **+2.133** | **0.0330** | * |
| Mean / SD ratio | -0.0039 | 0.0331 | ±0.0662 | -0.116 | 0.9074 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.3025**, Adj R² = **0.2979**, F-statistic = **64.60** (p = **1.03e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9217** | 0.4124 | ±0.8248 | **+58.005** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1214 | 0.0924 | ±0.1847 | -1.314 | 0.1888 |  |
| Education: high school or below (vs college) | +0.1984 | 0.1564 | ±0.3127 | +1.269 | 0.2045 |  |
| Site: UCSD (vs UAB) | -0.1214 | 0.1103 | ±0.2207 | -1.100 | 0.2714 |  |
| **Site: UW (vs UAB)** | **-1.1226** | 0.1074 | ±0.2147 | **-10.455** | **1.38e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3637** | 0.1200 | ±0.2400 | **-3.030** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8926** | 0.1385 | ±0.2770 | **+13.666** | **1.62e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3137** | 0.1232 | ±0.2465 | **-10.659** | **1.58e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.504** | **0.0123** | * |
| BMI (kg/m2) | +0.0105 | 0.0066 | ±0.0131 | +1.596 | 0.1105 |  |
| **Hypertension** | **+0.2920** | 0.0966 | ±0.1933 | **+3.021** | **0.0025** | ** |
| High cholesterol | -0.0857 | 0.0921 | ±0.1842 | -0.931 | 0.3519 |  |
| Kidney disease | +0.1260 | 0.1394 | ±0.2788 | +0.904 | 0.3660 |  |
| **Circulatory disease** | **+0.2755** | 0.1290 | ±0.2580 | **+2.136** | **0.0327** | * |
| Avg. daily mean/SD | +0.0024 | 0.0284 | ±0.0568 | +0.084 | 0.9331 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **1.03e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9667** | 0.4138 | ±0.8276 | **+57.915** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1217 | 0.0924 | ±0.1847 | -1.318 | 0.1876 |  |
| Education: high school or below (vs college) | +0.1989 | 0.1565 | ±0.3130 | +1.271 | 0.2038 |  |
| Site: UCSD (vs UAB) | -0.1220 | 0.1105 | ±0.2210 | -1.104 | 0.2696 |  |
| **Site: UW (vs UAB)** | **-1.1238** | 0.1080 | ±0.2160 | **-10.408** | **2.28e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3637** | 0.1200 | ±0.2400 | **-3.031** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8920** | 0.1387 | ±0.2774 | **+13.641** | **2.29e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3141** | 0.1233 | ±0.2466 | **-10.659** | **1.58e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.499** | **0.0125** | * |
| BMI (kg/m2) | +0.0105 | 0.0066 | ±0.0132 | +1.596 | 0.1104 |  |
| **Hypertension** | **+0.2917** | 0.0961 | ±0.1922 | **+3.035** | **0.0024** | ** |
| High cholesterol | -0.0859 | 0.0921 | ±0.1841 | -0.933 | 0.3506 |  |
| Kidney disease | +0.1262 | 0.1389 | ±0.2779 | +0.908 | 0.3636 |  |
| **Circulatory disease** | **+0.2756** | 0.1290 | ±0.2580 | **+2.137** | **0.0326** | * |
| MAG (mg/dL/h) | -0.0007 | 0.0051 | ±0.0102 | -0.129 | 0.8972 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **2100**, R² = **0.3025**, Adj R² = **0.2979**, F-statistic = **64.60** (p = **1.04e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9422** | 0.3772 | ±0.7545 | **+63.469** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1211 | 0.0922 | ±0.1844 | -1.313 | 0.1891 |  |
| Education: high school or below (vs college) | +0.1980 | 0.1570 | ±0.3139 | +1.262 | 0.2071 |  |
| Site: UCSD (vs UAB) | -0.1211 | 0.1106 | ±0.2212 | -1.095 | 0.2734 |  |
| **Site: UW (vs UAB)** | **-1.1224** | 0.1077 | ±0.2153 | **-10.424** | **1.93e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3635** | 0.1200 | ±0.2399 | **-3.031** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8926** | 0.1385 | ±0.2770 | **+13.665** | **1.65e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3137** | 0.1232 | ±0.2464 | **-10.663** | **1.52e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.492** | **0.0127** | * |
| BMI (kg/m2) | +0.0105 | 0.0066 | ±0.0131 | +1.594 | 0.1109 |  |
| **Hypertension** | **+0.2915** | 0.0964 | ±0.1928 | **+3.025** | **0.0025** | ** |
| High cholesterol | -0.0857 | 0.0920 | ±0.1840 | -0.932 | 0.3512 |  |
| Kidney disease | +0.1251 | 0.1401 | ±0.2803 | +0.893 | 0.3719 |  |
| **Circulatory disease** | **+0.2755** | 0.1291 | ±0.2581 | **+2.135** | **0.0328** | * |
| Avg. daily range (mg/dL) | -0.0000 | 0.0012 | ±0.0024 | -0.024 | 0.9811 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **2100**, R² = **0.3027**, Adj R² = **0.2980**, F-statistic = **64.64** (p = **8.67e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.3**, BIC = **8941.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9171** | 0.3635 | ±0.7270 | **+65.796** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1173 | 0.0921 | ±0.1843 | -1.273 | 0.2030 |  |
| Education: high school or below (vs college) | +0.1922 | 0.1571 | ±0.3142 | +1.224 | 0.2211 |  |
| Site: UCSD (vs UAB) | -0.1165 | 0.1111 | ±0.2221 | -1.049 | 0.2941 |  |
| **Site: UW (vs UAB)** | **-1.1182** | 0.1082 | ±0.2165 | **-10.332** | **5.04e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3642** | 0.1200 | ±0.2401 | **-3.034** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8909** | 0.1385 | ±0.2769 | **+13.657** | **1.84e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3145** | 0.1232 | ±0.2464 | **-10.669** | **1.42e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.491** | **0.0127** | * |
| BMI (kg/m2) | +0.0101 | 0.0066 | ±0.0132 | +1.531 | 0.1258 |  |
| **Hypertension** | **+0.2870** | 0.0963 | ±0.1925 | **+2.981** | **0.0029** | ** |
| High cholesterol | -0.0882 | 0.0921 | ±0.1841 | -0.958 | 0.3383 |  |
| Kidney disease | +0.1154 | 0.1393 | ±0.2785 | +0.829 | 0.4073 |  |
| **Circulatory disease** | **+0.2708** | 0.1291 | ±0.2581 | **+2.098** | **0.0359** | * |
| SD of daily means (mg/dL) | +0.0043 | 0.0086 | ±0.0171 | +0.497 | 0.6193 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **2100**, R² = **0.3027**, Adj R² = **0.2980**, F-statistic = **64.64** (p = **8.77e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.3**, BIC = **8941.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0712** | 0.4384 | ±0.8769 | **+54.904** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1184 | 0.0922 | ±0.1844 | -1.284 | 0.1991 |  |
| Education: high school or below (vs college) | +0.1888 | 0.1576 | ±0.3153 | +1.197 | 0.2312 |  |
| Site: UCSD (vs UAB) | -0.1154 | 0.1110 | ±0.2219 | -1.040 | 0.2982 |  |
| **Site: UW (vs UAB)** | **-1.1184** | 0.1080 | ±0.2160 | **-10.357** | **3.87e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3627** | 0.1200 | ±0.2400 | **-3.022** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8942** | 0.1386 | ±0.2773 | **+13.662** | **1.71e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3130** | 0.1232 | ±0.2463 | **-10.661** | **1.55e-26** | *** |
| **Age (years)** | **+0.0103** | 0.0042 | ±0.0084 | **+2.459** | **0.0139** | * |
| BMI (kg/m2) | +0.0102 | 0.0066 | ±0.0132 | +1.545 | 0.1224 |  |
| **Hypertension** | **+0.2874** | 0.0960 | ±0.1920 | **+2.995** | **0.0027** | ** |
| High cholesterol | -0.0881 | 0.0920 | ±0.1839 | -0.958 | 0.3381 |  |
| Kidney disease | +0.1148 | 0.1383 | ±0.2766 | +0.830 | 0.4066 |  |
| **Circulatory disease** | **+0.2730** | 0.1292 | ±0.2583 | **+2.114** | **0.0346** | * |
| Time in range 70-180, pooled (%) | -0.0013 | 0.0024 | ±0.0048 | -0.542 | 0.5881 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2980**, F-statistic = **64.63** (p = **9.08e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.4**, BIC = **8941.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0567** | 0.4388 | ±0.8775 | **+54.830** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1188 | 0.0922 | ±0.1844 | -1.288 | 0.1977 |  |
| Education: high school or below (vs college) | +0.1897 | 0.1577 | ±0.3153 | +1.203 | 0.2290 |  |
| Site: UCSD (vs UAB) | -0.1160 | 0.1110 | ±0.2220 | -1.045 | 0.2959 |  |
| **Site: UW (vs UAB)** | **-1.1188** | 0.1080 | ±0.2160 | **-10.361** | **3.75e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3629** | 0.1200 | ±0.2400 | **-3.025** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8938** | 0.1386 | ±0.2772 | **+13.662** | **1.72e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3133** | 0.1232 | ±0.2463 | **-10.663** | **1.51e-26** | *** |
| **Age (years)** | **+0.0103** | 0.0042 | ±0.0084 | **+2.461** | **0.0138** | * |
| BMI (kg/m2) | +0.0102 | 0.0066 | ±0.0132 | +1.549 | 0.1215 |  |
| **Hypertension** | **+0.2880** | 0.0960 | ±0.1920 | **+2.999** | **0.0027** | ** |
| High cholesterol | -0.0879 | 0.0920 | ±0.1839 | -0.956 | 0.3392 |  |
| Kidney disease | +0.1157 | 0.1383 | ±0.2765 | +0.837 | 0.4025 |  |
| **Circulatory disease** | **+0.2732** | 0.1291 | ±0.2583 | **+2.116** | **0.0344** | * |
| Avg. daily time in range 70-180 (%) | -0.0012 | 0.0024 | ±0.0048 | -0.479 | 0.6318 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.3027**, Adj R² = **0.2980**, F-statistic = **64.64** (p = **8.87e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.3**, BIC = **8941.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9676** | 0.3651 | ±0.7301 | **+65.652** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1222 | 0.0920 | ±0.1840 | -1.328 | 0.1843 |  |
| Education: high school or below (vs college) | +0.1923 | 0.1561 | ±0.3122 | +1.232 | 0.2178 |  |
| Site: UCSD (vs UAB) | -0.1272 | 0.1113 | ±0.2226 | -1.143 | 0.2531 |  |
| **Site: UW (vs UAB)** | **-1.1258** | 0.1080 | ±0.2160 | **-10.424** | **1.93e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3637** | 0.1199 | ±0.2397 | **-3.035** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8912** | 0.1386 | ±0.2771 | **+13.648** | **2.07e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3155** | 0.1232 | ±0.2465 | **-10.675** | **1.34e-26** | *** |
| **Age (years)** | **+0.0103** | 0.0042 | ±0.0084 | **+2.455** | **0.0141** | * |
| BMI (kg/m2) | +0.0106 | 0.0066 | ±0.0131 | +1.618 | 0.1057 |  |
| **Hypertension** | **+0.2918** | 0.0962 | ±0.1924 | **+3.033** | **0.0024** | ** |
| High cholesterol | -0.0890 | 0.0918 | ±0.1837 | -0.969 | 0.3325 |  |
| Kidney disease | +0.1232 | 0.1380 | ±0.2761 | +0.892 | 0.3721 |  |
| **Circulatory disease** | **+0.2794** | 0.1289 | ±0.2579 | **+2.167** | **0.0303** | * |
| Any reading < 54 during wear (0/1) | -0.0540 | 0.0972 | ±0.1945 | -0.555 | 0.5786 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.3037**, Adj R² = **0.2990**, F-statistic = **64.95** (p = **1.96e-152**), Residual SE = **1.985** on **2085** df, AIC = **8853.2**, BIC = **8938.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8864** | 0.3622 | ±0.7244 | **+65.944** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1182 | 0.0920 | ±0.1841 | -1.284 | 0.1990 |  |
| Education: high school or below (vs college) | +0.2113 | 0.1564 | ±0.3127 | +1.352 | 0.1765 |  |
| Site: UCSD (vs UAB) | -0.0975 | 0.1111 | ±0.2222 | -0.877 | 0.3804 |  |
| **Site: UW (vs UAB)** | **-1.1030** | 0.1079 | ±0.2158 | **-10.225** | **1.53e-24** | *** |
| **Season: spring (vs autumn)** | **-0.3597** | 0.1200 | ±0.2401 | **-2.997** | **0.0027** | ** |
| **Season: summer (vs autumn)** | **+1.8907** | 0.1384 | ±0.2769 | **+13.658** | **1.80e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3135** | 0.1231 | ±0.2462 | **-10.668** | **1.44e-26** | *** |
| **Age (years)** | **+0.0106** | 0.0042 | ±0.0084 | **+2.545** | **0.0109** | * |
| BMI (kg/m2) | +0.0105 | 0.0066 | ±0.0132 | +1.589 | 0.1121 |  |
| **Hypertension** | **+0.2949** | 0.0961 | ±0.1921 | **+3.070** | **0.0021** | ** |
| High cholesterol | -0.0765 | 0.0920 | ±0.1839 | -0.832 | 0.4052 |  |
| Kidney disease | +0.1250 | 0.1379 | ±0.2757 | +0.907 | 0.3646 |  |
| **Circulatory disease** | **+0.2701** | 0.1288 | ±0.2576 | **+2.097** | **0.0360** | * |
| Time < 54 (%) | +0.1554 | 0.0954 | ±0.1908 | +1.629 | 0.1033 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.3034**, Adj R² = **0.2987**, F-statistic = **64.87** (p = **2.88e-152**), Residual SE = **1.985** on **2085** df, AIC = **8854.0**, BIC = **8938.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9097** | 0.3612 | ±0.7225 | **+66.190** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1168 | 0.0920 | ±0.1840 | -1.269 | 0.2044 |  |
| Education: high school or below (vs college) | +0.2087 | 0.1562 | ±0.3125 | +1.336 | 0.1816 |  |
| Site: UCSD (vs UAB) | -0.1033 | 0.1109 | ±0.2218 | -0.932 | 0.3515 |  |
| **Site: UW (vs UAB)** | **-1.1045** | 0.1078 | ±0.2156 | **-10.244** | **1.25e-24** | *** |
| **Season: spring (vs autumn)** | **-0.3595** | 0.1200 | ±0.2400 | **-2.995** | **0.0027** | ** |
| **Season: summer (vs autumn)** | **+1.8910** | 0.1385 | ±0.2771 | **+13.649** | **2.04e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3152** | 0.1231 | ±0.2462 | **-10.683** | **1.22e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.494** | **0.0126** | * |
| BMI (kg/m2) | +0.0104 | 0.0066 | ±0.0131 | +1.590 | 0.1119 |  |
| **Hypertension** | **+0.2950** | 0.0961 | ±0.1921 | **+3.071** | **0.0021** | ** |
| High cholesterol | -0.0786 | 0.0919 | ±0.1838 | -0.855 | 0.3926 |  |
| Kidney disease | +0.1235 | 0.1378 | ±0.2756 | +0.896 | 0.3702 |  |
| **Circulatory disease** | **+0.2707** | 0.1288 | ±0.2576 | **+2.102** | **0.0355** | * |
| Avg. daily time < 54 (%) | +0.1638 | 0.1283 | ±0.2566 | +1.277 | 0.2017 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.3031**, Adj R² = **0.2984**, F-statistic = **64.77** (p = **4.74e-152**), Residual SE = **1.985** on **2085** df, AIC = **8855.0**, BIC = **8939.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9058** | 0.3630 | ±0.7259 | **+65.864** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1158 | 0.0922 | ±0.1843 | -1.256 | 0.2091 |  |
| Education: high school or below (vs college) | +0.2051 | 0.1561 | ±0.3123 | +1.314 | 0.1889 |  |
| Site: UCSD (vs UAB) | -0.1097 | 0.1108 | ±0.2216 | -0.990 | 0.3223 |  |
| **Site: UW (vs UAB)** | **-1.1110** | 0.1077 | ±0.2154 | **-10.314** | **6.08e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3612** | 0.1199 | ±0.2398 | **-3.012** | **0.0026** | ** |
| **Season: summer (vs autumn)** | **+1.8936** | 0.1383 | ±0.2765 | **+13.696** | **1.07e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3149** | 0.1232 | ±0.2464 | **-10.674** | **1.35e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.513** | **0.0120** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.570 | 0.1165 |  |
| **Hypertension** | **+0.2946** | 0.0960 | ±0.1921 | **+3.068** | **0.0022** | ** |
| High cholesterol | -0.0814 | 0.0921 | ±0.1842 | -0.884 | 0.3769 |  |
| Kidney disease | +0.1243 | 0.1379 | ±0.2757 | +0.902 | 0.3671 |  |
| **Circulatory disease** | **+0.2734** | 0.1290 | ±0.2580 | **+2.120** | **0.0340** | * |
| Time 54-69, pooled (%) | +0.0383 | 0.0277 | ±0.0554 | +1.383 | 0.1668 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2100**, R² = **0.3034**, Adj R² = **0.2987**, F-statistic = **64.86** (p = **3.06e-152**), Residual SE = **1.985** on **2085** df, AIC = **8854.1**, BIC = **8938.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9075** | 0.3620 | ±0.7241 | **+66.034** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1137 | 0.0921 | ±0.1843 | -1.234 | 0.2172 |  |
| Education: high school or below (vs college) | +0.2063 | 0.1561 | ±0.3122 | +1.321 | 0.1863 |  |
| Site: UCSD (vs UAB) | -0.1092 | 0.1107 | ±0.2214 | -0.986 | 0.3241 |  |
| **Site: UW (vs UAB)** | **-1.1082** | 0.1076 | ±0.2153 | **-10.295** | **7.39e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3608** | 0.1199 | ±0.2398 | **-3.010** | **0.0026** | ** |
| **Season: summer (vs autumn)** | **+1.8941** | 0.1382 | ±0.2764 | **+13.704** | **9.57e-43** | *** |
| **Season: winter (vs autumn)** | **-1.3164** | 0.1231 | ±0.2463 | **-10.689** | **1.14e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.493** | **0.0127** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.563 | 0.1181 |  |
| **Hypertension** | **+0.2955** | 0.0960 | ±0.1920 | **+3.078** | **0.0021** | ** |
| High cholesterol | -0.0809 | 0.0920 | ±0.1841 | -0.879 | 0.3796 |  |
| Kidney disease | +0.1246 | 0.1378 | ±0.2756 | +0.904 | 0.3659 |  |
| **Circulatory disease** | **+0.2735** | 0.1289 | ±0.2579 | **+2.122** | **0.0339** | * |
| Avg. daily time 54-69 (%) | +0.0472 | 0.0274 | ±0.0548 | +1.725 | 0.0845 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **2100**, R² = **0.3033**, Adj R² = **0.2987**, F-statistic = **64.85** (p = **3.17e-152**), Residual SE = **1.985** on **2085** df, AIC = **8854.2**, BIC = **8938.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8929** | 0.3630 | ±0.7259 | **+65.829** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1151 | 0.0921 | ±0.1842 | -1.250 | 0.2113 |  |
| Education: high school or below (vs college) | +0.2084 | 0.1561 | ±0.3122 | +1.335 | 0.1819 |  |
| Site: UCSD (vs UAB) | -0.1040 | 0.1109 | ±0.2218 | -0.938 | 0.3483 |  |
| **Site: UW (vs UAB)** | **-1.1064** | 0.1077 | ±0.2154 | **-10.271** | **9.53e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3603** | 0.1200 | ±0.2399 | **-3.004** | **0.0027** | ** |
| **Season: summer (vs autumn)** | **+1.8931** | 0.1383 | ±0.2765 | **+13.691** | **1.14e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3149** | 0.1232 | ±0.2463 | **-10.677** | **1.31e-26** | *** |
| **Age (years)** | **+0.0106** | 0.0042 | ±0.0084 | **+2.524** | **0.0116** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.568 | 0.1169 |  |
| **Hypertension** | **+0.2955** | 0.0960 | ±0.1921 | **+3.077** | **0.0021** | ** |
| High cholesterol | -0.0791 | 0.0921 | ±0.1841 | -0.860 | 0.3900 |  |
| Kidney disease | +0.1245 | 0.1379 | ±0.2757 | +0.903 | 0.3666 |  |
| **Circulatory disease** | **+0.2721** | 0.1289 | ±0.2579 | **+2.110** | **0.0348** | * |
| Time < 70 (%) | +0.0381 | 0.0234 | ±0.0467 | +1.629 | 0.1032 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **2100**, R² = **0.3035**, Adj R² = **0.2988**, F-statistic = **64.90** (p = **2.47e-152**), Residual SE = **1.985** on **2085** df, AIC = **8853.7**, BIC = **8938.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9028** | 0.3619 | ±0.7238 | **+66.047** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1133 | 0.0921 | ±0.1842 | -1.231 | 0.2185 |  |
| Education: high school or below (vs college) | +0.2083 | 0.1561 | ±0.3122 | +1.335 | 0.1820 |  |
| Site: UCSD (vs UAB) | -0.1057 | 0.1107 | ±0.2215 | -0.955 | 0.3397 |  |
| **Site: UW (vs UAB)** | **-1.1050** | 0.1076 | ±0.2153 | **-10.265** | **1.01e-24** | *** |
| **Season: spring (vs autumn)** | **-0.3601** | 0.1199 | ±0.2398 | **-3.003** | **0.0027** | ** |
| **Season: summer (vs autumn)** | **+1.8935** | 0.1383 | ±0.2765 | **+13.695** | **1.08e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3165** | 0.1231 | ±0.2462 | **-10.694** | **1.09e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.492** | **0.0127** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.565 | 0.1177 |  |
| **Hypertension** | **+0.2961** | 0.0960 | ±0.1920 | **+3.084** | **0.0020** | ** |
| High cholesterol | -0.0795 | 0.0920 | ±0.1840 | -0.864 | 0.3877 |  |
| Kidney disease | +0.1243 | 0.1378 | ±0.2755 | +0.902 | 0.3669 |  |
| **Circulatory disease** | **+0.2725** | 0.1289 | ±0.2578 | **+2.114** | **0.0345** | * |
| Avg. daily time < 70 (%) | +0.0426 | 0.0240 | ±0.0481 | +1.774 | 0.0760 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2980**, F-statistic = **64.63** (p = **8.93e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.3**, BIC = **8941.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1548** | 0.5764 | ±1.1527 | **+41.910** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1182 | 0.0922 | ±0.1844 | -1.281 | 0.2001 |  |
| Education: high school or below (vs college) | +0.1900 | 0.1574 | ±0.3149 | +1.207 | 0.2275 |  |
| Site: UCSD (vs UAB) | -0.1167 | 0.1110 | ±0.2219 | -1.052 | 0.2928 |  |
| **Site: UW (vs UAB)** | **-1.1179** | 0.1081 | ±0.2163 | **-10.338** | **4.74e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3626** | 0.1200 | ±0.2401 | **-3.021** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8960** | 0.1388 | ±0.2775 | **+13.663** | **1.69e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3130** | 0.1232 | ±0.2464 | **-10.657** | **1.62e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.508** | **0.0121** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.567 | 0.1171 |  |
| **Hypertension** | **+0.2887** | 0.0960 | ±0.1919 | **+3.008** | **0.0026** | ** |
| High cholesterol | -0.0864 | 0.0920 | ±0.1841 | -0.939 | 0.3477 |  |
| Kidney disease | +0.1187 | 0.1383 | ±0.2766 | +0.858 | 0.3907 |  |
| **Circulatory disease** | **+0.2732** | 0.1292 | ±0.2584 | **+2.114** | **0.0345** | * |
| Time 54-250, pooled (%) | -0.0022 | 0.0045 | ±0.0091 | -0.488 | 0.6253 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.63** (p = **9.29e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.4**, BIC = **8941.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1273** | 0.5849 | ±1.1699 | **+41.249** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1186 | 0.0922 | ±0.1845 | -1.286 | 0.1985 |  |
| Education: high school or below (vs college) | +0.1911 | 0.1574 | ±0.3149 | +1.214 | 0.2248 |  |
| Site: UCSD (vs UAB) | -0.1174 | 0.1110 | ±0.2219 | -1.058 | 0.2902 |  |
| **Site: UW (vs UAB)** | **-1.1187** | 0.1081 | ±0.2162 | **-10.346** | **4.35e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3629** | 0.1200 | ±0.2400 | **-3.023** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8953** | 0.1388 | ±0.2775 | **+13.659** | **1.78e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3132** | 0.1232 | ±0.2464 | **-10.658** | **1.59e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.504** | **0.0123** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.569 | 0.1166 |  |
| **Hypertension** | **+0.2891** | 0.0960 | ±0.1919 | **+3.013** | **0.0026** | ** |
| High cholesterol | -0.0864 | 0.0920 | ±0.1841 | -0.938 | 0.3481 |  |
| Kidney disease | +0.1193 | 0.1383 | ±0.2766 | +0.863 | 0.3883 |  |
| **Circulatory disease** | **+0.2734** | 0.1292 | ±0.2584 | **+2.116** | **0.0344** | * |
| Avg. daily time 54-250 (%) | -0.0019 | 0.0046 | ±0.0092 | -0.416 | 0.6772 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **9.94e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.5**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9441** | 0.3615 | ±0.7230 | **+66.237** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1204 | 0.0921 | ±0.1843 | -1.307 | 0.1912 |  |
| Education: high school or below (vs college) | +0.1941 | 0.1572 | ±0.3144 | +1.235 | 0.2169 |  |
| Site: UCSD (vs UAB) | -0.1189 | 0.1106 | ±0.2211 | -1.075 | 0.2822 |  |
| **Site: UW (vs UAB)** | **-1.1215** | 0.1076 | ±0.2152 | **-10.421** | **1.98e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3633** | 0.1199 | ±0.2398 | **-3.030** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8922** | 0.1384 | ±0.2768 | **+13.673** | **1.48e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3134** | 0.1232 | ±0.2463 | **-10.665** | **1.49e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.451** | **0.0142** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.567 | 0.1171 |  |
| **Hypertension** | **+0.2895** | 0.0961 | ±0.1922 | **+3.013** | **0.0026** | ** |
| High cholesterol | -0.0874 | 0.0920 | ±0.1839 | -0.951 | 0.3418 |  |
| Kidney disease | +0.1197 | 0.1381 | ±0.2762 | +0.867 | 0.3861 |  |
| **Circulatory disease** | **+0.2746** | 0.1291 | ±0.2581 | **+2.128** | **0.0334** | * |
| Time 181-250, pooled (%) | +0.0010 | 0.0036 | ±0.0072 | +0.281 | 0.7785 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **1.01e-151**), Residual SE = **1.986** on **2085** df, AIC = **8856.6**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9430** | 0.3614 | ±0.7228 | **+66.247** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1206 | 0.0921 | ±0.1843 | -1.309 | 0.1905 |  |
| Education: high school or below (vs college) | +0.1948 | 0.1572 | ±0.3145 | +1.239 | 0.2153 |  |
| Site: UCSD (vs UAB) | -0.1193 | 0.1106 | ±0.2212 | -1.079 | 0.2808 |  |
| **Site: UW (vs UAB)** | **-1.1216** | 0.1076 | ±0.2153 | **-10.420** | **2.01e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3634** | 0.1199 | ±0.2398 | **-3.030** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8923** | 0.1384 | ±0.2768 | **+13.674** | **1.45e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3135** | 0.1232 | ±0.2463 | **-10.665** | **1.48e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.461** | **0.0139** | * |
| BMI (kg/m2) | +0.0104 | 0.0066 | ±0.0132 | +1.572 | 0.1158 |  |
| **Hypertension** | **+0.2899** | 0.0961 | ±0.1922 | **+3.016** | **0.0026** | ** |
| High cholesterol | -0.0871 | 0.0919 | ±0.1839 | -0.947 | 0.3437 |  |
| Kidney disease | +0.1208 | 0.1380 | ±0.2760 | +0.875 | 0.3813 |  |
| **Circulatory disease** | **+0.2748** | 0.1291 | ±0.2581 | **+2.129** | **0.0332** | * |
| Avg. daily time 181-250 (%) | +0.0008 | 0.0035 | ±0.0071 | +0.215 | 0.8299 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.62** (p = **9.43e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.4**, BIC = **8941.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9418** | 0.3610 | ±0.7220 | **+66.322** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1192 | 0.0922 | ±0.1844 | -1.293 | 0.1959 |  |
| Education: high school or below (vs college) | +0.1908 | 0.1576 | ±0.3153 | +1.210 | 0.2262 |  |
| Site: UCSD (vs UAB) | -0.1173 | 0.1109 | ±0.2217 | -1.058 | 0.2901 |  |
| **Site: UW (vs UAB)** | **-1.1198** | 0.1079 | ±0.2158 | **-10.378** | **3.11e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3630** | 0.1200 | ±0.2400 | **-3.025** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8937** | 0.1386 | ±0.2773 | **+13.659** | **1.78e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3131** | 0.1232 | ±0.2463 | **-10.661** | **1.54e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.466** | **0.0137** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.556 | 0.1197 |  |
| **Hypertension** | **+0.2883** | 0.0960 | ±0.1919 | **+3.005** | **0.0027** | ** |
| High cholesterol | -0.0877 | 0.0920 | ±0.1839 | -0.953 | 0.3403 |  |
| Kidney disease | +0.1173 | 0.1383 | ±0.2766 | +0.848 | 0.3964 |  |
| **Circulatory disease** | **+0.2737** | 0.1292 | ±0.2583 | **+2.119** | **0.0341** | * |
| Time > 180 (%) | +0.0010 | 0.0024 | ±0.0048 | +0.406 | 0.6845 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.62** (p = **9.71e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.5**, BIC = **8941.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9417** | 0.3611 | ±0.7221 | **+66.310** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1196 | 0.0922 | ±0.1844 | -1.297 | 0.1945 |  |
| Education: high school or below (vs college) | +0.1919 | 0.1577 | ±0.3153 | +1.217 | 0.2235 |  |
| Site: UCSD (vs UAB) | -0.1178 | 0.1109 | ±0.2218 | -1.062 | 0.2881 |  |
| **Site: UW (vs UAB)** | **-1.1202** | 0.1079 | ±0.2158 | **-10.381** | **3.02e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3632** | 0.1200 | ±0.2399 | **-3.027** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8935** | 0.1386 | ±0.2772 | **+13.659** | **1.78e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3133** | 0.1232 | ±0.2463 | **-10.663** | **1.52e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.470** | **0.0135** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.561 | 0.1186 |  |
| **Hypertension** | **+0.2889** | 0.0960 | ±0.1919 | **+3.010** | **0.0026** | ** |
| High cholesterol | -0.0874 | 0.0919 | ±0.1839 | -0.950 | 0.3420 |  |
| Kidney disease | +0.1184 | 0.1383 | ±0.2765 | +0.857 | 0.3917 |  |
| **Circulatory disease** | **+0.2740** | 0.1292 | ±0.2583 | **+2.121** | **0.0339** | * |
| Avg. daily time > 180 (%) | +0.0008 | 0.0024 | ±0.0048 | +0.336 | 0.7372 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.61** (p = **9.96e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.5**, BIC = **8941.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9415** | 0.3612 | ±0.7223 | **+66.289** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1194 | 0.0923 | ±0.1846 | -1.294 | 0.1958 |  |
| Education: high school or below (vs college) | +0.1935 | 0.1574 | ±0.3149 | +1.229 | 0.2191 |  |
| Site: UCSD (vs UAB) | -0.1185 | 0.1109 | ±0.2218 | -1.069 | 0.2852 |  |
| **Site: UW (vs UAB)** | **-1.1208** | 0.1079 | ±0.2159 | **-10.384** | **2.94e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3637** | 0.1200 | ±0.2399 | **-3.032** | **0.0024** | ** |
| **Season: summer (vs autumn)** | **+1.8934** | 0.1386 | ±0.2772 | **+13.659** | **1.77e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3139** | 0.1232 | ±0.2464 | **-10.665** | **1.49e-26** | *** |
| **Age (years)** | **+0.0104** | 0.0042 | ±0.0084 | **+2.495** | **0.0126** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0133 | +1.546 | 0.1222 |  |
| **Hypertension** | **+0.2900** | 0.0960 | ±0.1919 | **+3.023** | **0.0025** | ** |
| High cholesterol | -0.0868 | 0.0920 | ±0.1840 | -0.944 | 0.3453 |  |
| Kidney disease | +0.1210 | 0.1378 | ±0.2756 | +0.878 | 0.3801 |  |
| **Circulatory disease** | **+0.2745** | 0.1291 | ±0.2583 | **+2.125** | **0.0336** | * |
| Nocturnal time > 180 (%) | +0.0006 | 0.0024 | ±0.0049 | +0.260 | 0.7952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.3027**, Adj R² = **0.2980**, F-statistic = **64.65** (p = **8.39e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.2**, BIC = **8940.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9464** | 0.3617 | ±0.7233 | **+66.213** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1245 | 0.0924 | ±0.1848 | -1.347 | 0.1779 |  |
| Education: high school or below (vs college) | +0.2025 | 0.1565 | ±0.3130 | +1.294 | 0.1955 |  |
| Site: UCSD (vs UAB) | -0.1240 | 0.1106 | ±0.2212 | -1.122 | 0.2621 |  |
| **Site: UW (vs UAB)** | **-1.1234** | 0.1075 | ±0.2150 | **-10.448** | **1.49e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3668** | 0.1201 | ±0.2402 | **-3.054** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.8921** | 0.1384 | ±0.2769 | **+13.668** | **1.57e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3171** | 0.1233 | ±0.2467 | **-10.678** | **1.29e-26** | *** |
| **Age (years)** | **+0.0107** | 0.0042 | ±0.0084 | **+2.555** | **0.0106** | * |
| BMI (kg/m2) | +0.0104 | 0.0066 | ±0.0132 | +1.586 | 0.1127 |  |
| **Hypertension** | **+0.2968** | 0.0962 | ±0.1925 | **+3.084** | **0.0020** | ** |
| High cholesterol | -0.0822 | 0.0920 | ±0.1841 | -0.894 | 0.3715 |  |
| Kidney disease | +0.1336 | 0.1388 | ±0.2775 | +0.963 | 0.3357 |  |
| **Circulatory disease** | **+0.2755** | 0.1290 | ±0.2579 | **+2.136** | **0.0327** | * |
| Any reading > 250 during wear (0/1) | -0.0604 | 0.0923 | ±0.1847 | -0.654 | 0.5133 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.62** (p = **9.33e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.4**, BIC = **8941.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9354** | 0.3609 | ±0.7217 | **+66.328** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1186 | 0.0922 | ±0.1844 | -1.287 | 0.1983 |  |
| Education: high school or below (vs college) | +0.1911 | 0.1575 | ±0.3150 | +1.213 | 0.2250 |  |
| Site: UCSD (vs UAB) | -0.1177 | 0.1109 | ±0.2218 | -1.061 | 0.2886 |  |
| **Site: UW (vs UAB)** | **-1.1188** | 0.1081 | ±0.2162 | **-10.350** | **4.17e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3628** | 0.1200 | ±0.2401 | **-3.023** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8955** | 0.1388 | ±0.2776 | **+13.658** | **1.81e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3131** | 0.1232 | ±0.2464 | **-10.657** | **1.61e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.507** | **0.0122** | * |
| BMI (kg/m2) | +0.0103 | 0.0066 | ±0.0132 | +1.571 | 0.1162 |  |
| **Hypertension** | **+0.2890** | 0.0960 | ±0.1919 | **+3.012** | **0.0026** | ** |
| High cholesterol | -0.0865 | 0.0920 | ±0.1841 | -0.939 | 0.3475 |  |
| Kidney disease | +0.1196 | 0.1383 | ±0.2765 | +0.865 | 0.3869 |  |
| **Circulatory disease** | **+0.2736** | 0.1292 | ±0.2584 | **+2.117** | **0.0342** | * |
| Time > 250 (%) | +0.0019 | 0.0045 | ±0.0090 | +0.411 | 0.6814 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.3026**, Adj R² = **0.2979**, F-statistic = **64.62** (p = **9.55e-152**), Residual SE = **1.986** on **2085** df, AIC = **8856.5**, BIC = **8941.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9366** | 0.3609 | ±0.7217 | **+66.330** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1190 | 0.0922 | ±0.1845 | -1.290 | 0.1971 |  |
| Education: high school or below (vs college) | +0.1919 | 0.1574 | ±0.3149 | +1.219 | 0.2229 |  |
| Site: UCSD (vs UAB) | -0.1180 | 0.1109 | ±0.2218 | -1.064 | 0.2873 |  |
| **Site: UW (vs UAB)** | **-1.1193** | 0.1081 | ±0.2162 | **-10.356** | **3.93e-25** | *** |
| **Season: spring (vs autumn)** | **-0.3630** | 0.1200 | ±0.2400 | **-3.025** | **0.0025** | ** |
| **Season: summer (vs autumn)** | **+1.8950** | 0.1388 | ±0.2775 | **+13.656** | **1.87e-42** | *** |
| **Season: winter (vs autumn)** | **-1.3133** | 0.1232 | ±0.2464 | **-10.659** | **1.59e-26** | *** |
| **Age (years)** | **+0.0105** | 0.0042 | ±0.0084 | **+2.504** | **0.0123** | * |
| BMI (kg/m2) | +0.0104 | 0.0066 | ±0.0132 | +1.572 | 0.1159 |  |
| **Hypertension** | **+0.2894** | 0.0960 | ±0.1919 | **+3.016** | **0.0026** | ** |
| High cholesterol | -0.0864 | 0.0920 | ±0.1841 | -0.938 | 0.3481 |  |
| Kidney disease | +0.1200 | 0.1383 | ±0.2766 | +0.868 | 0.3854 |  |
| **Circulatory disease** | **+0.2737** | 0.1292 | ±0.2584 | **+2.118** | **0.0342** | * |
| Avg. daily time > 250 (%) | +0.0017 | 0.0046 | ±0.0092 | +0.359 | 0.7195 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 2,100; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2414**, F-statistic = **52.38** (p = **7.12e-118**), Residual SE = **5.971** on **2086** df, AIC = **13478.5**, BIC = **13557.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4444** | 1.0674 | ±2.1347 | **+46.324** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6180** | 0.2811 | ±0.5622 | **+2.198** | **0.0279** | * |
| Education: high school or below (vs college) | +0.5496 | 0.4554 | ±0.9107 | +1.207 | 0.2274 |  |
| **Site: UCSD (vs UAB)** | **+3.1579** | 0.3410 | ±0.6821 | **+9.260** | **2.05e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3227** | 0.3159 | ±0.6319 | **-4.186** | **2.84e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7771** | 0.3672 | ±0.7344 | **-4.840** | **1.30e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8522** | 0.3805 | ±0.7609 | **+4.868** | **1.13e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7086** | 0.3910 | ±0.7819 | **-14.602** | **2.74e-48** | *** |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0249 | **-3.882** | **1.04e-04** | *** |
| BMI (kg/m2) | -0.0184 | 0.0199 | ±0.0398 | -0.924 | 0.3553 |  |
| Hypertension | -0.0452 | 0.2938 | ±0.5876 | -0.154 | 0.8777 |  |
| **High cholesterol** | **-0.7535** | 0.2746 | ±0.5491 | **-2.744** | **0.0061** | ** |
| Kidney disease | +0.6620 | 0.4192 | ±0.8383 | +1.579 | 0.1143 |  |
| Circulatory disease | +0.1963 | 0.3675 | ±0.7351 | +0.534 | 0.5933 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2411**, F-statistic = **48.63** (p = **4.90e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.3**, BIC = **13565.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1895** | 1.2571 | ±2.5142 | **+39.129** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6238** | 0.2814 | ±0.5628 | **+2.217** | **0.0266** | * |
| Education: high school or below (vs college) | +0.5291 | 0.4593 | ±0.9185 | +1.152 | 0.2493 |  |
| **Site: UCSD (vs UAB)** | **+3.1633** | 0.3421 | ±0.6842 | **+9.247** | **2.31e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3161** | 0.3171 | ±0.6343 | **-4.150** | **3.33e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7703** | 0.3682 | ±0.7365 | **-4.807** | **1.53e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8549** | 0.3805 | ±0.7610 | **+4.875** | **1.09e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7053** | 0.3910 | ±0.7820 | **-14.592** | **3.16e-48** | *** |
| **Age (years)** | **-0.0487** | 0.0125 | ±0.0250 | **-3.891** | **9.97e-05** | *** |
| BMI (kg/m2) | -0.0193 | 0.0201 | ±0.0403 | -0.958 | 0.3380 |  |
| Hypertension | -0.0557 | 0.2941 | ±0.5882 | -0.189 | 0.8498 |  |
| **High cholesterol** | **-0.7627** | 0.2760 | ±0.5520 | **-2.763** | **0.0057** | ** |
| Kidney disease | +0.6531 | 0.4199 | ±0.8397 | +1.555 | 0.1198 |  |
| Circulatory disease | +0.1918 | 0.3680 | ±0.7361 | +0.521 | 0.6024 |  |
| HbA1c (%) | +0.0496 | 0.1329 | ±0.2658 | +0.373 | 0.7090 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2411**, F-statistic = **48.62** (p = **5.00e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.4**, BIC = **13565.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3036** | 1.1416 | ±2.2831 | **+43.190** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6209** | 0.2813 | ±0.5626 | **+2.207** | **0.0273** | * |
| Education: high school or below (vs college) | +0.5339 | 0.4588 | ±0.9177 | +1.164 | 0.2446 |  |
| **Site: UCSD (vs UAB)** | **+3.1642** | 0.3428 | ±0.6857 | **+9.230** | **2.72e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3192** | 0.3169 | ±0.6337 | **-4.163** | **3.14e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7760** | 0.3676 | ±0.7352 | **-4.831** | **1.36e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8546** | 0.3805 | ±0.7610 | **+4.874** | **1.09e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7064** | 0.3909 | ±0.7817 | **-14.600** | **2.82e-48** | *** |
| **Age (years)** | **-0.0486** | 0.0125 | ±0.0250 | **-3.889** | **1.01e-04** | *** |
| BMI (kg/m2) | -0.0189 | 0.0201 | ±0.0402 | -0.941 | 0.3469 |  |
| Hypertension | -0.0541 | 0.2943 | ±0.5887 | -0.184 | 0.8541 |  |
| **High cholesterol** | **-0.7587** | 0.2752 | ±0.5504 | **-2.757** | **0.0058** | ** |
| Kidney disease | +0.6476 | 0.4206 | ±0.8411 | +1.540 | 0.1236 |  |
| Circulatory disease | +0.1925 | 0.3680 | ±0.7360 | +0.523 | 0.6009 |  |
| Mean glucose (mg/dL) | +0.0013 | 0.0041 | ±0.0081 | +0.316 | 0.7517 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2411**, F-statistic = **48.62** (p = **5.00e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.4**, BIC = **13565.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1252** | 1.4414 | ±2.8827 | **+34.082** | **1.35e-254** | *** |
| **Education: graduate level (vs college)** | **+0.6209** | 0.2813 | ±0.5626 | **+2.207** | **0.0273** | * |
| Education: high school or below (vs college) | +0.5339 | 0.4588 | ±0.9177 | +1.164 | 0.2446 |  |
| **Site: UCSD (vs UAB)** | **+3.1642** | 0.3428 | ±0.6857 | **+9.230** | **2.72e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3192** | 0.3169 | ±0.6337 | **-4.163** | **3.14e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7760** | 0.3676 | ±0.7352 | **-4.831** | **1.36e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8546** | 0.3805 | ±0.7610 | **+4.874** | **1.09e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7064** | 0.3909 | ±0.7817 | **-14.600** | **2.82e-48** | *** |
| **Age (years)** | **-0.0486** | 0.0125 | ±0.0250 | **-3.889** | **1.01e-04** | *** |
| BMI (kg/m2) | -0.0189 | 0.0201 | ±0.0402 | -0.941 | 0.3469 |  |
| Hypertension | -0.0541 | 0.2943 | ±0.5887 | -0.184 | 0.8541 |  |
| **High cholesterol** | **-0.7587** | 0.2752 | ±0.5504 | **-2.757** | **0.0058** | ** |
| Kidney disease | +0.6476 | 0.4206 | ±0.8411 | +1.540 | 0.1236 |  |
| Circulatory disease | +0.1925 | 0.3680 | ±0.7360 | +0.523 | 0.6009 |  |
| GMI (%) | +0.0539 | 0.1703 | ±0.3406 | +0.316 | 0.7517 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2411**, F-statistic = **48.63** (p = **4.84e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.3**, BIC = **13565.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.2662** | 1.1368 | ±2.2736 | **+43.337** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6223** | 0.2813 | ±0.5626 | **+2.212** | **0.0270** | * |
| Education: high school or below (vs college) | +0.5306 | 0.4583 | ±0.9165 | +1.158 | 0.2469 |  |
| **Site: UCSD (vs UAB)** | **+3.1639** | 0.3424 | ±0.6847 | **+9.241** | **2.43e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3200** | 0.3165 | ±0.6330 | **-4.171** | **3.04e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7782** | 0.3674 | ±0.7348 | **-4.840** | **1.30e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8551** | 0.3805 | ±0.7611 | **+4.875** | **1.09e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7083** | 0.3911 | ±0.7821 | **-14.597** | **2.94e-48** | *** |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0249 | **-3.882** | **1.04e-04** | *** |
| BMI (kg/m2) | -0.0194 | 0.0203 | ±0.0406 | -0.957 | 0.3386 |  |
| Hypertension | -0.0543 | 0.2939 | ±0.5878 | -0.185 | 0.8533 |  |
| **High cholesterol** | **-0.7605** | 0.2753 | ±0.5507 | **-2.762** | **0.0057** | ** |
| Kidney disease | +0.6497 | 0.4195 | ±0.8390 | +1.549 | 0.1214 |  |
| Circulatory disease | +0.1925 | 0.3680 | ±0.7361 | +0.523 | 0.6009 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0016 | 0.0040 | ±0.0081 | +0.407 | 0.6842 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.2463**, Adj R² = **0.2412**, F-statistic = **48.66** (p = **4.12e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.0**, BIC = **13564.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5845** | 1.0871 | ±2.1742 | **+45.612** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6068** | 0.2822 | ±0.5644 | **+2.150** | **0.0315** | * |
| Education: high school or below (vs college) | +0.5802 | 0.4571 | ±0.9142 | +1.269 | 0.2043 |  |
| **Site: UCSD (vs UAB)** | **+3.1396** | 0.3435 | ±0.6869 | **+9.141** | **6.18e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3376** | 0.3177 | ±0.6355 | **-4.210** | **2.56e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7807** | 0.3674 | ±0.7347 | **-4.847** | **1.25e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8481** | 0.3806 | ±0.7611 | **+4.856** | **1.20e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7135** | 0.3912 | ±0.7824 | **-14.606** | **2.58e-48** | *** |
| **Age (years)** | **-0.0476** | 0.0125 | ±0.0250 | **-3.806** | **1.41e-04** | *** |
| BMI (kg/m2) | -0.0176 | 0.0199 | ±0.0399 | -0.883 | 0.3770 |  |
| Hypertension | -0.0231 | 0.2942 | ±0.5883 | -0.079 | 0.9374 |  |
| **High cholesterol** | **-0.7453** | 0.2749 | ±0.5498 | **-2.711** | **0.0067** | ** |
| Kidney disease | +0.7145 | 0.4253 | ±0.8506 | +1.680 | 0.0930 | . |
| Circulatory disease | +0.2057 | 0.3676 | ±0.7352 | +0.560 | 0.5758 |  |
| Glucose SD, pooled (mg/dL) | -0.0081 | 0.0113 | ±0.0227 | -0.715 | 0.4747 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2411**, F-statistic = **48.63** (p = **4.76e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.3**, BIC = **13565.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5356** | 1.0874 | ±2.1749 | **+45.553** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6116** | 0.2821 | ±0.5642 | **+2.168** | **0.0302** | * |
| Education: high school or below (vs college) | +0.5700 | 0.4574 | ±0.9147 | +1.246 | 0.2127 |  |
| **Site: UCSD (vs UAB)** | **+3.1468** | 0.3433 | ±0.6866 | **+9.166** | **4.89e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3312** | 0.3175 | ±0.6351 | **-4.192** | **2.76e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7799** | 0.3675 | ±0.7349 | **-4.844** | **1.27e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8483** | 0.3807 | ±0.7613 | **+4.856** | **1.20e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7130** | 0.3913 | ±0.7825 | **-14.602** | **2.73e-48** | *** |
| **Age (years)** | **-0.0478** | 0.0125 | ±0.0250 | **-3.821** | **1.33e-04** | *** |
| BMI (kg/m2) | -0.0180 | 0.0199 | ±0.0399 | -0.902 | 0.3671 |  |
| Hypertension | -0.0312 | 0.2941 | ±0.5882 | -0.106 | 0.9154 |  |
| **High cholesterol** | **-0.7481** | 0.2750 | ±0.5500 | **-2.720** | **0.0065** | ** |
| Kidney disease | +0.6963 | 0.4253 | ±0.8506 | +1.637 | 0.1016 |  |
| Circulatory disease | +0.2012 | 0.3676 | ±0.7351 | +0.548 | 0.5840 |  |
| Avg. daily SD (mg/dL) | -0.0058 | 0.0128 | ±0.0256 | -0.456 | 0.6482 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **2100**, R² = **0.2467**, Adj R² = **0.2417**, F-statistic = **48.78** (p = **2.17e-117**), Residual SE = **5.970** on **2085** df, AIC = **13478.7**, BIC = **13563.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.9935** | 1.1531 | ±2.3061 | **+43.357** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.5972** | 0.2823 | ±0.5647 | **+2.115** | **0.0344** | * |
| Education: high school or below (vs college) | +0.5814 | 0.4558 | ±0.9115 | +1.276 | 0.2021 |  |
| **Site: UCSD (vs UAB)** | **+3.1243** | 0.3428 | ±0.6856 | **+9.114** | **7.96e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3529** | 0.3173 | ±0.6346 | **-4.264** | **2.01e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7868** | 0.3672 | ±0.7344 | **-4.866** | **1.14e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8519** | 0.3807 | ±0.7613 | **+4.865** | **1.14e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7150** | 0.3913 | ±0.7826 | **-14.605** | **2.60e-48** | *** |
| **Age (years)** | **-0.0467** | 0.0125 | ±0.0250 | **-3.731** | **1.91e-04** | *** |
| BMI (kg/m2) | -0.0179 | 0.0199 | ±0.0397 | -0.903 | 0.3663 |  |
| Hypertension | -0.0106 | 0.2942 | ±0.5884 | -0.036 | 0.9712 |  |
| **High cholesterol** | **-0.7494** | 0.2746 | ±0.5492 | **-2.729** | **0.0063** | ** |
| Kidney disease | +0.7553 | 0.4261 | ±0.8521 | +1.773 | 0.0763 | . |
| Circulatory disease | +0.2100 | 0.3673 | ±0.7347 | +0.572 | 0.5675 |  |
| CV (%) | -0.0341 | 0.0252 | ±0.0505 | -1.351 | 0.1767 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2100**, R² = **0.2466**, Adj R² = **0.2415**, F-statistic = **48.74** (p = **2.72e-117**), Residual SE = **5.970** on **2085** df, AIC = **13479.1**, BIC = **13563.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.7093** | 1.2304 | ±2.4609 | **+39.587** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6003** | 0.2822 | ±0.5644 | **+2.127** | **0.0334** | * |
| Education: high school or below (vs college) | +0.5787 | 0.4562 | ±0.9124 | +1.269 | 0.2046 |  |
| **Site: UCSD (vs UAB)** | **+3.1328** | 0.3424 | ±0.6847 | **+9.150** | **5.67e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3409** | 0.3166 | ±0.6333 | **-4.235** | **2.29e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7811** | 0.3672 | ±0.7345 | **-4.850** | **1.23e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8557** | 0.3808 | ±0.7616 | **+4.873** | **1.10e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7087** | 0.3912 | ±0.7823 | **-14.594** | **3.06e-48** | *** |
| **Age (years)** | **-0.0469** | 0.0125 | ±0.0251 | **-3.743** | **1.81e-04** | *** |
| BMI (kg/m2) | -0.0180 | 0.0199 | ±0.0398 | -0.906 | 0.3649 |  |
| Hypertension | -0.0145 | 0.2947 | ±0.5894 | -0.049 | 0.9607 |  |
| **High cholesterol** | **-0.7478** | 0.2746 | ±0.5492 | **-2.723** | **0.0065** | ** |
| Kidney disease | +0.7239 | 0.4232 | ±0.8464 | +1.710 | 0.0872 | . |
| Circulatory disease | +0.2085 | 0.3675 | ±0.7351 | +0.567 | 0.5705 |  |
| Mean / SD ratio | +0.1146 | 0.0979 | ±0.1958 | +1.171 | 0.2415 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2411**, F-statistic = **48.64** (p = **4.66e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.2**, BIC = **13565.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1350** | 1.2355 | ±2.4711 | **+39.768** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6114** | 0.2821 | ±0.5642 | **+2.167** | **0.0302** | * |
| Education: high school or below (vs college) | +0.5626 | 0.4563 | ±0.9127 | +1.233 | 0.2177 |  |
| **Site: UCSD (vs UAB)** | **+3.1504** | 0.3418 | ±0.6835 | **+9.218** | **3.01e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3285** | 0.3163 | ±0.6326 | **-4.200** | **2.67e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7799** | 0.3674 | ±0.7349 | **-4.844** | **1.27e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8509** | 0.3808 | ±0.7616 | **+4.861** | **1.17e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7104** | 0.3913 | ±0.7825 | **-14.595** | **3.03e-48** | *** |
| **Age (years)** | **-0.0477** | 0.0126 | ±0.0251 | **-3.796** | **1.47e-04** | *** |
| BMI (kg/m2) | -0.0182 | 0.0199 | ±0.0398 | -0.917 | 0.3591 |  |
| Hypertension | -0.0336 | 0.2947 | ±0.5895 | -0.114 | 0.9092 |  |
| **High cholesterol** | **-0.7517** | 0.2747 | ±0.5494 | **-2.736** | **0.0062** | ** |
| Kidney disease | +0.6873 | 0.4223 | ±0.8446 | +1.627 | 0.1037 |  |
| Circulatory disease | +0.1982 | 0.3676 | ±0.7351 | +0.539 | 0.5897 |  |
| Avg. daily mean/SD | +0.0411 | 0.0842 | ±0.1684 | +0.488 | 0.6259 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2410**, F-statistic = **48.62** (p = **5.17e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.4**, BIC = **13565.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5594** | 1.2129 | ±2.4258 | **+40.861** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6150** | 0.2820 | ±0.5640 | **+2.181** | **0.0292** | * |
| Education: high school or below (vs college) | +0.5548 | 0.4573 | ±0.9147 | +1.213 | 0.2251 |  |
| **Site: UCSD (vs UAB)** | **+3.1532** | 0.3434 | ±0.6868 | **+9.182** | **4.23e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3293** | 0.3193 | ±0.6386 | **-4.163** | **3.14e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7781** | 0.3674 | ±0.7349 | **-4.839** | **1.30e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8497** | 0.3804 | ±0.7608 | **+4.863** | **1.16e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7106** | 0.3908 | ±0.7815 | **-14.614** | **2.29e-48** | *** |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0249 | **-3.888** | **1.01e-04** | *** |
| BMI (kg/m2) | -0.0183 | 0.0199 | ±0.0398 | -0.917 | 0.3590 |  |
| Hypertension | -0.0437 | 0.2938 | ±0.5877 | -0.149 | 0.8818 |  |
| **High cholesterol** | **-0.7539** | 0.2747 | ±0.5494 | **-2.744** | **0.0061** | ** |
| Kidney disease | +0.6691 | 0.4222 | ±0.8445 | +1.585 | 0.1131 |  |
| Circulatory disease | +0.1970 | 0.3675 | ±0.7350 | +0.536 | 0.5919 |  |
| MAG (mg/dL/h) | -0.0028 | 0.0145 | ±0.0290 | -0.192 | 0.8476 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2412**, F-statistic = **48.65** (p = **4.42e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.1**, BIC = **13564.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.6357** | 1.1119 | ±2.2238 | **+44.640** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6098** | 0.2821 | ±0.5641 | **+2.162** | **0.0306** | * |
| Education: high school or below (vs college) | +0.5753 | 0.4579 | ±0.9158 | +1.256 | 0.2090 |  |
| **Site: UCSD (vs UAB)** | **+3.1423** | 0.3433 | ±0.6867 | **+9.153** | **5.55e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3343** | 0.3175 | ±0.6350 | **-4.203** | **2.64e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7799** | 0.3674 | ±0.7348 | **-4.844** | **1.27e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8487** | 0.3806 | ±0.7613 | **+4.857** | **1.19e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7139** | 0.3911 | ±0.7822 | **-14.609** | **2.46e-48** | *** |
| **Age (years)** | **-0.0478** | 0.0125 | ±0.0250 | **-3.817** | **1.35e-04** | *** |
| BMI (kg/m2) | -0.0182 | 0.0199 | ±0.0398 | -0.916 | 0.3594 |  |
| Hypertension | -0.0299 | 0.2940 | ±0.5880 | -0.102 | 0.9189 |  |
| **High cholesterol** | **-0.7472** | 0.2748 | ±0.5497 | **-2.719** | **0.0066** | ** |
| Kidney disease | +0.7042 | 0.4250 | ±0.8499 | +1.657 | 0.0975 | . |
| Circulatory disease | +0.2037 | 0.3674 | ±0.7347 | +0.555 | 0.5792 |  |
| Avg. daily range (mg/dL) | -0.0021 | 0.0034 | ±0.0068 | -0.611 | 0.5411 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **2100**, R² = **0.2463**, Adj R² = **0.2412**, F-statistic = **48.67** (p = **3.91e-117**), Residual SE = **5.971** on **2085** df, AIC = **13479.9**, BIC = **13564.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5325** | 1.0739 | ±2.1479 | **+46.122** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6035** | 0.2822 | ±0.5644 | **+2.139** | **0.0325** | * |
| Education: high school or below (vs college) | +0.5708 | 0.4562 | ±0.9123 | +1.251 | 0.2108 |  |
| **Site: UCSD (vs UAB)** | **+3.1407** | 0.3430 | ±0.6860 | **+9.157** | **5.35e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3383** | 0.3175 | ±0.6350 | **-4.215** | **2.50e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7743** | 0.3671 | ±0.7343 | **-4.833** | **1.35e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8590** | 0.3810 | ±0.7619 | **+4.880** | **1.06e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7051** | 0.3915 | ±0.7829 | **-14.574** | **4.12e-48** | *** |
| **Age (years)** | **-0.0483** | 0.0125 | ±0.0249 | **-3.871** | **1.08e-04** | *** |
| BMI (kg/m2) | -0.0170 | 0.0200 | ±0.0399 | -0.850 | 0.3951 |  |
| Hypertension | -0.0283 | 0.2943 | ±0.5886 | -0.096 | 0.9233 |  |
| **High cholesterol** | **-0.7444** | 0.2748 | ±0.5495 | **-2.709** | **0.0067** | ** |
| Kidney disease | +0.6976 | 0.4216 | ±0.8432 | +1.655 | 0.0980 | . |
| Circulatory disease | +0.2142 | 0.3689 | ±0.7378 | +0.581 | 0.5614 |  |
| SD of daily means (mg/dL) | -0.0166 | 0.0214 | ±0.0429 | -0.774 | 0.4389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2411**, F-statistic = **48.64** (p = **4.65e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.2**, BIC = **13565.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1038** | 1.2958 | ±2.5916 | **+37.894** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6112** | 0.2814 | ±0.5627 | **+2.172** | **0.0298** | * |
| Education: high school or below (vs college) | +0.5727 | 0.4589 | ±0.9177 | +1.248 | 0.2120 |  |
| **Site: UCSD (vs UAB)** | **+3.1437** | 0.3442 | ±0.6884 | **+9.133** | **6.65e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3327** | 0.3176 | ±0.6353 | **-4.196** | **2.72e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7792** | 0.3674 | ±0.7349 | **-4.842** | **1.28e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8482** | 0.3806 | ±0.7613 | **+4.856** | **1.20e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7103** | 0.3911 | ±0.7822 | **-14.600** | **2.81e-48** | *** |
| **Age (years)** | **-0.0481** | 0.0125 | ±0.0250 | **-3.845** | **1.21e-04** | *** |
| BMI (kg/m2) | -0.0176 | 0.0200 | ±0.0401 | -0.880 | 0.3790 |  |
| Hypertension | -0.0351 | 0.2941 | ±0.5881 | -0.120 | 0.9049 |  |
| **High cholesterol** | **-0.7477** | 0.2749 | ±0.5499 | **-2.719** | **0.0065** | ** |
| Kidney disease | +0.6873 | 0.4223 | ±0.8445 | +1.628 | 0.1036 |  |
| Circulatory disease | +0.2026 | 0.3677 | ±0.7354 | +0.551 | 0.5815 |  |
| Time in range 70-180, pooled (%) | +0.0034 | 0.0070 | ±0.0141 | +0.480 | 0.6315 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2411**, F-statistic = **48.63** (p = **4.73e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.3**, BIC = **13565.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1279** | 1.2979 | ±2.5958 | **+37.852** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6119** | 0.2814 | ±0.5628 | **+2.175** | **0.0297** | * |
| Education: high school or below (vs college) | +0.5712 | 0.4589 | ±0.9177 | +1.245 | 0.2132 |  |
| **Site: UCSD (vs UAB)** | **+3.1446** | 0.3443 | ±0.6886 | **+9.133** | **6.67e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3320** | 0.3177 | ±0.6354 | **-4.193** | **2.75e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7786** | 0.3674 | ±0.7348 | **-4.841** | **1.29e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8489** | 0.3806 | ±0.7613 | **+4.857** | **1.19e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7096** | 0.3911 | ±0.7823 | **-14.598** | **2.90e-48** | *** |
| **Age (years)** | **-0.0481** | 0.0125 | ±0.0250 | **-3.845** | **1.20e-04** | *** |
| BMI (kg/m2) | -0.0177 | 0.0201 | ±0.0401 | -0.882 | 0.3779 |  |
| Hypertension | -0.0361 | 0.2940 | ±0.5881 | -0.123 | 0.9024 |  |
| **High cholesterol** | **-0.7480** | 0.2750 | ±0.5500 | **-2.720** | **0.0065** | ** |
| Kidney disease | +0.6858 | 0.4222 | ±0.8445 | +1.624 | 0.1043 |  |
| Circulatory disease | +0.2021 | 0.3677 | ±0.7354 | +0.550 | 0.5825 |  |
| Avg. daily time in range 70-180 (%) | +0.0031 | 0.0070 | ±0.0140 | +0.443 | 0.6574 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.2465**, Adj R² = **0.2414**, F-statistic = **48.71** (p = **3.21e-117**), Residual SE = **5.971** on **2085** df, AIC = **13479.5**, BIC = **13564.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5949** | 1.0751 | ±2.1503 | **+46.129** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6117** | 0.2814 | ±0.5628 | **+2.174** | **0.0297** | * |
| Education: high school or below (vs college) | +0.5210 | 0.4568 | ±0.9136 | +1.140 | 0.2541 |  |
| **Site: UCSD (vs UAB)** | **+3.1240** | 0.3429 | ±0.6857 | **+9.112** | **8.11e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3418** | 0.3156 | ±0.6313 | **-4.251** | **2.13e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7782** | 0.3673 | ±0.7345 | **-4.842** | **1.29e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8444** | 0.3807 | ±0.7613 | **+4.845** | **1.27e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7187** | 0.3913 | ±0.7825 | **-14.616** | **2.22e-48** | *** |
| **Age (years)** | **-0.0493** | 0.0125 | ±0.0249 | **-3.958** | **7.55e-05** | *** |
| BMI (kg/m2) | -0.0177 | 0.0199 | ±0.0399 | -0.886 | 0.3756 |  |
| Hypertension | -0.0426 | 0.2940 | ±0.5881 | -0.145 | 0.8847 |  |
| **High cholesterol** | **-0.7706** | 0.2749 | ±0.5498 | **-2.803** | **0.0051** | ** |
| Kidney disease | +0.6546 | 0.4194 | ±0.8388 | +1.561 | 0.1185 |  |
| Circulatory disease | +0.2177 | 0.3686 | ±0.7372 | +0.591 | 0.5548 |  |
| Any reading < 54 during wear (0/1) | -0.2906 | 0.2931 | ±0.5861 | -0.992 | 0.3213 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.2473**, Adj R² = **0.2422**, F-statistic = **48.92** (p = **1.06e-117**), Residual SE = **5.968** on **2085** df, AIC = **13477.2**, BIC = **13561.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.6020** | 1.0705 | ±2.1409 | **+46.337** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6097** | 0.2809 | ±0.5618 | **+2.170** | **0.0300** | * |
| Education: high school or below (vs college) | +0.5091 | 0.4557 | ±0.9113 | +1.117 | 0.2638 |  |
| **Site: UCSD (vs UAB)** | **+3.0885** | 0.3432 | ±0.6864 | **+8.999** | **2.27e-19** | *** |
| **Site: UW (vs UAB)** | **-1.3795** | 0.3165 | ±0.6330 | **-4.359** | **1.31e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7882** | 0.3672 | ±0.7344 | **-4.870** | **1.12e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8578** | 0.3807 | ±0.7614 | **+4.880** | **1.06e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7091** | 0.3911 | ±0.7823 | **-14.596** | **2.96e-48** | *** |
| **Age (years)** | **-0.0489** | 0.0124 | ±0.0249 | **-3.932** | **8.44e-05** | *** |
| BMI (kg/m2) | -0.0183 | 0.0199 | ±0.0399 | -0.920 | 0.3577 |  |
| Hypertension | -0.0556 | 0.2939 | ±0.5878 | -0.189 | 0.8499 |  |
| **High cholesterol** | **-0.7810** | 0.2753 | ±0.5507 | **-2.836** | **0.0046** | ** |
| Kidney disease | +0.6606 | 0.4190 | ±0.8380 | +1.577 | 0.1149 |  |
| Circulatory disease | +0.2121 | 0.3679 | ±0.7358 | +0.576 | 0.5643 |  |
| **Time < 54 (%)** | **-0.4596** | 0.2117 | ±0.4233 | **-2.171** | **0.0299** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.2475**, Adj R² = **0.2425**, F-statistic = **48.99** (p = **7.41e-118**), Residual SE = **5.967** on **2085** df, AIC = **13476.5**, BIC = **13561.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5560** | 1.0660 | ±2.1321 | **+46.487** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6021** | 0.2810 | ±0.5620 | **+2.143** | **0.0321** | * |
| Education: high school or below (vs college) | +0.5085 | 0.4550 | ±0.9100 | +1.118 | 0.2637 |  |
| **Site: UCSD (vs UAB)** | **+3.0922** | 0.3426 | ±0.6851 | **+9.027** | **1.77e-19** | *** |
| **Site: UW (vs UAB)** | **-1.3886** | 0.3169 | ±0.6339 | **-4.381** | **1.18e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7920** | 0.3671 | ±0.7342 | **-4.882** | **1.05e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8581** | 0.3809 | ±0.7618 | **+4.878** | **1.07e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7029** | 0.3910 | ±0.7819 | **-14.587** | **3.40e-48** | *** |
| **Age (years)** | **-0.0483** | 0.0124 | ±0.0249 | **-3.880** | **1.05e-04** | *** |
| BMI (kg/m2) | -0.0183 | 0.0199 | ±0.0397 | -0.921 | 0.3569 |  |
| Hypertension | -0.0589 | 0.2938 | ±0.5876 | -0.200 | 0.8412 |  |
| **High cholesterol** | **-0.7806** | 0.2751 | ±0.5502 | **-2.837** | **0.0045** | ** |
| Kidney disease | +0.6659 | 0.4192 | ±0.8384 | +1.588 | 0.1122 |  |
| Circulatory disease | +0.2137 | 0.3673 | ±0.7345 | +0.582 | 0.5606 |  |
| **Avg. daily time < 54 (%)** | **-0.6104** | 0.3041 | ±0.6081 | **-2.007** | **0.0447** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.2465**, Adj R² = **0.2415**, F-statistic = **48.73** (p = **2.86e-117**), Residual SE = **5.971** on **2085** df, AIC = **13479.2**, BIC = **13564.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5344** | 1.0721 | ±2.1442 | **+46.204** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6040** | 0.2813 | ±0.5625 | **+2.147** | **0.0318** | * |
| Education: high school or below (vs college) | +0.5298 | 0.4551 | ±0.9103 | +1.164 | 0.2444 |  |
| **Site: UCSD (vs UAB)** | **+3.1280** | 0.3432 | ±0.6864 | **+9.114** | **7.95e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3524** | 0.3163 | ±0.6327 | **-4.275** | **1.91e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7831** | 0.3673 | ±0.7347 | **-4.854** | **1.21e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8496** | 0.3806 | ±0.7612 | **+4.860** | **1.17e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7051** | 0.3912 | ±0.7824 | **-14.584** | **3.57e-48** | *** |
| **Age (years)** | **-0.0485** | 0.0125 | ±0.0249 | **-3.896** | **9.77e-05** | *** |
| BMI (kg/m2) | -0.0180 | 0.0199 | ±0.0399 | -0.903 | 0.3665 |  |
| Hypertension | -0.0540 | 0.2939 | ±0.5878 | -0.184 | 0.8542 |  |
| **High cholesterol** | **-0.7653** | 0.2753 | ±0.5505 | **-2.781** | **0.0054** | ** |
| Kidney disease | +0.6626 | 0.4195 | ±0.8390 | +1.579 | 0.1142 |  |
| Circulatory disease | +0.2016 | 0.3678 | ±0.7356 | +0.548 | 0.5835 |  |
| Time 54-69, pooled (%) | -0.1018 | 0.0923 | ±0.1847 | -1.102 | 0.2703 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2100**, R² = **0.2466**, Adj R² = **0.2415**, F-statistic = **48.75** (p = **2.64e-117**), Residual SE = **5.970** on **2085** df, AIC = **13479.1**, BIC = **13563.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5173** | 1.0695 | ±2.1390 | **+46.300** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6014** | 0.2814 | ±0.5627 | **+2.138** | **0.0325** | * |
| Education: high school or below (vs college) | +0.5300 | 0.4550 | ±0.9099 | +1.165 | 0.2440 |  |
| **Site: UCSD (vs UAB)** | **+3.1312** | 0.3428 | ±0.6856 | **+9.135** | **6.55e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3545** | 0.3164 | ±0.6328 | **-4.281** | **1.86e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7831** | 0.3674 | ±0.7347 | **-4.854** | **1.21e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8489** | 0.3806 | ±0.7612 | **+4.858** | **1.19e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7024** | 0.3911 | ±0.7822 | **-14.580** | **3.75e-48** | *** |
| **Age (years)** | **-0.0483** | 0.0124 | ±0.0249 | **-3.879** | **1.05e-04** | *** |
| BMI (kg/m2) | -0.0180 | 0.0199 | ±0.0398 | -0.902 | 0.3672 |  |
| Hypertension | -0.0547 | 0.2938 | ±0.5876 | -0.186 | 0.8524 |  |
| **High cholesterol** | **-0.7647** | 0.2751 | ±0.5503 | **-2.779** | **0.0054** | ** |
| Kidney disease | +0.6619 | 0.4194 | ±0.8388 | +1.578 | 0.1145 |  |
| Circulatory disease | +0.2005 | 0.3677 | ±0.7355 | +0.545 | 0.5856 |  |
| Avg. daily time 54-69 (%) | -0.1070 | 0.0908 | ±0.1816 | -1.179 | 0.2384 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **2100**, R² = **0.2468**, Adj R² = **0.2418**, F-statistic = **48.80** (p = **1.95e-117**), Residual SE = **5.969** on **2085** df, AIC = **13478.4**, BIC = **13563.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5734** | 1.0725 | ±2.1449 | **+46.224** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6017** | 0.2811 | ±0.5623 | **+2.140** | **0.0323** | * |
| Education: high school or below (vs college) | +0.5199 | 0.4552 | ±0.9104 | +1.142 | 0.2534 |  |
| **Site: UCSD (vs UAB)** | **+3.1111** | 0.3437 | ±0.6873 | **+9.053** | **1.40e-19** | *** |
| **Site: UW (vs UAB)** | **-1.3664** | 0.3164 | ±0.6329 | **-4.318** | **1.57e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7859** | 0.3673 | ±0.7347 | **-4.862** | **1.16e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8508** | 0.3806 | ±0.7612 | **+4.863** | **1.16e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7051** | 0.3912 | ±0.7825 | **-14.583** | **3.63e-48** | *** |
| **Age (years)** | **-0.0486** | 0.0124 | ±0.0249 | **-3.908** | **9.31e-05** | *** |
| BMI (kg/m2) | -0.0180 | 0.0199 | ±0.0399 | -0.901 | 0.3674 |  |
| Hypertension | -0.0567 | 0.2939 | ±0.5879 | -0.193 | 0.8471 |  |
| **High cholesterol** | **-0.7720** | 0.2754 | ±0.5508 | **-2.803** | **0.0051** | ** |
| Kidney disease | +0.6623 | 0.4194 | ±0.8389 | +1.579 | 0.1143 |  |
| Circulatory disease | +0.2054 | 0.3679 | ±0.7357 | +0.558 | 0.5766 |  |
| Time < 70 (%) | -0.1051 | 0.0746 | ±0.1492 | -1.409 | 0.1588 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **2100**, R² = **0.2469**, Adj R² = **0.2418**, F-statistic = **48.82** (p = **1.80e-117**), Residual SE = **5.969** on **2085** df, AIC = **13478.3**, BIC = **13563.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5403** | 1.0687 | ±2.1374 | **+46.355** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.5979** | 0.2813 | ±0.5625 | **+2.126** | **0.0335** | * |
| Education: high school or below (vs college) | +0.5218 | 0.4549 | ±0.9098 | +1.147 | 0.2513 |  |
| **Site: UCSD (vs UAB)** | **+3.1183** | 0.3430 | ±0.6860 | **+9.092** | **9.75e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3677** | 0.3165 | ±0.6330 | **-4.321** | **1.55e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7860** | 0.3673 | ±0.7347 | **-4.862** | **1.16e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8498** | 0.3806 | ±0.7612 | **+4.861** | **1.17e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7011** | 0.3911 | ±0.7822 | **-14.578** | **3.89e-48** | *** |
| **Age (years)** | **-0.0483** | 0.0124 | ±0.0249 | **-3.879** | **1.05e-04** | *** |
| BMI (kg/m2) | -0.0179 | 0.0199 | ±0.0398 | -0.900 | 0.3679 |  |
| Hypertension | -0.0575 | 0.2938 | ±0.5876 | -0.196 | 0.8448 |  |
| **High cholesterol** | **-0.7701** | 0.2752 | ±0.5504 | **-2.798** | **0.0051** | ** |
| Kidney disease | +0.6626 | 0.4194 | ±0.8388 | +1.580 | 0.1141 |  |
| Circulatory disease | +0.2038 | 0.3676 | ±0.7353 | +0.554 | 0.5792 |  |
| Avg. daily time < 70 (%) | -0.1111 | 0.0755 | ±0.1510 | -1.471 | 0.1413 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2410**, F-statistic = **48.61** (p = **5.26e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.5**, BIC = **13565.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4065** | 1.6600 | ±3.3200 | **+29.763** | **1.18e-194** | *** |
| **Education: graduate level (vs college)** | **+0.6175** | 0.2812 | ±0.5624 | **+2.196** | **0.0281** | * |
| Education: high school or below (vs college) | +0.5510 | 0.4594 | ±0.9189 | +1.199 | 0.2305 |  |
| **Site: UCSD (vs UAB)** | **+3.1571** | 0.3432 | ±0.6864 | **+9.199** | **3.63e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3234** | 0.3181 | ±0.6361 | **-4.161** | **3.17e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7773** | 0.3676 | ±0.7353 | **-4.834** | **1.34e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8516** | 0.3808 | ±0.7617 | **+4.862** | **1.16e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7087** | 0.3911 | ±0.7821 | **-14.598** | **2.91e-48** | *** |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0249 | **-3.882** | **1.04e-04** | *** |
| BMI (kg/m2) | -0.0184 | 0.0200 | ±0.0400 | -0.919 | 0.3581 |  |
| Hypertension | -0.0447 | 0.2939 | ±0.5878 | -0.152 | 0.8790 |  |
| **High cholesterol** | **-0.7534** | 0.2747 | ±0.5494 | **-2.742** | **0.0061** | ** |
| Kidney disease | +0.6630 | 0.4207 | ±0.8415 | +1.576 | 0.1151 |  |
| Circulatory disease | +0.1967 | 0.3675 | ±0.7351 | +0.535 | 0.5926 |  |
| Time 54-250, pooled (%) | +0.0004 | 0.0126 | ±0.0251 | +0.031 | 0.9753 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2410**, F-statistic = **48.61** (p = **5.26e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.5**, BIC = **13565.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4322** | 1.6953 | ±3.3906 | **+29.159** | **6.52e-187** | *** |
| **Education: graduate level (vs college)** | **+0.6178** | 0.2812 | ±0.5625 | **+2.197** | **0.0280** | * |
| Education: high school or below (vs college) | +0.5500 | 0.4596 | ±0.9192 | +1.197 | 0.2314 |  |
| **Site: UCSD (vs UAB)** | **+3.1576** | 0.3432 | ±0.6864 | **+9.200** | **3.58e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3229** | 0.3180 | ±0.6360 | **-4.160** | **3.19e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7771** | 0.3676 | ±0.7352 | **-4.835** | **1.33e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8520** | 0.3808 | ±0.7615 | **+4.864** | **1.15e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7086** | 0.3911 | ±0.7822 | **-14.597** | **2.94e-48** | *** |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0249 | **-3.881** | **1.04e-04** | *** |
| BMI (kg/m2) | -0.0184 | 0.0200 | ±0.0400 | -0.920 | 0.3578 |  |
| Hypertension | -0.0451 | 0.2939 | ±0.5877 | -0.153 | 0.8781 |  |
| **High cholesterol** | **-0.7535** | 0.2747 | ±0.5495 | **-2.742** | **0.0061** | ** |
| Kidney disease | +0.6623 | 0.4209 | ±0.8417 | +1.574 | 0.1156 |  |
| Circulatory disease | +0.1964 | 0.3675 | ±0.7351 | +0.534 | 0.5931 |  |
| Avg. daily time 54-250 (%) | +0.0001 | 0.0129 | ±0.0258 | +0.010 | 0.9923 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2412**, F-statistic = **48.65** (p = **4.34e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.1**, BIC = **13564.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4149** | 1.0687 | ±2.1375 | **+46.236** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6141** | 0.2813 | ±0.5626 | **+2.183** | **0.0290** | * |
| Education: high school or below (vs college) | +0.5732 | 0.4566 | ±0.9132 | +1.255 | 0.2094 |  |
| **Site: UCSD (vs UAB)** | **+3.1446** | 0.3429 | ±0.6858 | **+9.171** | **4.69e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3275** | 0.3164 | ±0.6327 | **-4.196** | **2.71e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7782** | 0.3672 | ±0.7344 | **-4.842** | **1.28e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8547** | 0.3808 | ±0.7616 | **+4.871** | **1.11e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7103** | 0.3911 | ±0.7822 | **-14.600** | **2.79e-48** | *** |
| **Age (years)** | **-0.0476** | 0.0125 | ±0.0251 | **-3.803** | **1.43e-04** | *** |
| BMI (kg/m2) | -0.0174 | 0.0200 | ±0.0400 | -0.869 | 0.3848 |  |
| Hypertension | -0.0330 | 0.2942 | ±0.5883 | -0.112 | 0.9108 |  |
| **High cholesterol** | **-0.7431** | 0.2752 | ±0.5504 | **-2.700** | **0.0069** | ** |
| Kidney disease | +0.6940 | 0.4217 | ±0.8435 | +1.646 | 0.0999 | . |
| Circulatory disease | +0.2016 | 0.3677 | ±0.7354 | +0.548 | 0.5835 |  |
| Time 181-250, pooled (%) | -0.0066 | 0.0108 | ±0.0217 | -0.609 | 0.5423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2411**, F-statistic = **48.64** (p = **4.48e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.1**, BIC = **13564.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4180** | 1.0685 | ±2.1370 | **+46.249** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6147** | 0.2813 | ±0.5626 | **+2.186** | **0.0289** | * |
| Education: high school or below (vs college) | +0.5717 | 0.4565 | ±0.9130 | +1.252 | 0.2105 |  |
| **Site: UCSD (vs UAB)** | **+3.1449** | 0.3431 | ±0.6862 | **+9.166** | **4.89e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3277** | 0.3165 | ±0.6329 | **-4.196** | **2.72e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7778** | 0.3672 | ±0.7344 | **-4.841** | **1.29e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8545** | 0.3808 | ±0.7616 | **+4.870** | **1.11e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7097** | 0.3911 | ±0.7822 | **-14.598** | **2.88e-48** | *** |
| **Age (years)** | **-0.0477** | 0.0125 | ±0.0250 | **-3.813** | **1.37e-04** | *** |
| BMI (kg/m2) | -0.0175 | 0.0200 | ±0.0400 | -0.873 | 0.3828 |  |
| Hypertension | -0.0340 | 0.2941 | ±0.5883 | -0.116 | 0.9080 |  |
| **High cholesterol** | **-0.7439** | 0.2752 | ±0.5505 | **-2.703** | **0.0069** | ** |
| Kidney disease | +0.6914 | 0.4216 | ±0.8432 | +1.640 | 0.1010 |  |
| Circulatory disease | +0.2009 | 0.3678 | ±0.7355 | +0.546 | 0.5849 |  |
| Avg. daily time 181-250 (%) | -0.0060 | 0.0107 | ±0.0213 | -0.559 | 0.5758 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2411**, F-statistic = **48.63** (p = **4.92e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.3**, BIC = **13565.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4391** | 1.0682 | ±2.1363 | **+46.285** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6134** | 0.2813 | ±0.5627 | **+2.180** | **0.0292** | * |
| Education: high school or below (vs college) | +0.5671 | 0.4589 | ±0.9177 | +1.236 | 0.2165 |  |
| **Site: UCSD (vs UAB)** | **+3.1486** | 0.3437 | ±0.6873 | **+9.162** | **5.10e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3290** | 0.3174 | ±0.6348 | **-4.187** | **2.83e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7784** | 0.3674 | ±0.7349 | **-4.840** | **1.30e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8493** | 0.3806 | ±0.7613 | **+4.859** | **1.18e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7099** | 0.3911 | ±0.7822 | **-14.600** | **2.81e-48** | *** |
| **Age (years)** | **-0.0482** | 0.0125 | ±0.0250 | **-3.851** | **1.17e-04** | *** |
| BMI (kg/m2) | -0.0179 | 0.0201 | ±0.0401 | -0.890 | 0.3733 |  |
| Hypertension | -0.0376 | 0.2941 | ±0.5882 | -0.128 | 0.8982 |  |
| **High cholesterol** | **-0.7488** | 0.2750 | ±0.5501 | **-2.723** | **0.0065** | ** |
| Kidney disease | +0.6804 | 0.4220 | ±0.8440 | +1.612 | 0.1069 |  |
| Circulatory disease | +0.2007 | 0.3678 | ±0.7355 | +0.546 | 0.5853 |  |
| Time > 180 (%) | -0.0025 | 0.0070 | ±0.0139 | -0.352 | 0.7249 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2411**, F-statistic = **48.62** (p = **4.99e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.4**, BIC = **13565.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4388** | 1.0683 | ±2.1366 | **+46.278** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6141** | 0.2813 | ±0.5627 | **+2.183** | **0.0291** | * |
| Education: high school or below (vs college) | +0.5654 | 0.4588 | ±0.9177 | +1.232 | 0.2179 |  |
| **Site: UCSD (vs UAB)** | **+3.1493** | 0.3438 | ±0.6877 | **+9.159** | **5.24e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3284** | 0.3174 | ±0.6349 | **-4.185** | **2.86e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7780** | 0.3674 | ±0.7348 | **-4.839** | **1.30e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8499** | 0.3806 | ±0.7612 | **+4.860** | **1.17e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7095** | 0.3911 | ±0.7822 | **-14.598** | **2.87e-48** | *** |
| **Age (years)** | **-0.0482** | 0.0125 | ±0.0250 | **-3.853** | **1.16e-04** | *** |
| BMI (kg/m2) | -0.0179 | 0.0201 | ±0.0401 | -0.893 | 0.3721 |  |
| Hypertension | -0.0385 | 0.2940 | ±0.5881 | -0.131 | 0.8958 |  |
| **High cholesterol** | **-0.7493** | 0.2751 | ±0.5502 | **-2.724** | **0.0065** | ** |
| Kidney disease | +0.6788 | 0.4220 | ±0.8440 | +1.608 | 0.1077 |  |
| Circulatory disease | +0.2003 | 0.3678 | ±0.7356 | +0.545 | 0.5861 |  |
| Avg. daily time > 180 (%) | -0.0022 | 0.0070 | ±0.0139 | -0.315 | 0.7528 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.2462**, Adj R² = **0.2412**, F-statistic = **48.65** (p = **4.28e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.0**, BIC = **13564.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4319** | 1.0680 | ±2.1360 | **+46.285** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6070** | 0.2814 | ±0.5629 | **+2.157** | **0.0310** | * |
| Education: high school or below (vs college) | +0.5783 | 0.4586 | ±0.9172 | +1.261 | 0.2073 |  |
| **Site: UCSD (vs UAB)** | **+3.1414** | 0.3437 | ±0.6873 | **+9.141** | **6.20e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3324** | 0.3171 | ±0.6343 | **-4.201** | **2.65e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7757** | 0.3672 | ±0.7343 | **-4.836** | **1.32e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8466** | 0.3806 | ±0.7613 | **+4.851** | **1.23e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7070** | 0.3912 | ±0.7825 | **-14.587** | **3.39e-48** | *** |
| **Age (years)** | **-0.0483** | 0.0125 | ±0.0250 | **-3.869** | **1.09e-04** | *** |
| BMI (kg/m2) | -0.0170 | 0.0201 | ±0.0403 | -0.844 | 0.3985 |  |
| Hypertension | -0.0363 | 0.2940 | ±0.5880 | -0.123 | 0.9018 |  |
| **High cholesterol** | **-0.7466** | 0.2751 | ±0.5501 | **-2.714** | **0.0066** | ** |
| Kidney disease | +0.6868 | 0.4212 | ±0.8423 | +1.631 | 0.1030 |  |
| Circulatory disease | +0.2029 | 0.3675 | ±0.7350 | +0.552 | 0.5809 |  |
| Nocturnal time > 180 (%) | -0.0043 | 0.0069 | ±0.0138 | -0.628 | 0.5303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.2470**, Adj R² = **0.2419**, F-statistic = **48.85** (p = **1.53e-117**), Residual SE = **5.969** on **2085** df, AIC = **13477.9**, BIC = **13562.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4935** | 1.0660 | ±2.1320 | **+46.430** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.5927** | 0.2813 | ±0.5627 | **+2.107** | **0.0351** | * |
| Education: high school or below (vs college) | +0.5852 | 0.4572 | ±0.9143 | +1.280 | 0.2005 |  |
| **Site: UCSD (vs UAB)** | **+3.1351** | 0.3413 | ±0.6826 | **+9.186** | **4.10e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3312** | 0.3160 | ±0.6321 | **-4.212** | **2.53e-05** | *** |
| **Season: spring (vs autumn)** | **-1.8011** | 0.3668 | ±0.7336 | **-4.910** | **9.10e-07** | *** |
| **Season: summer (vs autumn)** | **+1.8485** | 0.3803 | ±0.7607 | **+4.860** | **1.17e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7336** | 0.3909 | ±0.7818 | **-14.667** | **1.04e-48** | *** |
| **Age (years)** | **-0.0465** | 0.0125 | ±0.0250 | **-3.716** | **2.03e-04** | *** |
| BMI (kg/m2) | -0.0187 | 0.0198 | ±0.0397 | -0.942 | 0.3461 |  |
| Hypertension | -0.0055 | 0.2937 | ±0.5874 | -0.019 | 0.9852 |  |
| **High cholesterol** | **-0.7273** | 0.2749 | ±0.5497 | **-2.646** | **0.0081** | ** |
| Kidney disease | +0.7278 | 0.4219 | ±0.8438 | +1.725 | 0.0845 | . |
| Circulatory disease | +0.1968 | 0.3675 | ±0.7349 | +0.536 | 0.5923 |  |
| Any reading > 250 during wear (0/1) | -0.4405 | 0.2793 | ±0.5587 | -1.577 | 0.1148 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2410**, F-statistic = **48.61** (p = **5.25e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.5**, BIC = **13565.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4429** | 1.0671 | ±2.1343 | **+46.332** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6188** | 0.2812 | ±0.5624 | **+2.200** | **0.0278** | * |
| Education: high school or below (vs college) | +0.5473 | 0.4595 | ±0.9191 | +1.191 | 0.2337 |  |
| **Site: UCSD (vs UAB)** | **+3.1590** | 0.3430 | ±0.6860 | **+9.210** | **3.27e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3215** | 0.3179 | ±0.6359 | **-4.156** | **3.23e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7769** | 0.3676 | ±0.7353 | **-4.833** | **1.34e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8532** | 0.3809 | ±0.7617 | **+4.866** | **1.14e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7084** | 0.3911 | ±0.7821 | **-14.597** | **2.92e-48** | *** |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0249 | **-3.880** | **1.04e-04** | *** |
| BMI (kg/m2) | -0.0184 | 0.0200 | ±0.0400 | -0.923 | 0.3563 |  |
| Hypertension | -0.0460 | 0.2939 | ±0.5878 | -0.157 | 0.8756 |  |
| **High cholesterol** | **-0.7537** | 0.2747 | ±0.5495 | **-2.743** | **0.0061** | ** |
| Kidney disease | +0.6603 | 0.4206 | ±0.8413 | +1.570 | 0.1165 |  |
| Circulatory disease | +0.1956 | 0.3676 | ±0.7352 | +0.532 | 0.5946 |  |
| Time > 250 (%) | +0.0007 | 0.0125 | ±0.0251 | +0.052 | 0.9586 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.2461**, Adj R² = **0.2410**, F-statistic = **48.61** (p = **5.25e-117**), Residual SE = **5.972** on **2085** df, AIC = **13480.5**, BIC = **13565.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4428** | 1.0671 | ±2.1343 | **+46.332** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6190** | 0.2812 | ±0.5624 | **+2.201** | **0.0277** | * |
| Education: high school or below (vs college) | +0.5466 | 0.4597 | ±0.9193 | +1.189 | 0.2344 |  |
| **Site: UCSD (vs UAB)** | **+3.1594** | 0.3431 | ±0.6861 | **+9.209** | **3.28e-20** | *** |
| **Site: UW (vs UAB)** | **-1.3211** | 0.3179 | ±0.6358 | **-4.156** | **3.24e-05** | *** |
| **Season: spring (vs autumn)** | **-1.7769** | 0.3676 | ±0.7352 | **-4.834** | **1.34e-06** | *** |
| **Season: summer (vs autumn)** | **+1.8534** | 0.3808 | ±0.7616 | **+4.867** | **1.13e-06** | *** |
| **Season: winter (vs autumn)** | **-5.7084** | 0.3911 | ±0.7821 | **-14.597** | **2.93e-48** | *** |
| **Age (years)** | **-0.0484** | 0.0125 | ±0.0249 | **-3.880** | **1.04e-04** | *** |
| BMI (kg/m2) | -0.0185 | 0.0200 | ±0.0400 | -0.923 | 0.3560 |  |
| Hypertension | -0.0462 | 0.2939 | ±0.5877 | -0.157 | 0.8750 |  |
| **High cholesterol** | **-0.7538** | 0.2748 | ±0.5495 | **-2.743** | **0.0061** | ** |
| Kidney disease | +0.6596 | 0.4208 | ±0.8416 | +1.568 | 0.1170 |  |
| Circulatory disease | +0.1954 | 0.3676 | ±0.7352 | +0.532 | 0.5950 |  |
| Avg. daily time > 250 (%) | +0.0009 | 0.0129 | ±0.0258 | +0.067 | 0.9469 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 2,100; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0430**, F-statistic = **8.26** (p = **1.76e-16**), Residual SE = **16.020** on **2086** df, AIC = **17623.6**, BIC = **17702.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.2419** | 3.2063 | ±6.4126 | **+39.061** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6093** | 0.7264 | ±1.4529 | **-2.215** | **0.0267** | * |
| **Education: high school or below (vs college)** | **+5.0469** | 1.3740 | ±2.7481 | **+3.673** | **2.40e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1622** | 0.9550 | ±1.9099 | **+2.264** | **0.0236** | * |
| Site: UW (vs UAB) | -0.9890 | 0.8558 | ±1.7117 | -1.156 | 0.2479 |  |
| **Season: spring (vs autumn)** | **+2.7791** | 0.9194 | ±1.8387 | **+3.023** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9774 | 1.0279 | ±2.0558 | +1.924 | 0.0544 | . |
| **Season: winter (vs autumn)** | **+4.2719** | 1.0344 | ±2.0687 | **+4.130** | **3.63e-05** | *** |
| **Age (years)** | **-0.1118** | 0.0356 | ±0.0713 | **-3.137** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1778** | 0.0541 | ±0.1083 | **+3.284** | **0.0010** | ** |
| Hypertension | +1.0969 | 0.7963 | ±1.5926 | +1.377 | 0.1684 |  |
| High cholesterol | -0.0469 | 0.7479 | ±1.4958 | -0.063 | 0.9500 |  |
| Kidney disease | -1.5921 | 1.1144 | ±2.2287 | -1.429 | 0.1531 |  |
| Circulatory disease | +0.1221 | 1.0355 | ±2.0711 | +0.118 | 0.9061 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **2100**, R² = **0.0499**, Adj R² = **0.0435**, F-statistic = **7.82** (p = **2.17e-16**), Residual SE = **16.016** on **2085** df, AIC = **17623.7**, BIC = **17708.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.7616** | 3.8103 | ±7.6206 | **+33.531** | **1.72e-246** | *** |
| **Education: graduate level (vs college)** | **-1.6673** | 0.7221 | ±1.4443 | **-2.309** | **0.0209** | * |
| **Education: high school or below (vs college)** | **+5.2497** | 1.3811 | ±2.7621 | **+3.801** | **1.44e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1089** | 0.9543 | ±1.9087 | **+2.210** | **0.0271** | * |
| Site: UW (vs UAB) | -1.0538 | 0.8530 | ±1.7059 | -1.235 | 0.2167 |  |
| **Season: spring (vs autumn)** | **+2.7118** | 0.9214 | ±1.8428 | **+2.943** | **0.0032** | ** |
| Season: summer (vs autumn) | +1.9507 | 1.0288 | ±2.0576 | +1.896 | 0.0579 | . |
| **Season: winter (vs autumn)** | **+4.2391** | 1.0382 | ±2.0765 | **+4.083** | **4.44e-05** | *** |
| **Age (years)** | **-0.1091** | 0.0358 | ±0.0716 | **-3.047** | **0.0023** | ** |
| **BMI (kg/m2)** | **+0.1866** | 0.0542 | ±0.1085 | **+3.439** | **5.83e-04** | *** |
| Hypertension | +1.2006 | 0.8069 | ±1.6137 | +1.488 | 0.1368 |  |
| High cholesterol | +0.0441 | 0.7539 | ±1.5078 | +0.058 | 0.9534 |  |
| Kidney disease | -1.5040 | 1.1098 | ±2.2196 | -1.355 | 0.1754 |  |
| Circulatory disease | +0.1669 | 1.0354 | ±2.0707 | +0.161 | 0.8719 |  |
| HbA1c (%) | -0.4903 | 0.4122 | ±0.8244 | -1.190 | 0.2342 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **2100**, R² = **0.0495**, Adj R² = **0.0431**, F-statistic = **7.75** (p = **3.15e-16**), Residual SE = **16.020** on **2085** df, AIC = **17624.5**, BIC = **17709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.4837** | 3.5747 | ±7.1494 | **+35.383** | **3.12e-274** | *** |
| **Education: graduate level (vs college)** | **-1.6354** | 0.7238 | ±1.4475 | **-2.260** | **0.0239** | * |
| **Education: high school or below (vs college)** | **+5.1856** | 1.3791 | ±2.7581 | **+3.760** | **1.70e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1061** | 0.9588 | ±1.9177 | **+2.197** | **0.0281** | * |
| Site: UW (vs UAB) | -1.0197 | 0.8553 | ±1.7105 | -1.192 | 0.2332 |  |
| **Season: spring (vs autumn)** | **+2.7692** | 0.9203 | ±1.8407 | **+3.009** | **0.0026** | ** |
| Season: summer (vs autumn) | +1.9561 | 1.0296 | ±2.0592 | +1.900 | 0.0575 | . |
| **Season: winter (vs autumn)** | **+4.2525** | 1.0381 | ±2.0761 | **+4.097** | **4.19e-05** | *** |
| **Age (years)** | **-0.1100** | 0.0357 | ±0.0714 | **-3.084** | **0.0020** | ** |
| **BMI (kg/m2)** | **+0.1823** | 0.0538 | ±0.1077 | **+3.385** | **7.11e-04** | *** |
| Hypertension | +1.1754 | 0.8088 | ±1.6176 | +1.453 | 0.1461 |  |
| High cholesterol | -0.0012 | 0.7527 | ±1.5055 | -0.002 | 0.9987 |  |
| Kidney disease | -1.4654 | 1.1164 | ±2.2327 | -1.313 | 0.1893 |  |
| Circulatory disease | +0.1556 | 1.0352 | ±2.0703 | +0.150 | 0.8805 |  |
| Mean glucose (mg/dL) | -0.0114 | 0.0125 | ±0.0250 | -0.910 | 0.3629 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **2100**, R² = **0.0495**, Adj R² = **0.0431**, F-statistic = **7.75** (p = **3.15e-16**), Residual SE = **16.020** on **2085** df, AIC = **17624.5**, BIC = **17709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.0563** | 4.6099 | ±9.2199 | **+27.778** | **7.93e-170** | *** |
| **Education: graduate level (vs college)** | **-1.6354** | 0.7238 | ±1.4475 | **-2.260** | **0.0239** | * |
| **Education: high school or below (vs college)** | **+5.1856** | 1.3791 | ±2.7581 | **+3.760** | **1.70e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1061** | 0.9588 | ±1.9177 | **+2.197** | **0.0281** | * |
| Site: UW (vs UAB) | -1.0197 | 0.8553 | ±1.7105 | -1.192 | 0.2332 |  |
| **Season: spring (vs autumn)** | **+2.7692** | 0.9203 | ±1.8407 | **+3.009** | **0.0026** | ** |
| Season: summer (vs autumn) | +1.9561 | 1.0296 | ±2.0592 | +1.900 | 0.0575 | . |
| **Season: winter (vs autumn)** | **+4.2525** | 1.0381 | ±2.0761 | **+4.097** | **4.19e-05** | *** |
| **Age (years)** | **-0.1100** | 0.0357 | ±0.0714 | **-3.084** | **0.0020** | ** |
| **BMI (kg/m2)** | **+0.1823** | 0.0538 | ±0.1077 | **+3.385** | **7.11e-04** | *** |
| Hypertension | +1.1754 | 0.8088 | ±1.6176 | +1.453 | 0.1461 |  |
| High cholesterol | -0.0012 | 0.7527 | ±1.5055 | -0.002 | 0.9987 |  |
| Kidney disease | -1.4654 | 1.1164 | ±2.2327 | -1.313 | 0.1893 |  |
| Circulatory disease | +0.1556 | 1.0352 | ±2.0703 | +0.150 | 0.8805 |  |
| GMI (%) | -0.4751 | 0.5222 | ±1.0443 | -0.910 | 0.3629 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **2100**, R² = **0.0497**, Adj R² = **0.0433**, F-statistic = **7.78** (p = **2.66e-16**), Residual SE = **16.018** on **2085** df, AIC = **17624.1**, BIC = **17708.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.6730** | 3.6717 | ±7.3435 | **+34.500** | **8.15e-261** | *** |
| **Education: graduate level (vs college)** | **-1.6439** | 0.7238 | ±1.4477 | **-2.271** | **0.0231** | * |
| **Education: high school or below (vs college)** | **+5.1996** | 1.3706 | ±2.7411 | **+3.794** | **1.48e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1135** | 0.9581 | ±1.9161 | **+2.206** | **0.0274** | * |
| Site: UW (vs UAB) | -1.0103 | 0.8553 | ±1.7106 | -1.181 | 0.2375 |  |
| **Season: spring (vs autumn)** | **+2.7879** | 0.9195 | ±1.8390 | **+3.032** | **0.0024** | ** |
| Season: summer (vs autumn) | +1.9535 | 1.0294 | ±2.0588 | +1.898 | 0.0577 | . |
| **Season: winter (vs autumn)** | **+4.2691** | 1.0344 | ±2.0687 | **+4.127** | **3.67e-05** | *** |
| **Age (years)** | **-0.1117** | 0.0357 | ±0.0714 | **-3.126** | **0.0018** | ** |
| **BMI (kg/m2)** | **+0.1859** | 0.0537 | ±0.1074 | **+3.462** | **5.37e-04** | *** |
| Hypertension | +1.1700 | 0.8080 | ±1.6160 | +1.448 | 0.1476 |  |
| High cholesterol | +0.0094 | 0.7555 | ±1.5110 | +0.012 | 0.9901 |  |
| Kidney disease | -1.4933 | 1.1165 | ±2.2329 | -1.338 | 0.1810 |  |
| Circulatory disease | +0.1522 | 1.0345 | ±2.0689 | +0.147 | 0.8830 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0132 | 0.0137 | ±0.0274 | -0.966 | 0.3341 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.67** (p = **5.13e-16**), Residual SE = **16.024** on **2085** df, AIC = **17625.6**, BIC = **17710.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3356** | 3.2433 | ±6.4867 | **+38.644** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6168** | 0.7234 | ±1.4468 | **-2.235** | **0.0254** | * |
| **Education: high school or below (vs college)** | **+5.0673** | 1.3758 | ±2.7517 | **+3.683** | **2.30e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1500** | 0.9622 | ±1.9244 | **+2.235** | **0.0254** | * |
| Site: UW (vs UAB) | -0.9989 | 0.8552 | ±1.7104 | -1.168 | 0.2428 |  |
| **Season: spring (vs autumn)** | **+2.7767** | 0.9198 | ±1.8396 | **+3.019** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9747 | 1.0288 | ±2.0577 | +1.919 | 0.0549 | . |
| **Season: winter (vs autumn)** | **+4.2687** | 1.0376 | ±2.0753 | **+4.114** | **3.89e-05** | *** |
| **Age (years)** | **-0.1113** | 0.0360 | ±0.0721 | **-3.089** | **0.0020** | ** |
| **BMI (kg/m2)** | **+0.1783** | 0.0542 | ±0.1084 | **+3.291** | **9.97e-04** | *** |
| Hypertension | +1.1117 | 0.8054 | ±1.6108 | +1.380 | 0.1675 |  |
| High cholesterol | -0.0414 | 0.7526 | ±1.5051 | -0.055 | 0.9561 |  |
| Kidney disease | -1.5571 | 1.1199 | ±2.2398 | -1.390 | 0.1644 |  |
| Circulatory disease | +0.1284 | 1.0339 | ±2.0677 | +0.124 | 0.9011 |  |
| Glucose SD, pooled (mg/dL) | -0.0054 | 0.0361 | ±0.0722 | -0.150 | 0.8808 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.67** (p = **5.11e-16**), Residual SE = **16.024** on **2085** df, AIC = **17625.6**, BIC = **17710.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1318** | 3.2468 | ±6.4937 | **+38.540** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6017** | 0.7245 | ±1.4491 | **-2.211** | **0.0271** | * |
| **Education: high school or below (vs college)** | **+5.0223** | 1.3738 | ±2.7475 | **+3.656** | **2.56e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1756** | 0.9590 | ±1.9180 | **+2.269** | **0.0233** | * |
| Site: UW (vs UAB) | -0.9787 | 0.8558 | ±1.7116 | -1.144 | 0.2528 |  |
| **Season: spring (vs autumn)** | **+2.7825** | 0.9198 | ±1.8396 | **+3.025** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9820 | 1.0290 | ±2.0580 | +1.926 | 0.0541 | . |
| **Season: winter (vs autumn)** | **+4.2773** | 1.0378 | ±2.0757 | **+4.121** | **3.77e-05** | *** |
| **Age (years)** | **-0.1125** | 0.0360 | ±0.0719 | **-3.127** | **0.0018** | ** |
| **BMI (kg/m2)** | **+0.1773** | 0.0541 | ±0.1083 | **+3.276** | **0.0011** | ** |
| Hypertension | +1.0800 | 0.8054 | ±1.6109 | +1.341 | 0.1799 |  |
| High cholesterol | -0.0534 | 0.7512 | ±1.5024 | -0.071 | 0.9433 |  |
| Kidney disease | -1.6335 | 1.1205 | ±2.2409 | -1.458 | 0.1449 |  |
| Circulatory disease | +0.1162 | 1.0348 | ±2.0695 | +0.112 | 0.9106 |  |
| Avg. daily SD (mg/dL) | +0.0070 | 0.0366 | ±0.0732 | +0.193 | 0.8473 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.69** (p = **4.51e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.3**, BIC = **17710.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.6218** | 3.2492 | ±6.4985 | **+38.354** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5859** | 0.7265 | ±1.4530 | **-2.183** | **0.0290** | * |
| **Education: high school or below (vs college)** | **+5.0110** | 1.3734 | ±2.7469 | **+3.649** | **2.64e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.2001** | 0.9598 | ±1.9196 | **+2.292** | **0.0219** | * |
| Site: UW (vs UAB) | -0.9548 | 0.8555 | ±1.7110 | -1.116 | 0.2644 |  |
| **Season: spring (vs autumn)** | **+2.7900** | 0.9189 | ±1.8378 | **+3.036** | **0.0024** | ** |
| Season: summer (vs autumn) | +1.9776 | 1.0282 | ±2.0564 | +1.923 | 0.0544 | . |
| **Season: winter (vs autumn)** | **+4.2791** | 1.0353 | ±2.0706 | **+4.133** | **3.58e-05** | *** |
| **Age (years)** | **-0.1137** | 0.0363 | ±0.0726 | **-3.132** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1773** | 0.0542 | ±0.1085 | **+3.269** | **0.0011** | ** |
| Hypertension | +1.0578 | 0.7980 | ±1.5961 | +1.326 | 0.1850 |  |
| High cholesterol | -0.0515 | 0.7490 | ±1.4979 | -0.069 | 0.9452 |  |
| Kidney disease | -1.6975 | 1.1143 | ±2.2286 | -1.523 | 0.1277 |  |
| Circulatory disease | +0.1066 | 1.0347 | ±2.0694 | +0.103 | 0.9179 |  |
| CV (%) | +0.0385 | 0.0689 | ±0.1379 | +0.558 | 0.5766 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.68** (p = **4.96e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.5**, BIC = **17710.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7960** | 3.8070 | ±7.6140 | **+33.043** | **1.95e-239** | *** |
| **Education: graduate level (vs college)** | **-1.5960** | 0.7264 | ±1.4528 | **-2.197** | **0.0280** | * |
| **Education: high school or below (vs college)** | **+5.0249** | 1.3728 | ±2.7456 | **+3.660** | **2.52e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1811** | 0.9593 | ±1.9186 | **+2.274** | **0.0230** | * |
| Site: UW (vs UAB) | -0.9752 | 0.8558 | ±1.7117 | -1.139 | 0.2545 |  |
| **Season: spring (vs autumn)** | **+2.7821** | 0.9193 | ±1.8385 | **+3.026** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9747 | 1.0284 | ±2.0569 | +1.920 | 0.0548 | . |
| **Season: winter (vs autumn)** | **+4.2720** | 1.0352 | ±2.0703 | **+4.127** | **3.68e-05** | *** |
| **Age (years)** | **-0.1129** | 0.0363 | ±0.0726 | **-3.110** | **0.0019** | ** |
| **BMI (kg/m2)** | **+0.1775** | 0.0542 | ±0.1084 | **+3.275** | **0.0011** | ** |
| Hypertension | +1.0737 | 0.8000 | ±1.6000 | +1.342 | 0.1795 |  |
| High cholesterol | -0.0512 | 0.7492 | ±1.4984 | -0.068 | 0.9455 |  |
| Kidney disease | -1.6388 | 1.1145 | ±2.2289 | -1.470 | 0.1414 |  |
| Circulatory disease | +0.1129 | 1.0350 | ±2.0700 | +0.109 | 0.9131 |  |
| Mean / SD ratio | -0.0864 | 0.2655 | ±0.5310 | -0.326 | 0.7448 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **2100**, R² = **0.0492**, Adj R² = **0.0428**, F-statistic = **7.71** (p = **4.09e-16**), Residual SE = **16.022** on **2085** df, AIC = **17625.1**, BIC = **17709.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.4757** | 3.7615 | ±7.5230 | **+33.624** | **7.55e-248** | *** |
| **Education: graduate level (vs college)** | **-1.5832** | 0.7273 | ±1.4546 | **-2.177** | **0.0295** | * |
| **Education: high school or below (vs college)** | **+4.9952** | 1.3720 | ±2.7439 | **+3.641** | **2.72e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1920** | 0.9565 | ±1.9130 | **+2.292** | **0.0219** | * |
| Site: UW (vs UAB) | -0.9655 | 0.8565 | ±1.7130 | -1.127 | 0.2596 |  |
| **Season: spring (vs autumn)** | **+2.7904** | 0.9187 | ±1.8375 | **+3.037** | **0.0024** | ** |
| Season: summer (vs autumn) | +1.9826 | 1.0279 | ±2.0559 | +1.929 | 0.0538 | . |
| **Season: winter (vs autumn)** | **+4.2792** | 1.0350 | ±2.0700 | **+4.134** | **3.56e-05** | *** |
| **Age (years)** | **-0.1147** | 0.0364 | ±0.0727 | **-3.153** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1772** | 0.0542 | ±0.1084 | **+3.270** | **0.0011** | ** |
| Hypertension | +1.0506 | 0.7981 | ±1.5962 | +1.316 | 0.1881 |  |
| High cholesterol | -0.0542 | 0.7487 | ±1.4974 | -0.072 | 0.9423 |  |
| Kidney disease | -1.6929 | 1.1177 | ±2.2353 | -1.515 | 0.1299 |  |
| Circulatory disease | +0.1144 | 1.0355 | ±2.0711 | +0.110 | 0.9120 |  |
| Avg. daily mean/SD | -0.1637 | 0.2180 | ±0.4360 | -0.751 | 0.4526 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **2100**, R² = **0.0492**, Adj R² = **0.0429**, F-statistic = **7.71** (p = **4.01e-16**), Residual SE = **16.022** on **2085** df, AIC = **17625.0**, BIC = **17709.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.9920** | 3.4503 | ±6.9005 | **+35.937** | **8.06e-283** | *** |
| **Education: graduate level (vs college)** | **-1.5774** | 0.7243 | ±1.4485 | **-2.178** | **0.0294** | * |
| **Education: high school or below (vs college)** | **+4.9908** | 1.3826 | ±2.7651 | **+3.610** | **3.06e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.2130** | 0.9527 | ±1.9054 | **+2.323** | **0.0202** | * |
| Site: UW (vs UAB) | -0.9165 | 0.8525 | ±1.7049 | -1.075 | 0.2823 |  |
| **Season: spring (vs autumn)** | **+2.7898** | 0.9190 | ±1.8381 | **+3.036** | **0.0024** | ** |
| Season: summer (vs autumn) | +2.0045 | 1.0262 | ±2.0524 | +1.953 | 0.0508 | . |
| **Season: winter (vs autumn)** | **+4.2930** | 1.0352 | ±2.0704 | **+4.147** | **3.37e-05** | *** |
| **Age (years)** | **-0.1113** | 0.0356 | ±0.0711 | **-3.131** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1763** | 0.0543 | ±0.1087 | **+3.246** | **0.0012** | ** |
| Hypertension | +1.0801 | 0.7970 | ±1.5941 | +1.355 | 0.1754 |  |
| High cholesterol | -0.0426 | 0.7488 | ±1.4976 | -0.057 | 0.9546 |  |
| Kidney disease | -1.6691 | 1.1101 | ±2.2203 | -1.504 | 0.1327 |  |
| Circulatory disease | +0.1146 | 1.0365 | ±2.0730 | +0.111 | 0.9120 |  |
| MAG (mg/dL/h) | +0.0303 | 0.0426 | ±0.0851 | +0.712 | 0.4762 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.68** (p = **4.78e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.4**, BIC = **17710.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.8675** | 3.3013 | ±6.6026 | **+37.823** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5934** | 0.7246 | ±1.4491 | **-2.199** | **0.0279** | * |
| **Education: high school or below (vs college)** | **+4.9966** | 1.3730 | ±2.7459 | **+3.639** | **2.73e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1926** | 0.9580 | ±1.9159 | **+2.289** | **0.0221** | * |
| Site: UW (vs UAB) | -0.9662 | 0.8548 | ±1.7096 | -1.130 | 0.2583 |  |
| **Season: spring (vs autumn)** | **+2.7845** | 0.9195 | ±1.8389 | **+3.028** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9842 | 1.0283 | ±2.0565 | +1.930 | 0.0536 | . |
| **Season: winter (vs autumn)** | **+4.2823** | 1.0373 | ±2.0746 | **+4.128** | **3.65e-05** | *** |
| **Age (years)** | **-0.1130** | 0.0359 | ±0.0718 | **-3.148** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1775** | 0.0541 | ±0.1083 | **+3.277** | **0.0010** | ** |
| Hypertension | +1.0670 | 0.8042 | ±1.6084 | +1.327 | 0.1846 |  |
| High cholesterol | -0.0593 | 0.7504 | ±1.5009 | -0.079 | 0.9370 |  |
| Kidney disease | -1.6748 | 1.1171 | ±2.2342 | -1.499 | 0.1338 |  |
| Circulatory disease | +0.1075 | 1.0351 | ±2.0703 | +0.104 | 0.9173 |  |
| Avg. daily range (mg/dL) | +0.0041 | 0.0099 | ±0.0198 | +0.411 | 0.6809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **2100**, R² = **0.0499**, Adj R² = **0.0435**, F-statistic = **7.81** (p = **2.19e-16**), Residual SE = **16.016** on **2085** df, AIC = **17623.7**, BIC = **17708.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.6651** | 3.2216 | ±6.4433 | **+39.007** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6786** | 0.7226 | ±1.4453 | **-2.323** | **0.0202** | * |
| **Education: high school or below (vs college)** | **+5.1487** | 1.3745 | ±2.7490 | **+3.746** | **1.80e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.0797** | 0.9674 | ±1.9348 | **+2.150** | **0.0316** | * |
| Site: UW (vs UAB) | -1.0642 | 0.8550 | ±1.7100 | -1.245 | 0.2133 |  |
| **Season: spring (vs autumn)** | **+2.7926** | 0.9204 | ±1.8409 | **+3.034** | **0.0024** | ** |
| Season: summer (vs autumn) | +2.0104 | 1.0289 | ±2.0578 | +1.954 | 0.0507 | . |
| **Season: winter (vs autumn)** | **+4.2888** | 1.0311 | ±2.0623 | **+4.159** | **3.19e-05** | *** |
| **Age (years)** | **-0.1112** | 0.0358 | ±0.0715 | **-3.110** | **0.0019** | ** |
| **BMI (kg/m2)** | **+0.1846** | 0.0548 | ±0.1097 | **+3.366** | **7.64e-04** | *** |
| Hypertension | +1.1780 | 0.8039 | ±1.6078 | +1.465 | 0.1428 |  |
| High cholesterol | -0.0035 | 0.7561 | ±1.5121 | -0.005 | 0.9963 |  |
| Kidney disease | -1.4209 | 1.1230 | ±2.2460 | -1.265 | 0.2058 |  |
| Circulatory disease | +0.2083 | 1.0295 | ±2.0590 | +0.202 | 0.8396 |  |
| SD of daily means (mg/dL) | -0.0796 | 0.0968 | ±0.1935 | -0.823 | 0.4104 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.69** (p = **4.70e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.4**, BIC = **17710.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.3696** | 3.8105 | ±7.6209 | **+32.639** | **1.15e-233** | *** |
| **Education: graduate level (vs college)** | **-1.6267** | 0.7222 | ±1.4444 | **-2.252** | **0.0243** | * |
| **Education: high school or below (vs college)** | **+5.1060** | 1.3795 | ±2.7590 | **+3.701** | **2.15e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1259** | 0.9602 | ±1.9204 | **+2.214** | **0.0268** | * |
| Site: UW (vs UAB) | -1.0147 | 0.8536 | ±1.7071 | -1.189 | 0.2345 |  |
| **Season: spring (vs autumn)** | **+2.7738** | 0.9203 | ±1.8407 | **+3.014** | **0.0026** | ** |
| Season: summer (vs autumn) | +1.9673 | 1.0299 | ±2.0599 | +1.910 | 0.0561 | . |
| **Season: winter (vs autumn)** | **+4.2677** | 1.0371 | ±2.0742 | **+4.115** | **3.87e-05** | *** |
| **Age (years)** | **-0.1109** | 0.0357 | ±0.0714 | **-3.109** | **0.0019** | ** |
| **BMI (kg/m2)** | **+0.1798** | 0.0538 | ±0.1077 | **+3.338** | **8.43e-04** | *** |
| Hypertension | +1.1227 | 0.8079 | ±1.6158 | +1.390 | 0.1646 |  |
| High cholesterol | -0.0320 | 0.7506 | ±1.5011 | -0.043 | 0.9660 |  |
| Kidney disease | -1.5273 | 1.1205 | ±2.2411 | -1.363 | 0.1729 |  |
| Circulatory disease | +0.1384 | 1.0352 | ±2.0704 | +0.134 | 0.8936 |  |
| Time in range 70-180, pooled (%) | +0.0086 | 0.0222 | ±0.0444 | +0.390 | 0.6968 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.69** (p = **4.56e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.3**, BIC = **17710.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.2480** | 3.8124 | ±7.6247 | **+32.591** | **5.53e-233** | *** |
| **Education: graduate level (vs college)** | **-1.6284** | 0.7224 | ±1.4448 | **-2.254** | **0.0242** | * |
| **Education: high school or below (vs college)** | **+5.1147** | 1.3787 | ±2.7574 | **+3.710** | **2.07e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1205** | 0.9604 | ±1.9209 | **+2.208** | **0.0273** | * |
| Site: UW (vs UAB) | -1.0184 | 0.8536 | ±1.7072 | -1.193 | 0.2329 |  |
| **Season: spring (vs autumn)** | **+2.7743** | 0.9202 | ±1.8404 | **+3.015** | **0.0026** | ** |
| Season: summer (vs autumn) | +1.9671 | 1.0297 | ±2.0594 | +1.910 | 0.0561 | . |
| **Season: winter (vs autumn)** | **+4.2688** | 1.0362 | ±2.0724 | **+4.120** | **3.79e-05** | *** |
| **Age (years)** | **-0.1108** | 0.0357 | ±0.0714 | **-3.104** | **0.0019** | ** |
| **BMI (kg/m2)** | **+0.1801** | 0.0538 | ±0.1076 | **+3.346** | **8.21e-04** | *** |
| Hypertension | +1.1257 | 0.8077 | ±1.6155 | +1.394 | 0.1634 |  |
| High cholesterol | -0.0296 | 0.7508 | ±1.5016 | -0.039 | 0.9686 |  |
| Kidney disease | -1.5173 | 1.1198 | ±2.2396 | -1.355 | 0.1754 |  |
| Circulatory disease | +0.1406 | 1.0353 | ±2.0705 | +0.136 | 0.8920 |  |
| Avg. daily time in range 70-180 (%) | +0.0098 | 0.0222 | ±0.0443 | +0.441 | 0.6593 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.0494**, Adj R² = **0.0431**, F-statistic = **7.75** (p = **3.30e-16**), Residual SE = **16.020** on **2085** df, AIC = **17624.6**, BIC = **17709.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.6484** | 3.1386 | ±6.2772 | **+40.033** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6263** | 0.7272 | ±1.4543 | **-2.236** | **0.0253** | * |
| **Education: high school or below (vs college)** | **+4.9695** | 1.3718 | ±2.7436 | **+3.623** | **2.92e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.0707** | 0.9571 | ±1.9142 | **+2.164** | **0.0305** | * |
| Site: UW (vs UAB) | -1.0406 | 0.8499 | ±1.6998 | -1.224 | 0.2208 |  |
| **Season: spring (vs autumn)** | **+2.7762** | 0.9194 | ±1.8387 | **+3.020** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9565 | 1.0275 | ±2.0551 | +1.904 | 0.0569 | . |
| **Season: winter (vs autumn)** | **+4.2448** | 1.0362 | ±2.0724 | **+4.096** | **4.20e-05** | *** |
| **Age (years)** | **-0.1142** | 0.0352 | ±0.0704 | **-3.244** | **0.0012** | ** |
| **BMI (kg/m2)** | **+0.1798** | 0.0545 | ±0.1089 | **+3.302** | **9.60e-04** | *** |
| Hypertension | +1.1039 | 0.7956 | ±1.5912 | +1.387 | 0.1653 |  |
| High cholesterol | -0.0930 | 0.7494 | ±1.4988 | -0.124 | 0.9012 |  |
| Kidney disease | -1.6120 | 1.1175 | ±2.2349 | -1.443 | 0.1491 |  |
| Circulatory disease | +0.1800 | 1.0329 | ±2.0658 | +0.174 | 0.8617 |  |
| Any reading < 54 during wear (0/1) | -0.7848 | 0.7883 | ±1.5766 | -0.996 | 0.3195 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.67** (p = **5.19e-16**), Residual SE = **16.024** on **2085** df, AIC = **17625.6**, BIC = **17710.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.2262** | 3.2086 | ±6.4172 | **+39.028** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6085** | 0.7271 | ±1.4541 | **-2.212** | **0.0269** | * |
| **Education: high school or below (vs college)** | **+5.0509** | 1.3729 | ±2.7457 | **+3.679** | **2.34e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1692** | 0.9596 | ±1.9192 | **+2.261** | **0.0238** | * |
| Site: UW (vs UAB) | -0.9833 | 0.8583 | ±1.7165 | -1.146 | 0.2519 |  |
| **Season: spring (vs autumn)** | **+2.7802** | 0.9199 | ±1.8398 | **+3.022** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9768 | 1.0281 | ±2.0563 | +1.923 | 0.0545 | . |
| **Season: winter (vs autumn)** | **+4.2720** | 1.0348 | ±2.0695 | **+4.129** | **3.65e-05** | *** |
| **Age (years)** | **-0.1117** | 0.0356 | ±0.0713 | **-3.136** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1778** | 0.0542 | ±0.1084 | **+3.281** | **0.0010** | ** |
| Hypertension | +1.0979 | 0.7968 | ±1.5936 | +1.378 | 0.1682 |  |
| High cholesterol | -0.0442 | 0.7486 | ±1.4973 | -0.059 | 0.9530 |  |
| Kidney disease | -1.5920 | 1.1150 | ±2.2301 | -1.428 | 0.1534 |  |
| Circulatory disease | +0.1206 | 1.0358 | ±2.0717 | +0.116 | 0.9073 |  |
| Time < 54 (%) | +0.0459 | 0.6379 | ±1.2757 | +0.072 | 0.9426 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.68** (p = **4.79e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.4**, BIC = **17710.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1772** | 3.2053 | ±6.4106 | **+39.053** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6002** | 0.7269 | ±1.4538 | **-2.201** | **0.0277** | * |
| **Education: high school or below (vs college)** | **+5.0707** | 1.3735 | ±2.7469 | **+3.692** | **2.23e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.2003** | 0.9594 | ±1.9187 | **+2.293** | **0.0218** | * |
| Site: UW (vs UAB) | -0.9507 | 0.8594 | ±1.7188 | -1.106 | 0.2686 |  |
| **Season: spring (vs autumn)** | **+2.7877** | 0.9200 | ±1.8399 | **+3.030** | **0.0024** | ** |
| Season: summer (vs autumn) | +1.9739 | 1.0278 | ±2.0556 | +1.921 | 0.0548 | . |
| **Season: winter (vs autumn)** | **+4.2686** | 1.0349 | ±2.0698 | **+4.125** | **3.71e-05** | *** |
| **Age (years)** | **-0.1119** | 0.0357 | ±0.0713 | **-3.138** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1777** | 0.0542 | ±0.1084 | **+3.280** | **0.0010** | ** |
| Hypertension | +1.1048 | 0.7965 | ±1.5931 | +1.387 | 0.1654 |  |
| High cholesterol | -0.0312 | 0.7485 | ±1.4969 | -0.042 | 0.9667 |  |
| Kidney disease | -1.5944 | 1.1137 | ±2.2275 | -1.432 | 0.1523 |  |
| Circulatory disease | +0.1120 | 1.0360 | ±2.0720 | +0.108 | 0.9139 |  |
| Avg. daily time < 54 (%) | +0.3536 | 0.7188 | ±1.4375 | +0.492 | 0.6227 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.68** (p = **4.90e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.5**, BIC = **17710.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1617** | 3.2007 | ±6.4014 | **+39.105** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5969** | 0.7287 | ±1.4575 | **-2.191** | **0.0284** | * |
| **Education: high school or below (vs college)** | **+5.0645** | 1.3735 | ±2.7469 | **+3.687** | **2.27e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1889** | 0.9590 | ±1.9179 | **+2.283** | **0.0225** | * |
| Site: UW (vs UAB) | -0.9624 | 0.8562 | ±1.7124 | -1.124 | 0.2610 |  |
| **Season: spring (vs autumn)** | **+2.7845** | 0.9195 | ±1.8390 | **+3.028** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9796 | 1.0279 | ±2.0559 | +1.926 | 0.0541 | . |
| **Season: winter (vs autumn)** | **+4.2688** | 1.0349 | ±2.0699 | **+4.125** | **3.71e-05** | *** |
| **Age (years)** | **-0.1117** | 0.0356 | ±0.0713 | **-3.134** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1774** | 0.0542 | ±0.1084 | **+3.272** | **0.0011** | ** |
| Hypertension | +1.1047 | 0.7969 | ±1.5938 | +1.386 | 0.1657 |  |
| High cholesterol | -0.0363 | 0.7494 | ±1.4988 | -0.048 | 0.9613 |  |
| Kidney disease | -1.5926 | 1.1141 | ±2.2282 | -1.430 | 0.1528 |  |
| Circulatory disease | +0.1174 | 1.0362 | ±2.0725 | +0.113 | 0.9098 |  |
| Time 54-69, pooled (%) | +0.0907 | 0.2487 | ±0.4974 | +0.365 | 0.7152 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.67** (p = **5.05e-16**), Residual SE = **16.024** on **2085** df, AIC = **17625.6**, BIC = **17710.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1994** | 3.2009 | ±6.4018 | **+39.114** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5997** | 0.7292 | ±1.4584 | **-2.194** | **0.0282** | * |
| **Education: high school or below (vs college)** | **+5.0583** | 1.3739 | ±2.7478 | **+3.682** | **2.32e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1778** | 0.9586 | ±1.9172 | **+2.272** | **0.0231** | * |
| Site: UW (vs UAB) | -0.9704 | 0.8567 | ±1.7134 | -1.133 | 0.2573 |  |
| **Season: spring (vs autumn)** | **+2.7826** | 0.9195 | ±1.8391 | **+3.026** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9793 | 1.0279 | ±2.0559 | +1.926 | 0.0542 | . |
| **Season: winter (vs autumn)** | **+4.2683** | 1.0350 | ±2.0701 | **+4.124** | **3.73e-05** | *** |
| **Age (years)** | **-0.1119** | 0.0357 | ±0.0713 | **-3.136** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1775** | 0.0542 | ±0.1084 | **+3.275** | **0.0011** | ** |
| Hypertension | +1.1024 | 0.7968 | ±1.5935 | +1.384 | 0.1665 |  |
| High cholesterol | -0.0404 | 0.7493 | ±1.4986 | -0.054 | 0.9570 |  |
| Kidney disease | -1.5921 | 1.1144 | ±2.2288 | -1.429 | 0.1531 |  |
| Circulatory disease | +0.1197 | 1.0362 | ±2.0725 | +0.115 | 0.9081 |  |
| Avg. daily time 54-69 (%) | +0.0625 | 0.2448 | ±0.4896 | +0.255 | 0.7985 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.68** (p = **4.97e-16**), Residual SE = **16.024** on **2085** df, AIC = **17625.5**, BIC = **17710.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1645** | 3.2015 | ±6.4030 | **+39.096** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5996** | 0.7284 | ±1.4568 | **-2.196** | **0.0281** | * |
| **Education: high school or below (vs college)** | **+5.0647** | 1.3730 | ±2.7459 | **+3.689** | **2.25e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1903** | 0.9601 | ±1.9202 | **+2.281** | **0.0225** | * |
| Site: UW (vs UAB) | -0.9627 | 0.8568 | ±1.7136 | -1.124 | 0.2612 |  |
| **Season: spring (vs autumn)** | **+2.7844** | 0.9196 | ±1.8391 | **+3.028** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9782 | 1.0281 | ±2.0561 | +1.924 | 0.0543 | . |
| **Season: winter (vs autumn)** | **+4.2699** | 1.0349 | ±2.0699 | **+4.126** | **3.70e-05** | *** |
| **Age (years)** | **-0.1117** | 0.0356 | ±0.0712 | **-3.134** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1775** | 0.0542 | ±0.1084 | **+3.275** | **0.0011** | ** |
| Hypertension | +1.1038 | 0.7969 | ±1.5938 | +1.385 | 0.1660 |  |
| High cholesterol | -0.0358 | 0.7495 | ±1.4990 | -0.048 | 0.9619 |  |
| Kidney disease | -1.5923 | 1.1142 | ±2.2283 | -1.429 | 0.1530 |  |
| Circulatory disease | +0.1167 | 1.0362 | ±2.0724 | +0.113 | 0.9104 |  |
| Time < 70 (%) | +0.0631 | 0.1945 | ±0.3889 | +0.324 | 0.7457 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **2100**, R² = **0.0490**, Adj R² = **0.0426**, F-statistic = **7.68** (p = **4.97e-16**), Residual SE = **16.024** on **2085** df, AIC = **17625.5**, BIC = **17710.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1860** | 3.2013 | ±6.4026 | **+39.105** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5977** | 0.7288 | ±1.4575 | **-2.192** | **0.0284** | * |
| **Education: high school or below (vs college)** | **+5.0631** | 1.3737 | ±2.7474 | **+3.686** | **2.28e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1853** | 0.9595 | ±1.9189 | **+2.278** | **0.0228** | * |
| Site: UW (vs UAB) | -0.9627 | 0.8575 | ±1.7149 | -1.123 | 0.2615 |  |
| **Season: spring (vs autumn)** | **+2.7843** | 0.9196 | ±1.8392 | **+3.028** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9788 | 1.0280 | ±2.0559 | +1.925 | 0.0542 | . |
| **Season: winter (vs autumn)** | **+4.2676** | 1.0350 | ±2.0700 | **+4.123** | **3.73e-05** | *** |
| **Age (years)** | **-0.1119** | 0.0357 | ±0.0713 | **-3.136** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1775** | 0.0542 | ±0.1084 | **+3.275** | **0.0011** | ** |
| Hypertension | +1.1040 | 0.7967 | ±1.5935 | +1.386 | 0.1658 |  |
| High cholesterol | -0.0373 | 0.7494 | ±1.4987 | -0.050 | 0.9603 |  |
| Kidney disease | -1.5925 | 1.1141 | ±2.2282 | -1.429 | 0.1529 |  |
| Circulatory disease | +0.1177 | 1.0363 | ±2.0725 | +0.114 | 0.9095 |  |
| Avg. daily time < 70 (%) | +0.0647 | 0.1957 | ±0.3913 | +0.331 | 0.7409 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.0507**, Adj R² = **0.0443**, F-statistic = **7.95** (p = **9.76e-17**), Residual SE = **16.009** on **2085** df, AIC = **17621.9**, BIC = **17706.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+119.1125** | 4.6084 | ±9.2168 | **+25.847** | **2.65e-147** | *** |
| **Education: graduate level (vs college)** | **-1.6906** | 0.7247 | ±1.4495 | **-2.333** | **0.0197** | * |
| **Education: high school or below (vs college)** | **+5.2648** | 1.3786 | ±2.7573 | **+3.819** | **1.34e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.0428** | 0.9619 | ±1.9239 | **+2.124** | **0.0337** | * |
| Site: UW (vs UAB) | -1.1121 | 0.8582 | ±1.7164 | -1.296 | 0.1950 |  |
| **Season: spring (vs autumn)** | **+2.7546** | 0.9217 | ±1.8434 | **+2.989** | **0.0028** | ** |
| Season: summer (vs autumn) | +1.8813 | 1.0329 | ±2.0659 | +1.821 | 0.0686 | . |
| **Season: winter (vs autumn)** | **+4.2551** | 1.0337 | ±2.0673 | **+4.117** | **3.85e-05** | *** |
| **Age (years)** | **-0.1127** | 0.0357 | ±0.0714 | **-3.155** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1823** | 0.0538 | ±0.1076 | **+3.387** | **7.07e-04** | *** |
| Hypertension | +1.1734 | 0.7979 | ±1.5957 | +1.471 | 0.1414 |  |
| High cholesterol | -0.0298 | 0.7488 | ±1.4977 | -0.040 | 0.9683 |  |
| Kidney disease | -1.4254 | 1.1103 | ±2.2205 | -1.284 | 0.1992 |  |
| Circulatory disease | +0.1865 | 1.0343 | ±2.0686 | +0.180 | 0.8569 |  |
| Time 54-250, pooled (%) | +0.0630 | 0.0366 | ±0.0733 | +1.719 | 0.0857 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **2100**, R² = **0.0508**, Adj R² = **0.0445**, F-statistic = **7.98** (p = **8.38e-17**), Residual SE = **16.008** on **2085** df, AIC = **17621.5**, BIC = **17706.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+118.7211** | 4.6817 | ±9.3634 | **+25.358** | **7.26e-142** | *** |
| **Education: graduate level (vs college)** | **-1.6935** | 0.7247 | ±1.4495 | **-2.337** | **0.0195** | * |
| **Education: high school or below (vs college)** | **+5.2748** | 1.3776 | ±2.7551 | **+3.829** | **1.29e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.0387** | 0.9616 | ±1.9233 | **+2.120** | **0.0340** | * |
| Site: UW (vs UAB) | -1.1134 | 0.8579 | ±1.7157 | -1.298 | 0.1943 |  |
| **Season: spring (vs autumn)** | **+2.7580** | 0.9215 | ±1.8431 | **+2.993** | **0.0028** | ** |
| Season: summer (vs autumn) | +1.8829 | 1.0325 | ±2.0650 | +1.824 | 0.0682 | . |
| **Season: winter (vs autumn)** | **+4.2587** | 1.0332 | ±2.0664 | **+4.122** | **3.76e-05** | *** |
| **Age (years)** | **-0.1124** | 0.0357 | ±0.0714 | **-3.146** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1826** | 0.0538 | ±0.1075 | **+3.396** | **6.84e-04** | *** |
| Hypertension | +1.1737 | 0.7979 | ±1.5958 | +1.471 | 0.1413 |  |
| High cholesterol | -0.0287 | 0.7489 | ±1.4978 | -0.038 | 0.9694 |  |
| Kidney disease | -1.4102 | 1.1090 | ±2.2180 | -1.272 | 0.2035 |  |
| Circulatory disease | +0.1934 | 1.0349 | ±2.0697 | +0.187 | 0.8518 |  |
| Avg. daily time 54-250 (%) | +0.0666 | 0.0378 | ±0.0756 | +1.762 | 0.0780 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.0493**, Adj R² = **0.0430**, F-statistic = **7.73** (p = **3.65e-16**), Residual SE = **16.021** on **2085** df, AIC = **17624.8**, BIC = **17709.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3546** | 3.2063 | ±6.4127 | **+39.096** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5947** | 0.7242 | ±1.4483 | **-2.202** | **0.0277** | * |
| **Education: high school or below (vs college)** | **+4.9567** | 1.3745 | ±2.7489 | **+3.606** | **3.11e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.2131** | 0.9549 | ±1.9099 | **+2.318** | **0.0205** | * |
| Site: UW (vs UAB) | -0.9703 | 0.8543 | ±1.7087 | -1.136 | 0.2561 |  |
| **Season: spring (vs autumn)** | **+2.7833** | 0.9201 | ±1.8401 | **+3.025** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9677 | 1.0282 | ±2.0564 | +1.914 | 0.0557 | . |
| **Season: winter (vs autumn)** | **+4.2784** | 1.0376 | ±2.0753 | **+4.123** | **3.74e-05** | *** |
| **Age (years)** | **-0.1147** | 0.0358 | ±0.0715 | **-3.207** | **0.0013** | ** |
| **BMI (kg/m2)** | **+0.1739** | 0.0540 | ±0.1080 | **+3.221** | **0.0013** | ** |
| Hypertension | +1.0500 | 0.8112 | ±1.6225 | +1.294 | 0.1956 |  |
| High cholesterol | -0.0865 | 0.7494 | ±1.4988 | -0.115 | 0.9081 |  |
| Kidney disease | -1.7146 | 1.1327 | ±2.2655 | -1.514 | 0.1301 |  |
| Circulatory disease | +0.1017 | 1.0352 | ±2.0703 | +0.098 | 0.9217 |  |
| Time 181-250, pooled (%) | +0.0253 | 0.0378 | ±0.0756 | +0.669 | 0.5036 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **2100**, R² = **0.0493**, Adj R² = **0.0429**, F-statistic = **7.72** (p = **3.79e-16**), Residual SE = **16.021** on **2085** df, AIC = **17624.9**, BIC = **17709.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3459** | 3.2067 | ±6.4134 | **+39.088** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5967** | 0.7244 | ±1.4489 | **-2.204** | **0.0275** | * |
| **Education: high school or below (vs college)** | **+4.9599** | 1.3743 | ±2.7486 | **+3.609** | **3.07e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.2132** | 0.9556 | ±1.9113 | **+2.316** | **0.0206** | * |
| Site: UW (vs UAB) | -0.9691 | 0.8542 | ±1.7083 | -1.135 | 0.2566 |  |
| **Season: spring (vs autumn)** | **+2.7818** | 0.9200 | ±1.8401 | **+3.024** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9680 | 1.0282 | ±2.0564 | +1.914 | 0.0556 | . |
| **Season: winter (vs autumn)** | **+4.2763** | 1.0370 | ±2.0741 | **+4.124** | **3.73e-05** | *** |
| **Age (years)** | **-0.1144** | 0.0358 | ±0.0715 | **-3.200** | **0.0014** | ** |
| **BMI (kg/m2)** | **+0.1741** | 0.0540 | ±0.1080 | **+3.223** | **0.0013** | ** |
| Hypertension | +1.0527 | 0.8107 | ±1.6215 | +1.298 | 0.1941 |  |
| High cholesterol | -0.0847 | 0.7498 | ±1.4996 | -0.113 | 0.9100 |  |
| Kidney disease | -1.7081 | 1.1327 | ±2.2654 | -1.508 | 0.1316 |  |
| Circulatory disease | +0.1039 | 1.0350 | ±2.0700 | +0.100 | 0.9200 |  |
| Avg. daily time 181-250 (%) | +0.0235 | 0.0369 | ±0.0739 | +0.637 | 0.5241 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.69** (p = **4.65e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.4**, BIC = **17710.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.2225** | 3.2088 | ±6.4176 | **+39.024** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6260** | 0.7224 | ±1.4449 | **-2.251** | **0.0244** | * |
| **Education: high school or below (vs college)** | **+5.1110** | 1.3795 | ±2.7590 | **+3.705** | **2.11e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1284** | 0.9592 | ±1.9184 | **+2.219** | **0.0265** | * |
| Site: UW (vs UAB) | -1.0121 | 0.8538 | ±1.7077 | -1.185 | 0.2359 |  |
| **Season: spring (vs autumn)** | **+2.7743** | 0.9203 | ±1.8405 | **+3.015** | **0.0026** | ** |
| Season: summer (vs autumn) | +1.9670 | 1.0299 | ±2.0599 | +1.910 | 0.0562 | . |
| **Season: winter (vs autumn)** | **+4.2673** | 1.0372 | ±2.0745 | **+4.114** | **3.89e-05** | *** |
| **Age (years)** | **-0.1109** | 0.0357 | ±0.0714 | **-3.108** | **0.0019** | ** |
| **BMI (kg/m2)** | **+0.1798** | 0.0539 | ±0.1077 | **+3.339** | **8.41e-04** | *** |
| Hypertension | +1.1248 | 0.8082 | ±1.6164 | +1.392 | 0.1640 |  |
| High cholesterol | -0.0298 | 0.7509 | ±1.5018 | -0.040 | 0.9683 |  |
| Kidney disease | -1.5246 | 1.1207 | ±2.2413 | -1.360 | 0.1737 |  |
| Circulatory disease | +0.1383 | 1.0352 | ±2.0705 | +0.134 | 0.8937 |  |
| Time > 180 (%) | -0.0090 | 0.0220 | ±0.0441 | -0.408 | 0.6829 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.69** (p = **4.51e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.3**, BIC = **17710.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.2161** | 3.2084 | ±6.4169 | **+39.027** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6273** | 0.7227 | ±1.4453 | **-2.252** | **0.0243** | * |
| **Education: high school or below (vs college)** | **+5.1198** | 1.3788 | ±2.7576 | **+3.713** | **2.05e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1225** | 0.9595 | ±1.9191 | **+2.212** | **0.0270** | * |
| Site: UW (vs UAB) | -1.0154 | 0.8538 | ±1.7077 | -1.189 | 0.2344 |  |
| **Season: spring (vs autumn)** | **+2.7750** | 0.9201 | ±1.8402 | **+3.016** | **0.0026** | ** |
| Season: summer (vs autumn) | +1.9669 | 1.0297 | ±2.0593 | +1.910 | 0.0561 | . |
| **Season: winter (vs autumn)** | **+4.2680** | 1.0365 | ±2.0730 | **+4.118** | **3.83e-05** | *** |
| **Age (years)** | **-0.1108** | 0.0357 | ±0.0714 | **-3.105** | **0.0019** | ** |
| **BMI (kg/m2)** | **+0.1801** | 0.0538 | ±0.1076 | **+3.346** | **8.19e-04** | *** |
| Hypertension | +1.1279 | 0.8081 | ±1.6161 | +1.396 | 0.1628 |  |
| High cholesterol | -0.0274 | 0.7511 | ±1.5022 | -0.036 | 0.9709 |  |
| Kidney disease | -1.5145 | 1.1200 | ±2.2399 | -1.352 | 0.1763 |  |
| Circulatory disease | +0.1406 | 1.0352 | ±2.0705 | +0.136 | 0.8920 |  |
| Avg. daily time > 180 (%) | -0.0101 | 0.0221 | ±0.0442 | -0.459 | 0.6460 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **2100**, R² = **0.0491**, Adj R² = **0.0427**, F-statistic = **7.68** (p = **4.81e-16**), Residual SE = **16.023** on **2085** df, AIC = **17625.5**, BIC = **17710.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.2202** | 3.2072 | ±6.4145 | **+39.043** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6284** | 0.7212 | ±1.4424 | **-2.258** | **0.0240** | * |
| **Education: high school or below (vs college)** | **+5.0970** | 1.3771 | ±2.7542 | **+3.701** | **2.15e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.1335** | 0.9609 | ±1.9217 | **+2.220** | **0.0264** | * |
| Site: UW (vs UAB) | -1.0060 | 0.8535 | ±1.7070 | -1.179 | 0.2385 |  |
| **Season: spring (vs autumn)** | **+2.7815** | 0.9193 | ±1.8386 | **+3.026** | **0.0025** | ** |
| Season: summer (vs autumn) | +1.9678 | 1.0305 | ±2.0611 | +1.909 | 0.0562 | . |
| **Season: winter (vs autumn)** | **+4.2747** | 1.0328 | ±2.0657 | **+4.139** | **3.49e-05** | *** |
| **Age (years)** | **-0.1116** | 0.0357 | ±0.0713 | **-3.128** | **0.0018** | ** |
| **BMI (kg/m2)** | **+0.1803** | 0.0538 | ±0.1076 | **+3.351** | **8.04e-04** | *** |
| Hypertension | +1.1125 | 0.8045 | ±1.6091 | +1.383 | 0.1667 |  |
| High cholesterol | -0.0349 | 0.7509 | ±1.5018 | -0.046 | 0.9630 |  |
| Kidney disease | -1.5489 | 1.1219 | ±2.2438 | -1.381 | 0.1674 |  |
| Circulatory disease | +0.1337 | 1.0346 | ±2.0693 | +0.129 | 0.8972 |  |
| Nocturnal time > 180 (%) | -0.0076 | 0.0244 | ±0.0487 | -0.311 | 0.7560 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.0499**, Adj R² = **0.0435**, F-statistic = **7.82** (p = **2.10e-16**), Residual SE = **16.016** on **2085** df, AIC = **17623.6**, BIC = **17708.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1232** | 3.2061 | ±6.4121 | **+39.027** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.5483** | 0.7234 | ±1.4468 | **-2.140** | **0.0323** | * |
| **Education: high school or below (vs college)** | **+4.9608** | 1.3697 | ±2.7393 | **+3.622** | **2.92e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.2171** | 0.9543 | ±1.9086 | **+2.323** | **0.0202** | * |
| Site: UW (vs UAB) | -0.9683 | 0.8551 | ±1.7101 | -1.132 | 0.2575 |  |
| **Season: spring (vs autumn)** | **+2.8372** | 0.9201 | ±1.8402 | **+3.084** | **0.0020** | ** |
| Season: summer (vs autumn) | +1.9863 | 1.0274 | ±2.0547 | +1.933 | 0.0532 | . |
| **Season: winter (vs autumn)** | **+4.3324** | 1.0419 | ±2.0837 | **+4.158** | **3.21e-05** | *** |
| **Age (years)** | **-0.1163** | 0.0357 | ±0.0715 | **-3.256** | **0.0011** | ** |
| **BMI (kg/m2)** | **+0.1785** | 0.0542 | ±0.1084 | **+3.292** | **9.95e-04** | *** |
| Hypertension | +1.0008 | 0.8072 | ±1.6144 | +1.240 | 0.2150 |  |
| High cholesterol | -0.1103 | 0.7511 | ±1.5022 | -0.147 | 0.8833 |  |
| Kidney disease | -1.7512 | 1.1147 | ±2.2293 | -1.571 | 0.1162 |  |
| Circulatory disease | +0.1210 | 1.0352 | ±2.0704 | +0.117 | 0.9070 |  |
| Any reading > 250 during wear (0/1) | +1.0645 | 0.7661 | ±1.5322 | +1.389 | 0.1647 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **2100**, R² = **0.0507**, Adj R² = **0.0443**, F-statistic = **7.95** (p = **9.73e-17**), Residual SE = **16.009** on **2085** df, AIC = **17621.8**, BIC = **17706.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3866** | 3.2113 | ±6.4226 | **+39.045** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6895** | 0.7247 | ±1.4494 | **-2.331** | **0.0197** | * |
| **Education: high school or below (vs college)** | **+5.2703** | 1.3788 | ±2.7576 | **+3.822** | **1.32e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.0523** | 0.9612 | ±1.9224 | **+2.135** | **0.0327** | * |
| Site: UW (vs UAB) | -1.1043 | 0.8579 | ±1.7158 | -1.287 | 0.1980 |  |
| **Season: spring (vs autumn)** | **+2.7561** | 0.9216 | ±1.8433 | **+2.990** | **0.0028** | ** |
| Season: summer (vs autumn) | +1.8805 | 1.0329 | ±2.0658 | +1.821 | 0.0687 | . |
| **Season: winter (vs autumn)** | **+4.2552** | 1.0337 | ±2.0674 | **+4.116** | **3.85e-05** | *** |
| **Age (years)** | **-0.1126** | 0.0357 | ±0.0714 | **-3.153** | **0.0016** | ** |
| **BMI (kg/m2)** | **+0.1823** | 0.0538 | ±0.1077 | **+3.386** | **7.09e-04** | *** |
| Hypertension | +1.1748 | 0.7979 | ±1.5959 | +1.472 | 0.1409 |  |
| High cholesterol | -0.0260 | 0.7491 | ±1.4981 | -0.035 | 0.9723 |  |
| Kidney disease | -1.4252 | 1.1101 | ±2.2201 | -1.284 | 0.1992 |  |
| Circulatory disease | +0.1844 | 1.0343 | ±2.0687 | +0.178 | 0.8585 |  |
| Time > 250 (%) | -0.0630 | 0.0366 | ±0.0733 | -1.718 | 0.0858 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 2,100)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **2100**, R² = **0.0509**, Adj R² = **0.0445**, F-statistic = **7.98** (p = **8.13e-17**), Residual SE = **16.008** on **2085** df, AIC = **17621.4**, BIC = **17706.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3680** | 3.2097 | ±6.4193 | **+39.060** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **-1.6924** | 0.7248 | ±1.4495 | **-2.335** | **0.0195** | * |
| **Education: high school or below (vs college)** | **+5.2813** | 1.3777 | ±2.7554 | **+3.833** | **1.26e-04** | *** |
| **Site: UCSD (vs UAB)** | **+2.0449** | 0.9611 | ±1.9221 | **+2.128** | **0.0334** | * |
| Site: UW (vs UAB) | -1.1072 | 0.8575 | ±1.7150 | -1.291 | 0.1967 |  |
| **Season: spring (vs autumn)** | **+2.7595** | 0.9215 | ±1.8430 | **+2.995** | **0.0027** | ** |
| Season: summer (vs autumn) | +1.8814 | 1.0324 | ±2.0649 | +1.822 | 0.0684 | . |
| **Season: winter (vs autumn)** | **+4.2579** | 1.0333 | ±2.0665 | **+4.121** | **3.77e-05** | *** |
| **Age (years)** | **-0.1124** | 0.0357 | ±0.0714 | **-3.147** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.1826** | 0.0538 | ±0.1075 | **+3.397** | **6.82e-04** | *** |
| Hypertension | +1.1759 | 0.7980 | ±1.5960 | +1.474 | 0.1406 |  |
| High cholesterol | -0.0256 | 0.7491 | ±1.4981 | -0.034 | 0.9727 |  |
| Kidney disease | -1.4091 | 1.1089 | ±2.2178 | -1.271 | 0.2038 |  |
| Circulatory disease | +0.1920 | 1.0348 | ±2.0696 | +0.186 | 0.8528 |  |
| Avg. daily time > 250 (%) | -0.0671 | 0.0378 | ±0.0757 | -1.775 | 0.0760 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Total analysis base - Home environment

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 124 single-predictor tests; 6 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 124 tests (samples with n >= 500), of which **2** are significant at BH q < 0.05 in the all-tests family and 0 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 2,100): best single predictor out of sample is **HbA1c** (CV R² 0.142 vs 0.139 for covariates alone, gain +0.004; +0.0733 per SD, p = 0.003, q = 0.015). FDR-robust associations (2): HbA1c (higher outcome, +0.0733 per SD, q = 0.015); SD of daily means (higher outcome, +0.0623 per SD, q = 0.026).
- **Indoor temperature, mean (deg C)** (n = 2,100): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.290 vs 0.290 for covariates alone, gain +0.000; +0.0746 per SD, p = 0.076, q = 0.184). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 2,100): best single predictor out of sample is **%<54 (daily avg)** (CV R² 0.231 vs 0.231 for covariates alone, gain +0.001; -0.263 per SD, p = 0.045, q = 0.127). No association survives FDR; nominal only: %<54 (pooled) (p = 0.030), %<54 (daily avg) (p = 0.045). Not predictable from glycaemia in this sample.
- **Indoor VOC index, mean** (n = 2,100): best single predictor out of sample is **%>250 (daily avg)** (CV R² 0.027 vs 0.027 for covariates alone, gain +0.000; -0.733 per SD, p = 0.076, q = 0.184). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.

**Most predictable outcomes (largest out-of-sample gain over covariates):** Indoor PM2.5, log(1 + mean ug/m3) (+0.004, via HbA1c); Indoor relative humidity, mean (%) (+0.001, via %<54 (daily avg)); Indoor temperature, mean (deg C) (+0.000, via %<70 (daily avg)); Indoor VOC index, mean (+0.000, via %>250 (daily avg)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (1 FDR-significant / 2 raw-significant of 32); HbA1c (1 FDR-significant / 1 raw-significant of 4); Band < 54 (0 FDR-significant / 2 raw-significant of 12).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 1 FDR-significant (2 raw); HbA1c alone: 1 FDR-significant (1 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Indoor temperature, mean (%<54 (pooled), ΔAIC -2.9); Indoor relative humidity, mean (%<54 (daily avg), ΔAIC -3.9); Indoor VOC index, mean (%>250 (daily avg), ΔAIC -2.2).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
