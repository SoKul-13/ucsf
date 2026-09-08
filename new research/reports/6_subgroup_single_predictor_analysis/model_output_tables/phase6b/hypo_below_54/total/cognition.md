# Phase 6b model output tables - Hypoglycaemia exposure: at least one reading < 54 - Total analysis base - Cognition

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 638; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **638**, R² = **0.1312**, Adj R² = **0.1173**, F-statistic = **9.46** (p = **9.68e-15**), Residual SE = **2.842** on **627** df, AIC = **3154.1**, BIC = **3203.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.3478** | 0.9133 | ±1.8266 | **+33.229** | **4.10e-242** | *** |
| **Education: graduate level (vs college)** | **+0.7836** | 0.2346 | ±0.4692 | **+3.340** | **8.37e-04** | *** |
| **Education: high school or below (vs college)** | **-2.0152** | 0.6156 | ±1.2313 | **-3.273** | **0.0011** | ** |
| Site: UCSD (vs UAB) | -0.4569 | 0.3145 | ±0.6291 | -1.453 | 0.1464 |  |
| Site: UW (vs UAB) | -0.4661 | 0.2786 | ±0.5572 | -1.673 | 0.0943 | . |
| **Age (years)** | **-0.0618** | 0.0122 | ±0.0245 | **-5.052** | **4.37e-07** | *** |
| BMI (kg/m2) | -0.0210 | 0.0145 | ±0.0290 | -1.453 | 0.1463 |  |
| Hypertension | -0.2793 | 0.2546 | ±0.5093 | -1.097 | 0.2727 |  |
| **High cholesterol** | **+0.6236** | 0.2477 | ±0.4953 | **+2.518** | **0.0118** | * |
| Kidney disease | -0.0119 | 0.4115 | ±0.8229 | -0.029 | 0.9770 |  |
| Circulatory disease | -0.2080 | 0.3195 | ±0.6391 | -0.651 | 0.5150 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **638**, R² = **0.1578**, Adj R² = **0.1430**, F-statistic = **10.66** (p = **4.07e-18**), Residual SE = **2.800** on **626** df, AIC = **3136.3**, BIC = **3189.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.4275** | 1.1474 | ±2.2949 | **+29.132** | **1.40e-186** | *** |
| **Education: graduate level (vs college)** | **+0.7049** | 0.2332 | ±0.4664 | **+3.023** | **0.0025** | ** |
| **Education: high school or below (vs college)** | **-1.8291** | 0.5998 | ±1.1996 | **-3.050** | **0.0023** | ** |
| Site: UCSD (vs UAB) | -0.4157 | 0.3067 | ±0.6134 | -1.355 | 0.1753 |  |
| **Site: UW (vs UAB)** | **-0.5475** | 0.2770 | ±0.5541 | **-1.976** | **0.0481** | * |
| **Age (years)** | **-0.0562** | 0.0122 | ±0.0243 | **-4.616** | **3.91e-06** | *** |
| BMI (kg/m2) | -0.0151 | 0.0141 | ±0.0282 | -1.071 | 0.2842 |  |
| Hypertension | -0.1533 | 0.2495 | ±0.4990 | -0.614 | 0.5389 |  |
| **High cholesterol** | **+0.6905** | 0.2446 | ±0.4891 | **+2.824** | **0.0047** | ** |
| Kidney disease | +0.0766 | 0.3940 | ±0.7879 | +0.194 | 0.8459 |  |
| Circulatory disease | -0.2225 | 0.3138 | ±0.6276 | -0.709 | 0.4782 |  |
| **HbA1c (%)** | **-0.6200** | 0.1441 | ±0.2882 | **-4.303** | **1.68e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **638**, R² = **0.1502**, Adj R² = **0.1353**, F-statistic = **10.06** (p = **5.44e-17**), Residual SE = **2.813** on **626** df, AIC = **3142.0**, BIC = **3195.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.2786** | 1.0309 | ±2.0617 | **+31.312** | **3.20e-215** | *** |
| **Education: graduate level (vs college)** | **+0.7848** | 0.2328 | ±0.4657 | **+3.370** | **7.51e-04** | *** |
| **Education: high school or below (vs college)** | **-1.8677** | 0.6077 | ±1.2154 | **-3.073** | **0.0021** | ** |
| Site: UCSD (vs UAB) | -0.4472 | 0.3062 | ±0.6124 | -1.460 | 0.1442 |  |
| Site: UW (vs UAB) | -0.4903 | 0.2774 | ±0.5549 | -1.767 | 0.0772 | . |
| **Age (years)** | **-0.0609** | 0.0123 | ±0.0247 | **-4.938** | **7.90e-07** | *** |
| BMI (kg/m2) | -0.0181 | 0.0143 | ±0.0285 | -1.268 | 0.2049 |  |
| Hypertension | -0.1514 | 0.2512 | ±0.5024 | -0.603 | 0.5466 |  |
| **High cholesterol** | **+0.6800** | 0.2470 | ±0.4941 | **+2.753** | **0.0059** | ** |
| Kidney disease | +0.1503 | 0.4093 | ±0.8187 | +0.367 | 0.7134 |  |
| Circulatory disease | -0.1904 | 0.3141 | ±0.6282 | -0.606 | 0.5444 |  |
| **Mean glucose (mg/dL)** | **-0.0179** | 0.0054 | ±0.0107 | **-3.344** | **8.27e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **638**, R² = **0.1502**, Adj R² = **0.1353**, F-statistic = **10.06** (p = **5.44e-17**), Residual SE = **2.813** on **626** df, AIC = **3142.0**, BIC = **3195.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+34.7622** | 1.5316 | ±3.0631 | **+22.697** | **4.76e-114** | *** |
| **Education: graduate level (vs college)** | **+0.7848** | 0.2328 | ±0.4657 | **+3.370** | **7.51e-04** | *** |
| **Education: high school or below (vs college)** | **-1.8677** | 0.6077 | ±1.2154 | **-3.073** | **0.0021** | ** |
| Site: UCSD (vs UAB) | -0.4472 | 0.3062 | ±0.6124 | -1.460 | 0.1442 |  |
| Site: UW (vs UAB) | -0.4903 | 0.2774 | ±0.5549 | -1.767 | 0.0772 | . |
| **Age (years)** | **-0.0609** | 0.0123 | ±0.0247 | **-4.938** | **7.90e-07** | *** |
| BMI (kg/m2) | -0.0181 | 0.0143 | ±0.0285 | -1.268 | 0.2049 |  |
| Hypertension | -0.1514 | 0.2512 | ±0.5024 | -0.603 | 0.5466 |  |
| **High cholesterol** | **+0.6800** | 0.2470 | ±0.4941 | **+2.753** | **0.0059** | ** |
| Kidney disease | +0.1503 | 0.4093 | ±0.8187 | +0.367 | 0.7134 |  |
| Circulatory disease | -0.1904 | 0.3141 | ±0.6282 | -0.606 | 0.5444 |  |
| **GMI (%)** | **-0.7503** | 0.2244 | ±0.4488 | **-3.344** | **8.27e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **638**, R² = **0.1472**, Adj R² = **0.1322**, F-statistic = **9.82** (p = **1.50e-16**), Residual SE = **2.818** on **626** df, AIC = **3144.2**, BIC = **3197.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.1173** | 1.0352 | ±2.0705 | **+31.024** | **2.56e-211** | *** |
| **Education: graduate level (vs college)** | **+0.7946** | 0.2337 | ±0.4675 | **+3.400** | **6.75e-04** | *** |
| **Education: high school or below (vs college)** | **-1.8862** | 0.6086 | ±1.2171 | **-3.100** | **0.0019** | ** |
| Site: UCSD (vs UAB) | -0.4415 | 0.3077 | ±0.6154 | -1.435 | 0.1513 |  |
| Site: UW (vs UAB) | -0.4796 | 0.2780 | ±0.5560 | -1.725 | 0.0845 | . |
| **Age (years)** | **-0.0629** | 0.0123 | ±0.0246 | **-5.124** | **2.99e-07** | *** |
| BMI (kg/m2) | -0.0160 | 0.0144 | ±0.0288 | -1.110 | 0.2668 |  |
| Hypertension | -0.1705 | 0.2524 | ±0.5048 | -0.676 | 0.4993 |  |
| **High cholesterol** | **+0.6947** | 0.2472 | ±0.4945 | **+2.810** | **0.0050** | ** |
| Kidney disease | +0.0330 | 0.4063 | ±0.8127 | +0.081 | 0.9353 |  |
| Circulatory disease | -0.2038 | 0.3132 | ±0.6264 | -0.651 | 0.5152 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0164** | 0.0051 | ±0.0103 | **-3.192** | **0.0014** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **638**, R² = **0.1497**, Adj R² = **0.1348**, F-statistic = **10.02** (p = **6.38e-17**), Residual SE = **2.813** on **626** df, AIC = **3142.3**, BIC = **3195.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.9386** | 0.9141 | ±1.8282 | **+33.847** | **4.05e-251** | *** |
| **Education: graduate level (vs college)** | **+0.7556** | 0.2320 | ±0.4640 | **+3.257** | **0.0011** | ** |
| **Education: high school or below (vs college)** | **-1.8146** | 0.5972 | ±1.1943 | **-3.039** | **0.0024** | ** |
| Site: UCSD (vs UAB) | -0.4512 | 0.3051 | ±0.6103 | -1.479 | 0.1392 |  |
| Site: UW (vs UAB) | -0.5409 | 0.2797 | ±0.5595 | -1.934 | 0.0532 | . |
| **Age (years)** | **-0.0571** | 0.0125 | ±0.0250 | **-4.570** | **4.87e-06** | *** |
| BMI (kg/m2) | -0.0205 | 0.0145 | ±0.0289 | -1.419 | 0.1560 |  |
| Hypertension | -0.1602 | 0.2517 | ±0.5035 | -0.636 | 0.5245 |  |
| **High cholesterol** | **+0.6308** | 0.2460 | ±0.4920 | **+2.564** | **0.0103** | * |
| Kidney disease | +0.2996 | 0.4141 | ±0.8282 | +0.724 | 0.4693 |  |
| Circulatory disease | -0.2238 | 0.3137 | ±0.6273 | -0.713 | 0.4756 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.0366** | 0.0110 | ±0.0219 | **-3.337** | **8.47e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **638**, R² = **0.1480**, Adj R² = **0.1331**, F-statistic = **9.89** (p = **1.13e-16**), Residual SE = **2.816** on **626** df, AIC = **3143.6**, BIC = **3197.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.9154** | 0.9108 | ±1.8216 | **+33.942** | **1.59e-252** | *** |
| **Education: graduate level (vs college)** | **+0.7510** | 0.2319 | ±0.4639 | **+3.238** | **0.0012** | ** |
| **Education: high school or below (vs college)** | **-1.7972** | 0.5970 | ±1.1939 | **-3.011** | **0.0026** | ** |
| Site: UCSD (vs UAB) | -0.4433 | 0.3050 | ±0.6100 | -1.453 | 0.1461 |  |
| Site: UW (vs UAB) | -0.5266 | 0.2798 | ±0.5597 | -1.882 | 0.0599 | . |
| **Age (years)** | **-0.0569** | 0.0126 | ±0.0251 | **-4.531** | **5.88e-06** | *** |
| BMI (kg/m2) | -0.0207 | 0.0144 | ±0.0289 | -1.434 | 0.1515 |  |
| Hypertension | -0.1749 | 0.2526 | ±0.5051 | -0.693 | 0.4885 |  |
| **High cholesterol** | **+0.6379** | 0.2464 | ±0.4927 | **+2.589** | **0.0096** | ** |
| Kidney disease | +0.2977 | 0.4136 | ±0.8273 | +0.720 | 0.4718 |  |
| Circulatory disease | -0.2341 | 0.3142 | ±0.6284 | -0.745 | 0.4562 |  |
| **Avg. daily SD (mg/dL)** | **-0.0406** | 0.0130 | ±0.0261 | **-3.113** | **0.0019** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **638**, R² = **0.1412**, Adj R² = **0.1261**, F-statistic = **9.36** (p = **1.12e-15**), Residual SE = **2.827** on **626** df, AIC = **3148.7**, BIC = **3202.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.1505** | 0.9431 | ±1.8863 | **+33.029** | **3.13e-239** | *** |
| **Education: graduate level (vs college)** | **+0.7595** | 0.2327 | ±0.4655 | **+3.263** | **0.0011** | ** |
| **Education: high school or below (vs college)** | **-1.8849** | 0.5995 | ±1.1990 | **-3.144** | **0.0017** | ** |
| Site: UCSD (vs UAB) | -0.4492 | 0.3094 | ±0.6189 | -1.452 | 0.1466 |  |
| Site: UW (vs UAB) | -0.5304 | 0.2804 | ±0.5608 | -1.891 | 0.0586 | . |
| **Age (years)** | **-0.0567** | 0.0125 | ±0.0249 | **-4.545** | **5.50e-06** | *** |
| BMI (kg/m2) | -0.0215 | 0.0146 | ±0.0292 | -1.474 | 0.1406 |  |
| Hypertension | -0.2157 | 0.2533 | ±0.5065 | -0.852 | 0.3945 |  |
| **High cholesterol** | **+0.6053** | 0.2468 | ±0.4936 | **+2.452** | **0.0142** | * |
| Kidney disease | +0.2341 | 0.4146 | ±0.8292 | +0.565 | 0.5723 |  |
| Circulatory disease | -0.2259 | 0.3173 | ±0.6347 | -0.712 | 0.4765 |  |
| **CV (%)** | **-0.0533** | 0.0197 | ±0.0393 | **-2.713** | **0.0067** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **638**, R² = **0.1430**, Adj R² = **0.1280**, F-statistic = **9.50** (p = **6.05e-16**), Residual SE = **2.824** on **626** df, AIC = **3147.3**, BIC = **3200.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5575** | 1.1070 | ±2.2141 | **+25.796** | **9.82e-147** | *** |
| **Education: graduate level (vs college)** | **+0.7767** | 0.2330 | ±0.4660 | **+3.333** | **8.59e-04** | *** |
| **Education: high school or below (vs college)** | **-1.8765** | 0.5981 | ±1.1963 | **-3.137** | **0.0017** | ** |
| Site: UCSD (vs UAB) | -0.4276 | 0.3082 | ±0.6164 | -1.388 | 0.1653 |  |
| Site: UW (vs UAB) | -0.5066 | 0.2789 | ±0.5577 | -1.817 | 0.0693 | . |
| **Age (years)** | **-0.0559** | 0.0124 | ±0.0247 | **-4.520** | **6.17e-06** | *** |
| BMI (kg/m2) | -0.0205 | 0.0146 | ±0.0291 | -1.406 | 0.1598 |  |
| Hypertension | -0.2204 | 0.2534 | ±0.5069 | -0.870 | 0.3844 |  |
| **High cholesterol** | **+0.6067** | 0.2467 | ±0.4934 | **+2.459** | **0.0139** | * |
| Kidney disease | +0.1897 | 0.4098 | ±0.8196 | +0.463 | 0.6434 |  |
| Circulatory disease | -0.2031 | 0.3178 | ±0.6356 | -0.639 | 0.5227 |  |
| **Mean / SD ratio** | **+0.2686** | 0.0895 | ±0.1790 | **+3.001** | **0.0027** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **638**, R² = **0.1377**, Adj R² = **0.1226**, F-statistic = **9.09** (p = **3.57e-15**), Residual SE = **2.833** on **626** df, AIC = **3151.3**, BIC = **3204.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.0269** | 1.1208 | ±2.2416 | **+25.898** | **6.95e-148** | *** |
| **Education: graduate level (vs college)** | **+0.7746** | 0.2337 | ±0.4675 | **+3.314** | **9.20e-04** | *** |
| **Education: high school or below (vs college)** | **-1.8986** | 0.6027 | ±1.2053 | **-3.150** | **0.0016** | ** |
| Site: UCSD (vs UAB) | -0.4191 | 0.3095 | ±0.6190 | -1.354 | 0.1756 |  |
| Site: UW (vs UAB) | -0.4858 | 0.2791 | ±0.5581 | -1.741 | 0.0817 | . |
| **Age (years)** | **-0.0571** | 0.0125 | ±0.0250 | **-4.573** | **4.82e-06** | *** |
| BMI (kg/m2) | -0.0204 | 0.0146 | ±0.0291 | -1.401 | 0.1611 |  |
| Hypertension | -0.2502 | 0.2549 | ±0.5098 | -0.981 | 0.3264 |  |
| **High cholesterol** | **+0.6192** | 0.2475 | ±0.4950 | **+2.502** | **0.0124** | * |
| Kidney disease | +0.1271 | 0.4090 | ±0.8181 | +0.311 | 0.7560 |  |
| Circulatory disease | -0.2136 | 0.3191 | ±0.6382 | -0.669 | 0.5034 |  |
| **Avg. daily mean/SD** | **+0.1635** | 0.0743 | ±0.1486 | **+2.200** | **0.0278** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **638**, R² = **0.1349**, Adj R² = **0.1197**, F-statistic = **8.87** (p = **9.16e-15**), Residual SE = **2.838** on **626** df, AIC = **3153.4**, BIC = **3206.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.1388** | 1.0136 | ±2.0273 | **+30.720** | **3.09e-207** | *** |
| **Education: graduate level (vs college)** | **+0.7767** | 0.2341 | ±0.4682 | **+3.318** | **9.06e-04** | *** |
| **Education: high school or below (vs college)** | **-1.9497** | 0.6084 | ±1.2167 | **-3.205** | **0.0014** | ** |
| Site: UCSD (vs UAB) | -0.4354 | 0.3120 | ±0.6240 | -1.395 | 0.1629 |  |
| Site: UW (vs UAB) | -0.5168 | 0.2807 | ±0.5614 | -1.841 | 0.0656 | . |
| **Age (years)** | **-0.0618** | 0.0122 | ±0.0245 | **-5.047** | **4.48e-07** | *** |
| BMI (kg/m2) | -0.0197 | 0.0146 | ±0.0292 | -1.350 | 0.1771 |  |
| Hypertension | -0.2591 | 0.2546 | ±0.5092 | -1.018 | 0.3088 |  |
| **High cholesterol** | **+0.6107** | 0.2488 | ±0.4977 | **+2.454** | **0.0141** | * |
| Kidney disease | +0.0119 | 0.4123 | ±0.8247 | +0.029 | 0.9770 |  |
| Circulatory disease | -0.2127 | 0.3204 | ±0.6409 | -0.664 | 0.5067 |  |
| MAG (mg/dL/h) | -0.0199 | 0.0131 | ±0.0263 | -1.515 | 0.1299 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **638**, R² = **0.1428**, Adj R² = **0.1277**, F-statistic = **9.48** (p = **6.55e-16**), Residual SE = **2.825** on **626** df, AIC = **3147.5**, BIC = **3201.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.1189** | 0.9292 | ±1.8584 | **+33.489** | **6.86e-246** | *** |
| **Education: graduate level (vs college)** | **+0.7539** | 0.2322 | ±0.4645 | **+3.246** | **0.0012** | ** |
| **Education: high school or below (vs college)** | **-1.8349** | 0.6014 | ±1.2029 | **-3.051** | **0.0023** | ** |
| Site: UCSD (vs UAB) | -0.4424 | 0.3073 | ±0.6146 | -1.440 | 0.1499 |  |
| Site: UW (vs UAB) | -0.5135 | 0.2800 | ±0.5599 | -1.834 | 0.0666 | . |
| **Age (years)** | **-0.0581** | 0.0125 | ±0.0251 | **-4.631** | **3.63e-06** | *** |
| BMI (kg/m2) | -0.0224 | 0.0145 | ±0.0290 | -1.545 | 0.1223 |  |
| Hypertension | -0.2084 | 0.2528 | ±0.5056 | -0.824 | 0.4098 |  |
| **High cholesterol** | **+0.6304** | 0.2471 | ±0.4941 | **+2.552** | **0.0107** | * |
| Kidney disease | +0.2260 | 0.4129 | ±0.8259 | +0.547 | 0.5841 |  |
| Circulatory disease | -0.2120 | 0.3174 | ±0.6348 | -0.668 | 0.5042 |  |
| **Avg. daily range (mg/dL)** | **-0.0089** | 0.0035 | ±0.0069 | **-2.567** | **0.0103** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **638**, R² = **0.1414**, Adj R² = **0.1263**, F-statistic = **9.37** (p = **1.04e-15**), Residual SE = **2.827** on **626** df, AIC = **3148.5**, BIC = **3202.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.6215** | 0.9192 | ±1.8384 | **+33.314** | **2.42e-243** | *** |
| **Education: graduate level (vs college)** | **+0.7687** | 0.2341 | ±0.4681 | **+3.284** | **0.0010** | ** |
| **Education: high school or below (vs college)** | **-1.9727** | 0.6039 | ±1.2077 | **-3.267** | **0.0011** | ** |
| Site: UCSD (vs UAB) | -0.4697 | 0.3108 | ±0.6217 | -1.511 | 0.1307 |  |
| Site: UW (vs UAB) | -0.5167 | 0.2800 | ±0.5599 | -1.846 | 0.0649 | . |
| **Age (years)** | **-0.0605** | 0.0123 | ±0.0247 | **-4.903** | **9.45e-07** | *** |
| BMI (kg/m2) | -0.0201 | 0.0145 | ±0.0291 | -1.380 | 0.1675 |  |
| Hypertension | -0.2000 | 0.2517 | ±0.5034 | -0.795 | 0.4268 |  |
| **High cholesterol** | **+0.6267** | 0.2470 | ±0.4940 | **+2.537** | **0.0112** | * |
| Kidney disease | +0.1267 | 0.4101 | ±0.8202 | +0.309 | 0.7573 |  |
| Circulatory disease | -0.1793 | 0.3168 | ±0.6335 | -0.566 | 0.5715 |  |
| **SD of daily means (mg/dL)** | **-0.0455** | 0.0181 | ±0.0362 | **-2.511** | **0.0120** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **638**, R² = **0.1536**, Adj R² = **0.1388**, F-statistic = **10.33** (p = **1.69e-17**), Residual SE = **2.807** on **626** df, AIC = **3139.4**, BIC = **3192.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.8171** | 1.3842 | ±2.7684 | **+19.374** | **1.29e-83** | *** |
| **Education: graduate level (vs college)** | **+0.7374** | 0.2317 | ±0.4634 | **+3.183** | **0.0015** | ** |
| **Education: high school or below (vs college)** | **-1.8738** | 0.6014 | ±1.2028 | **-3.116** | **0.0018** | ** |
| Site: UCSD (vs UAB) | -0.4895 | 0.3044 | ±0.6087 | -1.608 | 0.1078 |  |
| **Site: UW (vs UAB)** | **-0.5685** | 0.2794 | ±0.5588 | **-2.035** | **0.0419** | * |
| **Age (years)** | **-0.0599** | 0.0123 | ±0.0246 | **-4.868** | **1.13e-06** | *** |
| BMI (kg/m2) | -0.0200 | 0.0142 | ±0.0283 | -1.409 | 0.1589 |  |
| Hypertension | -0.1839 | 0.2498 | ±0.4996 | -0.736 | 0.4616 |  |
| **High cholesterol** | **+0.6610** | 0.2456 | ±0.4911 | **+2.692** | **0.0071** | ** |
| Kidney disease | +0.2449 | 0.4142 | ±0.8285 | +0.591 | 0.5543 |  |
| Circulatory disease | -0.1911 | 0.3121 | ±0.6242 | -0.612 | 0.5404 |  |
| **Time in range 70-180, pooled (%)** | **+0.0365** | 0.0103 | ±0.0205 | **+3.560** | **3.71e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **638**, R² = **0.1528**, Adj R² = **0.1379**, F-statistic = **10.26** (p = **2.28e-17**), Residual SE = **2.808** on **626** df, AIC = **3140.1**, BIC = **3193.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.8794** | 1.3903 | ±2.7806 | **+19.333** | **2.82e-83** | *** |
| **Education: graduate level (vs college)** | **+0.7367** | 0.2318 | ±0.4636 | **+3.178** | **0.0015** | ** |
| **Education: high school or below (vs college)** | **-1.8715** | 0.6011 | ±1.2022 | **-3.114** | **0.0018** | ** |
| Site: UCSD (vs UAB) | -0.4876 | 0.3048 | ±0.6096 | -1.600 | 0.1097 |  |
| **Site: UW (vs UAB)** | **-0.5688** | 0.2798 | ±0.5596 | **-2.033** | **0.0420** | * |
| **Age (years)** | **-0.0598** | 0.0123 | ±0.0246 | **-4.852** | **1.22e-06** | *** |
| BMI (kg/m2) | -0.0200 | 0.0142 | ±0.0284 | -1.408 | 0.1592 |  |
| Hypertension | -0.1890 | 0.2499 | ±0.4998 | -0.756 | 0.4494 |  |
| **High cholesterol** | **+0.6639** | 0.2459 | ±0.4918 | **+2.700** | **0.0069** | ** |
| Kidney disease | +0.2448 | 0.4137 | ±0.8275 | +0.592 | 0.5540 |  |
| Circulatory disease | -0.1922 | 0.3120 | ±0.6240 | -0.616 | 0.5380 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.0356** | 0.0103 | ±0.0205 | **+3.472** | **5.17e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **638**, R² = **0.1312**, Adj R² = **0.1159**, F-statistic = **8.59** (p = **3.04e-14**), Residual SE = **2.844** on **626** df, AIC = **3156.1**, BIC = **3209.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.3670** | 0.9198 | ±1.8396 | **+33.016** | **4.85e-239** | *** |
| **Education: graduate level (vs college)** | **+0.7826** | 0.2353 | ±0.4705 | **+3.326** | **8.79e-04** | *** |
| **Education: high school or below (vs college)** | **-2.0192** | 0.6161 | ±1.2321 | **-3.278** | **0.0010** | ** |
| Site: UCSD (vs UAB) | -0.4653 | 0.3171 | ±0.6342 | -1.467 | 0.1422 |  |
| Site: UW (vs UAB) | -0.4731 | 0.2797 | ±0.5595 | -1.691 | 0.0908 | . |
| **Age (years)** | **-0.0618** | 0.0122 | ±0.0245 | **-5.044** | **4.56e-07** | *** |
| BMI (kg/m2) | -0.0211 | 0.0145 | ±0.0291 | -1.451 | 0.1469 |  |
| Hypertension | -0.2814 | 0.2548 | ±0.5095 | -1.105 | 0.2694 |  |
| **High cholesterol** | **+0.6203** | 0.2492 | ±0.4983 | **+2.490** | **0.0128** | * |
| Kidney disease | -0.0112 | 0.4119 | ±0.8238 | -0.027 | 0.9783 |  |
| Circulatory disease | -0.2074 | 0.3203 | ±0.6406 | -0.647 | 0.5173 |  |
| Time < 54 (%) | -0.0262 | 0.1660 | ±0.3320 | -0.158 | 0.8747 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **638**, R² = **0.1312**, Adj R² = **0.1160**, F-statistic = **8.60** (p = **3.00e-14**), Residual SE = **2.844** on **626** df, AIC = **3156.1**, BIC = **3209.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.3614** | 0.9147 | ±1.8294 | **+33.192** | **1.40e-241** | *** |
| **Education: graduate level (vs college)** | **+0.7807** | 0.2352 | ±0.4703 | **+3.320** | **9.01e-04** | *** |
| **Education: high school or below (vs college)** | **-2.0204** | 0.6166 | ±1.2332 | **-3.277** | **0.0011** | ** |
| Site: UCSD (vs UAB) | -0.4661 | 0.3171 | ±0.6342 | -1.470 | 0.1416 |  |
| Site: UW (vs UAB) | -0.4762 | 0.2808 | ±0.5617 | -1.696 | 0.0899 | . |
| **Age (years)** | **-0.0617** | 0.0123 | ±0.0245 | **-5.028** | **4.96e-07** | *** |
| BMI (kg/m2) | -0.0211 | 0.0145 | ±0.0290 | -1.452 | 0.1464 |  |
| Hypertension | -0.2822 | 0.2551 | ±0.5103 | -1.106 | 0.2687 |  |
| **High cholesterol** | **+0.6194** | 0.2491 | ±0.4982 | **+2.486** | **0.0129** | * |
| Kidney disease | -0.0097 | 0.4117 | ±0.8234 | -0.023 | 0.9813 |  |
| Circulatory disease | -0.2066 | 0.3203 | ±0.6407 | -0.645 | 0.5189 |  |
| Avg. daily time < 54 (%) | -0.0393 | 0.1734 | ±0.3467 | -0.227 | 0.8206 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **638**, R² = **0.1328**, Adj R² = **0.1176**, F-statistic = **8.72** (p = **1.78e-14**), Residual SE = **2.841** on **626** df, AIC = **3154.9**, BIC = **3208.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.4310** | 0.9238 | ±1.8477 | **+32.940** | **5.88e-238** | *** |
| **Education: graduate level (vs college)** | **+0.7675** | 0.2358 | ±0.4715 | **+3.255** | **0.0011** | ** |
| **Education: high school or below (vs college)** | **-2.0178** | 0.6149 | ±1.2299 | **-3.281** | **0.0010** | ** |
| Site: UCSD (vs UAB) | -0.4807 | 0.3162 | ±0.6323 | -1.520 | 0.1284 |  |
| Site: UW (vs UAB) | -0.4946 | 0.2791 | ±0.5583 | -1.772 | 0.0764 | . |
| **Age (years)** | **-0.0613** | 0.0122 | ±0.0244 | **-5.022** | **5.11e-07** | *** |
| BMI (kg/m2) | -0.0210 | 0.0145 | ±0.0290 | -1.446 | 0.1481 |  |
| Hypertension | -0.2953 | 0.2537 | ±0.5073 | -1.164 | 0.2445 |  |
| **High cholesterol** | **+0.6171** | 0.2479 | ±0.4958 | **+2.489** | **0.0128** | * |
| Kidney disease | +0.0009 | 0.4126 | ±0.8253 | +0.002 | 0.9983 |  |
| Circulatory disease | -0.2136 | 0.3204 | ±0.6409 | -0.666 | 0.5051 |  |
| Time 54-69, pooled (%) | -0.0552 | 0.0474 | ±0.0948 | -1.166 | 0.2438 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **638**, R² = **0.1328**, Adj R² = **0.1176**, F-statistic = **8.72** (p = **1.79e-14**), Residual SE = **2.841** on **626** df, AIC = **3154.9**, BIC = **3208.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.4039** | 0.9213 | ±1.8426 | **+33.001** | **7.86e-239** | *** |
| **Education: graduate level (vs college)** | **+0.7657** | 0.2362 | ±0.4724 | **+3.241** | **0.0012** | ** |
| **Education: high school or below (vs college)** | **-2.0172** | 0.6150 | ±1.2299 | **-3.280** | **0.0010** | ** |
| Site: UCSD (vs UAB) | -0.4763 | 0.3161 | ±0.6323 | -1.507 | 0.1319 |  |
| Site: UW (vs UAB) | -0.4967 | 0.2798 | ±0.5596 | -1.775 | 0.0759 | . |
| **Age (years)** | **-0.0611** | 0.0122 | ±0.0244 | **-5.008** | **5.51e-07** | *** |
| BMI (kg/m2) | -0.0209 | 0.0145 | ±0.0290 | -1.440 | 0.1498 |  |
| Hypertension | -0.2946 | 0.2540 | ±0.5080 | -1.160 | 0.2461 |  |
| **High cholesterol** | **+0.6176** | 0.2478 | ±0.4957 | **+2.492** | **0.0127** | * |
| Kidney disease | -0.0007 | 0.4126 | ±0.8252 | -0.002 | 0.9987 |  |
| Circulatory disease | -0.2138 | 0.3206 | ±0.6412 | -0.667 | 0.5049 |  |
| Avg. daily time 54-69 (%) | -0.0530 | 0.0477 | ±0.0954 | -1.110 | 0.2669 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **638**, R² = **0.1324**, Adj R² = **0.1172**, F-statistic = **8.69** (p = **2.04e-14**), Residual SE = **2.842** on **626** df, AIC = **3155.2**, BIC = **3208.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.4347** | 0.9247 | ±1.8493 | **+32.914** | **1.37e-237** | *** |
| **Education: graduate level (vs college)** | **+0.7709** | 0.2357 | ±0.4715 | **+3.270** | **0.0011** | ** |
| **Education: high school or below (vs college)** | **-2.0230** | 0.6152 | ±1.2304 | **-3.289** | **0.0010** | ** |
| Site: UCSD (vs UAB) | -0.4862 | 0.3171 | ±0.6342 | -1.533 | 0.1252 |  |
| Site: UW (vs UAB) | -0.4965 | 0.2791 | ±0.5583 | -1.778 | 0.0753 | . |
| **Age (years)** | **-0.0614** | 0.0122 | ±0.0244 | **-5.027** | **4.98e-07** | *** |
| BMI (kg/m2) | -0.0211 | 0.0145 | ±0.0290 | -1.453 | 0.1462 |  |
| Hypertension | -0.2936 | 0.2537 | ±0.5074 | -1.157 | 0.2471 |  |
| **High cholesterol** | **+0.6141** | 0.2482 | ±0.4963 | **+2.475** | **0.0133** | * |
| Kidney disease | -0.0019 | 0.4119 | ±0.8239 | -0.005 | 0.9962 |  |
| Circulatory disease | -0.2109 | 0.3204 | ±0.6407 | -0.658 | 0.5103 |  |
| Time < 70 (%) | -0.0388 | 0.0383 | ±0.0766 | -1.013 | 0.3109 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **638**, R² = **0.1325**, Adj R² = **0.1172**, F-statistic = **8.69** (p = **2.01e-14**), Residual SE = **2.842** on **626** df, AIC = **3155.2**, BIC = **3208.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.4024** | 0.9207 | ±1.8415 | **+33.020** | **4.20e-239** | *** |
| **Education: graduate level (vs college)** | **+0.7676** | 0.2362 | ±0.4723 | **+3.250** | **0.0012** | ** |
| **Education: high school or below (vs college)** | **-2.0219** | 0.6151 | ±1.2303 | **-3.287** | **0.0010** | ** |
| Site: UCSD (vs UAB) | -0.4803 | 0.3169 | ±0.6338 | -1.516 | 0.1296 |  |
| Site: UW (vs UAB) | -0.4985 | 0.2800 | ±0.5600 | -1.780 | 0.0750 | . |
| **Age (years)** | **-0.0611** | 0.0122 | ±0.0244 | **-5.007** | **5.54e-07** | *** |
| BMI (kg/m2) | -0.0210 | 0.0145 | ±0.0290 | -1.446 | 0.1482 |  |
| Hypertension | -0.2934 | 0.2541 | ±0.5083 | -1.155 | 0.2482 |  |
| **High cholesterol** | **+0.6151** | 0.2480 | ±0.4961 | **+2.480** | **0.0132** | * |
| Kidney disease | -0.0015 | 0.4122 | ±0.8243 | -0.004 | 0.9972 |  |
| Circulatory disease | -0.2108 | 0.3204 | ±0.6408 | -0.658 | 0.5105 |  |
| Avg. daily time < 70 (%) | -0.0389 | 0.0388 | ±0.0776 | -1.001 | 0.3166 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **638**, R² = **0.1492**, Adj R² = **0.1343**, F-statistic = **9.98** (p = **7.57e-17**), Residual SE = **2.814** on **626** df, AIC = **3142.7**, BIC = **3196.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.2705** | 2.6531 | ±5.3063 | **+8.771** | **1.77e-18** | *** |
| **Education: graduate level (vs college)** | **+0.7449** | 0.2336 | ±0.4671 | **+3.189** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **-1.8989** | 0.6088 | ±1.2177 | **-3.119** | **0.0018** | ** |
| Site: UCSD (vs UAB) | -0.5011 | 0.3072 | ±0.6145 | -1.631 | 0.1029 |  |
| **Site: UW (vs UAB)** | **-0.5594** | 0.2790 | ±0.5581 | **-2.005** | **0.0450** | * |
| **Age (years)** | **-0.0621** | 0.0123 | ±0.0246 | **-5.053** | **4.35e-07** | *** |
| BMI (kg/m2) | -0.0216 | 0.0144 | ±0.0288 | -1.504 | 0.1325 |  |
| Hypertension | -0.2195 | 0.2533 | ±0.5065 | -0.867 | 0.3861 |  |
| **High cholesterol** | **+0.5969** | 0.2467 | ±0.4935 | **+2.419** | **0.0156** | * |
| Kidney disease | +0.1000 | 0.4099 | ±0.8199 | +0.244 | 0.8073 |  |
| Circulatory disease | -0.1787 | 0.3114 | ±0.6229 | -0.574 | 0.5660 |  |
| **Time 54-250, pooled (%)** | **+0.0725** | 0.0248 | ±0.0496 | **+2.922** | **0.0035** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **638**, R² = **0.1511**, Adj R² = **0.1361**, F-statistic = **10.13** (p = **4.07e-17**), Residual SE = **2.811** on **626** df, AIC = **3141.3**, BIC = **3194.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.0962** | 2.8732 | ±5.7464 | **+7.690** | **1.47e-14** | *** |
| **Education: graduate level (vs college)** | **+0.7381** | 0.2337 | ±0.4673 | **+3.159** | **0.0016** | ** |
| **Education: high school or below (vs college)** | **-1.8727** | 0.6054 | ±1.2107 | **-3.093** | **0.0020** | ** |
| Site: UCSD (vs UAB) | -0.4946 | 0.3060 | ±0.6120 | -1.616 | 0.1060 |  |
| **Site: UW (vs UAB)** | **-0.5605** | 0.2794 | ±0.5588 | **-2.006** | **0.0449** | * |
| **Age (years)** | **-0.0616** | 0.0123 | ±0.0246 | **-5.009** | **5.49e-07** | *** |
| BMI (kg/m2) | -0.0220 | 0.0144 | ±0.0288 | -1.528 | 0.1264 |  |
| Hypertension | -0.2157 | 0.2529 | ±0.5059 | -0.853 | 0.3937 |  |
| **High cholesterol** | **+0.6001** | 0.2463 | ±0.4927 | **+2.436** | **0.0149** | * |
| Kidney disease | +0.1280 | 0.4098 | ±0.8195 | +0.312 | 0.7547 |  |
| Circulatory disease | -0.1694 | 0.3113 | ±0.6227 | -0.544 | 0.5863 |  |
| **Avg. daily time 54-250 (%)** | **+0.0840** | 0.0271 | ±0.0541 | **+3.102** | **0.0019** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **638**, R² = **0.1450**, Adj R² = **0.1300**, F-statistic = **9.65** (p = **3.15e-16**), Residual SE = **2.821** on **626** df, AIC = **3145.9**, BIC = **3199.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.3273** | 0.9069 | ±1.8137 | **+33.442** | **3.40e-245** | *** |
| **Education: graduate level (vs college)** | **+0.7654** | 0.2321 | ±0.4642 | **+3.298** | **9.74e-04** | *** |
| **Education: high school or below (vs college)** | **-1.9197** | 0.6045 | ±1.2090 | **-3.176** | **0.0015** | ** |
| Site: UCSD (vs UAB) | -0.4508 | 0.3072 | ±0.6144 | -1.468 | 0.1422 |  |
| Site: UW (vs UAB) | -0.5074 | 0.2787 | ±0.5574 | -1.820 | 0.0687 | . |
| **Age (years)** | **-0.0599** | 0.0123 | ±0.0247 | **-4.860** | **1.17e-06** | *** |
| BMI (kg/m2) | -0.0195 | 0.0142 | ±0.0284 | -1.377 | 0.1687 |  |
| Hypertension | -0.1937 | 0.2505 | ±0.5010 | -0.773 | 0.4395 |  |
| **High cholesterol** | **+0.6860** | 0.2477 | ±0.4955 | **+2.769** | **0.0056** | ** |
| Kidney disease | +0.2049 | 0.4157 | ±0.8313 | +0.493 | 0.6220 |  |
| Circulatory disease | -0.2014 | 0.3170 | ±0.6340 | -0.635 | 0.5251 |  |
| **Time 181-250, pooled (%)** | **-0.0413** | 0.0146 | ±0.0292 | **-2.827** | **0.0047** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **638**, R² = **0.1444**, Adj R² = **0.1294**, F-statistic = **9.60** (p = **3.84e-16**), Residual SE = **2.822** on **626** df, AIC = **3146.3**, BIC = **3199.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.3442** | 0.9075 | ±1.8150 | **+33.437** | **3.93e-245** | *** |
| **Education: graduate level (vs college)** | **+0.7665** | 0.2321 | ±0.4643 | **+3.302** | **9.60e-04** | *** |
| **Education: high school or below (vs college)** | **-1.9221** | 0.6058 | ±1.2116 | **-3.173** | **0.0015** | ** |
| Site: UCSD (vs UAB) | -0.4587 | 0.3079 | ±0.6159 | -1.489 | 0.1364 |  |
| Site: UW (vs UAB) | -0.5124 | 0.2790 | ±0.5580 | -1.837 | 0.0663 | . |
| **Age (years)** | **-0.0602** | 0.0123 | ±0.0246 | **-4.888** | **1.02e-06** | *** |
| BMI (kg/m2) | -0.0195 | 0.0142 | ±0.0284 | -1.375 | 0.1691 |  |
| Hypertension | -0.1982 | 0.2508 | ±0.5016 | -0.790 | 0.4292 |  |
| **High cholesterol** | **+0.6833** | 0.2477 | ±0.4954 | **+2.759** | **0.0058** | ** |
| Kidney disease | +0.1970 | 0.4142 | ±0.8283 | +0.476 | 0.6343 |  |
| Circulatory disease | -0.2044 | 0.3167 | ±0.6333 | -0.645 | 0.5187 |  |
| **Avg. daily time 181-250 (%)** | **-0.0392** | 0.0139 | ±0.0279 | **-2.814** | **0.0049** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **638**, R² = **0.1513**, Adj R² = **0.1364**, F-statistic = **10.15** (p = **3.73e-17**), Residual SE = **2.811** on **626** df, AIC = **3141.2**, BIC = **3194.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.3874** | 0.9066 | ±1.8133 | **+33.517** | **2.74e-246** | *** |
| **Education: graduate level (vs college)** | **+0.7511** | 0.2318 | ±0.4637 | **+3.240** | **0.0012** | ** |
| **Education: high school or below (vs college)** | **-1.8742** | 0.6035 | ±1.2069 | **-3.106** | **0.0019** | ** |
| Site: UCSD (vs UAB) | -0.4617 | 0.3042 | ±0.6084 | -1.518 | 0.1291 |  |
| Site: UW (vs UAB) | -0.5360 | 0.2790 | ±0.5580 | -1.921 | 0.0547 | . |
| **Age (years)** | **-0.0604** | 0.0123 | ±0.0246 | **-4.903** | **9.43e-07** | *** |
| BMI (kg/m2) | -0.0200 | 0.0142 | ±0.0284 | -1.408 | 0.1590 |  |
| Hypertension | -0.1761 | 0.2505 | ±0.5010 | -0.703 | 0.4819 |  |
| **High cholesterol** | **+0.6675** | 0.2462 | ±0.4925 | **+2.711** | **0.0067** | ** |
| Kidney disease | +0.2225 | 0.4144 | ±0.8289 | +0.537 | 0.5913 |  |
| Circulatory disease | -0.1894 | 0.3129 | ±0.6257 | -0.605 | 0.5450 |  |
| **Time > 180 (%)** | **-0.0346** | 0.0106 | ±0.0211 | **-3.277** | **0.0010** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **638**, R² = **0.1507**, Adj R² = **0.1357**, F-statistic = **10.10** (p = **4.64e-17**), Residual SE = **2.812** on **626** df, AIC = **3141.6**, BIC = **3195.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.3916** | 0.9073 | ±1.8145 | **+33.498** | **5.11e-246** | *** |
| **Education: graduate level (vs college)** | **+0.7527** | 0.2319 | ±0.4638 | **+3.246** | **0.0012** | ** |
| **Education: high school or below (vs college)** | **-1.8719** | 0.6035 | ±1.2070 | **-3.102** | **0.0019** | ** |
| Site: UCSD (vs UAB) | -0.4657 | 0.3046 | ±0.6093 | -1.529 | 0.1263 |  |
| Site: UW (vs UAB) | -0.5359 | 0.2792 | ±0.5583 | -1.920 | 0.0549 | . |
| **Age (years)** | **-0.0605** | 0.0123 | ±0.0246 | **-4.910** | **9.09e-07** | *** |
| BMI (kg/m2) | -0.0201 | 0.0142 | ±0.0284 | -1.414 | 0.1573 |  |
| Hypertension | -0.1805 | 0.2505 | ±0.5010 | -0.721 | 0.4711 |  |
| **High cholesterol** | **+0.6696** | 0.2465 | ±0.4929 | **+2.717** | **0.0066** | ** |
| Kidney disease | +0.2245 | 0.4137 | ±0.8274 | +0.543 | 0.5873 |  |
| Circulatory disease | -0.1904 | 0.3128 | ±0.6256 | -0.609 | 0.5428 |  |
| **Avg. daily time > 180 (%)** | **-0.0341** | 0.0107 | ±0.0213 | **-3.198** | **0.0014** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **638**, R² = **0.1479**, Adj R² = **0.1329**, F-statistic = **9.88** (p = **1.18e-16**), Residual SE = **2.816** on **626** df, AIC = **3143.7**, BIC = **3197.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.3791** | 0.9073 | ±1.8146 | **+33.482** | **8.77e-246** | *** |
| **Education: graduate level (vs college)** | **+0.7479** | 0.2325 | ±0.4650 | **+3.217** | **0.0013** | ** |
| **Education: high school or below (vs college)** | **-1.9253** | 0.6049 | ±1.2099 | **-3.183** | **0.0015** | ** |
| Site: UCSD (vs UAB) | -0.4804 | 0.3069 | ±0.6139 | -1.565 | 0.1176 |  |
| Site: UW (vs UAB) | -0.5229 | 0.2802 | ±0.5605 | -1.866 | 0.0620 | . |
| **Age (years)** | **-0.0618** | 0.0122 | ±0.0245 | **-5.045** | **4.53e-07** | *** |
| BMI (kg/m2) | -0.0189 | 0.0142 | ±0.0284 | -1.329 | 0.1838 |  |
| Hypertension | -0.1878 | 0.2507 | ±0.5014 | -0.749 | 0.4537 |  |
| **High cholesterol** | **+0.6633** | 0.2463 | ±0.4926 | **+2.693** | **0.0071** | ** |
| Kidney disease | +0.0717 | 0.4104 | ±0.8208 | +0.175 | 0.8613 |  |
| Circulatory disease | -0.1835 | 0.3125 | ±0.6250 | -0.587 | 0.5572 |  |
| **Nocturnal time > 180 (%)** | **-0.0329** | 0.0109 | ±0.0219 | **-3.008** | **0.0026** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **638**, R² = **0.1390**, Adj R² = **0.1239**, F-statistic = **9.19** (p = **2.31e-15**), Residual SE = **2.831** on **626** df, AIC = **3150.3**, BIC = **3203.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.3882** | 0.9115 | ±1.8231 | **+33.337** | **1.11e-243** | *** |
| **Education: graduate level (vs college)** | **+0.7492** | 0.2327 | ±0.4655 | **+3.219** | **0.0013** | ** |
| **Education: high school or below (vs college)** | **-1.9535** | 0.6076 | ±1.2152 | **-3.215** | **0.0013** | ** |
| Site: UCSD (vs UAB) | -0.4332 | 0.3097 | ±0.6194 | -1.399 | 0.1618 |  |
| Site: UW (vs UAB) | -0.4845 | 0.2788 | ±0.5577 | -1.738 | 0.0823 | . |
| **Age (years)** | **-0.0594** | 0.0125 | ±0.0250 | **-4.755** | **1.98e-06** | *** |
| BMI (kg/m2) | -0.0228 | 0.0144 | ±0.0289 | -1.578 | 0.1146 |  |
| Hypertension | -0.2067 | 0.2535 | ±0.5070 | -0.815 | 0.4149 |  |
| **High cholesterol** | **+0.6368** | 0.2469 | ±0.4937 | **+2.580** | **0.0099** | ** |
| Kidney disease | +0.1345 | 0.4252 | ±0.8505 | +0.316 | 0.7517 |  |
| Circulatory disease | -0.2143 | 0.3207 | ±0.6414 | -0.668 | 0.5039 |  |
| **Any reading > 250 during wear (0/1)** | **-0.6163** | 0.2870 | ±0.5740 | **-2.148** | **0.0318** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **638**, R² = **0.1494**, Adj R² = **0.1345**, F-statistic = **10.00** (p = **7.01e-17**), Residual SE = **2.814** on **626** df, AIC = **3142.6**, BIC = **3196.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.4693** | 0.9122 | ±1.8245 | **+33.401** | **1.33e-244** | *** |
| **Education: graduate level (vs college)** | **+0.7468** | 0.2334 | ±0.4668 | **+3.200** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **-1.8850** | 0.6086 | ±1.2171 | **-3.097** | **0.0020** | ** |
| Site: UCSD (vs UAB) | -0.4780 | 0.3059 | ±0.6119 | -1.563 | 0.1182 |  |
| Site: UW (vs UAB) | -0.5416 | 0.2788 | ±0.5576 | -1.943 | 0.0521 | . |
| **Age (years)** | **-0.0622** | 0.0123 | ±0.0246 | **-5.060** | **4.19e-07** | *** |
| BMI (kg/m2) | -0.0214 | 0.0144 | ±0.0287 | -1.495 | 0.1350 |  |
| Hypertension | -0.2123 | 0.2540 | ±0.5080 | -0.836 | 0.4033 |  |
| **High cholesterol** | **+0.6057** | 0.2468 | ±0.4935 | **+2.455** | **0.0141** | * |
| Kidney disease | +0.1005 | 0.4110 | ±0.8219 | +0.244 | 0.8069 |  |
| Circulatory disease | -0.1800 | 0.3113 | ±0.6226 | -0.578 | 0.5631 |  |
| **Time > 250 (%)** | **-0.0740** | 0.0255 | ±0.0511 | **-2.898** | **0.0038** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 638)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **638**, R² = **0.1514**, Adj R² = **0.1365**, F-statistic = **10.15** (p = **3.61e-17**), Residual SE = **2.811** on **626** df, AIC = **3141.1**, BIC = **3194.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.4668** | 0.9125 | ±1.8249 | **+33.390** | **1.92e-244** | *** |
| **Education: graduate level (vs college)** | **+0.7431** | 0.2333 | ±0.4666 | **+3.185** | **0.0014** | ** |
| **Education: high school or below (vs college)** | **-1.8571** | 0.6056 | ±1.2113 | **-3.066** | **0.0022** | ** |
| Site: UCSD (vs UAB) | -0.4754 | 0.3047 | ±0.6093 | -1.560 | 0.1187 |  |
| Site: UW (vs UAB) | -0.5410 | 0.2790 | ±0.5581 | -1.939 | 0.0525 | . |
| **Age (years)** | **-0.0619** | 0.0123 | ±0.0246 | **-5.038** | **4.69e-07** | *** |
| BMI (kg/m2) | -0.0219 | 0.0144 | ±0.0287 | -1.524 | 0.1274 |  |
| Hypertension | -0.2075 | 0.2535 | ±0.5070 | -0.819 | 0.4131 |  |
| **High cholesterol** | **+0.6087** | 0.2463 | ±0.4925 | **+2.472** | **0.0134** | * |
| Kidney disease | +0.1271 | 0.4103 | ±0.8205 | +0.310 | 0.7568 |  |
| Circulatory disease | -0.1715 | 0.3113 | ±0.6225 | -0.551 | 0.5818 |  |
| **Avg. daily time > 250 (%)** | **-0.0863** | 0.0282 | ±0.0564 | **-3.062** | **0.0022** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 638; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0670**, LLR χ² = **55.72** (p = **2.32e-08**), AUC = **0.6743**, AIC = **798.1**, BIC = **847.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2307** | 0.7042 | ±1.4084 | **-4.588** | **4.48e-06** | 0.0395 | *** |
| **Education: graduate level (vs college)** | **-0.6831** | 0.1970 | ±0.3940 | **-3.467** | **5.26e-04** | 0.5051 | *** |
| **Education: high school or below (vs college)** | **+0.7593** | 0.2927 | ±0.5854 | **+2.594** | **0.0095** | 2.1368 | ** |
| Site: UCSD (vs UAB) | +0.1968 | 0.2265 | ±0.4531 | +0.869 | 0.3849 | 1.2175 |  |
| Site: UW (vs UAB) | -0.0678 | 0.2075 | ±0.4151 | -0.327 | 0.7437 | 0.9344 |  |
| **Age (years)** | **+0.0387** | 0.0086 | ±0.0171 | **+4.521** | **6.17e-06** | 1.0395 | *** |
| BMI (kg/m2) | +0.0185 | 0.0118 | ±0.0236 | +1.566 | 0.1174 | 1.0187 |  |
| Hypertension | -0.0964 | 0.1933 | ±0.3867 | -0.499 | 0.6179 | 0.9081 |  |
| High cholesterol | -0.2074 | 0.1829 | ±0.3658 | -1.134 | 0.2569 | 0.8127 |  |
| Kidney disease | -0.0291 | 0.3013 | ±0.6027 | -0.097 | 0.9230 | 0.9713 |  |
| Circulatory disease | +0.2127 | 0.2224 | ±0.4447 | +0.956 | 0.3389 | 1.2370 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0848**, LLR χ² = **70.58** (p = **9.48e-11**), AUC = **0.6958**, AIC = **785.2**, BIC = **838.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-5.4085** | 0.9386 | ±1.8773 | **-5.762** | **8.31e-09** | 0.0045 | *** |
| **Education: graduate level (vs college)** | **-0.6391** | 0.1992 | ±0.3983 | **-3.209** | **0.0013** | 0.5278 | ** |
| **Education: high school or below (vs college)** | **+0.6474** | 0.2997 | ±0.5994 | **+2.160** | **0.0308** | 1.9105 | * |
| Site: UCSD (vs UAB) | +0.1713 | 0.2299 | ±0.4598 | +0.745 | 0.4563 | 1.1868 |  |
| Site: UW (vs UAB) | -0.0039 | 0.2108 | ±0.4215 | -0.018 | 0.9853 | 0.9961 |  |
| **Age (years)** | **+0.0358** | 0.0087 | ±0.0174 | **+4.110** | **3.96e-05** | 1.0364 | *** |
| BMI (kg/m2) | +0.0146 | 0.0120 | ±0.0241 | +1.212 | 0.2255 | 1.0147 |  |
| Hypertension | -0.1875 | 0.1974 | ±0.3947 | -0.950 | 0.3420 | 0.8290 |  |
| High cholesterol | -0.2596 | 0.1865 | ±0.3731 | -1.392 | 0.1640 | 0.7713 |  |
| Kidney disease | -0.0995 | 0.3100 | ±0.6199 | -0.321 | 0.7481 | 0.9053 |  |
| Circulatory disease | +0.2316 | 0.2265 | ±0.4529 | +1.023 | 0.3064 | 1.2606 |  |
| **HbA1c (%)** | **+0.4257** | 0.1169 | ±0.2337 | **+3.643** | **2.70e-04** | 1.5306 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0740**, LLR χ² = **61.54** (p = **4.79e-09**), AUC = **0.6813**, AIC = **794.3**, BIC = **847.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.1931** | 0.8176 | ±1.6352 | **-5.128** | **2.92e-07** | 0.0151 | *** |
| **Education: graduate level (vs college)** | **-0.6864** | 0.1977 | ±0.3954 | **-3.472** | **5.16e-04** | 0.5034 | *** |
| **Education: high school or below (vs college)** | **+0.6936** | 0.2956 | ±0.5912 | **+2.347** | **0.0189** | 2.0009 | * |
| Site: UCSD (vs UAB) | +0.1955 | 0.2281 | ±0.4562 | +0.857 | 0.3913 | 1.2160 |  |
| Site: UW (vs UAB) | -0.0544 | 0.2084 | ±0.4168 | -0.261 | 0.7941 | 0.9471 |  |
| **Age (years)** | **+0.0384** | 0.0086 | ±0.0172 | **+4.476** | **7.60e-06** | 1.0392 | *** |
| BMI (kg/m2) | +0.0172 | 0.0119 | ±0.0238 | +1.445 | 0.1486 | 1.0173 |  |
| Hypertension | -0.1629 | 0.1964 | ±0.3929 | -0.829 | 0.4070 | 0.8497 |  |
| High cholesterol | -0.2340 | 0.1844 | ±0.3688 | -1.269 | 0.2045 | 0.7914 |  |
| Kidney disease | -0.1089 | 0.3062 | ±0.6123 | -0.356 | 0.7221 | 0.8968 |  |
| Circulatory disease | +0.2051 | 0.2243 | ±0.4486 | +0.914 | 0.3607 | 1.2276 |  |
| **Mean glucose (mg/dL)** | **+0.0088** | 0.0037 | ±0.0074 | **+2.374** | **0.0176** | 1.0088 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0740**, LLR χ² = **61.54** (p = **4.79e-09**), AUC = **0.6813**, AIC = **794.3**, BIC = **847.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-5.4104** | 1.1636 | ±2.3273 | **-4.650** | **3.33e-06** | 0.0045 | *** |
| **Education: graduate level (vs college)** | **-0.6864** | 0.1977 | ±0.3954 | **-3.472** | **5.16e-04** | 0.5034 | *** |
| **Education: high school or below (vs college)** | **+0.6936** | 0.2956 | ±0.5912 | **+2.347** | **0.0189** | 2.0009 | * |
| Site: UCSD (vs UAB) | +0.1955 | 0.2281 | ±0.4562 | +0.857 | 0.3913 | 1.2160 |  |
| Site: UW (vs UAB) | -0.0544 | 0.2084 | ±0.4168 | -0.261 | 0.7941 | 0.9471 |  |
| **Age (years)** | **+0.0384** | 0.0086 | ±0.0172 | **+4.476** | **7.60e-06** | 1.0392 | *** |
| BMI (kg/m2) | +0.0172 | 0.0119 | ±0.0238 | +1.445 | 0.1486 | 1.0173 |  |
| Hypertension | -0.1629 | 0.1964 | ±0.3929 | -0.829 | 0.4070 | 0.8497 |  |
| High cholesterol | -0.2340 | 0.1844 | ±0.3688 | -1.269 | 0.2045 | 0.7914 |  |
| Kidney disease | -0.1089 | 0.3062 | ±0.6123 | -0.356 | 0.7221 | 0.8968 |  |
| Circulatory disease | +0.2051 | 0.2243 | ±0.4486 | +0.914 | 0.3607 | 1.2276 |  |
| **GMI (%)** | **+0.3678** | 0.1549 | ±0.3099 | **+2.374** | **0.0176** | 1.4445 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0715**, LLR χ² = **59.51** (p = **1.14e-08**), AUC = **0.6783**, AIC = **796.3**, BIC = **849.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.0036** | 0.8141 | ±1.6282 | **-4.918** | **8.75e-07** | 0.0182 | *** |
| **Education: graduate level (vs college)** | **-0.6903** | 0.1975 | ±0.3949 | **-3.496** | **4.73e-04** | 0.5014 | *** |
| **Education: high school or below (vs college)** | **+0.7067** | 0.2949 | ±0.5897 | **+2.397** | **0.0165** | 2.0272 | * |
| Site: UCSD (vs UAB) | +0.1929 | 0.2276 | ±0.4552 | +0.848 | 0.3966 | 1.2128 |  |
| Site: UW (vs UAB) | -0.0609 | 0.2080 | ±0.4161 | -0.293 | 0.7698 | 0.9409 |  |
| **Age (years)** | **+0.0393** | 0.0086 | ±0.0172 | **+4.579** | **4.68e-06** | 1.0401 | *** |
| BMI (kg/m2) | +0.0165 | 0.0119 | ±0.0238 | +1.387 | 0.1654 | 1.0166 |  |
| Hypertension | -0.1464 | 0.1957 | ±0.3915 | -0.748 | 0.4545 | 0.8638 |  |
| High cholesterol | -0.2353 | 0.1842 | ±0.3684 | -1.277 | 0.2016 | 0.7904 |  |
| Kidney disease | -0.0477 | 0.3031 | ±0.6061 | -0.157 | 0.8750 | 0.9535 |  |
| Circulatory disease | +0.2096 | 0.2240 | ±0.4480 | +0.936 | 0.3495 | 1.2332 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0071 | 0.0037 | ±0.0073 | +1.925 | 0.0542 | 1.0071 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0769**, LLR χ² = **63.97** (p = **1.68e-09**), AUC = **0.6844**, AIC = **791.8**, BIC = **845.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.6014** | 0.7219 | ±1.4439 | **-4.989** | **6.08e-07** | 0.0273 | *** |
| **Education: graduate level (vs college)** | **-0.6690** | 0.1982 | ±0.3964 | **-3.375** | **7.37e-04** | 0.5122 | *** |
| **Education: high school or below (vs college)** | **+0.6479** | 0.2967 | ±0.5935 | **+2.184** | **0.0290** | 1.9116 | * |
| Site: UCSD (vs UAB) | +0.1976 | 0.2288 | ±0.4575 | +0.864 | 0.3876 | 1.2185 |  |
| Site: UW (vs UAB) | -0.0163 | 0.2096 | ±0.4193 | -0.078 | 0.9382 | 0.9839 |  |
| **Age (years)** | **+0.0361** | 0.0086 | ±0.0173 | **+4.181** | **2.90e-05** | 1.0368 | *** |
| BMI (kg/m2) | +0.0183 | 0.0119 | ±0.0238 | +1.542 | 0.1230 | 1.0185 |  |
| Hypertension | -0.1765 | 0.1971 | ±0.3941 | -0.896 | 0.3703 | 0.8382 |  |
| High cholesterol | -0.2114 | 0.1846 | ±0.3692 | -1.145 | 0.2521 | 0.8094 |  |
| Kidney disease | -0.2213 | 0.3147 | ±0.6294 | -0.703 | 0.4820 | 0.8015 |  |
| Circulatory disease | +0.2291 | 0.2240 | ±0.4481 | +1.023 | 0.3065 | 1.2575 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0217** | 0.0077 | ±0.0155 | **+2.809** | **0.0050** | 1.0220 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0748**, LLR χ² = **62.24** (p = **3.54e-09**), AUC = **0.6826**, AIC = **793.6**, BIC = **847.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.5603** | 0.7207 | ±1.4414 | **-4.940** | **7.81e-07** | 0.0284 | *** |
| **Education: graduate level (vs college)** | **-0.6672** | 0.1980 | ±0.3961 | **-3.369** | **7.54e-04** | 0.5132 | *** |
| **Education: high school or below (vs college)** | **+0.6464** | 0.2969 | ±0.5939 | **+2.177** | **0.0295** | 1.9086 | * |
| Site: UCSD (vs UAB) | +0.1927 | 0.2282 | ±0.4564 | +0.844 | 0.3985 | 1.2125 |  |
| Site: UW (vs UAB) | -0.0293 | 0.2092 | ±0.4184 | -0.140 | 0.8884 | 0.9711 |  |
| **Age (years)** | **+0.0362** | 0.0086 | ±0.0173 | **+4.187** | **2.83e-05** | 1.0368 | *** |
| BMI (kg/m2) | +0.0184 | 0.0119 | ±0.0237 | +1.552 | 0.1207 | 1.0186 |  |
| Hypertension | -0.1636 | 0.1966 | ±0.3932 | -0.832 | 0.4052 | 0.8491 |  |
| High cholesterol | -0.2141 | 0.1842 | ±0.3684 | -1.162 | 0.2452 | 0.8073 |  |
| Kidney disease | -0.2057 | 0.3143 | ±0.6286 | -0.655 | 0.5128 | 0.8141 |  |
| Circulatory disease | +0.2345 | 0.2236 | ±0.4473 | +1.048 | 0.2945 | 1.2642 |  |
| **Avg. daily SD (mg/dL)** | **+0.0224** | 0.0089 | ±0.0179 | **+2.507** | **0.0122** | 1.0227 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0745**, LLR χ² = **62.01** (p = **3.92e-09**), AUC = **0.6837**, AIC = **793.8**, BIC = **847.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.8135** | 0.7491 | ±1.4982 | **-5.091** | **3.57e-07** | 0.0221 | *** |
| **Education: graduate level (vs college)** | **-0.6674** | 0.1981 | ±0.3963 | **-3.368** | **7.56e-04** | 0.5130 | *** |
| **Education: high school or below (vs college)** | **+0.6723** | 0.2950 | ±0.5900 | **+2.279** | **0.0227** | 1.9588 | * |
| Site: UCSD (vs UAB) | +0.1954 | 0.2282 | ±0.4563 | +0.856 | 0.3918 | 1.2158 |  |
| Site: UW (vs UAB) | -0.0140 | 0.2098 | ±0.4197 | -0.067 | 0.9467 | 0.9861 |  |
| **Age (years)** | **+0.0352** | 0.0087 | ±0.0174 | **+4.062** | **4.87e-05** | 1.0359 | *** |
| BMI (kg/m2) | +0.0190 | 0.0119 | ±0.0237 | +1.598 | 0.1099 | 1.0191 |  |
| Hypertension | -0.1511 | 0.1959 | ±0.3918 | -0.771 | 0.4406 | 0.8598 |  |
| High cholesterol | -0.1936 | 0.1842 | ±0.3684 | -1.051 | 0.2932 | 0.8240 |  |
| Kidney disease | -0.2104 | 0.3146 | ±0.6293 | -0.669 | 0.5036 | 0.8102 |  |
| Circulatory disease | +0.2334 | 0.2231 | ±0.4461 | +1.047 | 0.2953 | 1.2629 |  |
| **CV (%)** | **+0.0376** | 0.0151 | ±0.0302 | **+2.491** | **0.0127** | 1.0383 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0737**, LLR χ² = **61.34** (p = **5.22e-09**), AUC = **0.6841**, AIC = **794.5**, BIC = **848.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.1238** | 0.8411 | ±1.6821 | **-2.525** | **0.0116** | 0.1196 | * |
| **Education: graduate level (vs college)** | **-0.6814** | 0.1980 | ±0.3961 | **-3.441** | **5.80e-04** | 0.5059 | *** |
| **Education: high school or below (vs college)** | **+0.6771** | 0.2947 | ±0.5895 | **+2.297** | **0.0216** | 1.9682 | * |
| Site: UCSD (vs UAB) | +0.1818 | 0.2278 | ±0.4557 | +0.798 | 0.4250 | 1.1994 |  |
| Site: UW (vs UAB) | -0.0364 | 0.2091 | ±0.4182 | -0.174 | 0.8619 | 0.9643 |  |
| **Age (years)** | **+0.0352** | 0.0087 | ±0.0174 | **+4.057** | **4.97e-05** | 1.0359 | *** |
| BMI (kg/m2) | +0.0183 | 0.0118 | ±0.0237 | +1.545 | 0.1225 | 1.0184 |  |
| Hypertension | -0.1437 | 0.1956 | ±0.3912 | -0.735 | 0.4624 | 0.8661 |  |
| High cholesterol | -0.1978 | 0.1841 | ±0.3682 | -1.074 | 0.2827 | 0.8206 |  |
| Kidney disease | -0.1606 | 0.3096 | ±0.6192 | -0.519 | 0.6040 | 0.8517 |  |
| Circulatory disease | +0.2191 | 0.2228 | ±0.4455 | +0.983 | 0.3254 | 1.2449 |  |
| **Mean / SD ratio** | **-0.1697** | 0.0723 | ±0.1446 | **-2.347** | **0.0189** | 0.8439 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0708**, LLR χ² = **58.88** (p = **1.50e-08**), AUC = **0.6802**, AIC = **796.9**, BIC = **850.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.4040** | 0.8411 | ±1.6822 | **-2.858** | **0.0043** | 0.0904 | ** |
| **Education: graduate level (vs college)** | **-0.6798** | 0.1977 | ±0.3954 | **-3.439** | **5.84e-04** | 0.5067 | *** |
| **Education: high school or below (vs college)** | **+0.6881** | 0.2950 | ±0.5900 | **+2.333** | **0.0197** | 1.9900 | * |
| Site: UCSD (vs UAB) | +0.1749 | 0.2274 | ±0.4549 | +0.769 | 0.4420 | 1.1911 |  |
| Site: UW (vs UAB) | -0.0525 | 0.2084 | ±0.4169 | -0.252 | 0.8010 | 0.9488 |  |
| **Age (years)** | **+0.0359** | 0.0087 | ±0.0174 | **+4.123** | **3.73e-05** | 1.0365 | *** |
| BMI (kg/m2) | +0.0181 | 0.0118 | ±0.0237 | +1.529 | 0.1261 | 1.0183 |  |
| Hypertension | -0.1236 | 0.1948 | ±0.3895 | -0.635 | 0.5255 | 0.8837 |  |
| High cholesterol | -0.2042 | 0.1836 | ±0.3671 | -1.113 | 0.2659 | 0.8153 |  |
| Kidney disease | -0.1203 | 0.3077 | ±0.6153 | -0.391 | 0.6958 | 0.8867 |  |
| Circulatory disease | +0.2235 | 0.2225 | ±0.4451 | +1.005 | 0.3151 | 1.2505 |  |
| Avg. daily mean/SD | -0.1041 | 0.0590 | ±0.1181 | -1.763 | 0.0779 | 0.9011 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0684**, LLR χ² = **56.90** (p = **3.47e-08**), AUC = **0.6774**, AIC = **798.9**, BIC = **852.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.6329** | 0.7990 | ±1.5981 | **-4.547** | **5.45e-06** | 0.0264 | *** |
| **Education: graduate level (vs college)** | **-0.6807** | 0.1973 | ±0.3945 | **-3.450** | **5.60e-04** | 0.5063 | *** |
| **Education: high school or below (vs college)** | **+0.7267** | 0.2939 | ±0.5877 | **+2.473** | **0.0134** | 2.0683 | * |
| Site: UCSD (vs UAB) | +0.1881 | 0.2271 | ±0.4542 | +0.828 | 0.4075 | 1.2070 |  |
| Site: UW (vs UAB) | -0.0398 | 0.2094 | ±0.4188 | -0.190 | 0.8494 | 0.9610 |  |
| **Age (years)** | **+0.0388** | 0.0086 | ±0.0171 | **+4.523** | **6.09e-06** | 1.0395 | *** |
| BMI (kg/m2) | +0.0179 | 0.0118 | ±0.0236 | +1.511 | 0.1308 | 1.0180 |  |
| Hypertension | -0.1089 | 0.1940 | ±0.3881 | -0.561 | 0.5746 | 0.8968 |  |
| High cholesterol | -0.2004 | 0.1833 | ±0.3665 | -1.093 | 0.2742 | 0.8184 |  |
| Kidney disease | -0.0402 | 0.3024 | ±0.6047 | -0.133 | 0.8943 | 0.9606 |  |
| Circulatory disease | +0.2176 | 0.2224 | ±0.4449 | +0.978 | 0.3280 | 1.2431 |  |
| MAG (mg/dL/h) | +0.0099 | 0.0092 | ±0.0183 | +1.085 | 0.2781 | 1.0100 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0719**, LLR χ² = **59.77** (p = **1.02e-08**), AUC = **0.6808**, AIC = **796.0**, BIC = **849.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.6481** | 0.7387 | ±1.4775 | **-4.938** | **7.88e-07** | 0.0260 | *** |
| **Education: graduate level (vs college)** | **-0.6686** | 0.1978 | ±0.3955 | **-3.380** | **7.24e-04** | 0.5124 | *** |
| **Education: high school or below (vs college)** | **+0.6699** | 0.2960 | ±0.5920 | **+2.263** | **0.0236** | 1.9541 | * |
| Site: UCSD (vs UAB) | +0.1924 | 0.2276 | ±0.4552 | +0.845 | 0.3980 | 1.2121 |  |
| Site: UW (vs UAB) | -0.0392 | 0.2088 | ±0.4175 | -0.188 | 0.8511 | 0.9616 |  |
| **Age (years)** | **+0.0369** | 0.0086 | ±0.0172 | **+4.286** | **1.82e-05** | 1.0376 | *** |
| BMI (kg/m2) | +0.0193 | 0.0119 | ±0.0237 | +1.626 | 0.1040 | 1.0195 |  |
| Hypertension | -0.1418 | 0.1957 | ±0.3914 | -0.725 | 0.4686 | 0.8678 |  |
| High cholesterol | -0.2088 | 0.1837 | ±0.3673 | -1.137 | 0.2557 | 0.8116 |  |
| Kidney disease | -0.1566 | 0.3113 | ±0.6225 | -0.503 | 0.6149 | 0.8550 |  |
| Circulatory disease | +0.2201 | 0.2229 | ±0.4458 | +0.987 | 0.3234 | 1.2462 |  |
| **Avg. daily range (mg/dL)** | **+0.0046** | 0.0023 | ±0.0046 | **+2.001** | **0.0454** | 1.0046 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0734**, LLR χ² = **61.03** (p = **5.96e-09**), AUC = **0.6833**, AIC = **794.8**, BIC = **848.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4155** | 0.7120 | ±1.4240 | **-4.797** | **1.61e-06** | 0.0329 | *** |
| **Education: graduate level (vs college)** | **-0.6756** | 0.1977 | ±0.3954 | **-3.417** | **6.33e-04** | 0.5088 | *** |
| **Education: high school or below (vs college)** | **+0.7341** | 0.2943 | ±0.5885 | **+2.495** | **0.0126** | 2.0836 | * |
| Site: UCSD (vs UAB) | +0.2093 | 0.2284 | ±0.4568 | +0.916 | 0.3595 | 1.2328 |  |
| Site: UW (vs UAB) | -0.0281 | 0.2090 | ±0.4180 | -0.134 | 0.8931 | 0.9723 |  |
| **Age (years)** | **+0.0379** | 0.0086 | ±0.0172 | **+4.417** | **1.00e-05** | 1.0387 | *** |
| BMI (kg/m2) | +0.0178 | 0.0119 | ±0.0237 | +1.500 | 0.1335 | 1.0179 |  |
| Hypertension | -0.1492 | 0.1957 | ±0.3914 | -0.763 | 0.4456 | 0.8614 |  |
| High cholesterol | -0.2128 | 0.1842 | ±0.3685 | -1.155 | 0.2481 | 0.8083 |  |
| Kidney disease | -0.1183 | 0.3070 | ±0.6140 | -0.385 | 0.7000 | 0.8884 |  |
| Circulatory disease | +0.1956 | 0.2241 | ±0.4483 | +0.872 | 0.3830 | 1.2160 |  |
| **SD of daily means (mg/dL)** | **+0.0300** | 0.0135 | ±0.0269 | **+2.225** | **0.0261** | 1.0304 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0793**, LLR χ² = **65.96** (p = **7.10e-10**), AUC = **0.6894**, AIC = **789.8**, BIC = **843.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.1206 | 0.9766 | ±1.9533 | -1.147 | 0.2512 | 0.3261 |  |
| **Education: graduate level (vs college)** | **-0.6614** | 0.1985 | ±0.3970 | **-3.332** | **8.63e-04** | 0.5161 | *** |
| **Education: high school or below (vs college)** | **+0.6850** | 0.2966 | ±0.5932 | **+2.310** | **0.0209** | 1.9838 | * |
| Site: UCSD (vs UAB) | +0.2229 | 0.2295 | ±0.4590 | +0.971 | 0.3315 | 1.2497 |  |
| Site: UW (vs UAB) | +0.0024 | 0.2103 | ±0.4207 | +0.011 | 0.9909 | 1.0024 |  |
| **Age (years)** | **+0.0378** | 0.0086 | ±0.0172 | **+4.392** | **1.13e-05** | 1.0385 | *** |
| BMI (kg/m2) | +0.0178 | 0.0119 | ±0.0238 | +1.491 | 0.1359 | 1.0179 |  |
| Hypertension | -0.1579 | 0.1961 | ±0.3922 | -0.805 | 0.4209 | 0.8540 |  |
| High cholesterol | -0.2353 | 0.1854 | ±0.3708 | -1.269 | 0.2043 | 0.7903 |  |
| Kidney disease | -0.1900 | 0.3116 | ±0.6232 | -0.610 | 0.5420 | 0.8269 |  |
| Circulatory disease | +0.2101 | 0.2253 | ±0.4506 | +0.933 | 0.3510 | 1.2338 |  |
| **Time in range 70-180, pooled (%)** | **-0.0220** | 0.0071 | ±0.0142 | **-3.101** | **0.0019** | 0.9783 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0786**, LLR χ² = **65.38** (p = **9.13e-10**), AUC = **0.6884**, AIC = **790.4**, BIC = **843.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.1840 | 0.9737 | ±1.9474 | -1.216 | 0.2240 | 0.3061 |  |
| **Education: graduate level (vs college)** | **-0.6616** | 0.1985 | ±0.3970 | **-3.333** | **8.58e-04** | 0.5160 | *** |
| **Education: high school or below (vs college)** | **+0.6843** | 0.2964 | ±0.5928 | **+2.309** | **0.0210** | 1.9824 | * |
| Site: UCSD (vs UAB) | +0.2214 | 0.2293 | ±0.4586 | +0.966 | 0.3342 | 1.2479 |  |
| Site: UW (vs UAB) | +0.0016 | 0.2103 | ±0.4206 | +0.008 | 0.9940 | 1.0016 |  |
| **Age (years)** | **+0.0377** | 0.0086 | ±0.0172 | **+4.384** | **1.16e-05** | 1.0384 | *** |
| BMI (kg/m2) | +0.0177 | 0.0119 | ±0.0238 | +1.491 | 0.1360 | 1.0179 |  |
| Hypertension | -0.1540 | 0.1960 | ±0.3920 | -0.786 | 0.4321 | 0.8573 |  |
| High cholesterol | -0.2363 | 0.1853 | ±0.3706 | -1.275 | 0.2023 | 0.7896 |  |
| Kidney disease | -0.1885 | 0.3118 | ±0.6237 | -0.604 | 0.5456 | 0.8282 |  |
| Circulatory disease | +0.2106 | 0.2251 | ±0.4502 | +0.936 | 0.3495 | 1.2344 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0211** | 0.0070 | ±0.0140 | **-3.026** | **0.0025** | 0.9791 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0677**, LLR χ² = **56.30** (p = **4.48e-08**), AUC = **0.6766**, AIC = **799.5**, BIC = **853.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2879** | 0.7086 | ±1.4172 | **-4.640** | **3.48e-06** | 0.0373 | *** |
| **Education: graduate level (vs college)** | **-0.6803** | 0.1971 | ±0.3943 | **-3.451** | **5.59e-04** | 0.5065 | *** |
| **Education: high school or below (vs college)** | **+0.7711** | 0.2933 | ±0.5865 | **+2.629** | **0.0086** | 2.1620 | ** |
| Site: UCSD (vs UAB) | +0.2223 | 0.2292 | ±0.4584 | +0.970 | 0.3320 | 1.2490 |  |
| Site: UW (vs UAB) | -0.0449 | 0.2099 | ±0.4198 | -0.214 | 0.8307 | 0.9561 |  |
| **Age (years)** | **+0.0386** | 0.0086 | ±0.0171 | **+4.511** | **6.46e-06** | 1.0394 | *** |
| BMI (kg/m2) | +0.0187 | 0.0118 | ±0.0236 | +1.585 | 0.1129 | 1.0189 |  |
| Hypertension | -0.0900 | 0.1936 | ±0.3871 | -0.465 | 0.6420 | 0.9139 |  |
| High cholesterol | -0.1982 | 0.1834 | ±0.3669 | -1.081 | 0.2799 | 0.8202 |  |
| Kidney disease | -0.0309 | 0.3012 | ±0.6025 | -0.103 | 0.9183 | 0.9696 |  |
| Circulatory disease | +0.2110 | 0.2225 | ±0.4449 | +0.948 | 0.3429 | 1.2349 |  |
| Time < 54 (%) | +0.0742 | 0.0992 | ±0.1984 | +0.748 | 0.4546 | 1.0770 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0679**, LLR χ² = **56.44** (p = **4.21e-08**), AUC = **0.6767**, AIC = **799.4**, BIC = **852.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2662** | 0.7057 | ±1.4114 | **-4.628** | **3.69e-06** | 0.0382 | *** |
| **Education: graduate level (vs college)** | **-0.6763** | 0.1973 | ±0.3946 | **-3.428** | **6.09e-04** | 0.5085 | *** |
| **Education: high school or below (vs college)** | **+0.7725** | 0.2932 | ±0.5864 | **+2.635** | **0.0084** | 2.1652 | ** |
| Site: UCSD (vs UAB) | +0.2209 | 0.2285 | ±0.4570 | +0.967 | 0.3336 | 1.2472 |  |
| Site: UW (vs UAB) | -0.0397 | 0.2104 | ±0.4208 | -0.189 | 0.8504 | 0.9611 |  |
| **Age (years)** | **+0.0383** | 0.0086 | ±0.0171 | **+4.474** | **7.69e-06** | 1.0391 | *** |
| BMI (kg/m2) | +0.0186 | 0.0118 | ±0.0236 | +1.577 | 0.1147 | 1.0188 |  |
| Hypertension | -0.0891 | 0.1936 | ±0.3873 | -0.460 | 0.6454 | 0.9148 |  |
| High cholesterol | -0.1968 | 0.1835 | ±0.3670 | -1.072 | 0.2836 | 0.8214 |  |
| Kidney disease | -0.0343 | 0.3014 | ±0.6027 | -0.114 | 0.9093 | 0.9663 |  |
| Circulatory disease | +0.2098 | 0.2225 | ±0.4450 | +0.943 | 0.3457 | 1.2335 |  |
| Avg. daily time < 54 (%) | +0.0952 | 0.1129 | ±0.2258 | +0.843 | 0.3993 | 1.0998 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0740**, LLR χ² = **61.54** (p = **4.79e-09**), AUC = **0.6813**, AIC = **794.3**, BIC = **847.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3740** | 0.7099 | ±1.4198 | **-4.753** | **2.01e-06** | 0.0343 | *** |
| **Education: graduate level (vs college)** | **-0.6592** | 0.1982 | ±0.3964 | **-3.326** | **8.81e-04** | 0.5173 | *** |
| **Education: high school or below (vs college)** | **+0.7704** | 0.2946 | ±0.5891 | **+2.616** | **0.0089** | 2.1607 | ** |
| Site: UCSD (vs UAB) | +0.2401 | 0.2285 | ±0.4570 | +1.051 | 0.2933 | 1.2714 |  |
| Site: UW (vs UAB) | -0.0108 | 0.2101 | ±0.4203 | -0.051 | 0.9592 | 0.9893 |  |
| **Age (years)** | **+0.0379** | 0.0086 | ±0.0172 | **+4.417** | **1.00e-05** | 1.0386 | *** |
| BMI (kg/m2) | +0.0182 | 0.0118 | ±0.0237 | +1.537 | 0.1244 | 1.0184 |  |
| Hypertension | -0.0686 | 0.1947 | ±0.3894 | -0.352 | 0.7247 | 0.9337 |  |
| High cholesterol | -0.1988 | 0.1841 | ±0.3683 | -1.079 | 0.2804 | 0.8198 |  |
| Kidney disease | -0.0538 | 0.3022 | ±0.6044 | -0.178 | 0.8586 | 0.9476 |  |
| Circulatory disease | +0.2277 | 0.2234 | ±0.4468 | +1.019 | 0.3081 | 1.2557 |  |
| **Time 54-69, pooled (%)** | **+0.0910** | 0.0380 | ±0.0760 | **+2.394** | **0.0167** | 1.0952 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0743**, LLR χ² = **61.79** (p = **4.30e-09**), AUC = **0.6812**, AIC = **794.0**, BIC = **847.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3340** | 0.7084 | ±1.4168 | **-4.707** | **2.52e-06** | 0.0357 | *** |
| **Education: graduate level (vs college)** | **-0.6556** | 0.1983 | ±0.3966 | **-3.306** | **9.45e-04** | 0.5191 | *** |
| **Education: high school or below (vs college)** | **+0.7710** | 0.2946 | ±0.5892 | **+2.617** | **0.0089** | 2.1619 | ** |
| Site: UCSD (vs UAB) | +0.2338 | 0.2283 | ±0.4567 | +1.024 | 0.3058 | 1.2634 |  |
| Site: UW (vs UAB) | -0.0054 | 0.2104 | ±0.4208 | -0.026 | 0.9793 | 0.9946 |  |
| **Age (years)** | **+0.0375** | 0.0086 | ±0.0172 | **+4.371** | **1.24e-05** | 1.0382 | *** |
| BMI (kg/m2) | +0.0181 | 0.0118 | ±0.0237 | +1.526 | 0.1270 | 1.0182 |  |
| Hypertension | -0.0692 | 0.1947 | ±0.3895 | -0.355 | 0.7222 | 0.9331 |  |
| High cholesterol | -0.1986 | 0.1841 | ±0.3683 | -1.079 | 0.2807 | 0.8198 |  |
| Kidney disease | -0.0508 | 0.3021 | ±0.6041 | -0.168 | 0.8665 | 0.9505 |  |
| Circulatory disease | +0.2281 | 0.2234 | ±0.4467 | +1.021 | 0.3071 | 1.2562 |  |
| **Avg. daily time 54-69 (%)** | **+0.0895** | 0.0367 | ±0.0735 | **+2.438** | **0.0148** | 1.0937 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0728**, LLR χ² = **60.52** (p = **7.42e-09**), AUC = **0.6813**, AIC = **795.3**, BIC = **848.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3860** | 0.7105 | ±1.4210 | **-4.766** | **1.88e-06** | 0.0338 | *** |
| **Education: graduate level (vs college)** | **-0.6631** | 0.1980 | ±0.3960 | **-3.349** | **8.10e-04** | 0.5152 | *** |
| **Education: high school or below (vs college)** | **+0.7773** | 0.2943 | ±0.5885 | **+2.642** | **0.0082** | 2.1757 | ** |
| Site: UCSD (vs UAB) | +0.2517 | 0.2290 | ±0.4580 | +1.099 | 0.2718 | 1.2862 |  |
| Site: UW (vs UAB) | -0.0049 | 0.2106 | ±0.4211 | -0.023 | 0.9814 | 0.9951 |  |
| **Age (years)** | **+0.0380** | 0.0086 | ±0.0172 | **+4.433** | **9.27e-06** | 1.0388 | *** |
| BMI (kg/m2) | +0.0184 | 0.0118 | ±0.0237 | +1.558 | 0.1192 | 1.0186 |  |
| Hypertension | -0.0693 | 0.1945 | ±0.3890 | -0.356 | 0.7215 | 0.9330 |  |
| High cholesterol | -0.1923 | 0.1840 | ±0.3680 | -1.045 | 0.2961 | 0.8251 |  |
| Kidney disease | -0.0491 | 0.3019 | ±0.6038 | -0.163 | 0.8708 | 0.9521 |  |
| Circulatory disease | +0.2231 | 0.2233 | ±0.4465 | +0.999 | 0.3176 | 1.2500 |  |
| **Time < 70 (%)** | **+0.0670** | 0.0309 | ±0.0617 | **+2.172** | **0.0299** | 1.0693 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0731**, LLR χ² = **60.81** (p = **6.56e-09**), AUC = **0.6812**, AIC = **795.0**, BIC = **848.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3318** | 0.7080 | ±1.4160 | **-4.706** | **2.53e-06** | 0.0357 | *** |
| **Education: graduate level (vs college)** | **-0.6575** | 0.1981 | ±0.3962 | **-3.319** | **9.05e-04** | 0.5182 | *** |
| **Education: high school or below (vs college)** | **+0.7767** | 0.2942 | ±0.5885 | **+2.639** | **0.0083** | 2.1742 | ** |
| Site: UCSD (vs UAB) | +0.2416 | 0.2285 | ±0.4570 | +1.057 | 0.2904 | 1.2733 |  |
| Site: UW (vs UAB) | -0.0007 | 0.2108 | ±0.4215 | -0.003 | 0.9974 | 0.9993 |  |
| **Age (years)** | **+0.0375** | 0.0086 | ±0.0172 | **+4.373** | **1.22e-05** | 1.0382 | *** |
| BMI (kg/m2) | +0.0182 | 0.0118 | ±0.0237 | +1.541 | 0.1233 | 1.0184 |  |
| Hypertension | -0.0702 | 0.1946 | ±0.3891 | -0.361 | 0.7184 | 0.9323 |  |
| High cholesterol | -0.1928 | 0.1840 | ±0.3680 | -1.048 | 0.2947 | 0.8246 |  |
| Kidney disease | -0.0492 | 0.3018 | ±0.6037 | -0.163 | 0.8705 | 0.9520 |  |
| Circulatory disease | +0.2230 | 0.2233 | ±0.4465 | +0.999 | 0.3178 | 1.2499 |  |
| **Avg. daily time < 70 (%)** | **+0.0676** | 0.0303 | ±0.0606 | **+2.232** | **0.0256** | 1.0699 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0758**, LLR χ² = **63.03** (p = **2.52e-09**), AUC = **0.6839**, AIC = **792.8**, BIC = **846.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.3417 | 2.1592 | ±4.3185 | +0.621 | 0.5343 | 3.8256 |  |
| **Education: graduate level (vs college)** | **-0.6628** | 0.1977 | ±0.3955 | **-3.352** | **8.03e-04** | 0.5154 | *** |
| **Education: high school or below (vs college)** | **+0.6892** | 0.2970 | ±0.5939 | **+2.321** | **0.0203** | 1.9922 | * |
| Site: UCSD (vs UAB) | +0.2281 | 0.2289 | ±0.4579 | +0.996 | 0.3191 | 1.2562 |  |
| Site: UW (vs UAB) | -0.0058 | 0.2096 | ±0.4192 | -0.028 | 0.9779 | 0.9942 |  |
| **Age (years)** | **+0.0388** | 0.0086 | ±0.0172 | **+4.518** | **6.25e-06** | 1.0396 | *** |
| BMI (kg/m2) | +0.0187 | 0.0119 | ±0.0237 | +1.577 | 0.1148 | 1.0189 |  |
| Hypertension | -0.1309 | 0.1950 | ±0.3900 | -0.671 | 0.5019 | 0.8773 |  |
| High cholesterol | -0.1963 | 0.1845 | ±0.3689 | -1.064 | 0.2872 | 0.8218 |  |
| Kidney disease | -0.1042 | 0.3065 | ±0.6129 | -0.340 | 0.7339 | 0.9011 |  |
| Circulatory disease | +0.2072 | 0.2247 | ±0.4495 | +0.922 | 0.3566 | 1.2302 |  |
| **Time 54-250, pooled (%)** | **-0.0467** | 0.0207 | ±0.0414 | **-2.257** | **0.0240** | 0.9544 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0750**, LLR χ² = **62.43** (p = **3.27e-09**), AUC = **0.6827**, AIC = **793.4**, BIC = **846.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.5887 | 2.2869 | ±4.5738 | +0.695 | 0.4872 | 4.8976 |  |
| **Education: graduate level (vs college)** | **-0.6607** | 0.1977 | ±0.3955 | **-3.341** | **8.34e-04** | 0.5165 | *** |
| **Education: high school or below (vs college)** | **+0.6817** | 0.2972 | ±0.5944 | **+2.294** | **0.0218** | 1.9772 | * |
| Site: UCSD (vs UAB) | +0.2231 | 0.2289 | ±0.4577 | +0.975 | 0.3297 | 1.2499 |  |
| Site: UW (vs UAB) | -0.0102 | 0.2095 | ±0.4190 | -0.049 | 0.9610 | 0.9898 |  |
| **Age (years)** | **+0.0385** | 0.0086 | ±0.0172 | **+4.489** | **7.15e-06** | 1.0393 | *** |
| BMI (kg/m2) | +0.0188 | 0.0118 | ±0.0237 | +1.585 | 0.1131 | 1.0190 |  |
| Hypertension | -0.1296 | 0.1949 | ±0.3899 | -0.665 | 0.5061 | 0.8784 |  |
| High cholesterol | -0.1996 | 0.1844 | ±0.3687 | -1.083 | 0.2789 | 0.8190 |  |
| Kidney disease | -0.1141 | 0.3074 | ±0.6148 | -0.371 | 0.7105 | 0.8922 |  |
| Circulatory disease | +0.2058 | 0.2248 | ±0.4495 | +0.915 | 0.3599 | 1.2285 |  |
| **Avg. daily time 54-250 (%)** | **-0.0489** | 0.0220 | ±0.0439 | **-2.227** | **0.0259** | 0.9523 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0731**, LLR χ² = **60.83** (p = **6.50e-09**), AUC = **0.6834**, AIC = **795.0**, BIC = **848.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2305** | 0.7055 | ±1.4109 | **-4.579** | **4.67e-06** | 0.0395 | *** |
| **Education: graduate level (vs college)** | **-0.6775** | 0.1978 | ±0.3956 | **-3.425** | **6.15e-04** | 0.5079 | *** |
| **Education: high school or below (vs college)** | **+0.7145** | 0.2945 | ±0.5889 | **+2.426** | **0.0153** | 2.0431 | * |
| Site: UCSD (vs UAB) | +0.1954 | 0.2279 | ±0.4557 | +0.858 | 0.3911 | 1.2158 |  |
| Site: UW (vs UAB) | -0.0434 | 0.2087 | ±0.4174 | -0.208 | 0.8353 | 0.9576 |  |
| **Age (years)** | **+0.0379** | 0.0086 | ±0.0172 | **+4.411** | **1.03e-05** | 1.0386 | *** |
| BMI (kg/m2) | +0.0177 | 0.0119 | ±0.0237 | +1.490 | 0.1362 | 1.0178 |  |
| Hypertension | -0.1462 | 0.1955 | ±0.3910 | -0.748 | 0.4545 | 0.8640 |  |
| High cholesterol | -0.2433 | 0.1847 | ±0.3695 | -1.317 | 0.1879 | 0.7841 |  |
| Kidney disease | -0.1486 | 0.3096 | ±0.6193 | -0.480 | 0.6312 | 0.8619 |  |
| Circulatory disease | +0.2117 | 0.2237 | ±0.4475 | +0.946 | 0.3441 | 1.2357 |  |
| **Time 181-250, pooled (%)** | **+0.0219** | 0.0097 | ±0.0194 | **+2.263** | **0.0236** | 1.0221 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0732**, LLR χ² = **60.93** (p = **6.23e-09**), AUC = **0.6832**, AIC = **794.9**, BIC = **848.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2398** | 0.7056 | ±1.4112 | **-4.591** | **4.40e-06** | 0.0392 | *** |
| **Education: graduate level (vs college)** | **-0.6784** | 0.1979 | ±0.3957 | **-3.429** | **6.07e-04** | 0.5074 | *** |
| **Education: high school or below (vs college)** | **+0.7140** | 0.2944 | ±0.5888 | **+2.426** | **0.0153** | 2.0422 | * |
| Site: UCSD (vs UAB) | +0.2000 | 0.2279 | ±0.4557 | +0.878 | 0.3801 | 1.2214 |  |
| Site: UW (vs UAB) | -0.0395 | 0.2088 | ±0.4176 | -0.189 | 0.8499 | 0.9612 |  |
| **Age (years)** | **+0.0380** | 0.0086 | ±0.0172 | **+4.431** | **9.39e-06** | 1.0388 | *** |
| BMI (kg/m2) | +0.0176 | 0.0119 | ±0.0237 | +1.486 | 0.1372 | 1.0178 |  |
| Hypertension | -0.1450 | 0.1954 | ±0.3909 | -0.742 | 0.4583 | 0.8650 |  |
| High cholesterol | -0.2429 | 0.1847 | ±0.3694 | -1.315 | 0.1884 | 0.7843 |  |
| Kidney disease | -0.1481 | 0.3096 | ±0.6193 | -0.478 | 0.6325 | 0.8624 |  |
| Circulatory disease | +0.2132 | 0.2237 | ±0.4474 | +0.953 | 0.3405 | 1.2377 |  |
| **Avg. daily time 181-250 (%)** | **+0.0214** | 0.0094 | ±0.0187 | **+2.286** | **0.0222** | 1.0217 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0758**, LLR χ² = **63.05** (p = **2.50e-09**), AUC = **0.6843**, AIC = **792.8**, BIC = **846.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2636** | 0.7068 | ±1.4136 | **-4.617** | **3.88e-06** | 0.0383 | *** |
| **Education: graduate level (vs college)** | **-0.6704** | 0.1980 | ±0.3961 | **-3.386** | **7.10e-04** | 0.5115 | *** |
| **Education: high school or below (vs college)** | **+0.6920** | 0.2958 | ±0.5916 | **+2.340** | **0.0193** | 1.9977 | * |
| Site: UCSD (vs UAB) | +0.2035 | 0.2286 | ±0.4571 | +0.891 | 0.3732 | 1.2257 |  |
| Site: UW (vs UAB) | -0.0259 | 0.2092 | ±0.4184 | -0.124 | 0.9015 | 0.9744 |  |
| **Age (years)** | **+0.0381** | 0.0086 | ±0.0172 | **+4.439** | **9.03e-06** | 1.0389 | *** |
| BMI (kg/m2) | +0.0179 | 0.0119 | ±0.0238 | +1.505 | 0.1324 | 1.0180 |  |
| Hypertension | -0.1552 | 0.1959 | ±0.3918 | -0.792 | 0.4281 | 0.8562 |  |
| High cholesterol | -0.2335 | 0.1848 | ±0.3696 | -1.264 | 0.2063 | 0.7917 |  |
| Kidney disease | -0.1577 | 0.3098 | ±0.6196 | -0.509 | 0.6108 | 0.8541 |  |
| Circulatory disease | +0.2072 | 0.2246 | ±0.4492 | +0.922 | 0.3563 | 1.2302 |  |
| **Time > 180 (%)** | **+0.0184** | 0.0069 | ±0.0139 | **+2.650** | **0.0081** | 1.0186 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0752**, LLR χ² = **62.54** (p = **3.11e-09**), AUC = **0.6833**, AIC = **793.3**, BIC = **846.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2639** | 0.7065 | ±1.4131 | **-4.620** | **3.84e-06** | 0.0382 | *** |
| **Education: graduate level (vs college)** | **-0.6717** | 0.1980 | ±0.3960 | **-3.393** | **6.92e-04** | 0.5108 | *** |
| **Education: high school or below (vs college)** | **+0.6919** | 0.2957 | ±0.5913 | **+2.340** | **0.0193** | 1.9975 | * |
| Site: UCSD (vs UAB) | +0.2056 | 0.2284 | ±0.4569 | +0.900 | 0.3681 | 1.2283 |  |
| Site: UW (vs UAB) | -0.0269 | 0.2092 | ±0.4184 | -0.129 | 0.8977 | 0.9735 |  |
| **Age (years)** | **+0.0382** | 0.0086 | ±0.0172 | **+4.447** | **8.70e-06** | 1.0389 | *** |
| BMI (kg/m2) | +0.0179 | 0.0119 | ±0.0238 | +1.510 | 0.1310 | 1.0181 |  |
| Hypertension | -0.1515 | 0.1957 | ±0.3914 | -0.774 | 0.4389 | 0.8594 |  |
| High cholesterol | -0.2341 | 0.1847 | ±0.3694 | -1.268 | 0.2049 | 0.7913 |  |
| Kidney disease | -0.1566 | 0.3100 | ±0.6201 | -0.505 | 0.6135 | 0.8550 |  |
| Circulatory disease | +0.2076 | 0.2245 | ±0.4490 | +0.925 | 0.3550 | 1.2308 |  |
| **Avg. daily time > 180 (%)** | **+0.0177** | 0.0069 | ±0.0138 | **+2.565** | **0.0103** | 1.0179 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0734**, LLR χ² = **61.08** (p = **5.83e-09**), AUC = **0.6827**, AIC = **794.7**, BIC = **848.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2559** | 0.7061 | ±1.4121 | **-4.611** | **4.00e-06** | 0.0385 | *** |
| **Education: graduate level (vs college)** | **-0.6694** | 0.1978 | ±0.3956 | **-3.384** | **7.14e-04** | 0.5120 | *** |
| **Education: high school or below (vs college)** | **+0.7162** | 0.2944 | ±0.5887 | **+2.433** | **0.0150** | 2.0467 | * |
| Site: UCSD (vs UAB) | +0.2132 | 0.2283 | ±0.4565 | +0.934 | 0.3503 | 1.2376 |  |
| Site: UW (vs UAB) | -0.0351 | 0.2089 | ±0.4177 | -0.168 | 0.8665 | 0.9655 |  |
| **Age (years)** | **+0.0388** | 0.0086 | ±0.0172 | **+4.526** | **6.01e-06** | 1.0396 | *** |
| BMI (kg/m2) | +0.0174 | 0.0119 | ±0.0237 | +1.467 | 0.1423 | 1.0176 |  |
| Hypertension | -0.1456 | 0.1954 | ±0.3907 | -0.745 | 0.4562 | 0.8645 |  |
| High cholesterol | -0.2278 | 0.1842 | ±0.3685 | -1.236 | 0.2163 | 0.7963 |  |
| Kidney disease | -0.0722 | 0.3047 | ±0.6093 | -0.237 | 0.8126 | 0.9303 |  |
| Circulatory disease | +0.2042 | 0.2244 | ±0.4488 | +0.910 | 0.3627 | 1.2266 |  |
| **Nocturnal time > 180 (%)** | **+0.0164** | 0.0072 | ±0.0145 | **+2.262** | **0.0237** | 1.0165 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0685**, LLR χ² = **56.99** (p = **3.34e-08**), AUC = **0.6761**, AIC = **798.8**, BIC = **852.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2506** | 0.7050 | ±1.4100 | **-4.611** | **4.01e-06** | 0.0388 | *** |
| **Education: graduate level (vs college)** | **-0.6715** | 0.1974 | ±0.3949 | **-3.401** | **6.71e-04** | 0.5109 | *** |
| **Education: high school or below (vs college)** | **+0.7388** | 0.2932 | ±0.5864 | **+2.520** | **0.0117** | 2.0935 | * |
| Site: UCSD (vs UAB) | +0.1893 | 0.2269 | ±0.4537 | +0.834 | 0.4041 | 1.2083 |  |
| Site: UW (vs UAB) | -0.0595 | 0.2079 | ±0.4158 | -0.286 | 0.7747 | 0.9422 |  |
| **Age (years)** | **+0.0379** | 0.0086 | ±0.0172 | **+4.408** | **1.04e-05** | 1.0386 | *** |
| BMI (kg/m2) | +0.0192 | 0.0118 | ±0.0237 | +1.622 | 0.1049 | 1.0194 |  |
| Hypertension | -0.1263 | 0.1956 | ±0.3912 | -0.646 | 0.5184 | 0.8813 |  |
| High cholesterol | -0.2115 | 0.1833 | ±0.3665 | -1.154 | 0.2484 | 0.8094 |  |
| Kidney disease | -0.0824 | 0.3060 | ±0.6120 | -0.269 | 0.7876 | 0.9209 |  |
| Circulatory disease | +0.2169 | 0.2226 | ±0.4451 | +0.975 | 0.3297 | 1.2423 |  |
| Any reading > 250 during wear (0/1) | +0.2195 | 0.1944 | ±0.3888 | +1.129 | 0.2590 | 1.2454 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0752**, LLR χ² = **62.59** (p = **3.05e-09**), AUC = **0.6827**, AIC = **793.2**, BIC = **846.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2916** | 0.7072 | ±1.4143 | **-4.655** | **3.24e-06** | 0.0372 | *** |
| **Education: graduate level (vs college)** | **-0.6649** | 0.1977 | ±0.3953 | **-3.364** | **7.68e-04** | 0.5143 | *** |
| **Education: high school or below (vs college)** | **+0.6834** | 0.2971 | ±0.5943 | **+2.300** | **0.0215** | 1.9806 | * |
| Site: UCSD (vs UAB) | +0.2119 | 0.2285 | ±0.4570 | +0.927 | 0.3538 | 1.2360 |  |
| Site: UW (vs UAB) | -0.0209 | 0.2090 | ±0.4179 | -0.100 | 0.9204 | 0.9793 |  |
| **Age (years)** | **+0.0389** | 0.0086 | ±0.0172 | **+4.525** | **6.03e-06** | 1.0396 | *** |
| BMI (kg/m2) | +0.0185 | 0.0119 | ±0.0237 | +1.562 | 0.1182 | 1.0187 |  |
| Hypertension | -0.1345 | 0.1951 | ±0.3902 | -0.689 | 0.4907 | 0.8742 |  |
| High cholesterol | -0.2019 | 0.1844 | ±0.3688 | -1.095 | 0.2736 | 0.8172 |  |
| Kidney disease | -0.1013 | 0.3064 | ±0.6128 | -0.331 | 0.7410 | 0.9037 |  |
| Circulatory disease | +0.2085 | 0.2247 | ±0.4494 | +0.928 | 0.3534 | 1.2319 |  |
| **Time > 250 (%)** | **+0.0458** | 0.0209 | ±0.0417 | **+2.193** | **0.0283** | 1.0468 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 638)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **638**, events = **228**, McFadden pseudo-R² = **0.0746**, LLR χ² = **62.03** (p = **3.88e-09**), AUC = **0.6820**, AIC = **793.8**, BIC = **847.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2842** | 0.7068 | ±1.4136 | **-4.647** | **3.37e-06** | 0.0375 | *** |
| **Education: graduate level (vs college)** | **-0.6644** | 0.1976 | ±0.3952 | **-3.362** | **7.75e-04** | 0.5146 | *** |
| **Education: high school or below (vs college)** | **+0.6756** | 0.2975 | ±0.5951 | **+2.271** | **0.0232** | 1.9651 | * |
| Site: UCSD (vs UAB) | +0.2108 | 0.2286 | ±0.4571 | +0.922 | 0.3565 | 1.2346 |  |
| Site: UW (vs UAB) | -0.0248 | 0.2089 | ±0.4178 | -0.119 | 0.9056 | 0.9755 |  |
| **Age (years)** | **+0.0387** | 0.0086 | ±0.0172 | **+4.512** | **6.43e-06** | 1.0395 | *** |
| BMI (kg/m2) | +0.0187 | 0.0118 | ±0.0237 | +1.576 | 0.1150 | 1.0189 |  |
| Hypertension | -0.1331 | 0.1950 | ±0.3900 | -0.683 | 0.4949 | 0.8754 |  |
| High cholesterol | -0.2049 | 0.1843 | ±0.3686 | -1.112 | 0.2663 | 0.8147 |  |
| Kidney disease | -0.1107 | 0.3073 | ±0.6147 | -0.360 | 0.7186 | 0.8952 |  |
| Circulatory disease | +0.2076 | 0.2248 | ±0.4496 | +0.924 | 0.3557 | 1.2307 |  |
| **Avg. daily time > 250 (%)** | **+0.0486** | 0.0226 | ±0.0451 | **+2.155** | **0.0312** | 1.0498 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 638; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **638**, R² = **0.0879**, Adj R² = **0.0734**, F-statistic = **6.04** (p = **8.39e-09**), Residual SE = **2.544** on **627** df, AIC = **3013.0**, BIC = **3062.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9662** | 0.8982 | ±1.7964 | **+17.776** | **1.08e-70** | *** |
| Education: graduate level (vs college) | +0.4103 | 0.2221 | ±0.4442 | +1.847 | 0.0647 | . |
| **Education: high school or below (vs college)** | **-0.9457** | 0.4091 | ±0.8183 | **-2.312** | **0.0208** | * |
| Site: UCSD (vs UAB) | +0.1881 | 0.2811 | ±0.5623 | +0.669 | 0.5035 |  |
| Site: UW (vs UAB) | +0.1554 | 0.2504 | ±0.5009 | +0.621 | 0.5349 |  |
| **Age (years)** | **-0.0506** | 0.0113 | ±0.0226 | **-4.472** | **7.74e-06** | *** |
| BMI (kg/m2) | -0.0104 | 0.0147 | ±0.0293 | -0.709 | 0.4781 |  |
| **Hypertension** | **-0.5625** | 0.2210 | ±0.4420 | **-2.545** | **0.0109** | * |
| **High cholesterol** | **+0.5559** | 0.2261 | ±0.4523 | **+2.458** | **0.0140** | * |
| Kidney disease | -0.2713 | 0.3860 | ±0.7719 | -0.703 | 0.4821 |  |
| Circulatory disease | +0.2220 | 0.2734 | ±0.5468 | +0.812 | 0.4168 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **638**, R² = **0.0985**, Adj R² = **0.0827**, F-statistic = **6.22** (p = **9.03e-10**), Residual SE = **2.531** on **626** df, AIC = **3007.6**, BIC = **3061.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.6655** | 1.1039 | ±2.2079 | **+16.002** | **1.23e-57** | *** |
| Education: graduate level (vs college) | +0.3669 | 0.2225 | ±0.4450 | +1.649 | 0.0992 | . |
| **Education: high school or below (vs college)** | **-0.8431** | 0.4138 | ±0.8276 | **-2.038** | **0.0416** | * |
| Site: UCSD (vs UAB) | +0.2108 | 0.2777 | ±0.5554 | +0.759 | 0.4479 |  |
| Site: UW (vs UAB) | +0.1105 | 0.2508 | ±0.5015 | +0.441 | 0.6595 |  |
| **Age (years)** | **-0.0475** | 0.0113 | ±0.0226 | **-4.209** | **2.57e-05** | *** |
| BMI (kg/m2) | -0.0071 | 0.0143 | ±0.0286 | -0.497 | 0.6189 |  |
| **Hypertension** | **-0.4930** | 0.2189 | ±0.4378 | **-2.252** | **0.0243** | * |
| **High cholesterol** | **+0.5928** | 0.2260 | ±0.4520 | **+2.623** | **0.0087** | ** |
| Kidney disease | -0.2225 | 0.3892 | ±0.7784 | -0.572 | 0.5675 |  |
| Circulatory disease | +0.2140 | 0.2706 | ±0.5413 | +0.791 | 0.4291 |  |
| **HbA1c (%)** | **-0.3421** | 0.1230 | ±0.2461 | **-2.780** | **0.0054** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **638**, R² = **0.0942**, Adj R² = **0.0783**, F-statistic = **5.92** (p = **3.36e-09**), Residual SE = **2.537** on **626** df, AIC = **3010.6**, BIC = **3064.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9334** | 1.0111 | ±2.0223 | **+16.747** | **5.99e-63** | *** |
| Education: graduate level (vs college) | +0.4109 | 0.2217 | ±0.4434 | +1.853 | 0.0638 | . |
| **Education: high school or below (vs college)** | **-0.8719** | 0.4133 | ±0.8265 | **-2.110** | **0.0349** | * |
| Site: UCSD (vs UAB) | +0.1929 | 0.2784 | ±0.5568 | +0.693 | 0.4884 |  |
| Site: UW (vs UAB) | +0.1433 | 0.2505 | ±0.5011 | +0.572 | 0.5673 |  |
| **Age (years)** | **-0.0501** | 0.0113 | ±0.0227 | **-4.419** | **9.90e-06** | *** |
| BMI (kg/m2) | -0.0089 | 0.0146 | ±0.0292 | -0.611 | 0.5409 |  |
| **Hypertension** | **-0.4984** | 0.2228 | ±0.4456 | **-2.237** | **0.0253** | * |
| **High cholesterol** | **+0.5841** | 0.2269 | ±0.4539 | **+2.574** | **0.0101** | * |
| Kidney disease | -0.1900 | 0.3983 | ±0.7965 | -0.477 | 0.6332 |  |
| Circulatory disease | +0.2308 | 0.2705 | ±0.5409 | +0.853 | 0.3935 |  |
| Mean glucose (mg/dL) | -0.0090 | 0.0049 | ±0.0098 | -1.841 | 0.0656 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **638**, R² = **0.0942**, Adj R² = **0.0783**, F-statistic = **5.92** (p = **3.36e-09**), Residual SE = **2.537** on **626** df, AIC = **3010.6**, BIC = **3064.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.1776** | 1.4526 | ±2.9052 | **+12.514** | **6.29e-36** | *** |
| Education: graduate level (vs college) | +0.4109 | 0.2217 | ±0.4434 | +1.853 | 0.0638 | . |
| **Education: high school or below (vs college)** | **-0.8719** | 0.4133 | ±0.8265 | **-2.110** | **0.0349** | * |
| Site: UCSD (vs UAB) | +0.1929 | 0.2784 | ±0.5568 | +0.693 | 0.4884 |  |
| Site: UW (vs UAB) | +0.1433 | 0.2505 | ±0.5011 | +0.572 | 0.5673 |  |
| **Age (years)** | **-0.0501** | 0.0113 | ±0.0227 | **-4.419** | **9.90e-06** | *** |
| BMI (kg/m2) | -0.0089 | 0.0146 | ±0.0292 | -0.611 | 0.5409 |  |
| **Hypertension** | **-0.4984** | 0.2228 | ±0.4456 | **-2.237** | **0.0253** | * |
| **High cholesterol** | **+0.5841** | 0.2269 | ±0.4539 | **+2.574** | **0.0101** | * |
| Kidney disease | -0.1900 | 0.3983 | ±0.7965 | -0.477 | 0.6332 |  |
| Circulatory disease | +0.2308 | 0.2705 | ±0.5409 | +0.853 | 0.3935 |  |
| GMI (%) | -0.3759 | 0.2042 | ±0.4084 | -1.841 | 0.0656 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **638**, R² = **0.0948**, Adj R² = **0.0789**, F-statistic = **5.96** (p = **2.78e-09**), Residual SE = **2.537** on **626** df, AIC = **3010.2**, BIC = **3063.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9800** | 0.9906 | ±1.9811 | **+17.142** | **7.23e-66** | *** |
| Education: graduate level (vs college) | +0.4166 | 0.2218 | ±0.4436 | +1.878 | 0.0604 | . |
| **Education: high school or below (vs college)** | **-0.8719** | 0.4124 | ±0.8248 | **-2.114** | **0.0345** | * |
| Site: UCSD (vs UAB) | +0.1969 | 0.2784 | ±0.5567 | +0.707 | 0.4795 |  |
| Site: UW (vs UAB) | +0.1477 | 0.2504 | ±0.5008 | +0.590 | 0.5553 |  |
| **Age (years)** | **-0.0512** | 0.0113 | ±0.0226 | **-4.528** | **5.95e-06** | *** |
| BMI (kg/m2) | -0.0075 | 0.0147 | ±0.0294 | -0.509 | 0.6104 |  |
| **Hypertension** | **-0.5002** | 0.2226 | ±0.4452 | **-2.247** | **0.0246** | * |
| **High cholesterol** | **+0.5966** | 0.2275 | ±0.4550 | **+2.623** | **0.0087** | ** |
| Kidney disease | -0.2456 | 0.3904 | ±0.7807 | -0.629 | 0.5293 |  |
| Circulatory disease | +0.2244 | 0.2704 | ±0.5409 | +0.830 | 0.4067 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0094 | 0.0050 | ±0.0099 | -1.898 | 0.0577 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **638**, R² = **0.0972**, Adj R² = **0.0814**, F-statistic = **6.13** (p = **1.35e-09**), Residual SE = **2.533** on **626** df, AIC = **3008.5**, BIC = **3062.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3314** | 0.9110 | ±1.8219 | **+17.928** | **7.15e-72** | *** |
| Education: graduate level (vs college) | +0.3930 | 0.2218 | ±0.4435 | +1.772 | 0.0764 | . |
| **Education: high school or below (vs college)** | **-0.8218** | 0.4086 | ±0.8173 | **-2.011** | **0.0443** | * |
| Site: UCSD (vs UAB) | +0.1915 | 0.2777 | ±0.5553 | +0.690 | 0.4903 |  |
| Site: UW (vs UAB) | +0.1092 | 0.2519 | ±0.5038 | +0.433 | 0.6648 |  |
| **Age (years)** | **-0.0477** | 0.0114 | ±0.0227 | **-4.193** | **2.75e-05** | *** |
| BMI (kg/m2) | -0.0101 | 0.0145 | ±0.0290 | -0.695 | 0.4871 |  |
| **Hypertension** | **-0.4889** | 0.2211 | ±0.4421 | **-2.211** | **0.0270** | * |
| **High cholesterol** | **+0.5603** | 0.2261 | ±0.4521 | **+2.479** | **0.0132** | * |
| Kidney disease | -0.0787 | 0.4150 | ±0.8299 | -0.190 | 0.8495 |  |
| Circulatory disease | +0.2123 | 0.2710 | ±0.5420 | +0.783 | 0.4335 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.0226** | 0.0097 | ±0.0195 | **-2.322** | **0.0202** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **638**, R² = **0.0957**, Adj R² = **0.0798**, F-statistic = **6.02** (p = **2.13e-09**), Residual SE = **2.535** on **626** df, AIC = **3009.6**, BIC = **3063.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3029** | 0.9127 | ±1.8255 | **+17.862** | **2.35e-71** | *** |
| Education: graduate level (vs college) | +0.3910 | 0.2219 | ±0.4438 | +1.762 | 0.0780 | . |
| **Education: high school or below (vs college)** | **-0.8164** | 0.4076 | ±0.8152 | **-2.003** | **0.0452** | * |
| Site: UCSD (vs UAB) | +0.1961 | 0.2781 | ±0.5563 | +0.705 | 0.4808 |  |
| Site: UW (vs UAB) | +0.1195 | 0.2514 | ±0.5027 | +0.475 | 0.6345 |  |
| **Age (years)** | **-0.0477** | 0.0114 | ±0.0227 | **-4.190** | **2.78e-05** | *** |
| BMI (kg/m2) | -0.0102 | 0.0145 | ±0.0291 | -0.701 | 0.4831 |  |
| **Hypertension** | **-0.5006** | 0.2217 | ±0.4434 | **-2.258** | **0.0239** | * |
| **High cholesterol** | **+0.5643** | 0.2259 | ±0.4519 | **+2.498** | **0.0125** | * |
| Kidney disease | -0.0877 | 0.4124 | ±0.8249 | -0.213 | 0.8316 |  |
| Circulatory disease | +0.2065 | 0.2717 | ±0.5434 | +0.760 | 0.4473 |  |
| **Avg. daily SD (mg/dL)** | **-0.0241** | 0.0108 | ±0.0215 | **-2.236** | **0.0253** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **638**, R² = **0.0932**, Adj R² = **0.0772**, F-statistic = **5.85** (p = **4.55e-09**), Residual SE = **2.539** on **626** df, AIC = **3011.3**, BIC = **3064.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4731** | 0.9597 | ±1.9195 | **+17.164** | **4.94e-66** | *** |
| Education: graduate level (vs college) | +0.3951 | 0.2223 | ±0.4446 | +1.777 | 0.0755 | . |
| **Education: high school or below (vs college)** | **-0.8635** | 0.4051 | ±0.8101 | **-2.132** | **0.0330** | * |
| Site: UCSD (vs UAB) | +0.1929 | 0.2799 | ±0.5598 | +0.689 | 0.4907 |  |
| Site: UW (vs UAB) | +0.1148 | 0.2529 | ±0.5057 | +0.454 | 0.6498 |  |
| **Age (years)** | **-0.0474** | 0.0113 | ±0.0226 | **-4.192** | **2.76e-05** | *** |
| BMI (kg/m2) | -0.0107 | 0.0146 | ±0.0292 | -0.734 | 0.4629 |  |
| **Hypertension** | **-0.5223** | 0.2201 | ±0.4402 | **-2.373** | **0.0176** | * |
| **High cholesterol** | **+0.5443** | 0.2270 | ±0.4540 | **+2.398** | **0.0165** | * |
| Kidney disease | -0.1160 | 0.4119 | ±0.8239 | -0.282 | 0.7783 |  |
| Circulatory disease | +0.2107 | 0.2731 | ±0.5462 | +0.771 | 0.4405 |  |
| CV (%) | -0.0337 | 0.0176 | ±0.0353 | -1.911 | 0.0561 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **638**, R² = **0.0914**, Adj R² = **0.0755**, F-statistic = **5.73** (p = **7.63e-09**), Residual SE = **2.541** on **626** df, AIC = **3012.6**, BIC = **3066.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.1162** | 0.9751 | ±1.9501 | **+15.503** | **3.32e-54** | *** |
| Education: graduate level (vs college) | +0.4070 | 0.2225 | ±0.4451 | +1.829 | 0.0674 | . |
| **Education: high school or below (vs college)** | **-0.8799** | 0.4064 | ±0.8128 | **-2.165** | **0.0304** | * |
| Site: UCSD (vs UAB) | +0.2019 | 0.2803 | ±0.5607 | +0.720 | 0.4713 |  |
| Site: UW (vs UAB) | +0.1362 | 0.2521 | ±0.5041 | +0.540 | 0.5890 |  |
| **Age (years)** | **-0.0478** | 0.0112 | ±0.0225 | **-4.249** | **2.15e-05** | *** |
| BMI (kg/m2) | -0.0101 | 0.0146 | ±0.0292 | -0.694 | 0.4875 |  |
| **Hypertension** | **-0.5345** | 0.2196 | ±0.4393 | **-2.434** | **0.0149** | * |
| **High cholesterol** | **+0.5478** | 0.2267 | ±0.4533 | **+2.417** | **0.0156** | * |
| Kidney disease | -0.1756 | 0.3983 | ±0.7966 | -0.441 | 0.6593 |  |
| Circulatory disease | +0.2243 | 0.2735 | ±0.5470 | +0.820 | 0.4122 |  |
| Mean / SD ratio | +0.1275 | 0.0791 | ±0.1582 | +1.612 | 0.1069 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **638**, R² = **0.0904**, Adj R² = **0.0745**, F-statistic = **5.66** (p = **1.03e-08**), Residual SE = **2.543** on **626** df, AIC = **3013.3**, BIC = **3066.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.2512** | 0.9717 | ±1.9435 | **+15.695** | **1.64e-55** | *** |
| Education: graduate level (vs college) | +0.4054 | 0.2225 | ±0.4450 | +1.822 | 0.0685 | . |
| **Education: high school or below (vs college)** | **-0.8827** | 0.4066 | ±0.8131 | **-2.171** | **0.0299** | * |
| Site: UCSD (vs UAB) | +0.2085 | 0.2806 | ±0.5613 | +0.743 | 0.4575 |  |
| Site: UW (vs UAB) | +0.1447 | 0.2516 | ±0.5033 | +0.575 | 0.5651 |  |
| **Age (years)** | **-0.0480** | 0.0113 | ±0.0225 | **-4.267** | **1.99e-05** | *** |
| BMI (kg/m2) | -0.0100 | 0.0146 | ±0.0292 | -0.688 | 0.4916 |  |
| **Hypertension** | **-0.5467** | 0.2206 | ±0.4411 | **-2.479** | **0.0132** | * |
| **High cholesterol** | **+0.5535** | 0.2265 | ±0.4530 | **+2.444** | **0.0145** | * |
| Kidney disease | -0.1961 | 0.3934 | ±0.7868 | -0.498 | 0.6182 |  |
| Circulatory disease | +0.2190 | 0.2740 | ±0.5480 | +0.799 | 0.4241 |  |
| Avg. daily mean/SD | +0.0885 | 0.0663 | ±0.1327 | +1.333 | 0.1824 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **638**, R² = **0.0927**, Adj R² = **0.0768**, F-statistic = **5.81** (p = **5.23e-09**), Residual SE = **2.540** on **626** df, AIC = **3011.7**, BIC = **3065.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.7509** | 1.0199 | ±2.0397 | **+16.425** | **1.27e-60** | *** |
| Education: graduate level (vs college) | +0.4034 | 0.2220 | ±0.4441 | +1.817 | 0.0692 | . |
| **Education: high school or below (vs college)** | **-0.8808** | 0.4023 | ±0.8045 | **-2.190** | **0.0285** | * |
| Site: UCSD (vs UAB) | +0.2093 | 0.2817 | ±0.5633 | +0.743 | 0.4573 |  |
| Site: UW (vs UAB) | +0.1051 | 0.2506 | ±0.5012 | +0.419 | 0.6749 |  |
| **Age (years)** | **-0.0506** | 0.0113 | ±0.0226 | **-4.478** | **7.53e-06** | *** |
| BMI (kg/m2) | -0.0091 | 0.0147 | ±0.0294 | -0.619 | 0.5361 |  |
| **Hypertension** | **-0.5425** | 0.2216 | ±0.4431 | **-2.448** | **0.0143** | * |
| **High cholesterol** | **+0.5431** | 0.2277 | ±0.4554 | **+2.385** | **0.0171** | * |
| Kidney disease | -0.2477 | 0.3928 | ±0.7856 | -0.631 | 0.5283 |  |
| Circulatory disease | +0.2173 | 0.2741 | ±0.5482 | +0.793 | 0.4279 |  |
| MAG (mg/dL/h) | -0.0198 | 0.0114 | ±0.0228 | -1.735 | 0.0828 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **638**, R² = **0.0936**, Adj R² = **0.0777**, F-statistic = **5.88** (p = **3.95e-09**), Residual SE = **2.538** on **626** df, AIC = **3011.0**, BIC = **3064.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4382** | 0.9354 | ±1.8708 | **+17.573** | **3.97e-69** | *** |
| Education: graduate level (vs college) | +0.3921 | 0.2218 | ±0.4436 | +1.768 | 0.0771 | . |
| **Education: high school or below (vs college)** | **-0.8354** | 0.4065 | ±0.8130 | **-2.055** | **0.0399** | * |
| Site: UCSD (vs UAB) | +0.1969 | 0.2789 | ±0.5578 | +0.706 | 0.4802 |  |
| Site: UW (vs UAB) | +0.1264 | 0.2511 | ±0.5023 | +0.503 | 0.6148 |  |
| **Age (years)** | **-0.0483** | 0.0114 | ±0.0228 | **-4.235** | **2.29e-05** | *** |
| BMI (kg/m2) | -0.0112 | 0.0146 | ±0.0292 | -0.767 | 0.4430 |  |
| **Hypertension** | **-0.5191** | 0.2214 | ±0.4429 | **-2.344** | **0.0191** | * |
| **High cholesterol** | **+0.5600** | 0.2263 | ±0.4526 | **+2.475** | **0.0133** | * |
| Kidney disease | -0.1257 | 0.4101 | ±0.8202 | -0.306 | 0.7593 |  |
| Circulatory disease | +0.2196 | 0.2724 | ±0.5447 | +0.806 | 0.4201 |  |
| Avg. daily range (mg/dL) | -0.0054 | 0.0029 | ±0.0058 | -1.885 | 0.0594 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **638**, R² = **0.0946**, Adj R² = **0.0786**, F-statistic = **5.94** (p = **3.01e-09**), Residual SE = **2.537** on **626** df, AIC = **3010.4**, BIC = **3063.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1584** | 0.8966 | ±1.7932 | **+18.022** | **1.32e-72** | *** |
| Education: graduate level (vs college) | +0.3998 | 0.2219 | ±0.4439 | +1.801 | 0.0716 | . |
| **Education: high school or below (vs college)** | **-0.9159** | 0.4104 | ±0.8208 | **-2.232** | **0.0256** | * |
| Site: UCSD (vs UAB) | +0.1790 | 0.2795 | ±0.5589 | +0.641 | 0.5218 |  |
| Site: UW (vs UAB) | +0.1199 | 0.2518 | ±0.5036 | +0.476 | 0.6341 |  |
| **Age (years)** | **-0.0497** | 0.0114 | ±0.0228 | **-4.367** | **1.26e-05** | *** |
| BMI (kg/m2) | -0.0097 | 0.0145 | ±0.0290 | -0.669 | 0.5036 |  |
| **Hypertension** | **-0.5068** | 0.2199 | ±0.4399 | **-2.304** | **0.0212** | * |
| **High cholesterol** | **+0.5580** | 0.2265 | ±0.4530 | **+2.464** | **0.0138** | * |
| Kidney disease | -0.1739 | 0.4004 | ±0.8007 | -0.434 | 0.6640 |  |
| Circulatory disease | +0.2422 | 0.2702 | ±0.5404 | +0.896 | 0.3701 |  |
| SD of daily means (mg/dL) | -0.0320 | 0.0191 | ±0.0383 | -1.670 | 0.0950 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **638**, R² = **0.0957**, Adj R² = **0.0798**, F-statistic = **6.02** (p = **2.13e-09**), Residual SE = **2.535** on **626** df, AIC = **3009.6**, BIC = **3063.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.1511** | 1.2676 | ±2.5352 | **+11.164** | **6.13e-29** | *** |
| Education: graduate level (vs college) | +0.3865 | 0.2217 | ±0.4433 | +1.744 | 0.0812 | . |
| **Education: high school or below (vs college)** | **-0.8731** | 0.4103 | ±0.8207 | **-2.128** | **0.0334** | * |
| Site: UCSD (vs UAB) | +0.1713 | 0.2782 | ±0.5564 | +0.616 | 0.5381 |  |
| Site: UW (vs UAB) | +0.1027 | 0.2521 | ±0.5043 | +0.407 | 0.6836 |  |
| **Age (years)** | **-0.0496** | 0.0113 | ±0.0226 | **-4.385** | **1.16e-05** | *** |
| BMI (kg/m2) | -0.0098 | 0.0145 | ±0.0289 | -0.681 | 0.4959 |  |
| **Hypertension** | **-0.5134** | 0.2196 | ±0.4393 | **-2.338** | **0.0194** | * |
| **High cholesterol** | **+0.5751** | 0.2263 | ±0.4525 | **+2.542** | **0.0110** | * |
| Kidney disease | -0.1393 | 0.4038 | ±0.8075 | -0.345 | 0.7301 |  |
| Circulatory disease | +0.2307 | 0.2691 | ±0.5382 | +0.857 | 0.3913 |  |
| **Time in range 70-180, pooled (%)** | **+0.0188** | 0.0092 | ±0.0184 | **+2.043** | **0.0411** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **638**, R² = **0.0955**, Adj R² = **0.0796**, F-statistic = **6.01** (p = **2.27e-09**), Residual SE = **2.536** on **626** df, AIC = **3009.7**, BIC = **3063.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.1732** | 1.2691 | ±2.5382 | **+11.168** | **5.86e-29** | *** |
| Education: graduate level (vs college) | +0.3860 | 0.2216 | ±0.4432 | +1.742 | 0.0815 | . |
| **Education: high school or below (vs college)** | **-0.8715** | 0.4109 | ±0.8217 | **-2.121** | **0.0339** | * |
| Site: UCSD (vs UAB) | +0.1722 | 0.2783 | ±0.5565 | +0.619 | 0.5361 |  |
| Site: UW (vs UAB) | +0.1023 | 0.2521 | ±0.5043 | +0.406 | 0.6849 |  |
| **Age (years)** | **-0.0495** | 0.0113 | ±0.0226 | **-4.375** | **1.21e-05** | *** |
| BMI (kg/m2) | -0.0098 | 0.0145 | ±0.0289 | -0.681 | 0.4962 |  |
| **Hypertension** | **-0.5158** | 0.2196 | ±0.4392 | **-2.349** | **0.0188** | * |
| **High cholesterol** | **+0.5767** | 0.2263 | ±0.4527 | **+2.548** | **0.0108** | * |
| Kidney disease | -0.1386 | 0.4028 | ±0.8055 | -0.344 | 0.7307 |  |
| Circulatory disease | +0.2302 | 0.2691 | ±0.5383 | +0.855 | 0.3924 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.0184** | 0.0091 | ±0.0182 | **+2.020** | **0.0434** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **638**, R² = **0.0885**, Adj R² = **0.0725**, F-statistic = **5.52** (p = **1.83e-08**), Residual SE = **2.545** on **626** df, AIC = **3014.6**, BIC = **3068.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9126** | 0.9059 | ±1.8118 | **+17.566** | **4.51e-69** | *** |
| Education: graduate level (vs college) | +0.4129 | 0.2220 | ±0.4440 | +1.860 | 0.0629 | . |
| **Education: high school or below (vs college)** | **-0.9344** | 0.4103 | ±0.8205 | **-2.278** | **0.0228** | * |
| Site: UCSD (vs UAB) | +0.2118 | 0.2849 | ±0.5698 | +0.743 | 0.4574 |  |
| Site: UW (vs UAB) | +0.1749 | 0.2536 | ±0.5072 | +0.690 | 0.4904 |  |
| **Age (years)** | **-0.0507** | 0.0113 | ±0.0226 | **-4.478** | **7.54e-06** | *** |
| BMI (kg/m2) | -0.0102 | 0.0147 | ±0.0294 | -0.694 | 0.4878 |  |
| **Hypertension** | **-0.5566** | 0.2215 | ±0.4429 | **-2.513** | **0.0120** | * |
| **High cholesterol** | **+0.5651** | 0.2276 | ±0.4552 | **+2.483** | **0.0130** | * |
| Kidney disease | -0.2731 | 0.3858 | ±0.7715 | -0.708 | 0.4789 |  |
| Circulatory disease | +0.2201 | 0.2738 | ±0.5477 | +0.804 | 0.4215 |  |
| Time < 54 (%) | +0.0732 | 0.0956 | ±0.1912 | +0.765 | 0.4440 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **638**, R² = **0.0880**, Adj R² = **0.0720**, F-statistic = **5.49** (p = **2.09e-08**), Residual SE = **2.546** on **626** df, AIC = **3015.0**, BIC = **3068.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9792** | 0.9031 | ±1.8062 | **+17.693** | **4.72e-70** | *** |
| Education: graduate level (vs college) | +0.4075 | 0.2226 | ±0.4452 | +1.831 | 0.0671 | . |
| **Education: high school or below (vs college)** | **-0.9508** | 0.4095 | ±0.8190 | **-2.322** | **0.0203** | * |
| Site: UCSD (vs UAB) | +0.1793 | 0.2841 | ±0.5681 | +0.631 | 0.5280 |  |
| Site: UW (vs UAB) | +0.1458 | 0.2546 | ±0.5091 | +0.573 | 0.5669 |  |
| **Age (years)** | **-0.0504** | 0.0113 | ±0.0227 | **-4.452** | **8.49e-06** | *** |
| BMI (kg/m2) | -0.0104 | 0.0147 | ±0.0294 | -0.712 | 0.4768 |  |
| **Hypertension** | **-0.5653** | 0.2218 | ±0.4436 | **-2.548** | **0.0108** | * |
| **High cholesterol** | **+0.5518** | 0.2274 | ±0.4548 | **+2.427** | **0.0152** | * |
| Kidney disease | -0.2692 | 0.3864 | ±0.7729 | -0.697 | 0.4861 |  |
| Circulatory disease | +0.2233 | 0.2737 | ±0.5474 | +0.816 | 0.4146 |  |
| Avg. daily time < 54 (%) | -0.0375 | 0.1092 | ±0.2185 | -0.344 | 0.7312 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **638**, R² = **0.0885**, Adj R² = **0.0724**, F-statistic = **5.52** (p = **1.84e-08**), Residual SE = **2.546** on **626** df, AIC = **3014.7**, BIC = **3068.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0072** | 0.9058 | ±1.8116 | **+17.671** | **6.96e-70** | *** |
| Education: graduate level (vs college) | +0.4024 | 0.2228 | ±0.4455 | +1.806 | 0.0709 | . |
| **Education: high school or below (vs college)** | **-0.9471** | 0.4084 | ±0.8167 | **-2.319** | **0.0204** | * |
| Site: UCSD (vs UAB) | +0.1763 | 0.2823 | ±0.5646 | +0.625 | 0.5323 |  |
| Site: UW (vs UAB) | +0.1414 | 0.2517 | ±0.5034 | +0.562 | 0.5744 |  |
| **Age (years)** | **-0.0503** | 0.0113 | ±0.0226 | **-4.458** | **8.28e-06** | *** |
| BMI (kg/m2) | -0.0104 | 0.0147 | ±0.0293 | -0.707 | 0.4795 |  |
| **Hypertension** | **-0.5704** | 0.2220 | ±0.4440 | **-2.569** | **0.0102** | * |
| **High cholesterol** | **+0.5526** | 0.2264 | ±0.4527 | **+2.441** | **0.0146** | * |
| Kidney disease | -0.2650 | 0.3871 | ±0.7743 | -0.685 | 0.4936 |  |
| Circulatory disease | +0.2193 | 0.2737 | ±0.5474 | +0.801 | 0.4231 |  |
| Time 54-69, pooled (%) | -0.0272 | 0.0439 | ±0.0877 | -0.621 | 0.5346 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **638**, R² = **0.0897**, Adj R² = **0.0737**, F-statistic = **5.61** (p = **1.29e-08**), Residual SE = **2.544** on **626** df, AIC = **3013.8**, BIC = **3067.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0163** | 0.9028 | ±1.8055 | **+17.741** | **2.01e-70** | *** |
| Education: graduate level (vs college) | +0.3943 | 0.2230 | ±0.4460 | +1.768 | 0.0771 | . |
| **Education: high school or below (vs college)** | **-0.9476** | 0.4067 | ±0.8135 | **-2.330** | **0.0198** | * |
| Site: UCSD (vs UAB) | +0.1707 | 0.2819 | ±0.5637 | +0.605 | 0.5449 |  |
| Site: UW (vs UAB) | +0.1281 | 0.2520 | ±0.5039 | +0.508 | 0.6112 |  |
| **Age (years)** | **-0.0499** | 0.0113 | ±0.0225 | **-4.430** | **9.42e-06** | *** |
| BMI (kg/m2) | -0.0103 | 0.0146 | ±0.0293 | -0.701 | 0.4832 |  |
| **Hypertension** | **-0.5762** | 0.2216 | ±0.4432 | **-2.600** | **0.0093** | ** |
| **High cholesterol** | **+0.5506** | 0.2261 | ±0.4522 | **+2.435** | **0.0149** | * |
| Kidney disease | -0.2613 | 0.3871 | ±0.7742 | -0.675 | 0.4996 |  |
| Circulatory disease | +0.2169 | 0.2735 | ±0.5471 | +0.793 | 0.4279 |  |
| Avg. daily time 54-69 (%) | -0.0473 | 0.0440 | ±0.0880 | -1.075 | 0.2822 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **638**, R² = **0.0881**, Adj R² = **0.0720**, F-statistic = **5.50** (p = **2.07e-08**), Residual SE = **2.546** on **626** df, AIC = **3014.9**, BIC = **3068.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9906** | 0.9083 | ±1.8167 | **+17.604** | **2.28e-69** | *** |
| Education: graduate level (vs college) | +0.4067 | 0.2227 | ±0.4453 | +1.827 | 0.0678 | . |
| **Education: high school or below (vs college)** | **-0.9480** | 0.4093 | ±0.8186 | **-2.316** | **0.0206** | * |
| Site: UCSD (vs UAB) | +0.1798 | 0.2835 | ±0.5671 | +0.634 | 0.5259 |  |
| Site: UW (vs UAB) | +0.1469 | 0.2527 | ±0.5055 | +0.581 | 0.5612 |  |
| **Age (years)** | **-0.0505** | 0.0113 | ±0.0226 | **-4.465** | **8.00e-06** | *** |
| BMI (kg/m2) | -0.0104 | 0.0147 | ±0.0293 | -0.710 | 0.4777 |  |
| **Hypertension** | **-0.5665** | 0.2221 | ±0.4442 | **-2.551** | **0.0108** | * |
| **High cholesterol** | **+0.5532** | 0.2267 | ±0.4534 | **+2.440** | **0.0147** | * |
| Kidney disease | -0.2685 | 0.3868 | ±0.7735 | -0.694 | 0.4875 |  |
| Circulatory disease | +0.2212 | 0.2737 | ±0.5473 | +0.808 | 0.4190 |  |
| Time < 70 (%) | -0.0109 | 0.0327 | ±0.0654 | -0.334 | 0.7387 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **638**, R² = **0.0893**, Adj R² = **0.0733**, F-statistic = **5.58** (p = **1.43e-08**), Residual SE = **2.544** on **626** df, AIC = **3014.1**, BIC = **3067.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0152** | 0.9037 | ±1.8075 | **+17.721** | **2.87e-70** | *** |
| Education: graduate level (vs college) | +0.3960 | 0.2231 | ±0.4461 | +1.775 | 0.0759 | . |
| **Education: high school or below (vs college)** | **-0.9518** | 0.4073 | ±0.8145 | **-2.337** | **0.0194** | * |
| Site: UCSD (vs UAB) | +0.1671 | 0.2825 | ±0.5651 | +0.591 | 0.5543 |  |
| Site: UW (vs UAB) | +0.1263 | 0.2529 | ±0.5058 | +0.499 | 0.6175 |  |
| **Age (years)** | **-0.0500** | 0.0113 | ±0.0226 | **-4.429** | **9.45e-06** | *** |
| BMI (kg/m2) | -0.0103 | 0.0146 | ±0.0293 | -0.707 | 0.4797 |  |
| **Hypertension** | **-0.5752** | 0.2217 | ±0.4435 | **-2.594** | **0.0095** | ** |
| **High cholesterol** | **+0.5482** | 0.2263 | ±0.4526 | **+2.422** | **0.0154** | * |
| Kidney disease | -0.2620 | 0.3870 | ±0.7740 | -0.677 | 0.4985 |  |
| Circulatory disease | +0.2195 | 0.2734 | ±0.5469 | +0.803 | 0.4222 |  |
| Avg. daily time < 70 (%) | -0.0349 | 0.0343 | ±0.0686 | -1.017 | 0.3092 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **638**, R² = **0.0968**, Adj R² = **0.0809**, F-statistic = **6.10** (p = **1.52e-09**), Residual SE = **2.534** on **626** df, AIC = **3008.8**, BIC = **3062.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.6289** | 2.5435 | ±5.0870 | **+4.572** | **4.83e-06** | *** |
| Education: graduate level (vs college) | +0.3866 | 0.2215 | ±0.4430 | +1.746 | 0.0809 | . |
| **Education: high school or below (vs college)** | **-0.8745** | 0.4143 | ±0.8287 | **-2.111** | **0.0348** | * |
| Site: UCSD (vs UAB) | +0.1610 | 0.2788 | ±0.5576 | +0.577 | 0.5637 |  |
| Site: UW (vs UAB) | +0.0982 | 0.2524 | ±0.5048 | +0.389 | 0.6972 |  |
| **Age (years)** | **-0.0508** | 0.0113 | ±0.0226 | **-4.493** | **7.03e-06** | *** |
| BMI (kg/m2) | -0.0108 | 0.0145 | ±0.0291 | -0.740 | 0.4593 |  |
| **Hypertension** | **-0.5258** | 0.2205 | ±0.4410 | **-2.385** | **0.0171** | * |
| **High cholesterol** | **+0.5395** | 0.2271 | ±0.4543 | **+2.375** | **0.0175** | * |
| Kidney disease | -0.2028 | 0.3951 | ±0.7903 | -0.513 | 0.6079 |  |
| Circulatory disease | +0.2399 | 0.2684 | ±0.5369 | +0.894 | 0.3714 |  |
| Time 54-250, pooled (%) | +0.0444 | 0.0238 | ±0.0476 | +1.867 | 0.0619 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **638**, R² = **0.0968**, Adj R² = **0.0809**, F-statistic = **6.10** (p = **1.54e-09**), Residual SE = **2.534** on **626** df, AIC = **3008.8**, BIC = **3062.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.1551** | 2.8638 | ±5.7277 | **+3.895** | **9.81e-05** | *** |
| Education: graduate level (vs college) | +0.3838 | 0.2215 | ±0.4429 | +1.733 | 0.0831 | . |
| **Education: high school or below (vs college)** | **-0.8627** | 0.4153 | ±0.8306 | **-2.077** | **0.0378** | * |
| Site: UCSD (vs UAB) | +0.1661 | 0.2783 | ±0.5565 | +0.597 | 0.5506 |  |
| Site: UW (vs UAB) | +0.1004 | 0.2521 | ±0.5043 | +0.398 | 0.6906 |  |
| **Age (years)** | **-0.0505** | 0.0113 | ±0.0226 | **-4.464** | **8.03e-06** | *** |
| BMI (kg/m2) | -0.0109 | 0.0145 | ±0.0291 | -0.753 | 0.4517 |  |
| **Hypertension** | **-0.5254** | 0.2201 | ±0.4402 | **-2.387** | **0.0170** | * |
| **High cholesterol** | **+0.5422** | 0.2269 | ±0.4538 | **+2.389** | **0.0169** | * |
| Kidney disease | -0.1897 | 0.3969 | ±0.7938 | -0.478 | 0.6326 |  |
| Circulatory disease | +0.2445 | 0.2686 | ±0.5372 | +0.910 | 0.3626 |  |
| Avg. daily time 54-250 (%) | +0.0490 | 0.0271 | ±0.0542 | +1.807 | 0.0708 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **638**, R² = **0.0915**, Adj R² = **0.0755**, F-statistic = **5.73** (p = **7.54e-09**), Residual SE = **2.541** on **626** df, AIC = **3012.5**, BIC = **3066.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9571** | 0.8964 | ±1.7929 | **+17.801** | **6.98e-71** | *** |
| Education: graduate level (vs college) | +0.4022 | 0.2219 | ±0.4437 | +1.813 | 0.0698 | . |
| **Education: high school or below (vs college)** | **-0.9035** | 0.4097 | ±0.8194 | **-2.205** | **0.0274** | * |
| Site: UCSD (vs UAB) | +0.1907 | 0.2791 | ±0.5582 | +0.683 | 0.4943 |  |
| Site: UW (vs UAB) | +0.1371 | 0.2509 | ±0.5018 | +0.547 | 0.5846 |  |
| **Age (years)** | **-0.0497** | 0.0113 | ±0.0227 | **-4.386** | **1.16e-05** | *** |
| BMI (kg/m2) | -0.0097 | 0.0145 | ±0.0290 | -0.671 | 0.5023 |  |
| **Hypertension** | **-0.5246** | 0.2213 | ±0.4427 | **-2.370** | **0.0178** | * |
| **High cholesterol** | **+0.5835** | 0.2268 | ±0.4537 | **+2.572** | **0.0101** | * |
| Kidney disease | -0.1754 | 0.4012 | ±0.8024 | -0.437 | 0.6621 |  |
| Circulatory disease | +0.2249 | 0.2719 | ±0.5438 | +0.827 | 0.4082 |  |
| Time 181-250, pooled (%) | -0.0183 | 0.0120 | ±0.0241 | -1.517 | 0.1293 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **638**, R² = **0.0912**, Adj R² = **0.0752**, F-statistic = **5.71** (p = **8.14e-09**), Residual SE = **2.542** on **626** df, AIC = **3012.7**, BIC = **3066.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9646** | 0.8969 | ±1.7937 | **+17.800** | **7.02e-71** | *** |
| Education: graduate level (vs college) | +0.4028 | 0.2218 | ±0.4437 | +1.816 | 0.0694 | . |
| **Education: high school or below (vs college)** | **-0.9052** | 0.4105 | ±0.8210 | **-2.205** | **0.0274** | * |
| Site: UCSD (vs UAB) | +0.1873 | 0.2794 | ±0.5589 | +0.670 | 0.5027 |  |
| Site: UW (vs UAB) | +0.1352 | 0.2511 | ±0.5021 | +0.539 | 0.5901 |  |
| **Age (years)** | **-0.0499** | 0.0113 | ±0.0227 | **-4.399** | **1.09e-05** | *** |
| BMI (kg/m2) | -0.0097 | 0.0145 | ±0.0290 | -0.671 | 0.5022 |  |
| **Hypertension** | **-0.5272** | 0.2213 | ±0.4426 | **-2.382** | **0.0172** | * |
| **High cholesterol** | **+0.5819** | 0.2268 | ±0.4536 | **+2.565** | **0.0103** | * |
| Kidney disease | -0.1803 | 0.3999 | ±0.7998 | -0.451 | 0.6521 |  |
| Circulatory disease | +0.2236 | 0.2719 | ±0.5438 | +0.822 | 0.4109 |  |
| Avg. daily time 181-250 (%) | -0.0171 | 0.0117 | ±0.0235 | -1.457 | 0.1451 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **638**, R² = **0.0953**, Adj R² = **0.0794**, F-statistic = **5.99** (p = **2.43e-09**), Residual SE = **2.536** on **626** df, AIC = **3009.9**, BIC = **3063.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9871** | 0.8957 | ±1.7914 | **+17.849** | **2.93e-71** | *** |
| Education: graduate level (vs college) | +0.3932 | 0.2214 | ±0.4428 | +1.776 | 0.0758 | . |
| **Education: high school or below (vs college)** | **-0.8715** | 0.4122 | ±0.8244 | **-2.114** | **0.0345** | * |
| Site: UCSD (vs UAB) | +0.1855 | 0.2775 | ±0.5550 | +0.669 | 0.5038 |  |
| Site: UW (vs UAB) | +0.1185 | 0.2513 | ±0.5026 | +0.472 | 0.6371 |  |
| **Age (years)** | **-0.0498** | 0.0113 | ±0.0226 | **-4.403** | **1.07e-05** | *** |
| BMI (kg/m2) | -0.0098 | 0.0145 | ±0.0289 | -0.679 | 0.4969 |  |
| **Hypertension** | **-0.5081** | 0.2204 | ±0.4408 | **-2.305** | **0.0211** | * |
| **High cholesterol** | **+0.5790** | 0.2265 | ±0.4530 | **+2.556** | **0.0106** | * |
| Kidney disease | -0.1478 | 0.4024 | ±0.8049 | -0.367 | 0.7135 |  |
| Circulatory disease | +0.2318 | 0.2695 | ±0.5389 | +0.860 | 0.3896 |  |
| **Time > 180 (%)** | **-0.0182** | 0.0093 | ±0.0186 | **-1.962** | **0.0498** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **638**, R² = **0.0942**, Adj R² = **0.0783**, F-statistic = **5.92** (p = **3.37e-09**), Residual SE = **2.538** on **626** df, AIC = **3010.6**, BIC = **3064.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9879** | 0.8961 | ±1.7923 | **+17.841** | **3.40e-71** | *** |
| Education: graduate level (vs college) | +0.3950 | 0.2214 | ±0.4429 | +1.784 | 0.0744 | . |
| **Education: high school or below (vs college)** | **-0.8749** | 0.4129 | ±0.8258 | **-2.119** | **0.0341** | * |
| Site: UCSD (vs UAB) | +0.1837 | 0.2780 | ±0.5560 | +0.661 | 0.5088 |  |
| Site: UW (vs UAB) | +0.1209 | 0.2514 | ±0.5028 | +0.481 | 0.6306 |  |
| **Age (years)** | **-0.0499** | 0.0113 | ±0.0227 | **-4.408** | **1.04e-05** | *** |
| BMI (kg/m2) | -0.0099 | 0.0145 | ±0.0290 | -0.684 | 0.4941 |  |
| **Hypertension** | **-0.5136** | 0.2204 | ±0.4408 | **-2.330** | **0.0198** | * |
| **High cholesterol** | **+0.5786** | 0.2267 | ±0.4533 | **+2.553** | **0.0107** | * |
| Kidney disease | -0.1544 | 0.4018 | ±0.8036 | -0.384 | 0.7008 |  |
| Circulatory disease | +0.2307 | 0.2698 | ±0.5395 | +0.855 | 0.3925 |  |
| Avg. daily time > 180 (%) | -0.0169 | 0.0093 | ±0.0187 | -1.806 | 0.0709 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **638**, R² = **0.0958**, Adj R² = **0.0799**, F-statistic = **6.03** (p = **2.08e-09**), Residual SE = **2.535** on **626** df, AIC = **3009.5**, BIC = **3063.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9849** | 0.8956 | ±1.7912 | **+17.848** | **3.00e-71** | *** |
| Education: graduate level (vs college) | +0.3889 | 0.2210 | ±0.4420 | +1.760 | 0.0784 | . |
| **Education: high school or below (vs college)** | **-0.8920** | 0.4111 | ±0.8221 | **-2.170** | **0.0300** | * |
| Site: UCSD (vs UAB) | +0.1740 | 0.2785 | ±0.5570 | +0.625 | 0.5321 |  |
| Site: UW (vs UAB) | +0.1214 | 0.2516 | ±0.5032 | +0.482 | 0.6295 |  |
| **Age (years)** | **-0.0506** | 0.0113 | ±0.0226 | **-4.471** | **7.78e-06** | *** |
| BMI (kg/m2) | -0.0091 | 0.0145 | ±0.0289 | -0.630 | 0.5286 |  |
| **Hypertension** | **-0.5078** | 0.2195 | ±0.4389 | **-2.314** | **0.0207** | * |
| **High cholesterol** | **+0.5796** | 0.2270 | ±0.4540 | **+2.554** | **0.0107** | * |
| Kidney disease | -0.2213 | 0.3924 | ±0.7848 | -0.564 | 0.5728 |  |
| Circulatory disease | +0.2367 | 0.2685 | ±0.5369 | +0.882 | 0.3780 |  |
| Nocturnal time > 180 (%) | -0.0197 | 0.0103 | ±0.0206 | -1.913 | 0.0558 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **638**, R² = **0.0913**, Adj R² = **0.0754**, F-statistic = **5.72** (p = **7.90e-09**), Residual SE = **2.542** on **626** df, AIC = **3012.6**, BIC = **3066.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9894** | 0.8980 | ±1.7961 | **+17.805** | **6.48e-71** | *** |
| Education: graduate level (vs college) | +0.3906 | 0.2231 | ±0.4461 | +1.751 | 0.0800 | . |
| **Education: high school or below (vs college)** | **-0.9104** | 0.4077 | ±0.8154 | **-2.233** | **0.0256** | * |
| Site: UCSD (vs UAB) | +0.2016 | 0.2808 | ±0.5615 | +0.718 | 0.4727 |  |
| Site: UW (vs UAB) | +0.1448 | 0.2500 | ±0.5001 | +0.579 | 0.5624 |  |
| **Age (years)** | **-0.0492** | 0.0115 | ±0.0229 | **-4.289** | **1.80e-05** | *** |
| BMI (kg/m2) | -0.0114 | 0.0146 | ±0.0293 | -0.779 | 0.4357 |  |
| **Hypertension** | **-0.5208** | 0.2223 | ±0.4446 | **-2.343** | **0.0191** | * |
| **High cholesterol** | **+0.5635** | 0.2263 | ±0.4526 | **+2.490** | **0.0128** | * |
| Kidney disease | -0.1873 | 0.4082 | ±0.8164 | -0.459 | 0.6463 |  |
| Circulatory disease | +0.2184 | 0.2743 | ±0.5486 | +0.796 | 0.4260 |  |
| Any reading > 250 during wear (0/1) | -0.3536 | 0.2545 | ±0.5089 | -1.389 | 0.1647 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **638**, R² = **0.0978**, Adj R² = **0.0819**, F-statistic = **6.17** (p = **1.13e-09**), Residual SE = **2.532** on **626** df, AIC = **3008.1**, BIC = **3061.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0442** | 0.8957 | ±1.7915 | **+17.911** | **9.60e-72** | *** |
| Education: graduate level (vs college) | +0.3867 | 0.2212 | ±0.4424 | +1.748 | 0.0804 | . |
| **Education: high school or below (vs college)** | **-0.8622** | 0.4152 | ±0.8304 | **-2.076** | **0.0378** | * |
| Site: UCSD (vs UAB) | +0.1745 | 0.2773 | ±0.5547 | +0.629 | 0.5293 |  |
| Site: UW (vs UAB) | +0.1069 | 0.2514 | ±0.5028 | +0.425 | 0.6706 |  |
| **Age (years)** | **-0.0508** | 0.0113 | ±0.0226 | **-4.500** | **6.79e-06** | *** |
| BMI (kg/m2) | -0.0107 | 0.0145 | ±0.0291 | -0.734 | 0.4632 |  |
| **Hypertension** | **-0.5195** | 0.2209 | ±0.4418 | **-2.352** | **0.0187** | * |
| **High cholesterol** | **+0.5444** | 0.2270 | ±0.4540 | **+2.398** | **0.0165** | * |
| Kidney disease | -0.1992 | 0.3952 | ±0.7904 | -0.504 | 0.6142 |  |
| Circulatory disease | +0.2400 | 0.2684 | ±0.5368 | +0.894 | 0.3713 |  |
| Time > 250 (%) | -0.0475 | 0.0248 | ±0.0495 | -1.919 | 0.0550 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 638)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **638**, R² = **0.0968**, Adj R² = **0.0810**, F-statistic = **6.10** (p = **1.52e-09**), Residual SE = **2.534** on **626** df, AIC = **3008.8**, BIC = **3062.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0352** | 0.8959 | ±1.7918 | **+17.899** | **1.21e-71** | *** |
| Education: graduate level (vs college) | +0.3868 | 0.2212 | ±0.4424 | +1.749 | 0.0803 | . |
| **Education: high school or below (vs college)** | **-0.8542** | 0.4165 | ±0.8331 | **-2.051** | **0.0403** | * |
| Site: UCSD (vs UAB) | +0.1773 | 0.2774 | ±0.5548 | +0.639 | 0.5227 |  |
| Site: UW (vs UAB) | +0.1120 | 0.2513 | ±0.5027 | +0.446 | 0.6558 |  |
| **Age (years)** | **-0.0507** | 0.0113 | ±0.0226 | **-4.484** | **7.32e-06** | *** |
| BMI (kg/m2) | -0.0109 | 0.0146 | ±0.0291 | -0.748 | 0.4543 |  |
| **Hypertension** | **-0.5209** | 0.2205 | ±0.4410 | **-2.363** | **0.0181** | * |
| **High cholesterol** | **+0.5472** | 0.2268 | ±0.4537 | **+2.412** | **0.0158** | * |
| Kidney disease | -0.1908 | 0.3968 | ±0.7937 | -0.481 | 0.6306 |  |
| Circulatory disease | +0.2432 | 0.2688 | ±0.5376 | +0.905 | 0.3657 |  |
| Avg. daily time > 250 (%) | -0.0500 | 0.0284 | ±0.0567 | -1.764 | 0.0778 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Total analysis base - Cognition

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 90 single-predictor tests; 53 with raw p < 0.05 (about 4 expected by chance); FDR rule applied to 90 tests (samples with n >= 500), of which **24** are significant at BH q < 0.05 in the all-tests family and 46 in the within-outcome family.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 638): best single predictor out of sample is **HbA1c** (CV R² 0.091 vs 0.067 for covariates alone, gain +0.024; -0.523 per SD, p = 1.7e-05, q = 0.002). FDR-robust associations (19): HbA1c (lower outcome, -0.523 per SD, q = 0.002); TIR 70-180 (pooled) (higher outcome, +0.475 per SD, q = 0.010); TIR 70-180 (daily avg) (higher outcome, +0.466 per SD, q = 0.013); Mean glucose (lower outcome, -0.435 per SD, q = 0.017); GMI (lower outcome, -0.435 per SD, q = 0.017); SD (pooled) (lower outcome, -0.442 per SD, q = 0.017); ....
- **Cognitive impairment (MoCA < 26)** (n = 638): best single predictor out of sample is **HbA1c** (CV AUC 0.663 vs 0.641 for covariates alone, gain +0.021; OR 1.43 per SD, p = 2.7e-04, q = 0.008). FDR-robust associations (4): HbA1c (higher outcome, OR 1.43 per SD, q = 0.008); TIR 70-180 (pooled) (lower outcome, OR 0.75 per SD, q = 0.026); TIR 70-180 (daily avg) (lower outcome, OR 0.76 per SD, q = 0.028); SD (pooled) (higher outcome, OR 1.30 per SD, q = 0.037).
- **MoCA memory index score (0-15)** (n = 638): best single predictor out of sample is **HbA1c** (CV R² 0.053 vs 0.043 for covariates alone, gain +0.010; -0.288 per SD, p = 0.005, q = 0.038). FDR-robust associations (1): HbA1c (lower outcome, -0.288 per SD, q = 0.038).

**Most predictable outcomes (largest out-of-sample gain over covariates):** MoCA total score (0-30) (+0.024, via HbA1c); Cognitive impairment (MoCA < 26) (+0.021, via HbA1c); MoCA memory index score (0-15) (+0.010, via HbA1c). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (5 FDR-significant / 15 raw-significant of 24); Range 70-180 (4 FDR-significant / 6 raw-significant of 6); Band > 180 (3 FDR-significant / 7 raw-significant of 9).
Level metrics: 3 FDR-significant (5 raw); variability metrics: 5 FDR-significant (15 raw); HbA1c alone: 3 FDR-significant (3 raw) across the outcomes in this file.

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
