# Phase 6b model output tables - Hypoglycaemia exposure: at least one reading < 54 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Cognition

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 408; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **408**, R² = **0.1199**, Adj R² = **0.0977**, F-statistic = **5.41** (p = **1.61e-07**), Residual SE = **2.498** on **397** df, AIC = **1915.7**, BIC = **1959.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5716** | 0.8988 | ±1.7977 | **+32.899** | **2.24e-237** | *** |
| **Education: graduate level (vs college)** | **+0.8077** | 0.2707 | ±0.5414 | **+2.984** | **0.0028** | ** |
| Education: high school or below (vs college) | -0.8186 | 0.6141 | ±1.2282 | -1.333 | 0.1825 |  |
| Site: UCSD (vs UAB) | -0.3523 | 0.3634 | ±0.7267 | -0.969 | 0.3323 |  |
| **Site: UW (vs UAB)** | **-0.5803** | 0.2769 | ±0.5539 | **-2.095** | **0.0361** | * |
| **Age (years)** | **-0.0505** | 0.0117 | ±0.0234 | **-4.319** | **1.57e-05** | *** |
| BMI (kg/m2) | -0.0091 | 0.0164 | ±0.0329 | -0.554 | 0.5795 |  |
| Hypertension | +0.1156 | 0.2788 | ±0.5576 | +0.415 | 0.6785 |  |
| **High cholesterol** | **+0.5787** | 0.2751 | ±0.5503 | **+2.103** | **0.0354** | * |
| Kidney disease | -0.6845 | 0.6528 | ±1.3056 | -1.049 | 0.2944 |  |
| **Circulatory disease** | **-0.9569** | 0.4030 | ±0.8060 | **-2.374** | **0.0176** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **408**, R² = **0.1235**, Adj R² = **0.0992**, F-statistic = **5.07** (p = **1.95e-07**), Residual SE = **2.496** on **396** df, AIC = **1915.9**, BIC = **1964.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.5079** | 1.6334 | ±3.2669 | **+19.289** | **6.59e-83** | *** |
| **Education: graduate level (vs college)** | **+0.7909** | 0.2708 | ±0.5415 | **+2.921** | **0.0035** | ** |
| Education: high school or below (vs college) | -0.7766 | 0.6166 | ±1.2331 | -1.260 | 0.2078 |  |
| Site: UCSD (vs UAB) | -0.2930 | 0.3643 | ±0.7286 | -0.804 | 0.4212 |  |
| **Site: UW (vs UAB)** | **-0.5660** | 0.2770 | ±0.5540 | **-2.043** | **0.0410** | * |
| **Age (years)** | **-0.0479** | 0.0116 | ±0.0233 | **-4.116** | **3.86e-05** | *** |
| BMI (kg/m2) | -0.0057 | 0.0163 | ±0.0326 | -0.350 | 0.7265 |  |
| Hypertension | +0.1084 | 0.2780 | ±0.5560 | +0.390 | 0.6965 |  |
| **High cholesterol** | **+0.6318** | 0.2803 | ±0.5606 | **+2.254** | **0.0242** | * |
| Kidney disease | -0.6657 | 0.6523 | ±1.3047 | -1.021 | 0.3075 |  |
| **Circulatory disease** | **-0.9809** | 0.4029 | ±0.8058 | **-2.435** | **0.0149** | * |
| HbA1c (%) | -0.3949 | 0.2663 | ±0.5326 | -1.483 | 0.1382 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **408**, R² = **0.1217**, Adj R² = **0.0973**, F-statistic = **4.99** (p = **2.77e-07**), Residual SE = **2.498** on **396** df, AIC = **1916.8**, BIC = **1964.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.4121** | 1.2444 | ±2.4887 | **+24.440** | **6.44e-132** | *** |
| **Education: graduate level (vs college)** | **+0.8212** | 0.2718 | ±0.5437 | **+3.021** | **0.0025** | ** |
| Education: high school or below (vs college) | -0.7845 | 0.6182 | ±1.2364 | -1.269 | 0.2044 |  |
| Site: UCSD (vs UAB) | -0.3439 | 0.3639 | ±0.7279 | -0.945 | 0.3447 |  |
| **Site: UW (vs UAB)** | **-0.5516** | 0.2766 | ±0.5532 | **-1.994** | **0.0461** | * |
| **Age (years)** | **-0.0498** | 0.0117 | ±0.0234 | **-4.249** | **2.15e-05** | *** |
| BMI (kg/m2) | -0.0082 | 0.0166 | ±0.0332 | -0.495 | 0.6208 |  |
| Hypertension | +0.1379 | 0.2794 | ±0.5588 | +0.494 | 0.6215 |  |
| **High cholesterol** | **+0.6031** | 0.2793 | ±0.5586 | **+2.159** | **0.0308** | * |
| Kidney disease | -0.6338 | 0.6514 | ±1.3027 | -0.973 | 0.3305 |  |
| **Circulatory disease** | **-0.9630** | 0.4045 | ±0.8091 | **-2.381** | **0.0173** | * |
| Mean glucose (mg/dL) | -0.0083 | 0.0088 | ±0.0176 | -0.944 | 0.3450 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **408**, R² = **0.1217**, Adj R² = **0.0973**, F-statistic = **4.99** (p = **2.77e-07**), Residual SE = **2.498** on **396** df, AIC = **1916.8**, BIC = **1964.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.5619** | 2.2656 | ±4.5313 | **+13.931** | **4.13e-44** | *** |
| **Education: graduate level (vs college)** | **+0.8212** | 0.2718 | ±0.5437 | **+3.021** | **0.0025** | ** |
| Education: high school or below (vs college) | -0.7845 | 0.6182 | ±1.2364 | -1.269 | 0.2044 |  |
| Site: UCSD (vs UAB) | -0.3439 | 0.3639 | ±0.7279 | -0.945 | 0.3447 |  |
| **Site: UW (vs UAB)** | **-0.5516** | 0.2766 | ±0.5532 | **-1.994** | **0.0461** | * |
| **Age (years)** | **-0.0498** | 0.0117 | ±0.0234 | **-4.249** | **2.15e-05** | *** |
| BMI (kg/m2) | -0.0082 | 0.0166 | ±0.0332 | -0.495 | 0.6208 |  |
| Hypertension | +0.1379 | 0.2794 | ±0.5588 | +0.494 | 0.6215 |  |
| **High cholesterol** | **+0.6031** | 0.2793 | ±0.5586 | **+2.159** | **0.0308** | * |
| Kidney disease | -0.6338 | 0.6514 | ±1.3027 | -0.973 | 0.3305 |  |
| **Circulatory disease** | **-0.9630** | 0.4045 | ±0.8091 | **-2.381** | **0.0173** | * |
| GMI (%) | -0.3474 | 0.3679 | ±0.7358 | -0.944 | 0.3450 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **408**, R² = **0.1212**, Adj R² = **0.0968**, F-statistic = **4.96** (p = **3.05e-07**), Residual SE = **2.499** on **396** df, AIC = **1917.0**, BIC = **1965.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.2210** | 1.2180 | ±2.4360 | **+24.812** | **6.71e-136** | *** |
| **Education: graduate level (vs college)** | **+0.8145** | 0.2716 | ±0.5433 | **+2.998** | **0.0027** | ** |
| Education: high school or below (vs college) | -0.7838 | 0.6179 | ±1.2358 | -1.269 | 0.2046 |  |
| Site: UCSD (vs UAB) | -0.3404 | 0.3640 | ±0.7279 | -0.935 | 0.3496 |  |
| **Site: UW (vs UAB)** | **-0.5617** | 0.2753 | ±0.5507 | **-2.040** | **0.0413** | * |
| **Age (years)** | **-0.0506** | 0.0118 | ±0.0235 | **-4.301** | **1.70e-05** | *** |
| BMI (kg/m2) | -0.0070 | 0.0169 | ±0.0339 | -0.413 | 0.6799 |  |
| Hypertension | +0.1329 | 0.2806 | ±0.5611 | +0.474 | 0.6358 |  |
| **High cholesterol** | **+0.6038** | 0.2812 | ±0.5624 | **+2.147** | **0.0318** | * |
| Kidney disease | -0.6748 | 0.6506 | ±1.3011 | -1.037 | 0.2997 |  |
| **Circulatory disease** | **-0.9698** | 0.4031 | ±0.8063 | **-2.406** | **0.0161** | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0065 | 0.0081 | ±0.0162 | -0.800 | 0.4235 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **408**, R² = **0.1217**, Adj R² = **0.0973**, F-statistic = **4.99** (p = **2.77e-07**), Residual SE = **2.498** on **396** df, AIC = **1916.8**, BIC = **1964.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.8409** | 0.9777 | ±1.9553 | **+30.522** | **1.32e-204** | *** |
| **Education: graduate level (vs college)** | **+0.8172** | 0.2714 | ±0.5429 | **+3.011** | **0.0026** | ** |
| Education: high school or below (vs college) | -0.8156 | 0.6113 | ±1.2225 | -1.334 | 0.1821 |  |
| Site: UCSD (vs UAB) | -0.3344 | 0.3605 | ±0.7210 | -0.928 | 0.3536 |  |
| **Site: UW (vs UAB)** | **-0.5712** | 0.2777 | ±0.5554 | **-2.057** | **0.0397** | * |
| **Age (years)** | **-0.0489** | 0.0116 | ±0.0233 | **-4.199** | **2.69e-05** | *** |
| BMI (kg/m2) | -0.0086 | 0.0166 | ±0.0332 | -0.517 | 0.6050 |  |
| Hypertension | +0.1304 | 0.2800 | ±0.5600 | +0.466 | 0.6415 |  |
| **High cholesterol** | **+0.5695** | 0.2752 | ±0.5505 | **+2.069** | **0.0385** | * |
| Kidney disease | -0.6108 | 0.6539 | ±1.3078 | -0.934 | 0.3503 |  |
| **Circulatory disease** | **-0.9616** | 0.4033 | ±0.8066 | **-2.384** | **0.0171** | * |
| Glucose SD, pooled (mg/dL) | -0.0181 | 0.0222 | ±0.0445 | -0.813 | 0.4164 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **408**, R² = **0.1218**, Adj R² = **0.0975**, F-statistic = **5.00** (p = **2.69e-07**), Residual SE = **2.498** on **396** df, AIC = **1916.7**, BIC = **1964.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.8248** | 0.9497 | ±1.8994 | **+31.404** | **1.78e-216** | *** |
| **Education: graduate level (vs college)** | **+0.8142** | 0.2715 | ±0.5429 | **+2.999** | **0.0027** | ** |
| Education: high school or below (vs college) | -0.8082 | 0.6108 | ±1.2216 | -1.323 | 0.1858 |  |
| Site: UCSD (vs UAB) | -0.3295 | 0.3575 | ±0.7151 | -0.921 | 0.3568 |  |
| **Site: UW (vs UAB)** | **-0.5674** | 0.2782 | ±0.5564 | **-2.039** | **0.0414** | * |
| **Age (years)** | **-0.0486** | 0.0117 | ±0.0234 | **-4.146** | **3.38e-05** | *** |
| BMI (kg/m2) | -0.0084 | 0.0166 | ±0.0331 | -0.509 | 0.6106 |  |
| Hypertension | +0.1290 | 0.2810 | ±0.5620 | +0.459 | 0.6462 |  |
| **High cholesterol** | **+0.5726** | 0.2756 | ±0.5511 | **+2.078** | **0.0377** | * |
| Kidney disease | -0.6021 | 0.6539 | ±1.3077 | -0.921 | 0.3571 |  |
| **Circulatory disease** | **-0.9638** | 0.4031 | ±0.8063 | **-2.391** | **0.0168** | * |
| Avg. daily SD (mg/dL) | -0.0206 | 0.0241 | ±0.0483 | -0.854 | 0.3933 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **408**, R² = **0.1214**, Adj R² = **0.0970**, F-statistic = **4.97** (p = **2.95e-07**), Residual SE = **2.499** on **396** df, AIC = **1917.0**, BIC = **1965.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.9224** | 1.0410 | ±2.0819 | **+28.745** | **1.05e-181** | *** |
| **Education: graduate level (vs college)** | **+0.8114** | 0.2710 | ±0.5420 | **+2.994** | **0.0028** | ** |
| Education: high school or below (vs college) | -0.8303 | 0.6112 | ±1.2223 | -1.359 | 0.1743 |  |
| Site: UCSD (vs UAB) | -0.3380 | 0.3607 | ±0.7214 | -0.937 | 0.3488 |  |
| **Site: UW (vs UAB)** | **-0.5856** | 0.2774 | ±0.5548 | **-2.111** | **0.0348** | * |
| **Age (years)** | **-0.0491** | 0.0116 | ±0.0233 | **-4.217** | **2.47e-05** | *** |
| BMI (kg/m2) | -0.0089 | 0.0166 | ±0.0332 | -0.539 | 0.5899 |  |
| Hypertension | +0.1207 | 0.2792 | ±0.5584 | +0.432 | 0.6655 |  |
| **High cholesterol** | **+0.5575** | 0.2748 | ±0.5495 | **+2.029** | **0.0424** | * |
| Kidney disease | -0.6315 | 0.6538 | ±1.3076 | -0.966 | 0.3341 |  |
| **Circulatory disease** | **-0.9595** | 0.4029 | ±0.8057 | **-2.382** | **0.0172** | * |
| CV (%) | -0.0228 | 0.0299 | ±0.0599 | -0.762 | 0.4460 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **408**, R² = **0.1243**, Adj R² = **0.1000**, F-statistic = **5.11** (p = **1.69e-07**), Residual SE = **2.495** on **396** df, AIC = **1915.6**, BIC = **1963.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.5088** | 1.1599 | ±2.3198 | **+24.579** | **2.14e-133** | *** |
| **Education: graduate level (vs college)** | **+0.8285** | 0.2706 | ±0.5412 | **+3.062** | **0.0022** | ** |
| Education: high school or below (vs college) | -0.8220 | 0.6063 | ±1.2127 | -1.356 | 0.1752 |  |
| Site: UCSD (vs UAB) | -0.3246 | 0.3590 | ±0.7179 | -0.904 | 0.3658 |  |
| **Site: UW (vs UAB)** | **-0.5742** | 0.2776 | ±0.5552 | **-2.068** | **0.0386** | * |
| **Age (years)** | **-0.0479** | 0.0116 | ±0.0232 | **-4.129** | **3.65e-05** | *** |
| BMI (kg/m2) | -0.0084 | 0.0166 | ±0.0331 | -0.510 | 0.6104 |  |
| Hypertension | +0.1241 | 0.2784 | ±0.5568 | +0.446 | 0.6558 |  |
| **High cholesterol** | **+0.5548** | 0.2747 | ±0.5494 | **+2.020** | **0.0434** | * |
| Kidney disease | -0.6049 | 0.6506 | ±1.3012 | -0.930 | 0.3525 |  |
| **Circulatory disease** | **-0.9560** | 0.4020 | ±0.8040 | **-2.378** | **0.0174** | * |
| Mean / SD ratio | +0.1601 | 0.1167 | ±0.2333 | +1.372 | 0.1700 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **408**, R² = **0.1223**, Adj R² = **0.0979**, F-statistic = **5.02** (p = **2.47e-07**), Residual SE = **2.497** on **396** df, AIC = **1916.5**, BIC = **1964.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.7900** | 1.1987 | ±2.3974 | **+24.018** | **1.80e-127** | *** |
| **Education: graduate level (vs college)** | **+0.8230** | 0.2716 | ±0.5432 | **+3.030** | **0.0024** | ** |
| Education: high school or below (vs college) | -0.8024 | 0.6088 | ±1.2176 | -1.318 | 0.1875 |  |
| Site: UCSD (vs UAB) | -0.3222 | 0.3570 | ±0.7141 | -0.902 | 0.3669 |  |
| **Site: UW (vs UAB)** | **-0.5720** | 0.2784 | ±0.5569 | **-2.054** | **0.0399** | * |
| **Age (years)** | **-0.0484** | 0.0118 | ±0.0236 | **-4.100** | **4.13e-05** | *** |
| BMI (kg/m2) | -0.0081 | 0.0165 | ±0.0331 | -0.493 | 0.6222 |  |
| Hypertension | +0.1168 | 0.2795 | ±0.5590 | +0.418 | 0.6760 |  |
| **High cholesterol** | **+0.5671** | 0.2755 | ±0.5510 | **+2.058** | **0.0396** | * |
| Kidney disease | -0.6128 | 0.6508 | ±1.3016 | -0.942 | 0.3464 |  |
| **Circulatory disease** | **-0.9603** | 0.4032 | ±0.8065 | **-2.382** | **0.0172** | * |
| Avg. daily mean/SD | +0.0954 | 0.0953 | ±0.1906 | +1.001 | 0.3168 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **408**, R² = **0.1207**, Adj R² = **0.0963**, F-statistic = **4.94** (p = **3.34e-07**), Residual SE = **2.500** on **396** df, AIC = **1917.3**, BIC = **1965.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.9752** | 1.1641 | ±2.3281 | **+25.751** | **3.18e-146** | *** |
| **Education: graduate level (vs college)** | **+0.8085** | 0.2709 | ±0.5419 | **+2.984** | **0.0028** | ** |
| Education: high school or below (vs college) | -0.8253 | 0.6158 | ±1.2315 | -1.340 | 0.1802 |  |
| Site: UCSD (vs UAB) | -0.3439 | 0.3634 | ±0.7269 | -0.946 | 0.3440 |  |
| **Site: UW (vs UAB)** | **-0.5995** | 0.2772 | ±0.5543 | **-2.163** | **0.0305** | * |
| **Age (years)** | **-0.0507** | 0.0117 | ±0.0235 | **-4.320** | **1.56e-05** | *** |
| BMI (kg/m2) | -0.0090 | 0.0166 | ±0.0331 | -0.543 | 0.5873 |  |
| Hypertension | +0.1221 | 0.2806 | ±0.5611 | +0.435 | 0.6634 |  |
| **High cholesterol** | **+0.5606** | 0.2769 | ±0.5538 | **+2.024** | **0.0429** | * |
| Kidney disease | -0.6806 | 0.6539 | ±1.3079 | -1.041 | 0.2980 |  |
| **Circulatory disease** | **-0.9586** | 0.4055 | ±0.8110 | **-2.364** | **0.0181** | * |
| MAG (mg/dL/h) | -0.0096 | 0.0167 | ±0.0334 | -0.577 | 0.5636 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **408**, R² = **0.1221**, Adj R² = **0.0977**, F-statistic = **5.01** (p = **2.56e-07**), Residual SE = **2.498** on **396** df, AIC = **1916.6**, BIC = **1964.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.9667** | 1.0150 | ±2.0300 | **+29.524** | **1.43e-191** | *** |
| **Education: graduate level (vs college)** | **+0.8096** | 0.2709 | ±0.5419 | **+2.988** | **0.0028** | ** |
| Education: high school or below (vs college) | -0.8105 | 0.6109 | ±1.2219 | -1.327 | 0.1846 |  |
| Site: UCSD (vs UAB) | -0.3316 | 0.3594 | ±0.7188 | -0.923 | 0.3562 |  |
| **Site: UW (vs UAB)** | **-0.5752** | 0.2776 | ±0.5551 | **-2.072** | **0.0382** | * |
| **Age (years)** | **-0.0488** | 0.0116 | ±0.0233 | **-4.191** | **2.78e-05** | *** |
| BMI (kg/m2) | -0.0098 | 0.0165 | ±0.0331 | -0.595 | 0.5518 |  |
| Hypertension | +0.1253 | 0.2799 | ±0.5599 | +0.448 | 0.6544 |  |
| **High cholesterol** | **+0.5640** | 0.2756 | ±0.5512 | **+2.046** | **0.0407** | * |
| Kidney disease | -0.6183 | 0.6508 | ±1.3015 | -0.950 | 0.3420 |  |
| **Circulatory disease** | **-0.9618** | 0.4040 | ±0.8080 | **-2.381** | **0.0173** | * |
| Avg. daily range (mg/dL) | -0.0048 | 0.0053 | ±0.0107 | -0.899 | 0.3685 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **408**, R² = **0.1211**, Adj R² = **0.0967**, F-statistic = **4.96** (p = **3.12e-07**), Residual SE = **2.499** on **396** df, AIC = **1917.1**, BIC = **1965.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.4464** | 0.9303 | ±1.8607 | **+31.651** | **7.30e-220** | *** |
| **Education: graduate level (vs college)** | **+0.7939** | 0.2708 | ±0.5416 | **+2.932** | **0.0034** | ** |
| Education: high school or below (vs college) | -0.7994 | 0.6188 | ±1.2376 | -1.292 | 0.1964 |  |
| Site: UCSD (vs UAB) | -0.3485 | 0.3636 | ±0.7272 | -0.958 | 0.3378 |  |
| **Site: UW (vs UAB)** | **-0.5816** | 0.2775 | ±0.5551 | **-2.095** | **0.0361** | * |
| **Age (years)** | **-0.0508** | 0.0117 | ±0.0234 | **-4.342** | **1.41e-05** | *** |
| BMI (kg/m2) | -0.0102 | 0.0165 | ±0.0330 | -0.619 | 0.5362 |  |
| Hypertension | +0.1142 | 0.2797 | ±0.5594 | +0.408 | 0.6829 |  |
| **High cholesterol** | **+0.5779** | 0.2755 | ±0.5509 | **+2.098** | **0.0359** | * |
| Kidney disease | -0.7008 | 0.6539 | ±1.3079 | -1.072 | 0.2839 |  |
| **Circulatory disease** | **-0.9599** | 0.4055 | ±0.8109 | **-2.367** | **0.0179** | * |
| SD of daily means (mg/dL) | +0.0244 | 0.0366 | ±0.0732 | +0.667 | 0.5049 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **408**, R² = **0.1207**, Adj R² = **0.0963**, F-statistic = **4.94** (p = **3.33e-07**), Residual SE = **2.500** on **396** df, AIC = **1917.3**, BIC = **1965.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.0662** | 2.0705 | ±4.1409 | **+13.556** | **7.35e-42** | *** |
| **Education: graduate level (vs college)** | **+0.8076** | 0.2709 | ±0.5418 | **+2.981** | **0.0029** | ** |
| Education: high school or below (vs college) | -0.8215 | 0.6136 | ±1.2271 | -1.339 | 0.1806 |  |
| Site: UCSD (vs UAB) | -0.3609 | 0.3657 | ±0.7314 | -0.987 | 0.3237 |  |
| **Site: UW (vs UAB)** | **-0.5886** | 0.2765 | ±0.5531 | **-2.128** | **0.0333** | * |
| **Age (years)** | **-0.0499** | 0.0117 | ±0.0233 | **-4.283** | **1.84e-05** | *** |
| BMI (kg/m2) | -0.0089 | 0.0165 | ±0.0329 | -0.541 | 0.5883 |  |
| Hypertension | +0.1189 | 0.2787 | ±0.5575 | +0.427 | 0.6697 |  |
| **High cholesterol** | **+0.5734** | 0.2752 | ±0.5504 | **+2.083** | **0.0372** | * |
| Kidney disease | -0.6344 | 0.6552 | ±1.3105 | -0.968 | 0.3329 |  |
| **Circulatory disease** | **-0.9703** | 0.4032 | ±0.8064 | **-2.406** | **0.0161** | * |
| Time in range 70-180, pooled (%) | +0.0154 | 0.0193 | ±0.0386 | +0.795 | 0.4264 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **408**, R² = **0.1204**, Adj R² = **0.0959**, F-statistic = **4.93** (p = **3.57e-07**), Residual SE = **2.500** on **396** df, AIC = **1917.4**, BIC = **1965.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.4556** | 2.0124 | ±4.0247 | **+14.140** | **2.14e-45** | *** |
| **Education: graduate level (vs college)** | **+0.8070** | 0.2710 | ±0.5419 | **+2.978** | **0.0029** | ** |
| Education: high school or below (vs college) | -0.8226 | 0.6137 | ±1.2273 | -1.340 | 0.1801 |  |
| Site: UCSD (vs UAB) | -0.3571 | 0.3654 | ±0.7308 | -0.977 | 0.3284 |  |
| **Site: UW (vs UAB)** | **-0.5864** | 0.2768 | ±0.5536 | **-2.118** | **0.0342** | * |
| **Age (years)** | **-0.0500** | 0.0117 | ±0.0233 | **-4.284** | **1.83e-05** | *** |
| BMI (kg/m2) | -0.0088 | 0.0165 | ±0.0329 | -0.537 | 0.5911 |  |
| Hypertension | +0.1179 | 0.2790 | ±0.5580 | +0.423 | 0.6726 |  |
| **High cholesterol** | **+0.5762** | 0.2754 | ±0.5508 | **+2.092** | **0.0364** | * |
| Kidney disease | -0.6470 | 0.6546 | ±1.3092 | -0.988 | 0.3230 |  |
| **Circulatory disease** | **-0.9666** | 0.4032 | ±0.8064 | **-2.397** | **0.0165** | * |
| Avg. daily time in range 70-180 (%) | +0.0113 | 0.0183 | ±0.0366 | +0.615 | 0.5388 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **408**, R² = **0.1200**, Adj R² = **0.0955**, F-statistic = **4.91** (p = **3.83e-07**), Residual SE = **2.501** on **396** df, AIC = **1917.6**, BIC = **1965.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.6008** | 0.9239 | ±1.8478 | **+32.039** | **3.11e-225** | *** |
| **Education: graduate level (vs college)** | **+0.8066** | 0.2728 | ±0.5456 | **+2.957** | **0.0031** | ** |
| Education: high school or below (vs college) | -0.8235 | 0.6156 | ±1.2312 | -1.338 | 0.1810 |  |
| Site: UCSD (vs UAB) | -0.3641 | 0.3657 | ±0.7315 | -0.995 | 0.3195 |  |
| **Site: UW (vs UAB)** | **-0.5897** | 0.2785 | ±0.5569 | **-2.117** | **0.0342** | * |
| **Age (years)** | **-0.0505** | 0.0117 | ±0.0235 | **-4.302** | **1.69e-05** | *** |
| BMI (kg/m2) | -0.0093 | 0.0167 | ±0.0334 | -0.556 | 0.5780 |  |
| Hypertension | +0.1117 | 0.2798 | ±0.5597 | +0.399 | 0.6897 |  |
| **High cholesterol** | **+0.5722** | 0.2761 | ±0.5522 | **+2.072** | **0.0382** | * |
| Kidney disease | -0.6818 | 0.6538 | ±1.3075 | -1.043 | 0.2970 |  |
| **Circulatory disease** | **-0.9597** | 0.4034 | ±0.8068 | **-2.379** | **0.0173** | * |
| Time < 54 (%) | -0.0330 | 0.2311 | ±0.4623 | -0.143 | 0.8864 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **408**, R² = **0.1199**, Adj R² = **0.0954**, F-statistic = **4.90** (p = **3.92e-07**), Residual SE = **2.501** on **396** df, AIC = **1917.7**, BIC = **1965.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5763** | 0.9085 | ±1.8170 | **+32.556** | **1.73e-232** | *** |
| **Education: graduate level (vs college)** | **+0.8071** | 0.2724 | ±0.5448 | **+2.963** | **0.0030** | ** |
| Education: high school or below (vs college) | -0.8200 | 0.6181 | ±1.2361 | -1.327 | 0.1846 |  |
| Site: UCSD (vs UAB) | -0.3548 | 0.3645 | ±0.7290 | -0.973 | 0.3304 |  |
| **Site: UW (vs UAB)** | **-0.5832** | 0.2788 | ±0.5576 | **-2.092** | **0.0365** | * |
| **Age (years)** | **-0.0505** | 0.0117 | ±0.0234 | **-4.313** | **1.61e-05** | *** |
| BMI (kg/m2) | -0.0091 | 0.0166 | ±0.0332 | -0.550 | 0.5821 |  |
| Hypertension | +0.1142 | 0.2806 | ±0.5611 | +0.407 | 0.6840 |  |
| **High cholesterol** | **+0.5772** | 0.2763 | ±0.5527 | **+2.089** | **0.0367** | * |
| Kidney disease | -0.6838 | 0.6536 | ±1.3073 | -1.046 | 0.2955 |  |
| **Circulatory disease** | **-0.9577** | 0.4038 | ±0.8077 | **-2.371** | **0.0177** | * |
| Avg. daily time < 54 (%) | -0.0108 | 0.2345 | ±0.4691 | -0.046 | 0.9634 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **408**, R² = **0.1220**, Adj R² = **0.0976**, F-statistic = **5.00** (p = **2.63e-07**), Residual SE = **2.498** on **396** df, AIC = **1916.7**, BIC = **1964.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.6865** | 0.9146 | ±1.8292 | **+32.458** | **4.22e-231** | *** |
| **Education: graduate level (vs college)** | **+0.8005** | 0.2717 | ±0.5434 | **+2.946** | **0.0032** | ** |
| Education: high school or below (vs college) | -0.8487 | 0.6117 | ±1.2234 | -1.387 | 0.1653 |  |
| Site: UCSD (vs UAB) | -0.3770 | 0.3627 | ±0.7255 | -1.039 | 0.2987 |  |
| **Site: UW (vs UAB)** | **-0.6146** | 0.2750 | ±0.5500 | **-2.235** | **0.0254** | * |
| **Age (years)** | **-0.0506** | 0.0117 | ±0.0234 | **-4.328** | **1.51e-05** | *** |
| BMI (kg/m2) | -0.0086 | 0.0164 | ±0.0328 | -0.522 | 0.6017 |  |
| Hypertension | +0.0942 | 0.2791 | ±0.5582 | +0.338 | 0.7356 |  |
| **High cholesterol** | **+0.5589** | 0.2747 | ±0.5493 | **+2.035** | **0.0419** | * |
| Kidney disease | -0.6865 | 0.6510 | ±1.3021 | -1.054 | 0.2917 |  |
| **Circulatory disease** | **-0.9672** | 0.4023 | ±0.8047 | **-2.404** | **0.0162** | * |
| Time 54-69, pooled (%) | -0.0577 | 0.0441 | ±0.0881 | -1.309 | 0.1904 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **408**, R² = **0.1214**, Adj R² = **0.0970**, F-statistic = **4.97** (p = **2.93e-07**), Residual SE = **2.499** on **396** df, AIC = **1916.9**, BIC = **1965.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.6476** | 0.9118 | ±1.8237 | **+32.514** | **6.83e-232** | *** |
| **Education: graduate level (vs college)** | **+0.7992** | 0.2722 | ±0.5444 | **+2.936** | **0.0033** | ** |
| Education: high school or below (vs college) | -0.8499 | 0.6136 | ±1.2271 | -1.385 | 0.1660 |  |
| Site: UCSD (vs UAB) | -0.3687 | 0.3631 | ±0.7261 | -1.015 | 0.3099 |  |
| **Site: UW (vs UAB)** | **-0.6112** | 0.2753 | ±0.5505 | **-2.220** | **0.0264** | * |
| **Age (years)** | **-0.0504** | 0.0117 | ±0.0234 | **-4.312** | **1.62e-05** | *** |
| BMI (kg/m2) | -0.0086 | 0.0164 | ±0.0328 | -0.522 | 0.6015 |  |
| Hypertension | +0.0961 | 0.2802 | ±0.5603 | +0.343 | 0.7316 |  |
| **High cholesterol** | **+0.5627** | 0.2748 | ±0.5496 | **+2.048** | **0.0406** | * |
| Kidney disease | -0.6878 | 0.6520 | ±1.3039 | -1.055 | 0.2915 |  |
| **Circulatory disease** | **-0.9633** | 0.4025 | ±0.8050 | **-2.393** | **0.0167** | * |
| Avg. daily time 54-69 (%) | -0.0481 | 0.0440 | ±0.0880 | -1.094 | 0.2739 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **408**, R² = **0.1215**, Adj R² = **0.0971**, F-statistic = **4.98** (p = **2.88e-07**), Residual SE = **2.499** on **396** df, AIC = **1916.9**, BIC = **1965.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.6879** | 0.9204 | ±1.8407 | **+32.257** | **2.85e-228** | *** |
| **Education: graduate level (vs college)** | **+0.8013** | 0.2720 | ±0.5439 | **+2.946** | **0.0032** | ** |
| Education: high school or below (vs college) | -0.8457 | 0.6130 | ±1.2259 | -1.380 | 0.1677 |  |
| Site: UCSD (vs UAB) | -0.3840 | 0.3630 | ±0.7261 | -1.058 | 0.2901 |  |
| **Site: UW (vs UAB)** | **-0.6158** | 0.2755 | ±0.5509 | **-2.236** | **0.0254** | * |
| **Age (years)** | **-0.0505** | 0.0117 | ±0.0234 | **-4.320** | **1.56e-05** | *** |
| BMI (kg/m2) | -0.0089 | 0.0165 | ±0.0329 | -0.544 | 0.5866 |  |
| Hypertension | +0.0959 | 0.2792 | ±0.5584 | +0.344 | 0.7311 |  |
| **High cholesterol** | **+0.5569** | 0.2747 | ±0.5495 | **+2.027** | **0.0427** | * |
| Kidney disease | -0.6825 | 0.6501 | ±1.3002 | -1.050 | 0.2938 |  |
| **Circulatory disease** | **-0.9676** | 0.4031 | ±0.8062 | **-2.400** | **0.0164** | * |
| Time < 70 (%) | -0.0404 | 0.0393 | ±0.0787 | -1.028 | 0.3038 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **408**, R² = **0.1210**, Adj R² = **0.0966**, F-statistic = **4.95** (p = **3.18e-07**), Residual SE = **2.499** on **396** df, AIC = **1917.1**, BIC = **1965.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.6400** | 0.9131 | ±1.8262 | **+32.460** | **3.90e-231** | *** |
| **Education: graduate level (vs college)** | **+0.7998** | 0.2725 | ±0.5449 | **+2.935** | **0.0033** | ** |
| Education: high school or below (vs college) | -0.8452 | 0.6150 | ±1.2300 | -1.374 | 0.1694 |  |
| Site: UCSD (vs UAB) | -0.3718 | 0.3631 | ±0.7262 | -1.024 | 0.3058 |  |
| **Site: UW (vs UAB)** | **-0.6112** | 0.2755 | ±0.5509 | **-2.219** | **0.0265** | * |
| **Age (years)** | **-0.0503** | 0.0117 | ±0.0234 | **-4.306** | **1.66e-05** | *** |
| BMI (kg/m2) | -0.0088 | 0.0165 | ±0.0329 | -0.536 | 0.5918 |  |
| Hypertension | +0.0975 | 0.2804 | ±0.5607 | +0.348 | 0.7281 |  |
| **High cholesterol** | **+0.5627** | 0.2751 | ±0.5501 | **+2.046** | **0.0408** | * |
| Kidney disease | -0.6843 | 0.6515 | ±1.3030 | -1.050 | 0.2935 |  |
| **Circulatory disease** | **-0.9638** | 0.4032 | ±0.8065 | **-2.390** | **0.0168** | * |
| Avg. daily time < 70 (%) | -0.0339 | 0.0393 | ±0.0787 | -0.863 | 0.3881 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **408**, R² = **0.1199**, Adj R² = **0.0954**, F-statistic = **4.90** (p = **3.92e-07**), Residual SE = **2.501** on **396** df, AIC = **1917.7**, BIC = **1965.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.0412** | 11.7405 | ±23.4809 | **+2.559** | **0.0105** | * |
| **Education: graduate level (vs college)** | **+0.8079** | 0.2716 | ±0.5431 | **+2.975** | **0.0029** | ** |
| Education: high school or below (vs college) | -0.8179 | 0.6150 | ±1.2300 | -1.330 | 0.1835 |  |
| Site: UCSD (vs UAB) | -0.3506 | 0.3687 | ±0.7375 | -0.951 | 0.3417 |  |
| **Site: UW (vs UAB)** | **-0.5787** | 0.2770 | ±0.5540 | **-2.089** | **0.0367** | * |
| **Age (years)** | **-0.0505** | 0.0117 | ±0.0233 | **-4.334** | **1.47e-05** | *** |
| BMI (kg/m2) | -0.0091 | 0.0166 | ±0.0333 | -0.546 | 0.5853 |  |
| Hypertension | +0.1159 | 0.2793 | ±0.5586 | +0.415 | 0.6781 |  |
| **High cholesterol** | **+0.5799** | 0.2732 | ±0.5464 | **+2.123** | **0.0338** | * |
| Kidney disease | -0.6876 | 0.6670 | ±1.3340 | -1.031 | 0.3026 |  |
| **Circulatory disease** | **-0.9560** | 0.4028 | ±0.8055 | **-2.374** | **0.0176** | * |
| Time 54-250, pooled (%) | -0.0047 | 0.1186 | ±0.2373 | -0.040 | 0.9682 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **408**, R² = **0.1203**, Adj R² = **0.0959**, F-statistic = **4.92** (p = **3.61e-07**), Residual SE = **2.500** on **396** df, AIC = **1917.5**, BIC = **1965.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+34.9073** | 10.5949 | ±21.1898 | **+3.295** | **9.85e-04** | *** |
| **Education: graduate level (vs college)** | **+0.8115** | 0.2709 | ±0.5418 | **+2.996** | **0.0027** | ** |
| Education: high school or below (vs college) | -0.8103 | 0.6175 | ±1.2350 | -1.312 | 0.1895 |  |
| Site: UCSD (vs UAB) | -0.3387 | 0.3686 | ±0.7373 | -0.919 | 0.3582 |  |
| **Site: UW (vs UAB)** | **-0.5641** | 0.2772 | ±0.5544 | **-2.035** | **0.0418** | * |
| **Age (years)** | **-0.0510** | 0.0117 | ±0.0234 | **-4.364** | **1.27e-05** | *** |
| BMI (kg/m2) | -0.0090 | 0.0165 | ±0.0330 | -0.547 | 0.5843 |  |
| Hypertension | +0.1207 | 0.2791 | ±0.5581 | +0.432 | 0.6654 |  |
| **High cholesterol** | **+0.5887** | 0.2734 | ±0.5468 | **+2.153** | **0.0313** | * |
| Kidney disease | -0.7205 | 0.6687 | ±1.3374 | -1.077 | 0.2813 |  |
| **Circulatory disease** | **-0.9473** | 0.4034 | ±0.8068 | **-2.348** | **0.0189** | * |
| Avg. daily time 54-250 (%) | -0.0535 | 0.1067 | ±0.2133 | -0.501 | 0.6161 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **408**, R² = **0.1200**, Adj R² = **0.0956**, F-statistic = **4.91** (p = **3.79e-07**), Residual SE = **2.501** on **396** df, AIC = **1917.6**, BIC = **1965.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5651** | 0.9009 | ±1.8018 | **+32.818** | **3.29e-236** | *** |
| **Education: graduate level (vs college)** | **+0.8091** | 0.2714 | ±0.5428 | **+2.981** | **0.0029** | ** |
| Education: high school or below (vs college) | -0.8143 | 0.6156 | ±1.2312 | -1.323 | 0.1859 |  |
| Site: UCSD (vs UAB) | -0.3503 | 0.3633 | ±0.7265 | -0.964 | 0.3349 |  |
| **Site: UW (vs UAB)** | **-0.5769** | 0.2775 | ±0.5550 | **-2.079** | **0.0376** | * |
| **Age (years)** | **-0.0502** | 0.0117 | ±0.0235 | **-4.278** | **1.88e-05** | *** |
| BMI (kg/m2) | -0.0090 | 0.0165 | ±0.0329 | -0.548 | 0.5835 |  |
| Hypertension | +0.1214 | 0.2809 | ±0.5618 | +0.432 | 0.6656 |  |
| **High cholesterol** | **+0.5810** | 0.2763 | ±0.5525 | **+2.103** | **0.0355** | * |
| Kidney disease | -0.6612 | 0.6533 | ±1.3067 | -1.012 | 0.3115 |  |
| **Circulatory disease** | **-0.9614** | 0.4028 | ±0.8056 | **-2.387** | **0.0170** | * |
| Time 181-250, pooled (%) | -0.0088 | 0.0252 | ±0.0504 | -0.350 | 0.7263 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **408**, R² = **0.1200**, Adj R² = **0.0956**, F-statistic = **4.91** (p = **3.80e-07**), Residual SE = **2.501** on **396** df, AIC = **1917.6**, BIC = **1965.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5641** | 0.9011 | ±1.8022 | **+32.809** | **4.42e-236** | *** |
| **Education: graduate level (vs college)** | **+0.8092** | 0.2715 | ±0.5430 | **+2.980** | **0.0029** | ** |
| Education: high school or below (vs college) | -0.8150 | 0.6155 | ±1.2310 | -1.324 | 0.1855 |  |
| Site: UCSD (vs UAB) | -0.3509 | 0.3634 | ±0.7268 | -0.966 | 0.3342 |  |
| **Site: UW (vs UAB)** | **-0.5771** | 0.2773 | ±0.5547 | **-2.081** | **0.0375** | * |
| **Age (years)** | **-0.0502** | 0.0117 | ±0.0235 | **-4.282** | **1.85e-05** | *** |
| BMI (kg/m2) | -0.0090 | 0.0165 | ±0.0329 | -0.546 | 0.5848 |  |
| Hypertension | +0.1212 | 0.2811 | ±0.5622 | +0.431 | 0.6663 |  |
| **High cholesterol** | **+0.5811** | 0.2762 | ±0.5524 | **+2.104** | **0.0354** | * |
| Kidney disease | -0.6628 | 0.6525 | ±1.3050 | -1.016 | 0.3097 |  |
| **Circulatory disease** | **-0.9613** | 0.4026 | ±0.8052 | **-2.388** | **0.0170** | * |
| Avg. daily time 181-250 (%) | -0.0080 | 0.0236 | ±0.0473 | -0.337 | 0.7358 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **408**, R² = **0.1199**, Adj R² = **0.0955**, F-statistic = **4.91** (p = **3.86e-07**), Residual SE = **2.501** on **396** df, AIC = **1917.6**, BIC = **1965.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5670** | 0.9012 | ±1.8024 | **+32.809** | **4.34e-236** | *** |
| **Education: graduate level (vs college)** | **+0.8085** | 0.2714 | ±0.5428 | **+2.979** | **0.0029** | ** |
| Education: high school or below (vs college) | -0.8161 | 0.6154 | ±1.2308 | -1.326 | 0.1848 |  |
| Site: UCSD (vs UAB) | -0.3511 | 0.3634 | ±0.7268 | -0.966 | 0.3340 |  |
| **Site: UW (vs UAB)** | **-0.5785** | 0.2775 | ±0.5550 | **-2.085** | **0.0371** | * |
| **Age (years)** | **-0.0503** | 0.0117 | ±0.0235 | **-4.289** | **1.80e-05** | *** |
| BMI (kg/m2) | -0.0091 | 0.0165 | ±0.0329 | -0.550 | 0.5822 |  |
| Hypertension | +0.1193 | 0.2808 | ±0.5616 | +0.425 | 0.6710 |  |
| **High cholesterol** | **+0.5797** | 0.2761 | ±0.5522 | **+2.100** | **0.0358** | * |
| Kidney disease | -0.6676 | 0.6566 | ±1.3133 | -1.017 | 0.3093 |  |
| **Circulatory disease** | **-0.9601** | 0.4025 | ±0.8051 | **-2.385** | **0.0171** | * |
| Time > 180 (%) | -0.0053 | 0.0219 | ±0.0438 | -0.241 | 0.8096 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **408**, R² = **0.1199**, Adj R² = **0.0955**, F-statistic = **4.90** (p = **3.90e-07**), Residual SE = **2.501** on **396** df, AIC = **1917.6**, BIC = **1965.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5676** | 0.9015 | ±1.8030 | **+32.799** | **6.06e-236** | *** |
| **Education: graduate level (vs college)** | **+0.8083** | 0.2715 | ±0.5430 | **+2.977** | **0.0029** | ** |
| Education: high school or below (vs college) | -0.8171 | 0.6152 | ±1.2304 | -1.328 | 0.1841 |  |
| Site: UCSD (vs UAB) | -0.3518 | 0.3636 | ±0.7272 | -0.967 | 0.3333 |  |
| **Site: UW (vs UAB)** | **-0.5790** | 0.2774 | ±0.5548 | **-2.087** | **0.0369** | * |
| **Age (years)** | **-0.0504** | 0.0117 | ±0.0234 | **-4.296** | **1.74e-05** | *** |
| BMI (kg/m2) | -0.0091 | 0.0165 | ±0.0329 | -0.550 | 0.5825 |  |
| Hypertension | +0.1182 | 0.2810 | ±0.5620 | +0.421 | 0.6741 |  |
| **High cholesterol** | **+0.5796** | 0.2761 | ±0.5522 | **+2.099** | **0.0358** | * |
| Kidney disease | -0.6729 | 0.6557 | ±1.3113 | -1.026 | 0.3047 |  |
| **Circulatory disease** | **-0.9592** | 0.4024 | ±0.8047 | **-2.384** | **0.0171** | * |
| Avg. daily time > 180 (%) | -0.0035 | 0.0202 | ±0.0405 | -0.172 | 0.8632 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **408**, R² = **0.1199**, Adj R² = **0.0955**, F-statistic = **4.90** (p = **3.89e-07**), Residual SE = **2.501** on **396** df, AIC = **1917.6**, BIC = **1965.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5777** | 0.9024 | ±1.8048 | **+32.778** | **1.23e-235** | *** |
| **Education: graduate level (vs college)** | **+0.8094** | 0.2704 | ±0.5408 | **+2.993** | **0.0028** | ** |
| Education: high school or below (vs college) | -0.8212 | 0.6153 | ±1.2307 | -1.335 | 0.1820 |  |
| Site: UCSD (vs UAB) | -0.3518 | 0.3646 | ±0.7292 | -0.965 | 0.3345 |  |
| **Site: UW (vs UAB)** | **-0.5807** | 0.2775 | ±0.5551 | **-2.092** | **0.0364** | * |
| **Age (years)** | **-0.0506** | 0.0117 | ±0.0234 | **-4.322** | **1.55e-05** | *** |
| BMI (kg/m2) | -0.0093 | 0.0165 | ±0.0329 | -0.565 | 0.5721 |  |
| Hypertension | +0.1125 | 0.2811 | ±0.5622 | +0.400 | 0.6890 |  |
| **High cholesterol** | **+0.5790** | 0.2751 | ±0.5502 | **+2.105** | **0.0353** | * |
| Kidney disease | -0.6851 | 0.6532 | ±1.3064 | -1.049 | 0.2943 |  |
| **Circulatory disease** | **-0.9522** | 0.4026 | ±0.8052 | **-2.365** | **0.0180** | * |
| Nocturnal time > 180 (%) | +0.0042 | 0.0218 | ±0.0436 | +0.191 | 0.8485 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **408**, R² = **0.1202**, Adj R² = **0.0957**, F-statistic = **4.92** (p = **3.69e-07**), Residual SE = **2.500** on **396** df, AIC = **1917.5**, BIC = **1965.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5788** | 0.8998 | ±1.7997 | **+32.871** | **5.65e-237** | *** |
| **Education: graduate level (vs college)** | **+0.8037** | 0.2710 | ±0.5420 | **+2.966** | **0.0030** | ** |
| Education: high school or below (vs college) | -0.8201 | 0.6148 | ±1.2295 | -1.334 | 0.1822 |  |
| Site: UCSD (vs UAB) | -0.3441 | 0.3614 | ±0.7229 | -0.952 | 0.3410 |  |
| **Site: UW (vs UAB)** | **-0.5809** | 0.2774 | ±0.5549 | **-2.094** | **0.0363** | * |
| **Age (years)** | **-0.0501** | 0.0118 | ±0.0235 | **-4.262** | **2.02e-05** | *** |
| BMI (kg/m2) | -0.0094 | 0.0165 | ±0.0331 | -0.567 | 0.5706 |  |
| Hypertension | +0.1213 | 0.2805 | ±0.5609 | +0.432 | 0.6654 |  |
| **High cholesterol** | **+0.5772** | 0.2757 | ±0.5514 | **+2.094** | **0.0363** | * |
| Kidney disease | -0.6702 | 0.6643 | ±1.3285 | -1.009 | 0.3130 |  |
| **Circulatory disease** | **-0.9621** | 0.4035 | ±0.8070 | **-2.384** | **0.0171** | * |
| Any reading > 250 during wear (0/1) | -0.1306 | 0.3997 | ±0.7995 | -0.327 | 0.7438 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **408**, R² = **0.1202**, Adj R² = **0.0958**, F-statistic = **4.92** (p = **3.66e-07**), Residual SE = **2.500** on **396** df, AIC = **1917.5**, BIC = **1965.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5816** | 0.9015 | ±1.8030 | **+32.813** | **3.82e-236** | *** |
| **Education: graduate level (vs college)** | **+0.8081** | 0.2714 | ±0.5428 | **+2.978** | **0.0029** | ** |
| Education: high school or below (vs college) | -0.8177 | 0.6145 | ±1.2290 | -1.331 | 0.1833 |  |
| Site: UCSD (vs UAB) | -0.3523 | 0.3652 | ±0.7304 | -0.965 | 0.3347 |  |
| **Site: UW (vs UAB)** | **-0.5770** | 0.2772 | ±0.5544 | **-2.082** | **0.0374** | * |
| **Age (years)** | **-0.0509** | 0.0117 | ±0.0234 | **-4.349** | **1.36e-05** | *** |
| BMI (kg/m2) | -0.0091 | 0.0165 | ±0.0330 | -0.553 | 0.5805 |  |
| Hypertension | +0.1124 | 0.2798 | ±0.5595 | +0.402 | 0.6878 |  |
| **High cholesterol** | **+0.5838** | 0.2736 | ±0.5471 | **+2.134** | **0.0328** | * |
| Kidney disease | -0.7258 | 0.6806 | ±1.3613 | -1.066 | 0.2863 |  |
| **Circulatory disease** | **-0.9498** | 0.4024 | ±0.8047 | **-2.360** | **0.0183** | * |
| Time > 250 (%) | +0.0733 | 0.1823 | ±0.3645 | +0.402 | 0.6876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 408)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **408**, R² = **0.1209**, Adj R² = **0.0965**, F-statistic = **4.95** (p = **3.22e-07**), Residual SE = **2.499** on **396** df, AIC = **1917.2**, BIC = **1965.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5953** | 0.9016 | ±1.8033 | **+32.824** | **2.66e-236** | *** |
| **Education: graduate level (vs college)** | **+0.8093** | 0.2719 | ±0.5438 | **+2.976** | **0.0029** | ** |
| Education: high school or below (vs college) | -0.8158 | 0.6151 | ±1.2302 | -1.326 | 0.1848 |  |
| Site: UCSD (vs UAB) | -0.3500 | 0.3656 | ±0.7313 | -0.957 | 0.3384 |  |
| **Site: UW (vs UAB)** | **-0.5762** | 0.2774 | ±0.5549 | **-2.077** | **0.0378** | * |
| **Age (years)** | **-0.0511** | 0.0117 | ±0.0234 | **-4.373** | **1.23e-05** | *** |
| BMI (kg/m2) | -0.0093 | 0.0164 | ±0.0328 | -0.564 | 0.5730 |  |
| Hypertension | +0.1117 | 0.2794 | ±0.5588 | +0.400 | 0.6893 |  |
| **High cholesterol** | **+0.5842** | 0.2745 | ±0.5491 | **+2.128** | **0.0333** | * |
| Kidney disease | -0.7536 | 0.6772 | ±1.3544 | -1.113 | 0.2657 |  |
| **Circulatory disease** | **-0.9444** | 0.4027 | ±0.8054 | **-2.345** | **0.0190** | * |
| Avg. daily time > 250 (%) | +0.1153 | 0.1978 | ±0.3956 | +0.583 | 0.5600 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 408; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0750**, LLR χ² = **37.44** (p = **4.75e-05**), AUC = **0.6789**, AIC = **484.0**, BIC = **528.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3301** | 0.9116 | ±1.8232 | **-3.653** | **2.59e-04** | 0.0358 | *** |
| **Education: graduate level (vs college)** | **-0.6718** | 0.2518 | ±0.5035 | **-2.669** | **0.0076** | 0.5108 | ** |
| Education: high school or below (vs college) | +0.6497 | 0.4299 | ±0.8597 | +1.511 | 0.1307 | 1.9149 |  |
| Site: UCSD (vs UAB) | +0.2011 | 0.3123 | ±0.6246 | +0.644 | 0.5197 | 1.2227 |  |
| Site: UW (vs UAB) | +0.1304 | 0.2682 | ±0.5364 | +0.486 | 0.6267 | 1.1393 |  |
| **Age (years)** | **+0.0390** | 0.0110 | ±0.0221 | **+3.534** | **4.09e-04** | 1.0397 | *** |
| BMI (kg/m2) | +0.0126 | 0.0162 | ±0.0323 | +0.781 | 0.4346 | 1.0127 |  |
| Hypertension | -0.4211 | 0.2603 | ±0.5207 | -1.618 | 0.1057 | 0.6563 |  |
| High cholesterol | -0.2299 | 0.2468 | ±0.4936 | -0.931 | 0.3516 | 0.7946 |  |
| Kidney disease | +0.3452 | 0.4523 | ±0.9045 | +0.763 | 0.4453 | 1.4123 |  |
| **Circulatory disease** | **+0.6842** | 0.3060 | ±0.6121 | **+2.236** | **0.0254** | 1.9822 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0761**, LLR χ² = **38.01** (p = **7.78e-05**), AUC = **0.6794**, AIC = **485.5**, BIC = **533.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.3683** | 1.6405 | ±3.2810 | **-2.663** | **0.0077** | 0.0127 | ** |
| **Education: graduate level (vs college)** | **-0.6619** | 0.2522 | ±0.5044 | **-2.625** | **0.0087** | 0.5159 | ** |
| Education: high school or below (vs college) | +0.6297 | 0.4306 | ±0.8612 | +1.462 | 0.1437 | 1.8770 |  |
| Site: UCSD (vs UAB) | +0.1696 | 0.3153 | ±0.6306 | +0.538 | 0.5907 | 1.1848 |  |
| Site: UW (vs UAB) | +0.1232 | 0.2686 | ±0.5371 | +0.459 | 0.6464 | 1.1311 |  |
| **Age (years)** | **+0.0377** | 0.0112 | ±0.0223 | **+3.381** | **7.23e-04** | 1.0384 | *** |
| BMI (kg/m2) | +0.0109 | 0.0164 | ±0.0327 | +0.664 | 0.5065 | 1.0109 |  |
| Hypertension | -0.4180 | 0.2607 | ±0.5214 | -1.604 | 0.1088 | 0.6583 |  |
| High cholesterol | -0.2587 | 0.2498 | ±0.4995 | -1.036 | 0.3003 | 0.7721 |  |
| Kidney disease | +0.3340 | 0.4539 | ±0.9078 | +0.736 | 0.4618 | 1.3966 |  |
| **Circulatory disease** | **+0.6971** | 0.3069 | ±0.6137 | **+2.272** | **0.0231** | 2.0079 | * |
| HbA1c (%) | +0.2095 | 0.2730 | ±0.5459 | +0.767 | 0.4429 | 1.2330 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0765**, LLR χ² = **38.19** (p = **7.27e-05**), AUC = **0.6806**, AIC = **485.3**, BIC = **533.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.5930** | 1.2499 | ±2.4997 | **-2.075** | **0.0380** | 0.0748 | * |
| **Education: graduate level (vs college)** | **-0.6617** | 0.2524 | ±0.5048 | **-2.622** | **0.0087** | 0.5160 | ** |
| Education: high school or below (vs college) | +0.6795 | 0.4324 | ±0.8647 | +1.572 | 0.1160 | 1.9730 |  |
| Site: UCSD (vs UAB) | +0.2084 | 0.3129 | ±0.6259 | +0.666 | 0.5055 | 1.2317 |  |
| Site: UW (vs UAB) | +0.1606 | 0.2708 | ±0.5416 | +0.593 | 0.5531 | 1.1742 |  |
| **Age (years)** | **+0.0398** | 0.0111 | ±0.0222 | **+3.586** | **3.36e-04** | 1.0406 | *** |
| BMI (kg/m2) | +0.0133 | 0.0162 | ±0.0324 | +0.820 | 0.4125 | 1.0134 |  |
| Hypertension | -0.3974 | 0.2614 | ±0.5228 | -1.520 | 0.1284 | 0.6721 |  |
| High cholesterol | -0.2115 | 0.2479 | ±0.4958 | -0.853 | 0.3936 | 0.8094 |  |
| Kidney disease | +0.3864 | 0.4559 | ±0.9117 | +0.848 | 0.3966 | 1.4717 |  |
| **Circulatory disease** | **+0.6826** | 0.3062 | ±0.6123 | **+2.230** | **0.0258** | 1.9791 | * |
| Mean glucose (mg/dL) | -0.0074 | 0.0086 | ±0.0173 | -0.857 | 0.3915 | 0.9926 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0765**, LLR χ² = **38.19** (p = **7.27e-05**), AUC = **0.6806**, AIC = **485.3**, BIC = **533.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.5681 | 2.2431 | ±4.4861 | -0.699 | 0.4845 | 0.2084 |  |
| **Education: graduate level (vs college)** | **-0.6617** | 0.2524 | ±0.5048 | **-2.622** | **0.0087** | 0.5160 | ** |
| Education: high school or below (vs college) | +0.6795 | 0.4324 | ±0.8647 | +1.572 | 0.1160 | 1.9730 |  |
| Site: UCSD (vs UAB) | +0.2084 | 0.3129 | ±0.6259 | +0.666 | 0.5055 | 1.2317 |  |
| Site: UW (vs UAB) | +0.1606 | 0.2708 | ±0.5416 | +0.593 | 0.5531 | 1.1742 |  |
| **Age (years)** | **+0.0398** | 0.0111 | ±0.0222 | **+3.586** | **3.36e-04** | 1.0406 | *** |
| BMI (kg/m2) | +0.0133 | 0.0162 | ±0.0324 | +0.820 | 0.4125 | 1.0134 |  |
| Hypertension | -0.3974 | 0.2614 | ±0.5228 | -1.520 | 0.1284 | 0.6721 |  |
| High cholesterol | -0.2115 | 0.2479 | ±0.4958 | -0.853 | 0.3936 | 0.8094 |  |
| Kidney disease | +0.3864 | 0.4559 | ±0.9117 | +0.848 | 0.3966 | 1.4717 |  |
| **Circulatory disease** | **+0.6826** | 0.3062 | ±0.6123 | **+2.230** | **0.0258** | 1.9791 | * |
| GMI (%) | -0.3097 | 0.3613 | ±0.7227 | -0.857 | 0.3915 | 0.7337 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0771**, LLR χ² = **38.51** (p = **6.42e-05**), AUC = **0.6820**, AIC = **485.0**, BIC = **533.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.5340** | 1.1964 | ±2.3928 | **-2.118** | **0.0342** | 0.0793 | * |
| **Education: graduate level (vs college)** | **-0.6664** | 0.2524 | ±0.5047 | **-2.641** | **0.0083** | 0.5135 | ** |
| Education: high school or below (vs college) | +0.6927 | 0.4329 | ±0.8658 | +1.600 | 0.1095 | 1.9991 |  |
| Site: UCSD (vs UAB) | +0.2177 | 0.3133 | ±0.6267 | +0.695 | 0.4872 | 1.2432 |  |
| Site: UW (vs UAB) | +0.1583 | 0.2700 | ±0.5401 | +0.586 | 0.5578 | 1.1715 |  |
| **Age (years)** | **+0.0391** | 0.0111 | ±0.0221 | **+3.532** | **4.13e-04** | 1.0398 | *** |
| BMI (kg/m2) | +0.0151 | 0.0164 | ±0.0327 | +0.922 | 0.3564 | 1.0152 |  |
| Hypertension | -0.3971 | 0.2611 | ±0.5221 | -1.521 | 0.1282 | 0.6722 |  |
| High cholesterol | -0.2046 | 0.2484 | ±0.4967 | -0.824 | 0.4099 | 0.8149 |  |
| Kidney disease | +0.3515 | 0.4545 | ±0.9089 | +0.774 | 0.4392 | 1.4213 |  |
| **Circulatory disease** | **+0.6749** | 0.3060 | ±0.6119 | **+2.206** | **0.0274** | 1.9639 | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0081 | 0.0079 | ±0.0158 | -1.023 | 0.3065 | 0.9920 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0750**, LLR χ² = **37.45** (p = **9.70e-05**), AUC = **0.6790**, AIC = **486.0**, BIC = **534.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3098** | 0.9483 | ±1.8967 | **-3.490** | **4.83e-04** | 0.0365 | *** |
| **Education: graduate level (vs college)** | **-0.6712** | 0.2519 | ±0.5037 | **-2.665** | **0.0077** | 0.5111 | ** |
| Education: high school or below (vs college) | +0.6497 | 0.4300 | ±0.8600 | +1.511 | 0.1308 | 1.9149 |  |
| Site: UCSD (vs UAB) | +0.2023 | 0.3127 | ±0.6255 | +0.647 | 0.5177 | 1.2242 |  |
| Site: UW (vs UAB) | +0.1311 | 0.2683 | ±0.5367 | +0.488 | 0.6252 | 1.1400 |  |
| **Age (years)** | **+0.0391** | 0.0112 | ±0.0223 | **+3.503** | **4.60e-04** | 1.0399 | *** |
| BMI (kg/m2) | +0.0127 | 0.0162 | ±0.0323 | +0.783 | 0.4336 | 1.0127 |  |
| Hypertension | -0.4194 | 0.2612 | ±0.5224 | -1.606 | 0.1083 | 0.6574 |  |
| High cholesterol | -0.2307 | 0.2470 | ±0.4940 | -0.934 | 0.3504 | 0.7940 |  |
| Kidney disease | +0.3507 | 0.4577 | ±0.9153 | +0.766 | 0.4435 | 1.4201 |  |
| **Circulatory disease** | **+0.6836** | 0.3062 | ±0.6123 | **+2.233** | **0.0256** | 1.9810 | * |
| Glucose SD, pooled (mg/dL) | -0.0014 | 0.0178 | ±0.0356 | -0.078 | 0.9381 | 0.9986 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0750**, LLR χ² = **37.45** (p = **9.67e-05**), AUC = **0.6790**, AIC = **486.0**, BIC = **534.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3027** | 0.9422 | ±1.8844 | **-3.505** | **4.56e-04** | 0.0368 | *** |
| **Education: graduate level (vs college)** | **-0.6713** | 0.2518 | ±0.5036 | **-2.666** | **0.0077** | 0.5111 | ** |
| Education: high school or below (vs college) | +0.6504 | 0.4302 | ±0.8604 | +1.512 | 0.1305 | 1.9163 |  |
| Site: UCSD (vs UAB) | +0.2034 | 0.3130 | ±0.6259 | +0.650 | 0.5158 | 1.2256 |  |
| Site: UW (vs UAB) | +0.1318 | 0.2685 | ±0.5370 | +0.491 | 0.6234 | 1.1409 |  |
| **Age (years)** | **+0.0392** | 0.0112 | ±0.0224 | **+3.502** | **4.61e-04** | 1.0400 | *** |
| BMI (kg/m2) | +0.0127 | 0.0162 | ±0.0323 | +0.785 | 0.4326 | 1.0128 |  |
| Hypertension | -0.4187 | 0.2611 | ±0.5222 | -1.603 | 0.1088 | 0.6579 |  |
| High cholesterol | -0.2307 | 0.2469 | ±0.4937 | -0.934 | 0.3501 | 0.7940 |  |
| Kidney disease | +0.3539 | 0.4583 | ±0.9167 | +0.772 | 0.4401 | 1.4245 |  |
| **Circulatory disease** | **+0.6831** | 0.3062 | ±0.6125 | **+2.231** | **0.0257** | 1.9801 | * |
| Avg. daily SD (mg/dL) | -0.0022 | 0.0195 | ±0.0391 | -0.115 | 0.9084 | 0.9978 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0756**, LLR χ² = **37.76** (p = **8.60e-05**), AUC = **0.6795**, AIC = **485.7**, BIC = **533.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.5432** | 0.9885 | ±1.9769 | **-3.585** | **3.38e-04** | 0.0289 | *** |
| **Education: graduate level (vs college)** | **-0.6733** | 0.2520 | ±0.5039 | **-2.672** | **0.0075** | 0.5100 | ** |
| Education: high school or below (vs college) | +0.6587 | 0.4293 | ±0.8585 | +1.535 | 0.1249 | 1.9324 |  |
| Site: UCSD (vs UAB) | +0.1940 | 0.3128 | ±0.6256 | +0.620 | 0.5351 | 1.2141 |  |
| Site: UW (vs UAB) | +0.1362 | 0.2686 | ±0.5372 | +0.507 | 0.6121 | 1.1459 |  |
| **Age (years)** | **+0.0381** | 0.0111 | ±0.0223 | **+3.425** | **6.16e-04** | 1.0388 | *** |
| BMI (kg/m2) | +0.0126 | 0.0162 | ±0.0323 | +0.777 | 0.4372 | 1.0126 |  |
| Hypertension | -0.4280 | 0.2611 | ±0.5222 | -1.639 | 0.1012 | 0.6518 |  |
| High cholesterol | -0.2169 | 0.2481 | ±0.4962 | -0.874 | 0.3821 | 0.8051 |  |
| Kidney disease | +0.3144 | 0.4564 | ±0.9128 | +0.689 | 0.4908 | 1.3695 |  |
| **Circulatory disease** | **+0.6889** | 0.3059 | ±0.6118 | **+2.252** | **0.0243** | 1.9914 | * |
| CV (%) | +0.0137 | 0.0244 | ±0.0488 | +0.564 | 0.5728 | 1.0138 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0762**, LLR χ² = **38.07** (p = **7.63e-05**), AUC = **0.6780**, AIC = **485.4**, BIC = **533.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.7912** | 1.1340 | ±2.2680 | **-2.461** | **0.0138** | 0.0613 | * |
| **Education: graduate level (vs college)** | **-0.6825** | 0.2525 | ±0.5050 | **-2.703** | **0.0069** | 0.5053 | ** |
| Education: high school or below (vs college) | +0.6545 | 0.4289 | ±0.8578 | +1.526 | 0.1270 | 1.9242 |  |
| Site: UCSD (vs UAB) | +0.1882 | 0.3131 | ±0.6262 | +0.601 | 0.5477 | 1.2071 |  |
| Site: UW (vs UAB) | +0.1295 | 0.2685 | ±0.5370 | +0.482 | 0.6297 | 1.1382 |  |
| **Age (years)** | **+0.0377** | 0.0111 | ±0.0223 | **+3.389** | **7.02e-04** | 1.0384 | *** |
| BMI (kg/m2) | +0.0124 | 0.0162 | ±0.0323 | +0.765 | 0.4444 | 1.0124 |  |
| Hypertension | -0.4309 | 0.2613 | ±0.5227 | -1.649 | 0.0992 | 0.6499 | . |
| High cholesterol | -0.2197 | 0.2476 | ±0.4951 | -0.887 | 0.3749 | 0.8028 |  |
| Kidney disease | +0.3072 | 0.4552 | ±0.9105 | +0.675 | 0.4999 | 1.3596 |  |
| **Circulatory disease** | **+0.6883** | 0.3057 | ±0.6115 | **+2.251** | **0.0244** | 1.9904 | * |
| Mean / SD ratio | -0.0823 | 0.1042 | ±0.2084 | -0.790 | 0.4294 | 0.9210 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0760**, LLR χ² = **37.94** (p = **8.02e-05**), AUC = **0.6776**, AIC = **485.5**, BIC = **533.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8607** | 1.1265 | ±2.2529 | **-2.539** | **0.0111** | 0.0572 | * |
| **Education: graduate level (vs college)** | **-0.6817** | 0.2525 | ±0.5050 | **-2.700** | **0.0069** | 0.5057 | ** |
| Education: high school or below (vs college) | +0.6428 | 0.4289 | ±0.8578 | +1.499 | 0.1340 | 1.9017 |  |
| Site: UCSD (vs UAB) | +0.1841 | 0.3135 | ±0.6270 | +0.587 | 0.5571 | 1.2021 |  |
| Site: UW (vs UAB) | +0.1265 | 0.2685 | ±0.5371 | +0.471 | 0.6375 | 1.1349 |  |
| **Age (years)** | **+0.0378** | 0.0112 | ±0.0223 | **+3.388** | **7.04e-04** | 1.0385 | *** |
| BMI (kg/m2) | +0.0121 | 0.0162 | ±0.0324 | +0.749 | 0.4541 | 1.0122 |  |
| Hypertension | -0.4287 | 0.2613 | ±0.5226 | -1.641 | 0.1009 | 0.6514 |  |
| High cholesterol | -0.2236 | 0.2473 | ±0.4945 | -0.904 | 0.3658 | 0.7996 |  |
| Kidney disease | +0.3048 | 0.4562 | ±0.9125 | +0.668 | 0.5041 | 1.3564 |  |
| **Circulatory disease** | **+0.6897** | 0.3058 | ±0.6117 | **+2.255** | **0.0241** | 1.9932 | * |
| Avg. daily mean/SD | -0.0585 | 0.0832 | ±0.1663 | -0.704 | 0.4814 | 0.9431 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0751**, LLR χ² = **37.52** (p = **9.41e-05**), AUC = **0.6784**, AIC = **486.0**, BIC = **534.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.5044** | 1.0939 | ±2.1878 | **-3.204** | **0.0014** | 0.0301 | ** |
| **Education: graduate level (vs college)** | **-0.6719** | 0.2518 | ±0.5036 | **-2.668** | **0.0076** | 0.5107 | ** |
| Education: high school or below (vs college) | +0.6524 | 0.4297 | ±0.8594 | +1.518 | 0.1290 | 1.9201 |  |
| Site: UCSD (vs UAB) | +0.1986 | 0.3125 | ±0.6249 | +0.636 | 0.5251 | 1.2197 |  |
| Site: UW (vs UAB) | +0.1389 | 0.2700 | ±0.5399 | +0.515 | 0.6068 | 1.1490 |  |
| **Age (years)** | **+0.0391** | 0.0110 | ±0.0221 | **+3.541** | **3.99e-04** | 1.0399 | *** |
| BMI (kg/m2) | +0.0127 | 0.0162 | ±0.0323 | +0.784 | 0.4329 | 1.0127 |  |
| Hypertension | -0.4254 | 0.2610 | ±0.5219 | -1.630 | 0.1031 | 0.6535 |  |
| High cholesterol | -0.2217 | 0.2484 | ±0.4969 | -0.892 | 0.3722 | 0.8011 |  |
| Kidney disease | +0.3448 | 0.4522 | ±0.9045 | +0.762 | 0.4458 | 1.4117 |  |
| **Circulatory disease** | **+0.6856** | 0.3060 | ±0.6120 | **+2.241** | **0.0250** | 1.9850 | * |
| MAG (mg/dL/h) | +0.0040 | 0.0140 | ±0.0279 | +0.289 | 0.7723 | 1.0040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0750**, LLR χ² = **37.45** (p = **9.70e-05**), AUC = **0.6791**, AIC = **486.0**, BIC = **534.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3587** | 0.9794 | ±1.9588 | **-3.429** | **6.05e-04** | 0.0348 | *** |
| **Education: graduate level (vs college)** | **-0.6719** | 0.2518 | ±0.5035 | **-2.669** | **0.0076** | 0.5107 | ** |
| Education: high school or below (vs college) | +0.6493 | 0.4297 | ±0.8594 | +1.511 | 0.1307 | 1.9143 |  |
| Site: UCSD (vs UAB) | +0.1999 | 0.3127 | ±0.6254 | +0.639 | 0.5226 | 1.2213 |  |
| Site: UW (vs UAB) | +0.1302 | 0.2682 | ±0.5364 | +0.485 | 0.6273 | 1.1391 |  |
| **Age (years)** | **+0.0389** | 0.0111 | ±0.0223 | **+3.492** | **4.80e-04** | 1.0396 | *** |
| BMI (kg/m2) | +0.0127 | 0.0162 | ±0.0324 | +0.784 | 0.4328 | 1.0128 |  |
| Hypertension | -0.4226 | 0.2610 | ±0.5221 | -1.619 | 0.1055 | 0.6553 |  |
| High cholesterol | -0.2286 | 0.2473 | ±0.4945 | -0.925 | 0.3551 | 0.7956 |  |
| Kidney disease | +0.3408 | 0.4557 | ±0.9114 | +0.748 | 0.4545 | 1.4061 |  |
| **Circulatory disease** | **+0.6848** | 0.3061 | ±0.6122 | **+2.237** | **0.0253** | 1.9833 | * |
| Avg. daily range (mg/dL) | +0.0003 | 0.0043 | ±0.0085 | +0.080 | 0.9363 | 1.0003 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0764**, LLR χ² = **38.18** (p = **7.29e-05**), AUC = **0.6823**, AIC = **485.3**, BIC = **533.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2040** | 0.9267 | ±1.8534 | **-3.457** | **5.45e-04** | 0.0406 | *** |
| **Education: graduate level (vs college)** | **-0.6582** | 0.2525 | ±0.5051 | **-2.606** | **0.0092** | 0.5178 | ** |
| Education: high school or below (vs college) | +0.6291 | 0.4312 | ±0.8625 | +1.459 | 0.1446 | 1.8760 |  |
| Site: UCSD (vs UAB) | +0.1963 | 0.3131 | ±0.6261 | +0.627 | 0.5306 | 1.2169 |  |
| Site: UW (vs UAB) | +0.1303 | 0.2685 | ±0.5370 | +0.485 | 0.6275 | 1.1391 |  |
| **Age (years)** | **+0.0394** | 0.0111 | ±0.0221 | **+3.564** | **3.65e-04** | 1.0402 | *** |
| BMI (kg/m2) | +0.0138 | 0.0163 | ±0.0326 | +0.846 | 0.3974 | 1.0139 |  |
| Hypertension | -0.4209 | 0.2602 | ±0.5204 | -1.618 | 0.1057 | 0.6565 |  |
| High cholesterol | -0.2278 | 0.2467 | ±0.4933 | -0.924 | 0.3557 | 0.7963 |  |
| Kidney disease | +0.3601 | 0.4547 | ±0.9093 | +0.792 | 0.4283 | 1.4335 |  |
| **Circulatory disease** | **+0.6871** | 0.3067 | ±0.6134 | **+2.240** | **0.0251** | 1.9879 | * |
| SD of daily means (mg/dL) | -0.0265 | 0.0313 | ±0.0626 | -0.846 | 0.3975 | 0.9739 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0751**, LLR χ² = **37.51** (p = **9.46e-05**), AUC = **0.6792**, AIC = **486.0**, BIC = **534.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.7547 | 2.3301 | ±4.6602 | -1.182 | 0.2371 | 0.0636 |  |
| **Education: graduate level (vs college)** | **-0.6718** | 0.2518 | ±0.5036 | **-2.668** | **0.0076** | 0.5108 | ** |
| Education: high school or below (vs college) | +0.6514 | 0.4295 | ±0.8591 | +1.517 | 0.1294 | 1.9183 |  |
| Site: UCSD (vs UAB) | +0.2052 | 0.3128 | ±0.6256 | +0.656 | 0.5118 | 1.2278 |  |
| Site: UW (vs UAB) | +0.1349 | 0.2688 | ±0.5377 | +0.502 | 0.6157 | 1.1445 |  |
| **Age (years)** | **+0.0387** | 0.0111 | ±0.0221 | **+3.502** | **4.61e-04** | 1.0395 | *** |
| BMI (kg/m2) | +0.0125 | 0.0162 | ±0.0323 | +0.775 | 0.4382 | 1.0126 |  |
| Hypertension | -0.4241 | 0.2608 | ±0.5216 | -1.626 | 0.1039 | 0.6544 |  |
| High cholesterol | -0.2283 | 0.2470 | ±0.4939 | -0.924 | 0.3552 | 0.7959 |  |
| Kidney disease | +0.3268 | 0.4577 | ±0.9154 | +0.714 | 0.4752 | 1.3866 |  |
| **Circulatory disease** | **+0.6904** | 0.3069 | ±0.6138 | **+2.250** | **0.0245** | 1.9945 | * |
| Time in range 70-180, pooled (%) | -0.0059 | 0.0218 | ±0.0437 | -0.268 | 0.7886 | 0.9942 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0750**, LLR χ² = **37.45** (p = **9.69e-05**), AUC = **0.6792**, AIC = **486.0**, BIC = **534.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -3.1402 | 2.3078 | ±4.6155 | -1.361 | 0.1736 | 0.0433 |  |
| **Education: graduate level (vs college)** | **-0.6718** | 0.2518 | ±0.5035 | **-2.668** | **0.0076** | 0.5108 | ** |
| Education: high school or below (vs college) | +0.6505 | 0.4298 | ±0.8597 | +1.513 | 0.1302 | 1.9166 |  |
| Site: UCSD (vs UAB) | +0.2021 | 0.3125 | ±0.6251 | +0.647 | 0.5179 | 1.2240 |  |
| Site: UW (vs UAB) | +0.1318 | 0.2687 | ±0.5374 | +0.491 | 0.6237 | 1.1409 |  |
| **Age (years)** | **+0.0389** | 0.0111 | ±0.0221 | **+3.512** | **4.45e-04** | 1.0396 | *** |
| BMI (kg/m2) | +0.0126 | 0.0162 | ±0.0323 | +0.778 | 0.4367 | 1.0127 |  |
| Hypertension | -0.4221 | 0.2606 | ±0.5213 | -1.619 | 0.1053 | 0.6557 |  |
| High cholesterol | -0.2296 | 0.2468 | ±0.4937 | -0.930 | 0.3523 | 0.7949 |  |
| Kidney disease | +0.3393 | 0.4572 | ±0.9144 | +0.742 | 0.4580 | 1.4039 |  |
| **Circulatory disease** | **+0.6861** | 0.3068 | ±0.6136 | **+2.236** | **0.0253** | 1.9860 | * |
| Avg. daily time in range 70-180 (%) | -0.0019 | 0.0213 | ±0.0427 | -0.090 | 0.9286 | 0.9981 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0762**, LLR χ² = **38.04** (p = **7.71e-05**), AUC = **0.6820**, AIC = **485.4**, BIC = **533.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4197** | 0.9198 | ±1.8396 | **-3.718** | **2.01e-04** | 0.0327 | *** |
| **Education: graduate level (vs college)** | **-0.6689** | 0.2520 | ±0.5040 | **-2.655** | **0.0079** | 0.5123 | ** |
| Education: high school or below (vs college) | +0.6639 | 0.4302 | ±0.8605 | +1.543 | 0.1228 | 1.9424 |  |
| Site: UCSD (vs UAB) | +0.2384 | 0.3166 | ±0.6332 | +0.753 | 0.4515 | 1.2692 |  |
| Site: UW (vs UAB) | +0.1646 | 0.2724 | ±0.5447 | +0.604 | 0.5456 | 1.1789 |  |
| **Age (years)** | **+0.0389** | 0.0110 | ±0.0221 | **+3.523** | **4.26e-04** | 1.0396 | *** |
| BMI (kg/m2) | +0.0133 | 0.0162 | ±0.0324 | +0.820 | 0.4124 | 1.0133 |  |
| Hypertension | -0.4092 | 0.2608 | ±0.5215 | -1.569 | 0.1166 | 0.6642 |  |
| High cholesterol | -0.2118 | 0.2481 | ±0.4961 | -0.854 | 0.3932 | 0.8091 |  |
| Kidney disease | +0.3353 | 0.4531 | ±0.9062 | +0.740 | 0.4593 | 1.3983 |  |
| **Circulatory disease** | **+0.6940** | 0.3063 | ±0.6125 | **+2.266** | **0.0234** | 2.0018 | * |
| Time < 54 (%) | +0.0902 | 0.1188 | ±0.2376 | +0.759 | 0.4479 | 1.0944 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0758**, LLR χ² = **37.87** (p = **8.24e-05**), AUC = **0.6815**, AIC = **485.6**, BIC = **533.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3835** | 0.9158 | ±1.8317 | **-3.694** | **2.20e-04** | 0.0339 | *** |
| **Education: graduate level (vs college)** | **-0.6659** | 0.2521 | ±0.5041 | **-2.642** | **0.0083** | 0.5138 | ** |
| Education: high school or below (vs college) | +0.6641 | 0.4302 | ±0.8603 | +1.544 | 0.1226 | 1.9427 |  |
| Site: UCSD (vs UAB) | +0.2284 | 0.3156 | ±0.6312 | +0.724 | 0.4693 | 1.2566 |  |
| Site: UW (vs UAB) | +0.1641 | 0.2736 | ±0.5473 | +0.600 | 0.5487 | 1.1784 |  |
| **Age (years)** | **+0.0386** | 0.0110 | ±0.0221 | **+3.500** | **4.66e-04** | 1.0394 | *** |
| BMI (kg/m2) | +0.0131 | 0.0162 | ±0.0323 | +0.808 | 0.4190 | 1.0131 |  |
| Hypertension | -0.4083 | 0.2612 | ±0.5224 | -1.563 | 0.1180 | 0.6648 |  |
| High cholesterol | -0.2150 | 0.2480 | ±0.4960 | -0.867 | 0.3859 | 0.8065 |  |
| Kidney disease | +0.3369 | 0.4529 | ±0.9059 | +0.744 | 0.4570 | 1.4006 |  |
| **Circulatory disease** | **+0.6934** | 0.3063 | ±0.6125 | **+2.264** | **0.0236** | 2.0005 | * |
| Avg. daily time < 54 (%) | +0.0995 | 0.1526 | ±0.3053 | +0.652 | 0.5146 | 1.1046 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0871**, LLR χ² = **43.50** (p = **8.90e-06**), AUC = **0.6835**, AIC = **480.0**, BIC = **528.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.6203** | 0.9280 | ±1.8559 | **-3.901** | **9.57e-05** | 0.0268 | *** |
| **Education: graduate level (vs college)** | **-0.6659** | 0.2541 | ±0.5082 | **-2.621** | **0.0088** | 0.5138 | ** |
| Education: high school or below (vs college) | +0.7285 | 0.4333 | ±0.8666 | +1.681 | 0.0927 | 2.0720 | . |
| Site: UCSD (vs UAB) | +0.2691 | 0.3170 | ±0.6339 | +0.849 | 0.3959 | 1.3088 |  |
| Site: UW (vs UAB) | +0.2316 | 0.2744 | ±0.5488 | +0.844 | 0.3987 | 1.2606 |  |
| **Age (years)** | **+0.0397** | 0.0111 | ±0.0222 | **+3.576** | **3.49e-04** | 1.0405 | *** |
| BMI (kg/m2) | +0.0108 | 0.0163 | ±0.0326 | +0.662 | 0.5079 | 1.0109 |  |
| Hypertension | -0.3761 | 0.2628 | ±0.5257 | -1.431 | 0.1524 | 0.6865 |  |
| High cholesterol | -0.1902 | 0.2495 | ±0.4991 | -0.762 | 0.4460 | 0.8268 |  |
| Kidney disease | +0.3552 | 0.4556 | ±0.9111 | +0.780 | 0.4355 | 1.4265 |  |
| **Circulatory disease** | **+0.7237** | 0.3075 | ±0.6150 | **+2.353** | **0.0186** | 2.0619 | * |
| **Time 54-69, pooled (%)** | **+0.1264** | 0.0513 | ±0.1026 | **+2.463** | **0.0138** | 1.1347 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0859**, LLR χ² = **42.93** (p = **1.12e-05**), AUC = **0.6841**, AIC = **480.6**, BIC = **528.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.5538** | 0.9240 | ±1.8479 | **-3.846** | **1.20e-04** | 0.0286 | *** |
| **Education: graduate level (vs college)** | **-0.6593** | 0.2538 | ±0.5076 | **-2.598** | **0.0094** | 0.5172 | ** |
| Education: high school or below (vs college) | +0.7388 | 0.4329 | ±0.8658 | +1.707 | 0.0879 | 2.0933 | . |
| Site: UCSD (vs UAB) | +0.2515 | 0.3162 | ±0.6324 | +0.795 | 0.4264 | 1.2859 |  |
| Site: UW (vs UAB) | +0.2290 | 0.2742 | ±0.5484 | +0.835 | 0.4036 | 1.2574 |  |
| **Age (years)** | **+0.0392** | 0.0111 | ±0.0222 | **+3.539** | **4.01e-04** | 1.0400 | *** |
| BMI (kg/m2) | +0.0109 | 0.0163 | ±0.0326 | +0.668 | 0.5042 | 1.0109 |  |
| Hypertension | -0.3763 | 0.2628 | ±0.5256 | -1.432 | 0.1522 | 0.6864 |  |
| High cholesterol | -0.1933 | 0.2492 | ±0.4984 | -0.776 | 0.4379 | 0.8242 |  |
| Kidney disease | +0.3614 | 0.4545 | ±0.9090 | +0.795 | 0.4264 | 1.4354 |  |
| **Circulatory disease** | **+0.7152** | 0.3071 | ±0.6141 | **+2.329** | **0.0199** | 2.0445 | * |
| **Avg. daily time 54-69 (%)** | **+0.1168** | 0.0498 | ±0.0997 | **+2.344** | **0.0191** | 1.1239 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0849**, LLR χ² = **42.41** (p = **1.37e-05**), AUC = **0.6861**, AIC = **481.1**, BIC = **529.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.6300** | 0.9292 | ±1.8584 | **-3.907** | **9.36e-05** | 0.0265 | *** |
| **Education: graduate level (vs college)** | **-0.6644** | 0.2537 | ±0.5074 | **-2.619** | **0.0088** | 0.5146 | ** |
| Education: high school or below (vs college) | +0.7216 | 0.4327 | ±0.8654 | +1.668 | 0.0954 | 2.0576 | . |
| Site: UCSD (vs UAB) | +0.2892 | 0.3180 | ±0.6359 | +0.910 | 0.3631 | 1.3354 |  |
| Site: UW (vs UAB) | +0.2392 | 0.2754 | ±0.5509 | +0.869 | 0.3851 | 1.2703 |  |
| **Age (years)** | **+0.0394** | 0.0111 | ±0.0222 | **+3.554** | **3.80e-04** | 1.0402 | *** |
| BMI (kg/m2) | +0.0119 | 0.0163 | ±0.0325 | +0.732 | 0.4642 | 1.0120 |  |
| Hypertension | -0.3754 | 0.2624 | ±0.5249 | -1.431 | 0.1526 | 0.6870 |  |
| High cholesterol | -0.1832 | 0.2494 | ±0.4988 | -0.735 | 0.4626 | 0.8326 |  |
| Kidney disease | +0.3416 | 0.4561 | ±0.9121 | +0.749 | 0.4539 | 1.4072 |  |
| **Circulatory disease** | **+0.7228** | 0.3072 | ±0.6144 | **+2.353** | **0.0186** | 2.0602 | * |
| **Time < 70 (%)** | **+0.0910** | 0.0406 | ±0.0811 | **+2.244** | **0.0248** | 1.0953 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0840**, LLR χ² = **41.94** (p = **1.66e-05**), AUC = **0.6850**, AIC = **481.5**, BIC = **529.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.5462** | 0.9238 | ±1.8475 | **-3.839** | **1.24e-04** | 0.0288 | *** |
| **Education: graduate level (vs college)** | **-0.6565** | 0.2535 | ±0.5069 | **-2.590** | **0.0096** | 0.5187 | ** |
| Education: high school or below (vs college) | +0.7301 | 0.4323 | ±0.8647 | +1.689 | 0.0913 | 2.0752 | . |
| Site: UCSD (vs UAB) | +0.2642 | 0.3166 | ±0.6332 | +0.835 | 0.4040 | 1.3024 |  |
| Site: UW (vs UAB) | +0.2356 | 0.2752 | ±0.5504 | +0.856 | 0.3920 | 1.2656 |  |
| **Age (years)** | **+0.0389** | 0.0111 | ±0.0221 | **+3.511** | **4.46e-04** | 1.0396 | *** |
| BMI (kg/m2) | +0.0117 | 0.0162 | ±0.0325 | +0.719 | 0.4723 | 1.0117 |  |
| Hypertension | -0.3755 | 0.2626 | ±0.5252 | -1.430 | 0.1528 | 0.6870 |  |
| High cholesterol | -0.1891 | 0.2491 | ±0.4982 | -0.759 | 0.4478 | 0.8277 |  |
| Kidney disease | +0.3499 | 0.4544 | ±0.9088 | +0.770 | 0.4413 | 1.4190 |  |
| **Circulatory disease** | **+0.7157** | 0.3069 | ±0.6137 | **+2.332** | **0.0197** | 2.0456 | * |
| **Avg. daily time < 70 (%)** | **+0.0876** | 0.0410 | ±0.0820 | **+2.137** | **0.0326** | 1.0916 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0750**, LLR χ² = **37.46** (p = **9.66e-05**), AUC = **0.6796**, AIC = **486.0**, BIC = **534.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.1695 | 9.0616 | ±18.1232 | -0.239 | 0.8108 | 0.1142 |  |
| **Education: graduate level (vs college)** | **-0.6713** | 0.2518 | ±0.5036 | **-2.666** | **0.0077** | 0.5110 | ** |
| Education: high school or below (vs college) | +0.6517 | 0.4300 | ±0.8601 | +1.515 | 0.1297 | 1.9187 |  |
| Site: UCSD (vs UAB) | +0.2058 | 0.3145 | ±0.6290 | +0.654 | 0.5129 | 1.2285 |  |
| Site: UW (vs UAB) | +0.1353 | 0.2709 | ±0.5418 | +0.499 | 0.6175 | 1.1448 |  |
| **Age (years)** | **+0.0389** | 0.0110 | ±0.0221 | **+3.522** | **4.29e-04** | 1.0397 | *** |
| BMI (kg/m2) | +0.0127 | 0.0162 | ±0.0323 | +0.786 | 0.4318 | 1.0128 |  |
| Hypertension | -0.4204 | 0.2604 | ±0.5209 | -1.614 | 0.1065 | 0.6568 |  |
| High cholesterol | -0.2266 | 0.2481 | ±0.4962 | -0.913 | 0.3610 | 0.7972 |  |
| Kidney disease | +0.3376 | 0.4563 | ±0.9126 | +0.740 | 0.4594 | 1.4016 |  |
| **Circulatory disease** | **+0.6866** | 0.3066 | ±0.6132 | **+2.239** | **0.0251** | 1.9870 | * |
| Time 54-250, pooled (%) | -0.0117 | 0.0909 | ±0.1818 | -0.129 | 0.8976 | 0.9884 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0753**, LLR χ² = **37.63** (p = **9.03e-05**), AUC = **0.6791**, AIC = **485.8**, BIC = **534.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -8.0718 | 11.1149 | ±22.2298 | -0.726 | 0.4677 | 0.0003 |  |
| **Education: graduate level (vs college)** | **-0.6752** | 0.2520 | ±0.5040 | **-2.679** | **0.0074** | 0.5091 | ** |
| Education: high school or below (vs college) | +0.6419 | 0.4307 | ±0.8615 | +1.490 | 0.1362 | 1.9001 |  |
| Site: UCSD (vs UAB) | +0.1887 | 0.3135 | ±0.6271 | +0.602 | 0.5472 | 1.2077 |  |
| Site: UW (vs UAB) | +0.1143 | 0.2706 | ±0.5412 | +0.422 | 0.6729 | 1.1210 |  |
| **Age (years)** | **+0.0394** | 0.0111 | ±0.0222 | **+3.555** | **3.77e-04** | 1.0402 | *** |
| BMI (kg/m2) | +0.0125 | 0.0162 | ±0.0324 | +0.773 | 0.4396 | 1.0126 |  |
| Hypertension | -0.4244 | 0.2602 | ±0.5205 | -1.631 | 0.1029 | 0.6541 |  |
| High cholesterol | -0.2393 | 0.2477 | ±0.4955 | -0.966 | 0.3340 | 0.7871 |  |
| Kidney disease | +0.3748 | 0.4570 | ±0.9140 | +0.820 | 0.4122 | 1.4546 |  |
| **Circulatory disease** | **+0.6753** | 0.3068 | ±0.6137 | **+2.201** | **0.0277** | 1.9647 | * |
| Avg. daily time 54-250 (%) | +0.0475 | 0.1111 | ±0.2221 | +0.428 | 0.6685 | 1.0487 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0771**, LLR χ² = **38.53** (p = **6.38e-05**), AUC = **0.6834**, AIC = **485.0**, BIC = **533.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3629** | 0.9158 | ±1.8316 | **-3.672** | **2.41e-04** | 0.0346 | *** |
| **Education: graduate level (vs college)** | **-0.6682** | 0.2522 | ±0.5045 | **-2.649** | **0.0081** | 0.5126 | ** |
| Education: high school or below (vs college) | +0.6639 | 0.4328 | ±0.8655 | +1.534 | 0.1250 | 1.9424 |  |
| Site: UCSD (vs UAB) | +0.2103 | 0.3131 | ±0.6262 | +0.672 | 0.5018 | 1.2340 |  |
| Site: UW (vs UAB) | +0.1468 | 0.2692 | ±0.5383 | +0.545 | 0.5855 | 1.1581 |  |
| **Age (years)** | **+0.0401** | 0.0111 | ±0.0223 | **+3.604** | **3.14e-04** | 1.0409 | *** |
| BMI (kg/m2) | +0.0128 | 0.0162 | ±0.0323 | +0.793 | 0.4276 | 1.0129 |  |
| Hypertension | -0.3947 | 0.2608 | ±0.5216 | -1.514 | 0.1301 | 0.6739 |  |
| High cholesterol | -0.2229 | 0.2469 | ±0.4938 | -0.903 | 0.3666 | 0.8002 |  |
| Kidney disease | +0.4154 | 0.4585 | ±0.9169 | +0.906 | 0.3649 | 1.5149 |  |
| **Circulatory disease** | **+0.6712** | 0.3070 | ±0.6140 | **+2.187** | **0.0288** | 1.9567 | * |
| Time 181-250, pooled (%) | -0.0317 | 0.0321 | ±0.0641 | -0.989 | 0.3227 | 0.9688 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0771**, LLR χ² = **38.53** (p = **6.37e-05**), AUC = **0.6832**, AIC = **485.0**, BIC = **533.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3661** | 0.9161 | ±1.8321 | **-3.675** | **2.38e-04** | 0.0345 | *** |
| **Education: graduate level (vs college)** | **-0.6672** | 0.2523 | ±0.5045 | **-2.645** | **0.0082** | 0.5131 | ** |
| Education: high school or below (vs college) | +0.6620 | 0.4327 | ±0.8653 | +1.530 | 0.1260 | 1.9386 |  |
| Site: UCSD (vs UAB) | +0.2087 | 0.3130 | ±0.6261 | +0.667 | 0.5050 | 1.2321 |  |
| Site: UW (vs UAB) | +0.1469 | 0.2692 | ±0.5384 | +0.546 | 0.5852 | 1.1583 |  |
| **Age (years)** | **+0.0400** | 0.0111 | ±0.0222 | **+3.600** | **3.18e-04** | 1.0408 | *** |
| BMI (kg/m2) | +0.0130 | 0.0162 | ±0.0323 | +0.802 | 0.4224 | 1.0130 |  |
| Hypertension | -0.3942 | 0.2608 | ±0.5217 | -1.511 | 0.1307 | 0.6742 |  |
| High cholesterol | -0.2220 | 0.2469 | ±0.4938 | -0.899 | 0.3686 | 0.8009 |  |
| Kidney disease | +0.4125 | 0.4581 | ±0.9162 | +0.900 | 0.3679 | 1.5106 |  |
| **Circulatory disease** | **+0.6711** | 0.3069 | ±0.6139 | **+2.187** | **0.0288** | 1.9565 | * |
| Avg. daily time 181-250 (%) | -0.0307 | 0.0312 | ±0.0623 | -0.985 | 0.3247 | 0.9698 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0772**, LLR χ² = **38.56** (p = **6.29e-05**), AUC = **0.6832**, AIC = **484.9**, BIC = **533.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3632** | 0.9159 | ±1.8318 | **-3.672** | **2.41e-04** | 0.0346 | *** |
| **Education: graduate level (vs college)** | **-0.6692** | 0.2522 | ±0.5045 | **-2.653** | **0.0080** | 0.5121 | ** |
| Education: high school or below (vs college) | +0.6620 | 0.4327 | ±0.8653 | +1.530 | 0.1260 | 1.9387 |  |
| Site: UCSD (vs UAB) | +0.2105 | 0.3132 | ±0.6263 | +0.672 | 0.5015 | 1.2343 |  |
| Site: UW (vs UAB) | +0.1447 | 0.2691 | ±0.5381 | +0.538 | 0.5906 | 1.1557 |  |
| **Age (years)** | **+0.0401** | 0.0111 | ±0.0223 | **+3.606** | **3.11e-04** | 1.0410 | *** |
| BMI (kg/m2) | +0.0128 | 0.0162 | ±0.0323 | +0.791 | 0.4289 | 1.0129 |  |
| Hypertension | -0.3953 | 0.2607 | ±0.5214 | -1.516 | 0.1294 | 0.6735 |  |
| High cholesterol | -0.2262 | 0.2469 | ±0.4937 | -0.916 | 0.3596 | 0.7976 |  |
| Kidney disease | +0.4211 | 0.4588 | ±0.9177 | +0.918 | 0.3588 | 1.5236 |  |
| **Circulatory disease** | **+0.6704** | 0.3070 | ±0.6139 | **+2.184** | **0.0290** | 1.9551 | * |
| Time > 180 (%) | -0.0288 | 0.0289 | ±0.0577 | -0.998 | 0.3183 | 0.9716 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0775**, LLR χ² = **38.73** (p = **5.90e-05**), AUC = **0.6835**, AIC = **484.8**, BIC = **532.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3698** | 0.9165 | ±1.8330 | **-3.677** | **2.36e-04** | 0.0344 | *** |
| **Education: graduate level (vs college)** | **-0.6684** | 0.2523 | ±0.5046 | **-2.649** | **0.0081** | 0.5125 | ** |
| Education: high school or below (vs college) | +0.6607 | 0.4328 | ±0.8656 | +1.527 | 0.1268 | 1.9362 |  |
| Site: UCSD (vs UAB) | +0.2095 | 0.3132 | ±0.6263 | +0.669 | 0.5035 | 1.2331 |  |
| Site: UW (vs UAB) | +0.1466 | 0.2692 | ±0.5384 | +0.544 | 0.5861 | 1.1579 |  |
| **Age (years)** | **+0.0402** | 0.0111 | ±0.0223 | **+3.608** | **3.08e-04** | 1.0410 | *** |
| BMI (kg/m2) | +0.0130 | 0.0162 | ±0.0323 | +0.802 | 0.4225 | 1.0130 |  |
| Hypertension | -0.3933 | 0.2607 | ±0.5214 | -1.509 | 0.1314 | 0.6748 |  |
| High cholesterol | -0.2246 | 0.2469 | ±0.4938 | -0.910 | 0.3629 | 0.7988 |  |
| Kidney disease | +0.4227 | 0.4586 | ±0.9172 | +0.922 | 0.3567 | 1.5260 |  |
| **Circulatory disease** | **+0.6696** | 0.3070 | ±0.6141 | **+2.181** | **0.0292** | 1.9535 | * |
| Avg. daily time > 180 (%) | -0.0301 | 0.0285 | ±0.0571 | -1.054 | 0.2917 | 0.9703 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0783**, LLR χ² = **39.09** (p = **5.11e-05**), AUC = **0.6842**, AIC = **484.4**, BIC = **532.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3934** | 0.9179 | ±1.8359 | **-3.697** | **2.18e-04** | 0.0336 | *** |
| **Education: graduate level (vs college)** | **-0.6842** | 0.2523 | ±0.5045 | **-2.712** | **0.0067** | 0.5045 | ** |
| Education: high school or below (vs college) | +0.6768 | 0.4342 | ±0.8684 | +1.559 | 0.1191 | 1.9675 |  |
| Site: UCSD (vs UAB) | +0.2065 | 0.3130 | ±0.6261 | +0.660 | 0.5095 | 1.2294 |  |
| Site: UW (vs UAB) | +0.1380 | 0.2689 | ±0.5378 | +0.513 | 0.6078 | 1.1480 |  |
| **Age (years)** | **+0.0398** | 0.0111 | ±0.0222 | **+3.589** | **3.32e-04** | 1.0406 | *** |
| BMI (kg/m2) | +0.0143 | 0.0162 | ±0.0325 | +0.883 | 0.3773 | 1.0144 |  |
| Hypertension | -0.3913 | 0.2605 | ±0.5210 | -1.502 | 0.1331 | 0.6762 |  |
| High cholesterol | -0.2364 | 0.2471 | ±0.4941 | -0.957 | 0.3387 | 0.7895 |  |
| Kidney disease | +0.3455 | 0.4533 | ±0.9066 | +0.762 | 0.4460 | 1.4127 |  |
| **Circulatory disease** | **+0.6486** | 0.3078 | ±0.6155 | **+2.108** | **0.0351** | 1.9129 | * |
| Nocturnal time > 180 (%) | -0.0387 | 0.0337 | ±0.0674 | -1.149 | 0.2504 | 0.9620 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0766**, LLR χ² = **38.26** (p = **7.08e-05**), AUC = **0.6828**, AIC = **485.2**, BIC = **533.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3199** | 0.9132 | ±1.8264 | **-3.635** | **2.77e-04** | 0.0362 | *** |
| **Education: graduate level (vs college)** | **-0.6821** | 0.2523 | ±0.5045 | **-2.704** | **0.0069** | 0.5055 | ** |
| Education: high school or below (vs college) | +0.6446 | 0.4321 | ±0.8641 | +1.492 | 0.1357 | 1.9053 |  |
| Site: UCSD (vs UAB) | +0.2146 | 0.3133 | ±0.6265 | +0.685 | 0.4933 | 1.2394 |  |
| Site: UW (vs UAB) | +0.1285 | 0.2683 | ±0.5367 | +0.479 | 0.6320 | 1.1371 |  |
| **Age (years)** | **+0.0398** | 0.0111 | ±0.0222 | **+3.584** | **3.39e-04** | 1.0406 | *** |
| BMI (kg/m2) | +0.0120 | 0.0162 | ±0.0323 | +0.742 | 0.4581 | 1.0121 |  |
| Hypertension | -0.4037 | 0.2605 | ±0.5211 | -1.550 | 0.1212 | 0.6678 |  |
| High cholesterol | -0.2328 | 0.2469 | ±0.4937 | -0.943 | 0.3456 | 0.7923 |  |
| Kidney disease | +0.3763 | 0.4536 | ±0.9072 | +0.830 | 0.4068 | 1.4569 |  |
| **Circulatory disease** | **+0.6732** | 0.3070 | ±0.6140 | **+2.193** | **0.0283** | 1.9606 | * |
| Any reading > 250 during wear (0/1) | -0.2824 | 0.3161 | ±0.6321 | -0.893 | 0.3717 | 0.7540 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0766**, LLR χ² = **38.24** (p = **7.13e-05**), AUC = **0.6822**, AIC = **485.2**, BIC = **533.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3471** | 0.9143 | ±1.8287 | **-3.661** | **2.51e-04** | 0.0352 | *** |
| **Education: graduate level (vs college)** | **-0.6754** | 0.2522 | ±0.5043 | **-2.678** | **0.0074** | 0.5090 | ** |
| Education: high school or below (vs college) | +0.6466 | 0.4312 | ±0.8624 | +1.500 | 0.1337 | 1.9090 |  |
| Site: UCSD (vs UAB) | +0.2051 | 0.3129 | ±0.6259 | +0.655 | 0.5123 | 1.2276 |  |
| Site: UW (vs UAB) | +0.1265 | 0.2685 | ±0.5370 | +0.471 | 0.6375 | 1.1349 |  |
| **Age (years)** | **+0.0397** | 0.0111 | ±0.0222 | **+3.584** | **3.39e-04** | 1.0405 | *** |
| BMI (kg/m2) | +0.0125 | 0.0162 | ±0.0324 | +0.771 | 0.4405 | 1.0126 |  |
| Hypertension | -0.4111 | 0.2601 | ±0.5201 | -1.581 | 0.1139 | 0.6629 |  |
| High cholesterol | -0.2441 | 0.2476 | ±0.4951 | -0.986 | 0.3241 | 0.7834 |  |
| Kidney disease | +0.4191 | 0.4589 | ±0.9179 | +0.913 | 0.3611 | 1.5206 |  |
| **Circulatory disease** | **+0.6723** | 0.3066 | ±0.6132 | **+2.193** | **0.0283** | 1.9587 | * |
| Time > 250 (%) | -0.1643 | 0.1991 | ±0.3981 | -0.825 | 0.4092 | 0.8485 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 408)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **408**, events = **123**, McFadden pseudo-R² = **0.0790**, LLR χ² = **39.47** (p = **4.40e-05**), AUC = **0.6850**, AIC = **484.0**, BIC = **532.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3558** | 0.9163 | ±1.8326 | **-3.662** | **2.50e-04** | 0.0349 | *** |
| **Education: graduate level (vs college)** | **-0.6837** | 0.2528 | ±0.5056 | **-2.704** | **0.0068** | 0.5047 | ** |
| Education: high school or below (vs college) | +0.6396 | 0.4321 | ±0.8642 | +1.480 | 0.1388 | 1.8958 |  |
| Site: UCSD (vs UAB) | +0.2056 | 0.3136 | ±0.6272 | +0.656 | 0.5120 | 1.2283 |  |
| Site: UW (vs UAB) | +0.1288 | 0.2688 | ±0.5376 | +0.479 | 0.6318 | 1.1375 |  |
| **Age (years)** | **+0.0402** | 0.0111 | ±0.0222 | **+3.618** | **2.97e-04** | 1.0410 | *** |
| BMI (kg/m2) | +0.0124 | 0.0162 | ±0.0324 | +0.766 | 0.4436 | 1.0125 |  |
| Hypertension | -0.4087 | 0.2599 | ±0.5197 | -1.573 | 0.1158 | 0.6645 |  |
| High cholesterol | -0.2517 | 0.2479 | ±0.4957 | -1.015 | 0.3100 | 0.7775 |  |
| Kidney disease | +0.4538 | 0.4592 | ±0.9185 | +0.988 | 0.3230 | 1.5743 |  |
| **Circulatory disease** | **+0.6684** | 0.3070 | ±0.6140 | **+2.177** | **0.0295** | 1.9510 | * |
| Avg. daily time > 250 (%) | -0.2924 | 0.2450 | ±0.4899 | -1.194 | 0.2326 | 0.7465 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 408; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **408**, R² = **0.0923**, Adj R² = **0.0694**, F-statistic = **4.04** (p = **2.74e-05**), Residual SE = **2.421** on **397** df, AIC = **1890.0**, BIC = **1934.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.3031** | 0.9918 | ±1.9836 | **+15.430** | **1.04e-53** | *** |
| Education: graduate level (vs college) | +0.4788 | 0.2699 | ±0.5398 | +1.774 | 0.0761 | . |
| Education: high school or below (vs college) | -0.4744 | 0.5672 | ±1.1343 | -0.836 | 0.4029 |  |
| Site: UCSD (vs UAB) | +0.2619 | 0.3472 | ±0.6945 | +0.754 | 0.4507 |  |
| Site: UW (vs UAB) | +0.1451 | 0.2972 | ±0.5944 | +0.488 | 0.6253 |  |
| **Age (years)** | **-0.0435** | 0.0124 | ±0.0249 | **-3.498** | **4.69e-04** | *** |
| BMI (kg/m2) | +0.0026 | 0.0160 | ±0.0321 | +0.161 | 0.8717 |  |
| Hypertension | -0.4629 | 0.2783 | ±0.5567 | -1.663 | 0.0963 | . |
| **High cholesterol** | **+0.5675** | 0.2746 | ±0.5492 | **+2.067** | **0.0388** | * |
| **Kidney disease** | **-1.4763** | 0.6887 | ±1.3775 | **-2.143** | **0.0321** | * |
| Circulatory disease | -0.0627 | 0.3805 | ±0.7610 | -0.165 | 0.8692 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **408**, R² = **0.0923**, Adj R² = **0.0670**, F-statistic = **3.66** (p = **5.81e-05**), Residual SE = **2.424** on **396** df, AIC = **1892.0**, BIC = **1940.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.3138** | 1.6552 | ±3.3105 | **+9.252** | **2.21e-20** | *** |
| Education: graduate level (vs college) | +0.4787 | 0.2715 | ±0.5430 | +1.763 | 0.0779 | . |
| Education: high school or below (vs college) | -0.4742 | 0.5676 | ±1.1352 | -0.835 | 0.4035 |  |
| Site: UCSD (vs UAB) | +0.2622 | 0.3558 | ±0.7116 | +0.737 | 0.4611 |  |
| Site: UW (vs UAB) | +0.1452 | 0.2984 | ±0.5968 | +0.487 | 0.6265 |  |
| **Age (years)** | **-0.0435** | 0.0126 | ±0.0251 | **-3.461** | **5.38e-04** | *** |
| BMI (kg/m2) | +0.0026 | 0.0161 | ±0.0322 | +0.162 | 0.8713 |  |
| Hypertension | -0.4629 | 0.2791 | ±0.5581 | -1.659 | 0.0972 | . |
| **High cholesterol** | **+0.5678** | 0.2746 | ±0.5492 | **+2.068** | **0.0386** | * |
| **Kidney disease** | **-1.4762** | 0.6909 | ±1.3818 | **-2.137** | **0.0326** | * |
| Circulatory disease | -0.0628 | 0.3818 | ±0.7637 | -0.164 | 0.8694 |  |
| HbA1c (%) | -0.0022 | 0.2610 | ±0.5220 | -0.008 | 0.9933 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **408**, R² = **0.0923**, Adj R² = **0.0671**, F-statistic = **3.66** (p = **5.80e-05**), Residual SE = **2.424** on **396** df, AIC = **1892.0**, BIC = **1940.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.2432** | 1.2759 | ±2.5518 | **+11.947** | **6.75e-33** | *** |
| Education: graduate level (vs college) | +0.4779 | 0.2713 | ±0.5427 | +1.761 | 0.0782 | . |
| Education: high school or below (vs college) | -0.4768 | 0.5664 | ±1.1327 | -0.842 | 0.3998 |  |
| Site: UCSD (vs UAB) | +0.2613 | 0.3496 | ±0.6992 | +0.747 | 0.4548 |  |
| Site: UW (vs UAB) | +0.1431 | 0.2998 | ±0.5996 | +0.477 | 0.6332 |  |
| **Age (years)** | **-0.0436** | 0.0125 | ±0.0249 | **-3.492** | **4.79e-04** | *** |
| BMI (kg/m2) | +0.0025 | 0.0162 | ±0.0325 | +0.156 | 0.8763 |  |
| Hypertension | -0.4644 | 0.2813 | ±0.5626 | -1.651 | 0.0987 | . |
| **High cholesterol** | **+0.5658** | 0.2745 | ±0.5490 | **+2.061** | **0.0393** | * |
| **Kidney disease** | **-1.4799** | 0.7011 | ±1.4021 | **-2.111** | **0.0348** | * |
| Circulatory disease | -0.0622 | 0.3804 | ±0.7608 | -0.164 | 0.8701 |  |
| Mean glucose (mg/dL) | +0.0006 | 0.0087 | ±0.0175 | +0.068 | 0.9460 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **408**, R² = **0.0923**, Adj R² = **0.0671**, F-statistic = **3.66** (p = **5.80e-05**), Residual SE = **2.424** on **396** df, AIC = **1892.0**, BIC = **1940.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.1613** | 2.2438 | ±4.4877 | **+6.757** | **1.41e-11** | *** |
| Education: graduate level (vs college) | +0.4779 | 0.2713 | ±0.5427 | +1.761 | 0.0782 | . |
| Education: high school or below (vs college) | -0.4768 | 0.5664 | ±1.1327 | -0.842 | 0.3998 |  |
| Site: UCSD (vs UAB) | +0.2613 | 0.3496 | ±0.6992 | +0.747 | 0.4548 |  |
| Site: UW (vs UAB) | +0.1431 | 0.2998 | ±0.5996 | +0.477 | 0.6332 |  |
| **Age (years)** | **-0.0436** | 0.0125 | ±0.0249 | **-3.492** | **4.79e-04** | *** |
| BMI (kg/m2) | +0.0025 | 0.0162 | ±0.0325 | +0.156 | 0.8763 |  |
| Hypertension | -0.4644 | 0.2813 | ±0.5626 | -1.651 | 0.0987 | . |
| **High cholesterol** | **+0.5658** | 0.2745 | ±0.5490 | **+2.061** | **0.0393** | * |
| **Kidney disease** | **-1.4799** | 0.7011 | ±1.4021 | **-2.111** | **0.0348** | * |
| Circulatory disease | -0.0622 | 0.3804 | ±0.7608 | -0.164 | 0.8701 |  |
| GMI (%) | +0.0247 | 0.3655 | ±0.7310 | +0.068 | 0.9460 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **408**, R² = **0.0924**, Adj R² = **0.0672**, F-statistic = **3.67** (p = **5.64e-05**), Residual SE = **2.423** on **396** df, AIC = **1892.0**, BIC = **1940.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.5265** | 1.1695 | ±2.3389 | **+13.277** | **3.17e-40** | *** |
| Education: graduate level (vs college) | +0.4811 | 0.2711 | ±0.5421 | +1.775 | 0.0759 | . |
| Education: high school or below (vs college) | -0.4624 | 0.5641 | ±1.1281 | -0.820 | 0.4123 |  |
| Site: UCSD (vs UAB) | +0.2660 | 0.3507 | ±0.7014 | +0.758 | 0.4482 |  |
| Site: UW (vs UAB) | +0.1515 | 0.2995 | ±0.5991 | +0.506 | 0.6130 |  |
| **Age (years)** | **-0.0436** | 0.0125 | ±0.0249 | **-3.494** | **4.76e-04** | *** |
| BMI (kg/m2) | +0.0033 | 0.0167 | ±0.0334 | +0.198 | 0.8427 |  |
| Hypertension | -0.4569 | 0.2819 | ±0.5639 | -1.621 | 0.1051 |  |
| **High cholesterol** | **+0.5762** | 0.2757 | ±0.5514 | **+2.090** | **0.0366** | * |
| **Kidney disease** | **-1.4729** | 0.6927 | ±1.3854 | **-2.126** | **0.0335** | * |
| Circulatory disease | -0.0671 | 0.3797 | ±0.7593 | -0.177 | 0.8597 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0022 | 0.0079 | ±0.0159 | -0.281 | 0.7790 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **408**, R² = **0.0941**, Adj R² = **0.0690**, F-statistic = **3.74** (p = **4.20e-05**), Residual SE = **2.421** on **396** df, AIC = **1891.2**, BIC = **1939.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.0426** | 1.0490 | ±2.0981 | **+14.339** | **1.24e-46** | *** |
| Education: graduate level (vs college) | +0.4697 | 0.2699 | ±0.5399 | +1.740 | 0.0819 | . |
| Education: high school or below (vs college) | -0.4774 | 0.5692 | ±1.1385 | -0.839 | 0.4017 |  |
| Site: UCSD (vs UAB) | +0.2446 | 0.3507 | ±0.7013 | +0.698 | 0.4854 |  |
| Site: UW (vs UAB) | +0.1364 | 0.2985 | ±0.5970 | +0.457 | 0.6478 |  |
| **Age (years)** | **-0.0451** | 0.0125 | ±0.0250 | **-3.609** | **3.08e-04** | *** |
| BMI (kg/m2) | +0.0021 | 0.0160 | ±0.0321 | +0.131 | 0.8961 |  |
| Hypertension | -0.4772 | 0.2795 | ±0.5589 | -1.707 | 0.0877 | . |
| **High cholesterol** | **+0.5764** | 0.2749 | ±0.5497 | **+2.097** | **0.0360** | * |
| **Kidney disease** | **-1.5477** | 0.7032 | ±1.4064 | **-2.201** | **0.0277** | * |
| Circulatory disease | -0.0582 | 0.3790 | ±0.7580 | -0.153 | 0.8780 |  |
| Glucose SD, pooled (mg/dL) | +0.0175 | 0.0186 | ±0.0371 | +0.941 | 0.3465 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **408**, R² = **0.0933**, Adj R² = **0.0681**, F-statistic = **3.70** (p = **4.89e-05**), Residual SE = **2.422** on **396** df, AIC = **1891.6**, BIC = **1939.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.1322** | 1.0402 | ±2.0803 | **+14.548** | **6.01e-48** | *** |
| Education: graduate level (vs college) | +0.4744 | 0.2701 | ±0.5402 | +1.757 | 0.0790 | . |
| Education: high school or below (vs college) | -0.4815 | 0.5691 | ±1.1382 | -0.846 | 0.3976 |  |
| Site: UCSD (vs UAB) | +0.2465 | 0.3518 | ±0.7036 | +0.701 | 0.4835 |  |
| Site: UW (vs UAB) | +0.1364 | 0.2986 | ±0.5973 | +0.457 | 0.6478 |  |
| **Age (years)** | **-0.0448** | 0.0125 | ±0.0250 | **-3.589** | **3.32e-04** | *** |
| BMI (kg/m2) | +0.0021 | 0.0161 | ±0.0321 | +0.133 | 0.8942 |  |
| Hypertension | -0.4719 | 0.2793 | ±0.5585 | -1.690 | 0.0911 | . |
| **High cholesterol** | **+0.5717** | 0.2750 | ±0.5501 | **+2.078** | **0.0377** | * |
| **Kidney disease** | **-1.5320** | 0.7058 | ±1.4115 | **-2.171** | **0.0300** | * |
| Circulatory disease | -0.0580 | 0.3791 | ±0.7582 | -0.153 | 0.8784 |  |
| Avg. daily SD (mg/dL) | +0.0139 | 0.0201 | ±0.0402 | +0.693 | 0.4885 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **408**, R² = **0.0946**, Adj R² = **0.0694**, F-statistic = **3.76** (p = **3.91e-05**), Residual SE = **2.421** on **396** df, AIC = **1891.0**, BIC = **1939.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.8912** | 1.1014 | ±2.2029 | **+13.520** | **1.19e-41** | *** |
| Education: graduate level (vs college) | +0.4745 | 0.2696 | ±0.5392 | +1.760 | 0.0784 | . |
| Education: high school or below (vs college) | -0.4607 | 0.5697 | ±1.1395 | -0.809 | 0.4188 |  |
| Site: UCSD (vs UAB) | +0.2451 | 0.3491 | ±0.6983 | +0.702 | 0.4827 |  |
| Site: UW (vs UAB) | +0.1514 | 0.2984 | ±0.5968 | +0.507 | 0.6120 |  |
| **Age (years)** | **-0.0452** | 0.0124 | ±0.0249 | **-3.628** | **2.86e-04** | *** |
| BMI (kg/m2) | +0.0024 | 0.0160 | ±0.0321 | +0.150 | 0.8809 |  |
| Hypertension | -0.4689 | 0.2790 | ±0.5579 | -1.681 | 0.0928 | . |
| **High cholesterol** | **+0.5924** | 0.2759 | ±0.5518 | **+2.147** | **0.0318** | * |
| **Kidney disease** | **-1.5386** | 0.6949 | ±1.3898 | **-2.214** | **0.0268** | * |
| Circulatory disease | -0.0596 | 0.3797 | ±0.7595 | -0.157 | 0.8753 |  |
| CV (%) | +0.0268 | 0.0234 | ±0.0468 | +1.145 | 0.2523 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **408**, R² = **0.0929**, Adj R² = **0.0677**, F-statistic = **3.69** (p = **5.17e-05**), Residual SE = **2.423** on **396** df, AIC = **1891.7**, BIC = **1939.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7010** | 1.1171 | ±2.2341 | **+14.056** | **7.11e-45** | *** |
| Education: graduate level (vs college) | +0.4710 | 0.2701 | ±0.5403 | +1.744 | 0.0812 | . |
| Education: high school or below (vs college) | -0.4731 | 0.5691 | ±1.1383 | -0.831 | 0.4058 |  |
| Site: UCSD (vs UAB) | +0.2516 | 0.3496 | ±0.6992 | +0.720 | 0.4718 |  |
| Site: UW (vs UAB) | +0.1428 | 0.2979 | ±0.5958 | +0.479 | 0.6316 |  |
| **Age (years)** | **-0.0445** | 0.0124 | ±0.0248 | **-3.581** | **3.42e-04** | *** |
| BMI (kg/m2) | +0.0023 | 0.0160 | ±0.0321 | +0.146 | 0.8841 |  |
| Hypertension | -0.4660 | 0.2788 | ±0.5577 | -1.671 | 0.0947 | . |
| **High cholesterol** | **+0.5765** | 0.2752 | ±0.5503 | **+2.095** | **0.0362** | * |
| **Kidney disease** | **-1.5061** | 0.6940 | ±1.3879 | **-2.170** | **0.0300** | * |
| Circulatory disease | -0.0630 | 0.3807 | ±0.7615 | -0.165 | 0.8686 |  |
| Mean / SD ratio | -0.0599 | 0.0997 | ±0.1993 | -0.601 | 0.5476 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **408**, R² = **0.0924**, Adj R² = **0.0672**, F-statistic = **3.66** (p = **5.71e-05**), Residual SE = **2.423** on **396** df, AIC = **1892.0**, BIC = **1940.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.4587** | 1.1410 | ±2.2821 | **+13.548** | **8.16e-42** | *** |
| Education: graduate level (vs college) | +0.4758 | 0.2703 | ±0.5406 | +1.760 | 0.0784 | . |
| Education: high school or below (vs college) | -0.4776 | 0.5691 | ±1.1381 | -0.839 | 0.4013 |  |
| Site: UCSD (vs UAB) | +0.2559 | 0.3515 | ±0.7029 | +0.728 | 0.4665 |  |
| Site: UW (vs UAB) | +0.1435 | 0.2983 | ±0.5966 | +0.481 | 0.6305 |  |
| **Age (years)** | **-0.0439** | 0.0124 | ±0.0249 | **-3.530** | **4.15e-04** | *** |
| BMI (kg/m2) | +0.0024 | 0.0160 | ±0.0320 | +0.150 | 0.8810 |  |
| Hypertension | -0.4631 | 0.2790 | ±0.5579 | -1.660 | 0.0969 | . |
| **High cholesterol** | **+0.5698** | 0.2754 | ±0.5507 | **+2.069** | **0.0385** | * |
| **Kidney disease** | **-1.4906** | 0.6953 | ±1.3907 | **-2.144** | **0.0321** | * |
| Circulatory disease | -0.0620 | 0.3809 | ±0.7618 | -0.163 | 0.8708 |  |
| Avg. daily mean/SD | -0.0190 | 0.0815 | ±0.1630 | -0.233 | 0.8156 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **408**, R² = **0.0955**, Adj R² = **0.0703**, F-statistic = **3.80** (p = **3.33e-05**), Residual SE = **2.419** on **396** df, AIC = **1890.6**, BIC = **1938.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0524** | 1.2020 | ±2.4040 | **+13.355** | **1.11e-40** | *** |
| Education: graduate level (vs college) | +0.4803 | 0.2702 | ±0.5405 | +1.777 | 0.0756 | . |
| Education: high school or below (vs college) | -0.4868 | 0.5650 | ±1.1301 | -0.861 | 0.3890 |  |
| Site: UCSD (vs UAB) | +0.2774 | 0.3488 | ±0.6975 | +0.795 | 0.4264 |  |
| Site: UW (vs UAB) | +0.1095 | 0.2971 | ±0.5942 | +0.368 | 0.7125 |  |
| **Age (years)** | **-0.0439** | 0.0124 | ±0.0249 | **-3.525** | **4.23e-04** | *** |
| BMI (kg/m2) | +0.0028 | 0.0162 | ±0.0325 | +0.172 | 0.8636 |  |
| Hypertension | -0.4508 | 0.2793 | ±0.5586 | -1.614 | 0.1065 |  |
| High cholesterol | +0.5339 | 0.2803 | ±0.5606 | +1.905 | 0.0568 | . |
| **Kidney disease** | **-1.4690** | 0.6971 | ±1.3942 | **-2.107** | **0.0351** | * |
| Circulatory disease | -0.0658 | 0.3843 | ±0.7686 | -0.171 | 0.8641 |  |
| MAG (mg/dL/h) | -0.0179 | 0.0154 | ±0.0309 | -1.158 | 0.2469 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **408**, R² = **0.0926**, Adj R² = **0.0674**, F-statistic = **3.67** (p = **5.51e-05**), Residual SE = **2.423** on **396** df, AIC = **1891.9**, BIC = **1940.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.1621** | 1.0739 | ±2.1478 | **+14.119** | **2.91e-45** | *** |
| Education: graduate level (vs college) | +0.4781 | 0.2704 | ±0.5407 | +1.769 | 0.0770 | . |
| Education: high school or below (vs college) | -0.4773 | 0.5685 | ±1.1371 | -0.840 | 0.4012 |  |
| Site: UCSD (vs UAB) | +0.2545 | 0.3506 | ±0.7013 | +0.726 | 0.4679 |  |
| Site: UW (vs UAB) | +0.1433 | 0.2982 | ±0.5963 | +0.481 | 0.6308 |  |
| **Age (years)** | **-0.0441** | 0.0124 | ±0.0249 | **-3.550** | **3.85e-04** | *** |
| BMI (kg/m2) | +0.0029 | 0.0161 | ±0.0321 | +0.178 | 0.8589 |  |
| Hypertension | -0.4663 | 0.2793 | ±0.5587 | -1.669 | 0.0950 | . |
| **High cholesterol** | **+0.5728** | 0.2759 | ±0.5518 | **+2.076** | **0.0379** | * |
| **Kidney disease** | **-1.5000** | 0.6991 | ±1.3982 | **-2.145** | **0.0319** | * |
| Circulatory disease | -0.0609 | 0.3798 | ±0.7595 | -0.160 | 0.8726 |  |
| Avg. daily range (mg/dL) | +0.0017 | 0.0043 | ±0.0086 | +0.399 | 0.6899 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **408**, R² = **0.0975**, Adj R² = **0.0724**, F-statistic = **3.89** (p = **2.33e-05**), Residual SE = **2.417** on **396** df, AIC = **1889.7**, BIC = **1937.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.0549** | 0.9954 | ±1.9908 | **+15.124** | **1.12e-51** | *** |
| Education: graduate level (vs college) | +0.4515 | 0.2701 | ±0.5402 | +1.672 | 0.0946 | . |
| Education: high school or below (vs college) | -0.4362 | 0.5733 | ±1.1467 | -0.761 | 0.4468 |  |
| Site: UCSD (vs UAB) | +0.2694 | 0.3455 | ±0.6911 | +0.780 | 0.4356 |  |
| Site: UW (vs UAB) | +0.1425 | 0.2977 | ±0.5955 | +0.479 | 0.6321 |  |
| **Age (years)** | **-0.0440** | 0.0124 | ±0.0248 | **-3.551** | **3.84e-04** | *** |
| BMI (kg/m2) | +0.0004 | 0.0161 | ±0.0323 | +0.027 | 0.9787 |  |
| Hypertension | -0.4655 | 0.2784 | ±0.5568 | -1.672 | 0.0945 | . |
| **High cholesterol** | **+0.5660** | 0.2732 | ±0.5465 | **+2.072** | **0.0383** | * |
| **Kidney disease** | **-1.5086** | 0.6884 | ±1.3768 | **-2.191** | **0.0284** | * |
| Circulatory disease | -0.0685 | 0.3803 | ±0.7606 | -0.180 | 0.8570 |  |
| SD of daily means (mg/dL) | +0.0484 | 0.0262 | ±0.0524 | +1.847 | 0.0648 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **408**, R² = **0.0945**, Adj R² = **0.0694**, F-statistic = **3.76** (p = **3.91e-05**), Residual SE = **2.421** on **396** df, AIC = **1891.0**, BIC = **1939.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.6350** | 2.4555 | ±4.9109 | **+7.182** | **6.87e-13** | *** |
| Education: graduate level (vs college) | +0.4790 | 0.2705 | ±0.5410 | +1.771 | 0.0766 | . |
| Education: high school or below (vs college) | -0.4700 | 0.5688 | ±1.1376 | -0.826 | 0.4086 |  |
| Site: UCSD (vs UAB) | +0.2753 | 0.3457 | ±0.6914 | +0.796 | 0.4258 |  |
| Site: UW (vs UAB) | +0.1580 | 0.2991 | ±0.5982 | +0.528 | 0.5974 |  |
| **Age (years)** | **-0.0444** | 0.0125 | ±0.0250 | **-3.555** | **3.77e-04** | *** |
| BMI (kg/m2) | +0.0023 | 0.0160 | ±0.0320 | +0.143 | 0.8862 |  |
| Hypertension | -0.4680 | 0.2784 | ±0.5569 | -1.681 | 0.0928 | . |
| **High cholesterol** | **+0.5758** | 0.2743 | ±0.5487 | **+2.099** | **0.0358** | * |
| **Kidney disease** | **-1.5539** | 0.7049 | ±1.4098 | **-2.205** | **0.0275** | * |
| Circulatory disease | -0.0420 | 0.3802 | ±0.7603 | -0.110 | 0.9121 |  |
| Time in range 70-180, pooled (%) | -0.0238 | 0.0234 | ±0.0468 | -1.017 | 0.3093 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **408**, R² = **0.0939**, Adj R² = **0.0687**, F-statistic = **3.73** (p = **4.38e-05**), Residual SE = **2.421** on **396** df, AIC = **1891.3**, BIC = **1939.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.2294** | 2.3723 | ±4.7447 | **+7.263** | **3.80e-13** | *** |
| Education: graduate level (vs college) | +0.4800 | 0.2707 | ±0.5413 | +1.773 | 0.0762 | . |
| Education: high school or below (vs college) | -0.4676 | 0.5693 | ±1.1386 | -0.821 | 0.4115 |  |
| Site: UCSD (vs UAB) | +0.2702 | 0.3460 | ±0.6921 | +0.781 | 0.4348 |  |
| Site: UW (vs UAB) | +0.1557 | 0.2990 | ±0.5981 | +0.521 | 0.6027 |  |
| **Age (years)** | **-0.0444** | 0.0125 | ±0.0249 | **-3.558** | **3.73e-04** | *** |
| BMI (kg/m2) | +0.0021 | 0.0160 | ±0.0321 | +0.134 | 0.8936 |  |
| Hypertension | -0.4669 | 0.2785 | ±0.5571 | -1.676 | 0.0937 | . |
| **High cholesterol** | **+0.5718** | 0.2744 | ±0.5489 | **+2.083** | **0.0372** | * |
| **Kidney disease** | **-1.5411** | 0.7055 | ±1.4109 | **-2.184** | **0.0289** | * |
| Circulatory disease | -0.0460 | 0.3804 | ±0.7608 | -0.121 | 0.9037 |  |
| Avg. daily time in range 70-180 (%) | -0.0194 | 0.0223 | ±0.0446 | -0.872 | 0.3831 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **408**, R² = **0.0951**, Adj R² = **0.0700**, F-statistic = **3.78** (p = **3.54e-05**), Residual SE = **2.420** on **396** df, AIC = **1890.8**, BIC = **1938.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.1740** | 1.0058 | ±2.0116 | **+15.086** | **1.99e-51** | *** |
| Education: graduate level (vs college) | +0.4838 | 0.2705 | ±0.5409 | +1.789 | 0.0737 | . |
| Education: high school or below (vs college) | -0.4527 | 0.5697 | ±1.1394 | -0.795 | 0.4268 |  |
| Site: UCSD (vs UAB) | +0.3141 | 0.3534 | ±0.7068 | +0.889 | 0.3740 |  |
| Site: UW (vs UAB) | +0.1867 | 0.3020 | ±0.6040 | +0.618 | 0.5365 |  |
| **Age (years)** | **-0.0437** | 0.0125 | ±0.0249 | **-3.506** | **4.55e-04** | *** |
| BMI (kg/m2) | +0.0034 | 0.0162 | ±0.0325 | +0.210 | 0.8335 |  |
| Hypertension | -0.4459 | 0.2790 | ±0.5580 | -1.598 | 0.1100 |  |
| **High cholesterol** | **+0.5962** | 0.2768 | ±0.5536 | **+2.154** | **0.0313** | * |
| **Kidney disease** | **-1.4886** | 0.6872 | ±1.3744 | **-2.166** | **0.0303** | * |
| Circulatory disease | -0.0501 | 0.3808 | ±0.7615 | -0.132 | 0.8953 |  |
| Time < 54 (%) | +0.1463 | 0.1922 | ±0.3844 | +0.761 | 0.4467 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **408**, R² = **0.0933**, Adj R² = **0.0681**, F-statistic = **3.71** (p = **4.84e-05**), Residual SE = **2.422** on **396** df, AIC = **1891.6**, BIC = **1939.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.2522** | 1.0003 | ±2.0006 | **+15.248** | **1.71e-52** | *** |
| Education: graduate level (vs college) | +0.4856 | 0.2705 | ±0.5411 | +1.795 | 0.0727 | . |
| Education: high school or below (vs college) | -0.4590 | 0.5703 | ±1.1406 | -0.805 | 0.4209 |  |
| Site: UCSD (vs UAB) | +0.2894 | 0.3507 | ±0.7015 | +0.825 | 0.4093 |  |
| Site: UW (vs UAB) | +0.1765 | 0.3036 | ±0.6073 | +0.581 | 0.5610 |  |
| **Age (years)** | **-0.0439** | 0.0124 | ±0.0249 | **-3.532** | **4.13e-04** | *** |
| BMI (kg/m2) | +0.0029 | 0.0161 | ±0.0323 | +0.180 | 0.8568 |  |
| Hypertension | -0.4477 | 0.2803 | ±0.5606 | -1.597 | 0.1102 |  |
| **High cholesterol** | **+0.5839** | 0.2760 | ±0.5519 | **+2.116** | **0.0344** | * |
| **Kidney disease** | **-1.4849** | 0.6886 | ±1.3771 | **-2.157** | **0.0310** | * |
| Circulatory disease | -0.0544 | 0.3814 | ±0.7628 | -0.143 | 0.8866 |  |
| Avg. daily time < 54 (%) | +0.1173 | 0.1498 | ±0.2996 | +0.783 | 0.4334 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **408**, R² = **0.0930**, Adj R² = **0.0678**, F-statistic = **3.69** (p = **5.08e-05**), Residual SE = **2.423** on **396** df, AIC = **1891.7**, BIC = **1939.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.2364** | 1.0080 | ±2.0160 | **+15.116** | **1.27e-51** | *** |
| Education: graduate level (vs college) | +0.4830 | 0.2702 | ±0.5405 | +1.787 | 0.0739 | . |
| Education: high school or below (vs college) | -0.4570 | 0.5727 | ±1.1454 | -0.798 | 0.4249 |  |
| Site: UCSD (vs UAB) | +0.2762 | 0.3477 | ±0.6953 | +0.795 | 0.4269 |  |
| Site: UW (vs UAB) | +0.1650 | 0.2996 | ±0.5991 | +0.551 | 0.5817 |  |
| **Age (years)** | **-0.0435** | 0.0125 | ±0.0249 | **-3.485** | **4.92e-04** | *** |
| BMI (kg/m2) | +0.0023 | 0.0161 | ±0.0322 | +0.141 | 0.8879 |  |
| Hypertension | -0.4505 | 0.2820 | ±0.5639 | -1.598 | 0.1101 |  |
| **High cholesterol** | **+0.5790** | 0.2739 | ±0.5477 | **+2.114** | **0.0345** | * |
| **Kidney disease** | **-1.4752** | 0.6884 | ±1.3768 | **-2.143** | **0.0321** | * |
| Circulatory disease | -0.0567 | 0.3843 | ±0.7685 | -0.147 | 0.8827 |  |
| Time 54-69, pooled (%) | +0.0335 | 0.0470 | ±0.0939 | +0.713 | 0.4761 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **408**, R² = **0.0925**, Adj R² = **0.0673**, F-statistic = **3.67** (p = **5.56e-05**), Residual SE = **2.423** on **396** df, AIC = **1891.9**, BIC = **1940.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.2732** | 1.0050 | ±2.0100 | **+15.198** | **3.67e-52** | *** |
| Education: graduate level (vs college) | +0.4822 | 0.2706 | ±0.5413 | +1.782 | 0.0748 | . |
| Education: high school or below (vs college) | -0.4621 | 0.5727 | ±1.1454 | -0.807 | 0.4197 |  |
| Site: UCSD (vs UAB) | +0.2684 | 0.3472 | ±0.6945 | +0.773 | 0.4396 |  |
| Site: UW (vs UAB) | +0.1573 | 0.3000 | ±0.6000 | +0.524 | 0.6001 |  |
| **Age (years)** | **-0.0435** | 0.0124 | ±0.0249 | **-3.499** | **4.67e-04** | *** |
| BMI (kg/m2) | +0.0024 | 0.0161 | ±0.0322 | +0.148 | 0.8824 |  |
| Hypertension | -0.4552 | 0.2817 | ±0.5635 | -1.616 | 0.1062 |  |
| **High cholesterol** | **+0.5738** | 0.2736 | ±0.5473 | **+2.097** | **0.0360** | * |
| **Kidney disease** | **-1.4751** | 0.6891 | ±1.3782 | **-2.141** | **0.0323** | * |
| Circulatory disease | -0.0601 | 0.3831 | ±0.7662 | -0.157 | 0.8752 |  |
| Avg. daily time 54-69 (%) | +0.0189 | 0.0455 | ±0.0910 | +0.416 | 0.6774 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **408**, R² = **0.0939**, Adj R² = **0.0688**, F-statistic = **3.73** (p = **4.36e-05**), Residual SE = **2.421** on **396** df, AIC = **1891.3**, BIC = **1939.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.1912** | 1.0115 | ±2.0230 | **+15.018** | **5.56e-51** | *** |
| Education: graduate level (vs college) | +0.4850 | 0.2700 | ±0.5401 | +1.796 | 0.0725 | . |
| Education: high school or below (vs college) | -0.4484 | 0.5735 | ±1.1470 | -0.782 | 0.4343 |  |
| Site: UCSD (vs UAB) | +0.2925 | 0.3492 | ±0.6985 | +0.837 | 0.4023 |  |
| Site: UW (vs UAB) | +0.1793 | 0.3014 | ±0.6027 | +0.595 | 0.5518 |  |
| **Age (years)** | **-0.0435** | 0.0125 | ±0.0249 | **-3.491** | **4.80e-04** | *** |
| BMI (kg/m2) | +0.0024 | 0.0161 | ±0.0322 | +0.151 | 0.8796 |  |
| Hypertension | -0.4439 | 0.2817 | ±0.5634 | -1.576 | 0.1150 |  |
| **High cholesterol** | **+0.5885** | 0.2746 | ±0.5491 | **+2.143** | **0.0321** | * |
| **Kidney disease** | **-1.4783** | 0.6878 | ±1.3755 | **-2.149** | **0.0316** | * |
| Circulatory disease | -0.0524 | 0.3841 | ±0.7682 | -0.136 | 0.8916 |  |
| Time < 70 (%) | +0.0389 | 0.0346 | ±0.0692 | +1.125 | 0.2604 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **408**, R² = **0.0928**, Adj R² = **0.0676**, F-statistic = **3.68** (p = **5.34e-05**), Residual SE = **2.423** on **396** df, AIC = **1891.8**, BIC = **1940.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.2596** | 1.0062 | ±2.0124 | **+15.165** | **5.99e-52** | *** |
| Education: graduate level (vs college) | +0.4839 | 0.2707 | ±0.5414 | +1.787 | 0.0739 | . |
| Education: high school or below (vs college) | -0.4575 | 0.5731 | ±1.1462 | -0.798 | 0.4247 |  |
| Site: UCSD (vs UAB) | +0.2743 | 0.3478 | ±0.6955 | +0.789 | 0.4302 |  |
| Site: UW (vs UAB) | +0.1648 | 0.3016 | ±0.6031 | +0.546 | 0.5848 |  |
| **Age (years)** | **-0.0436** | 0.0124 | ±0.0249 | **-3.509** | **4.49e-04** | *** |
| BMI (kg/m2) | +0.0024 | 0.0161 | ±0.0322 | +0.150 | 0.8808 |  |
| Hypertension | -0.4513 | 0.2819 | ±0.5639 | -1.601 | 0.1094 |  |
| **High cholesterol** | **+0.5777** | 0.2740 | ±0.5479 | **+2.109** | **0.0350** | * |
| **Kidney disease** | **-1.4765** | 0.6890 | ±1.3779 | **-2.143** | **0.0321** | * |
| Circulatory disease | -0.0583 | 0.3832 | ±0.7664 | -0.152 | 0.8791 |  |
| Avg. daily time < 70 (%) | +0.0216 | 0.0350 | ±0.0701 | +0.616 | 0.5379 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **408**, R² = **0.0944**, Adj R² = **0.0692**, F-statistic = **3.75** (p = **4.03e-05**), Residual SE = **2.421** on **396** df, AIC = **1891.1**, BIC = **1939.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0509** | 10.3201 | ±20.6401 | **+2.427** | **0.0152** | * |
| Education: graduate level (vs college) | +0.4827 | 0.2708 | ±0.5416 | +1.782 | 0.0747 | . |
| Education: high school or below (vs college) | -0.4586 | 0.5687 | ±1.1374 | -0.806 | 0.4200 |  |
| Site: UCSD (vs UAB) | +0.2969 | 0.3485 | ±0.6969 | +0.852 | 0.3942 |  |
| Site: UW (vs UAB) | +0.1773 | 0.3016 | ±0.6032 | +0.588 | 0.5565 |  |
| **Age (years)** | **-0.0441** | 0.0125 | ±0.0249 | **-3.540** | **4.01e-04** | *** |
| BMI (kg/m2) | +0.0031 | 0.0161 | ±0.0322 | +0.195 | 0.8455 |  |
| Hypertension | -0.4557 | 0.2784 | ±0.5568 | -1.637 | 0.1017 |  |
| **High cholesterol** | **+0.5937** | 0.2772 | ±0.5543 | **+2.142** | **0.0322** | * |
| **Kidney disease** | **-1.5398** | 0.7015 | ±1.4029 | **-2.195** | **0.0282** | * |
| Circulatory disease | -0.0447 | 0.3804 | ±0.7609 | -0.117 | 0.9066 |  |
| Time 54-250, pooled (%) | -0.0982 | 0.1039 | ±0.2077 | -0.946 | 0.3444 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **408**, R² = **0.0934**, Adj R² = **0.0683**, F-statistic = **3.71** (p = **4.73e-05**), Residual SE = **2.422** on **396** df, AIC = **1891.5**, BIC = **1939.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6293** | 10.3998 | ±20.7997 | **+2.272** | **0.0231** | * |
| Education: graduate level (vs college) | +0.4848 | 0.2712 | ±0.5424 | +1.787 | 0.0739 | . |
| Education: high school or below (vs college) | -0.4614 | 0.5694 | ±1.1388 | -0.810 | 0.4178 |  |
| Site: UCSD (vs UAB) | +0.2831 | 0.3477 | ±0.6954 | +0.814 | 0.4155 |  |
| Site: UW (vs UAB) | +0.1704 | 0.3021 | ±0.6042 | +0.564 | 0.5728 |  |
| **Age (years)** | **-0.0443** | 0.0125 | ±0.0250 | **-3.547** | **3.90e-04** | *** |
| BMI (kg/m2) | +0.0027 | 0.0161 | ±0.0321 | +0.169 | 0.8659 |  |
| Hypertension | -0.4549 | 0.2788 | ±0.5576 | -1.632 | 0.1027 |  |
| **High cholesterol** | **+0.5832** | 0.2766 | ±0.5533 | **+2.108** | **0.0350** | * |
| **Kidney disease** | **-1.5324** | 0.7049 | ±1.4098 | **-2.174** | **0.0297** | * |
| Circulatory disease | -0.0477 | 0.3812 | ±0.7624 | -0.125 | 0.9004 |  |
| Avg. daily time 54-250 (%) | -0.0835 | 0.1045 | ±0.2090 | -0.799 | 0.4245 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **408**, R² = **0.0933**, Adj R² = **0.0681**, F-statistic = **3.70** (p = **4.88e-05**), Residual SE = **2.422** on **396** df, AIC = **1891.6**, BIC = **1939.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.3175** | 0.9980 | ±1.9959 | **+15.349** | **3.60e-53** | *** |
| Education: graduate level (vs college) | +0.4757 | 0.2707 | ±0.5413 | +1.758 | 0.0788 | . |
| Education: high school or below (vs college) | -0.4842 | 0.5664 | ±1.1329 | -0.855 | 0.3927 |  |
| Site: UCSD (vs UAB) | +0.2576 | 0.3482 | ±0.6964 | +0.740 | 0.4595 |  |
| Site: UW (vs UAB) | +0.1376 | 0.2990 | ±0.5980 | +0.460 | 0.6453 |  |
| **Age (years)** | **-0.0441** | 0.0125 | ±0.0250 | **-3.526** | **4.22e-04** | *** |
| BMI (kg/m2) | +0.0024 | 0.0160 | ±0.0321 | +0.151 | 0.8799 |  |
| Hypertension | -0.4758 | 0.2801 | ±0.5603 | -1.698 | 0.0894 | . |
| **High cholesterol** | **+0.5624** | 0.2740 | ±0.5481 | **+2.052** | **0.0401** | * |
| **Kidney disease** | **-1.5284** | 0.7059 | ±1.4118 | **-2.165** | **0.0304** | * |
| Circulatory disease | -0.0527 | 0.3786 | ±0.7571 | -0.139 | 0.8893 |  |
| Time 181-250, pooled (%) | +0.0196 | 0.0301 | ±0.0602 | +0.653 | 0.5139 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **408**, R² = **0.0934**, Adj R² = **0.0682**, F-statistic = **3.71** (p = **4.80e-05**), Residual SE = **2.422** on **396** df, AIC = **1891.5**, BIC = **1939.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.3215** | 0.9978 | ±1.9957 | **+15.355** | **3.30e-53** | *** |
| Education: graduate level (vs college) | +0.4751 | 0.2707 | ±0.5414 | +1.755 | 0.0792 | . |
| Education: high school or below (vs college) | -0.4834 | 0.5664 | ±1.1328 | -0.853 | 0.3934 |  |
| Site: UCSD (vs UAB) | +0.2586 | 0.3479 | ±0.6958 | +0.743 | 0.4572 |  |
| Site: UW (vs UAB) | +0.1372 | 0.2989 | ±0.5977 | +0.459 | 0.6462 |  |
| **Age (years)** | **-0.0442** | 0.0125 | ±0.0250 | **-3.527** | **4.20e-04** | *** |
| BMI (kg/m2) | +0.0023 | 0.0160 | ±0.0321 | +0.145 | 0.8846 |  |
| Hypertension | -0.4768 | 0.2802 | ±0.5604 | -1.702 | 0.0888 | . |
| **High cholesterol** | **+0.5616** | 0.2739 | ±0.5478 | **+2.050** | **0.0403** | * |
| **Kidney disease** | **-1.5300** | 0.7059 | ±1.4118 | **-2.168** | **0.0302** | * |
| Circulatory disease | -0.0519 | 0.3785 | ±0.7571 | -0.137 | 0.8909 |  |
| Avg. daily time 181-250 (%) | +0.0197 | 0.0287 | ±0.0575 | +0.685 | 0.4932 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **408**, R² = **0.0931**, Adj R² = **0.0679**, F-statistic = **3.70** (p = **5.02e-05**), Residual SE = **2.422** on **396** df, AIC = **1891.7**, BIC = **1939.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.3170** | 0.9977 | ±1.9954 | **+15.352** | **3.43e-53** | *** |
| Education: graduate level (vs college) | +0.4764 | 0.2708 | ±0.5416 | +1.759 | 0.0785 | . |
| Education: high school or below (vs college) | -0.4821 | 0.5667 | ±1.1333 | -0.851 | 0.3949 |  |
| Site: UCSD (vs UAB) | +0.2584 | 0.3482 | ±0.6964 | +0.742 | 0.4581 |  |
| Site: UW (vs UAB) | +0.1397 | 0.2989 | ±0.5979 | +0.467 | 0.6402 |  |
| **Age (years)** | **-0.0441** | 0.0125 | ±0.0250 | **-3.523** | **4.27e-04** | *** |
| BMI (kg/m2) | +0.0025 | 0.0160 | ±0.0321 | +0.153 | 0.8784 |  |
| Hypertension | -0.4740 | 0.2800 | ±0.5600 | -1.693 | 0.0904 | . |
| **High cholesterol** | **+0.5645** | 0.2742 | ±0.5484 | **+2.059** | **0.0395** | * |
| **Kidney disease** | **-1.5275** | 0.7090 | ±1.4180 | **-2.154** | **0.0312** | * |
| Circulatory disease | -0.0530 | 0.3788 | ±0.7576 | -0.140 | 0.8887 |  |
| Time > 180 (%) | +0.0159 | 0.0272 | ±0.0544 | +0.586 | 0.5579 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **408**, R² = **0.0933**, Adj R² = **0.0681**, F-statistic = **3.70** (p = **4.87e-05**), Residual SE = **2.422** on **396** df, AIC = **1891.6**, BIC = **1939.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.3222** | 0.9977 | ±1.9953 | **+15.358** | **3.13e-53** | *** |
| Education: graduate level (vs college) | +0.4759 | 0.2709 | ±0.5417 | +1.757 | 0.0789 | . |
| Education: high school or below (vs college) | -0.4816 | 0.5666 | ±1.1333 | -0.850 | 0.3954 |  |
| Site: UCSD (vs UAB) | +0.2595 | 0.3478 | ±0.6957 | +0.746 | 0.4557 |  |
| Site: UW (vs UAB) | +0.1390 | 0.2989 | ±0.5977 | +0.465 | 0.6420 |  |
| **Age (years)** | **-0.0441** | 0.0125 | ±0.0250 | **-3.527** | **4.20e-04** | *** |
| BMI (kg/m2) | +0.0023 | 0.0160 | ±0.0321 | +0.146 | 0.8837 |  |
| Hypertension | -0.4752 | 0.2800 | ±0.5600 | -1.697 | 0.0896 | . |
| **High cholesterol** | **+0.5633** | 0.2740 | ±0.5481 | **+2.056** | **0.0398** | * |
| **Kidney disease** | **-1.5319** | 0.7086 | ±1.4173 | **-2.162** | **0.0306** | * |
| Circulatory disease | -0.0517 | 0.3787 | ±0.7575 | -0.137 | 0.8914 |  |
| Avg. daily time > 180 (%) | +0.0167 | 0.0263 | ±0.0527 | +0.635 | 0.5256 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **408**, R² = **0.0928**, Adj R² = **0.0676**, F-statistic = **3.68** (p = **5.33e-05**), Residual SE = **2.423** on **396** df, AIC = **1891.8**, BIC = **1940.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.3212** | 1.0021 | ±2.0042 | **+15.289** | **8.99e-53** | *** |
| Education: graduate level (vs college) | +0.4840 | 0.2712 | ±0.5423 | +1.785 | 0.0743 | . |
| Education: high school or below (vs college) | -0.4821 | 0.5676 | ±1.1351 | -0.849 | 0.3956 |  |
| Site: UCSD (vs UAB) | +0.2632 | 0.3471 | ±0.6943 | +0.758 | 0.4483 |  |
| Site: UW (vs UAB) | +0.1439 | 0.2983 | ±0.5966 | +0.482 | 0.6295 |  |
| **Age (years)** | **-0.0438** | 0.0125 | ±0.0251 | **-3.491** | **4.81e-04** | *** |
| BMI (kg/m2) | +0.0020 | 0.0162 | ±0.0324 | +0.122 | 0.9026 |  |
| Hypertension | -0.4720 | 0.2808 | ±0.5617 | -1.681 | 0.0928 | . |
| **High cholesterol** | **+0.5684** | 0.2743 | ±0.5485 | **+2.072** | **0.0382** | * |
| **Kidney disease** | **-1.4780** | 0.6900 | ±1.3799 | **-2.142** | **0.0322** | * |
| Circulatory disease | -0.0485 | 0.3808 | ±0.7615 | -0.127 | 0.8986 |  |
| Nocturnal time > 180 (%) | +0.0125 | 0.0272 | ±0.0544 | +0.458 | 0.6469 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **408**, R² = **0.0936**, Adj R² = **0.0684**, F-statistic = **3.72** (p = **4.61e-05**), Residual SE = **2.422** on **396** df, AIC = **1891.4**, BIC = **1939.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.2893** | 0.9936 | ±1.9872 | **+15.388** | **1.99e-53** | *** |
| Education: graduate level (vs college) | +0.4866 | 0.2707 | ±0.5415 | +1.797 | 0.0723 | . |
| Education: high school or below (vs college) | -0.4715 | 0.5663 | ±1.1325 | -0.833 | 0.4050 |  |
| Site: UCSD (vs UAB) | +0.2462 | 0.3507 | ±0.7015 | +0.702 | 0.4827 |  |
| Site: UW (vs UAB) | +0.1464 | 0.2983 | ±0.5966 | +0.491 | 0.6236 |  |
| **Age (years)** | **-0.0442** | 0.0125 | ±0.0250 | **-3.533** | **4.11e-04** | *** |
| BMI (kg/m2) | +0.0031 | 0.0160 | ±0.0320 | +0.194 | 0.8458 |  |
| Hypertension | -0.4739 | 0.2788 | ±0.5577 | -1.699 | 0.0892 | . |
| **High cholesterol** | **+0.5704** | 0.2749 | ±0.5498 | **+2.075** | **0.0380** | * |
| **Kidney disease** | **-1.5040** | 0.6886 | ±1.3772 | **-2.184** | **0.0290** | * |
| Circulatory disease | -0.0526 | 0.3777 | ±0.7553 | -0.139 | 0.8893 |  |
| Any reading > 250 during wear (0/1) | +0.2520 | 0.3506 | ±0.7012 | +0.719 | 0.4722 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **408**, R² = **0.0923**, Adj R² = **0.0671**, F-statistic = **3.66** (p = **5.76e-05**), Residual SE = **2.424** on **396** df, AIC = **1892.0**, BIC = **1940.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.3066** | 0.9959 | ±1.9918 | **+15.369** | **2.62e-53** | *** |
| Education: graduate level (vs college) | +0.4790 | 0.2711 | ±0.5421 | +1.767 | 0.0772 | . |
| Education: high school or below (vs college) | -0.4741 | 0.5674 | ±1.1347 | -0.836 | 0.4034 |  |
| Site: UCSD (vs UAB) | +0.2619 | 0.3484 | ±0.6967 | +0.752 | 0.4522 |  |
| Site: UW (vs UAB) | +0.1463 | 0.2982 | ±0.5964 | +0.490 | 0.6238 |  |
| **Age (years)** | **-0.0436** | 0.0125 | ±0.0250 | **-3.488** | **4.87e-04** | *** |
| BMI (kg/m2) | +0.0026 | 0.0161 | ±0.0321 | +0.161 | 0.8721 |  |
| Hypertension | -0.4640 | 0.2789 | ±0.5578 | -1.664 | 0.0962 | . |
| **High cholesterol** | **+0.5693** | 0.2758 | ±0.5517 | **+2.064** | **0.0390** | * |
| **Kidney disease** | **-1.4907** | 0.7200 | ±1.4400 | **-2.071** | **0.0384** | * |
| Circulatory disease | -0.0601 | 0.3805 | ±0.7611 | -0.158 | 0.8744 |  |
| Time > 250 (%) | +0.0257 | 0.1885 | ±0.3770 | +0.136 | 0.8917 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 408)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **408**, R² = **0.0926**, Adj R² = **0.0674**, F-statistic = **3.67** (p = **5.51e-05**), Residual SE = **2.423** on **396** df, AIC = **1891.9**, BIC = **1940.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.3154** | 0.9963 | ±1.9925 | **+15.373** | **2.49e-53** | *** |
| Education: graduate level (vs college) | +0.4796 | 0.2719 | ±0.5438 | +1.764 | 0.0777 | . |
| Education: high school or below (vs college) | -0.4729 | 0.5677 | ±1.1354 | -0.833 | 0.4048 |  |
| Site: UCSD (vs UAB) | +0.2631 | 0.3480 | ±0.6960 | +0.756 | 0.4497 |  |
| Site: UW (vs UAB) | +0.1472 | 0.2986 | ±0.5972 | +0.493 | 0.6220 |  |
| **Age (years)** | **-0.0438** | 0.0125 | ±0.0250 | **-3.504** | **4.58e-04** | *** |
| BMI (kg/m2) | +0.0025 | 0.0161 | ±0.0321 | +0.156 | 0.8757 |  |
| Hypertension | -0.4649 | 0.2787 | ±0.5574 | -1.668 | 0.0953 | . |
| **High cholesterol** | **+0.5704** | 0.2761 | ±0.5521 | **+2.066** | **0.0388** | * |
| **Kidney disease** | **-1.5122** | 0.7166 | ±1.4333 | **-2.110** | **0.0348** | * |
| Circulatory disease | -0.0561 | 0.3807 | ±0.7613 | -0.147 | 0.8828 |  |
| Avg. daily time > 250 (%) | +0.0600 | 0.2135 | ±0.4269 | +0.281 | 0.7788 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Healthy group (no diabetes + pre-diabetes / lifestyle) - Cognition

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 90 single-predictor tests; 4 with raw p < 0.05 (about 4 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 408): best single predictor out of sample is **Mean/SD** (CV R² 0.039 vs 0.038 for covariates alone, gain +0.001; +0.179 per SD, p = 0.170). No glycaemic measure is associated with this outcome (all p > 0.05). Not predictable from glycaemia in this sample.
- **Cognitive impairment (MoCA < 26)** (n = 408): best single predictor out of sample is **%<70 (pooled)** (CV AUC 0.641 vs 0.631 for covariates alone, gain +0.011; OR 1.28 per SD, p = 0.025). Raw p < 0.05 (FDR not applicable here): %54-69 (pooled) (p = 0.014), %54-69 (daily avg) (p = 0.019), %<70 (pooled) (p = 0.025), %<70 (daily avg) (p = 0.033).
- **MoCA memory index score (0-15)** (n = 408): best single predictor out of sample is **SD of daily means** (CV R² 0.038 vs 0.033 for covariates alone, gain +0.005; +0.183 per SD, p = 0.065). No glycaemic measure is associated with this outcome (all p > 0.05).

**Most predictable outcomes (largest out-of-sample gain over covariates):** Cognitive impairment (MoCA < 26) (+0.011, via %<70 (pooled)); MoCA memory index score (0-15) (+0.005, via SD of daily means); MoCA total score (0-30) (+0.001, via Mean/SD). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** Band 54-69 (0 FDR-significant / 2 raw-significant of 6); Band < 70 (0 FDR-significant / 2 raw-significant of 6); HbA1c (0 FDR-significant / 0 raw-significant of 3).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (0 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** Cognitive impairment (%54-69 (pooled), ΔAIC -5.5); MoCA memory index score (SD of daily means, ΔAIC -2.4).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
