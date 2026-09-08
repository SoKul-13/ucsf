# Phase 6b model output tables - Hyperglycaemia exposure: at least one reading > 250 - Non-healthy group (T2D non-insulin + T2D insulin) - Home environment

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 542; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **542**, R² = **0.2042**, Adj R² = **0.1846**, F-statistic = **10.42** (p = **8.88e-20**), Residual SE = **0.920** on **528** df, AIC = **1461.9**, BIC = **1522.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7380** | 0.4078 | ±0.8157 | **+9.166** | **4.92e-20** | *** |
| Education: graduate level (vs college) | -0.1110 | 0.0853 | ±0.1705 | -1.302 | 0.1930 |  |
| **Education: high school or below (vs college)** | **+0.4965** | 0.1321 | ±0.2642 | **+3.759** | **1.70e-04** | *** |
| Site: UCSD (vs UAB) | +0.0542 | 0.0870 | ±0.1739 | +0.623 | 0.5333 |  |
| **Site: UW (vs UAB)** | **-0.4309** | 0.1013 | ±0.2026 | **-4.255** | **2.09e-05** | *** |
| Season: spring (vs autumn) | -0.1216 | 0.1129 | ±0.2259 | -1.077 | 0.2814 |  |
| Season: summer (vs autumn) | +0.0856 | 0.1089 | ±0.2179 | +0.786 | 0.4320 |  |
| Season: winter (vs autumn) | +0.1012 | 0.1227 | ±0.2455 | +0.824 | 0.4097 |  |
| **Age (years)** | **-0.0281** | 0.0041 | ±0.0082 | **-6.855** | **7.14e-12** | *** |
| BMI (kg/m2) | +0.0029 | 0.0066 | ±0.0133 | +0.435 | 0.6635 |  |
| Hypertension | +0.0426 | 0.0855 | ±0.1709 | +0.498 | 0.6186 |  |
| High cholesterol | -0.0315 | 0.0857 | ±0.1714 | -0.367 | 0.7135 |  |
| Kidney disease | +0.0039 | 0.0996 | ±0.1992 | +0.039 | 0.9685 |  |
| Circulatory disease | -0.0159 | 0.0933 | ±0.1866 | -0.171 | 0.8645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **542**, R² = **0.2200**, Adj R² = **0.1993**, F-statistic = **10.62** (p = **2.29e-21**), Residual SE = **0.912** on **527** df, AIC = **1453.0**, BIC = **1517.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0377** | 0.4783 | ±0.9565 | **+6.352** | **2.13e-10** | *** |
| Education: graduate level (vs college) | -0.0928 | 0.0861 | ±0.1722 | -1.077 | 0.2813 |  |
| **Education: high school or below (vs college)** | **+0.4572** | 0.1271 | ±0.2543 | **+3.596** | **3.23e-04** | *** |
| Site: UCSD (vs UAB) | +0.0765 | 0.0875 | ±0.1750 | +0.875 | 0.3816 |  |
| **Site: UW (vs UAB)** | **-0.4047** | 0.0991 | ±0.1982 | **-4.085** | **4.41e-05** | *** |
| Season: spring (vs autumn) | -0.1030 | 0.1123 | ±0.2246 | -0.918 | 0.3589 |  |
| Season: summer (vs autumn) | +0.1106 | 0.1078 | ±0.2157 | +1.025 | 0.3053 |  |
| Season: winter (vs autumn) | +0.0993 | 0.1210 | ±0.2421 | +0.820 | 0.4121 |  |
| **Age (years)** | **-0.0273** | 0.0041 | ±0.0081 | **-6.722** | **1.80e-11** | *** |
| BMI (kg/m2) | +0.0008 | 0.0068 | ±0.0136 | +0.118 | 0.9065 |  |
| Hypertension | +0.0372 | 0.0854 | ±0.1707 | +0.436 | 0.6628 |  |
| High cholesterol | -0.0287 | 0.0859 | ±0.1718 | -0.334 | 0.7385 |  |
| Kidney disease | +0.0097 | 0.0998 | ±0.1996 | +0.097 | 0.9225 |  |
| Circulatory disease | -0.0269 | 0.0922 | ±0.1844 | -0.291 | 0.7707 |  |
| **HbA1c (%)** | **+0.0967** | 0.0400 | ±0.0799 | **+2.420** | **0.0155** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **542**, R² = **0.2115**, Adj R² = **0.1906**, F-statistic = **10.10** (p = **3.12e-20**), Residual SE = **0.917** on **527** df, AIC = **1458.8**, BIC = **1523.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.3443** | 0.4486 | ±0.8973 | **+7.454** | **9.03e-14** | *** |
| Education: graduate level (vs college) | -0.1003 | 0.0857 | ±0.1715 | -1.170 | 0.2421 |  |
| **Education: high school or below (vs college)** | **+0.4741** | 0.1283 | ±0.2567 | **+3.693** | **2.21e-04** | *** |
| Site: UCSD (vs UAB) | +0.0725 | 0.0866 | ±0.1732 | +0.838 | 0.4023 |  |
| **Site: UW (vs UAB)** | **-0.4147** | 0.1004 | ±0.2009 | **-4.129** | **3.64e-05** | *** |
| Season: spring (vs autumn) | -0.1287 | 0.1136 | ±0.2273 | -1.133 | 0.2572 |  |
| Season: summer (vs autumn) | +0.0996 | 0.1086 | ±0.2172 | +0.917 | 0.3591 |  |
| Season: winter (vs autumn) | +0.0882 | 0.1218 | ±0.2436 | +0.724 | 0.4688 |  |
| **Age (years)** | **-0.0275** | 0.0041 | ±0.0082 | **-6.744** | **1.55e-11** | *** |
| BMI (kg/m2) | +0.0019 | 0.0067 | ±0.0135 | +0.283 | 0.7775 |  |
| Hypertension | +0.0428 | 0.0858 | ±0.1716 | +0.498 | 0.6183 |  |
| High cholesterol | -0.0259 | 0.0862 | ±0.1724 | -0.300 | 0.7640 |  |
| Kidney disease | -0.0033 | 0.0995 | ±0.1989 | -0.034 | 0.9731 |  |
| Circulatory disease | -0.0272 | 0.0927 | ±0.1855 | -0.293 | 0.7693 |  |
| Mean glucose (mg/dL) | +0.0022 | 0.0012 | ±0.0024 | +1.858 | 0.0632 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **542**, R² = **0.2115**, Adj R² = **0.1906**, F-statistic = **10.10** (p = **3.12e-20**), Residual SE = **0.917** on **527** df, AIC = **1458.8**, BIC = **1523.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0396** | 0.5379 | ±1.0759 | **+5.650** | **1.60e-08** | *** |
| Education: graduate level (vs college) | -0.1003 | 0.0857 | ±0.1715 | -1.170 | 0.2421 |  |
| **Education: high school or below (vs college)** | **+0.4741** | 0.1283 | ±0.2567 | **+3.693** | **2.21e-04** | *** |
| Site: UCSD (vs UAB) | +0.0725 | 0.0866 | ±0.1732 | +0.838 | 0.4023 |  |
| **Site: UW (vs UAB)** | **-0.4147** | 0.1004 | ±0.2009 | **-4.129** | **3.64e-05** | *** |
| Season: spring (vs autumn) | -0.1287 | 0.1136 | ±0.2273 | -1.133 | 0.2572 |  |
| Season: summer (vs autumn) | +0.0996 | 0.1086 | ±0.2172 | +0.917 | 0.3591 |  |
| Season: winter (vs autumn) | +0.0882 | 0.1218 | ±0.2436 | +0.724 | 0.4688 |  |
| **Age (years)** | **-0.0275** | 0.0041 | ±0.0082 | **-6.744** | **1.55e-11** | *** |
| BMI (kg/m2) | +0.0019 | 0.0067 | ±0.0135 | +0.283 | 0.7775 |  |
| Hypertension | +0.0428 | 0.0858 | ±0.1716 | +0.498 | 0.6183 |  |
| High cholesterol | -0.0259 | 0.0862 | ±0.1724 | -0.300 | 0.7640 |  |
| Kidney disease | -0.0033 | 0.0995 | ±0.1989 | -0.034 | 0.9731 |  |
| Circulatory disease | -0.0272 | 0.0927 | ±0.1855 | -0.293 | 0.7693 |  |
| GMI (%) | +0.0921 | 0.0496 | ±0.0991 | +1.858 | 0.0632 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **542**, R² = **0.2170**, Adj R² = **0.1962**, F-statistic = **10.43** (p = **5.75e-21**), Residual SE = **0.914** on **527** df, AIC = **1455.0**, BIC = **1519.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.2668** | 0.4319 | ±0.8638 | **+7.564** | **3.91e-14** | *** |
| Education: graduate level (vs college) | -0.0925 | 0.0858 | ±0.1716 | -1.078 | 0.2809 |  |
| **Education: high school or below (vs college)** | **+0.4712** | 0.1279 | ±0.2558 | **+3.685** | **2.29e-04** | *** |
| Site: UCSD (vs UAB) | +0.0805 | 0.0863 | ±0.1725 | +0.933 | 0.3511 |  |
| **Site: UW (vs UAB)** | **-0.4198** | 0.1002 | ±0.2004 | **-4.189** | **2.80e-05** | *** |
| Season: spring (vs autumn) | -0.1362 | 0.1133 | ±0.2266 | -1.202 | 0.2292 |  |
| Season: summer (vs autumn) | +0.1012 | 0.1079 | ±0.2158 | +0.938 | 0.3483 |  |
| Season: winter (vs autumn) | +0.0828 | 0.1211 | ±0.2422 | +0.684 | 0.4941 |  |
| **Age (years)** | **-0.0269** | 0.0041 | ±0.0082 | **-6.597** | **4.18e-11** | *** |
| BMI (kg/m2) | +0.0008 | 0.0068 | ±0.0136 | +0.120 | 0.9047 |  |
| Hypertension | +0.0454 | 0.0857 | ±0.1714 | +0.530 | 0.5960 |  |
| High cholesterol | -0.0238 | 0.0859 | ±0.1718 | -0.276 | 0.7822 |  |
| Kidney disease | +0.0020 | 0.0983 | ±0.1966 | +0.020 | 0.9840 |  |
| Circulatory disease | -0.0310 | 0.0926 | ±0.1852 | -0.334 | 0.7383 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0027** | 0.0011 | ±0.0022 | **+2.488** | **0.0129** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2084**, Adj R² = **0.1874**, F-statistic = **9.91** (p = **8.03e-20**), Residual SE = **0.919** on **527** df, AIC = **1461.0**, BIC = **1525.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.5002** | 0.4321 | ±0.8642 | **+8.100** | **5.48e-16** | *** |
| Education: graduate level (vs college) | -0.1013 | 0.0856 | ±0.1712 | -1.183 | 0.2367 |  |
| **Education: high school or below (vs college)** | **+0.4794** | 0.1317 | ±0.2635 | **+3.639** | **2.74e-04** | *** |
| Site: UCSD (vs UAB) | +0.0648 | 0.0869 | ±0.1738 | +0.746 | 0.4555 |  |
| **Site: UW (vs UAB)** | **-0.4105** | 0.1005 | ±0.2010 | **-4.085** | **4.41e-05** | *** |
| Season: spring (vs autumn) | -0.1276 | 0.1131 | ±0.2262 | -1.128 | 0.2591 |  |
| Season: summer (vs autumn) | +0.0981 | 0.1096 | ±0.2192 | +0.896 | 0.3705 |  |
| Season: winter (vs autumn) | +0.0922 | 0.1221 | ±0.2442 | +0.755 | 0.4503 |  |
| **Age (years)** | **-0.0279** | 0.0041 | ±0.0082 | **-6.798** | **1.06e-11** | *** |
| BMI (kg/m2) | +0.0024 | 0.0066 | ±0.0132 | +0.370 | 0.7115 |  |
| Hypertension | +0.0382 | 0.0859 | ±0.1717 | +0.445 | 0.6561 |  |
| High cholesterol | -0.0250 | 0.0864 | ±0.1727 | -0.289 | 0.7726 |  |
| Kidney disease | -0.0254 | 0.0980 | ±0.1960 | -0.259 | 0.7956 |  |
| Circulatory disease | -0.0230 | 0.0930 | ±0.1860 | -0.247 | 0.8046 |  |
| Glucose SD, pooled (mg/dL) | +0.0056 | 0.0032 | ±0.0064 | +1.754 | 0.0794 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2053**, Adj R² = **0.1842**, F-statistic = **9.73** (p = **2.06e-19**), Residual SE = **0.920** on **527** df, AIC = **1463.1**, BIC = **1527.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6065** | 0.4379 | ±0.8757 | **+8.237** | **1.77e-16** | *** |
| Education: graduate level (vs college) | -0.1069 | 0.0857 | ±0.1714 | -1.247 | 0.2122 |  |
| **Education: high school or below (vs college)** | **+0.4858** | 0.1326 | ±0.2652 | **+3.663** | **2.49e-04** | *** |
| Site: UCSD (vs UAB) | +0.0598 | 0.0873 | ±0.1746 | +0.685 | 0.4935 |  |
| **Site: UW (vs UAB)** | **-0.4214** | 0.1012 | ±0.2024 | **-4.164** | **3.13e-05** | *** |
| Season: spring (vs autumn) | -0.1253 | 0.1129 | ±0.2257 | -1.110 | 0.2668 |  |
| Season: summer (vs autumn) | +0.0928 | 0.1102 | ±0.2204 | +0.842 | 0.3998 |  |
| Season: winter (vs autumn) | +0.0980 | 0.1225 | ±0.2450 | +0.800 | 0.4240 |  |
| **Age (years)** | **-0.0281** | 0.0041 | ±0.0082 | **-6.820** | **9.07e-12** | *** |
| BMI (kg/m2) | +0.0029 | 0.0066 | ±0.0133 | +0.435 | 0.6634 |  |
| Hypertension | +0.0414 | 0.0858 | ±0.1716 | +0.483 | 0.6293 |  |
| High cholesterol | -0.0286 | 0.0862 | ±0.1724 | -0.331 | 0.7404 |  |
| Kidney disease | -0.0127 | 0.0985 | ±0.1969 | -0.129 | 0.8970 |  |
| Circulatory disease | -0.0184 | 0.0934 | ±0.1868 | -0.197 | 0.8436 |  |
| Avg. daily SD (mg/dL) | +0.0034 | 0.0036 | ±0.0073 | +0.932 | 0.3513 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **542**, R² = **0.2042**, Adj R² = **0.1831**, F-statistic = **9.66** (p = **2.90e-19**), Residual SE = **0.921** on **527** df, AIC = **1463.8**, BIC = **1528.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7048** | 0.4701 | ±0.9401 | **+7.881** | **3.24e-15** | *** |
| Education: graduate level (vs college) | -0.1105 | 0.0854 | ±0.1709 | -1.293 | 0.1961 |  |
| **Education: high school or below (vs college)** | **+0.4957** | 0.1333 | ±0.2667 | **+3.718** | **2.01e-04** | *** |
| Site: UCSD (vs UAB) | +0.0545 | 0.0871 | ±0.1743 | +0.626 | 0.5316 |  |
| **Site: UW (vs UAB)** | **-0.4292** | 0.1015 | ±0.2031 | **-4.227** | **2.37e-05** | *** |
| Season: spring (vs autumn) | -0.1216 | 0.1132 | ±0.2264 | -1.074 | 0.2827 |  |
| Season: summer (vs autumn) | +0.0863 | 0.1095 | ±0.2191 | +0.788 | 0.4309 |  |
| Season: winter (vs autumn) | +0.1010 | 0.1230 | ±0.2460 | +0.821 | 0.4114 |  |
| **Age (years)** | **-0.0282** | 0.0041 | ±0.0082 | **-6.843** | **7.74e-12** | *** |
| BMI (kg/m2) | +0.0029 | 0.0067 | ±0.0133 | +0.435 | 0.6636 |  |
| Hypertension | +0.0417 | 0.0857 | ±0.1713 | +0.487 | 0.6265 |  |
| High cholesterol | -0.0311 | 0.0860 | ±0.1719 | -0.361 | 0.7179 |  |
| Kidney disease | +0.0002 | 0.0986 | ±0.1971 | +0.002 | 0.9981 |  |
| Circulatory disease | -0.0160 | 0.0934 | ±0.1869 | -0.171 | 0.8643 |  |
| CV (%) | +0.0014 | 0.0080 | ±0.0160 | +0.174 | 0.8619 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **542**, R² = **0.2042**, Adj R² = **0.1830**, F-statistic = **9.66** (p = **2.93e-19**), Residual SE = **0.921** on **527** df, AIC = **1463.9**, BIC = **1528.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7573** | 0.4453 | ±0.8906 | **+8.438** | **3.24e-17** | *** |
| Education: graduate level (vs college) | -0.1107 | 0.0855 | ±0.1710 | -1.295 | 0.1954 |  |
| **Education: high school or below (vs college)** | **+0.4962** | 0.1333 | ±0.2667 | **+3.721** | **1.98e-04** | *** |
| Site: UCSD (vs UAB) | +0.0541 | 0.0871 | ±0.1741 | +0.621 | 0.5343 |  |
| **Site: UW (vs UAB)** | **-0.4302** | 0.1017 | ±0.2035 | **-4.229** | **2.35e-05** | *** |
| Season: spring (vs autumn) | -0.1218 | 0.1129 | ±0.2258 | -1.079 | 0.2805 |  |
| Season: summer (vs autumn) | +0.0855 | 0.1090 | ±0.2180 | +0.784 | 0.4330 |  |
| Season: winter (vs autumn) | +0.1009 | 0.1231 | ±0.2462 | +0.820 | 0.4122 |  |
| **Age (years)** | **-0.0282** | 0.0041 | ±0.0082 | **-6.843** | **7.77e-12** | *** |
| BMI (kg/m2) | +0.0029 | 0.0067 | ±0.0133 | +0.436 | 0.6627 |  |
| Hypertension | +0.0422 | 0.0856 | ±0.1713 | +0.493 | 0.6218 |  |
| High cholesterol | -0.0315 | 0.0859 | ±0.1718 | -0.367 | 0.7135 |  |
| Kidney disease | +0.0022 | 0.0988 | ±0.1976 | +0.023 | 0.9819 |  |
| Circulatory disease | -0.0162 | 0.0935 | ±0.1870 | -0.173 | 0.8627 |  |
| Mean / SD ratio | -0.0045 | 0.0451 | ±0.0903 | -0.099 | 0.9213 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2049**, Adj R² = **0.1837**, F-statistic = **9.70** (p = **2.39e-19**), Residual SE = **0.921** on **527** df, AIC = **1463.4**, BIC = **1527.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6284** | 0.4340 | ±0.8679 | **+8.361** | **6.21e-17** | *** |
| Education: graduate level (vs college) | -0.1129 | 0.0857 | ±0.1714 | -1.317 | 0.1879 |  |
| **Education: high school or below (vs college)** | **+0.4993** | 0.1332 | ±0.2664 | **+3.748** | **1.78e-04** | *** |
| Site: UCSD (vs UAB) | +0.0549 | 0.0871 | ±0.1743 | +0.630 | 0.5290 |  |
| **Site: UW (vs UAB)** | **-0.4338** | 0.1018 | ±0.2036 | **-4.261** | **2.04e-05** | *** |
| Season: spring (vs autumn) | -0.1219 | 0.1133 | ±0.2265 | -1.076 | 0.2818 |  |
| Season: summer (vs autumn) | +0.0850 | 0.1092 | ±0.2184 | +0.778 | 0.4363 |  |
| Season: winter (vs autumn) | +0.1009 | 0.1228 | ±0.2457 | +0.821 | 0.4116 |  |
| **Age (years)** | **-0.0281** | 0.0041 | ±0.0082 | **-6.840** | **7.93e-12** | *** |
| BMI (kg/m2) | +0.0026 | 0.0067 | ±0.0135 | +0.379 | 0.7049 |  |
| Hypertension | +0.0437 | 0.0856 | ±0.1711 | +0.511 | 0.6094 |  |
| High cholesterol | -0.0315 | 0.0857 | ±0.1715 | -0.367 | 0.7134 |  |
| Kidney disease | +0.0136 | 0.0994 | ±0.1988 | +0.137 | 0.8914 |  |
| Circulatory disease | -0.0158 | 0.0934 | ±0.1869 | -0.169 | 0.8661 |  |
| Avg. daily mean/SD | +0.0225 | 0.0388 | ±0.0776 | +0.579 | 0.5623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **542**, R² = **0.2042**, Adj R² = **0.1831**, F-statistic = **9.66** (p = **2.90e-19**), Residual SE = **0.921** on **527** df, AIC = **1463.8**, BIC = **1528.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6952** | 0.4622 | ±0.9245 | **+7.994** | **1.31e-15** | *** |
| Education: graduate level (vs college) | -0.1098 | 0.0859 | ±0.1717 | -1.279 | 0.2010 |  |
| **Education: high school or below (vs college)** | **+0.4954** | 0.1310 | ±0.2620 | **+3.782** | **1.56e-04** | *** |
| Site: UCSD (vs UAB) | +0.0550 | 0.0872 | ±0.1743 | +0.631 | 0.5281 |  |
| **Site: UW (vs UAB)** | **-0.4282** | 0.1024 | ±0.2049 | **-4.180** | **2.92e-05** | *** |
| Season: spring (vs autumn) | -0.1218 | 0.1133 | ±0.2267 | -1.075 | 0.2824 |  |
| Season: summer (vs autumn) | +0.0874 | 0.1091 | ±0.2182 | +0.801 | 0.4232 |  |
| Season: winter (vs autumn) | +0.1013 | 0.1229 | ±0.2457 | +0.825 | 0.4095 |  |
| **Age (years)** | **-0.0280** | 0.0041 | ±0.0082 | **-6.815** | **9.44e-12** | *** |
| BMI (kg/m2) | +0.0029 | 0.0066 | ±0.0133 | +0.437 | 0.6622 |  |
| Hypertension | +0.0424 | 0.0857 | ±0.1714 | +0.495 | 0.6205 |  |
| High cholesterol | -0.0311 | 0.0861 | ±0.1722 | -0.361 | 0.7184 |  |
| Kidney disease | +0.0020 | 0.1012 | ±0.2024 | +0.020 | 0.9841 |  |
| Circulatory disease | -0.0162 | 0.0934 | ±0.1868 | -0.173 | 0.8624 |  |
| MAG (mg/dL/h) | +0.0008 | 0.0042 | ±0.0083 | +0.181 | 0.8567 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **542**, R² = **0.2047**, Adj R² = **0.1836**, F-statistic = **9.69** (p = **2.48e-19**), Residual SE = **0.921** on **527** df, AIC = **1463.5**, BIC = **1527.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6126** | 0.4605 | ±0.9209 | **+7.845** | **4.31e-15** | *** |
| Education: graduate level (vs college) | -0.1082 | 0.0858 | ±0.1717 | -1.260 | 0.2075 |  |
| **Education: high school or below (vs college)** | **+0.4889** | 0.1326 | ±0.2652 | **+3.688** | **2.26e-04** | *** |
| Site: UCSD (vs UAB) | +0.0584 | 0.0873 | ±0.1745 | +0.669 | 0.5034 |  |
| **Site: UW (vs UAB)** | **-0.4244** | 0.1015 | ±0.2031 | **-4.180** | **2.92e-05** | *** |
| Season: spring (vs autumn) | -0.1252 | 0.1127 | ±0.2255 | -1.110 | 0.2670 |  |
| Season: summer (vs autumn) | +0.0882 | 0.1095 | ±0.2191 | +0.805 | 0.4209 |  |
| Season: winter (vs autumn) | +0.0982 | 0.1226 | ±0.2452 | +0.801 | 0.4234 |  |
| **Age (years)** | **-0.0280** | 0.0041 | ±0.0083 | **-6.775** | **1.24e-11** | *** |
| BMI (kg/m2) | +0.0030 | 0.0066 | ±0.0133 | +0.447 | 0.6549 |  |
| Hypertension | +0.0430 | 0.0858 | ±0.1715 | +0.502 | 0.6158 |  |
| High cholesterol | -0.0309 | 0.0860 | ±0.1720 | -0.359 | 0.7198 |  |
| Kidney disease | -0.0083 | 0.0985 | ±0.1970 | -0.085 | 0.9325 |  |
| Circulatory disease | -0.0184 | 0.0937 | ±0.1874 | -0.196 | 0.8444 |  |
| Avg. daily range (mg/dL) | +0.0007 | 0.0011 | ±0.0021 | +0.656 | 0.5118 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **542**, R² = **0.2218**, Adj R² = **0.2011**, F-statistic = **10.73** (p = **1.32e-21**), Residual SE = **0.911** on **527** df, AIC = **1451.8**, BIC = **1516.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4699** | 0.4049 | ±0.8099 | **+8.569** | **1.04e-17** | *** |
| Education: graduate level (vs college) | -0.0818 | 0.0854 | ±0.1707 | -0.958 | 0.3379 |  |
| **Education: high school or below (vs college)** | **+0.4892** | 0.1290 | ±0.2581 | **+3.791** | **1.50e-04** | *** |
| Site: UCSD (vs UAB) | +0.0702 | 0.0862 | ±0.1723 | +0.814 | 0.4154 |  |
| **Site: UW (vs UAB)** | **-0.3956** | 0.0993 | ±0.1986 | **-3.985** | **6.76e-05** | *** |
| Season: spring (vs autumn) | -0.1187 | 0.1125 | ±0.2251 | -1.055 | 0.2914 |  |
| Season: summer (vs autumn) | +0.0963 | 0.1081 | ±0.2162 | +0.891 | 0.3727 |  |
| Season: winter (vs autumn) | +0.0775 | 0.1206 | ±0.2411 | +0.643 | 0.5204 |  |
| **Age (years)** | **-0.0268** | 0.0041 | ±0.0081 | **-6.582** | **4.64e-11** | *** |
| BMI (kg/m2) | +0.0009 | 0.0065 | ±0.0129 | +0.141 | 0.8876 |  |
| Hypertension | +0.0226 | 0.0859 | ±0.1718 | +0.264 | 0.7921 |  |
| High cholesterol | -0.0193 | 0.0856 | ±0.1712 | -0.225 | 0.8219 |  |
| Kidney disease | -0.0206 | 0.0963 | ±0.1925 | -0.214 | 0.8307 |  |
| Circulatory disease | -0.0495 | 0.0914 | ±0.1828 | -0.542 | 0.5879 |  |
| **SD of daily means (mg/dL)** | **+0.0161** | 0.0050 | ±0.0099 | **+3.236** | **0.0012** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **542**, R² = **0.2121**, Adj R² = **0.1912**, F-statistic = **10.14** (p = **2.60e-20**), Residual SE = **0.917** on **527** df, AIC = **1458.4**, BIC = **1522.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.9754** | 0.4304 | ±0.8607 | **+9.237** | **2.53e-20** | *** |
| Education: graduate level (vs college) | -0.1024 | 0.0858 | ±0.1715 | -1.194 | 0.2324 |  |
| **Education: high school or below (vs college)** | **+0.4716** | 0.1285 | ±0.2569 | **+3.671** | **2.41e-04** | *** |
| Site: UCSD (vs UAB) | +0.0772 | 0.0865 | ±0.1730 | +0.892 | 0.3724 |  |
| **Site: UW (vs UAB)** | **-0.4132** | 0.1002 | ±0.2004 | **-4.124** | **3.73e-05** | *** |
| Season: spring (vs autumn) | -0.1299 | 0.1135 | ±0.2269 | -1.145 | 0.2523 |  |
| Season: summer (vs autumn) | +0.0967 | 0.1084 | ±0.2168 | +0.892 | 0.3725 |  |
| Season: winter (vs autumn) | +0.0864 | 0.1218 | ±0.2436 | +0.709 | 0.4781 |  |
| **Age (years)** | **-0.0277** | 0.0041 | ±0.0081 | **-6.805** | **1.01e-11** | *** |
| BMI (kg/m2) | +0.0016 | 0.0067 | ±0.0134 | +0.236 | 0.8131 |  |
| Hypertension | +0.0454 | 0.0859 | ±0.1718 | +0.528 | 0.5974 |  |
| High cholesterol | -0.0206 | 0.0865 | ±0.1729 | -0.238 | 0.8116 |  |
| Kidney disease | -0.0082 | 0.0990 | ±0.1980 | -0.083 | 0.9341 |  |
| Circulatory disease | -0.0274 | 0.0920 | ±0.1841 | -0.298 | 0.7661 |  |
| **Time in range 70-180, pooled (%)** | **-0.0036** | 0.0018 | ±0.0035 | **-2.065** | **0.0389** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **542**, R² = **0.2120**, Adj R² = **0.1911**, F-statistic = **10.13** (p = **2.70e-20**), Residual SE = **0.917** on **527** df, AIC = **1458.5**, BIC = **1522.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.9768** | 0.4312 | ±0.8623 | **+9.224** | **2.87e-20** | *** |
| Education: graduate level (vs college) | -0.1035 | 0.0857 | ±0.1715 | -1.207 | 0.2276 |  |
| **Education: high school or below (vs college)** | **+0.4706** | 0.1284 | ±0.2568 | **+3.665** | **2.47e-04** | *** |
| Site: UCSD (vs UAB) | +0.0781 | 0.0865 | ±0.1730 | +0.903 | 0.3665 |  |
| **Site: UW (vs UAB)** | **-0.4130** | 0.1002 | ±0.2005 | **-4.121** | **3.77e-05** | *** |
| Season: spring (vs autumn) | -0.1306 | 0.1135 | ±0.2270 | -1.151 | 0.2498 |  |
| Season: summer (vs autumn) | +0.0950 | 0.1084 | ±0.2167 | +0.877 | 0.3805 |  |
| Season: winter (vs autumn) | +0.0849 | 0.1219 | ±0.2437 | +0.697 | 0.4861 |  |
| **Age (years)** | **-0.0277** | 0.0041 | ±0.0081 | **-6.811** | **9.71e-12** | *** |
| BMI (kg/m2) | +0.0016 | 0.0067 | ±0.0134 | +0.232 | 0.8166 |  |
| Hypertension | +0.0457 | 0.0860 | ±0.1719 | +0.532 | 0.5947 |  |
| High cholesterol | -0.0210 | 0.0864 | ±0.1729 | -0.243 | 0.8076 |  |
| Kidney disease | -0.0095 | 0.0989 | ±0.1978 | -0.096 | 0.9237 |  |
| Circulatory disease | -0.0273 | 0.0921 | ±0.1843 | -0.296 | 0.7669 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0036** | 0.0017 | ±0.0035 | **-2.053** | **0.0401** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.2059**, Adj R² = **0.1848**, F-statistic = **9.76** (p = **1.76e-19**), Residual SE = **0.920** on **527** df, AIC = **1462.7**, BIC = **1527.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6965** | 0.4066 | ±0.8132 | **+9.091** | **9.79e-20** | *** |
| Education: graduate level (vs college) | -0.1108 | 0.0855 | ±0.1710 | -1.296 | 0.1949 |  |
| **Education: high school or below (vs college)** | **+0.4986** | 0.1321 | ±0.2643 | **+3.774** | **1.61e-04** | *** |
| Site: UCSD (vs UAB) | +0.0611 | 0.0870 | ±0.1739 | +0.702 | 0.4825 |  |
| **Site: UW (vs UAB)** | **-0.4247** | 0.1012 | ±0.2024 | **-4.197** | **2.71e-05** | *** |
| Season: spring (vs autumn) | -0.1229 | 0.1133 | ±0.2267 | -1.084 | 0.2783 |  |
| Season: summer (vs autumn) | +0.0878 | 0.1091 | ±0.2183 | +0.804 | 0.4213 |  |
| Season: winter (vs autumn) | +0.1091 | 0.1229 | ±0.2459 | +0.888 | 0.3748 |  |
| **Age (years)** | **-0.0279** | 0.0041 | ±0.0082 | **-6.789** | **1.13e-11** | *** |
| BMI (kg/m2) | +0.0029 | 0.0066 | ±0.0132 | +0.434 | 0.6646 |  |
| Hypertension | +0.0331 | 0.0862 | ±0.1724 | +0.384 | 0.7011 |  |
| High cholesterol | -0.0246 | 0.0868 | ±0.1736 | -0.283 | 0.7773 |  |
| Kidney disease | +0.0016 | 0.0990 | ±0.1980 | +0.016 | 0.9875 |  |
| Circulatory disease | -0.0224 | 0.0945 | ±0.1891 | -0.237 | 0.8129 |  |
| Any reading < 54 during wear (0/1) | +0.1034 | 0.1038 | ±0.2075 | +0.997 | 0.3189 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.2102**, Adj R² = **0.1892**, F-statistic = **10.02** (p = **4.76e-20**), Residual SE = **0.918** on **527** df, AIC = **1459.8**, BIC = **1524.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7038** | 0.4054 | ±0.8108 | **+9.136** | **6.50e-20** | *** |
| Education: graduate level (vs college) | -0.1041 | 0.0852 | ±0.1703 | -1.223 | 0.2213 |  |
| **Education: high school or below (vs college)** | **+0.5067** | 0.1314 | ±0.2627 | **+3.857** | **1.15e-04** | *** |
| Site: UCSD (vs UAB) | +0.0717 | 0.0877 | ±0.1754 | +0.818 | 0.4134 |  |
| **Site: UW (vs UAB)** | **-0.4086** | 0.1010 | ±0.2020 | **-4.046** | **5.21e-05** | *** |
| Season: spring (vs autumn) | -0.1134 | 0.1139 | ±0.2278 | -0.996 | 0.3192 |  |
| Season: summer (vs autumn) | +0.0975 | 0.1087 | ±0.2174 | +0.897 | 0.3699 |  |
| Season: winter (vs autumn) | +0.1167 | 0.1238 | ±0.2477 | +0.943 | 0.3459 |  |
| **Age (years)** | **-0.0283** | 0.0041 | ±0.0083 | **-6.844** | **7.72e-12** | *** |
| BMI (kg/m2) | +0.0028 | 0.0065 | ±0.0130 | +0.439 | 0.6609 |  |
| Hypertension | +0.0224 | 0.0867 | ±0.1735 | +0.258 | 0.7966 |  |
| High cholesterol | -0.0157 | 0.0884 | ±0.1767 | -0.178 | 0.8588 |  |
| Kidney disease | +0.0000 | 0.0984 | ±0.1968 | +0.000 | 0.9998 |  |
| Circulatory disease | -0.0022 | 0.0926 | ±0.1851 | -0.023 | 0.9813 |  |
| Time < 54 (%) | +0.3179 | 0.2991 | ±0.5982 | +1.063 | 0.2878 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.2089**, Adj R² = **0.1879**, F-statistic = **9.94** (p = **6.89e-20**), Residual SE = **0.918** on **527** df, AIC = **1460.6**, BIC = **1525.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7149** | 0.4055 | ±0.8109 | **+9.162** | **5.08e-20** | *** |
| Education: graduate level (vs college) | -0.1065 | 0.0849 | ±0.1698 | -1.254 | 0.2100 |  |
| **Education: high school or below (vs college)** | **+0.5048** | 0.1315 | ±0.2630 | **+3.839** | **1.23e-04** | *** |
| Site: UCSD (vs UAB) | +0.0666 | 0.0875 | ±0.1751 | +0.760 | 0.4470 |  |
| **Site: UW (vs UAB)** | **-0.4152** | 0.1029 | ±0.2057 | **-4.036** | **5.44e-05** | *** |
| Season: spring (vs autumn) | -0.1046 | 0.1138 | ±0.2275 | -0.919 | 0.3580 |  |
| Season: summer (vs autumn) | +0.1020 | 0.1087 | ±0.2173 | +0.939 | 0.3479 |  |
| Season: winter (vs autumn) | +0.1165 | 0.1236 | ±0.2472 | +0.943 | 0.3459 |  |
| **Age (years)** | **-0.0282** | 0.0042 | ±0.0083 | **-6.775** | **1.25e-11** | *** |
| BMI (kg/m2) | +0.0027 | 0.0065 | ±0.0130 | +0.415 | 0.6782 |  |
| Hypertension | +0.0306 | 0.0864 | ±0.1728 | +0.354 | 0.7231 |  |
| High cholesterol | -0.0195 | 0.0872 | ±0.1745 | -0.224 | 0.8228 |  |
| Kidney disease | -0.0022 | 0.1016 | ±0.2031 | -0.022 | 0.9826 |  |
| Circulatory disease | -0.0083 | 0.0931 | ±0.1861 | -0.089 | 0.9289 |  |
| Avg. daily time < 54 (%) | +0.2053 | 0.5683 | ±1.1365 | +0.361 | 0.7179 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.2067**, Adj R² = **0.1856**, F-statistic = **9.81** (p = **1.35e-19**), Residual SE = **0.920** on **527** df, AIC = **1462.1**, BIC = **1526.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7071** | 0.4064 | ±0.8128 | **+9.122** | **7.37e-20** | *** |
| Education: graduate level (vs college) | -0.1076 | 0.0854 | ±0.1708 | -1.260 | 0.2077 |  |
| **Education: high school or below (vs college)** | **+0.4972** | 0.1327 | ±0.2654 | **+3.747** | **1.79e-04** | *** |
| Site: UCSD (vs UAB) | +0.0678 | 0.0869 | ±0.1738 | +0.780 | 0.4353 |  |
| **Site: UW (vs UAB)** | **-0.4182** | 0.1009 | ±0.2018 | **-4.144** | **3.41e-05** | *** |
| Season: spring (vs autumn) | -0.1109 | 0.1145 | ±0.2290 | -0.969 | 0.3327 |  |
| Season: summer (vs autumn) | +0.0955 | 0.1094 | ±0.2188 | +0.873 | 0.3829 |  |
| Season: winter (vs autumn) | +0.1116 | 0.1242 | ±0.2485 | +0.898 | 0.3692 |  |
| **Age (years)** | **-0.0284** | 0.0042 | ±0.0083 | **-6.820** | **9.12e-12** | *** |
| BMI (kg/m2) | +0.0032 | 0.0066 | ±0.0132 | +0.478 | 0.6328 |  |
| Hypertension | +0.0319 | 0.0855 | ±0.1710 | +0.373 | 0.7089 |  |
| High cholesterol | -0.0206 | 0.0876 | ±0.1753 | -0.235 | 0.8143 |  |
| Kidney disease | -0.0024 | 0.0984 | ±0.1968 | -0.024 | 0.9808 |  |
| Circulatory disease | -0.0095 | 0.0933 | ±0.1866 | -0.102 | 0.9190 |  |
| Time 54-69, pooled (%) | +0.0582 | 0.0590 | ±0.1180 | +0.986 | 0.3240 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **542**, R² = **0.2075**, Adj R² = **0.1864**, F-statistic = **9.85** (p = **1.08e-19**), Residual SE = **0.919** on **527** df, AIC = **1461.6**, BIC = **1526.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7126** | 0.4061 | ±0.8121 | **+9.143** | **6.09e-20** | *** |
| Education: graduate level (vs college) | -0.1059 | 0.0851 | ±0.1702 | -1.245 | 0.2133 |  |
| **Education: high school or below (vs college)** | **+0.4984** | 0.1328 | ±0.2656 | **+3.753** | **1.75e-04** | *** |
| Site: UCSD (vs UAB) | +0.0696 | 0.0869 | ±0.1737 | +0.801 | 0.4231 |  |
| **Site: UW (vs UAB)** | **-0.4149** | 0.1006 | ±0.2011 | **-4.126** | **3.70e-05** | *** |
| Season: spring (vs autumn) | -0.1093 | 0.1143 | ±0.2286 | -0.956 | 0.3388 |  |
| Season: summer (vs autumn) | +0.0966 | 0.1092 | ±0.2184 | +0.885 | 0.3761 |  |
| Season: winter (vs autumn) | +0.1124 | 0.1242 | ±0.2483 | +0.906 | 0.3652 |  |
| **Age (years)** | **-0.0284** | 0.0042 | ±0.0083 | **-6.828** | **8.59e-12** | *** |
| BMI (kg/m2) | +0.0030 | 0.0066 | ±0.0132 | +0.460 | 0.6454 |  |
| Hypertension | +0.0301 | 0.0855 | ±0.1711 | +0.352 | 0.7246 |  |
| High cholesterol | -0.0185 | 0.0877 | ±0.1754 | -0.211 | 0.8328 |  |
| Kidney disease | -0.0024 | 0.0981 | ±0.1962 | -0.024 | 0.9806 |  |
| Circulatory disease | -0.0074 | 0.0928 | ±0.1855 | -0.080 | 0.9364 |  |
| Avg. daily time 54-69 (%) | +0.0632 | 0.0572 | ±0.1144 | +1.106 | 0.2688 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **542**, R² = **0.2079**, Adj R² = **0.1868**, F-statistic = **9.88** (p = **9.51e-20**), Residual SE = **0.919** on **527** df, AIC = **1461.3**, BIC = **1525.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7002** | 0.4062 | ±0.8125 | **+9.109** | **8.34e-20** | *** |
| Education: graduate level (vs college) | -0.1063 | 0.0853 | ±0.1706 | -1.245 | 0.2130 |  |
| **Education: high school or below (vs college)** | **+0.4991** | 0.1326 | ±0.2651 | **+3.765** | **1.66e-04** | *** |
| Site: UCSD (vs UAB) | +0.0713 | 0.0871 | ±0.1742 | +0.818 | 0.4131 |  |
| **Site: UW (vs UAB)** | **-0.4138** | 0.1008 | ±0.2016 | **-4.104** | **4.06e-05** | *** |
| Season: spring (vs autumn) | -0.1092 | 0.1144 | ±0.2287 | -0.955 | 0.3396 |  |
| Season: summer (vs autumn) | +0.0978 | 0.1093 | ±0.2186 | +0.895 | 0.3706 |  |
| Season: winter (vs autumn) | +0.1146 | 0.1244 | ±0.2489 | +0.921 | 0.3570 |  |
| **Age (years)** | **-0.0284** | 0.0042 | ±0.0083 | **-6.828** | **8.62e-12** | *** |
| BMI (kg/m2) | +0.0031 | 0.0066 | ±0.0131 | +0.479 | 0.6319 |  |
| Hypertension | +0.0280 | 0.0858 | ±0.1716 | +0.326 | 0.7443 |  |
| High cholesterol | -0.0175 | 0.0882 | ±0.1763 | -0.198 | 0.8430 |  |
| Kidney disease | -0.0032 | 0.0982 | ±0.1963 | -0.033 | 0.9739 |  |
| Circulatory disease | -0.0068 | 0.0931 | ±0.1862 | -0.073 | 0.9416 |  |
| Time < 70 (%) | +0.0592 | 0.0523 | ±0.1047 | +1.131 | 0.2581 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **542**, R² = **0.2085**, Adj R² = **0.1875**, F-statistic = **9.92** (p = **7.86e-20**), Residual SE = **0.919** on **527** df, AIC = **1460.9**, BIC = **1525.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.7085** | 0.4056 | ±0.8112 | **+9.143** | **6.06e-20** | *** |
| Education: graduate level (vs college) | -0.1051 | 0.0850 | ±0.1700 | -1.237 | 0.2162 |  |
| **Education: high school or below (vs college)** | **+0.5005** | 0.1326 | ±0.2652 | **+3.775** | **1.60e-04** | *** |
| Site: UCSD (vs UAB) | +0.0716 | 0.0869 | ±0.1738 | +0.824 | 0.4099 |  |
| **Site: UW (vs UAB)** | **-0.4119** | 0.1005 | ±0.2011 | **-4.097** | **4.19e-05** | *** |
| Season: spring (vs autumn) | -0.1057 | 0.1142 | ±0.2284 | -0.925 | 0.3548 |  |
| Season: summer (vs autumn) | +0.1002 | 0.1091 | ±0.2181 | +0.919 | 0.3582 |  |
| Season: winter (vs autumn) | +0.1157 | 0.1243 | ±0.2485 | +0.931 | 0.3518 |  |
| **Age (years)** | **-0.0284** | 0.0042 | ±0.0083 | **-6.832** | **8.39e-12** | *** |
| BMI (kg/m2) | +0.0030 | 0.0066 | ±0.0131 | +0.452 | 0.6510 |  |
| Hypertension | +0.0279 | 0.0856 | ±0.1713 | +0.326 | 0.7442 |  |
| High cholesterol | -0.0164 | 0.0879 | ±0.1758 | -0.186 | 0.8522 |  |
| Kidney disease | -0.0035 | 0.0980 | ±0.1961 | -0.036 | 0.9714 |  |
| Circulatory disease | -0.0061 | 0.0926 | ±0.1853 | -0.065 | 0.9478 |  |
| Avg. daily time < 70 (%) | +0.0574 | 0.0545 | ±0.1089 | +1.054 | 0.2919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.2096**, Adj R² = **0.1886**, F-statistic = **9.98** (p = **5.59e-20**), Residual SE = **0.918** on **527** df, AIC = **1460.1**, BIC = **1524.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+4.0797** | 0.4753 | ±0.9507 | **+8.583** | **9.26e-18** | *** |
| Education: graduate level (vs college) | -0.0968 | 0.0866 | ±0.1732 | -1.118 | 0.2634 |  |
| **Education: high school or below (vs college)** | **+0.4788** | 0.1287 | ±0.2575 | **+3.720** | **2.00e-04** | *** |
| Site: UCSD (vs UAB) | +0.0694 | 0.0869 | ±0.1738 | +0.799 | 0.4245 |  |
| **Site: UW (vs UAB)** | **-0.4108** | 0.1005 | ±0.2009 | **-4.089** | **4.34e-05** | *** |
| Season: spring (vs autumn) | -0.1212 | 0.1137 | ±0.2273 | -1.066 | 0.2863 |  |
| Season: summer (vs autumn) | +0.1049 | 0.1092 | ±0.2183 | +0.961 | 0.3365 |  |
| Season: winter (vs autumn) | +0.0984 | 0.1221 | ±0.2442 | +0.806 | 0.4205 |  |
| **Age (years)** | **-0.0274** | 0.0041 | ±0.0082 | **-6.643** | **3.07e-11** | *** |
| BMI (kg/m2) | +0.0023 | 0.0067 | ±0.0135 | +0.339 | 0.7343 |  |
| Hypertension | +0.0353 | 0.0857 | ±0.1713 | +0.412 | 0.6803 |  |
| High cholesterol | -0.0257 | 0.0864 | ±0.1727 | -0.297 | 0.7662 |  |
| Kidney disease | -0.0057 | 0.1002 | ±0.2005 | -0.057 | 0.9544 |  |
| Circulatory disease | -0.0230 | 0.0935 | ±0.1871 | -0.246 | 0.8059 |  |
| Time 54-250, pooled (%) | -0.0043 | 0.0029 | ±0.0058 | -1.484 | 0.1378 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.2098**, Adj R² = **0.1888**, F-statistic = **9.99** (p = **5.34e-20**), Residual SE = **0.918** on **527** df, AIC = **1460.0**, BIC = **1524.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+4.0953** | 0.4779 | ±0.9558 | **+8.569** | **1.04e-17** | *** |
| Education: graduate level (vs college) | -0.0968 | 0.0866 | ±0.1731 | -1.118 | 0.2636 |  |
| **Education: high school or below (vs college)** | **+0.4786** | 0.1287 | ±0.2574 | **+3.718** | **2.00e-04** | *** |
| Site: UCSD (vs UAB) | +0.0699 | 0.0868 | ±0.1735 | +0.806 | 0.4203 |  |
| **Site: UW (vs UAB)** | **-0.4112** | 0.1004 | ±0.2009 | **-4.094** | **4.24e-05** | *** |
| Season: spring (vs autumn) | -0.1220 | 0.1137 | ±0.2273 | -1.074 | 0.2830 |  |
| Season: summer (vs autumn) | +0.1038 | 0.1090 | ±0.2180 | +0.953 | 0.3408 |  |
| Season: winter (vs autumn) | +0.0974 | 0.1221 | ±0.2442 | +0.798 | 0.4249 |  |
| **Age (years)** | **-0.0275** | 0.0041 | ±0.0082 | **-6.667** | **2.60e-11** | *** |
| BMI (kg/m2) | +0.0023 | 0.0067 | ±0.0135 | +0.335 | 0.7376 |  |
| Hypertension | +0.0358 | 0.0857 | ±0.1713 | +0.418 | 0.6763 |  |
| High cholesterol | -0.0256 | 0.0863 | ±0.1726 | -0.297 | 0.7666 |  |
| Kidney disease | -0.0072 | 0.1002 | ±0.2004 | -0.072 | 0.9429 |  |
| Circulatory disease | -0.0238 | 0.0936 | ±0.1873 | -0.254 | 0.7994 |  |
| Avg. daily time 54-250 (%) | -0.0044 | 0.0029 | ±0.0058 | -1.513 | 0.1303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.2079**, Adj R² = **0.1869**, F-statistic = **9.88** (p = **9.43e-20**), Residual SE = **0.919** on **527** df, AIC = **1461.3**, BIC = **1525.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6755** | 0.4019 | ±0.8038 | **+9.145** | **5.96e-20** | *** |
| Education: graduate level (vs college) | -0.1154 | 0.0857 | ±0.1714 | -1.347 | 0.1781 |  |
| **Education: high school or below (vs college)** | **+0.4847** | 0.1318 | ±0.2637 | **+3.677** | **2.36e-04** | *** |
| Site: UCSD (vs UAB) | +0.0651 | 0.0867 | ±0.1735 | +0.751 | 0.4528 |  |
| **Site: UW (vs UAB)** | **-0.4313** | 0.1011 | ±0.2022 | **-4.266** | **1.99e-05** | *** |
| Season: spring (vs autumn) | -0.1328 | 0.1131 | ±0.2263 | -1.174 | 0.2405 |  |
| Season: summer (vs autumn) | +0.0784 | 0.1091 | ±0.2181 | +0.719 | 0.4722 |  |
| Season: winter (vs autumn) | +0.0856 | 0.1238 | ±0.2476 | +0.691 | 0.4893 |  |
| **Age (years)** | **-0.0284** | 0.0041 | ±0.0082 | **-6.933** | **4.11e-12** | *** |
| BMI (kg/m2) | +0.0019 | 0.0067 | ±0.0133 | +0.289 | 0.7728 |  |
| Hypertension | +0.0541 | 0.0855 | ±0.1711 | +0.633 | 0.5270 |  |
| High cholesterol | -0.0252 | 0.0860 | ±0.1720 | -0.293 | 0.7693 |  |
| Kidney disease | -0.0002 | 0.0987 | ±0.1974 | -0.002 | 0.9982 |  |
| Circulatory disease | -0.0229 | 0.0915 | ±0.1829 | -0.250 | 0.8024 |  |
| Time 181-250, pooled (%) | +0.0044 | 0.0028 | ±0.0056 | +1.561 | 0.1185 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **542**, R² = **0.2076**, Adj R² = **0.1866**, F-statistic = **9.86** (p = **1.03e-19**), Residual SE = **0.919** on **527** df, AIC = **1461.5**, BIC = **1525.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6767** | 0.4018 | ±0.8037 | **+9.150** | **5.69e-20** | *** |
| Education: graduate level (vs college) | -0.1161 | 0.0858 | ±0.1716 | -1.353 | 0.1761 |  |
| **Education: high school or below (vs college)** | **+0.4835** | 0.1318 | ±0.2636 | **+3.668** | **2.44e-04** | *** |
| Site: UCSD (vs UAB) | +0.0658 | 0.0868 | ±0.1736 | +0.758 | 0.4486 |  |
| **Site: UW (vs UAB)** | **-0.4301** | 0.1011 | ±0.2023 | **-4.253** | **2.11e-05** | *** |
| Season: spring (vs autumn) | -0.1324 | 0.1132 | ±0.2265 | -1.169 | 0.2425 |  |
| Season: summer (vs autumn) | +0.0785 | 0.1091 | ±0.2183 | +0.720 | 0.4718 |  |
| Season: winter (vs autumn) | +0.0853 | 0.1238 | ±0.2477 | +0.689 | 0.4907 |  |
| **Age (years)** | **-0.0283** | 0.0041 | ±0.0082 | **-6.917** | **4.62e-12** | *** |
| BMI (kg/m2) | +0.0019 | 0.0067 | ±0.0134 | +0.291 | 0.7708 |  |
| Hypertension | +0.0534 | 0.0857 | ±0.1715 | +0.623 | 0.5335 |  |
| High cholesterol | -0.0259 | 0.0860 | ±0.1720 | -0.301 | 0.7635 |  |
| Kidney disease | -0.0006 | 0.0987 | ±0.1974 | -0.006 | 0.9955 |  |
| Circulatory disease | -0.0221 | 0.0916 | ±0.1833 | -0.241 | 0.8094 |  |
| Avg. daily time 181-250 (%) | +0.0041 | 0.0027 | ±0.0054 | +1.518 | 0.1291 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **542**, R² = **0.2116**, Adj R² = **0.1906**, F-statistic = **10.10** (p = **3.09e-20**), Residual SE = **0.917** on **527** df, AIC = **1458.8**, BIC = **1523.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6190** | 0.4063 | ±0.8127 | **+8.906** | **5.27e-19** | *** |
| Education: graduate level (vs college) | -0.1031 | 0.0857 | ±0.1715 | -1.202 | 0.2294 |  |
| **Education: high school or below (vs college)** | **+0.4725** | 0.1285 | ±0.2569 | **+3.678** | **2.35e-04** | *** |
| Site: UCSD (vs UAB) | +0.0752 | 0.0866 | ±0.1732 | +0.868 | 0.3853 |  |
| **Site: UW (vs UAB)** | **-0.4150** | 0.1003 | ±0.2007 | **-4.137** | **3.53e-05** | *** |
| Season: spring (vs autumn) | -0.1303 | 0.1135 | ±0.2271 | -1.148 | 0.2511 |  |
| Season: summer (vs autumn) | +0.0955 | 0.1085 | ±0.2169 | +0.880 | 0.3787 |  |
| Season: winter (vs autumn) | +0.0863 | 0.1219 | ±0.2438 | +0.708 | 0.4792 |  |
| **Age (years)** | **-0.0277** | 0.0041 | ±0.0081 | **-6.805** | **1.01e-11** | *** |
| BMI (kg/m2) | +0.0016 | 0.0067 | ±0.0134 | +0.242 | 0.8088 |  |
| Hypertension | +0.0461 | 0.0859 | ±0.1718 | +0.537 | 0.5914 |  |
| High cholesterol | -0.0219 | 0.0864 | ±0.1728 | -0.254 | 0.7997 |  |
| Kidney disease | -0.0072 | 0.0992 | ±0.1983 | -0.073 | 0.9418 |  |
| Circulatory disease | -0.0274 | 0.0921 | ±0.1841 | -0.298 | 0.7658 |  |
| **Time > 180 (%)** | **+0.0035** | 0.0018 | ±0.0035 | **+1.981** | **0.0476** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **542**, R² = **0.2114**, Adj R² = **0.1904**, F-statistic = **10.09** (p = **3.28e-20**), Residual SE = **0.917** on **527** df, AIC = **1458.9**, BIC = **1523.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6258** | 0.4061 | ±0.8121 | **+8.929** | **4.30e-19** | *** |
| Education: graduate level (vs college) | -0.1042 | 0.0857 | ±0.1715 | -1.215 | 0.2244 |  |
| **Education: high school or below (vs college)** | **+0.4716** | 0.1284 | ±0.2568 | **+3.673** | **2.40e-04** | *** |
| Site: UCSD (vs UAB) | +0.0760 | 0.0866 | ±0.1732 | +0.877 | 0.3803 |  |
| **Site: UW (vs UAB)** | **-0.4150** | 0.1004 | ±0.2007 | **-4.135** | **3.54e-05** | *** |
| Season: spring (vs autumn) | -0.1312 | 0.1136 | ±0.2272 | -1.155 | 0.2482 |  |
| Season: summer (vs autumn) | +0.0937 | 0.1084 | ±0.2168 | +0.864 | 0.3873 |  |
| Season: winter (vs autumn) | +0.0848 | 0.1220 | ±0.2440 | +0.695 | 0.4870 |  |
| **Age (years)** | **-0.0277** | 0.0041 | ±0.0081 | **-6.809** | **9.80e-12** | *** |
| BMI (kg/m2) | +0.0016 | 0.0067 | ±0.0135 | +0.240 | 0.8103 |  |
| Hypertension | +0.0464 | 0.0859 | ±0.1719 | +0.540 | 0.5889 |  |
| High cholesterol | -0.0224 | 0.0863 | ±0.1727 | -0.260 | 0.7950 |  |
| Kidney disease | -0.0084 | 0.0991 | ±0.1982 | -0.085 | 0.9325 |  |
| Circulatory disease | -0.0274 | 0.0922 | ±0.1844 | -0.297 | 0.7667 |  |
| Avg. daily time > 180 (%) | +0.0034 | 0.0017 | ±0.0035 | +1.957 | 0.0503 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **542**, R² = **0.2130**, Adj R² = **0.1921**, F-statistic = **10.19** (p = **2.01e-20**), Residual SE = **0.916** on **527** df, AIC = **1457.8**, BIC = **1522.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6409** | 0.4034 | ±0.8068 | **+9.025** | **1.79e-19** | *** |
| Education: graduate level (vs college) | -0.0950 | 0.0861 | ±0.1722 | -1.103 | 0.2700 |  |
| **Education: high school or below (vs college)** | **+0.4750** | 0.1287 | ±0.2575 | **+3.689** | **2.25e-04** | *** |
| Site: UCSD (vs UAB) | +0.0799 | 0.0865 | ±0.1731 | +0.923 | 0.3558 |  |
| **Site: UW (vs UAB)** | **-0.4196** | 0.1004 | ±0.2008 | **-4.180** | **2.92e-05** | *** |
| Season: spring (vs autumn) | -0.1318 | 0.1132 | ±0.2265 | -1.164 | 0.2446 |  |
| Season: summer (vs autumn) | +0.0976 | 0.1078 | ±0.2157 | +0.905 | 0.3654 |  |
| Season: winter (vs autumn) | +0.0854 | 0.1219 | ±0.2438 | +0.700 | 0.4838 |  |
| **Age (years)** | **-0.0273** | 0.0041 | ±0.0081 | **-6.706** | **1.99e-11** | *** |
| BMI (kg/m2) | +0.0008 | 0.0068 | ±0.0135 | +0.121 | 0.9035 |  |
| Hypertension | +0.0468 | 0.0857 | ±0.1714 | +0.546 | 0.5854 |  |
| High cholesterol | -0.0188 | 0.0862 | ±0.1725 | -0.218 | 0.8277 |  |
| Kidney disease | -0.0057 | 0.0989 | ±0.1977 | -0.057 | 0.9543 |  |
| Circulatory disease | -0.0292 | 0.0925 | ±0.1851 | -0.315 | 0.7526 |  |
| **Nocturnal time > 180 (%)** | **+0.0034** | 0.0015 | ±0.0031 | **+2.184** | **0.0290** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.2095**, Adj R² = **0.1885**, F-statistic = **9.97** (p = **5.87e-20**), Residual SE = **0.918** on **527** df, AIC = **1460.3**, BIC = **1524.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6548** | 0.4134 | ±0.8267 | **+8.842** | **9.43e-19** | *** |
| Education: graduate level (vs college) | -0.0971 | 0.0866 | ±0.1732 | -1.122 | 0.2620 |  |
| **Education: high school or below (vs college)** | **+0.4790** | 0.1287 | ±0.2574 | **+3.722** | **1.98e-04** | *** |
| Site: UCSD (vs UAB) | +0.0689 | 0.0869 | ±0.1738 | +0.793 | 0.4277 |  |
| **Site: UW (vs UAB)** | **-0.4114** | 0.1005 | ±0.2010 | **-4.093** | **4.25e-05** | *** |
| Season: spring (vs autumn) | -0.1213 | 0.1136 | ±0.2273 | -1.067 | 0.2858 |  |
| Season: summer (vs autumn) | +0.1045 | 0.1092 | ±0.2184 | +0.957 | 0.3387 |  |
| Season: winter (vs autumn) | +0.0982 | 0.1221 | ±0.2443 | +0.804 | 0.4213 |  |
| **Age (years)** | **-0.0274** | 0.0041 | ±0.0082 | **-6.645** | **3.03e-11** | *** |
| BMI (kg/m2) | +0.0023 | 0.0067 | ±0.0135 | +0.341 | 0.7333 |  |
| Hypertension | +0.0357 | 0.0857 | ±0.1713 | +0.416 | 0.6771 |  |
| High cholesterol | -0.0260 | 0.0863 | ±0.1727 | -0.301 | 0.7635 |  |
| Kidney disease | -0.0055 | 0.1003 | ±0.2005 | -0.055 | 0.9561 |  |
| Circulatory disease | -0.0231 | 0.0935 | ±0.1871 | -0.246 | 0.8053 |  |
| Time > 250 (%) | +0.0042 | 0.0029 | ±0.0058 | +1.459 | 0.1446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 542)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **542**, R² = **0.2096**, Adj R² = **0.1886**, F-statistic = **9.98** (p = **5.69e-20**), Residual SE = **0.918** on **527** df, AIC = **1460.2**, BIC = **1524.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6612** | 0.4130 | ±0.8260 | **+8.865** | **7.67e-19** | *** |
| Education: graduate level (vs college) | -0.0971 | 0.0866 | ±0.1732 | -1.122 | 0.2619 |  |
| **Education: high school or below (vs college)** | **+0.4788** | 0.1287 | ±0.2574 | **+3.721** | **1.99e-04** | *** |
| Site: UCSD (vs UAB) | +0.0694 | 0.0868 | ±0.1735 | +0.799 | 0.4240 |  |
| **Site: UW (vs UAB)** | **-0.4119** | 0.1005 | ±0.2009 | **-4.099** | **4.14e-05** | *** |
| Season: spring (vs autumn) | -0.1224 | 0.1137 | ±0.2273 | -1.077 | 0.2816 |  |
| Season: summer (vs autumn) | +0.1032 | 0.1090 | ±0.2180 | +0.946 | 0.3441 |  |
| Season: winter (vs autumn) | +0.0972 | 0.1221 | ±0.2442 | +0.796 | 0.4262 |  |
| **Age (years)** | **-0.0275** | 0.0041 | ±0.0082 | **-6.670** | **2.56e-11** | *** |
| BMI (kg/m2) | +0.0023 | 0.0067 | ±0.0135 | +0.337 | 0.7361 |  |
| Hypertension | +0.0361 | 0.0857 | ±0.1713 | +0.422 | 0.6731 |  |
| High cholesterol | -0.0260 | 0.0863 | ±0.1725 | -0.301 | 0.7633 |  |
| Kidney disease | -0.0068 | 0.1002 | ±0.2005 | -0.068 | 0.9456 |  |
| Circulatory disease | -0.0238 | 0.0937 | ±0.1873 | -0.254 | 0.7993 |  |
| Avg. daily time > 250 (%) | +0.0043 | 0.0029 | ±0.0058 | +1.482 | 0.1384 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 542; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **542**, R² = **0.2737**, Adj R² = **0.2559**, F-statistic = **15.31** (p = **1.41e-29**), Residual SE = **2.036** on **528** df, AIC = **2322.5**, BIC = **2382.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3803** | 0.7956 | ±1.5911 | **+29.388** | **7.76e-190** | *** |
| Education: graduate level (vs college) | -0.1217 | 0.2020 | ±0.4040 | -0.603 | 0.5467 |  |
| Education: high school or below (vs college) | +0.1466 | 0.2573 | ±0.5145 | +0.570 | 0.5688 |  |
| Site: UCSD (vs UAB) | +0.0765 | 0.2194 | ±0.4388 | +0.349 | 0.7275 |  |
| **Site: UW (vs UAB)** | **-1.2098** | 0.2192 | ±0.4384 | **-5.520** | **3.40e-08** | *** |
| Season: spring (vs autumn) | -0.1583 | 0.2389 | ±0.4777 | -0.663 | 0.5074 |  |
| **Season: summer (vs autumn)** | **+1.9130** | 0.2706 | ±0.5411 | **+7.071** | **1.54e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9427** | 0.2532 | ±0.5064 | **-3.723** | **1.97e-04** | *** |
| Age (years) | +0.0153 | 0.0097 | ±0.0195 | +1.574 | 0.1154 |  |
| BMI (kg/m2) | +0.0195 | 0.0136 | ±0.0271 | +1.437 | 0.1508 |  |
| Hypertension | +0.1339 | 0.1932 | ±0.3863 | +0.693 | 0.4882 |  |
| High cholesterol | -0.0451 | 0.1951 | ±0.3903 | -0.231 | 0.8172 |  |
| Kidney disease | -0.0735 | 0.2233 | ±0.4467 | -0.329 | 0.7420 |  |
| Circulatory disease | +0.2037 | 0.2352 | ±0.4704 | +0.866 | 0.3865 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **542**, R² = **0.2738**, Adj R² = **0.2545**, F-statistic = **14.19** (p = **5.55e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2388.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4693** | 1.0238 | ±2.0475 | **+22.925** | **2.63e-116** | *** |
| Education: graduate level (vs college) | -0.1241 | 0.2055 | ±0.4110 | -0.604 | 0.5460 |  |
| Education: high school or below (vs college) | +0.1516 | 0.2587 | ±0.5174 | +0.586 | 0.5579 |  |
| Site: UCSD (vs UAB) | +0.0736 | 0.2233 | ±0.4466 | +0.330 | 0.7416 |  |
| **Site: UW (vs UAB)** | **-1.2132** | 0.2202 | ±0.4405 | **-5.509** | **3.62e-08** | *** |
| Season: spring (vs autumn) | -0.1607 | 0.2421 | ±0.4842 | -0.664 | 0.5068 |  |
| **Season: summer (vs autumn)** | **+1.9098** | 0.2736 | ±0.5472 | **+6.980** | **2.94e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9424** | 0.2540 | ±0.5081 | **-3.710** | **2.07e-04** | *** |
| Age (years) | +0.0152 | 0.0098 | ±0.0196 | +1.557 | 0.1194 |  |
| BMI (kg/m2) | +0.0197 | 0.0139 | ±0.0278 | +1.419 | 0.1559 |  |
| Hypertension | +0.1346 | 0.1936 | ±0.3872 | +0.695 | 0.4871 |  |
| High cholesterol | -0.0455 | 0.1960 | ±0.3920 | -0.232 | 0.8165 |  |
| Kidney disease | -0.0742 | 0.2257 | ±0.4514 | -0.329 | 0.7422 |  |
| Circulatory disease | +0.2051 | 0.2374 | ±0.4748 | +0.864 | 0.3877 |  |
| HbA1c (%) | -0.0123 | 0.0940 | ±0.1879 | -0.131 | 0.8959 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **542**, R² = **0.2741**, Adj R² = **0.2548**, F-statistic = **14.21** (p = **4.95e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.2**, BIC = **2388.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5875** | 0.8904 | ±1.7808 | **+26.491** | **1.22e-154** | *** |
| Education: graduate level (vs college) | -0.1274 | 0.2027 | ±0.4053 | -0.629 | 0.5297 |  |
| Education: high school or below (vs college) | +0.1584 | 0.2600 | ±0.5200 | +0.609 | 0.5423 |  |
| Site: UCSD (vs UAB) | +0.0668 | 0.2216 | ±0.4433 | +0.301 | 0.7631 |  |
| **Site: UW (vs UAB)** | **-1.2184** | 0.2219 | ±0.4439 | **-5.490** | **4.03e-08** | *** |
| Season: spring (vs autumn) | -0.1546 | 0.2392 | ±0.4785 | -0.646 | 0.5181 |  |
| **Season: summer (vs autumn)** | **+1.9057** | 0.2723 | ±0.5446 | **+6.998** | **2.59e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9358** | 0.2545 | ±0.5089 | **-3.678** | **2.35e-04** | *** |
| Age (years) | +0.0150 | 0.0097 | ±0.0195 | +1.541 | 0.1234 |  |
| BMI (kg/m2) | +0.0200 | 0.0136 | ±0.0273 | +1.466 | 0.1428 |  |
| Hypertension | +0.1338 | 0.1937 | ±0.3874 | +0.691 | 0.4897 |  |
| High cholesterol | -0.0481 | 0.1956 | ±0.3913 | -0.246 | 0.8060 |  |
| Kidney disease | -0.0697 | 0.2230 | ±0.4461 | -0.312 | 0.7547 |  |
| Circulatory disease | +0.2096 | 0.2370 | ±0.4740 | +0.884 | 0.3765 |  |
| Mean glucose (mg/dL) | -0.0012 | 0.0024 | ±0.0048 | -0.488 | 0.6258 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **542**, R² = **0.2741**, Adj R² = **0.2548**, F-statistic = **14.21** (p = **4.95e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.2**, BIC = **2388.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7478** | 1.0779 | ±2.1559 | **+22.031** | **1.47e-107** | *** |
| Education: graduate level (vs college) | -0.1274 | 0.2027 | ±0.4053 | -0.629 | 0.5297 |  |
| Education: high school or below (vs college) | +0.1584 | 0.2600 | ±0.5200 | +0.609 | 0.5423 |  |
| Site: UCSD (vs UAB) | +0.0668 | 0.2216 | ±0.4433 | +0.301 | 0.7631 |  |
| **Site: UW (vs UAB)** | **-1.2184** | 0.2219 | ±0.4439 | **-5.490** | **4.03e-08** | *** |
| Season: spring (vs autumn) | -0.1546 | 0.2392 | ±0.4785 | -0.646 | 0.5181 |  |
| **Season: summer (vs autumn)** | **+1.9057** | 0.2723 | ±0.5446 | **+6.998** | **2.59e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9358** | 0.2545 | ±0.5089 | **-3.678** | **2.35e-04** | *** |
| Age (years) | +0.0150 | 0.0097 | ±0.0195 | +1.541 | 0.1234 |  |
| BMI (kg/m2) | +0.0200 | 0.0136 | ±0.0273 | +1.466 | 0.1428 |  |
| Hypertension | +0.1338 | 0.1937 | ±0.3874 | +0.691 | 0.4897 |  |
| High cholesterol | -0.0481 | 0.1956 | ±0.3913 | -0.246 | 0.8060 |  |
| Kidney disease | -0.0697 | 0.2230 | ±0.4461 | -0.312 | 0.7547 |  |
| Circulatory disease | +0.2096 | 0.2370 | ±0.4740 | +0.884 | 0.3765 |  |
| GMI (%) | -0.0485 | 0.0994 | ±0.1987 | -0.488 | 0.6258 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **542**, R² = **0.2739**, Adj R² = **0.2546**, F-statistic = **14.20** (p = **5.40e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.4**, BIC = **2388.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4888** | 0.8729 | ±1.7458 | **+26.908** | **1.75e-159** | *** |
| Education: graduate level (vs college) | -0.1260 | 0.2031 | ±0.4063 | -0.620 | 0.5351 |  |
| Education: high school or below (vs college) | +0.1524 | 0.2596 | ±0.5191 | +0.587 | 0.5571 |  |
| Site: UCSD (vs UAB) | +0.0704 | 0.2218 | ±0.4437 | +0.317 | 0.7509 |  |
| **Site: UW (vs UAB)** | **-1.2124** | 0.2211 | ±0.4422 | **-5.484** | **4.16e-08** | *** |
| Season: spring (vs autumn) | -0.1550 | 0.2397 | ±0.4794 | -0.647 | 0.5179 |  |
| **Season: summer (vs autumn)** | **+1.9094** | 0.2719 | ±0.5437 | **+7.023** | **2.17e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9384** | 0.2544 | ±0.5089 | **-3.688** | **2.26e-04** | *** |
| Age (years) | +0.0151 | 0.0098 | ±0.0196 | +1.539 | 0.1239 |  |
| BMI (kg/m2) | +0.0200 | 0.0138 | ±0.0277 | +1.442 | 0.1493 |  |
| Hypertension | +0.1332 | 0.1939 | ±0.3878 | +0.687 | 0.4921 |  |
| High cholesterol | -0.0469 | 0.1957 | ±0.3914 | -0.240 | 0.8106 |  |
| Kidney disease | -0.0731 | 0.2235 | ±0.4470 | -0.327 | 0.7437 |  |
| Circulatory disease | +0.2071 | 0.2373 | ±0.4745 | +0.873 | 0.3827 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0006 | 0.0023 | ±0.0046 | -0.275 | 0.7836 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2742**, Adj R² = **0.2550**, F-statistic = **14.22** (p = **4.73e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.2**, BIC = **2388.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5707** | 0.8563 | ±1.7126 | **+27.527** | **8.41e-167** | *** |
| Education: graduate level (vs college) | -0.1295 | 0.2028 | ±0.4057 | -0.638 | 0.5232 |  |
| Education: high school or below (vs college) | +0.1603 | 0.2598 | ±0.5195 | +0.617 | 0.5371 |  |
| Site: UCSD (vs UAB) | +0.0679 | 0.2211 | ±0.4423 | +0.307 | 0.7587 |  |
| **Site: UW (vs UAB)** | **-1.2262** | 0.2232 | ±0.4465 | **-5.492** | **3.96e-08** | *** |
| Season: spring (vs autumn) | -0.1535 | 0.2394 | ±0.4787 | -0.641 | 0.5212 |  |
| **Season: summer (vs autumn)** | **+1.9030** | 0.2723 | ±0.5446 | **+6.989** | **2.78e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9354** | 0.2536 | ±0.5072 | **-3.688** | **2.26e-04** | *** |
| Age (years) | +0.0152 | 0.0098 | ±0.0195 | +1.552 | 0.1207 |  |
| BMI (kg/m2) | +0.0198 | 0.0136 | ±0.0272 | +1.457 | 0.1451 |  |
| Hypertension | +0.1373 | 0.1936 | ±0.3871 | +0.710 | 0.4780 |  |
| High cholesterol | -0.0503 | 0.1954 | ±0.3908 | -0.258 | 0.7967 |  |
| Kidney disease | -0.0500 | 0.2263 | ±0.4527 | -0.221 | 0.8250 |  |
| Circulatory disease | +0.2093 | 0.2365 | ±0.4731 | +0.885 | 0.3762 |  |
| Glucose SD, pooled (mg/dL) | -0.0045 | 0.0077 | ±0.0155 | -0.582 | 0.5604 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2748**, Adj R² = **0.2555**, F-statistic = **14.26** (p = **3.97e-29**), Residual SE = **2.036** on **527** df, AIC = **2323.8**, BIC = **2388.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6645** | 0.8631 | ±1.7263 | **+27.417** | **1.71e-165** | *** |
| Education: graduate level (vs college) | -0.1306 | 0.2028 | ±0.4056 | -0.644 | 0.5196 |  |
| Education: high school or below (vs college) | +0.1699 | 0.2600 | ±0.5200 | +0.653 | 0.5135 |  |
| Site: UCSD (vs UAB) | +0.0644 | 0.2208 | ±0.4417 | +0.291 | 0.7707 |  |
| **Site: UW (vs UAB)** | **-1.2304** | 0.2222 | ±0.4443 | **-5.538** | **3.05e-08** | *** |
| Season: spring (vs autumn) | -0.1504 | 0.2394 | ±0.4788 | -0.628 | 0.5299 |  |
| **Season: summer (vs autumn)** | **+1.8975** | 0.2721 | ±0.5442 | **+6.973** | **3.10e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9357** | 0.2534 | ±0.5067 | **-3.693** | **2.21e-04** | *** |
| Age (years) | +0.0152 | 0.0098 | ±0.0196 | +1.553 | 0.1203 |  |
| BMI (kg/m2) | +0.0195 | 0.0136 | ±0.0272 | +1.432 | 0.1521 |  |
| Hypertension | +0.1364 | 0.1935 | ±0.3870 | +0.705 | 0.4810 |  |
| High cholesterol | -0.0514 | 0.1952 | ±0.3905 | -0.263 | 0.7924 |  |
| Kidney disease | -0.0375 | 0.2259 | ±0.4517 | -0.166 | 0.8681 |  |
| Circulatory disease | +0.2091 | 0.2364 | ±0.4727 | +0.885 | 0.3764 |  |
| Avg. daily SD (mg/dL) | -0.0073 | 0.0085 | ±0.0170 | -0.858 | 0.3909 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **542**, R² = **0.2738**, Adj R² = **0.2545**, F-statistic = **14.19** (p = **5.59e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2388.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4305** | 0.8766 | ±1.7532 | **+26.729** | **2.17e-157** | *** |
| Education: graduate level (vs college) | -0.1226 | 0.2024 | ±0.4048 | -0.606 | 0.5448 |  |
| Education: high school or below (vs college) | +0.1478 | 0.2581 | ±0.5163 | +0.573 | 0.5668 |  |
| Site: UCSD (vs UAB) | +0.0760 | 0.2199 | ±0.4398 | +0.345 | 0.7297 |  |
| **Site: UW (vs UAB)** | **-1.2125** | 0.2208 | ±0.4416 | **-5.491** | **4.00e-08** | *** |
| Season: spring (vs autumn) | -0.1584 | 0.2394 | ±0.4788 | -0.662 | 0.5081 |  |
| **Season: summer (vs autumn)** | **+1.9119** | 0.2710 | ±0.5420 | **+7.056** | **1.72e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9424** | 0.2537 | ±0.5073 | **-3.715** | **2.03e-04** | *** |
| Age (years) | +0.0154 | 0.0098 | ±0.0195 | +1.574 | 0.1156 |  |
| BMI (kg/m2) | +0.0195 | 0.0136 | ±0.0272 | +1.431 | 0.1524 |  |
| Hypertension | +0.1352 | 0.1947 | ±0.3894 | +0.694 | 0.4875 |  |
| High cholesterol | -0.0457 | 0.1954 | ±0.3908 | -0.234 | 0.8149 |  |
| Kidney disease | -0.0679 | 0.2289 | ±0.4578 | -0.297 | 0.7667 |  |
| Circulatory disease | +0.2038 | 0.2356 | ±0.4712 | +0.865 | 0.3871 |  |
| CV (%) | -0.0021 | 0.0157 | ±0.0315 | -0.134 | 0.8938 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **542**, R² = **0.2739**, Adj R² = **0.2546**, F-statistic = **14.20** (p = **5.40e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.4**, BIC = **2388.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4992** | 0.8906 | ±1.7812 | **+26.385** | **2.03e-153** | *** |
| Education: graduate level (vs college) | -0.1198 | 0.2021 | ±0.4042 | -0.593 | 0.5533 |  |
| Education: high school or below (vs college) | +0.1444 | 0.2583 | ±0.5166 | +0.559 | 0.5760 |  |
| Site: UCSD (vs UAB) | +0.0760 | 0.2197 | ±0.4394 | +0.346 | 0.7295 |  |
| **Site: UW (vs UAB)** | **-1.2055** | 0.2203 | ±0.4406 | **-5.472** | **4.45e-08** | *** |
| Season: spring (vs autumn) | -0.1594 | 0.2395 | ±0.4790 | -0.666 | 0.5056 |  |
| **Season: summer (vs autumn)** | **+1.9122** | 0.2710 | ±0.5421 | **+7.055** | **1.72e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9441** | 0.2537 | ±0.5073 | **-3.722** | **1.97e-04** | *** |
| Age (years) | +0.0153 | 0.0098 | ±0.0195 | +1.569 | 0.1165 |  |
| BMI (kg/m2) | +0.0196 | 0.0136 | ±0.0272 | +1.443 | 0.1490 |  |
| Hypertension | +0.1320 | 0.1941 | ±0.3882 | +0.680 | 0.4965 |  |
| High cholesterol | -0.0456 | 0.1956 | ±0.3911 | -0.233 | 0.8158 |  |
| Kidney disease | -0.0839 | 0.2271 | ±0.4541 | -0.370 | 0.7117 |  |
| Circulatory disease | +0.2021 | 0.2351 | ±0.4702 | +0.860 | 0.3899 |  |
| Mean / SD ratio | -0.0274 | 0.0875 | ±0.1751 | -0.313 | 0.7544 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2737**, Adj R² = **0.2544**, F-statistic = **14.19** (p = **5.63e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2389.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3572** | 0.8824 | ±1.7648 | **+26.470** | **2.13e-154** | *** |
| Education: graduate level (vs college) | -0.1221 | 0.2026 | ±0.4052 | -0.603 | 0.5466 |  |
| Education: high school or below (vs college) | +0.1472 | 0.2583 | ±0.5165 | +0.570 | 0.5688 |  |
| Site: UCSD (vs UAB) | +0.0766 | 0.2198 | ±0.4397 | +0.348 | 0.7275 |  |
| **Site: UW (vs UAB)** | **-1.2105** | 0.2198 | ±0.4397 | **-5.506** | **3.67e-08** | *** |
| Season: spring (vs autumn) | -0.1584 | 0.2396 | ±0.4791 | -0.661 | 0.5085 |  |
| **Season: summer (vs autumn)** | **+1.9129** | 0.2712 | ±0.5424 | **+7.054** | **1.74e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9427** | 0.2538 | ±0.5076 | **-3.715** | **2.04e-04** | *** |
| Age (years) | +0.0154 | 0.0098 | ±0.0195 | +1.574 | 0.1156 |  |
| BMI (kg/m2) | +0.0194 | 0.0137 | ±0.0274 | +1.417 | 0.1565 |  |
| Hypertension | +0.1341 | 0.1940 | ±0.3880 | +0.691 | 0.4893 |  |
| High cholesterol | -0.0451 | 0.1954 | ±0.3908 | -0.231 | 0.8174 |  |
| Kidney disease | -0.0715 | 0.2269 | ±0.4538 | -0.315 | 0.7528 |  |
| Circulatory disease | +0.2037 | 0.2358 | ±0.4716 | +0.864 | 0.3877 |  |
| Avg. daily mean/SD | +0.0047 | 0.0783 | ±0.1567 | +0.061 | 0.9518 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **542**, R² = **0.2742**, Adj R² = **0.2549**, F-statistic = **14.22** (p = **4.81e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.2**, BIC = **2388.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6853** | 0.9466 | ±1.8931 | **+25.023** | **3.47e-138** | *** |
| Education: graduate level (vs college) | -0.1304 | 0.2043 | ±0.4085 | -0.638 | 0.5233 |  |
| Education: high school or below (vs college) | +0.1544 | 0.2561 | ±0.5122 | +0.603 | 0.5465 |  |
| Site: UCSD (vs UAB) | +0.0707 | 0.2194 | ±0.4389 | +0.322 | 0.7473 |  |
| **Site: UW (vs UAB)** | **-1.2294** | 0.2195 | ±0.4391 | **-5.600** | **2.15e-08** | *** |
| Season: spring (vs autumn) | -0.1571 | 0.2397 | ±0.4795 | -0.655 | 0.5123 |  |
| **Season: summer (vs autumn)** | **+1.9004** | 0.2707 | ±0.5415 | **+7.019** | **2.23e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9438** | 0.2536 | ±0.5072 | **-3.722** | **1.98e-04** | *** |
| Age (years) | +0.0146 | 0.0098 | ±0.0196 | +1.491 | 0.1359 |  |
| BMI (kg/m2) | +0.0193 | 0.0136 | ±0.0272 | +1.424 | 0.1543 |  |
| Hypertension | +0.1348 | 0.1934 | ±0.3869 | +0.697 | 0.4859 |  |
| High cholesterol | -0.0481 | 0.1955 | ±0.3910 | -0.246 | 0.8058 |  |
| Kidney disease | -0.0599 | 0.2257 | ±0.4513 | -0.265 | 0.7907 |  |
| Circulatory disease | +0.2056 | 0.2357 | ±0.4715 | +0.872 | 0.3831 |  |
| MAG (mg/dL/h) | -0.0054 | 0.0090 | ±0.0180 | -0.596 | 0.5513 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **542**, R² = **0.2742**, Adj R² = **0.2549**, F-statistic = **14.22** (p = **4.80e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.2**, BIC = **2388.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6437** | 0.9039 | ±1.8078 | **+26.157** | **8.10e-151** | *** |
| Education: graduate level (vs college) | -0.1277 | 0.2026 | ±0.4052 | -0.630 | 0.5286 |  |
| Education: high school or below (vs college) | +0.1626 | 0.2594 | ±0.5188 | +0.627 | 0.5307 |  |
| Site: UCSD (vs UAB) | +0.0676 | 0.2204 | ±0.4408 | +0.307 | 0.7590 |  |
| **Site: UW (vs UAB)** | **-1.2236** | 0.2218 | ±0.4436 | **-5.517** | **3.45e-08** | *** |
| Season: spring (vs autumn) | -0.1510 | 0.2397 | ±0.4795 | -0.630 | 0.5288 |  |
| **Season: summer (vs autumn)** | **+1.9076** | 0.2711 | ±0.5421 | **+7.038** | **1.96e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9363** | 0.2540 | ±0.5080 | **-3.686** | **2.27e-04** | *** |
| Age (years) | +0.0150 | 0.0098 | ±0.0195 | +1.533 | 0.1253 |  |
| BMI (kg/m2) | +0.0193 | 0.0136 | ±0.0273 | +1.416 | 0.1568 |  |
| Hypertension | +0.1329 | 0.1934 | ±0.3868 | +0.687 | 0.4921 |  |
| High cholesterol | -0.0464 | 0.1953 | ±0.3906 | -0.238 | 0.8122 |  |
| Kidney disease | -0.0477 | 0.2271 | ±0.4541 | -0.210 | 0.8335 |  |
| Circulatory disease | +0.2088 | 0.2362 | ±0.4725 | +0.884 | 0.3767 |  |
| Avg. daily range (mg/dL) | -0.0015 | 0.0024 | ±0.0049 | -0.605 | 0.5454 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **542**, R² = **0.2738**, Adj R² = **0.2545**, F-statistic = **14.19** (p = **5.47e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2388.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3360** | 0.8144 | ±1.6289 | **+28.653** | **1.47e-180** | *** |
| Education: graduate level (vs college) | -0.1169 | 0.2036 | ±0.4071 | -0.574 | 0.5657 |  |
| Education: high school or below (vs college) | +0.1454 | 0.2584 | ±0.5168 | +0.563 | 0.5737 |  |
| Site: UCSD (vs UAB) | +0.0791 | 0.2215 | ±0.4430 | +0.357 | 0.7210 |  |
| **Site: UW (vs UAB)** | **-1.2040** | 0.2248 | ±0.4496 | **-5.356** | **8.51e-08** | *** |
| Season: spring (vs autumn) | -0.1579 | 0.2393 | ±0.4787 | -0.660 | 0.5095 |  |
| **Season: summer (vs autumn)** | **+1.9148** | 0.2718 | ±0.5435 | **+7.046** | **1.85e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9466** | 0.2536 | ±0.5073 | **-3.732** | **1.90e-04** | *** |
| Age (years) | +0.0156 | 0.0098 | ±0.0195 | +1.593 | 0.1111 |  |
| BMI (kg/m2) | +0.0192 | 0.0138 | ±0.0276 | +1.389 | 0.1647 |  |
| Hypertension | +0.1306 | 0.1929 | ±0.3859 | +0.677 | 0.4985 |  |
| High cholesterol | -0.0431 | 0.1957 | ±0.3915 | -0.220 | 0.8257 |  |
| Kidney disease | -0.0776 | 0.2254 | ±0.4509 | -0.344 | 0.7308 |  |
| Circulatory disease | +0.1981 | 0.2370 | ±0.4740 | +0.836 | 0.4032 |  |
| SD of daily means (mg/dL) | +0.0027 | 0.0130 | ±0.0260 | +0.204 | 0.8381 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **542**, R² = **0.2741**, Adj R² = **0.2549**, F-statistic = **14.22** (p = **4.89e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.2**, BIC = **2388.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.2548** | 0.8456 | ±1.6912 | **+27.501** | **1.73e-166** | *** |
| Education: graduate level (vs college) | -0.1263 | 0.2026 | ±0.4052 | -0.623 | 0.5331 |  |
| Education: high school or below (vs college) | +0.1598 | 0.2604 | ±0.5208 | +0.614 | 0.5395 |  |
| Site: UCSD (vs UAB) | +0.0643 | 0.2215 | ±0.4429 | +0.290 | 0.7715 |  |
| **Site: UW (vs UAB)** | **-1.2192** | 0.2221 | ±0.4442 | **-5.489** | **4.04e-08** | *** |
| Season: spring (vs autumn) | -0.1540 | 0.2394 | ±0.4788 | -0.643 | 0.5201 |  |
| **Season: summer (vs autumn)** | **+1.9071** | 0.2723 | ±0.5446 | **+7.004** | **2.49e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9348** | 0.2546 | ±0.5093 | **-3.671** | **2.41e-04** | *** |
| Age (years) | +0.0151 | 0.0097 | ±0.0195 | +1.552 | 0.1207 |  |
| BMI (kg/m2) | +0.0202 | 0.0137 | ±0.0273 | +1.477 | 0.1396 |  |
| Hypertension | +0.1324 | 0.1940 | ±0.3880 | +0.683 | 0.4949 |  |
| High cholesterol | -0.0509 | 0.1959 | ±0.3918 | -0.260 | 0.7952 |  |
| Kidney disease | -0.0671 | 0.2225 | ±0.4450 | -0.302 | 0.7630 |  |
| Circulatory disease | +0.2097 | 0.2370 | ±0.4741 | +0.885 | 0.3763 |  |
| Time in range 70-180, pooled (%) | +0.0019 | 0.0038 | ±0.0075 | +0.512 | 0.6084 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **542**, R² = **0.2743**, Adj R² = **0.2550**, F-statistic = **14.23** (p = **4.60e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.1**, BIC = **2388.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.2281** | 0.8465 | ±1.6930 | **+27.440** | **9.25e-166** | *** |
| Education: graduate level (vs college) | -0.1265 | 0.2025 | ±0.4050 | -0.625 | 0.5321 |  |
| Education: high school or below (vs college) | +0.1631 | 0.2605 | ±0.5211 | +0.626 | 0.5312 |  |
| Site: UCSD (vs UAB) | +0.0612 | 0.2216 | ±0.4431 | +0.276 | 0.7823 |  |
| **Site: UW (vs UAB)** | **-1.2212** | 0.2222 | ±0.4444 | **-5.496** | **3.88e-08** | *** |
| Season: spring (vs autumn) | -0.1526 | 0.2394 | ±0.4787 | -0.638 | 0.5237 |  |
| **Season: summer (vs autumn)** | **+1.9070** | 0.2721 | ±0.5443 | **+7.008** | **2.43e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9323** | 0.2549 | ±0.5098 | **-3.658** | **2.55e-04** | *** |
| Age (years) | +0.0151 | 0.0097 | ±0.0195 | +1.550 | 0.1213 |  |
| BMI (kg/m2) | +0.0203 | 0.0137 | ±0.0273 | +1.489 | 0.1365 |  |
| Hypertension | +0.1319 | 0.1941 | ±0.3881 | +0.679 | 0.4968 |  |
| High cholesterol | -0.0518 | 0.1959 | ±0.3917 | -0.264 | 0.7916 |  |
| Kidney disease | -0.0650 | 0.2223 | ±0.4446 | -0.292 | 0.7701 |  |
| Circulatory disease | +0.2109 | 0.2371 | ±0.4741 | +0.890 | 0.3736 |  |
| Avg. daily time in range 70-180 (%) | +0.0023 | 0.0037 | ±0.0075 | +0.609 | 0.5422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.2745**, Adj R² = **0.2552**, F-statistic = **14.24** (p = **4.37e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.0**, BIC = **2388.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4440** | 0.8108 | ±1.6216 | **+28.915** | **7.78e-184** | *** |
| Education: graduate level (vs college) | -0.1220 | 0.2023 | ±0.4047 | -0.603 | 0.5466 |  |
| Education: high school or below (vs college) | +0.1434 | 0.2564 | ±0.5127 | +0.559 | 0.5759 |  |
| Site: UCSD (vs UAB) | +0.0659 | 0.2221 | ±0.4442 | +0.297 | 0.7667 |  |
| **Site: UW (vs UAB)** | **-1.2194** | 0.2200 | ±0.4399 | **-5.544** | **2.96e-08** | *** |
| Season: spring (vs autumn) | -0.1565 | 0.2391 | ±0.4782 | -0.654 | 0.5128 |  |
| **Season: summer (vs autumn)** | **+1.9097** | 0.2710 | ±0.5420 | **+7.047** | **1.83e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9548** | 0.2528 | ±0.5056 | **-3.777** | **1.59e-04** | *** |
| Age (years) | +0.0149 | 0.0098 | ±0.0197 | +1.515 | 0.1297 |  |
| BMI (kg/m2) | +0.0195 | 0.0136 | ±0.0272 | +1.435 | 0.1512 |  |
| Hypertension | +0.1484 | 0.1958 | ±0.3917 | +0.758 | 0.4486 |  |
| High cholesterol | -0.0557 | 0.1938 | ±0.3877 | -0.287 | 0.7738 |  |
| Kidney disease | -0.0699 | 0.2237 | ±0.4475 | -0.312 | 0.7548 |  |
| Circulatory disease | +0.2136 | 0.2348 | ±0.4695 | +0.910 | 0.3629 |  |
| Any reading < 54 during wear (0/1) | -0.1586 | 0.2060 | ±0.4121 | -0.770 | 0.4416 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.2741**, Adj R² = **0.2548**, F-statistic = **14.21** (p = **5.04e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.3**, BIC = **2388.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3989** | 0.7977 | ±1.5955 | **+29.332** | **4.11e-189** | *** |
| Education: graduate level (vs college) | -0.1255 | 0.2021 | ±0.4042 | -0.621 | 0.5347 |  |
| Education: high school or below (vs college) | +0.1411 | 0.2574 | ±0.5148 | +0.548 | 0.5837 |  |
| Site: UCSD (vs UAB) | +0.0669 | 0.2213 | ±0.4427 | +0.302 | 0.7624 |  |
| **Site: UW (vs UAB)** | **-1.2220** | 0.2203 | ±0.4407 | **-5.546** | **2.93e-08** | *** |
| Season: spring (vs autumn) | -0.1628 | 0.2397 | ±0.4795 | -0.679 | 0.4971 |  |
| **Season: summer (vs autumn)** | **+1.9065** | 0.2704 | ±0.5409 | **+7.050** | **1.79e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9511** | 0.2532 | ±0.5064 | **-3.756** | **1.73e-04** | *** |
| Age (years) | +0.0154 | 0.0098 | ±0.0195 | +1.579 | 0.1143 |  |
| BMI (kg/m2) | +0.0195 | 0.0136 | ±0.0271 | +1.437 | 0.1506 |  |
| Hypertension | +0.1449 | 0.1959 | ±0.3918 | +0.740 | 0.4596 |  |
| High cholesterol | -0.0537 | 0.1954 | ±0.3908 | -0.275 | 0.7835 |  |
| Kidney disease | -0.0714 | 0.2237 | ±0.4475 | -0.319 | 0.7497 |  |
| Circulatory disease | +0.1962 | 0.2360 | ±0.4720 | +0.831 | 0.4058 |  |
| Time < 54 (%) | -0.1730 | 0.2859 | ±0.5719 | -0.605 | 0.5452 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.2744**, Adj R² = **0.2551**, F-statistic = **14.23** (p = **4.53e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.1**, BIC = **2388.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3999** | 0.7966 | ±1.5932 | **+29.375** | **1.15e-189** | *** |
| Education: graduate level (vs college) | -0.1256 | 0.2021 | ±0.4042 | -0.621 | 0.5343 |  |
| Education: high school or below (vs college) | +0.1396 | 0.2575 | ±0.5149 | +0.542 | 0.5876 |  |
| Site: UCSD (vs UAB) | +0.0660 | 0.2206 | ±0.4411 | +0.299 | 0.7648 |  |
| **Site: UW (vs UAB)** | **-1.2232** | 0.2203 | ±0.4406 | **-5.553** | **2.81e-08** | *** |
| Season: spring (vs autumn) | -0.1728 | 0.2401 | ±0.4801 | -0.720 | 0.4716 |  |
| **Season: summer (vs autumn)** | **+1.8991** | 0.2712 | ±0.5425 | **+7.001** | **2.53e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9557** | 0.2537 | ±0.5073 | **-3.768** | **1.65e-04** | *** |
| Age (years) | +0.0154 | 0.0098 | ±0.0195 | +1.580 | 0.1140 |  |
| BMI (kg/m2) | +0.0196 | 0.0136 | ±0.0271 | +1.447 | 0.1478 |  |
| Hypertension | +0.1440 | 0.1943 | ±0.3887 | +0.741 | 0.4587 |  |
| High cholesterol | -0.0552 | 0.1953 | ±0.3907 | -0.283 | 0.7774 |  |
| Kidney disease | -0.0683 | 0.2238 | ±0.4477 | -0.305 | 0.7602 |  |
| Circulatory disease | +0.1972 | 0.2356 | ±0.4712 | +0.837 | 0.4025 |  |
| Avg. daily time < 54 (%) | -0.1739 | 0.2390 | ±0.4781 | -0.728 | 0.4668 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.2740**, Adj R² = **0.2547**, F-statistic = **14.21** (p = **5.16e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.3**, BIC = **2388.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3577** | 0.8002 | ±1.6005 | **+29.189** | **2.70e-187** | *** |
| Education: graduate level (vs college) | -0.1192 | 0.2030 | ±0.4059 | -0.588 | 0.5568 |  |
| Education: high school or below (vs college) | +0.1471 | 0.2575 | ±0.5150 | +0.571 | 0.5678 |  |
| Site: UCSD (vs UAB) | +0.0865 | 0.2211 | ±0.4423 | +0.391 | 0.6959 |  |
| **Site: UW (vs UAB)** | **-1.2005** | 0.2217 | ±0.4435 | **-5.414** | **6.17e-08** | *** |
| Season: spring (vs autumn) | -0.1505 | 0.2379 | ±0.4759 | -0.632 | 0.5271 |  |
| **Season: summer (vs autumn)** | **+1.9202** | 0.2693 | ±0.5385 | **+7.131** | **9.94e-13** | *** |
| **Season: winter (vs autumn)** | **-0.9350** | 0.2521 | ±0.5043 | **-3.709** | **2.08e-04** | *** |
| Age (years) | +0.0152 | 0.0097 | ±0.0195 | +1.558 | 0.1192 |  |
| BMI (kg/m2) | +0.0197 | 0.0136 | ±0.0273 | +1.444 | 0.1488 |  |
| Hypertension | +0.1261 | 0.1971 | ±0.3942 | +0.640 | 0.5223 |  |
| High cholesterol | -0.0371 | 0.1961 | ±0.3923 | -0.189 | 0.8499 |  |
| Kidney disease | -0.0781 | 0.2245 | ±0.4490 | -0.348 | 0.7278 |  |
| Circulatory disease | +0.2084 | 0.2374 | ±0.4748 | +0.878 | 0.3801 |  |
| Time 54-69, pooled (%) | +0.0427 | 0.1123 | ±0.2246 | +0.380 | 0.7040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **542**, R² = **0.2744**, Adj R² = **0.2551**, F-statistic = **14.23** (p = **4.55e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.1**, BIC = **2388.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3547** | 0.7983 | ±1.5966 | **+29.256** | **3.75e-188** | *** |
| Education: graduate level (vs college) | -0.1167 | 0.2025 | ±0.4051 | -0.576 | 0.5646 |  |
| Education: high school or below (vs college) | +0.1485 | 0.2574 | ±0.5147 | +0.577 | 0.5640 |  |
| Site: UCSD (vs UAB) | +0.0920 | 0.2209 | ±0.4417 | +0.417 | 0.6770 |  |
| **Site: UW (vs UAB)** | **-1.1937** | 0.2211 | ±0.4422 | **-5.398** | **6.72e-08** | *** |
| Season: spring (vs autumn) | -0.1459 | 0.2379 | ±0.4757 | -0.613 | 0.5396 |  |
| **Season: summer (vs autumn)** | **+1.9242** | 0.2695 | ±0.5390 | **+7.140** | **9.32e-13** | *** |
| **Season: winter (vs autumn)** | **-0.9313** | 0.2526 | ±0.5052 | **-3.687** | **2.27e-04** | *** |
| Age (years) | +0.0150 | 0.0097 | ±0.0195 | +1.545 | 0.1223 |  |
| BMI (kg/m2) | +0.0196 | 0.0136 | ±0.0272 | +1.442 | 0.1494 |  |
| Hypertension | +0.1214 | 0.1966 | ±0.3931 | +0.617 | 0.5370 |  |
| High cholesterol | -0.0321 | 0.1959 | ±0.3918 | -0.164 | 0.8700 |  |
| Kidney disease | -0.0799 | 0.2244 | ±0.4488 | -0.356 | 0.7219 |  |
| Circulatory disease | +0.2123 | 0.2367 | ±0.4733 | +0.897 | 0.3698 |  |
| Avg. daily time 54-69 (%) | +0.0638 | 0.1019 | ±0.2038 | +0.626 | 0.5315 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **542**, R² = **0.2738**, Adj R² = **0.2545**, F-statistic = **14.19** (p = **5.48e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2388.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3671** | 0.8002 | ±1.6004 | **+29.201** | **1.89e-187** | *** |
| Education: graduate level (vs college) | -0.1201 | 0.2028 | ±0.4055 | -0.592 | 0.5537 |  |
| Education: high school or below (vs college) | +0.1475 | 0.2576 | ±0.5152 | +0.573 | 0.5669 |  |
| Site: UCSD (vs UAB) | +0.0825 | 0.2213 | ±0.4427 | +0.373 | 0.7095 |  |
| **Site: UW (vs UAB)** | **-1.2038** | 0.2215 | ±0.4430 | **-5.435** | **5.47e-08** | *** |
| Season: spring (vs autumn) | -0.1540 | 0.2384 | ±0.4768 | -0.646 | 0.5183 |  |
| **Season: summer (vs autumn)** | **+1.9173** | 0.2694 | ±0.5387 | **+7.118** | **1.10e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9379** | 0.2521 | ±0.5042 | **-3.720** | **1.99e-04** | *** |
| Age (years) | +0.0153 | 0.0098 | ±0.0195 | +1.565 | 0.1177 |  |
| BMI (kg/m2) | +0.0196 | 0.0136 | ±0.0272 | +1.438 | 0.1506 |  |
| Hypertension | +0.1288 | 0.1976 | ±0.3952 | +0.652 | 0.5146 |  |
| High cholesterol | -0.0402 | 0.1960 | ±0.3920 | -0.205 | 0.8375 |  |
| Kidney disease | -0.0760 | 0.2243 | ±0.4486 | -0.339 | 0.7347 |  |
| Circulatory disease | +0.2069 | 0.2371 | ±0.4742 | +0.872 | 0.3829 |  |
| Time < 70 (%) | +0.0208 | 0.0881 | ±0.1762 | +0.236 | 0.8138 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **542**, R² = **0.2739**, Adj R² = **0.2546**, F-statistic = **14.20** (p = **5.35e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.4**, BIC = **2388.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3674** | 0.7981 | ±1.5962 | **+29.279** | **1.95e-188** | *** |
| Education: graduate level (vs college) | -0.1192 | 0.2024 | ±0.4049 | -0.589 | 0.5561 |  |
| Education: high school or below (vs college) | +0.1483 | 0.2576 | ±0.5151 | +0.576 | 0.5646 |  |
| Site: UCSD (vs UAB) | +0.0841 | 0.2210 | ±0.4421 | +0.381 | 0.7035 |  |
| **Site: UW (vs UAB)** | **-1.2015** | 0.2211 | ±0.4421 | **-5.435** | **5.48e-08** | *** |
| Season: spring (vs autumn) | -0.1513 | 0.2383 | ±0.4766 | -0.635 | 0.5253 |  |
| **Season: summer (vs autumn)** | **+1.9194** | 0.2697 | ±0.5395 | **+7.116** | **1.11e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9363** | 0.2525 | ±0.5049 | **-3.709** | **2.08e-04** | *** |
| Age (years) | +0.0152 | 0.0098 | ±0.0195 | +1.560 | 0.1189 |  |
| BMI (kg/m2) | +0.0195 | 0.0136 | ±0.0272 | +1.435 | 0.1512 |  |
| Hypertension | +0.1275 | 0.1965 | ±0.3931 | +0.649 | 0.5165 |  |
| High cholesterol | -0.0385 | 0.1957 | ±0.3915 | -0.197 | 0.8441 |  |
| Kidney disease | -0.0768 | 0.2243 | ±0.4487 | -0.342 | 0.7322 |  |
| Circulatory disease | +0.2080 | 0.2364 | ±0.4727 | +0.880 | 0.3789 |  |
| Avg. daily time < 70 (%) | +0.0252 | 0.0875 | ±0.1749 | +0.288 | 0.7735 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.2737**, Adj R² = **0.2544**, F-statistic = **14.19** (p = **5.64e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2389.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3900** | 0.9239 | ±1.8477 | **+25.318** | **2.05e-141** | *** |
| Education: graduate level (vs college) | -0.1213 | 0.2033 | ±0.4066 | -0.597 | 0.5506 |  |
| Education: high school or below (vs college) | +0.1461 | 0.2593 | ±0.5187 | +0.563 | 0.5732 |  |
| Site: UCSD (vs UAB) | +0.0769 | 0.2221 | ±0.4442 | +0.346 | 0.7291 |  |
| **Site: UW (vs UAB)** | **-1.2093** | 0.2225 | ±0.4450 | **-5.434** | **5.50e-08** | *** |
| Season: spring (vs autumn) | -0.1583 | 0.2395 | ±0.4790 | -0.661 | 0.5086 |  |
| **Season: summer (vs autumn)** | **+1.9136** | 0.2725 | ±0.5450 | **+7.022** | **2.19e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9427** | 0.2538 | ±0.5076 | **-3.715** | **2.04e-04** | *** |
| Age (years) | +0.0154 | 0.0098 | ±0.0196 | +1.571 | 0.1161 |  |
| BMI (kg/m2) | +0.0195 | 0.0137 | ±0.0273 | +1.424 | 0.1543 |  |
| Hypertension | +0.1337 | 0.1926 | ±0.3851 | +0.694 | 0.4875 |  |
| High cholesterol | -0.0450 | 0.1956 | ±0.3912 | -0.230 | 0.8182 |  |
| Kidney disease | -0.0738 | 0.2238 | ±0.4476 | -0.330 | 0.7416 |  |
| Circulatory disease | +0.2035 | 0.2368 | ±0.4735 | +0.859 | 0.3901 |  |
| Time 54-250, pooled (%) | -0.0001 | 0.0055 | ±0.0111 | -0.022 | 0.9825 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.2737**, Adj R² = **0.2544**, F-statistic = **14.19** (p = **5.64e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2389.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3663** | 0.9347 | ±1.8694 | **+24.999** | **6.26e-138** | *** |
| Education: graduate level (vs college) | -0.1223 | 0.2034 | ±0.4067 | -0.601 | 0.5476 |  |
| Education: high school or below (vs college) | +0.1473 | 0.2592 | ±0.5184 | +0.568 | 0.5699 |  |
| Site: UCSD (vs UAB) | +0.0759 | 0.2221 | ±0.4443 | +0.341 | 0.7328 |  |
| **Site: UW (vs UAB)** | **-1.2106** | 0.2225 | ±0.4450 | **-5.441** | **5.31e-08** | *** |
| Season: spring (vs autumn) | -0.1583 | 0.2394 | ±0.4789 | -0.661 | 0.5085 |  |
| **Season: summer (vs autumn)** | **+1.9123** | 0.2725 | ±0.5451 | **+7.016** | **2.28e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9425** | 0.2538 | ±0.5076 | **-3.714** | **2.04e-04** | *** |
| Age (years) | +0.0153 | 0.0098 | ±0.0195 | +1.568 | 0.1169 |  |
| BMI (kg/m2) | +0.0195 | 0.0137 | ±0.0273 | +1.427 | 0.1536 |  |
| Hypertension | +0.1342 | 0.1926 | ±0.3852 | +0.697 | 0.4861 |  |
| High cholesterol | -0.0453 | 0.1956 | ±0.3912 | -0.232 | 0.8167 |  |
| Kidney disease | -0.0731 | 0.2238 | ±0.4476 | -0.327 | 0.7440 |  |
| Circulatory disease | +0.2040 | 0.2369 | ±0.4737 | +0.861 | 0.3891 |  |
| Avg. daily time 54-250 (%) | +0.0002 | 0.0056 | ±0.0112 | +0.030 | 0.9757 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.2751**, Adj R² = **0.2559**, F-statistic = **14.29** (p = **3.48e-29**), Residual SE = **2.036** on **527** df, AIC = **2323.5**, BIC = **2387.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4691** | 0.7961 | ±1.5922 | **+29.480** | **5.21e-191** | *** |
| Education: graduate level (vs college) | -0.1154 | 0.2023 | ±0.4046 | -0.571 | 0.5683 |  |
| Education: high school or below (vs college) | +0.1633 | 0.2591 | ±0.5182 | +0.630 | 0.5284 |  |
| Site: UCSD (vs UAB) | +0.0609 | 0.2186 | ±0.4371 | +0.279 | 0.7804 |  |
| **Site: UW (vs UAB)** | **-1.2093** | 0.2202 | ±0.4404 | **-5.491** | **3.99e-08** | *** |
| Season: spring (vs autumn) | -0.1425 | 0.2403 | ±0.4807 | -0.593 | 0.5532 |  |
| **Season: summer (vs autumn)** | **+1.9232** | 0.2698 | ±0.5397 | **+7.127** | **1.02e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9205** | 0.2565 | ±0.5131 | **-3.588** | **3.33e-04** | *** |
| Age (years) | +0.0157 | 0.0098 | ±0.0196 | +1.600 | 0.1096 |  |
| BMI (kg/m2) | +0.0208 | 0.0136 | ±0.0271 | +1.537 | 0.1243 |  |
| Hypertension | +0.1175 | 0.1951 | ±0.3903 | +0.602 | 0.5472 |  |
| High cholesterol | -0.0540 | 0.1960 | ±0.3921 | -0.275 | 0.7830 |  |
| Kidney disease | -0.0676 | 0.2226 | ±0.4452 | -0.304 | 0.7613 |  |
| Circulatory disease | +0.2136 | 0.2363 | ±0.4726 | +0.904 | 0.3661 |  |
| Time 181-250, pooled (%) | -0.0062 | 0.0060 | ±0.0120 | -1.032 | 0.3022 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **542**, R² = **0.2755**, Adj R² = **0.2563**, F-statistic = **14.31** (p = **3.09e-29**), Residual SE = **2.035** on **527** df, AIC = **2323.2**, BIC = **2387.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4813** | 0.7976 | ±1.5952 | **+29.440** | **1.70e-190** | *** |
| Education: graduate level (vs college) | -0.1134 | 0.2022 | ±0.4045 | -0.561 | 0.5751 |  |
| Education: high school or below (vs college) | +0.1680 | 0.2595 | ±0.5190 | +0.647 | 0.5173 |  |
| Site: UCSD (vs UAB) | +0.0573 | 0.2187 | ±0.4373 | +0.262 | 0.7931 |  |
| **Site: UW (vs UAB)** | **-1.2112** | 0.2204 | ±0.4407 | **-5.497** | **3.87e-08** | *** |
| Season: spring (vs autumn) | -0.1407 | 0.2403 | ±0.4806 | -0.585 | 0.5583 |  |
| **Season: summer (vs autumn)** | **+1.9247** | 0.2699 | ±0.5398 | **+7.131** | **9.99e-13** | *** |
| **Season: winter (vs autumn)** | **-0.9165** | 0.2570 | ±0.5140 | **-3.566** | **3.62e-04** | *** |
| Age (years) | +0.0156 | 0.0098 | ±0.0195 | +1.596 | 0.1105 |  |
| BMI (kg/m2) | +0.0210 | 0.0136 | ±0.0271 | +1.551 | 0.1210 |  |
| Hypertension | +0.1160 | 0.1951 | ±0.3903 | +0.595 | 0.5521 |  |
| High cholesterol | -0.0543 | 0.1960 | ±0.3920 | -0.277 | 0.7816 |  |
| Kidney disease | -0.0661 | 0.2224 | ±0.4448 | -0.297 | 0.7663 |  |
| Circulatory disease | +0.2139 | 0.2364 | ±0.4728 | +0.905 | 0.3657 |  |
| Avg. daily time 181-250 (%) | -0.0068 | 0.0059 | ±0.0119 | -1.142 | 0.2536 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **542**, R² = **0.2742**, Adj R² = **0.2549**, F-statistic = **14.22** (p = **4.88e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.2**, BIC = **2388.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4463** | 0.8007 | ±1.6013 | **+29.284** | **1.66e-188** | *** |
| Education: graduate level (vs college) | -0.1261 | 0.2026 | ±0.4051 | -0.623 | 0.5335 |  |
| Education: high school or below (vs college) | +0.1599 | 0.2604 | ±0.5208 | +0.614 | 0.5391 |  |
| Site: UCSD (vs UAB) | +0.0648 | 0.2213 | ±0.4425 | +0.293 | 0.7695 |  |
| **Site: UW (vs UAB)** | **-1.2187** | 0.2219 | ±0.4438 | **-5.492** | **3.97e-08** | *** |
| Season: spring (vs autumn) | -0.1536 | 0.2394 | ±0.4788 | -0.641 | 0.5212 |  |
| **Season: summer (vs autumn)** | **+1.9075** | 0.2722 | ±0.5445 | **+7.007** | **2.43e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9344** | 0.2546 | ±0.5092 | **-3.670** | **2.43e-04** | *** |
| Age (years) | +0.0151 | 0.0097 | ±0.0195 | +1.551 | 0.1208 |  |
| BMI (kg/m2) | +0.0202 | 0.0137 | ±0.0273 | +1.478 | 0.1395 |  |
| Hypertension | +0.1319 | 0.1941 | ±0.3882 | +0.680 | 0.4968 |  |
| High cholesterol | -0.0504 | 0.1958 | ±0.3917 | -0.257 | 0.7968 |  |
| Kidney disease | -0.0673 | 0.2226 | ±0.4451 | -0.302 | 0.7623 |  |
| Circulatory disease | +0.2100 | 0.2371 | ±0.4742 | +0.886 | 0.3757 |  |
| Time > 180 (%) | -0.0019 | 0.0037 | ±0.0075 | -0.519 | 0.6040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **542**, R² = **0.2743**, Adj R² = **0.2551**, F-statistic = **14.23** (p = **4.57e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.1**, BIC = **2388.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4561** | 0.8003 | ±1.6006 | **+29.309** | **7.95e-189** | *** |
| Education: graduate level (vs college) | -0.1264 | 0.2025 | ±0.4050 | -0.624 | 0.5326 |  |
| Education: high school or below (vs college) | +0.1635 | 0.2605 | ±0.5211 | +0.627 | 0.5304 |  |
| Site: UCSD (vs UAB) | +0.0618 | 0.2214 | ±0.4427 | +0.279 | 0.7802 |  |
| **Site: UW (vs UAB)** | **-1.2206** | 0.2220 | ±0.4439 | **-5.499** | **3.82e-08** | *** |
| Season: spring (vs autumn) | -0.1519 | 0.2394 | ±0.4787 | -0.635 | 0.5256 |  |
| **Season: summer (vs autumn)** | **+1.9075** | 0.2720 | ±0.5441 | **+7.012** | **2.35e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9316** | 0.2549 | ±0.5098 | **-3.655** | **2.57e-04** | *** |
| Age (years) | +0.0151 | 0.0097 | ±0.0195 | +1.548 | 0.1215 |  |
| BMI (kg/m2) | +0.0203 | 0.0137 | ±0.0273 | +1.489 | 0.1364 |  |
| Hypertension | +0.1313 | 0.1942 | ±0.3884 | +0.676 | 0.4991 |  |
| High cholesterol | -0.0512 | 0.1958 | ±0.3917 | -0.262 | 0.7937 |  |
| Kidney disease | -0.0652 | 0.2223 | ±0.4446 | -0.293 | 0.7694 |  |
| Circulatory disease | +0.2114 | 0.2371 | ±0.4743 | +0.891 | 0.3727 |  |
| Avg. daily time > 180 (%) | -0.0023 | 0.0037 | ±0.0074 | -0.620 | 0.5350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **542**, R² = **0.2741**, Adj R² = **0.2548**, F-statistic = **14.21** (p = **4.98e-29**), Residual SE = **2.037** on **527** df, AIC = **2324.3**, BIC = **2388.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4259** | 0.7982 | ±1.5963 | **+29.350** | **2.40e-189** | *** |
| Education: graduate level (vs college) | -0.1293 | 0.2035 | ±0.4070 | -0.635 | 0.5253 |  |
| Education: high school or below (vs college) | +0.1567 | 0.2598 | ±0.5195 | +0.603 | 0.5463 |  |
| Site: UCSD (vs UAB) | +0.0644 | 0.2219 | ±0.4439 | +0.290 | 0.7717 |  |
| **Site: UW (vs UAB)** | **-1.2151** | 0.2215 | ±0.4430 | **-5.486** | **4.11e-08** | *** |
| Season: spring (vs autumn) | -0.1536 | 0.2396 | ±0.4792 | -0.641 | 0.5215 |  |
| **Season: summer (vs autumn)** | **+1.9074** | 0.2719 | ±0.5438 | **+7.015** | **2.30e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9352** | 0.2544 | ±0.5089 | **-3.676** | **2.37e-04** | *** |
| Age (years) | +0.0150 | 0.0098 | ±0.0195 | +1.530 | 0.1260 |  |
| BMI (kg/m2) | +0.0204 | 0.0139 | ±0.0278 | +1.471 | 0.1414 |  |
| Hypertension | +0.1319 | 0.1941 | ±0.3882 | +0.680 | 0.4968 |  |
| High cholesterol | -0.0511 | 0.1957 | ±0.3914 | -0.261 | 0.7941 |  |
| Kidney disease | -0.0690 | 0.2226 | ±0.4451 | -0.310 | 0.7565 |  |
| Circulatory disease | +0.2099 | 0.2375 | ±0.4750 | +0.884 | 0.3769 |  |
| Nocturnal time > 180 (%) | -0.0016 | 0.0034 | ±0.0068 | -0.460 | 0.6453 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.2737**, Adj R² = **0.2544**, F-statistic = **14.19** (p = **5.64e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2389.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3772** | 0.8019 | ±1.6038 | **+29.152** | **7.95e-187** | *** |
| Education: graduate level (vs college) | -0.1212 | 0.2033 | ±0.4066 | -0.596 | 0.5509 |  |
| Education: high school or below (vs college) | +0.1459 | 0.2593 | ±0.5187 | +0.563 | 0.5736 |  |
| Site: UCSD (vs UAB) | +0.0770 | 0.2220 | ±0.4441 | +0.347 | 0.7287 |  |
| **Site: UW (vs UAB)** | **-1.2091** | 0.2224 | ±0.4449 | **-5.436** | **5.46e-08** | *** |
| Season: spring (vs autumn) | -0.1583 | 0.2395 | ±0.4790 | -0.661 | 0.5086 |  |
| **Season: summer (vs autumn)** | **+1.9137** | 0.2725 | ±0.5450 | **+7.023** | **2.18e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9428** | 0.2538 | ±0.5076 | **-3.715** | **2.03e-04** | *** |
| Age (years) | +0.0154 | 0.0098 | ±0.0196 | +1.572 | 0.1160 |  |
| BMI (kg/m2) | +0.0195 | 0.0137 | ±0.0273 | +1.424 | 0.1544 |  |
| Hypertension | +0.1336 | 0.1926 | ±0.3852 | +0.694 | 0.4877 |  |
| High cholesterol | -0.0449 | 0.1956 | ±0.3912 | -0.230 | 0.8184 |  |
| Kidney disease | -0.0739 | 0.2238 | ±0.4476 | -0.330 | 0.7414 |  |
| Circulatory disease | +0.2034 | 0.2368 | ±0.4736 | +0.859 | 0.3903 |  |
| Time > 250 (%) | +0.0002 | 0.0055 | ±0.0111 | +0.028 | 0.9776 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 542)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **542**, R² = **0.2737**, Adj R² = **0.2544**, F-statistic = **14.19** (p = **5.64e-29**), Residual SE = **2.038** on **527** df, AIC = **2324.5**, BIC = **2389.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3822** | 0.8005 | ±1.6011 | **+29.208** | **1.55e-187** | *** |
| Education: graduate level (vs college) | -0.1221 | 0.2034 | ±0.4067 | -0.600 | 0.5483 |  |
| Education: high school or below (vs college) | +0.1470 | 0.2592 | ±0.5185 | +0.567 | 0.5706 |  |
| Site: UCSD (vs UAB) | +0.0761 | 0.2221 | ±0.4441 | +0.343 | 0.7318 |  |
| **Site: UW (vs UAB)** | **-1.2103** | 0.2224 | ±0.4449 | **-5.441** | **5.29e-08** | *** |
| Season: spring (vs autumn) | -0.1583 | 0.2395 | ±0.4789 | -0.661 | 0.5085 |  |
| **Season: summer (vs autumn)** | **+1.9126** | 0.2725 | ±0.5450 | **+7.019** | **2.24e-12** | *** |
| **Season: winter (vs autumn)** | **-0.9426** | 0.2538 | ±0.5075 | **-3.714** | **2.04e-04** | *** |
| Age (years) | +0.0153 | 0.0098 | ±0.0195 | +1.569 | 0.1166 |  |
| BMI (kg/m2) | +0.0195 | 0.0137 | ±0.0273 | +1.426 | 0.1538 |  |
| Hypertension | +0.1340 | 0.1926 | ±0.3852 | +0.696 | 0.4865 |  |
| High cholesterol | -0.0452 | 0.1956 | ±0.3912 | -0.231 | 0.8171 |  |
| Kidney disease | -0.0732 | 0.2238 | ±0.4476 | -0.327 | 0.7434 |  |
| Circulatory disease | +0.2039 | 0.2369 | ±0.4738 | +0.861 | 0.3895 |  |
| Avg. daily time > 250 (%) | -0.0001 | 0.0056 | ±0.0112 | -0.019 | 0.9852 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 542; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **542**, R² = **0.2500**, Adj R² = **0.2315**, F-statistic = **13.53** (p = **4.25e-26**), Residual SE = **6.040** on **528** df, AIC = **3501.4**, BIC = **3561.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.1538** | 2.3990 | ±4.7980 | **+21.323** | **6.97e-101** | *** |
| Education: graduate level (vs college) | +0.1829 | 0.6303 | ±1.2605 | +0.290 | 0.7717 |  |
| Education: high school or below (vs college) | +0.4016 | 0.7317 | ±1.4634 | +0.549 | 0.5831 |  |
| **Site: UCSD (vs UAB)** | **+3.4065** | 0.6552 | ±1.3104 | **+5.199** | **2.00e-07** | *** |
| Site: UW (vs UAB) | -0.4409 | 0.6334 | ±1.2667 | -0.696 | 0.4863 |  |
| **Season: spring (vs autumn)** | **-2.3146** | 0.7562 | ±1.5123 | **-3.061** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5325** | 0.7352 | ±1.4705 | **+2.084** | **0.0371** | * |
| **Season: winter (vs autumn)** | **-5.7683** | 0.8499 | ±1.6997 | **-6.787** | **1.14e-11** | *** |
| Age (years) | -0.0526 | 0.0275 | ±0.0550 | -1.911 | 0.0560 | . |
| BMI (kg/m2) | -0.0602 | 0.0406 | ±0.0812 | -1.483 | 0.1380 |  |
| Hypertension | -1.0000 | 0.6180 | ±1.2361 | -1.618 | 0.1057 |  |
| High cholesterol | -0.2631 | 0.5833 | ±1.1666 | -0.451 | 0.6520 |  |
| **Kidney disease** | **+1.5243** | 0.6625 | ±1.3251 | **+2.301** | **0.0214** | * |
| Circulatory disease | -0.2638 | 0.6638 | ±1.3277 | -0.397 | 0.6911 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **542**, R² = **0.2504**, Adj R² = **0.2305**, F-statistic = **12.58** (p = **1.37e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.1**, BIC = **3567.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3221** | 2.7314 | ±5.4627 | **+18.424** | **8.48e-76** | *** |
| Education: graduate level (vs college) | +0.2045 | 0.6299 | ±1.2599 | +0.325 | 0.7455 |  |
| Education: high school or below (vs college) | +0.3549 | 0.7330 | ±1.4660 | +0.484 | 0.6282 |  |
| **Site: UCSD (vs UAB)** | **+3.4330** | 0.6601 | ±1.3201 | **+5.201** | **1.98e-07** | *** |
| Site: UW (vs UAB) | -0.4098 | 0.6359 | ±1.2718 | -0.644 | 0.5193 |  |
| **Season: spring (vs autumn)** | **-2.2925** | 0.7598 | ±1.5197 | **-3.017** | **0.0026** | ** |
| **Season: summer (vs autumn)** | **+1.5622** | 0.7382 | ±1.4763 | **+2.116** | **0.0343** | * |
| **Season: winter (vs autumn)** | **-5.7706** | 0.8522 | ±1.7044 | **-6.771** | **1.28e-11** | *** |
| Age (years) | -0.0516 | 0.0275 | ±0.0550 | -1.875 | 0.0607 | . |
| BMI (kg/m2) | -0.0627 | 0.0409 | ±0.0818 | -1.533 | 0.1253 |  |
| Hypertension | -1.0063 | 0.6183 | ±1.2366 | -1.628 | 0.1036 |  |
| High cholesterol | -0.2598 | 0.5839 | ±1.1679 | -0.445 | 0.6564 |  |
| **Kidney disease** | **+1.5311** | 0.6623 | ±1.3245 | **+2.312** | **0.0208** | * |
| Circulatory disease | -0.2768 | 0.6648 | ±1.3296 | -0.416 | 0.6771 |  |
| HbA1c (%) | +0.1149 | 0.2000 | ±0.3999 | +0.574 | 0.5657 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **542**, R² = **0.2518**, Adj R² = **0.2319**, F-statistic = **12.67** (p = **8.86e-26**), Residual SE = **6.039** on **527** df, AIC = **3502.1**, BIC = **3566.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8365** | 2.5483 | ±5.0965 | **+19.557** | **3.60e-85** | *** |
| Education: graduate level (vs college) | +0.2187 | 0.6303 | ±1.2607 | +0.347 | 0.7287 |  |
| Education: high school or below (vs college) | +0.3264 | 0.7312 | ±1.4624 | +0.446 | 0.6553 |  |
| **Site: UCSD (vs UAB)** | **+3.4678** | 0.6615 | ±1.3230 | **+5.242** | **1.59e-07** | *** |
| Site: UW (vs UAB) | -0.3868 | 0.6375 | ±1.2750 | -0.607 | 0.5440 |  |
| **Season: spring (vs autumn)** | **-2.3384** | 0.7566 | ±1.5131 | **-3.091** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.5793** | 0.7372 | ±1.4745 | **+2.142** | **0.0322** | * |
| **Season: winter (vs autumn)** | **-5.8117** | 0.8532 | ±1.7063 | **-6.812** | **9.63e-12** | *** |
| Age (years) | -0.0505 | 0.0274 | ±0.0548 | -1.845 | 0.0651 | . |
| BMI (kg/m2) | -0.0635 | 0.0408 | ±0.0815 | -1.557 | 0.1194 |  |
| Hypertension | -0.9993 | 0.6186 | ±1.2372 | -1.615 | 0.1062 |  |
| High cholesterol | -0.2444 | 0.5842 | ±1.1684 | -0.418 | 0.6757 |  |
| **Kidney disease** | **+1.4999** | 0.6605 | ±1.3211 | **+2.271** | **0.0232** | * |
| Circulatory disease | -0.3016 | 0.6637 | ±1.3275 | -0.454 | 0.6496 |  |
| Mean glucose (mg/dL) | +0.0074 | 0.0068 | ±0.0136 | +1.084 | 0.2784 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **542**, R² = **0.2518**, Adj R² = **0.2319**, F-statistic = **12.67** (p = **8.86e-26**), Residual SE = **6.039** on **527** df, AIC = **3502.1**, BIC = **3566.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.8167** | 3.0169 | ±6.0339 | **+16.181** | **6.89e-59** | *** |
| Education: graduate level (vs college) | +0.2187 | 0.6303 | ±1.2607 | +0.347 | 0.7287 |  |
| Education: high school or below (vs college) | +0.3264 | 0.7312 | ±1.4624 | +0.446 | 0.6553 |  |
| **Site: UCSD (vs UAB)** | **+3.4678** | 0.6615 | ±1.3230 | **+5.242** | **1.59e-07** | *** |
| Site: UW (vs UAB) | -0.3868 | 0.6375 | ±1.2750 | -0.607 | 0.5440 |  |
| **Season: spring (vs autumn)** | **-2.3384** | 0.7566 | ±1.5131 | **-3.091** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.5793** | 0.7372 | ±1.4745 | **+2.142** | **0.0322** | * |
| **Season: winter (vs autumn)** | **-5.8117** | 0.8532 | ±1.7063 | **-6.812** | **9.63e-12** | *** |
| Age (years) | -0.0505 | 0.0274 | ±0.0548 | -1.845 | 0.0651 | . |
| BMI (kg/m2) | -0.0635 | 0.0408 | ±0.0815 | -1.557 | 0.1194 |  |
| Hypertension | -0.9993 | 0.6186 | ±1.2372 | -1.615 | 0.1062 |  |
| High cholesterol | -0.2444 | 0.5842 | ±1.1684 | -0.418 | 0.6757 |  |
| **Kidney disease** | **+1.4999** | 0.6605 | ±1.3211 | **+2.271** | **0.0232** | * |
| Circulatory disease | -0.3016 | 0.6637 | ±1.3275 | -0.454 | 0.6496 |  |
| GMI (%) | +0.3081 | 0.2842 | ±0.5684 | +1.084 | 0.2784 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **542**, R² = **0.2507**, Adj R² = **0.2308**, F-statistic = **12.59** (p = **1.26e-25**), Residual SE = **6.043** on **527** df, AIC = **3502.9**, BIC = **3567.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3977** | 2.5126 | ±5.0252 | **+20.058** | **1.72e-89** | *** |
| Education: graduate level (vs college) | +0.2125 | 0.6318 | ±1.2637 | +0.336 | 0.7366 |  |
| Education: high school or below (vs college) | +0.3611 | 0.7323 | ±1.4646 | +0.493 | 0.6220 |  |
| **Site: UCSD (vs UAB)** | **+3.4486** | 0.6627 | ±1.3254 | **+5.204** | **1.95e-07** | *** |
| Site: UW (vs UAB) | -0.4230 | 0.6357 | ±1.2714 | -0.665 | 0.5058 |  |
| **Season: spring (vs autumn)** | **-2.3380** | 0.7569 | ±1.5137 | **-3.089** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.5576** | 0.7373 | ±1.4746 | **+2.113** | **0.0346** | * |
| **Season: winter (vs autumn)** | **-5.7978** | 0.8538 | ±1.7076 | **-6.791** | **1.12e-11** | *** |
| Age (years) | -0.0506 | 0.0274 | ±0.0548 | -1.847 | 0.0647 | . |
| BMI (kg/m2) | -0.0635 | 0.0411 | ±0.0822 | -1.545 | 0.1222 |  |
| Hypertension | -0.9954 | 0.6185 | ±1.2371 | -1.609 | 0.1076 |  |
| High cholesterol | -0.2507 | 0.5843 | ±1.1686 | -0.429 | 0.6678 |  |
| **Kidney disease** | **+1.5211** | 0.6624 | ±1.3248 | **+2.296** | **0.0217** | * |
| Circulatory disease | -0.2879 | 0.6644 | ±1.3288 | -0.433 | 0.6647 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0044 | 0.0062 | ±0.0123 | +0.711 | 0.4770 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2504**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.41e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.6633** | 2.6154 | ±5.2309 | **+19.371** | **1.36e-83** | *** |
| Education: graduate level (vs college) | +0.2029 | 0.6347 | ±1.2693 | +0.320 | 0.7492 |  |
| Education: high school or below (vs college) | +0.3662 | 0.7282 | ±1.4564 | +0.503 | 0.6150 |  |
| **Site: UCSD (vs UAB)** | **+3.4284** | 0.6623 | ±1.3245 | **+5.177** | **2.26e-07** | *** |
| Site: UW (vs UAB) | -0.3989 | 0.6422 | ±1.2845 | -0.621 | 0.5346 |  |
| **Season: spring (vs autumn)** | **-2.3270** | 0.7559 | ±1.5117 | **-3.079** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.5584** | 0.7426 | ±1.4852 | **+2.099** | **0.0358** | * |
| **Season: winter (vs autumn)** | **-5.7869** | 0.8490 | ±1.6981 | **-6.816** | **9.38e-12** | *** |
| Age (years) | -0.0521 | 0.0276 | ±0.0552 | -1.889 | 0.0588 | . |
| BMI (kg/m2) | -0.0612 | 0.0407 | ±0.0814 | -1.503 | 0.1329 |  |
| Hypertension | -1.0089 | 0.6183 | ±1.2366 | -1.632 | 0.1027 |  |
| High cholesterol | -0.2497 | 0.5847 | ±1.1695 | -0.427 | 0.6694 |  |
| **Kidney disease** | **+1.4638** | 0.6665 | ±1.3330 | **+2.196** | **0.0281** | * |
| Circulatory disease | -0.2784 | 0.6668 | ±1.3336 | -0.418 | 0.6763 |  |
| Glucose SD, pooled (mg/dL) | +0.0116 | 0.0216 | ±0.0432 | +0.538 | 0.5908 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2504**, Adj R² = **0.2305**, F-statistic = **12.57** (p = **1.39e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.1**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.6125** | 2.6118 | ±5.2235 | **+19.379** | **1.17e-83** | *** |
| Education: graduate level (vs college) | +0.1997 | 0.6346 | ±1.2693 | +0.315 | 0.7530 |  |
| Education: high school or below (vs college) | +0.3573 | 0.7294 | ±1.4588 | +0.490 | 0.6243 |  |
| **Site: UCSD (vs UAB)** | **+3.4295** | 0.6632 | ±1.3263 | **+5.171** | **2.32e-07** | *** |
| Site: UW (vs UAB) | -0.4017 | 0.6418 | ±1.2837 | -0.626 | 0.5314 |  |
| **Season: spring (vs autumn)** | **-2.3298** | 0.7557 | ±1.5113 | **-3.083** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.5622** | 0.7436 | ±1.4873 | **+2.101** | **0.0357** | * |
| **Season: winter (vs autumn)** | **-5.7816** | 0.8489 | ±1.6977 | **-6.811** | **9.69e-12** | *** |
| Age (years) | -0.0523 | 0.0276 | ±0.0552 | -1.896 | 0.0580 | . |
| BMI (kg/m2) | -0.0602 | 0.0407 | ±0.0814 | -1.479 | 0.1391 |  |
| Hypertension | -1.0047 | 0.6186 | ±1.2371 | -1.624 | 0.1043 |  |
| High cholesterol | -0.2511 | 0.5843 | ±1.1687 | -0.430 | 0.6674 |  |
| **Kidney disease** | **+1.4556** | 0.6674 | ±1.3349 | **+2.181** | **0.0292** | * |
| Circulatory disease | -0.2741 | 0.6667 | ±1.3333 | -0.411 | 0.6809 |  |
| Avg. daily SD (mg/dL) | +0.0139 | 0.0249 | ±0.0498 | +0.560 | 0.5758 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **542**, R² = **0.2503**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.44e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.7043** | 2.7987 | ±5.5975 | **+18.474** | **3.34e-76** | *** |
| Education: graduate level (vs college) | +0.1740 | 0.6337 | ±1.2673 | +0.275 | 0.7836 |  |
| Education: high school or below (vs college) | +0.4153 | 0.7293 | ±1.4585 | +0.569 | 0.5691 |  |
| **Site: UCSD (vs UAB)** | **+3.4010** | 0.6572 | ±1.3144 | **+5.175** | **2.28e-07** | *** |
| Site: UW (vs UAB) | -0.4695 | 0.6380 | ±1.2760 | -0.736 | 0.4618 |  |
| **Season: spring (vs autumn)** | **-2.3153** | 0.7572 | ±1.5145 | **-3.058** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5209** | 0.7377 | ±1.4755 | **+2.062** | **0.0392** | * |
| **Season: winter (vs autumn)** | **-5.7660** | 0.8519 | ±1.7039 | **-6.768** | **1.30e-11** | *** |
| Age (years) | -0.0523 | 0.0275 | ±0.0550 | -1.900 | 0.0574 | . |
| BMI (kg/m2) | -0.0605 | 0.0406 | ±0.0813 | -1.489 | 0.1365 |  |
| Hypertension | -0.9857 | 0.6171 | ±1.2342 | -1.597 | 0.1102 |  |
| High cholesterol | -0.2700 | 0.5842 | ±1.1684 | -0.462 | 0.6439 |  |
| **Kidney disease** | **+1.5856** | 0.6675 | ±1.3350 | **+2.375** | **0.0175** | * |
| Circulatory disease | -0.2629 | 0.6644 | ±1.3287 | -0.396 | 0.6923 |  |
| CV (%) | -0.0230 | 0.0486 | ±0.0971 | -0.474 | 0.6352 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **542**, R² = **0.2502**, Adj R² = **0.2303**, F-statistic = **12.56** (p = **1.47e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.6595** | 2.5242 | ±5.0483 | **+20.070** | **1.36e-89** | *** |
| Education: graduate level (vs college) | +0.1749 | 0.6345 | ±1.2691 | +0.276 | 0.7828 |  |
| Education: high school or below (vs college) | +0.4106 | 0.7295 | ±1.4590 | +0.563 | 0.5735 |  |
| **Site: UCSD (vs UAB)** | **+3.4086** | 0.6558 | ±1.3116 | **+5.198** | **2.02e-07** | *** |
| Site: UW (vs UAB) | -0.4588 | 0.6366 | ±1.2732 | -0.721 | 0.4710 |  |
| **Season: spring (vs autumn)** | **-2.3101** | 0.7565 | ±1.5129 | **-3.054** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5358** | 0.7347 | ±1.4695 | **+2.090** | **0.0366** | * |
| **Season: winter (vs autumn)** | **-5.7621** | 0.8509 | ±1.7018 | **-6.772** | **1.27e-11** | *** |
| Age (years) | -0.0524 | 0.0275 | ±0.0551 | -1.904 | 0.0569 | . |
| BMI (kg/m2) | -0.0607 | 0.0407 | ±0.0814 | -1.492 | 0.1358 |  |
| Hypertension | -0.9921 | 0.6174 | ±1.2348 | -1.607 | 0.1081 |  |
| High cholesterol | -0.2612 | 0.5845 | ±1.1690 | -0.447 | 0.6549 |  |
| **Kidney disease** | **+1.5675** | 0.6630 | ±1.3260 | **+2.364** | **0.0181** | * |
| Circulatory disease | -0.2574 | 0.6654 | ±1.3309 | -0.387 | 0.6990 |  |
| Mean / SD ratio | +0.1139 | 0.2693 | ±0.5386 | +0.423 | 0.6723 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **542**, R² = **0.2502**, Adj R² = **0.2302**, F-statistic = **12.56** (p = **1.50e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.7566** | 2.5434 | ±5.0868 | **+19.956** | **1.33e-88** | *** |
| Education: graduate level (vs college) | +0.1761 | 0.6351 | ±1.2703 | +0.277 | 0.7816 |  |
| Education: high school or below (vs college) | +0.4116 | 0.7304 | ±1.4608 | +0.564 | 0.5731 |  |
| **Site: UCSD (vs UAB)** | **+3.4089** | 0.6559 | ±1.3117 | **+5.198** | **2.02e-07** | *** |
| Site: UW (vs UAB) | -0.4513 | 0.6361 | ±1.2722 | -0.710 | 0.4780 |  |
| **Season: spring (vs autumn)** | **-2.3156** | 0.7581 | ±1.5162 | **-3.054** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5304** | 0.7372 | ±1.4743 | **+2.076** | **0.0379** | * |
| **Season: winter (vs autumn)** | **-5.7695** | 0.8529 | ±1.7058 | **-6.765** | **1.34e-11** | *** |
| Age (years) | -0.0523 | 0.0276 | ±0.0552 | -1.894 | 0.0582 | . |
| BMI (kg/m2) | -0.0614 | 0.0410 | ±0.0819 | -1.500 | 0.1337 |  |
| Hypertension | -0.9958 | 0.6181 | ±1.2362 | -1.611 | 0.1072 |  |
| High cholesterol | -0.2632 | 0.5845 | ±1.1689 | -0.450 | 0.6525 |  |
| **Kidney disease** | **+1.5592** | 0.6619 | ±1.3238 | **+2.356** | **0.0185** | * |
| Circulatory disease | -0.2632 | 0.6644 | ±1.3289 | -0.396 | 0.6920 |  |
| Avg. daily mean/SD | +0.0814 | 0.2304 | ±0.4609 | +0.353 | 0.7239 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **542**, R² = **0.2500**, Adj R² = **0.2301**, F-statistic = **12.55** (p = **1.56e-25**), Residual SE = **6.046** on **527** df, AIC = **3503.4**, BIC = **3567.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.7809** | 2.7914 | ±5.5828 | **+18.192** | **5.97e-74** | *** |
| Education: graduate level (vs college) | +0.1934 | 0.6364 | ±1.2728 | +0.304 | 0.7612 |  |
| Education: high school or below (vs college) | +0.3921 | 0.7326 | ±1.4653 | +0.535 | 0.5926 |  |
| **Site: UCSD (vs UAB)** | **+3.4135** | 0.6595 | ±1.3190 | **+5.176** | **2.27e-07** | *** |
| Site: UW (vs UAB) | -0.4171 | 0.6449 | ±1.2897 | -0.647 | 0.5178 |  |
| **Season: spring (vs autumn)** | **-2.3161** | 0.7575 | ±1.5151 | **-3.057** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5480** | 0.7416 | ±1.4833 | **+2.087** | **0.0369** | * |
| **Season: winter (vs autumn)** | **-5.7670** | 0.8516 | ±1.7031 | **-6.772** | **1.27e-11** | *** |
| Age (years) | -0.0517 | 0.0275 | ±0.0550 | -1.882 | 0.0599 | . |
| BMI (kg/m2) | -0.0601 | 0.0406 | ±0.0813 | -1.478 | 0.1394 |  |
| Hypertension | -1.0011 | 0.6188 | ±1.2376 | -1.618 | 0.1057 |  |
| High cholesterol | -0.2595 | 0.5838 | ±1.1675 | -0.445 | 0.6567 |  |
| **Kidney disease** | **+1.5076** | 0.6634 | ±1.3267 | **+2.273** | **0.0230** | * |
| Circulatory disease | -0.2662 | 0.6642 | ±1.3284 | -0.401 | 0.6886 |  |
| MAG (mg/dL/h) | +0.0065 | 0.0263 | ±0.0526 | +0.249 | 0.8036 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **542**, R² = **0.2501**, Adj R² = **0.2302**, F-statistic = **12.56** (p = **1.51e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.6806** | 2.7430 | ±5.4859 | **+18.477** | **3.18e-76** | *** |
| Education: graduate level (vs college) | +0.1935 | 0.6350 | ±1.2699 | +0.305 | 0.7605 |  |
| Education: high school or below (vs college) | +0.3729 | 0.7300 | ±1.4601 | +0.511 | 0.6095 |  |
| **Site: UCSD (vs UAB)** | **+3.4224** | 0.6635 | ±1.3270 | **+5.158** | **2.49e-07** | *** |
| Site: UW (vs UAB) | -0.4162 | 0.6424 | ±1.2849 | -0.648 | 0.5171 |  |
| **Season: spring (vs autumn)** | **-2.3279** | 0.7539 | ±1.5078 | **-3.088** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.5422** | 0.7394 | ±1.4788 | **+2.086** | **0.0370** | * |
| **Season: winter (vs autumn)** | **-5.7797** | 0.8487 | ±1.6975 | **-6.810** | **9.77e-12** | *** |
| Age (years) | -0.0519 | 0.0275 | ±0.0551 | -1.886 | 0.0592 | . |
| BMI (kg/m2) | -0.0599 | 0.0407 | ±0.0814 | -1.471 | 0.1413 |  |
| Hypertension | -0.9982 | 0.6196 | ±1.2392 | -1.611 | 0.1072 |  |
| High cholesterol | -0.2608 | 0.5843 | ±1.1686 | -0.446 | 0.6553 |  |
| **Kidney disease** | **+1.4779** | 0.6646 | ±1.3292 | **+2.224** | **0.0262** | * |
| Circulatory disease | -0.2731 | 0.6654 | ±1.3309 | -0.410 | 0.6815 |  |
| Avg. daily range (mg/dL) | +0.0026 | 0.0072 | ±0.0143 | +0.369 | 0.7119 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **542**, R² = **0.2500**, Adj R² = **0.2301**, F-statistic = **12.55** (p = **1.56e-25**), Residual SE = **6.046** on **527** df, AIC = **3503.4**, BIC = **3567.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0341** | 2.4812 | ±4.9624 | **+20.568** | **5.27e-94** | *** |
| Education: graduate level (vs college) | +0.1959 | 0.6333 | ±1.2667 | +0.309 | 0.7571 |  |
| Education: high school or below (vs college) | +0.3984 | 0.7321 | ±1.4643 | +0.544 | 0.5864 |  |
| **Site: UCSD (vs UAB)** | **+3.4136** | 0.6584 | ±1.3168 | **+5.185** | **2.16e-07** | *** |
| Site: UW (vs UAB) | -0.4251 | 0.6376 | ±1.2751 | -0.667 | 0.5049 |  |
| **Season: spring (vs autumn)** | **-2.3133** | 0.7581 | ±1.5162 | **-3.052** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5374** | 0.7380 | ±1.4759 | **+2.083** | **0.0372** | * |
| **Season: winter (vs autumn)** | **-5.7789** | 0.8543 | ±1.7086 | **-6.764** | **1.34e-11** | *** |
| Age (years) | -0.0520 | 0.0276 | ±0.0552 | -1.882 | 0.0598 | . |
| BMI (kg/m2) | -0.0611 | 0.0404 | ±0.0809 | -1.511 | 0.1308 |  |
| Hypertension | -1.0089 | 0.6205 | ±1.2411 | -1.626 | 0.1040 |  |
| High cholesterol | -0.2577 | 0.5847 | ±1.1695 | -0.441 | 0.6595 |  |
| **Kidney disease** | **+1.5133** | 0.6630 | ±1.3260 | **+2.283** | **0.0225** | * |
| Circulatory disease | -0.2788 | 0.6717 | ±1.3434 | -0.415 | 0.6781 |  |
| SD of daily means (mg/dL) | +0.0072 | 0.0307 | ±0.0613 | +0.234 | 0.8149 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **542**, R² = **0.2503**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.43e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.4894** | 2.5734 | ±5.1467 | **+20.009** | **4.63e-89** | *** |
| Education: graduate level (vs college) | +0.1950 | 0.6310 | ±1.2620 | +0.309 | 0.7573 |  |
| Education: high school or below (vs college) | +0.3664 | 0.7326 | ±1.4652 | +0.500 | 0.6170 |  |
| **Site: UCSD (vs UAB)** | **+3.4389** | 0.6637 | ±1.3274 | **+5.181** | **2.20e-07** | *** |
| Site: UW (vs UAB) | -0.4160 | 0.6376 | ±1.2753 | -0.652 | 0.5142 |  |
| **Season: spring (vs autumn)** | **-2.3263** | 0.7561 | ±1.5122 | **-3.077** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.5482** | 0.7387 | ±1.4774 | **+2.096** | **0.0361** | * |
| **Season: winter (vs autumn)** | **-5.7892** | 0.8537 | ±1.7074 | **-6.781** | **1.19e-11** | *** |
| Age (years) | -0.0520 | 0.0275 | ±0.0549 | -1.893 | 0.0584 | . |
| BMI (kg/m2) | -0.0621 | 0.0410 | ±0.0821 | -1.513 | 0.1303 |  |
| Hypertension | -0.9960 | 0.6190 | ±1.2381 | -1.609 | 0.1076 |  |
| High cholesterol | -0.2478 | 0.5847 | ±1.1695 | -0.424 | 0.6718 |  |
| **Kidney disease** | **+1.5071** | 0.6632 | ±1.3264 | **+2.273** | **0.0231** | * |
| Circulatory disease | -0.2800 | 0.6650 | ±1.3300 | -0.421 | 0.6737 |  |
| Time in range 70-180, pooled (%) | -0.0051 | 0.0111 | ±0.0222 | -0.464 | 0.6423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **542**, R² = **0.2503**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.41e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.5156** | 2.5766 | ±5.1531 | **+19.994** | **6.22e-89** | *** |
| Education: graduate level (vs college) | +0.1943 | 0.6311 | ±1.2622 | +0.308 | 0.7582 |  |
| Education: high school or below (vs college) | +0.3623 | 0.7326 | ±1.4651 | +0.495 | 0.6209 |  |
| **Site: UCSD (vs UAB)** | **+3.4427** | 0.6645 | ±1.3291 | **+5.181** | **2.21e-07** | *** |
| Site: UW (vs UAB) | -0.4138 | 0.6378 | ±1.2755 | -0.649 | 0.5164 |  |
| **Season: spring (vs autumn)** | **-2.3282** | 0.7560 | ±1.5120 | **-3.080** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.5469** | 0.7382 | ±1.4764 | **+2.095** | **0.0361** | * |
| **Season: winter (vs autumn)** | **-5.7930** | 0.8542 | ±1.7084 | **-6.782** | **1.19e-11** | *** |
| Age (years) | -0.0520 | 0.0275 | ±0.0549 | -1.893 | 0.0584 | . |
| BMI (kg/m2) | -0.0622 | 0.0410 | ±0.0821 | -1.517 | 0.1293 |  |
| Hypertension | -0.9952 | 0.6191 | ±1.2381 | -1.608 | 0.1079 |  |
| High cholesterol | -0.2473 | 0.5845 | ±1.1690 | -0.423 | 0.6722 |  |
| **Kidney disease** | **+1.5039** | 0.6632 | ±1.3264 | **+2.268** | **0.0233** | * |
| Circulatory disease | -0.2811 | 0.6652 | ±1.3303 | -0.423 | 0.6726 |  |
| Avg. daily time in range 70-180 (%) | -0.0054 | 0.0110 | ±0.0220 | -0.494 | 0.6210 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.2505**, Adj R² = **0.2306**, F-statistic = **12.58** (p = **1.34e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.1**, BIC = **3567.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.9955** | 2.4476 | ±4.8951 | **+20.835** | **2.08e-96** | *** |
| Education: graduate level (vs college) | +0.1835 | 0.6309 | ±1.2617 | +0.291 | 0.7712 |  |
| Education: high school or below (vs college) | +0.4096 | 0.7336 | ±1.4672 | +0.558 | 0.5766 |  |
| **Site: UCSD (vs UAB)** | **+3.4327** | 0.6580 | ±1.3159 | **+5.217** | **1.82e-07** | *** |
| Site: UW (vs UAB) | -0.4172 | 0.6338 | ±1.2677 | -0.658 | 0.5104 |  |
| **Season: spring (vs autumn)** | **-2.3193** | 0.7586 | ±1.5172 | **-3.057** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5408** | 0.7383 | ±1.4766 | **+2.087** | **0.0369** | * |
| **Season: winter (vs autumn)** | **-5.7380** | 0.8525 | ±1.7050 | **-6.731** | **1.69e-11** | *** |
| Age (years) | -0.0515 | 0.0277 | ±0.0554 | -1.861 | 0.0628 | . |
| BMI (kg/m2) | -0.0603 | 0.0407 | ±0.0815 | -1.481 | 0.1386 |  |
| Hypertension | -1.0360 | 0.6225 | ±1.2450 | -1.664 | 0.0961 | . |
| High cholesterol | -0.2367 | 0.5866 | ±1.1731 | -0.404 | 0.6865 |  |
| **Kidney disease** | **+1.5152** | 0.6637 | ±1.3274 | **+2.283** | **0.0224** | * |
| Circulatory disease | -0.2885 | 0.6693 | ±1.3387 | -0.431 | 0.6665 |  |
| Any reading < 54 during wear (0/1) | +0.3943 | 0.6480 | ±1.2961 | +0.608 | 0.5429 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.2501**, Adj R² = **0.2302**, F-statistic = **12.56** (p = **1.51e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.1947** | 2.4240 | ±4.8480 | **+21.120** | **5.20e-99** | *** |
| Education: graduate level (vs college) | +0.1747 | 0.6308 | ±1.2616 | +0.277 | 0.7818 |  |
| Education: high school or below (vs college) | +0.3895 | 0.7329 | ±1.4657 | +0.531 | 0.5951 |  |
| **Site: UCSD (vs UAB)** | **+3.3855** | 0.6577 | ±1.3154 | **+5.148** | **2.64e-07** | *** |
| Site: UW (vs UAB) | -0.4676 | 0.6343 | ±1.2685 | -0.737 | 0.4610 |  |
| **Season: spring (vs autumn)** | **-2.3244** | 0.7598 | ±1.5197 | **-3.059** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5183** | 0.7386 | ±1.4771 | **+2.056** | **0.0398** | * |
| **Season: winter (vs autumn)** | **-5.7869** | 0.8597 | ±1.7195 | **-6.731** | **1.68e-11** | *** |
| Age (years) | -0.0524 | 0.0275 | ±0.0550 | -1.904 | 0.0569 | . |
| BMI (kg/m2) | -0.0602 | 0.0408 | ±0.0816 | -1.474 | 0.1405 |  |
| Hypertension | -0.9758 | 0.6212 | ±1.2424 | -1.571 | 0.1162 |  |
| High cholesterol | -0.2819 | 0.5882 | ±1.1763 | -0.479 | 0.6317 |  |
| **Kidney disease** | **+1.5289** | 0.6650 | ±1.3301 | **+2.299** | **0.0215** | * |
| Circulatory disease | -0.2803 | 0.6643 | ±1.3285 | -0.422 | 0.6731 |  |
| Time < 54 (%) | -0.3803 | 1.2618 | ±2.5236 | -0.301 | 0.7631 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.2500**, Adj R² = **0.2301**, F-statistic = **12.55** (p = **1.56e-25**), Residual SE = **6.046** on **527** df, AIC = **3503.4**, BIC = **3567.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.1741** | 2.4132 | ±4.8263 | **+21.206** | **8.37e-100** | *** |
| Education: graduate level (vs college) | +0.1789 | 0.6308 | ±1.2616 | +0.284 | 0.7767 |  |
| Education: high school or below (vs college) | +0.3944 | 0.7329 | ±1.4659 | +0.538 | 0.5905 |  |
| **Site: UCSD (vs UAB)** | **+3.3956** | 0.6572 | ±1.3144 | **+5.167** | **2.38e-07** | *** |
| Site: UW (vs UAB) | -0.4548 | 0.6365 | ±1.2730 | -0.714 | 0.4749 |  |
| **Season: spring (vs autumn)** | **-2.3296** | 0.7624 | ±1.5248 | **-3.056** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5181** | 0.7415 | ±1.4831 | **+2.047** | **0.0406** | * |
| **Season: winter (vs autumn)** | **-5.7818** | 0.8586 | ±1.7171 | **-6.734** | **1.65e-11** | *** |
| Age (years) | -0.0525 | 0.0276 | ±0.0551 | -1.905 | 0.0568 | . |
| BMI (kg/m2) | -0.0601 | 0.0407 | ±0.0815 | -1.475 | 0.1402 |  |
| Hypertension | -0.9895 | 0.6196 | ±1.2391 | -1.597 | 0.1102 |  |
| High cholesterol | -0.2736 | 0.5860 | ±1.1720 | -0.467 | 0.6406 |  |
| **Kidney disease** | **+1.5296** | 0.6671 | ±1.3342 | **+2.293** | **0.0219** | * |
| Circulatory disease | -0.2705 | 0.6647 | ±1.3294 | -0.407 | 0.6840 |  |
| Avg. daily time < 54 (%) | -0.1804 | 1.5089 | ±3.0179 | -0.120 | 0.9049 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.2503**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.43e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2318** | 2.4072 | ±4.8144 | **+21.283** | **1.64e-100** | *** |
| Education: graduate level (vs college) | +0.1743 | 0.6309 | ±1.2617 | +0.276 | 0.7824 |  |
| Education: high school or below (vs college) | +0.3999 | 0.7322 | ±1.4643 | +0.546 | 0.5849 |  |
| **Site: UCSD (vs UAB)** | **+3.3720** | 0.6583 | ±1.3166 | **+5.122** | **3.02e-07** | *** |
| Site: UW (vs UAB) | -0.4732 | 0.6337 | ±1.2674 | -0.747 | 0.4553 |  |
| **Season: spring (vs autumn)** | **-2.3418** | 0.7648 | ±1.5296 | **-3.062** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5076** | 0.7381 | ±1.4762 | **+2.043** | **0.0411** | * |
| **Season: winter (vs autumn)** | **-5.7946** | 0.8616 | ±1.7231 | **-6.726** | **1.75e-11** | *** |
| Age (years) | -0.0520 | 0.0275 | ±0.0551 | -1.891 | 0.0586 | . |
| BMI (kg/m2) | -0.0609 | 0.0407 | ±0.0813 | -1.498 | 0.1341 |  |
| Hypertension | -0.9731 | 0.6169 | ±1.2338 | -1.577 | 0.1147 |  |
| High cholesterol | -0.2906 | 0.5876 | ±1.1752 | -0.495 | 0.6209 |  |
| **Kidney disease** | **+1.5402** | 0.6663 | ±1.3326 | **+2.312** | **0.0208** | * |
| Circulatory disease | -0.2801 | 0.6649 | ±1.3297 | -0.421 | 0.6736 |  |
| Time 54-69, pooled (%) | -0.1471 | 0.3801 | ±0.7602 | -0.387 | 0.6987 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **542**, R² = **0.2504**, Adj R² = **0.2305**, F-statistic = **12.58** (p = **1.37e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.1**, BIC = **3567.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2194** | 2.4002 | ±4.8005 | **+21.339** | **4.90e-101** | *** |
| Education: graduate level (vs college) | +0.1698 | 0.6308 | ±1.2617 | +0.269 | 0.7878 |  |
| Education: high school or below (vs college) | +0.3968 | 0.7317 | ±1.4634 | +0.542 | 0.5876 |  |
| **Site: UCSD (vs UAB)** | **+3.3666** | 0.6577 | ±1.3155 | **+5.118** | **3.08e-07** | *** |
| Site: UW (vs UAB) | -0.4825 | 0.6337 | ±1.2674 | -0.761 | 0.4464 |  |
| **Season: spring (vs autumn)** | **-2.3465** | 0.7651 | ±1.5301 | **-3.067** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5039** | 0.7383 | ±1.4765 | **+2.037** | **0.0416** | * |
| **Season: winter (vs autumn)** | **-5.7975** | 0.8619 | ±1.7237 | **-6.727** | **1.74e-11** | *** |
| Age (years) | -0.0518 | 0.0275 | ±0.0551 | -1.881 | 0.0599 | . |
| BMI (kg/m2) | -0.0606 | 0.0406 | ±0.0812 | -1.493 | 0.1355 |  |
| Hypertension | -0.9679 | 0.6164 | ±1.2328 | -1.570 | 0.1164 |  |
| High cholesterol | -0.2966 | 0.5882 | ±1.1764 | -0.504 | 0.6141 |  |
| **Kidney disease** | **+1.5406** | 0.6654 | ±1.3308 | **+2.315** | **0.0206** | * |
| Circulatory disease | -0.2859 | 0.6642 | ±1.3284 | -0.430 | 0.6669 |  |
| Avg. daily time 54-69 (%) | -0.1637 | 0.3642 | ±0.7285 | -0.449 | 0.6532 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **542**, R² = **0.2503**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.42e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2342** | 2.4124 | ±4.8248 | **+21.238** | **4.29e-100** | *** |
| Education: graduate level (vs college) | +0.1728 | 0.6307 | ±1.2614 | +0.274 | 0.7841 |  |
| Education: high school or below (vs college) | +0.3961 | 0.7320 | ±1.4640 | +0.541 | 0.5884 |  |
| **Site: UCSD (vs UAB)** | **+3.3700** | 0.6586 | ±1.3172 | **+5.117** | **3.10e-07** | *** |
| Site: UW (vs UAB) | -0.4774 | 0.6338 | ±1.2675 | -0.753 | 0.4513 |  |
| **Season: spring (vs autumn)** | **-2.3411** | 0.7643 | ±1.5287 | **-3.063** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5065** | 0.7386 | ±1.4771 | **+2.040** | **0.0414** | * |
| **Season: winter (vs autumn)** | **-5.7970** | 0.8624 | ±1.7248 | **-6.722** | **1.80e-11** | *** |
| Age (years) | -0.0521 | 0.0275 | ±0.0550 | -1.893 | 0.0584 | . |
| BMI (kg/m2) | -0.0608 | 0.0407 | ±0.0814 | -1.493 | 0.1354 |  |
| Hypertension | -0.9690 | 0.6177 | ±1.2354 | -1.569 | 0.1167 |  |
| High cholesterol | -0.2929 | 0.5881 | ±1.1761 | -0.498 | 0.6184 |  |
| **Kidney disease** | **+1.5394** | 0.6663 | ±1.3325 | **+2.311** | **0.0209** | * |
| Circulatory disease | -0.2832 | 0.6647 | ±1.3294 | -0.426 | 0.6700 |  |
| Time < 70 (%) | -0.1260 | 0.3108 | ±0.6215 | -0.406 | 0.6851 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **542**, R² = **0.2504**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.40e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2146** | 2.4044 | ±4.8088 | **+21.300** | **1.13e-100** | *** |
| Education: graduate level (vs college) | +0.1708 | 0.6308 | ±1.2616 | +0.271 | 0.7866 |  |
| Education: high school or below (vs college) | +0.3934 | 0.7319 | ±1.4639 | +0.538 | 0.5909 |  |
| **Site: UCSD (vs UAB)** | **+3.3705** | 0.6576 | ±1.3153 | **+5.125** | **2.97e-07** | *** |
| Site: UW (vs UAB) | -0.4801 | 0.6340 | ±1.2680 | -0.757 | 0.4489 |  |
| **Season: spring (vs autumn)** | **-2.3475** | 0.7651 | ±1.5303 | **-3.068** | **0.0022** | ** |
| **Season: summer (vs autumn)** | **+1.5024** | 0.7397 | ±1.4795 | **+2.031** | **0.0423** | * |
| **Season: winter (vs autumn)** | **-5.7983** | 0.8618 | ±1.7235 | **-6.728** | **1.72e-11** | *** |
| Age (years) | -0.0520 | 0.0275 | ±0.0551 | -1.888 | 0.0591 | . |
| BMI (kg/m2) | -0.0604 | 0.0406 | ±0.0813 | -1.486 | 0.1372 |  |
| Hypertension | -0.9699 | 0.6170 | ±1.2341 | -1.572 | 0.1160 |  |
| High cholesterol | -0.2942 | 0.5874 | ±1.1748 | -0.501 | 0.6164 |  |
| **Kidney disease** | **+1.5396** | 0.6654 | ±1.3307 | **+2.314** | **0.0207** | * |
| Circulatory disease | -0.2842 | 0.6642 | ±1.3285 | -0.428 | 0.6688 |  |
| Avg. daily time < 70 (%) | -0.1184 | 0.2831 | ±0.5661 | -0.418 | 0.6757 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.2502**, Adj R² = **0.2303**, F-statistic = **12.56** (p = **1.47e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6547** | 2.8198 | ±5.6395 | **+18.319** | **5.85e-75** | *** |
| Education: graduate level (vs college) | +0.2036 | 0.6307 | ±1.2615 | +0.323 | 0.7468 |  |
| Education: high school or below (vs college) | +0.3757 | 0.7349 | ±1.4699 | +0.511 | 0.6093 |  |
| **Site: UCSD (vs UAB)** | **+3.4287** | 0.6624 | ±1.3248 | **+5.176** | **2.26e-07** | *** |
| Site: UW (vs UAB) | -0.4114 | 0.6407 | ±1.2814 | -0.642 | 0.5208 |  |
| **Season: spring (vs autumn)** | **-2.3140** | 0.7583 | ±1.5165 | **-3.052** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5609** | 0.7395 | ±1.4790 | **+2.111** | **0.0348** | * |
| **Season: winter (vs autumn)** | **-5.7724** | 0.8515 | ±1.7029 | **-6.779** | **1.21e-11** | *** |
| Age (years) | -0.0515 | 0.0275 | ±0.0549 | -1.874 | 0.0609 | . |
| BMI (kg/m2) | -0.0611 | 0.0409 | ±0.0818 | -1.495 | 0.1349 |  |
| Hypertension | -1.0106 | 0.6198 | ±1.2395 | -1.631 | 0.1030 |  |
| High cholesterol | -0.2546 | 0.5849 | ±1.1699 | -0.435 | 0.6633 |  |
| **Kidney disease** | **+1.5101** | 0.6639 | ±1.3278 | **+2.275** | **0.0229** | * |
| Circulatory disease | -0.2742 | 0.6646 | ±1.3292 | -0.413 | 0.6799 |  |
| Time 54-250, pooled (%) | -0.0063 | 0.0153 | ±0.0305 | -0.410 | 0.6821 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.2502**, Adj R² = **0.2303**, F-statistic = **12.56** (p = **1.48e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6650** | 2.8599 | ±5.7198 | **+18.065** | **5.99e-73** | *** |
| Education: graduate level (vs college) | +0.2032 | 0.6309 | ±1.2618 | +0.322 | 0.7474 |  |
| Education: high school or below (vs college) | +0.3760 | 0.7353 | ±1.4705 | +0.511 | 0.6091 |  |
| **Site: UCSD (vs UAB)** | **+3.4290** | 0.6625 | ±1.3249 | **+5.176** | **2.27e-07** | *** |
| Site: UW (vs UAB) | -0.4127 | 0.6406 | ±1.2812 | -0.644 | 0.5194 |  |
| **Season: spring (vs autumn)** | **-2.3152** | 0.7582 | ±1.5164 | **-3.053** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5587** | 0.7387 | ±1.4775 | **+2.110** | **0.0349** | * |
| **Season: winter (vs autumn)** | **-5.7737** | 0.8518 | ±1.7036 | **-6.778** | **1.22e-11** | *** |
| Age (years) | -0.0516 | 0.0275 | ±0.0549 | -1.880 | 0.0601 | . |
| BMI (kg/m2) | -0.0611 | 0.0409 | ±0.0818 | -1.495 | 0.1349 |  |
| Hypertension | -1.0097 | 0.6196 | ±1.2392 | -1.630 | 0.1032 |  |
| High cholesterol | -0.2547 | 0.5847 | ±1.1695 | -0.436 | 0.6631 |  |
| **Kidney disease** | **+1.5084** | 0.6644 | ±1.3287 | **+2.270** | **0.0232** | * |
| Circulatory disease | -0.2751 | 0.6644 | ±1.3289 | -0.414 | 0.6789 |  |
| Avg. daily time 54-250 (%) | -0.0062 | 0.0156 | ±0.0313 | -0.399 | 0.6899 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.2501**, Adj R² = **0.2302**, F-statistic = **12.56** (p = **1.50e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0577** | 2.4084 | ±4.8169 | **+21.199** | **9.66e-100** | *** |
| Education: graduate level (vs college) | +0.1760 | 0.6318 | ±1.2637 | +0.279 | 0.7805 |  |
| Education: high school or below (vs college) | +0.3835 | 0.7305 | ±1.4609 | +0.525 | 0.5995 |  |
| **Site: UCSD (vs UAB)** | **+3.4233** | 0.6583 | ±1.3166 | **+5.200** | **1.99e-07** | *** |
| Site: UW (vs UAB) | -0.4415 | 0.6356 | ±1.2712 | -0.695 | 0.4873 |  |
| **Season: spring (vs autumn)** | **-2.3317** | 0.7537 | ±1.5075 | **-3.094** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.5215** | 0.7346 | ±1.4692 | **+2.071** | **0.0383** | * |
| **Season: winter (vs autumn)** | **-5.7922** | 0.8549 | ±1.7098 | **-6.775** | **1.24e-11** | *** |
| Age (years) | -0.0529 | 0.0276 | ±0.0552 | -1.918 | 0.0552 | . |
| BMI (kg/m2) | -0.0617 | 0.0408 | ±0.0816 | -1.512 | 0.1307 |  |
| Hypertension | -0.9822 | 0.6184 | ±1.2369 | -1.588 | 0.1122 |  |
| High cholesterol | -0.2535 | 0.5841 | ±1.1681 | -0.434 | 0.6643 |  |
| **Kidney disease** | **+1.5179** | 0.6629 | ±1.3259 | **+2.290** | **0.0220** | * |
| Circulatory disease | -0.2745 | 0.6663 | ±1.3326 | -0.412 | 0.6803 |  |
| Time 181-250, pooled (%) | +0.0067 | 0.0190 | ±0.0380 | +0.352 | 0.7248 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **542**, R² = **0.2502**, Adj R² = **0.2303**, F-statistic = **12.56** (p = **1.47e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.2**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0375** | 2.4120 | ±4.8240 | **+21.160** | **2.24e-99** | *** |
| Education: graduate level (vs college) | +0.1732 | 0.6318 | ±1.2635 | +0.274 | 0.7839 |  |
| Education: high school or below (vs college) | +0.3770 | 0.7300 | ±1.4599 | +0.516 | 0.6055 |  |
| **Site: UCSD (vs UAB)** | **+3.4285** | 0.6592 | ±1.3184 | **+5.201** | **1.98e-07** | *** |
| Site: UW (vs UAB) | -0.4393 | 0.6355 | ±1.2711 | -0.691 | 0.4894 |  |
| **Season: spring (vs autumn)** | **-2.3350** | 0.7538 | ±1.5076 | **-3.098** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.5191** | 0.7344 | ±1.4688 | **+2.069** | **0.0386** | * |
| **Season: winter (vs autumn)** | **-5.7984** | 0.8552 | ±1.7105 | **-6.780** | **1.20e-11** | *** |
| Age (years) | -0.0529 | 0.0276 | ±0.0551 | -1.918 | 0.0551 | . |
| BMI (kg/m2) | -0.0620 | 0.0408 | ±0.0816 | -1.519 | 0.1287 |  |
| Hypertension | -0.9794 | 0.6183 | ±1.2367 | -1.584 | 0.1132 |  |
| High cholesterol | -0.2525 | 0.5840 | ±1.1679 | -0.432 | 0.6655 |  |
| **Kidney disease** | **+1.5157** | 0.6628 | ±1.3255 | **+2.287** | **0.0222** | * |
| Circulatory disease | -0.2756 | 0.6665 | ±1.3330 | -0.413 | 0.6793 |  |
| Avg. daily time 181-250 (%) | +0.0078 | 0.0185 | ±0.0370 | +0.421 | 0.6736 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **542**, R² = **0.2503**, Adj R² = **0.2304**, F-statistic = **12.57** (p = **1.42e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.2**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.9731** | 2.3953 | ±4.7905 | **+21.281** | **1.71e-100** | *** |
| Education: graduate level (vs college) | +0.1949 | 0.6311 | ±1.2622 | +0.309 | 0.7574 |  |
| Education: high school or below (vs college) | +0.3652 | 0.7324 | ±1.4648 | +0.499 | 0.6181 |  |
| **Site: UCSD (vs UAB)** | **+3.4383** | 0.6632 | ±1.3264 | **+5.184** | **2.17e-07** | *** |
| Site: UW (vs UAB) | -0.4168 | 0.6375 | ±1.2750 | -0.654 | 0.5133 |  |
| **Season: spring (vs autumn)** | **-2.3277** | 0.7560 | ±1.5120 | **-3.079** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.5476** | 0.7383 | ±1.4767 | **+2.096** | **0.0361** | * |
| **Season: winter (vs autumn)** | **-5.7910** | 0.8541 | ±1.7081 | **-6.780** | **1.20e-11** | *** |
| Age (years) | -0.0519 | 0.0274 | ±0.0549 | -1.892 | 0.0586 | . |
| BMI (kg/m2) | -0.0621 | 0.0410 | ±0.0821 | -1.515 | 0.1299 |  |
| Hypertension | -0.9946 | 0.6190 | ±1.2379 | -1.607 | 0.1081 |  |
| High cholesterol | -0.2486 | 0.5846 | ±1.1693 | -0.425 | 0.6707 |  |
| **Kidney disease** | **+1.5073** | 0.6631 | ±1.3263 | **+2.273** | **0.0230** | * |
| Circulatory disease | -0.2813 | 0.6650 | ±1.3299 | -0.423 | 0.6723 |  |
| Time > 180 (%) | +0.0053 | 0.0110 | ±0.0220 | +0.480 | 0.6310 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **542**, R² = **0.2504**, Adj R² = **0.2305**, F-statistic = **12.57** (p = **1.39e-25**), Residual SE = **6.044** on **527** df, AIC = **3503.1**, BIC = **3567.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.9693** | 2.3940 | ±4.7880 | **+21.290** | **1.40e-100** | *** |
| Education: graduate level (vs college) | +0.1941 | 0.6311 | ±1.2622 | +0.308 | 0.7584 |  |
| Education: high school or below (vs college) | +0.3606 | 0.7325 | ±1.4650 | +0.492 | 0.6225 |  |
| **Site: UCSD (vs UAB)** | **+3.4422** | 0.6640 | ±1.3279 | **+5.184** | **2.17e-07** | *** |
| Site: UW (vs UAB) | -0.4148 | 0.6376 | ±1.2751 | -0.651 | 0.5153 |  |
| **Season: spring (vs autumn)** | **-2.3303** | 0.7559 | ±1.5119 | **-3.083** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.5459** | 0.7378 | ±1.4756 | **+2.095** | **0.0361** | * |
| **Season: winter (vs autumn)** | **-5.7952** | 0.8547 | ±1.7094 | **-6.781** | **1.20e-11** | *** |
| Age (years) | -0.0519 | 0.0274 | ±0.0549 | -1.892 | 0.0585 | . |
| BMI (kg/m2) | -0.0623 | 0.0410 | ±0.0821 | -1.519 | 0.1288 |  |
| Hypertension | -0.9936 | 0.6190 | ±1.2379 | -1.605 | 0.1084 |  |
| High cholesterol | -0.2483 | 0.5844 | ±1.1688 | -0.425 | 0.6710 |  |
| **Kidney disease** | **+1.5040** | 0.6632 | ±1.3264 | **+2.268** | **0.0233** | * |
| Circulatory disease | -0.2826 | 0.6651 | ±1.3303 | -0.425 | 0.6709 |  |
| Avg. daily time > 180 (%) | +0.0056 | 0.0109 | ±0.0219 | +0.513 | 0.6077 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **542**, R² = **0.2500**, Adj R² = **0.2301**, F-statistic = **12.55** (p = **1.57e-25**), Residual SE = **6.046** on **527** df, AIC = **3503.4**, BIC = **3567.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2101** | 2.4036 | ±4.8071 | **+21.306** | **1.00e-100** | *** |
| Education: graduate level (vs college) | +0.1736 | 0.6323 | ±1.2645 | +0.275 | 0.7837 |  |
| Education: high school or below (vs college) | +0.4142 | 0.7351 | ±1.4702 | +0.563 | 0.5732 |  |
| **Site: UCSD (vs UAB)** | **+3.3916** | 0.6655 | ±1.3311 | **+5.096** | **3.47e-07** | *** |
| Site: UW (vs UAB) | -0.4475 | 0.6363 | ±1.2725 | -0.703 | 0.4819 |  |
| **Season: spring (vs autumn)** | **-2.3088** | 0.7558 | ±1.5116 | **-3.055** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5256** | 0.7380 | ±1.4761 | **+2.067** | **0.0387** | * |
| **Season: winter (vs autumn)** | **-5.7591** | 0.8543 | ±1.7086 | **-6.741** | **1.57e-11** | *** |
| Age (years) | -0.0531 | 0.0275 | ±0.0550 | -1.929 | 0.0538 | . |
| BMI (kg/m2) | -0.0590 | 0.0413 | ±0.0826 | -1.430 | 0.1528 |  |
| Hypertension | -1.0024 | 0.6191 | ±1.2382 | -1.619 | 0.1054 |  |
| High cholesterol | -0.2705 | 0.5843 | ±1.1687 | -0.463 | 0.6435 |  |
| **Kidney disease** | **+1.5298** | 0.6646 | ±1.3292 | **+2.302** | **0.0213** | * |
| Circulatory disease | -0.2561 | 0.6642 | ±1.3285 | -0.386 | 0.6998 |  |
| Nocturnal time > 180 (%) | -0.0019 | 0.0095 | ±0.0189 | -0.206 | 0.8369 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.2502**, Adj R² = **0.2303**, F-statistic = **12.56** (p = **1.47e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0286** | 2.3887 | ±4.7774 | **+21.363** | **2.98e-101** | *** |
| Education: graduate level (vs college) | +0.2037 | 0.6307 | ±1.2615 | +0.323 | 0.7467 |  |
| Education: high school or below (vs college) | +0.3752 | 0.7350 | ±1.4699 | +0.510 | 0.6097 |  |
| **Site: UCSD (vs UAB)** | **+3.4286** | 0.6623 | ±1.3246 | **+5.177** | **2.26e-07** | *** |
| Site: UW (vs UAB) | -0.4115 | 0.6406 | ±1.2812 | -0.642 | 0.5206 |  |
| **Season: spring (vs autumn)** | **-2.3141** | 0.7582 | ±1.5165 | **-3.052** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5610** | 0.7394 | ±1.4788 | **+2.111** | **0.0348** | * |
| **Season: winter (vs autumn)** | **-5.7728** | 0.8515 | ±1.7031 | **-6.779** | **1.21e-11** | *** |
| Age (years) | -0.0515 | 0.0275 | ±0.0549 | -1.874 | 0.0610 | . |
| BMI (kg/m2) | -0.0611 | 0.0409 | ±0.0818 | -1.495 | 0.1349 |  |
| Hypertension | -1.0104 | 0.6197 | ±1.2395 | -1.630 | 0.1030 |  |
| High cholesterol | -0.2548 | 0.5849 | ±1.1698 | -0.436 | 0.6631 |  |
| **Kidney disease** | **+1.5100** | 0.6639 | ±1.3278 | **+2.275** | **0.0229** | * |
| Circulatory disease | -0.2746 | 0.6645 | ±1.3291 | -0.413 | 0.6795 |  |
| Time > 250 (%) | +0.0063 | 0.0153 | ±0.0305 | +0.414 | 0.6788 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 542)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **542**, R² = **0.2502**, Adj R² = **0.2303**, F-statistic = **12.56** (p = **1.47e-25**), Residual SE = **6.045** on **527** df, AIC = **3503.3**, BIC = **3567.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0407** | 2.3856 | ±4.7712 | **+21.395** | **1.48e-101** | *** |
| Education: graduate level (vs college) | +0.2033 | 0.6309 | ±1.2618 | +0.322 | 0.7473 |  |
| Education: high school or below (vs college) | +0.3755 | 0.7353 | ±1.4707 | +0.511 | 0.6096 |  |
| **Site: UCSD (vs UAB)** | **+3.4288** | 0.6624 | ±1.3247 | **+5.177** | **2.26e-07** | *** |
| Site: UW (vs UAB) | -0.4128 | 0.6404 | ±1.2809 | -0.645 | 0.5192 |  |
| **Season: spring (vs autumn)** | **-2.3157** | 0.7582 | ±1.5163 | **-3.054** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+1.5584** | 0.7386 | ±1.4771 | **+2.110** | **0.0348** | * |
| **Season: winter (vs autumn)** | **-5.7742** | 0.8519 | ±1.7038 | **-6.778** | **1.22e-11** | *** |
| Age (years) | -0.0516 | 0.0274 | ±0.0549 | -1.880 | 0.0601 | . |
| BMI (kg/m2) | -0.0611 | 0.0409 | ±0.0818 | -1.495 | 0.1349 |  |
| Hypertension | -1.0095 | 0.6196 | ±1.2392 | -1.629 | 0.1033 |  |
| High cholesterol | -0.2550 | 0.5847 | ±1.1694 | -0.436 | 0.6627 |  |
| **Kidney disease** | **+1.5084** | 0.6643 | ±1.3286 | **+2.271** | **0.0232** | * |
| Circulatory disease | -0.2755 | 0.6644 | ±1.3288 | -0.415 | 0.6785 |  |
| Avg. daily time > 250 (%) | +0.0063 | 0.0156 | ±0.0313 | +0.403 | 0.6870 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 542; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **542**, R² = **0.0682**, Adj R² = **0.0453**, F-statistic = **2.97** (p = **3.23e-04**), Residual SE = **17.841** on **528** df, AIC = **4675.5**, BIC = **4735.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.2272** | 9.3794 | ±18.7588 | **+13.565** | **6.50e-42** | *** |
| Education: graduate level (vs college) | -0.6600 | 1.5982 | ±3.1965 | -0.413 | 0.6796 |  |
| **Education: high school or below (vs college)** | **+5.9711** | 2.5465 | ±5.0929 | **+2.345** | **0.0190** | * |
| Site: UCSD (vs UAB) | +3.6077 | 2.0811 | ±4.1621 | +1.734 | 0.0830 | . |
| Site: UW (vs UAB) | -1.6926 | 1.7492 | ±3.4984 | -0.968 | 0.3332 |  |
| Season: spring (vs autumn) | +3.3906 | 1.8794 | ±3.7589 | +1.804 | 0.0712 | . |
| **Season: summer (vs autumn)** | **+5.0010** | 1.9597 | ±3.9195 | **+2.552** | **0.0107** | * |
| **Season: winter (vs autumn)** | **+6.5554** | 2.5277 | ±5.0555 | **+2.593** | **0.0095** | ** |
| Age (years) | -0.1647 | 0.0958 | ±0.1917 | -1.719 | 0.0857 | . |
| BMI (kg/m2) | +0.1399 | 0.1435 | ±0.2869 | +0.975 | 0.3295 |  |
| Hypertension | +0.6836 | 1.9658 | ±3.9316 | +0.348 | 0.7280 |  |
| High cholesterol | +2.2853 | 1.8143 | ±3.6286 | +1.260 | 0.2078 |  |
| Kidney disease | -1.9852 | 1.9576 | ±3.9152 | -1.014 | 0.3105 |  |
| Circulatory disease | +0.8686 | 2.0390 | ±4.0779 | +0.426 | 0.6701 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **542**, R² = **0.0779**, Adj R² = **0.0534**, F-statistic = **3.18** (p = **7.88e-05**), Residual SE = **17.765** on **527** df, AIC = **4671.8**, BIC = **4736.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+137.0407** | 10.0581 | ±20.1162 | **+13.625** | **2.85e-42** | *** |
| Education: graduate level (vs college) | -0.9152 | 1.5909 | ±3.1817 | -0.575 | 0.5651 |  |
| **Education: high school or below (vs college)** | **+6.5225** | 2.5323 | ±5.0646 | **+2.576** | **0.0100** | * |
| Site: UCSD (vs UAB) | +3.2945 | 2.0812 | ±4.1625 | +1.583 | 0.1134 |  |
| Site: UW (vs UAB) | -2.0599 | 1.7453 | ±3.4906 | -1.180 | 0.2379 |  |
| Season: spring (vs autumn) | +3.1296 | 1.8815 | ±3.7629 | +1.663 | 0.0962 | . |
| **Season: summer (vs autumn)** | **+4.6512** | 1.9713 | ±3.9425 | **+2.359** | **0.0183** | * |
| **Season: winter (vs autumn)** | **+6.5820** | 2.5149 | ±5.0299 | **+2.617** | **0.0089** | ** |
| Age (years) | -0.1767 | 0.0960 | ±0.1920 | -1.841 | 0.0657 | . |
| BMI (kg/m2) | +0.1692 | 0.1438 | ±0.2876 | +1.176 | 0.2395 |  |
| Hypertension | +0.7583 | 1.9509 | ±3.9018 | +0.389 | 0.6975 |  |
| High cholesterol | +2.2462 | 1.7998 | ±3.5996 | +1.248 | 0.2120 |  |
| Kidney disease | -2.0661 | 1.9475 | ±3.8950 | -1.061 | 0.2887 |  |
| Circulatory disease | +1.0221 | 2.0298 | ±4.0595 | +0.504 | 0.6146 |  |
| **HbA1c (%)** | **-1.3552** | 0.6140 | ±1.2280 | **-2.207** | **0.0273** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **542**, R² = **0.0756**, Adj R² = **0.0511**, F-statistic = **3.08** (p = **1.27e-04**), Residual SE = **17.787** on **527** df, AIC = **4673.2**, BIC = **4737.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+134.3027** | 10.4583 | ±20.9166 | **+12.842** | **9.57e-38** | *** |
| Education: graduate level (vs college) | -0.8523 | 1.5846 | ±3.1692 | -0.538 | 0.5907 |  |
| **Education: high school or below (vs college)** | **+6.3752** | 2.5430 | ±5.0861 | **+2.507** | **0.0122** | * |
| Site: UCSD (vs UAB) | +3.2781 | 2.1095 | ±4.2189 | +1.554 | 0.1202 |  |
| Site: UW (vs UAB) | -1.9832 | 1.7530 | ±3.5060 | -1.131 | 0.2579 |  |
| Season: spring (vs autumn) | +3.5181 | 1.8830 | ±3.7661 | +1.868 | 0.0617 | . |
| **Season: summer (vs autumn)** | **+4.7498** | 1.9772 | ±3.9544 | **+2.402** | **0.0163** | * |
| **Season: winter (vs autumn)** | **+6.7882** | 2.4854 | ±4.9708 | **+2.731** | **0.0063** | ** |
| Age (years) | -0.1759 | 0.0973 | ±0.1947 | -1.807 | 0.0708 | . |
| BMI (kg/m2) | +0.1575 | 0.1421 | ±0.2841 | +1.108 | 0.2677 |  |
| Hypertension | +0.6798 | 1.9560 | ±3.9120 | +0.348 | 0.7282 |  |
| High cholesterol | +2.1847 | 1.8030 | ±3.6061 | +1.212 | 0.2256 |  |
| Kidney disease | -1.8544 | 1.9612 | ±3.9224 | -0.946 | 0.3444 |  |
| Circulatory disease | +1.0713 | 2.0324 | ±4.0647 | +0.527 | 0.5981 |  |
| Mean glucose (mg/dL) | -0.0396 | 0.0203 | ±0.0405 | -1.953 | 0.0509 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **542**, R² = **0.0756**, Adj R² = **0.0511**, F-statistic = **3.08** (p = **1.27e-04**), Residual SE = **17.787** on **527** df, AIC = **4673.2**, BIC = **4737.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+139.7798** | 11.9943 | ±23.9885 | **+11.654** | **2.19e-31** | *** |
| Education: graduate level (vs college) | -0.8523 | 1.5846 | ±3.1692 | -0.538 | 0.5907 |  |
| **Education: high school or below (vs college)** | **+6.3752** | 2.5430 | ±5.0861 | **+2.507** | **0.0122** | * |
| Site: UCSD (vs UAB) | +3.2781 | 2.1095 | ±4.2189 | +1.554 | 0.1202 |  |
| Site: UW (vs UAB) | -1.9832 | 1.7530 | ±3.5060 | -1.131 | 0.2579 |  |
| Season: spring (vs autumn) | +3.5181 | 1.8830 | ±3.7661 | +1.868 | 0.0617 | . |
| **Season: summer (vs autumn)** | **+4.7498** | 1.9772 | ±3.9544 | **+2.402** | **0.0163** | * |
| **Season: winter (vs autumn)** | **+6.7882** | 2.4854 | ±4.9708 | **+2.731** | **0.0063** | ** |
| Age (years) | -0.1759 | 0.0973 | ±0.1947 | -1.807 | 0.0708 | . |
| BMI (kg/m2) | +0.1575 | 0.1421 | ±0.2841 | +1.108 | 0.2677 |  |
| Hypertension | +0.6798 | 1.9560 | ±3.9120 | +0.348 | 0.7282 |  |
| High cholesterol | +2.1847 | 1.8030 | ±3.6061 | +1.212 | 0.2256 |  |
| Kidney disease | -1.8544 | 1.9612 | ±3.9224 | -0.946 | 0.3444 |  |
| Circulatory disease | +1.0713 | 2.0324 | ±4.0647 | +0.527 | 0.5981 |  |
| GMI (%) | -1.6547 | 0.8474 | ±1.6948 | -1.953 | 0.0509 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **542**, R² = **0.0740**, Adj R² = **0.0494**, F-statistic = **3.01** (p = **1.80e-04**), Residual SE = **17.802** on **527** df, AIC = **4674.1**, BIC = **4738.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.8842** | 10.6615 | ±21.3231 | **+12.464** | **1.18e-35** | *** |
| Education: graduate level (vs college) | -0.8820 | 1.5855 | ±3.1710 | -0.556 | 0.5780 |  |
| **Education: high school or below (vs college)** | **+6.2747** | 2.5219 | ±5.0438 | **+2.488** | **0.0128** | * |
| Site: UCSD (vs UAB) | +3.2924 | 2.1157 | ±4.2315 | +1.556 | 0.1197 |  |
| Site: UW (vs UAB) | -1.8264 | 1.7487 | ±3.4975 | -1.044 | 0.2963 |  |
| Season: spring (vs autumn) | +3.5655 | 1.8786 | ±3.7571 | +1.898 | 0.0577 | . |
| **Season: summer (vs autumn)** | **+4.8136** | 1.9770 | ±3.9539 | **+2.435** | **0.0149** | * |
| **Season: winter (vs autumn)** | **+6.7757** | 2.4844 | ±4.9687 | **+2.727** | **0.0064** | ** |
| Age (years) | -0.1798 | 0.0988 | ±0.1975 | -1.820 | 0.0687 | . |
| BMI (kg/m2) | +0.1648 | 0.1416 | ±0.2832 | +1.163 | 0.2446 |  |
| Hypertension | +0.6491 | 1.9604 | ±3.9209 | +0.331 | 0.7406 |  |
| High cholesterol | +2.1926 | 1.8012 | ±3.6023 | +1.217 | 0.2235 |  |
| Kidney disease | -1.9617 | 1.9616 | ±3.9232 | -1.000 | 0.3173 |  |
| Circulatory disease | +1.0490 | 2.0255 | ±4.0510 | +0.518 | 0.6045 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0328 | 0.0214 | ±0.0429 | -1.529 | 0.1263 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **542**, R² = **0.0711**, Adj R² = **0.0465**, F-statistic = **2.88** (p = **3.25e-04**), Residual SE = **17.830** on **527** df, AIC = **4675.8**, BIC = **4740.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.7447** | 9.5610 | ±19.1219 | **+13.675** | **1.44e-42** | *** |
| Education: graduate level (vs college) | -0.8033 | 1.6015 | ±3.2030 | -0.502 | 0.6159 |  |
| **Education: high school or below (vs college)** | **+6.2250** | 2.5474 | ±5.0947 | **+2.444** | **0.0145** | * |
| Site: UCSD (vs UAB) | +3.4501 | 2.1052 | ±4.2105 | +1.639 | 0.1013 |  |
| Site: UW (vs UAB) | -1.9942 | 1.7685 | ±3.5370 | -1.128 | 0.2595 |  |
| Season: spring (vs autumn) | +3.4793 | 1.8921 | ±3.7842 | +1.839 | 0.0659 | . |
| **Season: summer (vs autumn)** | **+4.8154** | 1.9733 | ±3.9466 | **+2.440** | **0.0147** | * |
| **Season: winter (vs autumn)** | **+6.6887** | 2.5233 | ±5.0465 | **+2.651** | **0.0080** | ** |
| Age (years) | -0.1681 | 0.0958 | ±0.1917 | -1.754 | 0.0794 | . |
| BMI (kg/m2) | +0.1466 | 0.1442 | ±0.2883 | +1.017 | 0.3093 |  |
| Hypertension | +0.7474 | 1.9549 | ±3.9097 | +0.382 | 0.7022 |  |
| High cholesterol | +2.1890 | 1.7971 | ±3.5942 | +1.218 | 0.2232 |  |
| Kidney disease | -1.5516 | 1.9639 | ±3.9277 | -0.790 | 0.4295 |  |
| Circulatory disease | +0.9733 | 2.0305 | ±4.0610 | +0.479 | 0.6317 |  |
| Glucose SD, pooled (mg/dL) | -0.0834 | 0.0747 | ±0.1494 | -1.116 | 0.2643 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **542**, R² = **0.0689**, Adj R² = **0.0442**, F-statistic = **2.79** (p = **5.08e-04**), Residual SE = **17.851** on **527** df, AIC = **4677.1**, BIC = **4741.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.0657** | 9.7908 | ±19.5817 | **+13.182** | **1.11e-39** | *** |
| Education: graduate level (vs college) | -0.7172 | 1.6058 | ±3.2116 | -0.447 | 0.6551 |  |
| **Education: high school or below (vs college)** | **+6.1218** | 2.5445 | ±5.0891 | **+2.406** | **0.0161** | * |
| Site: UCSD (vs UAB) | +3.5294 | 2.0973 | ±4.1945 | +1.683 | 0.0924 | . |
| Site: UW (vs UAB) | -1.8259 | 1.7678 | ±3.5355 | -1.033 | 0.3017 |  |
| Season: spring (vs autumn) | +3.4421 | 1.8884 | ±3.7768 | +1.823 | 0.0683 | . |
| **Season: summer (vs autumn)** | **+4.9005** | 1.9801 | ±3.9602 | **+2.475** | **0.0133** | * |
| **Season: winter (vs autumn)** | **+6.6005** | 2.5356 | ±5.0712 | **+2.603** | **0.0092** | ** |
| Age (years) | -0.1657 | 0.0960 | ±0.1920 | -1.726 | 0.0843 | . |
| BMI (kg/m2) | +0.1399 | 0.1435 | ±0.2871 | +0.975 | 0.3297 |  |
| Hypertension | +0.6996 | 1.9635 | ±3.9269 | +0.356 | 0.7216 |  |
| High cholesterol | +2.2446 | 1.8092 | ±3.6184 | +1.241 | 0.2147 |  |
| Kidney disease | -1.7522 | 1.9655 | ±3.9309 | -0.892 | 0.3727 |  |
| Circulatory disease | +0.9036 | 2.0416 | ±4.0832 | +0.443 | 0.6581 |  |
| Avg. daily SD (mg/dL) | -0.0473 | 0.0725 | ±0.1450 | -0.652 | 0.5141 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **542**, R² = **0.0683**, Adj R² = **0.0435**, F-statistic = **2.76** (p = **5.78e-04**), Residual SE = **17.857** on **527** df, AIC = **4677.4**, BIC = **4741.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.5309** | 9.0795 | ±18.1591 | **+13.936** | **3.84e-44** | *** |
| Education: graduate level (vs college) | -0.6488 | 1.6102 | ±3.2203 | -0.403 | 0.6870 |  |
| **Education: high school or below (vs college)** | **+5.9538** | 2.5494 | ±5.0987 | **+2.335** | **0.0195** | * |
| Site: UCSD (vs UAB) | +3.6146 | 2.0864 | ±4.1727 | +1.733 | 0.0832 | . |
| Site: UW (vs UAB) | -1.6564 | 1.7564 | ±3.5128 | -0.943 | 0.3456 |  |
| Season: spring (vs autumn) | +3.3915 | 1.8835 | ±3.7669 | +1.801 | 0.0718 | . |
| **Season: summer (vs autumn)** | **+5.0158** | 1.9556 | ±3.9112 | **+2.565** | **0.0103** | * |
| **Season: winter (vs autumn)** | **+6.5526** | 2.5368 | ±5.0736 | **+2.583** | **0.0098** | ** |
| Age (years) | -0.1651 | 0.0965 | ±0.1931 | -1.710 | 0.0872 | . |
| BMI (kg/m2) | +0.1402 | 0.1433 | ±0.2865 | +0.979 | 0.3276 |  |
| Hypertension | +0.6656 | 1.9493 | ±3.8986 | +0.341 | 0.7328 |  |
| High cholesterol | +2.2940 | 1.8139 | ±3.6278 | +1.265 | 0.2060 |  |
| Kidney disease | -2.0628 | 1.9620 | ±3.9241 | -1.051 | 0.2931 |  |
| Circulatory disease | +0.8674 | 2.0424 | ±4.0848 | +0.425 | 0.6710 |  |
| CV (%) | +0.0291 | 0.1418 | ±0.2836 | +0.205 | 0.8372 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **542**, R² = **0.0683**, Adj R² = **0.0436**, F-statistic = **2.76** (p = **5.76e-04**), Residual SE = **17.857** on **527** df, AIC = **4677.4**, BIC = **4741.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.0299** | 10.7918 | ±21.5835 | **+11.864** | **1.83e-32** | *** |
| Education: graduate level (vs college) | -0.6471 | 1.6121 | ±3.2242 | -0.401 | 0.6881 |  |
| **Education: high school or below (vs college)** | **+5.9565** | 2.5465 | ±5.0930 | **+2.339** | **0.0193** | * |
| Site: UCSD (vs UAB) | +3.6043 | 2.0851 | ±4.1702 | +1.729 | 0.0839 | . |
| Site: UW (vs UAB) | -1.6635 | 1.7534 | ±3.5068 | -0.949 | 0.3428 |  |
| Season: spring (vs autumn) | +3.3832 | 1.8879 | ±3.7758 | +1.792 | 0.0731 | . |
| **Season: summer (vs autumn)** | **+4.9958** | 1.9639 | ±3.9277 | **+2.544** | **0.0110** | * |
| **Season: winter (vs autumn)** | **+6.5453** | 2.5444 | ±5.0888 | **+2.572** | **0.0101** | * |
| Age (years) | -0.1650 | 0.0963 | ±0.1926 | -1.713 | 0.0867 | . |
| BMI (kg/m2) | +0.1407 | 0.1429 | ±0.2858 | +0.985 | 0.3247 |  |
| Hypertension | +0.6708 | 1.9581 | ±3.9161 | +0.343 | 0.7319 |  |
| High cholesterol | +2.2822 | 1.8192 | ±3.6384 | +1.255 | 0.2097 |  |
| Kidney disease | -2.0555 | 1.9519 | ±3.9038 | -1.053 | 0.2923 |  |
| Circulatory disease | +0.8581 | 2.0400 | ±4.0800 | +0.421 | 0.6740 |  |
| Mean / SD ratio | -0.1850 | 0.8001 | ±1.6001 | -0.231 | 0.8172 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **542**, R² = **0.0697**, Adj R² = **0.0450**, F-statistic = **2.82** (p = **4.34e-04**), Residual SE = **17.844** on **527** df, AIC = **4676.6**, BIC = **4741.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.1044** | 10.1742 | ±20.3484 | **+12.788** | **1.92e-37** | *** |
| Education: graduate level (vs college) | -0.6110 | 1.6139 | ±3.2278 | -0.379 | 0.7050 |  |
| **Education: high school or below (vs college)** | **+5.8988** | 2.5400 | ±5.0799 | **+2.322** | **0.0202** | * |
| Site: UCSD (vs UAB) | +3.5902 | 2.0862 | ±4.1725 | +1.721 | 0.0853 | . |
| Site: UW (vs UAB) | -1.6171 | 1.7531 | ±3.5061 | -0.922 | 0.3563 |  |
| Season: spring (vs autumn) | +3.3976 | 1.8840 | ±3.7679 | +1.803 | 0.0713 | . |
| **Season: summer (vs autumn)** | **+5.0167** | 1.9576 | ±3.9151 | **+2.563** | **0.0104** | * |
| **Season: winter (vs autumn)** | **+6.5639** | 2.5256 | ±5.0513 | **+2.599** | **0.0094** | ** |
| Age (years) | -0.1671 | 0.0965 | ±0.1930 | -1.732 | 0.0833 | . |
| BMI (kg/m2) | +0.1486 | 0.1425 | ±0.2849 | +1.043 | 0.2969 |  |
| Hypertension | +0.6533 | 1.9651 | ±3.9303 | +0.332 | 0.7396 |  |
| High cholesterol | +2.2859 | 1.8187 | ±3.6373 | +1.257 | 0.2088 |  |
| Kidney disease | -2.2382 | 1.9629 | ±3.9257 | -1.140 | 0.2542 |  |
| Circulatory disease | +0.8643 | 2.0394 | ±4.0788 | +0.424 | 0.6717 |  |
| Avg. daily mean/SD | -0.5898 | 0.6093 | ±1.2186 | -0.968 | 0.3330 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **542**, R² = **0.0682**, Adj R² = **0.0435**, F-statistic = **2.76** (p = **5.84e-04**), Residual SE = **17.858** on **527** df, AIC = **4677.5**, BIC = **4741.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.6264** | 9.5731 | ±19.1462 | **+13.227** | **6.10e-40** | *** |
| Education: graduate level (vs college) | -0.6430 | 1.6061 | ±3.2122 | -0.400 | 0.6889 |  |
| **Education: high school or below (vs college)** | **+5.9556** | 2.5719 | ±5.1438 | **+2.316** | **0.0206** | * |
| Site: UCSD (vs UAB) | +3.6191 | 2.0753 | ±4.1505 | +1.744 | 0.0812 | . |
| Site: UW (vs UAB) | -1.6542 | 1.7388 | ±3.4777 | -0.951 | 0.3414 |  |
| Season: spring (vs autumn) | +3.3881 | 1.8849 | ±3.7699 | +1.797 | 0.0723 | . |
| **Season: summer (vs autumn)** | **+5.0259** | 1.9621 | ±3.9241 | **+2.562** | **0.0104** | * |
| **Season: winter (vs autumn)** | **+6.5576** | 2.5305 | ±5.0610 | **+2.591** | **0.0096** | ** |
| Age (years) | -0.1634 | 0.0941 | ±0.1881 | -1.737 | 0.0824 | . |
| BMI (kg/m2) | +0.1402 | 0.1435 | ±0.2871 | +0.976 | 0.3288 |  |
| Hypertension | +0.6819 | 1.9697 | ±3.9394 | +0.346 | 0.7292 |  |
| High cholesterol | +2.2910 | 1.8264 | ±3.6527 | +1.254 | 0.2097 |  |
| Kidney disease | -2.0121 | 1.9267 | ±3.8534 | -1.044 | 0.2963 |  |
| Circulatory disease | +0.8648 | 2.0496 | ±4.0993 | +0.422 | 0.6731 |  |
| MAG (mg/dL/h) | +0.0105 | 0.0882 | ±0.1763 | +0.120 | 0.9048 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **542**, R² = **0.0684**, Adj R² = **0.0437**, F-statistic = **2.77** (p = **5.60e-04**), Residual SE = **17.856** on **527** df, AIC = **4677.4**, BIC = **4741.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.6548** | 10.0538 | ±20.1075 | **+12.797** | **1.71e-37** | *** |
| Education: graduate level (vs college) | -0.6921 | 1.6064 | ±3.2129 | -0.431 | 0.6666 |  |
| **Education: high school or below (vs college)** | **+6.0579** | 2.5446 | ±5.0891 | **+2.381** | **0.0173** | * |
| Site: UCSD (vs UAB) | +3.5597 | 2.0934 | ±4.1868 | +1.700 | 0.0891 | . |
| Site: UW (vs UAB) | -1.7672 | 1.7595 | ±3.5189 | -1.004 | 0.3152 |  |
| Season: spring (vs autumn) | +3.4305 | 1.8924 | ±3.7849 | +1.813 | 0.0699 | . |
| **Season: summer (vs autumn)** | **+4.9718** | 1.9682 | ±3.9364 | **+2.526** | **0.0115** | * |
| **Season: winter (vs autumn)** | **+6.5898** | 2.5441 | ±5.0882 | **+2.590** | **0.0096** | ** |
| Age (years) | -0.1667 | 0.0961 | ±0.1922 | -1.735 | 0.0828 | . |
| BMI (kg/m2) | +0.1389 | 0.1435 | ±0.2871 | +0.968 | 0.3331 |  |
| Hypertension | +0.6781 | 1.9685 | ±3.9371 | +0.344 | 0.7305 |  |
| High cholesterol | +2.2783 | 1.8143 | ±3.6287 | +1.256 | 0.2092 |  |
| Kidney disease | -1.8455 | 1.9535 | ±3.9070 | -0.945 | 0.3448 |  |
| Circulatory disease | +0.8966 | 2.0408 | ±4.0816 | +0.439 | 0.6604 |  |
| Avg. daily range (mg/dL) | -0.0080 | 0.0213 | ±0.0426 | -0.375 | 0.7080 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **542**, R² = **0.0785**, Adj R² = **0.0540**, F-statistic = **3.21** (p = **6.91e-05**), Residual SE = **17.759** on **527** df, AIC = **4671.5**, BIC = **4735.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.9011** | 9.3642 | ±18.7284 | **+13.979** | **2.10e-44** | *** |
| Education: graduate level (vs college) | -1.0600 | 1.6023 | ±3.2046 | -0.662 | 0.5083 |  |
| **Education: high school or below (vs college)** | **+6.0714** | 2.5207 | ±5.0413 | **+2.409** | **0.0160** | * |
| Site: UCSD (vs UAB) | +3.3887 | 2.1021 | ±4.2041 | +1.612 | 0.1069 |  |
| Site: UW (vs UAB) | -2.1767 | 1.7713 | ±3.5426 | -1.229 | 0.2191 |  |
| Season: spring (vs autumn) | +3.3508 | 1.8715 | ±3.7431 | +1.790 | 0.0734 | . |
| **Season: summer (vs autumn)** | **+4.8536** | 1.9489 | ±3.8979 | **+2.490** | **0.0128** | * |
| **Season: winter (vs autumn)** | **+6.8801** | 2.4829 | ±4.9658 | **+2.771** | **0.0056** | ** |
| Age (years) | -0.1838 | 0.0958 | ±0.1916 | -1.919 | 0.0550 | . |
| BMI (kg/m2) | +0.1669 | 0.1489 | ±0.2977 | +1.121 | 0.2622 |  |
| Hypertension | +0.9566 | 1.9556 | ±3.9113 | +0.489 | 0.6247 |  |
| High cholesterol | +2.1181 | 1.7861 | ±3.5723 | +1.186 | 0.2357 |  |
| Kidney disease | -1.6493 | 1.9674 | ±3.9349 | -0.838 | 0.4019 |  |
| Circulatory disease | +1.3292 | 1.9863 | ±3.9727 | +0.669 | 0.5034 |  |
| SD of daily means (mg/dL) | -0.2203 | 0.1542 | ±0.3084 | -1.428 | 0.1532 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **542**, R² = **0.0741**, Adj R² = **0.0495**, F-statistic = **3.01** (p = **1.76e-04**), Residual SE = **17.801** on **527** df, AIC = **4674.1**, BIC = **4738.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.5735** | 9.5437 | ±19.0874 | **+12.948** | **2.41e-38** | *** |
| Education: graduate level (vs college) | -0.7921 | 1.5815 | ±3.1630 | -0.501 | 0.6165 |  |
| **Education: high school or below (vs college)** | **+6.3551** | 2.5546 | ±5.1092 | **+2.488** | **0.0129** | * |
| Site: UCSD (vs UAB) | +3.2540 | 2.1054 | ±4.2109 | +1.546 | 0.1222 |  |
| Site: UW (vs UAB) | -1.9645 | 1.7411 | ±3.4821 | -1.128 | 0.2592 |  |
| Season: spring (vs autumn) | +3.5178 | 1.8761 | ±3.7521 | +1.875 | 0.0608 | . |
| **Season: summer (vs autumn)** | **+4.8303** | 1.9696 | ±3.9391 | **+2.452** | **0.0142** | * |
| **Season: winter (vs autumn)** | **+6.7826** | 2.4802 | ±4.9605 | **+2.735** | **0.0062** | ** |
| Age (years) | -0.1715 | 0.0970 | ±0.1941 | -1.767 | 0.0772 | . |
| BMI (kg/m2) | +0.1599 | 0.1431 | ±0.2863 | +1.117 | 0.2639 |  |
| Hypertension | +0.6404 | 1.9566 | ±3.9132 | +0.327 | 0.7435 |  |
| High cholesterol | +2.1183 | 1.8105 | ±3.6211 | +1.170 | 0.2420 |  |
| Kidney disease | -1.7988 | 1.9680 | ±3.9360 | -0.914 | 0.3607 |  |
| Circulatory disease | +1.0450 | 2.0359 | ±4.0718 | +0.513 | 0.6078 |  |
| Time in range 70-180, pooled (%) | +0.0560 | 0.0322 | ±0.0644 | +1.741 | 0.0818 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **542**, R² = **0.0748**, Adj R² = **0.0502**, F-statistic = **3.04** (p = **1.51e-04**), Residual SE = **17.794** on **527** df, AIC = **4673.6**, BIC = **4738.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.3001** | 9.5342 | ±19.0684 | **+12.932** | **2.95e-38** | *** |
| Education: graduate level (vs college) | -0.7840 | 1.5827 | ±3.1654 | -0.495 | 0.6203 |  |
| **Education: high school or below (vs college)** | **+6.3979** | 2.5515 | ±5.1031 | **+2.507** | **0.0122** | * |
| Site: UCSD (vs UAB) | +3.2141 | 2.1077 | ±4.2154 | +1.525 | 0.1273 |  |
| Site: UW (vs UAB) | -1.9865 | 1.7410 | ±3.4819 | -1.141 | 0.2539 |  |
| Season: spring (vs autumn) | +3.5384 | 1.8751 | ±3.7502 | +1.887 | 0.0592 | . |
| **Season: summer (vs autumn)** | **+4.8454** | 1.9658 | ±3.9315 | **+2.465** | **0.0137** | * |
| **Season: winter (vs autumn)** | **+6.8233** | 2.4750 | ±4.9500 | **+2.757** | **0.0058** | ** |
| Age (years) | -0.1714 | 0.0970 | ±0.1941 | -1.766 | 0.0774 | . |
| BMI (kg/m2) | +0.1617 | 0.1429 | ±0.2858 | +1.132 | 0.2577 |  |
| Hypertension | +0.6314 | 1.9561 | ±3.9122 | +0.323 | 0.7469 |  |
| High cholesterol | +2.1138 | 1.8089 | ±3.6178 | +1.169 | 0.2426 |  |
| Kidney disease | -1.7647 | 1.9649 | ±3.9299 | -0.898 | 0.3691 |  |
| Circulatory disease | +1.0559 | 2.0358 | ±4.0715 | +0.519 | 0.6040 |  |
| Avg. daily time in range 70-180 (%) | +0.0589 | 0.0320 | ±0.0640 | +1.843 | 0.0654 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.0685**, Adj R² = **0.0438**, F-statistic = **2.77** (p = **5.53e-04**), Residual SE = **17.855** on **527** df, AIC = **4677.3**, BIC = **4741.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.9144** | 9.0365 | ±18.0730 | **+14.045** | **8.31e-45** | *** |
| Education: graduate level (vs college) | -0.6589 | 1.6030 | ±3.2060 | -0.411 | 0.6811 |  |
| **Education: high school or below (vs college)** | **+5.9868** | 2.5429 | ±5.0858 | **+2.354** | **0.0186** | * |
| Site: UCSD (vs UAB) | +3.6596 | 2.0856 | ±4.1713 | +1.755 | 0.0793 | . |
| Site: UW (vs UAB) | -1.6458 | 1.7260 | ±3.4520 | -0.954 | 0.3403 |  |
| Season: spring (vs autumn) | +3.3813 | 1.8907 | ±3.7815 | +1.788 | 0.0737 | . |
| **Season: summer (vs autumn)** | **+5.0174** | 1.9569 | ±3.9139 | **+2.564** | **0.0104** | * |
| **Season: winter (vs autumn)** | **+6.6152** | 2.5593 | ±5.1186 | **+2.585** | **0.0097** | ** |
| Age (years) | -0.1627 | 0.0939 | ±0.1878 | -1.732 | 0.0832 | . |
| BMI (kg/m2) | +0.1397 | 0.1439 | ±0.2878 | +0.971 | 0.3317 |  |
| Hypertension | +0.6125 | 1.9706 | ±3.9413 | +0.311 | 0.7560 |  |
| High cholesterol | +2.3373 | 1.8347 | ±3.6694 | +1.274 | 0.2027 |  |
| Kidney disease | -2.0031 | 1.9641 | ±3.9282 | -1.020 | 0.3078 |  |
| Circulatory disease | +0.8199 | 2.0347 | ±4.0693 | +0.403 | 0.6870 |  |
| Any reading < 54 during wear (0/1) | +0.7789 | 2.2245 | ±4.4491 | +0.350 | 0.7262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.0683**, Adj R² = **0.0436**, F-statistic = **2.76** (p = **5.74e-04**), Residual SE = **17.857** on **527** df, AIC = **4677.4**, BIC = **4741.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.1421** | 9.3470 | ±18.6940 | **+13.602** | **3.87e-42** | *** |
| Education: graduate level (vs college) | -0.6430 | 1.5999 | ±3.1998 | -0.402 | 0.6878 |  |
| **Education: high school or below (vs college)** | **+5.9964** | 2.5406 | ±5.0812 | **+2.360** | **0.0183** | * |
| Site: UCSD (vs UAB) | +3.6514 | 2.0957 | ±4.1914 | +1.742 | 0.0815 | . |
| Site: UW (vs UAB) | -1.6371 | 1.7543 | ±3.5086 | -0.933 | 0.3507 |  |
| Season: spring (vs autumn) | +3.4110 | 1.8887 | ±3.7773 | +1.806 | 0.0709 | . |
| **Season: summer (vs autumn)** | **+5.0306** | 1.9686 | ±3.9373 | **+2.555** | **0.0106** | * |
| **Season: winter (vs autumn)** | **+6.5941** | 2.5397 | ±5.0794 | **+2.596** | **0.0094** | ** |
| Age (years) | -0.1651 | 0.0961 | ±0.1922 | -1.718 | 0.0858 | . |
| BMI (kg/m2) | +0.1398 | 0.1438 | ±0.2875 | +0.972 | 0.3309 |  |
| Hypertension | +0.6334 | 1.9743 | ±3.9487 | +0.321 | 0.7484 |  |
| High cholesterol | +2.3244 | 1.8236 | ±3.6471 | +1.275 | 0.2024 |  |
| Kidney disease | -1.9950 | 1.9632 | ±3.9263 | -1.016 | 0.3095 |  |
| Circulatory disease | +0.9028 | 2.0477 | ±4.0955 | +0.441 | 0.6593 |  |
| Time < 54 (%) | +0.7908 | 2.6356 | ±5.2712 | +0.300 | 0.7641 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **542**, R² = **0.0682**, Adj R² = **0.0435**, F-statistic = **2.76** (p = **5.87e-04**), Residual SE = **17.858** on **527** df, AIC = **4677.5**, BIC = **4741.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.2133** | 9.3637 | ±18.7273 | **+13.586** | **4.86e-42** | *** |
| Education: graduate level (vs college) | -0.6573 | 1.5993 | ±3.1987 | -0.411 | 0.6811 |  |
| **Education: high school or below (vs college)** | **+5.9760** | 2.5465 | ±5.0931 | **+2.347** | **0.0189** | * |
| Site: UCSD (vs UAB) | +3.6151 | 2.0881 | ±4.1761 | +1.731 | 0.0834 | . |
| Site: UW (vs UAB) | -1.6832 | 1.7553 | ±3.5106 | -0.959 | 0.3376 |  |
| Season: spring (vs autumn) | +3.4008 | 1.8899 | ±3.7799 | +1.799 | 0.0719 | . |
| **Season: summer (vs autumn)** | **+5.0109** | 1.9749 | ±3.9498 | **+2.537** | **0.0112** | * |
| **Season: winter (vs autumn)** | **+6.5646** | 2.5371 | ±5.0742 | **+2.587** | **0.0097** | ** |
| Age (years) | -0.1648 | 0.0960 | ±0.1919 | -1.717 | 0.0859 | . |
| BMI (kg/m2) | +0.1398 | 0.1438 | ±0.2876 | +0.972 | 0.3310 |  |
| Hypertension | +0.6765 | 1.9756 | ±3.9513 | +0.342 | 0.7320 |  |
| High cholesterol | +2.2924 | 1.8250 | ±3.6501 | +1.256 | 0.2091 |  |
| Kidney disease | -1.9889 | 1.9647 | ±3.9293 | -1.012 | 0.3114 |  |
| Circulatory disease | +0.8732 | 2.0423 | ±4.0845 | +0.428 | 0.6690 |  |
| Avg. daily time < 54 (%) | +0.1231 | 1.5991 | ±3.1983 | +0.077 | 0.9386 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **542**, R² = **0.0684**, Adj R² = **0.0436**, F-statistic = **2.76** (p = **5.70e-04**), Residual SE = **17.856** on **527** df, AIC = **4677.4**, BIC = **4741.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.0942** | 9.3288 | ±18.6577 | **+13.624** | **2.89e-42** | *** |
| Education: graduate level (vs college) | -0.6454 | 1.6069 | ±3.2137 | -0.402 | 0.6880 |  |
| **Education: high school or below (vs college)** | **+5.9740** | 2.5470 | ±5.0940 | **+2.346** | **0.0190** | * |
| Site: UCSD (vs UAB) | +3.6663 | 2.0927 | ±4.1855 | +1.752 | 0.0798 | . |
| Site: UW (vs UAB) | -1.6377 | 1.7576 | ±3.5151 | -0.932 | 0.3514 |  |
| Season: spring (vs autumn) | +3.4368 | 1.8749 | ±3.7497 | +1.833 | 0.0668 | . |
| **Season: summer (vs autumn)** | **+5.0436** | 1.9498 | ±3.8997 | **+2.587** | **0.0097** | ** |
| **Season: winter (vs autumn)** | **+6.6001** | 2.5163 | ±5.0327 | **+2.623** | **0.0087** | ** |
| Age (years) | -0.1656 | 0.0964 | ±0.1928 | -1.718 | 0.0858 | . |
| BMI (kg/m2) | +0.1410 | 0.1431 | ±0.2863 | +0.985 | 0.3244 |  |
| Hypertension | +0.6378 | 1.9629 | ±3.9257 | +0.325 | 0.7452 |  |
| High cholesterol | +2.3321 | 1.8347 | ±3.6693 | +1.271 | 0.2037 |  |
| Kidney disease | -2.0124 | 1.9653 | ±3.9305 | -1.024 | 0.3058 |  |
| Circulatory disease | +0.8963 | 2.0453 | ±4.0906 | +0.438 | 0.6612 |  |
| Time 54-69, pooled (%) | +0.2506 | 0.8006 | ±1.6012 | +0.313 | 0.7543 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **542**, R² = **0.0682**, Adj R² = **0.0435**, F-statistic = **2.76** (p = **5.86e-04**), Residual SE = **17.858** on **527** df, AIC = **4677.5**, BIC = **4741.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.2509** | 9.3386 | ±18.6771 | **+13.626** | **2.79e-42** | *** |
| Education: graduate level (vs college) | -0.6648 | 1.6060 | ±3.2119 | -0.414 | 0.6789 |  |
| **Education: high school or below (vs college)** | **+5.9693** | 2.5484 | ±5.0968 | **+2.342** | **0.0192** | * |
| Site: UCSD (vs UAB) | +3.5933 | 2.0922 | ±4.1844 | +1.717 | 0.0859 | . |
| Site: UW (vs UAB) | -1.7077 | 1.7589 | ±3.5178 | -0.971 | 0.3316 |  |
| Season: spring (vs autumn) | +3.3790 | 1.8737 | ±3.7475 | +1.803 | 0.0713 | . |
| **Season: summer (vs autumn)** | **+4.9907** | 1.9499 | ±3.8999 | **+2.559** | **0.0105** | * |
| **Season: winter (vs autumn)** | **+6.5449** | 2.5199 | ±5.0398 | **+2.597** | **0.0094** | ** |
| Age (years) | -0.1645 | 0.0965 | ±0.1930 | -1.705 | 0.0883 | . |
| BMI (kg/m2) | +0.1398 | 0.1433 | ±0.2867 | +0.975 | 0.3296 |  |
| Hypertension | +0.6953 | 1.9654 | ±3.9308 | +0.354 | 0.7235 |  |
| High cholesterol | +2.2731 | 1.8381 | ±3.6762 | +1.237 | 0.2162 |  |
| Kidney disease | -1.9793 | 1.9627 | ±3.9253 | -1.008 | 0.3132 |  |
| Circulatory disease | +0.8606 | 2.0449 | ±4.0898 | +0.421 | 0.6739 |  |
| Avg. daily time 54-69 (%) | -0.0593 | 0.7153 | ±1.4307 | -0.083 | 0.9340 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **542**, R² = **0.0684**, Adj R² = **0.0436**, F-statistic = **2.76** (p = **5.68e-04**), Residual SE = **17.856** on **527** df, AIC = **4677.4**, BIC = **4741.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.0851** | 9.3240 | ±18.6480 | **+13.630** | **2.66e-42** | *** |
| Education: graduate level (vs college) | -0.6422 | 1.6063 | ±3.2125 | -0.400 | 0.6893 |  |
| **Education: high school or below (vs college)** | **+5.9808** | 2.5453 | ±5.0906 | **+2.350** | **0.0188** | * |
| Site: UCSD (vs UAB) | +3.6721 | 2.0952 | ±4.1903 | +1.753 | 0.0797 | . |
| Site: UW (vs UAB) | -1.6282 | 1.7576 | ±3.5152 | -0.926 | 0.3542 |  |
| Season: spring (vs autumn) | +3.4374 | 1.8788 | ±3.7576 | +1.830 | 0.0673 | . |
| **Season: summer (vs autumn)** | **+5.0471** | 1.9534 | ±3.9067 | **+2.584** | **0.0098** | ** |
| **Season: winter (vs autumn)** | **+6.6060** | 2.5199 | ±5.0398 | **+2.622** | **0.0088** | ** |
| Age (years) | -0.1656 | 0.0964 | ±0.1928 | -1.718 | 0.0858 | . |
| BMI (kg/m2) | +0.1409 | 0.1432 | ±0.2864 | +0.984 | 0.3252 |  |
| Hypertension | +0.6288 | 1.9646 | ±3.9292 | +0.320 | 0.7489 |  |
| High cholesterol | +2.3379 | 1.8346 | ±3.6692 | +1.274 | 0.2025 |  |
| Kidney disease | -2.0121 | 1.9663 | ±3.9326 | -1.023 | 0.3062 |  |
| Circulatory disease | +0.9029 | 2.0461 | ±4.0923 | +0.441 | 0.6590 |  |
| Time < 70 (%) | +0.2226 | 0.6548 | ±1.3097 | +0.340 | 0.7339 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **542**, R² = **0.0682**, Adj R² = **0.0435**, F-statistic = **2.76** (p = **5.87e-04**), Residual SE = **17.858** on **527** df, AIC = **4677.5**, BIC = **4741.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.2409** | 9.3397 | ±18.6795 | **+13.624** | **2.90e-42** | *** |
| Education: graduate level (vs college) | -0.6627 | 1.6045 | ±3.2091 | -0.413 | 0.6796 |  |
| **Education: high school or below (vs college)** | **+5.9692** | 2.5477 | ±5.0954 | **+2.343** | **0.0191** | * |
| Site: UCSD (vs UAB) | +3.5996 | 2.0920 | ±4.1840 | +1.721 | 0.0853 | . |
| Site: UW (vs UAB) | -1.7015 | 1.7586 | ±3.5171 | -0.968 | 0.3333 |  |
| Season: spring (vs autumn) | +3.3832 | 1.8765 | ±3.7530 | +1.803 | 0.0714 | . |
| **Season: summer (vs autumn)** | **+4.9942** | 1.9545 | ±3.9089 | **+2.555** | **0.0106** | * |
| **Season: winter (vs autumn)** | **+6.5487** | 2.5222 | ±5.0443 | **+2.596** | **0.0094** | ** |
| Age (years) | -0.1646 | 0.0964 | ±0.1927 | -1.708 | 0.0876 | . |
| BMI (kg/m2) | +0.1399 | 0.1435 | ±0.2869 | +0.975 | 0.3296 |  |
| Hypertension | +0.6904 | 1.9689 | ±3.9378 | +0.351 | 0.7258 |  |
| High cholesterol | +2.2782 | 1.8368 | ±3.6736 | +1.240 | 0.2148 |  |
| Kidney disease | -1.9818 | 1.9636 | ±3.9273 | -1.009 | 0.3129 |  |
| Circulatory disease | +0.8640 | 2.0446 | ±4.0892 | +0.423 | 0.6726 |  |
| Avg. daily time < 70 (%) | -0.0267 | 0.5009 | ±1.0018 | -0.053 | 0.9575 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.0761**, Adj R² = **0.0516**, F-statistic = **3.10** (p = **1.16e-04**), Residual SE = **17.782** on **527** df, AIC = **4672.9**, BIC = **4737.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+119.8760** | 9.6513 | ±19.3027 | **+12.421** | **2.02e-35** | *** |
| Education: graduate level (vs college) | -0.9648 | 1.5949 | ±3.1899 | -0.605 | 0.5453 |  |
| **Education: high school or below (vs college)** | **+6.3524** | 2.5440 | ±5.0881 | **+2.497** | **0.0125** | * |
| Site: UCSD (vs UAB) | +3.2807 | 2.1145 | ±4.2290 | +1.552 | 0.1208 |  |
| Site: UW (vs UAB) | -2.1256 | 1.7719 | ±3.5438 | -1.200 | 0.2303 |  |
| Season: spring (vs autumn) | +3.3809 | 1.8938 | ±3.7875 | +1.785 | 0.0742 | . |
| **Season: summer (vs autumn)** | **+4.5853** | 1.9985 | ±3.9969 | **+2.294** | **0.0218** | * |
| **Season: winter (vs autumn)** | **+6.6156** | 2.5057 | ±5.0114 | **+2.640** | **0.0083** | ** |
| Age (years) | -0.1807 | 0.0972 | ±0.1945 | -1.859 | 0.0630 | . |
| BMI (kg/m2) | +0.1529 | 0.1420 | ±0.2840 | +1.077 | 0.2817 |  |
| Hypertension | +0.8398 | 1.9506 | ±3.9013 | +0.431 | 0.6668 |  |
| High cholesterol | +2.1608 | 1.7991 | ±3.5981 | +1.201 | 0.2297 |  |
| Kidney disease | -1.7775 | 1.9531 | ±3.9063 | -0.910 | 0.3628 |  |
| Circulatory disease | +1.0206 | 2.0325 | ±4.0650 | +0.502 | 0.6156 |  |
| **Time 54-250, pooled (%)** | **+0.0918** | 0.0468 | ±0.0937 | **+1.960** | **0.0500** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **542**, R² = **0.0769**, Adj R² = **0.0523**, F-statistic = **3.13** (p = **9.82e-05**), Residual SE = **17.775** on **527** df, AIC = **4672.4**, BIC = **4736.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+119.2812** | 9.6541 | ±19.3081 | **+12.356** | **4.55e-35** | *** |
| Education: graduate level (vs college) | -0.9763 | 1.5952 | ±3.1905 | -0.612 | 0.5405 |  |
| **Education: high school or below (vs college)** | **+6.3691** | 2.5393 | ±5.0785 | **+2.508** | **0.0121** | * |
| Site: UCSD (vs UAB) | +3.2579 | 2.1138 | ±4.2276 | +1.541 | 0.1233 |  |
| Site: UW (vs UAB) | -2.1319 | 1.7688 | ±3.5376 | -1.205 | 0.2281 |  |
| Season: spring (vs autumn) | +3.3992 | 1.8933 | ±3.7866 | +1.795 | 0.0726 | . |
| **Season: summer (vs autumn)** | **+4.5952** | 1.9947 | ±3.9895 | **+2.304** | **0.0212** | * |
| **Season: winter (vs autumn)** | **+6.6390** | 2.5033 | ±5.0066 | **+2.652** | **0.0080** | ** |
| Age (years) | -0.1797 | 0.0971 | ±0.1943 | -1.850 | 0.0643 | . |
| BMI (kg/m2) | +0.1539 | 0.1416 | ±0.2832 | +1.087 | 0.2771 |  |
| Hypertension | +0.8346 | 1.9510 | ±3.9019 | +0.428 | 0.6688 |  |
| High cholesterol | +2.1552 | 1.7985 | ±3.5969 | +1.198 | 0.2308 |  |
| Kidney disease | -1.7382 | 1.9498 | ±3.8996 | -0.891 | 0.3727 |  |
| Circulatory disease | +1.0438 | 2.0346 | ±4.0692 | +0.513 | 0.6079 |  |
| **Avg. daily time 54-250 (%)** | **+0.0970** | 0.0480 | ±0.0961 | **+2.018** | **0.0435** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.0688**, Adj R² = **0.0441**, F-statistic = **2.78** (p = **5.18e-04**), Residual SE = **17.852** on **527** df, AIC = **4677.1**, BIC = **4741.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.6836** | 9.4537 | ±18.9074 | **+13.506** | **1.44e-41** | *** |
| Education: graduate level (vs college) | -0.6275 | 1.6160 | ±3.2319 | -0.388 | 0.6978 |  |
| **Education: high school or below (vs college)** | **+6.0571** | 2.5609 | ±5.1219 | **+2.365** | **0.0180** | * |
| Site: UCSD (vs UAB) | +3.5279 | 2.0807 | ±4.1614 | +1.696 | 0.0900 | . |
| Site: UW (vs UAB) | -1.6899 | 1.7550 | ±3.5099 | -0.963 | 0.3356 |  |
| Season: spring (vs autumn) | +3.4719 | 1.8747 | ±3.7494 | +1.852 | 0.0640 | . |
| **Season: summer (vs autumn)** | **+5.0535** | 1.9527 | ±3.9053 | **+2.588** | **0.0097** | ** |
| **Season: winter (vs autumn)** | **+6.6690** | 2.4539 | ±4.9079 | **+2.718** | **0.0066** | ** |
| Age (years) | -0.1631 | 0.0967 | ±0.1934 | -1.687 | 0.0916 | . |
| BMI (kg/m2) | +0.1469 | 0.1451 | ±0.2903 | +1.012 | 0.3115 |  |
| Hypertension | +0.5993 | 1.9280 | ±3.8560 | +0.311 | 0.7559 |  |
| High cholesterol | +2.2396 | 1.8360 | ±3.6720 | +1.220 | 0.2225 |  |
| Kidney disease | -1.9549 | 1.9730 | ±3.9461 | -0.991 | 0.3218 |  |
| Circulatory disease | +0.9195 | 2.0436 | ±4.0872 | +0.450 | 0.6528 |  |
| Time 181-250, pooled (%) | -0.0318 | 0.0642 | ±0.1284 | -0.495 | 0.6208 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **542**, R² = **0.0690**, Adj R² = **0.0443**, F-statistic = **2.79** (p = **5.00e-04**), Residual SE = **17.850** on **527** df, AIC = **4677.0**, BIC = **4741.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.7537** | 9.4520 | ±18.9040 | **+13.516** | **1.26e-41** | *** |
| Education: graduate level (vs college) | -0.6164 | 1.6179 | ±3.2359 | -0.381 | 0.7032 |  |
| **Education: high school or below (vs college)** | **+6.0827** | 2.5620 | ±5.1241 | **+2.374** | **0.0176** | * |
| Site: UCSD (vs UAB) | +3.5080 | 2.0844 | ±4.1688 | +1.683 | 0.0924 | . |
| Site: UW (vs UAB) | -1.6997 | 1.7511 | ±3.5023 | -0.971 | 0.3317 |  |
| Season: spring (vs autumn) | +3.4828 | 1.8742 | ±3.7484 | +1.858 | 0.0631 | . |
| **Season: summer (vs autumn)** | **+5.0617** | 1.9531 | ±3.9061 | **+2.592** | **0.0096** | ** |
| **Season: winter (vs autumn)** | **+6.6916** | 2.4506 | ±4.9011 | **+2.731** | **0.0063** | ** |
| Age (years) | -0.1634 | 0.0967 | ±0.1934 | -1.690 | 0.0910 | . |
| BMI (kg/m2) | +0.1480 | 0.1454 | ±0.2907 | +1.018 | 0.3087 |  |
| Hypertension | +0.5905 | 1.9321 | ±3.8641 | +0.306 | 0.7599 |  |
| High cholesterol | +2.2372 | 1.8320 | ±3.6641 | +1.221 | 0.2220 |  |
| Kidney disease | -1.9467 | 1.9737 | ±3.9473 | -0.986 | 0.3240 |  |
| Circulatory disease | +0.9217 | 2.0409 | ±4.0818 | +0.452 | 0.6515 |  |
| Avg. daily time 181-250 (%) | -0.0353 | 0.0614 | ±0.1228 | -0.574 | 0.5657 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **542**, R² = **0.0741**, Adj R² = **0.0495**, F-statistic = **3.01** (p = **1.76e-04**), Residual SE = **17.801** on **527** df, AIC = **4674.1**, BIC = **4738.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.1263** | 9.5501 | ±19.1001 | **+13.521** | **1.18e-41** | *** |
| Education: graduate level (vs college) | -0.7865 | 1.5822 | ±3.1645 | -0.497 | 0.6191 |  |
| **Education: high school or below (vs college)** | **+6.3544** | 2.5539 | ±5.1078 | **+2.488** | **0.0128** | * |
| Site: UCSD (vs UAB) | +3.2730 | 2.1037 | ±4.2074 | +1.556 | 0.1197 |  |
| Site: UW (vs UAB) | -1.9462 | 1.7415 | ±3.4830 | -1.118 | 0.2638 |  |
| Season: spring (vs autumn) | +3.5285 | 1.8758 | ±3.7517 | +1.881 | 0.0600 | . |
| **Season: summer (vs autumn)** | **+4.8432** | 1.9686 | ±3.9372 | **+2.460** | **0.0139** | * |
| **Season: winter (vs autumn)** | **+6.7934** | 2.4783 | ±4.9565 | **+2.741** | **0.0061** | ** |
| Age (years) | -0.1716 | 0.0971 | ±0.1941 | -1.768 | 0.0770 | . |
| BMI (kg/m2) | +0.1600 | 0.1431 | ±0.2862 | +1.118 | 0.2635 |  |
| Hypertension | +0.6270 | 1.9560 | ±3.9119 | +0.321 | 0.7485 |  |
| High cholesterol | +2.1328 | 1.8100 | ±3.6201 | +1.178 | 0.2387 |  |
| Kidney disease | -1.8071 | 1.9673 | ±3.9347 | -0.919 | 0.3583 |  |
| Circulatory disease | +1.0521 | 2.0357 | ±4.0714 | +0.517 | 0.6053 |  |
| Time > 180 (%) | -0.0556 | 0.0319 | ±0.0639 | -1.740 | 0.0819 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **542**, R² = **0.0747**, Adj R² = **0.0501**, F-statistic = **3.04** (p = **1.54e-04**), Residual SE = **17.795** on **527** df, AIC = **4673.7**, BIC = **4738.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.1372** | 9.5468 | ±19.0936 | **+13.527** | **1.09e-41** | *** |
| Education: graduate level (vs college) | -0.7764 | 1.5835 | ±3.1671 | -0.490 | 0.6239 |  |
| **Education: high school or below (vs college)** | **+6.3959** | 2.5515 | ±5.1029 | **+2.507** | **0.0122** | * |
| Site: UCSD (vs UAB) | +3.2373 | 2.1057 | ±4.2115 | +1.537 | 0.1242 |  |
| Site: UW (vs UAB) | -1.9631 | 1.7413 | ±3.4826 | -1.127 | 0.2596 |  |
| Season: spring (vs autumn) | +3.5524 | 1.8751 | ±3.7501 | +1.895 | 0.0582 | . |
| **Season: summer (vs autumn)** | **+4.8624** | 1.9649 | ±3.9297 | **+2.475** | **0.0133** | * |
| **Season: winter (vs autumn)** | **+6.8342** | 2.4730 | ±4.9460 | **+2.763** | **0.0057** | ** |
| Age (years) | -0.1716 | 0.0971 | ±0.1942 | -1.767 | 0.0772 | . |
| BMI (kg/m2) | +0.1615 | 0.1429 | ±0.2857 | +1.131 | 0.2582 |  |
| Hypertension | +0.6173 | 1.9556 | ±3.9112 | +0.316 | 0.7523 |  |
| High cholesterol | +2.1315 | 1.8086 | ±3.6171 | +1.179 | 0.2386 |  |
| Kidney disease | -1.7754 | 1.9644 | ±3.9289 | -0.904 | 0.3661 |  |
| Circulatory disease | +1.0633 | 2.0356 | ±4.0712 | +0.522 | 0.6014 |  |
| Avg. daily time > 180 (%) | -0.0581 | 0.0318 | ±0.0636 | -1.829 | 0.0674 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **542**, R² = **0.0703**, Adj R² = **0.0456**, F-statistic = **2.84** (p = **3.88e-04**), Residual SE = **17.838** on **527** df, AIC = **4676.3**, BIC = **4740.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.0676** | 9.5606 | ±19.1212 | **+13.395** | **6.44e-41** | *** |
| Education: graduate level (vs college) | -0.7986 | 1.5748 | ±3.1496 | -0.507 | 0.6121 |  |
| **Education: high school or below (vs college)** | **+6.1578** | 2.5498 | ±5.0996 | **+2.415** | **0.0157** | * |
| Site: UCSD (vs UAB) | +3.3852 | 2.1157 | ±4.2314 | +1.600 | 0.1096 |  |
| Site: UW (vs UAB) | -1.7902 | 1.7396 | ±3.4791 | -1.029 | 0.3034 |  |
| Season: spring (vs autumn) | +3.4782 | 1.8740 | ±3.7479 | +1.856 | 0.0634 | . |
| **Season: summer (vs autumn)** | **+4.8970** | 1.9764 | ±3.9527 | **+2.478** | **0.0132** | * |
| **Season: winter (vs autumn)** | **+6.6923** | 2.4806 | ±4.9613 | **+2.698** | **0.0070** | ** |
| Age (years) | -0.1720 | 0.0978 | ±0.1957 | -1.758 | 0.0788 | . |
| BMI (kg/m2) | +0.1578 | 0.1435 | ±0.2869 | +1.100 | 0.2714 |  |
| Hypertension | +0.6473 | 1.9645 | ±3.9289 | +0.329 | 0.7418 |  |
| High cholesterol | +2.1753 | 1.8146 | ±3.6292 | +1.199 | 0.2306 |  |
| Kidney disease | -1.9022 | 1.9718 | ±3.9435 | -0.965 | 0.3347 |  |
| Circulatory disease | +0.9832 | 2.0291 | ±4.0583 | +0.485 | 0.6280 |  |
| Nocturnal time > 180 (%) | -0.0291 | 0.0318 | ±0.0636 | -0.914 | 0.3610 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **542**, R² = **0.0761**, Adj R² = **0.0516**, F-statistic = **3.10** (p = **1.15e-04**), Residual SE = **17.782** on **527** df, AIC = **4672.9**, BIC = **4737.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.0457** | 9.4915 | ±18.9830 | **+13.596** | **4.23e-42** | *** |
| Education: graduate level (vs college) | -0.9630 | 1.5951 | ±3.1902 | -0.604 | 0.5460 |  |
| **Education: high school or below (vs college)** | **+6.3557** | 2.5438 | ±5.0876 | **+2.498** | **0.0125** | * |
| Site: UCSD (vs UAB) | +3.2855 | 2.1139 | ±4.2277 | +1.554 | 0.1201 |  |
| Site: UW (vs UAB) | -2.1196 | 1.7714 | ±3.5429 | -1.197 | 0.2315 |  |
| Season: spring (vs autumn) | +3.3833 | 1.8938 | ±3.7876 | +1.787 | 0.0740 | . |
| **Season: summer (vs autumn)** | **+4.5884** | 1.9979 | ±3.9957 | **+2.297** | **0.0216** | * |
| **Season: winter (vs autumn)** | **+6.6202** | 2.5055 | ±5.0110 | **+2.642** | **0.0082** | ** |
| Age (years) | -0.1808 | 0.0972 | ±0.1945 | -1.859 | 0.0630 | . |
| BMI (kg/m2) | +0.1529 | 0.1420 | ±0.2839 | +1.077 | 0.2816 |  |
| Hypertension | +0.8341 | 1.9507 | ±3.9015 | +0.428 | 0.6690 |  |
| High cholesterol | +2.1652 | 1.7993 | ±3.5986 | +1.203 | 0.2288 |  |
| Kidney disease | -1.7785 | 1.9529 | ±3.9058 | -0.911 | 0.3625 |  |
| Circulatory disease | +1.0247 | 2.0324 | ±4.0648 | +0.504 | 0.6141 |  |
| **Time > 250 (%)** | **-0.0919** | 0.0469 | ±0.0937 | **-1.961** | **0.0499** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 542)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **542**, R² = **0.0769**, Adj R² = **0.0524**, F-statistic = **3.13** (p = **9.81e-05**), Residual SE = **17.775** on **527** df, AIC = **4672.4**, BIC = **4736.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.9670** | 9.4775 | ±18.9550 | **+13.608** | **3.60e-42** | *** |
| Education: graduate level (vs college) | -0.9742 | 1.5953 | ±3.1906 | -0.611 | 0.5414 |  |
| **Education: high school or below (vs college)** | **+6.3731** | 2.5393 | ±5.0785 | **+2.510** | **0.0121** | * |
| Site: UCSD (vs UAB) | +3.2637 | 2.1131 | ±4.2262 | +1.544 | 0.1225 |  |
| Site: UW (vs UAB) | -2.1245 | 1.7682 | ±3.5364 | -1.201 | 0.2296 |  |
| Season: spring (vs autumn) | +3.4073 | 1.8932 | ±3.7863 | +1.800 | 0.0719 | . |
| **Season: summer (vs autumn)** | **+4.6029** | 1.9936 | ±3.9873 | **+2.309** | **0.0210** | * |
| **Season: winter (vs autumn)** | **+6.6462** | 2.5031 | ±5.0062 | **+2.655** | **0.0079** | ** |
| Age (years) | -0.1798 | 0.0972 | ±0.1943 | -1.850 | 0.0643 | . |
| BMI (kg/m2) | +0.1538 | 0.1416 | ±0.2832 | +1.086 | 0.2774 |  |
| Hypertension | +0.8290 | 1.9510 | ±3.9019 | +0.425 | 0.6709 |  |
| High cholesterol | +2.1608 | 1.7988 | ±3.5976 | +1.201 | 0.2296 |  |
| Kidney disease | -1.7411 | 1.9496 | ±3.8991 | -0.893 | 0.3718 |  |
| Circulatory disease | +1.0474 | 2.0345 | ±4.0691 | +0.515 | 0.6067 |  |
| **Avg. daily time > 250 (%)** | **-0.0970** | 0.0481 | ±0.0962 | **-2.017** | **0.0437** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Non-healthy group (T2D non-insulin + T2D insulin) - Home environment

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 120 single-predictor tests; 12 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 120 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family and 1 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 542): best single predictor out of sample is **SD of daily means** (CV R² 0.166 vs 0.147 for covariates alone, gain +0.019; +0.142 per SD, p = 0.001, q = 0.109). No association survives FDR; nominal only: SD of daily means (p = 0.001), Nocturnal mean (p = 0.013), HbA1c (p = 0.016), %>180 nocturnal (p = 0.029).
- **Indoor temperature, mean (deg C)** (n = 542): best single predictor out of sample is **%<54 (pooled)** (CV R² 0.221 vs 0.222 for covariates alone, gain -0.001; -0.0439 per SD, p = 0.545, q = 0.800). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 542): best single predictor out of sample is **Mean glucose** (CV R² 0.193 vs 0.193 for covariates alone, gain +0.000; +0.304 per SD, p = 0.278, q = 0.537). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor VOC index, mean** (n = 542): best single predictor out of sample is **HbA1c** (CV R² -0.012 vs -0.018 for covariates alone, gain +0.007; -1.88 per SD, p = 0.027, q = 0.311). No association survives FDR; nominal only: HbA1c (p = 0.027), %54-250 (daily avg) (p = 0.044), %>250 (daily avg) (p = 0.044), %>250 (pooled) (p = 0.050).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Indoor PM2.5, log(1 + mean ug/m3) (+0.019, via SD of daily means); Indoor VOC index, mean (+0.007, via HbA1c); Indoor relative humidity, mean (%) (+0.000, via Mean glucose); Indoor temperature, mean (deg C) (-0.001, via %<54 (pooled)). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** HbA1c (0 FDR-significant / 2 raw-significant of 4); Range 70-180 (0 FDR-significant / 2 raw-significant of 8); Band 54-250 (0 FDR-significant / 2 raw-significant of 8).
Level metrics: 0 FDR-significant (1 raw); variability metrics: 0 FDR-significant (1 raw); HbA1c alone: 0 FDR-significant (2 raw) across the outcomes in this file.

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
