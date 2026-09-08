# Phase 6 model output tables - All (analysis base) - Healthy group (no diabetes + pre-diabetes / lifestyle) - Cognition

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models. [Index of all model-output files](../../README.md)


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 1,271; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1271**, R² = **0.1050**, Adj R² = **0.0979**, F-statistic = **14.79** (p = **3.71e-25**), Residual SE = **2.735** on **1260** df, AIC = **6175.2**, BIC = **6231.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5580** | 0.6108 | ±1.2217 | **+48.390** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6088** | 0.1611 | ±0.3222 | **+3.779** | **1.57e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5624** | 0.3777 | ±0.7555 | **-4.136** | **3.53e-05** | *** |
| Site: UCSD (vs UAB) | -0.4023 | 0.2208 | ±0.4415 | -1.822 | 0.0684 | . |
| Site: UW (vs UAB) | -0.2607 | 0.2013 | ±0.4026 | -1.295 | 0.1953 |  |
| **Age (years)** | **-0.0508** | 0.0072 | ±0.0145 | **-7.004** | **2.48e-12** | *** |
| BMI (kg/m2) | -0.0093 | 0.0111 | ±0.0221 | -0.844 | 0.3989 |  |
| Hypertension | -0.2119 | 0.1732 | ±0.3463 | -1.224 | 0.2210 |  |
| High cholesterol | +0.2403 | 0.1614 | ±0.3227 | +1.489 | 0.1365 |  |
| Kidney disease | -0.2115 | 0.3433 | ±0.6865 | -0.616 | 0.5379 |  |
| **Circulatory disease** | **-0.7194** | 0.2565 | ±0.5131 | **-2.804** | **0.0050** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1271**, R² = **0.1160**, Adj R² = **0.1083**, F-statistic = **15.02** (p = **9.62e-28**), Residual SE = **2.719** on **1259** df, AIC = **6161.5**, BIC = **6223.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.4873** | 1.1968 | ±2.3936 | **+27.145** | **2.93e-162** | *** |
| **Education: graduate level (vs college)** | **+0.6120** | 0.1610 | ±0.3221 | **+3.800** | **1.45e-04** | *** |
| **Education: high school or below (vs college)** | **-1.4806** | 0.3694 | ±0.7388 | **-4.008** | **6.12e-05** | *** |
| Site: UCSD (vs UAB) | -0.3889 | 0.2192 | ±0.4385 | -1.774 | 0.0761 | . |
| Site: UW (vs UAB) | -0.2387 | 0.2005 | ±0.4010 | -1.191 | 0.2338 |  |
| **Age (years)** | **-0.0483** | 0.0073 | ±0.0145 | **-6.655** | **2.84e-11** | *** |
| BMI (kg/m2) | -0.0053 | 0.0112 | ±0.0225 | -0.476 | 0.6344 |  |
| Hypertension | -0.1793 | 0.1718 | ±0.3436 | -1.044 | 0.2966 |  |
| High cholesterol | +0.3000 | 0.1629 | ±0.3258 | +1.842 | 0.0655 | . |
| Kidney disease | -0.2205 | 0.3364 | ±0.6728 | -0.655 | 0.5123 |  |
| **Circulatory disease** | **-0.6754** | 0.2550 | ±0.5100 | **-2.648** | **0.0081** | ** |
| **HbA1c (%)** | **-0.5747** | 0.2055 | ±0.4110 | **-2.797** | **0.0052** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1271**, R² = **0.1248**, Adj R² = **0.1171**, F-statistic = **16.32** (p = **2.51e-30**), Residual SE = **2.705** on **1259** df, AIC = **6148.9**, BIC = **6210.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.8800** | 0.8229 | ±1.6458 | **+38.741** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6588** | 0.1604 | ±0.3209 | **+4.106** | **4.02e-05** | *** |
| **Education: high school or below (vs college)** | **-1.4463** | 0.3624 | ±0.7248 | **-3.991** | **6.59e-05** | *** |
| Site: UCSD (vs UAB) | -0.4136 | 0.2170 | ±0.4339 | -1.906 | 0.0566 | . |
| Site: UW (vs UAB) | -0.1938 | 0.2000 | ±0.3999 | -0.969 | 0.3324 |  |
| **Age (years)** | **-0.0492** | 0.0072 | ±0.0144 | **-6.842** | **7.79e-12** | *** |
| BMI (kg/m2) | -0.0065 | 0.0112 | ±0.0225 | -0.578 | 0.5631 |  |
| Hypertension | -0.1386 | 0.1717 | ±0.3433 | -0.807 | 0.4194 |  |
| High cholesterol | +0.2796 | 0.1612 | ±0.3225 | +1.734 | 0.0830 | . |
| Kidney disease | -0.1470 | 0.3347 | ±0.6694 | -0.439 | 0.6605 |  |
| **Circulatory disease** | **-0.6544** | 0.2515 | ±0.5031 | **-2.602** | **0.0093** | ** |
| **Mean glucose (mg/dL)** | **-0.0215** | 0.0055 | ±0.0109 | **-3.934** | **8.36e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1271**, R² = **0.1248**, Adj R² = **0.1171**, F-statistic = **16.32** (p = **2.51e-30**), Residual SE = **2.705** on **1259** df, AIC = **6148.9**, BIC = **6210.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+34.8580** | 1.4459 | ±2.8919 | **+24.108** | **2.08e-128** | *** |
| **Education: graduate level (vs college)** | **+0.6588** | 0.1604 | ±0.3209 | **+4.106** | **4.02e-05** | *** |
| **Education: high school or below (vs college)** | **-1.4463** | 0.3624 | ±0.7248 | **-3.991** | **6.59e-05** | *** |
| Site: UCSD (vs UAB) | -0.4136 | 0.2170 | ±0.4339 | -1.906 | 0.0566 | . |
| Site: UW (vs UAB) | -0.1938 | 0.2000 | ±0.3999 | -0.969 | 0.3324 |  |
| **Age (years)** | **-0.0492** | 0.0072 | ±0.0144 | **-6.842** | **7.79e-12** | *** |
| BMI (kg/m2) | -0.0065 | 0.0112 | ±0.0225 | -0.578 | 0.5631 |  |
| Hypertension | -0.1386 | 0.1717 | ±0.3433 | -0.807 | 0.4194 |  |
| High cholesterol | +0.2796 | 0.1612 | ±0.3225 | +1.734 | 0.0830 | . |
| Kidney disease | -0.1470 | 0.3347 | ±0.6694 | -0.439 | 0.6605 |  |
| **Circulatory disease** | **-0.6544** | 0.2515 | ±0.5031 | **-2.602** | **0.0093** | ** |
| **GMI (%)** | **-0.8997** | 0.2287 | ±0.4574 | **-3.934** | **8.36e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1271**, R² = **0.1199**, Adj R² = **0.1122**, F-statistic = **15.59** (p = **7.16e-29**), Residual SE = **2.713** on **1259** df, AIC = **6156.0**, BIC = **6217.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.4409** | 0.8071 | ±1.6143 | **+38.954** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6391** | 0.1610 | ±0.3220 | **+3.970** | **7.19e-05** | *** |
| **Education: high school or below (vs college)** | **-1.4653** | 0.3635 | ±0.7271 | **-4.031** | **5.56e-05** | *** |
| Site: UCSD (vs UAB) | -0.3869 | 0.2192 | ±0.4384 | -1.765 | 0.0775 | . |
| Site: UW (vs UAB) | -0.2080 | 0.2005 | ±0.4011 | -1.037 | 0.2997 |  |
| **Age (years)** | **-0.0512** | 0.0072 | ±0.0145 | **-7.071** | **1.54e-12** | *** |
| BMI (kg/m2) | -0.0024 | 0.0116 | ±0.0232 | -0.208 | 0.8350 |  |
| Hypertension | -0.1636 | 0.1722 | ±0.3445 | -0.950 | 0.3423 |  |
| High cholesterol | +0.2886 | 0.1627 | ±0.3253 | +1.774 | 0.0760 | . |
| Kidney disease | -0.2037 | 0.3365 | ±0.6730 | -0.605 | 0.5449 |  |
| **Circulatory disease** | **-0.6836** | 0.2510 | ±0.5019 | **-2.724** | **0.0064** | ** |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0179** | 0.0052 | ±0.0105 | **-3.410** | **6.49e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1271**, R² = **0.1115**, Adj R² = **0.1038**, F-statistic = **14.37** (p = **1.96e-26**), Residual SE = **2.726** on **1259** df, AIC = **6168.0**, BIC = **6229.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.2142** | 0.6563 | ±1.3126 | **+46.037** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6143** | 0.1609 | ±0.3218 | **+3.818** | **1.35e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5502** | 0.3725 | ±0.7450 | **-4.161** | **3.16e-05** | *** |
| **Site: UCSD (vs UAB)** | **-0.4336** | 0.2191 | ±0.4382 | **-1.979** | **0.0478** | * |
| Site: UW (vs UAB) | -0.2420 | 0.2013 | ±0.4026 | -1.202 | 0.2292 |  |
| **Age (years)** | **-0.0493** | 0.0072 | ±0.0145 | **-6.825** | **8.78e-12** | *** |
| BMI (kg/m2) | -0.0090 | 0.0113 | ±0.0225 | -0.798 | 0.4251 |  |
| Hypertension | -0.1665 | 0.1723 | ±0.3447 | -0.966 | 0.3339 |  |
| High cholesterol | +0.2372 | 0.1610 | ±0.3220 | +1.473 | 0.1408 |  |
| Kidney disease | -0.1400 | 0.3401 | ±0.6802 | -0.412 | 0.6807 |  |
| **Circulatory disease** | **-0.6859** | 0.2545 | ±0.5091 | **-2.695** | **0.0070** | ** |
| **Glucose SD, pooled (mg/dL)** | **-0.0360** | 0.0142 | ±0.0285 | **-2.528** | **0.0115** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1271**, R² = **0.1113**, Adj R² = **0.1035**, F-statistic = **14.33** (p = **2.32e-26**), Residual SE = **2.726** on **1259** df, AIC = **6168.3**, BIC = **6230.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.1523** | 0.6427 | ±1.2854 | **+46.914** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6178** | 0.1608 | ±0.3217 | **+3.841** | **1.23e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5495** | 0.3735 | ±0.7469 | **-4.149** | **3.34e-05** | *** |
| Site: UCSD (vs UAB) | -0.4292 | 0.2190 | ±0.4380 | -1.959 | 0.0501 | . |
| Site: UW (vs UAB) | -0.2386 | 0.2015 | ±0.4030 | -1.184 | 0.2363 |  |
| **Age (years)** | **-0.0492** | 0.0072 | ±0.0145 | **-6.805** | **1.01e-11** | *** |
| BMI (kg/m2) | -0.0086 | 0.0113 | ±0.0225 | -0.760 | 0.4470 |  |
| Hypertension | -0.1685 | 0.1728 | ±0.3456 | -0.975 | 0.3296 |  |
| High cholesterol | +0.2388 | 0.1611 | ±0.3222 | +1.482 | 0.1383 |  |
| Kidney disease | -0.1375 | 0.3399 | ±0.6798 | -0.404 | 0.6859 |  |
| **Circulatory disease** | **-0.6875** | 0.2551 | ±0.5102 | **-2.695** | **0.0070** | ** |
| **Avg. daily SD (mg/dL)** | **-0.0377** | 0.0143 | ±0.0286 | **-2.636** | **0.0084** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1271**, R² = **0.1052**, Adj R² = **0.0974**, F-statistic = **13.45** (p = **1.35e-24**), Residual SE = **2.736** on **1259** df, AIC = **6177.0**, BIC = **6238.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.6996** | 0.6985 | ±1.3969 | **+42.521** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6067** | 0.1613 | ±0.3226 | **+3.762** | **1.69e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5663** | 0.3776 | ±0.7551 | **-4.148** | **3.35e-05** | *** |
| Site: UCSD (vs UAB) | -0.4081 | 0.2218 | ±0.4436 | -1.840 | 0.0658 | . |
| Site: UW (vs UAB) | -0.2615 | 0.2015 | ±0.4029 | -1.298 | 0.1942 |  |
| **Age (years)** | **-0.0506** | 0.0073 | ±0.0145 | **-6.960** | **3.40e-12** | *** |
| BMI (kg/m2) | -0.0094 | 0.0111 | ±0.0222 | -0.850 | 0.3955 |  |
| Hypertension | -0.2079 | 0.1733 | ±0.3467 | -1.200 | 0.2303 |  |
| High cholesterol | +0.2370 | 0.1618 | ±0.3236 | +1.465 | 0.1429 |  |
| Kidney disease | -0.2027 | 0.3430 | ±0.6860 | -0.591 | 0.5546 |  |
| **Circulatory disease** | **-0.7174** | 0.2569 | ±0.5138 | **-2.793** | **0.0052** | ** |
| CV (%) | -0.0084 | 0.0203 | ±0.0406 | -0.412 | 0.6806 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1271**, R² = **0.1051**, Adj R² = **0.0973**, F-statistic = **13.44** (p = **1.43e-24**), Residual SE = **2.736** on **1259** df, AIC = **6177.2**, BIC = **6238.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.4618** | 0.7491 | ±1.4982 | **+39.330** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6075** | 0.1612 | ±0.3225 | **+3.767** | **1.65e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5631** | 0.3778 | ±0.7556 | **-4.137** | **3.51e-05** | *** |
| Site: UCSD (vs UAB) | -0.4052 | 0.2215 | ±0.4430 | -1.830 | 0.0673 | . |
| Site: UW (vs UAB) | -0.2602 | 0.2015 | ±0.4030 | -1.291 | 0.1965 |  |
| **Age (years)** | **-0.0507** | 0.0073 | ±0.0145 | **-6.972** | **3.12e-12** | *** |
| BMI (kg/m2) | -0.0094 | 0.0111 | ±0.0222 | -0.848 | 0.3967 |  |
| Hypertension | -0.2095 | 0.1731 | ±0.3462 | -1.210 | 0.2263 |  |
| High cholesterol | +0.2390 | 0.1618 | ±0.3235 | +1.478 | 0.1395 |  |
| Kidney disease | -0.2077 | 0.3428 | ±0.6856 | -0.606 | 0.5445 |  |
| **Circulatory disease** | **-0.7187** | 0.2568 | ±0.5136 | **-2.799** | **0.0051** | ** |
| Mean / SD ratio | +0.0156 | 0.0684 | ±0.1368 | +0.228 | 0.8199 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1271**, R² = **0.1051**, Adj R² = **0.0973**, F-statistic = **13.44** (p = **1.44e-24**), Residual SE = **2.736** on **1259** df, AIC = **6177.2**, BIC = **6238.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.4747** | 0.7467 | ±1.4934 | **+39.473** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6082** | 0.1613 | ±0.3226 | **+3.771** | **1.62e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5623** | 0.3781 | ±0.7562 | **-4.132** | **3.59e-05** | *** |
| Site: UCSD (vs UAB) | -0.4042 | 0.2213 | ±0.4426 | -1.827 | 0.0678 | . |
| Site: UW (vs UAB) | -0.2599 | 0.2015 | ±0.4030 | -1.290 | 0.1971 |  |
| **Age (years)** | **-0.0506** | 0.0073 | ±0.0145 | **-6.963** | **3.34e-12** | *** |
| BMI (kg/m2) | -0.0093 | 0.0111 | ±0.0222 | -0.839 | 0.4015 |  |
| Hypertension | -0.2104 | 0.1733 | ±0.3465 | -1.214 | 0.2247 |  |
| High cholesterol | +0.2393 | 0.1618 | ±0.3236 | +1.479 | 0.1392 |  |
| Kidney disease | -0.2074 | 0.3429 | ±0.6858 | -0.605 | 0.5453 |  |
| **Circulatory disease** | **-0.7191** | 0.2568 | ±0.5136 | **-2.800** | **0.0051** | ** |
| Avg. daily mean/SD | +0.0111 | 0.0555 | ±0.1110 | +0.201 | 0.8410 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1271**, R² = **0.1057**, Adj R² = **0.0979**, F-statistic = **13.52** (p = **9.71e-25**), Residual SE = **2.735** on **1259** df, AIC = **6176.3**, BIC = **6238.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.9305** | 0.7336 | ±1.4671 | **+40.801** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6061** | 0.1612 | ±0.3225 | **+3.759** | **1.71e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5569** | 0.3761 | ±0.7521 | **-4.140** | **3.47e-05** | *** |
| Site: UCSD (vs UAB) | -0.4146 | 0.2206 | ±0.4411 | -1.880 | 0.0601 | . |
| Site: UW (vs UAB) | -0.2732 | 0.2007 | ±0.4015 | -1.361 | 0.1735 |  |
| **Age (years)** | **-0.0509** | 0.0073 | ±0.0145 | **-7.017** | **2.26e-12** | *** |
| BMI (kg/m2) | -0.0092 | 0.0111 | ±0.0223 | -0.826 | 0.4085 |  |
| Hypertension | -0.2129 | 0.1733 | ±0.3465 | -1.229 | 0.2192 |  |
| High cholesterol | +0.2322 | 0.1614 | ±0.3227 | +1.439 | 0.1502 |  |
| Kidney disease | -0.2032 | 0.3444 | ±0.6888 | -0.590 | 0.5552 |  |
| **Circulatory disease** | **-0.7165** | 0.2566 | ±0.5132 | **-2.792** | **0.0052** | ** |
| MAG (mg/dL/h) | -0.0092 | 0.0103 | ±0.0205 | -0.900 | 0.3683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1271**, R² = **0.1091**, Adj R² = **0.1013**, F-statistic = **14.02** (p = **9.98e-26**), Residual SE = **2.730** on **1259** df, AIC = **6171.4**, BIC = **6233.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.2180** | 0.6770 | ±1.3539 | **+44.638** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6170** | 0.1609 | ±0.3218 | **+3.835** | **1.25e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5492** | 0.3740 | ±0.7481 | **-4.142** | **3.44e-05** | *** |
| Site: UCSD (vs UAB) | -0.4259 | 0.2195 | ±0.4390 | -1.940 | 0.0523 | . |
| Site: UW (vs UAB) | -0.2520 | 0.2009 | ±0.4018 | -1.255 | 0.2096 |  |
| **Age (years)** | **-0.0498** | 0.0072 | ±0.0145 | **-6.885** | **5.78e-12** | *** |
| BMI (kg/m2) | -0.0104 | 0.0111 | ±0.0223 | -0.933 | 0.3507 |  |
| Hypertension | -0.1871 | 0.1731 | ±0.3462 | -1.081 | 0.2798 |  |
| High cholesterol | +0.2307 | 0.1612 | ±0.3225 | +1.431 | 0.1524 |  |
| Kidney disease | -0.1645 | 0.3410 | ±0.6820 | -0.482 | 0.6295 |  |
| **Circulatory disease** | **-0.6953** | 0.2566 | ±0.5132 | **-2.710** | **0.0067** | ** |
| **Avg. daily range (mg/dL)** | **-0.0071** | 0.0033 | ±0.0067 | **-2.137** | **0.0326** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1271**, R² = **0.1056**, Adj R² = **0.0978**, F-statistic = **13.52** (p = **1.01e-24**), Residual SE = **2.735** on **1259** df, AIC = **6176.4**, BIC = **6238.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.6729** | 0.6388 | ±1.2777 | **+46.448** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6094** | 0.1615 | ±0.3229 | **+3.775** | **1.60e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5628** | 0.3768 | ±0.7535 | **-4.148** | **3.35e-05** | *** |
| Site: UCSD (vs UAB) | -0.4111 | 0.2211 | ±0.4423 | -1.859 | 0.0630 | . |
| Site: UW (vs UAB) | -0.2582 | 0.2017 | ±0.4034 | -1.280 | 0.2005 |  |
| **Age (years)** | **-0.0507** | 0.0073 | ±0.0145 | **-6.992** | **2.72e-12** | *** |
| BMI (kg/m2) | -0.0086 | 0.0112 | ±0.0224 | -0.771 | 0.4410 |  |
| Hypertension | -0.2095 | 0.1731 | ±0.3462 | -1.210 | 0.2261 |  |
| High cholesterol | +0.2433 | 0.1619 | ±0.3239 | +1.502 | 0.1330 |  |
| Kidney disease | -0.2095 | 0.3424 | ±0.6848 | -0.612 | 0.5406 |  |
| **Circulatory disease** | **-0.7113** | 0.2551 | ±0.5101 | **-2.788** | **0.0053** | ** |
| SD of daily means (mg/dL) | -0.0211 | 0.0324 | ±0.0648 | -0.653 | 0.5139 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1271**, R² = **0.1178**, Adj R² = **0.1100**, F-statistic = **15.28** (p = **3.00e-28**), Residual SE = **2.716** on **1259** df, AIC = **6159.0**, BIC = **6220.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.9366** | 1.3795 | ±2.7589 | **+18.802** | **7.30e-79** | *** |
| **Education: graduate level (vs college)** | **+0.6251** | 0.1608 | ±0.3216 | **+3.887** | **1.01e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5182** | 0.3655 | ±0.7309 | **-4.154** | **3.26e-05** | *** |
| **Site: UCSD (vs UAB)** | **-0.4486** | 0.2182 | ±0.4363 | **-2.056** | **0.0398** | * |
| Site: UW (vs UAB) | -0.2575 | 0.1992 | ±0.3985 | -1.292 | 0.1962 |  |
| **Age (years)** | **-0.0504** | 0.0072 | ±0.0144 | **-6.979** | **2.97e-12** | *** |
| BMI (kg/m2) | -0.0078 | 0.0113 | ±0.0225 | -0.696 | 0.4865 |  |
| Hypertension | -0.1748 | 0.1718 | ±0.3436 | -1.018 | 0.3089 |  |
| High cholesterol | +0.2536 | 0.1607 | ±0.3215 | +1.578 | 0.1146 |  |
| Kidney disease | -0.1494 | 0.3363 | ±0.6726 | -0.444 | 0.6569 |  |
| **Circulatory disease** | **-0.6694** | 0.2517 | ±0.5034 | **-2.660** | **0.0078** | ** |
| **Time in range 70-180, pooled (%)** | **+0.0369** | 0.0124 | ±0.0248 | **+2.979** | **0.0029** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1271**, R² = **0.1175**, Adj R² = **0.1098**, F-statistic = **15.23** (p = **3.65e-28**), Residual SE = **2.717** on **1259** df, AIC = **6159.5**, BIC = **6221.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.9747** | 1.3818 | ±2.7635 | **+18.798** | **7.83e-79** | *** |
| **Education: graduate level (vs college)** | **+0.6253** | 0.1609 | ±0.3218 | **+3.887** | **1.02e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5227** | 0.3655 | ±0.7311 | **-4.166** | **3.10e-05** | *** |
| **Site: UCSD (vs UAB)** | **-0.4460** | 0.2183 | ±0.4365 | **-2.044** | **0.0410** | * |
| Site: UW (vs UAB) | -0.2583 | 0.1993 | ±0.3986 | -1.296 | 0.1949 |  |
| **Age (years)** | **-0.0504** | 0.0072 | ±0.0144 | **-6.969** | **3.19e-12** | *** |
| BMI (kg/m2) | -0.0077 | 0.0113 | ±0.0225 | -0.681 | 0.4957 |  |
| Hypertension | -0.1763 | 0.1718 | ±0.3436 | -1.026 | 0.3048 |  |
| High cholesterol | +0.2554 | 0.1608 | ±0.3217 | +1.588 | 0.1123 |  |
| Kidney disease | -0.1496 | 0.3365 | ±0.6731 | -0.445 | 0.6567 |  |
| **Circulatory disease** | **-0.6699** | 0.2518 | ±0.5036 | **-2.661** | **0.0078** | ** |
| **Avg. daily time in range 70-180 (%)** | **+0.0364** | 0.0124 | ±0.0247 | **+2.944** | **0.0032** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1271**, R² = **0.1083**, Adj R² = **0.1005**, F-statistic = **13.89** (p = **1.75e-25**), Residual SE = **2.731** on **1259** df, AIC = **6172.6**, BIC = **6234.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.3831** | 0.6177 | ±1.2355 | **+47.565** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6246** | 0.1607 | ±0.3215 | **+3.886** | **1.02e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5230** | 0.3748 | ±0.7495 | **-4.064** | **4.83e-05** | *** |
| Site: UCSD (vs UAB) | -0.3494 | 0.2252 | ±0.4505 | -1.551 | 0.1209 |  |
| Site: UW (vs UAB) | -0.2370 | 0.2031 | ±0.4062 | -1.167 | 0.2432 |  |
| **Age (years)** | **-0.0500** | 0.0072 | ±0.0145 | **-6.908** | **4.90e-12** | *** |
| BMI (kg/m2) | -0.0103 | 0.0110 | ±0.0220 | -0.936 | 0.3493 |  |
| Hypertension | -0.2127 | 0.1729 | ±0.3458 | -1.230 | 0.2187 |  |
| High cholesterol | +0.2586 | 0.1616 | ±0.3231 | +1.600 | 0.1095 |  |
| Kidney disease | -0.2087 | 0.3447 | ±0.6893 | -0.605 | 0.5449 |  |
| **Circulatory disease** | **-0.7529** | 0.2574 | ±0.5147 | **-2.925** | **0.0034** | ** |
| **Any reading < 54 during wear (0/1)** | **+0.3559** | 0.1636 | ±0.3272 | **+2.175** | **0.0296** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1271**, R² = **0.1051**, Adj R² = **0.0973**, F-statistic = **13.45** (p = **1.38e-24**), Residual SE = **2.736** on **1259** df, AIC = **6177.1**, BIC = **6238.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5381** | 0.6178 | ±1.2356 | **+47.812** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6100** | 0.1613 | ±0.3226 | **+3.782** | **1.56e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5577** | 0.3780 | ±0.7559 | **-4.121** | **3.77e-05** | *** |
| Site: UCSD (vs UAB) | -0.3932 | 0.2238 | ±0.4476 | -1.757 | 0.0789 | . |
| Site: UW (vs UAB) | -0.2539 | 0.2034 | ±0.4069 | -1.248 | 0.2119 |  |
| **Age (years)** | **-0.0507** | 0.0073 | ±0.0145 | **-6.991** | **2.73e-12** | *** |
| BMI (kg/m2) | -0.0093 | 0.0111 | ±0.0222 | -0.837 | 0.4027 |  |
| Hypertension | -0.2101 | 0.1733 | ±0.3467 | -1.212 | 0.2254 |  |
| High cholesterol | +0.2444 | 0.1619 | ±0.3237 | +1.510 | 0.1311 |  |
| Kidney disease | -0.2128 | 0.3443 | ±0.6886 | -0.618 | 0.5365 |  |
| **Circulatory disease** | **-0.7193** | 0.2566 | ±0.5131 | **-2.804** | **0.0050** | ** |
| Time < 54 (%) | +0.0502 | 0.1398 | ±0.2795 | +0.359 | 0.7197 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1271**, R² = **0.1051**, Adj R² = **0.0973**, F-statistic = **13.45** (p = **1.37e-24**), Residual SE = **2.736** on **1259** df, AIC = **6177.1**, BIC = **6238.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5425** | 0.6141 | ±1.2281 | **+48.109** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6106** | 0.1613 | ±0.3226 | **+3.786** | **1.53e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5574** | 0.3784 | ±0.7568 | **-4.116** | **3.86e-05** | *** |
| Site: UCSD (vs UAB) | -0.3937 | 0.2231 | ±0.4461 | -1.765 | 0.0776 | . |
| Site: UW (vs UAB) | -0.2525 | 0.2034 | ±0.4069 | -1.241 | 0.2146 |  |
| **Age (years)** | **-0.0508** | 0.0072 | ±0.0145 | **-7.006** | **2.46e-12** | *** |
| BMI (kg/m2) | -0.0093 | 0.0111 | ±0.0222 | -0.839 | 0.4014 |  |
| Hypertension | -0.2089 | 0.1733 | ±0.3467 | -1.205 | 0.2280 |  |
| High cholesterol | +0.2441 | 0.1618 | ±0.3237 | +1.508 | 0.1315 |  |
| Kidney disease | -0.2130 | 0.3439 | ±0.6877 | -0.619 | 0.5357 |  |
| **Circulatory disease** | **-0.7190** | 0.2567 | ±0.5133 | **-2.802** | **0.0051** | ** |
| Avg. daily time < 54 (%) | +0.0720 | 0.1679 | ±0.3358 | +0.429 | 0.6680 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1271**, R² = **0.1051**, Adj R² = **0.0973**, F-statistic = **13.44** (p = **1.43e-24**), Residual SE = **2.736** on **1259** df, AIC = **6177.2**, BIC = **6238.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5420** | 0.6169 | ±1.2338 | **+47.889** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6110** | 0.1613 | ±0.3225 | **+3.789** | **1.51e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5572** | 0.3782 | ±0.7565 | **-4.117** | **3.84e-05** | *** |
| Site: UCSD (vs UAB) | -0.3978 | 0.2226 | ±0.4453 | -1.787 | 0.0739 | . |
| Site: UW (vs UAB) | -0.2559 | 0.2030 | ±0.4061 | -1.261 | 0.2075 |  |
| **Age (years)** | **-0.0507** | 0.0073 | ±0.0145 | **-6.989** | **2.76e-12** | *** |
| BMI (kg/m2) | -0.0094 | 0.0111 | ±0.0221 | -0.852 | 0.3941 |  |
| Hypertension | -0.2102 | 0.1733 | ±0.3466 | -1.213 | 0.2251 |  |
| High cholesterol | +0.2426 | 0.1618 | ±0.3236 | +1.499 | 0.1339 |  |
| Kidney disease | -0.2112 | 0.3436 | ±0.6872 | -0.615 | 0.5387 |  |
| **Circulatory disease** | **-0.7195** | 0.2568 | ±0.5135 | **-2.802** | **0.0051** | ** |
| Time 54-69, pooled (%) | +0.0144 | 0.0435 | ±0.0870 | +0.332 | 0.7402 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1271**, R² = **0.1051**, Adj R² = **0.0973**, F-statistic = **13.44** (p = **1.44e-24**), Residual SE = **2.736** on **1259** df, AIC = **6177.2**, BIC = **6239.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5472** | 0.6153 | ±1.2306 | **+48.021** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6107** | 0.1614 | ±0.3227 | **+3.785** | **1.54e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5579** | 0.3786 | ±0.7572 | **-4.115** | **3.87e-05** | *** |
| Site: UCSD (vs UAB) | -0.3995 | 0.2220 | ±0.4441 | -1.799 | 0.0720 | . |
| Site: UW (vs UAB) | -0.2569 | 0.2028 | ±0.4057 | -1.266 | 0.2053 |  |
| **Age (years)** | **-0.0507** | 0.0073 | ±0.0145 | **-6.997** | **2.62e-12** | *** |
| BMI (kg/m2) | -0.0094 | 0.0111 | ±0.0221 | -0.850 | 0.3953 |  |
| Hypertension | -0.2104 | 0.1734 | ±0.3468 | -1.213 | 0.2251 |  |
| High cholesterol | +0.2419 | 0.1617 | ±0.3235 | +1.496 | 0.1347 |  |
| Kidney disease | -0.2112 | 0.3434 | ±0.6869 | -0.615 | 0.5386 |  |
| **Circulatory disease** | **-0.7194** | 0.2568 | ±0.5135 | **-2.802** | **0.0051** | ** |
| Avg. daily time 54-69 (%) | +0.0115 | 0.0435 | ±0.0870 | +0.265 | 0.7912 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1271**, R² = **0.1051**, Adj R² = **0.0973**, F-statistic = **13.44** (p = **1.40e-24**), Residual SE = **2.736** on **1259** df, AIC = **6177.1**, BIC = **6238.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5364** | 0.6186 | ±1.2373 | **+47.745** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6113** | 0.1613 | ±0.3227 | **+3.789** | **1.51e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5558** | 0.3783 | ±0.7565 | **-4.113** | **3.91e-05** | *** |
| Site: UCSD (vs UAB) | -0.3953 | 0.2234 | ±0.4469 | -1.769 | 0.0769 | . |
| Site: UW (vs UAB) | -0.2540 | 0.2036 | ±0.4072 | -1.248 | 0.2121 |  |
| **Age (years)** | **-0.0507** | 0.0073 | ±0.0145 | **-6.987** | **2.81e-12** | *** |
| BMI (kg/m2) | -0.0094 | 0.0111 | ±0.0221 | -0.851 | 0.3950 |  |
| Hypertension | -0.2097 | 0.1733 | ±0.3466 | -1.210 | 0.2263 |  |
| High cholesterol | +0.2437 | 0.1619 | ±0.3239 | +1.505 | 0.1323 |  |
| Kidney disease | -0.2116 | 0.3439 | ±0.6877 | -0.615 | 0.5383 |  |
| **Circulatory disease** | **-0.7195** | 0.2567 | ±0.5135 | **-2.803** | **0.0051** | ** |
| Time < 70 (%) | +0.0143 | 0.0363 | ±0.0726 | +0.396 | 0.6925 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1271**, R² = **0.1051**, Adj R² = **0.0973**, F-statistic = **13.44** (p = **1.42e-24**), Residual SE = **2.736** on **1259** df, AIC = **6177.1**, BIC = **6238.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5435** | 0.6157 | ±1.2315 | **+47.981** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6112** | 0.1614 | ±0.3228 | **+3.788** | **1.52e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5566** | 0.3787 | ±0.7574 | **-4.110** | **3.95e-05** | *** |
| Site: UCSD (vs UAB) | -0.3977 | 0.2225 | ±0.4450 | -1.788 | 0.0739 | . |
| Site: UW (vs UAB) | -0.2551 | 0.2033 | ±0.4065 | -1.255 | 0.2095 |  |
| **Age (years)** | **-0.0507** | 0.0073 | ±0.0145 | **-6.998** | **2.60e-12** | *** |
| BMI (kg/m2) | -0.0094 | 0.0111 | ±0.0221 | -0.850 | 0.3954 |  |
| Hypertension | -0.2097 | 0.1734 | ±0.3469 | -1.209 | 0.2266 |  |
| High cholesterol | +0.2428 | 0.1618 | ±0.3236 | +1.500 | 0.1336 |  |
| Kidney disease | -0.2114 | 0.3435 | ±0.6871 | -0.615 | 0.5382 |  |
| **Circulatory disease** | **-0.7194** | 0.2568 | ±0.5136 | **-2.801** | **0.0051** | ** |
| Avg. daily time < 70 (%) | +0.0126 | 0.0374 | ±0.0749 | +0.338 | 0.7355 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1271**, R² = **0.1139**, Adj R² = **0.1061**, F-statistic = **14.71** (p = **4.10e-27**), Residual SE = **2.722** on **1259** df, AIC = **6164.6**, BIC = **6226.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0292** | 3.2772 | ±6.5544 | **+7.332** | **2.26e-13** | *** |
| **Education: graduate level (vs college)** | **+0.6122** | 0.1616 | ±0.3231 | **+3.789** | **1.51e-04** | *** |
| **Education: high school or below (vs college)** | **-1.4913** | 0.3682 | ±0.7363 | **-4.051** | **5.11e-05** | *** |
| Site: UCSD (vs UAB) | -0.4249 | 0.2198 | ±0.4397 | -1.933 | 0.0533 | . |
| Site: UW (vs UAB) | -0.2742 | 0.2009 | ±0.4017 | -1.365 | 0.1723 |  |
| **Age (years)** | **-0.0511** | 0.0072 | ±0.0145 | **-7.064** | **1.62e-12** | *** |
| BMI (kg/m2) | -0.0093 | 0.0111 | ±0.0221 | -0.844 | 0.3987 |  |
| Hypertension | -0.2062 | 0.1726 | ±0.3451 | -1.195 | 0.2322 |  |
| High cholesterol | +0.2300 | 0.1598 | ±0.3196 | +1.439 | 0.1502 |  |
| Kidney disease | -0.2020 | 0.3396 | ±0.6793 | -0.595 | 0.5520 |  |
| **Circulatory disease** | **-0.6629** | 0.2522 | ±0.5045 | **-2.628** | **0.0086** | ** |
| Time 54-250, pooled (%) | +0.0558 | 0.0324 | ±0.0647 | +1.726 | 0.0843 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1271**, R² = **0.1139**, Adj R² = **0.1062**, F-statistic = **14.71** (p = **4.00e-27**), Residual SE = **2.722** on **1259** df, AIC = **6164.6**, BIC = **6226.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8852** | 3.4104 | ±6.8208 | **+7.004** | **2.49e-12** | *** |
| **Education: graduate level (vs college)** | **+0.6124** | 0.1616 | ±0.3232 | **+3.789** | **1.51e-04** | *** |
| **Education: high school or below (vs college)** | **-1.4887** | 0.3679 | ±0.7359 | **-4.046** | **5.21e-05** | *** |
| Site: UCSD (vs UAB) | -0.4219 | 0.2198 | ±0.4396 | -1.919 | 0.0549 | . |
| Site: UW (vs UAB) | -0.2725 | 0.2008 | ±0.4016 | -1.357 | 0.1748 |  |
| **Age (years)** | **-0.0510** | 0.0072 | ±0.0145 | **-7.050** | **1.79e-12** | *** |
| BMI (kg/m2) | -0.0092 | 0.0111 | ±0.0221 | -0.832 | 0.4056 |  |
| Hypertension | -0.2063 | 0.1726 | ±0.3452 | -1.195 | 0.2321 |  |
| High cholesterol | +0.2309 | 0.1599 | ±0.3197 | +1.444 | 0.1486 |  |
| Kidney disease | -0.2036 | 0.3401 | ±0.6802 | -0.599 | 0.5495 |  |
| **Circulatory disease** | **-0.6619** | 0.2521 | ±0.5043 | **-2.625** | **0.0087** | ** |
| Avg. daily time 54-250 (%) | +0.0571 | 0.0336 | ±0.0672 | +1.700 | 0.0891 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1271**, R² = **0.1133**, Adj R² = **0.1055**, F-statistic = **14.62** (p = **6.10e-27**), Residual SE = **2.723** on **1259** df, AIC = **6165.5**, BIC = **6227.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5513** | 0.6141 | ±1.2281 | **+48.124** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6320** | 0.1605 | ±0.3210 | **+3.937** | **8.24e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5498** | 0.3741 | ±0.7482 | **-4.143** | **3.43e-05** | *** |
| Site: UCSD (vs UAB) | -0.4257 | 0.2187 | ±0.4374 | -1.946 | 0.0516 | . |
| Site: UW (vs UAB) | -0.2321 | 0.2010 | ±0.4020 | -1.155 | 0.2482 |  |
| **Age (years)** | **-0.0499** | 0.0072 | ±0.0144 | **-6.915** | **4.68e-12** | *** |
| BMI (kg/m2) | -0.0078 | 0.0113 | ±0.0226 | -0.694 | 0.4877 |  |
| Hypertension | -0.1676 | 0.1726 | ±0.3452 | -0.971 | 0.3316 |  |
| High cholesterol | +0.2709 | 0.1623 | ±0.3245 | +1.670 | 0.0950 | . |
| Kidney disease | -0.1450 | 0.3376 | ±0.6752 | -0.430 | 0.6675 |  |
| **Circulatory disease** | **-0.7048** | 0.2543 | ±0.5087 | **-2.771** | **0.0056** | ** |
| **Time 181-250, pooled (%)** | **-0.0435** | 0.0142 | ±0.0284 | **-3.059** | **0.0022** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1271**, R² = **0.1131**, Adj R² = **0.1053**, F-statistic = **14.59** (p = **7.05e-27**), Residual SE = **2.724** on **1259** df, AIC = **6165.8**, BIC = **6227.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5496** | 0.6143 | ±1.2286 | **+48.102** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6324** | 0.1606 | ±0.3211 | **+3.939** | **8.19e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5542** | 0.3742 | ±0.7483 | **-4.154** | **3.27e-05** | *** |
| Site: UCSD (vs UAB) | -0.4283 | 0.2187 | ±0.4374 | -1.958 | 0.0502 | . |
| Site: UW (vs UAB) | -0.2352 | 0.2009 | ±0.4017 | -1.171 | 0.2416 |  |
| **Age (years)** | **-0.0500** | 0.0072 | ±0.0144 | **-6.926** | **4.32e-12** | *** |
| BMI (kg/m2) | -0.0077 | 0.0113 | ±0.0226 | -0.686 | 0.4926 |  |
| Hypertension | -0.1689 | 0.1726 | ±0.3453 | -0.978 | 0.3279 |  |
| High cholesterol | +0.2710 | 0.1622 | ±0.3244 | +1.671 | 0.0948 | . |
| Kidney disease | -0.1442 | 0.3372 | ±0.6744 | -0.428 | 0.6690 |  |
| **Circulatory disease** | **-0.7044** | 0.2546 | ±0.5092 | **-2.767** | **0.0057** | ** |
| **Avg. daily time 181-250 (%)** | **-0.0424** | 0.0140 | ±0.0280 | **-3.026** | **0.0025** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1271**, R² = **0.1182**, Adj R² = **0.1104**, F-statistic = **15.33** (p = **2.29e-28**), Residual SE = **2.716** on **1259** df, AIC = **6158.5**, BIC = **6220.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5751** | 0.6132 | ±1.2264 | **+48.232** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6320** | 0.1608 | ±0.3217 | **+3.930** | **8.50e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5002** | 0.3656 | ±0.7311 | **-4.104** | **4.06e-05** | *** |
| **Site: UCSD (vs UAB)** | **-0.4308** | 0.2180 | ±0.4359 | **-1.976** | **0.0481** | * |
| Site: UW (vs UAB) | -0.2400 | 0.1997 | ±0.3994 | -1.202 | 0.2294 |  |
| **Age (years)** | **-0.0502** | 0.0072 | ±0.0144 | **-6.955** | **3.51e-12** | *** |
| BMI (kg/m2) | -0.0080 | 0.0112 | ±0.0225 | -0.711 | 0.4769 |  |
| Hypertension | -0.1685 | 0.1720 | ±0.3440 | -0.979 | 0.3274 |  |
| High cholesterol | +0.2629 | 0.1612 | ±0.3225 | +1.630 | 0.1031 |  |
| Kidney disease | -0.1488 | 0.3372 | ±0.6744 | -0.441 | 0.6590 |  |
| **Circulatory disease** | **-0.6687** | 0.2520 | ±0.5040 | **-2.654** | **0.0080** | ** |
| **Time > 180 (%)** | **-0.0375** | 0.0126 | ±0.0251 | **-2.988** | **0.0028** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1271**, R² = **0.1178**, Adj R² = **0.1101**, F-statistic = **15.28** (p = **2.90e-28**), Residual SE = **2.716** on **1259** df, AIC = **6159.0**, BIC = **6220.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5695** | 0.6136 | ±1.2272 | **+48.190** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6326** | 0.1609 | ±0.3218 | **+3.932** | **8.42e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5050** | 0.3658 | ±0.7317 | **-4.114** | **3.89e-05** | *** |
| **Site: UCSD (vs UAB)** | **-0.4331** | 0.2181 | ±0.4361 | **-1.986** | **0.0470** | * |
| Site: UW (vs UAB) | -0.2420 | 0.1997 | ±0.3995 | -1.211 | 0.2257 |  |
| **Age (years)** | **-0.0503** | 0.0072 | ±0.0144 | **-6.960** | **3.40e-12** | *** |
| BMI (kg/m2) | -0.0078 | 0.0113 | ±0.0225 | -0.697 | 0.4856 |  |
| Hypertension | -0.1693 | 0.1720 | ±0.3440 | -0.984 | 0.3249 |  |
| High cholesterol | +0.2629 | 0.1613 | ±0.3225 | +1.630 | 0.1031 |  |
| Kidney disease | -0.1486 | 0.3371 | ±0.6742 | -0.441 | 0.6593 |  |
| **Circulatory disease** | **-0.6690** | 0.2521 | ±0.5043 | **-2.653** | **0.0080** | ** |
| **Avg. daily time > 180 (%)** | **-0.0369** | 0.0125 | ±0.0250 | **-2.951** | **0.0032** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1271**, R² = **0.1133**, Adj R² = **0.1056**, F-statistic = **14.63** (p = **5.95e-27**), Residual SE = **2.723** on **1259** df, AIC = **6165.4**, BIC = **6227.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5230** | 0.6156 | ±1.2313 | **+47.956** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6120** | 0.1612 | ±0.3224 | **+3.797** | **1.46e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5177** | 0.3667 | ±0.7335 | **-4.138** | **3.50e-05** | *** |
| Site: UCSD (vs UAB) | -0.4171 | 0.2197 | ±0.4394 | -1.899 | 0.0576 | . |
| Site: UW (vs UAB) | -0.2491 | 0.2009 | ±0.4017 | -1.240 | 0.2149 |  |
| **Age (years)** | **-0.0510** | 0.0073 | ±0.0145 | **-7.035** | **2.00e-12** | *** |
| BMI (kg/m2) | -0.0061 | 0.0114 | ±0.0227 | -0.534 | 0.5935 |  |
| Hypertension | -0.1955 | 0.1727 | ±0.3453 | -1.132 | 0.2576 |  |
| High cholesterol | +0.2684 | 0.1626 | ±0.3251 | +1.651 | 0.0988 | . |
| Kidney disease | -0.2137 | 0.3388 | ±0.6777 | -0.631 | 0.5282 |  |
| **Circulatory disease** | **-0.7032** | 0.2524 | ±0.5048 | **-2.786** | **0.0053** | ** |
| **Nocturnal time > 180 (%)** | **-0.0313** | 0.0137 | ±0.0273 | **-2.293** | **0.0219** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1271**, R² = **0.1089**, Adj R² = **0.1011**, F-statistic = **13.99** (p = **1.14e-25**), Residual SE = **2.730** on **1259** df, AIC = **6171.7**, BIC = **6233.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.6693** | 0.6092 | ±1.2184 | **+48.704** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6062** | 0.1609 | ±0.3218 | **+3.768** | **1.65e-04** | *** |
| **Education: high school or below (vs college)** | **-1.5637** | 0.3771 | ±0.7541 | **-4.147** | **3.37e-05** | *** |
| Site: UCSD (vs UAB) | -0.4142 | 0.2193 | ±0.4386 | -1.889 | 0.0589 | . |
| Site: UW (vs UAB) | -0.2554 | 0.2009 | ±0.4018 | -1.271 | 0.2037 |  |
| **Age (years)** | **-0.0504** | 0.0072 | ±0.0145 | **-6.965** | **3.28e-12** | *** |
| BMI (kg/m2) | -0.0112 | 0.0110 | ±0.0221 | -1.016 | 0.3095 |  |
| Hypertension | -0.1841 | 0.1726 | ±0.3452 | -1.067 | 0.2861 |  |
| High cholesterol | +0.2482 | 0.1614 | ±0.3229 | +1.538 | 0.1241 |  |
| Kidney disease | -0.2034 | 0.3464 | ±0.6927 | -0.587 | 0.5570 |  |
| **Circulatory disease** | **-0.7198** | 0.2573 | ±0.5145 | **-2.798** | **0.0051** | ** |
| **Any reading > 250 during wear (0/1)** | **-0.4572** | 0.2262 | ±0.4524 | **-2.021** | **0.0433** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1271**, R² = **0.1142**, Adj R² = **0.1064**, F-statistic = **14.75** (p = **3.33e-27**), Residual SE = **2.722** on **1259** df, AIC = **6164.2**, BIC = **6225.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5928** | 0.6100 | ±1.2200 | **+48.514** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6137** | 0.1616 | ±0.3232 | **+3.798** | **1.46e-04** | *** |
| **Education: high school or below (vs college)** | **-1.4843** | 0.3685 | ±0.7371 | **-4.027** | **5.64e-05** | *** |
| Site: UCSD (vs UAB) | -0.4150 | 0.2195 | ±0.4390 | -1.891 | 0.0587 | . |
| Site: UW (vs UAB) | -0.2668 | 0.2006 | ±0.4012 | -1.330 | 0.1835 |  |
| **Age (years)** | **-0.0511** | 0.0072 | ±0.0145 | **-7.060** | **1.66e-12** | *** |
| BMI (kg/m2) | -0.0093 | 0.0111 | ±0.0221 | -0.839 | 0.4014 |  |
| Hypertension | -0.2040 | 0.1726 | ±0.3453 | -1.181 | 0.2374 |  |
| High cholesterol | +0.2344 | 0.1600 | ±0.3200 | +1.465 | 0.1429 |  |
| Kidney disease | -0.2033 | 0.3402 | ±0.6803 | -0.598 | 0.5500 |  |
| **Circulatory disease** | **-0.6615** | 0.2522 | ±0.5044 | **-2.623** | **0.0087** | ** |
| Time > 250 (%) | -0.0571 | 0.0329 | ±0.0658 | -1.737 | 0.0823 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1271**, R² = **0.1141**, Adj R² = **0.1064**, F-statistic = **14.75** (p = **3.43e-27**), Residual SE = **2.722** on **1259** df, AIC = **6164.2**, BIC = **6226.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.5876** | 0.6102 | ±1.2203 | **+48.491** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.6139** | 0.1616 | ±0.3232 | **+3.799** | **1.46e-04** | *** |
| **Education: high school or below (vs college)** | **-1.4834** | 0.3683 | ±0.7367 | **-4.027** | **5.64e-05** | *** |
| Site: UCSD (vs UAB) | -0.4152 | 0.2196 | ±0.4391 | -1.891 | 0.0586 | . |
| Site: UW (vs UAB) | -0.2661 | 0.2006 | ±0.4012 | -1.326 | 0.1848 |  |
| **Age (years)** | **-0.0510** | 0.0072 | ±0.0145 | **-7.055** | **1.73e-12** | *** |
| BMI (kg/m2) | -0.0092 | 0.0111 | ±0.0221 | -0.829 | 0.4069 |  |
| Hypertension | -0.2038 | 0.1727 | ±0.3453 | -1.180 | 0.2379 |  |
| High cholesterol | +0.2339 | 0.1600 | ±0.3200 | +1.462 | 0.1438 |  |
| Kidney disease | -0.2047 | 0.3403 | ±0.6807 | -0.601 | 0.5476 |  |
| **Circulatory disease** | **-0.6607** | 0.2521 | ±0.5043 | **-2.620** | **0.0088** | ** |
| Avg. daily time > 250 (%) | -0.0581 | 0.0339 | ±0.0678 | -1.712 | 0.0868 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 1,271; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0601**, LLR χ² = **98.48** (p = **1.10e-16**), AUC = **0.6599**, AIC = **1560.7**, BIC = **1617.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1201** | 0.5009 | ±1.0018 | **-6.229** | **4.69e-10** | 0.0442 | *** |
| **Education: graduate level (vs college)** | **-0.5074** | 0.1325 | ±0.2651 | **-3.828** | **1.29e-04** | 0.6021 | *** |
| **Education: high school or below (vs college)** | **+0.8474** | 0.2215 | ±0.4430 | **+3.826** | **1.30e-04** | 2.3336 | *** |
| **Site: UCSD (vs UAB)** | **+0.3403** | 0.1643 | ±0.3285 | **+2.072** | **0.0383** | 1.4054 | * |
| Site: UW (vs UAB) | +0.1516 | 0.1554 | ±0.3108 | +0.975 | 0.3294 | 1.1637 |  |
| **Age (years)** | **+0.0337** | 0.0058 | ±0.0117 | **+5.771** | **7.87e-09** | 1.0343 | *** |
| BMI (kg/m2) | +0.0123 | 0.0092 | ±0.0184 | +1.337 | 0.1814 | 1.0123 |  |
| Hypertension | +0.0461 | 0.1363 | ±0.2726 | +0.338 | 0.7353 | 1.0472 |  |
| High cholesterol | +0.0055 | 0.1287 | ±0.2575 | +0.043 | 0.9661 | 1.0055 |  |
| Kidney disease | -0.1846 | 0.2469 | ±0.4938 | -0.748 | 0.4545 | 0.8314 |  |
| **Circulatory disease** | **+0.3821** | 0.1795 | ±0.3590 | **+2.128** | **0.0333** | 1.4653 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0612**, LLR χ² = **100.26** (p = **1.59e-16**), AUC = **0.6616**, AIC = **1560.9**, BIC = **1622.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.9219** | 0.7942 | ±1.5883 | **-4.938** | **7.87e-07** | 0.0198 | *** |
| **Education: graduate level (vs college)** | **-0.5097** | 0.1326 | ±0.2653 | **-3.843** | **1.21e-04** | 0.6007 | *** |
| **Education: high school or below (vs college)** | **+0.8294** | 0.2223 | ±0.4447 | **+3.730** | **1.91e-04** | 2.2919 | *** |
| **Site: UCSD (vs UAB)** | **+0.3377** | 0.1644 | ±0.3288 | **+2.054** | **0.0400** | 1.4017 | * |
| Site: UW (vs UAB) | +0.1458 | 0.1557 | ±0.3115 | +0.936 | 0.3492 | 1.1569 |  |
| **Age (years)** | **+0.0332** | 0.0059 | ±0.0117 | **+5.657** | **1.54e-08** | 1.0337 | *** |
| BMI (kg/m2) | +0.0111 | 0.0092 | ±0.0184 | +1.209 | 0.2265 | 1.0112 |  |
| Hypertension | +0.0379 | 0.1365 | ±0.2731 | +0.277 | 0.7816 | 1.0386 |  |
| High cholesterol | -0.0103 | 0.1294 | ±0.2587 | -0.079 | 0.9368 | 0.9898 |  |
| Kidney disease | -0.1819 | 0.2469 | ±0.4939 | -0.736 | 0.4615 | 0.8337 |  |
| **Circulatory disease** | **+0.3704** | 0.1799 | ±0.3598 | **+2.059** | **0.0395** | 1.4483 | * |
| HbA1c (%) | +0.1560 | 0.1197 | ±0.2394 | +1.304 | 0.1924 | 1.1689 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0629**, LLR χ² = **102.92** (p = **4.70e-17**), AUC = **0.6640**, AIC = **1558.2**, BIC = **1620.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.8748** | 0.6212 | ±1.2424 | **-6.237** | **4.45e-10** | 0.0208 | *** |
| **Education: graduate level (vs college)** | **-0.5253** | 0.1330 | ±0.2661 | **-3.948** | **7.88e-05** | 0.5914 | *** |
| **Education: high school or below (vs college)** | **+0.8193** | 0.2225 | ±0.4451 | **+3.681** | **2.32e-04** | 2.2688 | *** |
| **Site: UCSD (vs UAB)** | **+0.3452** | 0.1645 | ±0.3290 | **+2.098** | **0.0359** | 1.4122 | * |
| Site: UW (vs UAB) | +0.1281 | 0.1562 | ±0.3125 | +0.820 | 0.4123 | 1.1366 |  |
| **Age (years)** | **+0.0333** | 0.0058 | ±0.0117 | **+5.700** | **1.20e-08** | 1.0339 | *** |
| BMI (kg/m2) | +0.0113 | 0.0092 | ±0.0184 | +1.225 | 0.2207 | 1.0113 |  |
| Hypertension | +0.0222 | 0.1371 | ±0.2742 | +0.162 | 0.8714 | 1.0224 |  |
| High cholesterol | -0.0043 | 0.1290 | ±0.2581 | -0.033 | 0.9736 | 0.9957 |  |
| Kidney disease | -0.2073 | 0.2477 | ±0.4954 | -0.837 | 0.4026 | 0.8128 |  |
| **Circulatory disease** | **+0.3642** | 0.1801 | ±0.3602 | **+2.022** | **0.0432** | 1.4393 | * |
| **Mean glucose (mg/dL)** | **+0.0069** | 0.0033 | ±0.0067 | **+2.070** | **0.0384** | 1.0070 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0629**, LLR χ² = **102.92** (p = **4.70e-17**), AUC = **0.6640**, AIC = **1558.2**, BIC = **1620.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.8343** | 0.9701 | ±1.9402 | **-4.983** | **6.25e-07** | 0.0080 | *** |
| **Education: graduate level (vs college)** | **-0.5253** | 0.1330 | ±0.2661 | **-3.948** | **7.88e-05** | 0.5914 | *** |
| **Education: high school or below (vs college)** | **+0.8193** | 0.2225 | ±0.4451 | **+3.681** | **2.32e-04** | 2.2688 | *** |
| **Site: UCSD (vs UAB)** | **+0.3452** | 0.1645 | ±0.3290 | **+2.098** | **0.0359** | 1.4122 | * |
| Site: UW (vs UAB) | +0.1281 | 0.1562 | ±0.3125 | +0.820 | 0.4123 | 1.1366 |  |
| **Age (years)** | **+0.0333** | 0.0058 | ±0.0117 | **+5.700** | **1.20e-08** | 1.0339 | *** |
| BMI (kg/m2) | +0.0113 | 0.0092 | ±0.0184 | +1.225 | 0.2207 | 1.0113 |  |
| Hypertension | +0.0222 | 0.1371 | ±0.2742 | +0.162 | 0.8714 | 1.0224 |  |
| High cholesterol | -0.0043 | 0.1290 | ±0.2581 | -0.033 | 0.9736 | 0.9957 |  |
| Kidney disease | -0.2073 | 0.2477 | ±0.4954 | -0.837 | 0.4026 | 0.8128 |  |
| **Circulatory disease** | **+0.3642** | 0.1801 | ±0.3602 | **+2.022** | **0.0432** | 1.4393 | * |
| **GMI (%)** | **+0.2899** | 0.1400 | ±0.2800 | **+2.070** | **0.0384** | 1.3363 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0615**, LLR χ² = **100.66** (p = **1.32e-16**), AUC = **0.6622**, AIC = **1560.5**, BIC = **1622.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.6106** | 0.6032 | ±1.2063 | **-5.986** | **2.15e-09** | 0.0270 | *** |
| **Education: graduate level (vs college)** | **-0.5161** | 0.1328 | ±0.2655 | **-3.888** | **1.01e-04** | 0.5968 | *** |
| **Education: high school or below (vs college)** | **+0.8268** | 0.2222 | ±0.4445 | **+3.720** | **1.99e-04** | 2.2859 | *** |
| **Site: UCSD (vs UAB)** | **+0.3374** | 0.1644 | ±0.3287 | **+2.053** | **0.0401** | 1.4013 | * |
| Site: UW (vs UAB) | +0.1373 | 0.1559 | ±0.3119 | +0.880 | 0.3787 | 1.1471 |  |
| **Age (years)** | **+0.0339** | 0.0058 | ±0.0117 | **+5.798** | **6.71e-09** | 1.0345 | *** |
| BMI (kg/m2) | +0.0104 | 0.0093 | ±0.0185 | +1.128 | 0.2593 | 1.0105 |  |
| Hypertension | +0.0340 | 0.1367 | ±0.2733 | +0.249 | 0.8034 | 1.0346 |  |
| High cholesterol | -0.0050 | 0.1290 | ±0.2580 | -0.039 | 0.9692 | 0.9950 |  |
| Kidney disease | -0.1875 | 0.2472 | ±0.4944 | -0.758 | 0.4482 | 0.8291 |  |
| **Circulatory disease** | **+0.3738** | 0.1798 | ±0.3597 | **+2.079** | **0.0376** | 1.4533 | * |
| Nocturnal mean 00-06h (mg/dL) | +0.0046 | 0.0031 | ±0.0063 | +1.465 | 0.1430 | 1.0046 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0613**, LLR χ² = **100.28** (p = **1.57e-16**), AUC = **0.6615**, AIC = **1560.9**, BIC = **1622.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3540** | 0.5310 | ±1.0620 | **-6.317** | **2.67e-10** | 0.0349 | *** |
| **Education: graduate level (vs college)** | **-0.5097** | 0.1327 | ±0.2653 | **-3.842** | **1.22e-04** | 0.6007 | *** |
| **Education: high school or below (vs college)** | **+0.8456** | 0.2217 | ±0.4435 | **+3.813** | **1.37e-04** | 2.3293 | *** |
| **Site: UCSD (vs UAB)** | **+0.3520** | 0.1646 | ±0.3292 | **+2.138** | **0.0325** | 1.4219 | * |
| Site: UW (vs UAB) | +0.1449 | 0.1556 | ±0.3113 | +0.931 | 0.3520 | 1.1559 |  |
| **Age (years)** | **+0.0333** | 0.0059 | ±0.0117 | **+5.683** | **1.32e-08** | 1.0338 | *** |
| BMI (kg/m2) | +0.0121 | 0.0092 | ±0.0183 | +1.319 | 0.1873 | 1.0122 |  |
| Hypertension | +0.0289 | 0.1371 | ±0.2741 | +0.211 | 0.8329 | 1.0293 |  |
| High cholesterol | +0.0077 | 0.1289 | ±0.2577 | +0.059 | 0.9527 | 1.0077 |  |
| Kidney disease | -0.2100 | 0.2478 | ±0.4956 | -0.847 | 0.3968 | 0.8106 |  |
| **Circulatory disease** | **+0.3715** | 0.1798 | ±0.3597 | **+2.066** | **0.0388** | 1.4500 | * |
| Glucose SD, pooled (mg/dL) | +0.0127 | 0.0094 | ±0.0188 | +1.347 | 0.1781 | 1.0128 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0614**, LLR χ² = **100.58** (p = **1.37e-16**), AUC = **0.6616**, AIC = **1560.6**, BIC = **1622.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3541** | 0.5269 | ±1.0539 | **-6.365** | **1.95e-10** | 0.0349 | *** |
| **Education: graduate level (vs college)** | **-0.5115** | 0.1327 | ±0.2654 | **-3.854** | **1.16e-04** | 0.5996 | *** |
| **Education: high school or below (vs college)** | **+0.8449** | 0.2217 | ±0.4434 | **+3.811** | **1.39e-04** | 2.3277 | *** |
| **Site: UCSD (vs UAB)** | **+0.3517** | 0.1646 | ±0.3291 | **+2.137** | **0.0326** | 1.4214 | * |
| Site: UW (vs UAB) | +0.1428 | 0.1557 | ±0.3114 | +0.917 | 0.3591 | 1.1535 |  |
| **Age (years)** | **+0.0332** | 0.0059 | ±0.0117 | **+5.664** | **1.48e-08** | 1.0337 | *** |
| BMI (kg/m2) | +0.0119 | 0.0092 | ±0.0183 | +1.299 | 0.1940 | 1.0120 |  |
| Hypertension | +0.0278 | 0.1371 | ±0.2741 | +0.203 | 0.8393 | 1.0282 |  |
| High cholesterol | +0.0070 | 0.1289 | ±0.2578 | +0.054 | 0.9567 | 1.0070 |  |
| Kidney disease | -0.2130 | 0.2479 | ±0.4957 | -0.859 | 0.3901 | 0.8082 |  |
| **Circulatory disease** | **+0.3711** | 0.1798 | ±0.3596 | **+2.064** | **0.0391** | 1.4493 | * |
| Avg. daily SD (mg/dL) | +0.0146 | 0.0101 | ±0.0201 | +1.456 | 0.1453 | 1.0147 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0603**, LLR χ² = **98.72** (p = **3.21e-16**), AUC = **0.6600**, AIC = **1562.4**, BIC = **1624.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2461** | 0.5631 | ±1.1261 | **-5.765** | **8.17e-09** | 0.0389 | *** |
| **Education: graduate level (vs college)** | **-0.5054** | 0.1326 | ±0.2652 | **-3.811** | **1.38e-04** | 0.6032 | *** |
| **Education: high school or below (vs college)** | **+0.8513** | 0.2217 | ±0.4434 | **+3.840** | **1.23e-04** | 2.3428 | *** |
| **Site: UCSD (vs UAB)** | **+0.3454** | 0.1646 | ±0.3292 | **+2.098** | **0.0359** | 1.4125 | * |
| Site: UW (vs UAB) | +0.1525 | 0.1555 | ±0.3109 | +0.981 | 0.3267 | 1.1647 |  |
| **Age (years)** | **+0.0335** | 0.0059 | ±0.0117 | **+5.733** | **9.88e-09** | 1.0341 | *** |
| BMI (kg/m2) | +0.0123 | 0.0092 | ±0.0183 | +1.344 | 0.1790 | 1.0124 |  |
| Hypertension | +0.0420 | 0.1366 | ±0.2732 | +0.307 | 0.7586 | 1.0429 |  |
| High cholesterol | +0.0085 | 0.1289 | ±0.2578 | +0.066 | 0.9475 | 1.0085 |  |
| Kidney disease | -0.1922 | 0.2473 | ±0.4947 | -0.777 | 0.4372 | 0.8252 |  |
| **Circulatory disease** | **+0.3806** | 0.1796 | ±0.3591 | **+2.119** | **0.0341** | 1.4631 | * |
| CV (%) | +0.0074 | 0.0151 | ±0.0303 | +0.491 | 0.6231 | 1.0075 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0602**, LLR χ² = **98.53** (p = **3.49e-16**), AUC = **0.6599**, AIC = **1562.6**, BIC = **1624.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.0480** | 0.5903 | ±1.1807 | **-5.163** | **2.43e-07** | 0.0475 | *** |
| **Education: graduate level (vs college)** | **-0.5064** | 0.1326 | ±0.2652 | **-3.818** | **1.34e-04** | 0.6027 | *** |
| **Education: high school or below (vs college)** | **+0.8481** | 0.2215 | ±0.4431 | **+3.828** | **1.29e-04** | 2.3352 | *** |
| **Site: UCSD (vs UAB)** | **+0.3424** | 0.1645 | ±0.3290 | **+2.081** | **0.0374** | 1.4083 | * |
| Site: UW (vs UAB) | +0.1513 | 0.1554 | ±0.3109 | +0.973 | 0.3305 | 1.1633 |  |
| **Age (years)** | **+0.0336** | 0.0059 | ±0.0117 | **+5.748** | **9.01e-09** | 1.0342 | *** |
| BMI (kg/m2) | +0.0123 | 0.0092 | ±0.0184 | +1.340 | 0.1802 | 1.0124 |  |
| Hypertension | +0.0441 | 0.1366 | ±0.2732 | +0.323 | 0.7468 | 1.0451 |  |
| High cholesterol | +0.0063 | 0.1288 | ±0.2576 | +0.049 | 0.9607 | 1.0064 |  |
| Kidney disease | -0.1873 | 0.2471 | ±0.4942 | -0.758 | 0.4486 | 0.8292 |  |
| **Circulatory disease** | **+0.3816** | 0.1795 | ±0.3591 | **+2.126** | **0.0335** | 1.4647 | * |
| Mean / SD ratio | -0.0116 | 0.0506 | ±0.1011 | -0.230 | 0.8179 | 0.9884 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0603**, LLR χ² = **98.69** (p = **3.24e-16**), AUC = **0.6599**, AIC = **1562.5**, BIC = **1624.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.9738** | 0.5898 | ±1.1796 | **-5.042** | **4.61e-07** | 0.0511 | *** |
| **Education: graduate level (vs college)** | **-0.5065** | 0.1326 | ±0.2651 | **-3.820** | **1.33e-04** | 0.6026 | *** |
| **Education: high school or below (vs college)** | **+0.8475** | 0.2215 | ±0.4431 | **+3.826** | **1.30e-04** | 2.3338 | *** |
| **Site: UCSD (vs UAB)** | **+0.3436** | 0.1644 | ±0.3289 | **+2.090** | **0.0366** | 1.4101 | * |
| Site: UW (vs UAB) | +0.1502 | 0.1555 | ±0.3109 | +0.966 | 0.3339 | 1.1621 |  |
| **Age (years)** | **+0.0335** | 0.0059 | ±0.0117 | **+5.722** | **1.05e-08** | 1.0341 | *** |
| BMI (kg/m2) | +0.0122 | 0.0092 | ±0.0183 | +1.330 | 0.1836 | 1.0123 |  |
| Hypertension | +0.0429 | 0.1365 | ±0.2730 | +0.314 | 0.7532 | 1.0439 |  |
| High cholesterol | +0.0070 | 0.1288 | ±0.2576 | +0.055 | 0.9564 | 1.0071 |  |
| Kidney disease | -0.1913 | 0.2472 | ±0.4945 | -0.774 | 0.4390 | 0.8259 |  |
| **Circulatory disease** | **+0.3816** | 0.1795 | ±0.3591 | **+2.126** | **0.0335** | 1.4647 | * |
| Avg. daily mean/SD | -0.0196 | 0.0419 | ±0.0837 | -0.468 | 0.6399 | 0.9806 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0604**, LLR χ² = **98.95** (p = **2.88e-16**), AUC = **0.6603**, AIC = **1562.2**, BIC = **1624.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3403** | 0.5940 | ±1.1881 | **-5.623** | **1.88e-08** | 0.0354 | *** |
| **Education: graduate level (vs college)** | **-0.5060** | 0.1326 | ±0.2652 | **-3.816** | **1.35e-04** | 0.6029 | *** |
| **Education: high school or below (vs college)** | **+0.8448** | 0.2215 | ±0.4430 | **+3.814** | **1.37e-04** | 2.3274 | *** |
| **Site: UCSD (vs UAB)** | **+0.3479** | 0.1647 | ±0.3293 | **+2.113** | **0.0346** | 1.4161 | * |
| Site: UW (vs UAB) | +0.1589 | 0.1558 | ±0.3116 | +1.020 | 0.3079 | 1.1722 |  |
| **Age (years)** | **+0.0339** | 0.0058 | ±0.0117 | **+5.791** | **7.01e-09** | 1.0344 | *** |
| BMI (kg/m2) | +0.0122 | 0.0092 | ±0.0183 | +1.331 | 0.1831 | 1.0123 |  |
| Hypertension | +0.0466 | 0.1363 | ±0.2727 | +0.341 | 0.7328 | 1.0477 |  |
| High cholesterol | +0.0097 | 0.1289 | ±0.2579 | +0.075 | 0.9400 | 1.0097 |  |
| Kidney disease | -0.1881 | 0.2469 | ±0.4937 | -0.762 | 0.4460 | 0.8285 |  |
| **Circulatory disease** | **+0.3808** | 0.1796 | ±0.3591 | **+2.121** | **0.0339** | 1.4635 | * |
| MAG (mg/dL/h) | +0.0054 | 0.0078 | ±0.0155 | +0.692 | 0.4887 | 1.0054 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0610**, LLR χ² = **99.87** (p = **1.89e-16**), AUC = **0.6609**, AIC = **1561.3**, BIC = **1623.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3823** | 0.5487 | ±1.0973 | **-6.165** | **7.06e-10** | 0.0340 | *** |
| **Education: graduate level (vs college)** | **-0.5110** | 0.1327 | ±0.2654 | **-3.851** | **1.18e-04** | 0.5999 | *** |
| **Education: high school or below (vs college)** | **+0.8437** | 0.2216 | ±0.4431 | **+3.808** | **1.40e-04** | 2.3249 | *** |
| **Site: UCSD (vs UAB)** | **+0.3502** | 0.1646 | ±0.3292 | **+2.128** | **0.0333** | 1.4194 | * |
| Site: UW (vs UAB) | +0.1481 | 0.1556 | ±0.3111 | +0.952 | 0.3412 | 1.1596 |  |
| **Age (years)** | **+0.0334** | 0.0059 | ±0.0117 | **+5.704** | **1.17e-08** | 1.0339 | *** |
| BMI (kg/m2) | +0.0126 | 0.0092 | ±0.0184 | +1.376 | 0.1689 | 1.0127 |  |
| Hypertension | +0.0351 | 0.1368 | ±0.2735 | +0.257 | 0.7975 | 1.0357 |  |
| High cholesterol | +0.0099 | 0.1289 | ±0.2578 | +0.077 | 0.9389 | 1.0099 |  |
| Kidney disease | -0.2016 | 0.2473 | ±0.4947 | -0.815 | 0.4151 | 0.8174 |  |
| **Circulatory disease** | **+0.3738** | 0.1797 | ±0.3594 | **+2.080** | **0.0375** | 1.4532 | * |
| Avg. daily range (mg/dL) | +0.0028 | 0.0024 | ±0.0047 | +1.185 | 0.2359 | 1.0028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0602**, LLR χ² = **98.52** (p = **3.51e-16**), AUC = **0.6601**, AIC = **1562.6**, BIC = **1624.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.0998** | 0.5109 | ±1.0218 | **-6.067** | **1.30e-09** | 0.0451 | *** |
| **Education: graduate level (vs college)** | **-0.5072** | 0.1326 | ±0.2651 | **-3.826** | **1.30e-04** | 0.6022 | *** |
| **Education: high school or below (vs college)** | **+0.8474** | 0.2215 | ±0.4430 | **+3.826** | **1.30e-04** | 2.3335 | *** |
| **Site: UCSD (vs UAB)** | **+0.3389** | 0.1644 | ±0.3288 | **+2.061** | **0.0393** | 1.4034 | * |
| Site: UW (vs UAB) | +0.1520 | 0.1554 | ±0.3109 | +0.978 | 0.3281 | 1.1642 |  |
| **Age (years)** | **+0.0337** | 0.0058 | ±0.0117 | **+5.773** | **7.81e-09** | 1.0343 | *** |
| BMI (kg/m2) | +0.0124 | 0.0092 | ±0.0184 | +1.347 | 0.1780 | 1.0125 |  |
| Hypertension | +0.0466 | 0.1363 | ±0.2726 | +0.342 | 0.7327 | 1.0477 |  |
| High cholesterol | +0.0059 | 0.1287 | ±0.2575 | +0.046 | 0.9635 | 1.0059 |  |
| Kidney disease | -0.1845 | 0.2469 | ±0.4939 | -0.747 | 0.4549 | 0.8315 |  |
| **Circulatory disease** | **+0.3836** | 0.1797 | ±0.3593 | **+2.135** | **0.0328** | 1.4675 | * |
| SD of daily means (mg/dL) | -0.0038 | 0.0187 | ±0.0374 | -0.203 | 0.8395 | 0.9962 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0613**, LLR χ² = **100.32** (p = **1.54e-16**), AUC = **0.6608**, AIC = **1560.8**, BIC = **1622.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.2052** | 0.8397 | ±1.6793 | **-2.626** | **0.0086** | 0.1102 | ** |
| **Education: graduate level (vs college)** | **-0.5121** | 0.1327 | ±0.2654 | **-3.860** | **1.14e-04** | 0.5992 | *** |
| **Education: high school or below (vs college)** | **+0.8403** | 0.2220 | ±0.4441 | **+3.784** | **1.54e-04** | 2.3171 | *** |
| **Site: UCSD (vs UAB)** | **+0.3520** | 0.1646 | ±0.3291 | **+2.139** | **0.0324** | 1.4219 | * |
| Site: UW (vs UAB) | +0.1506 | 0.1556 | ±0.3113 | +0.968 | 0.3332 | 1.1625 |  |
| **Age (years)** | **+0.0337** | 0.0058 | ±0.0117 | **+5.763** | **8.27e-09** | 1.0343 | *** |
| BMI (kg/m2) | +0.0118 | 0.0092 | ±0.0184 | +1.285 | 0.1989 | 1.0119 |  |
| Hypertension | +0.0362 | 0.1366 | ±0.2733 | +0.265 | 0.7908 | 1.0369 |  |
| High cholesterol | +0.0027 | 0.1289 | ±0.2577 | +0.021 | 0.9830 | 1.0027 |  |
| Kidney disease | -0.2008 | 0.2474 | ±0.4948 | -0.811 | 0.4171 | 0.8181 |  |
| **Circulatory disease** | **+0.3712** | 0.1798 | ±0.3597 | **+2.064** | **0.0390** | 1.4494 | * |
| Time in range 70-180, pooled (%) | -0.0093 | 0.0069 | ±0.0138 | -1.354 | 0.1757 | 0.9907 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0612**, LLR χ² = **100.27** (p = **1.58e-16**), AUC = **0.6607**, AIC = **1560.9**, BIC = **1622.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.2177** | 0.8398 | ±1.6796 | **-2.641** | **0.0083** | 0.1089 | ** |
| **Education: graduate level (vs college)** | **-0.5122** | 0.1327 | ±0.2654 | **-3.860** | **1.13e-04** | 0.5992 | *** |
| **Education: high school or below (vs college)** | **+0.8413** | 0.2220 | ±0.4440 | **+3.790** | **1.51e-04** | 2.3193 | *** |
| **Site: UCSD (vs UAB)** | **+0.3514** | 0.1645 | ±0.3291 | **+2.135** | **0.0327** | 1.4210 | * |
| Site: UW (vs UAB) | +0.1508 | 0.1556 | ±0.3112 | +0.969 | 0.3325 | 1.1628 |  |
| **Age (years)** | **+0.0337** | 0.0058 | ±0.0117 | **+5.760** | **8.42e-09** | 1.0342 | *** |
| BMI (kg/m2) | +0.0118 | 0.0092 | ±0.0184 | +1.281 | 0.2003 | 1.0118 |  |
| Hypertension | +0.0367 | 0.1366 | ±0.2733 | +0.268 | 0.7884 | 1.0374 |  |
| High cholesterol | +0.0023 | 0.1289 | ±0.2577 | +0.018 | 0.9859 | 1.0023 |  |
| Kidney disease | -0.2006 | 0.2474 | ±0.4948 | -0.811 | 0.4175 | 0.8182 |  |
| **Circulatory disease** | **+0.3713** | 0.1798 | ±0.3597 | **+2.065** | **0.0389** | 1.4496 | * |
| Avg. daily time in range 70-180 (%) | -0.0092 | 0.0069 | ±0.0137 | -1.335 | 0.1817 | 0.9909 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0626**, LLR χ² = **102.49** (p = **5.73e-17**), AUC = **0.6622**, AIC = **1558.7**, BIC = **1620.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.9969** | 0.5052 | ±1.0104 | **-5.932** | **2.99e-09** | 0.0499 | *** |
| **Education: graduate level (vs college)** | **-0.5213** | 0.1330 | ±0.2659 | **-3.920** | **8.84e-05** | 0.5938 | *** |
| **Education: high school or below (vs college)** | **+0.8186** | 0.2220 | ±0.4439 | **+3.688** | **2.26e-04** | 2.2673 | *** |
| Site: UCSD (vs UAB) | +0.3034 | 0.1655 | ±0.3310 | +1.833 | 0.0668 | 1.3545 | . |
| Site: UW (vs UAB) | +0.1352 | 0.1559 | ±0.3118 | +0.867 | 0.3860 | 1.1447 |  |
| **Age (years)** | **+0.0331** | 0.0058 | ±0.0117 | **+5.666** | **1.46e-08** | 1.0337 | *** |
| BMI (kg/m2) | +0.0131 | 0.0092 | ±0.0184 | +1.418 | 0.1561 | 1.0132 |  |
| Hypertension | +0.0475 | 0.1364 | ±0.2729 | +0.348 | 0.7279 | 1.0486 |  |
| High cholesterol | -0.0063 | 0.1290 | ±0.2581 | -0.049 | 0.9608 | 0.9937 |  |
| Kidney disease | -0.1883 | 0.2477 | ±0.4954 | -0.760 | 0.4471 | 0.8284 |  |
| **Circulatory disease** | **+0.4092** | 0.1803 | ±0.3605 | **+2.270** | **0.0232** | 1.5056 | * |
| **Any reading < 54 during wear (0/1)** | **-0.2719** | 0.1365 | ±0.2730 | **-1.992** | **0.0464** | 0.7619 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0602**, LLR χ² = **98.56** (p = **3.44e-16**), AUC = **0.6604**, AIC = **1562.6**, BIC = **1624.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1338** | 0.5031 | ±1.0062 | **-6.229** | **4.69e-10** | 0.0436 | *** |
| **Education: graduate level (vs college)** | **-0.5066** | 0.1326 | ±0.2652 | **-3.821** | **1.33e-04** | 0.6026 | *** |
| **Education: high school or below (vs college)** | **+0.8506** | 0.2218 | ±0.4436 | **+3.835** | **1.25e-04** | 2.3412 | *** |
| **Site: UCSD (vs UAB)** | **+0.3463** | 0.1655 | ±0.3311 | **+2.092** | **0.0364** | 1.4138 | * |
| Site: UW (vs UAB) | +0.1564 | 0.1563 | ±0.3126 | +1.001 | 0.3171 | 1.1693 |  |
| **Age (years)** | **+0.0337** | 0.0058 | ±0.0117 | **+5.775** | **7.69e-09** | 1.0343 | *** |
| BMI (kg/m2) | +0.0123 | 0.0092 | ±0.0184 | +1.342 | 0.1797 | 1.0124 |  |
| Hypertension | +0.0472 | 0.1364 | ±0.2727 | +0.346 | 0.7290 | 1.0484 |  |
| High cholesterol | +0.0080 | 0.1290 | ±0.2580 | +0.062 | 0.9507 | 1.0080 |  |
| Kidney disease | -0.1853 | 0.2469 | ±0.4938 | -0.751 | 0.4528 | 0.8308 |  |
| **Circulatory disease** | **+0.3822** | 0.1795 | ±0.3591 | **+2.129** | **0.0332** | 1.4656 | * |
| Time < 54 (%) | +0.0317 | 0.1063 | ±0.2127 | +0.298 | 0.7657 | 1.0322 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0602**, LLR χ² = **98.62** (p = **3.36e-16**), AUC = **0.6603**, AIC = **1562.6**, BIC = **1624.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1330** | 0.5022 | ±1.0043 | **-6.239** | **4.40e-10** | 0.0436 | *** |
| **Education: graduate level (vs college)** | **-0.5060** | 0.1326 | ±0.2652 | **-3.816** | **1.36e-04** | 0.6029 | *** |
| **Education: high school or below (vs college)** | **+0.8514** | 0.2218 | ±0.4436 | **+3.839** | **1.24e-04** | 2.3430 | *** |
| **Site: UCSD (vs UAB)** | **+0.3470** | 0.1653 | ±0.3306 | **+2.100** | **0.0358** | 1.4149 | * |
| Site: UW (vs UAB) | +0.1584 | 0.1565 | ±0.3131 | +1.012 | 0.3117 | 1.1716 |  |
| **Age (years)** | **+0.0337** | 0.0058 | ±0.0117 | **+5.769** | **7.99e-09** | 1.0343 | *** |
| BMI (kg/m2) | +0.0123 | 0.0092 | ±0.0184 | +1.342 | 0.1797 | 1.0124 |  |
| Hypertension | +0.0483 | 0.1364 | ±0.2729 | +0.354 | 0.7235 | 1.0494 |  |
| High cholesterol | +0.0084 | 0.1290 | ±0.2580 | +0.065 | 0.9483 | 1.0084 |  |
| Kidney disease | -0.1857 | 0.2469 | ±0.4938 | -0.752 | 0.4520 | 0.8305 |  |
| **Circulatory disease** | **+0.3826** | 0.1795 | ±0.3591 | **+2.131** | **0.0331** | 1.4661 | * |
| Avg. daily time < 54 (%) | +0.0537 | 0.1424 | ±0.2848 | +0.377 | 0.7060 | 1.0552 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0610**, LLR χ² = **99.95** (p = **1.83e-16**), AUC = **0.6610**, AIC = **1561.2**, BIC = **1623.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1815** | 0.5038 | ±1.0077 | **-6.314** | **2.71e-10** | 0.0415 | *** |
| **Education: graduate level (vs college)** | **-0.4993** | 0.1328 | ±0.2656 | **-3.760** | **1.70e-04** | 0.6069 | *** |
| **Education: high school or below (vs college)** | **+0.8687** | 0.2224 | ±0.4448 | **+3.906** | **9.38e-05** | 2.3837 | *** |
| **Site: UCSD (vs UAB)** | **+0.3575** | 0.1651 | ±0.3302 | **+2.165** | **0.0304** | 1.4298 | * |
| Site: UW (vs UAB) | +0.1720 | 0.1565 | ±0.3130 | +1.099 | 0.2717 | 1.1877 |  |
| **Age (years)** | **+0.0340** | 0.0059 | ±0.0117 | **+5.806** | **6.41e-09** | 1.0346 | *** |
| BMI (kg/m2) | +0.0119 | 0.0092 | ±0.0184 | +1.294 | 0.1957 | 1.0119 |  |
| Hypertension | +0.0522 | 0.1365 | ±0.2730 | +0.383 | 0.7020 | 1.0536 |  |
| High cholesterol | +0.0134 | 0.1290 | ±0.2580 | +0.104 | 0.9174 | 1.0135 |  |
| Kidney disease | -0.1832 | 0.2469 | ±0.4937 | -0.742 | 0.4581 | 0.8326 |  |
| **Circulatory disease** | **+0.3833** | 0.1796 | ±0.3593 | **+2.134** | **0.0329** | 1.4671 | * |
| Time 54-69, pooled (%) | +0.0532 | 0.0431 | ±0.0862 | +1.235 | 0.2170 | 1.0546 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0612**, LLR χ² = **100.22** (p = **1.62e-16**), AUC = **0.6610**, AIC = **1560.9**, BIC = **1622.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1769** | 0.5032 | ±1.0063 | **-6.314** | **2.72e-10** | 0.0417 | *** |
| **Education: graduate level (vs college)** | **-0.4980** | 0.1328 | ±0.2657 | **-3.749** | **1.78e-04** | 0.6078 | *** |
| **Education: high school or below (vs college)** | **+0.8717** | 0.2224 | ±0.4449 | **+3.919** | **8.89e-05** | 2.3911 | *** |
| **Site: UCSD (vs UAB)** | **+0.3552** | 0.1649 | ±0.3298 | **+2.154** | **0.0312** | 1.4265 | * |
| Site: UW (vs UAB) | +0.1736 | 0.1565 | ±0.3130 | +1.109 | 0.2673 | 1.1896 |  |
| **Age (years)** | **+0.0339** | 0.0058 | ±0.0117 | **+5.795** | **6.82e-09** | 1.0345 | *** |
| BMI (kg/m2) | +0.0119 | 0.0092 | ±0.0184 | +1.293 | 0.1961 | 1.0119 |  |
| Hypertension | +0.0537 | 0.1366 | ±0.2731 | +0.393 | 0.6942 | 1.0552 |  |
| High cholesterol | +0.0133 | 0.1290 | ±0.2580 | +0.103 | 0.9177 | 1.0134 |  |
| Kidney disease | -0.1826 | 0.2469 | ±0.4938 | -0.740 | 0.4595 | 0.8331 |  |
| **Circulatory disease** | **+0.3838** | 0.1796 | ±0.3592 | **+2.137** | **0.0326** | 1.4678 | * |
| Avg. daily time 54-69 (%) | +0.0573 | 0.0426 | ±0.0853 | +1.344 | 0.1790 | 1.0590 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0608**, LLR χ² = **99.60** (p = **2.14e-16**), AUC = **0.6613**, AIC = **1561.6**, BIC = **1623.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1790** | 0.5043 | ±1.0086 | **-6.304** | **2.91e-10** | 0.0416 | *** |
| **Education: graduate level (vs college)** | **-0.5008** | 0.1328 | ±0.2655 | **-3.772** | **1.62e-04** | 0.6060 | *** |
| **Education: high school or below (vs college)** | **+0.8661** | 0.2224 | ±0.4448 | **+3.895** | **9.83e-05** | 2.3776 | *** |
| **Site: UCSD (vs UAB)** | **+0.3595** | 0.1655 | ±0.3309 | **+2.173** | **0.0298** | 1.4326 | * |
| Site: UW (vs UAB) | +0.1717 | 0.1567 | ±0.3135 | +1.095 | 0.2734 | 1.1873 |  |
| **Age (years)** | **+0.0339** | 0.0059 | ±0.0117 | **+5.800** | **6.64e-09** | 1.0345 | *** |
| BMI (kg/m2) | +0.0120 | 0.0092 | ±0.0184 | +1.313 | 0.1892 | 1.0121 |  |
| Hypertension | +0.0518 | 0.1365 | ±0.2730 | +0.380 | 0.7042 | 1.0532 |  |
| High cholesterol | +0.0140 | 0.1291 | ±0.2581 | +0.108 | 0.9139 | 1.0141 |  |
| Kidney disease | -0.1846 | 0.2469 | ±0.4937 | -0.748 | 0.4545 | 0.8314 |  |
| **Circulatory disease** | **+0.3831** | 0.1796 | ±0.3592 | **+2.133** | **0.0329** | 1.4669 | * |
| Time < 70 (%) | +0.0372 | 0.0344 | ±0.0688 | +1.080 | 0.2801 | 1.0379 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0610**, LLR χ² = **99.92** (p = **1.86e-16**), AUC = **0.6611**, AIC = **1561.2**, BIC = **1623.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1739** | 0.5033 | ±1.0066 | **-6.306** | **2.86e-10** | 0.0418 | *** |
| **Education: graduate level (vs college)** | **-0.4991** | 0.1328 | ±0.2656 | **-3.758** | **1.72e-04** | 0.6071 | *** |
| **Education: high school or below (vs college)** | **+0.8693** | 0.2224 | ±0.4448 | **+3.909** | **9.28e-05** | 2.3853 | *** |
| **Site: UCSD (vs UAB)** | **+0.3573** | 0.1651 | ±0.3302 | **+2.164** | **0.0304** | 1.4295 | * |
| Site: UW (vs UAB) | +0.1741 | 0.1567 | ±0.3135 | +1.111 | 0.2667 | 1.1902 |  |
| **Age (years)** | **+0.0338** | 0.0058 | ±0.0117 | **+5.788** | **7.13e-09** | 1.0344 | *** |
| BMI (kg/m2) | +0.0120 | 0.0092 | ±0.0184 | +1.307 | 0.1911 | 1.0121 |  |
| Hypertension | +0.0537 | 0.1366 | ±0.2731 | +0.393 | 0.6940 | 1.0552 |  |
| High cholesterol | +0.0138 | 0.1290 | ±0.2581 | +0.107 | 0.9146 | 1.0139 |  |
| Kidney disease | -0.1840 | 0.2469 | ±0.4938 | -0.745 | 0.4561 | 0.8319 |  |
| **Circulatory disease** | **+0.3838** | 0.1796 | ±0.3592 | **+2.137** | **0.0326** | 1.4679 | * |
| Avg. daily time < 70 (%) | +0.0437 | 0.0357 | ±0.0715 | +1.222 | 0.2218 | 1.0446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0603**, LLR χ² = **98.67** (p = **3.27e-16**), AUC = **0.6595**, AIC = **1562.5**, BIC = **1624.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.5808 | 1.3297 | ±2.6594 | -1.941 | 0.0523 | 0.0757 | . |
| **Education: graduate level (vs college)** | **-0.5076** | 0.1326 | ±0.2651 | **-3.830** | **1.28e-04** | 0.6019 | *** |
| **Education: high school or below (vs college)** | **+0.8412** | 0.2220 | ±0.4440 | **+3.789** | **1.51e-04** | 2.3190 | *** |
| **Site: UCSD (vs UAB)** | **+0.3426** | 0.1643 | ±0.3287 | **+2.085** | **0.0371** | 1.4085 | * |
| Site: UW (vs UAB) | +0.1529 | 0.1555 | ±0.3110 | +0.984 | 0.3254 | 1.1652 |  |
| **Age (years)** | **+0.0338** | 0.0058 | ±0.0117 | **+5.777** | **7.62e-09** | 1.0343 | *** |
| BMI (kg/m2) | +0.0123 | 0.0092 | ±0.0183 | +1.337 | 0.1813 | 1.0123 |  |
| Hypertension | +0.0456 | 0.1363 | ±0.2726 | +0.335 | 0.7379 | 1.0467 |  |
| High cholesterol | +0.0065 | 0.1288 | ±0.2575 | +0.051 | 0.9596 | 1.0065 |  |
| Kidney disease | -0.1856 | 0.2469 | ±0.4938 | -0.752 | 0.4522 | 0.8306 |  |
| **Circulatory disease** | **+0.3768** | 0.1799 | ±0.3599 | **+2.094** | **0.0363** | 1.4576 | * |
| Time 54-250, pooled (%) | -0.0055 | 0.0124 | ±0.0249 | -0.438 | 0.6615 | 0.9946 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0602**, LLR χ² = **98.62** (p = **3.34e-16**), AUC = **0.6595**, AIC = **1562.5**, BIC = **1624.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.6404 | 1.3547 | ±2.7094 | -1.949 | 0.0513 | 0.0713 | . |
| **Education: graduate level (vs college)** | **-0.5076** | 0.1326 | ±0.2651 | **-3.830** | **1.28e-04** | 0.6019 | *** |
| **Education: high school or below (vs college)** | **+0.8417** | 0.2220 | ±0.4441 | **+3.791** | **1.50e-04** | 2.3203 | *** |
| **Site: UCSD (vs UAB)** | **+0.3420** | 0.1643 | ±0.3286 | **+2.082** | **0.0374** | 1.4078 | * |
| Site: UW (vs UAB) | +0.1526 | 0.1555 | ±0.3109 | +0.981 | 0.3264 | 1.1648 |  |
| **Age (years)** | **+0.0337** | 0.0058 | ±0.0117 | **+5.775** | **7.71e-09** | 1.0343 | *** |
| BMI (kg/m2) | +0.0123 | 0.0092 | ±0.0184 | +1.335 | 0.1817 | 1.0123 |  |
| Hypertension | +0.0457 | 0.1363 | ±0.2726 | +0.335 | 0.7375 | 1.0467 |  |
| High cholesterol | +0.0063 | 0.1288 | ±0.2575 | +0.049 | 0.9609 | 1.0063 |  |
| Kidney disease | -0.1853 | 0.2469 | ±0.4938 | -0.751 | 0.4529 | 0.8308 |  |
| **Circulatory disease** | **+0.3774** | 0.1799 | ±0.3599 | **+2.098** | **0.0359** | 1.4585 | * |
| Avg. daily time 54-250 (%) | -0.0048 | 0.0127 | ±0.0254 | -0.381 | 0.7031 | 0.9952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0613**, LLR χ² = **100.32** (p = **1.54e-16**), AUC = **0.6611**, AIC = **1560.8**, BIC = **1622.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1198** | 0.5007 | ±1.0013 | **-6.231** | **4.62e-10** | 0.0442 | *** |
| **Education: graduate level (vs college)** | **-0.5157** | 0.1328 | ±0.2656 | **-3.883** | **1.03e-04** | 0.5971 | *** |
| **Education: high school or below (vs college)** | **+0.8458** | 0.2217 | ±0.4435 | **+3.814** | **1.37e-04** | 2.3299 | *** |
| **Site: UCSD (vs UAB)** | **+0.3485** | 0.1644 | ±0.3289 | **+2.119** | **0.0341** | 1.4169 | * |
| Site: UW (vs UAB) | +0.1424 | 0.1557 | ±0.3114 | +0.915 | 0.3604 | 1.1530 |  |
| **Age (years)** | **+0.0335** | 0.0058 | ±0.0117 | **+5.731** | **9.97e-09** | 1.0341 | *** |
| BMI (kg/m2) | +0.0117 | 0.0092 | ±0.0184 | +1.276 | 0.2021 | 1.0118 |  |
| Hypertension | +0.0317 | 0.1368 | ±0.2737 | +0.232 | 0.8166 | 1.0322 |  |
| High cholesterol | -0.0031 | 0.1290 | ±0.2580 | -0.024 | 0.9806 | 0.9969 |  |
| Kidney disease | -0.2063 | 0.2478 | ±0.4955 | -0.833 | 0.4050 | 0.8136 |  |
| **Circulatory disease** | **+0.3787** | 0.1796 | ±0.3592 | **+2.109** | **0.0350** | 1.4604 | * |
| Time 181-250, pooled (%) | +0.0136 | 0.0099 | ±0.0198 | +1.370 | 0.1708 | 1.0137 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0613**, LLR χ² = **100.29** (p = **1.56e-16**), AUC = **0.6610**, AIC = **1560.9**, BIC = **1622.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1192** | 0.5006 | ±1.0013 | **-6.230** | **4.65e-10** | 0.0442 | *** |
| **Education: graduate level (vs college)** | **-0.5158** | 0.1328 | ±0.2656 | **-3.884** | **1.03e-04** | 0.5970 | *** |
| **Education: high school or below (vs college)** | **+0.8469** | 0.2217 | ±0.4434 | **+3.820** | **1.34e-04** | 2.3325 | *** |
| **Site: UCSD (vs UAB)** | **+0.3494** | 0.1645 | ±0.3289 | **+2.125** | **0.0336** | 1.4183 | * |
| Site: UW (vs UAB) | +0.1434 | 0.1557 | ±0.3114 | +0.921 | 0.3569 | 1.1542 |  |
| **Age (years)** | **+0.0335** | 0.0058 | ±0.0117 | **+5.735** | **9.73e-09** | 1.0341 | *** |
| BMI (kg/m2) | +0.0117 | 0.0092 | ±0.0184 | +1.273 | 0.2031 | 1.0118 |  |
| Hypertension | +0.0321 | 0.1368 | ±0.2737 | +0.234 | 0.8146 | 1.0326 |  |
| High cholesterol | -0.0033 | 0.1290 | ±0.2580 | -0.025 | 0.9797 | 0.9967 |  |
| Kidney disease | -0.2065 | 0.2478 | ±0.4956 | -0.833 | 0.4046 | 0.8134 |  |
| **Circulatory disease** | **+0.3785** | 0.1796 | ±0.3592 | **+2.108** | **0.0351** | 1.4601 | * |
| Avg. daily time 181-250 (%) | +0.0133 | 0.0098 | ±0.0196 | +1.361 | 0.1736 | 1.0134 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0610**, LLR χ² = **99.81** (p = **1.95e-16**), AUC = **0.6602**, AIC = **1561.4**, BIC = **1623.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1245** | 0.5007 | ±1.0014 | **-6.240** | **4.38e-10** | 0.0440 | *** |
| **Education: graduate level (vs college)** | **-0.5128** | 0.1327 | ±0.2654 | **-3.864** | **1.11e-04** | 0.5988 | *** |
| **Education: high school or below (vs college)** | **+0.8371** | 0.2220 | ±0.4440 | **+3.771** | **1.63e-04** | 2.3098 | *** |
| **Site: UCSD (vs UAB)** | **+0.3464** | 0.1644 | ±0.3288 | **+2.107** | **0.0351** | 1.4140 | * |
| Site: UW (vs UAB) | +0.1467 | 0.1556 | ±0.3113 | +0.942 | 0.3460 | 1.1580 |  |
| **Age (years)** | **+0.0336** | 0.0058 | ±0.0117 | **+5.757** | **8.55e-09** | 1.0342 | *** |
| BMI (kg/m2) | +0.0119 | 0.0092 | ±0.0184 | +1.298 | 0.1942 | 1.0120 |  |
| Hypertension | +0.0366 | 0.1367 | ±0.2733 | +0.268 | 0.7887 | 1.0373 |  |
| High cholesterol | +0.0015 | 0.1289 | ±0.2577 | +0.011 | 0.9910 | 1.0015 |  |
| Kidney disease | -0.1983 | 0.2474 | ±0.4947 | -0.802 | 0.4227 | 0.8201 |  |
| **Circulatory disease** | **+0.3725** | 0.1798 | ±0.3596 | **+2.072** | **0.0383** | 1.4514 | * |
| Time > 180 (%) | +0.0079 | 0.0069 | ±0.0137 | +1.153 | 0.2490 | 1.0080 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0609**, LLR χ² = **99.73** (p = **2.02e-16**), AUC = **0.6601**, AIC = **1561.4**, BIC = **1623.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1232** | 0.5007 | ±1.0014 | **-6.238** | **4.44e-10** | 0.0440 | *** |
| **Education: graduate level (vs college)** | **-0.5128** | 0.1327 | ±0.2654 | **-3.864** | **1.11e-04** | 0.5988 | *** |
| **Education: high school or below (vs college)** | **+0.8382** | 0.2219 | ±0.4439 | **+3.776** | **1.59e-04** | 2.3121 | *** |
| **Site: UCSD (vs UAB)** | **+0.3468** | 0.1644 | ±0.3288 | **+2.110** | **0.0349** | 1.4146 | * |
| Site: UW (vs UAB) | +0.1472 | 0.1556 | ±0.3112 | +0.946 | 0.3442 | 1.1586 |  |
| **Age (years)** | **+0.0336** | 0.0058 | ±0.0117 | **+5.759** | **8.47e-09** | 1.0342 | *** |
| BMI (kg/m2) | +0.0119 | 0.0092 | ±0.0184 | +1.296 | 0.1951 | 1.0120 |  |
| Hypertension | +0.0370 | 0.1366 | ±0.2733 | +0.271 | 0.7867 | 1.0377 |  |
| High cholesterol | +0.0015 | 0.1289 | ±0.2577 | +0.011 | 0.9909 | 1.0015 |  |
| Kidney disease | -0.1980 | 0.2474 | ±0.4947 | -0.801 | 0.4234 | 0.8203 |  |
| **Circulatory disease** | **+0.3727** | 0.1798 | ±0.3596 | **+2.073** | **0.0382** | 1.4516 | * |
| Avg. daily time > 180 (%) | +0.0077 | 0.0068 | ±0.0137 | +1.119 | 0.2631 | 1.0077 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0602**, LLR χ² = **98.48** (p = **3.58e-16**), AUC = **0.6598**, AIC = **1562.7**, BIC = **1624.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1199** | 0.5010 | ±1.0019 | **-6.228** | **4.73e-10** | 0.0442 | *** |
| **Education: graduate level (vs college)** | **-0.5074** | 0.1326 | ±0.2651 | **-3.828** | **1.29e-04** | 0.6021 | *** |
| **Education: high school or below (vs college)** | **+0.8471** | 0.2217 | ±0.4434 | **+3.821** | **1.33e-04** | 2.3329 | *** |
| **Site: UCSD (vs UAB)** | **+0.3404** | 0.1643 | ±0.3286 | **+2.072** | **0.0383** | 1.4056 | * |
| Site: UW (vs UAB) | +0.1515 | 0.1554 | ±0.3109 | +0.975 | 0.3297 | 1.1636 |  |
| **Age (years)** | **+0.0337** | 0.0058 | ±0.0117 | **+5.771** | **7.88e-09** | 1.0343 | *** |
| BMI (kg/m2) | +0.0122 | 0.0092 | ±0.0184 | +1.329 | 0.1838 | 1.0123 |  |
| Hypertension | +0.0460 | 0.1363 | ±0.2727 | +0.337 | 0.7360 | 1.0470 |  |
| High cholesterol | +0.0053 | 0.1288 | ±0.2577 | +0.041 | 0.9671 | 1.0053 |  |
| Kidney disease | -0.1847 | 0.2469 | ±0.4938 | -0.748 | 0.4545 | 0.8314 |  |
| **Circulatory disease** | **+0.3820** | 0.1796 | ±0.3591 | **+2.127** | **0.0334** | 1.4652 | * |
| Nocturnal time > 180 (%) | +0.0002 | 0.0073 | ±0.0145 | +0.030 | 0.9764 | 1.0002 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0607**, LLR χ² = **99.31** (p = **2.44e-16**), AUC = **0.6618**, AIC = **1561.9**, BIC = **1623.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1563** | 0.5027 | ±1.0053 | **-6.279** | **3.41e-10** | 0.0426 | *** |
| **Education: graduate level (vs college)** | **-0.5068** | 0.1326 | ±0.2652 | **-3.823** | **1.32e-04** | 0.6024 | *** |
| **Education: high school or below (vs college)** | **+0.8493** | 0.2217 | ±0.4433 | **+3.832** | **1.27e-04** | 2.3380 | *** |
| **Site: UCSD (vs UAB)** | **+0.3447** | 0.1644 | ±0.3288 | **+2.097** | **0.0360** | 1.4116 | * |
| Site: UW (vs UAB) | +0.1497 | 0.1555 | ±0.3110 | +0.963 | 0.3358 | 1.1615 |  |
| **Age (years)** | **+0.0336** | 0.0058 | ±0.0117 | **+5.758** | **8.50e-09** | 1.0342 | *** |
| BMI (kg/m2) | +0.0128 | 0.0092 | ±0.0184 | +1.394 | 0.1634 | 1.0129 |  |
| Hypertension | +0.0371 | 0.1367 | ±0.2734 | +0.271 | 0.7860 | 1.0378 |  |
| High cholesterol | +0.0033 | 0.1288 | ±0.2576 | +0.025 | 0.9799 | 1.0033 |  |
| Kidney disease | -0.1872 | 0.2470 | ±0.4940 | -0.758 | 0.4486 | 0.8293 |  |
| **Circulatory disease** | **+0.3834** | 0.1795 | ±0.3590 | **+2.136** | **0.0327** | 1.4673 | * |
| Any reading > 250 during wear (0/1) | +0.1423 | 0.1549 | ±0.3098 | +0.918 | 0.3584 | 1.1529 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0603**, LLR χ² = **98.64** (p = **3.31e-16**), AUC = **0.6595**, AIC = **1562.5**, BIC = **1624.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1233** | 0.5010 | ±1.0019 | **-6.235** | **4.52e-10** | 0.0440 | *** |
| **Education: graduate level (vs college)** | **-0.5077** | 0.1326 | ±0.2651 | **-3.831** | **1.28e-04** | 0.6019 | *** |
| **Education: high school or below (vs college)** | **+0.8410** | 0.2221 | ±0.4442 | **+3.787** | **1.52e-04** | 2.3187 | *** |
| **Site: UCSD (vs UAB)** | **+0.3415** | 0.1643 | ±0.3286 | **+2.079** | **0.0377** | 1.4070 | * |
| Site: UW (vs UAB) | +0.1521 | 0.1555 | ±0.3109 | +0.978 | 0.3279 | 1.1643 |  |
| **Age (years)** | **+0.0337** | 0.0058 | ±0.0117 | **+5.776** | **7.67e-09** | 1.0343 | *** |
| BMI (kg/m2) | +0.0123 | 0.0092 | ±0.0184 | +1.336 | 0.1816 | 1.0123 |  |
| Hypertension | +0.0455 | 0.1363 | ±0.2726 | +0.334 | 0.7387 | 1.0465 |  |
| High cholesterol | +0.0061 | 0.1288 | ±0.2575 | +0.047 | 0.9625 | 1.0061 |  |
| Kidney disease | -0.1854 | 0.2469 | ±0.4938 | -0.751 | 0.4527 | 0.8308 |  |
| **Circulatory disease** | **+0.3771** | 0.1799 | ±0.3599 | **+2.096** | **0.0361** | 1.4581 | * |
| Time > 250 (%) | +0.0051 | 0.0125 | ±0.0250 | +0.407 | 0.6841 | 1.0051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,271)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1271**, events = **438**, McFadden pseudo-R² = **0.0602**, LLR χ² = **98.60** (p = **3.38e-16**), AUC = **0.6595**, AIC = **1562.6**, BIC = **1624.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1225** | 0.5009 | ±1.0019 | **-6.233** | **4.57e-10** | 0.0440 | *** |
| **Education: graduate level (vs college)** | **-0.5077** | 0.1326 | ±0.2651 | **-3.830** | **1.28e-04** | 0.6019 | *** |
| **Education: high school or below (vs college)** | **+0.8418** | 0.2221 | ±0.4442 | **+3.790** | **1.50e-04** | 2.3205 | *** |
| **Site: UCSD (vs UAB)** | **+0.3414** | 0.1643 | ±0.3286 | **+2.078** | **0.0377** | 1.4069 | * |
| Site: UW (vs UAB) | +0.1520 | 0.1554 | ±0.3109 | +0.978 | 0.3282 | 1.1641 |  |
| **Age (years)** | **+0.0337** | 0.0058 | ±0.0117 | **+5.775** | **7.71e-09** | 1.0343 | *** |
| BMI (kg/m2) | +0.0123 | 0.0092 | ±0.0184 | +1.335 | 0.1818 | 1.0123 |  |
| Hypertension | +0.0455 | 0.1363 | ±0.2726 | +0.334 | 0.7383 | 1.0466 |  |
| High cholesterol | +0.0060 | 0.1287 | ±0.2575 | +0.047 | 0.9628 | 1.0060 |  |
| Kidney disease | -0.1852 | 0.2469 | ±0.4938 | -0.750 | 0.4532 | 0.8309 |  |
| **Circulatory disease** | **+0.3778** | 0.1799 | ±0.3599 | **+2.099** | **0.0358** | 1.4590 | * |
| Avg. daily time > 250 (%) | +0.0044 | 0.0127 | ±0.0254 | +0.350 | 0.7260 | 1.0045 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 1,271; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1271**, R² = **0.0790**, Adj R² = **0.0717**, F-statistic = **10.81** (p = **8.39e-18**), Residual SE = **2.553** on **1260** df, AIC = **6000.1**, BIC = **6056.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9965** | 0.5765 | ±1.1529 | **+27.750** | **1.76e-169** | *** |
| Education: graduate level (vs college) | +0.2132 | 0.1526 | ±0.3051 | +1.398 | 0.1622 |  |
| **Education: high school or below (vs college)** | **-1.1819** | 0.3514 | ±0.7028 | **-3.364** | **7.69e-04** | *** |
| Site: UCSD (vs UAB) | +0.1353 | 0.2042 | ±0.4085 | +0.662 | 0.5078 |  |
| Site: UW (vs UAB) | +0.0785 | 0.1957 | ±0.3913 | +0.401 | 0.6883 |  |
| **Age (years)** | **-0.0461** | 0.0071 | ±0.0141 | **-6.534** | **6.40e-11** | *** |
| BMI (kg/m2) | -0.0128 | 0.0102 | ±0.0204 | -1.257 | 0.2086 |  |
| **Hypertension** | **-0.4085** | 0.1613 | ±0.3226 | **-2.533** | **0.0113** | * |
| High cholesterol | +0.1177 | 0.1541 | ±0.3083 | +0.764 | 0.4449 |  |
| Kidney disease | -0.6540 | 0.3445 | ±0.6889 | -1.899 | 0.0576 | . |
| Circulatory disease | -0.0576 | 0.2177 | ±0.4353 | -0.265 | 0.7912 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1271**, R² = **0.0810**, Adj R² = **0.0729**, F-statistic = **10.08** (p = **8.48e-18**), Residual SE = **2.551** on **1259** df, AIC = **5999.4**, BIC = **6061.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.1263** | 0.8980 | ±1.7960 | **+19.071** | **4.39e-81** | *** |
| Education: graduate level (vs college) | +0.2144 | 0.1527 | ±0.3054 | +1.404 | 0.1602 |  |
| **Education: high school or below (vs college)** | **-1.1503** | 0.3508 | ±0.7016 | **-3.279** | **0.0010** | ** |
| Site: UCSD (vs UAB) | +0.1404 | 0.2043 | ±0.4086 | +0.687 | 0.4918 |  |
| Site: UW (vs UAB) | +0.0870 | 0.1958 | ±0.3916 | +0.444 | 0.6569 |  |
| **Age (years)** | **-0.0451** | 0.0071 | ±0.0142 | **-6.372** | **1.87e-10** | *** |
| BMI (kg/m2) | -0.0113 | 0.0103 | ±0.0206 | -1.092 | 0.2747 |  |
| **Hypertension** | **-0.3960** | 0.1612 | ±0.3224 | **-2.456** | **0.0140** | * |
| High cholesterol | +0.1408 | 0.1533 | ±0.3066 | +0.918 | 0.3584 |  |
| Kidney disease | -0.6574 | 0.3431 | ±0.6862 | -1.916 | 0.0553 | . |
| Circulatory disease | -0.0406 | 0.2172 | ±0.4345 | -0.187 | 0.8517 |  |
| HbA1c (%) | -0.2217 | 0.1386 | ±0.2772 | -1.599 | 0.1097 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1271**, R² = **0.0883**, Adj R² = **0.0803**, F-statistic = **11.08** (p = **8.13e-20**), Residual SE = **2.541** on **1259** df, AIC = **5989.2**, BIC = **6051.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.4583** | 0.6719 | ±1.3439 | **+25.982** | **7.93e-149** | *** |
| Education: graduate level (vs college) | +0.2447 | 0.1516 | ±0.3033 | +1.614 | 0.1066 |  |
| **Education: high school or below (vs college)** | **-1.1088** | 0.3467 | ±0.6933 | **-3.198** | **0.0014** | ** |
| Site: UCSD (vs UAB) | +0.1282 | 0.2019 | ±0.4038 | +0.635 | 0.5255 |  |
| Site: UW (vs UAB) | +0.1206 | 0.1963 | ±0.3926 | +0.614 | 0.5390 |  |
| **Age (years)** | **-0.0451** | 0.0071 | ±0.0141 | **-6.397** | **1.58e-10** | *** |
| BMI (kg/m2) | -0.0110 | 0.0103 | ±0.0207 | -1.067 | 0.2862 |  |
| **Hypertension** | **-0.3624** | 0.1624 | ±0.3247 | **-2.232** | **0.0256** | * |
| High cholesterol | +0.1425 | 0.1541 | ±0.3081 | +0.925 | 0.3551 |  |
| Kidney disease | -0.6134 | 0.3445 | ±0.6890 | -1.781 | 0.0750 | . |
| Circulatory disease | -0.0167 | 0.2182 | ±0.4364 | -0.077 | 0.9390 |  |
| **Mean glucose (mg/dL)** | **-0.0135** | 0.0039 | ±0.0077 | **-3.510** | **4.48e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1271**, R² = **0.0883**, Adj R² = **0.0803**, F-statistic = **11.08** (p = **8.13e-20**), Residual SE = **2.541** on **1259** df, AIC = **5989.2**, BIC = **6051.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19.3329** | 1.0532 | ±2.1063 | **+18.357** | **2.90e-75** | *** |
| Education: graduate level (vs college) | +0.2447 | 0.1516 | ±0.3033 | +1.614 | 0.1066 |  |
| **Education: high school or below (vs college)** | **-1.1088** | 0.3467 | ±0.6933 | **-3.198** | **0.0014** | ** |
| Site: UCSD (vs UAB) | +0.1282 | 0.2019 | ±0.4038 | +0.635 | 0.5255 |  |
| Site: UW (vs UAB) | +0.1206 | 0.1963 | ±0.3926 | +0.614 | 0.5390 |  |
| **Age (years)** | **-0.0451** | 0.0071 | ±0.0141 | **-6.397** | **1.58e-10** | *** |
| BMI (kg/m2) | -0.0110 | 0.0103 | ±0.0207 | -1.067 | 0.2862 |  |
| **Hypertension** | **-0.3624** | 0.1624 | ±0.3247 | **-2.232** | **0.0256** | * |
| High cholesterol | +0.1425 | 0.1541 | ±0.3081 | +0.925 | 0.3551 |  |
| Kidney disease | -0.6134 | 0.3445 | ±0.6890 | -1.781 | 0.0750 | . |
| Circulatory disease | -0.0167 | 0.2182 | ±0.4364 | -0.077 | 0.9390 |  |
| **GMI (%)** | **-0.5664** | 0.1614 | ±0.3227 | **-3.510** | **4.48e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1271**, R² = **0.0892**, Adj R² = **0.0813**, F-statistic = **11.22** (p = **4.34e-20**), Residual SE = **2.539** on **1259** df, AIC = **5987.9**, BIC = **6049.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.4351** | 0.6537 | ±1.3074 | **+26.671** | **1.02e-156** | *** |
| Education: graduate level (vs college) | +0.2363 | 0.1519 | ±0.3039 | +1.556 | 0.1198 |  |
| **Education: high school or below (vs college)** | **-1.1077** | 0.3459 | ±0.6919 | **-3.202** | **0.0014** | ** |
| Site: UCSD (vs UAB) | +0.1470 | 0.2032 | ±0.4063 | +0.724 | 0.4693 |  |
| Site: UW (vs UAB) | +0.1188 | 0.1957 | ±0.3914 | +0.607 | 0.5440 |  |
| **Age (years)** | **-0.0464** | 0.0070 | ±0.0141 | **-6.586** | **4.51e-11** | *** |
| BMI (kg/m2) | -0.0075 | 0.0106 | ±0.0211 | -0.713 | 0.4759 |  |
| **Hypertension** | **-0.3716** | 0.1622 | ±0.3244 | **-2.291** | **0.0220** | * |
| High cholesterol | +0.1546 | 0.1544 | ±0.3087 | +1.002 | 0.3164 |  |
| Kidney disease | -0.6481 | 0.3443 | ±0.6886 | -1.882 | 0.0598 | . |
| Circulatory disease | -0.0303 | 0.2171 | ±0.4341 | -0.139 | 0.8891 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0137** | 0.0036 | ±0.0072 | **-3.787** | **1.53e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1271**, R² = **0.0792**, Adj R² = **0.0712**, F-statistic = **9.85** (p = **2.54e-17**), Residual SE = **2.553** on **1259** df, AIC = **6001.8**, BIC = **6063.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0990** | 0.6121 | ±1.2242 | **+26.302** | **1.83e-152** | *** |
| Education: graduate level (vs college) | +0.2141 | 0.1526 | ±0.3051 | +1.403 | 0.1606 |  |
| **Education: high school or below (vs college)** | **-1.1800** | 0.3512 | ±0.7024 | **-3.360** | **7.80e-04** | *** |
| Site: UCSD (vs UAB) | +0.1304 | 0.2029 | ±0.4058 | +0.643 | 0.5205 |  |
| Site: UW (vs UAB) | +0.0814 | 0.1966 | ±0.3932 | +0.414 | 0.6788 |  |
| **Age (years)** | **-0.0458** | 0.0071 | ±0.0141 | **-6.495** | **8.28e-11** | *** |
| BMI (kg/m2) | -0.0128 | 0.0102 | ±0.0205 | -1.246 | 0.2126 |  |
| **Hypertension** | **-0.4015** | 0.1619 | ±0.3238 | **-2.480** | **0.0132** | * |
| High cholesterol | +0.1173 | 0.1543 | ±0.3086 | +0.760 | 0.4474 |  |
| Kidney disease | -0.6428 | 0.3489 | ±0.6977 | -1.843 | 0.0654 | . |
| Circulatory disease | -0.0524 | 0.2185 | ±0.4370 | -0.240 | 0.8105 |  |
| Glucose SD, pooled (mg/dL) | -0.0056 | 0.0118 | ±0.0236 | -0.476 | 0.6339 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1271**, R² = **0.0795**, Adj R² = **0.0714**, F-statistic = **9.88** (p = **2.18e-17**), Residual SE = **2.553** on **1259** df, AIC = **6001.5**, BIC = **6063.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1402** | 0.6057 | ±1.2113 | **+26.649** | **1.82e-156** | *** |
| Education: graduate level (vs college) | +0.2154 | 0.1524 | ±0.3049 | +1.413 | 0.1576 |  |
| **Education: high school or below (vs college)** | **-1.1788** | 0.3511 | ±0.7022 | **-3.357** | **7.87e-04** | *** |
| Site: UCSD (vs UAB) | +0.1288 | 0.2027 | ±0.4053 | +0.635 | 0.5251 |  |
| Site: UW (vs UAB) | +0.0838 | 0.1969 | ±0.3938 | +0.426 | 0.6703 |  |
| **Age (years)** | **-0.0457** | 0.0071 | ±0.0141 | **-6.471** | **9.75e-11** | *** |
| BMI (kg/m2) | -0.0126 | 0.0103 | ±0.0205 | -1.231 | 0.2183 |  |
| **Hypertension** | **-0.3980** | 0.1621 | ±0.3241 | **-2.456** | **0.0141** | * |
| High cholesterol | +0.1174 | 0.1543 | ±0.3086 | +0.761 | 0.4469 |  |
| Kidney disease | -0.6361 | 0.3490 | ±0.6979 | -1.823 | 0.0683 | . |
| Circulatory disease | -0.0499 | 0.2187 | ±0.4375 | -0.228 | 0.8195 |  |
| Avg. daily SD (mg/dL) | -0.0091 | 0.0128 | ±0.0255 | -0.715 | 0.4744 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1271**, R² = **0.0809**, Adj R² = **0.0728**, F-statistic = **10.07** (p = **9.00e-18**), Residual SE = **2.551** on **1259** df, AIC = **5999.5**, BIC = **6061.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.5190** | 0.6610 | ±1.3219 | **+23.479** | **6.62e-122** | *** |
| Education: graduate level (vs college) | +0.2202 | 0.1529 | ±0.3058 | +1.440 | 0.1498 |  |
| **Education: high school or below (vs college)** | **-1.1689** | 0.3511 | ±0.7023 | **-3.329** | **8.72e-04** | *** |
| Site: UCSD (vs UAB) | +0.1548 | 0.2040 | ±0.4080 | +0.759 | 0.4479 |  |
| Site: UW (vs UAB) | +0.0814 | 0.1958 | ±0.3917 | +0.415 | 0.6779 |  |
| **Age (years)** | **-0.0467** | 0.0071 | ±0.0141 | **-6.613** | **3.75e-11** | *** |
| BMI (kg/m2) | -0.0125 | 0.0101 | ±0.0203 | -1.233 | 0.2175 |  |
| **Hypertension** | **-0.4220** | 0.1611 | ±0.3222 | **-2.620** | **0.0088** | ** |
| High cholesterol | +0.1287 | 0.1545 | ±0.3091 | +0.833 | 0.4048 |  |
| **Kidney disease** | **-0.6836** | 0.3467 | ±0.6934 | **-1.972** | **0.0486** | * |
| Circulatory disease | -0.0644 | 0.2175 | ±0.4349 | -0.296 | 0.7671 |  |
| CV (%) | +0.0282 | 0.0178 | ±0.0356 | +1.581 | 0.1140 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1271**, R² = **0.0814**, Adj R² = **0.0734**, F-statistic = **10.14** (p = **6.37e-18**), Residual SE = **2.550** on **1259** df, AIC = **5998.8**, BIC = **6060.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.6500** | 0.6751 | ±1.3501 | **+24.665** | **2.57e-134** | *** |
| Education: graduate level (vs college) | +0.2224 | 0.1526 | ±0.3052 | +1.458 | 0.1450 |  |
| **Education: high school or below (vs college)** | **-1.1774** | 0.3513 | ±0.7025 | **-3.352** | **8.02e-04** | *** |
| Site: UCSD (vs UAB) | +0.1549 | 0.2044 | ±0.4087 | +0.758 | 0.4485 |  |
| Site: UW (vs UAB) | +0.0755 | 0.1958 | ±0.3916 | +0.386 | 0.6998 |  |
| **Age (years)** | **-0.0468** | 0.0071 | ±0.0141 | **-6.631** | **3.33e-11** | *** |
| BMI (kg/m2) | -0.0124 | 0.0101 | ±0.0202 | -1.230 | 0.2188 |  |
| **Hypertension** | **-0.4254** | 0.1610 | ±0.3220 | **-2.642** | **0.0082** | ** |
| High cholesterol | +0.1262 | 0.1544 | ±0.3089 | +0.817 | 0.4139 |  |
| **Kidney disease** | **-0.6795** | 0.3460 | ±0.6920 | **-1.964** | **0.0495** | * |
| Circulatory disease | -0.0626 | 0.2175 | ±0.4350 | -0.288 | 0.7735 |  |
| Mean / SD ratio | -0.1059 | 0.0641 | ±0.1283 | -1.650 | 0.0989 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1271**, R² = **0.0802**, Adj R² = **0.0722**, F-statistic = **9.98** (p = **1.34e-17**), Residual SE = **2.552** on **1259** df, AIC = **6000.4**, BIC = **6062.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4628** | 0.6776 | ±1.3553 | **+24.294** | **2.26e-130** | *** |
| Education: graduate level (vs college) | +0.2165 | 0.1527 | ±0.3054 | +1.418 | 0.1562 |  |
| **Education: high school or below (vs college)** | **-1.1829** | 0.3513 | ±0.7025 | **-3.367** | **7.59e-04** | *** |
| Site: UCSD (vs UAB) | +0.1459 | 0.2040 | ±0.4081 | +0.715 | 0.4746 |  |
| Site: UW (vs UAB) | +0.0743 | 0.1960 | ±0.3921 | +0.379 | 0.7048 |  |
| **Age (years)** | **-0.0467** | 0.0071 | ±0.0141 | **-6.622** | **3.55e-11** | *** |
| BMI (kg/m2) | -0.0130 | 0.0101 | ±0.0203 | -1.278 | 0.2011 |  |
| **Hypertension** | **-0.4172** | 0.1612 | ±0.3224 | **-2.588** | **0.0096** | ** |
| High cholesterol | +0.1235 | 0.1545 | ±0.3089 | +0.800 | 0.4239 |  |
| Kidney disease | -0.6769 | 0.3465 | ±0.6929 | -1.954 | 0.0507 | . |
| Circulatory disease | -0.0598 | 0.2174 | ±0.4349 | -0.275 | 0.7832 |  |
| Avg. daily mean/SD | -0.0623 | 0.0517 | ±0.1033 | -1.206 | 0.2277 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1271**, R² = **0.0794**, Adj R² = **0.0714**, F-statistic = **9.88** (p = **2.19e-17**), Residual SE = **2.553** on **1259** df, AIC = **6001.5**, BIC = **6063.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2759** | 0.6853 | ±1.3706 | **+23.749** | **1.12e-124** | *** |
| Education: graduate level (vs college) | +0.2112 | 0.1529 | ±0.3059 | +1.381 | 0.1673 |  |
| **Education: high school or below (vs college)** | **-1.1777** | 0.3501 | ±0.7002 | **-3.364** | **7.69e-04** | *** |
| Site: UCSD (vs UAB) | +0.1260 | 0.2029 | ±0.4057 | +0.621 | 0.5344 |  |
| Site: UW (vs UAB) | +0.0691 | 0.1944 | ±0.3888 | +0.355 | 0.7223 |  |
| **Age (years)** | **-0.0462** | 0.0071 | ±0.0141 | **-6.548** | **5.81e-11** | *** |
| BMI (kg/m2) | -0.0127 | 0.0102 | ±0.0205 | -1.242 | 0.2144 |  |
| **Hypertension** | **-0.4093** | 0.1613 | ±0.3227 | **-2.537** | **0.0112** | * |
| High cholesterol | +0.1117 | 0.1546 | ±0.3091 | +0.722 | 0.4700 |  |
| Kidney disease | -0.6478 | 0.3464 | ±0.6928 | -1.870 | 0.0615 | . |
| Circulatory disease | -0.0554 | 0.2186 | ±0.4372 | -0.253 | 0.7999 |  |
| MAG (mg/dL/h) | -0.0069 | 0.0098 | ±0.0195 | -0.709 | 0.4785 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1271**, R² = **0.0792**, Adj R² = **0.0712**, F-statistic = **9.85** (p = **2.53e-17**), Residual SE = **2.553** on **1259** df, AIC = **6001.8**, BIC = **6063.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1287** | 0.6366 | ±1.2732 | **+25.336** | **1.28e-141** | *** |
| Education: graduate level (vs college) | +0.2149 | 0.1524 | ±0.3049 | +1.410 | 0.1586 |  |
| **Education: high school or below (vs college)** | **-1.1792** | 0.3510 | ±0.7021 | **-3.359** | **7.81e-04** | *** |
| Site: UCSD (vs UAB) | +0.1306 | 0.2027 | ±0.4053 | +0.644 | 0.5194 |  |
| Site: UW (vs UAB) | +0.0802 | 0.1963 | ±0.3927 | +0.409 | 0.6828 |  |
| **Age (years)** | **-0.0459** | 0.0071 | ±0.0141 | **-6.498** | **8.15e-11** | *** |
| BMI (kg/m2) | -0.0130 | 0.0102 | ±0.0205 | -1.273 | 0.2030 |  |
| **Hypertension** | **-0.4036** | 0.1619 | ±0.3239 | **-2.492** | **0.0127** | * |
| High cholesterol | +0.1158 | 0.1544 | ±0.3089 | +0.750 | 0.4532 |  |
| Kidney disease | -0.6446 | 0.3473 | ±0.6945 | -1.856 | 0.0634 | . |
| Circulatory disease | -0.0528 | 0.2187 | ±0.4375 | -0.241 | 0.8093 |  |
| Avg. daily range (mg/dL) | -0.0014 | 0.0031 | ±0.0061 | -0.466 | 0.6415 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1271**, R² = **0.0791**, Adj R² = **0.0710**, F-statistic = **9.83** (p = **2.76e-17**), Residual SE = **2.554** on **1259** df, AIC = **6002.0**, BIC = **6063.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9631** | 0.5883 | ±1.1766 | **+27.135** | **3.78e-162** | *** |
| Education: graduate level (vs college) | +0.2130 | 0.1526 | ±0.3053 | +1.396 | 0.1628 |  |
| **Education: high school or below (vs college)** | **-1.1818** | 0.3524 | ±0.7047 | **-3.354** | **7.97e-04** | *** |
| Site: UCSD (vs UAB) | +0.1378 | 0.2049 | ±0.4098 | +0.673 | 0.5012 |  |
| Site: UW (vs UAB) | +0.0778 | 0.1957 | ±0.3914 | +0.397 | 0.6910 |  |
| **Age (years)** | **-0.0461** | 0.0071 | ±0.0141 | **-6.533** | **6.46e-11** | *** |
| BMI (kg/m2) | -0.0130 | 0.0102 | ±0.0205 | -1.272 | 0.2032 |  |
| **Hypertension** | **-0.4092** | 0.1614 | ±0.3228 | **-2.536** | **0.0112** | * |
| High cholesterol | +0.1169 | 0.1543 | ±0.3086 | +0.757 | 0.4488 |  |
| Kidney disease | -0.6545 | 0.3448 | ±0.6897 | -1.898 | 0.0577 | . |
| Circulatory disease | -0.0600 | 0.2179 | ±0.4359 | -0.275 | 0.7830 |  |
| SD of daily means (mg/dL) | +0.0062 | 0.0214 | ±0.0427 | +0.288 | 0.7733 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1271**, R² = **0.0831**, Adj R² = **0.0751**, F-statistic = **10.37** (p = **2.20e-18**), Residual SE = **2.548** on **1259** df, AIC = **5996.4**, BIC = **6058.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.1121** | 0.9854 | ±1.9708 | **+14.321** | **1.61e-46** | *** |
| Education: graduate level (vs college) | +0.2217 | 0.1522 | ±0.3044 | +1.457 | 0.1452 |  |
| **Education: high school or below (vs college)** | **-1.1589** | 0.3487 | ±0.6974 | **-3.324** | **8.89e-04** | *** |
| Site: UCSD (vs UAB) | +0.1112 | 0.2018 | ±0.4037 | +0.551 | 0.5816 |  |
| Site: UW (vs UAB) | +0.0802 | 0.1951 | ±0.3901 | +0.411 | 0.6811 |  |
| **Age (years)** | **-0.0459** | 0.0070 | ±0.0141 | **-6.510** | **7.51e-11** | *** |
| BMI (kg/m2) | -0.0120 | 0.0103 | ±0.0207 | -1.164 | 0.2444 |  |
| **Hypertension** | **-0.3892** | 0.1613 | ±0.3226 | **-2.413** | **0.0158** | * |
| High cholesterol | +0.1247 | 0.1540 | ±0.3080 | +0.810 | 0.4181 |  |
| Kidney disease | -0.6217 | 0.3452 | ±0.6905 | -1.801 | 0.0717 | . |
| Circulatory disease | -0.0316 | 0.2178 | ±0.4356 | -0.145 | 0.8847 |  |
| **Time in range 70-180, pooled (%)** | **+0.0192** | 0.0077 | ±0.0154 | **+2.502** | **0.0123** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1271**, R² = **0.0834**, Adj R² = **0.0754**, F-statistic = **10.41** (p = **1.84e-18**), Residual SE = **2.548** on **1259** df, AIC = **5996.1**, BIC = **6057.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.0472** | 0.9817 | ±1.9634 | **+14.309** | **1.91e-46** | *** |
| Education: graduate level (vs college) | +0.2222 | 0.1522 | ±0.3044 | +1.460 | 0.1443 |  |
| **Education: high school or below (vs college)** | **-1.1603** | 0.3485 | ±0.6970 | **-3.330** | **8.70e-04** | *** |
| Site: UCSD (vs UAB) | +0.1115 | 0.2019 | ±0.4037 | +0.552 | 0.5807 |  |
| Site: UW (vs UAB) | +0.0798 | 0.1950 | ±0.3900 | +0.409 | 0.6824 |  |
| **Age (years)** | **-0.0458** | 0.0071 | ±0.0141 | **-6.503** | **7.87e-11** | *** |
| BMI (kg/m2) | -0.0119 | 0.0103 | ±0.0207 | -1.152 | 0.2493 |  |
| **Hypertension** | **-0.3892** | 0.1613 | ±0.3226 | **-2.413** | **0.0158** | * |
| High cholesterol | +0.1260 | 0.1540 | ±0.3080 | +0.818 | 0.4132 |  |
| Kidney disease | -0.6203 | 0.3449 | ±0.6898 | -1.799 | 0.0721 | . |
| Circulatory disease | -0.0307 | 0.2178 | ±0.4356 | -0.141 | 0.8879 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.0198** | 0.0076 | ±0.0152 | **+2.608** | **0.0091** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1271**, R² = **0.0826**, Adj R² = **0.0746**, F-statistic = **10.31** (p = **2.93e-18**), Residual SE = **2.549** on **1259** df, AIC = **5997.1**, BIC = **6058.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8260** | 0.5804 | ±1.1607 | **+27.269** | **9.90e-164** | *** |
| Education: graduate level (vs college) | +0.2286 | 0.1517 | ±0.3035 | +1.507 | 0.1319 |  |
| **Education: high school or below (vs college)** | **-1.1434** | 0.3488 | ±0.6976 | **-3.278** | **0.0010** | ** |
| Site: UCSD (vs UAB) | +0.1870 | 0.2065 | ±0.4129 | +0.905 | 0.3652 |  |
| Site: UW (vs UAB) | +0.1016 | 0.1965 | ±0.3929 | +0.517 | 0.6051 |  |
| **Age (years)** | **-0.0453** | 0.0070 | ±0.0141 | **-6.431** | **1.27e-10** | *** |
| BMI (kg/m2) | -0.0137 | 0.0102 | ±0.0204 | -1.350 | 0.1769 |  |
| **Hypertension** | **-0.4093** | 0.1612 | ±0.3224 | **-2.539** | **0.0111** | * |
| High cholesterol | +0.1356 | 0.1540 | ±0.3080 | +0.881 | 0.3786 |  |
| Kidney disease | -0.6513 | 0.3468 | ±0.6937 | -1.878 | 0.0604 | . |
| Circulatory disease | -0.0903 | 0.2164 | ±0.4328 | -0.417 | 0.6766 |  |
| **Any reading < 54 during wear (0/1)** | **+0.3472** | 0.1511 | ±0.3021 | **+2.298** | **0.0215** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1271**, R² = **0.0806**, Adj R² = **0.0726**, F-statistic = **10.03** (p = **1.06e-17**), Residual SE = **2.551** on **1259** df, AIC = **5999.9**, BIC = **6061.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9226** | 0.5802 | ±1.1603 | **+27.444** | **8.10e-166** | *** |
| Education: graduate level (vs college) | +0.2178 | 0.1524 | ±0.3048 | +1.429 | 0.1530 |  |
| **Education: high school or below (vs college)** | **-1.1641** | 0.3517 | ±0.7034 | **-3.310** | **9.32e-04** | *** |
| Site: UCSD (vs UAB) | +0.1694 | 0.2076 | ±0.4151 | +0.816 | 0.4145 |  |
| Site: UW (vs UAB) | +0.1037 | 0.1976 | ±0.3951 | +0.525 | 0.5998 |  |
| **Age (years)** | **-0.0459** | 0.0071 | ±0.0141 | **-6.500** | **8.01e-11** | *** |
| BMI (kg/m2) | -0.0126 | 0.0103 | ±0.0205 | -1.231 | 0.2183 |  |
| **Hypertension** | **-0.4018** | 0.1614 | ±0.3227 | **-2.490** | **0.0128** | * |
| High cholesterol | +0.1330 | 0.1548 | ±0.3096 | +0.859 | 0.3902 |  |
| Kidney disease | -0.6591 | 0.3445 | ±0.6891 | -1.913 | 0.0558 | . |
| Circulatory disease | -0.0572 | 0.2175 | ±0.4350 | -0.263 | 0.7924 |  |
| Time < 54 (%) | +0.1869 | 0.2093 | ±0.4186 | +0.893 | 0.3717 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1271**, R² = **0.0797**, Adj R² = **0.0716**, F-statistic = **9.91** (p = **1.92e-17**), Residual SE = **2.553** on **1259** df, AIC = **6001.2**, BIC = **6063.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9622** | 0.5789 | ±1.1578 | **+27.573** | **2.32e-167** | *** |
| Education: graduate level (vs college) | +0.2173 | 0.1525 | ±0.3050 | +1.425 | 0.1543 |  |
| **Education: high school or below (vs college)** | **-1.1706** | 0.3518 | ±0.7036 | **-3.327** | **8.77e-04** | *** |
| Site: UCSD (vs UAB) | +0.1544 | 0.2064 | ±0.4128 | +0.748 | 0.4544 |  |
| Site: UW (vs UAB) | +0.0968 | 0.1980 | ±0.3960 | +0.489 | 0.6249 |  |
| **Age (years)** | **-0.0461** | 0.0071 | ±0.0141 | **-6.541** | **6.11e-11** | *** |
| BMI (kg/m2) | -0.0127 | 0.0102 | ±0.0204 | -1.246 | 0.2126 |  |
| **Hypertension** | **-0.4019** | 0.1617 | ±0.3234 | **-2.485** | **0.0129** | * |
| High cholesterol | +0.1263 | 0.1545 | ±0.3090 | +0.817 | 0.4138 |  |
| Kidney disease | -0.6573 | 0.3446 | ±0.6892 | -1.908 | 0.0565 | . |
| Circulatory disease | -0.0567 | 0.2178 | ±0.4355 | -0.260 | 0.7946 |  |
| Avg. daily time < 54 (%) | +0.1601 | 0.1796 | ±0.3592 | +0.891 | 0.3728 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1271**, R² = **0.0804**, Adj R² = **0.0723**, F-statistic = **10.00** (p = **1.23e-17**), Residual SE = **2.552** on **1259** df, AIC = **6000.2**, BIC = **6062.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9190** | 0.5806 | ±1.1612 | **+27.418** | **1.69e-165** | *** |
| Education: graduate level (vs college) | +0.2239 | 0.1523 | ±0.3046 | +1.470 | 0.1416 |  |
| **Education: high school or below (vs college)** | **-1.1562** | 0.3521 | ±0.7043 | **-3.283** | **0.0010** | ** |
| Site: UCSD (vs UAB) | +0.1571 | 0.2053 | ±0.4106 | +0.765 | 0.4440 |  |
| Site: UW (vs UAB) | +0.1016 | 0.1972 | ±0.3943 | +0.515 | 0.6062 |  |
| **Age (years)** | **-0.0458** | 0.0071 | ±0.0141 | **-6.484** | **8.91e-11** | *** |
| BMI (kg/m2) | -0.0132 | 0.0102 | ±0.0204 | -1.299 | 0.1940 |  |
| **Hypertension** | **-0.4003** | 0.1619 | ±0.3238 | **-2.473** | **0.0134** | * |
| High cholesterol | +0.1289 | 0.1542 | ±0.3084 | +0.836 | 0.4033 |  |
| Kidney disease | -0.6528 | 0.3447 | ±0.6894 | -1.894 | 0.0583 | . |
| Circulatory disease | -0.0579 | 0.2179 | ±0.4359 | -0.266 | 0.7903 |  |
| Time 54-69, pooled (%) | +0.0702 | 0.0387 | ±0.0774 | +1.814 | 0.0696 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1271**, R² = **0.0798**, Adj R² = **0.0718**, F-statistic = **9.93** (p = **1.76e-17**), Residual SE = **2.553** on **1259** df, AIC = **6001.0**, BIC = **6062.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9469** | 0.5800 | ±1.1601 | **+27.493** | **2.13e-166** | *** |
| Education: graduate level (vs college) | +0.2221 | 0.1525 | ±0.3050 | +1.456 | 0.1453 |  |
| **Education: high school or below (vs college)** | **-1.1609** | 0.3525 | ±0.7049 | **-3.294** | **9.89e-04** | *** |
| Site: UCSD (vs UAB) | +0.1485 | 0.2049 | ±0.4098 | +0.725 | 0.4687 |  |
| Site: UW (vs UAB) | +0.0960 | 0.1973 | ±0.3945 | +0.487 | 0.6264 |  |
| **Age (years)** | **-0.0459** | 0.0071 | ±0.0141 | **-6.510** | **7.53e-11** | *** |
| BMI (kg/m2) | -0.0131 | 0.0102 | ±0.0204 | -1.287 | 0.1980 |  |
| **Hypertension** | **-0.4014** | 0.1620 | ±0.3240 | **-2.478** | **0.0132** | * |
| High cholesterol | +0.1253 | 0.1542 | ±0.3083 | +0.813 | 0.4162 |  |
| Kidney disease | -0.6528 | 0.3448 | ±0.6896 | -1.893 | 0.0584 | . |
| Circulatory disease | -0.0576 | 0.2180 | ±0.4360 | -0.264 | 0.7917 |  |
| Avg. daily time 54-69 (%) | +0.0534 | 0.0382 | ±0.0764 | +1.397 | 0.1626 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1271**, R² = **0.0808**, Adj R² = **0.0728**, F-statistic = **10.06** (p = **9.46e-18**), Residual SE = **2.551** on **1259** df, AIC = **5999.6**, BIC = **6061.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9007** | 0.5812 | ±1.1624 | **+27.357** | **8.84e-165** | *** |
| Education: graduate level (vs college) | +0.2245 | 0.1522 | ±0.3045 | +1.474 | 0.1404 |  |
| **Education: high school or below (vs college)** | **-1.1525** | 0.3521 | ±0.7042 | **-3.273** | **0.0011** | ** |
| Site: UCSD (vs UAB) | +0.1668 | 0.2061 | ±0.4122 | +0.809 | 0.4183 |  |
| Site: UW (vs UAB) | +0.1081 | 0.1977 | ±0.3954 | +0.547 | 0.5844 |  |
| **Age (years)** | **-0.0458** | 0.0071 | ±0.0141 | **-6.485** | **8.89e-11** | *** |
| BMI (kg/m2) | -0.0131 | 0.0102 | ±0.0204 | -1.289 | 0.1974 |  |
| **Hypertension** | **-0.3987** | 0.1618 | ±0.3237 | **-2.464** | **0.0137** | * |
| High cholesterol | +0.1331 | 0.1543 | ±0.3087 | +0.862 | 0.3886 |  |
| Kidney disease | -0.6546 | 0.3447 | ±0.6893 | -1.899 | 0.0575 | . |
| Circulatory disease | -0.0578 | 0.2178 | ±0.4356 | -0.265 | 0.7908 |  |
| **Time < 70 (%)** | **+0.0639** | 0.0289 | ±0.0578 | **+2.211** | **0.0271** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1271**, R² = **0.0799**, Adj R² = **0.0719**, F-statistic = **9.94** (p = **1.64e-17**), Residual SE = **2.552** on **1259** df, AIC = **6000.9**, BIC = **6062.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9421** | 0.5804 | ±1.1607 | **+27.469** | **4.10e-166** | *** |
| Education: graduate level (vs college) | +0.2223 | 0.1525 | ±0.3050 | +1.458 | 0.1449 |  |
| **Education: high school or below (vs college)** | **-1.1598** | 0.3524 | ±0.7049 | **-3.291** | **9.98e-04** | *** |
| Site: UCSD (vs UAB) | +0.1527 | 0.2054 | ±0.4108 | +0.744 | 0.4571 |  |
| Site: UW (vs UAB) | +0.0995 | 0.1977 | ±0.3955 | +0.503 | 0.6146 |  |
| **Age (years)** | **-0.0460** | 0.0071 | ±0.0141 | **-6.516** | **7.20e-11** | *** |
| BMI (kg/m2) | -0.0131 | 0.0102 | ±0.0204 | -1.282 | 0.1998 |  |
| **Hypertension** | **-0.4002** | 0.1620 | ±0.3240 | **-2.470** | **0.0135** | * |
| High cholesterol | +0.1270 | 0.1542 | ±0.3085 | +0.824 | 0.4101 |  |
| Kidney disease | -0.6539 | 0.3448 | ±0.6896 | -1.896 | 0.0579 | . |
| Circulatory disease | -0.0573 | 0.2180 | ±0.4360 | -0.263 | 0.7926 |  |
| Avg. daily time < 70 (%) | +0.0475 | 0.0299 | ±0.0598 | +1.590 | 0.1119 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1271**, R² = **0.0829**, Adj R² = **0.0749**, F-statistic = **10.35** (p = **2.45e-18**), Residual SE = **2.548** on **1259** df, AIC = **5996.7**, BIC = **6058.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.6188** | 1.3894 | ±2.7787 | **+9.082** | **1.06e-19** | *** |
| Education: graduate level (vs college) | +0.2153 | 0.1525 | ±0.3050 | +1.412 | 0.1581 |  |
| **Education: high school or below (vs college)** | **-1.1384** | 0.3489 | ±0.6978 | **-3.263** | **0.0011** | ** |
| Site: UCSD (vs UAB) | +0.1215 | 0.2034 | ±0.4068 | +0.597 | 0.5502 |  |
| Site: UW (vs UAB) | +0.0703 | 0.1954 | ±0.3908 | +0.360 | 0.7192 |  |
| **Age (years)** | **-0.0463** | 0.0070 | ±0.0141 | **-6.572** | **4.96e-11** | *** |
| BMI (kg/m2) | -0.0128 | 0.0102 | ±0.0204 | -1.255 | 0.2094 |  |
| **Hypertension** | **-0.4050** | 0.1608 | ±0.3216 | **-2.519** | **0.0118** | * |
| High cholesterol | +0.1114 | 0.1537 | ±0.3074 | +0.725 | 0.4684 |  |
| Kidney disease | -0.6482 | 0.3441 | ±0.6883 | -1.884 | 0.0596 | . |
| Circulatory disease | -0.0231 | 0.2176 | ±0.4352 | -0.106 | 0.9156 |  |
| **Time 54-250, pooled (%)** | **+0.0341** | 0.0127 | ±0.0254 | **+2.685** | **0.0072** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1271**, R² = **0.0832**, Adj R² = **0.0752**, F-statistic = **10.39** (p = **2.01e-18**), Residual SE = **2.548** on **1259** df, AIC = **5996.2**, BIC = **6058.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.4017** | 1.4043 | ±2.8086 | **+8.831** | **1.04e-18** | *** |
| Education: graduate level (vs college) | +0.2155 | 0.1525 | ±0.3050 | +1.413 | 0.1576 |  |
| **Education: high school or below (vs college)** | **-1.1352** | 0.3489 | ±0.6978 | **-3.253** | **0.0011** | ** |
| Site: UCSD (vs UAB) | +0.1229 | 0.2033 | ±0.4066 | +0.604 | 0.5456 |  |
| Site: UW (vs UAB) | +0.0710 | 0.1954 | ±0.3908 | +0.363 | 0.7163 |  |
| **Age (years)** | **-0.0462** | 0.0070 | ±0.0141 | **-6.567** | **5.15e-11** | *** |
| BMI (kg/m2) | -0.0127 | 0.0102 | ±0.0204 | -1.247 | 0.2125 |  |
| **Hypertension** | **-0.4050** | 0.1608 | ±0.3215 | **-2.519** | **0.0118** | * |
| High cholesterol | +0.1118 | 0.1536 | ±0.3073 | +0.728 | 0.4668 |  |
| Kidney disease | -0.6490 | 0.3440 | ±0.6881 | -1.886 | 0.0592 | . |
| Circulatory disease | -0.0212 | 0.2176 | ±0.4352 | -0.097 | 0.9225 |  |
| **Avg. daily time 54-250 (%)** | **+0.0362** | 0.0128 | ±0.0256 | **+2.825** | **0.0047** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1271**, R² = **0.0817**, Adj R² = **0.0736**, F-statistic = **10.18** (p = **5.42e-18**), Residual SE = **2.550** on **1259** df, AIC = **5998.4**, BIC = **6060.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9930** | 0.5801 | ±1.1601 | **+27.571** | **2.46e-167** | *** |
| Education: graduate level (vs college) | +0.2253 | 0.1519 | ±0.3038 | +1.483 | 0.1381 |  |
| **Education: high school or below (vs college)** | **-1.1753** | 0.3514 | ±0.7028 | **-3.345** | **8.23e-04** | *** |
| Site: UCSD (vs UAB) | +0.1231 | 0.2024 | ±0.4047 | +0.608 | 0.5430 |  |
| Site: UW (vs UAB) | +0.0934 | 0.1967 | ±0.3933 | +0.475 | 0.6348 |  |
| **Age (years)** | **-0.0456** | 0.0071 | ±0.0141 | **-6.459** | **1.05e-10** | *** |
| BMI (kg/m2) | -0.0120 | 0.0104 | ±0.0207 | -1.162 | 0.2454 |  |
| **Hypertension** | **-0.3855** | 0.1620 | ±0.3241 | **-2.379** | **0.0174** | * |
| High cholesterol | +0.1337 | 0.1547 | ±0.3093 | +0.865 | 0.3873 |  |
| Kidney disease | -0.6194 | 0.3464 | ±0.6928 | -1.788 | 0.0738 | . |
| Circulatory disease | -0.0500 | 0.2179 | ±0.4358 | -0.229 | 0.8186 |  |
| Time 181-250, pooled (%) | -0.0227 | 0.0124 | ±0.0248 | -1.824 | 0.0681 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1271**, R² = **0.0817**, Adj R² = **0.0736**, F-statistic = **10.18** (p = **5.42e-18**), Residual SE = **2.550** on **1259** df, AIC = **5998.4**, BIC = **6060.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9921** | 0.5801 | ±1.1601 | **+27.569** | **2.59e-167** | *** |
| Education: graduate level (vs college) | +0.2257 | 0.1519 | ±0.3039 | +1.485 | 0.1374 |  |
| **Education: high school or below (vs college)** | **-1.1775** | 0.3512 | ±0.7025 | **-3.353** | **8.01e-04** | *** |
| Site: UCSD (vs UAB) | +0.1216 | 0.2023 | ±0.4045 | +0.601 | 0.5478 |  |
| Site: UW (vs UAB) | +0.0919 | 0.1965 | ±0.3929 | +0.468 | 0.6398 |  |
| **Age (years)** | **-0.0457** | 0.0071 | ±0.0141 | **-6.465** | **1.02e-10** | *** |
| BMI (kg/m2) | -0.0120 | 0.0104 | ±0.0207 | -1.157 | 0.2474 |  |
| **Hypertension** | **-0.3858** | 0.1621 | ±0.3241 | **-2.381** | **0.0173** | * |
| High cholesterol | +0.1339 | 0.1546 | ±0.3093 | +0.866 | 0.3864 |  |
| Kidney disease | -0.6185 | 0.3462 | ±0.6923 | -1.787 | 0.0740 | . |
| Circulatory disease | -0.0497 | 0.2180 | ±0.4359 | -0.228 | 0.8197 |  |
| Avg. daily time 181-250 (%) | -0.0224 | 0.0121 | ±0.0241 | -1.857 | 0.0633 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1271**, R² = **0.0842**, Adj R² = **0.0762**, F-statistic = **10.53** (p = **1.07e-18**), Residual SE = **2.546** on **1259** df, AIC = **5994.9**, BIC = **6056.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0064** | 0.5799 | ±1.1599 | **+27.601** | **1.09e-167** | *** |
| Education: graduate level (vs college) | +0.2267 | 0.1520 | ±0.3041 | +1.491 | 0.1360 |  |
| **Education: high school or below (vs college)** | **-1.1459** | 0.3487 | ±0.6974 | **-3.286** | **0.0010** | ** |
| Site: UCSD (vs UAB) | +0.1188 | 0.2020 | ±0.4040 | +0.588 | 0.5564 |  |
| Site: UW (vs UAB) | +0.0905 | 0.1954 | ±0.3909 | +0.463 | 0.6434 |  |
| **Age (years)** | **-0.0458** | 0.0070 | ±0.0141 | **-6.491** | **8.51e-11** | *** |
| BMI (kg/m2) | -0.0120 | 0.0104 | ±0.0207 | -1.164 | 0.2446 |  |
| **Hypertension** | **-0.3834** | 0.1615 | ±0.3230 | **-2.374** | **0.0176** | * |
| High cholesterol | +0.1308 | 0.1540 | ±0.3080 | +0.849 | 0.3957 |  |
| Kidney disease | -0.6177 | 0.3452 | ±0.6904 | -1.789 | 0.0736 | . |
| Circulatory disease | -0.0282 | 0.2180 | ±0.4361 | -0.129 | 0.8970 |  |
| **Time > 180 (%)** | **-0.0217** | 0.0078 | ±0.0155 | **-2.802** | **0.0051** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1271**, R² = **0.0841**, Adj R² = **0.0761**, F-statistic = **10.52** (p = **1.13e-18**), Residual SE = **2.547** on **1259** df, AIC = **5995.0**, BIC = **6056.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0032** | 0.5800 | ±1.1601 | **+27.590** | **1.46e-167** | *** |
| Education: graduate level (vs college) | +0.2271 | 0.1520 | ±0.3041 | +1.493 | 0.1353 |  |
| **Education: high school or below (vs college)** | **-1.1484** | 0.3486 | ±0.6972 | **-3.294** | **9.87e-04** | *** |
| Site: UCSD (vs UAB) | +0.1173 | 0.2020 | ±0.4040 | +0.581 | 0.5614 |  |
| Site: UW (vs UAB) | +0.0894 | 0.1954 | ±0.3908 | +0.458 | 0.6472 |  |
| **Age (years)** | **-0.0458** | 0.0071 | ±0.0141 | **-6.494** | **8.38e-11** | *** |
| BMI (kg/m2) | -0.0120 | 0.0103 | ±0.0207 | -1.155 | 0.2481 |  |
| **Hypertension** | **-0.3837** | 0.1615 | ±0.3231 | **-2.376** | **0.0175** | * |
| High cholesterol | +0.1309 | 0.1540 | ±0.3080 | +0.850 | 0.3953 |  |
| Kidney disease | -0.6173 | 0.3450 | ±0.6900 | -1.789 | 0.0736 | . |
| Circulatory disease | -0.0282 | 0.2180 | ±0.4361 | -0.129 | 0.8971 |  |
| **Avg. daily time > 180 (%)** | **-0.0215** | 0.0077 | ±0.0153 | **-2.802** | **0.0051** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1271**, R² = **0.0826**, Adj R² = **0.0746**, F-statistic = **10.31** (p = **2.93e-18**), Residual SE = **2.549** on **1259** df, AIC = **5997.1**, BIC = **6058.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.9753** | 0.5810 | ±1.1620 | **+27.496** | **1.96e-166** | *** |
| Education: graduate level (vs college) | +0.2152 | 0.1524 | ±0.3048 | +1.412 | 0.1580 |  |
| **Education: high school or below (vs college)** | **-1.1547** | 0.3491 | ±0.6982 | **-3.308** | **9.40e-04** | *** |
| Site: UCSD (vs UAB) | +0.1263 | 0.2034 | ±0.4068 | +0.621 | 0.5346 |  |
| Site: UW (vs UAB) | +0.0855 | 0.1956 | ±0.3912 | +0.437 | 0.6619 |  |
| **Age (years)** | **-0.0462** | 0.0071 | ±0.0141 | **-6.553** | **5.64e-11** | *** |
| BMI (kg/m2) | -0.0108 | 0.0104 | ±0.0208 | -1.042 | 0.2976 |  |
| **Hypertension** | **-0.3985** | 0.1614 | ±0.3228 | **-2.469** | **0.0135** | * |
| High cholesterol | +0.1348 | 0.1541 | ±0.3083 | +0.875 | 0.3818 |  |
| Kidney disease | -0.6554 | 0.3438 | ±0.6876 | -1.906 | 0.0566 | . |
| Circulatory disease | -0.0478 | 0.2168 | ±0.4336 | -0.220 | 0.8257 |  |
| **Nocturnal time > 180 (%)** | **-0.0190** | 0.0078 | ±0.0155 | **-2.454** | **0.0141** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1271**, R² = **0.0791**, Adj R² = **0.0710**, F-statistic = **9.83** (p = **2.78e-17**), Residual SE = **2.554** on **1259** df, AIC = **6002.0**, BIC = **6063.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0071** | 0.5783 | ±1.1567 | **+27.678** | **1.30e-168** | *** |
| Education: graduate level (vs college) | +0.2130 | 0.1528 | ±0.3055 | +1.394 | 0.1633 |  |
| **Education: high school or below (vs college)** | **-1.1820** | 0.3517 | ±0.7034 | **-3.361** | **7.77e-04** | *** |
| Site: UCSD (vs UAB) | +0.1341 | 0.2036 | ±0.4073 | +0.659 | 0.5101 |  |
| Site: UW (vs UAB) | +0.0790 | 0.1961 | ±0.3923 | +0.403 | 0.6871 |  |
| **Age (years)** | **-0.0460** | 0.0071 | ±0.0141 | **-6.528** | **6.69e-11** | *** |
| BMI (kg/m2) | -0.0130 | 0.0102 | ±0.0205 | -1.269 | 0.2045 |  |
| **Hypertension** | **-0.4059** | 0.1614 | ±0.3229 | **-2.514** | **0.0119** | * |
| High cholesterol | +0.1185 | 0.1543 | ±0.3086 | +0.768 | 0.4425 |  |
| Kidney disease | -0.6532 | 0.3454 | ±0.6907 | -1.891 | 0.0586 | . |
| Circulatory disease | -0.0577 | 0.2179 | ±0.4358 | -0.265 | 0.7913 |  |
| Any reading > 250 during wear (0/1) | -0.0436 | 0.1947 | ±0.3893 | -0.224 | 0.8227 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1271**, R² = **0.0836**, Adj R² = **0.0756**, F-statistic = **10.44** (p = **1.63e-18**), Residual SE = **2.547** on **1259** df, AIC = **5995.8**, BIC = **6057.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0191** | 0.5773 | ±1.1545 | **+27.750** | **1.76e-169** | *** |
| Education: graduate level (vs college) | +0.2164 | 0.1525 | ±0.3050 | +1.419 | 0.1559 |  |
| **Education: high school or below (vs college)** | **-1.1312** | 0.3491 | ±0.6982 | **-3.240** | **0.0012** | ** |
| Site: UCSD (vs UAB) | +0.1271 | 0.2032 | ±0.4064 | +0.625 | 0.5317 |  |
| Site: UW (vs UAB) | +0.0745 | 0.1953 | ±0.3906 | +0.382 | 0.7027 |  |
| **Age (years)** | **-0.0463** | 0.0070 | ±0.0141 | **-6.573** | **4.94e-11** | *** |
| BMI (kg/m2) | -0.0128 | 0.0102 | ±0.0204 | -1.252 | 0.2106 |  |
| **Hypertension** | **-0.4034** | 0.1608 | ±0.3215 | **-2.509** | **0.0121** | * |
| High cholesterol | +0.1139 | 0.1536 | ±0.3072 | +0.742 | 0.4583 |  |
| Kidney disease | -0.6487 | 0.3440 | ±0.6880 | -1.886 | 0.0593 | . |
| Circulatory disease | -0.0200 | 0.2176 | ±0.4352 | -0.092 | 0.9266 |  |
| **Time > 250 (%)** | **-0.0370** | 0.0127 | ±0.0254 | **-2.914** | **0.0036** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,271)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1271**, R² = **0.0836**, Adj R² = **0.0755**, F-statistic = **10.43** (p = **1.64e-18**), Residual SE = **2.547** on **1259** df, AIC = **5995.8**, BIC = **6057.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.0157** | 0.5774 | ±1.1547 | **+27.739** | **2.37e-169** | *** |
| Education: graduate level (vs college) | +0.2166 | 0.1525 | ±0.3050 | +1.420 | 0.1556 |  |
| **Education: high school or below (vs college)** | **-1.1306** | 0.3491 | ±0.6983 | **-3.238** | **0.0012** | ** |
| Site: UCSD (vs UAB) | +0.1269 | 0.2032 | ±0.4064 | +0.624 | 0.5324 |  |
| Site: UW (vs UAB) | +0.0750 | 0.1953 | ±0.3906 | +0.384 | 0.7009 |  |
| **Age (years)** | **-0.0463** | 0.0070 | ±0.0141 | **-6.571** | **5.01e-11** | *** |
| BMI (kg/m2) | -0.0127 | 0.0102 | ±0.0204 | -1.245 | 0.2133 |  |
| **Hypertension** | **-0.4033** | 0.1608 | ±0.3216 | **-2.508** | **0.0121** | * |
| High cholesterol | +0.1136 | 0.1536 | ±0.3072 | +0.739 | 0.4597 |  |
| Kidney disease | -0.6496 | 0.3440 | ±0.6880 | -1.888 | 0.0590 | . |
| Circulatory disease | -0.0195 | 0.2176 | ±0.4352 | -0.089 | 0.9287 |  |
| **Avg. daily time > 250 (%)** | **-0.0377** | 0.0129 | ±0.0257 | **-2.928** | **0.0034** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
