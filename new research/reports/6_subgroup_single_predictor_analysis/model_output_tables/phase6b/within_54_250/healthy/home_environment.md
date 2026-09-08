# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Home environment

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 674; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **674**, R² = **0.1475**, Adj R² = **0.1307**, F-statistic = **8.78** (p = **1.04e-16**), Residual SE = **0.824** on **660** df, AIC = **1665.0**, BIC = **1728.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9414** | 0.2293 | ±0.4585 | **+8.468** | **2.50e-17** | *** |
| Education: graduate level (vs college) | +0.0307 | 0.0685 | ±0.1370 | +0.448 | 0.6538 |  |
| **Education: high school or below (vs college)** | **+0.5081** | 0.1407 | ±0.2813 | **+3.612** | **3.04e-04** | *** |
| Site: UCSD (vs UAB) | -0.0224 | 0.0825 | ±0.1651 | -0.271 | 0.7865 |  |
| **Site: UW (vs UAB)** | **-0.3590** | 0.0901 | ±0.1803 | **-3.982** | **6.84e-05** | *** |
| Season: spring (vs autumn) | -0.0462 | 0.0924 | ±0.1849 | -0.500 | 0.6173 |  |
| Season: summer (vs autumn) | +0.0741 | 0.0955 | ±0.1910 | +0.776 | 0.4378 |  |
| Season: winter (vs autumn) | -0.0054 | 0.0894 | ±0.1787 | -0.060 | 0.9521 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.045** | **5.23e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0052 | ±0.0105 | **+4.401** | **1.08e-05** | *** |
| Hypertension | +0.0918 | 0.0751 | ±0.1503 | +1.222 | 0.2219 |  |
| High cholesterol | -0.0930 | 0.0627 | ±0.1255 | -1.482 | 0.1383 |  |
| Kidney disease | -0.0247 | 0.1074 | ±0.2147 | -0.230 | 0.8182 |  |
| **Circulatory disease** | **+0.3125** | 0.1232 | ±0.2464 | **+2.536** | **0.0112** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **674**, R² = **0.1484**, Adj R² = **0.1303**, F-statistic = **8.20** (p = **2.31e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.2**, BIC = **1733.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.5076** | 0.5972 | ±1.1945 | **+2.524** | **0.0116** | * |
| Education: graduate level (vs college) | +0.0297 | 0.0686 | ±0.1372 | +0.433 | 0.6651 |  |
| **Education: high school or below (vs college)** | **+0.5066** | 0.1405 | ±0.2810 | **+3.606** | **3.11e-04** | *** |
| Site: UCSD (vs UAB) | -0.0225 | 0.0829 | ±0.1658 | -0.271 | 0.7863 |  |
| **Site: UW (vs UAB)** | **-0.3605** | 0.0901 | ±0.1802 | **-4.000** | **6.32e-05** | *** |
| Season: spring (vs autumn) | -0.0340 | 0.0929 | ±0.1859 | -0.366 | 0.7142 |  |
| Season: summer (vs autumn) | +0.0761 | 0.0958 | ±0.1916 | +0.794 | 0.4270 |  |
| Season: winter (vs autumn) | +0.0017 | 0.0900 | ±0.1801 | +0.018 | 0.9853 |  |
| **Age (years)** | **-0.0122** | 0.0030 | ±0.0059 | **-4.113** | **3.90e-05** | *** |
| **BMI (kg/m2)** | **+0.0225** | 0.0052 | ±0.0104 | **+4.329** | **1.50e-05** | *** |
| Hypertension | +0.0872 | 0.0759 | ±0.1518 | +1.148 | 0.2509 |  |
| High cholesterol | -0.0993 | 0.0634 | ±0.1267 | -1.568 | 0.1170 |  |
| Kidney disease | -0.0258 | 0.1082 | ±0.2164 | -0.238 | 0.8117 |  |
| **Circulatory disease** | **+0.3165** | 0.1233 | ±0.2465 | **+2.567** | **0.0103** | * |
| HbA1c (%) | +0.0840 | 0.1026 | ±0.2052 | +0.818 | 0.4133 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **674**, R² = **0.1490**, Adj R² = **0.1309**, F-statistic = **8.24** (p = **1.88e-16**), Residual SE = **0.823** on **659** df, AIC = **1665.8**, BIC = **1733.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2834** | 0.3851 | ±0.7703 | **+5.929** | **3.05e-09** | *** |
| Education: graduate level (vs college) | +0.0357 | 0.0687 | ±0.1374 | +0.519 | 0.6037 |  |
| **Education: high school or below (vs college)** | **+0.5133** | 0.1407 | ±0.2813 | **+3.649** | **2.63e-04** | *** |
| Site: UCSD (vs UAB) | -0.0271 | 0.0827 | ±0.1654 | -0.328 | 0.7430 |  |
| **Site: UW (vs UAB)** | **-0.3534** | 0.0899 | ±0.1798 | **-3.932** | **8.43e-05** | *** |
| Season: spring (vs autumn) | -0.0479 | 0.0927 | ±0.1853 | -0.517 | 0.6049 |  |
| Season: summer (vs autumn) | +0.0749 | 0.0953 | ±0.1907 | +0.786 | 0.4322 |  |
| Season: winter (vs autumn) | -0.0088 | 0.0889 | ±0.1779 | -0.099 | 0.9208 |  |
| **Age (years)** | **-0.0117** | 0.0030 | ±0.0059 | **-3.981** | **6.85e-05** | *** |
| **BMI (kg/m2)** | **+0.0237** | 0.0053 | ±0.0105 | **+4.494** | **6.99e-06** | *** |
| Hypertension | +0.0968 | 0.0756 | ±0.1512 | +1.280 | 0.2005 |  |
| High cholesterol | -0.0930 | 0.0628 | ±0.1256 | -1.481 | 0.1386 |  |
| Kidney disease | -0.0183 | 0.1069 | ±0.2137 | -0.171 | 0.8642 |  |
| **Circulatory disease** | **+0.3188** | 0.1233 | ±0.2467 | **+2.584** | **0.0098** | ** |
| Mean glucose (mg/dL) | -0.0031 | 0.0029 | ±0.0057 | -1.096 | 0.2730 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **674**, R² = **0.1490**, Adj R² = **0.1309**, F-statistic = **8.24** (p = **1.88e-16**), Residual SE = **0.823** on **659** df, AIC = **1665.8**, BIC = **1733.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.7166** | 0.7410 | ±1.4819 | **+3.666** | **2.46e-04** | *** |
| Education: graduate level (vs college) | +0.0357 | 0.0687 | ±0.1374 | +0.519 | 0.6037 |  |
| **Education: high school or below (vs college)** | **+0.5133** | 0.1407 | ±0.2813 | **+3.649** | **2.63e-04** | *** |
| Site: UCSD (vs UAB) | -0.0271 | 0.0827 | ±0.1654 | -0.328 | 0.7430 |  |
| **Site: UW (vs UAB)** | **-0.3534** | 0.0899 | ±0.1798 | **-3.932** | **8.43e-05** | *** |
| Season: spring (vs autumn) | -0.0479 | 0.0927 | ±0.1853 | -0.517 | 0.6049 |  |
| Season: summer (vs autumn) | +0.0749 | 0.0953 | ±0.1907 | +0.786 | 0.4322 |  |
| Season: winter (vs autumn) | -0.0088 | 0.0889 | ±0.1779 | -0.099 | 0.9208 |  |
| **Age (years)** | **-0.0117** | 0.0030 | ±0.0059 | **-3.981** | **6.85e-05** | *** |
| **BMI (kg/m2)** | **+0.0237** | 0.0053 | ±0.0105 | **+4.494** | **6.99e-06** | *** |
| Hypertension | +0.0968 | 0.0756 | ±0.1512 | +1.280 | 0.2005 |  |
| High cholesterol | -0.0930 | 0.0628 | ±0.1256 | -1.481 | 0.1386 |  |
| Kidney disease | -0.0183 | 0.1069 | ±0.2137 | -0.171 | 0.8642 |  |
| **Circulatory disease** | **+0.3188** | 0.1233 | ±0.2467 | **+2.584** | **0.0098** | ** |
| GMI (%) | -0.1309 | 0.1194 | ±0.2388 | -1.096 | 0.2730 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **674**, R² = **0.1487**, Adj R² = **0.1306**, F-statistic = **8.22** (p = **2.08e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.0**, BIC = **1733.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2075** | 0.3543 | ±0.7086 | **+6.231** | **4.64e-10** | *** |
| Education: graduate level (vs college) | +0.0333 | 0.0686 | ±0.1372 | +0.486 | 0.6272 |  |
| **Education: high school or below (vs college)** | **+0.5117** | 0.1408 | ±0.2815 | **+3.635** | **2.78e-04** | *** |
| Site: UCSD (vs UAB) | -0.0230 | 0.0825 | ±0.1649 | -0.279 | 0.7802 |  |
| **Site: UW (vs UAB)** | **-0.3540** | 0.0899 | ±0.1798 | **-3.938** | **8.21e-05** | *** |
| Season: spring (vs autumn) | -0.0446 | 0.0926 | ±0.1851 | -0.482 | 0.6296 |  |
| Season: summer (vs autumn) | +0.0766 | 0.0956 | ±0.1912 | +0.802 | 0.4228 |  |
| Season: winter (vs autumn) | -0.0050 | 0.0894 | ±0.1788 | -0.055 | 0.9558 |  |
| **Age (years)** | **-0.0120** | 0.0029 | ±0.0059 | **-4.079** | **4.52e-05** | *** |
| **BMI (kg/m2)** | **+0.0241** | 0.0054 | ±0.0108 | **+4.478** | **7.52e-06** | *** |
| Hypertension | +0.0944 | 0.0753 | ±0.1506 | +1.254 | 0.2100 |  |
| High cholesterol | -0.0907 | 0.0627 | ±0.1254 | -1.448 | 0.1477 |  |
| Kidney disease | -0.0221 | 0.1071 | ±0.2142 | -0.207 | 0.8362 |  |
| **Circulatory disease** | **+0.3165** | 0.1234 | ±0.2468 | **+2.565** | **0.0103** | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0025 | 0.0026 | ±0.0052 | -0.968 | 0.3333 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **674**, R² = **0.1475**, Adj R² = **0.1294**, F-statistic = **8.14** (p = **3.16e-16**), Residual SE = **0.824** on **659** df, AIC = **1667.0**, BIC = **1734.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9352** | 0.2755 | ±0.5511 | **+7.023** | **2.17e-12** | *** |
| Education: graduate level (vs college) | +0.0308 | 0.0689 | ±0.1378 | +0.448 | 0.6545 |  |
| **Education: high school or below (vs college)** | **+0.5080** | 0.1405 | ±0.2810 | **+3.616** | **2.99e-04** | *** |
| Site: UCSD (vs UAB) | -0.0221 | 0.0832 | ±0.1665 | -0.266 | 0.7905 |  |
| **Site: UW (vs UAB)** | **-0.3591** | 0.0903 | ±0.1805 | **-3.979** | **6.93e-05** | *** |
| Season: spring (vs autumn) | -0.0462 | 0.0925 | ±0.1851 | -0.499 | 0.6176 |  |
| Season: summer (vs autumn) | +0.0741 | 0.0957 | ±0.1915 | +0.774 | 0.4392 |  |
| Season: winter (vs autumn) | -0.0055 | 0.0895 | ±0.1790 | -0.061 | 0.9514 |  |
| **Age (years)** | **-0.0119** | 0.0030 | ±0.0059 | **-4.037** | **5.41e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0052 | ±0.0105 | **+4.396** | **1.10e-05** | *** |
| Hypertension | +0.0916 | 0.0755 | ±0.1510 | +1.213 | 0.2252 |  |
| High cholesterol | -0.0930 | 0.0628 | ±0.1257 | -1.481 | 0.1387 |  |
| Kidney disease | -0.0249 | 0.1075 | ±0.2149 | -0.231 | 0.8171 |  |
| **Circulatory disease** | **+0.3125** | 0.1233 | ±0.2467 | **+2.534** | **0.0113** | * |
| Glucose SD, pooled (mg/dL) | +0.0004 | 0.0083 | ±0.0166 | +0.046 | 0.9630 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **674**, R² = **0.1475**, Adj R² = **0.1294**, F-statistic = **8.15** (p = **3.12e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.9**, BIC = **1734.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9643** | 0.2704 | ±0.5407 | **+7.265** | **3.72e-13** | *** |
| Education: graduate level (vs college) | +0.0305 | 0.0687 | ±0.1374 | +0.443 | 0.6576 |  |
| **Education: high school or below (vs college)** | **+0.5087** | 0.1405 | ±0.2810 | **+3.620** | **2.94e-04** | *** |
| Site: UCSD (vs UAB) | -0.0235 | 0.0833 | ±0.1666 | -0.282 | 0.7777 |  |
| **Site: UW (vs UAB)** | **-0.3583** | 0.0902 | ±0.1804 | **-3.972** | **7.12e-05** | *** |
| Season: spring (vs autumn) | -0.0464 | 0.0925 | ±0.1851 | -0.501 | 0.6163 |  |
| Season: summer (vs autumn) | +0.0740 | 0.0955 | ±0.1911 | +0.774 | 0.4387 |  |
| Season: winter (vs autumn) | -0.0055 | 0.0895 | ±0.1790 | -0.062 | 0.9509 |  |
| **Age (years)** | **-0.0118** | 0.0029 | ±0.0059 | **-4.026** | **5.68e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0052 | ±0.0105 | **+4.413** | **1.02e-05** | *** |
| Hypertension | +0.0924 | 0.0755 | ±0.1510 | +1.224 | 0.2210 |  |
| High cholesterol | -0.0929 | 0.0628 | ±0.1257 | -1.478 | 0.1394 |  |
| Kidney disease | -0.0237 | 0.1076 | ±0.2152 | -0.220 | 0.8255 |  |
| **Circulatory disease** | **+0.3124** | 0.1233 | ±0.2467 | **+2.533** | **0.0113** | * |
| Avg. daily SD (mg/dL) | -0.0016 | 0.0084 | ±0.0168 | -0.186 | 0.8524 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **674**, R² = **0.1479**, Adj R² = **0.1298**, F-statistic = **8.17** (p = **2.73e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.6**, BIC = **1734.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8407** | 0.3031 | ±0.6061 | **+6.074** | **1.25e-09** | *** |
| Education: graduate level (vs college) | +0.0340 | 0.0696 | ±0.1391 | +0.489 | 0.6246 |  |
| **Education: high school or below (vs college)** | **+0.5081** | 0.1405 | ±0.2811 | **+3.616** | **3.00e-04** | *** |
| Site: UCSD (vs UAB) | -0.0200 | 0.0831 | ±0.1662 | -0.240 | 0.8102 |  |
| **Site: UW (vs UAB)** | **-0.3599** | 0.0904 | ±0.1808 | **-3.982** | **6.83e-05** | *** |
| Season: spring (vs autumn) | -0.0469 | 0.0925 | ±0.1851 | -0.507 | 0.6123 |  |
| Season: summer (vs autumn) | +0.0734 | 0.0957 | ±0.1914 | +0.767 | 0.4430 |  |
| Season: winter (vs autumn) | -0.0080 | 0.0893 | ±0.1786 | -0.090 | 0.9284 |  |
| **Age (years)** | **-0.0120** | 0.0029 | ±0.0059 | **-4.087** | **4.37e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0053 | ±0.0105 | **+4.393** | **1.12e-05** | *** |
| Hypertension | +0.0903 | 0.0753 | ±0.1506 | +1.200 | 0.2302 |  |
| High cholesterol | -0.0935 | 0.0629 | ±0.1258 | -1.486 | 0.1373 |  |
| Kidney disease | -0.0256 | 0.1074 | ±0.2149 | -0.238 | 0.8119 |  |
| **Circulatory disease** | **+0.3146** | 0.1233 | ±0.2466 | **+2.551** | **0.0107** | * |
| CV (%) | +0.0067 | 0.0116 | ±0.0232 | +0.577 | 0.5640 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **674**, R² = **0.1477**, Adj R² = **0.1296**, F-statistic = **8.16** (p = **2.97e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.8**, BIC = **1734.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0142** | 0.2854 | ±0.5708 | **+7.057** | **1.70e-12** | *** |
| Education: graduate level (vs college) | +0.0330 | 0.0696 | ±0.1392 | +0.474 | 0.6357 |  |
| **Education: high school or below (vs college)** | **+0.5078** | 0.1405 | ±0.2810 | **+3.614** | **3.02e-04** | *** |
| Site: UCSD (vs UAB) | -0.0212 | 0.0830 | ±0.1660 | -0.255 | 0.7985 |  |
| **Site: UW (vs UAB)** | **-0.3599** | 0.0904 | ±0.1809 | **-3.980** | **6.89e-05** | *** |
| Season: spring (vs autumn) | -0.0472 | 0.0925 | ±0.1851 | -0.511 | 0.6097 |  |
| Season: summer (vs autumn) | +0.0739 | 0.0956 | ±0.1913 | +0.772 | 0.4399 |  |
| Season: winter (vs autumn) | -0.0072 | 0.0894 | ±0.1788 | -0.080 | 0.9359 |  |
| **Age (years)** | **-0.0120** | 0.0029 | ±0.0059 | **-4.062** | **4.86e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0053 | ±0.0105 | **+4.392** | **1.12e-05** | *** |
| Hypertension | +0.0907 | 0.0753 | ±0.1505 | +1.205 | 0.2280 |  |
| High cholesterol | -0.0931 | 0.0629 | ±0.1257 | -1.481 | 0.1386 |  |
| Kidney disease | -0.0253 | 0.1074 | ±0.2149 | -0.235 | 0.8140 |  |
| **Circulatory disease** | **+0.3139** | 0.1233 | ±0.2467 | **+2.545** | **0.0109** | * |
| Mean / SD ratio | -0.0107 | 0.0280 | ±0.0560 | -0.382 | 0.7026 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **674**, R² = **0.1475**, Adj R² = **0.1294**, F-statistic = **8.15** (p = **3.13e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.9**, BIC = **1734.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9699** | 0.2788 | ±0.5576 | **+7.066** | **1.60e-12** | *** |
| Education: graduate level (vs college) | +0.0315 | 0.0693 | ±0.1385 | +0.454 | 0.6498 |  |
| **Education: high school or below (vs college)** | **+0.5079** | 0.1406 | ±0.2813 | **+3.612** | **3.04e-04** | *** |
| Site: UCSD (vs UAB) | -0.0218 | 0.0831 | ±0.1662 | -0.262 | 0.7932 |  |
| **Site: UW (vs UAB)** | **-0.3594** | 0.0904 | ±0.1807 | **-3.977** | **6.98e-05** | *** |
| Season: spring (vs autumn) | -0.0464 | 0.0925 | ±0.1851 | -0.502 | 0.6159 |  |
| Season: summer (vs autumn) | +0.0743 | 0.0956 | ±0.1912 | +0.777 | 0.4374 |  |
| Season: winter (vs autumn) | -0.0057 | 0.0894 | ±0.1788 | -0.064 | 0.9493 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.047** | **5.18e-05** | *** |
| **BMI (kg/m2)** | **+0.0230** | 0.0052 | ±0.0105 | **+4.395** | **1.11e-05** | *** |
| Hypertension | +0.0916 | 0.0753 | ±0.1505 | +1.217 | 0.2236 |  |
| High cholesterol | -0.0929 | 0.0628 | ±0.1257 | -1.479 | 0.1392 |  |
| Kidney disease | -0.0251 | 0.1078 | ±0.2155 | -0.233 | 0.8157 |  |
| **Circulatory disease** | **+0.3131** | 0.1233 | ±0.2466 | **+2.539** | **0.0111** | * |
| Avg. daily mean/SD | -0.0036 | 0.0227 | ±0.0454 | -0.157 | 0.8751 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **674**, R² = **0.1483**, Adj R² = **0.1302**, F-statistic = **8.20** (p = **2.40e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.3**, BIC = **1734.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8015** | 0.2953 | ±0.5906 | **+6.101** | **1.05e-09** | *** |
| Education: graduate level (vs college) | +0.0306 | 0.0685 | ±0.1370 | +0.447 | 0.6551 |  |
| **Education: high school or below (vs college)** | **+0.5017** | 0.1428 | ±0.2857 | **+3.512** | **4.45e-04** | *** |
| Site: UCSD (vs UAB) | -0.0200 | 0.0832 | ±0.1663 | -0.240 | 0.8103 |  |
| **Site: UW (vs UAB)** | **-0.3580** | 0.0907 | ±0.1813 | **-3.948** | **7.87e-05** | *** |
| Season: spring (vs autumn) | -0.0470 | 0.0923 | ±0.1845 | -0.510 | 0.6102 |  |
| Season: summer (vs autumn) | +0.0765 | 0.0957 | ±0.1914 | +0.799 | 0.4241 |  |
| Season: winter (vs autumn) | -0.0043 | 0.0893 | ±0.1786 | -0.048 | 0.9614 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.033** | **5.50e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0053 | ±0.0105 | **+4.399** | **1.09e-05** | *** |
| Hypertension | +0.0941 | 0.0759 | ±0.1519 | +1.239 | 0.2154 |  |
| High cholesterol | -0.0924 | 0.0629 | ±0.1258 | -1.469 | 0.1419 |  |
| Kidney disease | -0.0286 | 0.1072 | ±0.2145 | -0.266 | 0.7900 |  |
| **Circulatory disease** | **+0.3138** | 0.1232 | ±0.2464 | **+2.547** | **0.0109** | * |
| MAG (mg/dL/h) | +0.0037 | 0.0050 | ±0.0100 | +0.750 | 0.4533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **674**, R² = **0.1479**, Adj R² = **0.1298**, F-statistic = **8.17** (p = **2.77e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.7**, BIC = **1734.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0323** | 0.2897 | ±0.5794 | **+7.015** | **2.29e-12** | *** |
| Education: graduate level (vs college) | +0.0312 | 0.0685 | ±0.1370 | +0.455 | 0.6491 |  |
| **Education: high school or below (vs college)** | **+0.5109** | 0.1404 | ±0.2808 | **+3.639** | **2.73e-04** | *** |
| Site: UCSD (vs UAB) | -0.0247 | 0.0828 | ±0.1656 | -0.298 | 0.7658 |  |
| **Site: UW (vs UAB)** | **-0.3570** | 0.0902 | ±0.1804 | **-3.959** | **7.52e-05** | *** |
| Season: spring (vs autumn) | -0.0458 | 0.0926 | ±0.1851 | -0.494 | 0.6210 |  |
| Season: summer (vs autumn) | +0.0731 | 0.0953 | ±0.1907 | +0.766 | 0.4435 |  |
| Season: winter (vs autumn) | -0.0057 | 0.0896 | ±0.1791 | -0.063 | 0.9496 |  |
| **Age (years)** | **-0.0118** | 0.0029 | ±0.0059 | **-4.013** | **6.00e-05** | *** |
| **BMI (kg/m2)** | **+0.0230** | 0.0052 | ±0.0105 | **+4.387** | **1.15e-05** | *** |
| Hypertension | +0.0925 | 0.0753 | ±0.1505 | +1.229 | 0.2190 |  |
| High cholesterol | -0.0933 | 0.0628 | ±0.1256 | -1.487 | 0.1371 |  |
| Kidney disease | -0.0215 | 0.1075 | ±0.2150 | -0.200 | 0.8411 |  |
| **Circulatory disease** | **+0.3133** | 0.1233 | ±0.2466 | **+2.541** | **0.0111** | * |
| Avg. daily range (mg/dL) | -0.0011 | 0.0019 | ±0.0037 | -0.582 | 0.5607 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **674**, R² = **0.1480**, Adj R² = **0.1299**, F-statistic = **8.18** (p = **2.66e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.6**, BIC = **1734.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9031** | 0.2345 | ±0.4691 | **+8.114** | **4.89e-16** | *** |
| Education: graduate level (vs college) | +0.0311 | 0.0686 | ±0.1371 | +0.454 | 0.6497 |  |
| **Education: high school or below (vs college)** | **+0.5072** | 0.1405 | ±0.2809 | **+3.611** | **3.05e-04** | *** |
| Site: UCSD (vs UAB) | -0.0216 | 0.0826 | ±0.1653 | -0.261 | 0.7941 |  |
| **Site: UW (vs UAB)** | **-0.3602** | 0.0903 | ±0.1807 | **-3.987** | **6.68e-05** | *** |
| Season: spring (vs autumn) | -0.0495 | 0.0922 | ±0.1844 | -0.537 | 0.5914 |  |
| Season: summer (vs autumn) | +0.0687 | 0.0967 | ±0.1934 | +0.710 | 0.4775 |  |
| Season: winter (vs autumn) | -0.0092 | 0.0905 | ±0.1810 | -0.102 | 0.9188 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.043** | **5.28e-05** | *** |
| **BMI (kg/m2)** | **+0.0228** | 0.0053 | ±0.0106 | **+4.278** | **1.89e-05** | *** |
| Hypertension | +0.0921 | 0.0753 | ±0.1505 | +1.224 | 0.2210 |  |
| High cholesterol | -0.0958 | 0.0627 | ±0.1254 | -1.528 | 0.1265 |  |
| Kidney disease | -0.0215 | 0.1072 | ±0.2143 | -0.200 | 0.8413 |  |
| **Circulatory disease** | **+0.3113** | 0.1230 | ±0.2461 | **+2.530** | **0.0114** | * |
| SD of daily means (mg/dL) | +0.0088 | 0.0148 | ±0.0296 | +0.597 | 0.5508 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **674**, R² = **0.1483**, Adj R² = **0.1302**, F-statistic = **8.19** (p = **2.44e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.4**, BIC = **1734.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0311 | 1.1315 | ±2.2630 | +0.911 | 0.3622 |  |
| Education: graduate level (vs college) | +0.0313 | 0.0685 | ±0.1370 | +0.457 | 0.6479 |  |
| **Education: high school or below (vs college)** | **+0.5081** | 0.1408 | ±0.2816 | **+3.608** | **3.09e-04** | *** |
| Site: UCSD (vs UAB) | -0.0266 | 0.0830 | ±0.1659 | -0.321 | 0.7481 |  |
| **Site: UW (vs UAB)** | **-0.3567** | 0.0900 | ±0.1800 | **-3.964** | **7.37e-05** | *** |
| Season: spring (vs autumn) | -0.0480 | 0.0924 | ±0.1848 | -0.520 | 0.6032 |  |
| Season: summer (vs autumn) | +0.0733 | 0.0955 | ±0.1909 | +0.767 | 0.4428 |  |
| Season: winter (vs autumn) | -0.0073 | 0.0893 | ±0.1786 | -0.082 | 0.9350 |  |
| **Age (years)** | **-0.0118** | 0.0029 | ±0.0059 | **-3.999** | **6.37e-05** | *** |
| **BMI (kg/m2)** | **+0.0232** | 0.0052 | ±0.0105 | **+4.431** | **9.38e-06** | *** |
| Hypertension | +0.0926 | 0.0752 | ±0.1504 | +1.232 | 0.2181 |  |
| High cholesterol | -0.0899 | 0.0625 | ±0.1249 | -1.439 | 0.1501 |  |
| Kidney disease | -0.0214 | 0.1069 | ±0.2138 | -0.200 | 0.8414 |  |
| **Circulatory disease** | **+0.3158** | 0.1235 | ±0.2469 | **+2.558** | **0.0105** | * |
| Time in range 70-180, pooled (%) | +0.0091 | 0.0112 | ±0.0224 | +0.815 | 0.4150 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **674**, R² = **0.1488**, Adj R² = **0.1307**, F-statistic = **8.23** (p = **2.04e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.0**, BIC = **1733.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.7361 | 1.1437 | ±2.2874 | +0.644 | 0.5198 |  |
| Education: graduate level (vs college) | +0.0315 | 0.0685 | ±0.1370 | +0.460 | 0.6452 |  |
| **Education: high school or below (vs college)** | **+0.5077** | 0.1407 | ±0.2815 | **+3.607** | **3.09e-04** | *** |
| Site: UCSD (vs UAB) | -0.0281 | 0.0829 | ±0.1658 | -0.338 | 0.7351 |  |
| **Site: UW (vs UAB)** | **-0.3565** | 0.0900 | ±0.1799 | **-3.963** | **7.41e-05** | *** |
| Season: spring (vs autumn) | -0.0485 | 0.0924 | ±0.1848 | -0.525 | 0.5992 |  |
| Season: summer (vs autumn) | +0.0731 | 0.0953 | ±0.1907 | +0.767 | 0.4433 |  |
| Season: winter (vs autumn) | -0.0083 | 0.0892 | ±0.1784 | -0.093 | 0.9262 |  |
| **Age (years)** | **-0.0117** | 0.0029 | ±0.0059 | **-3.994** | **6.49e-05** | *** |
| **BMI (kg/m2)** | **+0.0233** | 0.0052 | ±0.0105 | **+4.451** | **8.56e-06** | *** |
| Hypertension | +0.0925 | 0.0752 | ±0.1503 | +1.231 | 0.2185 |  |
| High cholesterol | -0.0889 | 0.0624 | ±0.1249 | -1.424 | 0.1545 |  |
| Kidney disease | -0.0199 | 0.1066 | ±0.2133 | -0.187 | 0.8520 |  |
| **Circulatory disease** | **+0.3175** | 0.1234 | ±0.2468 | **+2.572** | **0.0101** | * |
| Avg. daily time in range 70-180 (%) | +0.0121 | 0.0113 | ±0.0227 | +1.068 | 0.2856 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **674**, R² = **0.1476**, Adj R² = **0.1294**, F-statistic = **8.15** (p = **3.11e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.9**, BIC = **1734.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9379** | 0.2319 | ±0.4638 | **+8.356** | **6.48e-17** | *** |
| Education: graduate level (vs college) | +0.0320 | 0.0694 | ±0.1389 | +0.461 | 0.6445 |  |
| **Education: high school or below (vs college)** | **+0.5098** | 0.1412 | ±0.2824 | **+3.610** | **3.06e-04** | *** |
| Site: UCSD (vs UAB) | -0.0229 | 0.0825 | ±0.1649 | -0.277 | 0.7815 |  |
| **Site: UW (vs UAB)** | **-0.3586** | 0.0902 | ±0.1805 | **-3.974** | **7.08e-05** | *** |
| Season: spring (vs autumn) | -0.0464 | 0.0925 | ±0.1851 | -0.502 | 0.6159 |  |
| Season: summer (vs autumn) | +0.0735 | 0.0956 | ±0.1913 | +0.768 | 0.4423 |  |
| Season: winter (vs autumn) | -0.0063 | 0.0896 | ±0.1791 | -0.070 | 0.9439 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.037** | **5.41e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0052 | ±0.0105 | **+4.401** | **1.08e-05** | *** |
| Hypertension | +0.0916 | 0.0753 | ±0.1505 | +1.217 | 0.2237 |  |
| High cholesterol | -0.0933 | 0.0626 | ±0.1252 | -1.490 | 0.1363 |  |
| Kidney disease | -0.0242 | 0.1073 | ±0.2147 | -0.226 | 0.8216 |  |
| **Circulatory disease** | **+0.3132** | 0.1235 | ±0.2471 | **+2.535** | **0.0112** | * |
| Time 54-69, pooled (%) | +0.0114 | 0.0531 | ±0.1062 | +0.214 | 0.8306 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **674**, R² = **0.1476**, Adj R² = **0.1294**, F-statistic = **8.15** (p = **3.11e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.9**, BIC = **1734.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9381** | 0.2315 | ±0.4629 | **+8.374** | **5.59e-17** | *** |
| Education: graduate level (vs college) | +0.0322 | 0.0695 | ±0.1390 | +0.463 | 0.6436 |  |
| **Education: high school or below (vs college)** | **+0.5099** | 0.1413 | ±0.2825 | **+3.610** | **3.06e-04** | *** |
| Site: UCSD (vs UAB) | -0.0232 | 0.0824 | ±0.1649 | -0.281 | 0.7788 |  |
| **Site: UW (vs UAB)** | **-0.3587** | 0.0902 | ±0.1805 | **-3.975** | **7.04e-05** | *** |
| Season: spring (vs autumn) | -0.0463 | 0.0925 | ±0.1850 | -0.500 | 0.6169 |  |
| Season: summer (vs autumn) | +0.0736 | 0.0956 | ±0.1913 | +0.770 | 0.4415 |  |
| Season: winter (vs autumn) | -0.0064 | 0.0896 | ±0.1791 | -0.072 | 0.9427 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.041** | **5.32e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0052 | ±0.0105 | **+4.402** | **1.07e-05** | *** |
| Hypertension | +0.0916 | 0.0752 | ±0.1505 | +1.218 | 0.2233 |  |
| High cholesterol | -0.0932 | 0.0626 | ±0.1253 | -1.489 | 0.1366 |  |
| Kidney disease | -0.0243 | 0.1074 | ±0.2147 | -0.226 | 0.8209 |  |
| **Circulatory disease** | **+0.3134** | 0.1236 | ±0.2471 | **+2.536** | **0.0112** | * |
| Avg. daily time 54-69 (%) | +0.0115 | 0.0520 | ±0.1039 | +0.222 | 0.8245 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **674**, R² = **0.1476**, Adj R² = **0.1294**, F-statistic = **8.15** (p = **3.11e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.9**, BIC = **1734.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9379** | 0.2319 | ±0.4638 | **+8.356** | **6.48e-17** | *** |
| Education: graduate level (vs college) | +0.0320 | 0.0694 | ±0.1389 | +0.461 | 0.6445 |  |
| **Education: high school or below (vs college)** | **+0.5098** | 0.1412 | ±0.2824 | **+3.610** | **3.06e-04** | *** |
| Site: UCSD (vs UAB) | -0.0229 | 0.0825 | ±0.1649 | -0.277 | 0.7815 |  |
| **Site: UW (vs UAB)** | **-0.3586** | 0.0902 | ±0.1805 | **-3.974** | **7.08e-05** | *** |
| Season: spring (vs autumn) | -0.0464 | 0.0925 | ±0.1851 | -0.502 | 0.6159 |  |
| Season: summer (vs autumn) | +0.0735 | 0.0956 | ±0.1913 | +0.768 | 0.4423 |  |
| Season: winter (vs autumn) | -0.0063 | 0.0896 | ±0.1791 | -0.070 | 0.9439 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.037** | **5.41e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0052 | ±0.0105 | **+4.401** | **1.08e-05** | *** |
| Hypertension | +0.0916 | 0.0753 | ±0.1505 | +1.217 | 0.2237 |  |
| High cholesterol | -0.0933 | 0.0626 | ±0.1252 | -1.490 | 0.1363 |  |
| Kidney disease | -0.0242 | 0.1073 | ±0.2147 | -0.226 | 0.8216 |  |
| **Circulatory disease** | **+0.3132** | 0.1235 | ±0.2471 | **+2.535** | **0.0112** | * |
| Time < 70 (%) | +0.0114 | 0.0531 | ±0.1062 | +0.214 | 0.8306 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **674**, R² = **0.1476**, Adj R² = **0.1294**, F-statistic = **8.15** (p = **3.11e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.9**, BIC = **1734.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9381** | 0.2315 | ±0.4629 | **+8.374** | **5.59e-17** | *** |
| Education: graduate level (vs college) | +0.0322 | 0.0695 | ±0.1390 | +0.463 | 0.6436 |  |
| **Education: high school or below (vs college)** | **+0.5099** | 0.1413 | ±0.2825 | **+3.610** | **3.06e-04** | *** |
| Site: UCSD (vs UAB) | -0.0232 | 0.0824 | ±0.1649 | -0.281 | 0.7788 |  |
| **Site: UW (vs UAB)** | **-0.3587** | 0.0902 | ±0.1805 | **-3.975** | **7.04e-05** | *** |
| Season: spring (vs autumn) | -0.0463 | 0.0925 | ±0.1850 | -0.500 | 0.6169 |  |
| Season: summer (vs autumn) | +0.0736 | 0.0956 | ±0.1913 | +0.770 | 0.4415 |  |
| Season: winter (vs autumn) | -0.0064 | 0.0896 | ±0.1791 | -0.072 | 0.9427 |  |
| **Age (years)** | **-0.0119** | 0.0029 | ±0.0059 | **-4.041** | **5.32e-05** | *** |
| **BMI (kg/m2)** | **+0.0231** | 0.0052 | ±0.0105 | **+4.402** | **1.07e-05** | *** |
| Hypertension | +0.0916 | 0.0752 | ±0.1505 | +1.218 | 0.2233 |  |
| High cholesterol | -0.0932 | 0.0626 | ±0.1253 | -1.489 | 0.1366 |  |
| Kidney disease | -0.0243 | 0.1074 | ±0.2147 | -0.226 | 0.8209 |  |
| **Circulatory disease** | **+0.3134** | 0.1236 | ±0.2471 | **+2.536** | **0.0112** | * |
| Avg. daily time < 70 (%) | +0.0115 | 0.0520 | ±0.1039 | +0.222 | 0.8245 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **674**, R² = **0.1483**, Adj R² = **0.1302**, F-statistic = **8.20** (p = **2.38e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.3**, BIC = **1734.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9428** | 0.2293 | ±0.4587 | **+8.471** | **2.43e-17** | *** |
| Education: graduate level (vs college) | +0.0324 | 0.0685 | ±0.1371 | +0.473 | 0.6361 |  |
| **Education: high school or below (vs college)** | **+0.5094** | 0.1408 | ±0.2816 | **+3.619** | **2.96e-04** | *** |
| Site: UCSD (vs UAB) | -0.0272 | 0.0829 | ±0.1659 | -0.328 | 0.7427 |  |
| **Site: UW (vs UAB)** | **-0.3563** | 0.0900 | ±0.1800 | **-3.960** | **7.49e-05** | *** |
| Season: spring (vs autumn) | -0.0483 | 0.0924 | ±0.1849 | -0.523 | 0.6013 |  |
| Season: summer (vs autumn) | +0.0727 | 0.0954 | ±0.1909 | +0.762 | 0.4461 |  |
| Season: winter (vs autumn) | -0.0081 | 0.0893 | ±0.1786 | -0.091 | 0.9274 |  |
| **Age (years)** | **-0.0118** | 0.0029 | ±0.0059 | **-3.991** | **6.57e-05** | *** |
| **BMI (kg/m2)** | **+0.0233** | 0.0052 | ±0.0105 | **+4.434** | **9.27e-06** | *** |
| Hypertension | +0.0925 | 0.0752 | ±0.1503 | +1.230 | 0.2186 |  |
| High cholesterol | -0.0900 | 0.0626 | ±0.1252 | -1.438 | 0.1504 |  |
| Kidney disease | -0.0209 | 0.1069 | ±0.2137 | -0.195 | 0.8450 |  |
| **Circulatory disease** | **+0.3165** | 0.1235 | ±0.2471 | **+2.562** | **0.0104** | * |
| Time 181-250, pooled (%) | -0.0095 | 0.0112 | ±0.0224 | -0.846 | 0.3976 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **674**, R² = **0.1489**, Adj R² = **0.1308**, F-statistic = **8.23** (p = **1.98e-16**), Residual SE = **0.824** on **659** df, AIC = **1665.9**, BIC = **1733.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9425** | 0.2292 | ±0.4584 | **+8.475** | **2.36e-17** | *** |
| Education: graduate level (vs college) | +0.0331 | 0.0685 | ±0.1371 | +0.484 | 0.6287 |  |
| **Education: high school or below (vs college)** | **+0.5096** | 0.1407 | ±0.2813 | **+3.623** | **2.91e-04** | *** |
| Site: UCSD (vs UAB) | -0.0291 | 0.0829 | ±0.1659 | -0.351 | 0.7257 |  |
| **Site: UW (vs UAB)** | **-0.3561** | 0.0900 | ±0.1799 | **-3.959** | **7.52e-05** | *** |
| Season: spring (vs autumn) | -0.0487 | 0.0924 | ±0.1848 | -0.527 | 0.5981 |  |
| Season: summer (vs autumn) | +0.0725 | 0.0953 | ±0.1907 | +0.761 | 0.4467 |  |
| Season: winter (vs autumn) | -0.0095 | 0.0892 | ±0.1784 | -0.107 | 0.9151 |  |
| **Age (years)** | **-0.0117** | 0.0029 | ±0.0059 | **-3.989** | **6.62e-05** | *** |
| **BMI (kg/m2)** | **+0.0234** | 0.0052 | ±0.0105 | **+4.455** | **8.40e-06** | *** |
| Hypertension | +0.0923 | 0.0751 | ±0.1502 | +1.229 | 0.2191 |  |
| High cholesterol | -0.0890 | 0.0626 | ±0.1251 | -1.423 | 0.1548 |  |
| Kidney disease | -0.0193 | 0.1066 | ±0.2132 | -0.181 | 0.8560 |  |
| **Circulatory disease** | **+0.3187** | 0.1235 | ±0.2471 | **+2.580** | **0.0099** | ** |
| Avg. daily time 181-250 (%) | -0.0125 | 0.0114 | ±0.0227 | -1.098 | 0.2723 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **674**, R² = **0.1483**, Adj R² = **0.1302**, F-statistic = **8.20** (p = **2.38e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.3**, BIC = **1734.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9428** | 0.2293 | ±0.4587 | **+8.471** | **2.43e-17** | *** |
| Education: graduate level (vs college) | +0.0324 | 0.0685 | ±0.1371 | +0.473 | 0.6361 |  |
| **Education: high school or below (vs college)** | **+0.5094** | 0.1408 | ±0.2816 | **+3.619** | **2.96e-04** | *** |
| Site: UCSD (vs UAB) | -0.0272 | 0.0829 | ±0.1659 | -0.328 | 0.7427 |  |
| **Site: UW (vs UAB)** | **-0.3563** | 0.0900 | ±0.1800 | **-3.960** | **7.49e-05** | *** |
| Season: spring (vs autumn) | -0.0483 | 0.0924 | ±0.1849 | -0.523 | 0.6013 |  |
| Season: summer (vs autumn) | +0.0727 | 0.0954 | ±0.1909 | +0.762 | 0.4461 |  |
| Season: winter (vs autumn) | -0.0081 | 0.0893 | ±0.1786 | -0.091 | 0.9274 |  |
| **Age (years)** | **-0.0118** | 0.0029 | ±0.0059 | **-3.991** | **6.57e-05** | *** |
| **BMI (kg/m2)** | **+0.0233** | 0.0052 | ±0.0105 | **+4.434** | **9.27e-06** | *** |
| Hypertension | +0.0925 | 0.0752 | ±0.1503 | +1.230 | 0.2186 |  |
| High cholesterol | -0.0900 | 0.0626 | ±0.1252 | -1.438 | 0.1504 |  |
| Kidney disease | -0.0209 | 0.1069 | ±0.2137 | -0.195 | 0.8450 |  |
| **Circulatory disease** | **+0.3165** | 0.1235 | ±0.2471 | **+2.562** | **0.0104** | * |
| Time > 180 (%) | -0.0095 | 0.0112 | ±0.0224 | -0.846 | 0.3976 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **674**, R² = **0.1489**, Adj R² = **0.1308**, F-statistic = **8.23** (p = **1.98e-16**), Residual SE = **0.824** on **659** df, AIC = **1665.9**, BIC = **1733.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9425** | 0.2292 | ±0.4584 | **+8.475** | **2.36e-17** | *** |
| Education: graduate level (vs college) | +0.0331 | 0.0685 | ±0.1371 | +0.484 | 0.6287 |  |
| **Education: high school or below (vs college)** | **+0.5096** | 0.1407 | ±0.2813 | **+3.623** | **2.91e-04** | *** |
| Site: UCSD (vs UAB) | -0.0291 | 0.0829 | ±0.1659 | -0.351 | 0.7257 |  |
| **Site: UW (vs UAB)** | **-0.3561** | 0.0900 | ±0.1799 | **-3.959** | **7.52e-05** | *** |
| Season: spring (vs autumn) | -0.0487 | 0.0924 | ±0.1848 | -0.527 | 0.5981 |  |
| Season: summer (vs autumn) | +0.0725 | 0.0953 | ±0.1907 | +0.761 | 0.4467 |  |
| Season: winter (vs autumn) | -0.0095 | 0.0892 | ±0.1784 | -0.107 | 0.9151 |  |
| **Age (years)** | **-0.0117** | 0.0029 | ±0.0059 | **-3.989** | **6.62e-05** | *** |
| **BMI (kg/m2)** | **+0.0234** | 0.0052 | ±0.0105 | **+4.455** | **8.40e-06** | *** |
| Hypertension | +0.0923 | 0.0751 | ±0.1502 | +1.229 | 0.2191 |  |
| High cholesterol | -0.0890 | 0.0626 | ±0.1251 | -1.423 | 0.1548 |  |
| Kidney disease | -0.0193 | 0.1066 | ±0.2132 | -0.181 | 0.8560 |  |
| **Circulatory disease** | **+0.3187** | 0.1235 | ±0.2471 | **+2.580** | **0.0099** | ** |
| Avg. daily time > 180 (%) | -0.0125 | 0.0114 | ±0.0227 | -1.098 | 0.2723 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 674)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **674**, R² = **0.1479**, Adj R² = **0.1298**, F-statistic = **8.17** (p = **2.71e-16**), Residual SE = **0.824** on **659** df, AIC = **1666.6**, BIC = **1734.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9439** | 0.2298 | ±0.4595 | **+8.461** | **2.66e-17** | *** |
| Education: graduate level (vs college) | +0.0311 | 0.0686 | ±0.1371 | +0.454 | 0.6496 |  |
| **Education: high school or below (vs college)** | **+0.5059** | 0.1409 | ±0.2819 | **+3.590** | **3.31e-04** | *** |
| Site: UCSD (vs UAB) | -0.0206 | 0.0828 | ±0.1656 | -0.249 | 0.8037 |  |
| **Site: UW (vs UAB)** | **-0.3604** | 0.0902 | ±0.1804 | **-3.996** | **6.44e-05** | *** |
| Season: spring (vs autumn) | -0.0458 | 0.0927 | ±0.1854 | -0.494 | 0.6210 |  |
| Season: summer (vs autumn) | +0.0741 | 0.0958 | ±0.1915 | +0.774 | 0.4388 |  |
| Season: winter (vs autumn) | -0.0058 | 0.0898 | ±0.1795 | -0.064 | 0.9488 |  |
| **Age (years)** | **-0.0118** | 0.0029 | ±0.0059 | **-4.018** | **5.87e-05** | *** |
| **BMI (kg/m2)** | **+0.0227** | 0.0053 | ±0.0107 | **+4.250** | **2.14e-05** | *** |
| Hypertension | +0.0929 | 0.0751 | ±0.1503 | +1.236 | 0.2166 |  |
| High cholesterol | -0.0970 | 0.0626 | ±0.1251 | -1.550 | 0.1211 |  |
| Kidney disease | -0.0243 | 0.1075 | ±0.2151 | -0.226 | 0.8212 |  |
| **Circulatory disease** | **+0.3125** | 0.1232 | ±0.2465 | **+2.536** | **0.0112** | * |
| Nocturnal time > 180 (%) | +0.0061 | 0.0119 | ±0.0239 | +0.514 | 0.6076 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 674; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **674**, R² = **0.3509**, Adj R² = **0.3382**, F-statistic = **27.45** (p = **9.60e-54**), Residual SE = **1.850** on **660** df, AIC = **2755.5**, BIC = **2818.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3033** | 0.6310 | ±1.2621 | **+38.513** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2021 | 0.1536 | ±0.3072 | -1.316 | 0.1883 |  |
| Education: high school or below (vs college) | +0.1411 | 0.2981 | ±0.5962 | +0.473 | 0.6360 |  |
| Site: UCSD (vs UAB) | +0.0242 | 0.1975 | ±0.3950 | +0.123 | 0.9024 |  |
| **Site: UW (vs UAB)** | **-0.8980** | 0.1945 | ±0.3890 | **-4.617** | **3.89e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6942** | 0.2087 | ±0.4173 | **-3.327** | **8.78e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8638** | 0.2379 | ±0.4758 | **+7.835** | **4.71e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6257** | 0.2150 | ±0.4299 | **-7.563** | **3.95e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.966 | 0.3343 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.841 | 0.4005 |  |
| Hypertension | +0.2214 | 0.1753 | ±0.3506 | +1.263 | 0.2065 |  |
| High cholesterol | -0.1049 | 0.1548 | ±0.3096 | -0.678 | 0.4980 |  |
| Kidney disease | +0.1088 | 0.2670 | ±0.5339 | +0.407 | 0.6837 |  |
| **Circulatory disease** | **+0.5063** | 0.2527 | ±0.5054 | **+2.004** | **0.0451** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **674**, R² = **0.3513**, Adj R² = **0.3375**, F-statistic = **25.49** (p = **4.33e-53**), Residual SE = **1.850** on **659** df, AIC = **2757.2**, BIC = **2824.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6101** | 1.2933 | ±2.5866 | **+18.256** | **1.86e-74** | *** |
| Education: graduate level (vs college) | -0.2037 | 0.1539 | ±0.3078 | -1.324 | 0.1856 |  |
| Education: high school or below (vs college) | +0.1387 | 0.2998 | ±0.5996 | +0.463 | 0.6436 |  |
| Site: UCSD (vs UAB) | +0.0240 | 0.1976 | ±0.3953 | +0.122 | 0.9032 |  |
| **Site: UW (vs UAB)** | **-0.9005** | 0.1947 | ±0.3893 | **-4.626** | **3.73e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6748** | 0.2109 | ±0.4218 | **-3.200** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+1.8670** | 0.2384 | ±0.4769 | **+7.830** | **4.88e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6144** | 0.2163 | ±0.4326 | **-7.463** | **8.43e-14** | *** |
| Age (years) | +0.0061 | 0.0070 | ±0.0139 | +0.881 | 0.3781 |  |
| BMI (kg/m2) | +0.0091 | 0.0119 | ±0.0238 | +0.768 | 0.4427 |  |
| Hypertension | +0.2140 | 0.1756 | ±0.3512 | +1.219 | 0.2229 |  |
| High cholesterol | -0.1150 | 0.1587 | ±0.3175 | -0.725 | 0.4687 |  |
| Kidney disease | +0.1070 | 0.2682 | ±0.5364 | +0.399 | 0.6899 |  |
| **Circulatory disease** | **+0.5127** | 0.2531 | ±0.5062 | **+2.025** | **0.0428** | * |
| HbA1c (%) | +0.1341 | 0.2197 | ±0.4394 | +0.610 | 0.5416 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **674**, R² = **0.3512**, Adj R² = **0.3374**, F-statistic = **25.48** (p = **4.57e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.3**, BIC = **2825.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9512** | 0.9503 | ±1.9005 | **+25.205** | **3.53e-140** | *** |
| Education: graduate level (vs college) | -0.2072 | 0.1535 | ±0.3070 | -1.349 | 0.1772 |  |
| Education: high school or below (vs college) | +0.1358 | 0.2984 | ±0.5968 | +0.455 | 0.6491 |  |
| Site: UCSD (vs UAB) | +0.0291 | 0.1987 | ±0.3974 | +0.147 | 0.8835 |  |
| **Site: UW (vs UAB)** | **-0.9037** | 0.1942 | ±0.3884 | **-4.654** | **3.25e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6924** | 0.2088 | ±0.4176 | **-3.316** | **9.13e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8630** | 0.2381 | ±0.4761 | **+7.826** | **5.05e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6221** | 0.2151 | ±0.4303 | **-7.540** | **4.72e-14** | *** |
| Age (years) | +0.0065 | 0.0069 | ±0.0139 | +0.939 | 0.3478 |  |
| BMI (kg/m2) | +0.0094 | 0.0119 | ±0.0239 | +0.788 | 0.4306 |  |
| Hypertension | +0.2162 | 0.1747 | ±0.3494 | +1.238 | 0.2158 |  |
| High cholesterol | -0.1049 | 0.1550 | ±0.3099 | -0.677 | 0.4986 |  |
| Kidney disease | +0.1022 | 0.2662 | ±0.5324 | +0.384 | 0.7012 |  |
| **Circulatory disease** | **+0.4999** | 0.2530 | ±0.5059 | **+1.976** | **0.0482** | * |
| Mean glucose (mg/dL) | +0.0032 | 0.0064 | ±0.0128 | +0.502 | 0.6156 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **674**, R² = **0.3512**, Adj R² = **0.3374**, F-statistic = **25.48** (p = **4.57e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.3**, BIC = **2825.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5052** | 1.7193 | ±3.4387 | **+13.671** | **1.51e-42** | *** |
| Education: graduate level (vs college) | -0.2072 | 0.1535 | ±0.3070 | -1.349 | 0.1772 |  |
| Education: high school or below (vs college) | +0.1358 | 0.2984 | ±0.5968 | +0.455 | 0.6491 |  |
| Site: UCSD (vs UAB) | +0.0291 | 0.1987 | ±0.3974 | +0.147 | 0.8835 |  |
| **Site: UW (vs UAB)** | **-0.9037** | 0.1942 | ±0.3884 | **-4.654** | **3.25e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6924** | 0.2088 | ±0.4176 | **-3.316** | **9.13e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8630** | 0.2381 | ±0.4761 | **+7.826** | **5.05e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6221** | 0.2151 | ±0.4303 | **-7.540** | **4.72e-14** | *** |
| Age (years) | +0.0065 | 0.0069 | ±0.0139 | +0.939 | 0.3478 |  |
| BMI (kg/m2) | +0.0094 | 0.0119 | ±0.0239 | +0.788 | 0.4306 |  |
| Hypertension | +0.2162 | 0.1747 | ±0.3494 | +1.238 | 0.2158 |  |
| High cholesterol | -0.1049 | 0.1550 | ±0.3099 | -0.677 | 0.4986 |  |
| Kidney disease | +0.1022 | 0.2662 | ±0.5324 | +0.384 | 0.7012 |  |
| **Circulatory disease** | **+0.4999** | 0.2530 | ±0.5059 | **+1.976** | **0.0482** | * |
| GMI (%) | +0.1347 | 0.2683 | ±0.5367 | +0.502 | 0.6156 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **674**, R² = **0.3510**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.07e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1967** | 0.8661 | ±1.7322 | **+27.938** | **9.25e-172** | *** |
| Education: graduate level (vs college) | -0.2031 | 0.1535 | ±0.3069 | -1.324 | 0.1857 |  |
| Education: high school or below (vs college) | +0.1396 | 0.2985 | ±0.5970 | +0.468 | 0.6399 |  |
| Site: UCSD (vs UAB) | +0.0245 | 0.1978 | ±0.3957 | +0.124 | 0.9015 |  |
| **Site: UW (vs UAB)** | **-0.9000** | 0.1939 | ±0.3878 | **-4.642** | **3.45e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6949** | 0.2088 | ±0.4175 | **-3.328** | **8.73e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8628** | 0.2385 | ±0.4770 | **+7.811** | **5.68e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6258** | 0.2152 | ±0.4304 | **-7.556** | **4.17e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.972 | 0.3308 |  |
| BMI (kg/m2) | +0.0096 | 0.0121 | ±0.0243 | +0.791 | 0.4290 |  |
| Hypertension | +0.2204 | 0.1749 | ±0.3498 | +1.260 | 0.2077 |  |
| High cholesterol | -0.1058 | 0.1556 | ±0.3113 | -0.680 | 0.4967 |  |
| Kidney disease | +0.1077 | 0.2669 | ±0.5339 | +0.404 | 0.6865 |  |
| **Circulatory disease** | **+0.5047** | 0.2531 | ±0.5062 | **+1.994** | **0.0462** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.0010 | 0.0054 | ±0.0109 | +0.184 | 0.8541 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **674**, R² = **0.3518**, Adj R² = **0.3380**, F-statistic = **25.54** (p = **3.44e-53**), Residual SE = **1.850** on **659** df, AIC = **2756.7**, BIC = **2824.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5911** | 0.7186 | ±1.4371 | **+34.222** | **1.14e-256** | *** |
| Education: graduate level (vs college) | -0.2075 | 0.1542 | ±0.3085 | -1.346 | 0.1785 |  |
| Education: high school or below (vs college) | +0.1466 | 0.2962 | ±0.5924 | +0.495 | 0.6206 |  |
| Site: UCSD (vs UAB) | +0.0126 | 0.1977 | ±0.3954 | +0.064 | 0.9492 |  |
| **Site: UW (vs UAB)** | **-0.8897** | 0.1940 | ±0.3879 | **-4.586** | **4.51e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6938** | 0.2089 | ±0.4177 | **-3.322** | **8.95e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8658** | 0.2387 | ±0.4774 | **+7.816** | **5.44e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6217** | 0.2150 | ±0.4301 | **-7.541** | **4.65e-14** | *** |
| Age (years) | +0.0073 | 0.0069 | ±0.0138 | +1.052 | 0.2930 |  |
| BMI (kg/m2) | +0.0105 | 0.0120 | ±0.0239 | +0.877 | 0.3807 |  |
| Hypertension | +0.2299 | 0.1754 | ±0.3508 | +1.311 | 0.1899 |  |
| High cholesterol | -0.1025 | 0.1554 | ±0.3108 | -0.660 | 0.5095 |  |
| Kidney disease | +0.1169 | 0.2660 | ±0.5319 | +0.440 | 0.6603 |  |
| **Circulatory disease** | **+0.5051** | 0.2540 | ±0.5080 | **+1.989** | **0.0467** | * |
| Glucose SD, pooled (mg/dL) | -0.0177 | 0.0194 | ±0.0387 | -0.917 | 0.3594 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **674**, R² = **0.3518**, Adj R² = **0.3380**, F-statistic = **25.54** (p = **3.43e-53**), Residual SE = **1.850** on **659** df, AIC = **2756.7**, BIC = **2824.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5668** | 0.7130 | ±1.4261 | **+34.454** | **3.90e-260** | *** |
| Education: graduate level (vs college) | -0.2050 | 0.1542 | ±0.3083 | -1.330 | 0.1835 |  |
| Education: high school or below (vs college) | +0.1474 | 0.2963 | ±0.5925 | +0.497 | 0.6189 |  |
| Site: UCSD (vs UAB) | +0.0108 | 0.1977 | ±0.3954 | +0.055 | 0.9562 |  |
| **Site: UW (vs UAB)** | **-0.8901** | 0.1941 | ±0.3883 | **-4.585** | **4.54e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6963** | 0.2089 | ±0.4177 | **-3.334** | **8.57e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8626** | 0.2383 | ±0.4766 | **+7.817** | **5.43e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6272** | 0.2147 | ±0.4293 | **-7.580** | **3.44e-14** | *** |
| Age (years) | +0.0072 | 0.0069 | ±0.0138 | +1.053 | 0.2922 |  |
| BMI (kg/m2) | +0.0106 | 0.0120 | ±0.0240 | +0.887 | 0.3751 |  |
| Hypertension | +0.2288 | 0.1757 | ±0.3515 | +1.302 | 0.1929 |  |
| High cholesterol | -0.1034 | 0.1552 | ±0.3104 | -0.666 | 0.5052 |  |
| Kidney disease | +0.1198 | 0.2657 | ±0.5315 | +0.451 | 0.6522 |  |
| **Circulatory disease** | **+0.5055** | 0.2540 | ±0.5080 | **+1.990** | **0.0466** | * |
| Avg. daily SD (mg/dL) | -0.0180 | 0.0195 | ±0.0389 | -0.925 | 0.3549 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **674**, R² = **0.3525**, Adj R² = **0.3387**, F-statistic = **25.63** (p = **2.39e-53**), Residual SE = **1.849** on **659** df, AIC = **2755.9**, BIC = **2823.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.8018** | 0.7513 | ±1.5026 | **+33.011** | **5.60e-239** | *** |
| Education: graduate level (vs college) | -0.2185 | 0.1546 | ±0.3092 | -1.413 | 0.1575 |  |
| Education: high school or below (vs college) | +0.1411 | 0.2952 | ±0.5904 | +0.478 | 0.6328 |  |
| Site: UCSD (vs UAB) | +0.0123 | 0.1969 | ±0.3939 | +0.063 | 0.9502 |  |
| **Site: UW (vs UAB)** | **-0.8931** | 0.1938 | ±0.3876 | **-4.608** | **4.07e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6907** | 0.2086 | ±0.4173 | **-3.310** | **9.31e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8672** | 0.2381 | ±0.4763 | **+7.841** | **4.47e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6125** | 0.2151 | ±0.4303 | **-7.495** | **6.63e-14** | *** |
| Age (years) | +0.0074 | 0.0069 | ±0.0137 | +1.072 | 0.2836 |  |
| BMI (kg/m2) | +0.0099 | 0.0120 | ±0.0239 | +0.824 | 0.4098 |  |
| Hypertension | +0.2286 | 0.1756 | ±0.3511 | +1.302 | 0.1928 |  |
| High cholesterol | -0.1026 | 0.1552 | ±0.3104 | -0.661 | 0.5085 |  |
| Kidney disease | +0.1132 | 0.2668 | ±0.5336 | +0.424 | 0.6714 |  |
| Circulatory disease | +0.4957 | 0.2533 | ±0.5067 | +1.957 | 0.0504 | . |
| CV (%) | -0.0332 | 0.0251 | ±0.0502 | -1.322 | 0.1861 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **674**, R² = **0.3521**, Adj R² = **0.3383**, F-statistic = **25.58** (p = **2.98e-53**), Residual SE = **1.849** on **659** df, AIC = **2756.4**, BIC = **2824.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8388** | 0.7435 | ±1.4871 | **+32.062** | **1.51e-225** | *** |
| Education: graduate level (vs college) | -0.2165 | 0.1545 | ±0.3091 | -1.401 | 0.1612 |  |
| Education: high school or below (vs college) | +0.1433 | 0.2958 | ±0.5916 | +0.484 | 0.6280 |  |
| Site: UCSD (vs UAB) | +0.0168 | 0.1971 | ±0.3942 | +0.085 | 0.9323 |  |
| **Site: UW (vs UAB)** | **-0.8920** | 0.1940 | ±0.3881 | **-4.597** | **4.29e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6875** | 0.2091 | ±0.4182 | **-3.287** | **0.0010** | ** |
| **Season: summer (vs autumn)** | **+1.8652** | 0.2381 | ±0.4763 | **+7.832** | **4.80e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6141** | 0.2154 | ±0.4309 | **-7.492** | **6.79e-14** | *** |
| Age (years) | +0.0072 | 0.0069 | ±0.0137 | +1.044 | 0.2965 |  |
| BMI (kg/m2) | +0.0099 | 0.0119 | ±0.0239 | +0.829 | 0.4072 |  |
| Hypertension | +0.2281 | 0.1756 | ±0.3512 | +1.299 | 0.1940 |  |
| High cholesterol | -0.1043 | 0.1551 | ±0.3103 | -0.672 | 0.5015 |  |
| Kidney disease | +0.1126 | 0.2669 | ±0.5338 | +0.422 | 0.6731 |  |
| **Circulatory disease** | **+0.4974** | 0.2534 | ±0.5068 | **+1.963** | **0.0497** | * |
| Mean / SD ratio | +0.0683 | 0.0610 | ±0.1220 | +1.119 | 0.2631 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **674**, R² = **0.3517**, Adj R² = **0.3379**, F-statistic = **25.53** (p = **3.56e-53**), Residual SE = **1.850** on **659** df, AIC = **2756.8**, BIC = **2824.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9427** | 0.7183 | ±1.4366 | **+33.331** | **1.35e-243** | *** |
| Education: graduate level (vs college) | -0.2114 | 0.1547 | ±0.3095 | -1.366 | 0.1718 |  |
| Education: high school or below (vs college) | +0.1435 | 0.2965 | ±0.5930 | +0.484 | 0.6284 |  |
| Site: UCSD (vs UAB) | +0.0168 | 0.1972 | ±0.3943 | +0.085 | 0.9320 |  |
| **Site: UW (vs UAB)** | **-0.8922** | 0.1942 | ±0.3885 | **-4.593** | **4.36e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6912** | 0.2091 | ±0.4183 | **-3.305** | **9.51e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8617** | 0.2379 | ±0.4758 | **+7.825** | **5.07e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6217** | 0.2149 | ±0.4298 | **-7.546** | **4.47e-14** | *** |
| Age (years) | +0.0071 | 0.0069 | ±0.0137 | +1.038 | 0.2992 |  |
| BMI (kg/m2) | +0.0103 | 0.0120 | ±0.0239 | +0.858 | 0.3911 |  |
| Hypertension | +0.2237 | 0.1756 | ±0.3512 | +1.274 | 0.2028 |  |
| High cholesterol | -0.1060 | 0.1551 | ±0.3101 | -0.683 | 0.4943 |  |
| Kidney disease | +0.1143 | 0.2670 | ±0.5339 | +0.428 | 0.6685 |  |
| **Circulatory disease** | **+0.4988** | 0.2530 | ±0.5060 | **+1.972** | **0.0486** | * |
| Avg. daily mean/SD | +0.0453 | 0.0480 | ±0.0959 | +0.944 | 0.3450 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **674**, R² = **0.3514**, Adj R² = **0.3376**, F-statistic = **25.50** (p = **4.15e-53**), Residual SE = **1.850** on **659** df, AIC = **2757.1**, BIC = **2824.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0364** | 0.7480 | ±1.4960 | **+32.135** | **1.43e-226** | *** |
| Education: graduate level (vs college) | -0.2023 | 0.1538 | ±0.3076 | -1.315 | 0.1885 |  |
| Education: high school or below (vs college) | +0.1287 | 0.2993 | ±0.5986 | +0.430 | 0.6671 |  |
| Site: UCSD (vs UAB) | +0.0288 | 0.1984 | ±0.3967 | +0.145 | 0.8846 |  |
| **Site: UW (vs UAB)** | **-0.8961** | 0.1949 | ±0.3898 | **-4.598** | **4.27e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6958** | 0.2093 | ±0.4187 | **-3.324** | **8.87e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8684** | 0.2380 | ±0.4760 | **+7.851** | **4.13e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6237** | 0.2154 | ±0.4307 | **-7.539** | **4.74e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.976 | 0.3289 |  |
| BMI (kg/m2) | +0.0101 | 0.0119 | ±0.0238 | +0.849 | 0.3958 |  |
| Hypertension | +0.2258 | 0.1763 | ±0.3525 | +1.281 | 0.2001 |  |
| High cholesterol | -0.1037 | 0.1547 | ±0.3094 | -0.670 | 0.5027 |  |
| Kidney disease | +0.1013 | 0.2674 | ±0.5348 | +0.379 | 0.7047 |  |
| **Circulatory disease** | **+0.5089** | 0.2527 | ±0.5054 | **+2.014** | **0.0440** | * |
| MAG (mg/dL/h) | +0.0071 | 0.0114 | ±0.0228 | +0.623 | 0.5330 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **674**, R² = **0.3514**, Adj R² = **0.3377**, F-statistic = **25.51** (p = **4.05e-53**), Residual SE = **1.850** on **659** df, AIC = **2757.0**, BIC = **2824.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5682** | 0.7466 | ±1.4933 | **+32.906** | **1.82e-237** | *** |
| Education: graduate level (vs college) | -0.2008 | 0.1538 | ±0.3076 | -1.305 | 0.1918 |  |
| Education: high school or below (vs college) | +0.1492 | 0.2969 | ±0.5937 | +0.502 | 0.6153 |  |
| Site: UCSD (vs UAB) | +0.0175 | 0.1976 | ±0.3951 | +0.089 | 0.9293 |  |
| **Site: UW (vs UAB)** | **-0.8923** | 0.1944 | ±0.3889 | **-4.589** | **4.45e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6930** | 0.2092 | ±0.4184 | **-3.313** | **9.23e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8608** | 0.2378 | ±0.4756 | **+7.825** | **5.09e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6265** | 0.2150 | ±0.4299 | **-7.567** | **3.83e-14** | *** |
| Age (years) | +0.0070 | 0.0069 | ±0.0138 | +1.016 | 0.3094 |  |
| BMI (kg/m2) | +0.0097 | 0.0120 | ±0.0239 | +0.814 | 0.4154 |  |
| Hypertension | +0.2236 | 0.1759 | ±0.3517 | +1.271 | 0.2036 |  |
| High cholesterol | -0.1059 | 0.1551 | ±0.3102 | -0.683 | 0.4948 |  |
| Kidney disease | +0.1179 | 0.2670 | ±0.5339 | +0.441 | 0.6589 |  |
| **Circulatory disease** | **+0.5088** | 0.2539 | ±0.5078 | **+2.004** | **0.0451** | * |
| Avg. daily range (mg/dL) | -0.0031 | 0.0044 | ±0.0089 | -0.709 | 0.4782 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **674**, R² = **0.3510**, Adj R² = **0.3372**, F-statistic = **25.46** (p = **4.96e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3413** | 0.6545 | ±1.3091 | **+37.188** | **1.06e-302** | *** |
| Education: graduate level (vs college) | -0.2025 | 0.1539 | ±0.3078 | -1.316 | 0.1882 |  |
| Education: high school or below (vs college) | +0.1420 | 0.2983 | ±0.5965 | +0.476 | 0.6340 |  |
| Site: UCSD (vs UAB) | +0.0234 | 0.1976 | ±0.3952 | +0.119 | 0.9055 |  |
| **Site: UW (vs UAB)** | **-0.8968** | 0.1948 | ±0.3896 | **-4.604** | **4.15e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6910** | 0.2085 | ±0.4169 | **-3.315** | **9.18e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8692** | 0.2399 | ±0.4797 | **+7.793** | **6.56e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6218** | 0.2150 | ±0.4300 | **-7.544** | **4.55e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.964 | 0.3350 |  |
| BMI (kg/m2) | +0.0103 | 0.0120 | ±0.0239 | +0.863 | 0.3882 |  |
| Hypertension | +0.2211 | 0.1758 | ±0.3516 | +1.258 | 0.2085 |  |
| High cholesterol | -0.1021 | 0.1561 | ±0.3122 | -0.654 | 0.5130 |  |
| Kidney disease | +0.1056 | 0.2678 | ±0.5356 | +0.394 | 0.6935 |  |
| **Circulatory disease** | **+0.5075** | 0.2533 | ±0.5066 | **+2.003** | **0.0451** | * |
| SD of daily means (mg/dL) | -0.0087 | 0.0351 | ±0.0702 | -0.249 | 0.8034 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **674**, R² = **0.3509**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.12e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5753** | 2.3499 | ±4.6998 | **+10.458** | **1.35e-25** | *** |
| Education: graduate level (vs college) | -0.2022 | 0.1537 | ±0.3074 | -1.316 | 0.1882 |  |
| Education: high school or below (vs college) | +0.1411 | 0.2985 | ±0.5969 | +0.473 | 0.6364 |  |
| Site: UCSD (vs UAB) | +0.0255 | 0.1976 | ±0.3952 | +0.129 | 0.8973 |  |
| **Site: UW (vs UAB)** | **-0.8987** | 0.1947 | ±0.3893 | **-4.616** | **3.90e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6937** | 0.2090 | ±0.4181 | **-3.318** | **9.06e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8641** | 0.2380 | ±0.4760 | **+7.832** | **4.82e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6251** | 0.2152 | ±0.4304 | **-7.552** | **4.28e-14** | *** |
| Age (years) | +0.0066 | 0.0069 | ±0.0138 | +0.957 | 0.3383 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.837 | 0.4028 |  |
| Hypertension | +0.2212 | 0.1753 | ±0.3507 | +1.261 | 0.2071 |  |
| High cholesterol | -0.1058 | 0.1551 | ±0.3102 | -0.682 | 0.4950 |  |
| Kidney disease | +0.1078 | 0.2666 | ±0.5331 | +0.404 | 0.6860 |  |
| **Circulatory disease** | **+0.5053** | 0.2536 | ±0.5071 | **+1.993** | **0.0463** | * |
| Time in range 70-180, pooled (%) | -0.0027 | 0.0230 | ±0.0460 | -0.119 | 0.9054 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **674**, R² = **0.3509**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.14e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3820** | 2.4572 | ±4.9144 | **+9.923** | **3.32e-23** | *** |
| Education: graduate level (vs college) | -0.2021 | 0.1537 | ±0.3074 | -1.315 | 0.1885 |  |
| Education: high school or below (vs college) | +0.1411 | 0.2984 | ±0.5968 | +0.473 | 0.6363 |  |
| Site: UCSD (vs UAB) | +0.0246 | 0.1975 | ±0.3949 | +0.125 | 0.9009 |  |
| **Site: UW (vs UAB)** | **-0.8981** | 0.1947 | ±0.3895 | **-4.612** | **3.98e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6941** | 0.2091 | ±0.4182 | **-3.319** | **9.02e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8639** | 0.2381 | ±0.4761 | **+7.829** | **4.90e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6255** | 0.2153 | ±0.4305 | **-7.551** | **4.31e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.963 | 0.3357 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.839 | 0.4012 |  |
| Hypertension | +0.2214 | 0.1754 | ±0.3509 | +1.262 | 0.2070 |  |
| High cholesterol | -0.1052 | 0.1550 | ±0.3100 | -0.678 | 0.4975 |  |
| Kidney disease | +0.1084 | 0.2664 | ±0.5328 | +0.407 | 0.6839 |  |
| **Circulatory disease** | **+0.5060** | 0.2539 | ±0.5078 | **+1.993** | **0.0463** | * |
| Avg. daily time in range 70-180 (%) | -0.0008 | 0.0242 | ±0.0483 | -0.033 | 0.9739 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **674**, R² = **0.3510**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.10e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3089** | 0.6325 | ±1.2650 | **+38.432** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2042 | 0.1540 | ±0.3080 | -1.326 | 0.1849 |  |
| Education: high school or below (vs college) | +0.1385 | 0.2977 | ±0.5954 | +0.465 | 0.6418 |  |
| Site: UCSD (vs UAB) | +0.0250 | 0.1993 | ±0.3985 | +0.126 | 0.9000 |  |
| **Site: UW (vs UAB)** | **-0.8986** | 0.1944 | ±0.3887 | **-4.623** | **3.78e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6939** | 0.2088 | ±0.4177 | **-3.323** | **8.92e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8648** | 0.2379 | ±0.4758 | **+7.839** | **4.55e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6242** | 0.2156 | ±0.4313 | **-7.532** | **4.98e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.963 | 0.3356 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0239 | +0.837 | 0.4023 |  |
| Hypertension | +0.2217 | 0.1756 | ±0.3511 | +1.263 | 0.2065 |  |
| High cholesterol | -0.1045 | 0.1544 | ±0.3088 | -0.677 | 0.4986 |  |
| Kidney disease | +0.1080 | 0.2669 | ±0.5339 | +0.405 | 0.6857 |  |
| **Circulatory disease** | **+0.5052** | 0.2528 | ±0.5056 | **+1.998** | **0.0457** | * |
| Time 54-69, pooled (%) | -0.0179 | 0.1520 | ±0.3039 | -0.118 | 0.9061 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **674**, R² = **0.3509**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.15e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3030** | 0.6324 | ±1.2648 | **+38.429** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2019 | 0.1540 | ±0.3080 | -1.311 | 0.1899 |  |
| Education: high school or below (vs college) | +0.1413 | 0.2980 | ±0.5960 | +0.474 | 0.6355 |  |
| Site: UCSD (vs UAB) | +0.0241 | 0.1999 | ±0.3998 | +0.121 | 0.9039 |  |
| **Site: UW (vs UAB)** | **-0.8980** | 0.1944 | ±0.3889 | **-4.618** | **3.87e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6942** | 0.2088 | ±0.4177 | **-3.324** | **8.87e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8638** | 0.2379 | ±0.4758 | **+7.834** | **4.74e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6258** | 0.2157 | ±0.4313 | **-7.538** | **4.77e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.964 | 0.3348 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.841 | 0.4005 |  |
| Hypertension | +0.2214 | 0.1756 | ±0.3511 | +1.261 | 0.2072 |  |
| High cholesterol | -0.1049 | 0.1544 | ±0.3089 | -0.679 | 0.4969 |  |
| Kidney disease | +0.1088 | 0.2670 | ±0.5340 | +0.407 | 0.6837 |  |
| **Circulatory disease** | **+0.5064** | 0.2529 | ±0.5057 | **+2.003** | **0.0452** | * |
| Avg. daily time 54-69 (%) | +0.0012 | 0.1403 | ±0.2806 | +0.009 | 0.9931 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **674**, R² = **0.3510**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.10e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3089** | 0.6325 | ±1.2650 | **+38.432** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2042 | 0.1540 | ±0.3080 | -1.326 | 0.1849 |  |
| Education: high school or below (vs college) | +0.1385 | 0.2977 | ±0.5954 | +0.465 | 0.6418 |  |
| Site: UCSD (vs UAB) | +0.0250 | 0.1993 | ±0.3985 | +0.126 | 0.9000 |  |
| **Site: UW (vs UAB)** | **-0.8986** | 0.1944 | ±0.3887 | **-4.623** | **3.78e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6939** | 0.2088 | ±0.4177 | **-3.323** | **8.92e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8648** | 0.2379 | ±0.4758 | **+7.839** | **4.55e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6242** | 0.2156 | ±0.4313 | **-7.532** | **4.98e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.963 | 0.3356 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0239 | +0.837 | 0.4023 |  |
| Hypertension | +0.2217 | 0.1756 | ±0.3511 | +1.263 | 0.2065 |  |
| High cholesterol | -0.1045 | 0.1544 | ±0.3088 | -0.677 | 0.4986 |  |
| Kidney disease | +0.1080 | 0.2669 | ±0.5339 | +0.405 | 0.6857 |  |
| **Circulatory disease** | **+0.5052** | 0.2528 | ±0.5056 | **+1.998** | **0.0457** | * |
| Time < 70 (%) | -0.0179 | 0.1520 | ±0.3039 | -0.118 | 0.9061 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **674**, R² = **0.3509**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.15e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3030** | 0.6324 | ±1.2648 | **+38.429** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2019 | 0.1540 | ±0.3080 | -1.311 | 0.1899 |  |
| Education: high school or below (vs college) | +0.1413 | 0.2980 | ±0.5960 | +0.474 | 0.6355 |  |
| Site: UCSD (vs UAB) | +0.0241 | 0.1999 | ±0.3998 | +0.121 | 0.9039 |  |
| **Site: UW (vs UAB)** | **-0.8980** | 0.1944 | ±0.3889 | **-4.618** | **3.87e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6942** | 0.2088 | ±0.4177 | **-3.324** | **8.87e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8638** | 0.2379 | ±0.4758 | **+7.834** | **4.74e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6258** | 0.2157 | ±0.4313 | **-7.538** | **4.77e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.964 | 0.3348 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.841 | 0.4005 |  |
| Hypertension | +0.2214 | 0.1756 | ±0.3511 | +1.261 | 0.2072 |  |
| High cholesterol | -0.1049 | 0.1544 | ±0.3089 | -0.679 | 0.4969 |  |
| Kidney disease | +0.1088 | 0.2670 | ±0.5340 | +0.407 | 0.6837 |  |
| **Circulatory disease** | **+0.5064** | 0.2529 | ±0.5057 | **+2.003** | **0.0452** | * |
| Avg. daily time < 70 (%) | +0.0012 | 0.1403 | ±0.2806 | +0.009 | 0.9931 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **674**, R² = **0.3510**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.11e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3028** | 0.6315 | ±1.2629 | **+38.487** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2027 | 0.1537 | ±0.3074 | -1.319 | 0.1873 |  |
| Education: high school or below (vs college) | +0.1406 | 0.2984 | ±0.5968 | +0.471 | 0.6375 |  |
| Site: UCSD (vs UAB) | +0.0260 | 0.1981 | ±0.3962 | +0.131 | 0.8957 |  |
| **Site: UW (vs UAB)** | **-0.8989** | 0.1945 | ±0.3890 | **-4.621** | **3.81e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6935** | 0.2091 | ±0.4181 | **-3.317** | **9.10e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8643** | 0.2379 | ±0.4759 | **+7.836** | **4.67e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6247** | 0.2152 | ±0.4305 | **-7.548** | **4.41e-14** | *** |
| Age (years) | +0.0066 | 0.0069 | ±0.0138 | +0.955 | 0.3394 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.835 | 0.4036 |  |
| Hypertension | +0.2212 | 0.1754 | ±0.3507 | +1.261 | 0.2072 |  |
| High cholesterol | -0.1060 | 0.1554 | ±0.3108 | -0.682 | 0.4954 |  |
| Kidney disease | +0.1074 | 0.2664 | ±0.5328 | +0.403 | 0.6869 |  |
| **Circulatory disease** | **+0.5049** | 0.2536 | ±0.5072 | **+1.991** | **0.0465** | * |
| Time 181-250, pooled (%) | +0.0034 | 0.0233 | ±0.0466 | +0.145 | 0.8846 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **674**, R² = **0.3509**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.14e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3032** | 0.6317 | ±1.2635 | **+38.471** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2022 | 0.1537 | ±0.3074 | -1.315 | 0.1883 |  |
| Education: high school or below (vs college) | +0.1410 | 0.2983 | ±0.5966 | +0.473 | 0.6365 |  |
| Site: UCSD (vs UAB) | +0.0246 | 0.1981 | ±0.3961 | +0.124 | 0.9011 |  |
| **Site: UW (vs UAB)** | **-0.8982** | 0.1946 | ±0.3892 | **-4.615** | **3.93e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6941** | 0.2091 | ±0.4182 | **-3.319** | **9.03e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8639** | 0.2380 | ±0.4760 | **+7.832** | **4.80e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6254** | 0.2154 | ±0.4307 | **-7.548** | **4.43e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.962 | 0.3359 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.840 | 0.4011 |  |
| Hypertension | +0.2214 | 0.1755 | ±0.3509 | +1.262 | 0.2070 |  |
| High cholesterol | -0.1051 | 0.1554 | ±0.3108 | -0.677 | 0.4987 |  |
| Kidney disease | +0.1084 | 0.2662 | ±0.5325 | +0.407 | 0.6838 |  |
| **Circulatory disease** | **+0.5060** | 0.2540 | ±0.5080 | **+1.992** | **0.0464** | * |
| Avg. daily time 181-250 (%) | +0.0007 | 0.0245 | ±0.0489 | +0.030 | 0.9761 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **674**, R² = **0.3510**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.11e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3028** | 0.6315 | ±1.2629 | **+38.487** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2027 | 0.1537 | ±0.3074 | -1.319 | 0.1873 |  |
| Education: high school or below (vs college) | +0.1406 | 0.2984 | ±0.5968 | +0.471 | 0.6375 |  |
| Site: UCSD (vs UAB) | +0.0260 | 0.1981 | ±0.3962 | +0.131 | 0.8957 |  |
| **Site: UW (vs UAB)** | **-0.8989** | 0.1945 | ±0.3890 | **-4.621** | **3.81e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6935** | 0.2091 | ±0.4181 | **-3.317** | **9.10e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8643** | 0.2379 | ±0.4759 | **+7.836** | **4.67e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6247** | 0.2152 | ±0.4305 | **-7.548** | **4.41e-14** | *** |
| Age (years) | +0.0066 | 0.0069 | ±0.0138 | +0.955 | 0.3394 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.835 | 0.4036 |  |
| Hypertension | +0.2212 | 0.1754 | ±0.3507 | +1.261 | 0.2072 |  |
| High cholesterol | -0.1060 | 0.1554 | ±0.3108 | -0.682 | 0.4954 |  |
| Kidney disease | +0.1074 | 0.2664 | ±0.5328 | +0.403 | 0.6869 |  |
| **Circulatory disease** | **+0.5049** | 0.2536 | ±0.5072 | **+1.991** | **0.0465** | * |
| Time > 180 (%) | +0.0034 | 0.0233 | ±0.0466 | +0.145 | 0.8846 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **674**, R² = **0.3509**, Adj R² = **0.3372**, F-statistic = **25.45** (p = **5.14e-53**), Residual SE = **1.851** on **659** df, AIC = **2757.5**, BIC = **2825.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3032** | 0.6317 | ±1.2635 | **+38.471** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2022 | 0.1537 | ±0.3074 | -1.315 | 0.1883 |  |
| Education: high school or below (vs college) | +0.1410 | 0.2983 | ±0.5966 | +0.473 | 0.6365 |  |
| Site: UCSD (vs UAB) | +0.0246 | 0.1981 | ±0.3961 | +0.124 | 0.9011 |  |
| **Site: UW (vs UAB)** | **-0.8982** | 0.1946 | ±0.3892 | **-4.615** | **3.93e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6941** | 0.2091 | ±0.4182 | **-3.319** | **9.03e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8639** | 0.2380 | ±0.4760 | **+7.832** | **4.80e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6254** | 0.2154 | ±0.4307 | **-7.548** | **4.43e-14** | *** |
| Age (years) | +0.0067 | 0.0069 | ±0.0138 | +0.962 | 0.3359 |  |
| BMI (kg/m2) | +0.0100 | 0.0119 | ±0.0238 | +0.840 | 0.4011 |  |
| Hypertension | +0.2214 | 0.1755 | ±0.3509 | +1.262 | 0.2070 |  |
| High cholesterol | -0.1051 | 0.1554 | ±0.3108 | -0.677 | 0.4987 |  |
| Kidney disease | +0.1084 | 0.2662 | ±0.5325 | +0.407 | 0.6838 |  |
| **Circulatory disease** | **+0.5060** | 0.2540 | ±0.5080 | **+1.992** | **0.0464** | * |
| Avg. daily time > 180 (%) | +0.0007 | 0.0245 | ±0.0489 | +0.030 | 0.9761 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 674)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **674**, R² = **0.3517**, Adj R² = **0.3379**, F-statistic = **25.53** (p = **3.56e-53**), Residual SE = **1.850** on **659** df, AIC = **2756.8**, BIC = **2824.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3114** | 0.6290 | ±1.2580 | **+38.652** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2006 | 0.1536 | ±0.3073 | -1.306 | 0.1916 |  |
| Education: high school or below (vs college) | +0.1337 | 0.2987 | ±0.5975 | +0.448 | 0.6544 |  |
| Site: UCSD (vs UAB) | +0.0302 | 0.1978 | ±0.3956 | +0.153 | 0.8787 |  |
| **Site: UW (vs UAB)** | **-0.9028** | 0.1944 | ±0.3888 | **-4.644** | **3.42e-06** | *** |
| **Season: spring (vs autumn)** | **-0.6930** | 0.2084 | ±0.4169 | **-3.325** | **8.85e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8639** | 0.2377 | ±0.4755 | **+7.841** | **4.49e-15** | *** |
| **Season: winter (vs autumn)** | **-1.6270** | 0.2150 | ±0.4300 | **-7.567** | **3.81e-14** | *** |
| Age (years) | +0.0069 | 0.0069 | ±0.0138 | +0.993 | 0.3205 |  |
| BMI (kg/m2) | +0.0088 | 0.0120 | ±0.0239 | +0.738 | 0.4608 |  |
| Hypertension | +0.2250 | 0.1755 | ±0.3511 | +1.282 | 0.1999 |  |
| High cholesterol | -0.1183 | 0.1570 | ±0.3141 | -0.753 | 0.4514 |  |
| Kidney disease | +0.1100 | 0.2665 | ±0.5330 | +0.413 | 0.6798 |  |
| **Circulatory disease** | **+0.5065** | 0.2526 | ±0.5053 | **+2.005** | **0.0450** | * |
| Nocturnal time > 180 (%) | +0.0205 | 0.0215 | ±0.0430 | +0.953 | 0.3405 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 674; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **674**, R² = **0.2904**, Adj R² = **0.2764**, F-statistic = **20.77** (p = **2.09e-41**), Residual SE = **5.696** on **660** df, AIC = **4271.9**, BIC = **4335.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1962** | 1.6957 | ±3.3915 | **+29.602** | **1.43e-192** | *** |
| **Education: graduate level (vs college)** | **+1.3181** | 0.4746 | ±0.9493 | **+2.777** | **0.0055** | ** |
| Education: high school or below (vs college) | +0.1824 | 0.9085 | ±1.8170 | +0.201 | 0.8409 |  |
| **Site: UCSD (vs UAB)** | **+3.1257** | 0.6106 | ±1.2211 | **+5.119** | **3.06e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9015** | 0.5738 | ±1.1476 | **-3.314** | **9.20e-04** | *** |
| Season: spring (vs autumn) | -0.9288 | 0.6414 | ±1.2828 | -1.448 | 0.1476 |  |
| **Season: summer (vs autumn)** | **+2.4749** | 0.6646 | ±1.3291 | **+3.724** | **1.96e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9883** | 0.6541 | ±1.3082 | **-7.626** | **2.42e-14** | *** |
| **Age (years)** | **-0.0477** | 0.0208 | ±0.0415 | **-2.297** | **0.0216** | * |
| BMI (kg/m2) | -0.0548 | 0.0340 | ±0.0680 | -1.611 | 0.1072 |  |
| Hypertension | +0.1131 | 0.5185 | ±1.0370 | +0.218 | 0.8274 |  |
| High cholesterol | -0.9252 | 0.4809 | ±0.9617 | -1.924 | 0.0543 | . |
| Kidney disease | -0.4924 | 0.8778 | ±1.7556 | -0.561 | 0.5748 |  |
| Circulatory disease | -0.8169 | 0.7057 | ±1.4113 | -1.158 | 0.2470 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **674**, R² = **0.2908**, Adj R² = **0.2758**, F-statistic = **19.30** (p = **8.01e-41**), Residual SE = **5.699** on **659** df, AIC = **4273.5**, BIC = **4341.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8821** | 3.9030 | ±7.8060 | **+12.268** | **1.35e-34** | *** |
| **Education: graduate level (vs college)** | **+1.3126** | 0.4758 | ±0.9516 | **+2.759** | **0.0058** | ** |
| Education: high school or below (vs college) | +0.1745 | 0.9052 | ±1.8104 | +0.193 | 0.8471 |  |
| **Site: UCSD (vs UAB)** | **+3.1251** | 0.6113 | ±1.2225 | **+5.112** | **3.18e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9099** | 0.5746 | ±1.1491 | **-3.324** | **8.87e-04** | *** |
| Season: spring (vs autumn) | -0.8639 | 0.6493 | ±1.2986 | -1.331 | 0.1833 |  |
| **Season: summer (vs autumn)** | **+2.4856** | 0.6652 | ±1.3305 | **+3.736** | **1.87e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9508** | 0.6531 | ±1.3063 | **-7.580** | **3.45e-14** | *** |
| **Age (years)** | **-0.0494** | 0.0212 | ±0.0425 | **-2.327** | **0.0200** | * |
| BMI (kg/m2) | -0.0578 | 0.0345 | ±0.0690 | -1.676 | 0.0937 | . |
| Hypertension | +0.0884 | 0.5231 | ±1.0462 | +0.169 | 0.8658 |  |
| **High cholesterol** | **-0.9590** | 0.4803 | ±0.9606 | **-1.997** | **0.0459** | * |
| Kidney disease | -0.4983 | 0.8759 | ±1.7517 | -0.569 | 0.5694 |  |
| Circulatory disease | -0.7958 | 0.7036 | ±1.4073 | -1.131 | 0.2581 |  |
| HbA1c (%) | +0.4478 | 0.7000 | ±1.4001 | +0.640 | 0.5224 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **674**, R² = **0.2907**, Adj R² = **0.2756**, F-statistic = **19.29** (p = **8.53e-41**), Residual SE = **5.699** on **659** df, AIC = **4273.6**, BIC = **4341.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.0218** | 2.7763 | ±5.5526 | **+17.657** | **8.96e-70** | *** |
| **Education: graduate level (vs college)** | **+1.3011** | 0.4751 | ±0.9503 | **+2.738** | **0.0062** | ** |
| Education: high school or below (vs college) | +0.1647 | 0.9098 | ±1.8195 | +0.181 | 0.8563 |  |
| **Site: UCSD (vs UAB)** | **+3.1420** | 0.6125 | ±1.2251 | **+5.129** | **2.91e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9207** | 0.5739 | ±1.1478 | **-3.347** | **8.18e-04** | *** |
| Season: spring (vs autumn) | -0.9228 | 0.6434 | ±1.2868 | -1.434 | 0.1515 |  |
| **Season: summer (vs autumn)** | **+2.4721** | 0.6669 | ±1.3338 | **+3.707** | **2.10e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9764** | 0.6549 | ±1.3098 | **-7.599** | **2.99e-14** | *** |
| **Age (years)** | **-0.0482** | 0.0208 | ±0.0416 | **-2.315** | **0.0206** | * |
| BMI (kg/m2) | -0.0568 | 0.0341 | ±0.0682 | -1.668 | 0.0954 | . |
| Hypertension | +0.0958 | 0.5204 | ±1.0408 | +0.184 | 0.8539 |  |
| High cholesterol | -0.9252 | 0.4811 | ±0.9623 | -1.923 | 0.0545 | . |
| Kidney disease | -0.5144 | 0.8779 | ±1.7557 | -0.586 | 0.5579 |  |
| Circulatory disease | -0.8384 | 0.7090 | ±1.4180 | -1.183 | 0.2370 |  |
| Mean glucose (mg/dL) | +0.0108 | 0.0195 | ±0.0390 | +0.552 | 0.5809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **674**, R² = **0.2907**, Adj R² = **0.2756**, F-statistic = **19.29** (p = **8.53e-41**), Residual SE = **5.699** on **659** df, AIC = **4273.6**, BIC = **4341.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5340** | 5.1773 | ±10.3547 | **+9.181** | **4.26e-20** | *** |
| **Education: graduate level (vs college)** | **+1.3011** | 0.4751 | ±0.9503 | **+2.738** | **0.0062** | ** |
| Education: high school or below (vs college) | +0.1647 | 0.9098 | ±1.8195 | +0.181 | 0.8563 |  |
| **Site: UCSD (vs UAB)** | **+3.1420** | 0.6125 | ±1.2251 | **+5.129** | **2.91e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9207** | 0.5739 | ±1.1478 | **-3.347** | **8.18e-04** | *** |
| Season: spring (vs autumn) | -0.9228 | 0.6434 | ±1.2868 | -1.434 | 0.1515 |  |
| **Season: summer (vs autumn)** | **+2.4721** | 0.6669 | ±1.3338 | **+3.707** | **2.10e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9764** | 0.6549 | ±1.3098 | **-7.599** | **2.99e-14** | *** |
| **Age (years)** | **-0.0482** | 0.0208 | ±0.0416 | **-2.315** | **0.0206** | * |
| BMI (kg/m2) | -0.0568 | 0.0341 | ±0.0682 | -1.668 | 0.0954 | . |
| Hypertension | +0.0958 | 0.5204 | ±1.0408 | +0.184 | 0.8539 |  |
| High cholesterol | -0.9252 | 0.4811 | ±0.9623 | -1.923 | 0.0545 | . |
| Kidney disease | -0.5144 | 0.8779 | ±1.7557 | -0.586 | 0.5579 |  |
| Circulatory disease | -0.8384 | 0.7090 | ±1.4180 | -1.183 | 0.2370 |  |
| GMI (%) | +0.4495 | 0.8142 | ±1.6283 | +0.552 | 0.5809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **674**, R² = **0.2910**, Adj R² = **0.2760**, F-statistic = **19.32** (p = **7.25e-41**), Residual SE = **5.698** on **659** df, AIC = **4273.2**, BIC = **4340.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.6935** | 2.6130 | ±5.2260 | **+18.635** | **1.67e-77** | *** |
| **Education: graduate level (vs college)** | **+1.3033** | 0.4750 | ±0.9501 | **+2.744** | **0.0061** | ** |
| Education: high school or below (vs college) | +0.1621 | 0.9110 | ±1.8219 | +0.178 | 0.8588 |  |
| **Site: UCSD (vs UAB)** | **+3.1294** | 0.6120 | ±1.2241 | **+5.113** | **3.17e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9297** | 0.5738 | ±1.1477 | **-3.363** | **7.72e-04** | *** |
| Season: spring (vs autumn) | -0.9375 | 0.6418 | ±1.2835 | -1.461 | 0.1441 |  |
| **Season: summer (vs autumn)** | **+2.4605** | 0.6678 | ±1.3356 | **+3.685** | **2.29e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9907** | 0.6561 | ±1.3121 | **-7.607** | **2.80e-14** | *** |
| **Age (years)** | **-0.0470** | 0.0208 | ±0.0416 | **-2.261** | **0.0238** | * |
| BMI (kg/m2) | -0.0608 | 0.0349 | ±0.0697 | -1.744 | 0.0811 | . |
| Hypertension | +0.0982 | 0.5190 | ±1.0380 | +0.189 | 0.8499 |  |
| High cholesterol | -0.9380 | 0.4808 | ±0.9616 | -1.951 | 0.0510 | . |
| Kidney disease | -0.5068 | 0.8819 | ±1.7637 | -0.575 | 0.5655 |  |
| Circulatory disease | -0.8398 | 0.7089 | ±1.4178 | -1.185 | 0.2362 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0141 | 0.0177 | ±0.0354 | +0.795 | 0.4268 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **674**, R² = **0.2939**, Adj R² = **0.2789**, F-statistic = **19.60** (p = **2.00e-41**), Residual SE = **5.686** on **659** df, AIC = **4270.5**, BIC = **4338.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4321** | 1.9837 | ±3.9674 | **+24.415** | **1.19e-131** | *** |
| **Education: graduate level (vs college)** | **+1.3516** | 0.4744 | ±0.9488 | **+2.849** | **0.0044** | ** |
| Education: high school or below (vs college) | +0.1483 | 0.9039 | ±1.8078 | +0.164 | 0.8697 |  |
| **Site: UCSD (vs UAB)** | **+3.1971** | 0.6077 | ±1.2153 | **+5.261** | **1.43e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9526** | 0.5702 | ±1.1405 | **-3.424** | **6.16e-04** | *** |
| Season: spring (vs autumn) | -0.9317 | 0.6398 | ±1.2797 | -1.456 | 0.1454 |  |
| **Season: summer (vs autumn)** | **+2.4626** | 0.6643 | ±1.3286 | **+3.707** | **2.10e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0124** | 0.6570 | ±1.3139 | **-7.630** | **2.35e-14** | *** |
| **Age (years)** | **-0.0513** | 0.0207 | ±0.0414 | **-2.478** | **0.0132** | * |
| BMI (kg/m2) | -0.0577 | 0.0343 | ±0.0686 | -1.681 | 0.0927 | . |
| Hypertension | +0.0608 | 0.5186 | ±1.0372 | +0.117 | 0.9067 |  |
| High cholesterol | -0.9399 | 0.4809 | ±0.9619 | -1.954 | 0.0507 | . |
| Kidney disease | -0.5424 | 0.8717 | ±1.7435 | -0.622 | 0.5338 |  |
| Circulatory disease | -0.8091 | 0.7003 | ±1.4006 | -1.155 | 0.2479 |  |
| Glucose SD, pooled (mg/dL) | +0.1088 | 0.0593 | ±0.1186 | +1.834 | 0.0666 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **674**, R² = **0.2942**, Adj R² = **0.2792**, F-statistic = **19.62** (p = **1.76e-41**), Residual SE = **5.685** on **659** df, AIC = **4270.2**, BIC = **4337.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5183** | 1.9620 | ±3.9240 | **+24.729** | **5.20e-135** | *** |
| **Education: graduate level (vs college)** | **+1.3370** | 0.4741 | ±0.9482 | **+2.820** | **0.0048** | ** |
| Education: high school or below (vs college) | +0.1425 | 0.9050 | ±1.8099 | +0.157 | 0.8749 |  |
| **Site: UCSD (vs UAB)** | **+3.2109** | 0.6065 | ±1.2130 | **+5.294** | **1.20e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9518** | 0.5706 | ±1.1412 | **-3.421** | **6.25e-04** | *** |
| Season: spring (vs autumn) | -0.9159 | 0.6399 | ±1.2799 | -1.431 | 0.1524 |  |
| **Season: summer (vs autumn)** | **+2.4828** | 0.6637 | ±1.3275 | **+3.741** | **1.84e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9783** | 0.6558 | ±1.3116 | **-7.591** | **3.18e-14** | *** |
| **Age (years)** | **-0.0514** | 0.0206 | ±0.0412 | **-2.493** | **0.0127** | * |
| BMI (kg/m2) | -0.0587 | 0.0345 | ±0.0690 | -1.700 | 0.0891 | . |
| Hypertension | +0.0661 | 0.5185 | ±1.0370 | +0.127 | 0.8986 |  |
| High cholesterol | -0.9346 | 0.4815 | ±0.9630 | -1.941 | 0.0523 | . |
| Kidney disease | -0.5625 | 0.8690 | ±1.7380 | -0.647 | 0.5175 |  |
| Circulatory disease | -0.8118 | 0.7001 | ±1.4002 | -1.160 | 0.2462 |  |
| Avg. daily SD (mg/dL) | +0.1146 | 0.0602 | ±0.1204 | +1.903 | 0.0570 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **674**, R² = **0.2938**, Adj R² = **0.2788**, F-statistic = **19.58** (p = **2.13e-41**), Residual SE = **5.687** on **659** df, AIC = **4270.6**, BIC = **4338.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.0217** | 2.1218 | ±4.2436 | **+22.633** | **2.06e-113** | *** |
| **Education: graduate level (vs college)** | **+1.3898** | 0.4737 | ±0.9474 | **+2.934** | **0.0033** | ** |
| Education: high school or below (vs college) | +0.1825 | 0.9022 | ±1.8044 | +0.202 | 0.8397 |  |
| **Site: UCSD (vs UAB)** | **+3.1777** | 0.6066 | ±1.2131 | **+5.239** | **1.62e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9228** | 0.5699 | ±1.1399 | **-3.374** | **7.42e-04** | *** |
| Season: spring (vs autumn) | -0.9441 | 0.6390 | ±1.2780 | -1.478 | 0.1395 |  |
| **Season: summer (vs autumn)** | **+2.4602** | 0.6617 | ±1.3235 | **+3.718** | **2.01e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0456** | 0.6559 | ±1.3118 | **-7.693** | **1.44e-14** | *** |
| **Age (years)** | **-0.0507** | 0.0207 | ±0.0414 | **-2.452** | **0.0142** | * |
| BMI (kg/m2) | -0.0541 | 0.0341 | ±0.0682 | -1.586 | 0.1128 |  |
| Hypertension | +0.0815 | 0.5173 | ±1.0346 | +0.158 | 0.8748 |  |
| High cholesterol | -0.9352 | 0.4817 | ±0.9633 | -1.942 | 0.0522 | . |
| Kidney disease | -0.5118 | 0.8729 | ±1.7458 | -0.586 | 0.5577 |  |
| Circulatory disease | -0.7708 | 0.6987 | ±1.3973 | -1.103 | 0.2699 |  |
| CV (%) | +0.1447 | 0.0824 | ±0.1648 | +1.756 | 0.0792 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **674**, R² = **0.2923**, Adj R² = **0.2772**, F-statistic = **19.44** (p = **4.19e-41**), Residual SE = **5.693** on **659** df, AIC = **4272.1**, BIC = **4339.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.9864** | 2.2146 | ±4.4292 | **+23.474** | **7.44e-122** | *** |
| **Education: graduate level (vs college)** | **+1.3737** | 0.4741 | ±0.9482 | **+2.898** | **0.0038** | ** |
| Education: high school or below (vs college) | +0.1739 | 0.9053 | ±1.8106 | +0.192 | 0.8477 |  |
| **Site: UCSD (vs UAB)** | **+3.1545** | 0.6079 | ±1.2158 | **+5.189** | **2.11e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9248** | 0.5721 | ±1.1441 | **-3.365** | **7.67e-04** | *** |
| Season: spring (vs autumn) | -0.9549 | 0.6394 | ±1.2788 | -1.493 | 0.1353 |  |
| **Season: summer (vs autumn)** | **+2.4695** | 0.6639 | ±1.3278 | **+3.720** | **1.99e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0330** | 0.6567 | ±1.3134 | **-7.664** | **1.80e-14** | *** |
| **Age (years)** | **-0.0496** | 0.0208 | ±0.0415 | **-2.392** | **0.0168** | * |
| BMI (kg/m2) | -0.0543 | 0.0341 | ±0.0681 | -1.594 | 0.1110 |  |
| Hypertension | +0.0875 | 0.5182 | ±1.0364 | +0.169 | 0.8660 |  |
| High cholesterol | -0.9277 | 0.4818 | ±0.9636 | -1.925 | 0.0542 | . |
| Kidney disease | -0.5074 | 0.8749 | ±1.7498 | -0.580 | 0.5620 |  |
| Circulatory disease | -0.7825 | 0.7013 | ±1.4027 | -1.116 | 0.2645 |  |
| Mean / SD ratio | -0.2631 | 0.2062 | ±0.4125 | -1.276 | 0.2021 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **674**, R² = **0.2938**, Adj R² = **0.2788**, F-statistic = **19.58** (p = **2.15e-41**), Residual SE = **5.687** on **659** df, AIC = **4270.6**, BIC = **4338.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4589** | 2.1891 | ±4.3782 | **+23.964** | **6.68e-127** | *** |
| **Education: graduate level (vs college)** | **+1.3768** | 0.4722 | ±0.9444 | **+2.916** | **0.0036** | ** |
| Education: high school or below (vs college) | +0.1673 | 0.9051 | ±1.8103 | +0.185 | 0.8534 |  |
| **Site: UCSD (vs UAB)** | **+3.1722** | 0.6051 | ±1.2103 | **+5.242** | **1.59e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9381** | 0.5718 | ±1.1436 | **-3.390** | **7.00e-04** | *** |
| Season: spring (vs autumn) | -0.9481 | 0.6375 | ±1.2750 | -1.487 | 0.1370 |  |
| **Season: summer (vs autumn)** | **+2.4879** | 0.6620 | ±1.3241 | **+3.758** | **1.71e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0132** | 0.6542 | ±1.3084 | **-7.663** | **1.82e-14** | *** |
| **Age (years)** | **-0.0506** | 0.0207 | ±0.0413 | **-2.448** | **0.0144** | * |
| BMI (kg/m2) | -0.0563 | 0.0343 | ±0.0687 | -1.638 | 0.1015 |  |
| Hypertension | +0.0989 | 0.5163 | ±1.0325 | +0.192 | 0.8481 |  |
| High cholesterol | -0.9185 | 0.4825 | ±0.9650 | -1.903 | 0.0570 | . |
| Kidney disease | -0.5273 | 0.8710 | ±1.7420 | -0.605 | 0.5449 |  |
| Circulatory disease | -0.7698 | 0.6977 | ±1.3954 | -1.103 | 0.2699 |  |
| Avg. daily mean/SD | -0.2842 | 0.1728 | ±0.3457 | -1.644 | 0.1001 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **674**, R² = **0.2906**, Adj R² = **0.2755**, F-statistic = **19.28** (p = **8.92e-41**), Residual SE = **5.700** on **659** df, AIC = **4273.7**, BIC = **4341.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.7365** | 2.1037 | ±4.2074 | **+24.118** | **1.62e-128** | *** |
| **Education: graduate level (vs college)** | **+1.3185** | 0.4751 | ±0.9502 | **+2.775** | **0.0055** | ** |
| Education: high school or below (vs college) | +0.2074 | 0.9184 | ±1.8368 | +0.226 | 0.8213 |  |
| **Site: UCSD (vs UAB)** | **+3.1164** | 0.6123 | ±1.2247 | **+5.089** | **3.59e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9054** | 0.5740 | ±1.1480 | **-3.319** | **9.02e-04** | *** |
| Season: spring (vs autumn) | -0.9255 | 0.6431 | ±1.2861 | -1.439 | 0.1501 |  |
| **Season: summer (vs autumn)** | **+2.4656** | 0.6668 | ±1.3336 | **+3.698** | **2.17e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9924** | 0.6545 | ±1.3090 | **-7.628** | **2.38e-14** | *** |
| **Age (years)** | **-0.0478** | 0.0208 | ±0.0415 | **-2.303** | **0.0213** | * |
| BMI (kg/m2) | -0.0550 | 0.0341 | ±0.0681 | -1.614 | 0.1066 |  |
| Hypertension | +0.1042 | 0.5181 | ±1.0362 | +0.201 | 0.8406 |  |
| High cholesterol | -0.9277 | 0.4814 | ±0.9629 | -1.927 | 0.0540 | . |
| Kidney disease | -0.4774 | 0.8831 | ±1.7662 | -0.541 | 0.5888 |  |
| Circulatory disease | -0.8220 | 0.7070 | ±1.4140 | -1.163 | 0.2449 |  |
| MAG (mg/dL/h) | -0.0144 | 0.0340 | ±0.0680 | -0.424 | 0.6714 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **674**, R² = **0.2917**, Adj R² = **0.2767**, F-statistic = **19.39** (p = **5.34e-41**), Residual SE = **5.695** on **659** df, AIC = **4272.6**, BIC = **4340.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.8951** | 2.0939 | ±4.1878 | **+23.351** | **1.34e-120** | *** |
| **Education: graduate level (vs college)** | **+1.3116** | 0.4759 | ±0.9517 | **+2.756** | **0.0058** | ** |
| Education: high school or below (vs college) | +0.1427 | 0.9063 | ±1.8126 | +0.157 | 0.8749 |  |
| **Site: UCSD (vs UAB)** | **+3.1586** | 0.6082 | ±1.2165 | **+5.193** | **2.07e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9293** | 0.5747 | ±1.1495 | **-3.357** | **7.89e-04** | *** |
| Season: spring (vs autumn) | -0.9348 | 0.6388 | ±1.2776 | -1.463 | 0.1434 |  |
| **Season: summer (vs autumn)** | **+2.4897** | 0.6639 | ±1.3277 | **+3.750** | **1.77e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9843** | 0.6559 | ±1.3119 | **-7.599** | **2.99e-14** | *** |
| **Age (years)** | **-0.0494** | 0.0207 | ±0.0414 | **-2.385** | **0.0171** | * |
| BMI (kg/m2) | -0.0534 | 0.0341 | ±0.0681 | -1.569 | 0.1168 |  |
| Hypertension | +0.1025 | 0.5194 | ±1.0388 | +0.197 | 0.8436 |  |
| High cholesterol | -0.9204 | 0.4828 | ±0.9656 | -1.906 | 0.0566 | . |
| Kidney disease | -0.5372 | 0.8736 | ±1.7472 | -0.615 | 0.5386 |  |
| Circulatory disease | -0.8290 | 0.7052 | ±1.4104 | -1.176 | 0.2397 |  |
| Avg. daily range (mg/dL) | +0.0155 | 0.0141 | ±0.0281 | +1.099 | 0.2717 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **674**, R² = **0.2917**, Adj R² = **0.2766**, F-statistic = **19.38** (p = **5.46e-41**), Residual SE = **5.695** on **659** df, AIC = **4272.6**, BIC = **4340.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.7234** | 1.7437 | ±3.4874 | **+28.516** | **7.47e-179** | *** |
| **Education: graduate level (vs college)** | **+1.3233** | 0.4758 | ±0.9517 | **+2.781** | **0.0054** | ** |
| Education: high school or below (vs college) | +0.1709 | 0.9093 | ±1.8186 | +0.188 | 0.8509 |  |
| **Site: UCSD (vs UAB)** | **+3.1354** | 0.6119 | ±1.2239 | **+5.124** | **3.00e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9168** | 0.5721 | ±1.1441 | **-3.351** | **8.06e-04** | *** |
| Season: spring (vs autumn) | -0.9696 | 0.6454 | ±1.2908 | -1.502 | 0.1330 |  |
| **Season: summer (vs autumn)** | **+2.4082** | 0.6692 | ±1.3385 | **+3.598** | **3.20e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0358** | 0.6586 | ±1.3172 | **-7.646** | **2.07e-14** | *** |
| **Age (years)** | **-0.0477** | 0.0208 | ±0.0415 | **-2.298** | **0.0216** | * |
| BMI (kg/m2) | -0.0585 | 0.0344 | ±0.0687 | -1.703 | 0.0886 | . |
| Hypertension | +0.1171 | 0.5196 | ±1.0391 | +0.225 | 0.8217 |  |
| **High cholesterol** | **-0.9599** | 0.4814 | ±0.9628 | **-1.994** | **0.0462** | * |
| Kidney disease | -0.4527 | 0.8799 | ±1.7598 | -0.514 | 0.6069 |  |
| Circulatory disease | -0.8317 | 0.7000 | ±1.3999 | -1.188 | 0.2348 |  |
| SD of daily means (mg/dL) | +0.1088 | 0.1053 | ±0.2105 | +1.034 | 0.3012 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **674**, R² = **0.2915**, Adj R² = **0.2765**, F-statistic = **19.37** (p = **5.85e-41**), Residual SE = **5.696** on **659** df, AIC = **4272.8**, BIC = **4340.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.7430** | 7.7202 | ±15.4404 | **+7.609** | **2.76e-14** | *** |
| **Education: graduate level (vs college)** | **+1.3126** | 0.4756 | ±0.9511 | **+2.760** | **0.0058** | ** |
| Education: high school or below (vs college) | +0.1830 | 0.9078 | ±1.8156 | +0.202 | 0.8402 |  |
| **Site: UCSD (vs UAB)** | **+3.1658** | 0.6141 | ±1.2282 | **+5.155** | **2.53e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9227** | 0.5727 | ±1.1454 | **-3.357** | **7.87e-04** | *** |
| Season: spring (vs autumn) | -0.9114 | 0.6430 | ±1.2861 | -1.417 | 0.1564 |  |
| **Season: summer (vs autumn)** | **+2.4828** | 0.6663 | ±1.3326 | **+3.726** | **1.94e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9704** | 0.6552 | ±1.3105 | **-7.586** | **3.31e-14** | *** |
| **Age (years)** | **-0.0489** | 0.0207 | ±0.0415 | **-2.359** | **0.0183** | * |
| BMI (kg/m2) | -0.0564 | 0.0342 | ±0.0685 | -1.647 | 0.0995 | . |
| Hypertension | +0.1051 | 0.5181 | ±1.0361 | +0.203 | 0.8392 |  |
| **High cholesterol** | **-0.9545** | 0.4811 | ±0.9623 | **-1.984** | **0.0473** | * |
| Kidney disease | -0.5232 | 0.8740 | ±1.7481 | -0.599 | 0.5494 |  |
| Circulatory disease | -0.8481 | 0.7063 | ±1.4126 | -1.201 | 0.2298 |  |
| Time in range 70-180, pooled (%) | -0.0859 | 0.0765 | ±0.1530 | -1.122 | 0.2617 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **674**, R² = **0.2917**, Adj R² = **0.2767**, F-statistic = **19.39** (p = **5.36e-41**), Residual SE = **5.695** on **659** df, AIC = **4272.6**, BIC = **4340.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.6582** | 7.8600 | ±15.7200 | **+7.590** | **3.20e-14** | *** |
| **Education: graduate level (vs college)** | **+1.3115** | 0.4755 | ±0.9510 | **+2.758** | **0.0058** | ** |
| Education: high school or below (vs college) | +0.1858 | 0.9083 | ±1.8166 | +0.205 | 0.8379 |  |
| **Site: UCSD (vs UAB)** | **+3.1704** | 0.6143 | ±1.2287 | **+5.161** | **2.46e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9205** | 0.5726 | ±1.1451 | **-3.354** | **7.96e-04** | *** |
| Season: spring (vs autumn) | -0.9103 | 0.6429 | ±1.2858 | -1.416 | 0.1568 |  |
| **Season: summer (vs autumn)** | **+2.4827** | 0.6661 | ±1.3321 | **+3.727** | **1.93e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9657** | 0.6553 | ±1.3106 | **-7.578** | **3.52e-14** | *** |
| **Age (years)** | **-0.0488** | 0.0207 | ±0.0414 | **-2.359** | **0.0183** | * |
| BMI (kg/m2) | -0.0570 | 0.0343 | ±0.0687 | -1.660 | 0.0969 | . |
| Hypertension | +0.1075 | 0.5180 | ±1.0360 | +0.207 | 0.8356 |  |
| **High cholesterol** | **-0.9575** | 0.4812 | ±0.9625 | **-1.990** | **0.0466** | * |
| Kidney disease | -0.5300 | 0.8727 | ±1.7455 | -0.607 | 0.5437 |  |
| Circulatory disease | -0.8561 | 0.7065 | ±1.4129 | -1.212 | 0.2256 |  |
| Avg. daily time in range 70-180 (%) | -0.0950 | 0.0783 | ±0.1566 | -1.213 | 0.2252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **674**, R² = **0.2905**, Adj R² = **0.2754**, F-statistic = **19.27** (p = **9.14e-41**), Residual SE = **5.700** on **659** df, AIC = **4273.7**, BIC = **4341.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1462** | 1.7060 | ±3.4120 | **+29.394** | **6.60e-190** | *** |
| **Education: graduate level (vs college)** | **+1.3367** | 0.4762 | ±0.9524 | **+2.807** | **0.0050** | ** |
| Education: high school or below (vs college) | +0.2055 | 0.9083 | ±1.8165 | +0.226 | 0.8210 |  |
| **Site: UCSD (vs UAB)** | **+3.1185** | 0.6108 | ±1.2217 | **+5.105** | **3.30e-07** | *** |
| **Site: UW (vs UAB)** | **-1.8966** | 0.5746 | ±1.1491 | **-3.301** | **9.64e-04** | *** |
| Season: spring (vs autumn) | -0.9321 | 0.6414 | ±1.2828 | -1.453 | 0.1461 |  |
| **Season: summer (vs autumn)** | **+2.4662** | 0.6638 | ±1.3277 | **+3.715** | **2.03e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0014** | 0.6556 | ±1.3112 | **-7.629** | **2.37e-14** | *** |
| **Age (years)** | **-0.0476** | 0.0208 | ±0.0415 | **-2.291** | **0.0220** | * |
| BMI (kg/m2) | -0.0545 | 0.0340 | ±0.0681 | -1.601 | 0.1093 |  |
| Hypertension | +0.1102 | 0.5189 | ±1.0379 | +0.212 | 0.8319 |  |
| High cholesterol | -0.9291 | 0.4816 | ±0.9632 | -1.929 | 0.0537 | . |
| Kidney disease | -0.4859 | 0.8778 | ±1.7557 | -0.554 | 0.5799 |  |
| Circulatory disease | -0.8070 | 0.7064 | ±1.4128 | -1.142 | 0.2533 |  |
| Time 54-69, pooled (%) | +0.1591 | 0.4473 | ±0.8946 | +0.356 | 0.7220 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **674**, R² = **0.2904**, Adj R² = **0.2754**, F-statistic = **19.27** (p = **9.47e-41**), Residual SE = **5.700** on **659** df, AIC = **4273.8**, BIC = **4341.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1654** | 1.7044 | ±3.4088 | **+29.433** | **2.09e-190** | *** |
| **Education: graduate level (vs college)** | **+1.3313** | 0.4761 | ±0.9522 | **+2.796** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.1989 | 0.9085 | ±1.8170 | +0.219 | 0.8267 |  |
| **Site: UCSD (vs UAB)** | **+3.1184** | 0.6108 | ±1.2217 | **+5.105** | **3.31e-07** | *** |
| **Site: UW (vs UAB)** | **-1.8987** | 0.5744 | ±1.1488 | **-3.306** | **9.48e-04** | *** |
| Season: spring (vs autumn) | -0.9294 | 0.6415 | ±1.2830 | -1.449 | 0.1474 |  |
| **Season: summer (vs autumn)** | **+2.4703** | 0.6642 | ±1.3284 | **+3.719** | **2.00e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9982** | 0.6558 | ±1.3116 | **-7.622** | **2.51e-14** | *** |
| **Age (years)** | **-0.0476** | 0.0208 | ±0.0415 | **-2.294** | **0.0218** | * |
| BMI (kg/m2) | -0.0546 | 0.0340 | ±0.0681 | -1.603 | 0.1089 |  |
| Hypertension | +0.1115 | 0.5190 | ±1.0381 | +0.215 | 0.8299 |  |
| High cholesterol | -0.9275 | 0.4815 | ±0.9631 | -1.926 | 0.0541 | . |
| Kidney disease | -0.4890 | 0.8782 | ±1.7563 | -0.557 | 0.5776 |  |
| Circulatory disease | -0.8081 | 0.7074 | ±1.4147 | -1.142 | 0.2533 |  |
| Avg. daily time 54-69 (%) | +0.1059 | 0.4315 | ±0.8631 | +0.245 | 0.8061 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **674**, R² = **0.2905**, Adj R² = **0.2754**, F-statistic = **19.27** (p = **9.14e-41**), Residual SE = **5.700** on **659** df, AIC = **4273.7**, BIC = **4341.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1462** | 1.7060 | ±3.4120 | **+29.394** | **6.60e-190** | *** |
| **Education: graduate level (vs college)** | **+1.3367** | 0.4762 | ±0.9524 | **+2.807** | **0.0050** | ** |
| Education: high school or below (vs college) | +0.2055 | 0.9083 | ±1.8165 | +0.226 | 0.8210 |  |
| **Site: UCSD (vs UAB)** | **+3.1185** | 0.6108 | ±1.2217 | **+5.105** | **3.30e-07** | *** |
| **Site: UW (vs UAB)** | **-1.8966** | 0.5746 | ±1.1491 | **-3.301** | **9.64e-04** | *** |
| Season: spring (vs autumn) | -0.9321 | 0.6414 | ±1.2828 | -1.453 | 0.1461 |  |
| **Season: summer (vs autumn)** | **+2.4662** | 0.6638 | ±1.3277 | **+3.715** | **2.03e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0014** | 0.6556 | ±1.3112 | **-7.629** | **2.37e-14** | *** |
| **Age (years)** | **-0.0476** | 0.0208 | ±0.0415 | **-2.291** | **0.0220** | * |
| BMI (kg/m2) | -0.0545 | 0.0340 | ±0.0681 | -1.601 | 0.1093 |  |
| Hypertension | +0.1102 | 0.5189 | ±1.0379 | +0.212 | 0.8319 |  |
| High cholesterol | -0.9291 | 0.4816 | ±0.9632 | -1.929 | 0.0537 | . |
| Kidney disease | -0.4859 | 0.8778 | ±1.7557 | -0.554 | 0.5799 |  |
| Circulatory disease | -0.8070 | 0.7064 | ±1.4128 | -1.142 | 0.2533 |  |
| Time < 70 (%) | +0.1591 | 0.4473 | ±0.8946 | +0.356 | 0.7220 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **674**, R² = **0.2904**, Adj R² = **0.2754**, F-statistic = **19.27** (p = **9.47e-41**), Residual SE = **5.700** on **659** df, AIC = **4273.8**, BIC = **4341.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1654** | 1.7044 | ±3.4088 | **+29.433** | **2.09e-190** | *** |
| **Education: graduate level (vs college)** | **+1.3313** | 0.4761 | ±0.9522 | **+2.796** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.1989 | 0.9085 | ±1.8170 | +0.219 | 0.8267 |  |
| **Site: UCSD (vs UAB)** | **+3.1184** | 0.6108 | ±1.2217 | **+5.105** | **3.31e-07** | *** |
| **Site: UW (vs UAB)** | **-1.8987** | 0.5744 | ±1.1488 | **-3.306** | **9.48e-04** | *** |
| Season: spring (vs autumn) | -0.9294 | 0.6415 | ±1.2830 | -1.449 | 0.1474 |  |
| **Season: summer (vs autumn)** | **+2.4703** | 0.6642 | ±1.3284 | **+3.719** | **2.00e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9982** | 0.6558 | ±1.3116 | **-7.622** | **2.51e-14** | *** |
| **Age (years)** | **-0.0476** | 0.0208 | ±0.0415 | **-2.294** | **0.0218** | * |
| BMI (kg/m2) | -0.0546 | 0.0340 | ±0.0681 | -1.603 | 0.1089 |  |
| Hypertension | +0.1115 | 0.5190 | ±1.0381 | +0.215 | 0.8299 |  |
| High cholesterol | -0.9275 | 0.4815 | ±0.9631 | -1.926 | 0.0541 | . |
| Kidney disease | -0.4890 | 0.8782 | ±1.7563 | -0.557 | 0.5776 |  |
| Circulatory disease | -0.8081 | 0.7074 | ±1.4147 | -1.142 | 0.2533 |  |
| Avg. daily time < 70 (%) | +0.1059 | 0.4315 | ±0.8631 | +0.245 | 0.8061 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **674**, R² = **0.2914**, Adj R² = **0.2763**, F-statistic = **19.35** (p = **6.31e-41**), Residual SE = **5.697** on **659** df, AIC = **4272.9**, BIC = **4340.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1853** | 1.7029 | ±3.4058 | **+29.471** | **6.81e-191** | *** |
| **Education: graduate level (vs college)** | **+1.3038** | 0.4762 | ±0.9523 | **+2.738** | **0.0062** | ** |
| Education: high school or below (vs college) | +0.1715 | 0.9082 | ±1.8164 | +0.189 | 0.8502 |  |
| **Site: UCSD (vs UAB)** | **+3.1662** | 0.6143 | ±1.2285 | **+5.154** | **2.54e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9235** | 0.5729 | ±1.1457 | **-3.358** | **7.86e-04** | *** |
| Season: spring (vs autumn) | -0.9111 | 0.6435 | ±1.2870 | -1.416 | 0.1568 |  |
| **Season: summer (vs autumn)** | **+2.4864** | 0.6668 | ±1.3335 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9654** | 0.6556 | ±1.3111 | **-7.574** | **3.61e-14** | *** |
| **Age (years)** | **-0.0489** | 0.0207 | ±0.0415 | **-2.355** | **0.0185** | * |
| BMI (kg/m2) | -0.0564 | 0.0342 | ±0.0685 | -1.648 | 0.0994 | . |
| Hypertension | +0.1072 | 0.5183 | ±1.0366 | +0.207 | 0.8362 |  |
| **High cholesterol** | **-0.9503** | 0.4812 | ±0.9624 | **-1.975** | **0.0483** | * |
| Kidney disease | -0.5240 | 0.8746 | ±1.7492 | -0.599 | 0.5491 |  |
| Circulatory disease | -0.8506 | 0.7069 | ±1.4137 | -1.203 | 0.2289 |  |
| Time 181-250, pooled (%) | +0.0789 | 0.0767 | ±0.1533 | +1.030 | 0.3032 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **674**, R² = **0.2916**, Adj R² = **0.2765**, F-statistic = **19.37** (p = **5.70e-41**), Residual SE = **5.696** on **659** df, AIC = **4272.7**, BIC = **4340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1886** | 1.7055 | ±3.4109 | **+29.428** | **2.39e-190** | *** |
| **Education: graduate level (vs college)** | **+1.3006** | 0.4761 | ±0.9522 | **+2.732** | **0.0063** | ** |
| Education: high school or below (vs college) | +0.1716 | 0.9086 | ±1.8173 | +0.189 | 0.8502 |  |
| **Site: UCSD (vs UAB)** | **+3.1740** | 0.6148 | ±1.2296 | **+5.163** | **2.43e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9218** | 0.5727 | ±1.1454 | **-3.356** | **7.92e-04** | *** |
| Season: spring (vs autumn) | -0.9108 | 0.6432 | ±1.2864 | -1.416 | 0.1568 |  |
| **Season: summer (vs autumn)** | **+2.4861** | 0.6666 | ±1.3332 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9586** | 0.6559 | ±1.3117 | **-7.561** | **4.01e-14** | *** |
| **Age (years)** | **-0.0488** | 0.0207 | ±0.0414 | **-2.356** | **0.0185** | * |
| BMI (kg/m2) | -0.0570 | 0.0343 | ±0.0686 | -1.662 | 0.0966 | . |
| Hypertension | +0.1091 | 0.5183 | ±1.0366 | +0.211 | 0.8332 |  |
| **High cholesterol** | **-0.9538** | 0.4813 | ±0.9626 | **-1.982** | **0.0475** | * |
| Kidney disease | -0.5307 | 0.8734 | ±1.7468 | -0.608 | 0.5434 |  |
| Circulatory disease | -0.8613 | 0.7073 | ±1.4147 | -1.218 | 0.2233 |  |
| Avg. daily time 181-250 (%) | +0.0897 | 0.0785 | ±0.1571 | +1.142 | 0.2535 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **674**, R² = **0.2914**, Adj R² = **0.2763**, F-statistic = **19.35** (p = **6.31e-41**), Residual SE = **5.697** on **659** df, AIC = **4272.9**, BIC = **4340.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1853** | 1.7029 | ±3.4058 | **+29.471** | **6.81e-191** | *** |
| **Education: graduate level (vs college)** | **+1.3038** | 0.4762 | ±0.9523 | **+2.738** | **0.0062** | ** |
| Education: high school or below (vs college) | +0.1715 | 0.9082 | ±1.8164 | +0.189 | 0.8502 |  |
| **Site: UCSD (vs UAB)** | **+3.1662** | 0.6143 | ±1.2285 | **+5.154** | **2.54e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9235** | 0.5729 | ±1.1457 | **-3.358** | **7.86e-04** | *** |
| Season: spring (vs autumn) | -0.9111 | 0.6435 | ±1.2870 | -1.416 | 0.1568 |  |
| **Season: summer (vs autumn)** | **+2.4864** | 0.6668 | ±1.3335 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9654** | 0.6556 | ±1.3111 | **-7.574** | **3.61e-14** | *** |
| **Age (years)** | **-0.0489** | 0.0207 | ±0.0415 | **-2.355** | **0.0185** | * |
| BMI (kg/m2) | -0.0564 | 0.0342 | ±0.0685 | -1.648 | 0.0994 | . |
| Hypertension | +0.1072 | 0.5183 | ±1.0366 | +0.207 | 0.8362 |  |
| **High cholesterol** | **-0.9503** | 0.4812 | ±0.9624 | **-1.975** | **0.0483** | * |
| Kidney disease | -0.5240 | 0.8746 | ±1.7492 | -0.599 | 0.5491 |  |
| Circulatory disease | -0.8506 | 0.7069 | ±1.4137 | -1.203 | 0.2289 |  |
| Time > 180 (%) | +0.0789 | 0.0767 | ±0.1533 | +1.030 | 0.3032 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **674**, R² = **0.2916**, Adj R² = **0.2765**, F-statistic = **19.37** (p = **5.70e-41**), Residual SE = **5.696** on **659** df, AIC = **4272.7**, BIC = **4340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1886** | 1.7055 | ±3.4109 | **+29.428** | **2.39e-190** | *** |
| **Education: graduate level (vs college)** | **+1.3006** | 0.4761 | ±0.9522 | **+2.732** | **0.0063** | ** |
| Education: high school or below (vs college) | +0.1716 | 0.9086 | ±1.8173 | +0.189 | 0.8502 |  |
| **Site: UCSD (vs UAB)** | **+3.1740** | 0.6148 | ±1.2296 | **+5.163** | **2.43e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9218** | 0.5727 | ±1.1454 | **-3.356** | **7.92e-04** | *** |
| Season: spring (vs autumn) | -0.9108 | 0.6432 | ±1.2864 | -1.416 | 0.1568 |  |
| **Season: summer (vs autumn)** | **+2.4861** | 0.6666 | ±1.3332 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9586** | 0.6559 | ±1.3117 | **-7.561** | **4.01e-14** | *** |
| **Age (years)** | **-0.0488** | 0.0207 | ±0.0414 | **-2.356** | **0.0185** | * |
| BMI (kg/m2) | -0.0570 | 0.0343 | ±0.0686 | -1.662 | 0.0966 | . |
| Hypertension | +0.1091 | 0.5183 | ±1.0366 | +0.211 | 0.8332 |  |
| **High cholesterol** | **-0.9538** | 0.4813 | ±0.9626 | **-1.982** | **0.0475** | * |
| Kidney disease | -0.5307 | 0.8734 | ±1.7468 | -0.608 | 0.5434 |  |
| Circulatory disease | -0.8613 | 0.7073 | ±1.4147 | -1.218 | 0.2233 |  |
| Avg. daily time > 180 (%) | +0.0897 | 0.0785 | ±0.1571 | +1.142 | 0.2535 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 674)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **674**, R² = **0.2918**, Adj R² = **0.2767**, F-statistic = **19.39** (p = **5.28e-41**), Residual SE = **5.695** on **659** df, AIC = **4272.6**, BIC = **4340.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2288** | 1.7014 | ±3.4028 | **+29.522** | **1.52e-191** | *** |
| **Education: graduate level (vs college)** | **+1.3238** | 0.4746 | ±0.9493 | **+2.789** | **0.0053** | ** |
| Education: high school or below (vs college) | +0.1529 | 0.9096 | ±1.8191 | +0.168 | 0.8665 |  |
| **Site: UCSD (vs UAB)** | **+3.1496** | 0.6117 | ±1.2235 | **+5.148** | **2.63e-07** | *** |
| **Site: UW (vs UAB)** | **-1.9206** | 0.5735 | ±1.1470 | **-3.349** | **8.11e-04** | *** |
| Season: spring (vs autumn) | -0.9239 | 0.6416 | ±1.2831 | -1.440 | 0.1498 |  |
| **Season: summer (vs autumn)** | **+2.4754** | 0.6652 | ±1.3304 | **+3.721** | **1.98e-04** | *** |
| **Season: winter (vs autumn)** | **-4.9936** | 0.6538 | ±1.3075 | **-7.638** | **2.20e-14** | *** |
| **Age (years)** | **-0.0469** | 0.0208 | ±0.0415 | **-2.259** | **0.0239** | * |
| BMI (kg/m2) | -0.0596 | 0.0344 | ±0.0687 | -1.735 | 0.0828 | . |
| Hypertension | +0.1275 | 0.5197 | ±1.0394 | +0.245 | 0.8062 |  |
| **High cholesterol** | **-0.9788** | 0.4831 | ±0.9662 | **-2.026** | **0.0428** | * |
| Kidney disease | -0.4874 | 0.8802 | ±1.7604 | -0.554 | 0.5797 |  |
| Circulatory disease | -0.8162 | 0.7074 | ±1.4149 | -1.154 | 0.2486 |  |
| Nocturnal time > 180 (%) | +0.0822 | 0.0517 | ±0.1035 | +1.588 | 0.1122 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 674; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **674**, R² = **0.0365**, Adj R² = **0.0175**, F-statistic = **1.92** (p = **0.0249**), Residual SE = **15.454** on **660** df, AIC = **5617.3**, BIC = **5680.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2048** | 5.0857 | ±10.1714 | **+24.816** | **6.07e-136** | *** |
| Education: graduate level (vs college) | -2.0995 | 1.2822 | ±2.5645 | -1.637 | 0.1016 |  |
| Education: high school or below (vs college) | +3.6796 | 2.4478 | ±4.8956 | +1.503 | 0.1328 |  |
| Site: UCSD (vs UAB) | +0.7597 | 1.6229 | ±3.2458 | +0.468 | 0.6397 |  |
| Site: UW (vs UAB) | +0.0850 | 1.5766 | ±3.1532 | +0.054 | 0.9570 |  |
| Season: spring (vs autumn) | +3.0633 | 1.7026 | ±3.4052 | +1.799 | 0.0720 | . |
| Season: summer (vs autumn) | +2.4448 | 1.8092 | ±3.6185 | +1.351 | 0.1766 |  |
| **Season: winter (vs autumn)** | **+4.0573** | 1.7581 | ±3.5163 | **+2.308** | **0.0210** | * |
| Age (years) | -0.1135 | 0.0617 | ±0.1234 | -1.840 | 0.0657 | . |
| BMI (kg/m2) | +0.1643 | 0.0840 | ±0.1679 | +1.957 | 0.0504 | . |
| Hypertension | +0.7416 | 1.4143 | ±2.8285 | +0.524 | 0.6000 |  |
| High cholesterol | -0.1060 | 1.2796 | ±2.5591 | -0.083 | 0.9340 |  |
| Kidney disease | -1.0472 | 2.0363 | ±4.0726 | -0.514 | 0.6071 |  |
| Circulatory disease | +1.0222 | 2.0455 | ±4.0909 | +0.500 | 0.6172 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **674**, R² = **0.0372**, Adj R² = **0.0168**, F-statistic = **1.82** (p = **0.0323**), Residual SE = **15.460** on **659** df, AIC = **5618.7**, BIC = **5686.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+133.1489** | 11.7826 | ±23.5652 | **+11.300** | **1.31e-29** | *** |
| Education: graduate level (vs college) | -2.0831 | 1.2822 | ±2.5644 | -1.625 | 0.1042 |  |
| Education: high school or below (vs college) | +3.7033 | 2.4434 | ±4.8867 | +1.516 | 0.1296 |  |
| Site: UCSD (vs UAB) | +0.7616 | 1.6250 | ±3.2501 | +0.469 | 0.6393 |  |
| Site: UW (vs UAB) | +0.1100 | 1.5838 | ±3.1676 | +0.069 | 0.9446 |  |
| Season: spring (vs autumn) | +2.8686 | 1.7478 | ±3.4955 | +1.641 | 0.1007 |  |
| Season: summer (vs autumn) | +2.4126 | 1.8262 | ±3.6524 | +1.321 | 0.1865 |  |
| **Season: winter (vs autumn)** | **+3.9447** | 1.7824 | ±3.5649 | **+2.213** | **0.0269** | * |
| Age (years) | -0.1083 | 0.0623 | ±0.1247 | -1.738 | 0.0822 | . |
| **BMI (kg/m2)** | **+0.1733** | 0.0844 | ±0.1688 | **+2.054** | **0.0400** | * |
| Hypertension | +0.8156 | 1.4244 | ±2.8488 | +0.573 | 0.5669 |  |
| High cholesterol | -0.0047 | 1.3166 | ±2.6332 | -0.004 | 0.9972 |  |
| Kidney disease | -1.0296 | 2.0484 | ±4.0967 | -0.503 | 0.6152 |  |
| Circulatory disease | +0.9588 | 2.0694 | ±4.1388 | +0.463 | 0.6431 |  |
| HbA1c (%) | -1.3437 | 2.0567 | ±4.1135 | -0.653 | 0.5136 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **674**, R² = **0.0443**, Adj R² = **0.0240**, F-statistic = **2.18** (p = **0.0074**), Residual SE = **15.404** on **659** df, AIC = **5613.8**, BIC = **5681.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+139.9520** | 7.8225 | ±15.6450 | **+17.891** | **1.39e-71** | *** |
| Education: graduate level (vs college) | -1.9004 | 1.2841 | ±2.5683 | -1.480 | 0.1389 |  |
| Education: high school or below (vs college) | +3.8865 | 2.4469 | ±4.8938 | +1.588 | 0.1122 |  |
| Site: UCSD (vs UAB) | +0.5684 | 1.6178 | ±3.2357 | +0.351 | 0.7253 |  |
| Site: UW (vs UAB) | +0.3090 | 1.5727 | ±3.1453 | +0.196 | 0.8443 |  |
| Season: spring (vs autumn) | +2.9927 | 1.6927 | ±3.3854 | +1.768 | 0.0771 | . |
| Season: summer (vs autumn) | +2.4769 | 1.8139 | ±3.6278 | +1.366 | 0.1721 |  |
| **Season: winter (vs autumn)** | **+3.9177** | 1.7543 | ±3.5087 | **+2.233** | **0.0255** | * |
| Age (years) | -0.1074 | 0.0619 | ±0.1237 | -1.737 | 0.0824 | . |
| **BMI (kg/m2)** | **+0.1884** | 0.0831 | ±0.1662 | **+2.266** | **0.0234** | * |
| Hypertension | +0.9438 | 1.4098 | ±2.8197 | +0.669 | 0.5032 |  |
| High cholesterol | -0.1070 | 1.2796 | ±2.5593 | -0.084 | 0.9334 |  |
| Kidney disease | -0.7899 | 2.0680 | ±4.1359 | -0.382 | 0.7025 |  |
| Circulatory disease | +1.2740 | 2.0515 | ±4.1031 | +0.621 | 0.5346 |  |
| **Mean glucose (mg/dL)** | **-0.1258** | 0.0559 | ±0.1119 | **-2.250** | **0.0245** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **674**, R² = **0.0443**, Adj R² = **0.0240**, F-statistic = **2.18** (p = **0.0074**), Residual SE = **15.404** on **659** df, AIC = **5613.8**, BIC = **5681.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+157.3660** | 14.6173 | ±29.2347 | **+10.766** | **5.00e-27** | *** |
| Education: graduate level (vs college) | -1.9004 | 1.2841 | ±2.5683 | -1.480 | 0.1389 |  |
| Education: high school or below (vs college) | +3.8865 | 2.4469 | ±4.8938 | +1.588 | 0.1122 |  |
| Site: UCSD (vs UAB) | +0.5684 | 1.6178 | ±3.2357 | +0.351 | 0.7253 |  |
| Site: UW (vs UAB) | +0.3090 | 1.5727 | ±3.1453 | +0.196 | 0.8443 |  |
| Season: spring (vs autumn) | +2.9927 | 1.6927 | ±3.3854 | +1.768 | 0.0771 | . |
| Season: summer (vs autumn) | +2.4769 | 1.8139 | ±3.6278 | +1.366 | 0.1721 |  |
| **Season: winter (vs autumn)** | **+3.9177** | 1.7543 | ±3.5087 | **+2.233** | **0.0255** | * |
| Age (years) | -0.1074 | 0.0619 | ±0.1237 | -1.737 | 0.0824 | . |
| **BMI (kg/m2)** | **+0.1884** | 0.0831 | ±0.1662 | **+2.266** | **0.0234** | * |
| Hypertension | +0.9438 | 1.4098 | ±2.8197 | +0.669 | 0.5032 |  |
| High cholesterol | -0.1070 | 1.2796 | ±2.5593 | -0.084 | 0.9334 |  |
| Kidney disease | -0.7899 | 2.0680 | ±4.1359 | -0.382 | 0.7025 |  |
| Circulatory disease | +1.2740 | 2.0515 | ±4.1031 | +0.621 | 0.5346 |  |
| **GMI (%)** | **-5.2610** | 2.3384 | ±4.6768 | **-2.250** | **0.0245** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **674**, R² = **0.0410**, Adj R² = **0.0206**, F-statistic = **2.01** (p = **0.0149**), Residual SE = **15.430** on **659** df, AIC = **5616.1**, BIC = **5683.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.2821** | 7.1072 | ±14.2144 | **+19.035** | **8.83e-81** | *** |
| Education: graduate level (vs college) | -2.0102 | 1.2821 | ±2.5641 | -1.568 | 0.1169 |  |
| Education: high school or below (vs college) | +3.8025 | 2.4532 | ±4.9064 | +1.550 | 0.1211 |  |
| Site: UCSD (vs UAB) | +0.7374 | 1.6203 | ±3.2406 | +0.455 | 0.6490 |  |
| Site: UW (vs UAB) | +0.2551 | 1.5707 | ±3.1413 | +0.162 | 0.8710 |  |
| Season: spring (vs autumn) | +3.1160 | 1.7039 | ±3.4078 | +1.829 | 0.0674 | . |
| Season: summer (vs autumn) | +2.5316 | 1.8177 | ±3.6355 | +1.393 | 0.1637 |  |
| **Season: winter (vs autumn)** | **+4.0717** | 1.7621 | ±3.5241 | **+2.311** | **0.0208** | * |
| Age (years) | -0.1175 | 0.0618 | ±0.1236 | -1.902 | 0.0572 | . |
| **BMI (kg/m2)** | **+0.2007** | 0.0823 | ±0.1645 | **+2.440** | **0.0147** | * |
| Hypertension | +0.8313 | 1.4151 | ±2.8302 | +0.587 | 0.5569 |  |
| High cholesterol | -0.0286 | 1.2831 | ±2.5662 | -0.022 | 0.9822 |  |
| Kidney disease | -0.9605 | 2.0766 | ±4.1532 | -0.463 | 0.6437 |  |
| Circulatory disease | +1.1604 | 2.0523 | ±4.1045 | +0.565 | 0.5718 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0850 | 0.0465 | ±0.0930 | -1.828 | 0.0675 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **674**, R² = **0.0455**, Adj R² = **0.0253**, F-statistic = **2.25** (p = **0.0056**), Residual SE = **15.393** on **659** df, AIC = **5612.9**, BIC = **5680.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.7448** | 5.7141 | ±11.4282 | **+23.231** | **2.21e-119** | *** |
| Education: graduate level (vs college) | -2.2238 | 1.2767 | ±2.5534 | -1.742 | 0.0815 | . |
| Education: high school or below (vs college) | +3.8061 | 2.4556 | ±4.9112 | +1.550 | 0.1211 |  |
| Site: UCSD (vs UAB) | +0.4951 | 1.6141 | ±3.2283 | +0.307 | 0.7591 |  |
| Site: UW (vs UAB) | +0.2745 | 1.5530 | ±3.1059 | +0.177 | 0.8597 |  |
| Season: spring (vs autumn) | +3.0740 | 1.6948 | ±3.3895 | +1.814 | 0.0697 | . |
| Season: summer (vs autumn) | +2.4905 | 1.8171 | ±3.6341 | +1.371 | 0.1705 |  |
| **Season: winter (vs autumn)** | **+4.1465** | 1.7534 | ±3.5067 | **+2.365** | **0.0180** | * |
| Age (years) | -0.0999 | 0.0625 | ±0.1251 | -1.598 | 0.1101 |  |
| **BMI (kg/m2)** | **+0.1750** | 0.0820 | ±0.1641 | **+2.133** | **0.0329** | * |
| Hypertension | +0.9354 | 1.4165 | ±2.8331 | +0.660 | 0.5090 |  |
| High cholesterol | -0.0517 | 1.2767 | ±2.5533 | -0.041 | 0.9677 |  |
| Kidney disease | -0.8621 | 2.0233 | ±4.0467 | -0.426 | 0.6700 |  |
| Circulatory disease | +0.9933 | 2.0521 | ±4.1043 | +0.484 | 0.6284 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.4033** | 0.1672 | ±0.3343 | **-2.413** | **0.0158** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **674**, R² = **0.0459**, Adj R² = **0.0256**, F-statistic = **2.26** (p = **0.0052**), Residual SE = **15.391** on **659** df, AIC = **5612.7**, BIC = **5680.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.2926** | 5.5046 | ±11.0092 | **+24.033** | **1.26e-127** | *** |
| Education: graduate level (vs college) | -2.1683 | 1.2752 | ±2.5505 | -1.700 | 0.0891 | . |
| Education: high school or below (vs college) | +3.8244 | 2.4528 | ±4.9055 | +1.559 | 0.1189 |  |
| Site: UCSD (vs UAB) | +0.4506 | 1.6124 | ±3.2248 | +0.279 | 0.7799 |  |
| Site: UW (vs UAB) | +0.2676 | 1.5525 | ±3.1050 | +0.172 | 0.8632 |  |
| Season: spring (vs autumn) | +3.0167 | 1.6943 | ±3.3887 | +1.780 | 0.0750 | . |
| Season: summer (vs autumn) | +2.4161 | 1.8190 | ±3.6380 | +1.328 | 0.1841 |  |
| **Season: winter (vs autumn)** | **+4.0207** | 1.7498 | ±3.4995 | **+2.298** | **0.0216** | * |
| Age (years) | -0.0999 | 0.0628 | ±0.1255 | -1.592 | 0.1113 |  |
| **BMI (kg/m2)** | **+0.1784** | 0.0818 | ±0.1637 | **+2.180** | **0.0292** | * |
| Hypertension | +0.9121 | 1.4145 | ±2.8289 | +0.645 | 0.5190 |  |
| High cholesterol | -0.0721 | 1.2763 | ±2.5526 | -0.057 | 0.9549 |  |
| Kidney disease | -0.7931 | 2.0161 | ±4.0321 | -0.393 | 0.6940 |  |
| Circulatory disease | +1.0037 | 2.0444 | ±4.0889 | +0.491 | 0.6235 |  |
| **Avg. daily SD (mg/dL)** | **-0.4158** | 0.1682 | ±0.3364 | **-2.472** | **0.0134** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **674**, R² = **0.0397**, Adj R² = **0.0193**, F-statistic = **1.95** (p = **0.0197**), Residual SE = **15.441** on **659** df, AIC = **5617.0**, BIC = **5684.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+131.0877** | 6.0705 | ±12.1410 | **+21.594** | **2.04e-103** | *** |
| Education: graduate level (vs college) | -2.2607 | 1.2853 | ±2.5705 | -1.759 | 0.0786 | . |
| Education: high school or below (vs college) | +3.6793 | 2.4567 | ±4.9135 | +1.498 | 0.1342 |  |
| Site: UCSD (vs UAB) | +0.6430 | 1.6215 | ±3.2430 | +0.397 | 0.6917 |  |
| Site: UW (vs UAB) | +0.1328 | 1.5679 | ±3.1358 | +0.085 | 0.9325 |  |
| Season: spring (vs autumn) | +3.0978 | 1.7021 | ±3.4042 | +1.820 | 0.0688 | . |
| Season: summer (vs autumn) | +2.4778 | 1.8147 | ±3.6293 | +1.365 | 0.1721 |  |
| **Season: winter (vs autumn)** | **+4.1858** | 1.7616 | ±3.5232 | **+2.376** | **0.0175** | * |
| Age (years) | -0.1067 | 0.0624 | ±0.1247 | -1.711 | 0.0872 | . |
| BMI (kg/m2) | +0.1627 | 0.0835 | ±0.1669 | +1.949 | 0.0513 | . |
| Hypertension | +0.8124 | 1.4183 | ±2.8367 | +0.573 | 0.5668 |  |
| High cholesterol | -0.0836 | 1.2790 | ±2.5579 | -0.065 | 0.9479 |  |
| Kidney disease | -1.0038 | 2.0187 | ±4.0374 | -0.497 | 0.6190 |  |
| Circulatory disease | +0.9186 | 2.0503 | ±4.1005 | +0.448 | 0.6541 |  |
| CV (%) | -0.3249 | 0.2242 | ±0.4484 | -1.449 | 0.1473 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **674**, R² = **0.0408**, Adj R² = **0.0204**, F-statistic = **2.00** (p = **0.0156**), Residual SE = **15.432** on **659** df, AIC = **5616.3**, BIC = **5684.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+119.9430** | 6.3260 | ±12.6519 | **+18.960** | **3.62e-80** | *** |
| Education: graduate level (vs college) | -2.2942 | 1.2827 | ±2.5655 | -1.789 | 0.0737 | . |
| Education: high school or below (vs college) | +3.7095 | 2.4566 | ±4.9133 | +1.510 | 0.1310 |  |
| Site: UCSD (vs UAB) | +0.6589 | 1.6171 | ±3.2342 | +0.407 | 0.6837 |  |
| Site: UW (vs UAB) | +0.1663 | 1.5644 | ±3.1288 | +0.106 | 0.9154 |  |
| Season: spring (vs autumn) | +3.1545 | 1.7055 | ±3.4109 | +1.850 | 0.0644 | . |
| Season: summer (vs autumn) | +2.4635 | 1.8126 | ±3.6251 | +1.359 | 0.1741 |  |
| **Season: winter (vs autumn)** | **+4.2136** | 1.7609 | ±3.5218 | **+2.393** | **0.0167** | * |
| Age (years) | -0.1067 | 0.0623 | ±0.1245 | -1.713 | 0.0868 | . |
| BMI (kg/m2) | +0.1626 | 0.0834 | ±0.1668 | +1.950 | 0.0512 | . |
| Hypertension | +0.8312 | 1.4185 | ±2.8370 | +0.586 | 0.5579 |  |
| High cholesterol | -0.0976 | 1.2771 | ±2.5543 | -0.076 | 0.9391 |  |
| Kidney disease | -0.9950 | 2.0219 | ±4.0438 | -0.492 | 0.6226 |  |
| Circulatory disease | +0.9019 | 2.0477 | ±4.0953 | +0.440 | 0.6596 |  |
| Mean / SD ratio | +0.9203 | 0.5527 | ±1.1054 | +1.665 | 0.0959 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **674**, R² = **0.0407**, Adj R² = **0.0203**, F-statistic = **1.99** (p = **0.0161**), Residual SE = **15.433** on **659** df, AIC = **5616.3**, BIC = **5684.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+120.3793** | 6.3438 | ±12.6877 | **+18.976** | **2.70e-80** | *** |
| Education: graduate level (vs college) | -2.2508 | 1.2790 | ±2.5581 | -1.760 | 0.0785 | . |
| Education: high school or below (vs college) | +3.7185 | 2.4520 | ±4.9041 | +1.517 | 0.1294 |  |
| Site: UCSD (vs UAB) | +0.6399 | 1.6161 | ±3.2323 | +0.396 | 0.6921 |  |
| Site: UW (vs UAB) | +0.1791 | 1.5654 | ±3.1309 | +0.114 | 0.9089 |  |
| Season: spring (vs autumn) | +3.1130 | 1.7057 | ±3.4114 | +1.825 | 0.0680 | . |
| Season: summer (vs autumn) | +2.4113 | 1.8148 | ±3.6295 | +1.329 | 0.1839 |  |
| **Season: winter (vs autumn)** | **+4.1214** | 1.7587 | ±3.5174 | **+2.343** | **0.0191** | * |
| Age (years) | -0.1060 | 0.0625 | ±0.1250 | -1.696 | 0.0899 | . |
| **BMI (kg/m2)** | **+0.1680** | 0.0830 | ±0.1660 | **+2.024** | **0.0429** | * |
| Hypertension | +0.7781 | 1.4168 | ±2.8337 | +0.549 | 0.5829 |  |
| High cholesterol | -0.1235 | 1.2766 | ±2.5532 | -0.097 | 0.9229 |  |
| Kidney disease | -0.9574 | 2.0209 | ±4.0419 | -0.474 | 0.6357 |  |
| Circulatory disease | +0.9010 | 2.0464 | ±4.0929 | +0.440 | 0.6597 |  |
| Avg. daily mean/SD | +0.7318 | 0.4515 | ±0.9030 | +1.621 | 0.1051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **674**, R² = **0.0365**, Adj R² = **0.0161**, F-statistic = **1.78** (p = **0.0372**), Residual SE = **15.466** on **659** df, AIC = **5619.2**, BIC = **5686.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7981** | 6.0627 | ±12.1254 | **+20.750** | **1.24e-95** | *** |
| Education: graduate level (vs college) | -2.0998 | 1.2840 | ±2.5680 | -1.635 | 0.1020 |  |
| Education: high school or below (vs college) | +3.6608 | 2.4659 | ±4.9317 | +1.485 | 0.1377 |  |
| Site: UCSD (vs UAB) | +0.7667 | 1.6261 | ±3.2521 | +0.471 | 0.6373 |  |
| Site: UW (vs UAB) | +0.0879 | 1.5792 | ±3.1585 | +0.056 | 0.9556 |  |
| Season: spring (vs autumn) | +3.0608 | 1.7058 | ±3.4115 | +1.794 | 0.0728 | . |
| Season: summer (vs autumn) | +2.4518 | 1.8146 | ±3.6293 | +1.351 | 0.1767 |  |
| **Season: winter (vs autumn)** | **+4.0604** | 1.7621 | ±3.5241 | **+2.304** | **0.0212** | * |
| Age (years) | -0.1134 | 0.0618 | ±0.1235 | -1.836 | 0.0664 | . |
| BMI (kg/m2) | +0.1644 | 0.0841 | ±0.1682 | +1.955 | 0.0506 | . |
| Hypertension | +0.7483 | 1.4222 | ±2.8444 | +0.526 | 0.5988 |  |
| High cholesterol | -0.1042 | 1.2814 | ±2.5628 | -0.081 | 0.9352 |  |
| Kidney disease | -1.0585 | 2.0485 | ±4.0969 | -0.517 | 0.6053 |  |
| Circulatory disease | +1.0261 | 2.0495 | ±4.0990 | +0.501 | 0.6166 |  |
| MAG (mg/dL/h) | +0.0109 | 0.0888 | ±0.1777 | +0.122 | 0.9028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **674**, R² = **0.0399**, Adj R² = **0.0195**, F-statistic = **1.96** (p = **0.0187**), Residual SE = **15.438** on **659** df, AIC = **5616.9**, BIC = **5684.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+131.0228** | 5.8374 | ±11.6748 | **+22.445** | **1.42e-111** | *** |
| Education: graduate level (vs college) | -2.0756 | 1.2802 | ±2.5605 | -1.621 | 0.1050 |  |
| Education: high school or below (vs college) | +3.8266 | 2.4591 | ±4.9182 | +1.556 | 0.1197 |  |
| Site: UCSD (vs UAB) | +0.6377 | 1.6215 | ±3.2430 | +0.393 | 0.6941 |  |
| Site: UW (vs UAB) | +0.1878 | 1.5624 | ±3.1248 | +0.120 | 0.9043 |  |
| Season: spring (vs autumn) | +3.0854 | 1.7053 | ±3.4106 | +1.809 | 0.0704 | . |
| Season: summer (vs autumn) | +2.3899 | 1.8184 | ±3.6368 | +1.314 | 0.1887 |  |
| **Season: winter (vs autumn)** | **+4.0421** | 1.7593 | ±3.5185 | **+2.298** | **0.0216** | * |
| Age (years) | -0.1072 | 0.0625 | ±0.1250 | -1.714 | 0.0865 | . |
| BMI (kg/m2) | +0.1592 | 0.0838 | ±0.1677 | +1.899 | 0.0575 | . |
| Hypertension | +0.7808 | 1.4168 | ±2.8335 | +0.551 | 0.5815 |  |
| High cholesterol | -0.1240 | 1.2794 | ±2.5588 | -0.097 | 0.9228 |  |
| Kidney disease | -0.8815 | 2.0289 | ±4.0577 | -0.434 | 0.6639 |  |
| Circulatory disease | +1.0672 | 2.0485 | ±4.0971 | +0.521 | 0.6024 |  |
| Avg. daily range (mg/dL) | -0.0573 | 0.0374 | ±0.0748 | -1.531 | 0.1258 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **674**, R² = **0.0373**, Adj R² = **0.0169**, F-statistic = **1.82** (p = **0.0319**), Residual SE = **15.460** on **659** df, AIC = **5618.7**, BIC = **5686.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.0716** | 5.2882 | ±10.5763 | **+24.029** | **1.37e-127** | *** |
| Education: graduate level (vs college) | -2.1091 | 1.2840 | ±2.5681 | -1.643 | 0.1005 |  |
| Education: high school or below (vs college) | +3.7008 | 2.4510 | ±4.9020 | +1.510 | 0.1311 |  |
| Site: UCSD (vs UAB) | +0.7418 | 1.6246 | ±3.2492 | +0.457 | 0.6479 |  |
| Site: UW (vs UAB) | +0.1131 | 1.5784 | ±3.1568 | +0.072 | 0.9429 |  |
| Season: spring (vs autumn) | +3.1381 | 1.7192 | ±3.4383 | +1.825 | 0.0679 | . |
| Season: summer (vs autumn) | +2.5670 | 1.8163 | ±3.6326 | +1.413 | 0.1576 |  |
| **Season: winter (vs autumn)** | **+4.1444** | 1.7637 | ±3.5274 | **+2.350** | **0.0188** | * |
| Age (years) | -0.1135 | 0.0617 | ±0.1234 | -1.839 | 0.0659 | . |
| **BMI (kg/m2)** | **+0.1711** | 0.0835 | ±0.1669 | **+2.050** | **0.0404** | * |
| Hypertension | +0.7343 | 1.4153 | ±2.8306 | +0.519 | 0.6039 |  |
| High cholesterol | -0.0425 | 1.2805 | ±2.5609 | -0.033 | 0.9735 |  |
| Kidney disease | -1.1201 | 2.0434 | ±4.0868 | -0.548 | 0.5836 |  |
| Circulatory disease | +1.0493 | 2.0504 | ±4.1008 | +0.512 | 0.6088 |  |
| SD of daily means (mg/dL) | -0.1995 | 0.2907 | ±0.5814 | -0.686 | 0.4925 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **674**, R² = **0.0395**, Adj R² = **0.0191**, F-statistic = **1.94** (p = **0.0204**), Residual SE = **15.442** on **659** df, AIC = **5617.2**, BIC = **5684.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+94.0809** | 24.8602 | ±49.7204 | **+3.784** | **1.54e-04** | *** |
| Education: graduate level (vs college) | -2.0791 | 1.2837 | ±2.5673 | -1.620 | 0.1053 |  |
| Education: high school or below (vs college) | +3.6773 | 2.4687 | ±4.9374 | +1.490 | 0.1363 |  |
| Site: UCSD (vs UAB) | +0.6087 | 1.6251 | ±3.2502 | +0.375 | 0.7080 |  |
| Site: UW (vs UAB) | +0.1647 | 1.5845 | ±3.1689 | +0.104 | 0.9172 |  |
| Season: spring (vs autumn) | +2.9979 | 1.6956 | ±3.3911 | +1.768 | 0.0770 | . |
| Season: summer (vs autumn) | +2.4151 | 1.8223 | ±3.6446 | +1.325 | 0.1851 |  |
| **Season: winter (vs autumn)** | **+3.9898** | 1.7567 | ±3.5133 | **+2.271** | **0.0231** | * |
| Age (years) | -0.1089 | 0.0623 | ±0.1246 | -1.748 | 0.0805 | . |
| **BMI (kg/m2)** | **+0.1703** | 0.0840 | ±0.1680 | **+2.028** | **0.0426** | * |
| Hypertension | +0.7716 | 1.4141 | ±2.8282 | +0.546 | 0.5853 |  |
| High cholesterol | +0.0041 | 1.2895 | ±2.5790 | +0.003 | 0.9975 |  |
| Kidney disease | -0.9315 | 2.0317 | ±4.0634 | -0.458 | 0.6466 |  |
| Circulatory disease | +1.1397 | 2.0503 | ±4.1007 | +0.556 | 0.5783 |  |
| Time in range 70-180, pooled (%) | +0.3227 | 0.2379 | ±0.4757 | +1.357 | 0.1749 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **674**, R² = **0.0399**, Adj R² = **0.0195**, F-statistic = **1.96** (p = **0.0188**), Residual SE = **15.439** on **659** df, AIC = **5616.9**, BIC = **5684.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+91.1455** | 25.3227 | ±50.6454 | **+3.599** | **3.19e-04** | *** |
| Education: graduate level (vs college) | -2.0752 | 1.2839 | ±2.5677 | -1.616 | 0.1060 |  |
| Education: high school or below (vs college) | +3.6671 | 2.4652 | ±4.9305 | +1.488 | 0.1369 |  |
| Site: UCSD (vs UAB) | +0.5940 | 1.6245 | ±3.2489 | +0.366 | 0.7146 |  |
| Site: UW (vs UAB) | +0.1553 | 1.5837 | ±3.1675 | +0.098 | 0.9219 |  |
| Season: spring (vs autumn) | +2.9947 | 1.6958 | ±3.3917 | +1.766 | 0.0774 | . |
| Season: summer (vs autumn) | +2.4160 | 1.8227 | ±3.6454 | +1.326 | 0.1850 |  |
| **Season: winter (vs autumn)** | **+3.9733** | 1.7561 | ±3.5123 | **+2.263** | **0.0237** | * |
| Age (years) | -0.1092 | 0.0622 | ±0.1244 | -1.756 | 0.0791 | . |
| **BMI (kg/m2)** | **+0.1724** | 0.0839 | ±0.1679 | **+2.054** | **0.0400** | * |
| Hypertension | +0.7623 | 1.4142 | ±2.8284 | +0.539 | 0.5898 |  |
| High cholesterol | +0.0136 | 1.2888 | ±2.5776 | +0.011 | 0.9916 |  |
| Kidney disease | -0.9082 | 2.0298 | ±4.0597 | -0.447 | 0.6546 |  |
| Circulatory disease | +1.1673 | 2.0479 | ±4.0958 | +0.570 | 0.5687 |  |
| Avg. daily time in range 70-180 (%) | +0.3519 | 0.2420 | ±0.4839 | +1.454 | 0.1458 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **674**, R² = **0.0368**, Adj R² = **0.0164**, F-statistic = **1.80** (p = **0.0352**), Residual SE = **15.464** on **659** df, AIC = **5619.0**, BIC = **5686.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.0371** | 5.0804 | ±10.1609 | **+24.808** | **7.29e-136** | *** |
| Education: graduate level (vs college) | -2.0370 | 1.2898 | ±2.5797 | -1.579 | 0.1143 |  |
| Education: high school or below (vs college) | +3.7569 | 2.4530 | ±4.9061 | +1.532 | 0.1256 |  |
| Site: UCSD (vs UAB) | +0.7356 | 1.6264 | ±3.2527 | +0.452 | 0.6511 |  |
| Site: UW (vs UAB) | +0.1017 | 1.5720 | ±3.1440 | +0.065 | 0.9484 |  |
| Season: spring (vs autumn) | +3.0522 | 1.7027 | ±3.4053 | +1.793 | 0.0730 | . |
| Season: summer (vs autumn) | +2.4157 | 1.8110 | ±3.6221 | +1.334 | 0.1822 |  |
| **Season: winter (vs autumn)** | **+4.0136** | 1.7486 | ±3.4972 | **+2.295** | **0.0217** | * |
| Age (years) | -0.1132 | 0.0617 | ±0.1234 | -1.834 | 0.0666 | . |
| **BMI (kg/m2)** | **+0.1652** | 0.0840 | ±0.1679 | **+1.967** | **0.0491** | * |
| Hypertension | +0.7319 | 1.4176 | ±2.8352 | +0.516 | 0.6057 |  |
| High cholesterol | -0.1189 | 1.2835 | ±2.5669 | -0.093 | 0.9262 |  |
| Kidney disease | -1.0254 | 2.0390 | ±4.0780 | -0.503 | 0.6150 |  |
| Circulatory disease | +1.0556 | 2.0432 | ±4.0864 | +0.517 | 0.6054 |  |
| Time 54-69, pooled (%) | +0.5334 | 1.5831 | ±3.1661 | +0.337 | 0.7361 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **674**, R² = **0.0366**, Adj R² = **0.0161**, F-statistic = **1.79** (p = **0.0369**), Residual SE = **15.466** on **659** df, AIC = **5619.2**, BIC = **5686.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.1326** | 5.0854 | ±10.1709 | **+24.803** | **8.38e-136** | *** |
| Education: graduate level (vs college) | -2.0685 | 1.2915 | ±2.5830 | -1.602 | 0.1093 |  |
| Education: high school or below (vs college) | +3.7182 | 2.4531 | ±4.9062 | +1.516 | 0.1296 |  |
| Site: UCSD (vs UAB) | +0.7427 | 1.6273 | ±3.2546 | +0.456 | 0.6481 |  |
| Site: UW (vs UAB) | +0.0915 | 1.5739 | ±3.1479 | +0.058 | 0.9536 |  |
| Season: spring (vs autumn) | +3.0618 | 1.7034 | ±3.4067 | +1.797 | 0.0723 | . |
| Season: summer (vs autumn) | +2.4340 | 1.8111 | ±3.6222 | +1.344 | 0.1790 |  |
| **Season: winter (vs autumn)** | **+4.0344** | 1.7491 | ±3.4982 | **+2.307** | **0.0211** | * |
| Age (years) | -0.1134 | 0.0617 | ±0.1234 | -1.838 | 0.0661 | . |
| **BMI (kg/m2)** | **+0.1648** | 0.0840 | ±0.1679 | **+1.962** | **0.0497** | * |
| Hypertension | +0.7379 | 1.4173 | ±2.8345 | +0.521 | 0.6026 |  |
| High cholesterol | -0.1113 | 1.2826 | ±2.5652 | -0.087 | 0.9308 |  |
| Kidney disease | -1.0393 | 2.0373 | ±4.0747 | -0.510 | 0.6100 |  |
| Circulatory disease | +1.0427 | 2.0439 | ±4.0878 | +0.510 | 0.6099 |  |
| Avg. daily time 54-69 (%) | +0.2475 | 1.5088 | ±3.0176 | +0.164 | 0.8697 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **674**, R² = **0.0368**, Adj R² = **0.0164**, F-statistic = **1.80** (p = **0.0352**), Residual SE = **15.464** on **659** df, AIC = **5619.0**, BIC = **5686.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.0371** | 5.0804 | ±10.1609 | **+24.808** | **7.29e-136** | *** |
| Education: graduate level (vs college) | -2.0370 | 1.2898 | ±2.5797 | -1.579 | 0.1143 |  |
| Education: high school or below (vs college) | +3.7569 | 2.4530 | ±4.9061 | +1.532 | 0.1256 |  |
| Site: UCSD (vs UAB) | +0.7356 | 1.6264 | ±3.2527 | +0.452 | 0.6511 |  |
| Site: UW (vs UAB) | +0.1017 | 1.5720 | ±3.1440 | +0.065 | 0.9484 |  |
| Season: spring (vs autumn) | +3.0522 | 1.7027 | ±3.4053 | +1.793 | 0.0730 | . |
| Season: summer (vs autumn) | +2.4157 | 1.8110 | ±3.6221 | +1.334 | 0.1822 |  |
| **Season: winter (vs autumn)** | **+4.0136** | 1.7486 | ±3.4972 | **+2.295** | **0.0217** | * |
| Age (years) | -0.1132 | 0.0617 | ±0.1234 | -1.834 | 0.0666 | . |
| **BMI (kg/m2)** | **+0.1652** | 0.0840 | ±0.1679 | **+1.967** | **0.0491** | * |
| Hypertension | +0.7319 | 1.4176 | ±2.8352 | +0.516 | 0.6057 |  |
| High cholesterol | -0.1189 | 1.2835 | ±2.5669 | -0.093 | 0.9262 |  |
| Kidney disease | -1.0254 | 2.0390 | ±4.0780 | -0.503 | 0.6150 |  |
| Circulatory disease | +1.0556 | 2.0432 | ±4.0864 | +0.517 | 0.6054 |  |
| Time < 70 (%) | +0.5334 | 1.5831 | ±3.1661 | +0.337 | 0.7361 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **674**, R² = **0.0366**, Adj R² = **0.0161**, F-statistic = **1.79** (p = **0.0369**), Residual SE = **15.466** on **659** df, AIC = **5619.2**, BIC = **5686.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.1326** | 5.0854 | ±10.1709 | **+24.803** | **8.38e-136** | *** |
| Education: graduate level (vs college) | -2.0685 | 1.2915 | ±2.5830 | -1.602 | 0.1093 |  |
| Education: high school or below (vs college) | +3.7182 | 2.4531 | ±4.9062 | +1.516 | 0.1296 |  |
| Site: UCSD (vs UAB) | +0.7427 | 1.6273 | ±3.2546 | +0.456 | 0.6481 |  |
| Site: UW (vs UAB) | +0.0915 | 1.5739 | ±3.1479 | +0.058 | 0.9536 |  |
| Season: spring (vs autumn) | +3.0618 | 1.7034 | ±3.4067 | +1.797 | 0.0723 | . |
| Season: summer (vs autumn) | +2.4340 | 1.8111 | ±3.6222 | +1.344 | 0.1790 |  |
| **Season: winter (vs autumn)** | **+4.0344** | 1.7491 | ±3.4982 | **+2.307** | **0.0211** | * |
| Age (years) | -0.1134 | 0.0617 | ±0.1234 | -1.838 | 0.0661 | . |
| **BMI (kg/m2)** | **+0.1648** | 0.0840 | ±0.1679 | **+1.962** | **0.0497** | * |
| Hypertension | +0.7379 | 1.4173 | ±2.8345 | +0.521 | 0.6026 |  |
| High cholesterol | -0.1113 | 1.2826 | ±2.5652 | -0.087 | 0.9308 |  |
| Kidney disease | -1.0393 | 2.0373 | ±4.0747 | -0.510 | 0.6100 |  |
| Circulatory disease | +1.0427 | 2.0439 | ±4.0878 | +0.510 | 0.6099 |  |
| Avg. daily time < 70 (%) | +0.2475 | 1.5088 | ±3.0176 | +0.164 | 0.8697 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **674**, R² = **0.0399**, Adj R² = **0.0195**, F-statistic = **1.95** (p = **0.0190**), Residual SE = **15.439** on **659** df, AIC = **5616.9**, BIC = **5684.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2520** | 5.0852 | ±10.1705 | **+24.827** | **4.57e-136** | *** |
| Education: graduate level (vs college) | -2.0382 | 1.2855 | ±2.5710 | -1.586 | 0.1128 |  |
| Education: high school or below (vs college) | +3.7264 | 2.4674 | ±4.9348 | +1.510 | 0.1310 |  |
| Site: UCSD (vs UAB) | +0.5855 | 1.6252 | ±3.2504 | +0.360 | 0.7187 |  |
| Site: UW (vs UAB) | +0.1795 | 1.5822 | ±3.1643 | +0.113 | 0.9097 |  |
| Season: spring (vs autumn) | +2.9874 | 1.6945 | ±3.3890 | +1.763 | 0.0779 | . |
| Season: summer (vs autumn) | +2.3951 | 1.8233 | ±3.6467 | +1.314 | 0.1890 |  |
| **Season: winter (vs autumn)** | **+3.9584** | 1.7551 | ±3.5102 | **+2.255** | **0.0241** | * |
| Age (years) | -0.1084 | 0.0623 | ±0.1246 | -1.741 | 0.0817 | . |
| **BMI (kg/m2)** | **+0.1712** | 0.0840 | ±0.1680 | **+2.039** | **0.0415** | * |
| Hypertension | +0.7669 | 1.4136 | ±2.8271 | +0.543 | 0.5874 |  |
| High cholesterol | +0.0016 | 1.2891 | ±2.5782 | +0.001 | 0.9990 |  |
| Kidney disease | -0.9116 | 2.0330 | ±4.0661 | -0.448 | 0.6539 |  |
| Circulatory disease | +1.1670 | 2.0469 | ±4.0937 | +0.570 | 0.5686 |  |
| Time 181-250, pooled (%) | -0.3396 | 0.2377 | ±0.4753 | -1.429 | 0.1531 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **674**, R² = **0.0401**, Adj R² = **0.0197**, F-statistic = **1.97** (p = **0.0181**), Residual SE = **15.437** on **659** df, AIC = **5616.7**, BIC = **5684.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2354** | 5.0790 | ±10.1580 | **+24.854** | **2.33e-136** | *** |
| Education: graduate level (vs college) | -2.0297 | 1.2865 | ±2.5730 | -1.578 | 0.1146 |  |
| Education: high school or below (vs college) | +3.7229 | 2.4650 | ±4.9300 | +1.510 | 0.1310 |  |
| Site: UCSD (vs UAB) | +0.5659 | 1.6249 | ±3.2498 | +0.348 | 0.7276 |  |
| Site: UW (vs UAB) | +0.1663 | 1.5816 | ±3.1631 | +0.105 | 0.9163 |  |
| Season: spring (vs autumn) | +2.9911 | 1.6950 | ±3.3901 | +1.765 | 0.0776 | . |
| Season: summer (vs autumn) | +2.3998 | 1.8234 | ±3.6468 | +1.316 | 0.1881 |  |
| **Season: winter (vs autumn)** | **+3.9383** | 1.7546 | ±3.5092 | **+2.245** | **0.0248** | * |
| Age (years) | -0.1090 | 0.0622 | ±0.1244 | -1.753 | 0.0796 | . |
| **BMI (kg/m2)** | **+0.1733** | 0.0840 | ±0.1679 | **+2.064** | **0.0390** | * |
| Hypertension | +0.7574 | 1.4139 | ±2.8277 | +0.536 | 0.5922 |  |
| High cholesterol | +0.0084 | 1.2888 | ±2.5776 | +0.006 | 0.9948 |  |
| Kidney disease | -0.8937 | 2.0313 | ±4.0627 | -0.440 | 0.6600 |  |
| Circulatory disease | +1.2001 | 2.0438 | ±4.0876 | +0.587 | 0.5571 |  |
| Avg. daily time 181-250 (%) | -0.3593 | 0.2425 | ±0.4851 | -1.481 | 0.1385 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **674**, R² = **0.0399**, Adj R² = **0.0195**, F-statistic = **1.95** (p = **0.0190**), Residual SE = **15.439** on **659** df, AIC = **5616.9**, BIC = **5684.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2520** | 5.0852 | ±10.1705 | **+24.827** | **4.57e-136** | *** |
| Education: graduate level (vs college) | -2.0382 | 1.2855 | ±2.5710 | -1.586 | 0.1128 |  |
| Education: high school or below (vs college) | +3.7264 | 2.4674 | ±4.9348 | +1.510 | 0.1310 |  |
| Site: UCSD (vs UAB) | +0.5855 | 1.6252 | ±3.2504 | +0.360 | 0.7187 |  |
| Site: UW (vs UAB) | +0.1795 | 1.5822 | ±3.1643 | +0.113 | 0.9097 |  |
| Season: spring (vs autumn) | +2.9874 | 1.6945 | ±3.3890 | +1.763 | 0.0779 | . |
| Season: summer (vs autumn) | +2.3951 | 1.8233 | ±3.6467 | +1.314 | 0.1890 |  |
| **Season: winter (vs autumn)** | **+3.9584** | 1.7551 | ±3.5102 | **+2.255** | **0.0241** | * |
| Age (years) | -0.1084 | 0.0623 | ±0.1246 | -1.741 | 0.0817 | . |
| **BMI (kg/m2)** | **+0.1712** | 0.0840 | ±0.1680 | **+2.039** | **0.0415** | * |
| Hypertension | +0.7669 | 1.4136 | ±2.8271 | +0.543 | 0.5874 |  |
| High cholesterol | +0.0016 | 1.2891 | ±2.5782 | +0.001 | 0.9990 |  |
| Kidney disease | -0.9116 | 2.0330 | ±4.0661 | -0.448 | 0.6539 |  |
| Circulatory disease | +1.1670 | 2.0469 | ±4.0937 | +0.570 | 0.5686 |  |
| Time > 180 (%) | -0.3396 | 0.2377 | ±0.4753 | -1.429 | 0.1531 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **674**, R² = **0.0401**, Adj R² = **0.0197**, F-statistic = **1.97** (p = **0.0181**), Residual SE = **15.437** on **659** df, AIC = **5616.7**, BIC = **5684.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2354** | 5.0790 | ±10.1580 | **+24.854** | **2.33e-136** | *** |
| Education: graduate level (vs college) | -2.0297 | 1.2865 | ±2.5730 | -1.578 | 0.1146 |  |
| Education: high school or below (vs college) | +3.7229 | 2.4650 | ±4.9300 | +1.510 | 0.1310 |  |
| Site: UCSD (vs UAB) | +0.5659 | 1.6249 | ±3.2498 | +0.348 | 0.7276 |  |
| Site: UW (vs UAB) | +0.1663 | 1.5816 | ±3.1631 | +0.105 | 0.9163 |  |
| Season: spring (vs autumn) | +2.9911 | 1.6950 | ±3.3901 | +1.765 | 0.0776 | . |
| Season: summer (vs autumn) | +2.3998 | 1.8234 | ±3.6468 | +1.316 | 0.1881 |  |
| **Season: winter (vs autumn)** | **+3.9383** | 1.7546 | ±3.5092 | **+2.245** | **0.0248** | * |
| Age (years) | -0.1090 | 0.0622 | ±0.1244 | -1.753 | 0.0796 | . |
| **BMI (kg/m2)** | **+0.1733** | 0.0840 | ±0.1679 | **+2.064** | **0.0390** | * |
| Hypertension | +0.7574 | 1.4139 | ±2.8277 | +0.536 | 0.5922 |  |
| High cholesterol | +0.0084 | 1.2888 | ±2.5776 | +0.006 | 0.9948 |  |
| Kidney disease | -0.8937 | 2.0313 | ±4.0627 | -0.440 | 0.6600 |  |
| Circulatory disease | +1.2001 | 2.0438 | ±4.0876 | +0.587 | 0.5571 |  |
| Avg. daily time > 180 (%) | -0.3593 | 0.2425 | ±0.4851 | -1.481 | 0.1385 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 674)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **674**, R² = **0.0392**, Adj R² = **0.0187**, F-statistic = **1.92** (p = **0.0219**), Residual SE = **15.445** on **659** df, AIC = **5617.4**, BIC = **5685.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.0998** | 5.0657 | ±10.1315 | **+24.893** | **8.94e-137** | *** |
| Education: graduate level (vs college) | -2.1181 | 1.2790 | ±2.5580 | -1.656 | 0.0977 | . |
| Education: high school or below (vs college) | +3.7748 | 2.4872 | ±4.9744 | +1.518 | 0.1291 |  |
| Site: UCSD (vs UAB) | +0.6826 | 1.6235 | ±3.2470 | +0.420 | 0.6742 |  |
| Site: UW (vs UAB) | +0.1467 | 1.5716 | ±3.1432 | +0.093 | 0.9257 |  |
| Season: spring (vs autumn) | +3.0475 | 1.6978 | ±3.3955 | +1.795 | 0.0727 | . |
| Season: summer (vs autumn) | +2.4431 | 1.8236 | ±3.6473 | +1.340 | 0.1803 |  |
| **Season: winter (vs autumn)** | **+4.0741** | 1.7527 | ±3.5054 | **+2.324** | **0.0201** | * |
| Age (years) | -0.1160 | 0.0614 | ±0.1229 | -1.888 | 0.0591 | . |
| **BMI (kg/m2)** | **+0.1799** | 0.0832 | ±0.1665 | **+2.161** | **0.0307** | * |
| Hypertension | +0.6951 | 1.4144 | ±2.8288 | +0.491 | 0.6231 |  |
| High cholesterol | +0.0668 | 1.2951 | ±2.5901 | +0.052 | 0.9589 |  |
| Kidney disease | -1.0634 | 2.0465 | ±4.0930 | -0.520 | 0.6033 |  |
| Circulatory disease | +1.0200 | 2.0772 | ±4.1544 | +0.491 | 0.6234 |  |
| Nocturnal time > 180 (%) | -0.2651 | 0.1892 | ±0.3784 | -1.401 | 0.1611 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
