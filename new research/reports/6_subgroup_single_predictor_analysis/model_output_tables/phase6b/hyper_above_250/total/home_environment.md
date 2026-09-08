# Phase 6b model output tables - Hyperglycaemia exposure: at least one reading > 250 - Total analysis base - Home environment

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 783; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **783**, R² = **0.1867**, Adj R² = **0.1729**, F-statistic = **13.58** (p = **1.96e-27**), Residual SE = **0.896** on **769** df, AIC = **2063.8**, BIC = **2129.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0481** | 0.3027 | ±0.6055 | **+10.069** | **7.61e-24** | *** |
| Education: graduate level (vs college) | -0.1230 | 0.0666 | ±0.1331 | -1.848 | 0.0646 | . |
| **Education: high school or below (vs college)** | **+0.4850** | 0.1163 | ±0.2326 | **+4.170** | **3.05e-05** | *** |
| Site: UCSD (vs UAB) | +0.0036 | 0.0775 | ±0.1550 | +0.046 | 0.9634 |  |
| **Site: UW (vs UAB)** | **-0.4477** | 0.0796 | ±0.1593 | **-5.621** | **1.90e-08** | *** |
| Season: spring (vs autumn) | -0.0969 | 0.0881 | ±0.1762 | -1.099 | 0.2717 |  |
| Season: summer (vs autumn) | +0.0955 | 0.0890 | ±0.1780 | +1.073 | 0.2834 |  |
| Season: winter (vs autumn) | +0.0567 | 0.0965 | ±0.1929 | +0.587 | 0.5569 |  |
| **Age (years)** | **-0.0216** | 0.0031 | ±0.0063 | **-6.878** | **6.07e-12** | *** |
| BMI (kg/m2) | +0.0099 | 0.0054 | ±0.0107 | +1.843 | 0.0654 | . |
| Hypertension | +0.0327 | 0.0685 | ±0.1371 | +0.477 | 0.6334 |  |
| High cholesterol | +0.0420 | 0.0655 | ±0.1311 | +0.641 | 0.5214 |  |
| Kidney disease | -0.0324 | 0.0879 | ±0.1758 | -0.369 | 0.7125 |  |
| Circulatory disease | +0.0262 | 0.0827 | ±0.1654 | +0.317 | 0.7515 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **783**, R² = **0.2002**, Adj R² = **0.1856**, F-statistic = **13.73** (p = **1.82e-29**), Residual SE = **0.889** on **768** df, AIC = **2052.7**, BIC = **2122.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5134** | 0.3413 | ±0.6826 | **+7.364** | **1.79e-13** | *** |
| Education: graduate level (vs college) | -0.1057 | 0.0670 | ±0.1339 | -1.578 | 0.1145 |  |
| **Education: high school or below (vs college)** | **+0.4359** | 0.1124 | ±0.2247 | **+3.879** | **1.05e-04** | *** |
| Site: UCSD (vs UAB) | +0.0205 | 0.0775 | ±0.1550 | +0.264 | 0.7915 |  |
| **Site: UW (vs UAB)** | **-0.4243** | 0.0789 | ±0.1579 | **-5.375** | **7.64e-08** | *** |
| Season: spring (vs autumn) | -0.0875 | 0.0879 | ±0.1759 | -0.995 | 0.3195 |  |
| Season: summer (vs autumn) | +0.1079 | 0.0884 | ±0.1769 | +1.220 | 0.2225 |  |
| Season: winter (vs autumn) | +0.0578 | 0.0955 | ±0.1910 | +0.605 | 0.5449 |  |
| **Age (years)** | **-0.0214** | 0.0031 | ±0.0062 | **-6.879** | **6.02e-12** | *** |
| BMI (kg/m2) | +0.0071 | 0.0055 | ±0.0111 | +1.280 | 0.2004 |  |
| Hypertension | +0.0204 | 0.0680 | ±0.1360 | +0.300 | 0.7641 |  |
| High cholesterol | +0.0320 | 0.0654 | ±0.1308 | +0.490 | 0.6242 |  |
| Kidney disease | -0.0358 | 0.0873 | ±0.1746 | -0.411 | 0.6813 |  |
| Circulatory disease | +0.0071 | 0.0829 | ±0.1657 | +0.085 | 0.9320 |  |
| **HbA1c (%)** | **+0.0891** | 0.0314 | ±0.0627 | **+2.842** | **0.0045** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **783**, R² = **0.1934**, Adj R² = **0.1786**, F-statistic = **13.15** (p = **3.85e-28**), Residual SE = **0.893** on **768** df, AIC = **2059.3**, BIC = **2129.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.7491** | 0.3231 | ±0.6462 | **+8.508** | **1.77e-17** | *** |
| Education: graduate level (vs college) | -0.1154 | 0.0667 | ±0.1334 | -1.729 | 0.0837 | . |
| **Education: high school or below (vs college)** | **+0.4533** | 0.1132 | ±0.2263 | **+4.006** | **6.18e-05** | *** |
| Site: UCSD (vs UAB) | +0.0194 | 0.0774 | ±0.1548 | +0.251 | 0.8020 |  |
| **Site: UW (vs UAB)** | **-0.4320** | 0.0796 | ±0.1592 | **-5.428** | **5.71e-08** | *** |
| Season: spring (vs autumn) | -0.1041 | 0.0885 | ±0.1771 | -1.176 | 0.2397 |  |
| Season: summer (vs autumn) | +0.1062 | 0.0889 | ±0.1778 | +1.195 | 0.2320 |  |
| Season: winter (vs autumn) | +0.0548 | 0.0959 | ±0.1917 | +0.572 | 0.5676 |  |
| **Age (years)** | **-0.0213** | 0.0031 | ±0.0062 | **-6.845** | **7.64e-12** | *** |
| BMI (kg/m2) | +0.0081 | 0.0055 | ±0.0110 | +1.479 | 0.1391 |  |
| Hypertension | +0.0265 | 0.0686 | ±0.1373 | +0.387 | 0.6990 |  |
| High cholesterol | +0.0390 | 0.0656 | ±0.1312 | +0.595 | 0.5517 |  |
| Kidney disease | -0.0453 | 0.0876 | ±0.1752 | -0.517 | 0.6050 |  |
| Circulatory disease | +0.0117 | 0.0831 | ±0.1663 | +0.141 | 0.8881 |  |
| **Mean glucose (mg/dL)** | **+0.0021** | 0.0010 | ±0.0019 | **+2.166** | **0.0303** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **783**, R² = **0.1934**, Adj R² = **0.1786**, F-statistic = **13.15** (p = **3.85e-28**), Residual SE = **0.893** on **768** df, AIC = **2059.3**, BIC = **2129.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4597** | 0.3917 | ±0.7834 | **+6.280** | **3.40e-10** | *** |
| Education: graduate level (vs college) | -0.1154 | 0.0667 | ±0.1334 | -1.729 | 0.0837 | . |
| **Education: high school or below (vs college)** | **+0.4533** | 0.1132 | ±0.2263 | **+4.006** | **6.18e-05** | *** |
| Site: UCSD (vs UAB) | +0.0194 | 0.0774 | ±0.1548 | +0.251 | 0.8020 |  |
| **Site: UW (vs UAB)** | **-0.4320** | 0.0796 | ±0.1592 | **-5.428** | **5.71e-08** | *** |
| Season: spring (vs autumn) | -0.1041 | 0.0885 | ±0.1771 | -1.176 | 0.2397 |  |
| Season: summer (vs autumn) | +0.1062 | 0.0889 | ±0.1778 | +1.195 | 0.2320 |  |
| Season: winter (vs autumn) | +0.0548 | 0.0959 | ±0.1917 | +0.572 | 0.5676 |  |
| **Age (years)** | **-0.0213** | 0.0031 | ±0.0062 | **-6.845** | **7.64e-12** | *** |
| BMI (kg/m2) | +0.0081 | 0.0055 | ±0.0110 | +1.479 | 0.1391 |  |
| Hypertension | +0.0265 | 0.0686 | ±0.1373 | +0.387 | 0.6990 |  |
| High cholesterol | +0.0390 | 0.0656 | ±0.1312 | +0.595 | 0.5517 |  |
| Kidney disease | -0.0453 | 0.0876 | ±0.1752 | -0.517 | 0.6050 |  |
| Circulatory disease | +0.0117 | 0.0831 | ±0.1663 | +0.141 | 0.8881 |  |
| **GMI (%)** | **+0.0874** | 0.0404 | ±0.0807 | **+2.166** | **0.0303** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **783**, R² = **0.1962**, Adj R² = **0.1816**, F-statistic = **13.39** (p = **1.06e-28**), Residual SE = **0.891** on **768** df, AIC = **2056.5**, BIC = **2126.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.7205** | 0.3149 | ±0.6297 | **+8.640** | **5.61e-18** | *** |
| Education: graduate level (vs college) | -0.1100 | 0.0667 | ±0.1334 | -1.648 | 0.0994 | . |
| **Education: high school or below (vs college)** | **+0.4513** | 0.1129 | ±0.2258 | **+3.996** | **6.43e-05** | *** |
| Site: UCSD (vs UAB) | +0.0213 | 0.0771 | ±0.1543 | +0.276 | 0.7824 |  |
| **Site: UW (vs UAB)** | **-0.4352** | 0.0793 | ±0.1586 | **-5.488** | **4.06e-08** | *** |
| Season: spring (vs autumn) | -0.1099 | 0.0884 | ±0.1767 | -1.243 | 0.2137 |  |
| Season: summer (vs autumn) | +0.1089 | 0.0885 | ±0.1771 | +1.230 | 0.2185 |  |
| Season: winter (vs autumn) | +0.0518 | 0.0956 | ±0.1913 | +0.541 | 0.5882 |  |
| **Age (years)** | **-0.0209** | 0.0031 | ±0.0062 | **-6.727** | **1.73e-11** | *** |
| BMI (kg/m2) | +0.0073 | 0.0055 | ±0.0111 | +1.311 | 0.1898 |  |
| Hypertension | +0.0277 | 0.0687 | ±0.1373 | +0.403 | 0.6867 |  |
| High cholesterol | +0.0392 | 0.0656 | ±0.1311 | +0.598 | 0.5500 |  |
| Kidney disease | -0.0378 | 0.0867 | ±0.1734 | -0.436 | 0.6629 |  |
| Circulatory disease | +0.0104 | 0.0828 | ±0.1657 | +0.126 | 0.9001 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0024** | 0.0009 | ±0.0018 | **+2.615** | **0.0089** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **783**, R² = **0.1920**, Adj R² = **0.1772**, F-statistic = **13.03** (p = **7.11e-28**), Residual SE = **0.894** on **768** df, AIC = **2060.7**, BIC = **2130.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8543** | 0.3092 | ±0.6183 | **+9.232** | **2.65e-20** | *** |
| Education: graduate level (vs college) | -0.1122 | 0.0668 | ±0.1337 | -1.679 | 0.0932 | . |
| **Education: high school or below (vs college)** | **+0.4627** | 0.1154 | ±0.2308 | **+4.009** | **6.11e-05** | *** |
| Site: UCSD (vs UAB) | +0.0177 | 0.0774 | ±0.1549 | +0.228 | 0.8195 |  |
| **Site: UW (vs UAB)** | **-0.4245** | 0.0798 | ±0.1595 | **-5.323** | **1.02e-07** | *** |
| Season: spring (vs autumn) | -0.1040 | 0.0885 | ±0.1769 | -1.176 | 0.2396 |  |
| Season: summer (vs autumn) | +0.1028 | 0.0889 | ±0.1778 | +1.156 | 0.2477 |  |
| Season: winter (vs autumn) | +0.0545 | 0.0960 | ±0.1919 | +0.568 | 0.5700 |  |
| **Age (years)** | **-0.0217** | 0.0031 | ±0.0063 | **-6.906** | **4.99e-12** | *** |
| BMI (kg/m2) | +0.0085 | 0.0054 | ±0.0107 | +1.582 | 0.1136 |  |
| Hypertension | +0.0232 | 0.0684 | ±0.1368 | +0.339 | 0.7345 |  |
| High cholesterol | +0.0457 | 0.0657 | ±0.1315 | +0.695 | 0.4871 |  |
| Kidney disease | -0.0715 | 0.0866 | ±0.1732 | -0.826 | 0.4089 |  |
| Circulatory disease | +0.0154 | 0.0831 | ±0.1662 | +0.185 | 0.8532 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0063** | 0.0028 | ±0.0056 | **+2.240** | **0.0251** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **783**, R² = **0.1897**, Adj R² = **0.1749**, F-statistic = **12.84** (p = **1.95e-27**), Residual SE = **0.895** on **768** df, AIC = **2062.9**, BIC = **2132.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8955** | 0.3111 | ±0.6222 | **+9.308** | **1.31e-20** | *** |
| Education: graduate level (vs college) | -0.1166 | 0.0668 | ±0.1335 | -1.747 | 0.0807 | . |
| **Education: high school or below (vs college)** | **+0.4664** | 0.1162 | ±0.2323 | **+4.015** | **5.95e-05** | *** |
| Site: UCSD (vs UAB) | +0.0144 | 0.0777 | ±0.1554 | +0.186 | 0.8528 |  |
| **Site: UW (vs UAB)** | **-0.4316** | 0.0799 | ±0.1599 | **-5.399** | **6.72e-08** | *** |
| Season: spring (vs autumn) | -0.1020 | 0.0883 | ±0.1767 | -1.155 | 0.2480 |  |
| Season: summer (vs autumn) | +0.1016 | 0.0892 | ±0.1784 | +1.139 | 0.2547 |  |
| Season: winter (vs autumn) | +0.0572 | 0.0963 | ±0.1926 | +0.594 | 0.5525 |  |
| **Age (years)** | **-0.0217** | 0.0031 | ±0.0063 | **-6.908** | **4.92e-12** | *** |
| BMI (kg/m2) | +0.0091 | 0.0054 | ±0.0108 | +1.685 | 0.0920 | . |
| Hypertension | +0.0264 | 0.0684 | ±0.1369 | +0.386 | 0.6992 |  |
| High cholesterol | +0.0445 | 0.0658 | ±0.1315 | +0.676 | 0.4990 |  |
| Kidney disease | -0.0638 | 0.0869 | ±0.1739 | -0.734 | 0.4630 |  |
| Circulatory disease | +0.0193 | 0.0832 | ±0.1664 | +0.232 | 0.8163 |  |
| Avg. daily SD (mg/dL) | +0.0054 | 0.0031 | ±0.0062 | +1.734 | 0.0830 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **783**, R² = **0.1871**, Adj R² = **0.1723**, F-statistic = **12.62** (p = **6.19e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.4**, BIC = **2135.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9665** | 0.3355 | ±0.6711 | **+8.841** | **9.50e-19** | *** |
| Education: graduate level (vs college) | -0.1207 | 0.0668 | ±0.1336 | -1.807 | 0.0708 | . |
| **Education: high school or below (vs college)** | **+0.4842** | 0.1167 | ±0.2334 | **+4.149** | **3.34e-05** | *** |
| Site: UCSD (vs UAB) | +0.0059 | 0.0777 | ±0.1553 | +0.076 | 0.9397 |  |
| **Site: UW (vs UAB)** | **-0.4425** | 0.0798 | ±0.1597 | **-5.542** | **2.99e-08** | *** |
| Season: spring (vs autumn) | -0.0970 | 0.0883 | ±0.1766 | -1.098 | 0.2721 |  |
| Season: summer (vs autumn) | +0.0957 | 0.0890 | ±0.1781 | +1.075 | 0.2823 |  |
| Season: winter (vs autumn) | +0.0566 | 0.0966 | ±0.1932 | +0.586 | 0.5580 |  |
| **Age (years)** | **-0.0217** | 0.0031 | ±0.0063 | **-6.882** | **5.91e-12** | *** |
| BMI (kg/m2) | +0.0098 | 0.0053 | ±0.0107 | +1.831 | 0.0671 | . |
| Hypertension | +0.0304 | 0.0685 | ±0.1370 | +0.444 | 0.6568 |  |
| High cholesterol | +0.0446 | 0.0658 | ±0.1317 | +0.678 | 0.4978 |  |
| Kidney disease | -0.0434 | 0.0871 | ±0.1741 | -0.498 | 0.6183 |  |
| Circulatory disease | +0.0257 | 0.0829 | ±0.1657 | +0.310 | 0.7562 |  |
| CV (%) | +0.0038 | 0.0063 | ±0.0126 | +0.597 | 0.5507 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **783**, R² = **0.1871**, Adj R² = **0.1723**, F-statistic = **12.63** (p = **6.13e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.4**, BIC = **2135.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1478** | 0.3489 | ±0.6977 | **+9.023** | **1.83e-19** | *** |
| Education: graduate level (vs college) | -0.1212 | 0.0667 | ±0.1334 | -1.816 | 0.0694 | . |
| **Education: high school or below (vs college)** | **+0.4844** | 0.1168 | ±0.2336 | **+4.148** | **3.36e-05** | *** |
| Site: UCSD (vs UAB) | +0.0047 | 0.0776 | ±0.1551 | +0.061 | 0.9517 |  |
| **Site: UW (vs UAB)** | **-0.4433** | 0.0799 | ±0.1599 | **-5.545** | **2.94e-08** | *** |
| Season: spring (vs autumn) | -0.0978 | 0.0882 | ±0.1764 | -1.109 | 0.2676 |  |
| Season: summer (vs autumn) | +0.0935 | 0.0890 | ±0.1779 | +1.051 | 0.2935 |  |
| Season: winter (vs autumn) | +0.0553 | 0.0967 | ±0.1933 | +0.573 | 0.5670 |  |
| **Age (years)** | **-0.0216** | 0.0031 | ±0.0063 | **-6.879** | **6.03e-12** | *** |
| BMI (kg/m2) | +0.0098 | 0.0053 | ±0.0107 | +1.839 | 0.0659 | . |
| Hypertension | +0.0305 | 0.0685 | ±0.1369 | +0.445 | 0.6564 |  |
| High cholesterol | +0.0434 | 0.0656 | ±0.1312 | +0.662 | 0.5081 |  |
| Kidney disease | -0.0417 | 0.0874 | ±0.1748 | -0.478 | 0.6330 |  |
| Circulatory disease | +0.0248 | 0.0828 | ±0.1656 | +0.300 | 0.7642 |  |
| Mean / SD ratio | -0.0210 | 0.0346 | ±0.0692 | -0.607 | 0.5439 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **783**, R² = **0.1868**, Adj R² = **0.1720**, F-statistic = **12.60** (p = **6.97e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.7**, BIC = **2135.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1007** | 0.3402 | ±0.6803 | **+9.115** | **7.85e-20** | *** |
| Education: graduate level (vs college) | -0.1223 | 0.0667 | ±0.1335 | -1.832 | 0.0670 | . |
| **Education: high school or below (vs college)** | **+0.4845** | 0.1169 | ±0.2339 | **+4.143** | **3.43e-05** | *** |
| Site: UCSD (vs UAB) | +0.0041 | 0.0776 | ±0.1553 | +0.052 | 0.9583 |  |
| **Site: UW (vs UAB)** | **-0.4455** | 0.0800 | ±0.1600 | **-5.567** | **2.58e-08** | *** |
| Season: spring (vs autumn) | -0.0966 | 0.0884 | ±0.1768 | -1.093 | 0.2746 |  |
| Season: summer (vs autumn) | +0.0948 | 0.0889 | ±0.1778 | +1.066 | 0.2863 |  |
| Season: winter (vs autumn) | +0.0566 | 0.0966 | ±0.1933 | +0.585 | 0.5583 |  |
| **Age (years)** | **-0.0216** | 0.0031 | ±0.0063 | **-6.879** | **6.04e-12** | *** |
| BMI (kg/m2) | +0.0099 | 0.0053 | ±0.0107 | +1.850 | 0.0643 | . |
| Hypertension | +0.0315 | 0.0685 | ±0.1371 | +0.460 | 0.6455 |  |
| High cholesterol | +0.0430 | 0.0656 | ±0.1312 | +0.655 | 0.5123 |  |
| Kidney disease | -0.0374 | 0.0879 | ±0.1758 | -0.426 | 0.6704 |  |
| Circulatory disease | +0.0260 | 0.0828 | ±0.1656 | +0.314 | 0.7537 |  |
| Avg. daily mean/SD | -0.0096 | 0.0289 | ±0.0578 | -0.331 | 0.7410 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **783**, R² = **0.1883**, Adj R² = **0.1736**, F-statistic = **12.73** (p = **3.55e-27**), Residual SE = **0.896** on **768** df, AIC = **2064.2**, BIC = **2134.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8236** | 0.3403 | ±0.6806 | **+8.297** | **1.07e-16** | *** |
| Education: graduate level (vs college) | -0.1151 | 0.0671 | ±0.1342 | -1.715 | 0.0864 | . |
| **Education: high school or below (vs college)** | **+0.4808** | 0.1151 | ±0.2302 | **+4.178** | **2.94e-05** | *** |
| Site: UCSD (vs UAB) | +0.0123 | 0.0775 | ±0.1549 | +0.158 | 0.8743 |  |
| **Site: UW (vs UAB)** | **-0.4302** | 0.0804 | ±0.1608 | **-5.352** | **8.72e-08** | *** |
| Season: spring (vs autumn) | -0.0982 | 0.0885 | ±0.1770 | -1.109 | 0.2673 |  |
| Season: summer (vs autumn) | +0.1049 | 0.0888 | ±0.1777 | +1.181 | 0.2374 |  |
| Season: winter (vs autumn) | +0.0601 | 0.0962 | ±0.1923 | +0.625 | 0.5322 |  |
| **Age (years)** | **-0.0212** | 0.0031 | ±0.0063 | **-6.787** | **1.14e-11** | *** |
| BMI (kg/m2) | +0.0095 | 0.0054 | ±0.0108 | +1.770 | 0.0767 | . |
| Hypertension | +0.0353 | 0.0685 | ±0.1370 | +0.515 | 0.6062 |  |
| High cholesterol | +0.0485 | 0.0662 | ±0.1324 | +0.733 | 0.4634 |  |
| Kidney disease | -0.0419 | 0.0890 | ±0.1781 | -0.470 | 0.6381 |  |
| Circulatory disease | +0.0240 | 0.0829 | ±0.1658 | +0.289 | 0.7725 |  |
| MAG (mg/dL/h) | +0.0043 | 0.0034 | ±0.0068 | +1.271 | 0.2036 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **783**, R² = **0.1890**, Adj R² = **0.1742**, F-statistic = **12.78** (p = **2.66e-27**), Residual SE = **0.895** on **768** df, AIC = **2063.6**, BIC = **2133.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8440** | 0.3258 | ±0.6517 | **+8.728** | **2.59e-18** | *** |
| Education: graduate level (vs college) | -0.1175 | 0.0668 | ±0.1336 | -1.758 | 0.0787 | . |
| **Education: high school or below (vs college)** | **+0.4692** | 0.1161 | ±0.2322 | **+4.042** | **5.31e-05** | *** |
| Site: UCSD (vs UAB) | +0.0148 | 0.0776 | ±0.1552 | +0.190 | 0.8492 |  |
| **Site: UW (vs UAB)** | **-0.4326** | 0.0800 | ±0.1599 | **-5.410** | **6.32e-08** | *** |
| Season: spring (vs autumn) | -0.1033 | 0.0884 | ±0.1767 | -1.169 | 0.2425 |  |
| Season: summer (vs autumn) | +0.0978 | 0.0890 | ±0.1779 | +1.099 | 0.2718 |  |
| Season: winter (vs autumn) | +0.0558 | 0.0962 | ±0.1925 | +0.580 | 0.5619 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0063 | **-6.854** | **7.16e-12** | *** |
| BMI (kg/m2) | +0.0094 | 0.0054 | ±0.0107 | +1.746 | 0.0808 | . |
| Hypertension | +0.0306 | 0.0686 | ±0.1371 | +0.446 | 0.6555 |  |
| High cholesterol | +0.0450 | 0.0658 | ±0.1316 | +0.684 | 0.4939 |  |
| Kidney disease | -0.0592 | 0.0870 | ±0.1741 | -0.680 | 0.4964 |  |
| Circulatory disease | +0.0197 | 0.0833 | ±0.1665 | +0.237 | 0.8129 |  |
| Avg. daily range (mg/dL) | +0.0014 | 0.0009 | ±0.0018 | +1.537 | 0.1243 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **783**, R² = **0.1996**, Adj R² = **0.1851**, F-statistic = **13.68** (p = **2.30e-29**), Residual SE = **0.889** on **768** df, AIC = **2053.2**, BIC = **2123.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9082** | 0.2967 | ±0.5934 | **+9.801** | **1.11e-22** | *** |
| Education: graduate level (vs college) | -0.0971 | 0.0670 | ±0.1340 | -1.449 | 0.1473 |  |
| **Education: high school or below (vs college)** | **+0.4708** | 0.1136 | ±0.2272 | **+4.144** | **3.42e-05** | *** |
| Site: UCSD (vs UAB) | +0.0177 | 0.0768 | ±0.1536 | +0.230 | 0.8181 |  |
| **Site: UW (vs UAB)** | **-0.4199** | 0.0788 | ±0.1575 | **-5.333** | **9.68e-08** | *** |
| Season: spring (vs autumn) | -0.1056 | 0.0881 | ±0.1763 | -1.198 | 0.2310 |  |
| Season: summer (vs autumn) | +0.0964 | 0.0886 | ±0.1773 | +1.088 | 0.2766 |  |
| Season: winter (vs autumn) | +0.0423 | 0.0954 | ±0.1909 | +0.444 | 0.6574 |  |
| **Age (years)** | **-0.0211** | 0.0031 | ±0.0062 | **-6.789** | **1.13e-11** | *** |
| BMI (kg/m2) | +0.0073 | 0.0053 | ±0.0106 | +1.383 | 0.1668 |  |
| Hypertension | +0.0154 | 0.0685 | ±0.1371 | +0.225 | 0.8220 |  |
| High cholesterol | +0.0445 | 0.0653 | ±0.1306 | +0.682 | 0.4952 |  |
| Kidney disease | -0.0583 | 0.0852 | ±0.1703 | -0.685 | 0.4935 |  |
| Circulatory disease | +0.0018 | 0.0821 | ±0.1643 | +0.022 | 0.9825 |  |
| **SD of daily means (mg/dL)** | **+0.0143** | 0.0045 | ±0.0089 | **+3.219** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **783**, R² = **0.1942**, Adj R² = **0.1795**, F-statistic = **13.22** (p = **2.62e-28**), Residual SE = **0.892** on **768** df, AIC = **2058.5**, BIC = **2128.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.3612** | 0.3392 | ±0.6785 | **+9.908** | **3.83e-23** | *** |
| Education: graduate level (vs college) | -0.1146 | 0.0667 | ±0.1335 | -1.716 | 0.0861 | . |
| **Education: high school or below (vs college)** | **+0.4524** | 0.1133 | ±0.2265 | **+3.994** | **6.49e-05** | *** |
| Site: UCSD (vs UAB) | +0.0236 | 0.0774 | ±0.1547 | +0.305 | 0.7602 |  |
| **Site: UW (vs UAB)** | **-0.4277** | 0.0796 | ±0.1592 | **-5.374** | **7.68e-08** | *** |
| Season: spring (vs autumn) | -0.1044 | 0.0884 | ±0.1769 | -1.181 | 0.2376 |  |
| Season: summer (vs autumn) | +0.1040 | 0.0886 | ±0.1773 | +1.174 | 0.2406 |  |
| Season: winter (vs autumn) | +0.0516 | 0.0958 | ±0.1916 | +0.538 | 0.5902 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0062 | **-6.894** | **5.44e-12** | *** |
| BMI (kg/m2) | +0.0077 | 0.0055 | ±0.0110 | +1.396 | 0.1627 |  |
| Hypertension | +0.0281 | 0.0686 | ±0.1372 | +0.410 | 0.6818 |  |
| High cholesterol | +0.0428 | 0.0656 | ±0.1312 | +0.653 | 0.5135 |  |
| Kidney disease | -0.0529 | 0.0873 | ±0.1746 | -0.606 | 0.5443 |  |
| Circulatory disease | +0.0131 | 0.0825 | ±0.1651 | +0.159 | 0.8737 |  |
| **Time in range 70-180, pooled (%)** | **-0.0036** | 0.0015 | ±0.0030 | **-2.381** | **0.0173** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **783**, R² = **0.1942**, Adj R² = **0.1795**, F-statistic = **13.22** (p = **2.63e-28**), Residual SE = **0.892** on **768** df, AIC = **2058.5**, BIC = **2128.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.3633** | 0.3399 | ±0.6798 | **+9.895** | **4.39e-23** | *** |
| Education: graduate level (vs college) | -0.1154 | 0.0667 | ±0.1335 | -1.729 | 0.0837 | . |
| **Education: high school or below (vs college)** | **+0.4518** | 0.1132 | ±0.2265 | **+3.990** | **6.62e-05** | *** |
| Site: UCSD (vs UAB) | +0.0247 | 0.0773 | ±0.1547 | +0.319 | 0.7498 |  |
| **Site: UW (vs UAB)** | **-0.4274** | 0.0796 | ±0.1591 | **-5.371** | **7.84e-08** | *** |
| Season: spring (vs autumn) | -0.1052 | 0.0885 | ±0.1769 | -1.190 | 0.2342 |  |
| Season: summer (vs autumn) | +0.1030 | 0.0886 | ±0.1772 | +1.162 | 0.2451 |  |
| Season: winter (vs autumn) | +0.0505 | 0.0958 | ±0.1916 | +0.527 | 0.5983 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0062 | **-6.898** | **5.26e-12** | *** |
| BMI (kg/m2) | +0.0077 | 0.0055 | ±0.0110 | +1.388 | 0.1651 |  |
| Hypertension | +0.0284 | 0.0686 | ±0.1372 | +0.414 | 0.6789 |  |
| High cholesterol | +0.0427 | 0.0656 | ±0.1312 | +0.651 | 0.5152 |  |
| Kidney disease | -0.0541 | 0.0872 | ±0.1744 | -0.620 | 0.5352 |  |
| Circulatory disease | +0.0133 | 0.0826 | ±0.1651 | +0.161 | 0.8717 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0035** | 0.0015 | ±0.0030 | **-2.384** | **0.0171** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.1869**, Adj R² = **0.1721**, F-statistic = **12.61** (p = **6.60e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.5**, BIC = **2135.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0332** | 0.3007 | ±0.6015 | **+10.086** | **6.38e-24** | *** |
| Education: graduate level (vs college) | -0.1219 | 0.0666 | ±0.1332 | -1.830 | 0.0672 | . |
| **Education: high school or below (vs college)** | **+0.4871** | 0.1164 | ±0.2328 | **+4.184** | **2.86e-05** | *** |
| Site: UCSD (vs UAB) | +0.0056 | 0.0774 | ±0.1548 | +0.072 | 0.9427 |  |
| **Site: UW (vs UAB)** | **-0.4456** | 0.0793 | ±0.1586 | **-5.618** | **1.93e-08** | *** |
| Season: spring (vs autumn) | -0.0965 | 0.0883 | ±0.1767 | -1.092 | 0.2749 |  |
| Season: summer (vs autumn) | +0.0971 | 0.0893 | ±0.1786 | +1.087 | 0.2769 |  |
| Season: winter (vs autumn) | +0.0594 | 0.0969 | ±0.1937 | +0.613 | 0.5399 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0063 | **-6.880** | **5.98e-12** | *** |
| BMI (kg/m2) | +0.0098 | 0.0053 | ±0.0107 | +1.838 | 0.0660 | . |
| Hypertension | +0.0307 | 0.0689 | ±0.1377 | +0.446 | 0.6557 |  |
| High cholesterol | +0.0450 | 0.0664 | ±0.1328 | +0.677 | 0.4982 |  |
| Kidney disease | -0.0333 | 0.0876 | ±0.1752 | -0.380 | 0.7036 |  |
| Circulatory disease | +0.0244 | 0.0834 | ±0.1667 | +0.293 | 0.7698 |  |
| Any reading < 54 during wear (0/1) | +0.0383 | 0.0802 | ±0.1603 | +0.478 | 0.6330 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.1868**, Adj R² = **0.1720**, F-statistic = **12.60** (p = **6.92e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.6**, BIC = **2135.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0418** | 0.3042 | ±0.6084 | **+10.000** | **1.53e-23** | *** |
| Education: graduate level (vs college) | -0.1215 | 0.0666 | ±0.1332 | -1.824 | 0.0682 | . |
| **Education: high school or below (vs college)** | **+0.4869** | 0.1162 | ±0.2323 | **+4.192** | **2.77e-05** | *** |
| Site: UCSD (vs UAB) | +0.0058 | 0.0777 | ±0.1554 | +0.074 | 0.9408 |  |
| **Site: UW (vs UAB)** | **-0.4449** | 0.0797 | ±0.1594 | **-5.581** | **2.39e-08** | *** |
| Season: spring (vs autumn) | -0.0960 | 0.0883 | ±0.1765 | -1.088 | 0.2765 |  |
| Season: summer (vs autumn) | +0.0966 | 0.0891 | ±0.1781 | +1.084 | 0.2782 |  |
| Season: winter (vs autumn) | +0.0558 | 0.0967 | ±0.1935 | +0.577 | 0.5640 |  |
| **Age (years)** | **-0.0216** | 0.0031 | ±0.0063 | **-6.881** | **5.93e-12** | *** |
| BMI (kg/m2) | +0.0100 | 0.0054 | ±0.0108 | +1.844 | 0.0652 | . |
| Hypertension | +0.0326 | 0.0687 | ±0.1373 | +0.475 | 0.6350 |  |
| High cholesterol | +0.0442 | 0.0664 | ±0.1328 | +0.665 | 0.5059 |  |
| Kidney disease | -0.0322 | 0.0879 | ±0.1758 | -0.366 | 0.7143 |  |
| Circulatory disease | +0.0272 | 0.0826 | ±0.1653 | +0.329 | 0.7425 |  |
| Time < 54 (%) | +0.0218 | 0.1091 | ±0.2182 | +0.199 | 0.8419 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.1874**, Adj R² = **0.1726**, F-statistic = **12.65** (p = **5.45e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.1**, BIC = **2135.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0361** | 0.3036 | ±0.6073 | **+9.999** | **1.53e-23** | *** |
| Education: graduate level (vs college) | -0.1202 | 0.0665 | ±0.1331 | -1.806 | 0.0709 | . |
| **Education: high school or below (vs college)** | **+0.4893** | 0.1160 | ±0.2320 | **+4.218** | **2.47e-05** | *** |
| Site: UCSD (vs UAB) | +0.0083 | 0.0776 | ±0.1551 | +0.108 | 0.9143 |  |
| **Site: UW (vs UAB)** | **-0.4411** | 0.0795 | ±0.1590 | **-5.547** | **2.90e-08** | *** |
| Season: spring (vs autumn) | -0.0932 | 0.0883 | ±0.1767 | -1.055 | 0.2912 |  |
| Season: summer (vs autumn) | +0.0997 | 0.0891 | ±0.1781 | +1.119 | 0.2631 |  |
| Season: winter (vs autumn) | +0.0559 | 0.0967 | ±0.1934 | +0.578 | 0.5633 |  |
| **Age (years)** | **-0.0217** | 0.0031 | ±0.0063 | **-6.895** | **5.38e-12** | *** |
| BMI (kg/m2) | +0.0100 | 0.0054 | ±0.0108 | +1.856 | 0.0635 | . |
| Hypertension | +0.0321 | 0.0687 | ±0.1373 | +0.468 | 0.6397 |  |
| High cholesterol | +0.0472 | 0.0666 | ±0.1332 | +0.709 | 0.4783 |  |
| Kidney disease | -0.0331 | 0.0877 | ±0.1754 | -0.377 | 0.7060 |  |
| Circulatory disease | +0.0280 | 0.0825 | ±0.1651 | +0.340 | 0.7341 |  |
| Avg. daily time < 54 (%) | +0.0531 | 0.0930 | ±0.1860 | +0.571 | 0.5682 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.1869**, Adj R² = **0.1721**, F-statistic = **12.61** (p = **6.72e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.6**, BIC = **2135.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0408** | 0.3027 | ±0.6054 | **+10.046** | **9.60e-24** | *** |
| Education: graduate level (vs college) | -0.1210 | 0.0665 | ±0.1330 | -1.820 | 0.0687 | . |
| **Education: high school or below (vs college)** | **+0.4869** | 0.1163 | ±0.2327 | **+4.185** | **2.85e-05** | *** |
| Site: UCSD (vs UAB) | +0.0069 | 0.0774 | ±0.1548 | +0.089 | 0.9293 |  |
| **Site: UW (vs UAB)** | **-0.4440** | 0.0792 | ±0.1583 | **-5.608** | **2.05e-08** | *** |
| Season: spring (vs autumn) | -0.0947 | 0.0889 | ±0.1778 | -1.065 | 0.2867 |  |
| Season: summer (vs autumn) | +0.0982 | 0.0895 | ±0.1790 | +1.097 | 0.2726 |  |
| Season: winter (vs autumn) | +0.0577 | 0.0973 | ±0.1946 | +0.593 | 0.5530 |  |
| **Age (years)** | **-0.0216** | 0.0032 | ±0.0063 | **-6.849** | **7.46e-12** | *** |
| BMI (kg/m2) | +0.0099 | 0.0053 | ±0.0107 | +1.843 | 0.0654 | . |
| Hypertension | +0.0315 | 0.0691 | ±0.1382 | +0.456 | 0.6480 |  |
| High cholesterol | +0.0457 | 0.0670 | ±0.1339 | +0.682 | 0.4952 |  |
| Kidney disease | -0.0338 | 0.0875 | ±0.1751 | -0.386 | 0.6995 |  |
| Circulatory disease | +0.0280 | 0.0826 | ±0.1651 | +0.339 | 0.7344 |  |
| Time 54-69, pooled (%) | +0.0143 | 0.0526 | ±0.1051 | +0.273 | 0.7849 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **783**, R² = **0.1871**, Adj R² = **0.1723**, F-statistic = **12.63** (p = **6.14e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.4**, BIC = **2135.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0403** | 0.3024 | ±0.6049 | **+10.052** | **8.97e-24** | *** |
| Education: graduate level (vs college) | -0.1200 | 0.0665 | ±0.1330 | -1.804 | 0.0713 | . |
| **Education: high school or below (vs college)** | **+0.4878** | 0.1163 | ±0.2327 | **+4.193** | **2.75e-05** | *** |
| Site: UCSD (vs UAB) | +0.0082 | 0.0774 | ±0.1548 | +0.106 | 0.9156 |  |
| **Site: UW (vs UAB)** | **-0.4419** | 0.0792 | ±0.1585 | **-5.577** | **2.45e-08** | *** |
| Season: spring (vs autumn) | -0.0940 | 0.0889 | ±0.1777 | -1.058 | 0.2900 |  |
| Season: summer (vs autumn) | +0.0991 | 0.0894 | ±0.1788 | +1.109 | 0.2675 |  |
| Season: winter (vs autumn) | +0.0576 | 0.0972 | ±0.1944 | +0.592 | 0.5538 |  |
| **Age (years)** | **-0.0217** | 0.0032 | ±0.0063 | **-6.850** | **7.37e-12** | *** |
| BMI (kg/m2) | +0.0098 | 0.0053 | ±0.0107 | +1.841 | 0.0657 | . |
| Hypertension | +0.0311 | 0.0692 | ±0.1384 | +0.449 | 0.6536 |  |
| High cholesterol | +0.0473 | 0.0672 | ±0.1344 | +0.704 | 0.4814 |  |
| Kidney disease | -0.0341 | 0.0874 | ±0.1749 | -0.390 | 0.6964 |  |
| Circulatory disease | +0.0290 | 0.0826 | ±0.1651 | +0.351 | 0.7256 |  |
| Avg. daily time 54-69 (%) | +0.0190 | 0.0526 | ±0.1051 | +0.362 | 0.7171 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **783**, R² = **0.1869**, Adj R² = **0.1721**, F-statistic = **12.61** (p = **6.59e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.5**, BIC = **2135.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0388** | 0.3034 | ±0.6068 | **+10.015** | **1.31e-23** | *** |
| Education: graduate level (vs college) | -0.1205 | 0.0665 | ±0.1331 | -1.812 | 0.0700 | . |
| **Education: high school or below (vs college)** | **+0.4876** | 0.1162 | ±0.2324 | **+4.195** | **2.73e-05** | *** |
| Site: UCSD (vs UAB) | +0.0074 | 0.0775 | ±0.1550 | +0.096 | 0.9235 |  |
| **Site: UW (vs UAB)** | **-0.4431** | 0.0793 | ±0.1585 | **-5.591** | **2.26e-08** | *** |
| Season: spring (vs autumn) | -0.0947 | 0.0887 | ±0.1773 | -1.068 | 0.2856 |  |
| Season: summer (vs autumn) | +0.0983 | 0.0893 | ±0.1786 | +1.101 | 0.2709 |  |
| Season: winter (vs autumn) | +0.0571 | 0.0969 | ±0.1938 | +0.589 | 0.5558 |  |
| **Age (years)** | **-0.0216** | 0.0032 | ±0.0063 | **-6.857** | **7.06e-12** | *** |
| BMI (kg/m2) | +0.0099 | 0.0054 | ±0.0107 | +1.847 | 0.0647 | . |
| Hypertension | +0.0317 | 0.0688 | ±0.1377 | +0.460 | 0.6452 |  |
| High cholesterol | +0.0462 | 0.0671 | ±0.1341 | +0.689 | 0.4911 |  |
| Kidney disease | -0.0334 | 0.0876 | ±0.1752 | -0.382 | 0.7028 |  |
| Circulatory disease | +0.0282 | 0.0825 | ±0.1650 | +0.342 | 0.7325 |  |
| Time < 70 (%) | +0.0117 | 0.0341 | ±0.0681 | +0.344 | 0.7309 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **783**, R² = **0.1873**, Adj R² = **0.1725**, F-statistic = **12.64** (p = **5.65e-27**), Residual SE = **0.896** on **768** df, AIC = **2065.2**, BIC = **2135.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0371** | 0.3028 | ±0.6056 | **+10.030** | **1.13e-23** | *** |
| Education: graduate level (vs college) | -0.1193 | 0.0665 | ±0.1330 | -1.794 | 0.0728 | . |
| **Education: high school or below (vs college)** | **+0.4890** | 0.1162 | ±0.2324 | **+4.208** | **2.58e-05** | *** |
| Site: UCSD (vs UAB) | +0.0093 | 0.0775 | ±0.1549 | +0.121 | 0.9041 |  |
| **Site: UW (vs UAB)** | **-0.4403** | 0.0793 | ±0.1585 | **-5.554** | **2.79e-08** | *** |
| Season: spring (vs autumn) | -0.0931 | 0.0888 | ±0.1775 | -1.049 | 0.2942 |  |
| Season: summer (vs autumn) | +0.1002 | 0.0893 | ±0.1786 | +1.122 | 0.2620 |  |
| Season: winter (vs autumn) | +0.0572 | 0.0970 | ±0.1940 | +0.590 | 0.5551 |  |
| **Age (years)** | **-0.0217** | 0.0032 | ±0.0063 | **-6.867** | **6.55e-12** | *** |
| BMI (kg/m2) | +0.0099 | 0.0053 | ±0.0107 | +1.847 | 0.0647 | . |
| Hypertension | +0.0310 | 0.0690 | ±0.1380 | +0.450 | 0.6529 |  |
| High cholesterol | +0.0485 | 0.0673 | ±0.1346 | +0.721 | 0.4706 |  |
| Kidney disease | -0.0342 | 0.0874 | ±0.1748 | -0.391 | 0.6957 |  |
| Circulatory disease | +0.0293 | 0.0825 | ±0.1650 | +0.356 | 0.7221 |  |
| Avg. daily time < 70 (%) | +0.0173 | 0.0359 | ±0.0717 | +0.482 | 0.6295 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.1916**, Adj R² = **0.1769**, F-statistic = **13.00** (p = **8.33e-28**), Residual SE = **0.894** on **768** df, AIC = **2061.0**, BIC = **2131.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4286** | 0.3772 | ±0.7543 | **+9.091** | **9.84e-20** | *** |
| Education: graduate level (vs college) | -0.1115 | 0.0674 | ±0.1347 | -1.655 | 0.0980 | . |
| **Education: high school or below (vs college)** | **+0.4613** | 0.1132 | ±0.2264 | **+4.076** | **4.59e-05** | *** |
| Site: UCSD (vs UAB) | +0.0177 | 0.0775 | ±0.1550 | +0.228 | 0.8198 |  |
| **Site: UW (vs UAB)** | **-0.4297** | 0.0796 | ±0.1592 | **-5.399** | **6.69e-08** | *** |
| Season: spring (vs autumn) | -0.0980 | 0.0886 | ±0.1771 | -1.106 | 0.2687 |  |
| Season: summer (vs autumn) | +0.1102 | 0.0891 | ±0.1783 | +1.236 | 0.2165 |  |
| Season: winter (vs autumn) | +0.0566 | 0.0961 | ±0.1923 | +0.589 | 0.5559 |  |
| **Age (years)** | **-0.0211** | 0.0031 | ±0.0063 | **-6.715** | **1.88e-11** | *** |
| BMI (kg/m2) | +0.0090 | 0.0054 | ±0.0109 | +1.659 | 0.0970 | . |
| Hypertension | +0.0263 | 0.0685 | ±0.1370 | +0.384 | 0.7006 |  |
| High cholesterol | +0.0451 | 0.0659 | ±0.1317 | +0.685 | 0.4934 |  |
| Kidney disease | -0.0428 | 0.0881 | ±0.1763 | -0.486 | 0.6268 |  |
| Circulatory disease | +0.0153 | 0.0836 | ±0.1671 | +0.183 | 0.8545 |  |
| Time 54-250, pooled (%) | -0.0043 | 0.0025 | ±0.0050 | -1.724 | 0.0847 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.1917**, Adj R² = **0.1770**, F-statistic = **13.01** (p = **7.98e-28**), Residual SE = **0.894** on **768** df, AIC = **2060.9**, BIC = **2130.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4425** | 0.3797 | ±0.7595 | **+9.066** | **1.24e-19** | *** |
| Education: graduate level (vs college) | -0.1116 | 0.0673 | ±0.1346 | -1.657 | 0.0975 | . |
| **Education: high school or below (vs college)** | **+0.4610** | 0.1132 | ±0.2264 | **+4.073** | **4.64e-05** | *** |
| Site: UCSD (vs UAB) | +0.0180 | 0.0774 | ±0.1549 | +0.233 | 0.8160 |  |
| **Site: UW (vs UAB)** | **-0.4301** | 0.0795 | ±0.1591 | **-5.408** | **6.37e-08** | *** |
| Season: spring (vs autumn) | -0.0984 | 0.0886 | ±0.1771 | -1.112 | 0.2663 |  |
| Season: summer (vs autumn) | +0.1095 | 0.0891 | ±0.1781 | +1.229 | 0.2189 |  |
| Season: winter (vs autumn) | +0.0563 | 0.0961 | ±0.1923 | +0.585 | 0.5583 |  |
| **Age (years)** | **-0.0211** | 0.0031 | ±0.0063 | **-6.735** | **1.64e-11** | *** |
| BMI (kg/m2) | +0.0090 | 0.0054 | ±0.0109 | +1.652 | 0.0986 | . |
| Hypertension | +0.0267 | 0.0685 | ±0.1370 | +0.390 | 0.6969 |  |
| High cholesterol | +0.0452 | 0.0658 | ±0.1317 | +0.686 | 0.4925 |  |
| Kidney disease | -0.0440 | 0.0881 | ±0.1761 | -0.500 | 0.6171 |  |
| Circulatory disease | +0.0146 | 0.0837 | ±0.1673 | +0.175 | 0.8613 |  |
| Avg. daily time 54-250 (%) | -0.0044 | 0.0025 | ±0.0050 | -1.749 | 0.0803 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.1910**, Adj R² = **0.1762**, F-statistic = **12.95** (p = **1.10e-27**), Residual SE = **0.894** on **768** df, AIC = **2061.6**, BIC = **2131.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0478** | 0.3001 | ±0.6002 | **+10.156** | **3.11e-24** | *** |
| Education: graduate level (vs college) | -0.1251 | 0.0666 | ±0.1333 | -1.877 | 0.0605 | . |
| **Education: high school or below (vs college)** | **+0.4679** | 0.1161 | ±0.2321 | **+4.031** | **5.55e-05** | *** |
| Site: UCSD (vs UAB) | +0.0132 | 0.0775 | ±0.1550 | +0.170 | 0.8650 |  |
| **Site: UW (vs UAB)** | **-0.4424** | 0.0797 | ±0.1594 | **-5.552** | **2.82e-08** | *** |
| Season: spring (vs autumn) | -0.1060 | 0.0882 | ±0.1764 | -1.202 | 0.2294 |  |
| Season: summer (vs autumn) | +0.0901 | 0.0889 | ±0.1778 | +1.013 | 0.3112 |  |
| Season: winter (vs autumn) | +0.0499 | 0.0965 | ±0.1929 | +0.518 | 0.6048 |  |
| **Age (years)** | **-0.0220** | 0.0032 | ±0.0063 | **-6.975** | **3.06e-12** | *** |
| BMI (kg/m2) | +0.0080 | 0.0055 | ±0.0111 | +1.446 | 0.1481 |  |
| Hypertension | +0.0339 | 0.0686 | ±0.1371 | +0.495 | 0.6208 |  |
| High cholesterol | +0.0387 | 0.0656 | ±0.1311 | +0.590 | 0.5552 |  |
| Kidney disease | -0.0471 | 0.0871 | ±0.1741 | -0.540 | 0.5889 |  |
| Circulatory disease | +0.0204 | 0.0819 | ±0.1638 | +0.249 | 0.8030 |  |
| Time 181-250, pooled (%) | +0.0045 | 0.0023 | ±0.0047 | +1.940 | 0.0523 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **783**, R² = **0.1909**, Adj R² = **0.1761**, F-statistic = **12.94** (p = **1.15e-27**), Residual SE = **0.894** on **768** df, AIC = **2061.7**, BIC = **2131.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0468** | 0.3001 | ±0.6002 | **+10.152** | **3.23e-24** | *** |
| Education: graduate level (vs college) | -0.1257 | 0.0667 | ±0.1333 | -1.886 | 0.0593 | . |
| **Education: high school or below (vs college)** | **+0.4670** | 0.1160 | ±0.2320 | **+4.026** | **5.67e-05** | *** |
| Site: UCSD (vs UAB) | +0.0143 | 0.0775 | ±0.1550 | +0.184 | 0.8541 |  |
| **Site: UW (vs UAB)** | **-0.4414** | 0.0797 | ±0.1595 | **-5.536** | **3.09e-08** | *** |
| Season: spring (vs autumn) | -0.1063 | 0.0883 | ±0.1765 | -1.205 | 0.2283 |  |
| Season: summer (vs autumn) | +0.0899 | 0.0890 | ±0.1779 | +1.011 | 0.3120 |  |
| Season: winter (vs autumn) | +0.0492 | 0.0965 | ±0.1929 | +0.510 | 0.6102 |  |
| **Age (years)** | **-0.0219** | 0.0031 | ±0.0063 | **-6.965** | **3.29e-12** | *** |
| BMI (kg/m2) | +0.0080 | 0.0055 | ±0.0111 | +1.447 | 0.1479 |  |
| Hypertension | +0.0337 | 0.0686 | ±0.1372 | +0.492 | 0.6228 |  |
| High cholesterol | +0.0384 | 0.0656 | ±0.1312 | +0.586 | 0.5577 |  |
| Kidney disease | -0.0473 | 0.0871 | ±0.1741 | -0.543 | 0.5869 |  |
| Circulatory disease | +0.0211 | 0.0819 | ±0.1639 | +0.258 | 0.7965 |  |
| Avg. daily time 181-250 (%) | +0.0044 | 0.0023 | ±0.0045 | +1.935 | 0.0530 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **783**, R² = **0.1939**, Adj R² = **0.1792**, F-statistic = **13.20** (p = **2.98e-28**), Residual SE = **0.892** on **768** df, AIC = **2058.8**, BIC = **2128.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0092** | 0.3001 | ±0.6001 | **+10.029** | **1.14e-23** | *** |
| Education: graduate level (vs college) | -0.1155 | 0.0667 | ±0.1335 | -1.731 | 0.0834 | . |
| **Education: high school or below (vs college)** | **+0.4525** | 0.1133 | ±0.2265 | **+3.996** | **6.45e-05** | *** |
| Site: UCSD (vs UAB) | +0.0219 | 0.0774 | ±0.1548 | +0.283 | 0.7770 |  |
| **Site: UW (vs UAB)** | **-0.4296** | 0.0796 | ±0.1592 | **-5.398** | **6.76e-08** | *** |
| Season: spring (vs autumn) | -0.1049 | 0.0885 | ±0.1769 | -1.186 | 0.2358 |  |
| Season: summer (vs autumn) | +0.1030 | 0.0887 | ±0.1773 | +1.161 | 0.2455 |  |
| Season: winter (vs autumn) | +0.0516 | 0.0958 | ±0.1917 | +0.539 | 0.5902 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0062 | **-6.888** | **5.66e-12** | *** |
| BMI (kg/m2) | +0.0077 | 0.0055 | ±0.0110 | +1.402 | 0.1610 |  |
| Hypertension | +0.0285 | 0.0686 | ±0.1372 | +0.416 | 0.6774 |  |
| High cholesterol | +0.0416 | 0.0656 | ±0.1311 | +0.635 | 0.5257 |  |
| Kidney disease | -0.0521 | 0.0875 | ±0.1750 | -0.595 | 0.5516 |  |
| Circulatory disease | +0.0129 | 0.0825 | ±0.1651 | +0.156 | 0.8760 |  |
| **Time > 180 (%)** | **+0.0035** | 0.0015 | ±0.0030 | **+2.331** | **0.0198** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **783**, R² = **0.1939**, Adj R² = **0.1792**, F-statistic = **13.19** (p = **3.08e-28**), Residual SE = **0.893** on **768** df, AIC = **2058.9**, BIC = **2128.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0133** | 0.3002 | ±0.6003 | **+10.039** | **1.02e-23** | *** |
| Education: graduate level (vs college) | -0.1164 | 0.0667 | ±0.1334 | -1.744 | 0.0811 | . |
| **Education: high school or below (vs college)** | **+0.4520** | 0.1132 | ±0.2264 | **+3.992** | **6.55e-05** | *** |
| Site: UCSD (vs UAB) | +0.0229 | 0.0774 | ±0.1547 | +0.296 | 0.7676 |  |
| **Site: UW (vs UAB)** | **-0.4295** | 0.0796 | ±0.1592 | **-5.396** | **6.81e-08** | *** |
| Season: spring (vs autumn) | -0.1057 | 0.0885 | ±0.1770 | -1.194 | 0.2323 |  |
| Season: summer (vs autumn) | +0.1018 | 0.0886 | ±0.1773 | +1.149 | 0.2506 |  |
| Season: winter (vs autumn) | +0.0506 | 0.0958 | ±0.1917 | +0.528 | 0.5978 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0062 | **-6.892** | **5.49e-12** | *** |
| BMI (kg/m2) | +0.0077 | 0.0055 | ±0.0110 | +1.398 | 0.1622 |  |
| Hypertension | +0.0289 | 0.0686 | ±0.1372 | +0.421 | 0.6739 |  |
| High cholesterol | +0.0414 | 0.0656 | ±0.1311 | +0.631 | 0.5280 |  |
| Kidney disease | -0.0531 | 0.0874 | ±0.1748 | -0.607 | 0.5438 |  |
| Circulatory disease | +0.0131 | 0.0826 | ±0.1651 | +0.159 | 0.8739 |  |
| **Avg. daily time > 180 (%)** | **+0.0034** | 0.0015 | ±0.0030 | **+2.321** | **0.0203** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **783**, R² = **0.1944**, Adj R² = **0.1798**, F-statistic = **13.24** (p = **2.37e-28**), Residual SE = **0.892** on **768** df, AIC = **2058.3**, BIC = **2128.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0250** | 0.2999 | ±0.5997 | **+10.088** | **6.23e-24** | *** |
| Education: graduate level (vs college) | -0.1085 | 0.0670 | ±0.1340 | -1.619 | 0.1055 |  |
| **Education: high school or below (vs college)** | **+0.4574** | 0.1133 | ±0.2266 | **+4.038** | **5.39e-05** | *** |
| Site: UCSD (vs UAB) | +0.0235 | 0.0772 | ±0.1544 | +0.305 | 0.7607 |  |
| **Site: UW (vs UAB)** | **-0.4337** | 0.0793 | ±0.1587 | **-5.468** | **4.56e-08** | *** |
| Season: spring (vs autumn) | -0.1082 | 0.0884 | ±0.1769 | -1.223 | 0.2212 |  |
| Season: summer (vs autumn) | +0.1048 | 0.0883 | ±0.1766 | +1.187 | 0.2353 |  |
| Season: winter (vs autumn) | +0.0489 | 0.0959 | ±0.1918 | +0.510 | 0.6103 |  |
| **Age (years)** | **-0.0211** | 0.0031 | ±0.0062 | **-6.792** | **1.11e-11** | *** |
| BMI (kg/m2) | +0.0072 | 0.0056 | ±0.0111 | +1.292 | 0.1964 |  |
| Hypertension | +0.0310 | 0.0685 | ±0.1371 | +0.452 | 0.6513 |  |
| High cholesterol | +0.0434 | 0.0655 | ±0.1311 | +0.663 | 0.5075 |  |
| Kidney disease | -0.0454 | 0.0871 | ±0.1742 | -0.522 | 0.6019 |  |
| Circulatory disease | +0.0139 | 0.0826 | ±0.1651 | +0.168 | 0.8666 |  |
| **Nocturnal time > 180 (%)** | **+0.0033** | 0.0014 | ±0.0027 | **+2.416** | **0.0157** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.1916**, Adj R² = **0.1768**, F-statistic = **13.00** (p = **8.58e-28**), Residual SE = **0.894** on **768** df, AIC = **2061.1**, BIC = **2131.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0005** | 0.3047 | ±0.6095 | **+9.846** | **7.13e-23** | *** |
| Education: graduate level (vs college) | -0.1118 | 0.0673 | ±0.1347 | -1.661 | 0.0967 | . |
| **Education: high school or below (vs college)** | **+0.4611** | 0.1132 | ±0.2263 | **+4.075** | **4.60e-05** | *** |
| Site: UCSD (vs UAB) | +0.0171 | 0.0775 | ±0.1550 | +0.221 | 0.8251 |  |
| **Site: UW (vs UAB)** | **-0.4304** | 0.0796 | ±0.1591 | **-5.409** | **6.36e-08** | *** |
| Season: spring (vs autumn) | -0.0981 | 0.0886 | ±0.1771 | -1.108 | 0.2679 |  |
| Season: summer (vs autumn) | +0.1098 | 0.0891 | ±0.1783 | +1.232 | 0.2179 |  |
| Season: winter (vs autumn) | +0.0568 | 0.0962 | ±0.1923 | +0.591 | 0.5547 |  |
| **Age (years)** | **-0.0211** | 0.0031 | ±0.0063 | **-6.712** | **1.92e-11** | *** |
| BMI (kg/m2) | +0.0090 | 0.0054 | ±0.0109 | +1.655 | 0.0978 | . |
| Hypertension | +0.0264 | 0.0685 | ±0.1370 | +0.385 | 0.7000 |  |
| High cholesterol | +0.0447 | 0.0658 | ±0.1316 | +0.678 | 0.4975 |  |
| Kidney disease | -0.0428 | 0.0882 | ±0.1763 | -0.486 | 0.6272 |  |
| Circulatory disease | +0.0152 | 0.0836 | ±0.1671 | +0.182 | 0.8556 |  |
| Time > 250 (%) | +0.0043 | 0.0025 | ±0.0050 | +1.710 | 0.0872 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 783)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **783**, R² = **0.1916**, Adj R² = **0.1769**, F-statistic = **13.00** (p = **8.41e-28**), Residual SE = **0.894** on **768** df, AIC = **2061.0**, BIC = **2131.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0054** | 0.3046 | ±0.6093 | **+9.866** | **5.87e-23** | *** |
| Education: graduate level (vs college) | -0.1119 | 0.0673 | ±0.1346 | -1.663 | 0.0963 | . |
| **Education: high school or below (vs college)** | **+0.4610** | 0.1132 | ±0.2263 | **+4.074** | **4.62e-05** | *** |
| Site: UCSD (vs UAB) | +0.0174 | 0.0774 | ±0.1549 | +0.225 | 0.8217 |  |
| **Site: UW (vs UAB)** | **-0.4308** | 0.0795 | ±0.1590 | **-5.418** | **6.04e-08** | *** |
| Season: spring (vs autumn) | -0.0987 | 0.0886 | ±0.1771 | -1.115 | 0.2650 |  |
| Season: summer (vs autumn) | +0.1090 | 0.0891 | ±0.1781 | +1.224 | 0.2211 |  |
| Season: winter (vs autumn) | +0.0563 | 0.0961 | ±0.1923 | +0.586 | 0.5579 |  |
| **Age (years)** | **-0.0211** | 0.0031 | ±0.0063 | **-6.733** | **1.66e-11** | *** |
| BMI (kg/m2) | +0.0090 | 0.0054 | ±0.0109 | +1.650 | 0.0988 | . |
| Hypertension | +0.0268 | 0.0685 | ±0.1370 | +0.391 | 0.6956 |  |
| High cholesterol | +0.0447 | 0.0658 | ±0.1316 | +0.680 | 0.4967 |  |
| Kidney disease | -0.0438 | 0.0881 | ±0.1762 | -0.498 | 0.6188 |  |
| Circulatory disease | +0.0146 | 0.0837 | ±0.1673 | +0.175 | 0.8614 |  |
| Avg. daily time > 250 (%) | +0.0043 | 0.0025 | ±0.0050 | +1.726 | 0.0843 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 783; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **783**, R² = **0.3085**, Adj R² = **0.2968**, F-statistic = **26.39** (p = **2.38e-53**), Residual SE = **1.998** on **769** df, AIC = **3319.9**, BIC = **3385.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9596** | 0.6104 | ±1.2207 | **+37.617** | **1.14e-309** | *** |
| Education: graduate level (vs college) | -0.2588 | 0.1549 | ±0.3098 | -1.670 | 0.0948 | . |
| Education: high school or below (vs college) | +0.0893 | 0.2281 | ±0.4562 | +0.391 | 0.6955 |  |
| Site: UCSD (vs UAB) | +0.0038 | 0.1830 | ±0.3660 | +0.021 | 0.9836 |  |
| **Site: UW (vs UAB)** | **-1.2751** | 0.1744 | ±0.3488 | **-7.310** | **2.66e-13** | *** |
| Season: spring (vs autumn) | -0.2241 | 0.1949 | ±0.3897 | -1.150 | 0.2502 |  |
| **Season: summer (vs autumn)** | **+2.0187** | 0.2218 | ±0.4435 | **+9.103** | **8.79e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9676** | 0.1964 | ±0.3929 | **-4.926** | **8.41e-07** | *** |
| **Age (years)** | **+0.0205** | 0.0075 | ±0.0149 | **+2.752** | **0.0059** | ** |
| BMI (kg/m2) | +0.0193 | 0.0109 | ±0.0219 | +1.762 | 0.0781 | . |
| Hypertension | +0.1308 | 0.1553 | ±0.3106 | +0.842 | 0.3998 |  |
| High cholesterol | +0.0930 | 0.1541 | ±0.3081 | +0.604 | 0.5461 |  |
| Kidney disease | +0.1344 | 0.1965 | ±0.3930 | +0.684 | 0.4940 |  |
| Circulatory disease | +0.1289 | 0.1995 | ±0.3990 | +0.646 | 0.5181 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **783**, R² = **0.3091**, Adj R² = **0.2965**, F-statistic = **24.55** (p = **8.99e-53**), Residual SE = **1.998** on **768** df, AIC = **3321.2**, BIC = **3391.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.6830** | 0.7513 | ±1.5025 | **+30.193** | **2.92e-200** | *** |
| Education: graduate level (vs college) | -0.2498 | 0.1570 | ±0.3139 | -1.591 | 0.1115 |  |
| Education: high school or below (vs college) | +0.0639 | 0.2310 | ±0.4619 | +0.277 | 0.7821 |  |
| Site: UCSD (vs UAB) | +0.0125 | 0.1850 | ±0.3701 | +0.068 | 0.9460 |  |
| **Site: UW (vs UAB)** | **-1.2630** | 0.1755 | ±0.3510 | **-7.197** | **6.15e-13** | *** |
| Season: spring (vs autumn) | -0.2193 | 0.1966 | ±0.3932 | -1.115 | 0.2647 |  |
| **Season: summer (vs autumn)** | **+2.0251** | 0.2225 | ±0.4449 | **+9.103** | **8.77e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9670** | 0.1962 | ±0.3923 | **-4.930** | **8.24e-07** | *** |
| **Age (years)** | **+0.0206** | 0.0075 | ±0.0149 | **+2.768** | **0.0056** | ** |
| BMI (kg/m2) | +0.0178 | 0.0113 | ±0.0226 | +1.578 | 0.1145 |  |
| Hypertension | +0.1244 | 0.1550 | ±0.3100 | +0.803 | 0.4221 |  |
| High cholesterol | +0.0878 | 0.1556 | ±0.3112 | +0.564 | 0.5725 |  |
| Kidney disease | +0.1326 | 0.1983 | ±0.3966 | +0.669 | 0.5036 |  |
| Circulatory disease | +0.1191 | 0.2024 | ±0.4048 | +0.588 | 0.5564 |  |
| HbA1c (%) | +0.0461 | 0.0767 | ±0.1533 | +0.601 | 0.5477 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **783**, R² = **0.3089**, Adj R² = **0.2963**, F-statistic = **24.52** (p = **1.02e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.4**, BIC = **3391.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.7859** | 0.6645 | ±1.3291 | **+34.288** | **1.18e-257** | *** |
| Education: graduate level (vs college) | -0.2543 | 0.1552 | ±0.3104 | -1.639 | 0.1013 |  |
| Education: high school or below (vs college) | +0.0709 | 0.2316 | ±0.4632 | +0.306 | 0.7596 |  |
| Site: UCSD (vs UAB) | +0.0130 | 0.1842 | ±0.3685 | +0.070 | 0.9439 |  |
| **Site: UW (vs UAB)** | **-1.2660** | 0.1764 | ±0.3528 | **-7.176** | **7.17e-13** | *** |
| Season: spring (vs autumn) | -0.2283 | 0.1956 | ±0.3912 | -1.167 | 0.2432 |  |
| **Season: summer (vs autumn)** | **+2.0249** | 0.2223 | ±0.4446 | **+9.108** | **8.36e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9687** | 0.1966 | ±0.3931 | **-4.928** | **8.31e-07** | *** |
| **Age (years)** | **+0.0207** | 0.0075 | ±0.0149 | **+2.771** | **0.0056** | ** |
| BMI (kg/m2) | +0.0183 | 0.0111 | ±0.0222 | +1.645 | 0.0999 | . |
| Hypertension | +0.1272 | 0.1548 | ±0.3096 | +0.822 | 0.4112 |  |
| High cholesterol | +0.0912 | 0.1542 | ±0.3083 | +0.592 | 0.5540 |  |
| Kidney disease | +0.1269 | 0.1969 | ±0.3938 | +0.644 | 0.5193 |  |
| Circulatory disease | +0.1205 | 0.2011 | ±0.4021 | +0.599 | 0.5489 |  |
| Mean glucose (mg/dL) | +0.0012 | 0.0020 | ±0.0040 | +0.609 | 0.5423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **783**, R² = **0.3089**, Adj R² = **0.2963**, F-statistic = **24.52** (p = **1.02e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.4**, BIC = **3391.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.6178** | 0.8139 | ±1.6278 | **+27.790** | **5.70e-170** | *** |
| Education: graduate level (vs college) | -0.2543 | 0.1552 | ±0.3104 | -1.639 | 0.1013 |  |
| Education: high school or below (vs college) | +0.0709 | 0.2316 | ±0.4632 | +0.306 | 0.7596 |  |
| Site: UCSD (vs UAB) | +0.0130 | 0.1842 | ±0.3685 | +0.070 | 0.9439 |  |
| **Site: UW (vs UAB)** | **-1.2660** | 0.1764 | ±0.3528 | **-7.176** | **7.17e-13** | *** |
| Season: spring (vs autumn) | -0.2283 | 0.1956 | ±0.3912 | -1.167 | 0.2432 |  |
| **Season: summer (vs autumn)** | **+2.0249** | 0.2223 | ±0.4446 | **+9.108** | **8.36e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9687** | 0.1966 | ±0.3931 | **-4.928** | **8.31e-07** | *** |
| **Age (years)** | **+0.0207** | 0.0075 | ±0.0149 | **+2.771** | **0.0056** | ** |
| BMI (kg/m2) | +0.0183 | 0.0111 | ±0.0222 | +1.645 | 0.0999 | . |
| Hypertension | +0.1272 | 0.1548 | ±0.3096 | +0.822 | 0.4112 |  |
| High cholesterol | +0.0912 | 0.1542 | ±0.3083 | +0.592 | 0.5540 |  |
| Kidney disease | +0.1269 | 0.1969 | ±0.3938 | +0.644 | 0.5193 |  |
| Circulatory disease | +0.1205 | 0.2011 | ±0.4021 | +0.599 | 0.5489 |  |
| GMI (%) | +0.0508 | 0.0833 | ±0.1667 | +0.609 | 0.5423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **783**, R² = **0.3089**, Adj R² = **0.2963**, F-statistic = **24.52** (p = **1.03e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.4**, BIC = **3391.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8044** | 0.6542 | ±1.3083 | **+34.861** | **2.90e-266** | *** |
| Education: graduate level (vs college) | -0.2526 | 0.1554 | ±0.3107 | -1.626 | 0.1040 |  |
| Education: high school or below (vs college) | +0.0733 | 0.2310 | ±0.4620 | +0.317 | 0.7509 |  |
| Site: UCSD (vs UAB) | +0.0122 | 0.1840 | ±0.3680 | +0.066 | 0.9473 |  |
| **Site: UW (vs UAB)** | **-1.2692** | 0.1759 | ±0.3519 | **-7.213** | **5.46e-13** | *** |
| Season: spring (vs autumn) | -0.2303 | 0.1960 | ±0.3920 | -1.175 | 0.2401 |  |
| **Season: summer (vs autumn)** | **+2.0251** | 0.2223 | ±0.4445 | **+9.111** | **8.16e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9699** | 0.1966 | ±0.3932 | **-4.933** | **8.10e-07** | *** |
| **Age (years)** | **+0.0208** | 0.0075 | ±0.0149 | **+2.792** | **0.0052** | ** |
| BMI (kg/m2) | +0.0180 | 0.0113 | ±0.0225 | +1.603 | 0.1089 |  |
| Hypertension | +0.1284 | 0.1550 | ±0.3099 | +0.829 | 0.4073 |  |
| High cholesterol | +0.0916 | 0.1542 | ±0.3083 | +0.594 | 0.5522 |  |
| Kidney disease | +0.1318 | 0.1970 | ±0.3939 | +0.669 | 0.5033 |  |
| Circulatory disease | +0.1215 | 0.2010 | ±0.4020 | +0.604 | 0.5457 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0011 | 0.0019 | ±0.0038 | +0.591 | 0.5545 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **783**, R² = **0.3093**, Adj R² = **0.2967**, F-statistic = **24.57** (p = **8.11e-53**), Residual SE = **1.998** on **768** df, AIC = **3320.9**, BIC = **3390.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.7761** | 0.6376 | ±1.2753 | **+35.719** | **2.01e-279** | *** |
| Education: graduate level (vs college) | -0.2485 | 0.1550 | ±0.3100 | -1.603 | 0.1089 |  |
| Education: high school or below (vs college) | +0.0682 | 0.2313 | ±0.4626 | +0.295 | 0.7682 |  |
| Site: UCSD (vs UAB) | +0.0171 | 0.1839 | ±0.3678 | +0.093 | 0.9258 |  |
| **Site: UW (vs UAB)** | **-1.2531** | 0.1773 | ±0.3546 | **-7.067** | **1.58e-12** | *** |
| Season: spring (vs autumn) | -0.2309 | 0.1959 | ±0.3918 | -1.179 | 0.2386 |  |
| **Season: summer (vs autumn)** | **+2.0256** | 0.2220 | ±0.4440 | **+9.124** | **7.26e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9696** | 0.1967 | ±0.3933 | **-4.930** | **8.21e-07** | *** |
| **Age (years)** | **+0.0204** | 0.0075 | ±0.0149 | **+2.738** | **0.0062** | ** |
| BMI (kg/m2) | +0.0180 | 0.0110 | ±0.0220 | +1.631 | 0.1030 |  |
| Hypertension | +0.1218 | 0.1552 | ±0.3104 | +0.785 | 0.4326 |  |
| High cholesterol | +0.0965 | 0.1541 | ±0.3083 | +0.626 | 0.5315 |  |
| Kidney disease | +0.0973 | 0.2006 | ±0.4012 | +0.485 | 0.6275 |  |
| Circulatory disease | +0.1187 | 0.1998 | ±0.3997 | +0.594 | 0.5525 |  |
| Glucose SD, pooled (mg/dL) | +0.0060 | 0.0066 | ±0.0133 | +0.898 | 0.3689 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **783**, R² = **0.3090**, Adj R² = **0.2964**, F-statistic = **24.53** (p = **9.60e-53**), Residual SE = **1.999** on **768** df, AIC = **3321.3**, BIC = **3391.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8103** | 0.6405 | ±1.2810 | **+35.613** | **8.80e-278** | *** |
| Education: graduate level (vs college) | -0.2525 | 0.1550 | ±0.3100 | -1.629 | 0.1033 |  |
| Education: high school or below (vs college) | +0.0711 | 0.2317 | ±0.4634 | +0.307 | 0.7589 |  |
| Site: UCSD (vs UAB) | +0.0144 | 0.1836 | ±0.3672 | +0.078 | 0.9375 |  |
| **Site: UW (vs UAB)** | **-1.2593** | 0.1768 | ±0.3536 | **-7.123** | **1.05e-12** | *** |
| Season: spring (vs autumn) | -0.2292 | 0.1957 | ±0.3914 | -1.171 | 0.2416 |  |
| **Season: summer (vs autumn)** | **+2.0247** | 0.2219 | ±0.4437 | **+9.126** | **7.11e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9671** | 0.1968 | ±0.3936 | **-4.915** | **8.90e-07** | *** |
| **Age (years)** | **+0.0204** | 0.0075 | ±0.0149 | **+2.732** | **0.0063** | ** |
| BMI (kg/m2) | +0.0185 | 0.0110 | ±0.0219 | +1.686 | 0.0918 | . |
| Hypertension | +0.1247 | 0.1556 | ±0.3111 | +0.801 | 0.4229 |  |
| High cholesterol | +0.0954 | 0.1542 | ±0.3085 | +0.618 | 0.5364 |  |
| Kidney disease | +0.1037 | 0.2002 | ±0.4004 | +0.518 | 0.6046 |  |
| Circulatory disease | +0.1222 | 0.1999 | ±0.3997 | +0.612 | 0.5408 |  |
| Avg. daily SD (mg/dL) | +0.0053 | 0.0072 | ±0.0144 | +0.732 | 0.4643 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **783**, R² = **0.3094**, Adj R² = **0.2968**, F-statistic = **24.58** (p = **7.87e-53**), Residual SE = **1.998** on **768** df, AIC = **3320.9**, BIC = **3390.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.6717** | 0.6754 | ±1.3508 | **+33.568** | **4.99e-247** | *** |
| Education: graduate level (vs college) | -0.2505 | 0.1547 | ±0.3094 | -1.620 | 0.1053 |  |
| Education: high school or below (vs college) | +0.0868 | 0.2290 | ±0.4579 | +0.379 | 0.7047 |  |
| Site: UCSD (vs UAB) | +0.0120 | 0.1830 | ±0.3659 | +0.065 | 0.9479 |  |
| **Site: UW (vs UAB)** | **-1.2568** | 0.1754 | ±0.3507 | **-7.167** | **7.69e-13** | *** |
| Season: spring (vs autumn) | -0.2245 | 0.1954 | ±0.3908 | -1.149 | 0.2504 |  |
| **Season: summer (vs autumn)** | **+2.0196** | 0.2217 | ±0.4434 | **+9.109** | **8.32e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9679** | 0.1969 | ±0.3937 | **-4.917** | **8.80e-07** | *** |
| **Age (years)** | **+0.0202** | 0.0075 | ±0.0149 | **+2.703** | **0.0069** | ** |
| BMI (kg/m2) | +0.0189 | 0.0109 | ±0.0219 | +1.731 | 0.0834 | . |
| Hypertension | +0.1228 | 0.1562 | ±0.3124 | +0.786 | 0.4316 |  |
| High cholesterol | +0.1022 | 0.1545 | ±0.3089 | +0.662 | 0.5083 |  |
| Kidney disease | +0.0956 | 0.2021 | ±0.4043 | +0.473 | 0.6361 |  |
| Circulatory disease | +0.1273 | 0.1994 | ±0.3987 | +0.639 | 0.5230 |  |
| CV (%) | +0.0132 | 0.0133 | ±0.0266 | +0.993 | 0.3207 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **783**, R² = **0.3104**, Adj R² = **0.2978**, F-statistic = **24.69** (p = **4.65e-53**), Residual SE = **1.997** on **768** df, AIC = **3319.8**, BIC = **3389.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4599** | 0.6962 | ±1.3925 | **+33.695** | **6.89e-249** | *** |
| Education: graduate level (vs college) | -0.2494 | 0.1544 | ±0.3087 | -1.616 | 0.1062 |  |
| Education: high school or below (vs college) | +0.0863 | 0.2290 | ±0.4581 | +0.377 | 0.7063 |  |
| Site: UCSD (vs UAB) | +0.0095 | 0.1826 | ±0.3651 | +0.052 | 0.9585 |  |
| **Site: UW (vs UAB)** | **-1.2528** | 0.1750 | ±0.3500 | **-7.159** | **8.10e-13** | *** |
| Season: spring (vs autumn) | -0.2288 | 0.1952 | ±0.3905 | -1.172 | 0.2412 |  |
| **Season: summer (vs autumn)** | **+2.0085** | 0.2217 | ±0.4433 | **+9.061** | **1.29e-19** | *** |
| **Season: winter (vs autumn)** | **-0.9743** | 0.1966 | ±0.3932 | **-4.956** | **7.21e-07** | *** |
| **Age (years)** | **+0.0201** | 0.0074 | ±0.0149 | **+2.701** | **0.0069** | ** |
| BMI (kg/m2) | +0.0191 | 0.0109 | ±0.0219 | +1.745 | 0.0810 | . |
| Hypertension | +0.1196 | 0.1559 | ±0.3118 | +0.767 | 0.4431 |  |
| High cholesterol | +0.1000 | 0.1541 | ±0.3083 | +0.649 | 0.5165 |  |
| Kidney disease | +0.0875 | 0.2004 | ±0.4008 | +0.437 | 0.6623 |  |
| Circulatory disease | +0.1222 | 0.1990 | ±0.3980 | +0.614 | 0.5392 |  |
| Mean / SD ratio | -0.1054 | 0.0712 | ±0.1423 | -1.482 | 0.1384 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **783**, R² = **0.3098**, Adj R² = **0.2972**, F-statistic = **24.62** (p = **6.41e-53**), Residual SE = **1.998** on **768** df, AIC = **3320.4**, BIC = **3390.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.3401** | 0.6895 | ±1.3791 | **+33.848** | **3.82e-251** | *** |
| Education: graduate level (vs college) | -0.2532 | 0.1547 | ±0.3093 | -1.637 | 0.1016 |  |
| Education: high school or below (vs college) | +0.0857 | 0.2293 | ±0.4586 | +0.374 | 0.7087 |  |
| Site: UCSD (vs UAB) | +0.0074 | 0.1828 | ±0.3656 | +0.040 | 0.9677 |  |
| **Site: UW (vs UAB)** | **-1.2594** | 0.1750 | ±0.3500 | **-7.196** | **6.21e-13** | *** |
| Season: spring (vs autumn) | -0.2221 | 0.1951 | ±0.3902 | -1.138 | 0.2550 |  |
| **Season: summer (vs autumn)** | **+2.0137** | 0.2215 | ±0.4431 | **+9.090** | **9.93e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9683** | 0.1970 | ±0.3941 | **-4.914** | **8.93e-07** | *** |
| **Age (years)** | **+0.0200** | 0.0075 | ±0.0149 | **+2.686** | **0.0072** | ** |
| BMI (kg/m2) | +0.0195 | 0.0110 | ±0.0219 | +1.781 | 0.0750 | . |
| Hypertension | +0.1224 | 0.1562 | ±0.3124 | +0.784 | 0.4333 |  |
| High cholesterol | +0.0999 | 0.1543 | ±0.3085 | +0.648 | 0.5171 |  |
| Kidney disease | +0.0981 | 0.1999 | ±0.3999 | +0.491 | 0.6237 |  |
| Circulatory disease | +0.1275 | 0.1994 | ±0.3987 | +0.639 | 0.5226 |  |
| Avg. daily mean/SD | -0.0691 | 0.0597 | ±0.1195 | -1.157 | 0.2473 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **783**, R² = **0.3086**, Adj R² = **0.2960**, F-statistic = **24.48** (p = **1.22e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.8**, BIC = **3391.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8706** | 0.7095 | ±1.4190 | **+32.235** | **5.72e-228** | *** |
| Education: graduate level (vs college) | -0.2556 | 0.1562 | ±0.3123 | -1.637 | 0.1017 |  |
| Education: high school or below (vs college) | +0.0876 | 0.2283 | ±0.4566 | +0.384 | 0.7011 |  |
| Site: UCSD (vs UAB) | +0.0072 | 0.1829 | ±0.3658 | +0.039 | 0.9685 |  |
| **Site: UW (vs UAB)** | **-1.2682** | 0.1755 | ±0.3509 | **-7.227** | **4.93e-13** | *** |
| Season: spring (vs autumn) | -0.2246 | 0.1952 | ±0.3903 | -1.151 | 0.2498 |  |
| **Season: summer (vs autumn)** | **+2.0225** | 0.2226 | ±0.4453 | **+9.084** | **1.05e-19** | *** |
| **Season: winter (vs autumn)** | **-0.9662** | 0.1963 | ±0.3927 | **-4.921** | **8.61e-07** | *** |
| **Age (years)** | **+0.0206** | 0.0075 | ±0.0149 | **+2.766** | **0.0057** | ** |
| BMI (kg/m2) | +0.0191 | 0.0110 | ±0.0220 | +1.741 | 0.0816 | . |
| Hypertension | +0.1318 | 0.1557 | ±0.3113 | +0.847 | 0.3971 |  |
| High cholesterol | +0.0956 | 0.1548 | ±0.3096 | +0.617 | 0.5371 |  |
| Kidney disease | +0.1306 | 0.1978 | ±0.3957 | +0.660 | 0.5090 |  |
| Circulatory disease | +0.1281 | 0.1999 | ±0.3998 | +0.641 | 0.5218 |  |
| MAG (mg/dL/h) | +0.0017 | 0.0077 | ±0.0153 | +0.224 | 0.8230 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **783**, R² = **0.3094**, Adj R² = **0.2968**, F-statistic = **24.57** (p = **7.99e-53**), Residual SE = **1.998** on **768** df, AIC = **3320.9**, BIC = **3390.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.6628** | 0.6744 | ±1.3488 | **+33.604** | **1.46e-247** | *** |
| Education: graduate level (vs college) | -0.2507 | 0.1548 | ±0.3095 | -1.620 | 0.1053 |  |
| Education: high school or below (vs college) | +0.0664 | 0.2311 | ±0.4622 | +0.287 | 0.7739 |  |
| Site: UCSD (vs UAB) | +0.0201 | 0.1834 | ±0.3668 | +0.109 | 0.9129 |  |
| **Site: UW (vs UAB)** | **-1.2531** | 0.1768 | ±0.3535 | **-7.089** | **1.35e-12** | *** |
| Season: spring (vs autumn) | -0.2334 | 0.1959 | ±0.3918 | -1.192 | 0.2334 |  |
| **Season: summer (vs autumn)** | **+2.0220** | 0.2216 | ±0.4433 | **+9.124** | **7.27e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9688** | 0.1968 | ±0.3935 | **-4.924** | **8.49e-07** | *** |
| **Age (years)** | **+0.0206** | 0.0074 | ±0.0149 | **+2.770** | **0.0056** | ** |
| BMI (kg/m2) | +0.0186 | 0.0109 | ±0.0219 | +1.696 | 0.0900 | . |
| Hypertension | +0.1277 | 0.1553 | ±0.3107 | +0.822 | 0.4110 |  |
| High cholesterol | +0.0973 | 0.1544 | ±0.3088 | +0.630 | 0.5286 |  |
| Kidney disease | +0.0954 | 0.2004 | ±0.4008 | +0.476 | 0.6340 |  |
| Circulatory disease | +0.1195 | 0.1998 | ±0.3996 | +0.598 | 0.5497 |  |
| Avg. daily range (mg/dL) | +0.0020 | 0.0021 | ±0.0041 | +0.978 | 0.3280 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **783**, R² = **0.3095**, Adj R² = **0.2969**, F-statistic = **24.59** (p = **7.32e-53**), Residual SE = **1.998** on **768** df, AIC = **3320.7**, BIC = **3390.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8655** | 0.6145 | ±1.2291 | **+37.208** | **5.01e-303** | *** |
| Education: graduate level (vs college) | -0.2413 | 0.1558 | ±0.3117 | -1.549 | 0.1215 |  |
| Education: high school or below (vs college) | +0.0798 | 0.2292 | ±0.4585 | +0.348 | 0.7279 |  |
| Site: UCSD (vs UAB) | +0.0133 | 0.1842 | ±0.3684 | +0.072 | 0.9426 |  |
| **Site: UW (vs UAB)** | **-1.2564** | 0.1775 | ±0.3551 | **-7.077** | **1.47e-12** | *** |
| Season: spring (vs autumn) | -0.2299 | 0.1962 | ±0.3925 | -1.172 | 0.2413 |  |
| **Season: summer (vs autumn)** | **+2.0193** | 0.2223 | ±0.4445 | **+9.085** | **1.03e-19** | *** |
| **Season: winter (vs autumn)** | **-0.9772** | 0.1963 | ±0.3926 | **-4.978** | **6.43e-07** | *** |
| **Age (years)** | **+0.0209** | 0.0075 | ±0.0149 | **+2.798** | **0.0051** | ** |
| BMI (kg/m2) | +0.0176 | 0.0112 | ±0.0224 | +1.572 | 0.1159 |  |
| Hypertension | +0.1192 | 0.1547 | ±0.3094 | +0.770 | 0.4412 |  |
| High cholesterol | +0.0947 | 0.1541 | ±0.3082 | +0.614 | 0.5390 |  |
| Kidney disease | +0.1170 | 0.1987 | ±0.3973 | +0.589 | 0.5560 |  |
| Circulatory disease | +0.1126 | 0.2001 | ±0.4003 | +0.562 | 0.5738 |  |
| SD of daily means (mg/dL) | +0.0096 | 0.0112 | ±0.0224 | +0.859 | 0.3901 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **783**, R² = **0.3094**, Adj R² = **0.2968**, F-statistic = **24.57** (p = **8.01e-53**), Residual SE = **1.998** on **768** df, AIC = **3320.9**, BIC = **3390.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.2113** | 0.6837 | ±1.3674 | **+33.949** | **1.28e-252** | *** |
| Education: graduate level (vs college) | -0.2520 | 0.1551 | ±0.3103 | -1.624 | 0.1044 |  |
| Education: high school or below (vs college) | +0.0631 | 0.2315 | ±0.4631 | +0.273 | 0.7852 |  |
| Site: UCSD (vs UAB) | +0.0199 | 0.1841 | ±0.3682 | +0.108 | 0.9139 |  |
| **Site: UW (vs UAB)** | **-1.2590** | 0.1766 | ±0.3532 | **-7.128** | **1.02e-12** | *** |
| Season: spring (vs autumn) | -0.2302 | 0.1956 | ±0.3912 | -1.177 | 0.2393 |  |
| **Season: summer (vs autumn)** | **+2.0256** | 0.2223 | ±0.4447 | **+9.110** | **8.22e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9717** | 0.1963 | ±0.3926 | **-4.950** | **7.41e-07** | *** |
| **Age (years)** | **+0.0206** | 0.0075 | ±0.0149 | **+2.758** | **0.0058** | ** |
| BMI (kg/m2) | +0.0175 | 0.0111 | ±0.0222 | +1.574 | 0.1154 |  |
| Hypertension | +0.1271 | 0.1549 | ±0.3097 | +0.821 | 0.4118 |  |
| High cholesterol | +0.0936 | 0.1540 | ±0.3080 | +0.608 | 0.5431 |  |
| Kidney disease | +0.1179 | 0.1969 | ±0.3938 | +0.599 | 0.5494 |  |
| Circulatory disease | +0.1184 | 0.2006 | ±0.4012 | +0.590 | 0.5550 |  |
| Time in range 70-180, pooled (%) | -0.0029 | 0.0032 | ±0.0064 | -0.896 | 0.3704 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **783**, R² = **0.3092**, Adj R² = **0.2966**, F-statistic = **24.55** (p = **8.80e-53**), Residual SE = **1.998** on **768** df, AIC = **3321.1**, BIC = **3391.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.1850** | 0.6842 | ±1.3683 | **+33.889** | **9.78e-252** | *** |
| Education: graduate level (vs college) | -0.2533 | 0.1552 | ±0.3104 | -1.632 | 0.1026 |  |
| Education: high school or below (vs college) | +0.0655 | 0.2317 | ±0.4634 | +0.283 | 0.7773 |  |
| Site: UCSD (vs UAB) | +0.0189 | 0.1842 | ±0.3684 | +0.102 | 0.9184 |  |
| **Site: UW (vs UAB)** | **-1.2606** | 0.1767 | ±0.3535 | **-7.133** | **9.85e-13** | *** |
| Season: spring (vs autumn) | -0.2301 | 0.1956 | ±0.3912 | -1.176 | 0.2395 |  |
| **Season: summer (vs autumn)** | **+2.0241** | 0.2223 | ±0.4446 | **+9.105** | **8.65e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9720** | 0.1964 | ±0.3928 | **-4.949** | **7.46e-07** | *** |
| **Age (years)** | **+0.0206** | 0.0075 | ±0.0149 | **+2.754** | **0.0059** | ** |
| BMI (kg/m2) | +0.0177 | 0.0111 | ±0.0223 | +1.590 | 0.1119 |  |
| Hypertension | +0.1277 | 0.1549 | ±0.3098 | +0.824 | 0.4097 |  |
| High cholesterol | +0.0934 | 0.1540 | ±0.3081 | +0.607 | 0.5441 |  |
| Kidney disease | +0.1189 | 0.1968 | ±0.3935 | +0.604 | 0.5457 |  |
| Circulatory disease | +0.1197 | 0.2006 | ±0.4013 | +0.597 | 0.5506 |  |
| Avg. daily time in range 70-180 (%) | -0.0025 | 0.0032 | ±0.0064 | -0.793 | 0.4275 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.3086**, Adj R² = **0.2960**, F-statistic = **24.49** (p = **1.20e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.8**, BIC = **3391.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9791** | 0.6227 | ±1.2453 | **+36.904** | **4.00e-298** | *** |
| Education: graduate level (vs college) | -0.2602 | 0.1548 | ±0.3097 | -1.681 | 0.0928 | . |
| Education: high school or below (vs college) | +0.0864 | 0.2273 | ±0.4545 | +0.380 | 0.7037 |  |
| Site: UCSD (vs UAB) | +0.0012 | 0.1845 | ±0.3689 | +0.006 | 0.9950 |  |
| **Site: UW (vs UAB)** | **-1.2779** | 0.1752 | ±0.3505 | **-7.293** | **3.04e-13** | *** |
| Season: spring (vs autumn) | -0.2246 | 0.1950 | ±0.3900 | -1.152 | 0.2494 |  |
| **Season: summer (vs autumn)** | **+2.0166** | 0.2223 | ±0.4447 | **+9.071** | **1.18e-19** | *** |
| **Season: winter (vs autumn)** | **-0.9711** | 0.1975 | ±0.3949 | **-4.918** | **8.74e-07** | *** |
| **Age (years)** | **+0.0204** | 0.0075 | ±0.0150 | **+2.724** | **0.0064** | ** |
| BMI (kg/m2) | +0.0193 | 0.0109 | ±0.0219 | +1.765 | 0.0776 | . |
| Hypertension | +0.1334 | 0.1563 | ±0.3126 | +0.853 | 0.3935 |  |
| High cholesterol | +0.0891 | 0.1532 | ±0.3064 | +0.582 | 0.5607 |  |
| Kidney disease | +0.1356 | 0.1970 | ±0.3940 | +0.688 | 0.4912 |  |
| Circulatory disease | +0.1313 | 0.1992 | ±0.3985 | +0.659 | 0.5100 |  |
| Any reading < 54 during wear (0/1) | -0.0499 | 0.1711 | ±0.3421 | -0.292 | 0.7704 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.3113**, Adj R² = **0.2988**, F-statistic = **24.80** (p = **2.80e-53**), Residual SE = **1.995** on **768** df, AIC = **3318.7**, BIC = **3388.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.8945** | 0.6099 | ±1.2198 | **+37.537** | **2.30e-308** | *** |
| Education: graduate level (vs college) | -0.2428 | 0.1548 | ±0.3096 | -1.569 | 0.1168 |  |
| Education: high school or below (vs college) | +0.1096 | 0.2286 | ±0.4573 | +0.479 | 0.6318 |  |
| Site: UCSD (vs UAB) | +0.0265 | 0.1828 | ±0.3656 | +0.145 | 0.8849 |  |
| **Site: UW (vs UAB)** | **-1.2464** | 0.1748 | ±0.3495 | **-7.132** | **9.90e-13** | *** |
| Season: spring (vs autumn) | -0.2158 | 0.1954 | ±0.3908 | -1.104 | 0.2695 |  |
| **Season: summer (vs autumn)** | **+2.0299** | 0.2221 | ±0.4441 | **+9.141** | **6.18e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9765** | 0.1960 | ±0.3921 | **-4.981** | **6.31e-07** | *** |
| **Age (years)** | **+0.0201** | 0.0075 | ±0.0149 | **+2.691** | **0.0071** | ** |
| BMI (kg/m2) | +0.0203 | 0.0109 | ±0.0218 | +1.862 | 0.0627 | . |
| Hypertension | +0.1299 | 0.1554 | ±0.3109 | +0.835 | 0.4034 |  |
| High cholesterol | +0.1151 | 0.1542 | ±0.3085 | +0.746 | 0.4556 |  |
| Kidney disease | +0.1365 | 0.1965 | ±0.3930 | +0.694 | 0.4874 |  |
| Circulatory disease | +0.1389 | 0.2001 | ±0.4001 | +0.694 | 0.4875 |  |
| Time < 54 (%) | +0.2230 | 0.1819 | ±0.3639 | +1.226 | 0.2204 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.3098**, Adj R² = **0.2972**, F-statistic = **24.63** (p = **6.22e-53**), Residual SE = **1.997** on **768** df, AIC = **3320.4**, BIC = **3390.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9197** | 0.6098 | ±1.2196 | **+37.585** | **3.73e-309** | *** |
| Education: graduate level (vs college) | -0.2492 | 0.1549 | ±0.3098 | -1.609 | 0.1076 |  |
| Education: high school or below (vs college) | +0.1038 | 0.2286 | ±0.4572 | +0.454 | 0.6497 |  |
| Site: UCSD (vs UAB) | +0.0196 | 0.1829 | ±0.3658 | +0.107 | 0.9145 |  |
| **Site: UW (vs UAB)** | **-1.2533** | 0.1751 | ±0.3503 | **-7.156** | **8.30e-13** | *** |
| Season: spring (vs autumn) | -0.2121 | 0.1960 | ±0.3919 | -1.082 | 0.2791 |  |
| **Season: summer (vs autumn)** | **+2.0325** | 0.2228 | ±0.4455 | **+9.124** | **7.24e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9701** | 0.1973 | ±0.3946 | **-4.917** | **8.78e-07** | *** |
| **Age (years)** | **+0.0202** | 0.0075 | ±0.0149 | **+2.708** | **0.0068** | ** |
| BMI (kg/m2) | +0.0197 | 0.0109 | ±0.0219 | +1.797 | 0.0723 | . |
| Hypertension | +0.1290 | 0.1558 | ±0.3117 | +0.828 | 0.4079 |  |
| High cholesterol | +0.1102 | 0.1545 | ±0.3090 | +0.714 | 0.4755 |  |
| Kidney disease | +0.1321 | 0.1967 | ±0.3935 | +0.671 | 0.5019 |  |
| Circulatory disease | +0.1351 | 0.1999 | ±0.3997 | +0.676 | 0.4991 |  |
| Avg. daily time < 54 (%) | +0.1760 | 0.2616 | ±0.5231 | +0.673 | 0.5011 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.3090**, Adj R² = **0.2964**, F-statistic = **24.53** (p = **9.85e-53**), Residual SE = **1.999** on **768** df, AIC = **3321.4**, BIC = **3391.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9345** | 0.6130 | ±1.2260 | **+37.414** | **2.33e-306** | *** |
| Education: graduate level (vs college) | -0.2518 | 0.1555 | ±0.3110 | -1.620 | 0.1053 |  |
| Education: high school or below (vs college) | +0.0958 | 0.2283 | ±0.4565 | +0.420 | 0.6747 |  |
| Site: UCSD (vs UAB) | +0.0151 | 0.1838 | ±0.3675 | +0.082 | 0.9343 |  |
| **Site: UW (vs UAB)** | **-1.2622** | 0.1759 | ±0.3517 | **-7.178** | **7.09e-13** | *** |
| Season: spring (vs autumn) | -0.2168 | 0.1951 | ±0.3903 | -1.111 | 0.2666 |  |
| **Season: summer (vs autumn)** | **+2.0280** | 0.2216 | ±0.4432 | **+9.151** | **5.65e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9639** | 0.1970 | ±0.3940 | **-4.892** | **9.96e-07** | *** |
| **Age (years)** | **+0.0203** | 0.0074 | ±0.0149 | **+2.728** | **0.0064** | ** |
| BMI (kg/m2) | +0.0192 | 0.0110 | ±0.0219 | +1.757 | 0.0790 | . |
| Hypertension | +0.1268 | 0.1566 | ±0.3132 | +0.810 | 0.4181 |  |
| High cholesterol | +0.1056 | 0.1549 | ±0.3097 | +0.682 | 0.4955 |  |
| Kidney disease | +0.1296 | 0.1973 | ±0.3945 | +0.657 | 0.5113 |  |
| Circulatory disease | +0.1352 | 0.2008 | ±0.4017 | +0.673 | 0.5008 |  |
| Time 54-69, pooled (%) | +0.0493 | 0.0842 | ±0.1685 | +0.586 | 0.5580 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **783**, R² = **0.3092**, Adj R² = **0.2966**, F-statistic = **24.56** (p = **8.60e-53**), Residual SE = **1.998** on **768** df, AIC = **3321.1**, BIC = **3391.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9353** | 0.6118 | ±1.2236 | **+37.487** | **1.50e-307** | *** |
| Education: graduate level (vs college) | -0.2493 | 0.1553 | ±0.3107 | -1.605 | 0.1085 |  |
| Education: high school or below (vs college) | +0.0982 | 0.2283 | ±0.4565 | +0.430 | 0.6672 |  |
| Site: UCSD (vs UAB) | +0.0182 | 0.1836 | ±0.3673 | +0.099 | 0.9213 |  |
| **Site: UW (vs UAB)** | **-1.2571** | 0.1756 | ±0.3513 | **-7.157** | **8.23e-13** | *** |
| Season: spring (vs autumn) | -0.2154 | 0.1951 | ±0.3902 | -1.104 | 0.2696 |  |
| **Season: summer (vs autumn)** | **+2.0300** | 0.2217 | ±0.4433 | **+9.158** | **5.29e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9648** | 0.1970 | ±0.3941 | **-4.897** | **9.75e-07** | *** |
| **Age (years)** | **+0.0202** | 0.0074 | ±0.0149 | **+2.714** | **0.0067** | ** |
| BMI (kg/m2) | +0.0192 | 0.0110 | ±0.0219 | +1.749 | 0.0803 | . |
| Hypertension | +0.1257 | 0.1567 | ±0.3134 | +0.802 | 0.4224 |  |
| High cholesterol | +0.1094 | 0.1548 | ±0.3096 | +0.707 | 0.4798 |  |
| Kidney disease | +0.1290 | 0.1971 | ±0.3942 | +0.655 | 0.5128 |  |
| Circulatory disease | +0.1376 | 0.2005 | ±0.4011 | +0.686 | 0.4926 |  |
| Avg. daily time 54-69 (%) | +0.0589 | 0.0824 | ±0.1648 | +0.715 | 0.4743 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **783**, R² = **0.3099**, Adj R² = **0.2974**, F-statistic = **24.64** (p = **5.87e-53**), Residual SE = **1.997** on **768** df, AIC = **3320.3**, BIC = **3390.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9072** | 0.6123 | ±1.2247 | **+37.409** | **2.76e-306** | *** |
| Education: graduate level (vs college) | -0.2449 | 0.1553 | ±0.3105 | -1.577 | 0.1147 |  |
| Education: high school or below (vs college) | +0.1039 | 0.2282 | ±0.4565 | +0.455 | 0.6489 |  |
| Site: UCSD (vs UAB) | +0.0255 | 0.1834 | ±0.3667 | +0.139 | 0.8893 |  |
| **Site: UW (vs UAB)** | **-1.2496** | 0.1757 | ±0.3513 | **-7.113** | **1.13e-12** | *** |
| Season: spring (vs autumn) | -0.2119 | 0.1954 | ±0.3909 | -1.084 | 0.2782 |  |
| **Season: summer (vs autumn)** | **+2.0343** | 0.2218 | ±0.4437 | **+9.170** | **4.72e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9653** | 0.1970 | ±0.3940 | **-4.901** | **9.55e-07** | *** |
| **Age (years)** | **+0.0201** | 0.0074 | ±0.0149 | **+2.703** | **0.0069** | ** |
| BMI (kg/m2) | +0.0195 | 0.0110 | ±0.0219 | +1.784 | 0.0744 | . |
| Hypertension | +0.1253 | 0.1564 | ±0.3129 | +0.801 | 0.4233 |  |
| High cholesterol | +0.1162 | 0.1547 | ±0.3094 | +0.751 | 0.4526 |  |
| Kidney disease | +0.1286 | 0.1973 | ±0.3946 | +0.652 | 0.5144 |  |
| Circulatory disease | +0.1402 | 0.2010 | ±0.4020 | +0.698 | 0.4855 |  |
| Time < 70 (%) | +0.0655 | 0.0692 | ±0.1383 | +0.947 | 0.3436 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **783**, R² = **0.3096**, Adj R² = **0.2970**, F-statistic = **24.60** (p = **7.09e-53**), Residual SE = **1.998** on **768** df, AIC = **3320.7**, BIC = **3390.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9245** | 0.6113 | ±1.2225 | **+37.504** | **8.08e-308** | *** |
| Education: graduate level (vs college) | -0.2470 | 0.1552 | ±0.3103 | -1.592 | 0.1114 |  |
| Education: high school or below (vs college) | +0.1021 | 0.2283 | ±0.4566 | +0.447 | 0.6547 |  |
| Site: UCSD (vs UAB) | +0.0221 | 0.1833 | ±0.3667 | +0.121 | 0.9039 |  |
| **Site: UW (vs UAB)** | **-1.2515** | 0.1755 | ±0.3510 | **-7.131** | **9.95e-13** | *** |
| Season: spring (vs autumn) | -0.2122 | 0.1953 | ±0.3906 | -1.087 | 0.2772 |  |
| **Season: summer (vs autumn)** | **+2.0335** | 0.2219 | ±0.4438 | **+9.165** | **4.98e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9658** | 0.1970 | ±0.3941 | **-4.902** | **9.50e-07** | *** |
| **Age (years)** | **+0.0201** | 0.0074 | ±0.0149 | **+2.703** | **0.0069** | ** |
| BMI (kg/m2) | +0.0193 | 0.0110 | ±0.0219 | +1.762 | 0.0781 | . |
| Hypertension | +0.1255 | 0.1565 | ±0.3129 | +0.802 | 0.4225 |  |
| High cholesterol | +0.1137 | 0.1547 | ±0.3093 | +0.735 | 0.4624 |  |
| Kidney disease | +0.1287 | 0.1971 | ±0.3942 | +0.653 | 0.5138 |  |
| Circulatory disease | +0.1389 | 0.2004 | ±0.4009 | +0.693 | 0.4882 |  |
| Avg. daily time < 70 (%) | +0.0549 | 0.0657 | ±0.1315 | +0.836 | 0.4033 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.3091**, Adj R² = **0.2965**, F-statistic = **24.54** (p = **9.14e-53**), Residual SE = **1.998** on **768** df, AIC = **3321.2**, BIC = **3391.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.2769** | 0.7624 | ±1.5248 | **+30.530** | **1.04e-204** | *** |
| Education: graduate level (vs college) | -0.2491 | 0.1554 | ±0.3108 | -1.603 | 0.1090 |  |
| Education: high school or below (vs college) | +0.0696 | 0.2308 | ±0.4616 | +0.301 | 0.7631 |  |
| Site: UCSD (vs UAB) | +0.0155 | 0.1844 | ±0.3689 | +0.084 | 0.9329 |  |
| **Site: UW (vs UAB)** | **-1.2601** | 0.1769 | ±0.3538 | **-7.123** | **1.05e-12** | *** |
| Season: spring (vs autumn) | -0.2250 | 0.1956 | ±0.3913 | -1.150 | 0.2501 |  |
| **Season: summer (vs autumn)** | **+2.0309** | 0.2225 | ±0.4451 | **+9.126** | **7.11e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9676** | 0.1965 | ±0.3930 | **-4.924** | **8.47e-07** | *** |
| **Age (years)** | **+0.0209** | 0.0075 | ±0.0149 | **+2.803** | **0.0051** | ** |
| BMI (kg/m2) | +0.0186 | 0.0110 | ±0.0221 | +1.680 | 0.0930 | . |
| Hypertension | +0.1255 | 0.1548 | ±0.3095 | +0.811 | 0.4175 |  |
| High cholesterol | +0.0955 | 0.1542 | ±0.3083 | +0.620 | 0.5354 |  |
| Kidney disease | +0.1257 | 0.1974 | ±0.3948 | +0.637 | 0.5244 |  |
| Circulatory disease | +0.1199 | 0.2012 | ±0.4024 | +0.596 | 0.5512 |  |
| Time 54-250, pooled (%) | -0.0036 | 0.0049 | ±0.0098 | -0.729 | 0.4662 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.3090**, Adj R² = **0.2964**, F-statistic = **24.53** (p = **9.82e-53**), Residual SE = **1.999** on **768** df, AIC = **3321.3**, BIC = **3391.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.2459** | 0.7725 | ±1.5450 | **+30.092** | **6.20e-199** | *** |
| Education: graduate level (vs college) | -0.2504 | 0.1555 | ±0.3110 | -1.611 | 0.1072 |  |
| Education: high school or below (vs college) | +0.0719 | 0.2308 | ±0.4615 | +0.312 | 0.7553 |  |
| Site: UCSD (vs UAB) | +0.0143 | 0.1845 | ±0.3691 | +0.077 | 0.9384 |  |
| **Site: UW (vs UAB)** | **-1.2623** | 0.1769 | ±0.3537 | **-7.137** | **9.51e-13** | *** |
| Season: spring (vs autumn) | -0.2252 | 0.1956 | ±0.3912 | -1.152 | 0.2495 |  |
| **Season: summer (vs autumn)** | **+2.0289** | 0.2226 | ±0.4452 | **+9.114** | **7.92e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9679** | 0.1965 | ±0.3931 | **-4.924** | **8.46e-07** | *** |
| **Age (years)** | **+0.0208** | 0.0075 | ±0.0149 | **+2.792** | **0.0052** | ** |
| BMI (kg/m2) | +0.0186 | 0.0111 | ±0.0221 | +1.684 | 0.0922 | . |
| Hypertension | +0.1264 | 0.1548 | ±0.3096 | +0.817 | 0.4141 |  |
| High cholesterol | +0.0953 | 0.1542 | ±0.3084 | +0.618 | 0.5367 |  |
| Kidney disease | +0.1259 | 0.1974 | ±0.3948 | +0.638 | 0.5235 |  |
| Circulatory disease | +0.1205 | 0.2013 | ±0.4026 | +0.599 | 0.5493 |  |
| Avg. daily time 54-250 (%) | -0.0032 | 0.0050 | ±0.0100 | -0.635 | 0.5252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.3089**, Adj R² = **0.2963**, F-statistic = **24.52** (p = **1.02e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.4**, BIC = **3391.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9593** | 0.6110 | ±1.2220 | **+37.576** | **5.37e-309** | *** |
| Education: graduate level (vs college) | -0.2603 | 0.1551 | ±0.3102 | -1.678 | 0.0933 | . |
| Education: high school or below (vs college) | +0.0769 | 0.2302 | ±0.4605 | +0.334 | 0.7384 |  |
| Site: UCSD (vs UAB) | +0.0107 | 0.1831 | ±0.3661 | +0.059 | 0.9532 |  |
| **Site: UW (vs UAB)** | **-1.2713** | 0.1749 | ±0.3499 | **-7.267** | **3.69e-13** | *** |
| Season: spring (vs autumn) | -0.2307 | 0.1957 | ±0.3914 | -1.179 | 0.2385 |  |
| **Season: summer (vs autumn)** | **+2.0148** | 0.2218 | ±0.4436 | **+9.083** | **1.05e-19** | *** |
| **Season: winter (vs autumn)** | **-0.9725** | 0.1969 | ±0.3938 | **-4.939** | **7.85e-07** | *** |
| **Age (years)** | **+0.0202** | 0.0075 | ±0.0150 | **+2.689** | **0.0072** | ** |
| BMI (kg/m2) | +0.0179 | 0.0111 | ±0.0221 | +1.617 | 0.1058 |  |
| Hypertension | +0.1317 | 0.1553 | ±0.3107 | +0.848 | 0.3966 |  |
| High cholesterol | +0.0906 | 0.1540 | ±0.3080 | +0.588 | 0.5565 |  |
| Kidney disease | +0.1238 | 0.1961 | ±0.3922 | +0.631 | 0.5280 |  |
| Circulatory disease | +0.1248 | 0.1996 | ±0.3993 | +0.625 | 0.5320 |  |
| Time 181-250, pooled (%) | +0.0033 | 0.0051 | ±0.0102 | +0.643 | 0.5202 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **783**, R² = **0.3088**, Adj R² = **0.2962**, F-statistic = **24.51** (p = **1.07e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.5**, BIC = **3391.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9587** | 0.6109 | ±1.2217 | **+37.583** | **4.02e-309** | *** |
| Education: graduate level (vs college) | -0.2605 | 0.1551 | ±0.3102 | -1.680 | 0.0930 | . |
| Education: high school or below (vs college) | +0.0776 | 0.2305 | ±0.4610 | +0.337 | 0.7363 |  |
| Site: UCSD (vs UAB) | +0.0107 | 0.1831 | ±0.3661 | +0.058 | 0.9535 |  |
| **Site: UW (vs UAB)** | **-1.2710** | 0.1751 | ±0.3502 | **-7.258** | **3.93e-13** | *** |
| Season: spring (vs autumn) | -0.2302 | 0.1958 | ±0.3915 | -1.176 | 0.2396 |  |
| **Season: summer (vs autumn)** | **+2.0151** | 0.2218 | ±0.4436 | **+9.085** | **1.03e-19** | *** |
| **Season: winter (vs autumn)** | **-0.9724** | 0.1970 | ±0.3941 | **-4.935** | **8.01e-07** | *** |
| **Age (years)** | **+0.0203** | 0.0075 | ±0.0150 | **+2.701** | **0.0069** | ** |
| BMI (kg/m2) | +0.0181 | 0.0111 | ±0.0221 | +1.635 | 0.1021 |  |
| Hypertension | +0.1315 | 0.1554 | ±0.3107 | +0.846 | 0.3975 |  |
| High cholesterol | +0.0907 | 0.1541 | ±0.3081 | +0.589 | 0.5562 |  |
| Kidney disease | +0.1248 | 0.1959 | ±0.3919 | +0.637 | 0.5243 |  |
| Circulatory disease | +0.1257 | 0.1997 | ±0.3993 | +0.629 | 0.5291 |  |
| Avg. daily time 181-250 (%) | +0.0028 | 0.0050 | ±0.0100 | +0.566 | 0.5717 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **783**, R² = **0.3092**, Adj R² = **0.2966**, F-statistic = **24.56** (p = **8.59e-53**), Residual SE = **1.998** on **768** df, AIC = **3321.1**, BIC = **3391.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9302** | 0.6104 | ±1.2208 | **+37.567** | **7.57e-309** | *** |
| Education: graduate level (vs college) | -0.2531 | 0.1551 | ±0.3103 | -1.631 | 0.1028 |  |
| Education: high school or below (vs college) | +0.0649 | 0.2316 | ±0.4633 | +0.280 | 0.7794 |  |
| Site: UCSD (vs UAB) | +0.0176 | 0.1840 | ±0.3681 | +0.096 | 0.9239 |  |
| **Site: UW (vs UAB)** | **-1.2615** | 0.1764 | ±0.3529 | **-7.149** | **8.72e-13** | *** |
| Season: spring (vs autumn) | -0.2301 | 0.1956 | ±0.3912 | -1.176 | 0.2394 |  |
| **Season: summer (vs autumn)** | **+2.0243** | 0.2223 | ±0.4446 | **+9.106** | **8.55e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9714** | 0.1964 | ±0.3927 | **-4.947** | **7.54e-07** | *** |
| **Age (years)** | **+0.0206** | 0.0075 | ±0.0149 | **+2.760** | **0.0058** | ** |
| BMI (kg/m2) | +0.0177 | 0.0111 | ±0.0222 | +1.588 | 0.1123 |  |
| Hypertension | +0.1276 | 0.1549 | ±0.3098 | +0.824 | 0.4099 |  |
| High cholesterol | +0.0927 | 0.1540 | ±0.3080 | +0.602 | 0.5474 |  |
| Kidney disease | +0.1196 | 0.1968 | ±0.3936 | +0.608 | 0.5435 |  |
| Circulatory disease | +0.1189 | 0.2007 | ±0.4014 | +0.593 | 0.5534 |  |
| Time > 180 (%) | +0.0026 | 0.0032 | ±0.0063 | +0.823 | 0.4105 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **783**, R² = **0.3091**, Adj R² = **0.2965**, F-statistic = **24.54** (p = **9.29e-53**), Residual SE = **1.999** on **768** df, AIC = **3321.2**, BIC = **3391.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9361** | 0.6105 | ±1.2210 | **+37.570** | **6.66e-309** | *** |
| Education: graduate level (vs college) | -0.2543 | 0.1552 | ±0.3103 | -1.639 | 0.1013 |  |
| Education: high school or below (vs college) | +0.0671 | 0.2318 | ±0.4636 | +0.289 | 0.7723 |  |
| Site: UCSD (vs UAB) | +0.0168 | 0.1841 | ±0.3682 | +0.091 | 0.9274 |  |
| **Site: UW (vs UAB)** | **-1.2628** | 0.1765 | ±0.3530 | **-7.154** | **8.43e-13** | *** |
| Season: spring (vs autumn) | -0.2300 | 0.1956 | ±0.3912 | -1.176 | 0.2396 |  |
| **Season: summer (vs autumn)** | **+2.0230** | 0.2223 | ±0.4445 | **+9.102** | **8.91e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9717** | 0.1965 | ±0.3929 | **-4.946** | **7.59e-07** | *** |
| **Age (years)** | **+0.0206** | 0.0075 | ±0.0149 | **+2.756** | **0.0058** | ** |
| BMI (kg/m2) | +0.0178 | 0.0111 | ±0.0222 | +1.603 | 0.1090 |  |
| Hypertension | +0.1282 | 0.1549 | ±0.3099 | +0.827 | 0.4080 |  |
| High cholesterol | +0.0925 | 0.1541 | ±0.3081 | +0.601 | 0.5481 |  |
| Kidney disease | +0.1205 | 0.1967 | ±0.3934 | +0.613 | 0.5402 |  |
| Circulatory disease | +0.1201 | 0.2007 | ±0.4014 | +0.599 | 0.5495 |  |
| Avg. daily time > 180 (%) | +0.0023 | 0.0032 | ±0.0063 | +0.730 | 0.4655 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **783**, R² = **0.3088**, Adj R² = **0.2962**, F-statistic = **24.51** (p = **1.07e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.5**, BIC = **3391.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9487** | 0.6105 | ±1.2209 | **+37.592** | **2.86e-309** | *** |
| Education: graduate level (vs college) | -0.2519 | 0.1557 | ±0.3114 | -1.618 | 0.1056 |  |
| Education: high school or below (vs college) | +0.0764 | 0.2307 | ±0.4614 | +0.331 | 0.7406 |  |
| Site: UCSD (vs UAB) | +0.0131 | 0.1842 | ±0.3684 | +0.071 | 0.9432 |  |
| **Site: UW (vs UAB)** | **-1.2686** | 0.1763 | ±0.3526 | **-7.195** | **6.25e-13** | *** |
| Season: spring (vs autumn) | -0.2294 | 0.1960 | ±0.3920 | -1.171 | 0.2418 |  |
| **Season: summer (vs autumn)** | **+2.0231** | 0.2223 | ±0.4447 | **+9.099** | **9.08e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9712** | 0.1966 | ±0.3932 | **-4.940** | **7.82e-07** | *** |
| **Age (years)** | **+0.0207** | 0.0075 | ±0.0149 | **+2.779** | **0.0055** | ** |
| BMI (kg/m2) | +0.0180 | 0.0113 | ±0.0226 | +1.591 | 0.1116 |  |
| Hypertension | +0.1300 | 0.1552 | ±0.3104 | +0.837 | 0.4024 |  |
| High cholesterol | +0.0936 | 0.1542 | ±0.3083 | +0.607 | 0.5436 |  |
| Kidney disease | +0.1283 | 0.1964 | ±0.3929 | +0.653 | 0.5137 |  |
| Circulatory disease | +0.1232 | 0.2008 | ±0.4015 | +0.613 | 0.5396 |  |
| Nocturnal time > 180 (%) | +0.0015 | 0.0030 | ±0.0059 | +0.518 | 0.6045 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.3090**, Adj R² = **0.2964**, F-statistic = **24.53** (p = **9.57e-53**), Residual SE = **1.999** on **768** df, AIC = **3321.3**, BIC = **3391.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9226** | 0.6119 | ±1.2239 | **+37.459** | **4.34e-307** | *** |
| Education: graduate level (vs college) | -0.2501 | 0.1554 | ±0.3109 | -1.609 | 0.1076 |  |
| Education: high school or below (vs college) | +0.0708 | 0.2308 | ±0.4617 | +0.307 | 0.7592 |  |
| Site: UCSD (vs UAB) | +0.0143 | 0.1845 | ±0.3689 | +0.077 | 0.9383 |  |
| **Site: UW (vs UAB)** | **-1.2616** | 0.1769 | ±0.3538 | **-7.133** | **9.83e-13** | *** |
| Season: spring (vs autumn) | -0.2251 | 0.1956 | ±0.3912 | -1.151 | 0.2498 |  |
| **Season: summer (vs autumn)** | **+2.0298** | 0.2225 | ±0.4451 | **+9.121** | **7.45e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9675** | 0.1965 | ±0.3931 | **-4.922** | **8.55e-07** | *** |
| **Age (years)** | **+0.0209** | 0.0075 | ±0.0149 | **+2.800** | **0.0051** | ** |
| BMI (kg/m2) | +0.0186 | 0.0110 | ±0.0221 | +1.683 | 0.0923 | . |
| Hypertension | +0.1259 | 0.1547 | ±0.3095 | +0.814 | 0.4159 |  |
| High cholesterol | +0.0950 | 0.1542 | ±0.3084 | +0.616 | 0.5377 |  |
| Kidney disease | +0.1263 | 0.1974 | ±0.3947 | +0.640 | 0.5221 |  |
| Circulatory disease | +0.1204 | 0.2012 | ±0.4024 | +0.599 | 0.5495 |  |
| Time > 250 (%) | +0.0033 | 0.0049 | ±0.0098 | +0.673 | 0.5008 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 783)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **783**, R² = **0.3089**, Adj R² = **0.2963**, F-statistic = **24.52** (p = **1.01e-52**), Residual SE = **1.999** on **768** df, AIC = **3321.4**, BIC = **3391.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9298** | 0.6116 | ±1.2233 | **+37.489** | **1.40e-307** | *** |
| Education: graduate level (vs college) | -0.2510 | 0.1555 | ±0.3110 | -1.615 | 0.1064 |  |
| Education: high school or below (vs college) | +0.0726 | 0.2308 | ±0.4616 | +0.314 | 0.7532 |  |
| Site: UCSD (vs UAB) | +0.0134 | 0.1845 | ±0.3690 | +0.073 | 0.9419 |  |
| **Site: UW (vs UAB)** | **-1.2633** | 0.1768 | ±0.3536 | **-7.145** | **8.98e-13** | *** |
| Season: spring (vs autumn) | -0.2254 | 0.1956 | ±0.3911 | -1.153 | 0.2491 |  |
| **Season: summer (vs autumn)** | **+2.0281** | 0.2226 | ±0.4452 | **+9.112** | **8.10e-20** | *** |
| **Season: winter (vs autumn)** | **-0.9678** | 0.1966 | ±0.3931 | **-4.924** | **8.50e-07** | *** |
| **Age (years)** | **+0.0208** | 0.0075 | ±0.0149 | **+2.791** | **0.0053** | ** |
| BMI (kg/m2) | +0.0187 | 0.0111 | ±0.0221 | +1.687 | 0.0917 | . |
| Hypertension | +0.1267 | 0.1548 | ±0.3096 | +0.818 | 0.4131 |  |
| High cholesterol | +0.0949 | 0.1542 | ±0.3084 | +0.615 | 0.5385 |  |
| Kidney disease | +0.1264 | 0.1974 | ±0.3947 | +0.641 | 0.5218 |  |
| Circulatory disease | +0.1209 | 0.2013 | ±0.4026 | +0.601 | 0.5482 |  |
| Avg. daily time > 250 (%) | +0.0030 | 0.0050 | ±0.0100 | +0.602 | 0.5471 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 783; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **783**, R² = **0.2429**, Adj R² = **0.2301**, F-statistic = **18.98** (p = **8.92e-39**), Residual SE = **6.017** on **769** df, AIC = **5046.3**, BIC = **5111.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4585** | 1.8993 | ±3.7986 | **+26.040** | **1.74e-149** | *** |
| Education: graduate level (vs college) | +0.0099 | 0.4910 | ±0.9820 | +0.020 | 0.9839 |  |
| Education: high school or below (vs college) | +0.4064 | 0.6358 | ±1.2716 | +0.639 | 0.5227 |  |
| **Site: UCSD (vs UAB)** | **+3.0471** | 0.5694 | ±1.1389 | **+5.351** | **8.75e-08** | *** |
| Site: UW (vs UAB) | -0.8284 | 0.5206 | ±1.0411 | -1.591 | 0.1115 |  |
| **Season: spring (vs autumn)** | **-2.1310** | 0.6165 | ±1.2330 | **-3.457** | **5.47e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8428** | 0.6165 | ±1.2330 | **+2.989** | **0.0028** | ** |
| **Season: winter (vs autumn)** | **-5.6420** | 0.6626 | ±1.3252 | **-8.515** | **1.66e-17** | *** |
| **Age (years)** | **-0.0425** | 0.0216 | ±0.0433 | **-1.962** | **0.0497** | * |
| BMI (kg/m2) | -0.0262 | 0.0330 | ±0.0660 | -0.796 | 0.4262 |  |
| Hypertension | -0.7613 | 0.4995 | ±0.9989 | -1.524 | 0.1275 |  |
| High cholesterol | -0.5099 | 0.4593 | ±0.9186 | -1.110 | 0.2669 |  |
| Kidney disease | +1.1047 | 0.6056 | ±1.2113 | +1.824 | 0.0681 | . |
| Circulatory disease | +0.1813 | 0.5828 | ±1.1656 | +0.311 | 0.7557 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **783**, R² = **0.2439**, Adj R² = **0.2301**, F-statistic = **17.69** (p = **2.51e-38**), Residual SE = **6.017** on **768** df, AIC = **5047.3**, BIC = **5117.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4693** | 2.1405 | ±4.2809 | **+22.644** | **1.59e-113** | *** |
| Education: graduate level (vs college) | +0.0420 | 0.4911 | ±0.9823 | +0.086 | 0.9318 |  |
| Education: high school or below (vs college) | +0.3156 | 0.6363 | ±1.2725 | +0.496 | 0.6199 |  |
| **Site: UCSD (vs UAB)** | **+3.0784** | 0.5725 | ±1.1450 | **+5.377** | **7.57e-08** | *** |
| Site: UW (vs UAB) | -0.7851 | 0.5241 | ±1.0481 | -1.498 | 0.1341 |  |
| **Season: spring (vs autumn)** | **-2.1137** | 0.6173 | ±1.2346 | **-3.424** | **6.17e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8657** | 0.6168 | ±1.2336 | **+3.025** | **0.0025** | ** |
| **Season: winter (vs autumn)** | **-5.6399** | 0.6632 | ±1.3264 | **-8.504** | **1.84e-17** | *** |
| Age (years) | -0.0421 | 0.0217 | ±0.0433 | -1.943 | 0.0520 | . |
| BMI (kg/m2) | -0.0314 | 0.0334 | ±0.0668 | -0.940 | 0.3472 |  |
| Hypertension | -0.7840 | 0.4984 | ±0.9969 | -1.573 | 0.1157 |  |
| High cholesterol | -0.5284 | 0.4611 | ±0.9223 | -1.146 | 0.2519 |  |
| Kidney disease | +1.0983 | 0.6044 | ±1.2087 | +1.817 | 0.0692 | . |
| Circulatory disease | +0.1459 | 0.5845 | ±1.1691 | +0.250 | 0.8029 |  |
| HbA1c (%) | +0.1649 | 0.1672 | ±0.3343 | +0.986 | 0.3241 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **783**, R² = **0.2449**, Adj R² = **0.2311**, F-statistic = **17.79** (p = **1.51e-38**), Residual SE = **6.013** on **768** df, AIC = **5046.2**, BIC = **5116.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.3164** | 2.0322 | ±4.0643 | **+23.776** | **5.92e-125** | *** |
| Education: graduate level (vs college) | +0.0393 | 0.4908 | ±0.9817 | +0.080 | 0.9362 |  |
| Education: high school or below (vs college) | +0.2855 | 0.6371 | ±1.2742 | +0.448 | 0.6541 |  |
| **Site: UCSD (vs UAB)** | **+3.1076** | 0.5748 | ±1.1497 | **+5.406** | **6.45e-08** | *** |
| Site: UW (vs UAB) | -0.7686 | 0.5246 | ±1.0492 | -1.465 | 0.1429 |  |
| **Season: spring (vs autumn)** | **-2.1586** | 0.6159 | ±1.2318 | **-3.505** | **4.57e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8838** | 0.6161 | ±1.2322 | **+3.058** | **0.0022** | ** |
| **Season: winter (vs autumn)** | **-5.6491** | 0.6622 | ±1.3244 | **-8.531** | **1.45e-17** | *** |
| Age (years) | -0.0416 | 0.0216 | ±0.0433 | -1.922 | 0.0546 | . |
| BMI (kg/m2) | -0.0328 | 0.0335 | ±0.0669 | -0.982 | 0.3263 |  |
| Hypertension | -0.7847 | 0.4991 | ±0.9983 | -1.572 | 0.1159 |  |
| High cholesterol | -0.5213 | 0.4599 | ±0.9198 | -1.134 | 0.2570 |  |
| Kidney disease | +1.0553 | 0.6037 | ±1.2073 | +1.748 | 0.0804 | . |
| Circulatory disease | +0.1260 | 0.5861 | ±1.1723 | +0.215 | 0.8298 |  |
| Mean glucose (mg/dL) | +0.0080 | 0.0058 | ±0.0115 | +1.388 | 0.1651 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **783**, R² = **0.2449**, Adj R² = **0.2311**, F-statistic = **17.79** (p = **1.51e-38**), Residual SE = **6.013** on **768** df, AIC = **5046.2**, BIC = **5116.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.2114** | 2.4356 | ±4.8711 | **+19.384** | **1.05e-83** | *** |
| Education: graduate level (vs college) | +0.0393 | 0.4908 | ±0.9817 | +0.080 | 0.9362 |  |
| Education: high school or below (vs college) | +0.2855 | 0.6371 | ±1.2742 | +0.448 | 0.6541 |  |
| **Site: UCSD (vs UAB)** | **+3.1076** | 0.5748 | ±1.1497 | **+5.406** | **6.45e-08** | *** |
| Site: UW (vs UAB) | -0.7686 | 0.5246 | ±1.0492 | -1.465 | 0.1429 |  |
| **Season: spring (vs autumn)** | **-2.1586** | 0.6159 | ±1.2318 | **-3.505** | **4.57e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8838** | 0.6161 | ±1.2322 | **+3.058** | **0.0022** | ** |
| **Season: winter (vs autumn)** | **-5.6491** | 0.6622 | ±1.3244 | **-8.531** | **1.45e-17** | *** |
| Age (years) | -0.0416 | 0.0216 | ±0.0433 | -1.922 | 0.0546 | . |
| BMI (kg/m2) | -0.0328 | 0.0335 | ±0.0669 | -0.982 | 0.3263 |  |
| Hypertension | -0.7847 | 0.4991 | ±0.9983 | -1.572 | 0.1159 |  |
| High cholesterol | -0.5213 | 0.4599 | ±0.9198 | -1.134 | 0.2570 |  |
| Kidney disease | +1.0553 | 0.6037 | ±1.2073 | +1.748 | 0.0804 | . |
| Circulatory disease | +0.1260 | 0.5861 | ±1.1723 | +0.215 | 0.8298 |  |
| GMI (%) | +0.3339 | 0.2405 | ±0.4810 | +1.388 | 0.1651 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **783**, R² = **0.2441**, Adj R² = **0.2303**, F-statistic = **17.72** (p = **2.21e-38**), Residual SE = **6.016** on **768** df, AIC = **5047.1**, BIC = **5117.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.6438** | 2.0036 | ±4.0072 | **+24.278** | **3.35e-130** | *** |
| Education: graduate level (vs college) | +0.0424 | 0.4916 | ±0.9833 | +0.086 | 0.9312 |  |
| Education: high school or below (vs college) | +0.3227 | 0.6377 | ±1.2753 | +0.506 | 0.6129 |  |
| **Site: UCSD (vs UAB)** | **+3.0912** | 0.5744 | ±1.1488 | **+5.381** | **7.39e-08** | *** |
| Site: UW (vs UAB) | -0.7972 | 0.5230 | ±1.0460 | -1.524 | 0.1274 |  |
| **Season: spring (vs autumn)** | **-2.1634** | 0.6165 | ±1.2330 | **-3.509** | **4.50e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8762** | 0.6164 | ±1.2327 | **+3.044** | **0.0023** | ** |
| **Season: winter (vs autumn)** | **-5.6542** | 0.6630 | ±1.3261 | **-8.528** | **1.49e-17** | *** |
| Age (years) | -0.0409 | 0.0216 | ±0.0433 | -1.889 | 0.0589 | . |
| BMI (kg/m2) | -0.0327 | 0.0337 | ±0.0673 | -0.971 | 0.3317 |  |
| Hypertension | -0.7737 | 0.4992 | ±0.9984 | -1.550 | 0.1212 |  |
| High cholesterol | -0.5170 | 0.4600 | ±0.9200 | -1.124 | 0.2611 |  |
| Kidney disease | +1.0912 | 0.6046 | ±1.2092 | +1.805 | 0.0711 | . |
| Circulatory disease | +0.1420 | 0.5859 | ±1.1717 | +0.242 | 0.8084 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0059 | 0.0053 | ±0.0106 | +1.115 | 0.2648 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **783**, R² = **0.2431**, Adj R² = **0.2293**, F-statistic = **17.62** (p = **3.54e-38**), Residual SE = **6.020** on **768** df, AIC = **5048.1**, BIC = **5118.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1710** | 2.0304 | ±4.0607 | **+24.218** | **1.44e-129** | *** |
| Education: graduate level (vs college) | +0.0260 | 0.4956 | ±0.9911 | +0.053 | 0.9581 |  |
| Education: high school or below (vs college) | +0.3734 | 0.6313 | ±1.2627 | +0.591 | 0.5543 |  |
| **Site: UCSD (vs UAB)** | **+3.0680** | 0.5750 | ±1.1500 | **+5.336** | **9.51e-08** | *** |
| Site: UW (vs UAB) | -0.7940 | 0.5300 | ±1.0601 | -1.498 | 0.1341 |  |
| **Season: spring (vs autumn)** | **-2.1416** | 0.6160 | ±1.2320 | **-3.477** | **5.08e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8536** | 0.6183 | ±1.2365 | **+2.998** | **0.0027** | ** |
| **Season: winter (vs autumn)** | **-5.6452** | 0.6623 | ±1.3246 | **-8.524** | **1.55e-17** | *** |
| **Age (years)** | **-0.0426** | 0.0217 | ±0.0434 | **-1.966** | **0.0493** | * |
| BMI (kg/m2) | -0.0283 | 0.0332 | ±0.0664 | -0.852 | 0.3944 |  |
| Hypertension | -0.7753 | 0.4984 | ±0.9969 | -1.556 | 0.1198 |  |
| High cholesterol | -0.5045 | 0.4594 | ±0.9189 | -1.098 | 0.2722 |  |
| Kidney disease | +1.0466 | 0.6141 | ±1.2282 | +1.704 | 0.0883 | . |
| Circulatory disease | +0.1653 | 0.5860 | ±1.1719 | +0.282 | 0.7779 |  |
| Glucose SD, pooled (mg/dL) | +0.0093 | 0.0186 | ±0.0372 | +0.502 | 0.6158 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **783**, R² = **0.2435**, Adj R² = **0.2297**, F-statistic = **17.66** (p = **3.00e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.7**, BIC = **5117.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.9920** | 2.0270 | ±4.0541 | **+24.169** | **4.69e-129** | *** |
| Education: graduate level (vs college) | +0.0296 | 0.4949 | ±0.9897 | +0.060 | 0.9524 |  |
| Education: high school or below (vs college) | +0.3497 | 0.6321 | ±1.2641 | +0.553 | 0.5801 |  |
| **Site: UCSD (vs UAB)** | **+3.0803** | 0.5754 | ±1.1509 | **+5.353** | **8.66e-08** | *** |
| Site: UW (vs UAB) | -0.7792 | 0.5293 | ±1.0586 | -1.472 | 0.1410 |  |
| **Season: spring (vs autumn)** | **-2.1468** | 0.6162 | ±1.2324 | **-3.484** | **4.94e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8615** | 0.6187 | ±1.2375 | **+3.009** | **0.0026** | ** |
| **Season: winter (vs autumn)** | **-5.6404** | 0.6623 | ±1.3246 | **-8.516** | **1.65e-17** | *** |
| **Age (years)** | **-0.0429** | 0.0217 | ±0.0434 | **-1.977** | **0.0480** | * |
| BMI (kg/m2) | -0.0287 | 0.0332 | ±0.0665 | -0.863 | 0.3884 |  |
| Hypertension | -0.7803 | 0.4981 | ±0.9961 | -1.567 | 0.1172 |  |
| High cholesterol | -0.5025 | 0.4594 | ±0.9188 | -1.094 | 0.2741 |  |
| Kidney disease | +1.0086 | 0.6147 | ±1.2294 | +1.641 | 0.1008 |  |
| Circulatory disease | +0.1603 | 0.5863 | ±1.1725 | +0.273 | 0.7845 |  |
| Avg. daily SD (mg/dL) | +0.0165 | 0.0211 | ±0.0423 | +0.780 | 0.4351 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **783**, R² = **0.2434**, Adj R² = **0.2296**, F-statistic = **17.64** (p = **3.18e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.8**, BIC = **5117.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0631** | 2.1811 | ±4.3623 | **+22.953** | **1.38e-116** | *** |
| Education: graduate level (vs college) | -0.0074 | 0.4955 | ±0.9910 | -0.015 | 0.9881 |  |
| Education: high school or below (vs college) | +0.4117 | 0.6348 | ±1.2695 | +0.649 | 0.5167 |  |
| **Site: UCSD (vs UAB)** | **+3.0299** | 0.5714 | ±1.1428 | **+5.302** | **1.14e-07** | *** |
| Site: UW (vs UAB) | -0.8669 | 0.5253 | ±1.0506 | -1.650 | 0.0989 | . |
| **Season: spring (vs autumn)** | **-2.1300** | 0.6171 | ±1.2342 | **-3.452** | **5.57e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8410** | 0.6165 | ±1.2330 | **+2.986** | **0.0028** | ** |
| **Season: winter (vs autumn)** | **-5.6414** | 0.6641 | ±1.3283 | **-8.494** | **1.99e-17** | *** |
| Age (years) | -0.0417 | 0.0216 | ±0.0432 | -1.930 | 0.0537 | . |
| BMI (kg/m2) | -0.0256 | 0.0329 | ±0.0658 | -0.778 | 0.4365 |  |
| Hypertension | -0.7446 | 0.4984 | ±0.9968 | -1.494 | 0.1352 |  |
| High cholesterol | -0.5292 | 0.4592 | ±0.9184 | -1.153 | 0.2491 |  |
| Kidney disease | +1.1861 | 0.6167 | ±1.2333 | +1.923 | 0.0544 | . |
| Circulatory disease | +0.1846 | 0.5827 | ±1.1653 | +0.317 | 0.7513 |  |
| CV (%) | -0.0278 | 0.0410 | ±0.0819 | -0.678 | 0.4975 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **783**, R² = **0.2436**, Adj R² = **0.2298**, F-statistic = **17.67** (p = **2.81e-38**), Residual SE = **6.018** on **768** df, AIC = **5047.6**, BIC = **5117.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5594** | 2.0782 | ±4.1563 | **+23.367** | **9.36e-121** | *** |
| Education: graduate level (vs college) | -0.0069 | 0.4947 | ±0.9894 | -0.014 | 0.9889 |  |
| Education: high school or below (vs college) | +0.4117 | 0.6347 | ±1.2695 | +0.649 | 0.5166 |  |
| **Site: UCSD (vs UAB)** | **+3.0368** | 0.5703 | ±1.1406 | **+5.325** | **1.01e-07** | *** |
| Site: UW (vs UAB) | -0.8684 | 0.5238 | ±1.0476 | -1.658 | 0.0973 | . |
| **Season: spring (vs autumn)** | **-2.1224** | 0.6166 | ±1.2332 | **-3.442** | **5.77e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8611** | 0.6151 | ±1.2302 | **+3.026** | **0.0025** | ** |
| **Season: winter (vs autumn)** | **-5.6300** | 0.6633 | ±1.3266 | **-8.487** | **2.11e-17** | *** |
| Age (years) | -0.0418 | 0.0216 | ±0.0433 | -1.930 | 0.0536 | . |
| BMI (kg/m2) | -0.0259 | 0.0329 | ±0.0658 | -0.789 | 0.4302 |  |
| Hypertension | -0.7412 | 0.4984 | ±0.9967 | -1.487 | 0.1370 |  |
| High cholesterol | -0.5225 | 0.4589 | ±0.9177 | -1.139 | 0.2548 |  |
| Kidney disease | +1.1890 | 0.6107 | ±1.2215 | +1.947 | 0.0516 | . |
| Circulatory disease | +0.1934 | 0.5826 | ±1.1652 | +0.332 | 0.7399 |  |
| Mean / SD ratio | +0.1895 | 0.2212 | ±0.4424 | +0.857 | 0.3917 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **783**, R² = **0.2430**, Adj R² = **0.2292**, F-statistic = **17.61** (p = **3.82e-38**), Residual SE = **6.021** on **768** df, AIC = **5048.2**, BIC = **5118.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1703** | 2.0741 | ±4.1482 | **+23.707** | **3.09e-124** | *** |
| Education: graduate level (vs college) | +0.0057 | 0.4943 | ±0.9886 | +0.011 | 0.9908 |  |
| Education: high school or below (vs college) | +0.4092 | 0.6357 | ±1.2714 | +0.644 | 0.5198 |  |
| **Site: UCSD (vs UAB)** | **+3.0443** | 0.5702 | ±1.1404 | **+5.339** | **9.35e-08** | *** |
| Site: UW (vs UAB) | -0.8404 | 0.5236 | ±1.0472 | -1.605 | 0.1085 |  |
| **Season: spring (vs autumn)** | **-2.1325** | 0.6177 | ±1.2354 | **-3.452** | **5.56e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8465** | 0.6160 | ±1.2321 | **+2.997** | **0.0027** | ** |
| **Season: winter (vs autumn)** | **-5.6415** | 0.6637 | ±1.3274 | **-8.500** | **1.90e-17** | *** |
| Age (years) | -0.0421 | 0.0217 | ±0.0434 | -1.941 | 0.0523 | . |
| BMI (kg/m2) | -0.0264 | 0.0330 | ±0.0660 | -0.801 | 0.4234 |  |
| Hypertension | -0.7549 | 0.4983 | ±0.9966 | -1.515 | 0.1298 |  |
| High cholesterol | -0.5152 | 0.4588 | ±0.9177 | -1.123 | 0.2615 |  |
| Kidney disease | +1.1322 | 0.6099 | ±1.2199 | +1.856 | 0.0634 | . |
| Circulatory disease | +0.1824 | 0.5832 | ±1.1664 | +0.313 | 0.7545 |  |
| Avg. daily mean/SD | +0.0523 | 0.1812 | ±0.3624 | +0.289 | 0.7727 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **783**, R² = **0.2432**, Adj R² = **0.2294**, F-statistic = **17.63** (p = **3.44e-38**), Residual SE = **6.020** on **768** df, AIC = **5048.0**, BIC = **5118.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.7950** | 2.2118 | ±4.4237 | **+22.061** | **7.50e-108** | *** |
| Education: graduate level (vs college) | +0.0334 | 0.4974 | ±0.9948 | +0.067 | 0.9464 |  |
| Education: high school or below (vs college) | +0.3943 | 0.6354 | ±1.2708 | +0.621 | 0.5349 |  |
| **Site: UCSD (vs UAB)** | **+3.0728** | 0.5763 | ±1.1525 | **+5.332** | **9.70e-08** | *** |
| Site: UW (vs UAB) | -0.7768 | 0.5330 | ±1.0660 | -1.457 | 0.1450 |  |
| **Season: spring (vs autumn)** | **-2.1349** | 0.6174 | ±1.2348 | **-3.458** | **5.44e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8707** | 0.6182 | ±1.2364 | **+3.026** | **0.0025** | ** |
| **Season: winter (vs autumn)** | **-5.6320** | 0.6639 | ±1.3279 | **-8.483** | **2.20e-17** | *** |
| Age (years) | -0.0415 | 0.0216 | ±0.0433 | -1.917 | 0.0552 | . |
| BMI (kg/m2) | -0.0273 | 0.0331 | ±0.0661 | -0.824 | 0.4098 |  |
| Hypertension | -0.7535 | 0.5007 | ±1.0014 | -1.505 | 0.1324 |  |
| High cholesterol | -0.4906 | 0.4601 | ±0.9202 | -1.066 | 0.2863 |  |
| Kidney disease | +1.0766 | 0.6076 | ±1.2152 | +1.772 | 0.0764 | . |
| Circulatory disease | +0.1747 | 0.5830 | ±1.1659 | +0.300 | 0.7644 |  |
| MAG (mg/dL/h) | +0.0128 | 0.0222 | ±0.0444 | +0.576 | 0.5645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **783**, R² = **0.2434**, Adj R² = **0.2296**, F-statistic = **17.65** (p = **3.08e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.8**, BIC = **5117.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.7799** | 2.1539 | ±4.3078 | **+22.647** | **1.48e-113** | *** |
| Education: graduate level (vs college) | +0.0284 | 0.4955 | ±0.9909 | +0.057 | 0.9542 |  |
| Education: high school or below (vs college) | +0.3541 | 0.6326 | ±1.2653 | +0.560 | 0.5757 |  |
| **Site: UCSD (vs UAB)** | **+3.0843** | 0.5768 | ±1.1537 | **+5.347** | **8.94e-08** | *** |
| Site: UW (vs UAB) | -0.7781 | 0.5310 | ±1.0620 | -1.465 | 0.1428 |  |
| **Season: spring (vs autumn)** | **-2.1523** | 0.6153 | ±1.2306 | **-3.498** | **4.69e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8504** | 0.6172 | ±1.2345 | **+2.998** | **0.0027** | ** |
| **Season: winter (vs autumn)** | **-5.6448** | 0.6619 | ±1.3237 | **-8.529** | **1.48e-17** | *** |
| Age (years) | -0.0422 | 0.0217 | ±0.0434 | -1.946 | 0.0517 | . |
| BMI (kg/m2) | -0.0279 | 0.0331 | ±0.0663 | -0.840 | 0.4007 |  |
| Hypertension | -0.7682 | 0.4988 | ±0.9976 | -1.540 | 0.1235 |  |
| High cholesterol | -0.5000 | 0.4594 | ±0.9187 | -1.089 | 0.2764 |  |
| Kidney disease | +1.0155 | 0.6134 | ±1.2268 | +1.656 | 0.0978 | . |
| Circulatory disease | +0.1597 | 0.5852 | ±1.1704 | +0.273 | 0.7849 |  |
| Avg. daily range (mg/dL) | +0.0046 | 0.0061 | ±0.0122 | +0.760 | 0.4470 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **783**, R² = **0.2429**, Adj R² = **0.2291**, F-statistic = **17.60** (p = **3.97e-38**), Residual SE = **6.021** on **768** df, AIC = **5048.3**, BIC = **5118.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4749** | 1.9356 | ±3.8711 | **+25.561** | **4.13e-144** | *** |
| Education: graduate level (vs college) | +0.0069 | 0.4956 | ±0.9912 | +0.014 | 0.9889 |  |
| Education: high school or below (vs college) | +0.4081 | 0.6350 | ±1.2700 | +0.643 | 0.5204 |  |
| **Site: UCSD (vs UAB)** | **+3.0454** | 0.5722 | ±1.1443 | **+5.323** | **1.02e-07** | *** |
| Site: UW (vs UAB) | -0.8317 | 0.5249 | ±1.0498 | -1.585 | 0.1131 |  |
| **Season: spring (vs autumn)** | **-2.1300** | 0.6167 | ±1.2334 | **-3.454** | **5.53e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8427** | 0.6172 | ±1.2343 | **+2.986** | **0.0028** | ** |
| **Season: winter (vs autumn)** | **-5.6403** | 0.6648 | ±1.3296 | **-8.484** | **2.18e-17** | *** |
| Age (years) | -0.0425 | 0.0217 | ±0.0434 | -1.960 | 0.0500 | . |
| BMI (kg/m2) | -0.0260 | 0.0330 | ±0.0661 | -0.785 | 0.4323 |  |
| Hypertension | -0.7592 | 0.5012 | ±1.0023 | -1.515 | 0.1298 |  |
| High cholesterol | -0.5102 | 0.4597 | ±0.9195 | -1.110 | 0.2671 |  |
| Kidney disease | +1.1077 | 0.6071 | ±1.2142 | +1.825 | 0.0681 | . |
| Circulatory disease | +0.1841 | 0.5873 | ±1.1745 | +0.314 | 0.7538 |  |
| SD of daily means (mg/dL) | -0.0017 | 0.0273 | ±0.0547 | -0.062 | 0.9509 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **783**, R² = **0.2435**, Adj R² = **0.2297**, F-statistic = **17.66** (p = **2.99e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.7**, BIC = **5117.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0676** | 2.1045 | ±4.2091 | **+23.790** | **4.20e-125** | *** |
| Education: graduate level (vs college) | +0.0264 | 0.4917 | ±0.9834 | +0.054 | 0.9571 |  |
| Education: high school or below (vs college) | +0.3431 | 0.6360 | ±1.2720 | +0.539 | 0.5895 |  |
| **Site: UCSD (vs UAB)** | **+3.0861** | 0.5761 | ±1.1522 | **+5.357** | **8.47e-08** | *** |
| Site: UW (vs UAB) | -0.7895 | 0.5258 | ±1.0517 | -1.501 | 0.1333 |  |
| **Season: spring (vs autumn)** | **-2.1458** | 0.6161 | ±1.2322 | **-3.483** | **4.96e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8594** | 0.6170 | ±1.2340 | **+3.014** | **0.0026** | ** |
| **Season: winter (vs autumn)** | **-5.6519** | 0.6632 | ±1.3265 | **-8.522** | **1.57e-17** | *** |
| Age (years) | -0.0423 | 0.0217 | ±0.0433 | -1.955 | 0.0506 | . |
| BMI (kg/m2) | -0.0305 | 0.0337 | ±0.0675 | -0.903 | 0.3664 |  |
| Hypertension | -0.7701 | 0.4997 | ±0.9995 | -1.541 | 0.1233 |  |
| High cholesterol | -0.5083 | 0.4597 | ±0.9195 | -1.106 | 0.2689 |  |
| Kidney disease | +1.0647 | 0.6067 | ±1.2133 | +1.755 | 0.0793 | . |
| Circulatory disease | +0.1559 | 0.5855 | ±1.1710 | +0.266 | 0.7901 |  |
| Time in range 70-180, pooled (%) | -0.0069 | 0.0095 | ±0.0190 | -0.730 | 0.4652 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **783**, R² = **0.2436**, Adj R² = **0.2298**, F-statistic = **17.66** (p = **2.89e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.6**, BIC = **5117.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1100** | 2.1073 | ±4.2146 | **+23.779** | **5.44e-125** | *** |
| Education: graduate level (vs college) | +0.0257 | 0.4917 | ±0.9833 | +0.052 | 0.9583 |  |
| Education: high school or below (vs college) | +0.3378 | 0.6359 | ±1.2719 | +0.531 | 0.5953 |  |
| **Site: UCSD (vs UAB)** | **+3.0907** | 0.5766 | ±1.1532 | **+5.360** | **8.32e-08** | *** |
| Site: UW (vs UAB) | -0.7864 | 0.5260 | ±1.0519 | -1.495 | 0.1349 |  |
| **Season: spring (vs autumn)** | **-2.1483** | 0.6161 | ±1.2322 | **-3.487** | **4.88e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8583** | 0.6169 | ±1.2337 | **+3.013** | **0.0026** | ** |
| **Season: winter (vs autumn)** | **-5.6548** | 0.6633 | ±1.3266 | **-8.525** | **1.53e-17** | *** |
| Age (years) | -0.0424 | 0.0217 | ±0.0433 | -1.957 | 0.0504 | . |
| BMI (kg/m2) | -0.0308 | 0.0337 | ±0.0675 | -0.913 | 0.3614 |  |
| Hypertension | -0.7701 | 0.4997 | ±0.9993 | -1.541 | 0.1233 |  |
| High cholesterol | -0.5086 | 0.4598 | ±0.9195 | -1.106 | 0.2687 |  |
| Kidney disease | +1.0598 | 0.6067 | ±1.2133 | +1.747 | 0.0806 | . |
| Circulatory disease | +0.1547 | 0.5857 | ±1.1713 | +0.264 | 0.7917 |  |
| Avg. daily time in range 70-180 (%) | -0.0073 | 0.0094 | ±0.0188 | -0.776 | 0.4378 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.2429**, Adj R² = **0.2291**, F-statistic = **17.60** (p = **3.97e-38**), Residual SE = **6.021** on **768** df, AIC = **5048.3**, BIC = **5118.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4472** | 1.9138 | ±3.8277 | **+25.837** | **3.44e-147** | *** |
| Education: graduate level (vs college) | +0.0108 | 0.4922 | ±0.9845 | +0.022 | 0.9826 |  |
| Education: high school or below (vs college) | +0.4081 | 0.6378 | ±1.2757 | +0.640 | 0.5223 |  |
| **Site: UCSD (vs UAB)** | **+3.0486** | 0.5708 | ±1.1417 | **+5.341** | **9.27e-08** | *** |
| Site: UW (vs UAB) | -0.8268 | 0.5205 | ±1.0411 | -1.588 | 0.1122 |  |
| **Season: spring (vs autumn)** | **-2.1307** | 0.6177 | ±1.2355 | **-3.449** | **5.62e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8440** | 0.6176 | ±1.2351 | **+2.986** | **0.0028** | ** |
| **Season: winter (vs autumn)** | **-5.6400** | 0.6637 | ±1.3273 | **-8.498** | **1.92e-17** | *** |
| Age (years) | -0.0424 | 0.0217 | ±0.0433 | -1.959 | 0.0502 | . |
| BMI (kg/m2) | -0.0263 | 0.0330 | ±0.0660 | -0.796 | 0.4262 |  |
| Hypertension | -0.7628 | 0.5023 | ±1.0046 | -1.519 | 0.1289 |  |
| High cholesterol | -0.5077 | 0.4607 | ±0.9215 | -1.102 | 0.2705 |  |
| Kidney disease | +1.1040 | 0.6062 | ±1.2124 | +1.821 | 0.0686 | . |
| Circulatory disease | +0.1799 | 0.5841 | ±1.1683 | +0.308 | 0.7580 |  |
| Any reading < 54 during wear (0/1) | +0.0288 | 0.5209 | ±1.0418 | +0.055 | 0.9560 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.2446**, Adj R² = **0.2309**, F-statistic = **17.77** (p = **1.73e-38**), Residual SE = **6.014** on **768** df, AIC = **5046.5**, BIC = **5116.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.6056** | 1.8997 | ±3.7994 | **+26.112** | **2.66e-150** | *** |
| Education: graduate level (vs college) | -0.0262 | 0.4916 | ±0.9831 | -0.053 | 0.9576 |  |
| Education: high school or below (vs college) | +0.3606 | 0.6365 | ±1.2729 | +0.567 | 0.5710 |  |
| **Site: UCSD (vs UAB)** | **+2.9958** | 0.5698 | ±1.1396 | **+5.258** | **1.46e-07** | *** |
| Site: UW (vs UAB) | -0.8934 | 0.5211 | ±1.0423 | -1.714 | 0.0865 | . |
| **Season: spring (vs autumn)** | **-2.1498** | 0.6165 | ±1.2330 | **-3.487** | **4.88e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8174** | 0.6159 | ±1.2317 | **+2.951** | **0.0032** | ** |
| **Season: winter (vs autumn)** | **-5.6218** | 0.6629 | ±1.3258 | **-8.481** | **2.24e-17** | *** |
| Age (years) | -0.0414 | 0.0216 | ±0.0433 | -1.916 | 0.0554 | . |
| BMI (kg/m2) | -0.0285 | 0.0330 | ±0.0659 | -0.866 | 0.3865 |  |
| Hypertension | -0.7592 | 0.4993 | ±0.9987 | -1.520 | 0.1284 |  |
| High cholesterol | -0.5599 | 0.4602 | ±0.9203 | -1.217 | 0.2237 |  |
| Kidney disease | +1.1000 | 0.6061 | ±1.2122 | +1.815 | 0.0695 | . |
| Circulatory disease | +0.1588 | 0.5825 | ±1.1650 | +0.273 | 0.7852 |  |
| **Time < 54 (%)** | **-0.5042** | 0.2501 | ±0.5003 | **-2.016** | **0.0439** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.2441**, Adj R² = **0.2303**, F-statistic = **17.72** (p = **2.23e-38**), Residual SE = **6.016** on **768** df, AIC = **5047.1**, BIC = **5117.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5684** | 1.9008 | ±3.8015 | **+26.078** | **6.46e-150** | *** |
| Education: graduate level (vs college) | -0.0165 | 0.4916 | ±0.9833 | -0.033 | 0.9733 |  |
| Education: high school or below (vs college) | +0.3663 | 0.6367 | ±1.2735 | +0.575 | 0.5651 |  |
| **Site: UCSD (vs UAB)** | **+3.0033** | 0.5697 | ±1.1393 | **+5.272** | **1.35e-07** | *** |
| Site: UW (vs UAB) | -0.8887 | 0.5219 | ±1.0438 | -1.703 | 0.0886 | . |
| **Season: spring (vs autumn)** | **-2.1640** | 0.6171 | ±1.2342 | **-3.507** | **4.54e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8046** | 0.6174 | ±1.2347 | **+2.923** | **0.0035** | ** |
| **Season: winter (vs autumn)** | **-5.6350** | 0.6638 | ±1.3276 | **-8.489** | **2.09e-17** | *** |
| Age (years) | -0.0417 | 0.0216 | ±0.0433 | -1.926 | 0.0541 | . |
| BMI (kg/m2) | -0.0274 | 0.0329 | ±0.0659 | -0.831 | 0.4061 |  |
| Hypertension | -0.7563 | 0.4998 | ±0.9995 | -1.513 | 0.1302 |  |
| High cholesterol | -0.5575 | 0.4609 | ±0.9217 | -1.210 | 0.2264 |  |
| Kidney disease | +1.1111 | 0.6063 | ±1.2126 | +1.833 | 0.0669 | . |
| Circulatory disease | +0.1643 | 0.5822 | ±1.1645 | +0.282 | 0.7778 |  |
| Avg. daily time < 54 (%) | -0.4854 | 0.4767 | ±0.9534 | -1.018 | 0.3085 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.2429**, Adj R² = **0.2291**, F-statistic = **17.60** (p = **3.97e-38**), Residual SE = **6.021** on **768** df, AIC = **5048.3**, BIC = **5118.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4642** | 1.9045 | ±3.8089 | **+25.973** | **1.01e-148** | *** |
| Education: graduate level (vs college) | +0.0083 | 0.4920 | ±0.9840 | +0.017 | 0.9865 |  |
| Education: high school or below (vs college) | +0.4049 | 0.6362 | ±1.2725 | +0.636 | 0.5245 |  |
| **Site: UCSD (vs UAB)** | **+3.0445** | 0.5705 | ±1.1409 | **+5.337** | **9.46e-08** | *** |
| Site: UW (vs UAB) | -0.8314 | 0.5209 | ±1.0417 | -1.596 | 0.1105 |  |
| **Season: spring (vs autumn)** | **-2.1327** | 0.6190 | ±1.2381 | **-3.445** | **5.71e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8406** | 0.6182 | ±1.2363 | **+2.978** | **0.0029** | ** |
| **Season: winter (vs autumn)** | **-5.6428** | 0.6643 | ±1.3286 | **-8.495** | **1.98e-17** | *** |
| Age (years) | -0.0424 | 0.0217 | ±0.0434 | -1.957 | 0.0503 | . |
| BMI (kg/m2) | -0.0262 | 0.0330 | ±0.0661 | -0.794 | 0.4271 |  |
| Hypertension | -0.7604 | 0.4994 | ±0.9989 | -1.522 | 0.1279 |  |
| High cholesterol | -0.5128 | 0.4620 | ±0.9241 | -1.110 | 0.2671 |  |
| Kidney disease | +1.1058 | 0.6071 | ±1.2143 | +1.821 | 0.0686 | . |
| Circulatory disease | +0.1798 | 0.5837 | ±1.1674 | +0.308 | 0.7580 |  |
| Time 54-69, pooled (%) | -0.0113 | 0.2348 | ±0.4696 | -0.048 | 0.9616 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **783**, R² = **0.2429**, Adj R² = **0.2291**, F-statistic = **17.60** (p = **3.98e-38**), Residual SE = **6.021** on **768** df, AIC = **5048.3**, BIC = **5118.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4566** | 1.9043 | ±3.8086 | **+25.971** | **1.06e-148** | *** |
| Education: graduate level (vs college) | +0.0107 | 0.4922 | ±0.9844 | +0.022 | 0.9827 |  |
| Education: high school or below (vs college) | +0.4071 | 0.6368 | ±1.2735 | +0.639 | 0.5226 |  |
| **Site: UCSD (vs UAB)** | **+3.0482** | 0.5700 | ±1.1400 | **+5.348** | **8.90e-08** | *** |
| Site: UW (vs UAB) | -0.8270 | 0.5214 | ±1.0428 | -1.586 | 0.1127 |  |
| **Season: spring (vs autumn)** | **-2.1303** | 0.6190 | ±1.2381 | **-3.441** | **5.79e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8436** | 0.6186 | ±1.2372 | **+2.980** | **0.0029** | ** |
| **Season: winter (vs autumn)** | **-5.6418** | 0.6641 | ±1.3282 | **-8.496** | **1.97e-17** | *** |
| **Age (years)** | **-0.0425** | 0.0217 | ±0.0434 | **-1.960** | **0.0499** | * |
| BMI (kg/m2) | -0.0263 | 0.0330 | ±0.0661 | -0.794 | 0.4270 |  |
| Hypertension | -0.7617 | 0.4994 | ±0.9988 | -1.525 | 0.1272 |  |
| High cholesterol | -0.5086 | 0.4624 | ±0.9247 | -1.100 | 0.2713 |  |
| Kidney disease | +1.1043 | 0.6066 | ±1.2131 | +1.821 | 0.0687 | . |
| Circulatory disease | +0.1820 | 0.5837 | ±1.1673 | +0.312 | 0.7552 |  |
| Avg. daily time 54-69 (%) | +0.0045 | 0.2189 | ±0.4378 | +0.021 | 0.9834 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **783**, R² = **0.2432**, Adj R² = **0.2294**, F-statistic = **17.63** (p = **3.38e-38**), Residual SE = **6.020** on **768** df, AIC = **5048.0**, BIC = **5117.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5321** | 1.9039 | ±3.8078 | **+26.016** | **3.23e-149** | *** |
| Education: graduate level (vs college) | -0.0096 | 0.4921 | ±0.9842 | -0.020 | 0.9844 |  |
| Education: high school or below (vs college) | +0.3858 | 0.6358 | ±1.2717 | +0.607 | 0.5440 |  |
| **Site: UCSD (vs UAB)** | **+3.0165** | 0.5702 | ±1.1404 | **+5.290** | **1.22e-07** | *** |
| Site: UW (vs UAB) | -0.8643 | 0.5212 | ±1.0423 | -1.658 | 0.0972 | . |
| **Season: spring (vs autumn)** | **-2.1481** | 0.6187 | ±1.2373 | **-3.472** | **5.16e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8208** | 0.6171 | ±1.2342 | **+2.950** | **0.0032** | ** |
| **Season: winter (vs autumn)** | **-5.6451** | 0.6644 | ±1.3287 | **-8.497** | **1.94e-17** | *** |
| Age (years) | -0.0419 | 0.0217 | ±0.0433 | -1.935 | 0.0530 | . |
| BMI (kg/m2) | -0.0266 | 0.0330 | ±0.0660 | -0.807 | 0.4198 |  |
| Hypertension | -0.7535 | 0.4996 | ±0.9992 | -1.508 | 0.1315 |  |
| High cholesterol | -0.5425 | 0.4621 | ±0.9243 | -1.174 | 0.2404 |  |
| Kidney disease | +1.1128 | 0.6073 | ±1.2146 | +1.832 | 0.0669 | . |
| Circulatory disease | +0.1654 | 0.5836 | ±1.1672 | +0.283 | 0.7768 |  |
| Time < 70 (%) | -0.0921 | 0.1875 | ±0.3749 | -0.491 | 0.6232 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **783**, R² = **0.2430**, Adj R² = **0.2292**, F-statistic = **17.61** (p = **3.74e-38**), Residual SE = **6.021** on **768** df, AIC = **5048.2**, BIC = **5118.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4940** | 1.9041 | ±3.8081 | **+25.994** | **5.81e-149** | *** |
| Education: graduate level (vs college) | -0.0020 | 0.4922 | ±0.9844 | -0.004 | 0.9967 |  |
| Education: high school or below (vs college) | +0.3934 | 0.6363 | ±1.2727 | +0.618 | 0.5364 |  |
| **Site: UCSD (vs UAB)** | **+3.0285** | 0.5698 | ±1.1396 | **+5.315** | **1.07e-07** | *** |
| Site: UW (vs UAB) | -0.8523 | 0.5216 | ±1.0431 | -1.634 | 0.1022 |  |
| **Season: spring (vs autumn)** | **-2.1430** | 0.6190 | ±1.2380 | **-3.462** | **5.36e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8278** | 0.6182 | ±1.2364 | **+2.957** | **0.0031** | ** |
| **Season: winter (vs autumn)** | **-5.6438** | 0.6642 | ±1.3285 | **-8.497** | **1.95e-17** | *** |
| Age (years) | -0.0421 | 0.0217 | ±0.0433 | -1.943 | 0.0520 | . |
| BMI (kg/m2) | -0.0263 | 0.0330 | ±0.0660 | -0.796 | 0.4261 |  |
| Hypertension | -0.7559 | 0.4996 | ±0.9991 | -1.513 | 0.1302 |  |
| High cholesterol | -0.5309 | 0.4623 | ±0.9246 | -1.148 | 0.2509 |  |
| Kidney disease | +1.1105 | 0.6068 | ±1.2136 | +1.830 | 0.0672 | . |
| Circulatory disease | +0.1712 | 0.5834 | ±1.1667 | +0.293 | 0.7692 |  |
| Avg. daily time < 70 (%) | -0.0557 | 0.1729 | ±0.3457 | -0.322 | 0.7474 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.2435**, Adj R² = **0.2297**, F-statistic = **17.65** (p = **3.04e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.7**, BIC = **5117.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3472** | 2.3129 | ±4.6258 | **+21.768** | **4.68e-105** | *** |
| Education: graduate level (vs college) | +0.0370 | 0.4918 | ±0.9836 | +0.075 | 0.9401 |  |
| Education: high school or below (vs college) | +0.3512 | 0.6399 | ±1.2798 | +0.549 | 0.5831 |  |
| **Site: UCSD (vs UAB)** | **+3.0800** | 0.5747 | ±1.1493 | **+5.360** | **8.33e-08** | *** |
| Site: UW (vs UAB) | -0.7863 | 0.5262 | ±1.0525 | -1.494 | 0.1351 |  |
| **Season: spring (vs autumn)** | **-2.1336** | 0.6171 | ±1.2342 | **-3.457** | **5.46e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8770** | 0.6180 | ±1.2360 | **+3.037** | **0.0024** | ** |
| **Season: winter (vs autumn)** | **-5.6421** | 0.6628 | ±1.3256 | **-8.512** | **1.70e-17** | *** |
| Age (years) | -0.0413 | 0.0217 | ±0.0433 | -1.907 | 0.0565 | . |
| BMI (kg/m2) | -0.0282 | 0.0332 | ±0.0665 | -0.849 | 0.3957 |  |
| Hypertension | -0.7761 | 0.4998 | ±0.9996 | -1.553 | 0.1205 |  |
| High cholesterol | -0.5027 | 0.4598 | ±0.9196 | -1.093 | 0.2742 |  |
| Kidney disease | +1.0802 | 0.6060 | ±1.2120 | +1.783 | 0.0747 | . |
| Circulatory disease | +0.1559 | 0.5836 | ±1.1671 | +0.267 | 0.7893 |  |
| Time 54-250, pooled (%) | -0.0100 | 0.0136 | ±0.0272 | -0.739 | 0.4600 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.2435**, Adj R² = **0.2297**, F-statistic = **17.66** (p = **3.02e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.7**, BIC = **5117.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3854** | 2.3495 | ±4.6989 | **+21.445** | **5.04e-102** | *** |
| Education: graduate level (vs college) | +0.0369 | 0.4919 | ±0.9837 | +0.075 | 0.9402 |  |
| Education: high school or below (vs college) | +0.3502 | 0.6403 | ±1.2805 | +0.547 | 0.5844 |  |
| **Site: UCSD (vs UAB)** | **+3.0811** | 0.5747 | ±1.1494 | **+5.361** | **8.27e-08** | *** |
| Site: UW (vs UAB) | -0.7870 | 0.5260 | ±1.0521 | -1.496 | 0.1346 |  |
| **Season: spring (vs autumn)** | **-2.1347** | 0.6171 | ±1.2342 | **-3.459** | **5.42e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8757** | 0.6177 | ±1.2354 | **+3.037** | **0.0024** | ** |
| **Season: winter (vs autumn)** | **-5.6429** | 0.6629 | ±1.3258 | **-8.513** | **1.70e-17** | *** |
| Age (years) | -0.0414 | 0.0216 | ±0.0433 | -1.914 | 0.0556 | . |
| BMI (kg/m2) | -0.0283 | 0.0332 | ±0.0665 | -0.852 | 0.3943 |  |
| Hypertension | -0.7754 | 0.4997 | ±0.9994 | -1.552 | 0.1207 |  |
| High cholesterol | -0.5025 | 0.4597 | ±0.9194 | -1.093 | 0.2744 |  |
| Kidney disease | +1.0773 | 0.6063 | ±1.2127 | +1.777 | 0.0756 | . |
| Circulatory disease | +0.1541 | 0.5835 | ±1.1670 | +0.264 | 0.7917 |  |
| Avg. daily time 54-250 (%) | -0.0103 | 0.0139 | ±0.0279 | -0.740 | 0.4592 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.2431**, Adj R² = **0.2293**, F-statistic = **17.62** (p = **3.60e-38**), Residual SE = **6.020** on **768** df, AIC = **5048.1**, BIC = **5118.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4579** | 1.9012 | ±3.8025 | **+26.013** | **3.49e-149** | *** |
| Education: graduate level (vs college) | +0.0068 | 0.4915 | ±0.9830 | +0.014 | 0.9890 |  |
| Education: high school or below (vs college) | +0.3805 | 0.6328 | ±1.2657 | +0.601 | 0.5477 |  |
| **Site: UCSD (vs UAB)** | **+3.0617** | 0.5726 | ±1.1452 | **+5.347** | **8.94e-08** | *** |
| Site: UW (vs UAB) | -0.8204 | 0.5222 | ±1.0444 | -1.571 | 0.1162 |  |
| **Season: spring (vs autumn)** | **-2.1449** | 0.6159 | ±1.2318 | **-3.483** | **4.97e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8345** | 0.6171 | ±1.2342 | **+2.973** | **0.0030** | ** |
| **Season: winter (vs autumn)** | **-5.6522** | 0.6632 | ±1.3264 | **-8.523** | **1.56e-17** | *** |
| **Age (years)** | **-0.0431** | 0.0217 | ±0.0434 | **-1.985** | **0.0471** | * |
| BMI (kg/m2) | -0.0291 | 0.0337 | ±0.0674 | -0.863 | 0.3881 |  |
| Hypertension | -0.7594 | 0.4997 | ±0.9995 | -1.520 | 0.1286 |  |
| High cholesterol | -0.5150 | 0.4603 | ±0.9205 | -1.119 | 0.2632 |  |
| Kidney disease | +1.0824 | 0.6066 | ±1.2132 | +1.784 | 0.0744 | . |
| Circulatory disease | +0.1725 | 0.5856 | ±1.1712 | +0.295 | 0.7683 |  |
| Time 181-250, pooled (%) | +0.0069 | 0.0157 | ±0.0314 | +0.438 | 0.6613 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **783**, R² = **0.2432**, Adj R² = **0.2294**, F-statistic = **17.63** (p = **3.49e-38**), Residual SE = **6.020** on **768** df, AIC = **5048.0**, BIC = **5118.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4562** | 1.9016 | ±3.8032 | **+26.008** | **4.03e-149** | *** |
| Education: graduate level (vs college) | +0.0051 | 0.4914 | ±0.9828 | +0.010 | 0.9917 |  |
| Education: high school or below (vs college) | +0.3745 | 0.6324 | ±1.2648 | +0.592 | 0.5537 |  |
| **Site: UCSD (vs UAB)** | **+3.0660** | 0.5732 | ±1.1464 | **+5.349** | **8.85e-08** | *** |
| Site: UW (vs UAB) | -0.8173 | 0.5225 | ±1.0449 | -1.564 | 0.1178 |  |
| **Season: spring (vs autumn)** | **-2.1478** | 0.6159 | ±1.2319 | **-3.487** | **4.88e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8329** | 0.6170 | ±1.2340 | **+2.971** | **0.0030** | ** |
| **Season: winter (vs autumn)** | **-5.6553** | 0.6632 | ±1.3264 | **-8.527** | **1.50e-17** | *** |
| **Age (years)** | **-0.0431** | 0.0217 | ±0.0434 | **-1.988** | **0.0468** | * |
| BMI (kg/m2) | -0.0295 | 0.0337 | ±0.0674 | -0.877 | 0.3807 |  |
| Hypertension | -0.7594 | 0.4996 | ±0.9993 | -1.520 | 0.1286 |  |
| High cholesterol | -0.5162 | 0.4603 | ±0.9206 | -1.122 | 0.2621 |  |
| Kidney disease | +1.0783 | 0.6064 | ±1.2128 | +1.778 | 0.0754 | . |
| Circulatory disease | +0.1723 | 0.5857 | ±1.1714 | +0.294 | 0.7686 |  |
| Avg. daily time 181-250 (%) | +0.0078 | 0.0153 | ±0.0306 | +0.509 | 0.6111 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **783**, R² = **0.2435**, Adj R² = **0.2297**, F-statistic = **17.66** (p = **2.94e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.7**, BIC = **5117.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3786** | 1.8997 | ±3.7994 | **+25.993** | **5.98e-149** | *** |
| Education: graduate level (vs college) | +0.0253 | 0.4916 | ±0.9833 | +0.052 | 0.9589 |  |
| Education: high school or below (vs college) | +0.3399 | 0.6360 | ±1.2719 | +0.534 | 0.5930 |  |
| **Site: UCSD (vs UAB)** | **+3.0847** | 0.5756 | ±1.1512 | **+5.359** | **8.37e-08** | *** |
| Site: UW (vs UAB) | -0.7913 | 0.5255 | ±1.0509 | -1.506 | 0.1321 |  |
| **Season: spring (vs autumn)** | **-2.1475** | 0.6161 | ±1.2322 | **-3.486** | **4.91e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8581** | 0.6169 | ±1.2338 | **+3.012** | **0.0026** | ** |
| **Season: winter (vs autumn)** | **-5.6524** | 0.6632 | ±1.3265 | **-8.522** | **1.56e-17** | *** |
| Age (years) | -0.0423 | 0.0217 | ±0.0433 | -1.953 | 0.0508 | . |
| BMI (kg/m2) | -0.0306 | 0.0337 | ±0.0675 | -0.908 | 0.3641 |  |
| Hypertension | -0.7698 | 0.4997 | ±0.9994 | -1.540 | 0.1235 |  |
| High cholesterol | -0.5108 | 0.4598 | ±0.9197 | -1.111 | 0.2667 |  |
| Kidney disease | +1.0643 | 0.6066 | ±1.2132 | +1.755 | 0.0793 | . |
| Circulatory disease | +0.1540 | 0.5856 | ±1.1711 | +0.263 | 0.7926 |  |
| Time > 180 (%) | +0.0071 | 0.0094 | ±0.0188 | +0.754 | 0.4506 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **783**, R² = **0.2436**, Adj R² = **0.2298**, F-statistic = **17.67** (p = **2.85e-38**), Residual SE = **6.018** on **768** df, AIC = **5047.6**, BIC = **5117.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3834** | 1.8993 | ±3.7986 | **+26.001** | **4.86e-149** | *** |
| Education: graduate level (vs college) | +0.0243 | 0.4916 | ±0.9832 | +0.049 | 0.9606 |  |
| Education: high school or below (vs college) | +0.3353 | 0.6360 | ±1.2720 | +0.527 | 0.5980 |  |
| **Site: UCSD (vs UAB)** | **+3.0887** | 0.5762 | ±1.1523 | **+5.361** | **8.28e-08** | *** |
| Site: UW (vs UAB) | -0.7891 | 0.5255 | ±1.0511 | -1.501 | 0.1332 |  |
| **Season: spring (vs autumn)** | **-2.1501** | 0.6161 | ±1.2322 | **-3.490** | **4.83e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8565** | 0.6168 | ±1.2335 | **+3.010** | **0.0026** | ** |
| **Season: winter (vs autumn)** | **-5.6552** | 0.6633 | ±1.3267 | **-8.525** | **1.52e-17** | *** |
| Age (years) | -0.0423 | 0.0216 | ±0.0433 | -1.955 | 0.0506 | . |
| BMI (kg/m2) | -0.0309 | 0.0337 | ±0.0675 | -0.915 | 0.3604 |  |
| Hypertension | -0.7695 | 0.4997 | ±0.9993 | -1.540 | 0.1235 |  |
| High cholesterol | -0.5113 | 0.4599 | ±0.9198 | -1.112 | 0.2662 |  |
| Kidney disease | +1.0601 | 0.6067 | ±1.2133 | +1.747 | 0.0806 | . |
| Circulatory disease | +0.1531 | 0.5857 | ±1.1714 | +0.261 | 0.7938 |  |
| Avg. daily time > 180 (%) | +0.0074 | 0.0094 | ±0.0187 | +0.789 | 0.4302 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **783**, R² = **0.2429**, Adj R² = **0.2291**, F-statistic = **17.60** (p = **3.94e-38**), Residual SE = **6.021** on **768** df, AIC = **5048.3**, BIC = **5118.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4503** | 1.9009 | ±3.8018 | **+26.014** | **3.43e-149** | *** |
| Education: graduate level (vs college) | +0.0151 | 0.4927 | ±0.9854 | +0.031 | 0.9756 |  |
| Education: high school or below (vs college) | +0.3967 | 0.6376 | ±1.2752 | +0.622 | 0.5338 |  |
| **Site: UCSD (vs UAB)** | **+3.0541** | 0.5759 | ±1.1517 | **+5.304** | **1.14e-07** | *** |
| Site: UW (vs UAB) | -0.8235 | 0.5239 | ±1.0478 | -1.572 | 0.1160 |  |
| **Season: spring (vs autumn)** | **-2.1350** | 0.6164 | ±1.2328 | **-3.464** | **5.33e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8461** | 0.6171 | ±1.2342 | **+2.992** | **0.0028** | ** |
| **Season: winter (vs autumn)** | **-5.6447** | 0.6643 | ±1.3286 | **-8.497** | **1.94e-17** | *** |
| Age (years) | -0.0423 | 0.0217 | ±0.0433 | -1.953 | 0.0508 | . |
| BMI (kg/m2) | -0.0272 | 0.0339 | ±0.0678 | -0.802 | 0.4228 |  |
| Hypertension | -0.7619 | 0.5001 | ±1.0002 | -1.523 | 0.1276 |  |
| High cholesterol | -0.5094 | 0.4597 | ±0.9194 | -1.108 | 0.2678 |  |
| Kidney disease | +1.1001 | 0.6070 | ±1.2140 | +1.812 | 0.0699 | . |
| Circulatory disease | +0.1769 | 0.5840 | ±1.1679 | +0.303 | 0.7619 |  |
| Nocturnal time > 180 (%) | +0.0012 | 0.0083 | ±0.0167 | +0.138 | 0.8902 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.2435**, Adj R² = **0.2297**, F-statistic = **17.66** (p = **2.94e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.7**, BIC = **5117.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3396** | 1.8983 | ±3.7966 | **+25.991** | **6.20e-149** | *** |
| Education: graduate level (vs college) | +0.0379 | 0.4918 | ±0.9835 | +0.077 | 0.9386 |  |
| Education: high school or below (vs college) | +0.3469 | 0.6399 | ±1.2798 | +0.542 | 0.5877 |  |
| **Site: UCSD (vs UAB)** | **+3.0809** | 0.5745 | ±1.1490 | **+5.363** | **8.19e-08** | *** |
| Site: UW (vs UAB) | -0.7851 | 0.5260 | ±1.0521 | -1.493 | 0.1355 |  |
| **Season: spring (vs autumn)** | **-2.1342** | 0.6171 | ±1.2342 | **-3.458** | **5.43e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8785** | 0.6180 | ±1.2359 | **+3.040** | **0.0024** | ** |
| **Season: winter (vs autumn)** | **-5.6417** | 0.6627 | ±1.3254 | **-8.513** | **1.70e-17** | *** |
| Age (years) | -0.0412 | 0.0217 | ±0.0433 | -1.903 | 0.0570 | . |
| BMI (kg/m2) | -0.0284 | 0.0332 | ±0.0665 | -0.855 | 0.3928 |  |
| Hypertension | -0.7769 | 0.4998 | ±0.9996 | -1.555 | 0.1201 |  |
| High cholesterol | -0.5033 | 0.4598 | ±0.9196 | -1.095 | 0.2736 |  |
| Kidney disease | +1.0787 | 0.6059 | ±1.2118 | +1.780 | 0.0750 | . |
| Circulatory disease | +0.1539 | 0.5836 | ±1.1671 | +0.264 | 0.7920 |  |
| Time > 250 (%) | +0.0106 | 0.0136 | ±0.0272 | +0.784 | 0.4331 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 783)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **783**, R² = **0.2435**, Adj R² = **0.2297**, F-statistic = **17.66** (p = **2.94e-38**), Residual SE = **6.019** on **768** df, AIC = **5047.7**, BIC = **5117.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3523** | 1.8964 | ±3.7928 | **+26.024** | **2.63e-149** | *** |
| Education: graduate level (vs college) | +0.0375 | 0.4918 | ±0.9836 | +0.076 | 0.9392 |  |
| Education: high school or below (vs college) | +0.3469 | 0.6403 | ±1.2807 | +0.542 | 0.5880 |  |
| **Site: UCSD (vs UAB)** | **+3.0816** | 0.5745 | ±1.1491 | **+5.363** | **8.16e-08** | *** |
| Site: UW (vs UAB) | -0.7865 | 0.5258 | ±1.0517 | -1.496 | 0.1347 |  |
| **Season: spring (vs autumn)** | **-2.1356** | 0.6171 | ±1.2341 | **-3.461** | **5.38e-04** | *** |
| **Season: summer (vs autumn)** | **+1.8763** | 0.6176 | ±1.2353 | **+3.038** | **0.0024** | ** |
| **Season: winter (vs autumn)** | **-5.6428** | 0.6628 | ±1.3257 | **-8.513** | **1.69e-17** | *** |
| Age (years) | -0.0414 | 0.0216 | ±0.0433 | -1.911 | 0.0560 | . |
| BMI (kg/m2) | -0.0284 | 0.0332 | ±0.0665 | -0.855 | 0.3923 |  |
| Hypertension | -0.7759 | 0.4997 | ±0.9994 | -1.553 | 0.1205 |  |
| High cholesterol | -0.5032 | 0.4597 | ±0.9195 | -1.095 | 0.2737 |  |
| Kidney disease | +1.0762 | 0.6063 | ±1.2125 | +1.775 | 0.0759 | . |
| Circulatory disease | +0.1525 | 0.5835 | ±1.1670 | +0.261 | 0.7938 |  |
| Avg. daily time > 250 (%) | +0.0108 | 0.0139 | ±0.0279 | +0.772 | 0.4400 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 783; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **783**, R² = **0.0712**, Adj R² = **0.0555**, F-statistic = **4.53** (p = **1.67e-07**), Residual SE = **16.867** on **769** df, AIC = **6660.4**, BIC = **6725.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.6351** | 6.6943 | ±13.3887 | **+18.917** | **8.30e-80** | *** |
| Education: graduate level (vs college) | -1.0720 | 1.2495 | ±2.4991 | -0.858 | 0.3909 |  |
| **Education: high school or below (vs college)** | **+6.2851** | 2.2654 | ±4.5307 | **+2.774** | **0.0055** | ** |
| Site: UCSD (vs UAB) | +3.1010 | 1.6964 | ±3.3928 | +1.828 | 0.0675 | . |
| Site: UW (vs UAB) | -2.8051 | 1.4313 | ±2.8627 | -1.960 | 0.0500 | . |
| **Season: spring (vs autumn)** | **+3.5501** | 1.4970 | ±2.9940 | **+2.371** | **0.0177** | * |
| Season: summer (vs autumn) | +3.1214 | 1.6511 | ±3.3022 | +1.891 | 0.0587 | . |
| **Season: winter (vs autumn)** | **+3.7614** | 1.8748 | ±3.7495 | **+2.006** | **0.0448** | * |
| **Age (years)** | **-0.1493** | 0.0690 | ±0.1379 | **-2.165** | **0.0304** | * |
| BMI (kg/m2) | +0.1956 | 0.1098 | ±0.2196 | +1.782 | 0.0748 | . |
| Hypertension | +0.5220 | 1.4770 | ±2.9539 | +0.353 | 0.7238 |  |
| High cholesterol | +1.9132 | 1.3427 | ±2.6854 | +1.425 | 0.1542 |  |
| Kidney disease | -2.0221 | 1.7254 | ±3.4507 | -1.172 | 0.2412 |  |
| Circulatory disease | +0.0338 | 1.7091 | ±3.4182 | +0.020 | 0.9842 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **783**, R² = **0.0808**, Adj R² = **0.0640**, F-statistic = **4.82** (p = **1.40e-08**), Residual SE = **16.790** on **768** df, AIC = **6654.3**, BIC = **6724.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+134.5959** | 7.1333 | ±14.2666 | **+18.869** | **2.06e-79** | *** |
| Education: graduate level (vs college) | -1.3302 | 1.2398 | ±2.4796 | -1.073 | 0.2833 |  |
| **Education: high school or below (vs college)** | **+7.0160** | 2.2657 | ±4.5315 | **+3.097** | **0.0020** | ** |
| Site: UCSD (vs UAB) | +2.8489 | 1.6891 | ±3.3782 | +1.687 | 0.0917 | . |
| **Site: UW (vs UAB)** | **-3.1537** | 1.4258 | ±2.8516 | **-2.212** | **0.0270** | * |
| **Season: spring (vs autumn)** | **+3.4113** | 1.4957 | ±2.9914 | **+2.281** | **0.0226** | * |
| Season: summer (vs autumn) | +2.9369 | 1.6499 | ±3.2998 | +1.780 | 0.0751 | . |
| **Season: winter (vs autumn)** | **+3.7444** | 1.8659 | ±3.7317 | **+2.007** | **0.0448** | * |
| **Age (years)** | **-0.1524** | 0.0690 | ±0.1380 | **-2.209** | **0.0272** | * |
| **BMI (kg/m2)** | **+0.2371** | 0.1110 | ±0.2221 | **+2.135** | **0.0327** | * |
| Hypertension | +0.7048 | 1.4678 | ±2.9356 | +0.480 | 0.6311 |  |
| High cholesterol | +2.0618 | 1.3395 | ±2.6791 | +1.539 | 0.1238 |  |
| Kidney disease | -1.9705 | 1.7151 | ±3.4302 | -1.149 | 0.2506 |  |
| Circulatory disease | +0.3184 | 1.7059 | ±3.4117 | +0.187 | 0.8519 |  |
| **HbA1c (%)** | **-1.3267** | 0.5129 | ±1.0258 | **-2.587** | **0.0097** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **783**, R² = **0.0763**, Adj R² = **0.0595**, F-statistic = **4.53** (p = **6.48e-08**), Residual SE = **16.831** on **768** df, AIC = **6658.1**, BIC = **6728.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+131.2762** | 7.3033 | ±14.6065 | **+17.975** | **3.06e-72** | *** |
| Education: graduate level (vs college) | -1.1912 | 1.2420 | ±2.4839 | -0.959 | 0.3375 |  |
| **Education: high school or below (vs college)** | **+6.7766** | 2.2785 | ±4.5571 | **+2.974** | **0.0029** | ** |
| Site: UCSD (vs UAB) | +2.8551 | 1.7109 | ±3.4218 | +1.669 | 0.0952 | . |
| **Site: UW (vs UAB)** | **-3.0484** | 1.4345 | ±2.8689 | **-2.125** | **0.0336** | * |
| **Season: spring (vs autumn)** | **+3.6622** | 1.4962 | ±2.9924 | **+2.448** | **0.0144** | * |
| Season: summer (vs autumn) | +2.9547 | 1.6603 | ±3.3205 | +1.780 | 0.0751 | . |
| **Season: winter (vs autumn)** | **+3.7904** | 1.8626 | ±3.7252 | **+2.035** | **0.0418** | * |
| **Age (years)** | **-0.1530** | 0.0695 | ±0.1390 | **-2.201** | **0.0277** | * |
| **BMI (kg/m2)** | **+0.2225** | 0.1091 | ±0.2182 | **+2.039** | **0.0415** | * |
| Hypertension | +0.6173 | 1.4769 | ±2.9538 | +0.418 | 0.6760 |  |
| High cholesterol | +1.9597 | 1.3444 | ±2.6888 | +1.458 | 0.1449 |  |
| Kidney disease | -1.8215 | 1.7330 | ±3.4659 | -1.051 | 0.2932 |  |
| Circulatory disease | +0.2587 | 1.7067 | ±3.4134 | +0.152 | 0.8795 |  |
| Mean glucose (mg/dL) | -0.0325 | 0.0169 | ±0.0337 | -1.923 | 0.0545 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **783**, R² = **0.0763**, Adj R² = **0.0595**, F-statistic = **4.53** (p = **6.48e-08**), Residual SE = **16.831** on **768** df, AIC = **6658.1**, BIC = **6728.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+135.7669** | 8.5236 | ±17.0472 | **+15.928** | **4.03e-57** | *** |
| Education: graduate level (vs college) | -1.1912 | 1.2420 | ±2.4839 | -0.959 | 0.3375 |  |
| **Education: high school or below (vs college)** | **+6.7766** | 2.2785 | ±4.5571 | **+2.974** | **0.0029** | ** |
| Site: UCSD (vs UAB) | +2.8551 | 1.7109 | ±3.4218 | +1.669 | 0.0952 | . |
| **Site: UW (vs UAB)** | **-3.0484** | 1.4345 | ±2.8689 | **-2.125** | **0.0336** | * |
| **Season: spring (vs autumn)** | **+3.6622** | 1.4962 | ±2.9924 | **+2.448** | **0.0144** | * |
| Season: summer (vs autumn) | +2.9547 | 1.6603 | ±3.3205 | +1.780 | 0.0751 | . |
| **Season: winter (vs autumn)** | **+3.7904** | 1.8626 | ±3.7252 | **+2.035** | **0.0418** | * |
| **Age (years)** | **-0.1530** | 0.0695 | ±0.1390 | **-2.201** | **0.0277** | * |
| **BMI (kg/m2)** | **+0.2225** | 0.1091 | ±0.2182 | **+2.039** | **0.0415** | * |
| Hypertension | +0.6173 | 1.4769 | ±2.9538 | +0.418 | 0.6760 |  |
| High cholesterol | +1.9597 | 1.3444 | ±2.6888 | +1.458 | 0.1449 |  |
| Kidney disease | -1.8215 | 1.7330 | ±3.4659 | -1.051 | 0.2932 |  |
| Circulatory disease | +0.2587 | 1.7067 | ±3.4134 | +0.152 | 0.8795 |  |
| GMI (%) | -1.3567 | 0.7054 | ±1.4109 | -1.923 | 0.0545 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **783**, R² = **0.0754**, Adj R² = **0.0585**, F-statistic = **4.47** (p = **9.07e-08**), Residual SE = **16.840** on **768** df, AIC = **6658.9**, BIC = **6728.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.4578** | 7.4496 | ±14.8993 | **+17.512** | **1.16e-68** | *** |
| Education: graduate level (vs college) | -1.2246 | 1.2419 | ±2.4838 | -0.986 | 0.3241 |  |
| **Education: high school or below (vs college)** | **+6.6782** | 2.2526 | ±4.5053 | **+2.965** | **0.0030** | ** |
| Site: UCSD (vs UAB) | +2.8939 | 1.7127 | ±3.4254 | +1.690 | 0.0911 | . |
| **Site: UW (vs UAB)** | **-2.9516** | 1.4314 | ±2.8627 | **-2.062** | **0.0392** | * |
| **Season: spring (vs autumn)** | **+3.7021** | 1.4947 | ±2.9895 | **+2.477** | **0.0133** | * |
| Season: summer (vs autumn) | +2.9646 | 1.6638 | ±3.3276 | +1.782 | 0.0748 | . |
| **Season: winter (vs autumn)** | **+3.8185** | 1.8596 | ±3.7191 | **+2.053** | **0.0400** | * |
| **Age (years)** | **-0.1568** | 0.0702 | ±0.1403 | **-2.235** | **0.0254** | * |
| **BMI (kg/m2)** | **+0.2258** | 0.1086 | ±0.2172 | **+2.079** | **0.0376** | * |
| Hypertension | +0.5803 | 1.4795 | ±2.9590 | +0.392 | 0.6949 |  |
| High cholesterol | +1.9463 | 1.3459 | ±2.6919 | +1.446 | 0.1482 |  |
| Kidney disease | -1.9589 | 1.7311 | ±3.4622 | -1.132 | 0.2578 |  |
| Circulatory disease | +0.2180 | 1.7021 | ±3.4043 | +0.128 | 0.8981 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0276 | 0.0177 | ±0.0355 | -1.557 | 0.1194 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **783**, R² = **0.0742**, Adj R² = **0.0573**, F-statistic = **4.39** (p = **1.36e-07**), Residual SE = **16.851** on **768** df, AIC = **6659.9**, BIC = **6729.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.2029** | 6.7374 | ±13.4749 | **+19.177** | **5.78e-82** | *** |
| Education: graduate level (vs college) | -1.2158 | 1.2462 | ±2.4924 | -0.976 | 0.3293 |  |
| **Education: high school or below (vs college)** | **+6.5804** | 2.2759 | ±4.5519 | **+2.891** | **0.0038** | ** |
| Site: UCSD (vs UAB) | +2.9141 | 1.7111 | ±3.4222 | +1.703 | 0.0886 | . |
| **Site: UW (vs UAB)** | **-3.1123** | 1.4411 | ±2.8823 | **-2.160** | **0.0308** | * |
| **Season: spring (vs autumn)** | **+3.6451** | 1.4990 | ±2.9980 | **+2.432** | **0.0150** | * |
| Season: summer (vs autumn) | +3.0251 | 1.6554 | ±3.3108 | +1.827 | 0.0676 | . |
| **Season: winter (vs autumn)** | **+3.7901** | 1.8686 | ±3.7372 | **+2.028** | **0.0425** | * |
| **Age (years)** | **-0.1481** | 0.0693 | ±0.1386 | **-2.137** | **0.0326** | * |
| BMI (kg/m2) | +0.2138 | 0.1116 | ±0.2232 | +1.916 | 0.0554 | . |
| Hypertension | +0.6476 | 1.4685 | ±2.9370 | +0.441 | 0.6592 |  |
| High cholesterol | +1.8647 | 1.3376 | ±2.6751 | +1.394 | 0.1633 |  |
| Kidney disease | -1.5034 | 1.7507 | ±3.5015 | -0.859 | 0.3905 |  |
| Circulatory disease | +0.1769 | 1.7029 | ±3.4058 | +0.104 | 0.9173 |  |
| Glucose SD, pooled (mg/dL) | -0.0834 | 0.0609 | ±0.1219 | -1.368 | 0.1713 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **783**, R² = **0.0722**, Adj R² = **0.0552**, F-statistic = **4.27** (p = **2.66e-07**), Residual SE = **16.869** on **768** df, AIC = **6661.6**, BIC = **6731.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.1765** | 6.8007 | ±13.6015 | **+18.847** | **3.08e-79** | *** |
| Education: graduate level (vs college) | -1.1368 | 1.2505 | ±2.5010 | -0.909 | 0.3633 |  |
| **Education: high school or below (vs college)** | **+6.4726** | 2.2755 | ±4.5509 | **+2.845** | **0.0044** | ** |
| Site: UCSD (vs UAB) | +2.9913 | 1.7056 | ±3.4111 | +1.754 | 0.0795 | . |
| **Site: UW (vs UAB)** | **-2.9678** | 1.4409 | ±2.8819 | **-2.060** | **0.0394** | * |
| **Season: spring (vs autumn)** | **+3.6024** | 1.4974 | ±2.9947 | **+2.406** | **0.0161** | * |
| Season: summer (vs autumn) | +3.0595 | 1.6582 | ±3.3164 | +1.845 | 0.0650 | . |
| **Season: winter (vs autumn)** | **+3.7561** | 1.8748 | ±3.7495 | **+2.004** | **0.0451** | * |
| **Age (years)** | **-0.1480** | 0.0692 | ±0.1384 | **-2.138** | **0.0325** | * |
| BMI (kg/m2) | +0.2036 | 0.1107 | ±0.2213 | +1.840 | 0.0657 | . |
| Hypertension | +0.5850 | 1.4745 | ±2.9490 | +0.397 | 0.6915 |  |
| High cholesterol | +1.8886 | 1.3415 | ±2.6830 | +1.408 | 0.1592 |  |
| Kidney disease | -1.7046 | 1.7511 | ±3.5021 | -0.973 | 0.3303 |  |
| Circulatory disease | +0.1031 | 1.7106 | ±3.4212 | +0.060 | 0.9520 |  |
| Avg. daily SD (mg/dL) | -0.0545 | 0.0587 | ±0.1174 | -0.928 | 0.3533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **783**, R² = **0.0712**, Adj R² = **0.0543**, F-statistic = **4.21** (p = **3.61e-07**), Residual SE = **16.877** on **768** df, AIC = **6662.4**, BIC = **6732.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.2674** | 6.5137 | ±13.0275 | **+19.538** | **5.19e-85** | *** |
| Education: graduate level (vs college) | -1.0901 | 1.2575 | ±2.5150 | -0.867 | 0.3860 |  |
| **Education: high school or below (vs college)** | **+6.2906** | 2.2691 | ±4.5382 | **+2.772** | **0.0056** | ** |
| Site: UCSD (vs UAB) | +3.0830 | 1.6991 | ±3.3982 | +1.814 | 0.0696 | . |
| **Site: UW (vs UAB)** | **-2.8453** | 1.4348 | ±2.8697 | **-1.983** | **0.0474** | * |
| **Season: spring (vs autumn)** | **+3.5511** | 1.4992 | ±2.9984 | **+2.369** | **0.0179** | * |
| Season: summer (vs autumn) | +3.1195 | 1.6527 | ±3.3053 | +1.888 | 0.0591 | . |
| **Season: winter (vs autumn)** | **+3.7620** | 1.8774 | ±3.7549 | **+2.004** | **0.0451** | * |
| **Age (years)** | **-0.1485** | 0.0699 | ±0.1398 | **-2.125** | **0.0336** | * |
| BMI (kg/m2) | +0.1963 | 0.1106 | ±0.2211 | +1.776 | 0.0758 | . |
| Hypertension | +0.5394 | 1.4647 | ±2.9293 | +0.368 | 0.7127 |  |
| High cholesterol | +1.8930 | 1.3404 | ±2.6807 | +1.412 | 0.1579 |  |
| Kidney disease | -1.9369 | 1.7410 | ±3.4819 | -1.113 | 0.2659 |  |
| Circulatory disease | +0.0373 | 1.7108 | ±3.4215 | +0.022 | 0.9826 |  |
| CV (%) | -0.0291 | 0.1150 | ±0.2300 | -0.253 | 0.8005 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **783**, R² = **0.0712**, Adj R² = **0.0543**, F-statistic = **4.20** (p = **3.68e-07**), Residual SE = **16.878** on **768** df, AIC = **6662.4**, BIC = **6732.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2500** | 7.9794 | ±15.9589 | **+15.822** | **2.20e-56** | *** |
| Education: graduate level (vs college) | -1.0792 | 1.2566 | ±2.5132 | -0.859 | 0.3904 |  |
| **Education: high school or below (vs college)** | **+6.2874** | 2.2678 | ±4.5356 | **+2.772** | **0.0056** | ** |
| Site: UCSD (vs UAB) | +3.0966 | 1.6984 | ±3.3969 | +1.823 | 0.0683 | . |
| **Site: UW (vs UAB)** | **-2.8222** | 1.4330 | ±2.8661 | **-1.969** | **0.0489** | * |
| **Season: spring (vs autumn)** | **+3.5537** | 1.5004 | ±3.0007 | **+2.369** | **0.0179** | * |
| Season: summer (vs autumn) | +3.1293 | 1.6562 | ±3.3124 | +1.889 | 0.0588 | . |
| **Season: winter (vs autumn)** | **+3.7665** | 1.8832 | ±3.7663 | **+2.000** | **0.0455** | * |
| **Age (years)** | **-0.1490** | 0.0697 | ±0.1394 | **-2.138** | **0.0325** | * |
| BMI (kg/m2) | +0.1958 | 0.1101 | ±0.2202 | +1.778 | 0.0754 | . |
| Hypertension | +0.5306 | 1.4673 | ±2.9346 | +0.362 | 0.7176 |  |
| High cholesterol | +1.9078 | 1.3414 | ±2.6827 | +1.422 | 0.1549 |  |
| Kidney disease | -1.9860 | 1.7330 | ±3.4661 | -1.146 | 0.2518 |  |
| Circulatory disease | +0.0390 | 1.7092 | ±3.4183 | +0.023 | 0.9818 |  |
| Mean / SD ratio | +0.0812 | 0.6347 | ±1.2695 | +0.128 | 0.8983 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **783**, R² = **0.0717**, Adj R² = **0.0548**, F-statistic = **4.24** (p = **3.06e-07**), Residual SE = **16.873** on **768** df, AIC = **6662.0**, BIC = **6731.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.5085** | 7.6080 | ±15.2159 | **+16.891** | **5.21e-64** | *** |
| Education: graduate level (vs college) | -1.0444 | 1.2567 | ±2.5134 | -0.831 | 0.4059 |  |
| **Education: high school or below (vs college)** | **+6.2673** | 2.2642 | ±4.5284 | **+2.768** | **0.0056** | ** |
| Site: UCSD (vs UAB) | +3.1189 | 1.6976 | ±3.3952 | +1.837 | 0.0662 | . |
| Site: UW (vs UAB) | -2.7276 | 1.4351 | ±2.8701 | -1.901 | 0.0573 | . |
| **Season: spring (vs autumn)** | **+3.5598** | 1.5017 | ±3.0033 | **+2.371** | **0.0178** | * |
| Season: summer (vs autumn) | +3.0970 | 1.6520 | ±3.3039 | +1.875 | 0.0608 | . |
| **Season: winter (vs autumn)** | **+3.7580** | 1.8769 | ±3.7538 | **+2.002** | **0.0453** | * |
| **Age (years)** | **-0.1518** | 0.0697 | ±0.1395 | **-2.176** | **0.0296** | * |
| BMI (kg/m2) | +0.1968 | 0.1096 | ±0.2192 | +1.796 | 0.0725 | . |
| Hypertension | +0.4809 | 1.4715 | ±2.9429 | +0.327 | 0.7438 |  |
| High cholesterol | +1.9474 | 1.3455 | ±2.6911 | +1.447 | 0.1478 |  |
| Kidney disease | -2.2008 | 1.7415 | ±3.4830 | -1.264 | 0.2063 |  |
| Circulatory disease | +0.0265 | 1.7101 | ±3.4202 | +0.016 | 0.9876 |  |
| Avg. daily mean/SD | -0.3402 | 0.4846 | ±0.9691 | -0.702 | 0.4826 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **783**, R² = **0.0712**, Adj R² = **0.0542**, F-statistic = **4.20** (p = **3.70e-07**), Residual SE = **16.878** on **768** df, AIC = **6662.4**, BIC = **6732.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.8268** | 6.7159 | ±13.4319 | **+18.884** | **1.53e-79** | *** |
| Education: graduate level (vs college) | -1.0788 | 1.2509 | ±2.5017 | -0.862 | 0.3885 |  |
| **Education: high school or below (vs college)** | **+6.2886** | 2.2796 | ±4.5592 | **+2.759** | **0.0058** | ** |
| Site: UCSD (vs UAB) | +3.0936 | 1.6893 | ±3.3786 | +1.831 | 0.0671 | . |
| **Site: UW (vs UAB)** | **-2.8200** | 1.4228 | ±2.8455 | **-1.982** | **0.0475** | * |
| **Season: spring (vs autumn)** | **+3.5512** | 1.5005 | ±3.0011 | **+2.367** | **0.0180** | * |
| Season: summer (vs autumn) | +3.1134 | 1.6446 | ±3.2891 | +1.893 | 0.0583 | . |
| **Season: winter (vs autumn)** | **+3.7585** | 1.8728 | ±3.7455 | **+2.007** | **0.0448** | * |
| **Age (years)** | **-0.1496** | 0.0679 | ±0.1358 | **-2.204** | **0.0276** | * |
| BMI (kg/m2) | +0.1959 | 0.1111 | ±0.2222 | +1.763 | 0.0779 | . |
| Hypertension | +0.5198 | 1.4830 | ±2.9660 | +0.350 | 0.7260 |  |
| High cholesterol | +1.9077 | 1.3657 | ±2.7314 | +1.397 | 0.1625 |  |
| Kidney disease | -2.0140 | 1.7074 | ±3.4148 | -1.180 | 0.2382 |  |
| Circulatory disease | +0.0357 | 1.7186 | ±3.4371 | +0.021 | 0.9834 |  |
| MAG (mg/dL/h) | -0.0037 | 0.0717 | ±0.1434 | -0.052 | 0.9588 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **783**, R² = **0.0715**, Adj R² = **0.0546**, F-statistic = **4.23** (p = **3.28e-07**), Residual SE = **16.875** on **768** df, AIC = **6662.1**, BIC = **6732.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.0686** | 6.9079 | ±13.8158 | **+18.539** | **9.91e-77** | *** |
| Education: graduate level (vs college) | -1.1111 | 1.2515 | ±2.5030 | -0.888 | 0.3746 |  |
| **Education: high school or below (vs college)** | **+6.3956** | 2.2732 | ±4.5464 | **+2.813** | **0.0049** | ** |
| Site: UCSD (vs UAB) | +3.0223 | 1.7020 | ±3.4039 | +1.776 | 0.0758 | . |
| **Site: UW (vs UAB)** | **-2.9114** | 1.4337 | ±2.8675 | **-2.031** | **0.0423** | * |
| **Season: spring (vs autumn)** | **+3.5952** | 1.4998 | ±2.9997 | **+2.397** | **0.0165** | * |
| Season: summer (vs autumn) | +3.1054 | 1.6546 | ±3.3092 | +1.877 | 0.0605 | . |
| **Season: winter (vs autumn)** | **+3.7673** | 1.8760 | ±3.7520 | **+2.008** | **0.0446** | * |
| **Age (years)** | **-0.1499** | 0.0690 | ±0.1380 | **-2.172** | **0.0299** | * |
| BMI (kg/m2) | +0.1990 | 0.1106 | ±0.2212 | +1.800 | 0.0719 | . |
| Hypertension | +0.5368 | 1.4764 | ±2.9528 | +0.364 | 0.7162 |  |
| High cholesterol | +1.8924 | 1.3422 | ±2.6845 | +1.410 | 0.1586 |  |
| Kidney disease | -1.8337 | 1.7391 | ±3.4782 | -1.054 | 0.2917 |  |
| Circulatory disease | +0.0793 | 1.7116 | ±3.4233 | +0.046 | 0.9630 |  |
| Avg. daily range (mg/dL) | -0.0098 | 0.0173 | ±0.0346 | -0.564 | 0.5725 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **783**, R² = **0.0799**, Adj R² = **0.0631**, F-statistic = **4.76** (p = **1.91e-08**), Residual SE = **16.798** on **768** df, AIC = **6655.0**, BIC = **6725.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.6592** | 6.6878 | ±13.3757 | **+19.238** | **1.79e-82** | *** |
| Education: graduate level (vs college) | -1.4472 | 1.2468 | ±2.4935 | -1.161 | 0.2457 |  |
| **Education: high school or below (vs college)** | **+6.4897** | 2.2454 | ±4.4907 | **+2.890** | **0.0038** | ** |
| Site: UCSD (vs UAB) | +2.8968 | 1.7088 | ±3.4176 | +1.695 | 0.0900 | . |
| **Site: UW (vs UAB)** | **-3.2067** | 1.4383 | ±2.8766 | **-2.230** | **0.0258** | * |
| **Season: spring (vs autumn)** | **+3.6763** | 1.4990 | ±2.9981 | **+2.452** | **0.0142** | * |
| Season: summer (vs autumn) | +3.1077 | 1.6424 | ±3.2848 | +1.892 | 0.0585 | . |
| **Season: winter (vs autumn)** | **+3.9688** | 1.8424 | ±3.6849 | **+2.154** | **0.0312** | * |
| **Age (years)** | **-0.1568** | 0.0690 | ±0.1380 | **-2.272** | **0.0231** | * |
| **BMI (kg/m2)** | **+0.2320** | 0.1148 | ±0.2297 | **+2.020** | **0.0434** | * |
| Hypertension | +0.7718 | 1.4735 | ±2.9470 | +0.524 | 0.6004 |  |
| High cholesterol | +1.8768 | 1.3392 | ±2.6785 | +1.401 | 0.1611 |  |
| Kidney disease | -1.6470 | 1.7400 | ±3.4799 | -0.947 | 0.3439 |  |
| Circulatory disease | +0.3865 | 1.6833 | ±3.3667 | +0.230 | 0.8184 |  |
| SD of daily means (mg/dL) | -0.2075 | 0.1298 | ±0.2595 | -1.599 | 0.1098 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **783**, R² = **0.0756**, Adj R² = **0.0587**, F-statistic = **4.48** (p = **8.43e-08**), Residual SE = **16.838** on **768** df, AIC = **6658.7**, BIC = **6728.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.4185** | 7.0550 | ±14.1099 | **+17.352** | **1.90e-67** | *** |
| Education: graduate level (vs college) | -1.1862 | 1.2385 | ±2.4770 | -0.958 | 0.3382 |  |
| **Education: high school or below (vs college)** | **+6.7233** | 2.2847 | ±4.5695 | **+2.943** | **0.0033** | ** |
| Site: UCSD (vs UAB) | +2.8308 | 1.7075 | ±3.4150 | +1.658 | 0.0973 | . |
| **Site: UW (vs UAB)** | **-3.0746** | 1.4276 | ±2.8553 | **-2.154** | **0.0313** | * |
| **Season: spring (vs autumn)** | **+3.6523** | 1.4917 | ±2.9835 | **+2.448** | **0.0143** | * |
| Season: summer (vs autumn) | +3.0065 | 1.6561 | ±3.3121 | +1.815 | 0.0695 | . |
| **Season: winter (vs autumn)** | **+3.8297** | 1.8569 | ±3.7138 | **+2.062** | **0.0392** | * |
| **Age (years)** | **-0.1504** | 0.0695 | ±0.1390 | **-2.164** | **0.0305** | * |
| **BMI (kg/m2)** | **+0.2249** | 0.1100 | ±0.2200 | **+2.044** | **0.0409** | * |
| Hypertension | +0.5835 | 1.4787 | ±2.9574 | +0.395 | 0.6931 |  |
| High cholesterol | +1.9021 | 1.3433 | ±2.6866 | +1.416 | 0.1568 |  |
| Kidney disease | -1.7452 | 1.7444 | ±3.4888 | -1.000 | 0.3171 |  |
| Circulatory disease | +0.2098 | 1.7086 | ±3.4171 | +0.123 | 0.9023 |  |
| Time in range 70-180, pooled (%) | +0.0479 | 0.0279 | ±0.0557 | +1.720 | 0.0854 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **783**, R² = **0.0759**, Adj R² = **0.0590**, F-statistic = **4.50** (p = **7.58e-08**), Residual SE = **16.835** on **768** df, AIC = **6658.4**, BIC = **6728.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.2385** | 7.0485 | ±14.0969 | **+17.343** | **2.24e-67** | *** |
| Education: graduate level (vs college) | -1.1784 | 1.2396 | ±2.4791 | -0.951 | 0.3418 |  |
| **Education: high school or below (vs college)** | **+6.7482** | 2.2816 | ±4.5632 | **+2.958** | **0.0031** | ** |
| Site: UCSD (vs UAB) | +2.8065 | 1.7087 | ±3.4174 | +1.642 | 0.1005 |  |
| **Site: UW (vs UAB)** | **-3.0888** | 1.4278 | ±2.8555 | **-2.163** | **0.0305** | * |
| **Season: spring (vs autumn)** | **+3.6670** | 1.4911 | ±2.9822 | **+2.459** | **0.0139** | * |
| Season: summer (vs autumn) | +3.0168 | 1.6543 | ±3.3085 | +1.824 | 0.0682 | . |
| **Season: winter (vs autumn)** | **+3.8477** | 1.8537 | ±3.7074 | **+2.076** | **0.0379** | * |
| **Age (years)** | **-0.1500** | 0.0695 | ±0.1390 | **-2.159** | **0.0308** | * |
| **BMI (kg/m2)** | **+0.2264** | 0.1099 | ±0.2198 | **+2.060** | **0.0394** | * |
| Hypertension | +0.5817 | 1.4787 | ±2.9573 | +0.393 | 0.6940 |  |
| High cholesterol | +1.9041 | 1.3432 | ±2.6865 | +1.418 | 0.1563 |  |
| Kidney disease | -1.7193 | 1.7424 | ±3.4848 | -0.987 | 0.3238 |  |
| Circulatory disease | +0.2131 | 1.7089 | ±3.4178 | +0.125 | 0.9007 |  |
| Avg. daily time in range 70-180 (%) | +0.0493 | 0.0277 | ±0.0554 | +1.780 | 0.0751 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.0713**, Adj R² = **0.0543**, F-statistic = **4.21** (p = **3.59e-07**), Residual SE = **16.877** on **768** df, AIC = **6662.4**, BIC = **6732.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.4771** | 6.4697 | ±12.9393 | **+19.549** | **4.18e-85** | *** |
| Education: graduate level (vs college) | -1.0604 | 1.2495 | ±2.4990 | -0.849 | 0.3961 |  |
| **Education: high school or below (vs college)** | **+6.3080** | 2.2600 | ±4.5199 | **+2.791** | **0.0053** | ** |
| Site: UCSD (vs UAB) | +3.1222 | 1.6937 | ±3.3874 | +1.843 | 0.0653 | . |
| **Site: UW (vs UAB)** | **-2.7823** | 1.4132 | ±2.8264 | **-1.969** | **0.0490** | * |
| **Season: spring (vs autumn)** | **+3.5542** | 1.4989 | ±2.9979 | **+2.371** | **0.0177** | * |
| Season: summer (vs autumn) | +3.1384 | 1.6486 | ±3.2971 | +1.904 | 0.0569 | . |
| **Season: winter (vs autumn)** | **+3.7899** | 1.8903 | ±3.7806 | **+2.005** | **0.0450** | * |
| **Age (years)** | **-0.1487** | 0.0682 | ±0.1364 | **-2.180** | **0.0292** | * |
| BMI (kg/m2) | +0.1953 | 0.1102 | ±0.2204 | +1.773 | 0.0763 | . |
| Hypertension | +0.5011 | 1.4734 | ±2.9468 | +0.340 | 0.7338 |  |
| High cholesterol | +1.9445 | 1.3594 | ±2.7187 | +1.430 | 0.1526 |  |
| Kidney disease | -2.0320 | 1.7284 | ±3.4569 | -1.176 | 0.2397 |  |
| Circulatory disease | +0.0149 | 1.7088 | ±3.4175 | +0.009 | 0.9930 |  |
| Any reading < 54 during wear (0/1) | +0.4040 | 1.6179 | ±3.2357 | +0.250 | 0.8028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.0719**, Adj R² = **0.0550**, F-statistic = **4.25** (p = **2.85e-07**), Residual SE = **16.871** on **768** df, AIC = **6661.8**, BIC = **6731.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.8861** | 6.6885 | ±13.3771 | **+18.971** | **2.98e-80** | *** |
| Education: graduate level (vs college) | -1.1336 | 1.2528 | ±2.5057 | -0.905 | 0.3656 |  |
| **Education: high school or below (vs college)** | **+6.2069** | 2.2668 | ±4.5336 | **+2.738** | **0.0062** | ** |
| Site: UCSD (vs UAB) | +3.0135 | 1.7001 | ±3.4001 | +1.773 | 0.0763 | . |
| **Site: UW (vs UAB)** | **-2.9159** | 1.4379 | ±2.8759 | **-2.028** | **0.0426** | * |
| **Season: spring (vs autumn)** | **+3.5180** | 1.4981 | ±2.9962 | **+2.348** | **0.0189** | * |
| Season: summer (vs autumn) | +3.0782 | 1.6528 | ±3.3057 | +1.862 | 0.0626 | . |
| **Season: winter (vs autumn)** | **+3.7958** | 1.8783 | ±3.7566 | **+2.021** | **0.0433** | * |
| **Age (years)** | **-0.1475** | 0.0691 | ±0.1381 | **-2.137** | **0.0326** | * |
| BMI (kg/m2) | +0.1917 | 0.1098 | ±0.2195 | +1.747 | 0.0807 | . |
| Hypertension | +0.5255 | 1.4773 | ±2.9546 | +0.356 | 0.7221 |  |
| High cholesterol | +1.8279 | 1.3464 | ±2.6929 | +1.358 | 0.1746 |  |
| Kidney disease | -2.0301 | 1.7271 | ±3.4542 | -1.175 | 0.2398 |  |
| Circulatory disease | -0.0046 | 1.7105 | ±3.4210 | -0.003 | 0.9979 |  |
| Time < 54 (%) | -0.8603 | 1.3012 | ±2.6024 | -0.661 | 0.5085 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **783**, R² = **0.0720**, Adj R² = **0.0551**, F-statistic = **4.26** (p = **2.81e-07**), Residual SE = **16.870** on **768** df, AIC = **6661.7**, BIC = **6731.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.8660** | 6.6877 | ±13.3754 | **+18.970** | **3.02e-80** | *** |
| Education: graduate level (vs college) | -1.1274 | 1.2526 | ±2.5052 | -0.900 | 0.3681 |  |
| **Education: high school or below (vs college)** | **+6.2009** | 2.2674 | ±4.5347 | **+2.735** | **0.0062** | ** |
| Site: UCSD (vs UAB) | +3.0090 | 1.7001 | ±3.4003 | +1.770 | 0.0767 | . |
| **Site: UW (vs UAB)** | **-2.9316** | 1.4386 | ±2.8771 | **-2.038** | **0.0416** | * |
| **Season: spring (vs autumn)** | **+3.4808** | 1.4982 | ±2.9964 | **+2.323** | **0.0202** | * |
| Season: summer (vs autumn) | +3.0413 | 1.6550 | ±3.3100 | +1.838 | 0.0661 | . |
| **Season: winter (vs autumn)** | **+3.7761** | 1.8752 | ±3.7505 | **+2.014** | **0.0440** | * |
| **Age (years)** | **-0.1476** | 0.0690 | ±0.1381 | **-2.139** | **0.0325** | * |
| BMI (kg/m2) | +0.1933 | 0.1097 | ±0.2193 | +1.763 | 0.0780 | . |
| Hypertension | +0.5325 | 1.4767 | ±2.9533 | +0.361 | 0.7184 |  |
| High cholesterol | +1.8132 | 1.3492 | ±2.6983 | +1.344 | 0.1790 |  |
| Kidney disease | -2.0087 | 1.7280 | ±3.4560 | -1.162 | 0.2451 |  |
| Circulatory disease | -0.0019 | 1.7104 | ±3.4208 | -0.001 | 0.9991 |  |
| Avg. daily time < 54 (%) | -1.0196 | 0.6930 | ±1.3860 | -1.471 | 0.1412 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **783**, R² = **0.0720**, Adj R² = **0.0551**, F-statistic = **4.26** (p = **2.81e-07**), Residual SE = **16.870** on **768** df, AIC = **6661.7**, BIC = **6731.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.8829** | 6.6597 | ±13.3195 | **+19.052** | **6.29e-81** | *** |
| Education: graduate level (vs college) | -1.1407 | 1.2591 | ±2.5183 | -0.906 | 0.3650 |  |
| **Education: high school or below (vs college)** | **+6.2203** | 2.2661 | ±4.5321 | **+2.745** | **0.0061** | ** |
| Site: UCSD (vs UAB) | +2.9884 | 1.6967 | ±3.3933 | +1.761 | 0.0782 | . |
| **Site: UW (vs UAB)** | **-2.9326** | 1.4368 | ±2.8736 | **-2.041** | **0.0412** | * |
| **Season: spring (vs autumn)** | **+3.4777** | 1.4955 | ±2.9910 | **+2.325** | **0.0200** | * |
| Season: summer (vs autumn) | +3.0294 | 1.6465 | ±3.2930 | +1.840 | 0.0658 | . |
| **Season: winter (vs autumn)** | **+3.7251** | 1.8728 | ±3.7457 | **+1.989** | **0.0467** | * |
| **Age (years)** | **-0.1472** | 0.0693 | ±0.1385 | **-2.126** | **0.0335** | * |
| BMI (kg/m2) | +0.1958 | 0.1099 | ±0.2199 | +1.781 | 0.0749 | . |
| Hypertension | +0.5612 | 1.4729 | ±2.9459 | +0.381 | 0.7032 |  |
| High cholesterol | +1.7886 | 1.3607 | ±2.7214 | +1.314 | 0.1887 |  |
| Kidney disease | -1.9743 | 1.7298 | ±3.4597 | -1.141 | 0.2537 |  |
| Circulatory disease | -0.0284 | 1.7146 | ±3.4293 | -0.017 | 0.9868 |  |
| Time 54-69, pooled (%) | -0.4886 | 0.6255 | ±1.2511 | -0.781 | 0.4348 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **783**, R² = **0.0728**, Adj R² = **0.0559**, F-statistic = **4.30** (p = **2.18e-07**), Residual SE = **16.863** on **768** df, AIC = **6661.1**, BIC = **6731.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.9015** | 6.6664 | ±13.3329 | **+19.036** | **8.60e-81** | *** |
| Education: graduate level (vs college) | -1.1758 | 1.2581 | ±2.5163 | -0.935 | 0.3500 |  |
| **Education: high school or below (vs college)** | **+6.1875** | 2.2678 | ±4.5357 | **+2.728** | **0.0064** | ** |
| Site: UCSD (vs UAB) | +2.9430 | 1.6961 | ±3.3922 | +1.735 | 0.0827 | . |
| **Site: UW (vs UAB)** | **-3.0028** | 1.4367 | ±2.8735 | **-2.090** | **0.0366** | * |
| **Season: spring (vs autumn)** | **+3.4545** | 1.4945 | ±2.9890 | **+2.311** | **0.0208** | * |
| Season: summer (vs autumn) | +2.9977 | 1.6455 | ±3.2910 | +1.822 | 0.0685 | . |
| **Season: winter (vs autumn)** | **+3.7313** | 1.8725 | ±3.7451 | **+1.993** | **0.0463** | * |
| **Age (years)** | **-0.1459** | 0.0693 | ±0.1386 | **-2.105** | **0.0353** | * |
| BMI (kg/m2) | +0.1967 | 0.1101 | ±0.2202 | +1.787 | 0.0739 | . |
| Hypertension | +0.5775 | 1.4723 | ±2.9445 | +0.392 | 0.6949 |  |
| High cholesterol | +1.7329 | 1.3611 | ±2.7222 | +1.273 | 0.2030 |  |
| Kidney disease | -1.9630 | 1.7274 | ±3.4547 | -1.136 | 0.2558 |  |
| Circulatory disease | -0.0613 | 1.7121 | ±3.4243 | -0.036 | 0.9714 |  |
| Avg. daily time 54-69 (%) | -0.6477 | 0.5197 | ±1.0394 | -1.246 | 0.2127 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **783**, R² = **0.0723**, Adj R² = **0.0553**, F-statistic = **4.27** (p = **2.57e-07**), Residual SE = **16.868** on **768** df, AIC = **6661.5**, BIC = **6731.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.9701** | 6.6609 | ±13.3218 | **+19.062** | **5.23e-81** | *** |
| Education: graduate level (vs college) | -1.1610 | 1.2590 | ±2.5181 | -0.922 | 0.3565 |  |
| **Education: high school or below (vs college)** | **+6.1914** | 2.2664 | ±4.5328 | **+2.732** | **0.0063** | ** |
| Site: UCSD (vs UAB) | +2.9617 | 1.6986 | ±3.3971 | +1.744 | 0.0812 | . |
| **Site: UW (vs UAB)** | **-2.9685** | 1.4387 | ±2.8773 | **-2.063** | **0.0391** | * |
| **Season: spring (vs autumn)** | **+3.4723** | 1.4959 | ±2.9917 | **+2.321** | **0.0203** | * |
| Season: summer (vs autumn) | +3.0214 | 1.6480 | ±3.2960 | +1.833 | 0.0668 | . |
| **Season: winter (vs autumn)** | **+3.7470** | 1.8740 | ±3.7479 | **+2.000** | **0.0456** | * |
| **Age (years)** | **-0.1467** | 0.0693 | ±0.1385 | **-2.118** | **0.0342** | * |
| BMI (kg/m2) | +0.1939 | 0.1096 | ±0.2193 | +1.768 | 0.0770 | . |
| Hypertension | +0.5573 | 1.4734 | ±2.9468 | +0.378 | 0.7053 |  |
| High cholesterol | +1.7647 | 1.3577 | ±2.7154 | +1.300 | 0.1937 |  |
| Kidney disease | -1.9850 | 1.7290 | ±3.4579 | -1.148 | 0.2509 |  |
| Circulatory disease | -0.0383 | 1.7133 | ±3.4266 | -0.022 | 0.9822 |  |
| Time < 70 (%) | -0.4193 | 0.3908 | ±0.7817 | -1.073 | 0.2834 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **783**, R² = **0.0728**, Adj R² = **0.0559**, F-statistic = **4.31** (p = **2.16e-07**), Residual SE = **16.863** on **768** df, AIC = **6661.1**, BIC = **6731.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.9502** | 6.6671 | ±13.3341 | **+19.041** | **7.75e-81** | *** |
| Education: graduate level (vs college) | -1.1781 | 1.2575 | ±2.5150 | -0.937 | 0.3488 |  |
| **Education: high school or below (vs college)** | **+6.1698** | 2.2682 | ±4.5363 | **+2.720** | **0.0065** | ** |
| Site: UCSD (vs UAB) | +2.9359 | 1.6976 | ±3.3953 | +1.729 | 0.0837 | . |
| **Site: UW (vs UAB)** | **-3.0172** | 1.4388 | ±2.8776 | **-2.097** | **0.0360** | * |
| **Season: spring (vs autumn)** | **+3.4436** | 1.4951 | ±2.9902 | **+2.303** | **0.0213** | * |
| Season: summer (vs autumn) | +2.9882 | 1.6480 | ±3.2960 | +1.813 | 0.0698 | . |
| **Season: winter (vs autumn)** | **+3.7456** | 1.8730 | ±3.7460 | **+2.000** | **0.0455** | * |
| **Age (years)** | **-0.1459** | 0.0692 | ±0.1385 | **-2.107** | **0.0351** | * |
| BMI (kg/m2) | +0.1953 | 0.1098 | ±0.2196 | +1.779 | 0.0753 | . |
| Hypertension | +0.5694 | 1.4734 | ±2.9468 | +0.386 | 0.6992 |  |
| High cholesterol | +1.7272 | 1.3593 | ±2.7187 | +1.271 | 0.2039 |  |
| Kidney disease | -1.9705 | 1.7278 | ±3.4557 | -1.140 | 0.2541 |  |
| Circulatory disease | -0.0560 | 1.7118 | ±3.4235 | -0.033 | 0.9739 |  |
| Avg. daily time < 70 (%) | -0.4940 | 0.3423 | ±0.6846 | -1.443 | 0.1490 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.0802**, Adj R² = **0.0634**, F-statistic = **4.78** (p = **1.74e-08**), Residual SE = **16.796** on **768** df, AIC = **6654.8**, BIC = **6724.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+117.5779** | 7.2659 | ±14.5317 | **+16.182** | **6.73e-59** | *** |
| Education: graduate level (vs college) | -1.3477 | 1.2448 | ±2.4896 | -1.083 | 0.2790 |  |
| **Education: high school or below (vs college)** | **+6.8480** | 2.2694 | ±4.5388 | **+3.018** | **0.0025** | ** |
| Site: UCSD (vs UAB) | +2.7653 | 1.7123 | ±3.4246 | +1.615 | 0.1063 |  |
| **Site: UW (vs UAB)** | **-3.2342** | 1.4451 | ±2.8903 | **-2.238** | **0.0252** | * |
| **Season: spring (vs autumn)** | **+3.5768** | 1.5052 | ±3.0104 | **+2.376** | **0.0175** | * |
| Season: summer (vs autumn) | +2.7724 | 1.6709 | ±3.3417 | +1.659 | 0.0971 | . |
| **Season: winter (vs autumn)** | **+3.7624** | 1.8583 | ±3.7166 | **+2.025** | **0.0429** | * |
| **Age (years)** | **-0.1612** | 0.0695 | ±0.1391 | **-2.319** | **0.0204** | * |
| **BMI (kg/m2)** | **+0.2158** | 0.1086 | ±0.2172 | **+1.988** | **0.0469** | * |
| Hypertension | +0.6731 | 1.4649 | ±2.9297 | +0.460 | 0.6459 |  |
| High cholesterol | +1.8400 | 1.3363 | ±2.6726 | +1.377 | 0.1685 |  |
| Kidney disease | -1.7729 | 1.7255 | ±3.4510 | -1.027 | 0.3042 |  |
| Circulatory disease | +0.2923 | 1.7072 | ±3.4144 | +0.171 | 0.8641 |  |
| **Time 54-250, pooled (%)** | **+0.1023** | 0.0401 | ±0.0802 | **+2.552** | **0.0107** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **783**, R² = **0.0807**, Adj R² = **0.0640**, F-statistic = **4.82** (p = **1.44e-08**), Residual SE = **16.791** on **768** df, AIC = **6654.3**, BIC = **6724.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+117.0630** | 7.2933 | ±14.5866 | **+16.051** | **5.65e-58** | *** |
| Education: graduate level (vs college) | -1.3505 | 1.2450 | ±2.4900 | -1.085 | 0.2780 |  |
| **Education: high school or below (vs college)** | **+6.8656** | 2.2657 | ±4.5314 | **+3.030** | **0.0024** | ** |
| Site: UCSD (vs UAB) | +2.7500 | 1.7120 | ±3.4240 | +1.606 | 0.1082 |  |
| **Site: UW (vs UAB)** | **-3.2329** | 1.4432 | ±2.8865 | **-2.240** | **0.0251** | * |
| **Season: spring (vs autumn)** | **+3.5888** | 1.5052 | ±3.0104 | **+2.384** | **0.0171** | * |
| Season: summer (vs autumn) | +2.7813 | 1.6693 | ±3.3387 | +1.666 | 0.0957 | . |
| **Season: winter (vs autumn)** | **+3.7712** | 1.8571 | ±3.7142 | **+2.031** | **0.0423** | * |
| **Age (years)** | **-0.1602** | 0.0695 | ±0.1390 | **-2.305** | **0.0211** | * |
| **BMI (kg/m2)** | **+0.2170** | 0.1083 | ±0.2166 | **+2.004** | **0.0451** | * |
| Hypertension | +0.6676 | 1.4650 | ±2.9301 | +0.456 | 0.6486 |  |
| High cholesterol | +1.8365 | 1.3361 | ±2.6722 | +1.375 | 0.1693 |  |
| Kidney disease | -1.7392 | 1.7232 | ±3.4464 | -1.009 | 0.3128 |  |
| Circulatory disease | +0.3145 | 1.7100 | ±3.4200 | +0.184 | 0.8541 |  |
| **Avg. daily time 54-250 (%)** | **+0.1065** | 0.0413 | ±0.0825 | **+2.580** | **0.0099** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.0712**, Adj R² = **0.0542**, F-statistic = **4.20** (p = **3.70e-07**), Residual SE = **16.878** on **768** df, AIC = **6662.4**, BIC = **6732.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.6353** | 6.7183 | ±13.4365 | **+18.849** | **2.97e-79** | *** |
| Education: graduate level (vs college) | -1.0707 | 1.2564 | ±2.5127 | -0.852 | 0.3941 |  |
| **Education: high school or below (vs college)** | **+6.2962** | 2.2830 | ±4.5660 | **+2.758** | **0.0058** | ** |
| Site: UCSD (vs UAB) | +3.0948 | 1.6981 | ±3.3962 | +1.823 | 0.0684 | . |
| **Site: UW (vs UAB)** | **-2.8085** | 1.4273 | ±2.8546 | **-1.968** | **0.0491** | * |
| **Season: spring (vs autumn)** | **+3.5560** | 1.4923 | ±2.9846 | **+2.383** | **0.0172** | * |
| Season: summer (vs autumn) | +3.1250 | 1.6504 | ±3.3008 | +1.893 | 0.0583 | . |
| **Season: winter (vs autumn)** | **+3.7657** | 1.8527 | ±3.7055 | **+2.033** | **0.0421** | * |
| **Age (years)** | **-0.1491** | 0.0693 | ±0.1387 | **-2.150** | **0.0316** | * |
| BMI (kg/m2) | +0.1968 | 0.1120 | ±0.2239 | +1.758 | 0.0787 | . |
| Hypertension | +0.5212 | 1.4763 | ±2.9527 | +0.353 | 0.7241 |  |
| High cholesterol | +1.9154 | 1.3420 | ±2.6841 | +1.427 | 0.1535 |  |
| Kidney disease | -2.0125 | 1.7605 | ±3.5211 | -1.143 | 0.2530 |  |
| Circulatory disease | +0.0376 | 1.7093 | ±3.4187 | +0.022 | 0.9825 |  |
| Time 181-250, pooled (%) | -0.0029 | 0.0542 | ±0.1084 | -0.054 | 0.9567 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **783**, R² = **0.0712**, Adj R² = **0.0543**, F-statistic = **4.20** (p = **3.68e-07**), Residual SE = **16.878** on **768** df, AIC = **6662.4**, BIC = **6732.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.6366** | 6.7189 | ±13.4378 | **+18.848** | **3.06e-79** | *** |
| Education: graduate level (vs college) | -1.0689 | 1.2577 | ±2.5153 | -0.850 | 0.3954 |  |
| **Education: high school or below (vs college)** | **+6.3055** | 2.2829 | ±4.5658 | **+2.762** | **0.0057** | ** |
| Site: UCSD (vs UAB) | +3.0889 | 1.7000 | ±3.4000 | +1.817 | 0.0692 | . |
| **Site: UW (vs UAB)** | **-2.8122** | 1.4266 | ±2.8532 | **-1.971** | **0.0487** | * |
| **Season: spring (vs autumn)** | **+3.5608** | 1.4921 | ±2.9843 | **+2.386** | **0.0170** | * |
| Season: summer (vs autumn) | +3.1277 | 1.6505 | ±3.3010 | +1.895 | 0.0581 | . |
| **Season: winter (vs autumn)** | **+3.7699** | 1.8500 | ±3.7001 | **+2.038** | **0.0416** | * |
| **Age (years)** | **-0.1489** | 0.0693 | ±0.1386 | **-2.148** | **0.0317** | * |
| BMI (kg/m2) | +0.1977 | 0.1122 | ±0.2243 | +1.763 | 0.0779 | . |
| Hypertension | +0.5208 | 1.4770 | ±2.9539 | +0.353 | 0.7244 |  |
| High cholesterol | +1.9173 | 1.3424 | ±2.6847 | +1.428 | 0.1532 |  |
| Kidney disease | -2.0051 | 1.7613 | ±3.5225 | -1.138 | 0.2549 |  |
| Circulatory disease | +0.0395 | 1.7085 | ±3.4170 | +0.023 | 0.9815 |  |
| Avg. daily time 181-250 (%) | -0.0050 | 0.0522 | ±0.1045 | -0.095 | 0.9240 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **783**, R² = **0.0753**, Adj R² = **0.0584**, F-statistic = **4.46** (p = **9.39e-08**), Residual SE = **16.841** on **768** df, AIC = **6659.0**, BIC = **6728.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.1502** | 6.7376 | ±13.4751 | **+18.872** | **1.94e-79** | *** |
| Education: graduate level (vs college) | -1.1714 | 1.2395 | ±2.4791 | -0.945 | 0.3447 |  |
| **Education: high school or below (vs college)** | **+6.7140** | 2.2851 | ±4.5702 | **+2.938** | **0.0033** | ** |
| Site: UCSD (vs UAB) | +2.8581 | 1.7069 | ±3.4137 | +1.674 | 0.0940 | . |
| **Site: UW (vs UAB)** | **-3.0447** | 1.4279 | ±2.8558 | **-2.132** | **0.0330** | * |
| **Season: spring (vs autumn)** | **+3.6563** | 1.4914 | ±2.9828 | **+2.452** | **0.0142** | * |
| Season: summer (vs autumn) | +3.0225 | 1.6554 | ±3.3108 | +1.826 | 0.0679 | . |
| **Season: winter (vs autumn)** | **+3.8283** | 1.8573 | ±3.7145 | **+2.061** | **0.0393** | * |
| **Age (years)** | **-0.1506** | 0.0695 | ±0.1390 | **-2.167** | **0.0302** | * |
| **BMI (kg/m2)** | **+0.2238** | 0.1100 | ±0.2199 | **+2.035** | **0.0418** | * |
| Hypertension | +0.5769 | 1.4787 | ±2.9575 | +0.390 | 0.6964 |  |
| High cholesterol | +1.9189 | 1.3434 | ±2.6869 | +1.428 | 0.1532 |  |
| Kidney disease | -1.7616 | 1.7434 | ±3.4869 | -1.010 | 0.3123 |  |
| Circulatory disease | +0.2098 | 1.7082 | ±3.4165 | +0.123 | 0.9022 |  |
| Time > 180 (%) | -0.0458 | 0.0277 | ±0.0554 | -1.654 | 0.0980 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **783**, R² = **0.0755**, Adj R² = **0.0587**, F-statistic = **4.48** (p = **8.62e-08**), Residual SE = **16.838** on **768** df, AIC = **6658.8**, BIC = **6728.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.1119** | 6.7362 | ±13.4724 | **+18.870** | **2.01e-79** | *** |
| Education: graduate level (vs college) | -1.1632 | 1.2406 | ±2.4812 | -0.938 | 0.3484 |  |
| **Education: high school or below (vs college)** | **+6.7368** | 2.2825 | ±4.5651 | **+2.951** | **0.0032** | ** |
| Site: UCSD (vs UAB) | +2.8364 | 1.7081 | ±3.4161 | +1.661 | 0.0968 | . |
| **Site: UW (vs UAB)** | **-3.0550** | 1.4279 | ±2.8559 | **-2.139** | **0.0324** | * |
| **Season: spring (vs autumn)** | **+3.6715** | 1.4909 | ±2.9818 | **+2.463** | **0.0138** | * |
| Season: summer (vs autumn) | +3.0345 | 1.6537 | ±3.3074 | +1.835 | 0.0665 | . |
| **Season: winter (vs autumn)** | **+3.8450** | 1.8542 | ±3.7084 | **+2.074** | **0.0381** | * |
| **Age (years)** | **-0.1503** | 0.0695 | ±0.1390 | **-2.163** | **0.0305** | * |
| **BMI (kg/m2)** | **+0.2249** | 0.1098 | ±0.2196 | **+2.048** | **0.0405** | * |
| Hypertension | +0.5743 | 1.4787 | ±2.9573 | +0.388 | 0.6977 |  |
| High cholesterol | +1.9222 | 1.3436 | ±2.6871 | +1.431 | 0.1525 |  |
| Kidney disease | -1.7388 | 1.7416 | ±3.4832 | -0.998 | 0.3181 |  |
| Circulatory disease | +0.2130 | 1.7086 | ±3.4171 | +0.125 | 0.9008 |  |
| Avg. daily time > 180 (%) | -0.0469 | 0.0275 | ±0.0551 | -1.703 | 0.0886 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **783**, R² = **0.0731**, Adj R² = **0.0562**, F-statistic = **4.33** (p = **1.94e-07**), Residual SE = **16.860** on **768** df, AIC = **6660.8**, BIC = **6730.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.8379** | 6.7435 | ±13.4869 | **+18.809** | **6.37e-79** | *** |
| Education: graduate level (vs college) | -1.2000 | 1.2336 | ±2.4673 | -0.973 | 0.3307 |  |
| **Education: high school or below (vs college)** | **+6.5269** | 2.2746 | ±4.5492 | **+2.869** | **0.0041** | ** |
| Site: UCSD (vs UAB) | +2.9257 | 1.7140 | ±3.4281 | +1.707 | 0.0878 | . |
| **Site: UW (vs UAB)** | **-2.9277** | 1.4247 | ±2.8494 | **-2.055** | **0.0399** | * |
| **Season: spring (vs autumn)** | **+3.6496** | 1.4896 | ±2.9791 | **+2.450** | **0.0143** | * |
| Season: summer (vs autumn) | +3.0396 | 1.6595 | ±3.3191 | +1.832 | 0.0670 | . |
| **Season: winter (vs autumn)** | **+3.8297** | 1.8529 | ±3.7057 | **+2.067** | **0.0387** | * |
| **Age (years)** | **-0.1532** | 0.0699 | ±0.1398 | **-2.193** | **0.0283** | * |
| **BMI (kg/m2)** | **+0.2190** | 0.1099 | ±0.2198 | **+1.992** | **0.0463** | * |
| Hypertension | +0.5370 | 1.4796 | ±2.9591 | +0.363 | 0.7166 |  |
| High cholesterol | +1.9009 | 1.3450 | ±2.6900 | +1.413 | 0.1576 |  |
| Kidney disease | -1.9075 | 1.7423 | ±3.4846 | -1.095 | 0.2736 |  |
| Circulatory disease | +0.1419 | 1.7048 | ±3.4097 | +0.083 | 0.9337 |  |
| Nocturnal time > 180 (%) | -0.0287 | 0.0281 | ±0.0561 | -1.022 | 0.3069 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **783**, R² = **0.0800**, Adj R² = **0.0632**, F-statistic = **4.77** (p = **1.86e-08**), Residual SE = **16.798** on **768** df, AIC = **6655.0**, BIC = **6724.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.7648** | 6.7096 | ±13.4192 | **+19.042** | **7.63e-81** | *** |
| Education: graduate level (vs college) | -1.3374 | 1.2449 | ±2.4897 | -1.074 | 0.2827 |  |
| **Education: high school or below (vs college)** | **+6.8508** | 2.2699 | ±4.5399 | **+3.018** | **0.0025** | ** |
| Site: UCSD (vs UAB) | +2.7794 | 1.7117 | ±3.4234 | +1.624 | 0.1044 |  |
| **Site: UW (vs UAB)** | **-3.2163** | 1.4444 | ±2.8887 | **-2.227** | **0.0260** | * |
| **Season: spring (vs autumn)** | **+3.5802** | 1.5050 | ±3.0100 | **+2.379** | **0.0174** | * |
| Season: summer (vs autumn) | +2.7815 | 1.6704 | ±3.3408 | +1.665 | 0.0959 | . |
| **Season: winter (vs autumn)** | **+3.7583** | 1.8589 | ±3.7177 | **+2.022** | **0.0432** | * |
| **Age (years)** | **-0.1613** | 0.0695 | ±0.1391 | **-2.319** | **0.0204** | * |
| **BMI (kg/m2)** | **+0.2161** | 0.1086 | ±0.2173 | **+1.989** | **0.0467** | * |
| Hypertension | +0.6710 | 1.4651 | ±2.9302 | +0.458 | 0.6470 |  |
| High cholesterol | +1.8509 | 1.3368 | ±2.6737 | +1.385 | 0.1662 |  |
| Kidney disease | -1.7748 | 1.7252 | ±3.4504 | -1.029 | 0.3036 |  |
| Circulatory disease | +0.2939 | 1.7071 | ±3.4141 | +0.172 | 0.8633 |  |
| **Time > 250 (%)** | **-0.1011** | 0.0401 | ±0.0802 | **-2.522** | **0.0117** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 783)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **783**, R² = **0.0805**, Adj R² = **0.0638**, F-statistic = **4.81** (p = **1.53e-08**), Residual SE = **16.792** on **768** df, AIC = **6654.5**, BIC = **6724.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.6751** | 6.7025 | ±13.4049 | **+19.049** | **6.70e-81** | *** |
| Education: graduate level (vs college) | -1.3420 | 1.2450 | ±2.4901 | -1.078 | 0.2811 |  |
| **Education: high school or below (vs college)** | **+6.8686** | 2.2663 | ±4.5327 | **+3.031** | **0.0024** | ** |
| Site: UCSD (vs UAB) | +2.7630 | 1.7115 | ±3.4229 | +1.614 | 0.1064 |  |
| **Site: UW (vs UAB)** | **-3.2156** | 1.4425 | ±2.8851 | **-2.229** | **0.0258** | * |
| **Season: spring (vs autumn)** | **+3.5956** | 1.5049 | ±3.0099 | **+2.389** | **0.0169** | * |
| Season: summer (vs autumn) | +2.7930 | 1.6686 | ±3.3372 | +1.674 | 0.0942 | . |
| **Season: winter (vs autumn)** | **+3.7696** | 1.8576 | ±3.7152 | **+2.029** | **0.0424** | * |
| **Age (years)** | **-0.1603** | 0.0695 | ±0.1390 | **-2.306** | **0.0211** | * |
| **BMI (kg/m2)** | **+0.2171** | 0.1083 | ±0.2166 | **+2.004** | **0.0451** | * |
| Hypertension | +0.6651 | 1.4652 | ±2.9305 | +0.454 | 0.6499 |  |
| High cholesterol | +1.8476 | 1.3367 | ±2.6733 | +1.382 | 0.1669 |  |
| Kidney disease | -1.7433 | 1.7229 | ±3.4458 | -1.012 | 0.3116 |  |
| Circulatory disease | +0.3155 | 1.7099 | ±3.4197 | +0.184 | 0.8536 |  |
| **Avg. daily time > 250 (%)** | **-0.1054** | 0.0413 | ±0.0826 | **-2.553** | **0.0107** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Total analysis base - Home environment

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 120 single-predictor tests; 17 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 120 tests (samples with n >= 500), of which **2** are significant at BH q < 0.05 in the all-tests family and 1 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 783): best single predictor out of sample is **HbA1c** (CV R² 0.164 vs 0.152 for covariates alone, gain +0.012; +0.122 per SD, p = 0.004, q = 0.044). FDR-robust associations (2): SD of daily means (higher outcome, +0.119 per SD, q = 0.017); HbA1c (higher outcome, +0.122 per SD, q = 0.044).
- **Indoor temperature, mean (deg C)** (n = 783): best single predictor out of sample is **%<54 (pooled)** (CV R² 0.281 vs 0.279 for covariates alone, gain +0.001; +0.128 per SD, p = 0.220, q = 0.482). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Indoor relative humidity, mean (%)** (n = 783): best single predictor out of sample is **MAG** (CV R² 0.212 vs 0.213 for covariates alone, gain -0.001; +0.125 per SD, p = 0.564, q = 0.741). No association survives FDR; nominal only: %<54 (pooled) (p = 0.044). Not predictable from glycaemia in this sample.
- **Indoor VOC index, mean** (n = 783): best single predictor out of sample is **%54-250 (daily avg)** (CV R² 0.030 vs 0.024 for covariates alone, gain +0.005; +1.78 per SD, p = 0.010, q = 0.063). No association survives FDR; nominal only: HbA1c (p = 0.010), %54-250 (daily avg) (p = 0.010), %>250 (daily avg) (p = 0.011), %54-250 (pooled) (p = 0.011).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Indoor PM2.5, log(1 + mean ug/m3) (+0.012, via HbA1c); Indoor VOC index, mean (+0.005, via %54-250 (daily avg)); Indoor temperature, mean (deg C) (+0.001, via %<54 (pooled)); Indoor relative humidity, mean (%) (-0.001, via MAG). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** HbA1c (1 FDR-significant / 2 raw-significant of 4); CGM variability (1 FDR-significant / 2 raw-significant of 32); CGM level (0 FDR-significant / 3 raw-significant of 12).
Level metrics: 0 FDR-significant (3 raw); variability metrics: 1 FDR-significant (2 raw); HbA1c alone: 1 FDR-significant (2 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Indoor temperature, mean (%<54 (pooled), ΔAIC -2.5).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
