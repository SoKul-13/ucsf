# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Total analysis base - Home environment

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 872; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **872**, R² = **0.1432**, Adj R² = **0.1302**, F-statistic = **11.03** (p = **4.38e-22**), Residual SE = **0.824** on **858** df, AIC = **2150.9**, BIC = **2217.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9104** | 0.2079 | ±0.4159 | **+9.187** | **4.02e-20** | *** |
| Education: graduate level (vs college) | -0.0329 | 0.0587 | ±0.1175 | -0.561 | 0.5749 |  |
| **Education: high school or below (vs college)** | **+0.4985** | 0.1221 | ±0.2441 | **+4.084** | **4.42e-05** | *** |
| Site: UCSD (vs UAB) | +0.0302 | 0.0729 | ±0.1459 | +0.414 | 0.6789 |  |
| **Site: UW (vs UAB)** | **-0.2941** | 0.0778 | ±0.1556 | **-3.781** | **1.56e-04** | *** |
| Season: spring (vs autumn) | -0.0318 | 0.0797 | ±0.1594 | -0.398 | 0.6904 |  |
| Season: summer (vs autumn) | +0.0683 | 0.0801 | ±0.1603 | +0.852 | 0.3943 |  |
| Season: winter (vs autumn) | -0.0037 | 0.0750 | ±0.1500 | -0.049 | 0.9612 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.204** | **2.62e-05** | *** |
| **BMI (kg/m2)** | **+0.0219** | 0.0045 | ±0.0091 | **+4.827** | **1.38e-06** | *** |
| Hypertension | +0.0908 | 0.0608 | ±0.1216 | +1.494 | 0.1352 |  |
| High cholesterol | -0.0906 | 0.0554 | ±0.1108 | -1.636 | 0.1019 |  |
| Kidney disease | -0.0493 | 0.0935 | ±0.1870 | -0.527 | 0.5983 |  |
| **Circulatory disease** | **+0.2084** | 0.0949 | ±0.1898 | **+2.197** | **0.0280** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **872**, R² = **0.1434**, Adj R² = **0.1294**, F-statistic = **10.25** (p = **1.32e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.6**, BIC = **2224.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7167** | 0.4284 | ±0.8569 | **+4.007** | **6.15e-05** | *** |
| Education: graduate level (vs college) | -0.0331 | 0.0588 | ±0.1176 | -0.562 | 0.5739 |  |
| **Education: high school or below (vs college)** | **+0.4959** | 0.1218 | ±0.2436 | **+4.072** | **4.66e-05** | *** |
| Site: UCSD (vs UAB) | +0.0305 | 0.0731 | ±0.1462 | +0.417 | 0.6765 |  |
| **Site: UW (vs UAB)** | **-0.2937** | 0.0779 | ±0.1557 | **-3.773** | **1.61e-04** | *** |
| Season: spring (vs autumn) | -0.0277 | 0.0798 | ±0.1596 | -0.347 | 0.7284 |  |
| Season: summer (vs autumn) | +0.0673 | 0.0804 | ±0.1608 | +0.838 | 0.4023 |  |
| Season: winter (vs autumn) | -0.0012 | 0.0751 | ±0.1503 | -0.016 | 0.9872 |  |
| **Age (years)** | **-0.0110** | 0.0026 | ±0.0052 | **-4.239** | **2.25e-05** | *** |
| **BMI (kg/m2)** | **+0.0215** | 0.0046 | ±0.0091 | **+4.715** | **2.41e-06** | *** |
| Hypertension | +0.0865 | 0.0620 | ±0.1239 | +1.396 | 0.1626 |  |
| High cholesterol | -0.0950 | 0.0555 | ±0.1111 | -1.710 | 0.0872 | . |
| Kidney disease | -0.0492 | 0.0940 | ±0.1880 | -0.523 | 0.6010 |  |
| **Circulatory disease** | **+0.2062** | 0.0957 | ±0.1915 | **+2.154** | **0.0312** | * |
| HbA1c (%) | +0.0375 | 0.0694 | ±0.1389 | +0.540 | 0.5893 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **872**, R² = **0.1446**, Adj R² = **0.1306**, F-statistic = **10.35** (p = **7.71e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.5**, BIC = **2223.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2302** | 0.3293 | ±0.6586 | **+6.773** | **1.26e-11** | *** |
| Education: graduate level (vs college) | -0.0297 | 0.0590 | ±0.1179 | -0.503 | 0.6150 |  |
| **Education: high school or below (vs college)** | **+0.5012** | 0.1218 | ±0.2436 | **+4.114** | **3.89e-05** | *** |
| Site: UCSD (vs UAB) | +0.0260 | 0.0728 | ±0.1456 | +0.358 | 0.7205 |  |
| **Site: UW (vs UAB)** | **-0.2918** | 0.0778 | ±0.1556 | **-3.752** | **1.76e-04** | *** |
| Season: spring (vs autumn) | -0.0321 | 0.0799 | ±0.1599 | -0.401 | 0.6884 |  |
| Season: summer (vs autumn) | +0.0719 | 0.0805 | ±0.1610 | +0.893 | 0.3720 |  |
| Season: winter (vs autumn) | -0.0056 | 0.0749 | ±0.1498 | -0.075 | 0.9399 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.181** | **2.90e-05** | *** |
| **BMI (kg/m2)** | **+0.0225** | 0.0046 | ±0.0092 | **+4.896** | **9.79e-07** | *** |
| Hypertension | +0.0997 | 0.0618 | ±0.1236 | +1.614 | 0.1065 |  |
| High cholesterol | -0.0893 | 0.0553 | ±0.1106 | -1.615 | 0.1062 |  |
| Kidney disease | -0.0413 | 0.0931 | ±0.1862 | -0.444 | 0.6571 |  |
| **Circulatory disease** | **+0.2142** | 0.0949 | ±0.1899 | **+2.256** | **0.0241** | * |
| Mean glucose (mg/dL) | -0.0029 | 0.0024 | ±0.0048 | -1.210 | 0.2261 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **872**, R² = **0.1446**, Adj R² = **0.1306**, F-statistic = **10.35** (p = **7.71e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.5**, BIC = **2223.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.6290** | 0.6207 | ±1.2415 | **+4.235** | **2.28e-05** | *** |
| Education: graduate level (vs college) | -0.0297 | 0.0590 | ±0.1179 | -0.503 | 0.6150 |  |
| **Education: high school or below (vs college)** | **+0.5012** | 0.1218 | ±0.2436 | **+4.114** | **3.89e-05** | *** |
| Site: UCSD (vs UAB) | +0.0260 | 0.0728 | ±0.1456 | +0.358 | 0.7205 |  |
| **Site: UW (vs UAB)** | **-0.2918** | 0.0778 | ±0.1556 | **-3.752** | **1.76e-04** | *** |
| Season: spring (vs autumn) | -0.0321 | 0.0799 | ±0.1599 | -0.401 | 0.6884 |  |
| Season: summer (vs autumn) | +0.0719 | 0.0805 | ±0.1610 | +0.893 | 0.3720 |  |
| Season: winter (vs autumn) | -0.0056 | 0.0749 | ±0.1498 | -0.075 | 0.9399 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.181** | **2.90e-05** | *** |
| **BMI (kg/m2)** | **+0.0225** | 0.0046 | ±0.0092 | **+4.896** | **9.79e-07** | *** |
| Hypertension | +0.0997 | 0.0618 | ±0.1236 | +1.614 | 0.1065 |  |
| High cholesterol | -0.0893 | 0.0553 | ±0.1106 | -1.615 | 0.1062 |  |
| Kidney disease | -0.0413 | 0.0931 | ±0.1862 | -0.444 | 0.6571 |  |
| **Circulatory disease** | **+0.2142** | 0.0949 | ±0.1899 | **+2.256** | **0.0241** | * |
| GMI (%) | -0.1205 | 0.0995 | ±0.1991 | -1.210 | 0.2261 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **872**, R² = **0.1445**, Adj R² = **0.1305**, F-statistic = **10.34** (p = **8.23e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.6**, BIC = **2223.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1782** | 0.3015 | ±0.6029 | **+7.225** | **5.00e-13** | *** |
| Education: graduate level (vs college) | -0.0306 | 0.0589 | ±0.1178 | -0.520 | 0.6033 |  |
| **Education: high school or below (vs college)** | **+0.5007** | 0.1219 | ±0.2439 | **+4.106** | **4.02e-05** | *** |
| Site: UCSD (vs UAB) | +0.0295 | 0.0727 | ±0.1455 | +0.406 | 0.6847 |  |
| **Site: UW (vs UAB)** | **-0.2913** | 0.0779 | ±0.1558 | **-3.740** | **1.84e-04** | *** |
| Season: spring (vs autumn) | -0.0303 | 0.0799 | ±0.1598 | -0.379 | 0.7047 |  |
| Season: summer (vs autumn) | +0.0722 | 0.0804 | ±0.1608 | +0.898 | 0.3691 |  |
| Season: winter (vs autumn) | -0.0036 | 0.0751 | ±0.1502 | -0.048 | 0.9617 |  |
| **Age (years)** | **-0.0111** | 0.0026 | ±0.0052 | **-4.262** | **2.03e-05** | *** |
| **BMI (kg/m2)** | **+0.0229** | 0.0047 | ±0.0094 | **+4.858** | **1.19e-06** | *** |
| Hypertension | +0.0965 | 0.0612 | ±0.1224 | +1.576 | 0.1151 |  |
| High cholesterol | -0.0869 | 0.0552 | ±0.1104 | -1.574 | 0.1154 |  |
| Kidney disease | -0.0466 | 0.0930 | ±0.1860 | -0.501 | 0.6165 |  |
| **Circulatory disease** | **+0.2133** | 0.0949 | ±0.1899 | **+2.247** | **0.0246** | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0024 | 0.0022 | ±0.0043 | -1.128 | 0.2593 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **872**, R² = **0.1435**, Adj R² = **0.1295**, F-statistic = **10.26** (p = **1.29e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.6**, BIC = **2224.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8429** | 0.2409 | ±0.4818 | **+7.650** | **2.01e-14** | *** |
| Education: graduate level (vs college) | -0.0324 | 0.0589 | ±0.1177 | -0.551 | 0.5819 |  |
| **Education: high school or below (vs college)** | **+0.4944** | 0.1213 | ±0.2426 | **+4.075** | **4.61e-05** | *** |
| Site: UCSD (vs UAB) | +0.0336 | 0.0735 | ±0.1469 | +0.458 | 0.6472 |  |
| **Site: UW (vs UAB)** | **-0.2933** | 0.0779 | ±0.1558 | **-3.766** | **1.66e-04** | *** |
| Season: spring (vs autumn) | -0.0322 | 0.0798 | ±0.1595 | -0.403 | 0.6868 |  |
| Season: summer (vs autumn) | +0.0674 | 0.0803 | ±0.1607 | +0.839 | 0.4012 |  |
| Season: winter (vs autumn) | -0.0045 | 0.0751 | ±0.1501 | -0.060 | 0.9525 |  |
| **Age (years)** | **-0.0110** | 0.0026 | ±0.0052 | **-4.244** | **2.19e-05** | *** |
| **BMI (kg/m2)** | **+0.0218** | 0.0046 | ±0.0091 | **+4.779** | **1.76e-06** | *** |
| Hypertension | +0.0860 | 0.0617 | ±0.1233 | +1.395 | 0.1631 |  |
| High cholesterol | -0.0914 | 0.0554 | ±0.1108 | -1.651 | 0.0987 | . |
| Kidney disease | -0.0538 | 0.0940 | ±0.1880 | -0.573 | 0.5670 |  |
| **Circulatory disease** | **+0.2069** | 0.0951 | ±0.1902 | **+2.176** | **0.0296** | * |
| Glucose SD, pooled (mg/dL) | +0.0040 | 0.0067 | ±0.0133 | +0.602 | 0.5475 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **872**, R² = **0.1433**, Adj R² = **0.1293**, F-statistic = **10.24** (p = **1.43e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.8**, BIC = **2224.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8776** | 0.2366 | ±0.4732 | **+7.936** | **2.09e-15** | *** |
| Education: graduate level (vs college) | -0.0328 | 0.0588 | ±0.1176 | -0.558 | 0.5766 |  |
| **Education: high school or below (vs college)** | **+0.4966** | 0.1215 | ±0.2430 | **+4.088** | **4.35e-05** | *** |
| Site: UCSD (vs UAB) | +0.0319 | 0.0734 | ±0.1468 | +0.434 | 0.6641 |  |
| **Site: UW (vs UAB)** | **-0.2939** | 0.0779 | ±0.1558 | **-3.773** | **1.61e-04** | *** |
| Season: spring (vs autumn) | -0.0315 | 0.0797 | ±0.1595 | -0.395 | 0.6926 |  |
| Season: summer (vs autumn) | +0.0684 | 0.0803 | ±0.1605 | +0.852 | 0.3944 |  |
| Season: winter (vs autumn) | -0.0035 | 0.0750 | ±0.1501 | -0.046 | 0.9631 |  |
| **Age (years)** | **-0.0110** | 0.0026 | ±0.0052 | **-4.229** | **2.35e-05** | *** |
| **BMI (kg/m2)** | **+0.0218** | 0.0046 | ±0.0091 | **+4.793** | **1.64e-06** | *** |
| Hypertension | +0.0882 | 0.0618 | ±0.1237 | +1.427 | 0.1537 |  |
| High cholesterol | -0.0909 | 0.0554 | ±0.1108 | -1.640 | 0.1010 |  |
| Kidney disease | -0.0515 | 0.0939 | ±0.1878 | -0.548 | 0.5834 |  |
| **Circulatory disease** | **+0.2080** | 0.0951 | ±0.1901 | **+2.189** | **0.0286** | * |
| Avg. daily SD (mg/dL) | +0.0021 | 0.0066 | ±0.0133 | +0.324 | 0.7458 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **872**, R² = **0.1449**, Adj R² = **0.1309**, F-statistic = **10.37** (p = **6.77e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.2**, BIC = **2222.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7120** | 0.2642 | ±0.5284 | **+6.480** | **9.15e-11** | *** |
| Education: graduate level (vs college) | -0.0291 | 0.0592 | ±0.1183 | -0.492 | 0.6228 |  |
| **Education: high school or below (vs college)** | **+0.4894** | 0.1208 | ±0.2415 | **+4.052** | **5.08e-05** | *** |
| Site: UCSD (vs UAB) | +0.0369 | 0.0734 | ±0.1469 | +0.503 | 0.6151 |  |
| **Site: UW (vs UAB)** | **-0.2910** | 0.0779 | ±0.1557 | **-3.737** | **1.86e-04** | *** |
| Season: spring (vs autumn) | -0.0332 | 0.0798 | ±0.1596 | -0.416 | 0.6775 |  |
| Season: summer (vs autumn) | +0.0678 | 0.0803 | ±0.1605 | +0.845 | 0.3982 |  |
| Season: winter (vs autumn) | -0.0079 | 0.0749 | ±0.1497 | -0.106 | 0.9159 |  |
| **Age (years)** | **-0.0112** | 0.0026 | ±0.0052 | **-4.298** | **1.73e-05** | *** |
| **BMI (kg/m2)** | **+0.0219** | 0.0045 | ±0.0091 | **+4.834** | **1.34e-06** | *** |
| Hypertension | +0.0833 | 0.0610 | ±0.1219 | +1.366 | 0.1720 |  |
| High cholesterol | -0.0917 | 0.0554 | ±0.1108 | -1.655 | 0.0979 | . |
| Kidney disease | -0.0566 | 0.0939 | ±0.1877 | -0.603 | 0.5467 |  |
| **Circulatory disease** | **+0.2083** | 0.0949 | ±0.1899 | **+2.194** | **0.0282** | * |
| CV (%) | +0.0130 | 0.0096 | ±0.0192 | +1.355 | 0.1753 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **872**, R² = **0.1442**, Adj R² = **0.1302**, F-statistic = **10.32** (p = **9.25e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.9**, BIC = **2223.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0816** | 0.2528 | ±0.5056 | **+8.234** | **1.81e-16** | *** |
| Education: graduate level (vs college) | -0.0295 | 0.0593 | ±0.1185 | -0.498 | 0.6187 |  |
| **Education: high school or below (vs college)** | **+0.4919** | 0.1210 | ±0.2421 | **+4.065** | **4.81e-05** | *** |
| Site: UCSD (vs UAB) | +0.0342 | 0.0734 | ±0.1468 | +0.466 | 0.6409 |  |
| **Site: UW (vs UAB)** | **-0.2928** | 0.0779 | ±0.1558 | **-3.759** | **1.71e-04** | *** |
| Season: spring (vs autumn) | -0.0339 | 0.0798 | ±0.1595 | -0.425 | 0.6711 |  |
| Season: summer (vs autumn) | +0.0682 | 0.0803 | ±0.1605 | +0.850 | 0.3954 |  |
| Season: winter (vs autumn) | -0.0072 | 0.0750 | ±0.1500 | -0.096 | 0.9232 |  |
| **Age (years)** | **-0.0111** | 0.0026 | ±0.0052 | **-4.267** | **1.98e-05** | *** |
| **BMI (kg/m2)** | **+0.0219** | 0.0045 | ±0.0091 | **+4.826** | **1.40e-06** | *** |
| Hypertension | +0.0851 | 0.0610 | ±0.1219 | +1.395 | 0.1629 |  |
| High cholesterol | -0.0912 | 0.0554 | ±0.1108 | -1.645 | 0.1000 | . |
| Kidney disease | -0.0548 | 0.0937 | ±0.1875 | -0.584 | 0.5590 |  |
| **Circulatory disease** | **+0.2092** | 0.0949 | ±0.1898 | **+2.205** | **0.0275** | * |
| Mean / SD ratio | -0.0253 | 0.0235 | ±0.0471 | -1.073 | 0.2832 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **872**, R² = **0.1438**, Adj R² = **0.1298**, F-statistic = **10.28** (p = **1.13e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.3**, BIC = **2223.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0326** | 0.2479 | ±0.4958 | **+8.198** | **2.44e-16** | *** |
| Education: graduate level (vs college) | -0.0307 | 0.0591 | ±0.1183 | -0.518 | 0.6042 |  |
| **Education: high school or below (vs college)** | **+0.4944** | 0.1213 | ±0.2426 | **+4.075** | **4.59e-05** | *** |
| Site: UCSD (vs UAB) | +0.0327 | 0.0733 | ±0.1466 | +0.446 | 0.6555 |  |
| **Site: UW (vs UAB)** | **-0.2938** | 0.0779 | ±0.1558 | **-3.772** | **1.62e-04** | *** |
| Season: spring (vs autumn) | -0.0323 | 0.0797 | ±0.1594 | -0.406 | 0.6850 |  |
| Season: summer (vs autumn) | +0.0694 | 0.0803 | ±0.1605 | +0.865 | 0.3869 |  |
| Season: winter (vs autumn) | -0.0046 | 0.0749 | ±0.1499 | -0.061 | 0.9513 |  |
| **Age (years)** | **-0.0111** | 0.0026 | ±0.0052 | **-4.253** | **2.11e-05** | *** |
| **BMI (kg/m2)** | **+0.0218** | 0.0045 | ±0.0091 | **+4.808** | **1.53e-06** | *** |
| Hypertension | +0.0868 | 0.0610 | ±0.1220 | +1.423 | 0.1548 |  |
| High cholesterol | -0.0906 | 0.0555 | ±0.1109 | -1.634 | 0.1022 |  |
| Kidney disease | -0.0534 | 0.0939 | ±0.1878 | -0.569 | 0.5697 |  |
| **Circulatory disease** | **+0.2106** | 0.0948 | ±0.1896 | **+2.221** | **0.0263** | * |
| Avg. daily mean/SD | -0.0155 | 0.0189 | ±0.0378 | -0.818 | 0.4131 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **872**, R² = **0.1446**, Adj R² = **0.1306**, F-statistic = **10.35** (p = **7.73e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.5**, BIC = **2223.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7218** | 0.2562 | ±0.5123 | **+6.722** | **1.79e-11** | *** |
| Education: graduate level (vs college) | -0.0333 | 0.0587 | ±0.1175 | -0.567 | 0.5705 |  |
| **Education: high school or below (vs college)** | **+0.4896** | 0.1236 | ±0.2472 | **+3.961** | **7.47e-05** | *** |
| Site: UCSD (vs UAB) | +0.0330 | 0.0732 | ±0.1464 | +0.451 | 0.6522 |  |
| **Site: UW (vs UAB)** | **-0.2918** | 0.0782 | ±0.1564 | **-3.731** | **1.91e-04** | *** |
| Season: spring (vs autumn) | -0.0323 | 0.0795 | ±0.1590 | -0.406 | 0.6846 |  |
| Season: summer (vs autumn) | +0.0708 | 0.0802 | ±0.1603 | +0.883 | 0.3773 |  |
| Season: winter (vs autumn) | -0.0022 | 0.0749 | ±0.1498 | -0.029 | 0.9767 |  |
| **Age (years)** | **-0.0108** | 0.0026 | ±0.0052 | **-4.181** | **2.90e-05** | *** |
| **BMI (kg/m2)** | **+0.0219** | 0.0045 | ±0.0091 | **+4.819** | **1.45e-06** | *** |
| Hypertension | +0.0919 | 0.0610 | ±0.1221 | +1.506 | 0.1321 |  |
| High cholesterol | -0.0907 | 0.0554 | ±0.1108 | -1.637 | 0.1016 |  |
| Kidney disease | -0.0534 | 0.0934 | ±0.1867 | -0.572 | 0.5672 |  |
| **Circulatory disease** | **+0.2115** | 0.0949 | ±0.1898 | **+2.228** | **0.0259** | * |
| MAG (mg/dL/h) | +0.0050 | 0.0042 | ±0.0083 | +1.208 | 0.2272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **872**, R² = **0.1432**, Adj R² = **0.1292**, F-statistic = **10.23** (p = **1.47e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.9**, BIC = **2224.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8807** | 0.2532 | ±0.5063 | **+7.429** | **1.10e-13** | *** |
| Education: graduate level (vs college) | -0.0331 | 0.0588 | ±0.1175 | -0.563 | 0.5733 |  |
| **Education: high school or below (vs college)** | **+0.4972** | 0.1215 | ±0.2429 | **+4.094** | **4.25e-05** | *** |
| Site: UCSD (vs UAB) | +0.0311 | 0.0732 | ±0.1464 | +0.425 | 0.6707 |  |
| **Site: UW (vs UAB)** | **-0.2940** | 0.0779 | ±0.1557 | **-3.775** | **1.60e-04** | *** |
| Season: spring (vs autumn) | -0.0318 | 0.0798 | ±0.1596 | -0.399 | 0.6898 |  |
| Season: summer (vs autumn) | +0.0686 | 0.0802 | ±0.1603 | +0.856 | 0.3922 |  |
| Season: winter (vs autumn) | -0.0035 | 0.0750 | ±0.1501 | -0.046 | 0.9631 |  |
| **Age (years)** | **-0.0110** | 0.0026 | ±0.0052 | **-4.227** | **2.36e-05** | *** |
| **BMI (kg/m2)** | **+0.0219** | 0.0045 | ±0.0091 | **+4.831** | **1.36e-06** | *** |
| Hypertension | +0.0897 | 0.0614 | ±0.1227 | +1.461 | 0.1439 |  |
| High cholesterol | -0.0907 | 0.0554 | ±0.1108 | -1.636 | 0.1019 |  |
| Kidney disease | -0.0506 | 0.0937 | ±0.1874 | -0.540 | 0.5893 |  |
| **Circulatory disease** | **+0.2081** | 0.0950 | ±0.1901 | **+2.190** | **0.0285** | * |
| Avg. daily range (mg/dL) | +0.0003 | 0.0015 | ±0.0031 | +0.224 | 0.8230 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **872**, R² = **0.1446**, Adj R² = **0.1306**, F-statistic = **10.34** (p = **7.88e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.5**, BIC = **2223.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8449** | 0.2127 | ±0.4254 | **+8.675** | **4.15e-18** | *** |
| Education: graduate level (vs college) | -0.0332 | 0.0587 | ±0.1175 | -0.565 | 0.5724 |  |
| **Education: high school or below (vs college)** | **+0.4906** | 0.1213 | ±0.2427 | **+4.044** | **5.26e-05** | *** |
| Site: UCSD (vs UAB) | +0.0353 | 0.0727 | ±0.1454 | +0.485 | 0.6274 |  |
| **Site: UW (vs UAB)** | **-0.2915** | 0.0775 | ±0.1551 | **-3.759** | **1.71e-04** | *** |
| Season: spring (vs autumn) | -0.0383 | 0.0795 | ±0.1589 | -0.482 | 0.6298 |  |
| Season: summer (vs autumn) | +0.0572 | 0.0808 | ±0.1617 | +0.708 | 0.4791 |  |
| Season: winter (vs autumn) | -0.0090 | 0.0757 | ±0.1513 | -0.119 | 0.9054 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.199** | **2.69e-05** | *** |
| **BMI (kg/m2)** | **+0.0214** | 0.0046 | ±0.0092 | **+4.637** | **3.53e-06** | *** |
| Hypertension | +0.0905 | 0.0608 | ±0.1216 | +1.489 | 0.1366 |  |
| High cholesterol | -0.0963 | 0.0554 | ±0.1108 | -1.738 | 0.0822 | . |
| Kidney disease | -0.0524 | 0.0939 | ±0.1879 | -0.558 | 0.5766 |  |
| **Circulatory disease** | **+0.1996** | 0.0942 | ±0.1884 | **+2.118** | **0.0342** | * |
| SD of daily means (mg/dL) | +0.0143 | 0.0130 | ±0.0261 | +1.098 | 0.2720 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **872**, R² = **0.1440**, Adj R² = **0.1300**, F-statistic = **10.29** (p = **1.04e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.1**, BIC = **2223.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.1539 | 0.8311 | ±1.6622 | +1.388 | 0.1650 |  |
| Education: graduate level (vs college) | -0.0319 | 0.0588 | ±0.1176 | -0.542 | 0.5880 |  |
| **Education: high school or below (vs college)** | **+0.5018** | 0.1220 | ±0.2441 | **+4.112** | **3.92e-05** | *** |
| Site: UCSD (vs UAB) | +0.0255 | 0.0729 | ±0.1458 | +0.350 | 0.7267 |  |
| **Site: UW (vs UAB)** | **-0.2950** | 0.0779 | ±0.1557 | **-3.789** | **1.51e-04** | *** |
| Season: spring (vs autumn) | -0.0328 | 0.0798 | ±0.1595 | -0.412 | 0.6807 |  |
| Season: summer (vs autumn) | +0.0699 | 0.0803 | ±0.1606 | +0.870 | 0.3843 |  |
| Season: winter (vs autumn) | -0.0044 | 0.0751 | ±0.1502 | -0.058 | 0.9534 |  |
| **Age (years)** | **-0.0108** | 0.0026 | ±0.0052 | **-4.163** | **3.14e-05** | *** |
| **BMI (kg/m2)** | **+0.0221** | 0.0046 | ±0.0091 | **+4.849** | **1.24e-06** | *** |
| Hypertension | +0.0953 | 0.0612 | ±0.1224 | +1.557 | 0.1194 |  |
| High cholesterol | -0.0879 | 0.0551 | ±0.1103 | -1.595 | 0.1107 |  |
| Kidney disease | -0.0414 | 0.0934 | ±0.1868 | -0.443 | 0.6580 |  |
| **Circulatory disease** | **+0.2129** | 0.0951 | ±0.1903 | **+2.238** | **0.0253** | * |
| Time in range 70-180, pooled (%) | +0.0076 | 0.0080 | ±0.0160 | +0.947 | 0.3436 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **872**, R² = **0.1441**, Adj R² = **0.1302**, F-statistic = **10.31** (p = **9.51e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.9**, BIC = **2223.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0492 | 0.8606 | ±1.7212 | +1.219 | 0.2228 |  |
| Education: graduate level (vs college) | -0.0318 | 0.0588 | ±0.1176 | -0.542 | 0.5881 |  |
| **Education: high school or below (vs college)** | **+0.5014** | 0.1220 | ±0.2440 | **+4.110** | **3.95e-05** | *** |
| Site: UCSD (vs UAB) | +0.0248 | 0.0729 | ±0.1457 | +0.341 | 0.7334 |  |
| **Site: UW (vs UAB)** | **-0.2951** | 0.0779 | ±0.1557 | **-3.791** | **1.50e-04** | *** |
| Season: spring (vs autumn) | -0.0331 | 0.0798 | ±0.1595 | -0.416 | 0.6777 |  |
| Season: summer (vs autumn) | +0.0701 | 0.0803 | ±0.1606 | +0.873 | 0.3826 |  |
| Season: winter (vs autumn) | -0.0046 | 0.0751 | ±0.1502 | -0.062 | 0.9506 |  |
| **Age (years)** | **-0.0108** | 0.0026 | ±0.0052 | **-4.162** | **3.16e-05** | *** |
| **BMI (kg/m2)** | **+0.0221** | 0.0046 | ±0.0091 | **+4.856** | **1.20e-06** | *** |
| Hypertension | +0.0958 | 0.0612 | ±0.1225 | +1.565 | 0.1175 |  |
| High cholesterol | -0.0876 | 0.0551 | ±0.1102 | -1.589 | 0.1121 |  |
| Kidney disease | -0.0400 | 0.0933 | ±0.1866 | -0.429 | 0.6680 |  |
| **Circulatory disease** | **+0.2136** | 0.0952 | ±0.1903 | **+2.245** | **0.0248** | * |
| Avg. daily time in range 70-180 (%) | +0.0086 | 0.0083 | ±0.0166 | +1.041 | 0.2980 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **872**, R² = **0.1435**, Adj R² = **0.1295**, F-statistic = **10.25** (p = **1.30e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.6**, BIC = **2224.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9024** | 0.2087 | ±0.4175 | **+9.114** | **7.97e-20** | *** |
| Education: graduate level (vs college) | -0.0303 | 0.0595 | ±0.1189 | -0.509 | 0.6105 |  |
| **Education: high school or below (vs college)** | **+0.5010** | 0.1224 | ±0.2447 | **+4.094** | **4.23e-05** | *** |
| Site: UCSD (vs UAB) | +0.0293 | 0.0730 | ±0.1459 | +0.401 | 0.6882 |  |
| **Site: UW (vs UAB)** | **-0.2934** | 0.0778 | ±0.1555 | **-3.773** | **1.61e-04** | *** |
| Season: spring (vs autumn) | -0.0317 | 0.0798 | ±0.1595 | -0.397 | 0.6913 |  |
| Season: summer (vs autumn) | +0.0671 | 0.0801 | ±0.1602 | +0.838 | 0.4018 |  |
| Season: winter (vs autumn) | -0.0053 | 0.0750 | ±0.1500 | -0.071 | 0.9438 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.208** | **2.58e-05** | *** |
| **BMI (kg/m2)** | **+0.0220** | 0.0045 | ±0.0091 | **+4.842** | **1.28e-06** | *** |
| Hypertension | +0.0911 | 0.0608 | ±0.1216 | +1.498 | 0.1341 |  |
| High cholesterol | -0.0913 | 0.0553 | ±0.1105 | -1.651 | 0.0987 | . |
| Kidney disease | -0.0479 | 0.0935 | ±0.1871 | -0.512 | 0.6089 |  |
| **Circulatory disease** | **+0.2096** | 0.0952 | ±0.1903 | **+2.203** | **0.0276** | * |
| Time 54-69, pooled (%) | +0.0322 | 0.0610 | ±0.1221 | +0.527 | 0.5984 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **872**, R² = **0.1434**, Adj R² = **0.1294**, F-statistic = **10.24** (p = **1.37e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.7**, BIC = **2224.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9048** | 0.2086 | ±0.4173 | **+9.130** | **6.87e-20** | *** |
| Education: graduate level (vs college) | -0.0307 | 0.0595 | ±0.1191 | -0.516 | 0.6056 |  |
| **Education: high school or below (vs college)** | **+0.5006** | 0.1224 | ±0.2447 | **+4.091** | **4.29e-05** | *** |
| Site: UCSD (vs UAB) | +0.0289 | 0.0730 | ±0.1459 | +0.396 | 0.6917 |  |
| **Site: UW (vs UAB)** | **-0.2937** | 0.0778 | ±0.1556 | **-3.776** | **1.59e-04** | *** |
| Season: spring (vs autumn) | -0.0314 | 0.0797 | ±0.1595 | -0.394 | 0.6939 |  |
| Season: summer (vs autumn) | +0.0678 | 0.0802 | ±0.1603 | +0.845 | 0.3979 |  |
| Season: winter (vs autumn) | -0.0051 | 0.0750 | ±0.1500 | -0.068 | 0.9455 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.209** | **2.57e-05** | *** |
| **BMI (kg/m2)** | **+0.0219** | 0.0045 | ±0.0091 | **+4.840** | **1.30e-06** | *** |
| Hypertension | +0.0910 | 0.0608 | ±0.1216 | +1.497 | 0.1345 |  |
| High cholesterol | -0.0911 | 0.0553 | ±0.1106 | -1.647 | 0.0995 | . |
| Kidney disease | -0.0482 | 0.0935 | ±0.1870 | -0.516 | 0.6062 |  |
| **Circulatory disease** | **+0.2099** | 0.0953 | ±0.1905 | **+2.203** | **0.0276** | * |
| Avg. daily time 54-69 (%) | +0.0248 | 0.0574 | ±0.1149 | +0.432 | 0.6660 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **872**, R² = **0.1435**, Adj R² = **0.1295**, F-statistic = **10.25** (p = **1.30e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.6**, BIC = **2224.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9024** | 0.2087 | ±0.4175 | **+9.114** | **7.97e-20** | *** |
| Education: graduate level (vs college) | -0.0303 | 0.0595 | ±0.1189 | -0.509 | 0.6105 |  |
| **Education: high school or below (vs college)** | **+0.5010** | 0.1224 | ±0.2447 | **+4.094** | **4.23e-05** | *** |
| Site: UCSD (vs UAB) | +0.0293 | 0.0730 | ±0.1459 | +0.401 | 0.6882 |  |
| **Site: UW (vs UAB)** | **-0.2934** | 0.0778 | ±0.1555 | **-3.773** | **1.61e-04** | *** |
| Season: spring (vs autumn) | -0.0317 | 0.0798 | ±0.1595 | -0.397 | 0.6913 |  |
| Season: summer (vs autumn) | +0.0671 | 0.0801 | ±0.1602 | +0.838 | 0.4018 |  |
| Season: winter (vs autumn) | -0.0053 | 0.0750 | ±0.1500 | -0.071 | 0.9438 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.208** | **2.58e-05** | *** |
| **BMI (kg/m2)** | **+0.0220** | 0.0045 | ±0.0091 | **+4.842** | **1.28e-06** | *** |
| Hypertension | +0.0911 | 0.0608 | ±0.1216 | +1.498 | 0.1341 |  |
| High cholesterol | -0.0913 | 0.0553 | ±0.1105 | -1.651 | 0.0987 | . |
| Kidney disease | -0.0479 | 0.0935 | ±0.1871 | -0.512 | 0.6089 |  |
| **Circulatory disease** | **+0.2096** | 0.0952 | ±0.1903 | **+2.203** | **0.0276** | * |
| Time < 70 (%) | +0.0322 | 0.0610 | ±0.1221 | +0.527 | 0.5984 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **872**, R² = **0.1434**, Adj R² = **0.1294**, F-statistic = **10.24** (p = **1.37e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.7**, BIC = **2224.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9048** | 0.2086 | ±0.4173 | **+9.130** | **6.87e-20** | *** |
| Education: graduate level (vs college) | -0.0307 | 0.0595 | ±0.1191 | -0.516 | 0.6056 |  |
| **Education: high school or below (vs college)** | **+0.5006** | 0.1224 | ±0.2447 | **+4.091** | **4.29e-05** | *** |
| Site: UCSD (vs UAB) | +0.0289 | 0.0730 | ±0.1459 | +0.396 | 0.6917 |  |
| **Site: UW (vs UAB)** | **-0.2937** | 0.0778 | ±0.1556 | **-3.776** | **1.59e-04** | *** |
| Season: spring (vs autumn) | -0.0314 | 0.0797 | ±0.1595 | -0.394 | 0.6939 |  |
| Season: summer (vs autumn) | +0.0678 | 0.0802 | ±0.1603 | +0.845 | 0.3979 |  |
| Season: winter (vs autumn) | -0.0051 | 0.0750 | ±0.1500 | -0.068 | 0.9455 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.209** | **2.57e-05** | *** |
| **BMI (kg/m2)** | **+0.0219** | 0.0045 | ±0.0091 | **+4.840** | **1.30e-06** | *** |
| Hypertension | +0.0910 | 0.0608 | ±0.1216 | +1.497 | 0.1345 |  |
| High cholesterol | -0.0911 | 0.0553 | ±0.1106 | -1.647 | 0.0995 | . |
| Kidney disease | -0.0482 | 0.0935 | ±0.1870 | -0.516 | 0.6062 |  |
| **Circulatory disease** | **+0.2099** | 0.0953 | ±0.1905 | **+2.203** | **0.0276** | * |
| Avg. daily time < 70 (%) | +0.0248 | 0.0574 | ±0.1149 | +0.432 | 0.6660 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **872**, R² = **0.1441**, Adj R² = **0.1301**, F-statistic = **10.31** (p = **9.75e-22**), Residual SE = **0.824** on **857** df, AIC = **2152.0**, BIC = **2223.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9110** | 0.2078 | ±0.4156 | **+9.196** | **3.71e-20** | *** |
| Education: graduate level (vs college) | -0.0311 | 0.0588 | ±0.1177 | -0.529 | 0.5971 |  |
| **Education: high school or below (vs college)** | **+0.5027** | 0.1220 | ±0.2441 | **+4.119** | **3.80e-05** | *** |
| Site: UCSD (vs UAB) | +0.0249 | 0.0729 | ±0.1458 | +0.342 | 0.7325 |  |
| **Site: UW (vs UAB)** | **-0.2949** | 0.0778 | ±0.1557 | **-3.788** | **1.52e-04** | *** |
| Season: spring (vs autumn) | -0.0329 | 0.0798 | ±0.1595 | -0.412 | 0.6802 |  |
| Season: summer (vs autumn) | +0.0697 | 0.0803 | ±0.1606 | +0.868 | 0.3854 |  |
| Season: winter (vs autumn) | -0.0049 | 0.0751 | ±0.1501 | -0.065 | 0.9484 |  |
| **Age (years)** | **-0.0108** | 0.0026 | ±0.0052 | **-4.162** | **3.16e-05** | *** |
| **BMI (kg/m2)** | **+0.0221** | 0.0046 | ±0.0091 | **+4.856** | **1.20e-06** | *** |
| Hypertension | +0.0957 | 0.0612 | ±0.1223 | +1.564 | 0.1178 |  |
| High cholesterol | -0.0879 | 0.0552 | ±0.1104 | -1.593 | 0.1112 |  |
| Kidney disease | -0.0404 | 0.0933 | ±0.1867 | -0.433 | 0.6650 |  |
| **Circulatory disease** | **+0.2135** | 0.0952 | ±0.1904 | **+2.242** | **0.0249** | * |
| Time 181-250, pooled (%) | -0.0081 | 0.0079 | ±0.0158 | -1.029 | 0.3034 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **872**, R² = **0.1443**, Adj R² = **0.1303**, F-statistic = **10.32** (p = **9.01e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.8**, BIC = **2223.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9111** | 0.2077 | ±0.4155 | **+9.199** | **3.60e-20** | *** |
| Education: graduate level (vs college) | -0.0310 | 0.0589 | ±0.1177 | -0.526 | 0.5986 |  |
| **Education: high school or below (vs college)** | **+0.5023** | 0.1220 | ±0.2440 | **+4.118** | **3.82e-05** | *** |
| Site: UCSD (vs UAB) | +0.0241 | 0.0729 | ±0.1457 | +0.331 | 0.7409 |  |
| **Site: UW (vs UAB)** | **-0.2951** | 0.0778 | ±0.1557 | **-3.791** | **1.50e-04** | *** |
| Season: spring (vs autumn) | -0.0331 | 0.0798 | ±0.1595 | -0.415 | 0.6784 |  |
| Season: summer (vs autumn) | +0.0700 | 0.0803 | ±0.1606 | +0.872 | 0.3832 |  |
| Season: winter (vs autumn) | -0.0052 | 0.0751 | ±0.1501 | -0.070 | 0.9443 |  |
| **Age (years)** | **-0.0108** | 0.0026 | ±0.0052 | **-4.163** | **3.14e-05** | *** |
| **BMI (kg/m2)** | **+0.0222** | 0.0046 | ±0.0091 | **+4.862** | **1.16e-06** | *** |
| Hypertension | +0.0962 | 0.0612 | ±0.1224 | +1.571 | 0.1162 |  |
| High cholesterol | -0.0876 | 0.0552 | ±0.1103 | -1.588 | 0.1124 |  |
| Kidney disease | -0.0392 | 0.0932 | ±0.1865 | -0.420 | 0.6745 |  |
| **Circulatory disease** | **+0.2144** | 0.0953 | ±0.1905 | **+2.251** | **0.0244** | * |
| Avg. daily time 181-250 (%) | -0.0091 | 0.0082 | ±0.0164 | -1.105 | 0.2692 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **872**, R² = **0.1441**, Adj R² = **0.1301**, F-statistic = **10.31** (p = **9.75e-22**), Residual SE = **0.824** on **857** df, AIC = **2152.0**, BIC = **2223.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9110** | 0.2078 | ±0.4156 | **+9.196** | **3.71e-20** | *** |
| Education: graduate level (vs college) | -0.0311 | 0.0588 | ±0.1177 | -0.529 | 0.5971 |  |
| **Education: high school or below (vs college)** | **+0.5027** | 0.1220 | ±0.2441 | **+4.119** | **3.80e-05** | *** |
| Site: UCSD (vs UAB) | +0.0249 | 0.0729 | ±0.1458 | +0.342 | 0.7325 |  |
| **Site: UW (vs UAB)** | **-0.2949** | 0.0778 | ±0.1557 | **-3.788** | **1.52e-04** | *** |
| Season: spring (vs autumn) | -0.0329 | 0.0798 | ±0.1595 | -0.412 | 0.6802 |  |
| Season: summer (vs autumn) | +0.0697 | 0.0803 | ±0.1606 | +0.868 | 0.3854 |  |
| Season: winter (vs autumn) | -0.0049 | 0.0751 | ±0.1501 | -0.065 | 0.9484 |  |
| **Age (years)** | **-0.0108** | 0.0026 | ±0.0052 | **-4.162** | **3.16e-05** | *** |
| **BMI (kg/m2)** | **+0.0221** | 0.0046 | ±0.0091 | **+4.856** | **1.20e-06** | *** |
| Hypertension | +0.0957 | 0.0612 | ±0.1223 | +1.564 | 0.1178 |  |
| High cholesterol | -0.0879 | 0.0552 | ±0.1104 | -1.593 | 0.1112 |  |
| Kidney disease | -0.0404 | 0.0933 | ±0.1867 | -0.433 | 0.6650 |  |
| **Circulatory disease** | **+0.2135** | 0.0952 | ±0.1904 | **+2.242** | **0.0249** | * |
| Time > 180 (%) | -0.0081 | 0.0079 | ±0.0158 | -1.029 | 0.3034 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **872**, R² = **0.1443**, Adj R² = **0.1303**, F-statistic = **10.32** (p = **9.01e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.8**, BIC = **2223.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9111** | 0.2077 | ±0.4155 | **+9.199** | **3.60e-20** | *** |
| Education: graduate level (vs college) | -0.0310 | 0.0589 | ±0.1177 | -0.526 | 0.5986 |  |
| **Education: high school or below (vs college)** | **+0.5023** | 0.1220 | ±0.2440 | **+4.118** | **3.82e-05** | *** |
| Site: UCSD (vs UAB) | +0.0241 | 0.0729 | ±0.1457 | +0.331 | 0.7409 |  |
| **Site: UW (vs UAB)** | **-0.2951** | 0.0778 | ±0.1557 | **-3.791** | **1.50e-04** | *** |
| Season: spring (vs autumn) | -0.0331 | 0.0798 | ±0.1595 | -0.415 | 0.6784 |  |
| Season: summer (vs autumn) | +0.0700 | 0.0803 | ±0.1606 | +0.872 | 0.3832 |  |
| Season: winter (vs autumn) | -0.0052 | 0.0751 | ±0.1501 | -0.070 | 0.9443 |  |
| **Age (years)** | **-0.0108** | 0.0026 | ±0.0052 | **-4.163** | **3.14e-05** | *** |
| **BMI (kg/m2)** | **+0.0222** | 0.0046 | ±0.0091 | **+4.862** | **1.16e-06** | *** |
| Hypertension | +0.0962 | 0.0612 | ±0.1224 | +1.571 | 0.1162 |  |
| High cholesterol | -0.0876 | 0.0552 | ±0.1103 | -1.588 | 0.1124 |  |
| Kidney disease | -0.0392 | 0.0932 | ±0.1865 | -0.420 | 0.6745 |  |
| **Circulatory disease** | **+0.2144** | 0.0953 | ±0.1905 | **+2.251** | **0.0244** | * |
| Avg. daily time > 180 (%) | -0.0091 | 0.0082 | ±0.0164 | -1.105 | 0.2692 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **872**, R² = **0.1432**, Adj R² = **0.1292**, F-statistic = **10.23** (p = **1.48e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.9**, BIC = **2224.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9098** | 0.2085 | ±0.4169 | **+9.161** | **5.13e-20** | *** |
| Education: graduate level (vs college) | -0.0330 | 0.0588 | ±0.1176 | -0.560 | 0.5751 |  |
| **Education: high school or below (vs college)** | **+0.4995** | 0.1226 | ±0.2453 | **+4.073** | **4.65e-05** | *** |
| Site: UCSD (vs UAB) | +0.0296 | 0.0728 | ±0.1457 | +0.406 | 0.6847 |  |
| **Site: UW (vs UAB)** | **-0.2943** | 0.0779 | ±0.1558 | **-3.779** | **1.58e-04** | *** |
| Season: spring (vs autumn) | -0.0316 | 0.0798 | ±0.1597 | -0.396 | 0.6922 |  |
| Season: summer (vs autumn) | +0.0687 | 0.0803 | ±0.1605 | +0.856 | 0.3921 |  |
| Season: winter (vs autumn) | -0.0036 | 0.0751 | ±0.1502 | -0.047 | 0.9623 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.200** | **2.67e-05** | *** |
| **BMI (kg/m2)** | **+0.0220** | 0.0046 | ±0.0093 | **+4.735** | **2.19e-06** | *** |
| Hypertension | +0.0908 | 0.0608 | ±0.1217 | +1.492 | 0.1357 |  |
| High cholesterol | -0.0899 | 0.0551 | ±0.1102 | -1.631 | 0.1029 |  |
| Kidney disease | -0.0485 | 0.0938 | ±0.1875 | -0.517 | 0.6049 |  |
| **Circulatory disease** | **+0.2089** | 0.0951 | ±0.1902 | **+2.196** | **0.0281** | * |
| Nocturnal time > 180 (%) | -0.0009 | 0.0084 | ±0.0169 | -0.112 | 0.9112 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 872; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3207**, F-statistic = **32.63** (p = **3.59e-66**), Residual SE = **1.930** on **858** df, AIC = **3635.6**, BIC = **3702.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9305** | 0.5716 | ±1.1432 | **+43.615** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2096 | 0.1417 | ±0.2835 | -1.479 | 0.1392 |  |
| Education: high school or below (vs college) | +0.1090 | 0.2581 | ±0.5162 | +0.422 | 0.6727 |  |
| Site: UCSD (vs UAB) | -0.1633 | 0.1763 | ±0.3526 | -0.926 | 0.3545 |  |
| **Site: UW (vs UAB)** | **-1.1741** | 0.1784 | ±0.3569 | **-6.580** | **4.71e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7103** | 0.1908 | ±0.3815 | **-3.724** | **1.96e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5664** | 0.2175 | ±0.4351 | **+7.200** | **6.00e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7585** | 0.1996 | ±0.3992 | **-8.810** | **1.25e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0123 | +0.324 | 0.7461 |  |
| BMI (kg/m2) | +0.0074 | 0.0102 | ±0.0203 | +0.734 | 0.4631 |  |
| **Hypertension** | **+0.3204** | 0.1537 | ±0.3073 | **+2.085** | **0.0370** | * |
| High cholesterol | -0.0804 | 0.1394 | ±0.2789 | -0.577 | 0.5641 |  |
| Kidney disease | +0.1038 | 0.2248 | ±0.4496 | +0.462 | 0.6443 |  |
| Circulatory disease | +0.3715 | 0.2181 | ±0.4362 | +1.703 | 0.0886 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.27** (p = **2.03e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.7109** | 1.0404 | ±2.0809 | **+23.750** | **1.09e-124** | *** |
| Education: graduate level (vs college) | -0.2097 | 0.1419 | ±0.2839 | -1.478 | 0.1395 |  |
| Education: high school or below (vs college) | +0.1060 | 0.2590 | ±0.5180 | +0.409 | 0.6824 |  |
| Site: UCSD (vs UAB) | -0.1629 | 0.1765 | ±0.3529 | -0.923 | 0.3559 |  |
| **Site: UW (vs UAB)** | **-1.1738** | 0.1787 | ±0.3573 | **-6.570** | **5.04e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7057** | 0.1908 | ±0.3816 | **-3.698** | **2.17e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5653** | 0.2179 | ±0.4359 | **+7.183** | **6.84e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7557** | 0.2002 | ±0.4003 | **-8.772** | **1.76e-18** | *** |
| Age (years) | +0.0019 | 0.0062 | ±0.0124 | +0.309 | 0.7575 |  |
| BMI (kg/m2) | +0.0070 | 0.0103 | ±0.0207 | +0.676 | 0.4993 |  |
| **Hypertension** | **+0.3156** | 0.1542 | ±0.3084 | **+2.047** | **0.0407** | * |
| High cholesterol | -0.0854 | 0.1428 | ±0.2856 | -0.598 | 0.5497 |  |
| Kidney disease | +0.1039 | 0.2257 | ±0.4514 | +0.460 | 0.6452 |  |
| Circulatory disease | +0.3690 | 0.2192 | ±0.4383 | +1.683 | 0.0923 | . |
| HbA1c (%) | +0.0425 | 0.1741 | ±0.3482 | +0.244 | 0.8071 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3199**, F-statistic = **30.27** (p = **2.10e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9510** | 0.8402 | ±1.6804 | **+29.697** | **8.47e-194** | *** |
| Education: graduate level (vs college) | -0.2094 | 0.1423 | ±0.2846 | -1.471 | 0.1412 |  |
| Education: high school or below (vs college) | +0.1092 | 0.2584 | ±0.5168 | +0.423 | 0.6726 |  |
| Site: UCSD (vs UAB) | -0.1635 | 0.1772 | ±0.3543 | -0.923 | 0.3560 |  |
| **Site: UW (vs UAB)** | **-1.1740** | 0.1782 | ±0.3564 | **-6.588** | **4.45e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7103** | 0.1910 | ±0.3819 | **-3.720** | **1.99e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5666** | 0.2188 | ±0.4375 | **+7.161** | **7.98e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7586** | 0.1996 | ±0.3992 | **-8.811** | **1.24e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0124 | +0.324 | 0.7462 |  |
| BMI (kg/m2) | +0.0075 | 0.0102 | ±0.0205 | +0.732 | 0.4644 |  |
| **Hypertension** | **+0.3210** | 0.1530 | ±0.3059 | **+2.099** | **0.0359** | * |
| High cholesterol | -0.0803 | 0.1397 | ±0.2794 | -0.575 | 0.5652 |  |
| Kidney disease | +0.1043 | 0.2239 | ±0.4477 | +0.466 | 0.6413 |  |
| Circulatory disease | +0.3718 | 0.2193 | ±0.4387 | +1.695 | 0.0900 | . |
| Mean glucose (mg/dL) | -0.0002 | 0.0056 | ±0.0113 | -0.033 | 0.9738 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3199**, F-statistic = **30.27** (p = **2.10e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9766** | 1.5074 | ±3.0149 | **+16.569** | **1.17e-61** | *** |
| Education: graduate level (vs college) | -0.2094 | 0.1423 | ±0.2846 | -1.471 | 0.1412 |  |
| Education: high school or below (vs college) | +0.1092 | 0.2584 | ±0.5168 | +0.423 | 0.6726 |  |
| Site: UCSD (vs UAB) | -0.1635 | 0.1772 | ±0.3543 | -0.923 | 0.3560 |  |
| **Site: UW (vs UAB)** | **-1.1740** | 0.1782 | ±0.3564 | **-6.588** | **4.45e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7103** | 0.1910 | ±0.3819 | **-3.720** | **1.99e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5666** | 0.2188 | ±0.4375 | **+7.161** | **7.98e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7586** | 0.1996 | ±0.3992 | **-8.811** | **1.24e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0124 | +0.324 | 0.7462 |  |
| BMI (kg/m2) | +0.0075 | 0.0102 | ±0.0205 | +0.732 | 0.4644 |  |
| **Hypertension** | **+0.3210** | 0.1530 | ±0.3059 | **+2.099** | **0.0359** | * |
| High cholesterol | -0.0803 | 0.1397 | ±0.2794 | -0.575 | 0.5652 |  |
| Kidney disease | +0.1043 | 0.2239 | ±0.4477 | +0.466 | 0.6413 |  |
| Circulatory disease | +0.3718 | 0.2193 | ±0.4387 | +1.695 | 0.0900 | . |
| GMI (%) | -0.0077 | 0.2355 | ±0.4709 | -0.033 | 0.9738 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **872**, R² = **0.3311**, Adj R² = **0.3202**, F-statistic = **30.30** (p = **1.82e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.3**, BIC = **3708.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.2265** | 0.7814 | ±1.5629 | **+32.282** | **1.26e-228** | *** |
| Education: graduate level (vs college) | -0.2070 | 0.1419 | ±0.2838 | -1.459 | 0.1447 |  |
| Education: high school or below (vs college) | +0.1114 | 0.2589 | ±0.5178 | +0.430 | 0.6668 |  |
| Site: UCSD (vs UAB) | -0.1640 | 0.1767 | ±0.3534 | -0.928 | 0.3534 |  |
| **Site: UW (vs UAB)** | **-1.1711** | 0.1781 | ±0.3562 | **-6.576** | **4.85e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7087** | 0.1912 | ±0.3823 | **-3.707** | **2.09e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5707** | 0.2189 | ±0.4378 | **+7.175** | **7.23e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7584** | 0.1998 | ±0.3996 | **-8.801** | **1.36e-18** | *** |
| Age (years) | +0.0018 | 0.0062 | ±0.0123 | +0.290 | 0.7716 |  |
| BMI (kg/m2) | +0.0086 | 0.0104 | ±0.0209 | +0.823 | 0.4104 |  |
| **Hypertension** | **+0.3267** | 0.1532 | ±0.3063 | **+2.133** | **0.0329** | * |
| High cholesterol | -0.0764 | 0.1398 | ±0.2796 | -0.546 | 0.5848 |  |
| Kidney disease | +0.1068 | 0.2241 | ±0.4483 | +0.476 | 0.6338 |  |
| Circulatory disease | +0.3769 | 0.2190 | ±0.4379 | +1.721 | 0.0852 | . |
| Nocturnal mean 00-06h (mg/dL) | -0.0027 | 0.0050 | ±0.0099 | -0.545 | 0.5856 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **872**, R² = **0.3310**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **1.96e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.5**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0336** | 0.6514 | ±1.3027 | **+38.433** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2104 | 0.1420 | ±0.2841 | -1.481 | 0.1385 |  |
| Education: high school or below (vs college) | +0.1154 | 0.2568 | ±0.5136 | +0.450 | 0.6531 |  |
| Site: UCSD (vs UAB) | -0.1685 | 0.1767 | ±0.3535 | -0.953 | 0.3404 |  |
| **Site: UW (vs UAB)** | **-1.1753** | 0.1786 | ±0.3573 | **-6.579** | **4.73e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7097** | 0.1911 | ±0.3821 | **-3.715** | **2.04e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5676** | 0.2182 | ±0.4363 | **+7.186** | **6.68e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7572** | 0.1998 | ±0.3995 | **-8.797** | **1.41e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0123 | +0.348 | 0.7276 |  |
| BMI (kg/m2) | +0.0077 | 0.0101 | ±0.0203 | +0.754 | 0.4507 |  |
| **Hypertension** | **+0.3278** | 0.1545 | ±0.3089 | **+2.122** | **0.0338** | * |
| High cholesterol | -0.0791 | 0.1400 | ±0.2800 | -0.565 | 0.5722 |  |
| Kidney disease | +0.1108 | 0.2243 | ±0.4485 | +0.494 | 0.6214 |  |
| Circulatory disease | +0.3738 | 0.2185 | ±0.4370 | +1.711 | 0.0872 | . |
| Glucose SD, pooled (mg/dL) | -0.0061 | 0.0162 | ±0.0324 | -0.379 | 0.7050 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.27** (p = **2.05e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9861** | 0.6443 | ±1.2886 | **+38.779** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2098 | 0.1420 | ±0.2840 | -1.477 | 0.1396 |  |
| Education: high school or below (vs college) | +0.1123 | 0.2566 | ±0.5133 | +0.438 | 0.6617 |  |
| Site: UCSD (vs UAB) | -0.1661 | 0.1766 | ±0.3532 | -0.941 | 0.3469 |  |
| **Site: UW (vs UAB)** | **-1.1745** | 0.1786 | ±0.3572 | **-6.576** | **4.83e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7107** | 0.1910 | ±0.3821 | **-3.721** | **1.99e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5662** | 0.2178 | ±0.4356 | **+7.190** | **6.46e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7588** | 0.1998 | ±0.3997 | **-8.801** | **1.35e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0123 | +0.338 | 0.7350 |  |
| BMI (kg/m2) | +0.0076 | 0.0101 | ±0.0203 | +0.748 | 0.4546 |  |
| **Hypertension** | **+0.3249** | 0.1546 | ±0.3093 | **+2.101** | **0.0357** | * |
| High cholesterol | -0.0799 | 0.1398 | ±0.2796 | -0.572 | 0.5676 |  |
| Kidney disease | +0.1076 | 0.2243 | ±0.4487 | +0.480 | 0.6315 |  |
| Circulatory disease | +0.3721 | 0.2184 | ±0.4368 | +1.704 | 0.0884 | . |
| Avg. daily SD (mg/dL) | -0.0036 | 0.0163 | ±0.0326 | -0.223 | 0.8234 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **872**, R² = **0.3310**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **1.96e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.5**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0603** | 0.6972 | ±1.3944 | **+35.943** | **6.50e-283** | *** |
| Education: graduate level (vs college) | -0.2121 | 0.1426 | ±0.2851 | -1.488 | 0.1368 |  |
| Education: high school or below (vs college) | +0.1150 | 0.2565 | ±0.5129 | +0.449 | 0.6538 |  |
| Site: UCSD (vs UAB) | -0.1677 | 0.1762 | ±0.3524 | -0.952 | 0.3413 |  |
| **Site: UW (vs UAB)** | **-1.1761** | 0.1784 | ±0.3568 | **-6.593** | **4.32e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7094** | 0.1910 | ±0.3820 | **-3.714** | **2.04e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5667** | 0.2178 | ±0.4356 | **+7.193** | **6.33e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7557** | 0.1996 | ±0.3993 | **-8.795** | **1.44e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0123 | +0.349 | 0.7267 |  |
| BMI (kg/m2) | +0.0074 | 0.0102 | ±0.0204 | +0.729 | 0.4659 |  |
| **Hypertension** | **+0.3254** | 0.1546 | ±0.3092 | **+2.105** | **0.0353** | * |
| High cholesterol | -0.0797 | 0.1398 | ±0.2797 | -0.570 | 0.5688 |  |
| Kidney disease | +0.1086 | 0.2252 | ±0.4503 | +0.482 | 0.6296 |  |
| Circulatory disease | +0.3716 | 0.2183 | ±0.4366 | +1.702 | 0.0887 | . |
| CV (%) | -0.0085 | 0.0230 | ±0.0459 | -0.371 | 0.7107 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **1.98e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.5**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.7955** | 0.6658 | ±1.3316 | **+37.240** | **1.51e-303** | *** |
| Education: graduate level (vs college) | -0.2123 | 0.1429 | ±0.2858 | -1.486 | 0.1374 |  |
| Education: high school or below (vs college) | +0.1143 | 0.2565 | ±0.5130 | +0.445 | 0.6560 |  |
| Site: UCSD (vs UAB) | -0.1665 | 0.1763 | ±0.3525 | -0.944 | 0.3450 |  |
| **Site: UW (vs UAB)** | **-1.1751** | 0.1784 | ±0.3569 | **-6.585** | **4.55e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7087** | 0.1911 | ±0.3821 | **-3.709** | **2.08e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5664** | 0.2178 | ±0.4357 | **+7.191** | **6.45e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7557** | 0.1996 | ±0.3993 | **-8.794** | **1.44e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0123 | +0.346 | 0.7295 |  |
| BMI (kg/m2) | +0.0074 | 0.0102 | ±0.0203 | +0.732 | 0.4640 |  |
| **Hypertension** | **+0.3250** | 0.1543 | ±0.3086 | **+2.106** | **0.0352** | * |
| High cholesterol | -0.0800 | 0.1398 | ±0.2796 | -0.572 | 0.5674 |  |
| Kidney disease | +0.1081 | 0.2252 | ±0.4505 | +0.480 | 0.6311 |  |
| Circulatory disease | +0.3709 | 0.2183 | ±0.4367 | +1.699 | 0.0894 | . |
| Mean / SD ratio | +0.0199 | 0.0585 | ±0.1171 | +0.340 | 0.7337 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3199**, F-statistic = **30.27** (p = **2.10e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9151** | 0.6488 | ±1.2975 | **+38.404** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2099 | 0.1431 | ±0.2862 | -1.467 | 0.1425 |  |
| Education: high school or below (vs college) | +0.1096 | 0.2567 | ±0.5135 | +0.427 | 0.6696 |  |
| Site: UCSD (vs UAB) | -0.1636 | 0.1763 | ±0.3527 | -0.928 | 0.3536 |  |
| **Site: UW (vs UAB)** | **-1.1742** | 0.1786 | ±0.3572 | **-6.575** | **4.88e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7103** | 0.1911 | ±0.3821 | **-3.717** | **2.01e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5662** | 0.2179 | ±0.4359 | **+7.186** | **6.65e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7584** | 0.1998 | ±0.3995 | **-8.802** | **1.35e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0123 | +0.327 | 0.7435 |  |
| BMI (kg/m2) | +0.0075 | 0.0101 | ±0.0203 | +0.735 | 0.4623 |  |
| **Hypertension** | **+0.3210** | 0.1542 | ±0.3084 | **+2.081** | **0.0374** | * |
| High cholesterol | -0.0804 | 0.1397 | ±0.2793 | -0.576 | 0.5648 |  |
| Kidney disease | +0.1043 | 0.2252 | ±0.4504 | +0.463 | 0.6432 |  |
| Circulatory disease | +0.3712 | 0.2187 | ±0.4373 | +1.698 | 0.0896 | . |
| Avg. daily mean/SD | +0.0019 | 0.0478 | ±0.0956 | +0.041 | 0.9675 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **872**, R² = **0.3310**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **1.96e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.5**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.7935** | 0.7076 | ±1.4152 | **+35.040** | **5.53e-269** | *** |
| Education: graduate level (vs college) | -0.2099 | 0.1419 | ±0.2838 | -1.479 | 0.1392 |  |
| Education: high school or below (vs college) | +0.1025 | 0.2600 | ±0.5200 | +0.394 | 0.6934 |  |
| Site: UCSD (vs UAB) | -0.1612 | 0.1770 | ±0.3540 | -0.911 | 0.3623 |  |
| **Site: UW (vs UAB)** | **-1.1725** | 0.1790 | ±0.3579 | **-6.551** | **5.72e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7107** | 0.1911 | ±0.3821 | **-3.720** | **1.99e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5682** | 0.2181 | ±0.4362 | **+7.191** | **6.45e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7574** | 0.2001 | ±0.4003 | **-8.781** | **1.62e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0124 | +0.333 | 0.7392 |  |
| BMI (kg/m2) | +0.0075 | 0.0102 | ±0.0203 | +0.734 | 0.4629 |  |
| **Hypertension** | **+0.3212** | 0.1541 | ±0.3081 | **+2.085** | **0.0371** | * |
| High cholesterol | -0.0805 | 0.1396 | ±0.2792 | -0.577 | 0.5642 |  |
| Kidney disease | +0.1008 | 0.2253 | ±0.4505 | +0.447 | 0.6546 |  |
| Circulatory disease | +0.3737 | 0.2184 | ±0.4368 | +1.711 | 0.0871 | . |
| MAG (mg/dL/h) | +0.0037 | 0.0105 | ±0.0211 | +0.347 | 0.7285 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.27** (p = **2.05e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0051** | 0.6799 | ±1.3598 | **+36.778** | **4.22e-296** | *** |
| Education: graduate level (vs college) | -0.2092 | 0.1419 | ±0.2838 | -1.475 | 0.1403 |  |
| Education: high school or below (vs college) | +0.1125 | 0.2570 | ±0.5139 | +0.438 | 0.6616 |  |
| Site: UCSD (vs UAB) | -0.1656 | 0.1763 | ±0.3527 | -0.939 | 0.3477 |  |
| **Site: UW (vs UAB)** | **-1.1744** | 0.1786 | ±0.3572 | **-6.575** | **4.87e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7101** | 0.1911 | ±0.3821 | **-3.717** | **2.02e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5655** | 0.2176 | ±0.4352 | **+7.194** | **6.28e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7589** | 0.1999 | ±0.3998 | **-8.799** | **1.37e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0123 | +0.336 | 0.7368 |  |
| BMI (kg/m2) | +0.0074 | 0.0102 | ±0.0204 | +0.725 | 0.4687 |  |
| **Hypertension** | **+0.3234** | 0.1544 | ±0.3088 | **+2.095** | **0.0362** | * |
| High cholesterol | -0.0802 | 0.1397 | ±0.2794 | -0.574 | 0.5659 |  |
| Kidney disease | +0.1071 | 0.2248 | ±0.4496 | +0.476 | 0.6338 |  |
| Circulatory disease | +0.3723 | 0.2185 | ±0.4370 | +1.704 | 0.0884 | . |
| Avg. daily range (mg/dL) | -0.0009 | 0.0038 | ±0.0077 | -0.225 | 0.8221 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **872**, R² = **0.3315**, Adj R² = **0.3205**, F-statistic = **30.35** (p = **1.43e-65**), Residual SE = **1.931** on **857** df, AIC = **3636.8**, BIC = **3708.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0460** | 0.5984 | ±1.1968 | **+41.856** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2092 | 0.1421 | ±0.2841 | -1.473 | 0.1409 |  |
| Education: high school or below (vs college) | +0.1230 | 0.2583 | ±0.5166 | +0.476 | 0.6340 |  |
| Site: UCSD (vs UAB) | -0.1722 | 0.1764 | ±0.3528 | -0.976 | 0.3289 |  |
| **Site: UW (vs UAB)** | **-1.1787** | 0.1789 | ±0.3579 | **-6.587** | **4.48e-11** | *** |
| **Season: spring (vs autumn)** | **-0.6988** | 0.1900 | ±0.3801 | **-3.677** | **2.36e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5859** | 0.2193 | ±0.4385 | **+7.233** | **4.73e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7491** | 0.1993 | ±0.3987 | **-8.775** | **1.72e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0123 | +0.316 | 0.7519 |  |
| BMI (kg/m2) | +0.0083 | 0.0102 | ±0.0203 | +0.817 | 0.4138 |  |
| **Hypertension** | **+0.3209** | 0.1540 | ±0.3079 | **+2.084** | **0.0371** | * |
| High cholesterol | -0.0704 | 0.1409 | ±0.2818 | -0.499 | 0.6174 |  |
| Kidney disease | +0.1094 | 0.2243 | ±0.4486 | +0.488 | 0.6257 |  |
| Circulatory disease | +0.3871 | 0.2191 | ±0.4382 | +1.767 | 0.0772 | . |
| SD of daily means (mg/dL) | -0.0253 | 0.0303 | ±0.0607 | -0.834 | 0.4041 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.27** (p = **2.03e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.4192** | 1.8624 | ±3.7248 | **+13.112** | **2.82e-39** | *** |
| Education: graduate level (vs college) | -0.2089 | 0.1420 | ±0.2840 | -1.471 | 0.1414 |  |
| Education: high school or below (vs college) | +0.1113 | 0.2583 | ±0.5166 | +0.431 | 0.6667 |  |
| Site: UCSD (vs UAB) | -0.1664 | 0.1767 | ±0.3534 | -0.942 | 0.3463 |  |
| **Site: UW (vs UAB)** | **-1.1747** | 0.1787 | ±0.3575 | **-6.573** | **4.95e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7111** | 0.1910 | ±0.3821 | **-3.722** | **1.98e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5674** | 0.2179 | ±0.4358 | **+7.193** | **6.32e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7590** | 0.1998 | ±0.3996 | **-8.803** | **1.34e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0124 | +0.335 | 0.7377 |  |
| BMI (kg/m2) | +0.0076 | 0.0102 | ±0.0203 | +0.748 | 0.4546 |  |
| **Hypertension** | **+0.3235** | 0.1536 | ±0.3071 | **+2.106** | **0.0352** | * |
| High cholesterol | -0.0786 | 0.1399 | ±0.2798 | -0.562 | 0.5742 |  |
| Kidney disease | +0.1091 | 0.2231 | ±0.4462 | +0.489 | 0.6247 |  |
| Circulatory disease | +0.3745 | 0.2192 | ±0.4384 | +1.708 | 0.0876 | . |
| Time in range 70-180, pooled (%) | +0.0051 | 0.0180 | ±0.0360 | +0.285 | 0.7757 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **872**, R² = **0.3310**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **1.97e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.5**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1909** | 1.9322 | ±3.8645 | **+12.520** | **5.83e-36** | *** |
| Education: graduate level (vs college) | -0.2086 | 0.1420 | ±0.2840 | -1.469 | 0.1418 |  |
| Education: high school or below (vs college) | +0.1115 | 0.2581 | ±0.5163 | +0.432 | 0.6658 |  |
| Site: UCSD (vs UAB) | -0.1679 | 0.1767 | ±0.3533 | -0.950 | 0.3420 |  |
| **Site: UW (vs UAB)** | **-1.1750** | 0.1787 | ±0.3574 | **-6.575** | **4.87e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7115** | 0.1911 | ±0.3822 | **-3.723** | **1.97e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5679** | 0.2179 | ±0.4358 | **+7.195** | **6.24e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7593** | 0.1999 | ±0.3997 | **-8.802** | **1.34e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0124 | +0.338 | 0.7352 |  |
| BMI (kg/m2) | +0.0077 | 0.0102 | ±0.0203 | +0.755 | 0.4503 |  |
| **Hypertension** | **+0.3248** | 0.1538 | ±0.3075 | **+2.112** | **0.0347** | * |
| High cholesterol | -0.0778 | 0.1399 | ±0.2798 | -0.556 | 0.5780 |  |
| Kidney disease | +0.1117 | 0.2227 | ±0.4455 | +0.502 | 0.6159 |  |
| Circulatory disease | +0.3759 | 0.2193 | ±0.4387 | +1.714 | 0.0865 | . |
| Avg. daily time in range 70-180 (%) | +0.0074 | 0.0188 | ±0.0376 | +0.394 | 0.6933 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **872**, R² = **0.3311**, Adj R² = **0.3201**, F-statistic = **30.30** (p = **1.83e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.3**, BIC = **3708.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9487** | 0.5735 | ±1.1469 | **+43.506** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2156 | 0.1419 | ±0.2837 | -1.520 | 0.1285 |  |
| Education: high school or below (vs college) | +0.1036 | 0.2577 | ±0.5153 | +0.402 | 0.6878 |  |
| Site: UCSD (vs UAB) | -0.1612 | 0.1771 | ±0.3542 | -0.910 | 0.3628 |  |
| **Site: UW (vs UAB)** | **-1.1757** | 0.1783 | ±0.3567 | **-6.592** | **4.34e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7105** | 0.1907 | ±0.3813 | **-3.726** | **1.94e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5690** | 0.2173 | ±0.4345 | **+7.221** | **5.14e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7547** | 0.1997 | ±0.3993 | **-8.789** | **1.51e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0123 | +0.330 | 0.7418 |  |
| BMI (kg/m2) | +0.0073 | 0.0102 | ±0.0203 | +0.717 | 0.4732 |  |
| **Hypertension** | **+0.3198** | 0.1537 | ±0.3074 | **+2.081** | **0.0375** | * |
| High cholesterol | -0.0788 | 0.1393 | ±0.2786 | -0.566 | 0.5714 |  |
| Kidney disease | +0.1006 | 0.2248 | ±0.4495 | +0.448 | 0.6545 |  |
| Circulatory disease | +0.3688 | 0.2179 | ±0.4358 | +1.692 | 0.0906 | . |
| Time 54-69, pooled (%) | -0.0732 | 0.1516 | ±0.3032 | -0.483 | 0.6290 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **2.02e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.6**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9389** | 0.5733 | ±1.1466 | **+43.500** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2129 | 0.1420 | ±0.2839 | -1.500 | 0.1337 |  |
| Education: high school or below (vs college) | +0.1059 | 0.2579 | ±0.5159 | +0.411 | 0.6813 |  |
| Site: UCSD (vs UAB) | -0.1614 | 0.1776 | ±0.3551 | -0.909 | 0.3635 |  |
| **Site: UW (vs UAB)** | **-1.1747** | 0.1784 | ±0.3569 | **-6.583** | **4.61e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7109** | 0.1909 | ±0.3817 | **-3.724** | **1.96e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5671** | 0.2174 | ±0.4349 | **+7.207** | **5.72e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7563** | 0.1997 | ±0.3994 | **-8.795** | **1.43e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0123 | +0.328 | 0.7425 |  |
| BMI (kg/m2) | +0.0074 | 0.0102 | ±0.0203 | +0.725 | 0.4686 |  |
| **Hypertension** | **+0.3201** | 0.1537 | ±0.3075 | **+2.082** | **0.0373** | * |
| High cholesterol | -0.0797 | 0.1393 | ±0.2786 | -0.572 | 0.5673 |  |
| Kidney disease | +0.1022 | 0.2247 | ±0.4495 | +0.455 | 0.6492 |  |
| Circulatory disease | +0.3693 | 0.2180 | ±0.4361 | +1.694 | 0.0903 | . |
| Avg. daily time 54-69 (%) | -0.0372 | 0.1386 | ±0.2772 | -0.269 | 0.7881 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **872**, R² = **0.3311**, Adj R² = **0.3201**, F-statistic = **30.30** (p = **1.83e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.3**, BIC = **3708.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9487** | 0.5735 | ±1.1469 | **+43.506** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2156 | 0.1419 | ±0.2837 | -1.520 | 0.1285 |  |
| Education: high school or below (vs college) | +0.1036 | 0.2577 | ±0.5153 | +0.402 | 0.6878 |  |
| Site: UCSD (vs UAB) | -0.1612 | 0.1771 | ±0.3542 | -0.910 | 0.3628 |  |
| **Site: UW (vs UAB)** | **-1.1757** | 0.1783 | ±0.3567 | **-6.592** | **4.34e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7105** | 0.1907 | ±0.3813 | **-3.726** | **1.94e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5690** | 0.2173 | ±0.4345 | **+7.221** | **5.14e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7547** | 0.1997 | ±0.3993 | **-8.789** | **1.51e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0123 | +0.330 | 0.7418 |  |
| BMI (kg/m2) | +0.0073 | 0.0102 | ±0.0203 | +0.717 | 0.4732 |  |
| **Hypertension** | **+0.3198** | 0.1537 | ±0.3074 | **+2.081** | **0.0375** | * |
| High cholesterol | -0.0788 | 0.1393 | ±0.2786 | -0.566 | 0.5714 |  |
| Kidney disease | +0.1006 | 0.2248 | ±0.4495 | +0.448 | 0.6545 |  |
| Circulatory disease | +0.3688 | 0.2179 | ±0.4358 | +1.692 | 0.0906 | . |
| Time < 70 (%) | -0.0732 | 0.1516 | ±0.3032 | -0.483 | 0.6290 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **2.02e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.6**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9389** | 0.5733 | ±1.1466 | **+43.500** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2129 | 0.1420 | ±0.2839 | -1.500 | 0.1337 |  |
| Education: high school or below (vs college) | +0.1059 | 0.2579 | ±0.5159 | +0.411 | 0.6813 |  |
| Site: UCSD (vs UAB) | -0.1614 | 0.1776 | ±0.3551 | -0.909 | 0.3635 |  |
| **Site: UW (vs UAB)** | **-1.1747** | 0.1784 | ±0.3569 | **-6.583** | **4.61e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7109** | 0.1909 | ±0.3817 | **-3.724** | **1.96e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5671** | 0.2174 | ±0.4349 | **+7.207** | **5.72e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7563** | 0.1997 | ±0.3994 | **-8.795** | **1.43e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0123 | +0.328 | 0.7425 |  |
| BMI (kg/m2) | +0.0074 | 0.0102 | ±0.0203 | +0.725 | 0.4686 |  |
| **Hypertension** | **+0.3201** | 0.1537 | ±0.3075 | **+2.082** | **0.0373** | * |
| High cholesterol | -0.0797 | 0.1393 | ±0.2786 | -0.572 | 0.5673 |  |
| Kidney disease | +0.1022 | 0.2247 | ±0.4495 | +0.455 | 0.6492 |  |
| Circulatory disease | +0.3693 | 0.2180 | ±0.4361 | +1.694 | 0.0903 | . |
| Avg. daily time < 70 (%) | -0.0372 | 0.1386 | ±0.2772 | -0.269 | 0.7881 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3199**, F-statistic = **30.27** (p = **2.07e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9308** | 0.5724 | ±1.1448 | **+43.553** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2088 | 0.1421 | ±0.2842 | -1.470 | 0.1417 |  |
| Education: high school or below (vs college) | +0.1108 | 0.2583 | ±0.5167 | +0.429 | 0.6679 |  |
| Site: UCSD (vs UAB) | -0.1655 | 0.1770 | ±0.3539 | -0.935 | 0.3496 |  |
| **Site: UW (vs UAB)** | **-1.1745** | 0.1788 | ±0.3575 | **-6.570** | **5.02e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7108** | 0.1910 | ±0.3821 | **-3.721** | **1.99e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5670** | 0.2179 | ±0.4358 | **+7.191** | **6.44e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7590** | 0.1999 | ±0.3997 | **-8.802** | **1.35e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0124 | +0.331 | 0.7408 |  |
| BMI (kg/m2) | +0.0076 | 0.0102 | ±0.0203 | +0.744 | 0.4568 |  |
| **Hypertension** | **+0.3225** | 0.1535 | ±0.3070 | **+2.101** | **0.0356** | * |
| High cholesterol | -0.0793 | 0.1400 | ±0.2800 | -0.566 | 0.5713 |  |
| Kidney disease | +0.1076 | 0.2232 | ±0.4465 | +0.482 | 0.6297 |  |
| Circulatory disease | +0.3737 | 0.2193 | ±0.4385 | +1.704 | 0.0884 | . |
| Time 181-250, pooled (%) | -0.0035 | 0.0180 | ±0.0360 | -0.196 | 0.8446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **2.00e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.5**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9310** | 0.5728 | ±1.1456 | **+43.527** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2082 | 0.1421 | ±0.2842 | -1.465 | 0.1428 |  |
| Education: high school or below (vs college) | +0.1117 | 0.2582 | ±0.5163 | +0.433 | 0.6652 |  |
| Site: UCSD (vs UAB) | -0.1676 | 0.1770 | ±0.3540 | -0.947 | 0.3437 |  |
| **Site: UW (vs UAB)** | **-1.1748** | 0.1787 | ±0.3575 | **-6.573** | **4.94e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7113** | 0.1911 | ±0.3822 | **-3.722** | **1.98e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5676** | 0.2180 | ±0.4359 | **+7.192** | **6.38e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7596** | 0.1999 | ±0.3998 | **-8.802** | **1.35e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0124 | +0.335 | 0.7374 |  |
| BMI (kg/m2) | +0.0077 | 0.0102 | ±0.0203 | +0.754 | 0.4511 |  |
| **Hypertension** | **+0.3242** | 0.1537 | ±0.3074 | **+2.109** | **0.0349** | * |
| High cholesterol | -0.0783 | 0.1400 | ±0.2800 | -0.559 | 0.5760 |  |
| Kidney disease | +0.1110 | 0.2227 | ±0.4455 | +0.498 | 0.6184 |  |
| Circulatory disease | +0.3757 | 0.2194 | ±0.4389 | +1.712 | 0.0869 | . |
| Avg. daily time 181-250 (%) | -0.0064 | 0.0188 | ±0.0376 | -0.342 | 0.7324 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3199**, F-statistic = **30.27** (p = **2.07e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9308** | 0.5724 | ±1.1448 | **+43.553** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2088 | 0.1421 | ±0.2842 | -1.470 | 0.1417 |  |
| Education: high school or below (vs college) | +0.1108 | 0.2583 | ±0.5167 | +0.429 | 0.6679 |  |
| Site: UCSD (vs UAB) | -0.1655 | 0.1770 | ±0.3539 | -0.935 | 0.3496 |  |
| **Site: UW (vs UAB)** | **-1.1745** | 0.1788 | ±0.3575 | **-6.570** | **5.02e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7108** | 0.1910 | ±0.3821 | **-3.721** | **1.99e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5670** | 0.2179 | ±0.4358 | **+7.191** | **6.44e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7590** | 0.1999 | ±0.3997 | **-8.802** | **1.35e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0124 | +0.331 | 0.7408 |  |
| BMI (kg/m2) | +0.0076 | 0.0102 | ±0.0203 | +0.744 | 0.4568 |  |
| **Hypertension** | **+0.3225** | 0.1535 | ±0.3070 | **+2.101** | **0.0356** | * |
| High cholesterol | -0.0793 | 0.1400 | ±0.2800 | -0.566 | 0.5713 |  |
| Kidney disease | +0.1076 | 0.2232 | ±0.4465 | +0.482 | 0.6297 |  |
| Circulatory disease | +0.3737 | 0.2193 | ±0.4385 | +1.704 | 0.0884 | . |
| Time > 180 (%) | -0.0035 | 0.0180 | ±0.0360 | -0.196 | 0.8446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **2.00e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.5**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9310** | 0.5728 | ±1.1456 | **+43.527** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2082 | 0.1421 | ±0.2842 | -1.465 | 0.1428 |  |
| Education: high school or below (vs college) | +0.1117 | 0.2582 | ±0.5163 | +0.433 | 0.6652 |  |
| Site: UCSD (vs UAB) | -0.1676 | 0.1770 | ±0.3540 | -0.947 | 0.3437 |  |
| **Site: UW (vs UAB)** | **-1.1748** | 0.1787 | ±0.3575 | **-6.573** | **4.94e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7113** | 0.1911 | ±0.3822 | **-3.722** | **1.98e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5676** | 0.2180 | ±0.4359 | **+7.192** | **6.38e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7596** | 0.1999 | ±0.3998 | **-8.802** | **1.35e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0124 | +0.335 | 0.7374 |  |
| BMI (kg/m2) | +0.0077 | 0.0102 | ±0.0203 | +0.754 | 0.4511 |  |
| **Hypertension** | **+0.3242** | 0.1537 | ±0.3074 | **+2.109** | **0.0349** | * |
| High cholesterol | -0.0783 | 0.1400 | ±0.2800 | -0.559 | 0.5760 |  |
| Kidney disease | +0.1110 | 0.2227 | ±0.4455 | +0.498 | 0.6184 |  |
| Circulatory disease | +0.3757 | 0.2194 | ±0.4389 | +1.712 | 0.0869 | . |
| Avg. daily time > 180 (%) | -0.0064 | 0.0188 | ±0.0376 | -0.342 | 0.7324 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3199**, F-statistic = **30.27** (p = **2.10e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9305** | 0.5717 | ±1.1435 | **+43.604** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2096 | 0.1418 | ±0.2837 | -1.478 | 0.1395 |  |
| Education: high school or below (vs college) | +0.1091 | 0.2587 | ±0.5175 | +0.422 | 0.6734 |  |
| Site: UCSD (vs UAB) | -0.1633 | 0.1771 | ±0.3543 | -0.922 | 0.3566 |  |
| **Site: UW (vs UAB)** | **-1.1741** | 0.1789 | ±0.3578 | **-6.564** | **5.25e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7103** | 0.1908 | ±0.3815 | **-3.723** | **1.97e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5664** | 0.2177 | ±0.4355 | **+7.194** | **6.29e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7585** | 0.1997 | ±0.3994 | **-8.806** | **1.30e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0124 | +0.323 | 0.7465 |  |
| BMI (kg/m2) | +0.0075 | 0.0102 | ±0.0204 | +0.731 | 0.4648 |  |
| **Hypertension** | **+0.3204** | 0.1538 | ±0.3076 | **+2.083** | **0.0372** | * |
| High cholesterol | -0.0804 | 0.1413 | ±0.2825 | -0.569 | 0.5693 |  |
| Kidney disease | +0.1038 | 0.2246 | ±0.4493 | +0.462 | 0.6440 |  |
| Circulatory disease | +0.3715 | 0.2185 | ±0.4371 | +1.700 | 0.0892 | . |
| Nocturnal time > 180 (%) | -0.0000 | 0.0185 | ±0.0370 | -0.001 | 0.9990 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 872; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **872**, R² = **0.2626**, Adj R² = **0.2514**, F-statistic = **23.50** (p = **1.29e-48**), Residual SE = **5.775** on **858** df, AIC = **5546.7**, BIC = **5613.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4372** | 1.5438 | ±3.0877 | **+32.022** | **5.33e-225** | *** |
| **Education: graduate level (vs college)** | **+1.1957** | 0.4200 | ±0.8400 | **+2.847** | **0.0044** | ** |
| Education: high school or below (vs college) | +0.6717 | 0.7786 | ±1.5571 | +0.863 | 0.3882 |  |
| **Site: UCSD (vs UAB)** | **+3.2259** | 0.5302 | ±1.0603 | **+6.085** | **1.17e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5433** | 0.5089 | ±1.0178 | **-3.033** | **0.0024** | ** |
| **Season: spring (vs autumn)** | **-1.1481** | 0.5664 | ±1.1327 | **-2.027** | **0.0427** | * |
| **Season: summer (vs autumn)** | **+2.1417** | 0.5891 | ±1.1782 | **+3.635** | **2.77e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0946** | 0.5945 | ±1.1889 | **-8.570** | **1.03e-17** | *** |
| **Age (years)** | **-0.0368** | 0.0186 | ±0.0372 | **-1.981** | **0.0476** | * |
| BMI (kg/m2) | -0.0487 | 0.0283 | ±0.0566 | -1.719 | 0.0856 | . |
| Hypertension | +0.2814 | 0.4516 | ±0.9031 | +0.623 | 0.5332 |  |
| **High cholesterol** | **-1.0705** | 0.4199 | ±0.8398 | **-2.549** | **0.0108** | * |
| Kidney disease | +0.2443 | 0.7193 | ±1.4386 | +0.340 | 0.7341 |  |
| Circulatory disease | -0.4864 | 0.5933 | ±1.1865 | -0.820 | 0.4123 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **872**, R² = **0.2632**, Adj R² = **0.2511**, F-statistic = **21.86** (p = **4.59e-48**), Residual SE = **5.776** on **857** df, AIC = **5548.0**, BIC = **5619.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.2834** | 3.1745 | ±6.3490 | **+14.895** | **3.56e-50** | *** |
| **Education: graduate level (vs college)** | **+1.1943** | 0.4205 | ±0.8410 | **+2.840** | **0.0045** | ** |
| Education: high school or below (vs college) | +0.6419 | 0.7799 | ±1.5598 | +0.823 | 0.4104 |  |
| **Site: UCSD (vs UAB)** | **+3.2292** | 0.5302 | ±1.0604 | **+6.091** | **1.12e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5396** | 0.5094 | ±1.0189 | **-3.022** | **0.0025** | ** |
| Season: spring (vs autumn) | -1.1031 | 0.5690 | ±1.1380 | -1.939 | 0.0526 | . |
| **Season: summer (vs autumn)** | **+2.1313** | 0.5890 | ±1.1780 | **+3.618** | **2.96e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0674** | 0.5968 | ±1.1936 | **-8.491** | **2.04e-17** | *** |
| **Age (years)** | **-0.0377** | 0.0188 | ±0.0376 | **-2.005** | **0.0450** | * |
| BMI (kg/m2) | -0.0532 | 0.0292 | ±0.0584 | -1.823 | 0.0683 | . |
| Hypertension | +0.2337 | 0.4552 | ±0.9104 | +0.513 | 0.6076 |  |
| **High cholesterol** | **-1.1197** | 0.4237 | ±0.8473 | **-2.643** | **0.0082** | ** |
| Kidney disease | +0.2455 | 0.7175 | ±1.4349 | +0.342 | 0.7322 |  |
| Circulatory disease | -0.5109 | 0.5912 | ±1.1824 | -0.864 | 0.3875 |  |
| HbA1c (%) | +0.4170 | 0.5660 | ±1.1321 | +0.737 | 0.4613 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **872**, R² = **0.2642**, Adj R² = **0.2522**, F-statistic = **21.98** (p = **2.55e-48**), Residual SE = **5.772** on **857** df, AIC = **5546.8**, BIC = **5618.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.8514** | 2.4405 | ±4.8811 | **+19.197** | **3.91e-82** | *** |
| **Education: graduate level (vs college)** | **+1.1692** | 0.4202 | ±0.8405 | **+2.782** | **0.0054** | ** |
| Education: high school or below (vs college) | +0.6506 | 0.7765 | ±1.5530 | +0.838 | 0.4021 |  |
| **Site: UCSD (vs UAB)** | **+3.2595** | 0.5299 | ±1.0597 | **+6.152** | **7.67e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5612** | 0.5085 | ±1.0169 | **-3.070** | **0.0021** | ** |
| **Season: spring (vs autumn)** | **-1.1456** | 0.5666 | ±1.1331 | **-2.022** | **0.0432** | * |
| **Season: summer (vs autumn)** | **+2.1128** | 0.5917 | ±1.1834 | **+3.571** | **3.56e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0785** | 0.5946 | ±1.1893 | **-8.540** | **1.34e-17** | *** |
| **Age (years)** | **-0.0373** | 0.0186 | ±0.0372 | **-2.005** | **0.0450** | * |
| BMI (kg/m2) | -0.0538 | 0.0285 | ±0.0571 | -1.885 | 0.0594 | . |
| Hypertension | +0.2093 | 0.4555 | ±0.9111 | +0.459 | 0.6459 |  |
| **High cholesterol** | **-1.0807** | 0.4190 | ±0.8379 | **-2.579** | **0.0099** | ** |
| Kidney disease | +0.1801 | 0.7128 | ±1.4256 | +0.253 | 0.8005 |  |
| Circulatory disease | -0.5328 | 0.5927 | ±1.1855 | -0.899 | 0.3688 |  |
| Mean glucose (mg/dL) | +0.0233 | 0.0167 | ±0.0334 | +1.397 | 0.1624 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **872**, R² = **0.2642**, Adj R² = **0.2522**, F-statistic = **21.98** (p = **2.55e-48**), Residual SE = **5.772** on **857** df, AIC = **5546.8**, BIC = **5618.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6274** | 4.4711 | ±8.9423 | **+9.758** | **1.71e-22** | *** |
| **Education: graduate level (vs college)** | **+1.1692** | 0.4202 | ±0.8405 | **+2.782** | **0.0054** | ** |
| Education: high school or below (vs college) | +0.6506 | 0.7765 | ±1.5530 | +0.838 | 0.4021 |  |
| **Site: UCSD (vs UAB)** | **+3.2595** | 0.5299 | ±1.0597 | **+6.152** | **7.67e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5612** | 0.5085 | ±1.0169 | **-3.070** | **0.0021** | ** |
| **Season: spring (vs autumn)** | **-1.1456** | 0.5666 | ±1.1331 | **-2.022** | **0.0432** | * |
| **Season: summer (vs autumn)** | **+2.1128** | 0.5917 | ±1.1834 | **+3.571** | **3.56e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0785** | 0.5946 | ±1.1893 | **-8.540** | **1.34e-17** | *** |
| **Age (years)** | **-0.0373** | 0.0186 | ±0.0372 | **-2.005** | **0.0450** | * |
| BMI (kg/m2) | -0.0538 | 0.0285 | ±0.0571 | -1.885 | 0.0594 | . |
| Hypertension | +0.2093 | 0.4555 | ±0.9111 | +0.459 | 0.6459 |  |
| **High cholesterol** | **-1.0807** | 0.4190 | ±0.8379 | **-2.579** | **0.0099** | ** |
| Kidney disease | +0.1801 | 0.7128 | ±1.4256 | +0.253 | 0.8005 |  |
| Circulatory disease | -0.5328 | 0.5927 | ±1.1855 | -0.899 | 0.3688 |  |
| GMI (%) | +0.9740 | 0.6972 | ±1.3944 | +1.397 | 0.1624 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **872**, R² = **0.2644**, Adj R² = **0.2524**, F-statistic = **22.00** (p = **2.34e-48**), Residual SE = **5.771** on **857** df, AIC = **5546.6**, BIC = **5618.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.0513** | 2.2821 | ±4.5642 | **+20.618** | **1.91e-94** | *** |
| **Education: graduate level (vs college)** | **+1.1750** | 0.4204 | ±0.8408 | **+2.795** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.6523 | 0.7785 | ±1.5570 | +0.838 | 0.4021 |  |
| **Site: UCSD (vs UAB)** | **+3.2318** | 0.5303 | ±1.0607 | **+6.094** | **1.10e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5680** | 0.5085 | ±1.0170 | **-3.083** | **0.0020** | ** |
| **Season: spring (vs autumn)** | **-1.1611** | 0.5659 | ±1.1318 | **-2.052** | **0.0402** | * |
| **Season: summer (vs autumn)** | **+2.1066** | 0.5912 | ±1.1825 | **+3.563** | **3.66e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0950** | 0.5946 | ±1.1893 | **-8.568** | **1.05e-17** | *** |
| Age (years) | -0.0352 | 0.0186 | ±0.0373 | -1.887 | 0.0591 | . |
| **BMI (kg/m2)** | **-0.0579** | 0.0294 | ±0.0587 | **-1.973** | **0.0485** | * |
| Hypertension | +0.2312 | 0.4528 | ±0.9056 | +0.511 | 0.6096 |  |
| **High cholesterol** | **-1.1030** | 0.4185 | ±0.8369 | **-2.636** | **0.0084** | ** |
| Kidney disease | +0.2203 | 0.7170 | ±1.4339 | +0.307 | 0.7586 |  |
| Circulatory disease | -0.5300 | 0.5933 | ±1.1865 | -0.893 | 0.3716 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0218 | 0.0152 | ±0.0304 | +1.431 | 0.1524 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **872**, R² = **0.2698**, Adj R² = **0.2578**, F-statistic = **22.61** (p = **1.12e-49**), Residual SE = **5.750** on **857** df, AIC = **5540.2**, BIC = **5611.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.0502** | 1.7680 | ±3.5360 | **+26.612** | **4.88e-156** | *** |
| **Education: graduate level (vs college)** | **+1.2146** | 0.4193 | ±0.8387 | **+2.896** | **0.0038** | ** |
| Education: high school or below (vs college) | +0.5236 | 0.7688 | ±1.5376 | +0.681 | 0.4958 |  |
| **Site: UCSD (vs UAB)** | **+3.3470** | 0.5254 | ±1.0507 | **+6.371** | **1.88e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5171** | 0.5036 | ±1.0071 | **-3.013** | **0.0026** | ** |
| **Season: spring (vs autumn)** | **-1.1626** | 0.5640 | ±1.1279 | **-2.061** | **0.0393** | * |
| **Season: summer (vs autumn)** | **+2.1123** | 0.5868 | ±1.1736 | **+3.600** | **3.19e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1235** | 0.5942 | ±1.1883 | **-8.623** | **6.52e-18** | *** |
| **Age (years)** | **-0.0403** | 0.0185 | ±0.0370 | **-2.183** | **0.0290** | * |
| BMI (kg/m2) | -0.0534 | 0.0285 | ±0.0570 | -1.876 | 0.0607 | . |
| Hypertension | +0.1108 | 0.4537 | ±0.9075 | +0.244 | 0.8071 |  |
| **High cholesterol** | **-1.1013** | 0.4183 | ±0.8365 | **-2.633** | **0.0085** | ** |
| Kidney disease | +0.0833 | 0.6981 | ±1.3962 | +0.119 | 0.9051 |  |
| Circulatory disease | -0.5396 | 0.5818 | ±1.1636 | -0.927 | 0.3537 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.1421** | 0.0483 | ±0.0967 | **+2.940** | **0.0033** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **872**, R² = **0.2693**, Adj R² = **0.2574**, F-statistic = **22.56** (p = **1.45e-49**), Residual SE = **5.752** on **857** df, AIC = **5540.7**, BIC = **5612.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.3062** | 1.7532 | ±3.5064 | **+26.983** | **2.34e-160** | *** |
| **Education: graduate level (vs college)** | **+1.2024** | 0.4194 | ±0.8388 | **+2.867** | **0.0041** | ** |
| Education: high school or below (vs college) | +0.5470 | 0.7693 | ±1.5385 | +0.711 | 0.4770 |  |
| **Site: UCSD (vs UAB)** | **+3.3354** | 0.5249 | ±1.0499 | **+6.354** | **2.10e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5299** | 0.5037 | ±1.0075 | **-3.037** | **0.0024** | ** |
| **Season: spring (vs autumn)** | **-1.1327** | 0.5642 | ±1.1285 | **-2.008** | **0.0447** | * |
| **Season: summer (vs autumn)** | **+2.1476** | 0.5871 | ±1.1741 | **+3.658** | **2.54e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0832** | 0.5933 | ±1.1866 | **-8.568** | **1.05e-17** | *** |
| **Age (years)** | **-0.0403** | 0.0184 | ±0.0369 | **-2.186** | **0.0288** | * |
| BMI (kg/m2) | -0.0538 | 0.0286 | ±0.0572 | -1.882 | 0.0598 | . |
| Hypertension | +0.1120 | 0.4543 | ±0.9086 | +0.247 | 0.8052 |  |
| **High cholesterol** | **-1.0903** | 0.4187 | ±0.8374 | **-2.604** | **0.0092** | ** |
| Kidney disease | +0.0992 | 0.6996 | ±1.3991 | +0.142 | 0.8873 |  |
| Circulatory disease | -0.5124 | 0.5842 | ±1.1683 | -0.877 | 0.3805 |  |
| **Avg. daily SD (mg/dL)** | **+0.1397** | 0.0489 | ±0.0978 | **+2.858** | **0.0043** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **872**, R² = **0.2680**, Adj R² = **0.2560**, F-statistic = **22.41** (p = **3.06e-49**), Residual SE = **5.757** on **857** df, AIC = **5542.3**, BIC = **5613.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.7770** | 1.9067 | ±3.8134 | **+24.533** | **6.58e-133** | *** |
| **Education: graduate level (vs college)** | **+1.2472** | 0.4194 | ±0.8388 | **+2.974** | **0.0029** | ** |
| Education: high school or below (vs college) | +0.5488 | 0.7732 | ±1.5465 | +0.710 | 0.4779 |  |
| **Site: UCSD (vs UAB)** | **+3.3161** | 0.5266 | ±1.0533 | **+6.297** | **3.04e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5018** | 0.5049 | ±1.0098 | **-2.974** | **0.0029** | ** |
| **Season: spring (vs autumn)** | **-1.1671** | 0.5643 | ±1.1286 | **-2.068** | **0.0386** | * |
| **Season: summer (vs autumn)** | **+2.1354** | 0.5850 | ±1.1699 | **+3.650** | **2.62e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1517** | 0.5950 | ±1.1900 | **-8.658** | **4.80e-18** | *** |
| **Age (years)** | **-0.0400** | 0.0185 | ±0.0370 | **-2.161** | **0.0307** | * |
| BMI (kg/m2) | -0.0481 | 0.0284 | ±0.0568 | -1.696 | 0.0899 | . |
| Hypertension | +0.1800 | 0.4514 | ±0.9028 | +0.399 | 0.6900 |  |
| **High cholesterol** | **-1.0857** | 0.4194 | ±0.8388 | **-2.589** | **0.0096** | ** |
| Kidney disease | +0.1462 | 0.7071 | ±1.4142 | +0.207 | 0.8362 |  |
| Circulatory disease | -0.4884 | 0.5856 | ±1.1712 | -0.834 | 0.4042 |  |
| **CV (%)** | **+0.1745** | 0.0702 | ±0.1404 | **+2.486** | **0.0129** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **872**, R² = **0.2657**, Adj R² = **0.2537**, F-statistic = **22.15** (p = **1.12e-48**), Residual SE = **5.766** on **857** df, AIC = **5545.0**, BIC = **5616.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6715** | 1.9372 | ±3.8744 | **+26.673** | **9.63e-157** | *** |
| **Education: graduate level (vs college)** | **+1.2409** | 0.4200 | ±0.8400 | **+2.954** | **0.0031** | ** |
| Education: high school or below (vs college) | +0.5852 | 0.7766 | ±1.5532 | +0.754 | 0.4511 |  |
| **Site: UCSD (vs UAB)** | **+3.2788** | 0.5278 | ±1.0556 | **+6.212** | **5.23e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5274** | 0.5061 | ±1.0122 | **-3.018** | **0.0025** | ** |
| **Season: spring (vs autumn)** | **-1.1757** | 0.5650 | ±1.1301 | **-2.081** | **0.0375** | * |
| **Season: summer (vs autumn)** | **+2.1409** | 0.5873 | ±1.1745 | **+3.646** | **2.67e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1413** | 0.5957 | ±1.1913 | **-8.631** | **6.06e-18** | *** |
| **Age (years)** | **-0.0390** | 0.0185 | ±0.0371 | **-2.103** | **0.0355** | * |
| BMI (kg/m2) | -0.0487 | 0.0284 | ±0.0567 | -1.715 | 0.0863 | . |
| Hypertension | +0.2063 | 0.4522 | ±0.9043 | +0.456 | 0.6483 |  |
| **High cholesterol** | **-1.0782** | 0.4200 | ±0.8400 | **-2.567** | **0.0103** | * |
| Kidney disease | +0.1723 | 0.7114 | ±1.4228 | +0.242 | 0.8087 |  |
| Circulatory disease | -0.4766 | 0.5873 | ±1.1747 | -0.811 | 0.4171 |  |
| Mean / SD ratio | -0.3297 | 0.1768 | ±0.3536 | -1.865 | 0.0622 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **872**, R² = **0.2663**, Adj R² = **0.2543**, F-statistic = **22.21** (p = **8.11e-49**), Residual SE = **5.764** on **857** df, AIC = **5544.3**, BIC = **5615.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6983** | 1.8983 | ±3.7967 | **+27.233** | **2.62e-163** | *** |
| **Education: graduate level (vs college)** | **+1.2381** | 0.4195 | ±0.8391 | **+2.951** | **0.0032** | ** |
| Education: high school or below (vs college) | +0.5944 | 0.7759 | ±1.5518 | +0.766 | 0.4436 |  |
| **Site: UCSD (vs UAB)** | **+3.2724** | 0.5260 | ±1.0520 | **+6.221** | **4.93e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5386** | 0.5058 | ±1.0116 | **-3.042** | **0.0024** | ** |
| **Season: spring (vs autumn)** | **-1.1589** | 0.5646 | ±1.1291 | **-2.053** | **0.0401** | * |
| **Season: summer (vs autumn)** | **+2.1632** | 0.5873 | ±1.1747 | **+3.683** | **2.30e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1117** | 0.5940 | ±1.1881 | **-8.605** | **7.64e-18** | *** |
| **Age (years)** | **-0.0395** | 0.0185 | ±0.0370 | **-2.135** | **0.0327** | * |
| BMI (kg/m2) | -0.0501 | 0.0285 | ±0.0570 | -1.760 | 0.0785 | . |
| Hypertension | +0.2065 | 0.4517 | ±0.9034 | +0.457 | 0.6476 |  |
| **High cholesterol** | **-1.0713** | 0.4203 | ±0.8406 | **-2.549** | **0.0108** | * |
| Kidney disease | +0.1679 | 0.7105 | ±1.4210 | +0.236 | 0.8132 |  |
| Circulatory disease | -0.4464 | 0.5894 | ±1.1787 | -0.757 | 0.4488 |  |
| Avg. daily mean/SD | -0.2862 | 0.1461 | ±0.2922 | -1.959 | 0.0501 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **872**, R² = **0.2626**, Adj R² = **0.2506**, F-statistic = **21.80** (p = **6.16e-48**), Residual SE = **5.778** on **857** df, AIC = **5548.6**, BIC = **5620.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1222** | 1.9577 | ±3.9153 | **+25.092** | **6.06e-139** | *** |
| **Education: graduate level (vs college)** | **+1.1951** | 0.4206 | ±0.8413 | **+2.841** | **0.0045** | ** |
| Education: high school or below (vs college) | +0.6568 | 0.7818 | ±1.5636 | +0.840 | 0.4009 |  |
| **Site: UCSD (vs UAB)** | **+3.2306** | 0.5310 | ±1.0620 | **+6.084** | **1.17e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5394** | 0.5101 | ±1.0203 | **-3.018** | **0.0025** | ** |
| **Season: spring (vs autumn)** | **-1.1490** | 0.5666 | ±1.1332 | **-2.028** | **0.0426** | * |
| **Season: summer (vs autumn)** | **+2.1459** | 0.5893 | ±1.1786 | **+3.642** | **2.71e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0921** | 0.5952 | ±1.1905 | **-8.555** | **1.18e-17** | *** |
| **Age (years)** | **-0.0367** | 0.0186 | ±0.0372 | **-1.972** | **0.0486** | * |
| BMI (kg/m2) | -0.0486 | 0.0283 | ±0.0567 | -1.716 | 0.0862 | . |
| Hypertension | +0.2832 | 0.4521 | ±0.9042 | +0.626 | 0.5310 |  |
| **High cholesterol** | **-1.0707** | 0.4205 | ±0.8410 | **-2.546** | **0.0109** | * |
| Kidney disease | +0.2373 | 0.7212 | ±1.4424 | +0.329 | 0.7421 |  |
| Circulatory disease | -0.4813 | 0.5948 | ±1.1897 | -0.809 | 0.4185 |  |
| MAG (mg/dL/h) | +0.0084 | 0.0312 | ±0.0624 | +0.270 | 0.7873 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **872**, R² = **0.2661**, Adj R² = **0.2541**, F-statistic = **22.19** (p = **9.11e-49**), Residual SE = **5.765** on **857** df, AIC = **5544.6**, BIC = **5616.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.3951** | 1.8791 | ±3.7582 | **+25.222** | **2.28e-140** | *** |
| **Education: graduate level (vs college)** | **+1.1854** | 0.4206 | ±0.8412 | **+2.818** | **0.0048** | ** |
| Education: high school or below (vs college) | +0.5780 | 0.7719 | ±1.5438 | +0.749 | 0.4540 |  |
| **Site: UCSD (vs UAB)** | **+3.2898** | 0.5268 | ±1.0536 | **+6.245** | **4.24e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5367** | 0.5066 | ±1.0133 | **-3.033** | **0.0024** | ** |
| **Season: spring (vs autumn)** | **-1.1544** | 0.5634 | ±1.1268 | **-2.049** | **0.0405** | * |
| **Season: summer (vs autumn)** | **+2.1637** | 0.5867 | ±1.1735 | **+3.688** | **2.26e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0821** | 0.5950 | ±1.1901 | **-8.541** | **1.33e-17** | *** |
| **Age (years)** | **-0.0389** | 0.0185 | ±0.0369 | **-2.107** | **0.0351** | * |
| BMI (kg/m2) | -0.0470 | 0.0284 | ±0.0568 | -1.656 | 0.0977 | . |
| Hypertension | +0.2015 | 0.4537 | ±0.9074 | +0.444 | 0.6570 |  |
| **High cholesterol** | **-1.0766** | 0.4202 | ±0.8404 | **-2.562** | **0.0104** | * |
| Kidney disease | +0.1543 | 0.7085 | ±1.4170 | +0.218 | 0.8276 |  |
| Circulatory disease | -0.5085 | 0.5891 | ±1.1781 | -0.863 | 0.3880 |  |
| **Avg. daily range (mg/dL)** | **+0.0237** | 0.0116 | ±0.0233 | **+2.031** | **0.0423** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **872**, R² = **0.2653**, Adj R² = **0.2533**, F-statistic = **22.10** (p = **1.40e-48**), Residual SE = **5.768** on **857** df, AIC = **5545.5**, BIC = **5617.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.7475** | 1.5681 | ±3.1362 | **+31.087** | **3.60e-212** | *** |
| **Education: graduate level (vs college)** | **+1.1934** | 0.4202 | ±0.8404 | **+2.840** | **0.0045** | ** |
| Education: high school or below (vs college) | +0.5885 | 0.7781 | ±1.5561 | +0.756 | 0.4494 |  |
| **Site: UCSD (vs UAB)** | **+3.2795** | 0.5306 | ±1.0613 | **+6.180** | **6.39e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5162** | 0.5080 | ±1.0161 | **-2.984** | **0.0028** | ** |
| **Season: spring (vs autumn)** | **-1.2171** | 0.5683 | ±1.1367 | **-2.142** | **0.0322** | * |
| **Season: summer (vs autumn)** | **+2.0251** | 0.5900 | ±1.1800 | **+3.432** | **5.98e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1509** | 0.5966 | ±1.1933 | **-8.633** | **5.97e-18** | *** |
| **Age (years)** | **-0.0366** | 0.0186 | ±0.0371 | **-1.969** | **0.0489** | * |
| BMI (kg/m2) | -0.0538 | 0.0287 | ±0.0574 | -1.876 | 0.0607 | . |
| Hypertension | +0.2785 | 0.4519 | ±0.9038 | +0.616 | 0.5377 |  |
| **High cholesterol** | **-1.1305** | 0.4188 | ±0.8375 | **-2.700** | **0.0069** | ** |
| Kidney disease | +0.2107 | 0.7106 | ±1.4212 | +0.297 | 0.7668 |  |
| Circulatory disease | -0.5800 | 0.5862 | ±1.1725 | -0.989 | 0.3225 |  |
| SD of daily means (mg/dL) | +0.1511 | 0.0924 | ±0.1848 | +1.636 | 0.1019 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **872**, R² = **0.2662**, Adj R² = **0.2542**, F-statistic = **22.21** (p = **8.24e-49**), Residual SE = **5.764** on **857** df, AIC = **5544.4**, BIC = **5615.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.6964** | 6.4605 | ±12.9210 | **+9.550** | **1.30e-21** | *** |
| **Education: graduate level (vs college)** | **+1.1781** | 0.4200 | ±0.8400 | **+2.805** | **0.0050** | ** |
| Education: high school or below (vs college) | +0.6183 | 0.7769 | ±1.5537 | +0.796 | 0.4261 |  |
| **Site: UCSD (vs UAB)** | **+3.3021** | 0.5325 | ±1.0651 | **+6.201** | **5.62e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5283** | 0.5078 | ±1.0156 | **-3.010** | **0.0026** | ** |
| **Season: spring (vs autumn)** | **-1.1308** | 0.5652 | ±1.1304 | **-2.001** | **0.0454** | * |
| **Season: summer (vs autumn)** | **+2.1159** | 0.5897 | ±1.1794 | **+3.588** | **3.33e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0827** | 0.5922 | ±1.1844 | **-8.582** | **9.29e-18** | *** |
| **Age (years)** | **-0.0386** | 0.0186 | ±0.0372 | **-2.076** | **0.0379** | * |
| BMI (kg/m2) | -0.0522 | 0.0284 | ±0.0569 | -1.835 | 0.0665 | . |
| Hypertension | +0.2091 | 0.4545 | ±0.9089 | +0.460 | 0.6454 |  |
| **High cholesterol** | **-1.1134** | 0.4189 | ±0.8379 | **-2.658** | **0.0079** | ** |
| Kidney disease | +0.1160 | 0.7003 | ±1.4006 | +0.166 | 0.8684 |  |
| Circulatory disease | -0.5585 | 0.5868 | ±1.1736 | -0.952 | 0.3412 |  |
| Time in range 70-180, pooled (%) | -0.1230 | 0.0643 | ±0.1286 | -1.913 | 0.0558 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **872**, R² = **0.2668**, Adj R² = **0.2548**, F-statistic = **22.27** (p = **6.11e-49**), Residual SE = **5.762** on **857** df, AIC = **5543.7**, BIC = **5615.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8732** | 6.4308 | ±12.8616 | **+9.777** | **1.41e-22** | *** |
| **Education: graduate level (vs college)** | **+1.1786** | 0.4198 | ±0.8397 | **+2.807** | **0.0050** | ** |
| Education: high school or below (vs college) | +0.6270 | 0.7771 | ±1.5541 | +0.807 | 0.4198 |  |
| **Site: UCSD (vs UAB)** | **+3.3097** | 0.5321 | ±1.0643 | **+6.220** | **4.98e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5264** | 0.5076 | ±1.0151 | **-3.007** | **0.0026** | ** |
| **Season: spring (vs autumn)** | **-1.1263** | 0.5650 | ±1.1301 | **-1.993** | **0.0462** | * |
| **Season: summer (vs autumn)** | **+2.1129** | 0.5893 | ±1.1787 | **+3.585** | **3.37e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0790** | 0.5920 | ±1.1839 | **-8.580** | **9.50e-18** | *** |
| **Age (years)** | **-0.0385** | 0.0186 | ±0.0371 | **-2.074** | **0.0380** | * |
| BMI (kg/m2) | -0.0526 | 0.0285 | ±0.0569 | -1.849 | 0.0644 | . |
| Hypertension | +0.2029 | 0.4538 | ±0.9075 | +0.447 | 0.6547 |  |
| **High cholesterol** | **-1.1176** | 0.4188 | ±0.8375 | **-2.669** | **0.0076** | ** |
| Kidney disease | +0.0999 | 0.6983 | ±1.3967 | +0.143 | 0.8863 |  |
| Circulatory disease | -0.5671 | 0.5866 | ±1.1733 | -0.967 | 0.3337 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.1348** | 0.0641 | ±0.1282 | **-2.102** | **0.0355** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **872**, R² = **0.2627**, Adj R² = **0.2507**, F-statistic = **21.81** (p = **5.86e-48**), Residual SE = **5.778** on **857** df, AIC = **5548.5**, BIC = **5620.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3930** | 1.5488 | ±3.0976 | **+31.891** | **3.51e-223** | *** |
| **Education: graduate level (vs college)** | **+1.2104** | 0.4206 | ±0.8412 | **+2.878** | **0.0040** | ** |
| Education: high school or below (vs college) | +0.6850 | 0.7795 | ±1.5589 | +0.879 | 0.3795 |  |
| **Site: UCSD (vs UAB)** | **+3.2209** | 0.5304 | ±1.0607 | **+6.073** | **1.26e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5395** | 0.5092 | ±1.0184 | **-3.023** | **0.0025** | ** |
| **Season: spring (vs autumn)** | **-1.1476** | 0.5664 | ±1.1329 | **-2.026** | **0.0428** | * |
| **Season: summer (vs autumn)** | **+2.1354** | 0.5882 | ±1.1764 | **+3.630** | **2.83e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1037** | 0.5949 | ±1.1898 | **-8.579** | **9.56e-18** | *** |
| **Age (years)** | **-0.0369** | 0.0186 | ±0.0372 | **-1.984** | **0.0472** | * |
| BMI (kg/m2) | -0.0483 | 0.0283 | ±0.0566 | -1.704 | 0.0883 | . |
| Hypertension | +0.2829 | 0.4519 | ±0.9038 | +0.626 | 0.5313 |  |
| **High cholesterol** | **-1.0743** | 0.4203 | ±0.8406 | **-2.556** | **0.0106** | * |
| Kidney disease | +0.2521 | 0.7195 | ±1.4390 | +0.350 | 0.7261 |  |
| Circulatory disease | -0.4798 | 0.5948 | ±1.1895 | -0.807 | 0.4198 |  |
| Time 54-69, pooled (%) | +0.1777 | 0.4251 | ±0.8503 | +0.418 | 0.6760 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **872**, R² = **0.2626**, Adj R² = **0.2506**, F-statistic = **21.80** (p = **6.23e-48**), Residual SE = **5.778** on **857** df, AIC = **5548.6**, BIC = **5620.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4153** | 1.5478 | ±3.0956 | **+31.926** | **1.16e-223** | *** |
| **Education: graduate level (vs college)** | **+1.2044** | 0.4205 | ±0.8411 | **+2.864** | **0.0042** | ** |
| Education: high school or below (vs college) | +0.6798 | 0.7790 | ±1.5580 | +0.873 | 0.3828 |  |
| **Site: UCSD (vs UAB)** | **+3.2209** | 0.5302 | ±1.0605 | **+6.075** | **1.24e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5418** | 0.5092 | ±1.0184 | **-3.028** | **0.0025** | ** |
| **Season: spring (vs autumn)** | **-1.1466** | 0.5668 | ±1.1336 | **-2.023** | **0.0431** | * |
| **Season: summer (vs autumn)** | **+2.1397** | 0.5889 | ±1.1778 | **+3.633** | **2.80e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1004** | 0.5951 | ±1.1902 | **-8.571** | **1.03e-17** | *** |
| **Age (years)** | **-0.0369** | 0.0186 | ±0.0372 | **-1.984** | **0.0473** | * |
| BMI (kg/m2) | -0.0484 | 0.0283 | ±0.0567 | -1.710 | 0.0873 | . |
| Hypertension | +0.2822 | 0.4520 | ±0.9039 | +0.624 | 0.5324 |  |
| **High cholesterol** | **-1.0724** | 0.4202 | ±0.8404 | **-2.552** | **0.0107** | * |
| Kidney disease | +0.2484 | 0.7198 | ±1.4396 | +0.345 | 0.7300 |  |
| Circulatory disease | -0.4808 | 0.5951 | ±1.1901 | -0.808 | 0.4191 |  |
| Avg. daily time 54-69 (%) | +0.0972 | 0.4008 | ±0.8016 | +0.243 | 0.8083 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **872**, R² = **0.2627**, Adj R² = **0.2507**, F-statistic = **21.81** (p = **5.86e-48**), Residual SE = **5.778** on **857** df, AIC = **5548.5**, BIC = **5620.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3930** | 1.5488 | ±3.0976 | **+31.891** | **3.51e-223** | *** |
| **Education: graduate level (vs college)** | **+1.2104** | 0.4206 | ±0.8412 | **+2.878** | **0.0040** | ** |
| Education: high school or below (vs college) | +0.6850 | 0.7795 | ±1.5589 | +0.879 | 0.3795 |  |
| **Site: UCSD (vs UAB)** | **+3.2209** | 0.5304 | ±1.0607 | **+6.073** | **1.26e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5395** | 0.5092 | ±1.0184 | **-3.023** | **0.0025** | ** |
| **Season: spring (vs autumn)** | **-1.1476** | 0.5664 | ±1.1329 | **-2.026** | **0.0428** | * |
| **Season: summer (vs autumn)** | **+2.1354** | 0.5882 | ±1.1764 | **+3.630** | **2.83e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1037** | 0.5949 | ±1.1898 | **-8.579** | **9.56e-18** | *** |
| **Age (years)** | **-0.0369** | 0.0186 | ±0.0372 | **-1.984** | **0.0472** | * |
| BMI (kg/m2) | -0.0483 | 0.0283 | ±0.0566 | -1.704 | 0.0883 | . |
| Hypertension | +0.2829 | 0.4519 | ±0.9038 | +0.626 | 0.5313 |  |
| **High cholesterol** | **-1.0743** | 0.4203 | ±0.8406 | **-2.556** | **0.0106** | * |
| Kidney disease | +0.2521 | 0.7195 | ±1.4390 | +0.350 | 0.7261 |  |
| Circulatory disease | -0.4798 | 0.5948 | ±1.1895 | -0.807 | 0.4198 |  |
| Time < 70 (%) | +0.1777 | 0.4251 | ±0.8503 | +0.418 | 0.6760 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **872**, R² = **0.2626**, Adj R² = **0.2506**, F-statistic = **21.80** (p = **6.23e-48**), Residual SE = **5.778** on **857** df, AIC = **5548.6**, BIC = **5620.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4153** | 1.5478 | ±3.0956 | **+31.926** | **1.16e-223** | *** |
| **Education: graduate level (vs college)** | **+1.2044** | 0.4205 | ±0.8411 | **+2.864** | **0.0042** | ** |
| Education: high school or below (vs college) | +0.6798 | 0.7790 | ±1.5580 | +0.873 | 0.3828 |  |
| **Site: UCSD (vs UAB)** | **+3.2209** | 0.5302 | ±1.0605 | **+6.075** | **1.24e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5418** | 0.5092 | ±1.0184 | **-3.028** | **0.0025** | ** |
| **Season: spring (vs autumn)** | **-1.1466** | 0.5668 | ±1.1336 | **-2.023** | **0.0431** | * |
| **Season: summer (vs autumn)** | **+2.1397** | 0.5889 | ±1.1778 | **+3.633** | **2.80e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1004** | 0.5951 | ±1.1902 | **-8.571** | **1.03e-17** | *** |
| **Age (years)** | **-0.0369** | 0.0186 | ±0.0372 | **-1.984** | **0.0473** | * |
| BMI (kg/m2) | -0.0484 | 0.0283 | ±0.0567 | -1.710 | 0.0873 | . |
| Hypertension | +0.2822 | 0.4520 | ±0.9039 | +0.624 | 0.5324 |  |
| **High cholesterol** | **-1.0724** | 0.4202 | ±0.8404 | **-2.552** | **0.0107** | * |
| Kidney disease | +0.2484 | 0.7198 | ±1.4396 | +0.345 | 0.7300 |  |
| Circulatory disease | -0.4808 | 0.5951 | ±1.1901 | -0.808 | 0.4191 |  |
| Avg. daily time < 70 (%) | +0.0972 | 0.4008 | ±0.8016 | +0.243 | 0.8083 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **872**, R² = **0.2660**, Adj R² = **0.2540**, F-statistic = **22.18** (p = **9.61e-49**), Residual SE = **5.765** on **857** df, AIC = **5544.7**, BIC = **5616.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4281** | 1.5556 | ±3.1112 | **+31.775** | **1.45e-221** | *** |
| **Education: graduate level (vs college)** | **+1.1692** | 0.4203 | ±0.8406 | **+2.782** | **0.0054** | ** |
| Education: high school or below (vs college) | +0.6119 | 0.7763 | ±1.5527 | +0.788 | 0.4305 |  |
| **Site: UCSD (vs UAB)** | **+3.3020** | 0.5326 | ±1.0653 | **+6.199** | **5.68e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5314** | 0.5079 | ±1.0157 | **-3.015** | **0.0026** | ** |
| **Season: spring (vs autumn)** | **-1.1318** | 0.5654 | ±1.1309 | **-2.002** | **0.0453** | * |
| **Season: summer (vs autumn)** | **+2.1212** | 0.5903 | ±1.1806 | **+3.594** | **3.26e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0772** | 0.5924 | ±1.1849 | **-8.570** | **1.04e-17** | *** |
| **Age (years)** | **-0.0384** | 0.0186 | ±0.0372 | **-2.069** | **0.0386** | * |
| BMI (kg/m2) | -0.0523 | 0.0284 | ±0.0568 | -1.839 | 0.0659 | . |
| Hypertension | +0.2115 | 0.4546 | ±0.9092 | +0.465 | 0.6418 |  |
| **High cholesterol** | **-1.1089** | 0.4190 | ±0.8380 | **-2.647** | **0.0081** | ** |
| Kidney disease | +0.1168 | 0.7016 | ±1.4031 | +0.166 | 0.8678 |  |
| Circulatory disease | -0.5596 | 0.5874 | ±1.1749 | -0.953 | 0.3408 |  |
| Time 181-250, pooled (%) | +0.1174 | 0.0636 | ±0.1272 | +1.845 | 0.0650 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **872**, R² = **0.2666**, Adj R² = **0.2546**, F-statistic = **22.25** (p = **6.87e-49**), Residual SE = **5.763** on **857** df, AIC = **5544.0**, BIC = **5615.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4266** | 1.5564 | ±3.1128 | **+31.757** | **2.56e-221** | *** |
| **Education: graduate level (vs college)** | **+1.1675** | 0.4201 | ±0.8402 | **+2.779** | **0.0054** | ** |
| Education: high school or below (vs college) | +0.6176 | 0.7764 | ±1.5529 | +0.795 | 0.4263 |  |
| **Site: UCSD (vs UAB)** | **+3.3136** | 0.5324 | ±1.0649 | **+6.223** | **4.86e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5289** | 0.5076 | ±1.0153 | **-3.012** | **0.0026** | ** |
| **Season: spring (vs autumn)** | **-1.1290** | 0.5652 | ±1.1304 | **-1.997** | **0.0458** | * |
| **Season: summer (vs autumn)** | **+2.1165** | 0.5899 | ±1.1798 | **+3.588** | **3.33e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0717** | 0.5923 | ±1.1845 | **-8.563** | **1.10e-17** | *** |
| **Age (years)** | **-0.0384** | 0.0186 | ±0.0371 | **-2.066** | **0.0388** | * |
| BMI (kg/m2) | -0.0528 | 0.0284 | ±0.0569 | -1.856 | 0.0635 | . |
| Hypertension | +0.2045 | 0.4540 | ±0.9079 | +0.450 | 0.6524 |  |
| **High cholesterol** | **-1.1134** | 0.4189 | ±0.8377 | **-2.658** | **0.0079** | ** |
| Kidney disease | +0.0992 | 0.6994 | ±1.3987 | +0.142 | 0.8872 |  |
| Circulatory disease | -0.5719 | 0.5873 | ±1.1747 | -0.974 | 0.3302 |  |
| **Avg. daily time 181-250 (%)** | **+0.1303** | 0.0636 | ±0.1271 | **+2.050** | **0.0404** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **872**, R² = **0.2660**, Adj R² = **0.2540**, F-statistic = **22.18** (p = **9.61e-49**), Residual SE = **5.765** on **857** df, AIC = **5544.7**, BIC = **5616.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4281** | 1.5556 | ±3.1112 | **+31.775** | **1.45e-221** | *** |
| **Education: graduate level (vs college)** | **+1.1692** | 0.4203 | ±0.8406 | **+2.782** | **0.0054** | ** |
| Education: high school or below (vs college) | +0.6119 | 0.7763 | ±1.5527 | +0.788 | 0.4305 |  |
| **Site: UCSD (vs UAB)** | **+3.3020** | 0.5326 | ±1.0653 | **+6.199** | **5.68e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5314** | 0.5079 | ±1.0157 | **-3.015** | **0.0026** | ** |
| **Season: spring (vs autumn)** | **-1.1318** | 0.5654 | ±1.1309 | **-2.002** | **0.0453** | * |
| **Season: summer (vs autumn)** | **+2.1212** | 0.5903 | ±1.1806 | **+3.594** | **3.26e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0772** | 0.5924 | ±1.1849 | **-8.570** | **1.04e-17** | *** |
| **Age (years)** | **-0.0384** | 0.0186 | ±0.0372 | **-2.069** | **0.0386** | * |
| BMI (kg/m2) | -0.0523 | 0.0284 | ±0.0568 | -1.839 | 0.0659 | . |
| Hypertension | +0.2115 | 0.4546 | ±0.9092 | +0.465 | 0.6418 |  |
| **High cholesterol** | **-1.1089** | 0.4190 | ±0.8380 | **-2.647** | **0.0081** | ** |
| Kidney disease | +0.1168 | 0.7016 | ±1.4031 | +0.166 | 0.8678 |  |
| Circulatory disease | -0.5596 | 0.5874 | ±1.1749 | -0.953 | 0.3408 |  |
| Time > 180 (%) | +0.1174 | 0.0636 | ±0.1272 | +1.845 | 0.0650 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **872**, R² = **0.2666**, Adj R² = **0.2546**, F-statistic = **22.25** (p = **6.87e-49**), Residual SE = **5.763** on **857** df, AIC = **5544.0**, BIC = **5615.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4266** | 1.5564 | ±3.1128 | **+31.757** | **2.56e-221** | *** |
| **Education: graduate level (vs college)** | **+1.1675** | 0.4201 | ±0.8402 | **+2.779** | **0.0054** | ** |
| Education: high school or below (vs college) | +0.6176 | 0.7764 | ±1.5529 | +0.795 | 0.4263 |  |
| **Site: UCSD (vs UAB)** | **+3.3136** | 0.5324 | ±1.0649 | **+6.223** | **4.86e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5289** | 0.5076 | ±1.0153 | **-3.012** | **0.0026** | ** |
| **Season: spring (vs autumn)** | **-1.1290** | 0.5652 | ±1.1304 | **-1.997** | **0.0458** | * |
| **Season: summer (vs autumn)** | **+2.1165** | 0.5899 | ±1.1798 | **+3.588** | **3.33e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0717** | 0.5923 | ±1.1845 | **-8.563** | **1.10e-17** | *** |
| **Age (years)** | **-0.0384** | 0.0186 | ±0.0371 | **-2.066** | **0.0388** | * |
| BMI (kg/m2) | -0.0528 | 0.0284 | ±0.0569 | -1.856 | 0.0635 | . |
| Hypertension | +0.2045 | 0.4540 | ±0.9079 | +0.450 | 0.6524 |  |
| **High cholesterol** | **-1.1134** | 0.4189 | ±0.8377 | **-2.658** | **0.0079** | ** |
| Kidney disease | +0.0992 | 0.6994 | ±1.3987 | +0.142 | 0.8872 |  |
| Circulatory disease | -0.5719 | 0.5873 | ±1.1747 | -0.974 | 0.3302 |  |
| **Avg. daily time > 180 (%)** | **+0.1303** | 0.0636 | ±0.1271 | **+2.050** | **0.0404** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **872**, R² = **0.2655**, Adj R² = **0.2535**, F-statistic = **22.12** (p = **1.26e-48**), Residual SE = **5.767** on **857** df, AIC = **5545.3**, BIC = **5616.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4960** | 1.5485 | ±3.0970 | **+31.964** | **3.48e-224** | *** |
| **Education: graduate level (vs college)** | **+1.1969** | 0.4195 | ±0.8391 | **+2.853** | **0.0043** | ** |
| Education: high school or below (vs college) | +0.5701 | 0.7766 | ±1.5531 | +0.734 | 0.4629 |  |
| **Site: UCSD (vs UAB)** | **+3.2917** | 0.5328 | ±1.0655 | **+6.179** | **6.47e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5195** | 0.5091 | ±1.0181 | **-2.985** | **0.0028** | ** |
| **Season: spring (vs autumn)** | **-1.1640** | 0.5652 | ±1.1303 | **-2.059** | **0.0394** | * |
| **Season: summer (vs autumn)** | **+2.0988** | 0.5882 | ±1.1764 | **+3.568** | **3.59e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1052** | 0.5920 | ±1.1840 | **-8.624** | **6.48e-18** | *** |
| Age (years) | -0.0359 | 0.0186 | ±0.0373 | -1.925 | 0.0542 | . |
| BMI (kg/m2) | -0.0558 | 0.0285 | ±0.0569 | -1.959 | 0.0501 | . |
| Hypertension | +0.2867 | 0.4528 | ±0.9057 | +0.633 | 0.5267 |  |
| **High cholesterol** | **-1.1433** | 0.4202 | ±0.8404 | **-2.721** | **0.0065** | ** |
| Kidney disease | +0.1648 | 0.7094 | ±1.4189 | +0.232 | 0.8164 |  |
| Circulatory disease | -0.5312 | 0.5924 | ±1.1849 | -0.897 | 0.3699 |  |
| Nocturnal time > 180 (%) | +0.0998 | 0.0578 | ±0.1155 | +1.729 | 0.0839 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 872; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **872**, R² = **0.0503**, Adj R² = **0.0359**, F-statistic = **3.49** (p = **2.49e-05**), Residual SE = **15.631** on **858** df, AIC = **7283.3**, BIC = **7350.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5289** | 4.4723 | ±8.9447 | **+28.515** | **7.62e-179** | *** |
| **Education: graduate level (vs college)** | **-2.7893** | 1.1194 | ±2.2388 | **-2.492** | **0.0127** | * |
| **Education: high school or below (vs college)** | **+4.8557** | 2.1167 | ±4.2333 | **+2.294** | **0.0218** | * |
| Site: UCSD (vs UAB) | +1.3405 | 1.4016 | ±2.8032 | +0.956 | 0.3389 |  |
| Site: UW (vs UAB) | +0.2180 | 1.3842 | ±2.7684 | +0.158 | 0.8748 |  |
| Season: spring (vs autumn) | +2.5402 | 1.5130 | ±3.0260 | +1.679 | 0.0932 | . |
| Season: summer (vs autumn) | +2.1912 | 1.6545 | ±3.3091 | +1.324 | 0.1854 |  |
| **Season: winter (vs autumn)** | **+4.2175** | 1.6004 | ±3.2007 | **+2.635** | **0.0084** | ** |
| **Age (years)** | **-0.1289** | 0.0548 | ±0.1095 | **-2.354** | **0.0186** | * |
| **BMI (kg/m2)** | **+0.1583** | 0.0726 | ±0.1452 | **+2.180** | **0.0292** | * |
| Hypertension | +0.7867 | 1.2164 | ±2.4327 | +0.647 | 0.5178 |  |
| High cholesterol | -0.2576 | 1.1229 | ±2.2458 | -0.229 | 0.8186 |  |
| Kidney disease | -2.1917 | 1.6929 | ±3.3857 | -1.295 | 0.1954 |  |
| Circulatory disease | +0.5383 | 1.6596 | ±3.3193 | +0.324 | 0.7457 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **872**, R² = **0.0505**, Adj R² = **0.0349**, F-statistic = **3.25** (p = **4.59e-05**), Residual SE = **15.639** on **857** df, AIC = **7285.1**, BIC = **7356.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.3721** | 8.9717 | ±17.9433 | **+14.532** | **7.65e-48** | *** |
| **Education: graduate level (vs college)** | **-2.7873** | 1.1209 | ±2.2419 | **-2.487** | **0.0129** | * |
| **Education: high school or below (vs college)** | **+4.8951** | 2.1310 | ±4.2619 | **+2.297** | **0.0216** | * |
| Site: UCSD (vs UAB) | +1.3361 | 1.4027 | ±2.8054 | +0.953 | 0.3408 |  |
| Site: UW (vs UAB) | +0.2132 | 1.3847 | ±2.7695 | +0.154 | 0.8776 |  |
| Season: spring (vs autumn) | +2.4808 | 1.4957 | ±2.9913 | +1.659 | 0.0972 | . |
| Season: summer (vs autumn) | +2.2049 | 1.6688 | ±3.3376 | +1.321 | 0.1864 |  |
| **Season: winter (vs autumn)** | **+4.1816** | 1.5880 | ±3.1759 | **+2.633** | **0.0085** | ** |
| **Age (years)** | **-0.1279** | 0.0550 | ±0.1100 | **-2.324** | **0.0201** | * |
| **BMI (kg/m2)** | **+0.1643** | 0.0727 | ±0.1453 | **+2.262** | **0.0237** | * |
| Hypertension | +0.8497 | 1.2327 | ±2.4653 | +0.689 | 0.4906 |  |
| High cholesterol | -0.1926 | 1.1403 | ±2.2807 | -0.169 | 0.8659 |  |
| Kidney disease | -2.1934 | 1.6977 | ±3.3954 | -1.292 | 0.1964 |  |
| Circulatory disease | +0.5707 | 1.6708 | ±3.3415 | +0.342 | 0.7327 |  |
| HbA1c (%) | -0.5504 | 1.5713 | ±3.1426 | -0.350 | 0.7261 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **872**, R² = **0.0526**, Adj R² = **0.0371**, F-statistic = **3.40** (p = **2.23e-05**), Residual SE = **15.622** on **857** df, AIC = **7283.2**, BIC = **7354.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+134.8108** | 6.5741 | ±13.1481 | **+20.506** | **1.88e-93** | *** |
| **Education: graduate level (vs college)** | **-2.7145** | 1.1225 | ±2.2450 | **-2.418** | **0.0156** | * |
| **Education: high school or below (vs college)** | **+4.9154** | 2.1259 | ±4.2518 | **+2.312** | **0.0208** | * |
| Site: UCSD (vs UAB) | +1.2460 | 1.4025 | ±2.8051 | +0.888 | 0.3743 |  |
| Site: UW (vs UAB) | +0.2684 | 1.3825 | ±2.7651 | +0.194 | 0.8461 |  |
| Season: spring (vs autumn) | +2.5332 | 1.5134 | ±3.0268 | +1.674 | 0.0942 | . |
| Season: summer (vs autumn) | +2.2726 | 1.6709 | ±3.3417 | +1.360 | 0.1738 |  |
| **Season: winter (vs autumn)** | **+4.1721** | 1.5986 | ±3.1972 | **+2.610** | **0.0091** | ** |
| **Age (years)** | **-0.1277** | 0.0549 | ±0.1097 | **-2.328** | **0.0199** | * |
| **BMI (kg/m2)** | **+0.1728** | 0.0726 | ±0.1451 | **+2.381** | **0.0173** | * |
| Hypertension | +0.9898 | 1.2068 | ±2.4137 | +0.820 | 0.4121 |  |
| High cholesterol | -0.2289 | 1.1233 | ±2.2466 | -0.204 | 0.8386 |  |
| Kidney disease | -2.0110 | 1.7067 | ±3.4134 | -1.178 | 0.2387 |  |
| Circulatory disease | +0.6690 | 1.6672 | ±3.3343 | +0.401 | 0.6882 |  |
| Mean glucose (mg/dL) | -0.0656 | 0.0475 | ±0.0950 | -1.381 | 0.1672 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **872**, R² = **0.0526**, Adj R² = **0.0371**, F-statistic = **3.40** (p = **2.23e-05**), Residual SE = **15.622** on **857** df, AIC = **7283.2**, BIC = **7354.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+143.8899** | 12.2558 | ±24.5115 | **+11.741** | **7.89e-32** | *** |
| **Education: graduate level (vs college)** | **-2.7145** | 1.1225 | ±2.2450 | **-2.418** | **0.0156** | * |
| **Education: high school or below (vs college)** | **+4.9154** | 2.1259 | ±4.2518 | **+2.312** | **0.0208** | * |
| Site: UCSD (vs UAB) | +1.2460 | 1.4025 | ±2.8051 | +0.888 | 0.3743 |  |
| Site: UW (vs UAB) | +0.2684 | 1.3825 | ±2.7651 | +0.194 | 0.8461 |  |
| Season: spring (vs autumn) | +2.5332 | 1.5134 | ±3.0268 | +1.674 | 0.0942 | . |
| Season: summer (vs autumn) | +2.2726 | 1.6709 | ±3.3417 | +1.360 | 0.1738 |  |
| **Season: winter (vs autumn)** | **+4.1721** | 1.5986 | ±3.1972 | **+2.610** | **0.0091** | ** |
| **Age (years)** | **-0.1277** | 0.0549 | ±0.1097 | **-2.328** | **0.0199** | * |
| **BMI (kg/m2)** | **+0.1728** | 0.0726 | ±0.1451 | **+2.381** | **0.0173** | * |
| Hypertension | +0.9898 | 1.2068 | ±2.4137 | +0.820 | 0.4121 |  |
| High cholesterol | -0.2289 | 1.1233 | ±2.2466 | -0.204 | 0.8386 |  |
| Kidney disease | -2.0110 | 1.7067 | ±3.4134 | -1.178 | 0.2387 |  |
| Circulatory disease | +0.6690 | 1.6672 | ±3.3343 | +0.401 | 0.6882 |  |
| GMI (%) | -2.7429 | 1.9858 | ±3.9715 | -1.381 | 0.1672 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **872**, R² = **0.0524**, Adj R² = **0.0369**, F-statistic = **3.38** (p = **2.41e-05**), Residual SE = **15.623** on **857** df, AIC = **7283.4**, BIC = **7354.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+133.6271** | 6.1107 | ±12.2214 | **+21.868** | **5.27e-106** | *** |
| **Education: graduate level (vs college)** | **-2.7362** | 1.1214 | ±2.2428 | **-2.440** | **0.0147** | * |
| **Education: high school or below (vs college)** | **+4.9053** | 2.1250 | ±4.2500 | **+2.308** | **0.0210** | * |
| Site: UCSD (vs UAB) | +1.3254 | 1.4014 | ±2.8028 | +0.946 | 0.3443 |  |
| Site: UW (vs UAB) | +0.2812 | 1.3809 | ±2.7618 | +0.204 | 0.8386 |  |
| Season: spring (vs autumn) | +2.5736 | 1.5173 | ±3.0347 | +1.696 | 0.0899 | . |
| Season: summer (vs autumn) | +2.2809 | 1.6717 | ±3.3435 | +1.364 | 0.1724 |  |
| **Season: winter (vs autumn)** | **+4.2185** | 1.6051 | ±3.2101 | **+2.628** | **0.0086** | ** |
| **Age (years)** | **-0.1332** | 0.0548 | ±0.1096 | **-2.431** | **0.0151** | * |
| **BMI (kg/m2)** | **+0.1819** | 0.0729 | ±0.1458 | **+2.496** | **0.0126** | * |
| Hypertension | +0.9150 | 1.2113 | ±2.4226 | +0.755 | 0.4500 |  |
| High cholesterol | -0.1745 | 1.1291 | ±2.2582 | -0.155 | 0.8772 |  |
| Kidney disease | -2.1304 | 1.7101 | ±3.4201 | -1.246 | 0.2128 |  |
| Circulatory disease | +0.6499 | 1.6629 | ±3.3259 | +0.391 | 0.6960 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0556 | 0.0403 | ±0.0806 | -1.380 | 0.1675 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **872**, R² = **0.0527**, Adj R² = **0.0372**, F-statistic = **3.40** (p = **2.17e-05**), Residual SE = **15.621** on **857** df, AIC = **7283.1**, BIC = **7354.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.8021** | 4.7186 | ±9.4372 | **+27.720** | **3.96e-169** | *** |
| **Education: graduate level (vs college)** | **-2.8152** | 1.1174 | ±2.2347 | **-2.519** | **0.0118** | * |
| **Education: high school or below (vs college)** | **+5.0589** | 2.1309 | ±4.2618 | **+2.374** | **0.0176** | * |
| Site: UCSD (vs UAB) | +1.1745 | 1.4113 | ±2.8226 | +0.832 | 0.4053 |  |
| Site: UW (vs UAB) | +0.1821 | 1.3794 | ±2.7588 | +0.132 | 0.8950 |  |
| Season: spring (vs autumn) | +2.5601 | 1.5192 | ±3.0385 | +1.685 | 0.0920 | . |
| Season: summer (vs autumn) | +2.2315 | 1.6626 | ±3.3253 | +1.342 | 0.1796 |  |
| **Season: winter (vs autumn)** | **+4.2571** | 1.6090 | ±3.2180 | **+2.646** | **0.0081** | ** |
| **Age (years)** | **-0.1242** | 0.0555 | ±0.1110 | **-2.237** | **0.0253** | * |
| **BMI (kg/m2)** | **+0.1648** | 0.0721 | ±0.1443 | **+2.285** | **0.0223** | * |
| Hypertension | +1.0207 | 1.2138 | ±2.4277 | +0.841 | 0.4004 |  |
| High cholesterol | -0.2153 | 1.1248 | ±2.2496 | -0.191 | 0.8482 |  |
| Kidney disease | -1.9709 | 1.6868 | ±3.3735 | -1.168 | 0.2426 |  |
| Circulatory disease | +0.6112 | 1.6609 | ±3.3217 | +0.368 | 0.7129 |  |
| Glucose SD, pooled (mg/dL) | -0.1948 | 0.1414 | ±0.2829 | -1.377 | 0.1684 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **872**, R² = **0.0525**, Adj R² = **0.0370**, F-statistic = **3.39** (p = **2.30e-05**), Residual SE = **15.622** on **857** df, AIC = **7283.2**, BIC = **7354.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.4316** | 4.5856 | ±9.1713 | **+28.443** | **5.87e-178** | *** |
| **Education: graduate level (vs college)** | **-2.7983** | 1.1179 | ±2.2358 | **-2.503** | **0.0123** | * |
| **Education: high school or below (vs college)** | **+5.0257** | 2.1294 | ±4.2587 | **+2.360** | **0.0183** | * |
| Site: UCSD (vs UAB) | +1.1914 | 1.4082 | ±2.8164 | +0.846 | 0.3975 |  |
| Site: UW (vs UAB) | +0.1999 | 1.3789 | ±2.7578 | +0.145 | 0.8847 |  |
| Season: spring (vs autumn) | +2.5193 | 1.5121 | ±3.0242 | +1.666 | 0.0957 | . |
| Season: summer (vs autumn) | +2.1832 | 1.6585 | ±3.3171 | +1.316 | 0.1881 |  |
| **Season: winter (vs autumn)** | **+4.2019** | 1.5993 | ±3.1987 | **+2.627** | **0.0086** | ** |
| **Age (years)** | **-0.1242** | 0.0556 | ±0.1113 | **-2.233** | **0.0256** | * |
| **BMI (kg/m2)** | **+0.1653** | 0.0722 | ±0.1445 | **+2.288** | **0.0222** | * |
| Hypertension | +1.0174 | 1.2088 | ±2.4176 | +0.842 | 0.4000 |  |
| High cholesterol | -0.2306 | 1.1241 | ±2.2482 | -0.205 | 0.8375 |  |
| Kidney disease | -1.9940 | 1.6872 | ±3.3744 | -1.182 | 0.2373 |  |
| Circulatory disease | +0.5737 | 1.6593 | ±3.3186 | +0.346 | 0.7295 |  |
| Avg. daily SD (mg/dL) | -0.1903 | 0.1422 | ±0.2844 | -1.338 | 0.1808 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **872**, R² = **0.0511**, Adj R² = **0.0356**, F-statistic = **3.30** (p = **3.66e-05**), Residual SE = **15.634** on **857** df, AIC = **7284.5**, BIC = **7356.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.0393** | 4.9924 | ±9.9848 | **+26.048** | **1.43e-149** | *** |
| **Education: graduate level (vs college)** | **-2.8378** | 1.1184 | ±2.2368 | **-2.537** | **0.0112** | * |
| **Education: high school or below (vs college)** | **+4.9718** | 2.1213 | ±4.2425 | **+2.344** | **0.0191** | * |
| Site: UCSD (vs UAB) | +1.2554 | 1.4113 | ±2.8226 | +0.890 | 0.3737 |  |
| Site: UW (vs UAB) | +0.1789 | 1.3845 | ±2.7689 | +0.129 | 0.8972 |  |
| Season: spring (vs autumn) | +2.5581 | 1.5184 | ±3.0367 | +1.685 | 0.0920 | . |
| Season: summer (vs autumn) | +2.1972 | 1.6559 | ±3.3118 | +1.327 | 0.1845 |  |
| **Season: winter (vs autumn)** | **+4.2714** | 1.6109 | ±3.2217 | **+2.652** | **0.0080** | ** |
| **Age (years)** | **-0.1260** | 0.0554 | ±0.1108 | **-2.274** | **0.0230** | * |
| **BMI (kg/m2)** | **+0.1578** | 0.0725 | ±0.1449 | **+2.178** | **0.0294** | * |
| Hypertension | +0.8824 | 1.2198 | ±2.4397 | +0.723 | 0.4694 |  |
| High cholesterol | -0.2433 | 1.1247 | ±2.2494 | -0.216 | 0.8287 |  |
| Kidney disease | -2.0991 | 1.6835 | ±3.3670 | -1.247 | 0.2124 |  |
| Circulatory disease | +0.5402 | 1.6583 | ±3.3165 | +0.326 | 0.7446 |  |
| CV (%) | -0.1647 | 0.1877 | ±0.3753 | -0.877 | 0.3803 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **872**, R² = **0.0512**, Adj R² = **0.0357**, F-statistic = **3.30** (p = **3.63e-05**), Residual SE = **15.633** on **857** df, AIC = **7284.5**, BIC = **7356.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.7109** | 5.8516 | ±11.7033 | **+21.312** | **8.77e-101** | *** |
| **Education: graduate level (vs college)** | **-2.8462** | 1.1170 | ±2.2340 | **-2.548** | **0.0108** | * |
| **Education: high school or below (vs college)** | **+4.9649** | 2.1194 | ±4.2388 | **+2.343** | **0.0191** | * |
| Site: UCSD (vs UAB) | +1.2739 | 1.4075 | ±2.8151 | +0.905 | 0.3655 |  |
| Site: UW (vs UAB) | +0.1980 | 1.3828 | ±2.7657 | +0.143 | 0.8861 |  |
| Season: spring (vs autumn) | +2.5750 | 1.5226 | ±3.0453 | +1.691 | 0.0908 | . |
| Season: summer (vs autumn) | +2.1923 | 1.6550 | ±3.3100 | +1.325 | 0.1853 |  |
| **Season: winter (vs autumn)** | **+4.2764** | 1.6111 | ±3.2222 | **+2.654** | **0.0079** | ** |
| **Age (years)** | **-0.1262** | 0.0554 | ±0.1107 | **-2.280** | **0.0226** | * |
| **BMI (kg/m2)** | **+0.1583** | 0.0725 | ±0.1449 | **+2.184** | **0.0289** | * |
| Hypertension | +0.8815 | 1.2194 | ±2.4388 | +0.723 | 0.4697 |  |
| High cholesterol | -0.2479 | 1.1242 | ±2.2485 | -0.221 | 0.8255 |  |
| Kidney disease | -2.1008 | 1.6855 | ±3.3710 | -1.246 | 0.2126 |  |
| Circulatory disease | +0.5259 | 1.6591 | ±3.3181 | +0.317 | 0.7512 |  |
| Mean / SD ratio | +0.4158 | 0.4802 | ±0.9605 | +0.866 | 0.3866 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **872**, R² = **0.0509**, Adj R² = **0.0354**, F-statistic = **3.28** (p = **4.01e-05**), Residual SE = **15.636** on **857** df, AIC = **7284.7**, BIC = **7356.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3922** | 5.7783 | ±11.5565 | **+21.701** | **2.02e-104** | *** |
| **Education: graduate level (vs college)** | **-2.8293** | 1.1171 | ±2.2342 | **-2.533** | **0.0113** | * |
| **Education: high school or below (vs college)** | **+4.9288** | 2.1193 | ±4.2385 | **+2.326** | **0.0200** | * |
| Site: UCSD (vs UAB) | +1.2966 | 1.4042 | ±2.8084 | +0.923 | 0.3558 |  |
| Site: UW (vs UAB) | +0.2136 | 1.3830 | ±2.7659 | +0.154 | 0.8773 |  |
| Season: spring (vs autumn) | +2.5504 | 1.5182 | ±3.0364 | +1.680 | 0.0930 | . |
| Season: summer (vs autumn) | +2.1709 | 1.6549 | ±3.3097 | +1.312 | 0.1896 |  |
| **Season: winter (vs autumn)** | **+4.2337** | 1.6045 | ±3.2090 | **+2.639** | **0.0083** | ** |
| **Age (years)** | **-0.1264** | 0.0556 | ±0.1111 | **-2.275** | **0.0229** | * |
| **BMI (kg/m2)** | **+0.1597** | 0.0726 | ±0.1451 | **+2.201** | **0.0278** | * |
| Hypertension | +0.8575 | 1.2149 | ±2.4299 | +0.706 | 0.4803 |  |
| High cholesterol | -0.2568 | 1.1238 | ±2.2476 | -0.229 | 0.8192 |  |
| Kidney disease | -2.1195 | 1.6879 | ±3.3758 | -1.256 | 0.2092 |  |
| Circulatory disease | +0.5005 | 1.6596 | ±3.3191 | +0.302 | 0.7630 |  |
| Avg. daily mean/SD | +0.2705 | 0.3843 | ±0.7687 | +0.704 | 0.4816 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **872**, R² = **0.0504**, Adj R² = **0.0349**, F-statistic = **3.25** (p = **4.67e-05**), Residual SE = **15.639** on **857** df, AIC = **7285.1**, BIC = **7356.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.4902** | 5.3531 | ±10.7062 | **+23.629** | **1.93e-123** | *** |
| **Education: graduate level (vs college)** | **-2.7913** | 1.1208 | ±2.2416 | **-2.491** | **0.0128** | * |
| **Education: high school or below (vs college)** | **+4.8064** | 2.1407 | ±4.2813 | **+2.245** | **0.0247** | * |
| Site: UCSD (vs UAB) | +1.3559 | 1.4019 | ±2.8039 | +0.967 | 0.3335 |  |
| Site: UW (vs UAB) | +0.2306 | 1.3851 | ±2.7703 | +0.167 | 0.8678 |  |
| Season: spring (vs autumn) | +2.5371 | 1.5152 | ±3.0304 | +1.674 | 0.0940 | . |
| Season: summer (vs autumn) | +2.2049 | 1.6513 | ±3.3025 | +1.335 | 0.1818 |  |
| **Season: winter (vs autumn)** | **+4.2256** | 1.5992 | ±3.1985 | **+2.642** | **0.0082** | ** |
| **Age (years)** | **-0.1285** | 0.0548 | ±0.1096 | **-2.345** | **0.0190** | * |
| **BMI (kg/m2)** | **+0.1583** | 0.0729 | ±0.1457 | **+2.174** | **0.0297** | * |
| Hypertension | +0.7927 | 1.2190 | ±2.4381 | +0.650 | 0.5155 |  |
| High cholesterol | -0.2582 | 1.1243 | ±2.2487 | -0.230 | 0.8183 |  |
| Kidney disease | -2.2146 | 1.6967 | ±3.3934 | -1.305 | 0.1918 |  |
| Circulatory disease | +0.5550 | 1.6584 | ±3.3167 | +0.335 | 0.7379 |  |
| MAG (mg/dL/h) | +0.0278 | 0.0816 | ±0.1631 | +0.340 | 0.7336 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **872**, R² = **0.0514**, Adj R² = **0.0359**, F-statistic = **3.32** (p = **3.30e-05**), Residual SE = **15.631** on **857** df, AIC = **7284.2**, BIC = **7355.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.3348** | 4.8878 | ±9.7756 | **+26.665** | **1.19e-156** | *** |
| **Education: graduate level (vs college)** | **-2.7750** | 1.1200 | ±2.2400 | **-2.478** | **0.0132** | * |
| **Education: high school or below (vs college)** | **+4.9845** | 2.1302 | ±4.2605 | **+2.340** | **0.0193** | * |
| Site: UCSD (vs UAB) | +1.2527 | 1.4076 | ±2.8151 | +0.890 | 0.3735 |  |
| Site: UW (vs UAB) | +0.2090 | 1.3806 | ±2.7612 | +0.151 | 0.8796 |  |
| Season: spring (vs autumn) | +2.5489 | 1.5186 | ±3.0372 | +1.678 | 0.0933 | . |
| Season: summer (vs autumn) | +2.1610 | 1.6554 | ±3.3108 | +1.305 | 0.1918 |  |
| **Season: winter (vs autumn)** | **+4.2003** | 1.5997 | ±3.1993 | **+2.626** | **0.0086** | ** |
| **Age (years)** | **-0.1261** | 0.0555 | ±0.1110 | **-2.273** | **0.0231** | * |
| **BMI (kg/m2)** | **+0.1560** | 0.0725 | ±0.1451 | **+2.151** | **0.0315** | * |
| Hypertension | +0.8966 | 1.2137 | ±2.4274 | +0.739 | 0.4601 |  |
| High cholesterol | -0.2493 | 1.1236 | ±2.2472 | -0.222 | 0.8244 |  |
| Kidney disease | -2.0681 | 1.6873 | ±3.3746 | -1.226 | 0.2203 |  |
| Circulatory disease | +0.5686 | 1.6629 | ±3.3257 | +0.342 | 0.7324 |  |
| Avg. daily range (mg/dL) | -0.0325 | 0.0327 | ±0.0654 | -0.994 | 0.3203 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **872**, R² = **0.0503**, Adj R² = **0.0348**, F-statistic = **3.24** (p = **4.88e-05**), Residual SE = **15.641** on **857** df, AIC = **7285.3**, BIC = **7356.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5918** | 4.5834 | ±9.1669 | **+27.838** | **1.52e-170** | *** |
| **Education: graduate level (vs college)** | **-2.7891** | 1.1214 | ±2.2429 | **-2.487** | **0.0129** | * |
| **Education: high school or below (vs college)** | **+4.8633** | 2.1348 | ±4.2696 | **+2.278** | **0.0227** | * |
| Site: UCSD (vs UAB) | +1.3356 | 1.4099 | ±2.8199 | +0.947 | 0.3435 |  |
| Site: UW (vs UAB) | +0.2156 | 1.3852 | ±2.7703 | +0.156 | 0.8763 |  |
| Season: spring (vs autumn) | +2.5465 | 1.5428 | ±3.0856 | +1.651 | 0.0988 | . |
| Season: summer (vs autumn) | +2.2018 | 1.6975 | ±3.3950 | +1.297 | 0.1946 |  |
| **Season: winter (vs autumn)** | **+4.2226** | 1.6178 | ±3.2356 | **+2.610** | **0.0091** | ** |
| **Age (years)** | **-0.1290** | 0.0548 | ±0.1097 | **-2.352** | **0.0187** | * |
| **BMI (kg/m2)** | **+0.1588** | 0.0725 | ±0.1449 | **+2.191** | **0.0285** | * |
| Hypertension | +0.7870 | 1.2181 | ±2.4363 | +0.646 | 0.5182 |  |
| High cholesterol | -0.2521 | 1.1233 | ±2.2467 | -0.224 | 0.8224 |  |
| Kidney disease | -2.1886 | 1.6941 | ±3.3881 | -1.292 | 0.1964 |  |
| Circulatory disease | +0.5468 | 1.6840 | ±3.3681 | +0.325 | 0.7454 |  |
| SD of daily means (mg/dL) | -0.0138 | 0.2546 | ±0.5091 | -0.054 | 0.9568 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **872**, R² = **0.0507**, Adj R² = **0.0352**, F-statistic = **3.27** (p = **4.18e-05**), Residual SE = **15.637** on **857** df, AIC = **7284.8**, BIC = **7356.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+117.1786** | 20.6230 | ±41.2460 | **+5.682** | **1.33e-08** | *** |
| **Education: graduate level (vs college)** | **-2.7743** | 1.1230 | ±2.2460 | **-2.470** | **0.0135** | * |
| **Education: high school or below (vs college)** | **+4.9009** | 2.1349 | ±4.2697 | **+2.296** | **0.0217** | * |
| Site: UCSD (vs UAB) | +1.2762 | 1.4125 | ±2.8251 | +0.903 | 0.3663 |  |
| Site: UW (vs UAB) | +0.2054 | 1.3843 | ±2.7686 | +0.148 | 0.8820 |  |
| Season: spring (vs autumn) | +2.5256 | 1.5096 | ±3.0192 | +1.673 | 0.0943 | . |
| Season: summer (vs autumn) | +2.2130 | 1.6680 | ±3.3360 | +1.327 | 0.1846 |  |
| **Season: winter (vs autumn)** | **+4.2074** | 1.6001 | ±3.2001 | **+2.630** | **0.0085** | ** |
| **Age (years)** | **-0.1275** | 0.0554 | ±0.1107 | **-2.302** | **0.0213** | * |
| **BMI (kg/m2)** | **+0.1613** | 0.0727 | ±0.1453 | **+2.219** | **0.0265** | * |
| Hypertension | +0.8477 | 1.2135 | ±2.4270 | +0.699 | 0.4848 |  |
| High cholesterol | -0.2213 | 1.1286 | ±2.2572 | -0.196 | 0.8445 |  |
| Kidney disease | -2.0834 | 1.6990 | ±3.3980 | -1.226 | 0.2201 |  |
| Circulatory disease | +0.5992 | 1.6697 | ±3.3394 | +0.359 | 0.7197 |  |
| Time in range 70-180, pooled (%) | +0.1038 | 0.1931 | ±0.3861 | +0.538 | 0.5907 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **872**, R² = **0.0509**, Adj R² = **0.0354**, F-statistic = **3.28** (p = **3.96e-05**), Residual SE = **15.635** on **857** df, AIC = **7284.7**, BIC = **7356.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+115.2000** | 20.7892 | ±41.5784 | **+5.541** | **3.00e-08** | *** |
| **Education: graduate level (vs college)** | **-2.7735** | 1.1227 | ±2.2453 | **-2.470** | **0.0135** | * |
| **Education: high school or below (vs college)** | **+4.8968** | 2.1325 | ±4.2649 | **+2.296** | **0.0217** | * |
| Site: UCSD (vs UAB) | +1.2636 | 1.4128 | ±2.8257 | +0.894 | 0.3711 |  |
| Site: UW (vs UAB) | +0.2026 | 1.3840 | ±2.7680 | +0.146 | 0.8836 |  |
| Season: spring (vs autumn) | +2.5202 | 1.5089 | ±3.0177 | +1.670 | 0.0949 | . |
| Season: summer (vs autumn) | +2.2177 | 1.6678 | ±3.3356 | +1.330 | 0.1836 |  |
| **Season: winter (vs autumn)** | **+4.2032** | 1.5991 | ±3.1982 | **+2.628** | **0.0086** | ** |
| **Age (years)** | **-0.1274** | 0.0553 | ±0.1106 | **-2.303** | **0.0213** | * |
| **BMI (kg/m2)** | **+0.1619** | 0.0727 | ±0.1453 | **+2.228** | **0.0259** | * |
| Hypertension | +0.8587 | 1.2135 | ±2.4270 | +0.708 | 0.4792 |  |
| High cholesterol | -0.2144 | 1.1283 | ±2.2566 | -0.190 | 0.8493 |  |
| Kidney disease | -2.0592 | 1.6982 | ±3.3963 | -1.213 | 0.2253 |  |
| Circulatory disease | +0.6123 | 1.6697 | ±3.3393 | +0.367 | 0.7138 |  |
| Avg. daily time in range 70-180 (%) | +0.1237 | 0.1944 | ±0.3889 | +0.636 | 0.5248 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **872**, R² = **0.0504**, Adj R² = **0.0349**, F-statistic = **3.25** (p = **4.74e-05**), Residual SE = **15.640** on **857** df, AIC = **7285.2**, BIC = **7356.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.4518** | 4.4722 | ±8.9443 | **+28.499** | **1.21e-178** | *** |
| **Education: graduate level (vs college)** | **-2.7637** | 1.1231 | ±2.2462 | **-2.461** | **0.0139** | * |
| **Education: high school or below (vs college)** | **+4.8790** | 2.1193 | ±4.2387 | **+2.302** | **0.0213** | * |
| Site: UCSD (vs UAB) | +1.3317 | 1.4034 | ±2.8067 | +0.949 | 0.3427 |  |
| Site: UW (vs UAB) | +0.2245 | 1.3822 | ±2.7645 | +0.162 | 0.8710 |  |
| Season: spring (vs autumn) | +2.5409 | 1.5137 | ±3.0273 | +1.679 | 0.0932 | . |
| Season: summer (vs autumn) | +2.1801 | 1.6546 | ±3.3093 | +1.318 | 0.1876 |  |
| **Season: winter (vs autumn)** | **+4.2017** | 1.5948 | ±3.1896 | **+2.635** | **0.0084** | ** |
| **Age (years)** | **-0.1291** | 0.0548 | ±0.1097 | **-2.354** | **0.0186** | * |
| **BMI (kg/m2)** | **+0.1589** | 0.0726 | ±0.1453 | **+2.189** | **0.0286** | * |
| Hypertension | +0.7894 | 1.2165 | ±2.4331 | +0.649 | 0.5164 |  |
| High cholesterol | -0.2643 | 1.1249 | ±2.2499 | -0.235 | 0.8143 |  |
| Kidney disease | -2.1781 | 1.6955 | ±3.3910 | -1.285 | 0.1989 |  |
| Circulatory disease | +0.5497 | 1.6605 | ±3.3211 | +0.331 | 0.7406 |  |
| Time 54-69, pooled (%) | +0.3102 | 1.4124 | ±2.8248 | +0.220 | 0.8262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **872**, R² = **0.0503**, Adj R² = **0.0348**, F-statistic = **3.24** (p = **4.87e-05**), Residual SE = **15.640** on **857** df, AIC = **7285.3**, BIC = **7356.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5056** | 4.4740 | ±8.9480 | **+28.499** | **1.20e-178** | *** |
| **Education: graduate level (vs college)** | **-2.7801** | 1.1237 | ±2.2475 | **-2.474** | **0.0134** | * |
| **Education: high school or below (vs college)** | **+4.8643** | 2.1193 | ±4.2386 | **+2.295** | **0.0217** | * |
| Site: UCSD (vs UAB) | +1.3352 | 1.4036 | ±2.8071 | +0.951 | 0.3414 |  |
| Site: UW (vs UAB) | +0.2196 | 1.3834 | ±2.7667 | +0.159 | 0.8739 |  |
| Season: spring (vs autumn) | +2.5417 | 1.5147 | ±3.0295 | +1.678 | 0.0933 | . |
| Season: summer (vs autumn) | +2.1890 | 1.6547 | ±3.3094 | +1.323 | 0.1859 |  |
| **Season: winter (vs autumn)** | **+4.2113** | 1.5944 | ±3.1887 | **+2.641** | **0.0083** | ** |
| **Age (years)** | **-0.1290** | 0.0548 | ±0.1097 | **-2.353** | **0.0186** | * |
| **BMI (kg/m2)** | **+0.1585** | 0.0726 | ±0.1453 | **+2.183** | **0.0291** | * |
| Hypertension | +0.7876 | 1.2167 | ±2.4335 | +0.647 | 0.5174 |  |
| High cholesterol | -0.2596 | 1.1245 | ±2.2489 | -0.231 | 0.8174 |  |
| Kidney disease | -2.1873 | 1.6939 | ±3.3879 | -1.291 | 0.1966 |  |
| Circulatory disease | +0.5442 | 1.6603 | ±3.3205 | +0.328 | 0.7431 |  |
| Avg. daily time 54-69 (%) | +0.1034 | 1.3609 | ±2.7219 | +0.076 | 0.9394 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **872**, R² = **0.0504**, Adj R² = **0.0349**, F-statistic = **3.25** (p = **4.74e-05**), Residual SE = **15.640** on **857** df, AIC = **7285.2**, BIC = **7356.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.4518** | 4.4722 | ±8.9443 | **+28.499** | **1.21e-178** | *** |
| **Education: graduate level (vs college)** | **-2.7637** | 1.1231 | ±2.2462 | **-2.461** | **0.0139** | * |
| **Education: high school or below (vs college)** | **+4.8790** | 2.1193 | ±4.2387 | **+2.302** | **0.0213** | * |
| Site: UCSD (vs UAB) | +1.3317 | 1.4034 | ±2.8067 | +0.949 | 0.3427 |  |
| Site: UW (vs UAB) | +0.2245 | 1.3822 | ±2.7645 | +0.162 | 0.8710 |  |
| Season: spring (vs autumn) | +2.5409 | 1.5137 | ±3.0273 | +1.679 | 0.0932 | . |
| Season: summer (vs autumn) | +2.1801 | 1.6546 | ±3.3093 | +1.318 | 0.1876 |  |
| **Season: winter (vs autumn)** | **+4.2017** | 1.5948 | ±3.1896 | **+2.635** | **0.0084** | ** |
| **Age (years)** | **-0.1291** | 0.0548 | ±0.1097 | **-2.354** | **0.0186** | * |
| **BMI (kg/m2)** | **+0.1589** | 0.0726 | ±0.1453 | **+2.189** | **0.0286** | * |
| Hypertension | +0.7894 | 1.2165 | ±2.4331 | +0.649 | 0.5164 |  |
| High cholesterol | -0.2643 | 1.1249 | ±2.2499 | -0.235 | 0.8143 |  |
| Kidney disease | -2.1781 | 1.6955 | ±3.3910 | -1.285 | 0.1989 |  |
| Circulatory disease | +0.5497 | 1.6605 | ±3.3211 | +0.331 | 0.7406 |  |
| Time < 70 (%) | +0.3102 | 1.4124 | ±2.8248 | +0.220 | 0.8262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **872**, R² = **0.0503**, Adj R² = **0.0348**, F-statistic = **3.24** (p = **4.87e-05**), Residual SE = **15.640** on **857** df, AIC = **7285.3**, BIC = **7356.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5056** | 4.4740 | ±8.9480 | **+28.499** | **1.20e-178** | *** |
| **Education: graduate level (vs college)** | **-2.7801** | 1.1237 | ±2.2475 | **-2.474** | **0.0134** | * |
| **Education: high school or below (vs college)** | **+4.8643** | 2.1193 | ±4.2386 | **+2.295** | **0.0217** | * |
| Site: UCSD (vs UAB) | +1.3352 | 1.4036 | ±2.8071 | +0.951 | 0.3414 |  |
| Site: UW (vs UAB) | +0.2196 | 1.3834 | ±2.7667 | +0.159 | 0.8739 |  |
| Season: spring (vs autumn) | +2.5417 | 1.5147 | ±3.0295 | +1.678 | 0.0933 | . |
| Season: summer (vs autumn) | +2.1890 | 1.6547 | ±3.3094 | +1.323 | 0.1859 |  |
| **Season: winter (vs autumn)** | **+4.2113** | 1.5944 | ±3.1887 | **+2.641** | **0.0083** | ** |
| **Age (years)** | **-0.1290** | 0.0548 | ±0.1097 | **-2.353** | **0.0186** | * |
| **BMI (kg/m2)** | **+0.1585** | 0.0726 | ±0.1453 | **+2.183** | **0.0291** | * |
| Hypertension | +0.7876 | 1.2167 | ±2.4335 | +0.647 | 0.5174 |  |
| High cholesterol | -0.2596 | 1.1245 | ±2.2489 | -0.231 | 0.8174 |  |
| Kidney disease | -2.1873 | 1.6939 | ±3.3879 | -1.291 | 0.1966 |  |
| Circulatory disease | +0.5442 | 1.6603 | ±3.3205 | +0.328 | 0.7431 |  |
| Avg. daily time < 70 (%) | +0.1034 | 1.3609 | ±2.7219 | +0.076 | 0.9394 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **872**, R² = **0.0508**, Adj R² = **0.0353**, F-statistic = **3.28** (p = **4.11e-05**), Residual SE = **15.636** on **857** df, AIC = **7284.8**, BIC = **7356.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5374** | 4.4741 | ±8.9483 | **+28.505** | **1.00e-178** | *** |
| **Education: graduate level (vs college)** | **-2.7647** | 1.1246 | ±2.2492 | **-2.458** | **0.0140** | * |
| **Education: high school or below (vs college)** | **+4.9111** | 2.1369 | ±4.2739 | **+2.298** | **0.0216** | * |
| Site: UCSD (vs UAB) | +1.2701 | 1.4129 | ±2.8257 | +0.899 | 0.3687 |  |
| Site: UW (vs UAB) | +0.2071 | 1.3843 | ±2.7686 | +0.150 | 0.8811 |  |
| Season: spring (vs autumn) | +2.5251 | 1.5095 | ±3.0191 | +1.673 | 0.0944 | . |
| Season: summer (vs autumn) | +2.2102 | 1.6669 | ±3.3339 | +1.326 | 0.1849 |  |
| **Season: winter (vs autumn)** | **+4.2014** | 1.5976 | ±3.1952 | **+2.630** | **0.0085** | ** |
| **Age (years)** | **-0.1275** | 0.0553 | ±0.1107 | **-2.304** | **0.0212** | * |
| **BMI (kg/m2)** | **+0.1616** | 0.0727 | ±0.1454 | **+2.224** | **0.0262** | * |
| Hypertension | +0.8515 | 1.2124 | ±2.4247 | +0.702 | 0.4825 |  |
| High cholesterol | -0.2220 | 1.1283 | ±2.2566 | -0.197 | 0.8440 |  |
| Kidney disease | -2.0736 | 1.7001 | ±3.4002 | -1.220 | 0.2226 |  |
| Circulatory disease | +0.6061 | 1.6701 | ±3.3403 | +0.363 | 0.7167 |  |
| Time 181-250, pooled (%) | -0.1087 | 0.1924 | ±0.3848 | -0.565 | 0.5723 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **872**, R² = **0.0509**, Adj R² = **0.0354**, F-statistic = **3.28** (p = **3.94e-05**), Residual SE = **15.635** on **857** df, AIC = **7284.7**, BIC = **7356.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5390** | 4.4715 | ±8.9431 | **+28.522** | **6.18e-179** | *** |
| **Education: graduate level (vs college)** | **-2.7624** | 1.1245 | ±2.2490 | **-2.457** | **0.0140** | * |
| **Education: high school or below (vs college)** | **+4.9072** | 2.1346 | ±4.2692 | **+2.299** | **0.0215** | * |
| Site: UCSD (vs UAB) | +1.2571 | 1.4136 | ±2.8272 | +0.889 | 0.3739 |  |
| Site: UW (vs UAB) | +0.2044 | 1.3841 | ±2.7682 | +0.148 | 0.8826 |  |
| Season: spring (vs autumn) | +2.5221 | 1.5093 | ±3.0186 | +1.671 | 0.0947 | . |
| Season: summer (vs autumn) | +2.2152 | 1.6673 | ±3.3345 | +1.329 | 0.1840 |  |
| **Season: winter (vs autumn)** | **+4.1958** | 1.5963 | ±3.1926 | **+2.628** | **0.0086** | ** |
| **Age (years)** | **-0.1275** | 0.0553 | ±0.1106 | **-2.307** | **0.0211** | * |
| **BMI (kg/m2)** | **+0.1622** | 0.0727 | ±0.1454 | **+2.232** | **0.0256** | * |
| Hypertension | +0.8600 | 1.2124 | ±2.4247 | +0.709 | 0.4781 |  |
| High cholesterol | -0.2168 | 1.1282 | ±2.2564 | -0.192 | 0.8476 |  |
| Kidney disease | -2.0536 | 1.6993 | ±3.3987 | -1.208 | 0.2269 |  |
| Circulatory disease | +0.6196 | 1.6703 | ±3.3405 | +0.371 | 0.7106 |  |
| Avg. daily time 181-250 (%) | -0.1240 | 0.1937 | ±0.3874 | -0.640 | 0.5220 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **872**, R² = **0.0508**, Adj R² = **0.0353**, F-statistic = **3.28** (p = **4.11e-05**), Residual SE = **15.636** on **857** df, AIC = **7284.8**, BIC = **7356.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5374** | 4.4741 | ±8.9483 | **+28.505** | **1.00e-178** | *** |
| **Education: graduate level (vs college)** | **-2.7647** | 1.1246 | ±2.2492 | **-2.458** | **0.0140** | * |
| **Education: high school or below (vs college)** | **+4.9111** | 2.1369 | ±4.2739 | **+2.298** | **0.0216** | * |
| Site: UCSD (vs UAB) | +1.2701 | 1.4129 | ±2.8257 | +0.899 | 0.3687 |  |
| Site: UW (vs UAB) | +0.2071 | 1.3843 | ±2.7686 | +0.150 | 0.8811 |  |
| Season: spring (vs autumn) | +2.5251 | 1.5095 | ±3.0191 | +1.673 | 0.0944 | . |
| Season: summer (vs autumn) | +2.2102 | 1.6669 | ±3.3339 | +1.326 | 0.1849 |  |
| **Season: winter (vs autumn)** | **+4.2014** | 1.5976 | ±3.1952 | **+2.630** | **0.0085** | ** |
| **Age (years)** | **-0.1275** | 0.0553 | ±0.1107 | **-2.304** | **0.0212** | * |
| **BMI (kg/m2)** | **+0.1616** | 0.0727 | ±0.1454 | **+2.224** | **0.0262** | * |
| Hypertension | +0.8515 | 1.2124 | ±2.4247 | +0.702 | 0.4825 |  |
| High cholesterol | -0.2220 | 1.1283 | ±2.2566 | -0.197 | 0.8440 |  |
| Kidney disease | -2.0736 | 1.7001 | ±3.4002 | -1.220 | 0.2226 |  |
| Circulatory disease | +0.6061 | 1.6701 | ±3.3403 | +0.363 | 0.7167 |  |
| Time > 180 (%) | -0.1087 | 0.1924 | ±0.3848 | -0.565 | 0.5723 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **872**, R² = **0.0509**, Adj R² = **0.0354**, F-statistic = **3.28** (p = **3.94e-05**), Residual SE = **15.635** on **857** df, AIC = **7284.7**, BIC = **7356.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5390** | 4.4715 | ±8.9431 | **+28.522** | **6.18e-179** | *** |
| **Education: graduate level (vs college)** | **-2.7624** | 1.1245 | ±2.2490 | **-2.457** | **0.0140** | * |
| **Education: high school or below (vs college)** | **+4.9072** | 2.1346 | ±4.2692 | **+2.299** | **0.0215** | * |
| Site: UCSD (vs UAB) | +1.2571 | 1.4136 | ±2.8272 | +0.889 | 0.3739 |  |
| Site: UW (vs UAB) | +0.2044 | 1.3841 | ±2.7682 | +0.148 | 0.8826 |  |
| Season: spring (vs autumn) | +2.5221 | 1.5093 | ±3.0186 | +1.671 | 0.0947 | . |
| Season: summer (vs autumn) | +2.2152 | 1.6673 | ±3.3345 | +1.329 | 0.1840 |  |
| **Season: winter (vs autumn)** | **+4.1958** | 1.5963 | ±3.1926 | **+2.628** | **0.0086** | ** |
| **Age (years)** | **-0.1275** | 0.0553 | ±0.1106 | **-2.307** | **0.0211** | * |
| **BMI (kg/m2)** | **+0.1622** | 0.0727 | ±0.1454 | **+2.232** | **0.0256** | * |
| Hypertension | +0.8600 | 1.2124 | ±2.4247 | +0.709 | 0.4781 |  |
| High cholesterol | -0.2168 | 1.1282 | ±2.2564 | -0.192 | 0.8476 |  |
| Kidney disease | -2.0536 | 1.6993 | ±3.3987 | -1.208 | 0.2269 |  |
| Circulatory disease | +0.6196 | 1.6703 | ±3.3405 | +0.371 | 0.7106 |  |
| Avg. daily time > 180 (%) | -0.1240 | 0.1937 | ±0.3874 | -0.640 | 0.5220 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **872**, R² = **0.0522**, Adj R² = **0.0367**, F-statistic = **3.37** (p = **2.56e-05**), Residual SE = **15.625** on **857** df, AIC = **7283.5**, BIC = **7355.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.4156** | 4.4665 | ±8.9331 | **+28.527** | **5.47e-179** | *** |
| **Education: graduate level (vs college)** | **-2.7915** | 1.1167 | ±2.2334 | **-2.500** | **0.0124** | * |
| **Education: high school or below (vs college)** | **+5.0515** | 2.1502 | ±4.3005 | **+2.349** | **0.0188** | * |
| Site: UCSD (vs UAB) | +1.2138 | 1.4133 | ±2.8266 | +0.859 | 0.3904 |  |
| Site: UW (vs UAB) | +0.1722 | 1.3848 | ±2.7697 | +0.124 | 0.9010 |  |
| Season: spring (vs autumn) | +2.5708 | 1.5122 | ±3.0244 | +1.700 | 0.0891 | . |
| Season: summer (vs autumn) | +2.2738 | 1.6616 | ±3.3231 | +1.368 | 0.1712 |  |
| **Season: winter (vs autumn)** | **+4.2379** | 1.5992 | ±3.1984 | **+2.650** | **0.0080** | ** |
| **Age (years)** | **-0.1308** | 0.0546 | ±0.1092 | **-2.395** | **0.0166** | * |
| **BMI (kg/m2)** | **+0.1720** | 0.0730 | ±0.1459 | **+2.357** | **0.0184** | * |
| Hypertension | +0.7766 | 1.2177 | ±2.4353 | +0.638 | 0.5236 |  |
| High cholesterol | -0.1173 | 1.1388 | ±2.2775 | -0.103 | 0.9180 |  |
| Kidney disease | -2.0385 | 1.6993 | ±3.3987 | -1.200 | 0.2303 |  |
| Circulatory disease | +0.6246 | 1.6593 | ±3.3186 | +0.376 | 0.7066 |  |
| Nocturnal time > 180 (%) | -0.1923 | 0.1369 | ±0.2739 | -1.404 | 0.1602 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Total analysis base - Home environment

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 92 single-predictor tests; 7 with raw p < 0.05 (about 5 expected by chance); FDR rule applied to 92 tests (samples with n >= 500), of which **1** are significant at BH q < 0.05 in the all-tests family and 2 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 872): best single predictor out of sample is **SD of daily means** (CV R² 0.115 vs 0.115 for covariates alone, gain -0.000; +0.0339 per SD, p = 0.272, q = 0.604). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor temperature, mean (deg C)** (n = 872): best single predictor out of sample is **SD of daily means** (CV R² 0.301 vs 0.301 for covariates alone, gain -0.000; -0.0598 per SD, p = 0.404, q = 0.731). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 872): best single predictor out of sample is **SD (pooled)** (CV R² 0.242 vs 0.236 for covariates alone, gain +0.006; +0.587 per SD, p = 0.003, q = 0.048). FDR-robust associations (1): SD (pooled) (higher outcome, +0.587 per SD, q = 0.048).
- **Indoor VOC index, mean** (n = 872): best single predictor out of sample is **SD (pooled)** (CV R² 0.016 vs 0.015 for covariates alone, gain +0.002; -0.805 per SD, p = 0.168, q = 0.484). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.

**Most predictable outcomes (largest out-of-sample gain over covariates):** Indoor relative humidity, mean (%) (+0.006, via SD (pooled)); Indoor VOC index, mean (+0.002, via SD (pooled)); Indoor temperature, mean (deg C) (-0.000, via SD of daily means); Indoor PM2.5, log(1 + mean ug/m3) (-0.000, via SD of daily means). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (1 FDR-significant / 4 raw-significant of 32); Range 70-180 (0 FDR-significant / 1 raw-significant of 8); Band 181-250 (0 FDR-significant / 1 raw-significant of 8).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 1 FDR-significant (4 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Indoor relative humidity, mean (SD (pooled), ΔAIC -7.8); Indoor VOC index, mean (SD (pooled), ΔAIC -2.0).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
