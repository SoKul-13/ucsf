# Phase 6 model output tables - All (analysis base) - Healthy group (no diabetes + pre-diabetes / lifestyle)

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models.


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


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 1,270; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0914**, F-statistic = **13.77** (p = **2.80e-23**), Residual SE = **4.595** on **1259** df, AIC = **7488.4**, BIC = **7545.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4220** | 1.0738 | ±2.1476 | **+6.912** | **4.79e-12** | *** |
| Education: graduate level (vs college) | -0.4358 | 0.2745 | ±0.5489 | -1.588 | 0.1123 |  |
| **Education: high school or below (vs college)** | **+1.3322** | 0.5851 | ±1.1702 | **+2.277** | **0.0228** | * |
| Site: UCSD (vs UAB) | -0.2311 | 0.3587 | ±0.7174 | -0.644 | 0.5194 |  |
| Site: UW (vs UAB) | +0.0039 | 0.3349 | ±0.6699 | +0.012 | 0.9908 |  |
| **Age (years)** | **-0.0882** | 0.0122 | ±0.0244 | **-7.226** | **4.99e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0478 | **+4.099** | **4.14e-05** | *** |
| Hypertension | +0.5028 | 0.2981 | ±0.5963 | +1.687 | 0.0917 | . |
| **High cholesterol** | **+0.7229** | 0.2676 | ±0.5353 | **+2.701** | **0.0069** | ** |
| Kidney disease | +0.8364 | 0.5977 | ±1.1953 | +1.399 | 0.1617 |  |
| **Circulatory disease** | **+0.9609** | 0.4401 | ±0.8803 | **+2.183** | **0.0290** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0907**, F-statistic = **12.51** (p = **1.07e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.5651** | 1.7905 | ±3.5810 | **+4.225** | **2.39e-05** | *** |
| Education: graduate level (vs college) | -0.4356 | 0.2749 | ±0.5497 | -1.585 | 0.1130 |  |
| **Education: high school or below (vs college)** | **+1.3360** | 0.5895 | ±1.1790 | **+2.266** | **0.0234** | * |
| Site: UCSD (vs UAB) | -0.2304 | 0.3589 | ±0.7177 | -0.642 | 0.5208 |  |
| Site: UW (vs UAB) | +0.0049 | 0.3353 | ±0.6706 | +0.015 | 0.9883 |  |
| **Age (years)** | **-0.0881** | 0.0124 | ±0.0247 | **-7.128** | **1.02e-12** | *** |
| **BMI (kg/m2)** | **+0.0982** | 0.0238 | ±0.0477 | **+4.121** | **3.77e-05** | *** |
| Hypertension | +0.5043 | 0.2989 | ±0.5977 | +1.688 | 0.0915 | . |
| **High cholesterol** | **+0.7259** | 0.2705 | ±0.5409 | **+2.684** | **0.0073** | ** |
| Kidney disease | +0.8360 | 0.5984 | ±1.1967 | +1.397 | 0.1624 |  |
| **Circulatory disease** | **+0.9631** | 0.4397 | ±0.8795 | **+2.190** | **0.0285** | * |
| HbA1c (%) | -0.0281 | 0.2814 | ±0.5627 | -0.100 | 0.9205 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1270**, R² = **0.0987**, Adj R² = **0.0909**, F-statistic = **12.53** (p = **9.68e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.2**, BIC = **7552.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.7712** | 1.3806 | ±2.7612 | **+5.629** | **1.81e-08** | *** |
| Education: graduate level (vs college) | -0.4282 | 0.2756 | ±0.5511 | -1.554 | 0.1202 |  |
| **Education: high school or below (vs college)** | **+1.3477** | 0.5901 | ±1.1802 | **+2.284** | **0.0224** | * |
| Site: UCSD (vs UAB) | -0.2329 | 0.3590 | ±0.7180 | -0.649 | 0.5165 |  |
| Site: UW (vs UAB) | +0.0134 | 0.3365 | ±0.6731 | +0.040 | 0.9683 |  |
| **Age (years)** | **-0.0880** | 0.0122 | ±0.0245 | **-7.187** | **6.61e-13** | *** |
| **BMI (kg/m2)** | **+0.0984** | 0.0239 | ±0.0477 | **+4.124** | **3.73e-05** | *** |
| Hypertension | +0.5133 | 0.2994 | ±0.5989 | +1.714 | 0.0865 | . |
| **High cholesterol** | **+0.7292** | 0.2681 | ±0.5361 | **+2.720** | **0.0065** | ** |
| Kidney disease | +0.8463 | 0.5982 | ±1.1964 | +1.415 | 0.1572 |  |
| **Circulatory disease** | **+0.9711** | 0.4410 | ±0.8820 | **+2.202** | **0.0277** | * |
| Mean glucose (mg/dL) | -0.0032 | 0.0078 | ±0.0156 | -0.414 | 0.6792 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1270**, R² = **0.0987**, Adj R² = **0.0909**, F-statistic = **12.53** (p = **9.68e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.2**, BIC = **7552.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2182** | 2.2246 | ±4.4492 | **+3.694** | **2.21e-04** | *** |
| Education: graduate level (vs college) | -0.4282 | 0.2756 | ±0.5511 | -1.554 | 0.1202 |  |
| **Education: high school or below (vs college)** | **+1.3477** | 0.5901 | ±1.1802 | **+2.284** | **0.0224** | * |
| Site: UCSD (vs UAB) | -0.2329 | 0.3590 | ±0.7180 | -0.649 | 0.5165 |  |
| Site: UW (vs UAB) | +0.0134 | 0.3365 | ±0.6731 | +0.040 | 0.9683 |  |
| **Age (years)** | **-0.0880** | 0.0122 | ±0.0245 | **-7.187** | **6.61e-13** | *** |
| **BMI (kg/m2)** | **+0.0984** | 0.0239 | ±0.0477 | **+4.124** | **3.73e-05** | *** |
| Hypertension | +0.5133 | 0.2994 | ±0.5989 | +1.714 | 0.0865 | . |
| **High cholesterol** | **+0.7292** | 0.2681 | ±0.5361 | **+2.720** | **0.0065** | ** |
| Kidney disease | +0.8463 | 0.5982 | ±1.1964 | +1.415 | 0.1572 |  |
| **Circulatory disease** | **+0.9711** | 0.4410 | ±0.8820 | **+2.202** | **0.0277** | * |
| GMI (%) | -0.1350 | 0.3265 | ±0.6531 | -0.414 | 0.6792 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1270**, R² = **0.0987**, Adj R² = **0.0908**, F-statistic = **12.52** (p = **1.00e-22**), Residual SE = **4.596** on **1258** df, AIC = **7490.3**, BIC = **7552.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.6920** | 1.3362 | ±2.6724 | **+5.757** | **8.58e-09** | *** |
| Education: graduate level (vs college) | -0.4314 | 0.2755 | ±0.5509 | -1.566 | 0.1173 |  |
| **Education: high school or below (vs college)** | **+1.3451** | 0.5902 | ±1.1803 | **+2.279** | **0.0227** | * |
| Site: UCSD (vs UAB) | -0.2289 | 0.3590 | ±0.7180 | -0.638 | 0.5237 |  |
| Site: UW (vs UAB) | +0.0111 | 0.3360 | ±0.6720 | +0.033 | 0.9735 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.232** | **4.76e-13** | *** |
| **BMI (kg/m2)** | **+0.0990** | 0.0240 | ±0.0480 | **+4.128** | **3.65e-05** | *** |
| Hypertension | +0.5095 | 0.2982 | ±0.5964 | +1.708 | 0.0876 | . |
| **High cholesterol** | **+0.7300** | 0.2680 | ±0.5360 | **+2.724** | **0.0065** | ** |
| Kidney disease | +0.8376 | 0.5976 | ±1.1952 | +1.402 | 0.1610 |  |
| **Circulatory disease** | **+0.9662** | 0.4409 | ±0.8817 | **+2.192** | **0.0284** | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0026 | 0.0076 | ±0.0151 | -0.338 | 0.7354 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0907**, F-statistic = **12.51** (p = **1.07e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4523** | 1.1550 | ±2.3101 | **+6.452** | **1.10e-10** | *** |
| Education: graduate level (vs college) | -0.4355 | 0.2747 | ±0.5493 | -1.586 | 0.1128 |  |
| **Education: high school or below (vs college)** | **+1.3324** | 0.5856 | ±1.1711 | **+2.275** | **0.0229** | * |
| Site: UCSD (vs UAB) | -0.2325 | 0.3583 | ±0.7166 | -0.649 | 0.5163 |  |
| Site: UW (vs UAB) | +0.0047 | 0.3362 | ±0.6725 | +0.014 | 0.9890 |  |
| **Age (years)** | **-0.0881** | 0.0123 | ±0.0245 | **-7.186** | **6.68e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0478 | **+4.099** | **4.14e-05** | *** |
| Hypertension | +0.5048 | 0.3006 | ±0.6012 | +1.679 | 0.0931 | . |
| **High cholesterol** | **+0.7228** | 0.2678 | ±0.5357 | **+2.699** | **0.0070** | ** |
| Kidney disease | +0.8397 | 0.5978 | ±1.1956 | +1.405 | 0.1601 |  |
| **Circulatory disease** | **+0.9625** | 0.4410 | ±0.8821 | **+2.182** | **0.0291** | * |
| Glucose SD, pooled (mg/dL) | -0.0017 | 0.0206 | ±0.0412 | -0.081 | 0.9358 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1270**, R² = **0.0987**, Adj R² = **0.0908**, F-statistic = **12.52** (p = **1.02e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.3**, BIC = **7552.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.5380** | 1.1435 | ±2.2870 | **+6.592** | **4.34e-11** | *** |
| Education: graduate level (vs college) | -0.4340 | 0.2747 | ±0.5494 | -1.580 | 0.1141 |  |
| **Education: high school or below (vs college)** | **+1.3332** | 0.5861 | ±1.1722 | **+2.275** | **0.0229** | * |
| Site: UCSD (vs UAB) | -0.2364 | 0.3581 | ±0.7162 | -0.660 | 0.5092 |  |
| Site: UW (vs UAB) | +0.0078 | 0.3367 | ±0.6734 | +0.023 | 0.9816 |  |
| **Age (years)** | **-0.0879** | 0.0123 | ±0.0246 | **-7.159** | **8.10e-13** | *** |
| **BMI (kg/m2)** | **+0.0981** | 0.0239 | ±0.0478 | **+4.109** | **3.97e-05** | *** |
| Hypertension | +0.5109 | 0.3005 | ±0.6010 | +1.700 | 0.0891 | . |
| **High cholesterol** | **+0.7229** | 0.2678 | ±0.5356 | **+2.699** | **0.0069** | ** |
| Kidney disease | +0.8509 | 0.5983 | ±1.1967 | +1.422 | 0.1550 |  |
| **Circulatory disease** | **+0.9674** | 0.4410 | ±0.8820 | **+2.194** | **0.0282** | * |
| Avg. daily SD (mg/dL) | -0.0073 | 0.0225 | ±0.0450 | -0.326 | 0.7446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0908**, F-statistic = **12.51** (p = **1.04e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.2921** | 1.2139 | ±2.4279 | **+6.007** | **1.89e-09** | *** |
| Education: graduate level (vs college) | -0.4339 | 0.2751 | ±0.5501 | -1.577 | 0.1147 |  |
| **Education: high school or below (vs college)** | **+1.3360** | 0.5873 | ±1.1746 | **+2.275** | **0.0229** | * |
| Site: UCSD (vs UAB) | -0.2258 | 0.3578 | ±0.7157 | -0.631 | 0.5281 |  |
| Site: UW (vs UAB) | +0.0047 | 0.3348 | ±0.6697 | +0.014 | 0.9887 |  |
| **Age (years)** | **-0.0884** | 0.0122 | ±0.0245 | **-7.215** | **5.38e-13** | *** |
| **BMI (kg/m2)** | **+0.0981** | 0.0240 | ±0.0479 | **+4.092** | **4.27e-05** | *** |
| Hypertension | +0.4992 | 0.2994 | ±0.5987 | +1.668 | 0.0954 | . |
| **High cholesterol** | **+0.7258** | 0.2678 | ±0.5356 | **+2.710** | **0.0067** | ** |
| Kidney disease | +0.8283 | 0.5970 | ±1.1941 | +1.387 | 0.1653 |  |
| **Circulatory disease** | **+0.9590** | 0.4406 | ±0.8813 | **+2.176** | **0.0295** | * |
| CV (%) | +0.0077 | 0.0304 | ±0.0608 | +0.252 | 0.8013 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1270**, R² = **0.0988**, Adj R² = **0.0909**, F-statistic = **12.54** (p = **9.35e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.1**, BIC = **7551.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.7759** | 1.2268 | ±2.4536 | **+6.338** | **2.32e-10** | *** |
| Education: graduate level (vs college) | -0.4309 | 0.2751 | ±0.5502 | -1.566 | 0.1173 |  |
| **Education: high school or below (vs college)** | **+1.3353** | 0.5850 | ±1.1700 | **+2.282** | **0.0225** | * |
| Site: UCSD (vs UAB) | -0.2204 | 0.3580 | ±0.7159 | -0.616 | 0.5380 |  |
| Site: UW (vs UAB) | +0.0024 | 0.3355 | ±0.6709 | +0.007 | 0.9942 |  |
| **Age (years)** | **-0.0886** | 0.0123 | ±0.0245 | **-7.227** | **4.95e-13** | *** |
| **BMI (kg/m2)** | **+0.0982** | 0.0239 | ±0.0479 | **+4.101** | **4.11e-05** | *** |
| Hypertension | +0.4939 | 0.2995 | ±0.5990 | +1.649 | 0.0992 | . |
| **High cholesterol** | **+0.7274** | 0.2677 | ±0.5355 | **+2.717** | **0.0066** | ** |
| Kidney disease | +0.8225 | 0.5962 | ±1.1924 | +1.380 | 0.1677 |  |
| **Circulatory disease** | **+0.9581** | 0.4406 | ±0.8811 | **+2.175** | **0.0297** | * |
| Mean / SD ratio | -0.0574 | 0.1017 | ±0.2034 | -0.564 | 0.5727 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0907**, F-statistic = **12.51** (p = **1.05e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.2850** | 1.2499 | ±2.4999 | **+5.828** | **5.60e-09** | *** |
| Education: graduate level (vs college) | -0.4367 | 0.2748 | ±0.5496 | -1.589 | 0.1120 |  |
| **Education: high school or below (vs college)** | **+1.3321** | 0.5860 | ±1.1720 | **+2.273** | **0.0230** | * |
| Site: UCSD (vs UAB) | -0.2342 | 0.3579 | ±0.7158 | -0.654 | 0.5128 |  |
| Site: UW (vs UAB) | +0.0050 | 0.3359 | ±0.6719 | +0.015 | 0.9881 |  |
| **Age (years)** | **-0.0880** | 0.0123 | ±0.0245 | **-7.169** | **7.57e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0478 | **+4.099** | **4.16e-05** | *** |
| Hypertension | +0.5053 | 0.2992 | ±0.5984 | +1.689 | 0.0913 | . |
| **High cholesterol** | **+0.7213** | 0.2677 | ±0.5355 | **+2.694** | **0.0071** | ** |
| Kidney disease | +0.8432 | 0.5981 | ±1.1962 | +1.410 | 0.1586 |  |
| **Circulatory disease** | **+0.9616** | 0.4405 | ±0.8810 | **+2.183** | **0.0290** | * |
| Avg. daily mean/SD | +0.0183 | 0.0870 | ±0.1741 | +0.210 | 0.8333 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0907**, F-statistic = **12.51** (p = **1.07e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4770** | 1.2256 | ±2.4511 | **+6.101** | **1.05e-09** | *** |
| Education: graduate level (vs college) | -0.4362 | 0.2747 | ±0.5494 | -1.588 | 0.1123 |  |
| **Education: high school or below (vs college)** | **+1.3329** | 0.5864 | ±1.1728 | **+2.273** | **0.0230** | * |
| Site: UCSD (vs UAB) | -0.2329 | 0.3594 | ±0.7188 | -0.648 | 0.5170 |  |
| Site: UW (vs UAB) | +0.0020 | 0.3355 | ±0.6709 | +0.006 | 0.9953 |  |
| **Age (years)** | **-0.0882** | 0.0122 | ±0.0244 | **-7.239** | **4.54e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0479 | **+4.094** | **4.25e-05** | *** |
| Hypertension | +0.5026 | 0.2983 | ±0.5965 | +1.685 | 0.0919 | . |
| **High cholesterol** | **+0.7217** | 0.2688 | ±0.5375 | **+2.686** | **0.0072** | ** |
| Kidney disease | +0.8376 | 0.5978 | ±1.1955 | +1.401 | 0.1611 |  |
| **Circulatory disease** | **+0.9614** | 0.4407 | ±0.8814 | **+2.182** | **0.0291** | * |
| MAG (mg/dL/h) | -0.0014 | 0.0170 | ±0.0339 | -0.080 | 0.9359 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0908**, F-statistic = **12.51** (p = **1.04e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.5354** | 1.1866 | ±2.3731 | **+6.351** | **2.15e-10** | *** |
| Education: graduate level (vs college) | -0.4344 | 0.2747 | ±0.5494 | -1.581 | 0.1138 |  |
| **Education: high school or below (vs college)** | **+1.3335** | 0.5858 | ±1.1717 | **+2.276** | **0.0228** | * |
| Site: UCSD (vs UAB) | -0.2352 | 0.3584 | ±0.7168 | -0.656 | 0.5117 |  |
| Site: UW (vs UAB) | +0.0051 | 0.3358 | ±0.6716 | +0.015 | 0.9879 |  |
| **Age (years)** | **-0.0880** | 0.0123 | ±0.0245 | **-7.177** | **7.14e-13** | *** |
| **BMI (kg/m2)** | **+0.0978** | 0.0240 | ±0.0481 | **+4.070** | **4.70e-05** | *** |
| Hypertension | +0.5068 | 0.2996 | ±0.5991 | +1.692 | 0.0907 | . |
| **High cholesterol** | **+0.7215** | 0.2677 | ±0.5355 | **+2.695** | **0.0070** | ** |
| Kidney disease | +0.8445 | 0.5978 | ±1.1955 | +1.413 | 0.1577 |  |
| **Circulatory disease** | **+0.9652** | 0.4407 | ±0.8814 | **+2.190** | **0.0285** | * |
| Avg. daily range (mg/dL) | -0.0012 | 0.0052 | ±0.0103 | -0.237 | 0.8128 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1270**, R² = **0.0990**, Adj R² = **0.0911**, F-statistic = **12.56** (p = **8.33e-23**), Residual SE = **4.596** on **1258** df, AIC = **7489.9**, BIC = **7551.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.2639** | 1.0951 | ±2.1901 | **+6.633** | **3.28e-11** | *** |
| Education: graduate level (vs college) | -0.4367 | 0.2745 | ±0.5490 | -1.591 | 0.1117 |  |
| **Education: high school or below (vs college)** | **+1.3329** | 0.5849 | ±1.1699 | **+2.279** | **0.0227** | * |
| Site: UCSD (vs UAB) | -0.2191 | 0.3600 | ±0.7199 | -0.609 | 0.5428 |  |
| Site: UW (vs UAB) | +0.0006 | 0.3352 | ±0.6704 | +0.002 | 0.9987 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.227** | **4.92e-13** | *** |
| **BMI (kg/m2)** | **+0.0970** | 0.0238 | ±0.0477 | **+4.071** | **4.69e-05** | *** |
| Hypertension | +0.4996 | 0.2984 | ±0.5968 | +1.674 | 0.0941 | . |
| **High cholesterol** | **+0.7188** | 0.2679 | ±0.5357 | **+2.683** | **0.0073** | ** |
| Kidney disease | +0.8337 | 0.5990 | ±1.1979 | +1.392 | 0.1639 |  |
| **Circulatory disease** | **+0.9496** | 0.4405 | ±0.8810 | **+2.156** | **0.0311** | * |
| SD of daily means (mg/dL) | +0.0290 | 0.0356 | ±0.0712 | +0.816 | 0.4145 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1270**, R² = **0.0988**, Adj R² = **0.0910**, F-statistic = **12.54** (p = **9.16e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.1**, BIC = **7551.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2654** | 2.2524 | ±4.5047 | **+3.670** | **2.43e-04** | *** |
| Education: graduate level (vs college) | -0.4397 | 0.2751 | ±0.5503 | -1.598 | 0.1100 |  |
| **Education: high school or below (vs college)** | **+1.3254** | 0.5861 | ±1.1721 | **+2.261** | **0.0237** | * |
| Site: UCSD (vs UAB) | -0.2201 | 0.3597 | ±0.7193 | -0.612 | 0.5405 |  |
| Site: UW (vs UAB) | +0.0041 | 0.3353 | ±0.6707 | +0.012 | 0.9903 |  |
| **Age (years)** | **-0.0882** | 0.0122 | ±0.0244 | **-7.218** | **5.26e-13** | *** |
| **BMI (kg/m2)** | **+0.0976** | 0.0239 | ±0.0478 | **+4.086** | **4.39e-05** | *** |
| Hypertension | +0.4950 | 0.2997 | ±0.5995 | +1.652 | 0.0986 | . |
| **High cholesterol** | **+0.7191** | 0.2682 | ±0.5363 | **+2.682** | **0.0073** | ** |
| Kidney disease | +0.8216 | 0.5992 | ±1.1984 | +1.371 | 0.1703 |  |
| **Circulatory disease** | **+0.9484** | 0.4425 | ±0.8850 | **+2.143** | **0.0321** | * |
| Time in range 70-180, pooled (%) | -0.0086 | 0.0208 | ±0.0416 | -0.415 | 0.6784 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1270**, R² = **0.0989**, Adj R² = **0.0910**, F-statistic = **12.55** (p = **8.91e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.0**, BIC = **7551.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.3352** | 2.2542 | ±4.5083 | **+3.698** | **2.18e-04** | *** |
| Education: graduate level (vs college) | -0.4401 | 0.2752 | ±0.5503 | -1.600 | 0.1097 |  |
| **Education: high school or below (vs college)** | **+1.3258** | 0.5857 | ±1.1715 | **+2.264** | **0.0236** | * |
| Site: UCSD (vs UAB) | -0.2198 | 0.3596 | ±0.7193 | -0.611 | 0.5412 |  |
| Site: UW (vs UAB) | +0.0043 | 0.3353 | ±0.6706 | +0.013 | 0.9898 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.220** | **5.21e-13** | *** |
| **BMI (kg/m2)** | **+0.0975** | 0.0239 | ±0.0478 | **+4.085** | **4.41e-05** | *** |
| Hypertension | +0.4947 | 0.2996 | ±0.5993 | +1.651 | 0.0988 | . |
| **High cholesterol** | **+0.7183** | 0.2682 | ±0.5365 | **+2.678** | **0.0074** | ** |
| Kidney disease | +0.8202 | 0.5993 | ±1.1986 | +1.369 | 0.1711 |  |
| **Circulatory disease** | **+0.9474** | 0.4425 | ±0.8851 | **+2.141** | **0.0323** | * |
| Avg. daily time in range 70-180 (%) | -0.0093 | 0.0207 | ±0.0413 | -0.449 | 0.6531 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0908**, F-statistic = **12.52** (p = **1.04e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3852** | 1.0926 | ±2.1853 | **+6.759** | **1.39e-11** | *** |
| Education: graduate level (vs college) | -0.4325 | 0.2752 | ±0.5504 | -1.571 | 0.1161 |  |
| **Education: high school or below (vs college)** | **+1.3403** | 0.5864 | ±1.1728 | **+2.286** | **0.0223** | * |
| Site: UCSD (vs UAB) | -0.2199 | 0.3611 | ±0.7222 | -0.609 | 0.5425 |  |
| Site: UW (vs UAB) | +0.0088 | 0.3362 | ±0.6724 | +0.026 | 0.9791 |  |
| **Age (years)** | **-0.0880** | 0.0122 | ±0.0245 | **-7.188** | **6.57e-13** | *** |
| **BMI (kg/m2)** | **+0.0978** | 0.0238 | ±0.0477 | **+4.103** | **4.09e-05** | *** |
| Hypertension | +0.5026 | 0.2984 | ±0.5969 | +1.684 | 0.0922 | . |
| **High cholesterol** | **+0.7268** | 0.2678 | ±0.5356 | **+2.714** | **0.0066** | ** |
| Kidney disease | +0.8370 | 0.5984 | ±1.1967 | +1.399 | 0.1619 |  |
| **Circulatory disease** | **+0.9539** | 0.4414 | ±0.8828 | **+2.161** | **0.0307** | * |
| Any reading < 54 during wear (0/1) | +0.0749 | 0.2896 | ±0.5791 | +0.259 | 0.7959 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1270**, R² = **0.0987**, Adj R² = **0.0908**, F-statistic = **12.52** (p = **9.97e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.3**, BIC = **7552.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4578** | 1.0835 | ±2.1670 | **+6.883** | **5.86e-12** | *** |
| Education: graduate level (vs college) | -0.4380 | 0.2748 | ±0.5496 | -1.594 | 0.1110 |  |
| **Education: high school or below (vs college)** | **+1.3236** | 0.5874 | ±1.1748 | **+2.253** | **0.0242** | * |
| Site: UCSD (vs UAB) | -0.2476 | 0.3603 | ±0.7206 | -0.687 | 0.4919 |  |
| Site: UW (vs UAB) | -0.0083 | 0.3364 | ±0.6729 | -0.025 | 0.9803 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.229** | **4.87e-13** | *** |
| **BMI (kg/m2)** | **+0.0979** | 0.0240 | ±0.0479 | **+4.086** | **4.38e-05** | *** |
| Hypertension | +0.4995 | 0.2982 | ±0.5965 | +1.675 | 0.0939 | . |
| **High cholesterol** | **+0.7155** | 0.2686 | ±0.5372 | **+2.664** | **0.0077** | ** |
| Kidney disease | +0.8389 | 0.5978 | ±1.1955 | +1.403 | 0.1605 |  |
| **Circulatory disease** | **+0.9607** | 0.4401 | ±0.8803 | **+2.183** | **0.0291** | * |
| Time < 54 (%) | -0.0907 | 0.2173 | ±0.4346 | -0.417 | 0.6764 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0907**, F-statistic = **12.51** (p = **1.07e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4251** | 1.0801 | ±2.1601 | **+6.875** | **6.21e-12** | *** |
| Education: graduate level (vs college) | -0.4362 | 0.2750 | ±0.5500 | -1.586 | 0.1127 |  |
| **Education: high school or below (vs college)** | **+1.3312** | 0.5882 | ±1.1764 | **+2.263** | **0.0236** | * |
| Site: UCSD (vs UAB) | -0.2328 | 0.3593 | ±0.7186 | -0.648 | 0.5170 |  |
| Site: UW (vs UAB) | +0.0022 | 0.3360 | ±0.6719 | +0.007 | 0.9947 |  |
| **Age (years)** | **-0.0882** | 0.0122 | ±0.0244 | **-7.221** | **5.17e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0479 | **+4.092** | **4.27e-05** | *** |
| Hypertension | +0.5022 | 0.2986 | ±0.5973 | +1.682 | 0.0926 | . |
| **High cholesterol** | **+0.7221** | 0.2681 | ±0.5362 | **+2.693** | **0.0071** | ** |
| Kidney disease | +0.8367 | 0.5980 | ±1.1960 | +1.399 | 0.1617 |  |
| **Circulatory disease** | **+0.9608** | 0.4401 | ±0.8803 | **+2.183** | **0.0290** | * |
| Avg. daily time < 54 (%) | -0.0146 | 0.2485 | ±0.4971 | -0.059 | 0.9533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0908**, F-statistic = **12.51** (p = **1.04e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3960** | 1.0804 | ±2.1609 | **+6.845** | **7.63e-12** | *** |
| Education: graduate level (vs college) | -0.4322 | 0.2751 | ±0.5503 | -1.571 | 0.1162 |  |
| **Education: high school or below (vs college)** | **+1.3408** | 0.5884 | ±1.1767 | **+2.279** | **0.0227** | * |
| Site: UCSD (vs UAB) | -0.2238 | 0.3585 | ±0.7170 | -0.624 | 0.5325 |  |
| Site: UW (vs UAB) | +0.0116 | 0.3350 | ±0.6700 | +0.035 | 0.9723 |  |
| **Age (years)** | **-0.0881** | 0.0122 | ±0.0244 | **-7.208** | **5.70e-13** | *** |
| **BMI (kg/m2)** | **+0.0978** | 0.0239 | ±0.0478 | **+4.092** | **4.28e-05** | *** |
| Hypertension | +0.5056 | 0.2981 | ±0.5962 | +1.696 | 0.0899 | . |
| **High cholesterol** | **+0.7267** | 0.2683 | ±0.5365 | **+2.709** | **0.0068** | ** |
| Kidney disease | +0.8368 | 0.5982 | ±1.1963 | +1.399 | 0.1618 |  |
| **Circulatory disease** | **+0.9608** | 0.4403 | ±0.8807 | **+2.182** | **0.0291** | * |
| Time 54-69, pooled (%) | +0.0235 | 0.0999 | ±0.1999 | +0.236 | 0.8138 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1270**, R² = **0.0987**, Adj R² = **0.0909**, F-statistic = **12.53** (p = **9.74e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.2**, BIC = **7552.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3824** | 1.0780 | ±2.1559 | **+6.848** | **7.46e-12** | *** |
| Education: graduate level (vs college) | -0.4288 | 0.2752 | ±0.5505 | -1.558 | 0.1193 |  |
| **Education: high school or below (vs college)** | **+1.3489** | 0.5887 | ±1.1774 | **+2.291** | **0.0219** | * |
| Site: UCSD (vs UAB) | -0.2206 | 0.3585 | ±0.7169 | -0.615 | 0.5383 |  |
| Site: UW (vs UAB) | +0.0178 | 0.3350 | ±0.6700 | +0.053 | 0.9575 |  |
| **Age (years)** | **-0.0881** | 0.0122 | ±0.0244 | **-7.211** | **5.56e-13** | *** |
| **BMI (kg/m2)** | **+0.0977** | 0.0239 | ±0.0478 | **+4.089** | **4.34e-05** | *** |
| Hypertension | +0.5085 | 0.2982 | ±0.5964 | +1.705 | 0.0881 | . |
| **High cholesterol** | **+0.7290** | 0.2680 | ±0.5360 | **+2.720** | **0.0065** | ** |
| Kidney disease | +0.8374 | 0.5979 | ±1.1957 | +1.401 | 0.1613 |  |
| **Circulatory disease** | **+0.9609** | 0.4403 | ±0.8805 | **+2.183** | **0.0291** | * |
| Avg. daily time 54-69 (%) | +0.0426 | 0.1003 | ±0.2006 | +0.424 | 0.6712 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1270**, R² = **0.0986**, Adj R² = **0.0907**, F-statistic = **12.51** (p = **1.07e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.4**, BIC = **7552.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4139** | 1.0838 | ±2.1677 | **+6.841** | **7.89e-12** | *** |
| Education: graduate level (vs college) | -0.4349 | 0.2752 | ±0.5504 | -1.580 | 0.1141 |  |
| **Education: high school or below (vs college)** | **+1.3346** | 0.5889 | ±1.1778 | **+2.266** | **0.0234** | * |
| Site: UCSD (vs UAB) | -0.2284 | 0.3591 | ±0.7182 | -0.636 | 0.5247 |  |
| Site: UW (vs UAB) | +0.0064 | 0.3357 | ±0.6713 | +0.019 | 0.9849 |  |
| **Age (years)** | **-0.0882** | 0.0122 | ±0.0244 | **-7.216** | **5.35e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0478 | **+4.097** | **4.18e-05** | *** |
| Hypertension | +0.5036 | 0.2982 | ±0.5963 | +1.689 | 0.0912 | . |
| **High cholesterol** | **+0.7242** | 0.2686 | ±0.5371 | **+2.697** | **0.0070** | ** |
| Kidney disease | +0.8363 | 0.5984 | ±1.1967 | +1.398 | 0.1622 |  |
| **Circulatory disease** | **+0.9609** | 0.4403 | ±0.8806 | **+2.182** | **0.0291** | * |
| Time < 70 (%) | +0.0054 | 0.0780 | ±0.1560 | +0.069 | 0.9452 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1270**, R² = **0.0987**, Adj R² = **0.0908**, F-statistic = **12.52** (p = **1.01e-22**), Residual SE = **4.597** on **1258** df, AIC = **7490.3**, BIC = **7552.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3889** | 1.0797 | ±2.1593 | **+6.844** | **7.71e-12** | *** |
| Education: graduate level (vs college) | -0.4303 | 0.2753 | ±0.5506 | -1.563 | 0.1181 |  |
| **Education: high school or below (vs college)** | **+1.3456** | 0.5893 | ±1.1786 | **+2.283** | **0.0224** | * |
| Site: UCSD (vs UAB) | -0.2205 | 0.3587 | ±0.7173 | -0.615 | 0.5387 |  |
| Site: UW (vs UAB) | +0.0167 | 0.3354 | ±0.6707 | +0.050 | 0.9604 |  |
| **Age (years)** | **-0.0881** | 0.0122 | ±0.0244 | **-7.216** | **5.34e-13** | *** |
| **BMI (kg/m2)** | **+0.0978** | 0.0239 | ±0.0478 | **+4.093** | **4.25e-05** | *** |
| Hypertension | +0.5079 | 0.2983 | ±0.5967 | +1.702 | 0.0887 | . |
| **High cholesterol** | **+0.7286** | 0.2681 | ±0.5362 | **+2.718** | **0.0066** | ** |
| Kidney disease | +0.8365 | 0.5980 | ±1.1961 | +1.399 | 0.1619 |  |
| **Circulatory disease** | **+0.9611** | 0.4403 | ±0.8805 | **+2.183** | **0.0290** | * |
| Avg. daily time < 70 (%) | +0.0289 | 0.0812 | ±0.1624 | +0.355 | 0.7223 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1270**, R² = **0.0993**, Adj R² = **0.0915**, F-statistic = **12.61** (p = **6.61e-23**), Residual SE = **4.595** on **1258** df, AIC = **7489.4**, BIC = **7551.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.7369 | 3.1673 | ±6.3345 | +1.496 | 0.1348 |  |
| Education: graduate level (vs college) | -0.4340 | 0.2744 | ±0.5488 | -1.582 | 0.1137 |  |
| **Education: high school or below (vs college)** | **+1.3641** | 0.5906 | ±1.1812 | **+2.310** | **0.0209** | * |
| Site: UCSD (vs UAB) | -0.2422 | 0.3590 | ±0.7179 | -0.675 | 0.4999 |  |
| Site: UW (vs UAB) | -0.0034 | 0.3354 | ±0.6708 | -0.010 | 0.9919 |  |
| **Age (years)** | **-0.0884** | 0.0122 | ±0.0244 | **-7.240** | **4.47e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0478 | **+4.103** | **4.09e-05** | *** |
| Hypertension | +0.5049 | 0.2981 | ±0.5963 | +1.694 | 0.0903 | . |
| **High cholesterol** | **+0.7184** | 0.2678 | ±0.5355 | **+2.683** | **0.0073** | ** |
| Kidney disease | +0.8413 | 0.5976 | ±1.1953 | +1.408 | 0.1592 |  |
| **Circulatory disease** | **+0.9890** | 0.4412 | ±0.8825 | **+2.241** | **0.0250** | * |
| Time 54-250, pooled (%) | +0.0271 | 0.0305 | ±0.0609 | +0.891 | 0.3730 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1270**, R² = **0.0993**, Adj R² = **0.0914**, F-statistic = **12.61** (p = **6.84e-23**), Residual SE = **4.595** on **1258** df, AIC = **7489.5**, BIC = **7551.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.7703 | 3.3166 | ±6.6333 | +1.438 | 0.1504 |  |
| Education: graduate level (vs college) | -0.4340 | 0.2744 | ±0.5488 | -1.582 | 0.1137 |  |
| **Education: high school or below (vs college)** | **+1.3639** | 0.5907 | ±1.1814 | **+2.309** | **0.0209** | * |
| Site: UCSD (vs UAB) | -0.2404 | 0.3590 | ±0.7180 | -0.670 | 0.5032 |  |
| Site: UW (vs UAB) | -0.0024 | 0.3354 | ±0.6708 | -0.007 | 0.9943 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.238** | **4.56e-13** | *** |
| **BMI (kg/m2)** | **+0.0981** | 0.0239 | ±0.0478 | **+4.106** | **4.03e-05** | *** |
| Hypertension | +0.5048 | 0.2982 | ±0.5963 | +1.693 | 0.0905 | . |
| **High cholesterol** | **+0.7191** | 0.2678 | ±0.5355 | **+2.686** | **0.0072** | ** |
| Kidney disease | +0.8404 | 0.5977 | ±1.1955 | +1.406 | 0.1598 |  |
| **Circulatory disease** | **+0.9884** | 0.4413 | ±0.8825 | **+2.240** | **0.0251** | * |
| Avg. daily time 54-250 (%) | +0.0267 | 0.0319 | ±0.0638 | +0.838 | 0.4021 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1270**, R² = **0.1005**, Adj R² = **0.0926**, F-statistic = **12.77** (p = **3.12e-23**), Residual SE = **4.592** on **1258** df, AIC = **7487.8**, BIC = **7549.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4234** | 1.0762 | ±2.1524 | **+6.898** | **5.28e-12** | *** |
| Education: graduate level (vs college) | -0.4550 | 0.2755 | ±0.5509 | -1.652 | 0.0986 | . |
| **Education: high school or below (vs college)** | **+1.3328** | 0.5838 | ±1.1676 | **+2.283** | **0.0224** | * |
| Site: UCSD (vs UAB) | -0.2117 | 0.3587 | ±0.7175 | -0.590 | 0.5551 |  |
| Site: UW (vs UAB) | -0.0163 | 0.3364 | ±0.6728 | -0.049 | 0.9613 |  |
| **Age (years)** | **-0.0888** | 0.0122 | ±0.0245 | **-7.260** | **3.88e-13** | *** |
| **BMI (kg/m2)** | **+0.0967** | 0.0239 | ±0.0478 | **+4.043** | **5.28e-05** | *** |
| Hypertension | +0.4697 | 0.3010 | ±0.6020 | +1.560 | 0.1186 |  |
| **High cholesterol** | **+0.6960** | 0.2682 | ±0.5363 | **+2.596** | **0.0094** | ** |
| Kidney disease | +0.7815 | 0.5995 | ±1.1989 | +1.304 | 0.1923 |  |
| **Circulatory disease** | **+0.9466** | 0.4404 | ±0.8808 | **+2.149** | **0.0316** | * |
| Time 181-250, pooled (%) | +0.0352 | 0.0303 | ±0.0607 | +1.161 | 0.2457 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1270**, R² = **0.1004**, Adj R² = **0.0925**, F-statistic = **12.76** (p = **3.31e-23**), Residual SE = **4.592** on **1258** df, AIC = **7487.9**, BIC = **7549.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4248** | 1.0755 | ±2.1510 | **+6.904** | **5.07e-12** | *** |
| Education: graduate level (vs college) | -0.4551 | 0.2755 | ±0.5510 | -1.652 | 0.0986 | . |
| **Education: high school or below (vs college)** | **+1.3360** | 0.5838 | ±1.1676 | **+2.288** | **0.0221** | * |
| Site: UCSD (vs UAB) | -0.2098 | 0.3588 | ±0.7175 | -0.585 | 0.5587 |  |
| Site: UW (vs UAB) | -0.0137 | 0.3362 | ±0.6725 | -0.041 | 0.9676 |  |
| **Age (years)** | **-0.0887** | 0.0122 | ±0.0245 | **-7.255** | **4.01e-13** | *** |
| **BMI (kg/m2)** | **+0.0966** | 0.0239 | ±0.0478 | **+4.045** | **5.22e-05** | *** |
| Hypertension | +0.4710 | 0.3008 | ±0.6015 | +1.566 | 0.1173 |  |
| **High cholesterol** | **+0.6964** | 0.2683 | ±0.5366 | **+2.596** | **0.0094** | ** |
| Kidney disease | +0.7816 | 0.6000 | ±1.2000 | +1.303 | 0.1927 |  |
| **Circulatory disease** | **+0.9465** | 0.4406 | ±0.8811 | **+2.148** | **0.0317** | * |
| Avg. daily time 181-250 (%) | +0.0339 | 0.0301 | ±0.0602 | +1.127 | 0.2598 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1270**, R² = **0.0988**, Adj R² = **0.0909**, F-statistic = **12.54** (p = **9.23e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.1**, BIC = **7551.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4169** | 1.0759 | ±2.1519 | **+6.893** | **5.45e-12** | *** |
| Education: graduate level (vs college) | -0.4411 | 0.2754 | ±0.5508 | -1.602 | 0.1092 |  |
| **Education: high school or below (vs college)** | **+1.3217** | 0.5874 | ±1.1748 | **+2.250** | **0.0244** | * |
| Site: UCSD (vs UAB) | -0.2246 | 0.3594 | ±0.7188 | -0.625 | 0.5321 |  |
| Site: UW (vs UAB) | +0.0002 | 0.3355 | ±0.6710 | +0.001 | 0.9996 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0245 | **-7.220** | **5.21e-13** | *** |
| **BMI (kg/m2)** | **+0.0977** | 0.0239 | ±0.0478 | **+4.085** | **4.41e-05** | *** |
| Hypertension | +0.4939 | 0.2999 | ±0.5999 | +1.647 | 0.0996 | . |
| **High cholesterol** | **+0.7172** | 0.2684 | ±0.5368 | **+2.672** | **0.0075** | ** |
| Kidney disease | +0.8220 | 0.5991 | ±1.1983 | +1.372 | 0.1701 |  |
| **Circulatory disease** | **+0.9488** | 0.4424 | ±0.8849 | **+2.144** | **0.0320** | * |
| Time > 180 (%) | +0.0084 | 0.0210 | ±0.0420 | +0.400 | 0.6891 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1270**, R² = **0.0988**, Adj R² = **0.0909**, F-statistic = **12.54** (p = **9.26e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.1**, BIC = **7551.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4181** | 1.0756 | ±2.1512 | **+6.897** | **5.32e-12** | *** |
| Education: graduate level (vs college) | -0.4413 | 0.2754 | ±0.5508 | -1.602 | 0.1091 |  |
| **Education: high school or below (vs college)** | **+1.3227** | 0.5870 | ±1.1741 | **+2.253** | **0.0242** | * |
| Site: UCSD (vs UAB) | -0.2240 | 0.3594 | ±0.7188 | -0.623 | 0.5331 |  |
| Site: UW (vs UAB) | +0.0006 | 0.3355 | ±0.6710 | +0.002 | 0.9986 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0245 | **-7.220** | **5.21e-13** | *** |
| **BMI (kg/m2)** | **+0.0976** | 0.0239 | ±0.0478 | **+4.085** | **4.40e-05** | *** |
| Hypertension | +0.4941 | 0.2999 | ±0.5997 | +1.648 | 0.0994 | . |
| **High cholesterol** | **+0.7172** | 0.2684 | ±0.5368 | **+2.672** | **0.0075** | ** |
| Kidney disease | +0.8220 | 0.5993 | ±1.1986 | +1.372 | 0.1702 |  |
| **Circulatory disease** | **+0.9488** | 0.4425 | ±0.8849 | **+2.144** | **0.0320** | * |
| Avg. daily time > 180 (%) | +0.0083 | 0.0209 | ±0.0417 | +0.396 | 0.6918 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1270**, R² = **0.1001**, Adj R² = **0.0922**, F-statistic = **12.72** (p = **4.07e-23**), Residual SE = **4.593** on **1258** df, AIC = **7488.4**, BIC = **7550.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4463** | 1.0751 | ±2.1502 | **+6.926** | **4.32e-12** | *** |
| Education: graduate level (vs college) | -0.4381 | 0.2751 | ±0.5501 | -1.593 | 0.1112 |  |
| **Education: high school or below (vs college)** | **+1.3017** | 0.5882 | ±1.1764 | **+2.213** | **0.0269** | * |
| Site: UCSD (vs UAB) | -0.2206 | 0.3600 | ±0.7199 | -0.613 | 0.5400 |  |
| Site: UW (vs UAB) | -0.0040 | 0.3352 | ±0.6704 | -0.012 | 0.9905 |  |
| **Age (years)** | **-0.0880** | 0.0122 | ±0.0244 | **-7.203** | **5.90e-13** | *** |
| **BMI (kg/m2)** | **+0.0957** | 0.0239 | ±0.0478 | **+4.002** | **6.28e-05** | *** |
| Hypertension | +0.4914 | 0.2998 | ±0.5996 | +1.639 | 0.1012 |  |
| **High cholesterol** | **+0.7028** | 0.2687 | ±0.5374 | **+2.615** | **0.0089** | ** |
| Kidney disease | +0.8379 | 0.5998 | ±1.1996 | +1.397 | 0.1624 |  |
| **Circulatory disease** | **+0.9491** | 0.4434 | ±0.8868 | **+2.141** | **0.0323** | * |
| Nocturnal time > 180 (%) | +0.0222 | 0.0254 | ±0.0509 | +0.873 | 0.3829 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1270**, R² = **0.0988**, Adj R² = **0.0909**, F-statistic = **12.53** (p = **9.52e-23**), Residual SE = **4.596** on **1258** df, AIC = **7490.2**, BIC = **7551.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3809** | 1.0799 | ±2.1598 | **+6.835** | **8.22e-12** | *** |
| Education: graduate level (vs college) | -0.4349 | 0.2748 | ±0.5496 | -1.583 | 0.1135 |  |
| **Education: high school or below (vs college)** | **+1.3339** | 0.5847 | ±1.1693 | **+2.281** | **0.0225** | * |
| Site: UCSD (vs UAB) | -0.2267 | 0.3585 | ±0.7169 | -0.632 | 0.5271 |  |
| Site: UW (vs UAB) | +0.0023 | 0.3355 | ±0.6710 | +0.007 | 0.9946 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.227** | **4.95e-13** | *** |
| **BMI (kg/m2)** | **+0.0987** | 0.0241 | ±0.0482 | **+4.096** | **4.20e-05** | *** |
| Hypertension | +0.4930 | 0.2987 | ±0.5974 | +1.650 | 0.0988 | . |
| **High cholesterol** | **+0.7198** | 0.2680 | ±0.5360 | **+2.686** | **0.0072** | ** |
| Kidney disease | +0.8333 | 0.5971 | ±1.1942 | +1.396 | 0.1628 |  |
| **Circulatory disease** | **+0.9607** | 0.4405 | ±0.8810 | **+2.181** | **0.0292** | * |
| Any reading > 250 during wear (0/1) | +0.1666 | 0.3351 | ±0.6702 | +0.497 | 0.6191 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1270**, R² = **0.0993**, Adj R² = **0.0914**, F-statistic = **12.60** (p = **6.87e-23**), Residual SE = **4.595** on **1258** df, AIC = **7489.5**, BIC = **7551.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4389** | 1.0740 | ±2.1479 | **+6.927** | **4.31e-12** | *** |
| Education: graduate level (vs college) | -0.4335 | 0.2744 | ±0.5488 | -1.580 | 0.1142 |  |
| **Education: high school or below (vs college)** | **+1.3654** | 0.5911 | ±1.1823 | **+2.310** | **0.0209** | * |
| Site: UCSD (vs UAB) | -0.2370 | 0.3589 | ±0.7177 | -0.660 | 0.5090 |  |
| Site: UW (vs UAB) | +0.0004 | 0.3353 | ±0.6705 | +0.001 | 0.9991 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.238** | **4.54e-13** | *** |
| **BMI (kg/m2)** | **+0.0980** | 0.0239 | ±0.0478 | **+4.104** | **4.07e-05** | *** |
| Hypertension | +0.5058 | 0.2982 | ±0.5964 | +1.696 | 0.0898 | . |
| **High cholesterol** | **+0.7207** | 0.2678 | ±0.5356 | **+2.691** | **0.0071** | ** |
| Kidney disease | +0.8404 | 0.5978 | ±1.1957 | +1.406 | 0.1598 |  |
| **Circulatory disease** | **+0.9880** | 0.4412 | ±0.8823 | **+2.240** | **0.0251** | * |
| Time > 250 (%) | -0.0262 | 0.0309 | ±0.0618 | -0.848 | 0.3965 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1270**, R² = **0.0993**, Adj R² = **0.0914**, F-statistic = **12.61** (p = **6.84e-23**), Residual SE = **4.595** on **1258** df, AIC = **7489.5**, BIC = **7551.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4366** | 1.0738 | ±2.1475 | **+6.926** | **4.34e-12** | *** |
| Education: graduate level (vs college) | -0.4333 | 0.2744 | ±0.5489 | -1.579 | 0.1143 |  |
| **Education: high school or below (vs college)** | **+1.3659** | 0.5912 | ±1.1824 | **+2.310** | **0.0209** | * |
| Site: UCSD (vs UAB) | -0.2372 | 0.3589 | ±0.7178 | -0.661 | 0.5087 |  |
| Site: UW (vs UAB) | +0.0007 | 0.3352 | ±0.6705 | +0.002 | 0.9984 |  |
| **Age (years)** | **-0.0883** | 0.0122 | ±0.0244 | **-7.238** | **4.55e-13** | *** |
| **BMI (kg/m2)** | **+0.0981** | 0.0239 | ±0.0478 | **+4.107** | **4.02e-05** | *** |
| Hypertension | +0.5059 | 0.2982 | ±0.5964 | +1.697 | 0.0898 | . |
| **High cholesterol** | **+0.7205** | 0.2678 | ±0.5356 | **+2.690** | **0.0071** | ** |
| Kidney disease | +0.8398 | 0.5978 | ±1.1957 | +1.405 | 0.1601 |  |
| **Circulatory disease** | **+0.9886** | 0.4412 | ±0.8824 | **+2.241** | **0.0250** | * |
| Avg. daily time > 250 (%) | -0.0268 | 0.0322 | ±0.0644 | -0.832 | 0.4057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 1,270; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0781**, LLR χ² = **90.48** (p = **4.30e-15**), AUC = **0.6934**, AIC = **1089.8**, BIC = **1146.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6455 | 0.5975 | ±1.1951 | -1.080 | 0.2800 | 0.5244 |  |
| Education: graduate level (vs college) | -0.0601 | 0.1710 | ±0.3419 | -0.351 | 0.7254 | 0.9417 |  |
| Education: high school or below (vs college) | +0.3418 | 0.2620 | ±0.5240 | +1.305 | 0.1920 | 1.4075 |  |
| Site: UCSD (vs UAB) | -0.1869 | 0.2125 | ±0.4251 | -0.879 | 0.3793 | 0.8296 |  |
| Site: UW (vs UAB) | -0.0335 | 0.1881 | ±0.3763 | -0.178 | 0.8585 | 0.9670 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.799** | **6.69e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0461** | 0.0104 | ±0.0208 | **+4.434** | **9.24e-06** | 1.0471 | *** |
| Hypertension | +0.2435 | 0.1729 | ±0.3458 | +1.408 | 0.1591 | 1.2757 |  |
| **High cholesterol** | **+0.4268** | 0.1644 | ±0.3288 | **+2.596** | **0.0094** | 1.5323 | ** |
| Kidney disease | +0.4740 | 0.2801 | ±0.5602 | +1.692 | 0.0906 | 1.6064 | . |
| **Circulatory disease** | **+0.5643** | 0.2216 | ±0.4433 | **+2.546** | **0.0109** | 1.7581 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0789**, LLR χ² = **91.34** (p = **9.08e-15**), AUC = **0.6938**, AIC = **1090.9**, BIC = **1152.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.2567 | 0.8776 | ±1.7552 | -1.432 | 0.1521 | 0.2846 |  |
| Education: graduate level (vs college) | -0.0585 | 0.1710 | ±0.3421 | -0.342 | 0.7324 | 0.9432 |  |
| Education: high school or below (vs college) | +0.3287 | 0.2624 | ±0.5247 | +1.253 | 0.2103 | 1.3892 |  |
| Site: UCSD (vs UAB) | -0.1869 | 0.2126 | ±0.4253 | -0.879 | 0.3794 | 0.8295 |  |
| Site: UW (vs UAB) | -0.0372 | 0.1883 | ±0.3766 | -0.198 | 0.8434 | 0.9635 |  |
| **Age (years)** | **-0.0461** | 0.0079 | ±0.0158 | **-5.847** | **4.99e-09** | 0.9549 | *** |
| **BMI (kg/m2)** | **+0.0452** | 0.0104 | ±0.0208 | **+4.343** | **1.41e-05** | 1.0463 | *** |
| Hypertension | +0.2367 | 0.1731 | ±0.3461 | +1.367 | 0.1715 | 1.2670 |  |
| **High cholesterol** | **+0.4144** | 0.1650 | ±0.3299 | **+2.512** | **0.0120** | 1.5135 | * |
| Kidney disease | +0.4739 | 0.2802 | ±0.5604 | +1.691 | 0.0908 | 1.6062 | . |
| **Circulatory disease** | **+0.5536** | 0.2221 | ±0.4442 | **+2.492** | **0.0127** | 1.7395 | * |
| HbA1c (%) | +0.1199 | 0.1258 | ±0.2515 | +0.953 | 0.3404 | 1.1274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0787**, LLR χ² = **91.20** (p = **9.70e-15**), AUC = **0.6944**, AIC = **1091.1**, BIC = **1152.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.9895 | 0.7198 | ±1.4395 | -1.375 | 0.1692 | 0.3717 |  |
| Education: graduate level (vs college) | -0.0674 | 0.1712 | ±0.3425 | -0.394 | 0.6939 | 0.9348 |  |
| Education: high school or below (vs college) | +0.3285 | 0.2623 | ±0.5247 | +1.252 | 0.2105 | 1.3889 |  |
| Site: UCSD (vs UAB) | -0.1857 | 0.2126 | ±0.4251 | -0.873 | 0.3824 | 0.8306 |  |
| Site: UW (vs UAB) | -0.0424 | 0.1884 | ±0.3769 | -0.225 | 0.8219 | 0.9585 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.822** | **5.83e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0457** | 0.0104 | ±0.0208 | **+4.391** | **1.13e-05** | 1.0467 | *** |
| Hypertension | +0.2344 | 0.1734 | ±0.3467 | +1.352 | 0.1764 | 1.2641 |  |
| **High cholesterol** | **+0.4178** | 0.1647 | ±0.3295 | **+2.536** | **0.0112** | 1.5186 | * |
| Kidney disease | +0.4607 | 0.2809 | ±0.5619 | +1.640 | 0.1010 | 1.5853 |  |
| **Circulatory disease** | **+0.5519** | 0.2223 | ±0.4447 | **+2.482** | **0.0131** | 1.7366 | * |
| Mean glucose (mg/dL) | +0.0032 | 0.0037 | ±0.0074 | +0.860 | 0.3897 | 1.0032 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0787**, LLR χ² = **91.20** (p = **9.70e-15**), AUC = **0.6944**, AIC = **1091.1**, BIC = **1152.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4288 | 1.0901 | ±2.1801 | -1.311 | 0.1899 | 0.2396 |  |
| Education: graduate level (vs college) | -0.0674 | 0.1712 | ±0.3425 | -0.394 | 0.6939 | 0.9348 |  |
| Education: high school or below (vs college) | +0.3285 | 0.2623 | ±0.5247 | +1.252 | 0.2105 | 1.3889 |  |
| Site: UCSD (vs UAB) | -0.1857 | 0.2126 | ±0.4251 | -0.873 | 0.3824 | 0.8306 |  |
| Site: UW (vs UAB) | -0.0424 | 0.1884 | ±0.3769 | -0.225 | 0.8219 | 0.9585 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.822** | **5.83e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0457** | 0.0104 | ±0.0208 | **+4.391** | **1.13e-05** | 1.0467 | *** |
| Hypertension | +0.2344 | 0.1734 | ±0.3467 | +1.352 | 0.1764 | 1.2641 |  |
| **High cholesterol** | **+0.4178** | 0.1647 | ±0.3295 | **+2.536** | **0.0112** | 1.5186 | * |
| Kidney disease | +0.4607 | 0.2809 | ±0.5619 | +1.640 | 0.1010 | 1.5853 |  |
| **Circulatory disease** | **+0.5519** | 0.2223 | ±0.4447 | **+2.482** | **0.0131** | 1.7366 | * |
| GMI (%) | +0.1327 | 0.1543 | ±0.3086 | +0.860 | 0.3897 | 1.1419 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0801**, LLR χ² = **92.72** (p = **4.87e-15**), AUC = **0.6961**, AIC = **1089.5**, BIC = **1151.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.2101 | 0.7037 | ±1.4073 | -1.720 | 0.0855 | 0.2982 | . |
| Education: graduate level (vs college) | -0.0684 | 0.1712 | ±0.3424 | -0.400 | 0.6894 | 0.9339 |  |
| Education: high school or below (vs college) | +0.3158 | 0.2627 | ±0.5255 | +1.202 | 0.2293 | 1.3714 |  |
| Site: UCSD (vs UAB) | -0.1918 | 0.2126 | ±0.4253 | -0.902 | 0.3670 | 0.8254 |  |
| Site: UW (vs UAB) | -0.0488 | 0.1885 | ±0.3770 | -0.259 | 0.7955 | 0.9523 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.787** | **7.18e-09** | 0.9556 | *** |
| **BMI (kg/m2)** | **+0.0444** | 0.0104 | ±0.0209 | **+4.253** | **2.11e-05** | 1.0454 | *** |
| Hypertension | +0.2309 | 0.1733 | ±0.3466 | +1.332 | 0.1827 | 1.2597 |  |
| **High cholesterol** | **+0.4079** | 0.1650 | ±0.3300 | **+2.473** | **0.0134** | 1.5037 | * |
| Kidney disease | +0.4713 | 0.2806 | ±0.5612 | +1.680 | 0.0930 | 1.6020 | . |
| **Circulatory disease** | **+0.5513** | 0.2222 | ±0.4444 | **+2.481** | **0.0131** | 1.7354 | * |
| Nocturnal mean 00-06h (mg/dL) | +0.0053 | 0.0034 | ±0.0069 | +1.528 | 0.1266 | 1.0053 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0783**, LLR χ² = **90.68** (p = **1.23e-14**), AUC = **0.6933**, AIC = **1091.6**, BIC = **1153.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7385 | 0.6329 | ±1.2658 | -1.167 | 0.2433 | 0.4778 |  |
| Education: graduate level (vs college) | -0.0614 | 0.1710 | ±0.3420 | -0.359 | 0.7198 | 0.9405 |  |
| Education: high school or below (vs college) | +0.3414 | 0.2620 | ±0.5240 | +1.303 | 0.1925 | 1.4069 |  |
| Site: UCSD (vs UAB) | -0.1819 | 0.2128 | ±0.4257 | -0.855 | 0.3927 | 0.8337 |  |
| Site: UW (vs UAB) | -0.0347 | 0.1882 | ±0.3764 | -0.184 | 0.8537 | 0.9659 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.813** | **6.14e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0459** | 0.0104 | ±0.0208 | **+4.424** | **9.67e-06** | 1.0470 | *** |
| Hypertension | +0.2372 | 0.1736 | ±0.3472 | +1.367 | 0.1718 | 1.2677 |  |
| **High cholesterol** | **+0.4262** | 0.1644 | ±0.3289 | **+2.592** | **0.0095** | 1.5315 | ** |
| Kidney disease | +0.4611 | 0.2818 | ±0.5636 | +1.636 | 0.1018 | 1.5858 |  |
| **Circulatory disease** | **+0.5587** | 0.2221 | ±0.4442 | **+2.516** | **0.0119** | 1.7485 | * |
| Glucose SD, pooled (mg/dL) | +0.0052 | 0.0116 | ±0.0233 | +0.447 | 0.6551 | 1.0052 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.52** (p = **1.32e-14**), AUC = **0.6935**, AIC = **1091.7**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6836 | 0.6290 | ±1.2580 | -1.087 | 0.2771 | 0.5048 |  |
| Education: graduate level (vs college) | -0.0608 | 0.1710 | ±0.3420 | -0.355 | 0.7224 | 0.9410 |  |
| Education: high school or below (vs college) | +0.3417 | 0.2620 | ±0.5240 | +1.304 | 0.1922 | 1.4073 |  |
| Site: UCSD (vs UAB) | -0.1849 | 0.2128 | ±0.4255 | -0.869 | 0.3847 | 0.8312 |  |
| Site: UW (vs UAB) | -0.0343 | 0.1882 | ±0.3764 | -0.182 | 0.8554 | 0.9663 |  |
| **Age (years)** | **-0.0456** | 0.0079 | ±0.0157 | **-5.799** | **6.69e-09** | 0.9554 | *** |
| **BMI (kg/m2)** | **+0.0460** | 0.0104 | ±0.0208 | **+4.426** | **9.61e-06** | 1.0471 | *** |
| Hypertension | +0.2409 | 0.1735 | ±0.3469 | +1.389 | 0.1649 | 1.2724 |  |
| **High cholesterol** | **+0.4264** | 0.1644 | ±0.3289 | **+2.594** | **0.0095** | 1.5318 | ** |
| Kidney disease | +0.4679 | 0.2820 | ±0.5640 | +1.659 | 0.0971 | 1.5966 | . |
| **Circulatory disease** | **+0.5619** | 0.2220 | ±0.4440 | **+2.531** | **0.0114** | 1.7539 | * |
| Avg. daily SD (mg/dL) | +0.0024 | 0.0125 | ±0.0251 | +0.194 | 0.8460 | 1.0024 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0781**, LLR χ² = **90.49** (p = **1.34e-14**), AUC = **0.6935**, AIC = **1091.8**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6284 | 0.6796 | ±1.3591 | -0.925 | 0.3551 | 0.5335 |  |
| Education: graduate level (vs college) | -0.0602 | 0.1710 | ±0.3420 | -0.352 | 0.7247 | 0.9416 |  |
| Education: high school or below (vs college) | +0.3414 | 0.2621 | ±0.5242 | +1.303 | 0.1927 | 1.4069 |  |
| Site: UCSD (vs UAB) | -0.1877 | 0.2131 | ±0.4263 | -0.881 | 0.3785 | 0.8289 |  |
| Site: UW (vs UAB) | -0.0339 | 0.1882 | ±0.3765 | -0.180 | 0.8572 | 0.9667 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.784** | **7.31e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0461** | 0.0104 | ±0.0208 | **+4.434** | **9.27e-06** | 1.0471 | *** |
| Hypertension | +0.2441 | 0.1732 | ±0.3464 | +1.409 | 0.1588 | 1.2764 |  |
| **High cholesterol** | **+0.4264** | 0.1646 | ±0.3291 | **+2.591** | **0.0096** | 1.5317 | ** |
| Kidney disease | +0.4753 | 0.2811 | ±0.5622 | +1.691 | 0.0909 | 1.6084 | . |
| **Circulatory disease** | **+0.5645** | 0.2217 | ±0.4434 | **+2.546** | **0.0109** | 1.7585 | * |
| CV (%) | -0.0010 | 0.0195 | ±0.0390 | -0.053 | 0.9578 | 0.9990 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.54** (p = **1.31e-14**), AUC = **0.6935**, AIC = **1091.7**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5522 | 0.7197 | ±1.4395 | -0.767 | 0.4430 | 0.5757 |  |
| Education: graduate level (vs college) | -0.0591 | 0.1710 | ±0.3420 | -0.346 | 0.7295 | 0.9426 |  |
| Education: high school or below (vs college) | +0.3421 | 0.2621 | ±0.5241 | +1.305 | 0.1918 | 1.4079 |  |
| Site: UCSD (vs UAB) | -0.1833 | 0.2131 | ±0.4262 | -0.860 | 0.3897 | 0.8325 |  |
| Site: UW (vs UAB) | -0.0327 | 0.1882 | ±0.3764 | -0.174 | 0.8621 | 0.9678 |  |
| **Age (years)** | **-0.0456** | 0.0079 | ±0.0157 | **-5.800** | **6.62e-09** | 0.9554 | *** |
| **BMI (kg/m2)** | **+0.0461** | 0.0104 | ±0.0208 | **+4.438** | **9.09e-06** | 1.0472 | *** |
| Hypertension | +0.2408 | 0.1733 | ±0.3467 | +1.389 | 0.1647 | 1.2723 |  |
| **High cholesterol** | **+0.4280** | 0.1645 | ±0.3290 | **+2.602** | **0.0093** | 1.5343 | ** |
| Kidney disease | +0.4698 | 0.2807 | ±0.5614 | +1.674 | 0.0942 | 1.5997 | . |
| **Circulatory disease** | **+0.5637** | 0.2217 | ±0.4434 | **+2.543** | **0.0110** | 1.7572 | * |
| Mean / SD ratio | -0.0150 | 0.0643 | ±0.1287 | -0.232 | 0.8163 | 0.9852 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.57** (p = **1.29e-14**), AUC = **0.6940**, AIC = **1091.7**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7626 | 0.7202 | ±1.4404 | -1.059 | 0.2897 | 0.4665 |  |
| Education: graduate level (vs college) | -0.0607 | 0.1710 | ±0.3420 | -0.355 | 0.7224 | 0.9411 |  |
| Education: high school or below (vs college) | +0.3423 | 0.2619 | ±0.5239 | +1.307 | 0.1913 | 1.4081 |  |
| Site: UCSD (vs UAB) | -0.1902 | 0.2128 | ±0.4256 | -0.894 | 0.3715 | 0.8268 |  |
| Site: UW (vs UAB) | -0.0341 | 0.1881 | ±0.3763 | -0.181 | 0.8563 | 0.9665 |  |
| **Age (years)** | **-0.0454** | 0.0079 | ±0.0157 | **-5.760** | **8.41e-09** | 0.9557 | *** |
| **BMI (kg/m2)** | **+0.0461** | 0.0104 | ±0.0208 | **+4.437** | **9.10e-06** | 1.0472 | *** |
| Hypertension | +0.2457 | 0.1730 | ±0.3461 | +1.420 | 0.1556 | 1.2785 |  |
| **High cholesterol** | **+0.4253** | 0.1645 | ±0.3289 | **+2.586** | **0.0097** | 1.5300 | ** |
| Kidney disease | +0.4809 | 0.2811 | ±0.5621 | +1.711 | 0.0871 | 1.6175 | . |
| **Circulatory disease** | **+0.5648** | 0.2216 | ±0.4433 | **+2.548** | **0.0108** | 1.7591 | * |
| Avg. daily mean/SD | +0.0155 | 0.0532 | ±0.1065 | +0.292 | 0.7706 | 1.0156 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0781**, LLR χ² = **90.50** (p = **1.33e-14**), AUC = **0.6934**, AIC = **1091.8**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7012 | 0.7146 | ±1.4293 | -0.981 | 0.3265 | 0.4960 |  |
| Education: graduate level (vs college) | -0.0597 | 0.1710 | ±0.3420 | -0.349 | 0.7269 | 0.9420 |  |
| Education: high school or below (vs college) | +0.3413 | 0.2620 | ±0.5241 | +1.302 | 0.1928 | 1.4067 |  |
| Site: UCSD (vs UAB) | -0.1846 | 0.2131 | ±0.4263 | -0.866 | 0.3865 | 0.8315 |  |
| Site: UW (vs UAB) | -0.0313 | 0.1888 | ±0.3777 | -0.166 | 0.8685 | 0.9692 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.794** | **6.87e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0460** | 0.0104 | ±0.0208 | **+4.432** | **9.35e-06** | 1.0471 | *** |
| Hypertension | +0.2434 | 0.1729 | ±0.3459 | +1.407 | 0.1593 | 1.2756 |  |
| **High cholesterol** | **+0.4285** | 0.1648 | ±0.3297 | **+2.599** | **0.0093** | 1.5349 | ** |
| Kidney disease | +0.4727 | 0.2802 | ±0.5605 | +1.687 | 0.0916 | 1.6044 | . |
| **Circulatory disease** | **+0.5636** | 0.2217 | ±0.4434 | **+2.542** | **0.0110** | 1.7570 | * |
| MAG (mg/dL/h) | +0.0014 | 0.0097 | ±0.0195 | +0.142 | 0.8870 | 1.0014 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0781**, LLR χ² = **90.49** (p = **1.34e-14**), AUC = **0.6934**, AIC = **1091.8**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6643 | 0.6550 | ±1.3100 | -1.014 | 0.3105 | 0.5146 |  |
| Education: graduate level (vs college) | -0.0604 | 0.1710 | ±0.3421 | -0.353 | 0.7241 | 0.9414 |  |
| Education: high school or below (vs college) | +0.3415 | 0.2620 | ±0.5241 | +1.303 | 0.1924 | 1.4071 |  |
| Site: UCSD (vs UAB) | -0.1860 | 0.2129 | ±0.4257 | -0.874 | 0.3821 | 0.8302 |  |
| Site: UW (vs UAB) | -0.0335 | 0.1881 | ±0.3763 | -0.178 | 0.8586 | 0.9670 |  |
| **Age (years)** | **-0.0456** | 0.0079 | ±0.0157 | **-5.792** | **6.94e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0461** | 0.0104 | ±0.0208 | **+4.435** | **9.21e-06** | 1.0472 | *** |
| Hypertension | +0.2429 | 0.1732 | ±0.3464 | +1.402 | 0.1608 | 1.2749 |  |
| **High cholesterol** | **+0.4270** | 0.1644 | ±0.3289 | **+2.597** | **0.0094** | 1.5326 | ** |
| Kidney disease | +0.4722 | 0.2813 | ±0.5626 | +1.679 | 0.0932 | 1.6035 | . |
| **Circulatory disease** | **+0.5633** | 0.2221 | ±0.4441 | **+2.537** | **0.0112** | 1.7565 | * |
| Avg. daily range (mg/dL) | +0.0002 | 0.0030 | ±0.0060 | +0.070 | 0.9441 | 1.0002 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0791**, LLR χ² = **91.63** (p = **8.00e-15**), AUC = **0.6928**, AIC = **1090.6**, BIC = **1152.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7738 | 0.6088 | ±1.2176 | -1.271 | 0.2037 | 0.4613 |  |
| Education: graduate level (vs college) | -0.0604 | 0.1711 | ±0.3422 | -0.353 | 0.7240 | 0.9414 |  |
| Education: high school or below (vs college) | +0.3445 | 0.2619 | ±0.5238 | +1.315 | 0.1884 | 1.4113 |  |
| Site: UCSD (vs UAB) | -0.1755 | 0.2129 | ±0.4258 | -0.825 | 0.4096 | 0.8390 |  |
| Site: UW (vs UAB) | -0.0340 | 0.1883 | ±0.3766 | -0.181 | 0.8567 | 0.9666 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.816** | **6.02e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0453** | 0.0104 | ±0.0208 | **+4.350** | **1.36e-05** | 1.0463 | *** |
| Hypertension | +0.2402 | 0.1732 | ±0.3463 | +1.387 | 0.1654 | 1.2715 |  |
| **High cholesterol** | **+0.4215** | 0.1645 | ±0.3291 | **+2.561** | **0.0104** | 1.5242 | * |
| Kidney disease | +0.4723 | 0.2801 | ±0.5601 | +1.686 | 0.0917 | 1.6036 | . |
| **Circulatory disease** | **+0.5601** | 0.2218 | ±0.4435 | **+2.526** | **0.0115** | 1.7509 | * |
| SD of daily means (mg/dL) | +0.0242 | 0.0223 | ±0.0445 | +1.085 | 0.2779 | 1.0245 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0801**, LLR χ² = **92.72** (p = **4.88e-15**), AUC = **0.6956**, AIC = **1089.5**, BIC = **1151.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.4596 | 0.9360 | ±1.8720 | +0.491 | 0.6234 | 1.5834 |  |
| Education: graduate level (vs college) | -0.0666 | 0.1713 | ±0.3426 | -0.389 | 0.6973 | 0.9356 |  |
| Education: high school or below (vs college) | +0.3327 | 0.2622 | ±0.5244 | +1.269 | 0.2044 | 1.3948 |  |
| Site: UCSD (vs UAB) | -0.1732 | 0.2130 | ±0.4259 | -0.813 | 0.4160 | 0.8410 |  |
| Site: UW (vs UAB) | -0.0317 | 0.1885 | ±0.3769 | -0.168 | 0.8665 | 0.9688 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.811** | **6.21e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0456** | 0.0104 | ±0.0208 | **+4.380** | **1.19e-05** | 1.0466 | *** |
| Hypertension | +0.2337 | 0.1734 | ±0.3467 | +1.348 | 0.1775 | 1.2633 |  |
| **High cholesterol** | **+0.4192** | 0.1647 | ±0.3293 | **+2.546** | **0.0109** | 1.5208 | * |
| Kidney disease | +0.4475 | 0.2816 | ±0.5632 | +1.589 | 0.1121 | 1.5644 |  |
| **Circulatory disease** | **+0.5440** | 0.2227 | ±0.4453 | **+2.443** | **0.0146** | 1.7228 | * |
| Time in range 70-180, pooled (%) | -0.0112 | 0.0073 | ±0.0146 | -1.534 | 0.1251 | 0.9888 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0800**, LLR χ² = **92.66** (p = **5.00e-15**), AUC = **0.6955**, AIC = **1089.6**, BIC = **1151.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.4452 | 0.9356 | ±1.8711 | +0.476 | 0.6342 | 1.5608 |  |
| Education: graduate level (vs college) | -0.0666 | 0.1713 | ±0.3425 | -0.389 | 0.6976 | 0.9356 |  |
| Education: high school or below (vs college) | +0.3343 | 0.2621 | ±0.5242 | +1.276 | 0.2021 | 1.3970 |  |
| Site: UCSD (vs UAB) | -0.1738 | 0.2130 | ±0.4259 | -0.816 | 0.4145 | 0.8405 |  |
| Site: UW (vs UAB) | -0.0313 | 0.1884 | ±0.3769 | -0.166 | 0.8683 | 0.9692 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.814** | **6.11e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0455** | 0.0104 | ±0.0208 | **+4.378** | **1.20e-05** | 1.0466 | *** |
| Hypertension | +0.2339 | 0.1734 | ±0.3467 | +1.349 | 0.1773 | 1.2635 |  |
| **High cholesterol** | **+0.4188** | 0.1647 | ±0.3293 | **+2.543** | **0.0110** | 1.5202 | * |
| Kidney disease | +0.4476 | 0.2816 | ±0.5633 | +1.589 | 0.1120 | 1.5645 |  |
| **Circulatory disease** | **+0.5448** | 0.2226 | ±0.4452 | **+2.448** | **0.0144** | 1.7243 | * |
| Avg. daily time in range 70-180 (%) | -0.0110 | 0.0073 | ±0.0146 | -1.515 | 0.1298 | 0.9890 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0789**, LLR χ² = **91.43** (p = **8.75e-15**), AUC = **0.6927**, AIC = **1090.8**, BIC = **1152.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7245 | 0.6030 | ±1.2059 | -1.202 | 0.2295 | 0.4846 |  |
| Education: graduate level (vs college) | -0.0514 | 0.1713 | ±0.3426 | -0.300 | 0.7640 | 0.9499 |  |
| Education: high school or below (vs college) | +0.3604 | 0.2631 | ±0.5262 | +1.370 | 0.1707 | 1.4339 |  |
| Site: UCSD (vs UAB) | -0.1600 | 0.2144 | ±0.4289 | -0.746 | 0.4556 | 0.8522 |  |
| Site: UW (vs UAB) | -0.0205 | 0.1887 | ±0.3775 | -0.108 | 0.9136 | 0.9797 |  |
| **Age (years)** | **-0.0452** | 0.0079 | ±0.0157 | **-5.750** | **8.92e-09** | 0.9558 | *** |
| **BMI (kg/m2)** | **+0.0456** | 0.0104 | ±0.0208 | **+4.389** | **1.14e-05** | 1.0467 | *** |
| Hypertension | +0.2417 | 0.1731 | ±0.3462 | +1.396 | 0.1627 | 1.2734 |  |
| **High cholesterol** | **+0.4355** | 0.1648 | ±0.3295 | **+2.643** | **0.0082** | 1.5457 | ** |
| Kidney disease | +0.4708 | 0.2803 | ±0.5606 | +1.679 | 0.0931 | 1.6013 | . |
| **Circulatory disease** | **+0.5482** | 0.2225 | ±0.4450 | **+2.464** | **0.0138** | 1.7302 | * |
| Any reading < 54 during wear (0/1) | +0.1616 | 0.1655 | ±0.3310 | +0.976 | 0.3289 | 1.1754 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0781**, LLR χ² = **90.49** (p = **1.34e-14**), AUC = **0.6936**, AIC = **1091.8**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6420 | 0.5993 | ±1.1986 | -1.071 | 0.2840 | 0.5262 |  |
| Education: graduate level (vs college) | -0.0600 | 0.1710 | ±0.3419 | -0.351 | 0.7254 | 0.9417 |  |
| Education: high school or below (vs college) | +0.3410 | 0.2622 | ±0.5244 | +1.300 | 0.1935 | 1.4063 |  |
| Site: UCSD (vs UAB) | -0.1890 | 0.2143 | ±0.4287 | -0.882 | 0.3780 | 0.8278 |  |
| Site: UW (vs UAB) | -0.0349 | 0.1890 | ±0.3780 | -0.185 | 0.8534 | 0.9657 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.799** | **6.66e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0461** | 0.0104 | ±0.0208 | **+4.434** | **9.24e-06** | 1.0472 | *** |
| Hypertension | +0.2431 | 0.1730 | ±0.3460 | +1.405 | 0.1599 | 1.2752 |  |
| **High cholesterol** | **+0.4258** | 0.1650 | ±0.3299 | **+2.581** | **0.0099** | 1.5308 | ** |
| Kidney disease | +0.4745 | 0.2802 | ±0.5604 | +1.693 | 0.0904 | 1.6072 | . |
| **Circulatory disease** | **+0.5643** | 0.2216 | ±0.4433 | **+2.546** | **0.0109** | 1.7582 | * |
| Time < 54 (%) | -0.0125 | 0.1663 | ±0.3325 | -0.075 | 0.9402 | 0.9876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0784**, LLR χ² = **90.76** (p = **1.18e-14**), AUC = **0.6944**, AIC = **1091.5**, BIC = **1153.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6316 | 0.5982 | ±1.1964 | -1.056 | 0.2910 | 0.5317 |  |
| Education: graduate level (vs college) | -0.0607 | 0.1710 | ±0.3419 | -0.355 | 0.7228 | 0.9411 |  |
| Education: high school or below (vs college) | +0.3358 | 0.2621 | ±0.5242 | +1.281 | 0.2001 | 1.3991 |  |
| Site: UCSD (vs UAB) | -0.2000 | 0.2139 | ±0.4277 | -0.935 | 0.3497 | 0.8187 |  |
| Site: UW (vs UAB) | -0.0450 | 0.1893 | ±0.3785 | -0.238 | 0.8122 | 0.9560 |  |
| **Age (years)** | **-0.0455** | 0.0078 | ±0.0157 | **-5.794** | **6.88e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0463** | 0.0104 | ±0.0208 | **+4.445** | **8.79e-06** | 1.0474 | *** |
| Hypertension | +0.2389 | 0.1731 | ±0.3463 | +1.380 | 0.1677 | 1.2698 |  |
| **High cholesterol** | **+0.4211** | 0.1647 | ±0.3295 | **+2.557** | **0.0106** | 1.5237 | * |
| Kidney disease | +0.4772 | 0.2803 | ±0.5605 | +1.703 | 0.0886 | 1.6116 | . |
| **Circulatory disease** | **+0.5631** | 0.2217 | ±0.4434 | **+2.540** | **0.0111** | 1.7562 | * |
| Avg. daily time < 54 (%) | -0.1284 | 0.2593 | ±0.5185 | -0.495 | 0.6203 | 0.8795 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0784**, LLR χ² = **90.79** (p = **1.17e-14**), AUC = **0.6937**, AIC = **1091.5**, BIC = **1153.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6739 | 0.5998 | ±1.1996 | -1.124 | 0.2612 | 0.5097 |  |
| Education: graduate level (vs college) | -0.0561 | 0.1712 | ±0.3424 | -0.328 | 0.7432 | 0.9455 |  |
| Education: high school or below (vs college) | +0.3513 | 0.2628 | ±0.5255 | +1.337 | 0.1812 | 1.4209 |  |
| Site: UCSD (vs UAB) | -0.1757 | 0.2136 | ±0.4272 | -0.823 | 0.4107 | 0.8389 |  |
| Site: UW (vs UAB) | -0.0233 | 0.1892 | ±0.3784 | -0.123 | 0.9022 | 0.9770 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.794** | **6.85e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0459** | 0.0104 | ±0.0208 | **+4.419** | **9.90e-06** | 1.0470 | *** |
| Hypertension | +0.2488 | 0.1732 | ±0.3464 | +1.436 | 0.1509 | 1.2825 |  |
| **High cholesterol** | **+0.4334** | 0.1649 | ±0.3298 | **+2.628** | **0.0086** | 1.5424 | ** |
| Kidney disease | +0.4740 | 0.2802 | ±0.5603 | +1.692 | 0.0907 | 1.6063 | . |
| **Circulatory disease** | **+0.5659** | 0.2217 | ±0.4433 | **+2.553** | **0.0107** | 1.7610 | * |
| Time 54-69, pooled (%) | +0.0288 | 0.0511 | ±0.1022 | +0.565 | 0.5724 | 1.0293 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0783**, LLR χ² = **90.69** (p = **1.22e-14**), AUC = **0.6935**, AIC = **1091.6**, BIC = **1153.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6650 | 0.5992 | ±1.1983 | -1.110 | 0.2670 | 0.5143 |  |
| Education: graduate level (vs college) | -0.0565 | 0.1712 | ±0.3425 | -0.330 | 0.7413 | 0.9450 |  |
| Education: high school or below (vs college) | +0.3503 | 0.2628 | ±0.5256 | +1.333 | 0.1825 | 1.4196 |  |
| Site: UCSD (vs UAB) | -0.1795 | 0.2132 | ±0.4264 | -0.842 | 0.3998 | 0.8357 |  |
| Site: UW (vs UAB) | -0.0254 | 0.1891 | ±0.3782 | -0.134 | 0.8933 | 0.9750 |  |
| **Age (years)** | **-0.0456** | 0.0079 | ±0.0157 | **-5.799** | **6.68e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0459** | 0.0104 | ±0.0208 | **+4.422** | **9.77e-06** | 1.0470 | *** |
| Hypertension | +0.2479 | 0.1732 | ±0.3464 | +1.431 | 0.1524 | 1.2813 |  |
| **High cholesterol** | **+0.4317** | 0.1648 | ±0.3296 | **+2.619** | **0.0088** | 1.5398 | ** |
| Kidney disease | +0.4744 | 0.2801 | ±0.5603 | +1.693 | 0.0904 | 1.6070 | . |
| **Circulatory disease** | **+0.5659** | 0.2217 | ±0.4433 | **+2.553** | **0.0107** | 1.7611 | * |
| Avg. daily time 54-69 (%) | +0.0236 | 0.0512 | ±0.1024 | +0.461 | 0.6448 | 1.0239 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0783**, LLR χ² = **90.67** (p = **1.23e-14**), AUC = **0.6933**, AIC = **1091.6**, BIC = **1153.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6688 | 0.6000 | ±1.2001 | -1.115 | 0.2650 | 0.5123 |  |
| Education: graduate level (vs college) | -0.0576 | 0.1711 | ±0.3423 | -0.336 | 0.7366 | 0.9441 |  |
| Education: high school or below (vs college) | +0.3491 | 0.2627 | ±0.5254 | +1.329 | 0.1839 | 1.4178 |  |
| Site: UCSD (vs UAB) | -0.1765 | 0.2140 | ±0.4279 | -0.825 | 0.4094 | 0.8382 |  |
| Site: UW (vs UAB) | -0.0248 | 0.1893 | ±0.3787 | -0.131 | 0.8956 | 0.9755 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.794** | **6.85e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0459** | 0.0104 | ±0.0208 | **+4.423** | **9.72e-06** | 1.0470 | *** |
| Hypertension | +0.2475 | 0.1732 | ±0.3464 | +1.429 | 0.1530 | 1.2808 |  |
| **High cholesterol** | **+0.4325** | 0.1650 | ±0.3300 | **+2.622** | **0.0088** | 1.5412 | ** |
| Kidney disease | +0.4732 | 0.2801 | ±0.5603 | +1.689 | 0.0912 | 1.6051 | . |
| **Circulatory disease** | **+0.5653** | 0.2217 | ±0.4433 | **+2.550** | **0.0108** | 1.7599 | * |
| Time < 70 (%) | +0.0184 | 0.0420 | ±0.0839 | +0.438 | 0.6617 | 1.0185 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.56** (p = **1.29e-14**), AUC = **0.6934**, AIC = **1091.7**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6576 | 0.5991 | ±1.1982 | -1.098 | 0.2723 | 0.5181 |  |
| Education: graduate level (vs college) | -0.0581 | 0.1712 | ±0.3423 | -0.339 | 0.7344 | 0.9436 |  |
| Education: high school or below (vs college) | +0.3470 | 0.2627 | ±0.5255 | +1.321 | 0.1866 | 1.4149 |  |
| Site: UCSD (vs UAB) | -0.1815 | 0.2134 | ±0.4269 | -0.850 | 0.3952 | 0.8340 |  |
| Site: UW (vs UAB) | -0.0279 | 0.1893 | ±0.3786 | -0.147 | 0.8829 | 0.9725 |  |
| **Age (years)** | **-0.0456** | 0.0079 | ±0.0157 | **-5.799** | **6.66e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0460** | 0.0104 | ±0.0208 | **+4.426** | **9.59e-06** | 1.0471 | *** |
| Hypertension | +0.2464 | 0.1732 | ±0.3464 | +1.422 | 0.1550 | 1.2794 |  |
| **High cholesterol** | **+0.4300** | 0.1648 | ±0.3297 | **+2.609** | **0.0091** | 1.5373 | ** |
| Kidney disease | +0.4738 | 0.2801 | ±0.5602 | +1.692 | 0.0907 | 1.6061 | . |
| **Circulatory disease** | **+0.5653** | 0.2217 | ±0.4433 | **+2.550** | **0.0108** | 1.7599 | * |
| Avg. daily time < 70 (%) | +0.0127 | 0.0443 | ±0.0886 | +0.287 | 0.7744 | 1.0128 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.57** (p = **1.29e-14**), AUC = **0.6934**, AIC = **1091.7**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2546 | 1.4514 | ±2.9029 | -0.175 | 0.8608 | 0.7752 |  |
| Education: graduate level (vs college) | -0.0603 | 0.1710 | ±0.3420 | -0.353 | 0.7241 | 0.9414 |  |
| Education: high school or below (vs college) | +0.3381 | 0.2623 | ±0.5246 | +1.289 | 0.1973 | 1.4023 |  |
| Site: UCSD (vs UAB) | -0.1857 | 0.2126 | ±0.4251 | -0.874 | 0.3822 | 0.8305 |  |
| Site: UW (vs UAB) | -0.0328 | 0.1882 | ±0.3764 | -0.174 | 0.8617 | 0.9677 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.796** | **6.78e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0460** | 0.0104 | ±0.0208 | **+4.433** | **9.30e-06** | 1.0471 | *** |
| Hypertension | +0.2431 | 0.1729 | ±0.3458 | +1.406 | 0.1597 | 1.2752 |  |
| **High cholesterol** | **+0.4282** | 0.1645 | ±0.3289 | **+2.604** | **0.0092** | 1.5345 | ** |
| Kidney disease | +0.4734 | 0.2801 | ±0.5602 | +1.690 | 0.0910 | 1.6054 | . |
| **Circulatory disease** | **+0.5591** | 0.2224 | ±0.4448 | **+2.514** | **0.0119** | 1.7491 | * |
| Time 54-250, pooled (%) | -0.0039 | 0.0133 | ±0.0267 | -0.295 | 0.7677 | 0.9961 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.57** (p = **1.29e-14**), AUC = **0.6934**, AIC = **1091.7**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2394 | 1.4727 | ±2.9453 | -0.163 | 0.8709 | 0.7871 |  |
| Education: graduate level (vs college) | -0.0604 | 0.1710 | ±0.3420 | -0.353 | 0.7240 | 0.9414 |  |
| Education: high school or below (vs college) | +0.3378 | 0.2623 | ±0.5246 | +1.288 | 0.1978 | 1.4019 |  |
| Site: UCSD (vs UAB) | -0.1859 | 0.2125 | ±0.4251 | -0.874 | 0.3819 | 0.8304 |  |
| Site: UW (vs UAB) | -0.0328 | 0.1882 | ±0.3763 | -0.174 | 0.8615 | 0.9677 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.797** | **6.74e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0460** | 0.0104 | ±0.0208 | **+4.432** | **9.33e-06** | 1.0471 | *** |
| Hypertension | +0.2431 | 0.1729 | ±0.3458 | +1.406 | 0.1597 | 1.2752 |  |
| **High cholesterol** | **+0.4282** | 0.1645 | ±0.3289 | **+2.603** | **0.0092** | 1.5344 | ** |
| Kidney disease | +0.4735 | 0.2801 | ±0.5602 | +1.690 | 0.0909 | 1.6056 | . |
| **Circulatory disease** | **+0.5590** | 0.2224 | ±0.4448 | **+2.513** | **0.0120** | 1.7489 | * |
| Avg. daily time 54-250 (%) | -0.0041 | 0.0135 | ±0.0270 | -0.302 | 0.7629 | 0.9959 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0813**, LLR χ² = **94.18** (p = **2.52e-15**), AUC = **0.6978**, AIC = **1088.1**, BIC = **1149.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6400 | 0.5983 | ±1.1966 | -1.070 | 0.2847 | 0.5273 |  |
| Education: graduate level (vs college) | -0.0752 | 0.1716 | ±0.3431 | -0.438 | 0.6610 | 0.9275 |  |
| Education: high school or below (vs college) | +0.3430 | 0.2622 | ±0.5244 | +1.308 | 0.1909 | 1.4092 |  |
| Site: UCSD (vs UAB) | -0.1744 | 0.2131 | ±0.4261 | -0.818 | 0.4131 | 0.8400 |  |
| Site: UW (vs UAB) | -0.0436 | 0.1887 | ±0.3774 | -0.231 | 0.8172 | 0.9573 |  |
| **Age (years)** | **-0.0460** | 0.0079 | ±0.0157 | **-5.844** | **5.09e-09** | 0.9551 | *** |
| **BMI (kg/m2)** | **+0.0453** | 0.0104 | ±0.0208 | **+4.343** | **1.40e-05** | 1.0463 | *** |
| Hypertension | +0.2231 | 0.1739 | ±0.3478 | +1.283 | 0.1994 | 1.2500 |  |
| **High cholesterol** | **+0.3983** | 0.1654 | ±0.3307 | **+2.408** | **0.0160** | 1.4893 | * |
| Kidney disease | +0.4236 | 0.2835 | ±0.5671 | +1.494 | 0.1352 | 1.5274 |  |
| **Circulatory disease** | **+0.5553** | 0.2223 | ±0.4447 | **+2.497** | **0.0125** | 1.7424 | * |
| **Time 181-250, pooled (%)** | **+0.0223** | 0.0114 | ±0.0228 | **+1.962** | **0.0497** | 1.0226 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0812**, LLR χ² = **94.10** (p = **2.61e-15**), AUC = **0.6976**, AIC = **1088.2**, BIC = **1149.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6403 | 0.5982 | ±1.1964 | -1.070 | 0.2844 | 0.5271 |  |
| Education: graduate level (vs college) | -0.0751 | 0.1716 | ±0.3431 | -0.438 | 0.6614 | 0.9276 |  |
| Education: high school or below (vs college) | +0.3458 | 0.2621 | ±0.5243 | +1.319 | 0.1870 | 1.4132 |  |
| Site: UCSD (vs UAB) | -0.1729 | 0.2131 | ±0.4261 | -0.811 | 0.4172 | 0.8412 |  |
| Site: UW (vs UAB) | -0.0419 | 0.1886 | ±0.3773 | -0.222 | 0.8242 | 0.9590 |  |
| **Age (years)** | **-0.0459** | 0.0079 | ±0.0157 | **-5.841** | **5.19e-09** | 0.9551 | *** |
| **BMI (kg/m2)** | **+0.0453** | 0.0104 | ±0.0208 | **+4.344** | **1.40e-05** | 1.0463 | *** |
| Hypertension | +0.2233 | 0.1739 | ±0.3477 | +1.285 | 0.1990 | 1.2502 |  |
| **High cholesterol** | **+0.3988** | 0.1654 | ±0.3307 | **+2.412** | **0.0159** | 1.4901 | * |
| Kidney disease | +0.4226 | 0.2836 | ±0.5672 | +1.490 | 0.1362 | 1.5259 |  |
| **Circulatory disease** | **+0.5557** | 0.2223 | ±0.4446 | **+2.500** | **0.0124** | 1.7431 | * |
| Avg. daily time 181-250 (%) | +0.0218 | 0.0112 | ±0.0224 | +1.944 | 0.0519 | 1.0221 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0799**, LLR χ² = **92.49** (p = **5.41e-15**), AUC = **0.6954**, AIC = **1089.8**, BIC = **1151.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6494 | 0.5982 | ±1.1964 | -1.086 | 0.2777 | 0.5224 |  |
| Education: graduate level (vs college) | -0.0677 | 0.1713 | ±0.3425 | -0.395 | 0.6927 | 0.9346 |  |
| Education: high school or below (vs college) | +0.3292 | 0.2622 | ±0.5244 | +1.256 | 0.2092 | 1.3899 |  |
| Site: UCSD (vs UAB) | -0.1798 | 0.2128 | ±0.4256 | -0.845 | 0.3982 | 0.8354 |  |
| Site: UW (vs UAB) | -0.0367 | 0.1884 | ±0.3768 | -0.195 | 0.8453 | 0.9639 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.813** | **6.15e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0456** | 0.0104 | ±0.0208 | **+4.388** | **1.14e-05** | 1.0467 | *** |
| Hypertension | +0.2320 | 0.1734 | ±0.3468 | +1.338 | 0.1809 | 1.2612 |  |
| **High cholesterol** | **+0.4163** | 0.1647 | ±0.3294 | **+2.528** | **0.0115** | 1.5164 | * |
| Kidney disease | +0.4494 | 0.2815 | ±0.5631 | +1.596 | 0.1104 | 1.5674 |  |
| **Circulatory disease** | **+0.5445** | 0.2226 | ±0.4453 | **+2.446** | **0.0145** | 1.7237 | * |
| Time > 180 (%) | +0.0106 | 0.0073 | ±0.0146 | +1.454 | 0.1459 | 1.0107 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0799**, LLR χ² = **92.52** (p = **5.33e-15**), AUC = **0.6954**, AIC = **1089.7**, BIC = **1151.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6484 | 0.5982 | ±1.1963 | -1.084 | 0.2784 | 0.5229 |  |
| Education: graduate level (vs college) | -0.0680 | 0.1713 | ±0.3425 | -0.397 | 0.6913 | 0.9342 |  |
| Education: high school or below (vs college) | +0.3303 | 0.2621 | ±0.5243 | +1.260 | 0.2077 | 1.3914 |  |
| Site: UCSD (vs UAB) | -0.1787 | 0.2128 | ±0.4256 | -0.839 | 0.4012 | 0.8364 |  |
| Site: UW (vs UAB) | -0.0361 | 0.1884 | ±0.3768 | -0.192 | 0.8481 | 0.9646 |  |
| **Age (years)** | **-0.0457** | 0.0079 | ±0.0157 | **-5.813** | **6.15e-09** | 0.9553 | *** |
| **BMI (kg/m2)** | **+0.0456** | 0.0104 | ±0.0208 | **+4.386** | **1.15e-05** | 1.0467 | *** |
| Hypertension | +0.2319 | 0.1734 | ±0.3468 | +1.337 | 0.1812 | 1.2609 |  |
| **High cholesterol** | **+0.4164** | 0.1647 | ±0.3294 | **+2.528** | **0.0115** | 1.5165 | * |
| Kidney disease | +0.4486 | 0.2816 | ±0.5632 | +1.593 | 0.1111 | 1.5661 |  |
| **Circulatory disease** | **+0.5446** | 0.2226 | ±0.4452 | **+2.446** | **0.0144** | 1.7239 | * |
| Avg. daily time > 180 (%) | +0.0107 | 0.0073 | ±0.0146 | +1.466 | 0.1425 | 1.0107 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0831**, LLR χ² = **96.29** (p = **9.65e-16**), AUC = **0.7006**, AIC = **1086.0**, BIC = **1147.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6243 | 0.5997 | ±1.1994 | -1.041 | 0.2979 | 0.5356 |  |
| Education: graduate level (vs college) | -0.0621 | 0.1716 | ±0.3431 | -0.362 | 0.7173 | 0.9398 |  |
| Education: high school or below (vs college) | +0.3148 | 0.2632 | ±0.5264 | +1.196 | 0.2317 | 1.3700 |  |
| Site: UCSD (vs UAB) | -0.1801 | 0.2132 | ±0.4264 | -0.845 | 0.3982 | 0.8352 |  |
| Site: UW (vs UAB) | -0.0388 | 0.1889 | ±0.3778 | -0.206 | 0.8371 | 0.9619 |  |
| **Age (years)** | **-0.0456** | 0.0079 | ±0.0158 | **-5.785** | **7.24e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0444** | 0.0105 | ±0.0209 | **+4.247** | **2.16e-05** | 1.0454 | *** |
| Hypertension | +0.2338 | 0.1737 | ±0.3474 | +1.346 | 0.1783 | 1.2634 |  |
| **High cholesterol** | **+0.4056** | 0.1652 | ±0.3305 | **+2.455** | **0.0141** | 1.5002 | * |
| Kidney disease | +0.4787 | 0.2806 | ±0.5613 | +1.706 | 0.0880 | 1.6140 | . |
| **Circulatory disease** | **+0.5497** | 0.2230 | ±0.4459 | **+2.465** | **0.0137** | 1.7327 | * |
| **Nocturnal time > 180 (%)** | **+0.0181** | 0.0075 | ±0.0150 | **+2.414** | **0.0158** | 1.0183 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0797**, LLR χ² = **92.27** (p = **5.99e-15**), AUC = **0.6933**, AIC = **1090.0**, BIC = **1151.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6994 | 0.5996 | ±1.1993 | -1.166 | 0.2435 | 0.4969 |  |
| Education: graduate level (vs college) | -0.0595 | 0.1711 | ±0.3421 | -0.348 | 0.7279 | 0.9422 |  |
| Education: high school or below (vs college) | +0.3438 | 0.2625 | ±0.5249 | +1.310 | 0.1902 | 1.4103 |  |
| Site: UCSD (vs UAB) | -0.1816 | 0.2128 | ±0.4256 | -0.853 | 0.3934 | 0.8339 |  |
| Site: UW (vs UAB) | -0.0353 | 0.1883 | ±0.3767 | -0.188 | 0.8512 | 0.9653 |  |
| **Age (years)** | **-0.0458** | 0.0079 | ±0.0157 | **-5.825** | **5.70e-09** | 0.9552 | *** |
| **BMI (kg/m2)** | **+0.0470** | 0.0104 | ±0.0208 | **+4.513** | **6.40e-06** | 1.0481 | *** |
| Hypertension | +0.2277 | 0.1737 | ±0.3473 | +1.311 | 0.1898 | 1.2557 |  |
| **High cholesterol** | **+0.4218** | 0.1646 | ±0.3293 | **+2.562** | **0.0104** | 1.5248 | * |
| Kidney disease | +0.4619 | 0.2812 | ±0.5623 | +1.643 | 0.1004 | 1.5871 |  |
| **Circulatory disease** | **+0.5612** | 0.2221 | ±0.4442 | **+2.527** | **0.0115** | 1.7527 | * |
| Any reading > 250 during wear (0/1) | +0.2607 | 0.1927 | ±0.3854 | +1.353 | 0.1761 | 1.2978 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.57** (p = **1.29e-14**), AUC = **0.6933**, AIC = **1091.7**, BIC = **1153.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6472 | 0.5977 | ±1.1955 | -1.083 | 0.2789 | 0.5235 |  |
| Education: graduate level (vs college) | -0.0604 | 0.1710 | ±0.3420 | -0.353 | 0.7241 | 0.9414 |  |
| Education: high school or below (vs college) | +0.3377 | 0.2623 | ±0.5246 | +1.288 | 0.1979 | 1.4018 |  |
| Site: UCSD (vs UAB) | -0.1864 | 0.2125 | ±0.4251 | -0.877 | 0.3804 | 0.8299 |  |
| Site: UW (vs UAB) | -0.0332 | 0.1882 | ±0.3763 | -0.177 | 0.8598 | 0.9673 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.797** | **6.76e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0460** | 0.0104 | ±0.0208 | **+4.433** | **9.29e-06** | 1.0471 | *** |
| Hypertension | +0.2430 | 0.1729 | ±0.3458 | +1.405 | 0.1600 | 1.2750 |  |
| **High cholesterol** | **+0.4279** | 0.1644 | ±0.3289 | **+2.602** | **0.0093** | 1.5340 | ** |
| Kidney disease | +0.4735 | 0.2801 | ±0.5602 | +1.690 | 0.0910 | 1.6056 | . |
| **Circulatory disease** | **+0.5590** | 0.2224 | ±0.4448 | **+2.513** | **0.0120** | 1.7489 | * |
| Time > 250 (%) | +0.0040 | 0.0133 | ±0.0266 | +0.302 | 0.7623 | 1.0040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,270)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1270**, events = **216**, McFadden pseudo-R² = **0.0782**, LLR χ² = **90.59** (p = **1.28e-14**), AUC = **0.6933**, AIC = **1091.7**, BIC = **1153.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6469 | 0.5978 | ±1.1955 | -1.082 | 0.2791 | 0.5236 |  |
| Education: graduate level (vs college) | -0.0605 | 0.1710 | ±0.3420 | -0.354 | 0.7237 | 0.9413 |  |
| Education: high school or below (vs college) | +0.3371 | 0.2624 | ±0.5247 | +1.285 | 0.1988 | 1.4009 |  |
| Site: UCSD (vs UAB) | -0.1863 | 0.2125 | ±0.4251 | -0.876 | 0.3808 | 0.8301 |  |
| Site: UW (vs UAB) | -0.0332 | 0.1882 | ±0.3763 | -0.176 | 0.8599 | 0.9673 |  |
| **Age (years)** | **-0.0455** | 0.0079 | ±0.0157 | **-5.797** | **6.75e-09** | 0.9555 | *** |
| **BMI (kg/m2)** | **+0.0460** | 0.0104 | ±0.0208 | **+4.432** | **9.32e-06** | 1.0471 | *** |
| Hypertension | +0.2429 | 0.1729 | ±0.3458 | +1.405 | 0.1601 | 1.2749 |  |
| **High cholesterol** | **+0.4281** | 0.1644 | ±0.3289 | **+2.603** | **0.0092** | 1.5343 | ** |
| Kidney disease | +0.4736 | 0.2801 | ±0.5602 | +1.691 | 0.0909 | 1.6058 | . |
| **Circulatory disease** | **+0.5584** | 0.2224 | ±0.4449 | **+2.510** | **0.0121** | 1.7479 | * |
| Avg. daily time > 250 (%) | +0.0045 | 0.0134 | ±0.0269 | +0.335 | 0.7379 | 1.0045 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 1,251; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1368**, F-statistic = **16.24** (p = **9.99e-35**), Residual SE = **0.858** on **1237** df, AIC = **3182.3**, BIC = **3254.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2254** | 0.1902 | ±0.3805 | **+11.699** | **1.30e-31** | *** |
| Education: graduate level (vs college) | -0.0145 | 0.0501 | ±0.1001 | -0.290 | 0.7715 |  |
| **Education: high school or below (vs college)** | **+0.5106** | 0.1213 | ±0.2427 | **+4.208** | **2.58e-05** | *** |
| Site: UCSD (vs UAB) | -0.0285 | 0.0658 | ±0.1317 | -0.432 | 0.6654 |  |
| **Site: UW (vs UAB)** | **-0.3790** | 0.0660 | ±0.1320 | **-5.741** | **9.39e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1570** | 0.0668 | ±0.1336 | **-2.351** | **0.0187** | * |
| Season: summer (vs autumn) | -0.0401 | 0.0731 | ±0.1461 | -0.549 | 0.5830 |  |
| Season: winter (vs autumn) | -0.0456 | 0.0702 | ±0.1404 | -0.649 | 0.5162 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.840** | **5.23e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.654** | **3.26e-06** | *** |
| Hypertension | +0.0922 | 0.0567 | ±0.1134 | +1.626 | 0.1040 |  |
| High cholesterol | -0.0393 | 0.0492 | ±0.0985 | -0.799 | 0.4244 |  |
| Kidney disease | -0.0661 | 0.0819 | ±0.1638 | -0.807 | 0.4198 |  |
| **Circulatory disease** | **+0.2269** | 0.0904 | ±0.1808 | **+2.511** | **0.0121** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1361**, F-statistic = **15.07** (p = **4.12e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.3**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2168** | 0.2767 | ±0.5534 | **+8.011** | **1.14e-15** | *** |
| Education: graduate level (vs college) | -0.0146 | 0.0501 | ±0.1002 | -0.291 | 0.7713 |  |
| **Education: high school or below (vs college)** | **+0.5103** | 0.1222 | ±0.2443 | **+4.177** | **2.95e-05** | *** |
| Site: UCSD (vs UAB) | -0.0285 | 0.0658 | ±0.1315 | -0.434 | 0.6646 |  |
| **Site: UW (vs UAB)** | **-0.3791** | 0.0659 | ±0.1319 | **-5.750** | **8.94e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1568** | 0.0670 | ±0.1340 | **-2.341** | **0.0192** | * |
| Season: summer (vs autumn) | -0.0400 | 0.0732 | ±0.1464 | -0.547 | 0.5844 |  |
| Season: winter (vs autumn) | -0.0455 | 0.0704 | ±0.1407 | -0.646 | 0.5180 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.861** | **4.60e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.642** | **3.46e-06** | *** |
| Hypertension | +0.0921 | 0.0568 | ±0.1136 | +1.621 | 0.1050 |  |
| High cholesterol | -0.0395 | 0.0494 | ±0.0989 | -0.799 | 0.4241 |  |
| Kidney disease | -0.0661 | 0.0819 | ±0.1639 | -0.806 | 0.4202 |  |
| **Circulatory disease** | **+0.2268** | 0.0909 | ±0.1817 | **+2.496** | **0.0126** | * |
| HbA1c (%) | +0.0017 | 0.0358 | ±0.0717 | +0.047 | 0.9627 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **1251**, R² = **0.1489**, Adj R² = **0.1393**, F-statistic = **15.45** (p = **4.83e-35**), Residual SE = **0.857** on **1236** df, AIC = **3179.7**, BIC = **3256.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.5269** | 0.2363 | ±0.4726 | **+10.693** | **1.10e-26** | *** |
| Education: graduate level (vs college) | -0.0082 | 0.0500 | ±0.1000 | -0.164 | 0.8696 |  |
| **Education: high school or below (vs college)** | **+0.5266** | 0.1219 | ±0.2437 | **+4.321** | **1.55e-05** | *** |
| Site: UCSD (vs UAB) | -0.0309 | 0.0658 | ±0.1315 | -0.470 | 0.6384 |  |
| **Site: UW (vs UAB)** | **-0.3710** | 0.0659 | ±0.1318 | **-5.629** | **1.81e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1619** | 0.0670 | ±0.1339 | **-2.418** | **0.0156** | * |
| Season: summer (vs autumn) | -0.0479 | 0.0731 | ±0.1461 | -0.655 | 0.5124 |  |
| Season: winter (vs autumn) | -0.0538 | 0.0700 | ±0.1399 | -0.768 | 0.4422 |  |
| **Age (years)** | **-0.0130** | 0.0023 | ±0.0045 | **-5.769** | **7.96e-09** | *** |
| **BMI (kg/m2)** | **+0.0190** | 0.0040 | ±0.0080 | **+4.774** | **1.81e-06** | *** |
| Hypertension | +0.1018 | 0.0571 | ±0.1141 | +1.784 | 0.0745 | . |
| High cholesterol | -0.0339 | 0.0492 | ±0.0984 | -0.689 | 0.4907 |  |
| Kidney disease | -0.0572 | 0.0813 | ±0.1626 | -0.704 | 0.4817 |  |
| **Circulatory disease** | **+0.2346** | 0.0904 | ±0.1809 | **+2.594** | **0.0095** | ** |
| **Mean glucose (mg/dL)** | **-0.0027** | 0.0011 | ±0.0023 | **-2.407** | **0.0161** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **1251**, R² = **0.1489**, Adj R² = **0.1393**, F-statistic = **15.45** (p = **4.83e-35**), Residual SE = **0.857** on **1236** df, AIC = **3179.7**, BIC = **3256.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.9069** | 0.3543 | ±0.7085 | **+8.206** | **2.29e-16** | *** |
| Education: graduate level (vs college) | -0.0082 | 0.0500 | ±0.1000 | -0.164 | 0.8696 |  |
| **Education: high school or below (vs college)** | **+0.5266** | 0.1219 | ±0.2437 | **+4.321** | **1.55e-05** | *** |
| Site: UCSD (vs UAB) | -0.0309 | 0.0658 | ±0.1315 | -0.470 | 0.6384 |  |
| **Site: UW (vs UAB)** | **-0.3710** | 0.0659 | ±0.1318 | **-5.629** | **1.81e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1619** | 0.0670 | ±0.1339 | **-2.418** | **0.0156** | * |
| Season: summer (vs autumn) | -0.0479 | 0.0731 | ±0.1461 | -0.655 | 0.5124 |  |
| Season: winter (vs autumn) | -0.0538 | 0.0700 | ±0.1399 | -0.768 | 0.4422 |  |
| **Age (years)** | **-0.0130** | 0.0023 | ±0.0045 | **-5.769** | **7.96e-09** | *** |
| **BMI (kg/m2)** | **+0.0190** | 0.0040 | ±0.0080 | **+4.774** | **1.81e-06** | *** |
| Hypertension | +0.1018 | 0.0571 | ±0.1141 | +1.784 | 0.0745 | . |
| High cholesterol | -0.0339 | 0.0492 | ±0.0984 | -0.689 | 0.4907 |  |
| Kidney disease | -0.0572 | 0.0813 | ±0.1626 | -0.704 | 0.4817 |  |
| **Circulatory disease** | **+0.2346** | 0.0904 | ±0.1809 | **+2.594** | **0.0095** | ** |
| **GMI (%)** | **-0.1148** | 0.0477 | ±0.0954 | **-2.407** | **0.0161** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **1251**, R² = **0.1481**, Adj R² = **0.1384**, F-statistic = **15.35** (p = **8.60e-35**), Residual SE = **0.858** on **1236** df, AIC = **3180.9**, BIC = **3257.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.4652** | 0.2287 | ±0.4573 | **+10.781** | **4.24e-27** | *** |
| Education: graduate level (vs college) | -0.0109 | 0.0500 | ±0.1000 | -0.218 | 0.8271 |  |
| **Education: high school or below (vs college)** | **+0.5236** | 0.1220 | ±0.2440 | **+4.291** | **1.78e-05** | *** |
| Site: UCSD (vs UAB) | -0.0272 | 0.0658 | ±0.1315 | -0.413 | 0.6796 |  |
| **Site: UW (vs UAB)** | **-0.3730** | 0.0659 | ±0.1318 | **-5.662** | **1.49e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1575** | 0.0668 | ±0.1335 | **-2.359** | **0.0183** | * |
| Season: summer (vs autumn) | -0.0460 | 0.0731 | ±0.1463 | -0.629 | 0.5296 |  |
| Season: winter (vs autumn) | -0.0488 | 0.0699 | ±0.1399 | -0.698 | 0.4854 |  |
| **Age (years)** | **-0.0133** | 0.0023 | ±0.0045 | **-5.859** | **4.66e-09** | *** |
| **BMI (kg/m2)** | **+0.0195** | 0.0040 | ±0.0080 | **+4.867** | **1.13e-06** | *** |
| Hypertension | +0.0987 | 0.0570 | ±0.1139 | +1.732 | 0.0833 | . |
| High cholesterol | -0.0332 | 0.0492 | ±0.0985 | -0.675 | 0.4999 |  |
| Kidney disease | -0.0650 | 0.0816 | ±0.1632 | -0.796 | 0.4258 |  |
| **Circulatory disease** | **+0.2310** | 0.0905 | ±0.1810 | **+2.552** | **0.0107** | * |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0022** | 0.0011 | ±0.0021 | **-2.108** | **0.0350** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.1470**, Adj R² = **0.1373**, F-statistic = **15.21** (p = **1.84e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.5**, BIC = **3259.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.3171** | 0.2011 | ±0.4022 | **+11.522** | **1.02e-30** | *** |
| Education: graduate level (vs college) | -0.0138 | 0.0500 | ±0.1001 | -0.275 | 0.7833 |  |
| **Education: high school or below (vs college)** | **+0.5121** | 0.1214 | ±0.2428 | **+4.219** | **2.46e-05** | *** |
| Site: UCSD (vs UAB) | -0.0331 | 0.0660 | ±0.1319 | -0.502 | 0.6158 |  |
| **Site: UW (vs UAB)** | **-0.3766** | 0.0662 | ±0.1323 | **-5.692** | **1.25e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1601** | 0.0667 | ±0.1335 | **-2.398** | **0.0165** | * |
| Season: summer (vs autumn) | -0.0432 | 0.0731 | ±0.1462 | -0.591 | 0.5547 |  |
| Season: winter (vs autumn) | -0.0484 | 0.0702 | ±0.1405 | -0.689 | 0.4906 |  |
| **Age (years)** | **-0.0130** | 0.0023 | ±0.0045 | **-5.760** | **8.40e-09** | *** |
| **BMI (kg/m2)** | **+0.0187** | 0.0040 | ±0.0080 | **+4.675** | **2.94e-06** | *** |
| Hypertension | +0.0983 | 0.0570 | ±0.1139 | +1.725 | 0.0845 | . |
| High cholesterol | -0.0394 | 0.0492 | ±0.0984 | -0.801 | 0.4229 |  |
| Kidney disease | -0.0560 | 0.0815 | ±0.1629 | -0.687 | 0.4918 |  |
| **Circulatory disease** | **+0.2312** | 0.0904 | ±0.1809 | **+2.557** | **0.0106** | * |
| Glucose SD, pooled (mg/dL) | -0.0049 | 0.0035 | ±0.0069 | -1.419 | 0.1559 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.1467**, Adj R² = **0.1370**, F-statistic = **15.18** (p = **2.25e-34**), Residual SE = **0.858** on **1236** df, AIC = **3183.0**, BIC = **3259.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2996** | 0.2005 | ±0.4010 | **+11.470** | **1.86e-30** | *** |
| Education: graduate level (vs college) | -0.0134 | 0.0501 | ±0.1001 | -0.268 | 0.7887 |  |
| **Education: high school or below (vs college)** | **+0.5121** | 0.1214 | ±0.2428 | **+4.218** | **2.46e-05** | *** |
| Site: UCSD (vs UAB) | -0.0321 | 0.0659 | ±0.1319 | -0.486 | 0.6267 |  |
| **Site: UW (vs UAB)** | **-0.3765** | 0.0662 | ±0.1325 | **-5.685** | **1.31e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1603** | 0.0668 | ±0.1336 | **-2.399** | **0.0164** | * |
| Season: summer (vs autumn) | -0.0437 | 0.0732 | ±0.1464 | -0.596 | 0.5509 |  |
| Season: winter (vs autumn) | -0.0488 | 0.0703 | ±0.1406 | -0.694 | 0.4880 |  |
| **Age (years)** | **-0.0130** | 0.0023 | ±0.0045 | **-5.765** | **8.16e-09** | *** |
| **BMI (kg/m2)** | **+0.0187** | 0.0040 | ±0.0080 | **+4.682** | **2.84e-06** | *** |
| Hypertension | +0.0974 | 0.0570 | ±0.1141 | +1.707 | 0.0879 | . |
| High cholesterol | -0.0392 | 0.0492 | ±0.0984 | -0.797 | 0.4255 |  |
| Kidney disease | -0.0568 | 0.0816 | ±0.1632 | -0.696 | 0.4862 |  |
| **Circulatory disease** | **+0.2305** | 0.0905 | ±0.1810 | **+2.547** | **0.0109** | * |
| Avg. daily SD (mg/dL) | -0.0046 | 0.0038 | ±0.0076 | -1.194 | 0.2325 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1361**, F-statistic = **15.07** (p = **4.08e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.2**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2414** | 0.2111 | ±0.4222 | **+10.617** | **2.49e-26** | *** |
| Education: graduate level (vs college) | -0.0148 | 0.0501 | ±0.1003 | -0.294 | 0.7685 |  |
| **Education: high school or below (vs college)** | **+0.5101** | 0.1217 | ±0.2435 | **+4.190** | **2.79e-05** | *** |
| Site: UCSD (vs UAB) | -0.0291 | 0.0661 | ±0.1323 | -0.441 | 0.6595 |  |
| **Site: UW (vs UAB)** | **-0.3791** | 0.0660 | ±0.1320 | **-5.744** | **9.25e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1572** | 0.0667 | ±0.1335 | **-2.356** | **0.0185** | * |
| Season: summer (vs autumn) | -0.0402 | 0.0731 | ±0.1462 | -0.549 | 0.5829 |  |
| Season: winter (vs autumn) | -0.0455 | 0.0703 | ±0.1405 | -0.648 | 0.5169 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.820** | **5.90e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.653** | **3.28e-06** | *** |
| Hypertension | +0.0926 | 0.0567 | ±0.1134 | +1.633 | 0.1024 |  |
| High cholesterol | -0.0397 | 0.0493 | ±0.0987 | -0.804 | 0.4213 |  |
| Kidney disease | -0.0651 | 0.0822 | ±0.1645 | -0.791 | 0.4288 |  |
| **Circulatory disease** | **+0.2271** | 0.0905 | ±0.1810 | **+2.510** | **0.0121** | * |
| CV (%) | -0.0009 | 0.0059 | ±0.0118 | -0.159 | 0.8736 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1361**, F-statistic = **15.07** (p = **4.13e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.3**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2235** | 0.2289 | ±0.4577 | **+9.716** | **2.58e-22** | *** |
| Education: graduate level (vs college) | -0.0146 | 0.0502 | ±0.1003 | -0.290 | 0.7716 |  |
| **Education: high school or below (vs college)** | **+0.5106** | 0.1215 | ±0.2431 | **+4.201** | **2.66e-05** | *** |
| Site: UCSD (vs UAB) | -0.0285 | 0.0661 | ±0.1321 | -0.432 | 0.6658 |  |
| **Site: UW (vs UAB)** | **-0.3790** | 0.0661 | ±0.1323 | **-5.731** | **9.96e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1570** | 0.0668 | ±0.1336 | **-2.351** | **0.0187** | * |
| Season: summer (vs autumn) | -0.0401 | 0.0731 | ±0.1462 | -0.549 | 0.5831 |  |
| Season: winter (vs autumn) | -0.0456 | 0.0703 | ±0.1405 | -0.648 | 0.5168 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.824** | **5.74e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.653** | **3.27e-06** | *** |
| Hypertension | +0.0922 | 0.0567 | ±0.1134 | +1.627 | 0.1038 |  |
| High cholesterol | -0.0394 | 0.0493 | ±0.0986 | -0.798 | 0.4247 |  |
| Kidney disease | -0.0660 | 0.0822 | ±0.1643 | -0.803 | 0.4219 |  |
| **Circulatory disease** | **+0.2269** | 0.0905 | ±0.1810 | **+2.508** | **0.0121** | * |
| Mean / SD ratio | +0.0003 | 0.0191 | ±0.0383 | +0.016 | 0.9872 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.1459**, Adj R² = **0.1362**, F-statistic = **15.08** (p = **3.98e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.2**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2598** | 0.2277 | ±0.4554 | **+9.925** | **3.25e-23** | *** |
| Education: graduate level (vs college) | -0.0143 | 0.0501 | ±0.1002 | -0.286 | 0.7751 |  |
| **Education: high school or below (vs college)** | **+0.5106** | 0.1214 | ±0.2428 | **+4.207** | **2.59e-05** | *** |
| Site: UCSD (vs UAB) | -0.0277 | 0.0660 | ±0.1320 | -0.419 | 0.6749 |  |
| **Site: UW (vs UAB)** | **-0.3793** | 0.0662 | ±0.1324 | **-5.731** | **1.00e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1568** | 0.0668 | ±0.1336 | **-2.348** | **0.0189** | * |
| Season: summer (vs autumn) | -0.0396 | 0.0730 | ±0.1461 | -0.542 | 0.5879 |  |
| Season: winter (vs autumn) | -0.0457 | 0.0702 | ±0.1405 | -0.650 | 0.5154 |  |
| **Age (years)** | **-0.0133** | 0.0023 | ±0.0045 | **-5.842** | **5.17e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.644** | **3.42e-06** | *** |
| Hypertension | +0.0916 | 0.0567 | ±0.1135 | +1.614 | 0.1066 |  |
| High cholesterol | -0.0390 | 0.0493 | ±0.0986 | -0.790 | 0.4295 |  |
| Kidney disease | -0.0678 | 0.0825 | ±0.1649 | -0.822 | 0.4112 |  |
| **Circulatory disease** | **+0.2268** | 0.0905 | ±0.1810 | **+2.506** | **0.0122** | * |
| Avg. daily mean/SD | -0.0046 | 0.0158 | ±0.0315 | -0.292 | 0.7704 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1251**, R² = **0.1468**, Adj R² = **0.1372**, F-statistic = **15.20** (p = **2.02e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.7**, BIC = **3259.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0699** | 0.2214 | ±0.4428 | **+9.350** | **8.76e-21** | *** |
| Education: graduate level (vs college) | -0.0136 | 0.0500 | ±0.1000 | -0.271 | 0.7862 |  |
| **Education: high school or below (vs college)** | **+0.5079** | 0.1216 | ±0.2433 | **+4.176** | **2.97e-05** | *** |
| Site: UCSD (vs UAB) | -0.0228 | 0.0660 | ±0.1320 | -0.345 | 0.7300 |  |
| **Site: UW (vs UAB)** | **-0.3735** | 0.0662 | ±0.1325 | **-5.640** | **1.70e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1553** | 0.0667 | ±0.1334 | **-2.329** | **0.0199** | * |
| Season: summer (vs autumn) | -0.0372 | 0.0730 | ±0.1460 | -0.509 | 0.6108 |  |
| Season: winter (vs autumn) | -0.0432 | 0.0701 | ±0.1402 | -0.616 | 0.5380 |  |
| **Age (years)** | **-0.0131** | 0.0023 | ±0.0045 | **-5.820** | **5.88e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.636** | **3.55e-06** | *** |
| Hypertension | +0.0925 | 0.0567 | ±0.1135 | +1.630 | 0.1030 |  |
| High cholesterol | -0.0361 | 0.0494 | ±0.0989 | -0.730 | 0.4652 |  |
| Kidney disease | -0.0696 | 0.0820 | ±0.1640 | -0.849 | 0.3959 |  |
| **Circulatory disease** | **+0.2258** | 0.0902 | ±0.1803 | **+2.504** | **0.0123** | * |
| MAG (mg/dL/h) | +0.0038 | 0.0031 | ±0.0061 | +1.242 | 0.2143 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **1251**, R² = **0.1466**, Adj R² = **0.1369**, F-statistic = **15.16** (p = **2.46e-34**), Residual SE = **0.858** on **1236** df, AIC = **3183.2**, BIC = **3260.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.3187** | 0.2097 | ±0.4193 | **+11.059** | **1.98e-28** | *** |
| Education: graduate level (vs college) | -0.0134 | 0.0501 | ±0.1002 | -0.267 | 0.7896 |  |
| **Education: high school or below (vs college)** | **+0.5125** | 0.1215 | ±0.2430 | **+4.218** | **2.47e-05** | *** |
| Site: UCSD (vs UAB) | -0.0320 | 0.0658 | ±0.1317 | -0.487 | 0.6265 |  |
| **Site: UW (vs UAB)** | **-0.3779** | 0.0662 | ±0.1323 | **-5.711** | **1.12e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1595** | 0.0668 | ±0.1336 | **-2.388** | **0.0169** | * |
| Season: summer (vs autumn) | -0.0434 | 0.0731 | ±0.1462 | -0.594 | 0.5525 |  |
| Season: winter (vs autumn) | -0.0482 | 0.0703 | ±0.1406 | -0.685 | 0.4935 |  |
| **Age (years)** | **-0.0131** | 0.0023 | ±0.0045 | **-5.780** | **7.47e-09** | *** |
| **BMI (kg/m2)** | **+0.0185** | 0.0040 | ±0.0080 | **+4.630** | **3.65e-06** | *** |
| Hypertension | +0.0955 | 0.0569 | ±0.1138 | +1.680 | 0.0930 | . |
| High cholesterol | -0.0405 | 0.0492 | ±0.0985 | -0.822 | 0.4113 |  |
| Kidney disease | -0.0592 | 0.0816 | ±0.1631 | -0.726 | 0.4676 |  |
| **Circulatory disease** | **+0.2300** | 0.0905 | ±0.1810 | **+2.542** | **0.0110** | * |
| Avg. daily range (mg/dL) | -0.0010 | 0.0009 | ±0.0019 | -1.042 | 0.2976 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **1251**, R² = **0.1469**, Adj R² = **0.1372**, F-statistic = **15.20** (p = **1.93e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.6**, BIC = **3259.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2750** | 0.1905 | ±0.3811 | **+11.940** | **7.29e-33** | *** |
| Education: graduate level (vs college) | -0.0145 | 0.0501 | ±0.1001 | -0.290 | 0.7721 |  |
| **Education: high school or below (vs college)** | **+0.5103** | 0.1216 | ±0.2431 | **+4.198** | **2.69e-05** | *** |
| Site: UCSD (vs UAB) | -0.0326 | 0.0657 | ±0.1314 | -0.496 | 0.6201 |  |
| **Site: UW (vs UAB)** | **-0.3782** | 0.0661 | ±0.1322 | **-5.722** | **1.05e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1530** | 0.0670 | ±0.1341 | **-2.283** | **0.0225** | * |
| Season: summer (vs autumn) | -0.0367 | 0.0733 | ±0.1466 | -0.501 | 0.6162 |  |
| Season: winter (vs autumn) | -0.0438 | 0.0703 | ±0.1406 | -0.623 | 0.5334 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.823** | **5.77e-09** | *** |
| **BMI (kg/m2)** | **+0.0189** | 0.0040 | ±0.0081 | **+4.700** | **2.60e-06** | *** |
| Hypertension | +0.0934 | 0.0567 | ±0.1135 | +1.646 | 0.0997 | . |
| High cholesterol | -0.0380 | 0.0492 | ±0.0984 | -0.773 | 0.4397 |  |
| Kidney disease | -0.0656 | 0.0818 | ±0.1635 | -0.802 | 0.4224 |  |
| **Circulatory disease** | **+0.2309** | 0.0903 | ±0.1807 | **+2.556** | **0.0106** | * |
| SD of daily means (mg/dL) | -0.0094 | 0.0066 | ±0.0132 | -1.424 | 0.1545 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **1251**, R² = **0.1471**, Adj R² = **0.1375**, F-statistic = **15.23** (p = **1.66e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.3**, BIC = **3259.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8539** | 0.2784 | ±0.5568 | **+6.659** | **2.76e-11** | *** |
| Education: graduate level (vs college) | -0.0129 | 0.0500 | ±0.1001 | -0.257 | 0.7971 |  |
| **Education: high school or below (vs college)** | **+0.5156** | 0.1215 | ±0.2430 | **+4.244** | **2.20e-05** | *** |
| Site: UCSD (vs UAB) | -0.0337 | 0.0660 | ±0.1320 | -0.510 | 0.6101 |  |
| **Site: UW (vs UAB)** | **-0.3790** | 0.0659 | ±0.1319 | **-5.746** | **9.13e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1603** | 0.0668 | ±0.1336 | **-2.401** | **0.0164** | * |
| Season: summer (vs autumn) | -0.0465 | 0.0731 | ±0.1461 | -0.637 | 0.5244 |  |
| Season: winter (vs autumn) | -0.0488 | 0.0701 | ±0.1401 | -0.696 | 0.4865 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.829** | **5.59e-09** | *** |
| **BMI (kg/m2)** | **+0.0188** | 0.0040 | ±0.0080 | **+4.702** | **2.57e-06** | *** |
| Hypertension | +0.0960 | 0.0569 | ±0.1137 | +1.689 | 0.0913 | . |
| High cholesterol | -0.0378 | 0.0492 | ±0.0985 | -0.768 | 0.4424 |  |
| Kidney disease | -0.0592 | 0.0813 | ±0.1627 | -0.727 | 0.4670 |  |
| **Circulatory disease** | **+0.2319** | 0.0906 | ±0.1813 | **+2.559** | **0.0105** | * |
| Time in range 70-180, pooled (%) | +0.0038 | 0.0022 | ±0.0044 | +1.731 | 0.0834 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **1251**, R² = **0.1471**, Adj R² = **0.1374**, F-statistic = **15.23** (p = **1.69e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.3**, BIC = **3259.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8568** | 0.2789 | ±0.5578 | **+6.657** | **2.79e-11** | *** |
| Education: graduate level (vs college) | -0.0129 | 0.0500 | ±0.1001 | -0.257 | 0.7971 |  |
| **Education: high school or below (vs college)** | **+0.5151** | 0.1215 | ±0.2429 | **+4.241** | **2.23e-05** | *** |
| Site: UCSD (vs UAB) | -0.0334 | 0.0660 | ±0.1320 | -0.506 | 0.6125 |  |
| **Site: UW (vs UAB)** | **-0.3791** | 0.0660 | ±0.1319 | **-5.748** | **9.05e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1600** | 0.0668 | ±0.1336 | **-2.395** | **0.0166** | * |
| Season: summer (vs autumn) | -0.0465 | 0.0731 | ±0.1461 | -0.637 | 0.5244 |  |
| Season: winter (vs autumn) | -0.0486 | 0.0701 | ±0.1402 | -0.694 | 0.4878 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.827** | **5.66e-09** | *** |
| **BMI (kg/m2)** | **+0.0188** | 0.0040 | ±0.0080 | **+4.705** | **2.54e-06** | *** |
| Hypertension | +0.0959 | 0.0568 | ±0.1137 | +1.687 | 0.0916 | . |
| High cholesterol | -0.0376 | 0.0492 | ±0.0985 | -0.765 | 0.4446 |  |
| Kidney disease | -0.0592 | 0.0813 | ±0.1627 | -0.728 | 0.4668 |  |
| **Circulatory disease** | **+0.2319** | 0.0907 | ±0.1813 | **+2.558** | **0.0105** | * |
| Avg. daily time in range 70-180 (%) | +0.0038 | 0.0022 | ±0.0044 | +1.719 | 0.0856 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1361**, F-statistic = **15.07** (p = **4.08e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.2**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2296** | 0.1899 | ±0.3799 | **+11.738** | **8.10e-32** | *** |
| Education: graduate level (vs college) | -0.0149 | 0.0500 | ±0.1001 | -0.297 | 0.7665 |  |
| **Education: high school or below (vs college)** | **+0.5096** | 0.1226 | ±0.2451 | **+4.158** | **3.22e-05** | *** |
| Site: UCSD (vs UAB) | -0.0296 | 0.0661 | ±0.1322 | -0.448 | 0.6542 |  |
| **Site: UW (vs UAB)** | **-0.3795** | 0.0657 | ±0.1314 | **-5.774** | **7.72e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1570** | 0.0668 | ±0.1336 | **-2.351** | **0.0187** | * |
| Season: summer (vs autumn) | -0.0403 | 0.0731 | ±0.1461 | -0.552 | 0.5812 |  |
| Season: winter (vs autumn) | -0.0458 | 0.0703 | ±0.1406 | -0.651 | 0.5151 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.832** | **5.49e-09** | *** |
| **BMI (kg/m2)** | **+0.0187** | 0.0040 | ±0.0080 | **+4.638** | **3.52e-06** | *** |
| Hypertension | +0.0922 | 0.0568 | ±0.1135 | +1.624 | 0.1044 |  |
| High cholesterol | -0.0397 | 0.0494 | ±0.0987 | -0.805 | 0.4209 |  |
| Kidney disease | -0.0661 | 0.0820 | ±0.1639 | -0.806 | 0.4201 |  |
| **Circulatory disease** | **+0.2276** | 0.0904 | ±0.1808 | **+2.517** | **0.0118** | * |
| Any reading < 54 during wear (0/1) | -0.0078 | 0.0564 | ±0.1127 | -0.139 | 0.8893 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.1459**, Adj R² = **0.1362**, F-statistic = **15.08** (p = **3.82e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.1**, BIC = **3261.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2325** | 0.1903 | ±0.3806 | **+11.732** | **8.70e-32** | *** |
| Education: graduate level (vs college) | -0.0149 | 0.0500 | ±0.1001 | -0.298 | 0.7654 |  |
| **Education: high school or below (vs college)** | **+0.5087** | 0.1214 | ±0.2428 | **+4.191** | **2.78e-05** | *** |
| Site: UCSD (vs UAB) | -0.0317 | 0.0663 | ±0.1327 | -0.478 | 0.6330 |  |
| **Site: UW (vs UAB)** | **-0.3814** | 0.0661 | ±0.1322 | **-5.772** | **7.83e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1573** | 0.0668 | ±0.1335 | **-2.357** | **0.0184** | * |
| Season: summer (vs autumn) | -0.0395 | 0.0732 | ±0.1464 | -0.540 | 0.5894 |  |
| Season: winter (vs autumn) | -0.0453 | 0.0703 | ±0.1406 | -0.644 | 0.5198 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.844** | **5.11e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.646** | **3.38e-06** | *** |
| Hypertension | +0.0915 | 0.0567 | ±0.1134 | +1.614 | 0.1065 |  |
| High cholesterol | -0.0407 | 0.0495 | ±0.0991 | -0.822 | 0.4109 |  |
| Kidney disease | -0.0655 | 0.0819 | ±0.1639 | -0.800 | 0.4237 |  |
| **Circulatory disease** | **+0.2268** | 0.0904 | ±0.1807 | **+2.510** | **0.0121** | * |
| Time < 54 (%) | -0.0175 | 0.0316 | ±0.0632 | -0.554 | 0.5799 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.1459**, Adj R² = **0.1362**, F-statistic = **15.08** (p = **3.85e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.1**, BIC = **3261.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2301** | 0.1900 | ±0.3801 | **+11.734** | **8.49e-32** | *** |
| Education: graduate level (vs college) | -0.0151 | 0.0501 | ±0.1001 | -0.301 | 0.7632 |  |
| **Education: high school or below (vs college)** | **+0.5088** | 0.1215 | ±0.2430 | **+4.188** | **2.81e-05** | *** |
| Site: UCSD (vs UAB) | -0.0312 | 0.0663 | ±0.1325 | -0.470 | 0.6381 |  |
| **Site: UW (vs UAB)** | **-0.3817** | 0.0662 | ±0.1324 | **-5.764** | **8.23e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1570** | 0.0668 | ±0.1336 | **-2.351** | **0.0187** | * |
| Season: summer (vs autumn) | -0.0394 | 0.0732 | ±0.1463 | -0.539 | 0.5901 |  |
| Season: winter (vs autumn) | -0.0448 | 0.0703 | ±0.1406 | -0.637 | 0.5240 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.832** | **5.46e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.648** | **3.35e-06** | *** |
| Hypertension | +0.0912 | 0.0569 | ±0.1138 | +1.603 | 0.1090 |  |
| High cholesterol | -0.0405 | 0.0494 | ±0.0988 | -0.820 | 0.4121 |  |
| Kidney disease | -0.0656 | 0.0819 | ±0.1638 | -0.801 | 0.4234 |  |
| **Circulatory disease** | **+0.2267** | 0.0904 | ±0.1808 | **+2.507** | **0.0122** | * |
| Avg. daily time < 54 (%) | -0.0223 | 0.0429 | ±0.0859 | -0.520 | 0.6030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1361**, F-statistic = **15.07** (p = **4.10e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.2**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2275** | 0.1904 | ±0.3807 | **+11.701** | **1.26e-31** | *** |
| Education: graduate level (vs college) | -0.0148 | 0.0501 | ±0.1002 | -0.296 | 0.7672 |  |
| **Education: high school or below (vs college)** | **+0.5098** | 0.1224 | ±0.2447 | **+4.166** | **3.10e-05** | *** |
| Site: UCSD (vs UAB) | -0.0291 | 0.0664 | ±0.1328 | -0.438 | 0.6614 |  |
| **Site: UW (vs UAB)** | **-0.3797** | 0.0663 | ±0.1325 | **-5.731** | **1.00e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1569** | 0.0670 | ±0.1339 | **-2.343** | **0.0191** | * |
| Season: summer (vs autumn) | -0.0400 | 0.0732 | ±0.1465 | -0.546 | 0.5849 |  |
| Season: winter (vs autumn) | -0.0452 | 0.0706 | ±0.1412 | -0.640 | 0.5219 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.831** | **5.52e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.644** | **3.41e-06** | *** |
| Hypertension | +0.0919 | 0.0569 | ±0.1137 | +1.617 | 0.1060 |  |
| High cholesterol | -0.0397 | 0.0493 | ±0.0986 | -0.804 | 0.4211 |  |
| Kidney disease | -0.0661 | 0.0819 | ±0.1639 | -0.807 | 0.4198 |  |
| **Circulatory disease** | **+0.2269** | 0.0904 | ±0.1808 | **+2.510** | **0.0121** | * |
| Time 54-69, pooled (%) | -0.0020 | 0.0175 | ±0.0351 | -0.113 | 0.9102 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1361**, F-statistic = **15.07** (p = **4.12e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.3**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2263** | 0.1903 | ±0.3807 | **+11.698** | **1.31e-31** | *** |
| Education: graduate level (vs college) | -0.0147 | 0.0502 | ±0.1004 | -0.293 | 0.7694 |  |
| **Education: high school or below (vs college)** | **+0.5101** | 0.1225 | ±0.2450 | **+4.163** | **3.13e-05** | *** |
| Site: UCSD (vs UAB) | -0.0287 | 0.0662 | ±0.1325 | -0.434 | 0.6646 |  |
| **Site: UW (vs UAB)** | **-0.3794** | 0.0664 | ±0.1327 | **-5.716** | **1.09e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1569** | 0.0670 | ±0.1340 | **-2.343** | **0.0191** | * |
| Season: summer (vs autumn) | -0.0401 | 0.0732 | ±0.1463 | -0.548 | 0.5838 |  |
| Season: winter (vs autumn) | -0.0453 | 0.0706 | ±0.1412 | -0.642 | 0.5206 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.835** | **5.39e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.644** | **3.41e-06** | *** |
| Hypertension | +0.0920 | 0.0570 | ±0.1139 | +1.615 | 0.1062 |  |
| High cholesterol | -0.0395 | 0.0492 | ±0.0985 | -0.802 | 0.4225 |  |
| Kidney disease | -0.0661 | 0.0819 | ±0.1639 | -0.807 | 0.4199 |  |
| **Circulatory disease** | **+0.2269** | 0.0904 | ±0.1808 | **+2.510** | **0.0121** | * |
| Avg. daily time 54-69 (%) | -0.0011 | 0.0181 | ±0.0361 | -0.058 | 0.9534 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1362**, F-statistic = **15.07** (p = **4.03e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.2**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2299** | 0.1904 | ±0.3808 | **+11.712** | **1.10e-31** | *** |
| Education: graduate level (vs college) | -0.0151 | 0.0501 | ±0.1001 | -0.301 | 0.7633 |  |
| **Education: high school or below (vs college)** | **+0.5090** | 0.1222 | ±0.2444 | **+4.165** | **3.11e-05** | *** |
| Site: UCSD (vs UAB) | -0.0300 | 0.0666 | ±0.1331 | -0.450 | 0.6524 |  |
| **Site: UW (vs UAB)** | **-0.3805** | 0.0663 | ±0.1325 | **-5.742** | **9.37e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1569** | 0.0669 | ±0.1338 | **-2.346** | **0.0190** | * |
| Season: summer (vs autumn) | -0.0398 | 0.0733 | ±0.1465 | -0.544 | 0.5867 |  |
| Season: winter (vs autumn) | -0.0449 | 0.0706 | ±0.1411 | -0.637 | 0.5242 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.837** | **5.33e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.649** | **3.33e-06** | *** |
| Hypertension | +0.0917 | 0.0568 | ±0.1137 | +1.613 | 0.1067 |  |
| High cholesterol | -0.0401 | 0.0494 | ±0.0988 | -0.812 | 0.4170 |  |
| Kidney disease | -0.0660 | 0.0819 | ±0.1639 | -0.806 | 0.4203 |  |
| **Circulatory disease** | **+0.2269** | 0.0904 | ±0.1808 | **+2.510** | **0.0121** | * |
| Time < 70 (%) | -0.0031 | 0.0129 | ±0.0259 | -0.239 | 0.8111 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **1251**, R² = **0.1458**, Adj R² = **0.1361**, F-statistic = **15.07** (p = **4.08e-34**), Residual SE = **0.859** on **1236** df, AIC = **3184.2**, BIC = **3261.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2278** | 0.1902 | ±0.3805 | **+11.710** | **1.13e-31** | *** |
| Education: graduate level (vs college) | -0.0150 | 0.0502 | ±0.1003 | -0.298 | 0.7656 |  |
| **Education: high school or below (vs college)** | **+0.5095** | 0.1224 | ±0.2448 | **+4.163** | **3.14e-05** | *** |
| Site: UCSD (vs UAB) | -0.0293 | 0.0664 | ±0.1327 | -0.441 | 0.6593 |  |
| **Site: UW (vs UAB)** | **-0.3800** | 0.0664 | ±0.1328 | **-5.722** | **1.05e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1569** | 0.0669 | ±0.1339 | **-2.344** | **0.0191** | * |
| Season: summer (vs autumn) | -0.0400 | 0.0732 | ±0.1464 | -0.546 | 0.5849 |  |
| Season: winter (vs autumn) | -0.0450 | 0.0705 | ±0.1411 | -0.638 | 0.5233 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.839** | **5.27e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.648** | **3.35e-06** | *** |
| Hypertension | +0.0918 | 0.0570 | ±0.1140 | +1.610 | 0.1073 |  |
| High cholesterol | -0.0398 | 0.0493 | ±0.0985 | -0.807 | 0.4196 |  |
| Kidney disease | -0.0661 | 0.0819 | ±0.1639 | -0.806 | 0.4200 |  |
| **Circulatory disease** | **+0.2269** | 0.0904 | ±0.1808 | **+2.510** | **0.0121** | * |
| Avg. daily time < 70 (%) | -0.0022 | 0.0143 | ±0.0287 | -0.151 | 0.8797 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.1462**, Adj R² = **0.1365**, F-statistic = **15.12** (p = **3.16e-34**), Residual SE = **0.859** on **1236** df, AIC = **3183.7**, BIC = **3260.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8553** | 0.2606 | ±0.5212 | **+7.119** | **1.08e-12** | *** |
| Education: graduate level (vs college) | -0.0143 | 0.0501 | ±0.1001 | -0.286 | 0.7751 |  |
| **Education: high school or below (vs college)** | **+0.5156** | 0.1222 | ±0.2444 | **+4.220** | **2.44e-05** | *** |
| Site: UCSD (vs UAB) | -0.0301 | 0.0660 | ±0.1319 | -0.457 | 0.6480 |  |
| **Site: UW (vs UAB)** | **-0.3800** | 0.0660 | ±0.1321 | **-5.754** | **8.71e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1577** | 0.0668 | ±0.1336 | **-2.362** | **0.0182** | * |
| Season: summer (vs autumn) | -0.0421 | 0.0731 | ±0.1462 | -0.575 | 0.5650 |  |
| Season: winter (vs autumn) | -0.0462 | 0.0702 | ±0.1404 | -0.658 | 0.5107 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.847** | **5.00e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.657** | **3.21e-06** | *** |
| Hypertension | +0.0926 | 0.0567 | ±0.1134 | +1.632 | 0.1026 |  |
| High cholesterol | -0.0401 | 0.0492 | ±0.0985 | -0.813 | 0.4160 |  |
| Kidney disease | -0.0653 | 0.0817 | ±0.1634 | -0.799 | 0.4240 |  |
| **Circulatory disease** | **+0.2308** | 0.0909 | ±0.1817 | **+2.539** | **0.0111** | * |
| Time 54-250, pooled (%) | +0.0037 | 0.0020 | ±0.0040 | +1.885 | 0.0594 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.1462**, Adj R² = **0.1365**, F-statistic = **15.11** (p = **3.21e-34**), Residual SE = **0.859** on **1236** df, AIC = **3183.7**, BIC = **3260.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8580** | 0.2603 | ±0.5206 | **+7.138** | **9.48e-13** | *** |
| Education: graduate level (vs college) | -0.0143 | 0.0501 | ±0.1001 | -0.286 | 0.7751 |  |
| **Education: high school or below (vs college)** | **+0.5156** | 0.1222 | ±0.2444 | **+4.219** | **2.45e-05** | *** |
| Site: UCSD (vs UAB) | -0.0299 | 0.0659 | ±0.1319 | -0.453 | 0.6505 |  |
| **Site: UW (vs UAB)** | **-0.3799** | 0.0660 | ±0.1321 | **-5.753** | **8.78e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1577** | 0.0668 | ±0.1336 | **-2.361** | **0.0182** | * |
| Season: summer (vs autumn) | -0.0421 | 0.0731 | ±0.1462 | -0.575 | 0.5651 |  |
| Season: winter (vs autumn) | -0.0462 | 0.0702 | ±0.1404 | -0.658 | 0.5106 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.846** | **5.05e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.659** | **3.18e-06** | *** |
| Hypertension | +0.0925 | 0.0567 | ±0.1134 | +1.632 | 0.1026 |  |
| High cholesterol | -0.0400 | 0.0492 | ±0.0985 | -0.812 | 0.4170 |  |
| Kidney disease | -0.0655 | 0.0817 | ±0.1635 | -0.801 | 0.4232 |  |
| **Circulatory disease** | **+0.2307** | 0.0909 | ±0.1818 | **+2.538** | **0.0111** | * |
| Avg. daily time 54-250 (%) | +0.0037 | 0.0020 | ±0.0039 | +1.891 | 0.0586 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.1472**, Adj R² = **0.1375**, F-statistic = **15.23** (p = **1.64e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.3**, BIC = **3259.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2282** | 0.1902 | ±0.3803 | **+11.718** | **1.03e-31** | *** |
| Education: graduate level (vs college) | -0.0116 | 0.0500 | ±0.1000 | -0.231 | 0.8171 |  |
| **Education: high school or below (vs college)** | **+0.5126** | 0.1212 | ±0.2424 | **+4.229** | **2.34e-05** | *** |
| Site: UCSD (vs UAB) | -0.0320 | 0.0658 | ±0.1317 | -0.486 | 0.6273 |  |
| **Site: UW (vs UAB)** | **-0.3755** | 0.0660 | ±0.1321 | **-5.687** | **1.29e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1611** | 0.0670 | ±0.1340 | **-2.405** | **0.0162** | * |
| Season: summer (vs autumn) | -0.0469 | 0.0732 | ±0.1465 | -0.640 | 0.5221 |  |
| Season: winter (vs autumn) | -0.0504 | 0.0701 | ±0.1402 | -0.719 | 0.4719 |  |
| **Age (years)** | **-0.0131** | 0.0023 | ±0.0045 | **-5.805** | **6.42e-09** | *** |
| **BMI (kg/m2)** | **+0.0188** | 0.0040 | ±0.0080 | **+4.712** | **2.46e-06** | *** |
| Hypertension | +0.0979 | 0.0571 | ±0.1143 | +1.714 | 0.0866 | . |
| High cholesterol | -0.0351 | 0.0494 | ±0.0988 | -0.710 | 0.4775 |  |
| Kidney disease | -0.0569 | 0.0816 | ±0.1631 | -0.698 | 0.4854 |  |
| **Circulatory disease** | **+0.2285** | 0.0903 | ±0.1805 | **+2.532** | **0.0114** | * |
| Time 181-250, pooled (%) | -0.0056 | 0.0042 | ±0.0084 | -1.348 | 0.1776 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1251**, R² = **0.1472**, Adj R² = **0.1375**, F-statistic = **15.24** (p = **1.60e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.2**, BIC = **3259.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2280** | 0.1901 | ±0.3803 | **+11.718** | **1.03e-31** | *** |
| Education: graduate level (vs college) | -0.0114 | 0.0500 | ±0.1001 | -0.229 | 0.8190 |  |
| **Education: high school or below (vs college)** | **+0.5121** | 0.1212 | ±0.2424 | **+4.225** | **2.39e-05** | *** |
| Site: UCSD (vs UAB) | -0.0324 | 0.0658 | ±0.1317 | -0.492 | 0.6226 |  |
| **Site: UW (vs UAB)** | **-0.3759** | 0.0660 | ±0.1321 | **-5.693** | **1.25e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1607** | 0.0670 | ±0.1339 | **-2.400** | **0.0164** | * |
| Season: summer (vs autumn) | -0.0468 | 0.0732 | ±0.1464 | -0.640 | 0.5223 |  |
| Season: winter (vs autumn) | -0.0505 | 0.0701 | ±0.1402 | -0.720 | 0.4718 |  |
| **Age (years)** | **-0.0131** | 0.0023 | ±0.0045 | **-5.808** | **6.31e-09** | *** |
| **BMI (kg/m2)** | **+0.0189** | 0.0040 | ±0.0080 | **+4.714** | **2.43e-06** | *** |
| Hypertension | +0.0979 | 0.0572 | ±0.1143 | +1.713 | 0.0867 | . |
| High cholesterol | -0.0350 | 0.0494 | ±0.0988 | -0.709 | 0.4785 |  |
| Kidney disease | -0.0566 | 0.0815 | ±0.1631 | -0.694 | 0.4876 |  |
| **Circulatory disease** | **+0.2286** | 0.0903 | ±0.1805 | **+2.533** | **0.0113** | * |
| Avg. daily time 181-250 (%) | -0.0056 | 0.0042 | ±0.0083 | -1.357 | 0.1749 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **1251**, R² = **0.1470**, Adj R² = **0.1374**, F-statistic = **15.22** (p = **1.75e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.4**, BIC = **3259.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2301** | 0.1902 | ±0.3804 | **+11.726** | **9.42e-32** | *** |
| Education: graduate level (vs college) | -0.0123 | 0.0500 | ±0.1001 | -0.245 | 0.8062 |  |
| **Education: high school or below (vs college)** | **+0.5173** | 0.1216 | ±0.2433 | **+4.253** | **2.11e-05** | *** |
| Site: UCSD (vs UAB) | -0.0317 | 0.0659 | ±0.1318 | -0.481 | 0.6304 |  |
| **Site: UW (vs UAB)** | **-0.3772** | 0.0659 | ±0.1319 | **-5.720** | **1.07e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1603** | 0.0669 | ±0.1337 | **-2.398** | **0.0165** | * |
| Season: summer (vs autumn) | -0.0466 | 0.0732 | ±0.1464 | -0.637 | 0.5242 |  |
| Season: winter (vs autumn) | -0.0494 | 0.0701 | ±0.1401 | -0.705 | 0.4806 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.824** | **5.76e-09** | *** |
| **BMI (kg/m2)** | **+0.0188** | 0.0040 | ±0.0080 | **+4.699** | **2.61e-06** | *** |
| Hypertension | +0.0965 | 0.0569 | ±0.1138 | +1.696 | 0.0899 | . |
| High cholesterol | -0.0370 | 0.0493 | ±0.0985 | -0.750 | 0.4530 |  |
| Kidney disease | -0.0594 | 0.0813 | ±0.1627 | -0.731 | 0.4651 |  |
| **Circulatory disease** | **+0.2318** | 0.0906 | ±0.1813 | **+2.557** | **0.0105** | * |
| Time > 180 (%) | -0.0037 | 0.0022 | ±0.0044 | -1.675 | 0.0940 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.1471**, Adj R² = **0.1374**, F-statistic = **15.22** (p = **1.74e-34**), Residual SE = **0.858** on **1236** df, AIC = **3182.4**, BIC = **3259.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2296** | 0.1901 | ±0.3803 | **+11.726** | **9.40e-32** | *** |
| Education: graduate level (vs college) | -0.0122 | 0.0500 | ±0.1001 | -0.243 | 0.8077 |  |
| **Education: high school or below (vs college)** | **+0.5169** | 0.1216 | ±0.2432 | **+4.251** | **2.13e-05** | *** |
| Site: UCSD (vs UAB) | -0.0320 | 0.0659 | ±0.1318 | -0.486 | 0.6271 |  |
| **Site: UW (vs UAB)** | **-0.3774** | 0.0660 | ±0.1319 | **-5.722** | **1.05e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1601** | 0.0668 | ±0.1337 | **-2.395** | **0.0166** | * |
| Season: summer (vs autumn) | -0.0466 | 0.0732 | ±0.1464 | -0.637 | 0.5243 |  |
| Season: winter (vs autumn) | -0.0495 | 0.0701 | ±0.1402 | -0.707 | 0.4798 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.825** | **5.71e-09** | *** |
| **BMI (kg/m2)** | **+0.0188** | 0.0040 | ±0.0080 | **+4.703** | **2.57e-06** | *** |
| Hypertension | +0.0965 | 0.0569 | ±0.1138 | +1.695 | 0.0900 | . |
| High cholesterol | -0.0369 | 0.0492 | ±0.0985 | -0.750 | 0.4534 |  |
| Kidney disease | -0.0593 | 0.0813 | ±0.1627 | -0.729 | 0.4659 |  |
| **Circulatory disease** | **+0.2319** | 0.0906 | ±0.1813 | **+2.558** | **0.0105** | * |
| Avg. daily time > 180 (%) | -0.0037 | 0.0022 | ±0.0044 | -1.682 | 0.0926 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.1463**, Adj R² = **0.1367**, F-statistic = **15.13** (p = **2.84e-34**), Residual SE = **0.859** on **1236** df, AIC = **3183.5**, BIC = **3260.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2234** | 0.1900 | ±0.3801 | **+11.701** | **1.27e-31** | *** |
| Education: graduate level (vs college) | -0.0144 | 0.0501 | ±0.1001 | -0.287 | 0.7742 |  |
| **Education: high school or below (vs college)** | **+0.5146** | 0.1217 | ±0.2435 | **+4.227** | **2.37e-05** | *** |
| Site: UCSD (vs UAB) | -0.0299 | 0.0658 | ±0.1317 | -0.455 | 0.6495 |  |
| **Site: UW (vs UAB)** | **-0.3783** | 0.0660 | ±0.1320 | **-5.733** | **9.85e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1570** | 0.0668 | ±0.1335 | **-2.351** | **0.0187** | * |
| Season: summer (vs autumn) | -0.0436 | 0.0733 | ±0.1466 | -0.595 | 0.5519 |  |
| Season: winter (vs autumn) | -0.0461 | 0.0701 | ±0.1403 | -0.658 | 0.5105 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.840** | **5.21e-09** | *** |
| **BMI (kg/m2)** | **+0.0189** | 0.0040 | ±0.0081 | **+4.697** | **2.64e-06** | *** |
| Hypertension | +0.0936 | 0.0568 | ±0.1135 | +1.649 | 0.0992 | . |
| High cholesterol | -0.0371 | 0.0493 | ±0.0986 | -0.751 | 0.4524 |  |
| Kidney disease | -0.0662 | 0.0817 | ±0.1633 | -0.811 | 0.4176 |  |
| **Circulatory disease** | **+0.2283** | 0.0905 | ±0.1810 | **+2.523** | **0.0116** | * |
| Nocturnal time > 180 (%) | -0.0026 | 0.0022 | ±0.0044 | -1.170 | 0.2420 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.1464**, Adj R² = **0.1367**, F-statistic = **15.14** (p = **2.81e-34**), Residual SE = **0.859** on **1236** df, AIC = **3183.4**, BIC = **3260.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2411** | 0.1921 | ±0.3842 | **+11.667** | **1.89e-31** | *** |
| Education: graduate level (vs college) | -0.0150 | 0.0501 | ±0.1001 | -0.299 | 0.7649 |  |
| **Education: high school or below (vs college)** | **+0.5104** | 0.1213 | ±0.2427 | **+4.206** | **2.60e-05** | *** |
| Site: UCSD (vs UAB) | -0.0297 | 0.0659 | ±0.1317 | -0.451 | 0.6522 |  |
| **Site: UW (vs UAB)** | **-0.3781** | 0.0662 | ±0.1323 | **-5.715** | **1.10e-08** | *** |
| **Season: spring (vs autumn)** | **-0.1603** | 0.0670 | ±0.1340 | **-2.393** | **0.0167** | * |
| Season: summer (vs autumn) | -0.0427 | 0.0732 | ±0.1464 | -0.584 | 0.5594 |  |
| Season: winter (vs autumn) | -0.0483 | 0.0703 | ±0.1406 | -0.687 | 0.4924 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.825** | **5.71e-09** | *** |
| **BMI (kg/m2)** | **+0.0184** | 0.0040 | ±0.0080 | **+4.580** | **4.65e-06** | *** |
| Hypertension | +0.0955 | 0.0571 | ±0.1143 | +1.672 | 0.0946 | . |
| High cholesterol | -0.0384 | 0.0493 | ±0.0985 | -0.779 | 0.4358 |  |
| Kidney disease | -0.0647 | 0.0817 | ±0.1633 | -0.793 | 0.4281 |  |
| **Circulatory disease** | **+0.2265** | 0.0903 | ±0.1806 | **+2.507** | **0.0122** | * |
| Any reading > 250 during wear (0/1) | -0.0559 | 0.0606 | ±0.1212 | -0.923 | 0.3562 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.1461**, Adj R² = **0.1365**, F-statistic = **15.11** (p = **3.25e-34**), Residual SE = **0.859** on **1236** df, AIC = **3183.8**, BIC = **3260.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2282** | 0.1903 | ±0.3806 | **+11.708** | **1.16e-31** | *** |
| Education: graduate level (vs college) | -0.0142 | 0.0501 | ±0.1001 | -0.284 | 0.7761 |  |
| **Education: high school or below (vs college)** | **+0.5157** | 0.1223 | ±0.2445 | **+4.218** | **2.47e-05** | *** |
| Site: UCSD (vs UAB) | -0.0294 | 0.0659 | ±0.1318 | -0.446 | 0.6558 |  |
| **Site: UW (vs UAB)** | **-0.3795** | 0.0660 | ±0.1320 | **-5.748** | **9.04e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1576** | 0.0668 | ±0.1336 | **-2.360** | **0.0183** | * |
| Season: summer (vs autumn) | -0.0421 | 0.0731 | ±0.1463 | -0.575 | 0.5650 |  |
| Season: winter (vs autumn) | -0.0462 | 0.0702 | ±0.1404 | -0.658 | 0.5104 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.846** | **5.04e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.658** | **3.20e-06** | *** |
| Hypertension | +0.0927 | 0.0567 | ±0.1134 | +1.635 | 0.1022 |  |
| High cholesterol | -0.0397 | 0.0492 | ±0.0985 | -0.807 | 0.4196 |  |
| Kidney disease | -0.0655 | 0.0817 | ±0.1635 | -0.801 | 0.4231 |  |
| **Circulatory disease** | **+0.2306** | 0.0909 | ±0.1818 | **+2.537** | **0.0112** | * |
| Time > 250 (%) | -0.0035 | 0.0019 | ±0.0038 | -1.853 | 0.0639 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,251)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.1461**, Adj R² = **0.1365**, F-statistic = **15.11** (p = **3.28e-34**), Residual SE = **0.859** on **1236** df, AIC = **3183.8**, BIC = **3260.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2279** | 0.1903 | ±0.3806 | **+11.708** | **1.15e-31** | *** |
| Education: graduate level (vs college) | -0.0142 | 0.0501 | ±0.1001 | -0.284 | 0.7762 |  |
| **Education: high school or below (vs college)** | **+0.5157** | 0.1223 | ±0.2446 | **+4.217** | **2.47e-05** | *** |
| Site: UCSD (vs UAB) | -0.0294 | 0.0659 | ±0.1318 | -0.446 | 0.6557 |  |
| **Site: UW (vs UAB)** | **-0.3794** | 0.0660 | ±0.1320 | **-5.748** | **9.06e-09** | *** |
| **Season: spring (vs autumn)** | **-0.1576** | 0.0668 | ±0.1336 | **-2.360** | **0.0183** | * |
| Season: summer (vs autumn) | -0.0421 | 0.0731 | ±0.1463 | -0.576 | 0.5649 |  |
| Season: winter (vs autumn) | -0.0463 | 0.0702 | ±0.1404 | -0.659 | 0.5097 |  |
| **Age (years)** | **-0.0132** | 0.0023 | ±0.0045 | **-5.845** | **5.05e-09** | *** |
| **BMI (kg/m2)** | **+0.0186** | 0.0040 | ±0.0080 | **+4.659** | **3.17e-06** | *** |
| Hypertension | +0.0927 | 0.0567 | ±0.1134 | +1.635 | 0.1021 |  |
| High cholesterol | -0.0398 | 0.0492 | ±0.0985 | -0.807 | 0.4194 |  |
| Kidney disease | -0.0656 | 0.0818 | ±0.1635 | -0.802 | 0.4226 |  |
| **Circulatory disease** | **+0.2306** | 0.0909 | ±0.1818 | **+2.537** | **0.0112** | * |
| Avg. daily time > 250 (%) | -0.0036 | 0.0019 | ±0.0038 | -1.864 | 0.0623 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 1,251; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **1251**, R² = **0.3174**, Adj R² = **0.3103**, F-statistic = **44.25** (p = **3.88e-93**), Residual SE = **1.890** on **1237** df, AIC = **5156.2**, BIC = **5228.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8847** | 0.4341 | ±0.8683 | **+55.015** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1589 | 0.1132 | ±0.2265 | -1.403 | 0.1606 |  |
| Education: high school or below (vs college) | +0.1216 | 0.2214 | ±0.4428 | +0.549 | 0.5829 |  |
| Site: UCSD (vs UAB) | -0.0636 | 0.1418 | ±0.2837 | -0.448 | 0.6538 |  |
| **Site: UW (vs UAB)** | **-0.8944** | 0.1332 | ±0.2663 | **-6.716** | **1.86e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4696** | 0.1503 | ±0.3007 | **-3.124** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9790** | 0.1785 | ±0.3570 | **+11.087** | **1.45e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3873** | 0.1499 | ±0.2998 | **-9.254** | **2.17e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.313** | **0.0207** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0166 | +0.635 | 0.5254 |  |
| Hypertension | +0.2067 | 0.1216 | ±0.2432 | +1.699 | 0.0892 | . |
| High cholesterol | -0.0626 | 0.1138 | ±0.2277 | -0.549 | 0.5827 |  |
| **Kidney disease** | **+0.4715** | 0.2080 | ±0.4160 | **+2.267** | **0.0234** | * |
| Circulatory disease | +0.2936 | 0.1740 | ±0.3480 | +1.687 | 0.0916 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **1251**, R² = **0.3175**, Adj R² = **0.3097**, F-statistic = **41.06** (p = **2.60e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.2**, BIC = **5235.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7931** | 0.7532 | ±1.5064 | **+31.589** | **5.31e-219** | *** |
| Education: graduate level (vs college) | -0.1591 | 0.1134 | ±0.2269 | -1.402 | 0.1608 |  |
| Education: high school or below (vs college) | +0.1187 | 0.2239 | ±0.4479 | +0.530 | 0.5960 |  |
| Site: UCSD (vs UAB) | -0.0640 | 0.1419 | ±0.2839 | -0.451 | 0.6520 |  |
| **Site: UW (vs UAB)** | **-0.8951** | 0.1334 | ±0.2669 | **-6.708** | **1.98e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4673** | 0.1517 | ±0.3034 | **-3.081** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.9797** | 0.1787 | ±0.3574 | **+11.079** | **1.58e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3863** | 0.1503 | ±0.3005 | **-9.226** | **2.81e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0103 | **+2.278** | **0.0227** | * |
| BMI (kg/m2) | +0.0052 | 0.0083 | ±0.0166 | +0.620 | 0.5351 |  |
| Hypertension | +0.2056 | 0.1221 | ±0.2442 | +1.684 | 0.0922 | . |
| High cholesterol | -0.0645 | 0.1149 | ±0.2298 | -0.562 | 0.5744 |  |
| **Kidney disease** | **+0.4716** | 0.2081 | ±0.4162 | **+2.266** | **0.0235** | * |
| Circulatory disease | +0.2923 | 0.1745 | ±0.3491 | +1.675 | 0.0939 | . |
| HbA1c (%) | +0.0178 | 0.1196 | ±0.2392 | +0.149 | 0.8816 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **1251**, R² = **0.3174**, Adj R² = **0.3097**, F-statistic = **41.06** (p = **2.63e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.2**, BIC = **5235.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8701** | 0.5393 | ±1.0786 | **+44.262** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1592 | 0.1135 | ±0.2269 | -1.403 | 0.1606 |  |
| Education: high school or below (vs college) | +0.1208 | 0.2228 | ±0.4456 | +0.542 | 0.5876 |  |
| Site: UCSD (vs UAB) | -0.0635 | 0.1419 | ±0.2838 | -0.447 | 0.6546 |  |
| **Site: UW (vs UAB)** | **-0.8948** | 0.1339 | ±0.2679 | **-6.681** | **2.38e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4694** | 0.1508 | ±0.3015 | **-3.113** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9794** | 0.1785 | ±0.3570 | **+11.090** | **1.41e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3869** | 0.1502 | ±0.3005 | **-9.232** | **2.66e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.307** | **0.0210** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0167 | +0.632 | 0.5272 |  |
| Hypertension | +0.2062 | 0.1220 | ±0.2440 | +1.691 | 0.0909 | . |
| High cholesterol | -0.0628 | 0.1142 | ±0.2283 | -0.550 | 0.5822 |  |
| **Kidney disease** | **+0.4711** | 0.2082 | ±0.4164 | **+2.262** | **0.0237** | * |
| Circulatory disease | +0.2932 | 0.1747 | ±0.3494 | +1.678 | 0.0933 | . |
| Mean glucose (mg/dL) | +0.0001 | 0.0029 | ±0.0058 | +0.046 | 0.9630 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **1251**, R² = **0.3174**, Adj R² = **0.3097**, F-statistic = **41.06** (p = **2.63e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.2**, BIC = **5235.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8516** | 0.8393 | ±1.6785 | **+28.420** | **1.15e-177** | *** |
| Education: graduate level (vs college) | -0.1592 | 0.1135 | ±0.2269 | -1.403 | 0.1606 |  |
| Education: high school or below (vs college) | +0.1208 | 0.2228 | ±0.4456 | +0.542 | 0.5876 |  |
| Site: UCSD (vs UAB) | -0.0635 | 0.1419 | ±0.2838 | -0.447 | 0.6546 |  |
| **Site: UW (vs UAB)** | **-0.8948** | 0.1339 | ±0.2679 | **-6.681** | **2.38e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4694** | 0.1508 | ±0.3015 | **-3.113** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9794** | 0.1785 | ±0.3570 | **+11.090** | **1.41e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3869** | 0.1502 | ±0.3005 | **-9.232** | **2.66e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.307** | **0.0210** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0167 | +0.632 | 0.5272 |  |
| Hypertension | +0.2062 | 0.1220 | ±0.2440 | +1.691 | 0.0909 | . |
| High cholesterol | -0.0628 | 0.1142 | ±0.2283 | -0.550 | 0.5822 |  |
| **Kidney disease** | **+0.4711** | 0.2082 | ±0.4164 | **+2.262** | **0.0237** | * |
| Circulatory disease | +0.2932 | 0.1747 | ±0.3494 | +1.678 | 0.0933 | . |
| GMI (%) | +0.0056 | 0.1204 | ±0.2408 | +0.046 | 0.9630 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **1251**, R² = **0.3175**, Adj R² = **0.3098**, F-statistic = **41.07** (p = **2.52e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.1**, BIC = **5235.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9726** | 0.5284 | ±1.0568 | **+45.368** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1576 | 0.1134 | ±0.2267 | -1.390 | 0.1645 |  |
| Education: high school or below (vs college) | +0.1264 | 0.2229 | ±0.4459 | +0.567 | 0.5709 |  |
| Site: UCSD (vs UAB) | -0.0631 | 0.1421 | ±0.2842 | -0.444 | 0.6568 |  |
| **Site: UW (vs UAB)** | **-0.8922** | 0.1338 | ±0.2677 | **-6.667** | **2.61e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4698** | 0.1504 | ±0.3009 | **-3.123** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9768** | 0.1786 | ±0.3572 | **+11.069** | **1.78e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3884** | 0.1502 | ±0.3004 | **-9.245** | **2.35e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.307** | **0.0211** | * |
| BMI (kg/m2) | +0.0056 | 0.0084 | ±0.0168 | +0.668 | 0.5041 |  |
| Hypertension | +0.2091 | 0.1218 | ±0.2436 | +1.716 | 0.0861 | . |
| High cholesterol | -0.0603 | 0.1143 | ±0.2287 | -0.528 | 0.5978 |  |
| **Kidney disease** | **+0.4719** | 0.2082 | ±0.4165 | **+2.266** | **0.0234** | * |
| Circulatory disease | +0.2951 | 0.1744 | ±0.3488 | +1.692 | 0.0906 | . |
| Nocturnal mean 00-06h (mg/dL) | -0.0008 | 0.0028 | ±0.0056 | -0.297 | 0.7667 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.3176**, Adj R² = **0.3099**, F-statistic = **41.09** (p = **2.30e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.9**, BIC = **5234.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9667** | 0.4661 | ±0.9322 | **+51.418** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1582 | 0.1134 | ±0.2268 | -1.395 | 0.1630 |  |
| Education: high school or below (vs college) | +0.1230 | 0.2214 | ±0.4429 | +0.555 | 0.5786 |  |
| Site: UCSD (vs UAB) | -0.0677 | 0.1418 | ±0.2836 | -0.478 | 0.6329 |  |
| **Site: UW (vs UAB)** | **-0.8922** | 0.1337 | ±0.2673 | **-6.675** | **2.47e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4724** | 0.1506 | ±0.3011 | **-3.137** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9762** | 0.1786 | ±0.3573 | **+11.063** | **1.89e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3898** | 0.1502 | ±0.3003 | **-9.256** | **2.12e-20** | *** |
| **Age (years)** | **+0.0119** | 0.0051 | ±0.0101 | **+2.351** | **0.0187** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0167 | +0.640 | 0.5223 |  |
| Hypertension | +0.2122 | 0.1221 | ±0.2442 | +1.738 | 0.0822 | . |
| High cholesterol | -0.0626 | 0.1140 | ±0.2279 | -0.550 | 0.5825 |  |
| **Kidney disease** | **+0.4805** | 0.2097 | ±0.4194 | **+2.292** | **0.0219** | * |
| Circulatory disease | +0.2974 | 0.1745 | ±0.3490 | +1.704 | 0.0883 | . |
| Glucose SD, pooled (mg/dL) | -0.0044 | 0.0084 | ±0.0169 | -0.520 | 0.6030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.3176**, Adj R² = **0.3099**, F-statistic = **41.10** (p = **2.21e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.8**, BIC = **5234.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9704** | 0.4630 | ±0.9260 | **+51.770** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1576 | 0.1134 | ±0.2268 | -1.390 | 0.1645 |  |
| Education: high school or below (vs college) | +0.1234 | 0.2214 | ±0.4429 | +0.557 | 0.5774 |  |
| Site: UCSD (vs UAB) | -0.0678 | 0.1418 | ±0.2836 | -0.478 | 0.6327 |  |
| **Site: UW (vs UAB)** | **-0.8915** | 0.1337 | ±0.2674 | **-6.667** | **2.62e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4734** | 0.1506 | ±0.3012 | **-3.143** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9749** | 0.1788 | ±0.3576 | **+11.047** | **2.28e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3910** | 0.1501 | ±0.3003 | **-9.265** | **1.96e-20** | *** |
| **Age (years)** | **+0.0120** | 0.0051 | ±0.0101 | **+2.361** | **0.0182** | * |
| BMI (kg/m2) | +0.0054 | 0.0083 | ±0.0167 | +0.647 | 0.5173 |  |
| Hypertension | +0.2127 | 0.1221 | ±0.2442 | +1.742 | 0.0815 | . |
| High cholesterol | -0.0624 | 0.1139 | ±0.2279 | -0.548 | 0.5839 |  |
| **Kidney disease** | **+0.4822** | 0.2096 | ±0.4192 | **+2.300** | **0.0214** | * |
| Circulatory disease | +0.2977 | 0.1744 | ±0.3488 | +1.707 | 0.0879 | . |
| Avg. daily SD (mg/dL) | -0.0053 | 0.0089 | ±0.0178 | -0.592 | 0.5540 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **1251**, R² = **0.3177**, Adj R² = **0.3099**, F-statistic = **41.10** (p = **2.15e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.8**, BIC = **5234.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0300** | 0.4960 | ±0.9920 | **+48.445** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1609 | 0.1134 | ±0.2268 | -1.419 | 0.1558 |  |
| Education: high school or below (vs college) | +0.1168 | 0.2213 | ±0.4426 | +0.528 | 0.5975 |  |
| Site: UCSD (vs UAB) | -0.0696 | 0.1417 | ±0.2835 | -0.491 | 0.6235 |  |
| **Site: UW (vs UAB)** | **-0.8952** | 0.1332 | ±0.2663 | **-6.723** | **1.79e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4717** | 0.1503 | ±0.3007 | **-3.137** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9786** | 0.1785 | ±0.3570 | **+11.084** | **1.50e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3870** | 0.1499 | ±0.2998 | **-9.251** | **2.22e-20** | *** |
| **Age (years)** | **+0.0120** | 0.0051 | ±0.0101 | **+2.360** | **0.0183** | * |
| BMI (kg/m2) | +0.0052 | 0.0083 | ±0.0167 | +0.623 | 0.5330 |  |
| Hypertension | +0.2105 | 0.1218 | ±0.2436 | +1.728 | 0.0839 | . |
| High cholesterol | -0.0656 | 0.1139 | ±0.2278 | -0.576 | 0.5646 |  |
| **Kidney disease** | **+0.4806** | 0.2096 | ±0.4192 | **+2.293** | **0.0218** | * |
| Circulatory disease | +0.2955 | 0.1741 | ±0.3483 | +1.697 | 0.0897 | . |
| CV (%) | -0.0085 | 0.0135 | ±0.0271 | -0.630 | 0.5287 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1251**, R² = **0.3182**, Adj R² = **0.3105**, F-statistic = **41.21** (p = **1.32e-92**), Residual SE = **1.889** on **1236** df, AIC = **5156.8**, BIC = **5233.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5645** | 0.5003 | ±1.0006 | **+47.099** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1631 | 0.1134 | ±0.2268 | -1.439 | 0.1503 |  |
| Education: high school or below (vs college) | +0.1179 | 0.2207 | ±0.4414 | +0.534 | 0.5934 |  |
| Site: UCSD (vs UAB) | -0.0734 | 0.1417 | ±0.2833 | -0.518 | 0.6042 |  |
| **Site: UW (vs UAB)** | **-0.8930** | 0.1331 | ±0.2663 | **-6.707** | **1.99e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4710** | 0.1501 | ±0.3002 | **-3.138** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9774** | 0.1783 | ±0.3567 | **+11.087** | **1.45e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3845** | 0.1498 | ±0.2996 | **-9.244** | **2.38e-20** | *** |
| **Age (years)** | **+0.0121** | 0.0051 | ±0.0101 | **+2.392** | **0.0167** | * |
| BMI (kg/m2) | +0.0051 | 0.0083 | ±0.0166 | +0.614 | 0.5391 |  |
| Hypertension | +0.2144 | 0.1217 | ±0.2435 | +1.761 | 0.0782 | . |
| High cholesterol | -0.0662 | 0.1139 | ±0.2278 | -0.581 | 0.5613 |  |
| **Kidney disease** | **+0.4840** | 0.2093 | ±0.4186 | **+2.312** | **0.0208** | * |
| Circulatory disease | +0.2960 | 0.1740 | ±0.3480 | +1.701 | 0.0889 | . |
| Mean / SD ratio | +0.0518 | 0.0422 | ±0.0843 | +1.230 | 0.2187 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.3181**, Adj R² = **0.3103**, F-statistic = **41.18** (p = **1.51e-92**), Residual SE = **1.889** on **1236** df, AIC = **5157.0**, BIC = **5234.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.5960** | 0.5022 | ±1.0044 | **+46.984** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1608 | 0.1134 | ±0.2269 | -1.417 | 0.1564 |  |
| Education: high school or below (vs college) | +0.1212 | 0.2209 | ±0.4419 | +0.548 | 0.5835 |  |
| Site: UCSD (vs UAB) | -0.0703 | 0.1416 | ±0.2832 | -0.497 | 0.6194 |  |
| **Site: UW (vs UAB)** | **-0.8919** | 0.1332 | ±0.2665 | **-6.694** | **2.17e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4715** | 0.1502 | ±0.3005 | **-3.138** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9746** | 0.1785 | ±0.3570 | **+11.063** | **1.89e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3864** | 0.1498 | ±0.2996 | **-9.256** | **2.12e-20** | *** |
| **Age (years)** | **+0.0122** | 0.0051 | ±0.0101 | **+2.404** | **0.0162** | * |
| BMI (kg/m2) | +0.0054 | 0.0083 | ±0.0167 | +0.646 | 0.5181 |  |
| Hypertension | +0.2118 | 0.1217 | ±0.2433 | +1.741 | 0.0818 | . |
| High cholesterol | -0.0657 | 0.1139 | ±0.2278 | -0.577 | 0.5639 |  |
| **Kidney disease** | **+0.4857** | 0.2091 | ±0.4182 | **+2.323** | **0.0202** | * |
| Circulatory disease | +0.2947 | 0.1739 | ±0.3478 | +1.695 | 0.0901 | . |
| Avg. daily mean/SD | +0.0387 | 0.0353 | ±0.0706 | +1.096 | 0.2731 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1251**, R² = **0.3175**, Adj R² = **0.3097**, F-statistic = **41.06** (p = **2.58e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.1**, BIC = **5235.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8291** | 0.5119 | ±1.0239 | **+46.548** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1586 | 0.1133 | ±0.2266 | -1.400 | 0.1616 |  |
| Education: high school or below (vs college) | +0.1206 | 0.2218 | ±0.4435 | +0.544 | 0.5864 |  |
| Site: UCSD (vs UAB) | -0.0616 | 0.1423 | ±0.2846 | -0.433 | 0.6653 |  |
| **Site: UW (vs UAB)** | **-0.8924** | 0.1338 | ±0.2676 | **-6.670** | **2.55e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4690** | 0.1506 | ±0.3013 | **-3.113** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9800** | 0.1790 | ±0.3580 | **+11.062** | **1.92e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3864** | 0.1502 | ±0.3003 | **-9.233** | **2.62e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.316** | **0.0205** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0167 | +0.631 | 0.5279 |  |
| Hypertension | +0.2068 | 0.1217 | ±0.2435 | +1.699 | 0.0894 | . |
| High cholesterol | -0.0614 | 0.1139 | ±0.2278 | -0.539 | 0.5898 |  |
| **Kidney disease** | **+0.4703** | 0.2086 | ±0.4171 | **+2.255** | **0.0241** | * |
| Circulatory disease | +0.2932 | 0.1743 | ±0.3485 | +1.682 | 0.0925 | . |
| MAG (mg/dL/h) | +0.0014 | 0.0071 | ±0.0142 | +0.191 | 0.8484 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **1251**, R² = **0.3178**, Adj R² = **0.3100**, F-statistic = **41.12** (p = **1.97e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.6**, BIC = **5234.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0365** | 0.4811 | ±0.9621 | **+49.967** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1570 | 0.1135 | ±0.2269 | -1.384 | 0.1665 |  |
| Education: high school or below (vs college) | +0.1247 | 0.2215 | ±0.4430 | +0.563 | 0.5735 |  |
| Site: UCSD (vs UAB) | -0.0694 | 0.1419 | ±0.2837 | -0.489 | 0.6247 |  |
| **Site: UW (vs UAB)** | **-0.8925** | 0.1335 | ±0.2669 | **-6.688** | **2.26e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4736** | 0.1505 | ±0.3010 | **-3.146** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9736** | 0.1788 | ±0.3577 | **+11.035** | **2.58e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3915** | 0.1502 | ±0.3004 | **-9.265** | **1.95e-20** | *** |
| **Age (years)** | **+0.0120** | 0.0051 | ±0.0101 | **+2.363** | **0.0181** | * |
| BMI (kg/m2) | +0.0050 | 0.0083 | ±0.0167 | +0.606 | 0.5443 |  |
| Hypertension | +0.2122 | 0.1220 | ±0.2439 | +1.740 | 0.0819 | . |
| High cholesterol | -0.0644 | 0.1139 | ±0.2279 | -0.565 | 0.5720 |  |
| **Kidney disease** | **+0.4826** | 0.2097 | ±0.4193 | **+2.302** | **0.0213** | * |
| Circulatory disease | +0.2986 | 0.1742 | ±0.3484 | +1.714 | 0.0865 | . |
| Avg. daily range (mg/dL) | -0.0016 | 0.0021 | ±0.0042 | -0.763 | 0.4455 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **1251**, R² = **0.3175**, Adj R² = **0.3097**, F-statistic = **41.06** (p = **2.59e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.1**, BIC = **5235.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9005** | 0.4450 | ±0.8900 | **+53.710** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1589 | 0.1134 | ±0.2267 | -1.402 | 0.1611 |  |
| Education: high school or below (vs college) | +0.1215 | 0.2216 | ±0.4431 | +0.549 | 0.5833 |  |
| Site: UCSD (vs UAB) | -0.0649 | 0.1418 | ±0.2837 | -0.458 | 0.6472 |  |
| **Site: UW (vs UAB)** | **-0.8941** | 0.1335 | ±0.2669 | **-6.699** | **2.09e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4683** | 0.1504 | ±0.3008 | **-3.114** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9801** | 0.1791 | ±0.3581 | **+11.059** | **1.99e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3867** | 0.1499 | ±0.2998 | **-9.250** | **2.25e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.313** | **0.0207** | * |
| BMI (kg/m2) | +0.0054 | 0.0083 | ±0.0167 | +0.645 | 0.5187 |  |
| Hypertension | +0.2071 | 0.1218 | ±0.2437 | +1.700 | 0.0892 | . |
| High cholesterol | -0.0621 | 0.1140 | ±0.2280 | -0.545 | 0.5858 |  |
| **Kidney disease** | **+0.4717** | 0.2082 | ±0.4165 | **+2.265** | **0.0235** | * |
| Circulatory disease | +0.2948 | 0.1745 | ±0.3489 | +1.690 | 0.0911 | . |
| SD of daily means (mg/dL) | -0.0030 | 0.0179 | ±0.0358 | -0.167 | 0.8677 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **1251**, R² = **0.3179**, Adj R² = **0.3101**, F-statistic = **41.14** (p = **1.80e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.4**, BIC = **5234.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.4046** | 0.7427 | ±1.4853 | **+32.861** | **7.83e-237** | *** |
| Education: graduate level (vs college) | -0.1612 | 0.1134 | ±0.2269 | -1.421 | 0.1552 |  |
| Education: high school or below (vs college) | +0.1146 | 0.2220 | ±0.4439 | +0.516 | 0.6056 |  |
| Site: UCSD (vs UAB) | -0.0563 | 0.1418 | ±0.2837 | -0.397 | 0.6912 |  |
| **Site: UW (vs UAB)** | **-0.8945** | 0.1333 | ±0.2665 | **-6.712** | **1.92e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4650** | 0.1511 | ±0.3021 | **-3.078** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.9880** | 0.1788 | ±0.3576 | **+11.117** | **1.03e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3828** | 0.1501 | ±0.3002 | **-9.212** | **3.21e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.302** | **0.0213** | * |
| BMI (kg/m2) | +0.0050 | 0.0083 | ±0.0166 | +0.608 | 0.5430 |  |
| Hypertension | +0.2013 | 0.1219 | ±0.2438 | +1.651 | 0.0987 | . |
| High cholesterol | -0.0647 | 0.1138 | ±0.2276 | -0.568 | 0.5699 |  |
| **Kidney disease** | **+0.4619** | 0.2076 | ±0.4152 | **+2.225** | **0.0261** | * |
| Circulatory disease | +0.2866 | 0.1749 | ±0.3497 | +1.639 | 0.1013 |  |
| Time in range 70-180, pooled (%) | -0.0053 | 0.0063 | ±0.0126 | -0.849 | 0.3961 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **1251**, R² = **0.3179**, Adj R² = **0.3101**, F-statistic = **41.14** (p = **1.79e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.4**, BIC = **5234.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.4071** | 0.7391 | ±1.4782 | **+33.022** | **3.89e-239** | *** |
| Education: graduate level (vs college) | -0.1613 | 0.1134 | ±0.2269 | -1.422 | 0.1551 |  |
| Education: high school or below (vs college) | +0.1151 | 0.2219 | ±0.4438 | +0.519 | 0.6039 |  |
| Site: UCSD (vs UAB) | -0.0566 | 0.1418 | ±0.2836 | -0.399 | 0.6898 |  |
| **Site: UW (vs UAB)** | **-0.8943** | 0.1333 | ±0.2665 | **-6.711** | **1.93e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4654** | 0.1510 | ±0.3020 | **-3.082** | **0.0021** | ** |
| **Season: summer (vs autumn)** | **+1.9881** | 0.1788 | ±0.3577 | **+11.117** | **1.04e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3829** | 0.1501 | ±0.3002 | **-9.214** | **3.15e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.300** | **0.0214** | * |
| BMI (kg/m2) | +0.0050 | 0.0083 | ±0.0166 | +0.605 | 0.5451 |  |
| Hypertension | +0.2014 | 0.1219 | ±0.2439 | +1.652 | 0.0986 | . |
| High cholesterol | -0.0649 | 0.1138 | ±0.2276 | -0.571 | 0.5682 |  |
| **Kidney disease** | **+0.4618** | 0.2076 | ±0.4152 | **+2.224** | **0.0261** | * |
| Circulatory disease | +0.2866 | 0.1748 | ±0.3497 | +1.639 | 0.1012 |  |
| Avg. daily time in range 70-180 (%) | -0.0053 | 0.0062 | ±0.0125 | -0.857 | 0.3915 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.3175**, Adj R² = **0.3097**, F-statistic = **41.07** (p = **2.56e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.1**, BIC = **5235.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8995** | 0.4387 | ±0.8775 | **+54.473** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1601 | 0.1129 | ±0.2258 | -1.418 | 0.1562 |  |
| Education: high school or below (vs college) | +0.1182 | 0.2213 | ±0.4426 | +0.534 | 0.5934 |  |
| Site: UCSD (vs UAB) | -0.0677 | 0.1434 | ±0.2867 | -0.472 | 0.6368 |  |
| **Site: UW (vs UAB)** | **-0.8962** | 0.1340 | ±0.2681 | **-6.686** | **2.29e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4697** | 0.1505 | ±0.3009 | **-3.122** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9783** | 0.1790 | ±0.3579 | **+11.054** | **2.09e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3879** | 0.1501 | ±0.3001 | **-9.249** | **2.26e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.293** | **0.0219** | * |
| BMI (kg/m2) | +0.0054 | 0.0083 | ±0.0167 | +0.643 | 0.5202 |  |
| Hypertension | +0.2067 | 0.1217 | ±0.2434 | +1.698 | 0.0894 | . |
| High cholesterol | -0.0640 | 0.1142 | ±0.2284 | -0.561 | 0.5751 |  |
| **Kidney disease** | **+0.4715** | 0.2083 | ±0.4167 | **+2.263** | **0.0236** | * |
| Circulatory disease | +0.2961 | 0.1741 | ±0.3483 | +1.700 | 0.0891 | . |
| Any reading < 54 during wear (0/1) | -0.0280 | 0.1197 | ±0.2394 | -0.234 | 0.8149 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.3199**, Adj R² = **0.3122**, F-statistic = **41.53** (p = **2.97e-93**), Residual SE = **1.887** on **1236** df, AIC = **5153.7**, BIC = **5230.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8043** | 0.4359 | ±0.8718 | **+54.608** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1545 | 0.1131 | ±0.2261 | -1.366 | 0.1718 |  |
| Education: high school or below (vs college) | +0.1429 | 0.2215 | ±0.4430 | +0.645 | 0.5189 |  |
| Site: UCSD (vs UAB) | -0.0270 | 0.1431 | ±0.2861 | -0.189 | 0.8501 |  |
| **Site: UW (vs UAB)** | **-0.8668** | 0.1339 | ±0.2679 | **-6.472** | **9.67e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4658** | 0.1504 | ±0.3008 | **-3.097** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.9721** | 0.1786 | ±0.3572 | **+11.043** | **2.36e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3908** | 0.1495 | ±0.2991 | **-9.301** | **1.40e-20** | *** |
| **Age (years)** | **+0.0120** | 0.0051 | ±0.0102 | **+2.353** | **0.0186** | * |
| BMI (kg/m2) | +0.0055 | 0.0083 | ±0.0166 | +0.661 | 0.5086 |  |
| Hypertension | +0.2141 | 0.1214 | ±0.2428 | +1.764 | 0.0778 | . |
| High cholesterol | -0.0467 | 0.1138 | ±0.2275 | -0.410 | 0.6817 |  |
| **Kidney disease** | **+0.4656** | 0.2074 | ±0.4148 | **+2.245** | **0.0248** | * |
| Circulatory disease | +0.2950 | 0.1739 | ±0.3479 | +1.696 | 0.0899 | . |
| Time < 54 (%) | +0.1995 | 0.1129 | ±0.2257 | +1.767 | 0.0772 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.3195**, Adj R² = **0.3117**, F-statistic = **41.44** (p = **4.41e-93**), Residual SE = **1.887** on **1236** df, AIC = **5154.5**, BIC = **5231.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8338** | 0.4351 | ±0.8701 | **+54.783** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1530 | 0.1131 | ±0.2262 | -1.353 | 0.1761 |  |
| Education: high school or below (vs college) | +0.1411 | 0.2213 | ±0.4426 | +0.637 | 0.5238 |  |
| Site: UCSD (vs UAB) | -0.0342 | 0.1425 | ±0.2850 | -0.240 | 0.8101 |  |
| **Site: UW (vs UAB)** | **-0.8655** | 0.1338 | ±0.2676 | **-6.468** | **9.90e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4692** | 0.1503 | ±0.3007 | **-3.121** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9713** | 0.1790 | ±0.3579 | **+11.016** | **3.20e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3959** | 0.1494 | ±0.2988 | **-9.342** | **9.44e-21** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.302** | **0.0213** | * |
| BMI (kg/m2) | +0.0054 | 0.0083 | ±0.0166 | +0.649 | 0.5161 |  |
| Hypertension | +0.2172 | 0.1215 | ±0.2430 | +1.787 | 0.0739 | . |
| High cholesterol | -0.0497 | 0.1137 | ±0.2274 | -0.437 | 0.6618 |  |
| **Kidney disease** | **+0.4660** | 0.2072 | ±0.4145 | **+2.249** | **0.0245** | * |
| Circulatory disease | +0.2965 | 0.1738 | ±0.3476 | +1.706 | 0.0881 | . |
| Avg. daily time < 54 (%) | +0.2442 | 0.1802 | ±0.3603 | +1.356 | 0.1752 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.3182**, Adj R² = **0.3104**, F-statistic = **41.20** (p = **1.40e-92**), Residual SE = **1.889** on **1236** df, AIC = **5156.9**, BIC = **5233.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8381** | 0.4364 | ±0.8729 | **+54.619** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1522 | 0.1133 | ±0.2266 | -1.344 | 0.1791 |  |
| Education: high school or below (vs college) | +0.1394 | 0.2216 | ±0.4432 | +0.629 | 0.5294 |  |
| Site: UCSD (vs UAB) | -0.0503 | 0.1426 | ±0.2851 | -0.353 | 0.7243 |  |
| **Site: UW (vs UAB)** | **-0.8796** | 0.1340 | ±0.2679 | **-6.566** | **5.16e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4718** | 0.1505 | ±0.3009 | **-3.136** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9767** | 0.1785 | ±0.3570 | **+11.075** | **1.66e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3955** | 0.1501 | ±0.3001 | **-9.299** | **1.42e-20** | *** |
| **Age (years)** | **+0.0120** | 0.0051 | ±0.0102 | **+2.348** | **0.0189** | * |
| BMI (kg/m2) | +0.0050 | 0.0083 | ±0.0166 | +0.602 | 0.5473 |  |
| Hypertension | +0.2119 | 0.1216 | ±0.2432 | +1.742 | 0.0815 | . |
| High cholesterol | -0.0553 | 0.1142 | ±0.2285 | -0.484 | 0.6285 |  |
| **Kidney disease** | **+0.4723** | 0.2074 | ±0.4148 | **+2.277** | **0.0228** | * |
| Circulatory disease | +0.2936 | 0.1741 | ±0.3482 | +1.686 | 0.0917 | . |
| Time 54-69, pooled (%) | +0.0440 | 0.0305 | ±0.0610 | +1.442 | 0.1492 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1251**, R² = **0.3184**, Adj R² = **0.3107**, F-statistic = **41.24** (p = **1.14e-92**), Residual SE = **1.889** on **1236** df, AIC = **5156.4**, BIC = **5233.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8406** | 0.4355 | ±0.8710 | **+54.741** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1504 | 0.1133 | ±0.2266 | -1.328 | 0.1843 |  |
| Education: high school or below (vs college) | +0.1430 | 0.2215 | ±0.4431 | +0.646 | 0.5185 |  |
| Site: UCSD (vs UAB) | -0.0516 | 0.1423 | ±0.2846 | -0.362 | 0.7172 |  |
| **Site: UW (vs UAB)** | **-0.8774** | 0.1338 | ±0.2676 | **-6.558** | **5.47e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4723** | 0.1504 | ±0.3008 | **-3.140** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9777** | 0.1785 | ±0.3570 | **+11.080** | **1.57e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3983** | 0.1501 | ±0.3002 | **-9.317** | **1.20e-20** | *** |
| **Age (years)** | **+0.0119** | 0.0051 | ±0.0102 | **+2.338** | **0.0194** | * |
| BMI (kg/m2) | +0.0050 | 0.0083 | ±0.0166 | +0.598 | 0.5502 |  |
| Hypertension | +0.2135 | 0.1216 | ±0.2432 | +1.755 | 0.0792 | . |
| High cholesterol | -0.0549 | 0.1141 | ±0.2283 | -0.481 | 0.6303 |  |
| **Kidney disease** | **+0.4726** | 0.2074 | ±0.4147 | **+2.279** | **0.0227** | * |
| Circulatory disease | +0.2939 | 0.1741 | ±0.3482 | +1.688 | 0.0914 | . |
| Avg. daily time 54-69 (%) | +0.0507 | 0.0316 | ±0.0633 | +1.604 | 0.1087 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **1251**, R² = **0.3188**, Adj R² = **0.3111**, F-statistic = **41.32** (p = **7.66e-93**), Residual SE = **1.888** on **1236** df, AIC = **5155.6**, BIC = **5232.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8134** | 0.4363 | ±0.8726 | **+54.582** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1504 | 0.1131 | ±0.2262 | -1.330 | 0.1835 |  |
| Education: high school or below (vs college) | +0.1465 | 0.2215 | ±0.4430 | +0.661 | 0.5084 |  |
| Site: UCSD (vs UAB) | -0.0399 | 0.1426 | ±0.2852 | -0.280 | 0.7795 |  |
| **Site: UW (vs UAB)** | **-0.8713** | 0.1339 | ±0.2677 | **-6.509** | **7.59e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4711** | 0.1505 | ±0.3010 | **-3.131** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9748** | 0.1785 | ±0.3570 | **+11.063** | **1.89e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3972** | 0.1498 | ±0.2996 | **-9.328** | **1.08e-20** | *** |
| **Age (years)** | **+0.0120** | 0.0051 | ±0.0102 | **+2.362** | **0.0182** | * |
| BMI (kg/m2) | +0.0050 | 0.0083 | ±0.0166 | +0.605 | 0.5455 |  |
| Hypertension | +0.2142 | 0.1215 | ±0.2431 | +1.763 | 0.0779 | . |
| High cholesterol | -0.0506 | 0.1141 | ±0.2283 | -0.443 | 0.6574 |  |
| **Kidney disease** | **+0.4709** | 0.2071 | ±0.4142 | **+2.274** | **0.0230** | * |
| Circulatory disease | +0.2940 | 0.1741 | ±0.3482 | +1.689 | 0.0913 | . |
| Time < 70 (%) | +0.0488 | 0.0283 | ±0.0566 | +1.722 | 0.0851 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **1251**, R² = **0.3188**, Adj R² = **0.3111**, F-statistic = **41.32** (p = **7.76e-93**), Residual SE = **1.888** on **1236** df, AIC = **5155.7**, BIC = **5232.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8296** | 0.4353 | ±0.8706 | **+54.746** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1491 | 0.1132 | ±0.2264 | -1.318 | 0.1876 |  |
| Education: high school or below (vs college) | +0.1473 | 0.2215 | ±0.4429 | +0.665 | 0.5060 |  |
| Site: UCSD (vs UAB) | -0.0453 | 0.1422 | ±0.2845 | -0.318 | 0.7501 |  |
| **Site: UW (vs UAB)** | **-0.8712** | 0.1337 | ±0.2673 | **-6.518** | **7.15e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4723** | 0.1504 | ±0.3008 | **-3.140** | **0.0017** | ** |
| **Season: summer (vs autumn)** | **+1.9761** | 0.1786 | ±0.3572 | **+11.065** | **1.86e-28** | *** |
| **Season: winter (vs autumn)** | **-1.4002** | 0.1498 | ±0.2996 | **-9.346** | **9.08e-21** | *** |
| **Age (years)** | **+0.0119** | 0.0051 | ±0.0102 | **+2.337** | **0.0195** | * |
| BMI (kg/m2) | +0.0050 | 0.0083 | ±0.0166 | +0.600 | 0.5484 |  |
| Hypertension | +0.2157 | 0.1215 | ±0.2431 | +1.775 | 0.0759 | . |
| High cholesterol | -0.0522 | 0.1140 | ±0.2281 | -0.458 | 0.6472 |  |
| **Kidney disease** | **+0.4714** | 0.2071 | ±0.4143 | **+2.276** | **0.0229** | * |
| Circulatory disease | +0.2945 | 0.1741 | ±0.3481 | +1.692 | 0.0906 | . |
| Avg. daily time < 70 (%) | +0.0512 | 0.0302 | ±0.0604 | +1.696 | 0.0899 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.3177**, Adj R² = **0.3100**, F-statistic = **41.11** (p = **2.13e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.7**, BIC = **5234.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5980** | 1.5052 | ±3.0104 | **+16.342** | **4.95e-60** | *** |
| Education: graduate level (vs college) | -0.1594 | 0.1134 | ±0.2269 | -1.405 | 0.1601 |  |
| Education: high school or below (vs college) | +0.1119 | 0.2238 | ±0.4476 | +0.500 | 0.6172 |  |
| Site: UCSD (vs UAB) | -0.0604 | 0.1418 | ±0.2836 | -0.426 | 0.6700 |  |
| **Site: UW (vs UAB)** | **-0.8924** | 0.1335 | ±0.2670 | **-6.686** | **2.30e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4682** | 0.1510 | ±0.3020 | **-3.101** | **0.0019** | ** |
| **Season: summer (vs autumn)** | **+1.9828** | 0.1788 | ±0.3577 | **+11.087** | **1.46e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3861** | 0.1500 | ±0.3000 | **-9.241** | **2.43e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.320** | **0.0203** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0166 | +0.634 | 0.5258 |  |
| Hypertension | +0.2059 | 0.1218 | ±0.2435 | +1.691 | 0.0908 | . |
| High cholesterol | -0.0612 | 0.1139 | ±0.2278 | -0.537 | 0.5913 |  |
| **Kidney disease** | **+0.4701** | 0.2078 | ±0.4155 | **+2.263** | **0.0237** | * |
| Circulatory disease | +0.2862 | 0.1750 | ±0.3500 | +1.636 | 0.1019 |  |
| Time 54-250, pooled (%) | -0.0072 | 0.0145 | ±0.0291 | -0.496 | 0.6197 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.3176**, Adj R² = **0.3099**, F-statistic = **41.09** (p = **2.25e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.9**, BIC = **5234.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5096** | 1.5078 | ±3.0157 | **+16.255** | **2.07e-59** | *** |
| Education: graduate level (vs college) | -0.1593 | 0.1134 | ±0.2269 | -1.405 | 0.1602 |  |
| Education: high school or below (vs college) | +0.1130 | 0.2239 | ±0.4477 | +0.505 | 0.6137 |  |
| Site: UCSD (vs UAB) | -0.0612 | 0.1418 | ±0.2837 | -0.432 | 0.6659 |  |
| **Site: UW (vs UAB)** | **-0.8929** | 0.1334 | ±0.2669 | **-6.691** | **2.22e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4685** | 0.1509 | ±0.3019 | **-3.103** | **0.0019** | ** |
| **Season: summer (vs autumn)** | **+1.9823** | 0.1789 | ±0.3577 | **+11.084** | **1.51e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3863** | 0.1500 | ±0.3000 | **-9.241** | **2.44e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.317** | **0.0205** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0166 | +0.633 | 0.5269 |  |
| Hypertension | +0.2060 | 0.1218 | ±0.2435 | +1.692 | 0.0906 | . |
| High cholesterol | -0.0615 | 0.1139 | ±0.2278 | -0.540 | 0.5894 |  |
| **Kidney disease** | **+0.4705** | 0.2078 | ±0.4156 | **+2.264** | **0.0236** | * |
| Circulatory disease | +0.2872 | 0.1750 | ±0.3499 | +1.641 | 0.1007 |  |
| Avg. daily time 54-250 (%) | -0.0063 | 0.0145 | ±0.0291 | -0.434 | 0.6644 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.3176**, Adj R² = **0.3099**, F-statistic = **41.09** (p = **2.33e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.9**, BIC = **5234.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8826** | 0.4344 | ±0.8688 | **+54.977** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1612 | 0.1134 | ±0.2269 | -1.421 | 0.1552 |  |
| Education: high school or below (vs college) | +0.1200 | 0.2217 | ±0.4434 | +0.541 | 0.5883 |  |
| Site: UCSD (vs UAB) | -0.0609 | 0.1418 | ±0.2837 | -0.429 | 0.6678 |  |
| **Site: UW (vs UAB)** | **-0.8971** | 0.1338 | ±0.2675 | **-6.707** | **1.98e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4664** | 0.1508 | ±0.3015 | **-3.094** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.9843** | 0.1786 | ±0.3572 | **+11.109** | **1.13e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3834** | 0.1503 | ±0.3006 | **-9.205** | **3.43e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.294** | **0.0218** | * |
| BMI (kg/m2) | +0.0051 | 0.0083 | ±0.0166 | +0.616 | 0.5377 |  |
| Hypertension | +0.2022 | 0.1218 | ±0.2437 | +1.659 | 0.0970 | . |
| High cholesterol | -0.0659 | 0.1140 | ±0.2279 | -0.578 | 0.5631 |  |
| **Kidney disease** | **+0.4643** | 0.2083 | ±0.4167 | **+2.229** | **0.0258** | * |
| Circulatory disease | +0.2923 | 0.1742 | ±0.3484 | +1.678 | 0.0934 | . |
| Time 181-250, pooled (%) | +0.0044 | 0.0088 | ±0.0177 | +0.502 | 0.6158 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1251**, R² = **0.3176**, Adj R² = **0.3099**, F-statistic = **41.09** (p = **2.27e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.9**, BIC = **5234.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8826** | 0.4344 | ±0.8688 | **+54.981** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1616 | 0.1135 | ±0.2269 | -1.424 | 0.1545 |  |
| Education: high school or below (vs college) | +0.1203 | 0.2216 | ±0.4432 | +0.543 | 0.5872 |  |
| Site: UCSD (vs UAB) | -0.0602 | 0.1418 | ±0.2836 | -0.425 | 0.6710 |  |
| **Site: UW (vs UAB)** | **-0.8971** | 0.1337 | ±0.2674 | **-6.710** | **1.95e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4664** | 0.1507 | ±0.3015 | **-3.094** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.9848** | 0.1786 | ±0.3573 | **+11.110** | **1.12e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3831** | 0.1503 | ±0.3007 | **-9.200** | **3.57e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.295** | **0.0217** | * |
| BMI (kg/m2) | +0.0051 | 0.0083 | ±0.0166 | +0.613 | 0.5396 |  |
| Hypertension | +0.2018 | 0.1219 | ±0.2438 | +1.655 | 0.0979 | . |
| High cholesterol | -0.0663 | 0.1139 | ±0.2279 | -0.582 | 0.5609 |  |
| **Kidney disease** | **+0.4634** | 0.2083 | ±0.4167 | **+2.224** | **0.0261** | * |
| Circulatory disease | +0.2921 | 0.1742 | ±0.3485 | +1.677 | 0.0936 | . |
| Avg. daily time 181-250 (%) | +0.0048 | 0.0088 | ±0.0175 | +0.551 | 0.5819 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **1251**, R² = **0.3176**, Adj R² = **0.3099**, F-statistic = **41.09** (p = **2.25e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.9**, BIC = **5234.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8803** | 0.4345 | ±0.8689 | **+54.967** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1610 | 0.1135 | ±0.2271 | -1.418 | 0.1561 |  |
| Education: high school or below (vs college) | +0.1153 | 0.2224 | ±0.4448 | +0.519 | 0.6041 |  |
| Site: UCSD (vs UAB) | -0.0606 | 0.1418 | ±0.2836 | -0.427 | 0.6692 |  |
| **Site: UW (vs UAB)** | **-0.8961** | 0.1334 | ±0.2669 | **-6.716** | **1.87e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4665** | 0.1510 | ±0.3020 | **-3.090** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.9851** | 0.1789 | ±0.3577 | **+11.098** | **1.29e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3837** | 0.1502 | ±0.3005 | **-9.209** | **3.28e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.301** | **0.0214** | * |
| BMI (kg/m2) | +0.0051 | 0.0083 | ±0.0166 | +0.620 | 0.5354 |  |
| Hypertension | +0.2027 | 0.1220 | ±0.2439 | +1.662 | 0.0966 | . |
| High cholesterol | -0.0648 | 0.1139 | ±0.2277 | -0.569 | 0.5694 |  |
| **Kidney disease** | **+0.4653** | 0.2080 | ±0.4160 | **+2.237** | **0.0253** | * |
| Circulatory disease | +0.2890 | 0.1748 | ±0.3496 | +1.654 | 0.0982 | . |
| Time > 180 (%) | +0.0035 | 0.0063 | ±0.0126 | +0.547 | 0.5847 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.3176**, Adj R² = **0.3099**, F-statistic = **41.10** (p = **2.22e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.8**, BIC = **5234.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8807** | 0.4344 | ±0.8688 | **+54.973** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1612 | 0.1135 | ±0.2271 | -1.420 | 0.1557 |  |
| Education: high school or below (vs college) | +0.1155 | 0.2223 | ±0.4447 | +0.519 | 0.6035 |  |
| Site: UCSD (vs UAB) | -0.0602 | 0.1418 | ±0.2836 | -0.425 | 0.6712 |  |
| **Site: UW (vs UAB)** | **-0.8960** | 0.1334 | ±0.2668 | **-6.716** | **1.87e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4666** | 0.1510 | ±0.3019 | **-3.091** | **0.0020** | ** |
| **Season: summer (vs autumn)** | **+1.9853** | 0.1789 | ±0.3578 | **+11.098** | **1.28e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3835** | 0.1503 | ±0.3005 | **-9.207** | **3.37e-20** | *** |
| **Age (years)** | **+0.0117** | 0.0051 | ±0.0102 | **+2.302** | **0.0213** | * |
| BMI (kg/m2) | +0.0051 | 0.0083 | ±0.0166 | +0.617 | 0.5369 |  |
| Hypertension | +0.2025 | 0.1220 | ±0.2440 | +1.660 | 0.0969 | . |
| High cholesterol | -0.0649 | 0.1138 | ±0.2277 | -0.570 | 0.5687 |  |
| **Kidney disease** | **+0.4650** | 0.2080 | ±0.4160 | **+2.235** | **0.0254** | * |
| Circulatory disease | +0.2888 | 0.1748 | ±0.3495 | +1.652 | 0.0984 | . |
| Avg. daily time > 180 (%) | +0.0036 | 0.0063 | ±0.0125 | +0.571 | 0.5679 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.3178**, Adj R² = **0.3101**, F-statistic = **41.13** (p = **1.86e-92**), Residual SE = **1.890** on **1236** df, AIC = **5157.5**, BIC = **5234.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8890** | 0.4339 | ±0.8678 | **+55.059** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1593 | 0.1133 | ±0.2267 | -1.405 | 0.1599 |  |
| Education: high school or below (vs college) | +0.1132 | 0.2224 | ±0.4448 | +0.509 | 0.6106 |  |
| Site: UCSD (vs UAB) | -0.0606 | 0.1416 | ±0.2832 | -0.428 | 0.6688 |  |
| **Site: UW (vs UAB)** | **-0.8958** | 0.1333 | ±0.2666 | **-6.719** | **1.83e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4696** | 0.1506 | ±0.3012 | **-3.118** | **0.0018** | ** |
| **Season: summer (vs autumn)** | **+1.9863** | 0.1787 | ±0.3575 | **+11.112** | **1.09e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3861** | 0.1500 | ±0.3000 | **-9.240** | **2.46e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.321** | **0.0203** | * |
| BMI (kg/m2) | +0.0047 | 0.0083 | ±0.0166 | +0.567 | 0.5708 |  |
| Hypertension | +0.2037 | 0.1216 | ±0.2433 | +1.675 | 0.0940 | . |
| High cholesterol | -0.0673 | 0.1140 | ±0.2281 | -0.590 | 0.5550 |  |
| **Kidney disease** | **+0.4718** | 0.2074 | ±0.4148 | **+2.274** | **0.0229** | * |
| Circulatory disease | +0.2907 | 0.1748 | ±0.3496 | +1.663 | 0.0964 | . |
| Nocturnal time > 180 (%) | +0.0054 | 0.0070 | ±0.0141 | +0.763 | 0.4455 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.3194**, Adj R² = **0.3117**, F-statistic = **41.44** (p = **4.44e-93**), Residual SE = **1.888** on **1236** df, AIC = **5154.5**, BIC = **5231.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9579** | 0.4369 | ±0.8739 | **+54.831** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1609 | 0.1134 | ±0.2267 | -1.420 | 0.1557 |  |
| Education: high school or below (vs college) | +0.1207 | 0.2208 | ±0.4416 | +0.547 | 0.5846 |  |
| Site: UCSD (vs UAB) | -0.0692 | 0.1421 | ±0.2841 | -0.487 | 0.6259 |  |
| **Site: UW (vs UAB)** | **-0.8900** | 0.1335 | ±0.2669 | **-6.668** | **2.59e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4850** | 0.1506 | ±0.3011 | **-3.221** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+1.9667** | 0.1788 | ±0.3576 | **+10.998** | **3.89e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3998** | 0.1500 | ±0.3001 | **-9.330** | **1.06e-20** | *** |
| **Age (years)** | **+0.0120** | 0.0051 | ±0.0101 | **+2.361** | **0.0182** | * |
| BMI (kg/m2) | +0.0041 | 0.0083 | ±0.0166 | +0.496 | 0.6202 |  |
| Hypertension | +0.2222 | 0.1216 | ±0.2432 | +1.827 | 0.0676 | . |
| High cholesterol | -0.0581 | 0.1138 | ±0.2276 | -0.511 | 0.6094 |  |
| **Kidney disease** | **+0.4778** | 0.2094 | ±0.4188 | **+2.282** | **0.0225** | * |
| Circulatory disease | +0.2915 | 0.1731 | ±0.3462 | +1.684 | 0.0922 | . |
| Any reading > 250 during wear (0/1) | -0.2604 | 0.1388 | ±0.2775 | -1.877 | 0.0605 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.3175**, Adj R² = **0.3098**, F-statistic = **41.08** (p = **2.42e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.0**, BIC = **5235.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8812** | 0.4343 | ±0.8686 | **+54.985** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1593 | 0.1134 | ±0.2269 | -1.404 | 0.1602 |  |
| Education: high school or below (vs college) | +0.1149 | 0.2240 | ±0.4480 | +0.513 | 0.6079 |  |
| Site: UCSD (vs UAB) | -0.0624 | 0.1419 | ±0.2837 | -0.440 | 0.6598 |  |
| **Site: UW (vs UAB)** | **-0.8938** | 0.1334 | ±0.2668 | **-6.699** | **2.09e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4688** | 0.1509 | ±0.3018 | **-3.107** | **0.0019** | ** |
| **Season: summer (vs autumn)** | **+1.9816** | 0.1789 | ±0.3577 | **+11.078** | **1.60e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3865** | 0.1500 | ±0.3001 | **-9.240** | **2.46e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.316** | **0.0206** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0166 | +0.634 | 0.5262 |  |
| Hypertension | +0.2060 | 0.1218 | ±0.2436 | +1.691 | 0.0908 | . |
| High cholesterol | -0.0620 | 0.1140 | ±0.2279 | -0.544 | 0.5862 |  |
| **Kidney disease** | **+0.4707** | 0.2079 | ±0.4158 | **+2.264** | **0.0236** | * |
| Circulatory disease | +0.2889 | 0.1749 | ±0.3499 | +1.651 | 0.0987 | . |
| Time > 250 (%) | +0.0046 | 0.0144 | ±0.0289 | +0.318 | 0.7506 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.3175**, Adj R² = **0.3098**, F-statistic = **41.08** (p = **2.44e-92**), Residual SE = **1.890** on **1236** df, AIC = **5158.0**, BIC = **5235.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8817** | 0.4343 | ±0.8685 | **+54.992** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.1593 | 0.1134 | ±0.2269 | -1.404 | 0.1602 |  |
| Education: high school or below (vs college) | +0.1152 | 0.2240 | ±0.4480 | +0.514 | 0.6072 |  |
| Site: UCSD (vs UAB) | -0.0625 | 0.1419 | ±0.2837 | -0.440 | 0.6597 |  |
| **Site: UW (vs UAB)** | **-0.8939** | 0.1334 | ±0.2668 | **-6.701** | **2.07e-11** | *** |
| **Season: spring (vs autumn)** | **-0.4688** | 0.1509 | ±0.3018 | **-3.107** | **0.0019** | ** |
| **Season: summer (vs autumn)** | **+1.9815** | 0.1789 | ±0.3577 | **+11.078** | **1.61e-28** | *** |
| **Season: winter (vs autumn)** | **-1.3864** | 0.1501 | ±0.3001 | **-9.239** | **2.49e-20** | *** |
| **Age (years)** | **+0.0118** | 0.0051 | ±0.0102 | **+2.316** | **0.0206** | * |
| BMI (kg/m2) | +0.0053 | 0.0083 | ±0.0166 | +0.633 | 0.5268 |  |
| Hypertension | +0.2060 | 0.1218 | ±0.2436 | +1.691 | 0.0908 | . |
| High cholesterol | -0.0620 | 0.1140 | ±0.2279 | -0.544 | 0.5862 |  |
| **Kidney disease** | **+0.4709** | 0.2079 | ±0.4158 | **+2.265** | **0.0235** | * |
| Circulatory disease | +0.2890 | 0.1749 | ±0.3499 | +1.652 | 0.0985 | . |
| Avg. daily time > 250 (%) | +0.0045 | 0.0144 | ±0.0288 | +0.310 | 0.7567 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 1,251; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **1251**, R² = **0.2679**, Adj R² = **0.2602**, F-statistic = **34.81** (p = **1.05e-74**), Residual SE = **5.823** on **1237** df, AIC = **7972.2**, BIC = **8044.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3662** | 1.2999 | ±2.5998 | **+37.977** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9936** | 0.3543 | ±0.7087 | **+2.804** | **0.0050** | ** |
| Education: high school or below (vs college) | +0.8238 | 0.6702 | ±1.3404 | +1.229 | 0.2190 |  |
| **Site: UCSD (vs UAB)** | **+2.8535** | 0.4577 | ±0.9155 | **+6.234** | **4.55e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9571** | 0.4064 | ±0.8129 | **-4.815** | **1.47e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4850** | 0.4652 | ±0.9303 | **-3.192** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2286** | 0.5125 | ±1.0250 | **+4.348** | **1.37e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4450** | 0.4816 | ±0.9632 | **-11.305** | **1.23e-29** | *** |
| **Age (years)** | **-0.0516** | 0.0156 | ±0.0312 | **-3.302** | **9.61e-04** | *** |
| BMI (kg/m2) | -0.0145 | 0.0253 | ±0.0506 | -0.574 | 0.5659 |  |
| Hypertension | +0.0922 | 0.3774 | ±0.7548 | +0.244 | 0.8070 |  |
| High cholesterol | -0.6624 | 0.3497 | ±0.6994 | -1.894 | 0.0582 | . |
| Kidney disease | -0.2967 | 0.6681 | ±1.3362 | -0.444 | 0.6570 |  |
| Circulatory disease | +0.5547 | 0.5081 | ±1.0162 | +1.092 | 0.2749 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **1251**, R² = **0.2693**, Adj R² = **0.2610**, F-statistic = **32.54** (p = **1.92e-74**), Residual SE = **5.820** on **1236** df, AIC = **7971.7**, BIC = **8048.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.8318** | 1.8804 | ±3.7608 | **+24.905** | **6.55e-137** | *** |
| **Education: graduate level (vs college)** | **+0.9886** | 0.3543 | ±0.7087 | **+2.790** | **0.0053** | ** |
| Education: high school or below (vs college) | +0.7445 | 0.6735 | ±1.3470 | +1.105 | 0.2690 |  |
| **Site: UCSD (vs UAB)** | **+2.8422** | 0.4573 | ±0.9146 | **+6.215** | **5.13e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9778** | 0.4062 | ±0.8124 | **-4.869** | **1.12e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4223** | 0.4657 | ±0.9314 | **-3.054** | **0.0023** | ** |
| **Season: summer (vs autumn)** | **+2.2492** | 0.5130 | ±1.0259 | **+4.385** | **1.16e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4191** | 0.4804 | ±0.9609 | **-11.279** | **1.66e-29** | *** |
| **Age (years)** | **-0.0537** | 0.0157 | ±0.0314 | **-3.420** | **6.27e-04** | *** |
| BMI (kg/m2) | -0.0180 | 0.0253 | ±0.0507 | -0.709 | 0.4781 |  |
| Hypertension | +0.0634 | 0.3782 | ±0.7563 | +0.168 | 0.8668 |  |
| **High cholesterol** | **-0.7167** | 0.3501 | ±0.7002 | **-2.047** | **0.0406** | * |
| Kidney disease | -0.2951 | 0.6698 | ±1.3397 | -0.441 | 0.6595 |  |
| Circulatory disease | +0.5198 | 0.5057 | ±1.0114 | +1.028 | 0.3040 |  |
| HbA1c (%) | +0.4929 | 0.2662 | ±0.5324 | +1.851 | 0.0641 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **1251**, R² = **0.2679**, Adj R² = **0.2596**, F-statistic = **32.31** (p = **5.93e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.1**, BIC = **8051.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.0023** | 1.5834 | ±3.1669 | **+30.947** | **2.82e-210** | *** |
| **Education: graduate level (vs college)** | **+0.9859** | 0.3550 | ±0.7100 | **+2.777** | **0.0055** | ** |
| Education: high school or below (vs college) | +0.8045 | 0.6763 | ±1.3526 | +1.190 | 0.2342 |  |
| **Site: UCSD (vs UAB)** | **+2.8564** | 0.4584 | ±0.9168 | **+6.231** | **4.63e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9668** | 0.4070 | ±0.8140 | **-4.833** | **1.35e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4790** | 0.4663 | ±0.9326 | **-3.172** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2380** | 0.5133 | ±1.0265 | **+4.360** | **1.30e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4351** | 0.4816 | ±0.9632 | **-11.285** | **1.55e-29** | *** |
| **Age (years)** | **-0.0518** | 0.0157 | ±0.0313 | **-3.309** | **9.37e-04** | *** |
| BMI (kg/m2) | -0.0150 | 0.0253 | ±0.0507 | -0.591 | 0.5542 |  |
| Hypertension | +0.0806 | 0.3786 | ±0.7573 | +0.213 | 0.8314 |  |
| High cholesterol | -0.6690 | 0.3497 | ±0.6995 | -1.913 | 0.0558 | . |
| Kidney disease | -0.3074 | 0.6685 | ±1.3369 | -0.460 | 0.6456 |  |
| Circulatory disease | +0.5455 | 0.5097 | ±1.0195 | +1.070 | 0.2846 |  |
| Mean glucose (mg/dL) | +0.0033 | 0.0082 | ±0.0164 | +0.404 | 0.6859 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **1251**, R² = **0.2679**, Adj R² = **0.2596**, F-statistic = **32.31** (p = **5.93e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.1**, BIC = **8051.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5436** | 2.4167 | ±4.8335 | **+20.086** | **9.69e-90** | *** |
| **Education: graduate level (vs college)** | **+0.9859** | 0.3550 | ±0.7100 | **+2.777** | **0.0055** | ** |
| Education: high school or below (vs college) | +0.8045 | 0.6763 | ±1.3526 | +1.190 | 0.2342 |  |
| **Site: UCSD (vs UAB)** | **+2.8564** | 0.4584 | ±0.9168 | **+6.231** | **4.63e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9668** | 0.4070 | ±0.8140 | **-4.833** | **1.35e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4790** | 0.4663 | ±0.9326 | **-3.172** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2380** | 0.5133 | ±1.0265 | **+4.360** | **1.30e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4351** | 0.4816 | ±0.9632 | **-11.285** | **1.55e-29** | *** |
| **Age (years)** | **-0.0518** | 0.0157 | ±0.0313 | **-3.309** | **9.37e-04** | *** |
| BMI (kg/m2) | -0.0150 | 0.0253 | ±0.0507 | -0.591 | 0.5542 |  |
| Hypertension | +0.0806 | 0.3786 | ±0.7573 | +0.213 | 0.8314 |  |
| High cholesterol | -0.6690 | 0.3497 | ±0.6995 | -1.913 | 0.0558 | . |
| Kidney disease | -0.3074 | 0.6685 | ±1.3369 | -0.460 | 0.6456 |  |
| Circulatory disease | +0.5455 | 0.5097 | ±1.0195 | +1.070 | 0.2846 |  |
| GMI (%) | +0.1386 | 0.3426 | ±0.6852 | +0.404 | 0.6859 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **1251**, R² = **0.2684**, Adj R² = **0.2602**, F-statistic = **32.40** (p = **3.92e-74**), Residual SE = **5.823** on **1236** df, AIC = **7973.2**, BIC = **8050.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4756** | 1.5396 | ±3.0793 | **+31.485** | **1.40e-217** | *** |
| **Education: graduate level (vs college)** | **+0.9802** | 0.3546 | ±0.7091 | **+2.764** | **0.0057** | ** |
| Education: high school or below (vs college) | +0.7756 | 0.6757 | ±1.3514 | +1.148 | 0.2510 |  |
| **Site: UCSD (vs UAB)** | **+2.8486** | 0.4582 | ±0.9164 | **+6.217** | **5.06e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9794** | 0.4070 | ±0.8139 | **-4.864** | **1.15e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4830** | 0.4656 | ±0.9312 | **-3.185** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2504** | 0.5133 | ±1.0266 | **+4.384** | **1.16e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4331** | 0.4819 | ±0.9639 | **-11.273** | **1.78e-29** | *** |
| **Age (years)** | **-0.0513** | 0.0156 | ±0.0313 | **-3.282** | **0.0010** | ** |
| BMI (kg/m2) | -0.0178 | 0.0255 | ±0.0510 | -0.697 | 0.4856 |  |
| Hypertension | +0.0681 | 0.3785 | ±0.7571 | +0.180 | 0.8572 |  |
| High cholesterol | -0.6852 | 0.3498 | ±0.6997 | -1.959 | 0.0502 | . |
| Kidney disease | -0.3008 | 0.6708 | ±1.3416 | -0.448 | 0.6539 |  |
| Circulatory disease | +0.5396 | 0.5095 | ±1.0190 | +1.059 | 0.2896 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0084 | 0.0075 | ±0.0150 | +1.111 | 0.2667 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.2684**, Adj R² = **0.2601**, F-statistic = **32.39** (p = **3.95e-74**), Residual SE = **5.823** on **1236** df, AIC = **7973.2**, BIC = **8050.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8366** | 1.3582 | ±2.7164 | **+36.694** | **9.26e-295** | *** |
| **Education: graduate level (vs college)** | **+0.9976** | 0.3543 | ±0.7086 | **+2.816** | **0.0049** | ** |
| Education: high school or below (vs college) | +0.8318 | 0.6728 | ±1.3455 | +1.236 | 0.2163 |  |
| **Site: UCSD (vs UAB)** | **+2.8297** | 0.4593 | ±0.9185 | **+6.161** | **7.21e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9448** | 0.4074 | ±0.8147 | **-4.774** | **1.80e-06** | *** |
| **Season: spring (vs autumn)** | **-1.5008** | 0.4660 | ±0.9320 | **-3.221** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+2.2128** | 0.5133 | ±1.0266 | **+4.311** | **1.63e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4596** | 0.4813 | ±0.9627 | **-11.342** | **8.08e-30** | *** |
| **Age (years)** | **-0.0506** | 0.0157 | ±0.0314 | **-3.222** | **0.0013** | ** |
| BMI (kg/m2) | -0.0143 | 0.0254 | ±0.0507 | -0.562 | 0.5739 |  |
| Hypertension | +0.1236 | 0.3780 | ±0.7561 | +0.327 | 0.7436 |  |
| High cholesterol | -0.6630 | 0.3498 | ±0.6996 | -1.895 | 0.0580 | . |
| Kidney disease | -0.2450 | 0.6673 | ±1.3346 | -0.367 | 0.7135 |  |
| Circulatory disease | +0.5769 | 0.5091 | ±1.0182 | +1.133 | 0.2572 |  |
| Glucose SD, pooled (mg/dL) | -0.0251 | 0.0256 | ±0.0511 | -0.984 | 0.3253 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.2681**, Adj R² = **0.2598**, F-statistic = **32.35** (p = **5.04e-74**), Residual SE = **5.824** on **1236** df, AIC = **7973.7**, BIC = **8050.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.6728** | 1.3543 | ±2.7086 | **+36.678** | **1.67e-294** | *** |
| **Education: graduate level (vs college)** | **+0.9982** | 0.3544 | ±0.7089 | **+2.816** | **0.0049** | ** |
| Education: high school or below (vs college) | +0.8302 | 0.6724 | ±1.3449 | +1.235 | 0.2169 |  |
| **Site: UCSD (vs UAB)** | **+2.8386** | 0.4588 | ±0.9177 | **+6.187** | **6.15e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9467** | 0.4079 | ±0.8157 | **-4.773** | **1.81e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4986** | 0.4663 | ±0.9327 | **-3.214** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+2.2140** | 0.5139 | ±1.0278 | **+4.308** | **1.65e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4582** | 0.4818 | ±0.9636 | **-11.329** | **9.41e-30** | *** |
| **Age (years)** | **-0.0508** | 0.0157 | ±0.0314 | **-3.234** | **0.0012** | ** |
| BMI (kg/m2) | -0.0141 | 0.0254 | ±0.0507 | -0.557 | 0.5778 |  |
| Hypertension | +0.1138 | 0.3783 | ±0.7565 | +0.301 | 0.7636 |  |
| High cholesterol | -0.6620 | 0.3498 | ±0.6996 | -1.892 | 0.0585 | . |
| Kidney disease | -0.2584 | 0.6686 | ±1.3372 | -0.387 | 0.6991 |  |
| Circulatory disease | +0.5694 | 0.5088 | ±1.0177 | +1.119 | 0.2631 |  |
| Avg. daily SD (mg/dL) | -0.0188 | 0.0281 | ±0.0561 | -0.670 | 0.5025 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **1251**, R² = **0.2690**, Adj R² = **0.2607**, F-statistic = **32.48** (p = **2.57e-74**), Residual SE = **5.821** on **1236** df, AIC = **7972.3**, BIC = **8049.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3116** | 1.4337 | ±2.8675 | **+35.091** | **9.12e-270** | *** |
| **Education: graduate level (vs college)** | **+0.9804** | 0.3543 | ±0.7086 | **+2.767** | **0.0057** | ** |
| Education: high school or below (vs college) | +0.7929 | 0.6731 | ±1.3462 | +1.178 | 0.2388 |  |
| **Site: UCSD (vs UAB)** | **+2.8145** | 0.4596 | ±0.9193 | **+6.123** | **9.16e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9626** | 0.4071 | ±0.8142 | **-4.821** | **1.43e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4987** | 0.4657 | ±0.9313 | **-3.218** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+2.2258** | 0.5136 | ±1.0272 | **+4.334** | **1.47e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4430** | 0.4819 | ±0.9639 | **-11.294** | **1.40e-29** | *** |
| **Age (years)** | **-0.0503** | 0.0157 | ±0.0314 | **-3.203** | **0.0014** | ** |
| BMI (kg/m2) | -0.0151 | 0.0253 | ±0.0506 | -0.598 | 0.5497 |  |
| Hypertension | +0.1174 | 0.3777 | ±0.7554 | +0.311 | 0.7560 |  |
| High cholesterol | -0.6823 | 0.3501 | ±0.7003 | -1.949 | 0.0513 | . |
| Kidney disease | -0.2373 | 0.6693 | ±1.3385 | -0.355 | 0.7229 |  |
| Circulatory disease | +0.5674 | 0.5097 | ±1.0195 | +1.113 | 0.2657 |  |
| CV (%) | -0.0555 | 0.0416 | ±0.0833 | -1.333 | 0.1824 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1251**, R² = **0.2688**, Adj R² = **0.2605**, F-statistic = **32.45** (p = **3.02e-74**), Residual SE = **5.822** on **1236** df, AIC = **7972.7**, BIC = **8049.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.3379** | 1.6179 | ±3.2358 | **+29.877** | **3.97e-196** | *** |
| **Education: graduate level (vs college)** | **+0.9801** | 0.3543 | ±0.7085 | **+2.767** | **0.0057** | ** |
| Education: high school or below (vs college) | +0.8118 | 0.6730 | ±1.3460 | +1.206 | 0.2277 |  |
| **Site: UCSD (vs UAB)** | **+2.8219** | 0.4593 | ±0.9185 | **+6.144** | **8.03e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9526** | 0.4076 | ±0.8152 | **-4.790** | **1.66e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4895** | 0.4655 | ±0.9311 | **-3.200** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2234** | 0.5135 | ±1.0270 | **+4.330** | **1.49e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4361** | 0.4820 | ±0.9640 | **-11.278** | **1.69e-29** | *** |
| **Age (years)** | **-0.0504** | 0.0157 | ±0.0314 | **-3.209** | **0.0013** | ** |
| BMI (kg/m2) | -0.0151 | 0.0253 | ±0.0506 | -0.596 | 0.5509 |  |
| Hypertension | +0.1170 | 0.3784 | ±0.7567 | +0.309 | 0.7571 |  |
| High cholesterol | -0.6740 | 0.3501 | ±0.7001 | -1.925 | 0.0542 | . |
| Kidney disease | -0.2566 | 0.6681 | ±1.3361 | -0.384 | 0.7009 |  |
| Circulatory disease | +0.5625 | 0.5105 | ±1.0211 | +1.102 | 0.2706 |  |
| Mean / SD ratio | +0.1665 | 0.1387 | ±0.2773 | +1.201 | 0.2299 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.2680**, Adj R² = **0.2597**, F-statistic = **32.33** (p = **5.48e-74**), Residual SE = **5.825** on **1236** df, AIC = **7973.9**, BIC = **8050.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.9079** | 1.6352 | ±3.2705 | **+29.909** | **1.51e-196** | *** |
| **Education: graduate level (vs college)** | **+0.9907** | 0.3545 | ±0.7089 | **+2.795** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.8231 | 0.6719 | ±1.3438 | +1.225 | 0.2206 |  |
| **Site: UCSD (vs UAB)** | **+2.8428** | 0.4584 | ±0.9168 | **+6.201** | **5.60e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9532** | 0.4078 | ±0.8156 | **-4.790** | **1.67e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4879** | 0.4658 | ±0.9317 | **-3.194** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2216** | 0.5138 | ±1.0276 | **+4.324** | **1.53e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4436** | 0.4821 | ±0.9642 | **-11.292** | **1.44e-29** | *** |
| **Age (years)** | **-0.0509** | 0.0157 | ±0.0314 | **-3.237** | **0.0012** | ** |
| BMI (kg/m2) | -0.0144 | 0.0253 | ±0.0507 | -0.567 | 0.5707 |  |
| Hypertension | +0.1003 | 0.3785 | ±0.7570 | +0.265 | 0.7910 |  |
| High cholesterol | -0.6675 | 0.3502 | ±0.7004 | -1.906 | 0.0566 | . |
| Kidney disease | -0.2741 | 0.6697 | ±1.3394 | -0.409 | 0.6823 |  |
| Circulatory disease | +0.5565 | 0.5096 | ±1.0191 | +1.092 | 0.2748 |  |
| Avg. daily mean/SD | +0.0614 | 0.1212 | ±0.2423 | +0.507 | 0.6122 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1251**, R² = **0.2680**, Adj R² = **0.2597**, F-statistic = **32.32** (p = **5.65e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.0**, BIC = **8050.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.7863** | 1.5199 | ±3.0399 | **+32.755** | **2.56e-235** | *** |
| **Education: graduate level (vs college)** | **+0.9910** | 0.3544 | ±0.7089 | **+2.796** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.8310 | 0.6737 | ±1.3475 | +1.233 | 0.2174 |  |
| **Site: UCSD (vs UAB)** | **+2.8381** | 0.4600 | ±0.9200 | **+6.169** | **6.85e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9719** | 0.4075 | ±0.8150 | **-4.839** | **1.31e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4895** | 0.4660 | ±0.9320 | **-3.196** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2206** | 0.5130 | ±1.0261 | **+4.328** | **1.50e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4515** | 0.4812 | ±0.9624 | **-11.329** | **9.48e-30** | *** |
| **Age (years)** | **-0.0518** | 0.0156 | ±0.0312 | **-3.320** | **9.00e-04** | *** |
| BMI (kg/m2) | -0.0144 | 0.0253 | ±0.0507 | -0.567 | 0.5707 |  |
| Hypertension | +0.0913 | 0.3778 | ±0.7557 | +0.242 | 0.8090 |  |
| High cholesterol | -0.6712 | 0.3513 | ±0.7025 | -1.911 | 0.0560 | . |
| Kidney disease | -0.2872 | 0.6704 | ±1.3408 | -0.428 | 0.6684 |  |
| Circulatory disease | +0.5577 | 0.5090 | ±1.0180 | +1.096 | 0.2732 |  |
| MAG (mg/dL/h) | -0.0103 | 0.0215 | ±0.0430 | -0.478 | 0.6324 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **1251**, R² = **0.2682**, Adj R² = **0.2599**, F-statistic = **32.35** (p = **4.88e-74**), Residual SE = **5.824** on **1236** df, AIC = **7973.7**, BIC = **8050.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8112** | 1.4031 | ±2.8063 | **+35.500** | **4.97e-276** | *** |
| **Education: graduate level (vs college)** | **+0.9992** | 0.3544 | ±0.7087 | **+2.820** | **0.0048** | ** |
| Education: high school or below (vs college) | +0.8328 | 0.6733 | ±1.3467 | +1.237 | 0.2161 |  |
| **Site: UCSD (vs UAB)** | **+2.8365** | 0.4588 | ±0.9176 | **+6.183** | **6.30e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9517** | 0.4074 | ±0.8148 | **-4.791** | **1.66e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4966** | 0.4663 | ±0.9325 | **-3.210** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+2.2128** | 0.5137 | ±1.0274 | **+4.308** | **1.65e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4573** | 0.4816 | ±0.9632 | **-11.332** | **9.13e-30** | *** |
| **Age (years)** | **-0.0509** | 0.0157 | ±0.0314 | **-3.245** | **0.0012** | ** |
| BMI (kg/m2) | -0.0152 | 0.0253 | ±0.0506 | -0.601 | 0.5478 |  |
| Hypertension | +0.1084 | 0.3779 | ±0.7559 | +0.287 | 0.7743 |  |
| High cholesterol | -0.6678 | 0.3500 | ±0.7000 | -1.908 | 0.0564 | . |
| Kidney disease | -0.2641 | 0.6694 | ±1.3387 | -0.395 | 0.6931 |  |
| Circulatory disease | +0.5694 | 0.5087 | ±1.0174 | +1.119 | 0.2629 |  |
| Avg. daily range (mg/dL) | -0.0047 | 0.0065 | ±0.0130 | -0.724 | 0.4691 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **1251**, R² = **0.2680**, Adj R² = **0.2597**, F-statistic = **32.32** (p = **5.87e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.0**, BIC = **8051.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4737** | 1.3223 | ±2.6446 | **+37.415** | **2.23e-306** | *** |
| **Education: graduate level (vs college)** | **+0.9937** | 0.3546 | ±0.7093 | **+2.802** | **0.0051** | ** |
| Education: high school or below (vs college) | +0.8233 | 0.6707 | ±1.3414 | +1.228 | 0.2196 |  |
| **Site: UCSD (vs UAB)** | **+2.8445** | 0.4603 | ±0.9207 | **+6.179** | **6.44e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9553** | 0.4065 | ±0.8131 | **-4.810** | **1.51e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4763** | 0.4669 | ±0.9337 | **-3.162** | **0.0016** | ** |
| **Season: summer (vs autumn)** | **+2.2359** | 0.5141 | ±1.0282 | **+4.349** | **1.37e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4411** | 0.4827 | ±0.9655 | **-11.271** | **1.82e-29** | *** |
| **Age (years)** | **-0.0515** | 0.0156 | ±0.0313 | **-3.297** | **9.78e-04** | *** |
| BMI (kg/m2) | -0.0139 | 0.0254 | ±0.0508 | -0.546 | 0.5849 |  |
| Hypertension | +0.0949 | 0.3776 | ±0.7552 | +0.251 | 0.8015 |  |
| High cholesterol | -0.6596 | 0.3501 | ±0.7001 | -1.884 | 0.0595 | . |
| Kidney disease | -0.2957 | 0.6680 | ±1.3361 | -0.443 | 0.6581 |  |
| Circulatory disease | +0.5633 | 0.5100 | ±1.0200 | +1.105 | 0.2693 |  |
| SD of daily means (mg/dL) | -0.0204 | 0.0517 | ±0.1035 | -0.394 | 0.6934 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **1251**, R² = **0.2679**, Adj R² = **0.2596**, F-statistic = **32.30** (p = **6.25e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.2**, BIC = **8051.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.0289** | 2.2554 | ±4.5109 | **+21.738** | **8.95e-105** | *** |
| **Education: graduate level (vs college)** | **+0.9951** | 0.3549 | ±0.7097 | **+2.804** | **0.0050** | ** |
| Education: high school or below (vs college) | +0.8283 | 0.6731 | ±1.3463 | +1.231 | 0.2185 |  |
| **Site: UCSD (vs UAB)** | **+2.8487** | 0.4603 | ±0.9207 | **+6.188** | **6.08e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9571** | 0.4067 | ±0.8133 | **-4.813** | **1.49e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4880** | 0.4658 | ±0.9316 | **-3.194** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2228** | 0.5135 | ±1.0270 | **+4.329** | **1.50e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4479** | 0.4818 | ±0.9637 | **-11.306** | **1.22e-29** | *** |
| **Age (years)** | **-0.0515** | 0.0156 | ±0.0313 | **-3.297** | **9.79e-04** | *** |
| BMI (kg/m2) | -0.0144 | 0.0254 | ±0.0507 | -0.567 | 0.5708 |  |
| Hypertension | +0.0957 | 0.3773 | ±0.7547 | +0.254 | 0.7998 |  |
| High cholesterol | -0.6611 | 0.3498 | ±0.6996 | -1.890 | 0.0588 | . |
| Kidney disease | -0.2904 | 0.6671 | ±1.3341 | -0.435 | 0.6633 |  |
| Circulatory disease | +0.5593 | 0.5095 | ±1.0191 | +1.098 | 0.2724 |  |
| Time in range 70-180, pooled (%) | +0.0035 | 0.0187 | ±0.0373 | +0.186 | 0.8526 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **1251**, R² = **0.2679**, Adj R² = **0.2596**, F-statistic = **32.30** (p = **6.31e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.2**, BIC = **8051.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1375** | 2.2440 | ±4.4879 | **+21.898** | **2.74e-106** | *** |
| **Education: graduate level (vs college)** | **+0.9946** | 0.3549 | ±0.7097 | **+2.803** | **0.0051** | ** |
| Education: high school or below (vs college) | +0.8267 | 0.6728 | ±1.3457 | +1.229 | 0.2192 |  |
| **Site: UCSD (vs UAB)** | **+2.8504** | 0.4602 | ±0.9205 | **+6.193** | **5.90e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9572** | 0.4067 | ±0.8134 | **-4.812** | **1.49e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4868** | 0.4657 | ±0.9315 | **-3.192** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2246** | 0.5136 | ±1.0271 | **+4.332** | **1.48e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4469** | 0.4818 | ±0.9636 | **-11.305** | **1.24e-29** | *** |
| **Age (years)** | **-0.0515** | 0.0156 | ±0.0313 | **-3.297** | **9.79e-04** | *** |
| BMI (kg/m2) | -0.0144 | 0.0254 | ±0.0507 | -0.568 | 0.5698 |  |
| Hypertension | +0.0945 | 0.3774 | ±0.7549 | +0.250 | 0.8022 |  |
| High cholesterol | -0.6614 | 0.3498 | ±0.6997 | -1.891 | 0.0587 | . |
| Kidney disease | -0.2924 | 0.6673 | ±1.3345 | -0.438 | 0.6612 |  |
| Circulatory disease | +0.5578 | 0.5096 | ±1.0192 | +1.095 | 0.2737 |  |
| Avg. daily time in range 70-180 (%) | +0.0023 | 0.0185 | ±0.0369 | +0.127 | 0.8992 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.2684**, Adj R² = **0.2602**, F-statistic = **32.40** (p = **3.93e-74**), Residual SE = **5.823** on **1236** df, AIC = **7973.2**, BIC = **8050.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5546** | 1.3027 | ±2.6054 | **+38.041** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9788** | 0.3554 | ±0.7108 | **+2.754** | **0.0059** | ** |
| Education: high school or below (vs college) | +0.7800 | 0.6740 | ±1.3480 | +1.157 | 0.2472 |  |
| **Site: UCSD (vs UAB)** | **+2.8015** | 0.4620 | ±0.9239 | **+6.065** | **1.32e-09** | *** |
| **Site: UW (vs UAB)** | **-1.9802** | 0.4075 | ±0.8149 | **-4.860** | **1.17e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4869** | 0.4655 | ±0.9311 | **-3.194** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2195** | 0.5129 | ±1.0257 | **+4.328** | **1.51e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4537** | 0.4819 | ±0.9638 | **-11.317** | **1.08e-29** | *** |
| **Age (years)** | **-0.0525** | 0.0156 | ±0.0312 | **-3.367** | **7.61e-04** | *** |
| BMI (kg/m2) | -0.0136 | 0.0254 | ±0.0508 | -0.536 | 0.5920 |  |
| Hypertension | +0.0923 | 0.3780 | ±0.7560 | +0.244 | 0.8071 |  |
| High cholesterol | -0.6809 | 0.3500 | ±0.7000 | -1.945 | 0.0517 | . |
| Kidney disease | -0.2972 | 0.6697 | ±1.3394 | -0.444 | 0.6572 |  |
| Circulatory disease | +0.5862 | 0.5111 | ±1.0222 | +1.147 | 0.2514 |  |
| Any reading < 54 during wear (0/1) | -0.3568 | 0.3644 | ±0.7287 | -0.979 | 0.3274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.2696**, Adj R² = **0.2613**, F-statistic = **32.59** (p = **1.52e-74**), Residual SE = **5.819** on **1236** df, AIC = **7971.2**, BIC = **8048.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5677** | 1.2987 | ±2.5974 | **+38.167** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9825** | 0.3540 | ±0.7080 | **+2.775** | **0.0055** | ** |
| Education: high school or below (vs college) | +0.7705 | 0.6718 | ±1.3436 | +1.147 | 0.2514 |  |
| **Site: UCSD (vs UAB)** | **+2.7619** | 0.4614 | ±0.9228 | **+5.986** | **2.15e-09** | *** |
| **Site: UW (vs UAB)** | **-2.0262** | 0.4085 | ±0.8170 | **-4.960** | **7.05e-07** | *** |
| **Season: spring (vs autumn)** | **-1.4945** | 0.4651 | ±0.9302 | **-3.213** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+2.2459** | 0.5125 | ±1.0249 | **+4.383** | **1.17e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4361** | 0.4824 | ±0.9648 | **-11.269** | **1.86e-29** | *** |
| **Age (years)** | **-0.0521** | 0.0156 | ±0.0312 | **-3.338** | **8.44e-04** | *** |
| BMI (kg/m2) | -0.0150 | 0.0253 | ±0.0505 | -0.595 | 0.5518 |  |
| Hypertension | +0.0736 | 0.3783 | ±0.7566 | +0.195 | 0.8457 |  |
| **High cholesterol** | **-0.7023** | 0.3505 | ±0.7010 | **-2.004** | **0.0451** | * |
| Kidney disease | -0.2819 | 0.6671 | ±1.3341 | -0.423 | 0.6726 |  |
| Circulatory disease | +0.5512 | 0.5098 | ±1.0196 | +1.081 | 0.2796 |  |
| **Time < 54 (%)** | **-0.4995** | 0.1696 | ±0.3393 | **-2.945** | **0.0032** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.2701**, Adj R² = **0.2618**, F-statistic = **32.67** (p = **1.02e-74**), Residual SE = **5.817** on **1236** df, AIC = **7970.4**, BIC = **8047.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5255** | 1.2962 | ±2.5924 | **+38.209** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9751** | 0.3540 | ±0.7081 | **+2.754** | **0.0059** | ** |
| Education: high school or below (vs college) | +0.7629 | 0.6696 | ±1.3392 | +1.139 | 0.2546 |  |
| **Site: UCSD (vs UAB)** | **+2.7616** | 0.4607 | ±0.9214 | **+5.995** | **2.04e-09** | *** |
| **Site: UW (vs UAB)** | **-2.0475** | 0.4090 | ±0.8181 | **-5.006** | **5.57e-07** | *** |
| **Season: spring (vs autumn)** | **-1.4860** | 0.4650 | ±0.9299 | **-3.196** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2526** | 0.5128 | ±1.0256 | **+4.393** | **1.12e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4180** | 0.4827 | ±0.9653 | **-11.225** | **3.07e-29** | *** |
| **Age (years)** | **-0.0514** | 0.0156 | ±0.0312 | **-3.299** | **9.70e-04** | *** |
| BMI (kg/m2) | -0.0149 | 0.0252 | ±0.0504 | -0.591 | 0.5546 |  |
| Hypertension | +0.0594 | 0.3782 | ±0.7565 | +0.157 | 0.8753 |  |
| **High cholesterol** | **-0.7025** | 0.3501 | ±0.7002 | **-2.007** | **0.0448** | * |
| Kidney disease | -0.2795 | 0.6671 | ±1.3342 | -0.419 | 0.6752 |  |
| Circulatory disease | +0.5458 | 0.5081 | ±1.0162 | +1.074 | 0.2828 |  |
| **Avg. daily time < 54 (%)** | **-0.7639** | 0.2373 | ±0.4747 | **-3.219** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.2687**, Adj R² = **0.2605**, F-statistic = **32.45** (p = **3.05e-74**), Residual SE = **5.822** on **1236** df, AIC = **7972.7**, BIC = **8049.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5214** | 1.3031 | ±2.6062 | **+38.003** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9714** | 0.3548 | ±0.7097 | **+2.738** | **0.0062** | ** |
| Education: high school or below (vs college) | +0.7648 | 0.6726 | ±1.3452 | +1.137 | 0.2555 |  |
| **Site: UCSD (vs UAB)** | **+2.8092** | 0.4610 | ±0.9220 | **+6.093** | **1.11e-09** | *** |
| **Site: UW (vs UAB)** | **-2.0062** | 0.4087 | ±0.8173 | **-4.909** | **9.15e-07** | *** |
| **Season: spring (vs autumn)** | **-1.4775** | 0.4662 | ±0.9324 | **-3.169** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2361** | 0.5132 | ±1.0263 | **+4.358** | **1.31e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4177** | 0.4831 | ±0.9662 | **-11.214** | **3.46e-29** | *** |
| **Age (years)** | **-0.0523** | 0.0156 | ±0.0312 | **-3.346** | **8.21e-04** | *** |
| BMI (kg/m2) | -0.0136 | 0.0253 | ±0.0506 | -0.538 | 0.5907 |  |
| Hypertension | +0.0750 | 0.3784 | ±0.7567 | +0.198 | 0.8429 |  |
| High cholesterol | -0.6866 | 0.3506 | ±0.7013 | -1.958 | 0.0502 | . |
| Kidney disease | -0.2993 | 0.6701 | ±1.3402 | -0.447 | 0.6551 |  |
| Circulatory disease | +0.5546 | 0.5089 | ±1.0178 | +1.090 | 0.2758 |  |
| Time 54-69, pooled (%) | -0.1463 | 0.1007 | ±0.2014 | -1.453 | 0.1462 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1251**, R² = **0.2686**, Adj R² = **0.2603**, F-statistic = **32.42** (p = **3.46e-74**), Residual SE = **5.823** on **1236** df, AIC = **7972.9**, BIC = **8049.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4821** | 1.3020 | ±2.6039 | **+38.006** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9713** | 0.3550 | ±0.7100 | **+2.736** | **0.0062** | ** |
| Education: high school or below (vs college) | +0.7675 | 0.6722 | ±1.3443 | +1.142 | 0.2535 |  |
| **Site: UCSD (vs UAB)** | **+2.8218** | 0.4603 | ±0.9206 | **+6.130** | **8.77e-10** | *** |
| **Site: UW (vs UAB)** | **-2.0018** | 0.4085 | ±0.8171 | **-4.900** | **9.58e-07** | *** |
| **Season: spring (vs autumn)** | **-1.4778** | 0.4661 | ±0.9321 | **-3.171** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2319** | 0.5130 | ±1.0261 | **+4.350** | **1.36e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4160** | 0.4831 | ±0.9663 | **-11.210** | **3.64e-29** | *** |
| **Age (years)** | **-0.0519** | 0.0156 | ±0.0312 | **-3.328** | **8.76e-04** | *** |
| BMI (kg/m2) | -0.0137 | 0.0253 | ±0.0506 | -0.542 | 0.5878 |  |
| Hypertension | +0.0744 | 0.3783 | ±0.7566 | +0.197 | 0.8442 |  |
| High cholesterol | -0.6825 | 0.3505 | ±0.7010 | -1.947 | 0.0515 | . |
| Kidney disease | -0.2995 | 0.6698 | ±1.3397 | -0.447 | 0.6548 |  |
| Circulatory disease | +0.5539 | 0.5088 | ±1.0175 | +1.089 | 0.2763 |  |
| Avg. daily time 54-69 (%) | -0.1334 | 0.1015 | ±0.2029 | -1.315 | 0.1886 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **1251**, R² = **0.2692**, Adj R² = **0.2610**, F-statistic = **32.53** (p = **2.03e-74**), Residual SE = **5.820** on **1236** df, AIC = **7971.8**, BIC = **8048.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5782** | 1.3022 | ±2.6043 | **+38.074** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9684** | 0.3545 | ±0.7090 | **+2.732** | **0.0063** | ** |
| Education: high school or below (vs college) | +0.7499 | 0.6729 | ±1.3459 | +1.114 | 0.2651 |  |
| **Site: UCSD (vs UAB)** | **+2.7831** | 0.4619 | ±0.9238 | **+6.025** | **1.69e-09** | *** |
| **Site: UW (vs UAB)** | **-2.0257** | 0.4090 | ±0.8180 | **-4.953** | **7.31e-07** | *** |
| **Season: spring (vs autumn)** | **-1.4804** | 0.4661 | ±0.9321 | **-3.176** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2411** | 0.5132 | ±1.0263 | **+4.367** | **1.26e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4154** | 0.4833 | ±0.9665 | **-11.206** | **3.81e-29** | *** |
| **Age (years)** | **-0.0524** | 0.0156 | ±0.0312 | **-3.356** | **7.90e-04** | *** |
| BMI (kg/m2) | -0.0138 | 0.0253 | ±0.0506 | -0.545 | 0.5860 |  |
| Hypertension | +0.0698 | 0.3785 | ±0.7571 | +0.184 | 0.8538 |  |
| **High cholesterol** | **-0.6979** | 0.3508 | ±0.7016 | **-1.990** | **0.0466** | * |
| Kidney disease | -0.2950 | 0.6697 | ±1.3395 | -0.440 | 0.6596 |  |
| Circulatory disease | +0.5536 | 0.5093 | ±1.0186 | +1.087 | 0.2771 |  |
| Time < 70 (%) | -0.1448 | 0.0807 | ±0.1614 | -1.794 | 0.0727 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **1251**, R² = **0.2691**, Adj R² = **0.2608**, F-statistic = **32.50** (p = **2.36e-74**), Residual SE = **5.821** on **1236** df, AIC = **7972.1**, BIC = **8049.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5196** | 1.3005 | ±2.6010 | **+38.077** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9664** | 0.3547 | ±0.7095 | **+2.724** | **0.0064** | ** |
| Education: high school or below (vs college) | +0.7524 | 0.6719 | ±1.3438 | +1.120 | 0.2628 |  |
| **Site: UCSD (vs UAB)** | **+2.8025** | 0.4608 | ±0.9216 | **+6.082** | **1.19e-09** | *** |
| **Site: UW (vs UAB)** | **-2.0217** | 0.4089 | ±0.8178 | **-4.944** | **7.65e-07** | *** |
| **Season: spring (vs autumn)** | **-1.4775** | 0.4661 | ±0.9321 | **-3.170** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2366** | 0.5131 | ±1.0262 | **+4.359** | **1.31e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4090** | 0.4834 | ±0.9669 | **-11.189** | **4.62e-29** | *** |
| **Age (years)** | **-0.0519** | 0.0156 | ±0.0312 | **-3.330** | **8.69e-04** | *** |
| BMI (kg/m2) | -0.0137 | 0.0253 | ±0.0505 | -0.543 | 0.5869 |  |
| Hypertension | +0.0670 | 0.3784 | ±0.7569 | +0.177 | 0.8594 |  |
| **High cholesterol** | **-0.6913** | 0.3505 | ±0.7010 | **-1.972** | **0.0486** | * |
| Kidney disease | -0.2965 | 0.6697 | ±1.3395 | -0.443 | 0.6580 |  |
| Circulatory disease | +0.5521 | 0.5088 | ±1.0175 | +1.085 | 0.2778 |  |
| Avg. daily time < 70 (%) | -0.1423 | 0.0878 | ±0.1755 | -1.622 | 0.1048 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.2683**, Adj R² = **0.2600**, F-statistic = **32.37** (p = **4.55e-74**), Residual SE = **5.824** on **1236** df, AIC = **7973.5**, BIC = **8050.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.1276** | 2.8954 | ±5.7908 | **+18.003** | **1.83e-72** | *** |
| **Education: graduate level (vs college)** | **+0.9918** | 0.3544 | ±0.7088 | **+2.798** | **0.0051** | ** |
| Education: high school or below (vs college) | +0.7862 | 0.6756 | ±1.3513 | +1.164 | 0.2446 |  |
| **Site: UCSD (vs UAB)** | **+2.8657** | 0.4586 | ±0.9171 | **+6.249** | **4.13e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9496** | 0.4071 | ±0.8143 | **-4.788** | **1.68e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4797** | 0.4652 | ±0.9305 | **-3.180** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2433** | 0.5132 | ±1.0264 | **+4.371** | **1.24e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4406** | 0.4816 | ±0.9632 | **-11.297** | **1.37e-29** | *** |
| **Age (years)** | **-0.0514** | 0.0156 | ±0.0313 | **-3.289** | **0.0010** | ** |
| BMI (kg/m2) | -0.0146 | 0.0253 | ±0.0507 | -0.575 | 0.5651 |  |
| Hypertension | +0.0893 | 0.3773 | ±0.7546 | +0.237 | 0.8130 |  |
| High cholesterol | -0.6571 | 0.3498 | ±0.6996 | -1.879 | 0.0603 | . |
| Kidney disease | -0.3022 | 0.6696 | ±1.3391 | -0.451 | 0.6518 |  |
| Circulatory disease | +0.5261 | 0.5089 | ±1.0178 | +1.034 | 0.3012 |  |
| Time 54-250, pooled (%) | -0.0279 | 0.0264 | ±0.0528 | -1.059 | 0.2897 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.2683**, Adj R² = **0.2600**, F-statistic = **32.38** (p = **4.34e-74**), Residual SE = **5.824** on **1236** df, AIC = **7973.4**, BIC = **8050.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.3934** | 2.9246 | ±5.8493 | **+17.915** | **9.08e-72** | *** |
| **Education: graduate level (vs college)** | **+0.9917** | 0.3544 | ±0.7088 | **+2.798** | **0.0051** | ** |
| Education: high school or below (vs college) | +0.7821 | 0.6759 | ±1.3519 | +1.157 | 0.2472 |  |
| **Site: UCSD (vs UAB)** | **+2.8650** | 0.4584 | ±0.9169 | **+6.250** | **4.12e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9499** | 0.4071 | ±0.8142 | **-4.790** | **1.67e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4795** | 0.4652 | ±0.9304 | **-3.180** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2447** | 0.5133 | ±1.0265 | **+4.373** | **1.22e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4401** | 0.4816 | ±0.9633 | **-11.295** | **1.39e-29** | *** |
| **Age (years)** | **-0.0514** | 0.0156 | ±0.0313 | **-3.291** | **9.99e-04** | *** |
| BMI (kg/m2) | -0.0146 | 0.0253 | ±0.0507 | -0.578 | 0.5631 |  |
| Hypertension | +0.0892 | 0.3773 | ±0.7546 | +0.236 | 0.8132 |  |
| High cholesterol | -0.6572 | 0.3498 | ±0.6996 | -1.879 | 0.0602 | . |
| Kidney disease | -0.3017 | 0.6695 | ±1.3391 | -0.451 | 0.6523 |  |
| Circulatory disease | +0.5237 | 0.5091 | ±1.0182 | +1.029 | 0.3036 |  |
| Avg. daily time 54-250 (%) | -0.0305 | 0.0267 | ±0.0534 | -1.145 | 0.2522 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.2681**, Adj R² = **0.2598**, F-statistic = **32.34** (p = **5.14e-74**), Residual SE = **5.824** on **1236** df, AIC = **7973.8**, BIC = **8050.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3750** | 1.2995 | ±2.5990 | **+37.995** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+1.0031** | 0.3551 | ±0.7102 | **+2.825** | **0.0047** | ** |
| Education: high school or below (vs college) | +0.8303 | 0.6714 | ±1.3428 | +1.237 | 0.2162 |  |
| **Site: UCSD (vs UAB)** | **+2.8423** | 0.4586 | ±0.9172 | **+6.197** | **5.74e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9459** | 0.4067 | ±0.8134 | **-4.785** | **1.71e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4981** | 0.4653 | ±0.9307 | **-3.219** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+2.2069** | 0.5130 | ±1.0261 | **+4.302** | **1.70e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4606** | 0.4819 | ±0.9638 | **-11.331** | **9.20e-30** | *** |
| **Age (years)** | **-0.0512** | 0.0156 | ±0.0313 | **-3.274** | **0.0011** | ** |
| BMI (kg/m2) | -0.0139 | 0.0254 | ±0.0508 | -0.546 | 0.5852 |  |
| Hypertension | +0.1106 | 0.3775 | ±0.7551 | +0.293 | 0.7695 |  |
| High cholesterol | -0.6488 | 0.3495 | ±0.6990 | -1.857 | 0.0634 | . |
| Kidney disease | -0.2673 | 0.6639 | ±1.3279 | -0.403 | 0.6873 |  |
| Circulatory disease | +0.5600 | 0.5083 | ±1.0165 | +1.102 | 0.2706 |  |
| Time 181-250, pooled (%) | -0.0181 | 0.0278 | ±0.0556 | -0.649 | 0.5163 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1251**, R² = **0.2681**, Adj R² = **0.2598**, F-statistic = **32.34** (p = **5.26e-74**), Residual SE = **5.825** on **1236** df, AIC = **7973.8**, BIC = **8050.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3738** | 1.2996 | ±2.5992 | **+37.991** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+1.0028** | 0.3551 | ±0.7102 | **+2.824** | **0.0047** | ** |
| Education: high school or below (vs college) | +0.8283 | 0.6712 | ±1.3425 | +1.234 | 0.2172 |  |
| **Site: UCSD (vs UAB)** | **+2.8417** | 0.4588 | ±0.9176 | **+6.194** | **5.88e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9477** | 0.4066 | ±0.8132 | **-4.790** | **1.67e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4961** | 0.4653 | ±0.9305 | **-3.216** | **0.0013** | ** |
| **Season: summer (vs autumn)** | **+2.2085** | 0.5130 | ±1.0260 | **+4.305** | **1.67e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4596** | 0.4819 | ±0.9637 | **-11.330** | **9.32e-30** | *** |
| **Age (years)** | **-0.0513** | 0.0156 | ±0.0313 | **-3.278** | **0.0010** | ** |
| BMI (kg/m2) | -0.0139 | 0.0254 | ±0.0508 | -0.546 | 0.5852 |  |
| Hypertension | +0.1094 | 0.3776 | ±0.7552 | +0.290 | 0.7721 |  |
| High cholesterol | -0.6495 | 0.3496 | ±0.6992 | -1.858 | 0.0632 | . |
| Kidney disease | -0.2684 | 0.6641 | ±1.3283 | -0.404 | 0.6861 |  |
| Circulatory disease | +0.5599 | 0.5083 | ±1.0166 | +1.102 | 0.2707 |  |
| Avg. daily time 181-250 (%) | -0.0168 | 0.0274 | ±0.0547 | -0.615 | 0.5383 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **1251**, R² = **0.2679**, Adj R² = **0.2596**, F-statistic = **32.30** (p = **6.31e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.2**, BIC = **8051.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3634** | 1.3010 | ±2.6019 | **+37.943** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9923** | 0.3551 | ±0.7101 | **+2.795** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.8199 | 0.6741 | ±1.3482 | +1.216 | 0.2239 |  |
| **Site: UCSD (vs UAB)** | **+2.8553** | 0.4592 | ±0.9184 | **+6.218** | **5.03e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9582** | 0.4065 | ±0.8129 | **-4.818** | **1.45e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4830** | 0.4659 | ±0.9317 | **-3.183** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2324** | 0.5138 | ±1.0275 | **+4.345** | **1.39e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4427** | 0.4819 | ±0.9638 | **-11.295** | **1.39e-29** | *** |
| **Age (years)** | **-0.0516** | 0.0156 | ±0.0313 | **-3.298** | **9.74e-04** | *** |
| BMI (kg/m2) | -0.0146 | 0.0254 | ±0.0507 | -0.576 | 0.5643 |  |
| Hypertension | +0.0897 | 0.3775 | ±0.7551 | +0.238 | 0.8122 |  |
| High cholesterol | -0.6638 | 0.3498 | ±0.6996 | -1.898 | 0.0577 | . |
| Kidney disease | -0.3006 | 0.6679 | ±1.3358 | -0.450 | 0.6527 |  |
| Circulatory disease | +0.5519 | 0.5095 | ±1.0190 | +1.083 | 0.2787 |  |
| Time > 180 (%) | +0.0022 | 0.0182 | ±0.0364 | +0.119 | 0.9054 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.2679**, Adj R² = **0.2596**, F-statistic = **32.30** (p = **6.29e-74**), Residual SE = **5.825** on **1236** df, AIC = **7974.2**, BIC = **8051.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3632** | 1.3011 | ±2.6021 | **+37.941** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9919** | 0.3551 | ±0.7102 | **+2.794** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.8194 | 0.6737 | ±1.3474 | +1.216 | 0.2239 |  |
| **Site: UCSD (vs UAB)** | **+2.8559** | 0.4593 | ±0.9187 | **+6.218** | **5.05e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9583** | 0.4065 | ±0.8130 | **-4.818** | **1.45e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4828** | 0.4658 | ±0.9316 | **-3.183** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2332** | 0.5137 | ±1.0275 | **+4.347** | **1.38e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4422** | 0.4819 | ±0.9637 | **-11.294** | **1.40e-29** | *** |
| **Age (years)** | **-0.0516** | 0.0156 | ±0.0313 | **-3.299** | **9.72e-04** | *** |
| BMI (kg/m2) | -0.0146 | 0.0254 | ±0.0507 | -0.578 | 0.5636 |  |
| Hypertension | +0.0892 | 0.3776 | ±0.7552 | +0.236 | 0.8132 |  |
| High cholesterol | -0.6641 | 0.3499 | ±0.6997 | -1.898 | 0.0577 | . |
| Kidney disease | -0.3014 | 0.6680 | ±1.3360 | -0.451 | 0.6518 |  |
| Circulatory disease | +0.5513 | 0.5095 | ±1.0191 | +1.082 | 0.2793 |  |
| Avg. daily time > 180 (%) | +0.0026 | 0.0181 | ±0.0361 | +0.144 | 0.8858 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.2682**, Adj R² = **0.2599**, F-statistic = **32.36** (p = **4.78e-74**), Residual SE = **5.824** on **1236** df, AIC = **7973.6**, BIC = **8050.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3779** | 1.3025 | ±2.6049 | **+37.911** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9926** | 0.3546 | ±0.7091 | **+2.799** | **0.0051** | ** |
| Education: high school or below (vs college) | +0.8006 | 0.6728 | ±1.3456 | +1.190 | 0.2341 |  |
| **Site: UCSD (vs UAB)** | **+2.8619** | 0.4583 | ±0.9166 | **+6.245** | **4.25e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9611** | 0.4066 | ±0.8133 | **-4.823** | **1.42e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4850** | 0.4652 | ±0.9305 | **-3.192** | **0.0014** | ** |
| **Season: summer (vs autumn)** | **+2.2490** | 0.5125 | ±1.0250 | **+4.388** | **1.14e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4417** | 0.4815 | ±0.9631 | **-11.300** | **1.31e-29** | *** |
| **Age (years)** | **-0.0514** | 0.0156 | ±0.0313 | **-3.289** | **0.0010** | ** |
| BMI (kg/m2) | -0.0161 | 0.0255 | ±0.0510 | -0.633 | 0.5267 |  |
| Hypertension | +0.0839 | 0.3777 | ±0.7554 | +0.222 | 0.8243 |  |
| High cholesterol | -0.6757 | 0.3501 | ±0.7003 | -1.930 | 0.0536 | . |
| Kidney disease | -0.2960 | 0.6710 | ±1.3420 | -0.441 | 0.6592 |  |
| Circulatory disease | +0.5466 | 0.5086 | ±1.0172 | +1.075 | 0.2825 |  |
| Nocturnal time > 180 (%) | +0.0150 | 0.0162 | ±0.0325 | +0.923 | 0.3562 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.2685**, Adj R² = **0.2602**, F-statistic = **32.41** (p = **3.72e-74**), Residual SE = **5.823** on **1236** df, AIC = **7973.1**, BIC = **8050.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4902** | 1.2966 | ±2.5932 | **+38.169** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9902** | 0.3543 | ±0.7087 | **+2.794** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.8223 | 0.6712 | ±1.3423 | +1.225 | 0.2205 |  |
| **Site: UCSD (vs UAB)** | **+2.8439** | 0.4577 | ±0.9154 | **+6.214** | **5.17e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9496** | 0.4068 | ±0.8135 | **-4.793** | **1.64e-06** | *** |
| **Season: spring (vs autumn)** | **-1.5110** | 0.4656 | ±0.9312 | **-3.245** | **0.0012** | ** |
| **Season: summer (vs autumn)** | **+2.2078** | 0.5137 | ±1.0274 | **+4.298** | **1.72e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4663** | 0.4815 | ±0.9629 | **-11.354** | **7.11e-30** | *** |
| **Age (years)** | **-0.0512** | 0.0156 | ±0.0313 | **-3.275** | **0.0011** | ** |
| BMI (kg/m2) | -0.0165 | 0.0254 | ±0.0507 | -0.650 | 0.5156 |  |
| Hypertension | +0.1186 | 0.3772 | ±0.7543 | +0.314 | 0.7532 |  |
| High cholesterol | -0.6550 | 0.3495 | ±0.6991 | -1.874 | 0.0609 | . |
| Kidney disease | -0.2860 | 0.6665 | ±1.3330 | -0.429 | 0.6679 |  |
| Circulatory disease | +0.5512 | 0.5099 | ±1.0198 | +1.081 | 0.2797 |  |
| Any reading > 250 during wear (0/1) | -0.4415 | 0.4291 | ±0.8581 | -1.029 | 0.3035 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.2685**, Adj R² = **0.2602**, F-statistic = **32.40** (p = **3.78e-74**), Residual SE = **5.823** on **1236** df, AIC = **7973.1**, BIC = **8050.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3389** | 1.3017 | ±2.6033 | **+37.904** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9906** | 0.3543 | ±0.7086 | **+2.796** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.7729 | 0.6761 | ±1.3521 | +1.143 | 0.2529 |  |
| **Site: UCSD (vs UAB)** | **+2.8624** | 0.4581 | ±0.9162 | **+6.249** | **4.14e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9525** | 0.4068 | ±0.8137 | **-4.799** | **1.59e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4790** | 0.4651 | ±0.9303 | **-3.180** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2482** | 0.5133 | ±1.0265 | **+4.380** | **1.19e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4389** | 0.4816 | ±0.9632 | **-11.293** | **1.42e-29** | *** |
| **Age (years)** | **-0.0514** | 0.0156 | ±0.0313 | **-3.288** | **0.0010** | ** |
| BMI (kg/m2) | -0.0146 | 0.0253 | ±0.0506 | -0.577 | 0.5638 |  |
| Hypertension | +0.0872 | 0.3773 | ±0.7545 | +0.231 | 0.8172 |  |
| High cholesterol | -0.6585 | 0.3498 | ±0.6996 | -1.883 | 0.0598 | . |
| Kidney disease | -0.3025 | 0.6697 | ±1.3394 | -0.452 | 0.6515 |  |
| Circulatory disease | +0.5186 | 0.5091 | ±1.0181 | +1.019 | 0.3083 |  |
| Time > 250 (%) | +0.0350 | 0.0257 | ±0.0513 | +1.365 | 0.1722 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.2685**, Adj R² = **0.2602**, F-statistic = **32.41** (p = **3.68e-74**), Residual SE = **5.823** on **1236** df, AIC = **7973.1**, BIC = **8050.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3412** | 1.3016 | ±2.6032 | **+37.908** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.9904** | 0.3543 | ±0.7086 | **+2.795** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.7709 | 0.6761 | ±1.3522 | +1.140 | 0.2542 |  |
| **Site: UCSD (vs UAB)** | **+2.8629** | 0.4581 | ±0.9161 | **+6.250** | **4.10e-10** | *** |
| **Site: UW (vs UAB)** | **-1.9528** | 0.4068 | ±0.8136 | **-4.800** | **1.58e-06** | *** |
| **Season: spring (vs autumn)** | **-1.4784** | 0.4651 | ±0.9302 | **-3.179** | **0.0015** | ** |
| **Season: summer (vs autumn)** | **+2.2491** | 0.5133 | ±1.0266 | **+4.382** | **1.18e-05** | *** |
| **Season: winter (vs autumn)** | **-5.4378** | 0.4816 | ±0.9632 | **-11.291** | **1.46e-29** | *** |
| **Age (years)** | **-0.0514** | 0.0156 | ±0.0313 | **-3.289** | **0.0010** | ** |
| BMI (kg/m2) | -0.0147 | 0.0253 | ±0.0506 | -0.580 | 0.5619 |  |
| Hypertension | +0.0870 | 0.3773 | ±0.7545 | +0.231 | 0.8177 |  |
| High cholesterol | -0.6581 | 0.3498 | ±0.6996 | -1.881 | 0.0599 | . |
| Kidney disease | -0.3019 | 0.6697 | ±1.3394 | -0.451 | 0.6521 |  |
| Circulatory disease | +0.5171 | 0.5091 | ±1.0181 | +1.016 | 0.3097 |  |
| Avg. daily time > 250 (%) | +0.0366 | 0.0262 | ±0.0524 | +1.399 | 0.1619 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 1,251; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **1251**, R² = **0.0347**, Adj R² = **0.0245**, F-statistic = **3.42** (p = **3.26e-05**), Residual SE = **15.223** on **1237** df, AIC = **10376.5**, BIC = **10448.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.9972** | 3.5527 | ±7.1054 | **+35.184** | **3.53e-271** | *** |
| Education: graduate level (vs college) | -0.6569 | 0.9007 | ±1.8015 | -0.729 | 0.4658 |  |
| **Education: high school or below (vs college)** | **+4.3279** | 1.8802 | ±3.7605 | **+2.302** | **0.0213** | * |
| Site: UCSD (vs UAB) | +1.5135 | 1.2170 | ±2.4339 | +1.244 | 0.2136 |  |
| Site: UW (vs UAB) | -0.9535 | 1.0779 | ±2.1557 | -0.885 | 0.3764 |  |
| **Season: spring (vs autumn)** | **+2.8007** | 1.1677 | ±2.3355 | **+2.398** | **0.0165** | * |
| Season: summer (vs autumn) | +1.1537 | 1.3383 | ±2.6766 | +0.862 | 0.3886 |  |
| **Season: winter (vs autumn)** | **+3.2236** | 1.2255 | ±2.4509 | **+2.631** | **0.0085** | ** |
| **Age (years)** | **-0.1015** | 0.0419 | ±0.0839 | **-2.419** | **0.0156** | * |
| **BMI (kg/m2)** | **+0.1750** | 0.0634 | ±0.1268 | **+2.761** | **0.0058** | ** |
| Hypertension | +1.2082 | 0.9767 | ±1.9534 | +1.237 | 0.2161 |  |
| High cholesterol | -0.8229 | 0.9093 | ±1.8185 | -0.905 | 0.3655 |  |
| Kidney disease | -1.0302 | 1.5982 | ±3.1963 | -0.645 | 0.5192 |  |
| Circulatory disease | +0.4514 | 1.3648 | ±2.7296 | +0.331 | 0.7408 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **1251**, R² = **0.0357**, Adj R² = **0.0248**, F-statistic = **3.27** (p = **3.80e-05**), Residual SE = **15.221** on **1236** df, AIC = **10377.2**, BIC = **10454.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.9258** | 5.2340 | ±10.4680 | **+24.824** | **5.00e-136** | *** |
| Education: graduate level (vs college) | -0.6473 | 0.9005 | ±1.8009 | -0.719 | 0.4723 |  |
| **Education: high school or below (vs college)** | **+4.4821** | 1.8717 | ±3.7433 | **+2.395** | **0.0166** | * |
| Site: UCSD (vs UAB) | +1.5353 | 1.2174 | ±2.4347 | +1.261 | 0.2072 |  |
| Site: UW (vs UAB) | -0.9133 | 1.0781 | ±2.1562 | -0.847 | 0.3969 |  |
| **Season: spring (vs autumn)** | **+2.6788** | 1.1758 | ±2.3516 | **+2.278** | **0.0227** | * |
| Season: summer (vs autumn) | +1.1137 | 1.3415 | ±2.6830 | +0.830 | 0.4064 |  |
| **Season: winter (vs autumn)** | **+3.1732** | 1.2264 | ±2.4529 | **+2.587** | **0.0097** | ** |
| **Age (years)** | **-0.0973** | 0.0421 | ±0.0843 | **-2.307** | **0.0210** | * |
| **BMI (kg/m2)** | **+0.1817** | 0.0635 | ±0.1271 | **+2.860** | **0.0042** | ** |
| Hypertension | +1.2642 | 0.9792 | ±1.9583 | +1.291 | 0.1967 |  |
| High cholesterol | -0.7173 | 0.9138 | ±1.8276 | -0.785 | 0.4324 |  |
| Kidney disease | -1.0333 | 1.6034 | ±3.2069 | -0.644 | 0.5193 |  |
| Circulatory disease | +0.5194 | 1.3634 | ±2.7267 | +0.381 | 0.7032 |  |
| HbA1c (%) | -0.9585 | 0.7502 | ±1.5004 | -1.278 | 0.2013 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **1251**, R² = **0.0359**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.43e-05**), Residual SE = **15.219** on **1236** df, AIC = **10376.9**, BIC = **10453.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+128.2056** | 4.2975 | ±8.5950 | **+29.833** | **1.47e-195** | *** |
| Education: graduate level (vs college) | -0.5895 | 0.9009 | ±1.8018 | -0.654 | 0.5129 |  |
| **Education: high school or below (vs college)** | **+4.4986** | 1.8832 | ±3.7664 | **+2.389** | **0.0169** | * |
| Site: UCSD (vs UAB) | +1.4877 | 1.2178 | ±2.4356 | +1.222 | 0.2219 |  |
| Site: UW (vs UAB) | -0.8679 | 1.0751 | ±2.1501 | -0.807 | 0.4195 |  |
| **Season: spring (vs autumn)** | **+2.7484** | 1.1681 | ±2.3362 | **+2.353** | **0.0186** | * |
| Season: summer (vs autumn) | +1.0712 | 1.3404 | ±2.6808 | +0.799 | 0.4242 |  |
| **Season: winter (vs autumn)** | **+3.1364** | 1.2236 | ±2.4472 | **+2.563** | **0.0104** | * |
| **Age (years)** | **-0.0994** | 0.0421 | ±0.0841 | **-2.363** | **0.0182** | * |
| **BMI (kg/m2)** | **+0.1790** | 0.0633 | ±0.1266 | **+2.827** | **0.0047** | ** |
| Hypertension | +1.3105 | 0.9807 | ±1.9613 | +1.336 | 0.1814 |  |
| High cholesterol | -0.7652 | 0.9086 | ±1.8173 | -0.842 | 0.3997 |  |
| Kidney disease | -0.9357 | 1.6005 | ±3.2011 | -0.585 | 0.5588 |  |
| Circulatory disease | +0.5332 | 1.3655 | ±2.7309 | +0.390 | 0.6962 |  |
| Mean glucose (mg/dL) | -0.0292 | 0.0220 | ±0.0440 | -1.328 | 0.1843 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **1251**, R² = **0.0359**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.43e-05**), Residual SE = **15.219** on **1236** df, AIC = **10376.9**, BIC = **10453.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.2493** | 6.5171 | ±13.0343 | **+20.292** | **1.50e-91** | *** |
| Education: graduate level (vs college) | -0.5895 | 0.9009 | ±1.8018 | -0.654 | 0.5129 |  |
| **Education: high school or below (vs college)** | **+4.4986** | 1.8832 | ±3.7664 | **+2.389** | **0.0169** | * |
| Site: UCSD (vs UAB) | +1.4877 | 1.2178 | ±2.4356 | +1.222 | 0.2219 |  |
| Site: UW (vs UAB) | -0.8679 | 1.0751 | ±2.1501 | -0.807 | 0.4195 |  |
| **Season: spring (vs autumn)** | **+2.7484** | 1.1681 | ±2.3362 | **+2.353** | **0.0186** | * |
| Season: summer (vs autumn) | +1.0712 | 1.3404 | ±2.6808 | +0.799 | 0.4242 |  |
| **Season: winter (vs autumn)** | **+3.1364** | 1.2236 | ±2.4472 | **+2.563** | **0.0104** | * |
| **Age (years)** | **-0.0994** | 0.0421 | ±0.0841 | **-2.363** | **0.0182** | * |
| **BMI (kg/m2)** | **+0.1790** | 0.0633 | ±0.1266 | **+2.827** | **0.0047** | ** |
| Hypertension | +1.3105 | 0.9807 | ±1.9613 | +1.336 | 0.1814 |  |
| High cholesterol | -0.7652 | 0.9086 | ±1.8173 | -0.842 | 0.3997 |  |
| Kidney disease | -0.9357 | 1.6005 | ±3.2011 | -0.585 | 0.5588 |  |
| Circulatory disease | +0.5332 | 1.3655 | ±2.7309 | +0.390 | 0.6962 |  |
| GMI (%) | -1.2216 | 0.9202 | ±1.8404 | -1.328 | 0.1843 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **1251**, R² = **0.0354**, Adj R² = **0.0244**, F-statistic = **3.24** (p = **4.56e-05**), Residual SE = **15.224** on **1236** df, AIC = **10377.6**, BIC = **10454.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.1816** | 4.2313 | ±8.4626 | **+30.057** | **1.74e-198** | *** |
| Education: graduate level (vs college) | -0.6240 | 0.9005 | ±1.8009 | -0.693 | 0.4883 |  |
| **Education: high school or below (vs college)** | **+4.4463** | 1.8796 | ±3.7592 | **+2.366** | **0.0180** | * |
| Site: UCSD (vs UAB) | +1.5254 | 1.2183 | ±2.4367 | +1.252 | 0.2105 |  |
| Site: UW (vs UAB) | -0.8989 | 1.0746 | ±2.1491 | -0.837 | 0.4029 |  |
| **Season: spring (vs autumn)** | **+2.7959** | 1.1689 | ±2.3379 | **+2.392** | **0.0168** | * |
| Season: summer (vs autumn) | +1.1002 | 1.3384 | ±2.6768 | +0.822 | 0.4111 |  |
| **Season: winter (vs autumn)** | **+3.1944** | 1.2249 | ±2.4499 | **+2.608** | **0.0091** | ** |
| **Age (years)** | **-0.1020** | 0.0420 | ±0.0841 | **-2.427** | **0.0152** | * |
| **BMI (kg/m2)** | **+0.1830** | 0.0637 | ±0.1273 | **+2.874** | **0.0040** | ** |
| Hypertension | +1.2673 | 0.9810 | ±1.9619 | +1.292 | 0.1964 |  |
| High cholesterol | -0.7672 | 0.9089 | ±1.8179 | -0.844 | 0.3987 |  |
| Kidney disease | -1.0203 | 1.5987 | ±3.1975 | -0.638 | 0.5234 |  |
| Circulatory disease | +0.4885 | 1.3654 | ±2.7309 | +0.358 | 0.7205 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0205 | 0.0210 | ±0.0419 | -0.977 | 0.3287 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.0366**, Adj R² = **0.0256**, F-statistic = **3.35** (p = **2.55e-05**), Residual SE = **15.214** on **1236** df, AIC = **10376.1**, BIC = **10453.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.9324** | 3.6978 | ±7.3955 | **+34.327** | **3.13e-258** | *** |
| Education: graduate level (vs college) | -0.6405 | 0.9004 | ±1.8008 | -0.711 | 0.4768 |  |
| **Education: high school or below (vs college)** | **+4.3607** | 1.8845 | ±3.7690 | **+2.314** | **0.0207** | * |
| Site: UCSD (vs UAB) | +1.4157 | 1.2222 | ±2.4444 | +1.158 | 0.2467 |  |
| Site: UW (vs UAB) | -0.9026 | 1.0754 | ±2.1508 | -0.839 | 0.4013 |  |
| **Season: spring (vs autumn)** | **+2.7355** | 1.1684 | ±2.3368 | **+2.341** | **0.0192** | * |
| Season: summer (vs autumn) | +1.0885 | 1.3409 | ±2.6818 | +0.812 | 0.4169 |  |
| **Season: winter (vs autumn)** | **+3.1635** | 1.2242 | ±2.4485 | **+2.584** | **0.0098** | ** |
| **Age (years)** | **-0.0974** | 0.0424 | ±0.0847 | **-2.299** | **0.0215** | * |
| **BMI (kg/m2)** | **+0.1762** | 0.0631 | ±0.1262 | **+2.792** | **0.0052** | ** |
| Hypertension | +1.3374 | 0.9818 | ±1.9636 | +1.362 | 0.1731 |  |
| High cholesterol | -0.8251 | 0.9076 | ±1.8151 | -0.909 | 0.3633 |  |
| Kidney disease | -0.8177 | 1.5999 | ±3.1999 | -0.511 | 0.6093 |  |
| Circulatory disease | +0.5424 | 1.3637 | ±2.7274 | +0.398 | 0.6908 |  |
| Glucose SD, pooled (mg/dL) | -0.1035 | 0.0663 | ±0.1326 | -1.560 | 0.1187 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.0368**, Adj R² = **0.0259**, F-statistic = **3.37** (p = **2.27e-05**), Residual SE = **15.212** on **1236** df, AIC = **10375.8**, BIC = **10452.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.9093** | 3.6496 | ±7.2992 | **+34.774** | **6.11e-265** | *** |
| Education: graduate level (vs college) | -0.6280 | 0.9003 | ±1.8006 | -0.697 | 0.4855 |  |
| **Education: high school or below (vs college)** | **+4.3679** | 1.8845 | ±3.7690 | **+2.318** | **0.0205** | * |
| Site: UCSD (vs UAB) | +1.4207 | 1.2197 | ±2.4394 | +1.165 | 0.2441 |  |
| Site: UW (vs UAB) | -0.8884 | 1.0753 | ±2.1506 | -0.826 | 0.4087 |  |
| **Season: spring (vs autumn)** | **+2.7156** | 1.1683 | ±2.3366 | **+2.324** | **0.0201** | * |
| Season: summer (vs autumn) | +1.0624 | 1.3413 | ±2.6826 | +0.792 | 0.4283 |  |
| **Season: winter (vs autumn)** | **+3.1414** | 1.2247 | ±2.4494 | **+2.565** | **0.0103** | * |
| **Age (years)** | **-0.0966** | 0.0425 | ±0.0850 | **-2.272** | **0.0231** | * |
| **BMI (kg/m2)** | **+0.1776** | 0.0631 | ±0.1261 | **+2.817** | **0.0049** | ** |
| Hypertension | +1.3424 | 0.9804 | ±1.9607 | +1.369 | 0.1709 |  |
| High cholesterol | -0.8198 | 0.9075 | ±1.8151 | -0.903 | 0.3664 |  |
| Kidney disease | -0.7917 | 1.5971 | ±3.1942 | -0.496 | 0.6201 |  |
| Circulatory disease | +0.5427 | 1.3628 | ±2.7256 | +0.398 | 0.6905 |  |
| Avg. daily SD (mg/dL) | -0.1174 | 0.0724 | ±0.1447 | -1.622 | 0.1049 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **1251**, R² = **0.0359**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.53e-05**), Residual SE = **15.219** on **1236** df, AIC = **10377.0**, BIC = **10453.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.2596** | 3.8730 | ±7.7461 | **+32.858** | **8.81e-237** | *** |
| Education: graduate level (vs college) | -0.6886 | 0.9016 | ±1.8033 | -0.764 | 0.4450 |  |
| **Education: high school or below (vs college)** | **+4.2538** | 1.8926 | ±3.7852 | **+2.248** | **0.0246** | * |
| Site: UCSD (vs UAB) | +1.4203 | 1.2246 | ±2.4493 | +1.160 | 0.2461 |  |
| Site: UW (vs UAB) | -0.9665 | 1.0774 | ±2.1549 | -0.897 | 0.3697 |  |
| **Season: spring (vs autumn)** | **+2.7679** | 1.1681 | ±2.3362 | **+2.370** | **0.0178** | * |
| Season: summer (vs autumn) | +1.1471 | 1.3396 | ±2.6792 | +0.856 | 0.3918 |  |
| **Season: winter (vs autumn)** | **+3.2284** | 1.2242 | ±2.4484 | **+2.637** | **0.0084** | ** |
| **Age (years)** | **-0.0983** | 0.0423 | ±0.0847 | **-2.323** | **0.0202** | * |
| **BMI (kg/m2)** | **+0.1736** | 0.0633 | ±0.1266 | **+2.742** | **0.0061** | ** |
| Hypertension | +1.2684 | 0.9788 | ±1.9577 | +1.296 | 0.1950 |  |
| High cholesterol | -0.8704 | 0.9079 | ±1.8158 | -0.959 | 0.3377 |  |
| Kidney disease | -0.8881 | 1.5976 | ±3.1951 | -0.556 | 0.5783 |  |
| Circulatory disease | +0.4816 | 1.3639 | ±2.7277 | +0.353 | 0.7240 |  |
| CV (%) | -0.1329 | 0.1042 | ±0.2085 | -1.275 | 0.2024 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1251**, R² = **0.0364**, Adj R² = **0.0255**, F-statistic = **3.34** (p = **2.73e-05**), Residual SE = **15.215** on **1236** df, AIC = **10376.3**, BIC = **10453.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+121.7431** | 4.2786 | ±8.5572 | **+28.454** | **4.37e-178** | *** |
| Education: graduate level (vs college) | -0.6997 | 0.9015 | ±1.8029 | -0.776 | 0.4376 |  |
| **Education: high school or below (vs college)** | **+4.2898** | 1.8895 | ±3.7791 | **+2.270** | **0.0232** | * |
| Site: UCSD (vs UAB) | +1.4136 | 1.2246 | ±2.4493 | +1.154 | 0.2484 |  |
| Site: UW (vs UAB) | -0.9392 | 1.0760 | ±2.1520 | -0.873 | 0.3827 |  |
| **Season: spring (vs autumn)** | **+2.7863** | 1.1679 | ±2.3357 | **+2.386** | **0.0170** | * |
| Season: summer (vs autumn) | +1.1371 | 1.3395 | ±2.6791 | +0.849 | 0.3959 |  |
| **Season: winter (vs autumn)** | **+3.2518** | 1.2234 | ±2.4469 | **+2.658** | **0.0079** | ** |
| **Age (years)** | **-0.0978** | 0.0423 | ±0.0846 | **-2.312** | **0.0208** | * |
| **BMI (kg/m2)** | **+0.1733** | 0.0632 | ±0.1265 | **+2.741** | **0.0061** | ** |
| Hypertension | +1.2866 | 0.9795 | ±1.9590 | +1.314 | 0.1890 |  |
| High cholesterol | -0.8595 | 0.9068 | ±1.8136 | -0.948 | 0.3432 |  |
| Kidney disease | -0.9033 | 1.5973 | ±3.1945 | -0.566 | 0.5717 |  |
| Circulatory disease | +0.4760 | 1.3637 | ±2.7274 | +0.349 | 0.7271 |  |
| Mean / SD ratio | +0.5269 | 0.3576 | ±0.7153 | +1.473 | 0.1407 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1251**, R² = **0.0364**, Adj R² = **0.0254**, F-statistic = **3.33** (p = **2.81e-05**), Residual SE = **15.216** on **1236** df, AIC = **10376.3**, BIC = **10453.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+121.7970** | 4.3489 | ±8.6979 | **+28.006** | **1.37e-172** | *** |
| Education: graduate level (vs college) | -0.6774 | 0.9008 | ±1.8015 | -0.752 | 0.4520 |  |
| **Education: high school or below (vs college)** | **+4.3229** | 1.8850 | ±3.7700 | **+2.293** | **0.0218** | * |
| Site: UCSD (vs UAB) | +1.4388 | 1.2208 | ±2.4416 | +1.179 | 0.2386 |  |
| Site: UW (vs UAB) | -0.9260 | 1.0757 | ±2.1515 | -0.861 | 0.3893 |  |
| **Season: spring (vs autumn)** | **+2.7799** | 1.1677 | ±2.3355 | **+2.381** | **0.0173** | * |
| Season: summer (vs autumn) | +1.1050 | 1.3402 | ±2.6803 | +0.825 | 0.4096 |  |
| **Season: winter (vs autumn)** | **+3.2335** | 1.2242 | ±2.4484 | **+2.641** | **0.0083** | ** |
| **Age (years)** | **-0.0968** | 0.0425 | ±0.0851 | **-2.276** | **0.0228** | * |
| **BMI (kg/m2)** | **+0.1762** | 0.0631 | ±0.1263 | **+2.791** | **0.0053** | ** |
| Hypertension | +1.2646 | 0.9779 | ±1.9558 | +1.293 | 0.1959 |  |
| High cholesterol | -0.8579 | 0.9072 | ±1.8145 | -0.946 | 0.3443 |  |
| Kidney disease | -0.8725 | 1.5944 | ±3.1888 | -0.547 | 0.5842 |  |
| Circulatory disease | +0.4639 | 1.3630 | ±2.7260 | +0.340 | 0.7336 |  |
| Avg. daily mean/SD | +0.4289 | 0.3033 | ±0.6066 | +1.414 | 0.1574 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1251**, R² = **0.0347**, Adj R² = **0.0237**, F-statistic = **3.17** (p = **6.30e-05**), Residual SE = **15.229** on **1236** df, AIC = **10378.5**, BIC = **10455.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.2274** | 4.0920 | ±8.1840 | **+30.603** | **1.11e-205** | *** |
| Education: graduate level (vs college) | -0.6584 | 0.9018 | ±1.8035 | -0.730 | 0.4653 |  |
| **Education: high school or below (vs college)** | **+4.3318** | 1.8819 | ±3.7639 | **+2.302** | **0.0213** | * |
| Site: UCSD (vs UAB) | +1.5050 | 1.2217 | ±2.4434 | +1.232 | 0.2180 |  |
| Site: UW (vs UAB) | -0.9616 | 1.0810 | ±2.1620 | -0.890 | 0.3737 |  |
| **Season: spring (vs autumn)** | **+2.7982** | 1.1679 | ±2.3357 | **+2.396** | **0.0166** | * |
| Season: summer (vs autumn) | +1.1494 | 1.3397 | ±2.6793 | +0.858 | 0.3909 |  |
| **Season: winter (vs autumn)** | **+3.2200** | 1.2268 | ±2.4535 | **+2.625** | **0.0087** | ** |
| **Age (years)** | **-0.1016** | 0.0419 | ±0.0838 | **-2.424** | **0.0153** | * |
| **BMI (kg/m2)** | **+0.1751** | 0.0635 | ±0.1270 | **+2.759** | **0.0058** | ** |
| Hypertension | +1.2077 | 0.9779 | ±1.9558 | +1.235 | 0.2168 |  |
| High cholesterol | -0.8276 | 0.9129 | ±1.8257 | -0.907 | 0.3646 |  |
| Kidney disease | -1.0250 | 1.6010 | ±3.2020 | -0.640 | 0.5220 |  |
| Circulatory disease | +0.4530 | 1.3655 | ±2.7309 | +0.332 | 0.7401 |  |
| MAG (mg/dL/h) | -0.0056 | 0.0558 | ±0.1117 | -0.101 | 0.9196 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **1251**, R² = **0.0360**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.42e-05**), Residual SE = **15.219** on **1236** df, AIC = **10376.9**, BIC = **10453.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.0247** | 3.7631 | ±7.5262 | **+33.755** | **8.97e-250** | *** |
| Education: graduate level (vs college) | -0.6313 | 0.9006 | ±1.8011 | -0.701 | 0.4833 |  |
| **Education: high school or below (vs college)** | **+4.3689** | 1.8865 | ±3.7730 | **+2.316** | **0.0206** | * |
| Site: UCSD (vs UAB) | +1.4361 | 1.2185 | ±2.4371 | +1.179 | 0.2386 |  |
| Site: UW (vs UAB) | -0.9288 | 1.0772 | ±2.1544 | -0.862 | 0.3886 |  |
| **Season: spring (vs autumn)** | **+2.7475** | 1.1682 | ±2.3365 | **+2.352** | **0.0187** | * |
| Season: summer (vs autumn) | +1.0818 | 1.3402 | ±2.6804 | +0.807 | 0.4196 |  |
| **Season: winter (vs autumn)** | **+3.1676** | 1.2265 | ±2.4531 | **+2.583** | **0.0098** | ** |
| **Age (years)** | **-0.0984** | 0.0424 | ±0.0849 | **-2.319** | **0.0204** | * |
| **BMI (kg/m2)** | **+0.1719** | 0.0633 | ±0.1266 | **+2.716** | **0.0066** | ** |
| Hypertension | +1.2818 | 0.9798 | ±1.9597 | +1.308 | 0.1908 |  |
| High cholesterol | -0.8473 | 0.9090 | ±1.8179 | -0.932 | 0.3513 |  |
| Kidney disease | -0.8820 | 1.5953 | ±3.1905 | -0.553 | 0.5804 |  |
| Circulatory disease | +0.5184 | 1.3645 | ±2.7290 | +0.380 | 0.7040 |  |
| Avg. daily range (mg/dL) | -0.0214 | 0.0175 | ±0.0350 | -1.223 | 0.2215 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **1251**, R² = **0.0359**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.53e-05**), Residual SE = **15.219** on **1236** df, AIC = **10377.0**, BIC = **10453.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.8623** | 3.6315 | ±7.2630 | **+34.658** | **3.33e-263** | *** |
| Education: graduate level (vs college) | -0.6562 | 0.9011 | ±1.8022 | -0.728 | 0.4665 |  |
| **Education: high school or below (vs college)** | **+4.3239** | 1.8846 | ±3.7691 | **+2.294** | **0.0218** | * |
| Site: UCSD (vs UAB) | +1.4418 | 1.2243 | ±2.4486 | +1.178 | 0.2389 |  |
| Site: UW (vs UAB) | -0.9390 | 1.0773 | ±2.1546 | -0.872 | 0.3834 |  |
| **Season: spring (vs autumn)** | **+2.8705** | 1.1727 | ±2.3454 | **+2.448** | **0.0144** | * |
| Season: summer (vs autumn) | +1.2126 | 1.3397 | ±2.6795 | +0.905 | 0.3654 |  |
| **Season: winter (vs autumn)** | **+3.2549** | 1.2230 | ±2.4461 | **+2.661** | **0.0078** | ** |
| **Age (years)** | **-0.1011** | 0.0419 | ±0.0838 | **-2.412** | **0.0159** | * |
| **BMI (kg/m2)** | **+0.1803** | 0.0630 | ±0.1260 | **+2.862** | **0.0042** | ** |
| Hypertension | +1.2300 | 0.9780 | ±1.9561 | +1.258 | 0.2085 |  |
| High cholesterol | -0.8000 | 0.9075 | ±1.8151 | -0.882 | 0.3780 |  |
| Kidney disease | -1.0221 | 1.6089 | ±3.2178 | -0.635 | 0.5253 |  |
| Circulatory disease | +0.5206 | 1.3655 | ±2.7311 | +0.381 | 0.7030 |  |
| SD of daily means (mg/dL) | -0.1641 | 0.1320 | ±0.2640 | -1.243 | 0.2139 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.19** (p = **5.84e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.3**, BIC = **10455.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.8036** | 6.3571 | ±12.7142 | **+19.318** | **3.83e-83** | *** |
| Education: graduate level (vs college) | -0.6470 | 0.9009 | ±1.8018 | -0.718 | 0.4726 |  |
| **Education: high school or below (vs college)** | **+4.3573** | 1.8819 | ±3.7638 | **+2.315** | **0.0206** | * |
| Site: UCSD (vs UAB) | +1.4828 | 1.2188 | ±2.4376 | +1.217 | 0.2237 |  |
| Site: UW (vs UAB) | -0.9532 | 1.0786 | ±2.1572 | -0.884 | 0.3769 |  |
| **Season: spring (vs autumn)** | **+2.7812** | 1.1699 | ±2.3398 | **+2.377** | **0.0174** | * |
| Season: summer (vs autumn) | +1.1159 | 1.3422 | ±2.6844 | +0.831 | 0.4057 |  |
| **Season: winter (vs autumn)** | **+3.2048** | 1.2267 | ±2.4535 | **+2.612** | **0.0090** | ** |
| **Age (years)** | **-0.1013** | 0.0420 | ±0.0840 | **-2.411** | **0.0159** | * |
| **BMI (kg/m2)** | **+0.1760** | 0.0634 | ±0.1269 | **+2.775** | **0.0055** | ** |
| Hypertension | +1.2309 | 0.9831 | ±1.9662 | +1.252 | 0.2106 |  |
| High cholesterol | -0.8139 | 0.9094 | ±1.8188 | -0.895 | 0.3708 |  |
| Kidney disease | -0.9895 | 1.5998 | ±3.1996 | -0.619 | 0.5362 |  |
| Circulatory disease | +0.4810 | 1.3670 | ±2.7340 | +0.352 | 0.7249 |  |
| Time in range 70-180, pooled (%) | +0.0226 | 0.0538 | ±0.1077 | +0.419 | 0.6753 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.18** (p = **5.91e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.9891** | 6.3908 | ±12.7816 | **+19.245** | **1.56e-82** | *** |
| Education: graduate level (vs college) | -0.6478 | 0.9009 | ±1.8018 | -0.719 | 0.4721 |  |
| **Education: high school or below (vs college)** | **+4.3527** | 1.8819 | ±3.7639 | **+2.313** | **0.0207** | * |
| Site: UCSD (vs UAB) | +1.4865 | 1.2185 | ±2.4370 | +1.220 | 0.2225 |  |
| Site: UW (vs UAB) | -0.9538 | 1.0787 | ±2.1575 | -0.884 | 0.3766 |  |
| **Season: spring (vs autumn)** | **+2.7846** | 1.1697 | ±2.3394 | **+2.381** | **0.0173** | * |
| Season: summer (vs autumn) | +1.1189 | 1.3420 | ±2.6841 | +0.834 | 0.4045 |  |
| **Season: winter (vs autumn)** | **+3.2070** | 1.2269 | ±2.4537 | **+2.614** | **0.0090** | ** |
| **Age (years)** | **-0.1012** | 0.0420 | ±0.0840 | **-2.410** | **0.0159** | * |
| **BMI (kg/m2)** | **+0.1761** | 0.0635 | ±0.1269 | **+2.774** | **0.0055** | ** |
| Hypertension | +1.2284 | 0.9832 | ±1.9664 | +1.249 | 0.2115 |  |
| High cholesterol | -0.8137 | 0.9093 | ±1.8187 | -0.895 | 0.3709 |  |
| Kidney disease | -0.9928 | 1.5998 | ±3.1996 | -0.621 | 0.5349 |  |
| Circulatory disease | +0.4784 | 1.3672 | ±2.7344 | +0.350 | 0.7264 |  |
| Avg. daily time in range 70-180 (%) | +0.0205 | 0.0538 | ±0.1076 | +0.382 | 0.7026 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.0356**, Adj R² = **0.0247**, F-statistic = **3.26** (p = **4.01e-05**), Residual SE = **15.221** on **1236** df, AIC = **10377.3**, BIC = **10454.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.5442** | 3.5081 | ±7.0161 | **+35.787** | **1.74e-280** | *** |
| Education: graduate level (vs college) | -0.7000 | 0.9041 | ±1.8082 | -0.774 | 0.4388 |  |
| **Education: high school or below (vs college)** | **+4.2006** | 1.8873 | ±3.7745 | **+2.226** | **0.0260** | * |
| Site: UCSD (vs UAB) | +1.3626 | 1.2262 | ±2.4523 | +1.111 | 0.2664 |  |
| Site: UW (vs UAB) | -1.0205 | 1.0729 | ±2.1458 | -0.951 | 0.3415 |  |
| **Season: spring (vs autumn)** | **+2.7952** | 1.1675 | ±2.3351 | **+2.394** | **0.0167** | * |
| Season: summer (vs autumn) | +1.1272 | 1.3394 | ±2.6788 | +0.842 | 0.4000 |  |
| **Season: winter (vs autumn)** | **+3.1984** | 1.2288 | ±2.4576 | **+2.603** | **0.0092** | ** |
| **Age (years)** | **-0.1042** | 0.0416 | ±0.0831 | **-2.507** | **0.0122** | * |
| **BMI (kg/m2)** | **+0.1777** | 0.0636 | ±0.1271 | **+2.796** | **0.0052** | ** |
| Hypertension | +1.2084 | 0.9763 | ±1.9526 | +1.238 | 0.2158 |  |
| High cholesterol | -0.8765 | 0.9074 | ±1.8148 | -0.966 | 0.3341 |  |
| Kidney disease | -1.0318 | 1.6037 | ±3.2074 | -0.643 | 0.5200 |  |
| Circulatory disease | +0.5427 | 1.3700 | ±2.7399 | +0.396 | 0.6920 |  |
| Any reading < 54 during wear (0/1) | -1.0360 | 0.9449 | ±1.8897 | -1.096 | 0.2729 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0238**, F-statistic = **3.18** (p = **6.07e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0992** | 3.5635 | ±7.1270 | **+35.106** | **5.49e-270** | *** |
| Education: graduate level (vs college) | -0.6626 | 0.9015 | ±1.8029 | -0.735 | 0.4624 |  |
| **Education: high school or below (vs college)** | **+4.3009** | 1.8796 | ±3.7593 | **+2.288** | **0.0221** | * |
| Site: UCSD (vs UAB) | +1.4671 | 1.2217 | ±2.4434 | +1.201 | 0.2298 |  |
| Site: UW (vs UAB) | -0.9884 | 1.0798 | ±2.1597 | -0.915 | 0.3600 |  |
| **Season: spring (vs autumn)** | **+2.7959** | 1.1685 | ±2.3370 | **+2.393** | **0.0167** | * |
| Season: summer (vs autumn) | +1.1625 | 1.3393 | ±2.6786 | +0.868 | 0.3854 |  |
| **Season: winter (vs autumn)** | **+3.2281** | 1.2258 | ±2.4515 | **+2.634** | **0.0085** | ** |
| **Age (years)** | **-0.1017** | 0.0419 | ±0.0839 | **-2.425** | **0.0153** | * |
| **BMI (kg/m2)** | **+0.1748** | 0.0635 | ±0.1270 | **+2.752** | **0.0059** | ** |
| Hypertension | +1.1987 | 0.9779 | ±1.9558 | +1.226 | 0.2203 |  |
| High cholesterol | -0.8430 | 0.9105 | ±1.8210 | -0.926 | 0.3545 |  |
| Kidney disease | -1.0227 | 1.6046 | ±3.2092 | -0.637 | 0.5239 |  |
| Circulatory disease | +0.4496 | 1.3650 | ±2.7299 | +0.329 | 0.7419 |  |
| Time < 54 (%) | -0.2529 | 0.6931 | ±1.3862 | -0.365 | 0.7152 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0238**, F-statistic = **3.18** (p = **6.07e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0673** | 3.5573 | ±7.1145 | **+35.158** | **8.69e-271** | *** |
| Education: graduate level (vs college) | -0.6650 | 0.9010 | ±1.8021 | -0.738 | 0.4605 |  |
| **Education: high school or below (vs college)** | **+4.3011** | 1.8800 | ±3.7599 | **+2.288** | **0.0221** | * |
| Site: UCSD (vs UAB) | +1.4730 | 1.2224 | ±2.4448 | +1.205 | 0.2282 |  |
| Site: UW (vs UAB) | -0.9933 | 1.0811 | ±2.1622 | -0.919 | 0.3582 |  |
| **Season: spring (vs autumn)** | **+2.8002** | 1.1680 | ±2.3359 | **+2.398** | **0.0165** | * |
| Season: summer (vs autumn) | +1.1643 | 1.3410 | ±2.6820 | +0.868 | 0.3853 |  |
| **Season: winter (vs autumn)** | **+3.2355** | 1.2268 | ±2.4535 | **+2.637** | **0.0084** | ** |
| **Age (years)** | **-0.1014** | 0.0420 | ±0.0839 | **-2.416** | **0.0157** | * |
| **BMI (kg/m2)** | **+0.1749** | 0.0635 | ±0.1271 | **+2.753** | **0.0059** | ** |
| Hypertension | +1.1937 | 0.9774 | ±1.9548 | +1.221 | 0.2220 |  |
| High cholesterol | -0.8405 | 0.9104 | ±1.8208 | -0.923 | 0.3559 |  |
| Kidney disease | -1.0227 | 1.6012 | ±3.2025 | -0.639 | 0.5230 |  |
| Circulatory disease | +0.4474 | 1.3648 | ±2.7296 | +0.328 | 0.7430 |  |
| Avg. daily time < 54 (%) | -0.3362 | 0.9900 | ±1.9801 | -0.340 | 0.7342 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0238**, F-statistic = **3.18** (p = **6.04e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1122** | 3.5517 | ±7.1034 | **+35.226** | **8.00e-272** | *** |
| Education: graduate level (vs college) | -0.6734 | 0.9043 | ±1.8086 | -0.745 | 0.4565 |  |
| **Education: high school or below (vs college)** | **+4.2842** | 1.8816 | ±3.7631 | **+2.277** | **0.0228** | * |
| Site: UCSD (vs UAB) | +1.4806 | 1.2247 | ±2.4494 | +1.209 | 0.2267 |  |
| Site: UW (vs UAB) | -0.9899 | 1.0729 | ±2.1458 | -0.923 | 0.3562 |  |
| **Season: spring (vs autumn)** | **+2.8062** | 1.1686 | ±2.3372 | **+2.401** | **0.0163** | * |
| Season: summer (vs autumn) | +1.1593 | 1.3399 | ±2.6798 | +0.865 | 0.3869 |  |
| **Season: winter (vs autumn)** | **+3.2438** | 1.2232 | ±2.4464 | **+2.652** | **0.0080** | ** |
| **Age (years)** | **-0.1020** | 0.0419 | ±0.0838 | **-2.434** | **0.0149** | * |
| **BMI (kg/m2)** | **+0.1757** | 0.0635 | ±0.1270 | **+2.767** | **0.0057** | ** |
| Hypertension | +1.1954 | 0.9754 | ±1.9509 | +1.226 | 0.2204 |  |
| High cholesterol | -0.8408 | 0.9095 | ±1.8191 | -0.924 | 0.3553 |  |
| Kidney disease | -1.0322 | 1.6012 | ±3.2025 | -0.645 | 0.5192 |  |
| Circulatory disease | +0.4513 | 1.3650 | ±2.7299 | +0.331 | 0.7409 |  |
| Time 54-69, pooled (%) | -0.1084 | 0.3288 | ±0.6576 | -0.330 | 0.7417 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.18** (p = **5.90e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.3**, BIC = **10455.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1140** | 3.5522 | ±7.1044 | **+35.221** | **9.42e-272** | *** |
| Education: graduate level (vs college) | -0.6793 | 0.9055 | ±1.8110 | -0.750 | 0.4531 |  |
| **Education: high school or below (vs college)** | **+4.2712** | 1.8827 | ±3.7654 | **+2.269** | **0.0233** | * |
| Site: UCSD (vs UAB) | +1.4815 | 1.2241 | ±2.4482 | +1.210 | 0.2262 |  |
| Site: UW (vs UAB) | -0.9985 | 1.0740 | ±2.1480 | -0.930 | 0.3525 |  |
| **Season: spring (vs autumn)** | **+2.8079** | 1.1685 | ±2.3370 | **+2.403** | **0.0163** | * |
| Season: summer (vs autumn) | +1.1571 | 1.3403 | ±2.6806 | +0.863 | 0.3880 |  |
| **Season: winter (vs autumn)** | **+3.2528** | 1.2223 | ±2.4446 | **+2.661** | **0.0078** | ** |
| **Age (years)** | **-0.1018** | 0.0419 | ±0.0838 | **-2.430** | **0.0151** | * |
| **BMI (kg/m2)** | **+0.1759** | 0.0635 | ±0.1270 | **+2.770** | **0.0056** | ** |
| Hypertension | +1.1902 | 0.9749 | ±1.9497 | +1.221 | 0.2221 |  |
| High cholesterol | -0.8430 | 0.9097 | ±1.8193 | -0.927 | 0.3541 |  |
| Kidney disease | -1.0331 | 1.6002 | ±3.2003 | -0.646 | 0.5185 |  |
| Circulatory disease | +0.4505 | 1.3648 | ±2.7295 | +0.330 | 0.7413 |  |
| Avg. daily time 54-69 (%) | -0.1343 | 0.3410 | ±0.6820 | -0.394 | 0.6936 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.18** (p = **5.98e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1362** | 3.5559 | ±7.1118 | **+35.191** | **2.75e-271** | *** |
| Education: graduate level (vs college) | -0.6734 | 0.9035 | ±1.8071 | -0.745 | 0.4561 |  |
| **Education: high school or below (vs college)** | **+4.2795** | 1.8810 | ±3.7620 | **+2.275** | **0.0229** | * |
| Site: UCSD (vs UAB) | +1.4673 | 1.2263 | ±2.4526 | +1.197 | 0.2315 |  |
| Site: UW (vs UAB) | -0.9984 | 1.0743 | ±2.1486 | -0.929 | 0.3527 |  |
| **Season: spring (vs autumn)** | **+2.8037** | 1.1683 | ±2.3366 | **+2.400** | **0.0164** | * |
| Season: summer (vs autumn) | +1.1619 | 1.3400 | ±2.6801 | +0.867 | 0.3859 |  |
| **Season: winter (vs autumn)** | **+3.2430** | 1.2242 | ±2.4485 | **+2.649** | **0.0081** | ** |
| **Age (years)** | **-0.1020** | 0.0419 | ±0.0838 | **-2.435** | **0.0149** | * |
| **BMI (kg/m2)** | **+0.1755** | 0.0635 | ±0.1270 | **+2.765** | **0.0057** | ** |
| Hypertension | +1.1934 | 0.9760 | ±1.9521 | +1.223 | 0.2214 |  |
| High cholesterol | -0.8461 | 0.9099 | ±1.8199 | -0.930 | 0.3524 |  |
| Kidney disease | -1.0291 | 1.6031 | ±3.2062 | -0.642 | 0.5209 |  |
| Circulatory disease | +0.4506 | 1.3649 | ±2.7298 | +0.330 | 0.7413 |  |
| Time < 70 (%) | -0.0949 | 0.2550 | ±0.5100 | -0.372 | 0.7097 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.19** (p = **5.88e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.3**, BIC = **10455.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1218** | 3.5535 | ±7.1070 | **+35.211** | **1.38e-271** | *** |
| Education: graduate level (vs college) | -0.6790 | 0.9045 | ±1.8090 | -0.751 | 0.4529 |  |
| **Education: high school or below (vs college)** | **+4.2699** | 1.8822 | ±3.7643 | **+2.269** | **0.0233** | * |
| Site: UCSD (vs UAB) | +1.4721 | 1.2255 | ±2.4511 | +1.201 | 0.2297 |  |
| Site: UW (vs UAB) | -1.0059 | 1.0752 | ±2.1504 | -0.936 | 0.3495 |  |
| **Season: spring (vs autumn)** | **+2.8068** | 1.1683 | ±2.3365 | **+2.403** | **0.0163** | * |
| Season: summer (vs autumn) | +1.1602 | 1.3408 | ±2.6817 | +0.865 | 0.3869 |  |
| **Season: winter (vs autumn)** | **+3.2528** | 1.2235 | ±2.4469 | **+2.659** | **0.0078** | ** |
| **Age (years)** | **-0.1018** | 0.0419 | ±0.0838 | **-2.428** | **0.0152** | * |
| **BMI (kg/m2)** | **+0.1757** | 0.0635 | ±0.1270 | **+2.767** | **0.0057** | ** |
| Hypertension | +1.1877 | 0.9751 | ±1.9503 | +1.218 | 0.2232 |  |
| High cholesterol | -0.8463 | 0.9099 | ±1.8198 | -0.930 | 0.3523 |  |
| Kidney disease | -1.0301 | 1.6010 | ±3.2019 | -0.643 | 0.5199 |  |
| Circulatory disease | +0.4493 | 1.3647 | ±2.7293 | +0.329 | 0.7420 |  |
| Avg. daily time < 70 (%) | -0.1155 | 0.2809 | ±0.5618 | -0.411 | 0.6809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.0360**, Adj R² = **0.0251**, F-statistic = **3.29** (p = **3.38e-05**), Residual SE = **15.219** on **1236** df, AIC = **10376.8**, BIC = **10453.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+113.7317** | 7.4783 | ±14.9566 | **+15.208** | **3.12e-52** | *** |
| Education: graduate level (vs college) | -0.6498 | 0.9007 | ±1.8015 | -0.721 | 0.4707 |  |
| **Education: high school or below (vs college)** | **+4.4815** | 1.8819 | ±3.7638 | **+2.381** | **0.0172** | * |
| Site: UCSD (vs UAB) | +1.4635 | 1.2167 | ±2.4334 | +1.203 | 0.2290 |  |
| Site: UW (vs UAB) | -0.9844 | 1.0770 | ±2.1540 | -0.914 | 0.3607 |  |
| **Season: spring (vs autumn)** | **+2.7791** | 1.1690 | ±2.3380 | **+2.377** | **0.0174** | * |
| Season: summer (vs autumn) | +1.0939 | 1.3399 | ±2.6797 | +0.816 | 0.4143 |  |
| **Season: winter (vs autumn)** | **+3.2057** | 1.2249 | ±2.4497 | **+2.617** | **0.0089** | ** |
| **Age (years)** | **-0.1021** | 0.0419 | ±0.0839 | **-2.435** | **0.0149** | * |
| **BMI (kg/m2)** | **+0.1752** | 0.0632 | ±0.1264 | **+2.771** | **0.0056** | ** |
| Hypertension | +1.2202 | 0.9763 | ±1.9525 | +1.250 | 0.2113 |  |
| High cholesterol | -0.8448 | 0.9094 | ±1.8187 | -0.929 | 0.3529 |  |
| Kidney disease | -1.0079 | 1.6036 | ±3.2072 | -0.629 | 0.5297 |  |
| Circulatory disease | +0.5681 | 1.3723 | ±2.7446 | +0.414 | 0.6789 |  |
| Time 54-250, pooled (%) | +0.1140 | 0.0669 | ±0.1339 | +1.703 | 0.0885 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1251**, R² = **0.0360**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.41e-05**), Residual SE = **15.219** on **1236** df, AIC = **10376.9**, BIC = **10453.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+113.5416** | 7.8240 | ±15.6481 | **+14.512** | **1.02e-47** | *** |
| Education: graduate level (vs college) | -0.6496 | 0.9007 | ±1.8014 | -0.721 | 0.4708 |  |
| **Education: high school or below (vs college)** | **+4.4856** | 1.8825 | ±3.7650 | **+2.383** | **0.0172** | * |
| Site: UCSD (vs UAB) | +1.4699 | 1.2168 | ±2.4336 | +1.208 | 0.2271 |  |
| Site: UW (vs UAB) | -0.9808 | 1.0770 | ±2.1540 | -0.911 | 0.3625 |  |
| **Season: spring (vs autumn)** | **+2.7799** | 1.1689 | ±2.3379 | **+2.378** | **0.0174** | * |
| Season: summer (vs autumn) | +1.0927 | 1.3397 | ±2.6794 | +0.816 | 0.4147 |  |
| **Season: winter (vs autumn)** | **+3.2049** | 1.2250 | ±2.4500 | **+2.616** | **0.0089** | ** |
| **Age (years)** | **-0.1019** | 0.0419 | ±0.0839 | **-2.431** | **0.0151** | * |
| **BMI (kg/m2)** | **+0.1755** | 0.0632 | ±0.1264 | **+2.776** | **0.0055** | ** |
| Hypertension | +1.2198 | 0.9762 | ±1.9525 | +1.249 | 0.2115 |  |
| High cholesterol | -0.8426 | 0.9094 | ±1.8187 | -0.927 | 0.3542 |  |
| Kidney disease | -1.0112 | 1.6031 | ±3.2063 | -0.631 | 0.5282 |  |
| Circulatory disease | +0.5687 | 1.3725 | ±2.7449 | +0.414 | 0.6786 |  |
| Avg. daily time 54-250 (%) | +0.1156 | 0.0706 | ±0.1412 | +1.638 | 0.1015 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.19** (p = **5.87e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.3**, BIC = **10455.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.9815** | 3.5613 | ±7.1227 | **+35.094** | **8.36e-270** | *** |
| Education: graduate level (vs college) | -0.6737 | 0.9014 | ±1.8029 | -0.747 | 0.4548 |  |
| **Education: high school or below (vs college)** | **+4.3164** | 1.8790 | ±3.7580 | **+2.297** | **0.0216** | * |
| Site: UCSD (vs UAB) | +1.5332 | 1.2181 | ±2.4362 | +1.259 | 0.2081 |  |
| Site: UW (vs UAB) | -0.9733 | 1.0781 | ±2.1562 | -0.903 | 0.3666 |  |
| **Season: spring (vs autumn)** | **+2.8239** | 1.1685 | ±2.3369 | **+2.417** | **0.0157** | * |
| Season: summer (vs autumn) | +1.1921 | 1.3420 | ±2.6840 | +0.888 | 0.3744 |  |
| **Season: winter (vs autumn)** | **+3.2512** | 1.2273 | ±2.4545 | **+2.649** | **0.0081** | ** |
| **Age (years)** | **-0.1021** | 0.0420 | ±0.0841 | **-2.428** | **0.0152** | * |
| **BMI (kg/m2)** | **+0.1738** | 0.0638 | ±0.1276 | **+2.724** | **0.0064** | ** |
| Hypertension | +1.1756 | 0.9886 | ±1.9772 | +1.189 | 0.2344 |  |
| High cholesterol | -0.8469 | 0.9127 | ±1.8253 | -0.928 | 0.3534 |  |
| Kidney disease | -1.0823 | 1.5995 | ±3.1990 | -0.677 | 0.4986 |  |
| Circulatory disease | +0.4421 | 1.3651 | ±2.7302 | +0.324 | 0.7460 |  |
| Time 181-250, pooled (%) | +0.0319 | 0.0908 | ±0.1816 | +0.352 | 0.7249 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1251**, R² = **0.0349**, Adj R² = **0.0239**, F-statistic = **3.19** (p = **5.79e-05**), Residual SE = **15.227** on **1236** df, AIC = **10378.3**, BIC = **10455.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.9817** | 3.5606 | ±7.1213 | **+35.101** | **6.50e-270** | *** |
| Education: graduate level (vs college) | -0.6758 | 0.9014 | ±1.8028 | -0.750 | 0.4534 |  |
| **Education: high school or below (vs college)** | **+4.3187** | 1.8793 | ±3.7587 | **+2.298** | **0.0216** | * |
| Site: UCSD (vs UAB) | +1.5374 | 1.2178 | ±2.4357 | +1.262 | 0.2068 |  |
| Site: UW (vs UAB) | -0.9727 | 1.0784 | ±2.1567 | -0.902 | 0.3671 |  |
| **Season: spring (vs autumn)** | **+2.8233** | 1.1684 | ±2.3369 | **+2.416** | **0.0157** | * |
| Season: summer (vs autumn) | +1.1948 | 1.3419 | ±2.6838 | +0.890 | 0.3733 |  |
| **Season: winter (vs autumn)** | **+3.2534** | 1.2273 | ±2.4546 | **+2.651** | **0.0080** | ** |
| **Age (years)** | **-0.1021** | 0.0420 | ±0.0841 | **-2.428** | **0.0152** | * |
| **BMI (kg/m2)** | **+0.1737** | 0.0638 | ±0.1277 | **+2.720** | **0.0065** | ** |
| Hypertension | +1.1732 | 0.9884 | ±1.9767 | +1.187 | 0.2352 |  |
| High cholesterol | -0.8492 | 0.9125 | ±1.8251 | -0.931 | 0.3520 |  |
| Kidney disease | -1.0880 | 1.5997 | ±3.1995 | -0.680 | 0.4964 |  |
| Circulatory disease | +0.4409 | 1.3652 | ±2.7303 | +0.323 | 0.7467 |  |
| Avg. daily time 181-250 (%) | +0.0344 | 0.0893 | ±0.1786 | +0.385 | 0.7004 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.18** (p = **5.98e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0212** | 3.5553 | ±7.1106 | **+35.165** | **6.96e-271** | *** |
| Education: graduate level (vs college) | -0.6454 | 0.9011 | ±1.8021 | -0.716 | 0.4739 |  |
| **Education: high school or below (vs college)** | **+4.3622** | 1.8820 | ±3.7641 | **+2.318** | **0.0205** | * |
| Site: UCSD (vs UAB) | +1.4970 | 1.2179 | ±2.4357 | +1.229 | 0.2190 |  |
| Site: UW (vs UAB) | -0.9443 | 1.0781 | ±2.1563 | -0.876 | 0.3811 |  |
| **Season: spring (vs autumn)** | **+2.7837** | 1.1699 | ±2.3399 | **+2.379** | **0.0173** | * |
| Season: summer (vs autumn) | +1.1204 | 1.3424 | ±2.6848 | +0.835 | 0.4039 |  |
| **Season: winter (vs autumn)** | **+3.2040** | 1.2268 | ±2.4536 | **+2.612** | **0.0090** | ** |
| **Age (years)** | **-0.1012** | 0.0420 | ±0.0840 | **-2.409** | **0.0160** | * |
| **BMI (kg/m2)** | **+0.1758** | 0.0635 | ±0.1269 | **+2.770** | **0.0056** | ** |
| Hypertension | +1.2301 | 0.9840 | ±1.9680 | +1.250 | 0.2113 |  |
| High cholesterol | -0.8108 | 0.9093 | ±1.8185 | -0.892 | 0.3726 |  |
| Kidney disease | -0.9963 | 1.5994 | ±3.1988 | -0.623 | 0.5333 |  |
| Circulatory disease | +0.4763 | 1.3667 | ±2.7334 | +0.349 | 0.7274 |  |
| Time > 180 (%) | -0.0189 | 0.0542 | ±0.1083 | -0.349 | 0.7273 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0238**, F-statistic = **3.18** (p = **6.05e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0160** | 3.5550 | ±7.1100 | **+35.166** | **6.58e-271** | *** |
| Education: graduate level (vs college) | -0.6464 | 0.9011 | ±1.8022 | -0.717 | 0.4732 |  |
| **Education: high school or below (vs college)** | **+4.3563** | 1.8821 | ±3.7641 | **+2.315** | **0.0206** | * |
| Site: UCSD (vs UAB) | +1.4976 | 1.2176 | ±2.4352 | +1.230 | 0.2187 |  |
| Site: UW (vs UAB) | -0.9462 | 1.0784 | ±2.1568 | -0.877 | 0.3803 |  |
| **Season: spring (vs autumn)** | **+2.7868** | 1.1699 | ±2.3398 | **+2.382** | **0.0172** | * |
| Season: summer (vs autumn) | +1.1246 | 1.3423 | ±2.6847 | +0.838 | 0.4021 |  |
| **Season: winter (vs autumn)** | **+3.2060** | 1.2270 | ±2.4540 | **+2.613** | **0.0090** | ** |
| **Age (years)** | **-0.1012** | 0.0420 | ±0.0840 | **-2.410** | **0.0159** | * |
| **BMI (kg/m2)** | **+0.1758** | 0.0635 | ±0.1270 | **+2.768** | **0.0056** | ** |
| Hypertension | +1.2275 | 0.9842 | ±1.9683 | +1.247 | 0.2123 |  |
| High cholesterol | -0.8121 | 0.9092 | ±1.8185 | -0.893 | 0.3718 |  |
| Kidney disease | -1.0000 | 1.5995 | ±3.1989 | -0.625 | 0.5318 |  |
| Circulatory disease | +0.4735 | 1.3670 | ±2.7340 | +0.346 | 0.7290 |  |
| Avg. daily time > 180 (%) | -0.0166 | 0.0541 | ±0.1082 | -0.307 | 0.7590 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0239**, F-statistic = **3.18** (p = **5.89e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.3**, BIC = **10455.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.9797** | 3.5537 | ±7.1075 | **+35.168** | **6.07e-271** | *** |
| Education: graduate level (vs college) | -0.6554 | 0.9011 | ±1.8022 | -0.727 | 0.4670 |  |
| **Education: high school or below (vs college)** | **+4.3627** | 1.8818 | ±3.7636 | **+2.318** | **0.0204** | * |
| Site: UCSD (vs UAB) | +1.5008 | 1.2179 | ±2.4357 | +1.232 | 0.2178 |  |
| Site: UW (vs UAB) | -0.9475 | 1.0781 | ±2.1561 | -0.879 | 0.3794 |  |
| **Season: spring (vs autumn)** | **+2.8008** | 1.1692 | ±2.3383 | **+2.396** | **0.0166** | * |
| Season: summer (vs autumn) | +1.1232 | 1.3410 | ±2.6820 | +0.838 | 0.4023 |  |
| **Season: winter (vs autumn)** | **+3.2186** | 1.2262 | ±2.4524 | **+2.625** | **0.0087** | ** |
| **Age (years)** | **-0.1017** | 0.0420 | ±0.0840 | **-2.421** | **0.0155** | * |
| **BMI (kg/m2)** | **+0.1774** | 0.0636 | ±0.1271 | **+2.792** | **0.0052** | ** |
| Hypertension | +1.2207 | 0.9808 | ±1.9616 | +1.245 | 0.2133 |  |
| High cholesterol | -0.8030 | 0.9086 | ±1.8173 | -0.884 | 0.3768 |  |
| Kidney disease | -1.0313 | 1.5989 | ±3.1978 | -0.645 | 0.5189 |  |
| Circulatory disease | +0.4636 | 1.3664 | ±2.7329 | +0.339 | 0.7344 |  |
| Nocturnal time > 180 (%) | -0.0224 | 0.0586 | ±0.1172 | -0.382 | 0.7024 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.0348**, Adj R² = **0.0238**, F-statistic = **3.18** (p = **6.07e-05**), Residual SE = **15.228** on **1236** df, AIC = **10378.4**, BIC = **10455.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.8954** | 3.5468 | ±7.0936 | **+35.213** | **1.25e-271** | *** |
| Education: graduate level (vs college) | -0.6541 | 0.9012 | ±1.8024 | -0.726 | 0.4680 |  |
| **Education: high school or below (vs college)** | **+4.3291** | 1.8809 | ±3.7619 | **+2.302** | **0.0214** | * |
| Site: UCSD (vs UAB) | +1.5213 | 1.2172 | ±2.4345 | +1.250 | 0.2114 |  |
| Site: UW (vs UAB) | -0.9596 | 1.0795 | ±2.1590 | -0.889 | 0.3740 |  |
| **Season: spring (vs autumn)** | **+2.8221** | 1.1665 | ±2.3330 | **+2.419** | **0.0156** | * |
| Season: summer (vs autumn) | +1.1708 | 1.3402 | ±2.6804 | +0.874 | 0.3823 |  |
| **Season: winter (vs autumn)** | **+3.2411** | 1.2255 | ±2.4509 | **+2.645** | **0.0082** | ** |
| **Age (years)** | **-0.1018** | 0.0420 | ±0.0841 | **-2.421** | **0.0155** | * |
| **BMI (kg/m2)** | **+0.1766** | 0.0636 | ±0.1272 | **+2.777** | **0.0055** | ** |
| Hypertension | +1.1865 | 0.9827 | ±1.9654 | +1.207 | 0.2273 |  |
| High cholesterol | -0.8290 | 0.9102 | ±1.8204 | -0.911 | 0.3624 |  |
| Kidney disease | -1.0390 | 1.5983 | ±3.1965 | -0.650 | 0.5156 |  |
| Circulatory disease | +0.4543 | 1.3663 | ±2.7326 | +0.333 | 0.7395 |  |
| Any reading > 250 during wear (0/1) | +0.3625 | 1.0810 | ±2.1620 | +0.335 | 0.7374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hyper`  
**Model Diagnostics**: N = **1251**, R² = **0.0359**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.49e-05**), Residual SE = **15.219** on **1236** df, AIC = **10376.9**, BIC = **10453.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0842** | 3.5508 | ±7.1016 | **+35.227** | **7.72e-272** | *** |
| Education: graduate level (vs college) | -0.6474 | 0.9007 | ±1.8014 | -0.719 | 0.4723 |  |
| **Education: high school or below (vs college)** | **+4.4905** | 1.8823 | ±3.7647 | **+2.386** | **0.0171** | * |
| Site: UCSD (vs UAB) | +1.4850 | 1.2168 | ±2.4337 | +1.220 | 0.2223 |  |
| Site: UW (vs UAB) | -0.9683 | 1.0769 | ±2.1538 | -0.899 | 0.3686 |  |
| **Season: spring (vs autumn)** | **+2.7817** | 1.1689 | ±2.3378 | **+2.380** | **0.0173** | * |
| Season: summer (vs autumn) | +1.0912 | 1.3394 | ±2.6789 | +0.815 | 0.4153 |  |
| **Season: winter (vs autumn)** | **+3.2041** | 1.2251 | ±2.4503 | **+2.615** | **0.0089** | ** |
| **Age (years)** | **-0.1020** | 0.0419 | ±0.0839 | **-2.432** | **0.0150** | * |
| **BMI (kg/m2)** | **+0.1753** | 0.0632 | ±0.1264 | **+2.772** | **0.0056** | ** |
| Hypertension | +1.2242 | 0.9764 | ±1.9527 | +1.254 | 0.2099 |  |
| High cholesterol | -0.8354 | 0.9092 | ±1.8183 | -0.919 | 0.3581 |  |
| Kidney disease | -1.0116 | 1.6022 | ±3.2043 | -0.631 | 0.5278 |  |
| Circulatory disease | +0.5666 | 1.3723 | ±2.7445 | +0.413 | 0.6797 |  |
| Time > 250 (%) | -0.1118 | 0.0675 | ±0.1351 | -1.655 | 0.0979 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,251)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1251**, R² = **0.0359**, Adj R² = **0.0250**, F-statistic = **3.29** (p = **3.49e-05**), Residual SE = **15.219** on **1236** df, AIC = **10376.9**, BIC = **10453.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.0749** | 3.5504 | ±7.1009 | **+35.228** | **7.45e-272** | *** |
| Education: graduate level (vs college) | -0.6470 | 0.9007 | ±1.8014 | -0.718 | 0.4726 |  |
| **Education: high school or below (vs college)** | **+4.4922** | 1.8828 | ±3.7655 | **+2.386** | **0.0170** | * |
| Site: UCSD (vs UAB) | +1.4842 | 1.2169 | ±2.4337 | +1.220 | 0.2226 |  |
| Site: UW (vs UAB) | -0.9669 | 1.0769 | ±2.1538 | -0.898 | 0.3693 |  |
| **Season: spring (vs autumn)** | **+2.7804** | 1.1689 | ±2.3379 | **+2.379** | **0.0174** | * |
| Season: summer (vs autumn) | +1.0901 | 1.3394 | ±2.6789 | +0.814 | 0.4157 |  |
| **Season: winter (vs autumn)** | **+3.2012** | 1.2252 | ±2.4505 | **+2.613** | **0.0090** | ** |
| **Age (years)** | **-0.1020** | 0.0419 | ±0.0839 | **-2.431** | **0.0151** | * |
| **BMI (kg/m2)** | **+0.1755** | 0.0632 | ±0.1264 | **+2.776** | **0.0055** | ** |
| Hypertension | +1.2245 | 0.9764 | ±1.9527 | +1.254 | 0.2098 |  |
| High cholesterol | -0.8363 | 0.9092 | ±1.8185 | -0.920 | 0.3577 |  |
| Kidney disease | -1.0141 | 1.6024 | ±3.2048 | -0.633 | 0.5268 |  |
| Circulatory disease | +0.5682 | 1.3725 | ±2.7451 | +0.414 | 0.6789 |  |
| Avg. daily time > 250 (%) | -0.1138 | 0.0709 | ±0.1417 | -1.605 | 0.1085 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 1,125; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1253**, F-statistic = **17.10** (p = **3.89e-29**), Residual SE = **3758.368** on **1114** df, AIC = **21725.0**, BIC = **21780.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18042.5887** | 869.6609 | ±1739.3219 | **+20.747** | **1.31e-95** | *** |
| **Education: graduate level (vs college)** | **-533.0111** | 230.0878 | ±460.1757 | **-2.317** | **0.0205** | * |
| **Education: high school or below (vs college)** | **+1602.2738** | 598.8933 | ±1197.7867 | **+2.675** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +110.8789 | 308.9740 | ±617.9480 | +0.359 | 0.7197 |  |
| Site: UW (vs UAB) | -206.5139 | 274.3920 | ±548.7840 | -0.753 | 0.4517 |  |
| **Age (years)** | **-115.6421** | 10.5083 | ±21.0166 | **-11.005** | **3.62e-28** | *** |
| BMI (kg/m2) | -31.7766 | 17.8849 | ±35.7697 | -1.777 | 0.0756 | . |
| Hypertension | -106.7198 | 266.2986 | ±532.5973 | -0.401 | 0.6886 |  |
| High cholesterol | -76.1910 | 230.7635 | ±461.5269 | -0.330 | 0.7413 |  |
| Kidney disease | -337.5699 | 532.4419 | ±1064.8838 | -0.634 | 0.5261 |  |
| Circulatory disease | -651.5480 | 357.0262 | ±714.0525 | -1.825 | 0.0680 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1125**, R² = **0.1371**, Adj R² = **0.1286**, F-statistic = **16.08** (p = **1.38e-29**), Residual SE = **3751.207** on **1113** df, AIC = **21721.7**, BIC = **21782.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15537.1814** | 1331.5770 | ±2663.1539 | **+11.668** | **1.85e-31** | *** |
| **Education: graduate level (vs college)** | **-532.8054** | 229.5647 | ±459.1294 | **-2.321** | **0.0203** | * |
| **Education: high school or below (vs college)** | **+1547.2254** | 600.2836 | ±1200.5671 | **+2.577** | **0.0100** | ** |
| Site: UCSD (vs UAB) | +87.6834 | 309.1081 | ±618.2162 | +0.284 | 0.7767 |  |
| Site: UW (vs UAB) | -228.9389 | 273.8332 | ±547.6663 | -0.836 | 0.4031 |  |
| **Age (years)** | **-117.6473** | 10.4852 | ±20.9703 | **-11.220** | **3.24e-29** | *** |
| **BMI (kg/m2)** | **-35.2503** | 17.9424 | ±35.8848 | **-1.965** | **0.0495** | * |
| Hypertension | -130.4308 | 265.4728 | ±530.9456 | -0.491 | 0.6232 |  |
| High cholesterol | -147.4812 | 233.0321 | ±466.0643 | -0.633 | 0.5268 |  |
| Kidney disease | -335.8216 | 530.0786 | ±1060.1572 | -0.634 | 0.5264 |  |
| Circulatory disease | -679.7218 | 355.0559 | ±710.1118 | -1.914 | 0.0556 | . |
| **HbA1c (%)** | **+493.1986** | 196.9678 | ±393.9356 | **+2.504** | **0.0123** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.53** (p = **1.66e-28**), Residual SE = **3760.056** on **1113** df, AIC = **21727.0**, BIC = **21787.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18036.1630** | 1074.4248 | ±2148.8496 | **+16.787** | **3.05e-63** | *** |
| **Education: graduate level (vs college)** | **-533.1193** | 230.7736 | ±461.5472 | **-2.310** | **0.0209** | * |
| **Education: high school or below (vs college)** | **+1602.0796** | 599.4959 | ±1198.9919 | **+2.672** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +110.8304 | 309.4384 | ±618.8769 | +0.358 | 0.7202 |  |
| Site: UW (vs UAB) | -206.7266 | 275.4543 | ±550.9085 | -0.750 | 0.4530 |  |
| **Age (years)** | **-115.6452** | 10.5217 | ±21.0434 | **-10.991** | **4.22e-28** | *** |
| BMI (kg/m2) | -31.7849 | 17.9996 | ±35.9992 | -1.766 | 0.0774 | . |
| Hypertension | -106.9141 | 267.4302 | ±534.8603 | -0.400 | 0.6893 |  |
| High cholesterol | -76.3787 | 230.9019 | ±461.8038 | -0.331 | 0.7408 |  |
| Kidney disease | -337.8195 | 532.5187 | ±1065.0375 | -0.634 | 0.5258 |  |
| Circulatory disease | -651.6431 | 357.0931 | ±714.1861 | -1.825 | 0.0680 | . |
| Mean glucose (mg/dL) | +0.0596 | 6.1728 | ±12.3456 | +0.010 | 0.9923 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.53** (p = **1.66e-28**), Residual SE = **3760.056** on **1113** df, AIC = **21727.0**, BIC = **21787.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18027.9208** | 1721.0387 | ±3442.0773 | **+10.475** | **1.13e-25** | *** |
| **Education: graduate level (vs college)** | **-533.1193** | 230.7736 | ±461.5472 | **-2.310** | **0.0209** | * |
| **Education: high school or below (vs college)** | **+1602.0796** | 599.4959 | ±1198.9919 | **+2.672** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +110.8304 | 309.4384 | ±618.8769 | +0.358 | 0.7202 |  |
| Site: UW (vs UAB) | -206.7266 | 275.4543 | ±550.9085 | -0.750 | 0.4530 |  |
| **Age (years)** | **-115.6452** | 10.5217 | ±21.0434 | **-10.991** | **4.22e-28** | *** |
| BMI (kg/m2) | -31.7849 | 17.9996 | ±35.9992 | -1.766 | 0.0774 | . |
| Hypertension | -106.9141 | 267.4302 | ±534.8603 | -0.400 | 0.6893 |  |
| High cholesterol | -76.3787 | 230.9019 | ±461.8038 | -0.331 | 0.7408 |  |
| Kidney disease | -337.8195 | 532.5187 | ±1065.0375 | -0.634 | 0.5258 |  |
| Circulatory disease | -651.6431 | 357.0931 | ±714.1861 | -1.825 | 0.0680 | . |
| GMI (%) | +2.4901 | 258.0605 | ±516.1211 | +0.010 | 0.9923 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.55** (p = **1.53e-28**), Residual SE = **3759.777** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17792.1541** | 1042.2984 | ±2084.5967 | **+17.070** | **2.48e-65** | *** |
| **Education: graduate level (vs college)** | **-535.4184** | 230.3199 | ±460.6398 | **-2.325** | **0.0201** | * |
| **Education: high school or below (vs college)** | **+1594.0897** | 599.2489 | ±1198.4978 | **+2.660** | **0.0078** | ** |
| Site: UCSD (vs UAB) | +105.9055 | 309.6337 | ±619.2674 | +0.342 | 0.7323 |  |
| Site: UW (vs UAB) | -214.8009 | 274.3782 | ±548.7563 | -0.783 | 0.4337 |  |
| **Age (years)** | **-115.5412** | 10.5160 | ±21.0320 | **-10.987** | **4.41e-28** | *** |
| BMI (kg/m2) | -32.7004 | 18.1648 | ±36.3297 | -1.800 | 0.0718 | . |
| Hypertension | -112.9959 | 266.8552 | ±533.7104 | -0.423 | 0.6720 |  |
| High cholesterol | -85.5867 | 231.7794 | ±463.5588 | -0.369 | 0.7119 |  |
| Kidney disease | -340.7841 | 532.3796 | ±1064.7592 | -0.640 | 0.5221 |  |
| Circulatory disease | -653.2739 | 356.9776 | ±713.9552 | -1.830 | 0.0672 | . |
| Nocturnal mean 00-06h (mg/dL) | +2.3740 | 5.8350 | ±11.6699 | +0.407 | 0.6841 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.53** (p = **1.65e-28**), Residual SE = **3760.027** on **1113** df, AIC = **21727.0**, BIC = **21787.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18088.4039** | 920.6278 | ±1841.2557 | **+19.648** | **6.03e-86** | *** |
| **Education: graduate level (vs college)** | **-532.6974** | 230.4218 | ±460.8437 | **-2.312** | **0.0208** | * |
| **Education: high school or below (vs college)** | **+1602.5657** | 599.4784 | ±1198.9568 | **+2.673** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +109.4137 | 310.2195 | ±620.4390 | +0.353 | 0.7243 |  |
| Site: UW (vs UAB) | -205.0697 | 274.4960 | ±548.9920 | -0.747 | 0.4550 |  |
| **Age (years)** | **-115.5775** | 10.5307 | ±21.0615 | **-10.975** | **5.03e-28** | *** |
| BMI (kg/m2) | -31.8212 | 17.8684 | ±35.7368 | -1.781 | 0.0749 | . |
| Hypertension | -103.8317 | 266.9518 | ±533.9036 | -0.389 | 0.6973 |  |
| High cholesterol | -75.3228 | 230.7358 | ±461.4716 | -0.326 | 0.7441 |  |
| Kidney disease | -331.9697 | 533.7892 | ±1067.5783 | -0.622 | 0.5340 |  |
| Circulatory disease | -650.2989 | 356.9960 | ±713.9920 | -1.822 | 0.0685 | . |
| Glucose SD, pooled (mg/dL) | -2.3466 | 17.7812 | ±35.5624 | -0.132 | 0.8950 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.54** (p = **1.60e-28**), Residual SE = **3759.914** on **1113** df, AIC = **21726.9**, BIC = **21787.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18133.3085** | 910.9309 | ±1821.8617 | **+19.906** | **3.59e-88** | *** |
| **Education: graduate level (vs college)** | **-531.8678** | 230.4564 | ±460.9129 | **-2.308** | **0.0210** | * |
| **Education: high school or below (vs college)** | **+1603.4192** | 599.5374 | ±1199.0748 | **+2.674** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +108.4044 | 309.7441 | ±619.4883 | +0.350 | 0.7264 |  |
| Site: UW (vs UAB) | -202.7288 | 274.7589 | ±549.5178 | -0.738 | 0.4606 |  |
| **Age (years)** | **-115.4582** | 10.5412 | ±21.0825 | **-10.953** | **6.43e-28** | *** |
| BMI (kg/m2) | -31.7953 | 17.9041 | ±35.8082 | -1.776 | 0.0758 | . |
| Hypertension | -100.4268 | 266.7625 | ±533.5250 | -0.376 | 0.7066 |  |
| High cholesterol | -74.2244 | 230.8250 | ±461.6500 | -0.322 | 0.7478 |  |
| Kidney disease | -325.6053 | 533.5591 | ±1067.1183 | -0.610 | 0.5417 |  |
| Circulatory disease | -648.8405 | 357.0461 | ±714.0922 | -1.817 | 0.0692 | . |
| Avg. daily SD (mg/dL) | -5.4417 | 18.8882 | ±37.7764 | -0.288 | 0.7733 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.53** (p = **1.63e-28**), Residual SE = **3759.999** on **1113** df, AIC = **21726.9**, BIC = **21787.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18136.0180** | 998.2492 | ±1996.4984 | **+18.168** | **9.28e-74** | *** |
| **Education: graduate level (vs college)** | **-533.9678** | 230.0846 | ±460.1693 | **-2.321** | **0.0203** | * |
| **Education: high school or below (vs college)** | **+1600.4212** | 600.7456 | ±1201.4912 | **+2.664** | **0.0077** | ** |
| Site: UCSD (vs UAB) | +107.2043 | 311.6562 | ±623.3123 | +0.344 | 0.7309 |  |
| Site: UW (vs UAB) | -207.0085 | 274.6546 | ±549.3092 | -0.754 | 0.4510 |  |
| **Age (years)** | **-115.5552** | 10.5286 | ±21.0572 | **-10.975** | **5.02e-28** | *** |
| BMI (kg/m2) | -31.9608 | 17.8550 | ±35.7100 | -1.790 | 0.0735 | . |
| Hypertension | -104.2041 | 266.4931 | ±532.9862 | -0.391 | 0.6958 |  |
| High cholesterol | -77.4133 | 231.3502 | ±462.7004 | -0.335 | 0.7379 |  |
| Kidney disease | -331.4434 | 534.0917 | ±1068.1834 | -0.621 | 0.5349 |  |
| Circulatory disease | -650.8747 | 357.3452 | ±714.6905 | -1.821 | 0.0685 | . |
| CV (%) | -5.1921 | 28.7356 | ±57.4711 | -0.181 | 0.8566 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.54** (p = **1.60e-28**), Residual SE = **3759.931** on **1113** df, AIC = **21726.9**, BIC = **21787.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18193.2533** | 1045.9340 | ±2091.8679 | **+17.394** | **9.12e-68** | *** |
| **Education: graduate level (vs college)** | **-531.3316** | 229.9776 | ±459.9552 | **-2.310** | **0.0209** | * |
| **Education: high school or below (vs college)** | **+1603.2058** | 599.2856 | ±1198.5713 | **+2.675** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +116.2072 | 310.9079 | ±621.8158 | +0.374 | 0.7086 |  |
| Site: UW (vs UAB) | -207.1548 | 274.5064 | ±549.0128 | -0.755 | 0.4505 |  |
| **Age (years)** | **-115.7823** | 10.5325 | ±21.0650 | **-10.993** | **4.14e-28** | *** |
| BMI (kg/m2) | -31.5480 | 17.8580 | ±35.7161 | -1.767 | 0.0773 | . |
| Hypertension | -110.9964 | 266.2361 | ±532.4723 | -0.417 | 0.6767 |  |
| High cholesterol | -75.1039 | 231.1485 | ±462.2969 | -0.325 | 0.7452 |  |
| Kidney disease | -344.0027 | 533.8871 | ±1067.7741 | -0.644 | 0.5194 |  |
| Circulatory disease | -652.2786 | 357.1356 | ±714.2711 | -1.826 | 0.0678 | . |
| Mean / SD ratio | -25.3926 | 91.5093 | ±183.0186 | -0.277 | 0.7814 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.55** (p = **1.50e-28**), Residual SE = **3759.703** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18299.1497** | 1049.2592 | ±2098.5184 | **+17.440** | **4.10e-68** | *** |
| **Education: graduate level (vs college)** | **-532.1095** | 230.2177 | ±460.4354 | **-2.311** | **0.0208** | * |
| **Education: high school or below (vs college)** | **+1600.8183** | 598.5698 | ±1197.1396 | **+2.674** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +118.0230 | 309.8545 | ±619.7090 | +0.381 | 0.7033 |  |
| Site: UW (vs UAB) | -208.8094 | 274.4620 | ±548.9240 | -0.761 | 0.4468 |  |
| **Age (years)** | **-115.9923** | 10.5548 | ±21.1097 | **-10.989** | **4.29e-28** | *** |
| BMI (kg/m2) | -31.6184 | 17.8716 | ±35.7433 | -1.769 | 0.0769 | . |
| Hypertension | -112.0004 | 266.0356 | ±532.0712 | -0.421 | 0.6738 |  |
| High cholesterol | -74.6548 | 231.0001 | ±462.0003 | -0.323 | 0.7466 |  |
| Kidney disease | -350.4720 | 534.1571 | ±1068.3142 | -0.656 | 0.5117 |  |
| Circulatory disease | -652.1797 | 357.2171 | ±714.4341 | -1.826 | 0.0679 | . |
| Avg. daily mean/SD | -35.4788 | 76.3933 | ±152.7867 | -0.464 | 0.6423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1125**, R² = **0.1445**, Adj R² = **0.1360**, F-statistic = **17.09** (p = **1.48e-31**), Residual SE = **3735.169** on **1113** df, AIC = **21712.0**, BIC = **21772.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15724.4790** | 1042.7579 | ±2085.5158 | **+15.080** | **2.20e-51** | *** |
| **Education: graduate level (vs college)** | **-515.5912** | 229.0025 | ±458.0049 | **-2.251** | **0.0244** | * |
| **Education: high school or below (vs college)** | **+1568.7427** | 593.6309 | ±1187.2619 | **+2.643** | **0.0082** | ** |
| Site: UCSD (vs UAB) | +168.8285 | 307.9783 | ±615.9566 | +0.548 | 0.5836 |  |
| Site: UW (vs UAB) | -142.6833 | 275.7380 | ±551.4759 | -0.517 | 0.6048 |  |
| **Age (years)** | **-113.9293** | 10.3839 | ±20.7677 | **-10.972** | **5.22e-28** | *** |
| BMI (kg/m2) | -30.7829 | 17.6526 | ±35.3053 | -1.744 | 0.0812 | . |
| Hypertension | -95.8597 | 264.9230 | ±529.8461 | -0.362 | 0.7175 |  |
| High cholesterol | -44.0260 | 227.9099 | ±455.8199 | -0.193 | 0.8468 |  |
| Kidney disease | -408.2573 | 529.4294 | ±1058.8588 | -0.771 | 0.4406 |  |
| Circulatory disease | -618.7274 | 354.8170 | ±709.6340 | -1.744 | 0.0812 | . |
| **MAG (mg/dL/h)** | **+55.6816** | 15.1237 | ±30.2475 | **+3.682** | **2.32e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.54** (p = **1.56e-28**), Residual SE = **3759.826** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17884.7512** | 960.0665 | ±1920.1329 | **+18.629** | **1.88e-77** | *** |
| **Education: graduate level (vs college)** | **-534.6141** | 230.3203 | ±460.6407 | **-2.321** | **0.0203** | * |
| **Education: high school or below (vs college)** | **+1599.2347** | 598.4772 | ±1196.9543 | **+2.672** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +114.0933 | 309.8660 | ±619.7319 | +0.368 | 0.7127 |  |
| Site: UW (vs UAB) | -209.6170 | 274.6882 | ±549.3764 | -0.763 | 0.4454 |  |
| **Age (years)** | **-115.8203** | 10.5251 | ±21.0502 | **-11.004** | **3.65e-28** | *** |
| BMI (kg/m2) | -31.3400 | 17.8463 | ±35.6925 | -1.756 | 0.0791 | . |
| Hypertension | -112.2415 | 266.7652 | ±533.5305 | -0.421 | 0.6739 |  |
| High cholesterol | -76.5830 | 230.9166 | ±461.8332 | -0.332 | 0.7402 |  |
| Kidney disease | -349.3725 | 532.9941 | ±1065.9881 | -0.655 | 0.5122 |  |
| Circulatory disease | -654.2223 | 357.1102 | ±714.2205 | -1.832 | 0.0670 | . |
| Avg. daily range (mg/dL) | +1.6278 | 4.4326 | ±8.8653 | +0.367 | 0.7135 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1125**, R² = **0.1341**, Adj R² = **0.1255**, F-statistic = **15.67** (p = **8.86e-29**), Residual SE = **3757.821** on **1113** df, AIC = **21725.6**, BIC = **21785.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17783.0807** | 883.3959 | ±1766.7919 | **+20.130** | **4.00e-90** | *** |
| **Education: graduate level (vs college)** | **-534.9954** | 230.2931 | ±460.5861 | **-2.323** | **0.0202** | * |
| **Education: high school or below (vs college)** | **+1611.1013** | 597.8978 | ±1195.7957 | **+2.695** | **0.0070** | ** |
| Site: UCSD (vs UAB) | +130.8299 | 309.5766 | ±619.1532 | +0.423 | 0.6726 |  |
| Site: UW (vs UAB) | -209.7674 | 274.0395 | ±548.0791 | -0.765 | 0.4440 |  |
| **Age (years)** | **-115.3787** | 10.5033 | ±21.0066 | **-10.985** | **4.51e-28** | *** |
| BMI (kg/m2) | -32.6570 | 18.0037 | ±36.0074 | -1.814 | 0.0697 | . |
| Hypertension | -112.8385 | 265.9140 | ±531.8279 | -0.424 | 0.6713 |  |
| High cholesterol | -88.6128 | 231.1491 | ±462.2982 | -0.383 | 0.7015 |  |
| Kidney disease | -351.2047 | 533.8276 | ±1067.6553 | -0.658 | 0.5106 |  |
| Circulatory disease | -659.3186 | 356.5715 | ±713.1430 | -1.849 | 0.0645 | . |
| SD of daily means (mg/dL) | +41.5497 | 36.8219 | ±73.6439 | +1.128 | 0.2592 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.54** (p = **1.54e-28**), Residual SE = **3759.794** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17536.3244** | 1652.7554 | ±3305.5107 | **+10.610** | **2.67e-26** | *** |
| **Education: graduate level (vs college)** | **-531.5959** | 230.2530 | ±460.5060 | **-2.309** | **0.0210** | * |
| **Education: high school or below (vs college)** | **+1604.5192** | 600.3775 | ±1200.7550 | **+2.673** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +107.8338 | 309.7306 | ±619.4613 | +0.348 | 0.7277 |  |
| Site: UW (vs UAB) | -204.8959 | 274.8225 | ±549.6450 | -0.746 | 0.4559 |  |
| **Age (years)** | **-115.6795** | 10.5170 | ±21.0340 | **-10.999** | **3.85e-28** | *** |
| BMI (kg/m2) | -31.6014 | 17.9661 | ±35.9323 | -1.759 | 0.0786 | . |
| Hypertension | -101.7437 | 267.4045 | ±534.8089 | -0.380 | 0.7036 |  |
| High cholesterol | -71.3242 | 230.7065 | ±461.4130 | -0.309 | 0.7572 |  |
| Kidney disease | -326.0376 | 532.5405 | ±1065.0809 | -0.612 | 0.5404 |  |
| Circulatory disease | -647.1084 | 357.4703 | ±714.9406 | -1.810 | 0.0703 | . |
| Time in range 70-180, pooled (%) | +5.2073 | 14.1701 | ±28.3402 | +0.367 | 0.7133 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.55** (p = **1.52e-28**), Residual SE = **3759.742** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17487.2968** | 1659.4358 | ±3318.8716 | **+10.538** | **5.77e-26** | *** |
| **Education: graduate level (vs college)** | **-531.3875** | 230.2744 | ±460.5488 | **-2.308** | **0.0210** | * |
| **Education: high school or below (vs college)** | **+1604.0654** | 600.4921 | ±1200.9841 | **+2.671** | **0.0076** | ** |
| Site: UCSD (vs UAB) | +107.7455 | 309.7049 | ±619.4097 | +0.348 | 0.7279 |  |
| Site: UW (vs UAB) | -204.8528 | 274.8039 | ±549.6079 | -0.745 | 0.4560 |  |
| **Age (years)** | **-115.6664** | 10.5156 | ±21.0312 | **-11.000** | **3.84e-28** | *** |
| BMI (kg/m2) | -31.5504 | 17.9786 | ±35.9573 | -1.755 | 0.0793 | . |
| Hypertension | -101.3386 | 267.3718 | ±534.7436 | -0.379 | 0.7047 |  |
| High cholesterol | -70.5253 | 230.8207 | ±461.6414 | -0.306 | 0.7600 |  |
| Kidney disease | -325.1354 | 532.7017 | ±1065.4035 | -0.610 | 0.5416 |  |
| Circulatory disease | -646.7315 | 357.4873 | ±714.9745 | -1.809 | 0.0704 | . |
| Avg. daily time in range 70-180 (%) | +5.6761 | 14.1169 | ±28.2337 | +0.402 | 0.6876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.53** (p = **1.65e-28**), Residual SE = **3760.028** on **1113** df, AIC = **21727.0**, BIC = **21787.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18060.6762** | 891.1692 | ±1782.3383 | **+20.266** | **2.55e-91** | *** |
| **Education: graduate level (vs college)** | **-533.9451** | 230.8992 | ±461.7983 | **-2.312** | **0.0208** | * |
| **Education: high school or below (vs college)** | **+1598.8816** | 597.8636 | ±1195.7272 | **+2.674** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +105.9574 | 310.4141 | ±620.8282 | +0.341 | 0.7328 |  |
| Site: UW (vs UAB) | -208.6379 | 275.1269 | ±550.2538 | -0.758 | 0.4483 |  |
| **Age (years)** | **-115.7418** | 10.5973 | ±21.1946 | **-10.922** | **9.06e-28** | *** |
| BMI (kg/m2) | -31.7211 | 17.8837 | ±35.7673 | -1.774 | 0.0761 | . |
| Hypertension | -106.3525 | 266.7766 | ±533.5533 | -0.399 | 0.6901 |  |
| High cholesterol | -78.1774 | 230.9408 | ±461.8815 | -0.339 | 0.7350 |  |
| Kidney disease | -338.4214 | 533.3407 | ±1066.6814 | -0.635 | 0.5257 |  |
| Circulatory disease | -647.8504 | 357.2582 | ±714.5165 | -1.813 | 0.0698 | . |
| Any reading < 54 during wear (0/1) | -31.5991 | 242.4173 | ±484.8347 | -0.130 | 0.8963 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1125**, R² = **0.1333**, Adj R² = **0.1247**, F-statistic = **15.56** (p = **1.45e-28**), Residual SE = **3759.574** on **1113** df, AIC = **21726.7**, BIC = **21787.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18087.6088** | 877.3417 | ±1754.6835 | **+20.616** | **1.96e-94** | *** |
| **Education: graduate level (vs college)** | **-535.2651** | 230.3365 | ±460.6731 | **-2.324** | **0.0201** | * |
| **Education: high school or below (vs college)** | **+1592.6177** | 599.8072 | ±1199.6145 | **+2.655** | **0.0079** | ** |
| Site: UCSD (vs UAB) | +91.0565 | 310.8824 | ±621.7647 | +0.293 | 0.7696 |  |
| Site: UW (vs UAB) | -221.5373 | 274.3675 | ±548.7349 | -0.807 | 0.4194 |  |
| **Age (years)** | **-115.7600** | 10.5153 | ±21.0307 | **-11.009** | **3.47e-28** | *** |
| BMI (kg/m2) | -31.9148 | 17.9106 | ±35.8213 | -1.782 | 0.0748 | . |
| Hypertension | -111.1918 | 266.1753 | ±532.3506 | -0.418 | 0.6761 |  |
| High cholesterol | -85.2060 | 231.5071 | ±463.0142 | -0.368 | 0.7128 |  |
| Kidney disease | -333.2488 | 532.1154 | ±1064.2307 | -0.626 | 0.5311 |  |
| Circulatory disease | -651.5353 | 357.1507 | ±714.3014 | -1.824 | 0.0681 | . |
| Time < 54 (%) | -101.5489 | 142.4474 | ±284.8948 | -0.713 | 0.4759 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.54** (p = **1.61e-28**), Residual SE = **3759.949** on **1113** df, AIC = **21726.9**, BIC = **21787.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18057.9889** | 875.5171 | ±1751.0342 | **+20.626** | **1.62e-94** | *** |
| **Education: graduate level (vs college)** | **-534.5645** | 230.4510 | ±460.9020 | **-2.320** | **0.0204** | * |
| **Education: high school or below (vs college)** | **+1597.7786** | 599.4535 | ±1198.9071 | **+2.665** | **0.0077** | ** |
| Site: UCSD (vs UAB) | +102.5453 | 310.7326 | ±621.4652 | +0.330 | 0.7414 |  |
| Site: UW (vs UAB) | -214.3682 | 274.7618 | ±549.5236 | -0.780 | 0.4353 |  |
| **Age (years)** | **-115.6250** | 10.5131 | ±21.0263 | **-10.998** | **3.90e-28** | *** |
| BMI (kg/m2) | -31.8232 | 17.9316 | ±35.8632 | -1.775 | 0.0759 | . |
| Hypertension | -109.6120 | 266.1674 | ±532.3348 | -0.412 | 0.6805 |  |
| High cholesterol | -80.2281 | 231.2077 | ±462.4153 | -0.347 | 0.7286 |  |
| Kidney disease | -335.7177 | 532.3659 | ±1064.7319 | -0.631 | 0.5283 |  |
| Circulatory disease | -652.3369 | 356.9709 | ±713.9418 | -1.827 | 0.0676 | . |
| Avg. daily time < 54 (%) | -64.1694 | 225.5860 | ±451.1720 | -0.284 | 0.7761 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.55** (p = **1.52e-28**), Residual SE = **3759.742** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18086.3039** | 886.0161 | ±1772.0322 | **+20.413** | **1.28e-92** | *** |
| **Education: graduate level (vs college)** | **-537.9523** | 230.6103 | ±461.2206 | **-2.333** | **0.0197** | * |
| **Education: high school or below (vs college)** | **+1589.8651** | 598.9022 | ±1197.8043 | **+2.655** | **0.0079** | ** |
| Site: UCSD (vs UAB) | +99.6940 | 308.5371 | ±617.0743 | +0.323 | 0.7466 |  |
| Site: UW (vs UAB) | -218.2815 | 272.8285 | ±545.6570 | -0.800 | 0.4237 |  |
| **Age (years)** | **-115.8278** | 10.5475 | ±21.0950 | **-10.982** | **4.69e-28** | *** |
| BMI (kg/m2) | -31.6446 | 17.9118 | ±35.8236 | -1.767 | 0.0773 | . |
| Hypertension | -110.8634 | 266.2872 | ±532.5744 | -0.416 | 0.6772 |  |
| High cholesterol | -82.6320 | 231.6347 | ±463.2693 | -0.357 | 0.7213 |  |
| Kidney disease | -338.2275 | 532.8798 | ±1065.7597 | -0.635 | 0.5256 |  |
| Circulatory disease | -651.5544 | 357.0067 | ±714.0134 | -1.825 | 0.0680 | . |
| Time 54-69, pooled (%) | -33.5920 | 87.7037 | ±175.4074 | -0.383 | 0.7017 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.54** (p = **1.56e-28**), Residual SE = **3759.828** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18074.3324** | 882.8468 | ±1765.6937 | **+20.473** | **3.76e-93** | *** |
| **Education: graduate level (vs college)** | **-537.7639** | 230.5860 | ±461.1720 | **-2.332** | **0.0197** | * |
| **Education: high school or below (vs college)** | **+1590.8842** | 599.0536 | ±1198.1073 | **+2.656** | **0.0079** | ** |
| Site: UCSD (vs UAB) | +103.1152 | 308.5115 | ±617.0229 | +0.334 | 0.7382 |  |
| Site: UW (vs UAB) | -216.5089 | 273.1347 | ±546.2695 | -0.793 | 0.4280 |  |
| **Age (years)** | **-115.7420** | 10.5318 | ±21.0635 | **-10.990** | **4.28e-28** | *** |
| BMI (kg/m2) | -31.6711 | 17.9136 | ±35.8271 | -1.768 | 0.0771 | . |
| Hypertension | -110.6750 | 266.4153 | ±532.8306 | -0.415 | 0.6778 |  |
| High cholesterol | -81.2787 | 231.5164 | ±463.0328 | -0.351 | 0.7255 |  |
| Kidney disease | -338.5354 | 532.7158 | ±1065.4316 | -0.635 | 0.5251 |  |
| Circulatory disease | -651.9887 | 356.9664 | ±713.9328 | -1.826 | 0.0678 | . |
| Avg. daily time 54-69 (%) | -28.6122 | 89.9583 | ±179.9166 | -0.318 | 0.7504 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1125**, R² = **0.1333**, Adj R² = **0.1247**, F-statistic = **15.56** (p = **1.46e-28**), Residual SE = **3759.607** on **1113** df, AIC = **21726.7**, BIC = **21787.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18098.1311** | 886.7924 | ±1773.5848 | **+20.409** | **1.40e-92** | *** |
| **Education: graduate level (vs college)** | **-538.4005** | 230.6231 | ±461.2463 | **-2.335** | **0.0196** | * |
| **Education: high school or below (vs college)** | **+1587.4869** | 599.3106 | ±1198.6212 | **+2.649** | **0.0081** | ** |
| Site: UCSD (vs UAB) | +94.0648 | 309.1857 | ±618.3713 | +0.304 | 0.7609 |  |
| Site: UW (vs UAB) | -222.3757 | 273.0154 | ±546.0308 | -0.815 | 0.4153 |  |
| **Age (years)** | **-115.8550** | 10.5409 | ±21.0819 | **-10.991** | **4.22e-28** | *** |
| BMI (kg/m2) | -31.6948 | 17.9195 | ±35.8391 | -1.769 | 0.0769 | . |
| Hypertension | -112.0486 | 266.2067 | ±532.4134 | -0.421 | 0.6738 |  |
| High cholesterol | -85.1213 | 231.8256 | ±463.6512 | -0.367 | 0.7135 |  |
| Kidney disease | -336.8385 | 532.6262 | ±1065.2524 | -0.632 | 0.5271 |  |
| Circulatory disease | -651.5501 | 357.0020 | ±714.0041 | -1.825 | 0.0680 | . |
| Time < 70 (%) | -31.8351 | 65.3727 | ±130.7454 | -0.487 | 0.6263 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.54** (p = **1.56e-28**), Residual SE = **3759.824** on **1113** df, AIC = **21726.8**, BIC = **21787.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18075.1126** | 883.0421 | ±1766.0842 | **+20.469** | **4.06e-93** | *** |
| **Education: graduate level (vs college)** | **-537.5982** | 230.6316 | ±461.2633 | **-2.331** | **0.0198** | * |
| **Education: high school or below (vs college)** | **+1590.9912** | 599.2472 | ±1198.4944 | **+2.655** | **0.0079** | ** |
| Site: UCSD (vs UAB) | +101.2090 | 308.8957 | ±617.7914 | +0.328 | 0.7432 |  |
| Site: UW (vs UAB) | -217.8834 | 273.3682 | ±546.7364 | -0.797 | 0.4254 |  |
| **Age (years)** | **-115.7198** | 10.5251 | ±21.0502 | **-10.995** | **4.06e-28** | *** |
| BMI (kg/m2) | -31.7052 | 17.9184 | ±35.8367 | -1.769 | 0.0768 | . |
| Hypertension | -111.1378 | 266.3473 | ±532.6947 | -0.417 | 0.6765 |  |
| High cholesterol | -81.9930 | 231.5935 | ±463.1870 | -0.354 | 0.7233 |  |
| Kidney disease | -337.6875 | 532.6355 | ±1065.2710 | -0.634 | 0.5261 |  |
| Circulatory disease | -652.2155 | 356.9261 | ±713.8521 | -1.827 | 0.0677 | . |
| Avg. daily time < 70 (%) | -24.1019 | 72.5433 | ±145.0865 | -0.332 | 0.7397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1334**, Adj R² = **0.1249**, F-statistic = **15.58** (p = **1.33e-28**), Residual SE = **3759.254** on **1113** df, AIC = **21726.5**, BIC = **21786.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19743.0251** | 2850.0124 | ±5700.0248 | **+6.927** | **4.29e-12** | *** |
| **Education: graduate level (vs college)** | **-532.3636** | 230.1762 | ±460.3523 | **-2.313** | **0.0207** | * |
| **Education: high school or below (vs college)** | **+1591.1064** | 599.7883 | ±1199.5766 | **+2.653** | **0.0080** | ** |
| Site: UCSD (vs UAB) | +113.1586 | 309.0736 | ±618.1472 | +0.366 | 0.7143 |  |
| Site: UW (vs UAB) | -204.9401 | 274.5374 | ±549.0749 | -0.746 | 0.4554 |  |
| **Age (years)** | **-115.4495** | 10.5337 | ±21.0675 | **-10.960** | **5.95e-28** | *** |
| BMI (kg/m2) | -31.8309 | 17.8995 | ±35.7989 | -1.778 | 0.0754 | . |
| Hypertension | -105.3746 | 266.3218 | ±532.6437 | -0.396 | 0.6924 |  |
| High cholesterol | -77.1971 | 230.9067 | ±461.8135 | -0.334 | 0.7381 |  |
| Kidney disease | -344.0772 | 533.1014 | ±1066.2029 | -0.645 | 0.5187 |  |
| Circulatory disease | -661.1243 | 358.5694 | ±717.1387 | -1.844 | 0.0652 | . |
| Time 54-250, pooled (%) | -17.2021 | 27.3454 | ±54.6907 | -0.629 | 0.5293 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1335**, Adj R² = **0.1249**, F-statistic = **15.58** (p = **1.29e-28**), Residual SE = **3759.155** on **1113** df, AIC = **21726.4**, BIC = **21786.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19918.8972** | 2855.4540 | ±5710.9080 | **+6.976** | **3.04e-12** | *** |
| **Education: graduate level (vs college)** | **-532.3128** | 230.1650 | ±460.3299 | **-2.313** | **0.0207** | * |
| **Education: high school or below (vs college)** | **+1590.1870** | 599.8053 | ±1199.6105 | **+2.651** | **0.0080** | ** |
| Site: UCSD (vs UAB) | +112.1751 | 309.0326 | ±618.0652 | +0.363 | 0.7166 |  |
| Site: UW (vs UAB) | -205.6667 | 274.5495 | ±549.0990 | -0.749 | 0.4538 |  |
| **Age (years)** | **-115.4683** | 10.5290 | ±21.0581 | **-10.967** | **5.53e-28** | *** |
| BMI (kg/m2) | -31.8911 | 17.8979 | ±35.7957 | -1.782 | 0.0748 | . |
| Hypertension | -105.1168 | 266.2842 | ±532.5684 | -0.395 | 0.6930 |  |
| High cholesterol | -77.7281 | 230.8515 | ±461.7031 | -0.337 | 0.7363 |  |
| Kidney disease | -343.9654 | 533.0610 | ±1066.1220 | -0.645 | 0.5188 |  |
| Circulatory disease | -661.4605 | 358.5108 | ±717.0215 | -1.845 | 0.0650 | . |
| Avg. daily time 54-250 (%) | -18.9191 | 27.2973 | ±54.5945 | -0.693 | 0.4883 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1125**, R² = **0.1338**, Adj R² = **0.1253**, F-statistic = **15.63** (p = **1.04e-28**), Residual SE = **3758.408** on **1113** df, AIC = **21726.0**, BIC = **21786.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18048.7218** | 871.5550 | ±1743.1099 | **+20.709** | **2.89e-95** | *** |
| **Education: graduate level (vs college)** | **-524.4371** | 230.4655 | ±460.9311 | **-2.276** | **0.0229** | * |
| **Education: high school or below (vs college)** | **+1605.1174** | 598.8983 | ±1197.7967 | **+2.680** | **0.0074** | ** |
| Site: UCSD (vs UAB) | +108.6383 | 309.3623 | ±618.7247 | +0.351 | 0.7255 |  |
| Site: UW (vs UAB) | -192.3803 | 274.3239 | ±548.6477 | -0.701 | 0.4831 |  |
| **Age (years)** | **-115.4629** | 10.5115 | ±21.0231 | **-10.984** | **4.54e-28** | *** |
| BMI (kg/m2) | -31.2778 | 17.9996 | ±35.9993 | -1.738 | 0.0823 | . |
| Hypertension | -84.9865 | 267.3958 | ±534.7917 | -0.318 | 0.7506 |  |
| High cholesterol | -56.1342 | 230.7860 | ±461.5721 | -0.243 | 0.8078 |  |
| Kidney disease | -302.7118 | 533.4592 | ±1066.9183 | -0.567 | 0.5704 |  |
| Circulatory disease | -645.9874 | 356.9643 | ±713.9286 | -1.810 | 0.0703 | . |
| Time 181-250, pooled (%) | -18.7818 | 17.1953 | ±34.3907 | -1.092 | 0.2747 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1339**, Adj R² = **0.1254**, F-statistic = **15.65** (p = **9.77e-29**), Residual SE = **3758.169** on **1113** df, AIC = **21725.8**, BIC = **21786.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18047.2767** | 871.6776 | ±1743.3551 | **+20.704** | **3.18e-95** | *** |
| **Education: graduate level (vs college)** | **-523.3003** | 230.5309 | ±461.0618 | **-2.270** | **0.0232** | * |
| **Education: high school or below (vs college)** | **+1603.7599** | 599.0353 | ±1198.0706 | **+2.677** | **0.0074** | ** |
| Site: UCSD (vs UAB) | +106.6658 | 309.4540 | ±618.9080 | +0.345 | 0.7303 |  |
| Site: UW (vs UAB) | -192.8774 | 274.2815 | ±548.5631 | -0.703 | 0.4819 |  |
| **Age (years)** | **-115.4756** | 10.5095 | ±21.0190 | **-10.988** | **4.38e-28** | *** |
| BMI (kg/m2) | -31.1788 | 18.0095 | ±36.0191 | -1.731 | 0.0834 | . |
| Hypertension | -83.4682 | 267.4305 | ±534.8610 | -0.312 | 0.7550 |  |
| High cholesterol | -54.4536 | 230.9089 | ±461.8178 | -0.236 | 0.8136 |  |
| Kidney disease | -300.1132 | 533.5369 | ±1067.0738 | -0.562 | 0.5738 |  |
| Circulatory disease | -644.7967 | 356.8703 | ±713.7405 | -1.807 | 0.0708 | . |
| Avg. daily time 181-250 (%) | -19.8563 | 16.8791 | ±33.7583 | -1.176 | 0.2394 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.54** (p = **1.60e-28**), Residual SE = **3759.920** on **1113** df, AIC = **21726.9**, BIC = **21787.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18046.4783** | 870.0757 | ±1740.1513 | **+20.741** | **1.47e-95** | *** |
| **Education: graduate level (vs college)** | **-531.3500** | 230.3214 | ±460.6428 | **-2.307** | **0.0211** | * |
| **Education: high school or below (vs college)** | **+1605.6470** | 599.9767 | ±1199.9534 | **+2.676** | **0.0074** | ** |
| Site: UCSD (vs UAB) | +110.6657 | 309.5165 | ±619.0330 | +0.358 | 0.7207 |  |
| Site: UW (vs UAB) | -203.4672 | 275.0416 | ±550.0832 | -0.740 | 0.4594 |  |
| **Age (years)** | **-115.6439** | 10.5168 | ±21.0336 | **-10.996** | **3.99e-28** | *** |
| BMI (kg/m2) | -31.6595 | 17.9664 | ±35.9328 | -1.762 | 0.0780 | . |
| Hypertension | -102.4905 | 267.3777 | ±534.7553 | -0.383 | 0.7015 |  |
| High cholesterol | -71.6147 | 230.7450 | ±461.4900 | -0.310 | 0.7563 |  |
| Kidney disease | -329.3159 | 532.9084 | ±1065.8167 | -0.618 | 0.5366 |  |
| Circulatory disease | -648.3369 | 357.4065 | ±714.8130 | -1.814 | 0.0697 | . |
| Time > 180 (%) | -3.7661 | 14.0663 | ±28.1327 | -0.268 | 0.7889 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1125**, R² = **0.1332**, Adj R² = **0.1246**, F-statistic = **15.54** (p = **1.56e-28**), Residual SE = **3759.841** on **1113** df, AIC = **21726.8**, BIC = **21787.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18046.4586** | 870.1750 | ±1740.3501 | **+20.739** | **1.54e-95** | *** |
| **Education: graduate level (vs college)** | **-530.7650** | 230.3485 | ±460.6969 | **-2.304** | **0.0212** | * |
| **Education: high school or below (vs college)** | **+1605.9694** | 600.1378 | ±1200.2756 | **+2.676** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +110.1678 | 309.5696 | ±619.1392 | +0.356 | 0.7219 |  |
| Site: UW (vs UAB) | -202.9097 | 275.0044 | ±550.0088 | -0.738 | 0.4606 |  |
| **Age (years)** | **-115.6471** | 10.5158 | ±21.0316 | **-10.997** | **3.93e-28** | *** |
| BMI (kg/m2) | -31.6027 | 17.9800 | ±35.9599 | -1.758 | 0.0788 | . |
| Hypertension | -101.3853 | 267.4143 | ±534.8285 | -0.379 | 0.7046 |  |
| High cholesterol | -70.3495 | 230.8702 | ±461.7405 | -0.305 | 0.7606 |  |
| Kidney disease | -327.2175 | 532.9578 | ±1065.9156 | -0.614 | 0.5392 |  |
| Circulatory disease | -647.4163 | 357.4190 | ±714.8380 | -1.811 | 0.0701 | . |
| Avg. daily time > 180 (%) | -4.7151 | 14.0562 | ±28.1124 | -0.335 | 0.7373 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1125**, R² = **0.1331**, Adj R² = **0.1245**, F-statistic = **15.54** (p = **1.61e-28**), Residual SE = **3759.948** on **1113** df, AIC = **21726.9**, BIC = **21787.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18040.4306** | 871.2717 | ±1742.5434 | **+20.706** | **3.07e-95** | *** |
| **Education: graduate level (vs college)** | **-533.4263** | 230.2573 | ±460.5146 | **-2.317** | **0.0205** | * |
| **Education: high school or below (vs college)** | **+1604.4117** | 600.3573 | ±1200.7147 | **+2.672** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +110.6851 | 309.5281 | ±619.0563 | +0.358 | 0.7206 |  |
| Site: UW (vs UAB) | -204.5911 | 274.9345 | ±549.8690 | -0.744 | 0.4568 |  |
| **Age (years)** | **-115.7219** | 10.5164 | ±21.0328 | **-11.004** | **3.66e-28** | *** |
| BMI (kg/m2) | -31.4089 | 18.1446 | ±36.2892 | -1.731 | 0.0834 | . |
| Hypertension | -105.1008 | 266.9591 | ±533.9182 | -0.394 | 0.6938 |  |
| High cholesterol | -71.0423 | 231.3975 | ±462.7950 | -0.307 | 0.7588 |  |
| Kidney disease | -336.6388 | 532.6442 | ±1065.2884 | -0.632 | 0.5274 |  |
| Circulatory disease | -650.8688 | 357.2705 | ±714.5409 | -1.822 | 0.0685 | . |
| Nocturnal time > 180 (%) | -3.5454 | 14.9577 | ±29.9154 | -0.237 | 0.8126 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1333**, Adj R² = **0.1247**, F-statistic = **15.56** (p = **1.47e-28**), Residual SE = **3759.616** on **1113** df, AIC = **21726.7**, BIC = **21787.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18000.8648** | 876.6736 | ±1753.3473 | **+20.533** | **1.09e-93** | *** |
| **Education: graduate level (vs college)** | **-533.2133** | 230.2952 | ±460.5904 | **-2.315** | **0.0206** | * |
| **Education: high school or below (vs college)** | **+1600.5037** | 598.3156 | ±1196.6312 | **+2.675** | **0.0075** | ** |
| Site: UCSD (vs UAB) | +110.3232 | 309.0496 | ±618.0991 | +0.357 | 0.7211 |  |
| Site: UW (vs UAB) | -209.8143 | 274.8981 | ±549.7962 | -0.763 | 0.4453 |  |
| **Age (years)** | **-115.6524** | 10.5240 | ±21.0480 | **-10.989** | **4.30e-28** | *** |
| BMI (kg/m2) | -31.0196 | 17.8417 | ±35.6834 | -1.739 | 0.0821 | . |
| Hypertension | -115.8408 | 267.3927 | ±534.7855 | -0.433 | 0.6649 |  |
| High cholesterol | -81.8241 | 229.7035 | ±459.4071 | -0.356 | 0.7217 |  |
| Kidney disease | -342.8691 | 532.3086 | ±1064.6172 | -0.644 | 0.5195 |  |
| Circulatory disease | -650.1322 | 357.3663 | ±714.7326 | -1.819 | 0.0689 | . |
| Any reading > 250 during wear (0/1) | +146.0163 | 285.8194 | ±571.6389 | +0.511 | 0.6094 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1125**, R² = **0.1335**, Adj R² = **0.1249**, F-statistic = **15.59** (p = **1.26e-28**), Residual SE = **3759.067** on **1113** df, AIC = **21726.4**, BIC = **21786.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18029.0032** | 870.0381 | ±1740.0762 | **+20.722** | **2.19e-95** | *** |
| **Education: graduate level (vs college)** | **-532.7140** | 230.1420 | ±460.2840 | **-2.315** | **0.0206** | * |
| **Education: high school or below (vs college)** | **+1587.9570** | 599.7959 | ±1199.5917 | **+2.647** | **0.0081** | ** |
| Site: UCSD (vs UAB) | +109.6733 | 309.1106 | ±618.2212 | +0.355 | 0.7227 |  |
| Site: UW (vs UAB) | -207.5998 | 274.6402 | ±549.2803 | -0.756 | 0.4497 |  |
| **Age (years)** | **-115.4490** | 10.5309 | ±21.0619 | **-10.963** | **5.77e-28** | *** |
| BMI (kg/m2) | -31.8635 | 17.8970 | ±35.7940 | -1.780 | 0.0750 | . |
| Hypertension | -106.0626 | 266.2953 | ±532.5907 | -0.398 | 0.6904 |  |
| High cholesterol | -79.0237 | 230.7626 | ±461.5252 | -0.342 | 0.7320 |  |
| Kidney disease | -344.0280 | 533.1075 | ±1066.2151 | -0.645 | 0.5187 |  |
| Circulatory disease | -662.2541 | 358.5623 | ±717.1247 | -1.847 | 0.0648 | . |
| Time > 250 (%) | +19.2358 | 26.7857 | ±53.5715 | +0.718 | 0.4727 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,125)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1335**, Adj R² = **0.1249**, F-statistic = **15.59** (p = **1.26e-28**), Residual SE = **3759.082** on **1113** df, AIC = **21726.4**, BIC = **21786.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18031.0331** | 869.9435 | ±1739.8870 | **+20.727** | **1.99e-95** | *** |
| **Education: graduate level (vs college)** | **-532.7601** | 230.1395 | ±460.2790 | **-2.315** | **0.0206** | * |
| **Education: high school or below (vs college)** | **+1588.2616** | 599.8734 | ±1199.7467 | **+2.648** | **0.0081** | ** |
| Site: UCSD (vs UAB) | +109.6661 | 309.0954 | ±618.1908 | +0.355 | 0.7227 |  |
| Site: UW (vs UAB) | -208.0480 | 274.6631 | ±549.3263 | -0.757 | 0.4488 |  |
| **Age (years)** | **-115.4552** | 10.5294 | ±21.0588 | **-10.965** | **5.63e-28** | *** |
| BMI (kg/m2) | -31.9106 | 17.8995 | ±35.7989 | -1.783 | 0.0746 | . |
| Hypertension | -105.9360 | 266.2971 | ±532.5941 | -0.398 | 0.6908 |  |
| High cholesterol | -79.0403 | 230.7705 | ±461.5409 | -0.343 | 0.7320 |  |
| Kidney disease | -343.6810 | 533.0538 | ±1066.1076 | -0.645 | 0.5191 |  |
| Circulatory disease | -662.1470 | 358.4961 | ±716.9921 | -1.847 | 0.0647 | . |
| Avg. daily time > 250 (%) | +19.7656 | 27.1968 | ±54.3937 | +0.727 | 0.4674 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 1,125; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1394**, F-statistic = **19.21** (p = **6.57e-33**), Residual SE = **11.849** on **1114** df, AIC = **8766.2**, BIC = **8821.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8701** | 2.8500 | ±5.7001 | **+16.796** | **2.60e-63** | *** |
| Education: graduate level (vs college) | -1.4338 | 0.7423 | ±1.4846 | -1.932 | 0.0534 | . |
| **Education: high school or below (vs college)** | **+3.8401** | 1.7412 | ±3.4824 | **+2.205** | **0.0274** | * |
| Site: UCSD (vs UAB) | +0.6799 | 0.9956 | ±1.9913 | +0.683 | 0.4947 |  |
| Site: UW (vs UAB) | -0.0767 | 0.8585 | ±1.7170 | -0.089 | 0.9288 |  |
| **Age (years)** | **-0.3980** | 0.0328 | ±0.0656 | **-12.125** | **7.83e-34** | *** |
| BMI (kg/m2) | +0.0264 | 0.0569 | ±0.1139 | +0.464 | 0.6426 |  |
| Hypertension | -0.3428 | 0.8154 | ±1.6308 | -0.420 | 0.6742 |  |
| High cholesterol | -0.1133 | 0.7294 | ±1.4588 | -0.155 | 0.8766 |  |
| Kidney disease | -0.3528 | 1.6981 | ±3.3961 | -0.208 | 0.8354 |  |
| Circulatory disease | -1.9672 | 1.0698 | ±2.1396 | -1.839 | 0.0659 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1125**, R² = **0.1512**, Adj R² = **0.1428**, F-statistic = **18.02** (p = **2.26e-33**), Residual SE = **11.826** on **1113** df, AIC = **8762.7**, BIC = **8823.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.8581** | 4.4285 | ±8.8570 | **+9.000** | **2.25e-19** | *** |
| Education: graduate level (vs college) | -1.4331 | 0.7404 | ±1.4807 | -1.936 | 0.0529 | . |
| **Education: high school or below (vs college)** | **+3.6640** | 1.7510 | ±3.5021 | **+2.092** | **0.0364** | * |
| Site: UCSD (vs UAB) | +0.6057 | 0.9955 | ±1.9911 | +0.608 | 0.5429 |  |
| Site: UW (vs UAB) | -0.1484 | 0.8576 | ±1.7153 | -0.173 | 0.8626 |  |
| **Age (years)** | **-0.4044** | 0.0327 | ±0.0655 | **-12.355** | **4.60e-35** | *** |
| BMI (kg/m2) | +0.0153 | 0.0573 | ±0.1145 | +0.267 | 0.7892 |  |
| Hypertension | -0.4187 | 0.8135 | ±1.6269 | -0.515 | 0.6068 |  |
| High cholesterol | -0.3413 | 0.7400 | ±1.4801 | -0.461 | 0.6447 |  |
| Kidney disease | -0.3472 | 1.6840 | ±3.3681 | -0.206 | 0.8366 |  |
| Circulatory disease | -2.0573 | 1.0672 | ±2.1343 | -1.928 | 0.0539 | . |
| **HbA1c (%)** | **+1.5772** | 0.6799 | ±1.3598 | **+2.320** | **0.0204** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1125**, R² = **0.1475**, Adj R² = **0.1391**, F-statistic = **17.51** (p = **2.29e-32**), Residual SE = **11.852** on **1113** df, AIC = **8767.6**, BIC = **8827.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.3350** | 3.4451 | ±6.8901 | **+13.450** | **3.09e-41** | *** |
| **Education: graduate level (vs college)** | **-1.4596** | 0.7444 | ±1.4889 | **-1.961** | **0.0499** | * |
| **Education: high school or below (vs college)** | **+3.7937** | 1.7416 | ±3.4833 | **+2.178** | **0.0294** | * |
| Site: UCSD (vs UAB) | +0.6683 | 0.9959 | ±1.9918 | +0.671 | 0.5022 |  |
| Site: UW (vs UAB) | -0.1275 | 0.8632 | ±1.7264 | -0.148 | 0.8825 |  |
| **Age (years)** | **-0.3987** | 0.0329 | ±0.0658 | **-12.116** | **8.70e-34** | *** |
| BMI (kg/m2) | +0.0244 | 0.0572 | ±0.1144 | +0.427 | 0.6693 |  |
| Hypertension | -0.3892 | 0.8172 | ±1.6343 | -0.476 | 0.6338 |  |
| High cholesterol | -0.1581 | 0.7295 | ±1.4589 | -0.217 | 0.8284 |  |
| Kidney disease | -0.4124 | 1.6891 | ±3.3782 | -0.244 | 0.8071 |  |
| Circulatory disease | -1.9899 | 1.0722 | ±2.1445 | -1.856 | 0.0635 | . |
| Mean glucose (mg/dL) | +0.0142 | 0.0197 | ±0.0394 | +0.723 | 0.4698 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1125**, R² = **0.1475**, Adj R² = **0.1391**, F-statistic = **17.51** (p = **2.29e-32**), Residual SE = **11.852** on **1113** df, AIC = **8767.6**, BIC = **8827.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.3661** | 5.4669 | ±10.9338 | **+8.115** | **4.84e-16** | *** |
| **Education: graduate level (vs college)** | **-1.4596** | 0.7444 | ±1.4889 | **-1.961** | **0.0499** | * |
| **Education: high school or below (vs college)** | **+3.7937** | 1.7416 | ±3.4833 | **+2.178** | **0.0294** | * |
| Site: UCSD (vs UAB) | +0.6683 | 0.9959 | ±1.9918 | +0.671 | 0.5022 |  |
| Site: UW (vs UAB) | -0.1275 | 0.8632 | ±1.7264 | -0.148 | 0.8825 |  |
| **Age (years)** | **-0.3987** | 0.0329 | ±0.0658 | **-12.116** | **8.70e-34** | *** |
| BMI (kg/m2) | +0.0244 | 0.0572 | ±0.1144 | +0.427 | 0.6693 |  |
| Hypertension | -0.3892 | 0.8172 | ±1.6343 | -0.476 | 0.6338 |  |
| High cholesterol | -0.1581 | 0.7295 | ±1.4589 | -0.217 | 0.8284 |  |
| Kidney disease | -0.4124 | 1.6891 | ±3.3782 | -0.244 | 0.8071 |  |
| Circulatory disease | -1.9899 | 1.0722 | ±2.1445 | -1.856 | 0.0635 | . |
| GMI (%) | +0.5949 | 0.8231 | ±1.6461 | +0.723 | 0.4698 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1125**, R² = **0.1474**, Adj R² = **0.1390**, F-statistic = **17.50** (p = **2.36e-32**), Residual SE = **11.852** on **1113** df, AIC = **8767.7**, BIC = **8828.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5203** | 3.3931 | ±6.7861 | **+13.710** | **8.80e-43** | *** |
| Education: graduate level (vs college) | -1.4468 | 0.7430 | ±1.4861 | -1.947 | 0.0515 | . |
| **Education: high school or below (vs college)** | **+3.7960** | 1.7418 | ±3.4835 | **+2.179** | **0.0293** | * |
| Site: UCSD (vs UAB) | +0.6531 | 0.9968 | ±1.9935 | +0.655 | 0.5123 |  |
| Site: UW (vs UAB) | -0.1214 | 0.8620 | ±1.7241 | -0.141 | 0.8880 |  |
| **Age (years)** | **-0.3974** | 0.0328 | ±0.0657 | **-12.099** | **1.06e-33** | *** |
| BMI (kg/m2) | +0.0214 | 0.0578 | ±0.1157 | +0.371 | 0.7108 |  |
| Hypertension | -0.3767 | 0.8165 | ±1.6331 | -0.461 | 0.6446 |  |
| High cholesterol | -0.1639 | 0.7304 | ±1.4608 | -0.224 | 0.8224 |  |
| Kidney disease | -0.3701 | 1.6933 | ±3.3867 | -0.219 | 0.8270 |  |
| Circulatory disease | -1.9765 | 1.0709 | ±2.1419 | -1.846 | 0.0650 | . |
| Nocturnal mean 00-06h (mg/dL) | +0.0128 | 0.0190 | ±0.0381 | +0.672 | 0.5014 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1125**, R² = **0.1479**, Adj R² = **0.1395**, F-statistic = **17.56** (p = **1.77e-32**), Residual SE = **11.849** on **1113** df, AIC = **8767.1**, BIC = **8827.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.7362** | 3.0109 | ±6.0219 | **+15.522** | **2.46e-54** | *** |
| Education: graduate level (vs college) | -1.4416 | 0.7433 | ±1.4865 | -1.939 | 0.0524 | . |
| **Education: high school or below (vs college)** | **+3.8329** | 1.7375 | ±3.4749 | **+2.206** | **0.0274** | * |
| Site: UCSD (vs UAB) | +0.7161 | 0.9997 | ±1.9994 | +0.716 | 0.4738 |  |
| Site: UW (vs UAB) | -0.1125 | 0.8600 | ±1.7201 | -0.131 | 0.8960 |  |
| **Age (years)** | **-0.3996** | 0.0329 | ±0.0658 | **-12.151** | **5.65e-34** | *** |
| BMI (kg/m2) | +0.0275 | 0.0569 | ±0.1138 | +0.484 | 0.6285 |  |
| Hypertension | -0.4143 | 0.8170 | ±1.6339 | -0.507 | 0.6121 |  |
| High cholesterol | -0.1348 | 0.7294 | ±1.4588 | -0.185 | 0.8534 |  |
| Kidney disease | -0.4914 | 1.7000 | ±3.4000 | -0.289 | 0.7725 |  |
| Circulatory disease | -1.9981 | 1.0707 | ±2.1414 | -1.866 | 0.0620 | . |
| Glucose SD, pooled (mg/dL) | +0.0581 | 0.0580 | ±0.1160 | +1.002 | 0.3166 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1125**, R² = **0.1476**, Adj R² = **0.1392**, F-statistic = **17.52** (p = **2.09e-32**), Residual SE = **11.851** on **1113** df, AIC = **8767.4**, BIC = **8827.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.0262** | 2.9790 | ±5.9580 | **+15.786** | **3.89e-56** | *** |
| Education: graduate level (vs college) | -1.4444 | 0.7438 | ±1.4875 | -1.942 | 0.0521 | . |
| **Education: high school or below (vs college)** | **+3.8294** | 1.7393 | ±3.4787 | **+2.202** | **0.0277** | * |
| Site: UCSD (vs UAB) | +0.7029 | 0.9985 | ±1.9971 | +0.704 | 0.4815 |  |
| Site: UW (vs UAB) | -0.1119 | 0.8608 | ±1.7216 | -0.130 | 0.8965 |  |
| **Age (years)** | **-0.3997** | 0.0329 | ±0.0658 | **-12.142** | **6.36e-34** | *** |
| BMI (kg/m2) | +0.0266 | 0.0569 | ±0.1138 | +0.467 | 0.6402 |  |
| Hypertension | -0.4014 | 0.8168 | ±1.6336 | -0.491 | 0.6231 |  |
| High cholesterol | -0.1316 | 0.7298 | ±1.4596 | -0.180 | 0.8569 |  |
| Kidney disease | -0.4641 | 1.6972 | ±3.3945 | -0.273 | 0.7845 |  |
| Circulatory disease | -1.9924 | 1.0716 | ±2.1432 | -1.859 | 0.0630 | . |
| Avg. daily SD (mg/dL) | +0.0506 | 0.0617 | ±0.1235 | +0.820 | 0.4123 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1125**, R² = **0.1476**, Adj R² = **0.1391**, F-statistic = **17.51** (p = **2.20e-32**), Residual SE = **11.851** on **1113** df, AIC = **8767.5**, BIC = **8827.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.6013** | 3.3082 | ±6.6164 | **+14.087** | **4.60e-45** | *** |
| Education: graduate level (vs college) | -1.4208 | 0.7419 | ±1.4837 | -1.915 | 0.0555 | . |
| **Education: high school or below (vs college)** | **+3.8652** | 1.7401 | ±3.4801 | **+2.221** | **0.0263** | * |
| Site: UCSD (vs UAB) | +0.7298 | 1.0047 | ±2.0093 | +0.726 | 0.4676 |  |
| Site: UW (vs UAB) | -0.0700 | 0.8605 | ±1.7209 | -0.081 | 0.9352 |  |
| **Age (years)** | **-0.3992** | 0.0328 | ±0.0657 | **-12.158** | **5.21e-34** | *** |
| BMI (kg/m2) | +0.0289 | 0.0570 | ±0.1140 | +0.507 | 0.6118 |  |
| Hypertension | -0.3770 | 0.8167 | ±1.6335 | -0.462 | 0.6444 |  |
| High cholesterol | -0.0967 | 0.7300 | ±1.4601 | -0.132 | 0.8946 |  |
| Kidney disease | -0.4360 | 1.7088 | ±3.4176 | -0.255 | 0.7986 |  |
| Circulatory disease | -1.9763 | 1.0696 | ±2.1393 | -1.848 | 0.0647 | . |
| CV (%) | +0.0705 | 0.0957 | ±0.1914 | +0.737 | 0.4612 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1125**, R² = **0.1485**, Adj R² = **0.1401**, F-statistic = **17.65** (p = **1.19e-32**), Residual SE = **11.845** on **1113** df, AIC = **8766.3**, BIC = **8826.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2736** | 3.3979 | ±6.7957 | **+14.796** | **1.56e-49** | *** |
| Education: graduate level (vs college) | -1.4070 | 0.7410 | ±1.4820 | -1.899 | 0.0576 | . |
| **Education: high school or below (vs college)** | **+3.8549** | 1.7358 | ±3.4716 | **+2.221** | **0.0264** | * |
| Site: UCSD (vs UAB) | +0.7649 | 1.0012 | ±2.0025 | +0.764 | 0.4449 |  |
| Site: UW (vs UAB) | -0.0869 | 0.8594 | ±1.7188 | -0.101 | 0.9194 |  |
| **Age (years)** | **-0.4002** | 0.0328 | ±0.0656 | **-12.193** | **3.39e-34** | *** |
| BMI (kg/m2) | +0.0301 | 0.0570 | ±0.1139 | +0.528 | 0.5975 |  |
| Hypertension | -0.4111 | 0.8160 | ±1.6320 | -0.504 | 0.6144 |  |
| High cholesterol | -0.0959 | 0.7296 | ±1.4593 | -0.131 | 0.8954 |  |
| Kidney disease | -0.4554 | 1.7043 | ±3.4086 | -0.267 | 0.7893 |  |
| Circulatory disease | -1.9789 | 1.0675 | ±2.1349 | -1.854 | 0.0638 | . |
| Mean / SD ratio | -0.4051 | 0.3009 | ±0.6018 | -1.346 | 0.1782 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1125**, R² = **0.1486**, Adj R² = **0.1402**, F-statistic = **17.66** (p = **1.14e-32**), Residual SE = **11.844** on **1113** df, AIC = **8766.1**, BIC = **8826.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3789** | 3.4077 | ±6.8154 | **+14.784** | **1.86e-49** | *** |
| Education: graduate level (vs college) | -1.4250 | 0.7418 | ±1.4836 | -1.921 | 0.0547 | . |
| **Education: high school or below (vs college)** | **+3.8258** | 1.7365 | ±3.4730 | **+2.203** | **0.0276** | * |
| Site: UCSD (vs UAB) | +0.7497 | 0.9985 | ±1.9970 | +0.751 | 0.4527 |  |
| Site: UW (vs UAB) | -0.0992 | 0.8592 | ±1.7184 | -0.115 | 0.9081 |  |
| **Age (years)** | **-0.4014** | 0.0329 | ±0.0658 | **-12.209** | **2.78e-34** | *** |
| BMI (kg/m2) | +0.0280 | 0.0568 | ±0.1136 | +0.492 | 0.6225 |  |
| Hypertension | -0.3945 | 0.8153 | ±1.6306 | -0.484 | 0.6285 |  |
| High cholesterol | -0.0983 | 0.7295 | ±1.4590 | -0.135 | 0.8929 |  |
| Kidney disease | -0.4790 | 1.7012 | ±3.4024 | -0.282 | 0.7783 |  |
| Circulatory disease | -1.9734 | 1.0683 | ±2.1366 | -1.847 | 0.0647 | . |
| Avg. daily mean/SD | -0.3469 | 0.2499 | ±0.4997 | -1.388 | 0.1650 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1125**, R² = **0.1613**, Adj R² = **0.1530**, F-statistic = **19.46** (p = **3.89e-36**), Residual SE = **11.756** on **1113** df, AIC = **8749.3**, BIC = **8809.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.6564** | 3.4381 | ±6.8763 | **+11.534** | **8.87e-31** | *** |
| Education: graduate level (vs college) | -1.3721 | 0.7377 | ±1.4754 | -1.860 | 0.0629 | . |
| **Education: high school or below (vs college)** | **+3.7213** | 1.7112 | ±3.4225 | **+2.175** | **0.0297** | * |
| Site: UCSD (vs UAB) | +0.8852 | 0.9890 | ±1.9780 | +0.895 | 0.3708 |  |
| Site: UW (vs UAB) | +0.1494 | 0.8586 | ±1.7172 | +0.174 | 0.8618 |  |
| **Age (years)** | **-0.3919** | 0.0325 | ±0.0650 | **-12.059** | **1.74e-33** | *** |
| BMI (kg/m2) | +0.0299 | 0.0559 | ±0.1118 | +0.536 | 0.5921 |  |
| Hypertension | -0.3043 | 0.8105 | ±1.6209 | -0.376 | 0.7073 |  |
| High cholesterol | +0.0007 | 0.7207 | ±1.4414 | +0.001 | 0.9992 |  |
| Kidney disease | -0.6033 | 1.6796 | ±3.3592 | -0.359 | 0.7195 |  |
| Circulatory disease | -1.8509 | 1.0552 | ±2.1105 | -1.754 | 0.0794 | . |
| **MAG (mg/dL/h)** | **+0.1973** | 0.0490 | ±0.0981 | **+4.024** | **5.72e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1125**, R² = **0.1486**, Adj R² = **0.1402**, F-statistic = **17.66** (p = **1.15e-32**), Residual SE = **11.844** on **1113** df, AIC = **8766.2**, BIC = **8826.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.9687** | 3.1504 | ±6.3008 | **+14.591** | **3.19e-48** | *** |
| Education: graduate level (vs college) | -1.4531 | 0.7430 | ±1.4861 | -1.956 | 0.0505 | . |
| **Education: high school or below (vs college)** | **+3.8035** | 1.7360 | ±3.4720 | **+2.191** | **0.0285** | * |
| Site: UCSD (vs UAB) | +0.7186 | 0.9974 | ±1.9948 | +0.720 | 0.4712 |  |
| Site: UW (vs UAB) | -0.1141 | 0.8609 | ±1.7219 | -0.133 | 0.8946 |  |
| **Age (years)** | **-0.4001** | 0.0328 | ±0.0656 | **-12.192** | **3.41e-34** | *** |
| BMI (kg/m2) | +0.0317 | 0.0570 | ±0.1139 | +0.556 | 0.5782 |  |
| Hypertension | -0.4093 | 0.8167 | ±1.6334 | -0.501 | 0.6162 |  |
| High cholesterol | -0.1180 | 0.7292 | ±1.4583 | -0.162 | 0.8714 |  |
| Kidney disease | -0.4950 | 1.6944 | ±3.3888 | -0.292 | 0.7702 |  |
| Circulatory disease | -1.9994 | 1.0699 | ±2.1398 | -1.869 | 0.0617 | . |
| Avg. daily range (mg/dL) | +0.0196 | 0.0146 | ±0.0292 | +1.344 | 0.1789 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1125**, R² = **0.1494**, Adj R² = **0.1410**, F-statistic = **17.78** (p = **6.82e-33**), Residual SE = **11.838** on **1113** df, AIC = **8765.1**, BIC = **8825.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.6215** | 2.9011 | ±5.8023 | **+16.070** | **4.14e-58** | *** |
| Education: graduate level (vs college) | -1.4433 | 0.7423 | ±1.4846 | -1.944 | 0.0518 | . |
| **Education: high school or below (vs college)** | **+3.8826** | 1.7315 | ±3.4631 | **+2.242** | **0.0249** | * |
| Site: UCSD (vs UAB) | +0.7759 | 0.9973 | ±1.9946 | +0.778 | 0.4366 |  |
| Site: UW (vs UAB) | -0.0924 | 0.8578 | ±1.7155 | -0.108 | 0.9142 |  |
| **Age (years)** | **-0.3967** | 0.0328 | ±0.0656 | **-12.101** | **1.04e-33** | *** |
| BMI (kg/m2) | +0.0222 | 0.0573 | ±0.1147 | +0.387 | 0.6989 |  |
| Hypertension | -0.3723 | 0.8153 | ±1.6307 | -0.457 | 0.6480 |  |
| High cholesterol | -0.1730 | 0.7293 | ±1.4587 | -0.237 | 0.8125 |  |
| Kidney disease | -0.4184 | 1.7028 | ±3.4057 | -0.246 | 0.8059 |  |
| Circulatory disease | -2.0046 | 1.0666 | ±2.1331 | -1.880 | 0.0602 | . |
| SD of daily means (mg/dL) | +0.1999 | 0.1188 | ±0.2377 | +1.682 | 0.0925 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1125**, R² = **0.1473**, Adj R² = **0.1389**, F-statistic = **17.48** (p = **2.56e-32**), Residual SE = **11.853** on **1113** df, AIC = **8767.9**, BIC = **8828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1251** | 5.3799 | ±10.7597 | **+9.317** | **1.19e-20** | *** |
| Education: graduate level (vs college) | -1.4401 | 0.7430 | ±1.4860 | -1.938 | 0.0526 | . |
| **Education: high school or below (vs college)** | **+3.8301** | 1.7429 | ±3.4858 | **+2.198** | **0.0280** | * |
| Site: UCSD (vs UAB) | +0.6934 | 0.9974 | ±1.9948 | +0.695 | 0.4869 |  |
| Site: UW (vs UAB) | -0.0839 | 0.8601 | ±1.7203 | -0.098 | 0.9223 |  |
| **Age (years)** | **-0.3978** | 0.0329 | ±0.0657 | **-12.105** | **9.99e-34** | *** |
| BMI (kg/m2) | +0.0256 | 0.0571 | ±0.1142 | +0.449 | 0.6535 |  |
| Hypertension | -0.3650 | 0.8165 | ±1.6330 | -0.447 | 0.6549 |  |
| High cholesterol | -0.1350 | 0.7296 | ±1.4593 | -0.185 | 0.8533 |  |
| Kidney disease | -0.4042 | 1.6938 | ±3.3877 | -0.239 | 0.8114 |  |
| Circulatory disease | -1.9870 | 1.0736 | ±2.1472 | -1.851 | 0.0642 | . |
| Time in range 70-180, pooled (%) | -0.0232 | 0.0452 | ±0.0904 | -0.513 | 0.6079 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1125**, R² = **0.1473**, Adj R² = **0.1388**, F-statistic = **17.47** (p = **2.64e-32**), Residual SE = **11.853** on **1113** df, AIC = **8767.9**, BIC = **8828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8944** | 5.4060 | ±10.8121 | **+9.229** | **2.72e-20** | *** |
| Education: graduate level (vs college) | -1.4397 | 0.7431 | ±1.4862 | -1.937 | 0.0527 | . |
| **Education: high school or below (vs college)** | **+3.8335** | 1.7432 | ±3.4864 | **+2.199** | **0.0279** | * |
| Site: UCSD (vs UAB) | +0.6913 | 0.9974 | ±1.9948 | +0.693 | 0.4882 |  |
| Site: UW (vs UAB) | -0.0828 | 0.8600 | ±1.7201 | -0.096 | 0.9233 |  |
| **Age (years)** | **-0.3979** | 0.0329 | ±0.0657 | **-12.106** | **9.85e-34** | *** |
| BMI (kg/m2) | +0.0256 | 0.0571 | ±0.1143 | +0.448 | 0.6542 |  |
| Hypertension | -0.3624 | 0.8168 | ±1.6335 | -0.444 | 0.6572 |  |
| High cholesterol | -0.1339 | 0.7300 | ±1.4600 | -0.183 | 0.8544 |  |
| Kidney disease | -0.3982 | 1.6940 | ±3.3880 | -0.235 | 0.8142 |  |
| Circulatory disease | -1.9848 | 1.0736 | ±2.1472 | -1.849 | 0.0645 | . |
| Avg. daily time in range 70-180 (%) | -0.0207 | 0.0452 | ±0.0903 | -0.458 | 0.6467 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1387**, F-statistic = **17.45** (p = **2.89e-32**), Residual SE = **11.854** on **1113** df, AIC = **8768.1**, BIC = **8828.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.7644** | 2.9169 | ±5.8339 | **+16.375** | **2.89e-60** | *** |
| Education: graduate level (vs college) | -1.4283 | 0.7427 | ±1.4855 | -1.923 | 0.0545 | . |
| **Education: high school or below (vs college)** | **+3.8599** | 1.7400 | ±3.4799 | **+2.218** | **0.0265** | * |
| Site: UCSD (vs UAB) | +0.7086 | 1.0014 | ±2.0028 | +0.708 | 0.4792 |  |
| Site: UW (vs UAB) | -0.0643 | 0.8621 | ±1.7242 | -0.075 | 0.9405 |  |
| **Age (years)** | **-0.3974** | 0.0332 | ±0.0664 | **-11.978** | **4.64e-33** | *** |
| BMI (kg/m2) | +0.0261 | 0.0570 | ±0.1139 | +0.458 | 0.6468 |  |
| Hypertension | -0.3450 | 0.8171 | ±1.6342 | -0.422 | 0.6729 |  |
| High cholesterol | -0.1017 | 0.7298 | ±1.4596 | -0.139 | 0.8892 |  |
| Kidney disease | -0.3479 | 1.7002 | ±3.4005 | -0.205 | 0.8379 |  |
| Circulatory disease | -1.9888 | 1.0724 | ±2.1448 | -1.855 | 0.0637 | . |
| Any reading < 54 during wear (0/1) | +0.1846 | 0.7708 | ±1.5416 | +0.239 | 0.8108 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1387**, F-statistic = **17.45** (p = **2.91e-32**), Residual SE = **11.854** on **1113** df, AIC = **8768.1**, BIC = **8828.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.9271** | 2.8769 | ±5.7538 | **+16.659** | **2.60e-62** | *** |
| Education: graduate level (vs college) | -1.4366 | 0.7434 | ±1.4868 | -1.933 | 0.0533 | . |
| **Education: high school or below (vs college)** | **+3.8279** | 1.7430 | ±3.4860 | **+2.196** | **0.0281** | * |
| Site: UCSD (vs UAB) | +0.6548 | 1.0049 | ±2.0097 | +0.652 | 0.5146 |  |
| Site: UW (vs UAB) | -0.0957 | 0.8613 | ±1.7226 | -0.111 | 0.9115 |  |
| **Age (years)** | **-0.3981** | 0.0329 | ±0.0658 | **-12.108** | **9.61e-34** | *** |
| BMI (kg/m2) | +0.0262 | 0.0570 | ±0.1141 | +0.460 | 0.6455 |  |
| Hypertension | -0.3485 | 0.8154 | ±1.6308 | -0.427 | 0.6691 |  |
| High cholesterol | -0.1247 | 0.7312 | ±1.4624 | -0.171 | 0.8646 |  |
| Kidney disease | -0.3474 | 1.6990 | ±3.3980 | -0.204 | 0.8380 |  |
| Circulatory disease | -1.9672 | 1.0702 | ±2.1405 | -1.838 | 0.0660 | . |
| Time < 54 (%) | -0.1286 | 0.6136 | ±1.2272 | -0.210 | 0.8340 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1387**, F-statistic = **17.45** (p = **2.91e-32**), Residual SE = **11.855** on **1113** df, AIC = **8768.1**, BIC = **8828.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.9097** | 2.8701 | ±5.7401 | **+16.693** | **1.48e-62** | *** |
| Education: graduate level (vs college) | -1.4378 | 0.7437 | ±1.4875 | -1.933 | 0.0532 | . |
| **Education: high school or below (vs college)** | **+3.8285** | 1.7423 | ±3.4845 | **+2.197** | **0.0280** | * |
| Site: UCSD (vs UAB) | +0.6585 | 1.0042 | ±2.0083 | +0.656 | 0.5120 |  |
| Site: UW (vs UAB) | -0.0969 | 0.8615 | ±1.7230 | -0.112 | 0.9104 |  |
| **Age (years)** | **-0.3979** | 0.0328 | ±0.0657 | **-12.117** | **8.58e-34** | *** |
| BMI (kg/m2) | +0.0263 | 0.0571 | ±0.1141 | +0.461 | 0.6449 |  |
| Hypertension | -0.3503 | 0.8153 | ±1.6305 | -0.430 | 0.6675 |  |
| High cholesterol | -0.1237 | 0.7303 | ±1.4606 | -0.169 | 0.8655 |  |
| Kidney disease | -0.3481 | 1.6988 | ±3.3976 | -0.205 | 0.8377 |  |
| Circulatory disease | -1.9692 | 1.0697 | ±2.1394 | -1.841 | 0.0656 | . |
| Avg. daily time < 54 (%) | -0.1650 | 0.8196 | ±1.6392 | -0.201 | 0.8405 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1387**, F-statistic = **17.46** (p = **2.85e-32**), Residual SE = **11.854** on **1113** df, AIC = **8768.1**, BIC = **8828.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.9643** | 2.9022 | ±5.8044 | **+16.527** | **2.35e-61** | *** |
| Education: graduate level (vs college) | -1.4444 | 0.7438 | ±1.4876 | -1.942 | 0.0521 | . |
| **Education: high school or below (vs college)** | **+3.8133** | 1.7427 | ±3.4853 | **+2.188** | **0.0287** | * |
| Site: UCSD (vs UAB) | +0.6558 | 0.9975 | ±1.9949 | +0.657 | 0.5109 |  |
| Site: UW (vs UAB) | -0.1021 | 0.8576 | ±1.7152 | -0.119 | 0.9052 |  |
| **Age (years)** | **-0.3984** | 0.0330 | ±0.0659 | **-12.090** | **1.20e-33** | *** |
| BMI (kg/m2) | +0.0267 | 0.0570 | ±0.1140 | +0.469 | 0.6393 |  |
| Hypertension | -0.3518 | 0.8155 | ±1.6310 | -0.431 | 0.6662 |  |
| High cholesterol | -0.1272 | 0.7324 | ±1.4647 | -0.174 | 0.8622 |  |
| Kidney disease | -0.3542 | 1.6985 | ±3.3971 | -0.209 | 0.8348 |  |
| Circulatory disease | -1.9672 | 1.0699 | ±2.1399 | -1.839 | 0.0660 | . |
| Time 54-69, pooled (%) | -0.0724 | 0.2708 | ±0.5416 | -0.267 | 0.7892 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1125**, R² = **0.1472**, Adj R² = **0.1387**, F-statistic = **17.46** (p = **2.81e-32**), Residual SE = **11.854** on **1113** df, AIC = **8768.1**, BIC = **8828.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.9629** | 2.8930 | ±5.7859 | **+16.579** | **9.86e-62** | *** |
| Education: graduate level (vs college) | -1.4477 | 0.7438 | ±1.4876 | -1.946 | 0.0516 | . |
| **Education: high school or below (vs college)** | **+3.8068** | 1.7435 | ±3.4869 | **+2.183** | **0.0290** | * |
| Site: UCSD (vs UAB) | +0.6572 | 0.9967 | ±1.9933 | +0.659 | 0.5097 |  |
| Site: UW (vs UAB) | -0.1060 | 0.8578 | ±1.7156 | -0.124 | 0.9017 |  |
| **Age (years)** | **-0.3983** | 0.0329 | ±0.0658 | **-12.104** | **1.00e-33** | *** |
| BMI (kg/m2) | +0.0267 | 0.0570 | ±0.1140 | +0.469 | 0.6392 |  |
| Hypertension | -0.3544 | 0.8155 | ±1.6311 | -0.435 | 0.6639 |  |
| High cholesterol | -0.1282 | 0.7319 | ±1.4638 | -0.175 | 0.8610 |  |
| Kidney disease | -0.3556 | 1.6980 | ±3.3959 | -0.209 | 0.8341 |  |
| Circulatory disease | -1.9685 | 1.0697 | ±2.1394 | -1.840 | 0.0657 | . |
| Avg. daily time 54-69 (%) | -0.0837 | 0.2766 | ±0.5532 | -0.303 | 0.7622 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1387**, F-statistic = **17.46** (p = **2.84e-32**), Residual SE = **11.854** on **1113** df, AIC = **8768.1**, BIC = **8828.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.9732** | 2.9047 | ±5.8094 | **+16.516** | **2.83e-61** | *** |
| Education: graduate level (vs college) | -1.4438 | 0.7440 | ±1.4880 | -1.941 | 0.0523 | . |
| **Education: high school or below (vs college)** | **+3.8126** | 1.7432 | ±3.4864 | **+2.187** | **0.0287** | * |
| Site: UCSD (vs UAB) | +0.6487 | 1.0003 | ±2.0005 | +0.649 | 0.5167 |  |
| Site: UW (vs UAB) | -0.1062 | 0.8588 | ±1.7175 | -0.124 | 0.9016 |  |
| **Age (years)** | **-0.3984** | 0.0329 | ±0.0659 | **-12.094** | **1.13e-33** | *** |
| BMI (kg/m2) | +0.0266 | 0.0570 | ±0.1140 | +0.466 | 0.6411 |  |
| Hypertension | -0.3527 | 0.8154 | ±1.6307 | -0.433 | 0.6653 |  |
| High cholesterol | -0.1299 | 0.7327 | ±1.4654 | -0.177 | 0.8593 |  |
| Kidney disease | -0.3515 | 1.6986 | ±3.3972 | -0.207 | 0.8361 |  |
| Circulatory disease | -1.9672 | 1.0700 | ±2.1400 | -1.839 | 0.0660 | . |
| Time < 70 (%) | -0.0591 | 0.2055 | ±0.4110 | -0.288 | 0.7737 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1125**, R² = **0.1472**, Adj R² = **0.1387**, F-statistic = **17.46** (p = **2.81e-32**), Residual SE = **11.854** on **1113** df, AIC = **8768.1**, BIC = **8828.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.9632** | 2.8939 | ±5.7877 | **+16.574** | **1.07e-61** | *** |
| Education: graduate level (vs college) | -1.4469 | 0.7441 | ±1.4882 | -1.945 | 0.0518 | . |
| **Education: high school or below (vs college)** | **+3.8078** | 1.7435 | ±3.4870 | **+2.184** | **0.0290** | * |
| Site: UCSD (vs UAB) | +0.6522 | 0.9985 | ±1.9970 | +0.653 | 0.5136 |  |
| Site: UW (vs UAB) | -0.1093 | 0.8587 | ±1.7175 | -0.127 | 0.8987 |  |
| **Age (years)** | **-0.3982** | 0.0329 | ±0.0658 | **-12.108** | **9.58e-34** | *** |
| BMI (kg/m2) | +0.0266 | 0.0570 | ±0.1140 | +0.467 | 0.6405 |  |
| Hypertension | -0.3555 | 0.8154 | ±1.6308 | -0.436 | 0.6629 |  |
| High cholesterol | -0.1299 | 0.7320 | ±1.4639 | -0.177 | 0.8591 |  |
| Kidney disease | -0.3532 | 1.6981 | ±3.3961 | -0.208 | 0.8352 |  |
| Circulatory disease | -1.9691 | 1.0696 | ±2.1393 | -1.841 | 0.0656 | . |
| Avg. daily time < 70 (%) | -0.0690 | 0.2263 | ±0.4527 | -0.305 | 0.7604 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1481**, Adj R² = **0.1396**, F-statistic = **17.59** (p = **1.60e-32**), Residual SE = **11.848** on **1113** df, AIC = **8766.9**, BIC = **8827.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.7288** | 9.7908 | ±19.5817 | **+5.794** | **6.87e-09** | *** |
| Education: graduate level (vs college) | -1.4304 | 0.7425 | ±1.4849 | -1.927 | 0.0540 | . |
| **Education: high school or below (vs college)** | **+3.7819** | 1.7405 | ±3.4809 | **+2.173** | **0.0298** | * |
| Site: UCSD (vs UAB) | +0.6918 | 0.9948 | ±1.9897 | +0.695 | 0.4868 |  |
| Site: UW (vs UAB) | -0.0685 | 0.8592 | ±1.7184 | -0.080 | 0.9364 |  |
| **Age (years)** | **-0.3970** | 0.0329 | ±0.0658 | **-12.070** | **1.52e-33** | *** |
| BMI (kg/m2) | +0.0261 | 0.0570 | ±0.1140 | +0.459 | 0.6465 |  |
| Hypertension | -0.3358 | 0.8147 | ±1.6294 | -0.412 | 0.6802 |  |
| High cholesterol | -0.1185 | 0.7295 | ±1.4589 | -0.162 | 0.8709 |  |
| Kidney disease | -0.3867 | 1.7001 | ±3.4001 | -0.227 | 0.8201 |  |
| Circulatory disease | -2.0171 | 1.0767 | ±2.1535 | -1.873 | 0.0610 | . |
| Time 54-250, pooled (%) | -0.0896 | 0.0942 | ±0.1885 | -0.951 | 0.3416 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1481**, Adj R² = **0.1397**, F-statistic = **17.59** (p = **1.59e-32**), Residual SE = **11.848** on **1113** df, AIC = **8766.9**, BIC = **8827.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.1212** | 10.1068 | ±20.2136 | **+5.652** | **1.59e-08** | *** |
| Education: graduate level (vs college) | -1.4304 | 0.7425 | ±1.4849 | -1.926 | 0.0540 | . |
| **Education: high school or below (vs college)** | **+3.7805** | 1.7408 | ±3.4815 | **+2.172** | **0.0299** | * |
| Site: UCSD (vs UAB) | +0.6863 | 0.9947 | ±1.9895 | +0.690 | 0.4903 |  |
| Site: UW (vs UAB) | -0.0725 | 0.8592 | ±1.7184 | -0.084 | 0.9327 |  |
| **Age (years)** | **-0.3971** | 0.0329 | ±0.0658 | **-12.078** | **1.38e-33** | *** |
| BMI (kg/m2) | +0.0259 | 0.0570 | ±0.1140 | +0.454 | 0.6500 |  |
| Hypertension | -0.3349 | 0.8147 | ±1.6294 | -0.411 | 0.6810 |  |
| High cholesterol | -0.1209 | 0.7294 | ±1.4588 | -0.166 | 0.8684 |  |
| Kidney disease | -0.3844 | 1.6997 | ±3.3995 | -0.226 | 0.8211 |  |
| Circulatory disease | -2.0161 | 1.0767 | ±2.1534 | -1.872 | 0.0611 | . |
| Avg. daily time 54-250 (%) | -0.0933 | 0.0972 | ±0.1944 | -0.960 | 0.3372 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1386**, F-statistic = **17.45** (p = **2.97e-32**), Residual SE = **11.855** on **1113** df, AIC = **8768.2**, BIC = **8828.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8699** | 2.8529 | ±5.7058 | **+16.779** | **3.46e-63** | *** |
| Education: graduate level (vs college) | -1.4340 | 0.7449 | ±1.4898 | -1.925 | 0.0542 | . |
| **Education: high school or below (vs college)** | **+3.8400** | 1.7426 | ±3.4852 | **+2.204** | **0.0276** | * |
| Site: UCSD (vs UAB) | +0.6799 | 0.9972 | ±1.9944 | +0.682 | 0.4953 |  |
| Site: UW (vs UAB) | -0.0770 | 0.8593 | ±1.7187 | -0.090 | 0.9286 |  |
| **Age (years)** | **-0.3980** | 0.0329 | ±0.0659 | **-12.084** | **1.29e-33** | *** |
| BMI (kg/m2) | +0.0264 | 0.0572 | ±0.1144 | +0.462 | 0.6443 |  |
| Hypertension | -0.3433 | 0.8155 | ±1.6311 | -0.421 | 0.6738 |  |
| High cholesterol | -0.1137 | 0.7310 | ±1.4619 | -0.156 | 0.8763 |  |
| Kidney disease | -0.3536 | 1.6927 | ±3.3854 | -0.209 | 0.8345 |  |
| Circulatory disease | -1.9673 | 1.0710 | ±2.1419 | -1.837 | 0.0662 | . |
| Time 181-250, pooled (%) | +0.0004 | 0.0576 | ±0.1153 | +0.007 | 0.9940 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1386**, F-statistic = **17.45** (p = **2.97e-32**), Residual SE = **11.855** on **1113** df, AIC = **8768.2**, BIC = **8828.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8706** | 2.8537 | ±5.7074 | **+16.775** | **3.73e-63** | *** |
| Education: graduate level (vs college) | -1.4328 | 0.7452 | ±1.4904 | -1.923 | 0.0545 | . |
| **Education: high school or below (vs college)** | **+3.8402** | 1.7425 | ±3.4850 | **+2.204** | **0.0275** | * |
| Site: UCSD (vs UAB) | +0.6795 | 0.9978 | ±1.9955 | +0.681 | 0.4959 |  |
| Site: UW (vs UAB) | -0.0753 | 0.8591 | ±1.7183 | -0.088 | 0.9301 |  |
| **Age (years)** | **-0.3980** | 0.0329 | ±0.0659 | **-12.086** | **1.25e-33** | *** |
| BMI (kg/m2) | +0.0265 | 0.0572 | ±0.1145 | +0.463 | 0.6436 |  |
| Hypertension | -0.3405 | 0.8162 | ±1.6323 | -0.417 | 0.6765 |  |
| High cholesterol | -0.1111 | 0.7313 | ±1.4625 | -0.152 | 0.8793 |  |
| Kidney disease | -0.3490 | 1.6927 | ±3.3854 | -0.206 | 0.8366 |  |
| Circulatory disease | -1.9665 | 1.0711 | ±2.1421 | -1.836 | 0.0663 | . |
| Avg. daily time 181-250 (%) | -0.0020 | 0.0570 | ±0.1140 | -0.035 | 0.9720 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1125**, R² = **0.1474**, Adj R² = **0.1389**, F-statistic = **17.49** (p = **2.47e-32**), Residual SE = **11.853** on **1113** df, AIC = **8767.8**, BIC = **8828.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8432** | 2.8483 | ±5.6965 | **+16.797** | **2.55e-63** | *** |
| Education: graduate level (vs college) | -1.4453 | 0.7433 | ±1.4866 | -1.944 | 0.0518 | . |
| **Education: high school or below (vs college)** | **+3.8168** | 1.7427 | ±3.4855 | **+2.190** | **0.0285** | * |
| Site: UCSD (vs UAB) | +0.6814 | 0.9959 | ±1.9918 | +0.684 | 0.4939 |  |
| Site: UW (vs UAB) | -0.0978 | 0.8609 | ±1.7218 | -0.114 | 0.9096 |  |
| **Age (years)** | **-0.3980** | 0.0329 | ±0.0657 | **-12.106** | **9.79e-34** | *** |
| BMI (kg/m2) | +0.0256 | 0.0571 | ±0.1143 | +0.448 | 0.6540 |  |
| Hypertension | -0.3720 | 0.8163 | ±1.6325 | -0.456 | 0.6485 |  |
| High cholesterol | -0.1449 | 0.7299 | ±1.4597 | -0.199 | 0.8426 |  |
| Kidney disease | -0.4098 | 1.6932 | ±3.3864 | -0.242 | 0.8087 |  |
| Circulatory disease | -1.9894 | 1.0733 | ±2.1466 | -1.853 | 0.0638 | . |
| Time > 180 (%) | +0.0260 | 0.0450 | ±0.0900 | +0.578 | 0.5634 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1125**, R² = **0.1473**, Adj R² = **0.1389**, F-statistic = **17.48** (p = **2.55e-32**), Residual SE = **11.853** on **1113** df, AIC = **8767.9**, BIC = **8828.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8507** | 2.8489 | ±5.6978 | **+16.796** | **2.60e-63** | *** |
| Education: graduate level (vs college) | -1.4451 | 0.7434 | ±1.4869 | -1.944 | 0.0519 | . |
| **Education: high school or below (vs college)** | **+3.8215** | 1.7429 | ±3.4859 | **+2.193** | **0.0283** | * |
| Site: UCSD (vs UAB) | +0.6835 | 0.9962 | ±1.9925 | +0.686 | 0.4927 |  |
| Site: UW (vs UAB) | -0.0948 | 0.8608 | ±1.7215 | -0.110 | 0.9123 |  |
| **Age (years)** | **-0.3980** | 0.0329 | ±0.0657 | **-12.106** | **9.80e-34** | *** |
| BMI (kg/m2) | +0.0255 | 0.0572 | ±0.1144 | +0.447 | 0.6550 |  |
| Hypertension | -0.3696 | 0.8166 | ±1.6333 | -0.453 | 0.6509 |  |
| High cholesterol | -0.1426 | 0.7302 | ±1.4604 | -0.195 | 0.8452 |  |
| Kidney disease | -0.4048 | 1.6932 | ±3.3864 | -0.239 | 0.8111 |  |
| Circulatory disease | -1.9879 | 1.0734 | ±2.1467 | -1.852 | 0.0640 | . |
| Avg. daily time > 180 (%) | +0.0237 | 0.0450 | ±0.0899 | +0.526 | 0.5987 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1125**, R² = **0.1471**, Adj R² = **0.1386**, F-statistic = **17.45** (p = **2.97e-32**), Residual SE = **11.855** on **1113** df, AIC = **8768.2**, BIC = **8828.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8716** | 2.8542 | ±5.7084 | **+16.772** | **3.90e-63** | *** |
| Education: graduate level (vs college) | -1.4335 | 0.7429 | ±1.4858 | -1.930 | 0.0537 | . |
| **Education: high school or below (vs college)** | **+3.8386** | 1.7449 | ±3.4898 | **+2.200** | **0.0278** | * |
| Site: UCSD (vs UAB) | +0.6800 | 0.9973 | ±1.9946 | +0.682 | 0.4953 |  |
| Site: UW (vs UAB) | -0.0781 | 0.8610 | ±1.7219 | -0.091 | 0.9277 |  |
| **Age (years)** | **-0.3979** | 0.0329 | ±0.0657 | **-12.111** | **9.27e-34** | *** |
| BMI (kg/m2) | +0.0262 | 0.0578 | ±0.1156 | +0.453 | 0.6508 |  |
| Hypertension | -0.3440 | 0.8169 | ±1.6338 | -0.421 | 0.6737 |  |
| High cholesterol | -0.1170 | 0.7319 | ±1.4639 | -0.160 | 0.8730 |  |
| Kidney disease | -0.3535 | 1.6989 | ±3.3979 | -0.208 | 0.8352 |  |
| Circulatory disease | -1.9677 | 1.0709 | ±2.1417 | -1.837 | 0.0661 | . |
| Nocturnal time > 180 (%) | +0.0025 | 0.0488 | ±0.0976 | +0.052 | 0.9586 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1483**, Adj R² = **0.1399**, F-statistic = **17.62** (p = **1.39e-32**), Residual SE = **11.846** on **1113** df, AIC = **8766.6**, BIC = **8826.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5446** | 2.8702 | ±5.7403 | **+16.565** | **1.25e-61** | *** |
| Education: graduate level (vs college) | -1.4354 | 0.7426 | ±1.4853 | -1.933 | 0.0533 | . |
| **Education: high school or below (vs college)** | **+3.8263** | 1.7370 | ±3.4739 | **+2.203** | **0.0276** | * |
| Site: UCSD (vs UAB) | +0.6755 | 0.9951 | ±1.9903 | +0.679 | 0.4972 |  |
| Site: UW (vs UAB) | -0.1025 | 0.8609 | ±1.7218 | -0.119 | 0.9053 |  |
| **Age (years)** | **-0.3981** | 0.0329 | ±0.0657 | **-12.109** | **9.41e-34** | *** |
| BMI (kg/m2) | +0.0323 | 0.0572 | ±0.1144 | +0.565 | 0.5718 |  |
| Hypertension | -0.4140 | 0.8152 | ±1.6303 | -0.508 | 0.6116 |  |
| High cholesterol | -0.1572 | 0.7281 | ±1.4561 | -0.216 | 0.8290 |  |
| Kidney disease | -0.3942 | 1.6931 | ±3.3863 | -0.233 | 0.8159 |  |
| Circulatory disease | -1.9562 | 1.0706 | ±2.1411 | -1.827 | 0.0677 | . |
| Any reading > 250 during wear (0/1) | +1.1391 | 0.9316 | ±1.8632 | +1.223 | 0.2214 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1125**, R² = **0.1481**, Adj R² = **0.1397**, F-statistic = **17.59** (p = **1.54e-32**), Residual SE = **11.847** on **1113** df, AIC = **8766.8**, BIC = **8827.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8043** | 2.8513 | ±5.7027 | **+16.766** | **4.36e-63** | *** |
| Education: graduate level (vs college) | -1.4324 | 0.7424 | ±1.4847 | -1.929 | 0.0537 | . |
| **Education: high school or below (vs college)** | **+3.7707** | 1.7408 | ±3.4816 | **+2.166** | **0.0303** | * |
| Site: UCSD (vs UAB) | +0.6740 | 0.9948 | ±1.9896 | +0.678 | 0.4981 |  |
| Site: UW (vs UAB) | -0.0820 | 0.8593 | ±1.7185 | -0.095 | 0.9240 |  |
| **Age (years)** | **-0.3970** | 0.0329 | ±0.0658 | **-12.075** | **1.43e-33** | *** |
| BMI (kg/m2) | +0.0260 | 0.0570 | ±0.1139 | +0.456 | 0.6481 |  |
| Hypertension | -0.3396 | 0.8147 | ±1.6293 | -0.417 | 0.6767 |  |
| High cholesterol | -0.1270 | 0.7293 | ±1.4586 | -0.174 | 0.8618 |  |
| Kidney disease | -0.3841 | 1.6996 | ±3.3992 | -0.226 | 0.8212 |  |
| Circulatory disease | -2.0191 | 1.0769 | ±2.1537 | -1.875 | 0.0608 | . |
| Time > 250 (%) | +0.0932 | 0.0947 | ±0.1895 | +0.984 | 0.3252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,125)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1125**, R² = **0.1481**, Adj R² = **0.1397**, F-statistic = **17.59** (p = **1.55e-32**), Residual SE = **11.847** on **1113** df, AIC = **8766.8**, BIC = **8827.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8140** | 2.8511 | ±5.7022 | **+16.770** | **4.02e-63** | *** |
| Education: graduate level (vs college) | -1.4326 | 0.7424 | ±1.4848 | -1.930 | 0.0536 | . |
| **Education: high school or below (vs college)** | **+3.7721** | 1.7410 | ±3.4820 | **+2.167** | **0.0303** | * |
| Site: UCSD (vs UAB) | +0.6740 | 0.9948 | ±1.9895 | +0.678 | 0.4981 |  |
| Site: UW (vs UAB) | -0.0842 | 0.8594 | ±1.7187 | -0.098 | 0.9220 |  |
| **Age (years)** | **-0.3971** | 0.0329 | ±0.0658 | **-12.077** | **1.39e-33** | *** |
| BMI (kg/m2) | +0.0258 | 0.0570 | ±0.1140 | +0.452 | 0.6511 |  |
| Hypertension | -0.3390 | 0.8147 | ±1.6294 | -0.416 | 0.6773 |  |
| High cholesterol | -0.1271 | 0.7293 | ±1.4586 | -0.174 | 0.8617 |  |
| Kidney disease | -0.3825 | 1.6994 | ±3.3989 | -0.225 | 0.8219 |  |
| Circulatory disease | -2.0186 | 1.0767 | ±2.1534 | -1.875 | 0.0608 | . |
| Avg. daily time > 250 (%) | +0.0959 | 0.0975 | ±0.1950 | +0.983 | 0.3254 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 1,128; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1128**, R² = **0.1380**, Adj R² = **0.1303**, F-statistic = **17.89** (p = **1.47e-30**), Residual SE = **7.415** on **1117** df, AIC = **7732.0**, BIC = **7787.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6111** | 2.0009 | ±4.0018 | **+31.292** | **6.04e-215** | *** |
| Education: graduate level (vs college) | -0.8967 | 0.4744 | ±0.9487 | -1.890 | 0.0587 | . |
| Education: high school or below (vs college) | -0.1804 | 0.9266 | ±1.8533 | -0.195 | 0.8456 |  |
| **Site: UCSD (vs UAB)** | **-1.9665** | 0.6187 | ±1.2375 | **-3.178** | **0.0015** | ** |
| **Site: UW (vs UAB)** | **-2.3272** | 0.5477 | ±1.0954 | **-4.249** | **2.15e-05** | *** |
| **Age (years)** | **-0.1303** | 0.0216 | ±0.0432 | **-6.039** | **1.55e-09** | *** |
| **BMI (kg/m2)** | **+0.2547** | 0.0394 | ±0.0789 | **+6.458** | **1.06e-10** | *** |
| Hypertension | +0.5130 | 0.5143 | ±1.0287 | +0.997 | 0.3185 |  |
| High cholesterol | -0.3462 | 0.4651 | ±0.9302 | -0.744 | 0.4567 |  |
| Kidney disease | +0.8191 | 1.0332 | ±2.0664 | +0.793 | 0.4279 |  |
| Circulatory disease | +0.3881 | 0.6883 | ±1.3767 | +0.564 | 0.5729 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1128**, R² = **0.1481**, Adj R² = **0.1397**, F-statistic = **17.63** (p = **1.26e-32**), Residual SE = **7.375** on **1116** df, AIC = **7720.7**, BIC = **7781.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.8216** | 2.7690 | ±5.5379 | **+19.799** | **3.06e-87** | *** |
| Education: graduate level (vs college) | -0.8949 | 0.4717 | ±0.9435 | -1.897 | 0.0578 | . |
| Education: high school or below (vs college) | -0.3540 | 0.9115 | ±1.8230 | -0.388 | 0.6977 |  |
| **Site: UCSD (vs UAB)** | **-2.0459** | 0.6184 | ±1.2368 | **-3.308** | **9.38e-04** | *** |
| **Site: UW (vs UAB)** | **-2.3954** | 0.5430 | ±1.0860 | **-4.411** | **1.03e-05** | *** |
| **Age (years)** | **-0.1365** | 0.0215 | ±0.0431 | **-6.338** | **2.32e-10** | *** |
| **BMI (kg/m2)** | **+0.2437** | 0.0387 | ±0.0774 | **+6.294** | **3.09e-10** | *** |
| Hypertension | +0.4398 | 0.5117 | ±1.0233 | +0.860 | 0.3900 |  |
| High cholesterol | -0.5650 | 0.4606 | ±0.9211 | -1.227 | 0.2199 |  |
| Kidney disease | +0.8213 | 1.0210 | ±2.0419 | +0.804 | 0.4212 |  |
| Circulatory disease | +0.3031 | 0.6654 | ±1.3309 | +0.455 | 0.6488 |  |
| **HbA1c (%)** | **+1.5335** | 0.4072 | ±0.8144 | **+3.766** | **1.66e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1128**, R² = **0.1478**, Adj R² = **0.1394**, F-statistic = **17.60** (p = **1.48e-32**), Residual SE = **7.376** on **1116** df, AIC = **7721.1**, BIC = **7781.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.0003** | 2.4051 | ±4.8101 | **+24.116** | **1.70e-128** | *** |
| **Education: graduate level (vs college)** | **-0.9726** | 0.4731 | ±0.9463 | **-2.056** | **0.0398** | * |
| Education: high school or below (vs college) | -0.3197 | 0.9066 | ±1.8131 | -0.353 | 0.7244 |  |
| **Site: UCSD (vs UAB)** | **-2.0043** | 0.6180 | ±1.2360 | **-3.243** | **0.0012** | ** |
| **Site: UW (vs UAB)** | **-2.4817** | 0.5463 | ±1.0927 | **-4.542** | **5.56e-06** | *** |
| **Age (years)** | **-0.1325** | 0.0214 | ±0.0428 | **-6.190** | **6.03e-10** | *** |
| **BMI (kg/m2)** | **+0.2486** | 0.0392 | ±0.0784 | **+6.344** | **2.23e-10** | *** |
| Hypertension | +0.3703 | 0.5148 | ±1.0295 | +0.719 | 0.4719 |  |
| High cholesterol | -0.4799 | 0.4612 | ±0.9225 | -1.040 | 0.2982 |  |
| Kidney disease | +0.6393 | 1.0174 | ±2.0348 | +0.628 | 0.5298 |  |
| Circulatory disease | +0.3185 | 0.6682 | ±1.3364 | +0.477 | 0.6336 |  |
| **Mean glucose (mg/dL)** | **+0.0428** | 0.0133 | ±0.0267 | **+3.207** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1128**, R² = **0.1478**, Adj R² = **0.1394**, F-statistic = **17.60** (p = **1.48e-32**), Residual SE = **7.376** on **1116** df, AIC = **7721.1**, BIC = **7781.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.0832** | 3.7783 | ±7.5566 | **+13.785** | **3.15e-43** | *** |
| **Education: graduate level (vs college)** | **-0.9726** | 0.4731 | ±0.9463 | **-2.056** | **0.0398** | * |
| Education: high school or below (vs college) | -0.3197 | 0.9066 | ±1.8131 | -0.353 | 0.7244 |  |
| **Site: UCSD (vs UAB)** | **-2.0043** | 0.6180 | ±1.2360 | **-3.243** | **0.0012** | ** |
| **Site: UW (vs UAB)** | **-2.4817** | 0.5463 | ±1.0927 | **-4.542** | **5.56e-06** | *** |
| **Age (years)** | **-0.1325** | 0.0214 | ±0.0428 | **-6.190** | **6.03e-10** | *** |
| **BMI (kg/m2)** | **+0.2486** | 0.0392 | ±0.0784 | **+6.344** | **2.23e-10** | *** |
| Hypertension | +0.3703 | 0.5148 | ±1.0295 | +0.719 | 0.4719 |  |
| High cholesterol | -0.4799 | 0.4612 | ±0.9225 | -1.040 | 0.2982 |  |
| Kidney disease | +0.6393 | 1.0174 | ±2.0348 | +0.628 | 0.5298 |  |
| Circulatory disease | +0.3185 | 0.6682 | ±1.3364 | +0.477 | 0.6336 |  |
| **GMI (%)** | **+1.7876** | 0.5573 | ±1.1147 | **+3.207** | **0.0013** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1128**, R² = **0.1466**, Adj R² = **0.1382**, F-statistic = **17.43** (p = **3.13e-32**), Residual SE = **7.381** on **1116** df, AIC = **7722.7**, BIC = **7783.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.5668** | 2.3312 | ±4.6623 | **+25.123** | **2.76e-139** | *** |
| **Education: graduate level (vs college)** | **-0.9331** | 0.4727 | ±0.9454 | **-1.974** | **0.0484** | * |
| Education: high school or below (vs college) | -0.3110 | 0.9089 | ±1.8178 | -0.342 | 0.7322 |  |
| **Site: UCSD (vs UAB)** | **-2.0509** | 0.6192 | ±1.2383 | **-3.312** | **9.25e-04** | *** |
| **Site: UW (vs UAB)** | **-2.4617** | 0.5456 | ±1.0912 | **-4.512** | **6.43e-06** | *** |
| **Age (years)** | **-0.1287** | 0.0214 | ±0.0428 | **-6.008** | **1.87e-09** | *** |
| **BMI (kg/m2)** | **+0.2395** | 0.0391 | ±0.0782 | **+6.124** | **9.11e-10** | *** |
| Hypertension | +0.4073 | 0.5141 | ±1.0281 | +0.792 | 0.4282 |  |
| High cholesterol | -0.4976 | 0.4625 | ±0.9249 | -1.076 | 0.2819 |  |
| Kidney disease | +0.7682 | 1.0159 | ±2.0319 | +0.756 | 0.4496 |  |
| Circulatory disease | +0.3595 | 0.6699 | ±1.3398 | +0.537 | 0.5916 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0384** | 0.0128 | ±0.0256 | **+3.004** | **0.0027** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1128**, R² = **0.1480**, Adj R² = **0.1397**, F-statistic = **17.63** (p = **1.29e-32**), Residual SE = **7.375** on **1116** df, AIC = **7720.8**, BIC = **7781.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.1552** | 2.0610 | ±4.1220 | **+29.188** | **2.78e-187** | *** |
| Education: graduate level (vs college) | -0.9105 | 0.4706 | ±0.9412 | -1.935 | 0.0530 | . |
| Education: high school or below (vs college) | -0.2003 | 0.9060 | ±1.8121 | -0.221 | 0.8250 |  |
| **Site: UCSD (vs UAB)** | **-1.8946** | 0.6162 | ±1.2324 | **-3.075** | **0.0021** | ** |
| **Site: UW (vs UAB)** | **-2.4054** | 0.5448 | ±1.0897 | **-4.415** | **1.01e-05** | *** |
| **Age (years)** | **-0.1338** | 0.0214 | ±0.0428 | **-6.246** | **4.22e-10** | *** |
| **BMI (kg/m2)** | **+0.2571** | 0.0392 | ±0.0785 | **+6.552** | **5.68e-11** | *** |
| Hypertension | +0.3531 | 0.5150 | ±1.0301 | +0.686 | 0.4929 |  |
| High cholesterol | -0.3889 | 0.4617 | ±0.9235 | -0.842 | 0.3996 |  |
| Kidney disease | +0.5135 | 1.0325 | ±2.0651 | +0.497 | 0.6190 |  |
| Circulatory disease | +0.3235 | 0.6671 | ±1.3343 | +0.485 | 0.6278 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.1259** | 0.0371 | ±0.0742 | **+3.392** | **6.93e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1128**, R² = **0.1469**, Adj R² = **0.1384**, F-statistic = **17.46** (p = **2.71e-32**), Residual SE = **7.380** on **1116** df, AIC = **7722.4**, BIC = **7782.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.5294** | 2.0357 | ±4.0713 | **+29.735** | **2.75e-194** | *** |
| Education: graduate level (vs college) | -0.9197 | 0.4714 | ±0.9428 | -1.951 | 0.0511 | . |
| Education: high school or below (vs college) | -0.2103 | 0.9074 | ±1.8148 | -0.232 | 0.8167 |  |
| **Site: UCSD (vs UAB)** | **-1.9161** | 0.6159 | ±1.2317 | **-3.111** | **0.0019** | ** |
| **Site: UW (vs UAB)** | **-2.4157** | 0.5463 | ±1.0926 | **-4.422** | **9.78e-06** | *** |
| **Age (years)** | **-0.1345** | 0.0215 | ±0.0429 | **-6.264** | **3.75e-10** | *** |
| **BMI (kg/m2)** | **+0.2551** | 0.0391 | ±0.0781 | **+6.530** | **6.59e-11** | *** |
| Hypertension | +0.3634 | 0.5169 | ±1.0338 | +0.703 | 0.4820 |  |
| High cholesterol | -0.3875 | 0.4621 | ±0.9243 | -0.839 | 0.4017 |  |
| Kidney disease | +0.5395 | 1.0295 | ±2.0589 | +0.524 | 0.6002 |  |
| Circulatory disease | +0.3282 | 0.6686 | ±1.3372 | +0.491 | 0.6236 |  |
| **Avg. daily SD (mg/dL)** | **+0.1250** | 0.0393 | ±0.0787 | **+3.178** | **0.0015** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1128**, R² = **0.1419**, Adj R² = **0.1335**, F-statistic = **16.78** (p = **5.84e-31**), Residual SE = **7.402** on **1116** df, AIC = **7728.9**, BIC = **7789.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.3685** | 2.1660 | ±4.3320 | **+27.871** | **6.01e-171** | *** |
| Education: graduate level (vs college) | -0.8719 | 0.4723 | ±0.9446 | -1.846 | 0.0649 | . |
| Education: high school or below (vs college) | -0.1391 | 0.9197 | ±1.8393 | -0.151 | 0.8798 |  |
| **Site: UCSD (vs UAB)** | **-1.8826** | 0.6170 | ±1.2341 | **-3.051** | **0.0023** | ** |
| **Site: UW (vs UAB)** | **-2.3156** | 0.5464 | ±1.0928 | **-4.238** | **2.25e-05** | *** |
| **Age (years)** | **-0.1324** | 0.0216 | ±0.0432 | **-6.134** | **8.55e-10** | *** |
| **BMI (kg/m2)** | **+0.2591** | 0.0395 | ±0.0790 | **+6.560** | **5.38e-11** | *** |
| Hypertension | +0.4497 | 0.5139 | ±1.0277 | +0.875 | 0.3815 |  |
| High cholesterol | -0.3141 | 0.4654 | ±0.9307 | -0.675 | 0.4997 |  |
| Kidney disease | +0.6686 | 1.0411 | ±2.0822 | +0.642 | 0.5208 |  |
| Circulatory disease | +0.3741 | 0.6809 | ±1.3617 | +0.549 | 0.5827 |  |
| **CV (%)** | **+0.1246** | 0.0538 | ±0.1077 | **+2.316** | **0.0206** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1128**, R² = **0.1422**, Adj R² = **0.1337**, F-statistic = **16.82** (p = **4.92e-31**), Residual SE = **7.400** on **1116** df, AIC = **7728.5**, BIC = **7788.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.1189** | 2.2941 | ±4.5883 | **+28.385** | **3.10e-177** | *** |
| Education: graduate level (vs college) | -0.8661 | 0.4720 | ±0.9440 | -1.835 | 0.0665 | . |
| Education: high school or below (vs college) | -0.1669 | 0.9195 | ±1.8391 | -0.182 | 0.8560 |  |
| **Site: UCSD (vs UAB)** | **-1.8853** | 0.6169 | ±1.2337 | **-3.056** | **0.0022** | ** |
| **Site: UW (vs UAB)** | **-2.3416** | 0.5465 | ±1.0929 | **-4.285** | **1.83e-05** | *** |
| **Age (years)** | **-0.1326** | 0.0216 | ±0.0432 | **-6.141** | **8.20e-10** | *** |
| **BMI (kg/m2)** | **+0.2585** | 0.0394 | ±0.0788 | **+6.562** | **5.32e-11** | *** |
| Hypertension | +0.4368 | 0.5138 | ±1.0276 | +0.850 | 0.3953 |  |
| High cholesterol | -0.3230 | 0.4650 | ±0.9299 | -0.695 | 0.4873 |  |
| Kidney disease | +0.7096 | 1.0388 | ±2.0775 | +0.683 | 0.4946 |  |
| Circulatory disease | +0.3788 | 0.6803 | ±1.3606 | +0.557 | 0.5777 |  |
| **Mean / SD ratio** | **-0.4227** | 0.1740 | ±0.3480 | **-2.429** | **0.0151** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1128**, R² = **0.1420**, Adj R² = **0.1335**, F-statistic = **16.79** (p = **5.59e-31**), Residual SE = **7.401** on **1116** df, AIC = **7728.8**, BIC = **7789.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.0911** | 2.3024 | ±4.6049 | **+28.270** | **8.00e-176** | *** |
| Education: graduate level (vs college) | -0.8843 | 0.4724 | ±0.9447 | -1.872 | 0.0612 | . |
| Education: high school or below (vs college) | -0.1961 | 0.9192 | ±1.8385 | -0.213 | 0.8311 |  |
| **Site: UCSD (vs UAB)** | **-1.9065** | 0.6167 | ±1.2333 | **-3.092** | **0.0020** | ** |
| **Site: UW (vs UAB)** | **-2.3545** | 0.5472 | ±1.0944 | **-4.303** | **1.69e-05** | *** |
| **Age (years)** | **-0.1336** | 0.0217 | ±0.0433 | **-6.166** | **6.99e-10** | *** |
| **BMI (kg/m2)** | **+0.2561** | 0.0392 | ±0.0783 | **+6.537** | **6.27e-11** | *** |
| Hypertension | +0.4561 | 0.5151 | ±1.0302 | +0.886 | 0.3759 |  |
| High cholesterol | -0.3256 | 0.4652 | ±0.9304 | -0.700 | 0.4840 |  |
| Kidney disease | +0.6915 | 1.0358 | ±2.0716 | +0.668 | 0.5044 |  |
| Circulatory disease | +0.3842 | 0.6814 | ±1.3627 | +0.564 | 0.5728 |  |
| **Avg. daily mean/SD** | **-0.3429** | 0.1454 | ±0.2908 | **-2.358** | **0.0184** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1128**, R² = **0.1477**, Adj R² = **0.1393**, F-statistic = **17.59** (p = **1.56e-32**), Residual SE = **7.376** on **1116** df, AIC = **7721.2**, BIC = **7781.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.3888** | 2.2798 | ±4.5597 | **+25.611** | **1.15e-144** | *** |
| Education: graduate level (vs college) | -0.8587 | 0.4700 | ±0.9400 | -1.827 | 0.0677 | . |
| Education: high school or below (vs college) | -0.2433 | 0.9137 | ±1.8273 | -0.266 | 0.7900 |  |
| **Site: UCSD (vs UAB)** | **-1.8593** | 0.6156 | ±1.2313 | **-3.020** | **0.0025** | ** |
| **Site: UW (vs UAB)** | **-2.2175** | 0.5491 | ±1.0982 | **-4.039** | **5.38e-05** | *** |
| **Age (years)** | **-0.1272** | 0.0214 | ±0.0428 | **-5.950** | **2.68e-09** | *** |
| **BMI (kg/m2)** | **+0.2569** | 0.0388 | ±0.0775 | **+6.628** | **3.40e-11** | *** |
| Hypertension | +0.5257 | 0.5142 | ±1.0285 | +1.022 | 0.3066 |  |
| High cholesterol | -0.2921 | 0.4636 | ±0.9272 | -0.630 | 0.5286 |  |
| Kidney disease | +0.6851 | 1.0235 | ±2.0469 | +0.669 | 0.5032 |  |
| Circulatory disease | +0.4285 | 0.6780 | ±1.3560 | +0.632 | 0.5274 |  |
| **MAG (mg/dL/h)** | **+0.1013** | 0.0304 | ±0.0609 | **+3.329** | **8.71e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1128**, R² = **0.1450**, Adj R² = **0.1365**, F-statistic = **17.20** (p = **8.85e-32**), Residual SE = **7.388** on **1116** df, AIC = **7724.9**, BIC = **7785.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.0904** | 2.1233 | ±4.2466 | **+28.301** | **3.38e-176** | *** |
| Education: graduate level (vs college) | -0.9188 | 0.4722 | ±0.9443 | -1.946 | 0.0517 | . |
| Education: high school or below (vs college) | -0.2297 | 0.9111 | ±1.8223 | -0.252 | 0.8010 |  |
| **Site: UCSD (vs UAB)** | **-1.9209** | 0.6160 | ±1.2319 | **-3.119** | **0.0018** | ** |
| **Site: UW (vs UAB)** | **-2.3794** | 0.5465 | ±1.0930 | **-4.354** | **1.34e-05** | *** |
| **Age (years)** | **-0.1331** | 0.0215 | ±0.0430 | **-6.189** | **6.07e-10** | *** |
| **BMI (kg/m2)** | **+0.2616** | 0.0395 | ±0.0790 | **+6.618** | **3.64e-11** | *** |
| Hypertension | +0.4196 | 0.5168 | ±1.0337 | +0.812 | 0.4168 |  |
| High cholesterol | -0.3497 | 0.4638 | ±0.9275 | -0.754 | 0.4508 |  |
| Kidney disease | +0.6286 | 1.0318 | ±2.0636 | +0.609 | 0.5424 |  |
| Circulatory disease | +0.3459 | 0.6733 | ±1.3466 | +0.514 | 0.6074 |  |
| **Avg. daily range (mg/dL)** | **+0.0260** | 0.0088 | ±0.0176 | **+2.965** | **0.0030** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1128**, R² = **0.1516**, Adj R² = **0.1432**, F-statistic = **18.12** (p = **1.41e-33**), Residual SE = **7.360** on **1116** df, AIC = **7716.1**, BIC = **7776.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.7469** | 2.0032 | ±4.0064 | **+30.325** | **5.34e-202** | *** |
| Education: graduate level (vs college) | -0.9071 | 0.4698 | ±0.9395 | -1.931 | 0.0535 | . |
| Education: high school or below (vs college) | -0.1098 | 0.9051 | ±1.8103 | -0.121 | 0.9034 |  |
| **Site: UCSD (vs UAB)** | **-1.8198** | 0.6149 | ±1.2298 | **-2.960** | **0.0031** | ** |
| **Site: UW (vs UAB)** | **-2.3464** | 0.5402 | ±1.0805 | **-4.343** | **1.40e-05** | *** |
| **Age (years)** | **-0.1286** | 0.0213 | ±0.0426 | **-6.039** | **1.56e-09** | *** |
| **BMI (kg/m2)** | **+0.2485** | 0.0393 | ±0.0787 | **+6.316** | **2.69e-10** | *** |
| Hypertension | +0.4652 | 0.5084 | ±1.0169 | +0.915 | 0.3602 |  |
| High cholesterol | -0.4404 | 0.4614 | ±0.9227 | -0.955 | 0.3398 |  |
| Kidney disease | +0.7289 | 1.0283 | ±2.0566 | +0.709 | 0.4784 |  |
| Circulatory disease | +0.3345 | 0.6707 | ±1.3414 | +0.499 | 0.6180 |  |
| **SD of daily means (mg/dL)** | **+0.2998** | 0.0759 | ±0.1518 | **+3.950** | **7.81e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1128**, R² = **0.1463**, Adj R² = **0.1378**, F-statistic = **17.38** (p = **3.92e-32**), Residual SE = **7.383** on **1116** df, AIC = **7723.1**, BIC = **7783.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.8747** | 3.9915 | ±7.9830 | **+17.756** | **1.54e-70** | *** |
| Education: graduate level (vs college) | -0.9193 | 0.4716 | ±0.9433 | -1.949 | 0.0513 | . |
| Education: high school or below (vs college) | -0.2230 | 0.9094 | ±1.8187 | -0.245 | 0.8062 |  |
| **Site: UCSD (vs UAB)** | **-1.9181** | 0.6187 | ±1.2374 | **-3.100** | **0.0019** | ** |
| **Site: UW (vs UAB)** | **-2.3534** | 0.5434 | ±1.0869 | **-4.330** | **1.49e-05** | *** |
| **Age (years)** | **-0.1297** | 0.0214 | ±0.0427 | **-6.072** | **1.26e-09** | *** |
| **BMI (kg/m2)** | **+0.2519** | 0.0393 | ±0.0787 | **+6.405** | **1.50e-10** | *** |
| Hypertension | +0.4303 | 0.5140 | ±1.0280 | +0.837 | 0.4025 |  |
| High cholesterol | -0.4239 | 0.4623 | ±0.9246 | -0.917 | 0.3592 |  |
| Kidney disease | +0.6241 | 1.0250 | ±2.0499 | +0.609 | 0.5426 |  |
| Circulatory disease | +0.3156 | 0.6719 | ±1.3438 | +0.470 | 0.6385 |  |
| **Time in range 70-180, pooled (%)** | **-0.0850** | 0.0347 | ±0.0693 | **-2.453** | **0.0142** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1128**, R² = **0.1459**, Adj R² = **0.1375**, F-statistic = **17.33** (p = **4.90e-32**), Residual SE = **7.384** on **1116** df, AIC = **7723.6**, BIC = **7783.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+70.7173** | 4.0101 | ±8.0202 | **+17.635** | **1.33e-69** | *** |
| Education: graduate level (vs college) | -0.9198 | 0.4718 | ±0.9436 | -1.949 | 0.0512 | . |
| Education: high school or below (vs college) | -0.2118 | 0.9094 | ±1.8189 | -0.233 | 0.8158 |  |
| **Site: UCSD (vs UAB)** | **-1.9219** | 0.6186 | ±1.2371 | **-3.107** | **0.0019** | ** |
| **Site: UW (vs UAB)** | **-2.3512** | 0.5436 | ±1.0872 | **-4.325** | **1.52e-05** | *** |
| **Age (years)** | **-0.1300** | 0.0214 | ±0.0428 | **-6.079** | **1.21e-09** | *** |
| **BMI (kg/m2)** | **+0.2515** | 0.0393 | ±0.0786 | **+6.401** | **1.55e-10** | *** |
| Hypertension | +0.4330 | 0.5140 | ±1.0281 | +0.842 | 0.3996 |  |
| High cholesterol | -0.4274 | 0.4624 | ±0.9248 | -0.924 | 0.3553 |  |
| Kidney disease | +0.6315 | 1.0250 | ±2.0500 | +0.616 | 0.5378 |  |
| Circulatory disease | +0.3179 | 0.6724 | ±1.3447 | +0.473 | 0.6363 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0829** | 0.0346 | ±0.0691 | **-2.397** | **0.0165** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1128**, R² = **0.1387**, Adj R² = **0.1302**, F-statistic = **16.33** (p = **4.32e-30**), Residual SE = **7.415** on **1116** df, AIC = **7733.1**, BIC = **7793.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.3606** | 2.0120 | ±4.0239 | **+30.995** | **6.34e-211** | *** |
| Education: graduate level (vs college) | -0.8836 | 0.4751 | ±0.9503 | -1.860 | 0.0629 | . |
| Education: high school or below (vs college) | -0.1358 | 0.9340 | ±1.8679 | -0.145 | 0.8844 |  |
| **Site: UCSD (vs UAB)** | **-1.8975** | 0.6227 | ±1.2454 | **-3.047** | **0.0023** | ** |
| **Site: UW (vs UAB)** | **-2.2973** | 0.5490 | ±1.0980 | **-4.185** | **2.86e-05** | *** |
| **Age (years)** | **-0.1290** | 0.0216 | ±0.0432 | **-5.976** | **2.28e-09** | *** |
| **BMI (kg/m2)** | **+0.2540** | 0.0394 | ±0.0788 | **+6.446** | **1.15e-10** | *** |
| Hypertension | +0.5078 | 0.5155 | ±1.0309 | +0.985 | 0.3246 |  |
| High cholesterol | -0.3188 | 0.4660 | ±0.9321 | -0.684 | 0.4940 |  |
| Kidney disease | +0.8285 | 1.0360 | ±2.0721 | +0.800 | 0.4239 |  |
| Circulatory disease | +0.3372 | 0.6914 | ±1.3829 | +0.488 | 0.6257 |  |
| Any reading < 54 during wear (0/1) | +0.4364 | 0.4846 | ±0.9693 | +0.900 | 0.3679 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1128**, R² = **0.1385**, Adj R² = **0.1300**, F-statistic = **16.31** (p = **4.84e-30**), Residual SE = **7.416** on **1116** df, AIC = **7733.4**, BIC = **7793.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.4834** | 2.0133 | ±4.0267 | **+31.035** | **1.84e-211** | *** |
| Education: graduate level (vs college) | -0.8901 | 0.4745 | ±0.9490 | -1.876 | 0.0607 | . |
| Education: high school or below (vs college) | -0.1533 | 0.9282 | ±1.8563 | -0.165 | 0.8688 |  |
| **Site: UCSD (vs UAB)** | **-1.9102** | 0.6231 | ±1.2462 | **-3.066** | **0.0022** | ** |
| **Site: UW (vs UAB)** | **-2.2847** | 0.5507 | ±1.1014 | **-4.149** | **3.34e-05** | *** |
| **Age (years)** | **-0.1300** | 0.0216 | ±0.0432 | **-6.018** | **1.77e-09** | *** |
| **BMI (kg/m2)** | **+0.2551** | 0.0395 | ±0.0790 | **+6.459** | **1.06e-10** | *** |
| Hypertension | +0.5255 | 0.5148 | ±1.0297 | +1.021 | 0.3074 |  |
| High cholesterol | -0.3206 | 0.4659 | ±0.9317 | -0.688 | 0.4913 |  |
| Kidney disease | +0.8065 | 1.0346 | ±2.0692 | +0.780 | 0.4357 |  |
| Circulatory disease | +0.3879 | 0.6889 | ±1.3778 | +0.563 | 0.5734 |  |
| Time < 54 (%) | +0.2878 | 0.2594 | ±0.5189 | +1.109 | 0.2673 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1128**, R² = **0.1383**, Adj R² = **0.1298**, F-statistic = **16.28** (p = **5.54e-30**), Residual SE = **7.417** on **1116** df, AIC = **7733.6**, BIC = **7794.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5443** | 2.0091 | ±4.0183 | **+31.130** | **9.44e-213** | *** |
| Education: graduate level (vs college) | -0.8898 | 0.4748 | ±0.9495 | -1.874 | 0.0609 | . |
| Education: high school or below (vs college) | -0.1610 | 0.9280 | ±1.8560 | -0.174 | 0.8623 |  |
| **Site: UCSD (vs UAB)** | **-1.9303** | 0.6222 | ±1.2443 | **-3.103** | **0.0019** | ** |
| **Site: UW (vs UAB)** | **-2.2933** | 0.5511 | ±1.1022 | **-4.161** | **3.16e-05** | *** |
| **Age (years)** | **-0.1304** | 0.0216 | ±0.0432 | **-6.037** | **1.57e-09** | *** |
| **BMI (kg/m2)** | **+0.2549** | 0.0395 | ±0.0790 | **+6.456** | **1.08e-10** | *** |
| Hypertension | +0.5254 | 0.5153 | ±1.0306 | +1.020 | 0.3079 |  |
| High cholesterol | -0.3287 | 0.4663 | ±0.9326 | -0.705 | 0.4809 |  |
| Kidney disease | +0.8109 | 1.0340 | ±2.0680 | +0.784 | 0.4329 |  |
| Circulatory disease | +0.3913 | 0.6889 | ±1.3778 | +0.568 | 0.5700 |  |
| Avg. daily time < 54 (%) | +0.2783 | 0.3599 | ±0.7198 | +0.773 | 0.4393 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1128**, R² = **0.1380**, Adj R² = **0.1295**, F-statistic = **16.25** (p = **6.41e-30**), Residual SE = **7.418** on **1116** df, AIC = **7734.0**, BIC = **7794.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6064** | 2.0152 | ±4.0304 | **+31.067** | **6.72e-212** | *** |
| Education: graduate level (vs college) | -0.8962 | 0.4760 | ±0.9520 | -1.883 | 0.0597 | . |
| Education: high school or below (vs college) | -0.1791 | 0.9300 | ±1.8599 | -0.193 | 0.8473 |  |
| **Site: UCSD (vs UAB)** | **-1.9653** | 0.6221 | ±1.2441 | **-3.159** | **0.0016** | ** |
| **Site: UW (vs UAB)** | **-2.3260** | 0.5514 | ±1.1029 | **-4.218** | **2.47e-05** | *** |
| **Age (years)** | **-0.1303** | 0.0216 | ±0.0432 | **-6.029** | **1.65e-09** | *** |
| **BMI (kg/m2)** | **+0.2546** | 0.0395 | ±0.0789 | **+6.454** | **1.09e-10** | *** |
| Hypertension | +0.5135 | 0.5153 | ±1.0305 | +0.997 | 0.3190 |  |
| High cholesterol | -0.3455 | 0.4659 | ±0.9318 | -0.742 | 0.4584 |  |
| Kidney disease | +0.8192 | 1.0339 | ±2.0678 | +0.792 | 0.4282 |  |
| Circulatory disease | +0.3881 | 0.6887 | ±1.3773 | +0.563 | 0.5731 |  |
| Time 54-69, pooled (%) | +0.0036 | 0.1461 | ±0.2922 | +0.025 | 0.9803 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1128**, R² = **0.1380**, Adj R² = **0.1295**, F-statistic = **16.25** (p = **6.40e-30**), Residual SE = **7.418** on **1116** df, AIC = **7734.0**, BIC = **7794.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6051** | 2.0120 | ±4.0240 | **+31.116** | **1.48e-212** | *** |
| Education: graduate level (vs college) | -0.8958 | 0.4765 | ±0.9529 | -1.880 | 0.0601 | . |
| Education: high school or below (vs college) | -0.1783 | 0.9308 | ±1.8616 | -0.192 | 0.8481 |  |
| **Site: UCSD (vs UAB)** | **-1.9650** | 0.6209 | ±1.2419 | **-3.165** | **0.0016** | ** |
| **Site: UW (vs UAB)** | **-2.3253** | 0.5511 | ±1.1021 | **-4.220** | **2.45e-05** | *** |
| **Age (years)** | **-0.1303** | 0.0216 | ±0.0432 | **-6.033** | **1.61e-09** | *** |
| **BMI (kg/m2)** | **+0.2546** | 0.0395 | ±0.0789 | **+6.454** | **1.09e-10** | *** |
| Hypertension | +0.5138 | 0.5155 | ±1.0311 | +0.997 | 0.3190 |  |
| High cholesterol | -0.3452 | 0.4659 | ±0.9317 | -0.741 | 0.4587 |  |
| Kidney disease | +0.8193 | 1.0338 | ±2.0676 | +0.793 | 0.4281 |  |
| Circulatory disease | +0.3881 | 0.6886 | ±1.3773 | +0.564 | 0.5730 |  |
| Avg. daily time 54-69 (%) | +0.0054 | 0.1491 | ±0.2983 | +0.036 | 0.9711 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1128**, R² = **0.1381**, Adj R² = **0.1296**, F-statistic = **16.25** (p = **6.19e-30**), Residual SE = **7.418** on **1116** df, AIC = **7733.9**, BIC = **7794.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5540** | 2.0172 | ±4.0344 | **+31.011** | **3.89e-211** | *** |
| Education: graduate level (vs college) | -0.8911 | 0.4757 | ±0.9514 | -1.873 | 0.0610 | . |
| Education: high school or below (vs college) | -0.1655 | 0.9300 | ±1.8600 | -0.178 | 0.8588 |  |
| **Site: UCSD (vs UAB)** | **-1.9491** | 0.6236 | ±1.2472 | **-3.126** | **0.0018** | ** |
| **Site: UW (vs UAB)** | **-2.3110** | 0.5523 | ±1.1045 | **-4.184** | **2.86e-05** | *** |
| **Age (years)** | **-0.1301** | 0.0216 | ±0.0432 | **-6.020** | **1.75e-09** | *** |
| **BMI (kg/m2)** | **+0.2546** | 0.0394 | ±0.0789 | **+6.457** | **1.07e-10** | *** |
| Hypertension | +0.5184 | 0.5153 | ±1.0307 | +1.006 | 0.3144 |  |
| High cholesterol | -0.3371 | 0.4662 | ±0.9323 | -0.723 | 0.4697 |  |
| Kidney disease | +0.8181 | 1.0343 | ±2.0685 | +0.791 | 0.4289 |  |
| Circulatory disease | +0.3880 | 0.6888 | ±1.3776 | +0.563 | 0.5732 |  |
| Time < 70 (%) | +0.0326 | 0.1075 | ±0.2149 | +0.304 | 0.7614 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1128**, R² = **0.1381**, Adj R² = **0.1296**, F-statistic = **16.25** (p = **6.32e-30**), Residual SE = **7.418** on **1116** df, AIC = **7733.9**, BIC = **7794.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5815** | 2.0127 | ±4.0254 | **+31.093** | **3.00e-212** | *** |
| Education: graduate level (vs college) | -0.8925 | 0.4762 | ±0.9525 | -1.874 | 0.0609 | . |
| Education: high school or below (vs college) | -0.1703 | 0.9308 | ±1.8617 | -0.183 | 0.8548 |  |
| **Site: UCSD (vs UAB)** | **-1.9576** | 0.6219 | ±1.2437 | **-3.148** | **0.0016** | ** |
| **Site: UW (vs UAB)** | **-2.3169** | 0.5519 | ±1.1037 | **-4.198** | **2.69e-05** | *** |
| **Age (years)** | **-0.1303** | 0.0216 | ±0.0432 | **-6.032** | **1.62e-09** | *** |
| **BMI (kg/m2)** | **+0.2546** | 0.0394 | ±0.0789 | **+6.455** | **1.08e-10** | *** |
| Hypertension | +0.5170 | 0.5157 | ±1.0314 | +1.003 | 0.3161 |  |
| High cholesterol | -0.3409 | 0.4662 | ±0.9323 | -0.731 | 0.4645 |  |
| Kidney disease | +0.8191 | 1.0340 | ±2.0679 | +0.792 | 0.4282 |  |
| Circulatory disease | +0.3886 | 0.6887 | ±1.3775 | +0.564 | 0.5726 |  |
| Avg. daily time < 70 (%) | +0.0219 | 0.1197 | ±0.2394 | +0.183 | 0.8551 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1128**, R² = **0.1421**, Adj R² = **0.1337**, F-statistic = **16.81** (p = **5.14e-31**), Residual SE = **7.401** on **1116** df, AIC = **7728.6**, BIC = **7788.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+73.8098** | 7.2491 | ±14.4981 | **+10.182** | **2.39e-24** | *** |
| Education: graduate level (vs college) | -0.8927 | 0.4748 | ±0.9496 | -1.880 | 0.0601 | . |
| Education: high school or below (vs college) | -0.2564 | 0.9158 | ±1.8316 | -0.280 | 0.7795 |  |
| **Site: UCSD (vs UAB)** | **-1.9515** | 0.6207 | ±1.2414 | **-3.144** | **0.0017** | ** |
| **Site: UW (vs UAB)** | **-2.3168** | 0.5457 | ±1.0914 | **-4.246** | **2.18e-05** | *** |
| **Age (years)** | **-0.1291** | 0.0216 | ±0.0431 | **-5.990** | **2.10e-09** | *** |
| **BMI (kg/m2)** | **+0.2544** | 0.0395 | ±0.0790 | **+6.439** | **1.20e-10** | *** |
| Hypertension | +0.5217 | 0.5153 | ±1.0305 | +1.013 | 0.3113 |  |
| High cholesterol | -0.3522 | 0.4650 | ±0.9301 | -0.757 | 0.4488 |  |
| Kidney disease | +0.7736 | 1.0361 | ±2.0722 | +0.747 | 0.4553 |  |
| Circulatory disease | +0.3246 | 0.6783 | ±1.3566 | +0.479 | 0.6322 |  |
| Time 54-250, pooled (%) | -0.1133 | 0.0704 | ±0.1407 | -1.610 | 0.1073 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1128**, R² = **0.1420**, Adj R² = **0.1335**, F-statistic = **16.79** (p = **5.60e-31**), Residual SE = **7.401** on **1116** df, AIC = **7728.8**, BIC = **7789.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+74.0715** | 7.7352 | ±15.4704 | **+9.576** | **1.01e-21** | *** |
| Education: graduate level (vs college) | -0.8927 | 0.4750 | ±0.9499 | -1.879 | 0.0602 | . |
| Education: high school or below (vs college) | -0.2565 | 0.9160 | ±1.8320 | -0.280 | 0.7795 |  |
| **Site: UCSD (vs UAB)** | **-1.9585** | 0.6206 | ±1.2411 | **-3.156** | **0.0016** | ** |
| **Site: UW (vs UAB)** | **-2.3220** | 0.5458 | ±1.0916 | **-4.254** | **2.10e-05** | *** |
| **Age (years)** | **-0.1293** | 0.0216 | ±0.0431 | **-5.997** | **2.00e-09** | *** |
| **BMI (kg/m2)** | **+0.2540** | 0.0395 | ±0.0790 | **+6.432** | **1.26e-10** | *** |
| Hypertension | +0.5227 | 0.5154 | ±1.0308 | +1.014 | 0.3105 |  |
| High cholesterol | -0.3551 | 0.4652 | ±0.9305 | -0.763 | 0.4453 |  |
| Kidney disease | +0.7776 | 1.0361 | ±2.0721 | +0.751 | 0.4529 |  |
| Circulatory disease | +0.3272 | 0.6783 | ±1.3566 | +0.482 | 0.6296 |  |
| Avg. daily time 54-250 (%) | -0.1156 | 0.0752 | ±0.1503 | -1.537 | 0.1242 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1128**, R² = **0.1447**, Adj R² = **0.1363**, F-statistic = **17.17** (p = **1.02e-31**), Residual SE = **7.389** on **1116** df, AIC = **7725.2**, BIC = **7785.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5750** | 1.9719 | ±3.9437 | **+31.734** | **5.29e-221** | *** |
| **Education: graduate level (vs college)** | **-0.9463** | 0.4720 | ±0.9439 | **-2.005** | **0.0450** | * |
| Education: high school or below (vs college) | -0.2019 | 0.9212 | ±1.8424 | -0.219 | 0.8265 |  |
| **Site: UCSD (vs UAB)** | **-1.9555** | 0.6168 | ±1.2336 | **-3.171** | **0.0015** | ** |
| **Site: UW (vs UAB)** | **-2.4100** | 0.5476 | ±1.0952 | **-4.401** | **1.08e-05** | *** |
| **Age (years)** | **-0.1314** | 0.0214 | ±0.0428 | **-6.140** | **8.26e-10** | *** |
| **BMI (kg/m2)** | **+0.2518** | 0.0393 | ±0.0787 | **+6.399** | **1.56e-10** | *** |
| Hypertension | +0.3836 | 0.5156 | ±1.0311 | +0.744 | 0.4568 |  |
| High cholesterol | -0.4623 | 0.4602 | ±0.9205 | -1.004 | 0.3152 |  |
| Kidney disease | +0.6086 | 1.0166 | ±2.0332 | +0.599 | 0.5494 |  |
| Circulatory disease | +0.3560 | 0.6779 | ±1.3558 | +0.525 | 0.5995 |  |
| **Time 181-250, pooled (%)** | **+0.1104** | 0.0449 | ±0.0899 | **+2.457** | **0.0140** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1128**, R² = **0.1446**, Adj R² = **0.1361**, F-statistic = **17.15** (p = **1.12e-31**), Residual SE = **7.390** on **1116** df, AIC = **7725.4**, BIC = **7785.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5860** | 1.9709 | ±3.9418 | **+31.755** | **2.70e-221** | *** |
| **Education: graduate level (vs college)** | **-0.9484** | 0.4722 | ±0.9443 | **-2.009** | **0.0446** | * |
| Education: high school or below (vs college) | -0.1927 | 0.9205 | ±1.8410 | -0.209 | 0.8342 |  |
| **Site: UCSD (vs UAB)** | **-1.9458** | 0.6168 | ±1.2337 | **-3.154** | **0.0016** | ** |
| **Site: UW (vs UAB)** | **-2.4009** | 0.5472 | ±1.0944 | **-4.388** | **1.15e-05** | *** |
| **Age (years)** | **-0.1312** | 0.0214 | ±0.0428 | **-6.134** | **8.56e-10** | *** |
| **BMI (kg/m2)** | **+0.2514** | 0.0393 | ±0.0786 | **+6.400** | **1.56e-10** | *** |
| Hypertension | +0.3851 | 0.5156 | ±1.0312 | +0.747 | 0.4552 |  |
| High cholesterol | -0.4626 | 0.4602 | ±0.9204 | -1.005 | 0.3148 |  |
| Kidney disease | +0.6105 | 1.0169 | ±2.0338 | +0.600 | 0.5483 |  |
| Circulatory disease | +0.3521 | 0.6781 | ±1.3562 | +0.519 | 0.6036 |  |
| **Avg. daily time 181-250 (%)** | **+0.1079** | 0.0449 | ±0.0898 | **+2.404** | **0.0162** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1128**, R² = **0.1460**, Adj R² = **0.1376**, F-statistic = **17.35** (p = **4.59e-32**), Residual SE = **7.384** on **1116** df, AIC = **7723.5**, BIC = **7783.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5237** | 1.9770 | ±3.9539 | **+31.626** | **1.62e-219** | *** |
| **Education: graduate level (vs college)** | **-0.9333** | 0.4721 | ±0.9442 | **-1.977** | **0.0480** | * |
| Education: high school or below (vs college) | -0.2609 | 0.9115 | ±1.8229 | -0.286 | 0.7747 |  |
| **Site: UCSD (vs UAB)** | **-1.9635** | 0.6177 | ±1.2354 | **-3.179** | **0.0015** | ** |
| **Site: UW (vs UAB)** | **-2.3948** | 0.5450 | ±1.0900 | **-4.394** | **1.11e-05** | *** |
| **Age (years)** | **-0.1303** | 0.0214 | ±0.0428 | **-6.093** | **1.11e-09** | *** |
| **BMI (kg/m2)** | **+0.2521** | 0.0394 | ±0.0788 | **+6.398** | **1.57e-10** | *** |
| Hypertension | +0.4176 | 0.5145 | ±1.0290 | +0.812 | 0.4170 |  |
| High cholesterol | -0.4463 | 0.4624 | ±0.9247 | -0.965 | 0.3344 |  |
| Kidney disease | +0.6292 | 1.0240 | ±2.0480 | +0.614 | 0.5389 |  |
| Circulatory disease | +0.3168 | 0.6718 | ±1.3436 | +0.472 | 0.6373 |  |
| **Time > 180 (%)** | **+0.0839** | 0.0351 | ±0.0701 | **+2.392** | **0.0168** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1128**, R² = **0.1458**, Adj R² = **0.1374**, F-statistic = **17.31** (p = **5.29e-32**), Residual SE = **7.385** on **1116** df, AIC = **7723.8**, BIC = **7784.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5430** | 1.9761 | ±3.9522 | **+31.650** | **7.63e-220** | *** |
| **Education: graduate level (vs college)** | **-0.9354** | 0.4722 | ±0.9444 | **-1.981** | **0.0476** | * |
| Education: high school or below (vs college) | -0.2498 | 0.9116 | ±1.8233 | -0.274 | 0.7840 |  |
| **Site: UCSD (vs UAB)** | **-1.9557** | 0.6178 | ±1.2357 | **-3.165** | **0.0015** | ** |
| **Site: UW (vs UAB)** | **-2.3899** | 0.5450 | ±1.0900 | **-4.385** | **1.16e-05** | *** |
| **Age (years)** | **-0.1303** | 0.0214 | ±0.0428 | **-6.090** | **1.13e-09** | *** |
| **BMI (kg/m2)** | **+0.2517** | 0.0394 | ±0.0787 | **+6.394** | **1.61e-10** | *** |
| Hypertension | +0.4184 | 0.5146 | ±1.0292 | +0.813 | 0.4161 |  |
| High cholesterol | -0.4467 | 0.4624 | ±0.9249 | -0.966 | 0.3340 |  |
| Kidney disease | +0.6325 | 1.0241 | ±2.0481 | +0.618 | 0.5368 |  |
| Circulatory disease | +0.3162 | 0.6722 | ±1.3444 | +0.470 | 0.6381 |  |
| **Avg. daily time > 180 (%)** | **+0.0824** | 0.0350 | ±0.0700 | **+2.357** | **0.0184** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1128**, R² = **0.1396**, Adj R² = **0.1312**, F-statistic = **16.47** (p = **2.39e-30**), Residual SE = **7.411** on **1116** df, AIC = **7731.9**, BIC = **7792.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6375** | 1.9971 | ±3.9942 | **+31.364** | **6.29e-216** | *** |
| Education: graduate level (vs college) | -0.8910 | 0.4741 | ±0.9482 | -1.880 | 0.0602 | . |
| Education: high school or below (vs college) | -0.2048 | 0.9219 | ±1.8438 | -0.222 | 0.8242 |  |
| **Site: UCSD (vs UAB)** | **-1.9658** | 0.6197 | ±1.2394 | **-3.172** | **0.0015** | ** |
| **Site: UW (vs UAB)** | **-2.3483** | 0.5478 | ±1.0957 | **-4.287** | **1.81e-05** | *** |
| **Age (years)** | **-0.1295** | 0.0215 | ±0.0430 | **-6.014** | **1.81e-09** | *** |
| **BMI (kg/m2)** | **+0.2505** | 0.0399 | ±0.0797 | **+6.285** | **3.28e-10** | *** |
| Hypertension | +0.4935 | 0.5160 | ±1.0321 | +0.956 | 0.3389 |  |
| High cholesterol | -0.4036 | 0.4664 | ±0.9327 | -0.865 | 0.3868 |  |
| Kidney disease | +0.8078 | 1.0340 | ±2.0680 | +0.781 | 0.4346 |  |
| Circulatory disease | +0.3812 | 0.6845 | ±1.3690 | +0.557 | 0.5776 |  |
| Nocturnal time > 180 (%) | +0.0398 | 0.0388 | ±0.0776 | +1.027 | 0.3045 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1128**, R² = **0.1398**, Adj R² = **0.1313**, F-statistic = **16.48** (p = **2.22e-30**), Residual SE = **7.411** on **1116** df, AIC = **7731.7**, BIC = **7792.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.3709** | 2.0047 | ±4.0094 | **+31.112** | **1.64e-212** | *** |
| Education: graduate level (vs college) | -0.8998 | 0.4741 | ±0.9481 | -1.898 | 0.0577 | . |
| Education: high school or below (vs college) | -0.1852 | 0.9220 | ±1.8440 | -0.201 | 0.8408 |  |
| **Site: UCSD (vs UAB)** | **-1.9697** | 0.6185 | ±1.2370 | **-3.185** | **0.0014** | ** |
| **Site: UW (vs UAB)** | **-2.3454** | 0.5488 | ±1.0976 | **-4.274** | **1.92e-05** | *** |
| **Age (years)** | **-0.1304** | 0.0216 | ±0.0432 | **-6.045** | **1.50e-09** | *** |
| **BMI (kg/m2)** | **+0.2590** | 0.0397 | ±0.0795 | **+6.517** | **7.19e-11** | *** |
| Hypertension | +0.4623 | 0.5161 | ±1.0321 | +0.896 | 0.3704 |  |
| High cholesterol | -0.3784 | 0.4643 | ±0.9287 | -0.815 | 0.4151 |  |
| Kidney disease | +0.7964 | 1.0314 | ±2.0628 | +0.772 | 0.4400 |  |
| Circulatory disease | +0.4013 | 0.6834 | ±1.3669 | +0.587 | 0.5571 |  |
| Any reading > 250 during wear (0/1) | +0.8428 | 0.5614 | ±1.1227 | +1.501 | 0.1333 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1128**, R² = **0.1418**, Adj R² = **0.1334**, F-statistic = **16.77** (p = **6.17e-31**), Residual SE = **7.402** on **1116** df, AIC = **7729.0**, BIC = **7789.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5325** | 1.9997 | ±3.9994 | **+31.271** | **1.15e-214** | *** |
| Education: graduate level (vs college) | -0.8953 | 0.4749 | ±0.9497 | -1.885 | 0.0594 | . |
| Education: high school or below (vs college) | -0.2645 | 0.9175 | ±1.8349 | -0.288 | 0.7731 |  |
| **Site: UCSD (vs UAB)** | **-1.9735** | 0.6199 | ±1.2399 | **-3.183** | **0.0015** | ** |
| **Site: UW (vs UAB)** | **-2.3333** | 0.5457 | ±1.0914 | **-4.276** | **1.90e-05** | *** |
| **Age (years)** | **-0.1292** | 0.0216 | ±0.0431 | **-5.997** | **2.01e-09** | *** |
| **BMI (kg/m2)** | **+0.2542** | 0.0395 | ±0.0790 | **+6.436** | **1.23e-10** | *** |
| Hypertension | +0.5167 | 0.5152 | ±1.0303 | +1.003 | 0.3158 |  |
| High cholesterol | -0.3618 | 0.4654 | ±0.9308 | -0.777 | 0.4369 |  |
| Kidney disease | +0.7798 | 1.0358 | ±2.0717 | +0.753 | 0.4515 |  |
| Circulatory disease | +0.3266 | 0.6786 | ±1.3573 | +0.481 | 0.6304 |  |
| Time > 250 (%) | +0.1099 | 0.0729 | ±0.1459 | +1.507 | 0.1317 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,128)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1128**, R² = **0.1418**, Adj R² = **0.1334**, F-statistic = **16.77** (p = **6.18e-31**), Residual SE = **7.402** on **1116** df, AIC = **7729.0**, BIC = **7789.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5437** | 1.9995 | ±3.9990 | **+31.280** | **8.82e-215** | *** |
| Education: graduate level (vs college) | -0.8955 | 0.4749 | ±0.9498 | -1.886 | 0.0593 | . |
| Education: high school or below (vs college) | -0.2632 | 0.9175 | ±1.8350 | -0.287 | 0.7742 |  |
| **Site: UCSD (vs UAB)** | **-1.9734** | 0.6200 | ±1.2400 | **-3.183** | **0.0015** | ** |
| **Site: UW (vs UAB)** | **-2.3359** | 0.5458 | ±1.0915 | **-4.280** | **1.87e-05** | *** |
| **Age (years)** | **-0.1293** | 0.0216 | ±0.0431 | **-5.997** | **2.01e-09** | *** |
| **BMI (kg/m2)** | **+0.2539** | 0.0395 | ±0.0790 | **+6.430** | **1.28e-10** | *** |
| Hypertension | +0.5175 | 0.5153 | ±1.0306 | +1.004 | 0.3153 |  |
| High cholesterol | -0.3621 | 0.4655 | ±0.9310 | -0.778 | 0.4366 |  |
| Kidney disease | +0.7816 | 1.0359 | ±2.0718 | +0.755 | 0.4505 |  |
| Circulatory disease | +0.3268 | 0.6785 | ±1.3570 | +0.482 | 0.6300 |  |
| Avg. daily time > 250 (%) | +0.1137 | 0.0767 | ±0.1534 | +1.483 | 0.1381 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 1,137; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0214**, F-statistic = **3.48** (p = **1.57e-04**), Residual SE = **65.505** on **1126** df, AIC = **12747.8**, BIC = **12803.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.1684** | 16.4040 | ±32.8079 | **+24.638** | **4.89e-134** | *** |
| Education: graduate level (vs college) | +0.6486 | 4.0966 | ±8.1931 | +0.158 | 0.8742 |  |
| Education: high school or below (vs college) | -15.7250 | 8.7895 | ±17.5789 | -1.789 | 0.0736 | . |
| Site: UCSD (vs UAB) | -6.2682 | 5.4287 | ±10.8574 | -1.155 | 0.2482 |  |
| Site: UW (vs UAB) | -1.3074 | 4.7771 | ±9.5542 | -0.274 | 0.7843 |  |
| Age (years) | -0.0578 | 0.1879 | ±0.3758 | -0.307 | 0.7585 |  |
| **BMI (kg/m2)** | **-0.9238** | 0.3274 | ±0.6549 | **-2.821** | **0.0048** | ** |
| Hypertension | -7.6117 | 4.4007 | ±8.8014 | -1.730 | 0.0837 | . |
| High cholesterol | -2.5058 | 4.0275 | ±8.0550 | -0.622 | 0.5338 |  |
| Kidney disease | -18.6810 | 10.5899 | ±21.1797 | -1.764 | 0.0777 | . |
| Circulatory disease | +13.1569 | 6.9529 | ±13.9058 | +1.892 | 0.0585 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1137**, R² = **0.0334**, Adj R² = **0.0240**, F-statistic = **3.54** (p = **6.74e-05**), Residual SE = **65.418** on **1125** df, AIC = **12745.7**, BIC = **12806.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+443.0237** | 25.0012 | ±50.0024 | **+17.720** | **2.93e-70** | *** |
| Education: graduate level (vs college) | +0.5503 | 4.0897 | ±8.1795 | +0.135 | 0.8930 |  |
| Education: high school or below (vs college) | -14.8085 | 8.8127 | ±17.6254 | -1.680 | 0.0929 | . |
| Site: UCSD (vs UAB) | -6.1220 | 5.4198 | ±10.8395 | -1.130 | 0.2587 |  |
| Site: UW (vs UAB) | -0.9734 | 4.7742 | ±9.5483 | -0.204 | 0.8384 |  |
| Age (years) | -0.0229 | 0.1893 | ±0.3786 | -0.121 | 0.9039 |  |
| **BMI (kg/m2)** | **-0.8745** | 0.3274 | ±0.6547 | **-2.671** | **0.0076** | ** |
| Hypertension | -7.3771 | 4.3900 | ±8.7800 | -1.680 | 0.0929 | . |
| High cholesterol | -1.3317 | 4.0806 | ±8.1613 | -0.326 | 0.7442 |  |
| Kidney disease | -18.4698 | 10.5454 | ±21.0907 | -1.751 | 0.0799 | . |
| Circulatory disease | +13.6068 | 6.9872 | ±13.9743 | +1.947 | 0.0515 | . |
| **HbA1c (%)** | **-7.6546** | 3.6342 | ±7.2684 | **-2.106** | **0.0352** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1137**, R² = **0.0301**, Adj R² = **0.0206**, F-statistic = **3.17** (p = **2.99e-04**), Residual SE = **65.531** on **1125** df, AIC = **12749.7**, BIC = **12810.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.8771** | 19.7053 | ±39.4106 | **+20.699** | **3.55e-95** | *** |
| Education: graduate level (vs college) | +0.7053 | 4.1194 | ±8.2388 | +0.171 | 0.8641 |  |
| Education: high school or below (vs college) | -15.5941 | 8.8359 | ±17.6718 | -1.765 | 0.0776 | . |
| Site: UCSD (vs UAB) | -6.2687 | 5.4332 | ±10.8664 | -1.154 | 0.2486 |  |
| Site: UW (vs UAB) | -1.1882 | 4.8206 | ±9.6412 | -0.246 | 0.8053 |  |
| Age (years) | -0.0556 | 0.1883 | ±0.3767 | -0.295 | 0.7678 |  |
| **BMI (kg/m2)** | **-0.9196** | 0.3283 | ±0.6565 | **-2.801** | **0.0051** | ** |
| Hypertension | -7.5167 | 4.3970 | ±8.7941 | -1.709 | 0.0874 | . |
| High cholesterol | -2.3831 | 4.0483 | ±8.0966 | -0.589 | 0.5561 |  |
| Kidney disease | -18.5231 | 10.6118 | ±21.2237 | -1.746 | 0.0809 | . |
| Circulatory disease | +13.2069 | 6.9750 | ±13.9499 | +1.893 | 0.0583 | . |
| Mean glucose (mg/dL) | -0.0344 | 0.1071 | ±0.2143 | -0.321 | 0.7483 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1137**, R² = **0.0301**, Adj R² = **0.0206**, F-statistic = **3.17** (p = **2.99e-04**), Residual SE = **65.531** on **1125** df, AIC = **12749.7**, BIC = **12810.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+412.6348** | 30.5247 | ±61.0494 | **+13.518** | **1.22e-41** | *** |
| Education: graduate level (vs college) | +0.7053 | 4.1194 | ±8.2388 | +0.171 | 0.8641 |  |
| Education: high school or below (vs college) | -15.5941 | 8.8359 | ±17.6718 | -1.765 | 0.0776 | . |
| Site: UCSD (vs UAB) | -6.2687 | 5.4332 | ±10.8664 | -1.154 | 0.2486 |  |
| Site: UW (vs UAB) | -1.1882 | 4.8206 | ±9.6412 | -0.246 | 0.8053 |  |
| Age (years) | -0.0556 | 0.1883 | ±0.3767 | -0.295 | 0.7678 |  |
| **BMI (kg/m2)** | **-0.9196** | 0.3283 | ±0.6565 | **-2.801** | **0.0051** | ** |
| Hypertension | -7.5167 | 4.3970 | ±8.7941 | -1.709 | 0.0874 | . |
| High cholesterol | -2.3831 | 4.0483 | ±8.0966 | -0.589 | 0.5561 |  |
| Kidney disease | -18.5231 | 10.6118 | ±21.2237 | -1.746 | 0.0809 | . |
| Circulatory disease | +13.2069 | 6.9750 | ±13.9499 | +1.893 | 0.0583 | . |
| GMI (%) | -1.4374 | 4.4789 | ±8.9578 | -0.321 | 0.7483 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1137**, R² = **0.0308**, Adj R² = **0.0213**, F-statistic = **3.25** (p = **2.16e-04**), Residual SE = **65.506** on **1125** df, AIC = **12748.8**, BIC = **12809.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+415.0928** | 19.4244 | ±38.8488 | **+21.370** | **2.56e-101** | *** |
| Education: graduate level (vs college) | +0.7410 | 4.1007 | ±8.2014 | +0.181 | 0.8566 |  |
| Education: high school or below (vs college) | -15.3077 | 8.8402 | ±17.6805 | -1.732 | 0.0833 | . |
| Site: UCSD (vs UAB) | -6.1568 | 5.4301 | ±10.8601 | -1.134 | 0.2569 |  |
| Site: UW (vs UAB) | -0.9679 | 4.8119 | ±9.6239 | -0.201 | 0.8406 |  |
| Age (years) | -0.0610 | 0.1882 | ±0.3763 | -0.324 | 0.7459 |  |
| **BMI (kg/m2)** | **-0.8849** | 0.3287 | ±0.6575 | **-2.692** | **0.0071** | ** |
| Hypertension | -7.3879 | 4.4058 | ±8.8116 | -1.677 | 0.0936 | . |
| High cholesterol | -2.0390 | 4.0551 | ±8.1102 | -0.503 | 0.6151 |  |
| Kidney disease | -18.5058 | 10.5784 | ±21.1569 | -1.749 | 0.0802 | . |
| Circulatory disease | +13.2147 | 6.9716 | ±13.9431 | +1.896 | 0.0580 | . |
| Nocturnal mean 00-06h (mg/dL) | -0.1038 | 0.0998 | ±0.1995 | -1.040 | 0.2982 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1137**, R² = **0.0303**, Adj R² = **0.0208**, F-statistic = **3.20** (p = **2.72e-04**), Residual SE = **65.523** on **1125** df, AIC = **12749.4**, BIC = **12809.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.7394** | 17.1091 | ±34.2183 | **+23.832** | **1.57e-125** | *** |
| Education: graduate level (vs college) | +0.6672 | 4.1035 | ±8.2071 | +0.163 | 0.8708 |  |
| Education: high school or below (vs college) | -15.6686 | 8.8044 | ±17.6087 | -1.780 | 0.0751 | . |
| Site: UCSD (vs UAB) | -6.4091 | 5.4539 | ±10.9079 | -1.175 | 0.2399 |  |
| Site: UW (vs UAB) | -1.1991 | 4.7881 | ±9.5762 | -0.250 | 0.8023 |  |
| Age (years) | -0.0517 | 0.1890 | ±0.3780 | -0.273 | 0.7845 |  |
| **BMI (kg/m2)** | **-0.9279** | 0.3274 | ±0.6547 | **-2.834** | **0.0046** | ** |
| Hypertension | -7.4126 | 4.3898 | ±8.7797 | -1.689 | 0.0913 | . |
| High cholesterol | -2.4088 | 4.0334 | ±8.0667 | -0.597 | 0.5504 |  |
| Kidney disease | -18.1948 | 10.6208 | ±21.2416 | -1.713 | 0.0867 | . |
| Circulatory disease | +13.2524 | 6.9651 | ±13.9302 | +1.903 | 0.0571 | . |
| Glucose SD, pooled (mg/dL) | -0.1852 | 0.3136 | ±0.6272 | -0.591 | 0.5548 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1137**, R² = **0.0304**, Adj R² = **0.0209**, F-statistic = **3.20** (p = **2.65e-04**), Residual SE = **65.522** on **1125** df, AIC = **12749.3**, BIC = **12809.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.6832** | 16.8667 | ±33.7334 | **+24.171** | **4.51e-129** | *** |
| Education: graduate level (vs college) | +0.6888 | 4.1082 | ±8.2164 | +0.168 | 0.8668 |  |
| Education: high school or below (vs college) | -15.6328 | 8.8105 | ±17.6210 | -1.774 | 0.0760 | . |
| Site: UCSD (vs UAB) | -6.3939 | 5.4550 | ±10.9099 | -1.172 | 0.2411 |  |
| Site: UW (vs UAB) | -1.1631 | 4.7910 | ±9.5821 | -0.243 | 0.8082 |  |
| Age (years) | -0.0495 | 0.1894 | ±0.3787 | -0.262 | 0.7937 |  |
| **BMI (kg/m2)** | **-0.9253** | 0.3274 | ±0.6548 | **-2.826** | **0.0047** | ** |
| Hypertension | -7.4023 | 4.3888 | ±8.7775 | -1.687 | 0.0917 | . |
| High cholesterol | -2.3953 | 4.0345 | ±8.0691 | -0.594 | 0.5527 |  |
| Kidney disease | -18.1511 | 10.6407 | ±21.2813 | -1.706 | 0.0880 | . |
| Circulatory disease | +13.2640 | 6.9684 | ±13.9368 | +1.903 | 0.0570 | . |
| Avg. daily SD (mg/dL) | -0.2134 | 0.3333 | ±0.6666 | -0.640 | 0.5219 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1137**, R² = **0.0303**, Adj R² = **0.0208**, F-statistic = **3.19** (p = **2.76e-04**), Residual SE = **65.525** on **1125** df, AIC = **12749.4**, BIC = **12809.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+409.0816** | 18.0731 | ±36.1462 | **+22.635** | **1.97e-113** | *** |
| Education: graduate level (vs college) | +0.5943 | 4.0947 | ±8.1893 | +0.145 | 0.8846 |  |
| Education: high school or below (vs college) | -15.8043 | 8.7820 | ±17.5641 | -1.800 | 0.0719 | . |
| Site: UCSD (vs UAB) | -6.4563 | 5.4666 | ±10.9332 | -1.181 | 0.2376 |  |
| Site: UW (vs UAB) | -1.3320 | 4.7827 | ±9.5655 | -0.279 | 0.7806 |  |
| Age (years) | -0.0523 | 0.1889 | ±0.3778 | -0.277 | 0.7820 |  |
| **BMI (kg/m2)** | **-0.9335** | 0.3274 | ±0.6548 | **-2.851** | **0.0044** | ** |
| Hypertension | -7.4963 | 4.3934 | ±8.7868 | -1.706 | 0.0880 | . |
| High cholesterol | -2.5489 | 4.0334 | ±8.0669 | -0.632 | 0.5274 |  |
| Kidney disease | -18.3140 | 10.6110 | ±21.2220 | -1.726 | 0.0844 | . |
| Circulatory disease | +13.1972 | 6.9585 | ±13.9170 | +1.897 | 0.0579 | . |
| CV (%) | -0.2765 | 0.4802 | ±0.9604 | -0.576 | 0.5647 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1137**, R² = **0.0301**, Adj R² = **0.0206**, F-statistic = **3.17** (p = **2.97e-04**), Residual SE = **65.530** on **1125** df, AIC = **12749.6**, BIC = **12810.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.8681** | 19.3354 | ±38.6708 | **+20.732** | **1.77e-95** | *** |
| Education: graduate level (vs college) | +0.6118 | 4.0942 | ±8.1884 | +0.149 | 0.8812 |  |
| Education: high school or below (vs college) | -15.7300 | 8.7903 | ±17.5805 | -1.789 | 0.0735 | . |
| Site: UCSD (vs UAB) | -6.3813 | 5.4577 | ±10.9155 | -1.169 | 0.2423 |  |
| Site: UW (vs UAB) | -1.2972 | 4.7804 | ±9.5607 | -0.271 | 0.7861 |  |
| Age (years) | -0.0543 | 0.1890 | ±0.3780 | -0.287 | 0.7739 |  |
| **BMI (kg/m2)** | **-0.9289** | 0.3277 | ±0.6555 | **-2.834** | **0.0046** | ** |
| Hypertension | -7.5349 | 4.3977 | ±8.7953 | -1.713 | 0.0866 | . |
| High cholesterol | -2.5132 | 4.0312 | ±8.0625 | -0.623 | 0.5330 |  |
| Kidney disease | -18.5181 | 10.5943 | ±21.1887 | -1.748 | 0.0805 | . |
| Circulatory disease | +13.1762 | 6.9550 | ±13.9101 | +1.894 | 0.0582 | . |
| Mean / SD ratio | +0.5526 | 1.5517 | ±3.1034 | +0.356 | 0.7217 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1137**, R² = **0.0305**, Adj R² = **0.0211**, F-statistic = **3.22** (p = **2.46e-04**), Residual SE = **65.516** on **1125** df, AIC = **12749.1**, BIC = **12809.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.4354** | 19.6561 | ±39.3122 | **+20.169** | **1.85e-90** | *** |
| Education: graduate level (vs college) | +0.6295 | 4.0995 | ±8.1990 | +0.154 | 0.8780 |  |
| Education: high school or below (vs college) | -15.6313 | 8.7936 | ±17.5871 | -1.778 | 0.0755 | . |
| Site: UCSD (vs UAB) | -6.4709 | 5.4642 | ±10.9284 | -1.184 | 0.2363 |  |
| Site: UW (vs UAB) | -1.2417 | 4.7802 | ±9.5604 | -0.260 | 0.7950 |  |
| Age (years) | -0.0465 | 0.1896 | ±0.3792 | -0.245 | 0.8062 |  |
| **BMI (kg/m2)** | **-0.9288** | 0.3273 | ±0.6546 | **-2.838** | **0.0045** | ** |
| Hypertension | -7.4994 | 4.3970 | ±8.7939 | -1.706 | 0.0881 | . |
| High cholesterol | -2.5068 | 4.0319 | ±8.0638 | -0.622 | 0.5341 |  |
| Kidney disease | -18.2165 | 10.6274 | ±21.2549 | -1.714 | 0.0865 | . |
| Circulatory disease | +13.2047 | 6.9615 | ±13.9230 | +1.897 | 0.0579 | . |
| Avg. daily mean/SD | +1.0618 | 1.3161 | ±2.6322 | +0.807 | 0.4198 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1137**, R² = **0.0455**, Adj R² = **0.0361**, F-statistic = **4.87** (p = **2.16e-07**), Residual SE = **65.009** on **1125** df, AIC = **12731.5**, BIC = **12791.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+448.3426** | 18.5820 | ±37.1640 | **+24.128** | **1.28e-128** | *** |
| Education: graduate level (vs college) | +0.4202 | 4.0747 | ±8.1494 | +0.103 | 0.9179 |  |
| Education: high school or below (vs college) | -14.7301 | 8.6353 | ±17.2707 | -1.706 | 0.0880 | . |
| Site: UCSD (vs UAB) | -7.3409 | 5.4441 | ±10.8883 | -1.348 | 0.1775 |  |
| Site: UW (vs UAB) | -2.5141 | 4.7531 | ±9.5063 | -0.529 | 0.5968 |  |
| Age (years) | -0.0854 | 0.1864 | ±0.3728 | -0.458 | 0.6470 |  |
| **BMI (kg/m2)** | **-0.9437** | 0.3197 | ±0.6394 | **-2.952** | **0.0032** | ** |
| Hypertension | -7.8758 | 4.3711 | ±8.7421 | -1.802 | 0.0716 | . |
| High cholesterol | -2.9081 | 3.9994 | ±7.9988 | -0.727 | 0.4672 |  |
| Kidney disease | -17.1316 | 10.5369 | ±21.0738 | -1.626 | 0.1040 |  |
| Circulatory disease | +12.5144 | 6.9195 | ±13.8391 | +1.809 | 0.0705 | . |
| **MAG (mg/dL/h)** | **-1.0731** | 0.2601 | ±0.5203 | **-4.125** | **3.70e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1137**, R² = **0.0305**, Adj R² = **0.0210**, F-statistic = **3.22** (p = **2.49e-04**), Residual SE = **65.517** on **1125** df, AIC = **12749.2**, BIC = **12809.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+409.7936** | 17.6025 | ±35.2050 | **+23.280** | **7.00e-120** | *** |
| Education: graduate level (vs college) | +0.7155 | 4.1094 | ±8.2188 | +0.174 | 0.8618 |  |
| Education: high school or below (vs college) | -15.5720 | 8.8091 | ±17.6183 | -1.768 | 0.0771 | . |
| Site: UCSD (vs UAB) | -6.4129 | 5.4570 | ±10.9141 | -1.175 | 0.2399 |  |
| Site: UW (vs UAB) | -1.2077 | 4.7846 | ±9.5693 | -0.252 | 0.8007 |  |
| Age (years) | -0.0501 | 0.1889 | ±0.3778 | -0.265 | 0.7909 |  |
| **BMI (kg/m2)** | **-0.9400** | 0.3280 | ±0.6560 | **-2.866** | **0.0042** | ** |
| Hypertension | -7.4439 | 4.3938 | ±8.7876 | -1.694 | 0.0902 | . |
| High cholesterol | -2.4609 | 4.0345 | ±8.0690 | -0.610 | 0.5419 |  |
| Kidney disease | -18.1862 | 10.6349 | ±21.2699 | -1.710 | 0.0873 | . |
| Circulatory disease | +13.2387 | 6.9676 | ±13.9351 | +1.900 | 0.0574 | . |
| Avg. daily range (mg/dL) | -0.0587 | 0.0766 | ±0.1533 | -0.766 | 0.4439 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1137**, R² = **0.0303**, Adj R² = **0.0208**, F-statistic = **3.19** (p = **2.77e-04**), Residual SE = **65.525** on **1125** df, AIC = **12749.5**, BIC = **12809.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.2835** | 16.8166 | ±33.6332 | **+24.160** | **5.91e-129** | *** |
| Education: graduate level (vs college) | +0.6604 | 4.0981 | ±8.1962 | +0.161 | 0.8720 |  |
| Education: high school or below (vs college) | -15.8003 | 8.7898 | ±17.5796 | -1.798 | 0.0722 | . |
| Site: UCSD (vs UAB) | -6.4269 | 5.4234 | ±10.8469 | -1.185 | 0.2360 |  |
| Site: UW (vs UAB) | -1.2902 | 4.7805 | ±9.5610 | -0.270 | 0.7872 |  |
| Age (years) | -0.0597 | 0.1881 | ±0.3762 | -0.317 | 0.7511 |  |
| **BMI (kg/m2)** | **-0.9162** | 0.3271 | ±0.6542 | **-2.801** | **0.0051** | ** |
| Hypertension | -7.5825 | 4.4025 | ±8.8050 | -1.722 | 0.0850 | . |
| High cholesterol | -2.3708 | 4.0236 | ±8.0472 | -0.589 | 0.5557 |  |
| Kidney disease | -18.5838 | 10.5966 | ±21.1932 | -1.754 | 0.0795 | . |
| Circulatory disease | +13.2332 | 6.9536 | ±13.9073 | +1.903 | 0.0570 | . |
| SD of daily means (mg/dL) | -0.3435 | 0.5681 | ±1.1361 | -0.605 | 0.5454 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1137**, R² = **0.0303**, Adj R² = **0.0208**, F-statistic = **3.20** (p = **2.73e-04**), Residual SE = **65.524** on **1125** df, AIC = **12749.4**, BIC = **12809.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+418.1650** | 30.7562 | ±61.5125 | **+13.596** | **4.22e-42** | *** |
| Education: graduate level (vs college) | +0.6392 | 4.1012 | ±8.2023 | +0.156 | 0.8762 |  |
| Education: high school or below (vs college) | -15.8219 | 8.8230 | ±17.6459 | -1.793 | 0.0729 | . |
| Site: UCSD (vs UAB) | -6.1195 | 5.4499 | ±10.8997 | -1.123 | 0.2615 |  |
| Site: UW (vs UAB) | -1.3509 | 4.7824 | ±9.5648 | -0.282 | 0.7776 |  |
| Age (years) | -0.0581 | 0.1880 | ±0.3759 | -0.309 | 0.7574 |  |
| **BMI (kg/m2)** | **-0.9267** | 0.3285 | ±0.6570 | **-2.821** | **0.0048** | ** |
| Hypertension | -7.7013 | 4.3957 | ±8.7914 | -1.752 | 0.0798 | . |
| High cholesterol | -2.6758 | 4.0236 | ±8.0472 | -0.665 | 0.5060 |  |
| Kidney disease | -19.0530 | 10.6110 | ±21.2220 | -1.796 | 0.0726 | . |
| Circulatory disease | +13.0281 | 6.9716 | ±13.9432 | +1.869 | 0.0617 | . |
| Time in range 70-180, pooled (%) | -0.1438 | 0.2544 | ±0.5088 | -0.565 | 0.5718 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1137**, R² = **0.0303**, Adj R² = **0.0209**, F-statistic = **3.20** (p = **2.68e-04**), Residual SE = **65.523** on **1125** df, AIC = **12749.4**, BIC = **12809.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+419.0122** | 30.8392 | ±61.6784 | **+13.587** | **4.78e-42** | *** |
| Education: graduate level (vs college) | +0.6367 | 4.1014 | ±8.2028 | +0.155 | 0.8766 |  |
| Education: high school or below (vs college) | -15.8104 | 8.8215 | ±17.6429 | -1.792 | 0.0731 | . |
| Site: UCSD (vs UAB) | -6.1183 | 5.4473 | ±10.8945 | -1.123 | 0.2614 |  |
| Site: UW (vs UAB) | -1.3501 | 4.7821 | ±9.5642 | -0.282 | 0.7777 |  |
| Age (years) | -0.0584 | 0.1880 | ±0.3760 | -0.311 | 0.7559 |  |
| **BMI (kg/m2)** | **-0.9278** | 0.3287 | ±0.6574 | **-2.823** | **0.0048** | ** |
| Hypertension | -7.7034 | 4.3958 | ±8.7916 | -1.752 | 0.0797 | . |
| High cholesterol | -2.6953 | 4.0223 | ±8.0447 | -0.670 | 0.5028 |  |
| Kidney disease | -19.0703 | 10.6133 | ±21.2266 | -1.797 | 0.0724 | . |
| Circulatory disease | +13.0201 | 6.9713 | ±13.9425 | +1.868 | 0.0618 | . |
| Avg. daily time in range 70-180 (%) | -0.1516 | 0.2538 | ±0.5075 | -0.598 | 0.5501 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0205**, F-statistic = **3.17** (p = **3.06e-04**), Residual SE = **65.533** on **1125** df, AIC = **12749.7**, BIC = **12810.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.7145** | 16.7357 | ±33.4714 | **+24.123** | **1.44e-128** | *** |
| Education: graduate level (vs college) | +0.6756 | 4.1145 | ±8.2290 | +0.164 | 0.8696 |  |
| Education: high school or below (vs college) | -15.6309 | 8.8444 | ±17.6888 | -1.767 | 0.0772 | . |
| Site: UCSD (vs UAB) | -6.1498 | 5.4750 | ±10.9500 | -1.123 | 0.2613 |  |
| Site: UW (vs UAB) | -1.2505 | 4.7954 | ±9.5908 | -0.261 | 0.7943 |  |
| Age (years) | -0.0554 | 0.1882 | ±0.3763 | -0.294 | 0.7685 |  |
| **BMI (kg/m2)** | **-0.9255** | 0.3271 | ±0.6543 | **-2.829** | **0.0047** | ** |
| Hypertension | -7.6181 | 4.4039 | ±8.8079 | -1.730 | 0.0837 | . |
| High cholesterol | -2.4580 | 4.0611 | ±8.1223 | -0.605 | 0.5450 |  |
| Kidney disease | -18.6762 | 10.5909 | ±21.1817 | -1.763 | 0.0778 | . |
| Circulatory disease | +13.0605 | 6.9512 | ±13.9025 | +1.879 | 0.0603 | . |
| Any reading < 54 during wear (0/1) | +0.8253 | 4.1765 | ±8.3530 | +0.198 | 0.8433 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1137**, R² = **0.0305**, Adj R² = **0.0211**, F-statistic = **3.22** (p = **2.44e-04**), Residual SE = **65.515** on **1125** df, AIC = **12749.1**, BIC = **12809.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+405.3574** | 16.4550 | ±32.9100 | **+24.634** | **5.42e-134** | *** |
| Education: graduate level (vs college) | +0.5846 | 4.1000 | ±8.2001 | +0.143 | 0.8866 |  |
| Education: high school or below (vs college) | -15.9904 | 8.7851 | ±17.5701 | -1.820 | 0.0687 | . |
| Site: UCSD (vs UAB) | -6.7783 | 5.4708 | ±10.9416 | -1.239 | 0.2153 |  |
| Site: UW (vs UAB) | -1.7054 | 4.8139 | ±9.6278 | -0.354 | 0.7231 |  |
| Age (years) | -0.0609 | 0.1877 | ±0.3755 | -0.324 | 0.7456 |  |
| **BMI (kg/m2)** | **-0.9276** | 0.3274 | ±0.6548 | **-2.833** | **0.0046** | ** |
| Hypertension | -7.7306 | 4.4038 | ±8.8075 | -1.755 | 0.0792 | . |
| High cholesterol | -2.7301 | 4.0508 | ±8.1016 | -0.674 | 0.5003 |  |
| Kidney disease | -18.5706 | 10.6023 | ±21.2047 | -1.752 | 0.0799 | . |
| Circulatory disease | +13.1806 | 6.9492 | ±13.8984 | +1.897 | 0.0579 | . |
| Time < 54 (%) | -2.6405 | 1.9578 | ±3.9155 | -1.349 | 0.1774 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1137**, R² = **0.0307**, Adj R² = **0.0212**, F-statistic = **3.24** (p = **2.27e-04**), Residual SE = **65.510** on **1125** df, AIC = **12748.9**, BIC = **12809.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+405.1553** | 16.4304 | ±32.8608 | **+24.659** | **2.96e-134** | *** |
| Education: graduate level (vs college) | +0.5434 | 4.1035 | ±8.2070 | +0.132 | 0.8946 |  |
| Education: high school or below (vs college) | -16.0241 | 8.7855 | ±17.5710 | -1.824 | 0.0682 | . |
| Site: UCSD (vs UAB) | -6.7727 | 5.4556 | ±10.9113 | -1.241 | 0.2145 |  |
| Site: UW (vs UAB) | -1.8045 | 4.8106 | ±9.6213 | -0.375 | 0.7076 |  |
| Age (years) | -0.0569 | 0.1879 | ±0.3758 | -0.303 | 0.7621 |  |
| **BMI (kg/m2)** | **-0.9270** | 0.3271 | ±0.6541 | **-2.834** | **0.0046** | ** |
| Hypertension | -7.7979 | 4.4090 | ±8.8179 | -1.769 | 0.0770 | . |
| High cholesterol | -2.7429 | 4.0482 | ±8.0963 | -0.678 | 0.4981 |  |
| Kidney disease | -18.5685 | 10.6041 | ±21.2083 | -1.751 | 0.0799 | . |
| Circulatory disease | +13.1461 | 6.9521 | ±13.9042 | +1.891 | 0.0586 | . |
| Avg. daily time < 54 (%) | -4.0111 | 2.5181 | ±5.0361 | -1.593 | 0.1112 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1137**, R² = **0.0301**, Adj R² = **0.0207**, F-statistic = **3.18** (p = **2.92e-04**), Residual SE = **65.529** on **1125** df, AIC = **12749.6**, BIC = **12810.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.4709** | 16.4968 | ±32.9937 | **+24.457** | **4.19e-132** | *** |
| Education: graduate level (vs college) | +0.7238 | 4.1095 | ±8.2190 | +0.176 | 0.8602 |  |
| Education: high school or below (vs college) | -15.5279 | 8.8123 | ±17.6246 | -1.762 | 0.0781 | . |
| Site: UCSD (vs UAB) | -6.0973 | 5.4484 | ±10.8968 | -1.119 | 0.2631 |  |
| Site: UW (vs UAB) | -1.1234 | 4.8113 | ±9.6226 | -0.233 | 0.8154 |  |
| Age (years) | -0.0548 | 0.1880 | ±0.3760 | -0.292 | 0.7705 |  |
| **BMI (kg/m2)** | **-0.9260** | 0.3280 | ±0.6560 | **-2.823** | **0.0048** | ** |
| Hypertension | -7.5322 | 4.4142 | ±8.8284 | -1.706 | 0.0879 | . |
| High cholesterol | -2.4087 | 4.0440 | ±8.0879 | -0.596 | 0.5514 |  |
| Kidney disease | -18.6769 | 10.5822 | ±21.1643 | -1.765 | 0.0776 | . |
| Circulatory disease | +13.1348 | 6.9574 | ±13.9147 | +1.888 | 0.0590 | . |
| Time 54-69, pooled (%) | +0.5538 | 1.0905 | ±2.1811 | +0.508 | 0.6116 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1137**, R² = **0.0301**, Adj R² = **0.0206**, F-statistic = **3.18** (p = **2.93e-04**), Residual SE = **65.529** on **1125** df, AIC = **12749.6**, BIC = **12810.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.6011** | 16.4568 | ±32.9136 | **+24.525** | **8.01e-133** | *** |
| Education: graduate level (vs college) | +0.7296 | 4.1127 | ±8.2255 | +0.177 | 0.8592 |  |
| Education: high school or below (vs college) | -15.5226 | 8.8111 | ±17.6222 | -1.762 | 0.0781 | . |
| Site: UCSD (vs UAB) | -6.1385 | 5.4424 | ±10.8849 | -1.128 | 0.2594 |  |
| Site: UW (vs UAB) | -1.1323 | 4.8055 | ±9.6110 | -0.236 | 0.8137 |  |
| Age (years) | -0.0560 | 0.1879 | ±0.3759 | -0.298 | 0.7658 |  |
| **BMI (kg/m2)** | **-0.9257** | 0.3282 | ±0.6563 | **-2.821** | **0.0048** | ** |
| Hypertension | -7.5269 | 4.4192 | ±8.8384 | -1.703 | 0.0885 | . |
| High cholesterol | -2.4209 | 4.0418 | ±8.0837 | -0.599 | 0.5492 |  |
| Kidney disease | -18.6699 | 10.5821 | ±21.1643 | -1.764 | 0.0777 | . |
| Circulatory disease | +13.1421 | 6.9589 | ±13.9178 | +1.889 | 0.0590 | . |
| Avg. daily time 54-69 (%) | +0.5286 | 1.0890 | ±2.1780 | +0.485 | 0.6274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0205**, F-statistic = **3.16** (p = **3.10e-04**), Residual SE = **65.534** on **1125** df, AIC = **12749.8**, BIC = **12810.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.0522** | 16.5080 | ±33.0160 | **+24.476** | **2.65e-132** | *** |
| Education: graduate level (vs college) | +0.6595 | 4.1089 | ±8.2178 | +0.161 | 0.8725 |  |
| Education: high school or below (vs college) | -15.6940 | 8.8067 | ±17.6134 | -1.782 | 0.0747 | . |
| Site: UCSD (vs UAB) | -6.2341 | 5.4597 | ±10.9194 | -1.142 | 0.2535 |  |
| Site: UW (vs UAB) | -1.2746 | 4.8205 | ±9.6410 | -0.264 | 0.7915 |  |
| Age (years) | -0.0573 | 0.1880 | ±0.3759 | -0.305 | 0.7604 |  |
| **BMI (kg/m2)** | **-0.9240** | 0.3277 | ±0.6554 | **-2.820** | **0.0048** | ** |
| Hypertension | -7.5989 | 4.4128 | ±8.8255 | -1.722 | 0.0851 | . |
| High cholesterol | -2.4881 | 4.0513 | ±8.1026 | -0.614 | 0.5391 |  |
| Kidney disease | -18.6833 | 10.5925 | ±21.1851 | -1.764 | 0.0778 | . |
| Circulatory disease | +13.1536 | 6.9550 | ±13.9099 | +1.891 | 0.0586 | . |
| Time < 70 (%) | +0.0680 | 0.8445 | ±1.6890 | +0.080 | 0.9359 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0205**, F-statistic = **3.16** (p = **3.10e-04**), Residual SE = **65.534** on **1125** df, AIC = **12749.7**, BIC = **12810.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.0293** | 16.4621 | ±32.9242 | **+24.543** | **5.14e-133** | *** |
| Education: graduate level (vs college) | +0.6675 | 4.1132 | ±8.2263 | +0.162 | 0.8711 |  |
| Education: high school or below (vs college) | -15.6768 | 8.8077 | ±17.6154 | -1.780 | 0.0751 | . |
| Site: UCSD (vs UAB) | -6.2291 | 5.4477 | ±10.8954 | -1.143 | 0.2529 |  |
| Site: UW (vs UAB) | -1.2594 | 4.8122 | ±9.6244 | -0.262 | 0.7935 |  |
| Age (years) | -0.0574 | 0.1879 | ±0.3759 | -0.306 | 0.7599 |  |
| **BMI (kg/m2)** | **-0.9241** | 0.3278 | ±0.6556 | **-2.819** | **0.0048** | ** |
| Hypertension | -7.5899 | 4.4192 | ±8.8384 | -1.717 | 0.0859 | . |
| High cholesterol | -2.4826 | 4.0471 | ±8.0941 | -0.613 | 0.5396 |  |
| Kidney disease | -18.6817 | 10.5904 | ±21.1807 | -1.764 | 0.0777 | . |
| Circulatory disease | +13.1543 | 6.9566 | ±13.9133 | +1.891 | 0.0586 | . |
| Avg. daily time < 70 (%) | +0.1054 | 0.8810 | ±1.7620 | +0.120 | 0.9047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0206**, F-statistic = **3.17** (p = **3.04e-04**), Residual SE = **65.532** on **1125** df, AIC = **12749.7**, BIC = **12810.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.5692** | 44.8398 | ±89.6796 | **+8.755** | **2.04e-18** | *** |
| Education: graduate level (vs college) | +0.6253 | 4.0973 | ±8.1946 | +0.153 | 0.8787 |  |
| Education: high school or below (vs college) | -15.6428 | 8.8217 | ±17.6434 | -1.773 | 0.0762 | . |
| Site: UCSD (vs UAB) | -6.3216 | 5.4384 | ±10.8768 | -1.162 | 0.2451 |  |
| Site: UW (vs UAB) | -1.3206 | 4.7792 | ±9.5585 | -0.276 | 0.7823 |  |
| Age (years) | -0.0584 | 0.1880 | ±0.3759 | -0.311 | 0.7561 |  |
| **BMI (kg/m2)** | **-0.9247** | 0.3274 | ±0.6549 | **-2.824** | **0.0047** | ** |
| Hypertension | -7.6487 | 4.4095 | ±8.8190 | -1.735 | 0.0828 | . |
| High cholesterol | -2.4820 | 4.0273 | ±8.0547 | -0.616 | 0.5377 |  |
| Kidney disease | -18.6140 | 10.5971 | ±21.1941 | -1.757 | 0.0790 | . |
| Circulatory disease | +13.2281 | 6.9768 | ±13.9536 | +1.896 | 0.0580 | . |
| Time 54-250, pooled (%) | +0.1174 | 0.4156 | ±0.8313 | +0.283 | 0.7776 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0206**, F-statistic = **3.17** (p = **3.05e-04**), Residual SE = **65.532** on **1125** df, AIC = **12749.7**, BIC = **12810.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.8137** | 46.1902 | ±92.3805 | **+8.504** | **1.83e-17** | *** |
| Education: graduate level (vs college) | +0.6263 | 4.0974 | ±8.1948 | +0.153 | 0.8785 |  |
| Education: high school or below (vs college) | -15.6455 | 8.8207 | ±17.6415 | -1.774 | 0.0761 | . |
| Site: UCSD (vs UAB) | -6.3117 | 5.4365 | ±10.8731 | -1.161 | 0.2456 |  |
| Site: UW (vs UAB) | -1.3147 | 4.7793 | ±9.5587 | -0.275 | 0.7832 |  |
| Age (years) | -0.0582 | 0.1880 | ±0.3759 | -0.309 | 0.7570 |  |
| **BMI (kg/m2)** | **-0.9243** | 0.3275 | ±0.6549 | **-2.823** | **0.0048** | ** |
| Hypertension | -7.6481 | 4.4105 | ±8.8210 | -1.734 | 0.0829 | . |
| High cholesterol | -2.4801 | 4.0269 | ±8.0538 | -0.616 | 0.5380 |  |
| Kidney disease | -18.6209 | 10.5986 | ±21.1972 | -1.757 | 0.0789 | . |
| Circulatory disease | +13.2224 | 6.9763 | ±13.9527 | +1.895 | 0.0580 | . |
| Avg. daily time 54-250 (%) | +0.1146 | 0.4281 | ±0.8562 | +0.268 | 0.7890 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1137**, R² = **0.0306**, Adj R² = **0.0212**, F-statistic = **3.23** (p = **2.33e-04**), Residual SE = **65.512** on **1125** df, AIC = **12749.0**, BIC = **12809.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.1092** | 16.4427 | ±32.8854 | **+24.577** | **2.24e-133** | *** |
| Education: graduate level (vs college) | +0.5320 | 4.1212 | ±8.2424 | +0.129 | 0.8973 |  |
| Education: high school or below (vs college) | -15.8211 | 8.8023 | ±17.6047 | -1.797 | 0.0723 | . |
| Site: UCSD (vs UAB) | -6.1894 | 5.4376 | ±10.8752 | -1.138 | 0.2550 |  |
| Site: UW (vs UAB) | -1.5251 | 4.7917 | ±9.5833 | -0.318 | 0.7503 |  |
| Age (years) | -0.0615 | 0.1882 | ±0.3764 | -0.327 | 0.7440 |  |
| **BMI (kg/m2)** | **-0.9307** | 0.3289 | ±0.6578 | **-2.830** | **0.0047** | ** |
| Hypertension | -7.9268 | 4.3924 | ±8.7848 | -1.805 | 0.0711 | . |
| High cholesterol | -2.8424 | 4.0351 | ±8.0703 | -0.704 | 0.4812 |  |
| Kidney disease | -19.2707 | 10.6293 | ±21.2586 | -1.813 | 0.0698 | . |
| Circulatory disease | +13.0842 | 6.9569 | ±13.9138 | +1.881 | 0.0600 | . |
| Time 181-250, pooled (%) | +0.2915 | 0.3730 | ±0.7460 | +0.781 | 0.4346 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1137**, R² = **0.0307**, Adj R² = **0.0212**, F-statistic = **3.24** (p = **2.29e-04**), Residual SE = **65.510** on **1125** df, AIC = **12748.9**, BIC = **12809.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.1246** | 16.4457 | ±32.8915 | **+24.573** | **2.44e-133** | *** |
| Education: graduate level (vs college) | +0.5218 | 4.1222 | ±8.2445 | +0.127 | 0.8993 |  |
| Education: high school or below (vs college) | -15.8001 | 8.8010 | ±17.6021 | -1.795 | 0.0726 | . |
| Site: UCSD (vs UAB) | -6.1602 | 5.4391 | ±10.8782 | -1.133 | 0.2574 |  |
| Site: UW (vs UAB) | -1.5084 | 4.7886 | ±9.5772 | -0.315 | 0.7528 |  |
| Age (years) | -0.0611 | 0.1882 | ±0.3763 | -0.325 | 0.7454 |  |
| **BMI (kg/m2)** | **-0.9318** | 0.3289 | ±0.6579 | **-2.833** | **0.0046** | ** |
| Hypertension | -7.9334 | 4.3940 | ±8.7880 | -1.806 | 0.0710 | . |
| High cholesterol | -2.8583 | 4.0328 | ±8.0656 | -0.709 | 0.4785 |  |
| Kidney disease | -19.2943 | 10.6339 | ±21.2678 | -1.814 | 0.0696 | . |
| Circulatory disease | +13.0669 | 6.9572 | ±13.9144 | +1.878 | 0.0604 | . |
| Avg. daily time 181-250 (%) | +0.2971 | 0.3686 | ±0.7372 | +0.806 | 0.4202 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1137**, R² = **0.0303**, Adj R² = **0.0208**, F-statistic = **3.19** (p = **2.74e-04**), Residual SE = **65.524** on **1125** df, AIC = **12749.4**, BIC = **12809.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.0319** | 16.4117 | ±32.8234 | **+24.618** | **8.01e-134** | *** |
| Education: graduate level (vs college) | +0.6167 | 4.1056 | ±8.2112 | +0.150 | 0.8806 |  |
| Education: high school or below (vs college) | -15.8847 | 8.8290 | ±17.6579 | -1.799 | 0.0720 | . |
| Site: UCSD (vs UAB) | -6.1930 | 5.4398 | ±10.8797 | -1.138 | 0.2549 |  |
| Site: UW (vs UAB) | -1.4183 | 4.7918 | ±9.5836 | -0.296 | 0.7672 |  |
| Age (years) | -0.0590 | 0.1881 | ±0.3762 | -0.314 | 0.7538 |  |
| **BMI (kg/m2)** | **-0.9263** | 0.3283 | ±0.6567 | **-2.821** | **0.0048** | ** |
| Hypertension | -7.7264 | 4.3956 | ±8.7913 | -1.758 | 0.0788 | . |
| High cholesterol | -2.7096 | 4.0303 | ±8.0606 | -0.672 | 0.5014 |  |
| Kidney disease | -19.0416 | 10.6123 | ±21.2246 | -1.794 | 0.0728 | . |
| Circulatory disease | +13.0373 | 6.9713 | ±13.9425 | +1.870 | 0.0615 | . |
| Time > 180 (%) | +0.1413 | 0.2584 | ±0.5168 | +0.547 | 0.5844 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1137**, R² = **0.0303**, Adj R² = **0.0208**, F-statistic = **3.20** (p = **2.70e-04**), Residual SE = **65.523** on **1125** df, AIC = **12749.4**, BIC = **12809.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.0515** | 16.4166 | ±32.8331 | **+24.612** | **9.30e-134** | *** |
| Education: graduate level (vs college) | +0.6104 | 4.1065 | ±8.2130 | +0.149 | 0.8818 |  |
| Education: high school or below (vs college) | -15.8761 | 8.8264 | ±17.6527 | -1.799 | 0.0721 | . |
| Site: UCSD (vs UAB) | -6.1768 | 5.4404 | ±10.8807 | -1.135 | 0.2562 |  |
| Site: UW (vs UAB) | -1.4164 | 4.7907 | ±9.5814 | -0.296 | 0.7675 |  |
| Age (years) | -0.0589 | 0.1881 | ±0.3761 | -0.313 | 0.7542 |  |
| **BMI (kg/m2)** | **-0.9273** | 0.3285 | ±0.6569 | **-2.823** | **0.0048** | ** |
| Hypertension | -7.7318 | 4.3963 | ±8.7925 | -1.759 | 0.0786 | . |
| High cholesterol | -2.7233 | 4.0283 | ±8.0566 | -0.676 | 0.4990 |  |
| Kidney disease | -19.0599 | 10.6172 | ±21.2344 | -1.795 | 0.0726 | . |
| Circulatory disease | +13.0271 | 6.9710 | ±13.9420 | +1.869 | 0.0617 | . |
| Avg. daily time > 180 (%) | +0.1480 | 0.2578 | ±0.5157 | +0.574 | 0.5660 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1137**, R² = **0.0304**, Adj R² = **0.0210**, F-statistic = **3.21** (p = **2.55e-04**), Residual SE = **65.519** on **1125** df, AIC = **12749.2**, BIC = **12809.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.2483** | 16.4385 | ±32.8769 | **+24.592** | **1.55e-133** | *** |
| Education: graduate level (vs college) | +0.7098 | 4.0936 | ±8.1872 | +0.173 | 0.8623 |  |
| Education: high school or below (vs college) | -15.8767 | 8.8357 | ±17.6715 | -1.797 | 0.0724 | . |
| Site: UCSD (vs UAB) | -6.1622 | 5.4361 | ±10.8722 | -1.134 | 0.2570 |  |
| Site: UW (vs UAB) | -1.3895 | 4.7860 | ±9.5719 | -0.290 | 0.7716 |  |
| Age (years) | -0.0548 | 0.1879 | ±0.3759 | -0.292 | 0.7704 |  |
| **BMI (kg/m2)** | **-0.9403** | 0.3306 | ±0.6611 | **-2.845** | **0.0044** | ** |
| Hypertension | -7.6417 | 4.4042 | ±8.8084 | -1.735 | 0.0827 | . |
| High cholesterol | -2.8256 | 4.0410 | ±8.0820 | -0.699 | 0.4844 |  |
| Kidney disease | -18.7860 | 10.5874 | ±21.1748 | -1.774 | 0.0760 | . |
| Circulatory disease | +13.1223 | 6.9600 | ±13.9199 | +1.885 | 0.0594 | . |
| Nocturnal time > 180 (%) | +0.1896 | 0.2587 | ±0.5173 | +0.733 | 0.4636 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0205**, F-statistic = **3.16** (p = **3.10e-04**), Residual SE = **65.533** on **1125** df, AIC = **12749.7**, BIC = **12810.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.2996** | 16.4876 | ±32.9753 | **+24.521** | **8.74e-133** | *** |
| Education: graduate level (vs college) | +0.6494 | 4.1005 | ±8.2010 | +0.158 | 0.8742 |  |
| Education: high school or below (vs college) | -15.7257 | 8.7997 | ±17.5995 | -1.787 | 0.0739 | . |
| Site: UCSD (vs UAB) | -6.2749 | 5.4312 | ±10.8624 | -1.155 | 0.2480 |  |
| Site: UW (vs UAB) | -1.2974 | 4.7856 | ±9.5712 | -0.271 | 0.7863 |  |
| Age (years) | -0.0577 | 0.1881 | ±0.3763 | -0.307 | 0.7591 |  |
| **BMI (kg/m2)** | **-0.9262** | 0.3294 | ±0.6588 | **-2.812** | **0.0049** | ** |
| Hypertension | -7.5810 | 4.3996 | ±8.7991 | -1.723 | 0.0849 | . |
| High cholesterol | -2.4868 | 4.0281 | ±8.0561 | -0.617 | 0.5370 |  |
| Kidney disease | -18.6653 | 10.5943 | ±21.1887 | -1.762 | 0.0781 | . |
| Circulatory disease | +13.1481 | 6.9656 | ±13.9312 | +1.888 | 0.0591 | . |
| Any reading > 250 during wear (0/1) | -0.4700 | 5.0070 | ±10.0140 | -0.094 | 0.9252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0205**, F-statistic = **3.16** (p = **3.09e-04**), Residual SE = **65.533** on **1125** df, AIC = **12749.7**, BIC = **12810.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.2141** | 16.3987 | ±32.7973 | **+24.649** | **3.75e-134** | *** |
| Education: graduate level (vs college) | +0.6381 | 4.0969 | ±8.1937 | +0.156 | 0.8762 |  |
| Education: high school or below (vs college) | -15.6770 | 8.8292 | ±17.6585 | -1.776 | 0.0758 | . |
| Site: UCSD (vs UAB) | -6.2839 | 5.4348 | ±10.8696 | -1.156 | 0.2476 |  |
| Site: UW (vs UAB) | -1.3051 | 4.7823 | ±9.5646 | -0.273 | 0.7849 |  |
| Age (years) | -0.0580 | 0.1880 | ±0.3760 | -0.309 | 0.7577 |  |
| **BMI (kg/m2)** | **-0.9242** | 0.3275 | ±0.6550 | **-2.822** | **0.0048** | ** |
| Hypertension | -7.6279 | 4.4086 | ±8.8172 | -1.730 | 0.0836 | . |
| High cholesterol | -2.4885 | 4.0273 | ±8.0547 | -0.618 | 0.5366 |  |
| Kidney disease | -18.6492 | 10.5939 | ±21.1878 | -1.760 | 0.0783 | . |
| Circulatory disease | +13.1928 | 6.9801 | ±13.9601 | +1.890 | 0.0587 | . |
| Time > 250 (%) | -0.0600 | 0.4703 | ±0.9406 | -0.128 | 0.8984 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,137)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1137**, R² = **0.0300**, Adj R² = **0.0205**, F-statistic = **3.16** (p = **3.09e-04**), Residual SE = **65.533** on **1125** df, AIC = **12749.7**, BIC = **12810.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.2078** | 16.3983 | ±32.7967 | **+24.649** | **3.74e-134** | *** |
| Education: graduate level (vs college) | +0.6383 | 4.0968 | ±8.1936 | +0.156 | 0.8762 |  |
| Education: high school or below (vs college) | -15.6778 | 8.8271 | ±17.6541 | -1.776 | 0.0757 | . |
| Site: UCSD (vs UAB) | -6.2838 | 5.4346 | ±10.8692 | -1.156 | 0.2476 |  |
| Site: UW (vs UAB) | -1.3037 | 4.7825 | ±9.5651 | -0.273 | 0.7852 |  |
| Age (years) | -0.0580 | 0.1880 | ±0.3760 | -0.308 | 0.7577 |  |
| **BMI (kg/m2)** | **-0.9240** | 0.3275 | ±0.6551 | **-2.821** | **0.0048** | ** |
| Hypertension | -7.6284 | 4.4090 | ±8.8181 | -1.730 | 0.0836 | . |
| High cholesterol | -2.4884 | 4.0270 | ±8.0540 | -0.618 | 0.5366 |  |
| Kidney disease | -18.6505 | 10.5959 | ±21.1917 | -1.760 | 0.0784 | . |
| Circulatory disease | +13.1922 | 6.9795 | ±13.9589 | +1.890 | 0.0587 | . |
| Avg. daily time > 250 (%) | -0.0614 | 0.4728 | ±0.9456 | -0.130 | 0.8967 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 1,130; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **1130**, R² = **0.0816**, Adj R² = **0.0734**, F-statistic = **9.94** (p = **4.16e-16**), Residual SE = **16.661** on **1119** df, AIC = **9575.3**, BIC = **9630.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4909** | 4.4214 | ±8.8428 | **+11.872** | **1.65e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6726** | 1.0675 | ±2.1350 | **-2.504** | **0.0123** | * |
| Education: high school or below (vs college) | +0.5387 | 1.9678 | ±3.9356 | +0.274 | 0.7843 |  |
| Site: UCSD (vs UAB) | +0.3648 | 1.3705 | ±2.7409 | +0.266 | 0.7901 |  |
| Site: UW (vs UAB) | -2.2583 | 1.2008 | ±2.4016 | -1.881 | 0.0600 | . |
| **Age (years)** | **-0.2430** | 0.0487 | ±0.0975 | **-4.985** | **6.20e-07** | *** |
| **BMI (kg/m2)** | **+0.4354** | 0.0855 | ±0.1709 | **+5.094** | **3.51e-07** | *** |
| Hypertension | +0.0423 | 1.1464 | ±2.2929 | +0.037 | 0.9706 |  |
| High cholesterol | -0.0244 | 1.0575 | ±2.1150 | -0.023 | 0.9816 |  |
| Kidney disease | +1.2632 | 2.2584 | ±4.5168 | +0.559 | 0.5759 |  |
| Circulatory disease | -0.1758 | 1.5643 | ±3.1286 | -0.112 | 0.9105 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **1130**, R² = **0.0895**, Adj R² = **0.0806**, F-statistic = **9.99** (p = **1.62e-17**), Residual SE = **16.596** on **1118** df, AIC = **9567.5**, BIC = **9627.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+37.4757** | 6.4930 | ±12.9860 | **+5.772** | **7.85e-09** | *** |
| **Education: graduate level (vs college)** | **-2.6709** | 1.0659 | ±2.1317 | **-2.506** | **0.0122** | * |
| Education: high school or below (vs college) | +0.2032 | 1.9322 | ±3.8644 | +0.105 | 0.9162 |  |
| Site: UCSD (vs UAB) | +0.2278 | 1.3676 | ±2.7352 | +0.167 | 0.8677 |  |
| **Site: UW (vs UAB)** | **-2.3901** | 1.1919 | ±2.3837 | **-2.005** | **0.0449** | * |
| **Age (years)** | **-0.2554** | 0.0487 | ±0.0974 | **-5.244** | **1.57e-07** | *** |
| **BMI (kg/m2)** | **+0.4140** | 0.0838 | ±0.1675 | **+4.942** | **7.74e-07** | *** |
| Hypertension | -0.0939 | 1.1429 | ±2.2858 | -0.082 | 0.9345 |  |
| High cholesterol | -0.4475 | 1.0572 | ±2.1145 | -0.423 | 0.6721 |  |
| Kidney disease | +1.2716 | 2.2427 | ±4.4854 | +0.567 | 0.5707 |  |
| Circulatory disease | -0.3354 | 1.5297 | ±3.0594 | -0.219 | 0.8264 |  |
| **HbA1c (%)** | **+2.9623** | 0.9302 | ±1.8604 | **+3.185** | **0.0014** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **1130**, R² = **0.0857**, Adj R² = **0.0767**, F-statistic = **9.53** (p = **1.35e-16**), Residual SE = **16.631** on **1118** df, AIC = **9572.2**, BIC = **9632.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.9724** | 5.6176 | ±11.2351 | **+8.184** | **2.75e-16** | *** |
| **Education: graduate level (vs college)** | **-2.7848** | 1.0665 | ±2.1330 | **-2.611** | **0.0090** | ** |
| Education: high school or below (vs college) | +0.3351 | 1.9544 | ±3.9088 | +0.171 | 0.8639 |  |
| Site: UCSD (vs UAB) | +0.3172 | 1.3734 | ±2.7468 | +0.231 | 0.8173 |  |
| **Site: UW (vs UAB)** | **-2.4758** | 1.2044 | ±2.4089 | **-2.056** | **0.0398** | * |
| **Age (years)** | **-0.2462** | 0.0487 | ±0.0975 | **-5.052** | **4.37e-07** | *** |
| **BMI (kg/m2)** | **+0.4268** | 0.0852 | ±0.1703 | **+5.012** | **5.39e-07** | *** |
| Hypertension | -0.1539 | 1.1489 | ±2.2979 | -0.134 | 0.8935 |  |
| High cholesterol | -0.2104 | 1.0582 | ±2.1164 | -0.199 | 0.8424 |  |
| Kidney disease | +1.0083 | 2.2524 | ±4.5048 | +0.448 | 0.6544 |  |
| Circulatory disease | -0.2747 | 1.5504 | ±3.1008 | -0.177 | 0.8594 |  |
| Mean glucose (mg/dL) | +0.0605 | 0.0328 | ±0.0656 | +1.845 | 0.0651 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **1130**, R² = **0.0857**, Adj R² = **0.0767**, F-statistic = **9.53** (p = **1.35e-16**), Residual SE = **16.631** on **1118** df, AIC = **9572.2**, BIC = **9632.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+37.6006** | 9.1631 | ±18.3263 | **+4.103** | **4.07e-05** | *** |
| **Education: graduate level (vs college)** | **-2.7848** | 1.0665 | ±2.1330 | **-2.611** | **0.0090** | ** |
| Education: high school or below (vs college) | +0.3351 | 1.9544 | ±3.9088 | +0.171 | 0.8639 |  |
| Site: UCSD (vs UAB) | +0.3172 | 1.3734 | ±2.7468 | +0.231 | 0.8173 |  |
| **Site: UW (vs UAB)** | **-2.4758** | 1.2044 | ±2.4089 | **-2.056** | **0.0398** | * |
| **Age (years)** | **-0.2462** | 0.0487 | ±0.0975 | **-5.052** | **4.37e-07** | *** |
| **BMI (kg/m2)** | **+0.4268** | 0.0852 | ±0.1703 | **+5.012** | **5.39e-07** | *** |
| Hypertension | -0.1539 | 1.1489 | ±2.2979 | -0.134 | 0.8935 |  |
| High cholesterol | -0.2104 | 1.0582 | ±2.1164 | -0.199 | 0.8424 |  |
| Kidney disease | +1.0083 | 2.2524 | ±4.5048 | +0.448 | 0.6544 |  |
| Circulatory disease | -0.2747 | 1.5504 | ±3.1008 | -0.177 | 0.8594 |  |
| GMI (%) | +2.5292 | 1.3711 | ±2.7421 | +1.845 | 0.0651 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **1130**, R² = **0.0847**, Adj R² = **0.0757**, F-statistic = **9.41** (p = **2.40e-16**), Residual SE = **16.640** on **1118** df, AIC = **9573.4**, BIC = **9633.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.1952** | 5.4751 | ±10.9501 | **+8.620** | **6.69e-18** | *** |
| **Education: graduate level (vs college)** | **-2.7240** | 1.0666 | ±2.1333 | **-2.554** | **0.0107** | * |
| Education: high school or below (vs college) | +0.3592 | 1.9560 | ±3.9120 | +0.184 | 0.8543 |  |
| Site: UCSD (vs UAB) | +0.2582 | 1.3728 | ±2.7456 | +0.188 | 0.8508 |  |
| **Site: UW (vs UAB)** | **-2.4338** | 1.2045 | ±2.4090 | **-2.021** | **0.0433** | * |
| **Age (years)** | **-0.2409** | 0.0486 | ±0.0973 | **-4.953** | **7.30e-07** | *** |
| **BMI (kg/m2)** | **+0.4157** | 0.0855 | ±0.1710 | **+4.861** | **1.17e-06** | *** |
| Hypertension | -0.0918 | 1.1487 | ±2.2975 | -0.080 | 0.9363 |  |
| High cholesterol | -0.2211 | 1.0598 | ±2.1196 | -0.209 | 0.8347 |  |
| Kidney disease | +1.1970 | 2.2479 | ±4.4959 | +0.533 | 0.5944 |  |
| Circulatory disease | -0.2118 | 1.5509 | ±3.1018 | -0.137 | 0.8914 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0503 | 0.0318 | ±0.0636 | +1.582 | 0.1136 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **1130**, R² = **0.0879**, Adj R² = **0.0789**, F-statistic = **9.79** (p = **4.12e-17**), Residual SE = **16.611** on **1118** df, AIC = **9569.5**, BIC = **9629.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.2746** | 4.7285 | ±9.4569 | **+10.209** | **1.80e-24** | *** |
| **Education: graduate level (vs college)** | **-2.7063** | 1.0619 | ±2.1238 | **-2.549** | **0.0108** | * |
| Education: high school or below (vs college) | +0.5144 | 1.9507 | ±3.9015 | +0.264 | 0.7920 |  |
| Site: UCSD (vs UAB) | +0.4993 | 1.3724 | ±2.7447 | +0.364 | 0.7160 |  |
| **Site: UW (vs UAB)** | **-2.3948** | 1.2009 | ±2.4019 | **-1.994** | **0.0461** | * |
| **Age (years)** | **-0.2488** | 0.0487 | ±0.0973 | **-5.114** | **3.15e-07** | *** |
| **BMI (kg/m2)** | **+0.4393** | 0.0857 | ±0.1714 | **+5.127** | **2.94e-07** | *** |
| Hypertension | -0.2271 | 1.1516 | ±2.3031 | -0.197 | 0.8437 |  |
| High cholesterol | -0.0896 | 1.0551 | ±2.1103 | -0.085 | 0.9323 |  |
| Kidney disease | +0.7412 | 2.2741 | ±4.5482 | +0.326 | 0.7445 |  |
| Circulatory disease | -0.2881 | 1.5494 | ±3.0988 | -0.186 | 0.8525 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.2162** | 0.0876 | ±0.1752 | **+2.469** | **0.0136** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **1130**, R² = **0.0868**, Adj R² = **0.0778**, F-statistic = **9.66** (p = **7.56e-17**), Residual SE = **16.621** on **1118** df, AIC = **9570.9**, BIC = **9631.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.0248** | 4.6627 | ±9.3255 | **+10.514** | **7.43e-26** | *** |
| **Education: graduate level (vs college)** | **-2.7194** | 1.0632 | ±2.1265 | **-2.558** | **0.0105** | * |
| Education: high school or below (vs college) | +0.4908 | 1.9542 | ±3.9084 | +0.251 | 0.8017 |  |
| Site: UCSD (vs UAB) | +0.4560 | 1.3711 | ±2.7422 | +0.333 | 0.7394 |  |
| **Site: UW (vs UAB)** | **-2.4073** | 1.2026 | ±2.4052 | **-2.002** | **0.0453** | * |
| **Age (years)** | **-0.2499** | 0.0488 | ±0.0975 | **-5.126** | **2.97e-07** | *** |
| **BMI (kg/m2)** | **+0.4359** | 0.0853 | ±0.1707 | **+5.108** | **3.26e-07** | *** |
| Hypertension | -0.2008 | 1.1530 | ±2.3061 | -0.174 | 0.8618 |  |
| High cholesterol | -0.0873 | 1.0563 | ±2.1125 | -0.083 | 0.9341 |  |
| Kidney disease | +0.8005 | 2.2759 | ±4.5518 | +0.352 | 0.7250 |  |
| Circulatory disease | -0.2758 | 1.5514 | ±3.1029 | -0.178 | 0.8589 |  |
| **Avg. daily SD (mg/dL)** | **+0.2081** | 0.0925 | ±0.1851 | **+2.249** | **0.0245** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **1130**, R² = **0.0857**, Adj R² = **0.0767**, F-statistic = **9.53** (p = **1.35e-16**), Residual SE = **16.631** on **1118** df, AIC = **9572.2**, BIC = **9632.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4507** | 4.9923 | ±9.9846 | **+9.505** | **2.01e-21** | *** |
| **Education: graduate level (vs college)** | **-2.6248** | 1.0623 | ±2.1245 | **-2.471** | **0.0135** | * |
| Education: high school or below (vs college) | +0.6463 | 1.9591 | ±3.9183 | +0.330 | 0.7415 |  |
| Site: UCSD (vs UAB) | +0.5618 | 1.3692 | ±2.7384 | +0.410 | 0.6816 |  |
| Site: UW (vs UAB) | -2.2352 | 1.2010 | ±2.4021 | -1.861 | 0.0627 | . |
| **Age (years)** | **-0.2475** | 0.0487 | ±0.0975 | **-5.079** | **3.79e-07** | *** |
| **BMI (kg/m2)** | **+0.4451** | 0.0861 | ±0.1722 | **+5.170** | **2.34e-07** | *** |
| Hypertension | -0.0982 | 1.1487 | ±2.2975 | -0.086 | 0.9319 |  |
| High cholesterol | +0.0550 | 1.0580 | ±2.1160 | +0.052 | 0.9586 |  |
| Kidney disease | +0.9269 | 2.2805 | ±4.5610 | +0.406 | 0.6844 |  |
| Circulatory disease | -0.2093 | 1.5582 | ±3.1163 | -0.134 | 0.8931 |  |
| **CV (%)** | **+0.2801** | 0.1299 | ±0.2597 | **+2.157** | **0.0310** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **1130**, R² = **0.0872**, Adj R² = **0.0782**, F-statistic = **9.71** (p = **5.92e-17**), Residual SE = **16.617** on **1118** df, AIC = **9570.3**, BIC = **9630.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.8240** | 5.0035 | ±10.0071 | **+11.756** | **6.54e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6044** | 1.0609 | ±2.1218 | **-2.455** | **0.0141** | * |
| Education: high school or below (vs college) | +0.5863 | 1.9557 | ±3.9114 | +0.300 | 0.7643 |  |
| Site: UCSD (vs UAB) | +0.5776 | 1.3675 | ±2.7351 | +0.422 | 0.6727 |  |
| Site: UW (vs UAB) | -2.2974 | 1.1999 | ±2.3998 | -1.915 | 0.0555 | . |
| **Age (years)** | **-0.2484** | 0.0487 | ±0.0974 | **-5.099** | **3.41e-07** | *** |
| **BMI (kg/m2)** | **+0.4447** | 0.0859 | ±0.1718 | **+5.177** | **2.26e-07** | *** |
| Hypertension | -0.1486 | 1.1499 | ±2.2998 | -0.129 | 0.8972 |  |
| High cholesterol | +0.0440 | 1.0566 | ±2.1132 | +0.042 | 0.9668 |  |
| Kidney disease | +0.9838 | 2.2696 | ±4.5392 | +0.433 | 0.6647 |  |
| Circulatory disease | -0.2047 | 1.5556 | ±3.1112 | -0.132 | 0.8953 |  |
| **Mean / SD ratio** | **-1.0683** | 0.4090 | ±0.8180 | **-2.612** | **0.0090** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **1130**, R² = **0.0860**, Adj R² = **0.0770**, F-statistic = **9.56** (p = **1.16e-16**), Residual SE = **16.628** on **1118** df, AIC = **9571.8**, BIC = **9632.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.1931** | 5.0365 | ±10.0729 | **+11.554** | **7.02e-31** | *** |
| **Education: graduate level (vs college)** | **-2.6513** | 1.0628 | ±2.1255 | **-2.495** | **0.0126** | * |
| Education: high school or below (vs college) | +0.5070 | 1.9585 | ±3.9170 | +0.259 | 0.7957 |  |
| Site: UCSD (vs UAB) | +0.5065 | 1.3677 | ±2.7355 | +0.370 | 0.7111 |  |
| Site: UW (vs UAB) | -2.3240 | 1.2018 | ±2.4036 | -1.934 | 0.0531 | . |
| **Age (years)** | **-0.2503** | 0.0489 | ±0.0977 | **-5.123** | **3.00e-07** | *** |
| **BMI (kg/m2)** | **+0.4385** | 0.0853 | ±0.1706 | **+5.140** | **2.75e-07** | *** |
| Hypertension | -0.0854 | 1.1505 | ±2.3009 | -0.074 | 0.9409 |  |
| High cholesterol | +0.0295 | 1.0581 | ±2.1162 | +0.028 | 0.9778 |  |
| Kidney disease | +0.9689 | 2.2741 | ±4.5482 | +0.426 | 0.6701 |  |
| Circulatory disease | -0.1877 | 1.5599 | ±3.1198 | -0.120 | 0.9042 |  |
| **Avg. daily mean/SD** | **-0.7891** | 0.3420 | ±0.6840 | **-2.307** | **0.0210** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **1130**, R² = **0.0861**, Adj R² = **0.0771**, F-statistic = **9.58** (p = **1.08e-16**), Residual SE = **16.627** on **1118** df, AIC = **9571.7**, BIC = **9632.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.2161** | 5.1036 | ±10.2072 | **+9.056** | **1.36e-19** | *** |
| **Education: graduate level (vs college)** | **-2.6219** | 1.0621 | ±2.1242 | **-2.469** | **0.0136** | * |
| Education: high school or below (vs college) | +0.4461 | 1.9604 | ±3.9209 | +0.228 | 0.8200 |  |
| Site: UCSD (vs UAB) | +0.5306 | 1.3713 | ±2.7425 | +0.387 | 0.6988 |  |
| Site: UW (vs UAB) | -2.0977 | 1.2009 | ±2.4018 | -1.747 | 0.0807 | . |
| **Age (years)** | **-0.2384** | 0.0485 | ±0.0971 | **-4.912** | **9.03e-07** | *** |
| **BMI (kg/m2)** | **+0.4385** | 0.0850 | ±0.1700 | **+5.159** | **2.48e-07** | *** |
| Hypertension | +0.0676 | 1.1493 | ±2.2985 | +0.059 | 0.9531 |  |
| High cholesterol | +0.0587 | 1.0583 | ±2.1165 | +0.055 | 0.9558 |  |
| Kidney disease | +1.0704 | 2.2471 | ±4.4942 | +0.476 | 0.6338 |  |
| Circulatory disease | -0.1133 | 1.5567 | ±3.1134 | -0.073 | 0.9420 |  |
| **MAG (mg/dL/h)** | **+0.1508** | 0.0671 | ±0.1342 | **+2.247** | **0.0246** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **1130**, R² = **0.0870**, Adj R² = **0.0780**, F-statistic = **9.69** (p = **6.58e-17**), Residual SE = **16.619** on **1118** df, AIC = **9570.6**, BIC = **9630.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6468** | 4.8534 | ±9.7067 | **+9.817** | **9.49e-23** | *** |
| **Education: graduate level (vs college)** | **-2.7231** | 1.0629 | ±2.1257 | **-2.562** | **0.0104** | * |
| Education: high school or below (vs college) | +0.4461 | 1.9567 | ±3.9134 | +0.228 | 0.8197 |  |
| Site: UCSD (vs UAB) | +0.4638 | 1.3698 | ±2.7396 | +0.339 | 0.7349 |  |
| **Site: UW (vs UAB)** | **-2.3590** | 1.2011 | ±2.4021 | **-1.964** | **0.0495** | * |
| **Age (years)** | **-0.2484** | 0.0488 | ±0.0975 | **-5.095** | **3.49e-07** | *** |
| **BMI (kg/m2)** | **+0.4485** | 0.0863 | ±0.1726 | **+5.198** | **2.02e-07** | *** |
| Hypertension | -0.1322 | 1.1517 | ±2.3034 | -0.115 | 0.9086 |  |
| High cholesterol | -0.0243 | 1.0567 | ±2.1134 | -0.023 | 0.9816 |  |
| Kidney disease | +0.8957 | 2.2691 | ±4.5381 | +0.395 | 0.6930 |  |
| Circulatory disease | -0.2586 | 1.5550 | ±3.1101 | -0.166 | 0.8679 |  |
| **Avg. daily range (mg/dL)** | **+0.0501** | 0.0206 | ±0.0412 | **+2.433** | **0.0150** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **1130**, R² = **0.0885**, Adj R² = **0.0796**, F-statistic = **9.87** (p = **2.81e-17**), Residual SE = **16.605** on **1118** df, AIC = **9568.7**, BIC = **9629.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5982** | 4.5335 | ±9.0670 | **+10.940** | **7.38e-28** | *** |
| **Education: graduate level (vs college)** | **-2.7013** | 1.0635 | ±2.1270 | **-2.540** | **0.0111** | * |
| Education: high school or below (vs college) | +0.6332 | 1.9341 | ±3.8682 | +0.327 | 0.7434 |  |
| Site: UCSD (vs UAB) | +0.5939 | 1.3671 | ±2.7342 | +0.434 | 0.6640 |  |
| Site: UW (vs UAB) | -2.2992 | 1.1958 | ±2.3915 | -1.923 | 0.0545 | . |
| **Age (years)** | **-0.2401** | 0.0484 | ±0.0969 | **-4.957** | **7.17e-07** | *** |
| **BMI (kg/m2)** | **+0.4257** | 0.0858 | ±0.1715 | **+4.963** | **6.95e-07** | *** |
| Hypertension | -0.0259 | 1.1415 | ±2.2829 | -0.023 | 0.9819 |  |
| High cholesterol | -0.1572 | 1.0541 | ±2.1083 | -0.149 | 0.8814 |  |
| Kidney disease | +1.1062 | 2.2489 | ±4.4977 | +0.492 | 0.6228 |  |
| Circulatory disease | -0.2699 | 1.5476 | ±3.0952 | -0.174 | 0.8616 |  |
| **SD of daily means (mg/dL)** | **+0.4649** | 0.1707 | ±0.3414 | **+2.723** | **0.0065** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **1130**, R² = **0.0837**, Adj R² = **0.0746**, F-statistic = **9.28** (p = **4.31e-16**), Residual SE = **16.650** on **1118** df, AIC = **9574.7**, BIC = **9635.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.5103** | 9.0936 | ±18.1873 | **+6.764** | **1.34e-11** | *** |
| **Education: graduate level (vs college)** | **-2.6980** | 1.0675 | ±2.1349 | **-2.528** | **0.0115** | * |
| Education: high school or below (vs college) | +0.4962 | 1.9549 | ±3.9099 | +0.254 | 0.7997 |  |
| Site: UCSD (vs UAB) | +0.4205 | 1.3792 | ±2.7584 | +0.305 | 0.7604 |  |
| Site: UW (vs UAB) | -2.2865 | 1.1999 | ±2.3998 | -1.906 | 0.0567 | . |
| **Age (years)** | **-0.2423** | 0.0487 | ±0.0973 | **-4.980** | **6.35e-07** | *** |
| **BMI (kg/m2)** | **+0.4323** | 0.0855 | ±0.1711 | **+5.054** | **4.32e-07** | *** |
| Hypertension | -0.0466 | 1.1503 | ±2.3005 | -0.041 | 0.9677 |  |
| High cholesterol | -0.1100 | 1.0594 | ±2.1188 | -0.104 | 0.9173 |  |
| Kidney disease | +1.0564 | 2.2675 | ±4.5350 | +0.466 | 0.6413 |  |
| Circulatory disease | -0.2515 | 1.5575 | ±3.1150 | -0.161 | 0.8717 |  |
| Time in range 70-180, pooled (%) | -0.0927 | 0.0824 | ±0.1648 | -1.126 | 0.2602 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **1130**, R² = **0.0834**, Adj R² = **0.0743**, F-statistic = **9.24** (p = **5.09e-16**), Residual SE = **16.652** on **1118** df, AIC = **9575.1**, BIC = **9635.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.8604** | 9.1049 | ±18.2099 | **+6.684** | **2.32e-11** | *** |
| **Education: graduate level (vs college)** | **-2.6972** | 1.0677 | ±2.1354 | **-2.526** | **0.0115** | * |
| Education: high school or below (vs college) | +0.5091 | 1.9565 | ±3.9131 | +0.260 | 0.7947 |  |
| Site: UCSD (vs UAB) | +0.4129 | 1.3784 | ±2.7567 | +0.300 | 0.7645 |  |
| Site: UW (vs UAB) | -2.2829 | 1.2003 | ±2.4005 | -1.902 | 0.0572 | . |
| **Age (years)** | **-0.2426** | 0.0487 | ±0.0974 | **-4.984** | **6.22e-07** | *** |
| **BMI (kg/m2)** | **+0.4320** | 0.0855 | ±0.1710 | **+5.054** | **4.32e-07** | *** |
| Hypertension | -0.0391 | 1.1503 | ±2.3006 | -0.034 | 0.9729 |  |
| High cholesterol | -0.1090 | 1.0598 | ±2.1196 | -0.103 | 0.9181 |  |
| Kidney disease | +1.0747 | 2.2677 | ±4.5355 | +0.474 | 0.6356 |  |
| Circulatory disease | -0.2454 | 1.5585 | ±3.1169 | -0.157 | 0.8749 |  |
| Avg. daily time in range 70-180 (%) | -0.0855 | 0.0818 | ±0.1636 | -1.045 | 0.2958 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **1130**, R² = **0.0820**, Adj R² = **0.0730**, F-statistic = **9.08** (p = **1.07e-15**), Residual SE = **16.664** on **1118** df, AIC = **9576.7**, BIC = **9637.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.0475** | 4.4862 | ±8.9725 | **+11.602** | **4.05e-31** | *** |
| **Education: graduate level (vs college)** | **-2.6498** | 1.0689 | ±2.1378 | **-2.479** | **0.0132** | * |
| Education: high school or below (vs college) | +0.6201 | 1.9820 | ±3.9640 | +0.313 | 0.7544 |  |
| Site: UCSD (vs UAB) | +0.4910 | 1.3775 | ±2.7550 | +0.356 | 0.7215 |  |
| Site: UW (vs UAB) | -2.2049 | 1.2037 | ±2.4073 | -1.832 | 0.0670 | . |
| **Age (years)** | **-0.2406** | 0.0490 | ±0.0979 | **-4.914** | **8.94e-07** | *** |
| **BMI (kg/m2)** | **+0.4341** | 0.0855 | ±0.1710 | **+5.078** | **3.81e-07** | *** |
| Hypertension | +0.0337 | 1.1480 | ±2.2960 | +0.029 | 0.9766 |  |
| High cholesterol | +0.0244 | 1.0598 | ±2.1197 | +0.023 | 0.9817 |  |
| Kidney disease | +1.2823 | 2.2680 | ±4.5360 | +0.565 | 0.5718 |  |
| Circulatory disease | -0.2651 | 1.5721 | ±3.1442 | -0.169 | 0.8661 |  |
| Any reading < 54 during wear (0/1) | +0.7802 | 1.0759 | ±2.1519 | +0.725 | 0.4683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **1130**, R² = **0.0816**, Adj R² = **0.0726**, F-statistic = **9.03** (p = **1.36e-15**), Residual SE = **16.668** on **1118** df, AIC = **9577.3**, BIC = **9637.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4636** | 4.4479 | ±8.8957 | **+11.795** | **4.13e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6712** | 1.0677 | ±2.1355 | **-2.502** | **0.0124** | * |
| Education: high school or below (vs college) | +0.5446 | 1.9705 | ±3.9409 | +0.276 | 0.7823 |  |
| Site: UCSD (vs UAB) | +0.3770 | 1.3790 | ±2.7580 | +0.273 | 0.7846 |  |
| Site: UW (vs UAB) | -2.2491 | 1.2055 | ±2.4110 | -1.866 | 0.0621 | . |
| **Age (years)** | **-0.2429** | 0.0488 | ±0.0977 | **-4.975** | **6.54e-07** | *** |
| **BMI (kg/m2)** | **+0.4355** | 0.0856 | ±0.1713 | **+5.085** | **3.68e-07** | *** |
| Hypertension | +0.0449 | 1.1475 | ±2.2951 | +0.039 | 0.9688 |  |
| High cholesterol | -0.0189 | 1.0586 | ±2.1172 | -0.018 | 0.9858 |  |
| Kidney disease | +1.2605 | 2.2599 | ±4.5198 | +0.558 | 0.5770 |  |
| Circulatory disease | -0.1758 | 1.5649 | ±3.1297 | -0.112 | 0.9106 |  |
| Time < 54 (%) | +0.0618 | 0.8855 | ±1.7709 | +0.070 | 0.9444 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **1130**, R² = **0.0816**, Adj R² = **0.0726**, F-statistic = **9.04** (p = **1.32e-15**), Residual SE = **16.668** on **1118** df, AIC = **9577.2**, BIC = **9637.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.5557** | 4.4353 | ±8.8707 | **+11.849** | **2.17e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6793** | 1.0678 | ±2.1357 | **-2.509** | **0.0121** | * |
| Education: high school or below (vs college) | +0.5197 | 1.9724 | ±3.9448 | +0.263 | 0.7922 |  |
| Site: UCSD (vs UAB) | +0.3293 | 1.3754 | ±2.7509 | +0.239 | 0.8108 |  |
| Site: UW (vs UAB) | -2.2913 | 1.2051 | ±2.4103 | -1.901 | 0.0573 | . |
| **Age (years)** | **-0.2429** | 0.0488 | ±0.0975 | **-4.980** | **6.36e-07** | *** |
| **BMI (kg/m2)** | **+0.4352** | 0.0856 | ±0.1712 | **+5.085** | **3.68e-07** | *** |
| Hypertension | +0.0302 | 1.1490 | ±2.2981 | +0.026 | 0.9790 |  |
| High cholesterol | -0.0414 | 1.0581 | ±2.1162 | -0.039 | 0.9688 |  |
| Kidney disease | +1.2711 | 2.2602 | ±4.5205 | +0.562 | 0.5739 |  |
| Circulatory disease | -0.1791 | 1.5647 | ±3.1294 | -0.114 | 0.9089 |  |
| Avg. daily time < 54 (%) | -0.2710 | 1.1803 | ±2.3605 | -0.230 | 0.8184 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **1130**, R² = **0.0816**, Adj R² = **0.0726**, F-statistic = **9.03** (p = **1.33e-15**), Residual SE = **16.668** on **1118** df, AIC = **9577.2**, BIC = **9637.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.5928** | 4.4673 | ±8.9345 | **+11.773** | **5.38e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6843** | 1.0674 | ±2.1349 | **-2.515** | **0.0119** | * |
| Education: high school or below (vs college) | +0.5102 | 1.9742 | ±3.9484 | +0.258 | 0.7961 |  |
| Site: UCSD (vs UAB) | +0.3394 | 1.3750 | ±2.7500 | +0.247 | 0.8050 |  |
| Site: UW (vs UAB) | -2.2850 | 1.2049 | ±2.4098 | -1.896 | 0.0579 | . |
| **Age (years)** | **-0.2434** | 0.0489 | ±0.0978 | **-4.979** | **6.40e-07** | *** |
| **BMI (kg/m2)** | **+0.4357** | 0.0855 | ±0.1711 | **+5.094** | **3.51e-07** | *** |
| Hypertension | +0.0331 | 1.1479 | ±2.2958 | +0.029 | 0.9770 |  |
| High cholesterol | -0.0389 | 1.0585 | ±2.1170 | -0.037 | 0.9707 |  |
| Kidney disease | +1.2618 | 2.2587 | ±4.5174 | +0.559 | 0.5764 |  |
| Circulatory disease | -0.1758 | 1.5654 | ±3.1308 | -0.112 | 0.9106 |  |
| Time 54-69, pooled (%) | -0.0776 | 0.3633 | ±0.7266 | -0.214 | 0.8309 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **1130**, R² = **0.0817**, Adj R² = **0.0727**, F-statistic = **9.04** (p = **1.28e-15**), Residual SE = **16.667** on **1118** df, AIC = **9577.1**, BIC = **9637.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.6292** | 4.4566 | ±8.9131 | **+11.809** | **3.49e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6935** | 1.0681 | ±2.1362 | **-2.522** | **0.0117** | * |
| Education: high school or below (vs college) | +0.4899 | 1.9762 | ±3.9525 | +0.248 | 0.8042 |  |
| Site: UCSD (vs UAB) | +0.3323 | 1.3725 | ±2.7450 | +0.242 | 0.8087 |  |
| Site: UW (vs UAB) | -2.3005 | 1.2031 | ±2.4063 | -1.912 | 0.0559 | . |
| **Age (years)** | **-0.2434** | 0.0488 | ±0.0976 | **-4.986** | **6.17e-07** | *** |
| **BMI (kg/m2)** | **+0.4358** | 0.0856 | ±0.1711 | **+5.093** | **3.52e-07** | *** |
| Hypertension | +0.0259 | 1.1484 | ±2.2968 | +0.023 | 0.9820 |  |
| High cholesterol | -0.0457 | 1.0580 | ±2.1159 | -0.043 | 0.9656 |  |
| Kidney disease | +1.2591 | 2.2578 | ±4.5155 | +0.558 | 0.5771 |  |
| Circulatory disease | -0.1776 | 1.5656 | ±3.1312 | -0.113 | 0.9097 |  |
| Avg. daily time 54-69 (%) | -0.1230 | 0.3839 | ±0.7677 | -0.321 | 0.7486 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **1130**, R² = **0.0816**, Adj R² = **0.0726**, F-statistic = **9.03** (p = **1.34e-15**), Residual SE = **16.668** on **1118** df, AIC = **9577.2**, BIC = **9637.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.5652** | 4.4709 | ±8.9418 | **+11.757** | **6.49e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6800** | 1.0674 | ±2.1347 | **-2.511** | **0.0120** | * |
| Education: high school or below (vs college) | +0.5191 | 1.9742 | ±3.9484 | +0.263 | 0.7926 |  |
| Site: UCSD (vs UAB) | +0.3426 | 1.3778 | ±2.7556 | +0.249 | 0.8036 |  |
| Site: UW (vs UAB) | -2.2791 | 1.2065 | ±2.4130 | -1.889 | 0.0589 | . |
| **Age (years)** | **-0.2432** | 0.0489 | ±0.0978 | **-4.977** | **6.47e-07** | *** |
| **BMI (kg/m2)** | **+0.4355** | 0.0855 | ±0.1711 | **+5.091** | **3.56e-07** | *** |
| Hypertension | +0.0354 | 1.1481 | ±2.2961 | +0.031 | 0.9754 |  |
| High cholesterol | -0.0360 | 1.0588 | ±2.1177 | -0.034 | 0.9728 |  |
| Kidney disease | +1.2643 | 2.2592 | ±4.5184 | +0.560 | 0.5758 |  |
| Circulatory disease | -0.1758 | 1.5652 | ±3.1303 | -0.112 | 0.9106 |  |
| Time < 70 (%) | -0.0423 | 0.2782 | ±0.5563 | -0.152 | 0.8791 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **1130**, R² = **0.0817**, Adj R² = **0.0727**, F-statistic = **9.04** (p = **1.28e-15**), Residual SE = **16.667** on **1118** df, AIC = **9577.1**, BIC = **9637.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.6318** | 4.4571 | ±8.9143 | **+11.808** | **3.53e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6927** | 1.0681 | ±2.1361 | **-2.521** | **0.0117** | * |
| Education: high school or below (vs college) | +0.4905 | 1.9769 | ±3.9538 | +0.248 | 0.8040 |  |
| Site: UCSD (vs UAB) | +0.3240 | 1.3737 | ±2.7475 | +0.236 | 0.8135 |  |
| Site: UW (vs UAB) | -2.3063 | 1.2045 | ±2.4091 | -1.915 | 0.0555 | . |
| **Age (years)** | **-0.2433** | 0.0488 | ±0.0976 | **-4.986** | **6.17e-07** | *** |
| **BMI (kg/m2)** | **+0.4356** | 0.0856 | ±0.1711 | **+5.091** | **3.55e-07** | *** |
| Hypertension | +0.0240 | 1.1489 | ±2.2978 | +0.021 | 0.9834 |  |
| High cholesterol | -0.0487 | 1.0582 | ±2.1163 | -0.046 | 0.9633 |  |
| Kidney disease | +1.2628 | 2.2581 | ±4.5161 | +0.559 | 0.5760 |  |
| Circulatory disease | -0.1786 | 1.5654 | ±3.1308 | -0.114 | 0.9092 |  |
| Avg. daily time < 70 (%) | -0.1033 | 0.3251 | ±0.6502 | -0.318 | 0.7506 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **1130**, R² = **0.0828**, Adj R² = **0.0738**, F-statistic = **9.17** (p = **6.99e-16**), Residual SE = **16.657** on **1118** df, AIC = **9575.8**, BIC = **9636.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.7009** | 21.2201 | ±42.4402 | **+3.096** | **0.0020** | ** |
| **Education: graduate level (vs college)** | **-2.6678** | 1.0710 | ±2.1420 | **-2.491** | **0.0127** | * |
| Education: high school or below (vs college) | +0.4504 | 1.9629 | ±3.9257 | +0.229 | 0.8185 |  |
| Site: UCSD (vs UAB) | +0.3836 | 1.3807 | ±2.7614 | +0.278 | 0.7812 |  |
| Site: UW (vs UAB) | -2.2457 | 1.2010 | ±2.4020 | -1.870 | 0.0615 | . |
| **Age (years)** | **-0.2415** | 0.0488 | ±0.0977 | **-4.946** | **7.57e-07** | *** |
| **BMI (kg/m2)** | **+0.4350** | 0.0858 | ±0.1715 | **+5.073** | **3.92e-07** | *** |
| Hypertension | +0.0531 | 1.1530 | ±2.3060 | +0.046 | 0.9632 |  |
| High cholesterol | -0.0323 | 1.0605 | ±2.1211 | -0.030 | 0.9757 |  |
| Kidney disease | +1.2121 | 2.2701 | ±4.5401 | +0.534 | 0.5934 |  |
| Circulatory disease | -0.2492 | 1.5657 | ±3.1314 | -0.159 | 0.8735 |  |
| Time 54-250, pooled (%) | -0.1336 | 0.2101 | ±0.4202 | -0.636 | 0.5248 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **1130**, R² = **0.0827**, Adj R² = **0.0737**, F-statistic = **9.16** (p = **7.36e-16**), Residual SE = **16.658** on **1118** df, AIC = **9575.9**, BIC = **9636.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+65.6913** | 22.3930 | ±44.7859 | **+2.934** | **0.0034** | ** |
| **Education: graduate level (vs college)** | **-2.6678** | 1.0712 | ±2.1423 | **-2.491** | **0.0128** | * |
| Education: high school or below (vs college) | +0.4515 | 1.9638 | ±3.9276 | +0.230 | 0.8181 |  |
| Site: UCSD (vs UAB) | +0.3748 | 1.3800 | ±2.7600 | +0.272 | 0.7859 |  |
| Site: UW (vs UAB) | -2.2520 | 1.2014 | ±2.4027 | -1.875 | 0.0609 | . |
| **Age (years)** | **-0.2418** | 0.0488 | ±0.0976 | **-4.953** | **7.32e-07** | *** |
| **BMI (kg/m2)** | **+0.4346** | 0.0857 | ±0.1715 | **+5.069** | **4.00e-07** | *** |
| Hypertension | +0.0541 | 1.1533 | ±2.3066 | +0.047 | 0.9626 |  |
| High cholesterol | -0.0355 | 1.0609 | ±2.1217 | -0.033 | 0.9733 |  |
| Kidney disease | +1.2177 | 2.2699 | ±4.5398 | +0.536 | 0.5916 |  |
| Circulatory disease | -0.2445 | 1.5659 | ±3.1317 | -0.156 | 0.8759 |  |
| Avg. daily time 54-250 (%) | -0.1331 | 0.2214 | ±0.4429 | -0.601 | 0.5478 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **1130**, R² = **0.0832**, Adj R² = **0.0742**, F-statistic = **9.23** (p = **5.42e-16**), Residual SE = **16.653** on **1118** df, AIC = **9575.2**, BIC = **9635.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4550** | 4.4040 | ±8.8080 | **+11.911** | **1.04e-32** | *** |
| **Education: graduate level (vs college)** | **-2.7277** | 1.0672 | ±2.1343 | **-2.556** | **0.0106** | * |
| Education: high school or below (vs college) | +0.5189 | 1.9688 | ±3.9376 | +0.264 | 0.7921 |  |
| Site: UCSD (vs UAB) | +0.3807 | 1.3730 | ±2.7459 | +0.277 | 0.7816 |  |
| Site: UW (vs UAB) | -2.3471 | 1.2030 | ±2.4061 | -1.951 | 0.0511 | . |
| **Age (years)** | **-0.2442** | 0.0487 | ±0.0974 | **-5.016** | **5.28e-07** | *** |
| **BMI (kg/m2)** | **+0.4322** | 0.0855 | ±0.1710 | **+5.055** | **4.31e-07** | *** |
| Hypertension | -0.0961 | 1.1522 | ±2.3043 | -0.083 | 0.9335 |  |
| High cholesterol | -0.1501 | 1.0574 | ±2.1148 | -0.142 | 0.8871 |  |
| Kidney disease | +1.0402 | 2.2566 | ±4.5133 | +0.461 | 0.6448 |  |
| Circulatory disease | -0.2078 | 1.5615 | ±3.1230 | -0.133 | 0.8941 |  |
| Time 181-250, pooled (%) | +0.1195 | 0.0974 | ±0.1949 | +1.227 | 0.2199 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **1130**, R² = **0.0831**, Adj R² = **0.0740**, F-statistic = **9.21** (p = **5.99e-16**), Residual SE = **16.655** on **1118** df, AIC = **9575.5**, BIC = **9635.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4675** | 4.4036 | ±8.8072 | **+11.915** | **9.93e-33** | *** |
| **Education: graduate level (vs college)** | **-2.7276** | 1.0676 | ±2.1352 | **-2.555** | **0.0106** | * |
| Education: high school or below (vs college) | +0.5289 | 1.9681 | ±3.9362 | +0.269 | 0.7881 |  |
| Site: UCSD (vs UAB) | +0.3898 | 1.3735 | ±2.7469 | +0.284 | 0.7766 |  |
| Site: UW (vs UAB) | -2.3339 | 1.2029 | ±2.4057 | -1.940 | 0.0523 | . |
| **Age (years)** | **-0.2439** | 0.0487 | ±0.0974 | **-5.011** | **5.40e-07** | *** |
| **BMI (kg/m2)** | **+0.4320** | 0.0854 | ±0.1709 | **+5.057** | **4.26e-07** | *** |
| Hypertension | -0.0886 | 1.1519 | ±2.3038 | -0.077 | 0.9387 |  |
| High cholesterol | -0.1447 | 1.0574 | ±2.1149 | -0.137 | 0.8912 |  |
| Kidney disease | +1.0518 | 2.2573 | ±4.5145 | +0.466 | 0.6413 |  |
| Circulatory disease | -0.2106 | 1.5620 | ±3.1239 | -0.135 | 0.8927 |  |
| Avg. daily time 181-250 (%) | +0.1116 | 0.0957 | ±0.1915 | +1.165 | 0.2439 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **1130**, R² = **0.0838**, Adj R² = **0.0747**, F-statistic = **9.29** (p = **4.09e-16**), Residual SE = **16.649** on **1118** df, AIC = **9574.6**, BIC = **9635.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.3958** | 4.4080 | ±8.8161 | **+11.886** | **1.39e-32** | *** |
| **Education: graduate level (vs college)** | **-2.7152** | 1.0675 | ±2.1350 | **-2.544** | **0.0110** | * |
| Education: high school or below (vs college) | +0.4511 | 1.9565 | ±3.9129 | +0.231 | 0.8177 |  |
| Site: UCSD (vs UAB) | +0.3721 | 1.3755 | ±2.7510 | +0.271 | 0.7868 |  |
| Site: UW (vs UAB) | -2.3340 | 1.2016 | ±2.4032 | -1.942 | 0.0521 | . |
| **Age (years)** | **-0.2430** | 0.0487 | ±0.0973 | **-4.993** | **5.94e-07** | *** |
| **BMI (kg/m2)** | **+0.4324** | 0.0856 | ±0.1712 | **+5.053** | **4.36e-07** | *** |
| Hypertension | -0.0642 | 1.1510 | ±2.3019 | -0.056 | 0.9555 |  |
| High cholesterol | -0.1384 | 1.0605 | ±2.1209 | -0.131 | 0.8961 |  |
| Kidney disease | +1.0536 | 2.2669 | ±4.5337 | +0.465 | 0.6421 |  |
| Circulatory disease | -0.2535 | 1.5577 | ±3.1154 | -0.163 | 0.8707 |  |
| Time > 180 (%) | +0.0951 | 0.0831 | ±0.1661 | +1.145 | 0.2523 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **1130**, R² = **0.0836**, Adj R² = **0.0745**, F-statistic = **9.27** (p = **4.57e-16**), Residual SE = **16.651** on **1118** df, AIC = **9574.9**, BIC = **9635.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4197** | 4.4072 | ±8.8144 | **+11.894** | **1.27e-32** | *** |
| **Education: graduate level (vs college)** | **-2.7161** | 1.0677 | ±2.1354 | **-2.544** | **0.0110** | * |
| Education: high school or below (vs college) | +0.4653 | 1.9573 | ±3.9147 | +0.238 | 0.8121 |  |
| Site: UCSD (vs UAB) | +0.3800 | 1.3759 | ±2.7517 | +0.276 | 0.7824 |  |
| Site: UW (vs UAB) | -2.3263 | 1.2017 | ±2.4035 | -1.936 | 0.0529 | . |
| **Age (years)** | **-0.2429** | 0.0487 | ±0.0973 | **-4.991** | **6.00e-07** | *** |
| **BMI (kg/m2)** | **+0.4321** | 0.0855 | ±0.1710 | **+5.052** | **4.37e-07** | *** |
| Hypertension | -0.0596 | 1.1511 | ±2.3021 | -0.052 | 0.9587 |  |
| High cholesterol | -0.1349 | 1.0605 | ±2.1211 | -0.127 | 0.8987 |  |
| Kidney disease | +1.0638 | 2.2669 | ±4.5338 | +0.469 | 0.6389 |  |
| Circulatory disease | -0.2517 | 1.5584 | ±3.1168 | -0.162 | 0.8717 |  |
| Avg. daily time > 180 (%) | +0.0903 | 0.0824 | ±0.1649 | +1.095 | 0.2733 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **1130**, R² = **0.0816**, Adj R² = **0.0726**, F-statistic = **9.03** (p = **1.36e-15**), Residual SE = **16.668** on **1118** df, AIC = **9577.3**, BIC = **9637.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4937** | 4.4287 | ±8.8574 | **+11.853** | **2.08e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6721** | 1.0687 | ±2.1375 | **-2.500** | **0.0124** | * |
| Education: high school or below (vs college) | +0.5362 | 1.9768 | ±3.9535 | +0.271 | 0.7862 |  |
| Site: UCSD (vs UAB) | +0.3650 | 1.3741 | ±2.7481 | +0.266 | 0.7905 |  |
| Site: UW (vs UAB) | -2.2605 | 1.2052 | ±2.4104 | -1.876 | 0.0607 | . |
| **Age (years)** | **-0.2429** | 0.0488 | ±0.0976 | **-4.977** | **6.47e-07** | *** |
| **BMI (kg/m2)** | **+0.4349** | 0.0864 | ±0.1728 | **+5.034** | **4.81e-07** | *** |
| Hypertension | +0.0403 | 1.1517 | ±2.3033 | +0.035 | 0.9721 |  |
| High cholesterol | -0.0302 | 1.0628 | ±2.1256 | -0.028 | 0.9773 |  |
| Kidney disease | +1.2621 | 2.2627 | ±4.5254 | +0.558 | 0.5770 |  |
| Circulatory disease | -0.1764 | 1.5705 | ±3.1410 | -0.112 | 0.9106 |  |
| Nocturnal time > 180 (%) | +0.0041 | 0.0931 | ±0.1863 | +0.044 | 0.9651 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **1130**, R² = **0.0828**, Adj R² = **0.0738**, F-statistic = **9.18** (p = **6.90e-16**), Residual SE = **16.657** on **1118** df, AIC = **9575.8**, BIC = **9636.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.0525** | 4.4441 | ±8.8882 | **+11.713** | **1.10e-31** | *** |
| **Education: graduate level (vs college)** | **-2.6781** | 1.0665 | ±2.1329 | **-2.511** | **0.0120** | * |
| Education: high school or below (vs college) | +0.5320 | 1.9704 | ±3.9408 | +0.270 | 0.7872 |  |
| Site: UCSD (vs UAB) | +0.3623 | 1.3719 | ±2.7438 | +0.264 | 0.7917 |  |
| Site: UW (vs UAB) | -2.2913 | 1.2037 | ±2.4074 | -1.904 | 0.0570 | . |
| **Age (years)** | **-0.2431** | 0.0488 | ±0.0975 | **-4.985** | **6.19e-07** | *** |
| **BMI (kg/m2)** | **+0.4432** | 0.0863 | ±0.1725 | **+5.138** | **2.78e-07** | *** |
| Hypertension | -0.0552 | 1.1511 | ±2.3022 | -0.048 | 0.9618 |  |
| High cholesterol | -0.0784 | 1.0581 | ±2.1162 | -0.074 | 0.9409 |  |
| Kidney disease | +1.2058 | 2.2585 | ±4.5171 | +0.534 | 0.5934 |  |
| Circulatory disease | -0.1605 | 1.5647 | ±3.1294 | -0.103 | 0.9183 |  |
| Any reading > 250 during wear (0/1) | +1.5444 | 1.2728 | ±2.5456 | +1.213 | 0.2250 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **1130**, R² = **0.0828**, Adj R² = **0.0738**, F-statistic = **9.17** (p = **6.99e-16**), Residual SE = **16.657** on **1118** df, AIC = **9575.8**, BIC = **9636.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.3968** | 4.4249 | ±8.8499 | **+11.841** | **2.39e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6709** | 1.0709 | ±2.1417 | **-2.494** | **0.0126** | * |
| Education: high school or below (vs college) | +0.4370 | 1.9638 | ±3.9277 | +0.223 | 0.8239 |  |
| Site: UCSD (vs UAB) | +0.3572 | 1.3785 | ±2.7571 | +0.259 | 0.7955 |  |
| Site: UW (vs UAB) | -2.2655 | 1.2014 | ±2.4029 | -1.886 | 0.0593 | . |
| **Age (years)** | **-0.2416** | 0.0488 | ±0.0976 | **-4.950** | **7.41e-07** | *** |
| **BMI (kg/m2)** | **+0.4348** | 0.0857 | ±0.1715 | **+5.072** | **3.94e-07** | *** |
| Hypertension | +0.0474 | 1.1528 | ±2.3057 | +0.041 | 0.9672 |  |
| High cholesterol | -0.0442 | 1.0611 | ±2.1222 | -0.042 | 0.9668 |  |
| Kidney disease | +1.2176 | 2.2702 | ±4.5404 | +0.536 | 0.5917 |  |
| Circulatory disease | -0.2497 | 1.5659 | ±3.1317 | -0.159 | 0.8733 |  |
| Time > 250 (%) | +0.1345 | 0.2143 | ±0.4287 | +0.628 | 0.5303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 1,130)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **1130**, R² = **0.0828**, Adj R² = **0.0737**, F-statistic = **9.17** (p = **7.13e-16**), Residual SE = **16.658** on **1118** df, AIC = **9575.8**, BIC = **9636.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.4116** | 4.4245 | ±8.8491 | **+11.846** | **2.27e-32** | *** |
| **Education: graduate level (vs college)** | **-2.6711** | 1.0710 | ±2.1419 | **-2.494** | **0.0126** | * |
| Education: high school or below (vs college) | +0.4392 | 1.9641 | ±3.9282 | +0.224 | 0.8230 |  |
| Site: UCSD (vs UAB) | +0.3572 | 1.3786 | ±2.7571 | +0.259 | 0.7956 |  |
| Site: UW (vs UAB) | -2.2685 | 1.2017 | ±2.4034 | -1.888 | 0.0591 | . |
| **Age (years)** | **-0.2417** | 0.0488 | ±0.0976 | **-4.952** | **7.36e-07** | *** |
| **BMI (kg/m2)** | **+0.4345** | 0.0857 | ±0.1715 | **+5.068** | **4.02e-07** | *** |
| Hypertension | +0.0483 | 1.1531 | ±2.3062 | +0.042 | 0.9666 |  |
| High cholesterol | -0.0444 | 1.0613 | ±2.1225 | -0.042 | 0.9666 |  |
| Kidney disease | +1.2203 | 2.2700 | ±4.5399 | +0.538 | 0.5909 |  |
| Circulatory disease | -0.2483 | 1.5658 | ±3.1315 | -0.159 | 0.8740 |  |
| Avg. daily time > 250 (%) | +0.1372 | 0.2230 | ±0.4459 | +0.615 | 0.5384 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
