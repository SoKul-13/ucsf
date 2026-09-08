# Phase 6b model output tables - Near-normal substitute: >= 99% of readings within 70-180 - Total analysis base - Home environment

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 443; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **443**, R² = **0.1362**, Adj R² = **0.1101**, F-statistic = **5.21** (p = **1.17e-08**), Residual SE = **0.854** on **429** df, AIC = **1130.8**, BIC = **1188.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7378** | 0.2737 | ±0.5474 | **+6.349** | **2.16e-10** | *** |
| Education: graduate level (vs college) | -0.1039 | 0.0874 | ±0.1747 | -1.189 | 0.2344 |  |
| Education: high school or below (vs college) | +0.3335 | 0.1766 | ±0.3532 | +1.888 | 0.0590 | . |
| Site: UCSD (vs UAB) | +0.0536 | 0.1065 | ±0.2129 | +0.504 | 0.6143 |  |
| **Site: UW (vs UAB)** | **-0.3188** | 0.1156 | ±0.2313 | **-2.757** | **0.0058** | ** |
| Season: spring (vs autumn) | -0.1062 | 0.1119 | ±0.2238 | -0.949 | 0.3426 |  |
| Season: summer (vs autumn) | +0.2150 | 0.1294 | ±0.2589 | +1.661 | 0.0968 | . |
| Season: winter (vs autumn) | -0.0103 | 0.1180 | ±0.2359 | -0.087 | 0.9305 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0070 | **-2.018** | **0.0436** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0132 | **+3.160** | **0.0016** | ** |
| Hypertension | +0.0847 | 0.0947 | ±0.1894 | +0.894 | 0.3711 |  |
| High cholesterol | -0.0542 | 0.0818 | ±0.1635 | -0.663 | 0.5075 |  |
| Kidney disease | -0.1076 | 0.1694 | ±0.3388 | -0.635 | 0.5254 |  |
| Circulatory disease | +0.2827 | 0.1624 | ±0.3247 | +1.741 | 0.0817 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **443**, R² = **0.1383**, Adj R² = **0.1101**, F-statistic = **4.91** (p = **1.81e-08**), Residual SE = **0.854** on **428** df, AIC = **1131.8**, BIC = **1193.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.9996 | 0.8884 | ±1.7768 | +1.125 | 0.2605 |  |
| Education: graduate level (vs college) | -0.1004 | 0.0875 | ±0.1749 | -1.149 | 0.2507 |  |
| Education: high school or below (vs college) | +0.3232 | 0.1771 | ±0.3541 | +1.826 | 0.0679 | . |
| Site: UCSD (vs UAB) | +0.0520 | 0.1069 | ±0.2138 | +0.486 | 0.6267 |  |
| **Site: UW (vs UAB)** | **-0.3170** | 0.1157 | ±0.2314 | **-2.739** | **0.0062** | ** |
| Season: spring (vs autumn) | -0.0878 | 0.1117 | ±0.2234 | -0.786 | 0.4317 |  |
| Season: summer (vs autumn) | +0.2080 | 0.1307 | ±0.2614 | +1.592 | 0.1114 |  |
| Season: winter (vs autumn) | -0.0036 | 0.1180 | ±0.2361 | -0.030 | 0.9760 |  |
| **Age (years)** | **-0.0075** | 0.0036 | ±0.0072 | **-2.083** | **0.0372** | * |
| **BMI (kg/m2)** | **+0.0202** | 0.0066 | ±0.0132 | **+3.051** | **0.0023** | ** |
| Hypertension | +0.0766 | 0.0958 | ±0.1916 | +0.799 | 0.4242 |  |
| High cholesterol | -0.0728 | 0.0840 | ±0.1679 | -0.867 | 0.3862 |  |
| Kidney disease | -0.0986 | 0.1728 | ±0.3455 | -0.571 | 0.5680 |  |
| Circulatory disease | +0.2902 | 0.1633 | ±0.3266 | +1.777 | 0.0756 | . |
| HbA1c (%) | +0.1418 | 0.1634 | ±0.3267 | +0.868 | 0.3856 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **443**, R² = **0.1403**, Adj R² = **0.1121**, F-statistic = **4.99** (p = **1.21e-08**), Residual SE = **0.853** on **428** df, AIC = **1130.8**, BIC = **1192.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.6155** | 0.7110 | ±1.4219 | **+3.679** | **2.34e-04** | *** |
| Education: graduate level (vs college) | -0.1021 | 0.0875 | ±0.1749 | -1.168 | 0.2428 |  |
| Education: high school or below (vs college) | +0.3258 | 0.1751 | ±0.3502 | +1.861 | 0.0627 | . |
| Site: UCSD (vs UAB) | +0.0607 | 0.1070 | ±0.2141 | +0.567 | 0.5705 |  |
| **Site: UW (vs UAB)** | **-0.3104** | 0.1158 | ±0.2317 | **-2.679** | **0.0074** | ** |
| Season: spring (vs autumn) | -0.1136 | 0.1119 | ±0.2238 | -1.015 | 0.3099 |  |
| Season: summer (vs autumn) | +0.2139 | 0.1290 | ±0.2579 | +1.659 | 0.0971 | . |
| Season: winter (vs autumn) | -0.0158 | 0.1182 | ±0.2365 | -0.134 | 0.8935 |  |
| **Age (years)** | **-0.0073** | 0.0036 | ±0.0071 | **-2.035** | **0.0418** | * |
| **BMI (kg/m2)** | **+0.0214** | 0.0066 | ±0.0132 | **+3.255** | **0.0011** | ** |
| Hypertension | +0.0923 | 0.0956 | ±0.1912 | +0.965 | 0.3344 |  |
| High cholesterol | -0.0589 | 0.0820 | ±0.1641 | -0.718 | 0.4725 |  |
| Kidney disease | -0.0995 | 0.1705 | ±0.3410 | -0.584 | 0.5595 |  |
| Circulatory disease | +0.2837 | 0.1626 | ±0.3252 | +1.745 | 0.0810 | . |
| Mean glucose (mg/dL) | -0.0077 | 0.0054 | ±0.0107 | -1.447 | 0.1478 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **443**, R² = **0.1403**, Adj R² = **0.1121**, F-statistic = **4.99** (p = **1.21e-08**), Residual SE = **0.853** on **428** df, AIC = **1130.8**, BIC = **1192.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6879** | 1.4243 | ±2.8487 | **+2.589** | **0.0096** | ** |
| Education: graduate level (vs college) | -0.1021 | 0.0875 | ±0.1749 | -1.168 | 0.2428 |  |
| Education: high school or below (vs college) | +0.3258 | 0.1751 | ±0.3502 | +1.861 | 0.0627 | . |
| Site: UCSD (vs UAB) | +0.0607 | 0.1070 | ±0.2141 | +0.567 | 0.5705 |  |
| **Site: UW (vs UAB)** | **-0.3104** | 0.1158 | ±0.2317 | **-2.679** | **0.0074** | ** |
| Season: spring (vs autumn) | -0.1136 | 0.1119 | ±0.2238 | -1.015 | 0.3099 |  |
| Season: summer (vs autumn) | +0.2139 | 0.1290 | ±0.2579 | +1.659 | 0.0971 | . |
| Season: winter (vs autumn) | -0.0158 | 0.1182 | ±0.2365 | -0.134 | 0.8935 |  |
| **Age (years)** | **-0.0073** | 0.0036 | ±0.0071 | **-2.035** | **0.0418** | * |
| **BMI (kg/m2)** | **+0.0214** | 0.0066 | ±0.0132 | **+3.255** | **0.0011** | ** |
| Hypertension | +0.0923 | 0.0956 | ±0.1912 | +0.965 | 0.3344 |  |
| High cholesterol | -0.0589 | 0.0820 | ±0.1641 | -0.718 | 0.4725 |  |
| Kidney disease | -0.0995 | 0.1705 | ±0.3410 | -0.584 | 0.5595 |  |
| Circulatory disease | +0.2837 | 0.1626 | ±0.3252 | +1.745 | 0.0810 | . |
| GMI (%) | -0.3240 | 0.2238 | ±0.4477 | -1.447 | 0.1478 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **443**, R² = **0.1378**, Adj R² = **0.1096**, F-statistic = **4.89** (p = **2.00e-08**), Residual SE = **0.854** on **428** df, AIC = **1132.0**, BIC = **1193.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1820** | 0.5934 | ±1.1868 | **+3.677** | **2.36e-04** | *** |
| Education: graduate level (vs college) | -0.1062 | 0.0880 | ±0.1760 | -1.207 | 0.2273 |  |
| Education: high school or below (vs college) | +0.3273 | 0.1767 | ±0.3533 | +1.853 | 0.0639 | . |
| Site: UCSD (vs UAB) | +0.0627 | 0.1084 | ±0.2168 | +0.579 | 0.5629 |  |
| **Site: UW (vs UAB)** | **-0.3107** | 0.1168 | ±0.2335 | **-2.661** | **0.0078** | ** |
| Season: spring (vs autumn) | -0.1094 | 0.1123 | ±0.2245 | -0.975 | 0.3298 |  |
| Season: summer (vs autumn) | +0.2150 | 0.1294 | ±0.2587 | +1.662 | 0.0965 | . |
| Season: winter (vs autumn) | -0.0120 | 0.1184 | ±0.2368 | -0.101 | 0.9196 |  |
| **Age (years)** | **-0.0076** | 0.0037 | ±0.0074 | **-2.062** | **0.0392** | * |
| **BMI (kg/m2)** | **+0.0217** | 0.0066 | ±0.0132 | **+3.300** | **9.68e-04** | *** |
| Hypertension | +0.0895 | 0.0958 | ±0.1916 | +0.934 | 0.3501 |  |
| High cholesterol | -0.0551 | 0.0820 | ±0.1641 | -0.671 | 0.5021 |  |
| Kidney disease | -0.1108 | 0.1695 | ±0.3390 | -0.654 | 0.5133 |  |
| Circulatory disease | +0.2814 | 0.1635 | ±0.3269 | +1.721 | 0.0852 | . |
| Nocturnal mean 00-06h (mg/dL) | -0.0039 | 0.0042 | ±0.0084 | -0.921 | 0.3573 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **443**, R² = **0.1364**, Adj R² = **0.1082**, F-statistic = **4.83** (p = **2.67e-08**), Residual SE = **0.855** on **428** df, AIC = **1132.7**, BIC = **1194.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8229** | 0.3992 | ±0.7984 | **+4.566** | **4.96e-06** | *** |
| Education: graduate level (vs college) | -0.1053 | 0.0881 | ±0.1762 | -1.196 | 0.2319 |  |
| Education: high school or below (vs college) | +0.3340 | 0.1767 | ±0.3534 | +1.891 | 0.0587 | . |
| Site: UCSD (vs UAB) | +0.0517 | 0.1066 | ±0.2132 | +0.485 | 0.6275 |  |
| **Site: UW (vs UAB)** | **-0.3208** | 0.1156 | ±0.2313 | **-2.775** | **0.0055** | ** |
| Season: spring (vs autumn) | -0.1047 | 0.1125 | ±0.2251 | -0.931 | 0.3521 |  |
| Season: summer (vs autumn) | +0.2154 | 0.1296 | ±0.2593 | +1.662 | 0.0966 | . |
| Season: winter (vs autumn) | -0.0082 | 0.1197 | ±0.2394 | -0.069 | 0.9453 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0071 | **-2.006** | **0.0449** | * |
| **BMI (kg/m2)** | **+0.0210** | 0.0066 | ±0.0132 | **+3.176** | **0.0015** | ** |
| Hypertension | +0.0865 | 0.0954 | ±0.1907 | +0.906 | 0.3647 |  |
| High cholesterol | -0.0557 | 0.0825 | ±0.1650 | -0.675 | 0.4995 |  |
| Kidney disease | -0.1030 | 0.1690 | ±0.3380 | -0.609 | 0.5422 |  |
| Circulatory disease | +0.2841 | 0.1626 | ±0.3253 | +1.747 | 0.0807 | . |
| Glucose SD, pooled (mg/dL) | -0.0053 | 0.0172 | ±0.0344 | -0.306 | 0.7593 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **443**, R² = **0.1363**, Adj R² = **0.1081**, F-statistic = **4.83** (p = **2.73e-08**), Residual SE = **0.855** on **428** df, AIC = **1132.8**, BIC = **1194.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7868** | 0.3712 | ±0.7424 | **+4.814** | **1.48e-06** | *** |
| Education: graduate level (vs college) | -0.1050 | 0.0884 | ±0.1767 | -1.189 | 0.2346 |  |
| Education: high school or below (vs college) | +0.3332 | 0.1766 | ±0.3532 | +1.887 | 0.0592 | . |
| Site: UCSD (vs UAB) | +0.0527 | 0.1067 | ±0.2134 | +0.494 | 0.6211 |  |
| **Site: UW (vs UAB)** | **-0.3199** | 0.1156 | ±0.2313 | **-2.766** | **0.0057** | ** |
| Season: spring (vs autumn) | -0.1056 | 0.1124 | ±0.2249 | -0.939 | 0.3477 |  |
| Season: summer (vs autumn) | +0.2150 | 0.1297 | ±0.2593 | +1.658 | 0.0973 | . |
| Season: winter (vs autumn) | -0.0097 | 0.1188 | ±0.2376 | -0.082 | 0.9347 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0071 | **-2.003** | **0.0452** | * |
| **BMI (kg/m2)** | **+0.0210** | 0.0066 | ±0.0132 | **+3.188** | **0.0014** | ** |
| Hypertension | +0.0854 | 0.0952 | ±0.1905 | +0.896 | 0.3700 |  |
| High cholesterol | -0.0551 | 0.0825 | ±0.1649 | -0.668 | 0.5044 |  |
| Kidney disease | -0.1047 | 0.1688 | ±0.3376 | -0.620 | 0.5352 |  |
| Circulatory disease | +0.2828 | 0.1628 | ±0.3256 | +1.737 | 0.0823 | . |
| Avg. daily SD (mg/dL) | -0.0034 | 0.0166 | ±0.0332 | -0.205 | 0.8373 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **443**, R² = **0.1365**, Adj R² = **0.1082**, F-statistic = **4.83** (p = **2.63e-08**), Residual SE = **0.855** on **428** df, AIC = **1132.7**, BIC = **1194.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6404** | 0.3798 | ±0.7597 | **+4.319** | **1.57e-05** | *** |
| Education: graduate level (vs college) | -0.1020 | 0.0879 | ±0.1759 | -1.160 | 0.2460 |  |
| Education: high school or below (vs college) | +0.3320 | 0.1768 | ±0.3536 | +1.878 | 0.0604 | . |
| Site: UCSD (vs UAB) | +0.0566 | 0.1071 | ±0.2142 | +0.529 | 0.5971 |  |
| **Site: UW (vs UAB)** | **-0.3155** | 0.1159 | ±0.2319 | **-2.722** | **0.0065** | ** |
| Season: spring (vs autumn) | -0.1088 | 0.1121 | ±0.2242 | -0.970 | 0.3319 |  |
| Season: summer (vs autumn) | +0.2141 | 0.1297 | ±0.2595 | +1.650 | 0.0989 | . |
| Season: winter (vs autumn) | -0.0133 | 0.1198 | ±0.2396 | -0.111 | 0.9114 |  |
| **Age (years)** | **-0.0072** | 0.0035 | ±0.0071 | **-2.015** | **0.0439** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0133 | **+3.154** | **0.0016** | ** |
| Hypertension | +0.0837 | 0.0947 | ±0.1895 | +0.883 | 0.3772 |  |
| High cholesterol | -0.0529 | 0.0823 | ±0.1646 | -0.643 | 0.5202 |  |
| Kidney disease | -0.1118 | 0.1684 | ±0.3369 | -0.663 | 0.5070 |  |
| Circulatory disease | +0.2811 | 0.1626 | ±0.3253 | +1.728 | 0.0839 | . |
| CV (%) | +0.0068 | 0.0191 | ±0.0381 | +0.356 | 0.7220 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **443**, R² = **0.1363**, Adj R² = **0.1080**, F-statistic = **4.82** (p = **2.74e-08**), Residual SE = **0.855** on **428** df, AIC = **1132.8**, BIC = **1194.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7843** | 0.3907 | ±0.7814 | **+4.567** | **4.95e-06** | *** |
| Education: graduate level (vs college) | -0.1029 | 0.0880 | ±0.1761 | -1.168 | 0.2427 |  |
| Education: high school or below (vs college) | +0.3326 | 0.1768 | ±0.3536 | +1.881 | 0.0599 | . |
| Site: UCSD (vs UAB) | +0.0548 | 0.1071 | ±0.2141 | +0.512 | 0.6086 |  |
| **Site: UW (vs UAB)** | **-0.3175** | 0.1160 | ±0.2320 | **-2.736** | **0.0062** | ** |
| Season: spring (vs autumn) | -0.1075 | 0.1123 | ±0.2245 | -0.958 | 0.3381 |  |
| Season: summer (vs autumn) | +0.2146 | 0.1297 | ±0.2594 | +1.655 | 0.0980 | . |
| Season: winter (vs autumn) | -0.0117 | 0.1196 | ±0.2391 | -0.098 | 0.9220 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0071 | **-2.012** | **0.0442** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0133 | **+3.155** | **0.0016** | ** |
| Hypertension | +0.0842 | 0.0948 | ±0.1896 | +0.888 | 0.3745 |  |
| High cholesterol | -0.0535 | 0.0823 | ±0.1645 | -0.651 | 0.5153 |  |
| Kidney disease | -0.1090 | 0.1690 | ±0.3380 | -0.645 | 0.5189 |  |
| Circulatory disease | +0.2822 | 0.1626 | ±0.3253 | +1.735 | 0.0827 | . |
| Mean / SD ratio | -0.0066 | 0.0378 | ±0.0757 | -0.174 | 0.8619 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **443**, R² = **0.1368**, Adj R² = **0.1085**, F-statistic = **4.84** (p = **2.49e-08**), Residual SE = **0.854** on **428** df, AIC = **1132.6**, BIC = **1194.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8670** | 0.3754 | ±0.7507 | **+4.974** | **6.57e-07** | *** |
| Education: graduate level (vs college) | -0.1002 | 0.0883 | ±0.1765 | -1.136 | 0.2561 |  |
| Education: high school or below (vs college) | +0.3322 | 0.1769 | ±0.3539 | +1.877 | 0.0605 | . |
| Site: UCSD (vs UAB) | +0.0561 | 0.1069 | ±0.2139 | +0.524 | 0.6000 |  |
| **Site: UW (vs UAB)** | **-0.3157** | 0.1158 | ±0.2317 | **-2.725** | **0.0064** | ** |
| Season: spring (vs autumn) | -0.1099 | 0.1121 | ±0.2242 | -0.981 | 0.3267 |  |
| Season: summer (vs autumn) | +0.2136 | 0.1297 | ±0.2595 | +1.646 | 0.0997 | . |
| Season: winter (vs autumn) | -0.0130 | 0.1191 | ±0.2382 | -0.109 | 0.9129 |  |
| **Age (years)** | **-0.0072** | 0.0036 | ±0.0071 | **-2.026** | **0.0428** | * |
| **BMI (kg/m2)** | **+0.0208** | 0.0066 | ±0.0132 | **+3.141** | **0.0017** | ** |
| Hypertension | +0.0842 | 0.0948 | ±0.1895 | +0.889 | 0.3742 |  |
| High cholesterol | -0.0528 | 0.0821 | ±0.1643 | -0.643 | 0.5205 |  |
| Kidney disease | -0.1120 | 0.1685 | ±0.3371 | -0.665 | 0.5063 |  |
| Circulatory disease | +0.2837 | 0.1624 | ±0.3248 | +1.747 | 0.0807 | . |
| Avg. daily mean/SD | -0.0154 | 0.0291 | ±0.0582 | -0.530 | 0.5958 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **443**, R² = **0.1393**, Adj R² = **0.1111**, F-statistic = **4.95** (p = **1.48e-08**), Residual SE = **0.853** on **428** df, AIC = **1131.3**, BIC = **1192.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.4013** | 0.3789 | ±0.7578 | **+3.699** | **2.17e-04** | *** |
| Education: graduate level (vs college) | -0.1060 | 0.0873 | ±0.1745 | -1.215 | 0.2244 |  |
| Education: high school or below (vs college) | +0.3187 | 0.1778 | ±0.3556 | +1.792 | 0.0731 | . |
| Site: UCSD (vs UAB) | +0.0592 | 0.1063 | ±0.2126 | +0.556 | 0.5779 |  |
| **Site: UW (vs UAB)** | **-0.3054** | 0.1165 | ±0.2329 | **-2.622** | **0.0087** | ** |
| Season: spring (vs autumn) | -0.1063 | 0.1115 | ±0.2230 | -0.953 | 0.3405 |  |
| Season: summer (vs autumn) | +0.2192 | 0.1299 | ±0.2598 | +1.687 | 0.0916 | . |
| Season: winter (vs autumn) | -0.0129 | 0.1176 | ±0.2352 | -0.110 | 0.9126 |  |
| Age (years) | -0.0067 | 0.0035 | ±0.0071 | -1.882 | 0.0599 | . |
| **BMI (kg/m2)** | **+0.0213** | 0.0066 | ±0.0132 | **+3.221** | **0.0013** | ** |
| Hypertension | +0.0868 | 0.0945 | ±0.1891 | +0.919 | 0.3583 |  |
| High cholesterol | -0.0567 | 0.0816 | ±0.1632 | -0.695 | 0.4870 |  |
| Kidney disease | -0.1189 | 0.1666 | ±0.3333 | -0.714 | 0.4754 |  |
| Circulatory disease | +0.2890 | 0.1620 | ±0.3240 | +1.784 | 0.0744 | . |
| MAG (mg/dL/h) | +0.0087 | 0.0066 | ±0.0133 | +1.303 | 0.1926 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **443**, R² = **0.1365**, Adj R² = **0.1083**, F-statistic = **4.83** (p = **2.61e-08**), Residual SE = **0.855** on **428** df, AIC = **1132.7**, BIC = **1194.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8531** | 0.4100 | ±0.8199 | **+4.520** | **6.18e-06** | *** |
| Education: graduate level (vs college) | -0.1049 | 0.0879 | ±0.1757 | -1.194 | 0.2327 |  |
| Education: high school or below (vs college) | +0.3340 | 0.1766 | ±0.3532 | +1.891 | 0.0586 | . |
| Site: UCSD (vs UAB) | +0.0515 | 0.1068 | ±0.2136 | +0.483 | 0.6294 |  |
| **Site: UW (vs UAB)** | **-0.3212** | 0.1158 | ±0.2316 | **-2.773** | **0.0055** | ** |
| Season: spring (vs autumn) | -0.1047 | 0.1125 | ±0.2249 | -0.931 | 0.3520 |  |
| Season: summer (vs autumn) | +0.2152 | 0.1296 | ±0.2591 | +1.661 | 0.0968 | . |
| Season: winter (vs autumn) | -0.0084 | 0.1195 | ±0.2389 | -0.070 | 0.9440 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0071 | **-2.005** | **0.0449** | * |
| **BMI (kg/m2)** | **+0.0208** | 0.0067 | ±0.0133 | **+3.114** | **0.0018** | ** |
| Hypertension | +0.0839 | 0.0947 | ±0.1893 | +0.886 | 0.3755 |  |
| High cholesterol | -0.0544 | 0.0820 | ±0.1639 | -0.663 | 0.5072 |  |
| Kidney disease | -0.1043 | 0.1699 | ±0.3398 | -0.614 | 0.5395 |  |
| Circulatory disease | +0.2826 | 0.1628 | ±0.3256 | +1.736 | 0.0826 | . |
| Avg. daily range (mg/dL) | -0.0014 | 0.0036 | ±0.0072 | -0.389 | 0.6976 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **443**, R² = **0.1372**, Adj R² = **0.1090**, F-statistic = **4.86** (p = **2.27e-08**), Residual SE = **0.854** on **428** df, AIC = **1132.3**, BIC = **1193.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6638** | 0.3002 | ±0.6004 | **+5.542** | **2.99e-08** | *** |
| Education: graduate level (vs college) | -0.1059 | 0.0875 | ±0.1749 | -1.211 | 0.2259 |  |
| Education: high school or below (vs college) | +0.3263 | 0.1760 | ±0.3521 | +1.854 | 0.0638 | . |
| Site: UCSD (vs UAB) | +0.0579 | 0.1061 | ±0.2121 | +0.546 | 0.5851 |  |
| **Site: UW (vs UAB)** | **-0.3190** | 0.1157 | ±0.2315 | **-2.757** | **0.0058** | ** |
| Season: spring (vs autumn) | -0.1112 | 0.1117 | ±0.2233 | -0.995 | 0.3196 |  |
| Season: summer (vs autumn) | +0.2107 | 0.1312 | ±0.2623 | +1.607 | 0.1082 |  |
| Season: winter (vs autumn) | -0.0166 | 0.1185 | ±0.2371 | -0.140 | 0.8889 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0071 | **-1.987** | **0.0469** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0133 | **+3.150** | **0.0016** | ** |
| Hypertension | +0.0788 | 0.0953 | ±0.1907 | +0.827 | 0.4085 |  |
| High cholesterol | -0.0562 | 0.0821 | ±0.1642 | -0.685 | 0.4935 |  |
| Kidney disease | -0.1064 | 0.1697 | ±0.3394 | -0.627 | 0.5305 |  |
| Circulatory disease | +0.2747 | 0.1612 | ±0.3224 | +1.704 | 0.0883 | . |
| SD of daily means (mg/dL) | +0.0154 | 0.0220 | ±0.0440 | +0.701 | 0.4830 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **443**, R² = **0.1363**, Adj R² = **0.1080**, F-statistic = **4.82** (p = **2.76e-08**), Residual SE = **0.855** on **428** df, AIC = **1132.8**, BIC = **1194.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2.8346 | 14.3314 | ±28.6627 | +0.198 | 0.8432 |  |
| Education: graduate level (vs college) | -0.1037 | 0.0876 | ±0.1751 | -1.185 | 0.2361 |  |
| Education: high school or below (vs college) | +0.3336 | 0.1774 | ±0.3548 | +1.880 | 0.0600 | . |
| Site: UCSD (vs UAB) | +0.0542 | 0.1079 | ±0.2158 | +0.502 | 0.6154 |  |
| **Site: UW (vs UAB)** | **-0.3184** | 0.1169 | ±0.2337 | **-2.724** | **0.0064** | ** |
| Season: spring (vs autumn) | -0.1063 | 0.1121 | ±0.2243 | -0.948 | 0.3433 |  |
| Season: summer (vs autumn) | +0.2147 | 0.1300 | ±0.2599 | +1.653 | 0.0984 | . |
| Season: winter (vs autumn) | -0.0107 | 0.1195 | ±0.2389 | -0.090 | 0.9285 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0071 | **-2.005** | **0.0450** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0132 | **+3.166** | **0.0015** | ** |
| Hypertension | +0.0846 | 0.0951 | ±0.1901 | +0.890 | 0.3735 |  |
| High cholesterol | -0.0544 | 0.0819 | ±0.1639 | -0.664 | 0.5067 |  |
| Kidney disease | -0.1084 | 0.1689 | ±0.3378 | -0.642 | 0.5211 |  |
| Circulatory disease | +0.2828 | 0.1629 | ±0.3258 | +1.736 | 0.0825 | . |
| Time in range 70-180, pooled (%) | -0.0110 | 0.1441 | ±0.2882 | -0.077 | 0.9390 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **443**, R² = **0.1362**, Adj R² = **0.1080**, F-statistic = **4.82** (p = **2.77e-08**), Residual SE = **0.855** on **428** df, AIC = **1132.8**, BIC = **1194.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2.6231 | 13.9389 | ±27.8779 | +0.188 | 0.8507 |  |
| Education: graduate level (vs college) | -0.1037 | 0.0877 | ±0.1755 | -1.182 | 0.2372 |  |
| Education: high school or below (vs college) | +0.3337 | 0.1777 | ±0.3554 | +1.878 | 0.0604 | . |
| Site: UCSD (vs UAB) | +0.0539 | 0.1072 | ±0.2145 | +0.502 | 0.6155 |  |
| **Site: UW (vs UAB)** | **-0.3187** | 0.1161 | ±0.2323 | **-2.745** | **0.0061** | ** |
| Season: spring (vs autumn) | -0.1061 | 0.1121 | ±0.2243 | -0.946 | 0.3440 |  |
| Season: summer (vs autumn) | +0.2152 | 0.1294 | ±0.2587 | +1.663 | 0.0963 | . |
| Season: winter (vs autumn) | -0.0104 | 0.1185 | ±0.2371 | -0.088 | 0.9301 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0071 | **-2.004** | **0.0450** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0133 | **+3.156** | **0.0016** | ** |
| Hypertension | +0.0849 | 0.0947 | ±0.1894 | +0.896 | 0.3700 |  |
| High cholesterol | -0.0545 | 0.0820 | ±0.1640 | -0.665 | 0.5063 |  |
| Kidney disease | -0.1080 | 0.1692 | ±0.3383 | -0.638 | 0.5233 |  |
| Circulatory disease | +0.2826 | 0.1629 | ±0.3258 | +1.735 | 0.0828 | . |
| Avg. daily time in range 70-180 (%) | -0.0089 | 0.1400 | ±0.2801 | -0.064 | 0.9493 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.1380**, Adj R² = **0.1098**, F-statistic = **4.89** (p = **1.93e-08**), Residual SE = **0.854** on **428** df, AIC = **1131.9**, BIC = **1193.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7142** | 0.2804 | ±0.5608 | **+6.114** | **9.74e-10** | *** |
| Education: graduate level (vs college) | -0.1030 | 0.0873 | ±0.1746 | -1.180 | 0.2382 |  |
| Education: high school or below (vs college) | +0.3375 | 0.1782 | ±0.3564 | +1.894 | 0.0583 | . |
| Site: UCSD (vs UAB) | +0.0722 | 0.1106 | ±0.2213 | +0.653 | 0.5140 |  |
| **Site: UW (vs UAB)** | **-0.3083** | 0.1182 | ±0.2363 | **-2.609** | **0.0091** | ** |
| Season: spring (vs autumn) | -0.1187 | 0.1139 | ±0.2279 | -1.042 | 0.2974 |  |
| Season: summer (vs autumn) | +0.2073 | 0.1298 | ±0.2596 | +1.597 | 0.1104 |  |
| Season: winter (vs autumn) | -0.0213 | 0.1187 | ±0.2375 | -0.179 | 0.8576 |  |
| **Age (years)** | **-0.0070** | 0.0036 | ±0.0071 | **-1.979** | **0.0478** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0133 | **+3.157** | **0.0016** | ** |
| Hypertension | +0.0782 | 0.0955 | ±0.1910 | +0.818 | 0.4131 |  |
| High cholesterol | -0.0541 | 0.0822 | ±0.1645 | -0.658 | 0.5104 |  |
| Kidney disease | -0.0954 | 0.1700 | ±0.3401 | -0.561 | 0.5747 |  |
| Circulatory disease | +0.2791 | 0.1623 | ±0.3246 | +1.719 | 0.0855 | . |
| Any reading < 54 during wear (0/1) | +0.1051 | 0.1312 | ±0.2624 | +0.801 | 0.4231 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.1422**, Adj R² = **0.1141**, F-statistic = **5.07** (p = **8.08e-09**), Residual SE = **0.852** on **428** df, AIC = **1129.8**, BIC = **1191.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6948** | 0.2805 | ±0.5609 | **+6.043** | **1.51e-09** | *** |
| Education: graduate level (vs college) | -0.1044 | 0.0873 | ±0.1745 | -1.196 | 0.2318 |  |
| **Education: high school or below (vs college)** | **+0.3503** | 0.1778 | ±0.3556 | **+1.970** | **0.0488** | * |
| Site: UCSD (vs UAB) | +0.0790 | 0.1099 | ±0.2199 | +0.719 | 0.4721 |  |
| **Site: UW (vs UAB)** | **-0.3061** | 0.1175 | ±0.2349 | **-2.606** | **0.0092** | ** |
| Season: spring (vs autumn) | -0.1040 | 0.1117 | ±0.2233 | -0.931 | 0.3516 |  |
| Season: summer (vs autumn) | +0.2131 | 0.1293 | ±0.2587 | +1.648 | 0.0994 | . |
| Season: winter (vs autumn) | -0.0170 | 0.1169 | ±0.2339 | -0.145 | 0.8846 |  |
| Age (years) | -0.0066 | 0.0036 | ±0.0072 | -1.820 | 0.0688 | . |
| **BMI (kg/m2)** | **+0.0202** | 0.0067 | ±0.0134 | **+3.016** | **0.0026** | ** |
| Hypertension | +0.0691 | 0.0953 | ±0.1907 | +0.724 | 0.4689 |  |
| High cholesterol | -0.0492 | 0.0825 | ±0.1650 | -0.596 | 0.5510 |  |
| Kidney disease | -0.0932 | 0.1699 | ±0.3399 | -0.548 | 0.5834 |  |
| Circulatory disease | +0.2742 | 0.1606 | ±0.3212 | +1.707 | 0.0879 | . |
| Time < 54 (%) | +1.3438 | 0.9108 | ±1.8216 | +1.475 | 0.1401 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.1462**, Adj R² = **0.1183**, F-statistic = **5.24** (p = **3.46e-09**), Residual SE = **0.850** on **428** df, AIC = **1127.7**, BIC = **1189.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7037** | 0.2757 | ±0.5514 | **+6.180** | **6.42e-10** | *** |
| Education: graduate level (vs college) | -0.1060 | 0.0876 | ±0.1751 | -1.211 | 0.2260 |  |
| Education: high school or below (vs college) | +0.3430 | 0.1761 | ±0.3523 | +1.947 | 0.0515 | . |
| Site: UCSD (vs UAB) | +0.0682 | 0.1082 | ±0.2164 | +0.630 | 0.5285 |  |
| **Site: UW (vs UAB)** | **-0.3161** | 0.1156 | ±0.2313 | **-2.733** | **0.0063** | ** |
| Season: spring (vs autumn) | -0.0988 | 0.1123 | ±0.2247 | -0.879 | 0.3793 |  |
| Season: summer (vs autumn) | +0.2318 | 0.1294 | ±0.2588 | +1.791 | 0.0733 | . |
| Season: winter (vs autumn) | -0.0078 | 0.1178 | ±0.2355 | -0.067 | 0.9469 |  |
| Age (years) | -0.0068 | 0.0036 | ±0.0071 | -1.928 | 0.0539 | . |
| **BMI (kg/m2)** | **+0.0205** | 0.0066 | ±0.0133 | **+3.090** | **0.0020** | ** |
| Hypertension | +0.0771 | 0.0934 | ±0.1868 | +0.826 | 0.4090 |  |
| High cholesterol | -0.0542 | 0.0822 | ±0.1644 | -0.659 | 0.5098 |  |
| Kidney disease | -0.0973 | 0.1707 | ±0.3414 | -0.570 | 0.5686 |  |
| Circulatory disease | +0.2656 | 0.1613 | ±0.3225 | +1.647 | 0.0996 | . |
| Avg. daily time < 54 (%) | +2.3039 | 1.3775 | ±2.7550 | +1.673 | 0.0944 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.1430**, Adj R² = **0.1149**, F-statistic = **5.10** (p = **6.85e-09**), Residual SE = **0.851** on **428** df, AIC = **1129.4**, BIC = **1190.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6749** | 0.2760 | ±0.5520 | **+6.069** | **1.29e-09** | *** |
| Education: graduate level (vs college) | -0.0998 | 0.0869 | ±0.1739 | -1.148 | 0.2510 |  |
| Education: high school or below (vs college) | +0.3173 | 0.1758 | ±0.3515 | +1.805 | 0.0710 | . |
| Site: UCSD (vs UAB) | +0.0662 | 0.1077 | ±0.2153 | +0.615 | 0.5387 |  |
| **Site: UW (vs UAB)** | **-0.3039** | 0.1163 | ±0.2326 | **-2.613** | **0.0090** | ** |
| Season: spring (vs autumn) | -0.1107 | 0.1113 | ±0.2225 | -0.995 | 0.3196 |  |
| Season: summer (vs autumn) | +0.2112 | 0.1304 | ±0.2608 | +1.620 | 0.1053 |  |
| Season: winter (vs autumn) | -0.0212 | 0.1186 | ±0.2373 | -0.178 | 0.8585 |  |
| **Age (years)** | **-0.0071** | 0.0036 | ±0.0071 | **-1.995** | **0.0460** | * |
| **BMI (kg/m2)** | **+0.0210** | 0.0066 | ±0.0132 | **+3.173** | **0.0015** | ** |
| Hypertension | +0.0945 | 0.0947 | ±0.1895 | +0.997 | 0.3186 |  |
| High cholesterol | -0.0674 | 0.0819 | ±0.1637 | -0.824 | 0.4101 |  |
| Kidney disease | -0.0838 | 0.1696 | ±0.3393 | -0.494 | 0.6213 |  |
| Circulatory disease | +0.2859 | 0.1632 | ±0.3264 | +1.752 | 0.0797 | . |
| Time 54-69, pooled (%) | +0.4151 | 0.2466 | ±0.4931 | +1.684 | 0.0922 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **443**, R² = **0.1423**, Adj R² = **0.1143**, F-statistic = **5.07** (p = **7.84e-09**), Residual SE = **0.852** on **428** df, AIC = **1129.7**, BIC = **1191.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6852** | 0.2750 | ±0.5500 | **+6.128** | **8.89e-10** | *** |
| Education: graduate level (vs college) | -0.0970 | 0.0869 | ±0.1738 | -1.116 | 0.2644 |  |
| Education: high school or below (vs college) | +0.3169 | 0.1752 | ±0.3504 | +1.809 | 0.0705 | . |
| Site: UCSD (vs UAB) | +0.0595 | 0.1072 | ±0.2144 | +0.555 | 0.5786 |  |
| **Site: UW (vs UAB)** | **-0.3107** | 0.1158 | ±0.2317 | **-2.683** | **0.0073** | ** |
| Season: spring (vs autumn) | -0.1015 | 0.1115 | ±0.2230 | -0.910 | 0.3629 |  |
| Season: summer (vs autumn) | +0.2222 | 0.1306 | ±0.2612 | +1.701 | 0.0889 | . |
| Season: winter (vs autumn) | -0.0161 | 0.1184 | ±0.2368 | -0.136 | 0.8915 |  |
| **Age (years)** | **-0.0072** | 0.0036 | ±0.0071 | **-2.021** | **0.0432** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0132 | **+3.168** | **0.0015** | ** |
| Hypertension | +0.1033 | 0.0959 | ±0.1918 | +1.077 | 0.2814 |  |
| High cholesterol | -0.0656 | 0.0819 | ±0.1638 | -0.801 | 0.4229 |  |
| Kidney disease | -0.0920 | 0.1698 | ±0.3396 | -0.542 | 0.5881 |  |
| Circulatory disease | +0.2804 | 0.1636 | ±0.3271 | +1.714 | 0.0865 | . |
| Avg. daily time 54-69 (%) | +0.4010 | 0.2560 | ±0.5121 | +1.566 | 0.1173 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **443**, R² = **0.1449**, Adj R² = **0.1169**, F-statistic = **5.18** (p = **4.59e-09**), Residual SE = **0.850** on **428** df, AIC = **1128.4**, BIC = **1189.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6610** | 0.2787 | ±0.5574 | **+5.960** | **2.52e-09** | *** |
| Education: graduate level (vs college) | -0.0999 | 0.0868 | ±0.1735 | -1.152 | 0.2495 |  |
| Education: high school or below (vs college) | +0.3224 | 0.1764 | ±0.3527 | +1.828 | 0.0675 | . |
| Site: UCSD (vs UAB) | +0.0742 | 0.1085 | ±0.2170 | +0.684 | 0.4940 |  |
| **Site: UW (vs UAB)** | **-0.2998** | 0.1168 | ±0.2335 | **-2.568** | **0.0102** | * |
| Season: spring (vs autumn) | -0.1101 | 0.1111 | ±0.2223 | -0.991 | 0.3219 |  |
| Season: summer (vs autumn) | +0.2106 | 0.1303 | ±0.2606 | +1.616 | 0.1060 |  |
| Season: winter (vs autumn) | -0.0233 | 0.1182 | ±0.2364 | -0.197 | 0.8435 |  |
| Age (years) | -0.0069 | 0.0036 | ±0.0071 | -1.947 | 0.0515 | . |
| **BMI (kg/m2)** | **+0.0207** | 0.0066 | ±0.0132 | **+3.136** | **0.0017** | ** |
| Hypertension | +0.0897 | 0.0942 | ±0.1885 | +0.952 | 0.3413 |  |
| High cholesterol | -0.0660 | 0.0819 | ±0.1639 | -0.806 | 0.4205 |  |
| Kidney disease | -0.0791 | 0.1698 | ±0.3395 | -0.466 | 0.6412 |  |
| Circulatory disease | +0.2833 | 0.1626 | ±0.3252 | +1.742 | 0.0814 | . |
| Time < 70 (%) | +0.4188 | 0.2279 | ±0.4559 | +1.837 | 0.0662 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **443**, R² = **0.1447**, Adj R² = **0.1167**, F-statistic = **5.17** (p = **4.82e-09**), Residual SE = **0.851** on **428** df, AIC = **1128.5**, BIC = **1189.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6750** | 0.2757 | ±0.5514 | **+6.075** | **1.24e-09** | *** |
| Education: graduate level (vs college) | -0.0969 | 0.0866 | ±0.1733 | -1.118 | 0.2635 |  |
| Education: high school or below (vs college) | +0.3175 | 0.1755 | ±0.3510 | +1.809 | 0.0705 | . |
| Site: UCSD (vs UAB) | +0.0627 | 0.1075 | ±0.2150 | +0.583 | 0.5598 |  |
| **Site: UW (vs UAB)** | **-0.3096** | 0.1159 | ±0.2317 | **-2.673** | **0.0075** | ** |
| Season: spring (vs autumn) | -0.0997 | 0.1114 | ±0.2228 | -0.895 | 0.3708 |  |
| Season: summer (vs autumn) | +0.2259 | 0.1305 | ±0.2611 | +1.730 | 0.0835 | . |
| Season: winter (vs autumn) | -0.0161 | 0.1181 | ±0.2362 | -0.136 | 0.8914 |  |
| **Age (years)** | **-0.0072** | 0.0036 | ±0.0071 | **-2.009** | **0.0445** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0132 | **+3.159** | **0.0016** | ** |
| Hypertension | +0.1033 | 0.0956 | ±0.1911 | +1.081 | 0.2798 |  |
| High cholesterol | -0.0665 | 0.0819 | ±0.1638 | -0.812 | 0.4169 |  |
| Kidney disease | -0.0889 | 0.1700 | ±0.3400 | -0.523 | 0.6009 |  |
| Circulatory disease | +0.2770 | 0.1633 | ±0.3266 | +1.696 | 0.0898 | . |
| Avg. daily time < 70 (%) | +0.4306 | 0.2449 | ±0.4897 | +1.759 | 0.0786 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.1410**, Adj R² = **0.1129**, F-statistic = **5.02** (p = **1.05e-08**), Residual SE = **0.852** on **428** df, AIC = **1130.4**, BIC = **1191.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +118.4699 | 89.5473 | ±179.0946 | +1.323 | 0.1858 |  |
| Education: graduate level (vs college) | -0.1044 | 0.0874 | ±0.1747 | -1.195 | 0.2320 |  |
| **Education: high school or below (vs college)** | **+0.3486** | 0.1778 | ±0.3555 | **+1.961** | **0.0499** | * |
| Site: UCSD (vs UAB) | +0.0774 | 0.1101 | ±0.2203 | +0.703 | 0.4822 |  |
| **Site: UW (vs UAB)** | **-0.3065** | 0.1178 | ±0.2356 | **-2.601** | **0.0093** | ** |
| Season: spring (vs autumn) | -0.1055 | 0.1118 | ±0.2236 | -0.943 | 0.3455 |  |
| Season: summer (vs autumn) | +0.2135 | 0.1293 | ±0.2586 | +1.651 | 0.0987 | . |
| Season: winter (vs autumn) | -0.0171 | 0.1172 | ±0.2344 | -0.146 | 0.8842 |  |
| Age (years) | -0.0066 | 0.0036 | ±0.0073 | -1.810 | 0.0703 | . |
| **BMI (kg/m2)** | **+0.0203** | 0.0067 | ±0.0133 | **+3.049** | **0.0023** | ** |
| Hypertension | +0.0717 | 0.0953 | ±0.1907 | +0.752 | 0.4522 |  |
| High cholesterol | -0.0502 | 0.0824 | ±0.1649 | -0.609 | 0.5428 |  |
| Kidney disease | -0.0952 | 0.1699 | ±0.3399 | -0.560 | 0.5754 |  |
| Circulatory disease | +0.2750 | 0.1608 | ±0.3217 | +1.710 | 0.0873 | . |
| Time 54-250, pooled (%) | -1.1678 | 0.8960 | ±1.7921 | -1.303 | 0.1925 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.1440**, Adj R² = **0.1160**, F-statistic = **5.14** (p = **5.53e-09**), Residual SE = **0.851** on **428** df, AIC = **1128.8**, BIC = **1190.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +200.3425 | 128.7187 | ±257.4374 | +1.556 | 0.1196 |  |
| Education: graduate level (vs college) | -0.1059 | 0.0877 | ±0.1753 | -1.209 | 0.2268 |  |
| Education: high school or below (vs college) | +0.3425 | 0.1763 | ±0.3527 | +1.943 | 0.0521 | . |
| Site: UCSD (vs UAB) | +0.0693 | 0.1087 | ±0.2173 | +0.638 | 0.5233 |  |
| **Site: UW (vs UAB)** | **-0.3141** | 0.1162 | ±0.2324 | **-2.702** | **0.0069** | ** |
| Season: spring (vs autumn) | -0.1019 | 0.1122 | ±0.2244 | -0.909 | 0.3636 |  |
| Season: summer (vs autumn) | +0.2298 | 0.1293 | ±0.2586 | +1.777 | 0.0755 | . |
| Season: winter (vs autumn) | -0.0100 | 0.1177 | ±0.2353 | -0.085 | 0.9322 |  |
| Age (years) | -0.0067 | 0.0036 | ±0.0071 | -1.891 | 0.0586 | . |
| **BMI (kg/m2)** | **+0.0207** | 0.0066 | ±0.0133 | **+3.129** | **0.0018** | ** |
| Hypertension | +0.0792 | 0.0936 | ±0.1871 | +0.846 | 0.3974 |  |
| High cholesterol | -0.0548 | 0.0822 | ±0.1644 | -0.667 | 0.5049 |  |
| Kidney disease | -0.0989 | 0.1707 | ±0.3413 | -0.580 | 0.5621 |  |
| Circulatory disease | +0.2675 | 0.1614 | ±0.3229 | +1.657 | 0.0975 | . |
| Avg. daily time 54-250 (%) | -1.9865 | 1.2874 | ±2.5747 | -1.543 | 0.1228 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **443**, R² = **0.1401**, Adj R² = **0.1120**, F-statistic = **4.98** (p = **1.24e-08**), Residual SE = **0.853** on **428** df, AIC = **1130.8**, BIC = **1192.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8131** | 0.2863 | ±0.5726 | **+6.333** | **2.40e-10** | *** |
| Education: graduate level (vs college) | -0.1042 | 0.0874 | ±0.1749 | -1.192 | 0.2331 |  |
| Education: high school or below (vs college) | +0.3252 | 0.1770 | ±0.3541 | +1.837 | 0.0662 | . |
| Site: UCSD (vs UAB) | +0.0536 | 0.1060 | ±0.2120 | +0.506 | 0.6128 |  |
| **Site: UW (vs UAB)** | **-0.3175** | 0.1149 | ±0.2297 | **-2.764** | **0.0057** | ** |
| Season: spring (vs autumn) | -0.1068 | 0.1123 | ±0.2246 | -0.952 | 0.3413 |  |
| Season: summer (vs autumn) | +0.2167 | 0.1297 | ±0.2593 | +1.672 | 0.0946 | . |
| Season: winter (vs autumn) | -0.0089 | 0.1179 | ±0.2357 | -0.075 | 0.9399 |  |
| **Age (years)** | **-0.0072** | 0.0035 | ±0.0071 | **-2.025** | **0.0429** | * |
| **BMI (kg/m2)** | **+0.0205** | 0.0067 | ±0.0134 | **+3.056** | **0.0022** | ** |
| Hypertension | +0.0891 | 0.0948 | ±0.1896 | +0.940 | 0.3472 |  |
| High cholesterol | -0.0561 | 0.0819 | ±0.1639 | -0.685 | 0.4935 |  |
| Kidney disease | -0.0788 | 0.1743 | ±0.3485 | -0.452 | 0.6512 |  |
| Circulatory disease | +0.2803 | 0.1615 | ±0.3229 | +1.736 | 0.0825 | . |
| Time 181-250, pooled (%) | -0.2043 | 0.1470 | ±0.2940 | -1.390 | 0.1646 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **443**, R² = **0.1397**, Adj R² = **0.1115**, F-statistic = **4.96** (p = **1.37e-08**), Residual SE = **0.853** on **428** df, AIC = **1131.1**, BIC = **1192.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8006** | 0.2829 | ±0.5659 | **+6.364** | **1.97e-10** | *** |
| Education: graduate level (vs college) | -0.1044 | 0.0875 | ±0.1750 | -1.194 | 0.2326 |  |
| Education: high school or below (vs college) | +0.3223 | 0.1768 | ±0.3535 | +1.823 | 0.0683 | . |
| Site: UCSD (vs UAB) | +0.0534 | 0.1061 | ±0.2122 | +0.504 | 0.6145 |  |
| **Site: UW (vs UAB)** | **-0.3164** | 0.1149 | ±0.2298 | **-2.754** | **0.0059** | ** |
| Season: spring (vs autumn) | -0.1052 | 0.1126 | ±0.2251 | -0.934 | 0.3502 |  |
| Season: summer (vs autumn) | +0.2152 | 0.1295 | ±0.2590 | +1.662 | 0.0965 | . |
| Season: winter (vs autumn) | -0.0108 | 0.1179 | ±0.2358 | -0.091 | 0.9273 |  |
| **Age (years)** | **-0.0073** | 0.0035 | ±0.0071 | **-2.059** | **0.0395** | * |
| **BMI (kg/m2)** | **+0.0208** | 0.0066 | ±0.0132 | **+3.152** | **0.0016** | ** |
| Hypertension | +0.0887 | 0.0949 | ±0.1898 | +0.935 | 0.3499 |  |
| High cholesterol | -0.0534 | 0.0819 | ±0.1637 | -0.653 | 0.5139 |  |
| Kidney disease | -0.0911 | 0.1741 | ±0.3482 | -0.523 | 0.6008 |  |
| Circulatory disease | +0.2816 | 0.1614 | ±0.3228 | +1.745 | 0.0810 | . |
| Avg. daily time 181-250 (%) | -0.1892 | 0.1426 | ±0.2852 | -1.327 | 0.1846 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **443**, R² = **0.1403**, Adj R² = **0.1122**, F-statistic = **4.99** (p = **1.20e-08**), Residual SE = **0.853** on **428** df, AIC = **1130.8**, BIC = **1192.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8158** | 0.2867 | ±0.5733 | **+6.334** | **2.39e-10** | *** |
| Education: graduate level (vs college) | -0.1042 | 0.0874 | ±0.1748 | -1.192 | 0.2331 |  |
| Education: high school or below (vs college) | +0.3250 | 0.1770 | ±0.3540 | +1.836 | 0.0664 | . |
| Site: UCSD (vs UAB) | +0.0533 | 0.1060 | ±0.2120 | +0.503 | 0.6148 |  |
| **Site: UW (vs UAB)** | **-0.3177** | 0.1148 | ±0.2297 | **-2.766** | **0.0057** | ** |
| Season: spring (vs autumn) | -0.1066 | 0.1123 | ±0.2246 | -0.950 | 0.3422 |  |
| Season: summer (vs autumn) | +0.2167 | 0.1297 | ±0.2593 | +1.672 | 0.0946 | . |
| Season: winter (vs autumn) | -0.0087 | 0.1179 | ±0.2358 | -0.074 | 0.9412 |  |
| **Age (years)** | **-0.0072** | 0.0035 | ±0.0071 | **-2.029** | **0.0425** | * |
| **BMI (kg/m2)** | **+0.0204** | 0.0067 | ±0.0134 | **+3.052** | **0.0023** | ** |
| Hypertension | +0.0891 | 0.0948 | ±0.1895 | +0.940 | 0.3472 |  |
| High cholesterol | -0.0561 | 0.0819 | ±0.1639 | -0.685 | 0.4936 |  |
| Kidney disease | -0.0783 | 0.1744 | ±0.3487 | -0.449 | 0.6535 |  |
| Circulatory disease | +0.2803 | 0.1614 | ±0.3229 | +1.736 | 0.0825 | . |
| Time > 180 (%) | -0.2078 | 0.1467 | ±0.2933 | -1.417 | 0.1566 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **443**, R² = **0.1398**, Adj R² = **0.1117**, F-statistic = **4.97** (p = **1.33e-08**), Residual SE = **0.853** on **428** df, AIC = **1131.0**, BIC = **1192.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8032** | 0.2832 | ±0.5665 | **+6.366** | **1.93e-10** | *** |
| Education: graduate level (vs college) | -0.1044 | 0.0875 | ±0.1749 | -1.194 | 0.2326 |  |
| Education: high school or below (vs college) | +0.3220 | 0.1767 | ±0.3535 | +1.822 | 0.0685 | . |
| Site: UCSD (vs UAB) | +0.0531 | 0.1061 | ±0.2122 | +0.501 | 0.6165 |  |
| **Site: UW (vs UAB)** | **-0.3166** | 0.1149 | ±0.2297 | **-2.757** | **0.0058** | ** |
| Season: spring (vs autumn) | -0.1049 | 0.1126 | ±0.2252 | -0.932 | 0.3513 |  |
| Season: summer (vs autumn) | +0.2152 | 0.1295 | ±0.2590 | +1.662 | 0.0965 | . |
| Season: winter (vs autumn) | -0.0106 | 0.1179 | ±0.2359 | -0.090 | 0.9285 |  |
| **Age (years)** | **-0.0073** | 0.0035 | ±0.0071 | **-2.064** | **0.0391** | * |
| **BMI (kg/m2)** | **+0.0208** | 0.0066 | ±0.0132 | **+3.149** | **0.0016** | ** |
| Hypertension | +0.0887 | 0.0949 | ±0.1897 | +0.935 | 0.3499 |  |
| High cholesterol | -0.0534 | 0.0819 | ±0.1637 | -0.652 | 0.5145 |  |
| Kidney disease | -0.0908 | 0.1742 | ±0.3484 | -0.521 | 0.6023 |  |
| Circulatory disease | +0.2816 | 0.1614 | ±0.3227 | +1.745 | 0.0809 | . |
| Avg. daily time > 180 (%) | -0.1928 | 0.1421 | ±0.2842 | -1.357 | 0.1749 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **443**, R² = **0.1438**, Adj R² = **0.1157**, F-statistic = **5.13** (p = **5.83e-09**), Residual SE = **0.851** on **428** df, AIC = **1129.0**, BIC = **1190.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8023** | 0.2761 | ±0.5522 | **+6.528** | **6.67e-11** | *** |
| Education: graduate level (vs college) | -0.1126 | 0.0882 | ±0.1764 | -1.276 | 0.2019 |  |
| Education: high school or below (vs college) | +0.3279 | 0.1751 | ±0.3502 | +1.873 | 0.0611 | . |
| Site: UCSD (vs UAB) | +0.0541 | 0.1061 | ±0.2122 | +0.510 | 0.6102 |  |
| **Site: UW (vs UAB)** | **-0.3127** | 0.1149 | ±0.2298 | **-2.721** | **0.0065** | ** |
| Season: spring (vs autumn) | -0.1017 | 0.1126 | ±0.2251 | -0.903 | 0.3664 |  |
| Season: summer (vs autumn) | +0.2105 | 0.1282 | ±0.2564 | +1.642 | 0.1006 |  |
| Season: winter (vs autumn) | +0.0102 | 0.1199 | ±0.2399 | +0.085 | 0.9319 |  |
| **Age (years)** | **-0.0083** | 0.0036 | ±0.0073 | **-2.281** | **0.0225** | * |
| **BMI (kg/m2)** | **+0.0217** | 0.0065 | ±0.0131 | **+3.316** | **9.13e-04** | *** |
| Hypertension | +0.1016 | 0.0954 | ±0.1908 | +1.065 | 0.2868 |  |
| High cholesterol | -0.0496 | 0.0817 | ±0.1633 | -0.607 | 0.5440 |  |
| Kidney disease | -0.1056 | 0.1827 | ±0.3654 | -0.578 | 0.5635 |  |
| Circulatory disease | +0.2729 | 0.1617 | ±0.3235 | +1.688 | 0.0915 | . |
| Nocturnal time > 180 (%) | -0.2262 | 0.1273 | ±0.2547 | -1.776 | 0.0757 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 443; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **443**, R² = **0.3401**, Adj R² = **0.3201**, F-statistic = **17.01** (p = **1.31e-31**), Residual SE = **1.892** on **429** df, AIC = **1836.0**, BIC = **1893.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9350** | 0.8204 | ±1.6407 | **+29.177** | **3.85e-187** | *** |
| Education: graduate level (vs college) | +0.0519 | 0.1979 | ±0.3959 | +0.262 | 0.7930 |  |
| Education: high school or below (vs college) | +0.2979 | 0.3608 | ±0.7217 | +0.826 | 0.4090 |  |
| Site: UCSD (vs UAB) | -0.2705 | 0.2355 | ±0.4711 | -1.149 | 0.2507 |  |
| **Site: UW (vs UAB)** | **-1.0842** | 0.2344 | ±0.4688 | **-4.625** | **3.74e-06** | *** |
| Season: spring (vs autumn) | -0.2108 | 0.2729 | ±0.5459 | -0.772 | 0.4400 |  |
| **Season: summer (vs autumn)** | **+1.7948** | 0.3201 | ±0.6403 | **+5.606** | **2.07e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5259** | 0.2809 | ±0.5618 | **-5.432** | **5.57e-08** | *** |
| Age (years) | +0.0078 | 0.0085 | ±0.0171 | +0.911 | 0.3621 |  |
| BMI (kg/m2) | +0.0208 | 0.0156 | ±0.0313 | +1.331 | 0.1832 |  |
| Hypertension | -0.0935 | 0.2118 | ±0.4235 | -0.442 | 0.6588 |  |
| High cholesterol | -0.3404 | 0.1909 | ±0.3819 | -1.783 | 0.0746 | . |
| **Kidney disease** | **+0.9283** | 0.3632 | ±0.7264 | **+2.556** | **0.0106** | * |
| **Circulatory disease** | **+0.8075** | 0.3573 | ±0.7146 | **+2.260** | **0.0238** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **443**, R² = **0.3409**, Adj R² = **0.3194**, F-statistic = **15.81** (p = **4.36e-31**), Residual SE = **1.893** on **428** df, AIC = **1837.5**, BIC = **1898.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0863** | 1.8507 | ±3.7014 | **+13.555** | **7.39e-42** | *** |
| Education: graduate level (vs college) | +0.0466 | 0.1971 | ±0.3942 | +0.236 | 0.8131 |  |
| Education: high school or below (vs college) | +0.3139 | 0.3639 | ±0.7279 | +0.862 | 0.3884 |  |
| Site: UCSD (vs UAB) | -0.2679 | 0.2364 | ±0.4728 | -1.133 | 0.2570 |  |
| **Site: UW (vs UAB)** | **-1.0871** | 0.2351 | ±0.4702 | **-4.624** | **3.77e-06** | *** |
| Season: spring (vs autumn) | -0.2394 | 0.2739 | ±0.5478 | -0.874 | 0.3820 |  |
| **Season: summer (vs autumn)** | **+1.8056** | 0.3195 | ±0.6391 | **+5.651** | **1.60e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5364** | 0.2815 | ±0.5630 | **-5.458** | **4.81e-08** | *** |
| Age (years) | +0.0084 | 0.0088 | ±0.0175 | +0.963 | 0.3358 |  |
| BMI (kg/m2) | +0.0220 | 0.0162 | ±0.0324 | +1.353 | 0.1760 |  |
| Hypertension | -0.0808 | 0.2143 | ±0.4285 | -0.377 | 0.7060 |  |
| High cholesterol | -0.3114 | 0.1994 | ±0.3988 | -1.562 | 0.1183 |  |
| **Kidney disease** | **+0.9144** | 0.3611 | ±0.7222 | **+2.532** | **0.0113** | * |
| **Circulatory disease** | **+0.7958** | 0.3589 | ±0.7179 | **+2.217** | **0.0266** | * |
| HbA1c (%) | -0.2211 | 0.3438 | ±0.6876 | -0.643 | 0.5201 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **443**, R² = **0.3401**, Adj R² = **0.3186**, F-statistic = **15.76** (p = **5.53e-31**), Residual SE = **1.895** on **428** df, AIC = **1838.0**, BIC = **1899.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9690** | 1.5979 | ±3.1957 | **+15.001** | **7.27e-51** | *** |
| Education: graduate level (vs college) | +0.0520 | 0.1983 | ±0.3967 | +0.262 | 0.7931 |  |
| Education: high school or below (vs college) | +0.2976 | 0.3615 | ±0.7230 | +0.823 | 0.4103 |  |
| Site: UCSD (vs UAB) | -0.2702 | 0.2361 | ±0.4721 | -1.145 | 0.2523 |  |
| **Site: UW (vs UAB)** | **-1.0839** | 0.2350 | ±0.4701 | **-4.612** | **3.99e-06** | *** |
| Season: spring (vs autumn) | -0.2111 | 0.2724 | ±0.5448 | -0.775 | 0.4384 |  |
| **Season: summer (vs autumn)** | **+1.7948** | 0.3208 | ±0.6415 | **+5.595** | **2.20e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5262** | 0.2812 | ±0.5625 | **-5.426** | **5.75e-08** | *** |
| Age (years) | +0.0078 | 0.0086 | ±0.0171 | +0.909 | 0.3636 |  |
| BMI (kg/m2) | +0.0208 | 0.0158 | ±0.0315 | +1.323 | 0.1859 |  |
| Hypertension | -0.0932 | 0.2127 | ±0.4254 | -0.438 | 0.6612 |  |
| High cholesterol | -0.3406 | 0.1917 | ±0.3833 | -1.777 | 0.0756 | . |
| **Kidney disease** | **+0.9286** | 0.3638 | ±0.7275 | **+2.553** | **0.0107** | * |
| **Circulatory disease** | **+0.8076** | 0.3579 | ±0.7158 | **+2.256** | **0.0241** | * |
| Mean glucose (mg/dL) | -0.0003 | 0.0125 | ±0.0250 | -0.024 | 0.9809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **443**, R² = **0.3401**, Adj R² = **0.3186**, F-statistic = **15.76** (p = **5.53e-31**), Residual SE = **1.895** on **428** df, AIC = **1838.0**, BIC = **1899.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0105** | 3.2072 | ±6.4144 | **+7.486** | **7.08e-14** | *** |
| Education: graduate level (vs college) | +0.0520 | 0.1983 | ±0.3967 | +0.262 | 0.7931 |  |
| Education: high school or below (vs college) | +0.2976 | 0.3615 | ±0.7230 | +0.823 | 0.4103 |  |
| Site: UCSD (vs UAB) | -0.2702 | 0.2361 | ±0.4721 | -1.145 | 0.2523 |  |
| **Site: UW (vs UAB)** | **-1.0839** | 0.2350 | ±0.4701 | **-4.612** | **3.99e-06** | *** |
| Season: spring (vs autumn) | -0.2111 | 0.2724 | ±0.5448 | -0.775 | 0.4384 |  |
| **Season: summer (vs autumn)** | **+1.7948** | 0.3208 | ±0.6415 | **+5.595** | **2.20e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5262** | 0.2812 | ±0.5625 | **-5.426** | **5.75e-08** | *** |
| Age (years) | +0.0078 | 0.0086 | ±0.0171 | +0.909 | 0.3636 |  |
| BMI (kg/m2) | +0.0208 | 0.0158 | ±0.0315 | +1.323 | 0.1859 |  |
| Hypertension | -0.0932 | 0.2127 | ±0.4254 | -0.438 | 0.6612 |  |
| High cholesterol | -0.3406 | 0.1917 | ±0.3833 | -1.777 | 0.0756 | . |
| **Kidney disease** | **+0.9286** | 0.3638 | ±0.7275 | **+2.553** | **0.0107** | * |
| **Circulatory disease** | **+0.8076** | 0.3579 | ±0.7158 | **+2.256** | **0.0241** | * |
| GMI (%) | -0.0125 | 0.5225 | ±1.0450 | -0.024 | 0.9809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **443**, R² = **0.3419**, Adj R² = **0.3203**, F-statistic = **15.88** (p = **3.27e-31**), Residual SE = **1.892** on **428** df, AIC = **1836.9**, BIC = **1898.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.1050** | 1.3521 | ±2.7041 | **+18.568** | **5.86e-77** | *** |
| Education: graduate level (vs college) | +0.0457 | 0.1987 | ±0.3974 | +0.230 | 0.8180 |  |
| Education: high school or below (vs college) | +0.2818 | 0.3641 | ±0.7282 | +0.774 | 0.4390 |  |
| Site: UCSD (vs UAB) | -0.2466 | 0.2382 | ±0.4764 | -1.035 | 0.3005 |  |
| **Site: UW (vs UAB)** | **-1.0630** | 0.2362 | ±0.4723 | **-4.501** | **6.77e-06** | *** |
| Season: spring (vs autumn) | -0.2193 | 0.2727 | ±0.5455 | -0.804 | 0.4215 |  |
| **Season: summer (vs autumn)** | **+1.7950** | 0.3206 | ±0.6413 | **+5.598** | **2.17e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5303** | 0.2811 | ±0.5622 | **-5.444** | **5.20e-08** | *** |
| Age (years) | +0.0065 | 0.0086 | ±0.0173 | +0.756 | 0.4498 |  |
| BMI (kg/m2) | +0.0230 | 0.0165 | ±0.0330 | +1.393 | 0.1637 |  |
| Hypertension | -0.0809 | 0.2126 | ±0.4253 | -0.380 | 0.7038 |  |
| High cholesterol | -0.3427 | 0.1909 | ±0.3819 | -1.795 | 0.0727 | . |
| **Kidney disease** | **+0.9198** | 0.3586 | ±0.7173 | **+2.565** | **0.0103** | * |
| **Circulatory disease** | **+0.8041** | 0.3569 | ±0.7138 | **+2.253** | **0.0243** | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0102 | 0.0098 | ±0.0196 | -1.034 | 0.3012 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **443**, R² = **0.3441**, Adj R² = **0.3227**, F-statistic = **16.04** (p = **1.62e-31**), Residual SE = **1.889** on **428** df, AIC = **1835.3**, BIC = **1896.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9437** | 1.0674 | ±2.1347 | **+23.370** | **8.72e-121** | *** |
| Education: graduate level (vs college) | +0.0347 | 0.1997 | ±0.3995 | +0.174 | 0.8620 |  |
| Education: high school or below (vs college) | +0.3049 | 0.3590 | ±0.7181 | +0.849 | 0.3957 |  |
| Site: UCSD (vs UAB) | -0.2933 | 0.2352 | ±0.4705 | -1.247 | 0.2124 |  |
| **Site: UW (vs UAB)** | **-1.1085** | 0.2340 | ±0.4681 | **-4.736** | **2.18e-06** | *** |
| Season: spring (vs autumn) | -0.1934 | 0.2733 | ±0.5466 | -0.708 | 0.4791 |  |
| **Season: summer (vs autumn)** | **+1.8002** | 0.3185 | ±0.6370 | **+5.652** | **1.59e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5015** | 0.2821 | ±0.5642 | **-5.322** | **1.03e-07** | *** |
| Age (years) | +0.0081 | 0.0085 | ±0.0170 | +0.947 | 0.3434 |  |
| BMI (kg/m2) | +0.0217 | 0.0158 | ±0.0316 | +1.372 | 0.1700 |  |
| Hypertension | -0.0728 | 0.2122 | ±0.4244 | -0.343 | 0.7317 |  |
| High cholesterol | -0.3584 | 0.1915 | ±0.3831 | -1.871 | 0.0613 | . |
| **Kidney disease** | **+0.9827** | 0.3793 | ±0.7586 | **+2.591** | **0.0096** | ** |
| **Circulatory disease** | **+0.8241** | 0.3633 | ±0.7265 | **+2.269** | **0.0233** | * |
| Glucose SD, pooled (mg/dL) | -0.0623 | 0.0408 | ±0.0815 | -1.529 | 0.1262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **443**, R² = **0.3464**, Adj R² = **0.3250**, F-statistic = **16.20** (p = **8.01e-32**), Residual SE = **1.886** on **428** df, AIC = **1833.8**, BIC = **1895.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0452** | 1.0449 | ±2.0898 | **+23.969** | **5.87e-127** | *** |
| Education: graduate level (vs college) | +0.0258 | 0.2003 | ±0.4007 | +0.129 | 0.8975 |  |
| Education: high school or below (vs college) | +0.2932 | 0.3636 | ±0.7273 | +0.806 | 0.4200 |  |
| Site: UCSD (vs UAB) | -0.2911 | 0.2345 | ±0.4690 | -1.242 | 0.2144 |  |
| **Site: UW (vs UAB)** | **-1.1086** | 0.2326 | ±0.4652 | **-4.766** | **1.88e-06** | *** |
| Season: spring (vs autumn) | -0.1970 | 0.2730 | ±0.5461 | -0.722 | 0.4706 |  |
| **Season: summer (vs autumn)** | **+1.7956** | 0.3183 | ±0.6366 | **+5.641** | **1.69e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5135** | 0.2793 | ±0.5587 | **-5.418** | **6.02e-08** | *** |
| Age (years) | +0.0084 | 0.0085 | ±0.0169 | +0.991 | 0.3218 |  |
| BMI (kg/m2) | +0.0227 | 0.0161 | ±0.0322 | +1.414 | 0.1574 |  |
| Hypertension | -0.0781 | 0.2121 | ±0.4242 | -0.368 | 0.7129 |  |
| High cholesterol | -0.3601 | 0.1913 | ±0.3827 | -1.882 | 0.0598 | . |
| **Kidney disease** | **+0.9939** | 0.3830 | ±0.7660 | **+2.595** | **0.0095** | ** |
| **Circulatory disease** | **+0.8109** | 0.3633 | ±0.7265 | **+2.232** | **0.0256** | * |
| Avg. daily SD (mg/dL) | -0.0770 | 0.0420 | ±0.0840 | -1.834 | 0.0666 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **443**, R² = **0.3442**, Adj R² = **0.3228**, F-statistic = **16.05** (p = **1.57e-31**), Residual SE = **1.889** on **428** df, AIC = **1835.3**, BIC = **1896.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9306** | 1.0652 | ±2.1304 | **+23.405** | **3.81e-121** | *** |
| Education: graduate level (vs college) | +0.0330 | 0.1997 | ±0.3993 | +0.165 | 0.8687 |  |
| Education: high school or below (vs college) | +0.3128 | 0.3570 | ±0.7140 | +0.876 | 0.3809 |  |
| Site: UCSD (vs UAB) | -0.3009 | 0.2354 | ±0.4707 | -1.278 | 0.2011 |  |
| **Site: UW (vs UAB)** | **-1.1177** | 0.2340 | ±0.4679 | **-4.777** | **1.78e-06** | *** |
| Season: spring (vs autumn) | -0.1844 | 0.2727 | ±0.5455 | -0.676 | 0.4990 |  |
| **Season: summer (vs autumn)** | **+1.8037** | 0.3185 | ±0.6371 | **+5.663** | **1.49e-08** | *** |
| **Season: winter (vs autumn)** | **-1.4949** | 0.2825 | ±0.5649 | **-5.292** | **1.21e-07** | *** |
| Age (years) | +0.0082 | 0.0085 | ±0.0170 | +0.966 | 0.3342 |  |
| BMI (kg/m2) | +0.0211 | 0.0158 | ±0.0315 | +1.337 | 0.1813 |  |
| Hypertension | -0.0829 | 0.2118 | ±0.4236 | -0.391 | 0.6956 |  |
| High cholesterol | -0.3534 | 0.1916 | ±0.3832 | -1.844 | 0.0652 | . |
| **Kidney disease** | **+0.9711** | 0.3792 | ±0.7584 | **+2.561** | **0.0104** | * |
| **Circulatory disease** | **+0.8237** | 0.3634 | ±0.7268 | **+2.267** | **0.0234** | * |
| CV (%) | -0.0694 | 0.0449 | ±0.0897 | -1.546 | 0.1222 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **443**, R² = **0.3434**, Adj R² = **0.3220**, F-statistic = **15.99** (p = **2.01e-31**), Residual SE = **1.890** on **428** df, AIC = **1835.8**, BIC = **1897.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.0402** | 1.0217 | ±2.0434 | **+22.551** | **1.33e-112** | *** |
| Education: graduate level (vs college) | +0.0324 | 0.2003 | ±0.4007 | +0.162 | 0.8714 |  |
| Education: high school or below (vs college) | +0.3138 | 0.3572 | ±0.7143 | +0.879 | 0.3796 |  |
| Site: UCSD (vs UAB) | -0.2931 | 0.2349 | ±0.4699 | -1.247 | 0.2122 |  |
| **Site: UW (vs UAB)** | **-1.1098** | 0.2334 | ±0.4668 | **-4.755** | **1.98e-06** | *** |
| Season: spring (vs autumn) | -0.1850 | 0.2725 | ±0.5450 | -0.679 | 0.4972 |  |
| **Season: summer (vs autumn)** | **+1.8021** | 0.3190 | ±0.6379 | **+5.650** | **1.61e-08** | *** |
| **Season: winter (vs autumn)** | **-1.4987** | 0.2821 | ±0.5641 | **-5.313** | **1.08e-07** | *** |
| Age (years) | +0.0080 | 0.0085 | ±0.0170 | +0.948 | 0.3431 |  |
| BMI (kg/m2) | +0.0210 | 0.0157 | ±0.0314 | +1.339 | 0.1804 |  |
| Hypertension | -0.0834 | 0.2118 | ±0.4236 | -0.394 | 0.6936 |  |
| High cholesterol | -0.3532 | 0.1915 | ±0.3830 | -1.844 | 0.0651 | . |
| **Kidney disease** | **+0.9561** | 0.3749 | ±0.7497 | **+2.551** | **0.0108** | * |
| **Circulatory disease** | **+0.8172** | 0.3622 | ±0.7245 | **+2.256** | **0.0241** | * |
| Mean / SD ratio | +0.1265 | 0.0939 | ±0.1877 | +1.348 | 0.1776 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **443**, R² = **0.3451**, Adj R² = **0.3236**, F-statistic = **16.11** (p = **1.22e-31**), Residual SE = **1.887** on **428** df, AIC = **1834.7**, BIC = **1896.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9383** | 1.0102 | ±2.0204 | **+22.707** | **3.81e-114** | *** |
| Education: graduate level (vs college) | +0.0239 | 0.2023 | ±0.4046 | +0.118 | 0.9058 |  |
| Education: high school or below (vs college) | +0.3078 | 0.3604 | ±0.7208 | +0.854 | 0.3930 |  |
| Site: UCSD (vs UAB) | -0.2893 | 0.2342 | ±0.4685 | -1.235 | 0.2169 |  |
| **Site: UW (vs UAB)** | **-1.1084** | 0.2318 | ±0.4636 | **-4.781** | **1.74e-06** | *** |
| Season: spring (vs autumn) | -0.1819 | 0.2726 | ±0.5452 | -0.667 | 0.5046 |  |
| **Season: summer (vs autumn)** | **+1.8054** | 0.3191 | ±0.6382 | **+5.658** | **1.53e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5048** | 0.2803 | ±0.5606 | **-5.368** | **7.95e-08** | *** |
| Age (years) | +0.0084 | 0.0084 | ±0.0169 | +1.001 | 0.3170 |  |
| BMI (kg/m2) | +0.0219 | 0.0158 | ±0.0316 | +1.386 | 0.1658 |  |
| Hypertension | -0.0897 | 0.2115 | ±0.4231 | -0.424 | 0.6717 |  |
| High cholesterol | -0.3513 | 0.1916 | ±0.3832 | -1.833 | 0.0667 | . |
| **Kidney disease** | **+0.9626** | 0.3753 | ±0.7506 | **+2.565** | **0.0103** | * |
| **Circulatory disease** | **+0.7998** | 0.3601 | ±0.7203 | **+2.221** | **0.0264** | * |
| Avg. daily mean/SD | +0.1191 | 0.0796 | ±0.1592 | +1.497 | 0.1345 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **443**, R² = **0.3418**, Adj R² = **0.3203**, F-statistic = **15.88** (p = **3.33e-31**), Residual SE = **1.892** on **428** df, AIC = **1836.9**, BIC = **1898.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5645** | 1.0729 | ±2.1458 | **+22.895** | **5.16e-116** | *** |
| Education: graduate level (vs college) | +0.0559 | 0.1980 | ±0.3960 | +0.283 | 0.7775 |  |
| Education: high school or below (vs college) | +0.3255 | 0.3608 | ±0.7215 | +0.902 | 0.3669 |  |
| Site: UCSD (vs UAB) | -0.2808 | 0.2356 | ±0.4712 | -1.192 | 0.2332 |  |
| **Site: UW (vs UAB)** | **-1.1092** | 0.2348 | ±0.4696 | **-4.724** | **2.32e-06** | *** |
| Season: spring (vs autumn) | -0.2107 | 0.2733 | ±0.5466 | -0.771 | 0.4409 |  |
| **Season: summer (vs autumn)** | **+1.7869** | 0.3225 | ±0.6451 | **+5.540** | **3.02e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5210** | 0.2814 | ±0.5627 | **-5.406** | **6.44e-08** | *** |
| Age (years) | +0.0070 | 0.0086 | ±0.0172 | +0.810 | 0.4180 |  |
| BMI (kg/m2) | +0.0201 | 0.0159 | ±0.0318 | +1.267 | 0.2053 |  |
| Hypertension | -0.0975 | 0.2117 | ±0.4235 | -0.461 | 0.6451 |  |
| High cholesterol | -0.3356 | 0.1921 | ±0.3841 | -1.747 | 0.0806 | . |
| **Kidney disease** | **+0.9496** | 0.3668 | ±0.7335 | **+2.589** | **0.0096** | ** |
| **Circulatory disease** | **+0.7957** | 0.3580 | ±0.7160 | **+2.223** | **0.0262** | * |
| MAG (mg/dL/h) | -0.0162 | 0.0164 | ±0.0327 | -0.990 | 0.3222 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **443**, R² = **0.3508**, Adj R² = **0.3296**, F-statistic = **16.52** (p = **2.05e-32**), Residual SE = **1.879** on **428** df, AIC = **1830.8**, BIC = **1892.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.6899** | 1.0981 | ±2.1962 | **+23.395** | **4.82e-121** | *** |
| Education: graduate level (vs college) | +0.0369 | 0.1972 | ±0.3944 | +0.187 | 0.8518 |  |
| Education: high school or below (vs college) | +0.3056 | 0.3683 | ±0.7365 | +0.830 | 0.4066 |  |
| Site: UCSD (vs UAB) | -0.3027 | 0.2325 | ±0.4651 | -1.302 | 0.1931 |  |
| **Site: UW (vs UAB)** | **-1.1204** | 0.2323 | ±0.4646 | **-4.823** | **1.41e-06** | *** |
| Season: spring (vs autumn) | -0.1874 | 0.2712 | ±0.5425 | -0.691 | 0.4896 |  |
| **Season: summer (vs autumn)** | **+1.7982** | 0.3179 | ±0.6358 | **+5.657** | **1.54e-08** | *** |
| **Season: winter (vs autumn)** | **-1.4972** | 0.2777 | ±0.5555 | **-5.391** | **7.01e-08** | *** |
| Age (years) | +0.0082 | 0.0083 | ±0.0167 | +0.986 | 0.3242 |  |
| BMI (kg/m2) | +0.0183 | 0.0152 | ±0.0304 | +1.203 | 0.2292 |  |
| Hypertension | -0.1057 | 0.2109 | ±0.4219 | -0.501 | 0.6163 |  |
| High cholesterol | -0.3429 | 0.1903 | ±0.3806 | -1.802 | 0.0715 | . |
| **Kidney disease** | **+0.9788** | 0.3822 | ±0.7644 | **+2.561** | **0.0104** | * |
| **Circulatory disease** | **+0.8058** | 0.3596 | ±0.7192 | **+2.241** | **0.0250** | * |
| **Avg. daily range (mg/dL)** | **-0.0213** | 0.0085 | ±0.0170 | **-2.505** | **0.0122** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **443**, R² = **0.3419**, Adj R² = **0.3204**, F-statistic = **15.88** (p = **3.22e-31**), Residual SE = **1.892** on **428** df, AIC = **1836.9**, BIC = **1898.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6831** | 0.8496 | ±1.6992 | **+27.876** | **5.19e-171** | *** |
| Education: graduate level (vs college) | +0.0450 | 0.1980 | ±0.3960 | +0.227 | 0.8203 |  |
| Education: high school or below (vs college) | +0.2737 | 0.3643 | ±0.7286 | +0.751 | 0.4524 |  |
| Site: UCSD (vs UAB) | -0.2560 | 0.2353 | ±0.4706 | -1.088 | 0.2765 |  |
| **Site: UW (vs UAB)** | **-1.0850** | 0.2346 | ±0.4693 | **-4.624** | **3.76e-06** | *** |
| Season: spring (vs autumn) | -0.2277 | 0.2729 | ±0.5458 | -0.834 | 0.4041 |  |
| **Season: summer (vs autumn)** | **+1.7804** | 0.3216 | ±0.6433 | **+5.536** | **3.10e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5473** | 0.2823 | ±0.5646 | **-5.481** | **4.23e-08** | *** |
| Age (years) | +0.0080 | 0.0085 | ±0.0171 | +0.936 | 0.3494 |  |
| BMI (kg/m2) | +0.0207 | 0.0156 | ±0.0311 | +1.326 | 0.1848 |  |
| Hypertension | -0.1136 | 0.2147 | ±0.4293 | -0.529 | 0.5966 |  |
| High cholesterol | -0.3473 | 0.1905 | ±0.3811 | -1.823 | 0.0683 | . |
| **Kidney disease** | **+0.9322** | 0.3636 | ±0.7271 | **+2.564** | **0.0103** | * |
| **Circulatory disease** | **+0.7804** | 0.3535 | ±0.7071 | **+2.207** | **0.0273** | * |
| SD of daily means (mg/dL) | +0.0526 | 0.0459 | ±0.0919 | +1.144 | 0.2527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **443**, R² = **0.3430**, Adj R² = **0.3215**, F-statistic = **15.96** (p = **2.30e-31**), Residual SE = **1.890** on **428** df, AIC = **1836.1**, BIC = **1897.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -17.1394 | 30.1737 | ±60.3473 | -0.568 | 0.5700 |  |
| Education: graduate level (vs college) | +0.0473 | 0.1979 | ±0.3958 | +0.239 | 0.8110 |  |
| Education: high school or below (vs college) | +0.2919 | 0.3622 | ±0.7243 | +0.806 | 0.4202 |  |
| Site: UCSD (vs UAB) | -0.2914 | 0.2342 | ±0.4683 | -1.244 | 0.2134 |  |
| **Site: UW (vs UAB)** | **-1.1007** | 0.2354 | ±0.4709 | **-4.675** | **2.94e-06** | *** |
| Season: spring (vs autumn) | -0.2078 | 0.2734 | ±0.5469 | -0.760 | 0.4472 |  |
| **Season: summer (vs autumn)** | **+1.8027** | 0.3219 | ±0.6439 | **+5.599** | **2.15e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5099** | 0.2804 | ±0.5608 | **-5.385** | **7.24e-08** | *** |
| Age (years) | +0.0075 | 0.0085 | ±0.0170 | +0.878 | 0.3802 |  |
| BMI (kg/m2) | +0.0201 | 0.0152 | ±0.0305 | +1.317 | 0.1879 |  |
| Hypertension | -0.0897 | 0.2120 | ±0.4240 | -0.423 | 0.6721 |  |
| High cholesterol | -0.3325 | 0.1924 | ±0.3848 | -1.728 | 0.0839 | . |
| **Kidney disease** | **+0.9585** | 0.3758 | ±0.7516 | **+2.551** | **0.0108** | * |
| **Circulatory disease** | **+0.8022** | 0.3608 | ±0.7216 | **+2.223** | **0.0262** | * |
| Time in range 70-180, pooled (%) | +0.4131 | 0.3034 | ±0.6068 | +1.361 | 0.1734 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **443**, R² = **0.3419**, Adj R² = **0.3204**, F-statistic = **15.88** (p = **3.20e-31**), Residual SE = **1.892** on **428** df, AIC = **1836.8**, BIC = **1898.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -7.3655 | 29.8300 | ±59.6600 | -0.247 | 0.8050 |  |
| Education: graduate level (vs college) | +0.0459 | 0.1985 | ±0.3970 | +0.232 | 0.8169 |  |
| Education: high school or below (vs college) | +0.2909 | 0.3629 | ±0.7257 | +0.802 | 0.4228 |  |
| Site: UCSD (vs UAB) | -0.2779 | 0.2349 | ±0.4698 | -1.183 | 0.2367 |  |
| **Site: UW (vs UAB)** | **-1.0873** | 0.2352 | ±0.4705 | **-4.622** | **3.79e-06** | *** |
| Season: spring (vs autumn) | -0.2135 | 0.2734 | ±0.5469 | -0.781 | 0.4350 |  |
| **Season: summer (vs autumn)** | **+1.7872** | 0.3217 | ±0.6433 | **+5.556** | **2.76e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5222** | 0.2808 | ±0.5617 | **-5.420** | **5.95e-08** | *** |
| Age (years) | +0.0075 | 0.0086 | ±0.0171 | +0.872 | 0.3830 |  |
| BMI (kg/m2) | +0.0206 | 0.0157 | ±0.0313 | +1.319 | 0.1872 |  |
| Hypertension | -0.1006 | 0.2125 | ±0.4249 | -0.473 | 0.6359 |  |
| High cholesterol | -0.3301 | 0.1930 | ±0.3860 | -1.710 | 0.0872 | . |
| **Kidney disease** | **+0.9421** | 0.3758 | ±0.7515 | **+2.507** | **0.0122** | * |
| **Circulatory disease** | **+0.8099** | 0.3607 | ±0.7214 | **+2.245** | **0.0247** | * |
| Avg. daily time in range 70-180 (%) | +0.3145 | 0.2999 | ±0.5998 | +1.049 | 0.2943 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.3405**, Adj R² = **0.3189**, F-statistic = **15.78** (p = **5.01e-31**), Residual SE = **1.894** on **428** df, AIC = **1837.8**, BIC = **1899.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9606** | 0.8245 | ±1.6490 | **+29.061** | **1.12e-185** | *** |
| Education: graduate level (vs college) | +0.0510 | 0.1983 | ±0.3966 | +0.257 | 0.7970 |  |
| Education: high school or below (vs college) | +0.2936 | 0.3596 | ±0.7192 | +0.816 | 0.4143 |  |
| Site: UCSD (vs UAB) | -0.2907 | 0.2416 | ±0.4832 | -1.203 | 0.2290 |  |
| **Site: UW (vs UAB)** | **-1.0956** | 0.2407 | ±0.4815 | **-4.551** | **5.34e-06** | *** |
| Season: spring (vs autumn) | -0.1972 | 0.2746 | ±0.5492 | -0.718 | 0.4728 |  |
| **Season: summer (vs autumn)** | **+1.8032** | 0.3197 | ±0.6394 | **+5.640** | **1.70e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5140** | 0.2809 | ±0.5618 | **-5.389** | **7.07e-08** | *** |
| Age (years) | +0.0077 | 0.0085 | ±0.0171 | +0.901 | 0.3678 |  |
| BMI (kg/m2) | +0.0208 | 0.0157 | ±0.0314 | +1.324 | 0.1854 |  |
| Hypertension | -0.0864 | 0.2092 | ±0.4184 | -0.413 | 0.6796 |  |
| High cholesterol | -0.3405 | 0.1914 | ±0.3828 | -1.779 | 0.0753 | . |
| **Kidney disease** | **+0.9151** | 0.3636 | ±0.7273 | **+2.517** | **0.0118** | * |
| **Circulatory disease** | **+0.8115** | 0.3589 | ±0.7179 | **+2.261** | **0.0238** | * |
| Any reading < 54 during wear (0/1) | -0.1142 | 0.2647 | ±0.5294 | -0.432 | 0.6660 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.3403**, Adj R² = **0.3187**, F-statistic = **15.77** (p = **5.32e-31**), Residual SE = **1.894** on **428** df, AIC = **1838.0**, BIC = **1899.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9511** | 0.8237 | ±1.6474 | **+29.077** | **7.04e-186** | *** |
| Education: graduate level (vs college) | +0.0521 | 0.1992 | ±0.3983 | +0.262 | 0.7935 |  |
| Education: high school or below (vs college) | +0.2916 | 0.3602 | ±0.7203 | +0.810 | 0.4181 |  |
| Site: UCSD (vs UAB) | -0.2800 | 0.2376 | ±0.4752 | -1.178 | 0.2386 |  |
| **Site: UW (vs UAB)** | **-1.0889** | 0.2376 | ±0.4752 | **-4.583** | **4.59e-06** | *** |
| Season: spring (vs autumn) | -0.2116 | 0.2740 | ±0.5479 | -0.772 | 0.4399 |  |
| **Season: summer (vs autumn)** | **+1.7955** | 0.3218 | ±0.6435 | **+5.580** | **2.40e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5235** | 0.2813 | ±0.5627 | **-5.415** | **6.13e-08** | *** |
| Age (years) | +0.0076 | 0.0085 | ±0.0170 | +0.892 | 0.3724 |  |
| BMI (kg/m2) | +0.0211 | 0.0158 | ±0.0315 | +1.338 | 0.1808 |  |
| Hypertension | -0.0877 | 0.2077 | ±0.4154 | -0.422 | 0.6730 |  |
| High cholesterol | -0.3423 | 0.1910 | ±0.3819 | -1.792 | 0.0731 | . |
| **Kidney disease** | **+0.9229** | 0.3639 | ±0.7279 | **+2.536** | **0.0112** | * |
| **Circulatory disease** | **+0.8107** | 0.3590 | ±0.7180 | **+2.258** | **0.0239** | * |
| Time < 54 (%) | -0.5017 | 2.5207 | ±5.0414 | -0.199 | 0.8422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.3402**, Adj R² = **0.3186**, F-statistic = **15.76** (p = **5.52e-31**), Residual SE = **1.894** on **428** df, AIC = **1838.0**, BIC = **1899.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9378** | 0.8222 | ±1.6444 | **+29.114** | **2.42e-186** | *** |
| Education: graduate level (vs college) | +0.0521 | 0.1990 | ±0.3981 | +0.262 | 0.7934 |  |
| Education: high school or below (vs college) | +0.2971 | 0.3608 | ±0.7216 | +0.824 | 0.4102 |  |
| Site: UCSD (vs UAB) | -0.2717 | 0.2363 | ±0.4727 | -1.150 | 0.2503 |  |
| **Site: UW (vs UAB)** | **-1.0844** | 0.2360 | ±0.4719 | **-4.596** | **4.31e-06** | *** |
| Season: spring (vs autumn) | -0.2114 | 0.2745 | ±0.5489 | -0.770 | 0.4412 |  |
| **Season: summer (vs autumn)** | **+1.7934** | 0.3214 | ±0.6429 | **+5.579** | **2.41e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5262** | 0.2821 | ±0.5643 | **-5.409** | **6.32e-08** | *** |
| Age (years) | +0.0078 | 0.0086 | ±0.0172 | +0.905 | 0.3654 |  |
| BMI (kg/m2) | +0.0209 | 0.0157 | ±0.0314 | +1.328 | 0.1840 |  |
| Hypertension | -0.0929 | 0.2124 | ±0.4247 | -0.437 | 0.6618 |  |
| High cholesterol | -0.3404 | 0.1914 | ±0.3829 | -1.778 | 0.0754 | . |
| **Kidney disease** | **+0.9275** | 0.3637 | ±0.7275 | **+2.550** | **0.0108** | * |
| **Circulatory disease** | **+0.8090** | 0.3592 | ±0.7184 | **+2.252** | **0.0243** | * |
| Avg. daily time < 54 (%) | -0.1901 | 2.8160 | ±5.6320 | -0.068 | 0.9462 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.3447**, Adj R² = **0.3233**, F-statistic = **16.08** (p = **1.35e-31**), Residual SE = **1.888** on **428** df, AIC = **1835.0**, BIC = **1896.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0663** | 0.8295 | ±1.6591 | **+29.012** | **4.64e-185** | *** |
| Education: graduate level (vs college) | +0.0434 | 0.1980 | ±0.3959 | +0.219 | 0.8263 |  |
| Education: high school or below (vs college) | +0.3317 | 0.3584 | ±0.7168 | +0.925 | 0.3547 |  |
| Site: UCSD (vs UAB) | -0.2967 | 0.2354 | ±0.4708 | -1.260 | 0.2075 |  |
| **Site: UW (vs UAB)** | **-1.1154** | 0.2340 | ±0.4680 | **-4.767** | **1.87e-06** | *** |
| Season: spring (vs autumn) | -0.2013 | 0.2742 | ±0.5485 | -0.734 | 0.4629 |  |
| **Season: summer (vs autumn)** | **+1.8026** | 0.3228 | ±0.6457 | **+5.584** | **2.36e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5032** | 0.2816 | ±0.5633 | **-5.338** | **9.42e-08** | *** |
| Age (years) | +0.0078 | 0.0085 | ±0.0171 | +0.911 | 0.3624 |  |
| BMI (kg/m2) | +0.0207 | 0.0159 | ±0.0318 | +1.304 | 0.1923 |  |
| Hypertension | -0.1139 | 0.2122 | ±0.4245 | -0.537 | 0.5914 |  |
| High cholesterol | -0.3127 | 0.1912 | ±0.3824 | -1.635 | 0.1020 |  |
| **Kidney disease** | **+0.8787** | 0.3678 | ±0.7356 | **+2.389** | **0.0169** | * |
| **Circulatory disease** | **+0.8007** | 0.3582 | ±0.7164 | **+2.235** | **0.0254** | * |
| Time 54-69, pooled (%) | -0.8674 | 0.4949 | ±0.9898 | -1.753 | 0.0796 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **443**, R² = **0.3425**, Adj R² = **0.3210**, F-statistic = **15.93** (p = **2.65e-31**), Residual SE = **1.891** on **428** df, AIC = **1836.4**, BIC = **1897.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0185** | 0.8256 | ±1.6513 | **+29.091** | **4.68e-186** | *** |
| Education: graduate level (vs college) | +0.0410 | 0.1984 | ±0.3968 | +0.207 | 0.8363 |  |
| Education: high school or below (vs college) | +0.3242 | 0.3575 | ±0.7150 | +0.907 | 0.3645 |  |
| Site: UCSD (vs UAB) | -0.2799 | 0.2354 | ±0.4708 | -1.189 | 0.2345 |  |
| **Site: UW (vs UAB)** | **-1.0970** | 0.2341 | ±0.4682 | **-4.686** | **2.79e-06** | *** |
| Season: spring (vs autumn) | -0.2183 | 0.2736 | ±0.5471 | -0.798 | 0.4249 |  |
| **Season: summer (vs autumn)** | **+1.7833** | 0.3221 | ±0.6441 | **+5.537** | **3.07e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5166** | 0.2823 | ±0.5645 | **-5.373** | **7.75e-08** | *** |
| Age (years) | +0.0079 | 0.0085 | ±0.0171 | +0.928 | 0.3534 |  |
| BMI (kg/m2) | +0.0208 | 0.0158 | ±0.0316 | +1.319 | 0.1873 |  |
| Hypertension | -0.1231 | 0.2115 | ±0.4229 | -0.582 | 0.5606 |  |
| High cholesterol | -0.3222 | 0.1919 | ±0.3837 | -1.679 | 0.0931 | . |
| **Kidney disease** | **+0.9035** | 0.3677 | ±0.7354 | **+2.457** | **0.0140** | * |
| **Circulatory disease** | **+0.8112** | 0.3582 | ±0.7165 | **+2.264** | **0.0235** | * |
| Avg. daily time 54-69 (%) | -0.6371 | 0.4792 | ±0.9584 | -1.329 | 0.1837 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **443**, R² = **0.3441**, Adj R² = **0.3227**, F-statistic = **16.04** (p = **1.62e-31**), Residual SE = **1.889** on **428** df, AIC = **1835.4**, BIC = **1896.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0672** | 0.8316 | ±1.6631 | **+28.942** | **3.56e-184** | *** |
| Education: graduate level (vs college) | +0.0451 | 0.1984 | ±0.3968 | +0.227 | 0.8201 |  |
| Education: high school or below (vs college) | +0.3169 | 0.3580 | ±0.7161 | +0.885 | 0.3761 |  |
| Site: UCSD (vs UAB) | -0.3059 | 0.2351 | ±0.4703 | -1.301 | 0.1933 |  |
| **Site: UW (vs UAB)** | **-1.1169** | 0.2349 | ±0.4698 | **-4.754** | **1.99e-06** | *** |
| Season: spring (vs autumn) | -0.2041 | 0.2742 | ±0.5485 | -0.744 | 0.4568 |  |
| **Season: summer (vs autumn)** | **+1.8023** | 0.3230 | ±0.6459 | **+5.581** | **2.40e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5035** | 0.2815 | ±0.5629 | **-5.342** | **9.20e-08** | *** |
| Age (years) | +0.0075 | 0.0085 | ±0.0171 | +0.876 | 0.3808 |  |
| BMI (kg/m2) | +0.0212 | 0.0160 | ±0.0319 | +1.325 | 0.1852 |  |
| Hypertension | -0.1021 | 0.2129 | ±0.4257 | -0.480 | 0.6315 |  |
| High cholesterol | -0.3201 | 0.1917 | ±0.3834 | -1.669 | 0.0950 | . |
| **Kidney disease** | **+0.8793** | 0.3671 | ±0.7342 | **+2.395** | **0.0166** | * |
| **Circulatory disease** | **+0.8065** | 0.3585 | ±0.7169 | **+2.250** | **0.0245** | * |
| Time < 70 (%) | -0.7209 | 0.4632 | ±0.9264 | -1.556 | 0.1196 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **443**, R² = **0.3422**, Adj R² = **0.3207**, F-statistic = **15.90** (p = **2.94e-31**), Residual SE = **1.892** on **428** df, AIC = **1836.7**, BIC = **1898.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0138** | 0.8262 | ±1.6523 | **+29.067** | **9.51e-186** | *** |
| Education: graduate level (vs college) | +0.0432 | 0.1985 | ±0.3970 | +0.218 | 0.8278 |  |
| Education: high school or below (vs college) | +0.3180 | 0.3581 | ±0.7162 | +0.888 | 0.3745 |  |
| Site: UCSD (vs UAB) | -0.2819 | 0.2353 | ±0.4707 | -1.198 | 0.2310 |  |
| **Site: UW (vs UAB)** | **-1.0957** | 0.2345 | ±0.4691 | **-4.672** | **2.99e-06** | *** |
| Season: spring (vs autumn) | -0.2189 | 0.2736 | ±0.5473 | -0.800 | 0.4237 |  |
| **Season: summer (vs autumn)** | **+1.7811** | 0.3223 | ±0.6445 | **+5.527** | **3.26e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5186** | 0.2821 | ±0.5641 | **-5.384** | **7.28e-08** | *** |
| Age (years) | +0.0078 | 0.0085 | ±0.0171 | +0.917 | 0.3592 |  |
| BMI (kg/m2) | +0.0209 | 0.0158 | ±0.0316 | +1.324 | 0.1857 |  |
| Hypertension | -0.1168 | 0.2118 | ±0.4236 | -0.551 | 0.5813 |  |
| High cholesterol | -0.3250 | 0.1919 | ±0.3839 | -1.693 | 0.0904 | . |
| **Kidney disease** | **+0.9049** | 0.3673 | ±0.7345 | **+2.464** | **0.0137** | * |
| **Circulatory disease** | **+0.8147** | 0.3586 | ±0.7171 | **+2.272** | **0.0231** | * |
| Avg. daily time < 70 (%) | -0.5401 | 0.4387 | ±0.8775 | -1.231 | 0.2183 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.3403**, Adj R² = **0.3188**, F-statistic = **15.77** (p = **5.22e-31**), Residual SE = **1.894** on **428** df, AIC = **1837.9**, BIC = **1899.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -35.8153 | 239.6112 | ±479.2223 | -0.149 | 0.8812 |  |
| Education: graduate level (vs college) | +0.0522 | 0.1992 | ±0.3983 | +0.262 | 0.7932 |  |
| Education: high school or below (vs college) | +0.2902 | 0.3601 | ±0.7202 | +0.806 | 0.4203 |  |
| Site: UCSD (vs UAB) | -0.2827 | 0.2380 | ±0.4760 | -1.188 | 0.2350 |  |
| **Site: UW (vs UAB)** | **-1.0905** | 0.2379 | ±0.4757 | **-4.585** | **4.54e-06** | *** |
| Season: spring (vs autumn) | -0.2112 | 0.2739 | ±0.5478 | -0.771 | 0.4408 |  |
| **Season: summer (vs autumn)** | **+1.7956** | 0.3218 | ±0.6436 | **+5.580** | **2.40e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5225** | 0.2813 | ±0.5625 | **-5.413** | **6.19e-08** | *** |
| Age (years) | +0.0075 | 0.0085 | ±0.0170 | +0.883 | 0.3775 |  |
| BMI (kg/m2) | +0.0211 | 0.0158 | ±0.0315 | +1.341 | 0.1800 |  |
| Hypertension | -0.0868 | 0.2080 | ±0.4159 | -0.418 | 0.6763 |  |
| High cholesterol | -0.3425 | 0.1910 | ±0.3820 | -1.793 | 0.0730 | . |
| **Kidney disease** | **+0.9220** | 0.3638 | ±0.7276 | **+2.534** | **0.0113** | * |
| **Circulatory disease** | **+0.8115** | 0.3590 | ±0.7180 | **+2.260** | **0.0238** | * |
| Time 54-250, pooled (%) | +0.5977 | 2.3966 | ±4.7932 | +0.249 | 0.8030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.3402**, Adj R² = **0.3186**, F-statistic = **15.76** (p = **5.45e-31**), Residual SE = **1.894** on **428** df, AIC = **1838.0**, BIC = **1899.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -17.3252 | 274.3416 | ±548.6832 | -0.063 | 0.9496 |  |
| Education: graduate level (vs college) | +0.0524 | 0.1990 | ±0.3981 | +0.263 | 0.7925 |  |
| Education: high school or below (vs college) | +0.2960 | 0.3608 | ±0.7216 | +0.821 | 0.4119 |  |
| Site: UCSD (vs UAB) | -0.2738 | 0.2366 | ±0.4733 | -1.157 | 0.2473 |  |
| **Site: UW (vs UAB)** | **-1.0852** | 0.2361 | ±0.4722 | **-4.596** | **4.30e-06** | *** |
| Season: spring (vs autumn) | -0.2117 | 0.2745 | ±0.5490 | -0.771 | 0.4407 |  |
| **Season: summer (vs autumn)** | **+1.7917** | 0.3215 | ±0.6431 | **+5.572** | **2.51e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5260** | 0.2823 | ±0.5646 | **-5.406** | **6.46e-08** | *** |
| Age (years) | +0.0077 | 0.0086 | ±0.0172 | +0.898 | 0.3691 |  |
| BMI (kg/m2) | +0.0209 | 0.0157 | ±0.0314 | +1.329 | 0.1839 |  |
| Hypertension | -0.0924 | 0.2123 | ±0.4247 | -0.435 | 0.6636 |  |
| High cholesterol | -0.3403 | 0.1915 | ±0.3830 | -1.777 | 0.0756 | . |
| **Kidney disease** | **+0.9265** | 0.3638 | ±0.7276 | **+2.547** | **0.0109** | * |
| **Circulatory disease** | **+0.8107** | 0.3593 | ±0.7186 | **+2.256** | **0.0241** | * |
| Avg. daily time 54-250 (%) | +0.4127 | 2.7438 | ±5.4877 | +0.150 | 0.8804 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **443**, R² = **0.3403**, Adj R² = **0.3187**, F-statistic = **15.77** (p = **5.34e-31**), Residual SE = **1.894** on **428** df, AIC = **1838.0**, BIC = **1899.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9685** | 0.8328 | ±1.6656 | **+28.780** | **3.76e-182** | *** |
| Education: graduate level (vs college) | +0.0518 | 0.1983 | ±0.3966 | +0.261 | 0.7940 |  |
| Education: high school or below (vs college) | +0.2943 | 0.3632 | ±0.7264 | +0.810 | 0.4178 |  |
| Site: UCSD (vs UAB) | -0.2705 | 0.2358 | ±0.4716 | -1.147 | 0.2513 |  |
| **Site: UW (vs UAB)** | **-1.0836** | 0.2351 | ±0.4701 | **-4.610** | **4.03e-06** | *** |
| Season: spring (vs autumn) | -0.2111 | 0.2733 | ±0.5467 | -0.772 | 0.4400 |  |
| **Season: summer (vs autumn)** | **+1.7956** | 0.3209 | ±0.6418 | **+5.596** | **2.20e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5253** | 0.2814 | ±0.5628 | **-5.421** | **5.93e-08** | *** |
| Age (years) | +0.0078 | 0.0086 | ±0.0171 | +0.906 | 0.3648 |  |
| BMI (kg/m2) | +0.0206 | 0.0156 | ±0.0312 | +1.320 | 0.1870 |  |
| Hypertension | -0.0916 | 0.2117 | ±0.4234 | -0.433 | 0.6654 |  |
| High cholesterol | -0.3413 | 0.1908 | ±0.3815 | -1.789 | 0.0736 | . |
| **Kidney disease** | **+0.9411** | 0.3653 | ±0.7306 | **+2.576** | **0.0100** | ** |
| **Circulatory disease** | **+0.8065** | 0.3582 | ±0.7165 | **+2.251** | **0.0244** | * |
| Time 181-250, pooled (%) | -0.0906 | 0.3278 | ±0.6556 | -0.276 | 0.7822 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **443**, R² = **0.3404**, Adj R² = **0.3188**, F-statistic = **15.77** (p = **5.19e-31**), Residual SE = **1.894** on **428** df, AIC = **1837.9**, BIC = **1899.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9746** | 0.8314 | ±1.6628 | **+28.836** | **7.60e-183** | *** |
| Education: graduate level (vs college) | +0.0516 | 0.1983 | ±0.3966 | +0.260 | 0.7947 |  |
| Education: high school or below (vs college) | +0.2909 | 0.3644 | ±0.7288 | +0.798 | 0.4247 |  |
| Site: UCSD (vs UAB) | -0.2706 | 0.2358 | ±0.4715 | -1.148 | 0.2510 |  |
| **Site: UW (vs UAB)** | **-1.0827** | 0.2351 | ±0.4702 | **-4.605** | **4.12e-06** | *** |
| Season: spring (vs autumn) | -0.2101 | 0.2734 | ±0.5468 | -0.769 | 0.4421 |  |
| **Season: summer (vs autumn)** | **+1.7950** | 0.3208 | ±0.6415 | **+5.596** | **2.20e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5262** | 0.2812 | ±0.5624 | **-5.427** | **5.72e-08** | *** |
| Age (years) | +0.0077 | 0.0086 | ±0.0172 | +0.892 | 0.3722 |  |
| BMI (kg/m2) | +0.0207 | 0.0156 | ±0.0313 | +1.327 | 0.1846 |  |
| Hypertension | -0.0910 | 0.2121 | ±0.4243 | -0.429 | 0.6680 |  |
| High cholesterol | -0.3399 | 0.1915 | ±0.3830 | -1.775 | 0.0759 | . |
| **Kidney disease** | **+0.9387** | 0.3673 | ±0.7346 | **+2.555** | **0.0106** | * |
| **Circulatory disease** | **+0.8068** | 0.3585 | ±0.7170 | **+2.251** | **0.0244** | * |
| Avg. daily time 181-250 (%) | -0.1193 | 0.3266 | ±0.6532 | -0.365 | 0.7150 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **443**, R² = **0.3403**, Adj R² = **0.3187**, F-statistic = **15.77** (p = **5.32e-31**), Residual SE = **1.894** on **428** df, AIC = **1838.0**, BIC = **1899.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9706** | 0.8332 | ±1.6663 | **+28.771** | **4.98e-182** | *** |
| Education: graduate level (vs college) | +0.0518 | 0.1983 | ±0.3966 | +0.261 | 0.7940 |  |
| Education: high school or below (vs college) | +0.2941 | 0.3632 | ±0.7265 | +0.810 | 0.4182 |  |
| Site: UCSD (vs UAB) | -0.2706 | 0.2358 | ±0.4716 | -1.148 | 0.2511 |  |
| **Site: UW (vs UAB)** | **-1.0837** | 0.2351 | ±0.4701 | **-4.610** | **4.02e-06** | *** |
| Season: spring (vs autumn) | -0.2110 | 0.2733 | ±0.5467 | -0.772 | 0.4402 |  |
| **Season: summer (vs autumn)** | **+1.7956** | 0.3209 | ±0.6418 | **+5.596** | **2.20e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5252** | 0.2814 | ±0.5627 | **-5.421** | **5.94e-08** | *** |
| Age (years) | +0.0078 | 0.0086 | ±0.0171 | +0.905 | 0.3653 |  |
| BMI (kg/m2) | +0.0206 | 0.0156 | ±0.0312 | +1.319 | 0.1871 |  |
| Hypertension | -0.0915 | 0.2117 | ±0.4234 | -0.432 | 0.6655 |  |
| High cholesterol | -0.3413 | 0.1908 | ±0.3815 | -1.789 | 0.0736 | . |
| **Kidney disease** | **+0.9417** | 0.3654 | ±0.7308 | **+2.577** | **0.0100** | ** |
| **Circulatory disease** | **+0.8065** | 0.3583 | ±0.7165 | **+2.251** | **0.0244** | * |
| Time > 180 (%) | -0.0947 | 0.3268 | ±0.6537 | -0.290 | 0.7720 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **443**, R² = **0.3404**, Adj R² = **0.3188**, F-statistic = **15.78** (p = **5.16e-31**), Residual SE = **1.894** on **428** df, AIC = **1837.9**, BIC = **1899.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9769** | 0.8319 | ±1.6638 | **+28.822** | **1.15e-182** | *** |
| Education: graduate level (vs college) | +0.0516 | 0.1983 | ±0.3966 | +0.260 | 0.7947 |  |
| Education: high school or below (vs college) | +0.2906 | 0.3644 | ±0.7289 | +0.797 | 0.4252 |  |
| Site: UCSD (vs UAB) | -0.2708 | 0.2357 | ±0.4715 | -1.149 | 0.2506 |  |
| **Site: UW (vs UAB)** | **-1.0828** | 0.2351 | ±0.4702 | **-4.606** | **4.11e-06** | *** |
| Season: spring (vs autumn) | -0.2100 | 0.2734 | ±0.5468 | -0.768 | 0.4425 |  |
| **Season: summer (vs autumn)** | **+1.7950** | 0.3208 | ±0.6415 | **+5.596** | **2.20e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5261** | 0.2812 | ±0.5624 | **-5.427** | **5.72e-08** | *** |
| Age (years) | +0.0077 | 0.0086 | ±0.0172 | +0.891 | 0.3731 |  |
| BMI (kg/m2) | +0.0207 | 0.0156 | ±0.0313 | +1.326 | 0.1848 |  |
| Hypertension | -0.0910 | 0.2121 | ±0.4243 | -0.429 | 0.6681 |  |
| High cholesterol | -0.3399 | 0.1915 | ±0.3830 | -1.775 | 0.0759 | . |
| **Kidney disease** | **+0.9391** | 0.3675 | ±0.7349 | **+2.556** | **0.0106** | * |
| **Circulatory disease** | **+0.8068** | 0.3585 | ±0.7170 | **+2.251** | **0.0244** | * |
| Avg. daily time > 180 (%) | -0.1234 | 0.3252 | ±0.6503 | -0.380 | 0.7043 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **443**, R² = **0.3408**, Adj R² = **0.3192**, F-statistic = **15.80** (p = **4.54e-31**), Residual SE = **1.894** on **428** df, AIC = **1837.6**, BIC = **1899.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8870** | 0.8228 | ±1.6455 | **+29.033** | **2.53e-185** | *** |
| Education: graduate level (vs college) | +0.0584 | 0.1990 | ±0.3981 | +0.293 | 0.7691 |  |
| Education: high school or below (vs college) | +0.3020 | 0.3602 | ±0.7204 | +0.839 | 0.4017 |  |
| Site: UCSD (vs UAB) | -0.2708 | 0.2356 | ±0.4712 | -1.150 | 0.2503 |  |
| **Site: UW (vs UAB)** | **-1.0888** | 0.2346 | ±0.4692 | **-4.641** | **3.46e-06** | *** |
| Season: spring (vs autumn) | -0.2141 | 0.2728 | ±0.5455 | -0.785 | 0.4324 |  |
| **Season: summer (vs autumn)** | **+1.7981** | 0.3205 | ±0.6410 | **+5.610** | **2.02e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5412** | 0.2820 | ±0.5640 | **-5.465** | **4.62e-08** | *** |
| Age (years) | +0.0087 | 0.0087 | ±0.0175 | +0.995 | 0.3198 |  |
| BMI (kg/m2) | +0.0203 | 0.0156 | ±0.0313 | +1.297 | 0.1945 |  |
| Hypertension | -0.1061 | 0.2138 | ±0.4276 | -0.496 | 0.6198 |  |
| High cholesterol | -0.3438 | 0.1911 | ±0.3822 | -1.800 | 0.0719 | . |
| **Kidney disease** | **+0.9268** | 0.3641 | ±0.7281 | **+2.546** | **0.0109** | * |
| **Circulatory disease** | **+0.8148** | 0.3565 | ±0.7131 | **+2.285** | **0.0223** | * |
| Nocturnal time > 180 (%) | +0.1683 | 0.2121 | ±0.4242 | +0.793 | 0.4276 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 443; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **443**, R² = **0.2738**, Adj R² = **0.2518**, F-statistic = **12.44** (p = **3.37e-23**), Residual SE = **5.773** on **429** df, AIC = **2824.3**, BIC = **2881.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.7088** | 2.0049 | ±4.0098 | **+23.796** | **3.65e-125** | *** |
| Education: graduate level (vs college) | +0.8567 | 0.5853 | ±1.1707 | +1.464 | 0.1433 |  |
| Education: high school or below (vs college) | -0.9511 | 1.1068 | ±2.2137 | -0.859 | 0.3902 |  |
| **Site: UCSD (vs UAB)** | **+4.2304** | 0.7382 | ±1.4764 | **+5.731** | **9.99e-09** | *** |
| Site: UW (vs UAB) | -0.6757 | 0.7286 | ±1.4572 | -0.927 | 0.3537 |  |
| Season: spring (vs autumn) | -1.3297 | 0.7771 | ±1.5542 | -1.711 | 0.0871 | . |
| **Season: summer (vs autumn)** | **+3.1606** | 0.8448 | ±1.6896 | **+3.741** | **1.83e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5582** | 0.8665 | ±1.7330 | **-5.260** | **1.44e-07** | *** |
| Age (years) | -0.0344 | 0.0256 | ±0.0512 | -1.342 | 0.1797 |  |
| BMI (kg/m2) | -0.0302 | 0.0379 | ±0.0758 | -0.796 | 0.4263 |  |
| Hypertension | +0.2675 | 0.6471 | ±1.2942 | +0.413 | 0.6794 |  |
| High cholesterol | -0.8454 | 0.5921 | ±1.1841 | -1.428 | 0.1533 |  |
| Kidney disease | -1.1618 | 1.1552 | ±2.3105 | -1.006 | 0.3146 |  |
| Circulatory disease | -0.5109 | 0.8237 | ±1.6475 | -0.620 | 0.5351 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **443**, R² = **0.2761**, Adj R² = **0.2524**, F-statistic = **11.66** (p = **6.66e-23**), Residual SE = **5.771** on **428** df, AIC = **2825.0**, BIC = **2886.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.0700** | 5.1759 | ±10.3517 | **+8.128** | **4.36e-16** | *** |
| Education: graduate level (vs college) | +0.8829 | 0.5852 | ±1.1704 | +1.509 | 0.1313 |  |
| Education: high school or below (vs college) | -1.0292 | 1.1041 | ±2.2083 | -0.932 | 0.3513 |  |
| **Site: UCSD (vs UAB)** | **+4.2177** | 0.7387 | ±1.4774 | **+5.710** | **1.13e-08** | *** |
| Site: UW (vs UAB) | -0.6616 | 0.7252 | ±1.4503 | -0.912 | 0.3616 |  |
| Season: spring (vs autumn) | -1.1894 | 0.7800 | ±1.5601 | -1.525 | 0.1273 |  |
| **Season: summer (vs autumn)** | **+3.1077** | 0.8462 | ±1.6925 | **+3.672** | **2.40e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5068** | 0.8669 | ±1.7337 | **-5.199** | **2.00e-07** | *** |
| Age (years) | -0.0375 | 0.0263 | ±0.0526 | -1.427 | 0.1537 |  |
| BMI (kg/m2) | -0.0357 | 0.0383 | ±0.0765 | -0.934 | 0.3505 |  |
| Hypertension | +0.2053 | 0.6500 | ±1.3001 | +0.316 | 0.7522 |  |
| High cholesterol | -0.9872 | 0.6022 | ±1.2043 | -1.639 | 0.1011 |  |
| Kidney disease | -1.0936 | 1.1696 | ±2.3392 | -0.935 | 0.3498 |  |
| Circulatory disease | -0.4533 | 0.8171 | ±1.6343 | -0.555 | 0.5791 |  |
| HbA1c (%) | +1.0829 | 0.9541 | ±1.9081 | +1.135 | 0.2564 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **443**, R² = **0.2745**, Adj R² = **0.2508**, F-statistic = **11.57** (p = **1.02e-22**), Residual SE = **5.777** on **428** df, AIC = **2825.9**, BIC = **2887.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.1019** | 4.8596 | ±9.7191 | **+9.281** | **1.68e-20** | *** |
| Education: graduate level (vs college) | +0.8516 | 0.5853 | ±1.1705 | +1.455 | 0.1456 |  |
| Education: high school or below (vs college) | -0.9286 | 1.1189 | ±2.2377 | -0.830 | 0.4066 |  |
| **Site: UCSD (vs UAB)** | **+4.2094** | 0.7389 | ±1.4778 | **+5.697** | **1.22e-08** | *** |
| Site: UW (vs UAB) | -0.7007 | 0.7302 | ±1.4604 | -0.960 | 0.3373 |  |
| Season: spring (vs autumn) | -1.3076 | 0.7790 | ±1.5579 | -1.679 | 0.0932 | . |
| **Season: summer (vs autumn)** | **+3.1636** | 0.8482 | ±1.6965 | **+3.730** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5417** | 0.8674 | ±1.7349 | **-5.236** | **1.64e-07** | *** |
| Age (years) | -0.0339 | 0.0257 | ±0.0513 | -1.320 | 0.1867 |  |
| BMI (kg/m2) | -0.0317 | 0.0379 | ±0.0757 | -0.837 | 0.4028 |  |
| Hypertension | +0.2449 | 0.6553 | ±1.3105 | +0.374 | 0.7086 |  |
| High cholesterol | -0.8313 | 0.5941 | ±1.1882 | -1.399 | 0.1618 |  |
| Kidney disease | -1.1858 | 1.1552 | ±2.3104 | -1.026 | 0.3047 |  |
| Circulatory disease | -0.5139 | 0.8232 | ±1.6463 | -0.624 | 0.5324 |  |
| Mean glucose (mg/dL) | +0.0230 | 0.0368 | ±0.0735 | +0.626 | 0.5311 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **443**, R² = **0.2745**, Adj R² = **0.2508**, F-statistic = **11.57** (p = **1.02e-22**), Residual SE = **5.777** on **428** df, AIC = **2825.9**, BIC = **2887.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.9167** | 9.7261 | ±19.4522 | **+4.310** | **1.63e-05** | *** |
| Education: graduate level (vs college) | +0.8516 | 0.5853 | ±1.1705 | +1.455 | 0.1456 |  |
| Education: high school or below (vs college) | -0.9286 | 1.1189 | ±2.2377 | -0.830 | 0.4066 |  |
| **Site: UCSD (vs UAB)** | **+4.2094** | 0.7389 | ±1.4778 | **+5.697** | **1.22e-08** | *** |
| Site: UW (vs UAB) | -0.7007 | 0.7302 | ±1.4604 | -0.960 | 0.3373 |  |
| Season: spring (vs autumn) | -1.3076 | 0.7790 | ±1.5579 | -1.679 | 0.0932 | . |
| **Season: summer (vs autumn)** | **+3.1636** | 0.8482 | ±1.6965 | **+3.730** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5417** | 0.8674 | ±1.7349 | **-5.236** | **1.64e-07** | *** |
| Age (years) | -0.0339 | 0.0257 | ±0.0513 | -1.320 | 0.1867 |  |
| BMI (kg/m2) | -0.0317 | 0.0379 | ±0.0757 | -0.837 | 0.4028 |  |
| Hypertension | +0.2449 | 0.6553 | ±1.3105 | +0.374 | 0.7086 |  |
| High cholesterol | -0.8313 | 0.5941 | ±1.1882 | -1.399 | 0.1618 |  |
| Kidney disease | -1.1858 | 1.1552 | ±2.3104 | -1.026 | 0.3047 |  |
| Circulatory disease | -0.5139 | 0.8232 | ±1.6463 | -0.624 | 0.5324 |  |
| GMI (%) | +0.9623 | 1.5365 | ±3.0729 | +0.626 | 0.5311 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **443**, R² = **0.2773**, Adj R² = **0.2536**, F-statistic = **11.73** (p = **4.77e-23**), Residual SE = **5.766** on **428** df, AIC = **2824.2**, BIC = **2885.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.8934** | 4.0928 | ±8.1857 | **+10.480** | **1.07e-25** | *** |
| Education: graduate level (vs college) | +0.8823 | 0.5870 | ±1.1740 | +1.503 | 0.1328 |  |
| Education: high school or below (vs college) | -0.8848 | 1.1264 | ±2.2528 | -0.785 | 0.4322 |  |
| **Site: UCSD (vs UAB)** | **+4.1322** | 0.7399 | ±1.4799 | **+5.585** | **2.34e-08** | *** |
| Site: UW (vs UAB) | -0.7631 | 0.7291 | ±1.4582 | -1.047 | 0.2953 |  |
| Season: spring (vs autumn) | -1.2948 | 0.7781 | ±1.5562 | -1.664 | 0.0961 | . |
| **Season: summer (vs autumn)** | **+3.1597** | 0.8491 | ±1.6982 | **+3.721** | **1.98e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5401** | 0.8691 | ±1.7382 | **-5.224** | **1.75e-07** | *** |
| Age (years) | -0.0292 | 0.0261 | ±0.0522 | -1.118 | 0.2635 |  |
| BMI (kg/m2) | -0.0390 | 0.0382 | ±0.0764 | -1.020 | 0.3079 |  |
| Hypertension | +0.2154 | 0.6517 | ±1.3033 | +0.330 | 0.7410 |  |
| High cholesterol | -0.8359 | 0.5921 | ±1.1842 | -1.412 | 0.1580 |  |
| Kidney disease | -1.1268 | 1.1556 | ±2.3112 | -0.975 | 0.3295 |  |
| Circulatory disease | -0.4966 | 0.8138 | ±1.6277 | -0.610 | 0.5417 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0418 | 0.0284 | ±0.0567 | +1.473 | 0.1408 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **443**, R² = **0.2747**, Adj R² = **0.2509**, F-statistic = **11.58** (p = **9.75e-23**), Residual SE = **5.777** on **428** df, AIC = **2825.8**, BIC = **2887.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.0345** | 2.7877 | ±5.5754 | **+17.590** | **2.95e-69** | *** |
| Education: graduate level (vs college) | +0.8341 | 0.5887 | ±1.1775 | +1.417 | 0.1566 |  |
| Education: high school or below (vs college) | -0.9419 | 1.1041 | ±2.2081 | -0.853 | 0.3936 |  |
| **Site: UCSD (vs UAB)** | **+4.2004** | 0.7419 | ±1.4839 | **+5.661** | **1.50e-08** | *** |
| Site: UW (vs UAB) | -0.7076 | 0.7343 | ±1.4685 | -0.964 | 0.3352 |  |
| Season: spring (vs autumn) | -1.3069 | 0.7788 | ±1.5576 | -1.678 | 0.0933 | . |
| **Season: summer (vs autumn)** | **+3.1676** | 0.8481 | ±1.6962 | **+3.735** | **1.88e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5260** | 0.8703 | ±1.7406 | **-5.201** | **1.99e-07** | *** |
| Age (years) | -0.0340 | 0.0257 | ±0.0515 | -1.321 | 0.1864 |  |
| BMI (kg/m2) | -0.0290 | 0.0380 | ±0.0760 | -0.763 | 0.4456 |  |
| Hypertension | +0.2947 | 0.6560 | ±1.3120 | +0.449 | 0.6532 |  |
| High cholesterol | -0.8691 | 0.5989 | ±1.1977 | -1.451 | 0.1467 |  |
| Kidney disease | -1.0903 | 1.1611 | ±2.3221 | -0.939 | 0.3477 |  |
| Circulatory disease | -0.4891 | 0.8255 | ±1.6511 | -0.592 | 0.5536 |  |
| Glucose SD, pooled (mg/dL) | -0.0819 | 0.1228 | ±0.2456 | -0.667 | 0.5046 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **443**, R² = **0.2739**, Adj R² = **0.2502**, F-statistic = **11.53** (p = **1.19e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.3**, BIC = **2887.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.1134** | 2.6831 | ±5.3661 | **+17.932** | **6.60e-72** | *** |
| Education: graduate level (vs college) | +0.8472 | 0.5889 | ±1.1777 | +1.439 | 0.1502 |  |
| Education: high school or below (vs college) | -0.9529 | 1.1063 | ±2.2126 | -0.861 | 0.3891 |  |
| **Site: UCSD (vs UAB)** | **+4.2229** | 0.7406 | ±1.4811 | **+5.702** | **1.18e-08** | *** |
| Site: UW (vs UAB) | -0.6846 | 0.7316 | ±1.4632 | -0.936 | 0.3494 |  |
| Season: spring (vs autumn) | -1.3247 | 0.7792 | ±1.5584 | -1.700 | 0.0891 | . |
| **Season: summer (vs autumn)** | **+3.1609** | 0.8476 | ±1.6952 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5537** | 0.8690 | ±1.7380 | **-5.240** | **1.60e-07** | *** |
| Age (years) | -0.0341 | 0.0257 | ±0.0514 | -1.328 | 0.1843 |  |
| BMI (kg/m2) | -0.0295 | 0.0380 | ±0.0761 | -0.774 | 0.4387 |  |
| Hypertension | +0.2731 | 0.6536 | ±1.3072 | +0.418 | 0.6761 |  |
| High cholesterol | -0.8526 | 0.5982 | ±1.1964 | -1.425 | 0.1541 |  |
| Kidney disease | -1.1379 | 1.1584 | ±2.3168 | -0.982 | 0.3259 |  |
| Circulatory disease | -0.5097 | 0.8259 | ±1.6518 | -0.617 | 0.5372 |  |
| Avg. daily SD (mg/dL) | -0.0281 | 0.1241 | ±0.2481 | -0.226 | 0.8210 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **443**, R² = **0.2751**, Adj R² = **0.2514**, F-statistic = **11.60** (p = **8.72e-23**), Residual SE = **5.775** on **428** df, AIC = **2825.6**, BIC = **2887.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.2931** | 2.6935 | ±5.3870 | **+18.301** | **8.16e-75** | *** |
| Education: graduate level (vs college) | +0.8266 | 0.5874 | ±1.1747 | +1.407 | 0.1593 |  |
| Education: high school or below (vs college) | -0.9274 | 1.1079 | ±2.2159 | -0.837 | 0.4026 |  |
| **Site: UCSD (vs UAB)** | **+4.1821** | 0.7418 | ±1.4836 | **+5.638** | **1.72e-08** | *** |
| Site: UW (vs UAB) | -0.7291 | 0.7360 | ±1.4720 | -0.991 | 0.3219 |  |
| Season: spring (vs autumn) | -1.2877 | 0.7789 | ±1.5579 | -1.653 | 0.0983 | . |
| **Season: summer (vs autumn)** | **+3.1747** | 0.8493 | ±1.6986 | **+3.738** | **1.85e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5087** | 0.8697 | ±1.7394 | **-5.184** | **2.17e-07** | *** |
| Age (years) | -0.0337 | 0.0258 | ±0.0515 | -1.308 | 0.1907 |  |
| BMI (kg/m2) | -0.0297 | 0.0380 | ±0.0760 | -0.782 | 0.4342 |  |
| Hypertension | +0.2844 | 0.6519 | ±1.3038 | +0.436 | 0.6627 |  |
| High cholesterol | -0.8660 | 0.5968 | ±1.1936 | -1.451 | 0.1467 |  |
| Kidney disease | -1.0938 | 1.1599 | ±2.3199 | -0.943 | 0.3457 |  |
| Circulatory disease | -0.4851 | 0.8254 | ±1.6508 | -0.588 | 0.5567 |  |
| CV (%) | -0.1104 | 0.1376 | ±0.2752 | -0.802 | 0.4225 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **443**, R² = **0.2754**, Adj R² = **0.2517**, F-statistic = **11.62** (p = **8.00e-23**), Residual SE = **5.774** on **428** df, AIC = **2825.4**, BIC = **2886.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.9282** | 2.8843 | ±5.7686 | **+15.924** | **4.35e-57** | *** |
| Education: graduate level (vs college) | +0.8179 | 0.5871 | ±1.1742 | +1.393 | 0.1636 |  |
| Education: high school or below (vs college) | -0.9195 | 1.1077 | ±2.2154 | -0.830 | 0.4065 |  |
| **Site: UCSD (vs UAB)** | **+4.1855** | 0.7420 | ±1.4840 | **+5.641** | **1.69e-08** | *** |
| Site: UW (vs UAB) | -0.7266 | 0.7356 | ±1.4713 | -0.988 | 0.3233 |  |
| Season: spring (vs autumn) | -1.2785 | 0.7784 | ±1.5569 | -1.642 | 0.1005 |  |
| **Season: summer (vs autumn)** | **+3.1750** | 0.8488 | ±1.6976 | **+3.741** | **1.84e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5040** | 0.8691 | ±1.7383 | **-5.182** | **2.19e-07** | *** |
| Age (years) | -0.0338 | 0.0257 | ±0.0515 | -1.315 | 0.1884 |  |
| BMI (kg/m2) | -0.0297 | 0.0380 | ±0.0760 | -0.783 | 0.4337 |  |
| Hypertension | +0.2875 | 0.6520 | ±1.3040 | +0.441 | 0.6592 |  |
| High cholesterol | -0.8708 | 0.5963 | ±1.1926 | -1.460 | 0.1442 |  |
| Kidney disease | -1.1065 | 1.1563 | ±2.3126 | -0.957 | 0.3386 |  |
| Circulatory disease | -0.4917 | 0.8257 | ±1.6514 | -0.595 | 0.5515 |  |
| Mean / SD ratio | +0.2518 | 0.2753 | ±0.5505 | +0.915 | 0.3603 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **443**, R² = **0.2739**, Adj R² = **0.2501**, F-statistic = **11.53** (p = **1.20e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.3**, BIC = **2887.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4391** | 2.7523 | ±5.5045 | **+17.236** | **1.41e-66** | *** |
| Education: graduate level (vs college) | +0.8492 | 0.5877 | ±1.1753 | +1.445 | 0.1485 |  |
| Education: high school or below (vs college) | -0.9485 | 1.1095 | ±2.2190 | -0.855 | 0.3926 |  |
| **Site: UCSD (vs UAB)** | **+4.2254** | 0.7390 | ±1.4780 | **+5.718** | **1.08e-08** | *** |
| Site: UW (vs UAB) | -0.6822 | 0.7315 | ±1.4629 | -0.933 | 0.3510 |  |
| Season: spring (vs autumn) | -1.3219 | 0.7759 | ±1.5519 | -1.704 | 0.0885 | . |
| **Season: summer (vs autumn)** | **+3.1635** | 0.8472 | ±1.6944 | **+3.734** | **1.89e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5525** | 0.8678 | ±1.7356 | **-5.246** | **1.55e-07** | *** |
| Age (years) | -0.0342 | 0.0257 | ±0.0515 | -1.328 | 0.1842 |  |
| BMI (kg/m2) | -0.0299 | 0.0380 | ±0.0760 | -0.785 | 0.4323 |  |
| Hypertension | +0.2685 | 0.6503 | ±1.3006 | +0.413 | 0.6797 |  |
| High cholesterol | -0.8483 | 0.5960 | ±1.1920 | -1.423 | 0.1546 |  |
| Kidney disease | -1.1525 | 1.1567 | ±2.3134 | -0.996 | 0.3191 |  |
| Circulatory disease | -0.5130 | 0.8275 | ±1.6551 | -0.620 | 0.5353 |  |
| Avg. daily mean/SD | +0.0322 | 0.2196 | ±0.4392 | +0.147 | 0.8833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **443**, R² = **0.2741**, Adj R² = **0.2504**, F-statistic = **11.54** (p = **1.14e-22**), Residual SE = **5.779** on **428** df, AIC = **2826.2**, BIC = **2887.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.9820** | 2.8788 | ±5.7577 | **+16.320** | **7.13e-60** | *** |
| Education: graduate level (vs college) | +0.8521 | 0.5859 | ±1.1718 | +1.454 | 0.1458 |  |
| Education: high school or below (vs college) | -0.9830 | 1.1171 | ±2.2341 | -0.880 | 0.3789 |  |
| **Site: UCSD (vs UAB)** | **+4.2423** | 0.7403 | ±1.4805 | **+5.731** | **9.99e-09** | *** |
| Site: UW (vs UAB) | -0.6468 | 0.7344 | ±1.4687 | -0.881 | 0.3784 |  |
| Season: spring (vs autumn) | -1.3299 | 0.7782 | ±1.5565 | -1.709 | 0.0875 | . |
| **Season: summer (vs autumn)** | **+3.1697** | 0.8491 | ±1.6981 | **+3.733** | **1.89e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5638** | 0.8697 | ±1.7394 | **-5.248** | **1.54e-07** | *** |
| Age (years) | -0.0334 | 0.0259 | ±0.0518 | -1.289 | 0.1973 |  |
| BMI (kg/m2) | -0.0294 | 0.0381 | ±0.0762 | -0.770 | 0.4412 |  |
| Hypertension | +0.2721 | 0.6468 | ±1.2936 | +0.421 | 0.6740 |  |
| High cholesterol | -0.8509 | 0.5935 | ±1.1869 | -1.434 | 0.1516 |  |
| Kidney disease | -1.1864 | 1.1592 | ±2.3185 | -1.023 | 0.3061 |  |
| Circulatory disease | -0.4972 | 0.8276 | ±1.6553 | -0.601 | 0.5480 |  |
| MAG (mg/dL/h) | +0.0187 | 0.0490 | ±0.0980 | +0.382 | 0.7028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **443**, R² = **0.2738**, Adj R² = **0.2501**, F-statistic = **11.53** (p = **1.22e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.3**, BIC = **2887.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.7670** | 2.9464 | ±5.8928 | **+16.212** | **4.16e-59** | *** |
| Education: graduate level (vs college) | +0.8562 | 0.5876 | ±1.1753 | +1.457 | 0.1451 |  |
| Education: high school or below (vs college) | -0.9509 | 1.1101 | ±2.2202 | -0.857 | 0.3917 |  |
| **Site: UCSD (vs UAB)** | **+4.2294** | 0.7394 | ±1.4787 | **+5.720** | **1.06e-08** | *** |
| Site: UW (vs UAB) | -0.6769 | 0.7288 | ±1.4576 | -0.929 | 0.3530 |  |
| Season: spring (vs autumn) | -1.3289 | 0.7795 | ±1.5589 | -1.705 | 0.0882 | . |
| **Season: summer (vs autumn)** | **+3.1607** | 0.8476 | ±1.6951 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5572** | 0.8706 | ±1.7412 | **-5.235** | **1.65e-07** | *** |
| Age (years) | -0.0344 | 0.0257 | ±0.0514 | -1.338 | 0.1809 |  |
| BMI (kg/m2) | -0.0302 | 0.0380 | ±0.0760 | -0.796 | 0.4260 |  |
| Hypertension | +0.2670 | 0.6471 | ±1.2943 | +0.413 | 0.6799 |  |
| High cholesterol | -0.8455 | 0.5938 | ±1.1875 | -1.424 | 0.1545 |  |
| Kidney disease | -1.1601 | 1.1568 | ±2.3135 | -1.003 | 0.3159 |  |
| Circulatory disease | -0.5109 | 0.8262 | ±1.6523 | -0.618 | 0.5363 |  |
| Avg. daily range (mg/dL) | -0.0007 | 0.0269 | ±0.0538 | -0.026 | 0.9791 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **443**, R² = **0.2739**, Adj R² = **0.2502**, F-statistic = **11.53** (p = **1.20e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.3**, BIC = **2887.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8543** | 2.0879 | ±4.1758 | **+22.920** | **2.96e-116** | *** |
| Education: graduate level (vs college) | +0.8608 | 0.5875 | ±1.1751 | +1.465 | 0.1429 |  |
| Education: high school or below (vs college) | -0.9372 | 1.1131 | ±2.2263 | -0.842 | 0.3998 |  |
| **Site: UCSD (vs UAB)** | **+4.2221** | 0.7435 | ±1.4870 | **+5.679** | **1.36e-08** | *** |
| Site: UW (vs UAB) | -0.6752 | 0.7311 | ±1.4622 | -0.924 | 0.3557 |  |
| Season: spring (vs autumn) | -1.3200 | 0.7812 | ±1.5624 | -1.690 | 0.0911 | . |
| **Season: summer (vs autumn)** | **+3.1689** | 0.8476 | ±1.6952 | **+3.739** | **1.85e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5459** | 0.8770 | ±1.7539 | **-5.184** | **2.18e-07** | *** |
| Age (years) | -0.0345 | 0.0257 | ±0.0513 | -1.344 | 0.1790 |  |
| BMI (kg/m2) | -0.0301 | 0.0381 | ±0.0762 | -0.788 | 0.4305 |  |
| Hypertension | +0.2791 | 0.6471 | ±1.2942 | +0.431 | 0.6663 |  |
| High cholesterol | -0.8414 | 0.5910 | ±1.1820 | -1.424 | 0.1545 |  |
| Kidney disease | -1.1640 | 1.1531 | ±2.3062 | -1.009 | 0.3127 |  |
| Circulatory disease | -0.4952 | 0.8343 | ±1.6685 | -0.594 | 0.5528 |  |
| SD of daily means (mg/dL) | -0.0303 | 0.1603 | ±0.3206 | -0.189 | 0.8499 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **443**, R² = **0.2756**, Adj R² = **0.2519**, F-statistic = **11.63** (p = **7.64e-23**), Residual SE = **5.773** on **428** df, AIC = **2825.3**, BIC = **2886.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +140.1632 | 94.7383 | ±189.4766 | +1.479 | 0.1390 |  |
| Education: graduate level (vs college) | +0.8671 | 0.5856 | ±1.1712 | +1.481 | 0.1387 |  |
| Education: high school or below (vs college) | -0.9376 | 1.1094 | ±2.2189 | -0.845 | 0.3980 |  |
| **Site: UCSD (vs UAB)** | **+4.2774** | 0.7389 | ±1.4778 | **+5.789** | **7.09e-09** | *** |
| Site: UW (vs UAB) | -0.6385 | 0.7290 | ±1.4580 | -0.876 | 0.3811 |  |
| Season: spring (vs autumn) | -1.3364 | 0.7762 | ±1.5525 | -1.722 | 0.0851 | . |
| **Season: summer (vs autumn)** | **+3.1430** | 0.8479 | ±1.6958 | **+3.707** | **2.10e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5943** | 0.8717 | ±1.7434 | **-5.271** | **1.36e-07** | *** |
| Age (years) | -0.0337 | 0.0255 | ±0.0511 | -1.318 | 0.1875 |  |
| BMI (kg/m2) | -0.0284 | 0.0379 | ±0.0758 | -0.750 | 0.4532 |  |
| Hypertension | +0.2589 | 0.6450 | ±1.2899 | +0.401 | 0.6881 |  |
| High cholesterol | -0.8631 | 0.5923 | ±1.1847 | -1.457 | 0.1451 |  |
| Kidney disease | -1.2298 | 1.1551 | ±2.3103 | -1.065 | 0.2871 |  |
| Circulatory disease | -0.4989 | 0.8217 | ±1.6433 | -0.607 | 0.5438 |  |
| Time in range 70-180, pooled (%) | -0.9297 | 0.9516 | ±1.9031 | -0.977 | 0.3285 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **443**, R² = **0.2748**, Adj R² = **0.2511**, F-statistic = **11.58** (p = **9.36e-23**), Residual SE = **5.776** on **428** df, AIC = **2825.7**, BIC = **2887.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +114.8316 | 93.3497 | ±186.6995 | +1.230 | 0.2187 |  |
| Education: graduate level (vs college) | +0.8696 | 0.5866 | ±1.1732 | +1.482 | 0.1382 |  |
| Education: high school or below (vs college) | -0.9360 | 1.1133 | ±2.2266 | -0.841 | 0.4005 |  |
| **Site: UCSD (vs UAB)** | **+4.2464** | 0.7406 | ±1.4812 | **+5.734** | **9.82e-09** | *** |
| Site: UW (vs UAB) | -0.6689 | 0.7302 | ±1.4604 | -0.916 | 0.3596 |  |
| Season: spring (vs autumn) | -1.3240 | 0.7774 | ±1.5548 | -1.703 | 0.0886 | . |
| **Season: summer (vs autumn)** | **+3.1769** | 0.8479 | ±1.6957 | **+3.747** | **1.79e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5663** | 0.8704 | ±1.7409 | **-5.246** | **1.55e-07** | *** |
| Age (years) | -0.0337 | 0.0256 | ±0.0513 | -1.314 | 0.1889 |  |
| BMI (kg/m2) | -0.0298 | 0.0380 | ±0.0761 | -0.783 | 0.4337 |  |
| Hypertension | +0.2826 | 0.6462 | ±1.2924 | +0.437 | 0.6619 |  |
| High cholesterol | -0.8675 | 0.5920 | ±1.1840 | -1.465 | 0.1428 |  |
| Kidney disease | -1.1913 | 1.1578 | ±2.3157 | -1.029 | 0.3035 |  |
| Circulatory disease | -0.5160 | 0.8196 | ±1.6391 | -0.630 | 0.5290 |  |
| Avg. daily time in range 70-180 (%) | -0.6745 | 0.9375 | ±1.8751 | -0.719 | 0.4719 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.2744**, Adj R² = **0.2507**, F-statistic = **11.56** (p = **1.05e-22**), Residual SE = **5.778** on **428** df, AIC = **2826.0**, BIC = **2887.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6106** | 2.0192 | ±4.0385 | **+23.579** | **6.39e-123** | *** |
| Education: graduate level (vs college) | +0.8603 | 0.5860 | ±1.1721 | +1.468 | 0.1421 |  |
| Education: high school or below (vs college) | -0.9345 | 1.1090 | ±2.2180 | -0.843 | 0.3994 |  |
| **Site: UCSD (vs UAB)** | **+4.3078** | 0.7407 | ±1.4815 | **+5.816** | **6.04e-09** | *** |
| Site: UW (vs UAB) | -0.6319 | 0.7322 | ±1.4643 | -0.863 | 0.3881 |  |
| Season: spring (vs autumn) | -1.3820 | 0.7775 | ±1.5550 | -1.777 | 0.0755 | . |
| **Season: summer (vs autumn)** | **+3.1285** | 0.8480 | ±1.6960 | **+3.689** | **2.25e-04** | *** |
| **Season: winter (vs autumn)** | **-4.6041** | 0.8670 | ±1.7340 | **-5.310** | **1.09e-07** | *** |
| Age (years) | -0.0340 | 0.0256 | ±0.0512 | -1.328 | 0.1841 |  |
| BMI (kg/m2) | -0.0301 | 0.0380 | ±0.0760 | -0.792 | 0.4283 |  |
| Hypertension | +0.2401 | 0.6457 | ±1.2913 | +0.372 | 0.7099 |  |
| High cholesterol | -0.8451 | 0.5937 | ±1.1874 | -1.424 | 0.1546 |  |
| Kidney disease | -1.1111 | 1.1620 | ±2.3241 | -0.956 | 0.3390 |  |
| Circulatory disease | -0.5260 | 0.8225 | ±1.6450 | -0.640 | 0.5225 |  |
| Any reading < 54 during wear (0/1) | +0.4382 | 0.8105 | ±1.6210 | +0.541 | 0.5887 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.2772**, Adj R² = **0.2535**, F-statistic = **11.72** (p = **4.89e-23**), Residual SE = **5.767** on **428** df, AIC = **2824.3**, BIC = **2885.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4716** | 2.0082 | ±4.0165 | **+23.638** | **1.55e-123** | *** |
| Education: graduate level (vs college) | +0.8541 | 0.5891 | ±1.1781 | +1.450 | 0.1471 |  |
| Education: high school or below (vs college) | -0.8579 | 1.1062 | ±2.2123 | -0.776 | 0.4380 |  |
| **Site: UCSD (vs UAB)** | **+4.3706** | 0.7321 | ±1.4641 | **+5.970** | **2.37e-09** | *** |
| Site: UW (vs UAB) | -0.6055 | 0.7248 | ±1.4495 | -0.835 | 0.4035 |  |
| Season: spring (vs autumn) | -1.3177 | 0.7842 | ±1.5683 | -1.680 | 0.0929 | . |
| **Season: summer (vs autumn)** | **+3.1504** | 0.8544 | ±1.7088 | **+3.687** | **2.27e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5951** | 0.8705 | ±1.7410 | **-5.279** | **1.30e-07** | *** |
| Age (years) | -0.0314 | 0.0255 | ±0.0510 | -1.232 | 0.2180 |  |
| BMI (kg/m2) | -0.0343 | 0.0380 | ±0.0760 | -0.902 | 0.3670 |  |
| Hypertension | +0.1811 | 0.6369 | ±1.2738 | +0.284 | 0.7762 |  |
| High cholesterol | -0.8177 | 0.5904 | ±1.1807 | -1.385 | 0.1660 |  |
| Kidney disease | -1.0824 | 1.1634 | ±2.3268 | -0.930 | 0.3522 |  |
| Circulatory disease | -0.5580 | 0.8223 | ±1.6447 | -0.679 | 0.4974 |  |
| Time < 54 (%) | +7.4186 | 7.6314 | ±15.2628 | +0.972 | 0.3310 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.2740**, Adj R² = **0.2503**, F-statistic = **11.54** (p = **1.15e-22**), Residual SE = **5.779** on **428** df, AIC = **2826.2**, BIC = **2887.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6734** | 2.0084 | ±4.0168 | **+23.737** | **1.49e-124** | *** |
| Education: graduate level (vs college) | +0.8545 | 0.5884 | ±1.1769 | +1.452 | 0.1465 |  |
| Education: high school or below (vs college) | -0.9412 | 1.1093 | ±2.2186 | -0.848 | 0.3962 |  |
| **Site: UCSD (vs UAB)** | **+4.2456** | 0.7404 | ±1.4808 | **+5.734** | **9.80e-09** | *** |
| Site: UW (vs UAB) | -0.6729 | 0.7328 | ±1.4656 | -0.918 | 0.3585 |  |
| Season: spring (vs autumn) | -1.3220 | 0.7818 | ±1.5635 | -1.691 | 0.0908 | . |
| **Season: summer (vs autumn)** | **+3.1781** | 0.8504 | ±1.7008 | **+3.737** | **1.86e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5556** | 0.8703 | ±1.7407 | **-5.234** | **1.66e-07** | *** |
| Age (years) | -0.0341 | 0.0257 | ±0.0514 | -1.326 | 0.1850 |  |
| BMI (kg/m2) | -0.0306 | 0.0381 | ±0.0763 | -0.801 | 0.4230 |  |
| Hypertension | +0.2595 | 0.6497 | ±1.2995 | +0.399 | 0.6896 |  |
| High cholesterol | -0.8454 | 0.5935 | ±1.1870 | -1.424 | 0.1543 |  |
| Kidney disease | -1.1512 | 1.1579 | ±2.3157 | -0.994 | 0.3201 |  |
| Circulatory disease | -0.5287 | 0.8252 | ±1.6503 | -0.641 | 0.5217 |  |
| Avg. daily time < 54 (%) | +2.4000 | 8.4128 | ±16.8256 | +0.285 | 0.7754 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.2750**, Adj R² = **0.2512**, F-statistic = **11.59** (p = **9.00e-23**), Residual SE = **5.776** on **428** df, AIC = **2825.7**, BIC = **2887.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5208** | 2.0162 | ±4.0324 | **+23.569** | **7.98e-123** | *** |
| Education: graduate level (vs college) | +0.8689 | 0.5849 | ±1.1698 | +1.486 | 0.1374 |  |
| Education: high school or below (vs college) | -0.9995 | 1.1212 | ±2.2424 | -0.891 | 0.3727 |  |
| **Site: UCSD (vs UAB)** | **+4.2680** | 0.7400 | ±1.4801 | **+5.767** | **8.06e-09** | *** |
| Site: UW (vs UAB) | -0.6310 | 0.7359 | ±1.4719 | -0.857 | 0.3912 |  |
| Season: spring (vs autumn) | -1.3433 | 0.7760 | ±1.5521 | -1.731 | 0.0835 | . |
| **Season: summer (vs autumn)** | **+3.1494** | 0.8464 | ±1.6928 | **+3.721** | **1.98e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5907** | 0.8663 | ±1.7326 | **-5.299** | **1.16e-07** | *** |
| Age (years) | -0.0343 | 0.0257 | ±0.0514 | -1.337 | 0.1813 |  |
| BMI (kg/m2) | -0.0301 | 0.0379 | ±0.0758 | -0.793 | 0.4275 |  |
| Hypertension | +0.2967 | 0.6535 | ±1.3071 | +0.454 | 0.6498 |  |
| High cholesterol | -0.8851 | 0.5959 | ±1.1917 | -1.485 | 0.1375 |  |
| Kidney disease | -1.0907 | 1.1630 | ±2.3259 | -0.938 | 0.3483 |  |
| Circulatory disease | -0.5011 | 0.8239 | ±1.6478 | -0.608 | 0.5430 |  |
| Time 54-69, pooled (%) | +1.2428 | 1.6368 | ±3.2736 | +0.759 | 0.4477 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **443**, R² = **0.2739**, Adj R² = **0.2501**, F-statistic = **11.53** (p = **1.20e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.3**, BIC = **2887.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6739** | 2.0084 | ±4.0167 | **+23.738** | **1.47e-124** | *** |
| Education: graduate level (vs college) | +0.8613 | 0.5879 | ±1.1758 | +1.465 | 0.1429 |  |
| Education: high school or below (vs college) | -0.9621 | 1.1166 | ±2.2331 | -0.862 | 0.3889 |  |
| **Site: UCSD (vs UAB)** | **+4.2343** | 0.7408 | ±1.4816 | **+5.716** | **1.09e-08** | *** |
| Site: UW (vs UAB) | -0.6703 | 0.7325 | ±1.4650 | -0.915 | 0.3601 |  |
| Season: spring (vs autumn) | -1.3266 | 0.7808 | ±1.5615 | -1.699 | 0.0893 | . |
| **Season: summer (vs autumn)** | **+3.1654** | 0.8474 | ±1.6948 | **+3.735** | **1.87e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5621** | 0.8681 | ±1.7362 | **-5.255** | **1.48e-07** | *** |
| Age (years) | -0.0344 | 0.0257 | ±0.0514 | -1.338 | 0.1808 |  |
| BMI (kg/m2) | -0.0302 | 0.0380 | ±0.0759 | -0.794 | 0.4269 |  |
| Hypertension | +0.2798 | 0.6546 | ±1.3091 | +0.427 | 0.6690 |  |
| High cholesterol | -0.8530 | 0.5933 | ±1.1866 | -1.438 | 0.1505 |  |
| Kidney disease | -1.1515 | 1.1586 | ±2.3172 | -0.994 | 0.3203 |  |
| Circulatory disease | -0.5124 | 0.8248 | ±1.6495 | -0.621 | 0.5344 |  |
| Avg. daily time 54-69 (%) | +0.2665 | 1.6684 | ±3.3369 | +0.160 | 0.8731 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **443**, R² = **0.2758**, Adj R² = **0.2521**, F-statistic = **11.64** (p = **7.07e-23**), Residual SE = **5.772** on **428** df, AIC = **2825.1**, BIC = **2886.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4374** | 2.0171 | ±4.0342 | **+23.518** | **2.67e-122** | *** |
| Education: graduate level (vs college) | +0.8707 | 0.5847 | ±1.1694 | +1.489 | 0.1364 |  |
| Education: high school or below (vs college) | -0.9901 | 1.1190 | ±2.2380 | -0.885 | 0.3763 |  |
| **Site: UCSD (vs UAB)** | **+4.3031** | 0.7383 | ±1.4767 | **+5.828** | **5.60e-09** | *** |
| Site: UW (vs UAB) | -0.6085 | 0.7337 | ±1.4675 | -0.829 | 0.4069 |  |
| Season: spring (vs autumn) | -1.3435 | 0.7768 | ±1.5536 | -1.730 | 0.0837 | . |
| **Season: summer (vs autumn)** | **+3.1452** | 0.8476 | ±1.6952 | **+3.711** | **2.07e-04** | *** |
| **Season: winter (vs autumn)** | **-4.6043** | 0.8658 | ±1.7317 | **-5.318** | **1.05e-07** | *** |
| Age (years) | -0.0337 | 0.0256 | ±0.0513 | -1.316 | 0.1880 |  |
| BMI (kg/m2) | -0.0309 | 0.0379 | ±0.0758 | -0.814 | 0.4155 |  |
| Hypertension | +0.2851 | 0.6495 | ±1.2989 | +0.439 | 0.6607 |  |
| High cholesterol | -0.8871 | 0.5964 | ±1.1928 | -1.487 | 0.1369 |  |
| Kidney disease | -1.0612 | 1.1657 | ±2.3313 | -0.910 | 0.3626 |  |
| Circulatory disease | -0.5086 | 0.8224 | ±1.6448 | -0.618 | 0.5363 |  |
| Time < 70 (%) | +1.4805 | 1.5393 | ±3.0786 | +0.962 | 0.3361 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **443**, R² = **0.2739**, Adj R² = **0.2502**, F-statistic = **11.53** (p = **1.19e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.3**, BIC = **2887.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6619** | 2.0089 | ±4.0177 | **+23.726** | **1.95e-124** | *** |
| Education: graduate level (vs college) | +0.8620 | 0.5873 | ±1.1745 | +1.468 | 0.1422 |  |
| Education: high school or below (vs college) | -0.9631 | 1.1156 | ±2.2311 | -0.863 | 0.3879 |  |
| **Site: UCSD (vs UAB)** | **+4.2372** | 0.7411 | ±1.4822 | **+5.718** | **1.08e-08** | *** |
| Site: UW (vs UAB) | -0.6688 | 0.7327 | ±1.4654 | -0.913 | 0.3613 |  |
| Season: spring (vs autumn) | -1.3249 | 0.7812 | ±1.5624 | -1.696 | 0.0899 | . |
| **Season: summer (vs autumn)** | **+3.1688** | 0.8483 | ±1.6966 | **+3.736** | **1.87e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5626** | 0.8685 | ±1.7371 | **-5.253** | **1.50e-07** | *** |
| Age (years) | -0.0344 | 0.0257 | ±0.0514 | -1.338 | 0.1809 |  |
| BMI (kg/m2) | -0.0302 | 0.0380 | ±0.0760 | -0.795 | 0.4265 |  |
| Hypertension | +0.2813 | 0.6523 | ±1.3046 | +0.431 | 0.6662 |  |
| High cholesterol | -0.8546 | 0.5933 | ±1.1865 | -1.440 | 0.1497 |  |
| Kidney disease | -1.1479 | 1.1591 | ±2.3182 | -0.990 | 0.3220 |  |
| Circulatory disease | -0.5151 | 0.8243 | ±1.6486 | -0.625 | 0.5320 |  |
| Avg. daily time < 70 (%) | +0.3222 | 1.5282 | ±3.0565 | +0.211 | 0.8330 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.2777**, Adj R² = **0.2541**, F-statistic = **11.75** (p = **4.21e-23**), Residual SE = **5.765** on **428** df, AIC = **2824.0**, BIC = **2885.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +828.1423 | 724.7309 | ±1449.4618 | +1.143 | 0.2532 |  |
| Education: graduate level (vs college) | +0.8531 | 0.5888 | ±1.1775 | +1.449 | 0.1473 |  |
| Education: high school or below (vs college) | -0.8501 | 1.1065 | ±2.2130 | -0.768 | 0.4423 |  |
| **Site: UCSD (vs UAB)** | **+4.3892** | 0.7333 | ±1.4666 | **+5.986** | **2.15e-09** | *** |
| Site: UW (vs UAB) | -0.5931 | 0.7244 | ±1.4487 | -0.819 | 0.4129 |  |
| Season: spring (vs autumn) | -1.3248 | 0.7844 | ±1.5688 | -1.689 | 0.0912 | . |
| **Season: summer (vs autumn)** | **+3.1511** | 0.8546 | ±1.7093 | **+3.687** | **2.27e-04** | *** |
| **Season: winter (vs autumn)** | **-4.6035** | 0.8705 | ±1.7410 | **-5.288** | **1.24e-07** | *** |
| Age (years) | -0.0308 | 0.0255 | ±0.0510 | -1.207 | 0.2276 |  |
| BMI (kg/m2) | -0.0340 | 0.0380 | ±0.0759 | -0.896 | 0.3701 |  |
| Hypertension | +0.1803 | 0.6369 | ±1.2738 | +0.283 | 0.7771 |  |
| High cholesterol | -0.8185 | 0.5902 | ±1.1804 | -1.387 | 0.1655 |  |
| Kidney disease | -1.0789 | 1.1636 | ±2.3272 | -0.927 | 0.3538 |  |
| Circulatory disease | -0.5619 | 0.8221 | ±1.6442 | -0.684 | 0.4943 |  |
| Time 54-250, pooled (%) | -7.8073 | 7.2479 | ±14.4957 | -1.077 | 0.2814 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.2743**, Adj R² = **0.2506**, F-statistic = **11.56** (p = **1.06e-22**), Residual SE = **5.778** on **428** df, AIC = **2826.0**, BIC = **2887.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +419.7506 | 838.8309 | ±1677.6619 | +0.500 | 0.6168 |  |
| Education: graduate level (vs college) | +0.8529 | 0.5885 | ±1.1769 | +1.449 | 0.1472 |  |
| Education: high school or below (vs college) | -0.9342 | 1.1097 | ±2.2193 | -0.842 | 0.3999 |  |
| **Site: UCSD (vs UAB)** | **+4.2598** | 0.7414 | ±1.4829 | **+5.745** | **9.17e-09** | *** |
| Site: UW (vs UAB) | -0.6668 | 0.7329 | ±1.4657 | -0.910 | 0.3629 |  |
| Season: spring (vs autumn) | -1.3217 | 0.7824 | ±1.5648 | -1.689 | 0.0912 | . |
| **Season: summer (vs autumn)** | **+3.1884** | 0.8508 | ±1.7017 | **+3.747** | **1.79e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5577** | 0.8712 | ±1.7424 | **-5.231** | **1.68e-07** | *** |
| Age (years) | -0.0337 | 0.0257 | ±0.0515 | -1.309 | 0.1907 |  |
| BMI (kg/m2) | -0.0305 | 0.0381 | ±0.0762 | -0.801 | 0.4230 |  |
| Hypertension | +0.2571 | 0.6491 | ±1.2981 | +0.396 | 0.6920 |  |
| High cholesterol | -0.8466 | 0.5936 | ±1.1872 | -1.426 | 0.1538 |  |
| Kidney disease | -1.1456 | 1.1588 | ±2.3176 | -0.989 | 0.3228 |  |
| Circulatory disease | -0.5393 | 0.8243 | ±1.6486 | -0.654 | 0.5129 |  |
| Avg. daily time 54-250 (%) | -3.7212 | 8.3886 | ±16.7773 | -0.444 | 0.6573 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **443**, R² = **0.2740**, Adj R² = **0.2502**, F-statistic = **11.54** (p = **1.18e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.3**, BIC = **2887.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6123** | 2.0474 | ±4.0949 | **+23.254** | **1.28e-119** | *** |
| Education: graduate level (vs college) | +0.8572 | 0.5868 | ±1.1736 | +1.461 | 0.1441 |  |
| Education: high school or below (vs college) | -0.9405 | 1.1090 | ±2.2181 | -0.848 | 0.3964 |  |
| **Site: UCSD (vs UAB)** | **+4.2304** | 0.7399 | ±1.4798 | **+5.718** | **1.08e-08** | *** |
| Site: UW (vs UAB) | -0.6774 | 0.7309 | ±1.4619 | -0.927 | 0.3541 |  |
| Season: spring (vs autumn) | -1.3289 | 0.7790 | ±1.5581 | -1.706 | 0.0880 | . |
| **Season: summer (vs autumn)** | **+3.1583** | 0.8469 | ±1.6939 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5600** | 0.8697 | ±1.7394 | **-5.243** | **1.58e-07** | *** |
| Age (years) | -0.0343 | 0.0257 | ±0.0513 | -1.337 | 0.1813 |  |
| BMI (kg/m2) | -0.0296 | 0.0381 | ±0.0761 | -0.777 | 0.4372 |  |
| Hypertension | +0.2618 | 0.6507 | ±1.3013 | +0.402 | 0.6874 |  |
| High cholesterol | -0.8429 | 0.5935 | ±1.1870 | -1.420 | 0.1555 |  |
| Kidney disease | -1.1987 | 1.1622 | ±2.3243 | -1.031 | 0.3023 |  |
| Circulatory disease | -0.5078 | 0.8267 | ±1.6534 | -0.614 | 0.5390 |  |
| Time 181-250, pooled (%) | +0.2617 | 1.0236 | ±2.0472 | +0.256 | 0.7982 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **443**, R² = **0.2745**, Adj R² = **0.2508**, F-statistic = **11.57** (p = **1.01e-22**), Residual SE = **5.777** on **428** df, AIC = **2825.9**, BIC = **2887.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4984** | 2.0467 | ±4.0934 | **+23.207** | **3.84e-119** | *** |
| Education: graduate level (vs college) | +0.8586 | 0.5867 | ±1.1734 | +1.463 | 0.1434 |  |
| Education: high school or below (vs college) | -0.9137 | 1.1136 | ±2.2272 | -0.820 | 0.4120 |  |
| **Site: UCSD (vs UAB)** | **+4.2311** | 0.7399 | ±1.4798 | **+5.719** | **1.07e-08** | *** |
| Site: UW (vs UAB) | -0.6836 | 0.7310 | ±1.4619 | -0.935 | 0.3497 |  |
| Season: spring (vs autumn) | -1.3332 | 0.7779 | ±1.5559 | -1.714 | 0.0866 | . |
| **Season: summer (vs autumn)** | **+3.1597** | 0.8479 | ±1.6958 | **+3.727** | **1.94e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5566** | 0.8689 | ±1.7378 | **-5.244** | **1.57e-07** | *** |
| Age (years) | -0.0337 | 0.0257 | ±0.0514 | -1.313 | 0.1890 |  |
| BMI (kg/m2) | -0.0297 | 0.0381 | ±0.0763 | -0.779 | 0.4358 |  |
| Hypertension | +0.2541 | 0.6501 | ±1.3002 | +0.391 | 0.6959 |  |
| High cholesterol | -0.8479 | 0.5925 | ±1.1850 | -1.431 | 0.1524 |  |
| Kidney disease | -1.2169 | 1.1571 | ±2.3141 | -1.052 | 0.2929 |  |
| Circulatory disease | -0.5072 | 0.8235 | ±1.6470 | -0.616 | 0.5380 |  |
| Avg. daily time 181-250 (%) | +0.6336 | 1.0514 | ±2.1028 | +0.603 | 0.5468 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **443**, R² = **0.2740**, Adj R² = **0.2502**, F-statistic = **11.54** (p = **1.17e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.2**, BIC = **2887.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6007** | 2.0486 | ±4.0971 | **+23.236** | **1.96e-119** | *** |
| Education: graduate level (vs college) | +0.8572 | 0.5868 | ±1.1735 | +1.461 | 0.1440 |  |
| Education: high school or below (vs college) | -0.9394 | 1.1090 | ±2.2181 | -0.847 | 0.3970 |  |
| **Site: UCSD (vs UAB)** | **+4.2309** | 0.7399 | ±1.4798 | **+5.718** | **1.08e-08** | *** |
| Site: UW (vs UAB) | -0.6772 | 0.7308 | ±1.4616 | -0.927 | 0.3541 |  |
| Season: spring (vs autumn) | -1.3291 | 0.7789 | ±1.5578 | -1.706 | 0.0879 | . |
| **Season: summer (vs autumn)** | **+3.1581** | 0.8469 | ±1.6939 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5604** | 0.8699 | ±1.7397 | **-5.243** | **1.58e-07** | *** |
| Age (years) | -0.0343 | 0.0257 | ±0.0513 | -1.336 | 0.1816 |  |
| BMI (kg/m2) | -0.0295 | 0.0381 | ±0.0761 | -0.775 | 0.4385 |  |
| Hypertension | +0.2614 | 0.6505 | ±1.3011 | +0.402 | 0.6878 |  |
| High cholesterol | -0.8428 | 0.5934 | ±1.1869 | -1.420 | 0.1556 |  |
| Kidney disease | -1.2024 | 1.1620 | ±2.3240 | -1.035 | 0.3008 |  |
| Circulatory disease | -0.5076 | 0.8265 | ±1.6531 | -0.614 | 0.5391 |  |
| Time > 180 (%) | +0.2880 | 1.0208 | ±2.0416 | +0.282 | 0.7779 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **443**, R² = **0.2746**, Adj R² = **0.2509**, F-statistic = **11.57** (p = **9.88e-23**), Residual SE = **5.777** on **428** df, AIC = **2825.9**, BIC = **2887.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4850** | 2.0480 | ±4.0960 | **+23.186** | **6.27e-119** | *** |
| Education: graduate level (vs college) | +0.8586 | 0.5867 | ±1.1734 | +1.463 | 0.1433 |  |
| Education: high school or below (vs college) | -0.9118 | 1.1137 | ±2.2275 | -0.819 | 0.4130 |  |
| **Site: UCSD (vs UAB)** | **+4.2322** | 0.7399 | ±1.4798 | **+5.720** | **1.07e-08** | *** |
| Site: UW (vs UAB) | -0.6831 | 0.7307 | ±1.4615 | -0.935 | 0.3499 |  |
| Season: spring (vs autumn) | -1.3340 | 0.7779 | ±1.5558 | -1.715 | 0.0864 | . |
| **Season: summer (vs autumn)** | **+3.1598** | 0.8479 | ±1.6959 | **+3.726** | **1.94e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5572** | 0.8690 | ±1.7380 | **-5.244** | **1.57e-07** | *** |
| Age (years) | -0.0337 | 0.0257 | ±0.0514 | -1.310 | 0.1900 |  |
| BMI (kg/m2) | -0.0297 | 0.0382 | ±0.0763 | -0.777 | 0.4369 |  |
| Hypertension | +0.2538 | 0.6500 | ±1.2999 | +0.391 | 0.6961 |  |
| High cholesterol | -0.8482 | 0.5924 | ±1.1849 | -1.432 | 0.1522 |  |
| Kidney disease | -1.2193 | 1.1570 | ±2.3139 | -1.054 | 0.2919 |  |
| Circulatory disease | -0.5071 | 0.8233 | ±1.6466 | -0.616 | 0.5379 |  |
| Avg. daily time > 180 (%) | +0.6597 | 1.0472 | ±2.0945 | +0.630 | 0.5288 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **443**, R² = **0.2770**, Adj R² = **0.2534**, F-statistic = **11.72** (p = **5.07e-23**), Residual SE = **5.767** on **428** df, AIC = **2824.4**, BIC = **2885.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.0196** | 2.0339 | ±4.0678 | **+23.610** | **3.06e-123** | *** |
| Education: graduate level (vs college) | +0.8149 | 0.5909 | ±1.1818 | +1.379 | 0.1679 |  |
| Education: high school or below (vs college) | -0.9778 | 1.0988 | ±2.1976 | -0.890 | 0.3736 |  |
| **Site: UCSD (vs UAB)** | **+4.2326** | 0.7345 | ±1.4690 | **+5.762** | **8.29e-09** | *** |
| Site: UW (vs UAB) | -0.6461 | 0.7295 | ±1.4590 | -0.886 | 0.3758 |  |
| Season: spring (vs autumn) | -1.3079 | 0.7781 | ±1.5562 | -1.681 | 0.0928 | . |
| **Season: summer (vs autumn)** | **+3.1392** | 0.8394 | ±1.6787 | **+3.740** | **1.84e-04** | *** |
| **Season: winter (vs autumn)** | **-4.4594** | 0.8690 | ±1.7381 | **-5.131** | **2.88e-07** | *** |
| Age (years) | -0.0402 | 0.0261 | ±0.0521 | -1.542 | 0.1231 |  |
| BMI (kg/m2) | -0.0266 | 0.0370 | ±0.0740 | -0.720 | 0.4717 |  |
| Hypertension | +0.3489 | 0.6528 | ±1.3057 | +0.534 | 0.5931 |  |
| High cholesterol | -0.8231 | 0.5916 | ±1.1832 | -1.391 | 0.1641 |  |
| Kidney disease | -1.1521 | 1.1445 | ±2.2890 | -1.007 | 0.3141 |  |
| Circulatory disease | -0.5578 | 0.8281 | ±1.6561 | -0.674 | 0.5006 |  |
| Nocturnal time > 180 (%) | -1.0888 | 0.8389 | ±1.6779 | -1.298 | 0.1943 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 443; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **443**, R² = **0.0420**, Adj R² = **0.0130**, F-statistic = **1.45** (p = **0.1348**), Residual SE = **14.204** on **429** df, AIC = **3622.0**, BIC = **3679.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2064** | 5.6584 | ±11.3169 | **+22.304** | **3.37e-110** | *** |
| Education: graduate level (vs college) | -1.3171 | 1.4240 | ±2.8480 | -0.925 | 0.3550 |  |
| Education: high school or below (vs college) | +3.5906 | 2.6867 | ±5.3734 | +1.336 | 0.1814 |  |
| Site: UCSD (vs UAB) | +0.9079 | 1.8453 | ±3.6907 | +0.492 | 0.6227 |  |
| Site: UW (vs UAB) | +1.4580 | 1.8087 | ±3.6175 | +0.806 | 0.4202 |  |
| Season: spring (vs autumn) | +1.7470 | 1.9469 | ±3.8938 | +0.897 | 0.3696 |  |
| Season: summer (vs autumn) | +1.8866 | 2.0072 | ±4.0144 | +0.940 | 0.3473 |  |
| Season: winter (vs autumn) | +3.4614 | 2.0035 | ±4.0069 | +1.728 | 0.0840 | . |
| Age (years) | -0.1098 | 0.0708 | ±0.1415 | -1.552 | 0.1207 |  |
| BMI (kg/m2) | +0.1534 | 0.0992 | ±0.1983 | +1.547 | 0.1218 |  |
| Hypertension | +2.1145 | 1.5790 | ±3.1581 | +1.339 | 0.1805 |  |
| High cholesterol | -0.0361 | 1.4994 | ±2.9989 | -0.024 | 0.9808 |  |
| Kidney disease | -0.9878 | 2.5855 | ±5.1710 | -0.382 | 0.7024 |  |
| Circulatory disease | -1.0644 | 2.1839 | ±4.3678 | -0.487 | 0.6260 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **443**, R² = **0.0445**, Adj R² = **0.0133**, F-statistic = **1.42** (p = **0.1380**), Residual SE = **14.202** on **428** df, AIC = **3622.8**, BIC = **3684.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+139.0996** | 14.0380 | ±28.0761 | **+9.909** | **3.81e-23** | *** |
| Education: graduate level (vs college) | -1.3770 | 1.4361 | ±2.8722 | -0.959 | 0.3376 |  |
| Education: high school or below (vs college) | +3.7690 | 2.6912 | ±5.3824 | +1.400 | 0.1614 |  |
| Site: UCSD (vs UAB) | +0.9369 | 1.8498 | ±3.6997 | +0.506 | 0.6125 |  |
| Site: UW (vs UAB) | +1.4259 | 1.8197 | ±3.6394 | +0.784 | 0.4333 |  |
| Season: spring (vs autumn) | +1.4262 | 1.9865 | ±3.9730 | +0.718 | 0.4728 |  |
| Season: summer (vs autumn) | +2.0076 | 2.0130 | ±4.0260 | +0.997 | 0.3186 |  |
| Season: winter (vs autumn) | +3.3438 | 2.0295 | ±4.0590 | +1.648 | 0.0994 | . |
| Age (years) | -0.1027 | 0.0718 | ±0.1436 | -1.430 | 0.1527 |  |
| BMI (kg/m2) | +0.1662 | 0.0988 | ±0.1976 | +1.682 | 0.0925 | . |
| Hypertension | +2.2567 | 1.5701 | ±3.1402 | +1.437 | 0.1506 |  |
| High cholesterol | +0.2882 | 1.5691 | ±3.1382 | +0.184 | 0.8543 |  |
| Kidney disease | -1.1438 | 2.6019 | ±5.2039 | -0.440 | 0.6602 |  |
| Circulatory disease | -1.1962 | 2.2248 | ±4.4497 | -0.538 | 0.5908 |  |
| HbA1c (%) | -2.4761 | 2.5141 | ±5.0281 | -0.985 | 0.3247 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **443**, R² = **0.0499**, Adj R² = **0.0188**, F-statistic = **1.60** (p = **0.0748**), Residual SE = **14.163** on **428** df, AIC = **3620.4**, BIC = **3681.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+145.5802** | 12.2054 | ±24.4108 | **+11.928** | **8.51e-33** | *** |
| Education: graduate level (vs college) | -1.2790 | 1.4166 | ±2.8333 | -0.903 | 0.3666 |  |
| Education: high school or below (vs college) | +3.4227 | 2.6707 | ±5.3415 | +1.282 | 0.2000 |  |
| Site: UCSD (vs UAB) | +1.0640 | 1.8454 | ±3.6908 | +0.577 | 0.5642 |  |
| Site: UW (vs UAB) | +1.6437 | 1.8262 | ±3.6523 | +0.900 | 0.3681 |  |
| Season: spring (vs autumn) | +1.5827 | 1.9390 | ±3.8781 | +0.816 | 0.4144 |  |
| Season: summer (vs autumn) | +1.8642 | 2.0255 | ±4.0511 | +0.920 | 0.3574 |  |
| Season: winter (vs autumn) | +3.3390 | 2.0275 | ±4.0549 | +1.647 | 0.0996 | . |
| Age (years) | -0.1134 | 0.0708 | ±0.1417 | -1.601 | 0.1094 |  |
| BMI (kg/m2) | +0.1648 | 0.0988 | ±0.1976 | +1.668 | 0.0953 | . |
| Hypertension | +2.2820 | 1.5674 | ±3.1349 | +1.456 | 0.1454 |  |
| High cholesterol | -0.1409 | 1.5009 | ±3.0019 | -0.094 | 0.9252 |  |
| Kidney disease | -0.8096 | 2.6031 | ±5.2063 | -0.311 | 0.7558 |  |
| Circulatory disease | -1.0422 | 2.2058 | ±4.4116 | -0.472 | 0.6366 |  |
| Mean glucose (mg/dL) | -0.1711 | 0.0935 | ±0.1871 | -1.829 | 0.0675 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **443**, R² = **0.0499**, Adj R² = **0.0188**, F-statistic = **1.60** (p = **0.0748**), Residual SE = **14.163** on **428** df, AIC = **3620.4**, BIC = **3681.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+169.2510** | 24.4358 | ±48.8716 | **+6.926** | **4.32e-12** | *** |
| Education: graduate level (vs college) | -1.2790 | 1.4166 | ±2.8333 | -0.903 | 0.3666 |  |
| Education: high school or below (vs college) | +3.4227 | 2.6707 | ±5.3415 | +1.282 | 0.2000 |  |
| Site: UCSD (vs UAB) | +1.0640 | 1.8454 | ±3.6908 | +0.577 | 0.5642 |  |
| Site: UW (vs UAB) | +1.6437 | 1.8262 | ±3.6523 | +0.900 | 0.3681 |  |
| Season: spring (vs autumn) | +1.5827 | 1.9390 | ±3.8781 | +0.816 | 0.4144 |  |
| Season: summer (vs autumn) | +1.8642 | 2.0255 | ±4.0511 | +0.920 | 0.3574 |  |
| Season: winter (vs autumn) | +3.3390 | 2.0275 | ±4.0549 | +1.647 | 0.0996 | . |
| Age (years) | -0.1134 | 0.0708 | ±0.1417 | -1.601 | 0.1094 |  |
| BMI (kg/m2) | +0.1648 | 0.0988 | ±0.1976 | +1.668 | 0.0953 | . |
| Hypertension | +2.2820 | 1.5674 | ±3.1349 | +1.456 | 0.1454 |  |
| High cholesterol | -0.1409 | 1.5009 | ±3.0019 | -0.094 | 0.9252 |  |
| Kidney disease | -0.8096 | 2.6031 | ±5.2063 | -0.311 | 0.7558 |  |
| Circulatory disease | -1.0422 | 2.2058 | ±4.4116 | -0.472 | 0.6366 |  |
| GMI (%) | -7.1513 | 3.9109 | ±7.8217 | -1.829 | 0.0675 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **443**, R² = **0.0461**, Adj R² = **0.0149**, F-statistic = **1.48** (p = **0.1160**), Residual SE = **14.191** on **428** df, AIC = **3622.1**, BIC = **3683.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+137.4767** | 10.1588 | ±20.3175 | **+13.533** | **1.00e-41** | *** |
| Education: graduate level (vs college) | -1.3769 | 1.4294 | ±2.8588 | -0.963 | 0.3354 |  |
| Education: high school or below (vs college) | +3.4352 | 2.6886 | ±5.3772 | +1.278 | 0.2014 |  |
| Site: UCSD (vs UAB) | +1.1378 | 1.8644 | ±3.7289 | +0.610 | 0.5417 |  |
| Site: UW (vs UAB) | +1.6626 | 1.8380 | ±3.6759 | +0.905 | 0.3657 |  |
| Season: spring (vs autumn) | +1.6652 | 1.9462 | ±3.8923 | +0.856 | 0.3922 |  |
| Season: summer (vs autumn) | +1.8887 | 2.0228 | ±4.0456 | +0.934 | 0.3505 |  |
| Season: winter (vs autumn) | +3.4191 | 2.0173 | ±4.0345 | +1.695 | 0.0901 | . |
| Age (years) | -0.1220 | 0.0722 | ±0.1443 | -1.690 | 0.0910 | . |
| BMI (kg/m2) | +0.1741 | 0.0970 | ±0.1939 | +1.795 | 0.0726 | . |
| Hypertension | +2.2364 | 1.5762 | ±3.1523 | +1.419 | 0.1559 |  |
| High cholesterol | -0.0582 | 1.5024 | ±3.0049 | -0.039 | 0.9691 |  |
| Kidney disease | -1.0698 | 2.5753 | ±5.1506 | -0.415 | 0.6778 |  |
| Circulatory disease | -1.0978 | 2.1937 | ±4.3873 | -0.500 | 0.6168 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0978 | 0.0707 | ±0.1414 | -1.383 | 0.1666 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **443**, R² = **0.0420**, Adj R² = **0.0107**, F-statistic = **1.34** (p = **0.1802**), Residual SE = **14.221** on **428** df, AIC = **3624.0**, BIC = **3685.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.3365** | 7.2632 | ±14.5265 | **+17.394** | **9.16e-68** | *** |
| Education: graduate level (vs college) | -1.3193 | 1.4312 | ±2.8623 | -0.922 | 0.3566 |  |
| Education: high school or below (vs college) | +3.5915 | 2.6891 | ±5.3782 | +1.336 | 0.1817 |  |
| Site: UCSD (vs UAB) | +0.9049 | 1.8552 | ±3.7103 | +0.488 | 0.6257 |  |
| Site: UW (vs UAB) | +1.4548 | 1.8188 | ±3.6377 | +0.800 | 0.4238 |  |
| Season: spring (vs autumn) | +1.7492 | 1.9688 | ±3.9375 | +0.888 | 0.3743 |  |
| Season: summer (vs autumn) | +1.8873 | 2.0137 | ±4.0273 | +0.937 | 0.3486 |  |
| Season: winter (vs autumn) | +3.4645 | 2.0171 | ±4.0342 | +1.718 | 0.0859 | . |
| Age (years) | -0.1098 | 0.0712 | ±0.1423 | -1.543 | 0.1228 |  |
| BMI (kg/m2) | +0.1535 | 0.0993 | ±0.1985 | +1.547 | 0.1220 |  |
| Hypertension | +2.1172 | 1.5801 | ±3.1603 | +1.340 | 0.1803 |  |
| High cholesterol | -0.0384 | 1.4975 | ±2.9950 | -0.026 | 0.9795 |  |
| Kidney disease | -0.9808 | 2.5509 | ±5.1019 | -0.384 | 0.7006 |  |
| Circulatory disease | -1.0623 | 2.2000 | ±4.3999 | -0.483 | 0.6292 |  |
| Glucose SD, pooled (mg/dL) | -0.0080 | 0.3162 | ±0.6323 | -0.025 | 0.9797 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **443**, R² = **0.0421**, Adj R² = **0.0108**, F-statistic = **1.34** (p = **0.1784**), Residual SE = **14.220** on **428** df, AIC = **3624.0**, BIC = **3685.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.0756** | 6.8990 | ±13.7980 | **+18.419** | **9.17e-76** | *** |
| Education: graduate level (vs college) | -1.3376 | 1.4353 | ±2.8706 | -0.932 | 0.3514 |  |
| Education: high school or below (vs college) | +3.5869 | 2.6911 | ±5.3822 | +1.333 | 0.1826 |  |
| Site: UCSD (vs UAB) | +0.8917 | 1.8520 | ±3.7039 | +0.482 | 0.6302 |  |
| Site: UW (vs UAB) | +1.4389 | 1.8170 | ±3.6339 | +0.792 | 0.4284 |  |
| Season: spring (vs autumn) | +1.7577 | 1.9623 | ±3.9246 | +0.896 | 0.3704 |  |
| Season: summer (vs autumn) | +1.8872 | 2.0118 | ±4.0237 | +0.938 | 0.3482 |  |
| Season: winter (vs autumn) | +3.4711 | 2.0103 | ±4.0205 | +1.727 | 0.0842 | . |
| Age (years) | -0.1094 | 0.0715 | ±0.1429 | -1.530 | 0.1260 |  |
| BMI (kg/m2) | +0.1549 | 0.0992 | ±0.1985 | +1.561 | 0.1185 |  |
| Hypertension | +2.1266 | 1.5774 | ±3.1548 | +1.348 | 0.1776 |  |
| High cholesterol | -0.0515 | 1.4966 | ±2.9932 | -0.034 | 0.9725 |  |
| Kidney disease | -0.9365 | 2.5567 | ±5.1134 | -0.366 | 0.7142 |  |
| Circulatory disease | -1.0618 | 2.1929 | ±4.3859 | -0.484 | 0.6283 |  |
| Avg. daily SD (mg/dL) | -0.0603 | 0.3189 | ±0.6378 | -0.189 | 0.8500 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **443**, R² = **0.0434**, Adj R² = **0.0121**, F-statistic = **1.39** (p = **0.1556**), Residual SE = **14.211** on **428** df, AIC = **3623.4**, BIC = **3684.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.5772** | 7.2482 | ±14.4965 | **+16.911** | **3.71e-64** | *** |
| Education: graduate level (vs college) | -1.2481 | 1.4256 | ±2.8512 | -0.875 | 0.3813 |  |
| Education: high school or below (vs college) | +3.5362 | 2.6786 | ±5.3572 | +1.320 | 0.1868 |  |
| Site: UCSD (vs UAB) | +1.0187 | 1.8673 | ±3.7346 | +0.546 | 0.5854 |  |
| Site: UW (vs UAB) | +1.5803 | 1.8345 | ±3.6689 | +0.861 | 0.3890 |  |
| Season: spring (vs autumn) | +1.6507 | 1.9706 | ±3.9411 | +0.838 | 0.4022 |  |
| Season: summer (vs autumn) | +1.8543 | 2.0174 | ±4.0348 | +0.919 | 0.3580 |  |
| Season: winter (vs autumn) | +3.3481 | 2.0270 | ±4.0540 | +1.652 | 0.0986 | . |
| Age (years) | -0.1114 | 0.0712 | ±0.1425 | -1.563 | 0.1180 |  |
| BMI (kg/m2) | +0.1524 | 0.0996 | ±0.1992 | +1.531 | 0.1259 |  |
| Hypertension | +2.0758 | 1.5809 | ±3.1617 | +1.313 | 0.1892 |  |
| High cholesterol | +0.0113 | 1.4990 | ±2.9980 | +0.008 | 0.9940 |  |
| Kidney disease | -1.1436 | 2.5537 | ±5.1073 | -0.448 | 0.6543 |  |
| Circulatory disease | -1.1234 | 2.2003 | ±4.4007 | -0.511 | 0.6097 |  |
| CV (%) | +0.2528 | 0.3572 | ±0.7144 | +0.708 | 0.4791 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **443**, R² = **0.0434**, Adj R² = **0.0121**, F-statistic = **1.39** (p = **0.1562**), Residual SE = **14.211** on **428** df, AIC = **3623.4**, BIC = **3684.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.7977** | 8.0514 | ±16.1029 | **+16.121** | **1.81e-58** | *** |
| Education: graduate level (vs college) | -1.2387 | 1.4250 | ±2.8500 | -0.869 | 0.3847 |  |
| Education: high school or below (vs college) | +3.5268 | 2.6764 | ±5.3527 | +1.318 | 0.1876 |  |
| Site: UCSD (vs UAB) | +0.9984 | 1.8636 | ±3.7271 | +0.536 | 0.5921 |  |
| Site: UW (vs UAB) | +1.5606 | 1.8321 | ±3.6641 | +0.852 | 0.3943 |  |
| Season: spring (vs autumn) | +1.6436 | 1.9731 | ±3.9462 | +0.833 | 0.4049 |  |
| Season: summer (vs autumn) | +1.8576 | 2.0156 | ±4.0312 | +0.922 | 0.3567 |  |
| Season: winter (vs autumn) | +3.3521 | 2.0280 | ±4.0559 | +1.653 | 0.0983 | . |
| Age (years) | -0.1109 | 0.0711 | ±0.1422 | -1.560 | 0.1188 |  |
| BMI (kg/m2) | +0.1526 | 0.0995 | ±0.1990 | +1.534 | 0.1251 |  |
| Hypertension | +2.0741 | 1.5813 | ±3.1625 | +1.312 | 0.1896 |  |
| High cholesterol | +0.0153 | 1.4978 | ±2.9956 | +0.010 | 0.9919 |  |
| Kidney disease | -1.0993 | 2.5584 | ±5.1167 | -0.430 | 0.6674 |  |
| Circulatory disease | -1.1031 | 2.1980 | ±4.3960 | -0.502 | 0.6158 |  |
| Mean / SD ratio | -0.5079 | 0.7254 | ±1.4509 | -0.700 | 0.4839 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **443**, R² = **0.0434**, Adj R² = **0.0121**, F-statistic = **1.39** (p = **0.1557**), Residual SE = **14.211** on **428** df, AIC = **3623.4**, BIC = **3684.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.5213** | 7.8551 | ±15.7103 | **+16.489** | **4.42e-61** | *** |
| Education: graduate level (vs college) | -1.2239 | 1.4271 | ±2.8542 | -0.858 | 0.3911 |  |
| Education: high school or below (vs college) | +3.5576 | 2.6843 | ±5.3687 | +1.325 | 0.1851 |  |
| Site: UCSD (vs UAB) | +0.9702 | 1.8581 | ±3.7161 | +0.522 | 0.6016 |  |
| Site: UW (vs UAB) | +1.5384 | 1.8254 | ±3.6508 | +0.843 | 0.3994 |  |
| Season: spring (vs autumn) | +1.6508 | 1.9715 | ±3.9430 | +0.837 | 0.4024 |  |
| Season: summer (vs autumn) | +1.8514 | 2.0152 | ±4.0304 | +0.919 | 0.3582 |  |
| Season: winter (vs autumn) | +3.3911 | 2.0199 | ±4.0399 | +1.679 | 0.0932 | . |
| Age (years) | -0.1120 | 0.0715 | ±0.1431 | -1.566 | 0.1172 |  |
| BMI (kg/m2) | +0.1498 | 0.0998 | ±0.1997 | +1.501 | 0.1334 |  |
| Hypertension | +2.1017 | 1.5798 | ±3.1596 | +1.330 | 0.1834 |  |
| High cholesterol | +0.0003 | 1.4980 | ±2.9959 | +0.000 | 0.9999 |  |
| Kidney disease | -1.1018 | 2.5637 | ±5.1275 | -0.430 | 0.6674 |  |
| Circulatory disease | -1.0387 | 2.1911 | ±4.3822 | -0.474 | 0.6355 |  |
| Avg. daily mean/SD | -0.3962 | 0.5618 | ±1.1235 | -0.705 | 0.4807 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **443**, R² = **0.0528**, Adj R² = **0.0218**, F-statistic = **1.70** (p = **0.0519**), Residual SE = **14.140** on **428** df, AIC = **3619.0**, BIC = **3680.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+116.1585** | 7.3782 | ±14.7564 | **+15.743** | **7.62e-56** | *** |
| Education: graduate level (vs college) | -1.3809 | 1.4219 | ±2.8439 | -0.971 | 0.3315 |  |
| Education: high school or below (vs college) | +3.1503 | 2.6824 | ±5.3647 | +1.174 | 0.2402 |  |
| Site: UCSD (vs UAB) | +1.0724 | 1.8310 | ±3.6620 | +0.586 | 0.5581 |  |
| Site: UW (vs UAB) | +1.8568 | 1.7900 | ±3.5801 | +1.037 | 0.2996 |  |
| Season: spring (vs autumn) | +1.7451 | 1.9419 | ±3.8839 | +0.899 | 0.3689 |  |
| Season: summer (vs autumn) | +2.0131 | 1.9828 | ±3.9656 | +1.015 | 0.3100 |  |
| Season: winter (vs autumn) | +3.3832 | 1.9767 | ±3.9534 | +1.712 | 0.0870 | . |
| Age (years) | -0.0967 | 0.0708 | ±0.1415 | -1.366 | 0.1719 |  |
| BMI (kg/m2) | +0.1644 | 0.1001 | ±0.2001 | +1.642 | 0.1005 |  |
| Hypertension | +2.1784 | 1.5825 | ±3.1650 | +1.377 | 0.1686 |  |
| High cholesterol | -0.1121 | 1.5044 | ±3.0088 | -0.075 | 0.9406 |  |
| Kidney disease | -1.3270 | 2.5729 | ±5.1458 | -0.516 | 0.6060 |  |
| Circulatory disease | -0.8759 | 2.1582 | ±4.3165 | -0.406 | 0.6849 |  |
| **MAG (mg/dL/h)** | **+0.2585** | 0.1276 | ±0.2552 | **+2.026** | **0.0428** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **443**, R² = **0.0428**, Adj R² = **0.0115**, F-statistic = **1.37** (p = **0.1655**), Residual SE = **14.215** on **428** df, AIC = **3623.6**, BIC = **3685.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.1777** | 7.6144 | ±15.2288 | **+16.177** | **7.33e-59** | *** |
| Education: graduate level (vs college) | -1.2910 | 1.4308 | ±2.8616 | -0.902 | 0.3669 |  |
| Education: high school or below (vs college) | +3.5773 | 2.6858 | ±5.3716 | +1.332 | 0.1829 |  |
| Site: UCSD (vs UAB) | +0.9634 | 1.8558 | ±3.7115 | +0.519 | 0.6037 |  |
| Site: UW (vs UAB) | +1.5204 | 1.8199 | ±3.6399 | +0.835 | 0.4035 |  |
| Season: spring (vs autumn) | +1.7067 | 1.9677 | ±3.9355 | +0.867 | 0.3858 |  |
| Season: summer (vs autumn) | +1.8808 | 2.0118 | ±4.0236 | +0.935 | 0.3498 |  |
| Season: winter (vs autumn) | +3.4118 | 2.0140 | ±4.0279 | +1.694 | 0.0902 | . |
| Age (years) | -0.1106 | 0.0711 | ±0.1422 | -1.556 | 0.1198 |  |
| BMI (kg/m2) | +0.1578 | 0.0993 | ±0.1985 | +1.590 | 0.1119 |  |
| Hypertension | +2.1356 | 1.5896 | ±3.1793 | +1.343 | 0.1791 |  |
| High cholesterol | -0.0317 | 1.5024 | ±3.0048 | -0.021 | 0.9832 |  |
| Kidney disease | -1.0750 | 2.5733 | ±5.1466 | -0.418 | 0.6761 |  |
| Circulatory disease | -1.0614 | 2.1911 | ±4.3822 | -0.484 | 0.6281 |  |
| Avg. daily range (mg/dL) | +0.0367 | 0.0716 | ±0.1432 | +0.513 | 0.6081 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **443**, R² = **0.0420**, Adj R² = **0.0107**, F-statistic = **1.34** (p = **0.1800**), Residual SE = **14.221** on **428** df, AIC = **3624.0**, BIC = **3685.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.0764** | 5.8438 | ±11.6876 | **+21.574** | **3.13e-103** | *** |
| Education: graduate level (vs college) | -1.3207 | 1.4308 | ±2.8616 | -0.923 | 0.3560 |  |
| Education: high school or below (vs college) | +3.5781 | 2.6874 | ±5.3749 | +1.331 | 0.1831 |  |
| Site: UCSD (vs UAB) | +0.9153 | 1.8485 | ±3.6971 | +0.495 | 0.6205 |  |
| Site: UW (vs UAB) | +1.4575 | 1.8133 | ±3.6266 | +0.804 | 0.4215 |  |
| Season: spring (vs autumn) | +1.7382 | 1.9748 | ±3.9495 | +0.880 | 0.3787 |  |
| Season: summer (vs autumn) | +1.8792 | 2.0284 | ±4.0568 | +0.926 | 0.3542 |  |
| Season: winter (vs autumn) | +3.4504 | 2.0322 | ±4.0643 | +1.698 | 0.0895 | . |
| Age (years) | -0.1097 | 0.0709 | ±0.1418 | -1.547 | 0.1218 |  |
| BMI (kg/m2) | +0.1533 | 0.0992 | ±0.1985 | +1.545 | 0.1223 |  |
| Hypertension | +2.1042 | 1.6010 | ±3.2020 | +1.314 | 0.1888 |  |
| High cholesterol | -0.0396 | 1.5035 | ±3.0069 | -0.026 | 0.9790 |  |
| Kidney disease | -0.9858 | 2.6008 | ±5.2016 | -0.379 | 0.7047 |  |
| Circulatory disease | -1.0784 | 2.2039 | ±4.4078 | -0.489 | 0.6246 |  |
| SD of daily means (mg/dL) | +0.0271 | 0.3513 | ±0.7025 | +0.077 | 0.9385 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **443**, R² = **0.0429**, Adj R² = **0.0116**, F-statistic = **1.37** (p = **0.1642**), Residual SE = **14.214** on **428** df, AIC = **3623.6**, BIC = **3685.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +269.4891 | 241.0365 | ±482.0730 | +1.118 | 0.2635 |  |
| Education: graduate level (vs college) | -1.3010 | 1.4294 | ±2.8588 | -0.910 | 0.3627 |  |
| Education: high school or below (vs college) | +3.6115 | 2.6982 | ±5.3964 | +1.338 | 0.1807 |  |
| Site: UCSD (vs UAB) | +0.9807 | 1.8604 | ±3.7208 | +0.527 | 0.5981 |  |
| Site: UW (vs UAB) | +1.5156 | 1.8184 | ±3.6368 | +0.833 | 0.4046 |  |
| Season: spring (vs autumn) | +1.7367 | 1.9527 | ±3.9053 | +0.889 | 0.3738 |  |
| Season: summer (vs autumn) | +1.8593 | 2.0127 | ±4.0254 | +0.924 | 0.3556 |  |
| Season: winter (vs autumn) | +3.4055 | 2.0163 | ±4.0325 | +1.689 | 0.0912 | . |
| Age (years) | -0.1087 | 0.0707 | ±0.1415 | -1.537 | 0.1243 |  |
| BMI (kg/m2) | +0.1561 | 0.0978 | ±0.1957 | +1.595 | 0.1107 |  |
| Hypertension | +2.1013 | 1.5834 | ±3.1668 | +1.327 | 0.1845 |  |
| High cholesterol | -0.0636 | 1.5103 | ±3.0206 | -0.042 | 0.9664 |  |
| Kidney disease | -1.0931 | 2.5477 | ±5.0953 | -0.429 | 0.6679 |  |
| Circulatory disease | -1.0458 | 2.1809 | ±4.3619 | -0.480 | 0.6316 |  |
| Time in range 70-180, pooled (%) | -1.4409 | 2.4167 | ±4.8334 | -0.596 | 0.5510 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **443**, R² = **0.0425**, Adj R² = **0.0112**, F-statistic = **1.36** (p = **0.1710**), Residual SE = **14.217** on **428** df, AIC = **3623.8**, BIC = **3685.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +230.3051 | 242.0863 | ±484.1726 | +0.951 | 0.3414 |  |
| Education: graduate level (vs college) | -1.2971 | 1.4336 | ±2.8672 | -0.905 | 0.3656 |  |
| Education: high school or below (vs college) | +3.6141 | 2.7007 | ±5.4015 | +1.338 | 0.1808 |  |
| Site: UCSD (vs UAB) | +0.9326 | 1.8568 | ±3.7136 | +0.502 | 0.6155 |  |
| Site: UW (vs UAB) | +1.4684 | 1.8149 | ±3.6297 | +0.809 | 0.4185 |  |
| Season: spring (vs autumn) | +1.7558 | 1.9485 | ±3.8969 | +0.901 | 0.3675 |  |
| Season: summer (vs autumn) | +1.9119 | 2.0059 | ±4.0117 | +0.953 | 0.3405 |  |
| Season: winter (vs autumn) | +3.4489 | 2.0115 | ±4.0230 | +1.715 | 0.0864 | . |
| Age (years) | -0.1088 | 0.0708 | ±0.1417 | -1.536 | 0.1246 |  |
| BMI (kg/m2) | +0.1540 | 0.0990 | ±0.1980 | +1.555 | 0.1199 |  |
| Hypertension | +2.1381 | 1.5917 | ±3.1833 | +1.343 | 0.1792 |  |
| High cholesterol | -0.0704 | 1.5166 | ±3.0333 | -0.046 | 0.9630 |  |
| Kidney disease | -1.0336 | 2.5762 | ±5.1525 | -0.401 | 0.6883 |  |
| Circulatory disease | -1.0723 | 2.1932 | ±4.3865 | -0.489 | 0.6249 |  |
| Avg. daily time in range 70-180 (%) | -1.0461 | 2.4265 | ±4.8531 | -0.431 | 0.6664 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.0420**, Adj R² = **0.0107**, F-statistic = **1.34** (p = **0.1802**), Residual SE = **14.221** on **428** df, AIC = **3624.0**, BIC = **3685.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2172** | 5.6183 | ±11.2365 | **+22.466** | **9.02e-112** | *** |
| Education: graduate level (vs college) | -1.3175 | 1.4252 | ±2.8504 | -0.924 | 0.3553 |  |
| Education: high school or below (vs college) | +3.5887 | 2.6926 | ±5.3852 | +1.333 | 0.1826 |  |
| Site: UCSD (vs UAB) | +0.8994 | 1.8611 | ±3.7223 | +0.483 | 0.6289 |  |
| Site: UW (vs UAB) | +1.4532 | 1.8059 | ±3.6119 | +0.805 | 0.4210 |  |
| Season: spring (vs autumn) | +1.7527 | 1.9637 | ±3.9273 | +0.893 | 0.3721 |  |
| Season: summer (vs autumn) | +1.8901 | 2.0104 | ±4.0209 | +0.940 | 0.3471 |  |
| Season: winter (vs autumn) | +3.4664 | 2.0218 | ±4.0436 | +1.715 | 0.0864 | . |
| Age (years) | -0.1099 | 0.0707 | ±0.1415 | -1.553 | 0.1204 |  |
| BMI (kg/m2) | +0.1534 | 0.0993 | ±0.1986 | +1.545 | 0.1224 |  |
| Hypertension | +2.1175 | 1.5837 | ±3.1674 | +1.337 | 0.1812 |  |
| High cholesterol | -0.0361 | 1.5028 | ±3.0056 | -0.024 | 0.9808 |  |
| Kidney disease | -0.9933 | 2.5935 | ±5.1870 | -0.383 | 0.7017 |  |
| Circulatory disease | -1.0628 | 2.1908 | ±4.3816 | -0.485 | 0.6276 |  |
| Any reading < 54 during wear (0/1) | -0.0479 | 1.8803 | ±3.7606 | -0.025 | 0.9797 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.0429**, Adj R² = **0.0116**, F-statistic = **1.37** (p = **0.1644**), Residual SE = **14.214** on **428** df, AIC = **3623.6**, BIC = **3685.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.9450** | 5.6752 | ±11.3505 | **+22.192** | **4.10e-109** | *** |
| Education: graduate level (vs college) | -1.3200 | 1.4269 | ±2.8538 | -0.925 | 0.3549 |  |
| Education: high school or below (vs college) | +3.6932 | 2.6947 | ±5.3894 | +1.371 | 0.1705 |  |
| Site: UCSD (vs UAB) | +1.0623 | 1.8636 | ±3.7272 | +0.570 | 0.5687 |  |
| Site: UW (vs UAB) | +1.5353 | 1.8130 | ±3.6259 | +0.847 | 0.3971 |  |
| Season: spring (vs autumn) | +1.7602 | 1.9503 | ±3.9006 | +0.903 | 0.3668 |  |
| Season: summer (vs autumn) | +1.8754 | 2.0101 | ±4.0201 | +0.933 | 0.3508 |  |
| Season: winter (vs autumn) | +3.4208 | 2.0099 | ±4.0198 | +1.702 | 0.0888 | . |
| Age (years) | -0.1066 | 0.0708 | ±0.1416 | -1.505 | 0.1322 |  |
| BMI (kg/m2) | +0.1488 | 0.1004 | ±0.2008 | +1.483 | 0.1381 |  |
| Hypertension | +2.0194 | 1.5959 | ±3.1918 | +1.265 | 0.2057 |  |
| High cholesterol | -0.0056 | 1.5034 | ±3.0067 | -0.004 | 0.9970 |  |
| Kidney disease | -0.9003 | 2.5897 | ±5.1795 | -0.348 | 0.7281 |  |
| Circulatory disease | -1.1163 | 2.1764 | ±4.3528 | -0.513 | 0.6080 |  |
| Time < 54 (%) | +8.1730 | 12.8277 | ±25.6554 | +0.637 | 0.5240 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.0480**, Adj R² = **0.0168**, F-statistic = **1.54** (p = **0.0934**), Residual SE = **14.177** on **428** df, AIC = **3621.2**, BIC = **3682.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7905** | 5.6677 | ±11.3354 | **+22.194** | **3.90e-109** | *** |
| Education: graduate level (vs college) | -1.3433 | 1.4204 | ±2.8409 | -0.946 | 0.3443 |  |
| Education: high school or below (vs college) | +3.7075 | 2.6954 | ±5.3907 | +1.376 | 0.1690 |  |
| Site: UCSD (vs UAB) | +1.0859 | 1.8445 | ±3.6890 | +0.589 | 0.5560 |  |
| Site: UW (vs UAB) | +1.4911 | 1.8016 | ±3.6032 | +0.828 | 0.4079 |  |
| Season: spring (vs autumn) | +1.8379 | 1.9395 | ±3.8790 | +0.948 | 0.3433 |  |
| Season: summer (vs autumn) | +2.0925 | 1.9980 | ±3.9959 | +1.047 | 0.2949 |  |
| Season: winter (vs autumn) | +3.4913 | 1.9935 | ±3.9871 | +1.751 | 0.0799 | . |
| Age (years) | -0.1066 | 0.0707 | ±0.1415 | -1.507 | 0.1318 |  |
| BMI (kg/m2) | +0.1486 | 0.0994 | ±0.1988 | +1.495 | 0.1348 |  |
| Hypertension | +2.0217 | 1.5703 | ±3.1406 | +1.287 | 0.1979 |  |
| High cholesterol | -0.0361 | 1.5033 | ±3.0065 | -0.024 | 0.9809 |  |
| Kidney disease | -0.8626 | 2.5877 | ±5.1754 | -0.333 | 0.7389 |  |
| Circulatory disease | -1.2738 | 2.1574 | ±4.3148 | -0.590 | 0.5549 |  |
| Avg. daily time < 54 (%) | +28.1690 | 15.0602 | ±30.1203 | +1.870 | 0.0614 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.0451**, Adj R² = **0.0138**, F-statistic = **1.44** (p = **0.1297**), Residual SE = **14.198** on **428** df, AIC = **3622.6**, BIC = **3684.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.5349** | 5.6328 | ±11.2656 | **+22.286** | **5.00e-110** | *** |
| Education: graduate level (vs college) | -1.2736 | 1.4165 | ±2.8331 | -0.899 | 0.3686 |  |
| Education: high school or below (vs college) | +3.4180 | 2.7142 | ±5.4284 | +1.259 | 0.2079 |  |
| Site: UCSD (vs UAB) | +1.0419 | 1.8485 | ±3.6970 | +0.564 | 0.5730 |  |
| Site: UW (vs UAB) | +1.6174 | 1.8107 | ±3.6214 | +0.893 | 0.3717 |  |
| Season: spring (vs autumn) | +1.6985 | 1.9444 | ±3.8887 | +0.874 | 0.3823 |  |
| Season: summer (vs autumn) | +1.8467 | 2.0163 | ±4.0326 | +0.916 | 0.3597 |  |
| Season: winter (vs autumn) | +3.3452 | 2.0162 | ±4.0325 | +1.659 | 0.0971 | . |
| Age (years) | -0.1097 | 0.0710 | ±0.1420 | -1.546 | 0.1221 |  |
| BMI (kg/m2) | +0.1538 | 0.0995 | ±0.1990 | +1.546 | 0.1222 |  |
| Hypertension | +2.2190 | 1.5810 | ±3.1619 | +1.404 | 0.1605 |  |
| High cholesterol | -0.1778 | 1.5234 | ±3.0467 | -0.117 | 0.9071 |  |
| Kidney disease | -0.7338 | 2.6362 | ±5.2723 | -0.278 | 0.7807 |  |
| Circulatory disease | -1.0295 | 2.1859 | ±4.3717 | -0.471 | 0.6376 |  |
| Time 54-69, pooled (%) | +4.4375 | 3.7906 | ±7.5811 | +1.171 | 0.2417 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **443**, R² = **0.0451**, Adj R² = **0.0139**, F-statistic = **1.45** (p = **0.1286**), Residual SE = **14.198** on **428** df, AIC = **3622.5**, BIC = **3683.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.6088** | 5.6266 | ±11.2531 | **+22.324** | **2.15e-110** | *** |
| Education: graduate level (vs college) | -1.2387 | 1.4126 | ±2.8253 | -0.877 | 0.3806 |  |
| Education: high school or below (vs college) | +3.4022 | 2.7138 | ±5.4277 | +1.254 | 0.2100 |  |
| Site: UCSD (vs UAB) | +0.9749 | 1.8467 | ±3.6933 | +0.528 | 0.5976 |  |
| Site: UW (vs UAB) | +1.5497 | 1.8050 | ±3.6100 | +0.859 | 0.3906 |  |
| Season: spring (vs autumn) | +1.8008 | 1.9389 | ±3.8779 | +0.929 | 0.3530 |  |
| Season: summer (vs autumn) | +1.9691 | 2.0189 | ±4.0378 | +0.975 | 0.3294 |  |
| Season: winter (vs autumn) | +3.3948 | 2.0146 | ±4.0292 | +1.685 | 0.0920 | . |
| Age (years) | -0.1108 | 0.0711 | ±0.1421 | -1.559 | 0.1190 |  |
| BMI (kg/m2) | +0.1534 | 0.0993 | ±0.1986 | +1.544 | 0.1225 |  |
| Hypertension | +2.3263 | 1.5926 | ±3.1853 | +1.461 | 0.1441 |  |
| High cholesterol | -0.1664 | 1.5222 | ±3.0444 | -0.109 | 0.9130 |  |
| Kidney disease | -0.8103 | 2.6323 | ±5.2645 | -0.308 | 0.7582 |  |
| Circulatory disease | -1.0909 | 2.1852 | ±4.3703 | -0.499 | 0.6176 |  |
| Avg. daily time 54-69 (%) | +4.5622 | 3.7603 | ±7.5206 | +1.213 | 0.2250 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **443**, R² = **0.0453**, Adj R² = **0.0140**, F-statistic = **1.45** (p = **0.1272**), Residual SE = **14.197** on **428** df, AIC = **3622.5**, BIC = **3683.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.4617** | 5.6423 | ±11.2846 | **+22.236** | **1.54e-109** | *** |
| Education: graduate level (vs college) | -1.2787 | 1.4174 | ±2.8348 | -0.902 | 0.3670 |  |
| Education: high school or below (vs college) | +3.4836 | 2.7128 | ±5.4257 | +1.284 | 0.1991 |  |
| Site: UCSD (vs UAB) | +1.1073 | 1.8525 | ±3.7049 | +0.598 | 0.5500 |  |
| Site: UW (vs UAB) | +1.6423 | 1.8113 | ±3.6227 | +0.907 | 0.3646 |  |
| Season: spring (vs autumn) | +1.7092 | 1.9425 | ±3.8851 | +0.880 | 0.3789 |  |
| Season: summer (vs autumn) | +1.8445 | 2.0130 | ±4.0260 | +0.916 | 0.3595 |  |
| Season: winter (vs autumn) | +3.3348 | 2.0149 | ±4.0299 | +1.655 | 0.0979 | . |
| Age (years) | -0.1081 | 0.0709 | ±0.1418 | -1.525 | 0.1273 |  |
| BMI (kg/m2) | +0.1515 | 0.0999 | ±0.1997 | +1.517 | 0.1293 |  |
| Hypertension | +2.1628 | 1.5798 | ±3.1596 | +1.369 | 0.1710 |  |
| High cholesterol | -0.1507 | 1.5183 | ±3.0366 | -0.099 | 0.9210 |  |
| Kidney disease | -0.7117 | 2.6331 | ±5.2662 | -0.270 | 0.7869 |  |
| Circulatory disease | -1.0583 | 2.1807 | ±4.3615 | -0.485 | 0.6275 |  |
| Time < 70 (%) | +4.0626 | 3.3479 | ±6.6958 | +1.213 | 0.2250 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **443**, R² = **0.0465**, Adj R² = **0.0153**, F-statistic = **1.49** (p = **0.1106**), Residual SE = **14.187** on **428** df, AIC = **3621.9**, BIC = **3683.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.4805** | 5.6244 | ±11.2488 | **+22.310** | **2.95e-110** | *** |
| Education: graduate level (vs college) | -1.2362 | 1.4119 | ±2.8237 | -0.876 | 0.3813 |  |
| Education: high school or below (vs college) | +3.4057 | 2.7176 | ±5.4353 | +1.253 | 0.2101 |  |
| Site: UCSD (vs UAB) | +1.0125 | 1.8452 | ±3.6904 | +0.549 | 0.5832 |  |
| Site: UW (vs UAB) | +1.5640 | 1.8023 | ±3.6046 | +0.868 | 0.3855 |  |
| Season: spring (vs autumn) | +1.8219 | 1.9355 | ±3.8710 | +0.941 | 0.3466 |  |
| Season: summer (vs autumn) | +2.0130 | 2.0161 | ±4.0323 | +0.998 | 0.3181 |  |
| Season: winter (vs autumn) | +3.3939 | 2.0120 | ±4.0240 | +1.687 | 0.0916 | . |
| Age (years) | -0.1103 | 0.0710 | ±0.1421 | -1.553 | 0.1205 |  |
| BMI (kg/m2) | +0.1525 | 0.0993 | ±0.1987 | +1.536 | 0.1246 |  |
| Hypertension | +2.3293 | 1.5865 | ±3.1731 | +1.468 | 0.1421 |  |
| High cholesterol | -0.1783 | 1.5208 | ±3.0417 | -0.117 | 0.9067 |  |
| Kidney disease | -0.7719 | 2.6318 | ±5.2636 | -0.293 | 0.7693 |  |
| Circulatory disease | -1.1303 | 2.1794 | ±4.3588 | -0.519 | 0.6040 |  |
| Avg. daily time < 70 (%) | +4.9804 | 3.4454 | ±6.8909 | +1.446 | 0.1483 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.0422**, Adj R² = **0.0109**, F-statistic = **1.35** (p = **0.1755**), Residual SE = **14.219** on **428** df, AIC = **3623.9**, BIC = **3685.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +556.8655 | 1324.3762 | ±2648.7524 | +0.420 | 0.6741 |  |
| Education: graduate level (vs college) | -1.3191 | 1.4286 | ±2.8572 | -0.923 | 0.3558 |  |
| Education: high school or below (vs college) | +3.6463 | 2.6945 | ±5.3889 | +1.353 | 0.1760 |  |
| Site: UCSD (vs UAB) | +0.9955 | 1.8645 | ±3.7290 | +0.534 | 0.5934 |  |
| Site: UW (vs UAB) | +1.5035 | 1.8141 | ±3.6282 | +0.829 | 0.4072 |  |
| Season: spring (vs autumn) | +1.7497 | 1.9533 | ±3.9065 | +0.896 | 0.3704 |  |
| Season: summer (vs autumn) | +1.8814 | 2.0146 | ±4.0291 | +0.934 | 0.3504 |  |
| Season: winter (vs autumn) | +3.4364 | 2.0152 | ±4.0304 | +1.705 | 0.0881 | . |
| Age (years) | -0.1078 | 0.0708 | ±0.1415 | -1.524 | 0.1275 |  |
| BMI (kg/m2) | +0.1513 | 0.1000 | ±0.2000 | +1.513 | 0.1304 |  |
| Hypertension | +2.0664 | 1.5945 | ±3.1891 | +1.296 | 0.1950 |  |
| High cholesterol | -0.0213 | 1.5026 | ±3.0052 | -0.014 | 0.9887 |  |
| Kidney disease | -0.9420 | 2.5902 | ±5.1803 | -0.364 | 0.7161 |  |
| Circulatory disease | -1.0926 | 2.1818 | ±4.3635 | -0.501 | 0.6165 |  |
| Time 54-250, pooled (%) | -4.3083 | 13.2439 | ±26.4879 | -0.325 | 0.7450 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.0452**, Adj R² = **0.0140**, F-statistic = **1.45** (p = **0.1277**), Residual SE = **14.197** on **428** df, AIC = **3622.5**, BIC = **3683.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2148.4726 | 1758.0223 | ±3516.0446 | +1.222 | 0.2217 |  |
| Education: graduate level (vs college) | -1.3380 | 1.4250 | ±2.8500 | -0.939 | 0.3477 |  |
| Education: high school or below (vs college) | +3.6829 | 2.6928 | ±5.3855 | +1.368 | 0.1714 |  |
| Site: UCSD (vs UAB) | +1.0677 | 1.8486 | ±3.6973 | +0.578 | 0.5635 |  |
| Site: UW (vs UAB) | +1.5063 | 1.8095 | ±3.6190 | +0.832 | 0.4052 |  |
| Season: spring (vs autumn) | +1.7903 | 1.9446 | ±3.8892 | +0.921 | 0.3572 |  |
| Season: summer (vs autumn) | +2.0378 | 2.0008 | ±4.0017 | +1.018 | 0.3084 |  |
| Season: winter (vs autumn) | +3.4643 | 1.9993 | ±3.9987 | +1.733 | 0.0832 | . |
| Age (years) | -0.1061 | 0.0708 | ±0.1415 | -1.499 | 0.1338 |  |
| BMI (kg/m2) | +0.1514 | 0.0992 | ±0.1985 | +1.525 | 0.1271 |  |
| Hypertension | +2.0585 | 1.5727 | ±3.1455 | +1.309 | 0.1906 |  |
| High cholesterol | -0.0425 | 1.5049 | ±3.0098 | -0.028 | 0.9775 |  |
| Kidney disease | -0.8998 | 2.5872 | ±5.1744 | -0.348 | 0.7280 |  |
| Circulatory disease | -1.2191 | 2.1674 | ±4.3349 | -0.562 | 0.5738 |  |
| Avg. daily time 54-250 (%) | -20.2271 | 17.5788 | ±35.1575 | -1.151 | 0.2499 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **443**, R² = **0.0420**, Adj R² = **0.0107**, F-statistic = **1.34** (p = **0.1793**), Residual SE = **14.221** on **428** df, AIC = **3624.0**, BIC = **3685.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.3382** | 5.7163 | ±11.4327 | **+22.101** | **3.08e-108** | *** |
| Education: graduate level (vs college) | -1.3177 | 1.4283 | ±2.8567 | -0.923 | 0.3562 |  |
| Education: high school or below (vs college) | +3.5761 | 2.6939 | ±5.3878 | +1.327 | 0.1844 |  |
| Site: UCSD (vs UAB) | +0.9079 | 1.8481 | ±3.6961 | +0.491 | 0.6233 |  |
| Site: UW (vs UAB) | +1.4603 | 1.8117 | ±3.6234 | +0.806 | 0.4202 |  |
| Season: spring (vs autumn) | +1.7458 | 1.9507 | ±3.9013 | +0.895 | 0.3708 |  |
| Season: summer (vs autumn) | +1.8898 | 2.0147 | ±4.0294 | +0.938 | 0.3483 |  |
| Season: winter (vs autumn) | +3.4638 | 2.0087 | ±4.0173 | +1.724 | 0.0846 | . |
| Age (years) | -0.1099 | 0.0709 | ±0.1419 | -1.549 | 0.1213 |  |
| BMI (kg/m2) | +0.1526 | 0.1001 | ±0.2001 | +1.525 | 0.1272 |  |
| Hypertension | +2.1222 | 1.5784 | ±3.1568 | +1.345 | 0.1788 |  |
| High cholesterol | -0.0394 | 1.5024 | ±3.0048 | -0.026 | 0.9791 |  |
| Kidney disease | -0.9375 | 2.5751 | ±5.1502 | -0.364 | 0.7158 |  |
| Circulatory disease | -1.0686 | 2.1857 | ±4.3713 | -0.489 | 0.6249 |  |
| Time 181-250, pooled (%) | -0.3571 | 2.5811 | ±5.1622 | -0.138 | 0.8900 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **443**, R² = **0.0423**, Adj R² = **0.0110**, F-statistic = **1.35** (p = **0.1737**), Residual SE = **14.218** on **428** df, AIC = **3623.8**, BIC = **3685.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.5254** | 5.7094 | ±11.4189 | **+22.161** | **8.22e-109** | *** |
| Education: graduate level (vs college) | -1.3199 | 1.4283 | ±2.8566 | -0.924 | 0.3554 |  |
| Education: high school or below (vs college) | +3.5337 | 2.7031 | ±5.4063 | +1.307 | 0.1911 |  |
| Site: UCSD (vs UAB) | +0.9069 | 1.8446 | ±3.6891 | +0.492 | 0.6230 |  |
| Site: UW (vs UAB) | +1.4700 | 1.8093 | ±3.6185 | +0.812 | 0.4165 |  |
| Season: spring (vs autumn) | +1.7522 | 1.9536 | ±3.9073 | +0.897 | 0.3698 |  |
| Season: summer (vs autumn) | +1.8880 | 2.0147 | ±4.0294 | +0.937 | 0.3487 |  |
| Season: winter (vs autumn) | +3.4590 | 2.0084 | ±4.0167 | +1.722 | 0.0850 | . |
| Age (years) | -0.1108 | 0.0709 | ±0.1418 | -1.563 | 0.1181 |  |
| BMI (kg/m2) | +0.1528 | 0.0995 | ±0.1991 | +1.535 | 0.1249 |  |
| Hypertension | +2.1349 | 1.5782 | ±3.1564 | +1.353 | 0.1761 |  |
| High cholesterol | -0.0323 | 1.5056 | ±3.0112 | -0.021 | 0.9829 |  |
| Kidney disease | -0.9042 | 2.5815 | ±5.1630 | -0.350 | 0.7261 |  |
| Circulatory disease | -1.0700 | 2.1841 | ±4.3683 | -0.490 | 0.6242 |  |
| Avg. daily time 181-250 (%) | -0.9606 | 2.6811 | ±5.3622 | -0.358 | 0.7201 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **443**, R² = **0.0421**, Adj R² = **0.0107**, F-statistic = **1.34** (p = **0.1786**), Residual SE = **14.220** on **428** df, AIC = **3624.0**, BIC = **3685.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.3883** | 5.7211 | ±11.4422 | **+22.092** | **3.80e-108** | *** |
| Education: graduate level (vs college) | -1.3179 | 1.4282 | ±2.8564 | -0.923 | 0.3561 |  |
| Education: high school or below (vs college) | +3.5708 | 2.6940 | ±5.3880 | +1.325 | 0.1850 |  |
| Site: UCSD (vs UAB) | +0.9072 | 1.8477 | ±3.6954 | +0.491 | 0.6234 |  |
| Site: UW (vs UAB) | +1.4606 | 1.8116 | ±3.6232 | +0.806 | 0.4201 |  |
| Season: spring (vs autumn) | +1.7459 | 1.9507 | ±3.9014 | +0.895 | 0.3708 |  |
| Season: summer (vs autumn) | +1.8908 | 2.0150 | ±4.0300 | +0.938 | 0.3481 |  |
| Season: winter (vs autumn) | +3.4651 | 2.0087 | ±4.0174 | +1.725 | 0.0845 | . |
| Age (years) | -0.1100 | 0.0709 | ±0.1419 | -1.551 | 0.1210 |  |
| BMI (kg/m2) | +0.1523 | 0.1002 | ±0.2005 | +1.519 | 0.1287 |  |
| Hypertension | +2.1248 | 1.5783 | ±3.1566 | +1.346 | 0.1782 |  |
| High cholesterol | -0.0405 | 1.5025 | ±3.0050 | -0.027 | 0.9785 |  |
| Kidney disease | -0.9195 | 2.5772 | ±5.1543 | -0.357 | 0.7213 |  |
| Circulatory disease | -1.0699 | 2.1860 | ±4.3721 | -0.489 | 0.6245 |  |
| Time > 180 (%) | -0.4844 | 2.5785 | ±5.1570 | -0.188 | 0.8510 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **443**, R² = **0.0424**, Adj R² = **0.0111**, F-statistic = **1.36** (p = **0.1718**), Residual SE = **14.218** on **428** df, AIC = **3623.8**, BIC = **3685.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.5777** | 5.7102 | ±11.4203 | **+22.167** | **7.13e-109** | *** |
| Education: graduate level (vs college) | -1.3202 | 1.4280 | ±2.8560 | -0.924 | 0.3552 |  |
| Education: high school or below (vs college) | +3.5254 | 2.7032 | ±5.4064 | +1.304 | 0.1922 |  |
| Site: UCSD (vs UAB) | +0.9050 | 1.8439 | ±3.6878 | +0.491 | 0.6236 |  |
| Site: UW (vs UAB) | +1.4703 | 1.8090 | ±3.6180 | +0.813 | 0.4164 |  |
| Season: spring (vs autumn) | +1.7541 | 1.9538 | ±3.9076 | +0.898 | 0.3693 |  |
| Season: summer (vs autumn) | +1.8880 | 2.0150 | ±4.0300 | +0.937 | 0.3488 |  |
| Season: winter (vs autumn) | +3.4597 | 2.0084 | ±4.0168 | +1.723 | 0.0850 | . |
| Age (years) | -0.1110 | 0.0709 | ±0.1418 | -1.566 | 0.1174 |  |
| BMI (kg/m2) | +0.1526 | 0.0996 | ±0.1992 | +1.532 | 0.1254 |  |
| Hypertension | +2.1371 | 1.5781 | ±3.1562 | +1.354 | 0.1757 |  |
| High cholesterol | -0.0314 | 1.5057 | ±3.0114 | -0.021 | 0.9834 |  |
| Kidney disease | -0.8925 | 2.5829 | ±5.1658 | -0.346 | 0.7297 |  |
| Circulatory disease | -1.0706 | 2.1840 | ±4.3681 | -0.490 | 0.6240 |  |
| Avg. daily time > 180 (%) | -1.0940 | 2.6758 | ±5.3516 | -0.409 | 0.6827 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **443**, R² = **0.0431**, Adj R² = **0.0118**, F-statistic = **1.38** (p = **0.1598**), Residual SE = **14.212** on **428** df, AIC = **3623.5**, BIC = **3684.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.8066** | 5.7513 | ±11.5027 | **+21.874** | **4.56e-106** | *** |
| Education: graduate level (vs college) | -1.2632 | 1.4294 | ±2.8587 | -0.884 | 0.3768 |  |
| Education: high school or below (vs college) | +3.6248 | 2.6836 | ±5.3672 | +1.351 | 0.1768 |  |
| Site: UCSD (vs UAB) | +0.9051 | 1.8518 | ±3.7036 | +0.489 | 0.6250 |  |
| Site: UW (vs UAB) | +1.4199 | 1.8064 | ±3.6127 | +0.786 | 0.4318 |  |
| Season: spring (vs autumn) | +1.7189 | 1.9490 | ±3.8979 | +0.882 | 0.3778 |  |
| Season: summer (vs autumn) | +1.9141 | 2.0070 | ±4.0141 | +0.954 | 0.3402 |  |
| Season: winter (vs autumn) | +3.3342 | 2.0014 | ±4.0028 | +1.666 | 0.0957 | . |
| Age (years) | -0.1024 | 0.0714 | ±0.1428 | -1.434 | 0.1516 |  |
| BMI (kg/m2) | +0.1489 | 0.1005 | ±0.2010 | +1.482 | 0.1385 |  |
| Hypertension | +2.0098 | 1.5872 | ±3.1744 | +1.266 | 0.2054 |  |
| High cholesterol | -0.0648 | 1.4974 | ±2.9948 | -0.043 | 0.9655 |  |
| Kidney disease | -1.0003 | 2.5927 | ±5.1855 | -0.386 | 0.6996 |  |
| Circulatory disease | -1.0041 | 2.1877 | ±4.3754 | -0.459 | 0.6463 |  |
| Nocturnal time > 180 (%) | +1.4009 | 1.8332 | ±3.6664 | +0.764 | 0.4447 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Total analysis base - Home environment

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 112 single-predictor tests; 2 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 443): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.079 vs 0.075 for covariates alone, gain +0.004; -0.0811 per SD, p = 0.076). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Indoor temperature, mean (deg C)** (n = 443): best single predictor out of sample is **Daily range** (CV R² 0.300 vs 0.292 for covariates alone, gain +0.008; -0.239 per SD, p = 0.012). Raw p < 0.05 (FDR not applicable here): Daily range (p = 0.012).
- **Indoor relative humidity, mean (%)** (n = 443): best single predictor out of sample is **%>180 nocturnal** (CV R² 0.223 vs 0.220 for covariates alone, gain +0.003; -0.39 per SD, p = 0.194). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Indoor VOC index, mean** (n = 443): best single predictor out of sample is **%<54 (daily avg)** (CV R² -0.028 vs -0.037 for covariates alone, gain +0.009; +1.12 per SD, p = 0.061). Raw p < 0.05 (FDR not applicable here): MAG (p = 0.043).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Indoor VOC index, mean (+0.009, via %<54 (daily avg)); Indoor temperature, mean (deg C) (+0.008, via Daily range); Indoor PM2.5, log(1 + mean ug/m3) (+0.004, via %>180 nocturnal); Indoor relative humidity, mean (%) (+0.003, via %>180 nocturnal). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (0 FDR-significant / 2 raw-significant of 32); HbA1c (0 FDR-significant / 0 raw-significant of 4); CGM level (0 FDR-significant / 0 raw-significant of 12).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (2 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Indoor PM2.5, log(1 + mean ug/m3) (%<54 (daily avg), ΔAIC -4.1); Indoor temperature, mean (Daily range, ΔAIC -6.7); Indoor VOC index, mean (MAG, ΔAIC -3.9).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
