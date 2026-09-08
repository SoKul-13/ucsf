# Phase 6 model output tables - All (analysis base) - Healthy group (no diabetes + pre-diabetes / lifestyle) - Home environment

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models. [Index of all model-output files](../../README.md)


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 1,251; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1368**, F-statistic = **16.24** (p = **9.99e-35**), Residual SE = **0.858** on **1237** df, AIC = **3182.3**, BIC = **3254.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2254** | 0.1902 | ±0.3805 | **+11.699** | **1.30e-31** | *** |
| Education: graduate level (vs college) | -0.0145 | 0.0501 | ±0.1001 | -0.290 | 0.7715 |  |
| **Education: high school or below (vs college)** | **+0.5106** | 0.1213 | ±0.2427 | **+4.208** | **2.58e-05** | *** |
| Site: UCSD (vs UAB) | -0.0285 | 0.0658 | ±0.1317 | -0.432 | 0.6654 |  |
| **Site: UW (vs UAB)** | **-0.3790** | 0.0660 | ±0.1320 | **-5.741** | **9.39e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1570** | 0.0668 | ±0.1336 | **-2.351** | **0.0187** | * |
| Season: summer (vs autumn) | -0.0401 | 0.0731 | ±0.1461 | -0.549 | 0.5830 |  |
| Season: winter (vs autumn) | -0.0456 | 0.0702 | ±0.1404 | -0.649 | 0.5162 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.840** | **5.23e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.654** | **3.26e-06** | *** |
| Hypertension | +0.0922 | 0.0567 | ±0.1134 | +1.626 | 0.1040 |  |
| High cholesterol | -0.0393 | 0.0492 | ±0.0985 | -0.799 | 0.4244 |  |
| Kidney disease | -0.0661 | 0.0819 | ±0.1638 | -0.807 | 0.4198 |  |
| **Circulatory disease** | **+0.2269** | 0.0904 | ±0.1808 | **+2.511** | **0.0121** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1361**, F-statistic = **15.07** (p = **4.12e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.3**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2168** | 0.2767 | ±0.5534 | **+8.011** | **1.14e-15** | *** |
| Education: graduate level (vs college) | -0.0146 | 0.0501 | ±0.1002 | -0.291 | 0.7713 |  |
| **Education: high school or below (vs college)** | **+0.5103** | 0.1222 | ±0.2443 | **+4.177** | **2.95e-05** | *** |
| Site: UCSD (vs UAB) | -0.0285 | 0.0658 | ±0.1315 | -0.434 | 0.6646 |  |
| **Site: UW (vs UAB)** | **-0.3791** | 0.0659 | ±0.1319 | **-5.750** | **8.94e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1568** | 0.0670 | ±0.1340 | **-2.341** | **0.0192** | * |
| Season: summer (vs autumn) | -0.0400 | 0.0732 | ±0.1464 | -0.547 | 0.5844 |  |
| Season: winter (vs autumn) | -0.0455 | 0.0704 | ±0.1407 | -0.646 | 0.5180 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.861** | **4.60e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.642** | **3.46e-06** | *** |
| Hypertension | +0.0921 | 0.0568 | ±0.1136 | +1.621 | 0.1050 |  |
| High cholesterol | -0.0395 | 0.0494 | ±0.0989 | -0.799 | 0.4241 |  |
| Kidney disease | -0.0661 | 0.0819 | ±0.1639 | -0.806 | 0.4202 |  |
| **Circulatory disease** | **+0.2268** | 0.0909 | ±0.1817 | **+2.496** | **0.0126** | * |
| HbA1c (%) | +0.0017 | 0.0358 | ±0.0717 | +0.047 | 0.9627 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **1251**, R² = **0.1489**, Adj R² = **0.1393**, F-statistic = **15.45** (p = **4.83e-35**), Residual SE = **0.857** on **1236** df, AIC = **3179.7**, BIC = **3256.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5269** | 0.2363 | ±0.4726 | **+10.693** | **1.10e-26** | *** |
| Education: graduate level (vs college) | -0.0082 | 0.0500 | ±0.1000 | -0.164 | 0.8696 |  |
| **Education: high school or below (vs college)** | **+0.5266** | 0.1219 | ±0.2437 | **+4.321** | **1.55e-05** | *** |
| Site: UCSD (vs UAB) | -0.0309 | 0.0658 | ±0.1315 | -0.470 | 0.6384 |  |
| **Site: UW (vs UAB)** | **-0.3710** | 0.0659 | ±0.1318 | **-5.629** | **1.81e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1619** | 0.0670 | ±0.1339 | **-2.418** | **0.0156** | * |
| Season: summer (vs autumn) | -0.0479 | 0.0731 | ±0.1461 | -0.655 | 0.5124 |  |
| Season: winter (vs autumn) | -0.0538 | 0.0700 | ±0.1399 | -0.768 | 0.4422 |  |
| **Age (years)** | **-0.0130** | 0.0023 | ±0.0045 | **-5.769** | **7.96e-09** | *** |
| **BMI (kg/m2)** | **+0.0190** | 0.0040 | ±0.0080 | **+4.774** | **1.81e-06** | *** |
| Hypertension | +0.1018 | 0.0571 | ±0.1141 | +1.784 | 0.0745 | . |
| High cholesterol | -0.0339 | 0.0492 | ±0.0984 | -0.689 | 0.4907 |  |
| Kidney disease | -0.0572 | 0.0813 | ±0.1626 | -0.704 | 0.4817 |  |
| **Circulatory disease** | **+0.2346** | 0.0904 | ±0.1809 | **+2.594** | **0.0095** | ** |
| **Mean glucose (mg/dL)** | **-0.0027** | 0.0011 | ±0.0023 | **-2.407** | **0.0161** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **1251**, R² = **0.1489**, Adj R² = **0.1393**, F-statistic = **15.45** (p = **4.83e-35**), Residual SE = **0.857** on **1236** df, AIC = **3179.7**, BIC = **3256.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9069** | 0.3543 | ±0.7085 | **+8.206** | **2.29e-16** | *** |
| Education: graduate level (vs college) | -0.0082 | 0.0500 | ±0.1000 | -0.164 | 0.8696 |  |
| **Education: high school or below (vs college)** | **+0.5266** | 0.1219 | ±0.2437 | **+4.321** | **1.55e-05** | *** |
| Site: UCSD (vs UAB) | -0.0309 | 0.0658 | ±0.1315 | -0.470 | 0.6384 |  |
| **Site: UW (vs UAB)** | **-0.3710** | 0.0659 | ±0.1318 | **-5.629** | **1.81e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1619** | 0.0670 | ±0.1339 | **-2.418** | **0.0156** | * |
| Season: summer (vs autumn) | -0.0479 | 0.0731 | ±0.1461 | -0.655 | 0.5124 |  |
| Season: winter (vs autumn) | -0.0538 | 0.0700 | ±0.1399 | -0.768 | 0.4422 |  |
| **Age (years)** | **-0.0130** | 0.0023 | ±0.0045 | **-5.769** | **7.96e-09** | *** |
| **BMI (kg/m2)** | **+0.0190** | 0.0040 | ±0.0080 | **+4.774** | **1.81e-06** | *** |
| Hypertension | +0.1018 | 0.0571 | ±0.1141 | +1.784 | 0.0745 | . |
| High cholesterol | -0.0339 | 0.0492 | ±0.0984 | -0.689 | 0.4907 |  |
| Kidney disease | -0.0572 | 0.0813 | ±0.1626 | -0.704 | 0.4817 |  |
| **Circulatory disease** | **+0.2346** | 0.0904 | ±0.1809 | **+2.594** | **0.0095** | ** |
| **GMI (%)** | **-0.1148** | 0.0477 | ±0.0954 | **-2.407** | **0.0161** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **1251**, R² = **0.1481**, Adj R² = **0.1384**, F-statistic = **15.35** (p = **8.60e-35**), Residual SE = **0.858** on **1236** df, AIC = **3180.9**, BIC = **3257.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4652** | 0.2287 | ±0.4573 | **+10.781** | **4.24e-27** | *** |
| Education: graduate level (vs college) | -0.0109 | 0.0500 | ±0.1000 | -0.218 | 0.8271 |  |
| **Education: high school or below (vs college)** | **+0.5236** | 0.1220 | ±0.2440 | **+4.291** | **1.78e-05** | *** |
| Site: UCSD (vs UAB) | -0.0272 | 0.0658 | ±0.1315 | -0.413 | 0.6796 |  |
| **Site: UW (vs UAB)** | **-0.3730** | 0.0659 | ±0.1318 | **-5.662** | **1.49e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1575** | 0.0668 | ±0.1335 | **-2.359** | **0.0183** | * |
| Season: summer (vs autumn) | -0.0460 | 0.0731 | ±0.1463 | -0.629 | 0.5296 |  |
| Season: winter (vs autumn) | -0.0488 | 0.0699 | ±0.1399 | -0.698 | 0.4854 |  |
| **Age (years)** | **-0.0133** | 0.0023 | ±0.0045 | **-5.859** | **4.66e-09** | *** |
| **BMI (kg/m2)** | **+0.0195** | 0.0040 | ±0.0080 | **+4.867** | **1.13e-06** | *** |
| Hypertension | +0.0987 | 0.0570 | ±0.1139 | +1.732 | 0.0833 | . |
| High cholesterol | -0.0332 | 0.0492 | ±0.0985 | -0.675 | 0.4999 |  |
| Kidney disease | -0.0650 | 0.0816 | ±0.1632 | -0.796 | 0.4258 |  |
| **Circulatory disease** | **+0.2310** | 0.0905 | ±0.1810 | **+2.552** | **0.0107** | * |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0022** | 0.0011 | ±0.0021 | **-2.108** | **0.0350** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.1470**, Adj R² = **0.1373**, F-statistic = **15.21** (p = **1.84e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.5**, BIC = **3259.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.3171** | 0.2011 | ±0.4022 | **+11.522** | **1.02e-30** | *** |
| Education: graduate level (vs college) | -0.0138 | 0.0500 | ±0.1001 | -0.275 | 0.7833 |  |
| **Education: high school or below (vs college)** | **+0.5121** | 0.1214 | ±0.2428 | **+4.219** | **2.46e-05** | *** |
| Site: UCSD (vs UAB) | -0.0331 | 0.0660 | ±0.1319 | -0.502 | 0.6158 |  |
| **Site: UW (vs UAB)** | **-0.3766** | 0.0662 | ±0.1323 | **-5.692** | **1.25e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1601** | 0.0667 | ±0.1335 | **-2.398** | **0.0165** | * |
| Season: summer (vs autumn) | -0.0432 | 0.0731 | ±0.1462 | -0.591 | 0.5547 |  |
| Season: winter (vs autumn) | -0.0484 | 0.0702 | ±0.1405 | -0.689 | 0.4906 |  |
| **Age (years)** | **-0.0130** | 0.0023 | ±0.0045 | **-5.760** | **8.40e-09** | *** |
| **BMI (kg/m2)** | **+0.0187** | 0.0040 | ±0.0080 | **+4.675** | **2.94e-06** | *** |
| Hypertension | +0.0983 | 0.0570 | ±0.1139 | +1.725 | 0.0845 | . |
| High cholesterol | -0.0394 | 0.0492 | ±0.0984 | -0.801 | 0.4229 |  |
| Kidney disease | -0.0560 | 0.0815 | ±0.1629 | -0.687 | 0.4918 |  |
| **Circulatory disease** | **+0.2312** | 0.0904 | ±0.1809 | **+2.557** | **0.0106** | * |
| Glucose SD, pooled (mg/dL) | -0.0049 | 0.0035 | ±0.0069 | -1.419 | 0.1559 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.1467**, Adj R² = **0.1370**, F-statistic = **15.18** (p = **2.25e-34**), Residual SE = **0.858** on **1236** df, AIC = **3183.0**, BIC = **3259.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2996** | 0.2005 | ±0.4010 | **+11.470** | **1.86e-30** | *** |
| Education: graduate level (vs college) | -0.0134 | 0.0501 | ±0.1001 | -0.268 | 0.7887 |  |
| **Education: high school or below (vs college)** | **+0.5121** | 0.1214 | ±0.2428 | **+4.218** | **2.46e-05** | *** |
| Site: UCSD (vs UAB) | -0.0321 | 0.0659 | ±0.1319 | -0.486 | 0.6267 |  |
| **Site: UW (vs UAB)** | **-0.3765** | 0.0662 | ±0.1325 | **-5.685** | **1.31e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1603** | 0.0668 | ±0.1336 | **-2.399** | **0.0164** | * |
| Season: summer (vs autumn) | -0.0437 | 0.0732 | ±0.1464 | -0.596 | 0.5509 |  |
| Season: winter (vs autumn) | -0.0488 | 0.0703 | ±0.1406 | -0.694 | 0.4880 |  |
| **Age (years)** | **-0.0130** | 0.0023 | ±0.0045 | **-5.765** | **8.16e-09** | *** |
| **BMI (kg/m2)** | **+0.0187** | 0.0040 | ±0.0080 | **+4.682** | **2.84e-06** | *** |
| Hypertension | +0.0974 | 0.0570 | ±0.1141 | +1.707 | 0.0879 | . |
| High cholesterol | -0.0392 | 0.0492 | ±0.0984 | -0.797 | 0.4255 |  |
| Kidney disease | -0.0568 | 0.0816 | ±0.1632 | -0.696 | 0.4862 |  |
| **Circulatory disease** | **+0.2305** | 0.0905 | ±0.1810 | **+2.547** | **0.0109** | * |
| Avg. daily SD (mg/dL) | -0.0046 | 0.0038 | ±0.0076 | -1.194 | 0.2325 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1361**, F-statistic = **15.07** (p = **4.08e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.2**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2414** | 0.2111 | ±0.4222 | **+10.617** | **2.49e-26** | *** |
| Education: graduate level (vs college) | -0.0148 | 0.0501 | ±0.1003 | -0.294 | 0.7685 |  |
| **Education: high school or below (vs college)** | **+0.5101** | 0.1217 | ±0.2435 | **+4.190** | **2.79e-05** | *** |
| Site: UCSD (vs UAB) | -0.0291 | 0.0661 | ±0.1323 | -0.441 | 0.6595 |  |
| **Site: UW (vs UAB)** | **-0.3791** | 0.0660 | ±0.1320 | **-5.744** | **9.25e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1572** | 0.0667 | ±0.1335 | **-2.356** | **0.0185** | * |
| Season: summer (vs autumn) | -0.0402 | 0.0731 | ±0.1462 | -0.549 | 0.5829 |  |
| Season: winter (vs autumn) | -0.0455 | 0.0703 | ±0.1405 | -0.648 | 0.5169 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.820** | **5.90e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.653** | **3.28e-06** | *** |
| Hypertension | +0.0926 | 0.0567 | ±0.1134 | +1.633 | 0.1024 |  |
| High cholesterol | -0.0397 | 0.0493 | ±0.0987 | -0.804 | 0.4213 |  |
| Kidney disease | -0.0651 | 0.0822 | ±0.1645 | -0.791 | 0.4288 |  |
| **Circulatory disease** | **+0.2271** | 0.0905 | ±0.1810 | **+2.510** | **0.0121** | * |
| CV (%) | -0.0009 | 0.0059 | ±0.0118 | -0.159 | 0.8736 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1361**, F-statistic = **15.07** (p = **4.13e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.3**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2235** | 0.2289 | ±0.4577 | **+9.716** | **2.58e-22** | *** |
| Education: graduate level (vs college) | -0.0146 | 0.0502 | ±0.1003 | -0.290 | 0.7716 |  |
| **Education: high school or below (vs college)** | **+0.5106** | 0.1215 | ±0.2431 | **+4.201** | **2.66e-05** | *** |
| Site: UCSD (vs UAB) | -0.0285 | 0.0661 | ±0.1321 | -0.432 | 0.6658 |  |
| **Site: UW (vs UAB)** | **-0.3790** | 0.0661 | ±0.1323 | **-5.731** | **9.96e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1570** | 0.0668 | ±0.1336 | **-2.351** | **0.0187** | * |
| Season: summer (vs autumn) | -0.0401 | 0.0731 | ±0.1462 | -0.549 | 0.5831 |  |
| Season: winter (vs autumn) | -0.0456 | 0.0703 | ±0.1405 | -0.648 | 0.5168 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.824** | **5.74e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.653** | **3.27e-06** | *** |
| Hypertension | +0.0922 | 0.0567 | ±0.1134 | +1.627 | 0.1038 |  |
| High cholesterol | -0.0394 | 0.0493 | ±0.0986 | -0.798 | 0.4247 |  |
| Kidney disease | -0.0660 | 0.0822 | ±0.1643 | -0.803 | 0.4219 |  |
| **Circulatory disease** | **+0.2269** | 0.0905 | ±0.1810 | **+2.508** | **0.0121** | * |
| Mean / SD ratio | +0.0003 | 0.0191 | ±0.0383 | +0.016 | 0.9872 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.1459**, Adj R² = **0.1362**, F-statistic = **15.08** (p = **3.98e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.2**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2598** | 0.2277 | ±0.4554 | **+9.925** | **3.25e-23** | *** |
| Education: graduate level (vs college) | -0.0143 | 0.0501 | ±0.1002 | -0.286 | 0.7751 |  |
| **Education: high school or below (vs college)** | **+0.5106** | 0.1214 | ±0.2428 | **+4.207** | **2.59e-05** | *** |
| Site: UCSD (vs UAB) | -0.0277 | 0.0660 | ±0.1320 | -0.419 | 0.6749 |  |
| **Site: UW (vs UAB)** | **-0.3793** | 0.0662 | ±0.1324 | **-5.731** | **1.00e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1568** | 0.0668 | ±0.1336 | **-2.348** | **0.0189** | * |
| Season: summer (vs autumn) | -0.0396 | 0.0730 | ±0.1461 | -0.542 | 0.5879 |  |
| Season: winter (vs autumn) | -0.0457 | 0.0702 | ±0.1405 | -0.650 | 0.5154 |  |
| **Age (years)** | **-0.0133** | 0.0023 | ±0.0045 | **-5.842** | **5.17e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.644** | **3.42e-06** | *** |
| Hypertension | +0.0916 | 0.0567 | ±0.1135 | +1.614 | 0.1066 |  |
| High cholesterol | -0.0390 | 0.0493 | ±0.0986 | -0.790 | 0.4295 |  |
| Kidney disease | -0.0678 | 0.0825 | ±0.1649 | -0.822 | 0.4112 |  |
| **Circulatory disease** | **+0.2268** | 0.0905 | ±0.1810 | **+2.506** | **0.0122** | * |
| Avg. daily mean/SD | -0.0046 | 0.0158 | ±0.0315 | -0.292 | 0.7704 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1251**, R² = **0.1468**, Adj R² = **0.1372**, F-statistic = **15.20** (p = **2.02e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.7**, BIC = **3259.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0699** | 0.2214 | ±0.4428 | **+9.350** | **8.76e-21** | *** |
| Education: graduate level (vs college) | -0.0136 | 0.0500 | ±0.1000 | -0.271 | 0.7862 |  |
| **Education: high school or below (vs college)** | **+0.5079** | 0.1216 | ±0.2433 | **+4.176** | **2.97e-05** | *** |
| Site: UCSD (vs UAB) | -0.0228 | 0.0660 | ±0.1320 | -0.345 | 0.7300 |  |
| **Site: UW (vs UAB)** | **-0.3735** | 0.0662 | ±0.1325 | **-5.640** | **1.70e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1553** | 0.0667 | ±0.1334 | **-2.329** | **0.0199** | * |
| Season: summer (vs autumn) | -0.0372 | 0.0730 | ±0.1460 | -0.509 | 0.6108 |  |
| Season: winter (vs autumn) | -0.0432 | 0.0701 | ±0.1402 | -0.616 | 0.5380 |  |
| **Age (years)** | **-0.0131** | 0.0023 | ±0.0045 | **-5.820** | **5.88e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.636** | **3.55e-06** | *** |
| Hypertension | +0.0925 | 0.0567 | ±0.1135 | +1.630 | 0.1030 |  |
| High cholesterol | -0.0361 | 0.0494 | ±0.0989 | -0.730 | 0.4652 |  |
| Kidney disease | -0.0696 | 0.0820 | ±0.1640 | -0.849 | 0.3959 |  |
| **Circulatory disease** | **+0.2258** | 0.0902 | ±0.1803 | **+2.504** | **0.0123** | * |
| MAG (mg/dL/h) | +0.0038 | 0.0031 | ±0.0061 | +1.242 | 0.2143 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **1251**, R² = **0.1466**, Adj R² = **0.1369**, F-statistic = **15.16** (p = **2.46e-34**), Residual SE = **0.858** on **1236** df, AIC = **3183.2**, BIC = **3260.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.3187** | 0.2097 | ±0.4193 | **+11.059** | **1.98e-28** | *** |
| Education: graduate level (vs college) | -0.0134 | 0.0501 | ±0.1002 | -0.267 | 0.7896 |  |
| **Education: high school or below (vs college)** | **+0.5125** | 0.1215 | ±0.2430 | **+4.218** | **2.47e-05** | *** |
| Site: UCSD (vs UAB) | -0.0320 | 0.0658 | ±0.1317 | -0.487 | 0.6265 |  |
| **Site: UW (vs UAB)** | **-0.3779** | 0.0662 | ±0.1323 | **-5.711** | **1.12e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1595** | 0.0668 | ±0.1336 | **-2.388** | **0.0169** | * |
| Season: summer (vs autumn) | -0.0434 | 0.0731 | ±0.1462 | -0.594 | 0.5525 |  |
| Season: winter (vs autumn) | -0.0482 | 0.0703 | ±0.1406 | -0.685 | 0.4935 |  |
| **Age (years)** | **-0.0131** | 0.0023 | ±0.0045 | **-5.780** | **7.47e-09** | *** |
| **BMI (kg/m2)** | **+0.0185** | 0.0040 | ±0.0080 | **+4.630** | **3.65e-06** | *** |
| Hypertension | +0.0955 | 0.0569 | ±0.1138 | +1.680 | 0.0930 | . |
| High cholesterol | -0.0405 | 0.0492 | ±0.0985 | -0.822 | 0.4113 |  |
| Kidney disease | -0.0592 | 0.0816 | ±0.1631 | -0.726 | 0.4676 |  |
| **Circulatory disease** | **+0.2300** | 0.0905 | ±0.1810 | **+2.542** | **0.0110** | * |
| Avg. daily range (mg/dL) | -0.0010 | 0.0009 | ±0.0019 | -1.042 | 0.2976 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **1251**, R² = **0.1469**, Adj R² = **0.1372**, F-statistic = **15.20** (p = **1.93e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.6**, BIC = **3259.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2750** | 0.1905 | ±0.3811 | **+11.940** | **7.29e-33** | *** |
| Education: graduate level (vs college) | -0.0145 | 0.0501 | ±0.1001 | -0.290 | 0.7721 |  |
| **Education: high school or below (vs college)** | **+0.5103** | 0.1216 | ±0.2431 | **+4.198** | **2.69e-05** | *** |
| Site: UCSD (vs UAB) | -0.0326 | 0.0657 | ±0.1314 | -0.496 | 0.6201 |  |
| **Site: UW (vs UAB)** | **-0.3782** | 0.0661 | ±0.1322 | **-5.722** | **1.05e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1530** | 0.0670 | ±0.1341 | **-2.283** | **0.0225** | * |
| Season: summer (vs autumn) | -0.0367 | 0.0733 | ±0.1466 | -0.501 | 0.6162 |  |
| Season: winter (vs autumn) | -0.0438 | 0.0703 | ±0.1406 | -0.623 | 0.5334 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.823** | **5.77e-09** | *** |
| **BMI (kg/m2)** | **+0.0189** | 0.0040 | ±0.0081 | **+4.700** | **2.60e-06** | *** |
| Hypertension | +0.0934 | 0.0567 | ±0.1135 | +1.646 | 0.0997 | . |
| High cholesterol | -0.0380 | 0.0492 | ±0.0984 | -0.773 | 0.4397 |  |
| Kidney disease | -0.0656 | 0.0818 | ±0.1635 | -0.802 | 0.4224 |  |
| **Circulatory disease** | **+0.2309** | 0.0903 | ±0.1807 | **+2.556** | **0.0106** | * |
| SD of daily means (mg/dL) | -0.0094 | 0.0066 | ±0.0132 | -1.424 | 0.1545 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **1251**, R² = **0.1471**, Adj R² = **0.1375**, F-statistic = **15.23** (p = **1.66e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.3**, BIC = **3259.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8539** | 0.2784 | ±0.5568 | **+6.659** | **2.76e-11** | *** |
| Education: graduate level (vs college) | -0.0129 | 0.0500 | ±0.1001 | -0.257 | 0.7971 |  |
| **Education: high school or below (vs college)** | **+0.5156** | 0.1215 | ±0.2430 | **+4.244** | **2.20e-05** | *** |
| Site: UCSD (vs UAB) | -0.0337 | 0.0660 | ±0.1320 | -0.510 | 0.6101 |  |
| **Site: UW (vs UAB)** | **-0.3790** | 0.0659 | ±0.1319 | **-5.746** | **9.13e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1603** | 0.0668 | ±0.1336 | **-2.401** | **0.0164** | * |
| Season: summer (vs autumn) | -0.0465 | 0.0731 | ±0.1461 | -0.637 | 0.5244 |  |
| Season: winter (vs autumn) | -0.0488 | 0.0701 | ±0.1401 | -0.696 | 0.4865 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.829** | **5.59e-09** | *** |
| **BMI (kg/m2)** | **+0.0188** | 0.0040 | ±0.0080 | **+4.702** | **2.57e-06** | *** |
| Hypertension | +0.0960 | 0.0569 | ±0.1137 | +1.689 | 0.0913 | . |
| High cholesterol | -0.0378 | 0.0492 | ±0.0985 | -0.768 | 0.4424 |  |
| Kidney disease | -0.0592 | 0.0813 | ±0.1627 | -0.727 | 0.4670 |  |
| **Circulatory disease** | **+0.2319** | 0.0906 | ±0.1813 | **+2.559** | **0.0105** | * |
| Time in range 70-180, pooled (%) | +0.0038 | 0.0022 | ±0.0044 | +1.731 | 0.0834 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **1251**, R² = **0.1471**, Adj R² = **0.1374**, F-statistic = **15.23** (p = **1.69e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.3**, BIC = **3259.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8568** | 0.2789 | ±0.5578 | **+6.657** | **2.79e-11** | *** |
| Education: graduate level (vs college) | -0.0129 | 0.0500 | ±0.1001 | -0.257 | 0.7971 |  |
| **Education: high school or below (vs college)** | **+0.5151** | 0.1215 | ±0.2429 | **+4.241** | **2.23e-05** | *** |
| Site: UCSD (vs UAB) | -0.0334 | 0.0660 | ±0.1320 | -0.506 | 0.6125 |  |
| **Site: UW (vs UAB)** | **-0.3791** | 0.0660 | ±0.1319 | **-5.748** | **9.05e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1600** | 0.0668 | ±0.1336 | **-2.395** | **0.0166** | * |
| Season: summer (vs autumn) | -0.0465 | 0.0731 | ±0.1461 | -0.637 | 0.5244 |  |
| Season: winter (vs autumn) | -0.0486 | 0.0701 | ±0.1402 | -0.694 | 0.4878 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.827** | **5.66e-09** | *** |
| **BMI (kg/m2)** | **+0.0188** | 0.0040 | ±0.0080 | **+4.705** | **2.54e-06** | *** |
| Hypertension | +0.0959 | 0.0568 | ±0.1137 | +1.687 | 0.0916 | . |
| High cholesterol | -0.0376 | 0.0492 | ±0.0985 | -0.765 | 0.4446 |  |
| Kidney disease | -0.0592 | 0.0813 | ±0.1627 | -0.728 | 0.4668 |  |
| **Circulatory disease** | **+0.2319** | 0.0907 | ±0.1813 | **+2.558** | **0.0105** | * |
| Avg. daily time in range 70-180 (%) | +0.0038 | 0.0022 | ±0.0044 | +1.719 | 0.0856 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1361**, F-statistic = **15.07** (p = **4.08e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.2**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2296** | 0.1899 | ±0.3799 | **+11.738** | **8.10e-32** | *** |
| Education: graduate level (vs college) | -0.0149 | 0.0500 | ±0.1001 | -0.297 | 0.7665 |  |
| **Education: high school or below (vs college)** | **+0.5096** | 0.1226 | ±0.2451 | **+4.158** | **3.22e-05** | *** |
| Site: UCSD (vs UAB) | -0.0296 | 0.0661 | ±0.1322 | -0.448 | 0.6542 |  |
| **Site: UW (vs UAB)** | **-0.3795** | 0.0657 | ±0.1314 | **-5.774** | **7.72e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1570** | 0.0668 | ±0.1336 | **-2.351** | **0.0187** | * |
| Season: summer (vs autumn) | -0.0403 | 0.0731 | ±0.1461 | -0.552 | 0.5812 |  |
| Season: winter (vs autumn) | -0.0458 | 0.0703 | ±0.1406 | -0.651 | 0.5151 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.832** | **5.49e-09** | *** |
| **BMI (kg/m2)** | **+0.0187** | 0.0040 | ±0.0080 | **+4.638** | **3.52e-06** | *** |
| Hypertension | +0.0922 | 0.0568 | ±0.1135 | +1.624 | 0.1044 |  |
| High cholesterol | -0.0397 | 0.0494 | ±0.0987 | -0.805 | 0.4209 |  |
| Kidney disease | -0.0661 | 0.0820 | ±0.1639 | -0.806 | 0.4201 |  |
| **Circulatory disease** | **+0.2276** | 0.0904 | ±0.1808 | **+2.517** | **0.0118** | * |
| Any reading < 54 during wear (0/1) | -0.0078 | 0.0564 | ±0.1127 | -0.139 | 0.8893 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.1459**, Adj R² = **0.1362**, F-statistic = **15.08** (p = **3.82e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.1**, BIC = **3261.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2325** | 0.1903 | ±0.3806 | **+11.732** | **8.70e-32** | *** |
| Education: graduate level (vs college) | -0.0149 | 0.0500 | ±0.1001 | -0.298 | 0.7654 |  |
| **Education: high school or below (vs college)** | **+0.5087** | 0.1214 | ±0.2428 | **+4.191** | **2.78e-05** | *** |
| Site: UCSD (vs UAB) | -0.0317 | 0.0663 | ±0.1327 | -0.478 | 0.6330 |  |
| **Site: UW (vs UAB)** | **-0.3814** | 0.0661 | ±0.1322 | **-5.772** | **7.83e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1573** | 0.0668 | ±0.1335 | **-2.357** | **0.0184** | * |
| Season: summer (vs autumn) | -0.0395 | 0.0732 | ±0.1464 | -0.540 | 0.5894 |  |
| Season: winter (vs autumn) | -0.0453 | 0.0703 | ±0.1406 | -0.644 | 0.5198 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.844** | **5.11e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.646** | **3.38e-06** | *** |
| Hypertension | +0.0915 | 0.0567 | ±0.1134 | +1.614 | 0.1065 |  |
| High cholesterol | -0.0407 | 0.0495 | ±0.0991 | -0.822 | 0.4109 |  |
| Kidney disease | -0.0655 | 0.0819 | ±0.1639 | -0.800 | 0.4237 |  |
| **Circulatory disease** | **+0.2268** | 0.0904 | ±0.1807 | **+2.510** | **0.0121** | * |
| Time < 54 (%) | -0.0175 | 0.0316 | ±0.0632 | -0.554 | 0.5799 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.1459**, Adj R² = **0.1362**, F-statistic = **15.08** (p = **3.85e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.1**, BIC = **3261.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2301** | 0.1900 | ±0.3801 | **+11.734** | **8.49e-32** | *** |
| Education: graduate level (vs college) | -0.0151 | 0.0501 | ±0.1001 | -0.301 | 0.7632 |  |
| **Education: high school or below (vs college)** | **+0.5088** | 0.1215 | ±0.2430 | **+4.188** | **2.81e-05** | *** |
| Site: UCSD (vs UAB) | -0.0312 | 0.0663 | ±0.1325 | -0.470 | 0.6381 |  |
| **Site: UW (vs UAB)** | **-0.3817** | 0.0662 | ±0.1324 | **-5.764** | **8.23e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1570** | 0.0668 | ±0.1336 | **-2.351** | **0.0187** | * |
| Season: summer (vs autumn) | -0.0394 | 0.0732 | ±0.1463 | -0.539 | 0.5901 |  |
| Season: winter (vs autumn) | -0.0448 | 0.0703 | ±0.1406 | -0.637 | 0.5240 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.832** | **5.46e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.648** | **3.35e-06** | *** |
| Hypertension | +0.0912 | 0.0569 | ±0.1138 | +1.603 | 0.1090 |  |
| High cholesterol | -0.0405 | 0.0494 | ±0.0988 | -0.820 | 0.4121 |  |
| Kidney disease | -0.0656 | 0.0819 | ±0.1638 | -0.801 | 0.4234 |  |
| **Circulatory disease** | **+0.2267** | 0.0904 | ±0.1808 | **+2.507** | **0.0122** | * |
| Avg. daily time < 54 (%) | -0.0223 | 0.0429 | ±0.0859 | -0.520 | 0.6030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1361**, F-statistic = **15.07** (p = **4.10e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.2**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2275** | 0.1904 | ±0.3807 | **+11.701** | **1.26e-31** | *** |
| Education: graduate level (vs college) | -0.0148 | 0.0501 | ±0.1002 | -0.296 | 0.7672 |  |
| **Education: high school or below (vs college)** | **+0.5098** | 0.1224 | ±0.2447 | **+4.166** | **3.10e-05** | *** |
| Site: UCSD (vs UAB) | -0.0291 | 0.0664 | ±0.1328 | -0.438 | 0.6614 |  |
| **Site: UW (vs UAB)** | **-0.3797** | 0.0663 | ±0.1325 | **-5.731** | **1.00e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1569** | 0.0670 | ±0.1339 | **-2.343** | **0.0191** | * |
| Season: summer (vs autumn) | -0.0400 | 0.0732 | ±0.1465 | -0.546 | 0.5849 |  |
| Season: winter (vs autumn) | -0.0452 | 0.0706 | ±0.1412 | -0.640 | 0.5219 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.831** | **5.52e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.644** | **3.41e-06** | *** |
| Hypertension | +0.0919 | 0.0569 | ±0.1137 | +1.617 | 0.1060 |  |
| High cholesterol | -0.0397 | 0.0493 | ±0.0986 | -0.804 | 0.4211 |  |
| Kidney disease | -0.0661 | 0.0819 | ±0.1639 | -0.807 | 0.4198 |  |
| **Circulatory disease** | **+0.2269** | 0.0904 | ±0.1808 | **+2.510** | **0.0121** | * |
| Time 54-69, pooled (%) | -0.0020 | 0.0175 | ±0.0351 | -0.113 | 0.9102 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1361**, F-statistic = **15.07** (p = **4.12e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.3**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2263** | 0.1903 | ±0.3807 | **+11.698** | **1.31e-31** | *** |
| Education: graduate level (vs college) | -0.0147 | 0.0502 | ±0.1004 | -0.293 | 0.7694 |  |
| **Education: high school or below (vs college)** | **+0.5101** | 0.1225 | ±0.2450 | **+4.163** | **3.13e-05** | *** |
| Site: UCSD (vs UAB) | -0.0287 | 0.0662 | ±0.1325 | -0.434 | 0.6646 |  |
| **Site: UW (vs UAB)** | **-0.3794** | 0.0664 | ±0.1327 | **-5.716** | **1.09e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1569** | 0.0670 | ±0.1340 | **-2.343** | **0.0191** | * |
| Season: summer (vs autumn) | -0.0401 | 0.0732 | ±0.1463 | -0.548 | 0.5838 |  |
| Season: winter (vs autumn) | -0.0453 | 0.0706 | ±0.1412 | -0.642 | 0.5206 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.835** | **5.39e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.644** | **3.41e-06** | *** |
| Hypertension | +0.0920 | 0.0570 | ±0.1139 | +1.615 | 0.1062 |  |
| High cholesterol | -0.0395 | 0.0492 | ±0.0985 | -0.802 | 0.4225 |  |
| Kidney disease | -0.0661 | 0.0819 | ±0.1639 | -0.807 | 0.4199 |  |
| **Circulatory disease** | **+0.2269** | 0.0904 | ±0.1808 | **+2.510** | **0.0121** | * |
| Avg. daily time 54-69 (%) | -0.0011 | 0.0181 | ±0.0361 | -0.058 | 0.9534 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1362**, F-statistic = **15.07** (p = **4.03e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.2**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2299** | 0.1904 | ±0.3808 | **+11.712** | **1.10e-31** | *** |
| Education: graduate level (vs college) | -0.0151 | 0.0501 | ±0.1001 | -0.301 | 0.7633 |  |
| **Education: high school or below (vs college)** | **+0.5090** | 0.1222 | ±0.2444 | **+4.165** | **3.11e-05** | *** |
| Site: UCSD (vs UAB) | -0.0300 | 0.0666 | ±0.1331 | -0.450 | 0.6524 |  |
| **Site: UW (vs UAB)** | **-0.3805** | 0.0663 | ±0.1325 | **-5.742** | **9.37e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1569** | 0.0669 | ±0.1338 | **-2.346** | **0.0190** | * |
| Season: summer (vs autumn) | -0.0398 | 0.0733 | ±0.1465 | -0.544 | 0.5867 |  |
| Season: winter (vs autumn) | -0.0449 | 0.0706 | ±0.1411 | -0.637 | 0.5242 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.837** | **5.33e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.649** | **3.33e-06** | *** |
| Hypertension | +0.0917 | 0.0568 | ±0.1137 | +1.613 | 0.1067 |  |
| High cholesterol | -0.0401 | 0.0494 | ±0.0988 | -0.812 | 0.4170 |  |
| Kidney disease | -0.0660 | 0.0819 | ±0.1639 | -0.806 | 0.4203 |  |
| **Circulatory disease** | **+0.2269** | 0.0904 | ±0.1808 | **+2.510** | **0.0121** | * |
| Time < 70 (%) | -0.0031 | 0.0129 | ±0.0259 | -0.239 | 0.8111 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1361**, F-statistic = **15.07** (p = **4.08e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.2**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2278** | 0.1902 | ±0.3805 | **+11.710** | **1.13e-31** | *** |
| Education: graduate level (vs college) | -0.0150 | 0.0502 | ±0.1003 | -0.298 | 0.7656 |  |
| **Education: high school or below (vs college)** | **+0.5095** | 0.1224 | ±0.2448 | **+4.163** | **3.14e-05** | *** |
| Site: UCSD (vs UAB) | -0.0293 | 0.0664 | ±0.1327 | -0.441 | 0.6593 |  |
| **Site: UW (vs UAB)** | **-0.3800** | 0.0664 | ±0.1328 | **-5.722** | **1.05e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1569** | 0.0669 | ±0.1339 | **-2.344** | **0.0191** | * |
| Season: summer (vs autumn) | -0.0400 | 0.0732 | ±0.1464 | -0.546 | 0.5849 |  |
| Season: winter (vs autumn) | -0.0450 | 0.0705 | ±0.1411 | -0.638 | 0.5233 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.839** | **5.27e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.648** | **3.35e-06** | *** |
| Hypertension | +0.0918 | 0.0570 | ±0.1140 | +1.610 | 0.1073 |  |
| High cholesterol | -0.0398 | 0.0493 | ±0.0985 | -0.807 | 0.4196 |  |
| Kidney disease | -0.0661 | 0.0819 | ±0.1639 | -0.806 | 0.4200 |  |
| **Circulatory disease** | **+0.2269** | 0.0904 | ±0.1808 | **+2.510** | **0.0121** | * |
| Avg. daily time < 70 (%) | -0.0022 | 0.0143 | ±0.0287 | -0.151 | 0.8797 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.1462**, Adj R² = **0.1365**, F-statistic = **15.12** (p = **3.16e-34**), Residual SE = **0.859** on **1236** df, AIC = **3183.7**, BIC = **3260.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8553** | 0.2606 | ±0.5212 | **+7.119** | **1.08e-12** | *** |
| Education: graduate level (vs college) | -0.0143 | 0.0501 | ±0.1001 | -0.286 | 0.7751 |  |
| **Education: high school or below (vs college)** | **+0.5156** | 0.1222 | ±0.2444 | **+4.220** | **2.44e-05** | *** |
| Site: UCSD (vs UAB) | -0.0301 | 0.0660 | ±0.1319 | -0.457 | 0.6480 |  |
| **Site: UW (vs UAB)** | **-0.3800** | 0.0660 | ±0.1321 | **-5.754** | **8.71e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1577** | 0.0668 | ±0.1336 | **-2.362** | **0.0182** | * |
| Season: summer (vs autumn) | -0.0421 | 0.0731 | ±0.1462 | -0.575 | 0.5650 |  |
| Season: winter (vs autumn) | -0.0462 | 0.0702 | ±0.1404 | -0.658 | 0.5107 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.847** | **5.00e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.657** | **3.21e-06** | *** |
| Hypertension | +0.0926 | 0.0567 | ±0.1134 | +1.632 | 0.1026 |  |
| High cholesterol | -0.0401 | 0.0492 | ±0.0985 | -0.813 | 0.4160 |  |
| Kidney disease | -0.0653 | 0.0817 | ±0.1634 | -0.799 | 0.4240 |  |
| **Circulatory disease** | **+0.2308** | 0.0909 | ±0.1817 | **+2.539** | **0.0111** | * |
| Time 54-250, pooled (%) | +0.0037 | 0.0020 | ±0.0040 | +1.885 | 0.0594 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.1462**, Adj R² = **0.1365**, F-statistic = **15.11** (p = **3.21e-34**), Residual SE = **0.859** on **1236** df, AIC = **3183.7**, BIC = **3260.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8580** | 0.2603 | ±0.5206 | **+7.138** | **9.48e-13** | *** |
| Education: graduate level (vs college) | -0.0143 | 0.0501 | ±0.1001 | -0.286 | 0.7751 |  |
| **Education: high school or below (vs college)** | **+0.5156** | 0.1222 | ±0.2444 | **+4.219** | **2.45e-05** | *** |
| Site: UCSD (vs UAB) | -0.0299 | 0.0659 | ±0.1319 | -0.453 | 0.6505 |  |
| **Site: UW (vs UAB)** | **-0.3799** | 0.0660 | ±0.1321 | **-5.753** | **8.78e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1577** | 0.0668 | ±0.1336 | **-2.361** | **0.0182** | * |
| Season: summer (vs autumn) | -0.0421 | 0.0731 | ±0.1462 | -0.575 | 0.5651 |  |
| Season: winter (vs autumn) | -0.0462 | 0.0702 | ±0.1404 | -0.658 | 0.5106 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.846** | **5.05e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.659** | **3.18e-06** | *** |
| Hypertension | +0.0925 | 0.0567 | ±0.1134 | +1.632 | 0.1026 |  |
| High cholesterol | -0.0400 | 0.0492 | ±0.0985 | -0.812 | 0.4170 |  |
| Kidney disease | -0.0655 | 0.0817 | ±0.1635 | -0.801 | 0.4232 |  |
| **Circulatory disease** | **+0.2307** | 0.0909 | ±0.1818 | **+2.538** | **0.0111** | * |
| Avg. daily time 54-250 (%) | +0.0037 | 0.0020 | ±0.0039 | +1.891 | 0.0586 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.1472**, Adj R² = **0.1375**, F-statistic = **15.23** (p = **1.64e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.3**, BIC = **3259.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2282** | 0.1902 | ±0.3803 | **+11.718** | **1.03e-31** | *** |
| Education: graduate level (vs college) | -0.0116 | 0.0500 | ±0.1000 | -0.231 | 0.8171 |  |
| **Education: high school or below (vs college)** | **+0.5126** | 0.1212 | ±0.2424 | **+4.229** | **2.34e-05** | *** |
| Site: UCSD (vs UAB) | -0.0320 | 0.0658 | ±0.1317 | -0.486 | 0.6273 |  |
| **Site: UW (vs UAB)** | **-0.3755** | 0.0660 | ±0.1321 | **-5.687** | **1.29e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1611** | 0.0670 | ±0.1340 | **-2.405** | **0.0162** | * |
| Season: summer (vs autumn) | -0.0469 | 0.0732 | ±0.1465 | -0.640 | 0.5221 |  |
| Season: winter (vs autumn) | -0.0504 | 0.0701 | ±0.1402 | -0.719 | 0.4719 |  |
| **Age (years)** | **-0.0131** | 0.0023 | ±0.0045 | **-5.805** | **6.42e-09** | *** |
| **BMI (kg/m2)** | **+0.0188** | 0.0040 | ±0.0080 | **+4.712** | **2.46e-06** | *** |
| Hypertension | +0.0979 | 0.0571 | ±0.1143 | +1.714 | 0.0866 | . |
| High cholesterol | -0.0351 | 0.0494 | ±0.0988 | -0.710 | 0.4775 |  |
| Kidney disease | -0.0569 | 0.0816 | ±0.1631 | -0.698 | 0.4854 |  |
| **Circulatory disease** | **+0.2285** | 0.0903 | ±0.1805 | **+2.532** | **0.0114** | * |
| Time 181-250, pooled (%) | -0.0056 | 0.0042 | ±0.0084 | -1.348 | 0.1776 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1251**, R² = **0.1472**, Adj R² = **0.1375**, F-statistic = **15.24** (p = **1.60e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.2**, BIC = **3259.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2280** | 0.1901 | ±0.3803 | **+11.718** | **1.03e-31** | *** |
| Education: graduate level (vs college) | -0.0114 | 0.0500 | ±0.1001 | -0.229 | 0.8190 |  |
| **Education: high school or below (vs college)** | **+0.5121** | 0.1212 | ±0.2424 | **+4.225** | **2.39e-05** | *** |
| Site: UCSD (vs UAB) | -0.0324 | 0.0658 | ±0.1317 | -0.492 | 0.6226 |  |
| **Site: UW (vs UAB)** | **-0.3759** | 0.0660 | ±0.1321 | **-5.693** | **1.25e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1607** | 0.0670 | ±0.1339 | **-2.400** | **0.0164** | * |
| Season: summer (vs autumn) | -0.0468 | 0.0732 | ±0.1464 | -0.640 | 0.5223 |  |
| Season: winter (vs autumn) | -0.0505 | 0.0701 | ±0.1402 | -0.720 | 0.4718 |  |
| **Age (years)** | **-0.0131** | 0.0023 | ±0.0045 | **-5.808** | **6.31e-09** | *** |
| **BMI (kg/m2)** | **+0.0189** | 0.0040 | ±0.0080 | **+4.714** | **2.43e-06** | *** |
| Hypertension | +0.0979 | 0.0572 | ±0.1143 | +1.713 | 0.0867 | . |
| High cholesterol | -0.0350 | 0.0494 | ±0.0988 | -0.709 | 0.4785 |  |
| Kidney disease | -0.0566 | 0.0815 | ±0.1631 | -0.694 | 0.4876 |  |
| **Circulatory disease** | **+0.2286** | 0.0903 | ±0.1805 | **+2.533** | **0.0113** | * |
| Avg. daily time 181-250 (%) | -0.0056 | 0.0042 | ±0.0083 | -1.357 | 0.1749 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **1251**, R² = **0.1470**, Adj R² = **0.1374**, F-statistic = **15.22** (p = **1.75e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.4**, BIC = **3259.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2301** | 0.1902 | ±0.3804 | **+11.726** | **9.42e-32** | *** |
| Education: graduate level (vs college) | -0.0123 | 0.0500 | ±0.1001 | -0.245 | 0.8062 |  |
| **Education: high school or below (vs college)** | **+0.5173** | 0.1216 | ±0.2433 | **+4.253** | **2.11e-05** | *** |
| Site: UCSD (vs UAB) | -0.0317 | 0.0659 | ±0.1318 | -0.481 | 0.6304 |  |
| **Site: UW (vs UAB)** | **-0.3772** | 0.0659 | ±0.1319 | **-5.720** | **1.07e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1603** | 0.0669 | ±0.1337 | **-2.398** | **0.0165** | * |
| Season: summer (vs autumn) | -0.0466 | 0.0732 | ±0.1464 | -0.637 | 0.5242 |  |
| Season: winter (vs autumn) | -0.0494 | 0.0701 | ±0.1401 | -0.705 | 0.4806 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.824** | **5.76e-09** | *** |
| **BMI (kg/m2)** | **+0.0188** | 0.0040 | ±0.0080 | **+4.699** | **2.61e-06** | *** |
| Hypertension | +0.0965 | 0.0569 | ±0.1138 | +1.696 | 0.0899 | . |
| High cholesterol | -0.0370 | 0.0493 | ±0.0985 | -0.750 | 0.4530 |  |
| Kidney disease | -0.0594 | 0.0813 | ±0.1627 | -0.731 | 0.4651 |  |
| **Circulatory disease** | **+0.2318** | 0.0906 | ±0.1813 | **+2.557** | **0.0105** | * |
| Time > 180 (%) | -0.0037 | 0.0022 | ±0.0044 | -1.675 | 0.0940 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.1471**, Adj R² = **0.1374**, F-statistic = **15.22** (p = **1.74e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.4**, BIC = **3259.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2296** | 0.1901 | ±0.3803 | **+11.726** | **9.40e-32** | *** |
| Education: graduate level (vs college) | -0.0122 | 0.0500 | ±0.1001 | -0.243 | 0.8077 |  |
| **Education: high school or below (vs college)** | **+0.5169** | 0.1216 | ±0.2432 | **+4.251** | **2.13e-05** | *** |
| Site: UCSD (vs UAB) | -0.0320 | 0.0659 | ±0.1318 | -0.486 | 0.6271 |  |
| **Site: UW (vs UAB)** | **-0.3774** | 0.0660 | ±0.1319 | **-5.722** | **1.05e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1601** | 0.0668 | ±0.1337 | **-2.395** | **0.0166** | * |
| Season: summer (vs autumn) | -0.0466 | 0.0732 | ±0.1464 | -0.637 | 0.5243 |  |
| Season: winter (vs autumn) | -0.0495 | 0.0701 | ±0.1402 | -0.707 | 0.4798 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.825** | **5.71e-09** | *** |
| **BMI (kg/m2)** | **+0.0188** | 0.0040 | ±0.0080 | **+4.703** | **2.57e-06** | *** |
| Hypertension | +0.0965 | 0.0569 | ±0.1138 | +1.695 | 0.0900 | . |
| High cholesterol | -0.0369 | 0.0492 | ±0.0985 | -0.750 | 0.4534 |  |
| Kidney disease | -0.0593 | 0.0813 | ±0.1627 | -0.729 | 0.4659 |  |
| **Circulatory disease** | **+0.2319** | 0.0906 | ±0.1813 | **+2.558** | **0.0105** | * |
| Avg. daily time > 180 (%) | -0.0037 | 0.0022 | ±0.0044 | -1.682 | 0.0926 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.1463**, Adj R² = **0.1367**, F-statistic = **15.13** (p = **2.84e-34**), Residual SE = **0.859** on **1236** df, AIC = **3183.5**, BIC = **3260.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2234** | 0.1900 | ±0.3801 | **+11.701** | **1.27e-31** | *** |
| Education: graduate level (vs college) | -0.0144 | 0.0501 | ±0.1001 | -0.287 | 0.7742 |  |
| **Education: high school or below (vs college)** | **+0.5146** | 0.1217 | ±0.2435 | **+4.227** | **2.37e-05** | *** |
| Site: UCSD (vs UAB) | -0.0299 | 0.0658 | ±0.1317 | -0.455 | 0.6495 |  |
| **Site: UW (vs UAB)** | **-0.3783** | 0.0660 | ±0.1320 | **-5.733** | **9.85e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1570** | 0.0668 | ±0.1335 | **-2.351** | **0.0187** | * |
| Season: summer (vs autumn) | -0.0436 | 0.0733 | ±0.1466 | -0.595 | 0.5519 |  |
| Season: winter (vs autumn) | -0.0461 | 0.0701 | ±0.1403 | -0.658 | 0.5105 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.840** | **5.21e-09** | *** |
| **BMI (kg/m2)** | **+0.0189** | 0.0040 | ±0.0081 | **+4.697** | **2.64e-06** | *** |
| Hypertension | +0.0936 | 0.0568 | ±0.1135 | +1.649 | 0.0992 | . |
| High cholesterol | -0.0371 | 0.0493 | ±0.0986 | -0.751 | 0.4524 |  |
| Kidney disease | -0.0662 | 0.0817 | ±0.1633 | -0.811 | 0.4176 |  |
| **Circulatory disease** | **+0.2283** | 0.0905 | ±0.1810 | **+2.523** | **0.0116** | * |
| Nocturnal time > 180 (%) | -0.0026 | 0.0022 | ±0.0044 | -1.170 | 0.2420 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.1464**, Adj R² = **0.1367**, F-statistic = **15.14** (p = **2.81e-34**), Residual SE = **0.859** on **1236** df, AIC = **3183.4**, BIC = **3260.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2411** | 0.1921 | ±0.3842 | **+11.667** | **1.89e-31** | *** |
| Education: graduate level (vs college) | -0.0150 | 0.0501 | ±0.1001 | -0.299 | 0.7649 |  |
| **Education: high school or below (vs college)** | **+0.5104** | 0.1213 | ±0.2427 | **+4.206** | **2.60e-05** | *** |
| Site: UCSD (vs UAB) | -0.0297 | 0.0659 | ±0.1317 | -0.451 | 0.6522 |  |
| **Site: UW (vs UAB)** | **-0.3781** | 0.0662 | ±0.1323 | **-5.715** | **1.10e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1603** | 0.0670 | ±0.1340 | **-2.393** | **0.0167** | * |
| Season: summer (vs autumn) | -0.0427 | 0.0732 | ±0.1464 | -0.584 | 0.5594 |  |
| Season: winter (vs autumn) | -0.0483 | 0.0703 | ±0.1406 | -0.687 | 0.4924 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.825** | **5.71e-09** | *** |
| **BMI (kg/m2)** | **+0.0184** | 0.0040 | ±0.0080 | **+4.580** | **4.65e-06** | *** |
| Hypertension | +0.0955 | 0.0571 | ±0.1143 | +1.672 | 0.0946 | . |
| High cholesterol | -0.0384 | 0.0493 | ±0.0985 | -0.779 | 0.4358 |  |
| Kidney disease | -0.0647 | 0.0817 | ±0.1633 | -0.793 | 0.4281 |  |
| **Circulatory disease** | **+0.2265** | 0.0903 | ±0.1806 | **+2.507** | **0.0122** | * |
| Any reading > 250 during wear (0/1) | -0.0559 | 0.0606 | ±0.1212 | -0.923 | 0.3562 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.1461**, Adj R² = **0.1365**, F-statistic = **15.11** (p = **3.25e-34**), Residual SE = **0.859** on **1236** df, AIC = **3183.8**, BIC = **3260.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2282** | 0.1903 | ±0.3806 | **+11.708** | **1.16e-31** | *** |
| Education: graduate level (vs college) | -0.0142 | 0.0501 | ±0.1001 | -0.284 | 0.7761 |  |
| **Education: high school or below (vs college)** | **+0.5157** | 0.1223 | ±0.2445 | **+4.218** | **2.47e-05** | *** |
| Site: UCSD (vs UAB) | -0.0294 | 0.0659 | ±0.1318 | -0.446 | 0.6558 |  |
| **Site: UW (vs UAB)** | **-0.3795** | 0.0660 | ±0.1320 | **-5.748** | **9.04e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1576** | 0.0668 | ±0.1336 | **-2.360** | **0.0183** | * |
| Season: summer (vs autumn) | -0.0421 | 0.0731 | ±0.1463 | -0.575 | 0.5650 |  |
| Season: winter (vs autumn) | -0.0462 | 0.0702 | ±0.1404 | -0.658 | 0.5104 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.846** | **5.04e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.658** | **3.20e-06** | *** |
| Hypertension | +0.0927 | 0.0567 | ±0.1134 | +1.635 | 0.1022 |  |
| High cholesterol | -0.0397 | 0.0492 | ±0.0985 | -0.807 | 0.4196 |  |
| Kidney disease | -0.0655 | 0.0817 | ±0.1635 | -0.801 | 0.4231 |  |
| **Circulatory disease** | **+0.2306** | 0.0909 | ±0.1818 | **+2.537** | **0.0112** | * |
| Time > 250 (%) | -0.0035 | 0.0019 | ±0.0038 | -1.853 | 0.0639 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.1461**, Adj R² = **0.1365**, F-statistic = **15.11** (p = **3.28e-34**), Residual SE = **0.859** on **1236** df, AIC = **3183.8**, BIC = **3260.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2279** | 0.1903 | ±0.3806 | **+11.708** | **1.15e-31** | *** |
| Education: graduate level (vs college) | -0.0142 | 0.0501 | ±0.1001 | -0.284 | 0.7762 |  |
| **Education: high school or below (vs college)** | **+0.5157** | 0.1223 | ±0.2446 | **+4.217** | **2.47e-05** | *** |
| Site: UCSD (vs UAB) | -0.0294 | 0.0659 | ±0.1318 | -0.446 | 0.6557 |  |
| **Site: UW (vs UAB)** | **-0.3794** | 0.0660 | ±0.1320 | **-5.748** | **9.06e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1576** | 0.0668 | ±0.1336 | **-2.360** | **0.0183** | * |
| Season: summer (vs autumn) | -0.0421 | 0.0731 | ±0.1463 | -0.576 | 0.5649 |  |
| Season: winter (vs autumn) | -0.0463 | 0.0702 | ±0.1404 | -0.659 | 0.5097 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.845** | **5.05e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.659** | **3.17e-06** | *** |
| Hypertension | +0.0927 | 0.0567 | ±0.1134 | +1.635 | 0.1021 |  |
| High cholesterol | -0.0398 | 0.0492 | ±0.0985 | -0.807 | 0.4194 |  |
| Kidney disease | -0.0656 | 0.0818 | ±0.1635 | -0.802 | 0.4226 |  |
| **Circulatory disease** | **+0.2306** | 0.0909 | ±0.1818 | **+2.537** | **0.0112** | * |
| Avg. daily time > 250 (%) | -0.0036 | 0.0019 | ±0.0038 | -1.864 | 0.0623 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 1,251; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **1251**, R² = **0.3174**, Adj R² = **0.3103**, F-statistic = **44.25** (p = **3.88e-93**), Residual SE = **1.890** on **1237** df, AIC = **5156.2**, BIC = **5228.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8847** | 0.4341 | ±0.8683 | **+55.015** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1589 | 0.1132 | ±0.2265 | -1.403 | 0.1606 |  |
| Education: high school or below (vs college) | +0.1216 | 0.2214 | ±0.4428 | +0.549 | 0.5829 |  |
| Site: UCSD (vs UAB) | -0.0636 | 0.1418 | ±0.2837 | -0.448 | 0.6538 |  |
| **Site: UW (vs UAB)** | **-0.8944** | 0.1332 | ±0.2663 | **-6.716** | **1.86e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4696** | 0.1503 | ±0.3007 | **-3.124** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9790** | 0.1785 | ±0.3570 | **+11.087** | **1.45e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3873** | 0.1499 | ±0.2998 | **-9.254** | **2.17e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.313** | **0.0207** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0166 | +0.635 | 0.5254 |  |
| Hypertension | +0.2067 | 0.1216 | ±0.2432 | +1.699 | 0.0892 | . |
| High cholesterol | -0.0626 | 0.1138 | ±0.2277 | -0.549 | 0.5827 |  |
| **Kidney disease** | **+0.4715** | 0.2080 | ±0.4160 | **+2.267** | **0.0234** | * |
| Circulatory disease | +0.2936 | 0.1740 | ±0.3480 | +1.687 | 0.0916 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **1251**, R² = **0.3175**, Adj R² = **0.3097**, F-statistic = **41.06** (p = **2.60e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.2**, BIC = **5235.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7931** | 0.7532 | ±1.5064 | **+31.589** | **5.31e-219** | *** |
| Education: graduate level (vs college) | -0.1591 | 0.1134 | ±0.2269 | -1.402 | 0.1608 |  |
| Education: high school or below (vs college) | +0.1187 | 0.2239 | ±0.4479 | +0.530 | 0.5960 |  |
| Site: UCSD (vs UAB) | -0.0640 | 0.1419 | ±0.2839 | -0.451 | 0.6520 |  |
| **Site: UW (vs UAB)** | **-0.8951** | 0.1334 | ±0.2669 | **-6.708** | **1.98e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4673** | 0.1517 | ±0.3034 | **-3.081** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.9797** | 0.1787 | ±0.3574 | **+11.079** | **1.58e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3863** | 0.1503 | ±0.3005 | **-9.226** | **2.81e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0103 | **+2.278** | **0.0227** | * |
| BMI (kg/m2) | +0.0052 | 0.0083 | ±0.0166 | +0.620 | 0.5351 |  |
| Hypertension | +0.2056 | 0.1221 | ±0.2442 | +1.684 | 0.0922 | . |
| High cholesterol | -0.0645 | 0.1149 | ±0.2298 | -0.562 | 0.5744 |  |
| **Kidney disease** | **+0.4716** | 0.2081 | ±0.4162 | **+2.266** | **0.0235** | * |
| Circulatory disease | +0.2923 | 0.1745 | ±0.3491 | +1.675 | 0.0939 | . |
| HbA1c (%) | +0.0178 | 0.1196 | ±0.2392 | +0.149 | 0.8816 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **1251**, R² = **0.3174**, Adj R² = **0.3097**, F-statistic = **41.06** (p = **2.63e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.2**, BIC = **5235.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8701** | 0.5393 | ±1.0786 | **+44.262** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1592 | 0.1135 | ±0.2269 | -1.403 | 0.1606 |  |
| Education: high school or below (vs college) | +0.1208 | 0.2228 | ±0.4456 | +0.542 | 0.5876 |  |
| Site: UCSD (vs UAB) | -0.0635 | 0.1419 | ±0.2838 | -0.447 | 0.6546 |  |
| **Site: UW (vs UAB)** | **-0.8948** | 0.1339 | ±0.2679 | **-6.681** | **2.38e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4694** | 0.1508 | ±0.3015 | **-3.113** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9794** | 0.1785 | ±0.3570 | **+11.090** | **1.41e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3869** | 0.1502 | ±0.3005 | **-9.232** | **2.66e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.307** | **0.0210** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0167 | +0.632 | 0.5272 |  |
| Hypertension | +0.2062 | 0.1220 | ±0.2440 | +1.691 | 0.0909 | . |
| High cholesterol | -0.0628 | 0.1142 | ±0.2283 | -0.550 | 0.5822 |  |
| **Kidney disease** | **+0.4711** | 0.2082 | ±0.4164 | **+2.262** | **0.0237** | * |
| Circulatory disease | +0.2932 | 0.1747 | ±0.3494 | +1.678 | 0.0933 | . |
| Mean glucose (mg/dL) | +0.0001 | 0.0029 | ±0.0058 | +0.046 | 0.9630 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **1251**, R² = **0.3174**, Adj R² = **0.3097**, F-statistic = **41.06** (p = **2.63e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.2**, BIC = **5235.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8516** | 0.8393 | ±1.6785 | **+28.420** | **1.15e-177** | *** |
| Education: graduate level (vs college) | -0.1592 | 0.1135 | ±0.2269 | -1.403 | 0.1606 |  |
| Education: high school or below (vs college) | +0.1208 | 0.2228 | ±0.4456 | +0.542 | 0.5876 |  |
| Site: UCSD (vs UAB) | -0.0635 | 0.1419 | ±0.2838 | -0.447 | 0.6546 |  |
| **Site: UW (vs UAB)** | **-0.8948** | 0.1339 | ±0.2679 | **-6.681** | **2.38e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4694** | 0.1508 | ±0.3015 | **-3.113** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9794** | 0.1785 | ±0.3570 | **+11.090** | **1.41e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3869** | 0.1502 | ±0.3005 | **-9.232** | **2.66e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.307** | **0.0210** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0167 | +0.632 | 0.5272 |  |
| Hypertension | +0.2062 | 0.1220 | ±0.2440 | +1.691 | 0.0909 | . |
| High cholesterol | -0.0628 | 0.1142 | ±0.2283 | -0.550 | 0.5822 |  |
| **Kidney disease** | **+0.4711** | 0.2082 | ±0.4164 | **+2.262** | **0.0237** | * |
| Circulatory disease | +0.2932 | 0.1747 | ±0.3494 | +1.678 | 0.0933 | . |
| GMI (%) | +0.0056 | 0.1204 | ±0.2408 | +0.046 | 0.9630 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **1251**, R² = **0.3175**, Adj R² = **0.3098**, F-statistic = **41.07** (p = **2.52e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.1**, BIC = **5235.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9726** | 0.5284 | ±1.0568 | **+45.368** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1576 | 0.1134 | ±0.2267 | -1.390 | 0.1645 |  |
| Education: high school or below (vs college) | +0.1264 | 0.2229 | ±0.4459 | +0.567 | 0.5709 |  |
| Site: UCSD (vs UAB) | -0.0631 | 0.1421 | ±0.2842 | -0.444 | 0.6568 |  |
| **Site: UW (vs UAB)** | **-0.8922** | 0.1338 | ±0.2677 | **-6.667** | **2.61e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4698** | 0.1504 | ±0.3009 | **-3.123** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9768** | 0.1786 | ±0.3572 | **+11.069** | **1.78e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3884** | 0.1502 | ±0.3004 | **-9.245** | **2.35e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.307** | **0.0211** | * |
| BMI (kg/m2) | +0.0056 | 0.0084 | ±0.0168 | +0.668 | 0.5041 |  |
| Hypertension | +0.2091 | 0.1218 | ±0.2436 | +1.716 | 0.0861 | . |
| High cholesterol | -0.0603 | 0.1143 | ±0.2287 | -0.528 | 0.5978 |  |
| **Kidney disease** | **+0.4719** | 0.2082 | ±0.4165 | **+2.266** | **0.0234** | * |
| Circulatory disease | +0.2951 | 0.1744 | ±0.3488 | +1.692 | 0.0906 | . |
| Nocturnal mean 00-06h (mg/dL) | -0.0008 | 0.0028 | ±0.0056 | -0.297 | 0.7667 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.3176**, Adj R² = **0.3099**, F-statistic = **41.09** (p = **2.30e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.9**, BIC = **5234.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9667** | 0.4661 | ±0.9322 | **+51.418** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1582 | 0.1134 | ±0.2268 | -1.395 | 0.1630 |  |
| Education: high school or below (vs college) | +0.1230 | 0.2214 | ±0.4429 | +0.555 | 0.5786 |  |
| Site: UCSD (vs UAB) | -0.0677 | 0.1418 | ±0.2836 | -0.478 | 0.6329 |  |
| **Site: UW (vs UAB)** | **-0.8922** | 0.1337 | ±0.2673 | **-6.675** | **2.47e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4724** | 0.1506 | ±0.3011 | **-3.137** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9762** | 0.1786 | ±0.3573 | **+11.063** | **1.89e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3898** | 0.1502 | ±0.3003 | **-9.256** | **2.12e-20** | *** |
| **Age (years)** | **+0.0119** | 0.0051 | ±0.0101 | **+2.351** | **0.0187** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0167 | +0.640 | 0.5223 |  |
| Hypertension | +0.2122 | 0.1221 | ±0.2442 | +1.738 | 0.0822 | . |
| High cholesterol | -0.0626 | 0.1140 | ±0.2279 | -0.550 | 0.5825 |  |
| **Kidney disease** | **+0.4805** | 0.2097 | ±0.4194 | **+2.292** | **0.0219** | * |
| Circulatory disease | +0.2974 | 0.1745 | ±0.3490 | +1.704 | 0.0883 | . |
| Glucose SD, pooled (mg/dL) | -0.0044 | 0.0084 | ±0.0169 | -0.520 | 0.6030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.3176**, Adj R² = **0.3099**, F-statistic = **41.10** (p = **2.21e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.8**, BIC = **5234.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9704** | 0.4630 | ±0.9260 | **+51.770** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1576 | 0.1134 | ±0.2268 | -1.390 | 0.1645 |  |
| Education: high school or below (vs college) | +0.1234 | 0.2214 | ±0.4429 | +0.557 | 0.5774 |  |
| Site: UCSD (vs UAB) | -0.0678 | 0.1418 | ±0.2836 | -0.478 | 0.6327 |  |
| **Site: UW (vs UAB)** | **-0.8915** | 0.1337 | ±0.2674 | **-6.667** | **2.62e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4734** | 0.1506 | ±0.3012 | **-3.143** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9749** | 0.1788 | ±0.3576 | **+11.047** | **2.28e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3910** | 0.1501 | ±0.3003 | **-9.265** | **1.96e-20** | *** |
| **Age (years)** | **+0.0120** | 0.0051 | ±0.0101 | **+2.361** | **0.0182** | * |
| BMI (kg/m2) | +0.0054 | 0.0083 | ±0.0167 | +0.647 | 0.5173 |  |
| Hypertension | +0.2127 | 0.1221 | ±0.2442 | +1.742 | 0.0815 | . |
| High cholesterol | -0.0624 | 0.1139 | ±0.2279 | -0.548 | 0.5839 |  |
| **Kidney disease** | **+0.4822** | 0.2096 | ±0.4192 | **+2.300** | **0.0214** | * |
| Circulatory disease | +0.2977 | 0.1744 | ±0.3488 | +1.707 | 0.0879 | . |
| Avg. daily SD (mg/dL) | -0.0053 | 0.0089 | ±0.0178 | -0.592 | 0.5540 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **1251**, R² = **0.3177**, Adj R² = **0.3099**, F-statistic = **41.10** (p = **2.15e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.8**, BIC = **5234.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0300** | 0.4960 | ±0.9920 | **+48.445** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1609 | 0.1134 | ±0.2268 | -1.419 | 0.1558 |  |
| Education: high school or below (vs college) | +0.1168 | 0.2213 | ±0.4426 | +0.528 | 0.5975 |  |
| Site: UCSD (vs UAB) | -0.0696 | 0.1417 | ±0.2835 | -0.491 | 0.6235 |  |
| **Site: UW (vs UAB)** | **-0.8952** | 0.1332 | ±0.2663 | **-6.723** | **1.79e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4717** | 0.1503 | ±0.3007 | **-3.137** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9786** | 0.1785 | ±0.3570 | **+11.084** | **1.50e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3870** | 0.1499 | ±0.2998 | **-9.251** | **2.22e-20** | *** |
| **Age (years)** | **+0.0120** | 0.0051 | ±0.0101 | **+2.360** | **0.0183** | * |
| BMI (kg/m2) | +0.0052 | 0.0083 | ±0.0167 | +0.623 | 0.5330 |  |
| Hypertension | +0.2105 | 0.1218 | ±0.2436 | +1.728 | 0.0839 | . |
| High cholesterol | -0.0656 | 0.1139 | ±0.2278 | -0.576 | 0.5646 |  |
| **Kidney disease** | **+0.4806** | 0.2096 | ±0.4192 | **+2.293** | **0.0218** | * |
| Circulatory disease | +0.2955 | 0.1741 | ±0.3483 | +1.697 | 0.0897 | . |
| CV (%) | -0.0085 | 0.0135 | ±0.0271 | -0.630 | 0.5287 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1251**, R² = **0.3182**, Adj R² = **0.3105**, F-statistic = **41.21** (p = **1.32e-92**), Residual SE = **1.889** on **1236** df, AIC = **5156.8**, BIC = **5233.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5645** | 0.5003 | ±1.0006 | **+47.099** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1631 | 0.1134 | ±0.2268 | -1.439 | 0.1503 |  |
| Education: high school or below (vs college) | +0.1179 | 0.2207 | ±0.4414 | +0.534 | 0.5934 |  |
| Site: UCSD (vs UAB) | -0.0734 | 0.1417 | ±0.2833 | -0.518 | 0.6042 |  |
| **Site: UW (vs UAB)** | **-0.8930** | 0.1331 | ±0.2663 | **-6.707** | **1.99e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4710** | 0.1501 | ±0.3002 | **-3.138** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9774** | 0.1783 | ±0.3567 | **+11.087** | **1.45e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3845** | 0.1498 | ±0.2996 | **-9.244** | **2.38e-20** | *** |
| **Age (years)** | **+0.0121** | 0.0051 | ±0.0101 | **+2.392** | **0.0167** | * |
| BMI (kg/m2) | +0.0051 | 0.0083 | ±0.0166 | +0.614 | 0.5391 |  |
| Hypertension | +0.2144 | 0.1217 | ±0.2435 | +1.761 | 0.0782 | . |
| High cholesterol | -0.0662 | 0.1139 | ±0.2278 | -0.581 | 0.5613 |  |
| **Kidney disease** | **+0.4840** | 0.2093 | ±0.4186 | **+2.312** | **0.0208** | * |
| Circulatory disease | +0.2960 | 0.1740 | ±0.3480 | +1.701 | 0.0889 | . |
| Mean / SD ratio | +0.0518 | 0.0422 | ±0.0843 | +1.230 | 0.2187 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.3181**, Adj R² = **0.3103**, F-statistic = **41.18** (p = **1.51e-92**), Residual SE = **1.889** on **1236** df, AIC = **5157.0**, BIC = **5234.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5960** | 0.5022 | ±1.0044 | **+46.984** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1608 | 0.1134 | ±0.2269 | -1.417 | 0.1564 |  |
| Education: high school or below (vs college) | +0.1212 | 0.2209 | ±0.4419 | +0.548 | 0.5835 |  |
| Site: UCSD (vs UAB) | -0.0703 | 0.1416 | ±0.2832 | -0.497 | 0.6194 |  |
| **Site: UW (vs UAB)** | **-0.8919** | 0.1332 | ±0.2665 | **-6.694** | **2.17e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4715** | 0.1502 | ±0.3005 | **-3.138** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9746** | 0.1785 | ±0.3570 | **+11.063** | **1.89e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3864** | 0.1498 | ±0.2996 | **-9.256** | **2.12e-20** | *** |
| **Age (years)** | **+0.0122** | 0.0051 | ±0.0101 | **+2.404** | **0.0162** | * |
| BMI (kg/m2) | +0.0054 | 0.0083 | ±0.0167 | +0.646 | 0.5181 |  |
| Hypertension | +0.2118 | 0.1217 | ±0.2433 | +1.741 | 0.0818 | . |
| High cholesterol | -0.0657 | 0.1139 | ±0.2278 | -0.577 | 0.5639 |  |
| **Kidney disease** | **+0.4857** | 0.2091 | ±0.4182 | **+2.323** | **0.0202** | * |
| Circulatory disease | +0.2947 | 0.1739 | ±0.3478 | +1.695 | 0.0901 | . |
| Avg. daily mean/SD | +0.0387 | 0.0353 | ±0.0706 | +1.096 | 0.2731 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1251**, R² = **0.3175**, Adj R² = **0.3097**, F-statistic = **41.06** (p = **2.58e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.1**, BIC = **5235.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8291** | 0.5119 | ±1.0239 | **+46.548** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1586 | 0.1133 | ±0.2266 | -1.400 | 0.1616 |  |
| Education: high school or below (vs college) | +0.1206 | 0.2218 | ±0.4435 | +0.544 | 0.5864 |  |
| Site: UCSD (vs UAB) | -0.0616 | 0.1423 | ±0.2846 | -0.433 | 0.6653 |  |
| **Site: UW (vs UAB)** | **-0.8924** | 0.1338 | ±0.2676 | **-6.670** | **2.55e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4690** | 0.1506 | ±0.3013 | **-3.113** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9800** | 0.1790 | ±0.3580 | **+11.062** | **1.92e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3864** | 0.1502 | ±0.3003 | **-9.233** | **2.62e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.316** | **0.0205** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0167 | +0.631 | 0.5279 |  |
| Hypertension | +0.2068 | 0.1217 | ±0.2435 | +1.699 | 0.0894 | . |
| High cholesterol | -0.0614 | 0.1139 | ±0.2278 | -0.539 | 0.5898 |  |
| **Kidney disease** | **+0.4703** | 0.2086 | ±0.4171 | **+2.255** | **0.0241** | * |
| Circulatory disease | +0.2932 | 0.1743 | ±0.3485 | +1.682 | 0.0925 | . |
| MAG (mg/dL/h) | +0.0014 | 0.0071 | ±0.0142 | +0.191 | 0.8484 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **1251**, R² = **0.3178**, Adj R² = **0.3100**, F-statistic = **41.12** (p = **1.97e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.6**, BIC = **5234.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0365** | 0.4811 | ±0.9621 | **+49.967** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1570 | 0.1135 | ±0.2269 | -1.384 | 0.1665 |  |
| Education: high school or below (vs college) | +0.1247 | 0.2215 | ±0.4430 | +0.563 | 0.5735 |  |
| Site: UCSD (vs UAB) | -0.0694 | 0.1419 | ±0.2837 | -0.489 | 0.6247 |  |
| **Site: UW (vs UAB)** | **-0.8925** | 0.1335 | ±0.2669 | **-6.688** | **2.26e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4736** | 0.1505 | ±0.3010 | **-3.146** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9736** | 0.1788 | ±0.3577 | **+11.035** | **2.58e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3915** | 0.1502 | ±0.3004 | **-9.265** | **1.95e-20** | *** |
| **Age (years)** | **+0.0120** | 0.0051 | ±0.0101 | **+2.363** | **0.0181** | * |
| BMI (kg/m2) | +0.0050 | 0.0083 | ±0.0167 | +0.606 | 0.5443 |  |
| Hypertension | +0.2122 | 0.1220 | ±0.2439 | +1.740 | 0.0819 | . |
| High cholesterol | -0.0644 | 0.1139 | ±0.2279 | -0.565 | 0.5720 |  |
| **Kidney disease** | **+0.4826** | 0.2097 | ±0.4193 | **+2.302** | **0.0213** | * |
| Circulatory disease | +0.2986 | 0.1742 | ±0.3484 | +1.714 | 0.0865 | . |
| Avg. daily range (mg/dL) | -0.0016 | 0.0021 | ±0.0042 | -0.763 | 0.4455 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **1251**, R² = **0.3175**, Adj R² = **0.3097**, F-statistic = **41.06** (p = **2.59e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.1**, BIC = **5235.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9005** | 0.4450 | ±0.8900 | **+53.710** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1589 | 0.1134 | ±0.2267 | -1.402 | 0.1611 |  |
| Education: high school or below (vs college) | +0.1215 | 0.2216 | ±0.4431 | +0.549 | 0.5833 |  |
| Site: UCSD (vs UAB) | -0.0649 | 0.1418 | ±0.2837 | -0.458 | 0.6472 |  |
| **Site: UW (vs UAB)** | **-0.8941** | 0.1335 | ±0.2669 | **-6.699** | **2.09e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4683** | 0.1504 | ±0.3008 | **-3.114** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9801** | 0.1791 | ±0.3581 | **+11.059** | **1.99e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3867** | 0.1499 | ±0.2998 | **-9.250** | **2.25e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.313** | **0.0207** | * |
| BMI (kg/m2) | +0.0054 | 0.0083 | ±0.0167 | +0.645 | 0.5187 |  |
| Hypertension | +0.2071 | 0.1218 | ±0.2437 | +1.700 | 0.0892 | . |
| High cholesterol | -0.0621 | 0.1140 | ±0.2280 | -0.545 | 0.5858 |  |
| **Kidney disease** | **+0.4717** | 0.2082 | ±0.4165 | **+2.265** | **0.0235** | * |
| Circulatory disease | +0.2948 | 0.1745 | ±0.3489 | +1.690 | 0.0911 | . |
| SD of daily means (mg/dL) | -0.0030 | 0.0179 | ±0.0358 | -0.167 | 0.8677 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **1251**, R² = **0.3179**, Adj R² = **0.3101**, F-statistic = **41.14** (p = **1.80e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.4**, BIC = **5234.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.4046** | 0.7427 | ±1.4853 | **+32.861** | **7.83e-237** | *** |
| Education: graduate level (vs college) | -0.1612 | 0.1134 | ±0.2269 | -1.421 | 0.1552 |  |
| Education: high school or below (vs college) | +0.1146 | 0.2220 | ±0.4439 | +0.516 | 0.6056 |  |
| Site: UCSD (vs UAB) | -0.0563 | 0.1418 | ±0.2837 | -0.397 | 0.6912 |  |
| **Site: UW (vs UAB)** | **-0.8945** | 0.1333 | ±0.2665 | **-6.712** | **1.92e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4650** | 0.1511 | ±0.3021 | **-3.078** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.9880** | 0.1788 | ±0.3576 | **+11.117** | **1.03e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3828** | 0.1501 | ±0.3002 | **-9.212** | **3.21e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.302** | **0.0213** | * |
| BMI (kg/m2) | +0.0050 | 0.0083 | ±0.0166 | +0.608 | 0.5430 |  |
| Hypertension | +0.2013 | 0.1219 | ±0.2438 | +1.651 | 0.0987 | . |
| High cholesterol | -0.0647 | 0.1138 | ±0.2276 | -0.568 | 0.5699 |  |
| **Kidney disease** | **+0.4619** | 0.2076 | ±0.4152 | **+2.225** | **0.0261** | * |
| Circulatory disease | +0.2866 | 0.1749 | ±0.3497 | +1.639 | 0.1013 |  |
| Time in range 70-180, pooled (%) | -0.0053 | 0.0063 | ±0.0126 | -0.849 | 0.3961 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **1251**, R² = **0.3179**, Adj R² = **0.3101**, F-statistic = **41.14** (p = **1.79e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.4**, BIC = **5234.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.4071** | 0.7391 | ±1.4782 | **+33.022** | **3.89e-239** | *** |
| Education: graduate level (vs college) | -0.1613 | 0.1134 | ±0.2269 | -1.422 | 0.1551 |  |
| Education: high school or below (vs college) | +0.1151 | 0.2219 | ±0.4438 | +0.519 | 0.6039 |  |
| Site: UCSD (vs UAB) | -0.0566 | 0.1418 | ±0.2836 | -0.399 | 0.6898 |  |
| **Site: UW (vs UAB)** | **-0.8943** | 0.1333 | ±0.2665 | **-6.711** | **1.93e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4654** | 0.1510 | ±0.3020 | **-3.082** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.9881** | 0.1788 | ±0.3577 | **+11.117** | **1.04e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3829** | 0.1501 | ±0.3002 | **-9.214** | **3.15e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.300** | **0.0214** | * |
| BMI (kg/m2) | +0.0050 | 0.0083 | ±0.0166 | +0.605 | 0.5451 |  |
| Hypertension | +0.2014 | 0.1219 | ±0.2439 | +1.652 | 0.0986 | . |
| High cholesterol | -0.0649 | 0.1138 | ±0.2276 | -0.571 | 0.5682 |  |
| **Kidney disease** | **+0.4618** | 0.2076 | ±0.4152 | **+2.224** | **0.0261** | * |
| Circulatory disease | +0.2866 | 0.1748 | ±0.3497 | +1.639 | 0.1012 |  |
| Avg. daily time in range 70-180 (%) | -0.0053 | 0.0062 | ±0.0125 | -0.857 | 0.3915 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.3175**, Adj R² = **0.3097**, F-statistic = **41.07** (p = **2.56e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.1**, BIC = **5235.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8995** | 0.4387 | ±0.8775 | **+54.473** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1601 | 0.1129 | ±0.2258 | -1.418 | 0.1562 |  |
| Education: high school or below (vs college) | +0.1182 | 0.2213 | ±0.4426 | +0.534 | 0.5934 |  |
| Site: UCSD (vs UAB) | -0.0677 | 0.1434 | ±0.2867 | -0.472 | 0.6368 |  |
| **Site: UW (vs UAB)** | **-0.8962** | 0.1340 | ±0.2681 | **-6.686** | **2.29e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4697** | 0.1505 | ±0.3009 | **-3.122** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9783** | 0.1790 | ±0.3579 | **+11.054** | **2.09e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3879** | 0.1501 | ±0.3001 | **-9.249** | **2.26e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.293** | **0.0219** | * |
| BMI (kg/m2) | +0.0054 | 0.0083 | ±0.0167 | +0.643 | 0.5202 |  |
| Hypertension | +0.2067 | 0.1217 | ±0.2434 | +1.698 | 0.0894 | . |
| High cholesterol | -0.0640 | 0.1142 | ±0.2284 | -0.561 | 0.5751 |  |
| **Kidney disease** | **+0.4715** | 0.2083 | ±0.4167 | **+2.263** | **0.0236** | * |
| Circulatory disease | +0.2961 | 0.1741 | ±0.3483 | +1.700 | 0.0891 | . |
| Any reading < 54 during wear (0/1) | -0.0280 | 0.1197 | ±0.2394 | -0.234 | 0.8149 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.3199**, Adj R² = **0.3122**, F-statistic = **41.53** (p = **2.97e-93**), Residual SE = **1.887** on **1236** df, AIC = **5153.7**, BIC = **5230.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8043** | 0.4359 | ±0.8718 | **+54.608** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1545 | 0.1131 | ±0.2261 | -1.366 | 0.1718 |  |
| Education: high school or below (vs college) | +0.1429 | 0.2215 | ±0.4430 | +0.645 | 0.5189 |  |
| Site: UCSD (vs UAB) | -0.0270 | 0.1431 | ±0.2861 | -0.189 | 0.8501 |  |
| **Site: UW (vs UAB)** | **-0.8668** | 0.1339 | ±0.2679 | **-6.472** | **9.67e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4658** | 0.1504 | ±0.3008 | **-3.097** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.9721** | 0.1786 | ±0.3572 | **+11.043** | **2.36e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3908** | 0.1495 | ±0.2991 | **-9.301** | **1.40e-20** | *** |
| **Age (years)** | **+0.0120** | 0.0051 | ±0.0102 | **+2.353** | **0.0186** | * |
| BMI (kg/m2) | +0.0055 | 0.0083 | ±0.0166 | +0.661 | 0.5086 |  |
| Hypertension | +0.2141 | 0.1214 | ±0.2428 | +1.764 | 0.0778 | . |
| High cholesterol | -0.0467 | 0.1138 | ±0.2275 | -0.410 | 0.6817 |  |
| **Kidney disease** | **+0.4656** | 0.2074 | ±0.4148 | **+2.245** | **0.0248** | * |
| Circulatory disease | +0.2950 | 0.1739 | ±0.3479 | +1.696 | 0.0899 | . |
| Time < 54 (%) | +0.1995 | 0.1129 | ±0.2257 | +1.767 | 0.0772 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.3195**, Adj R² = **0.3117**, F-statistic = **41.44** (p = **4.41e-93**), Residual SE = **1.887** on **1236** df, AIC = **5154.5**, BIC = **5231.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8338** | 0.4351 | ±0.8701 | **+54.783** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1530 | 0.1131 | ±0.2262 | -1.353 | 0.1761 |  |
| Education: high school or below (vs college) | +0.1411 | 0.2213 | ±0.4426 | +0.637 | 0.5238 |  |
| Site: UCSD (vs UAB) | -0.0342 | 0.1425 | ±0.2850 | -0.240 | 0.8101 |  |
| **Site: UW (vs UAB)** | **-0.8655** | 0.1338 | ±0.2676 | **-6.468** | **9.90e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4692** | 0.1503 | ±0.3007 | **-3.121** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9713** | 0.1790 | ±0.3579 | **+11.016** | **3.20e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3959** | 0.1494 | ±0.2988 | **-9.342** | **9.44e-21** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.302** | **0.0213** | * |
| BMI (kg/m2) | +0.0054 | 0.0083 | ±0.0166 | +0.649 | 0.5161 |  |
| Hypertension | +0.2172 | 0.1215 | ±0.2430 | +1.787 | 0.0739 | . |
| High cholesterol | -0.0497 | 0.1137 | ±0.2274 | -0.437 | 0.6618 |  |
| **Kidney disease** | **+0.4660** | 0.2072 | ±0.4145 | **+2.249** | **0.0245** | * |
| Circulatory disease | +0.2965 | 0.1738 | ±0.3476 | +1.706 | 0.0881 | . |
| Avg. daily time < 54 (%) | +0.2442 | 0.1802 | ±0.3603 | +1.356 | 0.1752 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.3182**, Adj R² = **0.3104**, F-statistic = **41.20** (p = **1.40e-92**), Residual SE = **1.889** on **1236** df, AIC = **5156.9**, BIC = **5233.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8381** | 0.4364 | ±0.8729 | **+54.619** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1522 | 0.1133 | ±0.2266 | -1.344 | 0.1791 |  |
| Education: high school or below (vs college) | +0.1394 | 0.2216 | ±0.4432 | +0.629 | 0.5294 |  |
| Site: UCSD (vs UAB) | -0.0503 | 0.1426 | ±0.2851 | -0.353 | 0.7243 |  |
| **Site: UW (vs UAB)** | **-0.8796** | 0.1340 | ±0.2679 | **-6.566** | **5.16e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4718** | 0.1505 | ±0.3009 | **-3.136** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9767** | 0.1785 | ±0.3570 | **+11.075** | **1.66e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3955** | 0.1501 | ±0.3001 | **-9.299** | **1.42e-20** | *** |
| **Age (years)** | **+0.0120** | 0.0051 | ±0.0102 | **+2.348** | **0.0189** | * |
| BMI (kg/m2) | +0.0050 | 0.0083 | ±0.0166 | +0.602 | 0.5473 |  |
| Hypertension | +0.2119 | 0.1216 | ±0.2432 | +1.742 | 0.0815 | . |
| High cholesterol | -0.0553 | 0.1142 | ±0.2285 | -0.484 | 0.6285 |  |
| **Kidney disease** | **+0.4723** | 0.2074 | ±0.4148 | **+2.277** | **0.0228** | * |
| Circulatory disease | +0.2936 | 0.1741 | ±0.3482 | +1.686 | 0.0917 | . |
| Time 54-69, pooled (%) | +0.0440 | 0.0305 | ±0.0610 | +1.442 | 0.1492 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1251**, R² = **0.3184**, Adj R² = **0.3107**, F-statistic = **41.24** (p = **1.14e-92**), Residual SE = **1.889** on **1236** df, AIC = **5156.4**, BIC = **5233.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8406** | 0.4355 | ±0.8710 | **+54.741** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1504 | 0.1133 | ±0.2266 | -1.328 | 0.1843 |  |
| Education: high school or below (vs college) | +0.1430 | 0.2215 | ±0.4431 | +0.646 | 0.5185 |  |
| Site: UCSD (vs UAB) | -0.0516 | 0.1423 | ±0.2846 | -0.362 | 0.7172 |  |
| **Site: UW (vs UAB)** | **-0.8774** | 0.1338 | ±0.2676 | **-6.558** | **5.47e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4723** | 0.1504 | ±0.3008 | **-3.140** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9777** | 0.1785 | ±0.3570 | **+11.080** | **1.57e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3983** | 0.1501 | ±0.3002 | **-9.317** | **1.20e-20** | *** |
| **Age (years)** | **+0.0119** | 0.0051 | ±0.0102 | **+2.338** | **0.0194** | * |
| BMI (kg/m2) | +0.0050 | 0.0083 | ±0.0166 | +0.598 | 0.5502 |  |
| Hypertension | +0.2135 | 0.1216 | ±0.2432 | +1.755 | 0.0792 | . |
| High cholesterol | -0.0549 | 0.1141 | ±0.2283 | -0.481 | 0.6303 |  |
| **Kidney disease** | **+0.4726** | 0.2074 | ±0.4147 | **+2.279** | **0.0227** | * |
| Circulatory disease | +0.2939 | 0.1741 | ±0.3482 | +1.688 | 0.0914 | . |
| Avg. daily time 54-69 (%) | +0.0507 | 0.0316 | ±0.0633 | +1.604 | 0.1087 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **1251**, R² = **0.3188**, Adj R² = **0.3111**, F-statistic = **41.32** (p = **7.66e-93**), Residual SE = **1.888** on **1236** df, AIC = **5155.6**, BIC = **5232.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8134** | 0.4363 | ±0.8726 | **+54.582** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1504 | 0.1131 | ±0.2262 | -1.330 | 0.1835 |  |
| Education: high school or below (vs college) | +0.1465 | 0.2215 | ±0.4430 | +0.661 | 0.5084 |  |
| Site: UCSD (vs UAB) | -0.0399 | 0.1426 | ±0.2852 | -0.280 | 0.7795 |  |
| **Site: UW (vs UAB)** | **-0.8713** | 0.1339 | ±0.2677 | **-6.509** | **7.59e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4711** | 0.1505 | ±0.3010 | **-3.131** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9748** | 0.1785 | ±0.3570 | **+11.063** | **1.89e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3972** | 0.1498 | ±0.2996 | **-9.328** | **1.08e-20** | *** |
| **Age (years)** | **+0.0120** | 0.0051 | ±0.0102 | **+2.362** | **0.0182** | * |
| BMI (kg/m2) | +0.0050 | 0.0083 | ±0.0166 | +0.605 | 0.5455 |  |
| Hypertension | +0.2142 | 0.1215 | ±0.2431 | +1.763 | 0.0779 | . |
| High cholesterol | -0.0506 | 0.1141 | ±0.2283 | -0.443 | 0.6574 |  |
| **Kidney disease** | **+0.4709** | 0.2071 | ±0.4142 | **+2.274** | **0.0230** | * |
| Circulatory disease | +0.2940 | 0.1741 | ±0.3482 | +1.689 | 0.0913 | . |
| Time < 70 (%) | +0.0488 | 0.0283 | ±0.0566 | +1.722 | 0.0851 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **1251**, R² = **0.3188**, Adj R² = **0.3111**, F-statistic = **41.32** (p = **7.76e-93**), Residual SE = **1.888** on **1236** df, AIC = **5155.7**, BIC = **5232.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8296** | 0.4353 | ±0.8706 | **+54.746** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1491 | 0.1132 | ±0.2264 | -1.318 | 0.1876 |  |
| Education: high school or below (vs college) | +0.1473 | 0.2215 | ±0.4429 | +0.665 | 0.5060 |  |
| Site: UCSD (vs UAB) | -0.0453 | 0.1422 | ±0.2845 | -0.318 | 0.7501 |  |
| **Site: UW (vs UAB)** | **-0.8712** | 0.1337 | ±0.2673 | **-6.518** | **7.15e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4723** | 0.1504 | ±0.3008 | **-3.140** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9761** | 0.1786 | ±0.3572 | **+11.065** | **1.86e-28** | *** |
| **Season: winter (vs autumn)** | **-1.4002** | 0.1498 | ±0.2996 | **-9.346** | **9.08e-21** | *** |
| **Age (years)** | **+0.0119** | 0.0051 | ±0.0102 | **+2.337** | **0.0195** | * |
| BMI (kg/m2) | +0.0050 | 0.0083 | ±0.0166 | +0.600 | 0.5484 |  |
| Hypertension | +0.2157 | 0.1215 | ±0.2431 | +1.775 | 0.0759 | . |
| High cholesterol | -0.0522 | 0.1140 | ±0.2281 | -0.458 | 0.6472 |  |
| **Kidney disease** | **+0.4714** | 0.2071 | ±0.4143 | **+2.276** | **0.0229** | * |
| Circulatory disease | +0.2945 | 0.1741 | ±0.3481 | +1.692 | 0.0906 | . |
| Avg. daily time < 70 (%) | +0.0512 | 0.0302 | ±0.0604 | +1.696 | 0.0899 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.3177**, Adj R² = **0.3100**, F-statistic = **41.11** (p = **2.13e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.7**, BIC = **5234.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5980** | 1.5052 | ±3.0104 | **+16.342** | **4.95e-60** | *** |
| Education: graduate level (vs college) | -0.1594 | 0.1134 | ±0.2269 | -1.405 | 0.1601 |  |
| Education: high school or below (vs college) | +0.1119 | 0.2238 | ±0.4476 | +0.500 | 0.6172 |  |
| Site: UCSD (vs UAB) | -0.0604 | 0.1418 | ±0.2836 | -0.426 | 0.6700 |  |
| **Site: UW (vs UAB)** | **-0.8924** | 0.1335 | ±0.2670 | **-6.686** | **2.30e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4682** | 0.1510 | ±0.3020 | **-3.101** | **0.0019** | ** |
| **Season: summer (vs autumn)** | **+1.9828** | 0.1788 | ±0.3577 | **+11.087** | **1.46e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3861** | 0.1500 | ±0.3000 | **-9.241** | **2.43e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.320** | **0.0203** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0166 | +0.634 | 0.5258 |  |
| Hypertension | +0.2059 | 0.1218 | ±0.2435 | +1.691 | 0.0908 | . |
| High cholesterol | -0.0612 | 0.1139 | ±0.2278 | -0.537 | 0.5913 |  |
| **Kidney disease** | **+0.4701** | 0.2078 | ±0.4155 | **+2.263** | **0.0237** | * |
| Circulatory disease | +0.2862 | 0.1750 | ±0.3500 | +1.636 | 0.1019 |  |
| Time 54-250, pooled (%) | -0.0072 | 0.0145 | ±0.0291 | -0.496 | 0.6197 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.3176**, Adj R² = **0.3099**, F-statistic = **41.09** (p = **2.25e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.9**, BIC = **5234.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5096** | 1.5078 | ±3.0157 | **+16.255** | **2.07e-59** | *** |
| Education: graduate level (vs college) | -0.1593 | 0.1134 | ±0.2269 | -1.405 | 0.1602 |  |
| Education: high school or below (vs college) | +0.1130 | 0.2239 | ±0.4477 | +0.505 | 0.6137 |  |
| Site: UCSD (vs UAB) | -0.0612 | 0.1418 | ±0.2837 | -0.432 | 0.6659 |  |
| **Site: UW (vs UAB)** | **-0.8929** | 0.1334 | ±0.2669 | **-6.691** | **2.22e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4685** | 0.1509 | ±0.3019 | **-3.103** | **0.0019** | ** |
| **Season: summer (vs autumn)** | **+1.9823** | 0.1789 | ±0.3577 | **+11.084** | **1.51e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3863** | 0.1500 | ±0.3000 | **-9.241** | **2.44e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.317** | **0.0205** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0166 | +0.633 | 0.5269 |  |
| Hypertension | +0.2060 | 0.1218 | ±0.2435 | +1.692 | 0.0906 | . |
| High cholesterol | -0.0615 | 0.1139 | ±0.2278 | -0.540 | 0.5894 |  |
| **Kidney disease** | **+0.4705** | 0.2078 | ±0.4156 | **+2.264** | **0.0236** | * |
| Circulatory disease | +0.2872 | 0.1750 | ±0.3499 | +1.641 | 0.1007 |  |
| Avg. daily time 54-250 (%) | -0.0063 | 0.0145 | ±0.0291 | -0.434 | 0.6644 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.3176**, Adj R² = **0.3099**, F-statistic = **41.09** (p = **2.33e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.9**, BIC = **5234.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8826** | 0.4344 | ±0.8688 | **+54.977** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1612 | 0.1134 | ±0.2269 | -1.421 | 0.1552 |  |
| Education: high school or below (vs college) | +0.1200 | 0.2217 | ±0.4434 | +0.541 | 0.5883 |  |
| Site: UCSD (vs UAB) | -0.0609 | 0.1418 | ±0.2837 | -0.429 | 0.6678 |  |
| **Site: UW (vs UAB)** | **-0.8971** | 0.1338 | ±0.2675 | **-6.707** | **1.98e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4664** | 0.1508 | ±0.3015 | **-3.094** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.9843** | 0.1786 | ±0.3572 | **+11.109** | **1.13e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3834** | 0.1503 | ±0.3006 | **-9.205** | **3.43e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.294** | **0.0218** | * |
| BMI (kg/m2) | +0.0051 | 0.0083 | ±0.0166 | +0.616 | 0.5377 |  |
| Hypertension | +0.2022 | 0.1218 | ±0.2437 | +1.659 | 0.0970 | . |
| High cholesterol | -0.0659 | 0.1140 | ±0.2279 | -0.578 | 0.5631 |  |
| **Kidney disease** | **+0.4643** | 0.2083 | ±0.4167 | **+2.229** | **0.0258** | * |
| Circulatory disease | +0.2923 | 0.1742 | ±0.3484 | +1.678 | 0.0934 | . |
| Time 181-250, pooled (%) | +0.0044 | 0.0088 | ±0.0177 | +0.502 | 0.6158 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1251**, R² = **0.3176**, Adj R² = **0.3099**, F-statistic = **41.09** (p = **2.27e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.9**, BIC = **5234.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8826** | 0.4344 | ±0.8688 | **+54.981** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1616 | 0.1135 | ±0.2269 | -1.424 | 0.1545 |  |
| Education: high school or below (vs college) | +0.1203 | 0.2216 | ±0.4432 | +0.543 | 0.5872 |  |
| Site: UCSD (vs UAB) | -0.0602 | 0.1418 | ±0.2836 | -0.425 | 0.6710 |  |
| **Site: UW (vs UAB)** | **-0.8971** | 0.1337 | ±0.2674 | **-6.710** | **1.95e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4664** | 0.1507 | ±0.3015 | **-3.094** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.9848** | 0.1786 | ±0.3573 | **+11.110** | **1.12e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3831** | 0.1503 | ±0.3007 | **-9.200** | **3.57e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.295** | **0.0217** | * |
| BMI (kg/m2) | +0.0051 | 0.0083 | ±0.0166 | +0.613 | 0.5396 |  |
| Hypertension | +0.2018 | 0.1219 | ±0.2438 | +1.655 | 0.0979 | . |
| High cholesterol | -0.0663 | 0.1139 | ±0.2279 | -0.582 | 0.5609 |  |
| **Kidney disease** | **+0.4634** | 0.2083 | ±0.4167 | **+2.224** | **0.0261** | * |
| Circulatory disease | +0.2921 | 0.1742 | ±0.3485 | +1.677 | 0.0936 | . |
| Avg. daily time 181-250 (%) | +0.0048 | 0.0088 | ±0.0175 | +0.551 | 0.5819 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **1251**, R² = **0.3176**, Adj R² = **0.3099**, F-statistic = **41.09** (p = **2.25e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.9**, BIC = **5234.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8803** | 0.4345 | ±0.8689 | **+54.967** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1610 | 0.1135 | ±0.2271 | -1.418 | 0.1561 |  |
| Education: high school or below (vs college) | +0.1153 | 0.2224 | ±0.4448 | +0.519 | 0.6041 |  |
| Site: UCSD (vs UAB) | -0.0606 | 0.1418 | ±0.2836 | -0.427 | 0.6692 |  |
| **Site: UW (vs UAB)** | **-0.8961** | 0.1334 | ±0.2669 | **-6.716** | **1.87e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4665** | 0.1510 | ±0.3020 | **-3.090** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.9851** | 0.1789 | ±0.3577 | **+11.098** | **1.29e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3837** | 0.1502 | ±0.3005 | **-9.209** | **3.28e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.301** | **0.0214** | * |
| BMI (kg/m2) | +0.0051 | 0.0083 | ±0.0166 | +0.620 | 0.5354 |  |
| Hypertension | +0.2027 | 0.1220 | ±0.2439 | +1.662 | 0.0966 | . |
| High cholesterol | -0.0648 | 0.1139 | ±0.2277 | -0.569 | 0.5694 |  |
| **Kidney disease** | **+0.4653** | 0.2080 | ±0.4160 | **+2.237** | **0.0253** | * |
| Circulatory disease | +0.2890 | 0.1748 | ±0.3496 | +1.654 | 0.0982 | . |
| Time > 180 (%) | +0.0035 | 0.0063 | ±0.0126 | +0.547 | 0.5847 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.3176**, Adj R² = **0.3099**, F-statistic = **41.10** (p = **2.22e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.8**, BIC = **5234.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8807** | 0.4344 | ±0.8688 | **+54.973** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1612 | 0.1135 | ±0.2271 | -1.420 | 0.1557 |  |
| Education: high school or below (vs college) | +0.1155 | 0.2223 | ±0.4447 | +0.519 | 0.6035 |  |
| Site: UCSD (vs UAB) | -0.0602 | 0.1418 | ±0.2836 | -0.425 | 0.6712 |  |
| **Site: UW (vs UAB)** | **-0.8960** | 0.1334 | ±0.2668 | **-6.716** | **1.87e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4666** | 0.1510 | ±0.3019 | **-3.091** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.9853** | 0.1789 | ±0.3578 | **+11.098** | **1.28e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3835** | 0.1503 | ±0.3005 | **-9.207** | **3.37e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.302** | **0.0213** | * |
| BMI (kg/m2) | +0.0051 | 0.0083 | ±0.0166 | +0.617 | 0.5369 |  |
| Hypertension | +0.2025 | 0.1220 | ±0.2440 | +1.660 | 0.0969 | . |
| High cholesterol | -0.0649 | 0.1138 | ±0.2277 | -0.570 | 0.5687 |  |
| **Kidney disease** | **+0.4650** | 0.2080 | ±0.4160 | **+2.235** | **0.0254** | * |
| Circulatory disease | +0.2888 | 0.1748 | ±0.3495 | +1.652 | 0.0984 | . |
| Avg. daily time > 180 (%) | +0.0036 | 0.0063 | ±0.0125 | +0.571 | 0.5679 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.3178**, Adj R² = **0.3101**, F-statistic = **41.13** (p = **1.86e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.5**, BIC = **5234.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8890** | 0.4339 | ±0.8678 | **+55.059** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1593 | 0.1133 | ±0.2267 | -1.405 | 0.1599 |  |
| Education: high school or below (vs college) | +0.1132 | 0.2224 | ±0.4448 | +0.509 | 0.6106 |  |
| Site: UCSD (vs UAB) | -0.0606 | 0.1416 | ±0.2832 | -0.428 | 0.6688 |  |
| **Site: UW (vs UAB)** | **-0.8958** | 0.1333 | ±0.2666 | **-6.719** | **1.83e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4696** | 0.1506 | ±0.3012 | **-3.118** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9863** | 0.1787 | ±0.3575 | **+11.112** | **1.09e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3861** | 0.1500 | ±0.3000 | **-9.240** | **2.46e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.321** | **0.0203** | * |
| BMI (kg/m2) | +0.0047 | 0.0083 | ±0.0166 | +0.567 | 0.5708 |  |
| Hypertension | +0.2037 | 0.1216 | ±0.2433 | +1.675 | 0.0940 | . |
| High cholesterol | -0.0673 | 0.1140 | ±0.2281 | -0.590 | 0.5550 |  |
| **Kidney disease** | **+0.4718** | 0.2074 | ±0.4148 | **+2.274** | **0.0229** | * |
| Circulatory disease | +0.2907 | 0.1748 | ±0.3496 | +1.663 | 0.0964 | . |
| Nocturnal time > 180 (%) | +0.0054 | 0.0070 | ±0.0141 | +0.763 | 0.4455 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.3194**, Adj R² = **0.3117**, F-statistic = **41.44** (p = **4.44e-93**), Residual SE = **1.888** on **1236** df, AIC = **5154.5**, BIC = **5231.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9579** | 0.4369 | ±0.8739 | **+54.831** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1609 | 0.1134 | ±0.2267 | -1.420 | 0.1557 |  |
| Education: high school or below (vs college) | +0.1207 | 0.2208 | ±0.4416 | +0.547 | 0.5846 |  |
| Site: UCSD (vs UAB) | -0.0692 | 0.1421 | ±0.2841 | -0.487 | 0.6259 |  |
| **Site: UW (vs UAB)** | **-0.8900** | 0.1335 | ±0.2669 | **-6.668** | **2.59e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4850** | 0.1506 | ±0.3011 | **-3.221** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+1.9667** | 0.1788 | ±0.3576 | **+10.998** | **3.89e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3998** | 0.1500 | ±0.3001 | **-9.330** | **1.06e-20** | *** |
| **Age (years)** | **+0.0120** | 0.0051 | ±0.0101 | **+2.361** | **0.0182** | * |
| BMI (kg/m2) | +0.0041 | 0.0083 | ±0.0166 | +0.496 | 0.6202 |  |
| Hypertension | +0.2222 | 0.1216 | ±0.2432 | +1.827 | 0.0676 | . |
| High cholesterol | -0.0581 | 0.1138 | ±0.2276 | -0.511 | 0.6094 |  |
| **Kidney disease** | **+0.4778** | 0.2094 | ±0.4188 | **+2.282** | **0.0225** | * |
| Circulatory disease | +0.2915 | 0.1731 | ±0.3462 | +1.684 | 0.0922 | . |
| Any reading > 250 during wear (0/1) | -0.2604 | 0.1388 | ±0.2775 | -1.877 | 0.0605 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.3175**, Adj R² = **0.3098**, F-statistic = **41.08** (p = **2.42e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.0**, BIC = **5235.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8812** | 0.4343 | ±0.8686 | **+54.985** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1593 | 0.1134 | ±0.2269 | -1.404 | 0.1602 |  |
| Education: high school or below (vs college) | +0.1149 | 0.2240 | ±0.4480 | +0.513 | 0.6079 |  |
| Site: UCSD (vs UAB) | -0.0624 | 0.1419 | ±0.2837 | -0.440 | 0.6598 |  |
| **Site: UW (vs UAB)** | **-0.8938** | 0.1334 | ±0.2668 | **-6.699** | **2.09e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4688** | 0.1509 | ±0.3018 | **-3.107** | **0.0019** | ** |
| **Season: summer (vs autumn)** | **+1.9816** | 0.1789 | ±0.3577 | **+11.078** | **1.60e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3865** | 0.1500 | ±0.3001 | **-9.240** | **2.46e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.316** | **0.0206** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0166 | +0.634 | 0.5262 |  |
| Hypertension | +0.2060 | 0.1218 | ±0.2436 | +1.691 | 0.0908 | . |
| High cholesterol | -0.0620 | 0.1140 | ±0.2279 | -0.544 | 0.5862 |  |
| **Kidney disease** | **+0.4707** | 0.2079 | ±0.4158 | **+2.264** | **0.0236** | * |
| Circulatory disease | +0.2889 | 0.1749 | ±0.3499 | +1.651 | 0.0987 | . |
| Time > 250 (%) | +0.0046 | 0.0144 | ±0.0289 | +0.318 | 0.7506 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.3175**, Adj R² = **0.3098**, F-statistic = **41.08** (p = **2.44e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.0**, BIC = **5235.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8817** | 0.4343 | ±0.8685 | **+54.992** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1593 | 0.1134 | ±0.2269 | -1.404 | 0.1602 |  |
| Education: high school or below (vs college) | +0.1152 | 0.2240 | ±0.4480 | +0.514 | 0.6072 |  |
| Site: UCSD (vs UAB) | -0.0625 | 0.1419 | ±0.2837 | -0.440 | 0.6597 |  |
| **Site: UW (vs UAB)** | **-0.8939** | 0.1334 | ±0.2668 | **-6.701** | **2.07e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4688** | 0.1509 | ±0.3018 | **-3.107** | **0.0019** | ** |
| **Season: summer (vs autumn)** | **+1.9815** | 0.1789 | ±0.3577 | **+11.078** | **1.61e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3864** | 0.1501 | ±0.3001 | **-9.239** | **2.49e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.316** | **0.0206** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0166 | +0.633 | 0.5268 |  |
| Hypertension | +0.2060 | 0.1218 | ±0.2436 | +1.691 | 0.0908 | . |
| High cholesterol | -0.0620 | 0.1140 | ±0.2279 | -0.544 | 0.5862 |  |
| **Kidney disease** | **+0.4709** | 0.2079 | ±0.4158 | **+2.265** | **0.0235** | * |
| Circulatory disease | +0.2890 | 0.1749 | ±0.3499 | +1.652 | 0.0985 | . |
| Avg. daily time > 250 (%) | +0.0045 | 0.0144 | ±0.0288 | +0.310 | 0.7567 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 1,251; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **1251**, R² = **0.2679**, Adj R² = **0.2602**, F-statistic = **34.81** (p = **1.05e-74**), Residual SE = **5.823** on **1237** df, AIC = **7972.2**, BIC = **8044.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3662** | 1.2999 | ±2.5998 | **+37.977** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9936** | 0.3543 | ±0.7087 | **+2.804** | **0.0050** | ** |
| Education: high school or below (vs college) | +0.8238 | 0.6702 | ±1.3404 | +1.229 | 0.2190 |  |
| **Site: UCSD (vs UAB)** | **+2.8535** | 0.4577 | ±0.9155 | **+6.234** | **4.55e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9571** | 0.4064 | ±0.8129 | **-4.815** | **1.47e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4850** | 0.4652 | ±0.9303 | **-3.192** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2286** | 0.5125 | ±1.0250 | **+4.348** | **1.37e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4450** | 0.4816 | ±0.9632 | **-11.305** | **1.23e-29** | *** |
| **Age (years)** | **-0.0516** | 0.0156 | ±0.0312 | **-3.302** | **9.61e-04** | *** |
| BMI (kg/m2) | -0.0145 | 0.0253 | ±0.0506 | -0.574 | 0.5659 |  |
| Hypertension | +0.0922 | 0.3774 | ±0.7548 | +0.244 | 0.8070 |  |
| High cholesterol | -0.6624 | 0.3497 | ±0.6994 | -1.894 | 0.0582 | . |
| Kidney disease | -0.2967 | 0.6681 | ±1.3362 | -0.444 | 0.6570 |  |
| Circulatory disease | +0.5547 | 0.5081 | ±1.0162 | +1.092 | 0.2749 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **1251**, R² = **0.2693**, Adj R² = **0.2610**, F-statistic = **32.54** (p = **1.92e-74**), Residual SE = **5.820** on **1236** df, AIC = **7971.7**, BIC = **8048.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.8318** | 1.8804 | ±3.7608 | **+24.905** | **6.55e-137** | *** |
| **Education: graduate level (vs college)** | **+0.9886** | 0.3543 | ±0.7087 | **+2.790** | **0.0053** | ** |
| Education: high school or below (vs college) | +0.7445 | 0.6735 | ±1.3470 | +1.105 | 0.2690 |  |
| **Site: UCSD (vs UAB)** | **+2.8422** | 0.4573 | ±0.9146 | **+6.215** | **5.13e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9778** | 0.4062 | ±0.8124 | **-4.869** | **1.12e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4223** | 0.4657 | ±0.9314 | **-3.054** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+2.2492** | 0.5130 | ±1.0259 | **+4.385** | **1.16e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4191** | 0.4804 | ±0.9609 | **-11.279** | **1.66e-29** | *** |
| **Age (years)** | **-0.0537** | 0.0157 | ±0.0314 | **-3.420** | **6.27e-04** | *** |
| BMI (kg/m2) | -0.0180 | 0.0253 | ±0.0507 | -0.709 | 0.4781 |  |
| Hypertension | +0.0634 | 0.3782 | ±0.7563 | +0.168 | 0.8668 |  |
| **High cholesterol** | **-0.7167** | 0.3501 | ±0.7002 | **-2.047** | **0.0406** | * |
| Kidney disease | -0.2951 | 0.6698 | ±1.3397 | -0.441 | 0.6595 |  |
| Circulatory disease | +0.5198 | 0.5057 | ±1.0114 | +1.028 | 0.3040 |  |
| HbA1c (%) | +0.4929 | 0.2662 | ±0.5324 | +1.851 | 0.0641 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **1251**, R² = **0.2679**, Adj R² = **0.2596**, F-statistic = **32.31** (p = **5.93e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.1**, BIC = **8051.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.0023** | 1.5834 | ±3.1669 | **+30.947** | **2.82e-210** | *** |
| **Education: graduate level (vs college)** | **+0.9859** | 0.3550 | ±0.7100 | **+2.777** | **0.0055** | ** |
| Education: high school or below (vs college) | +0.8045 | 0.6763 | ±1.3526 | +1.190 | 0.2342 |  |
| **Site: UCSD (vs UAB)** | **+2.8564** | 0.4584 | ±0.9168 | **+6.231** | **4.63e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9668** | 0.4070 | ±0.8140 | **-4.833** | **1.35e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4790** | 0.4663 | ±0.9326 | **-3.172** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2380** | 0.5133 | ±1.0265 | **+4.360** | **1.30e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4351** | 0.4816 | ±0.9632 | **-11.285** | **1.55e-29** | *** |
| **Age (years)** | **-0.0518** | 0.0157 | ±0.0313 | **-3.309** | **9.37e-04** | *** |
| BMI (kg/m2) | -0.0150 | 0.0253 | ±0.0507 | -0.591 | 0.5542 |  |
| Hypertension | +0.0806 | 0.3786 | ±0.7573 | +0.213 | 0.8314 |  |
| High cholesterol | -0.6690 | 0.3497 | ±0.6995 | -1.913 | 0.0558 | . |
| Kidney disease | -0.3074 | 0.6685 | ±1.3369 | -0.460 | 0.6456 |  |
| Circulatory disease | +0.5455 | 0.5097 | ±1.0195 | +1.070 | 0.2846 |  |
| Mean glucose (mg/dL) | +0.0033 | 0.0082 | ±0.0164 | +0.404 | 0.6859 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **1251**, R² = **0.2679**, Adj R² = **0.2596**, F-statistic = **32.31** (p = **5.93e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.1**, BIC = **8051.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5436** | 2.4167 | ±4.8335 | **+20.086** | **9.69e-90** | *** |
| **Education: graduate level (vs college)** | **+0.9859** | 0.3550 | ±0.7100 | **+2.777** | **0.0055** | ** |
| Education: high school or below (vs college) | +0.8045 | 0.6763 | ±1.3526 | +1.190 | 0.2342 |  |
| **Site: UCSD (vs UAB)** | **+2.8564** | 0.4584 | ±0.9168 | **+6.231** | **4.63e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9668** | 0.4070 | ±0.8140 | **-4.833** | **1.35e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4790** | 0.4663 | ±0.9326 | **-3.172** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2380** | 0.5133 | ±1.0265 | **+4.360** | **1.30e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4351** | 0.4816 | ±0.9632 | **-11.285** | **1.55e-29** | *** |
| **Age (years)** | **-0.0518** | 0.0157 | ±0.0313 | **-3.309** | **9.37e-04** | *** |
| BMI (kg/m2) | -0.0150 | 0.0253 | ±0.0507 | -0.591 | 0.5542 |  |
| Hypertension | +0.0806 | 0.3786 | ±0.7573 | +0.213 | 0.8314 |  |
| High cholesterol | -0.6690 | 0.3497 | ±0.6995 | -1.913 | 0.0558 | . |
| Kidney disease | -0.3074 | 0.6685 | ±1.3369 | -0.460 | 0.6456 |  |
| Circulatory disease | +0.5455 | 0.5097 | ±1.0195 | +1.070 | 0.2846 |  |
| GMI (%) | +0.1386 | 0.3426 | ±0.6852 | +0.404 | 0.6859 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **1251**, R² = **0.2684**, Adj R² = **0.2602**, F-statistic = **32.40** (p = **3.92e-74**), Residual SE = **5.823** on **1236** df, AIC = **7973.2**, BIC = **8050.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4756** | 1.5396 | ±3.0793 | **+31.485** | **1.40e-217** | *** |
| **Education: graduate level (vs college)** | **+0.9802** | 0.3546 | ±0.7091 | **+2.764** | **0.0057** | ** |
| Education: high school or below (vs college) | +0.7756 | 0.6757 | ±1.3514 | +1.148 | 0.2510 |  |
| **Site: UCSD (vs UAB)** | **+2.8486** | 0.4582 | ±0.9164 | **+6.217** | **5.06e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9794** | 0.4070 | ±0.8139 | **-4.864** | **1.15e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4830** | 0.4656 | ±0.9312 | **-3.185** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2504** | 0.5133 | ±1.0266 | **+4.384** | **1.16e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4331** | 0.4819 | ±0.9639 | **-11.273** | **1.78e-29** | *** |
| **Age (years)** | **-0.0513** | 0.0156 | ±0.0313 | **-3.282** | **0.0010** | ** |
| BMI (kg/m2) | -0.0178 | 0.0255 | ±0.0510 | -0.697 | 0.4856 |  |
| Hypertension | +0.0681 | 0.3785 | ±0.7571 | +0.180 | 0.8572 |  |
| High cholesterol | -0.6852 | 0.3498 | ±0.6997 | -1.959 | 0.0502 | . |
| Kidney disease | -0.3008 | 0.6708 | ±1.3416 | -0.448 | 0.6539 |  |
| Circulatory disease | +0.5396 | 0.5095 | ±1.0190 | +1.059 | 0.2896 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0084 | 0.0075 | ±0.0150 | +1.111 | 0.2667 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.2684**, Adj R² = **0.2601**, F-statistic = **32.39** (p = **3.95e-74**), Residual SE = **5.823** on **1236** df, AIC = **7973.2**, BIC = **8050.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8366** | 1.3582 | ±2.7164 | **+36.694** | **9.26e-295** | *** |
| **Education: graduate level (vs college)** | **+0.9976** | 0.3543 | ±0.7086 | **+2.816** | **0.0049** | ** |
| Education: high school or below (vs college) | +0.8318 | 0.6728 | ±1.3455 | +1.236 | 0.2163 |  |
| **Site: UCSD (vs UAB)** | **+2.8297** | 0.4593 | ±0.9185 | **+6.161** | **7.21e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9448** | 0.4074 | ±0.8147 | **-4.774** | **1.80e-06** | *** |
| **Season: spring (vs autumn)** | **-1.5008** | 0.4660 | ±0.9320 | **-3.221** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+2.2128** | 0.5133 | ±1.0266 | **+4.311** | **1.63e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4596** | 0.4813 | ±0.9627 | **-11.342** | **8.08e-30** | *** |
| **Age (years)** | **-0.0506** | 0.0157 | ±0.0314 | **-3.222** | **0.0013** | ** |
| BMI (kg/m2) | -0.0143 | 0.0254 | ±0.0507 | -0.562 | 0.5739 |  |
| Hypertension | +0.1236 | 0.3780 | ±0.7561 | +0.327 | 0.7436 |  |
| High cholesterol | -0.6630 | 0.3498 | ±0.6996 | -1.895 | 0.0580 | . |
| Kidney disease | -0.2450 | 0.6673 | ±1.3346 | -0.367 | 0.7135 |  |
| Circulatory disease | +0.5769 | 0.5091 | ±1.0182 | +1.133 | 0.2572 |  |
| Glucose SD, pooled (mg/dL) | -0.0251 | 0.0256 | ±0.0511 | -0.984 | 0.3253 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.2681**, Adj R² = **0.2598**, F-statistic = **32.35** (p = **5.04e-74**), Residual SE = **5.824** on **1236** df, AIC = **7973.7**, BIC = **8050.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.6728** | 1.3543 | ±2.7086 | **+36.678** | **1.67e-294** | *** |
| **Education: graduate level (vs college)** | **+0.9982** | 0.3544 | ±0.7089 | **+2.816** | **0.0049** | ** |
| Education: high school or below (vs college) | +0.8302 | 0.6724 | ±1.3449 | +1.235 | 0.2169 |  |
| **Site: UCSD (vs UAB)** | **+2.8386** | 0.4588 | ±0.9177 | **+6.187** | **6.15e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9467** | 0.4079 | ±0.8157 | **-4.773** | **1.81e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4986** | 0.4663 | ±0.9327 | **-3.214** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+2.2140** | 0.5139 | ±1.0278 | **+4.308** | **1.65e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4582** | 0.4818 | ±0.9636 | **-11.329** | **9.41e-30** | *** |
| **Age (years)** | **-0.0508** | 0.0157 | ±0.0314 | **-3.234** | **0.0012** | ** |
| BMI (kg/m2) | -0.0141 | 0.0254 | ±0.0507 | -0.557 | 0.5778 |  |
| Hypertension | +0.1138 | 0.3783 | ±0.7565 | +0.301 | 0.7636 |  |
| High cholesterol | -0.6620 | 0.3498 | ±0.6996 | -1.892 | 0.0585 | . |
| Kidney disease | -0.2584 | 0.6686 | ±1.3372 | -0.387 | 0.6991 |  |
| Circulatory disease | +0.5694 | 0.5088 | ±1.0177 | +1.119 | 0.2631 |  |
| Avg. daily SD (mg/dL) | -0.0188 | 0.0281 | ±0.0561 | -0.670 | 0.5025 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **1251**, R² = **0.2690**, Adj R² = **0.2607**, F-statistic = **32.48** (p = **2.57e-74**), Residual SE = **5.821** on **1236** df, AIC = **7972.3**, BIC = **8049.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3116** | 1.4337 | ±2.8675 | **+35.091** | **9.12e-270** | *** |
| **Education: graduate level (vs college)** | **+0.9804** | 0.3543 | ±0.7086 | **+2.767** | **0.0057** | ** |
| Education: high school or below (vs college) | +0.7929 | 0.6731 | ±1.3462 | +1.178 | 0.2388 |  |
| **Site: UCSD (vs UAB)** | **+2.8145** | 0.4596 | ±0.9193 | **+6.123** | **9.16e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9626** | 0.4071 | ±0.8142 | **-4.821** | **1.43e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4987** | 0.4657 | ±0.9313 | **-3.218** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+2.2258** | 0.5136 | ±1.0272 | **+4.334** | **1.47e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4430** | 0.4819 | ±0.9639 | **-11.294** | **1.40e-29** | *** |
| **Age (years)** | **-0.0503** | 0.0157 | ±0.0314 | **-3.203** | **0.0014** | ** |
| BMI (kg/m2) | -0.0151 | 0.0253 | ±0.0506 | -0.598 | 0.5497 |  |
| Hypertension | +0.1174 | 0.3777 | ±0.7554 | +0.311 | 0.7560 |  |
| High cholesterol | -0.6823 | 0.3501 | ±0.7003 | -1.949 | 0.0513 | . |
| Kidney disease | -0.2373 | 0.6693 | ±1.3385 | -0.355 | 0.7229 |  |
| Circulatory disease | +0.5674 | 0.5097 | ±1.0195 | +1.113 | 0.2657 |  |
| CV (%) | -0.0555 | 0.0416 | ±0.0833 | -1.333 | 0.1824 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1251**, R² = **0.2688**, Adj R² = **0.2605**, F-statistic = **32.45** (p = **3.02e-74**), Residual SE = **5.822** on **1236** df, AIC = **7972.7**, BIC = **8049.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.3379** | 1.6179 | ±3.2358 | **+29.877** | **3.97e-196** | *** |
| **Education: graduate level (vs college)** | **+0.9801** | 0.3543 | ±0.7085 | **+2.767** | **0.0057** | ** |
| Education: high school or below (vs college) | +0.8118 | 0.6730 | ±1.3460 | +1.206 | 0.2277 |  |
| **Site: UCSD (vs UAB)** | **+2.8219** | 0.4593 | ±0.9185 | **+6.144** | **8.03e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9526** | 0.4076 | ±0.8152 | **-4.790** | **1.66e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4895** | 0.4655 | ±0.9311 | **-3.200** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2234** | 0.5135 | ±1.0270 | **+4.330** | **1.49e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4361** | 0.4820 | ±0.9640 | **-11.278** | **1.69e-29** | *** |
| **Age (years)** | **-0.0504** | 0.0157 | ±0.0314 | **-3.209** | **0.0013** | ** |
| BMI (kg/m2) | -0.0151 | 0.0253 | ±0.0506 | -0.596 | 0.5509 |  |
| Hypertension | +0.1170 | 0.3784 | ±0.7567 | +0.309 | 0.7571 |  |
| High cholesterol | -0.6740 | 0.3501 | ±0.7001 | -1.925 | 0.0542 | . |
| Kidney disease | -0.2566 | 0.6681 | ±1.3361 | -0.384 | 0.7009 |  |
| Circulatory disease | +0.5625 | 0.5105 | ±1.0211 | +1.102 | 0.2706 |  |
| Mean / SD ratio | +0.1665 | 0.1387 | ±0.2773 | +1.201 | 0.2299 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.2680**, Adj R² = **0.2597**, F-statistic = **32.33** (p = **5.48e-74**), Residual SE = **5.825** on **1236** df, AIC = **7973.9**, BIC = **8050.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.9079** | 1.6352 | ±3.2705 | **+29.909** | **1.51e-196** | *** |
| **Education: graduate level (vs college)** | **+0.9907** | 0.3545 | ±0.7089 | **+2.795** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.8231 | 0.6719 | ±1.3438 | +1.225 | 0.2206 |  |
| **Site: UCSD (vs UAB)** | **+2.8428** | 0.4584 | ±0.9168 | **+6.201** | **5.60e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9532** | 0.4078 | ±0.8156 | **-4.790** | **1.67e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4879** | 0.4658 | ±0.9317 | **-3.194** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2216** | 0.5138 | ±1.0276 | **+4.324** | **1.53e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4436** | 0.4821 | ±0.9642 | **-11.292** | **1.44e-29** | *** |
| **Age (years)** | **-0.0509** | 0.0157 | ±0.0314 | **-3.237** | **0.0012** | ** |
| BMI (kg/m2) | -0.0144 | 0.0253 | ±0.0507 | -0.567 | 0.5707 |  |
| Hypertension | +0.1003 | 0.3785 | ±0.7570 | +0.265 | 0.7910 |  |
| High cholesterol | -0.6675 | 0.3502 | ±0.7004 | -1.906 | 0.0566 | . |
| Kidney disease | -0.2741 | 0.6697 | ±1.3394 | -0.409 | 0.6823 |  |
| Circulatory disease | +0.5565 | 0.5096 | ±1.0191 | +1.092 | 0.2748 |  |
| Avg. daily mean/SD | +0.0614 | 0.1212 | ±0.2423 | +0.507 | 0.6122 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1251**, R² = **0.2680**, Adj R² = **0.2597**, F-statistic = **32.32** (p = **5.65e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.0**, BIC = **8050.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.7863** | 1.5199 | ±3.0399 | **+32.755** | **2.56e-235** | *** |
| **Education: graduate level (vs college)** | **+0.9910** | 0.3544 | ±0.7089 | **+2.796** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.8310 | 0.6737 | ±1.3475 | +1.233 | 0.2174 |  |
| **Site: UCSD (vs UAB)** | **+2.8381** | 0.4600 | ±0.9200 | **+6.169** | **6.85e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9719** | 0.4075 | ±0.8150 | **-4.839** | **1.31e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4895** | 0.4660 | ±0.9320 | **-3.196** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2206** | 0.5130 | ±1.0261 | **+4.328** | **1.50e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4515** | 0.4812 | ±0.9624 | **-11.329** | **9.48e-30** | *** |
| **Age (years)** | **-0.0518** | 0.0156 | ±0.0312 | **-3.320** | **9.00e-04** | *** |
| BMI (kg/m2) | -0.0144 | 0.0253 | ±0.0507 | -0.567 | 0.5707 |  |
| Hypertension | +0.0913 | 0.3778 | ±0.7557 | +0.242 | 0.8090 |  |
| High cholesterol | -0.6712 | 0.3513 | ±0.7025 | -1.911 | 0.0560 | . |
| Kidney disease | -0.2872 | 0.6704 | ±1.3408 | -0.428 | 0.6684 |  |
| Circulatory disease | +0.5577 | 0.5090 | ±1.0180 | +1.096 | 0.2732 |  |
| MAG (mg/dL/h) | -0.0103 | 0.0215 | ±0.0430 | -0.478 | 0.6324 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **1251**, R² = **0.2682**, Adj R² = **0.2599**, F-statistic = **32.35** (p = **4.88e-74**), Residual SE = **5.824** on **1236** df, AIC = **7973.7**, BIC = **8050.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8112** | 1.4031 | ±2.8063 | **+35.500** | **4.97e-276** | *** |
| **Education: graduate level (vs college)** | **+0.9992** | 0.3544 | ±0.7087 | **+2.820** | **0.0048** | ** |
| Education: high school or below (vs college) | +0.8328 | 0.6733 | ±1.3467 | +1.237 | 0.2161 |  |
| **Site: UCSD (vs UAB)** | **+2.8365** | 0.4588 | ±0.9176 | **+6.183** | **6.30e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9517** | 0.4074 | ±0.8148 | **-4.791** | **1.66e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4966** | 0.4663 | ±0.9325 | **-3.210** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+2.2128** | 0.5137 | ±1.0274 | **+4.308** | **1.65e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4573** | 0.4816 | ±0.9632 | **-11.332** | **9.13e-30** | *** |
| **Age (years)** | **-0.0509** | 0.0157 | ±0.0314 | **-3.245** | **0.0012** | ** |
| BMI (kg/m2) | -0.0152 | 0.0253 | ±0.0506 | -0.601 | 0.5478 |  |
| Hypertension | +0.1084 | 0.3779 | ±0.7559 | +0.287 | 0.7743 |  |
| High cholesterol | -0.6678 | 0.3500 | ±0.7000 | -1.908 | 0.0564 | . |
| Kidney disease | -0.2641 | 0.6694 | ±1.3387 | -0.395 | 0.6931 |  |
| Circulatory disease | +0.5694 | 0.5087 | ±1.0174 | +1.119 | 0.2629 |  |
| Avg. daily range (mg/dL) | -0.0047 | 0.0065 | ±0.0130 | -0.724 | 0.4691 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **1251**, R² = **0.2680**, Adj R² = **0.2597**, F-statistic = **32.32** (p = **5.87e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.0**, BIC = **8051.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4737** | 1.3223 | ±2.6446 | **+37.415** | **2.23e-306** | *** |
| **Education: graduate level (vs college)** | **+0.9937** | 0.3546 | ±0.7093 | **+2.802** | **0.0051** | ** |
| Education: high school or below (vs college) | +0.8233 | 0.6707 | ±1.3414 | +1.228 | 0.2196 |  |
| **Site: UCSD (vs UAB)** | **+2.8445** | 0.4603 | ±0.9207 | **+6.179** | **6.44e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9553** | 0.4065 | ±0.8131 | **-4.810** | **1.51e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4763** | 0.4669 | ±0.9337 | **-3.162** | **0.0016** | ** |
| **Season: summer (vs autumn)** | **+2.2359** | 0.5141 | ±1.0282 | **+4.349** | **1.37e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4411** | 0.4827 | ±0.9655 | **-11.271** | **1.82e-29** | *** |
| **Age (years)** | **-0.0515** | 0.0156 | ±0.0313 | **-3.297** | **9.78e-04** | *** |
| BMI (kg/m2) | -0.0139 | 0.0254 | ±0.0508 | -0.546 | 0.5849 |  |
| Hypertension | +0.0949 | 0.3776 | ±0.7552 | +0.251 | 0.8015 |  |
| High cholesterol | -0.6596 | 0.3501 | ±0.7001 | -1.884 | 0.0595 | . |
| Kidney disease | -0.2957 | 0.6680 | ±1.3361 | -0.443 | 0.6581 |  |
| Circulatory disease | +0.5633 | 0.5100 | ±1.0200 | +1.105 | 0.2693 |  |
| SD of daily means (mg/dL) | -0.0204 | 0.0517 | ±0.1035 | -0.394 | 0.6934 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **1251**, R² = **0.2679**, Adj R² = **0.2596**, F-statistic = **32.30** (p = **6.25e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.2**, BIC = **8051.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.0289** | 2.2554 | ±4.5109 | **+21.738** | **8.95e-105** | *** |
| **Education: graduate level (vs college)** | **+0.9951** | 0.3549 | ±0.7097 | **+2.804** | **0.0050** | ** |
| Education: high school or below (vs college) | +0.8283 | 0.6731 | ±1.3463 | +1.231 | 0.2185 |  |
| **Site: UCSD (vs UAB)** | **+2.8487** | 0.4603 | ±0.9207 | **+6.188** | **6.08e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9571** | 0.4067 | ±0.8133 | **-4.813** | **1.49e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4880** | 0.4658 | ±0.9316 | **-3.194** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2228** | 0.5135 | ±1.0270 | **+4.329** | **1.50e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4479** | 0.4818 | ±0.9637 | **-11.306** | **1.22e-29** | *** |
| **Age (years)** | **-0.0515** | 0.0156 | ±0.0313 | **-3.297** | **9.79e-04** | *** |
| BMI (kg/m2) | -0.0144 | 0.0254 | ±0.0507 | -0.567 | 0.5708 |  |
| Hypertension | +0.0957 | 0.3773 | ±0.7547 | +0.254 | 0.7998 |  |
| High cholesterol | -0.6611 | 0.3498 | ±0.6996 | -1.890 | 0.0588 | . |
| Kidney disease | -0.2904 | 0.6671 | ±1.3341 | -0.435 | 0.6633 |  |
| Circulatory disease | +0.5593 | 0.5095 | ±1.0191 | +1.098 | 0.2724 |  |
| Time in range 70-180, pooled (%) | +0.0035 | 0.0187 | ±0.0373 | +0.186 | 0.8526 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **1251**, R² = **0.2679**, Adj R² = **0.2596**, F-statistic = **32.30** (p = **6.31e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.2**, BIC = **8051.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1375** | 2.2440 | ±4.4879 | **+21.898** | **2.74e-106** | *** |
| **Education: graduate level (vs college)** | **+0.9946** | 0.3549 | ±0.7097 | **+2.803** | **0.0051** | ** |
| Education: high school or below (vs college) | +0.8267 | 0.6728 | ±1.3457 | +1.229 | 0.2192 |  |
| **Site: UCSD (vs UAB)** | **+2.8504** | 0.4602 | ±0.9205 | **+6.193** | **5.90e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9572** | 0.4067 | ±0.8134 | **-4.812** | **1.49e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4868** | 0.4657 | ±0.9315 | **-3.192** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2246** | 0.5136 | ±1.0271 | **+4.332** | **1.48e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4469** | 0.4818 | ±0.9636 | **-11.305** | **1.24e-29** | *** |
| **Age (years)** | **-0.0515** | 0.0156 | ±0.0313 | **-3.297** | **9.79e-04** | *** |
| BMI (kg/m2) | -0.0144 | 0.0254 | ±0.0507 | -0.568 | 0.5698 |  |
| Hypertension | +0.0945 | 0.3774 | ±0.7549 | +0.250 | 0.8022 |  |
| High cholesterol | -0.6614 | 0.3498 | ±0.6997 | -1.891 | 0.0587 | . |
| Kidney disease | -0.2924 | 0.6673 | ±1.3345 | -0.438 | 0.6612 |  |
| Circulatory disease | +0.5578 | 0.5096 | ±1.0192 | +1.095 | 0.2737 |  |
| Avg. daily time in range 70-180 (%) | +0.0023 | 0.0185 | ±0.0369 | +0.127 | 0.8992 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.2684**, Adj R² = **0.2602**, F-statistic = **32.40** (p = **3.93e-74**), Residual SE = **5.823** on **1236** df, AIC = **7973.2**, BIC = **8050.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5546** | 1.3027 | ±2.6054 | **+38.041** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9788** | 0.3554 | ±0.7108 | **+2.754** | **0.0059** | ** |
| Education: high school or below (vs college) | +0.7800 | 0.6740 | ±1.3480 | +1.157 | 0.2472 |  |
| **Site: UCSD (vs UAB)** | **+2.8015** | 0.4620 | ±0.9239 | **+6.065** | **1.32e-09** | *** |
| **Site: UW (vs UAB)** | **-1.9802** | 0.4075 | ±0.8149 | **-4.860** | **1.17e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4869** | 0.4655 | ±0.9311 | **-3.194** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2195** | 0.5129 | ±1.0257 | **+4.328** | **1.51e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4537** | 0.4819 | ±0.9638 | **-11.317** | **1.08e-29** | *** |
| **Age (years)** | **-0.0525** | 0.0156 | ±0.0312 | **-3.367** | **7.61e-04** | *** |
| BMI (kg/m2) | -0.0136 | 0.0254 | ±0.0508 | -0.536 | 0.5920 |  |
| Hypertension | +0.0923 | 0.3780 | ±0.7560 | +0.244 | 0.8071 |  |
| High cholesterol | -0.6809 | 0.3500 | ±0.7000 | -1.945 | 0.0517 | . |
| Kidney disease | -0.2972 | 0.6697 | ±1.3394 | -0.444 | 0.6572 |  |
| Circulatory disease | +0.5862 | 0.5111 | ±1.0222 | +1.147 | 0.2514 |  |
| Any reading < 54 during wear (0/1) | -0.3568 | 0.3644 | ±0.7287 | -0.979 | 0.3274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.2696**, Adj R² = **0.2613**, F-statistic = **32.59** (p = **1.52e-74**), Residual SE = **5.819** on **1236** df, AIC = **7971.2**, BIC = **8048.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5677** | 1.2987 | ±2.5974 | **+38.167** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9825** | 0.3540 | ±0.7080 | **+2.775** | **0.0055** | ** |
| Education: high school or below (vs college) | +0.7705 | 0.6718 | ±1.3436 | +1.147 | 0.2514 |  |
| **Site: UCSD (vs UAB)** | **+2.7619** | 0.4614 | ±0.9228 | **+5.986** | **2.15e-09** | *** |
| **Site: UW (vs UAB)** | **-2.0262** | 0.4085 | ±0.8170 | **-4.960** | **7.05e-07** | *** |
| **Season: spring (vs autumn)** | **-1.4945** | 0.4651 | ±0.9302 | **-3.213** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+2.2459** | 0.5125 | ±1.0249 | **+4.383** | **1.17e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4361** | 0.4824 | ±0.9648 | **-11.269** | **1.86e-29** | *** |
| **Age (years)** | **-0.0521** | 0.0156 | ±0.0312 | **-3.338** | **8.44e-04** | *** |
| BMI (kg/m2) | -0.0150 | 0.0253 | ±0.0505 | -0.595 | 0.5518 |  |
| Hypertension | +0.0736 | 0.3783 | ±0.7566 | +0.195 | 0.8457 |  |
| **High cholesterol** | **-0.7023** | 0.3505 | ±0.7010 | **-2.004** | **0.0451** | * |
| Kidney disease | -0.2819 | 0.6671 | ±1.3341 | -0.423 | 0.6726 |  |
| Circulatory disease | +0.5512 | 0.5098 | ±1.0196 | +1.081 | 0.2796 |  |
| **Time < 54 (%)** | **-0.4995** | 0.1696 | ±0.3393 | **-2.945** | **0.0032** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.2701**, Adj R² = **0.2618**, F-statistic = **32.67** (p = **1.02e-74**), Residual SE = **5.817** on **1236** df, AIC = **7970.4**, BIC = **8047.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5255** | 1.2962 | ±2.5924 | **+38.209** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9751** | 0.3540 | ±0.7081 | **+2.754** | **0.0059** | ** |
| Education: high school or below (vs college) | +0.7629 | 0.6696 | ±1.3392 | +1.139 | 0.2546 |  |
| **Site: UCSD (vs UAB)** | **+2.7616** | 0.4607 | ±0.9214 | **+5.995** | **2.04e-09** | *** |
| **Site: UW (vs UAB)** | **-2.0475** | 0.4090 | ±0.8181 | **-5.006** | **5.57e-07** | *** |
| **Season: spring (vs autumn)** | **-1.4860** | 0.4650 | ±0.9299 | **-3.196** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2526** | 0.5128 | ±1.0256 | **+4.393** | **1.12e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4180** | 0.4827 | ±0.9653 | **-11.225** | **3.07e-29** | *** |
| **Age (years)** | **-0.0514** | 0.0156 | ±0.0312 | **-3.299** | **9.70e-04** | *** |
| BMI (kg/m2) | -0.0149 | 0.0252 | ±0.0504 | -0.591 | 0.5546 |  |
| Hypertension | +0.0594 | 0.3782 | ±0.7565 | +0.157 | 0.8753 |  |
| **High cholesterol** | **-0.7025** | 0.3501 | ±0.7002 | **-2.007** | **0.0448** | * |
| Kidney disease | -0.2795 | 0.6671 | ±1.3342 | -0.419 | 0.6752 |  |
| Circulatory disease | +0.5458 | 0.5081 | ±1.0162 | +1.074 | 0.2828 |  |
| **Avg. daily time < 54 (%)** | **-0.7639** | 0.2373 | ±0.4747 | **-3.219** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.2687**, Adj R² = **0.2605**, F-statistic = **32.45** (p = **3.05e-74**), Residual SE = **5.822** on **1236** df, AIC = **7972.7**, BIC = **8049.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5214** | 1.3031 | ±2.6062 | **+38.003** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9714** | 0.3548 | ±0.7097 | **+2.738** | **0.0062** | ** |
| Education: high school or below (vs college) | +0.7648 | 0.6726 | ±1.3452 | +1.137 | 0.2555 |  |
| **Site: UCSD (vs UAB)** | **+2.8092** | 0.4610 | ±0.9220 | **+6.093** | **1.11e-09** | *** |
| **Site: UW (vs UAB)** | **-2.0062** | 0.4087 | ±0.8173 | **-4.909** | **9.15e-07** | *** |
| **Season: spring (vs autumn)** | **-1.4775** | 0.4662 | ±0.9324 | **-3.169** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2361** | 0.5132 | ±1.0263 | **+4.358** | **1.31e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4177** | 0.4831 | ±0.9662 | **-11.214** | **3.46e-29** | *** |
| **Age (years)** | **-0.0523** | 0.0156 | ±0.0312 | **-3.346** | **8.21e-04** | *** |
| BMI (kg/m2) | -0.0136 | 0.0253 | ±0.0506 | -0.538 | 0.5907 |  |
| Hypertension | +0.0750 | 0.3784 | ±0.7567 | +0.198 | 0.8429 |  |
| High cholesterol | -0.6866 | 0.3506 | ±0.7013 | -1.958 | 0.0502 | . |
| Kidney disease | -0.2993 | 0.6701 | ±1.3402 | -0.447 | 0.6551 |  |
| Circulatory disease | +0.5546 | 0.5089 | ±1.0178 | +1.090 | 0.2758 |  |
| Time 54-69, pooled (%) | -0.1463 | 0.1007 | ±0.2014 | -1.453 | 0.1462 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1251**, R² = **0.2686**, Adj R² = **0.2603**, F-statistic = **32.42** (p = **3.46e-74**), Residual SE = **5.823** on **1236** df, AIC = **7972.9**, BIC = **8049.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4821** | 1.3020 | ±2.6039 | **+38.006** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9713** | 0.3550 | ±0.7100 | **+2.736** | **0.0062** | ** |
| Education: high school or below (vs college) | +0.7675 | 0.6722 | ±1.3443 | +1.142 | 0.2535 |  |
| **Site: UCSD (vs UAB)** | **+2.8218** | 0.4603 | ±0.9206 | **+6.130** | **8.77e-10** | *** |
| **Site: UW (vs UAB)** | **-2.0018** | 0.4085 | ±0.8171 | **-4.900** | **9.58e-07** | *** |
| **Season: spring (vs autumn)** | **-1.4778** | 0.4661 | ±0.9321 | **-3.171** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2319** | 0.5130 | ±1.0261 | **+4.350** | **1.36e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4160** | 0.4831 | ±0.9663 | **-11.210** | **3.64e-29** | *** |
| **Age (years)** | **-0.0519** | 0.0156 | ±0.0312 | **-3.328** | **8.76e-04** | *** |
| BMI (kg/m2) | -0.0137 | 0.0253 | ±0.0506 | -0.542 | 0.5878 |  |
| Hypertension | +0.0744 | 0.3783 | ±0.7566 | +0.197 | 0.8442 |  |
| High cholesterol | -0.6825 | 0.3505 | ±0.7010 | -1.947 | 0.0515 | . |
| Kidney disease | -0.2995 | 0.6698 | ±1.3397 | -0.447 | 0.6548 |  |
| Circulatory disease | +0.5539 | 0.5088 | ±1.0175 | +1.089 | 0.2763 |  |
| Avg. daily time 54-69 (%) | -0.1334 | 0.1015 | ±0.2029 | -1.315 | 0.1886 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **1251**, R² = **0.2692**, Adj R² = **0.2610**, F-statistic = **32.53** (p = **2.03e-74**), Residual SE = **5.820** on **1236** df, AIC = **7971.8**, BIC = **8048.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5782** | 1.3022 | ±2.6043 | **+38.074** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9684** | 0.3545 | ±0.7090 | **+2.732** | **0.0063** | ** |
| Education: high school or below (vs college) | +0.7499 | 0.6729 | ±1.3459 | +1.114 | 0.2651 |  |
| **Site: UCSD (vs UAB)** | **+2.7831** | 0.4619 | ±0.9238 | **+6.025** | **1.69e-09** | *** |
| **Site: UW (vs UAB)** | **-2.0257** | 0.4090 | ±0.8180 | **-4.953** | **7.31e-07** | *** |
| **Season: spring (vs autumn)** | **-1.4804** | 0.4661 | ±0.9321 | **-3.176** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2411** | 0.5132 | ±1.0263 | **+4.367** | **1.26e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4154** | 0.4833 | ±0.9665 | **-11.206** | **3.81e-29** | *** |
| **Age (years)** | **-0.0524** | 0.0156 | ±0.0312 | **-3.356** | **7.90e-04** | *** |
| BMI (kg/m2) | -0.0138 | 0.0253 | ±0.0506 | -0.545 | 0.5860 |  |
| Hypertension | +0.0698 | 0.3785 | ±0.7571 | +0.184 | 0.8538 |  |
| **High cholesterol** | **-0.6979** | 0.3508 | ±0.7016 | **-1.990** | **0.0466** | * |
| Kidney disease | -0.2950 | 0.6697 | ±1.3395 | -0.440 | 0.6596 |  |
| Circulatory disease | +0.5536 | 0.5093 | ±1.0186 | +1.087 | 0.2771 |  |
| Time < 70 (%) | -0.1448 | 0.0807 | ±0.1614 | -1.794 | 0.0727 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **1251**, R² = **0.2691**, Adj R² = **0.2608**, F-statistic = **32.50** (p = **2.36e-74**), Residual SE = **5.821** on **1236** df, AIC = **7972.1**, BIC = **8049.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5196** | 1.3005 | ±2.6010 | **+38.077** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9664** | 0.3547 | ±0.7095 | **+2.724** | **0.0064** | ** |
| Education: high school or below (vs college) | +0.7524 | 0.6719 | ±1.3438 | +1.120 | 0.2628 |  |
| **Site: UCSD (vs UAB)** | **+2.8025** | 0.4608 | ±0.9216 | **+6.082** | **1.19e-09** | *** |
| **Site: UW (vs UAB)** | **-2.0217** | 0.4089 | ±0.8178 | **-4.944** | **7.65e-07** | *** |
| **Season: spring (vs autumn)** | **-1.4775** | 0.4661 | ±0.9321 | **-3.170** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2366** | 0.5131 | ±1.0262 | **+4.359** | **1.31e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4090** | 0.4834 | ±0.9669 | **-11.189** | **4.62e-29** | *** |
| **Age (years)** | **-0.0519** | 0.0156 | ±0.0312 | **-3.330** | **8.69e-04** | *** |
| BMI (kg/m2) | -0.0137 | 0.0253 | ±0.0505 | -0.543 | 0.5869 |  |
| Hypertension | +0.0670 | 0.3784 | ±0.7569 | +0.177 | 0.8594 |  |
| **High cholesterol** | **-0.6913** | 0.3505 | ±0.7010 | **-1.972** | **0.0486** | * |
| Kidney disease | -0.2965 | 0.6697 | ±1.3395 | -0.443 | 0.6580 |  |
| Circulatory disease | +0.5521 | 0.5088 | ±1.0175 | +1.085 | 0.2778 |  |
| Avg. daily time < 70 (%) | -0.1423 | 0.0878 | ±0.1755 | -1.622 | 0.1048 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.2683**, Adj R² = **0.2600**, F-statistic = **32.37** (p = **4.55e-74**), Residual SE = **5.824** on **1236** df, AIC = **7973.5**, BIC = **8050.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.1276** | 2.8954 | ±5.7908 | **+18.003** | **1.83e-72** | *** |
| **Education: graduate level (vs college)** | **+0.9918** | 0.3544 | ±0.7088 | **+2.798** | **0.0051** | ** |
| Education: high school or below (vs college) | +0.7862 | 0.6756 | ±1.3513 | +1.164 | 0.2446 |  |
| **Site: UCSD (vs UAB)** | **+2.8657** | 0.4586 | ±0.9171 | **+6.249** | **4.13e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9496** | 0.4071 | ±0.8143 | **-4.788** | **1.68e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4797** | 0.4652 | ±0.9305 | **-3.180** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2433** | 0.5132 | ±1.0264 | **+4.371** | **1.24e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4406** | 0.4816 | ±0.9632 | **-11.297** | **1.37e-29** | *** |
| **Age (years)** | **-0.0514** | 0.0156 | ±0.0313 | **-3.289** | **0.0010** | ** |
| BMI (kg/m2) | -0.0146 | 0.0253 | ±0.0507 | -0.575 | 0.5651 |  |
| Hypertension | +0.0893 | 0.3773 | ±0.7546 | +0.237 | 0.8130 |  |
| High cholesterol | -0.6571 | 0.3498 | ±0.6996 | -1.879 | 0.0603 | . |
| Kidney disease | -0.3022 | 0.6696 | ±1.3391 | -0.451 | 0.6518 |  |
| Circulatory disease | +0.5261 | 0.5089 | ±1.0178 | +1.034 | 0.3012 |  |
| Time 54-250, pooled (%) | -0.0279 | 0.0264 | ±0.0528 | -1.059 | 0.2897 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.2683**, Adj R² = **0.2600**, F-statistic = **32.38** (p = **4.34e-74**), Residual SE = **5.824** on **1236** df, AIC = **7973.4**, BIC = **8050.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.3934** | 2.9246 | ±5.8493 | **+17.915** | **9.08e-72** | *** |
| **Education: graduate level (vs college)** | **+0.9917** | 0.3544 | ±0.7088 | **+2.798** | **0.0051** | ** |
| Education: high school or below (vs college) | +0.7821 | 0.6759 | ±1.3519 | +1.157 | 0.2472 |  |
| **Site: UCSD (vs UAB)** | **+2.8650** | 0.4584 | ±0.9169 | **+6.250** | **4.12e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9499** | 0.4071 | ±0.8142 | **-4.790** | **1.67e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4795** | 0.4652 | ±0.9304 | **-3.180** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2447** | 0.5133 | ±1.0265 | **+4.373** | **1.22e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4401** | 0.4816 | ±0.9633 | **-11.295** | **1.39e-29** | *** |
| **Age (years)** | **-0.0514** | 0.0156 | ±0.0313 | **-3.291** | **9.99e-04** | *** |
| BMI (kg/m2) | -0.0146 | 0.0253 | ±0.0507 | -0.578 | 0.5631 |  |
| Hypertension | +0.0892 | 0.3773 | ±0.7546 | +0.236 | 0.8132 |  |
| High cholesterol | -0.6572 | 0.3498 | ±0.6996 | -1.879 | 0.0602 | . |
| Kidney disease | -0.3017 | 0.6695 | ±1.3391 | -0.451 | 0.6523 |  |
| Circulatory disease | +0.5237 | 0.5091 | ±1.0182 | +1.029 | 0.3036 |  |
| Avg. daily time 54-250 (%) | -0.0305 | 0.0267 | ±0.0534 | -1.145 | 0.2522 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.2681**, Adj R² = **0.2598**, F-statistic = **32.34** (p = **5.14e-74**), Residual SE = **5.824** on **1236** df, AIC = **7973.8**, BIC = **8050.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3750** | 1.2995 | ±2.5990 | **+37.995** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+1.0031** | 0.3551 | ±0.7102 | **+2.825** | **0.0047** | ** |
| Education: high school or below (vs college) | +0.8303 | 0.6714 | ±1.3428 | +1.237 | 0.2162 |  |
| **Site: UCSD (vs UAB)** | **+2.8423** | 0.4586 | ±0.9172 | **+6.197** | **5.74e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9459** | 0.4067 | ±0.8134 | **-4.785** | **1.71e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4981** | 0.4653 | ±0.9307 | **-3.219** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+2.2069** | 0.5130 | ±1.0261 | **+4.302** | **1.70e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4606** | 0.4819 | ±0.9638 | **-11.331** | **9.20e-30** | *** |
| **Age (years)** | **-0.0512** | 0.0156 | ±0.0313 | **-3.274** | **0.0011** | ** |
| BMI (kg/m2) | -0.0139 | 0.0254 | ±0.0508 | -0.546 | 0.5852 |  |
| Hypertension | +0.1106 | 0.3775 | ±0.7551 | +0.293 | 0.7695 |  |
| High cholesterol | -0.6488 | 0.3495 | ±0.6990 | -1.857 | 0.0634 | . |
| Kidney disease | -0.2673 | 0.6639 | ±1.3279 | -0.403 | 0.6873 |  |
| Circulatory disease | +0.5600 | 0.5083 | ±1.0165 | +1.102 | 0.2706 |  |
| Time 181-250, pooled (%) | -0.0181 | 0.0278 | ±0.0556 | -0.649 | 0.5163 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1251**, R² = **0.2681**, Adj R² = **0.2598**, F-statistic = **32.34** (p = **5.26e-74**), Residual SE = **5.825** on **1236** df, AIC = **7973.8**, BIC = **8050.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3738** | 1.2996 | ±2.5992 | **+37.991** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+1.0028** | 0.3551 | ±0.7102 | **+2.824** | **0.0047** | ** |
| Education: high school or below (vs college) | +0.8283 | 0.6712 | ±1.3425 | +1.234 | 0.2172 |  |
| **Site: UCSD (vs UAB)** | **+2.8417** | 0.4588 | ±0.9176 | **+6.194** | **5.88e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9477** | 0.4066 | ±0.8132 | **-4.790** | **1.67e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4961** | 0.4653 | ±0.9305 | **-3.216** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+2.2085** | 0.5130 | ±1.0260 | **+4.305** | **1.67e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4596** | 0.4819 | ±0.9637 | **-11.330** | **9.32e-30** | *** |
| **Age (years)** | **-0.0513** | 0.0156 | ±0.0313 | **-3.278** | **0.0010** | ** |
| BMI (kg/m2) | -0.0139 | 0.0254 | ±0.0508 | -0.546 | 0.5852 |  |
| Hypertension | +0.1094 | 0.3776 | ±0.7552 | +0.290 | 0.7721 |  |
| High cholesterol | -0.6495 | 0.3496 | ±0.6992 | -1.858 | 0.0632 | . |
| Kidney disease | -0.2684 | 0.6641 | ±1.3283 | -0.404 | 0.6861 |  |
| Circulatory disease | +0.5599 | 0.5083 | ±1.0166 | +1.102 | 0.2707 |  |
| Avg. daily time 181-250 (%) | -0.0168 | 0.0274 | ±0.0547 | -0.615 | 0.5383 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **1251**, R² = **0.2679**, Adj R² = **0.2596**, F-statistic = **32.30** (p = **6.31e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.2**, BIC = **8051.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3634** | 1.3010 | ±2.6019 | **+37.943** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9923** | 0.3551 | ±0.7101 | **+2.795** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.8199 | 0.6741 | ±1.3482 | +1.216 | 0.2239 |  |
| **Site: UCSD (vs UAB)** | **+2.8553** | 0.4592 | ±0.9184 | **+6.218** | **5.03e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9582** | 0.4065 | ±0.8129 | **-4.818** | **1.45e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4830** | 0.4659 | ±0.9317 | **-3.183** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2324** | 0.5138 | ±1.0275 | **+4.345** | **1.39e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4427** | 0.4819 | ±0.9638 | **-11.295** | **1.39e-29** | *** |
| **Age (years)** | **-0.0516** | 0.0156 | ±0.0313 | **-3.298** | **9.74e-04** | *** |
| BMI (kg/m2) | -0.0146 | 0.0254 | ±0.0507 | -0.576 | 0.5643 |  |
| Hypertension | +0.0897 | 0.3775 | ±0.7551 | +0.238 | 0.8122 |  |
| High cholesterol | -0.6638 | 0.3498 | ±0.6996 | -1.898 | 0.0577 | . |
| Kidney disease | -0.3006 | 0.6679 | ±1.3358 | -0.450 | 0.6527 |  |
| Circulatory disease | +0.5519 | 0.5095 | ±1.0190 | +1.083 | 0.2787 |  |
| Time > 180 (%) | +0.0022 | 0.0182 | ±0.0364 | +0.119 | 0.9054 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.2679**, Adj R² = **0.2596**, F-statistic = **32.30** (p = **6.29e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.2**, BIC = **8051.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3632** | 1.3011 | ±2.6021 | **+37.941** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9919** | 0.3551 | ±0.7102 | **+2.794** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.8194 | 0.6737 | ±1.3474 | +1.216 | 0.2239 |  |
| **Site: UCSD (vs UAB)** | **+2.8559** | 0.4593 | ±0.9187 | **+6.218** | **5.05e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9583** | 0.4065 | ±0.8130 | **-4.818** | **1.45e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4828** | 0.4658 | ±0.9316 | **-3.183** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2332** | 0.5137 | ±1.0275 | **+4.347** | **1.38e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4422** | 0.4819 | ±0.9637 | **-11.294** | **1.40e-29** | *** |
| **Age (years)** | **-0.0516** | 0.0156 | ±0.0313 | **-3.299** | **9.72e-04** | *** |
| BMI (kg/m2) | -0.0146 | 0.0254 | ±0.0507 | -0.578 | 0.5636 |  |
| Hypertension | +0.0892 | 0.3776 | ±0.7552 | +0.236 | 0.8132 |  |
| High cholesterol | -0.6641 | 0.3499 | ±0.6997 | -1.898 | 0.0577 | . |
| Kidney disease | -0.3014 | 0.6680 | ±1.3360 | -0.451 | 0.6518 |  |
| Circulatory disease | +0.5513 | 0.5095 | ±1.0191 | +1.082 | 0.2793 |  |
| Avg. daily time > 180 (%) | +0.0026 | 0.0181 | ±0.0361 | +0.144 | 0.8858 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.2682**, Adj R² = **0.2599**, F-statistic = **32.36** (p = **4.78e-74**), Residual SE = **5.824** on **1236** df, AIC = **7973.6**, BIC = **8050.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3779** | 1.3025 | ±2.6049 | **+37.911** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9926** | 0.3546 | ±0.7091 | **+2.799** | **0.0051** | ** |
| Education: high school or below (vs college) | +0.8006 | 0.6728 | ±1.3456 | +1.190 | 0.2341 |  |
| **Site: UCSD (vs UAB)** | **+2.8619** | 0.4583 | ±0.9166 | **+6.245** | **4.25e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9611** | 0.4066 | ±0.8133 | **-4.823** | **1.42e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4850** | 0.4652 | ±0.9305 | **-3.192** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2490** | 0.5125 | ±1.0250 | **+4.388** | **1.14e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4417** | 0.4815 | ±0.9631 | **-11.300** | **1.31e-29** | *** |
| **Age (years)** | **-0.0514** | 0.0156 | ±0.0313 | **-3.289** | **0.0010** | ** |
| BMI (kg/m2) | -0.0161 | 0.0255 | ±0.0510 | -0.633 | 0.5267 |  |
| Hypertension | +0.0839 | 0.3777 | ±0.7554 | +0.222 | 0.8243 |  |
| High cholesterol | -0.6757 | 0.3501 | ±0.7003 | -1.930 | 0.0536 | . |
| Kidney disease | -0.2960 | 0.6710 | ±1.3420 | -0.441 | 0.6592 |  |
| Circulatory disease | +0.5466 | 0.5086 | ±1.0172 | +1.075 | 0.2825 |  |
| Nocturnal time > 180 (%) | +0.0150 | 0.0162 | ±0.0325 | +0.923 | 0.3562 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.2685**, Adj R² = **0.2602**, F-statistic = **32.41** (p = **3.72e-74**), Residual SE = **5.823** on **1236** df, AIC = **7973.1**, BIC = **8050.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4902** | 1.2966 | ±2.5932 | **+38.169** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9902** | 0.3543 | ±0.7087 | **+2.794** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.8223 | 0.6712 | ±1.3423 | +1.225 | 0.2205 |  |
| **Site: UCSD (vs UAB)** | **+2.8439** | 0.4577 | ±0.9154 | **+6.214** | **5.17e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9496** | 0.4068 | ±0.8135 | **-4.793** | **1.64e-06** | *** |
| **Season: spring (vs autumn)** | **-1.5110** | 0.4656 | ±0.9312 | **-3.245** | **0.0012** | ** |
| **Season: summer (vs autumn)** | **+2.2078** | 0.5137 | ±1.0274 | **+4.298** | **1.72e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4663** | 0.4815 | ±0.9629 | **-11.354** | **7.11e-30** | *** |
| **Age (years)** | **-0.0512** | 0.0156 | ±0.0313 | **-3.275** | **0.0011** | ** |
| BMI (kg/m2) | -0.0165 | 0.0254 | ±0.0507 | -0.650 | 0.5156 |  |
| Hypertension | +0.1186 | 0.3772 | ±0.7543 | +0.314 | 0.7532 |  |
| High cholesterol | -0.6550 | 0.3495 | ±0.6991 | -1.874 | 0.0609 | . |
| Kidney disease | -0.2860 | 0.6665 | ±1.3330 | -0.429 | 0.6679 |  |
| Circulatory disease | +0.5512 | 0.5099 | ±1.0198 | +1.081 | 0.2797 |  |
| Any reading > 250 during wear (0/1) | -0.4415 | 0.4291 | ±0.8581 | -1.029 | 0.3035 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.2685**, Adj R² = **0.2602**, F-statistic = **32.40** (p = **3.78e-74**), Residual SE = **5.823** on **1236** df, AIC = **7973.1**, BIC = **8050.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3389** | 1.3017 | ±2.6033 | **+37.904** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9906** | 0.3543 | ±0.7086 | **+2.796** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.7729 | 0.6761 | ±1.3521 | +1.143 | 0.2529 |  |
| **Site: UCSD (vs UAB)** | **+2.8624** | 0.4581 | ±0.9162 | **+6.249** | **4.14e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9525** | 0.4068 | ±0.8137 | **-4.799** | **1.59e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4790** | 0.4651 | ±0.9303 | **-3.180** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2482** | 0.5133 | ±1.0265 | **+4.380** | **1.19e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4389** | 0.4816 | ±0.9632 | **-11.293** | **1.42e-29** | *** |
| **Age (years)** | **-0.0514** | 0.0156 | ±0.0313 | **-3.288** | **0.0010** | ** |
| BMI (kg/m2) | -0.0146 | 0.0253 | ±0.0506 | -0.577 | 0.5638 |  |
| Hypertension | +0.0872 | 0.3773 | ±0.7545 | +0.231 | 0.8172 |  |
| High cholesterol | -0.6585 | 0.3498 | ±0.6996 | -1.883 | 0.0598 | . |
| Kidney disease | -0.3025 | 0.6697 | ±1.3394 | -0.452 | 0.6515 |  |
| Circulatory disease | +0.5186 | 0.5091 | ±1.0181 | +1.019 | 0.3083 |  |
| Time > 250 (%) | +0.0350 | 0.0257 | ±0.0513 | +1.365 | 0.1722 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.2685**, Adj R² = **0.2602**, F-statistic = **32.41** (p = **3.68e-74**), Residual SE = **5.823** on **1236** df, AIC = **7973.1**, BIC = **8050.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3412** | 1.3016 | ±2.6032 | **+37.908** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9904** | 0.3543 | ±0.7086 | **+2.795** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.7709 | 0.6761 | ±1.3522 | +1.140 | 0.2542 |  |
| **Site: UCSD (vs UAB)** | **+2.8629** | 0.4581 | ±0.9161 | **+6.250** | **4.10e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9528** | 0.4068 | ±0.8136 | **-4.800** | **1.58e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4784** | 0.4651 | ±0.9302 | **-3.179** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2491** | 0.5133 | ±1.0266 | **+4.382** | **1.18e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4378** | 0.4816 | ±0.9632 | **-11.291** | **1.46e-29** | *** |
| **Age (years)** | **-0.0514** | 0.0156 | ±0.0313 | **-3.289** | **0.0010** | ** |
| BMI (kg/m2) | -0.0147 | 0.0253 | ±0.0506 | -0.580 | 0.5619 |  |
| Hypertension | +0.0870 | 0.3773 | ±0.7545 | +0.231 | 0.8177 |  |
| High cholesterol | -0.6581 | 0.3498 | ±0.6996 | -1.881 | 0.0599 | . |
| Kidney disease | -0.3019 | 0.6697 | ±1.3394 | -0.451 | 0.6521 |  |
| Circulatory disease | +0.5171 | 0.5091 | ±1.0181 | +1.016 | 0.3097 |  |
| Avg. daily time > 250 (%) | +0.0366 | 0.0262 | ±0.0524 | +1.399 | 0.1619 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 1,251; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **1251**, R² = **0.0347**, Adj R² = **0.0245**, F-statistic = **3.42** (p = **3.26e-05**), Residual SE = **15.223** on **1237** df, AIC = **10376.5**, BIC = **10448.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.9972** | 3.5527 | ±7.1054 | **+35.184** | **3.53e-271** | *** |
| Education: graduate level (vs college) | -0.6569 | 0.9007 | ±1.8015 | -0.729 | 0.4658 |  |
| **Education: high school or below (vs college)** | **+4.3279** | 1.8802 | ±3.7605 | **+2.302** | **0.0213** | * |
| Site: UCSD (vs UAB) | +1.5135 | 1.2170 | ±2.4339 | +1.244 | 0.2136 |  |
| Site: UW (vs UAB) | -0.9535 | 1.0779 | ±2.1557 | -0.885 | 0.3764 |  |
| **Season: spring (vs autumn)** | **+2.8007** | 1.1677 | ±2.3355 | **+2.398** | **0.0165** | * |
| Season: summer (vs autumn) | +1.1537 | 1.3383 | ±2.6766 | +0.862 | 0.3886 |  |
| **Season: winter (vs autumn)** | **+3.2236** | 1.2255 | ±2.4509 | **+2.631** | **0.0085** | ** |
| **Age (years)** | **-0.1015** | 0.0419 | ±0.0839 | **-2.419** | **0.0156** | * |
| **BMI (kg/m2)** | **+0.1750** | 0.0634 | ±0.1268 | **+2.761** | **0.0058** | ** |
| Hypertension | +1.2082 | 0.9767 | ±1.9534 | +1.237 | 0.2161 |  |
| High cholesterol | -0.8229 | 0.9093 | ±1.8185 | -0.905 | 0.3655 |  |
| Kidney disease | -1.0302 | 1.5982 | ±3.1963 | -0.645 | 0.5192 |  |
| Circulatory disease | +0.4514 | 1.3648 | ±2.7296 | +0.331 | 0.7408 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **1251**, R² = **0.0357**, Adj R² = **0.0248**, F-statistic = **3.27** (p = **3.80e-05**), Residual SE = **15.221** on **1236** df, AIC = **10377.2**, BIC = **10454.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.9258** | 5.2340 | ±10.4680 | **+24.824** | **5.00e-136** | *** |
| Education: graduate level (vs college) | -0.6473 | 0.9005 | ±1.8009 | -0.719 | 0.4723 |  |
| **Education: high school or below (vs college)** | **+4.4821** | 1.8717 | ±3.7433 | **+2.395** | **0.0166** | * |
| Site: UCSD (vs UAB) | +1.5353 | 1.2174 | ±2.4347 | +1.261 | 0.2072 |  |
| Site: UW (vs UAB) | -0.9133 | 1.0781 | ±2.1562 | -0.847 | 0.3969 |  |
| **Season: spring (vs autumn)** | **+2.6788** | 1.1758 | ±2.3516 | **+2.278** | **0.0227** | * |
| Season: summer (vs autumn) | +1.1137 | 1.3415 | ±2.6830 | +0.830 | 0.4064 |  |
| **Season: winter (vs autumn)** | **+3.1732** | 1.2264 | ±2.4529 | **+2.587** | **0.0097** | ** |
| **Age (years)** | **-0.0973** | 0.0421 | ±0.0843 | **-2.307** | **0.0210** | * |
| **BMI (kg/m2)** | **+0.1817** | 0.0635 | ±0.1271 | **+2.860** | **0.0042** | ** |
| Hypertension | +1.2642 | 0.9792 | ±1.9583 | +1.291 | 0.1967 |  |
| High cholesterol | -0.7173 | 0.9138 | ±1.8276 | -0.785 | 0.4324 |  |
| Kidney disease | -1.0333 | 1.6034 | ±3.2069 | -0.644 | 0.5193 |  |
| Circulatory disease | +0.5194 | 1.3634 | ±2.7267 | +0.381 | 0.7032 |  |
| HbA1c (%) | -0.9585 | 0.7502 | ±1.5004 | -1.278 | 0.2013 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **1251**, R² = **0.0359**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.43e-05**), Residual SE = **15.219** on **1236** df, AIC = **10376.9**, BIC = **10453.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.2056** | 4.2975 | ±8.5950 | **+29.833** | **1.47e-195** | *** |
| Education: graduate level (vs college) | -0.5895 | 0.9009 | ±1.8018 | -0.654 | 0.5129 |  |
| **Education: high school or below (vs college)** | **+4.4986** | 1.8832 | ±3.7664 | **+2.389** | **0.0169** | * |
| Site: UCSD (vs UAB) | +1.4877 | 1.2178 | ±2.4356 | +1.222 | 0.2219 |  |
| Site: UW (vs UAB) | -0.8679 | 1.0751 | ±2.1501 | -0.807 | 0.4195 |  |
| **Season: spring (vs autumn)** | **+2.7484** | 1.1681 | ±2.3362 | **+2.353** | **0.0186** | * |
| Season: summer (vs autumn) | +1.0712 | 1.3404 | ±2.6808 | +0.799 | 0.4242 |  |
| **Season: winter (vs autumn)** | **+3.1364** | 1.2236 | ±2.4472 | **+2.563** | **0.0104** | * |
| **Age (years)** | **-0.0994** | 0.0421 | ±0.0841 | **-2.363** | **0.0182** | * |
| **BMI (kg/m2)** | **+0.1790** | 0.0633 | ±0.1266 | **+2.827** | **0.0047** | ** |
| Hypertension | +1.3105 | 0.9807 | ±1.9613 | +1.336 | 0.1814 |  |
| High cholesterol | -0.7652 | 0.9086 | ±1.8173 | -0.842 | 0.3997 |  |
| Kidney disease | -0.9357 | 1.6005 | ±3.2011 | -0.585 | 0.5588 |  |
| Circulatory disease | +0.5332 | 1.3655 | ±2.7309 | +0.390 | 0.6962 |  |
| Mean glucose (mg/dL) | -0.0292 | 0.0220 | ±0.0440 | -1.328 | 0.1843 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **1251**, R² = **0.0359**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.43e-05**), Residual SE = **15.219** on **1236** df, AIC = **10376.9**, BIC = **10453.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.2493** | 6.5171 | ±13.0343 | **+20.292** | **1.50e-91** | *** |
| Education: graduate level (vs college) | -0.5895 | 0.9009 | ±1.8018 | -0.654 | 0.5129 |  |
| **Education: high school or below (vs college)** | **+4.4986** | 1.8832 | ±3.7664 | **+2.389** | **0.0169** | * |
| Site: UCSD (vs UAB) | +1.4877 | 1.2178 | ±2.4356 | +1.222 | 0.2219 |  |
| Site: UW (vs UAB) | -0.8679 | 1.0751 | ±2.1501 | -0.807 | 0.4195 |  |
| **Season: spring (vs autumn)** | **+2.7484** | 1.1681 | ±2.3362 | **+2.353** | **0.0186** | * |
| Season: summer (vs autumn) | +1.0712 | 1.3404 | ±2.6808 | +0.799 | 0.4242 |  |
| **Season: winter (vs autumn)** | **+3.1364** | 1.2236 | ±2.4472 | **+2.563** | **0.0104** | * |
| **Age (years)** | **-0.0994** | 0.0421 | ±0.0841 | **-2.363** | **0.0182** | * |
| **BMI (kg/m2)** | **+0.1790** | 0.0633 | ±0.1266 | **+2.827** | **0.0047** | ** |
| Hypertension | +1.3105 | 0.9807 | ±1.9613 | +1.336 | 0.1814 |  |
| High cholesterol | -0.7652 | 0.9086 | ±1.8173 | -0.842 | 0.3997 |  |
| Kidney disease | -0.9357 | 1.6005 | ±3.2011 | -0.585 | 0.5588 |  |
| Circulatory disease | +0.5332 | 1.3655 | ±2.7309 | +0.390 | 0.6962 |  |
| GMI (%) | -1.2216 | 0.9202 | ±1.8404 | -1.328 | 0.1843 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **1251**, R² = **0.0354**, Adj R² = **0.0244**, F-statistic = **3.24** (p = **4.56e-05**), Residual SE = **15.224** on **1236** df, AIC = **10377.6**, BIC = **10454.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.1816** | 4.2313 | ±8.4626 | **+30.057** | **1.74e-198** | *** |
| Education: graduate level (vs college) | -0.6240 | 0.9005 | ±1.8009 | -0.693 | 0.4883 |  |
| **Education: high school or below (vs college)** | **+4.4463** | 1.8796 | ±3.7592 | **+2.366** | **0.0180** | * |
| Site: UCSD (vs UAB) | +1.5254 | 1.2183 | ±2.4367 | +1.252 | 0.2105 |  |
| Site: UW (vs UAB) | -0.8989 | 1.0746 | ±2.1491 | -0.837 | 0.4029 |  |
| **Season: spring (vs autumn)** | **+2.7959** | 1.1689 | ±2.3379 | **+2.392** | **0.0168** | * |
| Season: summer (vs autumn) | +1.1002 | 1.3384 | ±2.6768 | +0.822 | 0.4111 |  |
| **Season: winter (vs autumn)** | **+3.1944** | 1.2249 | ±2.4499 | **+2.608** | **0.0091** | ** |
| **Age (years)** | **-0.1020** | 0.0420 | ±0.0841 | **-2.427** | **0.0152** | * |
| **BMI (kg/m2)** | **+0.1830** | 0.0637 | ±0.1273 | **+2.874** | **0.0040** | ** |
| Hypertension | +1.2673 | 0.9810 | ±1.9619 | +1.292 | 0.1964 |  |
| High cholesterol | -0.7672 | 0.9089 | ±1.8179 | -0.844 | 0.3987 |  |
| Kidney disease | -1.0203 | 1.5987 | ±3.1975 | -0.638 | 0.5234 |  |
| Circulatory disease | +0.4885 | 1.3654 | ±2.7309 | +0.358 | 0.7205 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0205 | 0.0210 | ±0.0419 | -0.977 | 0.3287 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.0366**, Adj R² = **0.0256**, F-statistic = **3.35** (p = **2.55e-05**), Residual SE = **15.214** on **1236** df, AIC = **10376.1**, BIC = **10453.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.9324** | 3.6978 | ±7.3955 | **+34.327** | **3.13e-258** | *** |
| Education: graduate level (vs college) | -0.6405 | 0.9004 | ±1.8008 | -0.711 | 0.4768 |  |
| **Education: high school or below (vs college)** | **+4.3607** | 1.8845 | ±3.7690 | **+2.314** | **0.0207** | * |
| Site: UCSD (vs UAB) | +1.4157 | 1.2222 | ±2.4444 | +1.158 | 0.2467 |  |
| Site: UW (vs UAB) | -0.9026 | 1.0754 | ±2.1508 | -0.839 | 0.4013 |  |
| **Season: spring (vs autumn)** | **+2.7355** | 1.1684 | ±2.3368 | **+2.341** | **0.0192** | * |
| Season: summer (vs autumn) | +1.0885 | 1.3409 | ±2.6818 | +0.812 | 0.4169 |  |
| **Season: winter (vs autumn)** | **+3.1635** | 1.2242 | ±2.4485 | **+2.584** | **0.0098** | ** |
| **Age (years)** | **-0.0974** | 0.0424 | ±0.0847 | **-2.299** | **0.0215** | * |
| **BMI (kg/m2)** | **+0.1762** | 0.0631 | ±0.1262 | **+2.792** | **0.0052** | ** |
| Hypertension | +1.3374 | 0.9818 | ±1.9636 | +1.362 | 0.1731 |  |
| High cholesterol | -0.8251 | 0.9076 | ±1.8151 | -0.909 | 0.3633 |  |
| Kidney disease | -0.8177 | 1.5999 | ±3.1999 | -0.511 | 0.6093 |  |
| Circulatory disease | +0.5424 | 1.3637 | ±2.7274 | +0.398 | 0.6908 |  |
| Glucose SD, pooled (mg/dL) | -0.1035 | 0.0663 | ±0.1326 | -1.560 | 0.1187 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.0368**, Adj R² = **0.0259**, F-statistic = **3.37** (p = **2.27e-05**), Residual SE = **15.212** on **1236** df, AIC = **10375.8**, BIC = **10452.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.9093** | 3.6496 | ±7.2992 | **+34.774** | **6.11e-265** | *** |
| Education: graduate level (vs college) | -0.6280 | 0.9003 | ±1.8006 | -0.697 | 0.4855 |  |
| **Education: high school or below (vs college)** | **+4.3679** | 1.8845 | ±3.7690 | **+2.318** | **0.0205** | * |
| Site: UCSD (vs UAB) | +1.4207 | 1.2197 | ±2.4394 | +1.165 | 0.2441 |  |
| Site: UW (vs UAB) | -0.8884 | 1.0753 | ±2.1506 | -0.826 | 0.4087 |  |
| **Season: spring (vs autumn)** | **+2.7156** | 1.1683 | ±2.3366 | **+2.324** | **0.0201** | * |
| Season: summer (vs autumn) | +1.0624 | 1.3413 | ±2.6826 | +0.792 | 0.4283 |  |
| **Season: winter (vs autumn)** | **+3.1414** | 1.2247 | ±2.4494 | **+2.565** | **0.0103** | * |
| **Age (years)** | **-0.0966** | 0.0425 | ±0.0850 | **-2.272** | **0.0231** | * |
| **BMI (kg/m2)** | **+0.1776** | 0.0631 | ±0.1261 | **+2.817** | **0.0049** | ** |
| Hypertension | +1.3424 | 0.9804 | ±1.9607 | +1.369 | 0.1709 |  |
| High cholesterol | -0.8198 | 0.9075 | ±1.8151 | -0.903 | 0.3664 |  |
| Kidney disease | -0.7917 | 1.5971 | ±3.1942 | -0.496 | 0.6201 |  |
| Circulatory disease | +0.5427 | 1.3628 | ±2.7256 | +0.398 | 0.6905 |  |
| Avg. daily SD (mg/dL) | -0.1174 | 0.0724 | ±0.1447 | -1.622 | 0.1049 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **1251**, R² = **0.0359**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.53e-05**), Residual SE = **15.219** on **1236** df, AIC = **10377.0**, BIC = **10453.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.2596** | 3.8730 | ±7.7461 | **+32.858** | **8.81e-237** | *** |
| Education: graduate level (vs college) | -0.6886 | 0.9016 | ±1.8033 | -0.764 | 0.4450 |  |
| **Education: high school or below (vs college)** | **+4.2538** | 1.8926 | ±3.7852 | **+2.248** | **0.0246** | * |
| Site: UCSD (vs UAB) | +1.4203 | 1.2246 | ±2.4493 | +1.160 | 0.2461 |  |
| Site: UW (vs UAB) | -0.9665 | 1.0774 | ±2.1549 | -0.897 | 0.3697 |  |
| **Season: spring (vs autumn)** | **+2.7679** | 1.1681 | ±2.3362 | **+2.370** | **0.0178** | * |
| Season: summer (vs autumn) | +1.1471 | 1.3396 | ±2.6792 | +0.856 | 0.3918 |  |
| **Season: winter (vs autumn)** | **+3.2284** | 1.2242 | ±2.4484 | **+2.637** | **0.0084** | ** |
| **Age (years)** | **-0.0983** | 0.0423 | ±0.0847 | **-2.323** | **0.0202** | * |
| **BMI (kg/m2)** | **+0.1736** | 0.0633 | ±0.1266 | **+2.742** | **0.0061** | ** |
| Hypertension | +1.2684 | 0.9788 | ±1.9577 | +1.296 | 0.1950 |  |
| High cholesterol | -0.8704 | 0.9079 | ±1.8158 | -0.959 | 0.3377 |  |
| Kidney disease | -0.8881 | 1.5976 | ±3.1951 | -0.556 | 0.5783 |  |
| Circulatory disease | +0.4816 | 1.3639 | ±2.7277 | +0.353 | 0.7240 |  |
| CV (%) | -0.1329 | 0.1042 | ±0.2085 | -1.275 | 0.2024 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1251**, R² = **0.0364**, Adj R² = **0.0255**, F-statistic = **3.34** (p = **2.73e-05**), Residual SE = **15.215** on **1236** df, AIC = **10376.3**, BIC = **10453.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+121.7431** | 4.2786 | ±8.5572 | **+28.454** | **4.37e-178** | *** |
| Education: graduate level (vs college) | -0.6997 | 0.9015 | ±1.8029 | -0.776 | 0.4376 |  |
| **Education: high school or below (vs college)** | **+4.2898** | 1.8895 | ±3.7791 | **+2.270** | **0.0232** | * |
| Site: UCSD (vs UAB) | +1.4136 | 1.2246 | ±2.4493 | +1.154 | 0.2484 |  |
| Site: UW (vs UAB) | -0.9392 | 1.0760 | ±2.1520 | -0.873 | 0.3827 |  |
| **Season: spring (vs autumn)** | **+2.7863** | 1.1679 | ±2.3357 | **+2.386** | **0.0170** | * |
| Season: summer (vs autumn) | +1.1371 | 1.3395 | ±2.6791 | +0.849 | 0.3959 |  |
| **Season: winter (vs autumn)** | **+3.2518** | 1.2234 | ±2.4469 | **+2.658** | **0.0079** | ** |
| **Age (years)** | **-0.0978** | 0.0423 | ±0.0846 | **-2.312** | **0.0208** | * |
| **BMI (kg/m2)** | **+0.1733** | 0.0632 | ±0.1265 | **+2.741** | **0.0061** | ** |
| Hypertension | +1.2866 | 0.9795 | ±1.9590 | +1.314 | 0.1890 |  |
| High cholesterol | -0.8595 | 0.9068 | ±1.8136 | -0.948 | 0.3432 |  |
| Kidney disease | -0.9033 | 1.5973 | ±3.1945 | -0.566 | 0.5717 |  |
| Circulatory disease | +0.4760 | 1.3637 | ±2.7274 | +0.349 | 0.7271 |  |
| Mean / SD ratio | +0.5269 | 0.3576 | ±0.7153 | +1.473 | 0.1407 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.0364**, Adj R² = **0.0254**, F-statistic = **3.33** (p = **2.81e-05**), Residual SE = **15.216** on **1236** df, AIC = **10376.3**, BIC = **10453.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+121.7970** | 4.3489 | ±8.6979 | **+28.006** | **1.37e-172** | *** |
| Education: graduate level (vs college) | -0.6774 | 0.9008 | ±1.8015 | -0.752 | 0.4520 |  |
| **Education: high school or below (vs college)** | **+4.3229** | 1.8850 | ±3.7700 | **+2.293** | **0.0218** | * |
| Site: UCSD (vs UAB) | +1.4388 | 1.2208 | ±2.4416 | +1.179 | 0.2386 |  |
| Site: UW (vs UAB) | -0.9260 | 1.0757 | ±2.1515 | -0.861 | 0.3893 |  |
| **Season: spring (vs autumn)** | **+2.7799** | 1.1677 | ±2.3355 | **+2.381** | **0.0173** | * |
| Season: summer (vs autumn) | +1.1050 | 1.3402 | ±2.6803 | +0.825 | 0.4096 |  |
| **Season: winter (vs autumn)** | **+3.2335** | 1.2242 | ±2.4484 | **+2.641** | **0.0083** | ** |
| **Age (years)** | **-0.0968** | 0.0425 | ±0.0851 | **-2.276** | **0.0228** | * |
| **BMI (kg/m2)** | **+0.1762** | 0.0631 | ±0.1263 | **+2.791** | **0.0053** | ** |
| Hypertension | +1.2646 | 0.9779 | ±1.9558 | +1.293 | 0.1959 |  |
| High cholesterol | -0.8579 | 0.9072 | ±1.8145 | -0.946 | 0.3443 |  |
| Kidney disease | -0.8725 | 1.5944 | ±3.1888 | -0.547 | 0.5842 |  |
| Circulatory disease | +0.4639 | 1.3630 | ±2.7260 | +0.340 | 0.7336 |  |
| Avg. daily mean/SD | +0.4289 | 0.3033 | ±0.6066 | +1.414 | 0.1574 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1251**, R² = **0.0347**, Adj R² = **0.0237**, F-statistic = **3.17** (p = **6.30e-05**), Residual SE = **15.229** on **1236** df, AIC = **10378.5**, BIC = **10455.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.2274** | 4.0920 | ±8.1840 | **+30.603** | **1.11e-205** | *** |
| Education: graduate level (vs college) | -0.6584 | 0.9018 | ±1.8035 | -0.730 | 0.4653 |  |
| **Education: high school or below (vs college)** | **+4.3318** | 1.8819 | ±3.7639 | **+2.302** | **0.0213** | * |
| Site: UCSD (vs UAB) | +1.5050 | 1.2217 | ±2.4434 | +1.232 | 0.2180 |  |
| Site: UW (vs UAB) | -0.9616 | 1.0810 | ±2.1620 | -0.890 | 0.3737 |  |
| **Season: spring (vs autumn)** | **+2.7982** | 1.1679 | ±2.3357 | **+2.396** | **0.0166** | * |
| Season: summer (vs autumn) | +1.1494 | 1.3397 | ±2.6793 | +0.858 | 0.3909 |  |
| **Season: winter (vs autumn)** | **+3.2200** | 1.2268 | ±2.4535 | **+2.625** | **0.0087** | ** |
| **Age (years)** | **-0.1016** | 0.0419 | ±0.0838 | **-2.424** | **0.0153** | * |
| **BMI (kg/m2)** | **+0.1751** | 0.0635 | ±0.1270 | **+2.759** | **0.0058** | ** |
| Hypertension | +1.2077 | 0.9779 | ±1.9558 | +1.235 | 0.2168 |  |
| High cholesterol | -0.8276 | 0.9129 | ±1.8257 | -0.907 | 0.3646 |  |
| Kidney disease | -1.0250 | 1.6010 | ±3.2020 | -0.640 | 0.5220 |  |
| Circulatory disease | +0.4530 | 1.3655 | ±2.7309 | +0.332 | 0.7401 |  |
| MAG (mg/dL/h) | -0.0056 | 0.0558 | ±0.1117 | -0.101 | 0.9196 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **1251**, R² = **0.0360**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.42e-05**), Residual SE = **15.219** on **1236** df, AIC = **10376.9**, BIC = **10453.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.0247** | 3.7631 | ±7.5262 | **+33.755** | **8.97e-250** | *** |
| Education: graduate level (vs college) | -0.6313 | 0.9006 | ±1.8011 | -0.701 | 0.4833 |  |
| **Education: high school or below (vs college)** | **+4.3689** | 1.8865 | ±3.7730 | **+2.316** | **0.0206** | * |
| Site: UCSD (vs UAB) | +1.4361 | 1.2185 | ±2.4371 | +1.179 | 0.2386 |  |
| Site: UW (vs UAB) | -0.9288 | 1.0772 | ±2.1544 | -0.862 | 0.3886 |  |
| **Season: spring (vs autumn)** | **+2.7475** | 1.1682 | ±2.3365 | **+2.352** | **0.0187** | * |
| Season: summer (vs autumn) | +1.0818 | 1.3402 | ±2.6804 | +0.807 | 0.4196 |  |
| **Season: winter (vs autumn)** | **+3.1676** | 1.2265 | ±2.4531 | **+2.583** | **0.0098** | ** |
| **Age (years)** | **-0.0984** | 0.0424 | ±0.0849 | **-2.319** | **0.0204** | * |
| **BMI (kg/m2)** | **+0.1719** | 0.0633 | ±0.1266 | **+2.716** | **0.0066** | ** |
| Hypertension | +1.2818 | 0.9798 | ±1.9597 | +1.308 | 0.1908 |  |
| High cholesterol | -0.8473 | 0.9090 | ±1.8179 | -0.932 | 0.3513 |  |
| Kidney disease | -0.8820 | 1.5953 | ±3.1905 | -0.553 | 0.5804 |  |
| Circulatory disease | +0.5184 | 1.3645 | ±2.7290 | +0.380 | 0.7040 |  |
| Avg. daily range (mg/dL) | -0.0214 | 0.0175 | ±0.0350 | -1.223 | 0.2215 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **1251**, R² = **0.0359**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.53e-05**), Residual SE = **15.219** on **1236** df, AIC = **10377.0**, BIC = **10453.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.8623** | 3.6315 | ±7.2630 | **+34.658** | **3.33e-263** | *** |
| Education: graduate level (vs college) | -0.6562 | 0.9011 | ±1.8022 | -0.728 | 0.4665 |  |
| **Education: high school or below (vs college)** | **+4.3239** | 1.8846 | ±3.7691 | **+2.294** | **0.0218** | * |
| Site: UCSD (vs UAB) | +1.4418 | 1.2243 | ±2.4486 | +1.178 | 0.2389 |  |
| Site: UW (vs UAB) | -0.9390 | 1.0773 | ±2.1546 | -0.872 | 0.3834 |  |
| **Season: spring (vs autumn)** | **+2.8705** | 1.1727 | ±2.3454 | **+2.448** | **0.0144** | * |
| Season: summer (vs autumn) | +1.2126 | 1.3397 | ±2.6795 | +0.905 | 0.3654 |  |
| **Season: winter (vs autumn)** | **+3.2549** | 1.2230 | ±2.4461 | **+2.661** | **0.0078** | ** |
| **Age (years)** | **-0.1011** | 0.0419 | ±0.0838 | **-2.412** | **0.0159** | * |
| **BMI (kg/m2)** | **+0.1803** | 0.0630 | ±0.1260 | **+2.862** | **0.0042** | ** |
| Hypertension | +1.2300 | 0.9780 | ±1.9561 | +1.258 | 0.2085 |  |
| High cholesterol | -0.8000 | 0.9075 | ±1.8151 | -0.882 | 0.3780 |  |
| Kidney disease | -1.0221 | 1.6089 | ±3.2178 | -0.635 | 0.5253 |  |
| Circulatory disease | +0.5206 | 1.3655 | ±2.7311 | +0.381 | 0.7030 |  |
| SD of daily means (mg/dL) | -0.1641 | 0.1320 | ±0.2640 | -1.243 | 0.2139 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.19** (p = **5.84e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.3**, BIC = **10455.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.8036** | 6.3571 | ±12.7142 | **+19.318** | **3.83e-83** | *** |
| Education: graduate level (vs college) | -0.6470 | 0.9009 | ±1.8018 | -0.718 | 0.4726 |  |
| **Education: high school or below (vs college)** | **+4.3573** | 1.8819 | ±3.7638 | **+2.315** | **0.0206** | * |
| Site: UCSD (vs UAB) | +1.4828 | 1.2188 | ±2.4376 | +1.217 | 0.2237 |  |
| Site: UW (vs UAB) | -0.9532 | 1.0786 | ±2.1572 | -0.884 | 0.3769 |  |
| **Season: spring (vs autumn)** | **+2.7812** | 1.1699 | ±2.3398 | **+2.377** | **0.0174** | * |
| Season: summer (vs autumn) | +1.1159 | 1.3422 | ±2.6844 | +0.831 | 0.4057 |  |
| **Season: winter (vs autumn)** | **+3.2048** | 1.2267 | ±2.4535 | **+2.612** | **0.0090** | ** |
| **Age (years)** | **-0.1013** | 0.0420 | ±0.0840 | **-2.411** | **0.0159** | * |
| **BMI (kg/m2)** | **+0.1760** | 0.0634 | ±0.1269 | **+2.775** | **0.0055** | ** |
| Hypertension | +1.2309 | 0.9831 | ±1.9662 | +1.252 | 0.2106 |  |
| High cholesterol | -0.8139 | 0.9094 | ±1.8188 | -0.895 | 0.3708 |  |
| Kidney disease | -0.9895 | 1.5998 | ±3.1996 | -0.619 | 0.5362 |  |
| Circulatory disease | +0.4810 | 1.3670 | ±2.7340 | +0.352 | 0.7249 |  |
| Time in range 70-180, pooled (%) | +0.0226 | 0.0538 | ±0.1077 | +0.419 | 0.6753 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.18** (p = **5.91e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.9891** | 6.3908 | ±12.7816 | **+19.245** | **1.56e-82** | *** |
| Education: graduate level (vs college) | -0.6478 | 0.9009 | ±1.8018 | -0.719 | 0.4721 |  |
| **Education: high school or below (vs college)** | **+4.3527** | 1.8819 | ±3.7639 | **+2.313** | **0.0207** | * |
| Site: UCSD (vs UAB) | +1.4865 | 1.2185 | ±2.4370 | +1.220 | 0.2225 |  |
| Site: UW (vs UAB) | -0.9538 | 1.0787 | ±2.1575 | -0.884 | 0.3766 |  |
| **Season: spring (vs autumn)** | **+2.7846** | 1.1697 | ±2.3394 | **+2.381** | **0.0173** | * |
| Season: summer (vs autumn) | +1.1189 | 1.3420 | ±2.6841 | +0.834 | 0.4045 |  |
| **Season: winter (vs autumn)** | **+3.2070** | 1.2269 | ±2.4537 | **+2.614** | **0.0090** | ** |
| **Age (years)** | **-0.1012** | 0.0420 | ±0.0840 | **-2.410** | **0.0159** | * |
| **BMI (kg/m2)** | **+0.1761** | 0.0635 | ±0.1269 | **+2.774** | **0.0055** | ** |
| Hypertension | +1.2284 | 0.9832 | ±1.9664 | +1.249 | 0.2115 |  |
| High cholesterol | -0.8137 | 0.9093 | ±1.8187 | -0.895 | 0.3709 |  |
| Kidney disease | -0.9928 | 1.5998 | ±3.1996 | -0.621 | 0.5349 |  |
| Circulatory disease | +0.4784 | 1.3672 | ±2.7344 | +0.350 | 0.7264 |  |
| Avg. daily time in range 70-180 (%) | +0.0205 | 0.0538 | ±0.1076 | +0.382 | 0.7026 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.0356**, Adj R² = **0.0247**, F-statistic = **3.26** (p = **4.01e-05**), Residual SE = **15.221** on **1236** df, AIC = **10377.3**, BIC = **10454.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.5442** | 3.5081 | ±7.0161 | **+35.787** | **1.74e-280** | *** |
| Education: graduate level (vs college) | -0.7000 | 0.9041 | ±1.8082 | -0.774 | 0.4388 |  |
| **Education: high school or below (vs college)** | **+4.2006** | 1.8873 | ±3.7745 | **+2.226** | **0.0260** | * |
| Site: UCSD (vs UAB) | +1.3626 | 1.2262 | ±2.4523 | +1.111 | 0.2664 |  |
| Site: UW (vs UAB) | -1.0205 | 1.0729 | ±2.1458 | -0.951 | 0.3415 |  |
| **Season: spring (vs autumn)** | **+2.7952** | 1.1675 | ±2.3351 | **+2.394** | **0.0167** | * |
| Season: summer (vs autumn) | +1.1272 | 1.3394 | ±2.6788 | +0.842 | 0.4000 |  |
| **Season: winter (vs autumn)** | **+3.1984** | 1.2288 | ±2.4576 | **+2.603** | **0.0092** | ** |
| **Age (years)** | **-0.1042** | 0.0416 | ±0.0831 | **-2.507** | **0.0122** | * |
| **BMI (kg/m2)** | **+0.1777** | 0.0636 | ±0.1271 | **+2.796** | **0.0052** | ** |
| Hypertension | +1.2084 | 0.9763 | ±1.9526 | +1.238 | 0.2158 |  |
| High cholesterol | -0.8765 | 0.9074 | ±1.8148 | -0.966 | 0.3341 |  |
| Kidney disease | -1.0318 | 1.6037 | ±3.2074 | -0.643 | 0.5200 |  |
| Circulatory disease | +0.5427 | 1.3700 | ±2.7399 | +0.396 | 0.6920 |  |
| Any reading < 54 during wear (0/1) | -1.0360 | 0.9449 | ±1.8897 | -1.096 | 0.2729 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0238**, F-statistic = **3.18** (p = **6.07e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0992** | 3.5635 | ±7.1270 | **+35.106** | **5.49e-270** | *** |
| Education: graduate level (vs college) | -0.6626 | 0.9015 | ±1.8029 | -0.735 | 0.4624 |  |
| **Education: high school or below (vs college)** | **+4.3009** | 1.8796 | ±3.7593 | **+2.288** | **0.0221** | * |
| Site: UCSD (vs UAB) | +1.4671 | 1.2217 | ±2.4434 | +1.201 | 0.2298 |  |
| Site: UW (vs UAB) | -0.9884 | 1.0798 | ±2.1597 | -0.915 | 0.3600 |  |
| **Season: spring (vs autumn)** | **+2.7959** | 1.1685 | ±2.3370 | **+2.393** | **0.0167** | * |
| Season: summer (vs autumn) | +1.1625 | 1.3393 | ±2.6786 | +0.868 | 0.3854 |  |
| **Season: winter (vs autumn)** | **+3.2281** | 1.2258 | ±2.4515 | **+2.634** | **0.0085** | ** |
| **Age (years)** | **-0.1017** | 0.0419 | ±0.0839 | **-2.425** | **0.0153** | * |
| **BMI (kg/m2)** | **+0.1748** | 0.0635 | ±0.1270 | **+2.752** | **0.0059** | ** |
| Hypertension | +1.1987 | 0.9779 | ±1.9558 | +1.226 | 0.2203 |  |
| High cholesterol | -0.8430 | 0.9105 | ±1.8210 | -0.926 | 0.3545 |  |
| Kidney disease | -1.0227 | 1.6046 | ±3.2092 | -0.637 | 0.5239 |  |
| Circulatory disease | +0.4496 | 1.3650 | ±2.7299 | +0.329 | 0.7419 |  |
| Time < 54 (%) | -0.2529 | 0.6931 | ±1.3862 | -0.365 | 0.7152 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0238**, F-statistic = **3.18** (p = **6.07e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0673** | 3.5573 | ±7.1145 | **+35.158** | **8.69e-271** | *** |
| Education: graduate level (vs college) | -0.6650 | 0.9010 | ±1.8021 | -0.738 | 0.4605 |  |
| **Education: high school or below (vs college)** | **+4.3011** | 1.8800 | ±3.7599 | **+2.288** | **0.0221** | * |
| Site: UCSD (vs UAB) | +1.4730 | 1.2224 | ±2.4448 | +1.205 | 0.2282 |  |
| Site: UW (vs UAB) | -0.9933 | 1.0811 | ±2.1622 | -0.919 | 0.3582 |  |
| **Season: spring (vs autumn)** | **+2.8002** | 1.1680 | ±2.3359 | **+2.398** | **0.0165** | * |
| Season: summer (vs autumn) | +1.1643 | 1.3410 | ±2.6820 | +0.868 | 0.3853 |  |
| **Season: winter (vs autumn)** | **+3.2355** | 1.2268 | ±2.4535 | **+2.637** | **0.0084** | ** |
| **Age (years)** | **-0.1014** | 0.0420 | ±0.0839 | **-2.416** | **0.0157** | * |
| **BMI (kg/m2)** | **+0.1749** | 0.0635 | ±0.1271 | **+2.753** | **0.0059** | ** |
| Hypertension | +1.1937 | 0.9774 | ±1.9548 | +1.221 | 0.2220 |  |
| High cholesterol | -0.8405 | 0.9104 | ±1.8208 | -0.923 | 0.3559 |  |
| Kidney disease | -1.0227 | 1.6012 | ±3.2025 | -0.639 | 0.5230 |  |
| Circulatory disease | +0.4474 | 1.3648 | ±2.7296 | +0.328 | 0.7430 |  |
| Avg. daily time < 54 (%) | -0.3362 | 0.9900 | ±1.9801 | -0.340 | 0.7342 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0238**, F-statistic = **3.18** (p = **6.04e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1122** | 3.5517 | ±7.1034 | **+35.226** | **8.00e-272** | *** |
| Education: graduate level (vs college) | -0.6734 | 0.9043 | ±1.8086 | -0.745 | 0.4565 |  |
| **Education: high school or below (vs college)** | **+4.2842** | 1.8816 | ±3.7631 | **+2.277** | **0.0228** | * |
| Site: UCSD (vs UAB) | +1.4806 | 1.2247 | ±2.4494 | +1.209 | 0.2267 |  |
| Site: UW (vs UAB) | -0.9899 | 1.0729 | ±2.1458 | -0.923 | 0.3562 |  |
| **Season: spring (vs autumn)** | **+2.8062** | 1.1686 | ±2.3372 | **+2.401** | **0.0163** | * |
| Season: summer (vs autumn) | +1.1593 | 1.3399 | ±2.6798 | +0.865 | 0.3869 |  |
| **Season: winter (vs autumn)** | **+3.2438** | 1.2232 | ±2.4464 | **+2.652** | **0.0080** | ** |
| **Age (years)** | **-0.1020** | 0.0419 | ±0.0838 | **-2.434** | **0.0149** | * |
| **BMI (kg/m2)** | **+0.1757** | 0.0635 | ±0.1270 | **+2.767** | **0.0057** | ** |
| Hypertension | +1.1954 | 0.9754 | ±1.9509 | +1.226 | 0.2204 |  |
| High cholesterol | -0.8408 | 0.9095 | ±1.8191 | -0.924 | 0.3553 |  |
| Kidney disease | -1.0322 | 1.6012 | ±3.2025 | -0.645 | 0.5192 |  |
| Circulatory disease | +0.4513 | 1.3650 | ±2.7299 | +0.331 | 0.7409 |  |
| Time 54-69, pooled (%) | -0.1084 | 0.3288 | ±0.6576 | -0.330 | 0.7417 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.18** (p = **5.90e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.3**, BIC = **10455.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1140** | 3.5522 | ±7.1044 | **+35.221** | **9.42e-272** | *** |
| Education: graduate level (vs college) | -0.6793 | 0.9055 | ±1.8110 | -0.750 | 0.4531 |  |
| **Education: high school or below (vs college)** | **+4.2712** | 1.8827 | ±3.7654 | **+2.269** | **0.0233** | * |
| Site: UCSD (vs UAB) | +1.4815 | 1.2241 | ±2.4482 | +1.210 | 0.2262 |  |
| Site: UW (vs UAB) | -0.9985 | 1.0740 | ±2.1480 | -0.930 | 0.3525 |  |
| **Season: spring (vs autumn)** | **+2.8079** | 1.1685 | ±2.3370 | **+2.403** | **0.0163** | * |
| Season: summer (vs autumn) | +1.1571 | 1.3403 | ±2.6806 | +0.863 | 0.3880 |  |
| **Season: winter (vs autumn)** | **+3.2528** | 1.2223 | ±2.4446 | **+2.661** | **0.0078** | ** |
| **Age (years)** | **-0.1018** | 0.0419 | ±0.0838 | **-2.430** | **0.0151** | * |
| **BMI (kg/m2)** | **+0.1759** | 0.0635 | ±0.1270 | **+2.770** | **0.0056** | ** |
| Hypertension | +1.1902 | 0.9749 | ±1.9497 | +1.221 | 0.2221 |  |
| High cholesterol | -0.8430 | 0.9097 | ±1.8193 | -0.927 | 0.3541 |  |
| Kidney disease | -1.0331 | 1.6002 | ±3.2003 | -0.646 | 0.5185 |  |
| Circulatory disease | +0.4505 | 1.3648 | ±2.7295 | +0.330 | 0.7413 |  |
| Avg. daily time 54-69 (%) | -0.1343 | 0.3410 | ±0.6820 | -0.394 | 0.6936 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.18** (p = **5.98e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1362** | 3.5559 | ±7.1118 | **+35.191** | **2.75e-271** | *** |
| Education: graduate level (vs college) | -0.6734 | 0.9035 | ±1.8071 | -0.745 | 0.4561 |  |
| **Education: high school or below (vs college)** | **+4.2795** | 1.8810 | ±3.7620 | **+2.275** | **0.0229** | * |
| Site: UCSD (vs UAB) | +1.4673 | 1.2263 | ±2.4526 | +1.197 | 0.2315 |  |
| Site: UW (vs UAB) | -0.9984 | 1.0743 | ±2.1486 | -0.929 | 0.3527 |  |
| **Season: spring (vs autumn)** | **+2.8037** | 1.1683 | ±2.3366 | **+2.400** | **0.0164** | * |
| Season: summer (vs autumn) | +1.1619 | 1.3400 | ±2.6801 | +0.867 | 0.3859 |  |
| **Season: winter (vs autumn)** | **+3.2430** | 1.2242 | ±2.4485 | **+2.649** | **0.0081** | ** |
| **Age (years)** | **-0.1020** | 0.0419 | ±0.0838 | **-2.435** | **0.0149** | * |
| **BMI (kg/m2)** | **+0.1755** | 0.0635 | ±0.1270 | **+2.765** | **0.0057** | ** |
| Hypertension | +1.1934 | 0.9760 | ±1.9521 | +1.223 | 0.2214 |  |
| High cholesterol | -0.8461 | 0.9099 | ±1.8199 | -0.930 | 0.3524 |  |
| Kidney disease | -1.0291 | 1.6031 | ±3.2062 | -0.642 | 0.5209 |  |
| Circulatory disease | +0.4506 | 1.3649 | ±2.7298 | +0.330 | 0.7413 |  |
| Time < 70 (%) | -0.0949 | 0.2550 | ±0.5100 | -0.372 | 0.7097 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.19** (p = **5.88e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.3**, BIC = **10455.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1218** | 3.5535 | ±7.1070 | **+35.211** | **1.38e-271** | *** |
| Education: graduate level (vs college) | -0.6790 | 0.9045 | ±1.8090 | -0.751 | 0.4529 |  |
| **Education: high school or below (vs college)** | **+4.2699** | 1.8822 | ±3.7643 | **+2.269** | **0.0233** | * |
| Site: UCSD (vs UAB) | +1.4721 | 1.2255 | ±2.4511 | +1.201 | 0.2297 |  |
| Site: UW (vs UAB) | -1.0059 | 1.0752 | ±2.1504 | -0.936 | 0.3495 |  |
| **Season: spring (vs autumn)** | **+2.8068** | 1.1683 | ±2.3365 | **+2.403** | **0.0163** | * |
| Season: summer (vs autumn) | +1.1602 | 1.3408 | ±2.6817 | +0.865 | 0.3869 |  |
| **Season: winter (vs autumn)** | **+3.2528** | 1.2235 | ±2.4469 | **+2.659** | **0.0078** | ** |
| **Age (years)** | **-0.1018** | 0.0419 | ±0.0838 | **-2.428** | **0.0152** | * |
| **BMI (kg/m2)** | **+0.1757** | 0.0635 | ±0.1270 | **+2.767** | **0.0057** | ** |
| Hypertension | +1.1877 | 0.9751 | ±1.9503 | +1.218 | 0.2232 |  |
| High cholesterol | -0.8463 | 0.9099 | ±1.8198 | -0.930 | 0.3523 |  |
| Kidney disease | -1.0301 | 1.6010 | ±3.2019 | -0.643 | 0.5199 |  |
| Circulatory disease | +0.4493 | 1.3647 | ±2.7293 | +0.329 | 0.7420 |  |
| Avg. daily time < 70 (%) | -0.1155 | 0.2809 | ±0.5618 | -0.411 | 0.6809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.0360**, Adj R² = **0.0251**, F-statistic = **3.29** (p = **3.38e-05**), Residual SE = **15.219** on **1236** df, AIC = **10376.8**, BIC = **10453.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+113.7317** | 7.4783 | ±14.9566 | **+15.208** | **3.12e-52** | *** |
| Education: graduate level (vs college) | -0.6498 | 0.9007 | ±1.8015 | -0.721 | 0.4707 |  |
| **Education: high school or below (vs college)** | **+4.4815** | 1.8819 | ±3.7638 | **+2.381** | **0.0172** | * |
| Site: UCSD (vs UAB) | +1.4635 | 1.2167 | ±2.4334 | +1.203 | 0.2290 |  |
| Site: UW (vs UAB) | -0.9844 | 1.0770 | ±2.1540 | -0.914 | 0.3607 |  |
| **Season: spring (vs autumn)** | **+2.7791** | 1.1690 | ±2.3380 | **+2.377** | **0.0174** | * |
| Season: summer (vs autumn) | +1.0939 | 1.3399 | ±2.6797 | +0.816 | 0.4143 |  |
| **Season: winter (vs autumn)** | **+3.2057** | 1.2249 | ±2.4497 | **+2.617** | **0.0089** | ** |
| **Age (years)** | **-0.1021** | 0.0419 | ±0.0839 | **-2.435** | **0.0149** | * |
| **BMI (kg/m2)** | **+0.1752** | 0.0632 | ±0.1264 | **+2.771** | **0.0056** | ** |
| Hypertension | +1.2202 | 0.9763 | ±1.9525 | +1.250 | 0.2113 |  |
| High cholesterol | -0.8448 | 0.9094 | ±1.8187 | -0.929 | 0.3529 |  |
| Kidney disease | -1.0079 | 1.6036 | ±3.2072 | -0.629 | 0.5297 |  |
| Circulatory disease | +0.5681 | 1.3723 | ±2.7446 | +0.414 | 0.6789 |  |
| Time 54-250, pooled (%) | +0.1140 | 0.0669 | ±0.1339 | +1.703 | 0.0885 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.0360**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.41e-05**), Residual SE = **15.219** on **1236** df, AIC = **10376.9**, BIC = **10453.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+113.5416** | 7.8240 | ±15.6481 | **+14.512** | **1.02e-47** | *** |
| Education: graduate level (vs college) | -0.6496 | 0.9007 | ±1.8014 | -0.721 | 0.4708 |  |
| **Education: high school or below (vs college)** | **+4.4856** | 1.8825 | ±3.7650 | **+2.383** | **0.0172** | * |
| Site: UCSD (vs UAB) | +1.4699 | 1.2168 | ±2.4336 | +1.208 | 0.2271 |  |
| Site: UW (vs UAB) | -0.9808 | 1.0770 | ±2.1540 | -0.911 | 0.3625 |  |
| **Season: spring (vs autumn)** | **+2.7799** | 1.1689 | ±2.3379 | **+2.378** | **0.0174** | * |
| Season: summer (vs autumn) | +1.0927 | 1.3397 | ±2.6794 | +0.816 | 0.4147 |  |
| **Season: winter (vs autumn)** | **+3.2049** | 1.2250 | ±2.4500 | **+2.616** | **0.0089** | ** |
| **Age (years)** | **-0.1019** | 0.0419 | ±0.0839 | **-2.431** | **0.0151** | * |
| **BMI (kg/m2)** | **+0.1755** | 0.0632 | ±0.1264 | **+2.776** | **0.0055** | ** |
| Hypertension | +1.2198 | 0.9762 | ±1.9525 | +1.249 | 0.2115 |  |
| High cholesterol | -0.8426 | 0.9094 | ±1.8187 | -0.927 | 0.3542 |  |
| Kidney disease | -1.0112 | 1.6031 | ±3.2063 | -0.631 | 0.5282 |  |
| Circulatory disease | +0.5687 | 1.3725 | ±2.7449 | +0.414 | 0.6786 |  |
| Avg. daily time 54-250 (%) | +0.1156 | 0.0706 | ±0.1412 | +1.638 | 0.1015 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.19** (p = **5.87e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.3**, BIC = **10455.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.9815** | 3.5613 | ±7.1227 | **+35.094** | **8.36e-270** | *** |
| Education: graduate level (vs college) | -0.6737 | 0.9014 | ±1.8029 | -0.747 | 0.4548 |  |
| **Education: high school or below (vs college)** | **+4.3164** | 1.8790 | ±3.7580 | **+2.297** | **0.0216** | * |
| Site: UCSD (vs UAB) | +1.5332 | 1.2181 | ±2.4362 | +1.259 | 0.2081 |  |
| Site: UW (vs UAB) | -0.9733 | 1.0781 | ±2.1562 | -0.903 | 0.3666 |  |
| **Season: spring (vs autumn)** | **+2.8239** | 1.1685 | ±2.3369 | **+2.417** | **0.0157** | * |
| Season: summer (vs autumn) | +1.1921 | 1.3420 | ±2.6840 | +0.888 | 0.3744 |  |
| **Season: winter (vs autumn)** | **+3.2512** | 1.2273 | ±2.4545 | **+2.649** | **0.0081** | ** |
| **Age (years)** | **-0.1021** | 0.0420 | ±0.0841 | **-2.428** | **0.0152** | * |
| **BMI (kg/m2)** | **+0.1738** | 0.0638 | ±0.1276 | **+2.724** | **0.0064** | ** |
| Hypertension | +1.1756 | 0.9886 | ±1.9772 | +1.189 | 0.2344 |  |
| High cholesterol | -0.8469 | 0.9127 | ±1.8253 | -0.928 | 0.3534 |  |
| Kidney disease | -1.0823 | 1.5995 | ±3.1990 | -0.677 | 0.4986 |  |
| Circulatory disease | +0.4421 | 1.3651 | ±2.7302 | +0.324 | 0.7460 |  |
| Time 181-250, pooled (%) | +0.0319 | 0.0908 | ±0.1816 | +0.352 | 0.7249 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1251**, R² = **0.0349**, Adj R² = **0.0239**, F-statistic = **3.19** (p = **5.79e-05**), Residual SE = **15.227** on **1236** df, AIC = **10378.3**, BIC = **10455.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.9817** | 3.5606 | ±7.1213 | **+35.101** | **6.50e-270** | *** |
| Education: graduate level (vs college) | -0.6758 | 0.9014 | ±1.8028 | -0.750 | 0.4534 |  |
| **Education: high school or below (vs college)** | **+4.3187** | 1.8793 | ±3.7587 | **+2.298** | **0.0216** | * |
| Site: UCSD (vs UAB) | +1.5374 | 1.2178 | ±2.4357 | +1.262 | 0.2068 |  |
| Site: UW (vs UAB) | -0.9727 | 1.0784 | ±2.1567 | -0.902 | 0.3671 |  |
| **Season: spring (vs autumn)** | **+2.8233** | 1.1684 | ±2.3369 | **+2.416** | **0.0157** | * |
| Season: summer (vs autumn) | +1.1948 | 1.3419 | ±2.6838 | +0.890 | 0.3733 |  |
| **Season: winter (vs autumn)** | **+3.2534** | 1.2273 | ±2.4546 | **+2.651** | **0.0080** | ** |
| **Age (years)** | **-0.1021** | 0.0420 | ±0.0841 | **-2.428** | **0.0152** | * |
| **BMI (kg/m2)** | **+0.1737** | 0.0638 | ±0.1277 | **+2.720** | **0.0065** | ** |
| Hypertension | +1.1732 | 0.9884 | ±1.9767 | +1.187 | 0.2352 |  |
| High cholesterol | -0.8492 | 0.9125 | ±1.8251 | -0.931 | 0.3520 |  |
| Kidney disease | -1.0880 | 1.5997 | ±3.1995 | -0.680 | 0.4964 |  |
| Circulatory disease | +0.4409 | 1.3652 | ±2.7303 | +0.323 | 0.7467 |  |
| Avg. daily time 181-250 (%) | +0.0344 | 0.0893 | ±0.1786 | +0.385 | 0.7004 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.18** (p = **5.98e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0212** | 3.5553 | ±7.1106 | **+35.165** | **6.96e-271** | *** |
| Education: graduate level (vs college) | -0.6454 | 0.9011 | ±1.8021 | -0.716 | 0.4739 |  |
| **Education: high school or below (vs college)** | **+4.3622** | 1.8820 | ±3.7641 | **+2.318** | **0.0205** | * |
| Site: UCSD (vs UAB) | +1.4970 | 1.2179 | ±2.4357 | +1.229 | 0.2190 |  |
| Site: UW (vs UAB) | -0.9443 | 1.0781 | ±2.1563 | -0.876 | 0.3811 |  |
| **Season: spring (vs autumn)** | **+2.7837** | 1.1699 | ±2.3399 | **+2.379** | **0.0173** | * |
| Season: summer (vs autumn) | +1.1204 | 1.3424 | ±2.6848 | +0.835 | 0.4039 |  |
| **Season: winter (vs autumn)** | **+3.2040** | 1.2268 | ±2.4536 | **+2.612** | **0.0090** | ** |
| **Age (years)** | **-0.1012** | 0.0420 | ±0.0840 | **-2.409** | **0.0160** | * |
| **BMI (kg/m2)** | **+0.1758** | 0.0635 | ±0.1269 | **+2.770** | **0.0056** | ** |
| Hypertension | +1.2301 | 0.9840 | ±1.9680 | +1.250 | 0.2113 |  |
| High cholesterol | -0.8108 | 0.9093 | ±1.8185 | -0.892 | 0.3726 |  |
| Kidney disease | -0.9963 | 1.5994 | ±3.1988 | -0.623 | 0.5333 |  |
| Circulatory disease | +0.4763 | 1.3667 | ±2.7334 | +0.349 | 0.7274 |  |
| Time > 180 (%) | -0.0189 | 0.0542 | ±0.1083 | -0.349 | 0.7273 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0238**, F-statistic = **3.18** (p = **6.05e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0160** | 3.5550 | ±7.1100 | **+35.166** | **6.58e-271** | *** |
| Education: graduate level (vs college) | -0.6464 | 0.9011 | ±1.8022 | -0.717 | 0.4732 |  |
| **Education: high school or below (vs college)** | **+4.3563** | 1.8821 | ±3.7641 | **+2.315** | **0.0206** | * |
| Site: UCSD (vs UAB) | +1.4976 | 1.2176 | ±2.4352 | +1.230 | 0.2187 |  |
| Site: UW (vs UAB) | -0.9462 | 1.0784 | ±2.1568 | -0.877 | 0.3803 |  |
| **Season: spring (vs autumn)** | **+2.7868** | 1.1699 | ±2.3398 | **+2.382** | **0.0172** | * |
| Season: summer (vs autumn) | +1.1246 | 1.3423 | ±2.6847 | +0.838 | 0.4021 |  |
| **Season: winter (vs autumn)** | **+3.2060** | 1.2270 | ±2.4540 | **+2.613** | **0.0090** | ** |
| **Age (years)** | **-0.1012** | 0.0420 | ±0.0840 | **-2.410** | **0.0159** | * |
| **BMI (kg/m2)** | **+0.1758** | 0.0635 | ±0.1270 | **+2.768** | **0.0056** | ** |
| Hypertension | +1.2275 | 0.9842 | ±1.9683 | +1.247 | 0.2123 |  |
| High cholesterol | -0.8121 | 0.9092 | ±1.8185 | -0.893 | 0.3718 |  |
| Kidney disease | -1.0000 | 1.5995 | ±3.1989 | -0.625 | 0.5318 |  |
| Circulatory disease | +0.4735 | 1.3670 | ±2.7340 | +0.346 | 0.7290 |  |
| Avg. daily time > 180 (%) | -0.0166 | 0.0541 | ±0.1082 | -0.307 | 0.7590 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.18** (p = **5.89e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.3**, BIC = **10455.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.9797** | 3.5537 | ±7.1075 | **+35.168** | **6.07e-271** | *** |
| Education: graduate level (vs college) | -0.6554 | 0.9011 | ±1.8022 | -0.727 | 0.4670 |  |
| **Education: high school or below (vs college)** | **+4.3627** | 1.8818 | ±3.7636 | **+2.318** | **0.0204** | * |
| Site: UCSD (vs UAB) | +1.5008 | 1.2179 | ±2.4357 | +1.232 | 0.2178 |  |
| Site: UW (vs UAB) | -0.9475 | 1.0781 | ±2.1561 | -0.879 | 0.3794 |  |
| **Season: spring (vs autumn)** | **+2.8008** | 1.1692 | ±2.3383 | **+2.396** | **0.0166** | * |
| Season: summer (vs autumn) | +1.1232 | 1.3410 | ±2.6820 | +0.838 | 0.4023 |  |
| **Season: winter (vs autumn)** | **+3.2186** | 1.2262 | ±2.4524 | **+2.625** | **0.0087** | ** |
| **Age (years)** | **-0.1017** | 0.0420 | ±0.0840 | **-2.421** | **0.0155** | * |
| **BMI (kg/m2)** | **+0.1774** | 0.0636 | ±0.1271 | **+2.792** | **0.0052** | ** |
| Hypertension | +1.2207 | 0.9808 | ±1.9616 | +1.245 | 0.2133 |  |
| High cholesterol | -0.8030 | 0.9086 | ±1.8173 | -0.884 | 0.3768 |  |
| Kidney disease | -1.0313 | 1.5989 | ±3.1978 | -0.645 | 0.5189 |  |
| Circulatory disease | +0.4636 | 1.3664 | ±2.7329 | +0.339 | 0.7344 |  |
| Nocturnal time > 180 (%) | -0.0224 | 0.0586 | ±0.1172 | -0.382 | 0.7024 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0238**, F-statistic = **3.18** (p = **6.07e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.8954** | 3.5468 | ±7.0936 | **+35.213** | **1.25e-271** | *** |
| Education: graduate level (vs college) | -0.6541 | 0.9012 | ±1.8024 | -0.726 | 0.4680 |  |
| **Education: high school or below (vs college)** | **+4.3291** | 1.8809 | ±3.7619 | **+2.302** | **0.0214** | * |
| Site: UCSD (vs UAB) | +1.5213 | 1.2172 | ±2.4345 | +1.250 | 0.2114 |  |
| Site: UW (vs UAB) | -0.9596 | 1.0795 | ±2.1590 | -0.889 | 0.3740 |  |
| **Season: spring (vs autumn)** | **+2.8221** | 1.1665 | ±2.3330 | **+2.419** | **0.0156** | * |
| Season: summer (vs autumn) | +1.1708 | 1.3402 | ±2.6804 | +0.874 | 0.3823 |  |
| **Season: winter (vs autumn)** | **+3.2411** | 1.2255 | ±2.4509 | **+2.645** | **0.0082** | ** |
| **Age (years)** | **-0.1018** | 0.0420 | ±0.0841 | **-2.421** | **0.0155** | * |
| **BMI (kg/m2)** | **+0.1766** | 0.0636 | ±0.1272 | **+2.777** | **0.0055** | ** |
| Hypertension | +1.1865 | 0.9827 | ±1.9654 | +1.207 | 0.2273 |  |
| High cholesterol | -0.8290 | 0.9102 | ±1.8204 | -0.911 | 0.3624 |  |
| Kidney disease | -1.0390 | 1.5983 | ±3.1965 | -0.650 | 0.5156 |  |
| Circulatory disease | +0.4543 | 1.3663 | ±2.7326 | +0.333 | 0.7395 |  |
| Any reading > 250 during wear (0/1) | +0.3625 | 1.0810 | ±2.1620 | +0.335 | 0.7374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.0359**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.49e-05**), Residual SE = **15.219** on **1236** df, AIC = **10376.9**, BIC = **10453.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0842** | 3.5508 | ±7.1016 | **+35.227** | **7.72e-272** | *** |
| Education: graduate level (vs college) | -0.6474 | 0.9007 | ±1.8014 | -0.719 | 0.4723 |  |
| **Education: high school or below (vs college)** | **+4.4905** | 1.8823 | ±3.7647 | **+2.386** | **0.0171** | * |
| Site: UCSD (vs UAB) | +1.4850 | 1.2168 | ±2.4337 | +1.220 | 0.2223 |  |
| Site: UW (vs UAB) | -0.9683 | 1.0769 | ±2.1538 | -0.899 | 0.3686 |  |
| **Season: spring (vs autumn)** | **+2.7817** | 1.1689 | ±2.3378 | **+2.380** | **0.0173** | * |
| Season: summer (vs autumn) | +1.0912 | 1.3394 | ±2.6789 | +0.815 | 0.4153 |  |
| **Season: winter (vs autumn)** | **+3.2041** | 1.2251 | ±2.4503 | **+2.615** | **0.0089** | ** |
| **Age (years)** | **-0.1020** | 0.0419 | ±0.0839 | **-2.432** | **0.0150** | * |
| **BMI (kg/m2)** | **+0.1753** | 0.0632 | ±0.1264 | **+2.772** | **0.0056** | ** |
| Hypertension | +1.2242 | 0.9764 | ±1.9527 | +1.254 | 0.2099 |  |
| High cholesterol | -0.8354 | 0.9092 | ±1.8183 | -0.919 | 0.3581 |  |
| Kidney disease | -1.0116 | 1.6022 | ±3.2043 | -0.631 | 0.5278 |  |
| Circulatory disease | +0.5666 | 1.3723 | ±2.7445 | +0.413 | 0.6797 |  |
| Time > 250 (%) | -0.1118 | 0.0675 | ±0.1351 | -1.655 | 0.0979 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.0359**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.49e-05**), Residual SE = **15.219** on **1236** df, AIC = **10376.9**, BIC = **10453.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0749** | 3.5504 | ±7.1009 | **+35.228** | **7.45e-272** | *** |
| Education: graduate level (vs college) | -0.6470 | 0.9007 | ±1.8014 | -0.718 | 0.4726 |  |
| **Education: high school or below (vs college)** | **+4.4922** | 1.8828 | ±3.7655 | **+2.386** | **0.0170** | * |
| Site: UCSD (vs UAB) | +1.4842 | 1.2169 | ±2.4337 | +1.220 | 0.2226 |  |
| Site: UW (vs UAB) | -0.9669 | 1.0769 | ±2.1538 | -0.898 | 0.3693 |  |
| **Season: spring (vs autumn)** | **+2.7804** | 1.1689 | ±2.3379 | **+2.379** | **0.0174** | * |
| Season: summer (vs autumn) | +1.0901 | 1.3394 | ±2.6789 | +0.814 | 0.4157 |  |
| **Season: winter (vs autumn)** | **+3.2012** | 1.2252 | ±2.4505 | **+2.613** | **0.0090** | ** |
| **Age (years)** | **-0.1020** | 0.0419 | ±0.0839 | **-2.431** | **0.0151** | * |
| **BMI (kg/m2)** | **+0.1755** | 0.0632 | ±0.1264 | **+2.776** | **0.0055** | ** |
| Hypertension | +1.2245 | 0.9764 | ±1.9527 | +1.254 | 0.2098 |  |
| High cholesterol | -0.8363 | 0.9092 | ±1.8185 | -0.920 | 0.3577 |  |
| Kidney disease | -1.0141 | 1.6024 | ±3.2048 | -0.633 | 0.5268 |  |
| Circulatory disease | +0.5682 | 1.3725 | ±2.7451 | +0.414 | 0.6789 |  |
| Avg. daily time > 250 (%) | -0.1138 | 0.0709 | ±0.1417 | -1.605 | 0.1085 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Healthy group (no diabetes + pre-diabetes / lifestyle) - Home environment

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 124 single-predictor tests; 5 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 124 tests (samples with n >= 500), of which **1** are significant at BH q < 0.05 in the all-tests family and 1 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 1,251): best single predictor out of sample is **GMI** (CV R² 0.116 vs 0.114 for covariates alone, gain +0.002; -0.0528 per SD, p = 0.016, q = 0.137). No association survives FDR; nominal only: Mean glucose (p = 0.016), GMI (p = 0.016), Nocturnal mean (p = 0.035). Not predictable from glycaemia in this sample.
- **Indoor temperature, mean (deg C)** (n = 1,251): best single predictor out of sample is **%<54 (pooled)** (CV R² 0.290 vs 0.289 for covariates alone, gain +0.001; +0.114 per SD, p = 0.077, q = 0.385). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 1,251): best single predictor out of sample is **%<54 (daily avg)** (CV R² 0.242 vs 0.240 for covariates alone, gain +0.001; -0.324 per SD, p = 0.001, q = 0.036). FDR-robust associations (1): %<54 (daily avg) (lower outcome, -0.324 per SD, q = 0.036).
- **Indoor VOC index, mean** (n = 1,251): best single predictor out of sample is **Mean/SD** (CV R² 0.003 vs 0.002 for covariates alone, gain +0.001; +0.65 per SD, p = 0.141, q = 0.503). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.

**Most predictable outcomes (largest out-of-sample gain over covariates):** Indoor PM2.5, log(1 + mean ug/m3) (+0.002, via GMI); Indoor relative humidity, mean (%) (+0.001, via %<54 (daily avg)); Indoor temperature, mean (deg C) (+0.001, via %<54 (pooled)); Indoor VOC index, mean (+0.001, via Mean/SD). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band < 54 (1 FDR-significant / 2 raw-significant of 12); CGM level (0 FDR-significant / 3 raw-significant of 12); HbA1c (0 FDR-significant / 0 raw-significant of 4).
Level metrics: 0 FDR-significant (3 raw); variability metrics: 0 FDR-significant (0 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Indoor PM2.5, log(1 + mean ug/m3) (Mean glucose, ΔAIC -4.6); Indoor temperature, mean (%<54 (pooled), ΔAIC -4.5).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
