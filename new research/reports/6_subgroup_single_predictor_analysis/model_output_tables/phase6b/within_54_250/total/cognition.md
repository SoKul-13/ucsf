# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Total analysis base - Cognition

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 890; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **890**, R² = **0.1216**, Adj R² = **0.1116**, F-statistic = **12.17** (p = **6.66e-20**), Residual SE = **2.723** on **879** df, AIC = **4319.5**, BIC = **4372.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.9213** | 0.7721 | ±1.5443 | **+38.751** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8286** | 0.1881 | ±0.3761 | **+4.406** | **1.05e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5733** | 0.4222 | ±0.8445 | **-3.726** | **1.94e-04** | *** |
| Site: UCSD (vs UAB) | -0.4059 | 0.2545 | ±0.5089 | -1.595 | 0.1106 |  |
| Site: UW (vs UAB) | -0.0738 | 0.2498 | ±0.4996 | -0.295 | 0.7676 |  |
| **Age (years)** | **-0.0464** | 0.0092 | ±0.0184 | **-5.047** | **4.48e-07** | *** |
| **BMI (kg/m2)** | **-0.0382** | 0.0143 | ±0.0286 | **-2.669** | **0.0076** | ** |
| Hypertension | -0.3390 | 0.2050 | ±0.4099 | -1.654 | 0.0981 | . |
| High cholesterol | +0.1445 | 0.1945 | ±0.3889 | +0.743 | 0.4576 |  |
| Kidney disease | -0.1494 | 0.3597 | ±0.7194 | -0.415 | 0.6779 |  |
| Circulatory disease | -0.2944 | 0.3142 | ±0.6284 | -0.937 | 0.3488 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **890**, R² = **0.1299**, Adj R² = **0.1190**, F-statistic = **11.91** (p = **5.08e-21**), Residual SE = **2.711** on **878** df, AIC = **4313.1**, BIC = **4370.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.2883** | 1.5422 | ±3.0844 | **+21.585** | **2.49e-103** | *** |
| **Education: graduate level (vs college)** | **+0.8295** | 0.1876 | ±0.3752 | **+4.422** | **9.77e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5359** | 0.4186 | ±0.8372 | **-3.669** | **2.43e-04** | *** |
| Site: UCSD (vs UAB) | -0.4170 | 0.2532 | ±0.5064 | -1.647 | 0.0996 | . |
| Site: UW (vs UAB) | -0.0854 | 0.2505 | ±0.5010 | -0.341 | 0.7331 |  |
| **Age (years)** | **-0.0451** | 0.0091 | ±0.0182 | **-4.947** | **7.55e-07** | *** |
| **BMI (kg/m2)** | **-0.0306** | 0.0141 | ±0.0282 | **-2.170** | **0.0300** | * |
| Hypertension | -0.2587 | 0.2066 | ±0.4133 | -1.252 | 0.2106 |  |
| High cholesterol | +0.2206 | 0.1928 | ±0.3856 | +1.144 | 0.2526 |  |
| Kidney disease | -0.1598 | 0.3519 | ±0.7037 | -0.454 | 0.6497 |  |
| Circulatory disease | -0.2494 | 0.3149 | ±0.6297 | -0.792 | 0.4283 |  |
| **HbA1c (%)** | **-0.6580** | 0.2442 | ±0.4884 | **-2.694** | **0.0071** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **890**, R² = **0.1377**, Adj R² = **0.1269**, F-statistic = **12.75** (p = **1.22e-22**), Residual SE = **2.699** on **878** df, AIC = **4305.0**, BIC = **4362.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.3749** | 1.1997 | ±2.3995 | **+27.819** | **2.58e-170** | *** |
| **Education: graduate level (vs college)** | **+0.8598** | 0.1863 | ±0.3727 | **+4.614** | **3.95e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5566** | 0.4159 | ±0.8319 | **-3.742** | **1.82e-04** | *** |
| Site: UCSD (vs UAB) | -0.4441 | 0.2502 | ±0.5003 | -1.775 | 0.0759 | . |
| Site: UW (vs UAB) | -0.0479 | 0.2469 | ±0.4937 | -0.194 | 0.8463 |  |
| **Age (years)** | **-0.0456** | 0.0091 | ±0.0182 | **-5.023** | **5.08e-07** | *** |
| **BMI (kg/m2)** | **-0.0311** | 0.0143 | ±0.0287 | **-2.169** | **0.0301** | * |
| Hypertension | -0.2485 | 0.2071 | ±0.4141 | -1.200 | 0.2301 |  |
| High cholesterol | +0.1588 | 0.1940 | ±0.3880 | +0.819 | 0.4131 |  |
| Kidney disease | -0.0660 | 0.3544 | ±0.7088 | -0.186 | 0.8523 |  |
| Circulatory disease | -0.2247 | 0.3101 | ±0.6202 | -0.725 | 0.4687 |  |
| **Mean glucose (mg/dL)** | **-0.0313** | 0.0087 | ±0.0174 | **-3.603** | **3.14e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **890**, R² = **0.1377**, Adj R² = **0.1269**, F-statistic = **12.75** (p = **1.22e-22**), Residual SE = **2.699** on **878** df, AIC = **4305.0**, BIC = **4362.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+37.7007** | 2.2599 | ±4.5198 | **+16.683** | **1.76e-62** | *** |
| **Education: graduate level (vs college)** | **+0.8598** | 0.1863 | ±0.3727 | **+4.614** | **3.95e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5566** | 0.4159 | ±0.8319 | **-3.742** | **1.82e-04** | *** |
| Site: UCSD (vs UAB) | -0.4441 | 0.2502 | ±0.5003 | -1.775 | 0.0759 | . |
| Site: UW (vs UAB) | -0.0479 | 0.2469 | ±0.4937 | -0.194 | 0.8463 |  |
| **Age (years)** | **-0.0456** | 0.0091 | ±0.0182 | **-5.023** | **5.08e-07** | *** |
| **BMI (kg/m2)** | **-0.0311** | 0.0143 | ±0.0287 | **-2.169** | **0.0301** | * |
| Hypertension | -0.2485 | 0.2071 | ±0.4141 | -1.200 | 0.2301 |  |
| High cholesterol | +0.1588 | 0.1940 | ±0.3880 | +0.819 | 0.4131 |  |
| Kidney disease | -0.0660 | 0.3544 | ±0.7088 | -0.186 | 0.8523 |  |
| Circulatory disease | -0.2247 | 0.3101 | ±0.6202 | -0.725 | 0.4687 |  |
| **GMI (%)** | **-1.3069** | 0.3627 | ±0.7254 | **-3.603** | **3.14e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **890**, R² = **0.1366**, Adj R² = **0.1257**, F-statistic = **12.62** (p = **2.13e-22**), Residual SE = **2.701** on **878** df, AIC = **4306.3**, BIC = **4363.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.8875** | 1.1000 | ±2.2001 | **+29.896** | **2.19e-196** | *** |
| **Education: graduate level (vs college)** | **+0.8521** | 0.1872 | ±0.3743 | **+4.552** | **5.30e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5589** | 0.4135 | ±0.8270 | **-3.770** | **1.63e-04** | *** |
| Site: UCSD (vs UAB) | -0.4082 | 0.2512 | ±0.5025 | -1.625 | 0.1042 |  |
| Site: UW (vs UAB) | -0.0406 | 0.2476 | ±0.4952 | -0.164 | 0.8696 |  |
| **Age (years)** | **-0.0484** | 0.0091 | ±0.0183 | **-5.295** | **1.19e-07** | *** |
| BMI (kg/m2) | -0.0265 | 0.0147 | ±0.0294 | -1.805 | 0.0711 | . |
| Hypertension | -0.2839 | 0.2056 | ±0.4111 | -1.381 | 0.1672 |  |
| High cholesterol | +0.1868 | 0.1947 | ±0.3895 | +0.959 | 0.3374 |  |
| Kidney disease | -0.1179 | 0.3564 | ±0.7128 | -0.331 | 0.7409 |  |
| Circulatory disease | -0.2302 | 0.3081 | ±0.6162 | -0.747 | 0.4549 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0270** | 0.0077 | ±0.0154 | **-3.515** | **4.40e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **890**, R² = **0.1263**, Adj R² = **0.1154**, F-statistic = **11.54** (p = **2.64e-20**), Residual SE = **2.717** on **878** df, AIC = **4316.7**, BIC = **4374.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.7575** | 0.8814 | ±1.7629 | **+34.895** | **8.84e-267** | *** |
| **Education: graduate level (vs college)** | **+0.8204** | 0.1884 | ±0.3767 | **+4.355** | **1.33e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5229** | 0.4183 | ±0.8366 | **-3.641** | **2.72e-04** | *** |
| Site: UCSD (vs UAB) | -0.4422 | 0.2545 | ±0.5090 | -1.738 | 0.0823 | . |
| Site: UW (vs UAB) | -0.0818 | 0.2503 | ±0.5005 | -0.327 | 0.7438 |  |
| **Age (years)** | **-0.0451** | 0.0092 | ±0.0184 | **-4.918** | **8.76e-07** | *** |
| **BMI (kg/m2)** | **-0.0365** | 0.0144 | ±0.0288 | **-2.536** | **0.0112** | * |
| Hypertension | -0.2825 | 0.2075 | ±0.4150 | -1.361 | 0.1734 |  |
| High cholesterol | +0.1536 | 0.1944 | ±0.3888 | +0.790 | 0.4295 |  |
| Kidney disease | -0.0941 | 0.3579 | ±0.7159 | -0.263 | 0.7927 |  |
| Circulatory disease | -0.2738 | 0.3123 | ±0.6246 | -0.877 | 0.3807 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.0497** | 0.0238 | ±0.0476 | **-2.087** | **0.0369** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **890**, R² = **0.1260**, Adj R² = **0.1150**, F-statistic = **11.50** (p = **3.15e-20**), Residual SE = **2.717** on **878** df, AIC = **4317.1**, BIC = **4374.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.6522** | 0.8667 | ±1.7335 | **+35.365** | **5.86e-274** | *** |
| **Education: graduate level (vs college)** | **+0.8255** | 0.1883 | ±0.3766 | **+4.384** | **1.17e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5315** | 0.4195 | ±0.8390 | **-3.651** | **2.62e-04** | *** |
| Site: UCSD (vs UAB) | -0.4381 | 0.2547 | ±0.5095 | -1.720 | 0.0854 | . |
| Site: UW (vs UAB) | -0.0772 | 0.2502 | ±0.5004 | -0.309 | 0.7576 |  |
| **Age (years)** | **-0.0452** | 0.0092 | ±0.0183 | **-4.924** | **8.47e-07** | *** |
| **BMI (kg/m2)** | **-0.0364** | 0.0144 | ±0.0288 | **-2.530** | **0.0114** | * |
| Hypertension | -0.2833 | 0.2079 | ±0.4159 | -1.362 | 0.1731 |  |
| High cholesterol | +0.1494 | 0.1944 | ±0.3889 | +0.768 | 0.4424 |  |
| Kidney disease | -0.1014 | 0.3570 | ±0.7141 | -0.284 | 0.7765 |  |
| Circulatory disease | -0.2812 | 0.3119 | ±0.6238 | -0.902 | 0.3672 |  |
| **Avg. daily SD (mg/dL)** | **-0.0484** | 0.0240 | ±0.0479 | **-2.020** | **0.0434** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **890**, R² = **0.1217**, Adj R² = **0.1107**, F-statistic = **11.06** (p = **2.26e-19**), Residual SE = **2.724** on **878** df, AIC = **4321.4**, BIC = **4378.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.1030** | 0.9653 | ±1.9305 | **+31.186** | **1.65e-213** | *** |
| **Education: graduate level (vs college)** | **+0.8250** | 0.1881 | ±0.3762 | **+4.386** | **1.16e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5646** | 0.4229 | ±0.8458 | **-3.700** | **2.16e-04** | *** |
| Site: UCSD (vs UAB) | -0.4112 | 0.2562 | ±0.5124 | -1.605 | 0.1084 |  |
| Site: UW (vs UAB) | -0.0765 | 0.2511 | ±0.5023 | -0.305 | 0.7607 |  |
| **Age (years)** | **-0.0462** | 0.0092 | ±0.0184 | **-5.012** | **5.39e-07** | *** |
| **BMI (kg/m2)** | **-0.0382** | 0.0143 | ±0.0287 | **-2.663** | **0.0077** | ** |
| Hypertension | -0.3324 | 0.2065 | ±0.4130 | -1.609 | 0.1075 |  |
| High cholesterol | +0.1451 | 0.1946 | ±0.3892 | +0.746 | 0.4557 |  |
| Kidney disease | -0.1427 | 0.3604 | ±0.7208 | -0.396 | 0.6920 |  |
| Circulatory disease | -0.2942 | 0.3143 | ±0.6285 | -0.936 | 0.3492 |  |
| CV (%) | -0.0118 | 0.0347 | ±0.0693 | -0.341 | 0.7332 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **890**, R² = **0.1216**, Adj R² = **0.1106**, F-statistic = **11.05** (p = **2.40e-19**), Residual SE = **2.724** on **878** df, AIC = **4321.5**, BIC = **4379.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.9186** | 0.9426 | ±1.8852 | **+31.740** | **4.40e-221** | *** |
| **Education: graduate level (vs college)** | **+0.8285** | 0.1876 | ±0.3753 | **+4.415** | **1.01e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5732** | 0.4233 | ±0.8467 | **-3.716** | **2.02e-04** | *** |
| Site: UCSD (vs UAB) | -0.4060 | 0.2559 | ±0.5118 | -1.587 | 0.1126 |  |
| Site: UW (vs UAB) | -0.0738 | 0.2506 | ±0.5013 | -0.295 | 0.7684 |  |
| **Age (years)** | **-0.0464** | 0.0092 | ±0.0184 | **-5.035** | **4.78e-07** | *** |
| **BMI (kg/m2)** | **-0.0382** | 0.0143 | ±0.0286 | **-2.665** | **0.0077** | ** |
| Hypertension | -0.3389 | 0.2062 | ±0.4124 | -1.644 | 0.1003 |  |
| High cholesterol | +0.1445 | 0.1946 | ±0.3893 | +0.742 | 0.4579 |  |
| Kidney disease | -0.1493 | 0.3602 | ±0.7204 | -0.415 | 0.6785 |  |
| Circulatory disease | -0.2944 | 0.3145 | ±0.6290 | -0.936 | 0.3493 |  |
| Mean / SD ratio | +0.0004 | 0.0885 | ±0.1771 | +0.005 | 0.9963 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **890**, R² = **0.1216**, Adj R² = **0.1106**, F-statistic = **11.05** (p = **2.35e-19**), Residual SE = **2.724** on **878** df, AIC = **4321.5**, BIC = **4379.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.8142** | 0.9101 | ±1.8203 | **+32.758** | **2.35e-235** | *** |
| **Education: graduate level (vs college)** | **+0.8266** | 0.1881 | ±0.3762 | **+4.395** | **1.11e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5695** | 0.4229 | ±0.8458 | **-3.711** | **2.06e-04** | *** |
| Site: UCSD (vs UAB) | -0.4077 | 0.2557 | ±0.5114 | -1.595 | 0.1108 |  |
| Site: UW (vs UAB) | -0.0740 | 0.2503 | ±0.5006 | -0.295 | 0.7677 |  |
| **Age (years)** | **-0.0463** | 0.0092 | ±0.0184 | **-5.025** | **5.04e-07** | *** |
| **BMI (kg/m2)** | **-0.0381** | 0.0143 | ±0.0286 | **-2.661** | **0.0078** | ** |
| Hypertension | -0.3356 | 0.2060 | ±0.4121 | -1.629 | 0.1034 |  |
| High cholesterol | +0.1443 | 0.1947 | ±0.3895 | +0.741 | 0.4586 |  |
| Kidney disease | -0.1459 | 0.3598 | ±0.7195 | -0.405 | 0.6852 |  |
| Circulatory disease | -0.2960 | 0.3143 | ±0.6286 | -0.942 | 0.3464 |  |
| Avg. daily mean/SD | +0.0136 | 0.0680 | ±0.1359 | +0.200 | 0.8414 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **890**, R² = **0.1221**, Adj R² = **0.1111**, F-statistic = **11.10** (p = **1.93e-19**), Residual SE = **2.724** on **878** df, AIC = **4321.1**, BIC = **4378.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.2696** | 0.9014 | ±1.8029 | **+33.579** | **3.42e-247** | *** |
| **Education: graduate level (vs college)** | **+0.8290** | 0.1882 | ±0.3763 | **+4.406** | **1.05e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5570** | 0.4206 | ±0.8412 | **-3.702** | **2.14e-04** | *** |
| Site: UCSD (vs UAB) | -0.4095 | 0.2545 | ±0.5089 | -1.609 | 0.1076 |  |
| Site: UW (vs UAB) | -0.0779 | 0.2500 | ±0.5000 | -0.312 | 0.7554 |  |
| **Age (years)** | **-0.0466** | 0.0092 | ±0.0184 | **-5.062** | **4.15e-07** | *** |
| **BMI (kg/m2)** | **-0.0382** | 0.0143 | ±0.0286 | **-2.666** | **0.0077** | ** |
| Hypertension | -0.3419 | 0.2049 | ±0.4099 | -1.669 | 0.0952 | . |
| High cholesterol | +0.1452 | 0.1947 | ±0.3894 | +0.746 | 0.4556 |  |
| Kidney disease | -0.1424 | 0.3617 | ±0.7233 | -0.394 | 0.6938 |  |
| Circulatory disease | -0.2986 | 0.3139 | ±0.6279 | -0.951 | 0.3415 |  |
| MAG (mg/dL/h) | -0.0094 | 0.0128 | ±0.0255 | -0.738 | 0.4606 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **890**, R² = **0.1245**, Adj R² = **0.1135**, F-statistic = **11.35** (p = **6.20e-20**), Residual SE = **2.720** on **878** df, AIC = **4318.6**, BIC = **4376.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.7180** | 0.9159 | ±1.8318 | **+33.539** | **1.31e-246** | *** |
| **Education: graduate level (vs college)** | **+0.8313** | 0.1885 | ±0.3770 | **+4.411** | **1.03e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5369** | 0.4188 | ±0.8376 | **-3.670** | **2.43e-04** | *** |
| Site: UCSD (vs UAB) | -0.4260 | 0.2548 | ±0.5097 | -1.672 | 0.0946 | . |
| Site: UW (vs UAB) | -0.0752 | 0.2499 | ±0.4998 | -0.301 | 0.7634 |  |
| **Age (years)** | **-0.0455** | 0.0092 | ±0.0183 | **-4.965** | **6.89e-07** | *** |
| **BMI (kg/m2)** | **-0.0388** | 0.0144 | ±0.0288 | **-2.699** | **0.0070** | ** |
| Hypertension | -0.3096 | 0.2070 | ±0.4140 | -1.496 | 0.1347 |  |
| High cholesterol | +0.1454 | 0.1946 | ±0.3892 | +0.747 | 0.4549 |  |
| Kidney disease | -0.1165 | 0.3577 | ±0.7155 | -0.326 | 0.7447 |  |
| Circulatory disease | -0.2842 | 0.3127 | ±0.6254 | -0.909 | 0.3634 |  |
| Avg. daily range (mg/dL) | -0.0093 | 0.0055 | ±0.0110 | -1.701 | 0.0889 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **890**, R² = **0.1254**, Adj R² = **0.1145**, F-statistic = **11.45** (p = **4.03e-20**), Residual SE = **2.718** on **878** df, AIC = **4317.7**, BIC = **4375.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.3018** | 0.7931 | ±1.5862 | **+38.207** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8275** | 0.1883 | ±0.3765 | **+4.395** | **1.11e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5307** | 0.4185 | ±0.8370 | **-3.658** | **2.54e-04** | *** |
| Site: UCSD (vs UAB) | -0.4302 | 0.2530 | ±0.5060 | -1.701 | 0.0890 | . |
| Site: UW (vs UAB) | -0.0858 | 0.2498 | ±0.4996 | -0.344 | 0.7311 |  |
| **Age (years)** | **-0.0465** | 0.0092 | ±0.0183 | **-5.070** | **3.98e-07** | *** |
| **BMI (kg/m2)** | **-0.0356** | 0.0144 | ±0.0289 | **-2.466** | **0.0137** | * |
| Hypertension | -0.3411 | 0.2047 | ±0.4094 | -1.666 | 0.0956 | . |
| High cholesterol | +0.1771 | 0.1939 | ±0.3878 | +0.913 | 0.3610 |  |
| Kidney disease | -0.1251 | 0.3567 | ±0.7135 | -0.351 | 0.7258 |  |
| Circulatory disease | -0.2501 | 0.3159 | ±0.6317 | -0.792 | 0.4285 |  |
| SD of daily means (mg/dL) | -0.0776 | 0.0406 | ±0.0811 | -1.913 | 0.0558 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **890**, R² = **0.1275**, Adj R² = **0.1166**, F-statistic = **11.67** (p = **1.52e-20**), Residual SE = **2.715** on **878** df, AIC = **4315.5**, BIC = **4373.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.2195** | 3.4224 | ±6.8448 | **+6.785** | **1.16e-11** | *** |
| **Education: graduate level (vs college)** | **+0.8361** | 0.1878 | ±0.3756 | **+4.452** | **8.49e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5494** | 0.4191 | ±0.8381 | **-3.697** | **2.18e-04** | *** |
| Site: UCSD (vs UAB) | -0.4453 | 0.2520 | ±0.5040 | -1.767 | 0.0772 | . |
| Site: UW (vs UAB) | -0.0839 | 0.2484 | ±0.4969 | -0.338 | 0.7354 |  |
| **Age (years)** | **-0.0454** | 0.0092 | ±0.0184 | **-4.941** | **7.79e-07** | *** |
| **BMI (kg/m2)** | **-0.0360** | 0.0145 | ±0.0289 | **-2.487** | **0.0129** | * |
| Hypertension | -0.3049 | 0.2065 | ±0.4130 | -1.476 | 0.1398 |  |
| High cholesterol | +0.1681 | 0.1955 | ±0.3910 | +0.860 | 0.3900 |  |
| Kidney disease | -0.0830 | 0.3573 | ±0.7146 | -0.232 | 0.8163 |  |
| Circulatory disease | -0.2490 | 0.3144 | ±0.6288 | -0.792 | 0.4284 |  |
| **Time in range 70-180, pooled (%)** | **+0.0671** | 0.0331 | ±0.0662 | **+2.027** | **0.0427** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **890**, R² = **0.1274**, Adj R² = **0.1165**, F-statistic = **11.65** (p = **1.61e-20**), Residual SE = **2.715** on **878** df, AIC = **4315.7**, BIC = **4373.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.1419** | 3.4593 | ±6.9185 | **+6.690** | **2.23e-11** | *** |
| **Education: graduate level (vs college)** | **+0.8350** | 0.1878 | ±0.3756 | **+4.446** | **8.74e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5566** | 0.4196 | ±0.8391 | **-3.710** | **2.07e-04** | *** |
| Site: UCSD (vs UAB) | -0.4455 | 0.2519 | ±0.5039 | -1.768 | 0.0770 | . |
| Site: UW (vs UAB) | -0.0837 | 0.2486 | ±0.4972 | -0.337 | 0.7364 |  |
| **Age (years)** | **-0.0454** | 0.0092 | ±0.0184 | **-4.951** | **7.37e-07** | *** |
| **BMI (kg/m2)** | **-0.0359** | 0.0145 | ±0.0290 | **-2.475** | **0.0133** | * |
| Hypertension | -0.3054 | 0.2064 | ±0.4128 | -1.480 | 0.1389 |  |
| High cholesterol | +0.1684 | 0.1955 | ±0.3911 | +0.861 | 0.3891 |  |
| Kidney disease | -0.0802 | 0.3562 | ±0.7124 | -0.225 | 0.8218 |  |
| Circulatory disease | -0.2468 | 0.3147 | ±0.6295 | -0.784 | 0.4329 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.0679** | 0.0334 | ±0.0667 | **+2.033** | **0.0420** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **890**, R² = **0.1232**, Adj R² = **0.1122**, F-statistic = **11.22** (p = **1.13e-19**), Residual SE = **2.722** on **878** df, AIC = **4319.9**, BIC = **4377.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.8569** | 0.7731 | ±1.5462 | **+38.621** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8479** | 0.1884 | ±0.3769 | **+4.500** | **6.81e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5556** | 0.4227 | ±0.8454 | **-3.680** | **2.33e-04** | *** |
| Site: UCSD (vs UAB) | -0.4139 | 0.2544 | ±0.5087 | -1.627 | 0.1037 |  |
| Site: UW (vs UAB) | -0.0685 | 0.2499 | ±0.4997 | -0.274 | 0.7838 |  |
| **Age (years)** | **-0.0465** | 0.0092 | ±0.0184 | **-5.060** | **4.18e-07** | *** |
| **BMI (kg/m2)** | **-0.0377** | 0.0143 | ±0.0285 | **-2.642** | **0.0083** | ** |
| Hypertension | -0.3355 | 0.2052 | ±0.4105 | -1.635 | 0.1021 |  |
| High cholesterol | +0.1374 | 0.1945 | ±0.3890 | +0.707 | 0.4798 |  |
| Kidney disease | -0.1403 | 0.3602 | ±0.7203 | -0.389 | 0.6969 |  |
| Circulatory disease | -0.2877 | 0.3133 | ±0.6267 | -0.918 | 0.3585 |  |
| Time 54-69, pooled (%) | +0.2444 | 0.1553 | ±0.3107 | +1.573 | 0.1157 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **890**, R² = **0.1229**, Adj R² = **0.1119**, F-statistic = **11.18** (p = **1.33e-19**), Residual SE = **2.722** on **878** df, AIC = **4320.3**, BIC = **4377.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.8725** | 0.7723 | ±1.5446 | **+38.681** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8464** | 0.1884 | ±0.3769 | **+4.492** | **7.07e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5558** | 0.4225 | ±0.8450 | **-3.683** | **2.31e-04** | *** |
| Site: UCSD (vs UAB) | -0.4177 | 0.2543 | ±0.5087 | -1.642 | 0.1005 |  |
| Site: UW (vs UAB) | -0.0708 | 0.2499 | ±0.4997 | -0.283 | 0.7769 |  |
| **Age (years)** | **-0.0466** | 0.0092 | ±0.0184 | **-5.064** | **4.10e-07** | *** |
| **BMI (kg/m2)** | **-0.0377** | 0.0143 | ±0.0286 | **-2.644** | **0.0082** | ** |
| Hypertension | -0.3359 | 0.2053 | ±0.4106 | -1.636 | 0.1018 |  |
| High cholesterol | +0.1389 | 0.1945 | ±0.3889 | +0.714 | 0.4749 |  |
| Kidney disease | -0.1409 | 0.3603 | ±0.7207 | -0.391 | 0.6957 |  |
| Circulatory disease | -0.2852 | 0.3133 | ±0.6266 | -0.910 | 0.3627 |  |
| Avg. daily time 54-69 (%) | +0.2093 | 0.1504 | ±0.3009 | +1.391 | 0.1642 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **890**, R² = **0.1232**, Adj R² = **0.1122**, F-statistic = **11.22** (p = **1.13e-19**), Residual SE = **2.722** on **878** df, AIC = **4319.9**, BIC = **4377.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.8569** | 0.7731 | ±1.5462 | **+38.621** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8479** | 0.1884 | ±0.3769 | **+4.500** | **6.81e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5556** | 0.4227 | ±0.8454 | **-3.680** | **2.33e-04** | *** |
| Site: UCSD (vs UAB) | -0.4139 | 0.2544 | ±0.5087 | -1.627 | 0.1037 |  |
| Site: UW (vs UAB) | -0.0685 | 0.2499 | ±0.4997 | -0.274 | 0.7838 |  |
| **Age (years)** | **-0.0465** | 0.0092 | ±0.0184 | **-5.060** | **4.18e-07** | *** |
| **BMI (kg/m2)** | **-0.0377** | 0.0143 | ±0.0285 | **-2.642** | **0.0083** | ** |
| Hypertension | -0.3355 | 0.2052 | ±0.4105 | -1.635 | 0.1021 |  |
| High cholesterol | +0.1374 | 0.1945 | ±0.3890 | +0.707 | 0.4798 |  |
| Kidney disease | -0.1403 | 0.3602 | ±0.7203 | -0.389 | 0.6969 |  |
| Circulatory disease | -0.2877 | 0.3133 | ±0.6267 | -0.918 | 0.3585 |  |
| Time < 70 (%) | +0.2444 | 0.1553 | ±0.3107 | +1.573 | 0.1157 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **890**, R² = **0.1229**, Adj R² = **0.1119**, F-statistic = **11.18** (p = **1.33e-19**), Residual SE = **2.722** on **878** df, AIC = **4320.3**, BIC = **4377.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.8725** | 0.7723 | ±1.5446 | **+38.681** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8464** | 0.1884 | ±0.3769 | **+4.492** | **7.07e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5558** | 0.4225 | ±0.8450 | **-3.683** | **2.31e-04** | *** |
| Site: UCSD (vs UAB) | -0.4177 | 0.2543 | ±0.5087 | -1.642 | 0.1005 |  |
| Site: UW (vs UAB) | -0.0708 | 0.2499 | ±0.4997 | -0.283 | 0.7769 |  |
| **Age (years)** | **-0.0466** | 0.0092 | ±0.0184 | **-5.064** | **4.10e-07** | *** |
| **BMI (kg/m2)** | **-0.0377** | 0.0143 | ±0.0286 | **-2.644** | **0.0082** | ** |
| Hypertension | -0.3359 | 0.2053 | ±0.4106 | -1.636 | 0.1018 |  |
| High cholesterol | +0.1389 | 0.1945 | ±0.3889 | +0.714 | 0.4749 |  |
| Kidney disease | -0.1409 | 0.3603 | ±0.7207 | -0.391 | 0.6957 |  |
| Circulatory disease | -0.2852 | 0.3133 | ±0.6266 | -0.910 | 0.3627 |  |
| Avg. daily time < 70 (%) | +0.2093 | 0.1504 | ±0.3009 | +1.391 | 0.1642 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **890**, R² = **0.1283**, Adj R² = **0.1174**, F-statistic = **11.75** (p = **1.04e-20**), Residual SE = **2.714** on **878** df, AIC = **4314.7**, BIC = **4372.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.9120** | 0.7723 | ±1.5445 | **+38.733** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8422** | 0.1876 | ±0.3752 | **+4.490** | **7.14e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5429** | 0.4190 | ±0.8380 | **-3.682** | **2.31e-04** | *** |
| Site: UCSD (vs UAB) | -0.4499 | 0.2518 | ±0.5037 | -1.787 | 0.0740 | . |
| Site: UW (vs UAB) | -0.0830 | 0.2484 | ±0.4967 | -0.334 | 0.7382 |  |
| **Age (years)** | **-0.0453** | 0.0092 | ±0.0184 | **-4.940** | **7.81e-07** | *** |
| **BMI (kg/m2)** | **-0.0357** | 0.0145 | ±0.0289 | **-2.470** | **0.0135** | * |
| Hypertension | -0.3019 | 0.2066 | ±0.4132 | -1.462 | 0.1438 |  |
| High cholesterol | +0.1674 | 0.1954 | ±0.3907 | +0.857 | 0.3916 |  |
| Kidney disease | -0.0766 | 0.3574 | ±0.7147 | -0.214 | 0.8304 |  |
| Circulatory disease | -0.2445 | 0.3141 | ±0.6282 | -0.778 | 0.4364 |  |
| **Time 181-250, pooled (%)** | **-0.0710** | 0.0329 | ±0.0658 | **-2.156** | **0.0311** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **890**, R² = **0.1281**, Adj R² = **0.1172**, F-statistic = **11.73** (p = **1.14e-20**), Residual SE = **2.714** on **878** df, AIC = **4314.9**, BIC = **4372.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.9109** | 0.7724 | ±1.5448 | **+38.725** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8414** | 0.1876 | ±0.3751 | **+4.486** | **7.26e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5497** | 0.4195 | ±0.8390 | **-3.694** | **2.21e-04** | *** |
| Site: UCSD (vs UAB) | -0.4516 | 0.2517 | ±0.5034 | -1.794 | 0.0728 | . |
| Site: UW (vs UAB) | -0.0832 | 0.2485 | ±0.4971 | -0.335 | 0.7379 |  |
| **Age (years)** | **-0.0454** | 0.0092 | ±0.0183 | **-4.955** | **7.23e-07** | *** |
| **BMI (kg/m2)** | **-0.0356** | 0.0145 | ±0.0290 | **-2.457** | **0.0140** | * |
| Hypertension | -0.3026 | 0.2065 | ±0.4129 | -1.466 | 0.1428 |  |
| High cholesterol | +0.1678 | 0.1954 | ±0.3909 | +0.859 | 0.3906 |  |
| Kidney disease | -0.0737 | 0.3563 | ±0.7126 | -0.207 | 0.8361 |  |
| Circulatory disease | -0.2412 | 0.3144 | ±0.6289 | -0.767 | 0.4431 |  |
| **Avg. daily time 181-250 (%)** | **-0.0714** | 0.0331 | ±0.0662 | **-2.157** | **0.0310** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **890**, R² = **0.1283**, Adj R² = **0.1174**, F-statistic = **11.75** (p = **1.04e-20**), Residual SE = **2.714** on **878** df, AIC = **4314.7**, BIC = **4372.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.9120** | 0.7723 | ±1.5445 | **+38.733** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8422** | 0.1876 | ±0.3752 | **+4.490** | **7.14e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5429** | 0.4190 | ±0.8380 | **-3.682** | **2.31e-04** | *** |
| Site: UCSD (vs UAB) | -0.4499 | 0.2518 | ±0.5037 | -1.787 | 0.0740 | . |
| Site: UW (vs UAB) | -0.0830 | 0.2484 | ±0.4967 | -0.334 | 0.7382 |  |
| **Age (years)** | **-0.0453** | 0.0092 | ±0.0184 | **-4.940** | **7.81e-07** | *** |
| **BMI (kg/m2)** | **-0.0357** | 0.0145 | ±0.0289 | **-2.470** | **0.0135** | * |
| Hypertension | -0.3019 | 0.2066 | ±0.4132 | -1.462 | 0.1438 |  |
| High cholesterol | +0.1674 | 0.1954 | ±0.3907 | +0.857 | 0.3916 |  |
| Kidney disease | -0.0766 | 0.3574 | ±0.7147 | -0.214 | 0.8304 |  |
| Circulatory disease | -0.2445 | 0.3141 | ±0.6282 | -0.778 | 0.4364 |  |
| **Time > 180 (%)** | **-0.0710** | 0.0329 | ±0.0658 | **-2.156** | **0.0311** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **890**, R² = **0.1281**, Adj R² = **0.1172**, F-statistic = **11.73** (p = **1.14e-20**), Residual SE = **2.714** on **878** df, AIC = **4314.9**, BIC = **4372.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.9109** | 0.7724 | ±1.5448 | **+38.725** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8414** | 0.1876 | ±0.3751 | **+4.486** | **7.26e-06** | *** |
| **Education: high school or below (vs college)** | **-1.5497** | 0.4195 | ±0.8390 | **-3.694** | **2.21e-04** | *** |
| Site: UCSD (vs UAB) | -0.4516 | 0.2517 | ±0.5034 | -1.794 | 0.0728 | . |
| Site: UW (vs UAB) | -0.0832 | 0.2485 | ±0.4971 | -0.335 | 0.7379 |  |
| **Age (years)** | **-0.0454** | 0.0092 | ±0.0183 | **-4.955** | **7.23e-07** | *** |
| **BMI (kg/m2)** | **-0.0356** | 0.0145 | ±0.0290 | **-2.457** | **0.0140** | * |
| Hypertension | -0.3026 | 0.2065 | ±0.4129 | -1.466 | 0.1428 |  |
| High cholesterol | +0.1678 | 0.1954 | ±0.3909 | +0.859 | 0.3906 |  |
| Kidney disease | -0.0737 | 0.3563 | ±0.7126 | -0.207 | 0.8361 |  |
| Circulatory disease | -0.2412 | 0.3144 | ±0.6289 | -0.767 | 0.4431 |  |
| **Avg. daily time > 180 (%)** | **-0.0714** | 0.0331 | ±0.0662 | **-2.157** | **0.0310** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 890)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **890**, R² = **0.1276**, Adj R² = **0.1166**, F-statistic = **11.67** (p = **1.48e-20**), Residual SE = **2.715** on **878** df, AIC = **4315.5**, BIC = **4373.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.8856** | 0.7704 | ±1.5408 | **+38.792** | **0.00e+00** | *** |
| **Education: graduate level (vs college)** | **+0.8260** | 0.1882 | ±0.3764 | **+4.389** | **1.14e-05** | *** |
| **Education: high school or below (vs college)** | **-1.5153** | 0.4150 | ±0.8299 | **-3.652** | **2.61e-04** | *** |
| Site: UCSD (vs UAB) | -0.4468 | 0.2528 | ±0.5055 | -1.768 | 0.0771 | . |
| Site: UW (vs UAB) | -0.0894 | 0.2494 | ±0.4988 | -0.359 | 0.7199 |  |
| **Age (years)** | **-0.0470** | 0.0092 | ±0.0183 | **-5.122** | **3.03e-07** | *** |
| **BMI (kg/m2)** | **-0.0334** | 0.0144 | ±0.0288 | **-2.325** | **0.0201** | * |
| Hypertension | -0.3490 | 0.2039 | ±0.4078 | -1.712 | 0.0869 | . |
| High cholesterol | +0.1919 | 0.1956 | ±0.3912 | +0.981 | 0.3266 |  |
| Kidney disease | -0.0999 | 0.3601 | ±0.7203 | -0.277 | 0.7816 |  |
| Circulatory disease | -0.2587 | 0.3113 | ±0.6225 | -0.831 | 0.4059 |  |
| **Nocturnal time > 180 (%)** | **-0.0617** | 0.0296 | ±0.0592 | **-2.082** | **0.0373** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 890; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0703**, LLR χ² = **82.96** (p = **1.32e-13**), AUC = **0.6811**, AIC = **1118.9**, BIC = **1171.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.0335** | 0.6117 | ±1.2233 | **-4.959** | **7.07e-07** | 0.0481 | *** |
| **Education: graduate level (vs college)** | **-0.6982** | 0.1571 | ±0.3142 | **-4.444** | **8.84e-06** | 0.4975 | *** |
| **Education: high school or below (vs college)** | **+0.7982** | 0.2459 | ±0.4918 | **+3.246** | **0.0012** | 2.2214 | ** |
| Site: UCSD (vs UAB) | +0.2823 | 0.1884 | ±0.3769 | +1.498 | 0.1341 | 1.3261 |  |
| Site: UW (vs UAB) | +0.0700 | 0.1895 | ±0.3790 | +0.369 | 0.7119 | 1.0725 |  |
| **Age (years)** | **+0.0277** | 0.0070 | ±0.0139 | **+3.986** | **6.73e-05** | 1.0281 | *** |
| **BMI (kg/m2)** | **+0.0283** | 0.0113 | ±0.0225 | **+2.515** | **0.0119** | 1.0287 | * |
| Hypertension | +0.2962 | 0.1581 | ±0.3162 | +1.873 | 0.0610 | 1.3447 | . |
| High cholesterol | -0.0691 | 0.1507 | ±0.3014 | -0.459 | 0.6465 | 0.9332 |  |
| Kidney disease | -0.1065 | 0.2641 | ±0.5283 | -0.403 | 0.6867 | 0.8989 |  |
| Circulatory disease | +0.1178 | 0.2149 | ±0.4297 | +0.548 | 0.5834 | 1.1251 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0740**, LLR χ² = **87.30** (p = **5.63e-14**), AUC = **0.6868**, AIC = **1116.6**, BIC = **1174.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.9650** | 1.1204 | ±2.2408 | **-4.431** | **9.36e-06** | 0.0070 | *** |
| **Education: graduate level (vs college)** | **-0.7053** | 0.1575 | ±0.3150 | **-4.478** | **7.53e-06** | 0.4940 | *** |
| **Education: high school or below (vs college)** | **+0.7827** | 0.2470 | ±0.4940 | **+3.169** | **0.0015** | 2.1874 | ** |
| Site: UCSD (vs UAB) | +0.2929 | 0.1891 | ±0.3781 | +1.549 | 0.1213 | 1.3403 |  |
| Site: UW (vs UAB) | +0.0824 | 0.1905 | ±0.3810 | +0.432 | 0.6655 | 1.0858 |  |
| **Age (years)** | **+0.0272** | 0.0070 | ±0.0140 | **+3.900** | **9.61e-05** | 1.0276 | *** |
| **BMI (kg/m2)** | **+0.0239** | 0.0114 | ±0.0227 | **+2.105** | **0.0353** | 1.0242 | * |
| Hypertension | +0.2552 | 0.1596 | ±0.3192 | +1.599 | 0.1099 | 1.2907 |  |
| High cholesterol | -0.1148 | 0.1527 | ±0.3054 | -0.752 | 0.4519 | 0.8915 |  |
| Kidney disease | -0.0982 | 0.2644 | ±0.5287 | -0.371 | 0.7104 | 0.9065 |  |
| Circulatory disease | +0.0960 | 0.2159 | ±0.4318 | +0.445 | 0.6565 | 1.1008 |  |
| **HbA1c (%)** | **+0.3746** | 0.1812 | ±0.3623 | **+2.067** | **0.0387** | 1.4544 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0813**, LLR χ² = **95.91** (p = **1.15e-15**), AUC = **0.6951**, AIC = **1108.0**, BIC = **1165.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-5.5298** | 0.9382 | ±1.8764 | **-5.894** | **3.77e-09** | 0.0040 | *** |
| **Education: graduate level (vs college)** | **-0.7330** | 0.1588 | ±0.3175 | **-4.616** | **3.90e-06** | 0.4805 | *** |
| **Education: high school or below (vs college)** | **+0.7995** | 0.2476 | ±0.4953 | **+3.229** | **0.0012** | 2.2245 | ** |
| Site: UCSD (vs UAB) | +0.3194 | 0.1902 | ±0.3803 | +1.679 | 0.0931 | 1.3763 | . |
| Site: UW (vs UAB) | +0.0521 | 0.1912 | ±0.3824 | +0.273 | 0.7851 | 1.0535 |  |
| **Age (years)** | **+0.0275** | 0.0070 | ±0.0140 | **+3.929** | **8.52e-05** | 1.0279 | *** |
| **BMI (kg/m2)** | **+0.0233** | 0.0113 | ±0.0226 | **+2.063** | **0.0391** | 1.0236 | * |
| Hypertension | +0.2370 | 0.1603 | ±0.3206 | +1.478 | 0.1393 | 1.2674 |  |
| High cholesterol | -0.0771 | 0.1517 | ±0.3034 | -0.508 | 0.6115 | 0.9258 |  |
| Kidney disease | -0.1736 | 0.2664 | ±0.5328 | -0.652 | 0.5146 | 0.8406 |  |
| Circulatory disease | +0.0694 | 0.2174 | ±0.4347 | +0.319 | 0.7494 | 1.0719 |  |
| **Mean glucose (mg/dL)** | **+0.0223** | 0.0062 | ±0.0125 | **+3.574** | **3.51e-04** | 1.0225 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0813**, LLR χ² = **95.91** (p = **1.15e-15**), AUC = **0.6951**, AIC = **1108.0**, BIC = **1165.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-8.6155** | 1.6891 | ±3.3781 | **-5.101** | **3.38e-07** | 0.0002 | *** |
| **Education: graduate level (vs college)** | **-0.7330** | 0.1588 | ±0.3175 | **-4.616** | **3.90e-06** | 0.4805 | *** |
| **Education: high school or below (vs college)** | **+0.7995** | 0.2476 | ±0.4953 | **+3.229** | **0.0012** | 2.2245 | ** |
| Site: UCSD (vs UAB) | +0.3194 | 0.1902 | ±0.3803 | +1.679 | 0.0931 | 1.3763 | . |
| Site: UW (vs UAB) | +0.0521 | 0.1912 | ±0.3824 | +0.273 | 0.7851 | 1.0535 |  |
| **Age (years)** | **+0.0275** | 0.0070 | ±0.0140 | **+3.929** | **8.52e-05** | 1.0279 | *** |
| **BMI (kg/m2)** | **+0.0233** | 0.0113 | ±0.0226 | **+2.063** | **0.0391** | 1.0236 | * |
| Hypertension | +0.2370 | 0.1603 | ±0.3206 | +1.478 | 0.1393 | 1.2674 |  |
| High cholesterol | -0.0771 | 0.1517 | ±0.3034 | -0.508 | 0.6115 | 0.9258 |  |
| Kidney disease | -0.1736 | 0.2664 | ±0.5328 | -0.652 | 0.5146 | 0.8406 |  |
| Circulatory disease | +0.0694 | 0.2174 | ±0.4347 | +0.319 | 0.7494 | 1.0719 |  |
| **GMI (%)** | **+0.9322** | 0.2608 | ±0.5216 | **+3.574** | **3.51e-04** | 2.5401 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0821**, LLR χ² = **96.86** (p = **7.47e-16**), AUC = **0.6950**, AIC = **1107.0**, BIC = **1164.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-5.3606** | 0.8867 | ±1.7734 | **-6.046** | **1.49e-09** | 0.0047 | *** |
| **Education: graduate level (vs college)** | **-0.7323** | 0.1588 | ±0.3175 | **-4.613** | **3.98e-06** | 0.4808 | *** |
| **Education: high school or below (vs college)** | **+0.7999** | 0.2480 | ±0.4961 | **+3.225** | **0.0013** | 2.2254 | ** |
| Site: UCSD (vs UAB) | +0.2963 | 0.1899 | ±0.3798 | +1.560 | 0.1187 | 1.3448 |  |
| Site: UW (vs UAB) | +0.0467 | 0.1914 | ±0.3829 | +0.244 | 0.8074 | 1.0478 |  |
| **Age (years)** | **+0.0297** | 0.0070 | ±0.0141 | **+4.224** | **2.40e-05** | 1.0301 | *** |
| BMI (kg/m2) | +0.0197 | 0.0114 | ±0.0227 | +1.733 | 0.0830 | 1.0199 | . |
| Hypertension | +0.2609 | 0.1597 | ±0.3194 | +1.634 | 0.1023 | 1.2981 |  |
| High cholesterol | -0.1007 | 0.1520 | ±0.3040 | -0.663 | 0.5075 | 0.9042 |  |
| Kidney disease | -0.1335 | 0.2659 | ±0.5318 | -0.502 | 0.6155 | 0.8750 |  |
| Circulatory disease | +0.0710 | 0.2169 | ±0.4338 | +0.327 | 0.7433 | 1.0736 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0208** | 0.0056 | ±0.0112 | **+3.701** | **2.15e-04** | 1.0210 | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0739**, LLR χ² = **87.19** (p = **5.91e-14**), AUC = **0.6846**, AIC = **1116.7**, BIC = **1174.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.6665** | 0.6869 | ±1.3738 | **-5.338** | **9.42e-08** | 0.0256 | *** |
| **Education: graduate level (vs college)** | **-0.6976** | 0.1575 | ±0.3150 | **-4.429** | **9.48e-06** | 0.4978 | *** |
| **Education: high school or below (vs college)** | **+0.7650** | 0.2471 | ±0.4941 | **+3.096** | **0.0020** | 2.1490 | ** |
| Site: UCSD (vs UAB) | +0.3142 | 0.1896 | ±0.3793 | +1.657 | 0.0975 | 1.3692 | . |
| Site: UW (vs UAB) | +0.0780 | 0.1903 | ±0.3805 | +0.410 | 0.6820 | 1.0811 |  |
| **Age (years)** | **+0.0268** | 0.0070 | ±0.0140 | **+3.846** | **1.20e-04** | 1.0272 | *** |
| **BMI (kg/m2)** | **+0.0269** | 0.0112 | ±0.0225 | **+2.398** | **0.0165** | 1.0273 | * |
| Hypertension | +0.2561 | 0.1598 | ±0.3195 | +1.603 | 0.1089 | 1.2919 |  |
| High cholesterol | -0.0758 | 0.1511 | ±0.3021 | -0.502 | 0.6159 | 0.9270 |  |
| Kidney disease | -0.1523 | 0.2653 | ±0.5307 | -0.574 | 0.5659 | 0.8587 |  |
| Circulatory disease | +0.1030 | 0.2158 | ±0.4317 | +0.477 | 0.6333 | 1.1085 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0373** | 0.0182 | ±0.0363 | **+2.053** | **0.0401** | 1.0380 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0738**, LLR χ² = **87.09** (p = **6.19e-14**), AUC = **0.6851**, AIC = **1116.8**, BIC = **1174.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.6007** | 0.6739 | ±1.3479 | **-5.343** | **9.15e-08** | 0.0273 | *** |
| **Education: graduate level (vs college)** | **-0.7012** | 0.1575 | ±0.3150 | **-4.452** | **8.53e-06** | 0.4960 | *** |
| **Education: high school or below (vs college)** | **+0.7703** | 0.2469 | ±0.4938 | **+3.120** | **0.0018** | 2.1604 | ** |
| Site: UCSD (vs UAB) | +0.3112 | 0.1895 | ±0.3789 | +1.642 | 0.1005 | 1.3651 |  |
| Site: UW (vs UAB) | +0.0736 | 0.1902 | ±0.3803 | +0.387 | 0.6986 | 1.0764 |  |
| **Age (years)** | **+0.0268** | 0.0070 | ±0.0140 | **+3.842** | **1.22e-04** | 1.0272 | *** |
| **BMI (kg/m2)** | **+0.0268** | 0.0112 | ±0.0224 | **+2.386** | **0.0170** | 1.0271 | * |
| Hypertension | +0.2554 | 0.1598 | ±0.3197 | +1.598 | 0.1100 | 1.2910 |  |
| High cholesterol | -0.0733 | 0.1511 | ±0.3021 | -0.485 | 0.6274 | 0.9293 |  |
| Kidney disease | -0.1465 | 0.2649 | ±0.5298 | -0.553 | 0.5802 | 0.8637 |  |
| Circulatory disease | +0.1086 | 0.2156 | ±0.4313 | +0.504 | 0.6145 | 1.1147 |  |
| **Avg. daily SD (mg/dL)** | **+0.0374** | 0.0184 | ±0.0369 | **+2.028** | **0.0426** | 1.0381 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0705**, LLR χ² = **83.14** (p = **3.63e-13**), AUC = **0.6812**, AIC = **1120.7**, BIC = **1178.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.2021** | 0.7271 | ±1.4543 | **-4.404** | **1.06e-05** | 0.0407 | *** |
| **Education: graduate level (vs college)** | **-0.6953** | 0.1573 | ±0.3145 | **-4.421** | **9.80e-06** | 0.4989 | *** |
| **Education: high school or below (vs college)** | **+0.7902** | 0.2466 | ±0.4933 | **+3.204** | **0.0014** | 2.2039 | ** |
| Site: UCSD (vs UAB) | +0.2876 | 0.1889 | ±0.3778 | +1.523 | 0.1278 | 1.3333 |  |
| Site: UW (vs UAB) | +0.0729 | 0.1897 | ±0.3794 | +0.384 | 0.7009 | 1.0756 |  |
| **Age (years)** | **+0.0275** | 0.0070 | ±0.0139 | **+3.949** | **7.85e-05** | 1.0279 | *** |
| **BMI (kg/m2)** | **+0.0283** | 0.0112 | ±0.0225 | **+2.517** | **0.0118** | 1.0287 | * |
| Hypertension | +0.2903 | 0.1587 | ±0.3175 | +1.829 | 0.0674 | 1.3368 | . |
| High cholesterol | -0.0698 | 0.1507 | ±0.3014 | -0.463 | 0.6434 | 0.9326 |  |
| Kidney disease | -0.1133 | 0.2646 | ±0.5292 | -0.428 | 0.6684 | 0.8929 |  |
| Circulatory disease | +0.1178 | 0.2149 | ±0.4298 | +0.548 | 0.5837 | 1.1250 |  |
| CV (%) | +0.0110 | 0.0257 | ±0.0513 | +0.430 | 0.6676 | 1.0111 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0703**, LLR χ² = **82.98** (p = **3.91e-13**), AUC = **0.6812**, AIC = **1120.9**, BIC = **1178.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.9745** | 0.7502 | ±1.5005 | **-3.965** | **7.35e-05** | 0.0511 | *** |
| **Education: graduate level (vs college)** | **-0.6971** | 0.1573 | ±0.3147 | **-4.431** | **9.39e-06** | 0.4980 | *** |
| **Education: high school or below (vs college)** | **+0.7958** | 0.2465 | ±0.4930 | **+3.228** | **0.0012** | 2.2162 | ** |
| Site: UCSD (vs UAB) | +0.2835 | 0.1887 | ±0.3773 | +1.503 | 0.1329 | 1.3278 |  |
| Site: UW (vs UAB) | +0.0704 | 0.1896 | ±0.3791 | +0.372 | 0.7102 | 1.0730 |  |
| **Age (years)** | **+0.0277** | 0.0070 | ±0.0139 | **+3.970** | **7.19e-05** | 1.0281 | *** |
| **BMI (kg/m2)** | **+0.0283** | 0.0112 | ±0.0225 | **+2.515** | **0.0119** | 1.0287 | * |
| Hypertension | +0.2944 | 0.1587 | ±0.3174 | +1.855 | 0.0636 | 1.3423 | . |
| High cholesterol | -0.0693 | 0.1507 | ±0.3014 | -0.460 | 0.6457 | 0.9331 |  |
| Kidney disease | -0.1086 | 0.2646 | ±0.5291 | -0.410 | 0.6815 | 0.8971 |  |
| Circulatory disease | +0.1181 | 0.2149 | ±0.4298 | +0.550 | 0.5826 | 1.1254 |  |
| Mean / SD ratio | -0.0087 | 0.0645 | ±0.1289 | -0.136 | 0.8921 | 0.9913 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0705**, LLR χ² = **83.21** (p = **3.52e-13**), AUC = **0.6814**, AIC = **1120.6**, BIC = **1178.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.8279** | 0.7353 | ±1.4706 | **-3.846** | **1.20e-04** | 0.0591 | *** |
| **Education: graduate level (vs college)** | **-0.6952** | 0.1572 | ±0.3145 | **-4.421** | **9.82e-06** | 0.4990 | *** |
| **Education: high school or below (vs college)** | **+0.7911** | 0.2464 | ±0.4927 | **+3.211** | **0.0013** | 2.2058 | ** |
| Site: UCSD (vs UAB) | +0.2861 | 0.1886 | ±0.3772 | +1.517 | 0.1293 | 1.3312 |  |
| Site: UW (vs UAB) | +0.0704 | 0.1896 | ±0.3792 | +0.371 | 0.7105 | 1.0729 |  |
| **Age (years)** | **+0.0275** | 0.0070 | ±0.0139 | **+3.942** | **8.07e-05** | 1.0279 | *** |
| **BMI (kg/m2)** | **+0.0281** | 0.0112 | ±0.0225 | **+2.502** | **0.0124** | 1.0285 | * |
| Hypertension | +0.2901 | 0.1586 | ±0.3172 | +1.829 | 0.0674 | 1.3365 | . |
| High cholesterol | -0.0693 | 0.1507 | ±0.3014 | -0.460 | 0.6455 | 0.9330 |  |
| Kidney disease | -0.1134 | 0.2644 | ±0.5289 | -0.429 | 0.6680 | 0.8928 |  |
| Circulatory disease | +0.1212 | 0.2150 | ±0.4300 | +0.564 | 0.5730 | 1.1288 |  |
| Avg. daily mean/SD | -0.0260 | 0.0519 | ±0.1038 | -0.501 | 0.6167 | 0.9744 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0711**, LLR χ² = **83.86** (p = **2.64e-13**), AUC = **0.6826**, AIC = **1120.0**, BIC = **1177.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4211** | 0.7376 | ±1.4753 | **-4.638** | **3.52e-06** | 0.0327 | *** |
| **Education: graduate level (vs college)** | **-0.7005** | 0.1572 | ±0.3145 | **-4.455** | **8.41e-06** | 0.4964 | *** |
| **Education: high school or below (vs college)** | **+0.7808** | 0.2465 | ±0.4929 | **+3.168** | **0.0015** | 2.1832 | ** |
| Site: UCSD (vs UAB) | +0.2877 | 0.1886 | ±0.3771 | +1.526 | 0.1271 | 1.3333 |  |
| Site: UW (vs UAB) | +0.0735 | 0.1897 | ±0.3794 | +0.387 | 0.6986 | 1.0762 |  |
| **Age (years)** | **+0.0279** | 0.0070 | ±0.0139 | **+4.013** | **6.00e-05** | 1.0283 | *** |
| **BMI (kg/m2)** | **+0.0283** | 0.0112 | ±0.0225 | **+2.519** | **0.0118** | 1.0287 | * |
| Hypertension | +0.3004 | 0.1582 | ±0.3165 | +1.898 | 0.0577 | 1.3503 | . |
| High cholesterol | -0.0711 | 0.1508 | ±0.3016 | -0.471 | 0.6374 | 0.9314 |  |
| Kidney disease | -0.1127 | 0.2640 | ±0.5281 | -0.427 | 0.6695 | 0.8934 |  |
| Circulatory disease | +0.1223 | 0.2151 | ±0.4302 | +0.569 | 0.5696 | 1.1301 |  |
| MAG (mg/dL/h) | +0.0104 | 0.0110 | ±0.0219 | +0.946 | 0.3443 | 1.0104 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0728**, LLR χ² = **85.94** (p = **1.04e-13**), AUC = **0.6833**, AIC = **1117.9**, BIC = **1175.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.6793** | 0.7203 | ±1.4405 | **-5.108** | **3.25e-07** | 0.0252 | *** |
| **Education: graduate level (vs college)** | **-0.7043** | 0.1575 | ±0.3150 | **-4.472** | **7.77e-06** | 0.4945 | *** |
| **Education: high school or below (vs college)** | **+0.7711** | 0.2467 | ±0.4933 | **+3.126** | **0.0018** | 2.1622 | ** |
| Site: UCSD (vs UAB) | +0.3016 | 0.1892 | ±0.3783 | +1.594 | 0.1109 | 1.3520 |  |
| Site: UW (vs UAB) | +0.0720 | 0.1900 | ±0.3800 | +0.379 | 0.7048 | 1.0746 |  |
| **Age (years)** | **+0.0271** | 0.0070 | ±0.0139 | **+3.881** | **1.04e-04** | 1.0274 | *** |
| **BMI (kg/m2)** | **+0.0288** | 0.0113 | ±0.0225 | **+2.556** | **0.0106** | 1.0292 | * |
| Hypertension | +0.2747 | 0.1590 | ±0.3179 | +1.728 | 0.0839 | 1.3162 | . |
| High cholesterol | -0.0706 | 0.1510 | ±0.3019 | -0.468 | 0.6398 | 0.9318 |  |
| Kidney disease | -0.1325 | 0.2643 | ±0.5285 | -0.501 | 0.6161 | 0.8759 |  |
| Circulatory disease | +0.1097 | 0.2155 | ±0.4309 | +0.509 | 0.6108 | 1.1159 |  |
| Avg. daily range (mg/dL) | +0.0075 | 0.0044 | ±0.0087 | +1.722 | 0.0850 | 1.0075 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0734**, LLR χ² = **86.60** (p = **7.70e-14**), AUC = **0.6831**, AIC = **1117.3**, BIC = **1174.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3403** | 0.6339 | ±1.2678 | **-5.269** | **1.37e-07** | 0.0354 | *** |
| **Education: graduate level (vs college)** | **-0.7026** | 0.1576 | ±0.3151 | **-4.459** | **8.23e-06** | 0.4953 | *** |
| **Education: high school or below (vs college)** | **+0.7686** | 0.2468 | ±0.4936 | **+3.115** | **0.0018** | 2.1568 | ** |
| Site: UCSD (vs UAB) | +0.3056 | 0.1893 | ±0.3787 | +1.614 | 0.1065 | 1.3574 |  |
| Site: UW (vs UAB) | +0.0842 | 0.1904 | ±0.3808 | +0.442 | 0.6583 | 1.0878 |  |
| **Age (years)** | **+0.0280** | 0.0070 | ±0.0139 | **+4.012** | **6.03e-05** | 1.0283 | *** |
| **BMI (kg/m2)** | **+0.0264** | 0.0113 | ±0.0226 | **+2.341** | **0.0193** | 1.0268 | * |
| Hypertension | +0.2981 | 0.1584 | ±0.3169 | +1.881 | 0.0599 | 1.3473 | . |
| High cholesterol | -0.0933 | 0.1514 | ±0.3029 | -0.616 | 0.5378 | 0.9109 |  |
| Kidney disease | -0.1260 | 0.2647 | ±0.5294 | -0.476 | 0.6341 | 0.8816 |  |
| Circulatory disease | +0.0837 | 0.2165 | ±0.4330 | +0.387 | 0.6989 | 1.0873 |  |
| SD of daily means (mg/dL) | +0.0593 | 0.0311 | ±0.0623 | +1.903 | 0.0571 | 1.0611 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0734**, LLR χ² = **86.65** (p = **7.52e-14**), AUC = **0.6846**, AIC = **1117.2**, BIC = **1174.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.1321 | 2.2429 | ±4.4859 | +0.505 | 0.6137 | 3.1021 |  |
| **Education: graduate level (vs college)** | **-0.7058** | 0.1576 | ±0.3151 | **-4.479** | **7.48e-06** | 0.4937 | *** |
| **Education: high school or below (vs college)** | **+0.7897** | 0.2466 | ±0.4933 | **+3.202** | **0.0014** | 2.2028 | ** |
| Site: UCSD (vs UAB) | +0.3101 | 0.1894 | ±0.3789 | +1.637 | 0.1017 | 1.3635 |  |
| Site: UW (vs UAB) | +0.0768 | 0.1900 | ±0.3801 | +0.404 | 0.6863 | 1.0798 |  |
| **Age (years)** | **+0.0272** | 0.0070 | ±0.0140 | **+3.892** | **9.93e-05** | 1.0275 | *** |
| **BMI (kg/m2)** | **+0.0269** | 0.0113 | ±0.0225 | **+2.389** | **0.0169** | 1.0273 | * |
| Hypertension | +0.2746 | 0.1591 | ±0.3181 | +1.726 | 0.0843 | 1.3160 | . |
| High cholesterol | -0.0830 | 0.1511 | ±0.3023 | -0.549 | 0.5831 | 0.9204 |  |
| Kidney disease | -0.1529 | 0.2659 | ±0.5319 | -0.575 | 0.5653 | 0.8582 |  |
| Circulatory disease | +0.0893 | 0.2163 | ±0.4327 | +0.413 | 0.6798 | 1.0934 |  |
| Time in range 70-180, pooled (%) | -0.0418 | 0.0217 | ±0.0434 | -1.923 | 0.0544 | 0.9591 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0738**, LLR χ² = **87.12** (p = **6.09e-14**), AUC = **0.6851**, AIC = **1116.7**, BIC = **1174.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.4742 | 2.2850 | ±4.5700 | +0.645 | 0.5188 | 4.3677 |  |
| **Education: graduate level (vs college)** | **-0.7055** | 0.1576 | ±0.3152 | **-4.477** | **7.57e-06** | 0.4938 | *** |
| **Education: high school or below (vs college)** | **+0.7933** | 0.2467 | ±0.4933 | **+3.216** | **0.0013** | 2.2106 | ** |
| Site: UCSD (vs UAB) | +0.3119 | 0.1895 | ±0.3789 | +1.646 | 0.0997 | 1.3660 | . |
| Site: UW (vs UAB) | +0.0769 | 0.1901 | ±0.3803 | +0.405 | 0.6858 | 1.0799 |  |
| **Age (years)** | **+0.0272** | 0.0070 | ±0.0140 | **+3.893** | **9.92e-05** | 1.0275 | *** |
| **BMI (kg/m2)** | **+0.0267** | 0.0113 | ±0.0225 | **+2.375** | **0.0175** | 1.0271 | * |
| Hypertension | +0.2735 | 0.1591 | ±0.3182 | +1.719 | 0.0857 | 1.3145 | . |
| High cholesterol | -0.0844 | 0.1512 | ±0.3024 | -0.559 | 0.5765 | 0.9190 |  |
| Kidney disease | -0.1573 | 0.2660 | ±0.5321 | -0.591 | 0.5542 | 0.8544 |  |
| Circulatory disease | +0.0860 | 0.2165 | ±0.4330 | +0.397 | 0.6912 | 1.0898 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0452** | 0.0221 | ±0.0443 | **-2.040** | **0.0413** | 0.9558 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0716**, LLR χ² = **84.43** (p = **2.04e-13**), AUC = **0.6833**, AIC = **1119.4**, BIC = **1176.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.9905** | 0.6131 | ±1.2263 | **-4.877** | **1.07e-06** | 0.0503 | *** |
| **Education: graduate level (vs college)** | **-0.7131** | 0.1577 | ±0.3154 | **-4.522** | **6.14e-06** | 0.4901 | *** |
| **Education: high school or below (vs college)** | **+0.7863** | 0.2461 | ±0.4922 | **+3.195** | **0.0014** | 2.1953 | ** |
| Site: UCSD (vs UAB) | +0.2893 | 0.1887 | ±0.3773 | +1.533 | 0.1252 | 1.3355 |  |
| Site: UW (vs UAB) | +0.0650 | 0.1896 | ±0.3793 | +0.343 | 0.7319 | 1.0671 |  |
| **Age (years)** | **+0.0279** | 0.0070 | ±0.0139 | **+4.000** | **6.32e-05** | 1.0282 | *** |
| **BMI (kg/m2)** | **+0.0280** | 0.0113 | ±0.0225 | **+2.488** | **0.0129** | 1.0284 | * |
| Hypertension | +0.2954 | 0.1582 | ±0.3163 | +1.868 | 0.0618 | 1.3437 | . |
| High cholesterol | -0.0624 | 0.1509 | ±0.3018 | -0.414 | 0.6790 | 0.9395 |  |
| Kidney disease | -0.1155 | 0.2645 | ±0.5289 | -0.437 | 0.6622 | 0.8909 |  |
| Circulatory disease | +0.1114 | 0.2152 | ±0.4304 | +0.518 | 0.6046 | 1.1179 |  |
| Time 54-69, pooled (%) | -0.1942 | 0.1687 | ±0.3374 | -1.151 | 0.2497 | 0.8235 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0713**, LLR χ² = **84.07** (p = **2.39e-13**), AUC = **0.6830**, AIC = **1119.8**, BIC = **1177.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.0010** | 0.6128 | ±1.2256 | **-4.897** | **9.71e-07** | 0.0497 | *** |
| **Education: graduate level (vs college)** | **-0.7117** | 0.1577 | ±0.3154 | **-4.512** | **6.41e-06** | 0.4908 | *** |
| **Education: high school or below (vs college)** | **+0.7862** | 0.2462 | ±0.4923 | **+3.194** | **0.0014** | 2.1950 | ** |
| Site: UCSD (vs UAB) | +0.2920 | 0.1888 | ±0.3775 | +1.547 | 0.1219 | 1.3391 |  |
| Site: UW (vs UAB) | +0.0673 | 0.1896 | ±0.3792 | +0.355 | 0.7227 | 1.0696 |  |
| **Age (years)** | **+0.0279** | 0.0070 | ±0.0139 | **+4.004** | **6.23e-05** | 1.0283 | *** |
| **BMI (kg/m2)** | **+0.0280** | 0.0113 | ±0.0225 | **+2.489** | **0.0128** | 1.0284 | * |
| Hypertension | +0.2954 | 0.1581 | ±0.3163 | +1.868 | 0.0618 | 1.3437 | . |
| High cholesterol | -0.0639 | 0.1508 | ±0.3017 | -0.424 | 0.6716 | 0.9381 |  |
| Kidney disease | -0.1146 | 0.2645 | ±0.5290 | -0.433 | 0.6648 | 0.8917 |  |
| Circulatory disease | +0.1096 | 0.2153 | ±0.4305 | +0.509 | 0.6107 | 1.1158 |  |
| Avg. daily time 54-69 (%) | -0.1617 | 0.1606 | ±0.3211 | -1.007 | 0.3139 | 0.8507 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0716**, LLR χ² = **84.43** (p = **2.04e-13**), AUC = **0.6833**, AIC = **1119.4**, BIC = **1176.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.9905** | 0.6131 | ±1.2263 | **-4.877** | **1.07e-06** | 0.0503 | *** |
| **Education: graduate level (vs college)** | **-0.7131** | 0.1577 | ±0.3154 | **-4.522** | **6.14e-06** | 0.4901 | *** |
| **Education: high school or below (vs college)** | **+0.7863** | 0.2461 | ±0.4922 | **+3.195** | **0.0014** | 2.1953 | ** |
| Site: UCSD (vs UAB) | +0.2893 | 0.1887 | ±0.3773 | +1.533 | 0.1252 | 1.3355 |  |
| Site: UW (vs UAB) | +0.0650 | 0.1896 | ±0.3793 | +0.343 | 0.7319 | 1.0671 |  |
| **Age (years)** | **+0.0279** | 0.0070 | ±0.0139 | **+4.000** | **6.32e-05** | 1.0282 | *** |
| **BMI (kg/m2)** | **+0.0280** | 0.0113 | ±0.0225 | **+2.488** | **0.0129** | 1.0284 | * |
| Hypertension | +0.2954 | 0.1582 | ±0.3163 | +1.868 | 0.0618 | 1.3437 | . |
| High cholesterol | -0.0624 | 0.1509 | ±0.3018 | -0.414 | 0.6790 | 0.9395 |  |
| Kidney disease | -0.1155 | 0.2645 | ±0.5289 | -0.437 | 0.6622 | 0.8909 |  |
| Circulatory disease | +0.1114 | 0.2152 | ±0.4304 | +0.518 | 0.6046 | 1.1179 |  |
| Time < 70 (%) | -0.1942 | 0.1687 | ±0.3374 | -1.151 | 0.2497 | 0.8235 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0713**, LLR χ² = **84.07** (p = **2.39e-13**), AUC = **0.6830**, AIC = **1119.8**, BIC = **1177.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.0010** | 0.6128 | ±1.2256 | **-4.897** | **9.71e-07** | 0.0497 | *** |
| **Education: graduate level (vs college)** | **-0.7117** | 0.1577 | ±0.3154 | **-4.512** | **6.41e-06** | 0.4908 | *** |
| **Education: high school or below (vs college)** | **+0.7862** | 0.2462 | ±0.4923 | **+3.194** | **0.0014** | 2.1950 | ** |
| Site: UCSD (vs UAB) | +0.2920 | 0.1888 | ±0.3775 | +1.547 | 0.1219 | 1.3391 |  |
| Site: UW (vs UAB) | +0.0673 | 0.1896 | ±0.3792 | +0.355 | 0.7227 | 1.0696 |  |
| **Age (years)** | **+0.0279** | 0.0070 | ±0.0139 | **+4.004** | **6.23e-05** | 1.0283 | *** |
| **BMI (kg/m2)** | **+0.0280** | 0.0113 | ±0.0225 | **+2.489** | **0.0128** | 1.0284 | * |
| Hypertension | +0.2954 | 0.1581 | ±0.3163 | +1.868 | 0.0618 | 1.3437 | . |
| High cholesterol | -0.0639 | 0.1508 | ±0.3017 | -0.424 | 0.6716 | 0.9381 |  |
| Kidney disease | -0.1146 | 0.2645 | ±0.5290 | -0.433 | 0.6648 | 0.8917 |  |
| Circulatory disease | +0.1096 | 0.2153 | ±0.4305 | +0.509 | 0.6107 | 1.1158 |  |
| Avg. daily time < 70 (%) | -0.1617 | 0.1606 | ±0.3211 | -1.007 | 0.3139 | 0.8507 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0740**, LLR χ² = **87.27** (p = **5.69e-14**), AUC = **0.6856**, AIC = **1116.6**, BIC = **1174.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.0357** | 0.6117 | ±1.2234 | **-4.963** | **6.96e-07** | 0.0480 | *** |
| **Education: graduate level (vs college)** | **-0.7103** | 0.1577 | ±0.3154 | **-4.504** | **6.66e-06** | 0.4915 | *** |
| **Education: high school or below (vs college)** | **+0.7864** | 0.2467 | ±0.4935 | **+3.187** | **0.0014** | 2.1955 | ** |
| Site: UCSD (vs UAB) | +0.3142 | 0.1896 | ±0.3792 | +1.657 | 0.0975 | 1.3691 | . |
| Site: UW (vs UAB) | +0.0761 | 0.1901 | ±0.3802 | +0.401 | 0.6888 | 1.0791 |  |
| **Age (years)** | **+0.0272** | 0.0070 | ±0.0140 | **+3.891** | **1.00e-04** | 1.0275 | *** |
| **BMI (kg/m2)** | **+0.0267** | 0.0113 | ±0.0225 | **+2.373** | **0.0176** | 1.0271 | * |
| Hypertension | +0.2727 | 0.1591 | ±0.3183 | +1.713 | 0.0866 | 1.3134 | . |
| High cholesterol | -0.0826 | 0.1511 | ±0.3023 | -0.546 | 0.5849 | 0.9208 |  |
| Kidney disease | -0.1584 | 0.2662 | ±0.5324 | -0.595 | 0.5517 | 0.8535 |  |
| Circulatory disease | +0.0858 | 0.2166 | ±0.4331 | +0.396 | 0.6920 | 1.0896 |  |
| **Time 181-250, pooled (%)** | **+0.0448** | 0.0216 | ±0.0431 | **+2.076** | **0.0379** | 1.0458 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0743**, LLR χ² = **87.72** (p = **4.66e-14**), AUC = **0.6861**, AIC = **1116.1**, BIC = **1173.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.0335** | 0.6116 | ±1.2231 | **-4.960** | **7.04e-07** | 0.0481 | *** |
| **Education: graduate level (vs college)** | **-0.7106** | 0.1577 | ±0.3155 | **-4.505** | **6.65e-06** | 0.4914 | *** |
| **Education: high school or below (vs college)** | **+0.7894** | 0.2467 | ±0.4935 | **+3.199** | **0.0014** | 2.2021 | ** |
| Site: UCSD (vs UAB) | +0.3170 | 0.1896 | ±0.3793 | +1.671 | 0.0946 | 1.3730 | . |
| Site: UW (vs UAB) | +0.0765 | 0.1902 | ±0.3804 | +0.402 | 0.6874 | 1.0795 |  |
| **Age (years)** | **+0.0272** | 0.0070 | ±0.0140 | **+3.894** | **9.85e-05** | 1.0276 | *** |
| **BMI (kg/m2)** | **+0.0266** | 0.0113 | ±0.0225 | **+2.359** | **0.0183** | 1.0269 | * |
| Hypertension | +0.2717 | 0.1592 | ±0.3184 | +1.707 | 0.0879 | 1.3122 | . |
| High cholesterol | -0.0840 | 0.1512 | ±0.3024 | -0.555 | 0.5787 | 0.9195 |  |
| Kidney disease | -0.1629 | 0.2663 | ±0.5326 | -0.612 | 0.5407 | 0.8497 |  |
| Circulatory disease | +0.0817 | 0.2167 | ±0.4335 | +0.377 | 0.7064 | 1.0851 |  |
| **Avg. daily time 181-250 (%)** | **+0.0479** | 0.0220 | ±0.0440 | **+2.178** | **0.0294** | 1.0490 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0740**, LLR χ² = **87.27** (p = **5.69e-14**), AUC = **0.6856**, AIC = **1116.6**, BIC = **1174.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.0357** | 0.6117 | ±1.2234 | **-4.963** | **6.96e-07** | 0.0480 | *** |
| **Education: graduate level (vs college)** | **-0.7103** | 0.1577 | ±0.3154 | **-4.504** | **6.66e-06** | 0.4915 | *** |
| **Education: high school or below (vs college)** | **+0.7864** | 0.2467 | ±0.4935 | **+3.187** | **0.0014** | 2.1955 | ** |
| Site: UCSD (vs UAB) | +0.3142 | 0.1896 | ±0.3792 | +1.657 | 0.0975 | 1.3691 | . |
| Site: UW (vs UAB) | +0.0761 | 0.1901 | ±0.3802 | +0.401 | 0.6888 | 1.0791 |  |
| **Age (years)** | **+0.0272** | 0.0070 | ±0.0140 | **+3.891** | **1.00e-04** | 1.0275 | *** |
| **BMI (kg/m2)** | **+0.0267** | 0.0113 | ±0.0225 | **+2.373** | **0.0176** | 1.0271 | * |
| Hypertension | +0.2727 | 0.1591 | ±0.3183 | +1.713 | 0.0866 | 1.3134 | . |
| High cholesterol | -0.0826 | 0.1511 | ±0.3023 | -0.546 | 0.5849 | 0.9208 |  |
| Kidney disease | -0.1584 | 0.2662 | ±0.5324 | -0.595 | 0.5517 | 0.8535 |  |
| Circulatory disease | +0.0858 | 0.2166 | ±0.4331 | +0.396 | 0.6920 | 1.0896 |  |
| **Time > 180 (%)** | **+0.0448** | 0.0216 | ±0.0431 | **+2.076** | **0.0379** | 1.0458 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0743**, LLR χ² = **87.72** (p = **4.66e-14**), AUC = **0.6861**, AIC = **1116.1**, BIC = **1173.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.0335** | 0.6116 | ±1.2231 | **-4.960** | **7.04e-07** | 0.0481 | *** |
| **Education: graduate level (vs college)** | **-0.7106** | 0.1577 | ±0.3155 | **-4.505** | **6.65e-06** | 0.4914 | *** |
| **Education: high school or below (vs college)** | **+0.7894** | 0.2467 | ±0.4935 | **+3.199** | **0.0014** | 2.2021 | ** |
| Site: UCSD (vs UAB) | +0.3170 | 0.1896 | ±0.3793 | +1.671 | 0.0946 | 1.3730 | . |
| Site: UW (vs UAB) | +0.0765 | 0.1902 | ±0.3804 | +0.402 | 0.6874 | 1.0795 |  |
| **Age (years)** | **+0.0272** | 0.0070 | ±0.0140 | **+3.894** | **9.85e-05** | 1.0276 | *** |
| **BMI (kg/m2)** | **+0.0266** | 0.0113 | ±0.0225 | **+2.359** | **0.0183** | 1.0269 | * |
| Hypertension | +0.2717 | 0.1592 | ±0.3184 | +1.707 | 0.0879 | 1.3122 | . |
| High cholesterol | -0.0840 | 0.1512 | ±0.3024 | -0.555 | 0.5787 | 0.9195 |  |
| Kidney disease | -0.1629 | 0.2663 | ±0.5326 | -0.612 | 0.5407 | 0.8497 |  |
| Circulatory disease | +0.0817 | 0.2167 | ±0.4335 | +0.377 | 0.7064 | 1.0851 |  |
| **Avg. daily time > 180 (%)** | **+0.0479** | 0.0220 | ±0.0440 | **+2.178** | **0.0294** | 1.0490 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 890)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **890**, events = **336**, McFadden pseudo-R² = **0.0739**, LLR χ² = **87.24** (p = **5.78e-14**), AUC = **0.6837**, AIC = **1116.6**, BIC = **1174.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.0210** | 0.6115 | ±1.2230 | **-4.940** | **7.80e-07** | 0.0488 | *** |
| **Education: graduate level (vs college)** | **-0.7007** | 0.1575 | ±0.3150 | **-4.449** | **8.61e-06** | 0.4962 | *** |
| **Education: high school or below (vs college)** | **+0.7663** | 0.2474 | ±0.4947 | **+3.098** | **0.0019** | 2.1517 | ** |
| Site: UCSD (vs UAB) | +0.3130 | 0.1895 | ±0.3790 | +1.652 | 0.0986 | 1.3675 | . |
| Site: UW (vs UAB) | +0.0812 | 0.1902 | ±0.3804 | +0.427 | 0.6695 | 1.0846 |  |
| **Age (years)** | **+0.0282** | 0.0070 | ±0.0140 | **+4.047** | **5.18e-05** | 1.0286 | *** |
| **BMI (kg/m2)** | **+0.0252** | 0.0113 | ±0.0226 | **+2.224** | **0.0261** | 1.0255 | * |
| Hypertension | +0.3027 | 0.1586 | ±0.3173 | +1.908 | 0.0563 | 1.3536 | . |
| High cholesterol | -0.1002 | 0.1517 | ±0.3035 | -0.660 | 0.5091 | 0.9047 |  |
| Kidney disease | -0.1402 | 0.2654 | ±0.5308 | -0.528 | 0.5974 | 0.8692 |  |
| Circulatory disease | +0.0943 | 0.2161 | ±0.4323 | +0.436 | 0.6626 | 1.0989 |  |
| **Nocturnal time > 180 (%)** | **+0.0415** | 0.0204 | ±0.0408 | **+2.033** | **0.0420** | 1.0423 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 890; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **890**, R² = **0.0743**, Adj R² = **0.0637**, F-statistic = **7.05** (p = **1.01e-10**), Residual SE = **2.532** on **879** df, AIC = **4190.1**, BIC = **4242.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2165** | 0.7079 | ±1.4158 | **+22.909** | **3.82e-116** | *** |
| Education: graduate level (vs college) | +0.2818 | 0.1792 | ±0.3584 | +1.572 | 0.1159 |  |
| **Education: high school or below (vs college)** | **-1.1375** | 0.3818 | ±0.7636 | **-2.979** | **0.0029** | ** |
| Site: UCSD (vs UAB) | +0.0424 | 0.2343 | ±0.4686 | +0.181 | 0.8565 |  |
| Site: UW (vs UAB) | +0.0351 | 0.2291 | ±0.4583 | +0.153 | 0.8783 |  |
| **Age (years)** | **-0.0455** | 0.0086 | ±0.0173 | **-5.267** | **1.39e-07** | *** |
| BMI (kg/m2) | -0.0234 | 0.0123 | ±0.0247 | -1.899 | 0.0575 | . |
| Hypertension | -0.2906 | 0.1882 | ±0.3765 | -1.544 | 0.1226 |  |
| High cholesterol | +0.0287 | 0.1826 | ±0.3652 | +0.157 | 0.8752 |  |
| Kidney disease | -0.2061 | 0.3795 | ±0.7591 | -0.543 | 0.5872 |  |
| Circulatory disease | +0.0018 | 0.2655 | ±0.5309 | +0.007 | 0.9947 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **890**, R² = **0.0743**, Adj R² = **0.0627**, F-statistic = **6.41** (p = **2.74e-10**), Residual SE = **2.533** on **878** df, AIC = **4192.1**, BIC = **4249.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4560** | 1.3611 | ±2.7221 | **+12.091** | **1.18e-33** | *** |
| Education: graduate level (vs college) | +0.2818 | 0.1794 | ±0.3588 | +1.571 | 0.1162 |  |
| **Education: high school or below (vs college)** | **-1.1348** | 0.3831 | ±0.7662 | **-2.962** | **0.0031** | ** |
| Site: UCSD (vs UAB) | +0.0416 | 0.2346 | ±0.4691 | +0.177 | 0.8593 |  |
| Site: UW (vs UAB) | +0.0343 | 0.2295 | ±0.4590 | +0.149 | 0.8813 |  |
| **Age (years)** | **-0.0454** | 0.0087 | ±0.0173 | **-5.242** | **1.59e-07** | *** |
| BMI (kg/m2) | -0.0229 | 0.0124 | ±0.0249 | -1.840 | 0.0658 | . |
| Hypertension | -0.2849 | 0.1904 | ±0.3808 | -1.496 | 0.1345 |  |
| High cholesterol | +0.0341 | 0.1832 | ±0.3664 | +0.186 | 0.8524 |  |
| Kidney disease | -0.2068 | 0.3800 | ±0.7599 | -0.544 | 0.5862 |  |
| Circulatory disease | +0.0050 | 0.2636 | ±0.5273 | +0.019 | 0.9850 |  |
| HbA1c (%) | -0.0468 | 0.2209 | ±0.4417 | -0.212 | 0.8322 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **890**, R² = **0.0810**, Adj R² = **0.0695**, F-statistic = **7.04** (p = **1.66e-11**), Residual SE = **2.524** on **878** df, AIC = **4185.6**, BIC = **4243.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.2376** | 1.1827 | ±2.3653 | **+15.421** | **1.19e-53** | *** |
| Education: graduate level (vs college) | +0.3000 | 0.1776 | ±0.3551 | +1.690 | 0.0911 | . |
| **Education: high school or below (vs college)** | **-1.1277** | 0.3813 | ±0.7625 | **-2.958** | **0.0031** | ** |
| Site: UCSD (vs UAB) | +0.0201 | 0.2312 | ±0.4624 | +0.087 | 0.9308 |  |
| Site: UW (vs UAB) | +0.0503 | 0.2299 | ±0.4598 | +0.219 | 0.8269 |  |
| **Age (years)** | **-0.0450** | 0.0086 | ±0.0172 | **-5.218** | **1.81e-07** | *** |
| BMI (kg/m2) | -0.0193 | 0.0126 | ±0.0252 | -1.529 | 0.1263 |  |
| Hypertension | -0.2377 | 0.1921 | ±0.3841 | -1.238 | 0.2159 |  |
| High cholesterol | +0.0371 | 0.1832 | ±0.3663 | +0.202 | 0.8397 |  |
| Kidney disease | -0.1572 | 0.3741 | ±0.7481 | -0.420 | 0.6742 |  |
| Circulatory disease | +0.0425 | 0.2632 | ±0.5264 | +0.162 | 0.8716 |  |
| Mean glucose (mg/dL) | -0.0183 | 0.0094 | ±0.0187 | -1.953 | 0.0508 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **890**, R² = **0.0810**, Adj R² = **0.0695**, F-statistic = **7.04** (p = **1.66e-11**), Residual SE = **2.524** on **878** df, AIC = **4185.6**, BIC = **4243.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20.7690** | 2.3560 | ±4.7121 | **+8.815** | **1.19e-18** | *** |
| Education: graduate level (vs college) | +0.3000 | 0.1776 | ±0.3551 | +1.690 | 0.0911 | . |
| **Education: high school or below (vs college)** | **-1.1277** | 0.3813 | ±0.7625 | **-2.958** | **0.0031** | ** |
| Site: UCSD (vs UAB) | +0.0201 | 0.2312 | ±0.4624 | +0.087 | 0.9308 |  |
| Site: UW (vs UAB) | +0.0503 | 0.2299 | ±0.4598 | +0.219 | 0.8269 |  |
| **Age (years)** | **-0.0450** | 0.0086 | ±0.0172 | **-5.218** | **1.81e-07** | *** |
| BMI (kg/m2) | -0.0193 | 0.0126 | ±0.0252 | -1.529 | 0.1263 |  |
| Hypertension | -0.2377 | 0.1921 | ±0.3841 | -1.238 | 0.2159 |  |
| High cholesterol | +0.0371 | 0.1832 | ±0.3663 | +0.202 | 0.8397 |  |
| Kidney disease | -0.1572 | 0.3741 | ±0.7481 | -0.420 | 0.6742 |  |
| Circulatory disease | +0.0425 | 0.2632 | ±0.5264 | +0.162 | 0.8716 |  |
| GMI (%) | -0.7648 | 0.3916 | ±0.7833 | -1.953 | 0.0508 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **890**, R² = **0.0833**, Adj R² = **0.0718**, F-statistic = **7.25** (p = **6.23e-12**), Residual SE = **2.521** on **878** df, AIC = **4183.4**, BIC = **4240.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.3040** | 1.0600 | ±2.1200 | **+17.268** | **8.25e-67** | *** |
| Education: graduate level (vs college) | +0.2983 | 0.1781 | ±0.3561 | +1.675 | 0.0939 | . |
| **Education: high school or below (vs college)** | **-1.1273** | 0.3805 | ±0.7609 | **-2.963** | **0.0030** | ** |
| Site: UCSD (vs UAB) | +0.0408 | 0.2325 | ±0.4649 | +0.175 | 0.8607 |  |
| Site: UW (vs UAB) | +0.0584 | 0.2300 | ±0.4599 | +0.254 | 0.7994 |  |
| **Age (years)** | **-0.0468** | 0.0086 | ±0.0172 | **-5.444** | **5.21e-08** | *** |
| BMI (kg/m2) | -0.0152 | 0.0130 | ±0.0261 | -1.169 | 0.2425 |  |
| Hypertension | -0.2519 | 0.1901 | ±0.3803 | -1.325 | 0.1853 |  |
| High cholesterol | +0.0585 | 0.1840 | ±0.3679 | +0.318 | 0.7506 |  |
| Kidney disease | -0.1839 | 0.3762 | ±0.7524 | -0.489 | 0.6250 |  |
| Circulatory disease | +0.0469 | 0.2616 | ±0.5232 | +0.179 | 0.8577 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0190** | 0.0079 | ±0.0157 | **-2.417** | **0.0156** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **890**, R² = **0.0743**, Adj R² = **0.0627**, F-statistic = **6.40** (p = **2.79e-10**), Residual SE = **2.533** on **878** df, AIC = **4192.1**, BIC = **4249.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2438** | 0.8029 | ±1.6057 | **+20.232** | **5.08e-91** | *** |
| Education: graduate level (vs college) | +0.2815 | 0.1797 | ±0.3594 | +1.566 | 0.1172 |  |
| **Education: high school or below (vs college)** | **-1.1358** | 0.3838 | ±0.7676 | **-2.960** | **0.0031** | ** |
| Site: UCSD (vs UAB) | +0.0412 | 0.2352 | ±0.4703 | +0.175 | 0.8610 |  |
| Site: UW (vs UAB) | +0.0348 | 0.2293 | ±0.4586 | +0.152 | 0.8793 |  |
| **Age (years)** | **-0.0454** | 0.0087 | ±0.0173 | **-5.249** | **1.53e-07** | *** |
| BMI (kg/m2) | -0.0234 | 0.0124 | ±0.0248 | -1.885 | 0.0595 | . |
| Hypertension | -0.2888 | 0.1896 | ±0.3792 | -1.523 | 0.1277 |  |
| High cholesterol | +0.0290 | 0.1827 | ±0.3655 | +0.159 | 0.8740 |  |
| Kidney disease | -0.2043 | 0.3817 | ±0.7633 | -0.535 | 0.5925 |  |
| Circulatory disease | +0.0024 | 0.2648 | ±0.5297 | +0.009 | 0.9926 |  |
| Glucose SD, pooled (mg/dL) | -0.0016 | 0.0223 | ±0.0446 | -0.073 | 0.9419 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **890**, R² = **0.0743**, Adj R² = **0.0627**, F-statistic = **6.41** (p = **2.74e-10**), Residual SE = **2.533** on **878** df, AIC = **4192.1**, BIC = **4249.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2899** | 0.7864 | ±1.5728 | **+20.714** | **2.58e-95** | *** |
| Education: graduate level (vs college) | +0.2815 | 0.1796 | ±0.3591 | +1.567 | 0.1170 |  |
| **Education: high school or below (vs college)** | **-1.1333** | 0.3835 | ±0.7670 | **-2.955** | **0.0031** | ** |
| Site: UCSD (vs UAB) | +0.0391 | 0.2348 | ±0.4695 | +0.167 | 0.8676 |  |
| Site: UW (vs UAB) | +0.0347 | 0.2294 | ±0.4587 | +0.151 | 0.8796 |  |
| **Age (years)** | **-0.0453** | 0.0086 | ±0.0173 | **-5.242** | **1.59e-07** | *** |
| BMI (kg/m2) | -0.0232 | 0.0124 | ±0.0248 | -1.873 | 0.0611 | . |
| Hypertension | -0.2850 | 0.1897 | ±0.3794 | -1.502 | 0.1330 |  |
| High cholesterol | +0.0292 | 0.1828 | ±0.3656 | +0.160 | 0.8733 |  |
| Kidney disease | -0.2012 | 0.3812 | ±0.7623 | -0.528 | 0.5975 |  |
| Circulatory disease | +0.0031 | 0.2651 | ±0.5302 | +0.012 | 0.9907 |  |
| Avg. daily SD (mg/dL) | -0.0049 | 0.0225 | ±0.0451 | -0.216 | 0.8293 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **890**, R² = **0.0757**, Adj R² = **0.0641**, F-statistic = **6.54** (p = **1.53e-10**), Residual SE = **2.531** on **878** df, AIC = **4190.8**, BIC = **4248.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.6749** | 0.8765 | ±1.7529 | **+17.884** | **1.56e-71** | *** |
| Education: graduate level (vs college) | +0.2925 | 0.1790 | ±0.3579 | +1.634 | 0.1022 |  |
| **Education: high school or below (vs college)** | **-1.1636** | 0.3833 | ±0.7666 | **-3.036** | **0.0024** | ** |
| Site: UCSD (vs UAB) | +0.0582 | 0.2359 | ±0.4718 | +0.247 | 0.8051 |  |
| Site: UW (vs UAB) | +0.0431 | 0.2294 | ±0.4588 | +0.188 | 0.8510 |  |
| **Age (years)** | **-0.0461** | 0.0087 | ±0.0173 | **-5.327** | **9.97e-08** | *** |
| BMI (kg/m2) | -0.0233 | 0.0123 | ±0.0246 | -1.898 | 0.0577 | . |
| Hypertension | -0.3103 | 0.1883 | ±0.3766 | -1.648 | 0.0993 | . |
| High cholesterol | +0.0267 | 0.1826 | ±0.3652 | +0.146 | 0.8839 |  |
| Kidney disease | -0.2259 | 0.3811 | ±0.7621 | -0.593 | 0.5533 |  |
| Circulatory disease | +0.0013 | 0.2665 | ±0.5331 | +0.005 | 0.9960 |  |
| CV (%) | +0.0352 | 0.0316 | ±0.0632 | +1.115 | 0.2650 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **890**, R² = **0.0762**, Adj R² = **0.0646**, F-statistic = **6.58** (p = **1.26e-10**), Residual SE = **2.531** on **878** df, AIC = **4190.3**, BIC = **4247.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.8932** | 0.8637 | ±1.7275 | **+19.558** | **3.51e-85** | *** |
| Education: graduate level (vs college) | +0.2963 | 0.1787 | ±0.3573 | +1.659 | 0.0972 | . |
| **Education: high school or below (vs college)** | **-1.1648** | 0.3830 | ±0.7660 | **-3.041** | **0.0024** | ** |
| Site: UCSD (vs UAB) | +0.0553 | 0.2357 | ±0.4714 | +0.235 | 0.8145 |  |
| Site: UW (vs UAB) | +0.0390 | 0.2292 | ±0.4584 | +0.170 | 0.8650 |  |
| **Age (years)** | **-0.0461** | 0.0086 | ±0.0173 | **-5.337** | **9.45e-08** | *** |
| BMI (kg/m2) | -0.0234 | 0.0123 | ±0.0245 | -1.907 | 0.0565 | . |
| Hypertension | -0.3128 | 0.1881 | ±0.3762 | -1.663 | 0.0963 | . |
| High cholesterol | +0.0274 | 0.1827 | ±0.3654 | +0.150 | 0.8807 |  |
| Kidney disease | -0.2284 | 0.3808 | ±0.7617 | -0.600 | 0.5486 |  |
| Circulatory disease | +0.0045 | 0.2668 | ±0.5337 | +0.017 | 0.9864 |  |
| Mean / SD ratio | -0.1009 | 0.0841 | ±0.1682 | -1.199 | 0.2303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **890**, R² = **0.0749**, Adj R² = **0.0633**, F-statistic = **6.47** (p = **2.12e-10**), Residual SE = **2.532** on **878** df, AIC = **4191.5**, BIC = **4249.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.5903** | 0.8303 | ±1.6606 | **+19.981** | **7.98e-89** | *** |
| Education: graduate level (vs college) | +0.2887 | 0.1790 | ±0.3580 | +1.613 | 0.1068 |  |
| **Education: high school or below (vs college)** | **-1.1509** | 0.3824 | ±0.7647 | **-3.010** | **0.0026** | ** |
| Site: UCSD (vs UAB) | +0.0487 | 0.2353 | ±0.4706 | +0.207 | 0.8360 |  |
| Site: UW (vs UAB) | +0.0356 | 0.2292 | ±0.4584 | +0.155 | 0.8765 |  |
| **Age (years)** | **-0.0459** | 0.0086 | ±0.0173 | **-5.317** | **1.05e-07** | *** |
| BMI (kg/m2) | -0.0237 | 0.0123 | ±0.0246 | -1.922 | 0.0546 | . |
| Hypertension | -0.3026 | 0.1884 | ±0.3767 | -1.606 | 0.1082 |  |
| High cholesterol | +0.0292 | 0.1829 | ±0.3658 | +0.159 | 0.8733 |  |
| Kidney disease | -0.2184 | 0.3810 | ±0.7620 | -0.573 | 0.5664 |  |
| Circulatory disease | +0.0074 | 0.2670 | ±0.5341 | +0.028 | 0.9779 |  |
| Avg. daily mean/SD | -0.0475 | 0.0628 | ±0.1255 | -0.756 | 0.4494 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **890**, R² = **0.0743**, Adj R² = **0.0627**, F-statistic = **6.41** (p = **2.77e-10**), Residual SE = **2.533** on **878** df, AIC = **4192.1**, BIC = **4249.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1440** | 0.8119 | ±1.6237 | **+19.885** | **5.44e-88** | *** |
| Education: graduate level (vs college) | +0.2817 | 0.1794 | ±0.3587 | +1.570 | 0.1163 |  |
| **Education: high school or below (vs college)** | **-1.1409** | 0.3805 | ±0.7611 | **-2.998** | **0.0027** | ** |
| Site: UCSD (vs UAB) | +0.0431 | 0.2346 | ±0.4691 | +0.184 | 0.8542 |  |
| Site: UW (vs UAB) | +0.0359 | 0.2296 | ±0.4591 | +0.157 | 0.8756 |  |
| **Age (years)** | **-0.0454** | 0.0086 | ±0.0173 | **-5.259** | **1.45e-07** | *** |
| BMI (kg/m2) | -0.0234 | 0.0123 | ±0.0247 | -1.898 | 0.0577 | . |
| Hypertension | -0.2900 | 0.1885 | ±0.3770 | -1.539 | 0.1239 |  |
| High cholesterol | +0.0285 | 0.1828 | ±0.3656 | +0.156 | 0.8761 |  |
| Kidney disease | -0.2075 | 0.3809 | ±0.7618 | -0.545 | 0.5859 |  |
| Circulatory disease | +0.0027 | 0.2657 | ±0.5315 | +0.010 | 0.9920 |  |
| MAG (mg/dL/h) | +0.0020 | 0.0119 | ±0.0238 | +0.164 | 0.8696 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **890**, R² = **0.0743**, Adj R² = **0.0627**, F-statistic = **6.41** (p = **2.74e-10**), Residual SE = **2.533** on **878** df, AIC = **4192.1**, BIC = **4249.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3098** | 0.8320 | ±1.6639 | **+19.604** | **1.44e-85** | *** |
| Education: graduate level (vs college) | +0.2821 | 0.1795 | ±0.3590 | +1.572 | 0.1160 |  |
| **Education: high school or below (vs college)** | **-1.1332** | 0.3826 | ±0.7651 | **-2.962** | **0.0031** | ** |
| Site: UCSD (vs UAB) | +0.0400 | 0.2348 | ±0.4696 | +0.170 | 0.8646 |  |
| Site: UW (vs UAB) | +0.0349 | 0.2294 | ±0.4588 | +0.152 | 0.8790 |  |
| **Age (years)** | **-0.0454** | 0.0086 | ±0.0173 | **-5.246** | **1.55e-07** | *** |
| BMI (kg/m2) | -0.0235 | 0.0123 | ±0.0247 | -1.904 | 0.0569 | . |
| Hypertension | -0.2872 | 0.1889 | ±0.3779 | -1.520 | 0.1285 |  |
| High cholesterol | +0.0288 | 0.1828 | ±0.3656 | +0.157 | 0.8749 |  |
| Kidney disease | -0.2022 | 0.3805 | ±0.7609 | -0.531 | 0.5951 |  |
| Circulatory disease | +0.0030 | 0.2652 | ±0.5303 | +0.011 | 0.9911 |  |
| Avg. daily range (mg/dL) | -0.0011 | 0.0050 | ±0.0101 | -0.217 | 0.8284 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **890**, R² = **0.0747**, Adj R² = **0.0631**, F-statistic = **6.44** (p = **2.34e-10**), Residual SE = **2.533** on **878** df, AIC = **4191.7**, BIC = **4249.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3322** | 0.7277 | ±1.4555 | **+22.443** | **1.51e-111** | *** |
| Education: graduate level (vs college) | +0.2814 | 0.1795 | ±0.3589 | +1.568 | 0.1168 |  |
| **Education: high school or below (vs college)** | **-1.1245** | 0.3813 | ±0.7627 | **-2.949** | **0.0032** | ** |
| Site: UCSD (vs UAB) | +0.0350 | 0.2354 | ±0.4709 | +0.149 | 0.8819 |  |
| Site: UW (vs UAB) | +0.0314 | 0.2297 | ±0.4593 | +0.137 | 0.8912 |  |
| **Age (years)** | **-0.0455** | 0.0086 | ±0.0173 | **-5.273** | **1.34e-07** | *** |
| BMI (kg/m2) | -0.0226 | 0.0125 | ±0.0250 | -1.813 | 0.0698 | . |
| Hypertension | -0.2913 | 0.1884 | ±0.3769 | -1.546 | 0.1222 |  |
| High cholesterol | +0.0386 | 0.1828 | ±0.3656 | +0.211 | 0.8327 |  |
| Kidney disease | -0.1987 | 0.3803 | ±0.7607 | -0.522 | 0.6014 |  |
| Circulatory disease | +0.0152 | 0.2660 | ±0.5319 | +0.057 | 0.9543 |  |
| SD of daily means (mg/dL) | -0.0236 | 0.0365 | ±0.0731 | -0.646 | 0.5183 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **890**, R² = **0.0775**, Adj R² = **0.0660**, F-statistic = **6.71** (p = **7.18e-11**), Residual SE = **2.529** on **878** df, AIC = **4189.0**, BIC = **4246.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.7163** | 3.9281 | ±7.8562 | **+2.983** | **0.0029** | ** |
| Education: graduate level (vs college) | +0.2868 | 0.1784 | ±0.3569 | +1.608 | 0.1079 |  |
| **Education: high school or below (vs college)** | **-1.1214** | 0.3837 | ±0.7674 | **-2.923** | **0.0035** | ** |
| Site: UCSD (vs UAB) | +0.0159 | 0.2301 | ±0.4601 | +0.069 | 0.9449 |  |
| Site: UW (vs UAB) | +0.0283 | 0.2279 | ±0.4558 | +0.124 | 0.9013 |  |
| **Age (years)** | **-0.0447** | 0.0087 | ±0.0173 | **-5.161** | **2.45e-07** | *** |
| BMI (kg/m2) | -0.0220 | 0.0125 | ±0.0251 | -1.750 | 0.0801 | . |
| Hypertension | -0.2678 | 0.1904 | ±0.3808 | -1.406 | 0.1597 |  |
| High cholesterol | +0.0445 | 0.1841 | ±0.3682 | +0.242 | 0.8089 |  |
| Kidney disease | -0.1615 | 0.3759 | ±0.7517 | -0.430 | 0.6674 |  |
| Circulatory disease | +0.0322 | 0.2638 | ±0.5275 | +0.122 | 0.9027 |  |
| Time in range 70-180, pooled (%) | +0.0451 | 0.0379 | ±0.0757 | +1.190 | 0.2339 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **890**, R² = **0.0774**, Adj R² = **0.0659**, F-statistic = **6.70** (p = **7.43e-11**), Residual SE = **2.529** on **878** df, AIC = **4189.1**, BIC = **4246.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.6715** | 4.0194 | ±8.0387 | **+2.904** | **0.0037** | ** |
| Education: graduate level (vs college) | +0.2860 | 0.1786 | ±0.3572 | +1.602 | 0.1092 |  |
| **Education: high school or below (vs college)** | **-1.1262** | 0.3834 | ±0.7667 | **-2.938** | **0.0033** | ** |
| Site: UCSD (vs UAB) | +0.0158 | 0.2299 | ±0.4599 | +0.069 | 0.9451 |  |
| Site: UW (vs UAB) | +0.0285 | 0.2281 | ±0.4562 | +0.125 | 0.9007 |  |
| **Age (years)** | **-0.0448** | 0.0087 | ±0.0173 | **-5.170** | **2.34e-07** | *** |
| BMI (kg/m2) | -0.0219 | 0.0126 | ±0.0251 | -1.743 | 0.0814 | . |
| Hypertension | -0.2681 | 0.1905 | ±0.3811 | -1.407 | 0.1594 |  |
| High cholesterol | +0.0447 | 0.1841 | ±0.3682 | +0.243 | 0.8080 |  |
| Kidney disease | -0.1597 | 0.3748 | ±0.7496 | -0.426 | 0.6701 |  |
| Circulatory disease | +0.0336 | 0.2636 | ±0.5271 | +0.128 | 0.8984 |  |
| Avg. daily time in range 70-180 (%) | +0.0455 | 0.0388 | ±0.0775 | +1.174 | 0.2405 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **890**, R² = **0.0747**, Adj R² = **0.0631**, F-statistic = **6.44** (p = **2.33e-10**), Residual SE = **2.533** on **878** df, AIC = **4191.7**, BIC = **4249.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1862** | 0.7098 | ±1.4195 | **+22.805** | **4.05e-115** | *** |
| Education: graduate level (vs college) | +0.2909 | 0.1795 | ±0.3589 | +1.621 | 0.1051 |  |
| **Education: high school or below (vs college)** | **-1.1292** | 0.3821 | ±0.7641 | **-2.955** | **0.0031** | ** |
| Site: UCSD (vs UAB) | +0.0386 | 0.2345 | ±0.4691 | +0.165 | 0.8692 |  |
| Site: UW (vs UAB) | +0.0376 | 0.2294 | ±0.4587 | +0.164 | 0.8699 |  |
| **Age (years)** | **-0.0455** | 0.0086 | ±0.0173 | **-5.270** | **1.37e-07** | *** |
| BMI (kg/m2) | -0.0232 | 0.0123 | ±0.0247 | -1.882 | 0.0599 | . |
| Hypertension | -0.2890 | 0.1883 | ±0.3766 | -1.535 | 0.1248 |  |
| High cholesterol | +0.0254 | 0.1825 | ±0.3651 | +0.139 | 0.8895 |  |
| Kidney disease | -0.2018 | 0.3796 | ±0.7592 | -0.532 | 0.5950 |  |
| Circulatory disease | +0.0049 | 0.2655 | ±0.5309 | +0.018 | 0.9853 |  |
| Time 54-69, pooled (%) | +0.1147 | 0.1257 | ±0.2515 | +0.912 | 0.3615 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **890**, R² = **0.0747**, Adj R² = **0.0632**, F-statistic = **6.45** (p = **2.30e-10**), Residual SE = **2.533** on **878** df, AIC = **4191.7**, BIC = **4249.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1894** | 0.7087 | ±1.4174 | **+22.843** | **1.70e-115** | *** |
| Education: graduate level (vs college) | +0.2916 | 0.1796 | ±0.3592 | +1.624 | 0.1044 |  |
| **Education: high school or below (vs college)** | **-1.1278** | 0.3819 | ±0.7638 | **-2.953** | **0.0031** | ** |
| Site: UCSD (vs UAB) | +0.0359 | 0.2348 | ±0.4695 | +0.153 | 0.8786 |  |
| Site: UW (vs UAB) | +0.0367 | 0.2293 | ±0.4586 | +0.160 | 0.8727 |  |
| **Age (years)** | **-0.0455** | 0.0086 | ±0.0173 | **-5.274** | **1.33e-07** | *** |
| BMI (kg/m2) | -0.0232 | 0.0123 | ±0.0247 | -1.881 | 0.0599 | . |
| Hypertension | -0.2889 | 0.1883 | ±0.3766 | -1.535 | 0.1249 |  |
| High cholesterol | +0.0256 | 0.1826 | ±0.3651 | +0.140 | 0.8884 |  |
| Kidney disease | -0.2014 | 0.3797 | ±0.7595 | -0.530 | 0.5959 |  |
| Circulatory disease | +0.0069 | 0.2656 | ±0.5312 | +0.026 | 0.9794 |  |
| Avg. daily time 54-69 (%) | +0.1158 | 0.1251 | ±0.2502 | +0.926 | 0.3546 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **890**, R² = **0.0747**, Adj R² = **0.0631**, F-statistic = **6.44** (p = **2.33e-10**), Residual SE = **2.533** on **878** df, AIC = **4191.7**, BIC = **4249.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1862** | 0.7098 | ±1.4195 | **+22.805** | **4.05e-115** | *** |
| Education: graduate level (vs college) | +0.2909 | 0.1795 | ±0.3589 | +1.621 | 0.1051 |  |
| **Education: high school or below (vs college)** | **-1.1292** | 0.3821 | ±0.7641 | **-2.955** | **0.0031** | ** |
| Site: UCSD (vs UAB) | +0.0386 | 0.2345 | ±0.4691 | +0.165 | 0.8692 |  |
| Site: UW (vs UAB) | +0.0376 | 0.2294 | ±0.4587 | +0.164 | 0.8699 |  |
| **Age (years)** | **-0.0455** | 0.0086 | ±0.0173 | **-5.270** | **1.37e-07** | *** |
| BMI (kg/m2) | -0.0232 | 0.0123 | ±0.0247 | -1.882 | 0.0599 | . |
| Hypertension | -0.2890 | 0.1883 | ±0.3766 | -1.535 | 0.1248 |  |
| High cholesterol | +0.0254 | 0.1825 | ±0.3651 | +0.139 | 0.8895 |  |
| Kidney disease | -0.2018 | 0.3796 | ±0.7592 | -0.532 | 0.5950 |  |
| Circulatory disease | +0.0049 | 0.2655 | ±0.5309 | +0.018 | 0.9853 |  |
| Time < 70 (%) | +0.1147 | 0.1257 | ±0.2515 | +0.912 | 0.3615 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **890**, R² = **0.0747**, Adj R² = **0.0632**, F-statistic = **6.45** (p = **2.30e-10**), Residual SE = **2.533** on **878** df, AIC = **4191.7**, BIC = **4249.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1894** | 0.7087 | ±1.4174 | **+22.843** | **1.70e-115** | *** |
| Education: graduate level (vs college) | +0.2916 | 0.1796 | ±0.3592 | +1.624 | 0.1044 |  |
| **Education: high school or below (vs college)** | **-1.1278** | 0.3819 | ±0.7638 | **-2.953** | **0.0031** | ** |
| Site: UCSD (vs UAB) | +0.0359 | 0.2348 | ±0.4695 | +0.153 | 0.8786 |  |
| Site: UW (vs UAB) | +0.0367 | 0.2293 | ±0.4586 | +0.160 | 0.8727 |  |
| **Age (years)** | **-0.0455** | 0.0086 | ±0.0173 | **-5.274** | **1.33e-07** | *** |
| BMI (kg/m2) | -0.0232 | 0.0123 | ±0.0247 | -1.881 | 0.0599 | . |
| Hypertension | -0.2889 | 0.1883 | ±0.3766 | -1.535 | 0.1249 |  |
| High cholesterol | +0.0256 | 0.1826 | ±0.3651 | +0.140 | 0.8884 |  |
| Kidney disease | -0.2014 | 0.3797 | ±0.7595 | -0.530 | 0.5959 |  |
| Circulatory disease | +0.0069 | 0.2656 | ±0.5312 | +0.026 | 0.9794 |  |
| Avg. daily time < 70 (%) | +0.1158 | 0.1251 | ±0.2502 | +0.926 | 0.3546 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **890**, R² = **0.0778**, Adj R² = **0.0663**, F-statistic = **6.74** (p = **6.36e-11**), Residual SE = **2.528** on **878** df, AIC = **4188.7**, BIC = **4246.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2103** | 0.7088 | ±1.4177 | **+22.869** | **9.46e-116** | *** |
| Education: graduate level (vs college) | +0.2907 | 0.1778 | ±0.3557 | +1.634 | 0.1022 |  |
| **Education: high school or below (vs college)** | **-1.1175** | 0.3840 | ±0.7679 | **-2.910** | **0.0036** | ** |
| Site: UCSD (vs UAB) | +0.0135 | 0.2300 | ±0.4600 | +0.059 | 0.9533 |  |
| Site: UW (vs UAB) | +0.0290 | 0.2281 | ±0.4563 | +0.127 | 0.8987 |  |
| **Age (years)** | **-0.0447** | 0.0087 | ±0.0173 | **-5.162** | **2.45e-07** | *** |
| BMI (kg/m2) | -0.0218 | 0.0126 | ±0.0251 | -1.738 | 0.0823 | . |
| Hypertension | -0.2663 | 0.1904 | ±0.3809 | -1.398 | 0.1621 |  |
| High cholesterol | +0.0437 | 0.1840 | ±0.3680 | +0.238 | 0.8121 |  |
| Kidney disease | -0.1582 | 0.3758 | ±0.7516 | -0.421 | 0.6738 |  |
| Circulatory disease | +0.0346 | 0.2637 | ±0.5274 | +0.131 | 0.8957 |  |
| Time 181-250, pooled (%) | -0.0466 | 0.0376 | ±0.0753 | -1.239 | 0.2153 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **890**, R² = **0.0778**, Adj R² = **0.0662**, F-statistic = **6.73** (p = **6.49e-11**), Residual SE = **2.528** on **878** df, AIC = **4188.8**, BIC = **4246.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2096** | 0.7092 | ±1.4183 | **+22.858** | **1.22e-115** | *** |
| Education: graduate level (vs college) | +0.2902 | 0.1779 | ±0.3559 | +1.631 | 0.1029 |  |
| **Education: high school or below (vs college)** | **-1.1218** | 0.3836 | ±0.7672 | **-2.925** | **0.0034** | ** |
| Site: UCSD (vs UAB) | +0.0121 | 0.2298 | ±0.4595 | +0.053 | 0.9579 |  |
| Site: UW (vs UAB) | +0.0289 | 0.2282 | ±0.4565 | +0.126 | 0.8993 |  |
| **Age (years)** | **-0.0448** | 0.0087 | ±0.0173 | **-5.173** | **2.30e-07** | *** |
| BMI (kg/m2) | -0.0217 | 0.0126 | ±0.0252 | -1.729 | 0.0838 | . |
| Hypertension | -0.2665 | 0.1906 | ±0.3812 | -1.398 | 0.1620 |  |
| High cholesterol | +0.0441 | 0.1840 | ±0.3680 | +0.240 | 0.8105 |  |
| Kidney disease | -0.1559 | 0.3748 | ±0.7495 | -0.416 | 0.6774 |  |
| Circulatory disease | +0.0370 | 0.2635 | ±0.5271 | +0.140 | 0.8883 |  |
| Avg. daily time 181-250 (%) | -0.0473 | 0.0385 | ±0.0769 | -1.230 | 0.2186 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **890**, R² = **0.0778**, Adj R² = **0.0663**, F-statistic = **6.74** (p = **6.36e-11**), Residual SE = **2.528** on **878** df, AIC = **4188.7**, BIC = **4246.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2103** | 0.7088 | ±1.4177 | **+22.869** | **9.46e-116** | *** |
| Education: graduate level (vs college) | +0.2907 | 0.1778 | ±0.3557 | +1.634 | 0.1022 |  |
| **Education: high school or below (vs college)** | **-1.1175** | 0.3840 | ±0.7679 | **-2.910** | **0.0036** | ** |
| Site: UCSD (vs UAB) | +0.0135 | 0.2300 | ±0.4600 | +0.059 | 0.9533 |  |
| Site: UW (vs UAB) | +0.0290 | 0.2281 | ±0.4563 | +0.127 | 0.8987 |  |
| **Age (years)** | **-0.0447** | 0.0087 | ±0.0173 | **-5.162** | **2.45e-07** | *** |
| BMI (kg/m2) | -0.0218 | 0.0126 | ±0.0251 | -1.738 | 0.0823 | . |
| Hypertension | -0.2663 | 0.1904 | ±0.3809 | -1.398 | 0.1621 |  |
| High cholesterol | +0.0437 | 0.1840 | ±0.3680 | +0.238 | 0.8121 |  |
| Kidney disease | -0.1582 | 0.3758 | ±0.7516 | -0.421 | 0.6738 |  |
| Circulatory disease | +0.0346 | 0.2637 | ±0.5274 | +0.131 | 0.8957 |  |
| Time > 180 (%) | -0.0466 | 0.0376 | ±0.0753 | -1.239 | 0.2153 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **890**, R² = **0.0778**, Adj R² = **0.0662**, F-statistic = **6.73** (p = **6.49e-11**), Residual SE = **2.528** on **878** df, AIC = **4188.8**, BIC = **4246.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2096** | 0.7092 | ±1.4183 | **+22.858** | **1.22e-115** | *** |
| Education: graduate level (vs college) | +0.2902 | 0.1779 | ±0.3559 | +1.631 | 0.1029 |  |
| **Education: high school or below (vs college)** | **-1.1218** | 0.3836 | ±0.7672 | **-2.925** | **0.0034** | ** |
| Site: UCSD (vs UAB) | +0.0121 | 0.2298 | ±0.4595 | +0.053 | 0.9579 |  |
| Site: UW (vs UAB) | +0.0289 | 0.2282 | ±0.4565 | +0.126 | 0.8993 |  |
| **Age (years)** | **-0.0448** | 0.0087 | ±0.0173 | **-5.173** | **2.30e-07** | *** |
| BMI (kg/m2) | -0.0217 | 0.0126 | ±0.0252 | -1.729 | 0.0838 | . |
| Hypertension | -0.2665 | 0.1906 | ±0.3812 | -1.398 | 0.1620 |  |
| High cholesterol | +0.0441 | 0.1840 | ±0.3680 | +0.240 | 0.8105 |  |
| Kidney disease | -0.1559 | 0.3748 | ±0.7495 | -0.416 | 0.6774 |  |
| Circulatory disease | +0.0370 | 0.2635 | ±0.5271 | +0.140 | 0.8883 |  |
| Avg. daily time > 180 (%) | -0.0473 | 0.0385 | ±0.0769 | -1.230 | 0.2186 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 890)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **890**, R² = **0.0757**, Adj R² = **0.0641**, F-statistic = **6.53** (p = **1.57e-10**), Residual SE = **2.531** on **878** df, AIC = **4190.8**, BIC = **4248.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2009** | 0.7080 | ±1.4161 | **+22.882** | **7.09e-116** | *** |
| Education: graduate level (vs college) | +0.2807 | 0.1795 | ±0.3590 | +1.564 | 0.1179 |  |
| **Education: high school or below (vs college)** | **-1.1122** | 0.3843 | ±0.7686 | **-2.894** | **0.0038** | ** |
| Site: UCSD (vs UAB) | +0.0246 | 0.2340 | ±0.4680 | +0.105 | 0.9164 |  |
| Site: UW (vs UAB) | +0.0283 | 0.2296 | ±0.4593 | +0.123 | 0.9020 |  |
| **Age (years)** | **-0.0457** | 0.0086 | ±0.0173 | **-5.293** | **1.20e-07** | *** |
| BMI (kg/m2) | -0.0214 | 0.0125 | ±0.0250 | -1.709 | 0.0874 | . |
| Hypertension | -0.2950 | 0.1884 | ±0.3767 | -1.566 | 0.1173 |  |
| High cholesterol | +0.0493 | 0.1829 | ±0.3658 | +0.270 | 0.7873 |  |
| Kidney disease | -0.1845 | 0.3795 | ±0.7590 | -0.486 | 0.6269 |  |
| Circulatory disease | +0.0173 | 0.2636 | ±0.5272 | +0.066 | 0.9476 |  |
| Nocturnal time > 180 (%) | -0.0269 | 0.0279 | ±0.0558 | -0.963 | 0.3355 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
