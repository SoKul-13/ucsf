# Phase 6b model output tables - Hypoglycaemia exposure: at least one reading < 54 - Total analysis base

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models.


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


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 637; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **637**, R² = **0.1291**, Adj R² = **0.1152**, F-statistic = **9.28** (p = **2.00e-14**), Residual SE = **4.764** on **626** df, AIC = **3807.6**, BIC = **3856.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.9321** | 1.5439 | ±3.0878 | **+4.490** | **7.12e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0471** | 0.4155 | ±0.8310 | **-2.520** | **0.0117** | * |
| **Education: high school or below (vs college)** | **+1.9717** | 0.7852 | ±1.5704 | **+2.511** | **0.0120** | * |
| Site: UCSD (vs UAB) | +0.8842 | 0.5240 | ±1.0481 | +1.687 | 0.0915 | . |
| Site: UW (vs UAB) | +0.2743 | 0.4492 | ±0.8983 | +0.611 | 0.5414 |  |
| **Age (years)** | **-0.0833** | 0.0174 | ±0.0349 | **-4.776** | **1.78e-06** | *** |
| **BMI (kg/m2)** | **+0.1139** | 0.0307 | ±0.0614 | **+3.710** | **2.08e-04** | *** |
| Hypertension | -0.1794 | 0.4472 | ±0.8943 | -0.401 | 0.6883 |  |
| High cholesterol | +0.6767 | 0.4052 | ±0.8103 | +1.670 | 0.0949 | . |
| Kidney disease | +1.0988 | 0.7130 | ±1.4261 | +1.541 | 0.1233 |  |
| Circulatory disease | +0.5826 | 0.5308 | ±1.0616 | +1.098 | 0.2723 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **637**, R² = **0.1335**, Adj R² = **0.1183**, F-statistic = **8.76** (p = **1.51e-14**), Residual SE = **4.756** on **625** df, AIC = **3806.3**, BIC = **3859.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+4.8402** | 1.9808 | ±3.9616 | **+2.444** | **0.0145** | * |
| **Education: graduate level (vs college)** | **-0.9937** | 0.4145 | ±0.8290 | **-2.397** | **0.0165** | * |
| **Education: high school or below (vs college)** | **+1.8454** | 0.7823 | ±1.5647 | **+2.359** | **0.0183** | * |
| Site: UCSD (vs UAB) | +0.8563 | 0.5198 | ±1.0396 | +1.647 | 0.0995 | . |
| Site: UW (vs UAB) | +0.3296 | 0.4507 | ±0.9015 | +0.731 | 0.4646 |  |
| **Age (years)** | **-0.0871** | 0.0178 | ±0.0356 | **-4.891** | **1.00e-06** | *** |
| **BMI (kg/m2)** | **+0.1098** | 0.0308 | ±0.0617 | **+3.561** | **3.70e-04** | *** |
| Hypertension | -0.2649 | 0.4498 | ±0.8996 | -0.589 | 0.5559 |  |
| High cholesterol | +0.6312 | 0.4038 | ±0.8075 | +1.563 | 0.1180 |  |
| Kidney disease | +1.0387 | 0.7158 | ±1.4316 | +1.451 | 0.1468 |  |
| Circulatory disease | +0.5925 | 0.5281 | ±1.0561 | +1.122 | 0.2619 |  |
| HbA1c (%) | +0.4211 | 0.2584 | ±0.5167 | +1.630 | 0.1031 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **637**, R² = **0.1342**, Adj R² = **0.1189**, F-statistic = **8.81** (p = **1.22e-14**), Residual SE = **4.754** on **625** df, AIC = **3805.9**, BIC = **3859.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.2726** | 1.7575 | ±3.5150 | **+3.000** | **0.0027** | ** |
| **Education: graduate level (vs college)** | **-1.0481** | 0.4150 | ±0.8301 | **-2.525** | **0.0116** | * |
| **Education: high school or below (vs college)** | **+1.8439** | 0.7856 | ±1.5711 | **+2.347** | **0.0189** | * |
| Site: UCSD (vs UAB) | +0.8758 | 0.5214 | ±1.0429 | +1.680 | 0.0930 | . |
| Site: UW (vs UAB) | +0.2947 | 0.4497 | ±0.8994 | +0.655 | 0.5123 |  |
| **Age (years)** | **-0.0841** | 0.0175 | ±0.0351 | **-4.795** | **1.63e-06** | *** |
| **BMI (kg/m2)** | **+0.1113** | 0.0308 | ±0.0616 | **+3.614** | **3.02e-04** | *** |
| Hypertension | -0.2894 | 0.4525 | ±0.9051 | -0.640 | 0.5225 |  |
| High cholesterol | +0.6280 | 0.4021 | ±0.8042 | +1.562 | 0.1183 |  |
| Kidney disease | +0.9594 | 0.7236 | ±1.4471 | +1.326 | 0.1849 |  |
| Circulatory disease | +0.5671 | 0.5297 | ±1.0595 | +1.071 | 0.2844 |  |
| Mean glucose (mg/dL) | +0.0154 | 0.0085 | ±0.0170 | +1.820 | 0.0687 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **637**, R² = **0.1342**, Adj R² = **0.1189**, F-statistic = **8.81** (p = **1.22e-14**), Residual SE = **4.754** on **625** df, AIC = **3805.9**, BIC = **3859.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.1359 | 2.5381 | ±5.0761 | +1.236 | 0.2166 |  |
| **Education: graduate level (vs college)** | **-1.0481** | 0.4150 | ±0.8301 | **-2.525** | **0.0116** | * |
| **Education: high school or below (vs college)** | **+1.8439** | 0.7856 | ±1.5711 | **+2.347** | **0.0189** | * |
| Site: UCSD (vs UAB) | +0.8758 | 0.5214 | ±1.0429 | +1.680 | 0.0930 | . |
| Site: UW (vs UAB) | +0.2947 | 0.4497 | ±0.8994 | +0.655 | 0.5123 |  |
| **Age (years)** | **-0.0841** | 0.0175 | ±0.0351 | **-4.795** | **1.63e-06** | *** |
| **BMI (kg/m2)** | **+0.1113** | 0.0308 | ±0.0616 | **+3.614** | **3.02e-04** | *** |
| Hypertension | -0.2894 | 0.4525 | ±0.9051 | -0.640 | 0.5225 |  |
| High cholesterol | +0.6280 | 0.4021 | ±0.8042 | +1.562 | 0.1183 |  |
| Kidney disease | +0.9594 | 0.7236 | ±1.4471 | +1.326 | 0.1849 |  |
| Circulatory disease | +0.5671 | 0.5297 | ±1.0595 | +1.071 | 0.2844 |  |
| GMI (%) | +0.6455 | 0.3547 | ±0.7093 | +1.820 | 0.0687 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **637**, R² = **0.1383**, Adj R² = **0.1231**, F-statistic = **9.12** (p = **3.15e-15**), Residual SE = **4.743** on **625** df, AIC = **3802.8**, BIC = **3856.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+4.6962** | 1.7548 | ±3.5096 | **+2.676** | **0.0074** | ** |
| **Education: graduate level (vs college)** | **-1.0610** | 0.4141 | ±0.8282 | **-2.562** | **0.0104** | * |
| **Education: high school or below (vs college)** | **+1.8088** | 0.7805 | ±1.5610 | **+2.318** | **0.0205** | * |
| Site: UCSD (vs UAB) | +0.8648 | 0.5185 | ±1.0369 | +1.668 | 0.0953 | . |
| Site: UW (vs UAB) | +0.2913 | 0.4493 | ±0.8985 | +0.648 | 0.5167 |  |
| **Age (years)** | **-0.0818** | 0.0175 | ±0.0350 | **-4.672** | **2.98e-06** | *** |
| **BMI (kg/m2)** | **+0.1074** | 0.0309 | ±0.0617 | **+3.483** | **4.97e-04** | *** |
| Hypertension | -0.3168 | 0.4499 | ±0.8997 | -0.704 | 0.4814 |  |
| High cholesterol | +0.5869 | 0.3997 | ±0.7995 | +1.468 | 0.1421 |  |
| Kidney disease | +1.0420 | 0.7221 | ±1.4443 | +1.443 | 0.1490 |  |
| Circulatory disease | +0.5773 | 0.5280 | ±1.0560 | +1.093 | 0.2742 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0208** | 0.0082 | ±0.0164 | **+2.530** | **0.0114** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **637**, R² = **0.1393**, Adj R² = **0.1242**, F-statistic = **9.20** (p = **2.25e-15**), Residual SE = **4.740** on **625** df, AIC = **3802.1**, BIC = **3855.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.1946** | 1.5640 | ±3.1281 | **+3.961** | **7.48e-05** | *** |
| **Education: graduate level (vs college)** | **-1.0126** | 0.4130 | ±0.8260 | **-2.452** | **0.0142** | * |
| **Education: high school or below (vs college)** | **+1.7273** | 0.7817 | ±1.5635 | **+2.210** | **0.0271** | * |
| Site: UCSD (vs UAB) | +0.8773 | 0.5197 | ±1.0394 | +1.688 | 0.0914 | . |
| Site: UW (vs UAB) | +0.3687 | 0.4473 | ±0.8947 | +0.824 | 0.4099 |  |
| **Age (years)** | **-0.0890** | 0.0176 | ±0.0352 | **-5.053** | **4.36e-07** | *** |
| **BMI (kg/m2)** | **+0.1132** | 0.0308 | ±0.0616 | **+3.675** | **2.38e-04** | *** |
| Hypertension | -0.3267 | 0.4496 | ±0.8992 | -0.727 | 0.4675 |  |
| High cholesterol | +0.6684 | 0.4010 | ±0.8020 | +1.667 | 0.0956 | . |
| Kidney disease | +0.7122 | 0.7329 | ±1.4658 | +0.972 | 0.3312 |  |
| Circulatory disease | +0.6036 | 0.5286 | ±1.0572 | +1.142 | 0.2535 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0453** | 0.0165 | ±0.0330 | **+2.746** | **0.0060** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **637**, R² = **0.1374**, Adj R² = **0.1222**, F-statistic = **9.05** (p = **4.29e-15**), Residual SE = **4.746** on **625** df, AIC = **3803.5**, BIC = **3857.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.2627** | 1.5636 | ±3.1272 | **+4.005** | **6.19e-05** | *** |
| **Education: graduate level (vs college)** | **-1.0093** | 0.4136 | ±0.8272 | **-2.440** | **0.0147** | * |
| **Education: high school or below (vs college)** | **+1.7218** | 0.7855 | ±1.5709 | **+2.192** | **0.0284** | * |
| Site: UCSD (vs UAB) | +0.8685 | 0.5214 | ±1.0428 | +1.666 | 0.0958 | . |
| Site: UW (vs UAB) | +0.3469 | 0.4476 | ±0.8951 | +0.775 | 0.4383 |  |
| **Age (years)** | **-0.0890** | 0.0176 | ±0.0352 | **-5.054** | **4.32e-07** | *** |
| **BMI (kg/m2)** | **+0.1135** | 0.0307 | ±0.0615 | **+3.693** | **2.22e-04** | *** |
| Hypertension | -0.3010 | 0.4503 | ±0.9006 | -0.668 | 0.5038 |  |
| High cholesterol | +0.6607 | 0.4016 | ±0.8032 | +1.645 | 0.0999 | . |
| Kidney disease | +0.7365 | 0.7388 | ±1.4777 | +0.997 | 0.3188 |  |
| Circulatory disease | +0.6148 | 0.5294 | ±1.0588 | +1.161 | 0.2455 |  |
| **Avg. daily SD (mg/dL)** | **+0.0473** | 0.0189 | ±0.0378 | **+2.507** | **0.0122** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **637**, R² = **0.1355**, Adj R² = **0.1202**, F-statistic = **8.90** (p = **8.04e-15**), Residual SE = **4.751** on **625** df, AIC = **3804.9**, BIC = **3858.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.8575** | 1.6236 | ±3.2473 | **+3.608** | **3.09e-04** | *** |
| **Education: graduate level (vs college)** | **-1.0153** | 0.4135 | ±0.8270 | **-2.455** | **0.0141** | * |
| **Education: high school or below (vs college)** | **+1.8049** | 0.7824 | ±1.5648 | **+2.307** | **0.0211** | * |
| Site: UCSD (vs UAB) | +0.8741 | 0.5222 | ±1.0444 | +1.674 | 0.0941 | . |
| Site: UW (vs UAB) | +0.3623 | 0.4455 | ±0.8911 | +0.813 | 0.4161 |  |
| **Age (years)** | **-0.0900** | 0.0177 | ±0.0353 | **-5.093** | **3.53e-07** | *** |
| **BMI (kg/m2)** | **+0.1146** | 0.0308 | ±0.0617 | **+3.715** | **2.03e-04** | *** |
| Hypertension | -0.2636 | 0.4483 | ±0.8965 | -0.588 | 0.5565 |  |
| High cholesterol | +0.7019 | 0.4036 | ±0.8072 | +1.739 | 0.0820 | . |
| Kidney disease | +0.7710 | 0.7333 | ±1.4667 | +1.051 | 0.2931 |  |
| Circulatory disease | +0.6087 | 0.5314 | ±1.0628 | +1.146 | 0.2520 |  |
| **CV (%)** | **+0.0708** | 0.0321 | ±0.0643 | **+2.201** | **0.0277** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **637**, R² = **0.1363**, Adj R² = **0.1211**, F-statistic = **8.97** (p = **6.11e-15**), Residual SE = **4.749** on **625** df, AIC = **3804.3**, BIC = **3857.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.2467** | 1.7980 | ±3.5959 | **+5.143** | **2.71e-07** | *** |
| **Education: graduate level (vs college)** | **-1.0383** | 0.4130 | ±0.8260 | **-2.514** | **0.0119** | * |
| **Education: high school or below (vs college)** | **+1.7967** | 0.7801 | ±1.5602 | **+2.303** | **0.0213** | * |
| Site: UCSD (vs UAB) | +0.8464 | 0.5231 | ±1.0463 | +1.618 | 0.1057 |  |
| Site: UW (vs UAB) | +0.3290 | 0.4465 | ±0.8929 | +0.737 | 0.4612 |  |
| **Age (years)** | **-0.0908** | 0.0176 | ±0.0352 | **-5.167** | **2.38e-07** | *** |
| **BMI (kg/m2)** | **+0.1131** | 0.0306 | ±0.0613 | **+3.692** | **2.22e-04** | *** |
| Hypertension | -0.2555 | 0.4488 | ±0.8975 | -0.569 | 0.5691 |  |
| High cholesterol | +0.6994 | 0.4031 | ±0.8061 | +1.735 | 0.0827 | . |
| Kidney disease | +0.8362 | 0.7319 | ±1.4637 | +1.143 | 0.2532 |  |
| Circulatory disease | +0.5782 | 0.5314 | ±1.0629 | +1.088 | 0.2766 |  |
| **Mean / SD ratio** | **-0.3484** | 0.1484 | ±0.2967 | **-2.349** | **0.0188** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **637**, R² = **0.1325**, Adj R² = **0.1172**, F-statistic = **8.68** (p = **2.11e-14**), Residual SE = **4.759** on **625** df, AIC = **3807.1**, BIC = **3860.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5106** | 1.7960 | ±3.5921 | **+4.739** | **2.15e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0364** | 0.4146 | ±0.8292 | **-2.500** | **0.0124** | * |
| **Education: high school or below (vs college)** | **+1.8354** | 0.7838 | ±1.5677 | **+2.342** | **0.0192** | * |
| Site: UCSD (vs UAB) | +0.8390 | 0.5273 | ±1.0547 | +1.591 | 0.1116 |  |
| Site: UW (vs UAB) | +0.2995 | 0.4475 | ±0.8950 | +0.669 | 0.5034 |  |
| **Age (years)** | **-0.0889** | 0.0176 | ±0.0351 | **-5.059** | **4.21e-07** | *** |
| **BMI (kg/m2)** | **+0.1131** | 0.0306 | ±0.0612 | **+3.696** | **2.19e-04** | *** |
| Hypertension | -0.2142 | 0.4497 | ±0.8994 | -0.476 | 0.6339 |  |
| High cholesterol | +0.6825 | 0.4042 | ±0.8084 | +1.689 | 0.0913 | . |
| Kidney disease | +0.9313 | 0.7314 | ±1.4628 | +1.273 | 0.2029 |  |
| Circulatory disease | +0.5906 | 0.5311 | ±1.0622 | +1.112 | 0.2661 |  |
| Avg. daily mean/SD | -0.1960 | 0.1226 | ±0.2452 | -1.599 | 0.1098 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **637**, R² = **0.1310**, Adj R² = **0.1157**, F-statistic = **8.56** (p = **3.49e-14**), Residual SE = **4.763** on **625** df, AIC = **3808.2**, BIC = **3861.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.0075** | 1.6905 | ±3.3810 | **+3.554** | **3.80e-04** | *** |
| **Education: graduate level (vs college)** | **-1.0389** | 0.4149 | ±0.8299 | **-2.504** | **0.0123** | * |
| **Education: high school or below (vs college)** | **+1.8913** | 0.7873 | ±1.5746 | **+2.402** | **0.0163** | * |
| Site: UCSD (vs UAB) | +0.8589 | 0.5258 | ±1.0516 | +1.634 | 0.1023 |  |
| Site: UW (vs UAB) | +0.3324 | 0.4524 | ±0.9048 | +0.735 | 0.4625 |  |
| **Age (years)** | **-0.0834** | 0.0174 | ±0.0349 | **-4.780** | **1.75e-06** | *** |
| **BMI (kg/m2)** | **+0.1123** | 0.0311 | ±0.0622 | **+3.610** | **3.06e-04** | *** |
| Hypertension | -0.2032 | 0.4481 | ±0.8963 | -0.453 | 0.6503 |  |
| High cholesterol | +0.6914 | 0.4064 | ±0.8128 | +1.701 | 0.0889 | . |
| Kidney disease | +1.0716 | 0.7163 | ±1.4326 | +1.496 | 0.1347 |  |
| Circulatory disease | +0.5869 | 0.5310 | ±1.0620 | +1.105 | 0.2691 |  |
| MAG (mg/dL/h) | +0.0234 | 0.0217 | ±0.0434 | +1.080 | 0.2802 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **637**, R² = **0.1356**, Adj R² = **0.1204**, F-statistic = **8.91** (p = **7.71e-15**), Residual SE = **4.751** on **625** df, AIC = **3804.8**, BIC = **3858.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.9710** | 1.5985 | ±3.1971 | **+3.735** | **1.88e-04** | *** |
| **Education: graduate level (vs college)** | **-1.0103** | 0.4142 | ±0.8284 | **-2.439** | **0.0147** | * |
| **Education: high school or below (vs college)** | **+1.7492** | 0.7859 | ±1.5719 | **+2.226** | **0.0260** | * |
| Site: UCSD (vs UAB) | +0.8663 | 0.5224 | ±1.0448 | +1.658 | 0.0973 | . |
| Site: UW (vs UAB) | +0.3339 | 0.4476 | ±0.8952 | +0.746 | 0.4556 |  |
| **Age (years)** | **-0.0879** | 0.0175 | ±0.0351 | **-5.010** | **5.45e-07** | *** |
| **BMI (kg/m2)** | **+0.1155** | 0.0307 | ±0.0615 | **+3.759** | **1.70e-04** | *** |
| Hypertension | -0.2675 | 0.4500 | ±0.8999 | -0.594 | 0.5522 |  |
| High cholesterol | +0.6685 | 0.4026 | ±0.8053 | +1.660 | 0.0969 | . |
| Kidney disease | +0.8026 | 0.7373 | ±1.4747 | +1.089 | 0.2763 |  |
| Circulatory disease | +0.5881 | 0.5307 | ±1.0614 | +1.108 | 0.2678 |  |
| **Avg. daily range (mg/dL)** | **+0.0111** | 0.0051 | ±0.0103 | **+2.147** | **0.0318** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **637**, R² = **0.1421**, Adj R² = **0.1270**, F-statistic = **9.41** (p = **8.93e-16**), Residual SE = **4.733** on **625** df, AIC = **3800.0**, BIC = **3853.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.4232** | 1.5516 | ±3.1033 | **+4.140** | **3.48e-05** | *** |
| **Education: graduate level (vs college)** | **-1.0190** | 0.4128 | ±0.8256 | **-2.468** | **0.0136** | * |
| **Education: high school or below (vs college)** | **+1.8885** | 0.7702 | ±1.5403 | **+2.452** | **0.0142** | * |
| Site: UCSD (vs UAB) | +0.9083 | 0.5154 | ±1.0307 | +1.763 | 0.0780 | . |
| Site: UW (vs UAB) | +0.3680 | 0.4461 | ±0.8922 | +0.825 | 0.4095 |  |
| **Age (years)** | **-0.0857** | 0.0177 | ±0.0354 | **-4.851** | **1.23e-06** | *** |
| **BMI (kg/m2)** | **+0.1120** | 0.0308 | ±0.0617 | **+3.631** | **2.82e-04** | *** |
| Hypertension | -0.3284 | 0.4462 | ±0.8925 | -0.736 | 0.4618 |  |
| High cholesterol | +0.6704 | 0.4009 | ±0.8017 | +1.672 | 0.0944 | . |
| Kidney disease | +0.8390 | 0.7153 | ±1.4306 | +1.173 | 0.2408 |  |
| Circulatory disease | +0.5273 | 0.5281 | ±1.0563 | +0.998 | 0.3181 |  |
| **SD of daily means (mg/dL)** | **+0.0855** | 0.0286 | ±0.0572 | **+2.990** | **0.0028** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **637**, R² = **0.1399**, Adj R² = **0.1247**, F-statistic = **9.24** (p = **1.86e-15**), Residual SE = **4.739** on **625** df, AIC = **3801.7**, BIC = **3855.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.0144** | 2.1280 | ±4.2561 | **+5.176** | **2.27e-07** | *** |
| **Education: graduate level (vs college)** | **-0.9937** | 0.4128 | ±0.8256 | **-2.407** | **0.0161** | * |
| **Education: high school or below (vs college)** | **+1.8086** | 0.7803 | ±1.5605 | **+2.318** | **0.0205** | * |
| Site: UCSD (vs UAB) | +0.9220 | 0.5179 | ±1.0359 | +1.780 | 0.0751 | . |
| Site: UW (vs UAB) | +0.3930 | 0.4477 | ±0.8953 | +0.878 | 0.3800 |  |
| **Age (years)** | **-0.0855** | 0.0176 | ±0.0351 | **-4.868** | **1.13e-06** | *** |
| **BMI (kg/m2)** | **+0.1126** | 0.0308 | ±0.0616 | **+3.659** | **2.53e-04** | *** |
| Hypertension | -0.2897 | 0.4462 | ±0.8924 | -0.649 | 0.5162 |  |
| High cholesterol | +0.6334 | 0.3999 | ±0.7998 | +1.584 | 0.1132 |  |
| Kidney disease | +0.8017 | 0.7287 | ±1.4574 | +1.100 | 0.2713 |  |
| Circulatory disease | +0.5632 | 0.5285 | ±1.0570 | +1.066 | 0.2866 |  |
| **Time in range 70-180, pooled (%)** | **-0.0423** | 0.0144 | ±0.0289 | **-2.927** | **0.0034** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **637**, R² = **0.1407**, Adj R² = **0.1256**, F-statistic = **9.30** (p = **1.42e-15**), Residual SE = **4.736** on **625** df, AIC = **3801.1**, BIC = **3854.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.1746** | 2.1409 | ±4.2818 | **+5.220** | **1.79e-07** | *** |
| **Education: graduate level (vs college)** | **-0.9898** | 0.4126 | ±0.8251 | **-2.399** | **0.0164** | * |
| **Education: high school or below (vs college)** | **+1.7956** | 0.7789 | ±1.5578 | **+2.305** | **0.0212** | * |
| Site: UCSD (vs UAB) | +0.9218 | 0.5175 | ±1.0350 | +1.781 | 0.0749 | . |
| Site: UW (vs UAB) | +0.3997 | 0.4474 | ±0.8947 | +0.894 | 0.3716 |  |
| **Age (years)** | **-0.0858** | 0.0176 | ±0.0351 | **-4.887** | **1.03e-06** | *** |
| **BMI (kg/m2)** | **+0.1126** | 0.0308 | ±0.0616 | **+3.657** | **2.55e-04** | *** |
| Hypertension | -0.2898 | 0.4459 | ±0.8919 | -0.650 | 0.5158 |  |
| High cholesterol | +0.6274 | 0.3997 | ±0.7994 | +1.570 | 0.1165 |  |
| Kidney disease | +0.7849 | 0.7285 | ±1.4571 | +1.077 | 0.2813 |  |
| Circulatory disease | +0.5631 | 0.5282 | ±1.0564 | +1.066 | 0.2864 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0436** | 0.0145 | ±0.0290 | **-3.007** | **0.0026** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **637**, R² = **0.1297**, Adj R² = **0.1144**, F-statistic = **8.47** (p = **5.30e-14**), Residual SE = **4.767** on **625** df, AIC = **3809.2**, BIC = **3862.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.0328** | 1.5613 | ±3.1226 | **+4.505** | **6.65e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0520** | 0.4161 | ±0.8321 | **-2.529** | **0.0115** | * |
| **Education: high school or below (vs college)** | **+1.9505** | 0.7880 | ±1.5759 | **+2.475** | **0.0133** | * |
| Site: UCSD (vs UAB) | +0.8396 | 0.5301 | ±1.0602 | +1.584 | 0.1132 |  |
| Site: UW (vs UAB) | +0.2376 | 0.4536 | ±0.9072 | +0.524 | 0.6003 |  |
| **Age (years)** | **-0.0831** | 0.0174 | ±0.0349 | **-4.765** | **1.89e-06** | *** |
| **BMI (kg/m2)** | **+0.1135** | 0.0307 | ±0.0615 | **+3.692** | **2.23e-04** | *** |
| Hypertension | -0.1904 | 0.4485 | ±0.8971 | -0.425 | 0.6711 |  |
| High cholesterol | +0.6594 | 0.4063 | ±0.8125 | +1.623 | 0.1046 |  |
| Kidney disease | +1.1022 | 0.7119 | ±1.4238 | +1.548 | 0.1216 |  |
| Circulatory disease | +0.5862 | 0.5308 | ±1.0615 | +1.105 | 0.2694 |  |
| Time < 54 (%) | -0.1378 | 0.1948 | ±0.3897 | -0.707 | 0.4795 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **637**, R² = **0.1292**, Adj R² = **0.1139**, F-statistic = **8.43** (p = **6.23e-14**), Residual SE = **4.768** on **625** df, AIC = **3809.5**, BIC = **3863.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.9475** | 1.5527 | ±3.1054 | **+4.474** | **7.66e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0503** | 0.4165 | ±0.8330 | **-2.522** | **0.0117** | * |
| **Education: high school or below (vs college)** | **+1.9657** | 0.7890 | ±1.5779 | **+2.492** | **0.0127** | * |
| Site: UCSD (vs UAB) | +0.8737 | 0.5265 | ±1.0531 | +1.659 | 0.0970 | . |
| Site: UW (vs UAB) | +0.2629 | 0.4524 | ±0.9047 | +0.581 | 0.5612 |  |
| **Age (years)** | **-0.0831** | 0.0175 | ±0.0350 | **-4.750** | **2.03e-06** | *** |
| **BMI (kg/m2)** | **+0.1138** | 0.0308 | ±0.0615 | **+3.698** | **2.17e-04** | *** |
| Hypertension | -0.1827 | 0.4495 | ±0.8990 | -0.406 | 0.6844 |  |
| High cholesterol | +0.6719 | 0.4055 | ±0.8109 | +1.657 | 0.0975 | . |
| Kidney disease | +1.1013 | 0.7137 | ±1.4274 | +1.543 | 0.1228 |  |
| Circulatory disease | +0.5843 | 0.5323 | ±1.0645 | +1.098 | 0.2723 |  |
| Avg. daily time < 54 (%) | -0.0446 | 0.2502 | ±0.5004 | -0.178 | 0.8585 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **637**, R² = **0.1298**, Adj R² = **0.1145**, F-statistic = **8.48** (p = **5.06e-14**), Residual SE = **4.766** on **625** df, AIC = **3809.1**, BIC = **3862.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8423** | 1.5523 | ±3.1046 | **+4.408** | **1.04e-05** | *** |
| **Education: graduate level (vs college)** | **-1.0299** | 0.4161 | ±0.8322 | **-2.475** | **0.0133** | * |
| **Education: high school or below (vs college)** | **+1.9751** | 0.7858 | ±1.5717 | **+2.513** | **0.0120** | * |
| Site: UCSD (vs UAB) | +0.9097 | 0.5224 | ±1.0448 | +1.741 | 0.0816 | . |
| Site: UW (vs UAB) | +0.3050 | 0.4469 | ±0.8939 | +0.682 | 0.4950 |  |
| **Age (years)** | **-0.0838** | 0.0174 | ±0.0349 | **-4.805** | **1.54e-06** | *** |
| **BMI (kg/m2)** | **+0.1138** | 0.0308 | ±0.0616 | **+3.697** | **2.18e-04** | *** |
| Hypertension | -0.1623 | 0.4488 | ±0.8976 | -0.362 | 0.7176 |  |
| High cholesterol | +0.6838 | 0.4057 | ±0.8114 | +1.685 | 0.0919 | . |
| Kidney disease | +1.0850 | 0.7139 | ±1.4278 | +1.520 | 0.1286 |  |
| Circulatory disease | +0.5887 | 0.5316 | ±1.0632 | +1.108 | 0.2681 |  |
| Time 54-69, pooled (%) | +0.0590 | 0.0821 | ±0.1642 | +0.719 | 0.4720 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **637**, R² = **0.1304**, Adj R² = **0.1151**, F-statistic = **8.52** (p = **4.15e-14**), Residual SE = **4.765** on **625** df, AIC = **3808.6**, BIC = **3862.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8476** | 1.5487 | ±3.0974 | **+4.422** | **9.80e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0207** | 0.4161 | ±0.8322 | **-2.453** | **0.0142** | * |
| **Education: high school or below (vs college)** | **+1.9758** | 0.7858 | ±1.5716 | **+2.514** | **0.0119** | * |
| Site: UCSD (vs UAB) | +0.9130 | 0.5219 | ±1.0438 | +1.749 | 0.0802 | . |
| Site: UW (vs UAB) | +0.3200 | 0.4465 | ±0.8930 | +0.717 | 0.4736 |  |
| **Age (years)** | **-0.0844** | 0.0175 | ±0.0349 | **-4.831** | **1.36e-06** | *** |
| **BMI (kg/m2)** | **+0.1136** | 0.0308 | ±0.0615 | **+3.693** | **2.21e-04** | *** |
| Hypertension | -0.1567 | 0.4486 | ±0.8973 | -0.349 | 0.7269 |  |
| High cholesterol | +0.6856 | 0.4054 | ±0.8108 | +1.691 | 0.0908 | . |
| Kidney disease | +1.0820 | 0.7126 | ±1.4251 | +1.518 | 0.1289 |  |
| Circulatory disease | +0.5915 | 0.5318 | ±1.0635 | +1.112 | 0.2660 |  |
| Avg. daily time 54-69 (%) | +0.0783 | 0.0804 | ±0.1607 | +0.974 | 0.3301 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **637**, R² = **0.1293**, Adj R² = **0.1140**, F-statistic = **8.44** (p = **5.93e-14**), Residual SE = **4.768** on **625** df, AIC = **3809.4**, BIC = **3862.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8744** | 1.5572 | ±3.1144 | **+4.415** | **1.01e-05** | *** |
| **Education: graduate level (vs college)** | **-1.0387** | 0.4165 | ±0.8330 | **-2.494** | **0.0126** | * |
| **Education: high school or below (vs college)** | **+1.9771** | 0.7860 | ±1.5719 | **+2.515** | **0.0119** | * |
| Site: UCSD (vs UAB) | +0.9036 | 0.5240 | ±1.0480 | +1.724 | 0.0846 | . |
| Site: UW (vs UAB) | +0.2945 | 0.4485 | ±0.8971 | +0.656 | 0.5115 |  |
| **Age (years)** | **-0.0835** | 0.0174 | ±0.0349 | **-4.791** | **1.66e-06** | *** |
| **BMI (kg/m2)** | **+0.1139** | 0.0308 | ±0.0615 | **+3.701** | **2.14e-04** | *** |
| Hypertension | -0.1699 | 0.4492 | ±0.8984 | -0.378 | 0.7053 |  |
| High cholesterol | +0.6830 | 0.4061 | ±0.8123 | +1.682 | 0.0926 | . |
| Kidney disease | +1.0921 | 0.7148 | ±1.4297 | +1.528 | 0.1266 |  |
| Circulatory disease | +0.5846 | 0.5316 | ±1.0631 | +1.100 | 0.2714 |  |
| Time < 70 (%) | +0.0256 | 0.0653 | ±0.1306 | +0.393 | 0.6946 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **637**, R² = **0.1299**, Adj R² = **0.1146**, F-statistic = **8.49** (p = **4.89e-14**), Residual SE = **4.766** on **625** df, AIC = **3809.0**, BIC = **3862.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8603** | 1.5503 | ±3.1006 | **+4.425** | **9.64e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0264** | 0.4165 | ±0.8329 | **-2.465** | **0.0137** | * |
| **Education: high school or below (vs college)** | **+1.9811** | 0.7858 | ±1.5717 | **+2.521** | **0.0117** | * |
| Site: UCSD (vs UAB) | +0.9146 | 0.5224 | ±1.0449 | +1.751 | 0.0800 | . |
| Site: UW (vs UAB) | +0.3167 | 0.4474 | ±0.8948 | +0.708 | 0.4790 |  |
| **Age (years)** | **-0.0842** | 0.0175 | ±0.0349 | **-4.819** | **1.44e-06** | *** |
| **BMI (kg/m2)** | **+0.1138** | 0.0308 | ±0.0615 | **+3.698** | **2.17e-04** | *** |
| Hypertension | -0.1610 | 0.4491 | ±0.8982 | -0.358 | 0.7200 |  |
| High cholesterol | +0.6879 | 0.4055 | ±0.8111 | +1.696 | 0.0899 | . |
| Kidney disease | +1.0851 | 0.7136 | ±1.4273 | +1.521 | 0.1284 |  |
| Circulatory disease | +0.5865 | 0.5320 | ±1.0641 | +1.102 | 0.2703 |  |
| Avg. daily time < 70 (%) | +0.0504 | 0.0659 | ±0.1318 | +0.765 | 0.4445 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **637**, R² = **0.1431**, Adj R² = **0.1280**, F-statistic = **9.49** (p = **6.43e-16**), Residual SE = **4.730** on **625** df, AIC = **3799.3**, BIC = **3852.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.3366** | 2.7708 | ±5.5417 | **+6.257** | **3.93e-10** | *** |
| **Education: graduate level (vs college)** | **-0.9902** | 0.4146 | ±0.8292 | **-2.388** | **0.0169** | * |
| **Education: high school or below (vs college)** | **+1.7965** | 0.7678 | ±1.5357 | **+2.340** | **0.0193** | * |
| Site: UCSD (vs UAB) | +0.9491 | 0.5166 | ±1.0333 | +1.837 | 0.0662 | . |
| Site: UW (vs UAB) | +0.4095 | 0.4495 | ±0.8989 | +0.911 | 0.3623 |  |
| **Age (years)** | **-0.0829** | 0.0174 | ±0.0349 | **-4.758** | **1.95e-06** | *** |
| **BMI (kg/m2)** | **+0.1147** | 0.0308 | ±0.0615 | **+3.729** | **1.92e-04** | *** |
| Hypertension | -0.2673 | 0.4437 | ±0.8875 | -0.602 | 0.5469 |  |
| High cholesterol | +0.7153 | 0.4002 | ±0.8005 | +1.787 | 0.0739 | . |
| Kidney disease | +0.9354 | 0.7178 | ±1.4356 | +1.303 | 0.1925 |  |
| Circulatory disease | +0.5379 | 0.5264 | ±1.0527 | +1.022 | 0.3068 |  |
| **Time 54-250, pooled (%)** | **-0.1065** | 0.0239 | ±0.0478 | **-4.458** | **8.28e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **637**, R² = **0.1431**, Adj R² = **0.1280**, F-statistic = **9.49** (p = **6.37e-16**), Residual SE = **4.730** on **625** df, AIC = **3799.3**, BIC = **3852.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.5038** | 3.3915 | ±6.7830 | **+5.456** | **4.87e-08** | *** |
| **Education: graduate level (vs college)** | **-0.9832** | 0.4146 | ±0.8292 | **-2.371** | **0.0177** | * |
| **Education: high school or below (vs college)** | **+1.7667** | 0.7677 | ±1.5354 | **+2.301** | **0.0214** | * |
| Site: UCSD (vs UAB) | +0.9370 | 0.5158 | ±1.0317 | +1.816 | 0.0693 | . |
| Site: UW (vs UAB) | +0.4043 | 0.4486 | ±0.8973 | +0.901 | 0.3675 |  |
| **Age (years)** | **-0.0837** | 0.0174 | ±0.0349 | **-4.800** | **1.59e-06** | *** |
| **BMI (kg/m2)** | **+0.1152** | 0.0307 | ±0.0615 | **+3.747** | **1.79e-04** | *** |
| Hypertension | -0.2686 | 0.4440 | ±0.8880 | -0.605 | 0.5452 |  |
| High cholesterol | +0.7089 | 0.4002 | ±0.8003 | +1.772 | 0.0765 | . |
| Kidney disease | +0.9039 | 0.7163 | ±1.4325 | +1.262 | 0.2070 |  |
| Circulatory disease | +0.5265 | 0.5270 | ±1.0541 | +0.999 | 0.3178 |  |
| **Avg. daily time 54-250 (%)** | **-0.1177** | 0.0308 | ±0.0616 | **-3.818** | **1.35e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **637**, R² = **0.1334**, Adj R² = **0.1182**, F-statistic = **8.75** (p = **1.56e-14**), Residual SE = **4.756** on **625** df, AIC = **3806.4**, BIC = **3859.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.9487** | 1.5459 | ±3.0917 | **+4.495** | **6.96e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0302** | 0.4137 | ±0.8274 | **-2.490** | **0.0128** | * |
| **Education: high school or below (vs college)** | **+1.8843** | 0.7882 | ±1.5764 | **+2.391** | **0.0168** | * |
| Site: UCSD (vs UAB) | +0.8786 | 0.5226 | ±1.0453 | +1.681 | 0.0928 | . |
| Site: UW (vs UAB) | +0.3135 | 0.4485 | ±0.8970 | +0.699 | 0.4845 |  |
| **Age (years)** | **-0.0850** | 0.0176 | ±0.0351 | **-4.840** | **1.30e-06** | *** |
| **BMI (kg/m2)** | **+0.1125** | 0.0308 | ±0.0615 | **+3.656** | **2.56e-04** | *** |
| Hypertension | -0.2592 | 0.4486 | ±0.8972 | -0.578 | 0.5635 |  |
| High cholesterol | +0.6188 | 0.4032 | ±0.8064 | +1.535 | 0.1248 |  |
| Kidney disease | +0.8962 | 0.7307 | ±1.4615 | +1.226 | 0.2200 |  |
| Circulatory disease | +0.5771 | 0.5306 | ±1.0613 | +1.088 | 0.2768 |  |
| Time 181-250, pooled (%) | +0.0385 | 0.0225 | ±0.0450 | +1.711 | 0.0871 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **637**, R² = **0.1346**, Adj R² = **0.1194**, F-statistic = **8.84** (p = **1.06e-14**), Residual SE = **4.753** on **625** df, AIC = **3805.5**, BIC = **3859.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.9346** | 1.5456 | ±3.0911 | **+4.487** | **7.23e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0288** | 0.4134 | ±0.8269 | **-2.488** | **0.0128** | * |
| **Education: high school or below (vs college)** | **+1.8726** | 0.7869 | ±1.5738 | **+2.380** | **0.0173** | * |
| Site: UCSD (vs UAB) | +0.8862 | 0.5221 | ±1.0442 | +1.697 | 0.0896 | . |
| Site: UW (vs UAB) | +0.3245 | 0.4484 | ±0.8968 | +0.724 | 0.4693 |  |
| **Age (years)** | **-0.0850** | 0.0176 | ±0.0351 | **-4.840** | **1.30e-06** | *** |
| **BMI (kg/m2)** | **+0.1122** | 0.0308 | ±0.0616 | **+3.646** | **2.66e-04** | *** |
| Hypertension | -0.2664 | 0.4480 | ±0.8960 | -0.595 | 0.5521 |  |
| High cholesterol | +0.6127 | 0.4027 | ±0.8054 | +1.521 | 0.1281 |  |
| Kidney disease | +0.8741 | 0.7321 | ±1.4641 | +1.194 | 0.2325 |  |
| Circulatory disease | +0.5790 | 0.5302 | ±1.0605 | +1.092 | 0.2748 |  |
| Avg. daily time 181-250 (%) | +0.0422 | 0.0223 | ±0.0445 | +1.894 | 0.0582 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **637**, R² = **0.1392**, Adj R² = **0.1241**, F-statistic = **9.19** (p = **2.30e-15**), Residual SE = **4.740** on **625** df, AIC = **3802.1**, BIC = **3855.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8851** | 1.5425 | ±3.0851 | **+4.463** | **8.06e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0087** | 0.4132 | ±0.8264 | **-2.441** | **0.0146** | * |
| **Education: high school or below (vs college)** | **+1.8049** | 0.7812 | ±1.5625 | **+2.310** | **0.0209** | * |
| Site: UCSD (vs UAB) | +0.8899 | 0.5193 | ±1.0386 | +1.714 | 0.0866 | . |
| Site: UW (vs UAB) | +0.3572 | 0.4482 | ±0.8963 | +0.797 | 0.4255 |  |
| **Age (years)** | **-0.0850** | 0.0175 | ±0.0351 | **-4.844** | **1.27e-06** | *** |
| **BMI (kg/m2)** | **+0.1126** | 0.0307 | ±0.0615 | **+3.663** | **2.49e-04** | *** |
| Hypertension | -0.3015 | 0.4472 | ±0.8944 | -0.674 | 0.5002 |  |
| High cholesterol | +0.6247 | 0.4002 | ±0.8004 | +1.561 | 0.1185 |  |
| Kidney disease | +0.8212 | 0.7283 | ±1.4566 | +1.128 | 0.2595 |  |
| Circulatory disease | +0.5606 | 0.5280 | ±1.0559 | +1.062 | 0.2883 |  |
| **Time > 180 (%)** | **+0.0410** | 0.0148 | ±0.0295 | **+2.778** | **0.0055** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **637**, R² = **0.1395**, Adj R² = **0.1244**, F-statistic = **9.21** (p = **2.11e-15**), Residual SE = **4.740** on **625** df, AIC = **3801.9**, BIC = **3855.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8802** | 1.5428 | ±3.0855 | **+4.460** | **8.21e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0095** | 0.4131 | ±0.8262 | **-2.444** | **0.0145** | * |
| **Education: high school or below (vs college)** | **+1.7961** | 0.7803 | ±1.5605 | **+2.302** | **0.0213** | * |
| Site: UCSD (vs UAB) | +0.8950 | 0.5190 | ±1.0380 | +1.725 | 0.0846 | . |
| Site: UW (vs UAB) | +0.3589 | 0.4481 | ±0.8963 | +0.801 | 0.4232 |  |
| **Age (years)** | **-0.0849** | 0.0175 | ±0.0351 | **-4.844** | **1.27e-06** | *** |
| **BMI (kg/m2)** | **+0.1127** | 0.0307 | ±0.0615 | **+3.664** | **2.48e-04** | *** |
| Hypertension | -0.2998 | 0.4470 | ±0.8941 | -0.671 | 0.5025 |  |
| High cholesterol | +0.6205 | 0.4001 | ±0.8001 | +1.551 | 0.1209 |  |
| Kidney disease | +0.8109 | 0.7287 | ±1.4574 | +1.113 | 0.2658 |  |
| Circulatory disease | +0.5608 | 0.5278 | ±1.0557 | +1.062 | 0.2881 |  |
| **Avg. daily time > 180 (%)** | **+0.0415** | 0.0149 | ±0.0298 | **+2.784** | **0.0054** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **637**, R² = **0.1495**, Adj R² = **0.1346**, F-statistic = **9.99** (p = **7.36e-17**), Residual SE = **4.712** on **625** df, AIC = **3794.5**, BIC = **3848.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8736** | 1.5394 | ±3.0787 | **+4.465** | **8.00e-06** | *** |
| **Education: graduate level (vs college)** | **-0.9813** | 0.4111 | ±0.8222 | **-2.387** | **0.0170** | * |
| **Education: high school or below (vs college)** | **+1.8064** | 0.7715 | ±1.5430 | **+2.341** | **0.0192** | * |
| Site: UCSD (vs UAB) | +0.9276 | 0.5138 | ±1.0276 | +1.805 | 0.0710 | . |
| Site: UW (vs UAB) | +0.3794 | 0.4460 | ±0.8920 | +0.851 | 0.3950 |  |
| **Age (years)** | **-0.0834** | 0.0175 | ±0.0350 | **-4.764** | **1.90e-06** | *** |
| **BMI (kg/m2)** | **+0.1099** | 0.0307 | ±0.0615 | **+3.575** | **3.50e-04** | *** |
| Hypertension | -0.3480 | 0.4440 | ±0.8879 | -0.784 | 0.4331 |  |
| High cholesterol | +0.6035 | 0.3970 | ±0.7940 | +1.520 | 0.1285 |  |
| Kidney disease | +0.9445 | 0.7250 | ±1.4501 | +1.303 | 0.1927 |  |
| Circulatory disease | +0.5375 | 0.5270 | ±1.0539 | +1.020 | 0.3077 |  |
| **Nocturnal time > 180 (%)** | **+0.0608** | 0.0148 | ±0.0297 | **+4.094** | **4.25e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **637**, R² = **0.1339**, Adj R² = **0.1187**, F-statistic = **8.79** (p = **1.33e-14**), Residual SE = **4.755** on **625** df, AIC = **3806.1**, BIC = **3859.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.8694** | 1.5351 | ±3.0702 | **+4.475** | **7.64e-06** | *** |
| **Education: graduate level (vs college)** | **-1.0025** | 0.4128 | ±0.8256 | **-2.429** | **0.0152** | * |
| **Education: high school or below (vs college)** | **+1.8976** | 0.7823 | ±1.5647 | **+2.425** | **0.0153** | * |
| Site: UCSD (vs UAB) | +0.8535 | 0.5250 | ±1.0499 | +1.626 | 0.1040 |  |
| Site: UW (vs UAB) | +0.3011 | 0.4482 | ±0.8965 | +0.672 | 0.5017 |  |
| **Age (years)** | **-0.0864** | 0.0174 | ±0.0347 | **-4.971** | **6.66e-07** | *** |
| **BMI (kg/m2)** | **+0.1162** | 0.0306 | ±0.0612 | **+3.796** | **1.47e-04** | *** |
| Hypertension | -0.2739 | 0.4504 | ±0.9007 | -0.608 | 0.5431 |  |
| High cholesterol | +0.6603 | 0.4041 | ±0.8081 | +1.634 | 0.1022 |  |
| Kidney disease | +0.9064 | 0.7084 | ±1.4169 | +1.279 | 0.2007 |  |
| Circulatory disease | +0.5933 | 0.5300 | ±1.0601 | +1.119 | 0.2630 |  |
| Any reading > 250 during wear (0/1) | +0.8037 | 0.4308 | ±0.8617 | +1.865 | 0.0621 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **637**, R² = **0.1444**, Adj R² = **0.1293**, F-statistic = **9.59** (p = **4.17e-16**), Residual SE = **4.726** on **625** df, AIC = **3798.3**, BIC = **3851.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.7537** | 1.5399 | ±3.0798 | **+4.386** | **1.16e-05** | *** |
| **Education: graduate level (vs college)** | **-0.9908** | 0.4142 | ±0.8283 | **-2.392** | **0.0167** | * |
| **Education: high school or below (vs college)** | **+1.7685** | 0.7689 | ±1.5378 | **+2.300** | **0.0214** | * |
| Site: UCSD (vs UAB) | +0.9164 | 0.5164 | ±1.0329 | +1.775 | 0.0760 | . |
| Site: UW (vs UAB) | +0.3876 | 0.4482 | ±0.8965 | +0.865 | 0.3871 |  |
| **Age (years)** | **-0.0828** | 0.0174 | ±0.0349 | **-4.751** | **2.03e-06** | *** |
| **BMI (kg/m2)** | **+0.1145** | 0.0307 | ±0.0614 | **+3.727** | **1.94e-04** | *** |
| Hypertension | -0.2818 | 0.4437 | ±0.8874 | -0.635 | 0.5254 |  |
| High cholesterol | +0.7034 | 0.3997 | ±0.7993 | +1.760 | 0.0784 | . |
| Kidney disease | +0.9283 | 0.7162 | ±1.4323 | +1.296 | 0.1949 |  |
| Circulatory disease | +0.5382 | 0.5253 | ±1.0507 | +1.024 | 0.3056 |  |
| **Time > 250 (%)** | **+0.1130** | 0.0251 | ±0.0501 | **+4.509** | **6.50e-06** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **637**, R² = **0.1439**, Adj R² = **0.1288**, F-statistic = **9.55** (p = **4.94e-16**), Residual SE = **4.728** on **625** df, AIC = **3798.7**, BIC = **3852.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.7710** | 1.5396 | ±3.0792 | **+4.398** | **1.09e-05** | *** |
| **Education: graduate level (vs college)** | **-0.9892** | 0.4142 | ±0.8285 | **-2.388** | **0.0169** | * |
| **Education: high school or below (vs college)** | **+1.7408** | 0.7701 | ±1.5402 | **+2.261** | **0.0238** | * |
| Site: UCSD (vs UAB) | +0.9105 | 0.5160 | ±1.0321 | +1.765 | 0.0776 | . |
| Site: UW (vs UAB) | +0.3787 | 0.4479 | ±0.8957 | +0.846 | 0.3978 |  |
| **Age (years)** | **-0.0832** | 0.0174 | ±0.0349 | **-4.775** | **1.80e-06** | *** |
| **BMI (kg/m2)** | **+0.1150** | 0.0307 | ±0.0614 | **+3.748** | **1.78e-04** | *** |
| Hypertension | -0.2819 | 0.4441 | ±0.8882 | -0.635 | 0.5255 |  |
| High cholesterol | +0.6972 | 0.3998 | ±0.7996 | +1.744 | 0.0812 | . |
| Kidney disease | +0.9018 | 0.7157 | ±1.4314 | +1.260 | 0.2077 |  |
| Circulatory disease | +0.5284 | 0.5262 | ±1.0524 | +1.004 | 0.3153 |  |
| **Avg. daily time > 250 (%)** | **+0.1231** | 0.0332 | ±0.0664 | **+3.708** | **2.09e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 637; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0687**, LLR χ² = **45.59** (p = **1.70e-06**), AUC = **0.6867**, AIC = **639.6**, BIC = **688.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4437 | 0.7945 | ±1.5889 | -1.817 | 0.0692 | 0.2361 | . |
| Education: graduate level (vs college) | -0.3656 | 0.2334 | ±0.4668 | -1.567 | 0.1172 | 0.6938 |  |
| Education: high school or below (vs college) | +0.4017 | 0.3147 | ±0.6293 | +1.277 | 0.2017 | 1.4944 |  |
| Site: UCSD (vs UAB) | +0.2438 | 0.2671 | ±0.5341 | +0.913 | 0.3613 | 1.2761 |  |
| Site: UW (vs UAB) | +0.0406 | 0.2405 | ±0.4811 | +0.169 | 0.8661 | 1.0414 |  |
| **Age (years)** | **-0.0259** | 0.0103 | ±0.0206 | **-2.513** | **0.0120** | 0.9745 | * |
| **BMI (kg/m2)** | **+0.0456** | 0.0128 | ±0.0257 | **+3.557** | **3.75e-04** | 1.0467 | *** |
| Hypertension | -0.0530 | 0.2262 | ±0.4523 | -0.234 | 0.8149 | 0.9484 |  |
| High cholesterol | +0.2159 | 0.2130 | ±0.4261 | +1.013 | 0.3109 | 1.2409 |  |
| **Kidney disease** | **+0.6401** | 0.3115 | ±0.6230 | **+2.055** | **0.0399** | 1.8966 | * |
| Circulatory disease | +0.3612 | 0.2509 | ±0.5017 | +1.440 | 0.1499 | 1.4351 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0810**, LLR χ² = **53.74** (p = **1.32e-07**), AUC = **0.6962**, AIC = **633.5**, BIC = **687.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.0875** | 0.9916 | ±1.9832 | **-3.114** | **0.0018** | 0.0456 | ** |
| Education: graduate level (vs college) | -0.3246 | 0.2358 | ±0.4716 | -1.377 | 0.1686 | 0.7228 |  |
| Education: high school or below (vs college) | +0.3094 | 0.3210 | ±0.6420 | +0.964 | 0.3351 | 1.3627 |  |
| Site: UCSD (vs UAB) | +0.2241 | 0.2702 | ±0.5404 | +0.829 | 0.4068 | 1.2512 |  |
| Site: UW (vs UAB) | +0.1041 | 0.2438 | ±0.4876 | +0.427 | 0.6695 | 1.1097 |  |
| **Age (years)** | **-0.0286** | 0.0104 | ±0.0208 | **-2.755** | **0.0059** | 0.9718 | ** |
| **BMI (kg/m2)** | **+0.0431** | 0.0130 | ±0.0259 | **+3.329** | **8.73e-04** | 1.0441 | *** |
| Hypertension | -0.1450 | 0.2312 | ±0.4624 | -0.627 | 0.5305 | 0.8650 |  |
| High cholesterol | +0.1888 | 0.2148 | ±0.4297 | +0.879 | 0.3795 | 1.2078 |  |
| Kidney disease | +0.6130 | 0.3153 | ±0.6307 | +1.944 | 0.0519 | 1.8459 | . |
| Circulatory disease | +0.3685 | 0.2534 | ±0.5067 | +1.454 | 0.1458 | 1.4456 |  |
| **HbA1c (%)** | **+0.3224** | 0.1132 | ±0.2263 | **+2.849** | **0.0044** | 1.3804 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0827**, LLR χ² = **54.84** (p = **8.30e-08**), AUC = **0.6936**, AIC = **632.4**, BIC = **685.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.7706** | 0.9156 | ±1.8312 | **-3.026** | **0.0025** | 0.0626 | ** |
| Education: graduate level (vs college) | -0.3725 | 0.2353 | ±0.4705 | -1.583 | 0.1134 | 0.6890 |  |
| Education: high school or below (vs college) | +0.3110 | 0.3203 | ±0.6406 | +0.971 | 0.3316 | 1.3648 |  |
| Site: UCSD (vs UAB) | +0.2294 | 0.2707 | ±0.5415 | +0.847 | 0.3968 | 1.2579 |  |
| Site: UW (vs UAB) | +0.0721 | 0.2426 | ±0.4853 | +0.297 | 0.7664 | 1.0747 |  |
| **Age (years)** | **-0.0261** | 0.0103 | ±0.0207 | **-2.520** | **0.0117** | 0.9743 | * |
| **BMI (kg/m2)** | **+0.0445** | 0.0129 | ±0.0259 | **+3.438** | **5.87e-04** | 1.0455 | *** |
| Hypertension | -0.1570 | 0.2322 | ±0.4644 | -0.676 | 0.4988 | 0.8547 |  |
| High cholesterol | +0.1833 | 0.2153 | ±0.4306 | +0.851 | 0.3946 | 1.2012 |  |
| Kidney disease | +0.5485 | 0.3163 | ±0.6325 | +1.734 | 0.0828 | 1.7307 | . |
| Circulatory disease | +0.3446 | 0.2541 | ±0.5083 | +1.356 | 0.1752 | 1.4114 |  |
| **Mean glucose (mg/dL)** | **+0.0118** | 0.0039 | ±0.0078 | **+3.027** | **0.0025** | 1.0119 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0827**, LLR χ² = **54.84** (p = **8.30e-08**), AUC = **0.6936**, AIC = **632.4**, BIC = **685.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.4020** | 1.2667 | ±2.5334 | **-3.475** | **5.11e-04** | 0.0123 | *** |
| Education: graduate level (vs college) | -0.3725 | 0.2353 | ±0.4705 | -1.583 | 0.1134 | 0.6890 |  |
| Education: high school or below (vs college) | +0.3110 | 0.3203 | ±0.6406 | +0.971 | 0.3316 | 1.3648 |  |
| Site: UCSD (vs UAB) | +0.2294 | 0.2707 | ±0.5415 | +0.847 | 0.3968 | 1.2579 |  |
| Site: UW (vs UAB) | +0.0721 | 0.2426 | ±0.4853 | +0.297 | 0.7664 | 1.0747 |  |
| **Age (years)** | **-0.0261** | 0.0103 | ±0.0207 | **-2.520** | **0.0117** | 0.9743 | * |
| **BMI (kg/m2)** | **+0.0445** | 0.0129 | ±0.0259 | **+3.438** | **5.87e-04** | 1.0455 | *** |
| Hypertension | -0.1570 | 0.2322 | ±0.4644 | -0.676 | 0.4988 | 0.8547 |  |
| High cholesterol | +0.1833 | 0.2153 | ±0.4306 | +0.851 | 0.3946 | 1.2012 |  |
| Kidney disease | +0.5485 | 0.3163 | ±0.6325 | +1.734 | 0.0828 | 1.7307 | . |
| Circulatory disease | +0.3446 | 0.2541 | ±0.5083 | +1.356 | 0.1752 | 1.4114 |  |
| **GMI (%)** | **+0.4929** | 0.1628 | ±0.3256 | **+3.027** | **0.0025** | 1.6370 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0910**, LLR χ² = **60.33** (p = **8.04e-09**), AUC = **0.7029**, AIC = **626.9**, BIC = **680.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1287** | 0.9217 | ±1.8435 | **-3.394** | **6.88e-04** | 0.0438 | *** |
| Education: graduate level (vs college) | -0.3785 | 0.2361 | ±0.4721 | -1.603 | 0.1089 | 0.6849 |  |
| Education: high school or below (vs college) | +0.3007 | 0.3212 | ±0.6423 | +0.936 | 0.3492 | 1.3507 |  |
| Site: UCSD (vs UAB) | +0.2294 | 0.2723 | ±0.5447 | +0.842 | 0.3995 | 1.2579 |  |
| Site: UW (vs UAB) | +0.0652 | 0.2435 | ±0.4870 | +0.268 | 0.7889 | 1.0674 |  |
| **Age (years)** | **-0.0248** | 0.0104 | ±0.0208 | **-2.384** | **0.0171** | 0.9755 | * |
| **BMI (kg/m2)** | **+0.0424** | 0.0130 | ±0.0260 | **+3.270** | **0.0011** | 1.0433 | ** |
| Hypertension | -0.1739 | 0.2329 | ±0.4658 | -0.747 | 0.4552 | 0.8404 |  |
| High cholesterol | +0.1562 | 0.2171 | ±0.4343 | +0.719 | 0.4718 | 1.1691 |  |
| Kidney disease | +0.6170 | 0.3164 | ±0.6328 | +1.950 | 0.0512 | 1.8534 | . |
| Circulatory disease | +0.3571 | 0.2562 | ±0.5123 | +1.394 | 0.1633 | 1.4292 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0150** | 0.0040 | ±0.0080 | **+3.753** | **1.75e-04** | 1.0151 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0857**, LLR χ² = **56.85** (p = **3.55e-08**), AUC = **0.7024**, AIC = **630.4**, BIC = **683.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.9278** | 0.8177 | ±1.6353 | **-2.358** | **0.0184** | 0.1455 | * |
| Education: graduate level (vs college) | -0.3507 | 0.2359 | ±0.4719 | -1.487 | 0.1371 | 0.7042 |  |
| Education: high school or below (vs college) | +0.2472 | 0.3242 | ±0.6484 | +0.762 | 0.4458 | 1.2804 |  |
| Site: UCSD (vs UAB) | +0.2302 | 0.2708 | ±0.5416 | +0.850 | 0.3953 | 1.2589 |  |
| Site: UW (vs UAB) | +0.1153 | 0.2442 | ±0.4884 | +0.472 | 0.6368 | 1.1222 |  |
| **Age (years)** | **-0.0294** | 0.0104 | ±0.0209 | **-2.820** | **0.0048** | 0.9710 | ** |
| **BMI (kg/m2)** | **+0.0461** | 0.0130 | ±0.0259 | **+3.557** | **3.75e-04** | 1.0472 | *** |
| Hypertension | -0.1691 | 0.2331 | ±0.4662 | -0.726 | 0.4681 | 0.8444 |  |
| High cholesterol | +0.2206 | 0.2159 | ±0.4318 | +1.022 | 0.3068 | 1.2469 |  |
| Kidney disease | +0.4131 | 0.3247 | ±0.6494 | +1.272 | 0.2033 | 1.5115 |  |
| Circulatory disease | +0.3850 | 0.2535 | ±0.5070 | +1.519 | 0.1287 | 1.4697 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0274** | 0.0082 | ±0.0165 | **+3.330** | **8.69e-04** | 1.0278 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0816**, LLR χ² = **54.15** (p = **1.11e-07**), AUC = **0.6994**, AIC = **633.1**, BIC = **686.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.8797** | 0.8171 | ±1.6342 | **-2.301** | **0.0214** | 0.1526 | * |
| Education: graduate level (vs college) | -0.3460 | 0.2353 | ±0.4706 | -1.470 | 0.1415 | 0.7075 |  |
| Education: high school or below (vs college) | +0.2459 | 0.3243 | ±0.6487 | +0.758 | 0.4483 | 1.2788 |  |
| Site: UCSD (vs UAB) | +0.2284 | 0.2699 | ±0.5399 | +0.846 | 0.3974 | 1.2566 |  |
| Site: UW (vs UAB) | +0.0988 | 0.2434 | ±0.4868 | +0.406 | 0.6849 | 1.1038 |  |
| **Age (years)** | **-0.0292** | 0.0104 | ±0.0209 | **-2.797** | **0.0052** | 0.9712 | ** |
| **BMI (kg/m2)** | **+0.0462** | 0.0129 | ±0.0259 | **+3.576** | **3.48e-04** | 1.0473 | *** |
| Hypertension | -0.1453 | 0.2318 | ±0.4636 | -0.627 | 0.5307 | 0.8647 |  |
| High cholesterol | +0.2164 | 0.2153 | ±0.4306 | +1.005 | 0.3147 | 1.2416 |  |
| Kidney disease | +0.4318 | 0.3240 | ±0.6480 | +1.333 | 0.1826 | 1.5401 |  |
| Circulatory disease | +0.3911 | 0.2526 | ±0.5053 | +1.548 | 0.1216 | 1.4787 |  |
| **Avg. daily SD (mg/dL)** | **+0.0279** | 0.0096 | ±0.0192 | **+2.905** | **0.0037** | 1.0283 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0763**, LLR χ² = **50.63** (p = **4.81e-07**), AUC = **0.7005**, AIC = **636.6**, BIC = **690.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0308** | 0.8424 | ±1.6848 | **-2.411** | **0.0159** | 0.1312 | * |
| Education: graduate level (vs college) | -0.3537 | 0.2349 | ±0.4698 | -1.506 | 0.1321 | 0.7021 |  |
| Education: high school or below (vs college) | +0.3032 | 0.3200 | ±0.6399 | +0.948 | 0.3433 | 1.3542 |  |
| Site: UCSD (vs UAB) | +0.2345 | 0.2683 | ±0.5366 | +0.874 | 0.3820 | 1.2643 |  |
| Site: UW (vs UAB) | +0.0958 | 0.2433 | ±0.4867 | +0.394 | 0.6938 | 1.1006 |  |
| **Age (years)** | **-0.0297** | 0.0105 | ±0.0210 | **-2.828** | **0.0047** | 0.9708 | ** |
| **BMI (kg/m2)** | **+0.0463** | 0.0129 | ±0.0258 | **+3.589** | **3.32e-04** | 1.0474 | *** |
| Hypertension | -0.1108 | 0.2297 | ±0.4594 | -0.482 | 0.6295 | 0.8951 |  |
| High cholesterol | +0.2346 | 0.2147 | ±0.4294 | +1.093 | 0.2745 | 1.2644 |  |
| Kidney disease | +0.4654 | 0.3237 | ±0.6474 | +1.438 | 0.1505 | 1.5927 |  |
| Circulatory disease | +0.3871 | 0.2519 | ±0.5039 | +1.536 | 0.1244 | 1.4727 |  |
| **CV (%)** | **+0.0383** | 0.0169 | ±0.0338 | **+2.262** | **0.0237** | 1.0390 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0765**, LLR χ² = **50.75** (p = **4.59e-07**), AUC = **0.6979**, AIC = **636.5**, BIC = **690.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2118 | 0.9624 | ±1.9249 | -0.220 | 0.8258 | 0.8092 |  |
| Education: graduate level (vs college) | -0.3691 | 0.2349 | ±0.4699 | -1.571 | 0.1162 | 0.6914 |  |
| Education: high school or below (vs college) | +0.3027 | 0.3194 | ±0.6389 | +0.948 | 0.3433 | 1.3536 |  |
| Site: UCSD (vs UAB) | +0.2250 | 0.2684 | ±0.5369 | +0.838 | 0.4019 | 1.2523 |  |
| Site: UW (vs UAB) | +0.0778 | 0.2426 | ±0.4851 | +0.321 | 0.7484 | 1.0809 |  |
| **Age (years)** | **-0.0301** | 0.0105 | ±0.0210 | **-2.857** | **0.0043** | 0.9704 | ** |
| **BMI (kg/m2)** | **+0.0455** | 0.0129 | ±0.0257 | **+3.539** | **4.02e-04** | 1.0466 | *** |
| Hypertension | -0.1029 | 0.2293 | ±0.4586 | -0.449 | 0.6535 | 0.9022 |  |
| High cholesterol | +0.2271 | 0.2146 | ±0.4293 | +1.058 | 0.2900 | 1.2549 |  |
| Kidney disease | +0.5085 | 0.3190 | ±0.6379 | +1.594 | 0.1109 | 1.6629 |  |
| Circulatory disease | +0.3711 | 0.2516 | ±0.5032 | +1.475 | 0.1402 | 1.4494 |  |
| **Mean / SD ratio** | **-0.1873** | 0.0835 | ±0.1671 | **-2.242** | **0.0249** | 0.8292 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0719**, LLR χ² = **47.67** (p = **1.63e-06**), AUC = **0.6928**, AIC = **639.6**, BIC = **693.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6763 | 0.9562 | ±1.9124 | -0.707 | 0.4794 | 0.5085 |  |
| Education: graduate level (vs college) | -0.3615 | 0.2341 | ±0.4683 | -1.544 | 0.1225 | 0.6966 |  |
| Education: high school or below (vs college) | +0.3323 | 0.3190 | ±0.6379 | +1.042 | 0.2976 | 1.3941 |  |
| Site: UCSD (vs UAB) | +0.2223 | 0.2679 | ±0.5358 | +0.830 | 0.4067 | 1.2490 |  |
| Site: UW (vs UAB) | +0.0583 | 0.2415 | ±0.4829 | +0.241 | 0.8093 | 1.0600 |  |
| **Age (years)** | **-0.0287** | 0.0105 | ±0.0210 | **-2.728** | **0.0064** | 0.9717 | ** |
| **BMI (kg/m2)** | **+0.0455** | 0.0129 | ±0.0257 | **+3.541** | **3.99e-04** | 1.0466 | *** |
| Hypertension | -0.0741 | 0.2278 | ±0.4556 | -0.325 | 0.7450 | 0.9286 |  |
| High cholesterol | +0.2198 | 0.2138 | ±0.4275 | +1.028 | 0.3038 | 1.2458 |  |
| Kidney disease | +0.5627 | 0.3167 | ±0.6334 | +1.777 | 0.0756 | 1.7554 | . |
| Circulatory disease | +0.3694 | 0.2511 | ±0.5021 | +1.471 | 0.1412 | 1.4468 |  |
| Avg. daily mean/SD | -0.0971 | 0.0679 | ±0.1358 | -1.429 | 0.1530 | 0.9075 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0696**, LLR χ² = **46.17** (p = **3.01e-06**), AUC = **0.6888**, AIC = **641.1**, BIC = **694.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.7616** | 0.8974 | ±1.7947 | **-1.963** | **0.0496** | 0.1718 | * |
| Education: graduate level (vs college) | -0.3651 | 0.2336 | ±0.4673 | -1.563 | 0.1182 | 0.6941 |  |
| Education: high school or below (vs college) | +0.3699 | 0.3178 | ±0.6357 | +1.164 | 0.2445 | 1.4476 |  |
| Site: UCSD (vs UAB) | +0.2347 | 0.2675 | ±0.5350 | +0.877 | 0.3803 | 1.2646 |  |
| Site: UW (vs UAB) | +0.0634 | 0.2427 | ±0.4853 | +0.261 | 0.7938 | 1.0655 |  |
| **Age (years)** | **-0.0259** | 0.0103 | ±0.0206 | **-2.514** | **0.0119** | 0.9744 | * |
| **BMI (kg/m2)** | **+0.0452** | 0.0129 | ±0.0257 | **+3.514** | **4.41e-04** | 1.0462 | *** |
| Hypertension | -0.0635 | 0.2271 | ±0.4542 | -0.279 | 0.7799 | 0.9385 |  |
| High cholesterol | +0.2237 | 0.2136 | ±0.4272 | +1.048 | 0.2948 | 1.2507 |  |
| **Kidney disease** | **+0.6318** | 0.3121 | ±0.6242 | **+2.024** | **0.0429** | 1.8810 | * |
| Circulatory disease | +0.3622 | 0.2510 | ±0.5020 | +1.443 | 0.1490 | 1.4365 |  |
| MAG (mg/dL/h) | +0.0080 | 0.0104 | ±0.0208 | +0.766 | 0.4439 | 1.0080 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0775**, LLR χ² = **51.39** (p = **3.51e-07**), AUC = **0.6953**, AIC = **635.9**, BIC = **689.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.0040** | 0.8347 | ±1.6695 | **-2.401** | **0.0164** | 0.1348 | * |
| Education: graduate level (vs college) | -0.3470 | 0.2349 | ±0.4699 | -1.477 | 0.1397 | 0.7068 |  |
| Education: high school or below (vs college) | +0.2675 | 0.3232 | ±0.6464 | +0.828 | 0.4078 | 1.3067 |  |
| Site: UCSD (vs UAB) | +0.2305 | 0.2690 | ±0.5381 | +0.857 | 0.3916 | 1.2592 |  |
| Site: UW (vs UAB) | +0.0856 | 0.2428 | ±0.4856 | +0.352 | 0.7246 | 1.0893 |  |
| **Age (years)** | **-0.0285** | 0.0104 | ±0.0209 | **-2.731** | **0.0063** | 0.9719 | ** |
| **BMI (kg/m2)** | **+0.0471** | 0.0129 | ±0.0258 | **+3.646** | **2.67e-04** | 1.0482 | *** |
| Hypertension | -0.1159 | 0.2305 | ±0.4610 | -0.503 | 0.6151 | 0.8906 |  |
| High cholesterol | +0.2194 | 0.2146 | ±0.4292 | +1.023 | 0.3065 | 1.2454 |  |
| Kidney disease | +0.4763 | 0.3222 | ±0.6444 | +1.479 | 0.1393 | 1.6102 |  |
| Circulatory disease | +0.3703 | 0.2522 | ±0.5044 | +1.468 | 0.1421 | 1.4482 |  |
| **Avg. daily range (mg/dL)** | **+0.0061** | 0.0025 | ±0.0051 | **+2.416** | **0.0157** | 1.0062 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0902**, LLR χ² = **59.82** (p = **1.00e-08**), AUC = **0.7045**, AIC = **627.4**, BIC = **680.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-1.7353** | 0.8074 | ±1.6149 | **-2.149** | **0.0316** | 0.1764 | * |
| Education: graduate level (vs college) | -0.3599 | 0.2366 | ±0.4731 | -1.521 | 0.1282 | 0.6977 |  |
| Education: high school or below (vs college) | +0.3564 | 0.3214 | ±0.6428 | +1.109 | 0.2675 | 1.4282 |  |
| Site: UCSD (vs UAB) | +0.2446 | 0.2726 | ±0.5453 | +0.897 | 0.3696 | 1.2771 |  |
| Site: UW (vs UAB) | +0.1063 | 0.2441 | ±0.4881 | +0.435 | 0.6632 | 1.1121 |  |
| **Age (years)** | **-0.0280** | 0.0104 | ±0.0208 | **-2.692** | **0.0071** | 0.9724 | ** |
| **BMI (kg/m2)** | **+0.0449** | 0.0130 | ±0.0260 | **+3.458** | **5.44e-04** | 1.0459 | *** |
| Hypertension | -0.1741 | 0.2328 | ±0.4656 | -0.748 | 0.4546 | 0.8402 |  |
| High cholesterol | +0.2217 | 0.2168 | ±0.4337 | +1.022 | 0.3066 | 1.2482 |  |
| Kidney disease | +0.4980 | 0.3220 | ±0.6439 | +1.547 | 0.1219 | 1.6454 |  |
| Circulatory disease | +0.3417 | 0.2560 | ±0.5121 | +1.334 | 0.1820 | 1.4073 |  |
| **SD of daily means (mg/dL)** | **+0.0513** | 0.0140 | ±0.0279 | **+3.670** | **2.43e-04** | 1.0526 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0893**, LLR χ² = **59.23** (p = **1.29e-08**), AUC = **0.7047**, AIC = **628.0**, BIC = **681.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0427 | 1.0564 | ±2.1128 | +0.987 | 0.3236 | 2.8370 |  |
| Education: graduate level (vs college) | -0.3356 | 0.2369 | ±0.4738 | -1.417 | 0.1565 | 0.7149 |  |
| Education: high school or below (vs college) | +0.3063 | 0.3224 | ±0.6447 | +0.950 | 0.3420 | 1.3584 |  |
| Site: UCSD (vs UAB) | +0.2625 | 0.2727 | ±0.5453 | +0.963 | 0.3357 | 1.3001 |  |
| Site: UW (vs UAB) | +0.1380 | 0.2451 | ±0.4903 | +0.563 | 0.5735 | 1.1480 |  |
| **Age (years)** | **-0.0273** | 0.0104 | ±0.0208 | **-2.622** | **0.0087** | 0.9731 | ** |
| **BMI (kg/m2)** | **+0.0457** | 0.0130 | ±0.0260 | **+3.522** | **4.28e-04** | 1.0468 | *** |
| Hypertension | -0.1452 | 0.2320 | ±0.4640 | -0.626 | 0.5315 | 0.8649 |  |
| High cholesterol | +0.1927 | 0.2168 | ±0.4335 | +0.889 | 0.3741 | 1.2125 |  |
| Kidney disease | +0.4662 | 0.3214 | ±0.6428 | +1.451 | 0.1469 | 1.5939 |  |
| Circulatory disease | +0.3508 | 0.2555 | ±0.5110 | +1.373 | 0.1697 | 1.4202 |  |
| **Time in range 70-180, pooled (%)** | **-0.0262** | 0.0072 | ±0.0144 | **-3.648** | **2.65e-04** | 0.9742 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0894**, LLR χ² = **59.30** (p = **1.25e-08**), AUC = **0.7050**, AIC = **627.9**, BIC = **681.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0483 | 1.0545 | ±2.1090 | +0.994 | 0.3202 | 2.8528 |  |
| Education: graduate level (vs college) | -0.3338 | 0.2369 | ±0.4739 | -1.409 | 0.1589 | 0.7162 |  |
| Education: high school or below (vs college) | +0.3015 | 0.3226 | ±0.6453 | +0.934 | 0.3501 | 1.3518 |  |
| Site: UCSD (vs UAB) | +0.2614 | 0.2728 | ±0.5455 | +0.958 | 0.3379 | 1.2988 |  |
| Site: UW (vs UAB) | +0.1402 | 0.2452 | ±0.4904 | +0.572 | 0.5675 | 1.1505 |  |
| **Age (years)** | **-0.0274** | 0.0104 | ±0.0208 | **-2.636** | **0.0084** | 0.9730 | ** |
| **BMI (kg/m2)** | **+0.0457** | 0.0130 | ±0.0260 | **+3.525** | **4.23e-04** | 1.0468 | *** |
| Hypertension | -0.1425 | 0.2320 | ±0.4640 | -0.614 | 0.5391 | 0.8672 |  |
| High cholesterol | +0.1909 | 0.2168 | ±0.4336 | +0.880 | 0.3787 | 1.2103 |  |
| Kidney disease | +0.4607 | 0.3220 | ±0.6440 | +1.431 | 0.1524 | 1.5853 |  |
| Circulatory disease | +0.3524 | 0.2555 | ±0.5109 | +1.379 | 0.1678 | 1.4224 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0260** | 0.0071 | ±0.0142 | **-3.665** | **2.47e-04** | 0.9743 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0700**, LLR χ² = **46.41** (p = **2.74e-06**), AUC = **0.6867**, AIC = **640.8**, BIC = **694.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3734 | 0.7981 | ±1.5961 | -1.721 | 0.0853 | 0.2532 | . |
| Education: graduate level (vs college) | -0.3640 | 0.2333 | ±0.4665 | -1.560 | 0.1186 | 0.6949 |  |
| Education: high school or below (vs college) | +0.3855 | 0.3153 | ±0.6305 | +1.223 | 0.2215 | 1.4703 |  |
| Site: UCSD (vs UAB) | +0.2044 | 0.2703 | ±0.5406 | +0.756 | 0.4496 | 1.2268 |  |
| Site: UW (vs UAB) | +0.0096 | 0.2426 | ±0.4852 | +0.040 | 0.9683 | 1.0097 |  |
| **Age (years)** | **-0.0258** | 0.0103 | ±0.0206 | **-2.506** | **0.0122** | 0.9746 | * |
| **BMI (kg/m2)** | **+0.0460** | 0.0129 | ±0.0257 | **+3.574** | **3.51e-04** | 1.0471 | *** |
| Hypertension | -0.0618 | 0.2266 | ±0.4532 | -0.273 | 0.7850 | 0.9401 |  |
| High cholesterol | +0.2014 | 0.2136 | ±0.4273 | +0.943 | 0.3459 | 1.2231 |  |
| **Kidney disease** | **+0.6398** | 0.3122 | ±0.6244 | **+2.050** | **0.0404** | 1.8962 | * |
| Circulatory disease | +0.3626 | 0.2511 | ±0.5021 | +1.444 | 0.1487 | 1.4371 |  |
| Time < 54 (%) | -0.1386 | 0.1653 | ±0.3305 | -0.839 | 0.4016 | 0.8706 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0693**, LLR χ² = **45.98** (p = **3.26e-06**), AUC = **0.6863**, AIC = **641.3**, BIC = **694.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4238 | 0.7950 | ±1.5900 | -1.791 | 0.0733 | 0.2408 | . |
| Education: graduate level (vs college) | -0.3698 | 0.2334 | ±0.4667 | -1.585 | 0.1130 | 0.6908 |  |
| Education: high school or below (vs college) | +0.3911 | 0.3151 | ±0.6301 | +1.241 | 0.2144 | 1.4787 |  |
| Site: UCSD (vs UAB) | +0.2224 | 0.2691 | ±0.5382 | +0.826 | 0.4086 | 1.2490 |  |
| Site: UW (vs UAB) | +0.0183 | 0.2429 | ±0.4858 | +0.076 | 0.9398 | 1.0185 |  |
| **Age (years)** | **-0.0255** | 0.0103 | ±0.0206 | **-2.474** | **0.0134** | 0.9748 | * |
| **BMI (kg/m2)** | **+0.0458** | 0.0129 | ±0.0257 | **+3.563** | **3.66e-04** | 1.0469 | *** |
| Hypertension | -0.0592 | 0.2264 | ±0.4528 | -0.262 | 0.7936 | 0.9425 |  |
| High cholesterol | +0.2061 | 0.2135 | ±0.4271 | +0.965 | 0.3346 | 1.2288 |  |
| **Kidney disease** | **+0.6434** | 0.3119 | ±0.6238 | **+2.063** | **0.0391** | 1.9030 | * |
| Circulatory disease | +0.3628 | 0.2510 | ±0.5020 | +1.445 | 0.1483 | 1.4374 |  |
| Avg. daily time < 54 (%) | -0.0980 | 0.1665 | ±0.3330 | -0.589 | 0.5560 | 0.9066 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0688**, LLR χ² = **45.62** (p = **3.77e-06**), AUC = **0.6870**, AIC = **641.6**, BIC = **695.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4527 | 0.7962 | ±1.5923 | -1.825 | 0.0681 | 0.2339 | . |
| Education: graduate level (vs college) | -0.3631 | 0.2339 | ±0.4678 | -1.552 | 0.1206 | 0.6955 |  |
| Education: high school or below (vs college) | +0.4020 | 0.3147 | ±0.6293 | +1.278 | 0.2014 | 1.4949 |  |
| Site: UCSD (vs UAB) | +0.2481 | 0.2682 | ±0.5364 | +0.925 | 0.3549 | 1.2816 |  |
| Site: UW (vs UAB) | +0.0444 | 0.2416 | ±0.4832 | +0.184 | 0.8541 | 1.0454 |  |
| **Age (years)** | **-0.0260** | 0.0103 | ±0.0206 | **-2.518** | **0.0118** | 0.9744 | * |
| **BMI (kg/m2)** | **+0.0456** | 0.0128 | ±0.0257 | **+3.555** | **3.78e-04** | 1.0467 | *** |
| Hypertension | -0.0503 | 0.2267 | ±0.4533 | -0.222 | 0.8244 | 0.9509 |  |
| High cholesterol | +0.2167 | 0.2131 | ±0.4262 | +1.017 | 0.3092 | 1.2420 |  |
| **Kidney disease** | **+0.6384** | 0.3116 | ±0.6232 | **+2.049** | **0.0405** | 1.8935 | * |
| Circulatory disease | +0.3629 | 0.2510 | ±0.5020 | +1.446 | 0.1482 | 1.4375 |  |
| Time 54-69, pooled (%) | +0.0077 | 0.0436 | ±0.0871 | +0.177 | 0.8594 | 1.0077 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0688**, LLR χ² = **45.65** (p = **3.72e-06**), AUC = **0.6870**, AIC = **641.6**, BIC = **695.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4520 | 0.7952 | ±1.5904 | -1.826 | 0.0679 | 0.2341 | . |
| Education: graduate level (vs college) | -0.3616 | 0.2340 | ±0.4681 | -1.545 | 0.1223 | 0.6965 |  |
| Education: high school or below (vs college) | +0.4021 | 0.3147 | ±0.6294 | +1.278 | 0.2013 | 1.4949 |  |
| Site: UCSD (vs UAB) | +0.2488 | 0.2679 | ±0.5358 | +0.929 | 0.3529 | 1.2825 |  |
| Site: UW (vs UAB) | +0.0462 | 0.2418 | ±0.4835 | +0.191 | 0.8484 | 1.0473 |  |
| **Age (years)** | **-0.0261** | 0.0103 | ±0.0207 | **-2.524** | **0.0116** | 0.9743 | * |
| **BMI (kg/m2)** | **+0.0456** | 0.0128 | ±0.0257 | **+3.553** | **3.80e-04** | 1.0466 | *** |
| Hypertension | -0.0496 | 0.2266 | ±0.4532 | -0.219 | 0.8266 | 0.9516 |  |
| High cholesterol | +0.2170 | 0.2131 | ±0.4263 | +1.018 | 0.3085 | 1.2424 |  |
| **Kidney disease** | **+0.6382** | 0.3116 | ±0.6231 | **+2.048** | **0.0405** | 1.8930 | * |
| Circulatory disease | +0.3637 | 0.2510 | ±0.5020 | +1.449 | 0.1474 | 1.4386 |  |
| Avg. daily time 54-69 (%) | +0.0103 | 0.0418 | ±0.0835 | +0.246 | 0.8057 | 1.0103 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0688**, LLR χ² = **45.60** (p = **3.80e-06**), AUC = **0.6866**, AIC = **641.6**, BIC = **695.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4383 | 0.7969 | ±1.5938 | -1.805 | 0.0711 | 0.2373 | . |
| Education: graduate level (vs college) | -0.3666 | 0.2337 | ±0.4673 | -1.569 | 0.1166 | 0.6931 |  |
| Education: high school or below (vs college) | +0.4012 | 0.3147 | ±0.6294 | +1.275 | 0.2024 | 1.4936 |  |
| Site: UCSD (vs UAB) | +0.2411 | 0.2689 | ±0.5379 | +0.896 | 0.3700 | 1.2726 |  |
| Site: UW (vs UAB) | +0.0382 | 0.2421 | ±0.4841 | +0.158 | 0.8746 | 1.0389 |  |
| **Age (years)** | **-0.0258** | 0.0103 | ±0.0206 | **-2.503** | **0.0123** | 0.9745 | * |
| **BMI (kg/m2)** | **+0.0456** | 0.0128 | ±0.0257 | **+3.557** | **3.74e-04** | 1.0467 | *** |
| Hypertension | -0.0543 | 0.2267 | ±0.4533 | -0.239 | 0.8108 | 0.9472 |  |
| High cholesterol | +0.2152 | 0.2132 | ±0.4264 | +1.009 | 0.3128 | 1.2401 |  |
| **Kidney disease** | **+0.6408** | 0.3116 | ±0.6232 | **+2.056** | **0.0398** | 1.8979 | * |
| Circulatory disease | +0.3606 | 0.2510 | ±0.5020 | +1.437 | 0.1508 | 1.4342 |  |
| Time < 70 (%) | -0.0031 | 0.0366 | ±0.0731 | -0.086 | 0.9316 | 0.9969 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0687**, LLR χ² = **45.60** (p = **3.81e-06**), AUC = **0.6869**, AIC = **641.6**, BIC = **695.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4458 | 0.7953 | ±1.5906 | -1.818 | 0.0691 | 0.2356 | . |
| Education: graduate level (vs college) | -0.3647 | 0.2339 | ±0.4678 | -1.559 | 0.1189 | 0.6944 |  |
| Education: high school or below (vs college) | +0.4020 | 0.3147 | ±0.6294 | +1.278 | 0.2014 | 1.4949 |  |
| Site: UCSD (vs UAB) | +0.2453 | 0.2683 | ±0.5366 | +0.914 | 0.3606 | 1.2780 |  |
| Site: UW (vs UAB) | +0.0422 | 0.2422 | ±0.4844 | +0.174 | 0.8617 | 1.0431 |  |
| **Age (years)** | **-0.0259** | 0.0103 | ±0.0207 | **-2.509** | **0.0121** | 0.9744 | * |
| **BMI (kg/m2)** | **+0.0456** | 0.0128 | ±0.0257 | **+3.556** | **3.77e-04** | 1.0467 | *** |
| Hypertension | -0.0522 | 0.2266 | ±0.4531 | -0.230 | 0.8179 | 0.9492 |  |
| High cholesterol | +0.2163 | 0.2132 | ±0.4264 | +1.015 | 0.3103 | 1.2415 |  |
| **Kidney disease** | **+0.6396** | 0.3116 | ±0.6232 | **+2.053** | **0.0401** | 1.8958 | * |
| Circulatory disease | +0.3617 | 0.2509 | ±0.5019 | +1.441 | 0.1495 | 1.4357 |  |
| Avg. daily time < 70 (%) | +0.0020 | 0.0351 | ±0.0702 | +0.058 | 0.9538 | 1.0020 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0915**, LLR χ² = **60.66** (p = **6.98e-09**), AUC = **0.6989**, AIC = **626.6**, BIC = **680.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.3229** | 2.4242 | ±4.8483 | **+2.196** | **0.0281** | 204.9791 | * |
| Education: graduate level (vs college) | -0.3362 | 0.2360 | ±0.4721 | -1.424 | 0.1544 | 0.7145 |  |
| Education: high school or below (vs college) | +0.2874 | 0.3281 | ±0.6563 | +0.876 | 0.3811 | 1.3329 |  |
| Site: UCSD (vs UAB) | +0.2774 | 0.2729 | ±0.5457 | +1.016 | 0.3094 | 1.3197 |  |
| Site: UW (vs UAB) | +0.1432 | 0.2450 | ±0.4900 | +0.584 | 0.5589 | 1.1540 |  |
| **Age (years)** | **-0.0259** | 0.0104 | ±0.0208 | **-2.486** | **0.0129** | 0.9744 | * |
| **BMI (kg/m2)** | **+0.0469** | 0.0130 | ±0.0259 | **+3.618** | **2.97e-04** | 1.0480 | *** |
| Hypertension | -0.1338 | 0.2316 | ±0.4632 | -0.578 | 0.5636 | 0.8748 |  |
| High cholesterol | +0.2499 | 0.2174 | ±0.4348 | +1.149 | 0.2504 | 1.2839 |  |
| Kidney disease | +0.5358 | 0.3198 | ±0.6395 | +1.676 | 0.0938 | 1.7088 | . |
| Circulatory disease | +0.3436 | 0.2565 | ±0.5129 | +1.340 | 0.1803 | 1.4101 |  |
| **Time 54-250, pooled (%)** | **-0.0694** | 0.0231 | ±0.0461 | **-3.008** | **0.0026** | 0.9330 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0918**, LLR χ² = **60.90** (p = **6.29e-09**), AUC = **0.6981**, AIC = **626.3**, BIC = **679.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.9995** | 2.5497 | ±5.0995 | **+2.353** | **0.0186** | 403.2113 | * |
| Education: graduate level (vs college) | -0.3296 | 0.2360 | ±0.4720 | -1.397 | 0.1625 | 0.7192 |  |
| Education: high school or below (vs college) | +0.2677 | 0.3299 | ±0.6599 | +0.811 | 0.4171 | 1.3070 |  |
| Site: UCSD (vs UAB) | +0.2711 | 0.2734 | ±0.5468 | +0.992 | 0.3214 | 1.3114 |  |
| Site: UW (vs UAB) | +0.1411 | 0.2449 | ±0.4898 | +0.576 | 0.5645 | 1.1515 |  |
| **Age (years)** | **-0.0264** | 0.0104 | ±0.0208 | **-2.530** | **0.0114** | 0.9740 | * |
| **BMI (kg/m2)** | **+0.0471** | 0.0130 | ±0.0259 | **+3.635** | **2.78e-04** | 1.0483 | *** |
| Hypertension | -0.1353 | 0.2318 | ±0.4636 | -0.584 | 0.5594 | 0.8735 |  |
| High cholesterol | +0.2462 | 0.2175 | ±0.4351 | +1.132 | 0.2578 | 1.2791 |  |
| Kidney disease | +0.5173 | 0.3210 | ±0.6420 | +1.611 | 0.1071 | 1.6774 |  |
| Circulatory disease | +0.3430 | 0.2568 | ±0.5136 | +1.336 | 0.1816 | 1.4092 |  |
| **Avg. daily time 54-250 (%)** | **-0.0758** | 0.0243 | ±0.0486 | **-3.119** | **0.0018** | 0.9270 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0802**, LLR χ² = **53.20** (p = **1.65e-07**), AUC = **0.6993**, AIC = **634.0**, BIC = **687.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4633 | 0.7999 | ±1.5998 | -1.829 | 0.0673 | 0.2315 | . |
| Education: graduate level (vs college) | -0.3578 | 0.2353 | ±0.4707 | -1.520 | 0.1284 | 0.6992 |  |
| Education: high school or below (vs college) | +0.3423 | 0.3176 | ±0.6353 | +1.078 | 0.2811 | 1.4082 |  |
| Site: UCSD (vs UAB) | +0.2291 | 0.2704 | ±0.5409 | +0.847 | 0.3969 | 1.2575 |  |
| Site: UW (vs UAB) | +0.0827 | 0.2426 | ±0.4852 | +0.341 | 0.7330 | 1.0863 |  |
| **Age (years)** | **-0.0270** | 0.0103 | ±0.0207 | **-2.609** | **0.0091** | 0.9734 | ** |
| **BMI (kg/m2)** | **+0.0451** | 0.0129 | ±0.0258 | **+3.488** | **4.87e-04** | 1.0461 | *** |
| Hypertension | -0.1250 | 0.2303 | ±0.4605 | -0.543 | 0.5872 | 0.8825 |  |
| High cholesterol | +0.1682 | 0.2158 | ±0.4315 | +0.779 | 0.4357 | 1.1831 |  |
| Kidney disease | +0.4969 | 0.3197 | ±0.6394 | +1.554 | 0.1201 | 1.6436 |  |
| Circulatory disease | +0.3555 | 0.2537 | ±0.5074 | +1.401 | 0.1611 | 1.4269 |  |
| **Time 181-250, pooled (%)** | **+0.0286** | 0.0103 | ±0.0205 | **+2.787** | **0.0053** | 1.0290 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0815**, LLR χ² = **54.07** (p = **1.15e-07**), AUC = **0.7008**, AIC = **633.2**, BIC = **686.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4769 | 0.8009 | ±1.6018 | -1.844 | 0.0652 | 0.2284 | . |
| Education: graduate level (vs college) | -0.3584 | 0.2356 | ±0.4712 | -1.521 | 0.1282 | 0.6988 |  |
| Education: high school or below (vs college) | +0.3386 | 0.3179 | ±0.6359 | +1.065 | 0.2868 | 1.4031 |  |
| Site: UCSD (vs UAB) | +0.2355 | 0.2707 | ±0.5415 | +0.870 | 0.3843 | 1.2656 |  |
| Site: UW (vs UAB) | +0.0913 | 0.2430 | ±0.4859 | +0.376 | 0.7072 | 1.0955 |  |
| **Age (years)** | **-0.0268** | 0.0103 | ±0.0207 | **-2.596** | **0.0094** | 0.9735 | ** |
| **BMI (kg/m2)** | **+0.0450** | 0.0129 | ±0.0259 | **+3.483** | **4.95e-04** | 1.0461 | *** |
| Hypertension | -0.1262 | 0.2304 | ±0.4608 | -0.548 | 0.5838 | 0.8814 |  |
| High cholesterol | +0.1673 | 0.2159 | ±0.4318 | +0.775 | 0.4384 | 1.1821 |  |
| Kidney disease | +0.4904 | 0.3202 | ±0.6403 | +1.532 | 0.1256 | 1.6330 |  |
| Circulatory disease | +0.3584 | 0.2539 | ±0.5078 | +1.412 | 0.1580 | 1.4311 |  |
| **Avg. daily time 181-250 (%)** | **+0.0292** | 0.0099 | ±0.0198 | **+2.942** | **0.0033** | 1.0296 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0893**, LLR χ² = **59.22** (p = **1.29e-08**), AUC = **0.7019**, AIC = **628.0**, BIC = **681.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5262 | 0.8057 | ±1.6115 | -1.894 | 0.0582 | 0.2174 | . |
| Education: graduate level (vs college) | -0.3441 | 0.2365 | ±0.4731 | -1.455 | 0.1458 | 0.7089 |  |
| Education: high school or below (vs college) | +0.3021 | 0.3227 | ±0.6453 | +0.936 | 0.3491 | 1.3527 |  |
| Site: UCSD (vs UAB) | +0.2381 | 0.2727 | ±0.5454 | +0.873 | 0.3826 | 1.2688 |  |
| Site: UW (vs UAB) | +0.1168 | 0.2443 | ±0.4886 | +0.478 | 0.6326 | 1.1239 |  |
| **Age (years)** | **-0.0268** | 0.0104 | ±0.0208 | **-2.582** | **0.0098** | 0.9736 | ** |
| **BMI (kg/m2)** | **+0.0458** | 0.0130 | ±0.0260 | **+3.528** | **4.18e-04** | 1.0469 | *** |
| Hypertension | -0.1563 | 0.2325 | ±0.4649 | -0.672 | 0.5013 | 0.8553 |  |
| High cholesterol | +0.1864 | 0.2167 | ±0.4335 | +0.860 | 0.3899 | 1.2048 |  |
| Kidney disease | +0.4737 | 0.3213 | ±0.6426 | +1.474 | 0.1404 | 1.6059 |  |
| Circulatory disease | +0.3454 | 0.2558 | ±0.5115 | +1.350 | 0.1769 | 1.4125 |  |
| **Time > 180 (%)** | **+0.0260** | 0.0071 | ±0.0143 | **+3.646** | **2.66e-04** | 1.0264 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0894**, LLR χ² = **59.27** (p = **1.27e-08**), AUC = **0.7028**, AIC = **628.0**, BIC = **681.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5253 | 0.8058 | ±1.6117 | -1.893 | 0.0584 | 0.2175 | . |
| Education: graduate level (vs college) | -0.3455 | 0.2366 | ±0.4732 | -1.460 | 0.1442 | 0.7079 |  |
| Education: high school or below (vs college) | +0.2966 | 0.3230 | ±0.6459 | +0.918 | 0.3584 | 1.3453 |  |
| Site: UCSD (vs UAB) | +0.2410 | 0.2728 | ±0.5456 | +0.883 | 0.3770 | 1.2725 |  |
| Site: UW (vs UAB) | +0.1180 | 0.2443 | ±0.4886 | +0.483 | 0.6291 | 1.1252 |  |
| **Age (years)** | **-0.0268** | 0.0104 | ±0.0208 | **-2.583** | **0.0098** | 0.9735 | ** |
| **BMI (kg/m2)** | **+0.0459** | 0.0130 | ±0.0260 | **+3.534** | **4.10e-04** | 1.0469 | *** |
| Hypertension | -0.1529 | 0.2323 | ±0.4646 | -0.658 | 0.5104 | 0.8582 |  |
| High cholesterol | +0.1840 | 0.2168 | ±0.4335 | +0.849 | 0.3959 | 1.2020 |  |
| Kidney disease | +0.4666 | 0.3220 | ±0.6440 | +1.449 | 0.1473 | 1.5946 |  |
| Circulatory disease | +0.3464 | 0.2558 | ±0.5116 | +1.354 | 0.1757 | 1.4140 |  |
| **Avg. daily time > 180 (%)** | **+0.0261** | 0.0071 | ±0.0142 | **+3.661** | **2.51e-04** | 1.0264 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.1027**, LLR χ² = **68.09** (p = **2.81e-10**), AUC = **0.7167**, AIC = **619.2**, BIC = **672.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5435 | 0.8113 | ±1.6227 | -1.902 | 0.0571 | 0.2136 | . |
| Education: graduate level (vs college) | -0.3199 | 0.2381 | ±0.4762 | -1.344 | 0.1791 | 0.7262 |  |
| Education: high school or below (vs college) | +0.3213 | 0.3243 | ±0.6485 | +0.991 | 0.3218 | 1.3789 |  |
| Site: UCSD (vs UAB) | +0.2731 | 0.2759 | ±0.5518 | +0.990 | 0.3222 | 1.3141 |  |
| Site: UW (vs UAB) | +0.1294 | 0.2463 | ±0.4926 | +0.525 | 0.5995 | 1.1381 |  |
| **Age (years)** | **-0.0261** | 0.0105 | ±0.0209 | **-2.496** | **0.0126** | 0.9742 | * |
| **BMI (kg/m2)** | **+0.0450** | 0.0131 | ±0.0261 | **+3.444** | **5.74e-04** | 1.0460 | *** |
| Hypertension | -0.1856 | 0.2349 | ±0.4698 | -0.790 | 0.4295 | 0.8306 |  |
| High cholesterol | +0.1731 | 0.2196 | ±0.4391 | +0.788 | 0.4306 | 1.1889 |  |
| Kidney disease | +0.5676 | 0.3208 | ±0.6417 | +1.769 | 0.0769 | 1.7641 | . |
| Circulatory disease | +0.3449 | 0.2599 | ±0.5197 | +1.327 | 0.1845 | 1.4118 |  |
| **Nocturnal time > 180 (%)** | **+0.0352** | 0.0080 | ±0.0160 | **+4.414** | **1.02e-05** | 1.0359 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0810**, LLR χ² = **53.75** (p = **1.31e-07**), AUC = **0.6965**, AIC = **633.5**, BIC = **687.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4927 | 0.8030 | ±1.6060 | -1.859 | 0.0630 | 0.2248 | . |
| Education: graduate level (vs college) | -0.3364 | 0.2355 | ±0.4711 | -1.428 | 0.1533 | 0.7143 |  |
| Education: high school or below (vs college) | +0.3420 | 0.3178 | ±0.6357 | +1.076 | 0.2820 | 1.4077 |  |
| Site: UCSD (vs UAB) | +0.2142 | 0.2694 | ±0.5387 | +0.795 | 0.4264 | 1.2389 |  |
| Site: UW (vs UAB) | +0.0600 | 0.2424 | ±0.4848 | +0.248 | 0.8045 | 1.0619 |  |
| **Age (years)** | **-0.0288** | 0.0105 | ±0.0209 | **-2.753** | **0.0059** | 0.9716 | ** |
| **BMI (kg/m2)** | **+0.0480** | 0.0129 | ±0.0259 | **+3.706** | **2.10e-04** | 1.0491 | *** |
| Hypertension | -0.1379 | 0.2315 | ±0.4631 | -0.595 | 0.5516 | 0.8712 |  |
| High cholesterol | +0.2061 | 0.2154 | ±0.4307 | +0.957 | 0.3387 | 1.2288 |  |
| Kidney disease | +0.4892 | 0.3200 | ±0.6401 | +1.529 | 0.1263 | 1.6311 |  |
| Circulatory disease | +0.3716 | 0.2535 | ±0.5070 | +1.466 | 0.1427 | 1.4500 |  |
| **Any reading > 250 during wear (0/1)** | **+0.6383** | 0.2216 | ±0.4431 | **+2.881** | **0.0040** | 1.8932 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0935**, LLR χ² = **62.00** (p = **3.94e-09**), AUC = **0.7009**, AIC = **625.2**, BIC = **678.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5709 | 0.8078 | ±1.6155 | -1.945 | 0.0518 | 0.2079 | . |
| Education: graduate level (vs college) | -0.3346 | 0.2361 | ±0.4722 | -1.417 | 0.1565 | 0.7156 |  |
| Education: high school or below (vs college) | +0.2675 | 0.3300 | ±0.6601 | +0.810 | 0.4177 | 1.3067 |  |
| Site: UCSD (vs UAB) | +0.2531 | 0.2733 | ±0.5467 | +0.926 | 0.3544 | 1.2881 |  |
| Site: UW (vs UAB) | +0.1288 | 0.2445 | ±0.4891 | +0.527 | 0.5984 | 1.1375 |  |
| **Age (years)** | **-0.0258** | 0.0104 | ±0.0208 | **-2.482** | **0.0131** | 0.9745 | * |
| **BMI (kg/m2)** | **+0.0469** | 0.0130 | ±0.0260 | **+3.612** | **3.04e-04** | 1.0480 | *** |
| Hypertension | -0.1459 | 0.2322 | ±0.4645 | -0.628 | 0.5299 | 0.8643 |  |
| High cholesterol | +0.2409 | 0.2177 | ±0.4354 | +1.106 | 0.2686 | 1.2723 |  |
| Kidney disease | +0.5250 | 0.3212 | ±0.6424 | +1.634 | 0.1022 | 1.6904 |  |
| Circulatory disease | +0.3464 | 0.2571 | ±0.5142 | +1.347 | 0.1779 | 1.4139 |  |
| **Time > 250 (%)** | **+0.0759** | 0.0250 | ±0.0500 | **+3.039** | **0.0024** | 1.0789 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 637)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **637**, events = **137**, McFadden pseudo-R² = **0.0939**, LLR χ² = **62.26** (p = **3.52e-09**), AUC = **0.7011**, AIC = **625.0**, BIC = **678.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5575 | 0.8079 | ±1.6159 | -1.928 | 0.0539 | 0.2107 | . |
| Education: graduate level (vs college) | -0.3322 | 0.2360 | ±0.4721 | -1.407 | 0.1593 | 0.7174 |  |
| Education: high school or below (vs college) | +0.2453 | 0.3321 | ±0.6642 | +0.739 | 0.4602 | 1.2779 |  |
| Site: UCSD (vs UAB) | +0.2525 | 0.2739 | ±0.5478 | +0.922 | 0.3566 | 1.2873 |  |
| Site: UW (vs UAB) | +0.1263 | 0.2445 | ±0.4890 | +0.517 | 0.6053 | 1.1347 |  |
| **Age (years)** | **-0.0262** | 0.0104 | ±0.0209 | **-2.510** | **0.0121** | 0.9742 | * |
| **BMI (kg/m2)** | **+0.0472** | 0.0130 | ±0.0260 | **+3.630** | **2.83e-04** | 1.0483 | *** |
| Hypertension | -0.1469 | 0.2323 | ±0.4646 | -0.633 | 0.5270 | 0.8634 |  |
| High cholesterol | +0.2369 | 0.2178 | ±0.4357 | +1.088 | 0.2768 | 1.2673 |  |
| Kidney disease | +0.5056 | 0.3225 | ±0.6451 | +1.568 | 0.1170 | 1.6580 |  |
| Circulatory disease | +0.3475 | 0.2575 | ±0.5151 | +1.349 | 0.1772 | 1.4156 |  |
| **Avg. daily time > 250 (%)** | **+0.0836** | 0.0263 | ±0.0527 | **+3.176** | **0.0015** | 1.0872 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


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


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 575; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **575**, R² = **0.1606**, Adj R² = **0.1457**, F-statistic = **10.79** (p = **7.14e-17**), Residual SE = **4142.120** on **564** df, AIC = **11221.0**, BIC = **11268.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20170.2242** | 1377.2456 | ±2754.4912 | **+14.645** | **1.44e-48** | *** |
| Education: graduate level (vs college) | -654.3042 | 389.1310 | ±778.2619 | -1.681 | 0.0927 | . |
| Education: high school or below (vs college) | +787.5540 | 705.0046 | ±1410.0093 | +1.117 | 0.2640 |  |
| Site: UCSD (vs UAB) | +220.4969 | 464.3232 | ±928.6463 | +0.475 | 0.6349 |  |
| Site: UW (vs UAB) | +240.8803 | 407.2541 | ±814.5082 | +0.591 | 0.5542 |  |
| **Age (years)** | **-146.5494** | 16.0585 | ±32.1170 | **-9.126** | **7.11e-20** | *** |
| BMI (kg/m2) | -42.8297 | 27.4461 | ±54.8923 | -1.560 | 0.1186 |  |
| Hypertension | -326.6177 | 400.6722 | ±801.3444 | -0.815 | 0.4150 |  |
| High cholesterol | -82.5906 | 363.2356 | ±726.4711 | -0.227 | 0.8201 |  |
| Kidney disease | -869.0912 | 716.8445 | ±1433.6890 | -1.212 | 0.2254 |  |
| Circulatory disease | -574.3306 | 450.8863 | ±901.7726 | -1.274 | 0.2027 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **575**, R² = **0.1649**, Adj R² = **0.1486**, F-statistic = **10.11** (p = **6.34e-17**), Residual SE = **4135.047** on **563** df, AIC = **11220.0**, BIC = **11272.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18371.8235** | 2086.6228 | ±4173.2456 | **+8.805** | **1.31e-18** | *** |
| Education: graduate level (vs college) | -604.6126 | 395.9142 | ±791.8284 | -1.527 | 0.1267 |  |
| Education: high school or below (vs college) | +691.3886 | 696.2810 | ±1392.5620 | +0.993 | 0.3207 |  |
| Site: UCSD (vs UAB) | +205.1773 | 464.2113 | ±928.4227 | +0.442 | 0.6585 |  |
| Site: UW (vs UAB) | +293.4581 | 410.4596 | ±820.9191 | +0.715 | 0.4746 |  |
| **Age (years)** | **-150.4708** | 16.2070 | ±32.4140 | **-9.284** | **1.63e-20** | *** |
| BMI (kg/m2) | -46.3519 | 27.2672 | ±54.5344 | -1.700 | 0.0891 | . |
| Hypertension | -385.6929 | 405.9415 | ±811.8829 | -0.950 | 0.3421 |  |
| High cholesterol | -132.6662 | 371.2113 | ±742.4227 | -0.357 | 0.7208 |  |
| Kidney disease | -907.1914 | 706.5372 | ±1413.0745 | -1.284 | 0.1991 |  |
| Circulatory disease | -559.0604 | 451.1610 | ±902.3220 | -1.239 | 0.2153 |  |
| HbA1c (%) | +367.1900 | 297.7031 | ±595.4062 | +1.233 | 0.2174 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **575**, R² = **0.1610**, Adj R² = **0.1446**, F-statistic = **9.82** (p = **2.13e-16**), Residual SE = **4144.745** on **563** df, AIC = **11222.7**, BIC = **11274.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20587.6454** | 1700.2985 | ±3400.5969 | **+12.108** | **9.55e-34** | *** |
| Education: graduate level (vs college) | -655.2399 | 389.6653 | ±779.3306 | -1.682 | 0.0927 | . |
| Education: high school or below (vs college) | +812.5592 | 703.1289 | ±1406.2577 | +1.156 | 0.2478 |  |
| Site: UCSD (vs UAB) | +223.6956 | 464.7368 | ±929.4736 | +0.481 | 0.6303 |  |
| Site: UW (vs UAB) | +235.3552 | 408.9722 | ±817.9445 | +0.575 | 0.5650 |  |
| **Age (years)** | **-146.2583** | 16.0445 | ±32.0889 | **-9.116** | **7.81e-20** | *** |
| BMI (kg/m2) | -42.2385 | 27.4149 | ±54.8297 | -1.541 | 0.1234 |  |
| Hypertension | -302.4647 | 407.1648 | ±814.3296 | -0.743 | 0.4576 |  |
| High cholesterol | -66.0284 | 365.4438 | ±730.8875 | -0.181 | 0.8566 |  |
| Kidney disease | -831.3034 | 723.1268 | ±1446.2537 | -1.150 | 0.2503 |  |
| Circulatory disease | -569.7429 | 452.3676 | ±904.7352 | -1.259 | 0.2079 |  |
| Mean glucose (mg/dL) | -3.9150 | 7.8798 | ±15.7596 | -0.497 | 0.6193 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **575**, R² = **0.1610**, Adj R² = **0.1446**, F-statistic = **9.82** (p = **2.13e-16**), Residual SE = **4144.745** on **563** df, AIC = **11222.7**, BIC = **11274.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+21129.3929** | 2506.1907 | ±5012.3813 | **+8.431** | **3.43e-17** | *** |
| Education: graduate level (vs college) | -655.2399 | 389.6653 | ±779.3306 | -1.682 | 0.0927 | . |
| Education: high school or below (vs college) | +812.5592 | 703.1289 | ±1406.2577 | +1.156 | 0.2478 |  |
| Site: UCSD (vs UAB) | +223.6956 | 464.7368 | ±929.4736 | +0.481 | 0.6303 |  |
| Site: UW (vs UAB) | +235.3552 | 408.9722 | ±817.9445 | +0.575 | 0.5650 |  |
| **Age (years)** | **-146.2583** | 16.0445 | ±32.0889 | **-9.116** | **7.81e-20** | *** |
| BMI (kg/m2) | -42.2385 | 27.4149 | ±54.8297 | -1.541 | 0.1234 |  |
| Hypertension | -302.4647 | 407.1648 | ±814.3296 | -0.743 | 0.4576 |  |
| High cholesterol | -66.0284 | 365.4438 | ±730.8875 | -0.181 | 0.8566 |  |
| Kidney disease | -831.3034 | 723.1268 | ±1446.2537 | -1.150 | 0.2503 |  |
| Circulatory disease | -569.7429 | 452.3676 | ±904.7352 | -1.259 | 0.2079 |  |
| GMI (%) | -163.6699 | 329.4241 | ±658.8481 | -0.497 | 0.6193 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **575**, R² = **0.1606**, Adj R² = **0.1442**, F-statistic = **9.79** (p = **2.40e-16**), Residual SE = **4145.692** on **563** df, AIC = **11223.0**, BIC = **11275.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20038.5087** | 1690.5840 | ±3381.1680 | **+11.853** | **2.08e-32** | *** |
| Education: graduate level (vs college) | -654.3046 | 389.6589 | ±779.3179 | -1.679 | 0.0931 | . |
| Education: high school or below (vs college) | +780.2746 | 704.5967 | ±1409.1935 | +1.107 | 0.2681 |  |
| Site: UCSD (vs UAB) | +218.3857 | 462.9645 | ±925.9289 | +0.472 | 0.6371 |  |
| Site: UW (vs UAB) | +241.4338 | 408.1285 | ±816.2571 | +0.592 | 0.5541 |  |
| **Age (years)** | **-146.4712** | 16.1385 | ±32.2771 | **-9.076** | **1.13e-19** | *** |
| BMI (kg/m2) | -43.2007 | 27.4743 | ±54.9487 | -1.572 | 0.1159 |  |
| Hypertension | -334.3476 | 406.8119 | ±813.6239 | -0.822 | 0.4111 |  |
| High cholesterol | -88.6842 | 367.2586 | ±734.5171 | -0.241 | 0.8092 |  |
| Kidney disease | -873.6059 | 718.2853 | ±1436.5706 | -1.216 | 0.2239 |  |
| Circulatory disease | -575.1063 | 452.1430 | ±904.2860 | -1.272 | 0.2034 |  |
| Nocturnal mean 00-06h (mg/dL) | +1.2256 | 7.7636 | ±15.5272 | +0.158 | 0.8746 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **575**, R² = **0.1634**, Adj R² = **0.1470**, F-statistic = **10.00** (p = **1.02e-16**), Residual SE = **4138.850** on **563** df, AIC = **11221.1**, BIC = **11273.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20522.8376** | 1424.5444 | ±2849.0888 | **+14.407** | **4.70e-47** | *** |
| Education: graduate level (vs college) | -674.3096 | 389.6834 | ±779.3668 | -1.730 | 0.0836 | . |
| Education: high school or below (vs college) | +895.9372 | 698.8887 | ±1397.7774 | +1.282 | 0.1999 |  |
| Site: UCSD (vs UAB) | +219.6306 | 466.6338 | ±933.2676 | +0.471 | 0.6379 |  |
| Site: UW (vs UAB) | +192.2897 | 411.3500 | ±822.7001 | +0.467 | 0.6402 |  |
| **Age (years)** | **-143.6019** | 16.0970 | ±32.1941 | **-8.921** | **4.62e-19** | *** |
| BMI (kg/m2) | -43.1722 | 27.4404 | ±54.8808 | -1.573 | 0.1156 |  |
| Hypertension | -272.4327 | 402.4590 | ±804.9179 | -0.677 | 0.4985 |  |
| High cholesterol | -63.5834 | 364.4792 | ±728.9584 | -0.174 | 0.8615 |  |
| Kidney disease | -689.2949 | 727.8601 | ±1455.7203 | -0.947 | 0.3436 |  |
| Circulatory disease | -586.5855 | 451.1068 | ±902.2136 | -1.300 | 0.1935 |  |
| Glucose SD, pooled (mg/dL) | -21.1469 | 15.3109 | ±30.6217 | -1.381 | 0.1672 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **575**, R² = **0.1642**, Adj R² = **0.1479**, F-statistic = **10.06** (p = **7.91e-17**), Residual SE = **4136.812** on **563** df, AIC = **11220.5**, BIC = **11272.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20573.5472** | 1421.7965 | ±2843.5930 | **+14.470** | **1.87e-47** | *** |
| Education: graduate level (vs college) | -680.8277 | 389.8676 | ±779.7351 | -1.746 | 0.0808 | . |
| Education: high school or below (vs college) | +928.1742 | 696.7538 | ±1393.5075 | +1.332 | 0.1828 |  |
| Site: UCSD (vs UAB) | +225.8480 | 465.4551 | ±930.9102 | +0.485 | 0.6275 |  |
| Site: UW (vs UAB) | +192.9973 | 410.2140 | ±820.4280 | +0.470 | 0.6380 |  |
| **Age (years)** | **-142.8911** | 16.0387 | ±32.0774 | **-8.909** | **5.14e-19** | *** |
| BMI (kg/m2) | -43.3774 | 27.4332 | ±54.8663 | -1.581 | 0.1138 |  |
| Hypertension | -268.9828 | 402.0704 | ±804.1407 | -0.669 | 0.5035 |  |
| High cholesterol | -55.7197 | 363.8973 | ±727.7946 | -0.153 | 0.8783 |  |
| Kidney disease | -660.5795 | 728.1605 | ±1456.3211 | -0.907 | 0.3643 |  |
| Circulatory disease | -595.7289 | 449.5958 | ±899.1916 | -1.325 | 0.1852 |  |
| Avg. daily SD (mg/dL) | -27.9504 | 16.9601 | ±33.9201 | -1.648 | 0.0993 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **575**, R² = **0.1637**, Adj R² = **0.1473**, F-statistic = **10.02** (p = **9.37e-17**), Residual SE = **4138.169** on **563** df, AIC = **11220.9**, BIC = **11273.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20864.3288** | 1464.8855 | ±2929.7710 | **+14.243** | **4.96e-46** | *** |
| Education: graduate level (vs college) | -677.2330 | 389.0061 | ±778.0122 | -1.741 | 0.0817 | . |
| Education: high school or below (vs college) | +901.0721 | 700.7867 | ±1401.5734 | +1.286 | 0.1985 |  |
| Site: UCSD (vs UAB) | +223.3038 | 465.4522 | ±930.9045 | +0.480 | 0.6314 |  |
| Site: UW (vs UAB) | +179.1778 | 411.3141 | ±822.6282 | +0.436 | 0.6631 |  |
| **Age (years)** | **-142.2047** | 16.3144 | ±32.6288 | **-8.717** | **2.87e-18** | *** |
| BMI (kg/m2) | -44.1636 | 27.5674 | ±55.1348 | -1.602 | 0.1092 |  |
| Hypertension | -287.2608 | 400.1970 | ±800.3940 | -0.718 | 0.4729 |  |
| High cholesterol | -83.1467 | 363.4563 | ±726.9125 | -0.229 | 0.8191 |  |
| Kidney disease | -670.3688 | 730.5321 | ±1461.0641 | -0.918 | 0.3588 |  |
| Circulatory disease | -597.8658 | 450.4116 | ±900.8232 | -1.327 | 0.1844 |  |
| CV (%) | -44.3301 | 28.3191 | ±56.6383 | -1.565 | 0.1175 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **575**, R² = **0.1608**, Adj R² = **0.1444**, F-statistic = **9.80** (p = **2.31e-16**), Residual SE = **4145.373** on **563** df, AIC = **11222.9**, BIC = **11275.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19855.5962** | 1629.0407 | ±3258.0814 | **+12.189** | **3.58e-34** | *** |
| Education: graduate level (vs college) | -655.2927 | 389.5265 | ±779.0530 | -1.682 | 0.0925 | . |
| Education: high school or below (vs college) | +813.4471 | 703.8538 | ±1407.7076 | +1.156 | 0.2478 |  |
| Site: UCSD (vs UAB) | +224.5328 | 464.7463 | ±929.4925 | +0.483 | 0.6290 |  |
| Site: UW (vs UAB) | +231.9637 | 410.0340 | ±820.0680 | +0.566 | 0.5716 |  |
| **Age (years)** | **-145.4823** | 16.3377 | ±32.6753 | **-8.905** | **5.35e-19** | *** |
| BMI (kg/m2) | -42.8766 | 27.5203 | ±55.0405 | -1.558 | 0.1192 |  |
| Hypertension | -318.1394 | 402.0132 | ±804.0264 | -0.791 | 0.4287 |  |
| High cholesterol | -82.3872 | 363.8148 | ±727.6296 | -0.226 | 0.8208 |  |
| Kidney disease | -834.9532 | 731.9654 | ±1463.9308 | -1.141 | 0.2540 |  |
| Circulatory disease | -575.6319 | 451.3578 | ±902.7157 | -1.275 | 0.2022 |  |
| Mean / SD ratio | +47.7094 | 133.4236 | ±266.8471 | +0.358 | 0.7207 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **575**, R² = **0.1606**, Adj R² = **0.1442**, F-statistic = **9.79** (p = **2.43e-16**), Residual SE = **4145.782** on **563** df, AIC = **11223.0**, BIC = **11275.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20229.3149** | 1628.8848 | ±3257.7697 | **+12.419** | **2.06e-35** | *** |
| Education: graduate level (vs college) | -654.0145 | 389.5682 | ±779.1364 | -1.679 | 0.0932 | . |
| Education: high school or below (vs college) | +782.2072 | 703.1710 | ±1406.3421 | +1.112 | 0.2660 |  |
| Site: UCSD (vs UAB) | +218.9113 | 464.4335 | ±928.8670 | +0.471 | 0.6374 |  |
| Site: UW (vs UAB) | +242.0167 | 408.6004 | ±817.2008 | +0.592 | 0.5536 |  |
| **Age (years)** | **-146.7683** | 16.3413 | ±32.6826 | **-8.981** | **2.67e-19** | *** |
| BMI (kg/m2) | -42.8332 | 27.4803 | ±54.9605 | -1.559 | 0.1191 |  |
| Hypertension | -327.7009 | 401.7399 | ±803.4799 | -0.816 | 0.4147 |  |
| High cholesterol | -82.9478 | 364.0270 | ±728.0540 | -0.228 | 0.8198 |  |
| Kidney disease | -874.7882 | 729.5399 | ±1459.0798 | -1.199 | 0.2305 |  |
| Circulatory disease | -573.7364 | 450.8883 | ±901.7767 | -1.272 | 0.2032 |  |
| Avg. daily mean/SD | -7.3613 | 106.3214 | ±212.6429 | -0.069 | 0.9448 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **575**, R² = **0.1619**, Adj R² = **0.1455**, F-statistic = **9.89** (p = **1.62e-16**), Residual SE = **4142.528** on **563** df, AIC = **11222.1**, BIC = **11274.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19462.2168** | 1634.3852 | ±3268.7703 | **+11.908** | **1.08e-32** | *** |
| Education: graduate level (vs college) | -646.2435 | 390.0558 | ±780.1117 | -1.657 | 0.0976 | . |
| Education: high school or below (vs college) | +741.8823 | 705.3531 | ±1410.7063 | +1.052 | 0.2929 |  |
| Site: UCSD (vs UAB) | +202.8243 | 460.8856 | ±921.7712 | +0.440 | 0.6599 |  |
| Site: UW (vs UAB) | +287.8676 | 415.1556 | ±830.3111 | +0.693 | 0.4881 |  |
| **Age (years)** | **-146.6457** | 16.0428 | ±32.0856 | **-9.141** | **6.19e-20** | *** |
| BMI (kg/m2) | -43.4397 | 27.4057 | ±54.8114 | -1.585 | 0.1130 |  |
| Hypertension | -342.8890 | 401.5992 | ±803.1983 | -0.854 | 0.3932 |  |
| High cholesterol | -77.9094 | 363.3517 | ±726.7035 | -0.214 | 0.8302 |  |
| Kidney disease | -894.0062 | 720.7641 | ±1441.5283 | -1.240 | 0.2148 |  |
| Circulatory disease | -570.3695 | 451.1752 | ±902.3505 | -1.264 | 0.2062 |  |
| MAG (mg/dL/h) | +17.5844 | 20.3346 | ±40.6691 | +0.865 | 0.3872 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **575**, R² = **0.1622**, Adj R² = **0.1459**, F-statistic = **9.91** (p = **1.46e-16**), Residual SE = **4141.716** on **563** df, AIC = **11221.8**, BIC = **11274.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20608.6988** | 1480.5866 | ±2961.1733 | **+13.919** | **4.84e-44** | *** |
| Education: graduate level (vs college) | -673.0084 | 390.7837 | ±781.5673 | -1.722 | 0.0850 | . |
| Education: high school or below (vs college) | +881.9130 | 698.8448 | ±1397.6897 | +1.262 | 0.2070 |  |
| Site: UCSD (vs UAB) | +230.7968 | 464.4311 | ±928.8623 | +0.497 | 0.6192 |  |
| Site: UW (vs UAB) | +211.0373 | 411.4002 | ±822.8005 | +0.513 | 0.6080 |  |
| **Age (years)** | **-144.3189** | 16.1020 | ±32.2039 | **-8.963** | **3.16e-19** | *** |
| BMI (kg/m2) | -44.0868 | 27.5891 | ±55.1783 | -1.598 | 0.1100 |  |
| Hypertension | -294.7057 | 401.8852 | ±803.7704 | -0.733 | 0.4634 |  |
| High cholesterol | -66.4974 | 364.2427 | ±728.4854 | -0.183 | 0.8551 |  |
| Kidney disease | -740.0027 | 727.1365 | ±1454.2730 | -1.018 | 0.3088 |  |
| Circulatory disease | -579.8070 | 450.4733 | ±900.9466 | -1.287 | 0.1981 |  |
| Avg. daily range (mg/dL) | -4.9747 | 4.7607 | ±9.5215 | -1.045 | 0.2960 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **575**, R² = **0.1607**, Adj R² = **0.1443**, F-statistic = **9.80** (p = **2.35e-16**), Residual SE = **4145.529** on **563** df, AIC = **11222.9**, BIC = **11275.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20215.8755** | 1409.5840 | ±2819.1680 | **+14.342** | **1.20e-46** | *** |
| Education: graduate level (vs college) | -658.1632 | 391.0592 | ±782.1185 | -1.683 | 0.0924 | . |
| Education: high school or below (vs college) | +791.5185 | 708.5610 | ±1417.1220 | +1.117 | 0.2640 |  |
| Site: UCSD (vs UAB) | +216.6188 | 467.5743 | ±935.1487 | +0.463 | 0.6432 |  |
| Site: UW (vs UAB) | +232.6540 | 411.9691 | ±823.9382 | +0.565 | 0.5723 |  |
| **Age (years)** | **-146.3317** | 16.1016 | ±32.2033 | **-9.088** | **1.01e-19** | *** |
| BMI (kg/m2) | -42.7913 | 27.4531 | ±54.9062 | -1.559 | 0.1191 |  |
| Hypertension | -316.4429 | 404.3091 | ±808.6181 | -0.783 | 0.4338 |  |
| High cholesterol | -80.4399 | 365.3781 | ±730.7561 | -0.220 | 0.8258 |  |
| Kidney disease | -848.3958 | 723.3064 | ±1446.6128 | -1.173 | 0.2408 |  |
| Circulatory disease | -570.3224 | 453.7056 | ±907.4113 | -1.257 | 0.2087 |  |
| SD of daily means (mg/dL) | -7.0007 | 29.7690 | ±59.5380 | -0.235 | 0.8141 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **575**, R² = **0.1632**, Adj R² = **0.1469**, F-statistic = **9.98** (p = **1.08e-16**), Residual SE = **4139.296** on **563** df, AIC = **11221.2**, BIC = **11273.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18395.4471** | 1764.9775 | ±3529.9549 | **+10.422** | **1.96e-25** | *** |
| Education: graduate level (vs college) | -684.1737 | 390.8510 | ±781.7019 | -1.750 | 0.0800 | . |
| Education: high school or below (vs college) | +843.3869 | 706.1644 | ±1412.3288 | +1.194 | 0.2324 |  |
| Site: UCSD (vs UAB) | +198.7483 | 473.1960 | ±946.3919 | +0.420 | 0.6745 |  |
| Site: UW (vs UAB) | +186.6221 | 410.9232 | ±821.8464 | +0.454 | 0.6497 |  |
| **Age (years)** | **-145.3192** | 16.0070 | ±32.0141 | **-9.078** | **1.10e-19** | *** |
| BMI (kg/m2) | -42.6466 | 27.4858 | ±54.9716 | -1.552 | 0.1208 |  |
| Hypertension | -291.2009 | 402.1897 | ±804.3794 | -0.724 | 0.4690 |  |
| High cholesterol | -52.3932 | 364.3973 | ±728.7946 | -0.144 | 0.8857 |  |
| Kidney disease | -735.0410 | 726.6934 | ±1453.3868 | -1.011 | 0.3118 |  |
| Circulatory disease | -564.6911 | 452.2750 | ±904.5500 | -1.249 | 0.2118 |  |
| Time in range 70-180, pooled (%) | +18.3969 | 14.1910 | ±28.3820 | +1.296 | 0.1948 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **575**, R² = **0.1631**, Adj R² = **0.1467**, F-statistic = **9.97** (p = **1.12e-16**), Residual SE = **4139.622** on **563** df, AIC = **11221.3**, BIC = **11273.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18437.3947** | 1784.7293 | ±3569.4587 | **+10.331** | **5.12e-25** | *** |
| Education: graduate level (vs college) | -684.2113 | 390.7964 | ±781.5928 | -1.751 | 0.0800 | . |
| Education: high school or below (vs college) | +844.8831 | 706.2160 | ±1412.4321 | +1.196 | 0.2316 |  |
| Site: UCSD (vs UAB) | +199.2511 | 472.4466 | ±944.8932 | +0.422 | 0.6732 |  |
| Site: UW (vs UAB) | +187.1992 | 410.9451 | ±821.8901 | +0.456 | 0.6487 |  |
| **Age (years)** | **-145.2635** | 16.0057 | ±32.0115 | **-9.076** | **1.13e-19** | *** |
| BMI (kg/m2) | -42.6894 | 27.4692 | ±54.9385 | -1.554 | 0.1202 |  |
| Hypertension | -293.3738 | 401.8443 | ±803.6885 | -0.730 | 0.4653 |  |
| High cholesterol | -51.4244 | 365.0717 | ±730.1433 | -0.141 | 0.8880 |  |
| Kidney disease | -737.1333 | 726.1854 | ±1452.3707 | -1.015 | 0.3101 |  |
| Circulatory disease | -564.6302 | 452.2128 | ±904.4256 | -1.249 | 0.2118 |  |
| Avg. daily time in range 70-180 (%) | +17.8433 | 14.1255 | ±28.2509 | +1.263 | 0.2065 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **575**, R² = **0.1627**, Adj R² = **0.1463**, F-statistic = **9.95** (p = **1.26e-16**), Residual SE = **4140.563** on **563** df, AIC = **11221.5**, BIC = **11273.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20343.9950** | 1395.3651 | ±2790.7302 | **+14.580** | **3.78e-48** | *** |
| Education: graduate level (vs college) | -665.9722 | 388.8031 | ±777.6062 | -1.713 | 0.0867 | . |
| Education: high school or below (vs college) | +753.8316 | 705.4639 | ±1410.9279 | +1.069 | 0.2853 |  |
| Site: UCSD (vs UAB) | +143.5148 | 471.1757 | ±942.3515 | +0.305 | 0.7607 |  |
| Site: UW (vs UAB) | +175.3340 | 408.8926 | ±817.7852 | +0.429 | 0.6681 |  |
| **Age (years)** | **-146.2828** | 16.0593 | ±32.1187 | **-9.109** | **8.32e-20** | *** |
| BMI (kg/m2) | -43.4427 | 27.6101 | ±55.2201 | -1.573 | 0.1156 |  |
| Hypertension | -345.8960 | 400.2402 | ±800.4803 | -0.864 | 0.3875 |  |
| High cholesterol | -113.5988 | 364.7821 | ±729.5642 | -0.311 | 0.7555 |  |
| Kidney disease | -854.6863 | 715.0338 | ±1430.0677 | -1.195 | 0.2320 |  |
| Circulatory disease | -570.5839 | 451.2019 | ±902.4038 | -1.265 | 0.2060 |  |
| Time < 54 (%) | -230.8858 | 131.2264 | ±262.4528 | -1.759 | 0.0785 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **575**, R² = **0.1630**, Adj R² = **0.1466**, F-statistic = **9.97** (p = **1.15e-16**), Residual SE = **4139.822** on **563** df, AIC = **11221.3**, BIC = **11273.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20269.3782** | 1384.9622 | ±2769.9243 | **+14.635** | **1.67e-48** | *** |
| Education: graduate level (vs college) | -678.7552 | 390.0488 | ±780.0976 | -1.740 | 0.0818 | . |
| Education: high school or below (vs college) | +749.7254 | 705.3428 | ±1410.6857 | +1.063 | 0.2878 |  |
| Site: UCSD (vs UAB) | +150.6283 | 470.4850 | ±940.9700 | +0.320 | 0.7489 |  |
| Site: UW (vs UAB) | +164.2694 | 410.5060 | ±821.0119 | +0.400 | 0.6890 |  |
| **Age (years)** | **-145.3150** | 16.0716 | ±32.1432 | **-9.042** | **1.54e-19** | *** |
| BMI (kg/m2) | -43.2799 | 27.5296 | ±55.0593 | -1.572 | 0.1159 |  |
| Hypertension | -347.4472 | 400.2301 | ±800.4602 | -0.868 | 0.3853 |  |
| High cholesterol | -117.8549 | 363.7664 | ±727.5329 | -0.324 | 0.7459 |  |
| Kidney disease | -847.5084 | 714.5792 | ±1429.1584 | -1.186 | 0.2356 |  |
| Circulatory disease | -567.6092 | 449.9640 | ±899.9279 | -1.261 | 0.2071 |  |
| Avg. daily time < 54 (%) | -285.5050 | 152.5420 | ±305.0840 | -1.872 | 0.0613 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **575**, R² = **0.1622**, Adj R² = **0.1459**, F-statistic = **9.91** (p = **1.47e-16**), Residual SE = **4141.744** on **563** df, AIC = **11221.9**, BIC = **11274.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20307.7728** | 1388.8564 | ±2777.7128 | **+14.622** | **2.04e-48** | *** |
| Education: graduate level (vs college) | -681.2575 | 387.8170 | ±775.6339 | -1.757 | 0.0790 | . |
| Education: high school or below (vs college) | +788.8929 | 708.1386 | ±1416.2771 | +1.114 | 0.2653 |  |
| Site: UCSD (vs UAB) | +181.4121 | 462.0513 | ±924.1025 | +0.393 | 0.6946 |  |
| Site: UW (vs UAB) | +195.3388 | 403.5968 | ±807.1935 | +0.484 | 0.6284 |  |
| **Age (years)** | **-145.8620** | 16.0623 | ±32.1245 | **-9.081** | **1.08e-19** | *** |
| BMI (kg/m2) | -42.9305 | 27.7709 | ±55.5419 | -1.546 | 0.1221 |  |
| Hypertension | -347.3897 | 403.1582 | ±806.3165 | -0.862 | 0.3889 |  |
| High cholesterol | -97.9196 | 363.6842 | ±727.3683 | -0.269 | 0.7877 |  |
| Kidney disease | -853.5602 | 714.6579 | ±1429.3158 | -1.194 | 0.2323 |  |
| Circulatory disease | -587.3914 | 450.8216 | ±901.6433 | -1.303 | 0.1926 |  |
| Time 54-69, pooled (%) | -78.7976 | 73.0169 | ±146.0339 | -1.079 | 0.2805 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **575**, R² = **0.1622**, Adj R² = **0.1459**, F-statistic = **9.91** (p = **1.46e-16**), Residual SE = **4141.721** on **563** df, AIC = **11221.8**, BIC = **11274.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20267.2553** | 1383.3358 | ±2766.6716 | **+14.651** | **1.33e-48** | *** |
| Education: graduate level (vs college) | -682.8945 | 388.1055 | ±776.2110 | -1.760 | 0.0785 | . |
| Education: high school or below (vs college) | +789.9552 | 708.1576 | ±1416.3153 | +1.116 | 0.2646 |  |
| Site: UCSD (vs UAB) | +186.9076 | 461.9115 | ±923.8230 | +0.405 | 0.6857 |  |
| Site: UW (vs UAB) | +192.7600 | 404.0776 | ±808.1552 | +0.477 | 0.6333 |  |
| **Age (years)** | **-145.4947** | 16.0907 | ±32.1813 | **-9.042** | **1.54e-19** | *** |
| BMI (kg/m2) | -42.8730 | 27.7277 | ±55.4554 | -1.546 | 0.1221 |  |
| Hypertension | -345.8446 | 403.3262 | ±806.6524 | -0.857 | 0.3912 |  |
| High cholesterol | -96.6767 | 363.4152 | ±726.8304 | -0.266 | 0.7902 |  |
| Kidney disease | -853.9739 | 714.5567 | ±1429.1135 | -1.195 | 0.2320 |  |
| Circulatory disease | -586.7207 | 450.2436 | ±900.4871 | -1.303 | 0.1925 |  |
| Avg. daily time 54-69 (%) | -75.8679 | 69.7930 | ±139.5860 | -1.087 | 0.2770 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **575**, R² = **0.1628**, Adj R² = **0.1464**, F-statistic = **9.95** (p = **1.23e-16**), Residual SE = **4140.336** on **563** df, AIC = **11221.5**, BIC = **11273.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20354.3103** | 1394.3209 | ±2788.6417 | **+14.598** | **2.89e-48** | *** |
| Education: graduate level (vs college) | -683.2331 | 387.8959 | ±775.7917 | -1.761 | 0.0782 | . |
| Education: high school or below (vs college) | +778.0436 | 707.3559 | ±1414.7118 | +1.100 | 0.2714 |  |
| Site: UCSD (vs UAB) | +159.3783 | 463.6965 | ±927.3930 | +0.344 | 0.7311 |  |
| Site: UW (vs UAB) | +177.3735 | 404.2471 | ±808.4941 | +0.439 | 0.6608 |  |
| **Age (years)** | **-145.8215** | 16.0538 | ±32.1077 | **-9.083** | **1.05e-19** | *** |
| BMI (kg/m2) | -43.1196 | 27.7865 | ±55.5730 | -1.552 | 0.1207 |  |
| Hypertension | -352.1951 | 402.6343 | ±805.2686 | -0.875 | 0.3817 |  |
| High cholesterol | -106.8216 | 363.9684 | ±727.9368 | -0.293 | 0.7691 |  |
| Kidney disease | -849.9702 | 714.0351 | ±1428.0702 | -1.190 | 0.2339 |  |
| Circulatory disease | -585.3486 | 450.9894 | ±901.9788 | -1.298 | 0.1943 |  |
| Time < 70 (%) | -73.6869 | 55.2934 | ±110.5867 | -1.333 | 0.1826 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **575**, R² = **0.1627**, Adj R² = **0.1464**, F-statistic = **9.95** (p = **1.25e-16**), Residual SE = **4140.465** on **563** df, AIC = **11221.5**, BIC = **11273.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20286.3727** | 1385.0957 | ±2770.1914 | **+14.646** | **1.42e-48** | *** |
| Education: graduate level (vs college) | -687.3355 | 388.4624 | ±776.9248 | -1.769 | 0.0768 | . |
| Education: high school or below (vs college) | +780.3514 | 707.2153 | ±1414.4306 | +1.103 | 0.2698 |  |
| Site: UCSD (vs UAB) | +171.3980 | 462.9831 | ±925.9661 | +0.370 | 0.7112 |  |
| Site: UW (vs UAB) | +176.4154 | 404.9493 | ±809.8987 | +0.436 | 0.6631 |  |
| **Age (years)** | **-145.2477** | 16.0863 | ±32.1726 | **-9.029** | **1.73e-19** | *** |
| BMI (kg/m2) | -42.9831 | 27.7178 | ±55.4356 | -1.551 | 0.1210 |  |
| Hypertension | -349.9284 | 402.8419 | ±805.6838 | -0.869 | 0.3850 |  |
| High cholesterol | -104.6728 | 363.3740 | ±726.7479 | -0.288 | 0.7733 |  |
| Kidney disease | -849.4608 | 713.9893 | ±1427.9785 | -1.190 | 0.2341 |  |
| Circulatory disease | -584.3132 | 449.9394 | ±899.8788 | -1.299 | 0.1941 |  |
| Avg. daily time < 70 (%) | -71.4214 | 54.5763 | ±109.1526 | -1.309 | 0.1907 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **575**, R² = **0.1634**, Adj R² = **0.1471**, F-statistic = **10.00** (p = **1.00e-16**), Residual SE = **4138.718** on **563** df, AIC = **11221.0**, BIC = **11273.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16103.2973** | 2934.0237 | ±5868.0474 | **+5.488** | **4.05e-08** | *** |
| Education: graduate level (vs college) | -681.2316 | 389.4004 | ±778.8007 | -1.749 | 0.0802 | . |
| Education: high school or below (vs college) | +841.0016 | 705.1319 | ±1410.2637 | +1.193 | 0.2330 |  |
| Site: UCSD (vs UAB) | +190.0550 | 470.6022 | ±941.2043 | +0.404 | 0.6863 |  |
| Site: UW (vs UAB) | +184.3836 | 409.2060 | ±818.4119 | +0.451 | 0.6523 |  |
| **Age (years)** | **-146.5633** | 16.0549 | ±32.1097 | **-9.129** | **6.92e-20** | *** |
| BMI (kg/m2) | -43.3173 | 27.3886 | ±54.7771 | -1.582 | 0.1137 |  |
| Hypertension | -301.0718 | 399.4671 | ±798.9342 | -0.754 | 0.4510 |  |
| High cholesterol | -91.0586 | 363.2624 | ±726.5247 | -0.251 | 0.8021 |  |
| Kidney disease | -796.4759 | 717.5896 | ±1435.1792 | -1.110 | 0.2670 |  |
| Circulatory disease | -551.6281 | 453.7554 | ±907.5109 | -1.216 | 0.2241 |  |
| Time 54-250, pooled (%) | +41.6817 | 27.8201 | ±55.6403 | +1.498 | 0.1341 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **575**, R² = **0.1624**, Adj R² = **0.1460**, F-statistic = **9.92** (p = **1.40e-16**), Residual SE = **4141.376** on **563** df, AIC = **11221.8**, BIC = **11274.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16566.9734** | 3391.1388 | ±6782.2776 | **+4.885** | **1.03e-06** | *** |
| Education: graduate level (vs college) | -678.4425 | 389.9362 | ±779.8724 | -1.740 | 0.0819 | . |
| Education: high school or below (vs college) | +836.1310 | 704.6270 | ±1409.2539 | +1.187 | 0.2354 |  |
| Site: UCSD (vs UAB) | +199.1717 | 469.7532 | ±939.5063 | +0.424 | 0.6716 |  |
| Site: UW (vs UAB) | +197.3360 | 409.2340 | ±818.4680 | +0.482 | 0.6297 |  |
| **Age (years)** | **-146.3190** | 16.0486 | ±32.0972 | **-9.117** | **7.71e-20** | *** |
| BMI (kg/m2) | -43.3883 | 27.4217 | ±54.8435 | -1.582 | 0.1136 |  |
| Hypertension | -306.4865 | 400.0440 | ±800.0880 | -0.766 | 0.4436 |  |
| High cholesterol | -87.2318 | 363.6536 | ±727.3072 | -0.240 | 0.8104 |  |
| Kidney disease | -801.3850 | 717.5601 | ±1435.1202 | -1.117 | 0.2641 |  |
| Circulatory disease | -552.4109 | 454.7112 | ±909.4223 | -1.215 | 0.2244 |  |
| Avg. daily time 54-250 (%) | +36.6828 | 32.6622 | ±65.3244 | +1.123 | 0.2614 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **575**, R² = **0.1614**, Adj R² = **0.1450**, F-statistic = **9.85** (p = **1.92e-16**), Residual SE = **4143.892** on **563** df, AIC = **11222.5**, BIC = **11274.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20160.9034** | 1377.5521 | ±2755.1042 | **+14.635** | **1.67e-48** | *** |
| Education: graduate level (vs college) | -663.4771 | 390.9008 | ±781.8016 | -1.697 | 0.0896 | . |
| Education: high school or below (vs college) | +812.6052 | 705.1587 | ±1410.3174 | +1.152 | 0.2492 |  |
| Site: UCSD (vs UAB) | +221.1344 | 467.6197 | ±935.2393 | +0.473 | 0.6363 |  |
| Site: UW (vs UAB) | +226.2170 | 409.8444 | ±819.6888 | +0.552 | 0.5810 |  |
| **Age (years)** | **-145.7053** | 15.9904 | ±31.9809 | **-9.112** | **8.09e-20** | *** |
| BMI (kg/m2) | -42.4987 | 27.4561 | ±54.9121 | -1.548 | 0.1217 |  |
| Hypertension | -303.8723 | 405.2551 | ±810.5102 | -0.750 | 0.4534 |  |
| High cholesterol | -53.1588 | 366.3862 | ±732.7725 | -0.145 | 0.8846 |  |
| Kidney disease | -791.9109 | 734.0587 | ±1468.1174 | -1.079 | 0.2807 |  |
| Circulatory disease | -572.2368 | 452.1166 | ±904.2332 | -1.266 | 0.2056 |  |
| Time 181-250, pooled (%) | -14.4335 | 21.8861 | ±43.7722 | -0.659 | 0.5096 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **575**, R² = **0.1618**, Adj R² = **0.1454**, F-statistic = **9.88** (p = **1.66e-16**), Residual SE = **4142.767** on **563** df, AIC = **11222.1**, BIC = **11274.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20167.3082** | 1379.0995 | ±2758.1991 | **+14.624** | **1.99e-48** | *** |
| Education: graduate level (vs college) | -665.6183 | 390.4045 | ±780.8090 | -1.705 | 0.0882 | . |
| Education: high school or below (vs college) | +820.3204 | 705.2070 | ±1410.4140 | +1.163 | 0.2447 |  |
| Site: UCSD (vs UAB) | +217.5571 | 468.8253 | ±937.6506 | +0.464 | 0.6426 |  |
| Site: UW (vs UAB) | +219.9334 | 409.9652 | ±819.9305 | +0.536 | 0.5916 |  |
| **Age (years)** | **-145.6340** | 16.0047 | ±32.0094 | **-9.099** | **9.08e-20** | *** |
| BMI (kg/m2) | -42.4121 | 27.4394 | ±54.8788 | -1.546 | 0.1222 |  |
| Hypertension | -298.9556 | 404.1033 | ±808.2067 | -0.740 | 0.4594 |  |
| High cholesterol | -46.2630 | 366.5226 | ±733.0452 | -0.126 | 0.8996 |  |
| Kidney disease | -774.6856 | 732.0717 | ±1464.1435 | -1.058 | 0.2900 |  |
| Circulatory disease | -572.4002 | 451.8978 | ±903.7956 | -1.267 | 0.2053 |  |
| Avg. daily time 181-250 (%) | -17.6447 | 20.6457 | ±41.2914 | -0.855 | 0.3928 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **575**, R² = **0.1622**, Adj R² = **0.1459**, F-statistic = **9.91** (p = **1.46e-16**), Residual SE = **4141.740** on **563** df, AIC = **11221.9**, BIC = **11274.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20185.2002** | 1381.3548 | ±2762.7097 | **+14.613** | **2.33e-48** | *** |
| Education: graduate level (vs college) | -672.1950 | 390.8107 | ±781.6213 | -1.720 | 0.0854 | . |
| Education: high school or below (vs college) | +833.5369 | 704.2169 | ±1408.4338 | +1.184 | 0.2366 |  |
| Site: UCSD (vs UAB) | +215.3702 | 469.4671 | ±938.9343 | +0.459 | 0.6464 |  |
| Site: UW (vs UAB) | +210.5426 | 410.2823 | ±820.5646 | +0.513 | 0.6078 |  |
| **Age (years)** | **-145.7211** | 16.0234 | ±32.0468 | **-9.094** | **9.52e-20** | *** |
| BMI (kg/m2) | -42.6278 | 27.4425 | ±54.8851 | -1.553 | 0.1203 |  |
| Hypertension | -293.5943 | 403.3692 | ±806.7384 | -0.728 | 0.4667 |  |
| High cholesterol | -53.9560 | 364.9394 | ±729.8787 | -0.148 | 0.8825 |  |
| Kidney disease | -766.9647 | 727.3540 | ±1454.7081 | -1.054 | 0.2917 |  |
| Circulatory disease | -564.5424 | 452.5856 | ±905.1712 | -1.247 | 0.2123 |  |
| Time > 180 (%) | -14.5333 | 14.5617 | ±29.1234 | -0.998 | 0.3183 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **575**, R² = **0.1621**, Adj R² = **0.1458**, F-statistic = **9.90** (p = **1.50e-16**), Residual SE = **4141.949** on **563** df, AIC = **11221.9**, BIC = **11274.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20188.0991** | 1381.3829 | ±2762.7658 | **+14.614** | **2.27e-48** | *** |
| Education: graduate level (vs college) | -671.5183 | 390.5775 | ±781.1550 | -1.719 | 0.0856 | . |
| Education: high school or below (vs college) | +834.5572 | 704.1984 | ±1408.3969 | +1.185 | 0.2360 |  |
| Site: UCSD (vs UAB) | +213.3589 | 469.6439 | ±939.2878 | +0.454 | 0.6496 |  |
| Site: UW (vs UAB) | +211.0102 | 410.1535 | ±820.3069 | +0.514 | 0.6069 |  |
| **Age (years)** | **-145.7857** | 16.0252 | ±32.0504 | **-9.097** | **9.26e-20** | *** |
| BMI (kg/m2) | -42.6877 | 27.4358 | ±54.8717 | -1.556 | 0.1197 |  |
| Hypertension | -295.5615 | 402.8690 | ±805.7381 | -0.734 | 0.4632 |  |
| High cholesterol | -53.4301 | 365.4261 | ±730.8523 | -0.146 | 0.8838 |  |
| Kidney disease | -768.0921 | 726.5975 | ±1453.1950 | -1.057 | 0.2905 |  |
| Circulatory disease | -564.6369 | 452.6414 | ±905.2828 | -1.247 | 0.2122 |  |
| Avg. daily time > 180 (%) | -14.1843 | 14.5056 | ±29.0111 | -0.978 | 0.3281 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **575**, R² = **0.1626**, Adj R² = **0.1463**, F-statistic = **9.94** (p = **1.28e-16**), Residual SE = **4140.686** on **563** df, AIC = **11221.6**, BIC = **11273.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20180.2711** | 1380.5930 | ±2761.1859 | **+14.617** | **2.18e-48** | *** |
| Education: graduate level (vs college) | -676.1803 | 389.7015 | ±779.4030 | -1.735 | 0.0827 | . |
| Education: high school or below (vs college) | +819.3442 | 707.9268 | ±1415.8535 | +1.157 | 0.2471 |  |
| Site: UCSD (vs UAB) | +211.3012 | 472.2375 | ±944.4749 | +0.447 | 0.6546 |  |
| Site: UW (vs UAB) | +213.7796 | 408.9859 | ±817.9718 | +0.523 | 0.6012 |  |
| **Age (years)** | **-146.3845** | 16.0702 | ±32.1403 | **-9.109** | **8.31e-20** | *** |
| BMI (kg/m2) | -41.7838 | 27.3723 | ±54.7446 | -1.526 | 0.1269 |  |
| Hypertension | -284.7475 | 402.8002 | ±805.6005 | -0.707 | 0.4796 |  |
| High cholesterol | -55.3321 | 365.0961 | ±730.1921 | -0.152 | 0.8795 |  |
| Kidney disease | -814.8635 | 721.5895 | ±1443.1789 | -1.129 | 0.2588 |  |
| Circulatory disease | -557.8745 | 453.5365 | ±907.0730 | -1.230 | 0.2187 |  |
| Nocturnal time > 180 (%) | -16.6306 | 15.4408 | ±30.8816 | -1.077 | 0.2815 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **575**, R² = **0.1608**, Adj R² = **0.1444**, F-statistic = **9.81** (p = **2.28e-16**), Residual SE = **4145.299** on **563** df, AIC = **11222.8**, BIC = **11275.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20162.4429** | 1382.4905 | ±2764.9811 | **+14.584** | **3.54e-48** | *** |
| Education: graduate level (vs college) | -646.1765 | 392.9623 | ±785.9247 | -1.644 | 0.1001 |  |
| Education: high school or below (vs college) | +773.7632 | 705.9574 | ±1411.9148 | +1.096 | 0.2731 |  |
| Site: UCSD (vs UAB) | +212.2822 | 460.2952 | ±920.5905 | +0.461 | 0.6447 |  |
| Site: UW (vs UAB) | +245.3992 | 409.8698 | ±819.7396 | +0.599 | 0.5494 |  |
| **Age (years)** | **-147.1892** | 16.0534 | ±32.1067 | **-9.169** | **4.79e-20** | *** |
| BMI (kg/m2) | -42.3409 | 27.7337 | ±55.4674 | -1.527 | 0.1268 |  |
| Hypertension | -341.5049 | 406.6035 | ±813.2070 | -0.840 | 0.4010 |  |
| High cholesterol | -91.0331 | 365.9153 | ±731.8307 | -0.249 | 0.8035 |  |
| Kidney disease | -903.0616 | 732.0779 | ±1464.1557 | -1.234 | 0.2174 |  |
| Circulatory disease | -570.8341 | 451.2208 | ±902.4416 | -1.265 | 0.2058 |  |
| Any reading > 250 during wear (0/1) | +147.2748 | 438.4513 | ±876.9026 | +0.336 | 0.7369 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **575**, R² = **0.1628**, Adj R² = **0.1464**, F-statistic = **9.95** (p = **1.23e-16**), Residual SE = **4140.320** on **563** df, AIC = **11221.5**, BIC = **11273.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20232.6303** | 1380.3036 | ±2760.6071 | **+14.658** | **1.20e-48** | *** |
| Education: graduate level (vs college) | -676.4742 | 389.5561 | ±779.1121 | -1.737 | 0.0825 | . |
| Education: high school or below (vs college) | +840.7310 | 704.1537 | ±1408.3074 | +1.194 | 0.2325 |  |
| Site: UCSD (vs UAB) | +205.7194 | 468.5634 | ±937.1267 | +0.439 | 0.6606 |  |
| Site: UW (vs UAB) | +200.9867 | 408.6617 | ±817.3234 | +0.492 | 0.6228 |  |
| **Age (years)** | **-146.6048** | 16.0613 | ±32.1226 | **-9.128** | **6.99e-20** | *** |
| BMI (kg/m2) | -43.1663 | 27.3885 | ±54.7770 | -1.576 | 0.1150 |  |
| Hypertension | -300.6915 | 399.8916 | ±799.7833 | -0.752 | 0.4521 |  |
| High cholesterol | -85.1542 | 363.4558 | ±726.9116 | -0.234 | 0.8148 |  |
| Kidney disease | -806.5540 | 717.9546 | ±1435.9093 | -1.123 | 0.2613 |  |
| Circulatory disease | -554.6568 | 453.8010 | ±907.6021 | -1.222 | 0.2216 |  |
| Time > 250 (%) | -37.2300 | 28.6399 | ±57.2798 | -1.300 | 0.1936 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 575)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **575**, R² = **0.1619**, Adj R² = **0.1455**, F-statistic = **9.88** (p = **1.64e-16**), Residual SE = **4142.657** on **563** df, AIC = **11222.1**, BIC = **11274.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20215.1719** | 1380.5096 | ±2761.0191 | **+14.643** | **1.49e-48** | *** |
| Education: graduate level (vs college) | -672.3528 | 389.8129 | ±779.6258 | -1.725 | 0.0846 | . |
| Education: high school or below (vs college) | +833.4882 | 703.4311 | ±1406.8622 | +1.185 | 0.2361 |  |
| Site: UCSD (vs UAB) | +209.8825 | 468.0798 | ±936.1596 | +0.448 | 0.6539 |  |
| Site: UW (vs UAB) | +211.9112 | 408.5128 | ±817.0256 | +0.519 | 0.6039 |  |
| **Age (years)** | **-146.4877** | 16.0568 | ±32.1135 | **-9.123** | **7.30e-20** | *** |
| BMI (kg/m2) | -43.2602 | 27.4245 | ±54.8490 | -1.577 | 0.1147 |  |
| Hypertension | -307.0126 | 400.3429 | ±800.6857 | -0.767 | 0.4432 |  |
| High cholesterol | -82.6854 | 363.8645 | ±727.7289 | -0.227 | 0.8202 |  |
| Kidney disease | -813.2753 | 717.5361 | ±1435.0722 | -1.133 | 0.2570 |  |
| Circulatory disease | -556.2310 | 454.7582 | ±909.5165 | -1.223 | 0.2213 |  |
| Avg. daily time > 250 (%) | -31.5322 | 33.0239 | ±66.0478 | -0.955 | 0.3397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 575; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **575**, R² = **0.1803**, Adj R² = **0.1658**, F-statistic = **12.40** (p = **1.38e-19**), Residual SE = **12.547** on **564** df, AIC = **4551.5**, BIC = **4599.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9225** | 4.1948 | ±8.3896 | **+13.093** | **3.61e-39** | *** |
| Education: graduate level (vs college) | -1.8636 | 1.1909 | ±2.3819 | -1.565 | 0.1176 |  |
| Education: high school or below (vs college) | +3.0714 | 2.1569 | ±4.3139 | +1.424 | 0.1545 |  |
| Site: UCSD (vs UAB) | +0.0930 | 1.4720 | ±2.9441 | +0.063 | 0.9496 |  |
| Site: UW (vs UAB) | +0.5793 | 1.2428 | ±2.4856 | +0.466 | 0.6411 |  |
| **Age (years)** | **-0.4788** | 0.0488 | ±0.0976 | **-9.813** | **9.87e-23** | *** |
| BMI (kg/m2) | -0.0306 | 0.0806 | ±0.1613 | -0.379 | 0.7045 |  |
| Hypertension | -0.7945 | 1.2017 | ±2.4034 | -0.661 | 0.5085 |  |
| High cholesterol | -0.2534 | 1.0919 | ±2.1838 | -0.232 | 0.8165 |  |
| Kidney disease | -2.5294 | 2.0328 | ±4.0655 | -1.244 | 0.2134 |  |
| Circulatory disease | -1.4825 | 1.3534 | ±2.7068 | -1.095 | 0.2734 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **575**, R² = **0.1875**, Adj R² = **0.1717**, F-statistic = **11.81** (p = **4.91e-20**), Residual SE = **12.502** on **563** df, AIC = **4548.4**, BIC = **4600.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8006** | 6.1233 | ±12.2465 | **+7.806** | **5.88e-15** | *** |
| Education: graduate level (vs college) | -1.6668 | 1.2020 | ±2.4039 | -1.387 | 0.1655 |  |
| Education: high school or below (vs college) | +2.6906 | 2.1192 | ±4.2384 | +1.270 | 0.2042 |  |
| Site: UCSD (vs UAB) | +0.0323 | 1.4665 | ±2.9329 | +0.022 | 0.9824 |  |
| Site: UW (vs UAB) | +0.7875 | 1.2466 | ±2.4932 | +0.632 | 0.5276 |  |
| **Age (years)** | **-0.4943** | 0.0495 | ±0.0990 | **-9.990** | **1.68e-23** | *** |
| BMI (kg/m2) | -0.0445 | 0.0801 | ±0.1601 | -0.556 | 0.5780 |  |
| Hypertension | -1.0285 | 1.2153 | ±2.4307 | -0.846 | 0.3974 |  |
| High cholesterol | -0.4517 | 1.1123 | ±2.2247 | -0.406 | 0.6847 |  |
| Kidney disease | -2.6803 | 1.9832 | ±3.9663 | -1.352 | 0.1765 |  |
| Circulatory disease | -1.4220 | 1.3447 | ±2.6895 | -1.057 | 0.2903 |  |
| HbA1c (%) | +1.4541 | 0.8747 | ±1.7493 | +1.662 | 0.0964 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **575**, R² = **0.1803**, Adj R² = **0.1643**, F-statistic = **11.26** (p = **5.03e-19**), Residual SE = **12.558** on **563** df, AIC = **4553.5**, BIC = **4605.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.0837** | 5.1373 | ±10.2747 | **+10.722** | **8.00e-27** | *** |
| Education: graduate level (vs college) | -1.8639 | 1.1927 | ±2.3854 | -1.563 | 0.1181 |  |
| Education: high school or below (vs college) | +3.0811 | 2.1594 | ±4.3187 | +1.427 | 0.1536 |  |
| Site: UCSD (vs UAB) | +0.0942 | 1.4724 | ±2.9449 | +0.064 | 0.9490 |  |
| Site: UW (vs UAB) | +0.5771 | 1.2474 | ±2.4947 | +0.463 | 0.6436 |  |
| **Age (years)** | **-0.4786** | 0.0488 | ±0.0977 | **-9.802** | **1.11e-22** | *** |
| BMI (kg/m2) | -0.0304 | 0.0806 | ±0.1612 | -0.377 | 0.7063 |  |
| Hypertension | -0.7852 | 1.2201 | ±2.4401 | -0.644 | 0.5198 |  |
| High cholesterol | -0.2470 | 1.1030 | ±2.2061 | -0.224 | 0.8228 |  |
| Kidney disease | -2.5148 | 2.0430 | ±4.0860 | -1.231 | 0.2183 |  |
| Circulatory disease | -1.4807 | 1.3573 | ±2.7147 | -1.091 | 0.2753 |  |
| Mean glucose (mg/dL) | -0.0015 | 0.0246 | ±0.0492 | -0.061 | 0.9510 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **575**, R² = **0.1803**, Adj R² = **0.1643**, F-statistic = **11.26** (p = **5.03e-19**), Residual SE = **12.558** on **563** df, AIC = **4553.5**, BIC = **4605.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.2928** | 7.6301 | ±15.2602 | **+7.247** | **4.27e-13** | *** |
| Education: graduate level (vs college) | -1.8639 | 1.1927 | ±2.3854 | -1.563 | 0.1181 |  |
| Education: high school or below (vs college) | +3.0811 | 2.1594 | ±4.3187 | +1.427 | 0.1536 |  |
| Site: UCSD (vs UAB) | +0.0942 | 1.4724 | ±2.9449 | +0.064 | 0.9490 |  |
| Site: UW (vs UAB) | +0.5771 | 1.2474 | ±2.4947 | +0.463 | 0.6436 |  |
| **Age (years)** | **-0.4786** | 0.0488 | ±0.0977 | **-9.802** | **1.11e-22** | *** |
| BMI (kg/m2) | -0.0304 | 0.0806 | ±0.1612 | -0.377 | 0.7063 |  |
| Hypertension | -0.7852 | 1.2201 | ±2.4401 | -0.644 | 0.5198 |  |
| High cholesterol | -0.2470 | 1.1030 | ±2.2061 | -0.224 | 0.8228 |  |
| Kidney disease | -2.5148 | 2.0430 | ±4.0860 | -1.231 | 0.2183 |  |
| Circulatory disease | -1.4807 | 1.3573 | ±2.7147 | -1.091 | 0.2753 |  |
| GMI (%) | -0.0632 | 1.0276 | ±2.0552 | -0.061 | 0.9510 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **575**, R² = **0.1808**, Adj R² = **0.1648**, F-statistic = **11.30** (p = **4.27e-19**), Residual SE = **12.554** on **563** df, AIC = **4553.2**, BIC = **4605.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.5101** | 5.1395 | ±10.2791 | **+10.411** | **2.20e-25** | *** |
| Education: graduate level (vs college) | -1.8636 | 1.1925 | ±2.3850 | -1.563 | 0.1181 |  |
| Education: high school or below (vs college) | +2.9934 | 2.1623 | ±4.3247 | +1.384 | 0.1663 |  |
| Site: UCSD (vs UAB) | +0.0703 | 1.4651 | ±2.9302 | +0.048 | 0.9617 |  |
| Site: UW (vs UAB) | +0.5852 | 1.2450 | ±2.4899 | +0.470 | 0.6383 |  |
| **Age (years)** | **-0.4779** | 0.0490 | ±0.0980 | **-9.757** | **1.72e-22** | *** |
| BMI (kg/m2) | -0.0346 | 0.0806 | ±0.1612 | -0.429 | 0.6681 |  |
| Hypertension | -0.8774 | 1.2190 | ±2.4379 | -0.720 | 0.4716 |  |
| High cholesterol | -0.3187 | 1.1059 | ±2.2118 | -0.288 | 0.7732 |  |
| Kidney disease | -2.5778 | 2.0282 | ±4.0563 | -1.271 | 0.2037 |  |
| Circulatory disease | -1.4908 | 1.3540 | ±2.7080 | -1.101 | 0.2709 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0131 | 0.0243 | ±0.0486 | +0.541 | 0.5886 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **575**, R² = **0.1811**, Adj R² = **0.1651**, F-statistic = **11.32** (p = **3.89e-19**), Residual SE = **12.551** on **563** df, AIC = **4553.0**, BIC = **4605.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.5045** | 4.3326 | ±8.6651 | **+12.811** | **1.42e-37** | *** |
| Education: graduate level (vs college) | -1.8966 | 1.1921 | ±2.3842 | -1.591 | 0.1116 |  |
| Education: high school or below (vs college) | +3.2503 | 2.1546 | ±4.3093 | +1.509 | 0.1314 |  |
| Site: UCSD (vs UAB) | +0.0915 | 1.4804 | ±2.9608 | +0.062 | 0.9507 |  |
| Site: UW (vs UAB) | +0.4991 | 1.2536 | ±2.5072 | +0.398 | 0.6906 |  |
| **Age (years)** | **-0.4739** | 0.0491 | ±0.0983 | **-9.645** | **5.14e-22** | *** |
| BMI (kg/m2) | -0.0312 | 0.0808 | ±0.1615 | -0.386 | 0.6997 |  |
| Hypertension | -0.7051 | 1.2120 | ±2.4240 | -0.582 | 0.5607 |  |
| High cholesterol | -0.2220 | 1.0995 | ±2.1990 | -0.202 | 0.8400 |  |
| Kidney disease | -2.2326 | 2.0650 | ±4.1299 | -1.081 | 0.2796 |  |
| Circulatory disease | -1.5027 | 1.3600 | ±2.7200 | -1.105 | 0.2692 |  |
| Glucose SD, pooled (mg/dL) | -0.0349 | 0.0495 | ±0.0991 | -0.705 | 0.4809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **575**, R² = **0.1820**, Adj R² = **0.1660**, F-statistic = **11.39** (p = **2.91e-19**), Residual SE = **12.544** on **563** df, AIC = **4552.3**, BIC = **4604.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.7743** | 4.3255 | ±8.6510 | **+12.894** | **4.85e-38** | *** |
| Education: graduate level (vs college) | -1.9196 | 1.1920 | ±2.3839 | -1.610 | 0.1073 |  |
| Education: high school or below (vs college) | +3.3684 | 2.1501 | ±4.3001 | +1.567 | 0.1172 |  |
| Site: UCSD (vs UAB) | +0.1043 | 1.4773 | ±2.9546 | +0.071 | 0.9437 |  |
| Site: UW (vs UAB) | +0.4782 | 1.2497 | ±2.4994 | +0.383 | 0.7020 |  |
| **Age (years)** | **-0.4710** | 0.0490 | ±0.0979 | **-9.623** | **6.42e-22** | *** |
| BMI (kg/m2) | -0.0317 | 0.0807 | ±0.1615 | -0.393 | 0.6942 |  |
| Hypertension | -0.6728 | 1.2116 | ±2.4233 | -0.555 | 0.5787 |  |
| High cholesterol | -0.1966 | 1.0981 | ±2.1963 | -0.179 | 0.8579 |  |
| Kidney disease | -2.0890 | 2.0613 | ±4.1227 | -1.013 | 0.3109 |  |
| Circulatory disease | -1.5277 | 1.3562 | ±2.7125 | -1.126 | 0.2600 |  |
| Avg. daily SD (mg/dL) | -0.0590 | 0.0541 | ±0.1081 | -1.092 | 0.2750 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **575**, R² = **0.1816**, Adj R² = **0.1656**, F-statistic = **11.35** (p = **3.37e-19**), Residual SE = **12.548** on **563** df, AIC = **4552.6**, BIC = **4604.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.2851** | 4.4666 | ±8.9332 | **+12.601** | **2.07e-36** | *** |
| Education: graduate level (vs college) | -1.9086 | 1.1904 | ±2.3809 | -1.603 | 0.1089 |  |
| Education: high school or below (vs college) | +3.2943 | 2.1562 | ±4.3124 | +1.528 | 0.1266 |  |
| Site: UCSD (vs UAB) | +0.0985 | 1.4774 | ±2.9548 | +0.067 | 0.9469 |  |
| Site: UW (vs UAB) | +0.4582 | 1.2525 | ±2.5049 | +0.366 | 0.7145 |  |
| **Age (years)** | **-0.4702** | 0.0495 | ±0.0990 | **-9.503** | **2.05e-21** | *** |
| BMI (kg/m2) | -0.0332 | 0.0810 | ±0.1619 | -0.410 | 0.6817 |  |
| Hypertension | -0.7173 | 1.2066 | ±2.4133 | -0.594 | 0.5522 |  |
| High cholesterol | -0.2545 | 1.0937 | ±2.1873 | -0.233 | 0.8160 |  |
| Kidney disease | -2.1393 | 2.0676 | ±4.1352 | -1.035 | 0.3008 |  |
| Circulatory disease | -1.5287 | 1.3562 | ±2.7123 | -1.127 | 0.2597 |  |
| CV (%) | -0.0870 | 0.0884 | ±0.1768 | -0.984 | 0.3250 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **575**, R² = **0.1803**, Adj R² = **0.1643**, F-statistic = **11.26** (p = **5.03e-19**), Residual SE = **12.558** on **563** df, AIC = **4553.5**, BIC = **4605.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.1015** | 4.9515 | ±9.9029 | **+11.128** | **9.13e-29** | *** |
| Education: graduate level (vs college) | -1.8630 | 1.1924 | ±2.3849 | -1.562 | 0.1182 |  |
| Education: high school or below (vs college) | +3.0567 | 2.1603 | ±4.3206 | +1.415 | 0.1571 |  |
| Site: UCSD (vs UAB) | +0.0907 | 1.4701 | ±2.9402 | +0.062 | 0.9508 |  |
| Site: UW (vs UAB) | +0.5844 | 1.2496 | ±2.4992 | +0.468 | 0.6400 |  |
| **Age (years)** | **-0.4794** | 0.0493 | ±0.0987 | **-9.718** | **2.54e-22** | *** |
| BMI (kg/m2) | -0.0306 | 0.0808 | ±0.1615 | -0.378 | 0.7051 |  |
| Hypertension | -0.7994 | 1.2107 | ±2.4213 | -0.660 | 0.5091 |  |
| High cholesterol | -0.2535 | 1.0938 | ±2.1876 | -0.232 | 0.8167 |  |
| Kidney disease | -2.5488 | 2.0649 | ±4.1298 | -1.234 | 0.2171 |  |
| Circulatory disease | -1.4818 | 1.3549 | ±2.7098 | -1.094 | 0.2741 |  |
| Mean / SD ratio | -0.0271 | 0.4075 | ±0.8150 | -0.067 | 0.9469 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **575**, R² = **0.1804**, Adj R² = **0.1644**, F-statistic = **11.27** (p = **4.86e-19**), Residual SE = **12.557** on **563** df, AIC = **4553.5**, BIC = **4605.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.7065** | 4.9504 | ±9.9008 | **+11.253** | **2.24e-29** | *** |
| Education: graduate level (vs college) | -1.8597 | 1.1919 | ±2.3838 | -1.560 | 0.1187 |  |
| Education: high school or below (vs college) | +3.0005 | 2.1579 | ±4.3159 | +1.390 | 0.1644 |  |
| Site: UCSD (vs UAB) | +0.0719 | 1.4680 | ±2.9360 | +0.049 | 0.9609 |  |
| Site: UW (vs UAB) | +0.5944 | 1.2450 | ±2.4900 | +0.477 | 0.6331 |  |
| **Age (years)** | **-0.4817** | 0.0493 | ±0.0986 | **-9.769** | **1.53e-22** | *** |
| BMI (kg/m2) | -0.0306 | 0.0807 | ±0.1613 | -0.380 | 0.7041 |  |
| Hypertension | -0.8089 | 1.2080 | ±2.4160 | -0.670 | 0.5031 |  |
| High cholesterol | -0.2581 | 1.0948 | ±2.1895 | -0.236 | 0.8136 |  |
| Kidney disease | -2.6050 | 2.0599 | ±4.1198 | -1.265 | 0.2060 |  |
| Circulatory disease | -1.4746 | 1.3528 | ±2.7055 | -1.090 | 0.2757 |  |
| Avg. daily mean/SD | -0.0977 | 0.3230 | ±0.6459 | -0.302 | 0.7623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **575**, R² = **0.1816**, Adj R² = **0.1656**, F-statistic = **11.36** (p = **3.34e-19**), Residual SE = **12.548** on **563** df, AIC = **4552.6**, BIC = **4604.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.7813** | 4.9852 | ±9.9705 | **+10.588** | **3.40e-26** | *** |
| Education: graduate level (vs college) | -1.8392 | 1.1924 | ±2.3848 | -1.542 | 0.1230 |  |
| Education: high school or below (vs college) | +2.9333 | 2.1619 | ±4.3238 | +1.357 | 0.1748 |  |
| Site: UCSD (vs UAB) | +0.0395 | 1.4590 | ±2.9180 | +0.027 | 0.9784 |  |
| Site: UW (vs UAB) | +0.7214 | 1.2595 | ±2.5190 | +0.573 | 0.5668 |  |
| **Age (years)** | **-0.4791** | 0.0488 | ±0.0975 | **-9.822** | **9.01e-23** | *** |
| BMI (kg/m2) | -0.0324 | 0.0805 | ±0.1610 | -0.403 | 0.6871 |  |
| Hypertension | -0.8437 | 1.2065 | ±2.4129 | -0.699 | 0.4843 |  |
| High cholesterol | -0.2392 | 1.0916 | ±2.1832 | -0.219 | 0.8265 |  |
| Kidney disease | -2.6047 | 2.0426 | ±4.0852 | -1.275 | 0.2022 |  |
| Circulatory disease | -1.4705 | 1.3527 | ±2.7053 | -1.087 | 0.2770 |  |
| MAG (mg/dL/h) | +0.0532 | 0.0626 | ±0.1251 | +0.850 | 0.3953 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **575**, R² = **0.1811**, Adj R² = **0.1651**, F-statistic = **11.32** (p = **3.86e-19**), Residual SE = **12.551** on **563** df, AIC = **4552.9**, BIC = **4605.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.8812** | 4.4955 | ±8.9910 | **+12.430** | **1.79e-35** | *** |
| Education: graduate level (vs college) | -1.9044 | 1.1938 | ±2.3876 | -1.595 | 0.1107 |  |
| Education: high school or below (vs college) | +3.2778 | 2.1556 | ±4.3112 | +1.521 | 0.1284 |  |
| Site: UCSD (vs UAB) | +0.1155 | 1.4726 | ±2.9452 | +0.078 | 0.9375 |  |
| Site: UW (vs UAB) | +0.5140 | 1.2521 | ±2.5043 | +0.411 | 0.6814 |  |
| **Age (years)** | **-0.4739** | 0.0490 | ±0.0980 | **-9.671** | **3.99e-22** | *** |
| BMI (kg/m2) | -0.0333 | 0.0811 | ±0.1623 | -0.411 | 0.6812 |  |
| Hypertension | -0.7248 | 1.2100 | ±2.4199 | -0.599 | 0.5492 |  |
| High cholesterol | -0.2182 | 1.0982 | ±2.1965 | -0.199 | 0.8425 |  |
| Kidney disease | -2.2471 | 2.0540 | ±4.1081 | -1.094 | 0.2739 |  |
| Circulatory disease | -1.4945 | 1.3564 | ±2.7129 | -1.102 | 0.2706 |  |
| Avg. daily range (mg/dL) | -0.0109 | 0.0148 | ±0.0296 | -0.735 | 0.4622 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **575**, R² = **0.1807**, Adj R² = **0.1647**, F-statistic = **11.29** (p = **4.39e-19**), Residual SE = **12.554** on **563** df, AIC = **4553.2**, BIC = **4605.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.6429** | 4.2843 | ±8.5687 | **+12.754** | **2.96e-37** | *** |
| Education: graduate level (vs college) | -1.8399 | 1.1970 | ±2.3939 | -1.537 | 0.1243 |  |
| Education: high school or below (vs college) | +3.0472 | 2.1592 | ±4.3184 | +1.411 | 0.1582 |  |
| Site: UCSD (vs UAB) | +0.1167 | 1.4810 | ±2.9620 | +0.079 | 0.9372 |  |
| Site: UW (vs UAB) | +0.6297 | 1.2582 | ±2.5163 | +0.500 | 0.6167 |  |
| **Age (years)** | **-0.4801** | 0.0489 | ±0.0978 | **-9.823** | **9.00e-23** | *** |
| BMI (kg/m2) | -0.0308 | 0.0808 | ±0.1615 | -0.382 | 0.7027 |  |
| Hypertension | -0.8569 | 1.2128 | ±2.4255 | -0.707 | 0.4799 |  |
| High cholesterol | -0.2666 | 1.0971 | ±2.1942 | -0.243 | 0.8080 |  |
| Kidney disease | -2.6562 | 2.0493 | ±4.0986 | -1.296 | 0.1949 |  |
| Circulatory disease | -1.5070 | 1.3530 | ±2.7060 | -1.114 | 0.2653 |  |
| SD of daily means (mg/dL) | +0.0429 | 0.0942 | ±0.1885 | +0.455 | 0.6491 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **575**, R² = **0.1808**, Adj R² = **0.1648**, F-statistic = **11.30** (p = **4.24e-19**), Residual SE = **12.554** on **563** df, AIC = **4553.2**, BIC = **4605.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4501** | 5.7407 | ±11.4815 | **+9.136** | **6.45e-20** | *** |
| Education: graduate level (vs college) | -1.9052 | 1.1963 | ±2.3926 | -1.593 | 0.1113 |  |
| Education: high school or below (vs college) | +3.1492 | 2.1635 | ±4.3271 | +1.456 | 0.1455 |  |
| Site: UCSD (vs UAB) | +0.0627 | 1.4979 | ±2.9958 | +0.042 | 0.9666 |  |
| Site: UW (vs UAB) | +0.5037 | 1.2548 | ±2.5096 | +0.401 | 0.6881 |  |
| **Age (years)** | **-0.4770** | 0.0488 | ±0.0976 | **-9.778** | **1.40e-22** | *** |
| BMI (kg/m2) | -0.0303 | 0.0808 | ±0.1616 | -0.375 | 0.7073 |  |
| Hypertension | -0.7452 | 1.2067 | ±2.4135 | -0.618 | 0.5369 |  |
| High cholesterol | -0.2113 | 1.1011 | ±2.2022 | -0.192 | 0.8478 |  |
| Kidney disease | -2.3427 | 2.0699 | ±4.1399 | -1.132 | 0.2577 |  |
| Circulatory disease | -1.4691 | 1.3613 | ±2.7227 | -1.079 | 0.2805 |  |
| Time in range 70-180, pooled (%) | +0.0256 | 0.0466 | ±0.0931 | +0.550 | 0.5820 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **575**, R² = **0.1808**, Adj R² = **0.1648**, F-statistic = **11.30** (p = **4.27e-19**), Residual SE = **12.554** on **563** df, AIC = **4553.2**, BIC = **4605.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4969** | 5.7635 | ±11.5269 | **+9.109** | **8.35e-20** | *** |
| Education: graduate level (vs college) | -1.9054 | 1.1962 | ±2.3924 | -1.593 | 0.1112 |  |
| Education: high school or below (vs college) | +3.1517 | 2.1631 | ±4.3262 | +1.457 | 0.1451 |  |
| Site: UCSD (vs UAB) | +0.0632 | 1.4967 | ±2.9933 | +0.042 | 0.9663 |  |
| Site: UW (vs UAB) | +0.5041 | 1.2546 | ±2.5091 | +0.402 | 0.6878 |  |
| **Age (years)** | **-0.4770** | 0.0488 | ±0.0976 | **-9.776** | **1.43e-22** | *** |
| BMI (kg/m2) | -0.0304 | 0.0808 | ±0.1616 | -0.376 | 0.7067 |  |
| Hypertension | -0.7480 | 1.2063 | ±2.4127 | -0.620 | 0.5352 |  |
| High cholesterol | -0.2098 | 1.1028 | ±2.2056 | -0.190 | 0.8491 |  |
| Kidney disease | -2.3447 | 2.0675 | ±4.1349 | -1.134 | 0.2568 |  |
| Circulatory disease | -1.4689 | 1.3613 | ±2.7226 | -1.079 | 0.2806 |  |
| Avg. daily time in range 70-180 (%) | +0.0250 | 0.0462 | ±0.0923 | +0.541 | 0.5884 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **575**, R² = **0.1815**, Adj R² = **0.1655**, F-statistic = **11.35** (p = **3.42e-19**), Residual SE = **12.548** on **563** df, AIC = **4552.7**, BIC = **4604.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.3254** | 4.2465 | ±8.4930 | **+13.028** | **8.43e-39** | *** |
| Education: graduate level (vs college) | -1.8906 | 1.1916 | ±2.3831 | -1.587 | 0.1126 |  |
| Education: high school or below (vs college) | +2.9932 | 2.1573 | ±4.3145 | +1.388 | 0.1653 |  |
| Site: UCSD (vs UAB) | -0.0855 | 1.4967 | ±2.9934 | -0.057 | 0.9544 |  |
| Site: UW (vs UAB) | +0.4273 | 1.2510 | ±2.5021 | +0.342 | 0.7327 |  |
| **Age (years)** | **-0.4781** | 0.0488 | ±0.0976 | **-9.802** | **1.11e-22** | *** |
| BMI (kg/m2) | -0.0320 | 0.0809 | ±0.1617 | -0.396 | 0.6923 |  |
| Hypertension | -0.8392 | 1.2019 | ±2.4037 | -0.698 | 0.4850 |  |
| High cholesterol | -0.3253 | 1.0957 | ±2.1914 | -0.297 | 0.7666 |  |
| Kidney disease | -2.4960 | 2.0295 | ±4.0591 | -1.230 | 0.2188 |  |
| Circulatory disease | -1.4738 | 1.3556 | ±2.7113 | -1.087 | 0.2770 |  |
| Time < 54 (%) | -0.5354 | 0.3859 | ±0.7718 | -1.387 | 0.1654 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **575**, R² = **0.1821**, Adj R² = **0.1662**, F-statistic = **11.40** (p = **2.78e-19**), Residual SE = **12.543** on **563** df, AIC = **4552.2**, BIC = **4604.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.1893** | 4.2192 | ±8.4385 | **+13.080** | **4.26e-39** | *** |
| Education: graduate level (vs college) | -1.9294 | 1.1953 | ±2.3905 | -1.614 | 0.1065 |  |
| Education: high school or below (vs college) | +2.9696 | 2.1563 | ±4.3125 | +1.377 | 0.1684 |  |
| Site: UCSD (vs UAB) | -0.0951 | 1.4951 | ±2.9901 | -0.064 | 0.9493 |  |
| Site: UW (vs UAB) | +0.3731 | 1.2534 | ±2.5067 | +0.298 | 0.7659 |  |
| **Age (years)** | **-0.4754** | 0.0488 | ±0.0976 | **-9.740** | **2.03e-22** | *** |
| BMI (kg/m2) | -0.0318 | 0.0808 | ±0.1616 | -0.393 | 0.6940 |  |
| Hypertension | -0.8506 | 1.2013 | ±2.4026 | -0.708 | 0.4789 |  |
| High cholesterol | -0.3483 | 1.0934 | ±2.1867 | -0.319 | 0.7501 |  |
| Kidney disease | -2.4713 | 2.0280 | ±4.0561 | -1.219 | 0.2230 |  |
| Circulatory disease | -1.4644 | 1.3540 | ±2.7080 | -1.082 | 0.2795 |  |
| Avg. daily time < 54 (%) | -0.7683 | 0.5185 | ±1.0370 | -1.482 | 0.1384 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **575**, R² = **0.1808**, Adj R² = **0.1648**, F-statistic = **11.30** (p = **4.25e-19**), Residual SE = **12.554** on **563** df, AIC = **4553.2**, BIC = **4605.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.1634** | 4.2325 | ±8.4650 | **+13.033** | **7.91e-39** | *** |
| Education: graduate level (vs college) | -1.9108 | 1.1911 | ±2.3821 | -1.604 | 0.1087 |  |
| Education: high school or below (vs college) | +3.0738 | 2.1644 | ±4.3288 | +1.420 | 0.1556 |  |
| Site: UCSD (vs UAB) | +0.0245 | 1.4689 | ±2.9378 | +0.017 | 0.9867 |  |
| Site: UW (vs UAB) | +0.4995 | 1.2368 | ±2.4735 | +0.404 | 0.6863 |  |
| **Age (years)** | **-0.4776** | 0.0488 | ±0.0977 | **-9.779** | **1.38e-22** | *** |
| BMI (kg/m2) | -0.0308 | 0.0812 | ±0.1625 | -0.379 | 0.7049 |  |
| Hypertension | -0.8309 | 1.2087 | ±2.4174 | -0.687 | 0.4918 |  |
| High cholesterol | -0.2802 | 1.0946 | ±2.1891 | -0.256 | 0.7979 |  |
| Kidney disease | -2.5022 | 2.0326 | ±4.0652 | -1.231 | 0.2183 |  |
| Circulatory disease | -1.5054 | 1.3538 | ±2.7076 | -1.112 | 0.2662 |  |
| Time 54-69, pooled (%) | -0.1380 | 0.2140 | ±0.4280 | -0.645 | 0.5191 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **575**, R² = **0.1809**, Adj R² = **0.1649**, F-statistic = **11.31** (p = **4.10e-19**), Residual SE = **12.553** on **563** df, AIC = **4553.1**, BIC = **4605.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.1087** | 4.2172 | ±8.4345 | **+13.067** | **5.05e-39** | *** |
| Education: graduate level (vs college) | -1.9184 | 1.1910 | ±2.3820 | -1.611 | 0.1072 |  |
| Education: high school or below (vs college) | +3.0760 | 2.1656 | ±4.3311 | +1.420 | 0.1555 |  |
| Site: UCSD (vs UAB) | +0.0285 | 1.4681 | ±2.9362 | +0.019 | 0.9845 |  |
| Site: UW (vs UAB) | +0.4870 | 1.2374 | ±2.4748 | +0.394 | 0.6939 |  |
| **Age (years)** | **-0.4767** | 0.0489 | ±0.0978 | **-9.749** | **1.87e-22** | *** |
| BMI (kg/m2) | -0.0307 | 0.0812 | ±0.1624 | -0.378 | 0.7057 |  |
| Hypertension | -0.8314 | 1.2088 | ±2.4177 | -0.688 | 0.4916 |  |
| High cholesterol | -0.2804 | 1.0936 | ±2.1873 | -0.256 | 0.7976 |  |
| Kidney disease | -2.5004 | 2.0316 | ±4.0632 | -1.231 | 0.2184 |  |
| Circulatory disease | -1.5063 | 1.3530 | ±2.7060 | -1.113 | 0.2656 |  |
| Avg. daily time 54-69 (%) | -0.1456 | 0.2073 | ±0.4145 | -0.702 | 0.4825 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **575**, R² = **0.1812**, Adj R² = **0.1652**, F-statistic = **11.32** (p = **3.82e-19**), Residual SE = **12.551** on **563** df, AIC = **4552.9**, BIC = **4605.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.2768** | 4.2474 | ±8.4949 | **+13.014** | **1.02e-38** | *** |
| Education: graduate level (vs college) | -1.9192 | 1.1915 | ±2.3829 | -1.611 | 0.1072 |  |
| Education: high school or below (vs college) | +3.0531 | 2.1625 | ±4.3251 | +1.412 | 0.1580 |  |
| Site: UCSD (vs UAB) | -0.0247 | 1.4746 | ±2.9492 | -0.017 | 0.9867 |  |
| Site: UW (vs UAB) | +0.4570 | 1.2393 | ±2.4785 | +0.369 | 0.7123 |  |
| **Age (years)** | **-0.4774** | 0.0488 | ±0.0976 | **-9.781** | **1.35e-22** | *** |
| BMI (kg/m2) | -0.0311 | 0.0813 | ±0.1625 | -0.383 | 0.7015 |  |
| Hypertension | -0.8438 | 1.2079 | ±2.4157 | -0.699 | 0.4848 |  |
| High cholesterol | -0.3000 | 1.0954 | ±2.1907 | -0.274 | 0.7842 |  |
| Kidney disease | -2.4926 | 2.0310 | ±4.0619 | -1.227 | 0.2197 |  |
| Circulatory disease | -1.5037 | 1.3545 | ±2.7091 | -1.110 | 0.2669 |  |
| Time < 70 (%) | -0.1418 | 0.1647 | ±0.3295 | -0.861 | 0.3893 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **575**, R² = **0.1813**, Adj R² = **0.1653**, F-statistic = **11.34** (p = **3.61e-19**), Residual SE = **12.550** on **563** df, AIC = **4552.8**, BIC = **4605.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.1705** | 4.2230 | ±8.4459 | **+13.064** | **5.26e-39** | *** |
| Education: graduate level (vs college) | -1.9341 | 1.1921 | ±2.3843 | -1.622 | 0.1047 |  |
| Education: high school or below (vs college) | +3.0561 | 2.1635 | ±4.3270 | +1.413 | 0.1578 |  |
| Site: UCSD (vs UAB) | -0.0119 | 1.4720 | ±2.9440 | -0.008 | 0.9936 |  |
| Site: UW (vs UAB) | +0.4416 | 1.2398 | ±2.4797 | +0.356 | 0.7217 |  |
| **Age (years)** | **-0.4760** | 0.0489 | ±0.0978 | **-9.738** | **2.08e-22** | *** |
| BMI (kg/m2) | -0.0309 | 0.0812 | ±0.1625 | -0.381 | 0.7035 |  |
| Hypertension | -0.8443 | 1.2080 | ±2.4160 | -0.699 | 0.4846 |  |
| High cholesterol | -0.3005 | 1.0937 | ±2.1873 | -0.275 | 0.7835 |  |
| Kidney disease | -2.4875 | 2.0301 | ±4.0602 | -1.225 | 0.2205 |  |
| Circulatory disease | -1.5038 | 1.3530 | ±2.7060 | -1.111 | 0.2664 |  |
| Avg. daily time < 70 (%) | -0.1525 | 0.1660 | ±0.3321 | -0.918 | 0.3584 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **575**, R² = **0.1809**, Adj R² = **0.1649**, F-statistic = **11.30** (p = **4.19e-19**), Residual SE = **12.553** on **563** df, AIC = **4553.1**, BIC = **4605.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3208** | 11.2931 | ±22.5862 | **+4.367** | **1.26e-05** | *** |
| Education: graduate level (vs college) | -1.9006 | 1.1926 | ±2.3852 | -1.594 | 0.1110 |  |
| Education: high school or below (vs college) | +3.1451 | 2.1640 | ±4.3280 | +1.453 | 0.1461 |  |
| Site: UCSD (vs UAB) | +0.0510 | 1.4972 | ±2.9943 | +0.034 | 0.9728 |  |
| Site: UW (vs UAB) | +0.5015 | 1.2522 | ±2.5044 | +0.400 | 0.6888 |  |
| **Age (years)** | **-0.4788** | 0.0488 | ±0.0977 | **-9.804** | **1.08e-22** | *** |
| BMI (kg/m2) | -0.0313 | 0.0807 | ±0.1614 | -0.387 | 0.6985 |  |
| Hypertension | -0.7593 | 1.2011 | ±2.4022 | -0.632 | 0.5272 |  |
| High cholesterol | -0.2651 | 1.0939 | ±2.1879 | -0.242 | 0.8086 |  |
| Kidney disease | -2.4294 | 2.0410 | ±4.0820 | -1.190 | 0.2339 |  |
| Circulatory disease | -1.4512 | 1.3652 | ±2.7304 | -1.063 | 0.2878 |  |
| Time 54-250, pooled (%) | +0.0574 | 0.1090 | ±0.2180 | +0.527 | 0.5984 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **575**, R² = **0.1804**, Adj R² = **0.1644**, F-statistic = **11.27** (p = **4.84e-19**), Residual SE = **12.557** on **563** df, AIC = **4553.4**, BIC = **4605.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.0011** | 12.2963 | ±24.5926 | **+4.229** | **2.35e-05** | *** |
| Education: graduate level (vs college) | -1.8831 | 1.1941 | ±2.3882 | -1.577 | 0.1148 |  |
| Education: high school or below (vs college) | +3.1108 | 2.1601 | ±4.3202 | +1.440 | 0.1498 |  |
| Site: UCSD (vs UAB) | +0.0757 | 1.4930 | ±2.9860 | +0.051 | 0.9596 |  |
| Site: UW (vs UAB) | +0.5440 | 1.2515 | ±2.5030 | +0.435 | 0.6638 |  |
| **Age (years)** | **-0.4786** | 0.0488 | ±0.0977 | **-9.798** | **1.15e-22** | *** |
| BMI (kg/m2) | -0.0310 | 0.0808 | ±0.1616 | -0.384 | 0.7008 |  |
| Hypertension | -0.7782 | 1.2029 | ±2.4059 | -0.647 | 0.5177 |  |
| High cholesterol | -0.2572 | 1.0947 | ±2.1894 | -0.235 | 0.8143 |  |
| Kidney disease | -2.4745 | 2.0392 | ±4.0784 | -1.213 | 0.2250 |  |
| Circulatory disease | -1.4647 | 1.3655 | ±2.7309 | -1.073 | 0.2834 |  |
| Avg. daily time 54-250 (%) | +0.0297 | 0.1192 | ±0.2385 | +0.249 | 0.8030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **575**, R² = **0.1804**, Adj R² = **0.1644**, F-statistic = **11.27** (p = **4.83e-19**), Residual SE = **12.557** on **563** df, AIC = **4553.4**, BIC = **4605.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9106** | 4.1966 | ±8.3932 | **+13.084** | **4.04e-39** | *** |
| Education: graduate level (vs college) | -1.8752 | 1.1956 | ±2.3911 | -1.569 | 0.1168 |  |
| Education: high school or below (vs college) | +3.1033 | 2.1593 | ±4.3187 | +1.437 | 0.1507 |  |
| Site: UCSD (vs UAB) | +0.0938 | 1.4798 | ±2.9596 | +0.063 | 0.9495 |  |
| Site: UW (vs UAB) | +0.5606 | 1.2499 | ±2.4998 | +0.449 | 0.6538 |  |
| **Age (years)** | **-0.4777** | 0.0487 | ±0.0975 | **-9.800** | **1.13e-22** | *** |
| BMI (kg/m2) | -0.0302 | 0.0807 | ±0.1614 | -0.374 | 0.7085 |  |
| Hypertension | -0.7656 | 1.2139 | ±2.4279 | -0.631 | 0.5283 |  |
| High cholesterol | -0.2159 | 1.1083 | ±2.2167 | -0.195 | 0.8456 |  |
| Kidney disease | -2.4311 | 2.0807 | ±4.1614 | -1.168 | 0.2426 |  |
| Circulatory disease | -1.4798 | 1.3584 | ±2.7169 | -1.089 | 0.2760 |  |
| Time 181-250, pooled (%) | -0.0184 | 0.0662 | ±0.1324 | -0.278 | 0.7813 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **575**, R² = **0.1806**, Adj R² = **0.1646**, F-statistic = **11.28** (p = **4.50e-19**), Residual SE = **12.555** on **563** df, AIC = **4553.3**, BIC = **4605.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9177** | 4.2006 | ±8.4013 | **+13.074** | **4.66e-39** | *** |
| Education: graduate level (vs college) | -1.8822 | 1.1943 | ±2.3887 | -1.576 | 0.1150 |  |
| Education: high school or below (vs college) | +3.1255 | 2.1598 | ±4.3195 | +1.447 | 0.1479 |  |
| Site: UCSD (vs UAB) | +0.0881 | 1.4841 | ±2.9682 | +0.059 | 0.9527 |  |
| Site: UW (vs UAB) | +0.5447 | 1.2503 | ±2.5007 | +0.436 | 0.6631 |  |
| **Age (years)** | **-0.4772** | 0.0487 | ±0.0975 | **-9.791** | **1.23e-22** | *** |
| BMI (kg/m2) | -0.0299 | 0.0807 | ±0.1613 | -0.371 | 0.7109 |  |
| Hypertension | -0.7489 | 1.2115 | ±2.4230 | -0.618 | 0.5365 |  |
| High cholesterol | -0.1934 | 1.1087 | ±2.2174 | -0.174 | 0.8615 |  |
| Kidney disease | -2.3735 | 2.0761 | ±4.1522 | -1.143 | 0.2529 |  |
| Circulatory disease | -1.4793 | 1.3588 | ±2.7175 | -1.089 | 0.2763 |  |
| Avg. daily time 181-250 (%) | -0.0291 | 0.0631 | ±0.1263 | -0.461 | 0.6445 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **575**, R² = **0.1806**, Adj R² = **0.1645**, F-statistic = **11.28** (p = **4.62e-19**), Residual SE = **12.556** on **563** df, AIC = **4553.3**, BIC = **4605.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9413** | 4.2075 | ±8.4151 | **+13.058** | **5.73e-39** | *** |
| Education: graduate level (vs college) | -1.8859 | 1.1954 | ±2.3908 | -1.578 | 0.1146 |  |
| Education: high school or below (vs college) | +3.1290 | 2.1593 | ±4.3186 | +1.449 | 0.1473 |  |
| Site: UCSD (vs UAB) | +0.0866 | 1.4860 | ±2.9719 | +0.058 | 0.9536 |  |
| Site: UW (vs UAB) | +0.5413 | 1.2516 | ±2.5033 | +0.432 | 0.6654 |  |
| **Age (years)** | **-0.4777** | 0.0488 | ±0.0976 | **-9.789** | **1.25e-22** | *** |
| BMI (kg/m2) | -0.0303 | 0.0807 | ±0.1615 | -0.376 | 0.7071 |  |
| Hypertension | -0.7532 | 1.2096 | ±2.4193 | -0.623 | 0.5335 |  |
| High cholesterol | -0.2175 | 1.1033 | ±2.2066 | -0.197 | 0.8437 |  |
| Kidney disease | -2.4015 | 2.0664 | ±4.1328 | -1.162 | 0.2452 |  |
| Circulatory disease | -1.4702 | 1.3605 | ±2.7209 | -1.081 | 0.2798 |  |
| Time > 180 (%) | -0.0182 | 0.0471 | ±0.0942 | -0.386 | 0.6993 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **575**, R² = **0.1805**, Adj R² = **0.1645**, F-statistic = **11.27** (p = **4.67e-19**), Residual SE = **12.556** on **563** df, AIC = **4553.4**, BIC = **4605.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9439** | 4.2080 | ±8.4161 | **+13.057** | **5.80e-39** | *** |
| Education: graduate level (vs college) | -1.8842 | 1.1951 | ±2.3903 | -1.577 | 0.1149 |  |
| Education: high school or below (vs college) | +3.1277 | 2.1582 | ±4.3164 | +1.449 | 0.1473 |  |
| Site: UCSD (vs UAB) | +0.0844 | 1.4871 | ±2.9742 | +0.057 | 0.9547 |  |
| Site: UW (vs UAB) | +0.5435 | 1.2514 | ±2.5028 | +0.434 | 0.6641 |  |
| **Age (years)** | **-0.4778** | 0.0488 | ±0.0976 | **-9.794** | **1.20e-22** | *** |
| BMI (kg/m2) | -0.0304 | 0.0807 | ±0.1615 | -0.377 | 0.7063 |  |
| Hypertension | -0.7573 | 1.2090 | ±2.4181 | -0.626 | 0.5311 |  |
| High cholesterol | -0.2185 | 1.1045 | ±2.2091 | -0.198 | 0.8432 |  |
| Kidney disease | -2.4084 | 2.0637 | ±4.1273 | -1.167 | 0.2432 |  |
| Circulatory disease | -1.4709 | 1.3605 | ±2.7211 | -1.081 | 0.2796 |  |
| Avg. daily time > 180 (%) | -0.0170 | 0.0468 | ±0.0937 | -0.363 | 0.7169 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **575**, R² = **0.1806**, Adj R² = **0.1646**, F-statistic = **11.28** (p = **4.54e-19**), Residual SE = **12.555** on **563** df, AIC = **4553.3**, BIC = **4605.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9348** | 4.2059 | ±8.4118 | **+13.061** | **5.47e-39** | *** |
| Education: graduate level (vs college) | -1.8902 | 1.1931 | ±2.3862 | -1.584 | 0.1131 |  |
| Education: high school or below (vs college) | +3.1102 | 2.1646 | ±4.3291 | +1.437 | 0.1508 |  |
| Site: UCSD (vs UAB) | +0.0818 | 1.4929 | ±2.9858 | +0.055 | 0.9563 |  |
| Site: UW (vs UAB) | +0.5462 | 1.2491 | ±2.4982 | +0.437 | 0.6619 |  |
| **Age (years)** | **-0.4786** | 0.0488 | ±0.0977 | **-9.801** | **1.12e-22** | *** |
| BMI (kg/m2) | -0.0293 | 0.0806 | ±0.1611 | -0.364 | 0.7160 |  |
| Hypertension | -0.7435 | 1.2077 | ±2.4153 | -0.616 | 0.5381 |  |
| High cholesterol | -0.2202 | 1.1034 | ±2.2068 | -0.200 | 0.8419 |  |
| Kidney disease | -2.4633 | 2.0480 | ±4.0960 | -1.203 | 0.2291 |  |
| Circulatory disease | -1.4624 | 1.3621 | ±2.7242 | -1.074 | 0.2830 |  |
| Nocturnal time > 180 (%) | -0.0203 | 0.0513 | ±0.1026 | -0.395 | 0.6927 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **575**, R² = **0.1806**, Adj R² = **0.1646**, F-statistic = **11.28** (p = **4.51e-19**), Residual SE = **12.555** on **563** df, AIC = **4553.3**, BIC = **4605.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.8910** | 4.2099 | ±8.4198 | **+13.039** | **7.38e-39** | *** |
| Education: graduate level (vs college) | -1.8306 | 1.1992 | ±2.3984 | -1.527 | 0.1269 |  |
| Education: high school or below (vs college) | +3.0156 | 2.1632 | ±4.3264 | +1.394 | 0.1633 |  |
| Site: UCSD (vs UAB) | +0.0597 | 1.4561 | ±2.9121 | +0.041 | 0.9673 |  |
| Site: UW (vs UAB) | +0.5976 | 1.2475 | ±2.4951 | +0.479 | 0.6319 |  |
| **Age (years)** | **-0.4813** | 0.0486 | ±0.0973 | **-9.895** | **4.36e-23** | *** |
| BMI (kg/m2) | -0.0286 | 0.0816 | ±0.1632 | -0.351 | 0.7258 |  |
| Hypertension | -0.8548 | 1.2217 | ±2.4435 | -0.700 | 0.4841 |  |
| High cholesterol | -0.2876 | 1.1032 | ±2.2064 | -0.261 | 0.7943 |  |
| Kidney disease | -2.6669 | 2.0755 | ±4.1510 | -1.285 | 0.1988 |  |
| Circulatory disease | -1.4683 | 1.3544 | ±2.7088 | -1.084 | 0.2783 |  |
| Any reading > 250 during wear (0/1) | +0.5963 | 1.3052 | ±2.6105 | +0.457 | 0.6478 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **575**, R² = **0.1806**, Adj R² = **0.1646**, F-statistic = **11.28** (p = **4.50e-19**), Residual SE = **12.555** on **563** df, AIC = **4553.3**, BIC = **4605.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9994** | 4.2072 | ±8.4144 | **+13.073** | **4.71e-39** | *** |
| Education: graduate level (vs college) | -1.8909 | 1.1924 | ±2.3848 | -1.586 | 0.1128 |  |
| Education: high school or below (vs college) | +3.1370 | 2.1626 | ±4.3251 | +1.451 | 0.1469 |  |
| Site: UCSD (vs UAB) | +0.0748 | 1.4885 | ±2.9771 | +0.050 | 0.9599 |  |
| Site: UW (vs UAB) | +0.5301 | 1.2490 | ±2.4981 | +0.424 | 0.6713 |  |
| **Age (years)** | **-0.4788** | 0.0488 | ±0.0977 | **-9.804** | **1.09e-22** | *** |
| BMI (kg/m2) | -0.0310 | 0.0807 | ±0.1614 | -0.384 | 0.7009 |  |
| Hypertension | -0.7626 | 1.2018 | ±2.4037 | -0.635 | 0.5257 |  |
| High cholesterol | -0.2566 | 1.0949 | ±2.1898 | -0.234 | 0.8147 |  |
| Kidney disease | -2.4523 | 2.0408 | ±4.0815 | -1.202 | 0.2295 |  |
| Circulatory disease | -1.4582 | 1.3645 | ±2.7291 | -1.069 | 0.2852 |  |
| Time > 250 (%) | -0.0459 | 0.1115 | ±0.2230 | -0.412 | 0.6807 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 575)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **575**, R² = **0.1803**, Adj R² = **0.1643**, F-statistic = **11.26** (p = **5.00e-19**), Residual SE = **12.558** on **563** df, AIC = **4553.5**, BIC = **4605.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.9412** | 4.2089 | ±8.4177 | **+13.054** | **6.05e-39** | *** |
| Education: graduate level (vs college) | -1.8711 | 1.1934 | ±2.3868 | -1.568 | 0.1169 |  |
| Education: high school or below (vs college) | +3.0905 | 2.1571 | ±4.3143 | +1.433 | 0.1519 |  |
| Site: UCSD (vs UAB) | +0.0886 | 1.4855 | ±2.9711 | +0.060 | 0.9525 |  |
| Site: UW (vs UAB) | +0.5672 | 1.2484 | ±2.4969 | +0.454 | 0.6496 |  |
| **Age (years)** | **-0.4787** | 0.0488 | ±0.0977 | **-9.800** | **1.12e-22** | *** |
| BMI (kg/m2) | -0.0308 | 0.0808 | ±0.1616 | -0.381 | 0.7034 |  |
| Hypertension | -0.7864 | 1.2038 | ±2.4075 | -0.653 | 0.5136 |  |
| High cholesterol | -0.2534 | 1.0956 | ±2.1911 | -0.231 | 0.8171 |  |
| Kidney disease | -2.5062 | 2.0373 | ±4.0747 | -1.230 | 0.2187 |  |
| Circulatory disease | -1.4750 | 1.3643 | ±2.7287 | -1.081 | 0.2797 |  |
| Avg. daily time > 250 (%) | -0.0131 | 0.1205 | ±0.2410 | -0.109 | 0.9134 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 576; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **576**, R² = **0.1842**, Adj R² = **0.1698**, F-statistic = **12.76** (p = **3.49e-20**), Residual SE = **7.926** on **565** df, AIC = **4030.4**, BIC = **4078.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4532** | 2.6221 | ±5.2442 | **+26.488** | **1.34e-154** | *** |
| Education: graduate level (vs college) | -1.2153 | 0.7312 | ±1.4624 | -1.662 | 0.0965 | . |
| Education: high school or below (vs college) | -0.2904 | 1.2064 | ±2.4127 | -0.241 | 0.8097 |  |
| **Site: UCSD (vs UAB)** | **-2.5191** | 0.9408 | ±1.8815 | **-2.678** | **0.0074** | ** |
| **Site: UW (vs UAB)** | **-3.0730** | 0.7943 | ±1.5886 | **-3.869** | **1.09e-04** | *** |
| **Age (years)** | **-0.1882** | 0.0308 | ±0.0616 | **-6.107** | **1.01e-09** | *** |
| **BMI (kg/m2)** | **+0.1985** | 0.0489 | ±0.0977 | **+4.062** | **4.86e-05** | *** |
| Hypertension | +1.3386 | 0.7535 | ±1.5070 | +1.776 | 0.0757 | . |
| High cholesterol | +0.2025 | 0.7075 | ±1.4150 | +0.286 | 0.7747 |  |
| Kidney disease | +0.9985 | 1.3696 | ±2.7391 | +0.729 | 0.4660 |  |
| Circulatory disease | -0.4305 | 0.9073 | ±1.8146 | -0.475 | 0.6351 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **576**, R² = **0.1989**, Adj R² = **0.1832**, F-statistic = **12.73** (p = **1.11e-21**), Residual SE = **7.862** on **564** df, AIC = **4022.0**, BIC = **4074.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.0921** | 3.6648 | ±7.3296 | **+17.216** | **2.02e-66** | *** |
| Education: graduate level (vs college) | -1.0349 | 0.7331 | ±1.4662 | -1.412 | 0.1580 |  |
| Education: high school or below (vs college) | -0.6931 | 1.1694 | ±2.3387 | -0.593 | 0.5534 |  |
| **Site: UCSD (vs UAB)** | **-2.6093** | 0.9338 | ±1.8676 | **-2.794** | **0.0052** | ** |
| **Site: UW (vs UAB)** | **-2.8883** | 0.7906 | ±1.5812 | **-3.653** | **2.59e-04** | *** |
| **Age (years)** | **-0.2017** | 0.0306 | ±0.0611 | **-6.602** | **4.06e-11** | *** |
| **BMI (kg/m2)** | **+0.1859** | 0.0480 | ±0.0960 | **+3.872** | **1.08e-04** | *** |
| Hypertension | +1.1147 | 0.7536 | ±1.5072 | +1.479 | 0.1391 |  |
| High cholesterol | +0.0344 | 0.7079 | ±1.4158 | +0.049 | 0.9612 |  |
| Kidney disease | +0.8663 | 1.3390 | ±2.6780 | +0.647 | 0.5176 |  |
| Circulatory disease | -0.3595 | 0.9062 | ±1.8124 | -0.397 | 0.6916 |  |
| **HbA1c (%)** | **+1.2969** | 0.5092 | ±1.0183 | **+2.547** | **0.0109** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **576**, R² = **0.1950**, Adj R² = **0.1793**, F-statistic = **12.42** (p = **3.91e-21**), Residual SE = **7.881** on **564** df, AIC = **4024.7**, BIC = **4077.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.4124** | 3.1378 | ±6.2757 | **+20.846** | **1.64e-96** | *** |
| Education: graduate level (vs college) | -1.2003 | 0.7319 | ±1.4637 | -1.640 | 0.1010 |  |
| Education: high school or below (vs college) | -0.5970 | 1.1784 | ±2.3569 | -0.507 | 0.6124 |  |
| **Site: UCSD (vs UAB)** | **-2.5832** | 0.9338 | ±1.8677 | **-2.766** | **0.0057** | ** |
| **Site: UW (vs UAB)** | **-3.0221** | 0.7871 | ±1.5742 | **-3.840** | **1.23e-04** | *** |
| **Age (years)** | **-0.1905** | 0.0304 | ±0.0608 | **-6.270** | **3.61e-10** | *** |
| **BMI (kg/m2)** | **+0.1927** | 0.0486 | ±0.0971 | **+3.968** | **7.26e-05** | *** |
| Hypertension | +1.0931 | 0.7658 | ±1.5317 | +1.427 | 0.1535 |  |
| High cholesterol | +0.0508 | 0.7017 | ±1.4033 | +0.072 | 0.9422 |  |
| Kidney disease | +0.6359 | 1.3284 | ±2.6569 | +0.479 | 0.6322 |  |
| Circulatory disease | -0.4583 | 0.9140 | ±1.8280 | -0.501 | 0.6160 |  |
| **Mean glucose (mg/dL)** | **+0.0377** | 0.0158 | ±0.0316 | **+2.385** | **0.0171** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **576**, R² = **0.1950**, Adj R² = **0.1793**, F-statistic = **12.42** (p = **3.91e-21**), Residual SE = **7.881** on **564** df, AIC = **4024.7**, BIC = **4077.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.1922** | 4.7275 | ±9.4550 | **+12.732** | **3.91e-37** | *** |
| Education: graduate level (vs college) | -1.2003 | 0.7319 | ±1.4637 | -1.640 | 0.1010 |  |
| Education: high school or below (vs college) | -0.5970 | 1.1784 | ±2.3569 | -0.507 | 0.6124 |  |
| **Site: UCSD (vs UAB)** | **-2.5832** | 0.9338 | ±1.8677 | **-2.766** | **0.0057** | ** |
| **Site: UW (vs UAB)** | **-3.0221** | 0.7871 | ±1.5742 | **-3.840** | **1.23e-04** | *** |
| **Age (years)** | **-0.1905** | 0.0304 | ±0.0608 | **-6.270** | **3.61e-10** | *** |
| **BMI (kg/m2)** | **+0.1927** | 0.0486 | ±0.0971 | **+3.968** | **7.26e-05** | *** |
| Hypertension | +1.0931 | 0.7658 | ±1.5317 | +1.427 | 0.1535 |  |
| High cholesterol | +0.0508 | 0.7017 | ±1.4033 | +0.072 | 0.9422 |  |
| Kidney disease | +0.6359 | 1.3284 | ±2.6569 | +0.479 | 0.6322 |  |
| Circulatory disease | -0.4583 | 0.9140 | ±1.8280 | -0.501 | 0.6160 |  |
| **GMI (%)** | **+1.5771** | 0.6614 | ±1.3228 | **+2.385** | **0.0171** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **576**, R² = **0.1915**, Adj R² = **0.1758**, F-statistic = **12.15** (p = **1.22e-20**), Residual SE = **7.898** on **564** df, AIC = **4027.2**, BIC = **4079.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.1123** | 3.0951 | ±6.1902 | **+21.360** | **3.14e-101** | *** |
| Education: graduate level (vs college) | -1.2088 | 0.7324 | ±1.4648 | -1.650 | 0.0989 | . |
| Education: high school or below (vs college) | -0.5139 | 1.1796 | ±2.3592 | -0.436 | 0.6631 |  |
| **Site: UCSD (vs UAB)** | **-2.5920** | 0.9382 | ±1.8764 | **-2.763** | **0.0057** | ** |
| **Site: UW (vs UAB)** | **-3.0583** | 0.7896 | ±1.5792 | **-3.873** | **1.07e-04** | *** |
| **Age (years)** | **-0.1860** | 0.0307 | ±0.0614 | **-6.060** | **1.36e-09** | *** |
| **BMI (kg/m2)** | **+0.1891** | 0.0487 | ±0.0975 | **+3.880** | **1.04e-04** | *** |
| Hypertension | +1.1350 | 0.7667 | ±1.5335 | +1.480 | 0.1388 |  |
| High cholesterol | +0.0514 | 0.7004 | ±1.4009 | +0.073 | 0.9415 |  |
| Kidney disease | +0.8842 | 1.3231 | ±2.6462 | +0.668 | 0.5040 |  |
| Circulatory disease | -0.4408 | 0.9122 | ±1.8244 | -0.483 | 0.6290 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0310** | 0.0145 | ±0.0290 | **+2.138** | **0.0325** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **576**, R² = **0.1961**, Adj R² = **0.1804**, F-statistic = **12.50** (p = **2.78e-21**), Residual SE = **7.876** on **564** df, AIC = **4024.0**, BIC = **4076.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.0470** | 2.6580 | ±5.3159 | **+25.601** | **1.48e-144** | *** |
| Education: graduate level (vs college) | -1.1274 | 0.7339 | ±1.4678 | -1.536 | 0.1245 |  |
| Education: high school or below (vs college) | -0.7839 | 1.1924 | ±2.3848 | -0.657 | 0.5109 |  |
| **Site: UCSD (vs UAB)** | **-2.5491** | 0.9284 | ±1.8568 | **-2.746** | **0.0060** | ** |
| **Site: UW (vs UAB)** | **-2.8820** | 0.7869 | ±1.5737 | **-3.663** | **2.50e-04** | *** |
| **Age (years)** | **-0.1994** | 0.0308 | ±0.0616 | **-6.474** | **9.53e-11** | *** |
| **BMI (kg/m2)** | **+0.1998** | 0.0484 | ±0.0967 | **+4.132** | **3.60e-05** | *** |
| Hypertension | +1.1119 | 0.7618 | ±1.5236 | +1.460 | 0.1444 |  |
| High cholesterol | +0.1339 | 0.7055 | ±1.4110 | +0.190 | 0.8495 |  |
| Kidney disease | +0.2914 | 1.3774 | ±2.7548 | +0.212 | 0.8324 |  |
| Circulatory disease | -0.3661 | 0.9047 | ±1.8095 | -0.405 | 0.6857 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0832** | 0.0351 | ±0.0702 | **+2.369** | **0.0178** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **576**, R² = **0.1941**, Adj R² = **0.1784**, F-statistic = **12.35** (p = **5.20e-21**), Residual SE = **7.885** on **564** df, AIC = **4025.4**, BIC = **4077.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.1591** | 2.6609 | ±5.3218 | **+25.615** | **1.04e-144** | *** |
| Education: graduate level (vs college) | -1.1233 | 0.7332 | ±1.4663 | -1.532 | 0.1255 |  |
| Education: high school or below (vs college) | -0.7961 | 1.2019 | ±2.4039 | -0.662 | 0.5078 |  |
| **Site: UCSD (vs UAB)** | **-2.5666** | 0.9309 | ±1.8618 | **-2.757** | **0.0058** | ** |
| **Site: UW (vs UAB)** | **-2.9213** | 0.7871 | ±1.5743 | **-3.711** | **2.06e-04** | *** |
| **Age (years)** | **-0.1994** | 0.0310 | ±0.0620 | **-6.438** | **1.21e-10** | *** |
| **BMI (kg/m2)** | **+0.2002** | 0.0484 | ±0.0969 | **+4.133** | **3.59e-05** | *** |
| Hypertension | +1.1434 | 0.7595 | ±1.5189 | +1.506 | 0.1322 |  |
| High cholesterol | +0.1231 | 0.7077 | ±1.4153 | +0.174 | 0.8619 |  |
| Kidney disease | +0.3380 | 1.3876 | ±2.7751 | +0.244 | 0.8075 |  |
| Circulatory disease | -0.3480 | 0.9058 | ±1.8115 | -0.384 | 0.7008 |  |
| **Avg. daily SD (mg/dL)** | **+0.0886** | 0.0419 | ±0.0839 | **+2.112** | **0.0346** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **576**, R² = **0.1933**, Adj R² = **0.1776**, F-statistic = **12.29** (p = **6.85e-21**), Residual SE = **7.889** on **564** df, AIC = **4026.0**, BIC = **4078.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1334** | 2.7400 | ±5.4800 | **+24.501** | **1.43e-132** | *** |
| Education: graduate level (vs college) | -1.1295 | 0.7331 | ±1.4663 | -1.541 | 0.1234 |  |
| Education: high school or below (vs college) | -0.6951 | 1.1981 | ±2.3962 | -0.580 | 0.5618 |  |
| **Site: UCSD (vs UAB)** | **-2.5384** | 0.9308 | ±1.8617 | **-2.727** | **0.0064** | ** |
| **Site: UW (vs UAB)** | **-2.8652** | 0.7913 | ±1.5825 | **-3.621** | **2.93e-04** | *** |
| **Age (years)** | **-0.2024** | 0.0313 | ±0.0625 | **-6.475** | **9.45e-11** | *** |
| **BMI (kg/m2)** | **+0.2030** | 0.0485 | ±0.0970 | **+4.186** | **2.84e-05** | *** |
| Hypertension | +1.2036 | 0.7566 | ±1.5133 | +1.591 | 0.1117 |  |
| High cholesterol | +0.2028 | 0.7060 | ±1.4120 | +0.287 | 0.7739 |  |
| Kidney disease | +0.3356 | 1.3977 | ±2.7955 | +0.240 | 0.8102 |  |
| Circulatory disease | -0.3475 | 0.9007 | ±1.8014 | -0.386 | 0.6996 |  |
| **CV (%)** | **+0.1473** | 0.0587 | ±0.1174 | **+2.509** | **0.0121** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **576**, R² = **0.1978**, Adj R² = **0.1821**, F-statistic = **12.64** (p = **1.58e-21**), Residual SE = **7.867** on **564** df, AIC = **4022.8**, BIC = **4075.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.8611** | 3.1179 | ±6.2358 | **+24.010** | **2.19e-127** | *** |
| Education: graduate level (vs college) | -1.1861 | 0.7308 | ±1.4617 | -1.623 | 0.1046 |  |
| Education: high school or below (vs college) | -0.7616 | 1.1883 | ±2.3767 | -0.641 | 0.5216 |  |
| **Site: UCSD (vs UAB)** | **-2.5947** | 0.9247 | ±1.8494 | **-2.806** | **0.0050** | ** |
| **Site: UW (vs UAB)** | **-2.9154** | 0.7868 | ±1.5735 | **-3.706** | **2.11e-04** | *** |
| **Age (years)** | **-0.2064** | 0.0311 | ±0.0621 | **-6.644** | **3.05e-11** | *** |
| **BMI (kg/m2)** | **+0.1995** | 0.0483 | ±0.0967 | **+4.127** | **3.68e-05** | *** |
| Hypertension | +1.1899 | 0.7555 | ±1.5111 | +1.575 | 0.1153 |  |
| High cholesterol | +0.1950 | 0.7037 | ±1.4074 | +0.277 | 0.7817 |  |
| Kidney disease | +0.4061 | 1.3781 | ±2.7561 | +0.295 | 0.7682 |  |
| Circulatory disease | -0.4050 | 0.8967 | ±1.7933 | -0.452 | 0.6515 |  |
| **Mean / SD ratio** | **-0.8225** | 0.2581 | ±0.5162 | **-3.187** | **0.0014** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **576**, R² = **0.1951**, Adj R² = **0.1795**, F-statistic = **12.43** (p = **3.75e-21**), Residual SE = **7.880** on **564** df, AIC = **4024.6**, BIC = **4076.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.3090** | 3.1174 | ±6.2347 | **+23.837** | **1.38e-125** | *** |
| Education: graduate level (vs college) | -1.1824 | 0.7303 | ±1.4607 | -1.619 | 0.1054 |  |
| Education: high school or below (vs college) | -0.7489 | 1.1921 | ±2.3843 | -0.628 | 0.5299 |  |
| **Site: UCSD (vs UAB)** | **-2.6556** | 0.9294 | ±1.8588 | **-2.857** | **0.0043** | ** |
| **Site: UW (vs UAB)** | **-2.9758** | 0.7889 | ±1.5779 | **-3.772** | **1.62e-04** | *** |
| **Age (years)** | **-0.2061** | 0.0314 | ±0.0627 | **-6.574** | **4.91e-11** | *** |
| **BMI (kg/m2)** | **+0.1983** | 0.0482 | ±0.0965 | **+4.111** | **3.94e-05** | *** |
| Hypertension | +1.2464 | 0.7531 | ±1.5063 | +1.655 | 0.0979 | . |
| High cholesterol | +0.1704 | 0.7054 | ±1.4108 | +0.242 | 0.8091 |  |
| Kidney disease | +0.5269 | 1.3811 | ±2.7623 | +0.381 | 0.7029 |  |
| Circulatory disease | -0.3789 | 0.8990 | ±1.7980 | -0.421 | 0.6734 |  |
| **Avg. daily mean/SD** | **-0.6060** | 0.2097 | ±0.4193 | **-2.891** | **0.0038** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **576**, R² = **0.1876**, Adj R² = **0.1717**, F-statistic = **11.84** (p = **4.40e-20**), Residual SE = **7.917** on **564** df, AIC = **4030.0**, BIC = **4082.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.2750** | 2.9058 | ±5.8116 | **+23.152** | **1.38e-118** | *** |
| Education: graduate level (vs college) | -1.1873 | 0.7313 | ±1.4626 | -1.624 | 0.1045 |  |
| Education: high school or below (vs college) | -0.4532 | 1.2031 | ±2.4061 | -0.377 | 0.7064 |  |
| **Site: UCSD (vs UAB)** | **-2.5860** | 0.9367 | ±1.8735 | **-2.761** | **0.0058** | ** |
| **Site: UW (vs UAB)** | **-2.9279** | 0.7972 | ±1.5943 | **-3.673** | **2.40e-04** | *** |
| **Age (years)** | **-0.1884** | 0.0308 | ±0.0616 | **-6.116** | **9.58e-10** | *** |
| **BMI (kg/m2)** | **+0.1966** | 0.0489 | ±0.0977 | **+4.023** | **5.74e-05** | *** |
| Hypertension | +1.2830 | 0.7528 | ±1.5056 | +1.704 | 0.0883 | . |
| High cholesterol | +0.2191 | 0.7072 | ±1.4144 | +0.310 | 0.7567 |  |
| Kidney disease | +0.9223 | 1.3787 | ±2.7574 | +0.669 | 0.5035 |  |
| Circulatory disease | -0.4125 | 0.9076 | ±1.8153 | -0.454 | 0.6495 |  |
| MAG (mg/dL/h) | +0.0540 | 0.0362 | ±0.0724 | +1.492 | 0.1357 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **576**, R² = **0.1934**, Adj R² = **0.1777**, F-statistic = **12.30** (p = **6.53e-21**), Residual SE = **7.889** on **564** df, AIC = **4025.9**, BIC = **4078.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.4442** | 2.7140 | ±5.4279 | **+24.851** | **2.53e-136** | *** |
| Education: graduate level (vs college) | -1.1227 | 0.7327 | ±1.4654 | -1.532 | 0.1255 |  |
| Education: high school or below (vs college) | -0.7665 | 1.2017 | ±2.4035 | -0.638 | 0.5236 |  |
| **Site: UCSD (vs UAB)** | **-2.5891** | 0.9302 | ±1.8603 | **-2.783** | **0.0054** | ** |
| **Site: UW (vs UAB)** | **-2.9364** | 0.7880 | ±1.5759 | **-3.727** | **1.94e-04** | *** |
| **Age (years)** | **-0.1981** | 0.0310 | ±0.0621 | **-6.383** | **1.74e-10** | *** |
| **BMI (kg/m2)** | **+0.2042** | 0.0485 | ±0.0969 | **+4.213** | **2.52e-05** | *** |
| Hypertension | +1.1837 | 0.7574 | ±1.5148 | +1.563 | 0.1181 |  |
| High cholesterol | +0.1328 | 0.7072 | ±1.4143 | +0.188 | 0.8510 |  |
| Kidney disease | +0.4106 | 1.3834 | ±2.7668 | +0.297 | 0.7666 |  |
| Circulatory disease | -0.3945 | 0.9053 | ±1.8105 | -0.436 | 0.6630 |  |
| **Avg. daily range (mg/dL)** | **+0.0227** | 0.0099 | ±0.0198 | **+2.292** | **0.0219** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **576**, R² = **0.1961**, Adj R² = **0.1805**, F-statistic = **12.51** (p = **2.72e-21**), Residual SE = **7.875** on **564** df, AIC = **4023.9**, BIC = **4076.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+68.5233** | 2.6400 | ±5.2800 | **+25.956** | **1.57e-148** | *** |
| Education: graduate level (vs college) | -1.1284 | 0.7338 | ±1.4677 | -1.538 | 0.1241 |  |
| Education: high school or below (vs college) | -0.4431 | 1.1860 | ±2.3719 | -0.374 | 0.7087 |  |
| **Site: UCSD (vs UAB)** | **-2.4804** | 0.9289 | ±1.8577 | **-2.670** | **0.0076** | ** |
| **Site: UW (vs UAB)** | **-2.9077** | 0.7901 | ±1.5803 | **-3.680** | **2.33e-04** | *** |
| **Age (years)** | **-0.1921** | 0.0305 | ±0.0610 | **-6.297** | **3.04e-10** | *** |
| **BMI (kg/m2)** | **+0.1976** | 0.0486 | ±0.0971 | **+4.070** | **4.70e-05** | *** |
| Hypertension | +1.1183 | 0.7602 | ±1.5204 | +1.471 | 0.1413 |  |
| High cholesterol | +0.1668 | 0.7026 | ±1.4052 | +0.237 | 0.8123 |  |
| Kidney disease | +0.5849 | 1.3334 | ±2.6667 | +0.439 | 0.6609 |  |
| Circulatory disease | -0.4923 | 0.9029 | ±1.8057 | -0.545 | 0.5856 |  |
| **SD of daily means (mg/dL)** | **+0.1402** | 0.0473 | ±0.0947 | **+2.962** | **0.0031** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **576**, R² = **0.1967**, Adj R² = **0.1810**, F-statistic = **12.55** (p = **2.26e-21**), Residual SE = **7.873** on **564** df, AIC = **4023.5**, BIC = **4075.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.7989** | 3.7866 | ±7.5732 | **+20.282** | **1.86e-91** | *** |
| Education: graduate level (vs college) | -1.0870 | 0.7407 | ±1.4813 | -1.468 | 0.1422 |  |
| Education: high school or below (vs college) | -0.6050 | 1.1677 | ±2.3354 | -0.518 | 0.6044 |  |
| **Site: UCSD (vs UAB)** | **-2.4750** | 0.9277 | ±1.8554 | **-2.668** | **0.0076** | ** |
| **Site: UW (vs UAB)** | **-2.8515** | 0.7886 | ±1.5773 | **-3.616** | **3.00e-04** | *** |
| **Age (years)** | **-0.1928** | 0.0303 | ±0.0607 | **-6.354** | **2.10e-10** | *** |
| **BMI (kg/m2)** | **+0.1975** | 0.0482 | ±0.0963 | **+4.102** | **4.09e-05** | *** |
| Hypertension | +1.1733 | 0.7597 | ±1.5194 | +1.544 | 0.1225 |  |
| High cholesterol | +0.0898 | 0.7034 | ±1.4068 | +0.128 | 0.8984 |  |
| Kidney disease | +0.4461 | 1.3357 | ±2.6713 | +0.334 | 0.7384 |  |
| Circulatory disease | -0.4482 | 0.9083 | ±1.8166 | -0.493 | 0.6217 |  |
| **Time in range 70-180, pooled (%)** | **-0.0763** | 0.0304 | ±0.0607 | **-2.512** | **0.0120** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **576**, R² = **0.1965**, Adj R² = **0.1809**, F-statistic = **12.54** (p = **2.37e-21**), Residual SE = **7.873** on **564** df, AIC = **4023.6**, BIC = **4075.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.7682** | 3.7228 | ±7.4457 | **+20.621** | **1.78e-94** | *** |
| Education: graduate level (vs college) | -1.0841 | 0.7425 | ±1.4850 | -1.460 | 0.1443 |  |
| Education: high school or below (vs college) | -0.6160 | 1.1668 | ±2.3337 | -0.528 | 0.5976 |  |
| **Site: UCSD (vs UAB)** | **-2.4755** | 0.9283 | ±1.8565 | **-2.667** | **0.0077** | ** |
| **Site: UW (vs UAB)** | **-2.8493** | 0.7888 | ±1.5777 | **-3.612** | **3.04e-04** | *** |
| **Age (years)** | **-0.1931** | 0.0304 | ±0.0607 | **-6.360** | **2.02e-10** | *** |
| **BMI (kg/m2)** | **+0.1977** | 0.0482 | ±0.0965 | **+4.098** | **4.17e-05** | *** |
| Hypertension | +1.1794 | 0.7605 | ±1.5209 | +1.551 | 0.1209 |  |
| High cholesterol | +0.0831 | 0.7025 | ±1.4050 | +0.118 | 0.9058 |  |
| Kidney disease | +0.4438 | 1.3349 | ±2.6698 | +0.332 | 0.7395 |  |
| Circulatory disease | -0.4492 | 0.9096 | ±1.8193 | -0.494 | 0.6214 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0755** | 0.0295 | ±0.0589 | **-2.562** | **0.0104** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **576**, R² = **0.1845**, Adj R² = **0.1686**, F-statistic = **11.60** (p = **1.20e-19**), Residual SE = **7.932** on **564** df, AIC = **4032.2**, BIC = **4084.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.3399** | 2.6444 | ±5.2888 | **+26.221** | **1.52e-151** | *** |
| Education: graduate level (vs college) | -1.2076 | 0.7316 | ±1.4631 | -1.651 | 0.0988 | . |
| Education: high school or below (vs college) | -0.2681 | 1.2079 | ±2.4158 | -0.222 | 0.8243 |  |
| **Site: UCSD (vs UAB)** | **-2.4687** | 0.9500 | ±1.8999 | **-2.599** | **0.0094** | ** |
| **Site: UW (vs UAB)** | **-3.0302** | 0.8004 | ±1.6007 | **-3.786** | **1.53e-04** | *** |
| **Age (years)** | **-0.1884** | 0.0309 | ±0.0617 | **-6.103** | **1.04e-09** | *** |
| **BMI (kg/m2)** | **+0.1989** | 0.0489 | ±0.0978 | **+4.065** | **4.80e-05** | *** |
| Hypertension | +1.3513 | 0.7550 | ±1.5100 | +1.790 | 0.0735 | . |
| High cholesterol | +0.2226 | 0.7070 | ±1.4139 | +0.315 | 0.7528 |  |
| Kidney disease | +0.9891 | 1.3726 | ±2.7451 | +0.721 | 0.4712 |  |
| Circulatory disease | -0.4331 | 0.9063 | ±1.8126 | -0.478 | 0.6327 |  |
| Time < 54 (%) | +0.1505 | 0.2742 | ±0.5484 | +0.549 | 0.5830 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **576**, R² = **0.1843**, Adj R² = **0.1683**, F-statistic = **11.58** (p = **1.29e-19**), Residual SE = **7.933** on **564** df, AIC = **4032.4**, BIC = **4084.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4425** | 2.6312 | ±5.2625 | **+26.392** | **1.71e-153** | *** |
| Education: graduate level (vs college) | -1.2126 | 0.7319 | ±1.4637 | -1.657 | 0.0975 | . |
| Education: high school or below (vs college) | -0.2864 | 1.2082 | ±2.4163 | -0.237 | 0.8126 |  |
| **Site: UCSD (vs UAB)** | **-2.5116** | 0.9496 | ±1.8992 | **-2.645** | **0.0082** | ** |
| **Site: UW (vs UAB)** | **-3.0648** | 0.8026 | ±1.6052 | **-3.819** | **1.34e-04** | *** |
| **Age (years)** | **-0.1884** | 0.0310 | ±0.0620 | **-6.072** | **1.26e-09** | *** |
| **BMI (kg/m2)** | **+0.1985** | 0.0490 | ±0.0980 | **+4.053** | **5.06e-05** | *** |
| Hypertension | +1.3408 | 0.7560 | ±1.5120 | +1.774 | 0.0761 | . |
| High cholesterol | +0.2063 | 0.7081 | ±1.4161 | +0.291 | 0.7708 |  |
| Kidney disease | +0.9962 | 1.3729 | ±2.7458 | +0.726 | 0.4681 |  |
| Circulatory disease | -0.4313 | 0.9090 | ±1.8181 | -0.474 | 0.6352 |  |
| Avg. daily time < 54 (%) | +0.0306 | 0.4285 | ±0.8569 | +0.071 | 0.9431 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **576**, R² = **0.1843**, Adj R² = **0.1683**, F-statistic = **11.58** (p = **1.29e-19**), Residual SE = **7.933** on **564** df, AIC = **4032.4**, BIC = **4084.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4402** | 2.6457 | ±5.2914 | **+26.246** | **7.89e-152** | *** |
| Education: graduate level (vs college) | -1.2127 | 0.7353 | ±1.4707 | -1.649 | 0.0991 | . |
| Education: high school or below (vs college) | -0.2904 | 1.2074 | ±2.4149 | -0.240 | 0.8099 |  |
| **Site: UCSD (vs UAB)** | **-2.5153** | 0.9486 | ±1.8973 | **-2.651** | **0.0080** | ** |
| **Site: UW (vs UAB)** | **-3.0687** | 0.8009 | ±1.6019 | **-3.831** | **1.27e-04** | *** |
| **Age (years)** | **-0.1883** | 0.0309 | ±0.0618 | **-6.098** | **1.07e-09** | *** |
| **BMI (kg/m2)** | **+0.1985** | 0.0489 | ±0.0978 | **+4.058** | **4.96e-05** | *** |
| Hypertension | +1.3406 | 0.7547 | ±1.5094 | +1.776 | 0.0757 | . |
| High cholesterol | +0.2039 | 0.7062 | ±1.4125 | +0.289 | 0.7728 |  |
| Kidney disease | +0.9970 | 1.3723 | ±2.7446 | +0.727 | 0.4675 |  |
| Circulatory disease | -0.4294 | 0.9097 | ±1.8194 | -0.472 | 0.6369 |  |
| Time 54-69, pooled (%) | +0.0074 | 0.1282 | ±0.2564 | +0.058 | 0.9538 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **576**, R² = **0.1842**, Adj R² = **0.1683**, F-statistic = **11.58** (p = **1.29e-19**), Residual SE = **7.933** on **564** df, AIC = **4032.4**, BIC = **4084.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4558** | 2.6366 | ±5.2731 | **+26.343** | **6.14e-153** | *** |
| Education: graduate level (vs college) | -1.2160 | 0.7362 | ±1.4725 | -1.652 | 0.0986 | . |
| Education: high school or below (vs college) | -0.2904 | 1.2078 | ±2.4156 | -0.240 | 0.8100 |  |
| **Site: UCSD (vs UAB)** | **-2.5200** | 0.9472 | ±1.8944 | **-2.660** | **0.0078** | ** |
| **Site: UW (vs UAB)** | **-3.0743** | 0.8006 | ±1.6012 | **-3.840** | **1.23e-04** | *** |
| **Age (years)** | **-0.1882** | 0.0309 | ±0.0619 | **-6.082** | **1.19e-09** | *** |
| **BMI (kg/m2)** | **+0.1985** | 0.0489 | ±0.0979 | **+4.056** | **4.99e-05** | *** |
| Hypertension | +1.3381 | 0.7550 | ±1.5099 | +1.772 | 0.0763 | . |
| High cholesterol | +0.2022 | 0.7064 | ±1.4127 | +0.286 | 0.7747 |  |
| Kidney disease | +0.9989 | 1.3719 | ±2.7439 | +0.728 | 0.4665 |  |
| Circulatory disease | -0.4308 | 0.9101 | ±1.8202 | -0.473 | 0.6359 |  |
| Avg. daily time 54-69 (%) | -0.0020 | 0.1279 | ±0.2558 | -0.015 | 0.9877 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **576**, R² = **0.1843**, Adj R² = **0.1684**, F-statistic = **11.58** (p = **1.27e-19**), Residual SE = **7.933** on **564** df, AIC = **4032.4**, BIC = **4084.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4043** | 2.6506 | ±5.3012 | **+26.185** | **3.98e-151** | *** |
| Education: graduate level (vs college) | -1.2076 | 0.7343 | ±1.4686 | -1.644 | 0.1001 |  |
| Education: high school or below (vs college) | -0.2874 | 1.2068 | ±2.4136 | -0.238 | 0.8118 |  |
| **Site: UCSD (vs UAB)** | **-2.5025** | 0.9516 | ±1.9032 | **-2.630** | **0.0085** | ** |
| **Site: UW (vs UAB)** | **-3.0562** | 0.8029 | ±1.6058 | **-3.806** | **1.41e-04** | *** |
| **Age (years)** | **-0.1884** | 0.0309 | ±0.0618 | **-6.102** | **1.05e-09** | *** |
| **BMI (kg/m2)** | **+0.1986** | 0.0489 | ±0.0978 | **+4.060** | **4.91e-05** | *** |
| Hypertension | +1.3455 | 0.7550 | ±1.5100 | +1.782 | 0.0747 | . |
| High cholesterol | +0.2088 | 0.7060 | ±1.4119 | +0.296 | 0.7674 |  |
| Kidney disease | +0.9934 | 1.3731 | ±2.7461 | +0.723 | 0.4694 |  |
| Circulatory disease | -0.4278 | 0.9091 | ±1.8181 | -0.471 | 0.6379 |  |
| Time < 70 (%) | +0.0195 | 0.1010 | ±0.2019 | +0.193 | 0.8467 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **576**, R² = **0.1842**, Adj R² = **0.1683**, F-statistic = **11.58** (p = **1.29e-19**), Residual SE = **7.933** on **564** df, AIC = **4032.4**, BIC = **4084.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4519** | 2.6367 | ±5.2735 | **+26.340** | **6.68e-153** | *** |
| Education: graduate level (vs college) | -1.2149 | 0.7356 | ±1.4712 | -1.652 | 0.0986 | . |
| Education: high school or below (vs college) | -0.2903 | 1.2072 | ±2.4144 | -0.241 | 0.8099 |  |
| **Site: UCSD (vs UAB)** | **-2.5186** | 0.9490 | ±1.8979 | **-2.654** | **0.0080** | ** |
| **Site: UW (vs UAB)** | **-3.0723** | 0.8024 | ±1.6048 | **-3.829** | **1.29e-04** | *** |
| **Age (years)** | **-0.1882** | 0.0310 | ±0.0620 | **-6.076** | **1.23e-09** | *** |
| **BMI (kg/m2)** | **+0.1985** | 0.0489 | ±0.0979 | **+4.055** | **5.01e-05** | *** |
| Hypertension | +1.3389 | 0.7554 | ±1.5108 | +1.772 | 0.0763 | . |
| High cholesterol | +0.2028 | 0.7061 | ±1.4122 | +0.287 | 0.7740 |  |
| Kidney disease | +0.9983 | 1.3725 | ±2.7450 | +0.727 | 0.4670 |  |
| Circulatory disease | -0.4304 | 0.9101 | ±1.8203 | -0.473 | 0.6363 |  |
| Avg. daily time < 70 (%) | +0.0008 | 0.1081 | ±0.2162 | +0.007 | 0.9941 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **576**, R² = **0.1866**, Adj R² = **0.1707**, F-statistic = **11.76** (p = **6.12e-20**), Residual SE = **7.922** on **564** df, AIC = **4030.7**, BIC = **4083.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.4069** | 7.9998 | ±15.9997 | **+9.551** | **1.28e-21** | *** |
| Education: graduate level (vs college) | -1.1687 | 0.7360 | ±1.4720 | -1.588 | 0.1123 |  |
| Education: high school or below (vs college) | -0.4204 | 1.1989 | ±2.3978 | -0.351 | 0.7259 |  |
| **Site: UCSD (vs UAB)** | **-2.4896** | 0.9369 | ±1.8739 | **-2.657** | **0.0079** | ** |
| **Site: UW (vs UAB)** | **-2.9786** | 0.7959 | ±1.5918 | **-3.743** | **1.82e-04** | *** |
| **Age (years)** | **-0.1880** | 0.0307 | ±0.0614 | **-6.126** | **9.03e-10** | *** |
| **BMI (kg/m2)** | **+0.1992** | 0.0489 | ±0.0978 | **+4.074** | **4.62e-05** | *** |
| Hypertension | +1.2858 | 0.7575 | ±1.5149 | +1.698 | 0.0896 | . |
| High cholesterol | +0.2239 | 0.7088 | ±1.4176 | +0.316 | 0.7521 |  |
| Kidney disease | +0.8767 | 1.3632 | ±2.7264 | +0.643 | 0.5202 |  |
| Circulatory disease | -0.4585 | 0.9124 | ±1.8248 | -0.503 | 0.6153 |  |
| Time 54-250, pooled (%) | -0.0713 | 0.0778 | ±0.1557 | -0.916 | 0.3595 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **576**, R² = **0.1880**, Adj R² = **0.1722**, F-statistic = **11.87** (p = **3.81e-20**), Residual SE = **7.915** on **564** df, AIC = **4029.7**, BIC = **4082.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.3248** | 7.8121 | ±15.6243 | **+10.154** | **3.18e-24** | *** |
| Education: graduate level (vs college) | -1.1484 | 0.7369 | ±1.4737 | -1.558 | 0.1191 |  |
| Education: high school or below (vs college) | -0.4813 | 1.1932 | ±2.3864 | -0.403 | 0.6867 |  |
| **Site: UCSD (vs UAB)** | **-2.4947** | 0.9362 | ±1.8724 | **-2.665** | **0.0077** | ** |
| **Site: UW (vs UAB)** | **-2.9570** | 0.7949 | ±1.5898 | **-3.720** | **1.99e-04** | *** |
| **Age (years)** | **-0.1885** | 0.0306 | ±0.0613 | **-6.154** | **7.56e-10** | *** |
| **BMI (kg/m2)** | **+0.1998** | 0.0489 | ±0.0977 | **+4.089** | **4.33e-05** | *** |
| Hypertension | +1.2697 | 0.7571 | ±1.5142 | +1.677 | 0.0935 | . |
| High cholesterol | +0.2257 | 0.7079 | ±1.4158 | +0.319 | 0.7499 |  |
| Kidney disease | +0.8165 | 1.3570 | ±2.7139 | +0.602 | 0.5474 |  |
| Circulatory disease | -0.4743 | 0.9131 | ±1.8262 | -0.519 | 0.6035 |  |
| Avg. daily time 54-250 (%) | -0.1006 | 0.0757 | ±0.1514 | -1.329 | 0.1838 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **576**, R² = **0.2011**, Adj R² = **0.1855**, F-statistic = **12.91** (p = **5.25e-22**), Residual SE = **7.851** on **564** df, AIC = **4020.4**, BIC = **4072.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.5204** | 2.5856 | ±5.1712 | **+26.888** | **3.07e-159** | *** |
| Education: graduate level (vs college) | -1.1265 | 0.7378 | ±1.4756 | -1.527 | 0.1268 |  |
| Education: high school or below (vs college) | -0.5897 | 1.1681 | ±2.3361 | -0.505 | 0.6136 |  |
| **Site: UCSD (vs UAB)** | **-2.5646** | 0.9254 | ±1.8508 | **-2.771** | **0.0056** | ** |
| **Site: UW (vs UAB)** | **-2.9432** | 0.7839 | ±1.5679 | **-3.754** | **1.74e-04** | *** |
| **Age (years)** | **-0.1953** | 0.0303 | ±0.0606 | **-6.451** | **1.11e-10** | *** |
| **BMI (kg/m2)** | **+0.1954** | 0.0481 | ±0.0961 | **+4.066** | **4.78e-05** | *** |
| Hypertension | +1.1182 | 0.7637 | ±1.5273 | +1.464 | 0.1431 |  |
| High cholesterol | -0.0524 | 0.6946 | ±1.3891 | -0.075 | 0.9398 |  |
| Kidney disease | +0.3071 | 1.3218 | ±2.6436 | +0.232 | 0.8163 |  |
| Circulatory disease | -0.4301 | 0.9087 | ±1.8175 | -0.473 | 0.6360 |  |
| **Time 181-250, pooled (%)** | **+0.1297** | 0.0433 | ±0.0866 | **+2.994** | **0.0028** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **576**, R² = **0.1991**, Adj R² = **0.1834**, F-statistic = **12.74** (p = **1.04e-21**), Residual SE = **7.861** on **564** df, AIC = **4021.8**, BIC = **4074.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4587** | 2.5909 | ±5.1818 | **+26.809** | **2.57e-158** | *** |
| Education: graduate level (vs college) | -1.1337 | 0.7396 | ±1.4791 | -1.533 | 0.1253 |  |
| Education: high school or below (vs college) | -0.5744 | 1.1693 | ±2.3385 | -0.491 | 0.6233 |  |
| **Site: UCSD (vs UAB)** | **-2.5343** | 0.9273 | ±1.8547 | **-2.733** | **0.0063** | ** |
| **Site: UW (vs UAB)** | **-2.9343** | 0.7852 | ±1.5704 | **-3.737** | **1.86e-04** | *** |
| **Age (years)** | **-0.1939** | 0.0303 | ±0.0606 | **-6.397** | **1.59e-10** | *** |
| **BMI (kg/m2)** | **+0.1956** | 0.0482 | ±0.0964 | **+4.059** | **4.92e-05** | *** |
| Hypertension | +1.1394 | 0.7653 | ±1.5307 | +1.489 | 0.1366 |  |
| High cholesterol | -0.0324 | 0.6956 | ±1.3912 | -0.047 | 0.9629 |  |
| Kidney disease | +0.3688 | 1.3266 | ±2.6532 | +0.278 | 0.7810 |  |
| Circulatory disease | -0.4267 | 0.9117 | ±1.8234 | -0.468 | 0.6398 |  |
| **Avg. daily time 181-250 (%)** | **+0.1180** | 0.0432 | ±0.0864 | **+2.732** | **0.0063** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **576**, R² = **0.1963**, Adj R² = **0.1807**, F-statistic = **12.53** (p = **2.53e-21**), Residual SE = **7.874** on **564** df, AIC = **4023.8**, BIC = **4076.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.3603** | 2.5921 | ±5.1843 | **+26.758** | **1.00e-157** | *** |
| Education: graduate level (vs college) | -1.1186 | 0.7384 | ±1.4767 | -1.515 | 0.1298 |  |
| Education: high school or below (vs college) | -0.6120 | 1.1707 | ±2.3415 | -0.523 | 0.6012 |  |
| **Site: UCSD (vs UAB)** | **-2.5396** | 0.9288 | ±1.8577 | **-2.734** | **0.0063** | ** |
| **Site: UW (vs UAB)** | **-2.9197** | 0.7868 | ±1.5736 | **-3.711** | **2.07e-04** | *** |
| **Age (years)** | **-0.1920** | 0.0303 | ±0.0606 | **-6.338** | **2.33e-10** | *** |
| **BMI (kg/m2)** | **+0.1972** | 0.0483 | ±0.0966 | **+4.083** | **4.45e-05** | *** |
| Hypertension | +1.1489 | 0.7627 | ±1.5254 | +1.506 | 0.1320 |  |
| High cholesterol | +0.0673 | 0.7021 | ±1.4042 | +0.096 | 0.9237 |  |
| Kidney disease | +0.4740 | 1.3308 | ±2.6617 | +0.356 | 0.7217 |  |
| Circulatory disease | -0.4585 | 0.9122 | ±1.8244 | -0.503 | 0.6152 |  |
| **Time > 180 (%)** | **+0.0752** | 0.0301 | ±0.0602 | **+2.499** | **0.0125** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **576**, R² = **0.1967**, Adj R² = **0.1810**, F-statistic = **12.55** (p = **2.27e-21**), Residual SE = **7.873** on **564** df, AIC = **4023.5**, BIC = **4075.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.3420** | 2.5964 | ±5.1929 | **+26.707** | **3.94e-157** | *** |
| Education: graduate level (vs college) | -1.1184 | 0.7398 | ±1.4796 | -1.512 | 0.1306 |  |
| Education: high school or below (vs college) | -0.6291 | 1.1688 | ±2.3377 | -0.538 | 0.5905 |  |
| **Site: UCSD (vs UAB)** | **-2.5292** | 0.9290 | ±1.8579 | **-2.723** | **0.0065** | ** |
| **Site: UW (vs UAB)** | **-2.9158** | 0.7871 | ±1.5742 | **-3.704** | **2.12e-04** | *** |
| **Age (years)** | **-0.1918** | 0.0303 | ±0.0606 | **-6.331** | **2.44e-10** | *** |
| **BMI (kg/m2)** | **+0.1975** | 0.0484 | ±0.0967 | **+4.083** | **4.45e-05** | *** |
| Hypertension | +1.1519 | 0.7638 | ±1.5276 | +1.508 | 0.1315 |  |
| High cholesterol | +0.0589 | 0.7004 | ±1.4008 | +0.084 | 0.9330 |  |
| Kidney disease | +0.4590 | 1.3287 | ±2.6573 | +0.345 | 0.7298 |  |
| Circulatory disease | -0.4594 | 0.9134 | ±1.8268 | -0.503 | 0.6150 |  |
| **Avg. daily time > 180 (%)** | **+0.0763** | 0.0292 | ±0.0583 | **+2.618** | **0.0089** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **576**, R² = **0.1901**, Adj R² = **0.1743**, F-statistic = **12.03** (p = **1.95e-20**), Residual SE = **7.905** on **564** df, AIC = **4028.2**, BIC = **4080.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.4150** | 2.6092 | ±5.2184 | **+26.604** | **6.10e-156** | *** |
| Education: graduate level (vs college) | -1.1407 | 0.7396 | ±1.4793 | -1.542 | 0.1230 |  |
| Education: high school or below (vs college) | -0.4368 | 1.1767 | ±2.3533 | -0.371 | 0.7105 |  |
| **Site: UCSD (vs UAB)** | **-2.5145** | 0.9341 | ±1.8681 | **-2.692** | **0.0071** | ** |
| **Site: UW (vs UAB)** | **-2.9856** | 0.7915 | ±1.5831 | **-3.772** | **1.62e-04** | *** |
| **Age (years)** | **-0.1885** | 0.0306 | ±0.0612 | **-6.159** | **7.33e-10** | *** |
| **BMI (kg/m2)** | **+0.1950** | 0.0484 | ±0.0968 | **+4.030** | **5.59e-05** | *** |
| Hypertension | +1.1924 | 0.7673 | ±1.5345 | +1.554 | 0.1201 |  |
| High cholesterol | +0.1202 | 0.7044 | ±1.4087 | +0.171 | 0.8645 |  |
| Kidney disease | +0.8247 | 1.3329 | ±2.6658 | +0.619 | 0.5361 |  |
| Circulatory disease | -0.4719 | 0.9125 | ±1.8250 | -0.517 | 0.6050 |  |
| Nocturnal time > 180 (%) | +0.0538 | 0.0288 | ±0.0575 | +1.870 | 0.0615 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **576**, R² = **0.1921**, Adj R² = **0.1764**, F-statistic = **12.19** (p = **1.01e-20**), Residual SE = **7.895** on **564** df, AIC = **4026.8**, BIC = **4079.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.3452** | 2.5953 | ±5.1905 | **+26.720** | **2.76e-157** | *** |
| Education: graduate level (vs college) | -1.1141 | 0.7329 | ±1.4658 | -1.520 | 0.1285 |  |
| Education: high school or below (vs college) | -0.4769 | 1.1946 | ±2.3892 | -0.399 | 0.6897 |  |
| **Site: UCSD (vs UAB)** | **-2.6246** | 0.9313 | ±1.8626 | **-2.818** | **0.0048** | ** |
| **Site: UW (vs UAB)** | **-3.0201** | 0.7884 | ±1.5768 | **-3.831** | **1.28e-04** | *** |
| **Age (years)** | **-0.1957** | 0.0309 | ±0.0618 | **-6.337** | **2.35e-10** | *** |
| **BMI (kg/m2)** | **+0.2044** | 0.0486 | ±0.0973 | **+4.203** | **2.64e-05** | *** |
| Hypertension | +1.1572 | 0.7595 | ±1.5190 | +1.524 | 0.1276 |  |
| High cholesterol | +0.1013 | 0.7051 | ±1.4102 | +0.144 | 0.8857 |  |
| Kidney disease | +0.5865 | 1.3614 | ±2.7228 | +0.431 | 0.6666 |  |
| Circulatory disease | -0.3846 | 0.9077 | ±1.8153 | -0.424 | 0.6718 |  |
| **Any reading > 250 during wear (0/1)** | **+1.7840** | 0.7798 | ±1.5595 | **+2.288** | **0.0221** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **576**, R² = **0.1864**, Adj R² = **0.1705**, F-statistic = **11.75** (p = **6.44e-20**), Residual SE = **7.923** on **564** df, AIC = **4030.9**, BIC = **4083.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.3307** | 2.6201 | ±5.2402 | **+26.461** | **2.72e-154** | *** |
| Education: graduate level (vs college) | -1.1732 | 0.7358 | ±1.4717 | -1.594 | 0.1108 |  |
| Education: high school or below (vs college) | -0.4280 | 1.2012 | ±2.4024 | -0.356 | 0.7216 |  |
| **Site: UCSD (vs UAB)** | **-2.5137** | 0.9383 | ±1.8765 | **-2.679** | **0.0074** | ** |
| **Site: UW (vs UAB)** | **-3.0004** | 0.7942 | ±1.5885 | **-3.778** | **1.58e-04** | *** |
| **Age (years)** | **-0.1879** | 0.0307 | ±0.0614 | **-6.124** | **9.10e-10** | *** |
| **BMI (kg/m2)** | **+0.1990** | 0.0489 | ±0.0978 | **+4.070** | **4.70e-05** | *** |
| Hypertension | +1.2810 | 0.7584 | ±1.5169 | +1.689 | 0.0912 | . |
| High cholesterol | +0.2142 | 0.7089 | ±1.4179 | +0.302 | 0.7626 |  |
| Kidney disease | +0.8836 | 1.3616 | ±2.7231 | +0.649 | 0.5164 |  |
| Circulatory disease | -0.4567 | 0.9135 | ±1.8269 | -0.500 | 0.6171 |  |
| Time > 250 (%) | +0.0698 | 0.0771 | ±0.1542 | +0.906 | 0.3651 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 576)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **576**, R² = **0.1881**, Adj R² = **0.1723**, F-statistic = **11.88** (p = **3.70e-20**), Residual SE = **7.915** on **564** df, AIC = **4029.6**, BIC = **4081.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+69.2972** | 2.6195 | ±5.2389 | **+26.455** | **3.22e-154** | *** |
| Education: graduate level (vs college) | -1.1553 | 0.7364 | ±1.4727 | -1.569 | 0.1167 |  |
| Education: high school or below (vs college) | -0.5010 | 1.1961 | ±2.3921 | -0.419 | 0.6753 |  |
| **Site: UCSD (vs UAB)** | **-2.5194** | 0.9375 | ±1.8750 | **-2.687** | **0.0072** | ** |
| **Site: UW (vs UAB)** | **-2.9813** | 0.7936 | ±1.5871 | **-3.757** | **1.72e-04** | *** |
| **Age (years)** | **-0.1881** | 0.0306 | ±0.0612 | **-6.142** | **8.15e-10** | *** |
| **BMI (kg/m2)** | **+0.1997** | 0.0489 | ±0.0977 | **+4.087** | **4.37e-05** | *** |
| Hypertension | +1.2599 | 0.7580 | ±1.5161 | +1.662 | 0.0965 | . |
| High cholesterol | +0.2137 | 0.7078 | ±1.4157 | +0.302 | 0.7627 |  |
| Kidney disease | +0.8187 | 1.3548 | ±2.7095 | +0.604 | 0.5456 |  |
| Circulatory disease | -0.4731 | 0.9146 | ±1.8293 | -0.517 | 0.6050 |  |
| Avg. daily time > 250 (%) | +0.1037 | 0.0766 | ±0.1531 | +1.354 | 0.1756 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 588; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **588**, R² = **0.0409**, Adj R² = **0.0243**, F-statistic = **2.46** (p = **0.0069**), Residual SE = **65.535** on **577** df, AIC = **6598.3**, BIC = **6646.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.6830** | 22.6798 | ±45.3596 | **+17.138** | **7.75e-66** | *** |
| Education: graduate level (vs college) | +5.9032 | 6.0751 | ±12.1502 | +0.972 | 0.3312 |  |
| **Education: high school or below (vs college)** | **-24.7347** | 10.6008 | ±21.2017 | **-2.333** | **0.0196** | * |
| Site: UCSD (vs UAB) | -1.1315 | 7.8398 | ±15.6797 | -0.144 | 0.8852 |  |
| Site: UW (vs UAB) | -1.1662 | 6.4178 | ±12.8355 | -0.182 | 0.8558 |  |
| Age (years) | -0.0183 | 0.2712 | ±0.5423 | -0.067 | 0.9462 |  |
| BMI (kg/m2) | -0.5914 | 0.4359 | ±0.8718 | -1.357 | 0.1749 |  |
| **Hypertension** | **-13.6400** | 6.0897 | ±12.1794 | **-2.240** | **0.0251** | * |
| High cholesterol | +5.8658 | 5.5923 | ±11.1845 | +1.049 | 0.2942 |  |
| Kidney disease | -2.0692 | 11.6137 | ±23.2275 | -0.178 | 0.8586 |  |
| Circulatory disease | +4.1510 | 7.9280 | ±15.8559 | +0.524 | 0.6006 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **588**, R² = **0.0554**, Adj R² = **0.0373**, F-statistic = **3.07** (p = **5.15e-04**), Residual SE = **65.095** on **576** df, AIC = **6591.3**, BIC = **6643.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+437.2358** | 27.5039 | ±55.0078 | **+15.897** | **6.62e-57** | *** |
| Education: graduate level (vs college) | +4.5624 | 6.0466 | ±12.0932 | +0.755 | 0.4505 |  |
| **Education: high school or below (vs college)** | **-21.3122** | 10.4972 | ±20.9944 | **-2.030** | **0.0423** | * |
| Site: UCSD (vs UAB) | -0.5373 | 7.7701 | ±15.5402 | -0.069 | 0.9449 |  |
| Site: UW (vs UAB) | -2.5681 | 6.4205 | ±12.8409 | -0.400 | 0.6892 |  |
| Age (years) | +0.0818 | 0.2688 | ±0.5375 | +0.304 | 0.7608 |  |
| BMI (kg/m2) | -0.4908 | 0.4366 | ±0.8732 | -1.124 | 0.2609 |  |
| Hypertension | -11.9127 | 6.0930 | ±12.1861 | -1.955 | 0.0506 | . |
| High cholesterol | +7.0892 | 5.5977 | ±11.1954 | +1.266 | 0.2054 |  |
| Kidney disease | -1.1531 | 11.5758 | ±23.1517 | -0.100 | 0.9207 |  |
| Circulatory disease | +3.4644 | 7.8622 | ±15.7243 | +0.441 | 0.6595 |  |
| **HbA1c (%)** | **-9.8950** | 3.1075 | ±6.2151 | **-3.184** | **0.0015** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **588**, R² = **0.0481**, Adj R² = **0.0299**, F-statistic = **2.65** (p = **0.0026**), Residual SE = **65.345** on **576** df, AIC = **6595.8**, BIC = **6648.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+414.2155** | 25.9640 | ±51.9279 | **+15.953** | **2.69e-57** | *** |
| Education: graduate level (vs college) | +5.7793 | 6.0928 | ±12.1856 | +0.949 | 0.3428 |  |
| **Education: high school or below (vs college)** | **-22.6335** | 10.6004 | ±21.2009 | **-2.135** | **0.0327** | * |
| Site: UCSD (vs UAB) | -0.9322 | 7.7726 | ±15.5452 | -0.120 | 0.9045 |  |
| Site: UW (vs UAB) | -1.4791 | 6.4314 | ±12.8628 | -0.230 | 0.8181 |  |
| Age (years) | -0.0024 | 0.2698 | ±0.5397 | -0.009 | 0.9930 |  |
| BMI (kg/m2) | -0.5562 | 0.4372 | ±0.8743 | -1.272 | 0.2033 |  |
| Hypertension | -12.0347 | 6.1913 | ±12.3825 | -1.944 | 0.0519 | . |
| High cholesterol | +6.7443 | 5.5782 | ±11.1563 | +1.209 | 0.2266 |  |
| Kidney disease | +0.0674 | 11.8000 | ±23.6001 | +0.006 | 0.9954 |  |
| Circulatory disease | +4.2717 | 7.8882 | ±15.7764 | +0.542 | 0.5881 |  |
| **Mean glucose (mg/dL)** | **-0.2384** | 0.1106 | ±0.2212 | **-2.156** | **0.0311** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **588**, R² = **0.0481**, Adj R² = **0.0299**, F-statistic = **2.65** (p = **0.0026**), Residual SE = **65.345** on **576** df, AIC = **6595.8**, BIC = **6648.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+447.2102** | 35.9493 | ±71.8985 | **+12.440** | **1.58e-35** | *** |
| Education: graduate level (vs college) | +5.7793 | 6.0928 | ±12.1856 | +0.949 | 0.3428 |  |
| **Education: high school or below (vs college)** | **-22.6335** | 10.6004 | ±21.2009 | **-2.135** | **0.0327** | * |
| Site: UCSD (vs UAB) | -0.9322 | 7.7726 | ±15.5452 | -0.120 | 0.9045 |  |
| Site: UW (vs UAB) | -1.4791 | 6.4314 | ±12.8628 | -0.230 | 0.8181 |  |
| Age (years) | -0.0024 | 0.2698 | ±0.5397 | -0.009 | 0.9930 |  |
| BMI (kg/m2) | -0.5562 | 0.4372 | ±0.8743 | -1.272 | 0.2033 |  |
| Hypertension | -12.0347 | 6.1913 | ±12.3825 | -1.944 | 0.0519 | . |
| High cholesterol | +6.7443 | 5.5782 | ±11.1563 | +1.209 | 0.2266 |  |
| Kidney disease | +0.0674 | 11.8000 | ±23.6001 | +0.006 | 0.9954 |  |
| Circulatory disease | +4.2717 | 7.8882 | ±15.7764 | +0.542 | 0.5881 |  |
| **GMI (%)** | **-9.9682** | 4.6230 | ±9.2459 | **-2.156** | **0.0311** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **588**, R² = **0.0481**, Adj R² = **0.0299**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **65.346** on **576** df, AIC = **6595.9**, BIC = **6648.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+414.2266** | 26.2922 | ±52.5843 | **+15.755** | **6.37e-56** | *** |
| Education: graduate level (vs college) | +5.8878 | 6.0993 | ±12.1987 | +0.965 | 0.3344 |  |
| **Education: high school or below (vs college)** | **-22.8785** | 10.5415 | ±21.0831 | **-2.170** | **0.0300** | * |
| Site: UCSD (vs UAB) | -0.8545 | 7.7870 | ±15.5739 | -0.110 | 0.9126 |  |
| Site: UW (vs UAB) | -1.2957 | 6.4344 | ±12.8688 | -0.201 | 0.8404 |  |
| Age (years) | -0.0331 | 0.2711 | ±0.5422 | -0.122 | 0.9027 |  |
| BMI (kg/m2) | -0.5228 | 0.4370 | ±0.8740 | -1.196 | 0.2316 |  |
| Hypertension | -12.1223 | 6.1912 | ±12.3824 | -1.958 | 0.0502 | . |
| High cholesterol | +7.0193 | 5.5841 | ±11.1681 | +1.257 | 0.2087 |  |
| Kidney disease | -1.2605 | 11.6844 | ±23.3689 | -0.108 | 0.9141 |  |
| Circulatory disease | +4.2156 | 7.8712 | ±15.7423 | +0.536 | 0.5923 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.2371** | 0.1172 | ±0.2344 | **-2.024** | **0.0430** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **588**, R² = **0.0448**, Adj R² = **0.0265**, F-statistic = **2.45** (p = **0.0053**), Residual SE = **65.459** on **576** df, AIC = **6597.9**, BIC = **6650.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+394.7748** | 22.8692 | ±45.7383 | **+17.262** | **9.04e-67** | *** |
| Education: graduate level (vs college) | +5.5095 | 6.0825 | ±12.1650 | +0.906 | 0.3650 |  |
| **Education: high school or below (vs college)** | **-22.4650** | 10.7948 | ±21.5896 | **-2.081** | **0.0374** | * |
| Site: UCSD (vs UAB) | -1.0230 | 7.7942 | ±15.5884 | -0.131 | 0.8956 |  |
| Site: UW (vs UAB) | -1.9803 | 6.4391 | ±12.8782 | -0.308 | 0.7584 |  |
| Age (years) | +0.0297 | 0.2721 | ±0.5442 | +0.109 | 0.9131 |  |
| BMI (kg/m2) | -0.5939 | 0.4368 | ±0.8736 | -1.360 | 0.1739 |  |
| **Hypertension** | **-12.5791** | 6.1228 | ±12.2456 | **-2.054** | **0.0399** | * |
| High cholesterol | +6.1060 | 5.5809 | ±11.1618 | +1.094 | 0.2739 |  |
| Kidney disease | +0.8464 | 12.1097 | ±24.2195 | +0.070 | 0.9443 |  |
| Circulatory disease | +3.7996 | 7.9342 | ±15.8685 | +0.479 | 0.6320 |  |
| Glucose SD, pooled (mg/dL) | -0.3639 | 0.2317 | ±0.4634 | -1.571 | 0.1163 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **588**, R² = **0.0437**, Adj R² = **0.0255**, F-statistic = **2.39** (p = **0.0066**), Residual SE = **65.494** on **576** df, AIC = **6598.5**, BIC = **6651.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.9268** | 22.8985 | ±45.7970 | **+17.203** | **2.51e-66** | *** |
| Education: graduate level (vs college) | +5.5174 | 6.0695 | ±12.1391 | +0.909 | 0.3633 |  |
| **Education: high school or below (vs college)** | **-22.5670** | 10.8358 | ±21.6715 | **-2.083** | **0.0373** | * |
| Site: UCSD (vs UAB) | -0.9197 | 7.8130 | ±15.6261 | -0.118 | 0.9063 |  |
| Site: UW (vs UAB) | -1.7646 | 6.4399 | ±12.8798 | -0.274 | 0.7841 |  |
| Age (years) | +0.0265 | 0.2720 | ±0.5441 | +0.097 | 0.9224 |  |
| BMI (kg/m2) | -0.5950 | 0.4372 | ±0.8743 | -1.361 | 0.1735 |  |
| **Hypertension** | **-12.7970** | 6.1299 | ±12.2597 | **-2.088** | **0.0368** | * |
| High cholesterol | +6.1447 | 5.5865 | ±11.1730 | +1.100 | 0.2714 |  |
| Kidney disease | +0.4952 | 12.0478 | ±24.0957 | +0.041 | 0.9672 |  |
| Circulatory disease | +3.7600 | 7.9506 | ±15.9012 | +0.473 | 0.6363 |  |
| Avg. daily SD (mg/dL) | -0.3622 | 0.2581 | ±0.5162 | -1.403 | 0.1606 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **588**, R² = **0.0411**, Adj R² = **0.0227**, F-statistic = **2.24** (p = **0.0114**), Residual SE = **65.586** on **576** df, AIC = **6600.2**, BIC = **6652.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+391.0985** | 23.3288 | ±46.6575 | **+16.765** | **4.43e-63** | *** |
| Education: graduate level (vs college) | +5.8132 | 6.0741 | ±12.1482 | +0.957 | 0.3385 |  |
| **Education: high school or below (vs college)** | **-24.2912** | 10.8090 | ±21.6179 | **-2.247** | **0.0246** | * |
| Site: UCSD (vs UAB) | -1.0940 | 7.8471 | ±15.6942 | -0.139 | 0.8891 |  |
| Site: UW (vs UAB) | -1.3772 | 6.4404 | ±12.8809 | -0.214 | 0.8307 |  |
| Age (years) | -0.0037 | 0.2768 | ±0.5537 | -0.013 | 0.9895 |  |
| BMI (kg/m2) | -0.5952 | 0.4360 | ±0.8719 | -1.365 | 0.1722 |  |
| **Hypertension** | **-13.4844** | 6.1010 | ±12.2020 | **-2.210** | **0.0271** | * |
| High cholesterol | +5.8571 | 5.6013 | ±11.2026 | +1.046 | 0.2957 |  |
| Kidney disease | -1.4097 | 12.0515 | ±24.1030 | -0.117 | 0.9069 |  |
| Circulatory disease | +4.0517 | 7.9573 | ±15.9146 | +0.509 | 0.6106 |  |
| CV (%) | -0.1546 | 0.4726 | ±0.9452 | -0.327 | 0.7436 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **588**, R² = **0.0410**, Adj R² = **0.0227**, F-statistic = **2.24** (p = **0.0115**), Residual SE = **65.588** on **576** df, AIC = **6600.2**, BIC = **6652.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+385.1472** | 27.4273 | ±54.8546 | **+14.042** | **8.57e-45** | *** |
| Education: graduate level (vs college) | +5.8796 | 6.0786 | ±12.1571 | +0.967 | 0.3334 |  |
| **Education: high school or below (vs college)** | **-24.4151** | 10.7620 | ±21.5239 | **-2.269** | **0.0233** | * |
| Site: UCSD (vs UAB) | -1.0604 | 7.8493 | ±15.6987 | -0.135 | 0.8925 |  |
| Site: UW (vs UAB) | -1.2639 | 6.4284 | ±12.8568 | -0.197 | 0.8441 |  |
| Age (years) | -0.0066 | 0.2769 | ±0.5539 | -0.024 | 0.9809 |  |
| BMI (kg/m2) | -0.5918 | 0.4361 | ±0.8723 | -1.357 | 0.1748 |  |
| **Hypertension** | **-13.5425** | 6.0949 | ±12.1898 | **-2.222** | **0.0263** | * |
| High cholesterol | +5.8715 | 5.5990 | ±11.1980 | +1.049 | 0.2943 |  |
| Kidney disease | -1.6954 | 11.8854 | ±23.7708 | -0.143 | 0.8866 |  |
| Circulatory disease | +4.1358 | 7.9418 | ±15.8836 | +0.521 | 0.6025 |  |
| Mean / SD ratio | +0.5381 | 2.1232 | ±4.2464 | +0.253 | 0.7999 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **588**, R² = **0.0414**, Adj R² = **0.0231**, F-statistic = **2.26** (p = **0.0107**), Residual SE = **65.576** on **576** df, AIC = **6600.0**, BIC = **6652.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+380.9448** | 27.0783 | ±54.1565 | **+14.068** | **5.95e-45** | *** |
| Education: graduate level (vs college) | +5.8496 | 6.0757 | ±12.1514 | +0.963 | 0.3357 |  |
| **Education: high school or below (vs college)** | **-23.9831** | 10.7833 | ±21.5665 | **-2.224** | **0.0261** | * |
| Site: UCSD (vs UAB) | -0.8442 | 7.8631 | ±15.7262 | -0.107 | 0.9145 |  |
| Site: UW (vs UAB) | -1.3100 | 6.4285 | ±12.8571 | -0.204 | 0.8385 |  |
| Age (years) | +0.0095 | 0.2757 | ±0.5513 | +0.035 | 0.9724 |  |
| BMI (kg/m2) | -0.5903 | 0.4362 | ±0.8723 | -1.353 | 0.1759 |  |
| **Hypertension** | **-13.5099** | 6.0918 | ±12.1836 | **-2.218** | **0.0266** | * |
| High cholesterol | +5.9304 | 5.5961 | ±11.1921 | +1.060 | 0.2893 |  |
| Kidney disease | -1.3312 | 11.8118 | ±23.6235 | -0.113 | 0.9103 |  |
| Circulatory disease | +4.0925 | 7.9426 | ±15.8852 | +0.515 | 0.6064 |  |
| Avg. daily mean/SD | +0.9662 | 1.7096 | ±3.4191 | +0.565 | 0.5720 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **588**, R² = **0.0727**, Adj R² = **0.0550**, F-statistic = **4.10** (p = **7.87e-06**), Residual SE = **64.495** on **576** df, AIC = **6580.5**, BIC = **6633.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+440.5311** | 24.9730 | ±49.9459 | **+17.640** | **1.21e-69** | *** |
| Education: graduate level (vs college) | +5.2860 | 5.9491 | ±11.8982 | +0.889 | 0.3742 |  |
| Education: high school or below (vs college) | -20.5308 | 10.6279 | ±21.2559 | -1.932 | 0.0534 | . |
| Site: UCSD (vs UAB) | +0.5428 | 7.7009 | ±15.4018 | +0.070 | 0.9438 |  |
| Site: UW (vs UAB) | -4.4992 | 6.2793 | ±12.5586 | -0.717 | 0.4737 |  |
| Age (years) | -0.0194 | 0.2652 | ±0.5303 | -0.073 | 0.9415 |  |
| BMI (kg/m2) | -0.5475 | 0.4235 | ±0.8470 | -1.293 | 0.1960 |  |
| **Hypertension** | **-12.3314** | 5.9712 | ±11.9424 | **-2.065** | **0.0389** | * |
| High cholesterol | +5.5483 | 5.5709 | ±11.1418 | +0.996 | 0.3193 |  |
| Kidney disease | -0.5871 | 11.6144 | ±23.2289 | -0.051 | 0.9597 |  |
| Circulatory disease | +3.8857 | 7.8835 | ±15.7670 | +0.493 | 0.6221 |  |
| **MAG (mg/dL/h)** | **-1.2816** | 0.3026 | ±0.6052 | **-4.236** | **2.28e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **588**, R² = **0.0445**, Adj R² = **0.0262**, F-statistic = **2.44** (p = **0.0056**), Residual SE = **65.469** on **576** df, AIC = **6598.1**, BIC = **6650.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.3006** | 23.4770 | ±46.9540 | **+16.966** | **1.48e-64** | *** |
| Education: graduate level (vs college) | +5.4475 | 6.0741 | ±12.1481 | +0.897 | 0.3698 |  |
| **Education: high school or below (vs college)** | **-22.3119** | 10.8438 | ±21.6875 | **-2.058** | **0.0396** | * |
| Site: UCSD (vs UAB) | -0.7990 | 7.8142 | ±15.6284 | -0.102 | 0.9186 |  |
| Site: UW (vs UAB) | -1.8024 | 6.4312 | ±12.8624 | -0.280 | 0.7793 |  |
| Age (years) | +0.0276 | 0.2716 | ±0.5432 | +0.101 | 0.9192 |  |
| BMI (kg/m2) | -0.6170 | 0.4379 | ±0.8758 | -1.409 | 0.1588 |  |
| **Hypertension** | **-12.8701** | 6.1092 | ±12.2183 | **-2.107** | **0.0351** | * |
| High cholesterol | +6.1443 | 5.5942 | ±11.1885 | +1.098 | 0.2721 |  |
| Kidney disease | +0.6249 | 11.9881 | ±23.9762 | +0.052 | 0.9584 |  |
| Circulatory disease | +3.9228 | 7.9621 | ±15.9242 | +0.493 | 0.6222 |  |
| Avg. daily range (mg/dL) | -0.1082 | 0.0694 | ±0.1388 | -1.558 | 0.1192 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **588**, R² = **0.0466**, Adj R² = **0.0284**, F-statistic = **2.56** (p = **0.0036**), Residual SE = **65.396** on **576** df, AIC = **6596.8**, BIC = **6649.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.5888** | 22.6556 | ±45.3112 | **+17.373** | **1.33e-67** | *** |
| Education: graduate level (vs college) | +5.4879 | 6.1044 | ±12.2088 | +0.899 | 0.3687 |  |
| **Education: high school or below (vs college)** | **-23.7944** | 10.5487 | ±21.0975 | **-2.256** | **0.0241** | * |
| Site: UCSD (vs UAB) | -1.4969 | 7.7593 | ±15.5186 | -0.193 | 0.8470 |  |
| Site: UW (vs UAB) | -2.0621 | 6.4461 | ±12.8922 | -0.320 | 0.7490 |  |
| Age (years) | +0.0032 | 0.2719 | ±0.5438 | +0.012 | 0.9907 |  |
| BMI (kg/m2) | -0.5865 | 0.4356 | ±0.8713 | -1.346 | 0.1782 |  |
| **Hypertension** | **-12.4056** | 6.0989 | ±12.1979 | **-2.034** | **0.0419** | * |
| High cholesterol | +6.0156 | 5.5726 | ±11.1453 | +1.079 | 0.2804 |  |
| Kidney disease | -0.0482 | 11.9162 | ±23.8323 | -0.004 | 0.9968 |  |
| Circulatory disease | +4.4246 | 7.8519 | ±15.7038 | +0.564 | 0.5731 |  |
| SD of daily means (mg/dL) | -0.7480 | 0.4231 | ±0.8462 | -1.768 | 0.0771 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **588**, R² = **0.0476**, Adj R² = **0.0294**, F-statistic = **2.62** (p = **0.0029**), Residual SE = **65.363** on **576** df, AIC = **6596.2**, BIC = **6648.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+347.2395** | 31.6215 | ±63.2431 | **+10.981** | **4.71e-28** | *** |
| Education: graduate level (vs college) | +5.1421 | 6.0992 | ±12.1985 | +0.843 | 0.3992 |  |
| **Education: high school or below (vs college)** | **-22.7772** | 10.6094 | ±21.2188 | **-2.147** | **0.0318** | * |
| Site: UCSD (vs UAB) | -1.6238 | 7.7418 | ±15.4835 | -0.210 | 0.8339 |  |
| Site: UW (vs UAB) | -2.3990 | 6.4527 | ±12.9054 | -0.372 | 0.7101 |  |
| Age (years) | +0.0073 | 0.2707 | ±0.5414 | +0.027 | 0.9786 |  |
| BMI (kg/m2) | -0.5878 | 0.4366 | ±0.8732 | -1.346 | 0.1782 |  |
| **Hypertension** | **-12.5901** | 6.0925 | ±12.1849 | **-2.066** | **0.0388** | * |
| High cholesterol | +6.4255 | 5.5733 | ±11.1466 | +1.153 | 0.2489 |  |
| Kidney disease | +0.8490 | 11.9566 | ±23.9132 | +0.071 | 0.9434 |  |
| Circulatory disease | +4.1847 | 7.9041 | ±15.8081 | +0.529 | 0.5965 |  |
| **Time in range 70-180, pooled (%)** | **+0.4312** | 0.2191 | ±0.4382 | **+1.968** | **0.0491** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **588**, R² = **0.0473**, Adj R² = **0.0292**, F-statistic = **2.60** (p = **0.0031**), Residual SE = **65.370** on **576** df, AIC = **6596.3**, BIC = **6648.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+347.8095** | 31.8596 | ±63.7192 | **+10.917** | **9.57e-28** | *** |
| Education: graduate level (vs college) | +5.1301 | 6.1067 | ±12.2134 | +0.840 | 0.4009 |  |
| **Education: high school or below (vs college)** | **-22.7304** | 10.6193 | ±21.2386 | **-2.140** | **0.0323** | * |
| Site: UCSD (vs UAB) | -1.6198 | 7.7471 | ±15.4943 | -0.209 | 0.8344 |  |
| Site: UW (vs UAB) | -2.3991 | 6.4563 | ±12.9125 | -0.372 | 0.7102 |  |
| Age (years) | +0.0089 | 0.2709 | ±0.5418 | +0.033 | 0.9737 |  |
| BMI (kg/m2) | -0.5893 | 0.4368 | ±0.8736 | -1.349 | 0.1773 |  |
| **Hypertension** | **-12.6359** | 6.0961 | ±12.1923 | **-2.073** | **0.0382** | * |
| High cholesterol | +6.4614 | 5.5737 | ±11.1475 | +1.159 | 0.2463 |  |
| Kidney disease | +0.8464 | 11.9901 | ±23.9803 | +0.071 | 0.9437 |  |
| Circulatory disease | +4.1944 | 7.9096 | ±15.8192 | +0.530 | 0.5959 |  |
| Avg. daily time in range 70-180 (%) | +0.4226 | 0.2220 | ±0.4441 | +1.903 | 0.0570 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **588**, R² = **0.0409**, Adj R² = **0.0226**, F-statistic = **2.23** (p = **0.0118**), Residual SE = **65.592** on **576** df, AIC = **6600.3**, BIC = **6652.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.7359** | 22.6853 | ±45.3707 | **+17.136** | **8.00e-66** | *** |
| Education: graduate level (vs college) | +5.8997 | 6.0823 | ±12.1647 | +0.970 | 0.3321 |  |
| **Education: high school or below (vs college)** | **-24.7446** | 10.5945 | ±21.1891 | **-2.336** | **0.0195** | * |
| Site: UCSD (vs UAB) | -1.1542 | 7.9167 | ±15.8333 | -0.146 | 0.8841 |  |
| Site: UW (vs UAB) | -1.1855 | 6.5063 | ±13.0125 | -0.182 | 0.8554 |  |
| Age (years) | -0.0183 | 0.2715 | ±0.5431 | -0.067 | 0.9464 |  |
| BMI (kg/m2) | -0.5916 | 0.4366 | ±0.8732 | -1.355 | 0.1754 |  |
| **Hypertension** | **-13.6457** | 6.1038 | ±12.2077 | **-2.236** | **0.0254** | * |
| High cholesterol | +5.8573 | 5.6124 | ±11.2247 | +1.044 | 0.2967 |  |
| Kidney disease | -2.0659 | 11.6355 | ±23.2710 | -0.178 | 0.8591 |  |
| Circulatory disease | +4.1534 | 7.9371 | ±15.8743 | +0.523 | 0.6008 |  |
| Time < 54 (%) | -0.0669 | 2.6398 | ±5.2796 | -0.025 | 0.9798 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **588**, R² = **0.0409**, Adj R² = **0.0226**, F-statistic = **2.23** (p = **0.0118**), Residual SE = **65.592** on **576** df, AIC = **6600.3**, BIC = **6652.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.7517** | 22.6807 | ±45.3614 | **+17.140** | **7.44e-66** | *** |
| Education: graduate level (vs college) | +5.8874 | 6.0956 | ±12.1912 | +0.966 | 0.3341 |  |
| **Education: high school or below (vs college)** | **-24.7585** | 10.5962 | ±21.1925 | **-2.337** | **0.0195** | * |
| Site: UCSD (vs UAB) | -1.1754 | 7.8919 | ±15.7839 | -0.149 | 0.8816 |  |
| Site: UW (vs UAB) | -1.2155 | 6.5024 | ±13.0048 | -0.187 | 0.8517 |  |
| Age (years) | -0.0176 | 0.2724 | ±0.5447 | -0.065 | 0.9485 |  |
| BMI (kg/m2) | -0.5917 | 0.4363 | ±0.8725 | -1.356 | 0.1750 |  |
| **Hypertension** | **-13.6537** | 6.1100 | ±12.2200 | **-2.235** | **0.0254** | * |
| High cholesterol | +5.8446 | 5.6191 | ±11.2381 | +1.040 | 0.2983 |  |
| Kidney disease | -2.0575 | 11.6370 | ±23.2740 | -0.177 | 0.8597 |  |
| Circulatory disease | +4.1577 | 7.9383 | ±15.8766 | +0.524 | 0.6005 |  |
| Avg. daily time < 54 (%) | -0.1818 | 2.8833 | ±5.7665 | -0.063 | 0.9497 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **588**, R² = **0.0415**, Adj R² = **0.0232**, F-statistic = **2.27** (p = **0.0104**), Residual SE = **65.570** on **576** df, AIC = **6599.9**, BIC = **6652.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+387.4005** | 22.6179 | ±45.2358 | **+17.128** | **9.17e-66** | *** |
| Education: graduate level (vs college) | +6.1286 | 6.0864 | ±12.1728 | +1.007 | 0.3140 |  |
| **Education: high school or below (vs college)** | **-24.7432** | 10.6088 | ±21.2176 | **-2.332** | **0.0197** | * |
| Site: UCSD (vs UAB) | -0.7561 | 7.8602 | ±15.7204 | -0.096 | 0.9234 |  |
| Site: UW (vs UAB) | -0.7521 | 6.4392 | ±12.8783 | -0.117 | 0.9070 |  |
| Age (years) | -0.0240 | 0.2721 | ±0.5441 | -0.088 | 0.9297 |  |
| BMI (kg/m2) | -0.5906 | 0.4362 | ±0.8724 | -1.354 | 0.1757 |  |
| **Hypertension** | **-13.4432** | 6.1378 | ±12.2756 | **-2.190** | **0.0285** | * |
| High cholesterol | +5.9844 | 5.6028 | ±11.2057 | +1.068 | 0.2855 |  |
| Kidney disease | -2.1833 | 11.6226 | ±23.2453 | -0.188 | 0.8510 |  |
| Circulatory disease | +4.2355 | 7.9296 | ±15.8593 | +0.534 | 0.5932 |  |
| Time 54-69, pooled (%) | +0.7337 | 1.0762 | ±2.1523 | +0.682 | 0.4954 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **588**, R² = **0.0413**, Adj R² = **0.0230**, F-statistic = **2.26** (p = **0.0108**), Residual SE = **65.577** on **576** df, AIC = **6600.0**, BIC = **6652.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+387.9494** | 22.6336 | ±45.2673 | **+17.140** | **7.41e-66** | *** |
| Education: graduate level (vs college) | +6.0985 | 6.0939 | ±12.1878 | +1.001 | 0.3169 |  |
| **Education: high school or below (vs college)** | **-24.7504** | 10.6174 | ±21.2348 | **-2.331** | **0.0197** | * |
| Site: UCSD (vs UAB) | -0.8743 | 7.8603 | ±15.7206 | -0.111 | 0.9114 |  |
| Site: UW (vs UAB) | -0.8120 | 6.4377 | ±12.8755 | -0.126 | 0.8996 |  |
| Age (years) | -0.0256 | 0.2724 | ±0.5448 | -0.094 | 0.9250 |  |
| BMI (kg/m2) | -0.5913 | 0.4364 | ±0.8729 | -1.355 | 0.1755 |  |
| **Hypertension** | **-13.4903** | 6.1348 | ±12.2695 | **-2.199** | **0.0279** | * |
| High cholesterol | +5.9501 | 5.6035 | ±11.2071 | +1.062 | 0.2883 |  |
| Kidney disease | -2.1611 | 11.6158 | ±23.2316 | -0.186 | 0.8524 |  |
| Circulatory disease | +4.2131 | 7.9339 | ±15.8677 | +0.531 | 0.5954 |  |
| Avg. daily time 54-69 (%) | +0.5716 | 1.0260 | ±2.0521 | +0.557 | 0.5774 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **588**, R² = **0.0413**, Adj R² = **0.0230**, F-statistic = **2.26** (p = **0.0109**), Residual SE = **65.578** on **576** df, AIC = **6600.0**, BIC = **6652.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+387.4910** | 22.6177 | ±45.2355 | **+17.132** | **8.54e-66** | *** |
| Education: graduate level (vs college) | +6.0716 | 6.0873 | ±12.1745 | +0.997 | 0.3186 |  |
| **Education: high school or below (vs college)** | **-24.6700** | 10.6001 | ±21.2002 | **-2.327** | **0.0199** | * |
| Site: UCSD (vs UAB) | -0.7322 | 7.8795 | ±15.7591 | -0.093 | 0.9260 |  |
| Site: UW (vs UAB) | -0.7656 | 6.4612 | ±12.9225 | -0.118 | 0.9057 |  |
| Age (years) | -0.0223 | 0.2721 | ±0.5442 | -0.082 | 0.9347 |  |
| BMI (kg/m2) | -0.5895 | 0.4360 | ±0.8721 | -1.352 | 0.1764 |  |
| **Hypertension** | **-13.4737** | 6.1344 | ±12.2688 | **-2.196** | **0.0281** | * |
| High cholesterol | +6.0013 | 5.6070 | ±11.2140 | +1.070 | 0.2845 |  |
| Kidney disease | -2.1649 | 11.6300 | ±23.2600 | -0.186 | 0.8523 |  |
| Circulatory disease | +4.1886 | 7.9304 | ±15.8609 | +0.528 | 0.5974 |  |
| Time < 70 (%) | +0.4694 | 0.8332 | ±1.6664 | +0.563 | 0.5731 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **588**, R² = **0.0412**, Adj R² = **0.0228**, F-statistic = **2.25** (p = **0.0112**), Residual SE = **65.583** on **576** df, AIC = **6600.1**, BIC = **6652.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.0607** | 22.6363 | ±45.2726 | **+17.143** | **7.05e-66** | *** |
| Education: graduate level (vs college) | +6.0636 | 6.0974 | ±12.1949 | +0.994 | 0.3200 |  |
| **Education: high school or below (vs college)** | **-24.6960** | 10.6061 | ±21.2122 | **-2.328** | **0.0199** | * |
| Site: UCSD (vs UAB) | -0.8727 | 7.8709 | ±15.7417 | -0.111 | 0.9117 |  |
| Site: UW (vs UAB) | -0.8323 | 6.4538 | ±12.9075 | -0.129 | 0.8974 |  |
| Age (years) | -0.0246 | 0.2726 | ±0.5451 | -0.090 | 0.9282 |  |
| BMI (kg/m2) | -0.5906 | 0.4363 | ±0.8726 | -1.354 | 0.1758 |  |
| **Hypertension** | **-13.5136** | 6.1333 | ±12.2665 | **-2.203** | **0.0276** | * |
| High cholesterol | +5.9647 | 5.6079 | ±11.2158 | +1.064 | 0.2875 |  |
| Kidney disease | -2.1534 | 11.6210 | ±23.2420 | -0.185 | 0.8530 |  |
| Circulatory disease | +4.1780 | 7.9347 | ±15.8695 | +0.527 | 0.5985 |  |
| Avg. daily time < 70 (%) | +0.3746 | 0.8051 | ±1.6102 | +0.465 | 0.6418 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **588**, R² = **0.0503**, Adj R² = **0.0322**, F-statistic = **2.78** (p = **0.0016**), Residual SE = **65.268** on **576** df, AIC = **6594.5**, BIC = **6647.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+280.5287** | 48.9210 | ±97.8420 | **+5.734** | **9.79e-09** | *** |
| Education: graduate level (vs college) | +5.1939 | 6.0887 | ±12.1774 | +0.853 | 0.3936 |  |
| **Education: high school or below (vs college)** | **-22.7163** | 10.5145 | ±21.0289 | **-2.160** | **0.0307** | * |
| Site: UCSD (vs UAB) | -1.7861 | 7.7460 | ±15.4919 | -0.231 | 0.8176 |  |
| Site: UW (vs UAB) | -2.6477 | 6.4345 | ±12.8691 | -0.411 | 0.6807 |  |
| Age (years) | -0.0222 | 0.2684 | ±0.5369 | -0.083 | 0.9342 |  |
| BMI (kg/m2) | -0.6017 | 0.4367 | ±0.8734 | -1.378 | 0.1682 |  |
| **Hypertension** | **-12.7562** | 6.0580 | ±12.1161 | **-2.106** | **0.0352** | * |
| High cholesterol | +5.5033 | 5.5672 | ±11.1345 | +0.989 | 0.3229 |  |
| Kidney disease | -0.3282 | 11.6667 | ±23.3333 | -0.028 | 0.9776 |  |
| Circulatory disease | +4.5591 | 7.8867 | ±15.7734 | +0.578 | 0.5632 |  |
| **Time 54-250, pooled (%)** | **+1.1091** | 0.4379 | ±0.8759 | **+2.533** | **0.0113** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **588**, R² = **0.0516**, Adj R² = **0.0334**, F-statistic = **2.85** (p = **0.0012**), Residual SE = **65.226** on **576** df, AIC = **6593.7**, BIC = **6646.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+260.9390** | 51.0205 | ±102.0410 | **+5.114** | **3.15e-07** | *** |
| Education: graduate level (vs college) | +5.0574 | 6.0907 | ±12.1815 | +0.830 | 0.4063 |  |
| **Education: high school or below (vs college)** | **-22.2476** | 10.5224 | ±21.0447 | **-2.114** | **0.0345** | * |
| Site: UCSD (vs UAB) | -1.6872 | 7.7297 | ±15.4595 | -0.218 | 0.8272 |  |
| Site: UW (vs UAB) | -2.6829 | 6.4333 | ±12.8666 | -0.417 | 0.6767 |  |
| Age (years) | -0.0143 | 0.2686 | ±0.5372 | -0.053 | 0.9575 |  |
| BMI (kg/m2) | -0.6086 | 0.4368 | ±0.8735 | -1.394 | 0.1635 |  |
| **Hypertension** | **-12.6867** | 6.0567 | ±12.1133 | **-2.095** | **0.0362** | * |
| High cholesterol | +5.5400 | 5.5648 | ±11.1296 | +0.996 | 0.3195 |  |
| Kidney disease | +0.1159 | 11.7015 | ±23.4030 | +0.010 | 0.9921 |  |
| Circulatory disease | +4.6810 | 7.8859 | ±15.7718 | +0.594 | 0.5528 |  |
| **Avg. daily time 54-250 (%)** | **+1.3014** | 0.4600 | ±0.9200 | **+2.829** | **0.0047** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **588**, R² = **0.0446**, Adj R² = **0.0263**, F-statistic = **2.44** (p = **0.0055**), Residual SE = **65.466** on **576** df, AIC = **6598.0**, BIC = **6650.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.5176** | 22.7706 | ±45.5412 | **+17.062** | **2.83e-65** | *** |
| Education: graduate level (vs college) | +5.5202 | 6.0930 | ±12.1860 | +0.906 | 0.3649 |  |
| **Education: high school or below (vs college)** | **-23.4674** | 10.6388 | ±21.2775 | **-2.206** | **0.0274** | * |
| Site: UCSD (vs UAB) | -1.1502 | 7.7785 | ±15.5571 | -0.148 | 0.8825 |  |
| Site: UW (vs UAB) | -1.6151 | 6.4479 | ±12.8958 | -0.250 | 0.8022 |  |
| Age (years) | +0.0074 | 0.2717 | ±0.5435 | +0.027 | 0.9782 |  |
| BMI (kg/m2) | -0.5826 | 0.4363 | ±0.8725 | -1.336 | 0.1817 |  |
| **Hypertension** | **-12.7480** | 6.1337 | ±12.2674 | **-2.078** | **0.0377** | * |
| High cholesterol | +6.7018 | 5.6094 | ±11.2187 | +1.195 | 0.2322 |  |
| Kidney disease | +0.2904 | 12.0227 | ±24.0453 | +0.024 | 0.9807 |  |
| Circulatory disease | +4.0693 | 7.9282 | ±15.8563 | +0.513 | 0.6078 |  |
| Time 181-250, pooled (%) | -0.4679 | 0.3301 | ±0.6602 | -1.418 | 0.1563 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **588**, R² = **0.0444**, Adj R² = **0.0261**, F-statistic = **2.43** (p = **0.0058**), Residual SE = **65.473** on **576** df, AIC = **6598.2**, BIC = **6650.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.7487** | 22.7667 | ±45.5334 | **+17.075** | **2.27e-65** | *** |
| Education: graduate level (vs college) | +5.5327 | 6.0990 | ±12.1980 | +0.907 | 0.3643 |  |
| **Education: high school or below (vs college)** | **-23.4946** | 10.6353 | ±21.2707 | **-2.209** | **0.0272** | * |
| Site: UCSD (vs UAB) | -1.2547 | 7.7810 | ±15.5621 | -0.161 | 0.8719 |  |
| Site: UW (vs UAB) | -1.6670 | 6.4502 | ±12.9004 | -0.258 | 0.7961 |  |
| Age (years) | +0.0032 | 0.2716 | ±0.5431 | +0.012 | 0.9907 |  |
| BMI (kg/m2) | -0.5832 | 0.4366 | ±0.8732 | -1.336 | 0.1816 |  |
| **Hypertension** | **-12.7974** | 6.1396 | ±12.2792 | **-2.084** | **0.0371** | * |
| High cholesterol | +6.6650 | 5.6072 | ±11.2143 | +1.189 | 0.2346 |  |
| Kidney disease | +0.1681 | 12.0374 | ±24.0748 | +0.014 | 0.9889 |  |
| Circulatory disease | +4.0644 | 7.9383 | ±15.8765 | +0.512 | 0.6087 |  |
| Avg. daily time 181-250 (%) | -0.4422 | 0.3269 | ±0.6539 | -1.353 | 0.1762 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **588**, R² = **0.0483**, Adj R² = **0.0302**, F-statistic = **2.66** (p = **0.0025**), Residual SE = **65.337** on **576** df, AIC = **6595.7**, BIC = **6648.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+389.2950** | 22.7257 | ±45.4514 | **+17.130** | **8.84e-66** | *** |
| Education: graduate level (vs college) | +5.2627 | 6.1040 | ±12.2081 | +0.862 | 0.3886 |  |
| **Education: high school or below (vs college)** | **-22.6045** | 10.5968 | ±21.1936 | **-2.133** | **0.0329** | * |
| Site: UCSD (vs UAB) | -1.2641 | 7.7357 | ±15.4714 | -0.163 | 0.8702 |  |
| Site: UW (vs UAB) | -2.0797 | 6.4489 | ±12.8977 | -0.322 | 0.7471 |  |
| Age (years) | +0.0048 | 0.2703 | ±0.5407 | +0.018 | 0.9858 |  |
| BMI (kg/m2) | -0.5857 | 0.4364 | ±0.8728 | -1.342 | 0.1795 |  |
| **Hypertension** | **-12.3698** | 6.1201 | ±12.2402 | **-2.021** | **0.0433** | * |
| High cholesterol | +6.5884 | 5.5713 | ±11.1425 | +1.183 | 0.2370 |  |
| Kidney disease | +0.9203 | 11.9531 | ±23.9063 | +0.077 | 0.9386 |  |
| Circulatory disease | +4.2230 | 7.8933 | ±15.7866 | +0.535 | 0.5926 |  |
| **Time > 180 (%)** | **-0.4554** | 0.2208 | ±0.4416 | **-2.063** | **0.0391** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **588**, R² = **0.0481**, Adj R² = **0.0299**, F-statistic = **2.64** (p = **0.0026**), Residual SE = **65.346** on **576** df, AIC = **6595.9**, BIC = **6648.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+389.4065** | 22.7380 | ±45.4759 | **+17.126** | **9.53e-66** | *** |
| Education: graduate level (vs college) | +5.2743 | 6.1084 | ±12.2167 | +0.863 | 0.3879 |  |
| **Education: high school or below (vs college)** | **-22.5596** | 10.6075 | ±21.2151 | **-2.127** | **0.0334** | * |
| Site: UCSD (vs UAB) | -1.3400 | 7.7381 | ±15.4762 | -0.173 | 0.8625 |  |
| Site: UW (vs UAB) | -2.0757 | 6.4528 | ±12.9056 | -0.322 | 0.7477 |  |
| Age (years) | +0.0031 | 0.2705 | ±0.5409 | +0.011 | 0.9909 |  |
| BMI (kg/m2) | -0.5882 | 0.4369 | ±0.8738 | -1.346 | 0.1782 |  |
| **Hypertension** | **-12.4222** | 6.1256 | ±12.2512 | **-2.028** | **0.0426** | * |
| High cholesterol | +6.6169 | 5.5721 | ±11.1442 | +1.188 | 0.2350 |  |
| Kidney disease | +0.9264 | 11.9879 | ±23.9759 | +0.077 | 0.9384 |  |
| Circulatory disease | +4.2294 | 7.9010 | ±15.8020 | +0.535 | 0.5924 |  |
| **Avg. daily time > 180 (%)** | **-0.4488** | 0.2276 | ±0.4552 | **-1.972** | **0.0486** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **588**, R² = **0.0461**, Adj R² = **0.0279**, F-statistic = **2.53** (p = **0.0040**), Residual SE = **65.413** on **576** df, AIC = **6597.1**, BIC = **6649.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+389.1392** | 22.6981 | ±45.3961 | **+17.144** | **6.95e-66** | *** |
| Education: graduate level (vs college) | +5.3370 | 6.1136 | ±12.2273 | +0.873 | 0.3827 |  |
| **Education: high school or below (vs college)** | **-23.5539** | 10.5377 | ±21.0754 | **-2.235** | **0.0254** | * |
| Site: UCSD (vs UAB) | -1.4553 | 7.7609 | ±15.5217 | -0.188 | 0.8513 |  |
| Site: UW (vs UAB) | -1.8293 | 6.4603 | ±12.9206 | -0.283 | 0.7771 |  |
| Age (years) | -0.0159 | 0.2709 | ±0.5419 | -0.059 | 0.9532 |  |
| BMI (kg/m2) | -0.5713 | 0.4354 | ±0.8708 | -1.312 | 0.1895 |  |
| **Hypertension** | **-12.5438** | 6.1189 | ±12.2379 | **-2.050** | **0.0404** | * |
| High cholesterol | +6.4417 | 5.5741 | ±11.1481 | +1.156 | 0.2478 |  |
| Kidney disease | -0.8704 | 11.7536 | ±23.5073 | -0.074 | 0.9410 |  |
| Circulatory disease | +4.4063 | 7.8994 | ±15.7988 | +0.558 | 0.5770 |  |
| Nocturnal time > 180 (%) | -0.3927 | 0.2508 | ±0.5015 | -1.566 | 0.1173 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **588**, R² = **0.0416**, Adj R² = **0.0233**, F-statistic = **2.27** (p = **0.0102**), Residual SE = **65.568** on **576** df, AIC = **6599.9**, BIC = **6652.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+388.9674** | 22.7199 | ±45.4399 | **+17.120** | **1.05e-65** | *** |
| Education: graduate level (vs college) | +5.6434 | 6.1050 | ±12.2099 | +0.924 | 0.3553 |  |
| **Education: high school or below (vs college)** | **-24.2464** | 10.6030 | ±21.2060 | **-2.287** | **0.0222** | * |
| Site: UCSD (vs UAB) | -0.9102 | 7.8636 | ±15.7273 | -0.116 | 0.9079 |  |
| Site: UW (vs UAB) | -1.2726 | 6.4376 | ±12.8752 | -0.198 | 0.8433 |  |
| Age (years) | -0.0010 | 0.2744 | ±0.5488 | -0.004 | 0.9969 |  |
| BMI (kg/m2) | -0.6065 | 0.4374 | ±0.8747 | -1.387 | 0.1655 |  |
| **Hypertension** | **-13.1517** | 6.1431 | ±12.2862 | **-2.141** | **0.0323** | * |
| High cholesterol | +6.0527 | 5.6025 | ±11.2050 | +1.080 | 0.2800 |  |
| Kidney disease | -1.2097 | 11.8972 | ±23.7944 | -0.102 | 0.9190 |  |
| Circulatory disease | +3.9753 | 7.9968 | ±15.9937 | +0.497 | 0.6191 |  |
| Any reading > 250 during wear (0/1) | -4.0743 | 6.5443 | ±13.0886 | -0.623 | 0.5336 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **588**, R² = **0.0506**, Adj R² = **0.0325**, F-statistic = **2.79** (p = **0.0015**), Residual SE = **65.259** on **576** df, AIC = **6594.3**, BIC = **6646.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+390.6177** | 22.5993 | ±45.1987 | **+17.284** | **6.16e-67** | *** |
| Education: graduate level (vs college) | +5.2331 | 6.0909 | ±12.1818 | +0.859 | 0.3902 |  |
| **Education: high school or below (vs college)** | **-22.4902** | 10.5238 | ±21.0475 | **-2.137** | **0.0326** | * |
| Site: UCSD (vs UAB) | -1.4179 | 7.7404 | ±15.4808 | -0.183 | 0.8547 |  |
| Site: UW (vs UAB) | -2.3592 | 6.4239 | ±12.8478 | -0.367 | 0.7134 |  |
| Age (years) | -0.0231 | 0.2685 | ±0.5370 | -0.086 | 0.9314 |  |
| BMI (kg/m2) | -0.5985 | 0.4364 | ±0.8729 | -1.371 | 0.1703 |  |
| **Hypertension** | **-12.6337** | 6.0671 | ±12.1341 | **-2.082** | **0.0373** | * |
| High cholesterol | +5.6380 | 5.5632 | ±11.1265 | +1.013 | 0.3109 |  |
| Kidney disease | -0.3351 | 11.6656 | ±23.3312 | -0.029 | 0.9771 |  |
| Circulatory disease | +4.5303 | 7.8751 | ±15.7503 | +0.575 | 0.5651 |  |
| **Time > 250 (%)** | **-1.1399** | 0.4393 | ±0.8786 | **-2.595** | **0.0095** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 588)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **588**, R² = **0.0519**, Adj R² = **0.0338**, F-statistic = **2.87** (p = **0.0011**), Residual SE = **65.215** on **576** df, AIC = **6593.5**, BIC = **6646.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+390.6537** | 22.6112 | ±45.2224 | **+17.277** | **7.01e-67** | *** |
| Education: graduate level (vs college) | +5.1446 | 6.0902 | ±12.1804 | +0.845 | 0.3983 |  |
| **Education: high school or below (vs college)** | **-21.9849** | 10.5410 | ±21.0820 | **-2.086** | **0.0370** | * |
| Site: UCSD (vs UAB) | -1.3818 | 7.7251 | ±15.4503 | -0.179 | 0.8580 |  |
| Site: UW (vs UAB) | -2.3698 | 6.4248 | ±12.8497 | -0.369 | 0.7122 |  |
| Age (years) | -0.0194 | 0.2685 | ±0.5371 | -0.072 | 0.9423 |  |
| BMI (kg/m2) | -0.6068 | 0.4369 | ±0.8739 | -1.389 | 0.1649 |  |
| **Hypertension** | **-12.5518** | 6.0664 | ±12.1327 | **-2.069** | **0.0385** | * |
| High cholesterol | +5.6858 | 5.5596 | ±11.1192 | +1.023 | 0.3065 |  |
| Kidney disease | +0.1056 | 11.6976 | ±23.3951 | +0.009 | 0.9928 |  |
| Circulatory disease | +4.6501 | 7.8749 | ±15.7498 | +0.590 | 0.5549 |  |
| **Avg. daily time > 250 (%)** | **-1.3466** | 0.4771 | ±0.9542 | **-2.822** | **0.0048** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 577; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **577**, R² = **0.1182**, Adj R² = **0.1027**, F-statistic = **7.59** (p = **2.06e-11**), Residual SE = **16.872** on **566** df, AIC = **4909.2**, BIC = **4957.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1190** | 6.0827 | ±12.1654 | **+11.034** | **2.61e-28** | *** |
| Education: graduate level (vs college) | -2.6214 | 1.5393 | ±3.0785 | -1.703 | 0.0886 | . |
| Education: high school or below (vs college) | +0.3677 | 2.6656 | ±5.3312 | +0.138 | 0.8903 |  |
| Site: UCSD (vs UAB) | +1.9482 | 2.0475 | ±4.0949 | +0.952 | 0.3413 |  |
| Site: UW (vs UAB) | -3.1233 | 1.6824 | ±3.3648 | -1.856 | 0.0634 | . |
| **Age (years)** | **-0.3932** | 0.0703 | ±0.1407 | **-5.590** | **2.27e-08** | *** |
| **BMI (kg/m2)** | **+0.2972** | 0.1095 | ±0.2190 | **+2.713** | **0.0067** | ** |
| Hypertension | +1.3338 | 1.6243 | ±3.2486 | +0.821 | 0.4115 |  |
| High cholesterol | +1.8563 | 1.5172 | ±3.0344 | +1.224 | 0.2211 |  |
| Kidney disease | -0.9888 | 3.0864 | ±6.1728 | -0.320 | 0.7487 |  |
| Circulatory disease | -2.4511 | 1.9500 | ±3.8999 | -1.257 | 0.2088 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **577**, R² = **0.1328**, Adj R² = **0.1159**, F-statistic = **7.87** (p = **8.89e-13**), Residual SE = **16.747** on **565** df, AIC = **4901.6**, BIC = **4953.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.1031** | 7.9721 | ±15.9443 | **+6.787** | **1.15e-11** | *** |
| Education: graduate level (vs college) | -2.2575 | 1.5416 | ±3.0831 | -1.464 | 0.1431 |  |
| Education: high school or below (vs college) | -0.4541 | 2.6307 | ±5.2614 | -0.173 | 0.8629 |  |
| Site: UCSD (vs UAB) | +1.7601 | 2.0401 | ±4.0803 | +0.863 | 0.3883 |  |
| Site: UW (vs UAB) | -2.7521 | 1.6733 | ±3.3466 | -1.645 | 0.1000 |  |
| **Age (years)** | **-0.4207** | 0.0707 | ±0.1413 | **-5.954** | **2.62e-09** | *** |
| **BMI (kg/m2)** | **+0.2717** | 0.1076 | ±0.2152 | **+2.525** | **0.0116** | * |
| Hypertension | +0.8684 | 1.6269 | ±3.2537 | +0.534 | 0.5935 |  |
| High cholesterol | +1.5203 | 1.5212 | ±3.0423 | +0.999 | 0.3176 |  |
| Kidney disease | -1.2548 | 2.9860 | ±5.9720 | -0.420 | 0.6743 |  |
| Circulatory disease | -2.3033 | 1.9620 | ±3.9241 | -1.174 | 0.2404 |  |
| **HbA1c (%)** | **+2.6515** | 1.0813 | ±2.1625 | **+2.452** | **0.0142** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **577**, R² = **0.1265**, Adj R² = **0.1095**, F-statistic = **7.44** (p = **5.49e-12**), Residual SE = **16.807** on **565** df, AIC = **4905.7**, BIC = **4958.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.8472** | 7.0267 | ±14.0534 | **+8.517** | **1.64e-17** | *** |
| Education: graduate level (vs college) | -2.5935 | 1.5372 | ±3.0744 | -1.687 | 0.0916 | . |
| Education: high school or below (vs college) | -0.1807 | 2.6530 | ±5.3061 | -0.068 | 0.9457 |  |
| Site: UCSD (vs UAB) | +1.8215 | 2.0451 | ±4.0902 | +0.891 | 0.3731 |  |
| Site: UW (vs UAB) | -3.0360 | 1.6728 | ±3.3456 | -1.815 | 0.0695 | . |
| **Age (years)** | **-0.3974** | 0.0702 | ±0.1404 | **-5.662** | **1.50e-08** | *** |
| **BMI (kg/m2)** | **+0.2867** | 0.1094 | ±0.2188 | **+2.621** | **0.0088** | ** |
| Hypertension | +0.8892 | 1.6431 | ±3.2863 | +0.541 | 0.5884 |  |
| High cholesterol | +1.5898 | 1.5190 | ±3.0379 | +1.047 | 0.2953 |  |
| Kidney disease | -1.6388 | 3.0145 | ±6.0289 | -0.544 | 0.5867 |  |
| Circulatory disease | -2.4968 | 1.9689 | ±3.9377 | -1.268 | 0.2047 |  |
| **Mean glucose (mg/dL)** | **+0.0679** | 0.0337 | ±0.0673 | **+2.016** | **0.0438** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **577**, R² = **0.1265**, Adj R² = **0.1095**, F-statistic = **7.44** (p = **5.49e-12**), Residual SE = **16.807** on **565** df, AIC = **4905.7**, BIC = **4958.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.4546** | 10.2105 | ±20.4210 | **+4.941** | **7.75e-07** | *** |
| Education: graduate level (vs college) | -2.5935 | 1.5372 | ±3.0744 | -1.687 | 0.0916 | . |
| Education: high school or below (vs college) | -0.1807 | 2.6530 | ±5.3061 | -0.068 | 0.9457 |  |
| Site: UCSD (vs UAB) | +1.8215 | 2.0451 | ±4.0902 | +0.891 | 0.3731 |  |
| Site: UW (vs UAB) | -3.0360 | 1.6728 | ±3.3456 | -1.815 | 0.0695 | . |
| **Age (years)** | **-0.3974** | 0.0702 | ±0.1404 | **-5.662** | **1.50e-08** | *** |
| **BMI (kg/m2)** | **+0.2867** | 0.1094 | ±0.2188 | **+2.621** | **0.0088** | ** |
| Hypertension | +0.8892 | 1.6431 | ±3.2863 | +0.541 | 0.5884 |  |
| High cholesterol | +1.5898 | 1.5190 | ±3.0379 | +1.047 | 0.2953 |  |
| Kidney disease | -1.6388 | 3.0145 | ±6.0289 | -0.544 | 0.5867 |  |
| Circulatory disease | -2.4968 | 1.9689 | ±3.9377 | -1.268 | 0.2047 |  |
| **GMI (%)** | **+2.8376** | 1.4078 | ±2.8155 | **+2.016** | **0.0438** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **577**, R² = **0.1226**, Adj R² = **0.1056**, F-statistic = **7.18** (p = **1.69e-11**), Residual SE = **16.845** on **565** df, AIC = **4908.3**, BIC = **4960.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.7994** | 7.0225 | ±14.0450 | **+8.800** | **1.37e-18** | *** |
| Education: graduate level (vs college) | -2.6152 | 1.5398 | ±3.0796 | -1.698 | 0.0894 | . |
| Education: high school or below (vs college) | +0.0135 | 2.6465 | ±5.2930 | +0.005 | 0.9959 |  |
| Site: UCSD (vs UAB) | +1.8294 | 2.0520 | ±4.1040 | +0.892 | 0.3727 |  |
| Site: UW (vs UAB) | -3.1054 | 1.6784 | ±3.3567 | -1.850 | 0.0643 | . |
| **Age (years)** | **-0.3896** | 0.0704 | ±0.1408 | **-5.533** | **3.15e-08** | *** |
| **BMI (kg/m2)** | **+0.2824** | 0.1097 | ±0.2194 | **+2.574** | **0.0101** | * |
| Hypertension | +1.0051 | 1.6428 | ±3.2855 | +0.612 | 0.5407 |  |
| High cholesterol | +1.6221 | 1.5153 | ±3.0307 | +1.070 | 0.2844 |  |
| Kidney disease | -1.1672 | 3.0229 | ±6.0459 | -0.386 | 0.6994 |  |
| Circulatory disease | -2.4653 | 1.9646 | ±3.9291 | -1.255 | 0.2095 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0493 | 0.0316 | ±0.0632 | +1.558 | 0.1192 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **577**, R² = **0.1268**, Adj R² = **0.1098**, F-statistic = **7.46** (p = **5.06e-12**), Residual SE = **16.805** on **565** df, AIC = **4905.5**, BIC = **4957.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.6672** | 6.1530 | ±12.3060 | **+10.510** | **7.78e-26** | *** |
| Education: graduate level (vs college) | -2.4692 | 1.5411 | ±3.0822 | -1.602 | 0.1091 |  |
| Education: high school or below (vs college) | -0.4887 | 2.6862 | ±5.3724 | -0.182 | 0.8556 |  |
| Site: UCSD (vs UAB) | +1.8803 | 2.0311 | ±4.0622 | +0.926 | 0.3546 |  |
| Site: UW (vs UAB) | -2.7990 | 1.6775 | ±3.3549 | -1.669 | 0.0952 | . |
| **Age (years)** | **-0.4125** | 0.0711 | ±0.1421 | **-5.805** | **6.44e-09** | *** |
| **BMI (kg/m2)** | **+0.2990** | 0.1090 | ±0.2181 | **+2.742** | **0.0061** | ** |
| Hypertension | +0.9439 | 1.6319 | ±3.2638 | +0.578 | 0.5630 |  |
| High cholesterol | +1.7454 | 1.5197 | ±3.0394 | +1.149 | 0.2507 |  |
| Kidney disease | -2.2187 | 3.1049 | ±6.2097 | -0.715 | 0.4749 |  |
| Circulatory disease | -2.3329 | 1.9604 | ±3.9208 | -1.190 | 0.2340 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.1451** | 0.0695 | ±0.1391 | **+2.086** | **0.0370** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **577**, R² = **0.1252**, Adj R² = **0.1081**, F-statistic = **7.35** (p = **8.18e-12**), Residual SE = **16.821** on **565** df, AIC = **4906.6**, BIC = **4958.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.9111** | 6.1598 | ±12.3197 | **+10.538** | **5.78e-26** | *** |
| Education: graduate level (vs college) | -2.4626 | 1.5397 | ±3.0795 | -1.599 | 0.1097 |  |
| Education: high school or below (vs college) | -0.4912 | 2.7014 | ±5.4028 | -0.182 | 0.8557 |  |
| Site: UCSD (vs UAB) | +1.8466 | 2.0337 | ±4.0674 | +0.908 | 0.3639 |  |
| Site: UW (vs UAB) | -2.8724 | 1.6794 | ±3.3588 | -1.710 | 0.0872 | . |
| **Age (years)** | **-0.4122** | 0.0714 | ±0.1429 | **-5.771** | **7.88e-09** | *** |
| **BMI (kg/m2)** | **+0.2995** | 0.1092 | ±0.2185 | **+2.741** | **0.0061** | ** |
| Hypertension | +1.0070 | 1.6304 | ±3.2607 | +0.618 | 0.5368 |  |
| High cholesterol | +1.7299 | 1.5244 | ±3.0487 | +1.135 | 0.2565 |  |
| Kidney disease | -2.1151 | 3.1242 | ±6.2484 | -0.677 | 0.4984 |  |
| Circulatory disease | -2.3028 | 1.9650 | ±3.9300 | -1.172 | 0.2412 |  |
| Avg. daily SD (mg/dL) | +0.1514 | 0.0844 | ±0.1688 | +1.794 | 0.0728 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **577**, R² = **0.1252**, Adj R² = **0.1082**, F-statistic = **7.35** (p = **8.04e-12**), Residual SE = **16.820** on **565** df, AIC = **4906.6**, BIC = **4958.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.9624** | 6.3407 | ±12.6814 | **+9.930** | **3.09e-23** | *** |
| Education: graduate level (vs college) | -2.4701 | 1.5395 | ±3.0789 | -1.605 | 0.1086 |  |
| Education: high school or below (vs college) | -0.3543 | 2.6954 | ±5.3908 | -0.131 | 0.8954 |  |
| Site: UCSD (vs UAB) | +1.8989 | 2.0304 | ±4.0608 | +0.935 | 0.3497 |  |
| Site: UW (vs UAB) | -2.7606 | 1.6811 | ±3.3623 | -1.642 | 0.1006 |  |
| **Age (years)** | **-0.4185** | 0.0717 | ±0.1435 | **-5.835** | **5.39e-09** | *** |
| **BMI (kg/m2)** | **+0.3046** | 0.1092 | ±0.2185 | **+2.789** | **0.0053** | ** |
| Hypertension | +1.1030 | 1.6237 | ±3.2475 | +0.679 | 0.4969 |  |
| High cholesterol | +1.8649 | 1.5169 | ±3.0338 | +1.229 | 0.2189 |  |
| Kidney disease | -2.1747 | 3.1574 | ±6.3147 | -0.689 | 0.4910 |  |
| Circulatory disease | -2.2968 | 1.9477 | ±3.8954 | -1.179 | 0.2383 |  |
| **CV (%)** | **+0.2640** | 0.1275 | ±0.2549 | **+2.071** | **0.0383** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **577**, R² = **0.1308**, Adj R² = **0.1139**, F-statistic = **7.73** (p = **1.60e-12**), Residual SE = **16.767** on **565** df, AIC = **4902.9**, BIC = **4955.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+77.7535** | 7.0954 | ±14.1908 | **+10.958** | **6.06e-28** | *** |
| Education: graduate level (vs college) | -2.5686 | 1.5327 | ±3.0653 | -1.676 | 0.0938 | . |
| Education: high school or below (vs college) | -0.5556 | 2.6872 | ±5.3744 | -0.207 | 0.8362 |  |
| Site: UCSD (vs UAB) | +1.7838 | 2.0173 | ±4.0346 | +0.884 | 0.3766 |  |
| Site: UW (vs UAB) | -2.8260 | 1.6716 | ±3.3432 | -1.691 | 0.0909 | . |
| **Age (years)** | **-0.4287** | 0.0710 | ±0.1421 | **-6.035** | **1.59e-09** | *** |
| **BMI (kg/m2)** | **+0.2981** | 0.1089 | ±0.2178 | **+2.737** | **0.0062** | ** |
| Hypertension | +1.0605 | 1.6202 | ±3.2405 | +0.655 | 0.5128 |  |
| High cholesterol | +1.8503 | 1.5113 | ±3.0226 | +1.224 | 0.2208 |  |
| Kidney disease | -2.1516 | 3.1047 | ±6.2093 | -0.693 | 0.4883 |  |
| Circulatory disease | -2.3951 | 1.9478 | ±3.8956 | -1.230 | 0.2188 |  |
| **Mean / SD ratio** | **-1.6172** | 0.5458 | ±1.0917 | **-2.963** | **0.0030** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **577**, R² = **0.1269**, Adj R² = **0.1099**, F-statistic = **7.46** (p = **4.96e-12**), Residual SE = **16.804** on **565** df, AIC = **4905.5**, BIC = **4957.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+75.9527** | 7.1222 | ±14.2445 | **+10.664** | **1.50e-26** | *** |
| Education: graduate level (vs college) | -2.5633 | 1.5340 | ±3.0680 | -1.671 | 0.0947 | . |
| Education: high school or below (vs college) | -0.4621 | 2.6942 | ±5.3883 | -0.172 | 0.8638 |  |
| Site: UCSD (vs UAB) | +1.6822 | 2.0241 | ±4.0483 | +0.831 | 0.4059 |  |
| Site: UW (vs UAB) | -2.9572 | 1.6783 | ±3.3566 | -1.762 | 0.0781 | . |
| **Age (years)** | **-0.4255** | 0.0717 | ±0.1434 | **-5.934** | **2.95e-09** | *** |
| **BMI (kg/m2)** | **+0.2959** | 0.1089 | ±0.2178 | **+2.717** | **0.0066** | ** |
| Hypertension | +1.1833 | 1.6216 | ±3.2431 | +0.730 | 0.4655 |  |
| High cholesterol | +1.8060 | 1.5157 | ±3.0313 | +1.192 | 0.2334 |  |
| Kidney disease | -1.8449 | 3.1107 | ±6.2213 | -0.593 | 0.5531 |  |
| Circulatory disease | -2.3510 | 1.9507 | ±3.9015 | -1.205 | 0.2281 |  |
| **Avg. daily mean/SD** | **-1.1019** | 0.4515 | ±0.9030 | **-2.440** | **0.0147** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **577**, R² = **0.1201**, Adj R² = **0.1029**, F-statistic = **7.01** (p = **3.51e-11**), Residual SE = **16.870** on **565** df, AIC = **4910.0**, BIC = **4962.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.8320** | 6.5570 | ±13.1139 | **+9.735** | **2.14e-22** | *** |
| Education: graduate level (vs college) | -2.5748 | 1.5386 | ±3.0772 | -1.673 | 0.0942 | . |
| Education: high school or below (vs college) | +0.1266 | 2.6900 | ±5.3800 | +0.047 | 0.9625 |  |
| Site: UCSD (vs UAB) | +1.8272 | 2.0445 | ±4.0891 | +0.894 | 0.3715 |  |
| Site: UW (vs UAB) | -2.9090 | 1.6907 | ±3.3814 | -1.721 | 0.0853 | . |
| **Age (years)** | **-0.3934** | 0.0704 | ±0.1408 | **-5.587** | **2.31e-08** | *** |
| **BMI (kg/m2)** | **+0.2938** | 0.1099 | ±0.2198 | **+2.673** | **0.0075** | ** |
| Hypertension | +1.2549 | 1.6284 | ±3.2569 | +0.771 | 0.4409 |  |
| High cholesterol | +1.8884 | 1.5191 | ±3.0381 | +1.243 | 0.2138 |  |
| Kidney disease | -1.1028 | 3.0979 | ±6.1957 | -0.356 | 0.7219 |  |
| Circulatory disease | -2.4173 | 1.9547 | ±3.9093 | -1.237 | 0.2162 |  |
| MAG (mg/dL/h) | +0.0817 | 0.0773 | ±0.1547 | +1.056 | 0.2909 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **577**, R² = **0.1247**, Adj R² = **0.1077**, F-statistic = **7.32** (p = **9.26e-12**), Residual SE = **16.825** on **565** df, AIC = **4906.9**, BIC = **4959.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.6845** | 6.2572 | ±12.5144 | **+10.178** | **2.49e-24** | *** |
| Education: graduate level (vs college) | -2.4570 | 1.5396 | ±3.0791 | -1.596 | 0.1105 |  |
| Education: high school or below (vs college) | -0.4404 | 2.7068 | ±5.4137 | -0.163 | 0.8708 |  |
| Site: UCSD (vs UAB) | +1.7971 | 2.0338 | ±4.0676 | +0.884 | 0.3769 |  |
| Site: UW (vs UAB) | -2.8984 | 1.6809 | ±3.3617 | -1.724 | 0.0846 | . |
| **Age (years)** | **-0.4100** | 0.0716 | ±0.1432 | **-5.725** | **1.03e-08** | *** |
| **BMI (kg/m2)** | **+0.3061** | 0.1094 | ±0.2188 | **+2.797** | **0.0052** | ** |
| Hypertension | +1.0779 | 1.6289 | ±3.2578 | +0.662 | 0.5081 |  |
| High cholesterol | +1.7485 | 1.5221 | ±3.0443 | +1.149 | 0.2507 |  |
| Kidney disease | -1.9943 | 3.1209 | ±6.2419 | -0.639 | 0.5228 |  |
| Circulatory disease | -2.3790 | 1.9592 | ±3.9184 | -1.214 | 0.2247 |  |
| Avg. daily range (mg/dL) | +0.0388 | 0.0208 | ±0.0415 | +1.870 | 0.0614 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **577**, R² = **0.1285**, Adj R² = **0.1116**, F-statistic = **7.58** (p = **3.07e-12**), Residual SE = **16.788** on **565** df, AIC = **4904.4**, BIC = **4956.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.3320** | 6.1323 | ±12.2645 | **+10.654** | **1.67e-26** | *** |
| Education: graduate level (vs college) | -2.4670 | 1.5425 | ±3.0850 | -1.599 | 0.1097 |  |
| Education: high school or below (vs college) | +0.0762 | 2.6548 | ±5.3096 | +0.029 | 0.9771 |  |
| Site: UCSD (vs UAB) | +2.0249 | 2.0249 | ±4.0498 | +1.000 | 0.3173 |  |
| Site: UW (vs UAB) | -2.8182 | 1.6733 | ±3.3467 | -1.684 | 0.0921 | . |
| **Age (years)** | **-0.4005** | 0.0701 | ±0.1402 | **-5.713** | **1.11e-08** | *** |
| **BMI (kg/m2)** | **+0.2958** | 0.1091 | ±0.2183 | **+2.710** | **0.0067** | ** |
| Hypertension | +0.9111 | 1.6324 | ±3.2647 | +0.558 | 0.5767 |  |
| High cholesterol | +1.7960 | 1.5128 | ±3.0257 | +1.187 | 0.2352 |  |
| Kidney disease | -1.7717 | 3.0330 | ±6.0660 | -0.584 | 0.5591 |  |
| Circulatory disease | -2.5678 | 1.9533 | ±3.9065 | -1.315 | 0.1886 |  |
| **SD of daily means (mg/dL)** | **+0.2670** | 0.0996 | ±0.1991 | **+2.682** | **0.0073** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **577**, R² = **0.1268**, Adj R² = **0.1098**, F-statistic = **7.46** (p = **5.15e-12**), Residual SE = **16.805** on **565** df, AIC = **4905.6**, BIC = **4957.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.5721** | 8.4500 | ±16.8999 | **+9.417** | **4.65e-21** | *** |
| Education: graduate level (vs college) | -2.4035 | 1.5507 | ±3.1014 | -1.550 | 0.1212 |  |
| Education: high school or below (vs college) | -0.1632 | 2.6421 | ±5.2842 | -0.062 | 0.9508 |  |
| Site: UCSD (vs UAB) | +2.0145 | 2.0302 | ±4.0603 | +0.992 | 0.3211 |  |
| Site: UW (vs UAB) | -2.7513 | 1.6832 | ±3.3664 | -1.635 | 0.1021 |  |
| **Age (years)** | **-0.4009** | 0.0700 | ±0.1400 | **-5.725** | **1.03e-08** | *** |
| **BMI (kg/m2)** | **+0.2955** | 0.1087 | ±0.2175 | **+2.718** | **0.0066** | ** |
| Hypertension | +1.0503 | 1.6358 | ±3.2716 | +0.642 | 0.5208 |  |
| High cholesterol | +1.6705 | 1.5193 | ±3.0386 | +1.100 | 0.2715 |  |
| Kidney disease | -1.9233 | 3.0320 | ±6.0640 | -0.634 | 0.5259 |  |
| Circulatory disease | -2.4777 | 1.9602 | ±3.9205 | -1.264 | 0.2062 |  |
| **Time in range 70-180, pooled (%)** | **-0.1294** | 0.0622 | ±0.1244 | **-2.080** | **0.0375** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **577**, R² = **0.1263**, Adj R² = **0.1093**, F-statistic = **7.43** (p = **5.83e-12**), Residual SE = **16.809** on **565** df, AIC = **4905.9**, BIC = **4958.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.2752** | 8.3821 | ±16.7643 | **+9.458** | **3.15e-21** | *** |
| Education: graduate level (vs college) | -2.4031 | 1.5530 | ±3.1059 | -1.547 | 0.1218 |  |
| Education: high school or below (vs college) | -0.1707 | 2.6439 | ±5.2878 | -0.065 | 0.9485 |  |
| Site: UCSD (vs UAB) | +2.0112 | 2.0307 | ±4.0614 | +0.990 | 0.3220 |  |
| Site: UW (vs UAB) | -2.7553 | 1.6842 | ±3.3684 | -1.636 | 0.1018 |  |
| **Age (years)** | **-0.4013** | 0.0701 | ±0.1402 | **-5.727** | **1.02e-08** | *** |
| **BMI (kg/m2)** | **+0.2958** | 0.1089 | ±0.2178 | **+2.717** | **0.0066** | ** |
| Hypertension | +1.0666 | 1.6366 | ±3.2731 | +0.652 | 0.5146 |  |
| High cholesterol | +1.6636 | 1.5190 | ±3.0380 | +1.095 | 0.2734 |  |
| Kidney disease | -1.9085 | 3.0361 | ±6.0722 | -0.629 | 0.5296 |  |
| Circulatory disease | -2.4785 | 1.9619 | ±3.9238 | -1.263 | 0.2065 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.1255** | 0.0610 | ±0.1219 | **-2.058** | **0.0396** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **577**, R² = **0.1183**, Adj R² = **0.1012**, F-statistic = **6.89** (p = **5.74e-11**), Residual SE = **16.886** on **565** df, AIC = **4911.1**, BIC = **4963.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.9667** | 6.1116 | ±12.2231 | **+10.957** | **6.13e-28** | *** |
| Education: graduate level (vs college) | -2.6113 | 1.5396 | ±3.0792 | -1.696 | 0.0899 | . |
| Education: high school or below (vs college) | +0.3976 | 2.6685 | ±5.3370 | +0.149 | 0.8816 |  |
| Site: UCSD (vs UAB) | +2.0160 | 2.0612 | ±4.1224 | +0.978 | 0.3280 |  |
| Site: UW (vs UAB) | -3.0659 | 1.6920 | ±3.3839 | -1.812 | 0.0700 | . |
| **Age (years)** | **-0.3934** | 0.0705 | ±0.1409 | **-5.583** | **2.36e-08** | *** |
| **BMI (kg/m2)** | **+0.2977** | 0.1098 | ±0.2196 | **+2.712** | **0.0067** | ** |
| Hypertension | +1.3504 | 1.6261 | ±3.2522 | +0.830 | 0.4063 |  |
| High cholesterol | +1.8834 | 1.5170 | ±3.0340 | +1.241 | 0.2144 |  |
| Kidney disease | -1.0014 | 3.0888 | ±6.1777 | -0.324 | 0.7458 |  |
| Circulatory disease | -2.4545 | 1.9508 | ±3.9015 | -1.258 | 0.2083 |  |
| Time < 54 (%) | +0.2018 | 0.8937 | ±1.7874 | +0.226 | 0.8214 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **577**, R² = **0.1182**, Adj R² = **0.1011**, F-statistic = **6.89** (p = **5.90e-11**), Residual SE = **16.887** on **565** df, AIC = **4911.2**, BIC = **4963.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1372** | 6.0931 | ±12.1861 | **+11.019** | **3.11e-28** | *** |
| Education: graduate level (vs college) | -2.6259 | 1.5393 | ±3.0786 | -1.706 | 0.0880 | . |
| Education: high school or below (vs college) | +0.3608 | 2.6701 | ±5.3402 | +0.135 | 0.8925 |  |
| Site: UCSD (vs UAB) | +1.9354 | 2.0594 | ±4.1189 | +0.940 | 0.3473 |  |
| Site: UW (vs UAB) | -3.1372 | 1.6942 | ±3.3883 | -1.852 | 0.0641 | . |
| **Age (years)** | **-0.3930** | 0.0707 | ±0.1414 | **-5.558** | **2.72e-08** | *** |
| **BMI (kg/m2)** | **+0.2971** | 0.1098 | ±0.2196 | **+2.705** | **0.0068** | ** |
| Hypertension | +1.3301 | 1.6270 | ±3.2539 | +0.818 | 0.4136 |  |
| High cholesterol | +1.8500 | 1.5205 | ±3.0411 | +1.217 | 0.2237 |  |
| Kidney disease | -0.9849 | 3.0931 | ±6.1862 | -0.318 | 0.7502 |  |
| Circulatory disease | -2.4498 | 1.9559 | ±3.9118 | -1.253 | 0.2104 |  |
| Avg. daily time < 54 (%) | -0.0518 | 1.0308 | ±2.0615 | -0.050 | 0.9599 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **577**, R² = **0.1183**, Adj R² = **0.1011**, F-statistic = **6.89** (p = **5.80e-11**), Residual SE = **16.886** on **565** df, AIC = **4911.1**, BIC = **4963.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.2289** | 6.1373 | ±12.2745 | **+10.954** | **6.34e-28** | *** |
| Education: graduate level (vs college) | -2.6428 | 1.5418 | ±3.0835 | -1.714 | 0.0865 | . |
| Education: high school or below (vs college) | +0.3673 | 2.6682 | ±5.3364 | +0.138 | 0.8905 |  |
| Site: UCSD (vs UAB) | +1.9156 | 2.0600 | ±4.1200 | +0.930 | 0.3524 |  |
| Site: UW (vs UAB) | -3.1595 | 1.6884 | ±3.3768 | -1.871 | 0.0613 | . |
| **Age (years)** | **-0.3926** | 0.0703 | ±0.1407 | **-5.581** | **2.39e-08** | *** |
| **BMI (kg/m2)** | **+0.2971** | 0.1098 | ±0.2195 | **+2.706** | **0.0068** | ** |
| Hypertension | +1.3173 | 1.6235 | ±3.2470 | +0.811 | 0.4171 |  |
| High cholesterol | +1.8446 | 1.5168 | ±3.0335 | +1.216 | 0.2239 |  |
| Kidney disease | -0.9764 | 3.0919 | ±6.1838 | -0.316 | 0.7522 |  |
| Circulatory disease | -2.4607 | 1.9560 | ±3.9120 | -1.258 | 0.2084 |  |
| Time 54-69, pooled (%) | -0.0625 | 0.3208 | ±0.6415 | -0.195 | 0.8456 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **577**, R² = **0.1184**, Adj R² = **0.1012**, F-statistic = **6.90** (p = **5.65e-11**), Residual SE = **16.886** on **565** df, AIC = **4911.1**, BIC = **4963.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.2402** | 6.1174 | ±12.2349 | **+10.992** | **4.20e-28** | *** |
| Education: graduate level (vs college) | -2.6567 | 1.5436 | ±3.0872 | -1.721 | 0.0852 | . |
| Education: high school or below (vs college) | +0.3687 | 2.6679 | ±5.3357 | +0.138 | 0.8901 |  |
| Site: UCSD (vs UAB) | +1.9042 | 2.0587 | ±4.1173 | +0.925 | 0.3550 |  |
| Site: UW (vs UAB) | -3.1828 | 1.6867 | ±3.3735 | -1.887 | 0.0592 | . |
| **Age (years)** | **-0.3919** | 0.0704 | ±0.1408 | **-5.567** | **2.59e-08** | *** |
| **BMI (kg/m2)** | **+0.2971** | 0.1098 | ±0.2196 | **+2.706** | **0.0068** | ** |
| Hypertension | +1.3098 | 1.6242 | ±3.2484 | +0.806 | 0.4200 |  |
| High cholesterol | +1.8398 | 1.5164 | ±3.0328 | +1.213 | 0.2250 |  |
| Kidney disease | -0.9699 | 3.0904 | ±6.1807 | -0.314 | 0.7536 |  |
| Circulatory disease | -2.4653 | 1.9565 | ±3.9131 | -1.260 | 0.2077 |  |
| Avg. daily time 54-69 (%) | -0.0935 | 0.3196 | ±0.6392 | -0.293 | 0.7699 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **577**, R² = **0.1183**, Adj R² = **0.1011**, F-statistic = **6.89** (p = **5.89e-11**), Residual SE = **16.887** on **565** df, AIC = **4911.2**, BIC = **4963.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1714** | 6.1404 | ±12.2808 | **+10.939** | **7.48e-28** | *** |
| Education: graduate level (vs college) | -2.6296 | 1.5402 | ±3.0804 | -1.707 | 0.0878 | . |
| Education: high school or below (vs college) | +0.3645 | 2.6678 | ±5.3357 | +0.137 | 0.8913 |  |
| Site: UCSD (vs UAB) | +1.9303 | 2.0638 | ±4.1276 | +0.935 | 0.3496 |  |
| Site: UW (vs UAB) | -3.1413 | 1.6920 | ±3.3840 | -1.857 | 0.0634 | . |
| **Age (years)** | **-0.3930** | 0.0704 | ±0.1407 | **-5.584** | **2.35e-08** | *** |
| **BMI (kg/m2)** | **+0.2971** | 0.1097 | ±0.2195 | **+2.707** | **0.0068** | ** |
| Hypertension | +1.3266 | 1.6241 | ±3.2482 | +0.817 | 0.4140 |  |
| High cholesterol | +1.8496 | 1.5166 | ±3.0333 | +1.220 | 0.2226 |  |
| Kidney disease | -0.9834 | 3.0931 | ±6.1862 | -0.318 | 0.7505 |  |
| Circulatory disease | -2.4539 | 1.9554 | ±3.9108 | -1.255 | 0.2095 |  |
| Time < 70 (%) | -0.0209 | 0.2550 | ±0.5101 | -0.082 | 0.9348 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **577**, R² = **0.1184**, Adj R² = **0.1012**, F-statistic = **6.90** (p = **5.71e-11**), Residual SE = **16.886** on **565** df, AIC = **4911.1**, BIC = **4963.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.2293** | 6.1129 | ±12.2258 | **+10.998** | **3.91e-28** | *** |
| Education: graduate level (vs college) | -2.6524 | 1.5426 | ±3.0852 | -1.719 | 0.0855 | . |
| Education: high school or below (vs college) | +0.3596 | 2.6673 | ±5.3346 | +0.135 | 0.8928 |  |
| Site: UCSD (vs UAB) | +1.9001 | 2.0607 | ±4.1213 | +0.922 | 0.3565 |  |
| Site: UW (vs UAB) | -3.1839 | 1.6899 | ±3.3798 | -1.884 | 0.0596 | . |
| **Age (years)** | **-0.3920** | 0.0705 | ±0.1409 | **-5.562** | **2.66e-08** | *** |
| **BMI (kg/m2)** | **+0.2970** | 0.1098 | ±0.2196 | **+2.705** | **0.0068** | ** |
| Hypertension | +1.3118 | 1.6247 | ±3.2494 | +0.807 | 0.4194 |  |
| High cholesterol | +1.8362 | 1.5165 | ±3.0330 | +1.211 | 0.2260 |  |
| Kidney disease | -0.9702 | 3.0920 | ±6.1839 | -0.314 | 0.7537 |  |
| Circulatory disease | -2.4596 | 1.9573 | ±3.9146 | -1.257 | 0.2089 |  |
| Avg. daily time < 70 (%) | -0.0670 | 0.2674 | ±0.5347 | -0.251 | 0.8021 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **577**, R² = **0.1192**, Adj R² = **0.1021**, F-statistic = **6.95** (p = **4.49e-11**), Residual SE = **16.878** on **565** df, AIC = **4910.5**, BIC = **4962.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+76.2986** | 17.2109 | ±34.4218 | **+4.433** | **9.29e-06** | *** |
| Education: graduate level (vs college) | -2.5597 | 1.5456 | ±3.0912 | -1.656 | 0.0977 | . |
| Education: high school or below (vs college) | +0.1965 | 2.6813 | ±5.3626 | +0.073 | 0.9416 |  |
| Site: UCSD (vs UAB) | +1.9861 | 2.0453 | ±4.0906 | +0.971 | 0.3315 |  |
| Site: UW (vs UAB) | -2.9989 | 1.6908 | ±3.3815 | -1.774 | 0.0761 | . |
| **Age (years)** | **-0.3928** | 0.0703 | ±0.1406 | **-5.589** | **2.28e-08** | *** |
| **BMI (kg/m2)** | **+0.2981** | 0.1095 | ±0.2191 | **+2.722** | **0.0065** | ** |
| Hypertension | +1.2628 | 1.6298 | ±3.2596 | +0.775 | 0.4384 |  |
| High cholesterol | +1.8853 | 1.5220 | ±3.0439 | +1.239 | 0.2154 |  |
| Kidney disease | -1.1494 | 3.0905 | ±6.1809 | -0.372 | 0.7100 |  |
| Circulatory disease | -2.4875 | 1.9649 | ±3.9299 | -1.266 | 0.2055 |  |
| Time 54-250, pooled (%) | -0.0942 | 0.1636 | ±0.3271 | -0.576 | 0.5648 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **577**, R² = **0.1197**, Adj R² = **0.1026**, F-statistic = **6.99** (p = **3.86e-11**), Residual SE = **16.873** on **565** df, AIC = **4910.2**, BIC = **4962.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+79.8329** | 19.7415 | ±39.4830 | **+4.044** | **5.26e-05** | *** |
| Education: graduate level (vs college) | -2.5349 | 1.5473 | ±3.0945 | -1.638 | 0.1014 |  |
| Education: high school or below (vs college) | +0.1224 | 2.6912 | ±5.3824 | +0.045 | 0.9637 |  |
| Site: UCSD (vs UAB) | +1.9782 | 2.0451 | ±4.0901 | +0.967 | 0.3334 |  |
| Site: UW (vs UAB) | -2.9742 | 1.6898 | ±3.3797 | -1.760 | 0.0784 | . |
| **Age (years)** | **-0.3936** | 0.0703 | ±0.1405 | **-5.601** | **2.13e-08** | *** |
| **BMI (kg/m2)** | **+0.2989** | 0.1095 | ±0.2190 | **+2.730** | **0.0063** | ** |
| Hypertension | +1.2435 | 1.6300 | ±3.2600 | +0.763 | 0.4455 |  |
| High cholesterol | +1.8871 | 1.5224 | ±3.0448 | +1.240 | 0.2151 |  |
| Kidney disease | -1.2228 | 3.0951 | ±6.1902 | -0.395 | 0.6928 |  |
| Circulatory disease | -2.5068 | 1.9683 | ±3.9366 | -1.274 | 0.2028 |  |
| Avg. daily time 54-250 (%) | -0.1295 | 0.1898 | ±0.3796 | -0.682 | 0.4949 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **577**, R² = **0.1317**, Adj R² = **0.1148**, F-statistic = **7.79** (p = **1.23e-12**), Residual SE = **16.758** on **565** df, AIC = **4902.3**, BIC = **4954.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.2409** | 6.0543 | ±12.1087 | **+11.106** | **1.17e-28** | *** |
| Education: graduate level (vs college) | -2.4586 | 1.5454 | ±3.0908 | -1.591 | 0.1116 |  |
| Education: high school or below (vs college) | -0.1757 | 2.6325 | ±5.2650 | -0.067 | 0.9468 |  |
| Site: UCSD (vs UAB) | +1.8504 | 2.0269 | ±4.0539 | +0.913 | 0.3613 |  |
| Site: UW (vs UAB) | -2.8922 | 1.6726 | ±3.3452 | -1.729 | 0.0838 | . |
| **Age (years)** | **-0.4061** | 0.0701 | ±0.1402 | **-5.792** | **6.96e-09** | *** |
| **BMI (kg/m2)** | **+0.2913** | 0.1086 | ±0.2172 | **+2.683** | **0.0073** | ** |
| Hypertension | +0.9300 | 1.6440 | ±3.2880 | +0.566 | 0.5716 |  |
| High cholesterol | +1.3983 | 1.5040 | ±3.0079 | +0.930 | 0.3525 |  |
| Kidney disease | -2.2503 | 2.9909 | ±5.9819 | -0.752 | 0.4518 |  |
| Circulatory disease | -2.4448 | 1.9567 | ±3.9133 | -1.249 | 0.2115 |  |
| **Time 181-250, pooled (%)** | **+0.2372** | 0.0885 | ±0.1769 | **+2.682** | **0.0073** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **577**, R² = **0.1300**, Adj R² = **0.1131**, F-statistic = **7.68** (p = **1.99e-12**), Residual SE = **16.774** on **565** df, AIC = **4903.4**, BIC = **4955.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.1285** | 6.0604 | ±12.1208 | **+11.077** | **1.63e-28** | *** |
| Education: graduate level (vs college) | -2.4714 | 1.5479 | ±3.0958 | -1.597 | 0.1103 |  |
| Education: high school or below (vs college) | -0.1471 | 2.6344 | ±5.2687 | -0.056 | 0.9555 |  |
| Site: UCSD (vs UAB) | +1.9050 | 2.0286 | ±4.0572 | +0.939 | 0.3477 |  |
| Site: UW (vs UAB) | -2.8761 | 1.6756 | ±3.3513 | -1.716 | 0.0861 | . |
| **Age (years)** | **-0.4036** | 0.0701 | ±0.1402 | **-5.757** | **8.57e-09** | *** |
| **BMI (kg/m2)** | **+0.2916** | 0.1087 | ±0.2175 | **+2.682** | **0.0073** | ** |
| Hypertension | +0.9692 | 1.6445 | ±3.2891 | +0.589 | 0.5556 |  |
| High cholesterol | +1.4354 | 1.5054 | ±3.0108 | +0.954 | 0.3403 |  |
| Kidney disease | -2.1369 | 3.0012 | ±6.0024 | -0.712 | 0.4765 |  |
| Circulatory disease | -2.4382 | 1.9601 | ±3.9203 | -1.244 | 0.2135 |  |
| **Avg. daily time 181-250 (%)** | **+0.2157** | 0.0862 | ±0.1725 | **+2.502** | **0.0124** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **577**, R² = **0.1269**, Adj R² = **0.1099**, F-statistic = **7.46** (p = **4.98e-12**), Residual SE = **16.804** on **565** df, AIC = **4905.5**, BIC = **4957.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.9571** | 6.0581 | ±12.1163 | **+11.052** | **2.13e-28** | *** |
| Education: graduate level (vs college) | -2.4532 | 1.5475 | ±3.0950 | -1.585 | 0.1129 |  |
| Education: high school or below (vs college) | -0.1864 | 2.6413 | ±5.2827 | -0.071 | 0.9438 |  |
| Site: UCSD (vs UAB) | +1.9032 | 2.0336 | ±4.0673 | +0.936 | 0.3493 |  |
| Site: UW (vs UAB) | -2.8615 | 1.6783 | ±3.3565 | -1.705 | 0.0882 | . |
| **Age (years)** | **-0.3997** | 0.0700 | ±0.1400 | **-5.711** | **1.12e-08** | *** |
| **BMI (kg/m2)** | **+0.2949** | 0.1089 | ±0.2178 | **+2.709** | **0.0068** | ** |
| Hypertension | +1.0033 | 1.6391 | ±3.2782 | +0.612 | 0.5405 |  |
| High cholesterol | +1.6276 | 1.5185 | ±3.0370 | +1.072 | 0.2838 |  |
| Kidney disease | -1.8949 | 3.0266 | ±6.0531 | -0.626 | 0.5313 |  |
| Circulatory disease | -2.4958 | 1.9661 | ±3.9321 | -1.269 | 0.2043 |  |
| **Time > 180 (%)** | **+0.1302** | 0.0622 | ±0.1244 | **+2.093** | **0.0363** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **577**, R² = **0.1269**, Adj R² = **0.1099**, F-statistic = **7.46** (p = **4.97e-12**), Residual SE = **16.804** on **565** df, AIC = **4905.5**, BIC = **4957.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.9282** | 6.0649 | ±12.1298 | **+11.035** | **2.58e-28** | *** |
| Education: graduate level (vs college) | -2.4548 | 1.5490 | ±3.0981 | -1.585 | 0.1130 |  |
| Education: high school or below (vs college) | -0.2079 | 2.6416 | ±5.2831 | -0.079 | 0.9373 |  |
| Site: UCSD (vs UAB) | +1.9200 | 2.0331 | ±4.0663 | +0.944 | 0.3450 |  |
| Site: UW (vs UAB) | -2.8588 | 1.6794 | ±3.3587 | -1.702 | 0.0887 | . |
| **Age (years)** | **-0.3993** | 0.0700 | ±0.1400 | **-5.704** | **1.17e-08** | *** |
| **BMI (kg/m2)** | **+0.2954** | 0.1090 | ±0.2179 | **+2.711** | **0.0067** | ** |
| Hypertension | +1.0130 | 1.6401 | ±3.2801 | +0.618 | 0.5368 |  |
| High cholesterol | +1.6168 | 1.5171 | ±3.0341 | +1.066 | 0.2865 |  |
| Kidney disease | -1.9087 | 3.0267 | ±6.0535 | -0.631 | 0.5283 |  |
| Circulatory disease | -2.4962 | 1.9677 | ±3.9354 | -1.269 | 0.2046 |  |
| **Avg. daily time > 180 (%)** | **+0.1304** | 0.0613 | ±0.1225 | **+2.129** | **0.0332** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **577**, R² = **0.1216**, Adj R² = **0.1045**, F-statistic = **7.11** (p = **2.28e-11**), Residual SE = **16.855** on **565** df, AIC = **4909.0**, BIC = **4961.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+67.0539** | 6.0840 | ±12.1679 | **+11.021** | **3.01e-28** | *** |
| Education: graduate level (vs college) | -2.5095 | 1.5507 | ±3.1013 | -1.618 | 0.1056 |  |
| Education: high school or below (vs college) | +0.1411 | 2.6404 | ±5.2807 | +0.053 | 0.9574 |  |
| Site: UCSD (vs UAB) | +1.9544 | 2.0429 | ±4.0859 | +0.957 | 0.3387 |  |
| Site: UW (vs UAB) | -2.9919 | 1.6833 | ±3.3666 | -1.777 | 0.0755 | . |
| **Age (years)** | **-0.3936** | 0.0703 | ±0.1405 | **-5.602** | **2.11e-08** | *** |
| **BMI (kg/m2)** | **+0.2919** | 0.1092 | ±0.2184 | **+2.673** | **0.0075** | ** |
| Hypertension | +1.1056 | 1.6414 | ±3.2827 | +0.674 | 0.5006 |  |
| High cholesterol | +1.7325 | 1.5193 | ±3.0385 | +1.140 | 0.2541 |  |
| Kidney disease | -1.2561 | 3.0451 | ±6.0902 | -0.413 | 0.6800 |  |
| Circulatory disease | -2.5142 | 1.9624 | ±3.9249 | -1.281 | 0.2001 |  |
| Nocturnal time > 180 (%) | +0.0833 | 0.0602 | ±0.1203 | +1.385 | 0.1662 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **577**, R² = **0.1248**, Adj R² = **0.1078**, F-statistic = **7.33** (p = **8.95e-12**), Residual SE = **16.824** on **565** df, AIC = **4906.8**, BIC = **4959.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.9319** | 6.0420 | ±12.0840 | **+11.078** | **1.61e-28** | *** |
| Education: graduate level (vs college) | -2.4276 | 1.5383 | ±3.0767 | -1.578 | 0.1146 |  |
| Education: high school or below (vs college) | +0.0189 | 2.6843 | ±5.3685 | +0.007 | 0.9944 |  |
| Site: UCSD (vs UAB) | +1.7439 | 2.0350 | ±4.0700 | +0.857 | 0.3915 |  |
| Site: UW (vs UAB) | -3.0237 | 1.6743 | ±3.3486 | -1.806 | 0.0709 | . |
| **Age (years)** | **-0.4072** | 0.0708 | ±0.1415 | **-5.754** | **8.73e-09** | *** |
| **BMI (kg/m2)** | **+0.3074** | 0.1088 | ±0.2176 | **+2.825** | **0.0047** | ** |
| Hypertension | +1.0146 | 1.6249 | ±3.2499 | +0.624 | 0.5324 |  |
| High cholesterol | +1.6631 | 1.5195 | ±3.0389 | +1.095 | 0.2737 |  |
| Kidney disease | -1.7649 | 3.0829 | ±6.1659 | -0.572 | 0.5670 |  |
| Circulatory disease | -2.3641 | 1.9580 | ±3.9159 | -1.207 | 0.2273 |  |
| **Any reading > 250 during wear (0/1)** | **+3.3430** | 1.6438 | ±3.2877 | **+2.034** | **0.0420** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **577**, R² = **0.1191**, Adj R² = **0.1020**, F-statistic = **6.95** (p = **4.58e-11**), Residual SE = **16.879** on **565** df, AIC = **4910.6**, BIC = **4962.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.9571** | 6.0821 | ±12.1641 | **+11.009** | **3.46e-28** | *** |
| Education: graduate level (vs college) | -2.5657 | 1.5457 | ±3.0915 | -1.660 | 0.0969 | . |
| Education: high school or below (vs college) | +0.1866 | 2.6865 | ±5.3729 | +0.069 | 0.9446 |  |
| Site: UCSD (vs UAB) | +1.9543 | 2.0480 | ±4.0960 | +0.954 | 0.3400 |  |
| Site: UW (vs UAB) | -3.0278 | 1.6875 | ±3.3749 | -1.794 | 0.0728 | . |
| **Age (years)** | **-0.3927** | 0.0703 | ±0.1405 | **-5.589** | **2.28e-08** | *** |
| **BMI (kg/m2)** | **+0.2979** | 0.1095 | ±0.2191 | **+2.719** | **0.0065** | ** |
| Hypertension | +1.2568 | 1.6308 | ±3.2616 | +0.771 | 0.4409 |  |
| High cholesterol | +1.8723 | 1.5229 | ±3.0457 | +1.229 | 0.2189 |  |
| Kidney disease | -1.1401 | 3.0897 | ±6.1794 | -0.369 | 0.7121 |  |
| Circulatory disease | -2.4852 | 1.9666 | ±3.9332 | -1.264 | 0.2063 |  |
| Time > 250 (%) | +0.0921 | 0.1667 | ±0.3334 | +0.552 | 0.5806 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 577)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **577**, R² = **0.1198**, Adj R² = **0.1027**, F-statistic = **6.99** (p = **3.77e-11**), Residual SE = **16.872** on **565** df, AIC = **4910.1**, BIC = **4962.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+66.9147** | 6.0834 | ±12.1668 | **+11.000** | **3.84e-28** | *** |
| Education: graduate level (vs college) | -2.5425 | 1.5466 | ±3.0931 | -1.644 | 0.1002 |  |
| Education: high school or below (vs college) | +0.0930 | 2.7010 | ±5.4021 | +0.034 | 0.9725 |  |
| Site: UCSD (vs UAB) | +1.9461 | 2.0486 | ±4.0971 | +0.950 | 0.3421 |  |
| Site: UW (vs UAB) | -3.0037 | 1.6865 | ±3.3730 | -1.781 | 0.0749 | . |
| **Age (years)** | **-0.3930** | 0.0702 | ±0.1405 | **-5.595** | **2.20e-08** | *** |
| **BMI (kg/m2)** | **+0.2988** | 0.1095 | ±0.2190 | **+2.729** | **0.0064** | ** |
| Hypertension | +1.2296 | 1.6307 | ±3.2614 | +0.754 | 0.4508 |  |
| High cholesterol | +1.8719 | 1.5237 | ±3.0475 | +1.228 | 0.2193 |  |
| Kidney disease | -1.2234 | 3.0940 | ±6.1881 | -0.395 | 0.6925 |  |
| Circulatory disease | -2.5060 | 1.9711 | ±3.9423 | -1.271 | 0.2036 |  |
| Avg. daily time > 250 (%) | +0.1356 | 0.1991 | ±0.3981 | +0.681 | 0.4959 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
