# Phase 6 model output tables - All (analysis base) - Non-healthy group (T2D non-insulin + T2D insulin) - Home environment

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models. [Index of all model-output files](../../README.md)


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 849; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **849**, R² = **0.1679**, Adj R² = **0.1549**, F-statistic = **12.96** (p = **2.60e-26**), Residual SE = **0.922** on **835** df, AIC = **2286.0**, BIC = **2352.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1741** | 0.3074 | ±0.6148 | **+10.327** | **5.35e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2316** | 0.0653 | ±0.1306 | **-3.547** | **3.90e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4494** | 0.1130 | ±0.2260 | **+3.977** | **6.97e-05** | *** |
| Site: UCSD (vs UAB) | +0.1177 | 0.0748 | ±0.1496 | +1.574 | 0.1156 |  |
| **Site: UW (vs UAB)** | **-0.3126** | 0.0822 | ±0.1645 | **-3.801** | **1.44e-04** | *** |
| Season: spring (vs autumn) | -0.1711 | 0.0886 | ±0.1772 | -1.931 | 0.0535 | . |
| Season: summer (vs autumn) | +0.0442 | 0.0891 | ±0.1783 | +0.496 | 0.6200 |  |
| Season: winter (vs autumn) | +0.0051 | 0.0957 | ±0.1914 | +0.053 | 0.9576 |  |
| **Age (years)** | **-0.0211** | 0.0031 | ±0.0063 | **-6.735** | **1.64e-11** | *** |
| BMI (kg/m2) | +0.0075 | 0.0051 | ±0.0102 | +1.464 | 0.1431 |  |
| Hypertension | +0.0983 | 0.0661 | ±0.1322 | +1.487 | 0.1370 |  |
| High cholesterol | -0.0738 | 0.0669 | ±0.1338 | -1.103 | 0.2699 |  |
| Kidney disease | -0.0557 | 0.0833 | ±0.1667 | -0.669 | 0.5036 |  |
| Circulatory disease | +0.0133 | 0.0787 | ±0.1574 | +0.168 | 0.8663 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **849**, R² = **0.1790**, Adj R² = **0.1652**, F-statistic = **12.99** (p = **5.17e-28**), Residual SE = **0.917** on **834** df, AIC = **2276.6**, BIC = **2347.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.6657** | 0.3407 | ±0.6813 | **+7.825** | **5.08e-15** | *** |
| **Education: graduate level (vs college)** | **-0.2112** | 0.0660 | ±0.1321 | **-3.197** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **+0.4155** | 0.1097 | ±0.2195 | **+3.787** | **1.52e-04** | *** |
| Site: UCSD (vs UAB) | +0.1321 | 0.0747 | ±0.1494 | +1.768 | 0.0770 | . |
| **Site: UW (vs UAB)** | **-0.3006** | 0.0812 | ±0.1624 | **-3.702** | **2.14e-04** | *** |
| Season: spring (vs autumn) | -0.1628 | 0.0880 | ±0.1761 | -1.849 | 0.0644 | . |
| Season: summer (vs autumn) | +0.0558 | 0.0887 | ±0.1773 | +0.629 | 0.5295 |  |
| Season: winter (vs autumn) | -0.0006 | 0.0949 | ±0.1899 | -0.006 | 0.9952 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0062 | **-6.933** | **4.11e-12** | *** |
| BMI (kg/m2) | +0.0062 | 0.0052 | ±0.0104 | +1.191 | 0.2336 |  |
| Hypertension | +0.0975 | 0.0658 | ±0.1317 | +1.481 | 0.1387 |  |
| High cholesterol | -0.0735 | 0.0669 | ±0.1337 | -1.100 | 0.2713 |  |
| Kidney disease | -0.0617 | 0.0828 | ±0.1656 | -0.746 | 0.4559 |  |
| Circulatory disease | +0.0093 | 0.0780 | ±0.1560 | +0.119 | 0.9055 |  |
| **HbA1c (%)** | **+0.0841** | 0.0320 | ±0.0640 | **+2.626** | **0.0086** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **849**, R² = **0.1704**, Adj R² = **0.1565**, F-statistic = **12.24** (p = **2.93e-26**), Residual SE = **0.922** on **834** df, AIC = **2285.4**, BIC = **2356.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9995** | 0.3223 | ±0.6447 | **+9.306** | **1.33e-20** | *** |
| **Education: graduate level (vs college)** | **-0.2231** | 0.0661 | ±0.1322 | **-3.375** | **7.37e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4362** | 0.1111 | ±0.2223 | **+3.925** | **8.66e-05** | *** |
| Site: UCSD (vs UAB) | +0.1264 | 0.0744 | ±0.1488 | +1.698 | 0.0894 | . |
| **Site: UW (vs UAB)** | **-0.3086** | 0.0819 | ±0.1639 | **-3.766** | **1.66e-04** | *** |
| Season: spring (vs autumn) | -0.1739 | 0.0889 | ±0.1779 | -1.955 | 0.0506 | . |
| Season: summer (vs autumn) | +0.0477 | 0.0891 | ±0.1783 | +0.536 | 0.5923 |  |
| Season: winter (vs autumn) | -0.0017 | 0.0956 | ±0.1912 | -0.018 | 0.9856 |  |
| **Age (years)** | **-0.0213** | 0.0031 | ±0.0063 | **-6.799** | **1.05e-11** | *** |
| BMI (kg/m2) | +0.0072 | 0.0052 | ±0.0103 | +1.403 | 0.1606 |  |
| Hypertension | +0.1005 | 0.0660 | ±0.1320 | +1.523 | 0.1278 |  |
| High cholesterol | -0.0709 | 0.0672 | ±0.1343 | -1.055 | 0.2913 |  |
| Kidney disease | -0.0673 | 0.0832 | ±0.1664 | -0.809 | 0.4186 |  |
| Circulatory disease | +0.0118 | 0.0787 | ±0.1575 | +0.149 | 0.8812 |  |
| Mean glucose (mg/dL) | +0.0013 | 0.0010 | ±0.0019 | +1.308 | 0.1910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **849**, R² = **0.1704**, Adj R² = **0.1565**, F-statistic = **12.24** (p = **2.93e-26**), Residual SE = **0.922** on **834** df, AIC = **2285.4**, BIC = **2356.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8256** | 0.3860 | ±0.7720 | **+7.321** | **2.47e-13** | *** |
| **Education: graduate level (vs college)** | **-0.2231** | 0.0661 | ±0.1322 | **-3.375** | **7.37e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4362** | 0.1111 | ±0.2223 | **+3.925** | **8.66e-05** | *** |
| Site: UCSD (vs UAB) | +0.1264 | 0.0744 | ±0.1488 | +1.698 | 0.0894 | . |
| **Site: UW (vs UAB)** | **-0.3086** | 0.0819 | ±0.1639 | **-3.766** | **1.66e-04** | *** |
| Season: spring (vs autumn) | -0.1739 | 0.0889 | ±0.1779 | -1.955 | 0.0506 | . |
| Season: summer (vs autumn) | +0.0477 | 0.0891 | ±0.1783 | +0.536 | 0.5923 |  |
| Season: winter (vs autumn) | -0.0017 | 0.0956 | ±0.1912 | -0.018 | 0.9856 |  |
| **Age (years)** | **-0.0213** | 0.0031 | ±0.0063 | **-6.799** | **1.05e-11** | *** |
| BMI (kg/m2) | +0.0072 | 0.0052 | ±0.0103 | +1.403 | 0.1606 |  |
| Hypertension | +0.1005 | 0.0660 | ±0.1320 | +1.523 | 0.1278 |  |
| High cholesterol | -0.0709 | 0.0672 | ±0.1343 | -1.055 | 0.2913 |  |
| Kidney disease | -0.0673 | 0.0832 | ±0.1664 | -0.809 | 0.4186 |  |
| Circulatory disease | +0.0118 | 0.0787 | ±0.1575 | +0.149 | 0.8812 |  |
| GMI (%) | +0.0525 | 0.0402 | ±0.0803 | +1.308 | 0.1910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **849**, R² = **0.1720**, Adj R² = **0.1581**, F-statistic = **12.38** (p = **1.39e-26**), Residual SE = **0.921** on **834** df, AIC = **2283.8**, BIC = **2355.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9549** | 0.3188 | ±0.6375 | **+9.270** | **1.86e-20** | *** |
| **Education: graduate level (vs college)** | **-0.2208** | 0.0660 | ±0.1321 | **-3.344** | **8.25e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4333** | 0.1108 | ±0.2216 | **+3.911** | **9.21e-05** | *** |
| Site: UCSD (vs UAB) | +0.1282 | 0.0745 | ±0.1489 | +1.722 | 0.0850 | . |
| **Site: UW (vs UAB)** | **-0.3113** | 0.0820 | ±0.1641 | **-3.795** | **1.48e-04** | *** |
| **Season: spring (vs autumn)** | **-0.1766** | 0.0889 | ±0.1779 | **-1.986** | **0.0471** | * |
| Season: summer (vs autumn) | +0.0481 | 0.0890 | ±0.1780 | +0.540 | 0.5892 |  |
| Season: winter (vs autumn) | -0.0046 | 0.0955 | ±0.1910 | -0.049 | 0.9612 |  |
| **Age (years)** | **-0.0210** | 0.0031 | ±0.0062 | **-6.762** | **1.36e-11** | *** |
| BMI (kg/m2) | +0.0068 | 0.0052 | ±0.0104 | +1.307 | 0.1914 |  |
| Hypertension | +0.1023 | 0.0660 | ±0.1320 | +1.551 | 0.1210 |  |
| High cholesterol | -0.0712 | 0.0670 | ±0.1341 | -1.061 | 0.2885 |  |
| Kidney disease | -0.0653 | 0.0826 | ±0.1651 | -0.790 | 0.4294 |  |
| Circulatory disease | +0.0115 | 0.0788 | ±0.1575 | +0.146 | 0.8837 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0016 | 0.0010 | ±0.0019 | +1.646 | 0.0998 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **849**, R² = **0.1714**, Adj R² = **0.1575**, F-statistic = **12.33** (p = **1.83e-26**), Residual SE = **0.921** on **834** df, AIC = **2284.4**, BIC = **2355.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0552** | 0.3070 | ±0.6140 | **+9.952** | **2.47e-23** | *** |
| **Education: graduate level (vs college)** | **-0.2194** | 0.0659 | ±0.1318 | **-3.328** | **8.74e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4313** | 0.1127 | ±0.2254 | **+3.827** | **1.29e-04** | *** |
| Site: UCSD (vs UAB) | +0.1285 | 0.0743 | ±0.1485 | +1.731 | 0.0835 | . |
| **Site: UW (vs UAB)** | **-0.3018** | 0.0817 | ±0.1634 | **-3.695** | **2.20e-04** | *** |
| Season: spring (vs autumn) | -0.1734 | 0.0888 | ±0.1777 | -1.952 | 0.0509 | . |
| Season: summer (vs autumn) | +0.0501 | 0.0893 | ±0.1785 | +0.561 | 0.5749 |  |
| Season: winter (vs autumn) | -0.0012 | 0.0955 | ±0.1909 | -0.012 | 0.9903 |  |
| **Age (years)** | **-0.0217** | 0.0032 | ±0.0063 | **-6.843** | **7.75e-12** | *** |
| BMI (kg/m2) | +0.0074 | 0.0051 | ±0.0102 | +1.458 | 0.1447 |  |
| Hypertension | +0.0993 | 0.0661 | ±0.1322 | +1.503 | 0.1330 |  |
| High cholesterol | -0.0683 | 0.0671 | ±0.1343 | -1.018 | 0.3087 |  |
| Kidney disease | -0.0850 | 0.0822 | ±0.1644 | -1.034 | 0.3010 |  |
| Circulatory disease | +0.0102 | 0.0785 | ±0.1570 | +0.129 | 0.8970 |  |
| Glucose SD, pooled (mg/dL) | +0.0045 | 0.0024 | ±0.0049 | +1.837 | 0.0662 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **849**, R² = **0.1696**, Adj R² = **0.1557**, F-statistic = **12.17** (p = **4.26e-26**), Residual SE = **0.922** on **834** df, AIC = **2286.3**, BIC = **2357.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0844** | 0.3091 | ±0.6182 | **+9.979** | **1.88e-23** | *** |
| **Education: graduate level (vs college)** | **-0.2236** | 0.0660 | ±0.1319 | **-3.390** | **7.00e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4356** | 0.1133 | ±0.2265 | **+3.846** | **1.20e-04** | *** |
| Site: UCSD (vs UAB) | +0.1249 | 0.0744 | ±0.1488 | +1.679 | 0.0931 | . |
| **Site: UW (vs UAB)** | **-0.3059** | 0.0819 | ±0.1638 | **-3.735** | **1.88e-04** | *** |
| Season: spring (vs autumn) | -0.1730 | 0.0888 | ±0.1776 | -1.948 | 0.0514 | . |
| Season: summer (vs autumn) | +0.0492 | 0.0895 | ±0.1789 | +0.550 | 0.5823 |  |
| Season: winter (vs autumn) | +0.0016 | 0.0956 | ±0.1912 | +0.017 | 0.9863 |  |
| **Age (years)** | **-0.0216** | 0.0032 | ±0.0064 | **-6.785** | **1.16e-11** | *** |
| BMI (kg/m2) | +0.0076 | 0.0051 | ±0.0102 | +1.496 | 0.1347 |  |
| Hypertension | +0.0994 | 0.0661 | ±0.1322 | +1.503 | 0.1328 |  |
| High cholesterol | -0.0700 | 0.0671 | ±0.1342 | -1.042 | 0.2972 |  |
| Kidney disease | -0.0769 | 0.0823 | ±0.1645 | -0.935 | 0.3496 |  |
| Circulatory disease | +0.0122 | 0.0786 | ±0.1573 | +0.155 | 0.8770 |  |
| Avg. daily SD (mg/dL) | +0.0036 | 0.0027 | ±0.0055 | +1.318 | 0.1876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **849**, R² = **0.1708**, Adj R² = **0.1569**, F-statistic = **12.27** (p = **2.46e-26**), Residual SE = **0.921** on **834** df, AIC = **2285.1**, BIC = **2356.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9981** | 0.3235 | ±0.6470 | **+9.268** | **1.90e-20** | *** |
| **Education: graduate level (vs college)** | **-0.2235** | 0.0654 | ±0.1307 | **-3.419** | **6.28e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4366** | 0.1144 | ±0.2288 | **+3.816** | **1.36e-04** | *** |
| Site: UCSD (vs UAB) | +0.1252 | 0.0744 | ±0.1489 | +1.681 | 0.0928 | . |
| **Site: UW (vs UAB)** | **-0.3013** | 0.0823 | ±0.1645 | **-3.663** | **2.50e-04** | *** |
| Season: spring (vs autumn) | -0.1702 | 0.0888 | ±0.1777 | -1.915 | 0.0554 | . |
| Season: summer (vs autumn) | +0.0475 | 0.0894 | ±0.1787 | +0.532 | 0.5947 |  |
| Season: winter (vs autumn) | +0.0036 | 0.0958 | ±0.1916 | +0.038 | 0.9698 |  |
| **Age (years)** | **-0.0218** | 0.0032 | ±0.0064 | **-6.837** | **8.09e-12** | *** |
| BMI (kg/m2) | +0.0077 | 0.0051 | ±0.0102 | +1.511 | 0.1309 |  |
| Hypertension | +0.0964 | 0.0662 | ±0.1323 | +1.457 | 0.1450 |  |
| High cholesterol | -0.0693 | 0.0670 | ±0.1340 | -1.034 | 0.3010 |  |
| Kidney disease | -0.0830 | 0.0826 | ±0.1652 | -1.005 | 0.3149 |  |
| Circulatory disease | +0.0101 | 0.0785 | ±0.1569 | +0.129 | 0.8976 |  |
| CV (%) | +0.0096 | 0.0060 | ±0.0119 | +1.604 | 0.1088 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **849**, R² = **0.1714**, Adj R² = **0.1575**, F-statistic = **12.33** (p = **1.84e-26**), Residual SE = **0.921** on **834** df, AIC = **2284.4**, BIC = **2355.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4514** | 0.3477 | ±0.6955 | **+9.925** | **3.24e-23** | *** |
| **Education: graduate level (vs college)** | **-0.2230** | 0.0653 | ±0.1306 | **-3.414** | **6.41e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4340** | 0.1145 | ±0.2291 | **+3.789** | **1.51e-04** | *** |
| Site: UCSD (vs UAB) | +0.1240 | 0.0745 | ±0.1491 | +1.664 | 0.0962 | . |
| **Site: UW (vs UAB)** | **-0.3014** | 0.0824 | ±0.1647 | **-3.659** | **2.53e-04** | *** |
| Season: spring (vs autumn) | -0.1716 | 0.0887 | ±0.1774 | -1.935 | 0.0530 | . |
| Season: summer (vs autumn) | +0.0438 | 0.0891 | ±0.1783 | +0.492 | 0.6230 |  |
| Season: winter (vs autumn) | +0.0016 | 0.0958 | ±0.1915 | +0.017 | 0.9866 |  |
| **Age (years)** | **-0.0219** | 0.0032 | ±0.0064 | **-6.855** | **7.14e-12** | *** |
| BMI (kg/m2) | +0.0077 | 0.0051 | ±0.0101 | +1.511 | 0.1308 |  |
| Hypertension | +0.0963 | 0.0661 | ±0.1321 | +1.458 | 0.1450 |  |
| High cholesterol | -0.0699 | 0.0668 | ±0.1337 | -1.046 | 0.2956 |  |
| Kidney disease | -0.0795 | 0.0826 | ±0.1653 | -0.962 | 0.3361 |  |
| Circulatory disease | +0.0082 | 0.0783 | ±0.1566 | +0.105 | 0.9166 |  |
| Mean / SD ratio | -0.0474 | 0.0250 | ±0.0500 | -1.898 | 0.0576 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **849**, R² = **0.1697**, Adj R² = **0.1558**, F-statistic = **12.18** (p = **4.13e-26**), Residual SE = **0.922** on **834** df, AIC = **2286.2**, BIC = **2357.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.3616** | 0.3402 | ±0.6804 | **+9.881** | **5.05e-23** | *** |
| **Education: graduate level (vs college)** | **-0.2249** | 0.0655 | ±0.1310 | **-3.433** | **5.97e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4390** | 0.1148 | ±0.2295 | **+3.825** | **1.31e-04** | *** |
| Site: UCSD (vs UAB) | +0.1193 | 0.0748 | ±0.1495 | +1.595 | 0.1106 |  |
| **Site: UW (vs UAB)** | **-0.3060** | 0.0825 | ±0.1649 | **-3.711** | **2.06e-04** | *** |
| Season: spring (vs autumn) | -0.1700 | 0.0888 | ±0.1775 | -1.916 | 0.0554 | . |
| Season: summer (vs autumn) | +0.0458 | 0.0894 | ±0.1787 | +0.513 | 0.6081 |  |
| Season: winter (vs autumn) | +0.0044 | 0.0959 | ±0.1918 | +0.046 | 0.9633 |  |
| **Age (years)** | **-0.0217** | 0.0032 | ±0.0064 | **-6.796** | **1.08e-11** | *** |
| BMI (kg/m2) | +0.0078 | 0.0051 | ±0.0102 | +1.536 | 0.1244 |  |
| Hypertension | +0.0967 | 0.0661 | ±0.1323 | +1.462 | 0.1439 |  |
| High cholesterol | -0.0709 | 0.0669 | ±0.1338 | -1.061 | 0.2889 |  |
| Kidney disease | -0.0703 | 0.0827 | ±0.1655 | -0.849 | 0.3957 |  |
| Circulatory disease | +0.0129 | 0.0787 | ±0.1573 | +0.164 | 0.8699 |  |
| Avg. daily mean/SD | -0.0282 | 0.0212 | ±0.0425 | -1.330 | 0.1836 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **849**, R² = **0.1693**, Adj R² = **0.1554**, F-statistic = **12.14** (p = **4.95e-26**), Residual SE = **0.922** on **834** df, AIC = **2286.6**, BIC = **2357.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9923** | 0.3232 | ±0.6464 | **+9.258** | **2.09e-20** | *** |
| **Education: graduate level (vs college)** | **-0.2240** | 0.0658 | ±0.1317 | **-3.402** | **6.68e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4423** | 0.1120 | ±0.2240 | **+3.949** | **7.86e-05** | *** |
| Site: UCSD (vs UAB) | +0.1225 | 0.0744 | ±0.1487 | +1.647 | 0.0996 | . |
| **Site: UW (vs UAB)** | **-0.3014** | 0.0822 | ±0.1645 | **-3.665** | **2.47e-04** | *** |
| Season: spring (vs autumn) | -0.1712 | 0.0888 | ±0.1776 | -1.927 | 0.0539 | . |
| Season: summer (vs autumn) | +0.0500 | 0.0887 | ±0.1774 | +0.564 | 0.5729 |  |
| Season: winter (vs autumn) | +0.0052 | 0.0956 | ±0.1912 | +0.054 | 0.9566 |  |
| **Age (years)** | **-0.0210** | 0.0031 | ±0.0062 | **-6.728** | **1.72e-11** | *** |
| BMI (kg/m2) | +0.0074 | 0.0051 | ±0.0102 | +1.450 | 0.1471 |  |
| Hypertension | +0.1000 | 0.0660 | ±0.1320 | +1.515 | 0.1297 |  |
| High cholesterol | -0.0721 | 0.0670 | ±0.1340 | -1.076 | 0.2820 |  |
| Kidney disease | -0.0659 | 0.0842 | ±0.1684 | -0.782 | 0.4340 |  |
| Circulatory disease | +0.0136 | 0.0788 | ±0.1577 | +0.172 | 0.8632 |  |
| MAG (mg/dL/h) | +0.0040 | 0.0033 | ±0.0066 | +1.203 | 0.2290 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **849**, R² = **0.1697**, Adj R² = **0.1557**, F-statistic = **12.17** (p = **4.16e-26**), Residual SE = **0.922** on **834** df, AIC = **2286.2**, BIC = **2357.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0460** | 0.3152 | ±0.6305 | **+9.662** | **4.36e-22** | *** |
| **Education: graduate level (vs college)** | **-0.2229** | 0.0661 | ±0.1323 | **-3.370** | **7.50e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4364** | 0.1131 | ±0.2262 | **+3.858** | **1.14e-04** | *** |
| Site: UCSD (vs UAB) | +0.1258 | 0.0742 | ±0.1485 | +1.694 | 0.0902 | . |
| **Site: UW (vs UAB)** | **-0.3059** | 0.0820 | ±0.1640 | **-3.731** | **1.91e-04** | *** |
| Season: spring (vs autumn) | -0.1738 | 0.0888 | ±0.1776 | -1.957 | 0.0503 | . |
| Season: summer (vs autumn) | +0.0470 | 0.0893 | ±0.1786 | +0.527 | 0.5983 |  |
| Season: winter (vs autumn) | +0.0010 | 0.0956 | ±0.1912 | +0.010 | 0.9916 |  |
| **Age (years)** | **-0.0215** | 0.0032 | ±0.0063 | **-6.796** | **1.08e-11** | *** |
| BMI (kg/m2) | +0.0078 | 0.0051 | ±0.0102 | +1.516 | 0.1296 |  |
| Hypertension | +0.1014 | 0.0660 | ±0.1320 | +1.536 | 0.1245 |  |
| High cholesterol | -0.0712 | 0.0670 | ±0.1341 | -1.063 | 0.2879 |  |
| Kidney disease | -0.0765 | 0.0823 | ±0.1645 | -0.930 | 0.3526 |  |
| Circulatory disease | +0.0114 | 0.0787 | ±0.1575 | +0.145 | 0.8845 |  |
| Avg. daily range (mg/dL) | +0.0010 | 0.0008 | ±0.0015 | +1.353 | 0.1762 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **849**, R² = **0.1797**, Adj R² = **0.1660**, F-statistic = **13.05** (p = **3.63e-28**), Residual SE = **0.916** on **834** df, AIC = **2275.9**, BIC = **2347.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0450** | 0.3004 | ±0.6009 | **+10.135** | **3.86e-24** | *** |
| **Education: graduate level (vs college)** | **-0.2060** | 0.0656 | ±0.1312 | **-3.141** | **0.0017** | ** |
| **Education: high school or below (vs college)** | **+0.4318** | 0.1106 | ±0.2213 | **+3.903** | **9.50e-05** | *** |
| Site: UCSD (vs UAB) | +0.1331 | 0.0742 | ±0.1484 | +1.795 | 0.0727 | . |
| **Site: UW (vs UAB)** | **-0.2935** | 0.0811 | ±0.1621 | **-3.620** | **2.94e-04** | *** |
| Season: spring (vs autumn) | -0.1703 | 0.0885 | ±0.1769 | -1.925 | 0.0542 | . |
| Season: summer (vs autumn) | +0.0435 | 0.0888 | ±0.1777 | +0.490 | 0.6240 |  |
| Season: winter (vs autumn) | -0.0091 | 0.0947 | ±0.1895 | -0.096 | 0.9236 |  |
| **Age (years)** | **-0.0212** | 0.0031 | ±0.0062 | **-6.812** | **9.65e-12** | *** |
| BMI (kg/m2) | +0.0065 | 0.0051 | ±0.0102 | +1.279 | 0.2008 |  |
| Hypertension | +0.0945 | 0.0660 | ±0.1320 | +1.432 | 0.1521 |  |
| High cholesterol | -0.0690 | 0.0667 | ±0.1334 | -1.034 | 0.3009 |  |
| Kidney disease | -0.0887 | 0.0815 | ±0.1629 | -1.089 | 0.2761 |  |
| Circulatory disease | -0.0064 | 0.0781 | ±0.1562 | -0.082 | 0.9349 |  |
| **SD of daily means (mg/dL)** | **+0.0137** | 0.0044 | ±0.0089 | **+3.084** | **0.0020** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **849**, R² = **0.1731**, Adj R² = **0.1593**, F-statistic = **12.47** (p = **8.20e-27**), Residual SE = **0.920** on **834** df, AIC = **2282.7**, BIC = **2353.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4321** | 0.3454 | ±0.6907 | **+9.938** | **2.86e-23** | *** |
| **Education: graduate level (vs college)** | **-0.2188** | 0.0658 | ±0.1316 | **-3.325** | **8.83e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4287** | 0.1109 | ±0.2218 | **+3.866** | **1.11e-04** | *** |
| Site: UCSD (vs UAB) | +0.1350 | 0.0741 | ±0.1482 | +1.821 | 0.0686 | . |
| **Site: UW (vs UAB)** | **-0.3050** | 0.0817 | ±0.1635 | **-3.732** | **1.90e-04** | *** |
| Season: spring (vs autumn) | -0.1735 | 0.0888 | ±0.1777 | -1.953 | 0.0508 | . |
| Season: summer (vs autumn) | +0.0497 | 0.0889 | ±0.1777 | +0.559 | 0.5764 |  |
| Season: winter (vs autumn) | -0.0044 | 0.0953 | ±0.1907 | -0.046 | 0.9633 |  |
| **Age (years)** | **-0.0216** | 0.0031 | ±0.0063 | **-6.880** | **5.99e-12** | *** |
| BMI (kg/m2) | +0.0070 | 0.0052 | ±0.0103 | +1.366 | 0.1720 |  |
| Hypertension | +0.1047 | 0.0660 | ±0.1321 | +1.585 | 0.1130 |  |
| High cholesterol | -0.0674 | 0.0672 | ±0.1344 | -1.003 | 0.3161 |  |
| Kidney disease | -0.0752 | 0.0829 | ±0.1658 | -0.907 | 0.3643 |  |
| Circulatory disease | +0.0095 | 0.0783 | ±0.1566 | +0.121 | 0.9033 |  |
| **Time in range 70-180, pooled (%)** | **-0.0029** | 0.0014 | ±0.0029 | **-2.024** | **0.0430** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **849**, R² = **0.1731**, Adj R² = **0.1592**, F-statistic = **12.47** (p = **8.27e-27**), Residual SE = **0.920** on **834** df, AIC = **2282.7**, BIC = **2353.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4334** | 0.3459 | ±0.6918 | **+9.926** | **3.20e-23** | *** |
| **Education: graduate level (vs college)** | **-0.2193** | 0.0658 | ±0.1316 | **-3.333** | **8.58e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4281** | 0.1108 | ±0.2217 | **+3.862** | **1.13e-04** | *** |
| Site: UCSD (vs UAB) | +0.1355 | 0.0741 | ±0.1481 | +1.829 | 0.0674 | . |
| **Site: UW (vs UAB)** | **-0.3051** | 0.0817 | ±0.1635 | **-3.732** | **1.90e-04** | *** |
| Season: spring (vs autumn) | -0.1740 | 0.0888 | ±0.1777 | -1.959 | 0.0501 | . |
| Season: summer (vs autumn) | +0.0488 | 0.0889 | ±0.1777 | +0.549 | 0.5833 |  |
| Season: winter (vs autumn) | -0.0054 | 0.0953 | ±0.1907 | -0.057 | 0.9546 |  |
| **Age (years)** | **-0.0216** | 0.0031 | ±0.0063 | **-6.883** | **5.88e-12** | *** |
| BMI (kg/m2) | +0.0070 | 0.0052 | ±0.0103 | +1.362 | 0.1731 |  |
| Hypertension | +0.1048 | 0.0661 | ±0.1322 | +1.586 | 0.1127 |  |
| High cholesterol | -0.0676 | 0.0672 | ±0.1344 | -1.006 | 0.3146 |  |
| Kidney disease | -0.0758 | 0.0828 | ±0.1657 | -0.916 | 0.3598 |  |
| Circulatory disease | +0.0095 | 0.0783 | ±0.1566 | +0.121 | 0.9034 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0029** | 0.0014 | ±0.0029 | **-2.023** | **0.0430** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.1714**, Adj R² = **0.1575**, F-statistic = **12.32** (p = **1.89e-26**), Residual SE = **0.921** on **834** df, AIC = **2284.5**, BIC = **2355.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1155** | 0.3054 | ±0.6109 | **+10.200** | **1.98e-24** | *** |
| **Education: graduate level (vs college)** | **-0.2321** | 0.0655 | ±0.1310 | **-3.545** | **3.93e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4576** | 0.1128 | ±0.2256 | **+4.057** | **4.98e-05** | *** |
| Site: UCSD (vs UAB) | +0.1285 | 0.0746 | ±0.1492 | +1.723 | 0.0848 | . |
| **Site: UW (vs UAB)** | **-0.2997** | 0.0827 | ±0.1653 | **-3.626** | **2.88e-04** | *** |
| Season: spring (vs autumn) | -0.1701 | 0.0887 | ±0.1774 | -1.918 | 0.0551 | . |
| Season: summer (vs autumn) | +0.0479 | 0.0886 | ±0.1773 | +0.540 | 0.5893 |  |
| Season: winter (vs autumn) | +0.0144 | 0.0955 | ±0.1910 | +0.151 | 0.8798 |  |
| **Age (years)** | **-0.0206** | 0.0031 | ±0.0063 | **-6.565** | **5.22e-11** | *** |
| BMI (kg/m2) | +0.0070 | 0.0051 | ±0.0102 | +1.367 | 0.1716 |  |
| Hypertension | +0.0908 | 0.0658 | ±0.1317 | +1.379 | 0.1680 |  |
| High cholesterol | -0.0669 | 0.0670 | ±0.1341 | -0.999 | 0.3179 |  |
| Kidney disease | -0.0529 | 0.0832 | ±0.1665 | -0.635 | 0.5253 |  |
| Circulatory disease | +0.0049 | 0.0790 | ±0.1579 | +0.062 | 0.9509 |  |
| Any reading < 54 during wear (0/1) | +0.1365 | 0.0786 | ±0.1571 | +1.737 | 0.0824 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.1801**, Adj R² = **0.1664**, F-statistic = **13.09** (p = **3.00e-28**), Residual SE = **0.916** on **834** df, AIC = **2275.4**, BIC = **2346.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1318** | 0.3055 | ±0.6111 | **+10.250** | **1.19e-24** | *** |
| **Education: graduate level (vs college)** | **-0.2246** | 0.0651 | ±0.1302 | **-3.449** | **5.64e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4675** | 0.1131 | ±0.2262 | **+4.133** | **3.57e-05** | *** |
| Site: UCSD (vs UAB) | +0.1453 | 0.0746 | ±0.1491 | +1.949 | 0.0513 | . |
| **Site: UW (vs UAB)** | **-0.2806** | 0.0823 | ±0.1647 | **-3.408** | **6.54e-04** | *** |
| Season: spring (vs autumn) | -0.1611 | 0.0890 | ±0.1780 | -1.810 | 0.0703 | . |
| Season: summer (vs autumn) | +0.0498 | 0.0876 | ±0.1752 | +0.568 | 0.5699 |  |
| Season: winter (vs autumn) | +0.0153 | 0.0954 | ±0.1907 | +0.161 | 0.8724 |  |
| **Age (years)** | **-0.0209** | 0.0031 | ±0.0063 | **-6.650** | **2.93e-11** | *** |
| BMI (kg/m2) | +0.0069 | 0.0049 | ±0.0098 | +1.393 | 0.1637 |  |
| Hypertension | +0.0920 | 0.0667 | ±0.1334 | +1.380 | 0.1677 |  |
| High cholesterol | -0.0694 | 0.0666 | ±0.1333 | -1.041 | 0.2979 |  |
| Kidney disease | -0.0489 | 0.0822 | ±0.1645 | -0.595 | 0.5518 |  |
| Circulatory disease | -0.0064 | 0.0779 | ±0.1558 | -0.082 | 0.9347 |  |
| **Time < 54 (%)** | **+0.2665** | 0.0959 | ±0.1918 | **+2.779** | **0.0055** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.1816**, Adj R² = **0.1679**, F-statistic = **13.22** (p = **1.48e-28**), Residual SE = **0.915** on **834** df, AIC = **2273.9**, BIC = **2345.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1496** | 0.3036 | ±0.6073 | **+10.373** | **3.31e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2213** | 0.0646 | ±0.1292 | **-3.427** | **6.11e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4647** | 0.1129 | ±0.2257 | **+4.118** | **3.83e-05** | *** |
| Site: UCSD (vs UAB) | +0.1411 | 0.0742 | ±0.1485 | +1.901 | 0.0573 | . |
| **Site: UW (vs UAB)** | **-0.2859** | 0.0818 | ±0.1636 | **-3.494** | **4.76e-04** | *** |
| Season: spring (vs autumn) | -0.1546 | 0.0887 | ±0.1774 | -1.743 | 0.0813 | . |
| Season: summer (vs autumn) | +0.0505 | 0.0879 | ±0.1759 | +0.574 | 0.5656 |  |
| Season: winter (vs autumn) | +0.0139 | 0.0957 | ±0.1913 | +0.145 | 0.8848 |  |
| **Age (years)** | **-0.0213** | 0.0031 | ±0.0063 | **-6.773** | **1.26e-11** | *** |
| BMI (kg/m2) | +0.0071 | 0.0049 | ±0.0099 | +1.445 | 0.1485 |  |
| Hypertension | +0.0939 | 0.0664 | ±0.1327 | +1.415 | 0.1572 |  |
| High cholesterol | -0.0653 | 0.0667 | ±0.1333 | -0.980 | 0.3270 |  |
| Kidney disease | -0.0527 | 0.0818 | ±0.1636 | -0.644 | 0.5194 |  |
| Circulatory disease | -0.0051 | 0.0787 | ±0.1575 | -0.064 | 0.9488 |  |
| Avg. daily time < 54 (%) | +0.2695 | 0.1462 | ±0.2923 | +1.844 | 0.0652 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.1853**, Adj R² = **0.1716**, F-statistic = **13.55** (p = **2.59e-29**), Residual SE = **0.913** on **834** df, AIC = **2270.1**, BIC = **2341.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1442** | 0.3042 | ±0.6085 | **+10.335** | **4.88e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2176** | 0.0646 | ±0.1292 | **-3.367** | **7.59e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4498** | 0.1134 | ±0.2267 | **+3.968** | **7.26e-05** | *** |
| Site: UCSD (vs UAB) | +0.1420 | 0.0743 | ±0.1486 | +1.910 | 0.0561 | . |
| **Site: UW (vs UAB)** | **-0.2883** | 0.0820 | ±0.1641 | **-3.514** | **4.41e-04** | *** |
| Season: spring (vs autumn) | -0.1505 | 0.0888 | ±0.1776 | -1.696 | 0.0900 | . |
| Season: summer (vs autumn) | +0.0579 | 0.0874 | ±0.1747 | +0.663 | 0.5075 |  |
| Season: winter (vs autumn) | +0.0244 | 0.0952 | ±0.1903 | +0.257 | 0.7975 |  |
| **Age (years)** | **-0.0216** | 0.0031 | ±0.0063 | **-6.891** | **5.52e-12** | *** |
| BMI (kg/m2) | +0.0071 | 0.0050 | ±0.0099 | +1.422 | 0.1549 |  |
| Hypertension | +0.0947 | 0.0662 | ±0.1325 | +1.429 | 0.1529 |  |
| High cholesterol | -0.0709 | 0.0664 | ±0.1328 | -1.068 | 0.2857 |  |
| Kidney disease | -0.0566 | 0.0828 | ±0.1655 | -0.684 | 0.4942 |  |
| Circulatory disease | +0.0025 | 0.0774 | ±0.1548 | +0.032 | 0.9745 |  |
| **Time 54-69, pooled (%)** | **+0.0898** | 0.0325 | ±0.0650 | **+2.762** | **0.0057** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **849**, R² = **0.1858**, Adj R² = **0.1721**, F-statistic = **13.59** (p = **2.05e-29**), Residual SE = **0.913** on **834** df, AIC = **2269.6**, BIC = **2340.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1613** | 0.3040 | ±0.6079 | **+10.400** | **2.47e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2164** | 0.0644 | ±0.1289 | **-3.358** | **7.85e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4476** | 0.1135 | ±0.2271 | **+3.943** | **8.06e-05** | *** |
| Site: UCSD (vs UAB) | +0.1400 | 0.0743 | ±0.1486 | +1.884 | 0.0596 | . |
| **Site: UW (vs UAB)** | **-0.2889** | 0.0819 | ±0.1638 | **-3.528** | **4.18e-04** | *** |
| Season: spring (vs autumn) | -0.1514 | 0.0887 | ±0.1774 | -1.707 | 0.0879 | . |
| Season: summer (vs autumn) | +0.0563 | 0.0874 | ±0.1747 | +0.644 | 0.5195 |  |
| Season: winter (vs autumn) | +0.0227 | 0.0951 | ±0.1902 | +0.239 | 0.8114 |  |
| **Age (years)** | **-0.0218** | 0.0031 | ±0.0063 | **-6.955** | **3.54e-12** | *** |
| BMI (kg/m2) | +0.0071 | 0.0050 | ±0.0099 | +1.421 | 0.1553 |  |
| Hypertension | +0.0947 | 0.0662 | ±0.1324 | +1.431 | 0.1524 |  |
| High cholesterol | -0.0698 | 0.0665 | ±0.1329 | -1.051 | 0.2933 |  |
| Kidney disease | -0.0548 | 0.0822 | ±0.1644 | -0.666 | 0.5053 |  |
| Circulatory disease | +0.0046 | 0.0774 | ±0.1549 | +0.060 | 0.9522 |  |
| **Avg. daily time 54-69 (%)** | **+0.0884** | 0.0326 | ±0.0651 | **+2.715** | **0.0066** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **849**, R² = **0.1861**, Adj R² = **0.1724**, F-statistic = **13.62** (p = **1.74e-29**), Residual SE = **0.913** on **834** df, AIC = **2269.3**, BIC = **2340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1368** | 0.3039 | ±0.6079 | **+10.321** | **5.68e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2177** | 0.0646 | ±0.1293 | **-3.369** | **7.56e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4549** | 0.1134 | ±0.2268 | **+4.011** | **6.06e-05** | *** |
| **Site: UCSD (vs UAB)** | **+0.1461** | 0.0743 | ±0.1486 | **+1.966** | **0.0492** | * |
| **Site: UW (vs UAB)** | **-0.2829** | 0.0821 | ±0.1642 | **-3.446** | **5.68e-04** | *** |
| Season: spring (vs autumn) | -0.1508 | 0.0888 | ±0.1777 | -1.698 | 0.0896 | . |
| Season: summer (vs autumn) | +0.0574 | 0.0871 | ±0.1743 | +0.659 | 0.5101 |  |
| Season: winter (vs autumn) | +0.0244 | 0.0951 | ±0.1902 | +0.256 | 0.7979 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0063 | **-6.849** | **7.46e-12** | *** |
| BMI (kg/m2) | +0.0069 | 0.0049 | ±0.0099 | +1.407 | 0.1593 |  |
| Hypertension | +0.0934 | 0.0663 | ±0.1327 | +1.409 | 0.1589 |  |
| High cholesterol | -0.0701 | 0.0663 | ±0.1327 | -1.056 | 0.2910 |  |
| Kidney disease | -0.0545 | 0.0824 | ±0.1648 | -0.661 | 0.5084 |  |
| Circulatory disease | -0.0015 | 0.0773 | ±0.1546 | -0.019 | 0.9848 |  |
| **Time < 70 (%)** | **+0.0760** | 0.0255 | ±0.0511 | **+2.977** | **0.0029** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **849**, R² = **0.1871**, Adj R² = **0.1734**, F-statistic = **13.71** (p = **1.10e-29**), Residual SE = **0.912** on **834** df, AIC = **2268.3**, BIC = **2339.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1563** | 0.3032 | ±0.6065 | **+10.408** | **2.28e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2157** | 0.0643 | ±0.1287 | **-3.352** | **8.02e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4522** | 0.1135 | ±0.2270 | **+3.984** | **6.78e-05** | *** |
| Site: UCSD (vs UAB) | +0.1434 | 0.0742 | ±0.1483 | +1.933 | 0.0532 | . |
| **Site: UW (vs UAB)** | **-0.2848** | 0.0817 | ±0.1635 | **-3.484** | **4.95e-04** | *** |
| Season: spring (vs autumn) | -0.1496 | 0.0887 | ±0.1774 | -1.686 | 0.0917 | . |
| Season: summer (vs autumn) | +0.0563 | 0.0872 | ±0.1743 | +0.646 | 0.5182 |  |
| Season: winter (vs autumn) | +0.0226 | 0.0951 | ±0.1901 | +0.238 | 0.8119 |  |
| **Age (years)** | **-0.0218** | 0.0031 | ±0.0063 | **-6.934** | **4.08e-12** | *** |
| BMI (kg/m2) | +0.0070 | 0.0049 | ±0.0099 | +1.422 | 0.1549 |  |
| Hypertension | +0.0940 | 0.0662 | ±0.1325 | +1.419 | 0.1558 |  |
| High cholesterol | -0.0680 | 0.0664 | ±0.1329 | -1.024 | 0.3058 |  |
| Kidney disease | -0.0540 | 0.0819 | ±0.1637 | -0.660 | 0.5092 |  |
| Circulatory disease | +0.0007 | 0.0774 | ±0.1548 | +0.010 | 0.9924 |  |
| **Avg. daily time < 70 (%)** | **+0.0757** | 0.0265 | ±0.0529 | **+2.861** | **0.0042** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.1722**, Adj R² = **0.1583**, F-statistic = **12.40** (p = **1.26e-26**), Residual SE = **0.921** on **834** df, AIC = **2283.6**, BIC = **2354.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.5693** | 0.4058 | ±0.8116 | **+8.795** | **1.43e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2182** | 0.0663 | ±0.1326 | **-3.291** | **0.0010** | ** |
| **Education: high school or below (vs college)** | **+0.4328** | 0.1105 | ±0.2210 | **+3.916** | **9.00e-05** | *** |
| Site: UCSD (vs UAB) | +0.1298 | 0.0744 | ±0.1488 | +1.746 | 0.0809 | . |
| **Site: UW (vs UAB)** | **-0.3000** | 0.0816 | ±0.1632 | **-3.675** | **2.38e-04** | *** |
| Season: spring (vs autumn) | -0.1689 | 0.0889 | ±0.1777 | -1.900 | 0.0574 | . |
| Season: summer (vs autumn) | +0.0580 | 0.0890 | ±0.1779 | +0.651 | 0.5147 |  |
| Season: winter (vs autumn) | +0.0030 | 0.0954 | ±0.1908 | +0.031 | 0.9752 |  |
| **Age (years)** | **-0.0209** | 0.0031 | ±0.0062 | **-6.709** | **1.96e-11** | *** |
| BMI (kg/m2) | +0.0072 | 0.0052 | ±0.0103 | +1.395 | 0.1630 |  |
| Hypertension | +0.0967 | 0.0662 | ±0.1324 | +1.461 | 0.1439 |  |
| High cholesterol | -0.0703 | 0.0672 | ±0.1343 | -1.046 | 0.2954 |  |
| Kidney disease | -0.0687 | 0.0837 | ±0.1674 | -0.821 | 0.4114 |  |
| Circulatory disease | +0.0105 | 0.0787 | ±0.1574 | +0.134 | 0.8937 |  |
| Time 54-250, pooled (%) | -0.0044 | 0.0027 | ±0.0055 | -1.591 | 0.1115 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.1723**, Adj R² = **0.1584**, F-statistic = **12.40** (p = **1.21e-26**), Residual SE = **0.920** on **834** df, AIC = **2283.5**, BIC = **2354.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.5824** | 0.4084 | ±0.8168 | **+8.772** | **1.75e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2182** | 0.0663 | ±0.1326 | **-3.292** | **9.95e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4327** | 0.1105 | ±0.2210 | **+3.916** | **9.02e-05** | *** |
| Site: UCSD (vs UAB) | +0.1301 | 0.0743 | ±0.1487 | +1.751 | 0.0800 | . |
| **Site: UW (vs UAB)** | **-0.3004** | 0.0816 | ±0.1632 | **-3.680** | **2.33e-04** | *** |
| Season: spring (vs autumn) | -0.1695 | 0.0889 | ±0.1778 | -1.908 | 0.0565 | . |
| Season: summer (vs autumn) | +0.0571 | 0.0889 | ±0.1779 | +0.642 | 0.5208 |  |
| Season: winter (vs autumn) | +0.0022 | 0.0954 | ±0.1908 | +0.023 | 0.9818 |  |
| **Age (years)** | **-0.0210** | 0.0031 | ±0.0062 | **-6.726** | **1.74e-11** | *** |
| BMI (kg/m2) | +0.0072 | 0.0052 | ±0.0103 | +1.392 | 0.1640 |  |
| Hypertension | +0.0970 | 0.0662 | ±0.1324 | +1.466 | 0.1426 |  |
| High cholesterol | -0.0702 | 0.0671 | ±0.1343 | -1.045 | 0.2958 |  |
| Kidney disease | -0.0698 | 0.0836 | ±0.1673 | -0.834 | 0.4042 |  |
| Circulatory disease | +0.0100 | 0.0788 | ±0.1575 | +0.127 | 0.8992 |  |
| Avg. daily time 54-250 (%) | -0.0044 | 0.0028 | ±0.0055 | -1.614 | 0.1065 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.1695**, Adj R² = **0.1556**, F-statistic = **12.16** (p = **4.49e-26**), Residual SE = **0.922** on **834** df, AIC = **2286.4**, BIC = **2357.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1695** | 0.3053 | ±0.6105 | **+10.383** | **2.96e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2285** | 0.0654 | ±0.1308 | **-3.496** | **4.73e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4407** | 0.1130 | ±0.2260 | **+3.900** | **9.61e-05** | *** |
| Site: UCSD (vs UAB) | +0.1253 | 0.0745 | ±0.1491 | +1.682 | 0.0926 | . |
| **Site: UW (vs UAB)** | **-0.3141** | 0.0823 | ±0.1646 | **-3.816** | **1.36e-04** | *** |
| **Season: spring (vs autumn)** | **-0.1753** | 0.0888 | ±0.1776 | **-1.974** | **0.0484** | * |
| Season: summer (vs autumn) | +0.0404 | 0.0894 | ±0.1788 | +0.452 | 0.6514 |  |
| Season: winter (vs autumn) | -0.0028 | 0.0962 | ±0.1924 | -0.029 | 0.9766 |  |
| **Age (years)** | **-0.0216** | 0.0032 | ±0.0064 | **-6.752** | **1.46e-11** | *** |
| BMI (kg/m2) | +0.0073 | 0.0051 | ±0.0103 | +1.415 | 0.1572 |  |
| Hypertension | +0.1052 | 0.0656 | ±0.1312 | +1.603 | 0.1089 |  |
| High cholesterol | -0.0702 | 0.0671 | ±0.1341 | -1.046 | 0.2954 |  |
| Kidney disease | -0.0656 | 0.0827 | ±0.1653 | -0.793 | 0.4278 |  |
| Circulatory disease | +0.0118 | 0.0785 | ±0.1570 | +0.151 | 0.8802 |  |
| Time 181-250, pooled (%) | +0.0027 | 0.0021 | ±0.0043 | +1.242 | 0.2144 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **849**, R² = **0.1695**, Adj R² = **0.1555**, F-statistic = **12.15** (p = **4.62e-26**), Residual SE = **0.922** on **834** df, AIC = **2286.4**, BIC = **2357.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1689** | 0.3053 | ±0.6105 | **+10.381** | **3.01e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2288** | 0.0654 | ±0.1308 | **-3.500** | **4.65e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4402** | 0.1129 | ±0.2259 | **+3.898** | **9.71e-05** | *** |
| Site: UCSD (vs UAB) | +0.1257 | 0.0745 | ±0.1490 | +1.687 | 0.0917 | . |
| **Site: UW (vs UAB)** | **-0.3137** | 0.0823 | ±0.1646 | **-3.811** | **1.38e-04** | *** |
| **Season: spring (vs autumn)** | **-0.1752** | 0.0888 | ±0.1776 | **-1.972** | **0.0486** | * |
| Season: summer (vs autumn) | +0.0404 | 0.0894 | ±0.1788 | +0.452 | 0.6511 |  |
| Season: winter (vs autumn) | -0.0031 | 0.0962 | ±0.1924 | -0.032 | 0.9745 |  |
| **Age (years)** | **-0.0216** | 0.0032 | ±0.0064 | **-6.749** | **1.49e-11** | *** |
| BMI (kg/m2) | +0.0073 | 0.0051 | ±0.0103 | +1.413 | 0.1575 |  |
| Hypertension | +0.1049 | 0.0657 | ±0.1314 | +1.597 | 0.1104 |  |
| High cholesterol | -0.0705 | 0.0671 | ±0.1341 | -1.051 | 0.2934 |  |
| Kidney disease | -0.0655 | 0.0826 | ±0.1653 | -0.793 | 0.4280 |  |
| Circulatory disease | +0.0121 | 0.0785 | ±0.1570 | +0.154 | 0.8778 |  |
| Avg. daily time 181-250 (%) | +0.0026 | 0.0021 | ±0.0042 | +1.224 | 0.2208 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **849**, R² = **0.1718**, Adj R² = **0.1579**, F-statistic = **12.35** (p = **1.58e-26**), Residual SE = **0.921** on **834** df, AIC = **2284.1**, BIC = **2355.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1473** | 0.3044 | ±0.6089 | **+10.338** | **4.72e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2212** | 0.0659 | ±0.1318 | **-3.357** | **7.87e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4317** | 0.1110 | ±0.2221 | **+3.888** | **1.01e-04** | *** |
| Site: UCSD (vs UAB) | +0.1314 | 0.0743 | ±0.1486 | +1.769 | 0.0769 | . |
| **Site: UW (vs UAB)** | **-0.3071** | 0.0819 | ±0.1637 | **-3.752** | **1.76e-04** | *** |
| Season: spring (vs autumn) | -0.1738 | 0.0889 | ±0.1777 | -1.956 | 0.0505 | . |
| Season: summer (vs autumn) | +0.0484 | 0.0890 | ±0.1780 | +0.544 | 0.5866 |  |
| Season: winter (vs autumn) | -0.0036 | 0.0955 | ±0.1910 | -0.037 | 0.9702 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0063 | **-6.843** | **7.74e-12** | *** |
| BMI (kg/m2) | +0.0071 | 0.0052 | ±0.0103 | +1.382 | 0.1670 |  |
| Hypertension | +0.1039 | 0.0660 | ±0.1320 | +1.574 | 0.1156 |  |
| High cholesterol | -0.0685 | 0.0672 | ±0.1344 | -1.019 | 0.3082 |  |
| Kidney disease | -0.0723 | 0.0830 | ±0.1660 | -0.871 | 0.3838 |  |
| Circulatory disease | +0.0106 | 0.0785 | ±0.1570 | +0.135 | 0.8930 |  |
| Time > 180 (%) | +0.0025 | 0.0014 | ±0.0029 | +1.716 | 0.0861 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **849**, R² = **0.1717**, Adj R² = **0.1578**, F-statistic = **12.35** (p = **1.63e-26**), Residual SE = **0.921** on **834** df, AIC = **2284.2**, BIC = **2355.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1497** | 0.3046 | ±0.6091 | **+10.342** | **4.56e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2217** | 0.0659 | ±0.1317 | **-3.366** | **7.63e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4313** | 0.1110 | ±0.2220 | **+3.886** | **1.02e-04** | *** |
| Site: UCSD (vs UAB) | +0.1319 | 0.0743 | ±0.1485 | +1.776 | 0.0758 | . |
| **Site: UW (vs UAB)** | **-0.3071** | 0.0819 | ±0.1637 | **-3.752** | **1.76e-04** | *** |
| **Season: spring (vs autumn)** | **-0.1743** | 0.0889 | ±0.1778 | **-1.960** | **0.0499** | * |
| Season: summer (vs autumn) | +0.0476 | 0.0890 | ±0.1780 | +0.535 | 0.5924 |  |
| Season: winter (vs autumn) | -0.0043 | 0.0955 | ±0.1911 | -0.045 | 0.9637 |  |
| **Age (years)** | **-0.0215** | 0.0031 | ±0.0063 | **-6.842** | **7.80e-12** | *** |
| BMI (kg/m2) | +0.0071 | 0.0052 | ±0.0103 | +1.379 | 0.1679 |  |
| Hypertension | +0.1039 | 0.0660 | ±0.1321 | +1.574 | 0.1155 |  |
| High cholesterol | -0.0687 | 0.0672 | ±0.1344 | -1.023 | 0.3063 |  |
| Kidney disease | -0.0727 | 0.0830 | ±0.1659 | -0.877 | 0.3805 |  |
| Circulatory disease | +0.0105 | 0.0785 | ±0.1570 | +0.134 | 0.8936 |  |
| Avg. daily time > 180 (%) | +0.0024 | 0.0014 | ±0.0029 | +1.703 | 0.0886 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **849**, R² = **0.1729**, Adj R² = **0.1590**, F-statistic = **12.45** (p = **9.37e-27**), Residual SE = **0.920** on **834** df, AIC = **2283.0**, BIC = **2354.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1493** | 0.3041 | ±0.6082 | **+10.356** | **3.94e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2171** | 0.0661 | ±0.1321 | **-3.286** | **0.0010** | ** |
| **Education: high school or below (vs college)** | **+0.4306** | 0.1108 | ±0.2216 | **+3.887** | **1.02e-04** | *** |
| Site: UCSD (vs UAB) | +0.1348 | 0.0743 | ±0.1486 | +1.814 | 0.0697 | . |
| **Site: UW (vs UAB)** | **-0.3080** | 0.0818 | ±0.1637 | **-3.764** | **1.67e-04** | *** |
| **Season: spring (vs autumn)** | **-0.1752** | 0.0888 | ±0.1776 | **-1.972** | **0.0486** | * |
| Season: summer (vs autumn) | +0.0497 | 0.0887 | ±0.1775 | +0.560 | 0.5753 |  |
| Season: winter (vs autumn) | -0.0054 | 0.0955 | ±0.1910 | -0.056 | 0.9552 |  |
| **Age (years)** | **-0.0212** | 0.0031 | ±0.0062 | **-6.801** | **1.04e-11** | *** |
| BMI (kg/m2) | +0.0066 | 0.0052 | ±0.0104 | +1.270 | 0.2042 |  |
| Hypertension | +0.1053 | 0.0661 | ±0.1322 | +1.592 | 0.1114 |  |
| High cholesterol | -0.0674 | 0.0671 | ±0.1342 | -1.005 | 0.3151 |  |
| Kidney disease | -0.0714 | 0.0828 | ±0.1656 | -0.863 | 0.3882 |  |
| Circulatory disease | +0.0095 | 0.0786 | ±0.1571 | +0.121 | 0.9040 |  |
| Nocturnal time > 180 (%) | +0.0027 | 0.0014 | ±0.0027 | +1.951 | 0.0511 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.1680**, Adj R² = **0.1540**, F-statistic = **12.03** (p = **9.22e-26**), Residual SE = **0.923** on **834** df, AIC = **2288.0**, BIC = **2359.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1682** | 0.3063 | ±0.6126 | **+10.344** | **4.46e-25** | *** |
| **Education: graduate level (vs college)** | **-0.2296** | 0.0661 | ±0.1323 | **-3.472** | **5.17e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4484** | 0.1131 | ±0.2261 | **+3.965** | **7.33e-05** | *** |
| Site: UCSD (vs UAB) | +0.1188 | 0.0746 | ±0.1493 | +1.592 | 0.1114 |  |
| **Site: UW (vs UAB)** | **-0.3132** | 0.0824 | ±0.1649 | **-3.800** | **1.45e-04** | *** |
| Season: spring (vs autumn) | -0.1708 | 0.0887 | ±0.1774 | -1.926 | 0.0541 | . |
| Season: summer (vs autumn) | +0.0441 | 0.0893 | ±0.1786 | +0.494 | 0.6212 |  |
| Season: winter (vs autumn) | +0.0049 | 0.0958 | ±0.1916 | +0.051 | 0.9592 |  |
| **Age (years)** | **-0.0212** | 0.0032 | ±0.0065 | **-6.576** | **4.83e-11** | *** |
| BMI (kg/m2) | +0.0075 | 0.0051 | ±0.0102 | +1.472 | 0.1409 |  |
| Hypertension | +0.0994 | 0.0659 | ±0.1317 | +1.508 | 0.1315 |  |
| High cholesterol | -0.0735 | 0.0670 | ±0.1340 | -1.097 | 0.2727 |  |
| Kidney disease | -0.0581 | 0.0832 | ±0.1664 | -0.699 | 0.4846 |  |
| Circulatory disease | +0.0136 | 0.0788 | ±0.1576 | +0.173 | 0.8629 |  |
| Any reading > 250 during wear (0/1) | +0.0204 | 0.0694 | ±0.1388 | +0.294 | 0.7685 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.1718**, Adj R² = **0.1579**, F-statistic = **12.36** (p = **1.52e-26**), Residual SE = **0.921** on **834** df, AIC = **2284.0**, BIC = **2355.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1364** | 0.3077 | ±0.6153 | **+10.194** | **2.11e-24** | *** |
| **Education: graduate level (vs college)** | **-0.2189** | 0.0663 | ±0.1327 | **-3.300** | **9.66e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4333** | 0.1105 | ±0.2209 | **+3.922** | **8.78e-05** | *** |
| Site: UCSD (vs UAB) | +0.1288 | 0.0744 | ±0.1489 | +1.731 | 0.0835 | . |
| **Site: UW (vs UAB)** | **-0.3011** | 0.0817 | ±0.1633 | **-3.687** | **2.27e-04** | *** |
| Season: spring (vs autumn) | -0.1691 | 0.0889 | ±0.1777 | -1.903 | 0.0570 | . |
| Season: summer (vs autumn) | +0.0572 | 0.0890 | ±0.1780 | +0.643 | 0.5203 |  |
| Season: winter (vs autumn) | +0.0029 | 0.0955 | ±0.1909 | +0.030 | 0.9757 |  |
| **Age (years)** | **-0.0209** | 0.0031 | ±0.0062 | **-6.712** | **1.93e-11** | *** |
| BMI (kg/m2) | +0.0072 | 0.0052 | ±0.0103 | +1.399 | 0.1618 |  |
| Hypertension | +0.0969 | 0.0662 | ±0.1323 | +1.464 | 0.1432 |  |
| High cholesterol | -0.0705 | 0.0672 | ±0.1343 | -1.050 | 0.2938 |  |
| Kidney disease | -0.0682 | 0.0837 | ±0.1674 | -0.815 | 0.4151 |  |
| Circulatory disease | +0.0110 | 0.0788 | ±0.1575 | +0.139 | 0.8894 |  |
| Time > 250 (%) | +0.0041 | 0.0027 | ±0.0055 | +1.513 | 0.1302 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 849)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.1719**, Adj R² = **0.1580**, F-statistic = **12.36** (p = **1.49e-26**), Residual SE = **0.921** on **834** df, AIC = **2284.0**, BIC = **2355.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1404** | 0.3077 | ±0.6154 | **+10.206** | **1.87e-24** | *** |
| **Education: graduate level (vs college)** | **-0.2190** | 0.0663 | ±0.1326 | **-3.303** | **9.57e-04** | *** |
| **Education: high school or below (vs college)** | **+0.4333** | 0.1105 | ±0.2210 | **+3.922** | **8.78e-05** | *** |
| Site: UCSD (vs UAB) | +0.1291 | 0.0744 | ±0.1488 | +1.736 | 0.0826 | . |
| **Site: UW (vs UAB)** | **-0.3014** | 0.0817 | ±0.1633 | **-3.691** | **2.23e-04** | *** |
| Season: spring (vs autumn) | -0.1699 | 0.0889 | ±0.1778 | -1.911 | 0.0560 | . |
| Season: summer (vs autumn) | +0.0563 | 0.0889 | ±0.1779 | +0.633 | 0.5265 |  |
| Season: winter (vs autumn) | +0.0022 | 0.0954 | ±0.1909 | +0.023 | 0.9817 |  |
| **Age (years)** | **-0.0210** | 0.0031 | ±0.0062 | **-6.726** | **1.75e-11** | *** |
| BMI (kg/m2) | +0.0072 | 0.0052 | ±0.0103 | +1.396 | 0.1628 |  |
| Hypertension | +0.0972 | 0.0662 | ±0.1323 | +1.468 | 0.1420 |  |
| High cholesterol | -0.0705 | 0.0671 | ±0.1343 | -1.050 | 0.2936 |  |
| Kidney disease | -0.0691 | 0.0837 | ±0.1674 | -0.826 | 0.4090 |  |
| Circulatory disease | +0.0104 | 0.0788 | ±0.1576 | +0.132 | 0.8946 |  |
| Avg. daily time > 250 (%) | +0.0042 | 0.0028 | ±0.0055 | +1.528 | 0.1266 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 849; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **849**, R² = **0.2625**, Adj R² = **0.2510**, F-statistic = **22.86** (p = **3.79e-47**), Residual SE = **2.114** on **835** df, AIC = **3694.1**, BIC = **3760.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1179** | 0.6462 | ±1.2923 | **+37.324** | **6.59e-305** | *** |
| Education: graduate level (vs college) | -0.0720 | 0.1621 | ±0.3243 | -0.444 | 0.6571 |  |
| Education: high school or below (vs college) | +0.2181 | 0.2229 | ±0.4457 | +0.979 | 0.3278 |  |
| Site: UCSD (vs UAB) | -0.1349 | 0.1780 | ±0.3559 | -0.758 | 0.4485 |  |
| **Site: UW (vs UAB)** | **-1.3869** | 0.1836 | ±0.3672 | **-7.555** | **4.20e-14** | *** |
| Season: spring (vs autumn) | -0.2256 | 0.1965 | ±0.3929 | -1.148 | 0.2509 |  |
| **Season: summer (vs autumn)** | **+1.7911** | 0.2210 | ±0.4419 | **+8.106** | **5.24e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2022** | 0.2132 | ±0.4264 | **-5.639** | **1.71e-08** | *** |
| Age (years) | +0.0094 | 0.0075 | ±0.0150 | +1.263 | 0.2065 |  |
| BMI (kg/m2) | +0.0134 | 0.0106 | ±0.0211 | +1.269 | 0.2043 |  |
| Hypertension | +0.3099 | 0.1596 | ±0.3192 | +1.942 | 0.0521 | . |
| High cholesterol | -0.1579 | 0.1570 | ±0.3140 | -1.006 | 0.3146 |  |
| Kidney disease | -0.1452 | 0.1912 | ±0.3824 | -0.760 | 0.4475 |  |
| Circulatory disease | +0.2291 | 0.1913 | ±0.3826 | +1.197 | 0.2311 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **849**, R² = **0.2628**, Adj R² = **0.2504**, F-statistic = **21.24** (p = **1.60e-46**), Residual SE = **2.115** on **834** df, AIC = **3695.8**, BIC = **3766.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3107** | 0.7821 | ±1.5643 | **+31.082** | **4.17e-212** | *** |
| Education: graduate level (vs college) | -0.0797 | 0.1644 | ±0.3289 | -0.485 | 0.6278 |  |
| Education: high school or below (vs college) | +0.2309 | 0.2239 | ±0.4478 | +1.031 | 0.3023 |  |
| Site: UCSD (vs UAB) | -0.1403 | 0.1796 | ±0.3592 | -0.781 | 0.4346 |  |
| **Site: UW (vs UAB)** | **-1.3915** | 0.1842 | ±0.3684 | **-7.554** | **4.22e-14** | *** |
| Season: spring (vs autumn) | -0.2288 | 0.1973 | ±0.3947 | -1.159 | 0.2464 |  |
| **Season: summer (vs autumn)** | **+1.7868** | 0.2223 | ±0.4445 | **+8.039** | **9.08e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2001** | 0.2139 | ±0.4277 | **-5.611** | **2.01e-08** | *** |
| Age (years) | +0.0096 | 0.0075 | ±0.0150 | +1.280 | 0.2006 |  |
| BMI (kg/m2) | +0.0139 | 0.0108 | ±0.0215 | +1.291 | 0.1968 |  |
| Hypertension | +0.3102 | 0.1600 | ±0.3199 | +1.940 | 0.0524 | . |
| High cholesterol | -0.1580 | 0.1573 | ±0.3147 | -1.004 | 0.3153 |  |
| Kidney disease | -0.1430 | 0.1915 | ±0.3830 | -0.746 | 0.4554 |  |
| Circulatory disease | +0.2306 | 0.1918 | ±0.3836 | +1.202 | 0.2293 |  |
| HbA1c (%) | -0.0319 | 0.0744 | ±0.1489 | -0.428 | 0.6684 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **849**, R² = **0.2633**, Adj R² = **0.2509**, F-statistic = **21.29** (p = **1.23e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.2**, BIC = **3766.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3492** | 0.7002 | ±1.4003 | **+34.776** | **5.58e-265** | *** |
| Education: graduate level (vs college) | -0.0832 | 0.1629 | ±0.3257 | -0.511 | 0.6093 |  |
| Education: high school or below (vs college) | +0.2356 | 0.2243 | ±0.4485 | +1.051 | 0.2934 |  |
| Site: UCSD (vs UAB) | -0.1464 | 0.1794 | ±0.3588 | -0.816 | 0.4146 |  |
| **Site: UW (vs UAB)** | **-1.3921** | 0.1846 | ±0.3692 | **-7.540** | **4.69e-14** | *** |
| Season: spring (vs autumn) | -0.2219 | 0.1963 | ±0.3925 | -1.131 | 0.2581 |  |
| **Season: summer (vs autumn)** | **+1.7865** | 0.2216 | ±0.4431 | **+8.063** | **7.45e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1932** | 0.2143 | ±0.4286 | **-5.568** | **2.58e-08** | *** |
| Age (years) | +0.0098 | 0.0075 | ±0.0150 | +1.302 | 0.1928 |  |
| BMI (kg/m2) | +0.0137 | 0.0106 | ±0.0213 | +1.290 | 0.1971 |  |
| Hypertension | +0.3070 | 0.1604 | ±0.3208 | +1.914 | 0.0556 | . |
| High cholesterol | -0.1618 | 0.1575 | ±0.3150 | -1.027 | 0.3044 |  |
| Kidney disease | -0.1299 | 0.1908 | ±0.3817 | -0.681 | 0.4960 |  |
| Circulatory disease | +0.2310 | 0.1916 | ±0.3832 | +1.206 | 0.2279 |  |
| Mean glucose (mg/dL) | -0.0017 | 0.0019 | ±0.0039 | -0.860 | 0.3900 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **849**, R² = **0.2633**, Adj R² = **0.2509**, F-statistic = **21.29** (p = **1.23e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.2**, BIC = **3766.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5796** | 0.8390 | ±1.6779 | **+29.298** | **1.10e-188** | *** |
| Education: graduate level (vs college) | -0.0832 | 0.1629 | ±0.3257 | -0.511 | 0.6093 |  |
| Education: high school or below (vs college) | +0.2356 | 0.2243 | ±0.4485 | +1.051 | 0.2934 |  |
| Site: UCSD (vs UAB) | -0.1464 | 0.1794 | ±0.3588 | -0.816 | 0.4146 |  |
| **Site: UW (vs UAB)** | **-1.3921** | 0.1846 | ±0.3692 | **-7.540** | **4.69e-14** | *** |
| Season: spring (vs autumn) | -0.2219 | 0.1963 | ±0.3925 | -1.131 | 0.2581 |  |
| **Season: summer (vs autumn)** | **+1.7865** | 0.2216 | ±0.4431 | **+8.063** | **7.45e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1932** | 0.2143 | ±0.4286 | **-5.568** | **2.58e-08** | *** |
| Age (years) | +0.0098 | 0.0075 | ±0.0150 | +1.302 | 0.1928 |  |
| BMI (kg/m2) | +0.0137 | 0.0106 | ±0.0213 | +1.290 | 0.1971 |  |
| Hypertension | +0.3070 | 0.1604 | ±0.3208 | +1.914 | 0.0556 | . |
| High cholesterol | -0.1618 | 0.1575 | ±0.3150 | -1.027 | 0.3044 |  |
| Kidney disease | -0.1299 | 0.1908 | ±0.3817 | -0.681 | 0.4960 |  |
| Circulatory disease | +0.2310 | 0.1916 | ±0.3832 | +1.206 | 0.2279 |  |
| GMI (%) | -0.0696 | 0.0810 | ±0.1620 | -0.860 | 0.3900 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **849**, R² = **0.2631**, Adj R² = **0.2507**, F-statistic = **21.27** (p = **1.36e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.4**, BIC = **3766.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3150** | 0.6946 | ±1.3891 | **+35.007** | **1.74e-268** | *** |
| Education: graduate level (vs college) | -0.0816 | 0.1630 | ±0.3259 | -0.501 | 0.6164 |  |
| Education: high school or below (vs college) | +0.2326 | 0.2242 | ±0.4484 | +1.038 | 0.2994 |  |
| Site: UCSD (vs UAB) | -0.1444 | 0.1793 | ±0.3586 | -0.805 | 0.4207 |  |
| **Site: UW (vs UAB)** | **-1.3880** | 0.1841 | ±0.3683 | **-7.538** | **4.79e-14** | *** |
| Season: spring (vs autumn) | -0.2206 | 0.1964 | ±0.3928 | -1.123 | 0.2613 |  |
| **Season: summer (vs autumn)** | **+1.7877** | 0.2215 | ±0.4430 | **+8.070** | **7.00e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1935** | 0.2143 | ±0.4286 | **-5.569** | **2.56e-08** | *** |
| Age (years) | +0.0094 | 0.0075 | ±0.0150 | +1.259 | 0.2080 |  |
| BMI (kg/m2) | +0.0140 | 0.0107 | ±0.0215 | +1.308 | 0.1910 |  |
| Hypertension | +0.3063 | 0.1606 | ±0.3211 | +1.908 | 0.0564 | . |
| High cholesterol | -0.1603 | 0.1574 | ±0.3149 | -1.018 | 0.3087 |  |
| Kidney disease | -0.1367 | 0.1907 | ±0.3814 | -0.717 | 0.4736 |  |
| Circulatory disease | +0.2306 | 0.1917 | ±0.3833 | +1.203 | 0.2289 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0014 | 0.0019 | ±0.0038 | -0.742 | 0.4581 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **849**, R² = **0.2631**, Adj R² = **0.2507**, F-statistic = **21.27** (p = **1.36e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.4**, BIC = **3766.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.2337** | 0.6721 | ±1.3441 | **+36.059** | **1.01e-284** | *** |
| Education: graduate level (vs college) | -0.0838 | 0.1632 | ±0.3264 | -0.514 | 0.6076 |  |
| Education: high school or below (vs college) | +0.2357 | 0.2245 | ±0.4490 | +1.050 | 0.2937 |  |
| Site: UCSD (vs UAB) | -0.1454 | 0.1795 | ±0.3589 | -0.810 | 0.4178 |  |
| **Site: UW (vs UAB)** | **-1.3974** | 0.1850 | ±0.3700 | **-7.554** | **4.24e-14** | *** |
| Season: spring (vs autumn) | -0.2234 | 0.1962 | ±0.3924 | -1.138 | 0.2550 |  |
| **Season: summer (vs autumn)** | **+1.7854** | 0.2220 | ±0.4439 | **+8.044** | **8.69e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1962** | 0.2136 | ±0.4272 | **-5.600** | **2.14e-08** | *** |
| Age (years) | +0.0101 | 0.0075 | ±0.0151 | +1.336 | 0.1814 |  |
| BMI (kg/m2) | +0.0134 | 0.0106 | ±0.0213 | +1.265 | 0.2057 |  |
| Hypertension | +0.3090 | 0.1600 | ±0.3200 | +1.931 | 0.0535 | . |
| High cholesterol | -0.1632 | 0.1577 | ±0.3154 | -1.035 | 0.3006 |  |
| Kidney disease | -0.1167 | 0.1941 | ±0.3881 | -0.601 | 0.5475 |  |
| Circulatory disease | +0.2321 | 0.1918 | ±0.3835 | +1.210 | 0.2262 |  |
| Glucose SD, pooled (mg/dL) | -0.0044 | 0.0059 | ±0.0118 | -0.740 | 0.4593 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **849**, R² = **0.2634**, Adj R² = **0.2510**, F-statistic = **21.30** (p = **1.15e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.1**, BIC = **3766.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.2726** | 0.6759 | ±1.3519 | **+35.910** | **2.16e-282** | *** |
| Education: graduate level (vs college) | -0.0857 | 0.1633 | ±0.3265 | -0.525 | 0.5997 |  |
| Education: high school or below (vs college) | +0.2420 | 0.2243 | ±0.4486 | +1.079 | 0.2808 |  |
| Site: UCSD (vs UAB) | -0.1473 | 0.1791 | ±0.3582 | -0.822 | 0.4108 |  |
| **Site: UW (vs UAB)** | **-1.3985** | 0.1845 | ±0.3691 | **-7.579** | **3.49e-14** | *** |
| Season: spring (vs autumn) | -0.2224 | 0.1962 | ±0.3924 | -1.134 | 0.2569 |  |
| **Season: summer (vs autumn)** | **+1.7825** | 0.2221 | ±0.4441 | **+8.027** | **1.00e-15** | *** |
| **Season: winter (vs autumn)** | **-1.1963** | 0.2134 | ±0.4269 | **-5.605** | **2.08e-08** | *** |
| Age (years) | +0.0103 | 0.0076 | ±0.0151 | +1.367 | 0.1717 |  |
| BMI (kg/m2) | +0.0131 | 0.0106 | ±0.0213 | +1.234 | 0.2172 |  |
| Hypertension | +0.3081 | 0.1600 | ±0.3199 | +1.926 | 0.0541 | . |
| High cholesterol | -0.1645 | 0.1576 | ±0.3153 | -1.043 | 0.2967 |  |
| Kidney disease | -0.1086 | 0.1938 | ±0.3876 | -0.561 | 0.5751 |  |
| Circulatory disease | +0.2309 | 0.1917 | ±0.3834 | +1.205 | 0.2283 |  |
| Avg. daily SD (mg/dL) | -0.0062 | 0.0065 | ±0.0131 | -0.950 | 0.3422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **849**, R² = **0.2625**, Adj R² = **0.2502**, F-statistic = **21.21** (p = **1.83e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.1**, BIC = **3767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1540** | 0.7012 | ±1.4025 | **+34.444** | **5.47e-260** | *** |
| Education: graduate level (vs college) | -0.0736 | 0.1626 | ±0.3252 | -0.453 | 0.6506 |  |
| Education: high school or below (vs college) | +0.2207 | 0.2241 | ±0.4481 | +0.985 | 0.3246 |  |
| Site: UCSD (vs UAB) | -0.1364 | 0.1786 | ±0.3571 | -0.764 | 0.4449 |  |
| **Site: UW (vs UAB)** | **-1.3892** | 0.1843 | ±0.3686 | **-7.537** | **4.80e-14** | *** |
| Season: spring (vs autumn) | -0.2258 | 0.1967 | ±0.3935 | -1.148 | 0.2511 |  |
| **Season: summer (vs autumn)** | **+1.7905** | 0.2216 | ±0.4432 | **+8.080** | **6.49e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2019** | 0.2134 | ±0.4268 | **-5.632** | **1.78e-08** | *** |
| Age (years) | +0.0096 | 0.0075 | ±0.0151 | +1.275 | 0.2022 |  |
| BMI (kg/m2) | +0.0134 | 0.0106 | ±0.0212 | +1.261 | 0.2072 |  |
| Hypertension | +0.3103 | 0.1600 | ±0.3200 | +1.939 | 0.0525 | . |
| High cholesterol | -0.1588 | 0.1575 | ±0.3150 | -1.008 | 0.3133 |  |
| Kidney disease | -0.1396 | 0.1954 | ±0.3908 | -0.715 | 0.4749 |  |
| Circulatory disease | +0.2297 | 0.1913 | ±0.3827 | +1.201 | 0.2299 |  |
| CV (%) | -0.0020 | 0.0129 | ±0.0259 | -0.152 | 0.8794 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **849**, R² = **0.2626**, Adj R² = **0.2502**, F-statistic = **21.21** (p = **1.80e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.0**, BIC = **3767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.2018** | 0.7162 | ±1.4325 | **+33.791** | **2.70e-250** | *** |
| Education: graduate level (vs college) | -0.0694 | 0.1626 | ±0.3252 | -0.427 | 0.6697 |  |
| Education: high school or below (vs college) | +0.2134 | 0.2241 | ±0.4482 | +0.952 | 0.3409 |  |
| Site: UCSD (vs UAB) | -0.1330 | 0.1783 | ±0.3566 | -0.746 | 0.4558 |  |
| **Site: UW (vs UAB)** | **-1.3835** | 0.1840 | ±0.3679 | **-7.520** | **5.46e-14** | *** |
| Season: spring (vs autumn) | -0.2257 | 0.1968 | ±0.3936 | -1.147 | 0.2514 |  |
| **Season: summer (vs autumn)** | **+1.7910** | 0.2213 | ±0.4426 | **+8.093** | **5.82e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2033** | 0.2134 | ±0.4268 | **-5.639** | **1.71e-08** | *** |
| Age (years) | +0.0092 | 0.0075 | ±0.0150 | +1.221 | 0.2221 |  |
| BMI (kg/m2) | +0.0135 | 0.0106 | ±0.0212 | +1.271 | 0.2036 |  |
| Hypertension | +0.3093 | 0.1600 | ±0.3199 | +1.934 | 0.0532 | . |
| High cholesterol | -0.1567 | 0.1574 | ±0.3148 | -0.996 | 0.3195 |  |
| Kidney disease | -0.1524 | 0.1945 | ±0.3891 | -0.784 | 0.4333 |  |
| Circulatory disease | +0.2275 | 0.1912 | ±0.3824 | +1.190 | 0.2340 |  |
| Mean / SD ratio | -0.0144 | 0.0627 | ±0.1254 | -0.229 | 0.8189 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **849**, R² = **0.2625**, Adj R² = **0.2502**, F-statistic = **21.21** (p = **1.85e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.1**, BIC = **3767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0946** | 0.7092 | ±1.4184 | **+33.974** | **5.32e-253** | *** |
| Education: graduate level (vs college) | -0.0728 | 0.1632 | ±0.3264 | -0.446 | 0.6555 |  |
| Education: high school or below (vs college) | +0.2194 | 0.2237 | ±0.4474 | +0.981 | 0.3267 |  |
| Site: UCSD (vs UAB) | -0.1351 | 0.1782 | ±0.3564 | -0.758 | 0.4484 |  |
| **Site: UW (vs UAB)** | **-1.3877** | 0.1833 | ±0.3666 | **-7.570** | **3.74e-14** | *** |
| Season: spring (vs autumn) | -0.2257 | 0.1971 | ±0.3942 | -1.145 | 0.2520 |  |
| **Season: summer (vs autumn)** | **+1.7909** | 0.2217 | ±0.4434 | **+8.078** | **6.60e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2022** | 0.2135 | ±0.4270 | **-5.631** | **1.79e-08** | *** |
| Age (years) | +0.0095 | 0.0075 | ±0.0151 | +1.266 | 0.2056 |  |
| BMI (kg/m2) | +0.0134 | 0.0107 | ±0.0213 | +1.254 | 0.2097 |  |
| Hypertension | +0.3101 | 0.1601 | ±0.3202 | +1.937 | 0.0527 | . |
| High cholesterol | -0.1582 | 0.1574 | ±0.3149 | -1.005 | 0.3148 |  |
| Kidney disease | -0.1434 | 0.1939 | ±0.3879 | -0.740 | 0.4596 |  |
| Circulatory disease | +0.2291 | 0.1915 | ±0.3830 | +1.196 | 0.2315 |  |
| Avg. daily mean/SD | +0.0035 | 0.0544 | ±0.1088 | +0.064 | 0.9486 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **849**, R² = **0.2637**, Adj R² = **0.2513**, F-statistic = **21.33** (p = **9.95e-47**), Residual SE = **2.113** on **834** df, AIC = **3694.8**, BIC = **3765.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5149** | 0.7556 | ±1.5111 | **+32.445** | **6.28e-231** | *** |
| Education: graduate level (vs college) | -0.0885 | 0.1640 | ±0.3279 | -0.540 | 0.5895 |  |
| Education: high school or below (vs college) | +0.2337 | 0.2221 | ±0.4443 | +1.052 | 0.2928 |  |
| Site: UCSD (vs UAB) | -0.1453 | 0.1778 | ±0.3555 | -0.817 | 0.4137 |  |
| **Site: UW (vs UAB)** | **-1.4112** | 0.1837 | ±0.3675 | **-7.681** | **1.58e-14** | *** |
| Season: spring (vs autumn) | -0.2254 | 0.1965 | ±0.3929 | -1.147 | 0.2512 |  |
| **Season: summer (vs autumn)** | **+1.7784** | 0.2221 | ±0.4443 | **+8.006** | **1.19e-15** | *** |
| **Season: winter (vs autumn)** | **-1.2025** | 0.2134 | ±0.4268 | **-5.635** | **1.75e-08** | *** |
| Age (years) | +0.0093 | 0.0075 | ±0.0150 | +1.239 | 0.2152 |  |
| BMI (kg/m2) | +0.0135 | 0.0106 | ±0.0212 | +1.279 | 0.2010 |  |
| Hypertension | +0.3062 | 0.1600 | ±0.3200 | +1.914 | 0.0557 | . |
| High cholesterol | -0.1617 | 0.1570 | ±0.3141 | -1.030 | 0.3032 |  |
| Kidney disease | -0.1231 | 0.1927 | ±0.3853 | -0.639 | 0.5229 |  |
| Circulatory disease | +0.2283 | 0.1918 | ±0.3835 | +1.191 | 0.2337 |  |
| MAG (mg/dL/h) | -0.0086 | 0.0078 | ±0.0156 | -1.110 | 0.2672 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **849**, R² = **0.2632**, Adj R² = **0.2508**, F-statistic = **21.27** (p = **1.32e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.4**, BIC = **3766.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.3018** | 0.6952 | ±1.3904 | **+34.956** | **1.05e-267** | *** |
| Education: graduate level (vs college) | -0.0844 | 0.1631 | ±0.3263 | -0.517 | 0.6049 |  |
| Education: high school or below (vs college) | +0.2369 | 0.2240 | ±0.4479 | +1.058 | 0.2902 |  |
| Site: UCSD (vs UAB) | -0.1465 | 0.1789 | ±0.3578 | -0.819 | 0.4128 |  |
| **Site: UW (vs UAB)** | **-1.3965** | 0.1844 | ±0.3688 | **-7.573** | **3.64e-14** | *** |
| Season: spring (vs autumn) | -0.2217 | 0.1962 | ±0.3924 | -1.130 | 0.2585 |  |
| **Season: summer (vs autumn)** | **+1.7871** | 0.2215 | ±0.4430 | **+8.069** | **7.10e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1964** | 0.2136 | ±0.4272 | **-5.601** | **2.14e-08** | *** |
| Age (years) | +0.0101 | 0.0075 | ±0.0151 | +1.335 | 0.1819 |  |
| BMI (kg/m2) | +0.0130 | 0.0107 | ±0.0213 | +1.223 | 0.2215 |  |
| Hypertension | +0.3055 | 0.1601 | ±0.3202 | +1.908 | 0.0564 | . |
| High cholesterol | -0.1616 | 0.1575 | ±0.3150 | -1.026 | 0.3050 |  |
| Kidney disease | -0.1155 | 0.1943 | ±0.3887 | -0.594 | 0.5524 |  |
| Circulatory disease | +0.2317 | 0.1916 | ±0.3833 | +1.209 | 0.2267 |  |
| Avg. daily range (mg/dL) | -0.0015 | 0.0018 | ±0.0036 | -0.808 | 0.4189 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **849**, R² = **0.2626**, Adj R² = **0.2502**, F-statistic = **21.21** (p = **1.83e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.1**, BIC = **3767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1319** | 0.6570 | ±1.3139 | **+36.732** | **2.24e-295** | *** |
| Education: graduate level (vs college) | -0.0747 | 0.1631 | ±0.3263 | -0.458 | 0.6468 |  |
| Education: high school or below (vs college) | +0.2200 | 0.2242 | ±0.4484 | +0.981 | 0.3265 |  |
| Site: UCSD (vs UAB) | -0.1366 | 0.1799 | ±0.3599 | -0.759 | 0.4479 |  |
| **Site: UW (vs UAB)** | **-1.3890** | 0.1863 | ±0.3725 | **-7.457** | **8.83e-14** | *** |
| Season: spring (vs autumn) | -0.2257 | 0.1966 | ±0.3932 | -1.148 | 0.2510 |  |
| **Season: summer (vs autumn)** | **+1.7912** | 0.2212 | ±0.4423 | **+8.099** | **5.55e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2007** | 0.2137 | ±0.4274 | **-5.619** | **1.92e-08** | *** |
| Age (years) | +0.0095 | 0.0075 | ±0.0150 | +1.263 | 0.2068 |  |
| BMI (kg/m2) | +0.0135 | 0.0106 | ±0.0213 | +1.270 | 0.2040 |  |
| Hypertension | +0.3103 | 0.1598 | ±0.3196 | +1.942 | 0.0521 | . |
| High cholesterol | -0.1584 | 0.1575 | ±0.3150 | -1.006 | 0.3145 |  |
| Kidney disease | -0.1417 | 0.1935 | ±0.3869 | -0.732 | 0.4640 |  |
| Circulatory disease | +0.2312 | 0.1918 | ±0.3836 | +1.206 | 0.2280 |  |
| SD of daily means (mg/dL) | -0.0015 | 0.0112 | ±0.0224 | -0.132 | 0.8946 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **849**, R² = **0.2631**, Adj R² = **0.2507**, F-statistic = **21.27** (p = **1.37e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.4**, BIC = **3766.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9140** | 0.7069 | ±1.4138 | **+33.830** | **7.15e-251** | *** |
| Education: graduate level (vs college) | -0.0820 | 0.1631 | ±0.3261 | -0.503 | 0.6149 |  |
| Education: high school or below (vs college) | +0.2345 | 0.2250 | ±0.4501 | +1.042 | 0.2974 |  |
| Site: UCSD (vs UAB) | -0.1485 | 0.1798 | ±0.3595 | -0.826 | 0.4086 |  |
| **Site: UW (vs UAB)** | **-1.3929** | 0.1848 | ±0.3695 | **-7.539** | **4.75e-14** | *** |
| Season: spring (vs autumn) | -0.2237 | 0.1964 | ±0.3927 | -1.139 | 0.2546 |  |
| **Season: summer (vs autumn)** | **+1.7868** | 0.2219 | ±0.4438 | **+8.052** | **8.12e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1948** | 0.2140 | ±0.4280 | **-5.582** | **2.37e-08** | *** |
| Age (years) | +0.0099 | 0.0075 | ±0.0151 | +1.311 | 0.1898 |  |
| BMI (kg/m2) | +0.0138 | 0.0106 | ±0.0213 | +1.295 | 0.1955 |  |
| Hypertension | +0.3049 | 0.1606 | ±0.3213 | +1.898 | 0.0577 | . |
| High cholesterol | -0.1630 | 0.1578 | ±0.3155 | -1.033 | 0.3016 |  |
| Kidney disease | -0.1298 | 0.1905 | ±0.3811 | -0.681 | 0.4956 |  |
| Circulatory disease | +0.2320 | 0.1917 | ±0.3834 | +1.210 | 0.2261 |  |
| Time in range 70-180, pooled (%) | +0.0023 | 0.0031 | ±0.0062 | +0.737 | 0.4610 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **849**, R² = **0.2632**, Adj R² = **0.2508**, F-statistic = **21.28** (p = **1.31e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.3**, BIC = **3766.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8962** | 0.7076 | ±1.4151 | **+33.773** | **4.90e-250** | *** |
| Education: graduate level (vs college) | -0.0825 | 0.1631 | ±0.3261 | -0.506 | 0.6130 |  |
| Education: high school or below (vs college) | +0.2363 | 0.2251 | ±0.4502 | +1.050 | 0.2937 |  |
| Site: UCSD (vs UAB) | -0.1501 | 0.1798 | ±0.3597 | -0.835 | 0.4040 |  |
| **Site: UW (vs UAB)** | **-1.3933** | 0.1848 | ±0.3695 | **-7.541** | **4.67e-14** | *** |
| Season: spring (vs autumn) | -0.2231 | 0.1963 | ±0.3927 | -1.136 | 0.2558 |  |
| **Season: summer (vs autumn)** | **+1.7872** | 0.2218 | ±0.4435 | **+8.060** | **7.65e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1933** | 0.2141 | ±0.4283 | **-5.572** | **2.51e-08** | *** |
| Age (years) | +0.0099 | 0.0075 | ±0.0151 | +1.318 | 0.1876 |  |
| BMI (kg/m2) | +0.0138 | 0.0106 | ±0.0213 | +1.298 | 0.1945 |  |
| Hypertension | +0.3044 | 0.1607 | ±0.3213 | +1.894 | 0.0582 | . |
| High cholesterol | -0.1632 | 0.1577 | ±0.3155 | -1.035 | 0.3008 |  |
| Kidney disease | -0.1280 | 0.1904 | ±0.3809 | -0.672 | 0.5014 |  |
| Circulatory disease | +0.2323 | 0.1917 | ±0.3834 | +1.212 | 0.2256 |  |
| Avg. daily time in range 70-180 (%) | +0.0025 | 0.0031 | ±0.0062 | +0.793 | 0.4276 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.2628**, Adj R² = **0.2504**, F-statistic = **21.23** (p = **1.64e-46**), Residual SE = **2.115** on **834** df, AIC = **3695.8**, BIC = **3767.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1542** | 0.6507 | ±1.3013 | **+37.122** | **1.25e-301** | *** |
| Education: graduate level (vs college) | -0.0716 | 0.1623 | ±0.3247 | -0.441 | 0.6590 |  |
| Education: high school or below (vs college) | +0.2130 | 0.2226 | ±0.4452 | +0.957 | 0.3386 |  |
| Site: UCSD (vs UAB) | -0.1416 | 0.1791 | ±0.3583 | -0.790 | 0.4292 |  |
| **Site: UW (vs UAB)** | **-1.3949** | 0.1845 | ±0.3690 | **-7.560** | **4.04e-14** | *** |
| Season: spring (vs autumn) | -0.2262 | 0.1965 | ±0.3929 | -1.151 | 0.2496 |  |
| **Season: summer (vs autumn)** | **+1.7889** | 0.2212 | ±0.4424 | **+8.088** | **6.07e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2081** | 0.2139 | ±0.4278 | **-5.647** | **1.63e-08** | *** |
| Age (years) | +0.0092 | 0.0075 | ±0.0150 | +1.221 | 0.2223 |  |
| BMI (kg/m2) | +0.0137 | 0.0105 | ±0.0211 | +1.302 | 0.1928 |  |
| **Hypertension** | **+0.3146** | 0.1602 | ±0.3205 | **+1.963** | **0.0496** | * |
| High cholesterol | -0.1621 | 0.1562 | ±0.3123 | -1.038 | 0.2992 |  |
| Kidney disease | -0.1470 | 0.1912 | ±0.3825 | -0.769 | 0.4421 |  |
| Circulatory disease | +0.2343 | 0.1915 | ±0.3829 | +1.224 | 0.2211 |  |
| Any reading < 54 during wear (0/1) | -0.0846 | 0.1658 | ±0.3316 | -0.510 | 0.6099 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.2626**, Adj R² = **0.2502**, F-statistic = **21.21** (p = **1.80e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.0**, BIC = **3767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1110** | 0.6467 | ±1.2934 | **+37.284** | **3.01e-304** | *** |
| Education: graduate level (vs college) | -0.0708 | 0.1623 | ±0.3246 | -0.436 | 0.6625 |  |
| Education: high school or below (vs college) | +0.2210 | 0.2226 | ±0.4451 | +0.993 | 0.3207 |  |
| Site: UCSD (vs UAB) | -0.1304 | 0.1786 | ±0.3572 | -0.730 | 0.4653 |  |
| **Site: UW (vs UAB)** | **-1.3817** | 0.1839 | ±0.3678 | **-7.513** | **5.77e-14** | *** |
| Season: spring (vs autumn) | -0.2240 | 0.1968 | ±0.3935 | -1.138 | 0.2550 |  |
| **Season: summer (vs autumn)** | **+1.7920** | 0.2209 | ±0.4417 | **+8.114** | **4.91e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2006** | 0.2140 | ±0.4281 | **-5.609** | **2.03e-08** | *** |
| Age (years) | +0.0095 | 0.0075 | ±0.0150 | +1.266 | 0.2054 |  |
| BMI (kg/m2) | +0.0133 | 0.0106 | ±0.0212 | +1.259 | 0.2079 |  |
| Hypertension | +0.3089 | 0.1604 | ±0.3209 | +1.925 | 0.0542 | . |
| High cholesterol | -0.1572 | 0.1570 | ±0.3141 | -1.001 | 0.3169 |  |
| Kidney disease | -0.1441 | 0.1913 | ±0.3826 | -0.753 | 0.4512 |  |
| Circulatory disease | +0.2259 | 0.1909 | ±0.3819 | +1.183 | 0.2368 |  |
| Time < 54 (%) | +0.0431 | 0.1788 | ±0.3576 | +0.241 | 0.8093 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.2626**, Adj R² = **0.2503**, F-statistic = **21.22** (p = **1.75e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.0**, BIC = **3767.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1125** | 0.6462 | ±1.2924 | **+37.313** | **1.00e-304** | *** |
| Education: graduate level (vs college) | -0.0697 | 0.1621 | ±0.3243 | -0.430 | 0.6671 |  |
| Education: high school or below (vs college) | +0.2214 | 0.2225 | ±0.4449 | +0.995 | 0.3196 |  |
| Site: UCSD (vs UAB) | -0.1298 | 0.1787 | ±0.3573 | -0.726 | 0.4675 |  |
| **Site: UW (vs UAB)** | **-1.3811** | 0.1841 | ±0.3682 | **-7.503** | **6.25e-14** | *** |
| Season: spring (vs autumn) | -0.2220 | 0.1968 | ±0.3937 | -1.128 | 0.2594 |  |
| **Season: summer (vs autumn)** | **+1.7925** | 0.2210 | ±0.4421 | **+8.110** | **5.08e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2003** | 0.2141 | ±0.4282 | **-5.607** | **2.06e-08** | *** |
| Age (years) | +0.0094 | 0.0075 | ±0.0150 | +1.255 | 0.2096 |  |
| BMI (kg/m2) | +0.0133 | 0.0106 | ±0.0212 | +1.262 | 0.2070 |  |
| Hypertension | +0.3090 | 0.1602 | ±0.3203 | +1.929 | 0.0537 | . |
| High cholesterol | -0.1561 | 0.1569 | ±0.3138 | -0.995 | 0.3199 |  |
| Kidney disease | -0.1446 | 0.1912 | ±0.3825 | -0.756 | 0.4497 |  |
| Circulatory disease | +0.2251 | 0.1912 | ±0.3823 | +1.177 | 0.2390 |  |
| Avg. daily time < 54 (%) | +0.0587 | 0.1998 | ±0.3996 | +0.294 | 0.7689 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.2632**, Adj R² = **0.2508**, F-statistic = **21.28** (p = **1.30e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.3**, BIC = **3766.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1038** | 0.6475 | ±1.2949 | **+37.227** | **2.45e-303** | *** |
| Education: graduate level (vs college) | -0.0654 | 0.1626 | ±0.3251 | -0.402 | 0.6876 |  |
| Education: high school or below (vs college) | +0.2183 | 0.2230 | ±0.4459 | +0.979 | 0.3276 |  |
| Site: UCSD (vs UAB) | -0.1235 | 0.1788 | ±0.3575 | -0.691 | 0.4898 |  |
| **Site: UW (vs UAB)** | **-1.3754** | 0.1836 | ±0.3673 | **-7.490** | **6.89e-14** | *** |
| Season: spring (vs autumn) | -0.2159 | 0.1966 | ±0.3932 | -1.098 | 0.2721 |  |
| **Season: summer (vs autumn)** | **+1.7976** | 0.2205 | ±0.4410 | **+8.152** | **3.57e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1931** | 0.2142 | ±0.4284 | **-5.571** | **2.54e-08** | *** |
| Age (years) | +0.0092 | 0.0075 | ±0.0149 | +1.232 | 0.2181 |  |
| BMI (kg/m2) | +0.0132 | 0.0106 | ±0.0213 | +1.245 | 0.2132 |  |
| Hypertension | +0.3082 | 0.1601 | ±0.3202 | +1.925 | 0.0542 | . |
| High cholesterol | -0.1565 | 0.1571 | ±0.3142 | -0.996 | 0.3191 |  |
| Kidney disease | -0.1456 | 0.1916 | ±0.3832 | -0.760 | 0.4472 |  |
| Circulatory disease | +0.2240 | 0.1912 | ±0.3824 | +1.171 | 0.2414 |  |
| Time 54-69, pooled (%) | +0.0423 | 0.0512 | ±0.1025 | +0.826 | 0.4087 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **849**, R² = **0.2636**, Adj R² = **0.2512**, F-statistic = **21.32** (p = **1.04e-46**), Residual SE = **2.113** on **834** df, AIC = **3694.9**, BIC = **3766.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1103** | 0.6466 | ±1.2931 | **+37.290** | **2.41e-304** | *** |
| Education: graduate level (vs college) | -0.0630 | 0.1624 | ±0.3249 | -0.388 | 0.6983 |  |
| Education: high school or below (vs college) | +0.2170 | 0.2231 | ±0.4462 | +0.973 | 0.3307 |  |
| Site: UCSD (vs UAB) | -0.1217 | 0.1787 | ±0.3575 | -0.681 | 0.4959 |  |
| **Site: UW (vs UAB)** | **-1.3729** | 0.1836 | ±0.3671 | **-7.479** | **7.47e-14** | *** |
| Season: spring (vs autumn) | -0.2139 | 0.1965 | ±0.3930 | -1.089 | 0.2763 |  |
| **Season: summer (vs autumn)** | **+1.7983** | 0.2204 | ±0.4409 | **+8.158** | **3.41e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1918** | 0.2142 | ±0.4283 | **-5.565** | **2.62e-08** | *** |
| Age (years) | +0.0090 | 0.0075 | ±0.0149 | +1.207 | 0.2275 |  |
| BMI (kg/m2) | +0.0132 | 0.0106 | ±0.0212 | +1.240 | 0.2148 |  |
| Hypertension | +0.3078 | 0.1600 | ±0.3199 | +1.924 | 0.0543 | . |
| High cholesterol | -0.1556 | 0.1571 | ±0.3142 | -0.990 | 0.3220 |  |
| Kidney disease | -0.1447 | 0.1914 | ±0.3829 | -0.756 | 0.4499 |  |
| Circulatory disease | +0.2240 | 0.1911 | ±0.3823 | +1.172 | 0.2413 |  |
| Avg. daily time 54-69 (%) | +0.0524 | 0.0485 | ±0.0971 | +1.080 | 0.2803 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **849**, R² = **0.2630**, Adj R² = **0.2507**, F-statistic = **21.26** (p = **1.40e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.5**, BIC = **3766.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1025** | 0.6477 | ±1.2953 | **+37.214** | **4.00e-303** | *** |
| Education: graduate level (vs college) | -0.0663 | 0.1625 | ±0.3251 | -0.408 | 0.6835 |  |
| Education: high school or below (vs college) | +0.2203 | 0.2227 | ±0.4455 | +0.989 | 0.3225 |  |
| Site: UCSD (vs UAB) | -0.1232 | 0.1788 | ±0.3576 | -0.689 | 0.4908 |  |
| **Site: UW (vs UAB)** | **-1.3747** | 0.1837 | ±0.3673 | **-7.484** | **7.20e-14** | *** |
| Season: spring (vs autumn) | -0.2173 | 0.1967 | ±0.3934 | -1.105 | 0.2694 |  |
| **Season: summer (vs autumn)** | **+1.7966** | 0.2205 | ±0.4410 | **+8.148** | **3.69e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1943** | 0.2142 | ±0.4284 | **-5.576** | **2.46e-08** | *** |
| Age (years) | +0.0093 | 0.0075 | ±0.0150 | +1.241 | 0.2144 |  |
| BMI (kg/m2) | +0.0132 | 0.0106 | ±0.0212 | +1.244 | 0.2137 |  |
| Hypertension | +0.3079 | 0.1602 | ±0.3205 | +1.922 | 0.0546 | . |
| High cholesterol | -0.1564 | 0.1571 | ±0.3142 | -0.995 | 0.3196 |  |
| Kidney disease | -0.1447 | 0.1916 | ±0.3832 | -0.755 | 0.4500 |  |
| Circulatory disease | +0.2230 | 0.1911 | ±0.3821 | +1.167 | 0.2431 |  |
| Time < 70 (%) | +0.0313 | 0.0418 | ±0.0837 | +0.748 | 0.4543 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **849**, R² = **0.2634**, Adj R² = **0.2510**, F-statistic = **21.30** (p = **1.16e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.1**, BIC = **3766.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1086** | 0.6466 | ±1.2933 | **+37.283** | **3.08e-304** | *** |
| Education: graduate level (vs college) | -0.0637 | 0.1624 | ±0.3248 | -0.393 | 0.6947 |  |
| Education: high school or below (vs college) | +0.2195 | 0.2229 | ±0.4457 | +0.985 | 0.3246 |  |
| Site: UCSD (vs UAB) | -0.1216 | 0.1788 | ±0.3576 | -0.680 | 0.4963 |  |
| **Site: UW (vs UAB)** | **-1.3725** | 0.1836 | ±0.3673 | **-7.474** | **7.76e-14** | *** |
| Season: spring (vs autumn) | -0.2145 | 0.1966 | ±0.3933 | -1.091 | 0.2754 |  |
| **Season: summer (vs autumn)** | **+1.7974** | 0.2205 | ±0.4410 | **+8.151** | **3.61e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1932** | 0.2142 | ±0.4283 | **-5.571** | **2.53e-08** | *** |
| Age (years) | +0.0091 | 0.0075 | ±0.0149 | +1.216 | 0.2240 |  |
| BMI (kg/m2) | +0.0132 | 0.0106 | ±0.0212 | +1.243 | 0.2139 |  |
| Hypertension | +0.3077 | 0.1600 | ±0.3201 | +1.923 | 0.0545 | . |
| High cholesterol | -0.1549 | 0.1571 | ±0.3141 | -0.986 | 0.3240 |  |
| Kidney disease | -0.1444 | 0.1914 | ±0.3828 | -0.754 | 0.4507 |  |
| Circulatory disease | +0.2226 | 0.1910 | ±0.3821 | +1.165 | 0.2439 |  |
| Avg. daily time < 70 (%) | +0.0392 | 0.0409 | ±0.0819 | +0.956 | 0.3389 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.2626**, Adj R² = **0.2503**, F-statistic = **21.22** (p = **1.75e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.0**, BIC = **3767.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9689** | 0.8084 | ±1.6168 | **+29.650** | **3.43e-193** | *** |
| Education: graduate level (vs college) | -0.0770 | 0.1632 | ±0.3263 | -0.472 | 0.6369 |  |
| Education: high school or below (vs college) | +0.2244 | 0.2245 | ±0.4490 | +0.999 | 0.3176 |  |
| Site: UCSD (vs UAB) | -0.1395 | 0.1799 | ±0.3597 | -0.775 | 0.4381 |  |
| **Site: UW (vs UAB)** | **-1.3916** | 0.1854 | ±0.3707 | **-7.508** | **6.02e-14** | *** |
| Season: spring (vs autumn) | -0.2264 | 0.1967 | ±0.3934 | -1.151 | 0.2496 |  |
| **Season: summer (vs autumn)** | **+1.7859** | 0.2228 | ±0.4456 | **+8.016** | **1.10e-15** | *** |
| **Season: winter (vs autumn)** | **-1.2015** | 0.2135 | ±0.4271 | **-5.626** | **1.84e-08** | *** |
| Age (years) | +0.0094 | 0.0075 | ±0.0150 | +1.256 | 0.2090 |  |
| BMI (kg/m2) | +0.0135 | 0.0106 | ±0.0212 | +1.273 | 0.2030 |  |
| Hypertension | +0.3105 | 0.1596 | ±0.3192 | +1.946 | 0.0517 | . |
| High cholesterol | -0.1592 | 0.1574 | ±0.3148 | -1.012 | 0.3118 |  |
| Kidney disease | -0.1403 | 0.1914 | ±0.3827 | -0.733 | 0.4634 |  |
| Circulatory disease | +0.2301 | 0.1917 | ±0.3834 | +1.200 | 0.2300 |  |
| Time 54-250, pooled (%) | +0.0016 | 0.0052 | ±0.0105 | +0.313 | 0.7540 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.2626**, Adj R² = **0.2503**, F-statistic = **21.22** (p = **1.74e-46**), Residual SE = **2.115** on **834** df, AIC = **3695.9**, BIC = **3767.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9536** | 0.8181 | ±1.6361 | **+29.281** | **1.82e-188** | *** |
| Education: graduate level (vs college) | -0.0774 | 0.1632 | ±0.3264 | -0.474 | 0.6355 |  |
| Education: high school or below (vs college) | +0.2248 | 0.2244 | ±0.4489 | +1.002 | 0.3164 |  |
| Site: UCSD (vs UAB) | -0.1399 | 0.1799 | ±0.3597 | -0.778 | 0.4367 |  |
| **Site: UW (vs UAB)** | **-1.3918** | 0.1853 | ±0.3707 | **-7.510** | **5.92e-14** | *** |
| Season: spring (vs autumn) | -0.2262 | 0.1966 | ±0.3933 | -1.150 | 0.2499 |  |
| **Season: summer (vs autumn)** | **+1.7859** | 0.2227 | ±0.4455 | **+8.018** | **1.07e-15** | *** |
| **Season: winter (vs autumn)** | **-1.2011** | 0.2135 | ±0.4271 | **-5.625** | **1.86e-08** | *** |
| Age (years) | +0.0094 | 0.0075 | ±0.0150 | +1.259 | 0.2082 |  |
| BMI (kg/m2) | +0.0135 | 0.0106 | ±0.0212 | +1.274 | 0.2028 |  |
| Hypertension | +0.3104 | 0.1596 | ±0.3193 | +1.945 | 0.0518 | . |
| High cholesterol | -0.1593 | 0.1574 | ±0.3148 | -1.012 | 0.3114 |  |
| Kidney disease | -0.1396 | 0.1914 | ±0.3828 | -0.729 | 0.4659 |  |
| Circulatory disease | +0.2304 | 0.1917 | ±0.3835 | +1.202 | 0.2295 |  |
| Avg. daily time 54-250 (%) | +0.0018 | 0.0053 | ±0.0106 | +0.336 | 0.7369 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.2635**, Adj R² = **0.2511**, F-statistic = **21.31** (p = **1.11e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.0**, BIC = **3766.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1265** | 0.6482 | ±1.2964 | **+37.219** | **3.31e-303** | *** |
| Education: graduate level (vs college) | -0.0776 | 0.1626 | ±0.3252 | -0.478 | 0.6330 |  |
| Education: high school or below (vs college) | +0.2344 | 0.2240 | ±0.4480 | +1.046 | 0.2954 |  |
| Site: UCSD (vs UAB) | -0.1491 | 0.1783 | ±0.3566 | -0.836 | 0.4031 |  |
| **Site: UW (vs UAB)** | **-1.3841** | 0.1839 | ±0.3678 | **-7.527** | **5.21e-14** | *** |
| Season: spring (vs autumn) | -0.2179 | 0.1965 | ±0.3929 | -1.109 | 0.2675 |  |
| **Season: summer (vs autumn)** | **+1.7982** | 0.2200 | ±0.4399 | **+8.175** | **2.95e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1876** | 0.2149 | ±0.4297 | **-5.527** | **3.26e-08** | *** |
| Age (years) | +0.0105 | 0.0076 | ±0.0152 | +1.381 | 0.1673 |  |
| BMI (kg/m2) | +0.0138 | 0.0106 | ±0.0213 | +1.301 | 0.1931 |  |
| Hypertension | +0.2971 | 0.1612 | ±0.3224 | +1.843 | 0.0653 | . |
| High cholesterol | -0.1646 | 0.1578 | ±0.3157 | -1.043 | 0.2969 |  |
| Kidney disease | -0.1270 | 0.1902 | ±0.3803 | -0.668 | 0.5043 |  |
| Circulatory disease | +0.2317 | 0.1916 | ±0.3832 | +1.209 | 0.2265 |  |
| Time 181-250, pooled (%) | -0.0049 | 0.0048 | ±0.0097 | -1.020 | 0.3079 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **849**, R² = **0.2637**, Adj R² = **0.2513**, F-statistic = **21.33** (p = **1.00e-46**), Residual SE = **2.113** on **834** df, AIC = **3694.8**, BIC = **3765.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1285** | 0.6486 | ±1.2972 | **+37.202** | **6.41e-303** | *** |
| Education: graduate level (vs college) | -0.0776 | 0.1626 | ±0.3251 | -0.478 | 0.6330 |  |
| Education: high school or below (vs college) | +0.2371 | 0.2241 | ±0.4483 | +1.058 | 0.2900 |  |
| Site: UCSD (vs UAB) | -0.1513 | 0.1784 | ±0.3568 | -0.848 | 0.3963 |  |
| **Site: UW (vs UAB)** | **-1.3847** | 0.1839 | ±0.3678 | **-7.528** | **5.13e-14** | *** |
| Season: spring (vs autumn) | -0.2172 | 0.1964 | ±0.3928 | -1.106 | 0.2688 |  |
| **Season: summer (vs autumn)** | **+1.7989** | 0.2200 | ±0.4399 | **+8.179** | **2.87e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1854** | 0.2150 | ±0.4301 | **-5.512** | **3.54e-08** | *** |
| Age (years) | +0.0106 | 0.0076 | ±0.0152 | +1.389 | 0.1649 |  |
| BMI (kg/m2) | +0.0139 | 0.0106 | ±0.0213 | +1.305 | 0.1918 |  |
| Hypertension | +0.2963 | 0.1612 | ±0.3223 | +1.838 | 0.0660 | . |
| High cholesterol | -0.1648 | 0.1578 | ±0.3156 | -1.044 | 0.2963 |  |
| Kidney disease | -0.1251 | 0.1900 | ±0.3800 | -0.658 | 0.5104 |  |
| Circulatory disease | +0.2315 | 0.1916 | ±0.3833 | +1.208 | 0.2270 |  |
| Avg. daily time 181-250 (%) | -0.0053 | 0.0048 | ±0.0095 | -1.109 | 0.2673 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **849**, R² = **0.2631**, Adj R² = **0.2508**, F-statistic = **21.27** (p = **1.32e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.4**, BIC = **3766.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1440** | 0.6487 | ±1.2974 | **+37.219** | **3.41e-303** | *** |
| Education: graduate level (vs college) | -0.0821 | 0.1630 | ±0.3260 | -0.503 | 0.6147 |  |
| Education: high school or below (vs college) | +0.2354 | 0.2249 | ±0.4497 | +1.047 | 0.2952 |  |
| Site: UCSD (vs UAB) | -0.1483 | 0.1796 | ±0.3591 | -0.826 | 0.4090 |  |
| **Site: UW (vs UAB)** | **-1.3922** | 0.1846 | ±0.3693 | **-7.540** | **4.71e-14** | *** |
| Season: spring (vs autumn) | -0.2230 | 0.1963 | ±0.3927 | -1.136 | 0.2561 |  |
| **Season: summer (vs autumn)** | **+1.7871** | 0.2218 | ±0.4436 | **+8.057** | **7.80e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1938** | 0.2141 | ±0.4282 | **-5.576** | **2.46e-08** | *** |
| Age (years) | +0.0099 | 0.0075 | ±0.0151 | +1.313 | 0.1892 |  |
| BMI (kg/m2) | +0.0138 | 0.0106 | ±0.0213 | +1.293 | 0.1959 |  |
| Hypertension | +0.3045 | 0.1607 | ±0.3215 | +1.895 | 0.0581 | . |
| High cholesterol | -0.1631 | 0.1578 | ±0.3155 | -1.034 | 0.3012 |  |
| Kidney disease | -0.1291 | 0.1906 | ±0.3811 | -0.678 | 0.4981 |  |
| Circulatory disease | +0.2317 | 0.1917 | ±0.3834 | +1.209 | 0.2267 |  |
| Time > 180 (%) | -0.0024 | 0.0031 | ±0.0062 | -0.778 | 0.4363 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **849**, R² = **0.2633**, Adj R² = **0.2509**, F-statistic = **21.29** (p = **1.24e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.2**, BIC = **3766.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1442** | 0.6487 | ±1.2975 | **+37.217** | **3.56e-303** | *** |
| Education: graduate level (vs college) | -0.0826 | 0.1630 | ±0.3260 | -0.507 | 0.6123 |  |
| Education: high school or below (vs college) | +0.2376 | 0.2249 | ±0.4498 | +1.056 | 0.2908 |  |
| Site: UCSD (vs UAB) | -0.1502 | 0.1796 | ±0.3593 | -0.836 | 0.4032 |  |
| **Site: UW (vs UAB)** | **-1.3927** | 0.1847 | ±0.3693 | **-7.542** | **4.61e-14** | *** |
| Season: spring (vs autumn) | -0.2222 | 0.1963 | ±0.3926 | -1.132 | 0.2577 |  |
| **Season: summer (vs autumn)** | **+1.7874** | 0.2216 | ±0.4433 | **+8.065** | **7.34e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1921** | 0.2142 | ±0.4284 | **-5.565** | **2.62e-08** | *** |
| Age (years) | +0.0099 | 0.0075 | ±0.0151 | +1.320 | 0.1869 |  |
| BMI (kg/m2) | +0.0138 | 0.0106 | ±0.0213 | +1.297 | 0.1945 |  |
| Hypertension | +0.3039 | 0.1608 | ±0.3215 | +1.890 | 0.0587 | . |
| High cholesterol | -0.1634 | 0.1577 | ±0.3154 | -1.036 | 0.3003 |  |
| Kidney disease | -0.1269 | 0.1904 | ±0.3809 | -0.666 | 0.5052 |  |
| Circulatory disease | +0.2320 | 0.1917 | ±0.3834 | +1.211 | 0.2261 |  |
| Avg. daily time > 180 (%) | -0.0026 | 0.0031 | ±0.0062 | -0.852 | 0.3942 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **849**, R² = **0.2632**, Adj R² = **0.2508**, F-statistic = **21.28** (p = **1.28e-46**), Residual SE = **2.114** on **834** df, AIC = **3695.3**, BIC = **3766.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1402** | 0.6485 | ±1.2969 | **+37.227** | **2.51e-303** | *** |
| Education: graduate level (vs college) | -0.0850 | 0.1636 | ±0.3271 | -0.519 | 0.6035 |  |
| Education: high school or below (vs college) | +0.2350 | 0.2246 | ±0.4492 | +1.046 | 0.2954 |  |
| Site: UCSD (vs UAB) | -0.1502 | 0.1799 | ±0.3598 | -0.835 | 0.4038 |  |
| **Site: UW (vs UAB)** | **-1.3910** | 0.1846 | ±0.3693 | **-7.534** | **4.92e-14** | *** |
| Season: spring (vs autumn) | -0.2220 | 0.1963 | ±0.3926 | -1.131 | 0.2582 |  |
| **Season: summer (vs autumn)** | **+1.7862** | 0.2218 | ±0.4436 | **+8.053** | **8.07e-16** | *** |
| **Season: winter (vs autumn)** | **-1.1929** | 0.2140 | ±0.4280 | **-5.574** | **2.49e-08** | *** |
| Age (years) | +0.0096 | 0.0075 | ±0.0150 | +1.277 | 0.2016 |  |
| BMI (kg/m2) | +0.0142 | 0.0107 | ±0.0215 | +1.323 | 0.1857 |  |
| Hypertension | +0.3037 | 0.1608 | ±0.3215 | +1.889 | 0.0589 | . |
| High cholesterol | -0.1636 | 0.1577 | ±0.3153 | -1.038 | 0.2994 |  |
| Kidney disease | -0.1311 | 0.1901 | ±0.3803 | -0.690 | 0.4904 |  |
| Circulatory disease | +0.2325 | 0.1918 | ±0.3836 | +1.212 | 0.2255 |  |
| Nocturnal time > 180 (%) | -0.0024 | 0.0030 | ±0.0060 | -0.807 | 0.4195 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.2627**, Adj R² = **0.2503**, F-statistic = **21.22** (p = **1.69e-46**), Residual SE = **2.115** on **834** df, AIC = **3695.9**, BIC = **3767.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1374** | 0.6510 | ±1.3019 | **+37.079** | **6.16e-301** | *** |
| Education: graduate level (vs college) | -0.0785 | 0.1634 | ±0.3269 | -0.480 | 0.6311 |  |
| Education: high school or below (vs college) | +0.2216 | 0.2231 | ±0.4462 | +0.993 | 0.3206 |  |
| Site: UCSD (vs UAB) | -0.1386 | 0.1786 | ±0.3573 | -0.776 | 0.4378 |  |
| **Site: UW (vs UAB)** | **-1.3847** | 0.1838 | ±0.3675 | **-7.536** | **4.85e-14** | *** |
| Season: spring (vs autumn) | -0.2265 | 0.1966 | ±0.3933 | -1.152 | 0.2495 |  |
| **Season: summer (vs autumn)** | **+1.7914** | 0.2210 | ±0.4420 | **+8.106** | **5.23e-16** | *** |
| **Season: winter (vs autumn)** | **-1.2017** | 0.2135 | ±0.4270 | **-5.629** | **1.82e-08** | *** |
| Age (years) | +0.0100 | 0.0076 | ±0.0153 | +1.310 | 0.1901 |  |
| BMI (kg/m2) | +0.0132 | 0.0106 | ±0.0212 | +1.246 | 0.2126 |  |
| Hypertension | +0.3065 | 0.1604 | ±0.3208 | +1.911 | 0.0560 | . |
| High cholesterol | -0.1589 | 0.1574 | ±0.3148 | -1.010 | 0.3126 |  |
| Kidney disease | -0.1373 | 0.1916 | ±0.3832 | -0.716 | 0.4737 |  |
| Circulatory disease | +0.2279 | 0.1916 | ±0.3833 | +1.189 | 0.2343 |  |
| Any reading > 250 during wear (0/1) | -0.0675 | 0.1616 | ±0.3233 | -0.418 | 0.6762 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.2626**, Adj R² = **0.2503**, F-statistic = **21.22** (p = **1.75e-46**), Residual SE = **2.115** on **834** df, AIC = **3696.0**, BIC = **3767.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1331** | 0.6487 | ±1.2974 | **+37.203** | **6.03e-303** | *** |
| Education: graduate level (vs college) | -0.0771 | 0.1632 | ±0.3263 | -0.472 | 0.6367 |  |
| Education: high school or below (vs college) | +0.2246 | 0.2245 | ±0.4491 | +1.000 | 0.3172 |  |
| Site: UCSD (vs UAB) | -0.1394 | 0.1798 | ±0.3595 | -0.775 | 0.4382 |  |
| **Site: UW (vs UAB)** | **-1.3915** | 0.1853 | ±0.3706 | **-7.510** | **5.92e-14** | *** |
| Season: spring (vs autumn) | -0.2264 | 0.1967 | ±0.3934 | -1.151 | 0.2497 |  |
| **Season: summer (vs autumn)** | **+1.7859** | 0.2228 | ±0.4456 | **+8.015** | **1.10e-15** | *** |
| **Season: winter (vs autumn)** | **-1.2014** | 0.2135 | ±0.4271 | **-5.626** | **1.85e-08** | *** |
| Age (years) | +0.0094 | 0.0075 | ±0.0150 | +1.256 | 0.2090 |  |
| BMI (kg/m2) | +0.0135 | 0.0106 | ±0.0212 | +1.273 | 0.2031 |  |
| Hypertension | +0.3105 | 0.1596 | ±0.3192 | +1.945 | 0.0517 | . |
| High cholesterol | -0.1592 | 0.1574 | ±0.3148 | -1.011 | 0.3118 |  |
| Kidney disease | -0.1402 | 0.1914 | ±0.3827 | -0.733 | 0.4638 |  |
| Circulatory disease | +0.2300 | 0.1917 | ±0.3834 | +1.200 | 0.2302 |  |
| Time > 250 (%) | -0.0017 | 0.0052 | ±0.0105 | -0.319 | 0.7499 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 849)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.2627**, Adj R² = **0.2503**, F-statistic = **21.22** (p = **1.73e-46**), Residual SE = **2.115** on **834** df, AIC = **3695.9**, BIC = **3767.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1326** | 0.6482 | ±1.2963 | **+37.233** | **2.02e-303** | *** |
| Education: graduate level (vs college) | -0.0774 | 0.1632 | ±0.3264 | -0.474 | 0.6352 |  |
| Education: high school or below (vs college) | +0.2251 | 0.2244 | ±0.4489 | +1.003 | 0.3158 |  |
| Site: UCSD (vs UAB) | -0.1399 | 0.1798 | ±0.3596 | -0.778 | 0.4366 |  |
| **Site: UW (vs UAB)** | **-1.3918** | 0.1853 | ±0.3705 | **-7.512** | **5.82e-14** | *** |
| Season: spring (vs autumn) | -0.2261 | 0.1966 | ±0.3933 | -1.150 | 0.2501 |  |
| **Season: summer (vs autumn)** | **+1.7859** | 0.2227 | ±0.4455 | **+8.018** | **1.07e-15** | *** |
| **Season: winter (vs autumn)** | **-1.2010** | 0.2135 | ±0.4271 | **-5.624** | **1.86e-08** | *** |
| Age (years) | +0.0094 | 0.0075 | ±0.0150 | +1.258 | 0.2083 |  |
| BMI (kg/m2) | +0.0135 | 0.0106 | ±0.0213 | +1.274 | 0.2028 |  |
| Hypertension | +0.3104 | 0.1597 | ±0.3193 | +1.944 | 0.0518 | . |
| High cholesterol | -0.1593 | 0.1574 | ±0.3148 | -1.012 | 0.3115 |  |
| Kidney disease | -0.1394 | 0.1914 | ±0.3828 | -0.728 | 0.4664 |  |
| Circulatory disease | +0.2303 | 0.1917 | ±0.3834 | +1.201 | 0.2297 |  |
| Avg. daily time > 250 (%) | -0.0018 | 0.0053 | ±0.0106 | -0.345 | 0.7301 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 849; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **849**, R² = **0.2259**, Adj R² = **0.2139**, F-statistic = **18.75** (p = **1.01e-38**), Residual SE = **6.185** on **835** df, AIC = **5517.2**, BIC = **5583.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0582** | 1.9391 | ±3.8782 | **+25.815** | **5.97e-147** | *** |
| Education: graduate level (vs college) | +0.0789 | 0.4778 | ±0.9557 | +0.165 | 0.8688 |  |
| Education: high school or below (vs college) | +0.2951 | 0.6343 | ±1.2685 | +0.465 | 0.6417 |  |
| **Site: UCSD (vs UAB)** | **+3.4705** | 0.5184 | ±1.0369 | **+6.694** | **2.17e-11** | *** |
| Site: UW (vs UAB) | -0.3932 | 0.5183 | ±1.0365 | -0.759 | 0.4480 |  |
| **Season: spring (vs autumn)** | **-2.0506** | 0.6033 | ±1.2066 | **-3.399** | **6.76e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3622** | 0.5794 | ±1.1588 | **+2.351** | **0.0187** | * |
| **Season: winter (vs autumn)** | **-5.9896** | 0.6729 | ±1.3458 | **-8.901** | **5.54e-19** | *** |
| **Age (years)** | **-0.0477** | 0.0214 | ±0.0427 | **-2.233** | **0.0256** | * |
| BMI (kg/m2) | -0.0270 | 0.0337 | ±0.0674 | -0.801 | 0.4234 |  |
| Hypertension | -0.2595 | 0.4895 | ±0.9791 | -0.530 | 0.5961 |  |
| **High cholesterol** | **-0.9368** | 0.4668 | ±0.9336 | **-2.007** | **0.0448** | * |
| **Kidney disease** | **+1.2889** | 0.5516 | ±1.1031 | **+2.337** | **0.0195** | * |
| Circulatory disease | -0.1407 | 0.5400 | ±1.0799 | -0.261 | 0.7944 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **849**, R² = **0.2260**, Adj R² = **0.2131**, F-statistic = **17.40** (p = **4.23e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.0**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.4232** | 2.1999 | ±4.3997 | **+22.921** | **2.87e-116** | *** |
| Education: graduate level (vs college) | +0.0643 | 0.4804 | ±0.9609 | +0.134 | 0.8936 |  |
| Education: high school or below (vs college) | +0.3194 | 0.6380 | ±1.2760 | +0.501 | 0.6166 |  |
| **Site: UCSD (vs UAB)** | **+3.4602** | 0.5227 | ±1.0454 | **+6.620** | **3.60e-11** | *** |
| Site: UW (vs UAB) | -0.4018 | 0.5205 | ±1.0410 | -0.772 | 0.4401 |  |
| **Season: spring (vs autumn)** | **-2.0566** | 0.6051 | ±1.2102 | **-3.399** | **6.77e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3540** | 0.5804 | ±1.1607 | **+2.333** | **0.0197** | * |
| **Season: winter (vs autumn)** | **-5.9855** | 0.6743 | ±1.3486 | **-8.876** | **6.90e-19** | *** |
| **Age (years)** | **-0.0474** | 0.0214 | ±0.0429 | **-2.210** | **0.0271** | * |
| BMI (kg/m2) | -0.0261 | 0.0339 | ±0.0678 | -0.769 | 0.4419 |  |
| Hypertension | -0.2589 | 0.4901 | ±0.9803 | -0.528 | 0.5974 |  |
| **High cholesterol** | **-0.9370** | 0.4674 | ±0.9347 | **-2.005** | **0.0450** | * |
| **Kidney disease** | **+1.2932** | 0.5536 | ±1.1072 | **+2.336** | **0.0195** | * |
| Circulatory disease | -0.1378 | 0.5412 | ±1.0825 | -0.255 | 0.7990 |  |
| HbA1c (%) | -0.0604 | 0.1754 | ±0.3509 | -0.344 | 0.7308 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **849**, R² = **0.2259**, Adj R² = **0.2129**, F-statistic = **17.39** (p = **4.49e-38**), Residual SE = **6.189** on **834** df, AIC = **5519.2**, BIC = **5590.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0187** | 2.0427 | ±4.0855 | **+24.486** | **2.07e-132** | *** |
| Education: graduate level (vs college) | +0.0809 | 0.4796 | ±0.9593 | +0.169 | 0.8661 |  |
| Education: high school or below (vs college) | +0.2921 | 0.6369 | ±1.2738 | +0.459 | 0.6465 |  |
| **Site: UCSD (vs UAB)** | **+3.4725** | 0.5247 | ±1.0494 | **+6.618** | **3.64e-11** | *** |
| Site: UW (vs UAB) | -0.3923 | 0.5208 | ±1.0416 | -0.753 | 0.4513 |  |
| **Season: spring (vs autumn)** | **-2.0512** | 0.6036 | ±1.2073 | **-3.398** | **6.79e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3630** | 0.5801 | ±1.1602 | **+2.350** | **0.0188** | * |
| **Season: winter (vs autumn)** | **-5.9911** | 0.6766 | ±1.3532 | **-8.854** | **8.41e-19** | *** |
| **Age (years)** | **-0.0477** | 0.0215 | ±0.0429 | **-2.226** | **0.0260** | * |
| BMI (kg/m2) | -0.0270 | 0.0339 | ±0.0677 | -0.798 | 0.4251 |  |
| Hypertension | -0.2590 | 0.4908 | ±0.9816 | -0.528 | 0.5978 |  |
| **High cholesterol** | **-0.9361** | 0.4677 | ±0.9354 | **-2.002** | **0.0453** | * |
| **Kidney disease** | **+1.2862** | 0.5531 | ±1.1062 | **+2.325** | **0.0200** | * |
| Circulatory disease | -0.1410 | 0.5408 | ±1.0816 | -0.261 | 0.7942 |  |
| Mean glucose (mg/dL) | +0.0003 | 0.0055 | ±0.0110 | +0.052 | 0.9588 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **849**, R² = **0.2259**, Adj R² = **0.2129**, F-statistic = **17.39** (p = **4.49e-38**), Residual SE = **6.189** on **834** df, AIC = **5519.2**, BIC = **5590.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.9794** | 2.3950 | ±4.7900 | **+20.868** | **1.05e-96** | *** |
| Education: graduate level (vs college) | +0.0809 | 0.4796 | ±0.9593 | +0.169 | 0.8661 |  |
| Education: high school or below (vs college) | +0.2921 | 0.6369 | ±1.2738 | +0.459 | 0.6465 |  |
| **Site: UCSD (vs UAB)** | **+3.4725** | 0.5247 | ±1.0494 | **+6.618** | **3.64e-11** | *** |
| Site: UW (vs UAB) | -0.3923 | 0.5208 | ±1.0416 | -0.753 | 0.4513 |  |
| **Season: spring (vs autumn)** | **-2.0512** | 0.6036 | ±1.2073 | **-3.398** | **6.79e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3630** | 0.5801 | ±1.1602 | **+2.350** | **0.0188** | * |
| **Season: winter (vs autumn)** | **-5.9911** | 0.6766 | ±1.3532 | **-8.854** | **8.41e-19** | *** |
| **Age (years)** | **-0.0477** | 0.0215 | ±0.0429 | **-2.226** | **0.0260** | * |
| BMI (kg/m2) | -0.0270 | 0.0339 | ±0.0677 | -0.798 | 0.4251 |  |
| Hypertension | -0.2590 | 0.4908 | ±0.9816 | -0.528 | 0.5978 |  |
| **High cholesterol** | **-0.9361** | 0.4677 | ±0.9354 | **-2.002** | **0.0453** | * |
| **Kidney disease** | **+1.2862** | 0.5531 | ±1.1062 | **+2.325** | **0.0200** | * |
| Circulatory disease | -0.1410 | 0.5408 | ±1.0816 | -0.261 | 0.7942 |  |
| GMI (%) | +0.0119 | 0.2301 | ±0.4603 | +0.052 | 0.9588 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **849**, R² = **0.2260**, Adj R² = **0.2130**, F-statistic = **17.39** (p = **4.39e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.1**, BIC = **5590.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2200** | 2.0238 | ±4.0476 | **+24.815** | **6.19e-136** | *** |
| Education: graduate level (vs college) | +0.0710 | 0.4799 | ±0.9597 | +0.148 | 0.8824 |  |
| Education: high school or below (vs college) | +0.3070 | 0.6365 | ±1.2729 | +0.482 | 0.6295 |  |
| **Site: UCSD (vs UAB)** | **+3.4628** | 0.5243 | ±1.0486 | **+6.605** | **3.99e-11** | *** |
| Site: UW (vs UAB) | -0.3941 | 0.5192 | ±1.0385 | -0.759 | 0.4478 |  |
| **Season: spring (vs autumn)** | **-2.0465** | 0.6032 | ±1.2064 | **-3.393** | **6.92e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3594** | 0.5802 | ±1.1604 | **+2.343** | **0.0191** | * |
| **Season: winter (vs autumn)** | **-5.9824** | 0.6769 | ±1.3539 | **-8.837** | **9.80e-19** | *** |
| **Age (years)** | **-0.0477** | 0.0214 | ±0.0428 | **-2.230** | **0.0257** | * |
| BMI (kg/m2) | -0.0265 | 0.0341 | ±0.0682 | -0.776 | 0.4378 |  |
| Hypertension | -0.2624 | 0.4914 | ±0.9828 | -0.534 | 0.5933 |  |
| **High cholesterol** | **-0.9387** | 0.4673 | ±0.9347 | **-2.009** | **0.0446** | * |
| **Kidney disease** | **+1.2959** | 0.5523 | ±1.1047 | **+2.346** | **0.0190** | * |
| Circulatory disease | -0.1394 | 0.5408 | ±1.0816 | -0.258 | 0.7966 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0012 | 0.0053 | ±0.0107 | -0.219 | 0.8266 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **849**, R² = **0.2262**, Adj R² = **0.2132**, F-statistic = **17.41** (p = **3.97e-38**), Residual SE = **6.188** on **834** df, AIC = **5518.9**, BIC = **5590.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2740** | 2.0122 | ±4.0243 | **+24.985** | **8.87e-138** | *** |
| Education: graduate level (vs college) | +0.0569 | 0.4830 | ±0.9659 | +0.118 | 0.9063 |  |
| Education: high school or below (vs college) | +0.3280 | 0.6346 | ±1.2691 | +0.517 | 0.6053 |  |
| **Site: UCSD (vs UAB)** | **+3.4510** | 0.5254 | ±1.0509 | **+6.568** | **5.11e-11** | *** |
| Site: UW (vs UAB) | -0.4128 | 0.5239 | ±1.0478 | -0.788 | 0.4307 |  |
| **Season: spring (vs autumn)** | **-2.0464** | 0.6031 | ±1.2062 | **-3.393** | **6.91e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3516** | 0.5804 | ±1.1609 | **+2.329** | **0.0199** | * |
| **Season: winter (vs autumn)** | **-5.9782** | 0.6750 | ±1.3499 | **-8.857** | **8.20e-19** | *** |
| **Age (years)** | **-0.0465** | 0.0214 | ±0.0429 | **-2.168** | **0.0302** | * |
| BMI (kg/m2) | -0.0269 | 0.0336 | ±0.0673 | -0.800 | 0.4235 |  |
| Hypertension | -0.2612 | 0.4904 | ±0.9808 | -0.533 | 0.5943 |  |
| **High cholesterol** | **-0.9467** | 0.4678 | ±0.9355 | **-2.024** | **0.0430** | * |
| **Kidney disease** | **+1.3420** | 0.5563 | ±1.1126 | **+2.412** | **0.0159** | * |
| Circulatory disease | -0.1351 | 0.5404 | ±1.0808 | -0.250 | 0.8026 |  |
| Glucose SD, pooled (mg/dL) | -0.0081 | 0.0157 | ±0.0313 | -0.518 | 0.6043 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.40** (p = **4.22e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.0**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2236** | 2.0171 | ±4.0342 | **+24.899** | **7.68e-137** | *** |
| Education: graduate level (vs college) | +0.0643 | 0.4828 | ±0.9655 | +0.133 | 0.8941 |  |
| Education: high school or below (vs college) | +0.3206 | 0.6354 | ±1.2708 | +0.505 | 0.6139 |  |
| **Site: UCSD (vs UAB)** | **+3.4573** | 0.5252 | ±1.0505 | **+6.582** | **4.63e-11** | *** |
| Site: UW (vs UAB) | -0.4056 | 0.5238 | ±1.0475 | -0.774 | 0.4387 |  |
| **Season: spring (vs autumn)** | **-2.0472** | 0.6032 | ±1.2065 | **-3.394** | **6.90e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3530** | 0.5809 | ±1.1618 | **+2.329** | **0.0199** | * |
| **Season: winter (vs autumn)** | **-5.9832** | 0.6744 | ±1.3488 | **-8.872** | **7.20e-19** | *** |
| **Age (years)** | **-0.0468** | 0.0215 | ±0.0430 | **-2.176** | **0.0295** | * |
| BMI (kg/m2) | -0.0273 | 0.0336 | ±0.0673 | -0.811 | 0.4176 |  |
| Hypertension | -0.2614 | 0.4906 | ±0.9812 | -0.533 | 0.5942 |  |
| **High cholesterol** | **-0.9438** | 0.4677 | ±0.9354 | **-2.018** | **0.0436** | * |
| **Kidney disease** | **+1.3280** | 0.5563 | ±1.1126 | **+2.387** | **0.0170** | * |
| Circulatory disease | -0.1387 | 0.5402 | ±1.0805 | -0.257 | 0.7974 |  |
| Avg. daily SD (mg/dL) | -0.0066 | 0.0179 | ±0.0357 | -0.371 | 0.7105 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **849**, R² = **0.2265**, Adj R² = **0.2135**, F-statistic = **17.45** (p = **3.31e-38**), Residual SE = **6.186** on **834** df, AIC = **5518.5**, BIC = **5589.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.6122** | 2.1463 | ±4.2927 | **+23.581** | **6.08e-123** | *** |
| Education: graduate level (vs college) | +0.0535 | 0.4824 | ±0.9647 | +0.111 | 0.9117 |  |
| Education: high school or below (vs college) | +0.3355 | 0.6330 | ±1.2660 | +0.530 | 0.5961 |  |
| **Site: UCSD (vs UAB)** | **+3.4471** | 0.5221 | ±1.0443 | **+6.602** | **4.06e-11** | *** |
| Site: UW (vs UAB) | -0.4288 | 0.5235 | ±1.0469 | -0.819 | 0.4127 |  |
| **Season: spring (vs autumn)** | **-2.0535** | 0.6035 | ±1.2069 | **-3.403** | **6.67e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3517** | 0.5800 | ±1.1600 | **+2.331** | **0.0198** | * |
| **Season: winter (vs autumn)** | **-5.9850** | 0.6739 | ±1.3479 | **-8.881** | **6.64e-19** | *** |
| **Age (years)** | **-0.0453** | 0.0214 | ±0.0427 | **-2.122** | **0.0339** | * |
| BMI (kg/m2) | -0.0276 | 0.0337 | ±0.0674 | -0.818 | 0.4131 |  |
| Hypertension | -0.2535 | 0.4896 | ±0.9792 | -0.518 | 0.6046 |  |
| **High cholesterol** | **-0.9509** | 0.4674 | ±0.9349 | **-2.034** | **0.0419** | * |
| **Kidney disease** | **+1.3747** | 0.5571 | ±1.1142 | **+2.468** | **0.0136** | * |
| Circulatory disease | -0.1308 | 0.5399 | ±1.0798 | -0.242 | 0.8086 |  |
| CV (%) | -0.0301 | 0.0370 | ±0.0741 | -0.814 | 0.4159 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.41** (p = **4.05e-38**), Residual SE = **6.188** on **834** df, AIC = **5518.9**, BIC = **5590.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5964** | 2.0259 | ±4.0518 | **+24.481** | **2.34e-132** | *** |
| Education: graduate level (vs college) | +0.0646 | 0.4830 | ±0.9659 | +0.134 | 0.8936 |  |
| Education: high school or below (vs college) | +0.3209 | 0.6337 | ±1.2673 | +0.506 | 0.6126 |  |
| **Site: UCSD (vs UAB)** | **+3.4600** | 0.5212 | ±1.0424 | **+6.638** | **3.17e-11** | *** |
| Site: UW (vs UAB) | -0.4119 | 0.5232 | ±1.0463 | -0.787 | 0.4311 |  |
| **Season: spring (vs autumn)** | **-2.0498** | 0.6037 | ±1.2073 | **-3.396** | **6.85e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3629** | 0.5801 | ±1.1601 | **+2.350** | **0.0188** | * |
| **Season: winter (vs autumn)** | **-5.9838** | 0.6741 | ±1.3481 | **-8.877** | **6.85e-19** | *** |
| **Age (years)** | **-0.0462** | 0.0214 | ±0.0428 | **-2.160** | **0.0308** | * |
| BMI (kg/m2) | -0.0273 | 0.0338 | ±0.0675 | -0.808 | 0.4191 |  |
| Hypertension | -0.2561 | 0.4898 | ±0.9796 | -0.523 | 0.6010 |  |
| **High cholesterol** | **-0.9433** | 0.4674 | ±0.9349 | **-2.018** | **0.0436** | * |
| **Kidney disease** | **+1.3284** | 0.5548 | ±1.1096 | **+2.394** | **0.0166** | * |
| Circulatory disease | -0.1323 | 0.5401 | ±1.0801 | -0.245 | 0.8065 |  |
| Mean / SD ratio | +0.0790 | 0.1623 | ±0.3246 | +0.487 | 0.6263 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **849**, R² = **0.2260**, Adj R² = **0.2130**, F-statistic = **17.39** (p = **4.42e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.1**, BIC = **5590.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8849** | 2.0340 | ±4.0681 | **+24.525** | **7.99e-133** | *** |
| Education: graduate level (vs college) | +0.0728 | 0.4837 | ±0.9674 | +0.150 | 0.8804 |  |
| Education: high school or below (vs college) | +0.3048 | 0.6345 | ±1.2690 | +0.480 | 0.6310 |  |
| **Site: UCSD (vs UAB)** | **+3.4691** | 0.5196 | ±1.0391 | **+6.677** | **2.44e-11** | *** |
| Site: UW (vs UAB) | -0.3993 | 0.5224 | ±1.0449 | -0.764 | 0.4447 |  |
| **Season: spring (vs autumn)** | **-2.0516** | 0.6041 | ±1.2081 | **-3.396** | **6.83e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3608** | 0.5805 | ±1.1610 | **+2.344** | **0.0191** | * |
| **Season: winter (vs autumn)** | **-5.9889** | 0.6738 | ±1.3475 | **-8.889** | **6.18e-19** | *** |
| **Age (years)** | **-0.0471** | 0.0215 | ±0.0431 | **-2.186** | **0.0288** | * |
| BMI (kg/m2) | -0.0273 | 0.0339 | ±0.0678 | -0.804 | 0.4212 |  |
| Hypertension | -0.2579 | 0.4898 | ±0.9796 | -0.527 | 0.5985 |  |
| **High cholesterol** | **-0.9394** | 0.4673 | ±0.9347 | **-2.010** | **0.0444** | * |
| **Kidney disease** | **+1.3023** | 0.5526 | ±1.1053 | **+2.357** | **0.0184** | * |
| Circulatory disease | -0.1404 | 0.5402 | ±1.0805 | -0.260 | 0.7950 |  |
| Avg. daily mean/SD | +0.0261 | 0.1351 | ±0.2701 | +0.193 | 0.8468 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **849**, R² = **0.2259**, Adj R² = **0.2129**, F-statistic = **17.39** (p = **4.46e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.1**, BIC = **5590.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.9264** | 2.1905 | ±4.3811 | **+22.792** | **5.53e-115** | *** |
| Education: graduate level (vs college) | +0.0844 | 0.4832 | ±0.9663 | +0.175 | 0.8613 |  |
| Education: high school or below (vs college) | +0.2899 | 0.6351 | ±1.2702 | +0.457 | 0.6480 |  |
| **Site: UCSD (vs UAB)** | **+3.4740** | 0.5228 | ±1.0456 | **+6.645** | **3.03e-11** | *** |
| Site: UW (vs UAB) | -0.3851 | 0.5283 | ±1.0566 | -0.729 | 0.4660 |  |
| **Season: spring (vs autumn)** | **-2.0507** | 0.6041 | ±1.2082 | **-3.395** | **6.87e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3665** | 0.5799 | ±1.1599 | **+2.356** | **0.0185** | * |
| **Season: winter (vs autumn)** | **-5.9895** | 0.6737 | ±1.3473 | **-8.891** | **6.07e-19** | *** |
| **Age (years)** | **-0.0476** | 0.0214 | ±0.0427 | **-2.230** | **0.0258** | * |
| BMI (kg/m2) | -0.0270 | 0.0337 | ±0.0674 | -0.801 | 0.4231 |  |
| Hypertension | -0.2582 | 0.4905 | ±0.9810 | -0.526 | 0.5986 |  |
| **High cholesterol** | **-0.9355** | 0.4672 | ±0.9345 | **-2.002** | **0.0453** | * |
| **Kidney disease** | **+1.2815** | 0.5528 | ±1.1055 | **+2.318** | **0.0204** | * |
| Circulatory disease | -0.1405 | 0.5408 | ±1.0817 | -0.260 | 0.7951 |  |
| MAG (mg/dL/h) | +0.0029 | 0.0213 | ±0.0426 | +0.135 | 0.8928 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.41** (p = **4.06e-38**), Residual SE = **6.188** on **834** df, AIC = **5518.9**, BIC = **5590.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3560** | 2.0683 | ±4.1366 | **+24.347** | **6.29e-131** | *** |
| Education: graduate level (vs college) | +0.0588 | 0.4833 | ±0.9666 | +0.122 | 0.9031 |  |
| Education: high school or below (vs college) | +0.3255 | 0.6361 | ±1.2722 | +0.512 | 0.6088 |  |
| **Site: UCSD (vs UAB)** | **+3.4518** | 0.5259 | ±1.0519 | **+6.563** | **5.27e-11** | *** |
| Site: UW (vs UAB) | -0.4088 | 0.5239 | ±1.0478 | -0.780 | 0.4352 |  |
| **Season: spring (vs autumn)** | **-2.0443** | 0.6031 | ±1.2061 | **-3.390** | **6.99e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3556** | 0.5803 | ±1.1606 | **+2.336** | **0.0195** | * |
| **Season: winter (vs autumn)** | **-5.9801** | 0.6747 | ±1.3493 | **-8.864** | **7.73e-19** | *** |
| **Age (years)** | **-0.0467** | 0.0215 | ±0.0430 | **-2.174** | **0.0297** | * |
| BMI (kg/m2) | -0.0276 | 0.0336 | ±0.0673 | -0.821 | 0.4119 |  |
| Hypertension | -0.2666 | 0.4916 | ±0.9832 | -0.542 | 0.5876 |  |
| **High cholesterol** | **-0.9427** | 0.4674 | ±0.9348 | **-2.017** | **0.0437** | * |
| **Kidney disease** | **+1.3370** | 0.5551 | ±1.1102 | **+2.409** | **0.0160** | * |
| Circulatory disease | -0.1365 | 0.5400 | ±1.0800 | -0.253 | 0.8005 |  |
| Avg. daily range (mg/dL) | -0.0024 | 0.0050 | ±0.0099 | -0.480 | 0.6315 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **849**, R² = **0.2265**, Adj R² = **0.2135**, F-statistic = **17.44** (p = **3.39e-38**), Residual SE = **6.186** on **834** df, AIC = **5518.6**, BIC = **5589.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2515** | 1.9639 | ±3.9277 | **+25.588** | **2.07e-144** | *** |
| Education: graduate level (vs college) | +0.0406 | 0.4820 | ±0.9639 | +0.084 | 0.9328 |  |
| Education: high school or below (vs college) | +0.3214 | 0.6352 | ±1.2703 | +0.506 | 0.6128 |  |
| **Site: UCSD (vs UAB)** | **+3.4475** | 0.5225 | ±1.0449 | **+6.599** | **4.15e-11** | *** |
| Site: UW (vs UAB) | -0.4218 | 0.5211 | ±1.0422 | -0.809 | 0.4183 |  |
| **Season: spring (vs autumn)** | **-2.0518** | 0.6032 | ±1.2063 | **-3.402** | **6.69e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3632** | 0.5795 | ±1.1591 | **+2.352** | **0.0187** | * |
| **Season: winter (vs autumn)** | **-5.9684** | 0.6763 | ±1.3527 | **-8.825** | **1.10e-18** | *** |
| **Age (years)** | **-0.0475** | 0.0214 | ±0.0427 | **-2.223** | **0.0262** | * |
| BMI (kg/m2) | -0.0255 | 0.0337 | ±0.0674 | -0.757 | 0.4488 |  |
| Hypertension | -0.2538 | 0.4899 | ±0.9799 | -0.518 | 0.6045 |  |
| **High cholesterol** | **-0.9440** | 0.4673 | ±0.9347 | **-2.020** | **0.0434** | * |
| **Kidney disease** | **+1.3383** | 0.5523 | ±1.1047 | **+2.423** | **0.0154** | * |
| Circulatory disease | -0.1113 | 0.5431 | ±1.0863 | -0.205 | 0.8376 |  |
| SD of daily means (mg/dL) | -0.0205 | 0.0268 | ±0.0535 | -0.767 | 0.4432 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **849**, R² = **0.2263**, Adj R² = **0.2133**, F-statistic = **17.43** (p = **3.65e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.7**, BIC = **5589.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5600** | 2.1212 | ±4.2424 | **+23.364** | **9.91e-121** | *** |
| Education: graduate level (vs college) | +0.0543 | 0.4795 | ±0.9590 | +0.113 | 0.9098 |  |
| Education: high school or below (vs college) | +0.3352 | 0.6388 | ±1.2775 | +0.525 | 0.5997 |  |
| **Site: UCSD (vs UAB)** | **+3.4372** | 0.5275 | ±1.0550 | **+6.516** | **7.22e-11** | *** |
| Site: UW (vs UAB) | -0.4078 | 0.5204 | ±1.0408 | -0.784 | 0.4333 |  |
| **Season: spring (vs autumn)** | **-2.0459** | 0.6028 | ±1.2056 | **-3.394** | **6.89e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3517** | 0.5805 | ±1.1610 | **+2.328** | **0.0199** | * |
| **Season: winter (vs autumn)** | **-5.9713** | 0.6759 | ±1.3519 | **-8.834** | **1.01e-18** | *** |
| **Age (years)** | **-0.0466** | 0.0215 | ±0.0430 | **-2.166** | **0.0303** | * |
| BMI (kg/m2) | -0.0261 | 0.0338 | ±0.0675 | -0.774 | 0.4390 |  |
| Hypertension | -0.2717 | 0.4911 | ±0.9822 | -0.553 | 0.5800 |  |
| **High cholesterol** | **-0.9492** | 0.4676 | ±0.9352 | **-2.030** | **0.0424** | * |
| **Kidney disease** | **+1.3265** | 0.5554 | ±1.1108 | **+2.388** | **0.0169** | * |
| Circulatory disease | -0.1335 | 0.5404 | ±1.0807 | -0.247 | 0.8049 |  |
| Time in range 70-180, pooled (%) | +0.0056 | 0.0089 | ±0.0179 | +0.628 | 0.5297 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **849**, R² = **0.2263**, Adj R² = **0.2133**, F-statistic = **17.42** (p = **3.70e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.7**, BIC = **5589.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5730** | 2.1258 | ±4.2516 | **+23.320** | **2.79e-120** | *** |
| Education: graduate level (vs college) | +0.0559 | 0.4796 | ±0.9592 | +0.117 | 0.9072 |  |
| Education: high school or below (vs college) | +0.3351 | 0.6388 | ±1.2776 | +0.525 | 0.5999 |  |
| **Site: UCSD (vs UAB)** | **+3.4373** | 0.5280 | ±1.0560 | **+6.510** | **7.53e-11** | *** |
| Site: UW (vs UAB) | -0.4073 | 0.5204 | ±1.0409 | -0.783 | 0.4339 |  |
| **Season: spring (vs autumn)** | **-2.0451** | 0.6028 | ±1.2056 | **-3.393** | **6.92e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3537** | 0.5804 | ±1.1608 | **+2.332** | **0.0197** | * |
| **Season: winter (vs autumn)** | **-5.9699** | 0.6763 | ±1.3527 | **-8.827** | **1.08e-18** | *** |
| **Age (years)** | **-0.0466** | 0.0215 | ±0.0431 | **-2.165** | **0.0304** | * |
| BMI (kg/m2) | -0.0261 | 0.0338 | ±0.0675 | -0.774 | 0.4390 |  |
| Hypertension | -0.2716 | 0.4912 | ±0.9823 | -0.553 | 0.5803 |  |
| **High cholesterol** | **-0.9484** | 0.4675 | ±0.9350 | **-2.029** | **0.0425** | * |
| **Kidney disease** | **+1.3265** | 0.5553 | ±1.1106 | **+2.389** | **0.0169** | * |
| Circulatory disease | -0.1337 | 0.5404 | ±1.0807 | -0.247 | 0.8046 |  |
| Avg. daily time in range 70-180 (%) | +0.0054 | 0.0089 | ±0.0178 | +0.606 | 0.5442 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.2260**, Adj R² = **0.2130**, F-statistic = **17.39** (p = **4.39e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.1**, BIC = **5590.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1044** | 1.9571 | ±3.9142 | **+25.601** | **1.47e-144** | *** |
| Education: graduate level (vs college) | +0.0794 | 0.4784 | ±0.9567 | +0.166 | 0.8682 |  |
| Education: high school or below (vs college) | +0.2887 | 0.6352 | ±1.2703 | +0.454 | 0.6495 |  |
| **Site: UCSD (vs UAB)** | **+3.4620** | 0.5201 | ±1.0402 | **+6.657** | **2.80e-11** | *** |
| Site: UW (vs UAB) | -0.4034 | 0.5162 | ±1.0325 | -0.781 | 0.4346 |  |
| **Season: spring (vs autumn)** | **-2.0513** | 0.6042 | ±1.2084 | **-3.395** | **6.86e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3594** | 0.5804 | ±1.1608 | **+2.342** | **0.0192** | * |
| **Season: winter (vs autumn)** | **-5.9970** | 0.6766 | ±1.3532 | **-8.864** | **7.75e-19** | *** |
| **Age (years)** | **-0.0481** | 0.0214 | ±0.0428 | **-2.248** | **0.0246** | * |
| BMI (kg/m2) | -0.0266 | 0.0336 | ±0.0671 | -0.791 | 0.4288 |  |
| Hypertension | -0.2535 | 0.4931 | ±0.9862 | -0.514 | 0.6072 |  |
| **High cholesterol** | **-0.9422** | 0.4676 | ±0.9353 | **-2.015** | **0.0439** | * |
| **Kidney disease** | **+1.2866** | 0.5523 | ±1.1045 | **+2.330** | **0.0198** | * |
| Circulatory disease | -0.1341 | 0.5420 | ±1.0839 | -0.247 | 0.8046 |  |
| Any reading < 54 during wear (0/1) | -0.1076 | 0.5046 | ±1.0093 | -0.213 | 0.8312 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.2262**, Adj R² = **0.2132**, F-statistic = **17.41** (p = **3.91e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.9**, BIC = **5590.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1021** | 1.9484 | ±3.8969 | **+25.714** | **8.18e-146** | *** |
| Education: graduate level (vs college) | +0.0717 | 0.4784 | ±0.9568 | +0.150 | 0.8809 |  |
| Education: high school or below (vs college) | +0.2764 | 0.6339 | ±1.2678 | +0.436 | 0.6628 |  |
| **Site: UCSD (vs UAB)** | **+3.4419** | 0.5214 | ±1.0428 | **+6.601** | **4.08e-11** | *** |
| Site: UW (vs UAB) | -0.4264 | 0.5195 | ±1.0390 | -0.821 | 0.4118 |  |
| **Season: spring (vs autumn)** | **-2.0610** | 0.6047 | ±1.2095 | **-3.408** | **6.54e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3564** | 0.5827 | ±1.1655 | **+2.328** | **0.0199** | * |
| **Season: winter (vs autumn)** | **-6.0002** | 0.6760 | ±1.3521 | **-8.876** | **6.95e-19** | *** |
| **Age (years)** | **-0.0478** | 0.0213 | ±0.0427 | **-2.240** | **0.0251** | * |
| BMI (kg/m2) | -0.0263 | 0.0338 | ±0.0675 | -0.780 | 0.4356 |  |
| Hypertension | -0.2529 | 0.4903 | ±0.9807 | -0.516 | 0.6060 |  |
| **High cholesterol** | **-0.9414** | 0.4679 | ±0.9357 | **-2.012** | **0.0442** | * |
| **Kidney disease** | **+1.2818** | 0.5516 | ±1.1031 | **+2.324** | **0.0201** | * |
| Circulatory disease | -0.1203 | 0.5394 | ±1.0787 | -0.223 | 0.8235 |  |
| Time < 54 (%) | -0.2766 | 0.7618 | ±1.5236 | -0.363 | 0.7166 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.2265**, Adj R² = **0.2135**, F-statistic = **17.44** (p = **3.39e-38**), Residual SE = **6.186** on **834** df, AIC = **5518.6**, BIC = **5589.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0923** | 1.9382 | ±3.8763 | **+25.845** | **2.75e-147** | *** |
| Education: graduate level (vs college) | +0.0647 | 0.4785 | ±0.9570 | +0.135 | 0.8924 |  |
| Education: high school or below (vs college) | +0.2738 | 0.6338 | ±1.2675 | +0.432 | 0.6657 |  |
| **Site: UCSD (vs UAB)** | **+3.4379** | 0.5192 | ±1.0384 | **+6.622** | **3.55e-11** | *** |
| Site: UW (vs UAB) | -0.4304 | 0.5188 | ±1.0376 | -0.830 | 0.4068 |  |
| **Season: spring (vs autumn)** | **-2.0735** | 0.6050 | ±1.2100 | **-3.427** | **6.09e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3535** | 0.5830 | ±1.1661 | **+2.321** | **0.0203** | * |
| **Season: winter (vs autumn)** | **-6.0018** | 0.6754 | ±1.3507 | **-8.887** | **6.30e-19** | *** |
| **Age (years)** | **-0.0474** | 0.0214 | ±0.0427 | **-2.219** | **0.0265** | * |
| BMI (kg/m2) | -0.0265 | 0.0337 | ±0.0673 | -0.787 | 0.4313 |  |
| Hypertension | -0.2533 | 0.4902 | ±0.9803 | -0.517 | 0.6054 |  |
| **High cholesterol** | **-0.9485** | 0.4680 | ±0.9360 | **-2.027** | **0.0427** | * |
| **Kidney disease** | **+1.2846** | 0.5522 | ±1.1044 | **+2.326** | **0.0200** | * |
| Circulatory disease | -0.1153 | 0.5392 | ±1.0784 | -0.214 | 0.8308 |  |
| Avg. daily time < 54 (%) | -0.3747 | 0.6872 | ±1.3743 | -0.545 | 0.5855 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.2260**, Adj R² = **0.2130**, F-statistic = **17.40** (p = **4.31e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.1**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0724** | 1.9439 | ±3.8879 | **+25.758** | **2.60e-146** | *** |
| Education: graduate level (vs college) | +0.0723 | 0.4786 | ±0.9572 | +0.151 | 0.8799 |  |
| Education: high school or below (vs college) | +0.2949 | 0.6348 | ±1.2697 | +0.465 | 0.6422 |  |
| **Site: UCSD (vs UAB)** | **+3.4590** | 0.5215 | ±1.0430 | **+6.633** | **3.30e-11** | *** |
| Site: UW (vs UAB) | -0.4047 | 0.5166 | ±1.0331 | -0.784 | 0.4333 |  |
| **Season: spring (vs autumn)** | **-2.0603** | 0.6044 | ±1.2088 | **-3.409** | **6.53e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3558** | 0.5816 | ±1.1631 | **+2.331** | **0.0197** | * |
| **Season: winter (vs autumn)** | **-5.9987** | 0.6774 | ±1.3549 | **-8.855** | **8.35e-19** | *** |
| **Age (years)** | **-0.0474** | 0.0214 | ±0.0428 | **-2.217** | **0.0267** | * |
| BMI (kg/m2) | -0.0268 | 0.0337 | ±0.0675 | -0.794 | 0.4274 |  |
| Hypertension | -0.2577 | 0.4909 | ±0.9818 | -0.525 | 0.5996 |  |
| **High cholesterol** | **-0.9382** | 0.4677 | ±0.9354 | **-2.006** | **0.0449** | * |
| **Kidney disease** | **+1.2893** | 0.5524 | ±1.1048 | **+2.334** | **0.0196** | * |
| Circulatory disease | -0.1356 | 0.5402 | ±1.0804 | -0.251 | 0.8018 |  |
| Time 54-69, pooled (%) | -0.0425 | 0.1797 | ±0.3594 | -0.237 | 0.8128 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **849**, R² = **0.2262**, Adj R² = **0.2132**, F-statistic = **17.41** (p = **3.95e-38**), Residual SE = **6.188** on **834** df, AIC = **5518.9**, BIC = **5590.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0688** | 1.9400 | ±3.8801 | **+25.808** | **7.20e-147** | *** |
| Education: graduate level (vs college) | +0.0664 | 0.4788 | ±0.9577 | +0.139 | 0.8898 |  |
| Education: high school or below (vs college) | +0.2966 | 0.6350 | ±1.2700 | +0.467 | 0.6404 |  |
| **Site: UCSD (vs UAB)** | **+3.4521** | 0.5211 | ±1.0423 | **+6.624** | **3.49e-11** | *** |
| Site: UW (vs UAB) | -0.4128 | 0.5170 | ±1.0340 | -0.798 | 0.4246 |  |
| **Season: spring (vs autumn)** | **-2.0669** | 0.6043 | ±1.2087 | **-3.420** | **6.26e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3523** | 0.5812 | ±1.1625 | **+2.327** | **0.0200** | * |
| **Season: winter (vs autumn)** | **-6.0041** | 0.6772 | ±1.3545 | **-8.866** | **7.60e-19** | *** |
| **Age (years)** | **-0.0471** | 0.0214 | ±0.0428 | **-2.199** | **0.0279** | * |
| BMI (kg/m2) | -0.0266 | 0.0337 | ±0.0674 | -0.789 | 0.4298 |  |
| Hypertension | -0.2565 | 0.4907 | ±0.9814 | -0.523 | 0.6012 |  |
| **High cholesterol** | **-0.9400** | 0.4677 | ±0.9353 | **-2.010** | **0.0444** | * |
| **Kidney disease** | **+1.2881** | 0.5520 | ±1.1040 | **+2.333** | **0.0196** | * |
| Circulatory disease | -0.1336 | 0.5401 | ±1.0802 | -0.247 | 0.8046 |  |
| Avg. daily time 54-69 (%) | -0.0731 | 0.1709 | ±0.3418 | -0.428 | 0.6690 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.40** (p = **4.21e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.0**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0800** | 1.9449 | ±3.8897 | **+25.750** | **3.23e-146** | *** |
| Education: graduate level (vs college) | +0.0709 | 0.4786 | ±0.9571 | +0.148 | 0.8823 |  |
| Education: high school or below (vs college) | +0.2919 | 0.6341 | ±1.2682 | +0.460 | 0.6452 |  |
| **Site: UCSD (vs UAB)** | **+3.4540** | 0.5217 | ±1.0434 | **+6.621** | **3.57e-11** | *** |
| Site: UW (vs UAB) | -0.4105 | 0.5166 | ±1.0332 | -0.795 | 0.4268 |  |
| **Season: spring (vs autumn)** | **-2.0624** | 0.6046 | ±1.2091 | **-3.411** | **6.46e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3546** | 0.5814 | ±1.1628 | **+2.330** | **0.0198** | * |
| **Season: winter (vs autumn)** | **-6.0008** | 0.6775 | ±1.3549 | **-8.858** | **8.16e-19** | *** |
| **Age (years)** | **-0.0474** | 0.0214 | ±0.0428 | **-2.219** | **0.0265** | * |
| BMI (kg/m2) | -0.0267 | 0.0337 | ±0.0675 | -0.790 | 0.4293 |  |
| Hypertension | -0.2566 | 0.4909 | ±0.9817 | -0.523 | 0.6011 |  |
| **High cholesterol** | **-0.9390** | 0.4677 | ±0.9353 | **-2.008** | **0.0447** | * |
| **Kidney disease** | **+1.2881** | 0.5522 | ±1.1043 | **+2.333** | **0.0197** | * |
| Circulatory disease | -0.1321 | 0.5399 | ±1.0798 | -0.245 | 0.8067 |  |
| Time < 70 (%) | -0.0442 | 0.1477 | ±0.2953 | -0.300 | 0.7645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **849**, R² = **0.2263**, Adj R² = **0.2133**, F-statistic = **17.42** (p = **3.76e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.8**, BIC = **5589.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0750** | 1.9393 | ±3.8787 | **+25.821** | **5.22e-147** | *** |
| Education: graduate level (vs college) | +0.0640 | 0.4788 | ±0.9575 | +0.134 | 0.8937 |  |
| Education: high school or below (vs college) | +0.2925 | 0.6342 | ±1.2685 | +0.461 | 0.6446 |  |
| **Site: UCSD (vs UAB)** | **+3.4464** | 0.5209 | ±1.0418 | **+6.616** | **3.68e-11** | *** |
| Site: UW (vs UAB) | -0.4193 | 0.5171 | ±1.0342 | -0.811 | 0.4174 |  |
| **Season: spring (vs autumn)** | **-2.0708** | 0.6045 | ±1.2090 | **-3.426** | **6.13e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3509** | 0.5813 | ±1.1626 | **+2.324** | **0.0201** | * |
| **Season: winter (vs autumn)** | **-6.0061** | 0.6772 | ±1.3543 | **-8.869** | **7.35e-19** | *** |
| **Age (years)** | **-0.0470** | 0.0214 | ±0.0428 | **-2.198** | **0.0279** | * |
| BMI (kg/m2) | -0.0265 | 0.0337 | ±0.0674 | -0.787 | 0.4310 |  |
| Hypertension | -0.2554 | 0.4906 | ±0.9812 | -0.521 | 0.6026 |  |
| **High cholesterol** | **-0.9422** | 0.4676 | ±0.9353 | **-2.015** | **0.0439** | * |
| **Kidney disease** | **+1.2873** | 0.5519 | ±1.1039 | **+2.332** | **0.0197** | * |
| Circulatory disease | -0.1289 | 0.5397 | ±1.0794 | -0.239 | 0.8112 |  |
| Avg. daily time < 70 (%) | -0.0712 | 0.1380 | ±0.2760 | -0.516 | 0.6060 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.40** (p = **4.17e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.0**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5532** | 2.4328 | ±4.8656 | **+20.369** | **3.16e-92** | *** |
| Education: graduate level (vs college) | +0.0618 | 0.4787 | ±0.9574 | +0.129 | 0.8972 |  |
| Education: high school or below (vs college) | +0.3164 | 0.6394 | ±1.2787 | +0.495 | 0.6207 |  |
| **Site: UCSD (vs UAB)** | **+3.4550** | 0.5242 | ±1.0483 | **+6.592** | **4.35e-11** | *** |
| Site: UW (vs UAB) | -0.4093 | 0.5232 | ±1.0464 | -0.782 | 0.4340 |  |
| **Season: spring (vs autumn)** | **-2.0535** | 0.6043 | ±1.2086 | **-3.398** | **6.79e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3447** | 0.5809 | ±1.1617 | **+2.315** | **0.0206** | * |
| **Season: winter (vs autumn)** | **-5.9869** | 0.6743 | ±1.3487 | **-8.878** | **6.79e-19** | *** |
| **Age (years)** | **-0.0479** | 0.0214 | ±0.0427 | **-2.240** | **0.0251** | * |
| BMI (kg/m2) | -0.0266 | 0.0338 | ±0.0677 | -0.787 | 0.4312 |  |
| Hypertension | -0.2574 | 0.4898 | ±0.9795 | -0.526 | 0.5992 |  |
| **High cholesterol** | **-0.9413** | 0.4675 | ±0.9349 | **-2.014** | **0.0440** | * |
| **Kidney disease** | **+1.3055** | 0.5543 | ±1.1086 | **+2.355** | **0.0185** | * |
| Circulatory disease | -0.1372 | 0.5404 | ±1.0808 | -0.254 | 0.7996 |  |
| Time 54-250, pooled (%) | +0.0056 | 0.0145 | ±0.0291 | +0.383 | 0.7018 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.40** (p = **4.17e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.0**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5421** | 2.4742 | ±4.9485 | **+20.023** | **3.46e-89** | *** |
| Education: graduate level (vs college) | +0.0620 | 0.4788 | ±0.9575 | +0.130 | 0.8969 |  |
| Education: high school or below (vs college) | +0.3163 | 0.6396 | ±1.2792 | +0.495 | 0.6209 |  |
| **Site: UCSD (vs UAB)** | **+3.4548** | 0.5243 | ±1.0486 | **+6.590** | **4.41e-11** | *** |
| Site: UW (vs UAB) | -0.4087 | 0.5231 | ±1.0461 | -0.781 | 0.4347 |  |
| **Season: spring (vs autumn)** | **-2.0526** | 0.6042 | ±1.2084 | **-3.397** | **6.81e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3459** | 0.5805 | ±1.1610 | **+2.318** | **0.0204** | * |
| **Season: winter (vs autumn)** | **-5.9859** | 0.6745 | ±1.3491 | **-8.874** | **7.06e-19** | *** |
| **Age (years)** | **-0.0478** | 0.0214 | ±0.0427 | **-2.236** | **0.0254** | * |
| BMI (kg/m2) | -0.0266 | 0.0338 | ±0.0677 | -0.786 | 0.4316 |  |
| Hypertension | -0.2578 | 0.4898 | ±0.9796 | -0.526 | 0.5986 |  |
| **High cholesterol** | **-0.9413** | 0.4674 | ±0.9348 | **-2.014** | **0.0440** | * |
| **Kidney disease** | **+1.3066** | 0.5545 | ±1.1091 | **+2.356** | **0.0185** | * |
| Circulatory disease | -0.1366 | 0.5404 | ±1.0807 | -0.253 | 0.8005 |  |
| Avg. daily time 54-250 (%) | +0.0056 | 0.0149 | ±0.0299 | +0.376 | 0.7069 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.2263**, Adj R² = **0.2133**, F-statistic = **17.43** (p = **3.66e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.7**, BIC = **5589.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0743** | 1.9428 | ±3.8856 | **+25.775** | **1.71e-146** | *** |
| Education: graduate level (vs college) | +0.0684 | 0.4789 | ±0.9579 | +0.143 | 0.8864 |  |
| Education: high school or below (vs college) | +0.3254 | 0.6354 | ±1.2708 | +0.512 | 0.6086 |  |
| **Site: UCSD (vs UAB)** | **+3.4442** | 0.5247 | ±1.0493 | **+6.565** | **5.22e-11** | *** |
| Site: UW (vs UAB) | -0.3880 | 0.5177 | ±1.0355 | -0.749 | 0.4536 |  |
| **Season: spring (vs autumn)** | **-2.0362** | 0.6019 | ±1.2038 | **-3.383** | **7.17e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3754** | 0.5802 | ±1.1605 | **+2.370** | **0.0178** | * |
| **Season: winter (vs autumn)** | **-5.9623** | 0.6767 | ±1.3534 | **-8.811** | **1.24e-18** | *** |
| **Age (years)** | **-0.0457** | 0.0216 | ±0.0432 | **-2.114** | **0.0346** | * |
| BMI (kg/m2) | -0.0262 | 0.0337 | ±0.0673 | -0.779 | 0.4362 |  |
| Hypertension | -0.2832 | 0.4929 | ±0.9859 | -0.575 | 0.5656 |  |
| **High cholesterol** | **-0.9493** | 0.4675 | ±0.9351 | **-2.030** | **0.0423** | * |
| **Kidney disease** | **+1.3227** | 0.5542 | ±1.1083 | **+2.387** | **0.0170** | * |
| Circulatory disease | -0.1358 | 0.5406 | ±1.0812 | -0.251 | 0.8017 |  |
| Time 181-250, pooled (%) | -0.0092 | 0.0144 | ±0.0288 | -0.635 | 0.5255 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **849**, R² = **0.2263**, Adj R² = **0.2133**, F-statistic = **17.42** (p = **3.79e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.8**, BIC = **5590.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0748** | 1.9426 | ±3.8852 | **+25.777** | **1.60e-146** | *** |
| Education: graduate level (vs college) | +0.0702 | 0.4789 | ±0.9579 | +0.147 | 0.8835 |  |
| Education: high school or below (vs college) | +0.3246 | 0.6353 | ±1.2706 | +0.511 | 0.6093 |  |
| **Site: UCSD (vs UAB)** | **+3.4451** | 0.5253 | ±1.0506 | **+6.558** | **5.44e-11** | *** |
| Site: UW (vs UAB) | -0.3898 | 0.5180 | ±1.0359 | -0.753 | 0.4517 |  |
| **Season: spring (vs autumn)** | **-2.0375** | 0.6020 | ±1.2040 | **-3.384** | **7.13e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3743** | 0.5802 | ±1.1604 | **+2.369** | **0.0179** | * |
| **Season: winter (vs autumn)** | **-5.9635** | 0.6770 | ±1.3539 | **-8.809** | **1.26e-18** | *** |
| **Age (years)** | **-0.0460** | 0.0216 | ±0.0432 | **-2.129** | **0.0332** | * |
| BMI (kg/m2) | -0.0263 | 0.0337 | ±0.0673 | -0.780 | 0.4354 |  |
| Hypertension | -0.2806 | 0.4929 | ±0.9859 | -0.569 | 0.5692 |  |
| **High cholesterol** | **-0.9475** | 0.4675 | ±0.9350 | **-2.027** | **0.0427** | * |
| **Kidney disease** | **+1.3201** | 0.5539 | ±1.1079 | **+2.383** | **0.0172** | * |
| Circulatory disease | -0.1369 | 0.5406 | ±1.0812 | -0.253 | 0.8001 |  |
| Avg. daily time 181-250 (%) | -0.0082 | 0.0141 | ±0.0283 | -0.580 | 0.5619 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **849**, R² = **0.2263**, Adj R² = **0.2133**, F-statistic = **17.42** (p = **3.73e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.8**, BIC = **5589.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1156** | 1.9411 | ±3.8822 | **+25.818** | **5.59e-147** | *** |
| Education: graduate level (vs college) | +0.0568 | 0.4794 | ±0.9588 | +0.119 | 0.9057 |  |
| Education: high school or below (vs college) | +0.3331 | 0.6384 | ±1.2768 | +0.522 | 0.6018 |  |
| **Site: UCSD (vs UAB)** | **+3.4412** | 0.5267 | ±1.0534 | **+6.534** | **6.41e-11** | *** |
| Site: UW (vs UAB) | -0.4048 | 0.5202 | ±1.0404 | -0.778 | 0.4364 |  |
| **Season: spring (vs autumn)** | **-2.0448** | 0.6028 | ±1.2055 | **-3.392** | **6.93e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3533** | 0.5805 | ±1.1610 | **+2.331** | **0.0197** | * |
| **Season: winter (vs autumn)** | **-5.9711** | 0.6763 | ±1.3525 | **-8.830** | **1.05e-18** | *** |
| **Age (years)** | **-0.0467** | 0.0215 | ±0.0430 | **-2.171** | **0.0299** | * |
| BMI (kg/m2) | -0.0262 | 0.0338 | ±0.0675 | -0.776 | 0.4375 |  |
| Hypertension | -0.2713 | 0.4913 | ±0.9826 | -0.552 | 0.5808 |  |
| **High cholesterol** | **-0.9482** | 0.4676 | ±0.9352 | **-2.028** | **0.0426** | * |
| **Kidney disease** | **+1.3243** | 0.5552 | ±1.1103 | **+2.385** | **0.0171** | * |
| Circulatory disease | -0.1349 | 0.5405 | ±1.0809 | -0.250 | 0.8028 |  |
| Time > 180 (%) | -0.0053 | 0.0089 | ±0.0177 | -0.595 | 0.5521 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **849**, R² = **0.2262**, Adj R² = **0.2133**, F-statistic = **17.42** (p = **3.81e-38**), Residual SE = **6.187** on **834** df, AIC = **5518.8**, BIC = **5590.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1077** | 1.9409 | ±3.8818 | **+25.817** | **5.75e-147** | *** |
| Education: graduate level (vs college) | +0.0590 | 0.4794 | ±0.9589 | +0.123 | 0.9020 |  |
| Education: high school or below (vs college) | +0.3317 | 0.6384 | ±1.2768 | +0.520 | 0.6034 |  |
| **Site: UCSD (vs UAB)** | **+3.4419** | 0.5272 | ±1.0545 | **+6.528** | **6.66e-11** | *** |
| Site: UW (vs UAB) | -0.4042 | 0.5202 | ±1.0405 | -0.777 | 0.4372 |  |
| **Season: spring (vs autumn)** | **-2.0442** | 0.6027 | ±1.2055 | **-3.391** | **6.95e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3553** | 0.5804 | ±1.1608 | **+2.335** | **0.0195** | * |
| **Season: winter (vs autumn)** | **-5.9705** | 0.6767 | ±1.3534 | **-8.823** | **1.12e-18** | *** |
| **Age (years)** | **-0.0467** | 0.0215 | ±0.0430 | **-2.173** | **0.0298** | * |
| BMI (kg/m2) | -0.0262 | 0.0338 | ±0.0676 | -0.777 | 0.4373 |  |
| Hypertension | -0.2708 | 0.4914 | ±0.9828 | -0.551 | 0.5816 |  |
| **High cholesterol** | **-0.9470** | 0.4675 | ±0.9350 | **-2.026** | **0.0428** | * |
| **Kidney disease** | **+1.3233** | 0.5552 | ±1.1103 | **+2.384** | **0.0171** | * |
| Circulatory disease | -0.1351 | 0.5405 | ±1.0810 | -0.250 | 0.8026 |  |
| Avg. daily time > 180 (%) | -0.0049 | 0.0088 | ±0.0177 | -0.557 | 0.5777 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **849**, R² = **0.2272**, Adj R² = **0.2142**, F-statistic = **17.51** (p = **2.36e-38**), Residual SE = **6.184** on **834** df, AIC = **5517.8**, BIC = **5588.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1451** | 1.9407 | ±3.8813 | **+25.839** | **3.21e-147** | *** |
| Education: graduate level (vs college) | +0.0284 | 0.4800 | ±0.9600 | +0.059 | 0.9529 |  |
| Education: high school or below (vs college) | +0.3609 | 0.6389 | ±1.2778 | +0.565 | 0.5722 |  |
| **Site: UCSD (vs UAB)** | **+3.4109** | 0.5275 | ±1.0549 | **+6.467** | **1.00e-10** | *** |
| Site: UW (vs UAB) | -0.4092 | 0.5193 | ±1.0386 | -0.788 | 0.4307 |  |
| **Season: spring (vs autumn)** | **-2.0364** | 0.6016 | ±1.2032 | **-3.385** | **7.11e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3430** | 0.5801 | ±1.1602 | **+2.315** | **0.0206** | * |
| **Season: winter (vs autumn)** | **-5.9530** | 0.6762 | ±1.3525 | **-8.803** | **1.33e-18** | *** |
| **Age (years)** | **-0.0472** | 0.0214 | ±0.0429 | **-2.202** | **0.0277** | * |
| BMI (kg/m2) | -0.0239 | 0.0339 | ±0.0678 | -0.705 | 0.4806 |  |
| Hypertension | -0.2837 | 0.4912 | ±0.9825 | -0.578 | 0.5636 |  |
| **High cholesterol** | **-0.9590** | 0.4669 | ±0.9338 | **-2.054** | **0.0400** | * |
| **Kidney disease** | **+1.3438** | 0.5544 | ±1.1088 | **+2.424** | **0.0154** | * |
| Circulatory disease | -0.1275 | 0.5397 | ±1.0794 | -0.236 | 0.8133 |  |
| Nocturnal time > 180 (%) | -0.0094 | 0.0084 | ±0.0167 | -1.121 | 0.2623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.2286**, Adj R² = **0.2157**, F-statistic = **17.65** (p = **1.13e-38**), Residual SE = **6.178** on **834** df, AIC = **5516.2**, BIC = **5587.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2821** | 1.9487 | ±3.8974 | **+25.803** | **8.29e-147** | *** |
| Education: graduate level (vs college) | +0.0042 | 0.4810 | ±0.9620 | +0.009 | 0.9930 |  |
| Education: high school or below (vs college) | +0.3353 | 0.6336 | ±1.2673 | +0.529 | 0.5967 |  |
| **Site: UCSD (vs UAB)** | **+3.4279** | 0.5208 | ±1.0416 | **+6.582** | **4.64e-11** | *** |
| Site: UW (vs UAB) | -0.3685 | 0.5165 | ±1.0329 | -0.713 | 0.4756 |  |
| **Season: spring (vs autumn)** | **-2.0605** | 0.6019 | ±1.2038 | **-3.423** | **6.18e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3654** | 0.5795 | ±1.1590 | **+2.356** | **0.0185** | * |
| **Season: winter (vs autumn)** | **-5.9827** | 0.6732 | ±1.3464 | **-8.887** | **6.29e-19** | *** |
| Age (years) | -0.0414 | 0.0216 | ±0.0431 | -1.922 | 0.0547 | . |
| BMI (kg/m2) | -0.0291 | 0.0333 | ±0.0667 | -0.874 | 0.3821 |  |
| Hypertension | -0.2990 | 0.4931 | ±0.9861 | -0.606 | 0.5443 |  |
| **High cholesterol** | **-0.9488** | 0.4655 | ±0.9311 | **-2.038** | **0.0415** | * |
| **Kidney disease** | **+1.3801** | 0.5527 | ±1.1054 | **+2.497** | **0.0125** | * |
| Circulatory disease | -0.1538 | 0.5390 | ±1.0780 | -0.285 | 0.7753 |  |
| Any reading > 250 during wear (0/1) | -0.7738 | 0.4632 | ±0.9264 | -1.670 | 0.0948 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.40** (p = **4.19e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.0**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1069** | 1.9360 | ±3.8721 | **+25.881** | **1.08e-147** | *** |
| Education: graduate level (vs college) | +0.0627 | 0.4787 | ±0.9573 | +0.131 | 0.8959 |  |
| Education: high school or below (vs college) | +0.3159 | 0.6394 | ±1.2788 | +0.494 | 0.6212 |  |
| **Site: UCSD (vs UAB)** | **+3.4562** | 0.5239 | ±1.0478 | **+6.597** | **4.20e-11** | *** |
| Site: UW (vs UAB) | -0.4080 | 0.5230 | ±1.0460 | -0.780 | 0.4353 |  |
| **Season: spring (vs autumn)** | **-2.0531** | 0.6043 | ±1.2086 | **-3.398** | **6.80e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3455** | 0.5809 | ±1.1617 | **+2.316** | **0.0205** | * |
| **Season: winter (vs autumn)** | **-5.9868** | 0.6744 | ±1.3487 | **-8.878** | **6.84e-19** | *** |
| **Age (years)** | **-0.0478** | 0.0214 | ±0.0427 | **-2.239** | **0.0252** | * |
| BMI (kg/m2) | -0.0267 | 0.0338 | ±0.0677 | -0.788 | 0.4308 |  |
| Hypertension | -0.2576 | 0.4898 | ±0.9795 | -0.526 | 0.5989 |  |
| **High cholesterol** | **-0.9410** | 0.4674 | ±0.9349 | **-2.013** | **0.0441** | * |
| **Kidney disease** | **+1.3050** | 0.5542 | ±1.1085 | **+2.355** | **0.0185** | * |
| Circulatory disease | -0.1377 | 0.5405 | ±1.0810 | -0.255 | 0.7988 |  |
| Time > 250 (%) | -0.0053 | 0.0145 | ±0.0291 | -0.367 | 0.7133 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 849)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.2261**, Adj R² = **0.2131**, F-statistic = **17.40** (p = **4.20e-38**), Residual SE = **6.188** on **834** df, AIC = **5519.0**, BIC = **5590.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1007** | 1.9357 | ±3.8715 | **+25.882** | **1.06e-147** | *** |
| Education: graduate level (vs college) | +0.0632 | 0.4787 | ±0.9574 | +0.132 | 0.8950 |  |
| Education: high school or below (vs college) | +0.3154 | 0.6396 | ±1.2792 | +0.493 | 0.6220 |  |
| **Site: UCSD (vs UAB)** | **+3.4562** | 0.5241 | ±1.0482 | **+6.594** | **4.27e-11** | *** |
| Site: UW (vs UAB) | -0.4072 | 0.5229 | ±1.0458 | -0.779 | 0.4361 |  |
| **Season: spring (vs autumn)** | **-2.0521** | 0.6042 | ±1.2083 | **-3.397** | **6.82e-04** | *** |
| **Season: summer (vs autumn)** | **+1.3470** | 0.5805 | ±1.1609 | **+2.321** | **0.0203** | * |
| **Season: winter (vs autumn)** | **-5.9859** | 0.6746 | ±1.3492 | **-8.873** | **7.11e-19** | *** |
| **Age (years)** | **-0.0478** | 0.0214 | ±0.0427 | **-2.236** | **0.0254** | * |
| BMI (kg/m2) | -0.0266 | 0.0338 | ±0.0677 | -0.787 | 0.4312 |  |
| Hypertension | -0.2580 | 0.4898 | ±0.9796 | -0.527 | 0.5984 |  |
| **High cholesterol** | **-0.9409** | 0.4674 | ±0.9348 | **-2.013** | **0.0441** | * |
| **Kidney disease** | **+1.3057** | 0.5545 | ±1.1090 | **+2.355** | **0.0185** | * |
| Circulatory disease | -0.1372 | 0.5405 | ±1.0809 | -0.254 | 0.7997 |  |
| Avg. daily time > 250 (%) | -0.0053 | 0.0149 | ±0.0299 | -0.354 | 0.7231 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 849; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **849**, R² = **0.0712**, Adj R² = **0.0567**, F-statistic = **4.92** (p = **2.22e-08**), Residual SE = **17.168** on **835** df, AIC = **7250.7**, BIC = **7317.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.5407** | 6.4186 | ±12.8371 | **+19.559** | **3.46e-85** | *** |
| **Education: graduate level (vs college)** | **-3.2550** | 1.2468 | ±2.4937 | **-2.611** | **0.0090** | ** |
| **Education: high school or below (vs college)** | **+5.2031** | 1.9923 | ±3.9847 | **+2.612** | **0.0090** | ** |
| **Site: UCSD (vs UAB)** | **+3.1181** | 1.5346 | ±3.0692 | **+2.032** | **0.0422** | * |
| Site: UW (vs UAB) | -1.1792 | 1.4059 | ±2.8117 | -0.839 | 0.4016 |  |
| Season: spring (vs autumn) | +2.5114 | 1.5082 | ±3.0164 | +1.665 | 0.0959 | . |
| Season: summer (vs autumn) | +2.6492 | 1.6239 | ±3.2478 | +1.631 | 0.1028 |  |
| **Season: winter (vs autumn)** | **+6.0552** | 1.9047 | ±3.8095 | **+3.179** | **0.0015** | ** |
| Age (years) | -0.1216 | 0.0672 | ±0.1344 | -1.809 | 0.0704 | . |
| BMI (kg/m2) | +0.1767 | 0.0989 | ±0.1977 | +1.787 | 0.0739 | . |
| Hypertension | +0.6411 | 1.4360 | ±2.8720 | +0.446 | 0.6553 |  |
| High cholesterol | +1.1973 | 1.3271 | ±2.6542 | +0.902 | 0.3669 |  |
| Kidney disease | -2.1222 | 1.5943 | ±3.1887 | -1.331 | 0.1832 |  |
| Circulatory disease | -0.0933 | 1.5859 | ±3.1718 | -0.059 | 0.9531 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **849**, R² = **0.0738**, Adj R² = **0.0582**, F-statistic = **4.74** (p = **1.98e-08**), Residual SE = **17.154** on **834** df, AIC = **7250.3**, BIC = **7321.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.8444** | 7.0824 | ±14.1649 | **+18.333** | **4.49e-75** | *** |
| **Education: graduate level (vs college)** | **-3.4278** | 1.2323 | ±2.4645 | **-2.782** | **0.0054** | ** |
| **Education: high school or below (vs college)** | **+5.4899** | 2.0087 | ±4.0174 | **+2.733** | **0.0063** | ** |
| Site: UCSD (vs UAB) | +2.9965 | 1.5360 | ±3.0721 | +1.951 | 0.0511 | . |
| Site: UW (vs UAB) | -1.2808 | 1.4032 | ±2.8064 | -0.913 | 0.3614 |  |
| Season: spring (vs autumn) | +2.4411 | 1.5095 | ±3.0190 | +1.617 | 0.1058 |  |
| Season: summer (vs autumn) | +2.5514 | 1.6261 | ±3.2522 | +1.569 | 0.1166 |  |
| **Season: winter (vs autumn)** | **+6.1031** | 1.8961 | ±3.7923 | **+3.219** | **0.0013** | ** |
| Age (years) | -0.1178 | 0.0675 | ±0.1350 | -1.746 | 0.0808 | . |
| BMI (kg/m2) | +0.1873 | 0.0986 | ±0.1971 | +1.900 | 0.0574 | . |
| Hypertension | +0.6478 | 1.4367 | ±2.8734 | +0.451 | 0.6520 |  |
| High cholesterol | +1.1952 | 1.3239 | ±2.6478 | +0.903 | 0.3666 |  |
| Kidney disease | -2.0713 | 1.5891 | ±3.1782 | -1.303 | 0.1924 |  |
| Circulatory disease | -0.0595 | 1.5866 | ±3.1732 | -0.038 | 0.9701 |  |
| HbA1c (%) | -0.7117 | 0.5220 | ±1.0441 | -1.363 | 0.1728 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **849**, R² = **0.0724**, Adj R² = **0.0568**, F-statistic = **4.65** (p = **3.28e-08**), Residual SE = **17.167** on **834** df, AIC = **7251.6**, BIC = **7322.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.6598** | 7.0311 | ±14.0623 | **+18.156** | **1.14e-73** | *** |
| **Education: graduate level (vs college)** | **-3.3582** | 1.2329 | ±2.4658 | **-2.724** | **0.0065** | ** |
| **Education: high school or below (vs college)** | **+5.3637** | 2.0033 | ±4.0066 | **+2.677** | **0.0074** | ** |
| Site: UCSD (vs UAB) | +3.0129 | 1.5496 | ±3.0993 | +1.944 | 0.0519 | . |
| Site: UW (vs UAB) | -1.2271 | 1.4059 | ±2.8118 | -0.873 | 0.3828 |  |
| Season: spring (vs autumn) | +2.5449 | 1.5088 | ±3.0175 | +1.687 | 0.0917 | . |
| Season: summer (vs autumn) | +2.6063 | 1.6290 | ±3.2580 | +1.600 | 0.1096 |  |
| **Season: winter (vs autumn)** | **+6.1379** | 1.8818 | ±3.7637 | **+3.262** | **0.0011** | ** |
| Age (years) | -0.1185 | 0.0672 | ±0.1343 | -1.765 | 0.0776 | . |
| BMI (kg/m2) | +0.1795 | 0.0985 | ±0.1969 | +1.824 | 0.0682 | . |
| Hypertension | +0.6143 | 1.4341 | ±2.8683 | +0.428 | 0.6684 |  |
| High cholesterol | +1.1618 | 1.3231 | ±2.6462 | +0.878 | 0.3799 |  |
| Kidney disease | -1.9818 | 1.5952 | ±3.1904 | -1.242 | 0.2141 |  |
| Circulatory disease | -0.0753 | 1.5883 | ±3.1766 | -0.047 | 0.9622 |  |
| Mean glucose (mg/dL) | -0.0153 | 0.0159 | ±0.0318 | -0.958 | 0.3382 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **849**, R² = **0.0724**, Adj R² = **0.0568**, F-statistic = **4.65** (p = **3.28e-08**), Residual SE = **17.167** on **834** df, AIC = **7251.6**, BIC = **7322.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.7704** | 8.1963 | ±16.3926 | **+15.833** | **1.85e-56** | *** |
| **Education: graduate level (vs college)** | **-3.3582** | 1.2329 | ±2.4658 | **-2.724** | **0.0065** | ** |
| **Education: high school or below (vs college)** | **+5.3637** | 2.0033 | ±4.0066 | **+2.677** | **0.0074** | ** |
| Site: UCSD (vs UAB) | +3.0129 | 1.5496 | ±3.0993 | +1.944 | 0.0519 | . |
| Site: UW (vs UAB) | -1.2271 | 1.4059 | ±2.8118 | -0.873 | 0.3828 |  |
| Season: spring (vs autumn) | +2.5449 | 1.5088 | ±3.0175 | +1.687 | 0.0917 | . |
| Season: summer (vs autumn) | +2.6063 | 1.6290 | ±3.2580 | +1.600 | 0.1096 |  |
| **Season: winter (vs autumn)** | **+6.1379** | 1.8818 | ±3.7637 | **+3.262** | **0.0011** | ** |
| Age (years) | -0.1185 | 0.0672 | ±0.1343 | -1.765 | 0.0776 | . |
| BMI (kg/m2) | +0.1795 | 0.0985 | ±0.1969 | +1.824 | 0.0682 | . |
| Hypertension | +0.6143 | 1.4341 | ±2.8683 | +0.428 | 0.6684 |  |
| High cholesterol | +1.1618 | 1.3231 | ±2.6462 | +0.878 | 0.3799 |  |
| Kidney disease | -1.9818 | 1.5952 | ±3.1904 | -1.242 | 0.2141 |  |
| Circulatory disease | -0.0753 | 1.5883 | ±3.1766 | -0.047 | 0.9622 |  |
| GMI (%) | -0.6376 | 0.6657 | ±1.3315 | -0.958 | 0.3382 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **849**, R² = **0.0731**, Adj R² = **0.0575**, F-statistic = **4.69** (p = **2.59e-08**), Residual SE = **17.161** on **834** df, AIC = **7251.0**, BIC = **7322.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.1173** | 7.2043 | ±14.4086 | **+17.783** | **9.49e-71** | *** |
| **Education: graduate level (vs college)** | **-3.3814** | 1.2343 | ±2.4687 | **-2.739** | **0.0062** | ** |
| **Education: high school or below (vs college)** | **+5.3931** | 1.9889 | ±3.9778 | **+2.712** | **0.0067** | ** |
| Site: UCSD (vs UAB) | +2.9942 | 1.5491 | ±3.0983 | +1.933 | 0.0533 | . |
| Site: UW (vs UAB) | -1.1939 | 1.4072 | ±2.8143 | -0.848 | 0.3962 |  |
| Season: spring (vs autumn) | +2.5764 | 1.5076 | ±3.0152 | +1.709 | 0.0875 | . |
| Season: summer (vs autumn) | +2.6039 | 1.6277 | ±3.2555 | +1.600 | 0.1097 |  |
| **Season: winter (vs autumn)** | **+6.1696** | 1.8768 | ±3.7535 | **+3.287** | **0.0010** | ** |
| Age (years) | -0.1218 | 0.0676 | ±0.1351 | -1.803 | 0.0713 | . |
| BMI (kg/m2) | +0.1846 | 0.0980 | ±0.1960 | +1.884 | 0.0595 | . |
| Hypertension | +0.5937 | 1.4319 | ±2.8638 | +0.415 | 0.6784 |  |
| High cholesterol | +1.1666 | 1.3223 | ±2.6446 | +0.882 | 0.3777 |  |
| Kidney disease | -2.0103 | 1.5980 | ±3.1960 | -1.258 | 0.2084 |  |
| Circulatory disease | -0.0729 | 1.5870 | ±3.1739 | -0.046 | 0.9633 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0186 | 0.0177 | ±0.0353 | -1.053 | 0.2922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **849**, R² = **0.0712**, Adj R² = **0.0556**, F-statistic = **4.57** (p = **5.09e-08**), Residual SE = **17.178** on **834** df, AIC = **7252.7**, BIC = **7323.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3967** | 6.4739 | ±12.9477 | **+19.370** | **1.39e-83** | *** |
| **Education: graduate level (vs college)** | **-3.2403** | 1.2385 | ±2.4771 | **-2.616** | **0.0089** | ** |
| **Education: high school or below (vs college)** | **+5.1811** | 2.0078 | ±4.0156 | **+2.581** | **0.0099** | ** |
| **Site: UCSD (vs UAB)** | **+3.1311** | 1.5534 | ±3.1068 | **+2.016** | **0.0438** | * |
| Site: UW (vs UAB) | -1.1661 | 1.4045 | ±2.8090 | -0.830 | 0.4064 |  |
| Season: spring (vs autumn) | +2.5086 | 1.5106 | ±3.0211 | +1.661 | 0.0968 | . |
| Season: summer (vs autumn) | +2.6563 | 1.6267 | ±3.2534 | +1.633 | 0.1025 |  |
| **Season: winter (vs autumn)** | **+6.0476** | 1.9022 | ±3.8044 | **+3.179** | **0.0015** | ** |
| Age (years) | -0.1224 | 0.0680 | ±0.1360 | -1.800 | 0.0719 | . |
| BMI (kg/m2) | +0.1766 | 0.0990 | ±0.1981 | +1.783 | 0.0745 | . |
| Hypertension | +0.6423 | 1.4382 | ±2.8764 | +0.447 | 0.6552 |  |
| High cholesterol | +1.2039 | 1.3210 | ±2.6420 | +0.911 | 0.3621 |  |
| Kidney disease | -2.1577 | 1.5982 | ±3.1963 | -1.350 | 0.1770 |  |
| Circulatory disease | -0.0971 | 1.5879 | ±3.1757 | -0.061 | 0.9512 |  |
| Glucose SD, pooled (mg/dL) | +0.0054 | 0.0496 | ±0.0992 | +0.109 | 0.9130 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **849**, R² = **0.0718**, Adj R² = **0.0562**, F-statistic = **4.61** (p = **4.13e-08**), Residual SE = **17.172** on **834** df, AIC = **7252.2**, BIC = **7323.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.6262** | 6.5361 | ±13.0721 | **+19.068** | **4.70e-81** | *** |
| **Education: graduate level (vs college)** | **-3.1739** | 1.2425 | ±2.4850 | **-2.555** | **0.0106** | * |
| **Education: high school or below (vs college)** | **+5.0620** | 2.0031 | ±4.0062 | **+2.527** | **0.0115** | * |
| **Site: UCSD (vs UAB)** | **+3.1914** | 1.5439 | ±3.0877 | **+2.067** | **0.0387** | * |
| Site: UW (vs UAB) | -1.1107 | 1.4047 | ±2.8094 | -0.791 | 0.4291 |  |
| Season: spring (vs autumn) | +2.4924 | 1.5086 | ±3.0171 | +1.652 | 0.0985 | . |
| Season: summer (vs autumn) | +2.7002 | 1.6264 | ±3.2527 | +1.660 | 0.0969 | . |
| **Season: winter (vs autumn)** | **+6.0201** | 1.9067 | ±3.8133 | **+3.157** | **0.0016** | ** |
| Age (years) | -0.1267 | 0.0675 | ±0.1349 | -1.879 | 0.0603 | . |
| BMI (kg/m2) | +0.1784 | 0.0991 | ±0.1983 | +1.799 | 0.0720 | . |
| Hypertension | +0.6518 | 1.4370 | ±2.8739 | +0.454 | 0.6501 |  |
| High cholesterol | +1.2364 | 1.3247 | ±2.6494 | +0.933 | 0.3507 |  |
| Kidney disease | -2.3385 | 1.5984 | ±3.1969 | -1.463 | 0.1435 |  |
| Circulatory disease | -0.1044 | 1.5867 | ±3.1735 | -0.066 | 0.9475 |  |
| Avg. daily SD (mg/dL) | +0.0367 | 0.0489 | ±0.0977 | +0.751 | 0.4527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **849**, R² = **0.0733**, Adj R² = **0.0577**, F-statistic = **4.71** (p = **2.40e-08**), Residual SE = **17.159** on **834** df, AIC = **7250.8**, BIC = **7322.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.9435** | 6.3035 | ±12.6069 | **+19.504** | **1.01e-84** | *** |
| **Education: graduate level (vs college)** | **-3.1356** | 1.2499 | ±2.4998 | **-2.509** | **0.0121** | * |
| **Education: high school or below (vs college)** | **+5.0138** | 2.0041 | ±4.0082 | **+2.502** | **0.0124** | * |
| **Site: UCSD (vs UAB)** | **+3.2279** | 1.5416 | ±3.0832 | **+2.094** | **0.0363** | * |
| Site: UW (vs UAB) | -1.0122 | 1.4021 | ±2.8041 | -0.722 | 0.4703 |  |
| Season: spring (vs autumn) | +2.5249 | 1.5079 | ±3.0158 | +1.674 | 0.0940 | . |
| Season: summer (vs autumn) | +2.6985 | 1.6200 | ±3.2401 | +1.666 | 0.0958 | . |
| **Season: winter (vs autumn)** | **+6.0336** | 1.9110 | ±3.8219 | **+3.157** | **0.0016** | ** |
| Age (years) | -0.1326 | 0.0693 | ±0.1386 | -1.913 | 0.0558 | . |
| BMI (kg/m2) | +0.1796 | 0.0989 | ±0.1977 | +1.817 | 0.0693 | . |
| Hypertension | +0.6133 | 1.4335 | ±2.8670 | +0.428 | 0.6688 |  |
| High cholesterol | +1.2635 | 1.3258 | ±2.6516 | +0.953 | 0.3406 |  |
| Kidney disease | -2.5247 | 1.5931 | ±3.1861 | -1.585 | 0.1130 |  |
| Circulatory disease | -0.1399 | 1.5853 | ±3.1706 | -0.088 | 0.9297 |  |
| CV (%) | +0.1412 | 0.1028 | ±0.2056 | +1.374 | 0.1694 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **849**, R² = **0.0743**, Adj R² = **0.0587**, F-statistic = **4.78** (p = **1.64e-08**), Residual SE = **17.149** on **834** df, AIC = **7249.9**, BIC = **7321.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.0910** | 7.4121 | ±14.8242 | **+17.551** | **5.83e-69** | *** |
| **Education: graduate level (vs college)** | **-3.1135** | 1.2480 | ±2.4960 | **-2.495** | **0.0126** | * |
| **Education: high school or below (vs college)** | **+4.9490** | 2.0056 | ±4.0111 | **+2.468** | **0.0136** | * |
| **Site: UCSD (vs UAB)** | **+3.2216** | 1.5375 | ±3.0749 | **+2.095** | **0.0361** | * |
| Site: UW (vs UAB) | -0.9950 | 1.4024 | ±2.8048 | -0.709 | 0.4780 |  |
| Season: spring (vs autumn) | +2.5039 | 1.5080 | ±3.0159 | +1.660 | 0.0968 | . |
| Season: summer (vs autumn) | +2.6430 | 1.6234 | ±3.2468 | +1.628 | 0.1035 |  |
| **Season: winter (vs autumn)** | **+5.9981** | 1.9115 | ±3.8230 | **+3.138** | **0.0017** | ** |
| **Age (years)** | **-0.1361** | 0.0694 | ±0.1388 | **-1.962** | **0.0498** | * |
| BMI (kg/m2) | +0.1798 | 0.0988 | ±0.1977 | +1.819 | 0.0689 | . |
| Hypertension | +0.6081 | 1.4333 | ±2.8666 | +0.424 | 0.6714 |  |
| High cholesterol | +1.2612 | 1.3255 | ±2.6509 | +0.952 | 0.3413 |  |
| Kidney disease | -2.5120 | 1.5979 | ±3.1958 | -1.572 | 0.1159 |  |
| Circulatory disease | -0.1763 | 1.5863 | ±3.1725 | -0.111 | 0.9115 |  |
| Mean / SD ratio | -0.7787 | 0.4434 | ±0.8867 | -1.756 | 0.0790 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **849**, R² = **0.0769**, Adj R² = **0.0614**, F-statistic = **4.96** (p = **6.11e-09**), Residual SE = **17.125** on **834** df, AIC = **7247.5**, BIC = **7318.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+131.4044** | 7.1142 | ±14.2284 | **+18.471** | **3.55e-76** | *** |
| **Education: graduate level (vs college)** | **-3.0466** | 1.2526 | ±2.5052 | **-2.432** | **0.0150** | * |
| **Education: high school or below (vs college)** | **+4.8757** | 1.9959 | ±3.9919 | **+2.443** | **0.0146** | * |
| **Site: UCSD (vs UAB)** | **+3.1675** | 1.5306 | ±3.0612 | **+2.069** | **0.0385** | * |
| Site: UW (vs UAB) | -0.9734 | 1.4038 | ±2.8077 | -0.693 | 0.4881 |  |
| Season: spring (vs autumn) | +2.5444 | 1.5066 | ±3.0131 | +1.689 | 0.0912 | . |
| Season: summer (vs autumn) | +2.6998 | 1.6195 | ±3.2389 | +1.667 | 0.0955 | . |
| **Season: winter (vs autumn)** | **+6.0340** | 1.9078 | ±3.8156 | **+3.163** | **0.0016** | ** |
| **Age (years)** | **-0.1428** | 0.0689 | ±0.1378 | **-2.072** | **0.0382** | * |
| BMI (kg/m2) | +0.1874 | 0.0984 | ±0.1968 | +1.905 | 0.0568 | . |
| Hypertension | +0.5895 | 1.4321 | ±2.8641 | +0.412 | 0.6806 |  |
| High cholesterol | +1.2862 | 1.3262 | ±2.6523 | +0.970 | 0.3321 |  |
| Kidney disease | -2.5770 | 1.6004 | ±3.2007 | -1.610 | 0.1073 |  |
| Circulatory disease | -0.1049 | 1.5816 | ±3.1632 | -0.066 | 0.9471 |  |
| **Avg. daily mean/SD** | **-0.8830** | 0.3452 | ±0.6905 | **-2.558** | **0.0105** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **849**, R² = **0.0719**, Adj R² = **0.0563**, F-statistic = **4.61** (p = **3.97e-08**), Residual SE = **17.171** on **834** df, AIC = **7252.1**, BIC = **7323.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.3076** | 6.6568 | ±13.3136 | **+18.524** | **1.33e-76** | *** |
| **Education: graduate level (vs college)** | **-3.1623** | 1.2407 | ±2.4813 | **-2.549** | **0.0108** | * |
| **Education: high school or below (vs college)** | **+5.1153** | 2.0174 | ±4.0347 | **+2.536** | **0.0112** | * |
| **Site: UCSD (vs UAB)** | **+3.1765** | 1.5283 | ±3.0567 | **+2.078** | **0.0377** | * |
| Site: UW (vs UAB) | -1.0423 | 1.3958 | ±2.7917 | -0.747 | 0.4553 |  |
| Season: spring (vs autumn) | +2.5104 | 1.5097 | ±3.0193 | +1.663 | 0.0963 | . |
| Season: summer (vs autumn) | +2.7206 | 1.6176 | ±3.2351 | +1.682 | 0.0926 | . |
| **Season: winter (vs autumn)** | **+6.0566** | 1.9084 | ±3.8168 | **+3.174** | **0.0015** | ** |
| Age (years) | -0.1206 | 0.0670 | ±0.1341 | -1.799 | 0.0720 | . |
| BMI (kg/m2) | +0.1761 | 0.0992 | ±0.1984 | +1.775 | 0.0760 | . |
| Hypertension | +0.6619 | 1.4367 | ±2.8734 | +0.461 | 0.6450 |  |
| High cholesterol | +1.2186 | 1.3327 | ±2.6653 | +0.914 | 0.3605 |  |
| Kidney disease | -2.2467 | 1.5788 | ±3.1576 | -1.423 | 0.1547 |  |
| Circulatory disease | -0.0893 | 1.5863 | ±3.1726 | -0.056 | 0.9551 |  |
| MAG (mg/dL/h) | +0.0486 | 0.0670 | ±0.1340 | +0.726 | 0.4680 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **849**, R² = **0.0722**, Adj R² = **0.0566**, F-statistic = **4.63** (p = **3.58e-08**), Residual SE = **17.169** on **834** df, AIC = **7251.8**, BIC = **7323.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.8817** | 6.6401 | ±13.2802 | **+18.657** | **1.11e-77** | *** |
| **Education: graduate level (vs college)** | **-3.1429** | 1.2419 | ±2.4838 | **-2.531** | **0.0114** | * |
| **Education: high school or below (vs college)** | **+5.0338** | 2.0038 | ±4.0077 | **+2.512** | **0.0120** | * |
| **Site: UCSD (vs UAB)** | **+3.2227** | 1.5427 | ±3.0853 | **+2.089** | **0.0367** | * |
| Site: UW (vs UAB) | -1.0922 | 1.4027 | ±2.8054 | -0.779 | 0.4362 |  |
| Season: spring (vs autumn) | +2.4761 | 1.5095 | ±3.0190 | +1.640 | 0.1009 |  |
| Season: summer (vs autumn) | +2.6860 | 1.6229 | ±3.2458 | +1.655 | 0.0979 | . |
| **Season: winter (vs autumn)** | **+6.0023** | 1.9083 | ±3.8166 | **+3.145** | **0.0017** | ** |
| Age (years) | -0.1271 | 0.0673 | ±0.1347 | -1.887 | 0.0591 | . |
| BMI (kg/m2) | +0.1803 | 0.0992 | ±0.1985 | +1.816 | 0.0693 | . |
| Hypertension | +0.6809 | 1.4358 | ±2.8716 | +0.474 | 0.6354 |  |
| High cholesterol | +1.2305 | 1.3268 | ±2.6536 | +0.927 | 0.3537 |  |
| Kidney disease | -2.3906 | 1.5925 | ±3.1850 | -1.501 | 0.1333 |  |
| Circulatory disease | -0.1168 | 1.5865 | ±3.1730 | -0.074 | 0.9413 |  |
| Avg. daily range (mg/dL) | +0.0133 | 0.0138 | ±0.0277 | +0.959 | 0.3376 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **849**, R² = **0.0735**, Adj R² = **0.0579**, F-statistic = **4.73** (p = **2.20e-08**), Residual SE = **17.157** on **834** df, AIC = **7250.6**, BIC = **7321.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.5396** | 6.4098 | ±12.8196 | **+19.742** | **9.48e-87** | *** |
| **Education: graduate level (vs college)** | **-3.4529** | 1.2387 | ±2.4774 | **-2.787** | **0.0053** | ** |
| **Education: high school or below (vs college)** | **+5.3391** | 1.9937 | ±3.9873 | **+2.678** | **0.0074** | ** |
| Site: UCSD (vs UAB) | +2.9988 | 1.5610 | ±3.1220 | +1.921 | 0.0547 | . |
| Site: UW (vs UAB) | -1.3269 | 1.4104 | ±2.8208 | -0.941 | 0.3468 |  |
| Season: spring (vs autumn) | +2.5049 | 1.5087 | ±3.0175 | +1.660 | 0.0969 | . |
| Season: summer (vs autumn) | +2.6542 | 1.6222 | ±3.2444 | +1.636 | 0.1018 |  |
| **Season: winter (vs autumn)** | **+6.1649** | 1.8853 | ±3.7705 | **+3.270** | **0.0011** | ** |
| Age (years) | -0.1206 | 0.0677 | ±0.1354 | -1.782 | 0.0748 | . |
| BMI (kg/m2) | +0.1841 | 0.1004 | ±0.2008 | +1.835 | 0.0666 | . |
| Hypertension | +0.6705 | 1.4410 | ±2.8821 | +0.465 | 0.6417 |  |
| High cholesterol | +1.1601 | 1.3206 | ±2.6413 | +0.878 | 0.3797 |  |
| Kidney disease | -1.8669 | 1.6090 | ±3.2181 | -1.160 | 0.2459 |  |
| Circulatory disease | +0.0586 | 1.5712 | ±3.1425 | +0.037 | 0.9703 |  |
| SD of daily means (mg/dL) | -0.1060 | 0.1271 | ±0.2542 | -0.834 | 0.4042 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **849**, R² = **0.0718**, Adj R² = **0.0562**, F-statistic = **4.61** (p = **4.08e-08**), Residual SE = **17.172** on **834** df, AIC = **7252.1**, BIC = **7323.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.9866** | 6.6884 | ±13.3769 | **+18.537** | **1.03e-76** | *** |
| **Education: graduate level (vs college)** | **-3.3317** | 1.2291 | ±2.4582 | **-2.711** | **0.0067** | ** |
| **Education: high school or below (vs college)** | **+5.3281** | 2.0087 | ±4.0174 | **+2.652** | **0.0080** | ** |
| Site: UCSD (vs UAB) | +3.0140 | 1.5512 | ±3.1024 | +1.943 | 0.0520 | . |
| Site: UW (vs UAB) | -1.2247 | 1.4030 | ±2.8061 | -0.873 | 0.3827 |  |
| Season: spring (vs autumn) | +2.5259 | 1.5083 | ±3.0166 | +1.675 | 0.0940 | . |
| Season: summer (vs autumn) | +2.6164 | 1.6293 | ±3.2586 | +1.606 | 0.1083 |  |
| **Season: winter (vs autumn)** | **+6.1122** | 1.8806 | ±3.7612 | **+3.250** | **0.0012** | ** |
| Age (years) | -0.1182 | 0.0672 | ±0.1345 | -1.758 | 0.0788 | . |
| BMI (kg/m2) | +0.1793 | 0.0985 | ±0.1971 | +1.819 | 0.0689 | . |
| Hypertension | +0.6027 | 1.4291 | ±2.8581 | +0.422 | 0.6732 |  |
| High cholesterol | +1.1586 | 1.3261 | ±2.6522 | +0.874 | 0.3823 |  |
| Kidney disease | -2.0048 | 1.6010 | ±3.2020 | -1.252 | 0.2105 |  |
| Circulatory disease | -0.0708 | 1.5882 | ±3.1765 | -0.045 | 0.9645 |  |
| Time in range 70-180, pooled (%) | +0.0175 | 0.0261 | ±0.0523 | +0.671 | 0.5024 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **849**, R² = **0.0720**, Adj R² = **0.0564**, F-statistic = **4.62** (p = **3.85e-08**), Residual SE = **17.171** on **834** df, AIC = **7252.0**, BIC = **7323.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.7887** | 6.6839 | ±13.3679 | **+18.520** | **1.41e-76** | *** |
| **Education: graduate level (vs college)** | **-3.3380** | 1.2298 | ±2.4595 | **-2.714** | **0.0066** | ** |
| **Education: high school or below (vs college)** | **+5.3474** | 2.0073 | ±4.0147 | **+2.664** | **0.0077** | ** |
| Site: UCSD (vs UAB) | +2.9979 | 1.5525 | ±3.1049 | +1.931 | 0.0535 | . |
| Site: UW (vs UAB) | -1.2299 | 1.4031 | ±2.8063 | -0.877 | 0.3808 |  |
| Season: spring (vs autumn) | +2.5312 | 1.5080 | ±3.0161 | +1.678 | 0.0933 | . |
| Season: summer (vs autumn) | +2.6185 | 1.6282 | ±3.2565 | +1.608 | 0.1078 |  |
| **Season: winter (vs autumn)** | **+6.1263** | 1.8777 | ±3.7553 | **+3.263** | **0.0011** | ** |
| Age (years) | -0.1177 | 0.0673 | ±0.1345 | -1.750 | 0.0801 | . |
| BMI (kg/m2) | +0.1797 | 0.0985 | ±0.1969 | +1.825 | 0.0681 | . |
| Hypertension | +0.5972 | 1.4290 | ±2.8580 | +0.418 | 0.6760 |  |
| High cholesterol | +1.1552 | 1.3256 | ±2.6512 | +0.871 | 0.3835 |  |
| Kidney disease | -1.9863 | 1.5995 | ±3.1989 | -1.242 | 0.2143 |  |
| Circulatory disease | -0.0680 | 1.5884 | ±3.1768 | -0.043 | 0.9658 |  |
| Avg. daily time in range 70-180 (%) | +0.0195 | 0.0261 | ±0.0522 | +0.748 | 0.4547 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.0713**, Adj R² = **0.0557**, F-statistic = **4.57** (p = **5.01e-08**), Residual SE = **17.177** on **834** df, AIC = **7252.6**, BIC = **7323.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.6734** | 6.2605 | ±12.5210 | **+20.074** | **1.24e-89** | *** |
| **Education: graduate level (vs college)** | **-3.2538** | 1.2484 | ±2.4969 | **-2.606** | **0.0092** | ** |
| **Education: high school or below (vs college)** | **+5.1846** | 1.9842 | ±3.9684 | **+2.613** | **0.0090** | ** |
| **Site: UCSD (vs UAB)** | **+3.0936** | 1.5362 | ±3.0723 | **+2.014** | **0.0440** | * |
| Site: UW (vs UAB) | -1.2083 | 1.3923 | ±2.7846 | -0.868 | 0.3855 |  |
| Season: spring (vs autumn) | +2.5092 | 1.5095 | ±3.0191 | +1.662 | 0.0965 | . |
| Season: summer (vs autumn) | +2.6409 | 1.6226 | ±3.2452 | +1.628 | 0.1036 |  |
| **Season: winter (vs autumn)** | **+6.0340** | 1.9140 | ±3.8279 | **+3.153** | **0.0016** | ** |
| Age (years) | -0.1226 | 0.0661 | ±0.1322 | -1.856 | 0.0635 | . |
| BMI (kg/m2) | +0.1778 | 0.1004 | ±0.2008 | +1.772 | 0.0765 | . |
| Hypertension | +0.6581 | 1.4408 | ±2.8817 | +0.457 | 0.6478 |  |
| High cholesterol | +1.1818 | 1.3351 | ±2.6702 | +0.885 | 0.3760 |  |
| Kidney disease | -2.1287 | 1.5981 | ±3.1961 | -1.332 | 0.1828 |  |
| Circulatory disease | -0.0743 | 1.5752 | ±3.1504 | -0.047 | 0.9624 |  |
| Any reading < 54 during wear (0/1) | -0.3089 | 1.4398 | ±2.8797 | -0.215 | 0.8301 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.0716**, Adj R² = **0.0560**, F-statistic = **4.59** (p = **4.49e-08**), Residual SE = **17.175** on **834** df, AIC = **7252.4**, BIC = **7323.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.4136** | 6.4121 | ±12.8242 | **+19.559** | **3.46e-85** | *** |
| **Education: graduate level (vs college)** | **-3.2339** | 1.2502 | ±2.5004 | **-2.587** | **0.0097** | ** |
| **Education: high school or below (vs college)** | **+5.2572** | 1.9885 | ±3.9771 | **+2.644** | **0.0082** | ** |
| **Site: UCSD (vs UAB)** | **+3.2010** | 1.5418 | ±3.0835 | **+2.076** | **0.0379** | * |
| Site: UW (vs UAB) | -1.0833 | 1.4143 | ±2.8286 | -0.766 | 0.4437 |  |
| Season: spring (vs autumn) | +2.5415 | 1.5112 | ±3.0224 | +1.682 | 0.0926 | . |
| Season: summer (vs autumn) | +2.6660 | 1.6241 | ±3.2481 | +1.642 | 0.1007 |  |
| **Season: winter (vs autumn)** | **+6.0859** | 1.9046 | ±3.8092 | **+3.195** | **0.0014** | ** |
| Age (years) | -0.1212 | 0.0672 | ±0.1344 | -1.803 | 0.0714 | . |
| BMI (kg/m2) | +0.1748 | 0.0993 | ±0.1986 | +1.761 | 0.0783 | . |
| Hypertension | +0.6221 | 1.4365 | ±2.8730 | +0.433 | 0.6649 |  |
| High cholesterol | +1.2107 | 1.3278 | ±2.6557 | +0.912 | 0.3619 |  |
| Kidney disease | -2.1018 | 1.5925 | ±3.1851 | -1.320 | 0.1869 |  |
| Circulatory disease | -0.1523 | 1.5843 | ±3.1687 | -0.096 | 0.9234 |  |
| Time < 54 (%) | +0.8004 | 0.9856 | ±1.9711 | +0.812 | 0.4167 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **849**, R² = **0.0722**, Adj R² = **0.0566**, F-statistic = **4.64** (p = **3.55e-08**), Residual SE = **17.169** on **834** df, AIC = **7251.8**, BIC = **7322.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.4246** | 6.4144 | ±12.8288 | **+19.554** | **3.84e-85** | *** |
| **Education: graduate level (vs college)** | **-3.2066** | 1.2486 | ±2.4972 | **-2.568** | **0.0102** | * |
| **Education: high school or below (vs college)** | **+5.2755** | 1.9904 | ±3.9809 | **+2.650** | **0.0080** | ** |
| **Site: UCSD (vs UAB)** | **+3.2290** | 1.5395 | ±3.0789 | **+2.097** | **0.0360** | * |
| Site: UW (vs UAB) | -1.0527 | 1.4133 | ±2.8266 | -0.745 | 0.4564 |  |
| Season: spring (vs autumn) | +2.5895 | 1.5123 | ±3.0246 | +1.712 | 0.0868 | . |
| Season: summer (vs autumn) | +2.6791 | 1.6251 | ±3.2503 | +1.649 | 0.0992 | . |
| **Season: winter (vs autumn)** | **+6.0967** | 1.9045 | ±3.8090 | **+3.201** | **0.0014** | ** |
| Age (years) | -0.1226 | 0.0673 | ±0.1346 | -1.822 | 0.0684 | . |
| BMI (kg/m2) | +0.1751 | 0.0991 | ±0.1981 | +1.768 | 0.0771 | . |
| Hypertension | +0.6200 | 1.4348 | ±2.8696 | +0.432 | 0.6656 |  |
| High cholesterol | +1.2373 | 1.3278 | ±2.6555 | +0.932 | 0.3514 |  |
| Kidney disease | -2.1078 | 1.5919 | ±3.1839 | -1.324 | 0.1855 |  |
| Circulatory disease | -0.1800 | 1.5890 | ±3.1780 | -0.113 | 0.9098 |  |
| Avg. daily time < 54 (%) | +1.2758 | 1.0453 | ±2.0907 | +1.221 | 0.2223 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **849**, R² = **0.0721**, Adj R² = **0.0566**, F-statistic = **4.63** (p = **3.62e-08**), Residual SE = **17.169** on **834** df, AIC = **7251.8**, BIC = **7323.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.4183** | 6.4185 | ±12.8369 | **+19.540** | **5.00e-85** | *** |
| **Education: graduate level (vs college)** | **-3.1976** | 1.2501 | ±2.5002 | **-2.558** | **0.0105** | * |
| **Education: high school or below (vs college)** | **+5.2045** | 1.9969 | ±3.9938 | **+2.606** | **0.0092** | ** |
| **Site: UCSD (vs UAB)** | **+3.2175** | 1.5387 | ±3.0775 | **+2.091** | **0.0365** | * |
| Site: UW (vs UAB) | -1.0795 | 1.4182 | ±2.8365 | -0.761 | 0.4465 |  |
| Season: spring (vs autumn) | +2.5956 | 1.5116 | ±3.0232 | +1.717 | 0.0860 | . |
| Season: summer (vs autumn) | +2.7053 | 1.6220 | ±3.2440 | +1.668 | 0.0953 | . |
| **Season: winter (vs autumn)** | **+6.1344** | 1.8957 | ±3.7914 | **+3.236** | **0.0012** | ** |
| Age (years) | -0.1237 | 0.0675 | ±0.1351 | -1.832 | 0.0669 | . |
| BMI (kg/m2) | +0.1750 | 0.0993 | ±0.1986 | +1.762 | 0.0780 | . |
| Hypertension | +0.6262 | 1.4348 | ±2.8695 | +0.436 | 0.6625 |  |
| High cholesterol | +1.2093 | 1.3280 | ±2.6560 | +0.911 | 0.3625 |  |
| Kidney disease | -2.1257 | 1.5916 | ±3.1832 | -1.336 | 0.1817 |  |
| Circulatory disease | -0.1375 | 1.5858 | ±3.1716 | -0.087 | 0.9309 |  |
| Time 54-69, pooled (%) | +0.3679 | 0.3629 | ±0.7258 | +1.014 | 0.3106 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **849**, R² = **0.0720**, Adj R² = **0.0564**, F-statistic = **4.62** (p = **3.87e-08**), Residual SE = **17.171** on **834** df, AIC = **7252.0**, BIC = **7323.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.4942** | 6.4209 | ±12.8418 | **+19.545** | **4.58e-85** | *** |
| **Education: graduate level (vs college)** | **-3.1998** | 1.2496 | ±2.4992 | **-2.561** | **0.0104** | * |
| **Education: high school or below (vs college)** | **+5.1965** | 1.9976 | ±3.9953 | **+2.601** | **0.0093** | ** |
| **Site: UCSD (vs UAB)** | **+3.1988** | 1.5381 | ±3.0763 | **+2.080** | **0.0376** | * |
| Site: UW (vs UAB) | -1.0933 | 1.4187 | ±2.8374 | -0.771 | 0.4409 |  |
| Season: spring (vs autumn) | +2.5828 | 1.5122 | ±3.0244 | +1.708 | 0.0876 | . |
| Season: summer (vs autumn) | +2.6929 | 1.6232 | ±3.2464 | +1.659 | 0.0971 | . |
| **Season: winter (vs autumn)** | **+6.1190** | 1.8971 | ±3.7943 | **+3.225** | **0.0013** | ** |
| Age (years) | -0.1243 | 0.0677 | ±0.1353 | -1.837 | 0.0662 | . |
| BMI (kg/m2) | +0.1752 | 0.0992 | ±0.1984 | +1.766 | 0.0774 | . |
| Hypertension | +0.6281 | 1.4345 | ±2.8690 | +0.438 | 0.6615 |  |
| High cholesterol | +1.2116 | 1.3285 | ±2.6570 | +0.912 | 0.3618 |  |
| Kidney disease | -2.1187 | 1.5928 | ±3.1855 | -1.330 | 0.1834 |  |
| Circulatory disease | -0.1246 | 1.5863 | ±3.1726 | -0.079 | 0.9374 |  |
| Avg. daily time 54-69 (%) | +0.3206 | 0.3446 | ±0.6892 | +0.930 | 0.3523 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **849**, R² = **0.0721**, Adj R² = **0.0565**, F-statistic = **4.63** (p = **3.69e-08**), Residual SE = **17.170** on **834** df, AIC = **7251.9**, BIC = **7323.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3955** | 6.4157 | ±12.8314 | **+19.545** | **4.54e-85** | *** |
| **Education: graduate level (vs college)** | **-3.2011** | 1.2505 | ±2.5010 | **-2.560** | **0.0105** | * |
| **Education: high school or below (vs college)** | **+5.2243** | 1.9945 | ±3.9890 | **+2.619** | **0.0088** | ** |
| **Site: UCSD (vs UAB)** | **+3.2285** | 1.5398 | ±3.0796 | **+2.097** | **0.0360** | * |
| Site: UW (vs UAB) | -1.0637 | 1.4187 | ±2.8374 | -0.750 | 0.4534 |  |
| Season: spring (vs autumn) | +2.5902 | 1.5114 | ±3.0227 | +1.714 | 0.0866 | . |
| Season: summer (vs autumn) | +2.7005 | 1.6222 | ±3.2443 | +1.665 | 0.0960 | . |
| **Season: winter (vs autumn)** | **+6.1302** | 1.8970 | ±3.7939 | **+3.232** | **0.0012** | ** |
| Age (years) | -0.1231 | 0.0675 | ±0.1349 | -1.826 | 0.0679 | . |
| BMI (kg/m2) | +0.1746 | 0.0993 | ±0.1987 | +1.758 | 0.0788 | . |
| Hypertension | +0.6221 | 1.4347 | ±2.8694 | +0.434 | 0.6646 |  |
| High cholesterol | +1.2119 | 1.3280 | ±2.6561 | +0.913 | 0.3615 |  |
| Kidney disease | -2.1174 | 1.5917 | ±3.1833 | -1.330 | 0.1834 |  |
| Circulatory disease | -0.1506 | 1.5853 | ±3.1706 | -0.095 | 0.9243 |  |
| Time < 70 (%) | +0.2955 | 0.2819 | ±0.5639 | +1.048 | 0.2945 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **849**, R² = **0.0721**, Adj R² = **0.0565**, F-statistic = **4.63** (p = **3.65e-08**), Residual SE = **17.169** on **834** df, AIC = **7251.9**, BIC = **7323.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.4719** | 6.4187 | ±12.8374 | **+19.548** | **4.30e-85** | *** |
| **Education: graduate level (vs college)** | **-3.1938** | 1.2495 | ±2.4991 | **-2.556** | **0.0106** | * |
| **Education: high school or below (vs college)** | **+5.2137** | 1.9959 | ±3.9918 | **+2.612** | **0.0090** | ** |
| **Site: UCSD (vs UAB)** | **+3.2168** | 1.5388 | ±3.0776 | **+2.091** | **0.0366** | * |
| Site: UW (vs UAB) | -1.0722 | 1.4188 | ±2.8375 | -0.756 | 0.4498 |  |
| Season: spring (vs autumn) | +2.5941 | 1.5123 | ±3.0245 | +1.715 | 0.0863 | . |
| Season: summer (vs autumn) | +2.6958 | 1.6234 | ±3.2468 | +1.661 | 0.0968 | . |
| **Season: winter (vs autumn)** | **+6.1227** | 1.8981 | ±3.7963 | **+3.226** | **0.0013** | ** |
| Age (years) | -0.1243 | 0.0676 | ±0.1352 | -1.839 | 0.0660 | . |
| BMI (kg/m2) | +0.1749 | 0.0992 | ±0.1984 | +1.764 | 0.0778 | . |
| Hypertension | +0.6245 | 1.4342 | ±2.8685 | +0.435 | 0.6633 |  |
| High cholesterol | +1.2195 | 1.3287 | ±2.6573 | +0.918 | 0.3587 |  |
| Kidney disease | -2.1157 | 1.5920 | ±3.1841 | -1.329 | 0.1839 |  |
| Circulatory disease | -0.1415 | 1.5861 | ±3.1721 | -0.089 | 0.9289 |  |
| Avg. daily time < 70 (%) | +0.2914 | 0.2624 | ±0.5249 | +1.111 | 0.2668 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.0749**, Adj R² = **0.0594**, F-statistic = **4.83** (p = **1.29e-08**), Residual SE = **17.143** on **834** df, AIC = **7249.3**, BIC = **7320.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+119.0980** | 7.1120 | ±14.2240 | **+16.746** | **6.05e-63** | *** |
| **Education: graduate level (vs college)** | **-3.4732** | 1.2425 | ±2.4849 | **-2.795** | **0.0052** | ** |
| **Education: high school or below (vs college)** | **+5.4751** | 1.9993 | ±3.9985 | **+2.739** | **0.0062** | ** |
| Site: UCSD (vs UAB) | +2.9201 | 1.5553 | ±3.1105 | +1.878 | 0.0604 | . |
| Site: UW (vs UAB) | -1.3847 | 1.4138 | ±2.8276 | -0.979 | 0.3274 |  |
| Season: spring (vs autumn) | +2.4749 | 1.5150 | ±3.0299 | +1.634 | 0.1023 |  |
| Season: summer (vs autumn) | +2.4248 | 1.6431 | ±3.2863 | +1.476 | 0.1400 |  |
| **Season: winter (vs autumn)** | **+6.0898** | 1.8941 | ±3.7881 | **+3.215** | **0.0013** | ** |
| Age (years) | -0.1237 | 0.0675 | ±0.1350 | -1.833 | 0.0668 | . |
| BMI (kg/m2) | +0.1810 | 0.0981 | ±0.1963 | +1.844 | 0.0651 | . |
| Hypertension | +0.6672 | 1.4347 | ±2.8694 | +0.465 | 0.6419 |  |
| High cholesterol | +1.1399 | 1.3203 | ±2.6407 | +0.863 | 0.3880 |  |
| Kidney disease | -1.9100 | 1.5884 | ±3.1767 | -1.203 | 0.2292 |  |
| Circulatory disease | -0.0487 | 1.5854 | ±3.1709 | -0.031 | 0.9755 |  |
| Time 54-250, pooled (%) | +0.0710 | 0.0429 | ±0.0857 | +1.657 | 0.0976 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **849**, R² = **0.0753**, Adj R² = **0.0598**, F-statistic = **4.85** (p = **1.12e-08**), Residual SE = **17.140** on **834** df, AIC = **7248.9**, BIC = **7320.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+118.6331** | 7.1480 | ±14.2959 | **+16.597** | **7.36e-62** | *** |
| **Education: graduate level (vs college)** | **-3.4815** | 1.2426 | ±2.4852 | **-2.802** | **0.0051** | ** |
| **Education: high school or below (vs college)** | **+5.4866** | 1.9967 | ±3.9934 | **+2.748** | **0.0060** | ** |
| Site: UCSD (vs UAB) | +2.9077 | 1.5547 | ±3.1095 | +1.870 | 0.0615 | . |
| Site: UW (vs UAB) | -1.3858 | 1.4126 | ±2.8253 | -0.981 | 0.3266 |  |
| Season: spring (vs autumn) | +2.4850 | 1.5144 | ±3.0288 | +1.641 | 0.1008 |  |
| Season: summer (vs autumn) | +2.4309 | 1.6412 | ±3.2825 | +1.481 | 0.1386 |  |
| **Season: winter (vs autumn)** | **+6.1044** | 1.8924 | ±3.7848 | **+3.226** | **0.0013** | ** |
| Age (years) | -0.1229 | 0.0674 | ±0.1349 | -1.823 | 0.0684 | . |
| BMI (kg/m2) | +0.1813 | 0.0980 | ±0.1960 | +1.850 | 0.0643 | . |
| Hypertension | +0.6628 | 1.4346 | ±2.8691 | +0.462 | 0.6441 |  |
| High cholesterol | +1.1365 | 1.3200 | ±2.6400 | +0.861 | 0.3893 |  |
| Kidney disease | -1.8846 | 1.5859 | ±3.1718 | -1.188 | 0.2347 |  |
| Circulatory disease | -0.0379 | 1.5861 | ±3.1722 | -0.024 | 0.9809 |  |
| Avg. daily time 54-250 (%) | +0.0752 | 0.0442 | ±0.0883 | +1.702 | 0.0888 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.0715**, Adj R² = **0.0559**, F-statistic = **4.59** (p = **4.59e-08**), Residual SE = **17.175** on **834** df, AIC = **7252.4**, BIC = **7323.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.5058** | 6.4219 | ±12.8438 | **+19.543** | **4.69e-85** | *** |
| **Education: graduate level (vs college)** | **-3.2322** | 1.2370 | ±2.4740 | **-2.613** | **0.0090** | ** |
| **Education: high school or below (vs college)** | **+5.1376** | 2.0043 | ±4.0086 | **+2.563** | **0.0104** | * |
| **Site: UCSD (vs UAB)** | **+3.1751** | 1.5366 | ±3.0732 | **+2.066** | **0.0388** | * |
| Site: UW (vs UAB) | -1.1905 | 1.4127 | ±2.8254 | -0.843 | 0.3994 |  |
| Season: spring (vs autumn) | +2.4802 | 1.5110 | ±3.0221 | +1.641 | 0.1007 |  |
| Season: summer (vs autumn) | +2.6207 | 1.6257 | ±3.2514 | +1.612 | 0.1070 |  |
| **Season: winter (vs autumn)** | **+5.9961** | 1.8673 | ±3.7345 | **+3.211** | **0.0013** | ** |
| Age (years) | -0.1259 | 0.0675 | ±0.1349 | -1.865 | 0.0621 | . |
| BMI (kg/m2) | +0.1750 | 0.0988 | ±0.1976 | +1.772 | 0.0765 | . |
| Hypertension | +0.6925 | 1.4095 | ±2.8190 | +0.491 | 0.6232 |  |
| High cholesterol | +1.2244 | 1.3356 | ±2.6711 | +0.917 | 0.3593 |  |
| Kidney disease | -2.1956 | 1.6145 | ±3.2290 | -1.360 | 0.1738 |  |
| Circulatory disease | -0.1040 | 1.5879 | ±3.1758 | -0.065 | 0.9478 |  |
| Time 181-250, pooled (%) | +0.0198 | 0.0466 | ±0.0933 | +0.425 | 0.6708 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **849**, R² = **0.0714**, Adj R² = **0.0558**, F-statistic = **4.58** (p = **4.75e-08**), Residual SE = **17.176** on **834** df, AIC = **7252.5**, BIC = **7323.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.5080** | 6.4240 | ±12.8480 | **+19.537** | **5.29e-85** | *** |
| **Education: graduate level (vs college)** | **-3.2377** | 1.2381 | ±2.4763 | **-2.615** | **0.0089** | ** |
| **Education: high school or below (vs college)** | **+5.1447** | 2.0044 | ±4.0088 | **+2.567** | **0.0103** | * |
| **Site: UCSD (vs UAB)** | **+3.1684** | 1.5392 | ±3.0783 | **+2.059** | **0.0395** | * |
| Site: UW (vs UAB) | -1.1860 | 1.4112 | ±2.8224 | -0.840 | 0.4007 |  |
| Season: spring (vs autumn) | +2.4856 | 1.5109 | ±3.0217 | +1.645 | 0.0999 | . |
| Season: summer (vs autumn) | +2.6254 | 1.6257 | ±3.2514 | +1.615 | 0.1063 |  |
| **Season: winter (vs autumn)** | **+6.0036** | 1.8656 | ±3.7313 | **+3.218** | **0.0013** | ** |
| Age (years) | -0.1250 | 0.0675 | ±0.1349 | -1.853 | 0.0639 | . |
| BMI (kg/m2) | +0.1753 | 0.0988 | ±0.1977 | +1.773 | 0.0762 | . |
| Hypertension | +0.6829 | 1.4113 | ±2.8226 | +0.484 | 0.6285 |  |
| High cholesterol | +1.2184 | 1.3342 | ±2.6684 | +0.913 | 0.3611 |  |
| Kidney disease | -2.1840 | 1.6149 | ±3.2298 | -1.352 | 0.1762 |  |
| Circulatory disease | -0.1008 | 1.5876 | ±3.1753 | -0.064 | 0.9494 |  |
| Avg. daily time 181-250 (%) | +0.0162 | 0.0452 | ±0.0904 | +0.359 | 0.7197 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **849**, R² = **0.0719**, Adj R² = **0.0563**, F-statistic = **4.62** (p = **3.94e-08**), Residual SE = **17.171** on **834** df, AIC = **7252.0**, BIC = **7323.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7430** | 6.4671 | ±12.9341 | **+19.444** | **3.30e-84** | *** |
| **Education: graduate level (vs college)** | **-3.3330** | 1.2298 | ±2.4596 | **-2.710** | **0.0067** | ** |
| **Education: high school or below (vs college)** | **+5.3370** | 2.0078 | ±4.0157 | **+2.658** | **0.0079** | ** |
| Site: UCSD (vs UAB) | +3.0147 | 1.5496 | ±3.0992 | +1.945 | 0.0517 | . |
| Site: UW (vs UAB) | -1.2202 | 1.4034 | ±2.8069 | -0.869 | 0.3846 |  |
| Season: spring (vs autumn) | +2.5317 | 1.5080 | ±3.0159 | +1.679 | 0.0932 | . |
| Season: summer (vs autumn) | +2.6176 | 1.6288 | ±3.2576 | +1.607 | 0.1080 |  |
| **Season: winter (vs autumn)** | **+6.1204** | 1.8786 | ±3.7572 | **+3.258** | **0.0011** | ** |
| Age (years) | -0.1181 | 0.0672 | ±0.1345 | -1.757 | 0.0790 | . |
| BMI (kg/m2) | +0.1793 | 0.0985 | ±0.1971 | +1.819 | 0.0689 | . |
| Hypertension | +0.5992 | 1.4287 | ±2.8574 | +0.419 | 0.6749 |  |
| High cholesterol | +1.1572 | 1.3258 | ±2.6517 | +0.873 | 0.3828 |  |
| Kidney disease | -1.9974 | 1.6009 | ±3.2018 | -1.248 | 0.2122 |  |
| Circulatory disease | -0.0730 | 1.5883 | ±3.1766 | -0.046 | 0.9633 |  |
| Time > 180 (%) | -0.0186 | 0.0258 | ±0.0517 | -0.720 | 0.4717 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **849**, R² = **0.0721**, Adj R² = **0.0565**, F-statistic = **4.63** (p = **3.70e-08**), Residual SE = **17.170** on **834** df, AIC = **7251.9**, BIC = **7323.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7480** | 6.4666 | ±12.9331 | **+19.446** | **3.16e-84** | *** |
| **Education: graduate level (vs college)** | **-3.3385** | 1.2306 | ±2.4612 | **-2.713** | **0.0067** | ** |
| **Education: high school or below (vs college)** | **+5.3565** | 2.0066 | ±4.0132 | **+2.669** | **0.0076** | ** |
| Site: UCSD (vs UAB) | +2.9980 | 1.5509 | ±3.1017 | +1.933 | 0.0532 | . |
| Site: UW (vs UAB) | -1.2252 | 1.4034 | ±2.8068 | -0.873 | 0.3827 |  |
| Season: spring (vs autumn) | +2.5382 | 1.5077 | ±3.0154 | +1.683 | 0.0923 | . |
| Season: summer (vs autumn) | +2.6200 | 1.6278 | ±3.2555 | +1.610 | 0.1075 |  |
| **Season: winter (vs autumn)** | **+6.1351** | 1.8758 | ±3.7516 | **+3.271** | **0.0011** | ** |
| Age (years) | -0.1177 | 0.0672 | ±0.1345 | -1.750 | 0.0802 | . |
| BMI (kg/m2) | +0.1797 | 0.0985 | ±0.1969 | +1.825 | 0.0680 | . |
| Hypertension | +0.5934 | 1.4286 | ±2.8573 | +0.415 | 0.6779 |  |
| High cholesterol | +1.1544 | 1.3253 | ±2.6506 | +0.871 | 0.3837 |  |
| Kidney disease | -1.9780 | 1.5995 | ±3.1990 | -1.237 | 0.2162 |  |
| Circulatory disease | -0.0700 | 1.5883 | ±3.1767 | -0.044 | 0.9649 |  |
| Avg. daily time > 180 (%) | -0.0207 | 0.0259 | ±0.0517 | -0.799 | 0.4245 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **849**, R² = **0.0716**, Adj R² = **0.0560**, F-statistic = **4.60** (p = **4.38e-08**), Residual SE = **17.174** on **834** df, AIC = **7252.3**, BIC = **7323.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.6687** | 6.4752 | ±12.9504 | **+19.408** | **6.64e-84** | *** |
| **Education: graduate level (vs college)** | **-3.3295** | 1.2257 | ±2.4515 | **-2.716** | **0.0066** | ** |
| **Education: high school or below (vs college)** | **+5.3000** | 2.0028 | ±4.0056 | **+2.646** | **0.0081** | ** |
| Site: UCSD (vs UAB) | +3.0302 | 1.5552 | ±3.1103 | +1.948 | 0.0514 | . |
| Site: UW (vs UAB) | -1.2028 | 1.4035 | ±2.8070 | -0.857 | 0.3915 |  |
| Season: spring (vs autumn) | +2.5322 | 1.5066 | ±3.0131 | +1.681 | 0.0928 | . |
| Season: summer (vs autumn) | +2.6208 | 1.6307 | ±3.2614 | +1.607 | 0.1080 |  |
| **Season: winter (vs autumn)** | **+6.1090** | 1.8732 | ±3.7464 | **+3.261** | **0.0011** | ** |
| Age (years) | -0.1208 | 0.0674 | ±0.1347 | -1.794 | 0.0728 | . |
| BMI (kg/m2) | +0.1812 | 0.0984 | ±0.1967 | +1.842 | 0.0655 | . |
| Hypertension | +0.6053 | 1.4291 | ±2.8581 | +0.424 | 0.6719 |  |
| High cholesterol | +1.1645 | 1.3261 | ±2.6523 | +0.878 | 0.3799 |  |
| Kidney disease | -2.0414 | 1.6055 | ±3.2110 | -1.271 | 0.2036 |  |
| Circulatory disease | -0.0739 | 1.5864 | ±3.1729 | -0.047 | 0.9629 |  |
| Nocturnal time > 180 (%) | -0.0138 | 0.0277 | ±0.0555 | -0.498 | 0.6188 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.0734**, Adj R² = **0.0579**, F-statistic = **4.72** (p = **2.26e-08**), Residual SE = **17.157** on **834** df, AIC = **7250.7**, BIC = **7321.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0251** | 6.4404 | ±12.8808 | **+19.413** | **6.04e-84** | *** |
| **Education: graduate level (vs college)** | **-3.0829** | 1.2369 | ±2.4738 | **-2.492** | **0.0127** | * |
| **Education: high school or below (vs college)** | **+5.1105** | 1.9957 | ±3.9915 | **+2.561** | **0.0104** | * |
| **Site: UCSD (vs UAB)** | **+3.2162** | 1.5356 | ±3.0713 | **+2.094** | **0.0362** | * |
| Site: UW (vs UAB) | -1.2362 | 1.4088 | ±2.8176 | -0.877 | 0.3802 |  |
| Season: spring (vs autumn) | +2.5342 | 1.5110 | ±3.0220 | +1.677 | 0.0935 | . |
| Season: summer (vs autumn) | +2.6420 | 1.6216 | ±3.2432 | +1.629 | 0.1033 |  |
| **Season: winter (vs autumn)** | **+6.0394** | 1.9074 | ±3.8148 | **+3.166** | **0.0015** | ** |
| **Age (years)** | **-0.1360** | 0.0670 | ±0.1340 | **-2.029** | **0.0425** | * |
| BMI (kg/m2) | +0.1817 | 0.0995 | ±0.1990 | +1.826 | 0.0678 | . |
| Hypertension | +0.7321 | 1.4265 | ±2.8530 | +0.513 | 0.6078 |  |
| High cholesterol | +1.2250 | 1.3286 | ±2.6573 | +0.922 | 0.3565 |  |
| Kidney disease | -2.3325 | 1.5912 | ±3.1824 | -1.466 | 0.1427 |  |
| Circulatory disease | -0.0631 | 1.5856 | ±3.1711 | -0.040 | 0.9683 |  |
| Any reading > 250 during wear (0/1) | +1.7822 | 1.2101 | ±2.4203 | +1.473 | 0.1408 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **849**, R² = **0.0750**, Adj R² = **0.0595**, F-statistic = **4.83** (p = **1.26e-08**), Residual SE = **17.143** on **834** df, AIC = **7249.2**, BIC = **7320.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.1916** | 6.4653 | ±12.9307 | **+19.518** | **7.69e-85** | *** |
| **Education: graduate level (vs college)** | **-3.4726** | 1.2423 | ±2.4847 | **-2.795** | **0.0052** | ** |
| **Education: high school or below (vs college)** | **+5.4815** | 1.9993 | ±3.9986 | **+2.742** | **0.0061** | ** |
| Site: UCSD (vs UAB) | +2.9264 | 1.5543 | ±3.1086 | +1.883 | 0.0597 | . |
| Site: UW (vs UAB) | -1.3773 | 1.4132 | ±2.8264 | -0.975 | 0.3298 |  |
| Season: spring (vs autumn) | +2.4773 | 1.5149 | ±3.0299 | +1.635 | 0.1020 |  |
| Season: summer (vs autumn) | +2.4251 | 1.6429 | ±3.2858 | +1.476 | 0.1399 |  |
| **Season: winter (vs autumn)** | **+6.0927** | 1.8937 | ±3.7875 | **+3.217** | **0.0013** | ** |
| Age (years) | -0.1237 | 0.0675 | ±0.1350 | -1.832 | 0.0669 | . |
| BMI (kg/m2) | +0.1809 | 0.0981 | ±0.1963 | +1.843 | 0.0654 | . |
| Hypertension | +0.6656 | 1.4347 | ±2.8694 | +0.464 | 0.6427 |  |
| High cholesterol | +1.1407 | 1.3204 | ±2.6407 | +0.864 | 0.3876 |  |
| Kidney disease | -1.9070 | 1.5881 | ±3.1763 | -1.201 | 0.2298 |  |
| Circulatory disease | -0.0537 | 1.5856 | ±3.1711 | -0.034 | 0.9730 |  |
| Time > 250 (%) | -0.0714 | 0.0428 | ±0.0856 | -1.668 | 0.0954 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 849)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **849**, R² = **0.0754**, Adj R² = **0.0599**, F-statistic = **4.86** (p = **1.08e-08**), Residual SE = **17.139** on **834** df, AIC = **7248.8**, BIC = **7320.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.1514** | 6.4587 | ±12.9173 | **+19.532** | **5.86e-85** | *** |
| **Education: graduate level (vs college)** | **-3.4815** | 1.2425 | ±2.4850 | **-2.802** | **0.0051** | ** |
| **Education: high school or below (vs college)** | **+5.4946** | 1.9967 | ±3.9935 | **+2.752** | **0.0059** | ** |
| Site: UCSD (vs UAB) | +2.9116 | 1.5539 | ±3.1077 | +1.874 | 0.0610 | . |
| Site: UW (vs UAB) | -1.3809 | 1.4121 | ±2.8242 | -0.978 | 0.3281 |  |
| Season: spring (vs autumn) | +2.4894 | 1.5142 | ±3.0285 | +1.644 | 0.1002 |  |
| Season: summer (vs autumn) | +2.4299 | 1.6409 | ±3.2817 | +1.481 | 0.1386 |  |
| **Season: winter (vs autumn)** | **+6.1075** | 1.8920 | ±3.7840 | **+3.228** | **0.0012** | ** |
| Age (years) | -0.1230 | 0.0674 | ±0.1349 | -1.824 | 0.0682 | . |
| BMI (kg/m2) | +0.1813 | 0.0980 | ±0.1960 | +1.850 | 0.0643 | . |
| Hypertension | +0.6618 | 1.4345 | ±2.8689 | +0.461 | 0.6446 |  |
| High cholesterol | +1.1381 | 1.3201 | ±2.6402 | +0.862 | 0.3886 |  |
| Kidney disease | -1.8806 | 1.5858 | ±3.1716 | -1.186 | 0.2357 |  |
| Circulatory disease | -0.0424 | 1.5860 | ±3.1720 | -0.027 | 0.9787 |  |
| Avg. daily time > 250 (%) | -0.0761 | 0.0442 | ±0.0884 | -1.724 | 0.0848 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
