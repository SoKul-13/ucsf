# Phase 6b model output tables - Within 54-250: no reading < 54 and none > 250 - Total analysis base

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models.


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


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 889; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **889**, R² = **0.0838**, Adj R² = **0.0733**, F-statistic = **8.03** (p = **1.79e-12**), Residual SE = **4.637** on **878** df, AIC = **5261.3**, BIC = **5314.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4156** | 1.2776 | ±2.5552 | **+6.587** | **4.49e-11** | *** |
| Education: graduate level (vs college) | -0.6325 | 0.3318 | ±0.6635 | -1.906 | 0.0566 | . |
| Education: high school or below (vs college) | +0.8848 | 0.6702 | ±1.3404 | +1.320 | 0.1868 |  |
| Site: UCSD (vs UAB) | -0.3348 | 0.4164 | ±0.8328 | -0.804 | 0.4213 |  |
| Site: UW (vs UAB) | +0.1650 | 0.4223 | ±0.8446 | +0.391 | 0.6959 |  |
| **Age (years)** | **-0.0867** | 0.0150 | ±0.0300 | **-5.774** | **7.76e-09** | *** |
| **BMI (kg/m2)** | **+0.0688** | 0.0250 | ±0.0500 | **+2.753** | **0.0059** | ** |
| Hypertension | +0.2493 | 0.3525 | ±0.7051 | +0.707 | 0.4795 |  |
| **High cholesterol** | **+0.7273** | 0.3274 | ±0.6548 | **+2.221** | **0.0263** | * |
| Kidney disease | +1.0851 | 0.6768 | ±1.3535 | +1.603 | 0.1089 |  |
| Circulatory disease | +0.7759 | 0.5319 | ±1.0638 | +1.459 | 0.1446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **889**, R² = **0.0844**, Adj R² = **0.0729**, F-statistic = **7.35** (p = **4.13e-12**), Residual SE = **4.638** on **877** df, AIC = **5262.8**, BIC = **5320.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.9049** | 2.4324 | ±4.8647 | **+4.072** | **4.66e-05** | *** |
| Education: graduate level (vs college) | -0.6321 | 0.3321 | ±0.6642 | -1.903 | 0.0570 | . |
| Education: high school or below (vs college) | +0.8995 | 0.6728 | ±1.3457 | +1.337 | 0.1812 |  |
| Site: UCSD (vs UAB) | -0.3404 | 0.4171 | ±0.8343 | -0.816 | 0.4145 |  |
| Site: UW (vs UAB) | +0.1598 | 0.4240 | ±0.8480 | +0.377 | 0.7063 |  |
| **Age (years)** | **-0.0861** | 0.0151 | ±0.0303 | **-5.692** | **1.26e-08** | *** |
| **BMI (kg/m2)** | **+0.0721** | 0.0255 | ±0.0509 | **+2.831** | **0.0046** | ** |
| Hypertension | +0.2853 | 0.3577 | ±0.7154 | +0.798 | 0.4251 |  |
| **High cholesterol** | **+0.7604** | 0.3271 | ±0.6541 | **+2.325** | **0.0201** | * |
| Kidney disease | +1.0809 | 0.6776 | ±1.3552 | +1.595 | 0.1107 |  |
| Circulatory disease | +0.7961 | 0.5327 | ±1.0653 | +1.494 | 0.1351 |  |
| HbA1c (%) | -0.2907 | 0.4140 | ±0.8281 | -0.702 | 0.4827 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **889**, R² = **0.0849**, Adj R² = **0.0734**, F-statistic = **7.40** (p = **3.27e-12**), Residual SE = **4.637** on **877** df, AIC = **5262.3**, BIC = **5319.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.9392** | 1.9121 | ±3.8243 | **+5.198** | **2.01e-07** | *** |
| Education: graduate level (vs college) | -0.6187 | 0.3329 | ±0.6657 | -1.859 | 0.0631 | . |
| Education: high school or below (vs college) | +0.8905 | 0.6692 | ±1.3385 | +1.331 | 0.1833 |  |
| Site: UCSD (vs UAB) | -0.3522 | 0.4152 | ±0.8303 | -0.848 | 0.3962 |  |
| Site: UW (vs UAB) | +0.1764 | 0.4233 | ±0.8465 | +0.417 | 0.6769 |  |
| **Age (years)** | **-0.0864** | 0.0150 | ±0.0301 | **-5.740** | **9.47e-09** | *** |
| **BMI (kg/m2)** | **+0.0719** | 0.0251 | ±0.0501 | **+2.867** | **0.0041** | ** |
| Hypertension | +0.2897 | 0.3555 | ±0.7110 | +0.815 | 0.4151 |  |
| **High cholesterol** | **+0.7331** | 0.3274 | ±0.6548 | **+2.239** | **0.0251** | * |
| Kidney disease | +1.1222 | 0.6736 | ±1.3472 | +1.666 | 0.0957 | . |
| Circulatory disease | +0.8069 | 0.5325 | ±1.0650 | +1.515 | 0.1297 |  |
| Mean glucose (mg/dL) | -0.0138 | 0.0133 | ±0.0266 | -1.036 | 0.3003 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **889**, R² = **0.0849**, Adj R² = **0.0734**, F-statistic = **7.40** (p = **3.27e-12**), Residual SE = **4.637** on **877** df, AIC = **5262.3**, BIC = **5319.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+11.8451** | 3.5040 | ±7.0080 | **+3.380** | **7.24e-04** | *** |
| Education: graduate level (vs college) | -0.6187 | 0.3329 | ±0.6657 | -1.859 | 0.0631 | . |
| Education: high school or below (vs college) | +0.8905 | 0.6692 | ±1.3385 | +1.331 | 0.1833 |  |
| Site: UCSD (vs UAB) | -0.3522 | 0.4152 | ±0.8303 | -0.848 | 0.3962 |  |
| Site: UW (vs UAB) | +0.1764 | 0.4233 | ±0.8465 | +0.417 | 0.6769 |  |
| **Age (years)** | **-0.0864** | 0.0150 | ±0.0301 | **-5.740** | **9.47e-09** | *** |
| **BMI (kg/m2)** | **+0.0719** | 0.0251 | ±0.0501 | **+2.867** | **0.0041** | ** |
| Hypertension | +0.2897 | 0.3555 | ±0.7110 | +0.815 | 0.4151 |  |
| **High cholesterol** | **+0.7331** | 0.3274 | ±0.6548 | **+2.239** | **0.0251** | * |
| Kidney disease | +1.1222 | 0.6736 | ±1.3472 | +1.666 | 0.0957 | . |
| Circulatory disease | +0.8069 | 0.5325 | ±1.0650 | +1.515 | 0.1297 |  |
| GMI (%) | -0.5758 | 0.5559 | ±1.1119 | -1.036 | 0.3003 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **889**, R² = **0.0838**, Adj R² = **0.0723**, F-statistic = **7.29** (p = **5.21e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.3**, BIC = **5320.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.6581** | 1.8016 | ±3.6032 | **+4.806** | **1.54e-06** | *** |
| Education: graduate level (vs college) | -0.6306 | 0.3333 | ±0.6665 | -1.892 | 0.0585 | . |
| Education: high school or below (vs college) | +0.8857 | 0.6714 | ±1.3428 | +1.319 | 0.1871 |  |
| Site: UCSD (vs UAB) | -0.3351 | 0.4168 | ±0.8336 | -0.804 | 0.4214 |  |
| Site: UW (vs UAB) | +0.1677 | 0.4239 | ±0.8478 | +0.396 | 0.6923 |  |
| **Age (years)** | **-0.0869** | 0.0150 | ±0.0300 | **-5.788** | **7.14e-09** | *** |
| **BMI (kg/m2)** | **+0.0698** | 0.0255 | ±0.0510 | **+2.736** | **0.0062** | ** |
| Hypertension | +0.2539 | 0.3528 | ±0.7055 | +0.720 | 0.4717 |  |
| **High cholesterol** | **+0.7306** | 0.3279 | ±0.6557 | **+2.228** | **0.0259** | * |
| Kidney disease | +1.0877 | 0.6765 | ±1.3531 | +1.608 | 0.1079 |  |
| Circulatory disease | +0.7812 | 0.5339 | ±1.0678 | +1.463 | 0.1434 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0022 | 0.0122 | ±0.0244 | -0.181 | 0.8563 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **889**, R² = **0.0840**, Adj R² = **0.0725**, F-statistic = **7.31** (p = **4.75e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.1**, BIC = **5320.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.7380** | 1.4133 | ±2.8266 | **+6.183** | **6.30e-10** | *** |
| Education: graduate level (vs college) | -0.6356 | 0.3317 | ±0.6634 | -1.916 | 0.0553 | . |
| Education: high school or below (vs college) | +0.9027 | 0.6738 | ±1.3476 | +1.340 | 0.1803 |  |
| Site: UCSD (vs UAB) | -0.3493 | 0.4163 | ±0.8326 | -0.839 | 0.4015 |  |
| Site: UW (vs UAB) | +0.1619 | 0.4226 | ±0.8452 | +0.383 | 0.7017 |  |
| **Age (years)** | **-0.0862** | 0.0151 | ±0.0301 | **-5.724** | **1.04e-08** | *** |
| **BMI (kg/m2)** | **+0.0694** | 0.0251 | ±0.0502 | **+2.767** | **0.0056** | ** |
| Hypertension | +0.2714 | 0.3571 | ±0.7142 | +0.760 | 0.4473 |  |
| **High cholesterol** | **+0.7304** | 0.3280 | ±0.6559 | **+2.227** | **0.0259** | * |
| Kidney disease | +1.1066 | 0.6760 | ±1.3519 | +1.637 | 0.1016 |  |
| Circulatory disease | +0.7840 | 0.5335 | ±1.0670 | +1.470 | 0.1416 |  |
| Glucose SD, pooled (mg/dL) | -0.0191 | 0.0383 | ±0.0765 | -0.498 | 0.6186 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **889**, R² = **0.0842**, Adj R² = **0.0727**, F-statistic = **7.33** (p = **4.47e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.0**, BIC = **5320.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.7841** | 1.3943 | ±2.7886 | **+6.300** | **2.98e-10** | *** |
| Education: graduate level (vs college) | -0.6341 | 0.3318 | ±0.6636 | -1.911 | 0.0560 | . |
| Education: high school or below (vs college) | +0.9043 | 0.6728 | ±1.3456 | +1.344 | 0.1789 |  |
| Site: UCSD (vs UAB) | -0.3515 | 0.4162 | ±0.8323 | -0.845 | 0.3983 |  |
| Site: UW (vs UAB) | +0.1632 | 0.4227 | ±0.8454 | +0.386 | 0.6994 |  |
| **Age (years)** | **-0.0861** | 0.0150 | ±0.0301 | **-5.719** | **1.07e-08** | *** |
| **BMI (kg/m2)** | **+0.0697** | 0.0251 | ±0.0502 | **+2.777** | **0.0055** | ** |
| Hypertension | +0.2777 | 0.3577 | ±0.7154 | +0.776 | 0.4376 |  |
| **High cholesterol** | **+0.7293** | 0.3278 | ±0.6556 | **+2.225** | **0.0261** | * |
| Kidney disease | +1.1095 | 0.6766 | ±1.3532 | +1.640 | 0.1010 |  |
| Circulatory disease | +0.7827 | 0.5331 | ±1.0663 | +1.468 | 0.1421 |  |
| Avg. daily SD (mg/dL) | -0.0243 | 0.0389 | ±0.0779 | -0.624 | 0.5327 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **889**, R² = **0.0838**, Adj R² = **0.0723**, F-statistic = **7.29** (p = **5.29e-12**), Residual SE = **4.640** on **877** df, AIC = **5263.3**, BIC = **5320.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4152** | 1.4958 | ±2.9915 | **+5.626** | **1.84e-08** | *** |
| Education: graduate level (vs college) | -0.6325 | 0.3318 | ±0.6636 | -1.906 | 0.0566 | . |
| Education: high school or below (vs college) | +0.8848 | 0.6723 | ±1.3445 | +1.316 | 0.1881 |  |
| Site: UCSD (vs UAB) | -0.3348 | 0.4173 | ±0.8346 | -0.802 | 0.4224 |  |
| Site: UW (vs UAB) | +0.1650 | 0.4230 | ±0.8459 | +0.390 | 0.6964 |  |
| **Age (years)** | **-0.0867** | 0.0150 | ±0.0301 | **-5.767** | **8.08e-09** | *** |
| **BMI (kg/m2)** | **+0.0688** | 0.0250 | ±0.0500 | **+2.751** | **0.0059** | ** |
| Hypertension | +0.2492 | 0.3546 | ±0.7092 | +0.703 | 0.4821 |  |
| **High cholesterol** | **+0.7273** | 0.3279 | ±0.6557 | **+2.218** | **0.0265** | * |
| Kidney disease | +1.0850 | 0.6760 | ±1.3520 | +1.605 | 0.1085 |  |
| Circulatory disease | +0.7759 | 0.5325 | ±1.0651 | +1.457 | 0.1451 |  |
| CV (%) | +0.0000 | 0.0518 | ±0.1037 | +0.001 | 0.9996 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **889**, R² = **0.0838**, Adj R² = **0.0723**, F-statistic = **7.29** (p = **5.27e-12**), Residual SE = **4.640** on **877** df, AIC = **5263.3**, BIC = **5320.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.5012** | 1.5676 | ±3.1352 | **+5.423** | **5.86e-08** | *** |
| Education: graduate level (vs college) | -0.6306 | 0.3320 | ±0.6640 | -1.900 | 0.0575 | . |
| Education: high school or below (vs college) | +0.8815 | 0.6717 | ±1.3434 | +1.312 | 0.1894 |  |
| Site: UCSD (vs UAB) | -0.3331 | 0.4171 | ±0.8342 | -0.799 | 0.4245 |  |
| Site: UW (vs UAB) | +0.1655 | 0.4227 | ±0.8454 | +0.392 | 0.6953 |  |
| **Age (years)** | **-0.0868** | 0.0151 | ±0.0301 | **-5.763** | **8.28e-09** | *** |
| **BMI (kg/m2)** | **+0.0688** | 0.0250 | ±0.0501 | **+2.750** | **0.0060** | ** |
| Hypertension | +0.2464 | 0.3538 | ±0.7075 | +0.697 | 0.4861 |  |
| **High cholesterol** | **+0.7272** | 0.3278 | ±0.6556 | **+2.218** | **0.0265** | * |
| Kidney disease | +1.0822 | 0.6756 | ±1.3512 | +1.602 | 0.1092 |  |
| Circulatory disease | +0.7762 | 0.5323 | ±1.0645 | +1.458 | 0.1447 |  |
| Mean / SD ratio | -0.0128 | 0.1279 | ±0.2559 | -0.100 | 0.9204 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **889**, R² = **0.0839**, Adj R² = **0.0724**, F-statistic = **7.30** (p = **5.06e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.2**, BIC = **5320.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.1441** | 1.5639 | ±3.1278 | **+5.207** | **1.91e-07** | *** |
| Education: graduate level (vs college) | -0.6375 | 0.3315 | ±0.6630 | -1.923 | 0.0545 | . |
| Education: high school or below (vs college) | +0.8940 | 0.6711 | ±1.3421 | +1.332 | 0.1828 |  |
| Site: UCSD (vs UAB) | -0.3396 | 0.4169 | ±0.8338 | -0.815 | 0.4153 |  |
| Site: UW (vs UAB) | +0.1646 | 0.4228 | ±0.8457 | +0.389 | 0.6970 |  |
| **Age (years)** | **-0.0864** | 0.0151 | ±0.0301 | **-5.739** | **9.51e-09** | *** |
| **BMI (kg/m2)** | **+0.0690** | 0.0251 | ±0.0501 | **+2.751** | **0.0059** | ** |
| Hypertension | +0.2581 | 0.3546 | ±0.7092 | +0.728 | 0.4667 |  |
| **High cholesterol** | **+0.7268** | 0.3278 | ±0.6556 | **+2.217** | **0.0266** | * |
| Kidney disease | +1.0942 | 0.6773 | ±1.3545 | +1.616 | 0.1062 |  |
| Circulatory disease | +0.7719 | 0.5312 | ±1.0624 | +1.453 | 0.1462 |  |
| Avg. daily mean/SD | +0.0345 | 0.1079 | ±0.2158 | +0.320 | 0.7488 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **889**, R² = **0.0858**, Adj R² = **0.0743**, F-statistic = **7.48** (p = **2.28e-12**), Residual SE = **4.635** on **877** df, AIC = **5261.4**, BIC = **5318.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.2244** | 1.4567 | ±2.9133 | **+4.960** | **7.06e-07** | *** |
| Education: graduate level (vs college) | -0.6338 | 0.3321 | ±0.6642 | -1.908 | 0.0563 | . |
| Education: high school or below (vs college) | +0.8312 | 0.6725 | ±1.3449 | +1.236 | 0.2165 |  |
| Site: UCSD (vs UAB) | -0.3219 | 0.4156 | ±0.8312 | -0.775 | 0.4386 |  |
| Site: UW (vs UAB) | +0.1791 | 0.4217 | ±0.8434 | +0.425 | 0.6710 |  |
| **Age (years)** | **-0.0863** | 0.0150 | ±0.0300 | **-5.744** | **9.25e-09** | *** |
| **BMI (kg/m2)** | **+0.0689** | 0.0249 | ±0.0498 | **+2.766** | **0.0057** | ** |
| Hypertension | +0.2587 | 0.3532 | ±0.7064 | +0.733 | 0.4639 |  |
| **High cholesterol** | **+0.7251** | 0.3277 | ±0.6554 | **+2.213** | **0.0269** | * |
| Kidney disease | +1.0607 | 0.6740 | ±1.3480 | +1.574 | 0.1155 |  |
| Circulatory disease | +0.7901 | 0.5335 | ±1.0669 | +1.481 | 0.1386 |  |
| MAG (mg/dL/h) | +0.0321 | 0.0229 | ±0.0458 | +1.405 | 0.1602 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **889**, R² = **0.0838**, Adj R² = **0.0723**, F-statistic = **7.30** (p = **5.15e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.3**, BIC = **5320.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.6073** | 1.4558 | ±2.9115 | **+5.913** | **3.37e-09** | *** |
| Education: graduate level (vs college) | -0.6318 | 0.3323 | ±0.6646 | -1.902 | 0.0572 | . |
| Education: high school or below (vs college) | +0.8931 | 0.6724 | ±1.3449 | +1.328 | 0.1841 |  |
| Site: UCSD (vs UAB) | -0.3398 | 0.4166 | ±0.8332 | -0.816 | 0.4147 |  |
| Site: UW (vs UAB) | +0.1647 | 0.4227 | ±0.8454 | +0.390 | 0.6969 |  |
| **Age (years)** | **-0.0865** | 0.0151 | ±0.0302 | **-5.737** | **9.66e-09** | *** |
| **BMI (kg/m2)** | **+0.0686** | 0.0250 | ±0.0501 | **+2.743** | **0.0061** | ** |
| Hypertension | +0.2565 | 0.3551 | ±0.7101 | +0.722 | 0.4701 |  |
| **High cholesterol** | **+0.7274** | 0.3278 | ±0.6555 | **+2.219** | **0.0265** | * |
| Kidney disease | +1.0931 | 0.6755 | ±1.3510 | +1.618 | 0.1056 |  |
| Circulatory disease | +0.7784 | 0.5330 | ±1.0659 | +1.461 | 0.1441 |  |
| Avg. daily range (mg/dL) | -0.0022 | 0.0089 | ±0.0178 | -0.251 | 0.8016 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **889**, R² = **0.0840**, Adj R² = **0.0725**, F-statistic = **7.31** (p = **4.83e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.1**, BIC = **5320.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2661** | 1.2950 | ±2.5900 | **+6.383** | **1.74e-10** | *** |
| Education: graduate level (vs college) | -0.6321 | 0.3319 | ±0.6639 | -1.904 | 0.0569 | . |
| Education: high school or below (vs college) | +0.8691 | 0.6769 | ±1.3538 | +1.284 | 0.1992 |  |
| Site: UCSD (vs UAB) | -0.3250 | 0.4180 | ±0.8359 | -0.778 | 0.4368 |  |
| Site: UW (vs UAB) | +0.1698 | 0.4228 | ±0.8457 | +0.402 | 0.6880 |  |
| **Age (years)** | **-0.0867** | 0.0150 | ±0.0301 | **-5.764** | **8.20e-09** | *** |
| **BMI (kg/m2)** | **+0.0678** | 0.0252 | ±0.0504 | **+2.693** | **0.0071** | ** |
| Hypertension | +0.2498 | 0.3528 | ±0.7057 | +0.708 | 0.4790 |  |
| **High cholesterol** | **+0.7147** | 0.3309 | ±0.6618 | **+2.160** | **0.0308** | * |
| Kidney disease | +1.0754 | 0.6749 | ±1.3498 | +1.593 | 0.1111 |  |
| Circulatory disease | +0.7585 | 0.5310 | ±1.0620 | +1.428 | 0.1532 |  |
| SD of daily means (mg/dL) | +0.0303 | 0.0668 | ±0.1337 | +0.453 | 0.6504 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **889**, R² = **0.0850**, Adj R² = **0.0735**, F-statistic = **7.41** (p = **3.13e-12**), Residual SE = **4.636** on **877** df, AIC = **5262.2**, BIC = **5319.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.3326 | 5.1609 | ±10.3218 | +0.646 | 0.5185 |  |
| Education: graduate level (vs college) | -0.6268 | 0.3318 | ±0.6636 | -1.889 | 0.0589 | . |
| Education: high school or below (vs college) | +0.9013 | 0.6712 | ±1.3424 | +1.343 | 0.1793 |  |
| Site: UCSD (vs UAB) | -0.3653 | 0.4145 | ±0.8289 | -0.881 | 0.3781 |  |
| Site: UW (vs UAB) | +0.1572 | 0.4221 | ±0.8443 | +0.372 | 0.7095 |  |
| **Age (years)** | **-0.0859** | 0.0150 | ±0.0301 | **-5.715** | **1.10e-08** | *** |
| **BMI (kg/m2)** | **+0.0704** | 0.0250 | ±0.0500 | **+2.817** | **0.0049** | ** |
| Hypertension | +0.2756 | 0.3562 | ±0.7123 | +0.774 | 0.4390 |  |
| **High cholesterol** | **+0.7447** | 0.3273 | ±0.6547 | **+2.275** | **0.0229** | * |
| Kidney disease | +1.1358 | 0.6744 | ±1.3488 | +1.684 | 0.0921 | . |
| Circulatory disease | +0.8106 | 0.5337 | ±1.0674 | +1.519 | 0.1288 |  |
| Time in range 70-180, pooled (%) | +0.0509 | 0.0499 | ±0.0998 | +1.020 | 0.3075 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **889**, R² = **0.0854**, Adj R² = **0.0739**, F-statistic = **7.44** (p = **2.66e-12**), Residual SE = **4.636** on **877** df, AIC = **5261.8**, BIC = **5319.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2.4705 | 5.1861 | ±10.3722 | +0.476 | 0.6338 |  |
| Education: graduate level (vs college) | -0.6269 | 0.3317 | ±0.6634 | -1.890 | 0.0588 | . |
| Education: high school or below (vs college) | +0.8985 | 0.6708 | ±1.3417 | +1.339 | 0.1805 |  |
| Site: UCSD (vs UAB) | -0.3699 | 0.4144 | ±0.8289 | -0.893 | 0.3721 |  |
| Site: UW (vs UAB) | +0.1563 | 0.4220 | ±0.8440 | +0.370 | 0.7111 |  |
| **Age (years)** | **-0.0858** | 0.0150 | ±0.0301 | **-5.714** | **1.11e-08** | *** |
| **BMI (kg/m2)** | **+0.0708** | 0.0250 | ±0.0500 | **+2.831** | **0.0046** | ** |
| Hypertension | +0.2791 | 0.3560 | ±0.7120 | +0.784 | 0.4331 |  |
| **High cholesterol** | **+0.7480** | 0.3273 | ±0.6546 | **+2.286** | **0.0223** | * |
| Kidney disease | +1.1460 | 0.6742 | ±1.3484 | +1.700 | 0.0892 | . |
| Circulatory disease | +0.8178 | 0.5336 | ±1.0672 | +1.533 | 0.1254 |  |
| Avg. daily time in range 70-180 (%) | +0.0595 | 0.0502 | ±0.1003 | +1.186 | 0.2355 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **889**, R² = **0.0842**, Adj R² = **0.0727**, F-statistic = **7.33** (p = **4.51e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.0**, BIC = **5320.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4667** | 1.2806 | ±2.5612 | **+6.611** | **3.81e-11** | *** |
| Education: graduate level (vs college) | -0.6480 | 0.3339 | ±0.6679 | -1.940 | 0.0523 | . |
| Education: high school or below (vs college) | +0.8711 | 0.6718 | ±1.3435 | +1.297 | 0.1947 |  |
| Site: UCSD (vs UAB) | -0.3283 | 0.4164 | ±0.8327 | -0.788 | 0.4305 |  |
| Site: UW (vs UAB) | +0.1609 | 0.4224 | ±0.8448 | +0.381 | 0.7033 |  |
| **Age (years)** | **-0.0866** | 0.0150 | ±0.0300 | **-5.766** | **8.11e-09** | *** |
| **BMI (kg/m2)** | **+0.0685** | 0.0250 | ±0.0501 | **+2.736** | **0.0062** | ** |
| Hypertension | +0.2463 | 0.3528 | ±0.7056 | +0.698 | 0.4851 |  |
| **High cholesterol** | **+0.7330** | 0.3278 | ±0.6556 | **+2.236** | **0.0254** | * |
| Kidney disease | +1.0777 | 0.6791 | ±1.3583 | +1.587 | 0.1126 |  |
| Circulatory disease | +0.7705 | 0.5314 | ±1.0628 | +1.450 | 0.1470 |  |
| Time 54-69, pooled (%) | -0.1954 | 0.3012 | ±0.6023 | -0.649 | 0.5164 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **889**, R² = **0.0841**, Adj R² = **0.0726**, F-statistic = **7.32** (p = **4.66e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.1**, BIC = **5320.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4544** | 1.2798 | ±2.5596 | **+6.606** | **3.95e-11** | *** |
| Education: graduate level (vs college) | -0.6468 | 0.3336 | ±0.6673 | -1.939 | 0.0525 | . |
| Education: high school or below (vs college) | +0.8711 | 0.6720 | ±1.3439 | +1.296 | 0.1948 |  |
| Site: UCSD (vs UAB) | -0.3252 | 0.4160 | ±0.8321 | -0.782 | 0.4344 |  |
| Site: UW (vs UAB) | +0.1627 | 0.4224 | ±0.8449 | +0.385 | 0.7002 |  |
| **Age (years)** | **-0.0866** | 0.0150 | ±0.0301 | **-5.760** | **8.41e-09** | *** |
| **BMI (kg/m2)** | **+0.0685** | 0.0250 | ±0.0501 | **+2.737** | **0.0062** | ** |
| Hypertension | +0.2466 | 0.3528 | ±0.7056 | +0.699 | 0.4845 |  |
| **High cholesterol** | **+0.7318** | 0.3279 | ±0.6558 | **+2.232** | **0.0256** | * |
| Kidney disease | +1.0782 | 0.6789 | ±1.3578 | +1.588 | 0.1123 |  |
| Circulatory disease | +0.7685 | 0.5318 | ±1.0636 | +1.445 | 0.1485 |  |
| Avg. daily time 54-69 (%) | -0.1679 | 0.3019 | ±0.6039 | -0.556 | 0.5781 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **889**, R² = **0.0842**, Adj R² = **0.0727**, F-statistic = **7.33** (p = **4.51e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.0**, BIC = **5320.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4667** | 1.2806 | ±2.5612 | **+6.611** | **3.81e-11** | *** |
| Education: graduate level (vs college) | -0.6480 | 0.3339 | ±0.6679 | -1.940 | 0.0523 | . |
| Education: high school or below (vs college) | +0.8711 | 0.6718 | ±1.3435 | +1.297 | 0.1947 |  |
| Site: UCSD (vs UAB) | -0.3283 | 0.4164 | ±0.8327 | -0.788 | 0.4305 |  |
| Site: UW (vs UAB) | +0.1609 | 0.4224 | ±0.8448 | +0.381 | 0.7033 |  |
| **Age (years)** | **-0.0866** | 0.0150 | ±0.0300 | **-5.766** | **8.11e-09** | *** |
| **BMI (kg/m2)** | **+0.0685** | 0.0250 | ±0.0501 | **+2.736** | **0.0062** | ** |
| Hypertension | +0.2463 | 0.3528 | ±0.7056 | +0.698 | 0.4851 |  |
| **High cholesterol** | **+0.7330** | 0.3278 | ±0.6556 | **+2.236** | **0.0254** | * |
| Kidney disease | +1.0777 | 0.6791 | ±1.3583 | +1.587 | 0.1126 |  |
| Circulatory disease | +0.7705 | 0.5314 | ±1.0628 | +1.450 | 0.1470 |  |
| Time < 70 (%) | -0.1954 | 0.3012 | ±0.6023 | -0.649 | 0.5164 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **889**, R² = **0.0841**, Adj R² = **0.0726**, F-statistic = **7.32** (p = **4.66e-12**), Residual SE = **4.639** on **877** df, AIC = **5263.1**, BIC = **5320.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4544** | 1.2798 | ±2.5596 | **+6.606** | **3.95e-11** | *** |
| Education: graduate level (vs college) | -0.6468 | 0.3336 | ±0.6673 | -1.939 | 0.0525 | . |
| Education: high school or below (vs college) | +0.8711 | 0.6720 | ±1.3439 | +1.296 | 0.1948 |  |
| Site: UCSD (vs UAB) | -0.3252 | 0.4160 | ±0.8321 | -0.782 | 0.4344 |  |
| Site: UW (vs UAB) | +0.1627 | 0.4224 | ±0.8449 | +0.385 | 0.7002 |  |
| **Age (years)** | **-0.0866** | 0.0150 | ±0.0301 | **-5.760** | **8.41e-09** | *** |
| **BMI (kg/m2)** | **+0.0685** | 0.0250 | ±0.0501 | **+2.737** | **0.0062** | ** |
| Hypertension | +0.2466 | 0.3528 | ±0.7056 | +0.699 | 0.4845 |  |
| **High cholesterol** | **+0.7318** | 0.3279 | ±0.6558 | **+2.232** | **0.0256** | * |
| Kidney disease | +1.0782 | 0.6789 | ±1.3578 | +1.588 | 0.1123 |  |
| Circulatory disease | +0.7685 | 0.5318 | ±1.0636 | +1.445 | 0.1485 |  |
| Avg. daily time < 70 (%) | -0.1679 | 0.3019 | ±0.6039 | -0.556 | 0.5781 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **889**, R² = **0.0848**, Adj R² = **0.0733**, F-statistic = **7.39** (p = **3.42e-12**), Residual SE = **4.637** on **877** df, AIC = **5262.4**, BIC = **5319.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4113** | 1.2769 | ±2.5538 | **+6.587** | **4.48e-11** | *** |
| Education: graduate level (vs college) | -0.6237 | 0.3321 | ±0.6642 | -1.878 | 0.0604 | . |
| Education: high school or below (vs college) | +0.9030 | 0.6715 | ±1.3431 | +1.345 | 0.1787 |  |
| Site: UCSD (vs UAB) | -0.3640 | 0.4145 | ±0.8290 | -0.878 | 0.3799 |  |
| Site: UW (vs UAB) | +0.1590 | 0.4222 | ±0.8445 | +0.376 | 0.7066 |  |
| **Age (years)** | **-0.0860** | 0.0150 | ±0.0301 | **-5.721** | **1.06e-08** | *** |
| **BMI (kg/m2)** | **+0.0704** | 0.0250 | ±0.0500 | **+2.813** | **0.0049** | ** |
| Hypertension | +0.2738 | 0.3561 | ±0.7123 | +0.769 | 0.4419 |  |
| **High cholesterol** | **+0.7417** | 0.3274 | ±0.6547 | **+2.266** | **0.0235** | * |
| Kidney disease | +1.1327 | 0.6750 | ±1.3499 | +1.678 | 0.0933 | . |
| Circulatory disease | +0.8086 | 0.5341 | ±1.0681 | +1.514 | 0.1300 |  |
| Time 181-250, pooled (%) | -0.0461 | 0.0495 | ±0.0990 | -0.931 | 0.3520 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **889**, R² = **0.0852**, Adj R² = **0.0737**, F-statistic = **7.42** (p = **2.93e-12**), Residual SE = **4.636** on **877** df, AIC = **5262.0**, BIC = **5319.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4089** | 1.2769 | ±2.5538 | **+6.585** | **4.54e-11** | *** |
| Education: graduate level (vs college) | -0.6227 | 0.3319 | ±0.6639 | -1.876 | 0.0607 | . |
| Education: high school or below (vs college) | +0.9018 | 0.6711 | ±1.3421 | +1.344 | 0.1790 |  |
| Site: UCSD (vs UAB) | -0.3702 | 0.4144 | ±0.8289 | -0.893 | 0.3717 |  |
| Site: UW (vs UAB) | +0.1578 | 0.4221 | ±0.8441 | +0.374 | 0.7085 |  |
| **Age (years)** | **-0.0860** | 0.0150 | ±0.0300 | **-5.722** | **1.05e-08** | *** |
| **BMI (kg/m2)** | **+0.0707** | 0.0250 | ±0.0500 | **+2.828** | **0.0047** | ** |
| Hypertension | +0.2775 | 0.3560 | ±0.7119 | +0.780 | 0.4357 |  |
| **High cholesterol** | **+0.7448** | 0.3273 | ±0.6546 | **+2.276** | **0.0229** | * |
| Kidney disease | +1.1432 | 0.6748 | ±1.3496 | +1.694 | 0.0902 | . |
| Circulatory disease | +0.8168 | 0.5341 | ±1.0682 | +1.529 | 0.1262 |  |
| Avg. daily time 181-250 (%) | -0.0547 | 0.0498 | ±0.0995 | -1.099 | 0.2719 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **889**, R² = **0.0848**, Adj R² = **0.0733**, F-statistic = **7.39** (p = **3.42e-12**), Residual SE = **4.637** on **877** df, AIC = **5262.4**, BIC = **5319.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4113** | 1.2769 | ±2.5538 | **+6.587** | **4.48e-11** | *** |
| Education: graduate level (vs college) | -0.6237 | 0.3321 | ±0.6642 | -1.878 | 0.0604 | . |
| Education: high school or below (vs college) | +0.9030 | 0.6715 | ±1.3431 | +1.345 | 0.1787 |  |
| Site: UCSD (vs UAB) | -0.3640 | 0.4145 | ±0.8290 | -0.878 | 0.3799 |  |
| Site: UW (vs UAB) | +0.1590 | 0.4222 | ±0.8445 | +0.376 | 0.7066 |  |
| **Age (years)** | **-0.0860** | 0.0150 | ±0.0301 | **-5.721** | **1.06e-08** | *** |
| **BMI (kg/m2)** | **+0.0704** | 0.0250 | ±0.0500 | **+2.813** | **0.0049** | ** |
| Hypertension | +0.2738 | 0.3561 | ±0.7123 | +0.769 | 0.4419 |  |
| **High cholesterol** | **+0.7417** | 0.3274 | ±0.6547 | **+2.266** | **0.0235** | * |
| Kidney disease | +1.1327 | 0.6750 | ±1.3499 | +1.678 | 0.0933 | . |
| Circulatory disease | +0.8086 | 0.5341 | ±1.0681 | +1.514 | 0.1300 |  |
| Time > 180 (%) | -0.0461 | 0.0495 | ±0.0990 | -0.931 | 0.3520 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **889**, R² = **0.0852**, Adj R² = **0.0737**, F-statistic = **7.42** (p = **2.93e-12**), Residual SE = **4.636** on **877** df, AIC = **5262.0**, BIC = **5319.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4089** | 1.2769 | ±2.5538 | **+6.585** | **4.54e-11** | *** |
| Education: graduate level (vs college) | -0.6227 | 0.3319 | ±0.6639 | -1.876 | 0.0607 | . |
| Education: high school or below (vs college) | +0.9018 | 0.6711 | ±1.3421 | +1.344 | 0.1790 |  |
| Site: UCSD (vs UAB) | -0.3702 | 0.4144 | ±0.8289 | -0.893 | 0.3717 |  |
| Site: UW (vs UAB) | +0.1578 | 0.4221 | ±0.8441 | +0.374 | 0.7085 |  |
| **Age (years)** | **-0.0860** | 0.0150 | ±0.0300 | **-5.722** | **1.05e-08** | *** |
| **BMI (kg/m2)** | **+0.0707** | 0.0250 | ±0.0500 | **+2.828** | **0.0047** | ** |
| Hypertension | +0.2775 | 0.3560 | ±0.7119 | +0.780 | 0.4357 |  |
| **High cholesterol** | **+0.7448** | 0.3273 | ±0.6546 | **+2.276** | **0.0229** | * |
| Kidney disease | +1.1432 | 0.6748 | ±1.3496 | +1.694 | 0.0902 | . |
| Circulatory disease | +0.8168 | 0.5341 | ±1.0682 | +1.529 | 0.1262 |  |
| Avg. daily time > 180 (%) | -0.0547 | 0.0498 | ±0.0995 | -1.099 | 0.2719 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **889**, R² = **0.0858**, Adj R² = **0.0744**, F-statistic = **7.49** (p = **2.19e-12**), Residual SE = **4.634** on **877** df, AIC = **5261.3**, BIC = **5318.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4470** | 1.2799 | ±2.5598 | **+6.600** | **4.12e-11** | *** |
| Education: graduate level (vs college) | -0.6300 | 0.3317 | ±0.6634 | -1.899 | 0.0575 | . |
| Education: high school or below (vs college) | +0.8313 | 0.6773 | ±1.3546 | +1.227 | 0.2197 |  |
| Site: UCSD (vs UAB) | -0.2936 | 0.4172 | ±0.8344 | -0.704 | 0.4815 |  |
| Site: UW (vs UAB) | +0.1805 | 0.4221 | ±0.8442 | +0.428 | 0.6689 |  |
| **Age (years)** | **-0.0861** | 0.0151 | ±0.0302 | **-5.708** | **1.14e-08** | *** |
| **BMI (kg/m2)** | **+0.0643** | 0.0252 | ±0.0504 | **+2.550** | **0.0108** | * |
| Hypertension | +0.2580 | 0.3528 | ±0.7057 | +0.731 | 0.4646 |  |
| **High cholesterol** | **+0.6817** | 0.3290 | ±0.6581 | **+2.072** | **0.0383** | * |
| Kidney disease | +1.0359 | 0.6858 | ±1.3715 | +1.511 | 0.1309 |  |
| Circulatory disease | +0.7405 | 0.5372 | ±1.0744 | +1.379 | 0.1680 |  |
| Nocturnal time > 180 (%) | +0.0603 | 0.0514 | ±0.1029 | +1.173 | 0.2409 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 889; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0666**, LLR χ² = **54.79** (p = **3.46e-08**), AUC = **0.6769**, AIC = **789.9**, BIC = **842.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2484 | 0.7192 | ±1.4383 | -0.345 | 0.7298 | 0.7800 |  |
| Education: graduate level (vs college) | -0.1145 | 0.2033 | ±0.4066 | -0.563 | 0.5734 | 0.8918 |  |
| Education: high school or below (vs college) | +0.4034 | 0.2851 | ±0.5702 | +1.415 | 0.1571 | 1.4969 |  |
| Site: UCSD (vs UAB) | -0.0951 | 0.2475 | ±0.4951 | -0.384 | 0.7009 | 0.9093 |  |
| Site: UW (vs UAB) | +0.2127 | 0.2324 | ±0.4648 | +0.915 | 0.3600 | 1.2370 |  |
| **Age (years)** | **-0.0450** | 0.0092 | ±0.0184 | **-4.888** | **1.02e-06** | 0.9560 | *** |
| **BMI (kg/m2)** | **+0.0287** | 0.0128 | ±0.0256 | **+2.244** | **0.0248** | 1.0291 | * |
| Hypertension | +0.1567 | 0.2039 | ±0.4078 | +0.769 | 0.4421 | 1.1696 |  |
| **High cholesterol** | **+0.5100** | 0.1932 | ±0.3863 | **+2.640** | **0.0083** | 1.6653 | ** |
| Kidney disease | +0.5648 | 0.3035 | ±0.6069 | +1.861 | 0.0627 | 1.7591 | . |
| Circulatory disease | +0.2961 | 0.2678 | ±0.5356 | +1.106 | 0.2688 | 1.3446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0669**, LLR χ² = **55.08** (p = **7.50e-08**), AUC = **0.6776**, AIC = **791.6**, BIC = **849.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3687 | 1.3558 | ±2.7116 | +0.272 | 0.7857 | 1.4458 |  |
| Education: graduate level (vs college) | -0.1157 | 0.2034 | ±0.4068 | -0.569 | 0.5695 | 0.8907 |  |
| Education: high school or below (vs college) | +0.4087 | 0.2853 | ±0.5706 | +1.432 | 0.1521 | 1.5048 |  |
| Site: UCSD (vs UAB) | -0.1008 | 0.2477 | ±0.4953 | -0.407 | 0.6840 | 0.9041 |  |
| Site: UW (vs UAB) | +0.2118 | 0.2322 | ±0.4644 | +0.912 | 0.3617 | 1.2359 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0184 | **-4.872** | **1.10e-06** | 0.9561 | *** |
| **BMI (kg/m2)** | **+0.0301** | 0.0130 | ±0.0260 | **+2.314** | **0.0206** | 1.0305 | * |
| Hypertension | +0.1746 | 0.2065 | ±0.4130 | +0.846 | 0.3978 | 1.1908 |  |
| **High cholesterol** | **+0.5264** | 0.1957 | ±0.3913 | **+2.690** | **0.0071** | 1.6927 | ** |
| Kidney disease | +0.5643 | 0.3037 | ±0.6075 | +1.858 | 0.0632 | 1.7582 | . |
| Circulatory disease | +0.3064 | 0.2682 | ±0.5364 | +1.142 | 0.2533 | 1.3585 |  |
| HbA1c (%) | -0.1198 | 0.2234 | ±0.4468 | -0.536 | 0.5918 | 0.8871 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0672**, LLR χ² = **55.30** (p = **6.82e-08**), AUC = **0.6783**, AIC = **791.4**, BIC = **848.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8575 | 1.1111 | ±2.2223 | -0.772 | 0.4403 | 0.4242 |  |
| Education: graduate level (vs college) | -0.1186 | 0.2035 | ±0.4071 | -0.583 | 0.5601 | 0.8882 |  |
| Education: high school or below (vs college) | +0.4050 | 0.2848 | ±0.5696 | +1.422 | 0.1550 | 1.4994 |  |
| Site: UCSD (vs UAB) | -0.0859 | 0.2480 | ±0.4959 | -0.346 | 0.7290 | 0.9177 |  |
| Site: UW (vs UAB) | +0.2080 | 0.2325 | ±0.4649 | +0.895 | 0.3708 | 1.2313 |  |
| **Age (years)** | **-0.0452** | 0.0092 | ±0.0184 | **-4.901** | **9.55e-07** | 0.9558 | *** |
| **BMI (kg/m2)** | **+0.0275** | 0.0129 | ±0.0258 | **+2.126** | **0.0335** | 1.0279 | * |
| Hypertension | +0.1425 | 0.2048 | ±0.4096 | +0.696 | 0.4864 | 1.1532 |  |
| **High cholesterol** | **+0.5037** | 0.1933 | ±0.3866 | **+2.606** | **0.0092** | 1.6548 | ** |
| Kidney disease | +0.5487 | 0.3041 | ±0.6082 | +1.804 | 0.0712 | 1.7310 | . |
| Circulatory disease | +0.2833 | 0.2686 | ±0.5372 | +1.055 | 0.2915 | 1.3275 |  |
| Mean glucose (mg/dL) | +0.0055 | 0.0076 | ±0.0152 | +0.720 | 0.4716 | 1.0055 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0672**, LLR χ² = **55.30** (p = **6.82e-08**), AUC = **0.6783**, AIC = **791.4**, BIC = **848.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6158 | 2.0315 | ±4.0631 | -0.795 | 0.4264 | 0.1987 |  |
| Education: graduate level (vs college) | -0.1186 | 0.2035 | ±0.4071 | -0.583 | 0.5601 | 0.8882 |  |
| Education: high school or below (vs college) | +0.4050 | 0.2848 | ±0.5696 | +1.422 | 0.1550 | 1.4994 |  |
| Site: UCSD (vs UAB) | -0.0859 | 0.2480 | ±0.4959 | -0.346 | 0.7290 | 0.9177 |  |
| Site: UW (vs UAB) | +0.2080 | 0.2325 | ±0.4649 | +0.895 | 0.3708 | 1.2313 |  |
| **Age (years)** | **-0.0452** | 0.0092 | ±0.0184 | **-4.901** | **9.55e-07** | 0.9558 | *** |
| **BMI (kg/m2)** | **+0.0275** | 0.0129 | ±0.0258 | **+2.126** | **0.0335** | 1.0279 | * |
| Hypertension | +0.1425 | 0.2048 | ±0.4096 | +0.696 | 0.4864 | 1.1532 |  |
| **High cholesterol** | **+0.5037** | 0.1933 | ±0.3866 | **+2.606** | **0.0092** | 1.6548 | ** |
| Kidney disease | +0.5487 | 0.3041 | ±0.6082 | +1.804 | 0.0712 | 1.7310 | . |
| Circulatory disease | +0.2833 | 0.2686 | ±0.5372 | +1.055 | 0.2915 | 1.3275 |  |
| GMI (%) | +0.2291 | 0.3183 | ±0.6366 | +0.720 | 0.4716 | 1.2575 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0716**, LLR χ² = **58.94** (p = **1.46e-08**), AUC = **0.6858**, AIC = **787.8**, BIC = **845.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.7767 | 1.0417 | ±2.0834 | -1.706 | 0.0881 | 0.1692 | . |
| Education: graduate level (vs college) | -0.1237 | 0.2041 | ±0.4081 | -0.606 | 0.5444 | 0.8836 |  |
| Education: high school or below (vs college) | +0.4058 | 0.2852 | ±0.5703 | +1.423 | 0.1547 | 1.5005 |  |
| Site: UCSD (vs UAB) | -0.0867 | 0.2482 | ±0.4964 | -0.349 | 0.7268 | 0.9169 |  |
| Site: UW (vs UAB) | +0.1968 | 0.2330 | ±0.4659 | +0.845 | 0.3983 | 1.2175 |  |
| **Age (years)** | **-0.0442** | 0.0092 | ±0.0185 | **-4.785** | **1.71e-06** | 0.9568 | *** |
| BMI (kg/m2) | +0.0235 | 0.0133 | ±0.0265 | +1.769 | 0.0770 | 1.0238 | . |
| Hypertension | +0.1301 | 0.2042 | ±0.4085 | +0.637 | 0.5242 | 1.1389 |  |
| **High cholesterol** | **+0.4839** | 0.1938 | ±0.3877 | **+2.496** | **0.0126** | 1.6224 | * |
| Kidney disease | +0.5523 | 0.3036 | ±0.6071 | +1.819 | 0.0689 | 1.7372 | . |
| Circulatory disease | +0.2625 | 0.2693 | ±0.5385 | +0.975 | 0.3295 | 1.3002 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0137** | 0.0067 | ±0.0134 | **+2.045** | **0.0409** | 1.0138 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0666**, LLR χ² = **54.80** (p = **8.44e-08**), AUC = **0.6773**, AIC = **791.9**, BIC = **849.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2872 | 0.8182 | ±1.6364 | -0.351 | 0.7256 | 0.7504 |  |
| Education: graduate level (vs college) | -0.1141 | 0.2033 | ±0.4067 | -0.561 | 0.5746 | 0.8921 |  |
| Education: high school or below (vs college) | +0.4013 | 0.2859 | ±0.5718 | +1.404 | 0.1604 | 1.4938 |  |
| Site: UCSD (vs UAB) | -0.0927 | 0.2487 | ±0.4975 | -0.373 | 0.7095 | 0.9115 |  |
| Site: UW (vs UAB) | +0.2137 | 0.2326 | ±0.4653 | +0.919 | 0.3583 | 1.2383 |  |
| **Age (years)** | **-0.0451** | 0.0092 | ±0.0185 | **-4.885** | **1.04e-06** | 0.9559 | *** |
| **BMI (kg/m2)** | **+0.0286** | 0.0128 | ±0.0256 | **+2.235** | **0.0254** | 1.0290 | * |
| Hypertension | +0.1542 | 0.2055 | ±0.4109 | +0.750 | 0.4530 | 1.1667 |  |
| **High cholesterol** | **+0.5091** | 0.1933 | ±0.3867 | **+2.633** | **0.0085** | 1.6639 | ** |
| Kidney disease | +0.5622 | 0.3045 | ±0.6091 | +1.846 | 0.0649 | 1.7545 | . |
| Circulatory disease | +0.2953 | 0.2679 | ±0.5358 | +1.102 | 0.2704 | 1.3435 |  |
| Glucose SD, pooled (mg/dL) | +0.0023 | 0.0228 | ±0.0455 | +0.099 | 0.9208 | 1.0023 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0666**, LLR χ² = **54.80** (p = **8.44e-08**), AUC = **0.6772**, AIC = **791.9**, BIC = **849.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2839 | 0.8024 | ±1.6049 | -0.354 | 0.7235 | 0.7529 |  |
| Education: graduate level (vs college) | -0.1143 | 0.2033 | ±0.4066 | -0.562 | 0.5739 | 0.8920 |  |
| Education: high school or below (vs college) | +0.4016 | 0.2857 | ±0.5713 | +1.406 | 0.1598 | 1.4942 |  |
| Site: UCSD (vs UAB) | -0.0930 | 0.2484 | ±0.4968 | -0.374 | 0.7081 | 0.9112 |  |
| Site: UW (vs UAB) | +0.2133 | 0.2325 | ±0.4649 | +0.917 | 0.3589 | 1.2377 |  |
| **Age (years)** | **-0.0451** | 0.0092 | ±0.0185 | **-4.884** | **1.04e-06** | 0.9559 | *** |
| **BMI (kg/m2)** | **+0.0286** | 0.0128 | ±0.0256 | **+2.233** | **0.0255** | 1.0290 | * |
| Hypertension | +0.1541 | 0.2056 | ±0.4111 | +0.750 | 0.4535 | 1.1666 |  |
| **High cholesterol** | **+0.5094** | 0.1932 | ±0.3865 | **+2.636** | **0.0084** | 1.6643 | ** |
| Kidney disease | +0.5624 | 0.3044 | ±0.6088 | +1.848 | 0.0647 | 1.7549 | . |
| Circulatory disease | +0.2957 | 0.2678 | ±0.5356 | +1.104 | 0.2695 | 1.3441 |  |
| Avg. daily SD (mg/dL) | +0.0023 | 0.0233 | ±0.0465 | +0.100 | 0.9206 | 1.0023 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0667**, LLR χ² = **54.87** (p = **8.20e-08**), AUC = **0.6761**, AIC = **791.9**, BIC = **849.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1063 | 0.8795 | ±1.7590 | -0.121 | 0.9038 | 0.8991 |  |
| Education: graduate level (vs college) | -0.1170 | 0.2035 | ±0.4070 | -0.575 | 0.5655 | 0.8896 |  |
| Education: high school or below (vs college) | +0.4106 | 0.2863 | ±0.5726 | +1.434 | 0.1515 | 1.5078 |  |
| Site: UCSD (vs UAB) | -0.1011 | 0.2484 | ±0.4968 | -0.407 | 0.6841 | 0.9039 |  |
| Site: UW (vs UAB) | +0.2084 | 0.2328 | ±0.4656 | +0.895 | 0.3707 | 1.2317 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0185 | **-4.861** | **1.17e-06** | 0.9561 | *** |
| **BMI (kg/m2)** | **+0.0286** | 0.0128 | ±0.0256 | **+2.241** | **0.0250** | 1.0291 | * |
| Hypertension | +0.1620 | 0.2047 | ±0.4095 | +0.791 | 0.4287 | 1.1759 |  |
| **High cholesterol** | **+0.5111** | 0.1932 | ±0.3864 | **+2.645** | **0.0082** | 1.6670 | ** |
| Kidney disease | +0.5699 | 0.3041 | ±0.6081 | +1.874 | 0.0609 | 1.7681 | . |
| Circulatory disease | +0.2957 | 0.2678 | ±0.5356 | +1.104 | 0.2695 | 1.3440 |  |
| CV (%) | -0.0092 | 0.0326 | ±0.0653 | -0.281 | 0.7791 | 0.9909 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0666**, LLR χ² = **54.79** (p = **8.45e-08**), AUC = **0.6768**, AIC = **791.9**, BIC = **849.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2882 | 0.9010 | ±1.8021 | -0.320 | 0.7491 | 0.7496 |  |
| Education: graduate level (vs college) | -0.1153 | 0.2036 | ±0.4072 | -0.566 | 0.5713 | 0.8911 |  |
| Education: high school or below (vs college) | +0.4052 | 0.2861 | ±0.5723 | +1.416 | 0.1568 | 1.4995 |  |
| Site: UCSD (vs UAB) | -0.0962 | 0.2480 | ±0.4960 | -0.388 | 0.6981 | 0.9083 |  |
| Site: UW (vs UAB) | +0.2119 | 0.2326 | ±0.4652 | +0.911 | 0.3623 | 1.2360 |  |
| **Age (years)** | **-0.0450** | 0.0092 | ±0.0185 | **-4.875** | **1.09e-06** | 0.9560 | *** |
| **BMI (kg/m2)** | **+0.0287** | 0.0128 | ±0.0256 | **+2.244** | **0.0248** | 1.0291 | * |
| Hypertension | +0.1580 | 0.2047 | ±0.4094 | +0.772 | 0.4401 | 1.1712 |  |
| **High cholesterol** | **+0.5102** | 0.1932 | ±0.3864 | **+2.641** | **0.0083** | 1.6656 | ** |
| Kidney disease | +0.5661 | 0.3040 | ±0.6080 | +1.862 | 0.0626 | 1.7614 | . |
| Circulatory disease | +0.2957 | 0.2678 | ±0.5357 | +1.104 | 0.2695 | 1.3441 |  |
| Mean / SD ratio | +0.0060 | 0.0814 | ±0.1629 | +0.073 | 0.9416 | 1.0060 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0667**, LLR χ² = **54.85** (p = **8.26e-08**), AUC = **0.6765**, AIC = **791.9**, BIC = **849.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3751 | 0.8809 | ±1.7617 | -0.426 | 0.6702 | 0.6872 |  |
| Education: graduate level (vs college) | -0.1167 | 0.2035 | ±0.4071 | -0.574 | 0.5662 | 0.8898 |  |
| Education: high school or below (vs college) | +0.4083 | 0.2858 | ±0.5716 | +1.429 | 0.1531 | 1.5043 |  |
| Site: UCSD (vs UAB) | -0.0977 | 0.2477 | ±0.4955 | -0.394 | 0.6934 | 0.9070 |  |
| Site: UW (vs UAB) | +0.2113 | 0.2324 | ±0.4648 | +0.909 | 0.3633 | 1.2353 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0185 | **-4.858** | **1.19e-06** | 0.9561 | *** |
| **BMI (kg/m2)** | **+0.0287** | 0.0128 | ±0.0256 | **+2.249** | **0.0245** | 1.0292 | * |
| Hypertension | +0.1608 | 0.2045 | ±0.4090 | +0.786 | 0.4318 | 1.1744 |  |
| **High cholesterol** | **+0.5100** | 0.1931 | ±0.3863 | **+2.641** | **0.0083** | 1.6653 | ** |
| Kidney disease | +0.5691 | 0.3040 | ±0.6079 | +1.872 | 0.0612 | 1.7668 | . |
| Circulatory disease | +0.2932 | 0.2681 | ±0.5361 | +1.094 | 0.2740 | 1.3407 |  |
| Avg. daily mean/SD | +0.0161 | 0.0645 | ±0.1291 | +0.249 | 0.8031 | 1.0162 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0705**, LLR χ² = **58.00** (p = **2.18e-08**), AUC = **0.6862**, AIC = **788.7**, BIC = **846.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.1547 | 0.8835 | ±1.7670 | -1.307 | 0.1912 | 0.3151 |  |
| Education: graduate level (vs college) | -0.1093 | 0.2039 | ±0.4078 | -0.536 | 0.5919 | 0.8965 |  |
| Education: high school or below (vs college) | +0.3673 | 0.2866 | ±0.5732 | +1.282 | 0.1999 | 1.4439 |  |
| Site: UCSD (vs UAB) | -0.0813 | 0.2483 | ±0.4966 | -0.327 | 0.7435 | 0.9220 |  |
| Site: UW (vs UAB) | +0.2224 | 0.2328 | ±0.4656 | +0.955 | 0.3394 | 1.2490 |  |
| **Age (years)** | **-0.0448** | 0.0092 | ±0.0185 | **-4.852** | **1.22e-06** | 0.9562 | *** |
| **BMI (kg/m2)** | **+0.0286** | 0.0129 | ±0.0258 | **+2.218** | **0.0265** | 1.0290 | * |
| Hypertension | +0.1637 | 0.2043 | ±0.4085 | +0.802 | 0.4228 | 1.1779 |  |
| **High cholesterol** | **+0.5155** | 0.1940 | ±0.3880 | **+2.657** | **0.0079** | 1.6745 | ** |
| Kidney disease | +0.5489 | 0.3041 | ±0.6082 | +1.805 | 0.0711 | 1.7313 | . |
| Circulatory disease | +0.3102 | 0.2685 | ±0.5370 | +1.155 | 0.2479 | 1.3637 |  |
| MAG (mg/dL/h) | +0.0242 | 0.0135 | ±0.0269 | +1.797 | 0.0723 | 1.0245 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0667**, LLR χ² = **54.90** (p = **8.09e-08**), AUC = **0.6774**, AIC = **791.8**, BIC = **849.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4055 | 0.8602 | ±1.7204 | -0.471 | 0.6374 | 0.6666 |  |
| Education: graduate level (vs college) | -0.1150 | 0.2034 | ±0.4067 | -0.565 | 0.5717 | 0.8914 |  |
| Education: high school or below (vs college) | +0.3967 | 0.2858 | ±0.5715 | +1.388 | 0.1651 | 1.4869 |  |
| Site: UCSD (vs UAB) | -0.0889 | 0.2483 | ±0.4965 | -0.358 | 0.7202 | 0.9149 |  |
| Site: UW (vs UAB) | +0.2143 | 0.2325 | ±0.4650 | +0.922 | 0.3566 | 1.2390 |  |
| **Age (years)** | **-0.0452** | 0.0092 | ±0.0185 | **-4.899** | **9.65e-07** | 0.9558 | *** |
| **BMI (kg/m2)** | **+0.0288** | 0.0128 | ±0.0256 | **+2.253** | **0.0243** | 1.0292 | * |
| Hypertension | +0.1510 | 0.2046 | ±0.4093 | +0.738 | 0.4606 | 1.1630 |  |
| **High cholesterol** | **+0.5092** | 0.1932 | ±0.3864 | **+2.635** | **0.0084** | 1.6639 | ** |
| Kidney disease | +0.5572 | 0.3043 | ±0.6086 | +1.831 | 0.0671 | 1.7457 | . |
| Circulatory disease | +0.2947 | 0.2679 | ±0.5357 | +1.100 | 0.2713 | 1.3427 |  |
| Avg. daily range (mg/dL) | +0.0018 | 0.0055 | ±0.0111 | +0.333 | 0.7392 | 1.0018 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0673**, LLR χ² = **55.33** (p = **6.73e-08**), AUC = **0.6791**, AIC = **791.4**, BIC = **848.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4057 | 0.7505 | ±1.5010 | -0.541 | 0.5888 | 0.6665 |  |
| Education: graduate level (vs college) | -0.1106 | 0.2036 | ±0.4071 | -0.543 | 0.5870 | 0.8953 |  |
| Education: high school or below (vs college) | +0.3902 | 0.2858 | ±0.5715 | +1.366 | 0.1721 | 1.4773 |  |
| Site: UCSD (vs UAB) | -0.0812 | 0.2486 | ±0.4972 | -0.327 | 0.7440 | 0.9220 |  |
| Site: UW (vs UAB) | +0.2231 | 0.2333 | ±0.4667 | +0.956 | 0.3390 | 1.2499 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0184 | **-4.873** | **1.10e-06** | 0.9561 | *** |
| **BMI (kg/m2)** | **+0.0279** | 0.0129 | ±0.0257 | **+2.169** | **0.0301** | 1.0283 | * |
| Hypertension | +0.1577 | 0.2040 | ±0.4080 | +0.773 | 0.4395 | 1.1708 |  |
| **High cholesterol** | **+0.4948** | 0.1942 | ±0.3884 | **+2.548** | **0.0108** | 1.6402 | * |
| Kidney disease | +0.5575 | 0.3035 | ±0.6070 | +1.837 | 0.0662 | 1.7463 | . |
| Circulatory disease | +0.2800 | 0.2690 | ±0.5379 | +1.041 | 0.2978 | 1.3231 |  |
| SD of daily means (mg/dL) | +0.0284 | 0.0382 | ±0.0764 | +0.742 | 0.4579 | 1.0288 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0669**, LLR χ² = **55.01** (p = **7.73e-08**), AUC = **0.6776**, AIC = **791.7**, BIC = **849.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.9472 | 2.6383 | ±5.2765 | +0.359 | 0.7196 | 2.5785 |  |
| Education: graduate level (vs college) | -0.1171 | 0.2035 | ±0.4070 | -0.575 | 0.5650 | 0.8895 |  |
| Education: high school or below (vs college) | +0.4003 | 0.2850 | ±0.5699 | +1.405 | 0.1601 | 1.4923 |  |
| Site: UCSD (vs UAB) | -0.0855 | 0.2484 | ±0.4968 | -0.344 | 0.7308 | 0.9181 |  |
| Site: UW (vs UAB) | +0.2158 | 0.2325 | ±0.4651 | +0.928 | 0.3533 | 1.2409 |  |
| **Age (years)** | **-0.0453** | 0.0092 | ±0.0185 | **-4.905** | **9.33e-07** | 0.9557 | *** |
| **BMI (kg/m2)** | **+0.0283** | 0.0128 | ±0.0257 | **+2.202** | **0.0276** | 1.0287 | * |
| Hypertension | +0.1530 | 0.2040 | ±0.4080 | +0.750 | 0.4532 | 1.1654 |  |
| **High cholesterol** | **+0.5032** | 0.1936 | ±0.3873 | **+2.599** | **0.0094** | 1.6540 | ** |
| Kidney disease | +0.5532 | 0.3043 | ±0.6087 | +1.818 | 0.0691 | 1.7388 | . |
| Circulatory disease | +0.2873 | 0.2686 | ±0.5372 | +1.069 | 0.2849 | 1.3328 |  |
| Time in range 70-180, pooled (%) | -0.0119 | 0.0253 | ±0.0506 | -0.471 | 0.6374 | 0.9882 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0668**, LLR χ² = **54.93** (p = **7.99e-08**), AUC = **0.6776**, AIC = **791.8**, BIC = **849.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.7414 | 2.7140 | ±5.4280 | +0.273 | 0.7847 | 2.0989 |  |
| Education: graduate level (vs college) | -0.1162 | 0.2034 | ±0.4069 | -0.571 | 0.5677 | 0.8903 |  |
| Education: high school or below (vs college) | +0.4018 | 0.2849 | ±0.5699 | +1.410 | 0.1585 | 1.4946 |  |
| Site: UCSD (vs UAB) | -0.0875 | 0.2484 | ±0.4967 | -0.352 | 0.7247 | 0.9163 |  |
| Site: UW (vs UAB) | +0.2150 | 0.2325 | ±0.4650 | +0.925 | 0.3552 | 1.2398 |  |
| **Age (years)** | **-0.0453** | 0.0092 | ±0.0185 | **-4.900** | **9.60e-07** | 0.9558 | *** |
| **BMI (kg/m2)** | **+0.0283** | 0.0128 | ±0.0257 | **+2.208** | **0.0273** | 1.0287 | * |
| Hypertension | +0.1536 | 0.2040 | ±0.4080 | +0.753 | 0.4514 | 1.1661 |  |
| **High cholesterol** | **+0.5044** | 0.1937 | ±0.3873 | **+2.605** | **0.0092** | 1.6560 | ** |
| Kidney disease | +0.5548 | 0.3045 | ±0.6090 | +1.822 | 0.0684 | 1.7416 | . |
| Circulatory disease | +0.2887 | 0.2686 | ±0.5372 | +1.075 | 0.2824 | 1.3347 |  |
| Avg. daily time in range 70-180 (%) | -0.0099 | 0.0261 | ±0.0521 | -0.378 | 0.7051 | 0.9902 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0668**, LLR χ² = **54.92** (p = **8.01e-08**), AUC = **0.6762**, AIC = **791.8**, BIC = **849.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2296 | 0.7209 | ±1.4418 | -0.318 | 0.7501 | 0.7949 |  |
| Education: graduate level (vs college) | -0.1187 | 0.2036 | ±0.4072 | -0.583 | 0.5600 | 0.8881 |  |
| Education: high school or below (vs college) | +0.3999 | 0.2852 | ±0.5704 | +1.402 | 0.1608 | 1.4917 |  |
| Site: UCSD (vs UAB) | -0.0938 | 0.2476 | ±0.4952 | -0.379 | 0.7049 | 0.9105 |  |
| Site: UW (vs UAB) | +0.2095 | 0.2325 | ±0.4649 | +0.901 | 0.3675 | 1.2331 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0184 | **-4.879** | **1.07e-06** | 0.9560 | *** |
| **BMI (kg/m2)** | **+0.0285** | 0.0128 | ±0.0256 | **+2.229** | **0.0258** | 1.0289 | * |
| Hypertension | +0.1546 | 0.2039 | ±0.4077 | +0.758 | 0.4482 | 1.1672 |  |
| **High cholesterol** | **+0.5114** | 0.1932 | ±0.3863 | **+2.648** | **0.0081** | 1.6677 | ** |
| Kidney disease | +0.5610 | 0.3037 | ±0.6073 | +1.848 | 0.0647 | 1.7525 | . |
| Circulatory disease | +0.2958 | 0.2678 | ±0.5356 | +1.105 | 0.2693 | 1.3442 |  |
| Time 54-69, pooled (%) | -0.0802 | 0.2242 | ±0.4483 | -0.358 | 0.7206 | 0.9230 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0667**, LLR χ² = **54.88** (p = **8.15e-08**), AUC = **0.6766**, AIC = **791.8**, BIC = **849.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2351 | 0.7204 | ±1.4408 | -0.326 | 0.7441 | 0.7905 |  |
| Education: graduate level (vs college) | -0.1181 | 0.2036 | ±0.4073 | -0.580 | 0.5619 | 0.8886 |  |
| Education: high school or below (vs college) | +0.4001 | 0.2852 | ±0.5705 | +1.403 | 0.1607 | 1.4919 |  |
| Site: UCSD (vs UAB) | -0.0923 | 0.2477 | ±0.4954 | -0.373 | 0.7094 | 0.9118 |  |
| Site: UW (vs UAB) | +0.2107 | 0.2324 | ±0.4648 | +0.907 | 0.3646 | 1.2345 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0184 | **-4.877** | **1.08e-06** | 0.9561 | *** |
| **BMI (kg/m2)** | **+0.0285** | 0.0128 | ±0.0256 | **+2.231** | **0.0257** | 1.0289 | * |
| Hypertension | +0.1550 | 0.2039 | ±0.4078 | +0.760 | 0.4470 | 1.1677 |  |
| **High cholesterol** | **+0.5109** | 0.1931 | ±0.3863 | **+2.645** | **0.0082** | 1.6668 | ** |
| Kidney disease | +0.5614 | 0.3037 | ±0.6074 | +1.849 | 0.0645 | 1.7531 | . |
| Circulatory disease | +0.2946 | 0.2678 | ±0.5357 | +1.100 | 0.2714 | 1.3425 |  |
| Avg. daily time 54-69 (%) | -0.0647 | 0.2198 | ±0.4397 | -0.294 | 0.7686 | 0.9374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0668**, LLR χ² = **54.92** (p = **8.01e-08**), AUC = **0.6762**, AIC = **791.8**, BIC = **849.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2296 | 0.7209 | ±1.4418 | -0.318 | 0.7501 | 0.7949 |  |
| Education: graduate level (vs college) | -0.1187 | 0.2036 | ±0.4072 | -0.583 | 0.5600 | 0.8881 |  |
| Education: high school or below (vs college) | +0.3999 | 0.2852 | ±0.5704 | +1.402 | 0.1608 | 1.4917 |  |
| Site: UCSD (vs UAB) | -0.0938 | 0.2476 | ±0.4952 | -0.379 | 0.7049 | 0.9105 |  |
| Site: UW (vs UAB) | +0.2095 | 0.2325 | ±0.4649 | +0.901 | 0.3675 | 1.2331 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0184 | **-4.879** | **1.07e-06** | 0.9560 | *** |
| **BMI (kg/m2)** | **+0.0285** | 0.0128 | ±0.0256 | **+2.229** | **0.0258** | 1.0289 | * |
| Hypertension | +0.1546 | 0.2039 | ±0.4077 | +0.758 | 0.4482 | 1.1672 |  |
| **High cholesterol** | **+0.5114** | 0.1932 | ±0.3863 | **+2.648** | **0.0081** | 1.6677 | ** |
| Kidney disease | +0.5610 | 0.3037 | ±0.6073 | +1.848 | 0.0647 | 1.7525 | . |
| Circulatory disease | +0.2958 | 0.2678 | ±0.5356 | +1.105 | 0.2693 | 1.3442 |  |
| Time < 70 (%) | -0.0802 | 0.2242 | ±0.4483 | -0.358 | 0.7206 | 0.9230 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0667**, LLR χ² = **54.88** (p = **8.15e-08**), AUC = **0.6766**, AIC = **791.8**, BIC = **849.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2351 | 0.7204 | ±1.4408 | -0.326 | 0.7441 | 0.7905 |  |
| Education: graduate level (vs college) | -0.1181 | 0.2036 | ±0.4073 | -0.580 | 0.5619 | 0.8886 |  |
| Education: high school or below (vs college) | +0.4001 | 0.2852 | ±0.5705 | +1.403 | 0.1607 | 1.4919 |  |
| Site: UCSD (vs UAB) | -0.0923 | 0.2477 | ±0.4954 | -0.373 | 0.7094 | 0.9118 |  |
| Site: UW (vs UAB) | +0.2107 | 0.2324 | ±0.4648 | +0.907 | 0.3646 | 1.2345 |  |
| **Age (years)** | **-0.0449** | 0.0092 | ±0.0184 | **-4.877** | **1.08e-06** | 0.9561 | *** |
| **BMI (kg/m2)** | **+0.0285** | 0.0128 | ±0.0256 | **+2.231** | **0.0257** | 1.0289 | * |
| Hypertension | +0.1550 | 0.2039 | ±0.4078 | +0.760 | 0.4470 | 1.1677 |  |
| **High cholesterol** | **+0.5109** | 0.1931 | ±0.3863 | **+2.645** | **0.0082** | 1.6668 | ** |
| Kidney disease | +0.5614 | 0.3037 | ±0.6074 | +1.849 | 0.0645 | 1.7531 | . |
| Circulatory disease | +0.2946 | 0.2678 | ±0.5357 | +1.100 | 0.2714 | 1.3425 |  |
| Avg. daily time < 70 (%) | -0.0647 | 0.2198 | ±0.4397 | -0.294 | 0.7686 | 0.9374 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0669**, LLR χ² = **55.04** (p = **7.61e-08**), AUC = **0.6777**, AIC = **791.7**, BIC = **849.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2410 | 0.7198 | ±1.4397 | -0.335 | 0.7378 | 0.7859 |  |
| Education: graduate level (vs college) | -0.1180 | 0.2035 | ±0.4071 | -0.580 | 0.5619 | 0.8887 |  |
| Education: high school or below (vs college) | +0.3994 | 0.2850 | ±0.5699 | +1.402 | 0.1610 | 1.4910 |  |
| Site: UCSD (vs UAB) | -0.0844 | 0.2484 | ±0.4969 | -0.340 | 0.7339 | 0.9190 |  |
| Site: UW (vs UAB) | +0.2156 | 0.2325 | ±0.4650 | +0.927 | 0.3538 | 1.2406 |  |
| **Age (years)** | **-0.0453** | 0.0092 | ±0.0185 | **-4.907** | **9.23e-07** | 0.9557 | *** |
| **BMI (kg/m2)** | **+0.0282** | 0.0128 | ±0.0257 | **+2.197** | **0.0280** | 1.0286 | * |
| Hypertension | +0.1524 | 0.2040 | ±0.4080 | +0.747 | 0.4550 | 1.1647 |  |
| **High cholesterol** | **+0.5029** | 0.1936 | ±0.3872 | **+2.598** | **0.0094** | 1.6535 | ** |
| Kidney disease | +0.5517 | 0.3044 | ±0.6088 | +1.812 | 0.0699 | 1.7361 | . |
| Circulatory disease | +0.2865 | 0.2686 | ±0.5372 | +1.067 | 0.2861 | 1.3318 |  |
| Time 181-250, pooled (%) | +0.0128 | 0.0250 | ±0.0500 | +0.512 | 0.6085 | 1.0129 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0668**, LLR χ² = **54.96** (p = **7.90e-08**), AUC = **0.6776**, AIC = **791.8**, BIC = **849.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2422 | 0.7198 | ±1.4396 | -0.337 | 0.7365 | 0.7849 |  |
| Education: graduate level (vs college) | -0.1171 | 0.2035 | ±0.4070 | -0.575 | 0.5651 | 0.8895 |  |
| Education: high school or below (vs college) | +0.4011 | 0.2849 | ±0.5699 | +1.408 | 0.1592 | 1.4935 |  |
| Site: UCSD (vs UAB) | -0.0863 | 0.2484 | ±0.4969 | -0.347 | 0.7283 | 0.9173 |  |
| Site: UW (vs UAB) | +0.2148 | 0.2325 | ±0.4649 | +0.924 | 0.3554 | 1.2396 |  |
| **Age (years)** | **-0.0453** | 0.0092 | ±0.0185 | **-4.901** | **9.52e-07** | 0.9558 | *** |
| **BMI (kg/m2)** | **+0.0283** | 0.0128 | ±0.0257 | **+2.202** | **0.0276** | 1.0287 | * |
| Hypertension | +0.1531 | 0.2040 | ±0.4080 | +0.750 | 0.4530 | 1.1654 |  |
| **High cholesterol** | **+0.5041** | 0.1936 | ±0.3873 | **+2.603** | **0.0092** | 1.6555 | ** |
| Kidney disease | +0.5534 | 0.3046 | ±0.6092 | +1.817 | 0.0692 | 1.7392 | . |
| Circulatory disease | +0.2878 | 0.2687 | ±0.5373 | +1.071 | 0.2840 | 1.3335 |  |
| Avg. daily time 181-250 (%) | +0.0106 | 0.0258 | ±0.0515 | +0.413 | 0.6795 | 1.0107 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0669**, LLR χ² = **55.04** (p = **7.61e-08**), AUC = **0.6777**, AIC = **791.7**, BIC = **849.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2410 | 0.7198 | ±1.4397 | -0.335 | 0.7378 | 0.7859 |  |
| Education: graduate level (vs college) | -0.1180 | 0.2035 | ±0.4071 | -0.580 | 0.5619 | 0.8887 |  |
| Education: high school or below (vs college) | +0.3994 | 0.2850 | ±0.5699 | +1.402 | 0.1610 | 1.4910 |  |
| Site: UCSD (vs UAB) | -0.0844 | 0.2484 | ±0.4969 | -0.340 | 0.7339 | 0.9190 |  |
| Site: UW (vs UAB) | +0.2156 | 0.2325 | ±0.4650 | +0.927 | 0.3538 | 1.2406 |  |
| **Age (years)** | **-0.0453** | 0.0092 | ±0.0185 | **-4.907** | **9.23e-07** | 0.9557 | *** |
| **BMI (kg/m2)** | **+0.0282** | 0.0128 | ±0.0257 | **+2.197** | **0.0280** | 1.0286 | * |
| Hypertension | +0.1524 | 0.2040 | ±0.4080 | +0.747 | 0.4550 | 1.1647 |  |
| **High cholesterol** | **+0.5029** | 0.1936 | ±0.3872 | **+2.598** | **0.0094** | 1.6535 | ** |
| Kidney disease | +0.5517 | 0.3044 | ±0.6088 | +1.812 | 0.0699 | 1.7361 | . |
| Circulatory disease | +0.2865 | 0.2686 | ±0.5372 | +1.067 | 0.2861 | 1.3318 |  |
| Time > 180 (%) | +0.0128 | 0.0250 | ±0.0500 | +0.512 | 0.6085 | 1.0129 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0668**, LLR χ² = **54.96** (p = **7.90e-08**), AUC = **0.6776**, AIC = **791.8**, BIC = **849.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2422 | 0.7198 | ±1.4396 | -0.337 | 0.7365 | 0.7849 |  |
| Education: graduate level (vs college) | -0.1171 | 0.2035 | ±0.4070 | -0.575 | 0.5651 | 0.8895 |  |
| Education: high school or below (vs college) | +0.4011 | 0.2849 | ±0.5699 | +1.408 | 0.1592 | 1.4935 |  |
| Site: UCSD (vs UAB) | -0.0863 | 0.2484 | ±0.4969 | -0.347 | 0.7283 | 0.9173 |  |
| Site: UW (vs UAB) | +0.2148 | 0.2325 | ±0.4649 | +0.924 | 0.3554 | 1.2396 |  |
| **Age (years)** | **-0.0453** | 0.0092 | ±0.0185 | **-4.901** | **9.52e-07** | 0.9558 | *** |
| **BMI (kg/m2)** | **+0.0283** | 0.0128 | ±0.0257 | **+2.202** | **0.0276** | 1.0287 | * |
| Hypertension | +0.1531 | 0.2040 | ±0.4080 | +0.750 | 0.4530 | 1.1654 |  |
| **High cholesterol** | **+0.5041** | 0.1936 | ±0.3873 | **+2.603** | **0.0092** | 1.6555 | ** |
| Kidney disease | +0.5534 | 0.3046 | ±0.6092 | +1.817 | 0.0692 | 1.7392 | . |
| Circulatory disease | +0.2878 | 0.2687 | ±0.5373 | +1.071 | 0.2840 | 1.3335 |  |
| Avg. daily time > 180 (%) | +0.0106 | 0.0258 | ±0.0515 | +0.413 | 0.6795 | 1.0107 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 889)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **889**, events = **155**, McFadden pseudo-R² = **0.0730**, LLR χ² = **60.03** (p = **9.15e-09**), AUC = **0.6843**, AIC = **786.7**, BIC = **844.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1992 | 0.7259 | ±1.4518 | -0.274 | 0.7838 | 0.8194 |  |
| Education: graduate level (vs college) | -0.1151 | 0.2042 | ±0.4084 | -0.564 | 0.5729 | 0.8913 |  |
| Education: high school or below (vs college) | +0.3596 | 0.2868 | ±0.5735 | +1.254 | 0.2098 | 1.4328 |  |
| Site: UCSD (vs UAB) | -0.0477 | 0.2492 | ±0.4983 | -0.191 | 0.8482 | 0.9534 |  |
| Site: UW (vs UAB) | +0.2310 | 0.2338 | ±0.4677 | +0.988 | 0.3233 | 1.2598 |  |
| **Age (years)** | **-0.0451** | 0.0093 | ±0.0185 | **-4.870** | **1.12e-06** | 0.9559 | *** |
| BMI (kg/m2) | +0.0248 | 0.0130 | ±0.0261 | +1.904 | 0.0569 | 1.0252 | . |
| Hypertension | +0.1806 | 0.2046 | ±0.4091 | +0.883 | 0.3774 | 1.1979 |  |
| **High cholesterol** | **+0.4622** | 0.1948 | ±0.3896 | **+2.373** | **0.0177** | 1.5875 | * |
| Kidney disease | +0.5299 | 0.3048 | ±0.6096 | +1.738 | 0.0822 | 1.6987 | . |
| Circulatory disease | +0.2626 | 0.2703 | ±0.5405 | +0.972 | 0.3312 | 1.3004 |  |
| **Nocturnal time > 180 (%)** | **+0.0467** | 0.0205 | ±0.0410 | **+2.277** | **0.0228** | 1.0478 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 872; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **872**, R² = **0.1432**, Adj R² = **0.1302**, F-statistic = **11.03** (p = **4.38e-22**), Residual SE = **0.824** on **858** df, AIC = **2150.9**, BIC = **2217.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9104** | 0.2079 | ±0.4159 | **+9.187** | **4.02e-20** | *** |
| Education: graduate level (vs college) | -0.0329 | 0.0587 | ±0.1175 | -0.561 | 0.5749 |  |
| **Education: high school or below (vs college)** | **+0.4985** | 0.1221 | ±0.2441 | **+4.084** | **4.42e-05** | *** |
| Site: UCSD (vs UAB) | +0.0302 | 0.0729 | ±0.1459 | +0.414 | 0.6789 |  |
| **Site: UW (vs UAB)** | **-0.2941** | 0.0778 | ±0.1556 | **-3.781** | **1.56e-04** | *** |
| Season: spring (vs autumn) | -0.0318 | 0.0797 | ±0.1594 | -0.398 | 0.6904 |  |
| Season: summer (vs autumn) | +0.0683 | 0.0801 | ±0.1603 | +0.852 | 0.3943 |  |
| Season: winter (vs autumn) | -0.0037 | 0.0750 | ±0.1500 | -0.049 | 0.9612 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.204** | **2.62e-05** | *** |
| **BMI (kg/m2)** | **+0.0219** | 0.0045 | ±0.0091 | **+4.827** | **1.38e-06** | *** |
| Hypertension | +0.0908 | 0.0608 | ±0.1216 | +1.494 | 0.1352 |  |
| High cholesterol | -0.0906 | 0.0554 | ±0.1108 | -1.636 | 0.1019 |  |
| Kidney disease | -0.0493 | 0.0935 | ±0.1870 | -0.527 | 0.5983 |  |
| **Circulatory disease** | **+0.2084** | 0.0949 | ±0.1898 | **+2.197** | **0.0280** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **872**, R² = **0.1434**, Adj R² = **0.1294**, F-statistic = **10.25** (p = **1.32e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.6**, BIC = **2224.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7167** | 0.4284 | ±0.8569 | **+4.007** | **6.15e-05** | *** |
| Education: graduate level (vs college) | -0.0331 | 0.0588 | ±0.1176 | -0.562 | 0.5739 |  |
| **Education: high school or below (vs college)** | **+0.4959** | 0.1218 | ±0.2436 | **+4.072** | **4.66e-05** | *** |
| Site: UCSD (vs UAB) | +0.0305 | 0.0731 | ±0.1462 | +0.417 | 0.6765 |  |
| **Site: UW (vs UAB)** | **-0.2937** | 0.0779 | ±0.1557 | **-3.773** | **1.61e-04** | *** |
| Season: spring (vs autumn) | -0.0277 | 0.0798 | ±0.1596 | -0.347 | 0.7284 |  |
| Season: summer (vs autumn) | +0.0673 | 0.0804 | ±0.1608 | +0.838 | 0.4023 |  |
| Season: winter (vs autumn) | -0.0012 | 0.0751 | ±0.1503 | -0.016 | 0.9872 |  |
| **Age (years)** | **-0.0110** | 0.0026 | ±0.0052 | **-4.239** | **2.25e-05** | *** |
| **BMI (kg/m2)** | **+0.0215** | 0.0046 | ±0.0091 | **+4.715** | **2.41e-06** | *** |
| Hypertension | +0.0865 | 0.0620 | ±0.1239 | +1.396 | 0.1626 |  |
| High cholesterol | -0.0950 | 0.0555 | ±0.1111 | -1.710 | 0.0872 | . |
| Kidney disease | -0.0492 | 0.0940 | ±0.1880 | -0.523 | 0.6010 |  |
| **Circulatory disease** | **+0.2062** | 0.0957 | ±0.1915 | **+2.154** | **0.0312** | * |
| HbA1c (%) | +0.0375 | 0.0694 | ±0.1389 | +0.540 | 0.5893 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **872**, R² = **0.1446**, Adj R² = **0.1306**, F-statistic = **10.35** (p = **7.71e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.5**, BIC = **2223.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.2302** | 0.3293 | ±0.6586 | **+6.773** | **1.26e-11** | *** |
| Education: graduate level (vs college) | -0.0297 | 0.0590 | ±0.1179 | -0.503 | 0.6150 |  |
| **Education: high school or below (vs college)** | **+0.5012** | 0.1218 | ±0.2436 | **+4.114** | **3.89e-05** | *** |
| Site: UCSD (vs UAB) | +0.0260 | 0.0728 | ±0.1456 | +0.358 | 0.7205 |  |
| **Site: UW (vs UAB)** | **-0.2918** | 0.0778 | ±0.1556 | **-3.752** | **1.76e-04** | *** |
| Season: spring (vs autumn) | -0.0321 | 0.0799 | ±0.1599 | -0.401 | 0.6884 |  |
| Season: summer (vs autumn) | +0.0719 | 0.0805 | ±0.1610 | +0.893 | 0.3720 |  |
| Season: winter (vs autumn) | -0.0056 | 0.0749 | ±0.1498 | -0.075 | 0.9399 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.181** | **2.90e-05** | *** |
| **BMI (kg/m2)** | **+0.0225** | 0.0046 | ±0.0092 | **+4.896** | **9.79e-07** | *** |
| Hypertension | +0.0997 | 0.0618 | ±0.1236 | +1.614 | 0.1065 |  |
| High cholesterol | -0.0893 | 0.0553 | ±0.1106 | -1.615 | 0.1062 |  |
| Kidney disease | -0.0413 | 0.0931 | ±0.1862 | -0.444 | 0.6571 |  |
| **Circulatory disease** | **+0.2142** | 0.0949 | ±0.1899 | **+2.256** | **0.0241** | * |
| Mean glucose (mg/dL) | -0.0029 | 0.0024 | ±0.0048 | -1.210 | 0.2261 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **872**, R² = **0.1446**, Adj R² = **0.1306**, F-statistic = **10.35** (p = **7.71e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.5**, BIC = **2223.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.6290** | 0.6207 | ±1.2415 | **+4.235** | **2.28e-05** | *** |
| Education: graduate level (vs college) | -0.0297 | 0.0590 | ±0.1179 | -0.503 | 0.6150 |  |
| **Education: high school or below (vs college)** | **+0.5012** | 0.1218 | ±0.2436 | **+4.114** | **3.89e-05** | *** |
| Site: UCSD (vs UAB) | +0.0260 | 0.0728 | ±0.1456 | +0.358 | 0.7205 |  |
| **Site: UW (vs UAB)** | **-0.2918** | 0.0778 | ±0.1556 | **-3.752** | **1.76e-04** | *** |
| Season: spring (vs autumn) | -0.0321 | 0.0799 | ±0.1599 | -0.401 | 0.6884 |  |
| Season: summer (vs autumn) | +0.0719 | 0.0805 | ±0.1610 | +0.893 | 0.3720 |  |
| Season: winter (vs autumn) | -0.0056 | 0.0749 | ±0.1498 | -0.075 | 0.9399 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.181** | **2.90e-05** | *** |
| **BMI (kg/m2)** | **+0.0225** | 0.0046 | ±0.0092 | **+4.896** | **9.79e-07** | *** |
| Hypertension | +0.0997 | 0.0618 | ±0.1236 | +1.614 | 0.1065 |  |
| High cholesterol | -0.0893 | 0.0553 | ±0.1106 | -1.615 | 0.1062 |  |
| Kidney disease | -0.0413 | 0.0931 | ±0.1862 | -0.444 | 0.6571 |  |
| **Circulatory disease** | **+0.2142** | 0.0949 | ±0.1899 | **+2.256** | **0.0241** | * |
| GMI (%) | -0.1205 | 0.0995 | ±0.1991 | -1.210 | 0.2261 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **872**, R² = **0.1445**, Adj R² = **0.1305**, F-statistic = **10.34** (p = **8.23e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.6**, BIC = **2223.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1782** | 0.3015 | ±0.6029 | **+7.225** | **5.00e-13** | *** |
| Education: graduate level (vs college) | -0.0306 | 0.0589 | ±0.1178 | -0.520 | 0.6033 |  |
| **Education: high school or below (vs college)** | **+0.5007** | 0.1219 | ±0.2439 | **+4.106** | **4.02e-05** | *** |
| Site: UCSD (vs UAB) | +0.0295 | 0.0727 | ±0.1455 | +0.406 | 0.6847 |  |
| **Site: UW (vs UAB)** | **-0.2913** | 0.0779 | ±0.1558 | **-3.740** | **1.84e-04** | *** |
| Season: spring (vs autumn) | -0.0303 | 0.0799 | ±0.1598 | -0.379 | 0.7047 |  |
| Season: summer (vs autumn) | +0.0722 | 0.0804 | ±0.1608 | +0.898 | 0.3691 |  |
| Season: winter (vs autumn) | -0.0036 | 0.0751 | ±0.1502 | -0.048 | 0.9617 |  |
| **Age (years)** | **-0.0111** | 0.0026 | ±0.0052 | **-4.262** | **2.03e-05** | *** |
| **BMI (kg/m2)** | **+0.0229** | 0.0047 | ±0.0094 | **+4.858** | **1.19e-06** | *** |
| Hypertension | +0.0965 | 0.0612 | ±0.1224 | +1.576 | 0.1151 |  |
| High cholesterol | -0.0869 | 0.0552 | ±0.1104 | -1.574 | 0.1154 |  |
| Kidney disease | -0.0466 | 0.0930 | ±0.1860 | -0.501 | 0.6165 |  |
| **Circulatory disease** | **+0.2133** | 0.0949 | ±0.1899 | **+2.247** | **0.0246** | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0024 | 0.0022 | ±0.0043 | -1.128 | 0.2593 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **872**, R² = **0.1435**, Adj R² = **0.1295**, F-statistic = **10.26** (p = **1.29e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.6**, BIC = **2224.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8429** | 0.2409 | ±0.4818 | **+7.650** | **2.01e-14** | *** |
| Education: graduate level (vs college) | -0.0324 | 0.0589 | ±0.1177 | -0.551 | 0.5819 |  |
| **Education: high school or below (vs college)** | **+0.4944** | 0.1213 | ±0.2426 | **+4.075** | **4.61e-05** | *** |
| Site: UCSD (vs UAB) | +0.0336 | 0.0735 | ±0.1469 | +0.458 | 0.6472 |  |
| **Site: UW (vs UAB)** | **-0.2933** | 0.0779 | ±0.1558 | **-3.766** | **1.66e-04** | *** |
| Season: spring (vs autumn) | -0.0322 | 0.0798 | ±0.1595 | -0.403 | 0.6868 |  |
| Season: summer (vs autumn) | +0.0674 | 0.0803 | ±0.1607 | +0.839 | 0.4012 |  |
| Season: winter (vs autumn) | -0.0045 | 0.0751 | ±0.1501 | -0.060 | 0.9525 |  |
| **Age (years)** | **-0.0110** | 0.0026 | ±0.0052 | **-4.244** | **2.19e-05** | *** |
| **BMI (kg/m2)** | **+0.0218** | 0.0046 | ±0.0091 | **+4.779** | **1.76e-06** | *** |
| Hypertension | +0.0860 | 0.0617 | ±0.1233 | +1.395 | 0.1631 |  |
| High cholesterol | -0.0914 | 0.0554 | ±0.1108 | -1.651 | 0.0987 | . |
| Kidney disease | -0.0538 | 0.0940 | ±0.1880 | -0.573 | 0.5670 |  |
| **Circulatory disease** | **+0.2069** | 0.0951 | ±0.1902 | **+2.176** | **0.0296** | * |
| Glucose SD, pooled (mg/dL) | +0.0040 | 0.0067 | ±0.0133 | +0.602 | 0.5475 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **872**, R² = **0.1433**, Adj R² = **0.1293**, F-statistic = **10.24** (p = **1.43e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.8**, BIC = **2224.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8776** | 0.2366 | ±0.4732 | **+7.936** | **2.09e-15** | *** |
| Education: graduate level (vs college) | -0.0328 | 0.0588 | ±0.1176 | -0.558 | 0.5766 |  |
| **Education: high school or below (vs college)** | **+0.4966** | 0.1215 | ±0.2430 | **+4.088** | **4.35e-05** | *** |
| Site: UCSD (vs UAB) | +0.0319 | 0.0734 | ±0.1468 | +0.434 | 0.6641 |  |
| **Site: UW (vs UAB)** | **-0.2939** | 0.0779 | ±0.1558 | **-3.773** | **1.61e-04** | *** |
| Season: spring (vs autumn) | -0.0315 | 0.0797 | ±0.1595 | -0.395 | 0.6926 |  |
| Season: summer (vs autumn) | +0.0684 | 0.0803 | ±0.1605 | +0.852 | 0.3944 |  |
| Season: winter (vs autumn) | -0.0035 | 0.0750 | ±0.1501 | -0.046 | 0.9631 |  |
| **Age (years)** | **-0.0110** | 0.0026 | ±0.0052 | **-4.229** | **2.35e-05** | *** |
| **BMI (kg/m2)** | **+0.0218** | 0.0046 | ±0.0091 | **+4.793** | **1.64e-06** | *** |
| Hypertension | +0.0882 | 0.0618 | ±0.1237 | +1.427 | 0.1537 |  |
| High cholesterol | -0.0909 | 0.0554 | ±0.1108 | -1.640 | 0.1010 |  |
| Kidney disease | -0.0515 | 0.0939 | ±0.1878 | -0.548 | 0.5834 |  |
| **Circulatory disease** | **+0.2080** | 0.0951 | ±0.1901 | **+2.189** | **0.0286** | * |
| Avg. daily SD (mg/dL) | +0.0021 | 0.0066 | ±0.0133 | +0.324 | 0.7458 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **872**, R² = **0.1449**, Adj R² = **0.1309**, F-statistic = **10.37** (p = **6.77e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.2**, BIC = **2222.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7120** | 0.2642 | ±0.5284 | **+6.480** | **9.15e-11** | *** |
| Education: graduate level (vs college) | -0.0291 | 0.0592 | ±0.1183 | -0.492 | 0.6228 |  |
| **Education: high school or below (vs college)** | **+0.4894** | 0.1208 | ±0.2415 | **+4.052** | **5.08e-05** | *** |
| Site: UCSD (vs UAB) | +0.0369 | 0.0734 | ±0.1469 | +0.503 | 0.6151 |  |
| **Site: UW (vs UAB)** | **-0.2910** | 0.0779 | ±0.1557 | **-3.737** | **1.86e-04** | *** |
| Season: spring (vs autumn) | -0.0332 | 0.0798 | ±0.1596 | -0.416 | 0.6775 |  |
| Season: summer (vs autumn) | +0.0678 | 0.0803 | ±0.1605 | +0.845 | 0.3982 |  |
| Season: winter (vs autumn) | -0.0079 | 0.0749 | ±0.1497 | -0.106 | 0.9159 |  |
| **Age (years)** | **-0.0112** | 0.0026 | ±0.0052 | **-4.298** | **1.73e-05** | *** |
| **BMI (kg/m2)** | **+0.0219** | 0.0045 | ±0.0091 | **+4.834** | **1.34e-06** | *** |
| Hypertension | +0.0833 | 0.0610 | ±0.1219 | +1.366 | 0.1720 |  |
| High cholesterol | -0.0917 | 0.0554 | ±0.1108 | -1.655 | 0.0979 | . |
| Kidney disease | -0.0566 | 0.0939 | ±0.1877 | -0.603 | 0.5467 |  |
| **Circulatory disease** | **+0.2083** | 0.0949 | ±0.1899 | **+2.194** | **0.0282** | * |
| CV (%) | +0.0130 | 0.0096 | ±0.0192 | +1.355 | 0.1753 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **872**, R² = **0.1442**, Adj R² = **0.1302**, F-statistic = **10.32** (p = **9.25e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.9**, BIC = **2223.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0816** | 0.2528 | ±0.5056 | **+8.234** | **1.81e-16** | *** |
| Education: graduate level (vs college) | -0.0295 | 0.0593 | ±0.1185 | -0.498 | 0.6187 |  |
| **Education: high school or below (vs college)** | **+0.4919** | 0.1210 | ±0.2421 | **+4.065** | **4.81e-05** | *** |
| Site: UCSD (vs UAB) | +0.0342 | 0.0734 | ±0.1468 | +0.466 | 0.6409 |  |
| **Site: UW (vs UAB)** | **-0.2928** | 0.0779 | ±0.1558 | **-3.759** | **1.71e-04** | *** |
| Season: spring (vs autumn) | -0.0339 | 0.0798 | ±0.1595 | -0.425 | 0.6711 |  |
| Season: summer (vs autumn) | +0.0682 | 0.0803 | ±0.1605 | +0.850 | 0.3954 |  |
| Season: winter (vs autumn) | -0.0072 | 0.0750 | ±0.1500 | -0.096 | 0.9232 |  |
| **Age (years)** | **-0.0111** | 0.0026 | ±0.0052 | **-4.267** | **1.98e-05** | *** |
| **BMI (kg/m2)** | **+0.0219** | 0.0045 | ±0.0091 | **+4.826** | **1.40e-06** | *** |
| Hypertension | +0.0851 | 0.0610 | ±0.1219 | +1.395 | 0.1629 |  |
| High cholesterol | -0.0912 | 0.0554 | ±0.1108 | -1.645 | 0.1000 | . |
| Kidney disease | -0.0548 | 0.0937 | ±0.1875 | -0.584 | 0.5590 |  |
| **Circulatory disease** | **+0.2092** | 0.0949 | ±0.1898 | **+2.205** | **0.0275** | * |
| Mean / SD ratio | -0.0253 | 0.0235 | ±0.0471 | -1.073 | 0.2832 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **872**, R² = **0.1438**, Adj R² = **0.1298**, F-statistic = **10.28** (p = **1.13e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.3**, BIC = **2223.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0326** | 0.2479 | ±0.4958 | **+8.198** | **2.44e-16** | *** |
| Education: graduate level (vs college) | -0.0307 | 0.0591 | ±0.1183 | -0.518 | 0.6042 |  |
| **Education: high school or below (vs college)** | **+0.4944** | 0.1213 | ±0.2426 | **+4.075** | **4.59e-05** | *** |
| Site: UCSD (vs UAB) | +0.0327 | 0.0733 | ±0.1466 | +0.446 | 0.6555 |  |
| **Site: UW (vs UAB)** | **-0.2938** | 0.0779 | ±0.1558 | **-3.772** | **1.62e-04** | *** |
| Season: spring (vs autumn) | -0.0323 | 0.0797 | ±0.1594 | -0.406 | 0.6850 |  |
| Season: summer (vs autumn) | +0.0694 | 0.0803 | ±0.1605 | +0.865 | 0.3869 |  |
| Season: winter (vs autumn) | -0.0046 | 0.0749 | ±0.1499 | -0.061 | 0.9513 |  |
| **Age (years)** | **-0.0111** | 0.0026 | ±0.0052 | **-4.253** | **2.11e-05** | *** |
| **BMI (kg/m2)** | **+0.0218** | 0.0045 | ±0.0091 | **+4.808** | **1.53e-06** | *** |
| Hypertension | +0.0868 | 0.0610 | ±0.1220 | +1.423 | 0.1548 |  |
| High cholesterol | -0.0906 | 0.0555 | ±0.1109 | -1.634 | 0.1022 |  |
| Kidney disease | -0.0534 | 0.0939 | ±0.1878 | -0.569 | 0.5697 |  |
| **Circulatory disease** | **+0.2106** | 0.0948 | ±0.1896 | **+2.221** | **0.0263** | * |
| Avg. daily mean/SD | -0.0155 | 0.0189 | ±0.0378 | -0.818 | 0.4131 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **872**, R² = **0.1446**, Adj R² = **0.1306**, F-statistic = **10.35** (p = **7.73e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.5**, BIC = **2223.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7218** | 0.2562 | ±0.5123 | **+6.722** | **1.79e-11** | *** |
| Education: graduate level (vs college) | -0.0333 | 0.0587 | ±0.1175 | -0.567 | 0.5705 |  |
| **Education: high school or below (vs college)** | **+0.4896** | 0.1236 | ±0.2472 | **+3.961** | **7.47e-05** | *** |
| Site: UCSD (vs UAB) | +0.0330 | 0.0732 | ±0.1464 | +0.451 | 0.6522 |  |
| **Site: UW (vs UAB)** | **-0.2918** | 0.0782 | ±0.1564 | **-3.731** | **1.91e-04** | *** |
| Season: spring (vs autumn) | -0.0323 | 0.0795 | ±0.1590 | -0.406 | 0.6846 |  |
| Season: summer (vs autumn) | +0.0708 | 0.0802 | ±0.1603 | +0.883 | 0.3773 |  |
| Season: winter (vs autumn) | -0.0022 | 0.0749 | ±0.1498 | -0.029 | 0.9767 |  |
| **Age (years)** | **-0.0108** | 0.0026 | ±0.0052 | **-4.181** | **2.90e-05** | *** |
| **BMI (kg/m2)** | **+0.0219** | 0.0045 | ±0.0091 | **+4.819** | **1.45e-06** | *** |
| Hypertension | +0.0919 | 0.0610 | ±0.1221 | +1.506 | 0.1321 |  |
| High cholesterol | -0.0907 | 0.0554 | ±0.1108 | -1.637 | 0.1016 |  |
| Kidney disease | -0.0534 | 0.0934 | ±0.1867 | -0.572 | 0.5672 |  |
| **Circulatory disease** | **+0.2115** | 0.0949 | ±0.1898 | **+2.228** | **0.0259** | * |
| MAG (mg/dL/h) | +0.0050 | 0.0042 | ±0.0083 | +1.208 | 0.2272 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **872**, R² = **0.1432**, Adj R² = **0.1292**, F-statistic = **10.23** (p = **1.47e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.9**, BIC = **2224.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8807** | 0.2532 | ±0.5063 | **+7.429** | **1.10e-13** | *** |
| Education: graduate level (vs college) | -0.0331 | 0.0588 | ±0.1175 | -0.563 | 0.5733 |  |
| **Education: high school or below (vs college)** | **+0.4972** | 0.1215 | ±0.2429 | **+4.094** | **4.25e-05** | *** |
| Site: UCSD (vs UAB) | +0.0311 | 0.0732 | ±0.1464 | +0.425 | 0.6707 |  |
| **Site: UW (vs UAB)** | **-0.2940** | 0.0779 | ±0.1557 | **-3.775** | **1.60e-04** | *** |
| Season: spring (vs autumn) | -0.0318 | 0.0798 | ±0.1596 | -0.399 | 0.6898 |  |
| Season: summer (vs autumn) | +0.0686 | 0.0802 | ±0.1603 | +0.856 | 0.3922 |  |
| Season: winter (vs autumn) | -0.0035 | 0.0750 | ±0.1501 | -0.046 | 0.9631 |  |
| **Age (years)** | **-0.0110** | 0.0026 | ±0.0052 | **-4.227** | **2.36e-05** | *** |
| **BMI (kg/m2)** | **+0.0219** | 0.0045 | ±0.0091 | **+4.831** | **1.36e-06** | *** |
| Hypertension | +0.0897 | 0.0614 | ±0.1227 | +1.461 | 0.1439 |  |
| High cholesterol | -0.0907 | 0.0554 | ±0.1108 | -1.636 | 0.1019 |  |
| Kidney disease | -0.0506 | 0.0937 | ±0.1874 | -0.540 | 0.5893 |  |
| **Circulatory disease** | **+0.2081** | 0.0950 | ±0.1901 | **+2.190** | **0.0285** | * |
| Avg. daily range (mg/dL) | +0.0003 | 0.0015 | ±0.0031 | +0.224 | 0.8230 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **872**, R² = **0.1446**, Adj R² = **0.1306**, F-statistic = **10.34** (p = **7.88e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.5**, BIC = **2223.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8449** | 0.2127 | ±0.4254 | **+8.675** | **4.15e-18** | *** |
| Education: graduate level (vs college) | -0.0332 | 0.0587 | ±0.1175 | -0.565 | 0.5724 |  |
| **Education: high school or below (vs college)** | **+0.4906** | 0.1213 | ±0.2427 | **+4.044** | **5.26e-05** | *** |
| Site: UCSD (vs UAB) | +0.0353 | 0.0727 | ±0.1454 | +0.485 | 0.6274 |  |
| **Site: UW (vs UAB)** | **-0.2915** | 0.0775 | ±0.1551 | **-3.759** | **1.71e-04** | *** |
| Season: spring (vs autumn) | -0.0383 | 0.0795 | ±0.1589 | -0.482 | 0.6298 |  |
| Season: summer (vs autumn) | +0.0572 | 0.0808 | ±0.1617 | +0.708 | 0.4791 |  |
| Season: winter (vs autumn) | -0.0090 | 0.0757 | ±0.1513 | -0.119 | 0.9054 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.199** | **2.69e-05** | *** |
| **BMI (kg/m2)** | **+0.0214** | 0.0046 | ±0.0092 | **+4.637** | **3.53e-06** | *** |
| Hypertension | +0.0905 | 0.0608 | ±0.1216 | +1.489 | 0.1366 |  |
| High cholesterol | -0.0963 | 0.0554 | ±0.1108 | -1.738 | 0.0822 | . |
| Kidney disease | -0.0524 | 0.0939 | ±0.1879 | -0.558 | 0.5766 |  |
| **Circulatory disease** | **+0.1996** | 0.0942 | ±0.1884 | **+2.118** | **0.0342** | * |
| SD of daily means (mg/dL) | +0.0143 | 0.0130 | ±0.0261 | +1.098 | 0.2720 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **872**, R² = **0.1440**, Adj R² = **0.1300**, F-statistic = **10.29** (p = **1.04e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.1**, BIC = **2223.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.1539 | 0.8311 | ±1.6622 | +1.388 | 0.1650 |  |
| Education: graduate level (vs college) | -0.0319 | 0.0588 | ±0.1176 | -0.542 | 0.5880 |  |
| **Education: high school or below (vs college)** | **+0.5018** | 0.1220 | ±0.2441 | **+4.112** | **3.92e-05** | *** |
| Site: UCSD (vs UAB) | +0.0255 | 0.0729 | ±0.1458 | +0.350 | 0.7267 |  |
| **Site: UW (vs UAB)** | **-0.2950** | 0.0779 | ±0.1557 | **-3.789** | **1.51e-04** | *** |
| Season: spring (vs autumn) | -0.0328 | 0.0798 | ±0.1595 | -0.412 | 0.6807 |  |
| Season: summer (vs autumn) | +0.0699 | 0.0803 | ±0.1606 | +0.870 | 0.3843 |  |
| Season: winter (vs autumn) | -0.0044 | 0.0751 | ±0.1502 | -0.058 | 0.9534 |  |
| **Age (years)** | **-0.0108** | 0.0026 | ±0.0052 | **-4.163** | **3.14e-05** | *** |
| **BMI (kg/m2)** | **+0.0221** | 0.0046 | ±0.0091 | **+4.849** | **1.24e-06** | *** |
| Hypertension | +0.0953 | 0.0612 | ±0.1224 | +1.557 | 0.1194 |  |
| High cholesterol | -0.0879 | 0.0551 | ±0.1103 | -1.595 | 0.1107 |  |
| Kidney disease | -0.0414 | 0.0934 | ±0.1868 | -0.443 | 0.6580 |  |
| **Circulatory disease** | **+0.2129** | 0.0951 | ±0.1903 | **+2.238** | **0.0253** | * |
| Time in range 70-180, pooled (%) | +0.0076 | 0.0080 | ±0.0160 | +0.947 | 0.3436 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **872**, R² = **0.1441**, Adj R² = **0.1302**, F-statistic = **10.31** (p = **9.51e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.9**, BIC = **2223.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0492 | 0.8606 | ±1.7212 | +1.219 | 0.2228 |  |
| Education: graduate level (vs college) | -0.0318 | 0.0588 | ±0.1176 | -0.542 | 0.5881 |  |
| **Education: high school or below (vs college)** | **+0.5014** | 0.1220 | ±0.2440 | **+4.110** | **3.95e-05** | *** |
| Site: UCSD (vs UAB) | +0.0248 | 0.0729 | ±0.1457 | +0.341 | 0.7334 |  |
| **Site: UW (vs UAB)** | **-0.2951** | 0.0779 | ±0.1557 | **-3.791** | **1.50e-04** | *** |
| Season: spring (vs autumn) | -0.0331 | 0.0798 | ±0.1595 | -0.416 | 0.6777 |  |
| Season: summer (vs autumn) | +0.0701 | 0.0803 | ±0.1606 | +0.873 | 0.3826 |  |
| Season: winter (vs autumn) | -0.0046 | 0.0751 | ±0.1502 | -0.062 | 0.9506 |  |
| **Age (years)** | **-0.0108** | 0.0026 | ±0.0052 | **-4.162** | **3.16e-05** | *** |
| **BMI (kg/m2)** | **+0.0221** | 0.0046 | ±0.0091 | **+4.856** | **1.20e-06** | *** |
| Hypertension | +0.0958 | 0.0612 | ±0.1225 | +1.565 | 0.1175 |  |
| High cholesterol | -0.0876 | 0.0551 | ±0.1102 | -1.589 | 0.1121 |  |
| Kidney disease | -0.0400 | 0.0933 | ±0.1866 | -0.429 | 0.6680 |  |
| **Circulatory disease** | **+0.2136** | 0.0952 | ±0.1903 | **+2.245** | **0.0248** | * |
| Avg. daily time in range 70-180 (%) | +0.0086 | 0.0083 | ±0.0166 | +1.041 | 0.2980 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **872**, R² = **0.1435**, Adj R² = **0.1295**, F-statistic = **10.25** (p = **1.30e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.6**, BIC = **2224.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9024** | 0.2087 | ±0.4175 | **+9.114** | **7.97e-20** | *** |
| Education: graduate level (vs college) | -0.0303 | 0.0595 | ±0.1189 | -0.509 | 0.6105 |  |
| **Education: high school or below (vs college)** | **+0.5010** | 0.1224 | ±0.2447 | **+4.094** | **4.23e-05** | *** |
| Site: UCSD (vs UAB) | +0.0293 | 0.0730 | ±0.1459 | +0.401 | 0.6882 |  |
| **Site: UW (vs UAB)** | **-0.2934** | 0.0778 | ±0.1555 | **-3.773** | **1.61e-04** | *** |
| Season: spring (vs autumn) | -0.0317 | 0.0798 | ±0.1595 | -0.397 | 0.6913 |  |
| Season: summer (vs autumn) | +0.0671 | 0.0801 | ±0.1602 | +0.838 | 0.4018 |  |
| Season: winter (vs autumn) | -0.0053 | 0.0750 | ±0.1500 | -0.071 | 0.9438 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.208** | **2.58e-05** | *** |
| **BMI (kg/m2)** | **+0.0220** | 0.0045 | ±0.0091 | **+4.842** | **1.28e-06** | *** |
| Hypertension | +0.0911 | 0.0608 | ±0.1216 | +1.498 | 0.1341 |  |
| High cholesterol | -0.0913 | 0.0553 | ±0.1105 | -1.651 | 0.0987 | . |
| Kidney disease | -0.0479 | 0.0935 | ±0.1871 | -0.512 | 0.6089 |  |
| **Circulatory disease** | **+0.2096** | 0.0952 | ±0.1903 | **+2.203** | **0.0276** | * |
| Time 54-69, pooled (%) | +0.0322 | 0.0610 | ±0.1221 | +0.527 | 0.5984 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **872**, R² = **0.1434**, Adj R² = **0.1294**, F-statistic = **10.24** (p = **1.37e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.7**, BIC = **2224.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9048** | 0.2086 | ±0.4173 | **+9.130** | **6.87e-20** | *** |
| Education: graduate level (vs college) | -0.0307 | 0.0595 | ±0.1191 | -0.516 | 0.6056 |  |
| **Education: high school or below (vs college)** | **+0.5006** | 0.1224 | ±0.2447 | **+4.091** | **4.29e-05** | *** |
| Site: UCSD (vs UAB) | +0.0289 | 0.0730 | ±0.1459 | +0.396 | 0.6917 |  |
| **Site: UW (vs UAB)** | **-0.2937** | 0.0778 | ±0.1556 | **-3.776** | **1.59e-04** | *** |
| Season: spring (vs autumn) | -0.0314 | 0.0797 | ±0.1595 | -0.394 | 0.6939 |  |
| Season: summer (vs autumn) | +0.0678 | 0.0802 | ±0.1603 | +0.845 | 0.3979 |  |
| Season: winter (vs autumn) | -0.0051 | 0.0750 | ±0.1500 | -0.068 | 0.9455 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.209** | **2.57e-05** | *** |
| **BMI (kg/m2)** | **+0.0219** | 0.0045 | ±0.0091 | **+4.840** | **1.30e-06** | *** |
| Hypertension | +0.0910 | 0.0608 | ±0.1216 | +1.497 | 0.1345 |  |
| High cholesterol | -0.0911 | 0.0553 | ±0.1106 | -1.647 | 0.0995 | . |
| Kidney disease | -0.0482 | 0.0935 | ±0.1870 | -0.516 | 0.6062 |  |
| **Circulatory disease** | **+0.2099** | 0.0953 | ±0.1905 | **+2.203** | **0.0276** | * |
| Avg. daily time 54-69 (%) | +0.0248 | 0.0574 | ±0.1149 | +0.432 | 0.6660 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **872**, R² = **0.1435**, Adj R² = **0.1295**, F-statistic = **10.25** (p = **1.30e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.6**, BIC = **2224.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9024** | 0.2087 | ±0.4175 | **+9.114** | **7.97e-20** | *** |
| Education: graduate level (vs college) | -0.0303 | 0.0595 | ±0.1189 | -0.509 | 0.6105 |  |
| **Education: high school or below (vs college)** | **+0.5010** | 0.1224 | ±0.2447 | **+4.094** | **4.23e-05** | *** |
| Site: UCSD (vs UAB) | +0.0293 | 0.0730 | ±0.1459 | +0.401 | 0.6882 |  |
| **Site: UW (vs UAB)** | **-0.2934** | 0.0778 | ±0.1555 | **-3.773** | **1.61e-04** | *** |
| Season: spring (vs autumn) | -0.0317 | 0.0798 | ±0.1595 | -0.397 | 0.6913 |  |
| Season: summer (vs autumn) | +0.0671 | 0.0801 | ±0.1602 | +0.838 | 0.4018 |  |
| Season: winter (vs autumn) | -0.0053 | 0.0750 | ±0.1500 | -0.071 | 0.9438 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.208** | **2.58e-05** | *** |
| **BMI (kg/m2)** | **+0.0220** | 0.0045 | ±0.0091 | **+4.842** | **1.28e-06** | *** |
| Hypertension | +0.0911 | 0.0608 | ±0.1216 | +1.498 | 0.1341 |  |
| High cholesterol | -0.0913 | 0.0553 | ±0.1105 | -1.651 | 0.0987 | . |
| Kidney disease | -0.0479 | 0.0935 | ±0.1871 | -0.512 | 0.6089 |  |
| **Circulatory disease** | **+0.2096** | 0.0952 | ±0.1903 | **+2.203** | **0.0276** | * |
| Time < 70 (%) | +0.0322 | 0.0610 | ±0.1221 | +0.527 | 0.5984 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **872**, R² = **0.1434**, Adj R² = **0.1294**, F-statistic = **10.24** (p = **1.37e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.7**, BIC = **2224.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9048** | 0.2086 | ±0.4173 | **+9.130** | **6.87e-20** | *** |
| Education: graduate level (vs college) | -0.0307 | 0.0595 | ±0.1191 | -0.516 | 0.6056 |  |
| **Education: high school or below (vs college)** | **+0.5006** | 0.1224 | ±0.2447 | **+4.091** | **4.29e-05** | *** |
| Site: UCSD (vs UAB) | +0.0289 | 0.0730 | ±0.1459 | +0.396 | 0.6917 |  |
| **Site: UW (vs UAB)** | **-0.2937** | 0.0778 | ±0.1556 | **-3.776** | **1.59e-04** | *** |
| Season: spring (vs autumn) | -0.0314 | 0.0797 | ±0.1595 | -0.394 | 0.6939 |  |
| Season: summer (vs autumn) | +0.0678 | 0.0802 | ±0.1603 | +0.845 | 0.3979 |  |
| Season: winter (vs autumn) | -0.0051 | 0.0750 | ±0.1500 | -0.068 | 0.9455 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.209** | **2.57e-05** | *** |
| **BMI (kg/m2)** | **+0.0219** | 0.0045 | ±0.0091 | **+4.840** | **1.30e-06** | *** |
| Hypertension | +0.0910 | 0.0608 | ±0.1216 | +1.497 | 0.1345 |  |
| High cholesterol | -0.0911 | 0.0553 | ±0.1106 | -1.647 | 0.0995 | . |
| Kidney disease | -0.0482 | 0.0935 | ±0.1870 | -0.516 | 0.6062 |  |
| **Circulatory disease** | **+0.2099** | 0.0953 | ±0.1905 | **+2.203** | **0.0276** | * |
| Avg. daily time < 70 (%) | +0.0248 | 0.0574 | ±0.1149 | +0.432 | 0.6660 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **872**, R² = **0.1441**, Adj R² = **0.1301**, F-statistic = **10.31** (p = **9.75e-22**), Residual SE = **0.824** on **857** df, AIC = **2152.0**, BIC = **2223.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9110** | 0.2078 | ±0.4156 | **+9.196** | **3.71e-20** | *** |
| Education: graduate level (vs college) | -0.0311 | 0.0588 | ±0.1177 | -0.529 | 0.5971 |  |
| **Education: high school or below (vs college)** | **+0.5027** | 0.1220 | ±0.2441 | **+4.119** | **3.80e-05** | *** |
| Site: UCSD (vs UAB) | +0.0249 | 0.0729 | ±0.1458 | +0.342 | 0.7325 |  |
| **Site: UW (vs UAB)** | **-0.2949** | 0.0778 | ±0.1557 | **-3.788** | **1.52e-04** | *** |
| Season: spring (vs autumn) | -0.0329 | 0.0798 | ±0.1595 | -0.412 | 0.6802 |  |
| Season: summer (vs autumn) | +0.0697 | 0.0803 | ±0.1606 | +0.868 | 0.3854 |  |
| Season: winter (vs autumn) | -0.0049 | 0.0751 | ±0.1501 | -0.065 | 0.9484 |  |
| **Age (years)** | **-0.0108** | 0.0026 | ±0.0052 | **-4.162** | **3.16e-05** | *** |
| **BMI (kg/m2)** | **+0.0221** | 0.0046 | ±0.0091 | **+4.856** | **1.20e-06** | *** |
| Hypertension | +0.0957 | 0.0612 | ±0.1223 | +1.564 | 0.1178 |  |
| High cholesterol | -0.0879 | 0.0552 | ±0.1104 | -1.593 | 0.1112 |  |
| Kidney disease | -0.0404 | 0.0933 | ±0.1867 | -0.433 | 0.6650 |  |
| **Circulatory disease** | **+0.2135** | 0.0952 | ±0.1904 | **+2.242** | **0.0249** | * |
| Time 181-250, pooled (%) | -0.0081 | 0.0079 | ±0.0158 | -1.029 | 0.3034 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **872**, R² = **0.1443**, Adj R² = **0.1303**, F-statistic = **10.32** (p = **9.01e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.8**, BIC = **2223.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9111** | 0.2077 | ±0.4155 | **+9.199** | **3.60e-20** | *** |
| Education: graduate level (vs college) | -0.0310 | 0.0589 | ±0.1177 | -0.526 | 0.5986 |  |
| **Education: high school or below (vs college)** | **+0.5023** | 0.1220 | ±0.2440 | **+4.118** | **3.82e-05** | *** |
| Site: UCSD (vs UAB) | +0.0241 | 0.0729 | ±0.1457 | +0.331 | 0.7409 |  |
| **Site: UW (vs UAB)** | **-0.2951** | 0.0778 | ±0.1557 | **-3.791** | **1.50e-04** | *** |
| Season: spring (vs autumn) | -0.0331 | 0.0798 | ±0.1595 | -0.415 | 0.6784 |  |
| Season: summer (vs autumn) | +0.0700 | 0.0803 | ±0.1606 | +0.872 | 0.3832 |  |
| Season: winter (vs autumn) | -0.0052 | 0.0751 | ±0.1501 | -0.070 | 0.9443 |  |
| **Age (years)** | **-0.0108** | 0.0026 | ±0.0052 | **-4.163** | **3.14e-05** | *** |
| **BMI (kg/m2)** | **+0.0222** | 0.0046 | ±0.0091 | **+4.862** | **1.16e-06** | *** |
| Hypertension | +0.0962 | 0.0612 | ±0.1224 | +1.571 | 0.1162 |  |
| High cholesterol | -0.0876 | 0.0552 | ±0.1103 | -1.588 | 0.1124 |  |
| Kidney disease | -0.0392 | 0.0932 | ±0.1865 | -0.420 | 0.6745 |  |
| **Circulatory disease** | **+0.2144** | 0.0953 | ±0.1905 | **+2.251** | **0.0244** | * |
| Avg. daily time 181-250 (%) | -0.0091 | 0.0082 | ±0.0164 | -1.105 | 0.2692 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **872**, R² = **0.1441**, Adj R² = **0.1301**, F-statistic = **10.31** (p = **9.75e-22**), Residual SE = **0.824** on **857** df, AIC = **2152.0**, BIC = **2223.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9110** | 0.2078 | ±0.4156 | **+9.196** | **3.71e-20** | *** |
| Education: graduate level (vs college) | -0.0311 | 0.0588 | ±0.1177 | -0.529 | 0.5971 |  |
| **Education: high school or below (vs college)** | **+0.5027** | 0.1220 | ±0.2441 | **+4.119** | **3.80e-05** | *** |
| Site: UCSD (vs UAB) | +0.0249 | 0.0729 | ±0.1458 | +0.342 | 0.7325 |  |
| **Site: UW (vs UAB)** | **-0.2949** | 0.0778 | ±0.1557 | **-3.788** | **1.52e-04** | *** |
| Season: spring (vs autumn) | -0.0329 | 0.0798 | ±0.1595 | -0.412 | 0.6802 |  |
| Season: summer (vs autumn) | +0.0697 | 0.0803 | ±0.1606 | +0.868 | 0.3854 |  |
| Season: winter (vs autumn) | -0.0049 | 0.0751 | ±0.1501 | -0.065 | 0.9484 |  |
| **Age (years)** | **-0.0108** | 0.0026 | ±0.0052 | **-4.162** | **3.16e-05** | *** |
| **BMI (kg/m2)** | **+0.0221** | 0.0046 | ±0.0091 | **+4.856** | **1.20e-06** | *** |
| Hypertension | +0.0957 | 0.0612 | ±0.1223 | +1.564 | 0.1178 |  |
| High cholesterol | -0.0879 | 0.0552 | ±0.1104 | -1.593 | 0.1112 |  |
| Kidney disease | -0.0404 | 0.0933 | ±0.1867 | -0.433 | 0.6650 |  |
| **Circulatory disease** | **+0.2135** | 0.0952 | ±0.1904 | **+2.242** | **0.0249** | * |
| Time > 180 (%) | -0.0081 | 0.0079 | ±0.0158 | -1.029 | 0.3034 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **872**, R² = **0.1443**, Adj R² = **0.1303**, F-statistic = **10.32** (p = **9.01e-22**), Residual SE = **0.824** on **857** df, AIC = **2151.8**, BIC = **2223.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9111** | 0.2077 | ±0.4155 | **+9.199** | **3.60e-20** | *** |
| Education: graduate level (vs college) | -0.0310 | 0.0589 | ±0.1177 | -0.526 | 0.5986 |  |
| **Education: high school or below (vs college)** | **+0.5023** | 0.1220 | ±0.2440 | **+4.118** | **3.82e-05** | *** |
| Site: UCSD (vs UAB) | +0.0241 | 0.0729 | ±0.1457 | +0.331 | 0.7409 |  |
| **Site: UW (vs UAB)** | **-0.2951** | 0.0778 | ±0.1557 | **-3.791** | **1.50e-04** | *** |
| Season: spring (vs autumn) | -0.0331 | 0.0798 | ±0.1595 | -0.415 | 0.6784 |  |
| Season: summer (vs autumn) | +0.0700 | 0.0803 | ±0.1606 | +0.872 | 0.3832 |  |
| Season: winter (vs autumn) | -0.0052 | 0.0751 | ±0.1501 | -0.070 | 0.9443 |  |
| **Age (years)** | **-0.0108** | 0.0026 | ±0.0052 | **-4.163** | **3.14e-05** | *** |
| **BMI (kg/m2)** | **+0.0222** | 0.0046 | ±0.0091 | **+4.862** | **1.16e-06** | *** |
| Hypertension | +0.0962 | 0.0612 | ±0.1224 | +1.571 | 0.1162 |  |
| High cholesterol | -0.0876 | 0.0552 | ±0.1103 | -1.588 | 0.1124 |  |
| Kidney disease | -0.0392 | 0.0932 | ±0.1865 | -0.420 | 0.6745 |  |
| **Circulatory disease** | **+0.2144** | 0.0953 | ±0.1905 | **+2.251** | **0.0244** | * |
| Avg. daily time > 180 (%) | -0.0091 | 0.0082 | ±0.0164 | -1.105 | 0.2692 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 872)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **872**, R² = **0.1432**, Adj R² = **0.1292**, F-statistic = **10.23** (p = **1.48e-21**), Residual SE = **0.824** on **857** df, AIC = **2152.9**, BIC = **2224.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9098** | 0.2085 | ±0.4169 | **+9.161** | **5.13e-20** | *** |
| Education: graduate level (vs college) | -0.0330 | 0.0588 | ±0.1176 | -0.560 | 0.5751 |  |
| **Education: high school or below (vs college)** | **+0.4995** | 0.1226 | ±0.2453 | **+4.073** | **4.65e-05** | *** |
| Site: UCSD (vs UAB) | +0.0296 | 0.0728 | ±0.1457 | +0.406 | 0.6847 |  |
| **Site: UW (vs UAB)** | **-0.2943** | 0.0779 | ±0.1558 | **-3.779** | **1.58e-04** | *** |
| Season: spring (vs autumn) | -0.0316 | 0.0798 | ±0.1597 | -0.396 | 0.6922 |  |
| Season: summer (vs autumn) | +0.0687 | 0.0803 | ±0.1605 | +0.856 | 0.3921 |  |
| Season: winter (vs autumn) | -0.0036 | 0.0751 | ±0.1502 | -0.047 | 0.9623 |  |
| **Age (years)** | **-0.0109** | 0.0026 | ±0.0052 | **-4.200** | **2.67e-05** | *** |
| **BMI (kg/m2)** | **+0.0220** | 0.0046 | ±0.0093 | **+4.735** | **2.19e-06** | *** |
| Hypertension | +0.0908 | 0.0608 | ±0.1217 | +1.492 | 0.1357 |  |
| High cholesterol | -0.0899 | 0.0551 | ±0.1102 | -1.631 | 0.1029 |  |
| Kidney disease | -0.0485 | 0.0938 | ±0.1875 | -0.517 | 0.6049 |  |
| **Circulatory disease** | **+0.2089** | 0.0951 | ±0.1902 | **+2.196** | **0.0281** | * |
| Nocturnal time > 180 (%) | -0.0009 | 0.0084 | ±0.0169 | -0.112 | 0.9112 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 872; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3207**, F-statistic = **32.63** (p = **3.59e-66**), Residual SE = **1.930** on **858** df, AIC = **3635.6**, BIC = **3702.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9305** | 0.5716 | ±1.1432 | **+43.615** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2096 | 0.1417 | ±0.2835 | -1.479 | 0.1392 |  |
| Education: high school or below (vs college) | +0.1090 | 0.2581 | ±0.5162 | +0.422 | 0.6727 |  |
| Site: UCSD (vs UAB) | -0.1633 | 0.1763 | ±0.3526 | -0.926 | 0.3545 |  |
| **Site: UW (vs UAB)** | **-1.1741** | 0.1784 | ±0.3569 | **-6.580** | **4.71e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7103** | 0.1908 | ±0.3815 | **-3.724** | **1.96e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5664** | 0.2175 | ±0.4351 | **+7.200** | **6.00e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7585** | 0.1996 | ±0.3992 | **-8.810** | **1.25e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0123 | +0.324 | 0.7461 |  |
| BMI (kg/m2) | +0.0074 | 0.0102 | ±0.0203 | +0.734 | 0.4631 |  |
| **Hypertension** | **+0.3204** | 0.1537 | ±0.3073 | **+2.085** | **0.0370** | * |
| High cholesterol | -0.0804 | 0.1394 | ±0.2789 | -0.577 | 0.5641 |  |
| Kidney disease | +0.1038 | 0.2248 | ±0.4496 | +0.462 | 0.6443 |  |
| Circulatory disease | +0.3715 | 0.2181 | ±0.4362 | +1.703 | 0.0886 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.27** (p = **2.03e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.7109** | 1.0404 | ±2.0809 | **+23.750** | **1.09e-124** | *** |
| Education: graduate level (vs college) | -0.2097 | 0.1419 | ±0.2839 | -1.478 | 0.1395 |  |
| Education: high school or below (vs college) | +0.1060 | 0.2590 | ±0.5180 | +0.409 | 0.6824 |  |
| Site: UCSD (vs UAB) | -0.1629 | 0.1765 | ±0.3529 | -0.923 | 0.3559 |  |
| **Site: UW (vs UAB)** | **-1.1738** | 0.1787 | ±0.3573 | **-6.570** | **5.04e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7057** | 0.1908 | ±0.3816 | **-3.698** | **2.17e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5653** | 0.2179 | ±0.4359 | **+7.183** | **6.84e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7557** | 0.2002 | ±0.4003 | **-8.772** | **1.76e-18** | *** |
| Age (years) | +0.0019 | 0.0062 | ±0.0124 | +0.309 | 0.7575 |  |
| BMI (kg/m2) | +0.0070 | 0.0103 | ±0.0207 | +0.676 | 0.4993 |  |
| **Hypertension** | **+0.3156** | 0.1542 | ±0.3084 | **+2.047** | **0.0407** | * |
| High cholesterol | -0.0854 | 0.1428 | ±0.2856 | -0.598 | 0.5497 |  |
| Kidney disease | +0.1039 | 0.2257 | ±0.4514 | +0.460 | 0.6452 |  |
| Circulatory disease | +0.3690 | 0.2192 | ±0.4383 | +1.683 | 0.0923 | . |
| HbA1c (%) | +0.0425 | 0.1741 | ±0.3482 | +0.244 | 0.8071 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3199**, F-statistic = **30.27** (p = **2.10e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9510** | 0.8402 | ±1.6804 | **+29.697** | **8.47e-194** | *** |
| Education: graduate level (vs college) | -0.2094 | 0.1423 | ±0.2846 | -1.471 | 0.1412 |  |
| Education: high school or below (vs college) | +0.1092 | 0.2584 | ±0.5168 | +0.423 | 0.6726 |  |
| Site: UCSD (vs UAB) | -0.1635 | 0.1772 | ±0.3543 | -0.923 | 0.3560 |  |
| **Site: UW (vs UAB)** | **-1.1740** | 0.1782 | ±0.3564 | **-6.588** | **4.45e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7103** | 0.1910 | ±0.3819 | **-3.720** | **1.99e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5666** | 0.2188 | ±0.4375 | **+7.161** | **7.98e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7586** | 0.1996 | ±0.3992 | **-8.811** | **1.24e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0124 | +0.324 | 0.7462 |  |
| BMI (kg/m2) | +0.0075 | 0.0102 | ±0.0205 | +0.732 | 0.4644 |  |
| **Hypertension** | **+0.3210** | 0.1530 | ±0.3059 | **+2.099** | **0.0359** | * |
| High cholesterol | -0.0803 | 0.1397 | ±0.2794 | -0.575 | 0.5652 |  |
| Kidney disease | +0.1043 | 0.2239 | ±0.4477 | +0.466 | 0.6413 |  |
| Circulatory disease | +0.3718 | 0.2193 | ±0.4387 | +1.695 | 0.0900 | . |
| Mean glucose (mg/dL) | -0.0002 | 0.0056 | ±0.0113 | -0.033 | 0.9738 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3199**, F-statistic = **30.27** (p = **2.10e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9766** | 1.5074 | ±3.0149 | **+16.569** | **1.17e-61** | *** |
| Education: graduate level (vs college) | -0.2094 | 0.1423 | ±0.2846 | -1.471 | 0.1412 |  |
| Education: high school or below (vs college) | +0.1092 | 0.2584 | ±0.5168 | +0.423 | 0.6726 |  |
| Site: UCSD (vs UAB) | -0.1635 | 0.1772 | ±0.3543 | -0.923 | 0.3560 |  |
| **Site: UW (vs UAB)** | **-1.1740** | 0.1782 | ±0.3564 | **-6.588** | **4.45e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7103** | 0.1910 | ±0.3819 | **-3.720** | **1.99e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5666** | 0.2188 | ±0.4375 | **+7.161** | **7.98e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7586** | 0.1996 | ±0.3992 | **-8.811** | **1.24e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0124 | +0.324 | 0.7462 |  |
| BMI (kg/m2) | +0.0075 | 0.0102 | ±0.0205 | +0.732 | 0.4644 |  |
| **Hypertension** | **+0.3210** | 0.1530 | ±0.3059 | **+2.099** | **0.0359** | * |
| High cholesterol | -0.0803 | 0.1397 | ±0.2794 | -0.575 | 0.5652 |  |
| Kidney disease | +0.1043 | 0.2239 | ±0.4477 | +0.466 | 0.6413 |  |
| Circulatory disease | +0.3718 | 0.2193 | ±0.4387 | +1.695 | 0.0900 | . |
| GMI (%) | -0.0077 | 0.2355 | ±0.4709 | -0.033 | 0.9738 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **872**, R² = **0.3311**, Adj R² = **0.3202**, F-statistic = **30.30** (p = **1.82e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.3**, BIC = **3708.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.2265** | 0.7814 | ±1.5629 | **+32.282** | **1.26e-228** | *** |
| Education: graduate level (vs college) | -0.2070 | 0.1419 | ±0.2838 | -1.459 | 0.1447 |  |
| Education: high school or below (vs college) | +0.1114 | 0.2589 | ±0.5178 | +0.430 | 0.6668 |  |
| Site: UCSD (vs UAB) | -0.1640 | 0.1767 | ±0.3534 | -0.928 | 0.3534 |  |
| **Site: UW (vs UAB)** | **-1.1711** | 0.1781 | ±0.3562 | **-6.576** | **4.85e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7087** | 0.1912 | ±0.3823 | **-3.707** | **2.09e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5707** | 0.2189 | ±0.4378 | **+7.175** | **7.23e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7584** | 0.1998 | ±0.3996 | **-8.801** | **1.36e-18** | *** |
| Age (years) | +0.0018 | 0.0062 | ±0.0123 | +0.290 | 0.7716 |  |
| BMI (kg/m2) | +0.0086 | 0.0104 | ±0.0209 | +0.823 | 0.4104 |  |
| **Hypertension** | **+0.3267** | 0.1532 | ±0.3063 | **+2.133** | **0.0329** | * |
| High cholesterol | -0.0764 | 0.1398 | ±0.2796 | -0.546 | 0.5848 |  |
| Kidney disease | +0.1068 | 0.2241 | ±0.4483 | +0.476 | 0.6338 |  |
| Circulatory disease | +0.3769 | 0.2190 | ±0.4379 | +1.721 | 0.0852 | . |
| Nocturnal mean 00-06h (mg/dL) | -0.0027 | 0.0050 | ±0.0099 | -0.545 | 0.5856 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **872**, R² = **0.3310**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **1.96e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.5**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0336** | 0.6514 | ±1.3027 | **+38.433** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2104 | 0.1420 | ±0.2841 | -1.481 | 0.1385 |  |
| Education: high school or below (vs college) | +0.1154 | 0.2568 | ±0.5136 | +0.450 | 0.6531 |  |
| Site: UCSD (vs UAB) | -0.1685 | 0.1767 | ±0.3535 | -0.953 | 0.3404 |  |
| **Site: UW (vs UAB)** | **-1.1753** | 0.1786 | ±0.3573 | **-6.579** | **4.73e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7097** | 0.1911 | ±0.3821 | **-3.715** | **2.04e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5676** | 0.2182 | ±0.4363 | **+7.186** | **6.68e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7572** | 0.1998 | ±0.3995 | **-8.797** | **1.41e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0123 | +0.348 | 0.7276 |  |
| BMI (kg/m2) | +0.0077 | 0.0101 | ±0.0203 | +0.754 | 0.4507 |  |
| **Hypertension** | **+0.3278** | 0.1545 | ±0.3089 | **+2.122** | **0.0338** | * |
| High cholesterol | -0.0791 | 0.1400 | ±0.2800 | -0.565 | 0.5722 |  |
| Kidney disease | +0.1108 | 0.2243 | ±0.4485 | +0.494 | 0.6214 |  |
| Circulatory disease | +0.3738 | 0.2185 | ±0.4370 | +1.711 | 0.0872 | . |
| Glucose SD, pooled (mg/dL) | -0.0061 | 0.0162 | ±0.0324 | -0.379 | 0.7050 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.27** (p = **2.05e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9861** | 0.6443 | ±1.2886 | **+38.779** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2098 | 0.1420 | ±0.2840 | -1.477 | 0.1396 |  |
| Education: high school or below (vs college) | +0.1123 | 0.2566 | ±0.5133 | +0.438 | 0.6617 |  |
| Site: UCSD (vs UAB) | -0.1661 | 0.1766 | ±0.3532 | -0.941 | 0.3469 |  |
| **Site: UW (vs UAB)** | **-1.1745** | 0.1786 | ±0.3572 | **-6.576** | **4.83e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7107** | 0.1910 | ±0.3821 | **-3.721** | **1.99e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5662** | 0.2178 | ±0.4356 | **+7.190** | **6.46e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7588** | 0.1998 | ±0.3997 | **-8.801** | **1.35e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0123 | +0.338 | 0.7350 |  |
| BMI (kg/m2) | +0.0076 | 0.0101 | ±0.0203 | +0.748 | 0.4546 |  |
| **Hypertension** | **+0.3249** | 0.1546 | ±0.3093 | **+2.101** | **0.0357** | * |
| High cholesterol | -0.0799 | 0.1398 | ±0.2796 | -0.572 | 0.5676 |  |
| Kidney disease | +0.1076 | 0.2243 | ±0.4487 | +0.480 | 0.6315 |  |
| Circulatory disease | +0.3721 | 0.2184 | ±0.4368 | +1.704 | 0.0884 | . |
| Avg. daily SD (mg/dL) | -0.0036 | 0.0163 | ±0.0326 | -0.223 | 0.8234 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **872**, R² = **0.3310**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **1.96e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.5**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0603** | 0.6972 | ±1.3944 | **+35.943** | **6.50e-283** | *** |
| Education: graduate level (vs college) | -0.2121 | 0.1426 | ±0.2851 | -1.488 | 0.1368 |  |
| Education: high school or below (vs college) | +0.1150 | 0.2565 | ±0.5129 | +0.449 | 0.6538 |  |
| Site: UCSD (vs UAB) | -0.1677 | 0.1762 | ±0.3524 | -0.952 | 0.3413 |  |
| **Site: UW (vs UAB)** | **-1.1761** | 0.1784 | ±0.3568 | **-6.593** | **4.32e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7094** | 0.1910 | ±0.3820 | **-3.714** | **2.04e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5667** | 0.2178 | ±0.4356 | **+7.193** | **6.33e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7557** | 0.1996 | ±0.3993 | **-8.795** | **1.44e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0123 | +0.349 | 0.7267 |  |
| BMI (kg/m2) | +0.0074 | 0.0102 | ±0.0204 | +0.729 | 0.4659 |  |
| **Hypertension** | **+0.3254** | 0.1546 | ±0.3092 | **+2.105** | **0.0353** | * |
| High cholesterol | -0.0797 | 0.1398 | ±0.2797 | -0.570 | 0.5688 |  |
| Kidney disease | +0.1086 | 0.2252 | ±0.4503 | +0.482 | 0.6296 |  |
| Circulatory disease | +0.3716 | 0.2183 | ±0.4366 | +1.702 | 0.0887 | . |
| CV (%) | -0.0085 | 0.0230 | ±0.0459 | -0.371 | 0.7107 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **1.98e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.5**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.7955** | 0.6658 | ±1.3316 | **+37.240** | **1.51e-303** | *** |
| Education: graduate level (vs college) | -0.2123 | 0.1429 | ±0.2858 | -1.486 | 0.1374 |  |
| Education: high school or below (vs college) | +0.1143 | 0.2565 | ±0.5130 | +0.445 | 0.6560 |  |
| Site: UCSD (vs UAB) | -0.1665 | 0.1763 | ±0.3525 | -0.944 | 0.3450 |  |
| **Site: UW (vs UAB)** | **-1.1751** | 0.1784 | ±0.3569 | **-6.585** | **4.55e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7087** | 0.1911 | ±0.3821 | **-3.709** | **2.08e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5664** | 0.2178 | ±0.4357 | **+7.191** | **6.45e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7557** | 0.1996 | ±0.3993 | **-8.794** | **1.44e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0123 | +0.346 | 0.7295 |  |
| BMI (kg/m2) | +0.0074 | 0.0102 | ±0.0203 | +0.732 | 0.4640 |  |
| **Hypertension** | **+0.3250** | 0.1543 | ±0.3086 | **+2.106** | **0.0352** | * |
| High cholesterol | -0.0800 | 0.1398 | ±0.2796 | -0.572 | 0.5674 |  |
| Kidney disease | +0.1081 | 0.2252 | ±0.4505 | +0.480 | 0.6311 |  |
| Circulatory disease | +0.3709 | 0.2183 | ±0.4367 | +1.699 | 0.0894 | . |
| Mean / SD ratio | +0.0199 | 0.0585 | ±0.1171 | +0.340 | 0.7337 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3199**, F-statistic = **30.27** (p = **2.10e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9151** | 0.6488 | ±1.2975 | **+38.404** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2099 | 0.1431 | ±0.2862 | -1.467 | 0.1425 |  |
| Education: high school or below (vs college) | +0.1096 | 0.2567 | ±0.5135 | +0.427 | 0.6696 |  |
| Site: UCSD (vs UAB) | -0.1636 | 0.1763 | ±0.3527 | -0.928 | 0.3536 |  |
| **Site: UW (vs UAB)** | **-1.1742** | 0.1786 | ±0.3572 | **-6.575** | **4.88e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7103** | 0.1911 | ±0.3821 | **-3.717** | **2.01e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5662** | 0.2179 | ±0.4359 | **+7.186** | **6.65e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7584** | 0.1998 | ±0.3995 | **-8.802** | **1.35e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0123 | +0.327 | 0.7435 |  |
| BMI (kg/m2) | +0.0075 | 0.0101 | ±0.0203 | +0.735 | 0.4623 |  |
| **Hypertension** | **+0.3210** | 0.1542 | ±0.3084 | **+2.081** | **0.0374** | * |
| High cholesterol | -0.0804 | 0.1397 | ±0.2793 | -0.576 | 0.5648 |  |
| Kidney disease | +0.1043 | 0.2252 | ±0.4504 | +0.463 | 0.6432 |  |
| Circulatory disease | +0.3712 | 0.2187 | ±0.4373 | +1.698 | 0.0896 | . |
| Avg. daily mean/SD | +0.0019 | 0.0478 | ±0.0956 | +0.041 | 0.9675 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **872**, R² = **0.3310**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **1.96e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.5**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.7935** | 0.7076 | ±1.4152 | **+35.040** | **5.53e-269** | *** |
| Education: graduate level (vs college) | -0.2099 | 0.1419 | ±0.2838 | -1.479 | 0.1392 |  |
| Education: high school or below (vs college) | +0.1025 | 0.2600 | ±0.5200 | +0.394 | 0.6934 |  |
| Site: UCSD (vs UAB) | -0.1612 | 0.1770 | ±0.3540 | -0.911 | 0.3623 |  |
| **Site: UW (vs UAB)** | **-1.1725** | 0.1790 | ±0.3579 | **-6.551** | **5.72e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7107** | 0.1911 | ±0.3821 | **-3.720** | **1.99e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5682** | 0.2181 | ±0.4362 | **+7.191** | **6.45e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7574** | 0.2001 | ±0.4003 | **-8.781** | **1.62e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0124 | +0.333 | 0.7392 |  |
| BMI (kg/m2) | +0.0075 | 0.0102 | ±0.0203 | +0.734 | 0.4629 |  |
| **Hypertension** | **+0.3212** | 0.1541 | ±0.3081 | **+2.085** | **0.0371** | * |
| High cholesterol | -0.0805 | 0.1396 | ±0.2792 | -0.577 | 0.5642 |  |
| Kidney disease | +0.1008 | 0.2253 | ±0.4505 | +0.447 | 0.6546 |  |
| Circulatory disease | +0.3737 | 0.2184 | ±0.4368 | +1.711 | 0.0871 | . |
| MAG (mg/dL/h) | +0.0037 | 0.0105 | ±0.0211 | +0.347 | 0.7285 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.27** (p = **2.05e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0051** | 0.6799 | ±1.3598 | **+36.778** | **4.22e-296** | *** |
| Education: graduate level (vs college) | -0.2092 | 0.1419 | ±0.2838 | -1.475 | 0.1403 |  |
| Education: high school or below (vs college) | +0.1125 | 0.2570 | ±0.5139 | +0.438 | 0.6616 |  |
| Site: UCSD (vs UAB) | -0.1656 | 0.1763 | ±0.3527 | -0.939 | 0.3477 |  |
| **Site: UW (vs UAB)** | **-1.1744** | 0.1786 | ±0.3572 | **-6.575** | **4.87e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7101** | 0.1911 | ±0.3821 | **-3.717** | **2.02e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5655** | 0.2176 | ±0.4352 | **+7.194** | **6.28e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7589** | 0.1999 | ±0.3998 | **-8.799** | **1.37e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0123 | +0.336 | 0.7368 |  |
| BMI (kg/m2) | +0.0074 | 0.0102 | ±0.0204 | +0.725 | 0.4687 |  |
| **Hypertension** | **+0.3234** | 0.1544 | ±0.3088 | **+2.095** | **0.0362** | * |
| High cholesterol | -0.0802 | 0.1397 | ±0.2794 | -0.574 | 0.5659 |  |
| Kidney disease | +0.1071 | 0.2248 | ±0.4496 | +0.476 | 0.6338 |  |
| Circulatory disease | +0.3723 | 0.2185 | ±0.4370 | +1.704 | 0.0884 | . |
| Avg. daily range (mg/dL) | -0.0009 | 0.0038 | ±0.0077 | -0.225 | 0.8221 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **872**, R² = **0.3315**, Adj R² = **0.3205**, F-statistic = **30.35** (p = **1.43e-65**), Residual SE = **1.931** on **857** df, AIC = **3636.8**, BIC = **3708.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0460** | 0.5984 | ±1.1968 | **+41.856** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2092 | 0.1421 | ±0.2841 | -1.473 | 0.1409 |  |
| Education: high school or below (vs college) | +0.1230 | 0.2583 | ±0.5166 | +0.476 | 0.6340 |  |
| Site: UCSD (vs UAB) | -0.1722 | 0.1764 | ±0.3528 | -0.976 | 0.3289 |  |
| **Site: UW (vs UAB)** | **-1.1787** | 0.1789 | ±0.3579 | **-6.587** | **4.48e-11** | *** |
| **Season: spring (vs autumn)** | **-0.6988** | 0.1900 | ±0.3801 | **-3.677** | **2.36e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5859** | 0.2193 | ±0.4385 | **+7.233** | **4.73e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7491** | 0.1993 | ±0.3987 | **-8.775** | **1.72e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0123 | +0.316 | 0.7519 |  |
| BMI (kg/m2) | +0.0083 | 0.0102 | ±0.0203 | +0.817 | 0.4138 |  |
| **Hypertension** | **+0.3209** | 0.1540 | ±0.3079 | **+2.084** | **0.0371** | * |
| High cholesterol | -0.0704 | 0.1409 | ±0.2818 | -0.499 | 0.6174 |  |
| Kidney disease | +0.1094 | 0.2243 | ±0.4486 | +0.488 | 0.6257 |  |
| Circulatory disease | +0.3871 | 0.2191 | ±0.4382 | +1.767 | 0.0772 | . |
| SD of daily means (mg/dL) | -0.0253 | 0.0303 | ±0.0607 | -0.834 | 0.4041 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.27** (p = **2.03e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.4192** | 1.8624 | ±3.7248 | **+13.112** | **2.82e-39** | *** |
| Education: graduate level (vs college) | -0.2089 | 0.1420 | ±0.2840 | -1.471 | 0.1414 |  |
| Education: high school or below (vs college) | +0.1113 | 0.2583 | ±0.5166 | +0.431 | 0.6667 |  |
| Site: UCSD (vs UAB) | -0.1664 | 0.1767 | ±0.3534 | -0.942 | 0.3463 |  |
| **Site: UW (vs UAB)** | **-1.1747** | 0.1787 | ±0.3575 | **-6.573** | **4.95e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7111** | 0.1910 | ±0.3821 | **-3.722** | **1.98e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5674** | 0.2179 | ±0.4358 | **+7.193** | **6.32e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7590** | 0.1998 | ±0.3996 | **-8.803** | **1.34e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0124 | +0.335 | 0.7377 |  |
| BMI (kg/m2) | +0.0076 | 0.0102 | ±0.0203 | +0.748 | 0.4546 |  |
| **Hypertension** | **+0.3235** | 0.1536 | ±0.3071 | **+2.106** | **0.0352** | * |
| High cholesterol | -0.0786 | 0.1399 | ±0.2798 | -0.562 | 0.5742 |  |
| Kidney disease | +0.1091 | 0.2231 | ±0.4462 | +0.489 | 0.6247 |  |
| Circulatory disease | +0.3745 | 0.2192 | ±0.4384 | +1.708 | 0.0876 | . |
| Time in range 70-180, pooled (%) | +0.0051 | 0.0180 | ±0.0360 | +0.285 | 0.7757 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **872**, R² = **0.3310**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **1.97e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.5**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1909** | 1.9322 | ±3.8645 | **+12.520** | **5.83e-36** | *** |
| Education: graduate level (vs college) | -0.2086 | 0.1420 | ±0.2840 | -1.469 | 0.1418 |  |
| Education: high school or below (vs college) | +0.1115 | 0.2581 | ±0.5163 | +0.432 | 0.6658 |  |
| Site: UCSD (vs UAB) | -0.1679 | 0.1767 | ±0.3533 | -0.950 | 0.3420 |  |
| **Site: UW (vs UAB)** | **-1.1750** | 0.1787 | ±0.3574 | **-6.575** | **4.87e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7115** | 0.1911 | ±0.3822 | **-3.723** | **1.97e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5679** | 0.2179 | ±0.4358 | **+7.195** | **6.24e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7593** | 0.1999 | ±0.3997 | **-8.802** | **1.34e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0124 | +0.338 | 0.7352 |  |
| BMI (kg/m2) | +0.0077 | 0.0102 | ±0.0203 | +0.755 | 0.4503 |  |
| **Hypertension** | **+0.3248** | 0.1538 | ±0.3075 | **+2.112** | **0.0347** | * |
| High cholesterol | -0.0778 | 0.1399 | ±0.2798 | -0.556 | 0.5780 |  |
| Kidney disease | +0.1117 | 0.2227 | ±0.4455 | +0.502 | 0.6159 |  |
| Circulatory disease | +0.3759 | 0.2193 | ±0.4387 | +1.714 | 0.0865 | . |
| Avg. daily time in range 70-180 (%) | +0.0074 | 0.0188 | ±0.0376 | +0.394 | 0.6933 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **872**, R² = **0.3311**, Adj R² = **0.3201**, F-statistic = **30.30** (p = **1.83e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.3**, BIC = **3708.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9487** | 0.5735 | ±1.1469 | **+43.506** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2156 | 0.1419 | ±0.2837 | -1.520 | 0.1285 |  |
| Education: high school or below (vs college) | +0.1036 | 0.2577 | ±0.5153 | +0.402 | 0.6878 |  |
| Site: UCSD (vs UAB) | -0.1612 | 0.1771 | ±0.3542 | -0.910 | 0.3628 |  |
| **Site: UW (vs UAB)** | **-1.1757** | 0.1783 | ±0.3567 | **-6.592** | **4.34e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7105** | 0.1907 | ±0.3813 | **-3.726** | **1.94e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5690** | 0.2173 | ±0.4345 | **+7.221** | **5.14e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7547** | 0.1997 | ±0.3993 | **-8.789** | **1.51e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0123 | +0.330 | 0.7418 |  |
| BMI (kg/m2) | +0.0073 | 0.0102 | ±0.0203 | +0.717 | 0.4732 |  |
| **Hypertension** | **+0.3198** | 0.1537 | ±0.3074 | **+2.081** | **0.0375** | * |
| High cholesterol | -0.0788 | 0.1393 | ±0.2786 | -0.566 | 0.5714 |  |
| Kidney disease | +0.1006 | 0.2248 | ±0.4495 | +0.448 | 0.6545 |  |
| Circulatory disease | +0.3688 | 0.2179 | ±0.4358 | +1.692 | 0.0906 | . |
| Time 54-69, pooled (%) | -0.0732 | 0.1516 | ±0.3032 | -0.483 | 0.6290 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **2.02e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.6**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9389** | 0.5733 | ±1.1466 | **+43.500** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2129 | 0.1420 | ±0.2839 | -1.500 | 0.1337 |  |
| Education: high school or below (vs college) | +0.1059 | 0.2579 | ±0.5159 | +0.411 | 0.6813 |  |
| Site: UCSD (vs UAB) | -0.1614 | 0.1776 | ±0.3551 | -0.909 | 0.3635 |  |
| **Site: UW (vs UAB)** | **-1.1747** | 0.1784 | ±0.3569 | **-6.583** | **4.61e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7109** | 0.1909 | ±0.3817 | **-3.724** | **1.96e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5671** | 0.2174 | ±0.4349 | **+7.207** | **5.72e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7563** | 0.1997 | ±0.3994 | **-8.795** | **1.43e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0123 | +0.328 | 0.7425 |  |
| BMI (kg/m2) | +0.0074 | 0.0102 | ±0.0203 | +0.725 | 0.4686 |  |
| **Hypertension** | **+0.3201** | 0.1537 | ±0.3075 | **+2.082** | **0.0373** | * |
| High cholesterol | -0.0797 | 0.1393 | ±0.2786 | -0.572 | 0.5673 |  |
| Kidney disease | +0.1022 | 0.2247 | ±0.4495 | +0.455 | 0.6492 |  |
| Circulatory disease | +0.3693 | 0.2180 | ±0.4361 | +1.694 | 0.0903 | . |
| Avg. daily time 54-69 (%) | -0.0372 | 0.1386 | ±0.2772 | -0.269 | 0.7881 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **872**, R² = **0.3311**, Adj R² = **0.3201**, F-statistic = **30.30** (p = **1.83e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.3**, BIC = **3708.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9487** | 0.5735 | ±1.1469 | **+43.506** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2156 | 0.1419 | ±0.2837 | -1.520 | 0.1285 |  |
| Education: high school or below (vs college) | +0.1036 | 0.2577 | ±0.5153 | +0.402 | 0.6878 |  |
| Site: UCSD (vs UAB) | -0.1612 | 0.1771 | ±0.3542 | -0.910 | 0.3628 |  |
| **Site: UW (vs UAB)** | **-1.1757** | 0.1783 | ±0.3567 | **-6.592** | **4.34e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7105** | 0.1907 | ±0.3813 | **-3.726** | **1.94e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5690** | 0.2173 | ±0.4345 | **+7.221** | **5.14e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7547** | 0.1997 | ±0.3993 | **-8.789** | **1.51e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0123 | +0.330 | 0.7418 |  |
| BMI (kg/m2) | +0.0073 | 0.0102 | ±0.0203 | +0.717 | 0.4732 |  |
| **Hypertension** | **+0.3198** | 0.1537 | ±0.3074 | **+2.081** | **0.0375** | * |
| High cholesterol | -0.0788 | 0.1393 | ±0.2786 | -0.566 | 0.5714 |  |
| Kidney disease | +0.1006 | 0.2248 | ±0.4495 | +0.448 | 0.6545 |  |
| Circulatory disease | +0.3688 | 0.2179 | ±0.4358 | +1.692 | 0.0906 | . |
| Time < 70 (%) | -0.0732 | 0.1516 | ±0.3032 | -0.483 | 0.6290 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **2.02e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.6**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9389** | 0.5733 | ±1.1466 | **+43.500** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2129 | 0.1420 | ±0.2839 | -1.500 | 0.1337 |  |
| Education: high school or below (vs college) | +0.1059 | 0.2579 | ±0.5159 | +0.411 | 0.6813 |  |
| Site: UCSD (vs UAB) | -0.1614 | 0.1776 | ±0.3551 | -0.909 | 0.3635 |  |
| **Site: UW (vs UAB)** | **-1.1747** | 0.1784 | ±0.3569 | **-6.583** | **4.61e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7109** | 0.1909 | ±0.3817 | **-3.724** | **1.96e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5671** | 0.2174 | ±0.4349 | **+7.207** | **5.72e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7563** | 0.1997 | ±0.3994 | **-8.795** | **1.43e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0123 | +0.328 | 0.7425 |  |
| BMI (kg/m2) | +0.0074 | 0.0102 | ±0.0203 | +0.725 | 0.4686 |  |
| **Hypertension** | **+0.3201** | 0.1537 | ±0.3075 | **+2.082** | **0.0373** | * |
| High cholesterol | -0.0797 | 0.1393 | ±0.2786 | -0.572 | 0.5673 |  |
| Kidney disease | +0.1022 | 0.2247 | ±0.4495 | +0.455 | 0.6492 |  |
| Circulatory disease | +0.3693 | 0.2180 | ±0.4361 | +1.694 | 0.0903 | . |
| Avg. daily time < 70 (%) | -0.0372 | 0.1386 | ±0.2772 | -0.269 | 0.7881 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3199**, F-statistic = **30.27** (p = **2.07e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9308** | 0.5724 | ±1.1448 | **+43.553** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2088 | 0.1421 | ±0.2842 | -1.470 | 0.1417 |  |
| Education: high school or below (vs college) | +0.1108 | 0.2583 | ±0.5167 | +0.429 | 0.6679 |  |
| Site: UCSD (vs UAB) | -0.1655 | 0.1770 | ±0.3539 | -0.935 | 0.3496 |  |
| **Site: UW (vs UAB)** | **-1.1745** | 0.1788 | ±0.3575 | **-6.570** | **5.02e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7108** | 0.1910 | ±0.3821 | **-3.721** | **1.99e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5670** | 0.2179 | ±0.4358 | **+7.191** | **6.44e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7590** | 0.1999 | ±0.3997 | **-8.802** | **1.35e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0124 | +0.331 | 0.7408 |  |
| BMI (kg/m2) | +0.0076 | 0.0102 | ±0.0203 | +0.744 | 0.4568 |  |
| **Hypertension** | **+0.3225** | 0.1535 | ±0.3070 | **+2.101** | **0.0356** | * |
| High cholesterol | -0.0793 | 0.1400 | ±0.2800 | -0.566 | 0.5713 |  |
| Kidney disease | +0.1076 | 0.2232 | ±0.4465 | +0.482 | 0.6297 |  |
| Circulatory disease | +0.3737 | 0.2193 | ±0.4385 | +1.704 | 0.0884 | . |
| Time 181-250, pooled (%) | -0.0035 | 0.0180 | ±0.0360 | -0.196 | 0.8446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **2.00e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.5**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9310** | 0.5728 | ±1.1456 | **+43.527** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2082 | 0.1421 | ±0.2842 | -1.465 | 0.1428 |  |
| Education: high school or below (vs college) | +0.1117 | 0.2582 | ±0.5163 | +0.433 | 0.6652 |  |
| Site: UCSD (vs UAB) | -0.1676 | 0.1770 | ±0.3540 | -0.947 | 0.3437 |  |
| **Site: UW (vs UAB)** | **-1.1748** | 0.1787 | ±0.3575 | **-6.573** | **4.94e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7113** | 0.1911 | ±0.3822 | **-3.722** | **1.98e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5676** | 0.2180 | ±0.4359 | **+7.192** | **6.38e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7596** | 0.1999 | ±0.3998 | **-8.802** | **1.35e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0124 | +0.335 | 0.7374 |  |
| BMI (kg/m2) | +0.0077 | 0.0102 | ±0.0203 | +0.754 | 0.4511 |  |
| **Hypertension** | **+0.3242** | 0.1537 | ±0.3074 | **+2.109** | **0.0349** | * |
| High cholesterol | -0.0783 | 0.1400 | ±0.2800 | -0.559 | 0.5760 |  |
| Kidney disease | +0.1110 | 0.2227 | ±0.4455 | +0.498 | 0.6184 |  |
| Circulatory disease | +0.3757 | 0.2194 | ±0.4389 | +1.712 | 0.0869 | . |
| Avg. daily time 181-250 (%) | -0.0064 | 0.0188 | ±0.0376 | -0.342 | 0.7324 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3199**, F-statistic = **30.27** (p = **2.07e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9308** | 0.5724 | ±1.1448 | **+43.553** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2088 | 0.1421 | ±0.2842 | -1.470 | 0.1417 |  |
| Education: high school or below (vs college) | +0.1108 | 0.2583 | ±0.5167 | +0.429 | 0.6679 |  |
| Site: UCSD (vs UAB) | -0.1655 | 0.1770 | ±0.3539 | -0.935 | 0.3496 |  |
| **Site: UW (vs UAB)** | **-1.1745** | 0.1788 | ±0.3575 | **-6.570** | **5.02e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7108** | 0.1910 | ±0.3821 | **-3.721** | **1.99e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5670** | 0.2179 | ±0.4358 | **+7.191** | **6.44e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7590** | 0.1999 | ±0.3997 | **-8.802** | **1.35e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0124 | +0.331 | 0.7408 |  |
| BMI (kg/m2) | +0.0076 | 0.0102 | ±0.0203 | +0.744 | 0.4568 |  |
| **Hypertension** | **+0.3225** | 0.1535 | ±0.3070 | **+2.101** | **0.0356** | * |
| High cholesterol | -0.0793 | 0.1400 | ±0.2800 | -0.566 | 0.5713 |  |
| Kidney disease | +0.1076 | 0.2232 | ±0.4465 | +0.482 | 0.6297 |  |
| Circulatory disease | +0.3737 | 0.2193 | ±0.4385 | +1.704 | 0.0884 | . |
| Time > 180 (%) | -0.0035 | 0.0180 | ±0.0360 | -0.196 | 0.8446 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3200**, F-statistic = **30.28** (p = **2.00e-65**), Residual SE = **1.931** on **857** df, AIC = **3637.5**, BIC = **3709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9310** | 0.5728 | ±1.1456 | **+43.527** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2082 | 0.1421 | ±0.2842 | -1.465 | 0.1428 |  |
| Education: high school or below (vs college) | +0.1117 | 0.2582 | ±0.5163 | +0.433 | 0.6652 |  |
| Site: UCSD (vs UAB) | -0.1676 | 0.1770 | ±0.3540 | -0.947 | 0.3437 |  |
| **Site: UW (vs UAB)** | **-1.1748** | 0.1787 | ±0.3575 | **-6.573** | **4.94e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7113** | 0.1911 | ±0.3822 | **-3.722** | **1.98e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5676** | 0.2180 | ±0.4359 | **+7.192** | **6.38e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7596** | 0.1999 | ±0.3998 | **-8.802** | **1.35e-18** | *** |
| Age (years) | +0.0021 | 0.0062 | ±0.0124 | +0.335 | 0.7374 |  |
| BMI (kg/m2) | +0.0077 | 0.0102 | ±0.0203 | +0.754 | 0.4511 |  |
| **Hypertension** | **+0.3242** | 0.1537 | ±0.3074 | **+2.109** | **0.0349** | * |
| High cholesterol | -0.0783 | 0.1400 | ±0.2800 | -0.559 | 0.5760 |  |
| Kidney disease | +0.1110 | 0.2227 | ±0.4455 | +0.498 | 0.6184 |  |
| Circulatory disease | +0.3757 | 0.2194 | ±0.4389 | +1.712 | 0.0869 | . |
| Avg. daily time > 180 (%) | -0.0064 | 0.0188 | ±0.0376 | -0.342 | 0.7324 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 872)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **872**, R² = **0.3309**, Adj R² = **0.3199**, F-statistic = **30.27** (p = **2.10e-65**), Residual SE = **1.932** on **857** df, AIC = **3637.6**, BIC = **3709.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9305** | 0.5717 | ±1.1435 | **+43.604** | **0.00e+00** | *** |
| Education: graduate level (vs college) | -0.2096 | 0.1418 | ±0.2837 | -1.478 | 0.1395 |  |
| Education: high school or below (vs college) | +0.1091 | 0.2587 | ±0.5175 | +0.422 | 0.6734 |  |
| Site: UCSD (vs UAB) | -0.1633 | 0.1771 | ±0.3543 | -0.922 | 0.3566 |  |
| **Site: UW (vs UAB)** | **-1.1741** | 0.1789 | ±0.3578 | **-6.564** | **5.25e-11** | *** |
| **Season: spring (vs autumn)** | **-0.7103** | 0.1908 | ±0.3815 | **-3.723** | **1.97e-04** | *** |
| **Season: summer (vs autumn)** | **+1.5664** | 0.2177 | ±0.4355 | **+7.194** | **6.29e-13** | *** |
| **Season: winter (vs autumn)** | **-1.7585** | 0.1997 | ±0.3994 | **-8.806** | **1.30e-18** | *** |
| Age (years) | +0.0020 | 0.0062 | ±0.0124 | +0.323 | 0.7465 |  |
| BMI (kg/m2) | +0.0075 | 0.0102 | ±0.0204 | +0.731 | 0.4648 |  |
| **Hypertension** | **+0.3204** | 0.1538 | ±0.3076 | **+2.083** | **0.0372** | * |
| High cholesterol | -0.0804 | 0.1413 | ±0.2825 | -0.569 | 0.5693 |  |
| Kidney disease | +0.1038 | 0.2246 | ±0.4493 | +0.462 | 0.6440 |  |
| Circulatory disease | +0.3715 | 0.2185 | ±0.4371 | +1.700 | 0.0892 | . |
| Nocturnal time > 180 (%) | -0.0000 | 0.0185 | ±0.0370 | -0.001 | 0.9990 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 872; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **872**, R² = **0.2626**, Adj R² = **0.2514**, F-statistic = **23.50** (p = **1.29e-48**), Residual SE = **5.775** on **858** df, AIC = **5546.7**, BIC = **5613.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4372** | 1.5438 | ±3.0877 | **+32.022** | **5.33e-225** | *** |
| **Education: graduate level (vs college)** | **+1.1957** | 0.4200 | ±0.8400 | **+2.847** | **0.0044** | ** |
| Education: high school or below (vs college) | +0.6717 | 0.7786 | ±1.5571 | +0.863 | 0.3882 |  |
| **Site: UCSD (vs UAB)** | **+3.2259** | 0.5302 | ±1.0603 | **+6.085** | **1.17e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5433** | 0.5089 | ±1.0178 | **-3.033** | **0.0024** | ** |
| **Season: spring (vs autumn)** | **-1.1481** | 0.5664 | ±1.1327 | **-2.027** | **0.0427** | * |
| **Season: summer (vs autumn)** | **+2.1417** | 0.5891 | ±1.1782 | **+3.635** | **2.77e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0946** | 0.5945 | ±1.1889 | **-8.570** | **1.03e-17** | *** |
| **Age (years)** | **-0.0368** | 0.0186 | ±0.0372 | **-1.981** | **0.0476** | * |
| BMI (kg/m2) | -0.0487 | 0.0283 | ±0.0566 | -1.719 | 0.0856 | . |
| Hypertension | +0.2814 | 0.4516 | ±0.9031 | +0.623 | 0.5332 |  |
| **High cholesterol** | **-1.0705** | 0.4199 | ±0.8398 | **-2.549** | **0.0108** | * |
| Kidney disease | +0.2443 | 0.7193 | ±1.4386 | +0.340 | 0.7341 |  |
| Circulatory disease | -0.4864 | 0.5933 | ±1.1865 | -0.820 | 0.4123 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **872**, R² = **0.2632**, Adj R² = **0.2511**, F-statistic = **21.86** (p = **4.59e-48**), Residual SE = **5.776** on **857** df, AIC = **5548.0**, BIC = **5619.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.2834** | 3.1745 | ±6.3490 | **+14.895** | **3.56e-50** | *** |
| **Education: graduate level (vs college)** | **+1.1943** | 0.4205 | ±0.8410 | **+2.840** | **0.0045** | ** |
| Education: high school or below (vs college) | +0.6419 | 0.7799 | ±1.5598 | +0.823 | 0.4104 |  |
| **Site: UCSD (vs UAB)** | **+3.2292** | 0.5302 | ±1.0604 | **+6.091** | **1.12e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5396** | 0.5094 | ±1.0189 | **-3.022** | **0.0025** | ** |
| Season: spring (vs autumn) | -1.1031 | 0.5690 | ±1.1380 | -1.939 | 0.0526 | . |
| **Season: summer (vs autumn)** | **+2.1313** | 0.5890 | ±1.1780 | **+3.618** | **2.96e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0674** | 0.5968 | ±1.1936 | **-8.491** | **2.04e-17** | *** |
| **Age (years)** | **-0.0377** | 0.0188 | ±0.0376 | **-2.005** | **0.0450** | * |
| BMI (kg/m2) | -0.0532 | 0.0292 | ±0.0584 | -1.823 | 0.0683 | . |
| Hypertension | +0.2337 | 0.4552 | ±0.9104 | +0.513 | 0.6076 |  |
| **High cholesterol** | **-1.1197** | 0.4237 | ±0.8473 | **-2.643** | **0.0082** | ** |
| Kidney disease | +0.2455 | 0.7175 | ±1.4349 | +0.342 | 0.7322 |  |
| Circulatory disease | -0.5109 | 0.5912 | ±1.1824 | -0.864 | 0.3875 |  |
| HbA1c (%) | +0.4170 | 0.5660 | ±1.1321 | +0.737 | 0.4613 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **872**, R² = **0.2642**, Adj R² = **0.2522**, F-statistic = **21.98** (p = **2.55e-48**), Residual SE = **5.772** on **857** df, AIC = **5546.8**, BIC = **5618.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.8514** | 2.4405 | ±4.8811 | **+19.197** | **3.91e-82** | *** |
| **Education: graduate level (vs college)** | **+1.1692** | 0.4202 | ±0.8405 | **+2.782** | **0.0054** | ** |
| Education: high school or below (vs college) | +0.6506 | 0.7765 | ±1.5530 | +0.838 | 0.4021 |  |
| **Site: UCSD (vs UAB)** | **+3.2595** | 0.5299 | ±1.0597 | **+6.152** | **7.67e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5612** | 0.5085 | ±1.0169 | **-3.070** | **0.0021** | ** |
| **Season: spring (vs autumn)** | **-1.1456** | 0.5666 | ±1.1331 | **-2.022** | **0.0432** | * |
| **Season: summer (vs autumn)** | **+2.1128** | 0.5917 | ±1.1834 | **+3.571** | **3.56e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0785** | 0.5946 | ±1.1893 | **-8.540** | **1.34e-17** | *** |
| **Age (years)** | **-0.0373** | 0.0186 | ±0.0372 | **-2.005** | **0.0450** | * |
| BMI (kg/m2) | -0.0538 | 0.0285 | ±0.0571 | -1.885 | 0.0594 | . |
| Hypertension | +0.2093 | 0.4555 | ±0.9111 | +0.459 | 0.6459 |  |
| **High cholesterol** | **-1.0807** | 0.4190 | ±0.8379 | **-2.579** | **0.0099** | ** |
| Kidney disease | +0.1801 | 0.7128 | ±1.4256 | +0.253 | 0.8005 |  |
| Circulatory disease | -0.5328 | 0.5927 | ±1.1855 | -0.899 | 0.3688 |  |
| Mean glucose (mg/dL) | +0.0233 | 0.0167 | ±0.0334 | +1.397 | 0.1624 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **872**, R² = **0.2642**, Adj R² = **0.2522**, F-statistic = **21.98** (p = **2.55e-48**), Residual SE = **5.772** on **857** df, AIC = **5546.8**, BIC = **5618.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6274** | 4.4711 | ±8.9423 | **+9.758** | **1.71e-22** | *** |
| **Education: graduate level (vs college)** | **+1.1692** | 0.4202 | ±0.8405 | **+2.782** | **0.0054** | ** |
| Education: high school or below (vs college) | +0.6506 | 0.7765 | ±1.5530 | +0.838 | 0.4021 |  |
| **Site: UCSD (vs UAB)** | **+3.2595** | 0.5299 | ±1.0597 | **+6.152** | **7.67e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5612** | 0.5085 | ±1.0169 | **-3.070** | **0.0021** | ** |
| **Season: spring (vs autumn)** | **-1.1456** | 0.5666 | ±1.1331 | **-2.022** | **0.0432** | * |
| **Season: summer (vs autumn)** | **+2.1128** | 0.5917 | ±1.1834 | **+3.571** | **3.56e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0785** | 0.5946 | ±1.1893 | **-8.540** | **1.34e-17** | *** |
| **Age (years)** | **-0.0373** | 0.0186 | ±0.0372 | **-2.005** | **0.0450** | * |
| BMI (kg/m2) | -0.0538 | 0.0285 | ±0.0571 | -1.885 | 0.0594 | . |
| Hypertension | +0.2093 | 0.4555 | ±0.9111 | +0.459 | 0.6459 |  |
| **High cholesterol** | **-1.0807** | 0.4190 | ±0.8379 | **-2.579** | **0.0099** | ** |
| Kidney disease | +0.1801 | 0.7128 | ±1.4256 | +0.253 | 0.8005 |  |
| Circulatory disease | -0.5328 | 0.5927 | ±1.1855 | -0.899 | 0.3688 |  |
| GMI (%) | +0.9740 | 0.6972 | ±1.3944 | +1.397 | 0.1624 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **872**, R² = **0.2644**, Adj R² = **0.2524**, F-statistic = **22.00** (p = **2.34e-48**), Residual SE = **5.771** on **857** df, AIC = **5546.6**, BIC = **5618.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.0513** | 2.2821 | ±4.5642 | **+20.618** | **1.91e-94** | *** |
| **Education: graduate level (vs college)** | **+1.1750** | 0.4204 | ±0.8408 | **+2.795** | **0.0052** | ** |
| Education: high school or below (vs college) | +0.6523 | 0.7785 | ±1.5570 | +0.838 | 0.4021 |  |
| **Site: UCSD (vs UAB)** | **+3.2318** | 0.5303 | ±1.0607 | **+6.094** | **1.10e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5680** | 0.5085 | ±1.0170 | **-3.083** | **0.0020** | ** |
| **Season: spring (vs autumn)** | **-1.1611** | 0.5659 | ±1.1318 | **-2.052** | **0.0402** | * |
| **Season: summer (vs autumn)** | **+2.1066** | 0.5912 | ±1.1825 | **+3.563** | **3.66e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0950** | 0.5946 | ±1.1893 | **-8.568** | **1.05e-17** | *** |
| Age (years) | -0.0352 | 0.0186 | ±0.0373 | -1.887 | 0.0591 | . |
| **BMI (kg/m2)** | **-0.0579** | 0.0294 | ±0.0587 | **-1.973** | **0.0485** | * |
| Hypertension | +0.2312 | 0.4528 | ±0.9056 | +0.511 | 0.6096 |  |
| **High cholesterol** | **-1.1030** | 0.4185 | ±0.8369 | **-2.636** | **0.0084** | ** |
| Kidney disease | +0.2203 | 0.7170 | ±1.4339 | +0.307 | 0.7586 |  |
| Circulatory disease | -0.5300 | 0.5933 | ±1.1865 | -0.893 | 0.3716 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0218 | 0.0152 | ±0.0304 | +1.431 | 0.1524 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **872**, R² = **0.2698**, Adj R² = **0.2578**, F-statistic = **22.61** (p = **1.12e-49**), Residual SE = **5.750** on **857** df, AIC = **5540.2**, BIC = **5611.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.0502** | 1.7680 | ±3.5360 | **+26.612** | **4.88e-156** | *** |
| **Education: graduate level (vs college)** | **+1.2146** | 0.4193 | ±0.8387 | **+2.896** | **0.0038** | ** |
| Education: high school or below (vs college) | +0.5236 | 0.7688 | ±1.5376 | +0.681 | 0.4958 |  |
| **Site: UCSD (vs UAB)** | **+3.3470** | 0.5254 | ±1.0507 | **+6.371** | **1.88e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5171** | 0.5036 | ±1.0071 | **-3.013** | **0.0026** | ** |
| **Season: spring (vs autumn)** | **-1.1626** | 0.5640 | ±1.1279 | **-2.061** | **0.0393** | * |
| **Season: summer (vs autumn)** | **+2.1123** | 0.5868 | ±1.1736 | **+3.600** | **3.19e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1235** | 0.5942 | ±1.1883 | **-8.623** | **6.52e-18** | *** |
| **Age (years)** | **-0.0403** | 0.0185 | ±0.0370 | **-2.183** | **0.0290** | * |
| BMI (kg/m2) | -0.0534 | 0.0285 | ±0.0570 | -1.876 | 0.0607 | . |
| Hypertension | +0.1108 | 0.4537 | ±0.9075 | +0.244 | 0.8071 |  |
| **High cholesterol** | **-1.1013** | 0.4183 | ±0.8365 | **-2.633** | **0.0085** | ** |
| Kidney disease | +0.0833 | 0.6981 | ±1.3962 | +0.119 | 0.9051 |  |
| Circulatory disease | -0.5396 | 0.5818 | ±1.1636 | -0.927 | 0.3537 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.1421** | 0.0483 | ±0.0967 | **+2.940** | **0.0033** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **872**, R² = **0.2693**, Adj R² = **0.2574**, F-statistic = **22.56** (p = **1.45e-49**), Residual SE = **5.752** on **857** df, AIC = **5540.7**, BIC = **5612.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.3062** | 1.7532 | ±3.5064 | **+26.983** | **2.34e-160** | *** |
| **Education: graduate level (vs college)** | **+1.2024** | 0.4194 | ±0.8388 | **+2.867** | **0.0041** | ** |
| Education: high school or below (vs college) | +0.5470 | 0.7693 | ±1.5385 | +0.711 | 0.4770 |  |
| **Site: UCSD (vs UAB)** | **+3.3354** | 0.5249 | ±1.0499 | **+6.354** | **2.10e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5299** | 0.5037 | ±1.0075 | **-3.037** | **0.0024** | ** |
| **Season: spring (vs autumn)** | **-1.1327** | 0.5642 | ±1.1285 | **-2.008** | **0.0447** | * |
| **Season: summer (vs autumn)** | **+2.1476** | 0.5871 | ±1.1741 | **+3.658** | **2.54e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0832** | 0.5933 | ±1.1866 | **-8.568** | **1.05e-17** | *** |
| **Age (years)** | **-0.0403** | 0.0184 | ±0.0369 | **-2.186** | **0.0288** | * |
| BMI (kg/m2) | -0.0538 | 0.0286 | ±0.0572 | -1.882 | 0.0598 | . |
| Hypertension | +0.1120 | 0.4543 | ±0.9086 | +0.247 | 0.8052 |  |
| **High cholesterol** | **-1.0903** | 0.4187 | ±0.8374 | **-2.604** | **0.0092** | ** |
| Kidney disease | +0.0992 | 0.6996 | ±1.3991 | +0.142 | 0.8873 |  |
| Circulatory disease | -0.5124 | 0.5842 | ±1.1683 | -0.877 | 0.3805 |  |
| **Avg. daily SD (mg/dL)** | **+0.1397** | 0.0489 | ±0.0978 | **+2.858** | **0.0043** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **872**, R² = **0.2680**, Adj R² = **0.2560**, F-statistic = **22.41** (p = **3.06e-49**), Residual SE = **5.757** on **857** df, AIC = **5542.3**, BIC = **5613.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.7770** | 1.9067 | ±3.8134 | **+24.533** | **6.58e-133** | *** |
| **Education: graduate level (vs college)** | **+1.2472** | 0.4194 | ±0.8388 | **+2.974** | **0.0029** | ** |
| Education: high school or below (vs college) | +0.5488 | 0.7732 | ±1.5465 | +0.710 | 0.4779 |  |
| **Site: UCSD (vs UAB)** | **+3.3161** | 0.5266 | ±1.0533 | **+6.297** | **3.04e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5018** | 0.5049 | ±1.0098 | **-2.974** | **0.0029** | ** |
| **Season: spring (vs autumn)** | **-1.1671** | 0.5643 | ±1.1286 | **-2.068** | **0.0386** | * |
| **Season: summer (vs autumn)** | **+2.1354** | 0.5850 | ±1.1699 | **+3.650** | **2.62e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1517** | 0.5950 | ±1.1900 | **-8.658** | **4.80e-18** | *** |
| **Age (years)** | **-0.0400** | 0.0185 | ±0.0370 | **-2.161** | **0.0307** | * |
| BMI (kg/m2) | -0.0481 | 0.0284 | ±0.0568 | -1.696 | 0.0899 | . |
| Hypertension | +0.1800 | 0.4514 | ±0.9028 | +0.399 | 0.6900 |  |
| **High cholesterol** | **-1.0857** | 0.4194 | ±0.8388 | **-2.589** | **0.0096** | ** |
| Kidney disease | +0.1462 | 0.7071 | ±1.4142 | +0.207 | 0.8362 |  |
| Circulatory disease | -0.4884 | 0.5856 | ±1.1712 | -0.834 | 0.4042 |  |
| **CV (%)** | **+0.1745** | 0.0702 | ±0.1404 | **+2.486** | **0.0129** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **872**, R² = **0.2657**, Adj R² = **0.2537**, F-statistic = **22.15** (p = **1.12e-48**), Residual SE = **5.766** on **857** df, AIC = **5545.0**, BIC = **5616.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6715** | 1.9372 | ±3.8744 | **+26.673** | **9.63e-157** | *** |
| **Education: graduate level (vs college)** | **+1.2409** | 0.4200 | ±0.8400 | **+2.954** | **0.0031** | ** |
| Education: high school or below (vs college) | +0.5852 | 0.7766 | ±1.5532 | +0.754 | 0.4511 |  |
| **Site: UCSD (vs UAB)** | **+3.2788** | 0.5278 | ±1.0556 | **+6.212** | **5.23e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5274** | 0.5061 | ±1.0122 | **-3.018** | **0.0025** | ** |
| **Season: spring (vs autumn)** | **-1.1757** | 0.5650 | ±1.1301 | **-2.081** | **0.0375** | * |
| **Season: summer (vs autumn)** | **+2.1409** | 0.5873 | ±1.1745 | **+3.646** | **2.67e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1413** | 0.5957 | ±1.1913 | **-8.631** | **6.06e-18** | *** |
| **Age (years)** | **-0.0390** | 0.0185 | ±0.0371 | **-2.103** | **0.0355** | * |
| BMI (kg/m2) | -0.0487 | 0.0284 | ±0.0567 | -1.715 | 0.0863 | . |
| Hypertension | +0.2063 | 0.4522 | ±0.9043 | +0.456 | 0.6483 |  |
| **High cholesterol** | **-1.0782** | 0.4200 | ±0.8400 | **-2.567** | **0.0103** | * |
| Kidney disease | +0.1723 | 0.7114 | ±1.4228 | +0.242 | 0.8087 |  |
| Circulatory disease | -0.4766 | 0.5873 | ±1.1747 | -0.811 | 0.4171 |  |
| Mean / SD ratio | -0.3297 | 0.1768 | ±0.3536 | -1.865 | 0.0622 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **872**, R² = **0.2663**, Adj R² = **0.2543**, F-statistic = **22.21** (p = **8.11e-49**), Residual SE = **5.764** on **857** df, AIC = **5544.3**, BIC = **5615.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6983** | 1.8983 | ±3.7967 | **+27.233** | **2.62e-163** | *** |
| **Education: graduate level (vs college)** | **+1.2381** | 0.4195 | ±0.8391 | **+2.951** | **0.0032** | ** |
| Education: high school or below (vs college) | +0.5944 | 0.7759 | ±1.5518 | +0.766 | 0.4436 |  |
| **Site: UCSD (vs UAB)** | **+3.2724** | 0.5260 | ±1.0520 | **+6.221** | **4.93e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5386** | 0.5058 | ±1.0116 | **-3.042** | **0.0024** | ** |
| **Season: spring (vs autumn)** | **-1.1589** | 0.5646 | ±1.1291 | **-2.053** | **0.0401** | * |
| **Season: summer (vs autumn)** | **+2.1632** | 0.5873 | ±1.1747 | **+3.683** | **2.30e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1117** | 0.5940 | ±1.1881 | **-8.605** | **7.64e-18** | *** |
| **Age (years)** | **-0.0395** | 0.0185 | ±0.0370 | **-2.135** | **0.0327** | * |
| BMI (kg/m2) | -0.0501 | 0.0285 | ±0.0570 | -1.760 | 0.0785 | . |
| Hypertension | +0.2065 | 0.4517 | ±0.9034 | +0.457 | 0.6476 |  |
| **High cholesterol** | **-1.0713** | 0.4203 | ±0.8406 | **-2.549** | **0.0108** | * |
| Kidney disease | +0.1679 | 0.7105 | ±1.4210 | +0.236 | 0.8132 |  |
| Circulatory disease | -0.4464 | 0.5894 | ±1.1787 | -0.757 | 0.4488 |  |
| Avg. daily mean/SD | -0.2862 | 0.1461 | ±0.2922 | -1.959 | 0.0501 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **872**, R² = **0.2626**, Adj R² = **0.2506**, F-statistic = **21.80** (p = **6.16e-48**), Residual SE = **5.778** on **857** df, AIC = **5548.6**, BIC = **5620.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.1222** | 1.9577 | ±3.9153 | **+25.092** | **6.06e-139** | *** |
| **Education: graduate level (vs college)** | **+1.1951** | 0.4206 | ±0.8413 | **+2.841** | **0.0045** | ** |
| Education: high school or below (vs college) | +0.6568 | 0.7818 | ±1.5636 | +0.840 | 0.4009 |  |
| **Site: UCSD (vs UAB)** | **+3.2306** | 0.5310 | ±1.0620 | **+6.084** | **1.17e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5394** | 0.5101 | ±1.0203 | **-3.018** | **0.0025** | ** |
| **Season: spring (vs autumn)** | **-1.1490** | 0.5666 | ±1.1332 | **-2.028** | **0.0426** | * |
| **Season: summer (vs autumn)** | **+2.1459** | 0.5893 | ±1.1786 | **+3.642** | **2.71e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0921** | 0.5952 | ±1.1905 | **-8.555** | **1.18e-17** | *** |
| **Age (years)** | **-0.0367** | 0.0186 | ±0.0372 | **-1.972** | **0.0486** | * |
| BMI (kg/m2) | -0.0486 | 0.0283 | ±0.0567 | -1.716 | 0.0862 | . |
| Hypertension | +0.2832 | 0.4521 | ±0.9042 | +0.626 | 0.5310 |  |
| **High cholesterol** | **-1.0707** | 0.4205 | ±0.8410 | **-2.546** | **0.0109** | * |
| Kidney disease | +0.2373 | 0.7212 | ±1.4424 | +0.329 | 0.7421 |  |
| Circulatory disease | -0.4813 | 0.5948 | ±1.1897 | -0.809 | 0.4185 |  |
| MAG (mg/dL/h) | +0.0084 | 0.0312 | ±0.0624 | +0.270 | 0.7873 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **872**, R² = **0.2661**, Adj R² = **0.2541**, F-statistic = **22.19** (p = **9.11e-49**), Residual SE = **5.765** on **857** df, AIC = **5544.6**, BIC = **5616.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.3951** | 1.8791 | ±3.7582 | **+25.222** | **2.28e-140** | *** |
| **Education: graduate level (vs college)** | **+1.1854** | 0.4206 | ±0.8412 | **+2.818** | **0.0048** | ** |
| Education: high school or below (vs college) | +0.5780 | 0.7719 | ±1.5438 | +0.749 | 0.4540 |  |
| **Site: UCSD (vs UAB)** | **+3.2898** | 0.5268 | ±1.0536 | **+6.245** | **4.24e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5367** | 0.5066 | ±1.0133 | **-3.033** | **0.0024** | ** |
| **Season: spring (vs autumn)** | **-1.1544** | 0.5634 | ±1.1268 | **-2.049** | **0.0405** | * |
| **Season: summer (vs autumn)** | **+2.1637** | 0.5867 | ±1.1735 | **+3.688** | **2.26e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0821** | 0.5950 | ±1.1901 | **-8.541** | **1.33e-17** | *** |
| **Age (years)** | **-0.0389** | 0.0185 | ±0.0369 | **-2.107** | **0.0351** | * |
| BMI (kg/m2) | -0.0470 | 0.0284 | ±0.0568 | -1.656 | 0.0977 | . |
| Hypertension | +0.2015 | 0.4537 | ±0.9074 | +0.444 | 0.6570 |  |
| **High cholesterol** | **-1.0766** | 0.4202 | ±0.8404 | **-2.562** | **0.0104** | * |
| Kidney disease | +0.1543 | 0.7085 | ±1.4170 | +0.218 | 0.8276 |  |
| Circulatory disease | -0.5085 | 0.5891 | ±1.1781 | -0.863 | 0.3880 |  |
| **Avg. daily range (mg/dL)** | **+0.0237** | 0.0116 | ±0.0233 | **+2.031** | **0.0423** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **872**, R² = **0.2653**, Adj R² = **0.2533**, F-statistic = **22.10** (p = **1.40e-48**), Residual SE = **5.768** on **857** df, AIC = **5545.5**, BIC = **5617.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.7475** | 1.5681 | ±3.1362 | **+31.087** | **3.60e-212** | *** |
| **Education: graduate level (vs college)** | **+1.1934** | 0.4202 | ±0.8404 | **+2.840** | **0.0045** | ** |
| Education: high school or below (vs college) | +0.5885 | 0.7781 | ±1.5561 | +0.756 | 0.4494 |  |
| **Site: UCSD (vs UAB)** | **+3.2795** | 0.5306 | ±1.0613 | **+6.180** | **6.39e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5162** | 0.5080 | ±1.0161 | **-2.984** | **0.0028** | ** |
| **Season: spring (vs autumn)** | **-1.2171** | 0.5683 | ±1.1367 | **-2.142** | **0.0322** | * |
| **Season: summer (vs autumn)** | **+2.0251** | 0.5900 | ±1.1800 | **+3.432** | **5.98e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1509** | 0.5966 | ±1.1933 | **-8.633** | **5.97e-18** | *** |
| **Age (years)** | **-0.0366** | 0.0186 | ±0.0371 | **-1.969** | **0.0489** | * |
| BMI (kg/m2) | -0.0538 | 0.0287 | ±0.0574 | -1.876 | 0.0607 | . |
| Hypertension | +0.2785 | 0.4519 | ±0.9038 | +0.616 | 0.5377 |  |
| **High cholesterol** | **-1.1305** | 0.4188 | ±0.8375 | **-2.700** | **0.0069** | ** |
| Kidney disease | +0.2107 | 0.7106 | ±1.4212 | +0.297 | 0.7668 |  |
| Circulatory disease | -0.5800 | 0.5862 | ±1.1725 | -0.989 | 0.3225 |  |
| SD of daily means (mg/dL) | +0.1511 | 0.0924 | ±0.1848 | +1.636 | 0.1019 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **872**, R² = **0.2662**, Adj R² = **0.2542**, F-statistic = **22.21** (p = **8.24e-49**), Residual SE = **5.764** on **857** df, AIC = **5544.4**, BIC = **5615.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.6964** | 6.4605 | ±12.9210 | **+9.550** | **1.30e-21** | *** |
| **Education: graduate level (vs college)** | **+1.1781** | 0.4200 | ±0.8400 | **+2.805** | **0.0050** | ** |
| Education: high school or below (vs college) | +0.6183 | 0.7769 | ±1.5537 | +0.796 | 0.4261 |  |
| **Site: UCSD (vs UAB)** | **+3.3021** | 0.5325 | ±1.0651 | **+6.201** | **5.62e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5283** | 0.5078 | ±1.0156 | **-3.010** | **0.0026** | ** |
| **Season: spring (vs autumn)** | **-1.1308** | 0.5652 | ±1.1304 | **-2.001** | **0.0454** | * |
| **Season: summer (vs autumn)** | **+2.1159** | 0.5897 | ±1.1794 | **+3.588** | **3.33e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0827** | 0.5922 | ±1.1844 | **-8.582** | **9.29e-18** | *** |
| **Age (years)** | **-0.0386** | 0.0186 | ±0.0372 | **-2.076** | **0.0379** | * |
| BMI (kg/m2) | -0.0522 | 0.0284 | ±0.0569 | -1.835 | 0.0665 | . |
| Hypertension | +0.2091 | 0.4545 | ±0.9089 | +0.460 | 0.6454 |  |
| **High cholesterol** | **-1.1134** | 0.4189 | ±0.8379 | **-2.658** | **0.0079** | ** |
| Kidney disease | +0.1160 | 0.7003 | ±1.4006 | +0.166 | 0.8684 |  |
| Circulatory disease | -0.5585 | 0.5868 | ±1.1736 | -0.952 | 0.3412 |  |
| Time in range 70-180, pooled (%) | -0.1230 | 0.0643 | ±0.1286 | -1.913 | 0.0558 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **872**, R² = **0.2668**, Adj R² = **0.2548**, F-statistic = **22.27** (p = **6.11e-49**), Residual SE = **5.762** on **857** df, AIC = **5543.7**, BIC = **5615.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8732** | 6.4308 | ±12.8616 | **+9.777** | **1.41e-22** | *** |
| **Education: graduate level (vs college)** | **+1.1786** | 0.4198 | ±0.8397 | **+2.807** | **0.0050** | ** |
| Education: high school or below (vs college) | +0.6270 | 0.7771 | ±1.5541 | +0.807 | 0.4198 |  |
| **Site: UCSD (vs UAB)** | **+3.3097** | 0.5321 | ±1.0643 | **+6.220** | **4.98e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5264** | 0.5076 | ±1.0151 | **-3.007** | **0.0026** | ** |
| **Season: spring (vs autumn)** | **-1.1263** | 0.5650 | ±1.1301 | **-1.993** | **0.0462** | * |
| **Season: summer (vs autumn)** | **+2.1129** | 0.5893 | ±1.1787 | **+3.585** | **3.37e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0790** | 0.5920 | ±1.1839 | **-8.580** | **9.50e-18** | *** |
| **Age (years)** | **-0.0385** | 0.0186 | ±0.0371 | **-2.074** | **0.0380** | * |
| BMI (kg/m2) | -0.0526 | 0.0285 | ±0.0569 | -1.849 | 0.0644 | . |
| Hypertension | +0.2029 | 0.4538 | ±0.9075 | +0.447 | 0.6547 |  |
| **High cholesterol** | **-1.1176** | 0.4188 | ±0.8375 | **-2.669** | **0.0076** | ** |
| Kidney disease | +0.0999 | 0.6983 | ±1.3967 | +0.143 | 0.8863 |  |
| Circulatory disease | -0.5671 | 0.5866 | ±1.1733 | -0.967 | 0.3337 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.1348** | 0.0641 | ±0.1282 | **-2.102** | **0.0355** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **872**, R² = **0.2627**, Adj R² = **0.2507**, F-statistic = **21.81** (p = **5.86e-48**), Residual SE = **5.778** on **857** df, AIC = **5548.5**, BIC = **5620.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3930** | 1.5488 | ±3.0976 | **+31.891** | **3.51e-223** | *** |
| **Education: graduate level (vs college)** | **+1.2104** | 0.4206 | ±0.8412 | **+2.878** | **0.0040** | ** |
| Education: high school or below (vs college) | +0.6850 | 0.7795 | ±1.5589 | +0.879 | 0.3795 |  |
| **Site: UCSD (vs UAB)** | **+3.2209** | 0.5304 | ±1.0607 | **+6.073** | **1.26e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5395** | 0.5092 | ±1.0184 | **-3.023** | **0.0025** | ** |
| **Season: spring (vs autumn)** | **-1.1476** | 0.5664 | ±1.1329 | **-2.026** | **0.0428** | * |
| **Season: summer (vs autumn)** | **+2.1354** | 0.5882 | ±1.1764 | **+3.630** | **2.83e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1037** | 0.5949 | ±1.1898 | **-8.579** | **9.56e-18** | *** |
| **Age (years)** | **-0.0369** | 0.0186 | ±0.0372 | **-1.984** | **0.0472** | * |
| BMI (kg/m2) | -0.0483 | 0.0283 | ±0.0566 | -1.704 | 0.0883 | . |
| Hypertension | +0.2829 | 0.4519 | ±0.9038 | +0.626 | 0.5313 |  |
| **High cholesterol** | **-1.0743** | 0.4203 | ±0.8406 | **-2.556** | **0.0106** | * |
| Kidney disease | +0.2521 | 0.7195 | ±1.4390 | +0.350 | 0.7261 |  |
| Circulatory disease | -0.4798 | 0.5948 | ±1.1895 | -0.807 | 0.4198 |  |
| Time 54-69, pooled (%) | +0.1777 | 0.4251 | ±0.8503 | +0.418 | 0.6760 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **872**, R² = **0.2626**, Adj R² = **0.2506**, F-statistic = **21.80** (p = **6.23e-48**), Residual SE = **5.778** on **857** df, AIC = **5548.6**, BIC = **5620.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4153** | 1.5478 | ±3.0956 | **+31.926** | **1.16e-223** | *** |
| **Education: graduate level (vs college)** | **+1.2044** | 0.4205 | ±0.8411 | **+2.864** | **0.0042** | ** |
| Education: high school or below (vs college) | +0.6798 | 0.7790 | ±1.5580 | +0.873 | 0.3828 |  |
| **Site: UCSD (vs UAB)** | **+3.2209** | 0.5302 | ±1.0605 | **+6.075** | **1.24e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5418** | 0.5092 | ±1.0184 | **-3.028** | **0.0025** | ** |
| **Season: spring (vs autumn)** | **-1.1466** | 0.5668 | ±1.1336 | **-2.023** | **0.0431** | * |
| **Season: summer (vs autumn)** | **+2.1397** | 0.5889 | ±1.1778 | **+3.633** | **2.80e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1004** | 0.5951 | ±1.1902 | **-8.571** | **1.03e-17** | *** |
| **Age (years)** | **-0.0369** | 0.0186 | ±0.0372 | **-1.984** | **0.0473** | * |
| BMI (kg/m2) | -0.0484 | 0.0283 | ±0.0567 | -1.710 | 0.0873 | . |
| Hypertension | +0.2822 | 0.4520 | ±0.9039 | +0.624 | 0.5324 |  |
| **High cholesterol** | **-1.0724** | 0.4202 | ±0.8404 | **-2.552** | **0.0107** | * |
| Kidney disease | +0.2484 | 0.7198 | ±1.4396 | +0.345 | 0.7300 |  |
| Circulatory disease | -0.4808 | 0.5951 | ±1.1901 | -0.808 | 0.4191 |  |
| Avg. daily time 54-69 (%) | +0.0972 | 0.4008 | ±0.8016 | +0.243 | 0.8083 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **872**, R² = **0.2627**, Adj R² = **0.2507**, F-statistic = **21.81** (p = **5.86e-48**), Residual SE = **5.778** on **857** df, AIC = **5548.5**, BIC = **5620.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.3930** | 1.5488 | ±3.0976 | **+31.891** | **3.51e-223** | *** |
| **Education: graduate level (vs college)** | **+1.2104** | 0.4206 | ±0.8412 | **+2.878** | **0.0040** | ** |
| Education: high school or below (vs college) | +0.6850 | 0.7795 | ±1.5589 | +0.879 | 0.3795 |  |
| **Site: UCSD (vs UAB)** | **+3.2209** | 0.5304 | ±1.0607 | **+6.073** | **1.26e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5395** | 0.5092 | ±1.0184 | **-3.023** | **0.0025** | ** |
| **Season: spring (vs autumn)** | **-1.1476** | 0.5664 | ±1.1329 | **-2.026** | **0.0428** | * |
| **Season: summer (vs autumn)** | **+2.1354** | 0.5882 | ±1.1764 | **+3.630** | **2.83e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1037** | 0.5949 | ±1.1898 | **-8.579** | **9.56e-18** | *** |
| **Age (years)** | **-0.0369** | 0.0186 | ±0.0372 | **-1.984** | **0.0472** | * |
| BMI (kg/m2) | -0.0483 | 0.0283 | ±0.0566 | -1.704 | 0.0883 | . |
| Hypertension | +0.2829 | 0.4519 | ±0.9038 | +0.626 | 0.5313 |  |
| **High cholesterol** | **-1.0743** | 0.4203 | ±0.8406 | **-2.556** | **0.0106** | * |
| Kidney disease | +0.2521 | 0.7195 | ±1.4390 | +0.350 | 0.7261 |  |
| Circulatory disease | -0.4798 | 0.5948 | ±1.1895 | -0.807 | 0.4198 |  |
| Time < 70 (%) | +0.1777 | 0.4251 | ±0.8503 | +0.418 | 0.6760 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **872**, R² = **0.2626**, Adj R² = **0.2506**, F-statistic = **21.80** (p = **6.23e-48**), Residual SE = **5.778** on **857** df, AIC = **5548.6**, BIC = **5620.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4153** | 1.5478 | ±3.0956 | **+31.926** | **1.16e-223** | *** |
| **Education: graduate level (vs college)** | **+1.2044** | 0.4205 | ±0.8411 | **+2.864** | **0.0042** | ** |
| Education: high school or below (vs college) | +0.6798 | 0.7790 | ±1.5580 | +0.873 | 0.3828 |  |
| **Site: UCSD (vs UAB)** | **+3.2209** | 0.5302 | ±1.0605 | **+6.075** | **1.24e-09** | *** |
| **Site: UW (vs UAB)** | **-1.5418** | 0.5092 | ±1.0184 | **-3.028** | **0.0025** | ** |
| **Season: spring (vs autumn)** | **-1.1466** | 0.5668 | ±1.1336 | **-2.023** | **0.0431** | * |
| **Season: summer (vs autumn)** | **+2.1397** | 0.5889 | ±1.1778 | **+3.633** | **2.80e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1004** | 0.5951 | ±1.1902 | **-8.571** | **1.03e-17** | *** |
| **Age (years)** | **-0.0369** | 0.0186 | ±0.0372 | **-1.984** | **0.0473** | * |
| BMI (kg/m2) | -0.0484 | 0.0283 | ±0.0567 | -1.710 | 0.0873 | . |
| Hypertension | +0.2822 | 0.4520 | ±0.9039 | +0.624 | 0.5324 |  |
| **High cholesterol** | **-1.0724** | 0.4202 | ±0.8404 | **-2.552** | **0.0107** | * |
| Kidney disease | +0.2484 | 0.7198 | ±1.4396 | +0.345 | 0.7300 |  |
| Circulatory disease | -0.4808 | 0.5951 | ±1.1901 | -0.808 | 0.4191 |  |
| Avg. daily time < 70 (%) | +0.0972 | 0.4008 | ±0.8016 | +0.243 | 0.8083 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **872**, R² = **0.2660**, Adj R² = **0.2540**, F-statistic = **22.18** (p = **9.61e-49**), Residual SE = **5.765** on **857** df, AIC = **5544.7**, BIC = **5616.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4281** | 1.5556 | ±3.1112 | **+31.775** | **1.45e-221** | *** |
| **Education: graduate level (vs college)** | **+1.1692** | 0.4203 | ±0.8406 | **+2.782** | **0.0054** | ** |
| Education: high school or below (vs college) | +0.6119 | 0.7763 | ±1.5527 | +0.788 | 0.4305 |  |
| **Site: UCSD (vs UAB)** | **+3.3020** | 0.5326 | ±1.0653 | **+6.199** | **5.68e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5314** | 0.5079 | ±1.0157 | **-3.015** | **0.0026** | ** |
| **Season: spring (vs autumn)** | **-1.1318** | 0.5654 | ±1.1309 | **-2.002** | **0.0453** | * |
| **Season: summer (vs autumn)** | **+2.1212** | 0.5903 | ±1.1806 | **+3.594** | **3.26e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0772** | 0.5924 | ±1.1849 | **-8.570** | **1.04e-17** | *** |
| **Age (years)** | **-0.0384** | 0.0186 | ±0.0372 | **-2.069** | **0.0386** | * |
| BMI (kg/m2) | -0.0523 | 0.0284 | ±0.0568 | -1.839 | 0.0659 | . |
| Hypertension | +0.2115 | 0.4546 | ±0.9092 | +0.465 | 0.6418 |  |
| **High cholesterol** | **-1.1089** | 0.4190 | ±0.8380 | **-2.647** | **0.0081** | ** |
| Kidney disease | +0.1168 | 0.7016 | ±1.4031 | +0.166 | 0.8678 |  |
| Circulatory disease | -0.5596 | 0.5874 | ±1.1749 | -0.953 | 0.3408 |  |
| Time 181-250, pooled (%) | +0.1174 | 0.0636 | ±0.1272 | +1.845 | 0.0650 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **872**, R² = **0.2666**, Adj R² = **0.2546**, F-statistic = **22.25** (p = **6.87e-49**), Residual SE = **5.763** on **857** df, AIC = **5544.0**, BIC = **5615.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4266** | 1.5564 | ±3.1128 | **+31.757** | **2.56e-221** | *** |
| **Education: graduate level (vs college)** | **+1.1675** | 0.4201 | ±0.8402 | **+2.779** | **0.0054** | ** |
| Education: high school or below (vs college) | +0.6176 | 0.7764 | ±1.5529 | +0.795 | 0.4263 |  |
| **Site: UCSD (vs UAB)** | **+3.3136** | 0.5324 | ±1.0649 | **+6.223** | **4.86e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5289** | 0.5076 | ±1.0153 | **-3.012** | **0.0026** | ** |
| **Season: spring (vs autumn)** | **-1.1290** | 0.5652 | ±1.1304 | **-1.997** | **0.0458** | * |
| **Season: summer (vs autumn)** | **+2.1165** | 0.5899 | ±1.1798 | **+3.588** | **3.33e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0717** | 0.5923 | ±1.1845 | **-8.563** | **1.10e-17** | *** |
| **Age (years)** | **-0.0384** | 0.0186 | ±0.0371 | **-2.066** | **0.0388** | * |
| BMI (kg/m2) | -0.0528 | 0.0284 | ±0.0569 | -1.856 | 0.0635 | . |
| Hypertension | +0.2045 | 0.4540 | ±0.9079 | +0.450 | 0.6524 |  |
| **High cholesterol** | **-1.1134** | 0.4189 | ±0.8377 | **-2.658** | **0.0079** | ** |
| Kidney disease | +0.0992 | 0.6994 | ±1.3987 | +0.142 | 0.8872 |  |
| Circulatory disease | -0.5719 | 0.5873 | ±1.1747 | -0.974 | 0.3302 |  |
| **Avg. daily time 181-250 (%)** | **+0.1303** | 0.0636 | ±0.1271 | **+2.050** | **0.0404** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **872**, R² = **0.2660**, Adj R² = **0.2540**, F-statistic = **22.18** (p = **9.61e-49**), Residual SE = **5.765** on **857** df, AIC = **5544.7**, BIC = **5616.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4281** | 1.5556 | ±3.1112 | **+31.775** | **1.45e-221** | *** |
| **Education: graduate level (vs college)** | **+1.1692** | 0.4203 | ±0.8406 | **+2.782** | **0.0054** | ** |
| Education: high school or below (vs college) | +0.6119 | 0.7763 | ±1.5527 | +0.788 | 0.4305 |  |
| **Site: UCSD (vs UAB)** | **+3.3020** | 0.5326 | ±1.0653 | **+6.199** | **5.68e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5314** | 0.5079 | ±1.0157 | **-3.015** | **0.0026** | ** |
| **Season: spring (vs autumn)** | **-1.1318** | 0.5654 | ±1.1309 | **-2.002** | **0.0453** | * |
| **Season: summer (vs autumn)** | **+2.1212** | 0.5903 | ±1.1806 | **+3.594** | **3.26e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0772** | 0.5924 | ±1.1849 | **-8.570** | **1.04e-17** | *** |
| **Age (years)** | **-0.0384** | 0.0186 | ±0.0372 | **-2.069** | **0.0386** | * |
| BMI (kg/m2) | -0.0523 | 0.0284 | ±0.0568 | -1.839 | 0.0659 | . |
| Hypertension | +0.2115 | 0.4546 | ±0.9092 | +0.465 | 0.6418 |  |
| **High cholesterol** | **-1.1089** | 0.4190 | ±0.8380 | **-2.647** | **0.0081** | ** |
| Kidney disease | +0.1168 | 0.7016 | ±1.4031 | +0.166 | 0.8678 |  |
| Circulatory disease | -0.5596 | 0.5874 | ±1.1749 | -0.953 | 0.3408 |  |
| Time > 180 (%) | +0.1174 | 0.0636 | ±0.1272 | +1.845 | 0.0650 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **872**, R² = **0.2666**, Adj R² = **0.2546**, F-statistic = **22.25** (p = **6.87e-49**), Residual SE = **5.763** on **857** df, AIC = **5544.0**, BIC = **5615.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4266** | 1.5564 | ±3.1128 | **+31.757** | **2.56e-221** | *** |
| **Education: graduate level (vs college)** | **+1.1675** | 0.4201 | ±0.8402 | **+2.779** | **0.0054** | ** |
| Education: high school or below (vs college) | +0.6176 | 0.7764 | ±1.5529 | +0.795 | 0.4263 |  |
| **Site: UCSD (vs UAB)** | **+3.3136** | 0.5324 | ±1.0649 | **+6.223** | **4.86e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5289** | 0.5076 | ±1.0153 | **-3.012** | **0.0026** | ** |
| **Season: spring (vs autumn)** | **-1.1290** | 0.5652 | ±1.1304 | **-1.997** | **0.0458** | * |
| **Season: summer (vs autumn)** | **+2.1165** | 0.5899 | ±1.1798 | **+3.588** | **3.33e-04** | *** |
| **Season: winter (vs autumn)** | **-5.0717** | 0.5923 | ±1.1845 | **-8.563** | **1.10e-17** | *** |
| **Age (years)** | **-0.0384** | 0.0186 | ±0.0371 | **-2.066** | **0.0388** | * |
| BMI (kg/m2) | -0.0528 | 0.0284 | ±0.0569 | -1.856 | 0.0635 | . |
| Hypertension | +0.2045 | 0.4540 | ±0.9079 | +0.450 | 0.6524 |  |
| **High cholesterol** | **-1.1134** | 0.4189 | ±0.8377 | **-2.658** | **0.0079** | ** |
| Kidney disease | +0.0992 | 0.6994 | ±1.3987 | +0.142 | 0.8872 |  |
| Circulatory disease | -0.5719 | 0.5873 | ±1.1747 | -0.974 | 0.3302 |  |
| **Avg. daily time > 180 (%)** | **+0.1303** | 0.0636 | ±0.1271 | **+2.050** | **0.0404** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 872)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **872**, R² = **0.2655**, Adj R² = **0.2535**, F-statistic = **22.12** (p = **1.26e-48**), Residual SE = **5.767** on **857** df, AIC = **5545.3**, BIC = **5616.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4960** | 1.5485 | ±3.0970 | **+31.964** | **3.48e-224** | *** |
| **Education: graduate level (vs college)** | **+1.1969** | 0.4195 | ±0.8391 | **+2.853** | **0.0043** | ** |
| Education: high school or below (vs college) | +0.5701 | 0.7766 | ±1.5531 | +0.734 | 0.4629 |  |
| **Site: UCSD (vs UAB)** | **+3.2917** | 0.5328 | ±1.0655 | **+6.179** | **6.47e-10** | *** |
| **Site: UW (vs UAB)** | **-1.5195** | 0.5091 | ±1.0181 | **-2.985** | **0.0028** | ** |
| **Season: spring (vs autumn)** | **-1.1640** | 0.5652 | ±1.1303 | **-2.059** | **0.0394** | * |
| **Season: summer (vs autumn)** | **+2.0988** | 0.5882 | ±1.1764 | **+3.568** | **3.59e-04** | *** |
| **Season: winter (vs autumn)** | **-5.1052** | 0.5920 | ±1.1840 | **-8.624** | **6.48e-18** | *** |
| Age (years) | -0.0359 | 0.0186 | ±0.0373 | -1.925 | 0.0542 | . |
| BMI (kg/m2) | -0.0558 | 0.0285 | ±0.0569 | -1.959 | 0.0501 | . |
| Hypertension | +0.2867 | 0.4528 | ±0.9057 | +0.633 | 0.5267 |  |
| **High cholesterol** | **-1.1433** | 0.4202 | ±0.8404 | **-2.721** | **0.0065** | ** |
| Kidney disease | +0.1648 | 0.7094 | ±1.4189 | +0.232 | 0.8164 |  |
| Circulatory disease | -0.5312 | 0.5924 | ±1.1849 | -0.897 | 0.3699 |  |
| Nocturnal time > 180 (%) | +0.0998 | 0.0578 | ±0.1155 | +1.729 | 0.0839 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 872; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **872**, R² = **0.0503**, Adj R² = **0.0359**, F-statistic = **3.49** (p = **2.49e-05**), Residual SE = **15.631** on **858** df, AIC = **7283.3**, BIC = **7350.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5289** | 4.4723 | ±8.9447 | **+28.515** | **7.62e-179** | *** |
| **Education: graduate level (vs college)** | **-2.7893** | 1.1194 | ±2.2388 | **-2.492** | **0.0127** | * |
| **Education: high school or below (vs college)** | **+4.8557** | 2.1167 | ±4.2333 | **+2.294** | **0.0218** | * |
| Site: UCSD (vs UAB) | +1.3405 | 1.4016 | ±2.8032 | +0.956 | 0.3389 |  |
| Site: UW (vs UAB) | +0.2180 | 1.3842 | ±2.7684 | +0.158 | 0.8748 |  |
| Season: spring (vs autumn) | +2.5402 | 1.5130 | ±3.0260 | +1.679 | 0.0932 | . |
| Season: summer (vs autumn) | +2.1912 | 1.6545 | ±3.3091 | +1.324 | 0.1854 |  |
| **Season: winter (vs autumn)** | **+4.2175** | 1.6004 | ±3.2007 | **+2.635** | **0.0084** | ** |
| **Age (years)** | **-0.1289** | 0.0548 | ±0.1095 | **-2.354** | **0.0186** | * |
| **BMI (kg/m2)** | **+0.1583** | 0.0726 | ±0.1452 | **+2.180** | **0.0292** | * |
| Hypertension | +0.7867 | 1.2164 | ±2.4327 | +0.647 | 0.5178 |  |
| High cholesterol | -0.2576 | 1.1229 | ±2.2458 | -0.229 | 0.8186 |  |
| Kidney disease | -2.1917 | 1.6929 | ±3.3857 | -1.295 | 0.1954 |  |
| Circulatory disease | +0.5383 | 1.6596 | ±3.3193 | +0.324 | 0.7457 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **872**, R² = **0.0505**, Adj R² = **0.0349**, F-statistic = **3.25** (p = **4.59e-05**), Residual SE = **15.639** on **857** df, AIC = **7285.1**, BIC = **7356.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.3721** | 8.9717 | ±17.9433 | **+14.532** | **7.65e-48** | *** |
| **Education: graduate level (vs college)** | **-2.7873** | 1.1209 | ±2.2419 | **-2.487** | **0.0129** | * |
| **Education: high school or below (vs college)** | **+4.8951** | 2.1310 | ±4.2619 | **+2.297** | **0.0216** | * |
| Site: UCSD (vs UAB) | +1.3361 | 1.4027 | ±2.8054 | +0.953 | 0.3408 |  |
| Site: UW (vs UAB) | +0.2132 | 1.3847 | ±2.7695 | +0.154 | 0.8776 |  |
| Season: spring (vs autumn) | +2.4808 | 1.4957 | ±2.9913 | +1.659 | 0.0972 | . |
| Season: summer (vs autumn) | +2.2049 | 1.6688 | ±3.3376 | +1.321 | 0.1864 |  |
| **Season: winter (vs autumn)** | **+4.1816** | 1.5880 | ±3.1759 | **+2.633** | **0.0085** | ** |
| **Age (years)** | **-0.1279** | 0.0550 | ±0.1100 | **-2.324** | **0.0201** | * |
| **BMI (kg/m2)** | **+0.1643** | 0.0727 | ±0.1453 | **+2.262** | **0.0237** | * |
| Hypertension | +0.8497 | 1.2327 | ±2.4653 | +0.689 | 0.4906 |  |
| High cholesterol | -0.1926 | 1.1403 | ±2.2807 | -0.169 | 0.8659 |  |
| Kidney disease | -2.1934 | 1.6977 | ±3.3954 | -1.292 | 0.1964 |  |
| Circulatory disease | +0.5707 | 1.6708 | ±3.3415 | +0.342 | 0.7327 |  |
| HbA1c (%) | -0.5504 | 1.5713 | ±3.1426 | -0.350 | 0.7261 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **872**, R² = **0.0526**, Adj R² = **0.0371**, F-statistic = **3.40** (p = **2.23e-05**), Residual SE = **15.622** on **857** df, AIC = **7283.2**, BIC = **7354.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+134.8108** | 6.5741 | ±13.1481 | **+20.506** | **1.88e-93** | *** |
| **Education: graduate level (vs college)** | **-2.7145** | 1.1225 | ±2.2450 | **-2.418** | **0.0156** | * |
| **Education: high school or below (vs college)** | **+4.9154** | 2.1259 | ±4.2518 | **+2.312** | **0.0208** | * |
| Site: UCSD (vs UAB) | +1.2460 | 1.4025 | ±2.8051 | +0.888 | 0.3743 |  |
| Site: UW (vs UAB) | +0.2684 | 1.3825 | ±2.7651 | +0.194 | 0.8461 |  |
| Season: spring (vs autumn) | +2.5332 | 1.5134 | ±3.0268 | +1.674 | 0.0942 | . |
| Season: summer (vs autumn) | +2.2726 | 1.6709 | ±3.3417 | +1.360 | 0.1738 |  |
| **Season: winter (vs autumn)** | **+4.1721** | 1.5986 | ±3.1972 | **+2.610** | **0.0091** | ** |
| **Age (years)** | **-0.1277** | 0.0549 | ±0.1097 | **-2.328** | **0.0199** | * |
| **BMI (kg/m2)** | **+0.1728** | 0.0726 | ±0.1451 | **+2.381** | **0.0173** | * |
| Hypertension | +0.9898 | 1.2068 | ±2.4137 | +0.820 | 0.4121 |  |
| High cholesterol | -0.2289 | 1.1233 | ±2.2466 | -0.204 | 0.8386 |  |
| Kidney disease | -2.0110 | 1.7067 | ±3.4134 | -1.178 | 0.2387 |  |
| Circulatory disease | +0.6690 | 1.6672 | ±3.3343 | +0.401 | 0.6882 |  |
| Mean glucose (mg/dL) | -0.0656 | 0.0475 | ±0.0950 | -1.381 | 0.1672 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **872**, R² = **0.0526**, Adj R² = **0.0371**, F-statistic = **3.40** (p = **2.23e-05**), Residual SE = **15.622** on **857** df, AIC = **7283.2**, BIC = **7354.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+143.8899** | 12.2558 | ±24.5115 | **+11.741** | **7.89e-32** | *** |
| **Education: graduate level (vs college)** | **-2.7145** | 1.1225 | ±2.2450 | **-2.418** | **0.0156** | * |
| **Education: high school or below (vs college)** | **+4.9154** | 2.1259 | ±4.2518 | **+2.312** | **0.0208** | * |
| Site: UCSD (vs UAB) | +1.2460 | 1.4025 | ±2.8051 | +0.888 | 0.3743 |  |
| Site: UW (vs UAB) | +0.2684 | 1.3825 | ±2.7651 | +0.194 | 0.8461 |  |
| Season: spring (vs autumn) | +2.5332 | 1.5134 | ±3.0268 | +1.674 | 0.0942 | . |
| Season: summer (vs autumn) | +2.2726 | 1.6709 | ±3.3417 | +1.360 | 0.1738 |  |
| **Season: winter (vs autumn)** | **+4.1721** | 1.5986 | ±3.1972 | **+2.610** | **0.0091** | ** |
| **Age (years)** | **-0.1277** | 0.0549 | ±0.1097 | **-2.328** | **0.0199** | * |
| **BMI (kg/m2)** | **+0.1728** | 0.0726 | ±0.1451 | **+2.381** | **0.0173** | * |
| Hypertension | +0.9898 | 1.2068 | ±2.4137 | +0.820 | 0.4121 |  |
| High cholesterol | -0.2289 | 1.1233 | ±2.2466 | -0.204 | 0.8386 |  |
| Kidney disease | -2.0110 | 1.7067 | ±3.4134 | -1.178 | 0.2387 |  |
| Circulatory disease | +0.6690 | 1.6672 | ±3.3343 | +0.401 | 0.6882 |  |
| GMI (%) | -2.7429 | 1.9858 | ±3.9715 | -1.381 | 0.1672 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **872**, R² = **0.0524**, Adj R² = **0.0369**, F-statistic = **3.38** (p = **2.41e-05**), Residual SE = **15.623** on **857** df, AIC = **7283.4**, BIC = **7354.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+133.6271** | 6.1107 | ±12.2214 | **+21.868** | **5.27e-106** | *** |
| **Education: graduate level (vs college)** | **-2.7362** | 1.1214 | ±2.2428 | **-2.440** | **0.0147** | * |
| **Education: high school or below (vs college)** | **+4.9053** | 2.1250 | ±4.2500 | **+2.308** | **0.0210** | * |
| Site: UCSD (vs UAB) | +1.3254 | 1.4014 | ±2.8028 | +0.946 | 0.3443 |  |
| Site: UW (vs UAB) | +0.2812 | 1.3809 | ±2.7618 | +0.204 | 0.8386 |  |
| Season: spring (vs autumn) | +2.5736 | 1.5173 | ±3.0347 | +1.696 | 0.0899 | . |
| Season: summer (vs autumn) | +2.2809 | 1.6717 | ±3.3435 | +1.364 | 0.1724 |  |
| **Season: winter (vs autumn)** | **+4.2185** | 1.6051 | ±3.2101 | **+2.628** | **0.0086** | ** |
| **Age (years)** | **-0.1332** | 0.0548 | ±0.1096 | **-2.431** | **0.0151** | * |
| **BMI (kg/m2)** | **+0.1819** | 0.0729 | ±0.1458 | **+2.496** | **0.0126** | * |
| Hypertension | +0.9150 | 1.2113 | ±2.4226 | +0.755 | 0.4500 |  |
| High cholesterol | -0.1745 | 1.1291 | ±2.2582 | -0.155 | 0.8772 |  |
| Kidney disease | -2.1304 | 1.7101 | ±3.4201 | -1.246 | 0.2128 |  |
| Circulatory disease | +0.6499 | 1.6629 | ±3.3259 | +0.391 | 0.6960 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0556 | 0.0403 | ±0.0806 | -1.380 | 0.1675 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **872**, R² = **0.0527**, Adj R² = **0.0372**, F-statistic = **3.40** (p = **2.17e-05**), Residual SE = **15.621** on **857** df, AIC = **7283.1**, BIC = **7354.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.8021** | 4.7186 | ±9.4372 | **+27.720** | **3.96e-169** | *** |
| **Education: graduate level (vs college)** | **-2.8152** | 1.1174 | ±2.2347 | **-2.519** | **0.0118** | * |
| **Education: high school or below (vs college)** | **+5.0589** | 2.1309 | ±4.2618 | **+2.374** | **0.0176** | * |
| Site: UCSD (vs UAB) | +1.1745 | 1.4113 | ±2.8226 | +0.832 | 0.4053 |  |
| Site: UW (vs UAB) | +0.1821 | 1.3794 | ±2.7588 | +0.132 | 0.8950 |  |
| Season: spring (vs autumn) | +2.5601 | 1.5192 | ±3.0385 | +1.685 | 0.0920 | . |
| Season: summer (vs autumn) | +2.2315 | 1.6626 | ±3.3253 | +1.342 | 0.1796 |  |
| **Season: winter (vs autumn)** | **+4.2571** | 1.6090 | ±3.2180 | **+2.646** | **0.0081** | ** |
| **Age (years)** | **-0.1242** | 0.0555 | ±0.1110 | **-2.237** | **0.0253** | * |
| **BMI (kg/m2)** | **+0.1648** | 0.0721 | ±0.1443 | **+2.285** | **0.0223** | * |
| Hypertension | +1.0207 | 1.2138 | ±2.4277 | +0.841 | 0.4004 |  |
| High cholesterol | -0.2153 | 1.1248 | ±2.2496 | -0.191 | 0.8482 |  |
| Kidney disease | -1.9709 | 1.6868 | ±3.3735 | -1.168 | 0.2426 |  |
| Circulatory disease | +0.6112 | 1.6609 | ±3.3217 | +0.368 | 0.7129 |  |
| Glucose SD, pooled (mg/dL) | -0.1948 | 0.1414 | ±0.2829 | -1.377 | 0.1684 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **872**, R² = **0.0525**, Adj R² = **0.0370**, F-statistic = **3.39** (p = **2.30e-05**), Residual SE = **15.622** on **857** df, AIC = **7283.2**, BIC = **7354.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.4316** | 4.5856 | ±9.1713 | **+28.443** | **5.87e-178** | *** |
| **Education: graduate level (vs college)** | **-2.7983** | 1.1179 | ±2.2358 | **-2.503** | **0.0123** | * |
| **Education: high school or below (vs college)** | **+5.0257** | 2.1294 | ±4.2587 | **+2.360** | **0.0183** | * |
| Site: UCSD (vs UAB) | +1.1914 | 1.4082 | ±2.8164 | +0.846 | 0.3975 |  |
| Site: UW (vs UAB) | +0.1999 | 1.3789 | ±2.7578 | +0.145 | 0.8847 |  |
| Season: spring (vs autumn) | +2.5193 | 1.5121 | ±3.0242 | +1.666 | 0.0957 | . |
| Season: summer (vs autumn) | +2.1832 | 1.6585 | ±3.3171 | +1.316 | 0.1881 |  |
| **Season: winter (vs autumn)** | **+4.2019** | 1.5993 | ±3.1987 | **+2.627** | **0.0086** | ** |
| **Age (years)** | **-0.1242** | 0.0556 | ±0.1113 | **-2.233** | **0.0256** | * |
| **BMI (kg/m2)** | **+0.1653** | 0.0722 | ±0.1445 | **+2.288** | **0.0222** | * |
| Hypertension | +1.0174 | 1.2088 | ±2.4176 | +0.842 | 0.4000 |  |
| High cholesterol | -0.2306 | 1.1241 | ±2.2482 | -0.205 | 0.8375 |  |
| Kidney disease | -1.9940 | 1.6872 | ±3.3744 | -1.182 | 0.2373 |  |
| Circulatory disease | +0.5737 | 1.6593 | ±3.3186 | +0.346 | 0.7295 |  |
| Avg. daily SD (mg/dL) | -0.1903 | 0.1422 | ±0.2844 | -1.338 | 0.1808 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **872**, R² = **0.0511**, Adj R² = **0.0356**, F-statistic = **3.30** (p = **3.66e-05**), Residual SE = **15.634** on **857** df, AIC = **7284.5**, BIC = **7356.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.0393** | 4.9924 | ±9.9848 | **+26.048** | **1.43e-149** | *** |
| **Education: graduate level (vs college)** | **-2.8378** | 1.1184 | ±2.2368 | **-2.537** | **0.0112** | * |
| **Education: high school or below (vs college)** | **+4.9718** | 2.1213 | ±4.2425 | **+2.344** | **0.0191** | * |
| Site: UCSD (vs UAB) | +1.2554 | 1.4113 | ±2.8226 | +0.890 | 0.3737 |  |
| Site: UW (vs UAB) | +0.1789 | 1.3845 | ±2.7689 | +0.129 | 0.8972 |  |
| Season: spring (vs autumn) | +2.5581 | 1.5184 | ±3.0367 | +1.685 | 0.0920 | . |
| Season: summer (vs autumn) | +2.1972 | 1.6559 | ±3.3118 | +1.327 | 0.1845 |  |
| **Season: winter (vs autumn)** | **+4.2714** | 1.6109 | ±3.2217 | **+2.652** | **0.0080** | ** |
| **Age (years)** | **-0.1260** | 0.0554 | ±0.1108 | **-2.274** | **0.0230** | * |
| **BMI (kg/m2)** | **+0.1578** | 0.0725 | ±0.1449 | **+2.178** | **0.0294** | * |
| Hypertension | +0.8824 | 1.2198 | ±2.4397 | +0.723 | 0.4694 |  |
| High cholesterol | -0.2433 | 1.1247 | ±2.2494 | -0.216 | 0.8287 |  |
| Kidney disease | -2.0991 | 1.6835 | ±3.3670 | -1.247 | 0.2124 |  |
| Circulatory disease | +0.5402 | 1.6583 | ±3.3165 | +0.326 | 0.7446 |  |
| CV (%) | -0.1647 | 0.1877 | ±0.3753 | -0.877 | 0.3803 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **872**, R² = **0.0512**, Adj R² = **0.0357**, F-statistic = **3.30** (p = **3.63e-05**), Residual SE = **15.633** on **857** df, AIC = **7284.5**, BIC = **7356.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.7109** | 5.8516 | ±11.7033 | **+21.312** | **8.77e-101** | *** |
| **Education: graduate level (vs college)** | **-2.8462** | 1.1170 | ±2.2340 | **-2.548** | **0.0108** | * |
| **Education: high school or below (vs college)** | **+4.9649** | 2.1194 | ±4.2388 | **+2.343** | **0.0191** | * |
| Site: UCSD (vs UAB) | +1.2739 | 1.4075 | ±2.8151 | +0.905 | 0.3655 |  |
| Site: UW (vs UAB) | +0.1980 | 1.3828 | ±2.7657 | +0.143 | 0.8861 |  |
| Season: spring (vs autumn) | +2.5750 | 1.5226 | ±3.0453 | +1.691 | 0.0908 | . |
| Season: summer (vs autumn) | +2.1923 | 1.6550 | ±3.3100 | +1.325 | 0.1853 |  |
| **Season: winter (vs autumn)** | **+4.2764** | 1.6111 | ±3.2222 | **+2.654** | **0.0079** | ** |
| **Age (years)** | **-0.1262** | 0.0554 | ±0.1107 | **-2.280** | **0.0226** | * |
| **BMI (kg/m2)** | **+0.1583** | 0.0725 | ±0.1449 | **+2.184** | **0.0289** | * |
| Hypertension | +0.8815 | 1.2194 | ±2.4388 | +0.723 | 0.4697 |  |
| High cholesterol | -0.2479 | 1.1242 | ±2.2485 | -0.221 | 0.8255 |  |
| Kidney disease | -2.1008 | 1.6855 | ±3.3710 | -1.246 | 0.2126 |  |
| Circulatory disease | +0.5259 | 1.6591 | ±3.3181 | +0.317 | 0.7512 |  |
| Mean / SD ratio | +0.4158 | 0.4802 | ±0.9605 | +0.866 | 0.3866 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **872**, R² = **0.0509**, Adj R² = **0.0354**, F-statistic = **3.28** (p = **4.01e-05**), Residual SE = **15.636** on **857** df, AIC = **7284.7**, BIC = **7356.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.3922** | 5.7783 | ±11.5565 | **+21.701** | **2.02e-104** | *** |
| **Education: graduate level (vs college)** | **-2.8293** | 1.1171 | ±2.2342 | **-2.533** | **0.0113** | * |
| **Education: high school or below (vs college)** | **+4.9288** | 2.1193 | ±4.2385 | **+2.326** | **0.0200** | * |
| Site: UCSD (vs UAB) | +1.2966 | 1.4042 | ±2.8084 | +0.923 | 0.3558 |  |
| Site: UW (vs UAB) | +0.2136 | 1.3830 | ±2.7659 | +0.154 | 0.8773 |  |
| Season: spring (vs autumn) | +2.5504 | 1.5182 | ±3.0364 | +1.680 | 0.0930 | . |
| Season: summer (vs autumn) | +2.1709 | 1.6549 | ±3.3097 | +1.312 | 0.1896 |  |
| **Season: winter (vs autumn)** | **+4.2337** | 1.6045 | ±3.2090 | **+2.639** | **0.0083** | ** |
| **Age (years)** | **-0.1264** | 0.0556 | ±0.1111 | **-2.275** | **0.0229** | * |
| **BMI (kg/m2)** | **+0.1597** | 0.0726 | ±0.1451 | **+2.201** | **0.0278** | * |
| Hypertension | +0.8575 | 1.2149 | ±2.4299 | +0.706 | 0.4803 |  |
| High cholesterol | -0.2568 | 1.1238 | ±2.2476 | -0.229 | 0.8192 |  |
| Kidney disease | -2.1195 | 1.6879 | ±3.3758 | -1.256 | 0.2092 |  |
| Circulatory disease | +0.5005 | 1.6596 | ±3.3191 | +0.302 | 0.7630 |  |
| Avg. daily mean/SD | +0.2705 | 0.3843 | ±0.7687 | +0.704 | 0.4816 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **872**, R² = **0.0504**, Adj R² = **0.0349**, F-statistic = **3.25** (p = **4.67e-05**), Residual SE = **15.639** on **857** df, AIC = **7285.1**, BIC = **7356.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.4902** | 5.3531 | ±10.7062 | **+23.629** | **1.93e-123** | *** |
| **Education: graduate level (vs college)** | **-2.7913** | 1.1208 | ±2.2416 | **-2.491** | **0.0128** | * |
| **Education: high school or below (vs college)** | **+4.8064** | 2.1407 | ±4.2813 | **+2.245** | **0.0247** | * |
| Site: UCSD (vs UAB) | +1.3559 | 1.4019 | ±2.8039 | +0.967 | 0.3335 |  |
| Site: UW (vs UAB) | +0.2306 | 1.3851 | ±2.7703 | +0.167 | 0.8678 |  |
| Season: spring (vs autumn) | +2.5371 | 1.5152 | ±3.0304 | +1.674 | 0.0940 | . |
| Season: summer (vs autumn) | +2.2049 | 1.6513 | ±3.3025 | +1.335 | 0.1818 |  |
| **Season: winter (vs autumn)** | **+4.2256** | 1.5992 | ±3.1985 | **+2.642** | **0.0082** | ** |
| **Age (years)** | **-0.1285** | 0.0548 | ±0.1096 | **-2.345** | **0.0190** | * |
| **BMI (kg/m2)** | **+0.1583** | 0.0729 | ±0.1457 | **+2.174** | **0.0297** | * |
| Hypertension | +0.7927 | 1.2190 | ±2.4381 | +0.650 | 0.5155 |  |
| High cholesterol | -0.2582 | 1.1243 | ±2.2487 | -0.230 | 0.8183 |  |
| Kidney disease | -2.2146 | 1.6967 | ±3.3934 | -1.305 | 0.1918 |  |
| Circulatory disease | +0.5550 | 1.6584 | ±3.3167 | +0.335 | 0.7379 |  |
| MAG (mg/dL/h) | +0.0278 | 0.0816 | ±0.1631 | +0.340 | 0.7336 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **872**, R² = **0.0514**, Adj R² = **0.0359**, F-statistic = **3.32** (p = **3.30e-05**), Residual SE = **15.631** on **857** df, AIC = **7284.2**, BIC = **7355.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+130.3348** | 4.8878 | ±9.7756 | **+26.665** | **1.19e-156** | *** |
| **Education: graduate level (vs college)** | **-2.7750** | 1.1200 | ±2.2400 | **-2.478** | **0.0132** | * |
| **Education: high school or below (vs college)** | **+4.9845** | 2.1302 | ±4.2605 | **+2.340** | **0.0193** | * |
| Site: UCSD (vs UAB) | +1.2527 | 1.4076 | ±2.8151 | +0.890 | 0.3735 |  |
| Site: UW (vs UAB) | +0.2090 | 1.3806 | ±2.7612 | +0.151 | 0.8796 |  |
| Season: spring (vs autumn) | +2.5489 | 1.5186 | ±3.0372 | +1.678 | 0.0933 | . |
| Season: summer (vs autumn) | +2.1610 | 1.6554 | ±3.3108 | +1.305 | 0.1918 |  |
| **Season: winter (vs autumn)** | **+4.2003** | 1.5997 | ±3.1993 | **+2.626** | **0.0086** | ** |
| **Age (years)** | **-0.1261** | 0.0555 | ±0.1110 | **-2.273** | **0.0231** | * |
| **BMI (kg/m2)** | **+0.1560** | 0.0725 | ±0.1451 | **+2.151** | **0.0315** | * |
| Hypertension | +0.8966 | 1.2137 | ±2.4274 | +0.739 | 0.4601 |  |
| High cholesterol | -0.2493 | 1.1236 | ±2.2472 | -0.222 | 0.8244 |  |
| Kidney disease | -2.0681 | 1.6873 | ±3.3746 | -1.226 | 0.2203 |  |
| Circulatory disease | +0.5686 | 1.6629 | ±3.3257 | +0.342 | 0.7324 |  |
| Avg. daily range (mg/dL) | -0.0325 | 0.0327 | ±0.0654 | -0.994 | 0.3203 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **872**, R² = **0.0503**, Adj R² = **0.0348**, F-statistic = **3.24** (p = **4.88e-05**), Residual SE = **15.641** on **857** df, AIC = **7285.3**, BIC = **7356.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5918** | 4.5834 | ±9.1669 | **+27.838** | **1.52e-170** | *** |
| **Education: graduate level (vs college)** | **-2.7891** | 1.1214 | ±2.2429 | **-2.487** | **0.0129** | * |
| **Education: high school or below (vs college)** | **+4.8633** | 2.1348 | ±4.2696 | **+2.278** | **0.0227** | * |
| Site: UCSD (vs UAB) | +1.3356 | 1.4099 | ±2.8199 | +0.947 | 0.3435 |  |
| Site: UW (vs UAB) | +0.2156 | 1.3852 | ±2.7703 | +0.156 | 0.8763 |  |
| Season: spring (vs autumn) | +2.5465 | 1.5428 | ±3.0856 | +1.651 | 0.0988 | . |
| Season: summer (vs autumn) | +2.2018 | 1.6975 | ±3.3950 | +1.297 | 0.1946 |  |
| **Season: winter (vs autumn)** | **+4.2226** | 1.6178 | ±3.2356 | **+2.610** | **0.0091** | ** |
| **Age (years)** | **-0.1290** | 0.0548 | ±0.1097 | **-2.352** | **0.0187** | * |
| **BMI (kg/m2)** | **+0.1588** | 0.0725 | ±0.1449 | **+2.191** | **0.0285** | * |
| Hypertension | +0.7870 | 1.2181 | ±2.4363 | +0.646 | 0.5182 |  |
| High cholesterol | -0.2521 | 1.1233 | ±2.2467 | -0.224 | 0.8224 |  |
| Kidney disease | -2.1886 | 1.6941 | ±3.3881 | -1.292 | 0.1964 |  |
| Circulatory disease | +0.5468 | 1.6840 | ±3.3681 | +0.325 | 0.7454 |  |
| SD of daily means (mg/dL) | -0.0138 | 0.2546 | ±0.5091 | -0.054 | 0.9568 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **872**, R² = **0.0507**, Adj R² = **0.0352**, F-statistic = **3.27** (p = **4.18e-05**), Residual SE = **15.637** on **857** df, AIC = **7284.8**, BIC = **7356.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+117.1786** | 20.6230 | ±41.2460 | **+5.682** | **1.33e-08** | *** |
| **Education: graduate level (vs college)** | **-2.7743** | 1.1230 | ±2.2460 | **-2.470** | **0.0135** | * |
| **Education: high school or below (vs college)** | **+4.9009** | 2.1349 | ±4.2697 | **+2.296** | **0.0217** | * |
| Site: UCSD (vs UAB) | +1.2762 | 1.4125 | ±2.8251 | +0.903 | 0.3663 |  |
| Site: UW (vs UAB) | +0.2054 | 1.3843 | ±2.7686 | +0.148 | 0.8820 |  |
| Season: spring (vs autumn) | +2.5256 | 1.5096 | ±3.0192 | +1.673 | 0.0943 | . |
| Season: summer (vs autumn) | +2.2130 | 1.6680 | ±3.3360 | +1.327 | 0.1846 |  |
| **Season: winter (vs autumn)** | **+4.2074** | 1.6001 | ±3.2001 | **+2.630** | **0.0085** | ** |
| **Age (years)** | **-0.1275** | 0.0554 | ±0.1107 | **-2.302** | **0.0213** | * |
| **BMI (kg/m2)** | **+0.1613** | 0.0727 | ±0.1453 | **+2.219** | **0.0265** | * |
| Hypertension | +0.8477 | 1.2135 | ±2.4270 | +0.699 | 0.4848 |  |
| High cholesterol | -0.2213 | 1.1286 | ±2.2572 | -0.196 | 0.8445 |  |
| Kidney disease | -2.0834 | 1.6990 | ±3.3980 | -1.226 | 0.2201 |  |
| Circulatory disease | +0.5992 | 1.6697 | ±3.3394 | +0.359 | 0.7197 |  |
| Time in range 70-180, pooled (%) | +0.1038 | 0.1931 | ±0.3861 | +0.538 | 0.5907 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **872**, R² = **0.0509**, Adj R² = **0.0354**, F-statistic = **3.28** (p = **3.96e-05**), Residual SE = **15.635** on **857** df, AIC = **7284.7**, BIC = **7356.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+115.2000** | 20.7892 | ±41.5784 | **+5.541** | **3.00e-08** | *** |
| **Education: graduate level (vs college)** | **-2.7735** | 1.1227 | ±2.2453 | **-2.470** | **0.0135** | * |
| **Education: high school or below (vs college)** | **+4.8968** | 2.1325 | ±4.2649 | **+2.296** | **0.0217** | * |
| Site: UCSD (vs UAB) | +1.2636 | 1.4128 | ±2.8257 | +0.894 | 0.3711 |  |
| Site: UW (vs UAB) | +0.2026 | 1.3840 | ±2.7680 | +0.146 | 0.8836 |  |
| Season: spring (vs autumn) | +2.5202 | 1.5089 | ±3.0177 | +1.670 | 0.0949 | . |
| Season: summer (vs autumn) | +2.2177 | 1.6678 | ±3.3356 | +1.330 | 0.1836 |  |
| **Season: winter (vs autumn)** | **+4.2032** | 1.5991 | ±3.1982 | **+2.628** | **0.0086** | ** |
| **Age (years)** | **-0.1274** | 0.0553 | ±0.1106 | **-2.303** | **0.0213** | * |
| **BMI (kg/m2)** | **+0.1619** | 0.0727 | ±0.1453 | **+2.228** | **0.0259** | * |
| Hypertension | +0.8587 | 1.2135 | ±2.4270 | +0.708 | 0.4792 |  |
| High cholesterol | -0.2144 | 1.1283 | ±2.2566 | -0.190 | 0.8493 |  |
| Kidney disease | -2.0592 | 1.6982 | ±3.3963 | -1.213 | 0.2253 |  |
| Circulatory disease | +0.6123 | 1.6697 | ±3.3393 | +0.367 | 0.7138 |  |
| Avg. daily time in range 70-180 (%) | +0.1237 | 0.1944 | ±0.3889 | +0.636 | 0.5248 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **872**, R² = **0.0504**, Adj R² = **0.0349**, F-statistic = **3.25** (p = **4.74e-05**), Residual SE = **15.640** on **857** df, AIC = **7285.2**, BIC = **7356.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.4518** | 4.4722 | ±8.9443 | **+28.499** | **1.21e-178** | *** |
| **Education: graduate level (vs college)** | **-2.7637** | 1.1231 | ±2.2462 | **-2.461** | **0.0139** | * |
| **Education: high school or below (vs college)** | **+4.8790** | 2.1193 | ±4.2387 | **+2.302** | **0.0213** | * |
| Site: UCSD (vs UAB) | +1.3317 | 1.4034 | ±2.8067 | +0.949 | 0.3427 |  |
| Site: UW (vs UAB) | +0.2245 | 1.3822 | ±2.7645 | +0.162 | 0.8710 |  |
| Season: spring (vs autumn) | +2.5409 | 1.5137 | ±3.0273 | +1.679 | 0.0932 | . |
| Season: summer (vs autumn) | +2.1801 | 1.6546 | ±3.3093 | +1.318 | 0.1876 |  |
| **Season: winter (vs autumn)** | **+4.2017** | 1.5948 | ±3.1896 | **+2.635** | **0.0084** | ** |
| **Age (years)** | **-0.1291** | 0.0548 | ±0.1097 | **-2.354** | **0.0186** | * |
| **BMI (kg/m2)** | **+0.1589** | 0.0726 | ±0.1453 | **+2.189** | **0.0286** | * |
| Hypertension | +0.7894 | 1.2165 | ±2.4331 | +0.649 | 0.5164 |  |
| High cholesterol | -0.2643 | 1.1249 | ±2.2499 | -0.235 | 0.8143 |  |
| Kidney disease | -2.1781 | 1.6955 | ±3.3910 | -1.285 | 0.1989 |  |
| Circulatory disease | +0.5497 | 1.6605 | ±3.3211 | +0.331 | 0.7406 |  |
| Time 54-69, pooled (%) | +0.3102 | 1.4124 | ±2.8248 | +0.220 | 0.8262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **872**, R² = **0.0503**, Adj R² = **0.0348**, F-statistic = **3.24** (p = **4.87e-05**), Residual SE = **15.640** on **857** df, AIC = **7285.3**, BIC = **7356.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5056** | 4.4740 | ±8.9480 | **+28.499** | **1.20e-178** | *** |
| **Education: graduate level (vs college)** | **-2.7801** | 1.1237 | ±2.2475 | **-2.474** | **0.0134** | * |
| **Education: high school or below (vs college)** | **+4.8643** | 2.1193 | ±4.2386 | **+2.295** | **0.0217** | * |
| Site: UCSD (vs UAB) | +1.3352 | 1.4036 | ±2.8071 | +0.951 | 0.3414 |  |
| Site: UW (vs UAB) | +0.2196 | 1.3834 | ±2.7667 | +0.159 | 0.8739 |  |
| Season: spring (vs autumn) | +2.5417 | 1.5147 | ±3.0295 | +1.678 | 0.0933 | . |
| Season: summer (vs autumn) | +2.1890 | 1.6547 | ±3.3094 | +1.323 | 0.1859 |  |
| **Season: winter (vs autumn)** | **+4.2113** | 1.5944 | ±3.1887 | **+2.641** | **0.0083** | ** |
| **Age (years)** | **-0.1290** | 0.0548 | ±0.1097 | **-2.353** | **0.0186** | * |
| **BMI (kg/m2)** | **+0.1585** | 0.0726 | ±0.1453 | **+2.183** | **0.0291** | * |
| Hypertension | +0.7876 | 1.2167 | ±2.4335 | +0.647 | 0.5174 |  |
| High cholesterol | -0.2596 | 1.1245 | ±2.2489 | -0.231 | 0.8174 |  |
| Kidney disease | -2.1873 | 1.6939 | ±3.3879 | -1.291 | 0.1966 |  |
| Circulatory disease | +0.5442 | 1.6603 | ±3.3205 | +0.328 | 0.7431 |  |
| Avg. daily time 54-69 (%) | +0.1034 | 1.3609 | ±2.7219 | +0.076 | 0.9394 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **872**, R² = **0.0504**, Adj R² = **0.0349**, F-statistic = **3.25** (p = **4.74e-05**), Residual SE = **15.640** on **857** df, AIC = **7285.2**, BIC = **7356.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.4518** | 4.4722 | ±8.9443 | **+28.499** | **1.21e-178** | *** |
| **Education: graduate level (vs college)** | **-2.7637** | 1.1231 | ±2.2462 | **-2.461** | **0.0139** | * |
| **Education: high school or below (vs college)** | **+4.8790** | 2.1193 | ±4.2387 | **+2.302** | **0.0213** | * |
| Site: UCSD (vs UAB) | +1.3317 | 1.4034 | ±2.8067 | +0.949 | 0.3427 |  |
| Site: UW (vs UAB) | +0.2245 | 1.3822 | ±2.7645 | +0.162 | 0.8710 |  |
| Season: spring (vs autumn) | +2.5409 | 1.5137 | ±3.0273 | +1.679 | 0.0932 | . |
| Season: summer (vs autumn) | +2.1801 | 1.6546 | ±3.3093 | +1.318 | 0.1876 |  |
| **Season: winter (vs autumn)** | **+4.2017** | 1.5948 | ±3.1896 | **+2.635** | **0.0084** | ** |
| **Age (years)** | **-0.1291** | 0.0548 | ±0.1097 | **-2.354** | **0.0186** | * |
| **BMI (kg/m2)** | **+0.1589** | 0.0726 | ±0.1453 | **+2.189** | **0.0286** | * |
| Hypertension | +0.7894 | 1.2165 | ±2.4331 | +0.649 | 0.5164 |  |
| High cholesterol | -0.2643 | 1.1249 | ±2.2499 | -0.235 | 0.8143 |  |
| Kidney disease | -2.1781 | 1.6955 | ±3.3910 | -1.285 | 0.1989 |  |
| Circulatory disease | +0.5497 | 1.6605 | ±3.3211 | +0.331 | 0.7406 |  |
| Time < 70 (%) | +0.3102 | 1.4124 | ±2.8248 | +0.220 | 0.8262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **872**, R² = **0.0503**, Adj R² = **0.0348**, F-statistic = **3.24** (p = **4.87e-05**), Residual SE = **15.640** on **857** df, AIC = **7285.3**, BIC = **7356.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5056** | 4.4740 | ±8.9480 | **+28.499** | **1.20e-178** | *** |
| **Education: graduate level (vs college)** | **-2.7801** | 1.1237 | ±2.2475 | **-2.474** | **0.0134** | * |
| **Education: high school or below (vs college)** | **+4.8643** | 2.1193 | ±4.2386 | **+2.295** | **0.0217** | * |
| Site: UCSD (vs UAB) | +1.3352 | 1.4036 | ±2.8071 | +0.951 | 0.3414 |  |
| Site: UW (vs UAB) | +0.2196 | 1.3834 | ±2.7667 | +0.159 | 0.8739 |  |
| Season: spring (vs autumn) | +2.5417 | 1.5147 | ±3.0295 | +1.678 | 0.0933 | . |
| Season: summer (vs autumn) | +2.1890 | 1.6547 | ±3.3094 | +1.323 | 0.1859 |  |
| **Season: winter (vs autumn)** | **+4.2113** | 1.5944 | ±3.1887 | **+2.641** | **0.0083** | ** |
| **Age (years)** | **-0.1290** | 0.0548 | ±0.1097 | **-2.353** | **0.0186** | * |
| **BMI (kg/m2)** | **+0.1585** | 0.0726 | ±0.1453 | **+2.183** | **0.0291** | * |
| Hypertension | +0.7876 | 1.2167 | ±2.4335 | +0.647 | 0.5174 |  |
| High cholesterol | -0.2596 | 1.1245 | ±2.2489 | -0.231 | 0.8174 |  |
| Kidney disease | -2.1873 | 1.6939 | ±3.3879 | -1.291 | 0.1966 |  |
| Circulatory disease | +0.5442 | 1.6603 | ±3.3205 | +0.328 | 0.7431 |  |
| Avg. daily time < 70 (%) | +0.1034 | 1.3609 | ±2.7219 | +0.076 | 0.9394 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **872**, R² = **0.0508**, Adj R² = **0.0353**, F-statistic = **3.28** (p = **4.11e-05**), Residual SE = **15.636** on **857** df, AIC = **7284.8**, BIC = **7356.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5374** | 4.4741 | ±8.9483 | **+28.505** | **1.00e-178** | *** |
| **Education: graduate level (vs college)** | **-2.7647** | 1.1246 | ±2.2492 | **-2.458** | **0.0140** | * |
| **Education: high school or below (vs college)** | **+4.9111** | 2.1369 | ±4.2739 | **+2.298** | **0.0216** | * |
| Site: UCSD (vs UAB) | +1.2701 | 1.4129 | ±2.8257 | +0.899 | 0.3687 |  |
| Site: UW (vs UAB) | +0.2071 | 1.3843 | ±2.7686 | +0.150 | 0.8811 |  |
| Season: spring (vs autumn) | +2.5251 | 1.5095 | ±3.0191 | +1.673 | 0.0944 | . |
| Season: summer (vs autumn) | +2.2102 | 1.6669 | ±3.3339 | +1.326 | 0.1849 |  |
| **Season: winter (vs autumn)** | **+4.2014** | 1.5976 | ±3.1952 | **+2.630** | **0.0085** | ** |
| **Age (years)** | **-0.1275** | 0.0553 | ±0.1107 | **-2.304** | **0.0212** | * |
| **BMI (kg/m2)** | **+0.1616** | 0.0727 | ±0.1454 | **+2.224** | **0.0262** | * |
| Hypertension | +0.8515 | 1.2124 | ±2.4247 | +0.702 | 0.4825 |  |
| High cholesterol | -0.2220 | 1.1283 | ±2.2566 | -0.197 | 0.8440 |  |
| Kidney disease | -2.0736 | 1.7001 | ±3.4002 | -1.220 | 0.2226 |  |
| Circulatory disease | +0.6061 | 1.6701 | ±3.3403 | +0.363 | 0.7167 |  |
| Time 181-250, pooled (%) | -0.1087 | 0.1924 | ±0.3848 | -0.565 | 0.5723 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **872**, R² = **0.0509**, Adj R² = **0.0354**, F-statistic = **3.28** (p = **3.94e-05**), Residual SE = **15.635** on **857** df, AIC = **7284.7**, BIC = **7356.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5390** | 4.4715 | ±8.9431 | **+28.522** | **6.18e-179** | *** |
| **Education: graduate level (vs college)** | **-2.7624** | 1.1245 | ±2.2490 | **-2.457** | **0.0140** | * |
| **Education: high school or below (vs college)** | **+4.9072** | 2.1346 | ±4.2692 | **+2.299** | **0.0215** | * |
| Site: UCSD (vs UAB) | +1.2571 | 1.4136 | ±2.8272 | +0.889 | 0.3739 |  |
| Site: UW (vs UAB) | +0.2044 | 1.3841 | ±2.7682 | +0.148 | 0.8826 |  |
| Season: spring (vs autumn) | +2.5221 | 1.5093 | ±3.0186 | +1.671 | 0.0947 | . |
| Season: summer (vs autumn) | +2.2152 | 1.6673 | ±3.3345 | +1.329 | 0.1840 |  |
| **Season: winter (vs autumn)** | **+4.1958** | 1.5963 | ±3.1926 | **+2.628** | **0.0086** | ** |
| **Age (years)** | **-0.1275** | 0.0553 | ±0.1106 | **-2.307** | **0.0211** | * |
| **BMI (kg/m2)** | **+0.1622** | 0.0727 | ±0.1454 | **+2.232** | **0.0256** | * |
| Hypertension | +0.8600 | 1.2124 | ±2.4247 | +0.709 | 0.4781 |  |
| High cholesterol | -0.2168 | 1.1282 | ±2.2564 | -0.192 | 0.8476 |  |
| Kidney disease | -2.0536 | 1.6993 | ±3.3987 | -1.208 | 0.2269 |  |
| Circulatory disease | +0.6196 | 1.6703 | ±3.3405 | +0.371 | 0.7106 |  |
| Avg. daily time 181-250 (%) | -0.1240 | 0.1937 | ±0.3874 | -0.640 | 0.5220 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **872**, R² = **0.0508**, Adj R² = **0.0353**, F-statistic = **3.28** (p = **4.11e-05**), Residual SE = **15.636** on **857** df, AIC = **7284.8**, BIC = **7356.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5374** | 4.4741 | ±8.9483 | **+28.505** | **1.00e-178** | *** |
| **Education: graduate level (vs college)** | **-2.7647** | 1.1246 | ±2.2492 | **-2.458** | **0.0140** | * |
| **Education: high school or below (vs college)** | **+4.9111** | 2.1369 | ±4.2739 | **+2.298** | **0.0216** | * |
| Site: UCSD (vs UAB) | +1.2701 | 1.4129 | ±2.8257 | +0.899 | 0.3687 |  |
| Site: UW (vs UAB) | +0.2071 | 1.3843 | ±2.7686 | +0.150 | 0.8811 |  |
| Season: spring (vs autumn) | +2.5251 | 1.5095 | ±3.0191 | +1.673 | 0.0944 | . |
| Season: summer (vs autumn) | +2.2102 | 1.6669 | ±3.3339 | +1.326 | 0.1849 |  |
| **Season: winter (vs autumn)** | **+4.2014** | 1.5976 | ±3.1952 | **+2.630** | **0.0085** | ** |
| **Age (years)** | **-0.1275** | 0.0553 | ±0.1107 | **-2.304** | **0.0212** | * |
| **BMI (kg/m2)** | **+0.1616** | 0.0727 | ±0.1454 | **+2.224** | **0.0262** | * |
| Hypertension | +0.8515 | 1.2124 | ±2.4247 | +0.702 | 0.4825 |  |
| High cholesterol | -0.2220 | 1.1283 | ±2.2566 | -0.197 | 0.8440 |  |
| Kidney disease | -2.0736 | 1.7001 | ±3.4002 | -1.220 | 0.2226 |  |
| Circulatory disease | +0.6061 | 1.6701 | ±3.3403 | +0.363 | 0.7167 |  |
| Time > 180 (%) | -0.1087 | 0.1924 | ±0.3848 | -0.565 | 0.5723 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **872**, R² = **0.0509**, Adj R² = **0.0354**, F-statistic = **3.28** (p = **3.94e-05**), Residual SE = **15.635** on **857** df, AIC = **7284.7**, BIC = **7356.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.5390** | 4.4715 | ±8.9431 | **+28.522** | **6.18e-179** | *** |
| **Education: graduate level (vs college)** | **-2.7624** | 1.1245 | ±2.2490 | **-2.457** | **0.0140** | * |
| **Education: high school or below (vs college)** | **+4.9072** | 2.1346 | ±4.2692 | **+2.299** | **0.0215** | * |
| Site: UCSD (vs UAB) | +1.2571 | 1.4136 | ±2.8272 | +0.889 | 0.3739 |  |
| Site: UW (vs UAB) | +0.2044 | 1.3841 | ±2.7682 | +0.148 | 0.8826 |  |
| Season: spring (vs autumn) | +2.5221 | 1.5093 | ±3.0186 | +1.671 | 0.0947 | . |
| Season: summer (vs autumn) | +2.2152 | 1.6673 | ±3.3345 | +1.329 | 0.1840 |  |
| **Season: winter (vs autumn)** | **+4.1958** | 1.5963 | ±3.1926 | **+2.628** | **0.0086** | ** |
| **Age (years)** | **-0.1275** | 0.0553 | ±0.1106 | **-2.307** | **0.0211** | * |
| **BMI (kg/m2)** | **+0.1622** | 0.0727 | ±0.1454 | **+2.232** | **0.0256** | * |
| Hypertension | +0.8600 | 1.2124 | ±2.4247 | +0.709 | 0.4781 |  |
| High cholesterol | -0.2168 | 1.1282 | ±2.2564 | -0.192 | 0.8476 |  |
| Kidney disease | -2.0536 | 1.6993 | ±3.3987 | -1.208 | 0.2269 |  |
| Circulatory disease | +0.6196 | 1.6703 | ±3.3405 | +0.371 | 0.7106 |  |
| Avg. daily time > 180 (%) | -0.1240 | 0.1937 | ±0.3874 | -0.640 | 0.5220 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 872)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **872**, R² = **0.0522**, Adj R² = **0.0367**, F-statistic = **3.37** (p = **2.56e-05**), Residual SE = **15.625** on **857** df, AIC = **7283.5**, BIC = **7355.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.4156** | 4.4665 | ±8.9331 | **+28.527** | **5.47e-179** | *** |
| **Education: graduate level (vs college)** | **-2.7915** | 1.1167 | ±2.2334 | **-2.500** | **0.0124** | * |
| **Education: high school or below (vs college)** | **+5.0515** | 2.1502 | ±4.3005 | **+2.349** | **0.0188** | * |
| Site: UCSD (vs UAB) | +1.2138 | 1.4133 | ±2.8266 | +0.859 | 0.3904 |  |
| Site: UW (vs UAB) | +0.1722 | 1.3848 | ±2.7697 | +0.124 | 0.9010 |  |
| Season: spring (vs autumn) | +2.5708 | 1.5122 | ±3.0244 | +1.700 | 0.0891 | . |
| Season: summer (vs autumn) | +2.2738 | 1.6616 | ±3.3231 | +1.368 | 0.1712 |  |
| **Season: winter (vs autumn)** | **+4.2379** | 1.5992 | ±3.1984 | **+2.650** | **0.0080** | ** |
| **Age (years)** | **-0.1308** | 0.0546 | ±0.1092 | **-2.395** | **0.0166** | * |
| **BMI (kg/m2)** | **+0.1720** | 0.0730 | ±0.1459 | **+2.357** | **0.0184** | * |
| Hypertension | +0.7766 | 1.2177 | ±2.4353 | +0.638 | 0.5236 |  |
| High cholesterol | -0.1173 | 1.1388 | ±2.2775 | -0.103 | 0.9180 |  |
| Kidney disease | -2.0385 | 1.6993 | ±3.3987 | -1.200 | 0.2303 |  |
| Circulatory disease | +0.6246 | 1.6593 | ±3.3186 | +0.376 | 0.7066 |  |
| Nocturnal time > 180 (%) | -0.1923 | 0.1369 | ±0.2739 | -1.404 | 0.1602 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 771; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **771**, R² = **0.1303**, Adj R² = **0.1189**, F-statistic = **11.39** (p = **2.50e-18**), Residual SE = **3970.187** on **760** df, AIC = **14976.8**, BIC = **15027.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17610.0497** | 1219.3992 | ±2438.7985 | **+14.442** | **2.83e-47** | *** |
| **Education: graduate level (vs college)** | **-1006.4026** | 295.4820 | ±590.9639 | **-3.406** | **6.59e-04** | *** |
| Education: high school or below (vs college) | +872.5576 | 631.1397 | ±1262.2794 | +1.383 | 0.1668 |  |
| Site: UCSD (vs UAB) | -10.3326 | 389.3921 | ±778.7842 | -0.027 | 0.9788 |  |
| Site: UW (vs UAB) | -206.8318 | 366.8178 | ±733.6357 | -0.564 | 0.5729 |  |
| **Age (years)** | **-117.2839** | 14.6500 | ±29.3000 | **-8.006** | **1.19e-15** | *** |
| BMI (kg/m2) | -4.7599 | 24.0314 | ±48.0629 | -0.198 | 0.8430 |  |
| Hypertension | +529.2261 | 346.9041 | ±693.8082 | +1.526 | 0.1271 |  |
| High cholesterol | -189.2004 | 291.6013 | ±583.2026 | -0.649 | 0.5164 |  |
| Kidney disease | -236.0257 | 575.1219 | ±1150.2439 | -0.410 | 0.6815 |  |
| **Circulatory disease** | **-1010.8211** | 427.9700 | ±855.9400 | **-2.362** | **0.0182** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **771**, R² = **0.1368**, Adj R² = **0.1243**, F-statistic = **10.94** (p = **6.33e-19**), Residual SE = **3957.981** on **759** df, AIC = **14973.0**, BIC = **15028.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+13191.2392** | 2251.2250 | ±4502.4500 | **+5.860** | **4.64e-09** | *** |
| **Education: graduate level (vs college)** | **-1003.3865** | 294.1974 | ±588.3948 | **-3.411** | **6.48e-04** | *** |
| Education: high school or below (vs college) | +834.1189 | 632.0873 | ±1264.1747 | +1.320 | 0.1870 |  |
| Site: UCSD (vs UAB) | +2.3077 | 387.8319 | ±775.6638 | +0.006 | 0.9953 |  |
| Site: UW (vs UAB) | -191.8740 | 366.4044 | ±732.8088 | -0.524 | 0.6005 |  |
| **Age (years)** | **-118.9088** | 14.5423 | ±29.0846 | **-8.177** | **2.92e-16** | *** |
| BMI (kg/m2) | -13.7654 | 23.3873 | ±46.7747 | -0.589 | 0.5561 |  |
| Hypertension | +424.3186 | 351.1922 | ±702.3843 | +1.208 | 0.2270 |  |
| High cholesterol | -312.4384 | 291.7150 | ±583.4299 | -1.071 | 0.2842 |  |
| Kidney disease | -195.7569 | 566.6824 | ±1133.3648 | -0.345 | 0.7298 |  |
| **Circulatory disease** | **-1083.7265** | 424.3187 | ±848.6374 | **-2.554** | **0.0106** | * |
| **HbA1c (%)** | **+861.6379** | 366.2845 | ±732.5691 | **+2.352** | **0.0187** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **771**, R² = **0.1314**, Adj R² = **0.1188**, F-statistic = **10.44** (p = **5.59e-18**), Residual SE = **3970.280** on **759** df, AIC = **14977.8**, BIC = **15033.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16286.5468** | 1830.6397 | ±3661.2794 | **+8.897** | **5.76e-19** | *** |
| **Education: graduate level (vs college)** | **-1011.4824** | 295.8027 | ±591.6053 | **-3.419** | **6.27e-04** | *** |
| Education: high school or below (vs college) | +878.5146 | 629.8647 | ±1259.7294 | +1.395 | 0.1631 |  |
| Site: UCSD (vs UAB) | +3.1448 | 389.3408 | ±778.6816 | +0.008 | 0.9936 |  |
| Site: UW (vs UAB) | -218.6530 | 366.6914 | ±733.3829 | -0.596 | 0.5510 |  |
| **Age (years)** | **-117.5271** | 14.6443 | ±29.2886 | **-8.025** | **1.01e-15** | *** |
| BMI (kg/m2) | -7.3783 | 24.1427 | ±48.2853 | -0.306 | 0.7599 |  |
| Hypertension | +497.3796 | 348.7981 | ±697.5961 | +1.426 | 0.1539 |  |
| High cholesterol | -202.2161 | 291.5210 | ±583.0421 | -0.694 | 0.4879 |  |
| Kidney disease | -275.0000 | 574.3330 | ±1148.6659 | -0.479 | 0.6321 |  |
| **Circulatory disease** | **-1038.6310** | 429.1437 | ±858.2873 | **-2.420** | **0.0155** | * |
| Mean glucose (mg/dL) | +11.9534 | 12.5761 | ±25.1521 | +0.950 | 0.3419 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **771**, R² = **0.1314**, Adj R² = **0.1188**, F-statistic = **10.44** (p = **5.59e-18**), Residual SE = **3970.280** on **759** df, AIC = **14977.8**, BIC = **15033.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14632.4665** | 3338.7737 | ±6677.5474 | **+4.383** | **1.17e-05** | *** |
| **Education: graduate level (vs college)** | **-1011.4824** | 295.8027 | ±591.6053 | **-3.419** | **6.27e-04** | *** |
| Education: high school or below (vs college) | +878.5146 | 629.8647 | ±1259.7294 | +1.395 | 0.1631 |  |
| Site: UCSD (vs UAB) | +3.1448 | 389.3408 | ±778.6816 | +0.008 | 0.9936 |  |
| Site: UW (vs UAB) | -218.6530 | 366.6914 | ±733.3829 | -0.596 | 0.5510 |  |
| **Age (years)** | **-117.5271** | 14.6443 | ±29.2886 | **-8.025** | **1.01e-15** | *** |
| BMI (kg/m2) | -7.3783 | 24.1427 | ±48.2853 | -0.306 | 0.7599 |  |
| Hypertension | +497.3796 | 348.7981 | ±697.5961 | +1.426 | 0.1539 |  |
| High cholesterol | -202.2161 | 291.5210 | ±583.0421 | -0.694 | 0.4879 |  |
| Kidney disease | -275.0000 | 574.3330 | ±1148.6659 | -0.479 | 0.6321 |  |
| **Circulatory disease** | **-1038.6310** | 429.1437 | ±858.2873 | **-2.420** | **0.0155** | * |
| GMI (%) | +499.7221 | 525.7552 | ±1051.5103 | +0.950 | 0.3419 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **771**, R² = **0.1324**, Adj R² = **0.1198**, F-statistic = **10.53** (p = **3.81e-18**), Residual SE = **3968.112** on **759** df, AIC = **14977.0**, BIC = **15032.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16007.8691** | 1695.2478 | ±3390.4955 | **+9.443** | **3.63e-21** | *** |
| **Education: graduate level (vs college)** | **-1010.7375** | 295.4789 | ±590.9578 | **-3.421** | **6.25e-04** | *** |
| Education: high school or below (vs college) | +868.8320 | 627.8369 | ±1255.6737 | +1.384 | 0.1664 |  |
| Site: UCSD (vs UAB) | -10.8978 | 390.0592 | ±780.1183 | -0.028 | 0.9777 |  |
| Site: UW (vs UAB) | -229.3775 | 365.2990 | ±730.5979 | -0.628 | 0.5301 |  |
| **Age (years)** | **-116.1730** | 14.6330 | ±29.2661 | **-7.939** | **2.04e-15** | *** |
| BMI (kg/m2) | -10.5018 | 24.2185 | ±48.4370 | -0.434 | 0.6646 |  |
| Hypertension | +497.8018 | 345.7354 | ±691.4709 | +1.440 | 0.1499 |  |
| High cholesterol | -218.2128 | 292.8423 | ±585.6845 | -0.745 | 0.4562 |  |
| Kidney disease | -253.3978 | 570.6908 | ±1141.3817 | -0.444 | 0.6570 |  |
| **Circulatory disease** | **-1044.2782** | 426.9985 | ±853.9971 | **-2.446** | **0.0145** | * |
| Nocturnal mean 00-06h (mg/dL) | +14.4976 | 11.3476 | ±22.6952 | +1.278 | 0.2014 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **771**, R² = **0.1307**, Adj R² = **0.1181**, F-statistic = **10.38** (p = **7.35e-18**), Residual SE = **3971.834** on **759** df, AIC = **14978.4**, BIC = **15034.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17238.9455** | 1342.6847 | ±2685.3695 | **+12.839** | **9.89e-38** | *** |
| **Education: graduate level (vs college)** | **-999.6664** | 296.4148 | ±592.8296 | **-3.373** | **7.45e-04** | *** |
| Education: high school or below (vs college) | +858.7495 | 631.0954 | ±1262.1908 | +1.361 | 0.1736 |  |
| Site: UCSD (vs UAB) | +7.7202 | 391.3920 | ±782.7839 | +0.020 | 0.9843 |  |
| Site: UW (vs UAB) | -204.4671 | 367.4409 | ±734.8817 | -0.556 | 0.5779 |  |
| **Age (years)** | **-117.8059** | 14.7150 | ±29.4299 | **-8.006** | **1.19e-15** | *** |
| BMI (kg/m2) | -5.3727 | 23.9761 | ±47.9522 | -0.224 | 0.8227 |  |
| Hypertension | +503.4278 | 345.4408 | ±690.8816 | +1.457 | 0.1450 |  |
| High cholesterol | -195.9615 | 292.1943 | ±584.3885 | -0.671 | 0.5024 |  |
| Kidney disease | -262.3628 | 577.0757 | ±1154.1515 | -0.455 | 0.6494 |  |
| **Circulatory disease** | **-1021.7959** | 428.1085 | ±856.2169 | **-2.387** | **0.0170** | * |
| Glucose SD, pooled (mg/dL) | +21.6542 | 35.0162 | ±70.0325 | +0.618 | 0.5363 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **771**, R² = **0.1306**, Adj R² = **0.1180**, F-statistic = **10.37** (p = **7.80e-18**), Residual SE = **3972.166** on **759** df, AIC = **14978.6**, BIC = **15034.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17334.5214** | 1325.2230 | ±2650.4460 | **+13.080** | **4.26e-39** | *** |
| **Education: graduate level (vs college)** | **-1002.7668** | 296.3871 | ±592.7741 | **-3.383** | **7.16e-04** | *** |
| Education: high school or below (vs college) | +863.6958 | 631.2738 | ±1262.5475 | +1.368 | 0.1713 |  |
| Site: UCSD (vs UAB) | +3.9156 | 391.1858 | ±782.3717 | +0.010 | 0.9920 |  |
| Site: UW (vs UAB) | -206.8037 | 367.1158 | ±734.2316 | -0.563 | 0.5732 |  |
| **Age (years)** | **-117.7425** | 14.7357 | ±29.4714 | **-7.990** | **1.35e-15** | *** |
| BMI (kg/m2) | -5.3039 | 23.9958 | ±47.9916 | -0.221 | 0.8251 |  |
| Hypertension | +508.1861 | 345.0372 | ±690.0743 | +1.473 | 0.1408 |  |
| High cholesterol | -193.4399 | 292.1020 | ±584.2040 | -0.662 | 0.5078 |  |
| Kidney disease | -254.6733 | 575.8516 | ±1151.7031 | -0.442 | 0.6583 |  |
| **Circulatory disease** | **-1017.9826** | 428.2802 | ±856.5603 | **-2.377** | **0.0175** | * |
| Avg. daily SD (mg/dL) | +17.9414 | 36.0940 | ±72.1881 | +0.497 | 0.6191 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **771**, R² = **0.1303**, Adj R² = **0.1177**, F-statistic = **10.34** (p = **8.69e-18**), Residual SE = **3972.779** on **759** df, AIC = **14978.8**, BIC = **15034.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17683.1280** | 1411.0172 | ±2822.0343 | **+12.532** | **4.98e-36** | *** |
| **Education: graduate level (vs college)** | **-1008.0691** | 296.9832 | ±593.9665 | **-3.394** | **6.88e-04** | *** |
| Education: high school or below (vs college) | +875.2858 | 633.9647 | ±1267.9295 | +1.381 | 0.1674 |  |
| Site: UCSD (vs UAB) | -12.8925 | 391.6692 | ±783.3383 | -0.033 | 0.9737 |  |
| Site: UW (vs UAB) | -207.8250 | 368.5577 | ±737.1154 | -0.564 | 0.5728 |  |
| **Age (years)** | **-117.2046** | 14.7405 | ±29.4811 | **-7.951** | **1.85e-15** | *** |
| BMI (kg/m2) | -4.7930 | 24.0924 | ±48.1848 | -0.199 | 0.8423 |  |
| Hypertension | +532.2061 | 344.9495 | ±689.8990 | +1.543 | 0.1229 |  |
| High cholesterol | -188.8473 | 292.0065 | ±584.0131 | -0.647 | 0.5178 |  |
| Kidney disease | -233.4142 | 575.4874 | ±1150.9748 | -0.406 | 0.6850 |  |
| **Circulatory disease** | **-1010.5649** | 428.5001 | ±857.0001 | **-2.358** | **0.0184** | * |
| CV (%) | -4.6801 | 46.0240 | ±92.0480 | -0.102 | 0.9190 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **771**, R² = **0.1303**, Adj R² = **0.1177**, F-statistic = **10.34** (p = **8.67e-18**), Residual SE = **3972.766** on **759** df, AIC = **14978.8**, BIC = **15034.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17707.3330** | 1457.4139 | ±2914.8278 | **+12.150** | **5.75e-34** | *** |
| **Education: graduate level (vs college)** | **-1003.9938** | 296.8013 | ±593.6026 | **-3.383** | **7.18e-04** | *** |
| Education: high school or below (vs college) | +869.4888 | 633.0436 | ±1266.0873 | +1.374 | 0.1696 |  |
| Site: UCSD (vs UAB) | -7.5694 | 391.3189 | ±782.6378 | -0.019 | 0.9846 |  |
| Site: UW (vs UAB) | -206.1680 | 367.8989 | ±735.7977 | -0.560 | 0.5752 |  |
| **Age (years)** | **-117.3780** | 14.7366 | ±29.4731 | **-7.965** | **1.65e-15** | *** |
| BMI (kg/m2) | -4.7383 | 24.0541 | ±48.1083 | -0.197 | 0.8438 |  |
| Hypertension | +525.7958 | 344.4699 | ±688.9398 | +1.526 | 0.1269 |  |
| High cholesterol | -189.5784 | 292.0339 | ±584.0678 | -0.649 | 0.5162 |  |
| Kidney disease | -239.1864 | 575.7931 | ±1151.5861 | -0.415 | 0.6778 |  |
| **Circulatory disease** | **-1010.5974** | 428.3434 | ±856.6867 | **-2.359** | **0.0183** | * |
| Mean / SD ratio | -14.6775 | 115.8816 | ±231.7632 | -0.127 | 0.8992 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **771**, R² = **0.1304**, Adj R² = **0.1178**, F-statistic = **10.35** (p = **8.41e-18**), Residual SE = **3972.594** on **759** df, AIC = **14978.7**, BIC = **15034.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17831.5306** | 1438.4045 | ±2876.8090 | **+12.397** | **2.72e-35** | *** |
| **Education: graduate level (vs college)** | **-1001.9083** | 296.7393 | ±593.4786 | **-3.376** | **7.34e-04** | *** |
| Education: high school or below (vs college) | +866.3589 | 632.3502 | ±1264.7004 | +1.370 | 0.1707 |  |
| Site: UCSD (vs UAB) | -4.1109 | 390.8036 | ±781.6073 | -0.011 | 0.9916 |  |
| Site: UW (vs UAB) | -206.4232 | 367.2695 | ±734.5390 | -0.562 | 0.5741 |  |
| **Age (years)** | **-117.5556** | 14.7665 | ±29.5330 | **-7.961** | **1.71e-15** | *** |
| BMI (kg/m2) | -4.8167 | 24.0243 | ±48.0486 | -0.200 | 0.8411 |  |
| Hypertension | +522.0778 | 344.1729 | ±688.3459 | +1.517 | 0.1293 |  |
| High cholesterol | -189.7497 | 292.0280 | ±584.0559 | -0.650 | 0.5158 |  |
| Kidney disease | -243.0993 | 575.7435 | ±1151.4871 | -0.422 | 0.6729 |  |
| **Circulatory disease** | **-1008.7573** | 428.3430 | ±856.6860 | **-2.355** | **0.0185** | * |
| Avg. daily mean/SD | -28.5461 | 93.4416 | ±186.8831 | -0.305 | 0.7600 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **771**, R² = **0.1475**, Adj R² = **0.1351**, F-statistic = **11.93** (p = **7.89e-21**), Residual SE = **3933.467** on **759** df, AIC = **14963.5**, BIC = **15019.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14593.5632** | 1359.1509 | ±2718.3019 | **+10.737** | **6.80e-27** | *** |
| **Education: graduate level (vs college)** | **-999.0177** | 291.8603 | ±583.7206 | **-3.423** | **6.19e-04** | *** |
| Education: high school or below (vs college) | +716.6220 | 635.1659 | ±1270.3318 | +1.128 | 0.2592 |  |
| Site: UCSD (vs UAB) | +30.0858 | 386.8635 | ±773.7270 | +0.078 | 0.9380 |  |
| Site: UW (vs UAB) | -175.9872 | 363.6320 | ±727.2641 | -0.484 | 0.6284 |  |
| **Age (years)** | **-116.7408** | 14.3536 | ±28.7073 | **-8.133** | **4.18e-16** | *** |
| BMI (kg/m2) | -5.9086 | 23.4180 | ±46.8359 | -0.252 | 0.8008 |  |
| Hypertension | +570.0378 | 344.6883 | ±689.3767 | +1.654 | 0.0982 | . |
| High cholesterol | -201.2569 | 289.0770 | ±578.1540 | -0.696 | 0.4863 |  |
| Kidney disease | -320.5200 | 578.6985 | ±1157.3971 | -0.554 | 0.5797 |  |
| **Circulatory disease** | **-943.9558** | 427.6507 | ±855.3014 | **-2.207** | **0.0273** | * |
| **MAG (mg/dL/h)** | **+83.1868** | 22.1221 | ±44.2442 | **+3.760** | **1.70e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **771**, R² = **0.1314**, Adj R² = **0.1188**, F-statistic = **10.44** (p = **5.58e-18**), Residual SE = **3970.266** on **759** df, AIC = **14977.8**, BIC = **15033.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16879.6476** | 1408.8083 | ±2817.6167 | **+11.982** | **4.44e-33** | *** |
| **Education: graduate level (vs college)** | **-1003.7187** | 296.0146 | ±592.0292 | **-3.391** | **6.97e-04** | *** |
| Education: high school or below (vs college) | +845.9686 | 632.3558 | ±1264.7116 | +1.338 | 0.1810 |  |
| Site: UCSD (vs UAB) | +11.5295 | 390.6775 | ±781.3550 | +0.030 | 0.9765 |  |
| Site: UW (vs UAB) | -207.5140 | 367.0629 | ±734.1258 | -0.565 | 0.5718 |  |
| **Age (years)** | **-118.1017** | 14.7205 | ±29.4410 | **-8.023** | **1.03e-15** | *** |
| BMI (kg/m2) | -4.0296 | 23.9870 | ±47.9740 | -0.168 | 0.8666 |  |
| Hypertension | +503.4938 | 346.6643 | ±693.3286 | +1.452 | 0.1464 |  |
| High cholesterol | -193.1856 | 291.7775 | ±583.5549 | -0.662 | 0.5079 |  |
| Kidney disease | -269.0876 | 574.2643 | ±1148.5286 | -0.469 | 0.6394 |  |
| **Circulatory disease** | **-1024.5368** | 427.2470 | ±854.4940 | **-2.398** | **0.0165** | * |
| Avg. daily range (mg/dL) | +8.4632 | 8.3724 | ±16.7448 | +1.011 | 0.3121 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **771**, R² = **0.1337**, Adj R² = **0.1211**, F-statistic = **10.65** (p = **2.23e-18**), Residual SE = **3965.075** on **759** df, AIC = **14975.8**, BIC = **15031.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17076.8749** | 1236.2965 | ±2472.5929 | **+13.813** | **2.13e-43** | *** |
| **Education: graduate level (vs college)** | **-1006.0308** | 295.1535 | ±590.3069 | **-3.409** | **6.53e-04** | *** |
| Education: high school or below (vs college) | +824.8035 | 625.3992 | ±1250.7983 | +1.319 | 0.1872 |  |
| Site: UCSD (vs UAB) | +29.0789 | 386.7803 | ±773.5605 | +0.075 | 0.9401 |  |
| Site: UW (vs UAB) | -182.7376 | 366.5247 | ±733.0495 | -0.499 | 0.6181 |  |
| **Age (years)** | **-117.0502** | 14.6522 | ±29.3043 | **-7.989** | **1.36e-15** | *** |
| BMI (kg/m2) | -8.3503 | 23.9786 | ±47.9573 | -0.348 | 0.7277 |  |
| Hypertension | +520.8110 | 345.7292 | ±691.4583 | +1.506 | 0.1320 |  |
| High cholesterol | -230.5732 | 292.9403 | ±585.8807 | -0.787 | 0.4312 |  |
| Kidney disease | -288.0180 | 583.8003 | ±1167.6005 | -0.493 | 0.6218 |  |
| **Circulatory disease** | **-1058.3233** | 430.8422 | ±861.6844 | **-2.456** | **0.0140** | * |
| SD of daily means (mg/dL) | +106.8370 | 68.1413 | ±136.2826 | +1.568 | 0.1169 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **771**, R² = **0.1303**, Adj R² = **0.1177**, F-statistic = **10.34** (p = **8.70e-18**), Residual SE = **3972.786** on **759** df, AIC = **14978.8**, BIC = **15034.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17281.4269** | 4824.2241 | ±9648.4481 | **+3.582** | **3.41e-04** | *** |
| **Education: graduate level (vs college)** | **-1006.0870** | 295.9075 | ±591.8150 | **-3.400** | **6.74e-04** | *** |
| Education: high school or below (vs college) | +872.7966 | 632.2352 | ±1264.4703 | +1.380 | 0.1674 |  |
| Site: UCSD (vs UAB) | -11.9035 | 390.0906 | ±780.1813 | -0.031 | 0.9757 |  |
| Site: UW (vs UAB) | -206.9160 | 367.5587 | ±735.1173 | -0.563 | 0.5735 |  |
| **Age (years)** | **-117.2318** | 14.6314 | ±29.2628 | **-8.012** | **1.13e-15** | *** |
| BMI (kg/m2) | -4.6555 | 24.2362 | ±48.4724 | -0.192 | 0.8477 |  |
| Hypertension | +530.7296 | 347.7066 | ±695.4132 | +1.526 | 0.1269 |  |
| High cholesterol | -187.8531 | 293.4749 | ±586.9498 | -0.640 | 0.5221 |  |
| Kidney disease | -232.1184 | 581.7870 | ±1163.5740 | -0.399 | 0.6899 |  |
| **Circulatory disease** | **-1007.7303** | 430.6498 | ±861.2996 | **-2.340** | **0.0193** | * |
| Time in range 70-180, pooled (%) | +3.2874 | 46.8566 | ±93.7131 | +0.070 | 0.9441 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **771**, R² = **0.1303**, Adj R² = **0.1177**, F-statistic = **10.34** (p = **8.71e-18**), Residual SE = **3972.796** on **759** df, AIC = **14978.8**, BIC = **15034.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17809.7059** | 5006.0042 | ±10012.0084 | **+3.558** | **3.74e-04** | *** |
| **Education: graduate level (vs college)** | **-1006.5651** | 296.0100 | ±592.0201 | **-3.400** | **6.73e-04** | *** |
| Education: high school or below (vs college) | +872.6438 | 632.2922 | ±1264.5844 | +1.380 | 0.1675 |  |
| Site: UCSD (vs UAB) | -9.3317 | 390.1811 | ±780.3622 | -0.024 | 0.9809 |  |
| Site: UW (vs UAB) | -206.7768 | 367.5601 | ±735.1203 | -0.563 | 0.5737 |  |
| **Age (years)** | **-117.3141** | 14.6320 | ±29.2641 | **-8.018** | **1.08e-15** | *** |
| BMI (kg/m2) | -4.8262 | 24.2431 | ±48.4862 | -0.199 | 0.8422 |  |
| Hypertension | +528.3033 | 347.4475 | ±694.8951 | +1.521 | 0.1284 |  |
| High cholesterol | -189.9991 | 293.5637 | ±587.1274 | -0.647 | 0.5175 |  |
| Kidney disease | -238.4461 | 582.0271 | ±1164.0542 | -0.410 | 0.6820 |  |
| **Circulatory disease** | **-1012.7703** | 431.4971 | ±862.9942 | **-2.347** | **0.0189** | * |
| Avg. daily time in range 70-180 (%) | -1.9952 | 48.6250 | ±97.2501 | -0.041 | 0.9673 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **771**, R² = **0.1319**, Adj R² = **0.1193**, F-statistic = **10.48** (p = **4.67e-18**), Residual SE = **3969.256** on **759** df, AIC = **14977.4**, BIC = **15033.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17699.3778** | 1228.1322 | ±2456.2644 | **+14.412** | **4.37e-47** | *** |
| **Education: graduate level (vs college)** | **-1034.3858** | 297.0233 | ±594.0466 | **-3.483** | **4.97e-04** | *** |
| Education: high school or below (vs college) | +850.0044 | 629.7035 | ±1259.4071 | +1.350 | 0.1771 |  |
| Site: UCSD (vs UAB) | +5.4817 | 390.8660 | ±781.7319 | +0.014 | 0.9888 |  |
| Site: UW (vs UAB) | -211.6061 | 366.6459 | ±733.2918 | -0.577 | 0.5638 |  |
| **Age (years)** | **-117.1154** | 14.6437 | ±29.2875 | **-7.998** | **1.27e-15** | *** |
| BMI (kg/m2) | -5.3945 | 24.0557 | ±48.1114 | -0.224 | 0.8226 |  |
| Hypertension | +523.7435 | 346.7773 | ±693.5546 | +1.510 | 0.1310 |  |
| High cholesterol | -183.6749 | 291.3118 | ±582.6236 | -0.631 | 0.5284 |  |
| Kidney disease | -255.2149 | 573.1379 | ±1146.2758 | -0.445 | 0.6561 |  |
| **Circulatory disease** | **-1015.1774** | 429.0496 | ±858.0992 | **-2.366** | **0.0180** | * |
| Time 54-69, pooled (%) | -338.2375 | 278.8362 | ±557.6723 | -1.213 | 0.2251 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **771**, R² = **0.1325**, Adj R² = **0.1199**, F-statistic = **10.54** (p = **3.63e-18**), Residual SE = **3967.838** on **759** df, AIC = **14976.9**, BIC = **15032.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17698.1285** | 1226.3368 | ±2452.6737 | **+14.432** | **3.27e-47** | *** |
| **Education: graduate level (vs college)** | **-1041.5631** | 296.9051 | ±593.8101 | **-3.508** | **4.51e-04** | *** |
| Education: high school or below (vs college) | +841.1424 | 628.9052 | ±1257.8105 | +1.337 | 0.1811 |  |
| Site: UCSD (vs UAB) | +17.5322 | 391.7386 | ±783.4772 | +0.045 | 0.9643 |  |
| Site: UW (vs UAB) | -209.4153 | 366.7465 | ±733.4929 | -0.571 | 0.5680 |  |
| **Age (years)** | **-116.9488** | 14.6327 | ±29.2654 | **-7.992** | **1.32e-15** | *** |
| BMI (kg/m2) | -5.4617 | 24.0690 | ±48.1381 | -0.227 | 0.8205 |  |
| Hypertension | +522.3078 | 346.7481 | ±693.4962 | +1.506 | 0.1320 |  |
| High cholesterol | -184.0787 | 291.2551 | ±582.5101 | -0.632 | 0.5274 |  |
| Kidney disease | -261.0457 | 572.2711 | ±1144.5423 | -0.456 | 0.6483 |  |
| **Circulatory disease** | **-1022.0227** | 428.8456 | ±857.6911 | **-2.383** | **0.0172** | * |
| Avg. daily time 54-69 (%) | -388.3808 | 264.6760 | ±529.3519 | -1.467 | 0.1423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **771**, R² = **0.1319**, Adj R² = **0.1193**, F-statistic = **10.48** (p = **4.67e-18**), Residual SE = **3969.256** on **759** df, AIC = **14977.4**, BIC = **15033.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17699.3778** | 1228.1322 | ±2456.2644 | **+14.412** | **4.37e-47** | *** |
| **Education: graduate level (vs college)** | **-1034.3858** | 297.0233 | ±594.0466 | **-3.483** | **4.97e-04** | *** |
| Education: high school or below (vs college) | +850.0044 | 629.7035 | ±1259.4071 | +1.350 | 0.1771 |  |
| Site: UCSD (vs UAB) | +5.4817 | 390.8660 | ±781.7319 | +0.014 | 0.9888 |  |
| Site: UW (vs UAB) | -211.6061 | 366.6459 | ±733.2918 | -0.577 | 0.5638 |  |
| **Age (years)** | **-117.1154** | 14.6437 | ±29.2875 | **-7.998** | **1.27e-15** | *** |
| BMI (kg/m2) | -5.3945 | 24.0557 | ±48.1114 | -0.224 | 0.8226 |  |
| Hypertension | +523.7435 | 346.7773 | ±693.5546 | +1.510 | 0.1310 |  |
| High cholesterol | -183.6749 | 291.3118 | ±582.6236 | -0.631 | 0.5284 |  |
| Kidney disease | -255.2149 | 573.1379 | ±1146.2758 | -0.445 | 0.6561 |  |
| **Circulatory disease** | **-1015.1774** | 429.0496 | ±858.0992 | **-2.366** | **0.0180** | * |
| Time < 70 (%) | -338.2375 | 278.8362 | ±557.6723 | -1.213 | 0.2251 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **771**, R² = **0.1325**, Adj R² = **0.1199**, F-statistic = **10.54** (p = **3.63e-18**), Residual SE = **3967.838** on **759** df, AIC = **14976.9**, BIC = **15032.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17698.1285** | 1226.3368 | ±2452.6737 | **+14.432** | **3.27e-47** | *** |
| **Education: graduate level (vs college)** | **-1041.5631** | 296.9051 | ±593.8101 | **-3.508** | **4.51e-04** | *** |
| Education: high school or below (vs college) | +841.1424 | 628.9052 | ±1257.8105 | +1.337 | 0.1811 |  |
| Site: UCSD (vs UAB) | +17.5322 | 391.7386 | ±783.4772 | +0.045 | 0.9643 |  |
| Site: UW (vs UAB) | -209.4153 | 366.7465 | ±733.4929 | -0.571 | 0.5680 |  |
| **Age (years)** | **-116.9488** | 14.6327 | ±29.2654 | **-7.992** | **1.32e-15** | *** |
| BMI (kg/m2) | -5.4617 | 24.0690 | ±48.1381 | -0.227 | 0.8205 |  |
| Hypertension | +522.3078 | 346.7481 | ±693.4962 | +1.506 | 0.1320 |  |
| High cholesterol | -184.0787 | 291.2551 | ±582.5101 | -0.632 | 0.5274 |  |
| Kidney disease | -261.0457 | 572.2711 | ±1144.5423 | -0.456 | 0.6483 |  |
| **Circulatory disease** | **-1022.0227** | 428.8456 | ±857.6911 | **-2.383** | **0.0172** | * |
| Avg. daily time < 70 (%) | -388.3808 | 264.6760 | ±529.3519 | -1.467 | 0.1423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **771**, R² = **0.1303**, Adj R² = **0.1177**, F-statistic = **10.34** (p = **8.69e-18**), Residual SE = **3972.780** on **759** df, AIC = **14978.8**, BIC = **15034.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17610.9161** | 1220.4782 | ±2440.9564 | **+14.430** | **3.37e-47** | *** |
| **Education: graduate level (vs college)** | **-1007.0814** | 295.8880 | ±591.7761 | **-3.404** | **6.65e-04** | *** |
| Education: high school or below (vs college) | +872.0283 | 631.6914 | ±1263.3827 | +1.380 | 0.1674 |  |
| Site: UCSD (vs UAB) | -8.3402 | 390.5150 | ±781.0300 | -0.021 | 0.9830 |  |
| Site: UW (vs UAB) | -206.7881 | 367.4306 | ±734.8612 | -0.563 | 0.5736 |  |
| **Age (years)** | **-117.3421** | 14.6458 | ±29.2917 | **-8.012** | **1.13e-15** | *** |
| BMI (kg/m2) | -4.8877 | 24.2104 | ±48.4208 | -0.202 | 0.8400 |  |
| Hypertension | +527.4277 | 347.9137 | ±695.8273 | +1.516 | 0.1295 |  |
| High cholesterol | -190.6948 | 293.4910 | ±586.9821 | -0.650 | 0.5159 |  |
| Kidney disease | -240.7551 | 581.4883 | ±1162.9766 | -0.414 | 0.6789 |  |
| **Circulatory disease** | **-1014.4408** | 430.3092 | ±860.6183 | **-2.357** | **0.0184** | * |
| Time 181-250, pooled (%) | +3.7978 | 46.5758 | ±93.1516 | +0.082 | 0.9350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **771**, R² = **0.1304**, Adj R² = **0.1178**, F-statistic = **10.35** (p = **8.46e-18**), Residual SE = **3972.631** on **759** df, AIC = **14978.7**, BIC = **15034.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17613.2951** | 1219.8898 | ±2439.7797 | **+14.438** | **2.97e-47** | *** |
| **Education: graduate level (vs college)** | **-1008.2845** | 296.0144 | ±592.0287 | **-3.406** | **6.59e-04** | *** |
| Education: high school or below (vs college) | +872.1454 | 631.6000 | ±1263.1999 | +1.381 | 0.1673 |  |
| Site: UCSD (vs UAB) | -4.0581 | 390.7121 | ±781.4241 | -0.010 | 0.9917 |  |
| Site: UW (vs UAB) | -206.6028 | 367.4427 | ±734.8855 | -0.562 | 0.5739 |  |
| **Age (years)** | **-117.4402** | 14.6473 | ±29.2945 | **-8.018** | **1.08e-15** | *** |
| BMI (kg/m2) | -5.1436 | 24.2056 | ±48.4112 | -0.212 | 0.8317 |  |
| Hypertension | +523.9697 | 347.7092 | ±695.4184 | +1.507 | 0.1318 |  |
| High cholesterol | -193.4368 | 293.5701 | ±587.1402 | -0.659 | 0.5100 |  |
| Kidney disease | -250.0058 | 581.5296 | ±1163.0593 | -0.430 | 0.6673 |  |
| **Circulatory disease** | **-1021.8272** | 431.1495 | ±862.2991 | **-2.370** | **0.0178** | * |
| Avg. daily time 181-250 (%) | +10.9431 | 48.3900 | ±96.7800 | +0.226 | 0.8211 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **771**, R² = **0.1303**, Adj R² = **0.1177**, F-statistic = **10.34** (p = **8.69e-18**), Residual SE = **3972.780** on **759** df, AIC = **14978.8**, BIC = **15034.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17610.9161** | 1220.4782 | ±2440.9564 | **+14.430** | **3.37e-47** | *** |
| **Education: graduate level (vs college)** | **-1007.0814** | 295.8880 | ±591.7761 | **-3.404** | **6.65e-04** | *** |
| Education: high school or below (vs college) | +872.0283 | 631.6914 | ±1263.3827 | +1.380 | 0.1674 |  |
| Site: UCSD (vs UAB) | -8.3402 | 390.5150 | ±781.0300 | -0.021 | 0.9830 |  |
| Site: UW (vs UAB) | -206.7881 | 367.4306 | ±734.8612 | -0.563 | 0.5736 |  |
| **Age (years)** | **-117.3421** | 14.6458 | ±29.2917 | **-8.012** | **1.13e-15** | *** |
| BMI (kg/m2) | -4.8877 | 24.2104 | ±48.4208 | -0.202 | 0.8400 |  |
| Hypertension | +527.4277 | 347.9137 | ±695.8273 | +1.516 | 0.1295 |  |
| High cholesterol | -190.6948 | 293.4910 | ±586.9821 | -0.650 | 0.5159 |  |
| Kidney disease | -240.7551 | 581.4883 | ±1162.9766 | -0.414 | 0.6789 |  |
| **Circulatory disease** | **-1014.4408** | 430.3092 | ±860.6183 | **-2.357** | **0.0184** | * |
| Time > 180 (%) | +3.7978 | 46.5758 | ±93.1516 | +0.082 | 0.9350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **771**, R² = **0.1304**, Adj R² = **0.1178**, F-statistic = **10.35** (p = **8.46e-18**), Residual SE = **3972.631** on **759** df, AIC = **14978.7**, BIC = **15034.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17613.2951** | 1219.8898 | ±2439.7797 | **+14.438** | **2.97e-47** | *** |
| **Education: graduate level (vs college)** | **-1008.2845** | 296.0144 | ±592.0287 | **-3.406** | **6.59e-04** | *** |
| Education: high school or below (vs college) | +872.1454 | 631.6000 | ±1263.1999 | +1.381 | 0.1673 |  |
| Site: UCSD (vs UAB) | -4.0581 | 390.7121 | ±781.4241 | -0.010 | 0.9917 |  |
| Site: UW (vs UAB) | -206.6028 | 367.4427 | ±734.8855 | -0.562 | 0.5739 |  |
| **Age (years)** | **-117.4402** | 14.6473 | ±29.2945 | **-8.018** | **1.08e-15** | *** |
| BMI (kg/m2) | -5.1436 | 24.2056 | ±48.4112 | -0.212 | 0.8317 |  |
| Hypertension | +523.9697 | 347.7092 | ±695.4184 | +1.507 | 0.1318 |  |
| High cholesterol | -193.4368 | 293.5701 | ±587.1402 | -0.659 | 0.5100 |  |
| Kidney disease | -250.0058 | 581.5296 | ±1163.0593 | -0.430 | 0.6673 |  |
| **Circulatory disease** | **-1021.8272** | 431.1495 | ±862.2991 | **-2.370** | **0.0178** | * |
| Avg. daily time > 180 (%) | +10.9431 | 48.3900 | ±96.7800 | +0.226 | 0.8211 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 771)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **771**, R² = **0.1304**, Adj R² = **0.1178**, F-statistic = **10.35** (p = **8.38e-18**), Residual SE = **3972.576** on **759** df, AIC = **14978.7**, BIC = **15034.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17615.9151** | 1220.3691 | ±2440.7381 | **+14.435** | **3.12e-47** | *** |
| **Education: graduate level (vs college)** | **-1005.8770** | 295.7997 | ±591.5995 | **-3.401** | **6.73e-04** | *** |
| Education: high school or below (vs college) | +863.2764 | 631.7881 | ±1263.5763 | +1.366 | 0.1718 |  |
| Site: UCSD (vs UAB) | -3.1566 | 389.6780 | ±779.3559 | -0.008 | 0.9935 |  |
| Site: UW (vs UAB) | -205.6088 | 367.4153 | ±734.8305 | -0.560 | 0.5757 |  |
| **Age (years)** | **-117.1856** | 14.6789 | ±29.3577 | **-7.983** | **1.42e-15** | *** |
| BMI (kg/m2) | -5.5363 | 24.2818 | ±48.5636 | -0.228 | 0.8196 |  |
| Hypertension | +529.9980 | 347.6357 | ±695.2714 | +1.525 | 0.1274 |  |
| High cholesterol | -198.3199 | 295.6271 | ±591.2542 | -0.671 | 0.5023 |  |
| Kidney disease | -247.2590 | 578.3474 | ±1156.6947 | -0.428 | 0.6690 |  |
| **Circulatory disease** | **-1019.8399** | 428.6705 | ±857.3410 | **-2.379** | **0.0174** | * |
| Nocturnal time > 180 (%) | +11.4315 | 45.4388 | ±90.8776 | +0.252 | 0.8014 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 771; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **771**, R² = **0.1526**, Adj R² = **0.1414**, F-statistic = **13.68** (p = **2.46e-22**), Residual SE = **12.051** on **760** df, AIC = **6037.2**, BIC = **6088.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6581** | 3.9688 | ±7.9377 | **+11.000** | **3.81e-28** | *** |
| **Education: graduate level (vs college)** | **-2.7257** | 0.9004 | ±1.8007 | **-3.027** | **0.0025** | ** |
| Education: high school or below (vs college) | +2.1540 | 1.9303 | ±3.8606 | +1.116 | 0.2645 |  |
| Site: UCSD (vs UAB) | -0.1785 | 1.1876 | ±2.3752 | -0.150 | 0.8805 |  |
| Site: UW (vs UAB) | -0.5365 | 1.0983 | ±2.1965 | -0.489 | 0.6252 |  |
| **Age (years)** | **-0.3794** | 0.0418 | ±0.0836 | **-9.077** | **1.12e-19** | *** |
| BMI (kg/m2) | +0.1613 | 0.0840 | ±0.1681 | +1.919 | 0.0550 | . |
| Hypertension | +1.1026 | 1.0004 | ±2.0007 | +1.102 | 0.2704 |  |
| High cholesterol | -0.1747 | 0.8817 | ±1.7633 | -0.198 | 0.8429 |  |
| Kidney disease | -0.1166 | 1.7255 | ±3.4509 | -0.068 | 0.9461 |  |
| **Circulatory disease** | **-2.9641** | 1.2665 | ±2.5329 | **-2.340** | **0.0193** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **771**, R² = **0.1598**, Adj R² = **0.1477**, F-statistic = **13.13** (p = **4.38e-23**), Residual SE = **12.007** on **759** df, AIC = **6032.5**, BIC = **6088.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+29.2536** | 7.1982 | ±14.3963 | **+4.064** | **4.82e-05** | *** |
| **Education: graduate level (vs college)** | **-2.7159** | 0.8940 | ±1.7880 | **-3.038** | **0.0024** | ** |
| Education: high school or below (vs college) | +2.0287 | 1.9388 | ±3.8776 | +1.046 | 0.2954 |  |
| Site: UCSD (vs UAB) | -0.1373 | 1.1788 | ±2.3576 | -0.116 | 0.9073 |  |
| Site: UW (vs UAB) | -0.4878 | 1.0948 | ±2.1896 | -0.446 | 0.6559 |  |
| **Age (years)** | **-0.3847** | 0.0413 | ±0.0825 | **-9.326** | **1.09e-20** | *** |
| BMI (kg/m2) | +0.1319 | 0.0809 | ±0.1617 | +1.631 | 0.1029 |  |
| Hypertension | +0.7606 | 1.0088 | ±2.0175 | +0.754 | 0.4508 |  |
| High cholesterol | -0.5764 | 0.8868 | ±1.7736 | -0.650 | 0.5157 |  |
| Kidney disease | +0.0147 | 1.6876 | ±3.3752 | +0.009 | 0.9930 |  |
| **Circulatory disease** | **-3.2017** | 1.2583 | ±2.5166 | **-2.545** | **0.0109** | * |
| **HbA1c (%)** | **+2.8088** | 1.1499 | ±2.2999 | **+2.443** | **0.0146** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **771**, R² = **0.1545**, Adj R² = **0.1422**, F-statistic = **12.60** (p = **4.24e-22**), Residual SE = **12.045** on **759** df, AIC = **6037.4**, BIC = **6093.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+38.3211** | 5.7068 | ±11.4136 | **+6.715** | **1.88e-11** | *** |
| **Education: graduate level (vs college)** | **-2.7462** | 0.9007 | ±1.8014 | **-3.049** | **0.0023** | ** |
| Education: high school or below (vs college) | +2.1780 | 1.9244 | ±3.8488 | +1.132 | 0.2577 |  |
| Site: UCSD (vs UAB) | -0.1241 | 1.1866 | ±2.3733 | -0.105 | 0.9167 |  |
| Site: UW (vs UAB) | -0.5842 | 1.0977 | ±2.1953 | -0.532 | 0.5946 |  |
| **Age (years)** | **-0.3804** | 0.0417 | ±0.0833 | **-9.132** | **6.74e-20** | *** |
| BMI (kg/m2) | +0.1507 | 0.0839 | ±0.1679 | +1.796 | 0.0725 | . |
| Hypertension | +0.9742 | 1.0013 | ±2.0025 | +0.973 | 0.3306 |  |
| High cholesterol | -0.2272 | 0.8809 | ±1.7618 | -0.258 | 0.7965 |  |
| Kidney disease | -0.2737 | 1.7176 | ±3.4352 | -0.159 | 0.8734 |  |
| **Circulatory disease** | **-3.0762** | 1.2759 | ±2.5517 | **-2.411** | **0.0159** | * |
| Mean glucose (mg/dL) | +0.0482 | 0.0372 | ±0.0744 | +1.295 | 0.1952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **771**, R² = **0.1545**, Adj R² = **0.1422**, F-statistic = **12.60** (p = **4.24e-22**), Residual SE = **12.045** on **759** df, AIC = **6037.4**, BIC = **6093.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.6510** | 10.0800 | ±20.1601 | **+3.140** | **0.0017** | ** |
| **Education: graduate level (vs college)** | **-2.7462** | 0.9007 | ±1.8014 | **-3.049** | **0.0023** | ** |
| Education: high school or below (vs college) | +2.1780 | 1.9244 | ±3.8488 | +1.132 | 0.2577 |  |
| Site: UCSD (vs UAB) | -0.1241 | 1.1866 | ±2.3733 | -0.105 | 0.9167 |  |
| Site: UW (vs UAB) | -0.5842 | 1.0977 | ±2.1953 | -0.532 | 0.5946 |  |
| **Age (years)** | **-0.3804** | 0.0417 | ±0.0833 | **-9.132** | **6.74e-20** | *** |
| BMI (kg/m2) | +0.1507 | 0.0839 | ±0.1679 | +1.796 | 0.0725 | . |
| Hypertension | +0.9742 | 1.0013 | ±2.0025 | +0.973 | 0.3306 |  |
| High cholesterol | -0.2272 | 0.8809 | ±1.7618 | -0.258 | 0.7965 |  |
| Kidney disease | -0.2737 | 1.7176 | ±3.4352 | -0.159 | 0.8734 |  |
| **Circulatory disease** | **-3.0762** | 1.2759 | ±2.5517 | **-2.411** | **0.0159** | * |
| GMI (%) | +2.0151 | 1.5556 | ±3.1111 | +1.295 | 0.1952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **771**, R² = **0.1543**, Adj R² = **0.1421**, F-statistic = **12.59** (p = **4.48e-22**), Residual SE = **12.046** on **759** df, AIC = **6037.5**, BIC = **6093.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.0816** | 5.2305 | ±10.4609 | **+7.472** | **7.90e-14** | *** |
| **Education: graduate level (vs college)** | **-2.7381** | 0.9004 | ±1.8008 | **-3.041** | **0.0024** | ** |
| Education: high school or below (vs college) | +2.1433 | 1.9228 | ±3.8457 | +1.115 | 0.2650 |  |
| Site: UCSD (vs UAB) | -0.1801 | 1.1885 | ±2.3770 | -0.152 | 0.8796 |  |
| Site: UW (vs UAB) | -0.6009 | 1.0974 | ±2.1947 | -0.548 | 0.5840 |  |
| **Age (years)** | **-0.3763** | 0.0418 | ±0.0836 | **-9.003** | **2.19e-19** | *** |
| BMI (kg/m2) | +0.1449 | 0.0847 | ±0.1694 | +1.710 | 0.0873 | . |
| Hypertension | +1.0128 | 0.9955 | ±1.9910 | +1.017 | 0.3090 |  |
| High cholesterol | -0.2576 | 0.8822 | ±1.7644 | -0.292 | 0.7703 |  |
| Kidney disease | -0.1662 | 1.7098 | ±3.4196 | -0.097 | 0.9226 |  |
| **Circulatory disease** | **-3.0596** | 1.2720 | ±2.5441 | **-2.405** | **0.0162** | * |
| Nocturnal mean 00-06h (mg/dL) | +0.0414 | 0.0335 | ±0.0671 | +1.234 | 0.2170 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **771**, R² = **0.1545**, Adj R² = **0.1422**, F-statistic = **12.61** (p = **4.23e-22**), Residual SE = **12.045** on **759** df, AIC = **6037.4**, BIC = **6093.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.2391** | 4.4162 | ±8.8323 | **+9.338** | **9.80e-21** | *** |
| **Education: graduate level (vs college)** | **-2.6818** | 0.9018 | ±1.8036 | **-2.974** | **0.0029** | ** |
| Education: high school or below (vs college) | +2.0639 | 1.9246 | ±3.8492 | +1.072 | 0.2835 |  |
| Site: UCSD (vs UAB) | -0.0608 | 1.1873 | ±2.3745 | -0.051 | 0.9592 |  |
| Site: UW (vs UAB) | -0.5211 | 1.0977 | ±2.1953 | -0.475 | 0.6350 |  |
| **Age (years)** | **-0.3828** | 0.0418 | ±0.0836 | **-9.160** | **5.21e-20** | *** |
| BMI (kg/m2) | +0.1573 | 0.0829 | ±0.1658 | +1.897 | 0.0578 | . |
| Hypertension | +0.9344 | 1.0025 | ±2.0051 | +0.932 | 0.3513 |  |
| High cholesterol | -0.2188 | 0.8807 | ±1.7613 | -0.248 | 0.8038 |  |
| Kidney disease | -0.2882 | 1.7280 | ±3.4561 | -0.167 | 0.8675 |  |
| **Circulatory disease** | **-3.0356** | 1.2685 | ±2.5369 | **-2.393** | **0.0167** | * |
| Glucose SD, pooled (mg/dL) | +0.1412 | 0.1077 | ±0.2155 | +1.310 | 0.1901 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **771**, R² = **0.1542**, Adj R² = **0.1419**, F-statistic = **12.58** (p = **4.81e-22**), Residual SE = **12.047** on **759** df, AIC = **6037.7**, BIC = **6093.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.6266** | 4.3430 | ±8.6860 | **+9.585** | **9.27e-22** | *** |
| **Education: graduate level (vs college)** | **-2.6989** | 0.9015 | ±1.8029 | **-2.994** | **0.0028** | ** |
| Education: high school or below (vs college) | +2.0886 | 1.9263 | ±3.8526 | +1.084 | 0.2782 |  |
| Site: UCSD (vs UAB) | -0.0734 | 1.1872 | ±2.3744 | -0.062 | 0.9507 |  |
| Site: UW (vs UAB) | -0.5363 | 1.0980 | ±2.1959 | -0.488 | 0.6252 |  |
| **Age (years)** | **-0.3828** | 0.0419 | ±0.0837 | **-9.143** | **6.07e-20** | *** |
| BMI (kg/m2) | +0.1573 | 0.0829 | ±0.1659 | +1.896 | 0.0579 | . |
| Hypertension | +0.9475 | 1.0017 | ±2.0034 | +0.946 | 0.3442 |  |
| High cholesterol | -0.2060 | 0.8814 | ±1.7627 | -0.234 | 0.8152 |  |
| Kidney disease | -0.2541 | 1.7230 | ±3.4459 | -0.147 | 0.8828 |  |
| **Circulatory disease** | **-3.0169** | 1.2688 | ±2.5376 | **-2.378** | **0.0174** | * |
| Avg. daily SD (mg/dL) | +0.1323 | 0.1101 | ±0.2203 | +1.201 | 0.2297 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **771**, R² = **0.1529**, Adj R² = **0.1406**, F-statistic = **12.45** (p = **8.31e-22**), Residual SE = **12.057** on **759** df, AIC = **6038.9**, BIC = **6094.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.4369** | 4.6752 | ±9.3503 | **+9.077** | **1.12e-19** | *** |
| **Education: graduate level (vs college)** | **-2.6979** | 0.9049 | ±1.8097 | **-2.982** | **0.0029** | ** |
| Education: high school or below (vs college) | +2.1084 | 1.9357 | ±3.8714 | +1.089 | 0.2761 |  |
| Site: UCSD (vs UAB) | -0.1357 | 1.1894 | ±2.3789 | -0.114 | 0.9092 |  |
| Site: UW (vs UAB) | -0.5199 | 1.1003 | ±2.2005 | -0.473 | 0.6365 |  |
| **Age (years)** | **-0.3808** | 0.0420 | ±0.0839 | **-9.072** | **1.17e-19** | *** |
| BMI (kg/m2) | +0.1618 | 0.0840 | ±0.1680 | +1.927 | 0.0540 | . |
| Hypertension | +1.0528 | 1.0027 | ±2.0054 | +1.050 | 0.2937 |  |
| High cholesterol | -0.1806 | 0.8822 | ±1.7644 | -0.205 | 0.8378 |  |
| Kidney disease | -0.1602 | 1.7301 | ±3.4601 | -0.093 | 0.9262 |  |
| **Circulatory disease** | **-2.9684** | 1.2665 | ±2.5331 | **-2.344** | **0.0191** | * |
| CV (%) | +0.0782 | 0.1464 | ±0.2928 | +0.534 | 0.5932 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **771**, R² = **0.1531**, Adj R² = **0.1408**, F-statistic = **12.47** (p = **7.55e-22**), Residual SE = **12.055** on **759** df, AIC = **6038.7**, BIC = **6094.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.3921** | 4.5900 | ±9.1801 | **+9.889** | **4.63e-23** | *** |
| **Education: graduate level (vs college)** | **-2.6828** | 0.9042 | ±1.8085 | **-2.967** | **0.0030** | ** |
| Education: high school or below (vs college) | +2.0993 | 1.9317 | ±3.8634 | +1.087 | 0.2772 |  |
| Site: UCSD (vs UAB) | -0.1292 | 1.1884 | ±2.3767 | -0.109 | 0.9134 |  |
| Site: UW (vs UAB) | -0.5247 | 1.0994 | ±2.1988 | -0.477 | 0.6332 |  |
| **Age (years)** | **-0.3811** | 0.0420 | ±0.0840 | **-9.078** | **1.10e-19** | *** |
| BMI (kg/m2) | +0.1617 | 0.0839 | ±0.1677 | +1.928 | 0.0539 | . |
| Hypertension | +1.0415 | 1.0008 | ±2.0015 | +1.041 | 0.2980 |  |
| High cholesterol | -0.1814 | 0.8823 | ±1.7646 | -0.206 | 0.8371 |  |
| Kidney disease | -0.1729 | 1.7289 | ±3.4578 | -0.100 | 0.9203 |  |
| **Circulatory disease** | **-2.9601** | 1.2657 | ±2.5314 | **-2.339** | **0.0194** | * |
| Mean / SD ratio | -0.2616 | 0.3642 | ±0.7285 | -0.718 | 0.4726 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **771**, R² = **0.1532**, Adj R² = **0.1409**, F-statistic = **12.48** (p = **7.27e-22**), Residual SE = **12.054** on **759** df, AIC = **6038.6**, BIC = **6094.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.4332** | 4.5251 | ±9.0502 | **+10.040** | **1.01e-23** | *** |
| **Education: graduate level (vs college)** | **-2.6897** | 0.9036 | ±1.8072 | **-2.977** | **0.0029** | ** |
| Education: high school or below (vs college) | +2.1043 | 1.9309 | ±3.8618 | +1.090 | 0.2758 |  |
| Site: UCSD (vs UAB) | -0.1286 | 1.1869 | ±2.3738 | -0.108 | 0.9137 |  |
| Site: UW (vs UAB) | -0.5333 | 1.0988 | ±2.1975 | -0.485 | 0.6274 |  |
| **Age (years)** | **-0.3816** | 0.0421 | ±0.0842 | **-9.070** | **1.19e-19** | *** |
| BMI (kg/m2) | +0.1608 | 0.0837 | ±0.1674 | +1.921 | 0.0547 | . |
| Hypertension | +1.0453 | 0.9990 | ±1.9979 | +1.046 | 0.2954 |  |
| High cholesterol | -0.1791 | 0.8826 | ±1.7651 | -0.203 | 0.8392 |  |
| Kidney disease | -0.1733 | 1.7261 | ±3.4522 | -0.100 | 0.9200 |  |
| **Circulatory disease** | **-2.9475** | 1.2654 | ±2.5308 | **-2.329** | **0.0198** | * |
| Avg. daily mean/SD | -0.2288 | 0.2888 | ±0.5777 | -0.792 | 0.4283 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **771**, R² = **0.1725**, Adj R² = **0.1605**, F-statistic = **14.38** (p = **1.95e-25**), Residual SE = **11.916** on **759** df, AIC = **6020.8**, BIC = **6076.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.6576** | 4.1993 | ±8.3986 | **+8.015** | **1.10e-15** | *** |
| **Education: graduate level (vs college)** | **-2.7013** | 0.8889 | ±1.7778 | **-3.039** | **0.0024** | ** |
| Education: high school or below (vs college) | +1.6370 | 1.9209 | ±3.8419 | +0.852 | 0.3941 |  |
| Site: UCSD (vs UAB) | -0.0445 | 1.1736 | ±2.3471 | -0.038 | 0.9698 |  |
| Site: UW (vs UAB) | -0.4343 | 1.0796 | ±2.1592 | -0.402 | 0.6875 |  |
| **Age (years)** | **-0.3776** | 0.0410 | ±0.0820 | **-9.216** | **3.08e-20** | *** |
| BMI (kg/m2) | +0.1575 | 0.0810 | ±0.1621 | +1.943 | 0.0520 | . |
| Hypertension | +1.2379 | 0.9878 | ±1.9757 | +1.253 | 0.2101 |  |
| High cholesterol | -0.2147 | 0.8727 | ±1.7453 | -0.246 | 0.8057 |  |
| Kidney disease | -0.3967 | 1.7374 | ±3.4747 | -0.228 | 0.8194 |  |
| **Circulatory disease** | **-2.7424** | 1.2541 | ±2.5082 | **-2.187** | **0.0288** | * |
| **MAG (mg/dL/h)** | **+0.2758** | 0.0646 | ±0.1292 | **+4.269** | **1.96e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **771**, R² = **0.1565**, Adj R² = **0.1443**, F-statistic = **12.80** (p = **1.80e-22**), Residual SE = **12.031** on **759** df, AIC = **6035.6**, BIC = **6091.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.4304** | 4.6890 | ±9.3780 | **+8.409** | **4.13e-17** | *** |
| **Education: graduate level (vs college)** | **-2.7102** | 0.8996 | ±1.7992 | **-3.013** | **0.0026** | ** |
| Education: high school or below (vs college) | +2.0001 | 1.9303 | ±3.8606 | +1.036 | 0.3001 |  |
| Site: UCSD (vs UAB) | -0.0519 | 1.1840 | ±2.3681 | -0.044 | 0.9650 |  |
| Site: UW (vs UAB) | -0.5405 | 1.0975 | ±2.1950 | -0.492 | 0.6224 |  |
| **Age (years)** | **-0.3842** | 0.0417 | ±0.0834 | **-9.209** | **3.28e-20** | *** |
| **BMI (kg/m2)** | **+0.1655** | 0.0835 | ±0.1670 | **+1.982** | **0.0474** | * |
| Hypertension | +0.9537 | 1.0026 | ±2.0053 | +0.951 | 0.3415 |  |
| High cholesterol | -0.1978 | 0.8807 | ±1.7615 | -0.225 | 0.8223 |  |
| Kidney disease | -0.3079 | 1.7159 | ±3.4319 | -0.179 | 0.8576 |  |
| **Circulatory disease** | **-3.0435** | 1.2636 | ±2.5271 | **-2.409** | **0.0160** | * |
| Avg. daily range (mg/dL) | +0.0490 | 0.0266 | ±0.0532 | +1.840 | 0.0657 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **771**, R² = **0.1560**, Adj R² = **0.1438**, F-statistic = **12.76** (p = **2.18e-22**), Residual SE = **12.034** on **759** df, AIC = **6036.0**, BIC = **6091.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.9934** | 4.0303 | ±8.0606 | **+10.419** | **2.02e-25** | *** |
| **Education: graduate level (vs college)** | **-2.7246** | 0.8991 | ±1.7982 | **-3.030** | **0.0024** | ** |
| Education: high school or below (vs college) | +2.0049 | 1.9060 | ±3.8121 | +1.052 | 0.2929 |  |
| Site: UCSD (vs UAB) | -0.0554 | 1.1776 | ±2.3552 | -0.047 | 0.9625 |  |
| Site: UW (vs UAB) | -0.4613 | 1.0954 | ±2.1909 | -0.421 | 0.6737 |  |
| **Age (years)** | **-0.3787** | 0.0418 | ±0.0835 | **-9.068** | **1.21e-19** | *** |
| BMI (kg/m2) | +0.1501 | 0.0833 | ±0.1667 | +1.800 | 0.0718 | . |
| Hypertension | +1.0763 | 0.9976 | ±1.9951 | +1.079 | 0.2806 |  |
| High cholesterol | -0.3039 | 0.8798 | ±1.7596 | -0.345 | 0.7298 |  |
| Kidney disease | -0.2789 | 1.7451 | ±3.4901 | -0.160 | 0.8730 |  |
| **Circulatory disease** | **-3.1124** | 1.2693 | ±2.5386 | **-2.452** | **0.0142** | * |
| SD of daily means (mg/dL) | +0.3336 | 0.2003 | ±0.4006 | +1.665 | 0.0959 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **771**, R² = **0.1528**, Adj R² = **0.1406**, F-statistic = **12.45** (p = **8.37e-22**), Residual SE = **12.057** on **759** df, AIC = **6038.9**, BIC = **6094.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0799** | 13.1700 | ±26.3399 | **+3.803** | **1.43e-04** | *** |
| **Education: graduate level (vs college)** | **-2.7319** | 0.9005 | ±1.8010 | **-3.034** | **0.0024** | ** |
| Education: high school or below (vs college) | +2.1493 | 1.9308 | ±3.8617 | +1.113 | 0.2657 |  |
| Site: UCSD (vs UAB) | -0.1478 | 1.1893 | ±2.3785 | -0.124 | 0.9011 |  |
| Site: UW (vs UAB) | -0.5349 | 1.0990 | ±2.1980 | -0.487 | 0.6265 |  |
| **Age (years)** | **-0.3805** | 0.0417 | ±0.0834 | **-9.125** | **7.20e-20** | *** |
| BMI (kg/m2) | +0.1592 | 0.0839 | ±0.1678 | +1.898 | 0.0577 | . |
| Hypertension | +1.0732 | 1.0030 | ±2.0060 | +1.070 | 0.2846 |  |
| High cholesterol | -0.2010 | 0.8832 | ±1.7664 | -0.228 | 0.8199 |  |
| Kidney disease | -0.1929 | 1.7366 | ±3.4732 | -0.111 | 0.9115 |  |
| **Circulatory disease** | **-3.0245** | 1.2808 | ±2.5616 | **-2.361** | **0.0182** | * |
| Time in range 70-180, pooled (%) | -0.0642 | 0.1282 | ±0.2563 | -0.501 | 0.6162 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **771**, R² = **0.1531**, Adj R² = **0.1408**, F-statistic = **12.47** (p = **7.58e-22**), Residual SE = **12.055** on **759** df, AIC = **6038.7**, BIC = **6094.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.5997** | 13.6074 | ±27.2148 | **+3.866** | **1.11e-04** | *** |
| **Education: graduate level (vs college)** | **-2.7330** | 0.9005 | ±1.8009 | **-3.035** | **0.0024** | ** |
| Education: high school or below (vs college) | +2.1578 | 1.9304 | ±3.8608 | +1.118 | 0.2637 |  |
| Site: UCSD (vs UAB) | -0.1337 | 1.1893 | ±2.3785 | -0.112 | 0.9105 |  |
| Site: UW (vs UAB) | -0.5341 | 1.0988 | ±2.1976 | -0.486 | 0.6269 |  |
| **Age (years)** | **-0.3808** | 0.0417 | ±0.0834 | **-9.133** | **6.68e-20** | *** |
| BMI (kg/m2) | +0.1583 | 0.0838 | ±0.1676 | +1.889 | 0.0589 | . |
| Hypertension | +1.0613 | 1.0027 | ±2.0055 | +1.058 | 0.2899 |  |
| High cholesterol | -0.2105 | 0.8833 | ±1.7665 | -0.238 | 0.8117 |  |
| Kidney disease | -0.2250 | 1.7349 | ±3.4698 | -0.130 | 0.8968 |  |
| **Circulatory disease** | **-3.0514** | 1.2819 | ±2.5638 | **-2.380** | **0.0173** | * |
| Avg. daily time in range 70-180 (%) | -0.0894 | 0.1323 | ±0.2646 | -0.675 | 0.4995 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **771**, R² = **0.1548**, Adj R² = **0.1426**, F-statistic = **12.64** (p = **3.63e-22**), Residual SE = **12.043** on **759** df, AIC = **6037.1**, BIC = **6092.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9901** | 3.9806 | ±7.9612 | **+11.051** | **2.16e-28** | *** |
| **Education: graduate level (vs college)** | **-2.8298** | 0.9075 | ±1.8149 | **-3.118** | **0.0018** | ** |
| Education: high school or below (vs college) | +2.0701 | 1.9268 | ±3.8536 | +1.074 | 0.2826 |  |
| Site: UCSD (vs UAB) | -0.1197 | 1.1891 | ±2.3781 | -0.101 | 0.9198 |  |
| Site: UW (vs UAB) | -0.5543 | 1.0975 | ±2.1949 | -0.505 | 0.6135 |  |
| **Age (years)** | **-0.3788** | 0.0418 | ±0.0836 | **-9.062** | **1.28e-19** | *** |
| BMI (kg/m2) | +0.1589 | 0.0842 | ±0.1684 | +1.887 | 0.0591 | . |
| Hypertension | +1.0822 | 0.9994 | ±1.9987 | +1.083 | 0.2788 |  |
| High cholesterol | -0.1542 | 0.8806 | ±1.7612 | -0.175 | 0.8610 |  |
| Kidney disease | -0.1879 | 1.7222 | ±3.4443 | -0.109 | 0.9131 |  |
| **Circulatory disease** | **-2.9803** | 1.2684 | ±2.5367 | **-2.350** | **0.0188** | * |
| Time 54-69, pooled (%) | -1.2573 | 0.6545 | ±1.3089 | -1.921 | 0.0547 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **771**, R² = **0.1555**, Adj R² = **0.1432**, F-statistic = **12.70** (p = **2.79e-22**), Residual SE = **12.038** on **759** df, AIC = **6036.5**, BIC = **6092.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9709** | 3.9776 | ±7.9551 | **+11.055** | **2.08e-28** | *** |
| **Education: graduate level (vs college)** | **-2.8506** | 0.9076 | ±1.8153 | **-3.141** | **0.0017** | ** |
| Education: high school or below (vs college) | +2.0424 | 1.9251 | ±3.8501 | +1.061 | 0.2887 |  |
| Site: UCSD (vs UAB) | -0.0795 | 1.1896 | ±2.3793 | -0.067 | 0.9467 |  |
| Site: UW (vs UAB) | -0.5457 | 1.0975 | ±2.1950 | -0.497 | 0.6190 |  |
| **Age (years)** | **-0.3782** | 0.0418 | ±0.0836 | **-9.051** | **1.42e-19** | *** |
| BMI (kg/m2) | +0.1588 | 0.0843 | ±0.1685 | +1.884 | 0.0596 | . |
| Hypertension | +1.0780 | 0.9992 | ±1.9983 | +1.079 | 0.2806 |  |
| High cholesterol | -0.1565 | 0.8804 | ±1.7608 | -0.178 | 0.8589 |  |
| Kidney disease | -0.2054 | 1.7186 | ±3.4372 | -0.120 | 0.9049 |  |
| **Circulatory disease** | **-3.0039** | 1.2687 | ±2.5374 | **-2.368** | **0.0179** | * |
| **Avg. daily time 54-69 (%)** | **-1.3795** | 0.6041 | ±1.2081 | **-2.284** | **0.0224** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **771**, R² = **0.1548**, Adj R² = **0.1426**, F-statistic = **12.64** (p = **3.63e-22**), Residual SE = **12.043** on **759** df, AIC = **6037.1**, BIC = **6092.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9901** | 3.9806 | ±7.9612 | **+11.051** | **2.16e-28** | *** |
| **Education: graduate level (vs college)** | **-2.8298** | 0.9075 | ±1.8149 | **-3.118** | **0.0018** | ** |
| Education: high school or below (vs college) | +2.0701 | 1.9268 | ±3.8536 | +1.074 | 0.2826 |  |
| Site: UCSD (vs UAB) | -0.1197 | 1.1891 | ±2.3781 | -0.101 | 0.9198 |  |
| Site: UW (vs UAB) | -0.5543 | 1.0975 | ±2.1949 | -0.505 | 0.6135 |  |
| **Age (years)** | **-0.3788** | 0.0418 | ±0.0836 | **-9.062** | **1.28e-19** | *** |
| BMI (kg/m2) | +0.1589 | 0.0842 | ±0.1684 | +1.887 | 0.0591 | . |
| Hypertension | +1.0822 | 0.9994 | ±1.9987 | +1.083 | 0.2788 |  |
| High cholesterol | -0.1542 | 0.8806 | ±1.7612 | -0.175 | 0.8610 |  |
| Kidney disease | -0.1879 | 1.7222 | ±3.4443 | -0.109 | 0.9131 |  |
| **Circulatory disease** | **-2.9803** | 1.2684 | ±2.5367 | **-2.350** | **0.0188** | * |
| Time < 70 (%) | -1.2573 | 0.6545 | ±1.3089 | -1.921 | 0.0547 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **771**, R² = **0.1555**, Adj R² = **0.1432**, F-statistic = **12.70** (p = **2.79e-22**), Residual SE = **12.038** on **759** df, AIC = **6036.5**, BIC = **6092.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.9709** | 3.9776 | ±7.9551 | **+11.055** | **2.08e-28** | *** |
| **Education: graduate level (vs college)** | **-2.8506** | 0.9076 | ±1.8153 | **-3.141** | **0.0017** | ** |
| Education: high school or below (vs college) | +2.0424 | 1.9251 | ±3.8501 | +1.061 | 0.2887 |  |
| Site: UCSD (vs UAB) | -0.0795 | 1.1896 | ±2.3793 | -0.067 | 0.9467 |  |
| Site: UW (vs UAB) | -0.5457 | 1.0975 | ±2.1950 | -0.497 | 0.6190 |  |
| **Age (years)** | **-0.3782** | 0.0418 | ±0.0836 | **-9.051** | **1.42e-19** | *** |
| BMI (kg/m2) | +0.1588 | 0.0843 | ±0.1685 | +1.884 | 0.0596 | . |
| Hypertension | +1.0780 | 0.9992 | ±1.9983 | +1.079 | 0.2806 |  |
| High cholesterol | -0.1565 | 0.8804 | ±1.7608 | -0.178 | 0.8589 |  |
| Kidney disease | -0.2054 | 1.7186 | ±3.4372 | -0.120 | 0.9049 |  |
| **Circulatory disease** | **-3.0039** | 1.2687 | ±2.5374 | **-2.368** | **0.0179** | * |
| **Avg. daily time < 70 (%)** | **-1.3795** | 0.6041 | ±1.2081 | **-2.284** | **0.0224** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **771**, R² = **0.1531**, Adj R² = **0.1408**, F-statistic = **12.47** (p = **7.47e-22**), Residual SE = **12.055** on **759** df, AIC = **6038.7**, BIC = **6094.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6785** | 3.9595 | ±7.9190 | **+11.031** | **2.70e-28** | *** |
| **Education: graduate level (vs college)** | **-2.7417** | 0.9000 | ±1.8000 | **-3.046** | **0.0023** | ** |
| Education: high school or below (vs college) | +2.1415 | 1.9296 | ±3.8592 | +1.110 | 0.2671 |  |
| Site: UCSD (vs UAB) | -0.1315 | 1.1897 | ±2.3794 | -0.111 | 0.9120 |  |
| Site: UW (vs UAB) | -0.5355 | 1.0987 | ±2.1974 | -0.487 | 0.6260 |  |
| **Age (years)** | **-0.3808** | 0.0417 | ±0.0834 | **-9.133** | **6.66e-20** | *** |
| BMI (kg/m2) | +0.1583 | 0.0838 | ±0.1675 | +1.889 | 0.0589 | . |
| Hypertension | +1.0602 | 1.0034 | ±2.0069 | +1.057 | 0.2907 |  |
| High cholesterol | -0.2099 | 0.8831 | ±1.7662 | -0.238 | 0.8121 |  |
| Kidney disease | -0.2280 | 1.7353 | ±3.4705 | -0.131 | 0.8955 |  |
| **Circulatory disease** | **-3.0493** | 1.2810 | ±2.5619 | **-2.380** | **0.0173** | * |
| Time 181-250, pooled (%) | +0.0895 | 0.1276 | ±0.2553 | +0.701 | 0.4834 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **771**, R² = **0.1535**, Adj R² = **0.1412**, F-statistic = **12.51** (p = **6.33e-22**), Residual SE = **12.052** on **759** df, AIC = **6038.3**, BIC = **6094.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6936** | 3.9539 | ±7.9077 | **+11.051** | **2.17e-28** | *** |
| **Education: graduate level (vs college)** | **-2.7463** | 0.8998 | ±1.7997 | **-3.052** | **0.0023** | ** |
| Education: high school or below (vs college) | +2.1494 | 1.9286 | ±3.8571 | +1.115 | 0.2651 |  |
| Site: UCSD (vs UAB) | -0.1098 | 1.1897 | ±2.3794 | -0.092 | 0.9265 |  |
| Site: UW (vs UAB) | -0.5340 | 1.0985 | ±2.1970 | -0.486 | 0.6269 |  |
| **Age (years)** | **-0.3812** | 0.0417 | ±0.0834 | **-9.142** | **6.14e-20** | *** |
| BMI (kg/m2) | +0.1571 | 0.0836 | ±0.1673 | +1.878 | 0.0604 | . |
| Hypertension | +1.0450 | 1.0032 | ±2.0065 | +1.042 | 0.2976 |  |
| High cholesterol | -0.2211 | 0.8830 | ±1.7660 | -0.250 | 0.8023 |  |
| Kidney disease | -0.2697 | 1.7327 | ±3.4653 | -0.156 | 0.8763 |  |
| **Circulatory disease** | **-3.0846** | 1.2824 | ±2.5648 | **-2.405** | **0.0162** | * |
| Avg. daily time 181-250 (%) | +0.1198 | 0.1318 | ±0.2636 | +0.909 | 0.3632 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **771**, R² = **0.1531**, Adj R² = **0.1408**, F-statistic = **12.47** (p = **7.47e-22**), Residual SE = **12.055** on **759** df, AIC = **6038.7**, BIC = **6094.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6785** | 3.9595 | ±7.9190 | **+11.031** | **2.70e-28** | *** |
| **Education: graduate level (vs college)** | **-2.7417** | 0.9000 | ±1.8000 | **-3.046** | **0.0023** | ** |
| Education: high school or below (vs college) | +2.1415 | 1.9296 | ±3.8592 | +1.110 | 0.2671 |  |
| Site: UCSD (vs UAB) | -0.1315 | 1.1897 | ±2.3794 | -0.111 | 0.9120 |  |
| Site: UW (vs UAB) | -0.5355 | 1.0987 | ±2.1974 | -0.487 | 0.6260 |  |
| **Age (years)** | **-0.3808** | 0.0417 | ±0.0834 | **-9.133** | **6.66e-20** | *** |
| BMI (kg/m2) | +0.1583 | 0.0838 | ±0.1675 | +1.889 | 0.0589 | . |
| Hypertension | +1.0602 | 1.0034 | ±2.0069 | +1.057 | 0.2907 |  |
| High cholesterol | -0.2099 | 0.8831 | ±1.7662 | -0.238 | 0.8121 |  |
| Kidney disease | -0.2280 | 1.7353 | ±3.4705 | -0.131 | 0.8955 |  |
| **Circulatory disease** | **-3.0493** | 1.2810 | ±2.5619 | **-2.380** | **0.0173** | * |
| Time > 180 (%) | +0.0895 | 0.1276 | ±0.2553 | +0.701 | 0.4834 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **771**, R² = **0.1535**, Adj R² = **0.1412**, F-statistic = **12.51** (p = **6.33e-22**), Residual SE = **12.052** on **759** df, AIC = **6038.3**, BIC = **6094.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.6936** | 3.9539 | ±7.9077 | **+11.051** | **2.17e-28** | *** |
| **Education: graduate level (vs college)** | **-2.7463** | 0.8998 | ±1.7997 | **-3.052** | **0.0023** | ** |
| Education: high school or below (vs college) | +2.1494 | 1.9286 | ±3.8571 | +1.115 | 0.2651 |  |
| Site: UCSD (vs UAB) | -0.1098 | 1.1897 | ±2.3794 | -0.092 | 0.9265 |  |
| Site: UW (vs UAB) | -0.5340 | 1.0985 | ±2.1970 | -0.486 | 0.6269 |  |
| **Age (years)** | **-0.3812** | 0.0417 | ±0.0834 | **-9.142** | **6.14e-20** | *** |
| BMI (kg/m2) | +0.1571 | 0.0836 | ±0.1673 | +1.878 | 0.0604 | . |
| Hypertension | +1.0450 | 1.0032 | ±2.0065 | +1.042 | 0.2976 |  |
| High cholesterol | -0.2211 | 0.8830 | ±1.7660 | -0.250 | 0.8023 |  |
| Kidney disease | -0.2697 | 1.7327 | ±3.4653 | -0.156 | 0.8763 |  |
| **Circulatory disease** | **-3.0846** | 1.2824 | ±2.5648 | **-2.405** | **0.0162** | * |
| Avg. daily time > 180 (%) | +0.1198 | 0.1318 | ±0.2636 | +0.909 | 0.3632 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 771)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **771**, R² = **0.1531**, Adj R² = **0.1408**, F-statistic = **12.47** (p = **7.52e-22**), Residual SE = **12.055** on **759** df, AIC = **6038.7**, BIC = **6094.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7000** | 3.9621 | ±7.9243 | **+11.029** | **2.76e-28** | *** |
| **Education: graduate level (vs college)** | **-2.7220** | 0.9007 | ±1.8013 | **-3.022** | **0.0025** | ** |
| Education: high school or below (vs college) | +2.0876 | 1.9356 | ±3.8711 | +1.079 | 0.2808 |  |
| Site: UCSD (vs UAB) | -0.1271 | 1.1869 | ±2.3739 | -0.107 | 0.9147 |  |
| Site: UW (vs UAB) | -0.5278 | 1.0980 | ±2.1960 | -0.481 | 0.6307 |  |
| **Age (years)** | **-0.3787** | 0.0419 | ±0.0838 | **-9.039** | **1.58e-19** | *** |
| BMI (kg/m2) | +0.1557 | 0.0845 | ±0.1690 | +1.843 | 0.0653 | . |
| Hypertension | +1.1081 | 1.0032 | ±2.0063 | +1.105 | 0.2693 |  |
| High cholesterol | -0.2399 | 0.8860 | ±1.7720 | -0.271 | 0.7865 |  |
| Kidney disease | -0.1969 | 1.7254 | ±3.4508 | -0.114 | 0.9091 |  |
| **Circulatory disease** | **-3.0286** | 1.2738 | ±2.5475 | **-2.378** | **0.0174** | * |
| Nocturnal time > 180 (%) | +0.0818 | 0.1329 | ±0.2657 | +0.615 | 0.5383 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 774; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **774**, R² = **0.1846**, Adj R² = **0.1739**, F-statistic = **17.28** (p = **1.67e-28**), Residual SE = **7.747** on **763** df, AIC = **5376.6**, BIC = **5427.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5124** | 2.8548 | ±5.7095 | **+21.898** | **2.73e-106** | *** |
| **Education: graduate level (vs college)** | **-2.2952** | 0.6151 | ±1.2303 | **-3.731** | **1.91e-04** | *** |
| Education: high school or below (vs college) | -1.7599 | 0.9955 | ±1.9910 | -1.768 | 0.0771 | . |
| **Site: UCSD (vs UAB)** | **-1.6295** | 0.7479 | ±1.4958 | **-2.179** | **0.0293** | * |
| **Site: UW (vs UAB)** | **-1.8219** | 0.7189 | ±1.4378 | **-2.534** | **0.0113** | * |
| **Age (years)** | **-0.1506** | 0.0295 | ±0.0590 | **-5.107** | **3.27e-07** | *** |
| **BMI (kg/m2)** | **+0.3064** | 0.0552 | ±0.1104 | **+5.552** | **2.83e-08** | *** |
| **Hypertension** | **+1.7532** | 0.6636 | ±1.3272 | **+2.642** | **0.0082** | ** |
| High cholesterol | +0.0066 | 0.5805 | ±1.1611 | +0.011 | 0.9909 |  |
| **Kidney disease** | **+2.8922** | 1.1299 | ±2.2598 | **+2.560** | **0.0105** | * |
| Circulatory disease | -0.0491 | 0.8952 | ±1.7904 | -0.055 | 0.9563 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **774**, R² = **0.1971**, Adj R² = **0.1855**, F-statistic = **17.00** (p = **2.72e-30**), Residual SE = **7.692** on **762** df, AIC = **5366.7**, BIC = **5422.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1542** | 4.2788 | ±8.5576 | **+11.722** | **9.89e-32** | *** |
| **Education: graduate level (vs college)** | **-2.2868** | 0.6084 | ±1.2168 | **-3.759** | **1.71e-04** | *** |
| Education: high school or below (vs college) | -1.8679 | 0.9992 | ±1.9984 | -1.869 | 0.0616 | . |
| **Site: UCSD (vs UAB)** | **-1.5987** | 0.7349 | ±1.4699 | **-2.175** | **0.0296** | * |
| **Site: UW (vs UAB)** | **-1.7773** | 0.7121 | ±1.4243 | **-2.496** | **0.0126** | * |
| **Age (years)** | **-0.1550** | 0.0290 | ±0.0580 | **-5.343** | **9.12e-08** | *** |
| **BMI (kg/m2)** | **+0.2808** | 0.0534 | ±0.1068 | **+5.259** | **1.45e-07** | *** |
| **Hypertension** | **+1.4631** | 0.6635 | ±1.3270 | **+2.205** | **0.0274** | * |
| High cholesterol | -0.3339 | 0.5734 | ±1.1467 | -0.582 | 0.5603 |  |
| **Kidney disease** | **+3.0027** | 1.0989 | ±2.1979 | **+2.732** | **0.0063** | ** |
| Circulatory disease | -0.2439 | 0.8630 | ±1.7260 | -0.283 | 0.7774 |  |
| **HbA1c (%)** | **+2.4096** | 0.7358 | ±1.4716 | **+3.275** | **0.0011** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **774**, R² = **0.2022**, Adj R² = **0.1907**, F-statistic = **17.56** (p = **2.64e-31**), Residual SE = **7.668** on **762** df, AIC = **5361.7**, BIC = **5417.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.8437** | 3.5942 | ±7.1884 | **+14.424** | **3.64e-47** | *** |
| **Education: graduate level (vs college)** | **-2.3253** | 0.6078 | ±1.2157 | **-3.826** | **1.30e-04** | *** |
| Education: high school or below (vs college) | -1.7122 | 0.9815 | ±1.9630 | -1.745 | 0.0811 | . |
| **Site: UCSD (vs UAB)** | **-1.5409** | 0.7372 | ±1.4744 | **-2.090** | **0.0366** | * |
| **Site: UW (vs UAB)** | **-1.9361** | 0.7096 | ±1.4192 | **-2.728** | **0.0064** | ** |
| **Age (years)** | **-0.1524** | 0.0290 | ±0.0579 | **-5.264** | **1.41e-07** | *** |
| **BMI (kg/m2)** | **+0.2848** | 0.0532 | ±0.1063 | **+5.357** | **8.47e-08** | *** |
| **Hypertension** | **+1.4925** | 0.6579 | ±1.3157 | **+2.269** | **0.0233** | * |
| High cholesterol | -0.1060 | 0.5737 | ±1.1475 | -0.185 | 0.8535 |  |
| **Kidney disease** | **+2.6195** | 1.1131 | ±2.2263 | **+2.353** | **0.0186** | * |
| Circulatory disease | -0.2817 | 0.8711 | ±1.7422 | -0.323 | 0.7464 |  |
| **Mean glucose (mg/dL)** | **+0.0965** | 0.0227 | ±0.0454 | **+4.256** | **2.08e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **774**, R² = **0.2022**, Adj R² = **0.1907**, F-statistic = **17.56** (p = **2.64e-31**), Residual SE = **7.668** on **762** df, AIC = **5361.7**, BIC = **5417.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+38.4854** | 6.1119 | ±12.2237 | **+6.297** | **3.04e-10** | *** |
| **Education: graduate level (vs college)** | **-2.3253** | 0.6078 | ±1.2157 | **-3.826** | **1.30e-04** | *** |
| Education: high school or below (vs college) | -1.7122 | 0.9815 | ±1.9630 | -1.745 | 0.0811 | . |
| **Site: UCSD (vs UAB)** | **-1.5409** | 0.7372 | ±1.4744 | **-2.090** | **0.0366** | * |
| **Site: UW (vs UAB)** | **-1.9361** | 0.7096 | ±1.4192 | **-2.728** | **0.0064** | ** |
| **Age (years)** | **-0.1524** | 0.0290 | ±0.0579 | **-5.264** | **1.41e-07** | *** |
| **BMI (kg/m2)** | **+0.2848** | 0.0532 | ±0.1063 | **+5.357** | **8.47e-08** | *** |
| **Hypertension** | **+1.4925** | 0.6579 | ±1.3157 | **+2.269** | **0.0233** | * |
| High cholesterol | -0.1060 | 0.5737 | ±1.1475 | -0.185 | 0.8535 |  |
| **Kidney disease** | **+2.6195** | 1.1131 | ±2.2263 | **+2.353** | **0.0186** | * |
| Circulatory disease | -0.2817 | 0.8711 | ±1.7422 | -0.323 | 0.7464 |  |
| **GMI (%)** | **+4.0358** | 0.9482 | ±1.8964 | **+4.256** | **2.08e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **774**, R² = **0.2015**, Adj R² = **0.1900**, F-statistic = **17.48** (p = **3.64e-31**), Residual SE = **7.671** on **762** df, AIC = **5362.4**, BIC = **5418.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.2659** | 3.2182 | ±6.4364 | **+16.551** | **1.56e-61** | *** |
| **Education: graduate level (vs college)** | **-2.3109** | 0.6067 | ±1.2133 | **-3.809** | **1.39e-04** | *** |
| Education: high school or below (vs college) | -1.7781 | 0.9907 | ±1.9814 | -1.795 | 0.0727 | . |
| **Site: UCSD (vs UAB)** | **-1.6524** | 0.7405 | ±1.4811 | **-2.231** | **0.0257** | * |
| **Site: UW (vs UAB)** | **-1.9670** | 0.7105 | ±1.4209 | **-2.769** | **0.0056** | ** |
| **Age (years)** | **-0.1440** | 0.0289 | ±0.0578 | **-4.982** | **6.29e-07** | *** |
| **BMI (kg/m2)** | **+0.2724** | 0.0525 | ±0.1051 | **+5.186** | **2.15e-07** | *** |
| **Hypertension** | **+1.5639** | 0.6583 | ±1.3166 | **+2.376** | **0.0175** | * |
| High cholesterol | -0.1641 | 0.5743 | ±1.1485 | -0.286 | 0.7750 |  |
| **Kidney disease** | **+2.8243** | 1.1018 | ±2.2036 | **+2.563** | **0.0104** | * |
| Circulatory disease | -0.2468 | 0.8648 | ±1.7295 | -0.285 | 0.7753 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.0839** | 0.0198 | ±0.0396 | **+4.241** | **2.22e-05** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **774**, R² = **0.1917**, Adj R² = **0.1800**, F-statistic = **16.43** (p = **3.08e-29**), Residual SE = **7.718** on **762** df, AIC = **5371.9**, BIC = **5427.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.4726** | 2.9048 | ±5.8096 | **+20.474** | **3.67e-93** | *** |
| **Education: graduate level (vs college)** | **-2.2318** | 0.6120 | ±1.2239 | **-3.647** | **2.65e-04** | *** |
| Education: high school or below (vs college) | -1.8769 | 0.9917 | ±1.9834 | -1.893 | 0.0584 | . |
| **Site: UCSD (vs UAB)** | **-1.5000** | 0.7434 | ±1.4869 | **-2.018** | **0.0436** | * |
| **Site: UW (vs UAB)** | **-1.8176** | 0.7150 | ±1.4300 | **-2.542** | **0.0110** | * |
| **Age (years)** | **-0.1547** | 0.0296 | ±0.0592 | **-5.229** | **1.71e-07** | *** |
| **BMI (kg/m2)** | **+0.3009** | 0.0540 | ±0.1080 | **+5.574** | **2.49e-08** | *** |
| **Hypertension** | **+1.5360** | 0.6610 | ±1.3220 | **+2.324** | **0.0201** | * |
| High cholesterol | -0.0490 | 0.5773 | ±1.1545 | -0.085 | 0.9323 |  |
| **Kidney disease** | **+2.7013** | 1.1246 | ±2.2492 | **+2.402** | **0.0163** | * |
| Circulatory disease | -0.1379 | 0.8772 | ±1.7545 | -0.157 | 0.8751 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.1782** | 0.0708 | ±0.1416 | **+2.516** | **0.0119** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **774**, R² = **0.1921**, Adj R² = **0.1805**, F-statistic = **16.47** (p = **2.54e-29**), Residual SE = **7.716** on **762** df, AIC = **5371.5**, BIC = **5427.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.6481** | 2.8677 | ±5.7353 | **+20.800** | **4.31e-96** | *** |
| **Education: graduate level (vs college)** | **-2.2483** | 0.6117 | ±1.2234 | **-3.676** | **2.37e-04** | *** |
| Education: high school or below (vs college) | -1.8554 | 0.9900 | ±1.9799 | -1.874 | 0.0609 | . |
| **Site: UCSD (vs UAB)** | **-1.5018** | 0.7427 | ±1.4853 | **-2.022** | **0.0432** | * |
| **Site: UW (vs UAB)** | **-1.8380** | 0.7153 | ±1.4307 | **-2.569** | **0.0102** | * |
| **Age (years)** | **-0.1551** | 0.0296 | ±0.0592 | **-5.242** | **1.59e-07** | *** |
| **BMI (kg/m2)** | **+0.3002** | 0.0538 | ±0.1076 | **+5.577** | **2.45e-08** | *** |
| **Hypertension** | **+1.5278** | 0.6633 | ±1.3267 | **+2.303** | **0.0213** | * |
| High cholesterol | -0.0371 | 0.5770 | ±1.1540 | -0.064 | 0.9488 |  |
| **Kidney disease** | **+2.7243** | 1.1230 | ±2.2461 | **+2.426** | **0.0153** | * |
| Circulatory disease | -0.1223 | 0.8769 | ±1.7538 | -0.139 | 0.8891 |  |
| **Avg. daily SD (mg/dL)** | **+0.1875** | 0.0733 | ±0.1466 | **+2.559** | **0.0105** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **774**, R² = **0.1850**, Adj R² = **0.1732**, F-statistic = **15.72** (p = **6.18e-28**), Residual SE = **7.750** on **762** df, AIC = **5378.3**, BIC = **5434.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.6669** | 3.0977 | ±6.1955 | **+19.907** | **3.53e-88** | *** |
| **Education: graduate level (vs college)** | **-2.2749** | 0.6176 | ±1.2351 | **-3.684** | **2.30e-04** | *** |
| Education: high school or below (vs college) | -1.7923 | 1.0003 | ±2.0007 | -1.792 | 0.0732 | . |
| **Site: UCSD (vs UAB)** | **-1.6028** | 0.7483 | ±1.4966 | **-2.142** | **0.0322** | * |
| **Site: UW (vs UAB)** | **-1.8127** | 0.7198 | ±1.4395 | **-2.518** | **0.0118** | * |
| **Age (years)** | **-0.1515** | 0.0298 | ±0.0596 | **-5.082** | **3.74e-07** | *** |
| **BMI (kg/m2)** | **+0.3067** | 0.0551 | ±0.1102 | **+5.565** | **2.62e-08** | *** |
| **Hypertension** | **+1.7174** | 0.6627 | ±1.3254 | **+2.591** | **0.0096** | ** |
| High cholesterol | +0.0033 | 0.5808 | ±1.1617 | +0.006 | 0.9954 |  |
| **Kidney disease** | **+2.8643** | 1.1348 | ±2.2696 | **+2.524** | **0.0116** | * |
| Circulatory disease | -0.0512 | 0.8934 | ±1.7868 | -0.057 | 0.9543 |  |
| CV (%) | +0.0543 | 0.0980 | ±0.1960 | +0.554 | 0.5799 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **774**, R² = **0.1849**, Adj R² = **0.1731**, F-statistic = **15.71** (p = **6.38e-28**), Residual SE = **7.751** on **762** df, AIC = **5378.4**, BIC = **5434.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.3112** | 3.3641 | ±6.7282 | **+18.820** | **5.22e-79** | *** |
| **Education: graduate level (vs college)** | **-2.2741** | 0.6180 | ±1.2360 | **-3.680** | **2.33e-04** | *** |
| Education: high school or below (vs college) | -1.7856 | 0.9985 | ±1.9970 | -1.788 | 0.0737 | . |
| **Site: UCSD (vs UAB)** | **-1.6104** | 0.7482 | ±1.4963 | **-2.152** | **0.0314** | * |
| **Site: UW (vs UAB)** | **-1.8195** | 0.7194 | ±1.4387 | **-2.529** | **0.0114** | * |
| **Age (years)** | **-0.1513** | 0.0297 | ±0.0595 | **-5.087** | **3.65e-07** | *** |
| **BMI (kg/m2)** | **+0.3065** | 0.0551 | ±0.1102 | **+5.562** | **2.66e-08** | *** |
| **Hypertension** | **+1.7231** | 0.6622 | ±1.3244 | **+2.602** | **0.0093** | ** |
| High cholesterol | +0.0048 | 0.5809 | ±1.1618 | +0.008 | 0.9934 |  |
| **Kidney disease** | **+2.8678** | 1.1352 | ±2.2703 | **+2.526** | **0.0115** | * |
| Circulatory disease | -0.0468 | 0.8942 | ±1.7885 | -0.052 | 0.9583 |  |
| Mean / SD ratio | -0.1203 | 0.2299 | ±0.4598 | -0.523 | 0.6007 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **774**, R² = **0.1854**, Adj R² = **0.1736**, F-statistic = **15.76** (p = **5.22e-28**), Residual SE = **7.748** on **762** df, AIC = **5377.9**, BIC = **5433.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.7548** | 3.3168 | ±6.6337 | **+19.222** | **2.44e-82** | *** |
| **Education: graduate level (vs college)** | **-2.2673** | 0.6171 | ±1.2341 | **-3.674** | **2.38e-04** | *** |
| Education: high school or below (vs college) | -1.7953 | 0.9964 | ±1.9928 | -1.802 | 0.0716 | . |
| **Site: UCSD (vs UAB)** | **-1.6017** | 0.7476 | ±1.4951 | **-2.143** | **0.0321** | * |
| **Site: UW (vs UAB)** | **-1.8253** | 0.7192 | ±1.4384 | **-2.538** | **0.0112** | * |
| **Age (years)** | **-0.1520** | 0.0298 | ±0.0595 | **-5.105** | **3.31e-07** | *** |
| **BMI (kg/m2)** | **+0.3059** | 0.0550 | ±0.1100 | **+5.562** | **2.66e-08** | *** |
| **Hypertension** | **+1.7095** | 0.6626 | ±1.3252 | **+2.580** | **0.0099** | ** |
| High cholesterol | +0.0062 | 0.5809 | ±1.1617 | +0.011 | 0.9915 |  |
| **Kidney disease** | **+2.8549** | 1.1329 | ±2.2659 | **+2.520** | **0.0117** | * |
| Circulatory disease | -0.0369 | 0.8942 | ±1.7884 | -0.041 | 0.9671 |  |
| Avg. daily mean/SD | -0.1598 | 0.1825 | ±0.3650 | -0.876 | 0.3812 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **774**, R² = **0.1966**, Adj R² = **0.1850**, F-statistic = **16.95** (p = **3.38e-30**), Residual SE = **7.695** on **762** df, AIC = **5367.2**, BIC = **5423.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.4565** | 2.9834 | ±5.9668 | **+19.259** | **1.19e-82** | *** |
| **Education: graduate level (vs college)** | **-2.2730** | 0.6090 | ±1.2180 | **-3.732** | **1.90e-04** | *** |
| **Education: high school or below (vs college)** | **-2.0144** | 0.9905 | ±1.9809 | **-2.034** | **0.0420** | * |
| **Site: UCSD (vs UAB)** | **-1.5671** | 0.7426 | ±1.4852 | **-2.110** | **0.0348** | * |
| **Site: UW (vs UAB)** | **-1.7900** | 0.7151 | ±1.4302 | **-2.503** | **0.0123** | * |
| **Age (years)** | **-0.1496** | 0.0291 | ±0.0581 | **-5.148** | **2.63e-07** | *** |
| **BMI (kg/m2)** | **+0.3048** | 0.0529 | ±0.1059 | **+5.759** | **8.46e-09** | *** |
| **Hypertension** | **+1.8119** | 0.6608 | ±1.3215 | **+2.742** | **0.0061** | ** |
| High cholesterol | -0.0216 | 0.5774 | ±1.1548 | -0.037 | 0.9702 |  |
| **Kidney disease** | **+2.7607** | 1.1236 | ±2.2471 | **+2.457** | **0.0140** | * |
| Circulatory disease | +0.0309 | 0.8790 | ±1.7579 | +0.035 | 0.9720 |  |
| **MAG (mg/dL/h)** | **+0.1394** | 0.0438 | ±0.0877 | **+3.179** | **0.0015** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **774**, R² = **0.1917**, Adj R² = **0.1800**, F-statistic = **16.43** (p = **3.07e-29**), Residual SE = **7.718** on **762** df, AIC = **5371.9**, BIC = **5427.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.8182** | 3.0528 | ±6.1056 | **+19.267** | **1.02e-82** | *** |
| **Education: graduate level (vs college)** | **-2.2721** | 0.6121 | ±1.2242 | **-3.712** | **2.06e-04** | *** |
| Education: high school or below (vs college) | -1.8947 | 0.9940 | ±1.9881 | -1.906 | 0.0566 | . |
| **Site: UCSD (vs UAB)** | **-1.5392** | 0.7448 | ±1.4896 | **-2.067** | **0.0388** | * |
| **Site: UW (vs UAB)** | **-1.8425** | 0.7158 | ±1.4317 | **-2.574** | **0.0101** | * |
| **Age (years)** | **-0.1544** | 0.0296 | ±0.0591 | **-5.225** | **1.74e-07** | *** |
| **BMI (kg/m2)** | **+0.3095** | 0.0548 | ±0.1095 | **+5.653** | **1.58e-08** | *** |
| **Hypertension** | **+1.6140** | 0.6626 | ±1.3252 | **+2.436** | **0.0149** | * |
| High cholesterol | -0.0117 | 0.5781 | ±1.1562 | -0.020 | 0.9839 |  |
| **Kidney disease** | **+2.7448** | 1.1246 | ±2.2491 | **+2.441** | **0.0147** | * |
| Circulatory disease | -0.1213 | 0.8748 | ±1.7496 | -0.139 | 0.8897 |  |
| **Avg. daily range (mg/dL)** | **+0.0430** | 0.0170 | ±0.0340 | **+2.529** | **0.0114** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **774**, R² = **0.1918**, Adj R² = **0.1801**, F-statistic = **16.43** (p = **3.01e-29**), Residual SE = **7.718** on **762** df, AIC = **5371.8**, BIC = **5427.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.9592** | 2.8063 | ±5.6127 | **+21.722** | **1.27e-104** | *** |
| **Education: graduate level (vs college)** | **-2.2920** | 0.6113 | ±1.2227 | **-3.749** | **1.77e-04** | *** |
| Education: high school or below (vs college) | -1.9006 | 0.9910 | ±1.9820 | -1.918 | 0.0551 | . |
| **Site: UCSD (vs UAB)** | **-1.5170** | 0.7440 | ±1.4879 | **-2.039** | **0.0414** | * |
| **Site: UW (vs UAB)** | **-1.7575** | 0.7144 | ±1.4287 | **-2.460** | **0.0139** | * |
| **Age (years)** | **-0.1499** | 0.0292 | ±0.0584 | **-5.135** | **2.83e-07** | *** |
| **BMI (kg/m2)** | **+0.2960** | 0.0541 | ±0.1083 | **+5.467** | **4.57e-08** | *** |
| **Hypertension** | **+1.7248** | 0.6565 | ±1.3130 | **+2.627** | **0.0086** | ** |
| High cholesterol | -0.1176 | 0.5811 | ±1.1623 | -0.202 | 0.8397 |  |
| **Kidney disease** | **+2.7516** | 1.1123 | ±2.2247 | **+2.474** | **0.0134** | * |
| Circulatory disease | -0.1926 | 0.8894 | ±1.7788 | -0.217 | 0.8286 |  |
| **SD of daily means (mg/dL)** | **+0.3126** | 0.1332 | ±0.2665 | **+2.347** | **0.0190** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **774**, R² = **0.1924**, Adj R² = **0.1807**, F-statistic = **16.50** (p = **2.25e-29**), Residual SE = **7.715** on **762** df, AIC = **5371.2**, BIC = **5427.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+85.0226** | 8.7041 | ±17.4083 | **+9.768** | **1.54e-22** | *** |
| **Education: graduate level (vs college)** | **-2.3049** | 0.6107 | ±1.2215 | **-3.774** | **1.61e-04** | *** |
| Education: high school or below (vs college) | -1.7803 | 0.9981 | ±1.9963 | -1.784 | 0.0745 | . |
| **Site: UCSD (vs UAB)** | **-1.5465** | 0.7460 | ±1.4920 | **-2.073** | **0.0382** | * |
| **Site: UW (vs UAB)** | **-1.8339** | 0.7132 | ±1.4263 | **-2.571** | **0.0101** | * |
| **Age (years)** | **-0.1540** | 0.0294 | ±0.0588 | **-5.236** | **1.64e-07** | *** |
| **BMI (kg/m2)** | **+0.2987** | 0.0541 | ±0.1083 | **+5.518** | **3.44e-08** | *** |
| **Hypertension** | **+1.6555** | 0.6619 | ±1.3238 | **+2.501** | **0.0124** | * |
| High cholesterol | -0.0963 | 0.5772 | ±1.1545 | -0.167 | 0.8675 |  |
| **Kidney disease** | **+2.6823** | 1.1224 | ±2.2448 | **+2.390** | **0.0169** | * |
| Circulatory disease | -0.2622 | 0.8880 | ±1.7759 | -0.295 | 0.7678 |  |
| **Time in range 70-180, pooled (%)** | **-0.2250** | 0.0806 | ±0.1612 | **-2.791** | **0.0053** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **774**, R² = **0.1933**, Adj R² = **0.1816**, F-statistic = **16.60** (p = **1.51e-29**), Residual SE = **7.711** on **762** df, AIC = **5370.4**, BIC = **5426.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+86.9031** | 8.8506 | ±17.7012 | **+9.819** | **9.34e-23** | *** |
| **Education: graduate level (vs college)** | **-2.3017** | 0.6101 | ±1.2203 | **-3.772** | **1.62e-04** | *** |
| Education: high school or below (vs college) | -1.7536 | 0.9977 | ±1.9954 | -1.758 | 0.0788 | . |
| **Site: UCSD (vs UAB)** | **-1.5347** | 0.7449 | ±1.4897 | **-2.060** | **0.0394** | * |
| **Site: UW (vs UAB)** | **-1.8350** | 0.7127 | ±1.4255 | **-2.575** | **0.0100** | * |
| **Age (years)** | **-0.1541** | 0.0294 | ±0.0588 | **-5.245** | **1.56e-07** | *** |
| **BMI (kg/m2)** | **+0.2976** | 0.0539 | ±0.1078 | **+5.523** | **3.34e-08** | *** |
| **Hypertension** | **+1.6462** | 0.6611 | ±1.3223 | **+2.490** | **0.0128** | * |
| High cholesterol | -0.1029 | 0.5764 | ±1.1529 | -0.179 | 0.8583 |  |
| **Kidney disease** | **+2.6613** | 1.1201 | ±2.2401 | **+2.376** | **0.0175** | * |
| Circulatory disease | -0.2891 | 0.8877 | ±1.7753 | -0.326 | 0.7447 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.2435** | 0.0818 | ±0.1637 | **-2.975** | **0.0029** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **774**, R² = **0.1934**, Adj R² = **0.1818**, F-statistic = **16.61** (p = **1.41e-29**), Residual SE = **7.710** on **762** df, AIC = **5370.2**, BIC = **5426.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.9450** | 2.8570 | ±5.7140 | **+22.032** | **1.43e-107** | *** |
| **Education: graduate level (vs college)** | **-2.4288** | 0.6175 | ±1.2349 | **-3.933** | **8.38e-05** | *** |
| Education: high school or below (vs college) | -1.8664 | 0.9933 | ±1.9866 | -1.879 | 0.0602 | . |
| **Site: UCSD (vs UAB)** | **-1.5559** | 0.7447 | ±1.4894 | **-2.089** | **0.0367** | * |
| **Site: UW (vs UAB)** | **-1.8447** | 0.7166 | ±1.4333 | **-2.574** | **0.0101** | * |
| **Age (years)** | **-0.1497** | 0.0294 | ±0.0588 | **-5.093** | **3.52e-07** | *** |
| **BMI (kg/m2)** | **+0.3031** | 0.0553 | ±0.1106 | **+5.483** | **4.18e-08** | *** |
| **Hypertension** | **+1.7273** | 0.6608 | ±1.3217 | **+2.614** | **0.0090** | ** |
| High cholesterol | +0.0328 | 0.5804 | ±1.1607 | +0.057 | 0.9549 |  |
| **Kidney disease** | **+2.8039** | 1.1229 | ±2.2458 | **+2.497** | **0.0125** | * |
| Circulatory disease | -0.0696 | 0.8901 | ±1.7802 | -0.078 | 0.9376 |  |
| **Time 54-69, pooled (%)** | **-1.6258** | 0.6836 | ±1.3672 | **-2.378** | **0.0174** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **774**, R² = **0.1923**, Adj R² = **0.1806**, F-statistic = **16.49** (p = **2.35e-29**), Residual SE = **7.715** on **762** df, AIC = **5371.3**, BIC = **5427.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8490** | 2.8548 | ±5.7096 | **+22.015** | **2.05e-107** | *** |
| **Education: graduate level (vs college)** | **-2.4273** | 0.6178 | ±1.2356 | **-3.929** | **8.53e-05** | *** |
| Education: high school or below (vs college) | -1.8767 | 0.9931 | ±1.9862 | -1.890 | 0.0588 | . |
| **Site: UCSD (vs UAB)** | **-1.5271** | 0.7445 | ±1.4890 | **-2.051** | **0.0403** | * |
| **Site: UW (vs UAB)** | **-1.8312** | 0.7169 | ±1.4338 | **-2.554** | **0.0106** | * |
| **Age (years)** | **-0.1492** | 0.0294 | ±0.0588 | **-5.074** | **3.89e-07** | *** |
| **BMI (kg/m2)** | **+0.3035** | 0.0553 | ±0.1107 | **+5.483** | **4.18e-08** | *** |
| **Hypertension** | **+1.7278** | 0.6613 | ±1.3226 | **+2.613** | **0.0090** | ** |
| High cholesterol | +0.0265 | 0.5805 | ±1.1610 | +0.046 | 0.9636 |  |
| **Kidney disease** | **+2.8003** | 1.1241 | ±2.2482 | **+2.491** | **0.0127** | * |
| Circulatory disease | -0.0904 | 0.8902 | ±1.7805 | -0.101 | 0.9192 |  |
| **Avg. daily time 54-69 (%)** | **-1.4725** | 0.6774 | ±1.3548 | **-2.174** | **0.0297** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **774**, R² = **0.1934**, Adj R² = **0.1818**, F-statistic = **16.61** (p = **1.41e-29**), Residual SE = **7.710** on **762** df, AIC = **5370.2**, BIC = **5426.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.9450** | 2.8570 | ±5.7140 | **+22.032** | **1.43e-107** | *** |
| **Education: graduate level (vs college)** | **-2.4288** | 0.6175 | ±1.2349 | **-3.933** | **8.38e-05** | *** |
| Education: high school or below (vs college) | -1.8664 | 0.9933 | ±1.9866 | -1.879 | 0.0602 | . |
| **Site: UCSD (vs UAB)** | **-1.5559** | 0.7447 | ±1.4894 | **-2.089** | **0.0367** | * |
| **Site: UW (vs UAB)** | **-1.8447** | 0.7166 | ±1.4333 | **-2.574** | **0.0101** | * |
| **Age (years)** | **-0.1497** | 0.0294 | ±0.0588 | **-5.093** | **3.52e-07** | *** |
| **BMI (kg/m2)** | **+0.3031** | 0.0553 | ±0.1106 | **+5.483** | **4.18e-08** | *** |
| **Hypertension** | **+1.7273** | 0.6608 | ±1.3217 | **+2.614** | **0.0090** | ** |
| High cholesterol | +0.0328 | 0.5804 | ±1.1607 | +0.057 | 0.9549 |  |
| **Kidney disease** | **+2.8039** | 1.1229 | ±2.2458 | **+2.497** | **0.0125** | * |
| Circulatory disease | -0.0696 | 0.8901 | ±1.7802 | -0.078 | 0.9376 |  |
| **Time < 70 (%)** | **-1.6258** | 0.6836 | ±1.3672 | **-2.378** | **0.0174** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **774**, R² = **0.1923**, Adj R² = **0.1806**, F-statistic = **16.49** (p = **2.35e-29**), Residual SE = **7.715** on **762** df, AIC = **5371.3**, BIC = **5427.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8490** | 2.8548 | ±5.7096 | **+22.015** | **2.05e-107** | *** |
| **Education: graduate level (vs college)** | **-2.4273** | 0.6178 | ±1.2356 | **-3.929** | **8.53e-05** | *** |
| Education: high school or below (vs college) | -1.8767 | 0.9931 | ±1.9862 | -1.890 | 0.0588 | . |
| **Site: UCSD (vs UAB)** | **-1.5271** | 0.7445 | ±1.4890 | **-2.051** | **0.0403** | * |
| **Site: UW (vs UAB)** | **-1.8312** | 0.7169 | ±1.4338 | **-2.554** | **0.0106** | * |
| **Age (years)** | **-0.1492** | 0.0294 | ±0.0588 | **-5.074** | **3.89e-07** | *** |
| **BMI (kg/m2)** | **+0.3035** | 0.0553 | ±0.1107 | **+5.483** | **4.18e-08** | *** |
| **Hypertension** | **+1.7278** | 0.6613 | ±1.3226 | **+2.613** | **0.0090** | ** |
| High cholesterol | +0.0265 | 0.5805 | ±1.1610 | +0.046 | 0.9636 |  |
| **Kidney disease** | **+2.8003** | 1.1241 | ±2.2482 | **+2.491** | **0.0127** | * |
| Circulatory disease | -0.0904 | 0.8902 | ±1.7805 | -0.101 | 0.9192 |  |
| **Avg. daily time < 70 (%)** | **-1.4725** | 0.6774 | ±1.3548 | **-2.174** | **0.0297** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **774**, R² = **0.1949**, Adj R² = **0.1833**, F-statistic = **16.77** (p = **7.39e-30**), Residual SE = **7.703** on **762** df, AIC = **5368.8**, BIC = **5424.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5969** | 2.8064 | ±5.6127 | **+22.305** | **3.27e-110** | *** |
| **Education: graduate level (vs college)** | **-2.3274** | 0.6096 | ±1.2191 | **-3.818** | **1.34e-04** | *** |
| Education: high school or below (vs college) | -1.8000 | 0.9981 | ±1.9961 | -1.803 | 0.0713 | . |
| **Site: UCSD (vs UAB)** | **-1.5232** | 0.7454 | ±1.4907 | **-2.044** | **0.0410** | * |
| **Site: UW (vs UAB)** | **-1.8392** | 0.7121 | ±1.4242 | **-2.583** | **0.0098** | ** |
| **Age (years)** | **-0.1543** | 0.0294 | ±0.0587 | **-5.255** | **1.48e-07** | *** |
| **BMI (kg/m2)** | **+0.2971** | 0.0540 | ±0.1079 | **+5.506** | **3.67e-08** | *** |
| **Hypertension** | **+1.6377** | 0.6616 | ±1.3233 | **+2.475** | **0.0133** | * |
| High cholesterol | -0.1065 | 0.5762 | ±1.1525 | -0.185 | 0.8533 |  |
| **Kidney disease** | **+2.6390** | 1.1202 | ±2.2404 | **+2.356** | **0.0185** | * |
| Circulatory disease | -0.2952 | 0.8863 | ±1.7725 | -0.333 | 0.7390 |  |
| **Time 181-250, pooled (%)** | **+0.2564** | 0.0819 | ±0.1638 | **+3.132** | **0.0017** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **774**, R² = **0.1958**, Adj R² = **0.1842**, F-statistic = **16.87** (p = **4.81e-30**), Residual SE = **7.698** on **762** df, AIC = **5367.9**, BIC = **5423.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6230** | 2.7958 | ±5.5916 | **+22.399** | **4.02e-111** | *** |
| **Education: graduate level (vs college)** | **-2.3272** | 0.6089 | ±1.2177 | **-3.822** | **1.32e-04** | *** |
| Education: high school or below (vs college) | -1.7746 | 0.9973 | ±1.9946 | -1.779 | 0.0752 | . |
| **Site: UCSD (vs UAB)** | **-1.5035** | 0.7441 | ±1.4881 | **-2.021** | **0.0433** | * |
| **Site: UW (vs UAB)** | **-1.8385** | 0.7117 | ±1.4235 | **-2.583** | **0.0098** | ** |
| **Age (years)** | **-0.1543** | 0.0293 | ±0.0587 | **-5.261** | **1.43e-07** | *** |
| **BMI (kg/m2)** | **+0.2959** | 0.0537 | ±0.1074 | **+5.510** | **3.58e-08** | *** |
| **Hypertension** | **+1.6278** | 0.6608 | ±1.3217 | **+2.463** | **0.0138** | * |
| High cholesterol | -0.1133 | 0.5754 | ±1.1508 | -0.197 | 0.8440 |  |
| **Kidney disease** | **+2.6145** | 1.1179 | ±2.2357 | **+2.339** | **0.0193** | * |
| Circulatory disease | -0.3275 | 0.8861 | ±1.7722 | -0.370 | 0.7117 |  |
| **Avg. daily time 181-250 (%)** | **+0.2747** | 0.0823 | ±0.1646 | **+3.338** | **8.45e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **774**, R² = **0.1949**, Adj R² = **0.1833**, F-statistic = **16.77** (p = **7.39e-30**), Residual SE = **7.703** on **762** df, AIC = **5368.8**, BIC = **5424.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5969** | 2.8064 | ±5.6127 | **+22.305** | **3.27e-110** | *** |
| **Education: graduate level (vs college)** | **-2.3274** | 0.6096 | ±1.2191 | **-3.818** | **1.34e-04** | *** |
| Education: high school or below (vs college) | -1.8000 | 0.9981 | ±1.9961 | -1.803 | 0.0713 | . |
| **Site: UCSD (vs UAB)** | **-1.5232** | 0.7454 | ±1.4907 | **-2.044** | **0.0410** | * |
| **Site: UW (vs UAB)** | **-1.8392** | 0.7121 | ±1.4242 | **-2.583** | **0.0098** | ** |
| **Age (years)** | **-0.1543** | 0.0294 | ±0.0587 | **-5.255** | **1.48e-07** | *** |
| **BMI (kg/m2)** | **+0.2971** | 0.0540 | ±0.1079 | **+5.506** | **3.67e-08** | *** |
| **Hypertension** | **+1.6377** | 0.6616 | ±1.3233 | **+2.475** | **0.0133** | * |
| High cholesterol | -0.1065 | 0.5762 | ±1.1525 | -0.185 | 0.8533 |  |
| **Kidney disease** | **+2.6390** | 1.1202 | ±2.2404 | **+2.356** | **0.0185** | * |
| Circulatory disease | -0.2952 | 0.8863 | ±1.7725 | -0.333 | 0.7390 |  |
| **Time > 180 (%)** | **+0.2564** | 0.0819 | ±0.1638 | **+3.132** | **0.0017** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **774**, R² = **0.1958**, Adj R² = **0.1842**, F-statistic = **16.87** (p = **4.81e-30**), Residual SE = **7.698** on **762** df, AIC = **5367.9**, BIC = **5423.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6230** | 2.7958 | ±5.5916 | **+22.399** | **4.02e-111** | *** |
| **Education: graduate level (vs college)** | **-2.3272** | 0.6089 | ±1.2177 | **-3.822** | **1.32e-04** | *** |
| Education: high school or below (vs college) | -1.7746 | 0.9973 | ±1.9946 | -1.779 | 0.0752 | . |
| **Site: UCSD (vs UAB)** | **-1.5035** | 0.7441 | ±1.4881 | **-2.021** | **0.0433** | * |
| **Site: UW (vs UAB)** | **-1.8385** | 0.7117 | ±1.4235 | **-2.583** | **0.0098** | ** |
| **Age (years)** | **-0.1543** | 0.0293 | ±0.0587 | **-5.261** | **1.43e-07** | *** |
| **BMI (kg/m2)** | **+0.2959** | 0.0537 | ±0.1074 | **+5.510** | **3.58e-08** | *** |
| **Hypertension** | **+1.6278** | 0.6608 | ±1.3217 | **+2.463** | **0.0138** | * |
| High cholesterol | -0.1133 | 0.5754 | ±1.1508 | -0.197 | 0.8440 |  |
| **Kidney disease** | **+2.6145** | 1.1179 | ±2.2357 | **+2.339** | **0.0193** | * |
| Circulatory disease | -0.3275 | 0.8861 | ±1.7722 | -0.370 | 0.7117 |  |
| **Avg. daily time > 180 (%)** | **+0.2747** | 0.0823 | ±0.1646 | **+3.338** | **8.45e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 774)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **774**, R² = **0.1885**, Adj R² = **0.1768**, F-statistic = **16.09** (p = **1.30e-28**), Residual SE = **7.733** on **762** df, AIC = **5374.9**, BIC = **5430.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6027** | 2.8309 | ±5.6619 | **+22.114** | **2.33e-108** | *** |
| **Education: graduate level (vs college)** | **-2.2823** | 0.6121 | ±1.2242 | **-3.729** | **1.93e-04** | *** |
| Education: high school or below (vs college) | -1.8741 | 0.9997 | ±1.9993 | -1.875 | 0.0608 | . |
| **Site: UCSD (vs UAB)** | **-1.5551** | 0.7466 | ±1.4931 | **-2.083** | **0.0373** | * |
| **Site: UW (vs UAB)** | **-1.8142** | 0.7172 | ±1.4345 | **-2.529** | **0.0114** | * |
| **Age (years)** | **-0.1492** | 0.0295 | ±0.0589 | **-5.061** | **4.17e-07** | *** |
| **BMI (kg/m2)** | **+0.2959** | 0.0549 | ±0.1098 | **+5.390** | **7.04e-08** | *** |
| **Hypertension** | **+1.7600** | 0.6636 | ±1.3272 | **+2.652** | **0.0080** | ** |
| High cholesterol | -0.1081 | 0.5841 | ±1.1682 | -0.185 | 0.8532 |  |
| **Kidney disease** | **+2.7727** | 1.1176 | ±2.2352 | **+2.481** | **0.0131** | * |
| Circulatory disease | -0.1601 | 0.8921 | ±1.7841 | -0.179 | 0.8576 |  |
| **Nocturnal time > 180 (%)** | **+0.1439** | 0.0552 | ±0.1103 | **+2.609** | **0.0091** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 779; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0337**, F-statistic = **3.72** (p = **6.96e-05**), Residual SE = **68.144** on **768** df, AIC = **8798.9**, BIC = **8850.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0289** | 20.0650 | ±40.1300 | **+19.737** | **1.03e-86** | *** |
| Education: graduate level (vs college) | +3.7391 | 5.1659 | ±10.3318 | +0.724 | 0.4692 |  |
| Education: high school or below (vs college) | -10.2480 | 9.4268 | ±18.8535 | -1.087 | 0.2770 |  |
| Site: UCSD (vs UAB) | -11.1787 | 6.4849 | ±12.9697 | -1.724 | 0.0847 | . |
| Site: UW (vs UAB) | -2.2734 | 6.2240 | ±12.4480 | -0.365 | 0.7149 |  |
| Age (years) | +0.2656 | 0.2290 | ±0.4580 | +1.160 | 0.2461 |  |
| **BMI (kg/m2)** | **-1.1725** | 0.3805 | ±0.7609 | **-3.082** | **0.0021** | ** |
| **Hypertension** | **-15.6581** | 5.4435 | ±10.8870 | **-2.876** | **0.0040** | ** |
| High cholesterol | -4.4069 | 5.0157 | ±10.0315 | -0.879 | 0.3796 |  |
| Kidney disease | -11.9639 | 11.6264 | ±23.2527 | -1.029 | 0.3035 |  |
| Circulatory disease | +12.0514 | 8.1584 | ±16.3168 | +1.477 | 0.1396 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **779**, R² = **0.0554**, Adj R² = **0.0419**, F-statistic = **4.09** (p = **7.30e-06**), Residual SE = **67.856** on **767** df, AIC = **8793.3**, BIC = **8849.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+482.7682** | 35.8793 | ±71.7585 | **+13.455** | **2.86e-41** | *** |
| Education: graduate level (vs college) | +3.5461 | 5.1616 | ±10.3231 | +0.687 | 0.4921 |  |
| Education: high school or below (vs college) | -9.4689 | 9.3853 | ±18.7706 | -1.009 | 0.3130 |  |
| Site: UCSD (vs UAB) | -11.7142 | 6.4523 | ±12.9047 | -1.815 | 0.0694 | . |
| Site: UW (vs UAB) | -2.6027 | 6.2097 | ±12.4195 | -0.419 | 0.6751 |  |
| Age (years) | +0.3013 | 0.2298 | ±0.4596 | +1.311 | 0.1899 |  |
| **BMI (kg/m2)** | **-0.9994** | 0.3752 | ±0.7503 | **-2.664** | **0.0077** | ** |
| **Hypertension** | **-13.6168** | 5.4973 | ±10.9947 | **-2.477** | **0.0132** | * |
| High cholesterol | -2.0829 | 5.0807 | ±10.1614 | -0.410 | 0.6818 |  |
| Kidney disease | -12.6035 | 11.3992 | ±22.7983 | -1.106 | 0.2689 |  |
| Circulatory disease | +13.3256 | 8.1530 | ±16.3060 | +1.634 | 0.1022 |  |
| **HbA1c (%)** | **-16.8999** | 6.0907 | ±12.1815 | **-2.775** | **0.0055** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **779**, R² = **0.0481**, Adj R² = **0.0345**, F-statistic = **3.52** (p = **7.71e-05**), Residual SE = **68.118** on **767** df, AIC = **8799.3**, BIC = **8855.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+425.0265** | 29.1694 | ±58.3388 | **+14.571** | **4.30e-48** | *** |
| Education: graduate level (vs college) | +3.8692 | 5.1689 | ±10.3378 | +0.749 | 0.4541 |  |
| Education: high school or below (vs college) | -10.3011 | 9.4304 | ±18.8609 | -1.092 | 0.2747 |  |
| Site: UCSD (vs UAB) | -11.4436 | 6.4843 | ±12.9687 | -1.765 | 0.0776 | . |
| Site: UW (vs UAB) | -1.9769 | 6.2589 | ±12.5179 | -0.316 | 0.7521 |  |
| Age (years) | +0.2716 | 0.2296 | ±0.4591 | +1.183 | 0.2368 |  |
| **BMI (kg/m2)** | **-1.1102** | 0.3816 | ±0.7632 | **-2.909** | **0.0036** | ** |
| **Hypertension** | **-14.9631** | 5.4338 | ±10.8676 | **-2.754** | **0.0059** | ** |
| High cholesterol | -4.1019 | 5.0472 | ±10.0944 | -0.813 | 0.4164 |  |
| Kidney disease | -11.0321 | 11.6922 | ±23.3844 | -0.944 | 0.3454 |  |
| Circulatory disease | +12.5722 | 8.2089 | ±16.4177 | +1.532 | 0.1256 |  |
| Mean glucose (mg/dL) | -0.2638 | 0.2102 | ±0.4204 | -1.255 | 0.2095 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **779**, R² = **0.0481**, Adj R² = **0.0345**, F-statistic = **3.52** (p = **7.71e-05**), Residual SE = **68.118** on **767** df, AIC = **8799.3**, BIC = **8855.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+461.5341** | 54.1930 | ±108.3861 | **+8.516** | **1.64e-17** | *** |
| Education: graduate level (vs college) | +3.8692 | 5.1689 | ±10.3378 | +0.749 | 0.4541 |  |
| Education: high school or below (vs college) | -10.3011 | 9.4304 | ±18.8609 | -1.092 | 0.2747 |  |
| Site: UCSD (vs UAB) | -11.4436 | 6.4843 | ±12.9687 | -1.765 | 0.0776 | . |
| Site: UW (vs UAB) | -1.9769 | 6.2589 | ±12.5179 | -0.316 | 0.7521 |  |
| Age (years) | +0.2716 | 0.2296 | ±0.4591 | +1.183 | 0.2368 |  |
| **BMI (kg/m2)** | **-1.1102** | 0.3816 | ±0.7632 | **-2.909** | **0.0036** | ** |
| **Hypertension** | **-14.9631** | 5.4338 | ±10.8676 | **-2.754** | **0.0059** | ** |
| High cholesterol | -4.1019 | 5.0472 | ±10.0944 | -0.813 | 0.4164 |  |
| Kidney disease | -11.0321 | 11.6922 | ±23.3844 | -0.944 | 0.3454 |  |
| Circulatory disease | +12.5722 | 8.2089 | ±16.4177 | +1.532 | 0.1256 |  |
| GMI (%) | -11.0295 | 8.7885 | ±17.5771 | -1.255 | 0.2095 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **779**, R² = **0.0518**, Adj R² = **0.0382**, F-statistic = **3.81** (p = **2.37e-05**), Residual SE = **67.986** on **767** df, AIC = **8796.3**, BIC = **8852.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+439.6318** | 28.3998 | ±56.7995 | **+15.480** | **4.73e-54** | *** |
| Education: graduate level (vs college) | +3.8390 | 5.1499 | ±10.2999 | +0.745 | 0.4560 |  |
| Education: high school or below (vs college) | -10.0908 | 9.4119 | ±18.8238 | -1.072 | 0.2837 |  |
| Site: UCSD (vs UAB) | -11.1201 | 6.4695 | ±12.9389 | -1.719 | 0.0856 | . |
| Site: UW (vs UAB) | -1.6079 | 6.2510 | ±12.5020 | -0.257 | 0.7970 |  |
| Age (years) | +0.2362 | 0.2278 | ±0.4557 | +1.037 | 0.2999 |  |
| **BMI (kg/m2)** | **-1.0053** | 0.3740 | ±0.7480 | **-2.688** | **0.0072** | ** |
| **Hypertension** | **-14.7319** | 5.4441 | ±10.8883 | **-2.706** | **0.0068** | ** |
| High cholesterol | -3.5412 | 5.0561 | ±10.1122 | -0.700 | 0.4837 |  |
| Kidney disease | -11.3945 | 11.6375 | ±23.2750 | -0.979 | 0.3275 |  |
| Circulatory disease | +12.7781 | 8.2013 | ±16.4026 | +1.558 | 0.1192 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.3983** | 0.1890 | ±0.3780 | **-2.107** | **0.0351** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **779**, R² = **0.0466**, Adj R² = **0.0329**, F-statistic = **3.41** (p = **1.25e-04**), Residual SE = **68.174** on **767** df, AIC = **8800.6**, BIC = **8856.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.9902** | 21.6009 | ±43.2018 | **+18.610** | **2.67e-77** | *** |
| Education: graduate level (vs college) | +3.6322 | 5.1712 | ±10.3423 | +0.702 | 0.4824 |  |
| Education: high school or below (vs college) | -9.9646 | 9.4931 | ±18.9861 | -1.050 | 0.2939 |  |
| Site: UCSD (vs UAB) | -11.4841 | 6.4978 | ±12.9956 | -1.767 | 0.0772 | . |
| Site: UW (vs UAB) | -2.3306 | 6.2342 | ±12.4684 | -0.374 | 0.7085 |  |
| Age (years) | +0.2752 | 0.2317 | ±0.4635 | +1.187 | 0.2351 |  |
| **BMI (kg/m2)** | **-1.1632** | 0.3816 | ±0.7632 | **-3.048** | **0.0023** | ** |
| **Hypertension** | **-15.2816** | 5.4746 | ±10.9492 | **-2.791** | **0.0052** | ** |
| High cholesterol | -4.2797 | 5.0513 | ±10.1025 | -0.847 | 0.3969 |  |
| Kidney disease | -11.4936 | 11.6579 | ±23.3158 | -0.986 | 0.3242 |  |
| Circulatory disease | +12.1904 | 8.1647 | ±16.3294 | +1.493 | 0.1354 |  |
| Glucose SD, pooled (mg/dL) | -0.3496 | 0.6377 | ±1.2754 | -0.548 | 0.5835 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **779**, R² = **0.0466**, Adj R² = **0.0329**, F-statistic = **3.41** (p = **1.23e-04**), Residual SE = **68.172** on **767** df, AIC = **8800.5**, BIC = **8856.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.7971** | 21.2089 | ±42.4178 | **+18.945** | **4.88e-80** | *** |
| Education: graduate level (vs college) | +3.6727 | 5.1699 | ±10.3398 | +0.710 | 0.4775 |  |
| Education: high school or below (vs college) | -9.9956 | 9.4795 | ±18.9589 | -1.054 | 0.2917 |  |
| Site: UCSD (vs UAB) | -11.4903 | 6.5079 | ±13.0157 | -1.766 | 0.0775 | . |
| Site: UW (vs UAB) | -2.2898 | 6.2349 | ±12.4699 | -0.367 | 0.7134 |  |
| Age (years) | +0.2761 | 0.2318 | ±0.4635 | +1.192 | 0.2334 |  |
| **BMI (kg/m2)** | **-1.1618** | 0.3816 | ±0.7632 | **-3.044** | **0.0023** | ** |
| **Hypertension** | **-15.2510** | 5.4846 | ±10.9692 | **-2.781** | **0.0054** | ** |
| High cholesterol | -4.3031 | 5.0434 | ±10.0868 | -0.853 | 0.3935 |  |
| Kidney disease | -11.5060 | 11.6844 | ±23.3688 | -0.985 | 0.3248 |  |
| Circulatory disease | +12.1723 | 8.1655 | ±16.3310 | +1.491 | 0.1360 |  |
| Avg. daily SD (mg/dL) | -0.3773 | 0.6417 | ±1.2835 | -0.588 | 0.5566 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.4775** | 23.4000 | ±46.8001 | **+16.901** | **4.45e-64** | *** |
| Education: graduate level (vs college) | +3.7521 | 5.1827 | ±10.3655 | +0.724 | 0.4691 |  |
| Education: high school or below (vs college) | -10.2726 | 9.5336 | ±19.0673 | -1.078 | 0.2813 |  |
| Site: UCSD (vs UAB) | -11.1581 | 6.5015 | ±13.0030 | -1.716 | 0.0861 | . |
| Site: UW (vs UAB) | -2.2643 | 6.2448 | ±12.4896 | -0.363 | 0.7169 |  |
| Age (years) | +0.2649 | 0.2311 | ±0.4621 | +1.147 | 0.2516 |  |
| **BMI (kg/m2)** | **-1.1721** | 0.3803 | ±0.7607 | **-3.082** | **0.0021** | ** |
| **Hypertension** | **-15.6773** | 5.4733 | ±10.9467 | **-2.864** | **0.0042** | ** |
| High cholesterol | -4.4109 | 5.0315 | ±10.0631 | -0.877 | 0.3807 |  |
| Kidney disease | -11.9860 | 11.6153 | ±23.2305 | -1.032 | 0.3021 |  |
| Circulatory disease | +12.0509 | 8.1689 | ±16.3377 | +1.475 | 0.1402 |  |
| CV (%) | +0.0353 | 0.8978 | ±1.7956 | +0.039 | 0.9686 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.38** (p = **1.40e-04**), Residual SE = **68.187** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+398.5744** | 26.0137 | ±52.0273 | **+15.322** | **5.47e-53** | *** |
| Education: graduate level (vs college) | +3.8019 | 5.1901 | ±10.3801 | +0.733 | 0.4638 |  |
| Education: high school or below (vs college) | -10.3454 | 9.5230 | ±19.0460 | -1.086 | 0.2773 |  |
| Site: UCSD (vs UAB) | -11.1000 | 6.4899 | ±12.9799 | -1.710 | 0.0872 | . |
| Site: UW (vs UAB) | -2.2450 | 6.2395 | ±12.4789 | -0.360 | 0.7190 |  |
| Age (years) | +0.2628 | 0.2310 | ±0.4621 | +1.138 | 0.2553 |  |
| **BMI (kg/m2)** | **-1.1713** | 0.3806 | ±0.7612 | **-3.078** | **0.0021** | ** |
| **Hypertension** | **-15.7349** | 5.4657 | ±10.9314 | **-2.879** | **0.0040** | ** |
| High cholesterol | -4.4226 | 5.0294 | ±10.0588 | -0.879 | 0.3792 |  |
| Kidney disease | -12.0516 | 11.6067 | ±23.2133 | -1.038 | 0.2991 |  |
| Circulatory disease | +12.0619 | 8.1750 | ±16.3501 | +1.475 | 0.1401 |  |
| Mean / SD ratio | -0.3855 | 2.2462 | ±4.4924 | -0.172 | 0.8637 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.1595** | 25.4373 | ±50.8746 | **+15.574** | **1.09e-54** | *** |
| Education: graduate level (vs college) | +3.7417 | 5.1793 | ±10.3586 | +0.722 | 0.4700 |  |
| Education: high school or below (vs college) | -10.2526 | 9.5055 | ±19.0111 | -1.079 | 0.2808 |  |
| Site: UCSD (vs UAB) | -11.1748 | 6.5004 | ±13.0009 | -1.719 | 0.0856 | . |
| Site: UW (vs UAB) | -2.2727 | 6.2334 | ±12.4668 | -0.365 | 0.7154 |  |
| Age (years) | +0.2654 | 0.2313 | ±0.4626 | +1.147 | 0.2512 |  |
| **BMI (kg/m2)** | **-1.1725** | 0.3810 | ±0.7619 | **-3.078** | **0.0021** | ** |
| **Hypertension** | **-15.6618** | 5.4637 | ±10.9275 | **-2.867** | **0.0042** | ** |
| High cholesterol | -4.4075 | 5.0268 | ±10.0537 | -0.877 | 0.3806 |  |
| Kidney disease | -11.9688 | 11.6357 | ±23.2715 | -1.029 | 0.3037 |  |
| Circulatory disease | +12.0527 | 8.1764 | ±16.3529 | +1.474 | 0.1405 |  |
| Avg. daily mean/SD | -0.0169 | 1.7753 | ±3.5506 | -0.010 | 0.9924 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **779**, R² = **0.0565**, Adj R² = **0.0429**, F-statistic = **4.17** (p = **5.19e-06**), Residual SE = **67.819** on **767** df, AIC = **8792.5**, BIC = **8848.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+434.0392** | 22.9255 | ±45.8510 | **+18.933** | **6.15e-80** | *** |
| Education: graduate level (vs college) | +3.7504 | 5.1557 | ±10.3113 | +0.727 | 0.4670 |  |
| Education: high school or below (vs college) | -7.8805 | 9.3442 | ±18.6884 | -0.843 | 0.3990 |  |
| Site: UCSD (vs UAB) | -11.7337 | 6.5311 | ±13.0622 | -1.797 | 0.0724 | . |
| Site: UW (vs UAB) | -2.6855 | 6.2158 | ±12.4315 | -0.432 | 0.6657 |  |
| Age (years) | +0.2640 | 0.2282 | ±0.4564 | +1.157 | 0.2474 |  |
| **BMI (kg/m2)** | **-1.1593** | 0.3756 | ±0.7512 | **-3.087** | **0.0020** | ** |
| **Hypertension** | **-16.2008** | 5.4105 | ±10.8209 | **-2.994** | **0.0028** | ** |
| High cholesterol | -4.2177 | 4.9869 | ±9.9737 | -0.846 | 0.3977 |  |
| Kidney disease | -10.8620 | 11.5934 | ±23.1868 | -0.937 | 0.3488 |  |
| Circulatory disease | +11.0424 | 8.1311 | ±16.2622 | +1.358 | 0.1745 |  |
| **MAG (mg/dL/h)** | **-1.0574** | 0.4362 | ±0.8725 | **-2.424** | **0.0154** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.9158** | 22.9621 | ±45.9242 | **+17.242** | **1.28e-66** | *** |
| Education: graduate level (vs college) | +3.7391 | 5.1741 | ±10.3482 | +0.723 | 0.4699 |  |
| Education: high school or below (vs college) | -10.2531 | 9.5291 | ±19.0582 | -1.076 | 0.2819 |  |
| Site: UCSD (vs UAB) | -11.1751 | 6.5313 | ±13.0626 | -1.711 | 0.0871 | . |
| Site: UW (vs UAB) | -2.2730 | 6.2328 | ±12.4656 | -0.365 | 0.7154 |  |
| Age (years) | +0.2655 | 0.2323 | ±0.4645 | +1.143 | 0.2531 |  |
| **BMI (kg/m2)** | **-1.1724** | 0.3807 | ±0.7615 | **-3.079** | **0.0021** | ** |
| **Hypertension** | **-15.6617** | 5.4541 | ±10.9082 | **-2.872** | **0.0041** | ** |
| High cholesterol | -4.4075 | 5.0326 | ±10.0652 | -0.876 | 0.3811 |  |
| Kidney disease | -11.9698 | 11.6755 | ±23.3509 | -1.025 | 0.3053 |  |
| Circulatory disease | +12.0499 | 8.1667 | ±16.3335 | +1.475 | 0.1401 |  |
| Avg. daily range (mg/dL) | +0.0013 | 0.1589 | ±0.3178 | +0.008 | 0.9934 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **779**, R² = **0.0467**, Adj R² = **0.0330**, F-statistic = **3.41** (p = **1.20e-04**), Residual SE = **68.169** on **767** df, AIC = **8800.5**, BIC = **8856.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+399.3971** | 20.4286 | ±40.8572 | **+19.551** | **4.05e-85** | *** |
| Education: graduate level (vs college) | +3.7011 | 5.1712 | ±10.3424 | +0.716 | 0.4742 |  |
| Education: high school or below (vs college) | -9.9381 | 9.4631 | ±18.9262 | -1.050 | 0.2936 |  |
| Site: UCSD (vs UAB) | -11.4337 | 6.4672 | ±12.9344 | -1.768 | 0.0771 | . |
| Site: UW (vs UAB) | -2.4292 | 6.2247 | ±12.4494 | -0.390 | 0.6964 |  |
| Age (years) | +0.2644 | 0.2292 | ±0.4584 | +1.154 | 0.2487 |  |
| **BMI (kg/m2)** | **-1.1483** | 0.3827 | ±0.7654 | **-3.001** | **0.0027** | ** |
| **Hypertension** | **-15.6671** | 5.4430 | ±10.8861 | **-2.878** | **0.0040** | ** |
| High cholesterol | -4.0790 | 5.0559 | ±10.1119 | -0.807 | 0.4198 |  |
| Kidney disease | -11.6395 | 11.6069 | ±23.2139 | -1.003 | 0.3160 |  |
| Circulatory disease | +12.3588 | 8.1883 | ±16.3767 | +1.509 | 0.1312 |  |
| SD of daily means (mg/dL) | -0.6839 | 1.0582 | ±2.1164 | -0.646 | 0.5181 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.38** (p = **1.41e-04**), Residual SE = **68.187** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+405.6835** | 71.2653 | ±142.5306 | **+5.693** | **1.25e-08** | *** |
| Education: graduate level (vs college) | +3.7363 | 5.1726 | ±10.3452 | +0.722 | 0.4701 |  |
| Education: high school or below (vs college) | -10.2649 | 9.4519 | ±18.9039 | -1.086 | 0.2775 |  |
| Site: UCSD (vs UAB) | -11.1398 | 6.4846 | ±12.9692 | -1.718 | 0.0858 | . |
| Site: UW (vs UAB) | -2.2798 | 6.2332 | ±12.4665 | -0.366 | 0.7146 |  |
| Age (years) | +0.2638 | 0.2296 | ±0.4593 | +1.149 | 0.2506 |  |
| **BMI (kg/m2)** | **-1.1760** | 0.3821 | ±0.7642 | **-3.078** | **0.0021** | ** |
| **Hypertension** | **-15.6991** | 5.4606 | ±10.9211 | **-2.875** | **0.0040** | ** |
| High cholesterol | -4.4505 | 5.0423 | ±10.0845 | -0.883 | 0.3774 |  |
| Kidney disease | -12.0946 | 11.7464 | ±23.4928 | -1.030 | 0.3032 |  |
| Circulatory disease | +11.9704 | 8.2450 | ±16.4900 | +1.452 | 0.1465 |  |
| Time in range 70-180, pooled (%) | -0.0962 | 0.6737 | ±1.3474 | -0.143 | 0.8864 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+394.4073** | 73.0940 | ±146.1880 | **+5.396** | **6.82e-08** | *** |
| Education: graduate level (vs college) | +3.7395 | 5.1720 | ±10.3440 | +0.723 | 0.4697 |  |
| Education: high school or below (vs college) | -10.2470 | 9.4426 | ±18.8852 | -1.085 | 0.2778 |  |
| Site: UCSD (vs UAB) | -11.1855 | 6.4812 | ±12.9624 | -1.726 | 0.0844 | . |
| Site: UW (vs UAB) | -2.2724 | 6.2360 | ±12.4721 | -0.364 | 0.7156 |  |
| Age (years) | +0.2659 | 0.2296 | ±0.4592 | +1.158 | 0.2468 |  |
| **BMI (kg/m2)** | **-1.1719** | 0.3819 | ±0.7638 | **-3.069** | **0.0022** | ** |
| **Hypertension** | **-15.6513** | 5.4647 | ±10.9295 | **-2.864** | **0.0042** | ** |
| High cholesterol | -4.3997 | 5.0378 | ±10.0756 | -0.873 | 0.3825 |  |
| Kidney disease | -11.9415 | 11.7737 | ±23.5474 | -1.014 | 0.3105 |  |
| Circulatory disease | +12.0658 | 8.2618 | ±16.5236 | +1.460 | 0.1442 |  |
| Avg. daily time in range 70-180 (%) | +0.0162 | 0.6937 | ±1.3874 | +0.023 | 0.9814 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.38** (p = **1.39e-04**), Residual SE = **68.186** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.7552** | 20.3133 | ±40.6266 | **+19.483** | **1.54e-84** | *** |
| Education: graduate level (vs college) | +3.8311 | 5.1982 | ±10.3963 | +0.737 | 0.4611 |  |
| Education: high school or below (vs college) | -10.1951 | 9.4336 | ±18.8673 | -1.081 | 0.2798 |  |
| Site: UCSD (vs UAB) | -11.2365 | 6.5074 | ±13.0148 | -1.727 | 0.0842 | . |
| Site: UW (vs UAB) | -2.2742 | 6.2288 | ±12.4577 | -0.365 | 0.7150 |  |
| Age (years) | +0.2647 | 0.2288 | ±0.4576 | +1.157 | 0.2473 |  |
| **BMI (kg/m2)** | **-1.1702** | 0.3822 | ±0.7644 | **-3.062** | **0.0022** | ** |
| **Hypertension** | **-15.6291** | 5.4402 | ±10.8804 | **-2.873** | **0.0041** | ** |
| High cholesterol | -4.4214 | 5.0157 | ±10.0314 | -0.882 | 0.3780 |  |
| Kidney disease | -11.9200 | 11.6340 | ±23.2680 | -1.025 | 0.3056 |  |
| Circulatory disease | +12.0635 | 8.1743 | ±16.3486 | +1.476 | 0.1400 |  |
| Time 54-69, pooled (%) | +1.1459 | 4.5203 | ±9.0405 | +0.254 | 0.7999 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0414** | 20.2281 | ±40.4563 | **+19.579** | **2.35e-85** | *** |
| Education: graduate level (vs college) | +3.7340 | 5.2102 | ±10.4204 | +0.717 | 0.4736 |  |
| Education: high school or below (vs college) | -10.2516 | 9.4372 | ±18.8744 | -1.086 | 0.2773 |  |
| Site: UCSD (vs UAB) | -11.1744 | 6.5168 | ±13.0337 | -1.715 | 0.0864 | . |
| Site: UW (vs UAB) | -2.2730 | 6.2271 | ±12.4543 | -0.365 | 0.7151 |  |
| Age (years) | +0.2657 | 0.2288 | ±0.4577 | +1.161 | 0.2456 |  |
| **BMI (kg/m2)** | **-1.1726** | 0.3814 | ±0.7629 | **-3.074** | **0.0021** | ** |
| **Hypertension** | **-15.6597** | 5.4437 | ±10.8874 | **-2.877** | **0.0040** | ** |
| High cholesterol | -4.4064 | 5.0167 | ±10.0334 | -0.878 | 0.3797 |  |
| Kidney disease | -11.9666 | 11.6396 | ±23.2792 | -1.028 | 0.3039 |  |
| Circulatory disease | +12.0498 | 8.1694 | ±16.3388 | +1.475 | 0.1402 |  |
| Avg. daily time 54-69 (%) | -0.0589 | 4.2605 | ±8.5210 | -0.014 | 0.9890 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.38** (p = **1.39e-04**), Residual SE = **68.186** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.7552** | 20.3133 | ±40.6266 | **+19.483** | **1.54e-84** | *** |
| Education: graduate level (vs college) | +3.8311 | 5.1982 | ±10.3963 | +0.737 | 0.4611 |  |
| Education: high school or below (vs college) | -10.1951 | 9.4336 | ±18.8673 | -1.081 | 0.2798 |  |
| Site: UCSD (vs UAB) | -11.2365 | 6.5074 | ±13.0148 | -1.727 | 0.0842 | . |
| Site: UW (vs UAB) | -2.2742 | 6.2288 | ±12.4577 | -0.365 | 0.7150 |  |
| Age (years) | +0.2647 | 0.2288 | ±0.4576 | +1.157 | 0.2473 |  |
| **BMI (kg/m2)** | **-1.1702** | 0.3822 | ±0.7644 | **-3.062** | **0.0022** | ** |
| **Hypertension** | **-15.6291** | 5.4402 | ±10.8804 | **-2.873** | **0.0041** | ** |
| High cholesterol | -4.4214 | 5.0157 | ±10.0314 | -0.882 | 0.3780 |  |
| Kidney disease | -11.9200 | 11.6340 | ±23.2680 | -1.025 | 0.3056 |  |
| Circulatory disease | +12.0635 | 8.1743 | ±16.3486 | +1.476 | 0.1400 |  |
| Time < 70 (%) | +1.1459 | 4.5203 | ±9.0405 | +0.254 | 0.7999 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0414** | 20.2281 | ±40.4563 | **+19.579** | **2.35e-85** | *** |
| Education: graduate level (vs college) | +3.7340 | 5.2102 | ±10.4204 | +0.717 | 0.4736 |  |
| Education: high school or below (vs college) | -10.2516 | 9.4372 | ±18.8744 | -1.086 | 0.2773 |  |
| Site: UCSD (vs UAB) | -11.1744 | 6.5168 | ±13.0337 | -1.715 | 0.0864 | . |
| Site: UW (vs UAB) | -2.2730 | 6.2271 | ±12.4543 | -0.365 | 0.7151 |  |
| Age (years) | +0.2657 | 0.2288 | ±0.4577 | +1.161 | 0.2456 |  |
| **BMI (kg/m2)** | **-1.1726** | 0.3814 | ±0.7629 | **-3.074** | **0.0021** | ** |
| **Hypertension** | **-15.6597** | 5.4437 | ±10.8874 | **-2.877** | **0.0040** | ** |
| High cholesterol | -4.4064 | 5.0167 | ±10.0334 | -0.878 | 0.3797 |  |
| Kidney disease | -11.9666 | 11.6396 | ±23.2792 | -1.028 | 0.3039 |  |
| Circulatory disease | +12.0498 | 8.1694 | ±16.3388 | +1.475 | 0.1402 |  |
| Avg. daily time < 70 (%) | -0.0589 | 4.2605 | ±8.5210 | -0.014 | 0.9890 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0690** | 20.1231 | ±40.2462 | **+19.682** | **3.06e-86** | *** |
| Education: graduate level (vs college) | +3.7314 | 5.1776 | ±10.3552 | +0.721 | 0.4711 |  |
| Education: high school or below (vs college) | -10.2637 | 9.4544 | ±18.9087 | -1.086 | 0.2777 |  |
| Site: UCSD (vs UAB) | -11.1465 | 6.4864 | ±12.9728 | -1.718 | 0.0857 | . |
| Site: UW (vs UAB) | -2.2781 | 6.2345 | ±12.4690 | -0.365 | 0.7148 |  |
| Age (years) | +0.2643 | 0.2298 | ±0.4596 | +1.150 | 0.2500 |  |
| **BMI (kg/m2)** | **-1.1752** | 0.3827 | ±0.7654 | **-3.071** | **0.0021** | ** |
| **Hypertension** | **-15.6901** | 5.4584 | ±10.9168 | **-2.874** | **0.0040** | ** |
| High cholesterol | -4.4381 | 5.0453 | ±10.0905 | -0.880 | 0.3790 |  |
| Kidney disease | -12.0629 | 11.7528 | ±23.5057 | -1.026 | 0.3047 |  |
| Circulatory disease | +11.9910 | 8.2519 | ±16.5038 | +1.453 | 0.1462 |  |
| Time 181-250, pooled (%) | +0.0709 | 0.6756 | ±1.3511 | +0.105 | 0.9164 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0201** | 20.1193 | ±40.2386 | **+19.684** | **2.98e-86** | *** |
| Education: graduate level (vs college) | +3.7407 | 5.1774 | ±10.3548 | +0.723 | 0.4700 |  |
| Education: high school or below (vs college) | -10.2463 | 9.4467 | ±18.8935 | -1.085 | 0.2781 |  |
| Site: UCSD (vs UAB) | -11.1859 | 6.4839 | ±12.9678 | -1.725 | 0.0845 | . |
| Site: UW (vs UAB) | -2.2726 | 6.2360 | ±12.4721 | -0.364 | 0.7155 |  |
| Age (years) | +0.2659 | 0.2297 | ±0.4594 | +1.157 | 0.2471 |  |
| **BMI (kg/m2)** | **-1.1719** | 0.3824 | ±0.7647 | **-3.065** | **0.0022** | ** |
| **Hypertension** | **-15.6516** | 5.4640 | ±10.9280 | **-2.865** | **0.0042** | ** |
| High cholesterol | -4.4005 | 5.0425 | ±10.0850 | -0.873 | 0.3828 |  |
| Kidney disease | -11.9431 | 11.7799 | ±23.5597 | -1.014 | 0.3106 |  |
| Circulatory disease | +12.0648 | 8.2678 | ±16.5356 | +1.459 | 0.1445 |  |
| Avg. daily time 181-250 (%) | -0.0145 | 0.6958 | ±1.3916 | -0.021 | 0.9833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0690** | 20.1231 | ±40.2462 | **+19.682** | **3.06e-86** | *** |
| Education: graduate level (vs college) | +3.7314 | 5.1776 | ±10.3552 | +0.721 | 0.4711 |  |
| Education: high school or below (vs college) | -10.2637 | 9.4544 | ±18.9087 | -1.086 | 0.2777 |  |
| Site: UCSD (vs UAB) | -11.1465 | 6.4864 | ±12.9728 | -1.718 | 0.0857 | . |
| Site: UW (vs UAB) | -2.2781 | 6.2345 | ±12.4690 | -0.365 | 0.7148 |  |
| Age (years) | +0.2643 | 0.2298 | ±0.4596 | +1.150 | 0.2500 |  |
| **BMI (kg/m2)** | **-1.1752** | 0.3827 | ±0.7654 | **-3.071** | **0.0021** | ** |
| **Hypertension** | **-15.6901** | 5.4584 | ±10.9168 | **-2.874** | **0.0040** | ** |
| High cholesterol | -4.4381 | 5.0453 | ±10.0905 | -0.880 | 0.3790 |  |
| Kidney disease | -12.0629 | 11.7528 | ±23.5057 | -1.026 | 0.3047 |  |
| Circulatory disease | +11.9910 | 8.2519 | ±16.5038 | +1.453 | 0.1462 |  |
| Time > 180 (%) | +0.0709 | 0.6756 | ±1.3511 | +0.105 | 0.9164 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.37** (p = **1.42e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0201** | 20.1193 | ±40.2386 | **+19.684** | **2.98e-86** | *** |
| Education: graduate level (vs college) | +3.7407 | 5.1774 | ±10.3548 | +0.723 | 0.4700 |  |
| Education: high school or below (vs college) | -10.2463 | 9.4467 | ±18.8935 | -1.085 | 0.2781 |  |
| Site: UCSD (vs UAB) | -11.1859 | 6.4839 | ±12.9678 | -1.725 | 0.0845 | . |
| Site: UW (vs UAB) | -2.2726 | 6.2360 | ±12.4721 | -0.364 | 0.7155 |  |
| Age (years) | +0.2659 | 0.2297 | ±0.4594 | +1.157 | 0.2471 |  |
| **BMI (kg/m2)** | **-1.1719** | 0.3824 | ±0.7647 | **-3.065** | **0.0022** | ** |
| **Hypertension** | **-15.6516** | 5.4640 | ±10.9280 | **-2.865** | **0.0042** | ** |
| High cholesterol | -4.4005 | 5.0425 | ±10.0850 | -0.873 | 0.3828 |  |
| Kidney disease | -11.9431 | 11.7799 | ±23.5597 | -1.014 | 0.3106 |  |
| Circulatory disease | +12.0648 | 8.2678 | ±16.5356 | +1.459 | 0.1445 |  |
| Avg. daily time > 180 (%) | -0.0145 | 0.6958 | ±1.3916 | -0.021 | 0.9833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 779)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **779**, R² = **0.0462**, Adj R² = **0.0325**, F-statistic = **3.38** (p = **1.41e-04**), Residual SE = **68.188** on **767** df, AIC = **8800.9**, BIC = **8856.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.0734** | 20.0872 | ±40.1743 | **+19.718** | **1.52e-86** | *** |
| Education: graduate level (vs college) | +3.7452 | 5.1676 | ±10.3352 | +0.725 | 0.4686 |  |
| Education: high school or below (vs college) | -10.3178 | 9.5389 | ±19.0778 | -1.082 | 0.2794 |  |
| Site: UCSD (vs UAB) | -11.1314 | 6.4692 | ±12.9384 | -1.721 | 0.0853 | . |
| Site: UW (vs UAB) | -2.2637 | 6.2278 | ±12.4556 | -0.363 | 0.7162 |  |
| Age (years) | +0.2662 | 0.2293 | ±0.4586 | +1.161 | 0.2457 |  |
| **BMI (kg/m2)** | **-1.1779** | 0.3807 | ±0.7614 | **-3.094** | **0.0020** | ** |
| **Hypertension** | **-15.6526** | 5.4508 | ±10.9016 | **-2.872** | **0.0041** | ** |
| High cholesterol | -4.4733 | 5.0770 | ±10.1540 | -0.881 | 0.3783 |  |
| Kidney disease | -12.0483 | 11.6687 | ±23.3373 | -1.033 | 0.3018 |  |
| Circulatory disease | +11.9969 | 8.1988 | ±16.3976 | +1.463 | 0.1434 |  |
| Nocturnal time > 180 (%) | +0.0782 | 0.7326 | ±1.4651 | +0.107 | 0.9150 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 775; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **775**, R² = **0.1374**, Adj R² = **0.1261**, F-statistic = **12.17** (p = **1.04e-19**), Residual SE = **17.203** on **764** df, AIC = **6620.1**, BIC = **6671.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2532** | 6.0370 | ±12.0740 | **+8.324** | **8.49e-17** | *** |
| **Education: graduate level (vs college)** | **-5.6311** | 1.3655 | ±2.7309 | **-4.124** | **3.72e-05** | *** |
| Education: high school or below (vs college) | -2.6615 | 2.0967 | ±4.1934 | -1.269 | 0.2043 |  |
| Site: UCSD (vs UAB) | +1.5652 | 1.6593 | ±3.3186 | +0.943 | 0.3455 |  |
| Site: UW (vs UAB) | -1.0669 | 1.5497 | ±3.0994 | -0.688 | 0.4912 |  |
| **Age (years)** | **-0.2791** | 0.0637 | ±0.1273 | **-4.383** | **1.17e-05** | *** |
| **BMI (kg/m2)** | **+0.5939** | 0.1161 | ±0.2322 | **+5.115** | **3.13e-07** | *** |
| Hypertension | +2.3802 | 1.4598 | ±2.9196 | +1.630 | 0.1030 |  |
| High cholesterol | -0.2785 | 1.2984 | ±2.5969 | -0.215 | 0.8301 |  |
| **Kidney disease** | **+6.6916** | 2.4056 | ±4.8113 | **+2.782** | **0.0054** | ** |
| Circulatory disease | -0.2829 | 1.9434 | ±3.8867 | -0.146 | 0.8843 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **775**, R² = **0.1432**, Adj R² = **0.1308**, F-statistic = **11.59** (p = **3.51e-20**), Residual SE = **17.157** on **763** df, AIC = **6617.0**, BIC = **6672.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.1962** | 9.6462 | ±19.2924 | **+3.338** | **8.45e-04** | *** |
| **Education: graduate level (vs college)** | **-5.6165** | 1.3582 | ±2.7164 | **-4.135** | **3.54e-05** | *** |
| Education: high school or below (vs college) | -2.8226 | 2.1103 | ±4.2205 | -1.338 | 0.1810 |  |
| Site: UCSD (vs UAB) | +1.6355 | 1.6450 | ±3.2901 | +0.994 | 0.3201 |  |
| Site: UW (vs UAB) | -0.9980 | 1.5427 | ±3.0855 | -0.647 | 0.5177 |  |
| **Age (years)** | **-0.2865** | 0.0630 | ±0.1260 | **-4.546** | **5.47e-06** | *** |
| **BMI (kg/m2)** | **+0.5560** | 0.1146 | ±0.2291 | **+4.854** | **1.21e-06** | *** |
| Hypertension | +1.9594 | 1.4704 | ±2.9409 | +1.333 | 0.1827 |  |
| High cholesterol | -0.7793 | 1.3059 | ±2.6117 | -0.597 | 0.5506 |  |
| **Kidney disease** | **+6.8492** | 2.3760 | ±4.7520 | **+2.883** | **0.0039** | ** |
| Circulatory disease | -0.5654 | 1.9129 | ±3.8258 | -0.296 | 0.7676 |  |
| **HbA1c (%)** | **+3.5328** | 1.6108 | ±3.2216 | **+2.193** | **0.0283** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **775**, R² = **0.1472**, Adj R² = **0.1349**, F-statistic = **11.97** (p = **6.54e-21**), Residual SE = **17.116** on **763** df, AIC = **6613.3**, BIC = **6669.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.1435** | 8.0090 | ±16.0179 | **+4.138** | **3.50e-05** | *** |
| **Education: graduate level (vs college)** | **-5.6966** | 1.3529 | ±2.7058 | **-4.211** | **2.55e-05** | *** |
| Education: high school or below (vs college) | -2.5993 | 2.1075 | ±4.2149 | -1.233 | 0.2174 |  |
| Site: UCSD (vs UAB) | +1.7294 | 1.6505 | ±3.3009 | +1.048 | 0.2947 |  |
| Site: UW (vs UAB) | -1.2427 | 1.5456 | ±3.0913 | -0.804 | 0.4214 |  |
| **Age (years)** | **-0.2824** | 0.0629 | ±0.1259 | **-4.488** | **7.18e-06** | *** |
| **BMI (kg/m2)** | **+0.5593** | 0.1135 | ±0.2270 | **+4.927** | **8.35e-07** | *** |
| Hypertension | +1.9780 | 1.4603 | ±2.9205 | +1.355 | 0.1756 |  |
| High cholesterol | -0.4457 | 1.2935 | ±2.5870 | -0.345 | 0.7304 |  |
| **Kidney disease** | **+6.2431** | 2.3915 | ±4.7830 | **+2.611** | **0.0090** | ** |
| Circulatory disease | -0.6646 | 1.9148 | ±3.8295 | -0.347 | 0.7285 |  |
| **Mean glucose (mg/dL)** | **+0.1550** | 0.0523 | ±0.1045 | **+2.965** | **0.0030** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **775**, R² = **0.1472**, Adj R² = **0.1349**, F-statistic = **11.97** (p = **6.54e-21**), Residual SE = **17.116** on **763** df, AIC = **6613.3**, BIC = **6669.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +11.7008 | 13.9751 | ±27.9502 | +0.837 | 0.4024 |  |
| **Education: graduate level (vs college)** | **-5.6966** | 1.3529 | ±2.7058 | **-4.211** | **2.55e-05** | *** |
| Education: high school or below (vs college) | -2.5993 | 2.1075 | ±4.2149 | -1.233 | 0.2174 |  |
| Site: UCSD (vs UAB) | +1.7294 | 1.6505 | ±3.3009 | +1.048 | 0.2947 |  |
| Site: UW (vs UAB) | -1.2427 | 1.5456 | ±3.0913 | -0.804 | 0.4214 |  |
| **Age (years)** | **-0.2824** | 0.0629 | ±0.1259 | **-4.488** | **7.18e-06** | *** |
| **BMI (kg/m2)** | **+0.5593** | 0.1135 | ±0.2270 | **+4.927** | **8.35e-07** | *** |
| Hypertension | +1.9780 | 1.4603 | ±2.9205 | +1.355 | 0.1756 |  |
| High cholesterol | -0.4457 | 1.2935 | ±2.5870 | -0.345 | 0.7304 |  |
| **Kidney disease** | **+6.2431** | 2.3915 | ±4.7830 | **+2.611** | **0.0090** | ** |
| Circulatory disease | -0.6646 | 1.9148 | ±3.8295 | -0.347 | 0.7285 |  |
| **GMI (%)** | **+6.4781** | 2.1852 | ±4.3705 | **+2.965** | **0.0030** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **775**, R² = **0.1477**, Adj R² = **0.1354**, F-statistic = **12.02** (p = **5.24e-21**), Residual SE = **17.111** on **763** df, AIC = **6612.8**, BIC = **6668.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+34.6728** | 7.3074 | ±14.6147 | **+4.745** | **2.09e-06** | *** |
| **Education: graduate level (vs college)** | **-5.6666** | 1.3522 | ±2.7045 | **-4.190** | **2.78e-05** | *** |
| Education: high school or below (vs college) | -2.6984 | 2.1167 | ±4.2334 | -1.275 | 0.2024 |  |
| Site: UCSD (vs UAB) | +1.5486 | 1.6516 | ±3.3032 | +0.938 | 0.3484 |  |
| Site: UW (vs UAB) | -1.3009 | 1.5460 | ±3.0921 | -0.841 | 0.4001 |  |
| **Age (years)** | **-0.2685** | 0.0628 | ±0.1255 | **-4.279** | **1.88e-05** | *** |
| **BMI (kg/m2)** | **+0.5367** | 0.1127 | ±0.2255 | **+4.761** | **1.93e-06** | *** |
| Hypertension | +2.0705 | 1.4571 | ±2.9141 | +1.421 | 0.1553 |  |
| High cholesterol | -0.5597 | 1.2936 | ±2.5872 | -0.433 | 0.6653 |  |
| **Kidney disease** | **+6.5726** | 2.3684 | ±4.7368 | **+2.775** | **0.0055** | ** |
| Circulatory disease | -0.6174 | 1.9057 | ±3.8114 | -0.324 | 0.7460 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **+0.1415** | 0.0463 | ±0.0926 | **+3.055** | **0.0022** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **775**, R² = **0.1415**, Adj R² = **0.1291**, F-statistic = **11.43** (p = **7.03e-20**), Residual SE = **17.173** on **763** df, AIC = **6618.5**, BIC = **6674.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.2703** | 6.3919 | ±12.7839 | **+7.082** | **1.42e-12** | *** |
| **Education: graduate level (vs college)** | **-5.5382** | 1.3632 | ±2.7263 | **-4.063** | **4.85e-05** | *** |
| Education: high school or below (vs college) | -2.8608 | 2.0900 | ±4.1800 | -1.369 | 0.1711 |  |
| Site: UCSD (vs UAB) | +1.7834 | 1.6549 | ±3.3099 | +1.078 | 0.2812 |  |
| Site: UW (vs UAB) | -1.0565 | 1.5476 | ±3.0951 | -0.683 | 0.4948 |  |
| **Age (years)** | **-0.2858** | 0.0639 | ±0.1278 | **-4.472** | **7.74e-06** | *** |
| **BMI (kg/m2)** | **+0.5850** | 0.1146 | ±0.2292 | **+5.104** | **3.32e-07** | *** |
| Hypertension | +2.0332 | 1.4695 | ±2.9389 | +1.384 | 0.1665 |  |
| High cholesterol | -0.3611 | 1.2962 | ±2.5923 | -0.279 | 0.7806 |  |
| **Kidney disease** | **+6.3739** | 2.3962 | ±4.7925 | **+2.660** | **0.0078** | ** |
| Circulatory disease | -0.4342 | 1.9195 | ±3.8390 | -0.226 | 0.8210 |  |
| Glucose SD, pooled (mg/dL) | +0.2917 | 0.1561 | ±0.3122 | +1.868 | 0.0617 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **775**, R² = **0.1407**, Adj R² = **0.1283**, F-statistic = **11.36** (p = **9.60e-20**), Residual SE = **17.181** on **763** df, AIC = **6619.2**, BIC = **6675.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.1347** | 6.3078 | ±12.6156 | **+7.314** | **2.59e-13** | *** |
| **Education: graduate level (vs college)** | **-5.5740** | 1.3629 | ±2.7257 | **-4.090** | **4.32e-05** | *** |
| Education: high school or below (vs college) | -2.8057 | 2.0882 | ±4.1765 | -1.344 | 0.1791 |  |
| Site: UCSD (vs UAB) | +1.7534 | 1.6556 | ±3.3113 | +1.059 | 0.2896 |  |
| Site: UW (vs UAB) | -1.0870 | 1.5496 | ±3.0992 | -0.701 | 0.4830 |  |
| **Age (years)** | **-0.2856** | 0.0640 | ±0.1279 | **-4.464** | **8.04e-06** | *** |
| **BMI (kg/m2)** | **+0.5851** | 0.1147 | ±0.2294 | **+5.102** | **3.36e-07** | *** |
| Hypertension | +2.0645 | 1.4705 | ±2.9410 | +1.404 | 0.1603 |  |
| High cholesterol | -0.3334 | 1.2974 | ±2.5948 | -0.257 | 0.7972 |  |
| **Kidney disease** | **+6.4459** | 2.4030 | ±4.8060 | **+2.682** | **0.0073** | ** |
| Circulatory disease | -0.3935 | 1.9232 | ±3.8464 | -0.205 | 0.8379 |  |
| Avg. daily SD (mg/dL) | +0.2691 | 0.1608 | ±0.3215 | +1.674 | 0.0942 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **775**, R² = **0.1377**, Adj R² = **0.1253**, F-statistic = **11.08** (p = **3.27e-19**), Residual SE = **17.211** on **763** df, AIC = **6621.8**, BIC = **6677.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4038** | 6.8371 | ±13.6742 | **+7.080** | **1.45e-12** | *** |
| **Education: graduate level (vs college)** | **-5.5888** | 1.3719 | ±2.7438 | **-4.074** | **4.63e-05** | *** |
| Education: high school or below (vs college) | -2.7337 | 2.1013 | ±4.2026 | -1.301 | 0.1933 |  |
| Site: UCSD (vs UAB) | +1.6237 | 1.6596 | ±3.3192 | +0.978 | 0.3279 |  |
| Site: UW (vs UAB) | -1.0464 | 1.5527 | ±3.1055 | -0.674 | 0.5004 |  |
| **Age (years)** | **-0.2810** | 0.0641 | ±0.1282 | **-4.383** | **1.17e-05** | *** |
| **BMI (kg/m2)** | **+0.5946** | 0.1161 | ±0.2322 | **+5.122** | **3.02e-07** | *** |
| Hypertension | +2.3035 | 1.4664 | ±2.9329 | +1.571 | 0.1162 |  |
| High cholesterol | -0.2841 | 1.2996 | ±2.5992 | -0.219 | 0.8270 |  |
| **Kidney disease** | **+6.6298** | 2.4143 | ±4.8285 | **+2.746** | **0.0060** | ** |
| Circulatory disease | -0.2887 | 1.9406 | ±3.8813 | -0.149 | 0.8818 |  |
| CV (%) | +0.1184 | 0.2181 | ±0.4361 | +0.543 | 0.5870 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **775**, R² = **0.1380**, Adj R² = **0.1255**, F-statistic = **11.10** (p = **2.99e-19**), Residual SE = **17.209** on **763** df, AIC = **6621.6**, BIC = **6677.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.7695** | 7.0506 | ±14.1013 | **+7.484** | **7.19e-14** | *** |
| **Education: graduate level (vs college)** | **-5.5673** | 1.3716 | ±2.7432 | **-4.059** | **4.93e-05** | *** |
| Education: high school or below (vs college) | -2.7446 | 2.0982 | ±4.1963 | -1.308 | 0.1908 |  |
| Site: UCSD (vs UAB) | +1.6252 | 1.6592 | ±3.3184 | +0.980 | 0.3273 |  |
| Site: UW (vs UAB) | -1.0589 | 1.5515 | ±3.1030 | -0.682 | 0.4949 |  |
| **Age (years)** | **-0.2813** | 0.0640 | ±0.1280 | **-4.395** | **1.11e-05** | *** |
| **BMI (kg/m2)** | **+0.5943** | 0.1160 | ±0.2320 | **+5.124** | **2.99e-07** | *** |
| Hypertension | +2.2870 | 1.4663 | ±2.9327 | +1.560 | 0.1188 |  |
| High cholesterol | -0.2820 | 1.2996 | ±2.5991 | -0.217 | 0.8282 |  |
| **Kidney disease** | **+6.6134** | 2.4123 | ±4.8247 | **+2.742** | **0.0061** | ** |
| Circulatory disease | -0.2773 | 1.9410 | ±3.8819 | -0.143 | 0.8864 |  |
| Mean / SD ratio | -0.3799 | 0.5345 | ±1.0689 | -0.711 | 0.4772 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **775**, R² = **0.1379**, Adj R² = **0.1254**, F-statistic = **11.09** (p = **3.12e-19**), Residual SE = **17.210** on **763** df, AIC = **6621.7**, BIC = **6677.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.3882** | 6.9730 | ±13.9460 | **+7.513** | **5.78e-14** | *** |
| **Education: graduate level (vs college)** | **-5.5854** | 1.3698 | ±2.7397 | **-4.077** | **4.55e-05** | *** |
| Education: high school or below (vs college) | -2.7241 | 2.0966 | ±4.1933 | -1.299 | 0.1939 |  |
| Site: UCSD (vs UAB) | +1.6128 | 1.6593 | ±3.3187 | +0.972 | 0.3311 |  |
| Site: UW (vs UAB) | -1.0727 | 1.5519 | ±3.1039 | -0.691 | 0.4894 |  |
| **Age (years)** | **-0.2815** | 0.0641 | ±0.1282 | **-4.392** | **1.12e-05** | *** |
| **BMI (kg/m2)** | **+0.5931** | 0.1159 | ±0.2318 | **+5.117** | **3.10e-07** | *** |
| Hypertension | +2.3065 | 1.4638 | ±2.9277 | +1.576 | 0.1151 |  |
| High cholesterol | -0.2774 | 1.3000 | ±2.6000 | -0.213 | 0.8310 |  |
| **Kidney disease** | **+6.6265** | 2.4146 | ±4.8292 | **+2.744** | **0.0061** | ** |
| Circulatory disease | -0.2634 | 1.9447 | ±3.8894 | -0.135 | 0.8923 |  |
| Avg. daily mean/SD | -0.2752 | 0.4258 | ±0.8516 | -0.646 | 0.5180 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **775**, R² = **0.1406**, Adj R² = **0.1282**, F-statistic = **11.34** (p = **1.03e-19**), Residual SE = **17.183** on **763** df, AIC = **6619.3**, BIC = **6675.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.6573** | 6.6734 | ±13.3468 | **+6.692** | **2.20e-11** | *** |
| **Education: graduate level (vs college)** | **-5.6121** | 1.3611 | ±2.7222 | **-4.123** | **3.74e-05** | *** |
| Education: high school or below (vs college) | -2.9483 | 2.1173 | ±4.2347 | -1.392 | 0.1638 |  |
| Site: UCSD (vs UAB) | +1.6353 | 1.6583 | ±3.3166 | +0.986 | 0.3241 |  |
| Site: UW (vs UAB) | -1.0328 | 1.5468 | ±3.0936 | -0.668 | 0.5043 |  |
| **Age (years)** | **-0.2780** | 0.0635 | ±0.1271 | **-4.375** | **1.21e-05** | *** |
| **BMI (kg/m2)** | **+0.5921** | 0.1141 | ±0.2282 | **+5.190** | **2.11e-07** | *** |
| Hypertension | +2.4497 | 1.4626 | ±2.9251 | +1.675 | 0.0939 | . |
| High cholesterol | -0.3053 | 1.2982 | ±2.5964 | -0.235 | 0.8141 |  |
| **Kidney disease** | **+6.5422** | 2.4104 | ±4.8207 | **+2.714** | **0.0066** | ** |
| Circulatory disease | -0.1988 | 1.9368 | ±3.8737 | -0.103 | 0.9183 |  |
| MAG (mg/dL/h) | +0.1543 | 0.0971 | ±0.1943 | +1.588 | 0.1123 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **775**, R² = **0.1408**, Adj R² = **0.1284**, F-statistic = **11.36** (p = **9.50e-20**), Residual SE = **17.181** on **763** df, AIC = **6619.1**, BIC = **6675.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.7791** | 6.7752 | ±13.5503 | **+6.609** | **3.86e-11** | *** |
| **Education: graduate level (vs college)** | **-5.6062** | 1.3622 | ±2.7243 | **-4.116** | **3.86e-05** | *** |
| Education: high school or below (vs college) | -2.8679 | 2.0938 | ±4.1876 | -1.370 | 0.1708 |  |
| Site: UCSD (vs UAB) | +1.7096 | 1.6606 | ±3.3213 | +1.029 | 0.3032 |  |
| Site: UW (vs UAB) | -1.0922 | 1.5482 | ±3.0965 | -0.705 | 0.4805 |  |
| **Age (years)** | **-0.2850** | 0.0640 | ±0.1279 | **-4.456** | **8.35e-06** | *** |
| **BMI (kg/m2)** | **+0.5986** | 0.1161 | ±0.2321 | **+5.158** | **2.50e-07** | *** |
| Hypertension | +2.1820 | 1.4650 | ±2.9300 | +1.489 | 0.1364 |  |
| High cholesterol | -0.2985 | 1.2977 | ±2.5955 | -0.230 | 0.8181 |  |
| **Kidney disease** | **+6.4685** | 2.4044 | ±4.8089 | **+2.690** | **0.0071** | ** |
| Circulatory disease | -0.3938 | 1.9242 | ±3.8483 | -0.205 | 0.8378 |  |
| Avg. daily range (mg/dL) | +0.0637 | 0.0379 | ±0.0758 | +1.681 | 0.0928 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **775**, R² = **0.1419**, Adj R² = **0.1296**, F-statistic = **11.47** (p = **5.81e-20**), Residual SE = **17.169** on **763** df, AIC = **6618.1**, BIC = **6673.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5806** | 6.0271 | ±12.0541 | **+7.894** | **2.91e-15** | *** |
| **Education: graduate level (vs college)** | **-5.6348** | 1.3597 | ±2.7194 | **-4.144** | **3.41e-05** | *** |
| Education: high school or below (vs college) | -2.9144 | 2.1062 | ±4.2124 | -1.384 | 0.1664 |  |
| Site: UCSD (vs UAB) | +1.7605 | 1.6528 | ±3.3055 | +1.065 | 0.2868 |  |
| Site: UW (vs UAB) | -0.9605 | 1.5417 | ±3.0835 | -0.623 | 0.5333 |  |
| **Age (years)** | **-0.2780** | 0.0633 | ±0.1267 | **-4.390** | **1.14e-05** | *** |
| **BMI (kg/m2)** | **+0.5758** | 0.1145 | ±0.2291 | **+5.027** | **4.99e-07** | *** |
| Hypertension | +2.3394 | 1.4521 | ±2.9042 | +1.611 | 0.1072 |  |
| High cholesterol | -0.4854 | 1.2985 | ±2.5970 | -0.374 | 0.7085 |  |
| **Kidney disease** | **+6.4408** | 2.3643 | ±4.7286 | **+2.724** | **0.0064** | ** |
| Circulatory disease | -0.5393 | 1.9327 | ±3.8654 | -0.279 | 0.7802 |  |
| **SD of daily means (mg/dL)** | **+0.5397** | 0.2682 | ±0.5365 | **+2.012** | **0.0442** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **775**, R² = **0.1378**, Adj R² = **0.1253**, F-statistic = **11.08** (p = **3.24e-19**), Residual SE = **17.210** on **763** df, AIC = **6621.8**, BIC = **6677.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.8602** | 18.0054 | ±36.0108 | **+3.380** | **7.25e-04** | *** |
| **Education: graduate level (vs college)** | **-5.6357** | 1.3644 | ±2.7288 | **-4.131** | **3.62e-05** | *** |
| Education: high school or below (vs college) | -2.6707 | 2.1038 | ±4.2076 | -1.269 | 0.2043 |  |
| Site: UCSD (vs UAB) | +1.6037 | 1.6608 | ±3.3217 | +0.966 | 0.3342 |  |
| Site: UW (vs UAB) | -1.0722 | 1.5508 | ±3.1017 | -0.691 | 0.4893 |  |
| **Age (years)** | **-0.2807** | 0.0639 | ±0.1278 | **-4.391** | **1.13e-05** | *** |
| **BMI (kg/m2)** | **+0.5903** | 0.1163 | ±0.2326 | **+5.076** | **3.85e-07** | *** |
| Hypertension | +2.3338 | 1.4635 | ±2.9271 | +1.595 | 0.1108 |  |
| High cholesterol | -0.3271 | 1.2994 | ±2.5987 | -0.252 | 0.8013 |  |
| **Kidney disease** | **+6.5931** | 2.4203 | ±4.8406 | **+2.724** | **0.0064** | ** |
| Circulatory disease | -0.3831 | 1.9419 | ±3.8838 | -0.197 | 0.8436 |  |
| Time in range 70-180, pooled (%) | -0.1060 | 0.1648 | ±0.3296 | -0.643 | 0.5199 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **775**, R² = **0.1377**, Adj R² = **0.1253**, F-statistic = **11.08** (p = **3.28e-19**), Residual SE = **17.211** on **763** df, AIC = **6621.8**, BIC = **6677.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.5881** | 18.2116 | ±36.4232 | **+3.327** | **8.78e-04** | *** |
| **Education: graduate level (vs college)** | **-5.6339** | 1.3645 | ±2.7291 | **-4.129** | **3.65e-05** | *** |
| Education: high school or below (vs college) | -2.6584 | 2.1046 | ±4.2091 | -1.263 | 0.2065 |  |
| Site: UCSD (vs UAB) | +1.6044 | 1.6606 | ±3.3211 | +0.966 | 0.3339 |  |
| Site: UW (vs UAB) | -1.0722 | 1.5510 | ±3.1020 | -0.691 | 0.4894 |  |
| **Age (years)** | **-0.2806** | 0.0639 | ±0.1278 | **-4.390** | **1.13e-05** | *** |
| **BMI (kg/m2)** | **+0.5902** | 0.1163 | ±0.2327 | **+5.073** | **3.92e-07** | *** |
| Hypertension | +2.3345 | 1.4633 | ±2.9266 | +1.595 | 0.1106 |  |
| High cholesterol | -0.3250 | 1.2992 | ±2.5984 | -0.250 | 0.8025 |  |
| **Kidney disease** | **+6.5942** | 2.4216 | ±4.8431 | **+2.723** | **0.0065** | ** |
| Circulatory disease | -0.3844 | 1.9419 | ±3.8838 | -0.198 | 0.8431 |  |
| Avg. daily time in range 70-180 (%) | -0.1032 | 0.1664 | ±0.3328 | -0.620 | 0.5351 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **775**, R² = **0.1450**, Adj R² = **0.1327**, F-statistic = **11.77** (p = **1.61e-20**), Residual SE = **17.138** on **763** df, AIC = **6615.3**, BIC = **6671.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.1894** | 6.0308 | ±12.0616 | **+8.488** | **2.10e-17** | *** |
| **Education: graduate level (vs college)** | **-5.9133** | 1.3693 | ±2.7386 | **-4.318** | **1.57e-05** | *** |
| Education: high school or below (vs college) | -2.8874 | 2.0949 | ±4.1897 | -1.378 | 0.1681 |  |
| Site: UCSD (vs UAB) | +1.7784 | 1.6504 | ±3.3007 | +1.078 | 0.2812 |  |
| Site: UW (vs UAB) | -1.0851 | 1.5457 | ±3.0913 | -0.702 | 0.4827 |  |
| **Age (years)** | **-0.2792** | 0.0634 | ±0.1268 | **-4.404** | **1.06e-05** | *** |
| **BMI (kg/m2)** | **+0.5872** | 0.1163 | ±0.2325 | **+5.051** | **4.39e-07** | *** |
| Hypertension | +2.3518 | 1.4545 | ±2.9090 | +1.617 | 0.1059 |  |
| High cholesterol | -0.2136 | 1.2986 | ±2.5973 | -0.165 | 0.8693 |  |
| **Kidney disease** | **+6.5041** | 2.4058 | ±4.8116 | **+2.704** | **0.0069** | ** |
| Circulatory disease | -0.3224 | 1.9383 | ±3.8766 | -0.166 | 0.8679 |  |
| **Time 54-69, pooled (%)** | **-3.2322** | 1.5095 | ±3.0190 | **-2.141** | **0.0323** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **775**, R² = **0.1450**, Adj R² = **0.1326**, F-statistic = **11.76** (p = **1.66e-20**), Residual SE = **17.139** on **763** df, AIC = **6615.3**, BIC = **6671.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0482** | 6.0261 | ±12.0523 | **+8.471** | **2.43e-17** | *** |
| **Education: graduate level (vs college)** | **-5.9277** | 1.3706 | ±2.7412 | **-4.325** | **1.53e-05** | *** |
| Education: high school or below (vs college) | -2.9230 | 2.0950 | ±4.1901 | -1.395 | 0.1630 |  |
| Site: UCSD (vs UAB) | +1.8529 | 1.6500 | ±3.2999 | +1.123 | 0.2614 |  |
| Site: UW (vs UAB) | -1.0579 | 1.5457 | ±3.0914 | -0.684 | 0.4937 |  |
| **Age (years)** | **-0.2781** | 0.0634 | ±0.1268 | **-4.389** | **1.14e-05** | *** |
| **BMI (kg/m2)** | **+0.5875** | 0.1164 | ±0.2327 | **+5.048** | **4.46e-07** | *** |
| Hypertension | +2.3496 | 1.4549 | ±2.9098 | +1.615 | 0.1063 |  |
| High cholesterol | -0.2240 | 1.2986 | ±2.5972 | -0.172 | 0.8631 |  |
| **Kidney disease** | **+6.4848** | 2.4047 | ±4.8095 | **+2.697** | **0.0070** | ** |
| Circulatory disease | -0.3680 | 1.9378 | ±3.8756 | -0.190 | 0.8494 |  |
| **Avg. daily time 54-69 (%)** | **-3.1232** | 1.5891 | ±3.1781 | **-1.965** | **0.0494** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **775**, R² = **0.1450**, Adj R² = **0.1327**, F-statistic = **11.77** (p = **1.61e-20**), Residual SE = **17.138** on **763** df, AIC = **6615.3**, BIC = **6671.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.1894** | 6.0308 | ±12.0616 | **+8.488** | **2.10e-17** | *** |
| **Education: graduate level (vs college)** | **-5.9133** | 1.3693 | ±2.7386 | **-4.318** | **1.57e-05** | *** |
| Education: high school or below (vs college) | -2.8874 | 2.0949 | ±4.1897 | -1.378 | 0.1681 |  |
| Site: UCSD (vs UAB) | +1.7784 | 1.6504 | ±3.3007 | +1.078 | 0.2812 |  |
| Site: UW (vs UAB) | -1.0851 | 1.5457 | ±3.0913 | -0.702 | 0.4827 |  |
| **Age (years)** | **-0.2792** | 0.0634 | ±0.1268 | **-4.404** | **1.06e-05** | *** |
| **BMI (kg/m2)** | **+0.5872** | 0.1163 | ±0.2325 | **+5.051** | **4.39e-07** | *** |
| Hypertension | +2.3518 | 1.4545 | ±2.9090 | +1.617 | 0.1059 |  |
| High cholesterol | -0.2136 | 1.2986 | ±2.5973 | -0.165 | 0.8693 |  |
| **Kidney disease** | **+6.5041** | 2.4058 | ±4.8116 | **+2.704** | **0.0069** | ** |
| Circulatory disease | -0.3224 | 1.9383 | ±3.8766 | -0.166 | 0.8679 |  |
| **Time < 70 (%)** | **-3.2322** | 1.5095 | ±3.0190 | **-2.141** | **0.0323** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **775**, R² = **0.1450**, Adj R² = **0.1326**, F-statistic = **11.76** (p = **1.66e-20**), Residual SE = **17.139** on **763** df, AIC = **6615.3**, BIC = **6671.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0482** | 6.0261 | ±12.0523 | **+8.471** | **2.43e-17** | *** |
| **Education: graduate level (vs college)** | **-5.9277** | 1.3706 | ±2.7412 | **-4.325** | **1.53e-05** | *** |
| Education: high school or below (vs college) | -2.9230 | 2.0950 | ±4.1901 | -1.395 | 0.1630 |  |
| Site: UCSD (vs UAB) | +1.8529 | 1.6500 | ±3.2999 | +1.123 | 0.2614 |  |
| Site: UW (vs UAB) | -1.0579 | 1.5457 | ±3.0914 | -0.684 | 0.4937 |  |
| **Age (years)** | **-0.2781** | 0.0634 | ±0.1268 | **-4.389** | **1.14e-05** | *** |
| **BMI (kg/m2)** | **+0.5875** | 0.1164 | ±0.2327 | **+5.048** | **4.46e-07** | *** |
| Hypertension | +2.3496 | 1.4549 | ±2.9098 | +1.615 | 0.1063 |  |
| High cholesterol | -0.2240 | 1.2986 | ±2.5972 | -0.172 | 0.8631 |  |
| **Kidney disease** | **+6.4848** | 2.4047 | ±4.8095 | **+2.697** | **0.0070** | ** |
| Circulatory disease | -0.3680 | 1.9378 | ±3.8756 | -0.190 | 0.8494 |  |
| **Avg. daily time < 70 (%)** | **-3.1232** | 1.5891 | ±3.1781 | **-1.965** | **0.0494** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **775**, R² = **0.1384**, Adj R² = **0.1260**, F-statistic = **11.14** (p = **2.47e-19**), Residual SE = **17.204** on **763** df, AIC = **6621.2**, BIC = **6677.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3099** | 6.0175 | ±12.0351 | **+8.361** | **6.24e-17** | *** |
| **Education: graduate level (vs college)** | **-5.6540** | 1.3622 | ±2.7245 | **-4.150** | **3.32e-05** | *** |
| Education: high school or below (vs college) | -2.6890 | 2.1051 | ±4.2103 | -1.277 | 0.2015 |  |
| Site: UCSD (vs UAB) | +1.6404 | 1.6605 | ±3.3210 | +0.988 | 0.3232 |  |
| Site: UW (vs UAB) | -1.0766 | 1.5504 | ±3.1007 | -0.694 | 0.4874 |  |
| **Age (years)** | **-0.2817** | 0.0638 | ±0.1277 | **-4.413** | **1.02e-05** | *** |
| **BMI (kg/m2)** | **+0.5876** | 0.1160 | ±0.2320 | **+5.065** | **4.08e-07** | *** |
| Hypertension | +2.3020 | 1.4656 | ±2.9312 | +1.571 | 0.1163 |  |
| High cholesterol | -0.3552 | 1.2987 | ±2.5975 | -0.274 | 0.7844 |  |
| **Kidney disease** | **+6.5187** | 2.4153 | ±4.8307 | **+2.699** | **0.0070** | ** |
| Circulatory disease | -0.4507 | 1.9389 | ±3.8779 | -0.232 | 0.8162 |  |
| Time 181-250, pooled (%) | +0.1752 | 0.1685 | ±0.3370 | +1.040 | 0.2984 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **775**, R² = **0.1384**, Adj R² = **0.1260**, F-statistic = **11.14** (p = **2.49e-19**), Residual SE = **17.204** on **763** df, AIC = **6621.2**, BIC = **6677.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3231** | 6.0145 | ±12.0290 | **+8.367** | **5.91e-17** | *** |
| **Education: graduate level (vs college)** | **-5.6527** | 1.3621 | ±2.7243 | **-4.150** | **3.33e-05** | *** |
| Education: high school or below (vs college) | -2.6711 | 2.1057 | ±4.2114 | -1.268 | 0.2046 |  |
| Site: UCSD (vs UAB) | +1.6491 | 1.6600 | ±3.3200 | +0.993 | 0.3205 |  |
| Site: UW (vs UAB) | -1.0756 | 1.5504 | ±3.1009 | -0.694 | 0.4879 |  |
| **Age (years)** | **-0.2816** | 0.0638 | ±0.1276 | **-4.412** | **1.03e-05** | *** |
| **BMI (kg/m2)** | **+0.5872** | 0.1160 | ±0.2319 | **+5.063** | **4.13e-07** | *** |
| Hypertension | +2.2997 | 1.4656 | ±2.9312 | +1.569 | 0.1166 |  |
| High cholesterol | -0.3555 | 1.2987 | ±2.5974 | -0.274 | 0.7843 |  |
| **Kidney disease** | **+6.5120** | 2.4165 | ±4.8330 | **+2.695** | **0.0070** | ** |
| Circulatory disease | -0.4627 | 1.9383 | ±3.8766 | -0.239 | 0.8113 |  |
| Avg. daily time 181-250 (%) | +0.1778 | 0.1690 | ±0.3380 | +1.052 | 0.2927 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **775**, R² = **0.1384**, Adj R² = **0.1260**, F-statistic = **11.14** (p = **2.47e-19**), Residual SE = **17.204** on **763** df, AIC = **6621.2**, BIC = **6677.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3099** | 6.0175 | ±12.0351 | **+8.361** | **6.24e-17** | *** |
| **Education: graduate level (vs college)** | **-5.6540** | 1.3622 | ±2.7245 | **-4.150** | **3.32e-05** | *** |
| Education: high school or below (vs college) | -2.6890 | 2.1051 | ±4.2103 | -1.277 | 0.2015 |  |
| Site: UCSD (vs UAB) | +1.6404 | 1.6605 | ±3.3210 | +0.988 | 0.3232 |  |
| Site: UW (vs UAB) | -1.0766 | 1.5504 | ±3.1007 | -0.694 | 0.4874 |  |
| **Age (years)** | **-0.2817** | 0.0638 | ±0.1277 | **-4.413** | **1.02e-05** | *** |
| **BMI (kg/m2)** | **+0.5876** | 0.1160 | ±0.2320 | **+5.065** | **4.08e-07** | *** |
| Hypertension | +2.3020 | 1.4656 | ±2.9312 | +1.571 | 0.1163 |  |
| High cholesterol | -0.3552 | 1.2987 | ±2.5975 | -0.274 | 0.7844 |  |
| **Kidney disease** | **+6.5187** | 2.4153 | ±4.8307 | **+2.699** | **0.0070** | ** |
| Circulatory disease | -0.4507 | 1.9389 | ±3.8779 | -0.232 | 0.8162 |  |
| Time > 180 (%) | +0.1752 | 0.1685 | ±0.3370 | +1.040 | 0.2984 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **775**, R² = **0.1384**, Adj R² = **0.1260**, F-statistic = **11.14** (p = **2.49e-19**), Residual SE = **17.204** on **763** df, AIC = **6621.2**, BIC = **6677.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3231** | 6.0145 | ±12.0290 | **+8.367** | **5.91e-17** | *** |
| **Education: graduate level (vs college)** | **-5.6527** | 1.3621 | ±2.7243 | **-4.150** | **3.33e-05** | *** |
| Education: high school or below (vs college) | -2.6711 | 2.1057 | ±4.2114 | -1.268 | 0.2046 |  |
| Site: UCSD (vs UAB) | +1.6491 | 1.6600 | ±3.3200 | +0.993 | 0.3205 |  |
| Site: UW (vs UAB) | -1.0756 | 1.5504 | ±3.1009 | -0.694 | 0.4879 |  |
| **Age (years)** | **-0.2816** | 0.0638 | ±0.1276 | **-4.412** | **1.03e-05** | *** |
| **BMI (kg/m2)** | **+0.5872** | 0.1160 | ±0.2319 | **+5.063** | **4.13e-07** | *** |
| Hypertension | +2.2997 | 1.4656 | ±2.9312 | +1.569 | 0.1166 |  |
| High cholesterol | -0.3555 | 1.2987 | ±2.5974 | -0.274 | 0.7843 |  |
| **Kidney disease** | **+6.5120** | 2.4165 | ±4.8330 | **+2.695** | **0.0070** | ** |
| Circulatory disease | -0.4627 | 1.9383 | ±3.8766 | -0.239 | 0.8113 |  |
| Avg. daily time > 180 (%) | +0.1778 | 0.1690 | ±0.3380 | +1.052 | 0.2927 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 775)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **775**, R² = **0.1382**, Adj R² = **0.1257**, F-statistic = **11.12** (p = **2.77e-19**), Residual SE = **17.207** on **763** df, AIC = **6621.5**, BIC = **6677.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3416** | 6.0284 | ±12.0568 | **+8.351** | **6.78e-17** | *** |
| **Education: graduate level (vs college)** | **-5.6188** | 1.3636 | ±2.7272 | **-4.121** | **3.78e-05** | *** |
| Education: high school or below (vs college) | -2.7704 | 2.1043 | ±4.2087 | -1.317 | 0.1880 |  |
| Site: UCSD (vs UAB) | +1.6381 | 1.6598 | ±3.3196 | +0.987 | 0.3237 |  |
| Site: UW (vs UAB) | -1.0587 | 1.5485 | ±3.0969 | -0.684 | 0.4942 |  |
| **Age (years)** | **-0.2778** | 0.0637 | ±0.1273 | **-4.365** | **1.27e-05** | *** |
| **BMI (kg/m2)** | **+0.5838** | 0.1172 | ±0.2344 | **+4.982** | **6.28e-07** | *** |
| Hypertension | +2.3869 | 1.4630 | ±2.9259 | +1.632 | 0.1028 |  |
| High cholesterol | -0.3880 | 1.3042 | ±2.6085 | -0.297 | 0.7661 |  |
| **Kidney disease** | **+6.5776** | 2.4038 | ±4.8076 | **+2.736** | **0.0062** | ** |
| Circulatory disease | -0.3883 | 1.9422 | ±3.8844 | -0.200 | 0.8415 |  |
| Nocturnal time > 180 (%) | +0.1373 | 0.1366 | ±0.2732 | +1.005 | 0.3148 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
