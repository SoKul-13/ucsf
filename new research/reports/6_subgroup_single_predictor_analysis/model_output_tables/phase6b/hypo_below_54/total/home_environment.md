# Phase 6b model output tables - Hypoglycaemia exposure: at least one reading < 54 - Total analysis base - Home environment

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 628; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **628**, R² = **0.1791**, Adj R² = **0.1617**, F-statistic = **10.31** (p = **7.19e-20**), Residual SE = **0.971** on **614** df, AIC = **1759.6**, BIC = **1821.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0331** | 0.3485 | ±0.6970 | **+8.703** | **3.23e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2104** | 0.0793 | ±0.1586 | **-2.654** | **0.0080** | ** |
| **Education: high school or below (vs college)** | **+0.6038** | 0.1911 | ±0.3823 | **+3.159** | **0.0016** | ** |
| Site: UCSD (vs UAB) | +0.1109 | 0.1042 | ±0.2084 | +1.065 | 0.2870 |  |
| **Site: UW (vs UAB)** | **-0.4015** | 0.0951 | ±0.1903 | **-4.220** | **2.44e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3812** | 0.1037 | ±0.2073 | **-3.678** | **2.35e-04** | *** |
| Season: summer (vs autumn) | -0.0960 | 0.1202 | ±0.2404 | -0.799 | 0.4244 |  |
| Season: winter (vs autumn) | -0.0531 | 0.1206 | ±0.2412 | -0.440 | 0.6596 |  |
| **Age (years)** | **-0.0184** | 0.0038 | ±0.0075 | **-4.875** | **1.09e-06** | *** |
| BMI (kg/m2) | +0.0077 | 0.0064 | ±0.0129 | +1.192 | 0.2333 |  |
| Hypertension | +0.1661 | 0.0897 | ±0.1794 | +1.853 | 0.0640 | . |
| High cholesterol | -0.0279 | 0.0836 | ±0.1672 | -0.334 | 0.7386 |  |
| Kidney disease | -0.0148 | 0.1401 | ±0.2803 | -0.105 | 0.9161 |  |
| Circulatory disease | -0.0076 | 0.1177 | ±0.2354 | -0.064 | 0.9487 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **628**, R² = **0.1882**, Adj R² = **0.1697**, F-statistic = **10.15** (p = **1.04e-20**), Residual SE = **0.967** on **613** df, AIC = **1754.6**, BIC = **1821.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.3976** | 0.4428 | ±0.8855 | **+5.415** | **6.12e-08** | *** |
| **Education: graduate level (vs college)** | **-0.1945** | 0.0788 | ±0.1576 | **-2.469** | **0.0136** | * |
| **Education: high school or below (vs college)** | **+0.5609** | 0.1912 | ±0.3825 | **+2.933** | **0.0034** | ** |
| Site: UCSD (vs UAB) | +0.1028 | 0.1042 | ±0.2084 | +0.987 | 0.3238 |  |
| **Site: UW (vs UAB)** | **-0.3839** | 0.0946 | ±0.1892 | **-4.057** | **4.96e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3741** | 0.1039 | ±0.2077 | **-3.602** | **3.16e-04** | *** |
| Season: summer (vs autumn) | -0.0881 | 0.1201 | ±0.2402 | -0.733 | 0.4634 |  |
| Season: winter (vs autumn) | -0.0450 | 0.1206 | ±0.2412 | -0.373 | 0.7090 |  |
| **Age (years)** | **-0.0195** | 0.0038 | ±0.0076 | **-5.164** | **2.42e-07** | *** |
| BMI (kg/m2) | +0.0064 | 0.0064 | ±0.0128 | +1.008 | 0.3135 |  |
| Hypertension | +0.1393 | 0.0905 | ±0.1810 | +1.539 | 0.1238 |  |
| High cholesterol | -0.0420 | 0.0831 | ±0.1662 | -0.505 | 0.6135 |  |
| Kidney disease | -0.0303 | 0.1355 | ±0.2710 | -0.224 | 0.8227 |  |
| Circulatory disease | -0.0055 | 0.1176 | ±0.2353 | -0.047 | 0.9624 |  |
| **HbA1c (%)** | **+0.1271** | 0.0562 | ±0.1123 | **+2.264** | **0.0236** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **628**, R² = **0.1793**, Adj R² = **0.1606**, F-statistic = **9.57** (p = **2.20e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.5**, BIC = **1828.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1062** | 0.3927 | ±0.7854 | **+7.909** | **2.59e-15** | *** |
| **Education: graduate level (vs college)** | **-0.2105** | 0.0794 | ±0.1588 | **-2.650** | **0.0080** | ** |
| **Education: high school or below (vs college)** | **+0.6095** | 0.1934 | ±0.3868 | **+3.152** | **0.0016** | ** |
| Site: UCSD (vs UAB) | +0.1113 | 0.1044 | ±0.2088 | +1.066 | 0.2863 |  |
| **Site: UW (vs UAB)** | **-0.4026** | 0.0950 | ±0.1900 | **-4.238** | **2.25e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3800** | 0.1036 | ±0.2072 | **-3.669** | **2.44e-04** | *** |
| Season: summer (vs autumn) | -0.0969 | 0.1205 | ±0.2411 | -0.804 | 0.4214 |  |
| Season: winter (vs autumn) | -0.0543 | 0.1209 | ±0.2419 | -0.449 | 0.6536 |  |
| **Age (years)** | **-0.0183** | 0.0038 | ±0.0076 | **-4.848** | **1.25e-06** | *** |
| BMI (kg/m2) | +0.0078 | 0.0064 | ±0.0129 | +1.206 | 0.2280 |  |
| Hypertension | +0.1711 | 0.0930 | ±0.1860 | +1.840 | 0.0658 | . |
| High cholesterol | -0.0258 | 0.0835 | ±0.1670 | -0.309 | 0.7570 |  |
| Kidney disease | -0.0091 | 0.1388 | ±0.2776 | -0.065 | 0.9480 |  |
| Circulatory disease | -0.0068 | 0.1179 | ±0.2359 | -0.058 | 0.9537 |  |
| Mean glucose (mg/dL) | -0.0007 | 0.0017 | ±0.0033 | -0.410 | 0.6819 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **628**, R² = **0.1793**, Adj R² = **0.1606**, F-statistic = **9.57** (p = **2.20e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.5**, BIC = **1828.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.1998** | 0.5367 | ±1.0733 | **+5.962** | **2.49e-09** | *** |
| **Education: graduate level (vs college)** | **-0.2105** | 0.0794 | ±0.1588 | **-2.650** | **0.0080** | ** |
| **Education: high school or below (vs college)** | **+0.6095** | 0.1934 | ±0.3868 | **+3.152** | **0.0016** | ** |
| Site: UCSD (vs UAB) | +0.1113 | 0.1044 | ±0.2088 | +1.066 | 0.2863 |  |
| **Site: UW (vs UAB)** | **-0.4026** | 0.0950 | ±0.1900 | **-4.238** | **2.25e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3800** | 0.1036 | ±0.2072 | **-3.669** | **2.44e-04** | *** |
| Season: summer (vs autumn) | -0.0969 | 0.1205 | ±0.2411 | -0.804 | 0.4214 |  |
| Season: winter (vs autumn) | -0.0543 | 0.1209 | ±0.2419 | -0.449 | 0.6536 |  |
| **Age (years)** | **-0.0183** | 0.0038 | ±0.0076 | **-4.848** | **1.25e-06** | *** |
| BMI (kg/m2) | +0.0078 | 0.0064 | ±0.0129 | +1.206 | 0.2280 |  |
| Hypertension | +0.1711 | 0.0930 | ±0.1860 | +1.840 | 0.0658 | . |
| High cholesterol | -0.0258 | 0.0835 | ±0.1670 | -0.309 | 0.7570 |  |
| Kidney disease | -0.0091 | 0.1388 | ±0.2776 | -0.065 | 0.9480 |  |
| Circulatory disease | -0.0068 | 0.1179 | ±0.2359 | -0.058 | 0.9537 |  |
| GMI (%) | -0.0283 | 0.0690 | ±0.1380 | -0.410 | 0.6819 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **628**, R² = **0.1792**, Adj R² = **0.1605**, F-statistic = **9.56** (p = **2.31e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.6**, BIC = **1828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0783** | 0.3914 | ±0.7828 | **+7.864** | **3.71e-15** | *** |
| **Education: graduate level (vs college)** | **-0.2103** | 0.0794 | ±0.1589 | **-2.647** | **0.0081** | ** |
| **Education: high school or below (vs college)** | **+0.6070** | 0.1926 | ±0.3852 | **+3.151** | **0.0016** | ** |
| Site: UCSD (vs UAB) | +0.1114 | 0.1045 | ±0.2091 | +1.066 | 0.2865 |  |
| **Site: UW (vs UAB)** | **-0.4019** | 0.0951 | ±0.1902 | **-4.226** | **2.38e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3801** | 0.1038 | ±0.2076 | **-3.661** | **2.51e-04** | *** |
| Season: summer (vs autumn) | -0.0970 | 0.1206 | ±0.2412 | -0.804 | 0.4212 |  |
| Season: winter (vs autumn) | -0.0533 | 0.1208 | ±0.2416 | -0.441 | 0.6591 |  |
| **Age (years)** | **-0.0184** | 0.0038 | ±0.0075 | **-4.874** | **1.10e-06** | *** |
| BMI (kg/m2) | +0.0078 | 0.0065 | ±0.0129 | +1.203 | 0.2291 |  |
| Hypertension | +0.1691 | 0.0932 | ±0.1864 | +1.814 | 0.0697 | . |
| High cholesterol | -0.0262 | 0.0838 | ±0.1675 | -0.312 | 0.7547 |  |
| Kidney disease | -0.0138 | 0.1400 | ±0.2800 | -0.099 | 0.9213 |  |
| Circulatory disease | -0.0074 | 0.1179 | ±0.2359 | -0.063 | 0.9498 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0004 | 0.0018 | ±0.0035 | -0.235 | 0.8139 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **628**, R² = **0.1796**, Adj R² = **0.1609**, F-statistic = **9.59** (p = **2.00e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.3**, BIC = **1827.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9986** | 0.3549 | ±0.7098 | **+8.449** | **2.95e-17** | *** |
| **Education: graduate level (vs college)** | **-0.2085** | 0.0793 | ±0.1586 | **-2.629** | **0.0086** | ** |
| **Education: high school or below (vs college)** | **+0.5915** | 0.1953 | ±0.3906 | **+3.029** | **0.0025** | ** |
| Site: UCSD (vs UAB) | +0.1108 | 0.1044 | ±0.2087 | +1.062 | 0.2881 |  |
| **Site: UW (vs UAB)** | **-0.3967** | 0.0949 | ±0.1897 | **-4.182** | **2.88e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3809** | 0.1040 | ±0.2079 | **-3.664** | **2.48e-04** | *** |
| Season: summer (vs autumn) | -0.0938 | 0.1205 | ±0.2409 | -0.779 | 0.4360 |  |
| Season: winter (vs autumn) | -0.0506 | 0.1211 | ±0.2423 | -0.418 | 0.6760 |  |
| **Age (years)** | **-0.0186** | 0.0038 | ±0.0077 | **-4.867** | **1.13e-06** | *** |
| BMI (kg/m2) | +0.0076 | 0.0064 | ±0.0128 | +1.189 | 0.2345 |  |
| Hypertension | +0.1592 | 0.0917 | ±0.1833 | +1.737 | 0.0824 | . |
| High cholesterol | -0.0282 | 0.0837 | ±0.1675 | -0.337 | 0.7363 |  |
| Kidney disease | -0.0320 | 0.1370 | ±0.2739 | -0.233 | 0.8155 |  |
| Circulatory disease | -0.0066 | 0.1178 | ±0.2356 | -0.056 | 0.9551 |  |
| Glucose SD, pooled (mg/dL) | +0.0021 | 0.0035 | ±0.0070 | +0.600 | 0.5485 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **628**, R² = **0.1794**, Adj R² = **0.1606**, F-statistic = **9.57** (p = **2.20e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.5**, BIC = **1828.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0098** | 0.3539 | ±0.7077 | **+8.505** | **1.81e-17** | *** |
| **Education: graduate level (vs college)** | **-0.2089** | 0.0793 | ±0.1586 | **-2.635** | **0.0084** | ** |
| **Education: high school or below (vs college)** | **+0.5944** | 0.1965 | ±0.3930 | **+3.025** | **0.0025** | ** |
| Site: UCSD (vs UAB) | +0.1105 | 0.1044 | ±0.2089 | +1.058 | 0.2900 |  |
| **Site: UW (vs UAB)** | **-0.3987** | 0.0949 | ±0.1897 | **-4.203** | **2.63e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3815** | 0.1039 | ±0.2078 | **-3.672** | **2.40e-04** | *** |
| Season: summer (vs autumn) | -0.0942 | 0.1206 | ±0.2412 | -0.781 | 0.4346 |  |
| Season: winter (vs autumn) | -0.0512 | 0.1212 | ±0.2423 | -0.423 | 0.6726 |  |
| **Age (years)** | **-0.0186** | 0.0038 | ±0.0077 | **-4.838** | **1.31e-06** | *** |
| BMI (kg/m2) | +0.0077 | 0.0064 | ±0.0129 | +1.190 | 0.2341 |  |
| Hypertension | +0.1618 | 0.0916 | ±0.1831 | +1.768 | 0.0771 | . |
| High cholesterol | -0.0284 | 0.0837 | ±0.1673 | -0.339 | 0.7346 |  |
| Kidney disease | -0.0267 | 0.1362 | ±0.2724 | -0.196 | 0.8445 |  |
| Circulatory disease | -0.0065 | 0.1177 | ±0.2354 | -0.055 | 0.9561 |  |
| Avg. daily SD (mg/dL) | +0.0016 | 0.0040 | ±0.0080 | +0.409 | 0.6824 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **628**, R² = **0.1806**, Adj R² = **0.1619**, F-statistic = **9.65** (p = **1.44e-19**), Residual SE = **0.971** on **613** df, AIC = **1760.5**, BIC = **1827.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9254** | 0.3667 | ±0.7334 | **+7.977** | **1.49e-15** | *** |
| **Education: graduate level (vs college)** | **-0.2067** | 0.0793 | ±0.1586 | **-2.608** | **0.0091** | ** |
| **Education: high school or below (vs college)** | **+0.5850** | 0.1948 | ±0.3897 | **+3.002** | **0.0027** | ** |
| Site: UCSD (vs UAB) | +0.1107 | 0.1045 | ±0.2089 | +1.060 | 0.2893 |  |
| **Site: UW (vs UAB)** | **-0.3920** | 0.0950 | ±0.1900 | **-4.126** | **3.69e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3789** | 0.1041 | ±0.2082 | **-3.639** | **2.74e-04** | *** |
| Season: summer (vs autumn) | -0.0945 | 0.1201 | ±0.2403 | -0.786 | 0.4316 |  |
| Season: winter (vs autumn) | -0.0494 | 0.1211 | ±0.2423 | -0.408 | 0.6833 |  |
| **Age (years)** | **-0.0191** | 0.0039 | ±0.0078 | **-4.875** | **1.09e-06** | *** |
| BMI (kg/m2) | +0.0077 | 0.0064 | ±0.0128 | +1.204 | 0.2286 |  |
| Hypertension | +0.1579 | 0.0901 | ±0.1802 | +1.752 | 0.0797 | . |
| High cholesterol | -0.0253 | 0.0842 | ±0.1684 | -0.300 | 0.7638 |  |
| Kidney disease | -0.0468 | 0.1391 | ±0.2781 | -0.336 | 0.7367 |  |
| Circulatory disease | -0.0049 | 0.1180 | ±0.2359 | -0.042 | 0.9668 |  |
| CV (%) | +0.0071 | 0.0074 | ±0.0149 | +0.960 | 0.3372 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **628**, R² = **0.1807**, Adj R² = **0.1620**, F-statistic = **9.66** (p = **1.40e-19**), Residual SE = **0.971** on **613** df, AIC = **1760.5**, BIC = **1827.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.2610** | 0.4208 | ±0.8417 | **+7.749** | **9.27e-15** | *** |
| **Education: graduate level (vs college)** | **-0.2091** | 0.0794 | ±0.1588 | **-2.633** | **0.0085** | ** |
| **Education: high school or below (vs college)** | **+0.5851** | 0.1938 | ±0.3877 | **+3.019** | **0.0025** | ** |
| Site: UCSD (vs UAB) | +0.1080 | 0.1045 | ±0.2090 | +1.034 | 0.3012 |  |
| **Site: UW (vs UAB)** | **-0.3954** | 0.0950 | ±0.1900 | **-4.163** | **3.14e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3796** | 0.1039 | ±0.2078 | **-3.653** | **2.59e-04** | *** |
| Season: summer (vs autumn) | -0.0961 | 0.1201 | ±0.2401 | -0.800 | 0.4235 |  |
| Season: winter (vs autumn) | -0.0502 | 0.1209 | ±0.2418 | -0.415 | 0.6782 |  |
| **Age (years)** | **-0.0192** | 0.0040 | ±0.0079 | **-4.826** | **1.39e-06** | *** |
| BMI (kg/m2) | +0.0076 | 0.0064 | ±0.0128 | +1.185 | 0.2360 |  |
| Hypertension | +0.1591 | 0.0896 | ±0.1793 | +1.774 | 0.0760 | . |
| High cholesterol | -0.0256 | 0.0841 | ±0.1682 | -0.304 | 0.7610 |  |
| Kidney disease | -0.0396 | 0.1386 | ±0.2773 | -0.285 | 0.7753 |  |
| Circulatory disease | -0.0079 | 0.1182 | ±0.2364 | -0.067 | 0.9468 |  |
| Mean / SD ratio | -0.0341 | 0.0315 | ±0.0630 | -1.082 | 0.2793 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **628**, R² = **0.1813**, Adj R² = **0.1626**, F-statistic = **9.70** (p = **1.12e-19**), Residual SE = **0.971** on **613** df, AIC = **1760.0**, BIC = **1826.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.3014** | 0.4174 | ±0.8349 | **+7.909** | **2.60e-15** | *** |
| **Education: graduate level (vs college)** | **-0.2079** | 0.0794 | ±0.1589 | **-2.617** | **0.0089** | ** |
| **Education: high school or below (vs college)** | **+0.5785** | 0.1944 | ±0.3888 | **+2.976** | **0.0029** | ** |
| Site: UCSD (vs UAB) | +0.1038 | 0.1050 | ±0.2099 | +0.989 | 0.3226 |  |
| **Site: UW (vs UAB)** | **-0.3964** | 0.0950 | ±0.1900 | **-4.172** | **3.02e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3810** | 0.1038 | ±0.2076 | **-3.670** | **2.43e-04** | *** |
| Season: summer (vs autumn) | -0.0924 | 0.1198 | ±0.2396 | -0.771 | 0.4408 |  |
| Season: winter (vs autumn) | -0.0495 | 0.1209 | ±0.2417 | -0.409 | 0.6824 |  |
| **Age (years)** | **-0.0194** | 0.0040 | ±0.0079 | **-4.892** | **1.00e-06** | *** |
| BMI (kg/m2) | +0.0075 | 0.0064 | ±0.0128 | +1.178 | 0.2387 |  |
| Hypertension | +0.1604 | 0.0898 | ±0.1797 | +1.785 | 0.0743 | . |
| High cholesterol | -0.0266 | 0.0838 | ±0.1677 | -0.317 | 0.7509 |  |
| Kidney disease | -0.0419 | 0.1384 | ±0.2769 | -0.303 | 0.7621 |  |
| Circulatory disease | -0.0061 | 0.1182 | ±0.2363 | -0.052 | 0.9587 |  |
| Avg. daily mean/SD | -0.0332 | 0.0252 | ±0.0504 | -1.318 | 0.1874 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **628**, R² = **0.1792**, Adj R² = **0.1604**, F-statistic = **9.56** (p = **2.34e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.6**, BIC = **1828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0019** | 0.3777 | ±0.7554 | **+7.948** | **1.90e-15** | *** |
| **Education: graduate level (vs college)** | **-0.2100** | 0.0795 | ±0.1590 | **-2.643** | **0.0082** | ** |
| **Education: high school or below (vs college)** | **+0.6010** | 0.1934 | ±0.3867 | **+3.108** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.1102 | 0.1047 | ±0.2094 | +1.053 | 0.2924 |  |
| **Site: UW (vs UAB)** | **-0.3993** | 0.0957 | ±0.1914 | **-4.173** | **3.00e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3811** | 0.1038 | ±0.2076 | **-3.672** | **2.41e-04** | *** |
| Season: summer (vs autumn) | -0.0954 | 0.1203 | ±0.2406 | -0.793 | 0.4279 |  |
| Season: winter (vs autumn) | -0.0525 | 0.1207 | ±0.2414 | -0.435 | 0.6638 |  |
| **Age (years)** | **-0.0184** | 0.0038 | ±0.0075 | **-4.869** | **1.12e-06** | *** |
| BMI (kg/m2) | +0.0076 | 0.0064 | ±0.0128 | +1.185 | 0.2361 |  |
| Hypertension | +0.1653 | 0.0902 | ±0.1804 | +1.832 | 0.0670 | . |
| High cholesterol | -0.0274 | 0.0838 | ±0.1676 | -0.326 | 0.7441 |  |
| Kidney disease | -0.0155 | 0.1406 | ±0.2812 | -0.110 | 0.9123 |  |
| Circulatory disease | -0.0074 | 0.1179 | ±0.2358 | -0.062 | 0.9502 |  |
| MAG (mg/dL/h) | +0.0008 | 0.0039 | ±0.0077 | +0.202 | 0.8401 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **628**, R² = **0.1792**, Adj R² = **0.1604**, F-statistic = **9.56** (p = **2.32e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.6**, BIC = **1828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0130** | 0.3629 | ±0.7258 | **+8.302** | **1.02e-16** | *** |
| **Education: graduate level (vs college)** | **-0.2095** | 0.0794 | ±0.1588 | **-2.639** | **0.0083** | ** |
| **Education: high school or below (vs college)** | **+0.5988** | 0.1963 | ±0.3926 | **+3.051** | **0.0023** | ** |
| Site: UCSD (vs UAB) | +0.1107 | 0.1045 | ±0.2090 | +1.059 | 0.2895 |  |
| **Site: UW (vs UAB)** | **-0.4001** | 0.0950 | ±0.1899 | **-4.213** | **2.52e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3814** | 0.1038 | ±0.2077 | **-3.672** | **2.40e-04** | *** |
| Season: summer (vs autumn) | -0.0953 | 0.1205 | ±0.2410 | -0.791 | 0.4288 |  |
| Season: winter (vs autumn) | -0.0522 | 0.1211 | ±0.2423 | -0.431 | 0.6666 |  |
| **Age (years)** | **-0.0185** | 0.0038 | ±0.0077 | **-4.818** | **1.45e-06** | *** |
| BMI (kg/m2) | +0.0077 | 0.0065 | ±0.0129 | +1.192 | 0.2332 |  |
| Hypertension | +0.1643 | 0.0912 | ±0.1824 | +1.801 | 0.0716 | . |
| High cholesterol | -0.0280 | 0.0837 | ±0.1675 | -0.334 | 0.7381 |  |
| Kidney disease | -0.0207 | 0.1365 | ±0.2730 | -0.151 | 0.8796 |  |
| Circulatory disease | -0.0074 | 0.1179 | ±0.2357 | -0.063 | 0.9497 |  |
| Avg. daily range (mg/dL) | +0.0002 | 0.0011 | ±0.0021 | +0.215 | 0.8299 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **628**, R² = **0.1808**, Adj R² = **0.1621**, F-statistic = **9.67** (p = **1.32e-19**), Residual SE = **0.971** on **613** df, AIC = **1760.3**, BIC = **1827.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9948** | 0.3490 | ±0.6980 | **+8.581** | **9.43e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2079** | 0.0792 | ±0.1584 | **-2.626** | **0.0087** | ** |
| **Education: high school or below (vs college)** | **+0.5971** | 0.1911 | ±0.3821 | **+3.125** | **0.0018** | ** |
| Site: UCSD (vs UAB) | +0.1132 | 0.1041 | ±0.2081 | +1.087 | 0.2768 |  |
| **Site: UW (vs UAB)** | **-0.3940** | 0.0947 | ±0.1893 | **-4.162** | **3.16e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3798** | 0.1037 | ±0.2073 | **-3.664** | **2.49e-04** | *** |
| Season: summer (vs autumn) | -0.0966 | 0.1203 | ±0.2405 | -0.804 | 0.4216 |  |
| Season: winter (vs autumn) | -0.0530 | 0.1206 | ±0.2412 | -0.439 | 0.6603 |  |
| **Age (years)** | **-0.0186** | 0.0038 | ±0.0076 | **-4.901** | **9.52e-07** | *** |
| BMI (kg/m2) | +0.0075 | 0.0064 | ±0.0128 | +1.176 | 0.2396 |  |
| Hypertension | +0.1548 | 0.0908 | ±0.1817 | +1.704 | 0.0884 | . |
| High cholesterol | -0.0285 | 0.0837 | ±0.1673 | -0.341 | 0.7330 |  |
| Kidney disease | -0.0342 | 0.1376 | ±0.2752 | -0.248 | 0.8040 |  |
| Circulatory disease | -0.0118 | 0.1185 | ±0.2370 | -0.099 | 0.9208 |  |
| SD of daily means (mg/dL) | +0.0065 | 0.0059 | ±0.0118 | +1.098 | 0.2722 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **628**, R² = **0.1810**, Adj R² = **0.1623**, F-statistic = **9.68** (p = **1.26e-19**), Residual SE = **0.971** on **613** df, AIC = **1760.2**, BIC = **1826.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.3890** | 0.4710 | ±0.9419 | **+7.196** | **6.21e-13** | *** |
| **Education: graduate level (vs college)** | **-0.2049** | 0.0790 | ±0.1580 | **-2.594** | **0.0095** | ** |
| **Education: high school or below (vs college)** | **+0.5885** | 0.1926 | ±0.3851 | **+3.056** | **0.0022** | ** |
| Site: UCSD (vs UAB) | +0.1145 | 0.1042 | ±0.2083 | +1.099 | 0.2718 |  |
| **Site: UW (vs UAB)** | **-0.3907** | 0.0950 | ±0.1900 | **-4.113** | **3.91e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3822** | 0.1039 | ±0.2079 | **-3.677** | **2.36e-04** | *** |
| Season: summer (vs autumn) | -0.0913 | 0.1201 | ±0.2402 | -0.760 | 0.4471 |  |
| Season: winter (vs autumn) | -0.0531 | 0.1206 | ±0.2413 | -0.440 | 0.6599 |  |
| **Age (years)** | **-0.0186** | 0.0038 | ±0.0076 | **-4.910** | **9.09e-07** | *** |
| BMI (kg/m2) | +0.0075 | 0.0064 | ±0.0128 | +1.178 | 0.2387 |  |
| Hypertension | +0.1562 | 0.0911 | ±0.1822 | +1.715 | 0.0863 | . |
| High cholesterol | -0.0314 | 0.0834 | ±0.1668 | -0.377 | 0.7064 |  |
| Kidney disease | -0.0399 | 0.1369 | ±0.2737 | -0.291 | 0.7707 |  |
| Circulatory disease | -0.0094 | 0.1182 | ±0.2365 | -0.080 | 0.9364 |  |
| Time in range 70-180, pooled (%) | -0.0037 | 0.0031 | ±0.0063 | -1.177 | 0.2394 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **628**, R² = **0.1812**, Adj R² = **0.1625**, F-statistic = **9.69** (p = **1.18e-19**), Residual SE = **0.971** on **613** df, AIC = **1760.1**, BIC = **1826.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.4078** | 0.4750 | ±0.9500 | **+7.174** | **7.28e-13** | *** |
| **Education: graduate level (vs college)** | **-0.2044** | 0.0789 | ±0.1579 | **-2.589** | **0.0096** | ** |
| **Education: high school or below (vs college)** | **+0.5871** | 0.1925 | ±0.3849 | **+3.051** | **0.0023** | ** |
| Site: UCSD (vs UAB) | +0.1145 | 0.1042 | ±0.2083 | +1.099 | 0.2717 |  |
| **Site: UW (vs UAB)** | **-0.3899** | 0.0950 | ±0.1900 | **-4.105** | **4.04e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3828** | 0.1039 | ±0.2079 | **-3.683** | **2.31e-04** | *** |
| Season: summer (vs autumn) | -0.0912 | 0.1200 | ±0.2401 | -0.760 | 0.4474 |  |
| Season: winter (vs autumn) | -0.0538 | 0.1206 | ±0.2412 | -0.446 | 0.6557 |  |
| **Age (years)** | **-0.0186** | 0.0038 | ±0.0076 | **-4.916** | **8.83e-07** | *** |
| BMI (kg/m2) | +0.0075 | 0.0064 | ±0.0128 | +1.177 | 0.2391 |  |
| Hypertension | +0.1561 | 0.0909 | ±0.1819 | +1.717 | 0.0860 | . |
| High cholesterol | -0.0319 | 0.0834 | ±0.1668 | -0.383 | 0.7017 |  |
| Kidney disease | -0.0418 | 0.1362 | ±0.2724 | -0.307 | 0.7591 |  |
| Circulatory disease | -0.0094 | 0.1182 | ±0.2364 | -0.080 | 0.9365 |  |
| Avg. daily time in range 70-180 (%) | -0.0038 | 0.0031 | ±0.0062 | -1.230 | 0.2187 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **628**, R² = **0.1803**, Adj R² = **0.1616**, F-statistic = **9.63** (p = **1.58e-19**), Residual SE = **0.972** on **613** df, AIC = **1760.7**, BIC = **1827.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0023** | 0.3530 | ±0.7060 | **+8.505** | **1.82e-17** | *** |
| **Education: graduate level (vs college)** | **-0.2090** | 0.0793 | ±0.1587 | **-2.634** | **0.0084** | ** |
| **Education: high school or below (vs college)** | **+0.6111** | 0.1911 | ±0.3822 | **+3.197** | **0.0014** | ** |
| Site: UCSD (vs UAB) | +0.1257 | 0.1049 | ±0.2099 | +1.198 | 0.2309 |  |
| **Site: UW (vs UAB)** | **-0.3895** | 0.0960 | ±0.1921 | **-4.056** | **5.00e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3781** | 0.1037 | ±0.2075 | **-3.645** | **2.67e-04** | *** |
| Season: summer (vs autumn) | -0.1001 | 0.1203 | ±0.2407 | -0.832 | 0.4055 |  |
| Season: winter (vs autumn) | -0.0554 | 0.1207 | ±0.2414 | -0.459 | 0.6461 |  |
| **Age (years)** | **-0.0184** | 0.0038 | ±0.0075 | **-4.875** | **1.09e-06** | *** |
| BMI (kg/m2) | +0.0077 | 0.0064 | ±0.0129 | +1.204 | 0.2286 |  |
| Hypertension | +0.1702 | 0.0902 | ±0.1804 | +1.888 | 0.0591 | . |
| High cholesterol | -0.0228 | 0.0846 | ±0.1692 | -0.269 | 0.7877 |  |
| Kidney disease | -0.0163 | 0.1399 | ±0.2797 | -0.117 | 0.9070 |  |
| Circulatory disease | -0.0083 | 0.1176 | ±0.2353 | -0.070 | 0.9438 |  |
| Time < 54 (%) | +0.0429 | 0.0644 | ±0.1289 | +0.665 | 0.5060 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **628**, R² = **0.1827**, Adj R² = **0.1641**, F-statistic = **9.79** (p = **6.93e-20**), Residual SE = **0.970** on **613** df, AIC = **1758.9**, BIC = **1825.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0050** | 0.3490 | ±0.6981 | **+8.609** | **7.34e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2040** | 0.0790 | ±0.1580 | **-2.582** | **0.0098** | ** |
| **Education: high school or below (vs college)** | **+0.6163** | 0.1911 | ±0.3822 | **+3.225** | **0.0013** | ** |
| Site: UCSD (vs UAB) | +0.1328 | 0.1042 | ±0.2085 | +1.274 | 0.2027 |  |
| **Site: UW (vs UAB)** | **-0.3783** | 0.0962 | ±0.1925 | **-3.931** | **8.46e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3752** | 0.1038 | ±0.2076 | **-3.614** | **3.01e-04** | *** |
| Season: summer (vs autumn) | -0.1022 | 0.1202 | ±0.2405 | -0.850 | 0.3954 |  |
| Season: winter (vs autumn) | -0.0593 | 0.1205 | ±0.2409 | -0.492 | 0.6225 |  |
| **Age (years)** | **-0.0187** | 0.0038 | ±0.0076 | **-4.932** | **8.16e-07** | *** |
| BMI (kg/m2) | +0.0077 | 0.0064 | ±0.0128 | +1.206 | 0.2278 |  |
| Hypertension | +0.1739 | 0.0906 | ±0.1813 | +1.919 | 0.0550 | . |
| High cholesterol | -0.0191 | 0.0843 | ±0.1686 | -0.227 | 0.8207 |  |
| Kidney disease | -0.0210 | 0.1394 | ±0.2789 | -0.150 | 0.8804 |  |
| Circulatory disease | -0.0097 | 0.1171 | ±0.2342 | -0.083 | 0.9341 |  |
| Avg. daily time < 54 (%) | +0.0864 | 0.0804 | ±0.1608 | +1.074 | 0.2826 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **628**, R² = **0.1853**, Adj R² = **0.1667**, F-statistic = **9.96** (p = **2.90e-20**), Residual SE = **0.969** on **613** df, AIC = **1756.9**, BIC = **1823.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9801** | 0.3488 | ±0.6976 | **+8.544** | **1.29e-17** | *** |
| **Education: graduate level (vs college)** | **-0.1986** | 0.0789 | ±0.1579 | **-2.516** | **0.0119** | * |
| **Education: high school or below (vs college)** | **+0.6061** | 0.1910 | ±0.3821 | **+3.172** | **0.0015** | ** |
| Site: UCSD (vs UAB) | +0.1276 | 0.1042 | ±0.2084 | +1.225 | 0.2207 |  |
| **Site: UW (vs UAB)** | **-0.3821** | 0.0960 | ±0.1921 | **-3.978** | **6.94e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3745** | 0.1031 | ±0.2062 | **-3.632** | **2.81e-04** | *** |
| Season: summer (vs autumn) | -0.0965 | 0.1194 | ±0.2387 | -0.809 | 0.4187 |  |
| Season: winter (vs autumn) | -0.0610 | 0.1204 | ±0.2408 | -0.507 | 0.6122 |  |
| **Age (years)** | **-0.0187** | 0.0038 | ±0.0076 | **-4.958** | **7.12e-07** | *** |
| BMI (kg/m2) | +0.0075 | 0.0064 | ±0.0128 | +1.182 | 0.2373 |  |
| **Hypertension** | **+0.1777** | 0.0906 | ±0.1812 | **+1.962** | **0.0498** | * |
| High cholesterol | -0.0240 | 0.0835 | ±0.1670 | -0.287 | 0.7739 |  |
| Kidney disease | -0.0247 | 0.1394 | ±0.2787 | -0.177 | 0.8595 |  |
| Circulatory disease | -0.0032 | 0.1170 | ±0.2339 | -0.028 | 0.9779 |  |
| Time 54-69, pooled (%) | +0.0369 | 0.0227 | ±0.0454 | +1.629 | 0.1034 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **628**, R² = **0.1863**, Adj R² = **0.1677**, F-statistic = **10.03** (p = **2.01e-20**), Residual SE = **0.968** on **613** df, AIC = **1756.1**, BIC = **1822.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9964** | 0.3474 | ±0.6948 | **+8.626** | **6.36e-18** | *** |
| **Education: graduate level (vs college)** | **-0.1959** | 0.0789 | ±0.1577 | **-2.484** | **0.0130** | * |
| **Education: high school or below (vs college)** | **+0.6053** | 0.1909 | ±0.3819 | **+3.170** | **0.0015** | ** |
| Site: UCSD (vs UAB) | +0.1259 | 0.1041 | ±0.2082 | +1.210 | 0.2264 |  |
| **Site: UW (vs UAB)** | **-0.3789** | 0.0962 | ±0.1924 | **-3.938** | **8.22e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3750** | 0.1030 | ±0.2061 | **-3.639** | **2.73e-04** | *** |
| Season: summer (vs autumn) | -0.0956 | 0.1191 | ±0.2382 | -0.803 | 0.4220 |  |
| Season: winter (vs autumn) | -0.0630 | 0.1203 | ±0.2406 | -0.524 | 0.6003 |  |
| **Age (years)** | **-0.0189** | 0.0038 | ±0.0076 | **-5.003** | **5.66e-07** | *** |
| BMI (kg/m2) | +0.0075 | 0.0064 | ±0.0128 | +1.172 | 0.2414 |  |
| **Hypertension** | **+0.1784** | 0.0906 | ±0.1813 | **+1.968** | **0.0490** | * |
| High cholesterol | -0.0240 | 0.0834 | ±0.1668 | -0.287 | 0.7738 |  |
| Kidney disease | -0.0245 | 0.1388 | ±0.2776 | -0.177 | 0.8596 |  |
| Circulatory disease | -0.0027 | 0.1168 | ±0.2336 | -0.023 | 0.9817 |  |
| Avg. daily time 54-69 (%) | +0.0386 | 0.0225 | ±0.0450 | +1.717 | 0.0860 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **628**, R² = **0.1846**, Adj R² = **0.1660**, F-statistic = **9.92** (p = **3.60e-20**), Residual SE = **0.969** on **613** df, AIC = **1757.4**, BIC = **1824.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9720** | 0.3502 | ±0.7004 | **+8.487** | **2.13e-17** | *** |
| **Education: graduate level (vs college)** | **-0.2004** | 0.0789 | ±0.1579 | **-2.539** | **0.0111** | * |
| **Education: high school or below (vs college)** | **+0.6104** | 0.1914 | ±0.3827 | **+3.190** | **0.0014** | ** |
| Site: UCSD (vs UAB) | +0.1336 | 0.1045 | ±0.2091 | +1.278 | 0.2013 |  |
| **Site: UW (vs UAB)** | **-0.3787** | 0.0965 | ±0.1929 | **-3.925** | **8.66e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3740** | 0.1032 | ±0.2064 | **-3.624** | **2.90e-04** | *** |
| Season: summer (vs autumn) | -0.0991 | 0.1197 | ±0.2394 | -0.828 | 0.4076 |  |
| Season: winter (vs autumn) | -0.0607 | 0.1204 | ±0.2408 | -0.504 | 0.6141 |  |
| **Age (years)** | **-0.0187** | 0.0038 | ±0.0076 | **-4.942** | **7.73e-07** | *** |
| BMI (kg/m2) | +0.0076 | 0.0064 | ±0.0128 | +1.195 | 0.2321 |  |
| Hypertension | +0.1777 | 0.0907 | ±0.1814 | +1.960 | 0.0500 | . |
| High cholesterol | -0.0215 | 0.0837 | ±0.1674 | -0.257 | 0.7974 |  |
| Kidney disease | -0.0234 | 0.1393 | ±0.2785 | -0.168 | 0.8665 |  |
| Circulatory disease | -0.0047 | 0.1169 | ±0.2339 | -0.040 | 0.9678 |  |
| Time < 70 (%) | +0.0284 | 0.0184 | ±0.0368 | +1.544 | 0.1226 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **628**, R² = **0.1865**, Adj R² = **0.1679**, F-statistic = **10.04** (p = **1.89e-20**), Residual SE = **0.968** on **613** df, AIC = **1756.0**, BIC = **1822.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9919** | 0.3476 | ±0.6951 | **+8.608** | **7.43e-18** | *** |
| **Education: graduate level (vs college)** | **-0.1959** | 0.0788 | ±0.1576 | **-2.485** | **0.0129** | * |
| **Education: high school or below (vs college)** | **+0.6097** | 0.1911 | ±0.3823 | **+3.190** | **0.0014** | ** |
| Site: UCSD (vs UAB) | +0.1317 | 0.1041 | ±0.2083 | +1.264 | 0.2061 |  |
| **Site: UW (vs UAB)** | **-0.3739** | 0.0965 | ±0.1930 | **-3.874** | **1.07e-04** | *** |
| **Season: spring (vs autumn)** | **-0.3737** | 0.1031 | ±0.2062 | **-3.625** | **2.89e-04** | *** |
| Season: summer (vs autumn) | -0.0980 | 0.1193 | ±0.2387 | -0.821 | 0.4115 |  |
| Season: winter (vs autumn) | -0.0637 | 0.1203 | ±0.2405 | -0.530 | 0.5961 |  |
| **Age (years)** | **-0.0190** | 0.0038 | ±0.0076 | **-5.003** | **5.65e-07** | *** |
| BMI (kg/m2) | +0.0075 | 0.0064 | ±0.0127 | +1.182 | 0.2372 |  |
| **Hypertension** | **+0.1793** | 0.0908 | ±0.1816 | **+1.975** | **0.0483** | * |
| High cholesterol | -0.0213 | 0.0835 | ±0.1670 | -0.255 | 0.7985 |  |
| Kidney disease | -0.0253 | 0.1387 | ±0.2773 | -0.182 | 0.8554 |  |
| Circulatory disease | -0.0043 | 0.1167 | ±0.2334 | -0.037 | 0.9708 |  |
| Avg. daily time < 70 (%) | +0.0323 | 0.0188 | ±0.0376 | +1.718 | 0.0858 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **628**, R² = **0.1794**, Adj R² = **0.1606**, F-statistic = **9.57** (p = **2.18e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.5**, BIC = **1828.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.3236** | 0.5826 | ±1.1653 | **+5.704** | **1.17e-08** | *** |
| **Education: graduate level (vs college)** | **-0.2085** | 0.0792 | ±0.1585 | **-2.631** | **0.0085** | ** |
| **Education: high school or below (vs college)** | **+0.5987** | 0.1929 | ±0.3857 | **+3.104** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.1127 | 0.1042 | ±0.2084 | +1.082 | 0.2794 |  |
| **Site: UW (vs UAB)** | **-0.3975** | 0.0954 | ±0.1908 | **-4.167** | **3.08e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3822** | 0.1039 | ±0.2077 | **-3.680** | **2.33e-04** | *** |
| Season: summer (vs autumn) | -0.0935 | 0.1205 | ±0.2410 | -0.776 | 0.4379 |  |
| Season: winter (vs autumn) | -0.0534 | 0.1207 | ±0.2413 | -0.442 | 0.6583 |  |
| **Age (years)** | **-0.0183** | 0.0038 | ±0.0075 | **-4.868** | **1.13e-06** | *** |
| BMI (kg/m2) | +0.0077 | 0.0064 | ±0.0129 | +1.194 | 0.2324 |  |
| Hypertension | +0.1635 | 0.0903 | ±0.1807 | +1.810 | 0.0703 | . |
| High cholesterol | -0.0267 | 0.0839 | ±0.1678 | -0.318 | 0.7505 |  |
| Kidney disease | -0.0191 | 0.1391 | ±0.2781 | -0.137 | 0.8906 |  |
| Circulatory disease | -0.0089 | 0.1183 | ±0.2365 | -0.075 | 0.9401 |  |
| Time 54-250, pooled (%) | -0.0030 | 0.0052 | ±0.0104 | -0.573 | 0.5663 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **628**, R² = **0.1797**, Adj R² = **0.1610**, F-statistic = **9.59** (p = **1.92e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.2**, BIC = **1827.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.5426** | 0.6814 | ±1.3629 | **+5.199** | **2.01e-07** | *** |
| **Education: graduate level (vs college)** | **-0.2070** | 0.0792 | ±0.1584 | **-2.613** | **0.0090** | ** |
| **Education: high school or below (vs college)** | **+0.5945** | 0.1933 | ±0.3866 | **+3.076** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.1132 | 0.1042 | ±0.2084 | +1.086 | 0.2774 |  |
| **Site: UW (vs UAB)** | **-0.3955** | 0.0953 | ±0.1906 | **-4.149** | **3.33e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3838** | 0.1039 | ±0.2078 | **-3.694** | **2.21e-04** | *** |
| Season: summer (vs autumn) | -0.0926 | 0.1204 | ±0.2408 | -0.769 | 0.4419 |  |
| Season: winter (vs autumn) | -0.0545 | 0.1206 | ±0.2413 | -0.452 | 0.6515 |  |
| **Age (years)** | **-0.0184** | 0.0038 | ±0.0075 | **-4.877** | **1.08e-06** | *** |
| BMI (kg/m2) | +0.0077 | 0.0064 | ±0.0129 | +1.200 | 0.2301 |  |
| Hypertension | +0.1619 | 0.0903 | ±0.1807 | +1.793 | 0.0730 | . |
| High cholesterol | -0.0262 | 0.0839 | ±0.1678 | -0.312 | 0.7549 |  |
| Kidney disease | -0.0231 | 0.1384 | ±0.2767 | -0.167 | 0.8673 |  |
| Circulatory disease | -0.0102 | 0.1185 | ±0.2369 | -0.086 | 0.9317 |  |
| Avg. daily time 54-250 (%) | -0.0052 | 0.0062 | ±0.0125 | -0.832 | 0.4056 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **628**, R² = **0.1801**, Adj R² = **0.1614**, F-statistic = **9.62** (p = **1.69e-19**), Residual SE = **0.972** on **613** df, AIC = **1760.9**, BIC = **1827.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0350** | 0.3480 | ±0.6960 | **+8.721** | **2.75e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2084** | 0.0792 | ±0.1585 | **-2.630** | **0.0085** | ** |
| **Education: high school or below (vs college)** | **+0.5941** | 0.1923 | ±0.3847 | **+3.089** | **0.0020** | ** |
| Site: UCSD (vs UAB) | +0.1106 | 0.1045 | ±0.2089 | +1.059 | 0.2898 |  |
| **Site: UW (vs UAB)** | **-0.3973** | 0.0949 | ±0.1898 | **-4.186** | **2.83e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3817** | 0.1039 | ±0.2079 | **-3.673** | **2.40e-04** | *** |
| Season: summer (vs autumn) | -0.0943 | 0.1203 | ±0.2407 | -0.784 | 0.4331 |  |
| Season: winter (vs autumn) | -0.0519 | 0.1208 | ±0.2417 | -0.430 | 0.6674 |  |
| **Age (years)** | **-0.0185** | 0.0038 | ±0.0076 | **-4.873** | **1.10e-06** | *** |
| BMI (kg/m2) | +0.0075 | 0.0064 | ±0.0129 | +1.170 | 0.2419 |  |
| Hypertension | +0.1580 | 0.0920 | ±0.1839 | +1.718 | 0.0858 | . |
| High cholesterol | -0.0336 | 0.0831 | ±0.1662 | -0.404 | 0.6860 |  |
| Kidney disease | -0.0344 | 0.1374 | ±0.2747 | -0.251 | 0.8022 |  |
| Circulatory disease | -0.0083 | 0.1182 | ±0.2364 | -0.070 | 0.9443 |  |
| Time 181-250, pooled (%) | +0.0039 | 0.0051 | ±0.0102 | +0.758 | 0.4483 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **628**, R² = **0.1799**, Adj R² = **0.1611**, F-statistic = **9.60** (p = **1.84e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.1**, BIC = **1827.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0332** | 0.3481 | ±0.6961 | **+8.715** | **2.91e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2087** | 0.0792 | ±0.1584 | **-2.634** | **0.0084** | ** |
| **Education: high school or below (vs college)** | **+0.5955** | 0.1923 | ±0.3847 | **+3.096** | **0.0020** | ** |
| Site: UCSD (vs UAB) | +0.1113 | 0.1044 | ±0.2087 | +1.066 | 0.2863 |  |
| **Site: UW (vs UAB)** | **-0.3973** | 0.0948 | ±0.1897 | **-4.190** | **2.79e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3815** | 0.1039 | ±0.2078 | **-3.671** | **2.42e-04** | *** |
| Season: summer (vs autumn) | -0.0941 | 0.1203 | ±0.2406 | -0.782 | 0.4339 |  |
| Season: winter (vs autumn) | -0.0520 | 0.1208 | ±0.2417 | -0.430 | 0.6671 |  |
| **Age (years)** | **-0.0185** | 0.0038 | ±0.0076 | **-4.869** | **1.12e-06** | *** |
| BMI (kg/m2) | +0.0075 | 0.0064 | ±0.0129 | +1.172 | 0.2412 |  |
| Hypertension | +0.1593 | 0.0918 | ±0.1837 | +1.734 | 0.0829 | . |
| High cholesterol | -0.0327 | 0.0832 | ±0.1663 | -0.393 | 0.6940 |  |
| Kidney disease | -0.0315 | 0.1370 | ±0.2741 | -0.230 | 0.8183 |  |
| Circulatory disease | -0.0079 | 0.1181 | ±0.2362 | -0.067 | 0.9465 |  |
| Avg. daily time 181-250 (%) | +0.0032 | 0.0049 | ±0.0097 | +0.666 | 0.5051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **628**, R² = **0.1798**, Adj R² = **0.1611**, F-statistic = **9.60** (p = **1.86e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.1**, BIC = **1827.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0304** | 0.3478 | ±0.6956 | **+8.713** | **2.97e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2078** | 0.0792 | ±0.1584 | **-2.624** | **0.0087** | ** |
| **Education: high school or below (vs college)** | **+0.5938** | 0.1929 | ±0.3859 | **+3.078** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.1113 | 0.1043 | ±0.2086 | +1.067 | 0.2860 |  |
| **Site: UW (vs UAB)** | **-0.3966** | 0.0949 | ±0.1899 | **-4.178** | **2.94e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3824** | 0.1039 | ±0.2078 | **-3.680** | **2.33e-04** | *** |
| Season: summer (vs autumn) | -0.0929 | 0.1204 | ±0.2407 | -0.772 | 0.4404 |  |
| Season: winter (vs autumn) | -0.0525 | 0.1208 | ±0.2415 | -0.435 | 0.6638 |  |
| **Age (years)** | **-0.0185** | 0.0038 | ±0.0076 | **-4.881** | **1.05e-06** | *** |
| BMI (kg/m2) | +0.0076 | 0.0064 | ±0.0128 | +1.182 | 0.2371 |  |
| Hypertension | +0.1591 | 0.0918 | ±0.1835 | +1.734 | 0.0829 | . |
| High cholesterol | -0.0306 | 0.0834 | ±0.1668 | -0.367 | 0.7139 |  |
| Kidney disease | -0.0296 | 0.1371 | ±0.2743 | -0.216 | 0.8293 |  |
| Circulatory disease | -0.0089 | 0.1183 | ±0.2367 | -0.076 | 0.9398 |  |
| Time > 180 (%) | +0.0023 | 0.0031 | ±0.0062 | +0.732 | 0.4641 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **628**, R² = **0.1798**, Adj R² = **0.1611**, F-statistic = **9.60** (p = **1.88e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.1**, BIC = **1827.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0303** | 0.3478 | ±0.6957 | **+8.712** | **2.99e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2079** | 0.0792 | ±0.1583 | **-2.626** | **0.0086** | ** |
| **Education: high school or below (vs college)** | **+0.5937** | 0.1930 | ±0.3860 | **+3.076** | **0.0021** | ** |
| Site: UCSD (vs UAB) | +0.1116 | 0.1043 | ±0.2086 | +1.070 | 0.2848 |  |
| **Site: UW (vs UAB)** | **-0.3967** | 0.0949 | ±0.1898 | **-4.179** | **2.92e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3827** | 0.1039 | ±0.2078 | **-3.682** | **2.31e-04** | *** |
| Season: summer (vs autumn) | -0.0931 | 0.1203 | ±0.2406 | -0.774 | 0.4391 |  |
| Season: winter (vs autumn) | -0.0528 | 0.1207 | ±0.2415 | -0.437 | 0.6621 |  |
| **Age (years)** | **-0.0185** | 0.0038 | ±0.0076 | **-4.880** | **1.06e-06** | *** |
| BMI (kg/m2) | +0.0076 | 0.0064 | ±0.0128 | +1.183 | 0.2368 |  |
| Hypertension | +0.1594 | 0.0917 | ±0.1834 | +1.739 | 0.0821 | . |
| High cholesterol | -0.0307 | 0.0834 | ±0.1668 | -0.368 | 0.7128 |  |
| Kidney disease | -0.0297 | 0.1366 | ±0.2733 | -0.217 | 0.8279 |  |
| Circulatory disease | -0.0089 | 0.1183 | ±0.2367 | -0.075 | 0.9402 |  |
| Avg. daily time > 180 (%) | +0.0022 | 0.0031 | ±0.0062 | +0.717 | 0.4733 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **628**, R² = **0.1810**, Adj R² = **0.1623**, F-statistic = **9.67** (p = **1.27e-19**), Residual SE = **0.971** on **613** df, AIC = **1760.2**, BIC = **1826.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0289** | 0.3467 | ±0.6933 | **+8.737** | **2.39e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2051** | 0.0790 | ±0.1579 | **-2.597** | **0.0094** | ** |
| **Education: high school or below (vs college)** | **+0.5924** | 0.1916 | ±0.3832 | **+3.092** | **0.0020** | ** |
| Site: UCSD (vs UAB) | +0.1134 | 0.1042 | ±0.2083 | +1.089 | 0.2762 |  |
| **Site: UW (vs UAB)** | **-0.3947** | 0.0949 | ±0.1898 | **-4.160** | **3.19e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3835** | 0.1040 | ±0.2081 | **-3.686** | **2.27e-04** | *** |
| Season: summer (vs autumn) | -0.0869 | 0.1202 | ±0.2404 | -0.723 | 0.4697 |  |
| Season: winter (vs autumn) | -0.0542 | 0.1206 | ±0.2413 | -0.450 | 0.6530 |  |
| **Age (years)** | **-0.0184** | 0.0038 | ±0.0075 | **-4.881** | **1.06e-06** | *** |
| BMI (kg/m2) | +0.0074 | 0.0064 | ±0.0128 | +1.154 | 0.2483 |  |
| Hypertension | +0.1548 | 0.0915 | ±0.1831 | +1.691 | 0.0908 | . |
| High cholesterol | -0.0322 | 0.0834 | ±0.1667 | -0.386 | 0.6995 |  |
| Kidney disease | -0.0237 | 0.1373 | ±0.2746 | -0.173 | 0.8630 |  |
| Circulatory disease | -0.0108 | 0.1186 | ±0.2372 | -0.091 | 0.9276 |  |
| Nocturnal time > 180 (%) | +0.0038 | 0.0036 | ±0.0072 | +1.059 | 0.2896 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **628**, R² = **0.1792**, Adj R² = **0.1605**, F-statistic = **9.56** (p = **2.29e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.6**, BIC = **1828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0356** | 0.3498 | ±0.6996 | **+8.678** | **4.03e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2118** | 0.0795 | ±0.1590 | **-2.665** | **0.0077** | ** |
| **Education: high school or below (vs college)** | **+0.6066** | 0.1921 | ±0.3842 | **+3.158** | **0.0016** | ** |
| Site: UCSD (vs UAB) | +0.1119 | 0.1045 | ±0.2091 | +1.070 | 0.2845 |  |
| **Site: UW (vs UAB)** | **-0.4023** | 0.0951 | ±0.1902 | **-4.230** | **2.34e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3822** | 0.1041 | ±0.2081 | **-3.673** | **2.39e-04** | *** |
| Season: summer (vs autumn) | -0.0967 | 0.1206 | ±0.2411 | -0.802 | 0.4225 |  |
| Season: winter (vs autumn) | -0.0553 | 0.1214 | ±0.2428 | -0.455 | 0.6491 |  |
| **Age (years)** | **-0.0182** | 0.0038 | ±0.0076 | **-4.779** | **1.76e-06** | *** |
| BMI (kg/m2) | +0.0076 | 0.0065 | ±0.0130 | +1.170 | 0.2420 |  |
| Hypertension | +0.1692 | 0.0925 | ±0.1851 | +1.828 | 0.0676 | . |
| High cholesterol | -0.0275 | 0.0836 | ±0.1672 | -0.329 | 0.7422 |  |
| Kidney disease | -0.0089 | 0.1385 | ±0.2771 | -0.064 | 0.9488 |  |
| Circulatory disease | -0.0079 | 0.1175 | ±0.2350 | -0.067 | 0.9465 |  |
| Any reading > 250 during wear (0/1) | -0.0258 | 0.0921 | ±0.1843 | -0.280 | 0.7795 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **628**, R² = **0.1792**, Adj R² = **0.1605**, F-statistic = **9.56** (p = **2.28e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.6**, BIC = **1828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0297** | 0.3496 | ±0.6992 | **+8.667** | **4.45e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2092** | 0.0793 | ±0.1587 | **-2.637** | **0.0084** | ** |
| **Education: high school or below (vs college)** | **+0.6000** | 0.1929 | ±0.3858 | **+3.111** | **0.0019** | ** |
| Site: UCSD (vs UAB) | +0.1114 | 0.1042 | ±0.2085 | +1.069 | 0.2850 |  |
| **Site: UW (vs UAB)** | **-0.3993** | 0.0953 | ±0.1907 | **-4.188** | **2.81e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3821** | 0.1038 | ±0.2076 | **-3.680** | **2.33e-04** | *** |
| Season: summer (vs autumn) | -0.0941 | 0.1205 | ±0.2410 | -0.781 | 0.4350 |  |
| Season: winter (vs autumn) | -0.0532 | 0.1207 | ±0.2413 | -0.441 | 0.6594 |  |
| **Age (years)** | **-0.0183** | 0.0038 | ±0.0075 | **-4.869** | **1.12e-06** | *** |
| BMI (kg/m2) | +0.0077 | 0.0064 | ±0.0129 | +1.192 | 0.2331 |  |
| Hypertension | +0.1641 | 0.0905 | ±0.1809 | +1.815 | 0.0696 | . |
| High cholesterol | -0.0273 | 0.0838 | ±0.1676 | -0.326 | 0.7445 |  |
| Kidney disease | -0.0177 | 0.1390 | ±0.2781 | -0.127 | 0.8988 |  |
| Circulatory disease | -0.0084 | 0.1183 | ±0.2366 | -0.071 | 0.9431 |  |
| Time > 250 (%) | +0.0020 | 0.0049 | ±0.0098 | +0.416 | 0.6771 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 628)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **628**, R² = **0.1794**, Adj R² = **0.1607**, F-statistic = **9.57** (p = **2.16e-19**), Residual SE = **0.972** on **613** df, AIC = **1761.4**, BIC = **1828.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.0286** | 0.3492 | ±0.6984 | **+8.673** | **4.23e-18** | *** |
| **Education: graduate level (vs college)** | **-0.2084** | 0.0793 | ±0.1586 | **-2.627** | **0.0086** | ** |
| **Education: high school or below (vs college)** | **+0.5970** | 0.1933 | ±0.3866 | **+3.088** | **0.0020** | ** |
| Site: UCSD (vs UAB) | +0.1116 | 0.1042 | ±0.2085 | +1.070 | 0.2846 |  |
| **Site: UW (vs UAB)** | **-0.3984** | 0.0953 | ±0.1906 | **-4.181** | **2.91e-05** | *** |
| **Season: spring (vs autumn)** | **-0.3832** | 0.1039 | ±0.2078 | **-3.689** | **2.25e-04** | *** |
| Season: summer (vs autumn) | -0.0934 | 0.1204 | ±0.2408 | -0.776 | 0.4377 |  |
| Season: winter (vs autumn) | -0.0538 | 0.1207 | ±0.2413 | -0.446 | 0.6558 |  |
| **Age (years)** | **-0.0184** | 0.0038 | ±0.0075 | **-4.872** | **1.11e-06** | *** |
| BMI (kg/m2) | +0.0077 | 0.0064 | ±0.0129 | +1.196 | 0.2317 |  |
| Hypertension | +0.1630 | 0.0905 | ±0.1810 | +1.801 | 0.0718 | . |
| High cholesterol | -0.0271 | 0.0838 | ±0.1676 | -0.323 | 0.7464 |  |
| Kidney disease | -0.0202 | 0.1384 | ±0.2768 | -0.146 | 0.8842 |  |
| Circulatory disease | -0.0092 | 0.1185 | ±0.2371 | -0.078 | 0.9379 |  |
| Avg. daily time > 250 (%) | +0.0035 | 0.0058 | ±0.0116 | +0.604 | 0.5457 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 628; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **628**, R² = **0.2851**, Adj R² = **0.2700**, F-statistic = **18.84** (p = **3.30e-37**), Residual SE = **2.044** on **614** df, AIC = **2694.2**, BIC = **2756.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6490** | 0.6356 | ±1.2712 | **+37.208** | **5.13e-303** | *** |
| Education: graduate level (vs college) | +0.0404 | 0.1758 | ±0.3517 | +0.230 | 0.8182 |  |
| Education: high school or below (vs college) | +0.1076 | 0.3068 | ±0.6136 | +0.351 | 0.7257 |  |
| Site: UCSD (vs UAB) | -0.1241 | 0.2119 | ±0.4238 | -0.586 | 0.5581 |  |
| **Site: UW (vs UAB)** | **-1.0365** | 0.1907 | ±0.3814 | **-5.435** | **5.49e-08** | *** |
| Season: spring (vs autumn) | -0.0803 | 0.2199 | ±0.4399 | -0.365 | 0.7152 |  |
| **Season: summer (vs autumn)** | **+2.3003** | 0.2562 | ±0.5124 | **+8.978** | **2.75e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0197** | 0.2280 | ±0.4560 | **-4.472** | **7.74e-06** | *** |
| Age (years) | +0.0145 | 0.0079 | ±0.0157 | +1.843 | 0.0654 | . |
| BMI (kg/m2) | +0.0041 | 0.0118 | ±0.0237 | +0.350 | 0.7264 |  |
| Hypertension | +0.3108 | 0.1829 | ±0.3659 | +1.699 | 0.0894 | . |
| High cholesterol | -0.3146 | 0.1764 | ±0.3529 | -1.783 | 0.0746 | . |
| Kidney disease | +0.2881 | 0.2809 | ±0.5617 | +1.026 | 0.3049 |  |
| Circulatory disease | +0.0964 | 0.2385 | ±0.4770 | +0.404 | 0.6860 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **628**, R² = **0.2852**, Adj R² = **0.2689**, F-statistic = **17.47** (p = **1.41e-36**), Residual SE = **2.046** on **613** df, AIC = **2696.2**, BIC = **2762.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7928** | 0.7946 | ±1.5892 | **+29.943** | **5.44e-197** | *** |
| Education: graduate level (vs college) | +0.0368 | 0.1761 | ±0.3522 | +0.209 | 0.8343 |  |
| Education: high school or below (vs college) | +0.1173 | 0.3120 | ±0.6240 | +0.376 | 0.7069 |  |
| Site: UCSD (vs UAB) | -0.1223 | 0.2118 | ±0.4235 | -0.577 | 0.5637 |  |
| **Site: UW (vs UAB)** | **-1.0405** | 0.1918 | ±0.3837 | **-5.423** | **5.85e-08** | *** |
| Season: spring (vs autumn) | -0.0819 | 0.2204 | ±0.4409 | -0.371 | 0.7103 |  |
| **Season: summer (vs autumn)** | **+2.2985** | 0.2564 | ±0.5128 | **+8.965** | **3.10e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0216** | 0.2289 | ±0.4578 | **-4.463** | **8.08e-06** | *** |
| Age (years) | +0.0148 | 0.0080 | ±0.0160 | +1.851 | 0.0642 | . |
| BMI (kg/m2) | +0.0044 | 0.0120 | ±0.0239 | +0.369 | 0.7119 |  |
| Hypertension | +0.3168 | 0.1833 | ±0.3666 | +1.728 | 0.0839 | . |
| High cholesterol | -0.3114 | 0.1778 | ±0.3555 | -1.752 | 0.0798 | . |
| Kidney disease | +0.2917 | 0.2823 | ±0.5646 | +1.033 | 0.3016 |  |
| Circulatory disease | +0.0960 | 0.2394 | ±0.4787 | +0.401 | 0.6885 |  |
| HbA1c (%) | -0.0287 | 0.1009 | ±0.2018 | -0.285 | 0.7757 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **628**, R² = **0.2857**, Adj R² = **0.2694**, F-statistic = **17.52** (p = **1.13e-36**), Residual SE = **2.045** on **613** df, AIC = **2695.7**, BIC = **2762.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9290** | 0.7610 | ±1.5219 | **+31.446** | **4.80e-217** | *** |
| Education: graduate level (vs college) | +0.0402 | 0.1761 | ±0.3523 | +0.228 | 0.8195 |  |
| Education: high school or below (vs college) | +0.1295 | 0.3100 | ±0.6199 | +0.418 | 0.6761 |  |
| Site: UCSD (vs UAB) | -0.1225 | 0.2129 | ±0.4258 | -0.575 | 0.5650 |  |
| **Site: UW (vs UAB)** | **-1.0406** | 0.1912 | ±0.3824 | **-5.442** | **5.27e-08** | *** |
| Season: spring (vs autumn) | -0.0756 | 0.2195 | ±0.4390 | -0.344 | 0.7307 |  |
| **Season: summer (vs autumn)** | **+2.2968** | 0.2564 | ±0.5128 | **+8.957** | **3.32e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0242** | 0.2289 | ±0.4579 | **-4.474** | **7.69e-06** | *** |
| Age (years) | +0.0146 | 0.0079 | ±0.0158 | +1.858 | 0.0631 | . |
| BMI (kg/m2) | +0.0045 | 0.0119 | ±0.0239 | +0.380 | 0.7043 |  |
| Hypertension | +0.3299 | 0.1830 | ±0.3660 | +1.803 | 0.0715 | . |
| High cholesterol | -0.3066 | 0.1787 | ±0.3574 | -1.716 | 0.0862 | . |
| Kidney disease | +0.3100 | 0.2840 | ±0.5681 | +1.091 | 0.2751 |  |
| Circulatory disease | +0.0992 | 0.2391 | ±0.4782 | +0.415 | 0.6783 |  |
| Mean glucose (mg/dL) | -0.0026 | 0.0039 | ±0.0078 | -0.669 | 0.5038 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **628**, R² = **0.2857**, Adj R² = **0.2694**, F-statistic = **17.52** (p = **1.13e-36**), Residual SE = **2.045** on **613** df, AIC = **2695.7**, BIC = **2762.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.2876** | 1.1463 | ±2.2925 | **+21.188** | **1.22e-99** | *** |
| Education: graduate level (vs college) | +0.0402 | 0.1761 | ±0.3523 | +0.228 | 0.8195 |  |
| Education: high school or below (vs college) | +0.1295 | 0.3100 | ±0.6199 | +0.418 | 0.6761 |  |
| Site: UCSD (vs UAB) | -0.1225 | 0.2129 | ±0.4258 | -0.575 | 0.5650 |  |
| **Site: UW (vs UAB)** | **-1.0406** | 0.1912 | ±0.3824 | **-5.442** | **5.27e-08** | *** |
| Season: spring (vs autumn) | -0.0756 | 0.2195 | ±0.4390 | -0.344 | 0.7307 |  |
| **Season: summer (vs autumn)** | **+2.2968** | 0.2564 | ±0.5128 | **+8.957** | **3.32e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0242** | 0.2289 | ±0.4579 | **-4.474** | **7.69e-06** | *** |
| Age (years) | +0.0146 | 0.0079 | ±0.0158 | +1.858 | 0.0631 | . |
| BMI (kg/m2) | +0.0045 | 0.0119 | ±0.0239 | +0.380 | 0.7043 |  |
| Hypertension | +0.3299 | 0.1830 | ±0.3660 | +1.803 | 0.0715 | . |
| High cholesterol | -0.3066 | 0.1787 | ±0.3574 | -1.716 | 0.0862 | . |
| Kidney disease | +0.3100 | 0.2840 | ±0.5681 | +1.091 | 0.2751 |  |
| Circulatory disease | +0.0992 | 0.2391 | ±0.4782 | +0.415 | 0.6783 |  |
| GMI (%) | -0.1083 | 0.1620 | ±0.3240 | -0.669 | 0.5038 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **628**, R² = **0.2863**, Adj R² = **0.2700**, F-statistic = **17.56** (p = **9.15e-37**), Residual SE = **2.044** on **613** df, AIC = **2695.2**, BIC = **2761.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0269** | 0.7812 | ±1.5623 | **+30.758** | **9.59e-208** | *** |
| Education: graduate level (vs college) | +0.0416 | 0.1763 | ±0.3527 | +0.236 | 0.8136 |  |
| Education: high school or below (vs college) | +0.1345 | 0.3092 | ±0.6185 | +0.435 | 0.6635 |  |
| Site: UCSD (vs UAB) | -0.1200 | 0.2131 | ±0.4262 | -0.563 | 0.5732 |  |
| **Site: UW (vs UAB)** | **-1.0402** | 0.1910 | ±0.3819 | **-5.447** | **5.11e-08** | *** |
| Season: spring (vs autumn) | -0.0706 | 0.2191 | ±0.4382 | -0.322 | 0.7474 |  |
| **Season: summer (vs autumn)** | **+2.2919** | 0.2565 | ±0.5129 | **+8.937** | **4.00e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0214** | 0.2293 | ±0.4586 | **-4.455** | **8.40e-06** | *** |
| Age (years) | +0.0142 | 0.0079 | ±0.0157 | +1.811 | 0.0702 | . |
| BMI (kg/m2) | +0.0052 | 0.0121 | ±0.0242 | +0.428 | 0.6686 |  |
| Hypertension | +0.3352 | 0.1822 | ±0.3643 | +1.840 | 0.0657 | . |
| High cholesterol | -0.3000 | 0.1804 | ±0.3608 | -1.663 | 0.0963 | . |
| Kidney disease | +0.2958 | 0.2803 | ±0.5606 | +1.055 | 0.2912 |  |
| Circulatory disease | +0.0976 | 0.2400 | ±0.4799 | +0.407 | 0.6840 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0035 | 0.0043 | ±0.0087 | -0.802 | 0.4223 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **628**, R² = **0.2853**, Adj R² = **0.2690**, F-statistic = **17.48** (p = **1.34e-36**), Residual SE = **2.046** on **613** df, AIC = **2696.0**, BIC = **2762.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7012** | 0.6504 | ±1.3008 | **+36.442** | **9.21e-291** | *** |
| Education: graduate level (vs college) | +0.0376 | 0.1761 | ±0.3522 | +0.213 | 0.8311 |  |
| Education: high school or below (vs college) | +0.1262 | 0.3142 | ±0.6284 | +0.402 | 0.6879 |  |
| Site: UCSD (vs UAB) | -0.1240 | 0.2128 | ±0.4256 | -0.583 | 0.5602 |  |
| **Site: UW (vs UAB)** | **-1.0437** | 0.1918 | ±0.3835 | **-5.442** | **5.26e-08** | *** |
| Season: spring (vs autumn) | -0.0807 | 0.2199 | ±0.4397 | -0.367 | 0.7136 |  |
| **Season: summer (vs autumn)** | **+2.2970** | 0.2565 | ±0.5130 | **+8.956** | **3.38e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0235** | 0.2290 | ±0.4581 | **-4.469** | **7.87e-06** | *** |
| Age (years) | +0.0149 | 0.0079 | ±0.0159 | +1.884 | 0.0595 | . |
| BMI (kg/m2) | +0.0042 | 0.0119 | ±0.0237 | +0.353 | 0.7243 |  |
| Hypertension | +0.3212 | 0.1853 | ±0.3707 | +1.733 | 0.0831 | . |
| High cholesterol | -0.3141 | 0.1768 | ±0.3537 | -1.776 | 0.0757 | . |
| Kidney disease | +0.3142 | 0.2922 | ±0.5843 | +1.075 | 0.2823 |  |
| Circulatory disease | +0.0950 | 0.2395 | ±0.4789 | +0.397 | 0.6916 |  |
| Glucose SD, pooled (mg/dL) | -0.0032 | 0.0077 | ±0.0155 | -0.411 | 0.6813 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **628**, R² = **0.2859**, Adj R² = **0.2696**, F-statistic = **17.53** (p = **1.08e-36**), Residual SE = **2.045** on **613** df, AIC = **2695.6**, BIC = **2762.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7463** | 0.6526 | ±1.3052 | **+36.388** | **6.49e-290** | *** |
| Education: graduate level (vs college) | +0.0342 | 0.1762 | ±0.3524 | +0.194 | 0.8462 |  |
| Education: high school or below (vs college) | +0.1466 | 0.3129 | ±0.6258 | +0.469 | 0.6394 |  |
| Site: UCSD (vs UAB) | -0.1224 | 0.2126 | ±0.4251 | -0.576 | 0.5648 |  |
| **Site: UW (vs UAB)** | **-1.0480** | 0.1911 | ±0.3822 | **-5.484** | **4.16e-08** | *** |
| Season: spring (vs autumn) | -0.0792 | 0.2197 | ±0.4395 | -0.361 | 0.7184 |  |
| **Season: summer (vs autumn)** | **+2.2928** | 0.2566 | ±0.5131 | **+8.937** | **4.02e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0277** | 0.2282 | ±0.4565 | **-4.503** | **6.71e-06** | *** |
| Age (years) | +0.0154 | 0.0079 | ±0.0158 | +1.949 | 0.0513 | . |
| BMI (kg/m2) | +0.0042 | 0.0119 | ±0.0237 | +0.353 | 0.7242 |  |
| Hypertension | +0.3286 | 0.1857 | ±0.3713 | +1.770 | 0.0767 | . |
| High cholesterol | -0.3126 | 0.1766 | ±0.3532 | -1.770 | 0.0767 | . |
| Kidney disease | +0.3379 | 0.2909 | ±0.5819 | +1.162 | 0.2454 |  |
| Circulatory disease | +0.0919 | 0.2388 | ±0.4776 | +0.385 | 0.7004 |  |
| Avg. daily SD (mg/dL) | -0.0068 | 0.0083 | ±0.0167 | -0.819 | 0.4129 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **628**, R² = **0.2852**, Adj R² = **0.2689**, F-statistic = **17.47** (p = **1.41e-36**), Residual SE = **2.046** on **613** df, AIC = **2696.2**, BIC = **2762.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5876** | 0.6799 | ±1.3597 | **+34.695** | **9.34e-264** | *** |
| Education: graduate level (vs college) | +0.0425 | 0.1762 | ±0.3525 | +0.241 | 0.8094 |  |
| Education: high school or below (vs college) | +0.0969 | 0.3125 | ±0.6250 | +0.310 | 0.7565 |  |
| Site: UCSD (vs UAB) | -0.1242 | 0.2122 | ±0.4245 | -0.585 | 0.5584 |  |
| **Site: UW (vs UAB)** | **-1.0310** | 0.1913 | ±0.3826 | **-5.390** | **7.05e-08** | *** |
| Season: spring (vs autumn) | -0.0789 | 0.2205 | ±0.4409 | -0.358 | 0.7203 |  |
| **Season: summer (vs autumn)** | **+2.3011** | 0.2566 | ±0.5131 | **+8.969** | **2.98e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0176** | 0.2287 | ±0.4574 | **-4.450** | **8.60e-06** | *** |
| Age (years) | +0.0141 | 0.0080 | ±0.0160 | +1.762 | 0.0781 | . |
| BMI (kg/m2) | +0.0042 | 0.0119 | ±0.0237 | +0.352 | 0.7250 |  |
| Hypertension | +0.3060 | 0.1856 | ±0.3713 | +1.649 | 0.0992 | . |
| High cholesterol | -0.3131 | 0.1768 | ±0.3536 | -1.771 | 0.0766 | . |
| Kidney disease | +0.2699 | 0.2946 | ±0.5891 | +0.916 | 0.3595 |  |
| Circulatory disease | +0.0979 | 0.2396 | ±0.4792 | +0.409 | 0.6827 |  |
| CV (%) | +0.0041 | 0.0150 | ±0.0300 | +0.271 | 0.7862 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **628**, R² = **0.2851**, Adj R² = **0.2688**, F-statistic = **17.46** (p = **1.47e-36**), Residual SE = **2.046** on **613** df, AIC = **2696.2**, BIC = **2762.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6634** | 0.7753 | ±1.5505 | **+30.523** | **1.28e-204** | *** |
| Education: graduate level (vs college) | +0.0405 | 0.1761 | ±0.3523 | +0.230 | 0.8181 |  |
| Education: high school or below (vs college) | +0.1064 | 0.3112 | ±0.6224 | +0.342 | 0.7323 |  |
| Site: UCSD (vs UAB) | -0.1243 | 0.2122 | ±0.4245 | -0.586 | 0.5582 |  |
| **Site: UW (vs UAB)** | **-1.0361** | 0.1907 | ±0.3813 | **-5.434** | **5.51e-08** | *** |
| Season: spring (vs autumn) | -0.0802 | 0.2205 | ±0.4409 | -0.364 | 0.7161 |  |
| **Season: summer (vs autumn)** | **+2.3003** | 0.2567 | ±0.5134 | **+8.961** | **3.21e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0196** | 0.2287 | ±0.4574 | **-4.458** | **8.26e-06** | *** |
| Age (years) | +0.0144 | 0.0080 | ±0.0160 | +1.807 | 0.0708 | . |
| BMI (kg/m2) | +0.0041 | 0.0119 | ±0.0237 | +0.349 | 0.7270 |  |
| Hypertension | +0.3103 | 0.1852 | ±0.3704 | +1.676 | 0.0938 | . |
| High cholesterol | -0.3144 | 0.1768 | ±0.3535 | -1.779 | 0.0753 | . |
| Kidney disease | +0.2866 | 0.2898 | ±0.5797 | +0.989 | 0.3228 |  |
| Circulatory disease | +0.0964 | 0.2388 | ±0.4776 | +0.404 | 0.6865 |  |
| Mean / SD ratio | -0.0022 | 0.0695 | ±0.1390 | -0.031 | 0.9753 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **628**, R² = **0.2855**, Adj R² = **0.2692**, F-statistic = **17.49** (p = **1.26e-36**), Residual SE = **2.046** on **613** df, AIC = **2695.9**, BIC = **2762.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.4017** | 0.7860 | ±1.5719 | **+29.774** | **8.36e-195** | *** |
| Education: graduate level (vs college) | +0.0381 | 0.1762 | ±0.3524 | +0.216 | 0.8287 |  |
| Education: high school or below (vs college) | +0.1309 | 0.3105 | ±0.6210 | +0.422 | 0.6732 |  |
| Site: UCSD (vs UAB) | -0.1175 | 0.2131 | ±0.4262 | -0.552 | 0.5812 |  |
| **Site: UW (vs UAB)** | **-1.0411** | 0.1903 | ±0.3806 | **-5.471** | **4.48e-08** | *** |
| Season: spring (vs autumn) | -0.0805 | 0.2203 | ±0.4405 | -0.366 | 0.7147 |  |
| **Season: summer (vs autumn)** | **+2.2969** | 0.2567 | ±0.5134 | **+8.948** | **3.61e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0231** | 0.2285 | ±0.4570 | **-4.478** | **7.55e-06** | *** |
| Age (years) | +0.0154 | 0.0080 | ±0.0160 | +1.924 | 0.0544 | . |
| BMI (kg/m2) | +0.0043 | 0.0118 | ±0.0237 | +0.360 | 0.7186 |  |
| Hypertension | +0.3161 | 0.1845 | ±0.3691 | +1.713 | 0.0868 | . |
| High cholesterol | -0.3157 | 0.1766 | ±0.3532 | -1.788 | 0.0738 | . |
| Kidney disease | +0.3132 | 0.2891 | ±0.5782 | +1.083 | 0.2787 |  |
| Circulatory disease | +0.0951 | 0.2386 | ±0.4771 | +0.399 | 0.6902 |  |
| Avg. daily mean/SD | +0.0306 | 0.0593 | ±0.1185 | +0.517 | 0.6055 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **628**, R² = **0.2851**, Adj R² = **0.2688**, F-statistic = **17.46** (p = **1.46e-36**), Residual SE = **2.046** on **613** df, AIC = **2696.2**, BIC = **2762.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6831** | 0.7249 | ±1.4498 | **+32.670** | **4.18e-234** | *** |
| Education: graduate level (vs college) | +0.0400 | 0.1766 | ±0.3532 | +0.227 | 0.8207 |  |
| Education: high school or below (vs college) | +0.1107 | 0.3063 | ±0.6125 | +0.361 | 0.7178 |  |
| Site: UCSD (vs UAB) | -0.1233 | 0.2127 | ±0.4254 | -0.580 | 0.5621 |  |
| **Site: UW (vs UAB)** | **-1.0388** | 0.1909 | ±0.3819 | **-5.441** | **5.30e-08** | *** |
| Season: spring (vs autumn) | -0.0804 | 0.2203 | ±0.4406 | -0.365 | 0.7151 |  |
| **Season: summer (vs autumn)** | **+2.2996** | 0.2564 | ±0.5127 | **+8.970** | **2.97e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0205** | 0.2281 | ±0.4563 | **-4.473** | **7.70e-06** | *** |
| Age (years) | +0.0145 | 0.0079 | ±0.0158 | +1.842 | 0.0655 | . |
| BMI (kg/m2) | +0.0042 | 0.0119 | ±0.0238 | +0.353 | 0.7240 |  |
| Hypertension | +0.3117 | 0.1841 | ±0.3683 | +1.693 | 0.0905 | . |
| High cholesterol | -0.3152 | 0.1768 | ±0.3536 | -1.783 | 0.0746 | . |
| Kidney disease | +0.2889 | 0.2816 | ±0.5632 | +1.026 | 0.3049 |  |
| Circulatory disease | +0.0962 | 0.2389 | ±0.4778 | +0.403 | 0.6872 |  |
| MAG (mg/dL/h) | -0.0009 | 0.0087 | ±0.0173 | -0.098 | 0.9217 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **628**, R² = **0.2859**, Adj R² = **0.2696**, F-statistic = **17.53** (p = **1.06e-36**), Residual SE = **2.045** on **613** df, AIC = **2695.5**, BIC = **2762.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8095** | 0.6737 | ±1.3474 | **+35.342** | **1.34e-273** | *** |
| Education: graduate level (vs college) | +0.0335 | 0.1764 | ±0.3528 | +0.190 | 0.8494 |  |
| Education: high school or below (vs college) | +0.1477 | 0.3123 | ±0.6245 | +0.473 | 0.6363 |  |
| Site: UCSD (vs UAB) | -0.1220 | 0.2126 | ±0.4253 | -0.574 | 0.5663 |  |
| **Site: UW (vs UAB)** | **-1.0477** | 0.1909 | ±0.3817 | **-5.489** | **4.05e-08** | *** |
| Season: spring (vs autumn) | -0.0793 | 0.2198 | ±0.4396 | -0.361 | 0.7183 |  |
| **Season: summer (vs autumn)** | **+2.2949** | 0.2565 | ±0.5131 | **+8.945** | **3.71e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0271** | 0.2281 | ±0.4562 | **-4.503** | **6.70e-06** | *** |
| Age (years) | +0.0154 | 0.0079 | ±0.0158 | +1.948 | 0.0514 | . |
| BMI (kg/m2) | +0.0038 | 0.0119 | ±0.0238 | +0.324 | 0.7462 |  |
| Hypertension | +0.3255 | 0.1852 | ±0.3704 | +1.758 | 0.0788 | . |
| High cholesterol | -0.3139 | 0.1765 | ±0.3530 | -1.778 | 0.0754 | . |
| Kidney disease | +0.3355 | 0.2902 | ±0.5803 | +1.156 | 0.2476 |  |
| Circulatory disease | +0.0954 | 0.2383 | ±0.4767 | +0.400 | 0.6890 |  |
| Avg. daily range (mg/dL) | -0.0018 | 0.0022 | ±0.0044 | -0.831 | 0.4057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **628**, R² = **0.2851**, Adj R² = **0.2688**, F-statistic = **17.46** (p = **1.47e-36**), Residual SE = **2.046** on **613** df, AIC = **2696.2**, BIC = **2762.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6527** | 0.6398 | ±1.2796 | **+36.968** | **3.78e-299** | *** |
| Education: graduate level (vs college) | +0.0402 | 0.1760 | ±0.3519 | +0.228 | 0.8194 |  |
| Education: high school or below (vs college) | +0.1083 | 0.3105 | ±0.6210 | +0.349 | 0.7273 |  |
| Site: UCSD (vs UAB) | -0.1243 | 0.2150 | ±0.4299 | -0.578 | 0.5630 |  |
| **Site: UW (vs UAB)** | **-1.0372** | 0.1928 | ±0.3857 | **-5.378** | **7.52e-08** | *** |
| Season: spring (vs autumn) | -0.0804 | 0.2203 | ±0.4405 | -0.365 | 0.7151 |  |
| **Season: summer (vs autumn)** | **+2.3003** | 0.2565 | ±0.5130 | **+8.968** | **3.02e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0198** | 0.2294 | ±0.4587 | **-4.446** | **8.75e-06** | *** |
| Age (years) | +0.0145 | 0.0079 | ±0.0159 | +1.831 | 0.0672 | . |
| BMI (kg/m2) | +0.0042 | 0.0119 | ±0.0238 | +0.349 | 0.7270 |  |
| Hypertension | +0.3119 | 0.1842 | ±0.3684 | +1.693 | 0.0904 | . |
| High cholesterol | -0.3145 | 0.1774 | ±0.3548 | -1.773 | 0.0763 | . |
| Kidney disease | +0.2900 | 0.2887 | ±0.5773 | +1.005 | 0.3151 |  |
| Circulatory disease | +0.0968 | 0.2386 | ±0.4773 | +0.406 | 0.6849 |  |
| SD of daily means (mg/dL) | -0.0006 | 0.0174 | ±0.0348 | -0.036 | 0.9714 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **628**, R² = **0.2852**, Adj R² = **0.2688**, F-statistic = **17.47** (p = **1.44e-36**), Residual SE = **2.046** on **613** df, AIC = **2696.2**, BIC = **2762.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5196** | 0.9389 | ±1.8779 | **+25.049** | **1.78e-138** | *** |
| Education: graduate level (vs college) | +0.0384 | 0.1761 | ±0.3523 | +0.218 | 0.8273 |  |
| Education: high school or below (vs college) | +0.1132 | 0.3123 | ±0.6246 | +0.362 | 0.7170 |  |
| Site: UCSD (vs UAB) | -0.1254 | 0.2142 | ±0.4284 | -0.585 | 0.5583 |  |
| **Site: UW (vs UAB)** | **-1.0404** | 0.1932 | ±0.3864 | **-5.385** | **7.23e-08** | *** |
| Season: spring (vs autumn) | -0.0799 | 0.2201 | ±0.4402 | -0.363 | 0.7165 |  |
| **Season: summer (vs autumn)** | **+2.2986** | 0.2565 | ±0.5129 | **+8.962** | **3.18e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0198** | 0.2286 | ±0.4573 | **-4.460** | **8.19e-06** | *** |
| Age (years) | +0.0146 | 0.0079 | ±0.0158 | +1.848 | 0.0646 | . |
| BMI (kg/m2) | +0.0042 | 0.0119 | ±0.0238 | +0.352 | 0.7247 |  |
| Hypertension | +0.3144 | 0.1836 | ±0.3671 | +1.712 | 0.0868 | . |
| High cholesterol | -0.3133 | 0.1777 | ±0.3554 | -1.763 | 0.0779 | . |
| Kidney disease | +0.2973 | 0.2869 | ±0.5739 | +1.036 | 0.3002 |  |
| Circulatory disease | +0.0971 | 0.2389 | ±0.4778 | +0.406 | 0.6844 |  |
| Time in range 70-180, pooled (%) | +0.0013 | 0.0072 | ±0.0144 | +0.186 | 0.8523 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **628**, R² = **0.2851**, Adj R² = **0.2688**, F-statistic = **17.47** (p = **1.45e-36**), Residual SE = **2.046** on **613** df, AIC = **2696.2**, BIC = **2762.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5423** | 0.9379 | ±1.8759 | **+25.100** | **4.98e-139** | *** |
| Education: graduate level (vs college) | +0.0387 | 0.1761 | ±0.3523 | +0.220 | 0.8261 |  |
| Education: high school or below (vs college) | +0.1124 | 0.3128 | ±0.6255 | +0.359 | 0.7194 |  |
| Site: UCSD (vs UAB) | -0.1251 | 0.2141 | ±0.4282 | -0.584 | 0.5590 |  |
| **Site: UW (vs UAB)** | **-1.0398** | 0.1933 | ±0.3866 | **-5.378** | **7.52e-08** | *** |
| Season: spring (vs autumn) | -0.0798 | 0.2202 | ±0.4404 | -0.363 | 0.7170 |  |
| **Season: summer (vs autumn)** | **+2.2989** | 0.2565 | ±0.5130 | **+8.963** | **3.15e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0196** | 0.2286 | ±0.4572 | **-4.460** | **8.21e-06** | *** |
| Age (years) | +0.0146 | 0.0079 | ±0.0158 | +1.847 | 0.0647 | . |
| BMI (kg/m2) | +0.0042 | 0.0119 | ±0.0238 | +0.352 | 0.7251 |  |
| Hypertension | +0.3136 | 0.1837 | ±0.3674 | +1.707 | 0.0878 | . |
| High cholesterol | -0.3134 | 0.1778 | ±0.3556 | -1.763 | 0.0779 | . |
| Kidney disease | +0.2958 | 0.2871 | ±0.5742 | +1.030 | 0.3029 |  |
| Circulatory disease | +0.0969 | 0.2389 | ±0.4778 | +0.406 | 0.6849 |  |
| Avg. daily time in range 70-180 (%) | +0.0011 | 0.0071 | ±0.0143 | +0.154 | 0.8779 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **628**, R² = **0.2902**, Adj R² = **0.2740**, F-statistic = **17.90** (p = **1.80e-37**), Residual SE = **2.039** on **613** df, AIC = **2691.7**, BIC = **2758.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5056** | 0.6371 | ±1.2743 | **+36.892** | **6.19e-298** | *** |
| Education: graduate level (vs college) | +0.0471 | 0.1757 | ±0.3514 | +0.268 | 0.7888 |  |
| Education: high school or below (vs college) | +0.1415 | 0.3059 | ±0.6119 | +0.463 | 0.6437 |  |
| Site: UCSD (vs UAB) | -0.0551 | 0.2122 | ±0.4244 | -0.260 | 0.7950 |  |
| **Site: UW (vs UAB)** | **-0.9805** | 0.1911 | ±0.3821 | **-5.132** | **2.87e-07** | *** |
| Season: spring (vs autumn) | -0.0657 | 0.2206 | ±0.4413 | -0.298 | 0.7657 |  |
| **Season: summer (vs autumn)** | **+2.2812** | 0.2573 | ±0.5145 | **+8.867** | **7.52e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0305** | 0.2265 | ±0.4530 | **-4.550** | **5.36e-06** | *** |
| Age (years) | +0.0143 | 0.0079 | ±0.0157 | +1.818 | 0.0690 | . |
| BMI (kg/m2) | +0.0045 | 0.0119 | ±0.0237 | +0.382 | 0.7023 |  |
| Hypertension | +0.3299 | 0.1819 | ±0.3639 | +1.813 | 0.0698 | . |
| High cholesterol | -0.2907 | 0.1763 | ±0.3527 | -1.648 | 0.0993 | . |
| Kidney disease | +0.2808 | 0.2811 | ±0.5623 | +0.999 | 0.3178 |  |
| Circulatory disease | +0.0931 | 0.2372 | ±0.4744 | +0.392 | 0.6948 |  |
| **Time < 54 (%)** | **+0.1996** | 0.0881 | ±0.1762 | **+2.266** | **0.0235** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **628**, R² = **0.2889**, Adj R² = **0.2726**, F-statistic = **17.79** (p = **3.13e-37**), Residual SE = **2.041** on **613** df, AIC = **2692.9**, BIC = **2759.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5843** | 0.6360 | ±1.2720 | **+37.083** | **5.20e-301** | *** |
| Education: graduate level (vs college) | +0.0551 | 0.1756 | ±0.3512 | +0.314 | 0.7536 |  |
| Education: high school or below (vs college) | +0.1365 | 0.3055 | ±0.6111 | +0.447 | 0.6551 |  |
| Site: UCSD (vs UAB) | -0.0736 | 0.2121 | ±0.4243 | -0.347 | 0.7285 |  |
| **Site: UW (vs UAB)** | **-0.9829** | 0.1913 | ±0.3826 | **-5.138** | **2.77e-07** | *** |
| Season: spring (vs autumn) | -0.0662 | 0.2207 | ±0.4414 | -0.300 | 0.7641 |  |
| **Season: summer (vs autumn)** | **+2.2861** | 0.2580 | ±0.5160 | **+8.861** | **7.96e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0341** | 0.2270 | ±0.4539 | **-4.556** | **5.21e-06** | *** |
| Age (years) | +0.0137 | 0.0079 | ±0.0158 | +1.735 | 0.0828 | . |
| BMI (kg/m2) | +0.0043 | 0.0118 | ±0.0237 | +0.364 | 0.7160 |  |
| Hypertension | +0.3287 | 0.1822 | ±0.3644 | +1.804 | 0.0712 | . |
| High cholesterol | -0.2942 | 0.1761 | ±0.3521 | -1.671 | 0.0947 | . |
| Kidney disease | +0.2738 | 0.2804 | ±0.5608 | +0.976 | 0.3288 |  |
| Circulatory disease | +0.0915 | 0.2371 | ±0.4743 | +0.386 | 0.6995 |  |
| Avg. daily time < 54 (%) | +0.1994 | 0.1295 | ±0.2590 | +1.540 | 0.1236 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **628**, R² = **0.2890**, Adj R² = **0.2727**, F-statistic = **17.79** (p = **3.03e-37**), Residual SE = **2.041** on **613** df, AIC = **2692.8**, BIC = **2759.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5543** | 0.6376 | ±1.2752 | **+36.941** | **1.02e-298** | *** |
| Education: graduate level (vs college) | +0.0616 | 0.1767 | ±0.3534 | +0.348 | 0.7275 |  |
| Education: high school or below (vs college) | +0.1117 | 0.3047 | ±0.6094 | +0.367 | 0.7139 |  |
| Site: UCSD (vs UAB) | -0.0942 | 0.2125 | ±0.4250 | -0.443 | 0.6575 |  |
| **Site: UW (vs UAB)** | **-1.0019** | 0.1904 | ±0.3809 | **-5.261** | **1.43e-07** | *** |
| Season: spring (vs autumn) | -0.0682 | 0.2193 | ±0.4386 | -0.311 | 0.7559 |  |
| **Season: summer (vs autumn)** | **+2.2994** | 0.2552 | ±0.5104 | **+9.009** | **2.07e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0339** | 0.2281 | ±0.4563 | **-4.532** | **5.85e-06** | *** |
| Age (years) | +0.0138 | 0.0078 | ±0.0156 | +1.766 | 0.0773 | . |
| BMI (kg/m2) | +0.0039 | 0.0119 | ±0.0238 | +0.330 | 0.7414 |  |
| Hypertension | +0.3315 | 0.1823 | ±0.3646 | +1.818 | 0.0690 | . |
| High cholesterol | -0.3075 | 0.1767 | ±0.3533 | -1.741 | 0.0817 | . |
| Kidney disease | +0.2704 | 0.2798 | ±0.5597 | +0.966 | 0.3338 |  |
| Circulatory disease | +0.1041 | 0.2386 | ±0.4772 | +0.436 | 0.6625 |  |
| **Time 54-69, pooled (%)** | **+0.0660** | 0.0320 | ±0.0640 | **+2.063** | **0.0391** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **628**, R² = **0.2901**, Adj R² = **0.2739**, F-statistic = **17.89** (p = **1.90e-37**), Residual SE = **2.039** on **613** df, AIC = **2691.8**, BIC = **2758.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5802** | 0.6349 | ±1.2699 | **+37.137** | **6.99e-302** | *** |
| Education: graduate level (vs college) | +0.0677 | 0.1765 | ±0.3529 | +0.384 | 0.7013 |  |
| Education: high school or below (vs college) | +0.1104 | 0.3051 | ±0.6101 | +0.362 | 0.7175 |  |
| Site: UCSD (vs UAB) | -0.0959 | 0.2123 | ±0.4245 | -0.452 | 0.6513 |  |
| **Site: UW (vs UAB)** | **-0.9940** | 0.1902 | ±0.3805 | **-5.225** | **1.74e-07** | *** |
| Season: spring (vs autumn) | -0.0685 | 0.2190 | ±0.4380 | -0.313 | 0.7546 |  |
| **Season: summer (vs autumn)** | **+2.3010** | 0.2548 | ±0.5097 | **+9.029** | **1.73e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0384** | 0.2278 | ±0.4557 | **-4.558** | **5.17e-06** | *** |
| Age (years) | +0.0134 | 0.0078 | ±0.0156 | +1.712 | 0.0869 | . |
| BMI (kg/m2) | +0.0038 | 0.0119 | ±0.0238 | +0.318 | 0.7504 |  |
| Hypertension | +0.3338 | 0.1821 | ±0.3642 | +1.833 | 0.0668 | . |
| High cholesterol | -0.3072 | 0.1765 | ±0.3529 | -1.741 | 0.0817 | . |
| Kidney disease | +0.2698 | 0.2792 | ±0.5584 | +0.966 | 0.3339 |  |
| Circulatory disease | +0.1056 | 0.2381 | ±0.4763 | +0.443 | 0.6575 |  |
| **Avg. daily time 54-69 (%)** | **+0.0726** | 0.0312 | ±0.0625 | **+2.324** | **0.0201** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **628**, R² = **0.2904**, Adj R² = **0.2742**, F-statistic = **17.92** (p = **1.70e-37**), Residual SE = **2.039** on **613** df, AIC = **2691.6**, BIC = **2758.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5145** | 0.6377 | ±1.2753 | **+36.876** | **1.11e-297** | *** |
| Education: graduate level (vs college) | +0.0625 | 0.1763 | ±0.3526 | +0.355 | 0.7228 |  |
| Education: high school or below (vs college) | +0.1221 | 0.3044 | ±0.6087 | +0.401 | 0.6883 |  |
| Site: UCSD (vs UAB) | -0.0742 | 0.2121 | ±0.4243 | -0.350 | 0.7264 |  |
| **Site: UW (vs UAB)** | **-0.9862** | 0.1901 | ±0.3803 | **-5.187** | **2.14e-07** | *** |
| Season: spring (vs autumn) | -0.0643 | 0.2195 | ±0.4391 | -0.293 | 0.7696 |  |
| **Season: summer (vs autumn)** | **+2.2934** | 0.2558 | ±0.5115 | **+8.967** | **3.05e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0365** | 0.2274 | ±0.4547 | **-4.559** | **5.15e-06** | *** |
| Age (years) | +0.0138 | 0.0078 | ±0.0156 | +1.763 | 0.0779 | . |
| BMI (kg/m2) | +0.0041 | 0.0119 | ±0.0238 | +0.341 | 0.7329 |  |
| Hypertension | +0.3363 | 0.1820 | ±0.3639 | +1.848 | 0.0645 | . |
| High cholesterol | -0.3004 | 0.1766 | ±0.3531 | -1.702 | 0.0888 | . |
| Kidney disease | +0.2691 | 0.2800 | ±0.5600 | +0.961 | 0.3365 |  |
| Circulatory disease | +0.1027 | 0.2382 | ±0.4763 | +0.431 | 0.6664 |  |
| **Time < 70 (%)** | **+0.0625** | 0.0268 | ±0.0537 | **+2.328** | **0.0199** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **628**, R² = **0.2907**, Adj R² = **0.2745**, F-statistic = **17.94** (p = **1.51e-37**), Residual SE = **2.038** on **613** df, AIC = **2691.3**, BIC = **2758.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5685** | 0.6350 | ±1.2700 | **+37.117** | **1.51e-301** | *** |
| Education: graduate level (vs college) | +0.0689 | 0.1761 | ±0.3522 | +0.391 | 0.6958 |  |
| Education: high school or below (vs college) | +0.1192 | 0.3048 | ±0.6096 | +0.391 | 0.6958 |  |
| Site: UCSD (vs UAB) | -0.0835 | 0.2120 | ±0.4241 | -0.394 | 0.6936 |  |
| **Site: UW (vs UAB)** | **-0.9825** | 0.1901 | ±0.3801 | **-5.169** | **2.35e-07** | *** |
| Season: spring (vs autumn) | -0.0655 | 0.2193 | ±0.4386 | -0.299 | 0.7651 |  |
| **Season: summer (vs autumn)** | **+2.2964** | 0.2556 | ±0.5112 | **+8.984** | **2.61e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0406** | 0.2273 | ±0.4547 | **-4.577** | **4.71e-06** | *** |
| Age (years) | +0.0133 | 0.0078 | ±0.0157 | +1.696 | 0.0899 | . |
| BMI (kg/m2) | +0.0039 | 0.0119 | ±0.0238 | +0.327 | 0.7439 |  |
| Hypertension | +0.3365 | 0.1818 | ±0.3637 | +1.851 | 0.0642 | . |
| High cholesterol | -0.3017 | 0.1763 | ±0.3527 | -1.711 | 0.0871 | . |
| Kidney disease | +0.2676 | 0.2792 | ±0.5583 | +0.958 | 0.3378 |  |
| Circulatory disease | +0.1029 | 0.2377 | ±0.4755 | +0.433 | 0.6653 |  |
| **Avg. daily time < 70 (%)** | **+0.0633** | 0.0273 | ±0.0546 | **+2.318** | **0.0205** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **628**, R² = **0.2851**, Adj R² = **0.2688**, F-statistic = **17.46** (p = **1.47e-36**), Residual SE = **2.046** on **613** df, AIC = **2696.2**, BIC = **2762.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6798** | 2.0489 | ±4.0979 | **+11.557** | **6.79e-31** | *** |
| Education: graduate level (vs college) | +0.0406 | 0.1757 | ±0.3514 | +0.231 | 0.8172 |  |
| Education: high school or below (vs college) | +0.1071 | 0.3135 | ±0.6270 | +0.342 | 0.7327 |  |
| Site: UCSD (vs UAB) | -0.1239 | 0.2161 | ±0.4322 | -0.573 | 0.5664 |  |
| **Site: UW (vs UAB)** | **-1.0361** | 0.1939 | ±0.3877 | **-5.344** | **9.07e-08** | *** |
| Season: spring (vs autumn) | -0.0804 | 0.2205 | ±0.4409 | -0.365 | 0.7154 |  |
| **Season: summer (vs autumn)** | **+2.3005** | 0.2566 | ±0.5133 | **+8.964** | **3.13e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0198** | 0.2290 | ±0.4581 | **-4.453** | **8.49e-06** | *** |
| Age (years) | +0.0145 | 0.0079 | ±0.0158 | +1.840 | 0.0657 | . |
| BMI (kg/m2) | +0.0041 | 0.0118 | ±0.0237 | +0.350 | 0.7264 |  |
| Hypertension | +0.3105 | 0.1828 | ±0.3655 | +1.699 | 0.0893 | . |
| High cholesterol | -0.3144 | 0.1763 | ±0.3526 | -1.783 | 0.0745 | . |
| Kidney disease | +0.2877 | 0.2835 | ±0.5670 | +1.015 | 0.3102 |  |
| Circulatory disease | +0.0963 | 0.2390 | ±0.4781 | +0.403 | 0.6871 |  |
| Time 54-250, pooled (%) | -0.0003 | 0.0195 | ±0.0391 | -0.016 | 0.9871 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **628**, R² = **0.2851**, Adj R² = **0.2688**, F-statistic = **17.46** (p = **1.47e-36**), Residual SE = **2.046** on **613** df, AIC = **2696.2**, BIC = **2762.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6120** | 2.3459 | ±4.6917 | **+10.065** | **7.86e-24** | *** |
| Education: graduate level (vs college) | +0.0402 | 0.1757 | ±0.3514 | +0.229 | 0.8192 |  |
| Education: high school or below (vs college) | +0.1083 | 0.3155 | ±0.6310 | +0.343 | 0.7314 |  |
| Site: UCSD (vs UAB) | -0.1243 | 0.2160 | ±0.4321 | -0.575 | 0.5652 |  |
| **Site: UW (vs UAB)** | **-1.0369** | 0.1940 | ±0.3880 | **-5.345** | **9.05e-08** | *** |
| Season: spring (vs autumn) | -0.0801 | 0.2206 | ±0.4412 | -0.363 | 0.7166 |  |
| **Season: summer (vs autumn)** | **+2.3000** | 0.2566 | ±0.5131 | **+8.965** | **3.11e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0196** | 0.2286 | ±0.4573 | **-4.460** | **8.21e-06** | *** |
| Age (years) | +0.0145 | 0.0079 | ±0.0158 | +1.839 | 0.0659 | . |
| BMI (kg/m2) | +0.0041 | 0.0118 | ±0.0237 | +0.349 | 0.7267 |  |
| Hypertension | +0.3111 | 0.1829 | ±0.3657 | +1.701 | 0.0889 | . |
| High cholesterol | -0.3147 | 0.1764 | ±0.3528 | -1.784 | 0.0745 | . |
| Kidney disease | +0.2887 | 0.2845 | ±0.5690 | +1.015 | 0.3101 |  |
| Circulatory disease | +0.0966 | 0.2388 | ±0.4777 | +0.404 | 0.6859 |  |
| Avg. daily time 54-250 (%) | +0.0004 | 0.0225 | ±0.0450 | +0.017 | 0.9867 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **628**, R² = **0.2858**, Adj R² = **0.2695**, F-statistic = **17.52** (p = **1.10e-36**), Residual SE = **2.045** on **613** df, AIC = **2695.6**, BIC = **2762.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6453** | 0.6367 | ±1.2735 | **+37.135** | **7.66e-302** | *** |
| Education: graduate level (vs college) | +0.0365 | 0.1760 | ±0.3520 | +0.208 | 0.8356 |  |
| Education: high school or below (vs college) | +0.1261 | 0.3088 | ±0.6177 | +0.408 | 0.6830 |  |
| Site: UCSD (vs UAB) | -0.1235 | 0.2128 | ±0.4257 | -0.580 | 0.5619 |  |
| **Site: UW (vs UAB)** | **-1.0445** | 0.1915 | ±0.3830 | **-5.455** | **4.90e-08** | *** |
| Season: spring (vs autumn) | -0.0794 | 0.2195 | ±0.4391 | -0.362 | 0.7175 |  |
| **Season: summer (vs autumn)** | **+2.2970** | 0.2565 | ±0.5130 | **+8.955** | **3.38e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0220** | 0.2281 | ±0.4561 | **-4.481** | **7.41e-06** | *** |
| Age (years) | +0.0149 | 0.0079 | ±0.0158 | +1.887 | 0.0592 | . |
| BMI (kg/m2) | +0.0044 | 0.0119 | ±0.0238 | +0.370 | 0.7114 |  |
| Hypertension | +0.3263 | 0.1838 | ±0.3675 | +1.776 | 0.0757 | . |
| High cholesterol | -0.3037 | 0.1784 | ±0.3567 | -1.703 | 0.0886 | . |
| Kidney disease | +0.3256 | 0.2866 | ±0.5731 | +1.136 | 0.2558 |  |
| Circulatory disease | +0.0977 | 0.2384 | ±0.4767 | +0.410 | 0.6818 |  |
| Time 181-250, pooled (%) | -0.0074 | 0.0092 | ±0.0185 | -0.796 | 0.4260 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **628**, R² = **0.2858**, Adj R² = **0.2695**, F-statistic = **17.52** (p = **1.11e-36**), Residual SE = **2.045** on **613** df, AIC = **2695.6**, BIC = **2762.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6487** | 0.6369 | ±1.2738 | **+37.130** | **9.29e-302** | *** |
| Education: graduate level (vs college) | +0.0367 | 0.1760 | ±0.3519 | +0.209 | 0.8348 |  |
| Education: high school or below (vs college) | +0.1256 | 0.3089 | ±0.6178 | +0.407 | 0.6843 |  |
| Site: UCSD (vs UAB) | -0.1248 | 0.2130 | ±0.4260 | -0.586 | 0.5579 |  |
| **Site: UW (vs UAB)** | **-1.0454** | 0.1916 | ±0.3833 | **-5.455** | **4.90e-08** | *** |
| Season: spring (vs autumn) | -0.0798 | 0.2196 | ±0.4391 | -0.363 | 0.7164 |  |
| **Season: summer (vs autumn)** | **+2.2962** | 0.2565 | ±0.5130 | **+8.952** | **3.48e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0222** | 0.2281 | ±0.4561 | **-4.482** | **7.39e-06** | *** |
| Age (years) | +0.0148 | 0.0079 | ±0.0158 | +1.880 | 0.0601 | . |
| BMI (kg/m2) | +0.0044 | 0.0119 | ±0.0238 | +0.370 | 0.7113 |  |
| Hypertension | +0.3255 | 0.1837 | ±0.3675 | +1.772 | 0.0764 | . |
| High cholesterol | -0.3042 | 0.1783 | ±0.3566 | -1.706 | 0.0880 | . |
| Kidney disease | +0.3242 | 0.2864 | ±0.5727 | +1.132 | 0.2576 |  |
| Circulatory disease | +0.0972 | 0.2384 | ±0.4769 | +0.408 | 0.6836 |  |
| Avg. daily time 181-250 (%) | -0.0070 | 0.0090 | ±0.0179 | -0.780 | 0.4354 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **628**, R² = **0.2856**, Adj R² = **0.2693**, F-statistic = **17.51** (p = **1.18e-36**), Residual SE = **2.045** on **613** df, AIC = **2695.8**, BIC = **2762.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6542** | 0.6369 | ±1.2739 | **+37.137** | **7.16e-302** | *** |
| Education: graduate level (vs college) | +0.0354 | 0.1759 | ±0.3519 | +0.201 | 0.8407 |  |
| Education: high school or below (vs college) | +0.1272 | 0.3115 | ±0.6230 | +0.408 | 0.6831 |  |
| Site: UCSD (vs UAB) | -0.1248 | 0.2135 | ±0.4270 | -0.585 | 0.5588 |  |
| **Site: UW (vs UAB)** | **-1.0460** | 0.1924 | ±0.3847 | **-5.438** | **5.40e-08** | *** |
| Season: spring (vs autumn) | -0.0780 | 0.2196 | ±0.4393 | -0.355 | 0.7226 |  |
| **Season: summer (vs autumn)** | **+2.2941** | 0.2565 | ±0.5130 | **+8.944** | **3.77e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0210** | 0.2287 | ±0.4573 | **-4.465** | **8.01e-06** | *** |
| Age (years) | +0.0147 | 0.0079 | ±0.0158 | +1.865 | 0.0622 | . |
| BMI (kg/m2) | +0.0043 | 0.0119 | ±0.0238 | +0.359 | 0.7196 |  |
| Hypertension | +0.3245 | 0.1832 | ±0.3664 | +1.771 | 0.0765 | . |
| High cholesterol | -0.3093 | 0.1780 | ±0.3561 | -1.738 | 0.0823 | . |
| Kidney disease | +0.3171 | 0.2863 | ±0.5726 | +1.108 | 0.2680 |  |
| Circulatory disease | +0.0991 | 0.2389 | ±0.4778 | +0.415 | 0.6782 |  |
| Time > 180 (%) | -0.0044 | 0.0073 | ±0.0145 | -0.612 | 0.5404 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **628**, R² = **0.2856**, Adj R² = **0.2693**, F-statistic = **17.51** (p = **1.19e-36**), Residual SE = **2.045** on **613** df, AIC = **2695.8**, BIC = **2762.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6544** | 0.6370 | ±1.2740 | **+37.135** | **7.77e-302** | *** |
| Education: graduate level (vs college) | +0.0356 | 0.1759 | ±0.3518 | +0.202 | 0.8397 |  |
| Education: high school or below (vs college) | +0.1273 | 0.3118 | ±0.6236 | +0.408 | 0.6831 |  |
| Site: UCSD (vs UAB) | -0.1253 | 0.2137 | ±0.4273 | -0.587 | 0.5575 |  |
| **Site: UW (vs UAB)** | **-1.0459** | 0.1924 | ±0.3848 | **-5.436** | **5.44e-08** | *** |
| Season: spring (vs autumn) | -0.0775 | 0.2197 | ±0.4394 | -0.353 | 0.7244 |  |
| **Season: summer (vs autumn)** | **+2.2946** | 0.2565 | ±0.5129 | **+8.947** | **3.65e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0204** | 0.2286 | ±0.4573 | **-4.463** | **8.07e-06** | *** |
| Age (years) | +0.0147 | 0.0079 | ±0.0158 | +1.863 | 0.0624 | . |
| BMI (kg/m2) | +0.0043 | 0.0119 | ±0.0238 | +0.358 | 0.7204 |  |
| Hypertension | +0.3239 | 0.1832 | ±0.3665 | +1.768 | 0.0771 | . |
| High cholesterol | -0.3091 | 0.1781 | ±0.3562 | -1.736 | 0.0826 | . |
| Kidney disease | +0.3173 | 0.2866 | ±0.5733 | +1.107 | 0.2683 |  |
| Circulatory disease | +0.0990 | 0.2389 | ±0.4778 | +0.414 | 0.6787 |  |
| Avg. daily time > 180 (%) | -0.0044 | 0.0073 | ±0.0146 | -0.598 | 0.5498 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **628**, R² = **0.2856**, Adj R² = **0.2693**, F-statistic = **17.50** (p = **1.20e-36**), Residual SE = **2.045** on **613** df, AIC = **2695.8**, BIC = **2762.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6539** | 0.6369 | ±1.2739 | **+37.138** | **6.98e-302** | *** |
| Education: graduate level (vs college) | +0.0342 | 0.1757 | ±0.3515 | +0.195 | 0.8457 |  |
| Education: high school or below (vs college) | +0.1210 | 0.3105 | ±0.6211 | +0.390 | 0.6968 |  |
| Site: UCSD (vs UAB) | -0.1270 | 0.2152 | ±0.4304 | -0.590 | 0.5550 |  |
| **Site: UW (vs UAB)** | **-1.0445** | 0.1927 | ±0.3853 | **-5.421** | **5.92e-08** | *** |
| Season: spring (vs autumn) | -0.0776 | 0.2196 | ±0.4391 | -0.353 | 0.7239 |  |
| **Season: summer (vs autumn)** | **+2.2896** | 0.2571 | ±0.5141 | **+8.906** | **5.27e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0184** | 0.2288 | ±0.4577 | **-4.451** | **8.57e-06** | *** |
| Age (years) | +0.0145 | 0.0079 | ±0.0157 | +1.844 | 0.0652 | . |
| BMI (kg/m2) | +0.0044 | 0.0120 | ±0.0239 | +0.371 | 0.7105 |  |
| Hypertension | +0.3241 | 0.1822 | ±0.3644 | +1.779 | 0.0753 | . |
| High cholesterol | -0.3096 | 0.1786 | ±0.3571 | -1.734 | 0.0830 | . |
| Kidney disease | +0.2986 | 0.2811 | ±0.5622 | +1.062 | 0.2881 |  |
| Circulatory disease | +0.1002 | 0.2393 | ±0.4787 | +0.419 | 0.6755 |  |
| Nocturnal time > 180 (%) | -0.0045 | 0.0089 | ±0.0178 | -0.504 | 0.6142 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **628**, R² = **0.2852**, Adj R² = **0.2689**, F-statistic = **17.47** (p = **1.39e-36**), Residual SE = **2.046** on **613** df, AIC = **2696.1**, BIC = **2762.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6554** | 0.6389 | ±1.2779 | **+37.023** | **4.87e-300** | *** |
| Education: graduate level (vs college) | +0.0369 | 0.1769 | ±0.3537 | +0.208 | 0.8349 |  |
| Education: high school or below (vs college) | +0.1147 | 0.3087 | ±0.6173 | +0.371 | 0.7103 |  |
| Site: UCSD (vs UAB) | -0.1217 | 0.2120 | ±0.4239 | -0.574 | 0.5659 |  |
| **Site: UW (vs UAB)** | **-1.0386** | 0.1911 | ±0.3822 | **-5.435** | **5.48e-08** | *** |
| Season: spring (vs autumn) | -0.0827 | 0.2204 | ±0.4408 | -0.375 | 0.7073 |  |
| **Season: summer (vs autumn)** | **+2.2986** | 0.2570 | ±0.5140 | **+8.943** | **3.77e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0251** | 0.2294 | ±0.4588 | **-4.469** | **7.87e-06** | *** |
| Age (years) | +0.0148 | 0.0078 | ±0.0157 | +1.885 | 0.0595 | . |
| BMI (kg/m2) | +0.0039 | 0.0119 | ±0.0238 | +0.330 | 0.7412 |  |
| Hypertension | +0.3184 | 0.1845 | ±0.3690 | +1.726 | 0.0844 | . |
| High cholesterol | -0.3135 | 0.1769 | ±0.3537 | -1.773 | 0.0763 | . |
| Kidney disease | +0.3029 | 0.2869 | ±0.5739 | +1.056 | 0.2911 |  |
| Circulatory disease | +0.0956 | 0.2387 | ±0.4774 | +0.401 | 0.6888 |  |
| Any reading > 250 during wear (0/1) | -0.0648 | 0.1884 | ±0.3768 | -0.344 | 0.7307 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **628**, R² = **0.2852**, Adj R² = **0.2689**, F-statistic = **17.47** (p = **1.41e-36**), Residual SE = **2.046** on **613** df, AIC = **2696.1**, BIC = **2762.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6565** | 0.6356 | ±1.2712 | **+37.219** | **3.36e-303** | *** |
| Education: graduate level (vs college) | +0.0377 | 0.1758 | ±0.3515 | +0.215 | 0.8301 |  |
| Education: high school or below (vs college) | +0.1160 | 0.3141 | ±0.6283 | +0.369 | 0.7119 |  |
| Site: UCSD (vs UAB) | -0.1252 | 0.2151 | ±0.4301 | -0.582 | 0.5604 |  |
| **Site: UW (vs UAB)** | **-1.0411** | 0.1933 | ±0.3867 | **-5.385** | **7.25e-08** | *** |
| Season: spring (vs autumn) | -0.0785 | 0.2202 | ±0.4404 | -0.356 | 0.7215 |  |
| **Season: summer (vs autumn)** | **+2.2960** | 0.2568 | ±0.5136 | **+8.942** | **3.83e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0196** | 0.2293 | ±0.4586 | **-4.447** | **8.72e-06** | *** |
| Age (years) | +0.0145 | 0.0079 | ±0.0158 | +1.839 | 0.0660 | . |
| BMI (kg/m2) | +0.0041 | 0.0119 | ±0.0237 | +0.347 | 0.7285 |  |
| Hypertension | +0.3151 | 0.1825 | ±0.3650 | +1.727 | 0.0842 | . |
| High cholesterol | -0.3159 | 0.1765 | ±0.3531 | -1.789 | 0.0736 | . |
| Kidney disease | +0.2945 | 0.2831 | ±0.5662 | +1.040 | 0.2982 |  |
| Circulatory disease | +0.0983 | 0.2395 | ±0.4789 | +0.411 | 0.6814 |  |
| Time > 250 (%) | -0.0045 | 0.0204 | ±0.0409 | -0.218 | 0.8274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 628)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **628**, R² = **0.2852**, Adj R² = **0.2689**, F-statistic = **17.47** (p = **1.41e-36**), Residual SE = **2.046** on **613** df, AIC = **2696.2**, BIC = **2762.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6551** | 0.6356 | ±1.2712 | **+37.217** | **3.63e-303** | *** |
| Education: graduate level (vs college) | +0.0377 | 0.1757 | ±0.3515 | +0.214 | 0.8302 |  |
| Education: high school or below (vs college) | +0.1168 | 0.3166 | ±0.6331 | +0.369 | 0.7121 |  |
| Site: UCSD (vs UAB) | -0.1249 | 0.2152 | ±0.4303 | -0.581 | 0.5615 |  |
| **Site: UW (vs UAB)** | **-1.0407** | 0.1933 | ±0.3867 | **-5.383** | **7.34e-08** | *** |
| Season: spring (vs autumn) | -0.0776 | 0.2205 | ±0.4411 | -0.352 | 0.7250 |  |
| **Season: summer (vs autumn)** | **+2.2968** | 0.2566 | ±0.5133 | **+8.950** | **3.56e-19** | *** |
| **Season: winter (vs autumn)** | **-1.0188** | 0.2290 | ±0.4580 | **-4.449** | **8.62e-06** | *** |
| Age (years) | +0.0145 | 0.0079 | ±0.0158 | +1.840 | 0.0658 | . |
| BMI (kg/m2) | +0.0041 | 0.0118 | ±0.0237 | +0.345 | 0.7298 |  |
| Hypertension | +0.3150 | 0.1825 | ±0.3650 | +1.726 | 0.0843 | . |
| High cholesterol | -0.3156 | 0.1767 | ±0.3533 | -1.787 | 0.0740 | . |
| Kidney disease | +0.2954 | 0.2843 | ±0.5686 | +1.039 | 0.2988 |  |
| Circulatory disease | +0.0987 | 0.2393 | ±0.4785 | +0.412 | 0.6801 |  |
| Avg. daily time > 250 (%) | -0.0047 | 0.0241 | ±0.0482 | -0.196 | 0.8446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 628; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **628**, R² = **0.2308**, Adj R² = **0.2145**, F-statistic = **14.17** (p = **6.04e-28**), Residual SE = **6.193** on **614** df, AIC = **4086.2**, BIC = **4148.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3535** | 2.0334 | ±4.0669 | **+24.271** | **3.98e-130** | *** |
| Education: graduate level (vs college) | +0.2754 | 0.5418 | ±1.0835 | +0.508 | 0.6113 |  |
| Education: high school or below (vs college) | +0.7833 | 0.9697 | ±1.9395 | +0.808 | 0.4192 |  |
| **Site: UCSD (vs UAB)** | **+2.7884** | 0.6750 | ±1.3499 | **+4.131** | **3.61e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7694** | 0.5595 | ±1.1189 | **-3.163** | **0.0016** | ** |
| **Season: spring (vs autumn)** | **-2.1437** | 0.6750 | ±1.3501 | **-3.176** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+1.4137** | 0.7199 | ±1.4397 | **+1.964** | **0.0495** | * |
| **Season: winter (vs autumn)** | **-6.1418** | 0.7434 | ±1.4867 | **-8.262** | **1.43e-16** | *** |
| **Age (years)** | **-0.0583** | 0.0230 | ±0.0461 | **-2.532** | **0.0113** | * |
| BMI (kg/m2) | -0.0007 | 0.0398 | ±0.0797 | -0.019 | 0.9851 |  |
| Hypertension | +0.4854 | 0.5494 | ±1.0989 | +0.883 | 0.3770 |  |
| High cholesterol | -0.3542 | 0.5233 | ±1.0466 | -0.677 | 0.4986 |  |
| Kidney disease | +0.3261 | 0.8506 | ±1.7011 | +0.383 | 0.7014 |  |
| Circulatory disease | +1.1763 | 0.6857 | ±1.3713 | +1.716 | 0.0862 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **628**, R² = **0.2328**, Adj R² = **0.2153**, F-statistic = **13.29** (p = **1.11e-27**), Residual SE = **6.190** on **613** df, AIC = **4086.6**, BIC = **4153.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.3988** | 2.6920 | ±5.3841 | **+17.607** | **2.18e-69** | *** |
| Education: graduate level (vs college) | +0.3242 | 0.5434 | ±1.0868 | +0.597 | 0.5507 |  |
| Education: high school or below (vs college) | +0.6512 | 0.9723 | ±1.9447 | +0.670 | 0.5030 |  |
| **Site: UCSD (vs UAB)** | **+2.7634** | 0.6766 | ±1.3531 | **+4.084** | **4.42e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7153** | 0.5585 | ±1.1170 | **-3.071** | **0.0021** | ** |
| **Season: spring (vs autumn)** | **-2.1216** | 0.6767 | ±1.3535 | **-3.135** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.4382** | 0.7202 | ±1.4405 | **+1.997** | **0.0458** | * |
| **Season: winter (vs autumn)** | **-6.1169** | 0.7427 | ±1.4854 | **-8.236** | **1.78e-16** | *** |
| **Age (years)** | **-0.0620** | 0.0230 | ±0.0460 | **-2.698** | **0.0070** | ** |
| BMI (kg/m2) | -0.0045 | 0.0398 | ±0.0796 | -0.112 | 0.9105 |  |
| Hypertension | +0.4028 | 0.5544 | ±1.1088 | +0.727 | 0.4675 |  |
| High cholesterol | -0.3974 | 0.5237 | ±1.0474 | -0.759 | 0.4479 |  |
| Kidney disease | +0.2782 | 0.8489 | ±1.6977 | +0.328 | 0.7431 |  |
| Circulatory disease | +1.1825 | 0.6859 | ±1.3719 | +1.724 | 0.0847 | . |
| HbA1c (%) | +0.3910 | 0.3218 | ±0.6437 | +1.215 | 0.2244 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **628**, R² = **0.2313**, Adj R² = **0.2138**, F-statistic = **13.18** (p = **1.93e-27**), Residual SE = **6.196** on **613** df, AIC = **4087.8**, BIC = **4154.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.6299** | 2.3436 | ±4.6871 | **+20.751** | **1.21e-95** | *** |
| Education: graduate level (vs college) | +0.2760 | 0.5418 | ±1.0835 | +0.509 | 0.6105 |  |
| Education: high school or below (vs college) | +0.7267 | 0.9723 | ±1.9446 | +0.747 | 0.4548 |  |
| **Site: UCSD (vs UAB)** | **+2.7843** | 0.6758 | ±1.3516 | **+4.120** | **3.79e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7587** | 0.5603 | ±1.1207 | **-3.139** | **0.0017** | ** |
| **Season: spring (vs autumn)** | **-2.1558** | 0.6753 | ±1.3507 | **-3.192** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+1.4227** | 0.7200 | ±1.4401 | **+1.976** | **0.0482** | * |
| **Season: winter (vs autumn)** | **-6.1303** | 0.7426 | ±1.4853 | **-8.255** | **1.52e-16** | *** |
| **Age (years)** | **-0.0587** | 0.0230 | ±0.0460 | **-2.550** | **0.0108** | * |
| BMI (kg/m2) | -0.0017 | 0.0399 | ±0.0799 | -0.044 | 0.9651 |  |
| Hypertension | +0.4360 | 0.5581 | ±1.1161 | +0.781 | 0.4346 |  |
| High cholesterol | -0.3746 | 0.5262 | ±1.0523 | -0.712 | 0.4765 |  |
| Kidney disease | +0.2697 | 0.8506 | ±1.7012 | +0.317 | 0.7512 |  |
| Circulatory disease | +1.1692 | 0.6880 | ±1.3760 | +1.699 | 0.0893 | . |
| Mean glucose (mg/dL) | +0.0067 | 0.0104 | ±0.0208 | +0.643 | 0.5203 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **628**, R² = **0.2313**, Adj R² = **0.2138**, F-statistic = **13.18** (p = **1.93e-27**), Residual SE = **6.196** on **613** df, AIC = **4087.8**, BIC = **4154.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.7032** | 3.3043 | ±6.6086 | **+14.437** | **3.04e-47** | *** |
| Education: graduate level (vs college) | +0.2760 | 0.5418 | ±1.0835 | +0.509 | 0.6105 |  |
| Education: high school or below (vs college) | +0.7267 | 0.9723 | ±1.9446 | +0.747 | 0.4548 |  |
| **Site: UCSD (vs UAB)** | **+2.7843** | 0.6758 | ±1.3516 | **+4.120** | **3.79e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7587** | 0.5603 | ±1.1207 | **-3.139** | **0.0017** | ** |
| **Season: spring (vs autumn)** | **-2.1558** | 0.6753 | ±1.3507 | **-3.192** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+1.4227** | 0.7200 | ±1.4401 | **+1.976** | **0.0482** | * |
| **Season: winter (vs autumn)** | **-6.1303** | 0.7426 | ±1.4853 | **-8.255** | **1.52e-16** | *** |
| **Age (years)** | **-0.0587** | 0.0230 | ±0.0460 | **-2.550** | **0.0108** | * |
| BMI (kg/m2) | -0.0017 | 0.0399 | ±0.0799 | -0.044 | 0.9651 |  |
| Hypertension | +0.4360 | 0.5581 | ±1.1161 | +0.781 | 0.4346 |  |
| High cholesterol | -0.3746 | 0.5262 | ±1.0523 | -0.712 | 0.4765 |  |
| Kidney disease | +0.2697 | 0.8506 | ±1.7012 | +0.317 | 0.7512 |  |
| Circulatory disease | +1.1692 | 0.6880 | ±1.3760 | +1.699 | 0.0893 | . |
| GMI (%) | +0.2800 | 0.4355 | ±0.8711 | +0.643 | 0.5203 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **628**, R² = **0.2309**, Adj R² = **0.2133**, F-statistic = **13.14** (p = **2.29e-27**), Residual SE = **6.198** on **613** df, AIC = **4088.2**, BIC = **4154.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1399** | 2.3453 | ±4.6907 | **+20.952** | **1.80e-97** | *** |
| Education: graduate level (vs college) | +0.2747 | 0.5422 | ±1.0844 | +0.507 | 0.6124 |  |
| Education: high school or below (vs college) | +0.7681 | 0.9704 | ±1.9407 | +0.792 | 0.4286 |  |
| **Site: UCSD (vs UAB)** | **+2.7861** | 0.6756 | ±1.3512 | **+4.124** | **3.73e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7673** | 0.5605 | ±1.1210 | **-3.153** | **0.0016** | ** |
| **Season: spring (vs autumn)** | **-2.1491** | 0.6757 | ±1.3513 | **-3.181** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+1.4184** | 0.7196 | ±1.4393 | **+1.971** | **0.0487** | * |
| **Season: winter (vs autumn)** | **-6.1409** | 0.7441 | ±1.4883 | **-8.252** | **1.55e-16** | *** |
| **Age (years)** | **-0.0582** | 0.0231 | ±0.0462 | **-2.520** | **0.0117** | * |
| BMI (kg/m2) | -0.0013 | 0.0401 | ±0.0802 | -0.033 | 0.9736 |  |
| Hypertension | +0.4715 | 0.5547 | ±1.1094 | +0.850 | 0.3953 |  |
| High cholesterol | -0.3624 | 0.5288 | ±1.0576 | -0.685 | 0.4932 |  |
| Kidney disease | +0.3218 | 0.8514 | ±1.7028 | +0.378 | 0.7055 |  |
| Circulatory disease | +1.1756 | 0.6872 | ±1.3744 | +1.711 | 0.0871 | . |
| Nocturnal mean 00-06h (mg/dL) | +0.0020 | 0.0106 | ±0.0211 | +0.186 | 0.8521 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **628**, R² = **0.2311**, Adj R² = **0.2135**, F-statistic = **13.16** (p = **2.12e-27**), Residual SE = **6.197** on **613** df, AIC = **4088.0**, BIC = **4154.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5168** | 2.0803 | ±4.1606 | **+23.803** | **3.11e-125** | *** |
| Education: graduate level (vs college) | +0.2664 | 0.5428 | ±1.0857 | +0.491 | 0.6236 |  |
| Education: high school or below (vs college) | +0.8414 | 0.9777 | ±1.9554 | +0.861 | 0.3894 |  |
| **Site: UCSD (vs UAB)** | **+2.7888** | 0.6763 | ±1.3526 | **+4.124** | **3.73e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7919** | 0.5625 | ±1.1250 | **-3.186** | **0.0014** | ** |
| **Season: spring (vs autumn)** | **-2.1450** | 0.6760 | ±1.3519 | **-3.173** | **0.0015** | ** |
| Season: summer (vs autumn) | +1.4033 | 0.7192 | ±1.4384 | +1.951 | 0.0510 | . |
| **Season: winter (vs autumn)** | **-6.1535** | 0.7436 | ±1.4871 | **-8.276** | **1.28e-16** | *** |
| **Age (years)** | **-0.0569** | 0.0232 | ±0.0464 | **-2.455** | **0.0141** | * |
| BMI (kg/m2) | -0.0006 | 0.0398 | ±0.0797 | -0.015 | 0.9877 |  |
| Hypertension | +0.5181 | 0.5564 | ±1.1129 | +0.931 | 0.3518 |  |
| High cholesterol | -0.3528 | 0.5239 | ±1.0478 | -0.673 | 0.5007 |  |
| Kidney disease | +0.4076 | 0.8612 | ±1.7223 | +0.473 | 0.6360 |  |
| Circulatory disease | +1.1718 | 0.6853 | ±1.3706 | +1.710 | 0.0873 | . |
| Glucose SD, pooled (mg/dL) | -0.0100 | 0.0211 | ±0.0422 | -0.472 | 0.6369 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **628**, R² = **0.2309**, Adj R² = **0.2133**, F-statistic = **13.15** (p = **2.25e-27**), Residual SE = **6.198** on **613** df, AIC = **4088.2**, BIC = **4154.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4556** | 2.0721 | ±4.1442 | **+23.867** | **6.71e-126** | *** |
| Education: graduate level (vs college) | +0.2688 | 0.5433 | ±1.0866 | +0.495 | 0.6208 |  |
| Education: high school or below (vs college) | +0.8242 | 0.9806 | ±1.9612 | +0.841 | 0.4006 |  |
| **Site: UCSD (vs UAB)** | **+2.7902** | 0.6758 | ±1.3517 | **+4.129** | **3.65e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7816** | 0.5617 | ±1.1235 | **-3.171** | **0.0015** | ** |
| **Season: spring (vs autumn)** | **-2.1426** | 0.6759 | ±1.3518 | **-3.170** | **0.0015** | ** |
| Season: summer (vs autumn) | +1.4059 | 0.7192 | ±1.4384 | +1.955 | 0.0506 | . |
| **Season: winter (vs autumn)** | **-6.1502** | 0.7434 | ±1.4868 | **-8.273** | **1.31e-16** | *** |
| **Age (years)** | **-0.0574** | 0.0232 | ±0.0465 | **-2.471** | **0.0135** | * |
| BMI (kg/m2) | -0.0007 | 0.0399 | ±0.0797 | -0.018 | 0.9859 |  |
| Hypertension | +0.5041 | 0.5560 | ±1.1120 | +0.907 | 0.3646 |  |
| High cholesterol | -0.3521 | 0.5240 | ±1.0479 | -0.672 | 0.5015 |  |
| Kidney disease | +0.3784 | 0.8637 | ±1.7273 | +0.438 | 0.6613 |  |
| Circulatory disease | +1.1715 | 0.6857 | ±1.3713 | +1.709 | 0.0875 | . |
| Avg. daily SD (mg/dL) | -0.0072 | 0.0239 | ±0.0478 | -0.299 | 0.7646 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **628**, R² = **0.2331**, Adj R² = **0.2156**, F-statistic = **13.31** (p = **1.00e-27**), Residual SE = **6.189** on **613** df, AIC = **4086.4**, BIC = **4153.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2328** | 2.1545 | ±4.3089 | **+23.316** | **3.08e-120** | *** |
| Education: graduate level (vs college) | +0.2455 | 0.5422 | ±1.0844 | +0.453 | 0.6507 |  |
| Education: high school or below (vs college) | +0.9368 | 0.9777 | ±1.9553 | +0.958 | 0.3380 |  |
| **Site: UCSD (vs UAB)** | **+2.7902** | 0.6761 | ±1.3522 | **+4.127** | **3.68e-05** | *** |
| **Site: UW (vs UAB)** | **-1.8472** | 0.5619 | ±1.1237 | **-3.288** | **0.0010** | ** |
| **Season: spring (vs autumn)** | **-2.1628** | 0.6757 | ±1.3514 | **-3.201** | **0.0014** | ** |
| Season: summer (vs autumn) | +1.4011 | 0.7207 | ±1.4413 | +1.944 | 0.0519 | . |
| **Season: winter (vs autumn)** | **-6.1720** | 0.7430 | ±1.4860 | **-8.307** | **9.83e-17** | *** |
| **Age (years)** | **-0.0523** | 0.0234 | ±0.0469 | **-2.232** | **0.0256** | * |
| BMI (kg/m2) | -0.0012 | 0.0397 | ±0.0795 | -0.031 | 0.9753 |  |
| Hypertension | +0.5530 | 0.5521 | ±1.1043 | +1.002 | 0.3166 |  |
| High cholesterol | -0.3754 | 0.5243 | ±1.0485 | -0.716 | 0.4740 |  |
| Kidney disease | +0.5875 | 0.8789 | ±1.7578 | +0.668 | 0.5039 |  |
| Circulatory disease | +1.1546 | 0.6840 | ±1.3680 | +1.688 | 0.0914 | . |
| CV (%) | -0.0583 | 0.0436 | ±0.0872 | -1.339 | 0.1806 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **628**, R² = **0.2341**, Adj R² = **0.2166**, F-statistic = **13.38** (p = **6.86e-28**), Residual SE = **6.185** on **613** df, AIC = **4085.6**, BIC = **4152.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.1777** | 2.4330 | ±4.8660 | **+19.391** | **9.26e-84** | *** |
| Education: graduate level (vs college) | +0.2624 | 0.5418 | ±1.0836 | +0.484 | 0.6281 |  |
| Education: high school or below (vs college) | +0.9614 | 0.9752 | ±1.9505 | +0.986 | 0.3242 |  |
| **Site: UCSD (vs UAB)** | **+2.8160** | 0.6744 | ±1.3489 | **+4.175** | **2.98e-05** | *** |
| **Site: UW (vs UAB)** | **-1.8272** | 0.5597 | ±1.1194 | **-3.265** | **0.0011** | ** |
| **Season: spring (vs autumn)** | **-2.1595** | 0.6753 | ±1.3506 | **-3.198** | **0.0014** | ** |
| Season: summer (vs autumn) | +1.4144 | 0.7228 | ±1.4455 | +1.957 | 0.0504 | . |
| **Season: winter (vs autumn)** | **-6.1699** | 0.7419 | ±1.4838 | **-8.316** | **9.07e-17** | *** |
| **Age (years)** | **-0.0507** | 0.0235 | ±0.0470 | **-2.157** | **0.0310** | * |
| BMI (kg/m2) | +0.0000 | 0.0397 | ±0.0794 | +0.000 | 0.9998 |  |
| Hypertension | +0.5530 | 0.5516 | ±1.1033 | +1.002 | 0.3162 |  |
| High cholesterol | -0.3764 | 0.5236 | ±1.0473 | -0.719 | 0.4722 |  |
| Kidney disease | +0.5630 | 0.8730 | ±1.7460 | +0.645 | 0.5190 |  |
| Circulatory disease | +1.1793 | 0.6812 | ±1.3624 | +1.731 | 0.0834 | . |
| Mean / SD ratio | +0.3255 | 0.2022 | ±0.4045 | +1.610 | 0.1075 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **628**, R² = **0.2331**, Adj R² = **0.2156**, F-statistic = **13.31** (p = **1.00e-27**), Residual SE = **6.189** on **613** df, AIC = **4086.4**, BIC = **4153.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5645** | 2.4503 | ±4.9007 | **+19.411** | **6.18e-84** | *** |
| Education: graduate level (vs college) | +0.2587 | 0.5426 | ±1.0853 | +0.477 | 0.6336 |  |
| Education: high school or below (vs college) | +0.9520 | 0.9781 | ±1.9563 | +0.973 | 0.3304 |  |
| **Site: UCSD (vs UAB)** | **+2.8358** | 0.6745 | ±1.3491 | **+4.204** | **2.62e-05** | *** |
| **Site: UW (vs UAB)** | **-1.8031** | 0.5593 | ±1.1186 | **-3.224** | **0.0013** | ** |
| **Season: spring (vs autumn)** | **-2.1455** | 0.6745 | ±1.3490 | **-3.181** | **0.0015** | ** |
| Season: summer (vs autumn) | +1.3894 | 0.7216 | ±1.4431 | +1.925 | 0.0542 | . |
| **Season: winter (vs autumn)** | **-6.1661** | 0.7426 | ±1.4851 | **-8.304** | **1.01e-16** | *** |
| **Age (years)** | **-0.0515** | 0.0236 | ±0.0473 | **-2.181** | **0.0292** | * |
| BMI (kg/m2) | +0.0002 | 0.0397 | ±0.0794 | +0.004 | 0.9969 |  |
| Hypertension | +0.5238 | 0.5510 | ±1.1020 | +0.951 | 0.3418 |  |
| High cholesterol | -0.3627 | 0.5237 | ±1.0474 | -0.693 | 0.4885 |  |
| Kidney disease | +0.5071 | 0.8701 | ±1.7402 | +0.583 | 0.5600 |  |
| Circulatory disease | +1.1666 | 0.6836 | ±1.3672 | +1.707 | 0.0879 | . |
| Avg. daily mean/SD | +0.2215 | 0.1654 | ±0.3308 | +1.339 | 0.1806 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **628**, R² = **0.2309**, Adj R² = **0.2133**, F-statistic = **13.14** (p = **2.28e-27**), Residual SE = **6.198** on **613** df, AIC = **4088.2**, BIC = **4154.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5948** | 2.2371 | ±4.4742 | **+22.169** | **6.82e-109** | *** |
| Education: graduate level (vs college) | +0.2726 | 0.5436 | ±1.0871 | +0.501 | 0.6160 |  |
| Education: high school or below (vs college) | +0.8050 | 0.9687 | ±1.9373 | +0.831 | 0.4060 |  |
| **Site: UCSD (vs UAB)** | **+2.7940** | 0.6756 | ±1.3512 | **+4.135** | **3.54e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7860** | 0.5672 | ±1.1344 | **-3.149** | **0.0016** | ** |
| **Season: spring (vs autumn)** | **-2.1447** | 0.6757 | ±1.3515 | **-3.174** | **0.0015** | ** |
| Season: summer (vs autumn) | +1.4087 | 0.7198 | ±1.4397 | +1.957 | 0.0503 | . |
| **Season: winter (vs autumn)** | **-6.1468** | 0.7426 | ±1.4851 | **-8.278** | **1.25e-16** | *** |
| **Age (years)** | **-0.0583** | 0.0231 | ±0.0462 | **-2.525** | **0.0116** | * |
| BMI (kg/m2) | -0.0004 | 0.0398 | ±0.0797 | -0.009 | 0.9928 |  |
| Hypertension | +0.4920 | 0.5525 | ±1.1051 | +0.890 | 0.3732 |  |
| High cholesterol | -0.3584 | 0.5232 | ±1.0465 | -0.685 | 0.4934 |  |
| Kidney disease | +0.3317 | 0.8519 | ±1.7038 | +0.389 | 0.6970 |  |
| Circulatory disease | +1.1747 | 0.6865 | ±1.3730 | +1.711 | 0.0871 | . |
| MAG (mg/dL/h) | -0.0060 | 0.0247 | ±0.0494 | -0.245 | 0.8068 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **628**, R² = **0.2310**, Adj R² = **0.2134**, F-statistic = **13.15** (p = **2.20e-27**), Residual SE = **6.197** on **613** df, AIC = **4088.1**, BIC = **4154.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5635** | 2.1059 | ±4.2117 | **+23.536** | **1.75e-122** | *** |
| Education: graduate level (vs college) | +0.2663 | 0.5442 | ±1.0883 | +0.489 | 0.6246 |  |
| Education: high school or below (vs college) | +0.8357 | 0.9793 | ±1.9585 | +0.853 | 0.3935 |  |
| **Site: UCSD (vs UAB)** | **+2.7912** | 0.6755 | ±1.3511 | **+4.132** | **3.60e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7841** | 0.5617 | ±1.1235 | **-3.176** | **0.0015** | ** |
| **Season: spring (vs autumn)** | **-2.1424** | 0.6760 | ±1.3520 | **-3.169** | **0.0015** | ** |
| Season: summer (vs autumn) | +1.4066 | 0.7191 | ±1.4383 | +1.956 | 0.0505 | . |
| **Season: winter (vs autumn)** | **-6.1514** | 0.7424 | ±1.4848 | **-8.286** | **1.17e-16** | *** |
| **Age (years)** | **-0.0572** | 0.0233 | ±0.0466 | **-2.458** | **0.0140** | * |
| BMI (kg/m2) | -0.0011 | 0.0399 | ±0.0798 | -0.028 | 0.9773 |  |
| Hypertension | +0.5047 | 0.5555 | ±1.1111 | +0.908 | 0.3636 |  |
| High cholesterol | -0.3532 | 0.5239 | ±1.0478 | -0.674 | 0.5002 |  |
| Kidney disease | +0.3881 | 0.8630 | ±1.7259 | +0.450 | 0.6529 |  |
| Circulatory disease | +1.1749 | 0.6859 | ±1.3719 | +1.713 | 0.0867 | . |
| Avg. daily range (mg/dL) | -0.0024 | 0.0063 | ±0.0126 | -0.382 | 0.7022 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **628**, R² = **0.2310**, Adj R² = **0.2135**, F-statistic = **13.16** (p = **2.15e-27**), Residual SE = **6.197** on **613** df, AIC = **4088.1**, BIC = **4154.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4436** | 2.0693 | ±4.1387 | **+23.894** | **3.57e-126** | *** |
| Education: graduate level (vs college) | +0.2695 | 0.5426 | ±1.0852 | +0.497 | 0.6194 |  |
| Education: high school or below (vs college) | +0.7991 | 0.9712 | ±1.9424 | +0.823 | 0.4106 |  |
| **Site: UCSD (vs UAB)** | **+2.7831** | 0.6772 | ±1.3544 | **+4.110** | **3.96e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7871** | 0.5629 | ±1.1258 | **-3.175** | **0.0015** | ** |
| **Season: spring (vs autumn)** | **-2.1471** | 0.6763 | ±1.3527 | **-3.175** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+1.4152** | 0.7212 | ±1.4424 | **+1.962** | **0.0497** | * |
| **Season: winter (vs autumn)** | **-6.1421** | 0.7445 | ±1.4890 | **-8.250** | **1.59e-16** | *** |
| **Age (years)** | **-0.0578** | 0.0231 | ±0.0461 | **-2.509** | **0.0121** | * |
| BMI (kg/m2) | -0.0004 | 0.0398 | ±0.0796 | -0.010 | 0.9921 |  |
| Hypertension | +0.5122 | 0.5555 | ±1.1110 | +0.922 | 0.3565 |  |
| High cholesterol | -0.3527 | 0.5241 | ±1.0483 | -0.673 | 0.5010 |  |
| Kidney disease | +0.3718 | 0.8532 | ±1.7063 | +0.436 | 0.6630 |  |
| Circulatory disease | +1.1862 | 0.6898 | ±1.3797 | +1.720 | 0.0855 | . |
| SD of daily means (mg/dL) | -0.0153 | 0.0379 | ±0.0758 | -0.404 | 0.6862 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **628**, R² = **0.2310**, Adj R² = **0.2135**, F-statistic = **13.16** (p = **2.15e-27**), Residual SE = **6.197** on **613** df, AIC = **4088.1**, BIC = **4154.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1518** | 2.7538 | ±5.5076 | **+18.212** | **4.16e-74** | *** |
| Education: graduate level (vs college) | +0.2877 | 0.5425 | ±1.0850 | +0.530 | 0.5959 |  |
| Education: high school or below (vs college) | +0.7489 | 0.9752 | ±1.9504 | +0.768 | 0.4425 |  |
| **Site: UCSD (vs UAB)** | **+2.7963** | 0.6780 | ±1.3560 | **+4.124** | **3.72e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7451** | 0.5641 | ±1.1282 | **-3.094** | **0.0020** | ** |
| **Season: spring (vs autumn)** | **-2.1458** | 0.6759 | ±1.3518 | **-3.175** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+1.4242** | 0.7193 | ±1.4386 | **+1.980** | **0.0477** | * |
| **Season: winter (vs autumn)** | **-6.1418** | 0.7438 | ±1.4877 | **-8.257** | **1.49e-16** | *** |
| **Age (years)** | **-0.0588** | 0.0231 | ±0.0461 | **-2.552** | **0.0107** | * |
| BMI (kg/m2) | -0.0010 | 0.0399 | ±0.0799 | -0.025 | 0.9800 |  |
| Hypertension | +0.4632 | 0.5547 | ±1.1093 | +0.835 | 0.4037 |  |
| High cholesterol | -0.3620 | 0.5236 | ±1.0472 | -0.691 | 0.4893 |  |
| Kidney disease | +0.2698 | 0.8533 | ±1.7066 | +0.316 | 0.7519 |  |
| Circulatory disease | +1.1721 | 0.6882 | ±1.3763 | +1.703 | 0.0885 | . |
| Time in range 70-180, pooled (%) | -0.0083 | 0.0203 | ±0.0407 | -0.406 | 0.6849 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **628**, R² = **0.2310**, Adj R² = **0.2135**, F-statistic = **13.15** (p = **2.16e-27**), Residual SE = **6.197** on **613** df, AIC = **4088.1**, BIC = **4154.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1277** | 2.7953 | ±5.5906 | **+17.933** | **6.53e-72** | *** |
| Education: graduate level (vs college) | +0.2878 | 0.5426 | ±1.0853 | +0.530 | 0.5959 |  |
| Education: high school or below (vs college) | +0.7489 | 0.9757 | ±1.9515 | +0.768 | 0.4428 |  |
| **Site: UCSD (vs UAB)** | **+2.7957** | 0.6781 | ±1.3562 | **+4.123** | **3.74e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7455** | 0.5644 | ±1.1288 | **-3.093** | **0.0020** | ** |
| **Season: spring (vs autumn)** | **-2.1469** | 0.6759 | ±1.3518 | **-3.176** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+1.4236** | 0.7193 | ±1.4386 | **+1.979** | **0.0478** | * |
| **Season: winter (vs autumn)** | **-6.1432** | 0.7441 | ±1.4882 | **-8.256** | **1.51e-16** | *** |
| **Age (years)** | **-0.0588** | 0.0231 | ±0.0461 | **-2.552** | **0.0107** | * |
| BMI (kg/m2) | -0.0010 | 0.0399 | ±0.0799 | -0.025 | 0.9802 |  |
| Hypertension | +0.4647 | 0.5547 | ±1.1095 | +0.838 | 0.4022 |  |
| High cholesterol | -0.3625 | 0.5238 | ±1.0476 | -0.692 | 0.4889 |  |
| Kidney disease | +0.2704 | 0.8527 | ±1.7053 | +0.317 | 0.7512 |  |
| Circulatory disease | +1.1724 | 0.6883 | ±1.3766 | +1.703 | 0.0885 | . |
| Avg. daily time in range 70-180 (%) | -0.0079 | 0.0207 | ±0.0413 | -0.384 | 0.7007 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **628**, R² = **0.2337**, Adj R² = **0.2162**, F-statistic = **13.35** (p = **7.96e-28**), Residual SE = **6.186** on **613** df, AIC = **4085.9**, BIC = **4152.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.6672** | 2.0407 | ±4.0813 | **+24.339** | **7.61e-131** | *** |
| Education: graduate level (vs college) | +0.2608 | 0.5405 | ±1.0810 | +0.483 | 0.6294 |  |
| Education: high school or below (vs college) | +0.7092 | 0.9700 | ±1.9399 | +0.731 | 0.4647 |  |
| **Site: UCSD (vs UAB)** | **+2.6375** | 0.6822 | ±1.3644 | **+3.866** | **1.11e-04** | *** |
| **Site: UW (vs UAB)** | **-1.8918** | 0.5641 | ±1.1282 | **-3.354** | **7.97e-04** | *** |
| **Season: spring (vs autumn)** | **-2.1754** | 0.6753 | ±1.3507 | **-3.221** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+1.4554** | 0.7223 | ±1.4446 | **+2.015** | **0.0439** | * |
| **Season: winter (vs autumn)** | **-6.1182** | 0.7443 | ±1.4885 | **-8.221** | **2.03e-16** | *** |
| **Age (years)** | **-0.0579** | 0.0230 | ±0.0460 | **-2.515** | **0.0119** | * |
| BMI (kg/m2) | -0.0016 | 0.0399 | ±0.0798 | -0.040 | 0.9679 |  |
| Hypertension | +0.4436 | 0.5513 | ±1.1026 | +0.805 | 0.4210 |  |
| High cholesterol | -0.4064 | 0.5268 | ±1.0536 | -0.771 | 0.4404 |  |
| Kidney disease | +0.3422 | 0.8513 | ±1.7026 | +0.402 | 0.6878 |  |
| Circulatory disease | +1.1836 | 0.6860 | ±1.3720 | +1.725 | 0.0845 | . |
| **Time < 54 (%)** | **-0.4365** | 0.2079 | ±0.4157 | **-2.100** | **0.0357** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **628**, R² = **0.2350**, Adj R² = **0.2175**, F-statistic = **13.45** (p = **4.91e-28**), Residual SE = **6.181** on **613** df, AIC = **4084.8**, BIC = **4151.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5520** | 2.0217 | ±4.0434 | **+24.510** | **1.16e-132** | *** |
| Education: graduate level (vs college) | +0.2303 | 0.5409 | ±1.0818 | +0.426 | 0.6703 |  |
| Education: high school or below (vs college) | +0.6947 | 0.9666 | ±1.9332 | +0.719 | 0.4723 |  |
| **Site: UCSD (vs UAB)** | **+2.6336** | 0.6793 | ±1.3585 | **+3.877** | **1.06e-04** | *** |
| **Site: UW (vs UAB)** | **-1.9337** | 0.5658 | ±1.1316 | **-3.417** | **6.32e-04** | *** |
| **Season: spring (vs autumn)** | **-2.1867** | 0.6745 | ±1.3490 | **-3.242** | **0.0012** | ** |
| **Season: summer (vs autumn)** | **+1.4573** | 0.7225 | ±1.4449 | **+2.017** | **0.0437** | * |
| **Season: winter (vs autumn)** | **-6.0978** | 0.7436 | ±1.4871 | **-8.201** | **2.38e-16** | *** |
| **Age (years)** | **-0.0559** | 0.0230 | ±0.0459 | **-2.435** | **0.0149** | * |
| BMI (kg/m2) | -0.0012 | 0.0395 | ±0.0790 | -0.031 | 0.9750 |  |
| Hypertension | +0.4304 | 0.5498 | ±1.0996 | +0.783 | 0.4338 |  |
| High cholesterol | -0.4165 | 0.5260 | ±1.0520 | -0.792 | 0.4285 |  |
| Kidney disease | +0.3702 | 0.8519 | ±1.7037 | +0.435 | 0.6639 |  |
| Circulatory disease | +1.1913 | 0.6823 | ±1.3646 | +1.746 | 0.0808 | . |
| **Avg. daily time < 54 (%)** | **-0.6116** | 0.2975 | ±0.5949 | **-2.056** | **0.0398** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **628**, R² = **0.2317**, Adj R² = **0.2142**, F-statistic = **13.21** (p = **1.65e-27**), Residual SE = **6.194** on **613** df, AIC = **4087.5**, BIC = **4154.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4884** | 2.0446 | ±4.0893 | **+24.204** | **2.01e-129** | *** |
| Education: graduate level (vs college) | +0.2452 | 0.5414 | ±1.0828 | +0.453 | 0.6506 |  |
| Education: high school or below (vs college) | +0.7775 | 0.9690 | ±1.9380 | +0.802 | 0.4223 |  |
| **Site: UCSD (vs UAB)** | **+2.7458** | 0.6815 | ±1.3630 | **+4.029** | **5.60e-05** | *** |
| **Site: UW (vs UAB)** | **-1.8187** | 0.5610 | ±1.1220 | **-3.242** | **0.0012** | ** |
| **Season: spring (vs autumn)** | **-2.1609** | 0.6756 | ±1.3511 | **-3.199** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+1.4150** | 0.7203 | ±1.4406 | **+1.964** | **0.0495** | * |
| **Season: winter (vs autumn)** | **-6.1217** | 0.7448 | ±1.4896 | **-8.219** | **2.05e-16** | *** |
| **Age (years)** | **-0.0574** | 0.0230 | ±0.0459 | **-2.499** | **0.0125** | * |
| BMI (kg/m2) | -0.0004 | 0.0399 | ±0.0798 | -0.011 | 0.9910 |  |
| Hypertension | +0.4559 | 0.5510 | ±1.1020 | +0.827 | 0.4080 |  |
| High cholesterol | -0.3642 | 0.5255 | ±1.0509 | -0.693 | 0.4883 |  |
| Kidney disease | +0.3514 | 0.8542 | ±1.7083 | +0.411 | 0.6808 |  |
| Circulatory disease | +1.1653 | 0.6874 | ±1.3748 | +1.695 | 0.0900 | . |
| Time 54-69, pooled (%) | -0.0941 | 0.1041 | ±0.2082 | -0.904 | 0.3662 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **628**, R² = **0.2319**, Adj R² = **0.2144**, F-statistic = **13.22** (p = **1.53e-27**), Residual SE = **6.193** on **613** df, AIC = **4087.3**, BIC = **4153.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4490** | 2.0355 | ±4.0710 | **+24.293** | **2.31e-130** | *** |
| Education: graduate level (vs college) | +0.2375 | 0.5418 | ±1.0836 | +0.438 | 0.6611 |  |
| Education: high school or below (vs college) | +0.7795 | 0.9688 | ±1.9375 | +0.805 | 0.4210 |  |
| **Site: UCSD (vs UAB)** | **+2.7493** | 0.6804 | ±1.3608 | **+4.041** | **5.33e-05** | *** |
| **Site: UW (vs UAB)** | **-1.8283** | 0.5612 | ±1.1224 | **-3.258** | **0.0011** | ** |
| **Season: spring (vs autumn)** | **-2.1600** | 0.6757 | ±1.3515 | **-3.197** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+1.4127** | 0.7201 | ±1.4401 | **+1.962** | **0.0498** | * |
| **Season: winter (vs autumn)** | **-6.1159** | 0.7446 | ±1.4892 | **-8.214** | **2.14e-16** | *** |
| **Age (years)** | **-0.0568** | 0.0230 | ±0.0459 | **-2.474** | **0.0134** | * |
| BMI (kg/m2) | -0.0003 | 0.0398 | ±0.0796 | -0.006 | 0.9950 |  |
| Hypertension | +0.4535 | 0.5502 | ±1.1003 | +0.824 | 0.4098 |  |
| High cholesterol | -0.3644 | 0.5253 | ±1.0505 | -0.694 | 0.4878 |  |
| Kidney disease | +0.3516 | 0.8531 | ±1.7063 | +0.412 | 0.6802 |  |
| Circulatory disease | +1.1636 | 0.6869 | ±1.3737 | +1.694 | 0.0903 | . |
| Avg. daily time 54-69 (%) | -0.1007 | 0.1007 | ±0.2014 | -1.000 | 0.3174 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **628**, R² = **0.2325**, Adj R² = **0.2150**, F-statistic = **13.26** (p = **1.24e-27**), Residual SE = **6.191** on **613** df, AIC = **4086.8**, BIC = **4153.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5764** | 2.0459 | ±4.0918 | **+24.232** | **1.02e-129** | *** |
| Education: graduate level (vs college) | +0.2387 | 0.5409 | ±1.0817 | +0.441 | 0.6589 |  |
| Education: high school or below (vs college) | +0.7593 | 0.9681 | ±1.9361 | +0.784 | 0.4328 |  |
| **Site: UCSD (vs UAB)** | **+2.7057** | 0.6836 | ±1.3672 | **+3.958** | **7.55e-05** | *** |
| **Site: UW (vs UAB)** | **-1.8527** | 0.5622 | ±1.1244 | **-3.295** | **9.83e-04** | *** |
| **Season: spring (vs autumn)** | **-2.1701** | 0.6756 | ±1.3513 | **-3.212** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+1.4250** | 0.7207 | ±1.4414 | **+1.977** | **0.0480** | * |
| **Season: winter (vs autumn)** | **-6.1140** | 0.7449 | ±1.4899 | **-8.208** | **2.26e-16** | *** |
| **Age (years)** | **-0.0572** | 0.0229 | ±0.0459 | **-2.491** | **0.0127** | * |
| BMI (kg/m2) | -0.0006 | 0.0399 | ±0.0798 | -0.016 | 0.9875 |  |
| Hypertension | +0.4430 | 0.5515 | ±1.1030 | +0.803 | 0.4218 |  |
| High cholesterol | -0.3776 | 0.5264 | ±1.0529 | -0.717 | 0.4733 |  |
| Kidney disease | +0.3577 | 0.8543 | ±1.7085 | +0.419 | 0.6754 |  |
| Circulatory disease | +1.1659 | 0.6873 | ±1.3746 | +1.696 | 0.0898 | . |
| Time < 70 (%) | -0.1036 | 0.0834 | ±0.1669 | -1.241 | 0.2145 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **628**, R² = **0.2328**, Adj R² = **0.2153**, F-statistic = **13.29** (p = **1.11e-27**), Residual SE = **6.190** on **613** df, AIC = **4086.6**, BIC = **4153.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4944** | 2.0317 | ±4.0634 | **+24.361** | **4.43e-131** | *** |
| Education: graduate level (vs college) | +0.2256 | 0.5413 | ±1.0826 | +0.417 | 0.6768 |  |
| Education: high school or below (vs college) | +0.7631 | 0.9674 | ±1.9348 | +0.789 | 0.4302 |  |
| **Site: UCSD (vs UAB)** | **+2.7174** | 0.6813 | ±1.3626 | **+3.988** | **6.65e-05** | *** |
| **Site: UW (vs UAB)** | **-1.8639** | 0.5625 | ±1.1249 | **-3.314** | **9.20e-04** | *** |
| **Season: spring (vs autumn)** | **-2.1694** | 0.6756 | ±1.3512 | **-3.211** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+1.4205** | 0.7201 | ±1.4403 | **+1.973** | **0.0485** | * |
| **Season: winter (vs autumn)** | **-6.1054** | 0.7445 | ±1.4889 | **-8.201** | **2.38e-16** | *** |
| **Age (years)** | **-0.0562** | 0.0229 | ±0.0459 | **-2.451** | **0.0143** | * |
| BMI (kg/m2) | -0.0003 | 0.0397 | ±0.0795 | -0.007 | 0.9942 |  |
| Hypertension | +0.4404 | 0.5500 | ±1.0999 | +0.801 | 0.4233 |  |
| High cholesterol | -0.3767 | 0.5258 | ±1.0516 | -0.716 | 0.4737 |  |
| Kidney disease | +0.3621 | 0.8533 | ±1.7065 | +0.424 | 0.6713 |  |
| Circulatory disease | +1.1650 | 0.6858 | ±1.3716 | +1.699 | 0.0894 | . |
| Avg. daily time < 70 (%) | -0.1107 | 0.0826 | ±0.1651 | -1.341 | 0.1800 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **628**, R² = **0.2309**, Adj R² = **0.2134**, F-statistic = **13.15** (p = **2.22e-27**), Residual SE = **6.197** on **613** df, AIC = **4088.1**, BIC = **4154.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.7258** | 4.0058 | ±8.0116 | **+12.663** | **9.48e-37** | *** |
| Education: graduate level (vs college) | +0.2844 | 0.5420 | ±1.0839 | +0.525 | 0.5998 |  |
| Education: high school or below (vs college) | +0.7593 | 0.9724 | ±1.9447 | +0.781 | 0.4349 |  |
| **Site: UCSD (vs UAB)** | **+2.7968** | 0.6767 | ±1.3533 | **+4.133** | **3.58e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7508** | 0.5632 | ±1.1264 | **-3.109** | **0.0019** | ** |
| **Season: spring (vs autumn)** | **-2.1483** | 0.6756 | ±1.3512 | **-3.180** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+1.4257** | 0.7202 | ±1.4403 | **+1.980** | **0.0477** | * |
| **Season: winter (vs autumn)** | **-6.1430** | 0.7437 | ±1.4874 | **-8.260** | **1.46e-16** | *** |
| **Age (years)** | **-0.0583** | 0.0231 | ±0.0461 | **-2.529** | **0.0115** | * |
| BMI (kg/m2) | -0.0006 | 0.0399 | ±0.0799 | -0.016 | 0.9873 |  |
| Hypertension | +0.4730 | 0.5518 | ±1.1036 | +0.857 | 0.3914 |  |
| High cholesterol | -0.3483 | 0.5258 | ±1.0516 | -0.662 | 0.5077 |  |
| Kidney disease | +0.3056 | 0.8500 | ±1.6999 | +0.359 | 0.7192 |  |
| Circulatory disease | +1.1700 | 0.6894 | ±1.3788 | +1.697 | 0.0897 | . |
| Time 54-250, pooled (%) | -0.0141 | 0.0367 | ±0.0734 | -0.383 | 0.7017 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **628**, R² = **0.2310**, Adj R² = **0.2135**, F-statistic = **13.16** (p = **2.15e-27**), Residual SE = **6.197** on **613** df, AIC = **4088.0**, BIC = **4154.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.3645** | 4.8277 | ±9.6553 | **+10.640** | **1.95e-26** | *** |
| Education: graduate level (vs college) | +0.2887 | 0.5420 | ±1.0840 | +0.533 | 0.5943 |  |
| Education: high school or below (vs college) | +0.7465 | 0.9739 | ±1.9478 | +0.767 | 0.4434 |  |
| **Site: UCSD (vs UAB)** | **+2.7972** | 0.6765 | ±1.3529 | **+4.135** | **3.55e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7459** | 0.5631 | ±1.1261 | **-3.101** | **0.0019** | ** |
| **Season: spring (vs autumn)** | **-2.1539** | 0.6762 | ±1.3523 | **-3.185** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+1.4273** | 0.7198 | ±1.4396 | **+1.983** | **0.0474** | * |
| **Season: winter (vs autumn)** | **-6.1473** | 0.7442 | ±1.4884 | **-8.260** | **1.46e-16** | *** |
| **Age (years)** | **-0.0584** | 0.0231 | ±0.0461 | **-2.533** | **0.0113** | * |
| BMI (kg/m2) | -0.0005 | 0.0400 | ±0.0799 | -0.013 | 0.9898 |  |
| Hypertension | +0.4688 | 0.5524 | ±1.1047 | +0.849 | 0.3960 |  |
| High cholesterol | -0.3474 | 0.5256 | ±1.0513 | -0.661 | 0.5087 |  |
| Kidney disease | +0.2932 | 0.8501 | ±1.7001 | +0.345 | 0.7302 |  |
| Circulatory disease | +1.1661 | 0.6911 | ±1.3822 | +1.687 | 0.0915 | . |
| Avg. daily time 54-250 (%) | -0.0204 | 0.0454 | ±0.0909 | -0.450 | 0.6528 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **628**, R² = **0.2313**, Adj R² = **0.2137**, F-statistic = **13.17** (p = **1.96e-27**), Residual SE = **6.196** on **613** df, AIC = **4087.8**, BIC = **4154.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3624** | 2.0379 | ±4.0758 | **+24.222** | **1.30e-129** | *** |
| Education: graduate level (vs college) | +0.2846 | 0.5422 | ±1.0843 | +0.525 | 0.5996 |  |
| Education: high school or below (vs college) | +0.7393 | 0.9733 | ±1.9465 | +0.760 | 0.4475 |  |
| **Site: UCSD (vs UAB)** | **+2.7869** | 0.6762 | ±1.3525 | **+4.121** | **3.77e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7503** | 0.5613 | ±1.1226 | **-3.118** | **0.0018** | ** |
| **Season: spring (vs autumn)** | **-2.1456** | 0.6761 | ±1.3523 | **-3.173** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+1.4214** | 0.7196 | ±1.4391 | **+1.975** | **0.0482** | * |
| **Season: winter (vs autumn)** | **-6.1364** | 0.7434 | ±1.4868 | **-8.254** | **1.53e-16** | *** |
| **Age (years)** | **-0.0592** | 0.0231 | ±0.0461 | **-2.569** | **0.0102** | * |
| BMI (kg/m2) | -0.0014 | 0.0400 | ±0.0800 | -0.034 | 0.9727 |  |
| Hypertension | +0.4484 | 0.5558 | ±1.1117 | +0.807 | 0.4198 |  |
| High cholesterol | -0.3799 | 0.5262 | ±1.0525 | -0.722 | 0.4703 |  |
| Kidney disease | +0.2371 | 0.8555 | ±1.7110 | +0.277 | 0.7817 |  |
| Circulatory disease | +1.1731 | 0.6876 | ±1.3753 | +1.706 | 0.0880 | . |
| Time 181-250, pooled (%) | +0.0175 | 0.0307 | ±0.0614 | +0.569 | 0.5692 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **628**, R² = **0.2312**, Adj R² = **0.2137**, F-statistic = **13.17** (p = **2.00e-27**), Residual SE = **6.196** on **613** df, AIC = **4087.9**, BIC = **4154.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3542** | 2.0379 | ±4.0758 | **+24.218** | **1.44e-129** | *** |
| Education: graduate level (vs college) | +0.2838 | 0.5422 | ±1.0844 | +0.523 | 0.6007 |  |
| Education: high school or below (vs college) | +0.7426 | 0.9732 | ±1.9465 | +0.763 | 0.4455 |  |
| **Site: UCSD (vs UAB)** | **+2.7900** | 0.6767 | ±1.3535 | **+4.123** | **3.74e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7492** | 0.5617 | ±1.1235 | **-3.114** | **0.0018** | ** |
| **Season: spring (vs autumn)** | **-2.1448** | 0.6762 | ±1.3525 | **-3.172** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+1.4228** | 0.7194 | ±1.4388 | **+1.978** | **0.0480** | * |
| **Season: winter (vs autumn)** | **-6.1363** | 0.7434 | ±1.4869 | **-8.254** | **1.53e-16** | *** |
| **Age (years)** | **-0.0591** | 0.0230 | ±0.0461 | **-2.563** | **0.0104** | * |
| BMI (kg/m2) | -0.0013 | 0.0400 | ±0.0800 | -0.034 | 0.9732 |  |
| Hypertension | +0.4519 | 0.5553 | ±1.1106 | +0.814 | 0.4158 |  |
| High cholesterol | -0.3777 | 0.5262 | ±1.0524 | -0.718 | 0.4729 |  |
| Kidney disease | +0.2444 | 0.8547 | ±1.7095 | +0.286 | 0.7749 |  |
| Circulatory disease | +1.1745 | 0.6875 | ±1.3749 | +1.709 | 0.0875 | . |
| Avg. daily time 181-250 (%) | +0.0158 | 0.0299 | ±0.0598 | +0.530 | 0.5958 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **628**, R² = **0.2314**, Adj R² = **0.2138**, F-statistic = **13.18** (p = **1.88e-27**), Residual SE = **6.196** on **613** df, AIC = **4087.8**, BIC = **4154.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3380** | 2.0394 | ±4.0789 | **+24.192** | **2.70e-129** | *** |
| Education: graduate level (vs college) | +0.2906 | 0.5420 | ±1.0841 | +0.536 | 0.5918 |  |
| Education: high school or below (vs college) | +0.7244 | 0.9744 | ±1.9488 | +0.743 | 0.4572 |  |
| **Site: UCSD (vs UAB)** | **+2.7906** | 0.6760 | ±1.3521 | **+4.128** | **3.66e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7408** | 0.5623 | ±1.1246 | **-3.096** | **0.0020** | ** |
| **Season: spring (vs autumn)** | **-2.1506** | 0.6757 | ±1.3515 | **-3.183** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+1.4323** | 0.7192 | ±1.4385 | **+1.991** | **0.0464** | * |
| **Season: winter (vs autumn)** | **-6.1381** | 0.7433 | ±1.4866 | **-8.258** | **1.48e-16** | *** |
| **Age (years)** | **-0.0590** | 0.0230 | ±0.0461 | **-2.560** | **0.0105** | * |
| BMI (kg/m2) | -0.0011 | 0.0400 | ±0.0800 | -0.029 | 0.9772 |  |
| Hypertension | +0.4439 | 0.5559 | ±1.1119 | +0.798 | 0.4246 |  |
| High cholesterol | -0.3699 | 0.5241 | ±1.0482 | -0.706 | 0.4803 |  |
| Kidney disease | +0.2387 | 0.8518 | ±1.7037 | +0.280 | 0.7793 |  |
| Circulatory disease | +1.1682 | 0.6888 | ±1.3776 | +1.696 | 0.0899 | . |
| Time > 180 (%) | +0.0134 | 0.0204 | ±0.0407 | +0.658 | 0.5105 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **628**, R² = **0.2314**, Adj R² = **0.2139**, F-statistic = **13.18** (p = **1.87e-27**), Residual SE = **6.196** on **613** df, AIC = **4087.7**, BIC = **4154.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3365** | 2.0393 | ±4.0786 | **+24.193** | **2.64e-129** | *** |
| Education: graduate level (vs college) | +0.2906 | 0.5420 | ±1.0841 | +0.536 | 0.5919 |  |
| Education: high school or below (vs college) | +0.7214 | 0.9745 | ±1.9491 | +0.740 | 0.4592 |  |
| **Site: UCSD (vs UAB)** | **+2.7923** | 0.6764 | ±1.3527 | **+4.128** | **3.65e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7398** | 0.5623 | ±1.1247 | **-3.094** | **0.0020** | ** |
| **Season: spring (vs autumn)** | **-2.1525** | 0.6758 | ±1.3516 | **-3.185** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+1.4317** | 0.7191 | ±1.4382 | **+1.991** | **0.0465** | * |
| **Season: winter (vs autumn)** | **-6.1397** | 0.7434 | ±1.4868 | **-8.259** | **1.47e-16** | *** |
| **Age (years)** | **-0.0590** | 0.0230 | ±0.0461 | **-2.559** | **0.0105** | * |
| BMI (kg/m2) | -0.0011 | 0.0400 | ±0.0799 | -0.028 | 0.9777 |  |
| Hypertension | +0.4440 | 0.5555 | ±1.1109 | +0.799 | 0.4241 |  |
| High cholesterol | -0.3713 | 0.5244 | ±1.0488 | -0.708 | 0.4789 |  |
| Kidney disease | +0.2342 | 0.8520 | ±1.7040 | +0.275 | 0.7834 |  |
| Circulatory disease | +1.1682 | 0.6889 | ±1.3778 | +1.696 | 0.0899 | . |
| Avg. daily time > 180 (%) | +0.0137 | 0.0209 | ±0.0418 | +0.657 | 0.5113 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **628**, R² = **0.2310**, Adj R² = **0.2134**, F-statistic = **13.15** (p = **2.19e-27**), Residual SE = **6.197** on **613** df, AIC = **4088.1**, BIC = **4154.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3617** | 2.0348 | ±4.0697 | **+24.258** | **5.40e-130** | *** |
| Education: graduate level (vs college) | +0.2648 | 0.5420 | ±1.0840 | +0.489 | 0.6251 |  |
| Education: high school or below (vs college) | +0.8059 | 0.9728 | ±1.9456 | +0.828 | 0.4074 |  |
| **Site: UCSD (vs UAB)** | **+2.7835** | 0.6769 | ±1.3538 | **+4.112** | **3.92e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7829** | 0.5632 | ±1.1264 | **-3.166** | **0.0015** | ** |
| **Season: spring (vs autumn)** | **-2.1391** | 0.6761 | ±1.3523 | **-3.164** | **0.0016** | ** |
| Season: summer (vs autumn) | +1.3956 | 0.7189 | ±1.4379 | +1.941 | 0.0522 | . |
| **Season: winter (vs autumn)** | **-6.1395** | 0.7448 | ±1.4896 | **-8.243** | **1.68e-16** | *** |
| **Age (years)** | **-0.0583** | 0.0231 | ±0.0461 | **-2.528** | **0.0115** | * |
| BMI (kg/m2) | -0.0002 | 0.0398 | ±0.0796 | -0.006 | 0.9951 |  |
| Hypertension | +0.5079 | 0.5541 | ±1.1082 | +0.917 | 0.3593 |  |
| High cholesterol | -0.3457 | 0.5241 | ±1.0481 | -0.660 | 0.5095 |  |
| Kidney disease | +0.3439 | 0.8498 | ±1.6996 | +0.405 | 0.6857 |  |
| Circulatory disease | +1.1827 | 0.6887 | ±1.3773 | +1.717 | 0.0859 | . |
| Nocturnal time > 180 (%) | -0.0076 | 0.0215 | ±0.0431 | -0.352 | 0.7247 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **628**, R² = **0.2313**, Adj R² = **0.2138**, F-statistic = **13.18** (p = **1.93e-27**), Residual SE = **6.196** on **613** df, AIC = **4087.8**, BIC = **4154.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3890** | 2.0345 | ±4.0691 | **+24.275** | **3.56e-130** | *** |
| Education: graduate level (vs college) | +0.2556 | 0.5427 | ±1.0854 | +0.471 | 0.6377 |  |
| Education: high school or below (vs college) | +0.8225 | 0.9747 | ±1.9493 | +0.844 | 0.3988 |  |
| **Site: UCSD (vs UAB)** | **+2.8017** | 0.6761 | ±1.3523 | **+4.144** | **3.42e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7815** | 0.5598 | ±1.1195 | **-3.183** | **0.0015** | ** |
| **Season: spring (vs autumn)** | **-2.1574** | 0.6755 | ±1.3510 | **-3.194** | **0.0014** | ** |
| Season: summer (vs autumn) | +1.4044 | 0.7184 | ±1.4368 | +1.955 | 0.0506 | . |
| **Season: winter (vs autumn)** | **-6.1719** | 0.7425 | ±1.4851 | **-8.312** | **9.42e-17** | *** |
| **Age (years)** | **-0.0568** | 0.0231 | ±0.0462 | **-2.456** | **0.0141** | * |
| BMI (kg/m2) | -0.0019 | 0.0398 | ±0.0797 | -0.048 | 0.9617 |  |
| Hypertension | +0.5277 | 0.5542 | ±1.1085 | +0.952 | 0.3411 |  |
| High cholesterol | -0.3484 | 0.5240 | ±1.0480 | -0.665 | 0.5060 |  |
| Kidney disease | +0.4083 | 0.8570 | ±1.7141 | +0.476 | 0.6338 |  |
| Circulatory disease | +1.1718 | 0.6858 | ±1.3715 | +1.709 | 0.0875 | . |
| Any reading > 250 during wear (0/1) | -0.3612 | 0.5700 | ±1.1400 | -0.634 | 0.5262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **628**, R² = **0.2312**, Adj R² = **0.2137**, F-statistic = **13.17** (p = **2.01e-27**), Residual SE = **6.196** on **613** df, AIC = **4087.9**, BIC = **4154.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3120** | 2.0413 | ±4.0827 | **+24.157** | **6.33e-129** | *** |
| Education: graduate level (vs college) | +0.2906 | 0.5418 | ±1.0836 | +0.536 | 0.5917 |  |
| Education: high school or below (vs college) | +0.7364 | 0.9730 | ±1.9461 | +0.757 | 0.4492 |  |
| **Site: UCSD (vs UAB)** | **+2.7947** | 0.6754 | ±1.3508 | **+4.138** | **3.51e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7434** | 0.5621 | ±1.1242 | **-3.101** | **0.0019** | ** |
| **Season: spring (vs autumn)** | **-2.1537** | 0.6756 | ±1.3512 | **-3.188** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+1.4373** | 0.7206 | ±1.4411 | **+1.995** | **0.0461** | * |
| **Season: winter (vs autumn)** | **-6.1426** | 0.7434 | ±1.4868 | **-8.263** | **1.42e-16** | *** |
| **Age (years)** | **-0.0583** | 0.0231 | ±0.0461 | **-2.526** | **0.0115** | * |
| BMI (kg/m2) | -0.0006 | 0.0399 | ±0.0799 | -0.015 | 0.9880 |  |
| Hypertension | +0.4609 | 0.5527 | ±1.1054 | +0.834 | 0.4043 |  |
| High cholesterol | -0.3468 | 0.5255 | ±1.0509 | -0.660 | 0.5093 |  |
| Kidney disease | +0.2905 | 0.8500 | ±1.7000 | +0.342 | 0.7325 |  |
| Circulatory disease | +1.1656 | 0.6899 | ±1.3799 | +1.689 | 0.0911 | . |
| Time > 250 (%) | +0.0250 | 0.0389 | ±0.0777 | +0.642 | 0.5207 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 628)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **628**, R² = **0.2314**, Adj R² = **0.2139**, F-statistic = **13.18** (p = **1.86e-27**), Residual SE = **6.196** on **613** df, AIC = **4087.7**, BIC = **4154.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3094** | 2.0403 | ±4.0806 | **+24.168** | **4.84e-129** | *** |
| Education: graduate level (vs college) | +0.2954 | 0.5418 | ±1.0835 | +0.545 | 0.5856 |  |
| Education: high school or below (vs college) | +0.7161 | 0.9749 | ±1.9498 | +0.735 | 0.4626 |  |
| **Site: UCSD (vs UAB)** | **+2.7946** | 0.6754 | ±1.3507 | **+4.138** | **3.50e-05** | *** |
| **Site: UW (vs UAB)** | **-1.7389** | 0.5618 | ±1.1236 | **-3.095** | **0.0020** | ** |
| **Season: spring (vs autumn)** | **-2.1634** | 0.6763 | ±1.3525 | **-3.199** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+1.4391** | 0.7199 | ±1.4398 | **+1.999** | **0.0456** | * |
| **Season: winter (vs autumn)** | **-6.1485** | 0.7438 | ±1.4875 | **-8.267** | **1.38e-16** | *** |
| **Age (years)** | **-0.0583** | 0.0231 | ±0.0461 | **-2.530** | **0.0114** | * |
| BMI (kg/m2) | -0.0004 | 0.0400 | ±0.0799 | -0.010 | 0.9924 |  |
| Hypertension | +0.4543 | 0.5528 | ±1.1056 | +0.822 | 0.4112 |  |
| High cholesterol | -0.3462 | 0.5254 | ±1.0509 | -0.659 | 0.5100 |  |
| Kidney disease | +0.2729 | 0.8508 | ±1.7015 | +0.321 | 0.7484 |  |
| Circulatory disease | +1.1599 | 0.6916 | ±1.3831 | +1.677 | 0.0935 | . |
| Avg. daily time > 250 (%) | +0.0345 | 0.0492 | ±0.0984 | +0.702 | 0.4828 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 628; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **628**, R² = **0.0524**, Adj R² = **0.0323**, F-statistic = **2.61** (p = **0.0015**), Residual SE = **16.840** on **614** df, AIC = **5342.7**, BIC = **5404.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.4135** | 5.7288 | ±11.4576 | **+21.717** | **1.41e-104** | *** |
| Education: graduate level (vs college) | -1.1837 | 1.4735 | ±2.9471 | -0.803 | 0.4218 |  |
| Education: high school or below (vs college) | +4.5149 | 2.6352 | ±5.2705 | +1.713 | 0.0867 | . |
| Site: UCSD (vs UAB) | +2.8517 | 1.9756 | ±3.9513 | +1.443 | 0.1489 |  |
| Site: UW (vs UAB) | -1.5984 | 1.5569 | ±3.1138 | -1.027 | 0.3046 |  |
| Season: spring (vs autumn) | +3.1278 | 1.7427 | ±3.4855 | +1.795 | 0.0727 | . |
| Season: summer (vs autumn) | +1.1254 | 1.9785 | ±3.9569 | +0.569 | 0.5695 |  |
| **Season: winter (vs autumn)** | **+6.1380** | 2.0822 | ±4.1645 | **+2.948** | **0.0032** | ** |
| Age (years) | -0.1040 | 0.0612 | ±0.1223 | -1.700 | 0.0891 | . |
| BMI (kg/m2) | +0.1525 | 0.0928 | ±0.1857 | +1.642 | 0.1006 |  |
| Hypertension | +1.7198 | 1.5036 | ±3.0072 | +1.144 | 0.2527 |  |
| High cholesterol | -0.4676 | 1.5222 | ±3.0445 | -0.307 | 0.7587 |  |
| Kidney disease | +0.7808 | 2.5151 | ±5.0301 | +0.310 | 0.7562 |  |
| Circulatory disease | -0.9924 | 1.9680 | ±3.9359 | -0.504 | 0.6141 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **628**, R² = **0.0539**, Adj R² = **0.0323**, F-statistic = **2.49** (p = **0.0019**), Residual SE = **16.840** on **613** df, AIC = **5343.7**, BIC = **5410.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.5982** | 7.6834 | ±15.3668 | **+16.737** | **7.02e-63** | *** |
| Education: graduate level (vs college) | -1.2883 | 1.4385 | ±2.8771 | -0.896 | 0.3705 |  |
| Education: high school or below (vs college) | +4.7976 | 2.6562 | ±5.3123 | +1.806 | 0.0709 | . |
| Site: UCSD (vs UAB) | +2.9052 | 1.9770 | ±3.9539 | +1.470 | 0.1417 |  |
| Site: UW (vs UAB) | -1.7142 | 1.5496 | ±3.0991 | -1.106 | 0.2686 |  |
| Season: spring (vs autumn) | +3.0805 | 1.7439 | ±3.4878 | +1.766 | 0.0773 | . |
| Season: summer (vs autumn) | +1.0730 | 1.9774 | ±3.9548 | +0.543 | 0.5874 |  |
| **Season: winter (vs autumn)** | **+6.0846** | 2.1217 | ±4.2434 | **+2.868** | **0.0041** | ** |
| Age (years) | -0.0962 | 0.0690 | ±0.1380 | -1.394 | 0.1633 |  |
| BMI (kg/m2) | +0.1604 | 0.0982 | ±0.1964 | +1.634 | 0.1024 |  |
| Hypertension | +1.8966 | 1.5374 | ±3.0747 | +1.234 | 0.2173 |  |
| High cholesterol | -0.3749 | 1.5388 | ±3.0776 | -0.244 | 0.8075 |  |
| Kidney disease | +0.8834 | 2.4905 | ±4.9809 | +0.355 | 0.7228 |  |
| Circulatory disease | -1.0058 | 1.9681 | ±3.9362 | -0.511 | 0.6093 |  |
| HbA1c (%) | -0.8371 | 1.5719 | ±3.1438 | -0.533 | 0.5944 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **628**, R² = **0.0536**, Adj R² = **0.0320**, F-statistic = **2.48** (p = **0.0020**), Residual SE = **16.843** on **613** df, AIC = **5343.8**, BIC = **5410.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.2077** | 6.3321 | ±12.6642 | **+20.089** | **9.16e-90** | *** |
| Education: graduate level (vs college) | -1.1859 | 1.4779 | ±2.9557 | -0.802 | 0.4223 |  |
| Education: high school or below (vs college) | +4.7332 | 2.7098 | ±5.4196 | +1.747 | 0.0807 | . |
| Site: UCSD (vs UAB) | +2.8676 | 1.9841 | ±3.9681 | +1.445 | 0.1484 |  |
| Site: UW (vs UAB) | -1.6396 | 1.5533 | ±3.1067 | -1.056 | 0.2912 |  |
| Season: spring (vs autumn) | +3.1748 | 1.7407 | ±3.4813 | +1.824 | 0.0682 | . |
| Season: summer (vs autumn) | +1.0906 | 1.9800 | ±3.9600 | +0.551 | 0.5817 |  |
| **Season: winter (vs autumn)** | **+6.0934** | 2.1259 | ±4.2518 | **+2.866** | **0.0042** | ** |
| Age (years) | -0.1026 | 0.0631 | ±0.1261 | -1.626 | 0.1039 |  |
| BMI (kg/m2) | +0.1563 | 0.0961 | ±0.1923 | +1.626 | 0.1039 |  |
| Hypertension | +1.9103 | 1.5377 | ±3.0753 | +1.242 | 0.2141 |  |
| High cholesterol | -0.3886 | 1.5405 | ±3.0809 | -0.252 | 0.8008 |  |
| Kidney disease | +0.9988 | 2.5283 | ±5.0566 | +0.395 | 0.6928 |  |
| Circulatory disease | -0.9649 | 1.9680 | ±3.9359 | -0.490 | 0.6239 |  |
| Mean glucose (mg/dL) | -0.0259 | 0.0526 | ±0.1051 | -0.492 | 0.6227 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **628**, R² = **0.0536**, Adj R² = **0.0320**, F-statistic = **2.48** (p = **0.0020**), Residual SE = **16.843** on **613** df, AIC = **5343.8**, BIC = **5410.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.7861** | 11.9341 | ±23.8682 | **+10.959** | **6.01e-28** | *** |
| Education: graduate level (vs college) | -1.1859 | 1.4779 | ±2.9557 | -0.802 | 0.4223 |  |
| Education: high school or below (vs college) | +4.7332 | 2.7098 | ±5.4196 | +1.747 | 0.0807 | . |
| Site: UCSD (vs UAB) | +2.8676 | 1.9841 | ±3.9681 | +1.445 | 0.1484 |  |
| Site: UW (vs UAB) | -1.6396 | 1.5533 | ±3.1067 | -1.056 | 0.2912 |  |
| Season: spring (vs autumn) | +3.1748 | 1.7407 | ±3.4813 | +1.824 | 0.0682 | . |
| Season: summer (vs autumn) | +1.0906 | 1.9800 | ±3.9600 | +0.551 | 0.5817 |  |
| **Season: winter (vs autumn)** | **+6.0934** | 2.1259 | ±4.2518 | **+2.866** | **0.0042** | ** |
| Age (years) | -0.1026 | 0.0631 | ±0.1261 | -1.626 | 0.1039 |  |
| BMI (kg/m2) | +0.1563 | 0.0961 | ±0.1923 | +1.626 | 0.1039 |  |
| Hypertension | +1.9103 | 1.5377 | ±3.0753 | +1.242 | 0.2141 |  |
| High cholesterol | -0.3886 | 1.5405 | ±3.0809 | -0.252 | 0.8008 |  |
| Kidney disease | +0.9988 | 2.5283 | ±5.0566 | +0.395 | 0.6928 |  |
| Circulatory disease | -0.9649 | 1.9680 | ±3.9359 | -0.490 | 0.6239 |  |
| GMI (%) | -1.0811 | 2.1969 | ±4.3939 | -0.492 | 0.6227 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **628**, R² = **0.0565**, Adj R² = **0.0350**, F-statistic = **2.62** (p = **0.0010**), Residual SE = **16.816** on **613** df, AIC = **5341.9**, BIC = **5408.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.5514** | 6.7177 | ±13.4355 | **+19.285** | **7.19e-83** | *** |
| Education: graduate level (vs college) | -1.1680 | 1.4831 | ±2.9662 | -0.788 | 0.4310 |  |
| Education: high school or below (vs college) | +4.8806 | 2.6890 | ±5.3781 | +1.815 | 0.0695 | . |
| Site: UCSD (vs UAB) | +2.9069 | 1.9809 | ±3.9618 | +1.467 | 0.1423 |  |
| Site: UW (vs UAB) | -1.6488 | 1.5556 | ±3.1112 | -1.060 | 0.2892 |  |
| Season: spring (vs autumn) | +3.2597 | 1.7408 | ±3.4816 | +1.873 | 0.0611 | . |
| Season: summer (vs autumn) | +1.0121 | 1.9734 | ±3.9467 | +0.513 | 0.6080 |  |
| **Season: winter (vs autumn)** | **+6.1159** | 2.0999 | ±4.1998 | **+2.912** | **0.0036** | ** |
| Age (years) | -0.1075 | 0.0609 | ±0.1219 | -1.764 | 0.0778 | . |
| BMI (kg/m2) | +0.1664 | 0.1000 | ±0.2000 | +1.664 | 0.0961 | . |
| Hypertension | +2.0525 | 1.5371 | ±3.0741 | +1.335 | 0.1818 |  |
| High cholesterol | -0.2700 | 1.5534 | ±3.1068 | -0.174 | 0.8620 |  |
| Kidney disease | +0.8853 | 2.4851 | ±4.9703 | +0.356 | 0.7217 |  |
| Circulatory disease | -0.9757 | 1.9597 | ±3.9195 | -0.498 | 0.6186 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0474 | 0.0569 | ±0.1139 | -0.832 | 0.4052 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **628**, R² = **0.0529**, Adj R² = **0.0312**, F-statistic = **2.44** (p = **0.0023**), Residual SE = **16.849** on **613** df, AIC = **5344.3**, BIC = **5411.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.9830** | 5.4763 | ±10.9527 | **+22.822** | **2.75e-115** | *** |
| Education: graduate level (vs college) | -1.2148 | 1.4600 | ±2.9200 | -0.832 | 0.4054 |  |
| Education: high school or below (vs college) | +4.7176 | 2.7012 | ±5.4025 | +1.746 | 0.0807 | . |
| Site: UCSD (vs UAB) | +2.8530 | 1.9839 | ±3.9679 | +1.438 | 0.1504 |  |
| Site: UW (vs UAB) | -1.6768 | 1.5526 | ±3.1051 | -1.080 | 0.2801 |  |
| Season: spring (vs autumn) | +3.1230 | 1.7438 | ±3.4877 | +1.791 | 0.0733 | . |
| Season: summer (vs autumn) | +1.0892 | 1.9771 | ±3.9543 | +0.551 | 0.5817 |  |
| **Season: winter (vs autumn)** | **+6.0971** | 2.1154 | ±4.2308 | **+2.882** | **0.0039** | ** |
| Age (years) | -0.0992 | 0.0662 | ±0.1324 | -1.498 | 0.1342 |  |
| BMI (kg/m2) | +0.1529 | 0.0934 | ±0.1868 | +1.637 | 0.1016 |  |
| Hypertension | +1.8341 | 1.4985 | ±2.9971 | +1.224 | 0.2210 |  |
| High cholesterol | -0.4627 | 1.5295 | ±3.0591 | -0.303 | 0.7622 |  |
| Kidney disease | +1.0647 | 2.5647 | ±5.1295 | +0.415 | 0.6780 |  |
| Circulatory disease | -1.0079 | 1.9842 | ±3.9685 | -0.508 | 0.6115 |  |
| Glucose SD, pooled (mg/dL) | -0.0347 | 0.0883 | ±0.1767 | -0.393 | 0.6944 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **628**, R² = **0.0524**, Adj R² = **0.0307**, F-statistic = **2.42** (p = **0.0026**), Residual SE = **16.854** on **613** df, AIC = **5344.7**, BIC = **5411.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.4550** | 5.5170 | ±11.0339 | **+22.559** | **1.11e-112** | *** |
| Education: graduate level (vs college) | -1.1863 | 1.4625 | ±2.9250 | -0.811 | 0.4173 |  |
| Education: high school or below (vs college) | +4.5315 | 2.6785 | ±5.3569 | +1.692 | 0.0907 | . |
| Site: UCSD (vs UAB) | +2.8524 | 1.9794 | ±3.9588 | +1.441 | 0.1496 |  |
| Site: UW (vs UAB) | -1.6033 | 1.5517 | ±3.1035 | -1.033 | 0.3015 |  |
| Season: spring (vs autumn) | +3.1282 | 1.7461 | ±3.4921 | +1.792 | 0.0732 | . |
| Season: summer (vs autumn) | +1.1222 | 1.9777 | ±3.9553 | +0.567 | 0.5704 |  |
| **Season: winter (vs autumn)** | **+6.1346** | 2.1105 | ±4.2209 | **+2.907** | **0.0037** | ** |
| Age (years) | -0.1036 | 0.0651 | ±0.1302 | -1.591 | 0.1115 |  |
| BMI (kg/m2) | +0.1525 | 0.0931 | ±0.1862 | +1.637 | 0.1015 |  |
| Hypertension | +1.7274 | 1.5047 | ±3.0094 | +1.148 | 0.2510 |  |
| High cholesterol | -0.4668 | 1.5262 | ±3.0524 | -0.306 | 0.7597 |  |
| Kidney disease | +0.8020 | 2.5630 | ±5.1259 | +0.313 | 0.7543 |  |
| Circulatory disease | -0.9944 | 1.9819 | ±3.9639 | -0.502 | 0.6159 |  |
| Avg. daily SD (mg/dL) | -0.0029 | 0.0826 | ±0.1651 | -0.035 | 0.9719 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **628**, R² = **0.0524**, Adj R² = **0.0308**, F-statistic = **2.42** (p = **0.0026**), Residual SE = **16.853** on **613** df, AIC = **5344.6**, BIC = **5411.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.0774** | 5.6872 | ±11.3744 | **+21.817** | **1.60e-105** | *** |
| Education: graduate level (vs college) | -1.1722 | 1.4703 | ±2.9406 | -0.797 | 0.4253 |  |
| Education: high school or below (vs college) | +4.4562 | 2.6511 | ±5.3022 | +1.681 | 0.0928 | . |
| Site: UCSD (vs UAB) | +2.8510 | 1.9797 | ±3.9593 | +1.440 | 0.1498 |  |
| Site: UW (vs UAB) | -1.5687 | 1.5571 | ±3.1142 | -1.007 | 0.3137 |  |
| Season: spring (vs autumn) | +3.1351 | 1.7448 | ±3.4896 | +1.797 | 0.0724 | . |
| Season: summer (vs autumn) | +1.1302 | 1.9786 | ±3.9571 | +0.571 | 0.5679 |  |
| **Season: winter (vs autumn)** | **+6.1495** | 2.0934 | ±4.1869 | **+2.938** | **0.0033** | ** |
| Age (years) | -0.1063 | 0.0648 | ±0.1295 | -1.641 | 0.1007 |  |
| BMI (kg/m2) | +0.1526 | 0.0929 | ±0.1858 | +1.643 | 0.1003 |  |
| Hypertension | +1.6940 | 1.4975 | ±2.9950 | +1.131 | 0.2580 |  |
| High cholesterol | -0.4595 | 1.5264 | ±3.0528 | -0.301 | 0.7634 |  |
| Kidney disease | +0.6809 | 2.5391 | ±5.0783 | +0.268 | 0.7886 |  |
| Circulatory disease | -0.9841 | 1.9768 | ±3.9536 | -0.498 | 0.6186 |  |
| CV (%) | +0.0223 | 0.1253 | ±0.2506 | +0.178 | 0.8588 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **628**, R² = **0.0527**, Adj R² = **0.0311**, F-statistic = **2.44** (p = **0.0024**), Residual SE = **16.850** on **613** df, AIC = **5344.4**, BIC = **5411.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.1796** | 7.5242 | ±15.0483 | **+16.770** | **4.05e-63** | *** |
| Education: graduate level (vs college) | -1.1732 | 1.4747 | ±2.9494 | -0.796 | 0.4263 |  |
| Education: high school or below (vs college) | +4.3703 | 2.6486 | ±5.2971 | +1.650 | 0.0989 | . |
| Site: UCSD (vs UAB) | +2.8292 | 1.9762 | ±3.9525 | +1.432 | 0.1523 |  |
| Site: UW (vs UAB) | -1.5515 | 1.5551 | ±3.1103 | -0.998 | 0.3185 |  |
| Season: spring (vs autumn) | +3.1407 | 1.7460 | ±3.4919 | +1.799 | 0.0721 | . |
| Season: summer (vs autumn) | +1.1248 | 1.9815 | ±3.9630 | +0.568 | 0.5703 |  |
| **Season: winter (vs autumn)** | **+6.1608** | 2.0964 | ±4.1928 | **+2.939** | **0.0033** | ** |
| Age (years) | -0.1102 | 0.0654 | ±0.1308 | -1.686 | 0.0919 | . |
| BMI (kg/m2) | +0.1518 | 0.0932 | ±0.1863 | +1.630 | 0.1031 |  |
| Hypertension | +1.6649 | 1.5041 | ±3.0081 | +1.107 | 0.2683 |  |
| High cholesterol | -0.4495 | 1.5281 | ±3.0562 | -0.294 | 0.7686 |  |
| Kidney disease | +0.5885 | 2.5467 | ±5.0933 | +0.231 | 0.8172 |  |
| Circulatory disease | -0.9949 | 1.9707 | ±3.9413 | -0.505 | 0.6137 |  |
| Mean / SD ratio | -0.2642 | 0.5717 | ±1.1434 | -0.462 | 0.6440 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **628**, R² = **0.0532**, Adj R² = **0.0316**, F-statistic = **2.46** (p = **0.0022**), Residual SE = **16.846** on **613** df, AIC = **5344.1**, BIC = **5410.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.1140** | 7.0874 | ±14.1748 | **+17.935** | **6.26e-72** | *** |
| Education: graduate level (vs college) | -1.1585 | 1.4777 | ±2.9553 | -0.784 | 0.4330 |  |
| Education: high school or below (vs college) | +4.2603 | 2.6323 | ±5.2646 | +1.618 | 0.1056 |  |
| Site: UCSD (vs UAB) | +2.7801 | 1.9773 | ±3.9546 | +1.406 | 0.1597 |  |
| Site: UW (vs UAB) | -1.5476 | 1.5590 | ±3.1181 | -0.993 | 0.3209 |  |
| Season: spring (vs autumn) | +3.1306 | 1.7465 | ±3.4929 | +1.793 | 0.0730 | . |
| Season: summer (vs autumn) | +1.1621 | 1.9785 | ±3.9571 | +0.587 | 0.5570 |  |
| **Season: winter (vs autumn)** | **+6.1746** | 2.0928 | ±4.1857 | **+2.950** | **0.0032** | ** |
| Age (years) | -0.1143 | 0.0645 | ±0.1289 | -1.773 | 0.0763 | . |
| BMI (kg/m2) | +0.1511 | 0.0930 | ±0.1860 | +1.625 | 0.1041 |  |
| Hypertension | +1.6619 | 1.5082 | ±3.0164 | +1.102 | 0.2705 |  |
| High cholesterol | -0.4546 | 1.5255 | ±3.0510 | -0.298 | 0.7657 |  |
| Kidney disease | +0.5076 | 2.5462 | ±5.0923 | +0.199 | 0.8420 |  |
| Circulatory disease | -0.9778 | 1.9678 | ±3.9356 | -0.497 | 0.6193 |  |
| Avg. daily mean/SD | -0.3343 | 0.4448 | ±0.8895 | -0.752 | 0.4523 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **628**, R² = **0.0553**, Adj R² = **0.0338**, F-statistic = **2.56** (p = **0.0014**), Residual SE = **16.827** on **613** df, AIC = **5342.7**, BIC = **5409.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+120.3719** | 5.6679 | ±11.3359 | **+21.237** | **4.31e-100** | *** |
| Education: graduate level (vs college) | -1.1371 | 1.4692 | ±2.9385 | -0.774 | 0.4390 |  |
| Education: high school or below (vs college) | +4.1518 | 2.6014 | ±5.2028 | +1.596 | 0.1105 |  |
| Site: UCSD (vs UAB) | +2.7579 | 1.9848 | ±3.9696 | +1.390 | 0.1647 |  |
| Site: UW (vs UAB) | -1.3206 | 1.5256 | ±3.0512 | -0.866 | 0.3867 |  |
| Season: spring (vs autumn) | +3.1449 | 1.7490 | ±3.4980 | +1.798 | 0.0722 | . |
| Season: summer (vs autumn) | +1.2088 | 1.9813 | ±3.9625 | +0.610 | 0.5418 |  |
| **Season: winter (vs autumn)** | **+6.2222** | 2.0920 | ±4.1840 | **+2.974** | **0.0029** | ** |
| Age (years) | -0.1050 | 0.0612 | ±0.1224 | -1.715 | 0.0864 | . |
| BMI (kg/m2) | +0.1460 | 0.0932 | ±0.1864 | +1.566 | 0.1173 |  |
| Hypertension | +1.6089 | 1.5095 | ±3.0191 | +1.066 | 0.2865 |  |
| High cholesterol | -0.3962 | 1.5329 | ±3.0658 | -0.258 | 0.7961 |  |
| Kidney disease | +0.6874 | 2.5260 | ±5.0519 | +0.272 | 0.7855 |  |
| Circulatory disease | -0.9658 | 1.9655 | ±3.9310 | -0.491 | 0.6232 |  |
| MAG (mg/dL/h) | +0.1011 | 0.0832 | ±0.1664 | +1.215 | 0.2244 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **628**, R² = **0.0527**, Adj R² = **0.0310**, F-statistic = **2.43** (p = **0.0024**), Residual SE = **16.851** on **613** df, AIC = **5344.5**, BIC = **5411.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.6959** | 5.4564 | ±10.9127 | **+22.670** | **8.85e-114** | *** |
| Education: graduate level (vs college) | -1.1527 | 1.4620 | ±2.9239 | -0.788 | 0.4304 |  |
| Education: high school or below (vs college) | +4.3359 | 2.6495 | ±5.2990 | +1.637 | 0.1017 |  |
| Site: UCSD (vs UAB) | +2.8421 | 1.9796 | ±3.9591 | +1.436 | 0.1511 |  |
| Site: UW (vs UAB) | -1.5483 | 1.5477 | ±3.0953 | -1.000 | 0.3171 |  |
| Season: spring (vs autumn) | +3.1234 | 1.7481 | ±3.4962 | +1.787 | 0.0740 | . |
| Season: summer (vs autumn) | +1.1495 | 1.9783 | ±3.9566 | +0.581 | 0.5612 |  |
| **Season: winter (vs autumn)** | **+6.1709** | 2.1075 | ±4.2151 | **+2.928** | **0.0034** | ** |
| Age (years) | -0.1078 | 0.0646 | ±0.1292 | -1.670 | 0.0950 | . |
| BMI (kg/m2) | +0.1538 | 0.0922 | ±0.1844 | +1.668 | 0.0952 | . |
| Hypertension | +1.6538 | 1.5077 | ±3.0153 | +1.097 | 0.2727 |  |
| High cholesterol | -0.4707 | 1.5253 | ±3.0506 | -0.309 | 0.7576 |  |
| Kidney disease | +0.5692 | 2.5383 | ±5.0767 | +0.224 | 0.8226 |  |
| Circulatory disease | -0.9878 | 1.9750 | ±3.9500 | -0.500 | 0.6170 |  |
| Avg. daily range (mg/dL) | +0.0082 | 0.0216 | ±0.0432 | +0.381 | 0.7030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **628**, R² = **0.0598**, Adj R² = **0.0384**, F-statistic = **2.79** (p = **4.87e-04**), Residual SE = **16.787** on **613** df, AIC = **5339.7**, BIC = **5406.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.6998** | 5.5420 | ±11.0839 | **+22.681** | **6.83e-114** | *** |
| Education: graduate level (vs college) | -1.2677 | 1.4647 | ±2.9295 | -0.865 | 0.3868 |  |
| Education: high school or below (vs college) | +4.7413 | 2.6415 | ±5.2830 | +1.795 | 0.0727 | . |
| Site: UCSD (vs UAB) | +2.7760 | 1.9984 | ±3.9968 | +1.389 | 0.1648 |  |
| Site: UW (vs UAB) | -1.8512 | 1.5574 | ±3.1148 | -1.189 | 0.2346 |  |
| Season: spring (vs autumn) | +3.0785 | 1.7282 | ±3.4565 | +1.781 | 0.0749 | . |
| Season: summer (vs autumn) | +1.1466 | 1.9843 | ±3.9685 | +0.578 | 0.5634 |  |
| **Season: winter (vs autumn)** | **+6.1340** | 2.0887 | ±4.1774 | **+2.937** | **0.0033** | ** |
| Age (years) | -0.0970 | 0.0648 | ±0.1296 | -1.497 | 0.1343 |  |
| BMI (kg/m2) | +0.1575 | 0.0944 | ±0.1888 | +1.668 | 0.0954 | . |
| Hypertension | +2.1025 | 1.5079 | ±3.0157 | +1.394 | 0.1632 |  |
| High cholesterol | -0.4464 | 1.5356 | ±3.0712 | -0.291 | 0.7713 |  |
| Kidney disease | +1.4329 | 2.5239 | ±5.0477 | +0.568 | 0.5702 |  |
| Circulatory disease | -0.8506 | 1.9437 | ±3.8873 | -0.438 | 0.6617 |  |
| SD of daily means (mg/dL) | -0.2187 | 0.2309 | ±0.4618 | -0.947 | 0.3435 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **628**, R² = **0.0524**, Adj R² = **0.0307**, F-statistic = **2.42** (p = **0.0026**), Residual SE = **16.854** on **613** df, AIC = **5344.7**, BIC = **5411.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.3225** | 14.1547 | ±28.3094 | **+8.783** | **1.59e-18** | *** |
| Education: graduate level (vs college) | -1.1851 | 1.4367 | ±2.8733 | -0.825 | 0.4094 |  |
| Education: high school or below (vs college) | +4.5188 | 2.7278 | ±5.4555 | +1.657 | 0.0976 | . |
| Site: UCSD (vs UAB) | +2.8508 | 2.0036 | ±4.0071 | +1.423 | 0.1548 |  |
| Site: UW (vs UAB) | -1.6012 | 1.5383 | ±3.0766 | -1.041 | 0.2979 |  |
| Season: spring (vs autumn) | +3.1280 | 1.7464 | ±3.4928 | +1.791 | 0.0733 | . |
| Season: summer (vs autumn) | +1.1242 | 1.9782 | ±3.9563 | +0.568 | 0.5698 |  |
| **Season: winter (vs autumn)** | **+6.1379** | 2.1023 | ±4.2046 | **+2.920** | **0.0035** | ** |
| Age (years) | -0.1040 | 0.0648 | ±0.1296 | -1.604 | 0.1087 |  |
| BMI (kg/m2) | +0.1525 | 0.0943 | ±0.1887 | +1.616 | 0.1060 |  |
| Hypertension | +1.7223 | 1.5385 | ±3.0770 | +1.119 | 0.2629 |  |
| High cholesterol | -0.4667 | 1.5342 | ±3.0684 | -0.304 | 0.7610 |  |
| Kidney disease | +0.7872 | 2.5978 | ±5.1955 | +0.303 | 0.7619 |  |
| Circulatory disease | -0.9920 | 1.9825 | ±3.9650 | -0.500 | 0.6168 |  |
| Time in range 70-180, pooled (%) | +0.0009 | 0.1101 | ±0.2203 | +0.009 | 0.9932 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **628**, R² = **0.0524**, Adj R² = **0.0307**, F-statistic = **2.42** (p = **0.0026**), Residual SE = **16.853** on **613** df, AIC = **5344.6**, BIC = **5411.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.7190** | 14.2032 | ±28.4064 | **+8.711** | **3.02e-18** | *** |
| Education: graduate level (vs college) | -1.1948 | 1.4363 | ±2.8727 | -0.832 | 0.4055 |  |
| Education: high school or below (vs college) | +4.5457 | 2.7250 | ±5.4501 | +1.668 | 0.0953 | . |
| Site: UCSD (vs UAB) | +2.8451 | 2.0017 | ±4.0034 | +1.421 | 0.1552 |  |
| Site: UW (vs UAB) | -1.6198 | 1.5372 | ±3.0743 | -1.054 | 0.2920 |  |
| Season: spring (vs autumn) | +3.1307 | 1.7464 | ±3.4929 | +1.793 | 0.0730 | . |
| Season: summer (vs autumn) | +1.1165 | 1.9775 | ±3.9550 | +0.565 | 0.5724 |  |
| **Season: winter (vs autumn)** | **+6.1392** | 2.0947 | ±4.1893 | **+2.931** | **0.0034** | ** |
| Age (years) | -0.1035 | 0.0651 | ±0.1303 | -1.590 | 0.1119 |  |
| BMI (kg/m2) | +0.1527 | 0.0943 | ±0.1887 | +1.618 | 0.1056 |  |
| Hypertension | +1.7384 | 1.5371 | ±3.0742 | +1.131 | 0.2581 |  |
| High cholesterol | -0.4601 | 1.5348 | ±3.0696 | -0.300 | 0.7643 |  |
| Kidney disease | +0.8308 | 2.5916 | ±5.1833 | +0.321 | 0.7485 |  |
| Circulatory disease | -0.9890 | 1.9818 | ±3.9636 | -0.499 | 0.6178 |  |
| Avg. daily time in range 70-180 (%) | +0.0071 | 0.1098 | ±0.2195 | +0.065 | 0.9483 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **628**, R² = **0.0527**, Adj R² = **0.0311**, F-statistic = **2.44** (p = **0.0024**), Residual SE = **16.851** on **613** df, AIC = **5344.4**, BIC = **5411.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.1524** | 5.8286 | ±11.6571 | **+21.301** | **1.12e-100** | *** |
| Education: graduate level (vs college) | -1.1716 | 1.4769 | ±2.9539 | -0.793 | 0.4276 |  |
| Education: high school or below (vs college) | +4.5766 | 2.6293 | ±5.2587 | +1.741 | 0.0818 | . |
| Site: UCSD (vs UAB) | +2.9773 | 1.9947 | ±3.9894 | +1.493 | 0.1355 |  |
| Site: UW (vs UAB) | -1.4965 | 1.5870 | ±3.1739 | -0.943 | 0.3457 |  |
| Season: spring (vs autumn) | +3.1542 | 1.7467 | ±3.4934 | +1.806 | 0.0709 | . |
| Season: summer (vs autumn) | +1.0907 | 1.9749 | ±3.9498 | +0.552 | 0.5808 |  |
| **Season: winter (vs autumn)** | **+6.1183** | 2.0895 | ±4.1789 | **+2.928** | **0.0034** | ** |
| Age (years) | -0.1044 | 0.0612 | ±0.1223 | -1.707 | 0.0877 | . |
| BMI (kg/m2) | +0.1532 | 0.0934 | ±0.1868 | +1.640 | 0.1010 |  |
| Hypertension | +1.7546 | 1.5045 | ±3.0090 | +1.166 | 0.2435 |  |
| High cholesterol | -0.4241 | 1.5215 | ±3.0430 | -0.279 | 0.7805 |  |
| Kidney disease | +0.7675 | 2.5152 | ±5.0303 | +0.305 | 0.7603 |  |
| Circulatory disease | -0.9986 | 1.9682 | ±3.9365 | -0.507 | 0.6119 |  |
| Time < 54 (%) | +0.3634 | 0.8833 | ±1.7666 | +0.411 | 0.6808 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **628**, R² = **0.0530**, Adj R² = **0.0314**, F-statistic = **2.45** (p = **0.0023**), Residual SE = **16.848** on **613** df, AIC = **5344.2**, BIC = **5410.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.2156** | 5.7630 | ±11.5261 | **+21.554** | **4.87e-103** | *** |
| Education: graduate level (vs college) | -1.1387 | 1.4758 | ±2.9516 | -0.772 | 0.4404 |  |
| Education: high school or below (vs college) | +4.6032 | 2.6321 | ±5.2643 | +1.749 | 0.0803 | . |
| Site: UCSD (vs UAB) | +3.0060 | 1.9916 | ±3.9833 | +1.509 | 0.1312 |  |
| Site: UW (vs UAB) | -1.4347 | 1.5873 | ±3.1746 | -0.904 | 0.3661 |  |
| Season: spring (vs autumn) | +3.1707 | 1.7465 | ±3.4930 | +1.815 | 0.0695 | . |
| Season: summer (vs autumn) | +1.0819 | 1.9744 | ±3.9487 | +0.548 | 0.5837 |  |
| **Season: winter (vs autumn)** | **+6.0941** | 2.0882 | ±4.1764 | **+2.918** | **0.0035** | ** |
| Age (years) | -0.1064 | 0.0609 | ±0.1219 | -1.747 | 0.0807 | . |
| BMI (kg/m2) | +0.1530 | 0.0931 | ±0.1863 | +1.642 | 0.1006 |  |
| Hypertension | +1.7746 | 1.5013 | ±3.0027 | +1.182 | 0.2372 |  |
| High cholesterol | -0.4055 | 1.5216 | ±3.0432 | -0.266 | 0.7899 |  |
| Kidney disease | +0.7369 | 2.5132 | ±5.0263 | +0.293 | 0.7694 |  |
| Circulatory disease | -1.0074 | 1.9671 | ±3.9343 | -0.512 | 0.6086 |  |
| Avg. daily time < 54 (%) | +0.6096 | 0.8685 | ±1.7369 | +0.702 | 0.4827 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **628**, R² = **0.0534**, Adj R² = **0.0318**, F-statistic = **2.47** (p = **0.0021**), Residual SE = **16.844** on **613** df, AIC = **5344.0**, BIC = **5410.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.0578** | 5.8182 | ±11.6364 | **+21.322** | **7.03e-101** | *** |
| Education: graduate level (vs college) | -1.1042 | 1.4840 | ±2.9680 | -0.744 | 0.4568 |  |
| Education: high school or below (vs college) | +4.5302 | 2.6424 | ±5.2849 | +1.714 | 0.0865 | . |
| Site: UCSD (vs UAB) | +2.9639 | 1.9849 | ±3.9698 | +1.493 | 0.1354 |  |
| Site: UW (vs UAB) | -1.4684 | 1.5749 | ±3.1499 | -0.932 | 0.3512 |  |
| Season: spring (vs autumn) | +3.1731 | 1.7421 | ±3.4843 | +1.821 | 0.0685 | . |
| Season: summer (vs autumn) | +1.1219 | 1.9764 | ±3.9529 | +0.568 | 0.5703 |  |
| **Season: winter (vs autumn)** | **+6.0848** | 2.0910 | ±4.1819 | **+2.910** | **0.0036** | ** |
| Age (years) | -0.1066 | 0.0609 | ±0.1218 | -1.749 | 0.0802 | . |
| BMI (kg/m2) | +0.1517 | 0.0931 | ±0.1862 | +1.629 | 0.1033 |  |
| Hypertension | +1.7975 | 1.5035 | ±3.0070 | +1.196 | 0.2319 |  |
| High cholesterol | -0.4412 | 1.5250 | ±3.0500 | -0.289 | 0.7723 |  |
| Kidney disease | +0.7142 | 2.5101 | ±5.0201 | +0.285 | 0.7760 |  |
| Circulatory disease | -0.9634 | 1.9663 | ±3.9326 | -0.490 | 0.6242 |  |
| Time 54-69, pooled (%) | +0.2481 | 0.2960 | ±0.5921 | +0.838 | 0.4020 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **628**, R² = **0.0530**, Adj R² = **0.0314**, F-statistic = **2.45** (p = **0.0023**), Residual SE = **16.848** on **613** df, AIC = **5344.2**, BIC = **5410.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.2305** | 5.7783 | ±11.5566 | **+21.499** | **1.58e-102** | *** |
| Education: graduate level (vs college) | -1.1111 | 1.4860 | ±2.9721 | -0.748 | 0.4546 |  |
| Education: high school or below (vs college) | +4.5222 | 2.6424 | ±5.2849 | +1.711 | 0.0870 | . |
| Site: UCSD (vs UAB) | +2.9266 | 1.9846 | ±3.9692 | +1.475 | 0.1403 |  |
| Site: UW (vs UAB) | -1.4855 | 1.5762 | ±3.1524 | -0.942 | 0.3460 |  |
| Season: spring (vs autumn) | +3.1592 | 1.7431 | ±3.4862 | +1.812 | 0.0699 | . |
| Season: summer (vs autumn) | +1.1273 | 1.9772 | ±3.9545 | +0.570 | 0.5686 |  |
| **Season: winter (vs autumn)** | **+6.0883** | 2.0903 | ±4.1806 | **+2.913** | **0.0036** | ** |
| Age (years) | -0.1070 | 0.0609 | ±0.1219 | -1.756 | 0.0791 | . |
| BMI (kg/m2) | +0.1515 | 0.0929 | ±0.1859 | +1.630 | 0.1031 |  |
| Hypertension | +1.7809 | 1.5021 | ±3.0041 | +1.186 | 0.2358 |  |
| High cholesterol | -0.4479 | 1.5249 | ±3.0498 | -0.294 | 0.7690 |  |
| Kidney disease | +0.7319 | 2.5132 | ±5.0264 | +0.291 | 0.7709 |  |
| Circulatory disease | -0.9680 | 1.9664 | ±3.9329 | -0.492 | 0.6225 |  |
| Avg. daily time 54-69 (%) | +0.1929 | 0.2834 | ±0.5668 | +0.681 | 0.4960 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **628**, R² = **0.0534**, Adj R² = **0.0318**, F-statistic = **2.47** (p = **0.0021**), Residual SE = **16.845** on **613** df, AIC = **5344.0**, BIC = **5410.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.9878** | 5.8414 | ±11.6828 | **+21.226** | **5.52e-100** | *** |
| Education: graduate level (vs college) | -1.1137 | 1.4822 | ±2.9644 | -0.751 | 0.4524 |  |
| Education: high school or below (vs college) | +4.5607 | 2.6382 | ±5.2765 | +1.729 | 0.0839 | . |
| Site: UCSD (vs UAB) | +3.0095 | 1.9909 | ±3.9817 | +1.512 | 0.1306 |  |
| Site: UW (vs UAB) | -1.4393 | 1.5827 | ±3.1655 | -0.909 | 0.3632 |  |
| Season: spring (vs autumn) | +3.1783 | 1.7428 | ±3.4856 | +1.824 | 0.0682 | . |
| Season: summer (vs autumn) | +1.1037 | 1.9757 | ±3.9515 | +0.559 | 0.5764 |  |
| **Season: winter (vs autumn)** | **+6.0849** | 2.0919 | ±4.1838 | **+2.909** | **0.0036** | ** |
| Age (years) | -0.1063 | 0.0609 | ±0.1218 | -1.745 | 0.0810 | . |
| BMI (kg/m2) | +0.1522 | 0.0932 | ±0.1865 | +1.633 | 0.1025 |  |
| Hypertension | +1.8007 | 1.5034 | ±3.0068 | +1.198 | 0.2310 |  |
| High cholesterol | -0.4229 | 1.5247 | ±3.0495 | -0.277 | 0.7815 |  |
| Kidney disease | +0.7205 | 2.5097 | ±5.0195 | +0.287 | 0.7741 |  |
| Circulatory disease | -0.9726 | 1.9664 | ±3.9329 | -0.495 | 0.6209 |  |
| Time < 70 (%) | +0.1978 | 0.2339 | ±0.4677 | +0.846 | 0.3977 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **628**, R² = **0.0532**, Adj R² = **0.0315**, F-statistic = **2.46** (p = **0.0022**), Residual SE = **16.846** on **613** df, AIC = **5344.1**, BIC = **5410.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.1925** | 5.7825 | ±11.5650 | **+21.477** | **2.54e-102** | *** |
| Education: graduate level (vs college) | -1.1056 | 1.4843 | ±2.9687 | -0.745 | 0.4564 |  |
| Education: high school or below (vs college) | +4.5466 | 2.6404 | ±5.2807 | +1.722 | 0.0851 | . |
| Site: UCSD (vs UAB) | +2.9630 | 1.9885 | ±3.9770 | +1.490 | 0.1362 |  |
| Site: UW (vs UAB) | -1.4501 | 1.5825 | ±3.1651 | -0.916 | 0.3595 |  |
| Season: spring (vs autumn) | +3.1682 | 1.7434 | ±3.4869 | +1.817 | 0.0692 | . |
| Season: summer (vs autumn) | +1.1147 | 1.9764 | ±3.9528 | +0.564 | 0.5727 |  |
| **Season: winter (vs autumn)** | **+6.0808** | 2.0905 | ±4.1811 | **+2.909** | **0.0036** | ** |
| Age (years) | -0.1074 | 0.0609 | ±0.1218 | -1.764 | 0.0778 | . |
| BMI (kg/m2) | +0.1517 | 0.0930 | ±0.1860 | +1.632 | 0.1027 |  |
| Hypertension | +1.7904 | 1.5013 | ±3.0026 | +1.193 | 0.2330 |  |
| High cholesterol | -0.4322 | 1.5248 | ±3.0495 | -0.283 | 0.7768 |  |
| Kidney disease | +0.7243 | 2.5122 | ±5.0245 | +0.288 | 0.7731 |  |
| Circulatory disease | -0.9747 | 1.9661 | ±3.9322 | -0.496 | 0.6200 |  |
| Avg. daily time < 70 (%) | +0.1736 | 0.2266 | ±0.4531 | +0.766 | 0.4434 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **628**, R² = **0.0596**, Adj R² = **0.0381**, F-statistic = **2.77** (p = **5.15e-04**), Residual SE = **16.789** on **613** df, AIC = **5339.9**, BIC = **5406.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+99.1730** | 27.8292 | ±55.6585 | **+3.564** | **3.66e-04** | *** |
| Education: graduate level (vs college) | -1.3498 | 1.4554 | ±2.9108 | -0.927 | 0.3537 |  |
| Education: high school or below (vs college) | +4.9571 | 2.7179 | ±5.4358 | +1.824 | 0.0682 | . |
| Site: UCSD (vs UAB) | +2.6974 | 2.0182 | ±4.0365 | +1.337 | 0.1814 |  |
| Site: UW (vs UAB) | -1.9405 | 1.5916 | ±3.1831 | -1.219 | 0.2228 |  |
| Season: spring (vs autumn) | +3.2128 | 1.7405 | ±3.4810 | +1.846 | 0.0649 | . |
| Season: summer (vs autumn) | +0.9052 | 1.9809 | ±3.9617 | +0.457 | 0.6477 |  |
| **Season: winter (vs autumn)** | **+6.1605** | 2.0758 | ±4.1517 | **+2.968** | **0.0030** | ** |
| Age (years) | -0.1046 | 0.0617 | ±0.1234 | -1.695 | 0.0901 | . |
| BMI (kg/m2) | +0.1504 | 0.0927 | ±0.1853 | +1.624 | 0.1045 |  |
| Hypertension | +1.9481 | 1.4992 | ±2.9984 | +1.299 | 0.1938 |  |
| High cholesterol | -0.5752 | 1.5234 | ±3.0468 | -0.378 | 0.7057 |  |
| Kidney disease | +1.1595 | 2.5155 | ±5.0311 | +0.461 | 0.6449 |  |
| Circulatory disease | -0.8778 | 1.9386 | ±3.8772 | -0.453 | 0.6507 |  |
| Time 54-250, pooled (%) | +0.2586 | 0.2666 | ±0.5333 | +0.970 | 0.3322 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **628**, R² = **0.0607**, Adj R² = **0.0392**, F-statistic = **2.83** (p = **3.97e-04**), Residual SE = **16.779** on **613** df, AIC = **5339.1**, BIC = **5405.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+94.2280** | 31.6097 | ±63.2194 | **+2.981** | **0.0029** | ** |
| Education: graduate level (vs college) | -1.3839 | 1.4536 | ±2.9072 | -0.952 | 0.3411 |  |
| Education: high school or below (vs college) | +5.0668 | 2.7230 | ±5.4459 | +1.861 | 0.0628 | . |
| Site: UCSD (vs UAB) | +2.7191 | 2.0109 | ±4.0218 | +1.352 | 0.1763 |  |
| Site: UW (vs UAB) | -1.9517 | 1.5897 | ±3.1794 | -1.228 | 0.2195 |  |
| Season: spring (vs autumn) | +3.2813 | 1.7413 | ±3.4825 | +1.884 | 0.0595 | . |
| Season: summer (vs autumn) | +0.9217 | 1.9763 | ±3.9526 | +0.466 | 0.6409 |  |
| **Season: winter (vs autumn)** | **+6.2196** | 2.0641 | ±4.1281 | **+3.013** | **0.0026** | ** |
| Age (years) | -0.1028 | 0.0622 | ±0.1244 | -1.652 | 0.0986 | . |
| BMI (kg/m2) | +0.1490 | 0.0925 | ±0.1851 | +1.610 | 0.1074 |  |
| Hypertension | +1.9685 | 1.4982 | ±2.9963 | +1.314 | 0.1889 |  |
| High cholesterol | -0.5696 | 1.5231 | ±3.0461 | -0.374 | 0.7084 |  |
| Kidney disease | +1.2757 | 2.5158 | ±5.0315 | +0.507 | 0.6121 |  |
| Circulatory disease | -0.8391 | 1.9338 | ±3.8676 | -0.434 | 0.6643 |  |
| Avg. daily time 54-250 (%) | +0.3068 | 0.3033 | ±0.6066 | +1.012 | 0.3118 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **628**, R² = **0.0545**, Adj R² = **0.0329**, F-statistic = **2.52** (p = **0.0017**), Residual SE = **16.835** on **613** df, AIC = **5343.3**, BIC = **5409.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.4593** | 5.7996 | ±11.5992 | **+21.460** | **3.69e-102** | *** |
| Education: graduate level (vs college) | -1.1357 | 1.4559 | ±2.9118 | -0.780 | 0.4353 |  |
| Education: high school or below (vs college) | +4.2872 | 2.6915 | ±5.3830 | +1.593 | 0.1112 |  |
| Site: UCSD (vs UAB) | +2.8438 | 1.9882 | ±3.9763 | +1.430 | 0.1526 |  |
| Site: UW (vs UAB) | -1.4994 | 1.5291 | ±3.0581 | -0.981 | 0.3268 |  |
| Season: spring (vs autumn) | +3.1175 | 1.7533 | ±3.5066 | +1.778 | 0.0754 | . |
| Season: summer (vs autumn) | +1.1651 | 1.9787 | ±3.9573 | +0.589 | 0.5560 |  |
| **Season: winter (vs autumn)** | **+6.1658** | 2.1179 | ±4.2358 | **+2.911** | **0.0036** | ** |
| Age (years) | -0.1087 | 0.0657 | ±0.1313 | -1.654 | 0.0980 | . |
| BMI (kg/m2) | +0.1492 | 0.0948 | ±0.1895 | +1.575 | 0.1153 |  |
| Hypertension | +1.5282 | 1.5875 | ±3.1750 | +0.963 | 0.3357 |  |
| High cholesterol | -0.6011 | 1.4881 | ±2.9762 | -0.404 | 0.6862 |  |
| Kidney disease | +0.3194 | 2.6216 | ±5.2431 | +0.122 | 0.9030 |  |
| Circulatory disease | -1.0087 | 1.9797 | ±3.9594 | -0.510 | 0.6104 |  |
| Time 181-250, pooled (%) | +0.0906 | 0.1558 | ±0.3116 | +0.581 | 0.5610 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **628**, R² = **0.0538**, Adj R² = **0.0322**, F-statistic = **2.49** (p = **0.0019**), Residual SE = **16.841** on **613** df, AIC = **5343.7**, BIC = **5410.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.4165** | 5.7699 | ±11.5397 | **+21.563** | **3.99e-103** | *** |
| Education: graduate level (vs college) | -1.1448 | 1.4571 | ±2.9142 | -0.786 | 0.4321 |  |
| Education: high school or below (vs college) | +4.3270 | 2.6871 | ±5.3742 | +1.610 | 0.1073 |  |
| Site: UCSD (vs UAB) | +2.8592 | 1.9862 | ±3.9724 | +1.440 | 0.1500 |  |
| Site: UW (vs UAB) | -1.5053 | 1.5269 | ±3.0538 | -0.986 | 0.3242 |  |
| Season: spring (vs autumn) | +3.1224 | 1.7526 | ±3.5052 | +1.782 | 0.0748 | . |
| Season: summer (vs autumn) | +1.1675 | 1.9788 | ±3.9576 | +0.590 | 0.5552 |  |
| **Season: winter (vs autumn)** | **+6.1635** | 2.1196 | ±4.2393 | **+2.908** | **0.0036** | ** |
| Age (years) | -0.1073 | 0.0650 | ±0.1300 | -1.651 | 0.0987 | . |
| BMI (kg/m2) | +0.1497 | 0.0948 | ±0.1896 | +1.579 | 0.1143 |  |
| Hypertension | +1.5653 | 1.5790 | ±3.1580 | +0.991 | 0.3215 |  |
| High cholesterol | -0.5760 | 1.4938 | ±2.9876 | -0.386 | 0.6998 |  |
| Kidney disease | +0.4037 | 2.6085 | ±5.2170 | +0.155 | 0.8770 |  |
| Circulatory disease | -1.0005 | 1.9798 | ±3.9595 | -0.505 | 0.6133 |  |
| Avg. daily time 181-250 (%) | +0.0731 | 0.1483 | ±0.2966 | +0.493 | 0.6221 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **628**, R² = **0.0524**, Adj R² = **0.0308**, F-statistic = **2.42** (p = **0.0026**), Residual SE = **16.853** on **613** df, AIC = **5344.6**, BIC = **5411.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.4260** | 5.7498 | ±11.4996 | **+21.640** | **7.55e-104** | *** |
| Education: graduate level (vs college) | -1.1959 | 1.4457 | ±2.8913 | -0.827 | 0.4081 |  |
| Education: high school or below (vs college) | +4.5622 | 2.7364 | ±5.4728 | +1.667 | 0.0955 | . |
| Site: UCSD (vs UAB) | +2.8499 | 1.9941 | ±3.9881 | +1.429 | 0.1529 |  |
| Site: UW (vs UAB) | -1.6214 | 1.5381 | ±3.0763 | -1.054 | 0.2918 |  |
| Season: spring (vs autumn) | +3.1333 | 1.7454 | ±3.4908 | +1.795 | 0.0726 | . |
| Season: summer (vs autumn) | +1.1104 | 1.9793 | ±3.9587 | +0.561 | 0.5748 |  |
| **Season: winter (vs autumn)** | **+6.1350** | 2.1145 | ±4.2290 | **+2.901** | **0.0037** | ** |
| Age (years) | -0.1035 | 0.0644 | ±0.1289 | -1.606 | 0.1082 |  |
| BMI (kg/m2) | +0.1528 | 0.0944 | ±0.1888 | +1.618 | 0.1056 |  |
| Hypertension | +1.7531 | 1.5504 | ±3.1009 | +1.131 | 0.2582 |  |
| High cholesterol | -0.4549 | 1.5345 | ±3.0691 | -0.296 | 0.7669 |  |
| Kidney disease | +0.8510 | 2.5924 | ±5.1847 | +0.328 | 0.7427 |  |
| Circulatory disease | -0.9859 | 1.9791 | ±3.9583 | -0.498 | 0.6184 |  |
| Time > 180 (%) | -0.0108 | 0.1132 | ±0.2264 | -0.095 | 0.9242 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **628**, R² = **0.0525**, Adj R² = **0.0309**, F-statistic = **2.43** (p = **0.0025**), Residual SE = **16.852** on **613** df, AIC = **5344.6**, BIC = **5411.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.4334** | 5.7502 | ±11.5005 | **+21.640** | **7.61e-104** | *** |
| Education: graduate level (vs college) | -1.2016 | 1.4471 | ±2.8942 | -0.830 | 0.4063 |  |
| Education: high school or below (vs college) | +4.5877 | 2.7346 | ±5.4692 | +1.678 | 0.0934 | . |
| Site: UCSD (vs UAB) | +2.8471 | 1.9943 | ±3.9886 | +1.428 | 0.1534 |  |
| Site: UW (vs UAB) | -1.6332 | 1.5372 | ±3.0745 | -1.062 | 0.2881 |  |
| Season: spring (vs autumn) | +3.1382 | 1.7459 | ±3.4918 | +1.797 | 0.0723 | . |
| Season: summer (vs autumn) | +1.1042 | 1.9782 | ±3.9565 | +0.558 | 0.5767 |  |
| **Season: winter (vs autumn)** | **+6.1355** | 2.1089 | ±4.2177 | **+2.909** | **0.0036** | ** |
| Age (years) | -0.1033 | 0.0643 | ±0.1287 | -1.605 | 0.1084 |  |
| BMI (kg/m2) | +0.1529 | 0.0943 | ±0.1886 | +1.621 | 0.1050 |  |
| Hypertension | +1.7684 | 1.5480 | ±3.0960 | +1.142 | 0.2533 |  |
| High cholesterol | -0.4474 | 1.5357 | ±3.0714 | -0.291 | 0.7708 |  |
| Kidney disease | +0.8888 | 2.5878 | ±5.1756 | +0.343 | 0.7313 |  |
| Circulatory disease | -0.9830 | 1.9787 | ±3.9574 | -0.497 | 0.6193 |  |
| Avg. daily time > 180 (%) | -0.0161 | 0.1138 | ±0.2276 | -0.142 | 0.8873 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **628**, R² = **0.0535**, Adj R² = **0.0319**, F-statistic = **2.47** (p = **0.0020**), Residual SE = **16.844** on **613** df, AIC = **5343.9**, BIC = **5410.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.4660** | 5.7996 | ±11.5991 | **+21.461** | **3.59e-102** | *** |
| Education: graduate level (vs college) | -1.2510 | 1.4334 | ±2.8669 | -0.873 | 0.3828 |  |
| Education: high school or below (vs college) | +4.6597 | 2.7202 | ±5.4404 | +1.713 | 0.0867 | . |
| Site: UCSD (vs UAB) | +2.8202 | 2.0085 | ±4.0171 | +1.404 | 0.1603 |  |
| Site: UW (vs UAB) | -1.6850 | 1.5446 | ±3.0893 | -1.091 | 0.2753 |  |
| Season: spring (vs autumn) | +3.1571 | 1.7417 | ±3.4835 | +1.813 | 0.0699 | . |
| Season: summer (vs autumn) | +1.0096 | 1.9866 | ±3.9732 | +0.508 | 0.6113 |  |
| **Season: winter (vs autumn)** | **+6.1525** | 2.0959 | ±4.1918 | **+2.935** | **0.0033** | ** |
| Age (years) | -0.1038 | 0.0628 | ±0.1257 | -1.651 | 0.0986 | . |
| BMI (kg/m2) | +0.1557 | 0.0969 | ±0.1938 | +1.607 | 0.1081 |  |
| Hypertension | +1.8640 | 1.5723 | ±3.1445 | +1.186 | 0.2358 |  |
| High cholesterol | -0.4133 | 1.5450 | ±3.0901 | -0.267 | 0.7891 |  |
| Kidney disease | +0.8944 | 2.5157 | ±5.0314 | +0.356 | 0.7222 |  |
| Circulatory disease | -0.9516 | 1.9691 | ±3.9382 | -0.483 | 0.6289 |  |
| Nocturnal time > 180 (%) | -0.0485 | 0.1409 | ±0.2818 | -0.345 | 0.7305 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **628**, R² = **0.0548**, Adj R² = **0.0332**, F-statistic = **2.54** (p = **0.0015**), Residual SE = **16.832** on **613** df, AIC = **5343.0**, BIC = **5409.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.2223** | 5.6370 | ±11.2739 | **+22.037** | **1.27e-107** | *** |
| Education: graduate level (vs college) | -1.0771 | 1.4605 | ±2.9210 | -0.738 | 0.4608 |  |
| Education: high school or below (vs college) | +4.3041 | 2.6073 | ±5.2145 | +1.651 | 0.0988 | . |
| Site: UCSD (vs UAB) | +2.7799 | 1.9792 | ±3.9584 | +1.405 | 0.1602 |  |
| Site: UW (vs UAB) | -1.5333 | 1.5478 | ±3.0956 | -0.991 | 0.3219 |  |
| Season: spring (vs autumn) | +3.2020 | 1.7454 | ±3.4909 | +1.834 | 0.0666 | . |
| Season: summer (vs autumn) | +1.1756 | 1.9711 | ±3.9421 | +0.596 | 0.5509 |  |
| **Season: winter (vs autumn)** | **+6.2997** | 2.1192 | ±4.2385 | **+2.973** | **0.0030** | ** |
| Age (years) | -0.1125 | 0.0638 | ±0.1276 | -1.764 | 0.0777 | . |
| BMI (kg/m2) | +0.1587 | 0.0914 | ±0.1828 | +1.737 | 0.0824 | . |
| Hypertension | +1.4922 | 1.5174 | ±3.0349 | +0.983 | 0.3254 |  |
| High cholesterol | -0.4983 | 1.5189 | ±3.0378 | -0.328 | 0.7429 |  |
| Kidney disease | +0.3388 | 2.5292 | ±5.0583 | +0.134 | 0.8935 |  |
| Circulatory disease | -0.9681 | 1.9705 | ±3.9410 | -0.491 | 0.6232 |  |
| Any reading > 250 during wear (0/1) | +1.9444 | 1.7670 | ±3.5340 | +1.100 | 0.2712 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **628**, R² = **0.0603**, Adj R² = **0.0388**, F-statistic = **2.81** (p = **4.36e-04**), Residual SE = **16.783** on **613** df, AIC = **5339.4**, BIC = **5406.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.8715** | 5.7037 | ±11.4073 | **+21.893** | **3.01e-106** | *** |
| Education: graduate level (vs college) | -1.3514 | 1.4556 | ±2.9112 | -0.928 | 0.3532 |  |
| Education: high school or below (vs college) | +5.0325 | 2.7232 | ±5.4464 | +1.848 | 0.0646 | . |
| Site: UCSD (vs UAB) | +2.7825 | 1.9944 | ±3.9888 | +1.395 | 0.1630 |  |
| Site: UW (vs UAB) | -1.8855 | 1.5782 | ±3.1565 | -1.195 | 0.2322 |  |
| Season: spring (vs autumn) | +3.2383 | 1.7408 | ±3.4815 | +1.860 | 0.0628 | . |
| Season: summer (vs autumn) | +0.8646 | 1.9786 | ±3.9572 | +0.437 | 0.6621 |  |
| **Season: winter (vs autumn)** | **+6.1471** | 2.0792 | ±4.1584 | **+2.956** | **0.0031** | ** |
| Age (years) | -0.1049 | 0.0617 | ±0.1234 | -1.701 | 0.0889 | . |
| BMI (kg/m2) | +0.1508 | 0.0928 | ±0.1855 | +1.626 | 0.1039 |  |
| Hypertension | +1.9892 | 1.5021 | ±3.0042 | +1.324 | 0.1854 |  |
| High cholesterol | -0.5492 | 1.5264 | ±3.0529 | -0.360 | 0.7190 |  |
| Kidney disease | +1.1739 | 2.5106 | ±5.0211 | +0.468 | 0.6401 |  |
| Circulatory disease | -0.8750 | 1.9372 | ±3.8744 | -0.452 | 0.6515 |  |
| Time > 250 (%) | -0.2753 | 0.2763 | ±0.5526 | -0.996 | 0.3190 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 628)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **628**, R² = **0.0618**, Adj R² = **0.0403**, F-statistic = **2.88** (p = **3.09e-04**), Residual SE = **16.770** on **613** df, AIC = **5338.4**, BIC = **5405.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.8381** | 5.7185 | ±11.4370 | **+21.831** | **1.19e-105** | *** |
| Education: graduate level (vs college) | -1.3760 | 1.4552 | ±2.9105 | -0.946 | 0.3444 |  |
| Education: high school or below (vs college) | +5.1606 | 2.7312 | ±5.4625 | +1.889 | 0.0588 | . |
| Site: UCSD (vs UAB) | +2.7922 | 1.9909 | ±3.9817 | +1.403 | 0.1608 |  |
| Site: UW (vs UAB) | -1.8917 | 1.5766 | ±3.1532 | -1.200 | 0.2302 |  |
| Season: spring (vs autumn) | +3.3174 | 1.7427 | ±3.4853 | +1.904 | 0.0570 | . |
| Season: summer (vs autumn) | +0.8812 | 1.9726 | ±3.9451 | +0.447 | 0.6551 |  |
| **Season: winter (vs autumn)** | **+6.2025** | 2.0670 | ±4.1340 | **+3.001** | **0.0027** | ** |
| Age (years) | -0.1040 | 0.0620 | ±0.1240 | -1.677 | 0.0935 | . |
| BMI (kg/m2) | +0.1489 | 0.0925 | ±0.1850 | +1.610 | 0.1073 |  |
| Hypertension | +2.0190 | 1.5012 | ±3.0024 | +1.345 | 0.1786 |  |
| High cholesterol | -0.5442 | 1.5259 | ±3.0518 | -0.357 | 0.7214 |  |
| Kidney disease | +1.2927 | 2.5108 | ±5.0216 | +0.515 | 0.6067 |  |
| Circulatory disease | -0.8346 | 1.9313 | ±3.8627 | -0.432 | 0.6657 |  |
| Avg. daily time > 250 (%) | -0.3322 | 0.3159 | ±0.6317 | -1.052 | 0.2930 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Total analysis base - Home environment

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 120 single-predictor tests; 8 with raw p < 0.05 (about 6 expected by chance); FDR rule applied to 120 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family and 0 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **Indoor PM2.5, log(1 + mean ug/m3)** (n = 628): best single predictor out of sample is **HbA1c** (CV R² 0.120 vs 0.114 for covariates alone, gain +0.006; +0.108 per SD, p = 0.024, q = 0.093). No association survives FDR; nominal only: HbA1c (p = 0.024).
- **Indoor temperature, mean (deg C)** (n = 628): best single predictor out of sample is **%<70 (daily avg)** (CV R² 0.239 vs 0.233 for covariates alone, gain +0.006; +0.182 per SD, p = 0.020, q = 0.087). No association survives FDR; nominal only: %<70 (pooled) (p = 0.020), %54-69 (daily avg) (p = 0.020), %<70 (daily avg) (p = 0.020), %<54 (pooled) (p = 0.023).
- **Indoor relative humidity, mean (%)** (n = 628): best single predictor out of sample is **%<54 (daily avg)** (CV R² 0.193 vs 0.190 for covariates alone, gain +0.003; -0.462 per SD, p = 0.040, q = 0.125). No association survives FDR; nominal only: %<54 (pooled) (p = 0.036), %<54 (daily avg) (p = 0.040).
- **Indoor VOC index, mean** (n = 628): best single predictor out of sample is **MAG** (CV R² 0.011 vs 0.011 for covariates alone, gain +0.000; +0.963 per SD, p = 0.224, q = 0.432). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.

**Most predictable outcomes (largest out-of-sample gain over covariates):** Indoor PM2.5, log(1 + mean ug/m3) (+0.006, via HbA1c); Indoor temperature, mean (deg C) (+0.006, via %<70 (daily avg)); Indoor relative humidity, mean (%) (+0.003, via %<54 (daily avg)); Indoor VOC index, mean (+0.000, via MAG). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band < 54 (0 FDR-significant / 3 raw-significant of 8); Band 54-69 (0 FDR-significant / 2 raw-significant of 8); Band < 70 (0 FDR-significant / 2 raw-significant of 8).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (0 raw); HbA1c alone: 0 FDR-significant (1 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Indoor temperature, mean (%<70 (daily avg), ΔAIC -4.8); Indoor VOC index, mean (%>250 (daily avg), ΔAIC -5.3).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
