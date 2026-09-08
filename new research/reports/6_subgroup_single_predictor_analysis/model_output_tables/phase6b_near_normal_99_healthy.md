# Phase 6b model output tables - Near-normal substitute: >= 99% of readings within 70-180 - Healthy group (no diabetes + pre-diabetes / lifestyle)

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models.


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 393; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **393**, R² = **0.1391**, Adj R² = **0.1166**, F-statistic = **6.17** (p = **9.43e-09**), Residual SE = **2.607** on **382** df, AIC = **1879.1**, BIC = **1922.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.4259** | 1.0871 | ±2.1742 | **+28.908** | **9.51e-184** | *** |
| **Education: graduate level (vs college)** | **+0.9049** | 0.2781 | ±0.5563 | **+3.254** | **0.0011** | ** |
| Education: high school or below (vs college) | -0.5548 | 0.6472 | ±1.2943 | -0.857 | 0.3913 |  |
| **Site: UCSD (vs UAB)** | **-0.7757** | 0.3676 | ±0.7352 | **-2.110** | **0.0348** | * |
| Site: UW (vs UAB) | -0.5492 | 0.3467 | ±0.6933 | -1.584 | 0.1132 |  |
| **Age (years)** | **-0.0568** | 0.0128 | ±0.0256 | **-4.434** | **9.26e-06** | *** |
| **BMI (kg/m2)** | **-0.0507** | 0.0189 | ±0.0378 | **-2.683** | **0.0073** | ** |
| Hypertension | -0.3259 | 0.3321 | ±0.6643 | -0.981 | 0.3266 |  |
| High cholesterol | -0.1947 | 0.2976 | ±0.5951 | -0.654 | 0.5129 |  |
| Kidney disease | +0.8477 | 0.5716 | ±1.1431 | +1.483 | 0.1380 |  |
| Circulatory disease | -0.6313 | 0.5242 | ±1.0483 | -1.204 | 0.2284 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **393**, R² = **0.1435**, Adj R² = **0.1187**, F-statistic = **5.80** (p = **1.06e-08**), Residual SE = **2.603** on **381** df, AIC = **1879.1**, BIC = **1926.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+34.7519** | 2.7597 | ±5.5194 | **+12.593** | **2.32e-36** | *** |
| **Education: graduate level (vs college)** | **+0.9009** | 0.2784 | ±0.5568 | **+3.236** | **0.0012** | ** |
| Education: high school or below (vs college) | -0.5377 | 0.6446 | ±1.2892 | -0.834 | 0.4041 |  |
| **Site: UCSD (vs UAB)** | **-0.7915** | 0.3648 | ±0.7297 | **-2.170** | **0.0300** | * |
| Site: UW (vs UAB) | -0.5767 | 0.3440 | ±0.6879 | -1.677 | 0.0936 | . |
| **Age (years)** | **-0.0550** | 0.0129 | ±0.0258 | **-4.258** | **2.06e-05** | *** |
| **BMI (kg/m2)** | **-0.0480** | 0.0183 | ±0.0366 | **-2.621** | **0.0088** | ** |
| Hypertension | -0.2914 | 0.3302 | ±0.6603 | -0.883 | 0.3774 |  |
| High cholesterol | -0.1223 | 0.3004 | ±0.6008 | -0.407 | 0.6840 |  |
| Kidney disease | +0.7944 | 0.5661 | ±1.1323 | +1.403 | 0.1606 |  |
| Circulatory disease | -0.6540 | 0.5266 | ±1.0532 | -1.242 | 0.2143 |  |
| HbA1c (%) | -0.6375 | 0.4928 | ±0.9856 | -1.294 | 0.1958 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **393**, R² = **0.1441**, Adj R² = **0.1194**, F-statistic = **5.83** (p = **9.35e-09**), Residual SE = **2.602** on **381** df, AIC = **1878.8**, BIC = **1926.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+34.3841** | 2.3763 | ±4.7525 | **+14.470** | **1.88e-47** | *** |
| **Education: graduate level (vs college)** | **+0.9134** | 0.2784 | ±0.5568 | **+3.281** | **0.0010** | ** |
| Education: high school or below (vs college) | -0.5693 | 0.6415 | ±1.2829 | -0.887 | 0.3748 |  |
| **Site: UCSD (vs UAB)** | **-0.7473** | 0.3716 | ±0.7431 | **-2.011** | **0.0443** | * |
| Site: UW (vs UAB) | -0.5167 | 0.3491 | ±0.6983 | -1.480 | 0.1389 |  |
| **Age (years)** | **-0.0574** | 0.0128 | ±0.0255 | **-4.499** | **6.82e-06** | *** |
| **BMI (kg/m2)** | **-0.0485** | 0.0187 | ±0.0374 | **-2.599** | **0.0094** | ** |
| Hypertension | -0.2972 | 0.3328 | ±0.6655 | -0.893 | 0.3718 |  |
| High cholesterol | -0.2165 | 0.3003 | ±0.6006 | -0.721 | 0.4710 |  |
| Kidney disease | +0.8783 | 0.5599 | ±1.1198 | +1.569 | 0.1167 |  |
| Circulatory disease | -0.6249 | 0.5205 | ±1.0410 | -1.201 | 0.2299 |  |
| Mean glucose (mg/dL) | -0.0263 | 0.0187 | ±0.0374 | -1.406 | 0.1597 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **393**, R² = **0.1441**, Adj R² = **0.1194**, F-statistic = **5.83** (p = **9.35e-09**), Residual SE = **2.602** on **381** df, AIC = **1878.8**, BIC = **1926.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+38.0261** | 4.8309 | ±9.6618 | **+7.871** | **3.51e-15** | *** |
| **Education: graduate level (vs college)** | **+0.9134** | 0.2784 | ±0.5568 | **+3.281** | **0.0010** | ** |
| Education: high school or below (vs college) | -0.5693 | 0.6415 | ±1.2829 | -0.887 | 0.3748 |  |
| **Site: UCSD (vs UAB)** | **-0.7473** | 0.3716 | ±0.7431 | **-2.011** | **0.0443** | * |
| Site: UW (vs UAB) | -0.5167 | 0.3491 | ±0.6983 | -1.480 | 0.1389 |  |
| **Age (years)** | **-0.0574** | 0.0128 | ±0.0255 | **-4.499** | **6.82e-06** | *** |
| **BMI (kg/m2)** | **-0.0485** | 0.0187 | ±0.0374 | **-2.599** | **0.0094** | ** |
| Hypertension | -0.2972 | 0.3328 | ±0.6655 | -0.893 | 0.3718 |  |
| High cholesterol | -0.2165 | 0.3003 | ±0.6006 | -0.721 | 0.4710 |  |
| Kidney disease | +0.8783 | 0.5599 | ±1.1198 | +1.569 | 0.1167 |  |
| Circulatory disease | -0.6249 | 0.5205 | ±1.0410 | -1.201 | 0.2299 |  |
| GMI (%) | -1.1003 | 0.7826 | ±1.5652 | -1.406 | 0.1597 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **393**, R² = **0.1393**, Adj R² = **0.1144**, F-statistic = **5.60** (p = **2.37e-08**), Residual SE = **2.610** on **381** df, AIC = **1881.1**, BIC = **1928.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.8703** | 1.9971 | ±3.9942 | **+15.958** | **2.49e-57** | *** |
| **Education: graduate level (vs college)** | **+0.9022** | 0.2797 | ±0.5594 | **+3.226** | **0.0013** | ** |
| Education: high school or below (vs college) | -0.5603 | 0.6496 | ±1.2991 | -0.863 | 0.3884 |  |
| **Site: UCSD (vs UAB)** | **-0.7663** | 0.3767 | ±0.7535 | **-2.034** | **0.0419** | * |
| Site: UW (vs UAB) | -0.5410 | 0.3533 | ±0.7066 | -1.531 | 0.1257 |  |
| **Age (years)** | **-0.0573** | 0.0129 | ±0.0257 | **-4.448** | **8.67e-06** | *** |
| **BMI (kg/m2)** | **-0.0498** | 0.0192 | ±0.0384 | **-2.590** | **0.0096** | ** |
| Hypertension | -0.3232 | 0.3327 | ±0.6654 | -0.972 | 0.3313 |  |
| High cholesterol | -0.1956 | 0.2990 | ±0.5981 | -0.654 | 0.5130 |  |
| Kidney disease | +0.8466 | 0.5707 | ±1.1413 | +1.483 | 0.1379 |  |
| Circulatory disease | -0.6316 | 0.5247 | ±1.0495 | -1.204 | 0.2287 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0039 | 0.0152 | ±0.0304 | -0.256 | 0.7980 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **393**, R² = **0.1398**, Adj R² = **0.1149**, F-statistic = **5.63** (p = **2.15e-08**), Residual SE = **2.609** on **381** df, AIC = **1880.8**, BIC = **1928.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.8811** | 1.4138 | ±2.8276 | **+21.842** | **9.21e-106** | *** |
| **Education: graduate level (vs college)** | **+0.9157** | 0.2772 | ±0.5544 | **+3.303** | **9.56e-04** | *** |
| Education: high school or below (vs college) | -0.5559 | 0.6502 | ±1.3004 | -0.855 | 0.3926 |  |
| **Site: UCSD (vs UAB)** | **-0.7597** | 0.3634 | ±0.7269 | **-2.090** | **0.0366** | * |
| Site: UW (vs UAB) | -0.5393 | 0.3465 | ±0.6930 | -1.556 | 0.1196 |  |
| **Age (years)** | **-0.0568** | 0.0128 | ±0.0257 | **-4.421** | **9.81e-06** | *** |
| **BMI (kg/m2)** | **-0.0511** | 0.0191 | ±0.0383 | **-2.673** | **0.0075** | ** |
| Hypertension | -0.3283 | 0.3330 | ±0.6660 | -0.986 | 0.3242 |  |
| High cholesterol | -0.1864 | 0.3008 | ±0.6015 | -0.620 | 0.5355 |  |
| Kidney disease | +0.8276 | 0.5706 | ±1.1412 | +1.450 | 0.1469 |  |
| Circulatory disease | -0.6362 | 0.5266 | ±1.0532 | -1.208 | 0.2270 |  |
| Glucose SD, pooled (mg/dL) | +0.0325 | 0.0666 | ±0.1332 | +0.487 | 0.6259 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **393**, R² = **0.1419**, Adj R² = **0.1171**, F-statistic = **5.73** (p = **1.44e-08**), Residual SE = **2.606** on **381** df, AIC = **1879.9**, BIC = **1927.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.4305** | 1.3249 | ±2.6498 | **+22.968** | **9.75e-117** | *** |
| **Education: graduate level (vs college)** | **+0.9270** | 0.2784 | ±0.5567 | **+3.330** | **8.68e-04** | *** |
| Education: high school or below (vs college) | -0.5498 | 0.6513 | ±1.3026 | -0.844 | 0.3985 |  |
| **Site: UCSD (vs UAB)** | **-0.7397** | 0.3641 | ±0.7282 | **-2.032** | **0.0422** | * |
| Site: UW (vs UAB) | -0.5278 | 0.3464 | ±0.6927 | -1.524 | 0.1276 |  |
| **Age (years)** | **-0.0568** | 0.0128 | ±0.0256 | **-4.432** | **9.34e-06** | *** |
| **BMI (kg/m2)** | **-0.0524** | 0.0194 | ±0.0387 | **-2.706** | **0.0068** | ** |
| Hypertension | -0.3232 | 0.3336 | ±0.6673 | -0.969 | 0.3327 |  |
| High cholesterol | -0.1810 | 0.2989 | ±0.5977 | -0.606 | 0.5448 |  |
| Kidney disease | +0.8076 | 0.5664 | ±1.1327 | +1.426 | 0.1539 |  |
| Circulatory disease | -0.6352 | 0.5275 | ±1.0549 | -1.204 | 0.2285 |  |
| Avg. daily SD (mg/dL) | +0.0658 | 0.0605 | ±0.1211 | +1.087 | 0.2772 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **393**, R² = **0.1424**, Adj R² = **0.1177**, F-statistic = **5.75** (p = **1.29e-08**), Residual SE = **2.605** on **381** df, AIC = **1879.6**, BIC = **1927.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.2397** | 1.3397 | ±2.6794 | **+22.572** | **8.11e-113** | *** |
| **Education: graduate level (vs college)** | **+0.9316** | 0.2767 | ±0.5533 | **+3.367** | **7.59e-04** | *** |
| Education: high school or below (vs college) | -0.5624 | 0.6484 | ±1.2969 | -0.867 | 0.3858 |  |
| **Site: UCSD (vs UAB)** | **-0.7310** | 0.3645 | ±0.7289 | **-2.006** | **0.0449** | * |
| Site: UW (vs UAB) | -0.5151 | 0.3470 | ±0.6941 | -1.484 | 0.1377 |  |
| **Age (years)** | **-0.0570** | 0.0128 | ±0.0256 | **-4.450** | **8.58e-06** | *** |
| **BMI (kg/m2)** | **-0.0508** | 0.0188 | ±0.0377 | **-2.699** | **0.0070** | ** |
| Hypertension | -0.3204 | 0.3341 | ±0.6682 | -0.959 | 0.3375 |  |
| High cholesterol | -0.1835 | 0.2989 | ±0.5979 | -0.614 | 0.5392 |  |
| Kidney disease | +0.8177 | 0.5602 | ±1.1203 | +1.460 | 0.1444 |  |
| Circulatory disease | -0.6404 | 0.5267 | ±1.0534 | -1.216 | 0.2241 |  |
| CV (%) | +0.0791 | 0.0666 | ±0.1333 | +1.188 | 0.2350 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **393**, R² = **0.1432**, Adj R² = **0.1185**, F-statistic = **5.79** (p = **1.12e-08**), Residual SE = **2.604** on **381** df, AIC = **1879.3**, BIC = **1926.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.6398** | 1.5198 | ±3.0397 | **+21.476** | **2.61e-102** | *** |
| **Education: graduate level (vs college)** | **+0.9380** | 0.2767 | ±0.5534 | **+3.390** | **6.99e-04** | *** |
| Education: high school or below (vs college) | -0.5630 | 0.6493 | ±1.2986 | -0.867 | 0.3859 |  |
| **Site: UCSD (vs UAB)** | **-0.7373** | 0.3652 | ±0.7304 | **-2.019** | **0.0435** | * |
| Site: UW (vs UAB) | -0.5220 | 0.3473 | ±0.6946 | -1.503 | 0.1328 |  |
| **Age (years)** | **-0.0569** | 0.0128 | ±0.0256 | **-4.448** | **8.66e-06** | *** |
| **BMI (kg/m2)** | **-0.0508** | 0.0188 | ±0.0375 | **-2.704** | **0.0069** | ** |
| Hypertension | -0.3266 | 0.3334 | ±0.6667 | -0.980 | 0.3272 |  |
| High cholesterol | -0.1805 | 0.2985 | ±0.5970 | -0.605 | 0.5453 |  |
| Kidney disease | +0.8254 | 0.5626 | ±1.1252 | +1.467 | 0.1424 |  |
| Circulatory disease | -0.6403 | 0.5263 | ±1.0526 | -1.217 | 0.2238 |  |
| Mean / SD ratio | -0.1794 | 0.1331 | ±0.2662 | -1.348 | 0.1777 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **393**, R² = **0.1446**, Adj R² = **0.1199**, F-statistic = **5.86** (p = **8.45e-09**), Residual SE = **2.602** on **381** df, AIC = **1878.6**, BIC = **1926.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.7502** | 1.4620 | ±2.9239 | **+22.402** | **3.80e-111** | *** |
| **Education: graduate level (vs college)** | **+0.9434** | 0.2781 | ±0.5562 | **+3.392** | **6.93e-04** | *** |
| Education: high school or below (vs college) | -0.5550 | 0.6490 | ±1.2979 | -0.855 | 0.3924 |  |
| **Site: UCSD (vs UAB)** | **-0.7246** | 0.3658 | ±0.7316 | **-1.981** | **0.0476** | * |
| Site: UW (vs UAB) | -0.5189 | 0.3461 | ±0.6923 | -1.499 | 0.1338 |  |
| **Age (years)** | **-0.0569** | 0.0127 | ±0.0255 | **-4.460** | **8.18e-06** | *** |
| **BMI (kg/m2)** | **-0.0526** | 0.0191 | ±0.0383 | **-2.747** | **0.0060** | ** |
| Hypertension | -0.3112 | 0.3343 | ±0.6686 | -0.931 | 0.3519 |  |
| High cholesterol | -0.1851 | 0.2979 | ±0.5958 | -0.621 | 0.5343 |  |
| Kidney disease | +0.8144 | 0.5604 | ±1.1208 | +1.453 | 0.1462 |  |
| Circulatory disease | -0.6346 | 0.5264 | ±1.0528 | -1.206 | 0.2280 |  |
| Avg. daily mean/SD | -0.1679 | 0.1051 | ±0.2102 | -1.597 | 0.1103 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **393**, R² = **0.1393**, Adj R² = **0.1145**, F-statistic = **5.61** (p = **2.34e-08**), Residual SE = **2.610** on **381** df, AIC = **1881.0**, BIC = **1928.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.7231** | 1.4335 | ±2.8669 | **+22.130** | **1.61e-108** | *** |
| **Education: graduate level (vs college)** | **+0.9057** | 0.2786 | ±0.5572 | **+3.251** | **0.0012** | ** |
| Education: high school or below (vs college) | -0.5438 | 0.6425 | ±1.2851 | -0.846 | 0.3974 |  |
| **Site: UCSD (vs UAB)** | **-0.7822** | 0.3681 | ±0.7362 | **-2.125** | **0.0336** | * |
| Site: UW (vs UAB) | -0.5614 | 0.3486 | ±0.6973 | -1.610 | 0.1073 |  |
| **Age (years)** | **-0.0572** | 0.0130 | ±0.0260 | **-4.403** | **1.07e-05** | *** |
| **BMI (kg/m2)** | **-0.0511** | 0.0189 | ±0.0379 | **-2.700** | **0.0069** | ** |
| Hypertension | -0.3302 | 0.3322 | ±0.6643 | -0.994 | 0.3201 |  |
| High cholesterol | -0.1888 | 0.2992 | ±0.5983 | -0.631 | 0.5281 |  |
| Kidney disease | +0.8565 | 0.5735 | ±1.1470 | +1.494 | 0.1353 |  |
| Circulatory disease | -0.6317 | 0.5239 | ±1.0478 | -1.206 | 0.2279 |  |
| MAG (mg/dL/h) | -0.0074 | 0.0222 | ±0.0444 | -0.331 | 0.7406 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **393**, R² = **0.1405**, Adj R² = **0.1157**, F-statistic = **5.66** (p = **1.87e-08**), Residual SE = **2.608** on **381** df, AIC = **1880.5**, BIC = **1928.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.5929** | 1.4518 | ±2.9035 | **+21.073** | **1.41e-98** | *** |
| **Education: graduate level (vs college)** | **+0.9121** | 0.2784 | ±0.5569 | **+3.276** | **0.0011** | ** |
| Education: high school or below (vs college) | -0.5523 | 0.6537 | ±1.3075 | -0.845 | 0.3982 |  |
| **Site: UCSD (vs UAB)** | **-0.7538** | 0.3662 | ±0.7324 | **-2.058** | **0.0396** | * |
| Site: UW (vs UAB) | -0.5331 | 0.3488 | ±0.6977 | -1.528 | 0.1265 |  |
| **Age (years)** | **-0.0566** | 0.0128 | ±0.0256 | **-4.427** | **9.55e-06** | *** |
| **BMI (kg/m2)** | **-0.0495** | 0.0187 | ±0.0374 | **-2.650** | **0.0081** | ** |
| Hypertension | -0.3148 | 0.3326 | ±0.6652 | -0.946 | 0.3439 |  |
| High cholesterol | -0.1973 | 0.2978 | ±0.5957 | -0.662 | 0.5078 |  |
| Kidney disease | +0.8318 | 0.5698 | ±1.1397 | +1.460 | 0.1444 |  |
| Circulatory disease | -0.6373 | 0.5250 | ±1.0500 | -1.214 | 0.2248 |  |
| Avg. daily range (mg/dL) | +0.0097 | 0.0122 | ±0.0245 | +0.791 | 0.4291 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **393**, R² = **0.1480**, Adj R² = **0.1234**, F-statistic = **6.02** (p = **4.39e-09**), Residual SE = **2.596** on **381** df, AIC = **1877.0**, BIC = **1924.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.1245** | 1.1029 | ±2.2059 | **+29.127** | **1.65e-186** | *** |
| **Education: graduate level (vs college)** | **+0.9236** | 0.2799 | ±0.5598 | **+3.300** | **9.67e-04** | *** |
| Education: high school or below (vs college) | -0.4996 | 0.6439 | ±1.2879 | -0.776 | 0.4378 |  |
| **Site: UCSD (vs UAB)** | **-0.7902** | 0.3655 | ±0.7310 | **-2.162** | **0.0306** | * |
| Site: UW (vs UAB) | -0.5207 | 0.3482 | ±0.6964 | -1.495 | 0.1348 |  |
| **Age (years)** | **-0.0564** | 0.0127 | ±0.0253 | **-4.455** | **8.38e-06** | *** |
| **BMI (kg/m2)** | **-0.0503** | 0.0188 | ±0.0377 | **-2.668** | **0.0076** | ** |
| Hypertension | -0.2892 | 0.3285 | ±0.6570 | -0.880 | 0.3787 |  |
| High cholesterol | -0.1791 | 0.2950 | ±0.5900 | -0.607 | 0.5437 |  |
| Kidney disease | +0.8036 | 0.5647 | ±1.1294 | +1.423 | 0.1547 |  |
| Circulatory disease | -0.5969 | 0.5186 | ±1.0373 | -1.151 | 0.2497 |  |
| SD of daily means (mg/dL) | -0.1519 | 0.1001 | ±0.2002 | -1.517 | 0.1293 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **393**, R² = **0.1392**, Adj R² = **0.1143**, F-statistic = **5.60** (p = **2.42e-08**), Residual SE = **2.610** on **381** df, AIC = **1881.1**, BIC = **1928.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +23.9832 | 44.9619 | ±89.9239 | +0.533 | 0.5937 |  |
| **Education: graduate level (vs college)** | **+0.9038** | 0.2788 | ±0.5576 | **+3.242** | **0.0012** | ** |
| Education: high school or below (vs college) | -0.5554 | 0.6483 | ±1.2965 | -0.857 | 0.3916 |  |
| **Site: UCSD (vs UAB)** | **-0.7790** | 0.3672 | ±0.7344 | **-2.122** | **0.0339** | * |
| Site: UW (vs UAB) | -0.5521 | 0.3480 | ±0.6959 | -1.587 | 0.1126 |  |
| **Age (years)** | **-0.0569** | 0.0129 | ±0.0257 | **-4.416** | **1.00e-05** | *** |
| **BMI (kg/m2)** | **-0.0509** | 0.0189 | ±0.0377 | **-2.697** | **0.0070** | ** |
| Hypertension | -0.3250 | 0.3330 | ±0.6660 | -0.976 | 0.3291 |  |
| High cholesterol | -0.1925 | 0.2975 | ±0.5950 | -0.647 | 0.5175 |  |
| Kidney disease | +0.8524 | 0.5712 | ±1.1423 | +1.492 | 0.1356 |  |
| Circulatory disease | -0.6304 | 0.5260 | ±1.0521 | -1.198 | 0.2308 |  |
| Time in range 70-180, pooled (%) | +0.0749 | 0.4518 | ±0.9036 | +0.166 | 0.8683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **393**, R² = **0.1391**, Adj R² = **0.1143**, F-statistic = **5.60** (p = **2.43e-08**), Residual SE = **2.610** on **381** df, AIC = **1881.1**, BIC = **1928.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +37.4854 | 47.1978 | ±94.3955 | +0.794 | 0.4271 |  |
| **Education: graduate level (vs college)** | **+0.9057** | 0.2788 | ±0.5576 | **+3.248** | **0.0012** | ** |
| Education: high school or below (vs college) | -0.5534 | 0.6502 | ±1.3004 | -0.851 | 0.3947 |  |
| **Site: UCSD (vs UAB)** | **-0.7741** | 0.3677 | ±0.7353 | **-2.106** | **0.0352** | * |
| Site: UW (vs UAB) | -0.5489 | 0.3478 | ±0.6956 | -1.578 | 0.1145 |  |
| **Age (years)** | **-0.0566** | 0.0129 | ±0.0258 | **-4.395** | **1.11e-05** | *** |
| **BMI (kg/m2)** | **-0.0506** | 0.0188 | ±0.0377 | **-2.685** | **0.0072** | ** |
| Hypertension | -0.3246 | 0.3338 | ±0.6676 | -0.972 | 0.3308 |  |
| High cholesterol | -0.1971 | 0.2971 | ±0.5942 | -0.664 | 0.5070 |  |
| Kidney disease | +0.8471 | 0.5747 | ±1.1493 | +1.474 | 0.1404 |  |
| Circulatory disease | -0.6337 | 0.5273 | ±1.0547 | -1.202 | 0.2295 |  |
| Avg. daily time in range 70-180 (%) | -0.0609 | 0.4735 | ±0.9470 | -0.129 | 0.8976 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **393**, R² = **0.1456**, Adj R² = **0.1209**, F-statistic = **5.90** (p = **7.05e-09**), Residual SE = **2.600** on **381** df, AIC = **1878.2**, BIC = **1925.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.2840** | 1.0915 | ±2.1830 | **+28.661** | **1.17e-180** | *** |
| **Education: graduate level (vs college)** | **+0.9178** | 0.2775 | ±0.5549 | **+3.308** | **9.40e-04** | *** |
| Education: high school or below (vs college) | -0.5289 | 0.6435 | ±1.2870 | -0.822 | 0.4111 |  |
| Site: UCSD (vs UAB) | -0.6745 | 0.3777 | ±0.7554 | -1.786 | 0.0741 | . |
| Site: UW (vs UAB) | -0.4830 | 0.3566 | ±0.7132 | -1.354 | 0.1756 |  |
| **Age (years)** | **-0.0570** | 0.0127 | ±0.0254 | **-4.479** | **7.52e-06** | *** |
| **BMI (kg/m2)** | **-0.0508** | 0.0189 | ±0.0379 | **-2.681** | **0.0073** | ** |
| Hypertension | -0.3645 | 0.3309 | ±0.6617 | -1.102 | 0.2706 |  |
| High cholesterol | -0.1969 | 0.2969 | ±0.5939 | -0.663 | 0.5072 |  |
| Kidney disease | +0.9132 | 0.5756 | ±1.1512 | +1.586 | 0.1126 |  |
| Circulatory disease | -0.6595 | 0.5259 | ±1.0517 | -1.254 | 0.2098 |  |
| Any reading < 54 during wear (0/1) | +0.6198 | 0.3364 | ±0.6728 | +1.842 | 0.0654 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **393**, R² = **0.1418**, Adj R² = **0.1170**, F-statistic = **5.72** (p = **1.46e-08**), Residual SE = **2.606** on **381** df, AIC = **1879.9**, BIC = **1927.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.3702** | 1.0936 | ±2.1872 | **+28.685** | **5.92e-181** | *** |
| **Education: graduate level (vs college)** | **+0.9108** | 0.2788 | ±0.5575 | **+3.267** | **0.0011** | ** |
| Education: high school or below (vs college) | -0.5227 | 0.6472 | ±1.2944 | -0.808 | 0.4193 |  |
| Site: UCSD (vs UAB) | -0.7272 | 0.3742 | ±0.7485 | -1.943 | 0.0520 | . |
| Site: UW (vs UAB) | -0.5230 | 0.3509 | ±0.7017 | -1.491 | 0.1361 |  |
| **Age (years)** | **-0.0563** | 0.0128 | ±0.0257 | **-4.382** | **1.17e-05** | *** |
| **BMI (kg/m2)** | **-0.0522** | 0.0191 | ±0.0382 | **-2.731** | **0.0063** | ** |
| Hypertension | -0.3503 | 0.3332 | ±0.6663 | -1.051 | 0.2931 |  |
| High cholesterol | -0.1918 | 0.2978 | ±0.5957 | -0.644 | 0.5197 |  |
| Kidney disease | +0.8784 | 0.5729 | ±1.1458 | +1.533 | 0.1252 |  |
| Circulatory disease | -0.6670 | 0.5243 | ±1.0485 | -1.272 | 0.2033 |  |
| Time < 54 (%) | +2.9216 | 2.4240 | ±4.8479 | +1.205 | 0.2281 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **393**, R² = **0.1401**, Adj R² = **0.1153**, F-statistic = **5.64** (p = **2.01e-08**), Residual SE = **2.608** on **381** df, AIC = **1880.7**, BIC = **1928.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.4075** | 1.0909 | ±2.1819 | **+28.789** | **2.91e-182** | *** |
| **Education: graduate level (vs college)** | **+0.9032** | 0.2786 | ±0.5573 | **+3.241** | **0.0012** | ** |
| Education: high school or below (vs college) | -0.5458 | 0.6459 | ±1.2918 | -0.845 | 0.3981 |  |
| **Site: UCSD (vs UAB)** | **-0.7597** | 0.3713 | ±0.7425 | **-2.046** | **0.0407** | * |
| Site: UW (vs UAB) | -0.5430 | 0.3490 | ±0.6981 | -1.556 | 0.1198 |  |
| **Age (years)** | **-0.0566** | 0.0129 | ±0.0257 | **-4.401** | **1.08e-05** | *** |
| **BMI (kg/m2)** | **-0.0513** | 0.0190 | ±0.0381 | **-2.693** | **0.0071** | ** |
| Hypertension | -0.3335 | 0.3327 | ±0.6654 | -1.002 | 0.3161 |  |
| High cholesterol | -0.1925 | 0.2985 | ±0.5969 | -0.645 | 0.5188 |  |
| Kidney disease | +0.8597 | 0.5718 | ±1.1437 | +1.503 | 0.1327 |  |
| Circulatory disease | -0.6620 | 0.5254 | ±1.0507 | -1.260 | 0.2076 |  |
| Avg. daily time < 54 (%) | +2.1483 | 3.2156 | ±6.4313 | +0.668 | 0.5041 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **393**, R² = **0.1417**, Adj R² = **0.1169**, F-statistic = **5.72** (p = **1.48e-08**), Residual SE = **2.606** on **381** df, AIC = **1879.9**, BIC = **1927.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.2869** | 1.1106 | ±2.2213 | **+28.170** | **1.36e-174** | *** |
| **Education: graduate level (vs college)** | **+0.9206** | 0.2793 | ±0.5586 | **+3.296** | **9.81e-04** | *** |
| Education: high school or below (vs college) | -0.5759 | 0.6467 | ±1.2933 | -0.891 | 0.3732 |  |
| **Site: UCSD (vs UAB)** | **-0.7513** | 0.3701 | ±0.7403 | **-2.030** | **0.0424** | * |
| Site: UW (vs UAB) | -0.5166 | 0.3507 | ±0.7014 | -1.473 | 0.1408 |  |
| **Age (years)** | **-0.0569** | 0.0128 | ±0.0257 | **-4.430** | **9.40e-06** | *** |
| **BMI (kg/m2)** | **-0.0502** | 0.0190 | ±0.0380 | **-2.643** | **0.0082** | ** |
| Hypertension | -0.2972 | 0.3335 | ±0.6670 | -0.891 | 0.3728 |  |
| High cholesterol | -0.2315 | 0.3007 | ±0.6013 | -0.770 | 0.4413 |  |
| Kidney disease | +0.8911 | 0.5787 | ±1.1575 | +1.540 | 0.1236 |  |
| Circulatory disease | -0.6279 | 0.5263 | ±1.0527 | -1.193 | 0.2329 |  |
| Time 54-69, pooled (%) | +0.8063 | 0.7415 | ±1.4830 | +1.087 | 0.2769 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **393**, R² = **0.1432**, Adj R² = **0.1184**, F-statistic = **5.79** (p = **1.12e-08**), Residual SE = **2.604** on **381** df, AIC = **1879.3**, BIC = **1927.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.2826** | 1.0993 | ±2.1986 | **+28.457** | **4.00e-178** | *** |
| **Education: graduate level (vs college)** | **+0.9314** | 0.2798 | ±0.5595 | **+3.329** | **8.71e-04** | *** |
| Education: high school or below (vs college) | -0.5820 | 0.6437 | ±1.2874 | -0.904 | 0.3659 |  |
| **Site: UCSD (vs UAB)** | **-0.7622** | 0.3689 | ±0.7379 | **-2.066** | **0.0389** | * |
| Site: UW (vs UAB) | -0.5324 | 0.3497 | ±0.6995 | -1.522 | 0.1279 |  |
| **Age (years)** | **-0.0570** | 0.0128 | ±0.0257 | **-4.447** | **8.73e-06** | *** |
| **BMI (kg/m2)** | **-0.0502** | 0.0189 | ±0.0379 | **-2.653** | **0.0080** | ** |
| Hypertension | -0.2665 | 0.3368 | ±0.6736 | -0.791 | 0.4288 |  |
| High cholesterol | -0.2287 | 0.2989 | ±0.5977 | -0.765 | 0.4442 |  |
| Kidney disease | +0.8976 | 0.5798 | ±1.1596 | +1.548 | 0.1216 |  |
| Circulatory disease | -0.6431 | 0.5259 | ±1.0519 | -1.223 | 0.2214 |  |
| Avg. daily time 54-69 (%) | +1.0139 | 0.7362 | ±1.4724 | +1.377 | 0.1684 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **393**, R² = **0.1425**, Adj R² = **0.1178**, F-statistic = **5.76** (p = **1.27e-08**), Residual SE = **2.605** on **381** df, AIC = **1879.6**, BIC = **1927.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.2681** | 1.1116 | ±2.2231 | **+28.130** | **4.21e-174** | *** |
| **Education: graduate level (vs college)** | **+0.9226** | 0.2793 | ±0.5586 | **+3.303** | **9.56e-04** | *** |
| Education: high school or below (vs college) | -0.5673 | 0.6458 | ±1.2916 | -0.878 | 0.3797 |  |
| **Site: UCSD (vs UAB)** | **-0.7370** | 0.3714 | ±0.7428 | **-1.985** | **0.0472** | * |
| Site: UW (vs UAB) | -0.5085 | 0.3518 | ±0.7036 | -1.445 | 0.1484 |  |
| **Age (years)** | **-0.0567** | 0.0128 | ±0.0257 | **-4.418** | **9.96e-06** | *** |
| **BMI (kg/m2)** | **-0.0506** | 0.0190 | ±0.0381 | **-2.662** | **0.0078** | ** |
| Hypertension | -0.3035 | 0.3326 | ±0.6652 | -0.913 | 0.3615 |  |
| High cholesterol | -0.2315 | 0.2997 | ±0.5994 | -0.772 | 0.4399 |  |
| Kidney disease | +0.9007 | 0.5788 | ±1.1576 | +1.556 | 0.1197 |  |
| Circulatory disease | -0.6379 | 0.5261 | ±1.0522 | -1.212 | 0.2253 |  |
| Time < 70 (%) | +0.8242 | 0.6463 | ±1.2926 | +1.275 | 0.2022 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **393**, R² = **0.1432**, Adj R² = **0.1185**, F-statistic = **5.79** (p = **1.10e-08**), Residual SE = **2.604** on **381** df, AIC = **1879.2**, BIC = **1926.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.2872** | 1.0994 | ±2.1989 | **+28.457** | **3.95e-178** | *** |
| **Education: graduate level (vs college)** | **+0.9283** | 0.2797 | ±0.5594 | **+3.319** | **9.03e-04** | *** |
| Education: high school or below (vs college) | -0.5757 | 0.6429 | ±1.2858 | -0.896 | 0.3705 |  |
| **Site: UCSD (vs UAB)** | **-0.7564** | 0.3692 | ±0.7384 | **-2.049** | **0.0405** | * |
| Site: UW (vs UAB) | -0.5312 | 0.3501 | ±0.7003 | -1.517 | 0.1292 |  |
| **Age (years)** | **-0.0569** | 0.0128 | ±0.0257 | **-4.438** | **9.10e-06** | *** |
| **BMI (kg/m2)** | **-0.0505** | 0.0190 | ±0.0379 | **-2.664** | **0.0077** | ** |
| Hypertension | -0.2750 | 0.3356 | ±0.6712 | -0.819 | 0.4125 |  |
| High cholesterol | -0.2248 | 0.2986 | ±0.5972 | -0.753 | 0.4516 |  |
| Kidney disease | +0.8984 | 0.5791 | ±1.1582 | +1.551 | 0.1208 |  |
| Circulatory disease | -0.6553 | 0.5255 | ±1.0511 | -1.247 | 0.2125 |  |
| Avg. daily time < 70 (%) | +0.9256 | 0.6594 | ±1.3189 | +1.404 | 0.1604 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **393**, R² = **0.1422**, Adj R² = **0.1174**, F-statistic = **5.74** (p = **1.36e-08**), Residual SE = **2.605** on **381** df, AIC = **1879.7**, BIC = **1927.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +341.2095 | 244.1645 | ±488.3290 | +1.397 | 0.1623 |  |
| **Education: graduate level (vs college)** | **+0.9135** | 0.2790 | ±0.5579 | **+3.275** | **0.0011** | ** |
| Education: high school or below (vs college) | -0.5188 | 0.6472 | ±1.2945 | -0.801 | 0.4228 |  |
| Site: UCSD (vs UAB) | -0.7240 | 0.3742 | ±0.7483 | -1.935 | 0.0530 | . |
| Site: UW (vs UAB) | -0.5233 | 0.3506 | ±0.7013 | -1.492 | 0.1356 |  |
| **Age (years)** | **-0.0561** | 0.0128 | ±0.0257 | **-4.371** | **1.23e-05** | *** |
| **BMI (kg/m2)** | **-0.0522** | 0.0191 | ±0.0382 | **-2.733** | **0.0063** | ** |
| Hypertension | -0.3509 | 0.3330 | ±0.6661 | -1.053 | 0.2921 |  |
| High cholesterol | -0.1944 | 0.2976 | ±0.5953 | -0.653 | 0.5137 |  |
| Kidney disease | +0.8809 | 0.5729 | ±1.1459 | +1.537 | 0.1242 |  |
| Circulatory disease | -0.6688 | 0.5242 | ±1.0485 | -1.276 | 0.2020 |  |
| Time 54-250, pooled (%) | -3.0985 | 2.4429 | ±4.8859 | -1.268 | 0.2047 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **393**, R² = **0.1404**, Adj R² = **0.1156**, F-statistic = **5.66** (p = **1.89e-08**), Residual SE = **2.608** on **381** df, AIC = **1880.5**, BIC = **1928.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +273.7451 | 324.9383 | ±649.8767 | +0.842 | 0.3995 |  |
| **Education: graduate level (vs college)** | **+0.9050** | 0.2788 | ±0.5575 | **+3.246** | **0.0012** | ** |
| Education: high school or below (vs college) | -0.5429 | 0.6457 | ±1.2914 | -0.841 | 0.4004 |  |
| **Site: UCSD (vs UAB)** | **-0.7575** | 0.3711 | ±0.7422 | **-2.041** | **0.0412** | * |
| Site: UW (vs UAB) | -0.5438 | 0.3490 | ±0.6980 | -1.558 | 0.1192 |  |
| **Age (years)** | **-0.0565** | 0.0129 | ±0.0257 | **-4.391** | **1.13e-05** | *** |
| **BMI (kg/m2)** | **-0.0513** | 0.0190 | ±0.0380 | **-2.695** | **0.0070** | ** |
| Hypertension | -0.3337 | 0.3327 | ±0.6655 | -1.003 | 0.3159 |  |
| High cholesterol | -0.1947 | 0.2982 | ±0.5965 | -0.653 | 0.5139 |  |
| Kidney disease | +0.8618 | 0.5719 | ±1.1437 | +1.507 | 0.1318 |  |
| Circulatory disease | -0.6656 | 0.5253 | ±1.0506 | -1.267 | 0.2051 |  |
| Avg. daily time 54-250 (%) | -2.4235 | 3.2503 | ±6.5006 | -0.746 | 0.4559 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **393**, R² = **0.1417**, Adj R² = **0.1169**, F-statistic = **5.72** (p = **1.50e-08**), Residual SE = **2.606** on **381** df, AIC = **1880.0**, BIC = **1927.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.6423** | 1.1045 | ±2.2091 | **+28.648** | **1.71e-180** | *** |
| **Education: graduate level (vs college)** | **+0.9086** | 0.2795 | ±0.5590 | **+3.251** | **0.0012** | ** |
| Education: high school or below (vs college) | -0.5663 | 0.6408 | ±1.2817 | -0.884 | 0.3768 |  |
| **Site: UCSD (vs UAB)** | **-0.7744** | 0.3697 | ±0.7394 | **-2.094** | **0.0362** | * |
| Site: UW (vs UAB) | -0.5443 | 0.3472 | ±0.6944 | -1.568 | 0.1170 |  |
| **Age (years)** | **-0.0573** | 0.0129 | ±0.0257 | **-4.458** | **8.28e-06** | *** |
| **BMI (kg/m2)** | **-0.0520** | 0.0194 | ±0.0388 | **-2.685** | **0.0073** | ** |
| Hypertension | -0.3062 | 0.3326 | ±0.6653 | -0.921 | 0.3572 |  |
| High cholesterol | -0.2031 | 0.2987 | ±0.5974 | -0.680 | 0.4966 |  |
| Kidney disease | +0.9116 | 0.5700 | ±1.1401 | +1.599 | 0.1098 |  |
| Circulatory disease | -0.6290 | 0.5256 | ±1.0512 | -1.197 | 0.2314 |  |
| Time 181-250, pooled (%) | -0.5045 | 0.4835 | ±0.9670 | -1.043 | 0.2968 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **393**, R² = **0.1405**, Adj R² = **0.1157**, F-statistic = **5.66** (p = **1.85e-08**), Residual SE = **2.608** on **381** df, AIC = **1880.5**, BIC = **1928.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.5788** | 1.0870 | ±2.1741 | **+29.050** | **1.53e-185** | *** |
| **Education: graduate level (vs college)** | **+0.9098** | 0.2798 | ±0.5596 | **+3.252** | **0.0011** | ** |
| Education: high school or below (vs college) | -0.5716 | 0.6434 | ±1.2868 | -0.888 | 0.3743 |  |
| **Site: UCSD (vs UAB)** | **-0.7775** | 0.3687 | ±0.7373 | **-2.109** | **0.0349** | * |
| Site: UW (vs UAB) | -0.5436 | 0.3480 | ±0.6959 | -1.562 | 0.1183 |  |
| **Age (years)** | **-0.0576** | 0.0129 | ±0.0258 | **-4.472** | **7.75e-06** | *** |
| **BMI (kg/m2)** | **-0.0511** | 0.0189 | ±0.0378 | **-2.699** | **0.0070** | ** |
| Hypertension | -0.3128 | 0.3332 | ±0.6664 | -0.939 | 0.3479 |  |
| High cholesterol | -0.1922 | 0.2979 | ±0.5957 | -0.645 | 0.5187 |  |
| Kidney disease | +0.8723 | 0.5691 | ±1.1381 | +1.533 | 0.1253 |  |
| Circulatory disease | -0.6261 | 0.5268 | ±1.0536 | -1.189 | 0.2346 |  |
| Avg. daily time 181-250 (%) | -0.3790 | 0.5184 | ±1.0368 | -0.731 | 0.4647 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **393**, R² = **0.1416**, Adj R² = **0.1168**, F-statistic = **5.71** (p = **1.52e-08**), Residual SE = **2.606** on **381** df, AIC = **1880.0**, BIC = **1927.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.6408** | 1.1047 | ±2.2094 | **+28.642** | **2.03e-180** | *** |
| **Education: graduate level (vs college)** | **+0.9082** | 0.2795 | ±0.5590 | **+3.249** | **0.0012** | ** |
| Education: high school or below (vs college) | -0.5665 | 0.6410 | ±1.2820 | -0.884 | 0.3768 |  |
| **Site: UCSD (vs UAB)** | **-0.7744** | 0.3697 | ±0.7394 | **-2.095** | **0.0362** | * |
| Site: UW (vs UAB) | -0.5440 | 0.3472 | ±0.6944 | -1.567 | 0.1171 |  |
| **Age (years)** | **-0.0573** | 0.0129 | ±0.0257 | **-4.458** | **8.28e-06** | *** |
| **BMI (kg/m2)** | **-0.0520** | 0.0194 | ±0.0388 | **-2.686** | **0.0072** | ** |
| Hypertension | -0.3067 | 0.3326 | ±0.6653 | -0.922 | 0.3566 |  |
| High cholesterol | -0.2025 | 0.2987 | ±0.5974 | -0.678 | 0.4978 |  |
| Kidney disease | +0.9106 | 0.5701 | ±1.1402 | +1.597 | 0.1102 |  |
| Circulatory disease | -0.6291 | 0.5256 | ±1.0512 | -1.197 | 0.2313 |  |
| Time > 180 (%) | -0.4973 | 0.4827 | ±0.9654 | -1.030 | 0.3029 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **393**, R² = **0.1405**, Adj R² = **0.1157**, F-statistic = **5.66** (p = **1.87e-08**), Residual SE = **2.608** on **381** df, AIC = **1880.5**, BIC = **1928.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.5769** | 1.0874 | ±2.1749 | **+29.038** | **2.18e-185** | *** |
| **Education: graduate level (vs college)** | **+0.9094** | 0.2798 | ±0.5595 | **+3.251** | **0.0012** | ** |
| Education: high school or below (vs college) | -0.5716 | 0.6436 | ±1.2872 | -0.888 | 0.3745 |  |
| **Site: UCSD (vs UAB)** | **-0.7775** | 0.3686 | ±0.7373 | **-2.109** | **0.0349** | * |
| Site: UW (vs UAB) | -0.5434 | 0.3480 | ±0.6960 | -1.562 | 0.1184 |  |
| **Age (years)** | **-0.0576** | 0.0129 | ±0.0258 | **-4.471** | **7.80e-06** | *** |
| **BMI (kg/m2)** | **-0.0511** | 0.0189 | ±0.0378 | **-2.699** | **0.0069** | ** |
| Hypertension | -0.3131 | 0.3332 | ±0.6663 | -0.940 | 0.3473 |  |
| High cholesterol | -0.1919 | 0.2979 | ±0.5957 | -0.644 | 0.5194 |  |
| Kidney disease | +0.8717 | 0.5691 | ±1.1383 | +1.532 | 0.1256 |  |
| Circulatory disease | -0.6263 | 0.5268 | ±1.0536 | -1.189 | 0.2345 |  |
| Avg. daily time > 180 (%) | -0.3711 | 0.5173 | ±1.0346 | -0.717 | 0.4731 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 393)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **393**, R² = **0.1397**, Adj R² = **0.1149**, F-statistic = **5.62** (p = **2.18e-08**), Residual SE = **2.609** on **381** df, AIC = **1880.9**, BIC = **1928.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.4879** | 1.0737 | ±2.1473 | **+29.328** | **4.58e-189** | *** |
| **Education: graduate level (vs college)** | **+0.8957** | 0.2780 | ±0.5560 | **+3.222** | **0.0013** | ** |
| Education: high school or below (vs college) | -0.5546 | 0.6492 | ±1.2984 | -0.854 | 0.3930 |  |
| **Site: UCSD (vs UAB)** | **-0.7843** | 0.3658 | ±0.7316 | **-2.144** | **0.0320** | * |
| Site: UW (vs UAB) | -0.5444 | 0.3512 | ±0.7023 | -1.550 | 0.1211 |  |
| **Age (years)** | **-0.0580** | 0.0127 | ±0.0254 | **-4.562** | **5.07e-06** | *** |
| **BMI (kg/m2)** | **-0.0496** | 0.0193 | ±0.0387 | **-2.561** | **0.0104** | * |
| Hypertension | -0.3170 | 0.3294 | ±0.6588 | -0.962 | 0.3359 |  |
| High cholesterol | -0.1855 | 0.2945 | ±0.5890 | -0.630 | 0.5287 |  |
| Kidney disease | +0.8613 | 0.5789 | ±1.1578 | +1.488 | 0.1368 |  |
| Circulatory disease | -0.6344 | 0.5249 | ±1.0497 | -1.209 | 0.2268 |  |
| Nocturnal time > 180 (%) | -0.2120 | 0.5578 | ±1.1156 | -0.380 | 0.7039 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 393; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0830**, LLR χ² = **41.06** (p = **1.10e-05**), AUC = **0.6811**, AIC = **475.5**, BIC = **519.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.0519** | 0.9425 | ±1.8850 | **-4.299** | **1.71e-05** | 0.0174 | *** |
| **Education: graduate level (vs college)** | **-0.7385** | 0.2449 | ±0.4897 | **-3.016** | **0.0026** | 0.4778 | ** |
| Education: high school or below (vs college) | +0.4290 | 0.3915 | ±0.7831 | +1.096 | 0.2732 | 1.5358 |  |
| Site: UCSD (vs UAB) | +0.5377 | 0.2955 | ±0.5910 | +1.820 | 0.0688 | 1.7120 | . |
| Site: UW (vs UAB) | +0.4388 | 0.3037 | ±0.6073 | +1.445 | 0.1485 | 1.5508 |  |
| **Age (years)** | **+0.0327** | 0.0106 | ±0.0213 | **+3.076** | **0.0021** | 1.0333 | ** |
| **BMI (kg/m2)** | **+0.0383** | 0.0177 | ±0.0353 | **+2.169** | **0.0301** | 1.0391 | * |
| Hypertension | +0.3218 | 0.2521 | ±0.5043 | +1.276 | 0.2018 | 1.3797 |  |
| High cholesterol | +0.1176 | 0.2396 | ±0.4792 | +0.491 | 0.6236 | 1.1248 |  |
| Kidney disease | -0.6986 | 0.5398 | ±1.0796 | -1.294 | 0.1956 | 0.4973 |  |
| Circulatory disease | +0.5114 | 0.3533 | ±0.7067 | +1.447 | 0.1478 | 1.6677 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0843**, LLR χ² = **41.70** (p = **1.82e-05**), AUC = **0.6845**, AIC = **476.9**, BIC = **524.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-5.7321** | 2.3035 | ±4.6070 | **-2.488** | **0.0128** | 0.0032 | * |
| **Education: graduate level (vs college)** | **-0.7421** | 0.2452 | ±0.4904 | **-3.026** | **0.0025** | 0.4761 | ** |
| Education: high school or below (vs college) | +0.4214 | 0.3919 | ±0.7838 | +1.075 | 0.2823 | 1.5241 |  |
| Site: UCSD (vs UAB) | +0.5500 | 0.2960 | ±0.5920 | +1.858 | 0.0632 | 1.7333 | . |
| Site: UW (vs UAB) | +0.4573 | 0.3054 | ±0.6107 | +1.498 | 0.1342 | 1.5799 |  |
| **Age (years)** | **+0.0321** | 0.0107 | ±0.0214 | **+3.005** | **0.0027** | 1.0326 | ** |
| **BMI (kg/m2)** | **+0.0368** | 0.0176 | ±0.0353 | **+2.086** | **0.0370** | 1.0375 | * |
| Hypertension | +0.3068 | 0.2528 | ±0.5057 | +1.214 | 0.2249 | 1.3591 |  |
| High cholesterol | +0.0807 | 0.2442 | ±0.4883 | +0.331 | 0.7410 | 1.0841 |  |
| Kidney disease | -0.6739 | 0.5420 | ±1.0840 | -1.243 | 0.2137 | 0.5097 |  |
| Circulatory disease | +0.5225 | 0.3532 | ±0.7063 | +1.480 | 0.1390 | 1.6863 |  |
| HbA1c (%) | +0.3198 | 0.3983 | ±0.7966 | +0.803 | 0.4221 | 1.3768 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0881**, LLR χ² = **43.57** (p = **8.66e-06**), AUC = **0.6906**, AIC = **475.0**, BIC = **522.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-6.8046** | 1.9965 | ±3.9931 | **-3.408** | **6.54e-04** | 0.0011 | *** |
| **Education: graduate level (vs college)** | **-0.7604** | 0.2464 | ±0.4928 | **-3.086** | **0.0020** | 0.4675 | ** |
| Education: high school or below (vs college) | +0.4420 | 0.3937 | ±0.7874 | +1.123 | 0.2616 | 1.5558 |  |
| Site: UCSD (vs UAB) | +0.5201 | 0.2968 | ±0.5936 | +1.752 | 0.0797 | 1.6822 | . |
| Site: UW (vs UAB) | +0.4142 | 0.3052 | ±0.6105 | +1.357 | 0.1748 | 1.5132 |  |
| **Age (years)** | **+0.0335** | 0.0107 | ±0.0214 | **+3.135** | **0.0017** | 1.0341 | ** |
| **BMI (kg/m2)** | **+0.0364** | 0.0177 | ±0.0354 | **+2.054** | **0.0400** | 1.0371 | * |
| Hypertension | +0.2973 | 0.2535 | ±0.5069 | +1.173 | 0.2408 | 1.3462 |  |
| High cholesterol | +0.1458 | 0.2414 | ±0.4828 | +0.604 | 0.5457 | 1.1570 |  |
| Kidney disease | -0.7291 | 0.5410 | ±1.0820 | -1.348 | 0.1778 | 0.4824 |  |
| Circulatory disease | +0.5124 | 0.3528 | ±0.7056 | +1.452 | 0.1464 | 1.6693 |  |
| Mean glucose (mg/dL) | +0.0243 | 0.0154 | ±0.0308 | +1.579 | 0.1143 | 1.0246 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0881**, LLR χ² = **43.57** (p = **8.66e-06**), AUC = **0.6906**, AIC = **475.0**, BIC = **522.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-10.1691** | 4.0030 | ±8.0060 | **-2.540** | **0.0111** | 0.0000 | * |
| **Education: graduate level (vs college)** | **-0.7604** | 0.2464 | ±0.4928 | **-3.086** | **0.0020** | 0.4675 | ** |
| Education: high school or below (vs college) | +0.4420 | 0.3937 | ±0.7874 | +1.123 | 0.2616 | 1.5558 |  |
| Site: UCSD (vs UAB) | +0.5201 | 0.2968 | ±0.5936 | +1.752 | 0.0797 | 1.6822 | . |
| Site: UW (vs UAB) | +0.4142 | 0.3052 | ±0.6105 | +1.357 | 0.1748 | 1.5132 |  |
| **Age (years)** | **+0.0335** | 0.0107 | ±0.0214 | **+3.135** | **0.0017** | 1.0341 | ** |
| **BMI (kg/m2)** | **+0.0364** | 0.0177 | ±0.0354 | **+2.054** | **0.0400** | 1.0371 | * |
| Hypertension | +0.2973 | 0.2535 | ±0.5069 | +1.173 | 0.2408 | 1.3462 |  |
| High cholesterol | +0.1458 | 0.2414 | ±0.4828 | +0.604 | 0.5457 | 1.1570 |  |
| Kidney disease | -0.7291 | 0.5410 | ±1.0820 | -1.348 | 0.1778 | 0.4824 |  |
| Circulatory disease | +0.5124 | 0.3528 | ±0.7056 | +1.452 | 0.1464 | 1.6693 |  |
| GMI (%) | +1.0165 | 0.6437 | ±1.2874 | +1.579 | 0.1143 | 2.7634 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0838**, LLR χ² = **41.47** (p = **2.00e-05**), AUC = **0.6851**, AIC = **477.1**, BIC = **524.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.9680** | 1.7163 | ±3.4326 | **-2.895** | **0.0038** | 0.0070 | ** |
| **Education: graduate level (vs college)** | **-0.7382** | 0.2450 | ±0.4901 | **-3.013** | **0.0026** | 0.4780 | ** |
| Education: high school or below (vs college) | +0.4394 | 0.3922 | ±0.7843 | +1.120 | 0.2625 | 1.5518 |  |
| Site: UCSD (vs UAB) | +0.5217 | 0.2966 | ±0.5931 | +1.759 | 0.0785 | 1.6849 | . |
| Site: UW (vs UAB) | +0.4237 | 0.3048 | ±0.6095 | +1.390 | 0.1644 | 1.5277 |  |
| **Age (years)** | **+0.0337** | 0.0108 | ±0.0215 | **+3.135** | **0.0017** | 1.0343 | ** |
| **BMI (kg/m2)** | **+0.0364** | 0.0178 | ±0.0356 | **+2.045** | **0.0409** | 1.0371 | * |
| Hypertension | +0.3168 | 0.2523 | ±0.5046 | +1.256 | 0.2093 | 1.3727 |  |
| High cholesterol | +0.1230 | 0.2400 | ±0.4800 | +0.513 | 0.6082 | 1.1309 |  |
| Kidney disease | -0.6959 | 0.5395 | ±1.0790 | -1.290 | 0.1971 | 0.4986 |  |
| Circulatory disease | +0.5154 | 0.3529 | ±0.7057 | +1.461 | 0.1441 | 1.6742 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0080 | 0.0125 | ±0.0249 | +0.642 | 0.5212 | 1.0080 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0830**, LLR χ² = **41.06** (p = **2.35e-05**), AUC = **0.6805**, AIC = **477.5**, BIC = **525.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.1168** | 1.2868 | ±2.5736 | **-3.199** | **0.0014** | 0.0163 | ** |
| **Education: graduate level (vs college)** | **-0.7375** | 0.2453 | ±0.4906 | **-3.007** | **0.0026** | 0.4783 | ** |
| Education: high school or below (vs college) | +0.4289 | 0.3916 | ±0.7832 | +1.095 | 0.2734 | 1.5356 |  |
| Site: UCSD (vs UAB) | +0.5394 | 0.2963 | ±0.5927 | +1.820 | 0.0687 | 1.7149 | . |
| Site: UW (vs UAB) | +0.4398 | 0.3040 | ±0.6080 | +1.447 | 0.1480 | 1.5524 |  |
| **Age (years)** | **+0.0327** | 0.0106 | ±0.0213 | **+3.075** | **0.0021** | 1.0333 | ** |
| **BMI (kg/m2)** | **+0.0383** | 0.0177 | ±0.0354 | **+2.165** | **0.0304** | 1.0390 | * |
| Hypertension | +0.3214 | 0.2522 | ±0.5044 | +1.274 | 0.2025 | 1.3791 |  |
| High cholesterol | +0.1188 | 0.2401 | ±0.4803 | +0.495 | 0.6209 | 1.1261 |  |
| Kidney disease | -0.7016 | 0.5415 | ±1.0829 | -1.296 | 0.1951 | 0.4958 |  |
| Circulatory disease | +0.5108 | 0.3535 | ±0.7069 | +1.445 | 0.1484 | 1.6666 |  |
| Glucose SD, pooled (mg/dL) | +0.0039 | 0.0523 | ±0.1046 | +0.074 | 0.9409 | 1.0039 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0831**, LLR χ² = **41.09** (p = **2.33e-05**), AUC = **0.6821**, AIC = **477.5**, BIC = **525.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.9238** | 1.2182 | ±2.4363 | **-3.221** | **0.0013** | 0.0198 | ** |
| **Education: graduate level (vs college)** | **-0.7410** | 0.2454 | ±0.4907 | **-3.020** | **0.0025** | 0.4766 | ** |
| Education: high school or below (vs college) | +0.4285 | 0.3915 | ±0.7829 | +1.094 | 0.2737 | 1.5349 |  |
| Site: UCSD (vs UAB) | +0.5338 | 0.2965 | ±0.5929 | +1.801 | 0.0718 | 1.7054 | . |
| Site: UW (vs UAB) | +0.4361 | 0.3041 | ±0.6082 | +1.434 | 0.1515 | 1.5467 |  |
| **Age (years)** | **+0.0327** | 0.0106 | ±0.0213 | **+3.076** | **0.0021** | 1.0333 | ** |
| **BMI (kg/m2)** | **+0.0386** | 0.0177 | ±0.0355 | **+2.173** | **0.0298** | 1.0393 | * |
| Hypertension | +0.3217 | 0.2521 | ±0.5042 | +1.276 | 0.2020 | 1.3794 |  |
| High cholesterol | +0.1157 | 0.2399 | ±0.4797 | +0.482 | 0.6296 | 1.1226 |  |
| Kidney disease | -0.6927 | 0.5409 | ±1.0818 | -1.281 | 0.2003 | 0.5002 |  |
| Circulatory disease | +0.5119 | 0.3533 | ±0.7067 | +1.449 | 0.1474 | 1.6685 |  |
| Avg. daily SD (mg/dL) | -0.0086 | 0.0517 | ±0.1034 | -0.166 | 0.8683 | 0.9915 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0838**, LLR χ² = **41.47** (p = **2.00e-05**), AUC = **0.6832**, AIC = **477.1**, BIC = **524.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.5118** | 1.2623 | ±2.5247 | **-2.782** | **0.0054** | 0.0298 | ** |
| **Education: graduate level (vs college)** | **-0.7515** | 0.2460 | ±0.4920 | **-3.055** | **0.0022** | 0.4716 | ** |
| Education: high school or below (vs college) | +0.4325 | 0.3915 | ±0.7831 | +1.105 | 0.2693 | 1.5412 |  |
| Site: UCSD (vs UAB) | +0.5214 | 0.2968 | ±0.5937 | +1.757 | 0.0790 | 1.6844 | . |
| Site: UW (vs UAB) | +0.4254 | 0.3046 | ±0.6093 | +1.396 | 0.1626 | 1.5302 |  |
| **Age (years)** | **+0.0329** | 0.0107 | ±0.0213 | **+3.085** | **0.0020** | 1.0334 | ** |
| **BMI (kg/m2)** | **+0.0384** | 0.0177 | ±0.0354 | **+2.170** | **0.0300** | 1.0391 | * |
| Hypertension | +0.3211 | 0.2522 | ±0.5043 | +1.273 | 0.2029 | 1.3786 |  |
| High cholesterol | +0.1124 | 0.2398 | ±0.4796 | +0.469 | 0.6392 | 1.1190 |  |
| Kidney disease | -0.6804 | 0.5399 | ±1.0799 | -1.260 | 0.2076 | 0.5064 |  |
| Circulatory disease | +0.5178 | 0.3532 | ±0.7063 | +1.466 | 0.1426 | 1.6784 |  |
| CV (%) | -0.0363 | 0.0568 | ±0.1137 | -0.639 | 0.5226 | 0.9643 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0846**, LLR χ² = **41.86** (p = **1.72e-05**), AUC = **0.6838**, AIC = **476.7**, BIC = **524.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.7610** | 1.2380 | ±2.4760 | **-3.846** | **1.20e-04** | 0.0086 | *** |
| **Education: graduate level (vs college)** | **-0.7598** | 0.2466 | ±0.4932 | **-3.081** | **0.0021** | 0.4678 | ** |
| Education: high school or below (vs college) | +0.4339 | 0.3915 | ±0.7831 | +1.108 | 0.2678 | 1.5433 |  |
| Site: UCSD (vs UAB) | +0.5218 | 0.2965 | ±0.5930 | +1.760 | 0.0784 | 1.6850 | . |
| Site: UW (vs UAB) | +0.4270 | 0.3045 | ±0.6090 | +1.402 | 0.1608 | 1.5326 |  |
| **Age (years)** | **+0.0329** | 0.0107 | ±0.0213 | **+3.083** | **0.0021** | 1.0334 | ** |
| **BMI (kg/m2)** | **+0.0384** | 0.0177 | ±0.0354 | **+2.170** | **0.0300** | 1.0391 | * |
| Hypertension | +0.3245 | 0.2523 | ±0.5046 | +1.286 | 0.1984 | 1.3834 |  |
| High cholesterol | +0.1095 | 0.2399 | ±0.4799 | +0.457 | 0.6480 | 1.1158 |  |
| Kidney disease | -0.6800 | 0.5393 | ±1.0787 | -1.261 | 0.2074 | 0.5066 |  |
| Circulatory disease | +0.5198 | 0.3534 | ±0.7067 | +1.471 | 0.1413 | 1.6817 |  |
| Mean / SD ratio | +0.1033 | 0.1154 | ±0.2309 | +0.895 | 0.3709 | 1.1088 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0847**, LLR χ² = **41.91** (p = **1.68e-05**), AUC = **0.6855**, AIC = **476.7**, BIC = **524.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.7385** | 1.2066 | ±2.4131 | **-3.927** | **8.59e-05** | 0.0088 | *** |
| **Education: graduate level (vs college)** | **-0.7600** | 0.2466 | ±0.4932 | **-3.082** | **0.0021** | 0.4677 | ** |
| Education: high school or below (vs college) | +0.4291 | 0.3914 | ±0.7828 | +1.096 | 0.2730 | 1.5358 |  |
| Site: UCSD (vs UAB) | +0.5179 | 0.2967 | ±0.5935 | +1.745 | 0.0809 | 1.6785 | . |
| Site: UW (vs UAB) | +0.4260 | 0.3046 | ±0.6092 | +1.398 | 0.1620 | 1.5311 |  |
| **Age (years)** | **+0.0329** | 0.0107 | ±0.0213 | **+3.082** | **0.0021** | 1.0334 | ** |
| **BMI (kg/m2)** | **+0.0395** | 0.0178 | ±0.0356 | **+2.219** | **0.0265** | 1.0403 | * |
| Hypertension | +0.3156 | 0.2523 | ±0.5047 | +1.251 | 0.2111 | 1.3710 |  |
| High cholesterol | +0.1137 | 0.2397 | ±0.4795 | +0.474 | 0.6353 | 1.1204 |  |
| Kidney disease | -0.6784 | 0.5396 | ±1.0791 | -1.257 | 0.2086 | 0.5074 |  |
| Circulatory disease | +0.5152 | 0.3536 | ±0.7071 | +1.457 | 0.1450 | 1.6741 |  |
| Avg. daily mean/SD | +0.0852 | 0.0920 | ±0.1841 | +0.926 | 0.3544 | 1.0890 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0873**, LLR χ² = **43.15** (p = **1.02e-05**), AUC = **0.6879**, AIC = **475.4**, BIC = **523.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-5.2225** | 1.2518 | ±2.5036 | **-4.172** | **3.02e-05** | 0.0054 | *** |
| **Education: graduate level (vs college)** | **-0.7514** | 0.2458 | ±0.4916 | **-3.057** | **0.0022** | 0.4717 | ** |
| Education: high school or below (vs college) | +0.3862 | 0.3942 | ±0.7885 | +0.979 | 0.3273 | 1.4713 |  |
| Site: UCSD (vs UAB) | +0.5596 | 0.2964 | ±0.5927 | +1.888 | 0.0590 | 1.7499 | . |
| Site: UW (vs UAB) | +0.4822 | 0.3055 | ±0.6111 | +1.578 | 0.1145 | 1.6196 |  |
| **Age (years)** | **+0.0347** | 0.0108 | ±0.0215 | **+3.224** | **0.0013** | 1.0353 | ** |
| **BMI (kg/m2)** | **+0.0400** | 0.0177 | ±0.0354 | **+2.259** | **0.0239** | 1.0408 | * |
| Hypertension | +0.3423 | 0.2533 | ±0.5067 | +1.351 | 0.1767 | 1.4082 |  |
| High cholesterol | +0.0946 | 0.2409 | ±0.4818 | +0.393 | 0.6947 | 1.0992 |  |
| Kidney disease | -0.7377 | 0.5451 | ±1.0903 | -1.353 | 0.1760 | 0.4782 |  |
| Circulatory disease | +0.5178 | 0.3550 | ±0.7100 | +1.458 | 0.1447 | 1.6783 |  |
| MAG (mg/dL/h) | +0.0290 | 0.0200 | ±0.0401 | +1.449 | 0.1473 | 1.0294 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0835**, LLR χ² = **41.29** (p = **2.15e-05**), AUC = **0.6816**, AIC = **477.3**, BIC = **525.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.4983** | 1.3258 | ±2.6516 | **-3.393** | **6.92e-04** | 0.0111 | *** |
| **Education: graduate level (vs college)** | **-0.7369** | 0.2450 | ±0.4900 | **-3.008** | **0.0026** | 0.4786 | ** |
| Education: high school or below (vs college) | +0.4306 | 0.3919 | ±0.7837 | +1.099 | 0.2718 | 1.5382 |  |
| Site: UCSD (vs UAB) | +0.5486 | 0.2965 | ±0.5930 | +1.850 | 0.0643 | 1.7308 | . |
| Site: UW (vs UAB) | +0.4479 | 0.3043 | ±0.6086 | +1.472 | 0.1411 | 1.5649 |  |
| **Age (years)** | **+0.0329** | 0.0107 | ±0.0213 | **+3.084** | **0.0020** | 1.0334 | ** |
| **BMI (kg/m2)** | **+0.0391** | 0.0178 | ±0.0356 | **+2.195** | **0.0281** | 1.0399 | * |
| Hypertension | +0.3274 | 0.2526 | ±0.5052 | +1.296 | 0.1950 | 1.3873 |  |
| High cholesterol | +0.1165 | 0.2398 | ±0.4796 | +0.486 | 0.6271 | 1.1236 |  |
| Kidney disease | -0.7092 | 0.5412 | ±1.0824 | -1.310 | 0.1900 | 0.4920 |  |
| Circulatory disease | +0.5083 | 0.3537 | ±0.7074 | +1.437 | 0.1507 | 1.6625 |  |
| Avg. daily range (mg/dL) | +0.0051 | 0.0106 | ±0.0212 | +0.482 | 0.6299 | 1.0051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0865**, LLR χ² = **42.80** (p = **1.18e-05**), AUC = **0.6836**, AIC = **475.8**, BIC = **523.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.4825** | 1.0043 | ±2.0085 | **-4.463** | **8.06e-06** | 0.0113 | *** |
| **Education: graduate level (vs college)** | **-0.7578** | 0.2463 | ±0.4925 | **-3.077** | **0.0021** | 0.4687 | ** |
| Education: high school or below (vs college) | +0.3984 | 0.3927 | ±0.7854 | +1.014 | 0.3103 | 1.4894 |  |
| Site: UCSD (vs UAB) | +0.5549 | 0.2966 | ±0.5932 | +1.871 | 0.0613 | 1.7418 | . |
| Site: UW (vs UAB) | +0.4294 | 0.3049 | ±0.6098 | +1.408 | 0.1591 | 1.5363 |  |
| **Age (years)** | **+0.0327** | 0.0107 | ±0.0213 | **+3.070** | **0.0021** | 1.0333 | ** |
| **BMI (kg/m2)** | **+0.0385** | 0.0177 | ±0.0354 | **+2.172** | **0.0298** | 1.0392 | * |
| Hypertension | +0.2981 | 0.2536 | ±0.5071 | +1.176 | 0.2397 | 1.3473 |  |
| High cholesterol | +0.1144 | 0.2401 | ±0.4803 | +0.477 | 0.6337 | 1.1212 |  |
| Kidney disease | -0.6746 | 0.5398 | ±1.0797 | -1.250 | 0.2114 | 0.5094 |  |
| Circulatory disease | +0.4942 | 0.3548 | ±0.7095 | +1.393 | 0.1636 | 1.6393 |  |
| SD of daily means (mg/dL) | +0.0868 | 0.0655 | ±0.1310 | +1.325 | 0.1851 | 1.0906 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0833**, LLR χ² = **41.22** (p = **2.21e-05**), AUC = **0.6807**, AIC = **477.4**, BIC = **525.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +11.4988 | 38.6552 | ±77.3104 | +0.297 | 0.7661 | 98601.8887 |  |
| **Education: graduate level (vs college)** | **-0.7347** | 0.2451 | ±0.4901 | **-2.998** | **0.0027** | 0.4797 | ** |
| Education: high school or below (vs college) | +0.4310 | 0.3915 | ±0.7831 | +1.101 | 0.2710 | 1.5387 |  |
| Site: UCSD (vs UAB) | +0.5431 | 0.2959 | ±0.5917 | +1.836 | 0.0664 | 1.7213 | . |
| Site: UW (vs UAB) | +0.4431 | 0.3039 | ±0.6077 | +1.458 | 0.1447 | 1.5576 |  |
| **Age (years)** | **+0.0329** | 0.0107 | ±0.0213 | **+3.084** | **0.0020** | 1.0334 | ** |
| **BMI (kg/m2)** | **+0.0390** | 0.0179 | ±0.0357 | **+2.185** | **0.0289** | 1.0398 | * |
| Hypertension | +0.3196 | 0.2523 | ±0.5045 | +1.267 | 0.2052 | 1.3765 |  |
| High cholesterol | +0.1134 | 0.2399 | ±0.4798 | +0.473 | 0.6365 | 1.1200 |  |
| Kidney disease | -0.7088 | 0.5408 | ±1.0817 | -1.311 | 0.1900 | 0.4922 |  |
| Circulatory disease | +0.5093 | 0.3536 | ±0.7073 | +1.440 | 0.1498 | 1.6641 |  |
| Time in range 70-180, pooled (%) | -0.1565 | 0.3890 | ±0.7780 | -0.402 | 0.6874 | 0.8551 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0832**, LLR χ² = **41.16** (p = **2.26e-05**), AUC = **0.6809**, AIC = **477.4**, BIC = **525.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +7.9284 | 37.5593 | ±75.1187 | +0.211 | 0.8328 | 2774.9596 |  |
| **Education: graduate level (vs college)** | **-0.7370** | 0.2449 | ±0.4898 | **-3.009** | **0.0026** | 0.4785 | ** |
| Education: high school or below (vs college) | +0.4318 | 0.3917 | ±0.7833 | +1.102 | 0.2702 | 1.5400 |  |
| Site: UCSD (vs UAB) | +0.5396 | 0.2956 | ±0.5912 | +1.825 | 0.0679 | 1.7153 | . |
| Site: UW (vs UAB) | +0.4384 | 0.3036 | ±0.6073 | +1.444 | 0.1488 | 1.5502 |  |
| **Age (years)** | **+0.0329** | 0.0107 | ±0.0213 | **+3.087** | **0.0020** | 1.0335 | ** |
| **BMI (kg/m2)** | **+0.0385** | 0.0177 | ±0.0354 | **+2.178** | **0.0294** | 1.0393 | * |
| Hypertension | +0.3241 | 0.2523 | ±0.5046 | +1.285 | 0.1989 | 1.3828 |  |
| High cholesterol | +0.1129 | 0.2401 | ±0.4802 | +0.470 | 0.6382 | 1.1195 |  |
| Kidney disease | -0.6983 | 0.5397 | ±1.0793 | -1.294 | 0.1957 | 0.4975 |  |
| Circulatory disease | +0.5070 | 0.3537 | ±0.7074 | +1.433 | 0.1518 | 1.6603 |  |
| Avg. daily time in range 70-180 (%) | -0.1204 | 0.3775 | ±0.7551 | -0.319 | 0.7497 | 0.8865 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0844**, LLR χ² = **41.76** (p = **1.78e-05**), AUC = **0.6817**, AIC = **476.8**, BIC = **524.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.0075** | 0.9465 | ±1.8929 | **-4.234** | **2.29e-05** | 0.0182 | *** |
| **Education: graduate level (vs college)** | **-0.7463** | 0.2454 | ±0.4907 | **-3.042** | **0.0024** | 0.4741 | ** |
| Education: high school or below (vs college) | +0.4158 | 0.3923 | ±0.7846 | +1.060 | 0.2892 | 1.5157 |  |
| Site: UCSD (vs UAB) | +0.4987 | 0.2994 | ±0.5988 | +1.666 | 0.0958 | 1.6466 | . |
| Site: UW (vs UAB) | +0.4152 | 0.3054 | ±0.6108 | +1.360 | 0.1740 | 1.5147 |  |
| **Age (years)** | **+0.0329** | 0.0107 | ±0.0213 | **+3.086** | **0.0020** | 1.0335 | ** |
| **BMI (kg/m2)** | **+0.0386** | 0.0177 | ±0.0354 | **+2.178** | **0.0294** | 1.0393 | * |
| Hypertension | +0.3432 | 0.2534 | ±0.5068 | +1.354 | 0.1757 | 1.4094 |  |
| High cholesterol | +0.1188 | 0.2399 | ±0.4798 | +0.495 | 0.6205 | 1.1261 |  |
| Kidney disease | -0.7237 | 0.5394 | ±1.0789 | -1.342 | 0.1797 | 0.4849 |  |
| Circulatory disease | +0.5244 | 0.3538 | ±0.7075 | +1.482 | 0.1383 | 1.6894 |  |
| Any reading < 54 during wear (0/1) | -0.2663 | 0.3220 | ±0.6440 | -0.827 | 0.4082 | 0.7662 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0843**, LLR χ² = **41.70** (p = **1.83e-05**), AUC = **0.6829**, AIC = **476.9**, BIC = **524.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.0335** | 0.9455 | ±1.8910 | **-4.266** | **1.99e-05** | 0.0177 | *** |
| **Education: graduate level (vs college)** | **-0.7482** | 0.2457 | ±0.4914 | **-3.045** | **0.0023** | 0.4732 | ** |
| Education: high school or below (vs college) | +0.4065 | 0.3929 | ±0.7857 | +1.035 | 0.3008 | 1.5016 |  |
| Site: UCSD (vs UAB) | +0.5104 | 0.2975 | ±0.5951 | +1.715 | 0.0863 | 1.6659 | . |
| Site: UW (vs UAB) | +0.4280 | 0.3044 | ±0.6088 | +1.406 | 0.1598 | 1.5341 |  |
| **Age (years)** | **+0.0326** | 0.0107 | ±0.0213 | **+3.061** | **0.0022** | 1.0332 | ** |
| **BMI (kg/m2)** | **+0.0394** | 0.0178 | ±0.0356 | **+2.215** | **0.0268** | 1.0402 | * |
| Hypertension | +0.3369 | 0.2529 | ±0.5058 | +1.332 | 0.1828 | 1.4006 |  |
| High cholesterol | +0.1177 | 0.2399 | ±0.4798 | +0.490 | 0.6238 | 1.1249 |  |
| Kidney disease | -0.7195 | 0.5402 | ±1.0804 | -1.332 | 0.1829 | 0.4870 |  |
| Circulatory disease | +0.5380 | 0.3548 | ±0.7096 | +1.516 | 0.1295 | 1.7126 |  |
| Time < 54 (%) | -1.9644 | 2.5362 | ±5.0725 | -0.775 | 0.4386 | 0.1402 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0839**, LLR χ² = **41.52** (p = **1.96e-05**), AUC = **0.6816**, AIC = **477.1**, BIC = **524.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.0488** | 0.9440 | ±1.8881 | **-4.289** | **1.80e-05** | 0.0174 | *** |
| **Education: graduate level (vs college)** | **-0.7414** | 0.2453 | ±0.4906 | **-3.022** | **0.0025** | 0.4764 | ** |
| Education: high school or below (vs college) | +0.4204 | 0.3923 | ±0.7847 | +1.072 | 0.2839 | 1.5226 |  |
| Site: UCSD (vs UAB) | +0.5289 | 0.2960 | ±0.5919 | +1.787 | 0.0739 | 1.6971 | . |
| Site: UW (vs UAB) | +0.4389 | 0.3042 | ±0.6084 | +1.443 | 0.1490 | 1.5510 |  |
| **Age (years)** | **+0.0328** | 0.0107 | ±0.0213 | **+3.075** | **0.0021** | 1.0333 | ** |
| **BMI (kg/m2)** | **+0.0389** | 0.0177 | ±0.0355 | **+2.192** | **0.0284** | 1.0396 | * |
| Hypertension | +0.3261 | 0.2523 | ±0.5047 | +1.292 | 0.1963 | 1.3855 |  |
| High cholesterol | +0.1168 | 0.2399 | ±0.4797 | +0.487 | 0.6264 | 1.1239 |  |
| Kidney disease | -0.7092 | 0.5396 | ±1.0792 | -1.314 | 0.1887 | 0.4920 |  |
| Circulatory disease | +0.5437 | 0.3566 | ±0.7131 | +1.525 | 0.1273 | 1.7224 |  |
| Avg. daily time < 54 (%) | -2.0339 | 3.1209 | ±6.2417 | -0.652 | 0.5146 | 0.1308 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0870**, LLR χ² = **43.03** (p = **1.07e-05**), AUC = **0.6881**, AIC = **475.5**, BIC = **523.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.9491** | 0.9492 | ±1.8985 | **-4.160** | **3.18e-05** | 0.0193 | *** |
| **Education: graduate level (vs college)** | **-0.7671** | 0.2466 | ±0.4932 | **-3.111** | **0.0019** | 0.4644 | ** |
| Education: high school or below (vs college) | +0.4499 | 0.3939 | ±0.7878 | +1.142 | 0.2533 | 1.5682 |  |
| Site: UCSD (vs UAB) | +0.5220 | 0.2968 | ±0.5936 | +1.759 | 0.0786 | 1.6855 | . |
| Site: UW (vs UAB) | +0.4115 | 0.3049 | ±0.6098 | +1.349 | 0.1772 | 1.5090 |  |
| **Age (years)** | **+0.0334** | 0.0107 | ±0.0214 | **+3.123** | **0.0018** | 1.0340 | ** |
| **BMI (kg/m2)** | **+0.0384** | 0.0177 | ±0.0355 | **+2.162** | **0.0306** | 1.0391 | * |
| Hypertension | +0.2937 | 0.2531 | ±0.5062 | +1.161 | 0.2458 | 1.3414 |  |
| High cholesterol | +0.1620 | 0.2424 | ±0.4848 | +0.668 | 0.5041 | 1.1758 |  |
| Kidney disease | -0.7458 | 0.5391 | ±1.0782 | -1.383 | 0.1665 | 0.4743 |  |
| Circulatory disease | +0.5077 | 0.3525 | ±0.7049 | +1.440 | 0.1498 | 1.6614 |  |
| Time 54-69, pooled (%) | -0.9390 | 0.6808 | ±1.3617 | -1.379 | 0.1678 | 0.3910 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0880**, LLR χ² = **43.51** (p = **8.87e-06**), AUC = **0.6895**, AIC = **475.1**, BIC = **522.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.9671** | 0.9492 | ±1.8985 | **-4.179** | **2.93e-05** | 0.0189 | *** |
| **Education: graduate level (vs college)** | **-0.7773** | 0.2473 | ±0.4946 | **-3.144** | **0.0017** | 0.4596 | ** |
| Education: high school or below (vs college) | +0.4531 | 0.3946 | ±0.7892 | +1.148 | 0.2509 | 1.5731 |  |
| Site: UCSD (vs UAB) | +0.5368 | 0.2965 | ±0.5929 | +1.811 | 0.0702 | 1.7105 | . |
| Site: UW (vs UAB) | +0.4292 | 0.3045 | ±0.6089 | +1.410 | 0.1587 | 1.5360 |  |
| **Age (years)** | **+0.0337** | 0.0107 | ±0.0214 | **+3.143** | **0.0017** | 1.0342 | ** |
| **BMI (kg/m2)** | **+0.0384** | 0.0177 | ±0.0355 | **+2.161** | **0.0307** | 1.0391 | * |
| Hypertension | +0.2664 | 0.2548 | ±0.5096 | +1.045 | 0.2958 | 1.3053 |  |
| High cholesterol | +0.1550 | 0.2417 | ±0.4835 | +0.641 | 0.5215 | 1.1676 |  |
| Kidney disease | -0.7544 | 0.5407 | ±1.0814 | -1.395 | 0.1630 | 0.4703 |  |
| Circulatory disease | +0.5255 | 0.3530 | ±0.7061 | +1.489 | 0.1366 | 1.6914 |  |
| Avg. daily time 54-69 (%) | -1.0674 | 0.7000 | ±1.4000 | -1.525 | 0.1273 | 0.3439 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0873**, LLR χ² = **43.16** (p = **1.02e-05**), AUC = **0.6884**, AIC = **475.4**, BIC = **523.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.9495** | 0.9499 | ±1.8999 | **-4.158** | **3.22e-05** | 0.0193 | *** |
| **Education: graduate level (vs college)** | **-0.7690** | 0.2468 | ±0.4937 | **-3.115** | **0.0018** | 0.4635 | ** |
| Education: high school or below (vs college) | +0.4382 | 0.3937 | ±0.7874 | +1.113 | 0.2657 | 1.5500 |  |
| Site: UCSD (vs UAB) | +0.5111 | 0.2972 | ±0.5943 | +1.720 | 0.0854 | 1.6672 | . |
| Site: UW (vs UAB) | +0.4089 | 0.3051 | ±0.6103 | +1.340 | 0.1802 | 1.5052 |  |
| **Age (years)** | **+0.0333** | 0.0107 | ±0.0214 | **+3.114** | **0.0018** | 1.0339 | ** |
| **BMI (kg/m2)** | **+0.0388** | 0.0178 | ±0.0355 | **+2.185** | **0.0289** | 1.0396 | * |
| Hypertension | +0.3023 | 0.2528 | ±0.5056 | +1.196 | 0.2318 | 1.3530 |  |
| High cholesterol | +0.1585 | 0.2421 | ±0.4842 | +0.655 | 0.5128 | 1.1717 |  |
| Kidney disease | -0.7511 | 0.5393 | ±1.0786 | -1.393 | 0.1637 | 0.4719 |  |
| Circulatory disease | +0.5197 | 0.3526 | ±0.7051 | +1.474 | 0.1405 | 1.6815 |  |
| Time < 70 (%) | -0.8622 | 0.6067 | ±1.2134 | -1.421 | 0.1553 | 0.4222 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0879**, LLR χ² = **43.47** (p = **9.01e-06**), AUC = **0.6890**, AIC = **475.1**, BIC = **522.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.9742** | 0.9492 | ±1.8984 | **-4.187** | **2.83e-05** | 0.0188 | *** |
| **Education: graduate level (vs college)** | **-0.7745** | 0.2472 | ±0.4944 | **-3.133** | **0.0017** | 0.4610 | ** |
| Education: high school or below (vs college) | +0.4464 | 0.3944 | ±0.7889 | +1.132 | 0.2577 | 1.5627 |  |
| Site: UCSD (vs UAB) | +0.5330 | 0.2965 | ±0.5930 | +1.798 | 0.0722 | 1.7040 | . |
| Site: UW (vs UAB) | +0.4305 | 0.3046 | ±0.6092 | +1.413 | 0.1575 | 1.5381 |  |
| **Age (years)** | **+0.0336** | 0.0107 | ±0.0214 | **+3.135** | **0.0017** | 1.0342 | ** |
| **BMI (kg/m2)** | **+0.0386** | 0.0178 | ±0.0355 | **+2.173** | **0.0298** | 1.0394 | * |
| Hypertension | +0.2736 | 0.2545 | ±0.5089 | +1.075 | 0.2823 | 1.3147 |  |
| High cholesterol | +0.1509 | 0.2415 | ±0.4831 | +0.625 | 0.5322 | 1.1628 |  |
| Kidney disease | -0.7534 | 0.5405 | ±1.0811 | -1.394 | 0.1633 | 0.4707 |  |
| Circulatory disease | +0.5390 | 0.3534 | ±0.7068 | +1.525 | 0.1272 | 1.7144 |  |
| Avg. daily time < 70 (%) | -0.9545 | 0.6314 | ±1.2627 | -1.512 | 0.1306 | 0.3850 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0845**, LLR χ² = **41.79** (p = **1.76e-05**), AUC = **0.6831**, AIC = **476.8**, BIC = **524.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -213.6379 | 254.2159 | ±508.4318 | -0.840 | 0.4007 | 0.0000 |  |
| **Education: graduate level (vs college)** | **-0.7501** | 0.2459 | ±0.4917 | **-3.051** | **0.0023** | 0.4723 | ** |
| Education: high school or below (vs college) | +0.4041 | 0.3930 | ±0.7859 | +1.028 | 0.3038 | 1.4979 |  |
| Site: UCSD (vs UAB) | +0.5085 | 0.2975 | ±0.5951 | +1.709 | 0.0874 | 1.6628 | . |
| Site: UW (vs UAB) | +0.4284 | 0.3044 | ±0.6088 | +1.407 | 0.1593 | 1.5348 |  |
| **Age (years)** | **+0.0326** | 0.0107 | ±0.0213 | **+3.055** | **0.0022** | 1.0331 | ** |
| **BMI (kg/m2)** | **+0.0394** | 0.0178 | ±0.0356 | **+2.215** | **0.0268** | 1.0402 | * |
| Hypertension | +0.3373 | 0.2529 | ±0.5057 | +1.334 | 0.1822 | 1.4012 |  |
| High cholesterol | +0.1193 | 0.2400 | ±0.4800 | +0.497 | 0.6192 | 1.1267 |  |
| Kidney disease | -0.7209 | 0.5401 | ±1.0802 | -1.335 | 0.1820 | 0.4863 |  |
| Circulatory disease | +0.5397 | 0.3548 | ±0.7097 | +1.521 | 0.1282 | 1.7155 |  |
| Time 54-250, pooled (%) | +2.0961 | 2.5424 | ±5.0847 | +0.824 | 0.4097 | 8.1345 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0842**, LLR χ² = **41.62** (p = **1.88e-05**), AUC = **0.6823**, AIC = **477.0**, BIC = **524.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -228.5139 | 313.1377 | ±626.2755 | -0.730 | 0.4655 | 0.0000 |  |
| **Education: graduate level (vs college)** | **-0.7432** | 0.2454 | ±0.4909 | **-3.028** | **0.0025** | 0.4756 | ** |
| Education: high school or below (vs college) | +0.4184 | 0.3924 | ±0.7849 | +1.066 | 0.2864 | 1.5195 |  |
| Site: UCSD (vs UAB) | +0.5280 | 0.2960 | ±0.5919 | +1.784 | 0.0745 | 1.6955 | . |
| Site: UW (vs UAB) | +0.4403 | 0.3043 | ±0.6085 | +1.447 | 0.1479 | 1.5531 |  |
| **Age (years)** | **+0.0327** | 0.0107 | ±0.0213 | **+3.069** | **0.0021** | 1.0333 | ** |
| **BMI (kg/m2)** | **+0.0388** | 0.0177 | ±0.0354 | **+2.190** | **0.0285** | 1.0396 | * |
| Hypertension | +0.3257 | 0.2523 | ±0.5047 | +1.291 | 0.1968 | 1.3851 |  |
| High cholesterol | +0.1185 | 0.2399 | ±0.4799 | +0.494 | 0.6214 | 1.1258 |  |
| Kidney disease | -0.7103 | 0.5395 | ±1.0790 | -1.317 | 0.1880 | 0.4915 |  |
| Circulatory disease | +0.5470 | 0.3566 | ±0.7131 | +1.534 | 0.1250 | 1.7280 |  |
| Avg. daily time 54-250 (%) | +2.2447 | 3.1314 | ±6.2628 | +0.717 | 0.4735 | 9.4378 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0874**, LLR χ² = **43.22** (p = **9.94e-06**), AUC = **0.6871**, AIC = **475.4**, BIC = **523.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.3780** | 0.9859 | ±1.9719 | **-4.440** | **8.98e-06** | 0.0126 | *** |
| **Education: graduate level (vs college)** | **-0.7466** | 0.2458 | ±0.4917 | **-3.037** | **0.0024** | 0.4740 | ** |
| Education: high school or below (vs college) | +0.4447 | 0.3926 | ±0.7851 | +1.133 | 0.2573 | 1.5600 |  |
| Site: UCSD (vs UAB) | +0.5399 | 0.2965 | ±0.5930 | +1.821 | 0.0686 | 1.7159 | . |
| Site: UW (vs UAB) | +0.4337 | 0.3043 | ±0.6086 | +1.425 | 0.1541 | 1.5430 |  |
| **Age (years)** | **+0.0337** | 0.0107 | ±0.0215 | **+3.138** | **0.0017** | 1.0342 | ** |
| **BMI (kg/m2)** | **+0.0416** | 0.0183 | ±0.0365 | **+2.277** | **0.0228** | 1.0424 | * |
| Hypertension | +0.2981 | 0.2532 | ±0.5064 | +1.177 | 0.2391 | 1.3473 |  |
| High cholesterol | +0.1311 | 0.2407 | ±0.4813 | +0.545 | 0.5860 | 1.1400 |  |
| Kidney disease | -0.7821 | 0.5439 | ±1.0878 | -1.438 | 0.1504 | 0.4574 |  |
| Circulatory disease | +0.5083 | 0.3539 | ±0.7078 | +1.436 | 0.1509 | 1.6625 |  |
| Time 181-250, pooled (%) | +0.6110 | 0.4154 | ±0.8308 | +1.471 | 0.1413 | 1.8422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0871**, LLR χ² = **43.08** (p = **1.05e-05**), AUC = **0.6871**, AIC = **475.5**, BIC = **523.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.3166** | 0.9681 | ±1.9363 | **-4.459** | **8.25e-06** | 0.0133 | *** |
| **Education: graduate level (vs college)** | **-0.7546** | 0.2460 | ±0.4920 | **-3.068** | **0.0022** | 0.4702 | ** |
| Education: high school or below (vs college) | +0.4570 | 0.3933 | ±0.7865 | +1.162 | 0.2452 | 1.5793 |  |
| Site: UCSD (vs UAB) | +0.5445 | 0.2964 | ±0.5928 | +1.837 | 0.0662 | 1.7237 | . |
| Site: UW (vs UAB) | +0.4317 | 0.3044 | ±0.6087 | +1.418 | 0.1560 | 1.5399 |  |
| **Age (years)** | **+0.0341** | 0.0107 | ±0.0215 | **+3.176** | **0.0015** | 1.0347 | ** |
| **BMI (kg/m2)** | **+0.0396** | 0.0178 | ±0.0357 | **+2.220** | **0.0264** | 1.0404 | * |
| Hypertension | +0.3015 | 0.2532 | ±0.5063 | +1.191 | 0.2336 | 1.3519 |  |
| High cholesterol | +0.1161 | 0.2405 | ±0.4811 | +0.483 | 0.6293 | 1.1231 |  |
| Kidney disease | -0.7370 | 0.5403 | ±1.0806 | -1.364 | 0.1725 | 0.4785 |  |
| Circulatory disease | +0.5061 | 0.3537 | ±0.7075 | +1.431 | 0.1525 | 1.6589 |  |
| Avg. daily time 181-250 (%) | +0.5847 | 0.4104 | ±0.8207 | +1.425 | 0.1542 | 1.7944 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0873**, LLR χ² = **43.19** (p = **1.01e-05**), AUC = **0.6868**, AIC = **475.4**, BIC = **523.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.3774** | 0.9861 | ±1.9722 | **-4.439** | **9.04e-06** | 0.0126 | *** |
| **Education: graduate level (vs college)** | **-0.7462** | 0.2458 | ±0.4916 | **-3.036** | **0.0024** | 0.4742 | ** |
| Education: high school or below (vs college) | +0.4449 | 0.3926 | ±0.7851 | +1.133 | 0.2571 | 1.5603 |  |
| Site: UCSD (vs UAB) | +0.5400 | 0.2965 | ±0.5930 | +1.821 | 0.0686 | 1.7160 | . |
| Site: UW (vs UAB) | +0.4334 | 0.3043 | ±0.6086 | +1.424 | 0.1543 | 1.5425 |  |
| **Age (years)** | **+0.0337** | 0.0107 | ±0.0215 | **+3.139** | **0.0017** | 1.0343 | ** |
| **BMI (kg/m2)** | **+0.0416** | 0.0183 | ±0.0365 | **+2.277** | **0.0228** | 1.0424 | * |
| Hypertension | +0.2985 | 0.2532 | ±0.5064 | +1.179 | 0.2385 | 1.3478 |  |
| High cholesterol | +0.1305 | 0.2406 | ±0.4813 | +0.542 | 0.5877 | 1.1394 |  |
| Kidney disease | -0.7814 | 0.5439 | ±1.0878 | -1.437 | 0.1508 | 0.4578 |  |
| Circulatory disease | +0.5084 | 0.3539 | ±0.7078 | +1.436 | 0.1509 | 1.6626 |  |
| Time > 180 (%) | +0.6062 | 0.4151 | ±0.8303 | +1.460 | 0.1442 | 1.8335 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0870**, LLR χ² = **43.05** (p = **1.07e-05**), AUC = **0.6868**, AIC = **475.5**, BIC = **523.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.3162** | 0.9684 | ±1.9367 | **-4.457** | **8.30e-06** | 0.0134 | *** |
| **Education: graduate level (vs college)** | **-0.7541** | 0.2460 | ±0.4919 | **-3.066** | **0.0022** | 0.4705 | ** |
| Education: high school or below (vs college) | +0.4570 | 0.3933 | ±0.7865 | +1.162 | 0.2452 | 1.5794 |  |
| Site: UCSD (vs UAB) | +0.5445 | 0.2964 | ±0.5927 | +1.837 | 0.0662 | 1.7237 | . |
| Site: UW (vs UAB) | +0.4314 | 0.3044 | ±0.6087 | +1.418 | 0.1563 | 1.5395 |  |
| **Age (years)** | **+0.0341** | 0.0107 | ±0.0215 | **+3.177** | **0.0015** | 1.0347 | ** |
| **BMI (kg/m2)** | **+0.0396** | 0.0178 | ±0.0357 | **+2.220** | **0.0264** | 1.0404 | * |
| Hypertension | +0.3019 | 0.2531 | ±0.5063 | +1.193 | 0.2330 | 1.3524 |  |
| High cholesterol | +0.1156 | 0.2405 | ±0.4810 | +0.481 | 0.6308 | 1.1225 |  |
| Kidney disease | -0.7366 | 0.5403 | ±1.0806 | -1.363 | 0.1728 | 0.4787 |  |
| Circulatory disease | +0.5062 | 0.3537 | ±0.7074 | +1.431 | 0.1524 | 1.6590 |  |
| Avg. daily time > 180 (%) | +0.5792 | 0.4100 | ±0.8199 | +1.413 | 0.1577 | 1.7847 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 393)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **393**, events = **127**, McFadden pseudo-R² = **0.0853**, LLR χ² = **42.17** (p = **1.51e-05**), AUC = **0.6854**, AIC = **476.4**, BIC = **524.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.1680** | 0.9478 | ±1.8956 | **-4.398** | **1.09e-05** | 0.0155 | *** |
| **Education: graduate level (vs college)** | **-0.7270** | 0.2456 | ±0.4913 | **-2.960** | **0.0031** | 0.4833 | ** |
| Education: high school or below (vs college) | +0.4289 | 0.3923 | ±0.7847 | +1.093 | 0.2743 | 1.5356 |  |
| Site: UCSD (vs UAB) | +0.5534 | 0.2960 | ±0.5920 | +1.870 | 0.0615 | 1.7392 | . |
| Site: UW (vs UAB) | +0.4330 | 0.3042 | ±0.6084 | +1.423 | 0.1546 | 1.5418 |  |
| **Age (years)** | **+0.0350** | 0.0109 | ±0.0218 | **+3.214** | **0.0013** | 1.0356 | ** |
| **BMI (kg/m2)** | **+0.0363** | 0.0177 | ±0.0353 | **+2.056** | **0.0398** | 1.0370 | * |
| Hypertension | +0.3065 | 0.2528 | ±0.5056 | +1.212 | 0.2253 | 1.3586 |  |
| High cholesterol | +0.1062 | 0.2402 | ±0.4804 | +0.442 | 0.6583 | 1.1121 |  |
| Kidney disease | -0.7117 | 0.5384 | ±1.0768 | -1.322 | 0.1862 | 0.4908 |  |
| Circulatory disease | +0.5163 | 0.3535 | ±0.7070 | +1.460 | 0.1442 | 1.6758 |  |
| Nocturnal time > 180 (%) | +0.3577 | 0.3336 | ±0.6673 | +1.072 | 0.2837 | 1.4300 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 393; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **393**, R² = **0.0913**, Adj R² = **0.0675**, F-statistic = **3.84** (p = **5.78e-05**), Residual SE = **2.570** on **382** df, AIC = **1868.0**, BIC = **1911.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9541** | 1.0969 | ±2.1937 | **+15.457** | **6.78e-54** | *** |
| Education: graduate level (vs college) | +0.3859 | 0.2794 | ±0.5589 | +1.381 | 0.1672 |  |
| Education: high school or below (vs college) | -0.8815 | 0.6194 | ±1.2387 | -1.423 | 0.1547 |  |
| Site: UCSD (vs UAB) | -0.3739 | 0.3374 | ±0.6749 | -1.108 | 0.2678 |  |
| Site: UW (vs UAB) | -0.2089 | 0.3538 | ±0.7077 | -0.590 | 0.5550 |  |
| **Age (years)** | **-0.0446** | 0.0132 | ±0.0265 | **-3.369** | **7.55e-04** | *** |
| **BMI (kg/m2)** | **-0.0397** | 0.0186 | ±0.0371 | **-2.139** | **0.0325** | * |
| Hypertension | -0.4810 | 0.3276 | ±0.6551 | -1.468 | 0.1420 |  |
| High cholesterol | -0.0953 | 0.2958 | ±0.5917 | -0.322 | 0.7473 |  |
| Kidney disease | -0.0616 | 0.7623 | ±1.5247 | -0.081 | 0.9356 |  |
| Circulatory disease | -0.2210 | 0.4616 | ±0.9231 | -0.479 | 0.6321 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **393**, R² = **0.0914**, Adj R² = **0.0651**, F-statistic = **3.48** (p = **1.18e-04**), Residual SE = **2.573** on **381** df, AIC = **1869.9**, BIC = **1917.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.5491** | 3.0526 | ±6.1052 | **+5.421** | **5.92e-08** | *** |
| Education: graduate level (vs college) | +0.3864 | 0.2806 | ±0.5613 | +1.377 | 0.1685 |  |
| Education: high school or below (vs college) | -0.8836 | 0.6238 | ±1.2477 | -1.416 | 0.1567 |  |
| Site: UCSD (vs UAB) | -0.3720 | 0.3378 | ±0.6756 | -1.101 | 0.2708 |  |
| Site: UW (vs UAB) | -0.2055 | 0.3547 | ±0.7094 | -0.579 | 0.5623 |  |
| **Age (years)** | **-0.0448** | 0.0135 | ±0.0270 | **-3.320** | **9.00e-04** | *** |
| **BMI (kg/m2)** | **-0.0400** | 0.0183 | ±0.0366 | **-2.189** | **0.0286** | * |
| Hypertension | -0.4852 | 0.3263 | ±0.6525 | -1.487 | 0.1370 |  |
| High cholesterol | -0.1041 | 0.2946 | ±0.5893 | -0.353 | 0.7237 |  |
| Kidney disease | -0.0551 | 0.7714 | ±1.5427 | -0.071 | 0.9430 |  |
| Circulatory disease | -0.2182 | 0.4666 | ±0.9333 | -0.468 | 0.6400 |  |
| HbA1c (%) | +0.0776 | 0.5312 | ±1.0624 | +0.146 | 0.8838 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **393**, R² = **0.0926**, Adj R² = **0.0664**, F-statistic = **3.54** (p = **9.62e-05**), Residual SE = **2.571** on **381** df, AIC = **1869.4**, BIC = **1917.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.4193** | 2.2992 | ±4.5984 | **+8.011** | **1.14e-15** | *** |
| Education: graduate level (vs college) | +0.3901 | 0.2804 | ±0.5607 | +1.392 | 0.1641 |  |
| Education: high school or below (vs college) | -0.8887 | 0.6193 | ±1.2386 | -1.435 | 0.1513 |  |
| Site: UCSD (vs UAB) | -0.3599 | 0.3384 | ±0.6768 | -1.063 | 0.2876 |  |
| Site: UW (vs UAB) | -0.1928 | 0.3518 | ±0.7036 | -0.548 | 0.5837 |  |
| **Age (years)** | **-0.0449** | 0.0132 | ±0.0264 | **-3.402** | **6.70e-04** | *** |
| **BMI (kg/m2)** | **-0.0387** | 0.0185 | ±0.0371 | **-2.086** | **0.0370** | * |
| Hypertension | -0.4668 | 0.3298 | ±0.6595 | -1.416 | 0.1569 |  |
| High cholesterol | -0.1061 | 0.2983 | ±0.5966 | -0.356 | 0.7221 |  |
| Kidney disease | -0.0465 | 0.7641 | ±1.5282 | -0.061 | 0.9515 |  |
| Circulatory disease | -0.2178 | 0.4608 | ±0.9217 | -0.473 | 0.6365 |  |
| Mean glucose (mg/dL) | -0.0130 | 0.0180 | ±0.0361 | -0.723 | 0.4698 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **393**, R² = **0.0926**, Adj R² = **0.0664**, F-statistic = **3.54** (p = **9.62e-05**), Residual SE = **2.571** on **381** df, AIC = **1869.4**, BIC = **1917.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20.2232** | 4.6472 | ±9.2945 | **+4.352** | **1.35e-05** | *** |
| Education: graduate level (vs college) | +0.3901 | 0.2804 | ±0.5607 | +1.392 | 0.1641 |  |
| Education: high school or below (vs college) | -0.8887 | 0.6193 | ±1.2386 | -1.435 | 0.1513 |  |
| Site: UCSD (vs UAB) | -0.3599 | 0.3384 | ±0.6768 | -1.063 | 0.2876 |  |
| Site: UW (vs UAB) | -0.1928 | 0.3518 | ±0.7036 | -0.548 | 0.5837 |  |
| **Age (years)** | **-0.0449** | 0.0132 | ±0.0264 | **-3.402** | **6.70e-04** | *** |
| **BMI (kg/m2)** | **-0.0387** | 0.0185 | ±0.0371 | **-2.086** | **0.0370** | * |
| Hypertension | -0.4668 | 0.3298 | ±0.6595 | -1.416 | 0.1569 |  |
| High cholesterol | -0.1061 | 0.2983 | ±0.5966 | -0.356 | 0.7221 |  |
| Kidney disease | -0.0465 | 0.7641 | ±1.5282 | -0.061 | 0.9515 |  |
| Circulatory disease | -0.2178 | 0.4608 | ±0.9217 | -0.473 | 0.6365 |  |
| GMI (%) | -0.5450 | 0.7539 | ±1.5078 | -0.723 | 0.4698 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **393**, R² = **0.0920**, Adj R² = **0.0658**, F-statistic = **3.51** (p = **1.07e-04**), Residual SE = **2.572** on **381** df, AIC = **1869.7**, BIC = **1917.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.8159** | 1.9217 | ±3.8434 | **+9.271** | **1.85e-20** | *** |
| Education: graduate level (vs college) | +0.3807 | 0.2803 | ±0.5606 | +1.358 | 0.1745 |  |
| Education: high school or below (vs college) | -0.8921 | 0.6219 | ±1.2438 | -1.434 | 0.1514 |  |
| Site: UCSD (vs UAB) | -0.3557 | 0.3390 | ±0.6780 | -1.049 | 0.2941 |  |
| Site: UW (vs UAB) | -0.1930 | 0.3524 | ±0.7049 | -0.548 | 0.5840 |  |
| **Age (years)** | **-0.0455** | 0.0131 | ±0.0262 | **-3.475** | **5.11e-04** | *** |
| **BMI (kg/m2)** | **-0.0380** | 0.0188 | ±0.0376 | **-2.019** | **0.0435** | * |
| Hypertension | -0.4758 | 0.3288 | ±0.6576 | -1.447 | 0.1478 |  |
| High cholesterol | -0.0971 | 0.2975 | ±0.5950 | -0.326 | 0.7442 |  |
| Kidney disease | -0.0639 | 0.7667 | ±1.5333 | -0.083 | 0.9336 |  |
| Circulatory disease | -0.2216 | 0.4625 | ±0.9249 | -0.479 | 0.6318 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0075 | 0.0146 | ±0.0291 | -0.517 | 0.6049 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **393**, R² = **0.0914**, Adj R² = **0.0651**, F-statistic = **3.48** (p = **1.18e-04**), Residual SE = **2.573** on **381** df, AIC = **1869.9**, BIC = **1917.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.7647** | 1.4081 | ±2.8162 | **+11.906** | **1.10e-32** | *** |
| Education: graduate level (vs college) | +0.3897 | 0.2812 | ±0.5623 | +1.386 | 0.1658 |  |
| Education: high school or below (vs college) | -0.8819 | 0.6207 | ±1.2415 | -1.421 | 0.1554 |  |
| Site: UCSD (vs UAB) | -0.3684 | 0.3380 | ±0.6761 | -1.090 | 0.2758 |  |
| Site: UW (vs UAB) | -0.2054 | 0.3539 | ±0.7079 | -0.580 | 0.5616 |  |
| **Age (years)** | **-0.0446** | 0.0133 | ±0.0265 | **-3.361** | **7.76e-04** | *** |
| **BMI (kg/m2)** | **-0.0399** | 0.0186 | ±0.0373 | **-2.138** | **0.0325** | * |
| Hypertension | -0.4818 | 0.3280 | ±0.6560 | -1.469 | 0.1418 |  |
| High cholesterol | -0.0924 | 0.2977 | ±0.5954 | -0.310 | 0.7562 |  |
| Kidney disease | -0.0686 | 0.7645 | ±1.5291 | -0.090 | 0.9285 |  |
| Circulatory disease | -0.2227 | 0.4625 | ±0.9249 | -0.481 | 0.6302 |  |
| Glucose SD, pooled (mg/dL) | +0.0113 | 0.0558 | ±0.1117 | +0.202 | 0.8397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **393**, R² = **0.0920**, Adj R² = **0.0658**, F-statistic = **3.51** (p = **1.06e-04**), Residual SE = **2.572** on **381** df, AIC = **1869.6**, BIC = **1917.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4556** | 1.3275 | ±2.6550 | **+12.396** | **2.74e-35** | *** |
| Education: graduate level (vs college) | +0.3970 | 0.2818 | ±0.5636 | +1.409 | 0.1589 |  |
| Education: high school or below (vs college) | -0.8790 | 0.6223 | ±1.2445 | -1.413 | 0.1578 |  |
| Site: UCSD (vs UAB) | -0.3559 | 0.3369 | ±0.6739 | -1.056 | 0.2908 |  |
| Site: UW (vs UAB) | -0.1981 | 0.3524 | ±0.7048 | -0.562 | 0.5739 |  |
| **Age (years)** | **-0.0446** | 0.0132 | ±0.0265 | **-3.363** | **7.70e-04** | *** |
| **BMI (kg/m2)** | **-0.0406** | 0.0187 | ±0.0374 | **-2.171** | **0.0300** | * |
| Hypertension | -0.4797 | 0.3291 | ±0.6582 | -1.458 | 0.1450 |  |
| High cholesterol | -0.0885 | 0.2974 | ±0.5949 | -0.297 | 0.7662 |  |
| Kidney disease | -0.0817 | 0.7635 | ±1.5270 | -0.107 | 0.9148 |  |
| Circulatory disease | -0.2229 | 0.4643 | ±0.9286 | -0.480 | 0.6311 |  |
| Avg. daily SD (mg/dL) | +0.0329 | 0.0544 | ±0.1089 | +0.605 | 0.5451 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **393**, R² = **0.0917**, Adj R² = **0.0655**, F-statistic = **3.50** (p = **1.11e-04**), Residual SE = **2.572** on **381** df, AIC = **1869.8**, BIC = **1917.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.5384** | 1.4297 | ±2.8595 | **+11.567** | **6.02e-31** | *** |
| Education: graduate level (vs college) | +0.3953 | 0.2815 | ±0.5630 | +1.404 | 0.1603 |  |
| Education: high school or below (vs college) | -0.8842 | 0.6211 | ±1.2422 | -1.424 | 0.1546 |  |
| Site: UCSD (vs UAB) | -0.3583 | 0.3378 | ±0.6755 | -1.061 | 0.2888 |  |
| Site: UW (vs UAB) | -0.1969 | 0.3522 | ±0.7043 | -0.559 | 0.5760 |  |
| **Age (years)** | **-0.0446** | 0.0133 | ±0.0265 | **-3.368** | **7.57e-04** | *** |
| **BMI (kg/m2)** | **-0.0398** | 0.0186 | ±0.0372 | **-2.139** | **0.0324** | * |
| Hypertension | -0.4791 | 0.3292 | ±0.6584 | -1.455 | 0.1456 |  |
| High cholesterol | -0.0914 | 0.2974 | ±0.5947 | -0.307 | 0.7585 |  |
| Kidney disease | -0.0722 | 0.7641 | ±1.5282 | -0.094 | 0.9248 |  |
| Circulatory disease | -0.2242 | 0.4633 | ±0.9266 | -0.484 | 0.6285 |  |
| CV (%) | +0.0277 | 0.0636 | ±0.1273 | +0.436 | 0.6631 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **393**, R² = **0.0921**, Adj R² = **0.0659**, F-statistic = **3.51** (p = **1.05e-04**), Residual SE = **2.572** on **381** df, AIC = **1869.6**, BIC = **1917.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.4650** | 1.4449 | ±2.8897 | **+12.088** | **1.23e-33** | *** |
| Education: graduate level (vs college) | +0.3998 | 0.2818 | ±0.5635 | +1.419 | 0.1559 |  |
| Education: high school or below (vs college) | -0.8850 | 0.6213 | ±1.2426 | -1.424 | 0.1543 |  |
| Site: UCSD (vs UAB) | -0.3578 | 0.3372 | ±0.6744 | -1.061 | 0.2887 |  |
| Site: UW (vs UAB) | -0.1974 | 0.3525 | ±0.7050 | -0.560 | 0.5754 |  |
| **Age (years)** | **-0.0446** | 0.0132 | ±0.0265 | **-3.367** | **7.59e-04** | *** |
| **BMI (kg/m2)** | **-0.0398** | 0.0186 | ±0.0371 | **-2.142** | **0.0322** | * |
| Hypertension | -0.4813 | 0.3286 | ±0.6571 | -1.465 | 0.1429 |  |
| High cholesterol | -0.0894 | 0.2972 | ±0.5943 | -0.301 | 0.7636 |  |
| Kidney disease | -0.0710 | 0.7632 | ±1.5265 | -0.093 | 0.9258 |  |
| Circulatory disease | -0.2247 | 0.4634 | ±0.9268 | -0.485 | 0.6277 |  |
| Mean / SD ratio | -0.0755 | 0.1281 | ±0.2561 | -0.590 | 0.5554 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **393**, R² = **0.0924**, Adj R² = **0.0662**, F-statistic = **3.53** (p = **9.97e-05**), Residual SE = **2.572** on **381** df, AIC = **1869.5**, BIC = **1917.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.5250** | 1.3970 | ±2.7941 | **+12.544** | **4.26e-36** | *** |
| Education: graduate level (vs college) | +0.4025 | 0.2829 | ±0.5658 | +1.423 | 0.1548 |  |
| Education: high school or below (vs college) | -0.8816 | 0.6218 | ±1.2436 | -1.418 | 0.1562 |  |
| Site: UCSD (vs UAB) | -0.3519 | 0.3372 | ±0.6743 | -1.044 | 0.2966 |  |
| Site: UW (vs UAB) | -0.1958 | 0.3514 | ±0.7027 | -0.557 | 0.5773 |  |
| **Age (years)** | **-0.0446** | 0.0132 | ±0.0265 | **-3.369** | **7.54e-04** | *** |
| **BMI (kg/m2)** | **-0.0405** | 0.0187 | ±0.0374 | **-2.168** | **0.0302** | * |
| Hypertension | -0.4747 | 0.3298 | ±0.6596 | -1.439 | 0.1501 |  |
| High cholesterol | -0.0912 | 0.2970 | ±0.5941 | -0.307 | 0.7588 |  |
| Kidney disease | -0.0760 | 0.7622 | ±1.5245 | -0.100 | 0.9206 |  |
| Circulatory disease | -0.2224 | 0.4634 | ±0.9268 | -0.480 | 0.6313 |  |
| Avg. daily mean/SD | -0.0724 | 0.0998 | ±0.1996 | -0.725 | 0.4683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **393**, R² = **0.0940**, Adj R² = **0.0679**, F-statistic = **3.59** (p = **7.66e-05**), Residual SE = **2.569** on **381** df, AIC = **1868.8**, BIC = **1916.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.9401** | 1.3513 | ±2.7025 | **+13.276** | **3.17e-40** | *** |
| Education: graduate level (vs college) | +0.3884 | 0.2802 | ±0.5604 | +1.386 | 0.1657 |  |
| Education: high school or below (vs college) | -0.8449 | 0.6094 | ±1.2188 | -1.387 | 0.1656 |  |
| Site: UCSD (vs UAB) | -0.3955 | 0.3367 | ±0.6733 | -1.175 | 0.2400 |  |
| Site: UW (vs UAB) | -0.2495 | 0.3529 | ±0.7058 | -0.707 | 0.4796 |  |
| **Age (years)** | **-0.0462** | 0.0132 | ±0.0264 | **-3.495** | **4.74e-04** | *** |
| **BMI (kg/m2)** | **-0.0412** | 0.0184 | ±0.0368 | **-2.240** | **0.0251** | * |
| Hypertension | -0.4955 | 0.3292 | ±0.6583 | -1.505 | 0.1323 |  |
| High cholesterol | -0.0756 | 0.2978 | ±0.5955 | -0.254 | 0.7995 |  |
| Kidney disease | -0.0324 | 0.7655 | ±1.5309 | -0.042 | 0.9662 |  |
| Circulatory disease | -0.2221 | 0.4631 | ±0.9263 | -0.480 | 0.6315 |  |
| MAG (mg/dL/h) | -0.0244 | 0.0246 | ±0.0493 | -0.991 | 0.3217 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **393**, R² = **0.0913**, Adj R² = **0.0651**, F-statistic = **3.48** (p = **1.19e-04**), Residual SE = **2.573** on **381** df, AIC = **1869.9**, BIC = **1917.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.8309** | 1.3702 | ±2.7403 | **+12.284** | **1.11e-34** | *** |
| Education: graduate level (vs college) | +0.3870 | 0.2809 | ±0.5619 | +1.378 | 0.1683 |  |
| Education: high school or below (vs college) | -0.8812 | 0.6230 | ±1.2459 | -1.414 | 0.1572 |  |
| Site: UCSD (vs UAB) | -0.3707 | 0.3358 | ±0.6716 | -1.104 | 0.2696 |  |
| Site: UW (vs UAB) | -0.2065 | 0.3530 | ±0.7059 | -0.585 | 0.5585 |  |
| **Age (years)** | **-0.0445** | 0.0132 | ±0.0264 | **-3.370** | **7.52e-04** | *** |
| **BMI (kg/m2)** | **-0.0395** | 0.0185 | ±0.0370 | **-2.139** | **0.0324** | * |
| Hypertension | -0.4794 | 0.3291 | ±0.6582 | -1.457 | 0.1452 |  |
| High cholesterol | -0.0957 | 0.2963 | ±0.5926 | -0.323 | 0.7467 |  |
| Kidney disease | -0.0640 | 0.7638 | ±1.5277 | -0.084 | 0.9332 |  |
| Circulatory disease | -0.2219 | 0.4626 | ±0.9252 | -0.480 | 0.6315 |  |
| Avg. daily range (mg/dL) | +0.0014 | 0.0116 | ±0.0233 | +0.123 | 0.9022 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **393**, R² = **0.1026**, Adj R² = **0.0767**, F-statistic = **3.96** (p = **1.81e-05**), Residual SE = **2.557** on **381** df, AIC = **1865.0**, BIC = **1912.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.7082** | 1.1364 | ±2.2727 | **+15.583** | **9.44e-55** | *** |
| Education: graduate level (vs college) | +0.4061 | 0.2792 | ±0.5585 | +1.454 | 0.1458 |  |
| Education: high school or below (vs college) | -0.8220 | 0.6056 | ±1.2112 | -1.357 | 0.1747 |  |
| Site: UCSD (vs UAB) | -0.3896 | 0.3359 | ±0.6719 | -1.160 | 0.2461 |  |
| Site: UW (vs UAB) | -0.1782 | 0.3516 | ±0.7032 | -0.507 | 0.6123 |  |
| **Age (years)** | **-0.0441** | 0.0131 | ±0.0262 | **-3.370** | **7.51e-04** | *** |
| **BMI (kg/m2)** | **-0.0393** | 0.0186 | ±0.0373 | **-2.107** | **0.0351** | * |
| Hypertension | -0.4414 | 0.3318 | ±0.6636 | -1.330 | 0.1834 |  |
| High cholesterol | -0.0785 | 0.2936 | ±0.5872 | -0.267 | 0.7892 |  |
| Kidney disease | -0.1092 | 0.7519 | ±1.5038 | -0.145 | 0.8845 |  |
| Circulatory disease | -0.1839 | 0.4606 | ±0.9212 | -0.399 | 0.6898 |  |
| **SD of daily means (mg/dL)** | **-0.1639** | 0.0782 | ±0.1564 | **-2.096** | **0.0361** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **393**, R² = **0.0916**, Adj R² = **0.0654**, F-statistic = **3.49** (p = **1.13e-04**), Residual SE = **2.573** on **381** df, AIC = **1869.8**, BIC = **1917.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +33.9128 | 43.9642 | ±87.9284 | +0.771 | 0.4405 |  |
| Education: graduate level (vs college) | +0.3885 | 0.2799 | ±0.5599 | +1.388 | 0.1652 |  |
| Education: high school or below (vs college) | -0.8801 | 0.6218 | ±1.2436 | -1.415 | 0.1569 |  |
| Site: UCSD (vs UAB) | -0.3664 | 0.3338 | ±0.6676 | -1.098 | 0.2724 |  |
| Site: UW (vs UAB) | -0.2022 | 0.3522 | ±0.7044 | -0.574 | 0.5659 |  |
| **Age (years)** | **-0.0444** | 0.0132 | ±0.0263 | **-3.367** | **7.59e-04** | *** |
| **BMI (kg/m2)** | **-0.0392** | 0.0184 | ±0.0367 | **-2.136** | **0.0327** | * |
| Hypertension | -0.4829 | 0.3284 | ±0.6568 | -1.471 | 0.1414 |  |
| High cholesterol | -0.1003 | 0.2966 | ±0.5932 | -0.338 | 0.7353 |  |
| Kidney disease | -0.0722 | 0.7643 | ±1.5287 | -0.094 | 0.9247 |  |
| Circulatory disease | -0.2231 | 0.4629 | ±0.9257 | -0.482 | 0.6298 |  |
| Time in range 70-180, pooled (%) | -0.1707 | 0.4399 | ±0.8797 | -0.388 | 0.6980 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **393**, R² = **0.0919**, Adj R² = **0.0656**, F-statistic = **3.50** (p = **1.09e-04**), Residual SE = **2.572** on **381** df, AIC = **1869.7**, BIC = **1917.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +37.8171 | 41.3558 | ±82.7117 | +0.914 | 0.3605 |  |
| Education: graduate level (vs college) | +0.3887 | 0.2803 | ±0.5605 | +1.387 | 0.1654 |  |
| Education: high school or below (vs college) | -0.8768 | 0.6220 | ±1.2439 | -1.410 | 0.1586 |  |
| Site: UCSD (vs UAB) | -0.3686 | 0.3363 | ±0.6726 | -1.096 | 0.2731 |  |
| Site: UW (vs UAB) | -0.2080 | 0.3553 | ±0.7106 | -0.586 | 0.5582 |  |
| **Age (years)** | **-0.0441** | 0.0132 | ±0.0263 | **-3.351** | **8.04e-04** | *** |
| **BMI (kg/m2)** | **-0.0395** | 0.0185 | ±0.0371 | **-2.127** | **0.0334** | * |
| Hypertension | -0.4767 | 0.3281 | ±0.6561 | -1.453 | 0.1462 |  |
| High cholesterol | -0.1037 | 0.2966 | ±0.5933 | -0.350 | 0.7266 |  |
| Kidney disease | -0.0637 | 0.7683 | ±1.5365 | -0.083 | 0.9339 |  |
| Circulatory disease | -0.2292 | 0.4637 | ±0.9274 | -0.494 | 0.6210 |  |
| Avg. daily time in range 70-180 (%) | -0.2098 | 0.4137 | ±0.8274 | -0.507 | 0.6121 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **393**, R² = **0.0914**, Adj R² = **0.0651**, F-statistic = **3.48** (p = **1.18e-04**), Residual SE = **2.573** on **381** df, AIC = **1869.9**, BIC = **1917.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9404** | 1.0952 | ±2.1905 | **+15.467** | **5.78e-54** | *** |
| Education: graduate level (vs college) | +0.3872 | 0.2803 | ±0.5605 | +1.381 | 0.1671 |  |
| Education: high school or below (vs college) | -0.8790 | 0.6174 | ±1.2347 | -1.424 | 0.1545 |  |
| Site: UCSD (vs UAB) | -0.3641 | 0.3380 | ±0.6760 | -1.077 | 0.2814 |  |
| Site: UW (vs UAB) | -0.2024 | 0.3511 | ±0.7022 | -0.577 | 0.5642 |  |
| **Age (years)** | **-0.0446** | 0.0133 | ±0.0265 | **-3.361** | **7.76e-04** | *** |
| **BMI (kg/m2)** | **-0.0397** | 0.0187 | ±0.0373 | **-2.129** | **0.0332** | * |
| Hypertension | -0.4847 | 0.3259 | ±0.6517 | -1.488 | 0.1369 |  |
| High cholesterol | -0.0955 | 0.2969 | ±0.5939 | -0.322 | 0.7476 |  |
| Kidney disease | -0.0553 | 0.7711 | ±1.5423 | -0.072 | 0.9429 |  |
| Circulatory disease | -0.2237 | 0.4610 | ±0.9220 | -0.485 | 0.6275 |  |
| Any reading < 54 during wear (0/1) | +0.0602 | 0.3971 | ±0.7943 | +0.152 | 0.8796 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **393**, R² = **0.0918**, Adj R² = **0.0656**, F-statistic = **3.50** (p = **1.11e-04**), Residual SE = **2.572** on **381** df, AIC = **1869.8**, BIC = **1917.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9316** | 1.0978 | ±2.1956 | **+15.423** | **1.15e-53** | *** |
| Education: graduate level (vs college) | +0.3883 | 0.2800 | ±0.5600 | +1.387 | 0.1655 |  |
| Education: high school or below (vs college) | -0.8685 | 0.6182 | ±1.2364 | -1.405 | 0.1601 |  |
| Site: UCSD (vs UAB) | -0.3543 | 0.3381 | ±0.6762 | -1.048 | 0.2947 |  |
| Site: UW (vs UAB) | -0.1983 | 0.3536 | ±0.7072 | -0.561 | 0.5750 |  |
| **Age (years)** | **-0.0444** | 0.0132 | ±0.0265 | **-3.353** | **8.00e-04** | *** |
| **BMI (kg/m2)** | **-0.0403** | 0.0188 | ±0.0377 | **-2.140** | **0.0323** | * |
| Hypertension | -0.4909 | 0.3283 | ±0.6566 | -1.495 | 0.1349 |  |
| High cholesterol | -0.0941 | 0.2961 | ±0.5922 | -0.318 | 0.7506 |  |
| Kidney disease | -0.0492 | 0.7658 | ±1.5315 | -0.064 | 0.9488 |  |
| Circulatory disease | -0.2354 | 0.4603 | ±0.9207 | -0.511 | 0.6090 |  |
| Time < 54 (%) | +1.1843 | 2.1886 | ±4.3772 | +0.541 | 0.5884 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **393**, R² = **0.0916**, Adj R² = **0.0654**, F-statistic = **3.49** (p = **1.14e-04**), Residual SE = **2.573** on **381** df, AIC = **1869.8**, BIC = **1917.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9445** | 1.0997 | ±2.1994 | **+15.408** | **1.44e-53** | *** |
| Education: graduate level (vs college) | +0.3850 | 0.2803 | ±0.5605 | +1.374 | 0.1695 |  |
| Education: high school or below (vs college) | -0.8768 | 0.6187 | ±1.2373 | -1.417 | 0.1564 |  |
| Site: UCSD (vs UAB) | -0.3655 | 0.3380 | ±0.6760 | -1.082 | 0.2795 |  |
| Site: UW (vs UAB) | -0.2056 | 0.3549 | ±0.7098 | -0.579 | 0.5623 |  |
| **Age (years)** | **-0.0445** | 0.0132 | ±0.0265 | **-3.357** | **7.87e-04** | *** |
| **BMI (kg/m2)** | **-0.0400** | 0.0188 | ±0.0376 | **-2.131** | **0.0331** | * |
| Hypertension | -0.4850 | 0.3277 | ±0.6554 | -1.480 | 0.1388 |  |
| High cholesterol | -0.0942 | 0.2962 | ±0.5924 | -0.318 | 0.7505 |  |
| Kidney disease | -0.0553 | 0.7657 | ±1.5314 | -0.072 | 0.9424 |  |
| Circulatory disease | -0.2371 | 0.4583 | ±0.9166 | -0.517 | 0.6049 |  |
| Avg. daily time < 54 (%) | +1.1269 | 2.8842 | ±5.7685 | +0.391 | 0.6960 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **393**, R² = **0.0931**, Adj R² = **0.0669**, F-statistic = **3.55** (p = **8.94e-05**), Residual SE = **2.571** on **381** df, AIC = **1869.2**, BIC = **1916.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.0641** | 1.0818 | ±2.1636 | **+15.773** | **4.74e-56** | *** |
| Education: graduate level (vs college) | +0.3736 | 0.2807 | ±0.5614 | +1.331 | 0.1832 |  |
| Education: high school or below (vs college) | -0.8649 | 0.6245 | ±1.2489 | -1.385 | 0.1661 |  |
| Site: UCSD (vs UAB) | -0.3933 | 0.3313 | ±0.6626 | -1.187 | 0.2352 |  |
| Site: UW (vs UAB) | -0.2347 | 0.3439 | ±0.6878 | -0.682 | 0.4950 |  |
| **Age (years)** | **-0.0445** | 0.0133 | ±0.0266 | **-3.347** | **8.17e-04** | *** |
| **BMI (kg/m2)** | **-0.0401** | 0.0185 | ±0.0370 | **-2.166** | **0.0303** | * |
| Hypertension | -0.5036 | 0.3278 | ±0.6557 | -1.536 | 0.1245 |  |
| High cholesterol | -0.0662 | 0.2956 | ±0.5913 | -0.224 | 0.8228 |  |
| Kidney disease | -0.0960 | 0.7622 | ±1.5244 | -0.126 | 0.8998 |  |
| Circulatory disease | -0.2237 | 0.4633 | ±0.9266 | -0.483 | 0.6292 |  |
| Time 54-69, pooled (%) | -0.6381 | 0.8400 | ±1.6800 | -0.760 | 0.4475 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **393**, R² = **0.0915**, Adj R² = **0.0652**, F-statistic = **3.49** (p = **1.17e-04**), Residual SE = **2.573** on **381** df, AIC = **1869.9**, BIC = **1917.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9817** | 1.0863 | ±2.1725 | **+15.633** | **4.33e-55** | *** |
| Education: graduate level (vs college) | +0.3808 | 0.2817 | ±0.5634 | +1.352 | 0.1764 |  |
| Education: high school or below (vs college) | -0.8763 | 0.6241 | ±1.2482 | -1.404 | 0.1603 |  |
| Site: UCSD (vs UAB) | -0.3766 | 0.3360 | ±0.6720 | -1.121 | 0.2624 |  |
| Site: UW (vs UAB) | -0.2121 | 0.3510 | ±0.7020 | -0.604 | 0.5457 |  |
| **Age (years)** | **-0.0445** | 0.0133 | ±0.0266 | **-3.348** | **8.15e-04** | *** |
| **BMI (kg/m2)** | **-0.0398** | 0.0186 | ±0.0372 | **-2.142** | **0.0322** | * |
| Hypertension | -0.4924 | 0.3286 | ±0.6573 | -1.498 | 0.1340 |  |
| High cholesterol | -0.0888 | 0.2960 | ±0.5920 | -0.300 | 0.7642 |  |
| Kidney disease | -0.0712 | 0.7655 | ±1.5311 | -0.093 | 0.9259 |  |
| Circulatory disease | -0.2187 | 0.4633 | ±0.9265 | -0.472 | 0.6368 |  |
| Avg. daily time 54-69 (%) | -0.1953 | 0.7972 | ±1.5943 | -0.245 | 0.8064 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **393**, R² = **0.0923**, Adj R² = **0.0661**, F-statistic = **3.52** (p = **1.01e-04**), Residual SE = **2.572** on **381** df, AIC = **1869.5**, BIC = **1917.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.0372** | 1.0836 | ±2.1672 | **+15.723** | **1.06e-55** | *** |
| Education: graduate level (vs college) | +0.3767 | 0.2807 | ±0.5613 | +1.342 | 0.1796 |  |
| Education: high school or below (vs college) | -0.8750 | 0.6234 | ±1.2468 | -1.404 | 0.1605 |  |
| Site: UCSD (vs UAB) | -0.3943 | 0.3306 | ±0.6611 | -1.193 | 0.2330 |  |
| Site: UW (vs UAB) | -0.2303 | 0.3444 | ±0.6889 | -0.669 | 0.5037 |  |
| **Age (years)** | **-0.0446** | 0.0133 | ±0.0266 | **-3.357** | **7.88e-04** | *** |
| **BMI (kg/m2)** | **-0.0397** | 0.0185 | ±0.0371 | **-2.144** | **0.0321** | * |
| Hypertension | -0.4928 | 0.3278 | ±0.6557 | -1.503 | 0.1328 |  |
| High cholesterol | -0.0760 | 0.2961 | ±0.5923 | -0.257 | 0.7976 |  |
| Kidney disease | -0.0895 | 0.7637 | ±1.5274 | -0.117 | 0.9067 |  |
| Circulatory disease | -0.2175 | 0.4639 | ±0.9277 | -0.469 | 0.6391 |  |
| Time < 70 (%) | -0.4339 | 0.7395 | ±1.4791 | -0.587 | 0.5574 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **393**, R² = **0.0914**, Adj R² = **0.0651**, F-statistic = **3.48** (p = **1.19e-04**), Residual SE = **2.573** on **381** df, AIC = **1869.9**, BIC = **1917.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9702** | 1.0880 | ±2.1761 | **+15.597** | **7.61e-55** | *** |
| Education: graduate level (vs college) | +0.3832 | 0.2817 | ±0.5633 | +1.361 | 0.1736 |  |
| Education: high school or below (vs college) | -0.8791 | 0.6230 | ±1.2459 | -1.411 | 0.1582 |  |
| Site: UCSD (vs UAB) | -0.3762 | 0.3355 | ±0.6711 | -1.121 | 0.2622 |  |
| Site: UW (vs UAB) | -0.2109 | 0.3513 | ±0.7027 | -0.600 | 0.5482 |  |
| **Age (years)** | **-0.0445** | 0.0133 | ±0.0266 | **-3.353** | **7.99e-04** | *** |
| **BMI (kg/m2)** | **-0.0397** | 0.0186 | ±0.0372 | **-2.137** | **0.0326** | * |
| Hypertension | -0.4869 | 0.3287 | ±0.6574 | -1.481 | 0.1385 |  |
| High cholesterol | -0.0918 | 0.2965 | ±0.5929 | -0.310 | 0.7567 |  |
| Kidney disease | -0.0675 | 0.7665 | ±1.5330 | -0.088 | 0.9298 |  |
| Circulatory disease | -0.2182 | 0.4634 | ±0.9267 | -0.471 | 0.6377 |  |
| Avg. daily time < 70 (%) | -0.1070 | 0.7246 | ±1.4492 | -0.148 | 0.8826 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **393**, R² = **0.0918**, Adj R² = **0.0656**, F-statistic = **3.50** (p = **1.11e-04**), Residual SE = **2.572** on **381** df, AIC = **1869.8**, BIC = **1917.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +135.6054 | 217.1462 | ±434.2924 | +0.624 | 0.5323 |  |
| Education: graduate level (vs college) | +0.3892 | 0.2800 | ±0.5600 | +1.390 | 0.1645 |  |
| Education: high school or below (vs college) | -0.8677 | 0.6183 | ±1.2365 | -1.403 | 0.1605 |  |
| Site: UCSD (vs UAB) | -0.3542 | 0.3382 | ±0.6763 | -1.047 | 0.2950 |  |
| Site: UW (vs UAB) | -0.1990 | 0.3536 | ±0.7072 | -0.563 | 0.5737 |  |
| **Age (years)** | **-0.0443** | 0.0132 | ±0.0265 | **-3.349** | **8.11e-04** | *** |
| **BMI (kg/m2)** | **-0.0403** | 0.0188 | ±0.0376 | **-2.141** | **0.0323** | * |
| Hypertension | -0.4906 | 0.3282 | ±0.6564 | -1.495 | 0.1350 |  |
| High cholesterol | -0.0952 | 0.2963 | ±0.5925 | -0.321 | 0.7479 |  |
| Kidney disease | -0.0489 | 0.7659 | ±1.5319 | -0.064 | 0.9491 |  |
| Circulatory disease | -0.2353 | 0.4604 | ±0.9207 | -0.511 | 0.6092 |  |
| Time 54-250, pooled (%) | -1.1868 | 2.1709 | ±4.3418 | -0.547 | 0.5846 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **393**, R² = **0.0916**, Adj R² = **0.0654**, F-statistic = **3.49** (p = **1.14e-04**), Residual SE = **2.573** on **381** df, AIC = **1869.8**, BIC = **1917.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +129.6465 | 283.6565 | ±567.3130 | +0.457 | 0.6476 |  |
| Education: graduate level (vs college) | +0.3860 | 0.2804 | ±0.5607 | +1.377 | 0.1686 |  |
| Education: high school or below (vs college) | -0.8760 | 0.6187 | ±1.2373 | -1.416 | 0.1568 |  |
| Site: UCSD (vs UAB) | -0.3655 | 0.3380 | ±0.6760 | -1.081 | 0.2796 |  |
| Site: UW (vs UAB) | -0.2064 | 0.3550 | ±0.7100 | -0.581 | 0.5610 |  |
| **Age (years)** | **-0.0444** | 0.0133 | ±0.0265 | **-3.353** | **7.99e-04** | *** |
| **BMI (kg/m2)** | **-0.0400** | 0.0188 | ±0.0375 | **-2.132** | **0.0330** | * |
| Hypertension | -0.4847 | 0.3277 | ±0.6553 | -1.479 | 0.1391 |  |
| High cholesterol | -0.0953 | 0.2964 | ±0.5928 | -0.322 | 0.7477 |  |
| Kidney disease | -0.0551 | 0.7659 | ±1.5318 | -0.072 | 0.9427 |  |
| Circulatory disease | -0.2369 | 0.4583 | ±0.9166 | -0.517 | 0.6052 |  |
| Avg. daily time 54-250 (%) | -1.1271 | 2.8362 | ±5.6724 | -0.397 | 0.6911 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **393**, R² = **0.0931**, Adj R² = **0.0669**, F-statistic = **3.56** (p = **8.87e-05**), Residual SE = **2.571** on **381** df, AIC = **1869.2**, BIC = **1916.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.7786** | 1.0826 | ±2.1652 | **+15.498** | **3.56e-54** | *** |
| Education: graduate level (vs college) | +0.3830 | 0.2791 | ±0.5581 | +1.372 | 0.1700 |  |
| Education: high school or below (vs college) | -0.8722 | 0.6253 | ±1.2507 | -1.395 | 0.1631 |  |
| Site: UCSD (vs UAB) | -0.3750 | 0.3376 | ±0.6753 | -1.111 | 0.2666 |  |
| Site: UW (vs UAB) | -0.2129 | 0.3545 | ±0.7090 | -0.600 | 0.5482 |  |
| **Age (years)** | **-0.0441** | 0.0131 | ±0.0263 | **-3.355** | **7.93e-04** | *** |
| **BMI (kg/m2)** | **-0.0386** | 0.0182 | ±0.0365 | **-2.117** | **0.0342** | * |
| Hypertension | -0.4969 | 0.3279 | ±0.6559 | -1.515 | 0.1297 |  |
| High cholesterol | -0.0885 | 0.2957 | ±0.5915 | -0.299 | 0.7646 |  |
| Kidney disease | -0.1134 | 0.7661 | ±1.5321 | -0.148 | 0.8823 |  |
| Circulatory disease | -0.2228 | 0.4648 | ±0.9297 | -0.479 | 0.6317 |  |
| Time 181-250, pooled (%) | +0.4091 | 0.4486 | ±0.8973 | +0.912 | 0.3618 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **393**, R² = **0.0923**, Adj R² = **0.0661**, F-statistic = **3.52** (p = **1.02e-04**), Residual SE = **2.572** on **381** df, AIC = **1869.5**, BIC = **1917.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.8339** | 1.0983 | ±2.1966 | **+15.327** | **5.02e-53** | *** |
| Education: graduate level (vs college) | +0.3821 | 0.2792 | ±0.5584 | +1.368 | 0.1712 |  |
| Education: high school or below (vs college) | -0.8683 | 0.6267 | ±1.2535 | -1.385 | 0.1659 |  |
| Site: UCSD (vs UAB) | -0.3725 | 0.3380 | ±0.6760 | -1.102 | 0.2704 |  |
| Site: UW (vs UAB) | -0.2133 | 0.3551 | ±0.7102 | -0.601 | 0.5481 |  |
| **Age (years)** | **-0.0439** | 0.0132 | ±0.0264 | **-3.321** | **8.95e-04** | *** |
| **BMI (kg/m2)** | **-0.0394** | 0.0185 | ±0.0371 | **-2.127** | **0.0334** | * |
| Hypertension | -0.4913 | 0.3288 | ±0.6577 | -1.494 | 0.1352 |  |
| High cholesterol | -0.0973 | 0.2962 | ±0.5924 | -0.328 | 0.7426 |  |
| Kidney disease | -0.0810 | 0.7665 | ±1.5330 | -0.106 | 0.9159 |  |
| Circulatory disease | -0.2250 | 0.4645 | ±0.9290 | -0.484 | 0.6280 |  |
| Avg. daily time 181-250 (%) | +0.2980 | 0.4580 | ±0.9160 | +0.651 | 0.5153 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **393**, R² = **0.0931**, Adj R² = **0.0669**, F-statistic = **3.56** (p = **8.87e-05**), Residual SE = **2.571** on **381** df, AIC = **1869.2**, BIC = **1916.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.7774** | 1.0829 | ±2.1659 | **+15.493** | **3.89e-54** | *** |
| Education: graduate level (vs college) | +0.3833 | 0.2791 | ±0.5581 | +1.373 | 0.1696 |  |
| Education: high school or below (vs college) | -0.8719 | 0.6253 | ±1.2507 | -1.394 | 0.1632 |  |
| Site: UCSD (vs UAB) | -0.3750 | 0.3376 | ±0.6752 | -1.111 | 0.2667 |  |
| Site: UW (vs UAB) | -0.2131 | 0.3545 | ±0.7089 | -0.601 | 0.5477 |  |
| **Age (years)** | **-0.0441** | 0.0131 | ±0.0263 | **-3.354** | **7.96e-04** | *** |
| **BMI (kg/m2)** | **-0.0386** | 0.0182 | ±0.0365 | **-2.116** | **0.0343** | * |
| Hypertension | -0.4968 | 0.3279 | ±0.6559 | -1.515 | 0.1298 |  |
| High cholesterol | -0.0889 | 0.2957 | ±0.5914 | -0.301 | 0.7637 |  |
| Kidney disease | -0.1133 | 0.7660 | ±1.5321 | -0.148 | 0.8824 |  |
| Circulatory disease | -0.2228 | 0.4649 | ±0.9297 | -0.479 | 0.6318 |  |
| Time > 180 (%) | +0.4089 | 0.4478 | ±0.8957 | +0.913 | 0.3613 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **393**, R² = **0.0923**, Adj R² = **0.0661**, F-statistic = **3.52** (p = **1.02e-04**), Residual SE = **2.572** on **381** df, AIC = **1869.5**, BIC = **1917.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.8329** | 1.0987 | ±2.1974 | **+15.321** | **5.53e-53** | *** |
| Education: graduate level (vs college) | +0.3823 | 0.2792 | ±0.5584 | +1.369 | 0.1709 |  |
| Education: high school or below (vs college) | -0.8681 | 0.6268 | ±1.2535 | -1.385 | 0.1660 |  |
| Site: UCSD (vs UAB) | -0.3725 | 0.3380 | ±0.6760 | -1.102 | 0.2704 |  |
| Site: UW (vs UAB) | -0.2135 | 0.3551 | ±0.7103 | -0.601 | 0.5478 |  |
| **Age (years)** | **-0.0439** | 0.0132 | ±0.0264 | **-3.320** | **8.99e-04** | *** |
| **BMI (kg/m2)** | **-0.0394** | 0.0185 | ±0.0371 | **-2.126** | **0.0335** | * |
| Hypertension | -0.4912 | 0.3288 | ±0.6576 | -1.494 | 0.1352 |  |
| High cholesterol | -0.0976 | 0.2962 | ±0.5924 | -0.329 | 0.7419 |  |
| Kidney disease | -0.0809 | 0.7665 | ±1.5330 | -0.106 | 0.9159 |  |
| Circulatory disease | -0.2250 | 0.4645 | ±0.9290 | -0.484 | 0.6281 |  |
| Avg. daily time > 180 (%) | +0.2978 | 0.4569 | ±0.9139 | +0.652 | 0.5146 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 393)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **393**, R² = **0.0915**, Adj R² = **0.0652**, F-statistic = **3.49** (p = **1.16e-04**), Residual SE = **2.573** on **381** df, AIC = **1869.9**, BIC = **1917.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9213** | 1.1128 | ±2.2256 | **+15.206** | **3.21e-52** | *** |
| Education: graduate level (vs college) | +0.3908 | 0.2820 | ±0.5641 | +1.386 | 0.1658 |  |
| Education: high school or below (vs college) | -0.8817 | 0.6195 | ±1.2390 | -1.423 | 0.1547 |  |
| Site: UCSD (vs UAB) | -0.3694 | 0.3391 | ±0.6782 | -1.089 | 0.2760 |  |
| Site: UW (vs UAB) | -0.2114 | 0.3533 | ±0.7065 | -0.598 | 0.5496 |  |
| **Age (years)** | **-0.0439** | 0.0134 | ±0.0269 | **-3.270** | **0.0011** | ** |
| **BMI (kg/m2)** | **-0.0403** | 0.0186 | ±0.0373 | **-2.161** | **0.0307** | * |
| Hypertension | -0.4857 | 0.3290 | ±0.6581 | -1.476 | 0.1399 |  |
| High cholesterol | -0.1002 | 0.2955 | ±0.5910 | -0.339 | 0.7346 |  |
| Kidney disease | -0.0688 | 0.7656 | ±1.5313 | -0.090 | 0.9284 |  |
| Circulatory disease | -0.2194 | 0.4623 | ±0.9246 | -0.475 | 0.6351 |  |
| Nocturnal time > 180 (%) | +0.1122 | 0.3831 | ±0.7661 | +0.293 | 0.7696 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 393; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **393**, R² = **0.0855**, Adj R² = **0.0615**, F-statistic = **3.57** (p = **1.53e-04**), Residual SE = **4.401** on **382** df, AIC = **2290.8**, BIC = **2334.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2725** | 1.7826 | ±3.5651 | **+4.641** | **3.47e-06** | *** |
| Education: graduate level (vs college) | -0.4633 | 0.4776 | ±0.9553 | -0.970 | 0.3321 |  |
| Education: high school or below (vs college) | +0.8485 | 0.9154 | ±1.8307 | +0.927 | 0.3539 |  |
| Site: UCSD (vs UAB) | -0.7089 | 0.5593 | ±1.1187 | -1.267 | 0.2050 |  |
| Site: UW (vs UAB) | -0.0976 | 0.6136 | ±1.2271 | -0.159 | 0.8736 |  |
| **Age (years)** | **-0.0812** | 0.0212 | ±0.0425 | **-3.824** | **1.31e-04** | *** |
| BMI (kg/m2) | +0.0661 | 0.0351 | ±0.0703 | +1.881 | 0.0600 | . |
| Hypertension | +0.5328 | 0.5323 | ±1.0646 | +1.001 | 0.3169 |  |
| High cholesterol | +0.6718 | 0.4857 | ±0.9713 | +1.383 | 0.1665 |  |
| Kidney disease | +0.8591 | 0.8844 | ±1.7687 | +0.971 | 0.3313 |  |
| Circulatory disease | +1.3896 | 0.8270 | ±1.6540 | +1.680 | 0.0929 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **393**, R² = **0.0857**, Adj R² = **0.0593**, F-statistic = **3.25** (p = **2.96e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.7**, BIC = **2340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.4977** | 4.6602 | ±9.3203 | **+2.038** | **0.0415** | * |
| Education: graduate level (vs college) | -0.4647 | 0.4780 | ±0.9560 | -0.972 | 0.3309 |  |
| Education: high school or below (vs college) | +0.8548 | 0.9192 | ±1.8383 | +0.930 | 0.3524 |  |
| Site: UCSD (vs UAB) | -0.7148 | 0.5639 | ±1.1278 | -1.268 | 0.2050 |  |
| Site: UW (vs UAB) | -0.1077 | 0.6190 | ±1.2380 | -0.174 | 0.8618 |  |
| **Age (years)** | **-0.0806** | 0.0214 | ±0.0429 | **-3.762** | **1.69e-04** | *** |
| BMI (kg/m2) | +0.0670 | 0.0355 | ±0.0710 | +1.889 | 0.0589 | . |
| Hypertension | +0.5455 | 0.5291 | ±1.0583 | +1.031 | 0.3026 |  |
| High cholesterol | +0.6985 | 0.5065 | ±1.0131 | +1.379 | 0.1679 |  |
| Kidney disease | +0.8394 | 0.8917 | ±1.7833 | +0.941 | 0.3465 |  |
| Circulatory disease | +1.3813 | 0.8291 | ±1.6581 | +1.666 | 0.0957 | . |
| HbA1c (%) | -0.2348 | 0.8152 | ±1.6303 | -0.288 | 0.7733 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **393**, R² = **0.0857**, Adj R² = **0.0593**, F-statistic = **3.24** (p = **2.97e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.7**, BIC = **2340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.2350** | 3.6545 | ±7.3090 | **+2.527** | **0.0115** | * |
| Education: graduate level (vs college) | -0.4605 | 0.4790 | ±0.9580 | -0.961 | 0.3364 |  |
| Education: high school or below (vs college) | +0.8438 | 0.9169 | ±1.8337 | +0.920 | 0.3574 |  |
| Site: UCSD (vs UAB) | -0.6997 | 0.5663 | ±1.1326 | -1.236 | 0.2166 |  |
| Site: UW (vs UAB) | -0.0870 | 0.6240 | ±1.2480 | -0.139 | 0.8891 |  |
| **Age (years)** | **-0.0815** | 0.0212 | ±0.0424 | **-3.844** | **1.21e-04** | *** |
| BMI (kg/m2) | +0.0668 | 0.0351 | ±0.0702 | +1.902 | 0.0571 | . |
| Hypertension | +0.5421 | 0.5356 | ±1.0711 | +1.012 | 0.3114 |  |
| High cholesterol | +0.6648 | 0.4884 | ±0.9767 | +1.361 | 0.1734 |  |
| Kidney disease | +0.8691 | 0.8844 | ±1.7687 | +0.983 | 0.3258 |  |
| Circulatory disease | +1.3917 | 0.8285 | ±1.6569 | +1.680 | 0.0930 | . |
| Mean glucose (mg/dL) | -0.0086 | 0.0300 | ±0.0599 | -0.286 | 0.7750 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **393**, R² = **0.0857**, Adj R² = **0.0593**, F-statistic = **3.24** (p = **2.97e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.7**, BIC = **2340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +10.4199 | 7.5510 | ±15.1020 | +1.380 | 0.1676 |  |
| Education: graduate level (vs college) | -0.4605 | 0.4790 | ±0.9580 | -0.961 | 0.3364 |  |
| Education: high school or below (vs college) | +0.8438 | 0.9169 | ±1.8337 | +0.920 | 0.3574 |  |
| Site: UCSD (vs UAB) | -0.6997 | 0.5663 | ±1.1326 | -1.236 | 0.2166 |  |
| Site: UW (vs UAB) | -0.0870 | 0.6240 | ±1.2480 | -0.139 | 0.8891 |  |
| **Age (years)** | **-0.0815** | 0.0212 | ±0.0424 | **-3.844** | **1.21e-04** | *** |
| BMI (kg/m2) | +0.0668 | 0.0351 | ±0.0702 | +1.902 | 0.0571 | . |
| Hypertension | +0.5421 | 0.5356 | ±1.0711 | +1.012 | 0.3114 |  |
| High cholesterol | +0.6648 | 0.4884 | ±0.9767 | +1.361 | 0.1734 |  |
| Kidney disease | +0.8691 | 0.8844 | ±1.7687 | +0.983 | 0.3258 |  |
| Circulatory disease | +1.3917 | 0.8285 | ±1.6569 | +1.680 | 0.0930 | . |
| GMI (%) | -0.3580 | 1.2526 | ±2.5052 | -0.286 | 0.7750 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **393**, R² = **0.0870**, Adj R² = **0.0606**, F-statistic = **3.30** (p = **2.42e-04**), Residual SE = **4.403** on **381** df, AIC = **2292.1**, BIC = **2339.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.4350** | 3.0817 | ±6.1634 | **+3.386** | **7.09e-04** | *** |
| Education: graduate level (vs college) | -0.4765 | 0.4791 | ±0.9582 | -0.994 | 0.3200 |  |
| Education: high school or below (vs college) | +0.8219 | 0.9141 | ±1.8281 | +0.899 | 0.3685 |  |
| Site: UCSD (vs UAB) | -0.6631 | 0.5702 | ±1.1403 | -1.163 | 0.2448 |  |
| Site: UW (vs UAB) | -0.0577 | 0.6274 | ±1.2549 | -0.092 | 0.9267 |  |
| **Age (years)** | **-0.0836** | 0.0210 | ±0.0420 | **-3.985** | **6.75e-05** | *** |
| **BMI (kg/m2)** | **+0.0705** | 0.0356 | ±0.0711 | **+1.982** | **0.0474** | * |
| Hypertension | +0.5457 | 0.5329 | ±1.0658 | +1.024 | 0.3058 |  |
| High cholesterol | +0.6675 | 0.4866 | ±0.9732 | +1.372 | 0.1702 |  |
| Kidney disease | +0.8535 | 0.8838 | ±1.7676 | +0.966 | 0.3342 |  |
| Circulatory disease | +1.3880 | 0.8293 | ±1.6587 | +1.674 | 0.0942 | . |
| Nocturnal mean 00-06h (mg/dL) | -0.0189 | 0.0230 | ±0.0461 | -0.821 | 0.4119 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **393**, R² = **0.0878**, Adj R² = **0.0614**, F-statistic = **3.33** (p = **2.12e-04**), Residual SE = **4.401** on **381** df, AIC = **2291.8**, BIC = **2339.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.6087** | 2.4517 | ±4.9034 | **+2.696** | **0.0070** | ** |
| Education: graduate level (vs college) | -0.4304 | 0.4829 | ±0.9657 | -0.891 | 0.3727 |  |
| Education: high school or below (vs college) | +0.8452 | 0.9186 | ±1.8371 | +0.920 | 0.3575 |  |
| Site: UCSD (vs UAB) | -0.6600 | 0.5599 | ±1.1197 | -1.179 | 0.2385 |  |
| Site: UW (vs UAB) | -0.0675 | 0.6130 | ±1.2260 | -0.110 | 0.9123 |  |
| **Age (years)** | **-0.0813** | 0.0213 | ±0.0426 | **-3.817** | **1.35e-04** | *** |
| BMI (kg/m2) | +0.0647 | 0.0351 | ±0.0702 | +1.842 | 0.0654 | . |
| Hypertension | +0.5254 | 0.5328 | ±1.0657 | +0.986 | 0.3241 |  |
| High cholesterol | +0.6973 | 0.4875 | ±0.9750 | +1.430 | 0.1526 |  |
| Kidney disease | +0.7977 | 0.8692 | ±1.7384 | +0.918 | 0.3588 |  |
| Circulatory disease | +1.3747 | 0.8275 | ±1.6549 | +1.661 | 0.0966 | . |
| Glucose SD, pooled (mg/dL) | +0.0992 | 0.1016 | ±0.2031 | +0.977 | 0.3288 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **393**, R² = **0.0858**, Adj R² = **0.0594**, F-statistic = **3.25** (p = **2.91e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.6**, BIC = **2340.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.6986** | 2.2995 | ±4.5990 | **+3.348** | **8.14e-04** | *** |
| Education: graduate level (vs college) | -0.4506 | 0.4814 | ±0.9628 | -0.936 | 0.3493 |  |
| Education: high school or below (vs college) | +0.8514 | 0.9178 | ±1.8355 | +0.928 | 0.3536 |  |
| Site: UCSD (vs UAB) | -0.6882 | 0.5573 | ±1.1146 | -1.235 | 0.2169 |  |
| Site: UW (vs UAB) | -0.0852 | 0.6127 | ±1.2255 | -0.139 | 0.8894 |  |
| **Age (years)** | **-0.0812** | 0.0213 | ±0.0426 | **-3.816** | **1.35e-04** | *** |
| BMI (kg/m2) | +0.0651 | 0.0353 | ±0.0705 | +1.845 | 0.0651 | . |
| Hypertension | +0.5343 | 0.5344 | ±1.0688 | +1.000 | 0.3174 |  |
| High cholesterol | +0.6798 | 0.4880 | ±0.9760 | +1.393 | 0.1637 |  |
| Kidney disease | +0.8360 | 0.8808 | ±1.7616 | +0.949 | 0.3426 |  |
| Circulatory disease | +1.3873 | 0.8274 | ±1.6549 | +1.677 | 0.0936 | . |
| Avg. daily SD (mg/dL) | +0.0379 | 0.1045 | ±0.2091 | +0.363 | 0.7168 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **393**, R² = **0.0883**, Adj R² = **0.0620**, F-statistic = **3.36** (p = **1.93e-04**), Residual SE = **4.399** on **381** df, AIC = **2291.5**, BIC = **2339.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.4667** | 2.4484 | ±4.8967 | **+2.641** | **0.0083** | ** |
| Education: graduate level (vs college) | -0.4227 | 0.4828 | ±0.9657 | -0.875 | 0.3813 |  |
| Education: high school or below (vs college) | +0.8369 | 0.9171 | ±1.8343 | +0.913 | 0.3615 |  |
| Site: UCSD (vs UAB) | -0.6408 | 0.5650 | ±1.1299 | -1.134 | 0.2567 |  |
| Site: UW (vs UAB) | -0.0458 | 0.6182 | ±1.2365 | -0.074 | 0.9410 |  |
| **Age (years)** | **-0.0816** | 0.0213 | ±0.0426 | **-3.831** | **1.28e-04** | *** |
| BMI (kg/m2) | +0.0658 | 0.0350 | ±0.0700 | +1.879 | 0.0603 | . |
| Hypertension | +0.5411 | 0.5333 | ±1.0666 | +1.015 | 0.3103 |  |
| High cholesterol | +0.6888 | 0.4860 | ±0.9719 | +1.417 | 0.1563 |  |
| Kidney disease | +0.8133 | 0.8704 | ±1.7408 | +0.934 | 0.3501 |  |
| Circulatory disease | +1.3758 | 0.8293 | ±1.6586 | +1.659 | 0.0971 | . |
| CV (%) | +0.1205 | 0.1072 | ±0.2145 | +1.123 | 0.2613 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **393**, R² = **0.0887**, Adj R² = **0.0624**, F-statistic = **3.37** (p = **1.84e-04**), Residual SE = **4.399** on **381** df, AIC = **2291.4**, BIC = **2339.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+10.0284** | 2.2370 | ±4.4740 | **+4.483** | **7.36e-06** | *** |
| Education: graduate level (vs college) | -0.4154 | 0.4830 | ±0.9661 | -0.860 | 0.3898 |  |
| Education: high school or below (vs college) | +0.8367 | 0.9164 | ±1.8328 | +0.913 | 0.3613 |  |
| Site: UCSD (vs UAB) | -0.6533 | 0.5621 | ±1.1242 | -1.162 | 0.2451 |  |
| Site: UW (vs UAB) | -0.0583 | 0.6151 | ±1.2302 | -0.095 | 0.9245 |  |
| **Age (years)** | **-0.0814** | 0.0213 | ±0.0426 | **-3.822** | **1.33e-04** | *** |
| BMI (kg/m2) | +0.0659 | 0.0351 | ±0.0702 | +1.879 | 0.0603 | . |
| Hypertension | +0.5317 | 0.5323 | ±1.0647 | +0.999 | 0.3179 |  |
| High cholesterol | +0.6923 | 0.4859 | ±0.9719 | +1.425 | 0.1542 |  |
| Kidney disease | +0.8267 | 0.8690 | ±1.7380 | +0.951 | 0.3414 |  |
| Circulatory disease | +1.3767 | 0.8282 | ±1.6564 | +1.662 | 0.0965 | . |
| Mean / SD ratio | -0.2596 | 0.2077 | ±0.4154 | -1.250 | 0.2114 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **393**, R² = **0.0858**, Adj R² = **0.0594**, F-statistic = **3.25** (p = **2.90e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.6**, BIC = **2340.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.8214** | 2.3611 | ±4.7222 | **+3.736** | **1.87e-04** | *** |
| Education: graduate level (vs college) | -0.4473 | 0.4810 | ±0.9619 | -0.930 | 0.3523 |  |
| Education: high school or below (vs college) | +0.8484 | 0.9163 | ±1.8325 | +0.926 | 0.3545 |  |
| Site: UCSD (vs UAB) | -0.6877 | 0.5591 | ±1.1182 | -1.230 | 0.2187 |  |
| Site: UW (vs UAB) | -0.0851 | 0.6144 | ±1.2289 | -0.138 | 0.8899 |  |
| **Age (years)** | **-0.0813** | 0.0213 | ±0.0426 | **-3.817** | **1.35e-04** | *** |
| BMI (kg/m2) | +0.0653 | 0.0353 | ±0.0706 | +1.849 | 0.0645 | . |
| Hypertension | +0.5389 | 0.5350 | ±1.0700 | +1.007 | 0.3138 |  |
| High cholesterol | +0.6758 | 0.4873 | ±0.9745 | +1.387 | 0.1655 |  |
| Kidney disease | +0.8453 | 0.8826 | ±1.7651 | +0.958 | 0.3382 |  |
| Circulatory disease | +1.3882 | 0.8279 | ±1.6557 | +1.677 | 0.0936 | . |
| Avg. daily mean/SD | -0.0696 | 0.1831 | ±0.3662 | -0.380 | 0.7040 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **393**, R² = **0.1010**, Adj R² = **0.0750**, F-statistic = **3.89** (p = **2.38e-05**), Residual SE = **4.369** on **381** df, AIC = **2286.1**, BIC = **2333.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4.2485 | 2.1681 | ±4.3362 | +1.960 | 0.0500 | . |
| Education: graduate level (vs college) | -0.4734 | 0.4775 | ±0.9550 | -0.991 | 0.3215 |  |
| Education: high school or below (vs college) | +0.6992 | 0.8907 | ±1.7815 | +0.785 | 0.4325 |  |
| Site: UCSD (vs UAB) | -0.6208 | 0.5459 | ±1.0917 | -1.137 | 0.2554 |  |
| Site: UW (vs UAB) | +0.0683 | 0.5962 | ±1.1925 | +0.115 | 0.9088 |  |
| **Age (years)** | **-0.0747** | 0.0213 | ±0.0425 | **-3.514** | **4.42e-04** | *** |
| **BMI (kg/m2)** | **+0.0720** | 0.0339 | ±0.0679 | **+2.122** | **0.0338** | * |
| Hypertension | +0.5919 | 0.5310 | ±1.0620 | +1.115 | 0.2650 |  |
| High cholesterol | +0.5914 | 0.4837 | ±0.9674 | +1.223 | 0.2214 |  |
| Kidney disease | +0.7399 | 0.8578 | ±1.7157 | +0.863 | 0.3884 |  |
| Circulatory disease | +1.3943 | 0.8189 | ±1.6377 | +1.703 | 0.0886 | . |
| **MAG (mg/dL/h)** | **+0.0996** | 0.0378 | ±0.0756 | **+2.636** | **0.0084** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **393**, R² = **0.0875**, Adj R² = **0.0611**, F-statistic = **3.32** (p = **2.23e-04**), Residual SE = **4.402** on **381** df, AIC = **2291.9**, BIC = **2339.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.6516** | 2.3592 | ±4.7184 | **+2.819** | **0.0048** | ** |
| Education: graduate level (vs college) | -0.4493 | 0.4788 | ±0.9575 | -0.938 | 0.3480 |  |
| Education: high school or below (vs college) | +0.8534 | 0.9111 | ±1.8222 | +0.937 | 0.3489 |  |
| Site: UCSD (vs UAB) | -0.6662 | 0.5550 | ±1.1100 | -1.200 | 0.2300 |  |
| Site: UW (vs UAB) | -0.0663 | 0.6100 | ±1.2200 | -0.109 | 0.9135 |  |
| **Age (years)** | **-0.0809** | 0.0213 | ±0.0425 | **-3.803** | **1.43e-04** | *** |
| BMI (kg/m2) | +0.0684 | 0.0355 | ±0.0711 | +1.924 | 0.0544 | . |
| Hypertension | +0.5544 | 0.5340 | ±1.0680 | +1.038 | 0.2992 |  |
| High cholesterol | +0.6669 | 0.4866 | ±0.9732 | +1.370 | 0.1706 |  |
| Kidney disease | +0.8281 | 0.8655 | ±1.7311 | +0.957 | 0.3387 |  |
| Circulatory disease | +1.3779 | 0.8257 | ±1.6514 | +1.669 | 0.0952 | . |
| Avg. daily range (mg/dL) | +0.0188 | 0.0200 | ±0.0401 | +0.939 | 0.3476 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **393**, R² = **0.0913**, Adj R² = **0.0651**, F-statistic = **3.48** (p = **1.20e-04**), Residual SE = **4.392** on **381** df, AIC = **2290.3**, BIC = **2338.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3475** | 1.9054 | ±3.8107 | **+3.856** | **1.15e-04** | *** |
| Education: graduate level (vs college) | -0.4880 | 0.4752 | ±0.9505 | -1.027 | 0.3045 |  |
| Education: high school or below (vs college) | +0.7754 | 0.9333 | ±1.8667 | +0.831 | 0.4061 |  |
| Site: UCSD (vs UAB) | -0.6897 | 0.5604 | ±1.1208 | -1.231 | 0.2184 |  |
| Site: UW (vs UAB) | -0.1352 | 0.6124 | ±1.2247 | -0.221 | 0.8252 |  |
| **Age (years)** | **-0.0818** | 0.0214 | ±0.0427 | **-3.825** | **1.31e-04** | *** |
| BMI (kg/m2) | +0.0656 | 0.0349 | ±0.0699 | +1.877 | 0.0606 | . |
| Hypertension | +0.4842 | 0.5276 | ±1.0551 | +0.918 | 0.3587 |  |
| High cholesterol | +0.6512 | 0.4853 | ±0.9706 | +1.342 | 0.1796 |  |
| Kidney disease | +0.9175 | 0.8977 | ±1.7955 | +1.022 | 0.3068 |  |
| Circulatory disease | +1.3441 | 0.8321 | ±1.6642 | +1.615 | 0.1063 |  |
| SD of daily means (mg/dL) | +0.2011 | 0.1288 | ±0.2576 | +1.561 | 0.1185 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **393**, R² = **0.0861**, Adj R² = **0.0597**, F-statistic = **3.26** (p = **2.77e-04**), Residual SE = **4.405** on **381** df, AIC = **2292.5**, BIC = **2340.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +47.1756 | 67.2035 | ±134.4070 | +0.702 | 0.4827 |  |
| Education: graduate level (vs college) | -0.4575 | 0.4779 | ±0.9557 | -0.957 | 0.3384 |  |
| Education: high school or below (vs college) | +0.8518 | 0.9158 | ±1.8315 | +0.930 | 0.3523 |  |
| Site: UCSD (vs UAB) | -0.6916 | 0.5585 | ±1.1171 | -1.238 | 0.2156 |  |
| Site: UW (vs UAB) | -0.0823 | 0.6132 | ±1.2265 | -0.134 | 0.8933 |  |
| **Age (years)** | **-0.0808** | 0.0213 | ±0.0426 | **-3.796** | **1.47e-04** | *** |
| BMI (kg/m2) | +0.0672 | 0.0358 | ±0.0716 | +1.877 | 0.0605 | . |
| Hypertension | +0.5283 | 0.5325 | ±1.0649 | +0.992 | 0.3211 |  |
| High cholesterol | +0.6605 | 0.4875 | ±0.9750 | +1.355 | 0.1754 |  |
| Kidney disease | +0.8348 | 0.8709 | ±1.7417 | +0.959 | 0.3378 |  |
| Circulatory disease | +1.3848 | 0.8285 | ±1.6570 | +1.671 | 0.0946 | . |
| Time in range 70-180, pooled (%) | -0.3915 | 0.6751 | ±1.3502 | -0.580 | 0.5620 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **393**, R² = **0.0857**, Adj R² = **0.0593**, F-statistic = **3.25** (p = **2.93e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.7**, BIC = **2340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +33.4258 | 67.4653 | ±134.9306 | +0.495 | 0.6203 |  |
| Education: graduate level (vs college) | -0.4599 | 0.4775 | ±0.9550 | -0.963 | 0.3355 |  |
| Education: high school or below (vs college) | +0.8542 | 0.9149 | ±1.8298 | +0.934 | 0.3505 |  |
| Site: UCSD (vs UAB) | -0.7024 | 0.5590 | ±1.1180 | -1.257 | 0.2089 |  |
| Site: UW (vs UAB) | -0.0966 | 0.6143 | ±1.2286 | -0.157 | 0.8751 |  |
| **Age (years)** | **-0.0807** | 0.0212 | ±0.0425 | **-3.803** | **1.43e-04** | *** |
| BMI (kg/m2) | +0.0664 | 0.0352 | ±0.0705 | +1.883 | 0.0596 | . |
| Hypertension | +0.5380 | 0.5348 | ±1.0696 | +1.006 | 0.3144 |  |
| High cholesterol | +0.6617 | 0.4882 | ±0.9764 | +1.355 | 0.1753 |  |
| Kidney disease | +0.8566 | 0.8795 | ±1.7591 | +0.974 | 0.3301 |  |
| Circulatory disease | +1.3796 | 0.8266 | ±1.6532 | +1.669 | 0.0951 | . |
| Avg. daily time in range 70-180 (%) | -0.2529 | 0.6765 | ±1.3530 | -0.374 | 0.7085 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **393**, R² = **0.0882**, Adj R² = **0.0618**, F-statistic = **3.35** (p = **1.99e-04**), Residual SE = **4.400** on **381** df, AIC = **2291.6**, BIC = **2339.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.4222** | 1.7883 | ±3.5766 | **+4.710** | **2.48e-06** | *** |
| Education: graduate level (vs college) | -0.4768 | 0.4787 | ±0.9575 | -0.996 | 0.3192 |  |
| Education: high school or below (vs college) | +0.8212 | 0.9248 | ±1.8496 | +0.888 | 0.3746 |  |
| Site: UCSD (vs UAB) | -0.8157 | 0.5735 | ±1.1470 | -1.422 | 0.1549 |  |
| Site: UW (vs UAB) | -0.1674 | 0.6193 | ±1.2386 | -0.270 | 0.7869 |  |
| **Age (years)** | **-0.0810** | 0.0212 | ±0.0425 | **-3.817** | **1.35e-04** | *** |
| BMI (kg/m2) | +0.0662 | 0.0352 | ±0.0705 | +1.879 | 0.0603 | . |
| Hypertension | +0.5736 | 0.5344 | ±1.0689 | +1.073 | 0.2831 |  |
| High cholesterol | +0.6742 | 0.4852 | ±0.9704 | +1.390 | 0.1647 |  |
| Kidney disease | +0.7900 | 0.8832 | ±1.7663 | +0.895 | 0.3710 |  |
| Circulatory disease | +1.4194 | 0.8291 | ±1.6582 | +1.712 | 0.0869 | . |
| Any reading < 54 during wear (0/1) | -0.6540 | 0.6311 | ±1.2622 | -1.036 | 0.3000 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **393**, R² = **0.0897**, Adj R² = **0.0634**, F-statistic = **3.41** (p = **1.56e-04**), Residual SE = **4.396** on **381** df, AIC = **2291.0**, BIC = **2338.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.3862** | 1.8009 | ±3.6018 | **+4.657** | **3.21e-06** | *** |
| Education: graduate level (vs college) | -0.4753 | 0.4782 | ±0.9563 | -0.994 | 0.3202 |  |
| Education: high school or below (vs college) | +0.7829 | 0.9170 | ±1.8341 | +0.854 | 0.3933 |  |
| Site: UCSD (vs UAB) | -0.8081 | 0.5644 | ±1.1288 | -1.432 | 0.1522 |  |
| Site: UW (vs UAB) | -0.1510 | 0.6139 | ±1.2278 | -0.246 | 0.8057 |  |
| **Age (years)** | **-0.0823** | 0.0212 | ±0.0425 | **-3.871** | **1.08e-04** | *** |
| BMI (kg/m2) | +0.0692 | 0.0357 | ±0.0714 | +1.940 | 0.0524 | . |
| Hypertension | +0.5827 | 0.5328 | ±1.0655 | +1.094 | 0.2741 |  |
| High cholesterol | +0.6658 | 0.4842 | ±0.9684 | +1.375 | 0.1691 |  |
| Kidney disease | +0.7964 | 0.8827 | ±1.7654 | +0.902 | 0.3670 |  |
| Circulatory disease | +1.4625 | 0.8381 | ±1.6762 | +1.745 | 0.0810 | . |
| Time < 54 (%) | -5.9692 | 4.9258 | ±9.8516 | -1.212 | 0.2256 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **393**, R² = **0.0897**, Adj R² = **0.0634**, F-statistic = **3.41** (p = **1.56e-04**), Residual SE = **4.396** on **381** df, AIC = **2291.0**, BIC = **2338.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.3328** | 1.7921 | ±3.5842 | **+4.650** | **3.32e-06** | *** |
| Education: graduate level (vs college) | -0.4575 | 0.4765 | ±0.9530 | -0.960 | 0.3370 |  |
| Education: high school or below (vs college) | +0.8189 | 0.9146 | ±1.8291 | +0.895 | 0.3706 |  |
| Site: UCSD (vs UAB) | -0.7617 | 0.5576 | ±1.1152 | -1.366 | 0.1719 |  |
| Site: UW (vs UAB) | -0.1179 | 0.6142 | ±1.2284 | -0.192 | 0.8477 |  |
| **Age (years)** | **-0.0818** | 0.0212 | ±0.0424 | **-3.860** | **1.13e-04** | *** |
| BMI (kg/m2) | +0.0681 | 0.0354 | ±0.0709 | +1.922 | 0.0546 | . |
| Hypertension | +0.5581 | 0.5325 | ±1.0650 | +1.048 | 0.2946 |  |
| High cholesterol | +0.6647 | 0.4845 | ±0.9690 | +1.372 | 0.1701 |  |
| Kidney disease | +0.8195 | 0.8818 | ±1.7636 | +0.929 | 0.3527 |  |
| Circulatory disease | +1.4908 | 0.8449 | ±1.6899 | +1.764 | 0.0777 | . |
| Avg. daily time < 54 (%) | -7.0830 | 6.3729 | ±12.7458 | -1.111 | 0.2664 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **393**, R² = **0.0884**, Adj R² = **0.0621**, F-statistic = **3.36** (p = **1.91e-04**), Residual SE = **4.399** on **381** df, AIC = **2291.5**, BIC = **2339.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.0309** | 1.7877 | ±3.5754 | **+4.492** | **7.05e-06** | *** |
| Education: graduate level (vs college) | -0.4361 | 0.4762 | ±0.9523 | -0.916 | 0.3597 |  |
| Education: high school or below (vs college) | +0.8119 | 0.9203 | ±1.8407 | +0.882 | 0.3777 |  |
| Site: UCSD (vs UAB) | -0.6665 | 0.5607 | ±1.1213 | -1.189 | 0.2346 |  |
| Site: UW (vs UAB) | -0.0409 | 0.6179 | ±1.2357 | -0.066 | 0.9472 |  |
| **Age (years)** | **-0.0814** | 0.0213 | ±0.0425 | **-3.832** | **1.27e-04** | *** |
| BMI (kg/m2) | +0.0668 | 0.0349 | ±0.0697 | +1.917 | 0.0552 | . |
| Hypertension | +0.5825 | 0.5331 | ±1.0663 | +1.093 | 0.2745 |  |
| High cholesterol | +0.6079 | 0.4883 | ±0.9765 | +1.245 | 0.2131 |  |
| Kidney disease | +0.9345 | 0.8858 | ±1.7716 | +1.055 | 0.2914 |  |
| Circulatory disease | +1.3956 | 0.8313 | ±1.6626 | +1.679 | 0.0932 | . |
| Time 54-69, pooled (%) | +1.4014 | 1.1837 | ±2.3674 | +1.184 | 0.2364 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **393**, R² = **0.0865**, Adj R² = **0.0601**, F-statistic = **3.28** (p = **2.60e-04**), Residual SE = **4.404** on **381** df, AIC = **2292.3**, BIC = **2340.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.1532** | 1.7863 | ±3.5725 | **+4.564** | **5.01e-06** | *** |
| Education: graduate level (vs college) | -0.4412 | 0.4757 | ±0.9514 | -0.928 | 0.3537 |  |
| Education: high school or below (vs college) | +0.8259 | 0.9209 | ±1.8418 | +0.897 | 0.3698 |  |
| Site: UCSD (vs UAB) | -0.6977 | 0.5603 | ±1.1205 | -1.245 | 0.2130 |  |
| Site: UW (vs UAB) | -0.0836 | 0.6161 | ±1.2323 | -0.136 | 0.8920 |  |
| **Age (years)** | **-0.0815** | 0.0213 | ±0.0425 | **-3.832** | **1.27e-04** | *** |
| BMI (kg/m2) | +0.0664 | 0.0350 | ±0.0701 | +1.896 | 0.0580 | . |
| Hypertension | +0.5822 | 0.5390 | ±1.0781 | +1.080 | 0.2801 |  |
| High cholesterol | +0.6435 | 0.4890 | ±0.9781 | +1.316 | 0.1882 |  |
| Kidney disease | +0.9006 | 0.8848 | ±1.7695 | +1.018 | 0.3087 |  |
| Circulatory disease | +1.3798 | 0.8319 | ±1.6637 | +1.659 | 0.0972 | . |
| Avg. daily time 54-69 (%) | +0.8445 | 1.2348 | ±2.4696 | +0.684 | 0.4940 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **393**, R² = **0.0865**, Adj R² = **0.0601**, F-statistic = **3.28** (p = **2.60e-04**), Residual SE = **4.404** on **381** df, AIC = **2292.3**, BIC = **2340.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.1303** | 1.7901 | ±3.5803 | **+4.542** | **5.58e-06** | *** |
| Education: graduate level (vs college) | -0.4474 | 0.4787 | ±0.9573 | -0.935 | 0.3500 |  |
| Education: high school or below (vs college) | +0.8373 | 0.9181 | ±1.8363 | +0.912 | 0.3618 |  |
| Site: UCSD (vs UAB) | -0.6741 | 0.5614 | ±1.1228 | -1.201 | 0.2298 |  |
| Site: UW (vs UAB) | -0.0609 | 0.6183 | ±1.2366 | -0.098 | 0.9215 |  |
| **Age (years)** | **-0.0812** | 0.0213 | ±0.0426 | **-3.813** | **1.37e-04** | *** |
| BMI (kg/m2) | +0.0661 | 0.0350 | ±0.0700 | +1.888 | 0.0591 | . |
| Hypertension | +0.5529 | 0.5352 | ±1.0703 | +1.033 | 0.3015 |  |
| High cholesterol | +0.6387 | 0.4897 | ±0.9795 | +1.304 | 0.1922 |  |
| Kidney disease | +0.9069 | 0.8880 | ±1.7760 | +1.021 | 0.3071 |  |
| Circulatory disease | +1.3837 | 0.8310 | ±1.6620 | +1.665 | 0.0959 | . |
| Time < 70 (%) | +0.7427 | 1.1001 | ±2.2001 | +0.675 | 0.4996 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **393**, R² = **0.0857**, Adj R² = **0.0593**, F-statistic = **3.25** (p = **2.96e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.7**, BIC = **2340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2185** | 1.7885 | ±3.5770 | **+4.595** | **4.32e-06** | *** |
| Education: graduate level (vs college) | -0.4541 | 0.4781 | ±0.9562 | -0.950 | 0.3422 |  |
| Education: high school or below (vs college) | +0.8404 | 0.9202 | ±1.8404 | +0.913 | 0.3611 |  |
| Site: UCSD (vs UAB) | -0.7014 | 0.5599 | ±1.1198 | -1.253 | 0.2103 |  |
| Site: UW (vs UAB) | -0.0906 | 0.6166 | ±1.2333 | -0.147 | 0.8832 |  |
| **Age (years)** | **-0.0813** | 0.0213 | ±0.0426 | **-3.818** | **1.34e-04** | *** |
| BMI (kg/m2) | +0.0661 | 0.0352 | ±0.0703 | +1.881 | 0.0600 | . |
| Hypertension | +0.5526 | 0.5398 | ±1.0796 | +1.024 | 0.3060 |  |
| High cholesterol | +0.6601 | 0.4900 | ±0.9800 | +1.347 | 0.1779 |  |
| Kidney disease | +0.8788 | 0.8872 | ±1.7744 | +0.991 | 0.3219 |  |
| Circulatory disease | +1.3803 | 0.8326 | ±1.6652 | +1.658 | 0.0974 | . |
| Avg. daily time < 70 (%) | +0.3605 | 1.1565 | ±2.3129 | +0.312 | 0.7553 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **393**, R² = **0.0897**, Adj R² = **0.0635**, F-statistic = **3.41** (p = **1.54e-04**), Residual SE = **4.396** on **381** df, AIC = **2290.9**, BIC = **2338.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -591.8577 | 487.5781 | ±975.1563 | -1.214 | 0.2248 |  |
| Education: graduate level (vs college) | -0.4799 | 0.4785 | ±0.9571 | -1.003 | 0.3159 |  |
| Education: high school or below (vs college) | +0.7787 | 0.9174 | ±1.8348 | +0.849 | 0.3960 |  |
| Site: UCSD (vs UAB) | -0.8090 | 0.5644 | ±1.1288 | -1.433 | 0.1517 |  |
| Site: UW (vs UAB) | -0.1478 | 0.6135 | ±1.2270 | -0.241 | 0.8097 |  |
| **Age (years)** | **-0.0824** | 0.0213 | ±0.0425 | **-3.879** | **1.05e-04** | *** |
| BMI (kg/m2) | +0.0690 | 0.0356 | ±0.0712 | +1.938 | 0.0526 | . |
| Hypertension | +0.5812 | 0.5326 | ±1.0652 | +1.091 | 0.2751 |  |
| High cholesterol | +0.6712 | 0.4844 | ±0.9688 | +1.386 | 0.1659 |  |
| Kidney disease | +0.7949 | 0.8826 | ±1.7653 | +0.901 | 0.3678 |  |
| Circulatory disease | +1.4623 | 0.8379 | ±1.6759 | +1.745 | 0.0810 | . |
| Time 54-250, pooled (%) | +6.0026 | 4.8772 | ±9.7544 | +1.231 | 0.2184 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **393**, R² = **0.0897**, Adj R² = **0.0635**, F-statistic = **3.41** (p = **1.54e-04**), Residual SE = **4.396** on **381** df, AIC = **2290.9**, BIC = **2338.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -700.9211 | 623.4404 | ±1246.8808 | -1.124 | 0.2609 |  |
| Education: graduate level (vs college) | -0.4635 | 0.4768 | ±0.9536 | -0.972 | 0.3310 |  |
| Education: high school or below (vs college) | +0.8138 | 0.9147 | ±1.8294 | +0.890 | 0.3736 |  |
| Site: UCSD (vs UAB) | -0.7623 | 0.5576 | ±1.1152 | -1.367 | 0.1716 |  |
| Site: UW (vs UAB) | -0.1134 | 0.6140 | ±1.2281 | -0.185 | 0.8535 |  |
| **Age (years)** | **-0.0821** | 0.0212 | ±0.0424 | **-3.869** | **1.09e-04** | *** |
| BMI (kg/m2) | +0.0678 | 0.0354 | ±0.0707 | +1.918 | 0.0551 | . |
| Hypertension | +0.5559 | 0.5323 | ±1.0646 | +1.044 | 0.2963 |  |
| High cholesterol | +0.6718 | 0.4850 | ±0.9701 | +1.385 | 0.1660 |  |
| Kidney disease | +0.8180 | 0.8817 | ±1.7634 | +0.928 | 0.3536 |  |
| Circulatory disease | +1.4900 | 0.8445 | ±1.6890 | +1.764 | 0.0777 | . |
| Avg. daily time 54-250 (%) | +7.0928 | 6.2359 | ±12.4718 | +1.137 | 0.2554 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **393**, R² = **0.0855**, Adj R² = **0.0591**, F-statistic = **3.24** (p = **3.06e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.8**, BIC = **2340.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2429** | 1.8048 | ±3.6096 | **+4.567** | **4.94e-06** | *** |
| Education: graduate level (vs college) | -0.4638 | 0.4792 | ±0.9584 | -0.968 | 0.3331 |  |
| Education: high school or below (vs college) | +0.8501 | 0.9163 | ±1.8327 | +0.928 | 0.3536 |  |
| Site: UCSD (vs UAB) | -0.7091 | 0.5610 | ±1.1220 | -1.264 | 0.2062 |  |
| Site: UW (vs UAB) | -0.0983 | 0.6157 | ±1.2313 | -0.160 | 0.8732 |  |
| **Age (years)** | **-0.0812** | 0.0212 | ±0.0425 | **-3.820** | **1.33e-04** | *** |
| BMI (kg/m2) | +0.0663 | 0.0355 | ±0.0710 | +1.866 | 0.0620 | . |
| Hypertension | +0.5301 | 0.5325 | ±1.0650 | +0.996 | 0.3195 |  |
| High cholesterol | +0.6730 | 0.4870 | ±0.9740 | +1.382 | 0.1670 |  |
| Kidney disease | +0.8504 | 0.8814 | ±1.7628 | +0.965 | 0.3347 |  |
| Circulatory disease | +1.3893 | 0.8287 | ±1.6574 | +1.676 | 0.0936 | . |
| Time 181-250, pooled (%) | +0.0690 | 0.7615 | ±1.5231 | +0.091 | 0.9278 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **393**, R² = **0.0855**, Adj R² = **0.0591**, F-statistic = **3.24** (p = **3.04e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.8**, BIC = **2340.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2208** | 1.7874 | ±3.5748 | **+4.599** | **4.24e-06** | *** |
| Education: graduate level (vs college) | -0.4649 | 0.4799 | ±0.9597 | -0.969 | 0.3326 |  |
| Education: high school or below (vs college) | +0.8542 | 0.9163 | ±1.8326 | +0.932 | 0.3512 |  |
| Site: UCSD (vs UAB) | -0.7083 | 0.5605 | ±1.1209 | -1.264 | 0.2063 |  |
| Site: UW (vs UAB) | -0.0995 | 0.6159 | ±1.2318 | -0.162 | 0.8717 |  |
| **Age (years)** | **-0.0810** | 0.0212 | ±0.0423 | **-3.825** | **1.31e-04** | *** |
| BMI (kg/m2) | +0.0662 | 0.0353 | ±0.0706 | +1.877 | 0.0606 | . |
| Hypertension | +0.5284 | 0.5318 | ±1.0636 | +0.994 | 0.3205 |  |
| High cholesterol | +0.6710 | 0.4868 | ±0.9736 | +1.378 | 0.1681 |  |
| Kidney disease | +0.8508 | 0.8806 | ±1.7612 | +0.966 | 0.3340 |  |
| Circulatory disease | +1.3879 | 0.8278 | ±1.6555 | +1.677 | 0.0936 | . |
| Avg. daily time 181-250 (%) | +0.1280 | 0.7650 | ±1.5300 | +0.167 | 0.8671 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **393**, R² = **0.0855**, Adj R² = **0.0591**, F-statistic = **3.24** (p = **3.06e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.8**, BIC = **2340.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2439** | 1.8054 | ±3.6108 | **+4.566** | **4.97e-06** | *** |
| Education: graduate level (vs college) | -0.4637 | 0.4791 | ±0.9583 | -0.968 | 0.3332 |  |
| Education: high school or below (vs college) | +0.8501 | 0.9163 | ±1.8326 | +0.928 | 0.3536 |  |
| Site: UCSD (vs UAB) | -0.7091 | 0.5610 | ±1.1220 | -1.264 | 0.2062 |  |
| Site: UW (vs UAB) | -0.0983 | 0.6157 | ±1.2314 | -0.160 | 0.8732 |  |
| **Age (years)** | **-0.0812** | 0.0212 | ±0.0425 | **-3.820** | **1.33e-04** | *** |
| BMI (kg/m2) | +0.0663 | 0.0355 | ±0.0710 | +1.866 | 0.0620 | . |
| Hypertension | +0.5302 | 0.5325 | ±1.0650 | +0.996 | 0.3194 |  |
| High cholesterol | +0.6729 | 0.4870 | ±0.9740 | +1.382 | 0.1670 |  |
| Kidney disease | +0.8507 | 0.8815 | ±1.7630 | +0.965 | 0.3345 |  |
| Circulatory disease | +1.3893 | 0.8287 | ±1.6574 | +1.676 | 0.0936 | . |
| Time > 180 (%) | +0.0662 | 0.7604 | ±1.5208 | +0.087 | 0.9306 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **393**, R² = **0.0855**, Adj R² = **0.0591**, F-statistic = **3.24** (p = **3.04e-04**), Residual SE = **4.406** on **381** df, AIC = **2292.8**, BIC = **2340.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.2217** | 1.7880 | ±3.5761 | **+4.598** | **4.26e-06** | *** |
| Education: graduate level (vs college) | -0.4648 | 0.4798 | ±0.9596 | -0.969 | 0.3327 |  |
| Education: high school or below (vs college) | +0.8542 | 0.9163 | ±1.8326 | +0.932 | 0.3512 |  |
| Site: UCSD (vs UAB) | -0.7083 | 0.5604 | ±1.1209 | -1.264 | 0.2063 |  |
| Site: UW (vs UAB) | -0.0995 | 0.6160 | ±1.2319 | -0.162 | 0.8717 |  |
| **Age (years)** | **-0.0810** | 0.0212 | ±0.0423 | **-3.825** | **1.31e-04** | *** |
| BMI (kg/m2) | +0.0662 | 0.0353 | ±0.0706 | +1.877 | 0.0606 | . |
| Hypertension | +0.5285 | 0.5318 | ±1.0636 | +0.994 | 0.3203 |  |
| High cholesterol | +0.6709 | 0.4868 | ±0.9736 | +1.378 | 0.1681 |  |
| Kidney disease | +0.8510 | 0.8807 | ±1.7613 | +0.966 | 0.3339 |  |
| Circulatory disease | +1.3879 | 0.8278 | ±1.6556 | +1.677 | 0.0936 | . |
| Avg. daily time > 180 (%) | +0.1249 | 0.7633 | ±1.5265 | +0.164 | 0.8701 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **393**, R² = **0.0908**, Adj R² = **0.0646**, F-statistic = **3.46** (p = **1.30e-04**), Residual SE = **4.394** on **381** df, AIC = **2290.5**, BIC = **2338.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.9731** | 1.7794 | ±3.5588 | **+4.481** | **7.44e-06** | *** |
| Education: graduate level (vs college) | -0.4187 | 0.4783 | ±0.9566 | -0.875 | 0.3814 |  |
| Education: high school or below (vs college) | +0.8473 | 0.9228 | ±1.8457 | +0.918 | 0.3585 |  |
| Site: UCSD (vs UAB) | -0.6673 | 0.5628 | ±1.1256 | -1.186 | 0.2358 |  |
| Site: UW (vs UAB) | -0.1207 | 0.6139 | ±1.2278 | -0.197 | 0.8442 |  |
| **Age (years)** | **-0.0753** | 0.0210 | ±0.0419 | **-3.593** | **3.27e-04** | *** |
| BMI (kg/m2) | +0.0607 | 0.0354 | ±0.0708 | +1.714 | 0.0865 | . |
| Hypertension | +0.4902 | 0.5317 | ±1.0634 | +0.922 | 0.3566 |  |
| High cholesterol | +0.6276 | 0.4859 | ±0.9717 | +1.292 | 0.1964 |  |
| Kidney disease | +0.7936 | 0.8851 | ±1.7702 | +0.897 | 0.3699 |  |
| Circulatory disease | +1.4043 | 0.8202 | ±1.6404 | +1.712 | 0.0869 | . |
| Nocturnal time > 180 (%) | +1.0233 | 0.7515 | ±1.5030 | +1.362 | 0.1733 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 393; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0856**, LLR χ² = **30.98** (p = **5.91e-04**), AUC = **0.6802**, AIC = **353.1**, BIC = **396.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2778 | 1.0135 | ±2.0271 | -0.274 | 0.7841 | 0.7575 |  |
| Education: graduate level (vs college) | -0.2457 | 0.2996 | ±0.5993 | -0.820 | 0.4122 | 0.7822 |  |
| Education: high school or below (vs college) | -0.0197 | 0.4906 | ±0.9812 | -0.040 | 0.9680 | 0.9805 |  |
| Site: UCSD (vs UAB) | -0.0916 | 0.3753 | ±0.7507 | -0.244 | 0.8072 | 0.9125 |  |
| Site: UW (vs UAB) | +0.2340 | 0.3547 | ±0.7095 | +0.660 | 0.5095 | 1.2636 |  |
| **Age (years)** | **-0.0515** | 0.0141 | ±0.0283 | **-3.642** | **2.70e-04** | 0.9498 | *** |
| **BMI (kg/m2)** | **+0.0422** | 0.0178 | ±0.0355 | **+2.377** | **0.0175** | 1.0431 | * |
| Hypertension | +0.2534 | 0.3183 | ±0.6366 | +0.796 | 0.4260 | 1.2884 |  |
| High cholesterol | +0.5777 | 0.2993 | ±0.5987 | +1.930 | 0.0536 | 1.7819 | . |
| Kidney disease | +0.3785 | 0.5798 | ±1.1595 | +0.653 | 0.5138 | 1.4602 |  |
| **Circulatory disease** | **+0.9049** | 0.4242 | ±0.8483 | **+2.133** | **0.0329** | 2.4718 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0856**, LLR χ² = **30.99** (p = **0.0011**), AUC = **0.6805**, AIC = **355.1**, BIC = **402.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5336 | 2.6540 | ±5.3080 | -0.201 | 0.8407 | 0.5865 |  |
| Education: graduate level (vs college) | -0.2440 | 0.3001 | ±0.6001 | -0.813 | 0.4161 | 0.7835 |  |
| Education: high school or below (vs college) | -0.0206 | 0.4907 | ±0.9815 | -0.042 | 0.9664 | 0.9796 |  |
| Site: UCSD (vs UAB) | -0.0888 | 0.3763 | ±0.7526 | -0.236 | 0.8134 | 0.9150 |  |
| Site: UW (vs UAB) | +0.2364 | 0.3555 | ±0.7111 | +0.665 | 0.5061 | 1.2667 |  |
| **Age (years)** | **-0.0516** | 0.0142 | ±0.0284 | **-3.638** | **2.75e-04** | 0.9497 | *** |
| **BMI (kg/m2)** | **+0.0420** | 0.0179 | ±0.0358 | **+2.349** | **0.0188** | 1.0429 | * |
| Hypertension | +0.2506 | 0.3194 | ±0.6388 | +0.784 | 0.4328 | 1.2848 |  |
| High cholesterol | +0.5721 | 0.3041 | ±0.6082 | +1.881 | 0.0600 | 1.7719 | . |
| Kidney disease | +0.3814 | 0.5804 | ±1.1608 | +0.657 | 0.5111 | 1.4643 |  |
| **Circulatory disease** | **+0.9083** | 0.4253 | ±0.8507 | **+2.135** | **0.0327** | 2.4801 | * |
| HbA1c (%) | +0.0488 | 0.4673 | ±0.9345 | +0.104 | 0.9169 | 1.0500 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0858**, LLR χ² = **31.06** (p = **0.0011**), AUC = **0.6795**, AIC = **355.0**, BIC = **402.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.2858 | 2.3167 | ±4.6334 | +0.123 | 0.9018 | 1.3309 |  |
| Education: graduate level (vs college) | -0.2466 | 0.2997 | ±0.5995 | -0.823 | 0.4107 | 0.7815 |  |
| Education: high school or below (vs college) | -0.0249 | 0.4913 | ±0.9825 | -0.051 | 0.9595 | 0.9754 |  |
| Site: UCSD (vs UAB) | -0.0905 | 0.3754 | ±0.7508 | -0.241 | 0.8095 | 0.9135 |  |
| Site: UW (vs UAB) | +0.2384 | 0.3551 | ±0.7101 | +0.671 | 0.5020 | 1.2692 |  |
| **Age (years)** | **-0.0517** | 0.0142 | ±0.0283 | **-3.649** | **2.64e-04** | 0.9496 | *** |
| **BMI (kg/m2)** | **+0.0426** | 0.0178 | ±0.0357 | **+2.390** | **0.0168** | 1.0435 | * |
| Hypertension | +0.2565 | 0.3186 | ±0.6372 | +0.805 | 0.4207 | 1.2924 |  |
| High cholesterol | +0.5767 | 0.2993 | ±0.5985 | +1.927 | 0.0540 | 1.7801 | . |
| Kidney disease | +0.3888 | 0.5810 | ±1.1620 | +0.669 | 0.5033 | 1.4752 |  |
| **Circulatory disease** | **+0.9039** | 0.4246 | ±0.8492 | **+2.129** | **0.0333** | 2.4691 | * |
| Mean glucose (mg/dL) | -0.0049 | 0.0183 | ±0.0366 | -0.270 | 0.7869 | 0.9951 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0858**, LLR χ² = **31.06** (p = **0.0011**), AUC = **0.6795**, AIC = **355.0**, BIC = **402.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.9704 | 4.7250 | ±9.4499 | +0.205 | 0.8373 | 2.6389 |  |
| Education: graduate level (vs college) | -0.2466 | 0.2997 | ±0.5995 | -0.823 | 0.4107 | 0.7815 |  |
| Education: high school or below (vs college) | -0.0249 | 0.4913 | ±0.9825 | -0.051 | 0.9595 | 0.9754 |  |
| Site: UCSD (vs UAB) | -0.0905 | 0.3754 | ±0.7508 | -0.241 | 0.8095 | 0.9135 |  |
| Site: UW (vs UAB) | +0.2384 | 0.3551 | ±0.7101 | +0.671 | 0.5020 | 1.2692 |  |
| **Age (years)** | **-0.0517** | 0.0142 | ±0.0283 | **-3.649** | **2.64e-04** | 0.9496 | *** |
| **BMI (kg/m2)** | **+0.0426** | 0.0178 | ±0.0357 | **+2.390** | **0.0168** | 1.0435 | * |
| Hypertension | +0.2565 | 0.3186 | ±0.6372 | +0.805 | 0.4207 | 1.2924 |  |
| High cholesterol | +0.5767 | 0.2993 | ±0.5985 | +1.927 | 0.0540 | 1.7801 | . |
| Kidney disease | +0.3888 | 0.5810 | ±1.1620 | +0.669 | 0.5033 | 1.4752 |  |
| **Circulatory disease** | **+0.9039** | 0.4246 | ±0.8492 | **+2.129** | **0.0333** | 2.4691 | * |
| GMI (%) | -0.2068 | 0.7649 | ±1.5298 | -0.270 | 0.7869 | 0.8132 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0859**, LLR χ² = **31.11** (p = **0.0011**), AUC = **0.6791**, AIC = **355.0**, BIC = **402.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3447 | 2.0242 | ±4.0484 | +0.170 | 0.8648 | 1.4115 |  |
| Education: graduate level (vs college) | -0.2509 | 0.3002 | ±0.6003 | -0.836 | 0.4032 | 0.7781 |  |
| Education: high school or below (vs college) | -0.0268 | 0.4910 | ±0.9820 | -0.055 | 0.9564 | 0.9735 |  |
| Site: UCSD (vs UAB) | -0.0849 | 0.3758 | ±0.7516 | -0.226 | 0.8213 | 0.9186 |  |
| Site: UW (vs UAB) | +0.2424 | 0.3554 | ±0.7108 | +0.682 | 0.4953 | 1.2743 |  |
| **Age (years)** | **-0.0524** | 0.0144 | ±0.0287 | **-3.642** | **2.70e-04** | 0.9490 | *** |
| **BMI (kg/m2)** | **+0.0432** | 0.0180 | ±0.0359 | **+2.407** | **0.0161** | 1.0442 | * |
| Hypertension | +0.2565 | 0.3185 | ±0.6370 | +0.805 | 0.4206 | 1.2924 |  |
| High cholesterol | +0.5814 | 0.2994 | ±0.5989 | +1.942 | 0.0522 | 1.7886 | . |
| Kidney disease | +0.3801 | 0.5799 | ±1.1597 | +0.656 | 0.5121 | 1.4625 |  |
| **Circulatory disease** | **+0.9009** | 0.4249 | ±0.8498 | **+2.120** | **0.0340** | 2.4619 | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0053 | 0.0148 | ±0.0296 | -0.355 | 0.7229 | 0.9948 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0883**, LLR χ² = **31.95** (p = **7.76e-04**), AUC = **0.6839**, AIC = **354.1**, BIC = **401.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3872 | 1.5171 | ±3.0342 | -0.914 | 0.3605 | 0.2498 |  |
| Education: graduate level (vs college) | -0.2230 | 0.3007 | ±0.6013 | -0.742 | 0.4583 | 0.8001 |  |
| Education: high school or below (vs college) | -0.0276 | 0.4927 | ±0.9854 | -0.056 | 0.9553 | 0.9727 |  |
| Site: UCSD (vs UAB) | -0.0404 | 0.3802 | ±0.7605 | -0.106 | 0.9154 | 0.9604 |  |
| Site: UW (vs UAB) | +0.2774 | 0.3589 | ±0.7179 | +0.773 | 0.4395 | 1.3198 |  |
| **Age (years)** | **-0.0513** | 0.0141 | ±0.0282 | **-3.643** | **2.70e-04** | 0.9500 | *** |
| **BMI (kg/m2)** | **+0.0416** | 0.0178 | ±0.0357 | **+2.335** | **0.0195** | 1.0425 | * |
| Hypertension | +0.2440 | 0.3195 | ±0.6389 | +0.764 | 0.4450 | 1.2763 |  |
| **High cholesterol** | **+0.5905** | 0.3003 | ±0.6005 | **+1.967** | **0.0492** | 1.8049 | * |
| Kidney disease | +0.3149 | 0.5880 | ±1.1761 | +0.535 | 0.5923 | 1.3701 |  |
| **Circulatory disease** | **+0.9182** | 0.4240 | ±0.8481 | **+2.165** | **0.0304** | 2.5048 | * |
| Glucose SD, pooled (mg/dL) | +0.0639 | 0.0650 | ±0.1301 | +0.982 | 0.3261 | 1.0659 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0873**, LLR χ² = **31.62** (p = **8.77e-04**), AUC = **0.6817**, AIC = **354.5**, BIC = **402.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0991 | 1.4450 | ±2.8899 | -0.761 | 0.4469 | 0.3332 |  |
| Education: graduate level (vs college) | -0.2265 | 0.3006 | ±0.6011 | -0.754 | 0.4511 | 0.7973 |  |
| Education: high school or below (vs college) | -0.0162 | 0.4919 | ±0.9838 | -0.033 | 0.9737 | 0.9839 |  |
| Site: UCSD (vs UAB) | -0.0489 | 0.3799 | ±0.7598 | -0.129 | 0.8976 | 0.9523 |  |
| Site: UW (vs UAB) | +0.2686 | 0.3585 | ±0.7170 | +0.749 | 0.4537 | 1.3082 |  |
| **Age (years)** | **-0.0513** | 0.0141 | ±0.0282 | **-3.638** | **2.74e-04** | 0.9500 | *** |
| **BMI (kg/m2)** | **+0.0411** | 0.0179 | ±0.0358 | **+2.300** | **0.0214** | 1.0420 | * |
| Hypertension | +0.2511 | 0.3191 | ±0.6381 | +0.787 | 0.4312 | 1.2855 |  |
| High cholesterol | +0.5872 | 0.3002 | ±0.6004 | +1.956 | 0.0505 | 1.7989 | . |
| Kidney disease | +0.3284 | 0.5866 | ±1.1731 | +0.560 | 0.5756 | 1.3887 |  |
| **Circulatory disease** | **+0.9177** | 0.4242 | ±0.8484 | **+2.163** | **0.0305** | 2.5035 | * |
| Avg. daily SD (mg/dL) | +0.0522 | 0.0655 | ±0.1310 | +0.797 | 0.4253 | 1.0536 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0888**, LLR χ² = **32.17** (p = **7.17e-04**), AUC = **0.6842**, AIC = **353.9**, BIC = **401.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4410 | 1.4746 | ±2.9491 | -0.977 | 0.3284 | 0.2367 |  |
| Education: graduate level (vs college) | -0.2215 | 0.3008 | ±0.6016 | -0.736 | 0.4615 | 0.8013 |  |
| Education: high school or below (vs college) | -0.0370 | 0.4936 | ±0.9871 | -0.075 | 0.9403 | 0.9637 |  |
| Site: UCSD (vs UAB) | -0.0358 | 0.3803 | ±0.7605 | -0.094 | 0.9250 | 0.9649 |  |
| Site: UW (vs UAB) | +0.2885 | 0.3597 | ±0.7195 | +0.802 | 0.4226 | 1.3344 |  |
| **Age (years)** | **-0.0517** | 0.0141 | ±0.0282 | **-3.662** | **2.50e-04** | 0.9496 | *** |
| **BMI (kg/m2)** | **+0.0423** | 0.0178 | ±0.0357 | **+2.371** | **0.0178** | 1.0432 | * |
| Hypertension | +0.2500 | 0.3196 | ±0.6392 | +0.782 | 0.4341 | 1.2840 |  |
| **High cholesterol** | **+0.5908** | 0.3002 | ±0.6003 | **+1.968** | **0.0490** | 1.8055 | * |
| Kidney disease | +0.3317 | 0.5866 | ±1.1733 | +0.565 | 0.5718 | 1.3933 |  |
| **Circulatory disease** | **+0.9153** | 0.4246 | ±0.8493 | **+2.156** | **0.0311** | 2.4975 | * |
| CV (%) | +0.0760 | 0.0699 | ±0.1397 | +1.087 | 0.2770 | 1.0789 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0886**, LLR χ² = **32.08** (p = **7.41e-04**), AUC = **0.6844**, AIC = **354.0**, BIC = **401.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.7448 | 1.4147 | ±2.8294 | +0.527 | 0.5985 | 2.1061 |  |
| Education: graduate level (vs college) | -0.2224 | 0.3007 | ±0.6014 | -0.740 | 0.4596 | 0.8006 |  |
| Education: high school or below (vs college) | -0.0380 | 0.4936 | ±0.9872 | -0.077 | 0.9386 | 0.9627 |  |
| Site: UCSD (vs UAB) | -0.0513 | 0.3784 | ±0.7569 | -0.136 | 0.8922 | 0.9500 |  |
| Site: UW (vs UAB) | +0.2754 | 0.3581 | ±0.7162 | +0.769 | 0.4418 | 1.3171 |  |
| **Age (years)** | **-0.0516** | 0.0141 | ±0.0282 | **-3.653** | **2.59e-04** | 0.9498 | *** |
| **BMI (kg/m2)** | **+0.0424** | 0.0178 | ±0.0356 | **+2.378** | **0.0174** | 1.0433 | * |
| Hypertension | +0.2453 | 0.3195 | ±0.6391 | +0.768 | 0.4426 | 1.2780 |  |
| **High cholesterol** | **+0.5908** | 0.3001 | ±0.6002 | **+1.969** | **0.0490** | 1.8054 | * |
| Kidney disease | +0.3476 | 0.5851 | ±1.1702 | +0.594 | 0.5524 | 1.4157 |  |
| **Circulatory disease** | **+0.9135** | 0.4246 | ±0.8492 | **+2.151** | **0.0314** | 2.4930 | * |
| Mean / SD ratio | -0.1541 | 0.1488 | ±0.2976 | -1.036 | 0.3004 | 0.8572 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0870**, LLR χ² = **31.50** (p = **9.17e-04**), AUC = **0.6818**, AIC = **354.6**, BIC = **402.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3968 | 1.3882 | ±2.7765 | +0.286 | 0.7750 | 1.4871 |  |
| Education: graduate level (vs college) | -0.2285 | 0.3005 | ±0.6010 | -0.760 | 0.4470 | 0.7957 |  |
| Education: high school or below (vs college) | -0.0237 | 0.4921 | ±0.9841 | -0.048 | 0.9616 | 0.9766 |  |
| Site: UCSD (vs UAB) | -0.0620 | 0.3781 | ±0.7563 | -0.164 | 0.8697 | 0.9399 |  |
| Site: UW (vs UAB) | +0.2616 | 0.3574 | ±0.7149 | +0.732 | 0.4642 | 1.2990 |  |
| **Age (years)** | **-0.0515** | 0.0141 | ±0.0282 | **-3.645** | **2.68e-04** | 0.9498 | *** |
| **BMI (kg/m2)** | **+0.0415** | 0.0178 | ±0.0357 | **+2.323** | **0.0202** | 1.0423 | * |
| Hypertension | +0.2556 | 0.3192 | ±0.6383 | +0.801 | 0.4232 | 1.2912 |  |
| High cholesterol | +0.5836 | 0.2999 | ±0.5997 | +1.946 | 0.0516 | 1.7925 | . |
| Kidney disease | +0.3548 | 0.5834 | ±1.1668 | +0.608 | 0.5431 | 1.4258 |  |
| **Circulatory disease** | **+0.9123** | 0.4244 | ±0.8487 | **+2.150** | **0.0316** | 2.4900 | * |
| Avg. daily mean/SD | -0.0876 | 0.1229 | ±0.2458 | -0.712 | 0.4762 | 0.9161 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.1144**, LLR χ² = **41.44** (p = **2.03e-05**), AUC = **0.7176**, AIC = **344.6**, BIC = **392.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.5985** | 1.4633 | ±2.9265 | **-2.459** | **0.0139** | 0.0274 | * |
| Education: graduate level (vs college) | -0.2440 | 0.3040 | ±0.6080 | -0.803 | 0.4222 | 0.7835 |  |
| Education: high school or below (vs college) | -0.1506 | 0.5045 | ±1.0089 | -0.298 | 0.7654 | 0.8602 |  |
| Site: UCSD (vs UAB) | -0.0039 | 0.3812 | ±0.7625 | -0.010 | 0.9918 | 0.9961 |  |
| Site: UW (vs UAB) | +0.3954 | 0.3643 | ±0.7287 | +1.085 | 0.2778 | 1.4850 |  |
| **Age (years)** | **-0.0470** | 0.0142 | ±0.0284 | **-3.309** | **9.36e-04** | 0.9541 | *** |
| **BMI (kg/m2)** | **+0.0489** | 0.0183 | ±0.0366 | **+2.671** | **0.0076** | 1.0501 | ** |
| Hypertension | +0.3275 | 0.3244 | ±0.6489 | +1.010 | 0.3127 | 1.3875 |  |
| High cholesterol | +0.5267 | 0.3049 | ±0.6098 | +1.728 | 0.0840 | 1.6934 | . |
| Kidney disease | +0.3132 | 0.5931 | ±1.1863 | +0.528 | 0.5974 | 1.3679 |  |
| **Circulatory disease** | **+0.9553** | 0.4328 | ±0.8656 | **+2.207** | **0.0273** | 2.5994 | * |
| **MAG (mg/dL/h)** | **+0.0793** | 0.0247 | ±0.0495 | **+3.206** | **0.0013** | 1.0826 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0897**, LLR χ² = **32.49** (p = **6.36e-04**), AUC = **0.6854**, AIC = **353.6**, BIC = **401.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6892 | 1.5349 | ±3.0698 | -1.101 | 0.2711 | 0.1847 |  |
| Education: graduate level (vs college) | -0.2380 | 0.3002 | ±0.6005 | -0.793 | 0.4278 | 0.7882 |  |
| Education: high school or below (vs college) | -0.0297 | 0.4941 | ±0.9882 | -0.060 | 0.9520 | 0.9707 |  |
| Site: UCSD (vs UAB) | -0.0402 | 0.3790 | ±0.7579 | -0.106 | 0.9155 | 0.9606 |  |
| Site: UW (vs UAB) | +0.2805 | 0.3582 | ±0.7165 | +0.783 | 0.4337 | 1.3237 |  |
| **Age (years)** | **-0.0518** | 0.0142 | ±0.0283 | **-3.653** | **2.59e-04** | 0.9496 | *** |
| **BMI (kg/m2)** | **+0.0440** | 0.0178 | ±0.0357 | **+2.470** | **0.0135** | 1.0450 | * |
| Hypertension | +0.2755 | 0.3205 | ±0.6410 | +0.860 | 0.3900 | 1.3172 |  |
| High cholesterol | +0.5744 | 0.3007 | ±0.6014 | +1.910 | 0.0561 | 1.7761 | . |
| Kidney disease | +0.3364 | 0.5859 | ±1.1719 | +0.574 | 0.5659 | 1.3999 |  |
| **Circulatory disease** | **+0.9125** | 0.4250 | ±0.8500 | **+2.147** | **0.0318** | 2.4905 | * |
| Avg. daily range (mg/dL) | +0.0166 | 0.0136 | ±0.0272 | +1.220 | 0.2225 | 1.0167 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0909**, LLR χ² = **32.93** (p = **5.41e-04**), AUC = **0.6908**, AIC = **353.1**, BIC = **400.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8550 | 1.0958 | ±2.1915 | -0.780 | 0.4352 | 0.4253 |  |
| Education: graduate level (vs college) | -0.2428 | 0.3008 | ±0.6016 | -0.807 | 0.4196 | 0.7845 |  |
| Education: high school or below (vs college) | -0.0524 | 0.4914 | ±0.9828 | -0.107 | 0.9151 | 0.9490 |  |
| Site: UCSD (vs UAB) | -0.0734 | 0.3773 | ±0.7546 | -0.194 | 0.8458 | 0.9293 |  |
| Site: UW (vs UAB) | +0.2258 | 0.3568 | ±0.7136 | +0.633 | 0.5268 | 1.2533 |  |
| **Age (years)** | **-0.0513** | 0.0141 | ±0.0281 | **-3.650** | **2.62e-04** | 0.9500 | *** |
| **BMI (kg/m2)** | **+0.0428** | 0.0178 | ±0.0357 | **+2.400** | **0.0164** | 1.0437 | * |
| Hypertension | +0.2262 | 0.3203 | ±0.6406 | +0.706 | 0.4801 | 1.2538 |  |
| High cholesterol | +0.5583 | 0.3002 | ±0.6003 | +1.860 | 0.0629 | 1.7478 | . |
| Kidney disease | +0.4035 | 0.5807 | ±1.1614 | +0.695 | 0.4871 | 1.4971 |  |
| **Circulatory disease** | **+0.9207** | 0.4231 | ±0.8463 | **+2.176** | **0.0296** | 2.5110 | * |
| SD of daily means (mg/dL) | +0.1087 | 0.0774 | ±0.1547 | +1.405 | 0.1600 | 1.1148 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0863**, LLR χ² = **31.25** (p = **0.0010**), AUC = **0.6817**, AIC = **354.8**, BIC = **402.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -24.9740 | 47.6036 | ±95.2072 | -0.525 | 0.5998 | 0.0000 |  |
| Education: graduate level (vs college) | -0.2460 | 0.2998 | ±0.5995 | -0.821 | 0.4119 | 0.7819 |  |
| Education: high school or below (vs college) | -0.0220 | 0.4912 | ±0.9823 | -0.045 | 0.9642 | 0.9782 |  |
| Site: UCSD (vs UAB) | -0.1093 | 0.3770 | ±0.7540 | -0.290 | 0.7718 | 0.8964 |  |
| Site: UW (vs UAB) | +0.2216 | 0.3559 | ±0.7117 | +0.623 | 0.5336 | 1.2480 |  |
| **Age (years)** | **-0.0515** | 0.0141 | ±0.0283 | **-3.647** | **2.65e-04** | 0.9498 | *** |
| **BMI (kg/m2)** | **+0.0418** | 0.0179 | ±0.0357 | **+2.341** | **0.0192** | 1.0427 | * |
| Hypertension | +0.2560 | 0.3184 | ±0.6368 | +0.804 | 0.4214 | 1.2918 |  |
| High cholesterol | +0.5822 | 0.2995 | ±0.5990 | +1.944 | 0.0519 | 1.7901 | . |
| Kidney disease | +0.4004 | 0.5805 | ±1.1609 | +0.690 | 0.4903 | 1.4925 |  |
| **Circulatory disease** | **+0.9018** | 0.4243 | ±0.8487 | **+2.125** | **0.0336** | 2.4640 | * |
| Time in range 70-180, pooled (%) | +0.2483 | 0.4785 | ±0.9571 | +0.519 | 0.6038 | 1.2819 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0856**, LLR χ² = **30.99** (p = **0.0011**), AUC = **0.6805**, AIC = **355.1**, BIC = **402.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -4.3819 | 45.7539 | ±91.5077 | -0.096 | 0.9237 | 0.0125 |  |
| Education: graduate level (vs college) | -0.2457 | 0.2997 | ±0.5993 | -0.820 | 0.4123 | 0.7822 |  |
| Education: high school or below (vs college) | -0.0204 | 0.4907 | ±0.9814 | -0.042 | 0.9668 | 0.9798 |  |
| Site: UCSD (vs UAB) | -0.0943 | 0.3766 | ±0.7531 | -0.250 | 0.8022 | 0.9100 |  |
| Site: UW (vs UAB) | +0.2328 | 0.3550 | ±0.7099 | +0.656 | 0.5119 | 1.2622 |  |
| **Age (years)** | **-0.0515** | 0.0141 | ±0.0283 | **-3.642** | **2.70e-04** | 0.9498 | *** |
| **BMI (kg/m2)** | **+0.0422** | 0.0178 | ±0.0356 | **+2.371** | **0.0177** | 1.0431 | * |
| Hypertension | +0.2522 | 0.3186 | ±0.6372 | +0.792 | 0.4286 | 1.2868 |  |
| High cholesterol | +0.5786 | 0.2995 | ±0.5990 | +1.932 | 0.0534 | 1.7835 | . |
| Kidney disease | +0.3800 | 0.5799 | ±1.1598 | +0.655 | 0.5123 | 1.4622 |  |
| **Circulatory disease** | **+0.9052** | 0.4242 | ±0.8484 | **+2.134** | **0.0329** | 2.4724 | * |
| Avg. daily time in range 70-180 (%) | +0.0413 | 0.4600 | ±0.9200 | +0.090 | 0.9285 | 1.0421 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0865**, LLR χ² = **31.33** (p = **9.76e-04**), AUC = **0.6825**, AIC = **354.7**, BIC = **402.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2347 | 1.0161 | ±2.0321 | -0.231 | 0.8173 | 0.7908 |  |
| Education: graduate level (vs college) | -0.2514 | 0.2999 | ±0.5998 | -0.838 | 0.4019 | 0.7777 |  |
| Education: high school or below (vs college) | -0.0354 | 0.4925 | ±0.9850 | -0.072 | 0.9427 | 0.9652 |  |
| Site: UCSD (vs UAB) | -0.1262 | 0.3799 | ±0.7597 | -0.332 | 0.7398 | 0.8815 |  |
| Site: UW (vs UAB) | +0.2124 | 0.3567 | ±0.7135 | +0.596 | 0.5515 | 1.2367 |  |
| **Age (years)** | **-0.0513** | 0.0141 | ±0.0282 | **-3.637** | **2.76e-04** | 0.9499 | *** |
| **BMI (kg/m2)** | **+0.0424** | 0.0178 | ±0.0355 | **+2.388** | **0.0169** | 1.0433 | * |
| Hypertension | +0.2709 | 0.3196 | ±0.6392 | +0.848 | 0.3967 | 1.3111 |  |
| High cholesterol | +0.5771 | 0.2996 | ±0.5992 | +1.926 | 0.0541 | 1.7809 | . |
| Kidney disease | +0.3576 | 0.5812 | ±1.1624 | +0.615 | 0.5384 | 1.4298 |  |
| **Circulatory disease** | **+0.9157** | 0.4247 | ±0.8494 | **+2.156** | **0.0311** | 2.4985 | * |
| Any reading < 54 during wear (0/1) | -0.2324 | 0.3998 | ±0.7995 | -0.581 | 0.5610 | 0.7926 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0874**, LLR χ² = **31.65** (p = **8.68e-04**), AUC = **0.6838**, AIC = **354.4**, BIC = **402.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2457 | 1.0131 | ±2.0261 | -0.242 | 0.8084 | 0.7822 |  |
| Education: graduate level (vs college) | -0.2499 | 0.3002 | ±0.6004 | -0.832 | 0.4053 | 0.7789 |  |
| Education: high school or below (vs college) | -0.0493 | 0.4931 | ±0.9863 | -0.100 | 0.9203 | 0.9519 |  |
| Site: UCSD (vs UAB) | -0.1280 | 0.3777 | ±0.7555 | -0.339 | 0.7346 | 0.8798 |  |
| Site: UW (vs UAB) | +0.2183 | 0.3556 | ±0.7112 | +0.614 | 0.5392 | 1.2440 |  |
| **Age (years)** | **-0.0517** | 0.0141 | ±0.0283 | **-3.661** | **2.51e-04** | 0.9496 | *** |
| **BMI (kg/m2)** | **+0.0434** | 0.0178 | ±0.0356 | **+2.439** | **0.0147** | 1.0444 | * |
| Hypertension | +0.2739 | 0.3195 | ±0.6390 | +0.857 | 0.3913 | 1.3151 |  |
| High cholesterol | +0.5716 | 0.2996 | ±0.5993 | +1.908 | 0.0564 | 1.7712 | . |
| Kidney disease | +0.3590 | 0.5808 | ±1.1616 | +0.618 | 0.5365 | 1.4319 |  |
| **Circulatory disease** | **+0.9326** | 0.4252 | ±0.8505 | **+2.193** | **0.0283** | 2.5411 | * |
| Time < 54 (%) | -2.2464 | 2.9194 | ±5.8388 | -0.769 | 0.4416 | 0.1058 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0863**, LLR χ² = **31.26** (p = **0.0010**), AUC = **0.6820**, AIC = **354.8**, BIC = **402.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.2699 | 1.0130 | ±2.0260 | -0.266 | 0.7899 | 0.7634 |  |
| Education: graduate level (vs college) | -0.2406 | 0.3000 | ±0.5999 | -0.802 | 0.4225 | 0.7862 |  |
| Education: high school or below (vs college) | -0.0294 | 0.4917 | ±0.9834 | -0.060 | 0.9523 | 0.9710 |  |
| Site: UCSD (vs UAB) | -0.1066 | 0.3763 | ±0.7526 | -0.283 | 0.7770 | 0.8989 |  |
| Site: UW (vs UAB) | +0.2291 | 0.3551 | ±0.7102 | +0.645 | 0.5189 | 1.2574 |  |
| **Age (years)** | **-0.0516** | 0.0141 | ±0.0283 | **-3.647** | **2.65e-04** | 0.9498 | *** |
| **BMI (kg/m2)** | **+0.0428** | 0.0178 | ±0.0356 | **+2.407** | **0.0161** | 1.0438 | * |
| Hypertension | +0.2595 | 0.3189 | ±0.6378 | +0.814 | 0.4158 | 1.2963 |  |
| High cholesterol | +0.5708 | 0.2998 | ±0.5995 | +1.904 | 0.0569 | 1.7696 | . |
| Kidney disease | +0.3726 | 0.5802 | ±1.1604 | +0.642 | 0.5207 | 1.4516 |  |
| **Circulatory disease** | **+0.9311** | 0.4271 | ±0.8542 | **+2.180** | **0.0293** | 2.5373 | * |
| Avg. daily time < 54 (%) | -1.6735 | 3.3367 | ±6.6734 | -0.502 | 0.6160 | 0.1876 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0906**, LLR χ² = **32.81** (p = **5.64e-04**), AUC = **0.6910**, AIC = **353.3**, BIC = **400.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.4354 | 1.0220 | ±2.0439 | -0.426 | 0.6701 | 0.6470 |  |
| Education: graduate level (vs college) | -0.2377 | 0.3004 | ±0.6008 | -0.791 | 0.4287 | 0.7884 |  |
| Education: high school or below (vs college) | -0.0615 | 0.4950 | ±0.9901 | -0.124 | 0.9012 | 0.9404 |  |
| Site: UCSD (vs UAB) | -0.0641 | 0.3765 | ±0.7531 | -0.170 | 0.8648 | 0.9379 |  |
| Site: UW (vs UAB) | +0.2798 | 0.3575 | ±0.7149 | +0.783 | 0.4338 | 1.3228 |  |
| **Age (years)** | **-0.0523** | 0.0142 | ±0.0284 | **-3.683** | **2.31e-04** | 0.9490 | *** |
| **BMI (kg/m2)** | **+0.0433** | 0.0179 | ±0.0357 | **+2.422** | **0.0154** | 1.0442 | * |
| Hypertension | +0.2921 | 0.3218 | ±0.6436 | +0.908 | 0.3640 | 1.3392 |  |
| High cholesterol | +0.5340 | 0.3021 | ±0.6041 | +1.768 | 0.0771 | 1.7057 | . |
| Kidney disease | +0.4387 | 0.5864 | ±1.1728 | +0.748 | 0.4544 | 1.5506 |  |
| **Circulatory disease** | **+0.9143** | 0.4257 | ±0.8514 | **+2.148** | **0.0317** | 2.4952 | * |
| Time 54-69, pooled (%) | +1.0300 | 0.7455 | ±1.4909 | +1.382 | 0.1671 | 2.8011 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0879**, LLR χ² = **31.82** (p = **8.14e-04**), AUC = **0.6845**, AIC = **354.3**, BIC = **401.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3662 | 1.0176 | ±2.0353 | -0.360 | 0.7189 | 0.6933 |  |
| Education: graduate level (vs college) | -0.2401 | 0.3000 | ±0.6001 | -0.800 | 0.4236 | 0.7866 |  |
| Education: high school or below (vs college) | -0.0540 | 0.4937 | ±0.9874 | -0.109 | 0.9129 | 0.9474 |  |
| Site: UCSD (vs UAB) | -0.0792 | 0.3759 | ±0.7518 | -0.211 | 0.8331 | 0.9239 |  |
| Site: UW (vs UAB) | +0.2525 | 0.3558 | ±0.7117 | +0.709 | 0.4780 | 1.2872 |  |
| **Age (years)** | **-0.0521** | 0.0142 | ±0.0284 | **-3.675** | **2.38e-04** | 0.9492 | *** |
| **BMI (kg/m2)** | **+0.0429** | 0.0178 | ±0.0356 | **+2.408** | **0.0160** | 1.0438 | * |
| Hypertension | +0.2973 | 0.3231 | ±0.6463 | +0.920 | 0.3575 | 1.3462 |  |
| High cholesterol | +0.5578 | 0.3006 | ±0.6012 | +1.856 | 0.0635 | 1.7469 | . |
| Kidney disease | +0.4176 | 0.5828 | ±1.1655 | +0.717 | 0.4737 | 1.5182 |  |
| **Circulatory disease** | **+0.8982** | 0.4247 | ±0.8494 | **+2.115** | **0.0345** | 2.4551 | * |
| Avg. daily time 54-69 (%) | +0.7110 | 0.7606 | ±1.5213 | +0.935 | 0.3499 | 2.0360 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0882**, LLR χ² = **31.93** (p = **7.82e-04**), AUC = **0.6856**, AIC = **354.1**, BIC = **401.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3875 | 1.0215 | ±2.0430 | -0.379 | 0.7044 | 0.6787 |  |
| Education: graduate level (vs college) | -0.2402 | 0.3000 | ±0.6001 | -0.801 | 0.4234 | 0.7865 |  |
| Education: high school or below (vs college) | -0.0345 | 0.4921 | ±0.9843 | -0.070 | 0.9441 | 0.9661 |  |
| Site: UCSD (vs UAB) | -0.0611 | 0.3770 | ±0.7540 | -0.162 | 0.8712 | 0.9407 |  |
| Site: UW (vs UAB) | +0.2683 | 0.3572 | ±0.7144 | +0.751 | 0.4526 | 1.3078 |  |
| **Age (years)** | **-0.0519** | 0.0142 | ±0.0284 | **-3.658** | **2.54e-04** | 0.9494 | *** |
| **BMI (kg/m2)** | **+0.0424** | 0.0178 | ±0.0357 | **+2.380** | **0.0173** | 1.0434 | * |
| Hypertension | +0.2689 | 0.3200 | ±0.6399 | +0.840 | 0.4008 | 1.3085 |  |
| High cholesterol | +0.5524 | 0.3010 | ±0.6020 | +1.835 | 0.0665 | 1.7375 | . |
| Kidney disease | +0.4215 | 0.5842 | ±1.1683 | +0.722 | 0.4706 | 1.5242 |  |
| **Circulatory disease** | **+0.9017** | 0.4252 | ±0.8504 | **+2.121** | **0.0340** | 2.4638 | * |
| Time < 70 (%) | +0.6563 | 0.6633 | ±1.3267 | +0.989 | 0.3225 | 1.9276 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0869**, LLR χ² = **31.47** (p = **9.28e-04**), AUC = **0.6823**, AIC = **354.6**, BIC = **402.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3399 | 1.0174 | ±2.0348 | -0.334 | 0.7383 | 0.7118 |  |
| Education: graduate level (vs college) | -0.2440 | 0.2998 | ±0.5997 | -0.814 | 0.4158 | 0.7835 |  |
| Education: high school or below (vs college) | -0.0387 | 0.4920 | ±0.9839 | -0.079 | 0.9373 | 0.9620 |  |
| Site: UCSD (vs UAB) | -0.0779 | 0.3760 | ±0.7521 | -0.207 | 0.8359 | 0.9251 |  |
| Site: UW (vs UAB) | +0.2482 | 0.3557 | ±0.7114 | +0.698 | 0.4853 | 1.2817 |  |
| **Age (years)** | **-0.0519** | 0.0142 | ±0.0283 | **-3.661** | **2.51e-04** | 0.9495 | *** |
| **BMI (kg/m2)** | **+0.0425** | 0.0178 | ±0.0356 | **+2.387** | **0.0170** | 1.0434 | * |
| Hypertension | +0.2798 | 0.3212 | ±0.6425 | +0.871 | 0.3837 | 1.3229 |  |
| High cholesterol | +0.5664 | 0.3001 | ±0.6001 | +1.888 | 0.0591 | 1.7619 | . |
| Kidney disease | +0.4063 | 0.5819 | ±1.1639 | +0.698 | 0.4851 | 1.5013 |  |
| **Circulatory disease** | **+0.8918** | 0.4249 | ±0.8498 | **+2.099** | **0.0358** | 2.4396 | * |
| Avg. daily time < 70 (%) | +0.4826 | 0.6837 | ±1.3674 | +0.706 | 0.4803 | 1.6203 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0878**, LLR χ² = **31.80** (p = **8.23e-04**), AUC = **0.6843**, AIC = **354.3**, BIC = **402.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -249.9017 | 295.6968 | ±591.3937 | -0.845 | 0.3980 | 0.0000 |  |
| Education: graduate level (vs college) | -0.2536 | 0.3005 | ±0.6010 | -0.844 | 0.3988 | 0.7760 |  |
| Education: high school or below (vs college) | -0.0547 | 0.4935 | ±0.9870 | -0.111 | 0.9118 | 0.9468 |  |
| Site: UCSD (vs UAB) | -0.1315 | 0.3777 | ±0.7555 | -0.348 | 0.7278 | 0.8768 |  |
| Site: UW (vs UAB) | +0.2195 | 0.3556 | ±0.7112 | +0.617 | 0.5371 | 1.2454 |  |
| **Age (years)** | **-0.0519** | 0.0141 | ±0.0283 | **-3.668** | **2.44e-04** | 0.9494 | *** |
| **BMI (kg/m2)** | **+0.0434** | 0.0178 | ±0.0356 | **+2.440** | **0.0147** | 1.0444 | * |
| Hypertension | +0.2745 | 0.3195 | ±0.6389 | +0.859 | 0.3901 | 1.3159 |  |
| High cholesterol | +0.5748 | 0.2998 | ±0.5996 | +1.917 | 0.0552 | 1.7768 | . |
| Kidney disease | +0.3561 | 0.5810 | ±1.1620 | +0.613 | 0.5400 | 1.4277 |  |
| **Circulatory disease** | **+0.9349** | 0.4253 | ±0.8506 | **+2.198** | **0.0279** | 2.5470 | * |
| Time 54-250, pooled (%) | +2.4967 | 2.9574 | ±5.9148 | +0.844 | 0.3985 | 12.1422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0867**, LLR χ² = **31.39** (p = **9.56e-04**), AUC = **0.6819**, AIC = **354.7**, BIC = **402.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -203.8564 | 340.4895 | ±680.9789 | -0.599 | 0.5494 | 0.0000 |  |
| Education: graduate level (vs college) | -0.2426 | 0.3000 | ±0.6000 | -0.809 | 0.4187 | 0.7846 |  |
| Education: high school or below (vs college) | -0.0334 | 0.4920 | ±0.9841 | -0.068 | 0.9458 | 0.9671 |  |
| Site: UCSD (vs UAB) | -0.1093 | 0.3763 | ±0.7526 | -0.290 | 0.7715 | 0.8965 |  |
| Site: UW (vs UAB) | +0.2305 | 0.3552 | ±0.7103 | +0.649 | 0.5162 | 1.2593 |  |
| **Age (years)** | **-0.0517** | 0.0141 | ±0.0283 | **-3.653** | **2.59e-04** | 0.9496 | *** |
| **BMI (kg/m2)** | **+0.0428** | 0.0178 | ±0.0356 | **+2.408** | **0.0160** | 1.0438 | * |
| Hypertension | +0.2592 | 0.3190 | ±0.6380 | +0.813 | 0.4164 | 1.2959 |  |
| High cholesterol | +0.5726 | 0.2998 | ±0.5995 | +1.910 | 0.0561 | 1.7729 | . |
| Kidney disease | +0.3707 | 0.5804 | ±1.1607 | +0.639 | 0.5229 | 1.4488 |  |
| **Circulatory disease** | **+0.9358** | 0.4271 | ±0.8541 | **+2.191** | **0.0284** | 2.5491 | * |
| Avg. daily time 54-250 (%) | +2.0360 | 3.4051 | ±6.8102 | +0.598 | 0.5499 | 7.6596 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0899**, LLR χ² = **32.56** (p = **6.19e-04**), AUC = **0.6880**, AIC = **353.5**, BIC = **401.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0326 | 1.0478 | ±2.0957 | -0.031 | 0.9752 | 0.9679 |  |
| Education: graduate level (vs college) | -0.2429 | 0.3003 | ±0.6006 | -0.809 | 0.4186 | 0.7844 |  |
| Education: high school or below (vs college) | -0.0362 | 0.4929 | ±0.9858 | -0.073 | 0.9414 | 0.9644 |  |
| Site: UCSD (vs UAB) | -0.1091 | 0.3763 | ±0.7526 | -0.290 | 0.7719 | 0.8967 |  |
| Site: UW (vs UAB) | +0.2325 | 0.3560 | ±0.7121 | +0.653 | 0.5137 | 1.2618 |  |
| **Age (years)** | **-0.0520** | 0.0142 | ±0.0284 | **-3.668** | **2.45e-04** | 0.9493 | *** |
| **BMI (kg/m2)** | **+0.0414** | 0.0181 | ±0.0362 | **+2.287** | **0.0222** | 1.0423 | * |
| Hypertension | +0.2735 | 0.3200 | ±0.6399 | +0.855 | 0.3927 | 1.3145 |  |
| High cholesterol | +0.5660 | 0.2998 | ±0.5997 | +1.888 | 0.0591 | 1.7611 | . |
| Kidney disease | +0.4707 | 0.5851 | ±1.1702 | +0.805 | 0.4211 | 1.6012 |  |
| **Circulatory disease** | **+0.8943** | 0.4256 | ±0.8511 | **+2.102** | **0.0356** | 2.4457 | * |
| Time 181-250, pooled (%) | -0.6456 | 0.5201 | ±1.0401 | -1.241 | 0.2145 | 0.5244 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0865**, LLR χ² = **31.31** (p = **9.83e-04**), AUC = **0.6824**, AIC = **354.8**, BIC = **402.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1562 | 1.0383 | ±2.0767 | -0.150 | 0.8804 | 0.8554 |  |
| Education: graduate level (vs college) | -0.2449 | 0.2999 | ±0.5998 | -0.817 | 0.4142 | 0.7828 |  |
| Education: high school or below (vs college) | -0.0340 | 0.4917 | ±0.9834 | -0.069 | 0.9448 | 0.9665 |  |
| Site: UCSD (vs UAB) | -0.1020 | 0.3760 | ±0.7519 | -0.271 | 0.7862 | 0.9030 |  |
| Site: UW (vs UAB) | +0.2339 | 0.3550 | ±0.7100 | +0.659 | 0.5100 | 1.2635 |  |
| **Age (years)** | **-0.0521** | 0.0142 | ±0.0284 | **-3.670** | **2.42e-04** | 0.9493 | *** |
| **BMI (kg/m2)** | **+0.0420** | 0.0178 | ±0.0356 | **+2.357** | **0.0184** | 1.0428 | * |
| Hypertension | +0.2603 | 0.3189 | ±0.6378 | +0.816 | 0.4145 | 1.2973 |  |
| High cholesterol | +0.5775 | 0.2994 | ±0.5987 | +1.929 | 0.0537 | 1.7816 | . |
| Kidney disease | +0.4030 | 0.5815 | ±1.1630 | +0.693 | 0.4882 | 1.4964 |  |
| **Circulatory disease** | **+0.8992** | 0.4247 | ±0.8493 | **+2.118** | **0.0342** | 2.4577 | * |
| Avg. daily time 181-250 (%) | -0.2874 | 0.5054 | ±1.0109 | -0.569 | 0.5697 | 0.7502 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0900**, LLR χ² = **32.60** (p = **6.10e-04**), AUC = **0.6882**, AIC = **353.5**, BIC = **401.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.0274 | 1.0486 | ±2.0972 | -0.026 | 0.9792 | 0.9730 |  |
| Education: graduate level (vs college) | -0.2436 | 0.3003 | ±0.6006 | -0.811 | 0.4172 | 0.7838 |  |
| Education: high school or below (vs college) | -0.0370 | 0.4929 | ±0.9859 | -0.075 | 0.9401 | 0.9636 |  |
| Site: UCSD (vs UAB) | -0.1093 | 0.3763 | ±0.7527 | -0.290 | 0.7715 | 0.8965 |  |
| Site: UW (vs UAB) | +0.2331 | 0.3561 | ±0.7121 | +0.655 | 0.5127 | 1.2625 |  |
| **Age (years)** | **-0.0521** | 0.0142 | ±0.0284 | **-3.669** | **2.43e-04** | 0.9492 | *** |
| **BMI (kg/m2)** | **+0.0414** | 0.0181 | ±0.0362 | **+2.284** | **0.0224** | 1.0422 | * |
| Hypertension | +0.2734 | 0.3200 | ±0.6400 | +0.854 | 0.3929 | 1.3144 |  |
| High cholesterol | +0.5668 | 0.2999 | ±0.5998 | +1.890 | 0.0587 | 1.7626 | . |
| Kidney disease | +0.4715 | 0.5851 | ±1.1702 | +0.806 | 0.4203 | 1.6024 |  |
| **Circulatory disease** | **+0.8941** | 0.4256 | ±0.8512 | **+2.101** | **0.0357** | 2.4450 | * |
| Time > 180 (%) | -0.6526 | 0.5196 | ±1.0391 | -1.256 | 0.2091 | 0.5207 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0865**, LLR χ² = **31.33** (p = **9.76e-04**), AUC = **0.6824**, AIC = **354.7**, BIC = **402.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.1515 | 1.0389 | ±2.0777 | -0.146 | 0.8841 | 0.8595 |  |
| Education: graduate level (vs college) | -0.2453 | 0.2999 | ±0.5998 | -0.818 | 0.4134 | 0.7825 |  |
| Education: high school or below (vs college) | -0.0348 | 0.4918 | ±0.9835 | -0.071 | 0.9436 | 0.9658 |  |
| Site: UCSD (vs UAB) | -0.1023 | 0.3760 | ±0.7520 | -0.272 | 0.7856 | 0.9028 |  |
| Site: UW (vs UAB) | +0.2342 | 0.3550 | ±0.7100 | +0.660 | 0.5095 | 1.2639 |  |
| **Age (years)** | **-0.0521** | 0.0142 | ±0.0284 | **-3.672** | **2.41e-04** | 0.9492 | *** |
| **BMI (kg/m2)** | **+0.0419** | 0.0178 | ±0.0356 | **+2.356** | **0.0185** | 1.0428 | * |
| Hypertension | +0.2603 | 0.3189 | ±0.6378 | +0.816 | 0.4144 | 1.2973 |  |
| High cholesterol | +0.5780 | 0.2994 | ±0.5988 | +1.931 | 0.0535 | 1.7825 | . |
| Kidney disease | +0.4036 | 0.5815 | ±1.1630 | +0.694 | 0.4876 | 1.4972 |  |
| **Circulatory disease** | **+0.8990** | 0.4247 | ±0.8494 | **+2.117** | **0.0343** | 2.4571 | * |
| Avg. daily time > 180 (%) | -0.2957 | 0.5048 | ±1.0096 | -0.586 | 0.5581 | 0.7440 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 393)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **393**, events = **68**, McFadden pseudo-R² = **0.0857**, LLR χ² = **31.01** (p = **0.0011**), AUC = **0.6805**, AIC = **355.1**, BIC = **402.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.3046 | 1.0250 | ±2.0500 | -0.297 | 0.7664 | 0.7374 |  |
| Education: graduate level (vs college) | -0.2434 | 0.3000 | ±0.6000 | -0.811 | 0.4172 | 0.7840 |  |
| Education: high school or below (vs college) | -0.0211 | 0.4909 | ±0.9817 | -0.043 | 0.9657 | 0.9791 |  |
| Site: UCSD (vs UAB) | -0.0875 | 0.3761 | ±0.7521 | -0.233 | 0.8160 | 0.9162 |  |
| Site: UW (vs UAB) | +0.2328 | 0.3549 | ±0.7098 | +0.656 | 0.5119 | 1.2621 |  |
| **Age (years)** | **-0.0509** | 0.0144 | ±0.0289 | **-3.530** | **4.16e-04** | 0.9503 | *** |
| **BMI (kg/m2)** | **+0.0419** | 0.0179 | ±0.0357 | **+2.345** | **0.0190** | 1.0428 | * |
| Hypertension | +0.2499 | 0.3189 | ±0.6378 | +0.784 | 0.4333 | 1.2839 |  |
| High cholesterol | +0.5735 | 0.3002 | ±0.6004 | +1.910 | 0.0561 | 1.7745 | . |
| Kidney disease | +0.3712 | 0.5816 | ±1.1633 | +0.638 | 0.5233 | 1.4495 |  |
| **Circulatory disease** | **+0.9063** | 0.4243 | ±0.8487 | **+2.136** | **0.0327** | 2.4751 | * |
| Nocturnal time > 180 (%) | +0.0630 | 0.3548 | ±0.7095 | +0.178 | 0.8590 | 1.0651 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 384; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **384**, R² = **0.1418**, Adj R² = **0.1116**, F-statistic = **4.70** (p = **1.52e-07**), Residual SE = **0.869** on **370** df, AIC = **995.6**, BIC = **1050.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7434** | 0.2892 | ±0.5785 | **+6.027** | **1.67e-09** | *** |
| Education: graduate level (vs college) | -0.0865 | 0.0966 | ±0.1931 | -0.895 | 0.3706 |  |
| Education: high school or below (vs college) | +0.3106 | 0.1965 | ±0.3929 | +1.581 | 0.1139 |  |
| Site: UCSD (vs UAB) | +0.0137 | 0.1167 | ±0.2335 | +0.117 | 0.9067 |  |
| **Site: UW (vs UAB)** | **-0.3611** | 0.1259 | ±0.2517 | **-2.869** | **0.0041** | ** |
| Season: spring (vs autumn) | -0.1346 | 0.1240 | ±0.2479 | -1.086 | 0.2774 |  |
| Season: summer (vs autumn) | +0.1862 | 0.1481 | ±0.2963 | +1.257 | 0.2086 |  |
| Season: winter (vs autumn) | -0.0393 | 0.1307 | ±0.2614 | -0.301 | 0.7637 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0074 | **-2.011** | **0.0443** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0070 | ±0.0139 | **+3.333** | **8.60e-04** | *** |
| Hypertension | +0.1148 | 0.1094 | ±0.2187 | +1.050 | 0.2939 |  |
| High cholesterol | -0.0403 | 0.0902 | ±0.1803 | -0.447 | 0.6546 |  |
| Kidney disease | -0.1015 | 0.1579 | ±0.3159 | -0.642 | 0.5207 |  |
| Circulatory disease | +0.3080 | 0.1872 | ±0.3743 | +1.646 | 0.0998 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **384**, R² = **0.1436**, Adj R² = **0.1111**, F-statistic = **4.42** (p = **2.50e-07**), Residual SE = **0.869** on **369** df, AIC = **996.8**, BIC = **1056.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0032 | 1.0107 | ±2.0214 | +0.993 | 0.3209 |  |
| Education: graduate level (vs college) | -0.0858 | 0.0968 | ±0.1935 | -0.886 | 0.3754 |  |
| Education: high school or below (vs college) | +0.3057 | 0.1955 | ±0.3911 | +1.563 | 0.1180 |  |
| Site: UCSD (vs UAB) | +0.0142 | 0.1171 | ±0.2343 | +0.121 | 0.9034 |  |
| **Site: UW (vs UAB)** | **-0.3578** | 0.1262 | ±0.2524 | **-2.836** | **0.0046** | ** |
| Season: spring (vs autumn) | -0.1162 | 0.1229 | ±0.2458 | -0.945 | 0.3446 |  |
| Season: summer (vs autumn) | +0.1776 | 0.1501 | ±0.3003 | +1.183 | 0.2367 |  |
| Season: winter (vs autumn) | -0.0337 | 0.1305 | ±0.2610 | -0.259 | 0.7959 |  |
| **Age (years)** | **-0.0079** | 0.0038 | ±0.0076 | **-2.072** | **0.0383** | * |
| **BMI (kg/m2)** | **+0.0227** | 0.0070 | ±0.0139 | **+3.267** | **0.0011** | ** |
| Hypertension | +0.1072 | 0.1112 | ±0.2223 | +0.964 | 0.3349 |  |
| High cholesterol | -0.0582 | 0.0935 | ±0.1869 | -0.623 | 0.5334 |  |
| Kidney disease | -0.0895 | 0.1593 | ±0.3185 | -0.562 | 0.5743 |  |
| Circulatory disease | +0.3202 | 0.1887 | ±0.3773 | +1.697 | 0.0896 | . |
| HbA1c (%) | +0.1416 | 0.1870 | ±0.3740 | +0.757 | 0.4489 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **384**, R² = **0.1477**, Adj R² = **0.1154**, F-statistic = **4.57** (p = **1.21e-07**), Residual SE = **0.867** on **369** df, AIC = **995.0**, BIC = **1054.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.8228** | 0.7919 | ±1.5839 | **+3.565** | **3.65e-04** | *** |
| Education: graduate level (vs college) | -0.0828 | 0.0966 | ±0.1932 | -0.857 | 0.3914 |  |
| Education: high school or below (vs college) | +0.3048 | 0.1951 | ±0.3903 | +1.562 | 0.1182 |  |
| Site: UCSD (vs UAB) | +0.0235 | 0.1175 | ±0.2351 | +0.200 | 0.8417 |  |
| **Site: UW (vs UAB)** | **-0.3496** | 0.1261 | ±0.2523 | **-2.771** | **0.0056** | ** |
| Season: spring (vs autumn) | -0.1435 | 0.1239 | ±0.2477 | -1.158 | 0.2468 |  |
| Season: summer (vs autumn) | +0.1872 | 0.1476 | ±0.2953 | +1.268 | 0.2048 |  |
| Season: winter (vs autumn) | -0.0434 | 0.1313 | ±0.2627 | -0.330 | 0.7413 |  |
| **Age (years)** | **-0.0077** | 0.0038 | ±0.0076 | **-2.038** | **0.0416** | * |
| **BMI (kg/m2)** | **+0.0240** | 0.0069 | ±0.0138 | **+3.468** | **5.24e-04** | *** |
| Hypertension | +0.1259 | 0.1106 | ±0.2212 | +1.138 | 0.2551 |  |
| High cholesterol | -0.0470 | 0.0903 | ±0.1807 | -0.520 | 0.6031 |  |
| Kidney disease | -0.0906 | 0.1617 | ±0.3233 | -0.561 | 0.5751 |  |
| Circulatory disease | +0.3040 | 0.1884 | ±0.3767 | +1.614 | 0.1066 |  |
| Mean glucose (mg/dL) | -0.0096 | 0.0060 | ±0.0120 | -1.596 | 0.1106 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **384**, R² = **0.1477**, Adj R² = **0.1154**, F-statistic = **4.57** (p = **1.21e-07**), Residual SE = **0.867** on **369** df, AIC = **995.0**, BIC = **1054.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+4.1454** | 1.5935 | ±3.1871 | **+2.601** | **0.0093** | ** |
| Education: graduate level (vs college) | -0.0828 | 0.0966 | ±0.1932 | -0.857 | 0.3914 |  |
| Education: high school or below (vs college) | +0.3048 | 0.1951 | ±0.3903 | +1.562 | 0.1182 |  |
| Site: UCSD (vs UAB) | +0.0235 | 0.1175 | ±0.2351 | +0.200 | 0.8417 |  |
| **Site: UW (vs UAB)** | **-0.3496** | 0.1261 | ±0.2523 | **-2.771** | **0.0056** | ** |
| Season: spring (vs autumn) | -0.1435 | 0.1239 | ±0.2477 | -1.158 | 0.2468 |  |
| Season: summer (vs autumn) | +0.1872 | 0.1476 | ±0.2953 | +1.268 | 0.2048 |  |
| Season: winter (vs autumn) | -0.0434 | 0.1313 | ±0.2627 | -0.330 | 0.7413 |  |
| **Age (years)** | **-0.0077** | 0.0038 | ±0.0076 | **-2.038** | **0.0416** | * |
| **BMI (kg/m2)** | **+0.0240** | 0.0069 | ±0.0138 | **+3.468** | **5.24e-04** | *** |
| Hypertension | +0.1259 | 0.1106 | ±0.2212 | +1.138 | 0.2551 |  |
| High cholesterol | -0.0470 | 0.0903 | ±0.1807 | -0.520 | 0.6031 |  |
| Kidney disease | -0.0906 | 0.1617 | ±0.3233 | -0.561 | 0.5751 |  |
| Circulatory disease | +0.3040 | 0.1884 | ±0.3767 | +1.614 | 0.1066 |  |
| GMI (%) | -0.3996 | 0.2504 | ±0.5008 | -1.596 | 0.1106 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **384**, R² = **0.1433**, Adj R² = **0.1108**, F-statistic = **4.41** (p = **2.64e-07**), Residual SE = **0.869** on **369** df, AIC = **996.9**, BIC = **1056.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1897** | 0.6537 | ±1.3075 | **+3.350** | **8.09e-04** | *** |
| Education: graduate level (vs college) | -0.0896 | 0.0975 | ±0.1950 | -0.919 | 0.3583 |  |
| Education: high school or below (vs college) | +0.3043 | 0.1972 | ±0.3944 | +1.543 | 0.1227 |  |
| Site: UCSD (vs UAB) | +0.0235 | 0.1190 | ±0.2381 | +0.197 | 0.8435 |  |
| **Site: UW (vs UAB)** | **-0.3527** | 0.1271 | ±0.2541 | **-2.776** | **0.0055** | ** |
| Season: spring (vs autumn) | -0.1353 | 0.1245 | ±0.2489 | -1.087 | 0.2769 |  |
| Season: summer (vs autumn) | +0.1890 | 0.1486 | ±0.2972 | +1.272 | 0.2035 |  |
| Season: winter (vs autumn) | -0.0392 | 0.1313 | ±0.2627 | -0.298 | 0.7654 |  |
| **Age (years)** | **-0.0080** | 0.0039 | ±0.0078 | **-2.029** | **0.0424** | * |
| **BMI (kg/m2)** | **+0.0241** | 0.0070 | ±0.0140 | **+3.452** | **5.57e-04** | *** |
| Hypertension | +0.1182 | 0.1102 | ±0.2204 | +1.072 | 0.2836 |  |
| High cholesterol | -0.0409 | 0.0904 | ±0.1808 | -0.452 | 0.6510 |  |
| Kidney disease | -0.1041 | 0.1611 | ±0.3221 | -0.646 | 0.5181 |  |
| Circulatory disease | +0.3047 | 0.1896 | ±0.3792 | +1.607 | 0.1081 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0039 | 0.0046 | ±0.0093 | -0.843 | 0.3992 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **384**, R² = **0.1426**, Adj R² = **0.1101**, F-statistic = **4.38** (p = **2.98e-07**), Residual SE = **0.870** on **369** df, AIC = **997.2**, BIC = **1056.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9406** | 0.4433 | ±0.8865 | **+4.378** | **1.20e-05** | *** |
| Education: graduate level (vs college) | -0.0896 | 0.0974 | ±0.1947 | -0.921 | 0.3572 |  |
| Education: high school or below (vs college) | +0.3114 | 0.1964 | ±0.3929 | +1.585 | 0.1129 |  |
| Site: UCSD (vs UAB) | +0.0073 | 0.1165 | ±0.2329 | +0.062 | 0.9503 |  |
| **Site: UW (vs UAB)** | **-0.3650** | 0.1257 | ±0.2513 | **-2.905** | **0.0037** | ** |
| Season: spring (vs autumn) | -0.1289 | 0.1250 | ±0.2500 | -1.032 | 0.3023 |  |
| Season: summer (vs autumn) | +0.1900 | 0.1487 | ±0.2973 | +1.278 | 0.2012 |  |
| Season: winter (vs autumn) | -0.0332 | 0.1334 | ±0.2669 | -0.249 | 0.8033 |  |
| **Age (years)** | **-0.0074** | 0.0037 | ±0.0075 | **-1.999** | **0.0456** | * |
| **BMI (kg/m2)** | **+0.0234** | 0.0070 | ±0.0139 | **+3.362** | **7.74e-04** | *** |
| Hypertension | +0.1150 | 0.1095 | ±0.2190 | +1.050 | 0.2937 |  |
| High cholesterol | -0.0431 | 0.0907 | ±0.1815 | -0.475 | 0.6344 |  |
| Kidney disease | -0.0965 | 0.1601 | ±0.3203 | -0.603 | 0.5468 |  |
| Circulatory disease | +0.3104 | 0.1867 | ±0.3733 | +1.663 | 0.0963 | . |
| Glucose SD, pooled (mg/dL) | -0.0121 | 0.0198 | ±0.0396 | -0.610 | 0.5419 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **384**, R² = **0.1425**, Adj R² = **0.1100**, F-statistic = **4.38** (p = **3.04e-07**), Residual SE = **0.870** on **369** df, AIC = **997.3**, BIC = **1056.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.9065** | 0.4120 | ±0.8241 | **+4.627** | **3.71e-06** | *** |
| Education: graduate level (vs college) | -0.0898 | 0.0976 | ±0.1952 | -0.920 | 0.3576 |  |
| Education: high school or below (vs college) | +0.3097 | 0.1960 | ±0.3921 | +1.580 | 0.1142 |  |
| Site: UCSD (vs UAB) | +0.0074 | 0.1170 | ±0.2339 | +0.063 | 0.9494 |  |
| **Site: UW (vs UAB)** | **-0.3649** | 0.1256 | ±0.2513 | **-2.904** | **0.0037** | ** |
| Season: spring (vs autumn) | -0.1302 | 0.1251 | ±0.2502 | -1.041 | 0.2981 |  |
| Season: summer (vs autumn) | +0.1886 | 0.1490 | ±0.2979 | +1.266 | 0.2054 |  |
| Season: winter (vs autumn) | -0.0361 | 0.1325 | ±0.2650 | -0.273 | 0.7851 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-2.001** | **0.0454** | * |
| **BMI (kg/m2)** | **+0.0235** | 0.0069 | ±0.0139 | **+3.397** | **6.82e-04** | *** |
| Hypertension | +0.1139 | 0.1093 | ±0.2186 | +1.042 | 0.2974 |  |
| High cholesterol | -0.0423 | 0.0907 | ±0.1813 | -0.467 | 0.6406 |  |
| Kidney disease | -0.0968 | 0.1598 | ±0.3195 | -0.606 | 0.5447 |  |
| Circulatory disease | +0.3086 | 0.1870 | ±0.3740 | +1.650 | 0.0989 | . |
| Avg. daily SD (mg/dL) | -0.0110 | 0.0189 | ±0.0378 | -0.584 | 0.5592 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **384**, R² = **0.1419**, Adj R² = **0.1093**, F-statistic = **4.36** (p = **3.40e-07**), Residual SE = **0.870** on **369** df, AIC = **997.6**, BIC = **1056.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6917** | 0.4147 | ±0.8293 | **+4.080** | **4.51e-05** | *** |
| Education: graduate level (vs college) | -0.0854 | 0.0973 | ±0.1945 | -0.878 | 0.3797 |  |
| Education: high school or below (vs college) | +0.3101 | 0.1969 | ±0.3937 | +1.575 | 0.1152 |  |
| Site: UCSD (vs UAB) | +0.0158 | 0.1175 | ±0.2349 | +0.135 | 0.8930 |  |
| **Site: UW (vs UAB)** | **-0.3595** | 0.1261 | ±0.2523 | **-2.850** | **0.0044** | ** |
| Season: spring (vs autumn) | -0.1366 | 0.1245 | ±0.2489 | -1.097 | 0.2725 |  |
| Season: summer (vs autumn) | +0.1852 | 0.1481 | ±0.2963 | +1.250 | 0.2113 |  |
| Season: winter (vs autumn) | -0.0411 | 0.1330 | ±0.2659 | -0.309 | 0.7573 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-2.000** | **0.0455** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0070 | ±0.0140 | **+3.327** | **8.78e-04** | *** |
| Hypertension | +0.1153 | 0.1098 | ±0.2196 | +1.050 | 0.2938 |  |
| High cholesterol | -0.0399 | 0.0906 | ±0.1812 | -0.440 | 0.6600 |  |
| Kidney disease | -0.1021 | 0.1582 | ±0.3163 | -0.646 | 0.5184 |  |
| Circulatory disease | +0.3072 | 0.1875 | ±0.3751 | +1.638 | 0.1014 |  |
| CV (%) | +0.0036 | 0.0217 | ±0.0433 | +0.164 | 0.8694 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **384**, R² = **0.1418**, Adj R² = **0.1092**, F-statistic = **4.35** (p = **3.44e-07**), Residual SE = **0.870** on **369** df, AIC = **997.6**, BIC = **1056.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7424** | 0.4332 | ±0.8664 | **+4.022** | **5.76e-05** | *** |
| Education: graduate level (vs college) | -0.0865 | 0.0974 | ±0.1947 | -0.888 | 0.3744 |  |
| Education: high school or below (vs college) | +0.3106 | 0.1968 | ±0.3936 | +1.578 | 0.1145 |  |
| Site: UCSD (vs UAB) | +0.0136 | 0.1174 | ±0.2348 | +0.116 | 0.9074 |  |
| **Site: UW (vs UAB)** | **-0.3611** | 0.1262 | ±0.2523 | **-2.862** | **0.0042** | ** |
| Season: spring (vs autumn) | -0.1346 | 0.1246 | ±0.2492 | -1.080 | 0.2800 |  |
| Season: summer (vs autumn) | +0.1863 | 0.1483 | ±0.2966 | +1.256 | 0.2091 |  |
| Season: winter (vs autumn) | -0.0393 | 0.1328 | ±0.2656 | -0.296 | 0.7675 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-2.002** | **0.0453** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0070 | ±0.0140 | **+3.326** | **8.80e-04** | *** |
| Hypertension | +0.1148 | 0.1097 | ±0.2194 | +1.047 | 0.2952 |  |
| High cholesterol | -0.0403 | 0.0905 | ±0.1811 | -0.446 | 0.6559 |  |
| Kidney disease | -0.1014 | 0.1584 | ±0.3168 | -0.640 | 0.5219 |  |
| Circulatory disease | +0.3081 | 0.1873 | ±0.3745 | +1.645 | 0.1000 | . |
| Mean / SD ratio | +0.0001 | 0.0436 | ±0.0873 | +0.003 | 0.9973 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **384**, R² = **0.1419**, Adj R² = **0.1093**, F-statistic = **4.36** (p = **3.37e-07**), Residual SE = **0.870** on **369** df, AIC = **997.6**, BIC = **1056.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8062** | 0.4139 | ±0.8278 | **+4.364** | **1.28e-05** | *** |
| Education: graduate level (vs college) | -0.0848 | 0.0976 | ±0.1952 | -0.868 | 0.3851 |  |
| Education: high school or below (vs college) | +0.3105 | 0.1969 | ±0.3939 | +1.577 | 0.1148 |  |
| Site: UCSD (vs UAB) | +0.0162 | 0.1177 | ±0.2354 | +0.137 | 0.8908 |  |
| **Site: UW (vs UAB)** | **-0.3595** | 0.1261 | ±0.2521 | **-2.852** | **0.0043** | ** |
| Season: spring (vs autumn) | -0.1373 | 0.1247 | ±0.2494 | -1.101 | 0.2709 |  |
| Season: summer (vs autumn) | +0.1852 | 0.1485 | ±0.2969 | +1.247 | 0.2123 |  |
| Season: winter (vs autumn) | -0.0410 | 0.1323 | ±0.2646 | -0.310 | 0.7569 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-2.005** | **0.0450** | * |
| **BMI (kg/m2)** | **+0.0231** | 0.0070 | ±0.0139 | **+3.325** | **8.85e-04** | *** |
| Hypertension | +0.1156 | 0.1097 | ±0.2193 | +1.054 | 0.2917 |  |
| High cholesterol | -0.0400 | 0.0905 | ±0.1809 | -0.442 | 0.6587 |  |
| Kidney disease | -0.1023 | 0.1580 | ±0.3160 | -0.647 | 0.5175 |  |
| Circulatory disease | +0.3076 | 0.1874 | ±0.3748 | +1.641 | 0.1007 |  |
| Avg. daily mean/SD | -0.0077 | 0.0343 | ±0.0687 | -0.224 | 0.8225 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **384**, R² = **0.1436**, Adj R² = **0.1111**, F-statistic = **4.42** (p = **2.51e-07**), Residual SE = **0.869** on **369** df, AIC = **996.8**, BIC = **1056.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.4650** | 0.4251 | ±0.8502 | **+3.446** | **5.68e-04** | *** |
| Education: graduate level (vs college) | -0.0885 | 0.0965 | ±0.1930 | -0.917 | 0.3591 |  |
| Education: high school or below (vs college) | +0.2991 | 0.1980 | ±0.3960 | +1.511 | 0.1309 |  |
| Site: UCSD (vs UAB) | +0.0216 | 0.1170 | ±0.2340 | +0.185 | 0.8532 |  |
| **Site: UW (vs UAB)** | **-0.3483** | 0.1276 | ±0.2552 | **-2.729** | **0.0064** | ** |
| Season: spring (vs autumn) | -0.1401 | 0.1238 | ±0.2476 | -1.132 | 0.2578 |  |
| Season: summer (vs autumn) | +0.1868 | 0.1488 | ±0.2975 | +1.256 | 0.2092 |  |
| Season: winter (vs autumn) | -0.0450 | 0.1307 | ±0.2613 | -0.345 | 0.7303 |  |
| Age (years) | -0.0070 | 0.0038 | ±0.0076 | -1.850 | 0.0643 | . |
| **BMI (kg/m2)** | **+0.0236** | 0.0070 | ±0.0139 | **+3.396** | **6.83e-04** | *** |
| Hypertension | +0.1180 | 0.1093 | ±0.2186 | +1.080 | 0.2803 |  |
| High cholesterol | -0.0452 | 0.0903 | ±0.1805 | -0.501 | 0.6165 |  |
| Kidney disease | -0.1104 | 0.1539 | ±0.3077 | -0.717 | 0.4732 |  |
| Circulatory disease | +0.3081 | 0.1867 | ±0.3734 | +1.650 | 0.0989 | . |
| MAG (mg/dL/h) | +0.0069 | 0.0075 | ±0.0150 | +0.925 | 0.3552 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **384**, R² = **0.1431**, Adj R² = **0.1106**, F-statistic = **4.40** (p = **2.72e-07**), Residual SE = **0.869** on **369** df, AIC = **997.0**, BIC = **1056.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.0086** | 0.4598 | ±0.9197 | **+4.368** | **1.25e-05** | *** |
| Education: graduate level (vs college) | -0.0876 | 0.0969 | ±0.1937 | -0.904 | 0.3658 |  |
| Education: high school or below (vs college) | +0.3106 | 0.1963 | ±0.3927 | +1.582 | 0.1136 |  |
| Site: UCSD (vs UAB) | +0.0055 | 0.1172 | ±0.2344 | +0.047 | 0.9626 |  |
| **Site: UW (vs UAB)** | **-0.3670** | 0.1259 | ±0.2518 | **-2.914** | **0.0036** | ** |
| Season: spring (vs autumn) | -0.1280 | 0.1249 | ±0.2497 | -1.025 | 0.3053 |  |
| Season: summer (vs autumn) | +0.1888 | 0.1486 | ±0.2972 | +1.270 | 0.2039 |  |
| Season: winter (vs autumn) | -0.0330 | 0.1334 | ±0.2667 | -0.247 | 0.8045 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-2.019** | **0.0435** | * |
| **BMI (kg/m2)** | **+0.0229** | 0.0070 | ±0.0141 | **+3.252** | **0.0011** | ** |
| Hypertension | +0.1110 | 0.1089 | ±0.2178 | +1.020 | 0.3079 |  |
| High cholesterol | -0.0396 | 0.0903 | ±0.1806 | -0.439 | 0.6606 |  |
| Kidney disease | -0.0977 | 0.1608 | ±0.3216 | -0.608 | 0.5435 |  |
| Circulatory disease | +0.3103 | 0.1866 | ±0.3732 | +1.663 | 0.0963 | . |
| Avg. daily range (mg/dL) | -0.0031 | 0.0041 | ±0.0081 | -0.770 | 0.4413 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **384**, R² = **0.1442**, Adj R² = **0.1117**, F-statistic = **4.44** (p = **2.26e-07**), Residual SE = **0.869** on **369** df, AIC = **996.5**, BIC = **1055.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6310** | 0.3166 | ±0.6332 | **+5.152** | **2.58e-07** | *** |
| Education: graduate level (vs college) | -0.0906 | 0.0968 | ±0.1937 | -0.935 | 0.3496 |  |
| Education: high school or below (vs college) | +0.3000 | 0.1946 | ±0.3892 | +1.542 | 0.1231 |  |
| Site: UCSD (vs UAB) | +0.0167 | 0.1166 | ±0.2333 | +0.143 | 0.8864 |  |
| **Site: UW (vs UAB)** | **-0.3659** | 0.1259 | ±0.2518 | **-2.906** | **0.0037** | ** |
| Season: spring (vs autumn) | -0.1435 | 0.1236 | ±0.2471 | -1.161 | 0.2456 |  |
| Season: summer (vs autumn) | +0.1766 | 0.1502 | ±0.3005 | +1.175 | 0.2399 |  |
| Season: winter (vs autumn) | -0.0529 | 0.1317 | ±0.2634 | -0.402 | 0.6878 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-2.022** | **0.0432** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0070 | ±0.0139 | **+3.333** | **8.61e-04** | *** |
| Hypertension | +0.1084 | 0.1099 | ±0.2198 | +0.987 | 0.3238 |  |
| High cholesterol | -0.0423 | 0.0906 | ±0.1811 | -0.467 | 0.6406 |  |
| Kidney disease | -0.0901 | 0.1569 | ±0.3138 | -0.574 | 0.5657 |  |
| Circulatory disease | +0.2996 | 0.1861 | ±0.3721 | +1.610 | 0.1074 |  |
| SD of daily means (mg/dL) | +0.0262 | 0.0274 | ±0.0548 | +0.956 | 0.3390 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **384**, R² = **0.1418**, Adj R² = **0.1093**, F-statistic = **4.36** (p = **3.40e-07**), Residual SE = **0.870** on **369** df, AIC = **997.6**, BIC = **1056.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5507 | 15.8108 | ±31.6215 | -0.035 | 0.9722 |  |
| Education: graduate level (vs college) | -0.0865 | 0.0968 | ±0.1936 | -0.893 | 0.3717 |  |
| Education: high school or below (vs college) | +0.3108 | 0.1969 | ±0.3939 | +1.578 | 0.1145 |  |
| Site: UCSD (vs UAB) | +0.0125 | 0.1182 | ±0.2364 | +0.105 | 0.9161 |  |
| **Site: UW (vs UAB)** | **-0.3620** | 0.1272 | ±0.2543 | **-2.846** | **0.0044** | ** |
| Season: spring (vs autumn) | -0.1337 | 0.1244 | ±0.2489 | -1.075 | 0.2826 |  |
| Season: summer (vs autumn) | +0.1876 | 0.1496 | ±0.2991 | +1.254 | 0.2097 |  |
| Season: winter (vs autumn) | -0.0380 | 0.1333 | ±0.2667 | -0.285 | 0.7758 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-2.006** | **0.0448** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0070 | ±0.0140 | **+3.315** | **9.17e-04** | *** |
| Hypertension | +0.1147 | 0.1096 | ±0.2192 | +1.047 | 0.2950 |  |
| High cholesterol | -0.0397 | 0.0904 | ±0.1808 | -0.439 | 0.6608 |  |
| Kidney disease | -0.1003 | 0.1588 | ±0.3177 | -0.632 | 0.5277 |  |
| Circulatory disease | +0.3086 | 0.1873 | ±0.3745 | +1.648 | 0.0994 | . |
| Time in range 70-180, pooled (%) | +0.0231 | 0.1590 | ±0.3181 | +0.145 | 0.8846 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **384**, R² = **0.1418**, Adj R² = **0.1092**, F-statistic = **4.35** (p = **3.43e-07**), Residual SE = **0.870** on **369** df, AIC = **997.6**, BIC = **1056.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0613 | 15.5192 | ±31.0384 | +0.068 | 0.9455 |  |
| Education: graduate level (vs college) | -0.0865 | 0.0968 | ±0.1936 | -0.893 | 0.3719 |  |
| Education: high school or below (vs college) | +0.3105 | 0.1974 | ±0.3947 | +1.574 | 0.1156 |  |
| Site: UCSD (vs UAB) | +0.0134 | 0.1180 | ±0.2360 | +0.114 | 0.9094 |  |
| **Site: UW (vs UAB)** | **-0.3612** | 0.1264 | ±0.2528 | **-2.857** | **0.0043** | ** |
| Season: spring (vs autumn) | -0.1344 | 0.1244 | ±0.2488 | -1.081 | 0.2798 |  |
| Season: summer (vs autumn) | +0.1864 | 0.1490 | ±0.2980 | +1.251 | 0.2110 |  |
| Season: winter (vs autumn) | -0.0390 | 0.1327 | ±0.2653 | -0.294 | 0.7689 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-1.998** | **0.0458** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0070 | ±0.0140 | **+3.324** | **8.88e-04** | *** |
| Hypertension | +0.1146 | 0.1092 | ±0.2185 | +1.049 | 0.2941 |  |
| High cholesterol | -0.0401 | 0.0904 | ±0.1808 | -0.443 | 0.6576 |  |
| Kidney disease | -0.1014 | 0.1586 | ±0.3173 | -0.639 | 0.5228 |  |
| Circulatory disease | +0.3083 | 0.1879 | ±0.3758 | +1.641 | 0.1008 |  |
| Avg. daily time in range 70-180 (%) | +0.0069 | 0.1560 | ±0.3120 | +0.044 | 0.9649 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.1448**, Adj R² = **0.1124**, F-statistic = **4.46** (p = **2.03e-07**), Residual SE = **0.869** on **369** df, AIC = **996.3**, BIC = **1055.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7187** | 0.2958 | ±0.5916 | **+5.810** | **6.23e-09** | *** |
| Education: graduate level (vs college) | -0.0843 | 0.0963 | ±0.1925 | -0.876 | 0.3812 |  |
| Education: high school or below (vs college) | +0.3134 | 0.1986 | ±0.3972 | +1.578 | 0.1145 |  |
| Site: UCSD (vs UAB) | +0.0383 | 0.1212 | ±0.2424 | +0.316 | 0.7517 |  |
| **Site: UW (vs UAB)** | **-0.3452** | 0.1291 | ±0.2582 | **-2.673** | **0.0075** | ** |
| Season: spring (vs autumn) | -0.1531 | 0.1262 | ±0.2524 | -1.213 | 0.2252 |  |
| Season: summer (vs autumn) | +0.1771 | 0.1487 | ±0.2973 | +1.191 | 0.2336 |  |
| Season: winter (vs autumn) | -0.0520 | 0.1312 | ±0.2625 | -0.396 | 0.6918 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0074 | **-2.013** | **0.0442** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0070 | ±0.0139 | **+3.334** | **8.57e-04** | *** |
| Hypertension | +0.1055 | 0.1099 | ±0.2198 | +0.960 | 0.3371 |  |
| High cholesterol | -0.0402 | 0.0908 | ±0.1815 | -0.442 | 0.6583 |  |
| Kidney disease | -0.0865 | 0.1600 | ±0.3200 | -0.541 | 0.5887 |  |
| Circulatory disease | +0.2999 | 0.1872 | ±0.3744 | +1.602 | 0.1092 |  |
| Any reading < 54 during wear (0/1) | +0.1420 | 0.1498 | ±0.2996 | +0.948 | 0.3431 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.1508**, Adj R² = **0.1186**, F-statistic = **4.68** (p = **6.95e-08**), Residual SE = **0.866** on **369** df, AIC = **993.5**, BIC = **1052.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7046** | 0.2933 | ±0.5866 | **+5.811** | **6.20e-09** | *** |
| Education: graduate level (vs college) | -0.0851 | 0.0961 | ±0.1923 | -0.885 | 0.3761 |  |
| Education: high school or below (vs college) | +0.3279 | 0.1975 | ±0.3951 | +1.660 | 0.0969 | . |
| Site: UCSD (vs UAB) | +0.0437 | 0.1201 | ±0.2402 | +0.364 | 0.7157 |  |
| **Site: UW (vs UAB)** | **-0.3461** | 0.1274 | ±0.2548 | **-2.716** | **0.0066** | ** |
| Season: spring (vs autumn) | -0.1306 | 0.1236 | ±0.2472 | -1.057 | 0.2907 |  |
| Season: summer (vs autumn) | +0.1841 | 0.1482 | ±0.2965 | +1.242 | 0.2142 |  |
| Season: winter (vs autumn) | -0.0379 | 0.1290 | ±0.2581 | -0.294 | 0.7691 |  |
| Age (years) | -0.0071 | 0.0037 | ±0.0075 | -1.902 | 0.0572 | . |
| **BMI (kg/m2)** | **+0.0223** | 0.0070 | ±0.0139 | **+3.216** | **0.0013** | ** |
| Hypertension | +0.0996 | 0.1087 | ±0.2174 | +0.916 | 0.3597 |  |
| High cholesterol | -0.0382 | 0.0908 | ±0.1817 | -0.421 | 0.6738 |  |
| Kidney disease | -0.0848 | 0.1594 | ±0.3187 | -0.532 | 0.5948 |  |
| Circulatory disease | +0.2900 | 0.1848 | ±0.3695 | +1.570 | 0.1165 |  |
| Time < 54 (%) | +1.7790 | 1.1129 | ±2.2258 | +1.598 | 0.1099 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.1521**, Adj R² = **0.1199**, F-statistic = **4.73** (p = **5.56e-08**), Residual SE = **0.865** on **369** df, AIC = **993.0**, BIC = **1052.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7093** | 0.2908 | ±0.5816 | **+5.878** | **4.16e-09** | *** |
| Education: graduate level (vs college) | -0.0920 | 0.0975 | ±0.1950 | -0.943 | 0.3455 |  |
| Education: high school or below (vs college) | +0.3183 | 0.1958 | ±0.3916 | +1.625 | 0.1041 |  |
| Site: UCSD (vs UAB) | +0.0320 | 0.1195 | ±0.2389 | +0.268 | 0.7890 |  |
| **Site: UW (vs UAB)** | **-0.3540** | 0.1268 | ±0.2535 | **-2.793** | **0.0052** | ** |
| Season: spring (vs autumn) | -0.1281 | 0.1247 | ±0.2494 | -1.027 | 0.3043 |  |
| Season: summer (vs autumn) | +0.2071 | 0.1484 | ±0.2968 | +1.396 | 0.1628 |  |
| Season: winter (vs autumn) | -0.0347 | 0.1308 | ±0.2615 | -0.265 | 0.7907 |  |
| Age (years) | -0.0072 | 0.0037 | ±0.0075 | -1.910 | 0.0562 | . |
| **BMI (kg/m2)** | **+0.0227** | 0.0070 | ±0.0140 | **+3.235** | **0.0012** | ** |
| Hypertension | +0.1050 | 0.1078 | ±0.2157 | +0.973 | 0.3304 |  |
| High cholesterol | -0.0371 | 0.0910 | ±0.1819 | -0.408 | 0.6833 |  |
| Kidney disease | -0.0953 | 0.1602 | ±0.3205 | -0.595 | 0.5522 |  |
| Circulatory disease | +0.2811 | 0.1876 | ±0.3753 | +1.498 | 0.1341 |  |
| Avg. daily time < 54 (%) | +2.2870 | 1.5469 | ±3.0938 | +1.478 | 0.1393 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.1494**, Adj R² = **0.1171**, F-statistic = **4.63** (p = **8.99e-08**), Residual SE = **0.866** on **369** df, AIC = **994.2**, BIC = **1053.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6736** | 0.2916 | ±0.5833 | **+5.739** | **9.54e-09** | *** |
| Education: graduate level (vs college) | -0.0807 | 0.0960 | ±0.1919 | -0.842 | 0.4000 |  |
| Education: high school or below (vs college) | +0.2981 | 0.1969 | ±0.3937 | +1.514 | 0.1299 |  |
| Site: UCSD (vs UAB) | +0.0301 | 0.1184 | ±0.2368 | +0.254 | 0.7994 |  |
| **Site: UW (vs UAB)** | **-0.3418** | 0.1268 | ±0.2536 | **-2.695** | **0.0070** | ** |
| Season: spring (vs autumn) | -0.1435 | 0.1229 | ±0.2459 | -1.167 | 0.2431 |  |
| Season: summer (vs autumn) | +0.1832 | 0.1493 | ±0.2986 | +1.227 | 0.2198 |  |
| Season: winter (vs autumn) | -0.0533 | 0.1317 | ±0.2634 | -0.405 | 0.6858 |  |
| **Age (years)** | **-0.0076** | 0.0038 | ±0.0075 | **-2.013** | **0.0441** | * |
| **BMI (kg/m2)** | **+0.0235** | 0.0069 | ±0.0138 | **+3.392** | **6.95e-04** | *** |
| Hypertension | +0.1315 | 0.1098 | ±0.2195 | +1.198 | 0.2310 |  |
| High cholesterol | -0.0580 | 0.0902 | ±0.1803 | -0.643 | 0.5204 |  |
| Kidney disease | -0.0720 | 0.1557 | ±0.3114 | -0.463 | 0.6437 |  |
| Circulatory disease | +0.3062 | 0.1892 | ±0.3784 | +1.618 | 0.1056 |  |
| Time 54-69, pooled (%) | +0.4595 | 0.2854 | ±0.5707 | +1.610 | 0.1073 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **384**, R² = **0.1485**, Adj R² = **0.1162**, F-statistic = **4.60** (p = **1.05e-07**), Residual SE = **0.867** on **369** df, AIC = **994.6**, BIC = **1053.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6803** | 0.2910 | ±0.5820 | **+5.775** | **7.70e-09** | *** |
| Education: graduate level (vs college) | -0.0788 | 0.0959 | ±0.1919 | -0.821 | 0.4114 |  |
| Education: high school or below (vs college) | +0.2968 | 0.1961 | ±0.3923 | +1.513 | 0.1303 |  |
| Site: UCSD (vs UAB) | +0.0225 | 0.1178 | ±0.2356 | +0.191 | 0.8484 |  |
| **Site: UW (vs UAB)** | **-0.3521** | 0.1261 | ±0.2522 | **-2.792** | **0.0052** | ** |
| Season: spring (vs autumn) | -0.1314 | 0.1236 | ±0.2471 | -1.064 | 0.2874 |  |
| Season: summer (vs autumn) | +0.1937 | 0.1498 | ±0.2996 | +1.293 | 0.1961 |  |
| Season: winter (vs autumn) | -0.0483 | 0.1313 | ±0.2626 | -0.368 | 0.7130 |  |
| **Age (years)** | **-0.0075** | 0.0038 | ±0.0075 | **-2.006** | **0.0448** | * |
| **BMI (kg/m2)** | **+0.0234** | 0.0069 | ±0.0138 | **+3.381** | **7.21e-04** | *** |
| Hypertension | +0.1402 | 0.1118 | ±0.2236 | +1.254 | 0.2098 |  |
| High cholesterol | -0.0524 | 0.0904 | ±0.1808 | -0.580 | 0.5617 |  |
| Kidney disease | -0.0819 | 0.1558 | ±0.3116 | -0.525 | 0.5992 |  |
| Circulatory disease | +0.3014 | 0.1898 | ±0.3796 | +1.588 | 0.1123 |  |
| Avg. daily time 54-69 (%) | +0.4359 | 0.2967 | ±0.5934 | +1.469 | 0.1418 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **384**, R² = **0.1521**, Adj R² = **0.1199**, F-statistic = **4.73** (p = **5.51e-08**), Residual SE = **0.865** on **369** df, AIC = **993.0**, BIC = **1052.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6604** | 0.2939 | ±0.5877 | **+5.650** | **1.60e-08** | *** |
| Education: graduate level (vs college) | -0.0802 | 0.0956 | ±0.1913 | -0.838 | 0.4020 |  |
| Education: high school or below (vs college) | +0.3023 | 0.1975 | ±0.3950 | +1.530 | 0.1259 |  |
| Site: UCSD (vs UAB) | +0.0388 | 0.1192 | ±0.2384 | +0.326 | 0.7447 |  |
| **Site: UW (vs UAB)** | **-0.3370** | 0.1272 | ±0.2544 | **-2.649** | **0.0081** | ** |
| Season: spring (vs autumn) | -0.1428 | 0.1228 | ±0.2455 | -1.163 | 0.2448 |  |
| Season: summer (vs autumn) | +0.1825 | 0.1492 | ±0.2983 | +1.224 | 0.2211 |  |
| Season: winter (vs autumn) | -0.0535 | 0.1309 | ±0.2617 | -0.409 | 0.6828 |  |
| **Age (years)** | **-0.0075** | 0.0037 | ±0.0075 | **-1.995** | **0.0460** | * |
| **BMI (kg/m2)** | **+0.0232** | 0.0069 | ±0.0138 | **+3.375** | **7.38e-04** | *** |
| Hypertension | +0.1280 | 0.1089 | ±0.2178 | +1.176 | 0.2396 |  |
| High cholesterol | -0.0581 | 0.0901 | ±0.1803 | -0.645 | 0.5192 |  |
| Kidney disease | -0.0664 | 0.1560 | ±0.3120 | -0.425 | 0.6706 |  |
| Circulatory disease | +0.3013 | 0.1884 | ±0.3768 | +1.599 | 0.1098 |  |
| Time < 70 (%) | +0.4779 | 0.2622 | ±0.5244 | +1.822 | 0.0684 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **384**, R² = **0.1510**, Adj R² = **0.1188**, F-statistic = **4.69** (p = **6.73e-08**), Residual SE = **0.865** on **369** df, AIC = **993.5**, BIC = **1052.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6698** | 0.2916 | ±0.5832 | **+5.727** | **1.02e-08** | *** |
| Education: graduate level (vs college) | -0.0795 | 0.0957 | ±0.1915 | -0.830 | 0.4064 |  |
| Education: high school or below (vs college) | +0.2975 | 0.1964 | ±0.3928 | +1.515 | 0.1298 |  |
| Site: UCSD (vs UAB) | +0.0267 | 0.1183 | ±0.2365 | +0.226 | 0.8212 |  |
| **Site: UW (vs UAB)** | **-0.3501** | 0.1263 | ±0.2525 | **-2.773** | **0.0056** | ** |
| Season: spring (vs autumn) | -0.1299 | 0.1235 | ±0.2470 | -1.052 | 0.2927 |  |
| Season: summer (vs autumn) | +0.1983 | 0.1498 | ±0.2995 | +1.324 | 0.1854 |  |
| Season: winter (vs autumn) | -0.0479 | 0.1309 | ±0.2619 | -0.366 | 0.7145 |  |
| **Age (years)** | **-0.0075** | 0.0038 | ±0.0075 | **-1.992** | **0.0464** | * |
| **BMI (kg/m2)** | **+0.0233** | 0.0069 | ±0.0138 | **+3.373** | **7.43e-04** | *** |
| Hypertension | +0.1397 | 0.1112 | ±0.2225 | +1.256 | 0.2091 |  |
| High cholesterol | -0.0525 | 0.0903 | ±0.1806 | -0.581 | 0.5610 |  |
| Kidney disease | -0.0795 | 0.1561 | ±0.3122 | -0.509 | 0.6106 |  |
| Circulatory disease | +0.2955 | 0.1897 | ±0.3795 | +1.558 | 0.1193 |  |
| Avg. daily time < 70 (%) | +0.4613 | 0.2793 | ±0.5587 | +1.651 | 0.0987 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.1501**, Adj R² = **0.1179**, F-statistic = **4.66** (p = **7.87e-08**), Residual SE = **0.866** on **369** df, AIC = **993.9**, BIC = **1053.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +171.8998 | 110.0403 | ±220.0807 | +1.562 | 0.1183 |  |
| Education: graduate level (vs college) | -0.0840 | 0.0961 | ±0.1921 | -0.874 | 0.3819 |  |
| Education: high school or below (vs college) | +0.3281 | 0.1976 | ±0.3952 | +1.660 | 0.0969 | . |
| Site: UCSD (vs UAB) | +0.0425 | 0.1200 | ±0.2400 | +0.354 | 0.7230 |  |
| **Site: UW (vs UAB)** | **-0.3476** | 0.1273 | ±0.2546 | **-2.731** | **0.0063** | ** |
| Season: spring (vs autumn) | -0.1307 | 0.1236 | ±0.2471 | -1.057 | 0.2903 |  |
| Season: summer (vs autumn) | +0.1841 | 0.1482 | ±0.2964 | +1.242 | 0.2142 |  |
| Season: winter (vs autumn) | -0.0393 | 0.1291 | ±0.2583 | -0.305 | 0.7607 |  |
| Age (years) | -0.0071 | 0.0038 | ±0.0075 | -1.884 | 0.0595 | . |
| **BMI (kg/m2)** | **+0.0225** | 0.0069 | ±0.0139 | **+3.233** | **0.0012** | ** |
| Hypertension | +0.1007 | 0.1088 | ±0.2175 | +0.925 | 0.3547 |  |
| High cholesterol | -0.0399 | 0.0908 | ±0.1816 | -0.439 | 0.6607 |  |
| Kidney disease | -0.0851 | 0.1594 | ±0.3187 | -0.534 | 0.5933 |  |
| Circulatory disease | +0.2910 | 0.1848 | ±0.3697 | +1.574 | 0.1154 |  |
| Time 54-250, pooled (%) | -1.7020 | 1.1009 | ±2.2018 | -1.546 | 0.1221 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.1510**, Adj R² = **0.1188**, F-statistic = **4.69** (p = **6.71e-08**), Residual SE = **0.865** on **369** df, AIC = **993.5**, BIC = **1052.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +216.5489 | 148.3761 | ±296.7522 | +1.459 | 0.1444 |  |
| Education: graduate level (vs college) | -0.0900 | 0.0973 | ±0.1946 | -0.926 | 0.3547 |  |
| Education: high school or below (vs college) | +0.3191 | 0.1959 | ±0.3919 | +1.629 | 0.1034 |  |
| Site: UCSD (vs UAB) | +0.0310 | 0.1193 | ±0.2387 | +0.260 | 0.7950 |  |
| **Site: UW (vs UAB)** | **-0.3557** | 0.1265 | ±0.2531 | **-2.811** | **0.0049** | ** |
| Season: spring (vs autumn) | -0.1284 | 0.1246 | ±0.2491 | -1.031 | 0.3027 |  |
| Season: summer (vs autumn) | +0.2057 | 0.1483 | ±0.2966 | +1.387 | 0.1656 |  |
| Season: winter (vs autumn) | -0.0369 | 0.1307 | ±0.2614 | -0.283 | 0.7775 |  |
| Age (years) | -0.0071 | 0.0038 | ±0.0075 | -1.890 | 0.0588 | . |
| **BMI (kg/m2)** | **+0.0228** | 0.0070 | ±0.0140 | **+3.259** | **0.0011** | ** |
| Hypertension | +0.1061 | 0.1079 | ±0.2158 | +0.984 | 0.3253 |  |
| High cholesterol | -0.0394 | 0.0909 | ±0.1818 | -0.434 | 0.6643 |  |
| Kidney disease | -0.0951 | 0.1601 | ±0.3203 | -0.594 | 0.5527 |  |
| Circulatory disease | +0.2830 | 0.1875 | ±0.3750 | +1.509 | 0.1312 |  |
| Avg. daily time 54-250 (%) | -2.1484 | 1.4839 | ±2.9678 | -1.448 | 0.1477 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **384**, R² = **0.1480**, Adj R² = **0.1157**, F-statistic = **4.58** (p = **1.15e-07**), Residual SE = **0.867** on **369** df, AIC = **994.8**, BIC = **1054.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8457** | 0.3032 | ±0.6063 | **+6.088** | **1.14e-09** | *** |
| Education: graduate level (vs college) | -0.0832 | 0.0962 | ±0.1925 | -0.864 | 0.3876 |  |
| Education: high school or below (vs college) | +0.3084 | 0.1966 | ±0.3932 | +1.569 | 0.1167 |  |
| Site: UCSD (vs UAB) | +0.0135 | 0.1159 | ±0.2319 | +0.116 | 0.9075 |  |
| **Site: UW (vs UAB)** | **-0.3579** | 0.1246 | ±0.2491 | **-2.874** | **0.0041** | ** |
| Season: spring (vs autumn) | -0.1286 | 0.1244 | ±0.2488 | -1.034 | 0.3012 |  |
| Season: summer (vs autumn) | +0.1995 | 0.1495 | ±0.2990 | +1.335 | 0.1820 |  |
| Season: winter (vs autumn) | -0.0324 | 0.1315 | ±0.2631 | -0.246 | 0.8056 |  |
| **Age (years)** | **-0.0077** | 0.0037 | ±0.0075 | **-2.068** | **0.0386** | * |
| **BMI (kg/m2)** | **+0.0226** | 0.0070 | ±0.0140 | **+3.223** | **0.0013** | ** |
| Hypertension | +0.1214 | 0.1094 | ±0.2189 | +1.109 | 0.2673 |  |
| High cholesterol | -0.0427 | 0.0903 | ±0.1806 | -0.473 | 0.6362 |  |
| Kidney disease | -0.0693 | 0.1656 | ±0.3313 | -0.418 | 0.6756 |  |
| Circulatory disease | +0.3102 | 0.1843 | ±0.3687 | +1.683 | 0.0924 | . |
| Time 181-250, pooled (%) | -0.2616 | 0.1619 | ±0.3239 | -1.616 | 0.1062 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **384**, R² = **0.1464**, Adj R² = **0.1140**, F-statistic = **4.52** (p = **1.54e-07**), Residual SE = **0.868** on **369** df, AIC = **995.6**, BIC = **1054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8256** | 0.3018 | ±0.6037 | **+6.048** | **1.47e-09** | *** |
| Education: graduate level (vs college) | -0.0832 | 0.0963 | ±0.1926 | -0.865 | 0.3872 |  |
| Education: high school or below (vs college) | +0.3027 | 0.1962 | ±0.3924 | +1.543 | 0.1229 |  |
| Site: UCSD (vs UAB) | +0.0113 | 0.1165 | ±0.2329 | +0.097 | 0.9224 |  |
| **Site: UW (vs UAB)** | **-0.3582** | 0.1250 | ±0.2499 | **-2.866** | **0.0042** | ** |
| Season: spring (vs autumn) | -0.1256 | 0.1253 | ±0.2506 | -1.002 | 0.3162 |  |
| Season: summer (vs autumn) | +0.1965 | 0.1502 | ±0.3003 | +1.308 | 0.1908 |  |
| Season: winter (vs autumn) | -0.0335 | 0.1320 | ±0.2640 | -0.254 | 0.7995 |  |
| **Age (years)** | **-0.0079** | 0.0038 | ±0.0075 | **-2.109** | **0.0349** | * |
| **BMI (kg/m2)** | **+0.0230** | 0.0069 | ±0.0138 | **+3.327** | **8.78e-04** | *** |
| Hypertension | +0.1205 | 0.1096 | ±0.2193 | +1.099 | 0.2716 |  |
| High cholesterol | -0.0380 | 0.0903 | ±0.1807 | -0.420 | 0.6742 |  |
| Kidney disease | -0.0883 | 0.1656 | ±0.3311 | -0.533 | 0.5938 |  |
| Circulatory disease | +0.3118 | 0.1846 | ±0.3692 | +1.689 | 0.0912 | . |
| Avg. daily time 181-250 (%) | -0.2230 | 0.1577 | ±0.3154 | -1.414 | 0.1574 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **384**, R² = **0.1481**, Adj R² = **0.1158**, F-statistic = **4.58** (p = **1.13e-07**), Residual SE = **0.867** on **369** df, AIC = **994.8**, BIC = **1054.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8471** | 0.3034 | ±0.6068 | **+6.088** | **1.14e-09** | *** |
| Education: graduate level (vs college) | -0.0833 | 0.0962 | ±0.1925 | -0.866 | 0.3867 |  |
| Education: high school or below (vs college) | +0.3083 | 0.1966 | ±0.3932 | +1.568 | 0.1169 |  |
| Site: UCSD (vs UAB) | +0.0135 | 0.1159 | ±0.2319 | +0.116 | 0.9076 |  |
| **Site: UW (vs UAB)** | **-0.3578** | 0.1245 | ±0.2491 | **-2.873** | **0.0041** | ** |
| Season: spring (vs autumn) | -0.1286 | 0.1244 | ±0.2488 | -1.034 | 0.3013 |  |
| Season: summer (vs autumn) | +0.1996 | 0.1495 | ±0.2990 | +1.335 | 0.1818 |  |
| Season: winter (vs autumn) | -0.0321 | 0.1315 | ±0.2631 | -0.244 | 0.8071 |  |
| **Age (years)** | **-0.0077** | 0.0037 | ±0.0075 | **-2.071** | **0.0384** | * |
| **BMI (kg/m2)** | **+0.0225** | 0.0070 | ±0.0140 | **+3.220** | **0.0013** | ** |
| Hypertension | +0.1214 | 0.1094 | ±0.2189 | +1.109 | 0.2674 |  |
| High cholesterol | -0.0425 | 0.0903 | ±0.1805 | -0.471 | 0.6379 |  |
| Kidney disease | -0.0692 | 0.1657 | ±0.3314 | -0.418 | 0.6763 |  |
| Circulatory disease | +0.3102 | 0.1843 | ±0.3686 | +1.683 | 0.0924 | . |
| Time > 180 (%) | -0.2631 | 0.1618 | ±0.3236 | -1.626 | 0.1039 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **384**, R² = **0.1464**, Adj R² = **0.1141**, F-statistic = **4.52** (p = **1.52e-07**), Residual SE = **0.868** on **369** df, AIC = **995.5**, BIC = **1054.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8270** | 0.3020 | ±0.6040 | **+6.049** | **1.46e-09** | *** |
| Education: graduate level (vs college) | -0.0834 | 0.0963 | ±0.1926 | -0.866 | 0.3864 |  |
| Education: high school or below (vs college) | +0.3025 | 0.1962 | ±0.3923 | +1.542 | 0.1231 |  |
| Site: UCSD (vs UAB) | +0.0113 | 0.1165 | ±0.2329 | +0.097 | 0.9226 |  |
| **Site: UW (vs UAB)** | **-0.3580** | 0.1250 | ±0.2499 | **-2.865** | **0.0042** | ** |
| Season: spring (vs autumn) | -0.1255 | 0.1253 | ±0.2506 | -1.002 | 0.3164 |  |
| Season: summer (vs autumn) | +0.1966 | 0.1502 | ±0.3003 | +1.309 | 0.1905 |  |
| Season: winter (vs autumn) | -0.0333 | 0.1320 | ±0.2641 | -0.252 | 0.8010 |  |
| **Age (years)** | **-0.0080** | 0.0038 | ±0.0075 | **-2.112** | **0.0347** | * |
| **BMI (kg/m2)** | **+0.0230** | 0.0069 | ±0.0138 | **+3.325** | **8.83e-04** | *** |
| Hypertension | +0.1205 | 0.1096 | ±0.2193 | +1.099 | 0.2716 |  |
| High cholesterol | -0.0377 | 0.0903 | ±0.1806 | -0.418 | 0.6761 |  |
| Kidney disease | -0.0883 | 0.1656 | ±0.3313 | -0.533 | 0.5941 |  |
| Circulatory disease | +0.3118 | 0.1846 | ±0.3691 | +1.689 | 0.0911 | . |
| Avg. daily time > 180 (%) | -0.2246 | 0.1575 | ±0.3150 | -1.426 | 0.1538 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 384)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **384**, R² = **0.1509**, Adj R² = **0.1187**, F-statistic = **4.69** (p = **6.81e-08**), Residual SE = **0.865** on **369** df, AIC = **993.5**, BIC = **1052.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8194** | 0.2916 | ±0.5832 | **+6.240** | **4.39e-10** | *** |
| Education: graduate level (vs college) | -0.0974 | 0.0976 | ±0.1952 | -0.998 | 0.3183 |  |
| Education: high school or below (vs college) | +0.3072 | 0.1944 | ±0.3889 | +1.580 | 0.1142 |  |
| Site: UCSD (vs UAB) | +0.0035 | 0.1171 | ±0.2342 | +0.030 | 0.9759 |  |
| **Site: UW (vs UAB)** | **-0.3560** | 0.1247 | ±0.2494 | **-2.855** | **0.0043** | ** |
| Season: spring (vs autumn) | -0.1255 | 0.1240 | ±0.2481 | -1.012 | 0.3116 |  |
| Season: summer (vs autumn) | +0.1886 | 0.1464 | ±0.2928 | +1.288 | 0.1976 |  |
| Season: winter (vs autumn) | -0.0167 | 0.1319 | ±0.2637 | -0.127 | 0.8990 |  |
| **Age (years)** | **-0.0091** | 0.0038 | ±0.0076 | **-2.389** | **0.0169** | * |
| **BMI (kg/m2)** | **+0.0245** | 0.0069 | ±0.0138 | **+3.558** | **3.73e-04** | *** |
| Hypertension | +0.1268 | 0.1090 | ±0.2180 | +1.164 | 0.2446 |  |
| High cholesterol | -0.0302 | 0.0895 | ±0.1791 | -0.337 | 0.7360 |  |
| Kidney disease | -0.0949 | 0.1801 | ±0.3603 | -0.527 | 0.5983 |  |
| Circulatory disease | +0.3078 | 0.1855 | ±0.3709 | +1.660 | 0.0969 | . |
| Nocturnal time > 180 (%) | -0.2724 | 0.1523 | ±0.3047 | -1.788 | 0.0738 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 384; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **384**, R² = **0.3432**, Adj R² = **0.3201**, F-statistic = **14.87** (p = **5.60e-27**), Residual SE = **1.860** on **370** df, AIC = **1580.3**, BIC = **1635.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1018** | 0.8617 | ±1.7234 | **+27.970** | **3.77e-172** | *** |
| Education: graduate level (vs college) | +0.0429 | 0.2062 | ±0.4124 | +0.208 | 0.8351 |  |
| Education: high school or below (vs college) | +0.3652 | 0.3892 | ±0.7784 | +0.938 | 0.3480 |  |
| Site: UCSD (vs UAB) | -0.3276 | 0.2574 | ±0.5149 | -1.272 | 0.2032 |  |
| **Site: UW (vs UAB)** | **-1.0869** | 0.2500 | ±0.4999 | **-4.348** | **1.37e-05** | *** |
| Season: spring (vs autumn) | -0.2866 | 0.2929 | ±0.5858 | -0.979 | 0.3278 |  |
| **Season: summer (vs autumn)** | **+1.7933** | 0.3505 | ±0.7009 | **+5.117** | **3.11e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5176** | 0.2914 | ±0.5829 | **-5.207** | **1.92e-07** | *** |
| Age (years) | +0.0070 | 0.0090 | ±0.0180 | +0.784 | 0.4331 |  |
| BMI (kg/m2) | +0.0189 | 0.0165 | ±0.0330 | +1.143 | 0.2532 |  |
| Hypertension | -0.1757 | 0.2315 | ±0.4630 | -0.759 | 0.4480 |  |
| High cholesterol | -0.2933 | 0.2068 | ±0.4136 | -1.418 | 0.1561 |  |
| **Kidney disease** | **+0.7553** | 0.3599 | ±0.7199 | **+2.098** | **0.0359** | * |
| Circulatory disease | +0.6409 | 0.3905 | ±0.7811 | +1.641 | 0.1008 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **384**, R² = **0.3436**, Adj R² = **0.3187**, F-statistic = **13.80** (p = **1.99e-26**), Residual SE = **1.862** on **369** df, AIC = **1582.0**, BIC = **1641.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.2430** | 2.0743 | ±4.1486 | **+11.205** | **3.85e-29** | *** |
| Education: graduate level (vs college) | +0.0437 | 0.2064 | ±0.4129 | +0.212 | 0.8322 |  |
| Education: high school or below (vs college) | +0.3596 | 0.3936 | ±0.7872 | +0.914 | 0.3610 |  |
| Site: UCSD (vs UAB) | -0.3270 | 0.2584 | ±0.5168 | -1.265 | 0.2057 |  |
| **Site: UW (vs UAB)** | **-1.0831** | 0.2502 | ±0.5005 | **-4.328** | **1.50e-05** | *** |
| Season: spring (vs autumn) | -0.2652 | 0.2967 | ±0.5934 | -0.894 | 0.3715 |  |
| **Season: summer (vs autumn)** | **+1.7833** | 0.3501 | ±0.7002 | **+5.094** | **3.52e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5111** | 0.2922 | ±0.5843 | **-5.172** | **2.31e-07** | *** |
| Age (years) | +0.0065 | 0.0092 | ±0.0184 | +0.708 | 0.4786 |  |
| BMI (kg/m2) | +0.0183 | 0.0164 | ±0.0328 | +1.116 | 0.2646 |  |
| Hypertension | -0.1845 | 0.2340 | ±0.4680 | -0.788 | 0.4304 |  |
| High cholesterol | -0.3141 | 0.2185 | ±0.4371 | -1.437 | 0.1507 |  |
| **Kidney disease** | **+0.7692** | 0.3611 | ±0.7222 | **+2.130** | **0.0332** | * |
| Circulatory disease | +0.6551 | 0.3933 | ±0.7867 | +1.665 | 0.0958 | . |
| HbA1c (%) | +0.1643 | 0.3775 | ±0.7551 | +0.435 | 0.6635 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **384**, R² = **0.3432**, Adj R² = **0.3183**, F-statistic = **13.77** (p = **2.20e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.2**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8960** | 1.6177 | ±3.2355 | **+14.771** | **2.24e-49** | *** |
| Education: graduate level (vs college) | +0.0422 | 0.2062 | ±0.4123 | +0.205 | 0.8377 |  |
| Education: high school or below (vs college) | +0.3663 | 0.3897 | ±0.7795 | +0.940 | 0.3472 |  |
| Site: UCSD (vs UAB) | -0.3294 | 0.2584 | ±0.5168 | -1.275 | 0.2023 |  |
| **Site: UW (vs UAB)** | **-1.0891** | 0.2512 | ±0.5024 | **-4.336** | **1.45e-05** | *** |
| Season: spring (vs autumn) | -0.2849 | 0.2925 | ±0.5850 | -0.974 | 0.3300 |  |
| **Season: summer (vs autumn)** | **+1.7931** | 0.3513 | ±0.7026 | **+5.104** | **3.33e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5168** | 0.2922 | ±0.5843 | **-5.192** | **2.08e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0180 | +0.786 | 0.4316 |  |
| BMI (kg/m2) | +0.0187 | 0.0166 | ±0.0332 | +1.129 | 0.2590 |  |
| Hypertension | -0.1778 | 0.2322 | ±0.4645 | -0.766 | 0.4439 |  |
| High cholesterol | -0.2921 | 0.2068 | ±0.4136 | -1.412 | 0.1578 |  |
| **Kidney disease** | **+0.7532** | 0.3600 | ±0.7200 | **+2.092** | **0.0364** | * |
| Circulatory disease | +0.6417 | 0.3911 | ±0.7823 | +1.641 | 0.1009 |  |
| Mean glucose (mg/dL) | +0.0018 | 0.0122 | ±0.0243 | +0.150 | 0.8809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **384**, R² = **0.3432**, Adj R² = **0.3183**, F-statistic = **13.77** (p = **2.20e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.2**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6439** | 3.1706 | ±6.3411 | **+7.457** | **8.83e-14** | *** |
| Education: graduate level (vs college) | +0.0422 | 0.2062 | ±0.4123 | +0.205 | 0.8377 |  |
| Education: high school or below (vs college) | +0.3663 | 0.3897 | ±0.7795 | +0.940 | 0.3472 |  |
| Site: UCSD (vs UAB) | -0.3294 | 0.2584 | ±0.5168 | -1.275 | 0.2023 |  |
| **Site: UW (vs UAB)** | **-1.0891** | 0.2512 | ±0.5024 | **-4.336** | **1.45e-05** | *** |
| Season: spring (vs autumn) | -0.2849 | 0.2925 | ±0.5850 | -0.974 | 0.3300 |  |
| **Season: summer (vs autumn)** | **+1.7931** | 0.3513 | ±0.7026 | **+5.104** | **3.33e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5168** | 0.2922 | ±0.5843 | **-5.192** | **2.08e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0180 | +0.786 | 0.4316 |  |
| BMI (kg/m2) | +0.0187 | 0.0166 | ±0.0332 | +1.129 | 0.2590 |  |
| Hypertension | -0.1778 | 0.2322 | ±0.4645 | -0.766 | 0.4439 |  |
| High cholesterol | -0.2921 | 0.2068 | ±0.4136 | -1.412 | 0.1578 |  |
| **Kidney disease** | **+0.7532** | 0.3600 | ±0.7200 | **+2.092** | **0.0364** | * |
| Circulatory disease | +0.6417 | 0.3911 | ±0.7823 | +1.641 | 0.1009 |  |
| GMI (%) | +0.0762 | 0.5083 | ±1.0166 | +0.150 | 0.8809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **384**, R² = **0.3442**, Adj R² = **0.3193**, F-statistic = **13.83** (p = **1.70e-26**), Residual SE = **1.862** on **369** df, AIC = **1581.7**, BIC = **1640.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9906** | 1.4099 | ±2.8197 | **+17.726** | **2.66e-70** | *** |
| Education: graduate level (vs college) | +0.0367 | 0.2075 | ±0.4149 | +0.177 | 0.8595 |  |
| Education: high school or below (vs college) | +0.3528 | 0.3937 | ±0.7875 | +0.896 | 0.3703 |  |
| Site: UCSD (vs UAB) | -0.3080 | 0.2612 | ±0.5223 | -1.179 | 0.2382 |  |
| **Site: UW (vs UAB)** | **-1.0703** | 0.2523 | ±0.5045 | **-4.242** | **2.21e-05** | *** |
| Season: spring (vs autumn) | -0.2880 | 0.2934 | ±0.5868 | -0.982 | 0.3263 |  |
| **Season: summer (vs autumn)** | **+1.7988** | 0.3513 | ±0.7026 | **+5.120** | **3.05e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5174** | 0.2917 | ±0.5833 | **-5.202** | **1.97e-07** | *** |
| Age (years) | +0.0061 | 0.0091 | ±0.0183 | +0.666 | 0.5053 |  |
| BMI (kg/m2) | +0.0207 | 0.0173 | ±0.0347 | +1.191 | 0.2336 |  |
| Hypertension | -0.1690 | 0.2321 | ±0.4642 | -0.728 | 0.4665 |  |
| High cholesterol | -0.2945 | 0.2067 | ±0.4134 | -1.424 | 0.1543 |  |
| **Kidney disease** | **+0.7500** | 0.3584 | ±0.7167 | **+2.093** | **0.0364** | * |
| Circulatory disease | +0.6342 | 0.3898 | ±0.7797 | +1.627 | 0.1038 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0078 | 0.0098 | ±0.0195 | -0.795 | 0.4264 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **384**, R² = **0.3515**, Adj R² = **0.3269**, F-statistic = **14.29** (p = **2.45e-27**), Residual SE = **1.851** on **369** df, AIC = **1577.4**, BIC = **1636.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.6380** | 1.1050 | ±2.2100 | **+23.202** | **4.35e-119** | *** |
| Education: graduate level (vs college) | +0.0181 | 0.2063 | ±0.4125 | +0.088 | 0.9301 |  |
| Education: high school or below (vs college) | +0.3714 | 0.3855 | ±0.7711 | +0.963 | 0.3354 |  |
| Site: UCSD (vs UAB) | -0.3776 | 0.2543 | ±0.5086 | -1.485 | 0.1375 |  |
| **Site: UW (vs UAB)** | **-1.1176** | 0.2504 | ±0.5008 | **-4.464** | **8.06e-06** | *** |
| Season: spring (vs autumn) | -0.2422 | 0.2922 | ±0.5843 | -0.829 | 0.4071 |  |
| **Season: summer (vs autumn)** | **+1.8227** | 0.3467 | ±0.6935 | **+5.257** | **1.47e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4704** | 0.2907 | ±0.5814 | **-5.058** | **4.23e-07** | *** |
| Age (years) | +0.0072 | 0.0089 | ±0.0178 | +0.810 | 0.4179 |  |
| BMI (kg/m2) | +0.0202 | 0.0167 | ±0.0335 | +1.208 | 0.2271 |  |
| Hypertension | -0.1741 | 0.2313 | ±0.4626 | -0.753 | 0.4516 |  |
| High cholesterol | -0.3152 | 0.2062 | ±0.4124 | -1.529 | 0.1264 |  |
| **Kidney disease** | **+0.7940** | 0.3778 | ±0.7555 | **+2.102** | **0.0356** | * |
| Circulatory disease | +0.6594 | 0.3969 | ±0.7938 | +1.661 | 0.0966 | . |
| **Glucose SD, pooled (mg/dL)** | **-0.0940** | 0.0430 | ±0.0860 | **-2.186** | **0.0288** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **384**, R² = **0.3554**, Adj R² = **0.3309**, F-statistic = **14.53** (p = **8.64e-28**), Residual SE = **1.846** on **369** df, AIC = **1575.1**, BIC = **1634.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.7686** | 1.0834 | ±2.1668 | **+23.785** | **4.77e-125** | *** |
| Education: graduate level (vs college) | +0.0089 | 0.2058 | ±0.4115 | +0.043 | 0.9653 |  |
| Education: high school or below (vs college) | +0.3557 | 0.3933 | ±0.7865 | +0.905 | 0.3657 |  |
| Site: UCSD (vs UAB) | -0.3916 | 0.2531 | ±0.5062 | -1.547 | 0.1218 |  |
| **Site: UW (vs UAB)** | **-1.1257** | 0.2484 | ±0.4969 | **-4.531** | **5.87e-06** | *** |
| Season: spring (vs autumn) | -0.2412 | 0.2914 | ±0.5827 | -0.828 | 0.4078 |  |
| **Season: summer (vs autumn)** | **+1.8177** | 0.3462 | ±0.6925 | **+5.250** | **1.52e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4852** | 0.2862 | ±0.5724 | **-5.189** | **2.11e-07** | *** |
| Age (years) | +0.0072 | 0.0089 | ±0.0177 | +0.814 | 0.4155 |  |
| BMI (kg/m2) | +0.0219 | 0.0172 | ±0.0344 | +1.275 | 0.2024 |  |
| Hypertension | -0.1849 | 0.2312 | ±0.4624 | -0.800 | 0.4239 |  |
| High cholesterol | -0.3137 | 0.2059 | ±0.4117 | -1.524 | 0.1275 |  |
| **Kidney disease** | **+0.8032** | 0.3818 | ±0.7635 | **+2.104** | **0.0354** | * |
| Circulatory disease | +0.6464 | 0.3950 | ±0.7900 | +1.637 | 0.1017 |  |
| **Avg. daily SD (mg/dL)** | **-0.1127** | 0.0436 | ±0.0873 | **-2.583** | **0.0098** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **384**, R² = **0.3514**, Adj R² = **0.3268**, F-statistic = **14.28** (p = **2.50e-27**), Residual SE = **1.851** on **369** df, AIC = **1577.4**, BIC = **1636.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.5749** | 1.0817 | ±2.1634 | **+23.644** | **1.38e-123** | *** |
| Education: graduate level (vs college) | +0.0142 | 0.2061 | ±0.4122 | +0.069 | 0.9450 |  |
| Education: high school or below (vs college) | +0.3790 | 0.3817 | ±0.7634 | +0.993 | 0.3207 |  |
| Site: UCSD (vs UAB) | -0.3879 | 0.2549 | ±0.5098 | -1.522 | 0.1280 |  |
| **Site: UW (vs UAB)** | **-1.1322** | 0.2504 | ±0.5008 | **-4.522** | **6.13e-06** | *** |
| Season: spring (vs autumn) | -0.2315 | 0.2916 | ±0.5832 | -0.794 | 0.4272 |  |
| **Season: summer (vs autumn)** | **+1.8241** | 0.3470 | ±0.6940 | **+5.256** | **1.47e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4664** | 0.2913 | ±0.5825 | **-5.035** | **4.79e-07** | *** |
| Age (years) | +0.0075 | 0.0089 | ±0.0178 | +0.842 | 0.3996 |  |
| BMI (kg/m2) | +0.0192 | 0.0166 | ±0.0333 | +1.152 | 0.2493 |  |
| Hypertension | -0.1894 | 0.2317 | ±0.4634 | -0.817 | 0.4138 |  |
| High cholesterol | -0.3069 | 0.2069 | ±0.4139 | -1.483 | 0.1381 |  |
| **Kidney disease** | **+0.7751** | 0.3763 | ±0.7527 | **+2.059** | **0.0395** | * |
| Circulatory disease | +0.6655 | 0.3978 | ±0.7957 | +1.673 | 0.0944 | . |
| **CV (%)** | **-0.1015** | 0.0459 | ±0.0917 | **-2.212** | **0.0270** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **384**, R² = **0.3501**, Adj R² = **0.3255**, F-statistic = **14.20** (p = **3.52e-27**), Residual SE = **1.853** on **369** df, AIC = **1578.2**, BIC = **1637.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.7636** | 1.0808 | ±2.1616 | **+21.061** | **1.79e-98** | *** |
| Education: graduate level (vs college) | +0.0131 | 0.2059 | ±0.4118 | +0.064 | 0.9493 |  |
| Education: high school or below (vs college) | +0.3783 | 0.3829 | ±0.7657 | +0.988 | 0.3231 |  |
| Site: UCSD (vs UAB) | -0.3735 | 0.2547 | ±0.5094 | -1.466 | 0.1426 |  |
| **Site: UW (vs UAB)** | **-1.1197** | 0.2497 | ±0.4995 | **-4.483** | **7.36e-06** | *** |
| Season: spring (vs autumn) | -0.2325 | 0.2922 | ±0.5844 | -0.796 | 0.4262 |  |
| **Season: summer (vs autumn)** | **+1.8185** | 0.3477 | ±0.6955 | **+5.229** | **1.70e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4710** | 0.2916 | ±0.5831 | **-5.045** | **4.53e-07** | *** |
| Age (years) | +0.0073 | 0.0089 | ±0.0178 | +0.817 | 0.4139 |  |
| BMI (kg/m2) | +0.0191 | 0.0165 | ±0.0330 | +1.155 | 0.2482 |  |
| Hypertension | -0.1810 | 0.2314 | ±0.4627 | -0.782 | 0.4341 |  |
| High cholesterol | -0.3067 | 0.2069 | ±0.4139 | -1.482 | 0.1383 |  |
| **Kidney disease** | **+0.7636** | 0.3734 | ±0.7469 | **+2.045** | **0.0409** | * |
| Circulatory disease | +0.6615 | 0.3974 | ±0.7948 | +1.665 | 0.0960 | . |
| **Mean / SD ratio** | **+0.1913** | 0.0922 | ±0.1844 | **+2.075** | **0.0380** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **384**, R² = **0.3534**, Adj R² = **0.3289**, F-statistic = **14.41** (p = **1.47e-27**), Residual SE = **1.848** on **369** df, AIC = **1576.2**, BIC = **1635.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.5856** | 1.0579 | ±2.1158 | **+21.350** | **3.92e-101** | *** |
| Education: graduate level (vs college) | +0.0022 | 0.2059 | ±0.4117 | +0.011 | 0.9914 |  |
| Education: high school or below (vs college) | +0.3665 | 0.3883 | ±0.7766 | +0.944 | 0.3452 |  |
| Site: UCSD (vs UAB) | -0.3873 | 0.2535 | ±0.5070 | -1.528 | 0.1266 |  |
| **Site: UW (vs UAB)** | **-1.1242** | 0.2475 | ±0.4950 | **-4.542** | **5.57e-06** | *** |
| Season: spring (vs autumn) | -0.2223 | 0.2924 | ±0.5847 | -0.760 | 0.4471 |  |
| **Season: summer (vs autumn)** | **+1.8189** | 0.3473 | ±0.6946 | **+5.237** | **1.63e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4772** | 0.2880 | ±0.5760 | **-5.129** | **2.91e-07** | *** |
| Age (years) | +0.0074 | 0.0088 | ±0.0177 | +0.833 | 0.4051 |  |
| BMI (kg/m2) | +0.0211 | 0.0169 | ±0.0337 | +1.251 | 0.2110 |  |
| Hypertension | -0.1959 | 0.2307 | ±0.4613 | -0.849 | 0.3957 |  |
| High cholesterol | -0.3023 | 0.2067 | ±0.4135 | -1.462 | 0.1436 |  |
| **Kidney disease** | **+0.7749** | 0.3742 | ±0.7484 | **+2.071** | **0.0384** | * |
| Circulatory disease | +0.6523 | 0.3930 | ±0.7859 | +1.660 | 0.0969 | . |
| **Avg. daily mean/SD** | **+0.1861** | 0.0747 | ±0.1494 | **+2.492** | **0.0127** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **384**, R² = **0.3467**, Adj R² = **0.3219**, F-statistic = **13.99** (p = **8.73e-27**), Residual SE = **1.858** on **369** df, AIC = **1580.2**, BIC = **1639.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0548** | 1.1100 | ±2.2201 | **+22.571** | **8.33e-113** | *** |
| Education: graduate level (vs college) | +0.0500 | 0.2059 | ±0.4118 | +0.243 | 0.8082 |  |
| Education: high school or below (vs college) | +0.4047 | 0.3941 | ±0.7882 | +1.027 | 0.3044 |  |
| Site: UCSD (vs UAB) | -0.3548 | 0.2583 | ±0.5166 | -1.374 | 0.1695 |  |
| **Site: UW (vs UAB)** | **-1.1307** | 0.2532 | ±0.5063 | **-4.466** | **7.96e-06** | *** |
| Season: spring (vs autumn) | -0.2679 | 0.2927 | ±0.5855 | -0.915 | 0.3601 |  |
| **Season: summer (vs autumn)** | **+1.7912** | 0.3519 | ±0.7039 | **+5.090** | **3.59e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4979** | 0.2920 | ±0.5841 | **-5.129** | **2.91e-07** | *** |
| Age (years) | +0.0054 | 0.0090 | ±0.0181 | +0.597 | 0.5506 |  |
| BMI (kg/m2) | +0.0175 | 0.0168 | ±0.0336 | +1.039 | 0.2990 |  |
| Hypertension | -0.1867 | 0.2313 | ±0.4625 | -0.807 | 0.4194 |  |
| High cholesterol | -0.2766 | 0.2082 | ±0.4165 | -1.328 | 0.1840 |  |
| **Kidney disease** | **+0.7858** | 0.3659 | ±0.7318 | **+2.148** | **0.0318** | * |
| Circulatory disease | +0.6407 | 0.3912 | ±0.7825 | +1.638 | 0.1015 |  |
| MAG (mg/dL/h) | -0.0237 | 0.0170 | ±0.0340 | -1.394 | 0.1633 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **384**, R² = **0.3571**, Adj R² = **0.3327**, F-statistic = **14.64** (p = **5.36e-28**), Residual SE = **1.843** on **369** df, AIC = **1574.0**, BIC = **1633.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+26.2030** | 1.1181 | ±2.2362 | **+23.435** | **1.88e-121** | *** |
| Education: graduate level (vs college) | +0.0339 | 0.2038 | ±0.4076 | +0.166 | 0.8681 |  |
| Education: high school or below (vs college) | +0.3656 | 0.4001 | ±0.8003 | +0.914 | 0.3609 |  |
| Site: UCSD (vs UAB) | -0.3924 | 0.2531 | ±0.5061 | -1.551 | 0.1210 |  |
| **Site: UW (vs UAB)** | **-1.1333** | 0.2485 | ±0.4970 | **-4.561** | **5.10e-06** | *** |
| Season: spring (vs autumn) | -0.2340 | 0.2905 | ±0.5809 | -0.805 | 0.4206 |  |
| **Season: summer (vs autumn)** | **+1.8135** | 0.3469 | ±0.6938 | **+5.227** | **1.72e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4677** | 0.2862 | ±0.5724 | **-5.128** | **2.92e-07** | *** |
| Age (years) | +0.0066 | 0.0088 | ±0.0175 | +0.750 | 0.4531 |  |
| BMI (kg/m2) | +0.0159 | 0.0158 | ±0.0316 | +1.005 | 0.3149 |  |
| Hypertension | -0.2055 | 0.2314 | ±0.4628 | -0.888 | 0.3746 |  |
| High cholesterol | -0.2878 | 0.2056 | ±0.4112 | -1.400 | 0.1616 |  |
| **Kidney disease** | **+0.7850** | 0.3776 | ±0.7551 | **+2.079** | **0.0376** | * |
| Circulatory disease | +0.6590 | 0.3925 | ±0.7851 | +1.679 | 0.0932 | . |
| **Avg. daily range (mg/dL)** | **-0.0248** | 0.0088 | ±0.0177 | **-2.800** | **0.0051** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **384**, R² = **0.3474**, Adj R² = **0.3227**, F-statistic = **14.03** (p = **7.24e-27**), Residual SE = **1.857** on **369** df, AIC = **1579.8**, BIC = **1639.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.7368** | 0.8851 | ±1.7703 | **+26.817** | **2.05e-158** | *** |
| Education: graduate level (vs college) | +0.0295 | 0.2055 | ±0.4110 | +0.144 | 0.8857 |  |
| Education: high school or below (vs college) | +0.3310 | 0.3947 | ±0.7894 | +0.839 | 0.4017 |  |
| Site: UCSD (vs UAB) | -0.3179 | 0.2562 | ±0.5124 | -1.241 | 0.2147 |  |
| **Site: UW (vs UAB)** | **-1.1024** | 0.2495 | ±0.4990 | **-4.419** | **9.94e-06** | *** |
| Season: spring (vs autumn) | -0.3153 | 0.2918 | ±0.5836 | -1.081 | 0.2799 |  |
| **Season: summer (vs autumn)** | **+1.7619** | 0.3517 | ±0.7035 | **+5.009** | **5.46e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5618** | 0.2920 | ±0.5840 | **-5.348** | **8.88e-08** | *** |
| Age (years) | +0.0068 | 0.0089 | ±0.0179 | +0.760 | 0.4471 |  |
| BMI (kg/m2) | +0.0188 | 0.0164 | ±0.0327 | +1.147 | 0.2515 |  |
| Hypertension | -0.1963 | 0.2321 | ±0.4643 | -0.846 | 0.3977 |  |
| High cholesterol | -0.2997 | 0.2065 | ±0.4130 | -1.451 | 0.1467 |  |
| **Kidney disease** | **+0.7920** | 0.3668 | ±0.7336 | **+2.159** | **0.0308** | * |
| Circulatory disease | +0.6134 | 0.3869 | ±0.7738 | +1.585 | 0.1129 |  |
| SD of daily means (mg/dL) | +0.0851 | 0.0516 | ±0.1032 | +1.649 | 0.0991 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **384**, R² = **0.3460**, Adj R² = **0.3212**, F-statistic = **13.94** (p = **1.06e-26**), Residual SE = **1.859** on **369** df, AIC = **1580.6**, BIC = **1639.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -16.4064 | 32.9168 | ±65.8336 | -0.498 | 0.6182 |  |
| Education: graduate level (vs college) | +0.0424 | 0.2062 | ±0.4124 | +0.206 | 0.8370 |  |
| Education: high school or below (vs college) | +0.3687 | 0.3907 | ±0.7814 | +0.944 | 0.3453 |  |
| Site: UCSD (vs UAB) | -0.3494 | 0.2568 | ±0.5136 | -1.360 | 0.1737 |  |
| **Site: UW (vs UAB)** | **-1.1023** | 0.2518 | ±0.5035 | **-4.378** | **1.20e-05** | *** |
| Season: spring (vs autumn) | -0.2703 | 0.2954 | ±0.5908 | -0.915 | 0.3602 |  |
| **Season: summer (vs autumn)** | **+1.8172** | 0.3548 | ±0.7096 | **+5.122** | **3.03e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4944** | 0.2934 | ±0.5868 | **-5.093** | **3.52e-07** | *** |
| Age (years) | +0.0066 | 0.0090 | ±0.0179 | +0.738 | 0.4608 |  |
| BMI (kg/m2) | +0.0178 | 0.0160 | ±0.0319 | +1.115 | 0.2649 |  |
| Hypertension | -0.1768 | 0.2329 | ±0.4659 | -0.759 | 0.4478 |  |
| High cholesterol | -0.2815 | 0.2086 | ±0.4172 | -1.350 | 0.1771 |  |
| **Kidney disease** | **+0.7754** | 0.3711 | ±0.7422 | **+2.089** | **0.0367** | * |
| Circulatory disease | +0.6500 | 0.3958 | ±0.7916 | +1.642 | 0.1005 |  |
| Time in range 70-180, pooled (%) | +0.4074 | 0.3305 | ±0.6609 | +1.233 | 0.2177 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **384**, R² = **0.3445**, Adj R² = **0.3196**, F-statistic = **13.85** (p = **1.57e-26**), Residual SE = **1.861** on **369** df, AIC = **1581.5**, BIC = **1640.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.6805 | 32.5214 | ±65.0428 | -0.082 | 0.9343 |  |
| Education: graduate level (vs college) | +0.0425 | 0.2066 | ±0.4132 | +0.206 | 0.8369 |  |
| Education: high school or below (vs college) | +0.3631 | 0.3911 | ±0.7822 | +0.928 | 0.3532 |  |
| Site: UCSD (vs UAB) | -0.3380 | 0.2572 | ±0.5144 | -1.314 | 0.1888 |  |
| **Site: UW (vs UAB)** | **-1.0896** | 0.2509 | ±0.5018 | **-4.343** | **1.41e-05** | *** |
| Season: spring (vs autumn) | -0.2785 | 0.2950 | ±0.5900 | -0.944 | 0.3452 |  |
| **Season: summer (vs autumn)** | **+1.7986** | 0.3531 | ±0.7062 | **+5.094** | **3.51e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5053** | 0.2937 | ±0.5873 | **-5.126** | **2.96e-07** | *** |
| Age (years) | +0.0065 | 0.0090 | ±0.0181 | +0.715 | 0.4744 |  |
| BMI (kg/m2) | +0.0186 | 0.0165 | ±0.0330 | +1.127 | 0.2596 |  |
| Hypertension | -0.1834 | 0.2337 | ±0.4674 | -0.785 | 0.4326 |  |
| High cholesterol | -0.2831 | 0.2097 | ±0.4194 | -1.350 | 0.1770 |  |
| **Kidney disease** | **+0.7583** | 0.3703 | ±0.7405 | **+2.048** | **0.0406** | * |
| Circulatory disease | +0.6528 | 0.3970 | ±0.7939 | +1.644 | 0.1001 |  |
| Avg. daily time in range 70-180 (%) | +0.2693 | 0.3265 | ±0.6530 | +0.825 | 0.4095 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.3435**, Adj R² = **0.3186**, F-statistic = **13.79** (p = **2.04e-26**), Residual SE = **1.862** on **369** df, AIC = **1582.1**, BIC = **1641.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1212** | 0.8658 | ±1.7316 | **+27.861** | **8.01e-171** | *** |
| Education: graduate level (vs college) | +0.0412 | 0.2061 | ±0.4123 | +0.200 | 0.8414 |  |
| Education: high school or below (vs college) | +0.3631 | 0.3885 | ±0.7770 | +0.934 | 0.3500 |  |
| Site: UCSD (vs UAB) | -0.3470 | 0.2651 | ±0.5302 | -1.309 | 0.1907 |  |
| **Site: UW (vs UAB)** | **-1.0994** | 0.2571 | ±0.5143 | **-4.276** | **1.91e-05** | *** |
| Season: spring (vs autumn) | -0.2721 | 0.2951 | ±0.5903 | -0.922 | 0.3566 |  |
| **Season: summer (vs autumn)** | **+1.8005** | 0.3498 | ±0.6997 | **+5.147** | **2.65e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5076** | 0.2930 | ±0.5861 | **-5.145** | **2.68e-07** | *** |
| Age (years) | +0.0070 | 0.0090 | ±0.0180 | +0.784 | 0.4332 |  |
| BMI (kg/m2) | +0.0189 | 0.0166 | ±0.0332 | +1.136 | 0.2559 |  |
| Hypertension | -0.1684 | 0.2294 | ±0.4589 | -0.734 | 0.4631 |  |
| High cholesterol | -0.2935 | 0.2074 | ±0.4149 | -1.415 | 0.1571 |  |
| **Kidney disease** | **+0.7435** | 0.3614 | ±0.7228 | **+2.057** | **0.0397** | * |
| Circulatory disease | +0.6474 | 0.3931 | ±0.7862 | +1.647 | 0.0996 | . |
| Any reading < 54 during wear (0/1) | -0.1117 | 0.2839 | ±0.5678 | -0.393 | 0.6941 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.3432**, Adj R² = **0.3183**, F-statistic = **13.77** (p = **2.20e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.2**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0965** | 0.8626 | ±1.7253 | **+27.933** | **1.05e-171** | *** |
| Education: graduate level (vs college) | +0.0431 | 0.2069 | ±0.4137 | +0.208 | 0.8349 |  |
| Education: high school or below (vs college) | +0.3676 | 0.3890 | ±0.7780 | +0.945 | 0.3446 |  |
| Site: UCSD (vs UAB) | -0.3235 | 0.2601 | ±0.5201 | -1.244 | 0.2135 |  |
| **Site: UW (vs UAB)** | **-1.0848** | 0.2523 | ±0.5046 | **-4.299** | **1.71e-05** | *** |
| Season: spring (vs autumn) | -0.2861 | 0.2941 | ±0.5881 | -0.973 | 0.3307 |  |
| **Season: summer (vs autumn)** | **+1.7930** | 0.3522 | ±0.7045 | **+5.090** | **3.58e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5174** | 0.2925 | ±0.5849 | **-5.188** | **2.12e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0180 | +0.787 | 0.4312 |  |
| BMI (kg/m2) | +0.0188 | 0.0166 | ±0.0332 | +1.129 | 0.2587 |  |
| Hypertension | -0.1778 | 0.2305 | ±0.4611 | -0.771 | 0.4406 |  |
| High cholesterol | -0.2930 | 0.2074 | ±0.4147 | -1.413 | 0.1576 |  |
| **Kidney disease** | **+0.7576** | 0.3605 | ±0.7209 | **+2.102** | **0.0356** | * |
| Circulatory disease | +0.6385 | 0.3921 | ±0.7842 | +1.628 | 0.1035 |  |
| Time < 54 (%) | +0.2422 | 2.1258 | ±4.2515 | +0.114 | 0.9093 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.3432**, Adj R² = **0.3183**, F-statistic = **13.77** (p = **2.19e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.2**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0965** | 0.8627 | ±1.7254 | **+27.931** | **1.12e-171** | *** |
| Education: graduate level (vs college) | +0.0421 | 0.2074 | ±0.4148 | +0.203 | 0.8393 |  |
| Education: high school or below (vs college) | +0.3664 | 0.3891 | ±0.7781 | +0.942 | 0.3463 |  |
| Site: UCSD (vs UAB) | -0.3247 | 0.2589 | ±0.5179 | -1.254 | 0.2098 |  |
| **Site: UW (vs UAB)** | **-1.0858** | 0.2515 | ±0.5031 | **-4.316** | **1.59e-05** | *** |
| Season: spring (vs autumn) | -0.2856 | 0.2946 | ±0.5892 | -0.969 | 0.3323 |  |
| **Season: summer (vs autumn)** | **+1.7965** | 0.3516 | ±0.7033 | **+5.109** | **3.23e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5169** | 0.2929 | ±0.5858 | **-5.179** | **2.23e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0180 | +0.787 | 0.4315 |  |
| BMI (kg/m2) | +0.0188 | 0.0166 | ±0.0331 | +1.136 | 0.2562 |  |
| Hypertension | -0.1772 | 0.2322 | ±0.4645 | -0.763 | 0.4454 |  |
| High cholesterol | -0.2928 | 0.2071 | ±0.4142 | -1.414 | 0.1574 |  |
| **Kidney disease** | **+0.7563** | 0.3602 | ±0.7204 | **+2.100** | **0.0358** | * |
| Circulatory disease | +0.6367 | 0.3931 | ±0.7862 | +1.620 | 0.1053 |  |
| Avg. daily time < 54 (%) | +0.3578 | 2.7475 | ±5.4949 | +0.130 | 0.8964 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.3473**, Adj R² = **0.3225**, F-statistic = **14.02** (p = **7.54e-27**), Residual SE = **1.857** on **369** df, AIC = **1579.9**, BIC = **1639.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.2269** | 0.8680 | ±1.7360 | **+27.911** | **1.98e-171** | *** |
| Education: graduate level (vs college) | +0.0327 | 0.2060 | ±0.4121 | +0.159 | 0.8739 |  |
| Education: high school or below (vs college) | +0.3876 | 0.3864 | ±0.7728 | +1.003 | 0.3158 |  |
| Site: UCSD (vs UAB) | -0.3570 | 0.2588 | ±0.5176 | -1.379 | 0.1678 |  |
| **Site: UW (vs UAB)** | **-1.1215** | 0.2503 | ±0.5007 | **-4.480** | **7.47e-06** | *** |
| Season: spring (vs autumn) | -0.2707 | 0.2953 | ±0.5905 | -0.917 | 0.3592 |  |
| **Season: summer (vs autumn)** | **+1.7988** | 0.3532 | ±0.7064 | **+5.093** | **3.52e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4925** | 0.2942 | ±0.5884 | **-5.073** | **3.91e-07** | *** |
| Age (years) | +0.0072 | 0.0090 | ±0.0179 | +0.803 | 0.4222 |  |
| BMI (kg/m2) | +0.0185 | 0.0168 | ±0.0336 | +1.101 | 0.2708 |  |
| Hypertension | -0.2056 | 0.2335 | ±0.4671 | -0.880 | 0.3788 |  |
| High cholesterol | -0.2618 | 0.2065 | ±0.4130 | -1.268 | 0.2049 |  |
| Kidney disease | +0.7026 | 0.3643 | ±0.7286 | +1.928 | 0.0538 | . |
| Circulatory disease | +0.6442 | 0.3921 | ±0.7841 | +1.643 | 0.1004 |  |
| Time 54-69, pooled (%) | -0.8235 | 0.5593 | ±1.1186 | -1.472 | 0.1409 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **384**, R² = **0.3457**, Adj R² = **0.3208**, F-statistic = **13.92** (p = **1.15e-26**), Residual SE = **1.859** on **369** df, AIC = **1580.8**, BIC = **1640.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1953** | 0.8637 | ±1.7275 | **+28.012** | **1.16e-172** | *** |
| Education: graduate level (vs college) | +0.0316 | 0.2066 | ±0.4132 | +0.153 | 0.8784 |  |
| Education: high school or below (vs college) | +0.3857 | 0.3860 | ±0.7719 | +0.999 | 0.3176 |  |
| Site: UCSD (vs UAB) | -0.3407 | 0.2577 | ±0.5153 | -1.322 | 0.1861 |  |
| **Site: UW (vs UAB)** | **-1.1003** | 0.2492 | ±0.4985 | **-4.414** | **1.01e-05** | *** |
| Season: spring (vs autumn) | -0.2913 | 0.2936 | ±0.5871 | -0.992 | 0.3210 |  |
| **Season: summer (vs autumn)** | **+1.7823** | 0.3520 | ±0.7039 | **+5.064** | **4.11e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5042** | 0.2941 | ±0.5882 | **-5.115** | **3.14e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0179 | +0.797 | 0.4255 |  |
| BMI (kg/m2) | +0.0186 | 0.0167 | ±0.0333 | +1.119 | 0.2629 |  |
| Hypertension | -0.2134 | 0.2339 | ±0.4678 | -0.912 | 0.3616 |  |
| High cholesterol | -0.2754 | 0.2079 | ±0.4159 | -1.324 | 0.1854 |  |
| **Kidney disease** | **+0.7263** | 0.3644 | ±0.7287 | **+1.993** | **0.0462** | * |
| Circulatory disease | +0.6509 | 0.3922 | ±0.7844 | +1.660 | 0.0970 | . |
| Avg. daily time 54-69 (%) | -0.6462 | 0.5429 | ±1.0857 | -1.190 | 0.2339 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **384**, R² = **0.3463**, Adj R² = **0.3215**, F-statistic = **13.96** (p = **9.79e-27**), Residual SE = **1.859** on **369** df, AIC = **1580.4**, BIC = **1639.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.2129** | 0.8698 | ±1.7396 | **+27.837** | **1.56e-170** | *** |
| Education: graduate level (vs college) | +0.0345 | 0.2063 | ±0.4126 | +0.167 | 0.8672 |  |
| Education: high school or below (vs college) | +0.3764 | 0.3864 | ±0.7728 | +0.974 | 0.3300 |  |
| Site: UCSD (vs UAB) | -0.3612 | 0.2591 | ±0.5182 | -1.394 | 0.1633 |  |
| **Site: UW (vs UAB)** | **-1.1192** | 0.2515 | ±0.5030 | **-4.450** | **8.60e-06** | *** |
| Season: spring (vs autumn) | -0.2757 | 0.2952 | ±0.5904 | -0.934 | 0.3503 |  |
| **Season: summer (vs autumn)** | **+1.7983** | 0.3534 | ±0.7068 | **+5.088** | **3.61e-07** | *** |
| **Season: winter (vs autumn)** | **-1.4986** | 0.2941 | ±0.5881 | **-5.096** | **3.46e-07** | *** |
| Age (years) | +0.0070 | 0.0090 | ±0.0180 | +0.782 | 0.4341 |  |
| BMI (kg/m2) | +0.0189 | 0.0168 | ±0.0337 | +1.122 | 0.2617 |  |
| Hypertension | -0.1934 | 0.2337 | ±0.4674 | -0.828 | 0.4079 |  |
| High cholesterol | -0.2696 | 0.2068 | ±0.4135 | -1.304 | 0.1923 |  |
| Kidney disease | +0.7083 | 0.3637 | ±0.7275 | +1.947 | 0.0515 | . |
| Circulatory disease | +0.6500 | 0.3929 | ±0.7857 | +1.655 | 0.0980 | . |
| Time < 70 (%) | -0.6397 | 0.5008 | ±1.0017 | -1.277 | 0.2015 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **384**, R² = **0.3451**, Adj R² = **0.3203**, F-statistic = **13.89** (p = **1.34e-26**), Residual SE = **1.860** on **369** df, AIC = **1581.1**, BIC = **1640.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1838** | 0.8646 | ±1.7293 | **+27.970** | **3.74e-172** | *** |
| Education: graduate level (vs college) | +0.0352 | 0.2067 | ±0.4134 | +0.170 | 0.8649 |  |
| Education: high school or below (vs college) | +0.3798 | 0.3868 | ±0.7737 | +0.982 | 0.3262 |  |
| Site: UCSD (vs UAB) | -0.3421 | 0.2577 | ±0.5154 | -1.328 | 0.1843 |  |
| **Site: UW (vs UAB)** | **-1.0991** | 0.2498 | ±0.4995 | **-4.401** | **1.08e-05** | *** |
| Season: spring (vs autumn) | -0.2918 | 0.2937 | ±0.5875 | -0.994 | 0.3204 |  |
| **Season: summer (vs autumn)** | **+1.7798** | 0.3521 | ±0.7042 | **+5.055** | **4.30e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5080** | 0.2937 | ±0.5873 | **-5.135** | **2.82e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0180 | +0.785 | 0.4325 |  |
| BMI (kg/m2) | +0.0188 | 0.0167 | ±0.0333 | +1.129 | 0.2590 |  |
| Hypertension | -0.2034 | 0.2339 | ±0.4679 | -0.870 | 0.3845 |  |
| High cholesterol | -0.2798 | 0.2081 | ±0.4161 | -1.345 | 0.1787 |  |
| **Kidney disease** | **+0.7308** | 0.3642 | ±0.7284 | **+2.007** | **0.0448** | * |
| Circulatory disease | +0.6549 | 0.3930 | ±0.7859 | +1.667 | 0.0956 | . |
| Avg. daily time < 70 (%) | -0.5138 | 0.4878 | ±0.9757 | -1.053 | 0.2922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.3432**, Adj R² = **0.3183**, F-statistic = **13.77** (p = **2.21e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.3**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +42.0935 | 211.8386 | ±423.6772 | +0.199 | 0.8425 |  |
| Education: graduate level (vs college) | +0.0432 | 0.2068 | ±0.4136 | +0.209 | 0.8345 |  |
| Education: high school or below (vs college) | +0.3671 | 0.3890 | ±0.7779 | +0.944 | 0.3453 |  |
| Site: UCSD (vs UAB) | -0.3245 | 0.2600 | ±0.5200 | -1.248 | 0.2120 |  |
| **Site: UW (vs UAB)** | **-1.0855** | 0.2522 | ±0.5044 | **-4.304** | **1.68e-05** | *** |
| Season: spring (vs autumn) | -0.2862 | 0.2941 | ±0.5882 | -0.973 | 0.3305 |  |
| **Season: summer (vs autumn)** | **+1.7931** | 0.3523 | ±0.7046 | **+5.090** | **3.59e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5176** | 0.2925 | ±0.5851 | **-5.188** | **2.13e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0180 | +0.786 | 0.4319 |  |
| BMI (kg/m2) | +0.0188 | 0.0166 | ±0.0332 | +1.132 | 0.2576 |  |
| Hypertension | -0.1772 | 0.2305 | ±0.4611 | -0.769 | 0.4422 |  |
| High cholesterol | -0.2933 | 0.2073 | ±0.4146 | -1.415 | 0.1572 |  |
| **Kidney disease** | **+0.7570** | 0.3605 | ±0.7210 | **+2.100** | **0.0357** | * |
| Circulatory disease | +0.6391 | 0.3921 | ±0.7842 | +1.630 | 0.1031 |  |
| Time 54-250, pooled (%) | -0.1800 | 2.1187 | ±4.2374 | -0.085 | 0.9323 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.3432**, Adj R² = **0.3183**, F-statistic = **13.77** (p = **2.20e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.2**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +49.6526 | 273.3871 | ±546.7742 | +0.182 | 0.8559 |  |
| Education: graduate level (vs college) | +0.0425 | 0.2073 | ±0.4146 | +0.205 | 0.8375 |  |
| Education: high school or below (vs college) | +0.3663 | 0.3890 | ±0.7781 | +0.941 | 0.3465 |  |
| Site: UCSD (vs UAB) | -0.3255 | 0.2589 | ±0.5178 | -1.257 | 0.2086 |  |
| **Site: UW (vs UAB)** | **-1.0862** | 0.2515 | ±0.5031 | **-4.318** | **1.57e-05** | *** |
| Season: spring (vs autumn) | -0.2859 | 0.2946 | ±0.5893 | -0.970 | 0.3319 |  |
| **Season: summer (vs autumn)** | **+1.7956** | 0.3516 | ±0.7033 | **+5.106** | **3.28e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5173** | 0.2930 | ±0.5860 | **-5.178** | **2.24e-07** | *** |
| Age (years) | +0.0071 | 0.0090 | ±0.0180 | +0.786 | 0.4319 |  |
| BMI (kg/m2) | +0.0188 | 0.0166 | ±0.0331 | +1.138 | 0.2553 |  |
| Hypertension | -0.1767 | 0.2323 | ±0.4645 | -0.761 | 0.4467 |  |
| High cholesterol | -0.2932 | 0.2072 | ±0.4145 | -1.415 | 0.1571 |  |
| **Kidney disease** | **+0.7561** | 0.3603 | ±0.7206 | **+2.098** | **0.0359** | * |
| Circulatory disease | +0.6380 | 0.3931 | ±0.7862 | +1.623 | 0.1046 |  |
| Avg. daily time 54-250 (%) | -0.2556 | 2.7341 | ±5.4682 | -0.093 | 0.9255 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **384**, R² = **0.3435**, Adj R² = **0.3186**, F-statistic = **13.79** (p = **2.06e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.1**, BIC = **1641.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1541** | 0.8657 | ±1.7313 | **+27.903** | **2.48e-171** | *** |
| Education: graduate level (vs college) | +0.0446 | 0.2063 | ±0.4125 | +0.216 | 0.8287 |  |
| Education: high school or below (vs college) | +0.3641 | 0.3914 | ±0.7827 | +0.930 | 0.3521 |  |
| Site: UCSD (vs UAB) | -0.3277 | 0.2577 | ±0.5153 | -1.272 | 0.2035 |  |
| **Site: UW (vs UAB)** | **-1.0853** | 0.2508 | ±0.5016 | **-4.327** | **1.51e-05** | *** |
| Season: spring (vs autumn) | -0.2835 | 0.2944 | ±0.5888 | -0.963 | 0.3355 |  |
| **Season: summer (vs autumn)** | **+1.8001** | 0.3540 | ±0.7080 | **+5.085** | **3.67e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5140** | 0.2925 | ±0.5850 | **-5.176** | **2.27e-07** | *** |
| Age (years) | +0.0069 | 0.0090 | ±0.0180 | +0.766 | 0.4437 |  |
| BMI (kg/m2) | +0.0185 | 0.0164 | ±0.0328 | +1.130 | 0.2584 |  |
| Hypertension | -0.1723 | 0.2311 | ±0.4622 | -0.746 | 0.4559 |  |
| High cholesterol | -0.2945 | 0.2066 | ±0.4132 | -1.426 | 0.1540 |  |
| **Kidney disease** | **+0.7718** | 0.3632 | ±0.7265 | **+2.125** | **0.0336** | * |
| Circulatory disease | +0.6420 | 0.3924 | ±0.7848 | +1.636 | 0.1018 |  |
| Time 181-250, pooled (%) | -0.1339 | 0.3512 | ±0.7023 | -0.381 | 0.7030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **384**, R² = **0.3433**, Adj R² = **0.3183**, F-statistic = **13.78** (p = **2.17e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.2**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1276** | 0.8703 | ±1.7405 | **+27.724** | **3.55e-169** | *** |
| Education: graduate level (vs college) | +0.0439 | 0.2063 | ±0.4127 | +0.213 | 0.8314 |  |
| Education: high school or below (vs college) | +0.3627 | 0.3915 | ±0.7830 | +0.927 | 0.3542 |  |
| Site: UCSD (vs UAB) | -0.3283 | 0.2579 | ±0.5158 | -1.273 | 0.2031 |  |
| **Site: UW (vs UAB)** | **-1.0860** | 0.2507 | ±0.5014 | **-4.332** | **1.48e-05** | *** |
| Season: spring (vs autumn) | -0.2838 | 0.2954 | ±0.5907 | -0.961 | 0.3367 |  |
| **Season: summer (vs autumn)** | **+1.7965** | 0.3532 | ±0.7063 | **+5.087** | **3.64e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5158** | 0.2926 | ±0.5853 | **-5.180** | **2.22e-07** | *** |
| Age (years) | +0.0069 | 0.0091 | ±0.0182 | +0.759 | 0.4478 |  |
| BMI (kg/m2) | +0.0188 | 0.0165 | ±0.0330 | +1.139 | 0.2546 |  |
| Hypertension | -0.1739 | 0.2316 | ±0.4632 | -0.751 | 0.4528 |  |
| High cholesterol | -0.2926 | 0.2080 | ±0.4160 | -1.407 | 0.1595 |  |
| **Kidney disease** | **+0.7594** | 0.3631 | ±0.7263 | **+2.091** | **0.0365** | * |
| Circulatory disease | +0.6421 | 0.3930 | ±0.7859 | +1.634 | 0.1022 |  |
| Avg. daily time 181-250 (%) | -0.0700 | 0.3504 | ±0.7008 | -0.200 | 0.8416 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **384**, R² = **0.3435**, Adj R² = **0.3186**, F-statistic = **13.79** (p = **2.06e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.1**, BIC = **1641.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1552** | 0.8658 | ±1.7316 | **+27.899** | **2.75e-171** | *** |
| Education: graduate level (vs college) | +0.0445 | 0.2063 | ±0.4125 | +0.216 | 0.8290 |  |
| Education: high school or below (vs college) | +0.3640 | 0.3914 | ±0.7828 | +0.930 | 0.3523 |  |
| Site: UCSD (vs UAB) | -0.3277 | 0.2577 | ±0.5153 | -1.272 | 0.2034 |  |
| **Site: UW (vs UAB)** | **-1.0852** | 0.2508 | ±0.5016 | **-4.327** | **1.51e-05** | *** |
| Season: spring (vs autumn) | -0.2835 | 0.2944 | ±0.5888 | -0.963 | 0.3356 |  |
| **Season: summer (vs autumn)** | **+1.8002** | 0.3540 | ±0.7080 | **+5.085** | **3.67e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5139** | 0.2925 | ±0.5851 | **-5.175** | **2.28e-07** | *** |
| Age (years) | +0.0069 | 0.0090 | ±0.0180 | +0.765 | 0.4442 |  |
| BMI (kg/m2) | +0.0185 | 0.0164 | ±0.0328 | +1.130 | 0.2585 |  |
| Hypertension | -0.1723 | 0.2311 | ±0.4622 | -0.746 | 0.4559 |  |
| High cholesterol | -0.2944 | 0.2067 | ±0.4133 | -1.425 | 0.1542 |  |
| **Kidney disease** | **+0.7719** | 0.3633 | ±0.7265 | **+2.125** | **0.0336** | * |
| Circulatory disease | +0.6420 | 0.3924 | ±0.7848 | +1.636 | 0.1018 |  |
| Time > 180 (%) | -0.1356 | 0.3507 | ±0.7014 | -0.387 | 0.6991 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **384**, R² = **0.3433**, Adj R² = **0.3184**, F-statistic = **13.78** (p = **2.17e-26**), Residual SE = **1.863** on **369** df, AIC = **1582.2**, BIC = **1641.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.1286** | 0.8705 | ±1.7410 | **+27.717** | **4.32e-169** | *** |
| Education: graduate level (vs college) | +0.0439 | 0.2063 | ±0.4127 | +0.213 | 0.8315 |  |
| Education: high school or below (vs college) | +0.3626 | 0.3915 | ±0.7831 | +0.926 | 0.3544 |  |
| Site: UCSD (vs UAB) | -0.3283 | 0.2579 | ±0.5158 | -1.273 | 0.2030 |  |
| **Site: UW (vs UAB)** | **-1.0859** | 0.2507 | ±0.5014 | **-4.332** | **1.48e-05** | *** |
| Season: spring (vs autumn) | -0.2837 | 0.2954 | ±0.5907 | -0.961 | 0.3368 |  |
| **Season: summer (vs autumn)** | **+1.7966** | 0.3532 | ±0.7063 | **+5.087** | **3.64e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5156** | 0.2927 | ±0.5853 | **-5.179** | **2.24e-07** | *** |
| Age (years) | +0.0069 | 0.0091 | ±0.0182 | +0.758 | 0.4483 |  |
| BMI (kg/m2) | +0.0188 | 0.0165 | ±0.0330 | +1.139 | 0.2547 |  |
| Hypertension | -0.1739 | 0.2316 | ±0.4632 | -0.751 | 0.4529 |  |
| High cholesterol | -0.2925 | 0.2081 | ±0.4162 | -1.406 | 0.1598 |  |
| **Kidney disease** | **+0.7595** | 0.3632 | ±0.7264 | **+2.091** | **0.0365** | * |
| Circulatory disease | +0.6421 | 0.3930 | ±0.7859 | +1.634 | 0.1022 |  |
| Avg. daily time > 180 (%) | -0.0719 | 0.3497 | ±0.6995 | -0.206 | 0.8370 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 384)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **384**, R² = **0.3449**, Adj R² = **0.3201**, F-statistic = **13.88** (p = **1.41e-26**), Residual SE = **1.861** on **369** df, AIC = **1581.3**, BIC = **1640.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0213** | 0.8628 | ±1.7257 | **+27.840** | **1.44e-170** | *** |
| Education: graduate level (vs college) | +0.0545 | 0.2074 | ±0.4147 | +0.263 | 0.7925 |  |
| Education: high school or below (vs college) | +0.3689 | 0.3853 | ±0.7706 | +0.957 | 0.3384 |  |
| Site: UCSD (vs UAB) | -0.3168 | 0.2576 | ±0.5152 | -1.230 | 0.2188 |  |
| **Site: UW (vs UAB)** | **-1.0923** | 0.2505 | ±0.5011 | **-4.359** | **1.30e-05** | *** |
| Season: spring (vs autumn) | -0.2963 | 0.2929 | ±0.5859 | -1.011 | 0.3118 |  |
| **Season: summer (vs autumn)** | **+1.7908** | 0.3503 | ±0.7007 | **+5.112** | **3.19e-07** | *** |
| **Season: winter (vs autumn)** | **-1.5415** | 0.2931 | ±0.5863 | **-5.259** | **1.45e-07** | *** |
| Age (years) | +0.0088 | 0.0093 | ±0.0185 | +0.945 | 0.3449 |  |
| BMI (kg/m2) | +0.0175 | 0.0165 | ±0.0329 | +1.062 | 0.2884 |  |
| Hypertension | -0.1884 | 0.2323 | ±0.4646 | -0.811 | 0.4173 |  |
| High cholesterol | -0.3041 | 0.2075 | ±0.4150 | -1.466 | 0.1427 |  |
| **Kidney disease** | **+0.7483** | 0.3617 | ±0.7234 | **+2.069** | **0.0386** | * |
| Circulatory disease | +0.6412 | 0.3885 | ±0.7769 | +1.651 | 0.0988 | . |
| Nocturnal time > 180 (%) | +0.2889 | 0.2596 | ±0.5192 | +1.113 | 0.2658 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 384; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **384**, R² = **0.3083**, Adj R² = **0.2840**, F-statistic = **12.69** (p = **4.52e-23**), Residual SE = **5.674** on **370** df, AIC = **2436.7**, BIC = **2492.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5680** | 2.0759 | ±4.1518 | **+22.914** | **3.34e-116** | *** |
| Education: graduate level (vs college) | +0.7740 | 0.6166 | ±1.2331 | +1.255 | 0.2094 |  |
| Education: high school or below (vs college) | -1.1445 | 1.1983 | ±2.3965 | -0.955 | 0.3395 |  |
| **Site: UCSD (vs UAB)** | **+4.5169** | 0.7799 | ±1.5597 | **+5.792** | **6.96e-09** | *** |
| Site: UW (vs UAB) | -0.8223 | 0.7583 | ±1.5165 | -1.084 | 0.2782 |  |
| Season: spring (vs autumn) | -0.9710 | 0.8341 | ±1.6682 | -1.164 | 0.2444 |  |
| **Season: summer (vs autumn)** | **+3.9692** | 0.9180 | ±1.8360 | **+4.324** | **1.53e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9848** | 0.8908 | ±1.7816 | **-4.473** | **7.70e-06** | *** |
| Age (years) | -0.0376 | 0.0262 | ±0.0525 | -1.432 | 0.1521 |  |
| BMI (kg/m2) | -0.0372 | 0.0406 | ±0.0812 | -0.916 | 0.3595 |  |
| Hypertension | +0.4303 | 0.6921 | ±1.3841 | +0.622 | 0.5341 |  |
| High cholesterol | -0.4429 | 0.6408 | ±1.2816 | -0.691 | 0.4894 |  |
| Kidney disease | -1.1481 | 1.2801 | ±2.5602 | -0.897 | 0.3698 |  |
| Circulatory disease | -0.3590 | 0.9495 | ±1.8990 | -0.378 | 0.7054 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **384**, R² = **0.3103**, Adj R² = **0.2841**, F-statistic = **11.86** (p = **1.00e-22**), Residual SE = **5.674** on **369** df, AIC = **2437.6**, BIC = **2496.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.9019** | 5.5076 | ±11.0152 | **+7.608** | **2.78e-14** | *** |
| Education: graduate level (vs college) | +0.7792 | 0.6170 | ±1.2340 | +1.263 | 0.2066 |  |
| Education: high school or below (vs college) | -1.1820 | 1.1892 | ±2.3784 | -0.994 | 0.3203 |  |
| **Site: UCSD (vs UAB)** | **+4.5210** | 0.7794 | ±1.5588 | **+5.801** | **6.60e-09** | *** |
| Site: UW (vs UAB) | -0.7971 | 0.7561 | ±1.5122 | -1.054 | 0.2918 |  |
| Season: spring (vs autumn) | -0.8296 | 0.8342 | ±1.6685 | -0.994 | 0.3200 |  |
| **Season: summer (vs autumn)** | **+3.9034** | 0.9216 | ±1.8432 | **+4.235** | **2.28e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9423** | 0.8864 | ±1.7729 | **-4.447** | **8.69e-06** | *** |
| Age (years) | -0.0410 | 0.0271 | ±0.0542 | -1.511 | 0.1308 |  |
| BMI (kg/m2) | -0.0412 | 0.0410 | ±0.0819 | -1.006 | 0.3145 |  |
| Hypertension | +0.3721 | 0.6969 | ±1.3937 | +0.534 | 0.5934 |  |
| High cholesterol | -0.5797 | 0.6500 | ±1.3000 | -0.892 | 0.3725 |  |
| Kidney disease | -1.0563 | 1.2982 | ±2.5963 | -0.814 | 0.4158 |  |
| Circulatory disease | -0.2657 | 0.9501 | ±1.9002 | -0.280 | 0.7798 |  |
| HbA1c (%) | +1.0837 | 1.0105 | ±2.0210 | +1.072 | 0.2835 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **384**, R² = **0.3094**, Adj R² = **0.2832**, F-statistic = **11.81** (p = **1.24e-22**), Residual SE = **5.677** on **369** df, AIC = **2438.1**, BIC = **2497.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.1116** | 5.1188 | ±10.2376 | **+8.618** | **6.84e-18** | *** |
| Education: graduate level (vs college) | +0.7623 | 0.6152 | ±1.2304 | +1.239 | 0.2153 |  |
| Education: high school or below (vs college) | -1.1260 | 1.2146 | ±2.4292 | -0.927 | 0.3539 |  |
| **Site: UCSD (vs UAB)** | **+4.4856** | 0.7814 | ±1.5628 | **+5.740** | **9.45e-09** | *** |
| Site: UW (vs UAB) | -0.8592 | 0.7604 | ±1.5207 | -1.130 | 0.2585 |  |
| Season: spring (vs autumn) | -0.9427 | 0.8365 | ±1.6730 | -1.127 | 0.2598 |  |
| **Season: summer (vs autumn)** | **+3.9662** | 0.9227 | ±1.8455 | **+4.298** | **1.72e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9717** | 0.8922 | ±1.7843 | **-4.452** | **8.52e-06** | *** |
| Age (years) | -0.0368 | 0.0263 | ±0.0526 | -1.398 | 0.1621 |  |
| BMI (kg/m2) | -0.0396 | 0.0406 | ±0.0812 | -0.975 | 0.3296 |  |
| Hypertension | +0.3949 | 0.7011 | ±1.4022 | +0.563 | 0.5733 |  |
| High cholesterol | -0.4217 | 0.6436 | ±1.2873 | -0.655 | 0.5124 |  |
| Kidney disease | -1.1828 | 1.2815 | ±2.5630 | -0.923 | 0.3560 |  |
| Circulatory disease | -0.3460 | 0.9503 | ±1.9005 | -0.364 | 0.7157 |  |
| Mean glucose (mg/dL) | +0.0306 | 0.0390 | ±0.0780 | +0.785 | 0.4324 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **384**, R² = **0.3094**, Adj R² = **0.2832**, F-statistic = **11.81** (p = **1.24e-22**), Residual SE = **5.677** on **369** df, AIC = **2438.1**, BIC = **2497.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+39.8764** | 10.2883 | ±20.5765 | **+3.876** | **1.06e-04** | *** |
| Education: graduate level (vs college) | +0.7623 | 0.6152 | ±1.2304 | +1.239 | 0.2153 |  |
| Education: high school or below (vs college) | -1.1260 | 1.2146 | ±2.4292 | -0.927 | 0.3539 |  |
| **Site: UCSD (vs UAB)** | **+4.4856** | 0.7814 | ±1.5628 | **+5.740** | **9.45e-09** | *** |
| Site: UW (vs UAB) | -0.8592 | 0.7604 | ±1.5207 | -1.130 | 0.2585 |  |
| Season: spring (vs autumn) | -0.9427 | 0.8365 | ±1.6730 | -1.127 | 0.2598 |  |
| **Season: summer (vs autumn)** | **+3.9662** | 0.9227 | ±1.8455 | **+4.298** | **1.72e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9717** | 0.8922 | ±1.7843 | **-4.452** | **8.52e-06** | *** |
| Age (years) | -0.0368 | 0.0263 | ±0.0526 | -1.398 | 0.1621 |  |
| BMI (kg/m2) | -0.0396 | 0.0406 | ±0.0812 | -0.975 | 0.3296 |  |
| Hypertension | +0.3949 | 0.7011 | ±1.4022 | +0.563 | 0.5733 |  |
| High cholesterol | -0.4217 | 0.6436 | ±1.2873 | -0.655 | 0.5124 |  |
| Kidney disease | -1.1828 | 1.2815 | ±2.5630 | -0.923 | 0.3560 |  |
| Circulatory disease | -0.3460 | 0.9503 | ±1.9005 | -0.364 | 0.7157 |  |
| GMI (%) | +1.2795 | 1.6296 | ±3.2592 | +0.785 | 0.4324 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **384**, R² = **0.3117**, Adj R² = **0.2856**, F-statistic = **11.94** (p = **7.03e-23**), Residual SE = **5.668** on **369** df, AIC = **2436.8**, BIC = **2496.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.6731** | 4.4617 | ±8.9235 | **+9.564** | **1.13e-21** | *** |
| Education: graduate level (vs college) | +0.8082 | 0.6200 | ±1.2400 | +1.304 | 0.1924 |  |
| Education: high school or below (vs college) | -1.0757 | 1.2240 | ±2.4480 | -0.879 | 0.3795 |  |
| **Site: UCSD (vs UAB)** | **+4.4093** | 0.7831 | ±1.5662 | **+5.631** | **1.80e-08** | *** |
| Site: UW (vs UAB) | -0.9139 | 0.7590 | ±1.5179 | -1.204 | 0.2286 |  |
| Season: spring (vs autumn) | -0.9633 | 0.8358 | ±1.6717 | -1.153 | 0.2491 |  |
| **Season: summer (vs autumn)** | **+3.9391** | 0.9248 | ±1.8496 | **+4.259** | **2.05e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9858** | 0.8935 | ±1.7869 | **-4.461** | **8.16e-06** | *** |
| Age (years) | -0.0323 | 0.0269 | ±0.0537 | -1.203 | 0.2290 |  |
| BMI (kg/m2) | -0.0469 | 0.0412 | ±0.0824 | -1.140 | 0.2543 |  |
| Hypertension | +0.3933 | 0.6966 | ±1.3932 | +0.565 | 0.5723 |  |
| High cholesterol | -0.4367 | 0.6415 | ±1.2830 | -0.681 | 0.4960 |  |
| Kidney disease | -1.1190 | 1.2869 | ±2.5739 | -0.870 | 0.3846 |  |
| Circulatory disease | -0.3220 | 0.9416 | ±1.8832 | -0.342 | 0.7324 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0428 | 0.0315 | ±0.0630 | +1.359 | 0.1742 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **384**, R² = **0.3083**, Adj R² = **0.2821**, F-statistic = **11.75** (p = **1.65e-22**), Residual SE = **5.682** on **369** df, AIC = **2438.7**, BIC = **2498.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.7160** | 3.0216 | ±6.0431 | **+15.792** | **3.54e-56** | *** |
| Education: graduate level (vs college) | +0.7716 | 0.6200 | ±1.2401 | +1.244 | 0.2134 |  |
| Education: high school or below (vs college) | -1.1439 | 1.2010 | ±2.4019 | -0.952 | 0.3408 |  |
| **Site: UCSD (vs UAB)** | **+4.5121** | 0.7814 | ±1.5628 | **+5.774** | **7.73e-09** | *** |
| Site: UW (vs UAB) | -0.8252 | 0.7618 | ±1.5235 | -1.083 | 0.2787 |  |
| Season: spring (vs autumn) | -0.9667 | 0.8413 | ±1.6825 | -1.149 | 0.2505 |  |
| **Season: summer (vs autumn)** | **+3.9721** | 0.9240 | ±1.8480 | **+4.299** | **1.72e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9802** | 0.9035 | ±1.8070 | **-4.405** | **1.06e-05** | *** |
| Age (years) | -0.0376 | 0.0263 | ±0.0527 | -1.426 | 0.1537 |  |
| BMI (kg/m2) | -0.0371 | 0.0407 | ±0.0815 | -0.910 | 0.3630 |  |
| Hypertension | +0.4304 | 0.6942 | ±1.3885 | +0.620 | 0.5353 |  |
| High cholesterol | -0.4450 | 0.6458 | ±1.2916 | -0.689 | 0.4908 |  |
| Kidney disease | -1.1444 | 1.2839 | ±2.5677 | -0.891 | 0.3727 |  |
| Circulatory disease | -0.3572 | 0.9495 | ±1.8989 | -0.376 | 0.7067 |  |
| Glucose SD, pooled (mg/dL) | -0.0091 | 0.1407 | ±0.2815 | -0.064 | 0.9487 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **384**, R² = **0.3088**, Adj R² = **0.2826**, F-statistic = **11.78** (p = **1.44e-22**), Residual SE = **5.680** on **369** df, AIC = **2438.4**, BIC = **2497.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5176** | 2.9345 | ±5.8691 | **+15.852** | **1.37e-56** | *** |
| Education: graduate level (vs college) | +0.7954 | 0.6191 | ±1.2383 | +1.285 | 0.1989 |  |
| Education: high school or below (vs college) | -1.1385 | 1.2102 | ±2.4204 | -0.941 | 0.3468 |  |
| **Site: UCSD (vs UAB)** | **+4.5573** | 0.7774 | ±1.5548 | **+5.862** | **4.56e-09** | *** |
| Site: UW (vs UAB) | -0.7978 | 0.7580 | ±1.5159 | -1.053 | 0.2925 |  |
| Season: spring (vs autumn) | -0.9996 | 0.8380 | ±1.6760 | -1.193 | 0.2329 |  |
| **Season: summer (vs autumn)** | **+3.9538** | 0.9226 | ±1.8453 | **+4.285** | **1.82e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0052** | 0.8990 | ±1.7980 | **-4.455** | **8.39e-06** | *** |
| Age (years) | -0.0377 | 0.0262 | ±0.0525 | -1.436 | 0.1510 |  |
| BMI (kg/m2) | -0.0391 | 0.0410 | ±0.0821 | -0.953 | 0.3407 |  |
| Hypertension | +0.4361 | 0.6910 | ±1.3820 | +0.631 | 0.5280 |  |
| High cholesterol | -0.4301 | 0.6454 | ±1.2908 | -0.666 | 0.5052 |  |
| Kidney disease | -1.1783 | 1.2717 | ±2.5434 | -0.927 | 0.3542 |  |
| Circulatory disease | -0.3625 | 0.9467 | ±1.8935 | -0.383 | 0.7018 |  |
| Avg. daily SD (mg/dL) | +0.0710 | 0.1442 | ±0.2884 | +0.492 | 0.6224 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **384**, R² = **0.3086**, Adj R² = **0.2823**, F-statistic = **11.76** (p = **1.55e-22**), Residual SE = **5.681** on **369** df, AIC = **2438.6**, BIC = **2497.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.3544** | 2.9184 | ±5.8369 | **+16.569** | **1.17e-61** | *** |
| Education: graduate level (vs college) | +0.7586 | 0.6180 | ±1.2359 | +1.228 | 0.2196 |  |
| Education: high school or below (vs college) | -1.1372 | 1.2000 | ±2.4000 | -0.948 | 0.3433 |  |
| **Site: UCSD (vs UAB)** | **+4.4847** | 0.7824 | ±1.5649 | **+5.732** | **9.94e-09** | *** |
| Site: UW (vs UAB) | -0.8465 | 0.7647 | ±1.5294 | -1.107 | 0.2683 |  |
| Season: spring (vs autumn) | -0.9416 | 0.8425 | ±1.6850 | -1.118 | 0.2638 |  |
| **Season: summer (vs autumn)** | **+3.9857** | 0.9245 | ±1.8491 | **+4.311** | **1.62e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9574** | 0.9012 | ±1.8025 | **-4.391** | **1.13e-05** | *** |
| Age (years) | -0.0373 | 0.0264 | ±0.0528 | -1.414 | 0.1573 |  |
| BMI (kg/m2) | -0.0370 | 0.0407 | ±0.0815 | -0.909 | 0.3633 |  |
| Hypertension | +0.4230 | 0.6946 | ±1.3892 | +0.609 | 0.5426 |  |
| High cholesterol | -0.4501 | 0.6442 | ±1.2885 | -0.699 | 0.4847 |  |
| Kidney disease | -1.1376 | 1.2927 | ±2.5853 | -0.880 | 0.3789 |  |
| Circulatory disease | -0.3459 | 0.9510 | ±1.9019 | -0.364 | 0.7161 |  |
| CV (%) | -0.0542 | 0.1571 | ±0.3142 | -0.345 | 0.7303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **384**, R² = **0.3087**, Adj R² = **0.2825**, F-statistic = **11.77** (p = **1.49e-22**), Residual SE = **5.680** on **369** df, AIC = **2438.5**, BIC = **2497.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.5997** | 3.1959 | ±6.3917 | **+14.581** | **3.70e-48** | *** |
| Education: graduate level (vs college) | +0.7524 | 0.6179 | ±1.2358 | +1.218 | 0.2234 |  |
| Education: high school or below (vs college) | -1.1351 | 1.1992 | ±2.3983 | -0.947 | 0.3439 |  |
| **Site: UCSD (vs UAB)** | **+4.4837** | 0.7835 | ±1.5671 | **+5.722** | **1.05e-08** | *** |
| Site: UW (vs UAB) | -0.8460 | 0.7644 | ±1.5288 | -1.107 | 0.2684 |  |
| Season: spring (vs autumn) | -0.9318 | 0.8419 | ±1.6837 | -1.107 | 0.2683 |  |
| **Season: summer (vs autumn)** | **+3.9874** | 0.9233 | ±1.8466 | **+4.319** | **1.57e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9511** | 0.9006 | ±1.8013 | **-4.387** | **1.15e-05** | *** |
| Age (years) | -0.0374 | 0.0264 | ±0.0527 | -1.419 | 0.1560 |  |
| BMI (kg/m2) | -0.0370 | 0.0407 | ±0.0815 | -0.909 | 0.3632 |  |
| Hypertension | +0.4265 | 0.6952 | ±1.3904 | +0.613 | 0.5396 |  |
| High cholesterol | -0.4526 | 0.6440 | ±1.2881 | -0.703 | 0.4822 |  |
| Kidney disease | -1.1421 | 1.2884 | ±2.5768 | -0.886 | 0.3754 |  |
| Circulatory disease | -0.3441 | 0.9510 | ±1.9020 | -0.362 | 0.7175 |  |
| Mean / SD ratio | +0.1385 | 0.3208 | ±0.6417 | +0.432 | 0.6661 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **384**, R² = **0.3088**, Adj R² = **0.2826**, F-statistic = **11.77** (p = **1.46e-22**), Residual SE = **5.680** on **369** df, AIC = **2438.4**, BIC = **2497.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5599** | 3.1038 | ±6.2077 | **+15.645** | **3.59e-55** | *** |
| Education: graduate level (vs college) | +0.8006 | 0.6170 | ±1.2339 | +1.298 | 0.1944 |  |
| Education: high school or below (vs college) | -1.1454 | 1.2059 | ±2.4117 | -0.950 | 0.3422 |  |
| **Site: UCSD (vs UAB)** | **+4.5560** | 0.7773 | ±1.5547 | **+5.861** | **4.60e-09** | *** |
| Site: UW (vs UAB) | -0.7979 | 0.7601 | ±1.5202 | -1.050 | 0.2939 |  |
| Season: spring (vs autumn) | -1.0131 | 0.8339 | ±1.6679 | -1.215 | 0.2244 |  |
| **Season: summer (vs autumn)** | **+3.9525** | 0.9212 | ±1.8424 | **+4.291** | **1.78e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0112** | 0.8967 | ±1.7933 | **-4.473** | **7.70e-06** | *** |
| Age (years) | -0.0378 | 0.0263 | ±0.0526 | -1.438 | 0.1505 |  |
| BMI (kg/m2) | -0.0386 | 0.0411 | ±0.0821 | -0.941 | 0.3469 |  |
| Hypertension | +0.4435 | 0.6898 | ±1.3796 | +0.643 | 0.5203 |  |
| High cholesterol | -0.4370 | 0.6442 | ±1.2884 | -0.678 | 0.4975 |  |
| Kidney disease | -1.1609 | 1.2776 | ±2.5553 | -0.909 | 0.3635 |  |
| Circulatory disease | -0.3664 | 0.9466 | ±1.8932 | -0.387 | 0.6987 |  |
| Avg. daily mean/SD | -0.1217 | 0.2706 | ±0.5412 | -0.450 | 0.6528 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **384**, R² = **0.3089**, Adj R² = **0.2827**, F-statistic = **11.78** (p = **1.42e-22**), Residual SE = **5.680** on **369** df, AIC = **2438.4**, BIC = **2497.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.3941** | 3.0650 | ±6.1301 | **+15.137** | **9.30e-52** | *** |
| Education: graduate level (vs college) | +0.7653 | 0.6173 | ±1.2346 | +1.240 | 0.2151 |  |
| Education: high school or below (vs college) | -1.1931 | 1.2111 | ±2.4222 | -0.985 | 0.3245 |  |
| **Site: UCSD (vs UAB)** | **+4.5505** | 0.7815 | ±1.5630 | **+5.823** | **5.79e-09** | *** |
| Site: UW (vs UAB) | -0.7682 | 0.7654 | ±1.5308 | -1.004 | 0.3155 |  |
| Season: spring (vs autumn) | -0.9940 | 0.8310 | ±1.6620 | -1.196 | 0.2316 |  |
| **Season: summer (vs autumn)** | **+3.9717** | 0.9221 | ±1.8441 | **+4.307** | **1.65e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0090** | 0.8966 | ±1.7932 | **-4.471** | **7.77e-06** | *** |
| Age (years) | -0.0355 | 0.0268 | ±0.0536 | -1.326 | 0.1849 |  |
| BMI (kg/m2) | -0.0354 | 0.0407 | ±0.0815 | -0.870 | 0.3841 |  |
| Hypertension | +0.4438 | 0.6919 | ±1.3839 | +0.641 | 0.5212 |  |
| High cholesterol | -0.4635 | 0.6434 | ±1.2868 | -0.720 | 0.4713 |  |
| Kidney disease | -1.1856 | 1.2846 | ±2.5693 | -0.923 | 0.3560 |  |
| Circulatory disease | -0.3587 | 0.9495 | ±1.8990 | -0.378 | 0.7056 |  |
| MAG (mg/dL/h) | +0.0292 | 0.0537 | ±0.1074 | +0.544 | 0.5867 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **384**, R² = **0.3086**, Adj R² = **0.2824**, F-statistic = **11.76** (p = **1.54e-22**), Residual SE = **5.681** on **369** df, AIC = **2438.5**, BIC = **2497.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.6621** | 3.2481 | ±6.4962 | **+14.366** | **8.46e-47** | *** |
| Education: graduate level (vs college) | +0.7779 | 0.6187 | ±1.2374 | +1.257 | 0.2087 |  |
| Education: high school or below (vs college) | -1.1446 | 1.2055 | ±2.4111 | -0.949 | 0.3424 |  |
| **Site: UCSD (vs UAB)** | **+4.5449** | 0.7780 | ±1.5561 | **+5.841** | **5.18e-09** | *** |
| Site: UW (vs UAB) | -0.8023 | 0.7565 | ±1.5130 | -1.060 | 0.2889 |  |
| Season: spring (vs autumn) | -0.9937 | 0.8382 | ±1.6763 | -1.186 | 0.2358 |  |
| **Season: summer (vs autumn)** | **+3.9605** | 0.9229 | ±1.8459 | **+4.291** | **1.78e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0062** | 0.9008 | ±1.8015 | **-4.448** | **8.69e-06** | *** |
| Age (years) | -0.0374 | 0.0263 | ±0.0526 | -1.421 | 0.1553 |  |
| BMI (kg/m2) | -0.0359 | 0.0406 | ±0.0812 | -0.884 | 0.3765 |  |
| Hypertension | +0.4431 | 0.6900 | ±1.3800 | +0.642 | 0.5207 |  |
| High cholesterol | -0.4453 | 0.6429 | ±1.2858 | -0.693 | 0.4885 |  |
| Kidney disease | -1.1609 | 1.2751 | ±2.5501 | -0.910 | 0.3626 |  |
| Circulatory disease | -0.3668 | 0.9464 | ±1.8929 | -0.388 | 0.6984 |  |
| Avg. daily range (mg/dL) | +0.0107 | 0.0311 | ±0.0621 | +0.344 | 0.7310 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **384**, R² = **0.3083**, Adj R² = **0.2821**, F-statistic = **11.75** (p = **1.65e-22**), Residual SE = **5.682** on **369** df, AIC = **2438.7**, BIC = **2498.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5228** | 2.1401 | ±4.2803 | **+22.206** | **3.04e-109** | *** |
| Education: graduate level (vs college) | +0.7723 | 0.6207 | ±1.2414 | +1.244 | 0.2134 |  |
| Education: high school or below (vs college) | -1.1487 | 1.2078 | ±2.4156 | -0.951 | 0.3416 |  |
| **Site: UCSD (vs UAB)** | **+4.5181** | 0.7839 | ±1.5677 | **+5.764** | **8.22e-09** | *** |
| Site: UW (vs UAB) | -0.8242 | 0.7564 | ±1.5129 | -1.090 | 0.2759 |  |
| Season: spring (vs autumn) | -0.9745 | 0.8442 | ±1.6884 | -1.154 | 0.2484 |  |
| **Season: summer (vs autumn)** | **+3.9653** | 0.9246 | ±1.8492 | **+4.289** | **1.80e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9902** | 0.9102 | ±1.8205 | **-4.384** | **1.17e-05** | *** |
| Age (years) | -0.0376 | 0.0264 | ±0.0527 | -1.426 | 0.1539 |  |
| BMI (kg/m2) | -0.0372 | 0.0407 | ±0.0814 | -0.914 | 0.3606 |  |
| Hypertension | +0.4277 | 0.6904 | ±1.3807 | +0.620 | 0.5356 |  |
| High cholesterol | -0.4437 | 0.6422 | ±1.2843 | -0.691 | 0.4896 |  |
| Kidney disease | -1.1435 | 1.2857 | ±2.5715 | -0.889 | 0.3738 |  |
| Circulatory disease | -0.3624 | 0.9568 | ±1.9136 | -0.379 | 0.7049 |  |
| SD of daily means (mg/dL) | +0.0105 | 0.1732 | ±0.3464 | +0.061 | 0.9515 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **384**, R² = **0.3102**, Adj R² = **0.2841**, F-statistic = **11.86** (p = **1.02e-22**), Residual SE = **5.674** on **369** df, AIC = **2437.6**, BIC = **2496.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +147.8247 | 98.2035 | ±196.4071 | +1.505 | 0.1322 |  |
| Education: graduate level (vs college) | +0.7752 | 0.6176 | ±1.2352 | +1.255 | 0.2094 |  |
| Education: high school or below (vs college) | -1.1532 | 1.2023 | ±2.4045 | -0.959 | 0.3375 |  |
| **Site: UCSD (vs UAB)** | **+4.5709** | 0.7793 | ±1.5586 | **+5.865** | **4.48e-09** | *** |
| Site: UW (vs UAB) | -0.7841 | 0.7615 | ±1.5230 | -1.030 | 0.3032 |  |
| Season: spring (vs autumn) | -1.0114 | 0.8277 | ±1.6554 | -1.222 | 0.2217 |  |
| **Season: summer (vs autumn)** | **+3.9100** | 0.9208 | ±1.8416 | **+4.246** | **2.17e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0422** | 0.8966 | ±1.7932 | **-4.508** | **6.54e-06** | *** |
| Age (years) | -0.0365 | 0.0262 | ±0.0523 | -1.396 | 0.1628 |  |
| BMI (kg/m2) | -0.0345 | 0.0405 | ±0.0810 | -0.853 | 0.3937 |  |
| Hypertension | +0.4330 | 0.6904 | ±1.3808 | +0.627 | 0.5305 |  |
| High cholesterol | -0.4721 | 0.6412 | ±1.2824 | -0.736 | 0.4615 |  |
| Kidney disease | -1.1977 | 1.2748 | ±2.5497 | -0.940 | 0.3475 |  |
| Circulatory disease | -0.3814 | 0.9390 | ±1.8780 | -0.406 | 0.6846 |  |
| Time in range 70-180, pooled (%) | -1.0083 | 0.9862 | ±1.9724 | -1.022 | 0.3066 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **384**, R² = **0.3109**, Adj R² = **0.2848**, F-statistic = **11.89** (p = **8.67e-23**), Residual SE = **5.671** on **369** df, AIC = **2437.3**, BIC = **2496.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +160.1843 | 99.9365 | ±199.8730 | +1.603 | 0.1090 |  |
| Education: graduate level (vs college) | +0.7757 | 0.6175 | ±1.2350 | +1.256 | 0.2091 |  |
| Education: high school or below (vs college) | -1.1356 | 1.2092 | ±2.4183 | -0.939 | 0.3476 |  |
| **Site: UCSD (vs UAB)** | **+4.5609** | 0.7788 | ±1.5575 | **+5.857** | **4.73e-09** | *** |
| Site: UW (vs UAB) | -0.8109 | 0.7609 | ±1.5218 | -1.066 | 0.2865 |  |
| Season: spring (vs autumn) | -1.0053 | 0.8279 | ±1.6557 | -1.214 | 0.2246 |  |
| **Season: summer (vs autumn)** | **+3.9469** | 0.9232 | ±1.8464 | **+4.275** | **1.91e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0362** | 0.8959 | ±1.7918 | **-4.505** | **6.63e-06** | *** |
| Age (years) | -0.0352 | 0.0262 | ±0.0524 | -1.342 | 0.1797 |  |
| BMI (kg/m2) | -0.0360 | 0.0408 | ±0.0816 | -0.882 | 0.3776 |  |
| Hypertension | +0.4626 | 0.6911 | ±1.3821 | +0.669 | 0.5032 |  |
| High cholesterol | -0.4859 | 0.6426 | ±1.2852 | -0.756 | 0.4496 |  |
| Kidney disease | -1.1606 | 1.2779 | ±2.5558 | -0.908 | 0.3637 |  |
| Circulatory disease | -0.4088 | 0.9324 | ±1.8648 | -0.438 | 0.6611 |  |
| Avg. daily time in range 70-180 (%) | -1.1322 | 1.0032 | ±2.0064 | -1.129 | 0.2591 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.3090**, Adj R² = **0.2828**, F-statistic = **11.78** (p = **1.40e-22**), Residual SE = **5.679** on **369** df, AIC = **2438.3**, BIC = **2497.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4831** | 2.0971 | ±4.1942 | **+22.642** | **1.67e-113** | *** |
| Education: graduate level (vs college) | +0.7813 | 0.6178 | ±1.2356 | +1.265 | 0.2060 |  |
| Education: high school or below (vs college) | -1.1350 | 1.2013 | ±2.4025 | -0.945 | 0.3448 |  |
| **Site: UCSD (vs UAB)** | **+4.6016** | 0.7924 | ±1.5847 | **+5.808** | **6.34e-09** | *** |
| Site: UW (vs UAB) | -0.7675 | 0.7675 | ±1.5350 | -1.000 | 0.3173 |  |
| Season: spring (vs autumn) | -1.0344 | 0.8319 | ±1.6639 | -1.243 | 0.2138 |  |
| **Season: summer (vs autumn)** | **+3.9377** | 0.9203 | ±1.8406 | **+4.279** | **1.88e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0285** | 0.8938 | ±1.7876 | **-4.507** | **6.57e-06** | *** |
| Age (years) | -0.0376 | 0.0262 | ±0.0525 | -1.433 | 0.1519 |  |
| BMI (kg/m2) | -0.0372 | 0.0407 | ±0.0815 | -0.912 | 0.3617 |  |
| Hypertension | +0.3982 | 0.6900 | ±1.3799 | +0.577 | 0.5638 |  |
| High cholesterol | -0.4423 | 0.6424 | ±1.2849 | -0.688 | 0.4912 |  |
| Kidney disease | -1.0967 | 1.2898 | ±2.5796 | -0.850 | 0.3952 |  |
| Circulatory disease | -0.3872 | 0.9450 | ±1.8900 | -0.410 | 0.6820 |  |
| Any reading < 54 during wear (0/1) | +0.4880 | 0.8538 | ±1.7076 | +0.572 | 0.5676 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.3091**, Adj R² = **0.2829**, F-statistic = **11.79** (p = **1.36e-22**), Residual SE = **5.679** on **369** df, AIC = **2438.3**, BIC = **2497.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4852** | 2.0870 | ±4.1739 | **+22.753** | **1.33e-114** | *** |
| Education: graduate level (vs college) | +0.7768 | 0.6190 | ±1.2379 | +1.255 | 0.2095 |  |
| Education: high school or below (vs college) | -1.1076 | 1.1994 | ±2.3988 | -0.923 | 0.3558 |  |
| **Site: UCSD (vs UAB)** | **+4.5810** | 0.7836 | ±1.5672 | **+5.846** | **5.04e-09** | *** |
| Site: UW (vs UAB) | -0.7903 | 0.7621 | ±1.5242 | -1.037 | 0.2998 |  |
| Season: spring (vs autumn) | -0.9623 | 0.8397 | ±1.6794 | -1.146 | 0.2518 |  |
| **Season: summer (vs autumn)** | **+3.9647** | 0.9256 | ±1.8512 | **+4.283** | **1.84e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9817** | 0.8954 | ±1.7908 | **-4.447** | **8.72e-06** | *** |
| Age (years) | -0.0368 | 0.0264 | ±0.0528 | -1.395 | 0.1632 |  |
| BMI (kg/m2) | -0.0391 | 0.0410 | ±0.0821 | -0.952 | 0.3412 |  |
| Hypertension | +0.3978 | 0.6896 | ±1.3791 | +0.577 | 0.5640 |  |
| High cholesterol | -0.4385 | 0.6414 | ±1.2829 | -0.684 | 0.4942 |  |
| Kidney disease | -1.1126 | 1.2856 | ±2.5712 | -0.865 | 0.3868 |  |
| Circulatory disease | -0.3975 | 0.9481 | ±1.8961 | -0.419 | 0.6750 |  |
| Time < 54 (%) | +3.7900 | 6.3030 | ±12.6059 | +0.601 | 0.5476 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.3087**, Adj R² = **0.2825**, F-statistic = **11.77** (p = **1.50e-22**), Residual SE = **5.681** on **369** df, AIC = **2438.5**, BIC = **2497.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5200** | 2.0836 | ±4.1671 | **+22.807** | **3.91e-115** | *** |
| Education: graduate level (vs college) | +0.7662 | 0.6209 | ±1.2417 | +1.234 | 0.2172 |  |
| Education: high school or below (vs college) | -1.1337 | 1.2008 | ±2.4015 | -0.944 | 0.3451 |  |
| **Site: UCSD (vs UAB)** | **+4.5427** | 0.7846 | ±1.5692 | **+5.790** | **7.04e-09** | *** |
| Site: UW (vs UAB) | -0.8123 | 0.7634 | ±1.5268 | -1.064 | 0.2873 |  |
| Season: spring (vs autumn) | -0.9618 | 0.8409 | ±1.6818 | -1.144 | 0.2527 |  |
| **Season: summer (vs autumn)** | **+3.9986** | 0.9257 | ±1.8514 | **+4.320** | **1.56e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9783** | 0.8956 | ±1.7913 | **-4.442** | **8.92e-06** | *** |
| Age (years) | -0.0371 | 0.0264 | ±0.0527 | -1.408 | 0.1592 |  |
| BMI (kg/m2) | -0.0380 | 0.0409 | ±0.0817 | -0.930 | 0.3524 |  |
| Hypertension | +0.4164 | 0.6952 | ±1.3905 | +0.599 | 0.5492 |  |
| High cholesterol | -0.4384 | 0.6419 | ±1.2839 | -0.683 | 0.4947 |  |
| Kidney disease | -1.1394 | 1.2844 | ±2.5688 | -0.887 | 0.3750 |  |
| Circulatory disease | -0.3969 | 0.9518 | ±1.9037 | -0.417 | 0.6767 |  |
| Avg. daily time < 54 (%) | +3.2192 | 8.5892 | ±17.1785 | +0.375 | 0.7078 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.3086**, Adj R² = **0.2823**, F-statistic = **11.76** (p = **1.54e-22**), Residual SE = **5.681** on **369** df, AIC = **2438.6**, BIC = **2497.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4700** | 2.0936 | ±4.1871 | **+22.674** | **8.02e-114** | *** |
| Education: graduate level (vs college) | +0.7820 | 0.6170 | ±1.2340 | +1.267 | 0.2050 |  |
| Education: high school or below (vs college) | -1.1620 | 1.2091 | ±2.4182 | -0.961 | 0.3365 |  |
| **Site: UCSD (vs UAB)** | **+4.5400** | 0.7891 | ±1.5783 | **+5.753** | **8.76e-09** | *** |
| Site: UW (vs UAB) | -0.7952 | 0.7752 | ±1.5503 | -1.026 | 0.3050 |  |
| Season: spring (vs autumn) | -0.9834 | 0.8354 | ±1.6709 | -1.177 | 0.2391 |  |
| **Season: summer (vs autumn)** | **+3.9649** | 0.9193 | ±1.8386 | **+4.313** | **1.61e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0044** | 0.8940 | ±1.7879 | **-4.479** | **7.49e-06** | *** |
| Age (years) | -0.0377 | 0.0264 | ±0.0527 | -1.430 | 0.1526 |  |
| BMI (kg/m2) | -0.0369 | 0.0406 | ±0.0813 | -0.908 | 0.3641 |  |
| Hypertension | +0.4537 | 0.7032 | ±1.4063 | +0.645 | 0.5188 |  |
| High cholesterol | -0.4677 | 0.6465 | ±1.2930 | -0.723 | 0.4695 |  |
| Kidney disease | -1.1068 | 1.2865 | ±2.5730 | -0.860 | 0.3896 |  |
| Circulatory disease | -0.3616 | 0.9507 | ±1.9014 | -0.380 | 0.7037 |  |
| Time 54-69, pooled (%) | +0.6452 | 1.7865 | ±3.5730 | +0.361 | 0.7180 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **384**, R² = **0.3083**, Adj R² = **0.2821**, F-statistic = **11.75** (p = **1.65e-22**), Residual SE = **5.682** on **369** df, AIC = **2438.7**, BIC = **2498.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5585** | 2.0838 | ±4.1676 | **+22.823** | **2.71e-115** | *** |
| Education: graduate level (vs college) | +0.7751 | 0.6192 | ±1.2384 | +1.252 | 0.2107 |  |
| Education: high school or below (vs college) | -1.1466 | 1.2081 | ±2.4161 | -0.949 | 0.3426 |  |
| **Site: UCSD (vs UAB)** | **+4.5183** | 0.7853 | ±1.5706 | **+5.754** | **8.73e-09** | *** |
| Site: UW (vs UAB) | -0.8209 | 0.7639 | ±1.5277 | -1.075 | 0.2825 |  |
| Season: spring (vs autumn) | -0.9705 | 0.8377 | ±1.6753 | -1.159 | 0.2466 |  |
| **Season: summer (vs autumn)** | **+3.9704** | 0.9206 | ±1.8413 | **+4.313** | **1.61e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9861** | 0.8937 | ±1.7875 | **-4.460** | **8.20e-06** | *** |
| Age (years) | -0.0376 | 0.0264 | ±0.0527 | -1.426 | 0.1538 |  |
| BMI (kg/m2) | -0.0372 | 0.0407 | ±0.0813 | -0.914 | 0.3608 |  |
| Hypertension | +0.4341 | 0.7027 | ±1.4053 | +0.618 | 0.5367 |  |
| High cholesterol | -0.4447 | 0.6448 | ±1.2895 | -0.690 | 0.4903 |  |
| Kidney disease | -1.1451 | 1.2841 | ±2.5682 | -0.892 | 0.3725 |  |
| Circulatory disease | -0.3600 | 0.9511 | ±1.9021 | -0.379 | 0.7050 |  |
| Avg. daily time 54-69 (%) | +0.0658 | 1.8120 | ±3.6240 | +0.036 | 0.9710 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **384**, R² = **0.3088**, Adj R² = **0.2826**, F-statistic = **11.77** (p = **1.47e-22**), Residual SE = **5.680** on **369** df, AIC = **2438.4**, BIC = **2497.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4373** | 2.0966 | ±4.1933 | **+22.625** | **2.43e-113** | *** |
| Education: graduate level (vs college) | +0.7839 | 0.6168 | ±1.2335 | +1.271 | 0.2038 |  |
| Education: high school or below (vs college) | -1.1576 | 1.2072 | ±2.4144 | -0.959 | 0.3376 |  |
| **Site: UCSD (vs UAB)** | **+4.5565** | 0.7911 | ±1.5823 | **+5.759** | **8.44e-09** | *** |
| Site: UW (vs UAB) | -0.7843 | 0.7753 | ±1.5506 | -1.012 | 0.3117 |  |
| Season: spring (vs autumn) | -0.9838 | 0.8355 | ±1.6709 | -1.178 | 0.2390 |  |
| **Season: summer (vs autumn)** | **+3.9633** | 0.9198 | ±1.8396 | **+4.309** | **1.64e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0071** | 0.8941 | ±1.7882 | **-4.482** | **7.40e-06** | *** |
| Age (years) | -0.0376 | 0.0263 | ±0.0527 | -1.427 | 0.1537 |  |
| BMI (kg/m2) | -0.0372 | 0.0406 | ±0.0813 | -0.915 | 0.3601 |  |
| Hypertension | +0.4511 | 0.6991 | ±1.3982 | +0.645 | 0.5188 |  |
| High cholesterol | -0.4709 | 0.6459 | ±1.2918 | -0.729 | 0.4660 |  |
| Kidney disease | -1.0928 | 1.2875 | ±2.5751 | -0.849 | 0.3960 |  |
| Circulatory disease | -0.3696 | 0.9497 | ±1.8994 | -0.389 | 0.6971 |  |
| Time < 70 (%) | +0.7526 | 1.5922 | ±3.1845 | +0.473 | 0.6364 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **384**, R² = **0.3083**, Adj R² = **0.2821**, F-statistic = **11.75** (p = **1.64e-22**), Residual SE = **5.682** on **369** df, AIC = **2438.7**, BIC = **2497.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5361** | 2.0853 | ±4.1707 | **+22.795** | **5.10e-115** | *** |
| Education: graduate level (vs college) | +0.7770 | 0.6184 | ±1.2369 | +1.256 | 0.2090 |  |
| Education: high school or below (vs college) | -1.1502 | 1.2075 | ±2.4150 | -0.953 | 0.3408 |  |
| **Site: UCSD (vs UAB)** | **+4.5226** | 0.7863 | ±1.5727 | **+5.752** | **8.85e-09** | *** |
| Site: UW (vs UAB) | -0.8175 | 0.7646 | ±1.5291 | -1.069 | 0.2849 |  |
| Season: spring (vs autumn) | -0.9689 | 0.8380 | ±1.6759 | -1.156 | 0.2476 |  |
| **Season: summer (vs autumn)** | **+3.9745** | 0.9215 | ±1.8430 | **+4.313** | **1.61e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9885** | 0.8941 | ±1.7883 | **-4.461** | **8.17e-06** | *** |
| Age (years) | -0.0376 | 0.0263 | ±0.0527 | -1.427 | 0.1536 |  |
| BMI (kg/m2) | -0.0372 | 0.0407 | ±0.0814 | -0.913 | 0.3610 |  |
| Hypertension | +0.4411 | 0.6996 | ±1.3991 | +0.631 | 0.5284 |  |
| High cholesterol | -0.4482 | 0.6444 | ±1.2888 | -0.696 | 0.4867 |  |
| Kidney disease | -1.1386 | 1.2845 | ±2.5690 | -0.886 | 0.3754 |  |
| Circulatory disease | -0.3644 | 0.9505 | ±1.9010 | -0.383 | 0.7014 |  |
| Avg. daily time < 70 (%) | +0.2000 | 1.6469 | ±3.2937 | +0.121 | 0.9033 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.3093**, Adj R² = **0.2831**, F-statistic = **11.80** (p = **1.30e-22**), Residual SE = **5.678** on **369** df, AIC = **2438.2**, BIC = **2497.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +467.1467 | 633.5871 | ±1267.1742 | +0.737 | 0.4609 |  |
| Education: graduate level (vs college) | +0.7800 | 0.6189 | ±1.2378 | +1.260 | 0.2076 |  |
| Education: high school or below (vs college) | -1.1013 | 1.1997 | ±2.3993 | -0.918 | 0.3586 |  |
| **Site: UCSD (vs UAB)** | **+4.5881** | 0.7836 | ±1.5672 | **+5.855** | **4.76e-09** | *** |
| Site: UW (vs UAB) | -0.7891 | 0.7618 | ±1.5236 | -1.036 | 0.3003 |  |
| Season: spring (vs autumn) | -0.9612 | 0.8401 | ±1.6802 | -1.144 | 0.2526 |  |
| **Season: summer (vs autumn)** | **+3.9639** | 0.9262 | ±1.8524 | **+4.280** | **1.87e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9849** | 0.8957 | ±1.7915 | **-4.449** | **8.64e-06** | *** |
| Age (years) | -0.0366 | 0.0264 | ±0.0528 | -1.385 | 0.1659 |  |
| BMI (kg/m2) | -0.0391 | 0.0410 | ±0.0820 | -0.954 | 0.3403 |  |
| Hypertension | +0.3954 | 0.6892 | ±1.3784 | +0.574 | 0.5662 |  |
| High cholesterol | -0.4417 | 0.6415 | ±1.2831 | -0.689 | 0.4911 |  |
| Kidney disease | -1.1078 | 1.2862 | ±2.5723 | -0.861 | 0.3891 |  |
| Circulatory disease | -0.4011 | 0.9474 | ±1.8949 | -0.423 | 0.6720 |  |
| Time 54-250, pooled (%) | -4.1968 | 6.3365 | ±12.6729 | -0.662 | 0.5078 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.3089**, Adj R² = **0.2826**, F-statistic = **11.78** (p = **1.44e-22**), Residual SE = **5.680** on **369** df, AIC = **2438.4**, BIC = **2497.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +433.7557 | 867.0902 | ±1734.1804 | +0.500 | 0.6169 |  |
| Education: graduate level (vs college) | +0.7675 | 0.6204 | ±1.2408 | +1.237 | 0.2161 |  |
| Education: high school or below (vs college) | -1.1292 | 1.2010 | ±2.4021 | -0.940 | 0.3471 |  |
| **Site: UCSD (vs UAB)** | **+4.5481** | 0.7846 | ±1.5692 | **+5.797** | **6.77e-09** | *** |
| Site: UW (vs UAB) | -0.8126 | 0.7634 | ±1.5268 | -1.064 | 0.2871 |  |
| Season: spring (vs autumn) | -0.9598 | 0.8416 | ±1.6831 | -1.140 | 0.2541 |  |
| **Season: summer (vs autumn)** | **+4.0041** | 0.9259 | ±1.8517 | **+4.325** | **1.53e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9805** | 0.8965 | ±1.7929 | **-4.440** | **8.99e-06** | *** |
| Age (years) | -0.0369 | 0.0264 | ±0.0528 | -1.399 | 0.1619 |  |
| BMI (kg/m2) | -0.0380 | 0.0408 | ±0.0817 | -0.930 | 0.3524 |  |
| Hypertension | +0.4147 | 0.6949 | ±1.3898 | +0.597 | 0.5507 |  |
| High cholesterol | -0.4413 | 0.6422 | ±1.2844 | -0.687 | 0.4920 |  |
| Kidney disease | -1.1366 | 1.2852 | ±2.5704 | -0.884 | 0.3765 |  |
| Circulatory disease | -0.4040 | 0.9512 | ±1.9024 | -0.425 | 0.6710 |  |
| Avg. daily time 54-250 (%) | -3.8626 | 8.6708 | ±17.3417 | -0.445 | 0.6560 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **384**, R² = **0.3092**, Adj R² = **0.2830**, F-statistic = **11.80** (p = **1.31e-22**), Residual SE = **5.678** on **369** df, AIC = **2438.2**, BIC = **2497.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.2805** | 2.0976 | ±4.1951 | **+22.541** | **1.66e-112** | *** |
| Education: graduate level (vs college) | +0.7647 | 0.6179 | ±1.2357 | +1.238 | 0.2159 |  |
| Education: high school or below (vs college) | -1.1384 | 1.2004 | ±2.4008 | -0.948 | 0.3429 |  |
| **Site: UCSD (vs UAB)** | **+4.5175** | 0.7801 | ±1.5602 | **+5.791** | **7.01e-09** | *** |
| Site: UW (vs UAB) | -0.8312 | 0.7634 | ±1.5267 | -1.089 | 0.2762 |  |
| Season: spring (vs autumn) | -0.9880 | 0.8314 | ±1.6627 | -1.188 | 0.2347 |  |
| **Season: summer (vs autumn)** | **+3.9319** | 0.9210 | ±1.8420 | **+4.269** | **1.96e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0042** | 0.8942 | ±1.7883 | **-4.478** | **7.53e-06** | *** |
| Age (years) | -0.0368 | 0.0262 | ±0.0524 | -1.406 | 0.1598 |  |
| BMI (kg/m2) | -0.0353 | 0.0407 | ±0.0814 | -0.867 | 0.3859 |  |
| Hypertension | +0.4117 | 0.6948 | ±1.3895 | +0.593 | 0.5534 |  |
| High cholesterol | -0.4362 | 0.6425 | ±1.2850 | -0.679 | 0.4972 |  |
| Kidney disease | -1.2385 | 1.2785 | ±2.5569 | -0.969 | 0.3327 |  |
| Circulatory disease | -0.3650 | 0.9467 | ±1.8934 | -0.386 | 0.6998 |  |
| Time 181-250, pooled (%) | +0.7356 | 1.0392 | ±2.0785 | +0.708 | 0.4790 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **384**, R² = **0.3109**, Adj R² = **0.2847**, F-statistic = **11.89** (p = **8.78e-23**), Residual SE = **5.672** on **369** df, AIC = **2437.3**, BIC = **2496.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.1219** | 2.1063 | ±4.2127 | **+22.371** | **7.47e-111** | *** |
| Education: graduate level (vs college) | +0.7566 | 0.6183 | ±1.2366 | +1.224 | 0.2211 |  |
| Education: high school or below (vs college) | -1.1014 | 1.2083 | ±2.4165 | -0.912 | 0.3620 |  |
| **Site: UCSD (vs UAB)** | **+4.5296** | 0.7781 | ±1.5561 | **+5.822** | **5.82e-09** | *** |
| Site: UW (vs UAB) | -0.8382 | 0.7624 | ±1.5247 | -1.100 | 0.2715 |  |
| Season: spring (vs autumn) | -1.0200 | 0.8298 | ±1.6596 | -1.229 | 0.2190 |  |
| **Season: summer (vs autumn)** | **+3.9138** | 0.9263 | ±1.8527 | **+4.225** | **2.39e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0161** | 0.8933 | ±1.7866 | **-4.496** | **6.93e-06** | *** |
| Age (years) | -0.0350 | 0.0263 | ±0.0525 | -1.333 | 0.1824 |  |
| BMI (kg/m2) | -0.0361 | 0.0410 | ±0.0820 | -0.881 | 0.3783 |  |
| Hypertension | +0.3991 | 0.6937 | ±1.3874 | +0.575 | 0.5651 |  |
| High cholesterol | -0.4557 | 0.6413 | ±1.2825 | -0.711 | 0.4773 |  |
| Kidney disease | -1.2195 | 1.2732 | ±2.5463 | -0.958 | 0.3381 |  |
| Circulatory disease | -0.3795 | 0.9395 | ±1.8789 | -0.404 | 0.6862 |  |
| Avg. daily time 181-250 (%) | +1.2107 | 1.0935 | ±2.1871 | +1.107 | 0.2682 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **384**, R² = **0.3093**, Adj R² = **0.2831**, F-statistic = **11.80** (p = **1.30e-22**), Residual SE = **5.678** on **369** df, AIC = **2438.2**, BIC = **2497.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.2732** | 2.0980 | ±4.1959 | **+22.533** | **1.97e-112** | *** |
| Education: graduate level (vs college) | +0.7650 | 0.6179 | ±1.2357 | +1.238 | 0.2156 |  |
| Education: high school or below (vs college) | -1.1379 | 1.2004 | ±2.4008 | -0.948 | 0.3432 |  |
| **Site: UCSD (vs UAB)** | **+4.5176** | 0.7801 | ±1.5602 | **+5.791** | **6.99e-09** | *** |
| Site: UW (vs UAB) | -0.8317 | 0.7635 | ±1.5270 | -1.089 | 0.2760 |  |
| Season: spring (vs autumn) | -0.9882 | 0.8313 | ±1.6626 | -1.189 | 0.2345 |  |
| **Season: summer (vs autumn)** | **+3.9312** | 0.9210 | ±1.8420 | **+4.268** | **1.97e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0051** | 0.8943 | ±1.7885 | **-4.479** | **7.51e-06** | *** |
| Age (years) | -0.0368 | 0.0262 | ±0.0524 | -1.405 | 0.1602 |  |
| BMI (kg/m2) | -0.0352 | 0.0407 | ±0.0814 | -0.865 | 0.3868 |  |
| Hypertension | +0.4116 | 0.6947 | ±1.3894 | +0.592 | 0.5535 |  |
| High cholesterol | -0.4368 | 0.6424 | ±1.2848 | -0.680 | 0.4965 |  |
| Kidney disease | -1.2399 | 1.2783 | ±2.5567 | -0.970 | 0.3321 |  |
| Circulatory disease | -0.3650 | 0.9466 | ±1.8932 | -0.386 | 0.6998 |  |
| Time > 180 (%) | +0.7483 | 1.0382 | ±2.0764 | +0.721 | 0.4710 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **384**, R² = **0.3109**, Adj R² = **0.2848**, F-statistic = **11.89** (p = **8.65e-23**), Residual SE = **5.671** on **369** df, AIC = **2437.3**, BIC = **2496.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.1131** | 2.1068 | ±4.2136 | **+22.363** | **9.10e-111** | *** |
| Education: graduate level (vs college) | +0.7573 | 0.6182 | ±1.2364 | +1.225 | 0.2206 |  |
| Education: high school or below (vs college) | -1.1002 | 1.2084 | ±2.4168 | -0.910 | 0.3626 |  |
| **Site: UCSD (vs UAB)** | **+4.5298** | 0.7780 | ±1.5560 | **+5.822** | **5.80e-09** | *** |
| Site: UW (vs UAB) | -0.8391 | 0.7625 | ±1.5249 | -1.101 | 0.2711 |  |
| Season: spring (vs autumn) | -1.0205 | 0.8297 | ±1.6595 | -1.230 | 0.2187 |  |
| **Season: summer (vs autumn)** | **+3.9131** | 0.9264 | ±1.8528 | **+4.224** | **2.40e-05** | *** |
| **Season: winter (vs autumn)** | **-4.0175** | 0.8934 | ±1.7868 | **-4.497** | **6.89e-06** | *** |
| Age (years) | -0.0349 | 0.0263 | ±0.0525 | -1.331 | 0.1833 |  |
| BMI (kg/m2) | -0.0360 | 0.0410 | ±0.0820 | -0.879 | 0.3793 |  |
| Hypertension | +0.3991 | 0.6937 | ±1.3874 | +0.575 | 0.5650 |  |
| High cholesterol | -0.4571 | 0.6412 | ±1.2824 | -0.713 | 0.4760 |  |
| Kidney disease | -1.2199 | 1.2731 | ±2.5461 | -0.958 | 0.3379 |  |
| Circulatory disease | -0.3796 | 0.9394 | ±1.8787 | -0.404 | 0.6862 |  |
| Avg. daily time > 180 (%) | +1.2231 | 1.0917 | ±2.1834 | +1.120 | 0.2626 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 384)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **384**, R² = **0.3097**, Adj R² = **0.2836**, F-statistic = **11.83** (p = **1.16e-22**), Residual SE = **5.676** on **369** df, AIC = **2437.9**, BIC = **2497.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.7877** | 2.1214 | ±4.2429 | **+22.526** | **2.30e-112** | *** |
| Education: graduate level (vs college) | +0.7423 | 0.6235 | ±1.2471 | +1.190 | 0.2339 |  |
| Education: high school or below (vs college) | -1.1545 | 1.1920 | ±2.3840 | -0.968 | 0.3328 |  |
| **Site: UCSD (vs UAB)** | **+4.4876** | 0.7823 | ±1.5646 | **+5.736** | **9.68e-09** | *** |
| Site: UW (vs UAB) | -0.8076 | 0.7587 | ±1.5174 | -1.064 | 0.2871 |  |
| Season: spring (vs autumn) | -0.9446 | 0.8334 | ±1.6668 | -1.133 | 0.2570 |  |
| **Season: summer (vs autumn)** | **+3.9760** | 0.9101 | ±1.8201 | **+4.369** | **1.25e-05** | *** |
| **Season: winter (vs autumn)** | **-3.9195** | 0.8939 | ±1.7878 | **-4.385** | **1.16e-05** | *** |
| Age (years) | -0.0423 | 0.0268 | ±0.0536 | -1.576 | 0.1151 |  |
| BMI (kg/m2) | -0.0334 | 0.0395 | ±0.0791 | -0.844 | 0.3984 |  |
| Hypertension | +0.4650 | 0.6969 | ±1.3939 | +0.667 | 0.5047 |  |
| High cholesterol | -0.4136 | 0.6395 | ±1.2790 | -0.647 | 0.5178 |  |
| Kidney disease | -1.1291 | 1.2729 | ±2.5458 | -0.887 | 0.3751 |  |
| Circulatory disease | -0.3596 | 0.9513 | ±1.9027 | -0.378 | 0.7054 |  |
| Nocturnal time > 180 (%) | -0.7879 | 0.8696 | ±1.7392 | -0.906 | 0.3649 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 384; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **384**, R² = **0.0369**, Adj R² = **0.0030**, F-statistic = **1.09** (p = **0.3660**), Residual SE = **14.230** on **370** df, AIC = **3142.8**, BIC = **3198.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.1843** | 6.0667 | ±12.1334 | **+20.635** | **1.34e-94** | *** |
| Education: graduate level (vs college) | -0.0316 | 1.5544 | ±3.1088 | -0.020 | 0.9838 |  |
| Education: high school or below (vs college) | +4.3297 | 2.9401 | ±5.8802 | +1.473 | 0.1408 |  |
| Site: UCSD (vs UAB) | -0.3830 | 1.9948 | ±3.9896 | -0.192 | 0.8477 |  |
| Site: UW (vs UAB) | +0.8781 | 1.9828 | ±3.9656 | +0.443 | 0.6579 |  |
| Season: spring (vs autumn) | +1.1125 | 2.1626 | ±4.3252 | +0.514 | 0.6069 |  |
| Season: summer (vs autumn) | +2.0181 | 2.2023 | ±4.4045 | +0.916 | 0.3595 |  |
| Season: winter (vs autumn) | +3.3276 | 2.1687 | ±4.3374 | +1.534 | 0.1249 |  |
| Age (years) | -0.0899 | 0.0752 | ±0.1504 | -1.196 | 0.2319 |  |
| BMI (kg/m2) | +0.1555 | 0.1078 | ±0.2155 | +1.443 | 0.1489 |  |
| Hypertension | +1.7134 | 1.7861 | ±3.5722 | +0.959 | 0.3374 |  |
| High cholesterol | +1.1137 | 1.6851 | ±3.3701 | +0.661 | 0.5087 |  |
| Kidney disease | -1.1039 | 2.3550 | ±4.7101 | -0.469 | 0.6393 |  |
| Circulatory disease | -0.8413 | 2.3008 | ±4.6016 | -0.366 | 0.7146 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **384**, R² = **0.0461**, Adj R² = **0.0099**, F-statistic = **1.27** (p = **0.2206**), Residual SE = **14.181** on **369** df, AIC = **3141.1**, BIC = **3200.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+150.9357** | 16.1466 | ±32.2933 | **+9.348** | **8.95e-21** | *** |
| Education: graduate level (vs college) | -0.0556 | 1.5617 | ±3.1233 | -0.036 | 0.9716 |  |
| Education: high school or below (vs college) | +4.5000 | 2.9369 | ±5.8738 | +1.532 | 0.1255 |  |
| Site: UCSD (vs UAB) | -0.4016 | 1.9930 | ±3.9861 | -0.202 | 0.8403 |  |
| Site: UW (vs UAB) | +0.7635 | 1.9906 | ±3.9812 | +0.384 | 0.7013 |  |
| Season: spring (vs autumn) | +0.4700 | 2.2050 | ±4.4100 | +0.213 | 0.8312 |  |
| Season: summer (vs autumn) | +2.3174 | 2.1889 | ±4.3777 | +1.059 | 0.2897 |  |
| Season: winter (vs autumn) | +3.1348 | 2.1884 | ±4.3769 | +1.432 | 0.1520 |  |
| Age (years) | -0.0745 | 0.0762 | ±0.1524 | -0.977 | 0.3285 |  |
| BMI (kg/m2) | +0.1737 | 0.1047 | ±0.2094 | +1.659 | 0.0971 | . |
| Hypertension | +1.9778 | 1.7680 | ±3.5360 | +1.119 | 0.2633 |  |
| High cholesterol | +1.7354 | 1.7609 | ±3.5218 | +0.986 | 0.3244 |  |
| Kidney disease | -1.5212 | 2.4366 | ±4.8731 | -0.624 | 0.5324 |  |
| Circulatory disease | -1.2655 | 2.3933 | ±4.7867 | -0.529 | 0.5970 |  |
| HbA1c (%) | -4.9252 | 2.8750 | ±5.7499 | -1.713 | 0.0867 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **384**, R² = **0.0482**, Adj R² = **0.0121**, F-statistic = **1.33** (p = **0.1844**), Residual SE = **14.166** on **369** df, AIC = **3140.3**, BIC = **3199.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+148.2311** | 13.0731 | ±26.1462 | **+11.339** | **8.45e-30** | *** |
| Education: graduate level (vs college) | +0.0461 | 1.5414 | ±3.0827 | +0.030 | 0.9761 |  |
| Education: high school or below (vs college) | +4.2063 | 2.9264 | ±5.8528 | +1.437 | 0.1506 |  |
| Site: UCSD (vs UAB) | -0.1741 | 1.9918 | ±3.9836 | -0.087 | 0.9304 |  |
| Site: UW (vs UAB) | +1.1244 | 2.0007 | ±4.0014 | +0.562 | 0.5741 |  |
| Season: spring (vs autumn) | +0.9242 | 2.1421 | ±4.2842 | +0.431 | 0.6661 |  |
| Season: summer (vs autumn) | +2.0383 | 2.2137 | ±4.4275 | +0.921 | 0.3572 |  |
| Season: winter (vs autumn) | +3.2408 | 2.1923 | ±4.3845 | +1.478 | 0.1393 |  |
| Age (years) | -0.0953 | 0.0753 | ±0.1505 | -1.266 | 0.2054 |  |
| BMI (kg/m2) | +0.1716 | 0.1064 | ±0.2129 | +1.612 | 0.1069 |  |
| Hypertension | +1.9494 | 1.7633 | ±3.5267 | +1.105 | 0.2690 |  |
| High cholesterol | +0.9720 | 1.6867 | ±3.3734 | +0.576 | 0.5644 |  |
| Kidney disease | -0.8728 | 2.4019 | ±4.8038 | -0.363 | 0.7163 |  |
| Circulatory disease | -0.9276 | 2.3394 | ±4.6787 | -0.397 | 0.6917 |  |
| **Mean glucose (mg/dL)** | **-0.2041** | 0.1017 | ±0.2034 | **-2.006** | **0.0448** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **384**, R² = **0.0482**, Adj R² = **0.0121**, F-statistic = **1.33** (p = **0.1844**), Residual SE = **14.166** on **369** df, AIC = **3140.3**, BIC = **3199.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+176.4700** | 26.3852 | ±52.7703 | **+6.688** | **2.26e-11** | *** |
| Education: graduate level (vs college) | +0.0461 | 1.5414 | ±3.0827 | +0.030 | 0.9761 |  |
| Education: high school or below (vs college) | +4.2063 | 2.9264 | ±5.8528 | +1.437 | 0.1506 |  |
| Site: UCSD (vs UAB) | -0.1741 | 1.9918 | ±3.9836 | -0.087 | 0.9304 |  |
| Site: UW (vs UAB) | +1.1244 | 2.0007 | ±4.0014 | +0.562 | 0.5741 |  |
| Season: spring (vs autumn) | +0.9242 | 2.1421 | ±4.2842 | +0.431 | 0.6661 |  |
| Season: summer (vs autumn) | +2.0383 | 2.2137 | ±4.4275 | +0.921 | 0.3572 |  |
| Season: winter (vs autumn) | +3.2408 | 2.1923 | ±4.3845 | +1.478 | 0.1393 |  |
| Age (years) | -0.0953 | 0.0753 | ±0.1505 | -1.266 | 0.2054 |  |
| BMI (kg/m2) | +0.1716 | 0.1064 | ±0.2129 | +1.612 | 0.1069 |  |
| Hypertension | +1.9494 | 1.7633 | ±3.5267 | +1.105 | 0.2690 |  |
| High cholesterol | +0.9720 | 1.6867 | ±3.3734 | +0.576 | 0.5644 |  |
| Kidney disease | -0.8728 | 2.4019 | ±4.8038 | -0.363 | 0.7163 |  |
| Circulatory disease | -0.9276 | 2.3394 | ±4.6787 | -0.397 | 0.6917 |  |
| **GMI (%)** | **-8.5314** | 4.2525 | ±8.5051 | **-2.006** | **0.0448** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **384**, R² = **0.0410**, Adj R² = **0.0046**, F-statistic = **1.13** (p = **0.3316**), Residual SE = **14.219** on **369** df, AIC = **3143.2**, BIC = **3202.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+136.5828** | 10.8933 | ±21.7867 | **+12.538** | **4.61e-36** | *** |
| Education: graduate level (vs college) | -0.1113 | 1.5648 | ±3.1297 | -0.071 | 0.9433 |  |
| Education: high school or below (vs college) | +4.1695 | 2.9510 | ±5.9019 | +1.413 | 0.1577 |  |
| Site: UCSD (vs UAB) | -0.1323 | 2.0205 | ±4.0410 | -0.065 | 0.9478 |  |
| Site: UW (vs UAB) | +1.0913 | 2.0127 | ±4.0253 | +0.542 | 0.5877 |  |
| Season: spring (vs autumn) | +1.0947 | 2.1606 | ±4.3211 | +0.507 | 0.6124 |  |
| Season: summer (vs autumn) | +2.0883 | 2.2192 | ±4.4384 | +0.941 | 0.3467 |  |
| Season: winter (vs autumn) | +3.3301 | 2.1845 | ±4.3689 | +1.524 | 0.1274 |  |
| Age (years) | -0.1021 | 0.0764 | ±0.1529 | -1.336 | 0.1815 |  |
| BMI (kg/m2) | +0.1783 | 0.1045 | ±0.2089 | +1.706 | 0.0879 | . |
| Hypertension | +1.7994 | 1.7797 | ±3.5594 | +1.011 | 0.3120 |  |
| High cholesterol | +1.0993 | 1.6889 | ±3.3778 | +0.651 | 0.5151 |  |
| Kidney disease | -1.1716 | 2.3897 | ±4.7794 | -0.490 | 0.6239 |  |
| Circulatory disease | -0.9275 | 2.3253 | ±4.6505 | -0.399 | 0.6900 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0997 | 0.0771 | ±0.1542 | -1.293 | 0.1960 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **384**, R² = **0.0418**, Adj R² = **0.0055**, F-statistic = **1.15** (p = **0.3125**), Residual SE = **14.213** on **369** df, AIC = **3142.8**, BIC = **3202.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.6598** | 8.0950 | ±16.1900 | **+16.388** | **2.33e-60** | *** |
| Education: graduate level (vs college) | -0.1524 | 1.5602 | ±3.1205 | -0.098 | 0.9222 |  |
| Education: high school or below (vs college) | +4.3596 | 2.9683 | ±5.9365 | +1.469 | 0.1419 |  |
| Site: UCSD (vs UAB) | -0.6265 | 1.9844 | ±3.9687 | -0.316 | 0.7522 |  |
| Site: UW (vs UAB) | +0.7287 | 1.9796 | ±3.9592 | +0.368 | 0.7128 |  |
| Season: spring (vs autumn) | +1.3286 | 2.1920 | ±4.3839 | +0.606 | 0.5444 |  |
| Season: summer (vs autumn) | +2.1614 | 2.2076 | ±4.4151 | +0.979 | 0.3275 |  |
| Season: winter (vs autumn) | +3.5571 | 2.1807 | ±4.3613 | +1.631 | 0.1028 |  |
| Age (years) | -0.0890 | 0.0755 | ±0.1510 | -1.179 | 0.2384 |  |
| BMI (kg/m2) | +0.1620 | 0.1068 | ±0.2136 | +1.516 | 0.1294 |  |
| Hypertension | +1.7210 | 1.7807 | ±3.5613 | +0.967 | 0.3338 |  |
| High cholesterol | +1.0071 | 1.6791 | ±3.3582 | +0.600 | 0.5486 |  |
| Kidney disease | -0.9156 | 2.4266 | ±4.8532 | -0.377 | 0.7059 |  |
| Circulatory disease | -0.7514 | 2.2984 | ±4.5967 | -0.327 | 0.7437 |  |
| Glucose SD, pooled (mg/dL) | -0.4576 | 0.3493 | ±0.6985 | -1.310 | 0.1901 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **384**, R² = **0.0428**, Adj R² = **0.0065**, F-statistic = **1.18** (p = **0.2888**), Residual SE = **14.206** on **369** df, AIC = **3142.4**, BIC = **3201.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+132.5422** | 7.6899 | ±15.3797 | **+17.236** | **1.43e-66** | *** |
| Education: graduate level (vs college) | -0.1816 | 1.5645 | ±3.1291 | -0.116 | 0.9076 |  |
| Education: high school or below (vs college) | +4.2876 | 2.9571 | ±5.9141 | +1.450 | 0.1471 |  |
| Site: UCSD (vs UAB) | -0.6657 | 1.9827 | ±3.9654 | -0.336 | 0.7371 |  |
| Site: UW (vs UAB) | +0.7068 | 1.9778 | ±3.9555 | +0.357 | 0.7208 |  |
| Season: spring (vs autumn) | +1.3131 | 2.1872 | ±4.3745 | +0.600 | 0.5483 |  |
| Season: summer (vs autumn) | +2.1260 | 2.2069 | ±4.4139 | +0.963 | 0.3354 |  |
| Season: winter (vs autumn) | +3.4706 | 2.1762 | ±4.3523 | +1.595 | 0.1108 |  |
| Age (years) | -0.0891 | 0.0756 | ±0.1512 | -1.179 | 0.2383 |  |
| BMI (kg/m2) | +0.1689 | 0.1053 | ±0.2106 | +1.604 | 0.1087 |  |
| Hypertension | +1.6727 | 1.7829 | ±3.5658 | +0.938 | 0.3482 |  |
| High cholesterol | +1.0236 | 1.6768 | ±3.3537 | +0.610 | 0.5416 |  |
| Kidney disease | -0.8925 | 2.4058 | ±4.8117 | -0.371 | 0.7107 |  |
| Circulatory disease | -0.8169 | 2.2739 | ±4.5478 | -0.359 | 0.7194 |  |
| Avg. daily SD (mg/dL) | -0.4975 | 0.3552 | ±0.7103 | -1.401 | 0.1613 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **384**, R² = **0.0372**, Adj R² = **0.0007**, F-statistic = **1.02** (p = **0.4332**), Residual SE = **14.247** on **369** df, AIC = **3144.7**, BIC = **3203.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.0580** | 8.0539 | ±16.1078 | **+15.776** | **4.56e-56** | *** |
| Education: graduate level (vs college) | -0.0681 | 1.5610 | ±3.1219 | -0.044 | 0.9652 |  |
| Education: high school or below (vs college) | +4.3472 | 2.9486 | ±5.8972 | +1.474 | 0.1404 |  |
| Site: UCSD (vs UAB) | -0.4598 | 2.0130 | ±4.0260 | -0.228 | 0.8193 |  |
| Site: UW (vs UAB) | +0.8204 | 2.0022 | ±4.0044 | +0.410 | 0.6820 |  |
| Season: spring (vs autumn) | +1.1826 | 2.1975 | ±4.3950 | +0.538 | 0.5905 |  |
| Season: summer (vs autumn) | +2.0573 | 2.2036 | ±4.4073 | +0.934 | 0.3505 |  |
| Season: winter (vs autumn) | +3.3927 | 2.1857 | ±4.3715 | +1.552 | 0.1206 |  |
| Age (years) | -0.0893 | 0.0757 | ±0.1514 | -1.179 | 0.2383 |  |
| BMI (kg/m2) | +0.1559 | 0.1079 | ±0.2158 | +1.445 | 0.1486 |  |
| Hypertension | +1.6960 | 1.7878 | ±3.5756 | +0.949 | 0.3428 |  |
| High cholesterol | +1.0965 | 1.6857 | ±3.3715 | +0.650 | 0.5154 |  |
| Kidney disease | -1.0787 | 2.3749 | ±4.7498 | -0.454 | 0.6497 |  |
| Circulatory disease | -0.8100 | 2.3143 | ±4.6287 | -0.350 | 0.7263 |  |
| CV (%) | -0.1290 | 0.3884 | ±0.7767 | -0.332 | 0.7397 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **384**, R² = **0.0375**, Adj R² = **0.0010**, F-statistic = **1.03** (p = **0.4258**), Residual SE = **14.245** on **369** df, AIC = **3144.6**, BIC = **3203.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.7062** | 8.4894 | ±16.9787 | **+14.454** | **2.36e-47** | *** |
| Education: graduate level (vs college) | -0.0869 | 1.5602 | ±3.1204 | -0.056 | 0.9556 |  |
| Education: high school or below (vs college) | +4.3539 | 2.9496 | ±5.8993 | +1.476 | 0.1399 |  |
| Site: UCSD (vs UAB) | -0.4680 | 2.0085 | ±4.0169 | -0.233 | 0.8158 |  |
| Site: UW (vs UAB) | +0.8174 | 1.9983 | ±3.9966 | +0.409 | 0.6825 |  |
| Season: spring (vs autumn) | +1.2127 | 2.2002 | ±4.4004 | +0.551 | 0.5815 |  |
| Season: summer (vs autumn) | +2.0647 | 2.2045 | ±4.4090 | +0.937 | 0.3490 |  |
| Season: winter (vs autumn) | +3.4138 | 2.1863 | ±4.3726 | +1.561 | 0.1184 |  |
| Age (years) | -0.0894 | 0.0756 | ±0.1511 | -1.184 | 0.2365 |  |
| BMI (kg/m2) | +0.1559 | 0.1079 | ±0.2158 | +1.445 | 0.1485 |  |
| Hypertension | +1.7037 | 1.7882 | ±3.5763 | +0.953 | 0.3407 |  |
| High cholesterol | +1.0889 | 1.6839 | ±3.3678 | +0.647 | 0.5179 |  |
| Kidney disease | -1.0885 | 2.3819 | ±4.7638 | -0.457 | 0.6477 |  |
| Circulatory disease | -0.8031 | 2.3146 | ±4.6292 | -0.347 | 0.7286 |  |
| Mean / SD ratio | +0.3543 | 0.8040 | ±1.6079 | +0.441 | 0.6594 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **384**, R² = **0.0378**, Adj R² = **0.0013**, F-statistic = **1.03** (p = **0.4173**), Residual SE = **14.243** on **369** df, AIC = **3144.5**, BIC = **3203.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.3474** | 8.5238 | ±17.0475 | **+14.354** | **1.01e-46** | *** |
| Education: graduate level (vs college) | -0.1078 | 1.5635 | ±3.1270 | -0.069 | 0.9450 |  |
| Education: high school or below (vs college) | +4.3321 | 2.9515 | ±5.9029 | +1.468 | 0.1422 |  |
| Site: UCSD (vs UAB) | -0.4948 | 2.0053 | ±4.0105 | -0.247 | 0.8051 |  |
| Site: UW (vs UAB) | +0.8083 | 1.9947 | ±3.9895 | +0.405 | 0.6853 |  |
| Season: spring (vs autumn) | +1.2329 | 2.2025 | ±4.4049 | +0.560 | 0.5756 |  |
| Season: summer (vs autumn) | +2.0660 | 2.2079 | ±4.4157 | +0.936 | 0.3494 |  |
| Season: winter (vs autumn) | +3.4032 | 2.1831 | ±4.3662 | +1.559 | 0.1190 |  |
| Age (years) | -0.0893 | 0.0757 | ±0.1514 | -1.179 | 0.2383 |  |
| BMI (kg/m2) | +0.1596 | 0.1072 | ±0.2144 | +1.489 | 0.1364 |  |
| Hypertension | +1.6756 | 1.7932 | ±3.5865 | +0.934 | 0.3501 |  |
| High cholesterol | +1.0968 | 1.6844 | ±3.3687 | +0.651 | 0.5149 |  |
| Kidney disease | -1.0672 | 2.3694 | ±4.7388 | -0.450 | 0.6524 |  |
| Circulatory disease | -0.8200 | 2.2971 | ±4.5942 | -0.357 | 0.7211 |  |
| Avg. daily mean/SD | +0.3482 | 0.6683 | ±1.3367 | +0.521 | 0.6024 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **384**, R² = **0.0410**, Adj R² = **0.0046**, F-statistic = **1.13** (p = **0.3326**), Residual SE = **14.219** on **369** df, AIC = **3143.2**, BIC = **3202.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+118.6917** | 8.2137 | ±16.4274 | **+14.450** | **2.49e-47** | *** |
| Education: graduate level (vs college) | -0.0797 | 1.5567 | ±3.1134 | -0.051 | 0.9592 |  |
| Education: high school or below (vs college) | +4.0607 | 2.9309 | ±5.8618 | +1.385 | 0.1659 |  |
| Site: UCSD (vs UAB) | -0.1974 | 1.9886 | ±3.9772 | -0.099 | 0.9209 |  |
| Site: UW (vs UAB) | +1.1770 | 1.9710 | ±3.9420 | +0.597 | 0.5504 |  |
| Season: spring (vs autumn) | +0.9849 | 2.1765 | ±4.3530 | +0.453 | 0.6509 |  |
| Season: summer (vs autumn) | +2.0320 | 2.1838 | ±4.3676 | +0.930 | 0.3521 |  |
| Season: winter (vs autumn) | +3.1936 | 2.1584 | ±4.3169 | +1.480 | 0.1390 |  |
| Age (years) | -0.0786 | 0.0756 | ±0.1512 | -1.040 | 0.2982 |  |
| BMI (kg/m2) | +0.1652 | 0.1082 | ±0.2163 | +1.527 | 0.1268 |  |
| Hypertension | +1.7885 | 1.8096 | ±3.6193 | +0.988 | 0.3230 |  |
| High cholesterol | +0.9999 | 1.7035 | ±3.4071 | +0.587 | 0.5572 |  |
| Kidney disease | -1.3115 | 2.3088 | ±4.6176 | -0.568 | 0.5700 |  |
| Circulatory disease | -0.8399 | 2.3048 | ±4.6095 | -0.364 | 0.7156 |  |
| MAG (mg/dL/h) | +0.1615 | 0.1441 | ±0.2883 | +1.120 | 0.2626 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **384**, R² = **0.0374**, Adj R² = **0.0009**, F-statistic = **1.02** (p = **0.4274**), Residual SE = **14.246** on **369** df, AIC = **3144.6**, BIC = **3203.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.7944** | 8.5262 | ±17.0523 | **+14.988** | **8.73e-51** | *** |
| Education: graduate level (vs college) | -0.0429 | 1.5592 | ±3.1185 | -0.027 | 0.9781 |  |
| Education: high school or below (vs college) | +4.3301 | 2.9552 | ±5.9104 | +1.465 | 0.1429 |  |
| Site: UCSD (vs UAB) | -0.4635 | 1.9920 | ±3.9840 | -0.233 | 0.8160 |  |
| Site: UW (vs UAB) | +0.8204 | 1.9913 | ±3.9825 | +0.412 | 0.6804 |  |
| Season: spring (vs autumn) | +1.1779 | 2.2023 | ±4.4045 | +0.535 | 0.5927 |  |
| Season: summer (vs autumn) | +2.0432 | 2.2157 | ±4.4314 | +0.922 | 0.3564 |  |
| Season: winter (vs autumn) | +3.3895 | 2.1867 | ±4.3734 | +1.550 | 0.1211 |  |
| Age (years) | -0.0905 | 0.0754 | ±0.1508 | -1.200 | 0.2302 |  |
| BMI (kg/m2) | +0.1518 | 0.1096 | ±0.2193 | +1.385 | 0.1662 |  |
| Hypertension | +1.6764 | 1.8034 | ±3.6067 | +0.930 | 0.3526 |  |
| High cholesterol | +1.1205 | 1.6935 | ±3.3871 | +0.662 | 0.5082 |  |
| Kidney disease | -1.0670 | 2.3662 | ±4.7324 | -0.451 | 0.6520 |  |
| Circulatory disease | -0.8189 | 2.3056 | ±4.6112 | -0.355 | 0.7225 |  |
| Avg. daily range (mg/dL) | -0.0308 | 0.0789 | ±0.1577 | -0.390 | 0.6964 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **384**, R² = **0.0379**, Adj R² = **0.0014**, F-statistic = **1.04** (p = **0.4146**), Residual SE = **14.242** on **369** df, AIC = **3144.4**, BIC = **3203.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.3023** | 6.2995 | ±12.5990 | **+20.050** | **2.03e-89** | *** |
| Education: graduate level (vs college) | +0.0094 | 1.5609 | ±3.1218 | +0.006 | 0.9952 |  |
| Education: high school or below (vs college) | +4.4346 | 2.9431 | ±5.8861 | +1.507 | 0.1319 |  |
| Site: UCSD (vs UAB) | -0.4126 | 1.9987 | ±3.9974 | -0.206 | 0.8364 |  |
| Site: UW (vs UAB) | +0.9257 | 1.9892 | ±3.9784 | +0.465 | 0.6417 |  |
| Season: spring (vs autumn) | +1.2003 | 2.1911 | ±4.3823 | +0.548 | 0.5838 |  |
| Season: summer (vs autumn) | +2.1142 | 2.2123 | ±4.4246 | +0.956 | 0.3392 |  |
| Season: winter (vs autumn) | +3.4631 | 2.1990 | ±4.3980 | +1.575 | 0.1153 |  |
| Age (years) | -0.0891 | 0.0751 | ±0.1502 | -1.187 | 0.2353 |  |
| BMI (kg/m2) | +0.1559 | 0.1080 | ±0.2161 | +1.443 | 0.1490 |  |
| Hypertension | +1.7766 | 1.8058 | ±3.6117 | +0.984 | 0.3252 |  |
| High cholesterol | +1.1331 | 1.6892 | ±3.3785 | +0.671 | 0.5024 |  |
| Kidney disease | -1.2164 | 2.4176 | ±4.8351 | -0.503 | 0.6149 |  |
| Circulatory disease | -0.7569 | 2.3031 | ±4.6062 | -0.329 | 0.7424 |  |
| SD of daily means (mg/dL) | -0.2606 | 0.3944 | ±0.7888 | -0.661 | 0.5087 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **384**, R² = **0.0371**, Adj R² = **0.0005**, F-statistic = **1.01** (p = **0.4373**), Residual SE = **14.248** on **369** df, AIC = **3144.7**, BIC = **3204.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +58.6111 | 265.8494 | ±531.6988 | +0.220 | 0.8255 |  |
| Education: graduate level (vs college) | -0.0324 | 1.5589 | ±3.1178 | -0.021 | 0.9834 |  |
| Education: high school or below (vs college) | +4.3354 | 2.9494 | ±5.8987 | +1.470 | 0.1416 |  |
| Site: UCSD (vs UAB) | -0.4188 | 2.0060 | ±4.0120 | -0.209 | 0.8346 |  |
| Site: UW (vs UAB) | +0.8527 | 1.9944 | ±3.9889 | +0.428 | 0.6690 |  |
| Season: spring (vs autumn) | +1.1394 | 2.1831 | ±4.3661 | +0.522 | 0.6017 |  |
| Season: summer (vs autumn) | +2.0574 | 2.2267 | ±4.4533 | +0.924 | 0.3555 |  |
| Season: winter (vs autumn) | +3.3658 | 2.1886 | ±4.3773 | +1.538 | 0.1241 |  |
| Age (years) | -0.0906 | 0.0753 | ±0.1507 | -1.203 | 0.2292 |  |
| BMI (kg/m2) | +0.1538 | 0.1094 | ±0.2188 | +1.406 | 0.1599 |  |
| Hypertension | +1.7116 | 1.7897 | ±3.5794 | +0.956 | 0.3389 |  |
| High cholesterol | +1.1331 | 1.7036 | ±3.4071 | +0.665 | 0.5060 |  |
| Kidney disease | -1.0709 | 2.3684 | ±4.7368 | -0.452 | 0.6512 |  |
| Circulatory disease | -0.8264 | 2.3128 | ±4.6256 | -0.357 | 0.7209 |  |
| Time in range 70-180, pooled (%) | +0.6695 | 2.6679 | ±5.3358 | +0.251 | 0.8018 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **384**, R² = **0.0372**, Adj R² = **0.0007**, F-statistic = **1.02** (p = **0.4327**), Residual SE = **14.247** on **369** df, AIC = **3144.7**, BIC = **3203.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +37.0839 | 265.3609 | ±530.7218 | +0.140 | 0.8889 |  |
| Education: graduate level (vs college) | -0.0329 | 1.5586 | ±3.1172 | -0.021 | 0.9831 |  |
| Education: high school or below (vs college) | +4.3227 | 2.9511 | ±5.9021 | +1.465 | 0.1430 |  |
| Site: UCSD (vs UAB) | -0.4174 | 1.9997 | ±3.9993 | -0.209 | 0.8347 |  |
| Site: UW (vs UAB) | +0.8692 | 1.9899 | ±3.9798 | +0.437 | 0.6623 |  |
| Season: spring (vs autumn) | +1.1393 | 2.1794 | ±4.3588 | +0.523 | 0.6011 |  |
| Season: summer (vs autumn) | +2.0356 | 2.2178 | ±4.4356 | +0.918 | 0.3587 |  |
| Season: winter (vs autumn) | +3.3679 | 2.1884 | ±4.3767 | +1.539 | 0.1238 |  |
| Age (years) | -0.0918 | 0.0754 | ±0.1509 | -1.216 | 0.2238 |  |
| BMI (kg/m2) | +0.1546 | 0.1083 | ±0.2166 | +1.427 | 0.1534 |  |
| Hypertension | +1.6881 | 1.7971 | ±3.5941 | +0.939 | 0.3475 |  |
| High cholesterol | +1.1473 | 1.7098 | ±3.4195 | +0.671 | 0.5022 |  |
| Kidney disease | -1.0940 | 2.3823 | ±4.7646 | -0.459 | 0.6461 |  |
| Circulatory disease | -0.8023 | 2.3176 | ±4.6351 | -0.346 | 0.7292 |  |
| Avg. daily time in range 70-180 (%) | +0.8857 | 2.6634 | ±5.3269 | +0.333 | 0.7395 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.0369**, Adj R² = **0.0004**, F-statistic = **1.01** (p = **0.4425**), Residual SE = **14.250** on **369** df, AIC = **3144.8**, BIC = **3204.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.2080** | 6.0222 | ±12.0443 | **+20.791** | **5.20e-96** | *** |
| Education: graduate level (vs college) | -0.0337 | 1.5544 | ±3.1087 | -0.022 | 0.9827 |  |
| Education: high school or below (vs college) | +4.3270 | 2.9497 | ±5.8993 | +1.467 | 0.1424 |  |
| Site: UCSD (vs UAB) | -0.4066 | 1.9980 | ±3.9960 | -0.204 | 0.8387 |  |
| Site: UW (vs UAB) | +0.8628 | 1.9814 | ±3.9629 | +0.435 | 0.6632 |  |
| Season: spring (vs autumn) | +1.1302 | 2.1833 | ±4.3666 | +0.518 | 0.6047 |  |
| Season: summer (vs autumn) | +2.0269 | 2.2051 | ±4.4102 | +0.919 | 0.3580 |  |
| Season: winter (vs autumn) | +3.3398 | 2.1853 | ±4.3707 | +1.528 | 0.1264 |  |
| Age (years) | -0.0899 | 0.0754 | ±0.1508 | -1.192 | 0.2332 |  |
| BMI (kg/m2) | +0.1555 | 0.1079 | ±0.2158 | +1.441 | 0.1495 |  |
| Hypertension | +1.7223 | 1.7960 | ±3.5920 | +0.959 | 0.3376 |  |
| High cholesterol | +1.1135 | 1.6888 | ±3.3777 | +0.659 | 0.5097 |  |
| Kidney disease | -1.1182 | 2.3716 | ±4.7431 | -0.471 | 0.6373 |  |
| Circulatory disease | -0.8334 | 2.3124 | ±4.6249 | -0.360 | 0.7185 |  |
| Any reading < 54 during wear (0/1) | -0.1361 | 2.0109 | ±4.0217 | -0.068 | 0.9460 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.0390**, Adj R² = **0.0026**, F-statistic = **1.07** (p = **0.3834**), Residual SE = **14.234** on **369** df, AIC = **3144.0**, BIC = **3203.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.8927** | 6.0830 | ±12.1660 | **+20.531** | **1.13e-93** | *** |
| Education: graduate level (vs college) | -0.0215 | 1.5576 | ±3.1152 | -0.014 | 0.9890 |  |
| Education: high school or below (vs college) | +4.4597 | 2.9495 | ±5.8989 | +1.512 | 0.1305 |  |
| Site: UCSD (vs UAB) | -0.1575 | 2.0118 | ±4.0235 | -0.078 | 0.9376 |  |
| Site: UW (vs UAB) | +0.9909 | 1.9856 | ±3.9712 | +0.499 | 0.6177 |  |
| Season: spring (vs autumn) | +1.1430 | 2.1643 | ±4.3286 | +0.528 | 0.5974 |  |
| Season: summer (vs autumn) | +2.0023 | 2.1995 | ±4.3991 | +0.910 | 0.3627 |  |
| Season: winter (vs autumn) | +3.3383 | 2.1673 | ±4.3346 | +1.540 | 0.1235 |  |
| Age (years) | -0.0872 | 0.0750 | ±0.1501 | -1.162 | 0.2452 |  |
| BMI (kg/m2) | +0.1489 | 0.1093 | ±0.2187 | +1.362 | 0.1732 |  |
| Hypertension | +1.5991 | 1.7969 | ±3.5939 | +0.890 | 0.3735 |  |
| High cholesterol | +1.1294 | 1.6907 | ±3.3815 | +0.668 | 0.5042 |  |
| Kidney disease | -0.9787 | 2.3646 | ±4.7292 | -0.414 | 0.6790 |  |
| Circulatory disease | -0.9767 | 2.2764 | ±4.5527 | -0.429 | 0.6679 |  |
| Time < 54 (%) | +13.3508 | 14.3664 | ±28.7328 | +0.929 | 0.3527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **384**, R² = **0.0422**, Adj R² = **0.0059**, F-statistic = **1.16** (p = **0.3029**), Residual SE = **14.210** on **369** df, AIC = **3142.7**, BIC = **3201.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.8045** | 6.0826 | ±12.1652 | **+20.518** | **1.48e-93** | *** |
| Education: graduate level (vs college) | -0.0933 | 1.5569 | ±3.1138 | -0.060 | 0.9522 |  |
| Education: high school or below (vs college) | +4.4149 | 2.9508 | ±5.9015 | +1.496 | 0.1346 |  |
| Site: UCSD (vs UAB) | -0.1796 | 1.9950 | ±3.9899 | -0.090 | 0.9283 |  |
| Site: UW (vs UAB) | +0.9569 | 1.9748 | ±3.9497 | +0.485 | 0.6280 |  |
| Season: spring (vs autumn) | +1.1852 | 2.1551 | ±4.3102 | +0.550 | 0.5824 |  |
| Season: summer (vs autumn) | +2.2503 | 2.1841 | ±4.3682 | +1.030 | 0.3029 |  |
| Season: winter (vs autumn) | +3.3787 | 2.1596 | ±4.3191 | +1.565 | 0.1177 |  |
| Age (years) | -0.0864 | 0.0751 | ±0.1502 | -1.150 | 0.2501 |  |
| BMI (kg/m2) | +0.1492 | 0.1086 | ±0.2172 | +1.374 | 0.1694 |  |
| Hypertension | +1.6038 | 1.7810 | ±3.5620 | +0.901 | 0.3679 |  |
| High cholesterol | +1.1495 | 1.6912 | ±3.3823 | +0.680 | 0.4967 |  |
| Kidney disease | -1.0350 | 2.3622 | ±4.7245 | -0.438 | 0.6613 |  |
| Circulatory disease | -1.1410 | 2.2740 | ±4.5480 | -0.502 | 0.6158 |  |
| Avg. daily time < 54 (%) | +25.4487 | 16.1985 | ±32.3970 | +1.571 | 0.1162 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **384**, R² = **0.0384**, Adj R² = **0.0019**, F-statistic = **1.05** (p = **0.4005**), Residual SE = **14.239** on **369** df, AIC = **3144.2**, BIC = **3203.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.7046** | 6.0550 | ±12.1100 | **+20.595** | **3.02e-94** | *** |
| Education: graduate level (vs college) | +0.0076 | 1.5487 | ±3.0974 | +0.005 | 0.9961 |  |
| Education: high school or below (vs college) | +4.2440 | 2.9588 | ±5.9176 | +1.434 | 0.1515 |  |
| Site: UCSD (vs UAB) | -0.2702 | 2.0027 | ±4.0055 | -0.135 | 0.8927 |  |
| Site: UW (vs UAB) | +1.0109 | 1.9913 | ±3.9827 | +0.508 | 0.6117 |  |
| Season: spring (vs autumn) | +1.0515 | 2.1655 | ±4.3311 | +0.486 | 0.6273 |  |
| Season: summer (vs autumn) | +1.9971 | 2.2049 | ±4.4099 | +0.906 | 0.3651 |  |
| Season: winter (vs autumn) | +3.2314 | 2.1849 | ±4.3698 | +1.479 | 0.1391 |  |
| Age (years) | -0.0905 | 0.0755 | ±0.1511 | -1.198 | 0.2309 |  |
| BMI (kg/m2) | +0.1571 | 0.1079 | ±0.2158 | +1.456 | 0.1455 |  |
| Hypertension | +1.8279 | 1.7873 | ±3.5746 | +1.023 | 0.3064 |  |
| High cholesterol | +0.9926 | 1.7251 | ±3.4502 | +0.575 | 0.5650 |  |
| Kidney disease | -0.9016 | 2.3758 | ±4.7515 | -0.379 | 0.7043 |  |
| Circulatory disease | -0.8539 | 2.3111 | ±4.6223 | -0.369 | 0.7118 |  |
| Time 54-69, pooled (%) | +3.1584 | 4.3095 | ±8.6190 | +0.733 | 0.4636 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **384**, R² = **0.0386**, Adj R² = **0.0021**, F-statistic = **1.06** (p = **0.3959**), Residual SE = **14.237** on **369** df, AIC = **3144.1**, BIC = **3203.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.6996** | 6.0481 | ±12.0961 | **+20.618** | **1.89e-94** | *** |
| Education: graduate level (vs college) | +0.0271 | 1.5458 | ±3.0915 | +0.018 | 0.9860 |  |
| Education: high school or below (vs college) | +4.2235 | 2.9574 | ±5.9147 | +1.428 | 0.1533 |  |
| Site: UCSD (vs UAB) | -0.3151 | 1.9962 | ±3.9924 | -0.158 | 0.8746 |  |
| Site: UW (vs UAB) | +0.9474 | 1.9798 | ±3.9596 | +0.479 | 0.6323 |  |
| Season: spring (vs autumn) | +1.1370 | 2.1598 | ±4.3196 | +0.526 | 0.5986 |  |
| Season: summer (vs autumn) | +2.0751 | 2.2080 | ±4.4160 | +0.940 | 0.3473 |  |
| Season: winter (vs autumn) | +3.2585 | 2.1826 | ±4.3651 | +1.493 | 0.1355 |  |
| Age (years) | -0.0904 | 0.0756 | ±0.1512 | -1.196 | 0.2315 |  |
| BMI (kg/m2) | +0.1568 | 0.1077 | ±0.2155 | +1.455 | 0.1456 |  |
| Hypertension | +1.9088 | 1.7999 | ±3.5997 | +1.061 | 0.2889 |  |
| High cholesterol | +1.0206 | 1.7144 | ±3.4287 | +0.595 | 0.5516 |  |
| Kidney disease | -0.9534 | 2.3577 | ±4.7154 | -0.404 | 0.6859 |  |
| Circulatory disease | -0.8927 | 2.3100 | ±4.6201 | -0.386 | 0.6992 |  |
| Avg. daily time 54-69 (%) | +3.3492 | 4.1073 | ±8.2147 | +0.815 | 0.4148 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **384**, R² = **0.0390**, Adj R² = **0.0026**, F-statistic = **1.07** (p = **0.3834**), Residual SE = **14.234** on **369** df, AIC = **3144.0**, BIC = **3203.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.6014** | 6.0520 | ±12.1041 | **+20.588** | **3.49e-94** | *** |
| Education: graduate level (vs college) | +0.0126 | 1.5493 | ±3.0985 | +0.008 | 0.9935 |  |
| Education: high school or below (vs college) | +4.2713 | 2.9589 | ±5.9178 | +1.444 | 0.1489 |  |
| Site: UCSD (vs UAB) | -0.2065 | 2.0058 | ±4.0117 | -0.103 | 0.9180 |  |
| Site: UW (vs UAB) | +1.0475 | 1.9904 | ±3.9808 | +0.526 | 0.5987 |  |
| Season: spring (vs autumn) | +1.0554 | 2.1622 | ±4.3245 | +0.488 | 0.6255 |  |
| Season: summer (vs autumn) | +1.9918 | 2.2018 | ±4.4036 | +0.905 | 0.3657 |  |
| Season: winter (vs autumn) | +3.2281 | 2.1817 | ±4.3635 | +1.480 | 0.1390 |  |
| Age (years) | -0.0899 | 0.0755 | ±0.1509 | -1.191 | 0.2338 |  |
| BMI (kg/m2) | +0.1555 | 0.1081 | ±0.2162 | +1.439 | 0.1503 |  |
| Hypertension | +1.8064 | 1.7854 | ±3.5707 | +1.012 | 0.3117 |  |
| High cholesterol | +0.9889 | 1.7195 | ±3.4390 | +0.575 | 0.5652 |  |
| Kidney disease | -0.8575 | 2.3755 | ±4.7510 | -0.361 | 0.7181 |  |
| Circulatory disease | -0.8887 | 2.3037 | ±4.6073 | -0.386 | 0.6997 |  |
| Time < 70 (%) | +3.3556 | 3.8211 | ±7.6423 | +0.878 | 0.3799 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **384**, R² = **0.0396**, Adj R² = **0.0032**, F-statistic = **1.09** (p = **0.3667**), Residual SE = **14.229** on **369** df, AIC = **3143.7**, BIC = **3203.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.5614** | 6.0409 | ±12.0818 | **+20.620** | **1.83e-94** | *** |
| Education: graduate level (vs college) | +0.0274 | 1.5465 | ±3.0931 | +0.018 | 0.9859 |  |
| Education: high school or below (vs college) | +4.2190 | 2.9586 | ±5.9172 | +1.426 | 0.1539 |  |
| Site: UCSD (vs UAB) | -0.2727 | 1.9943 | ±3.9886 | -0.137 | 0.8912 |  |
| Site: UW (vs UAB) | +0.9710 | 1.9763 | ±3.9526 | +0.491 | 0.6232 |  |
| Season: spring (vs autumn) | +1.1522 | 2.1564 | ±4.3128 | +0.534 | 0.5931 |  |
| Season: summer (vs autumn) | +2.1201 | 2.2036 | ±4.4072 | +0.962 | 0.3360 |  |
| Season: winter (vs autumn) | +3.2549 | 2.1803 | ±4.3607 | +1.493 | 0.1355 |  |
| Age (years) | -0.0900 | 0.0756 | ±0.1512 | -1.191 | 0.2338 |  |
| BMI (kg/m2) | +0.1560 | 0.1078 | ±0.2155 | +1.448 | 0.1477 |  |
| Hypertension | +1.9242 | 1.7922 | ±3.5844 | +1.074 | 0.2830 |  |
| High cholesterol | +1.0107 | 1.7109 | ±3.4219 | +0.591 | 0.5547 |  |
| Kidney disease | -0.9180 | 2.3547 | ±4.7095 | -0.390 | 0.6967 |  |
| Circulatory disease | -0.9471 | 2.3055 | ±4.6109 | -0.411 | 0.6812 |  |
| Avg. daily time < 70 (%) | +3.9018 | 3.7271 | ±7.4542 | +1.047 | 0.2952 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.0384**, Adj R² = **0.0019**, F-statistic = **1.05** (p = **0.4003**), Residual SE = **14.238** on **369** df, AIC = **3144.2**, BIC = **3203.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1243.3989 | 1484.9720 | ±2969.9440 | +0.837 | 0.4024 |  |
| Education: graduate level (vs college) | -0.0155 | 1.5587 | ±3.1174 | -0.010 | 0.9921 |  |
| Education: high school or below (vs college) | +4.4447 | 2.9491 | ±5.8983 | +1.507 | 0.1318 |  |
| Site: UCSD (vs UAB) | -0.1934 | 2.0120 | ±4.0240 | -0.096 | 0.9234 |  |
| Site: UW (vs UAB) | +0.9667 | 1.9864 | ±3.9728 | +0.487 | 0.6265 |  |
| Season: spring (vs autumn) | +1.1386 | 2.1657 | ±4.3315 | +0.526 | 0.5991 |  |
| Season: summer (vs autumn) | +2.0039 | 2.2035 | ±4.4070 | +0.909 | 0.3631 |  |
| Season: winter (vs autumn) | +3.3274 | 2.1705 | ±4.3409 | +1.533 | 0.1253 |  |
| Age (years) | -0.0873 | 0.0750 | ±0.1501 | -1.163 | 0.2449 |  |
| BMI (kg/m2) | +0.1504 | 0.1091 | ±0.2182 | +1.379 | 0.1678 |  |
| Hypertension | +1.6204 | 1.7965 | ±3.5930 | +0.902 | 0.3671 |  |
| High cholesterol | +1.1168 | 1.6916 | ±3.3832 | +0.660 | 0.5091 |  |
| Kidney disease | -0.9964 | 2.3651 | ±4.7301 | -0.421 | 0.6735 |  |
| Circulatory disease | -0.9535 | 2.2816 | ±4.5632 | -0.418 | 0.6760 |  |
| Time 54-250, pooled (%) | -11.1849 | 14.8479 | ±29.6959 | -0.753 | 0.4513 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **384**, R² = **0.0408**, Adj R² = **0.0045**, F-statistic = **1.12** (p = **0.3361**), Residual SE = **14.220** on **369** df, AIC = **3143.2**, BIC = **3202.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2298.0656 | 1750.9408 | ±3501.8815 | +1.312 | 0.1894 |  |
| Education: graduate level (vs college) | -0.0679 | 1.5579 | ±3.1158 | -0.044 | 0.9652 |  |
| Education: high school or below (vs college) | +4.4156 | 2.9501 | ±5.9002 | +1.497 | 0.1345 |  |
| Site: UCSD (vs UAB) | -0.2078 | 1.9950 | ±3.9901 | -0.104 | 0.9170 |  |
| Site: UW (vs UAB) | +0.9326 | 1.9771 | ±3.9542 | +0.472 | 0.6371 |  |
| Season: spring (vs autumn) | +1.1757 | 2.1573 | ±4.3147 | +0.545 | 0.5858 |  |
| Season: summer (vs autumn) | +2.2144 | 2.1870 | ±4.3740 | +1.013 | 0.3113 |  |
| Season: winter (vs autumn) | +3.3514 | 2.1639 | ±4.3278 | +1.549 | 0.1214 |  |
| Age (years) | -0.0861 | 0.0751 | ±0.1503 | -1.146 | 0.2519 |  |
| BMI (kg/m2) | +0.1511 | 0.1084 | ±0.2167 | +1.395 | 0.1631 |  |
| Hypertension | +1.6257 | 1.7819 | ±3.5638 | +0.912 | 0.3616 |  |
| High cholesterol | +1.1227 | 1.6928 | ±3.3856 | +0.663 | 0.5072 |  |
| Kidney disease | -1.0394 | 2.3611 | ±4.7221 | -0.440 | 0.6598 |  |
| Circulatory disease | -1.0945 | 2.2806 | ±4.5611 | -0.480 | 0.6313 |  |
| Avg. daily time 54-250 (%) | -21.7328 | 17.5077 | ±35.0154 | -1.241 | 0.2145 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **384**, R² = **0.0390**, Adj R² = **0.0025**, F-statistic = **1.07** (p = **0.3842**), Residual SE = **14.234** on **369** df, AIC = **3144.0**, BIC = **3203.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.1033** | 6.2629 | ±12.5257 | **+20.135** | **3.64e-90** | *** |
| Education: graduate level (vs college) | -0.0020 | 1.5472 | ±3.0943 | -0.001 | 0.9990 |  |
| Education: high school or below (vs college) | +4.3103 | 2.9497 | ±5.8993 | +1.461 | 0.1439 |  |
| Site: UCSD (vs UAB) | -0.3849 | 1.9886 | ±3.9772 | -0.194 | 0.8465 |  |
| Site: UW (vs UAB) | +0.9065 | 1.9834 | ±3.9668 | +0.457 | 0.6476 |  |
| Season: spring (vs autumn) | +1.1669 | 2.1682 | ±4.3364 | +0.538 | 0.5905 |  |
| Season: summer (vs autumn) | +2.1375 | 2.2292 | ±4.4585 | +0.959 | 0.3376 |  |
| Season: winter (vs autumn) | +3.3898 | 2.1774 | ±4.3548 | +1.557 | 0.1195 |  |
| Age (years) | -0.0922 | 0.0755 | ±0.1510 | -1.222 | 0.2219 |  |
| BMI (kg/m2) | +0.1494 | 0.1125 | ±0.2251 | +1.328 | 0.1843 |  |
| Hypertension | +1.7726 | 1.7796 | ±3.5592 | +0.996 | 0.3192 |  |
| High cholesterol | +1.0923 | 1.6914 | ±3.3828 | +0.646 | 0.5184 |  |
| Kidney disease | -0.8149 | 2.4140 | ±4.8279 | -0.338 | 0.7357 |  |
| Circulatory disease | -0.8220 | 2.2999 | ±4.5998 | -0.357 | 0.7208 |  |
| Time 181-250, pooled (%) | -2.3514 | 2.8056 | ±5.6112 | -0.838 | 0.4020 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **384**, R² = **0.0399**, Adj R² = **0.0035**, F-statistic = **1.10** (p = **0.3600**), Residual SE = **14.227** on **369** df, AIC = **3143.6**, BIC = **3202.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2153** | 6.1729 | ±12.3458 | **+20.447** | **6.44e-93** | *** |
| Education: graduate level (vs college) | +0.0086 | 1.5433 | ±3.0866 | +0.006 | 0.9956 |  |
| Education: high school or below (vs college) | +4.2300 | 2.9552 | ±5.9105 | +1.431 | 0.1523 |  |
| Site: UCSD (vs UAB) | -0.4123 | 1.9815 | ±3.9629 | -0.208 | 0.8352 |  |
| Site: UW (vs UAB) | +0.9149 | 1.9808 | ±3.9616 | +0.462 | 0.6442 |  |
| Season: spring (vs autumn) | +1.2259 | 2.1781 | ±4.3562 | +0.563 | 0.5736 |  |
| Season: summer (vs autumn) | +2.1463 | 2.2308 | ±4.4616 | +0.962 | 0.3360 |  |
| Season: winter (vs autumn) | +3.4001 | 2.1806 | ±4.3612 | +1.559 | 0.1189 |  |
| Age (years) | -0.0958 | 0.0757 | ±0.1513 | -1.266 | 0.2054 |  |
| BMI (kg/m2) | +0.1530 | 0.1089 | ±0.2179 | +1.405 | 0.1601 |  |
| Hypertension | +1.7853 | 1.7800 | ±3.5600 | +1.003 | 0.3159 |  |
| High cholesterol | +1.1433 | 1.6969 | ±3.3938 | +0.674 | 0.5005 |  |
| Kidney disease | -0.9388 | 2.4114 | ±4.8229 | -0.389 | 0.6970 |  |
| Circulatory disease | -0.7939 | 2.2829 | ±4.5657 | -0.348 | 0.7280 |  |
| Avg. daily time 181-250 (%) | -2.7980 | 2.9185 | ±5.8370 | -0.959 | 0.3377 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **384**, R² = **0.0391**, Adj R² = **0.0026**, F-statistic = **1.07** (p = **0.3811**), Residual SE = **14.233** on **369** df, AIC = **3143.9**, BIC = **3203.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.1348** | 6.2671 | ±12.5342 | **+20.126** | **4.33e-90** | *** |
| Education: graduate level (vs college) | -0.0029 | 1.5475 | ±3.0949 | -0.002 | 0.9985 |  |
| Education: high school or below (vs college) | +4.3085 | 2.9497 | ±5.8995 | +1.461 | 0.1441 |  |
| Site: UCSD (vs UAB) | -0.3851 | 1.9884 | ±3.9767 | -0.194 | 0.8464 |  |
| Site: UW (vs UAB) | +0.9086 | 1.9833 | ±3.9665 | +0.458 | 0.6469 |  |
| Season: spring (vs autumn) | +1.1682 | 2.1680 | ±4.3360 | +0.539 | 0.5900 |  |
| Season: summer (vs autumn) | +2.1408 | 2.2294 | ±4.4589 | +0.960 | 0.3369 |  |
| Season: winter (vs autumn) | +3.3934 | 2.1774 | ±4.3549 | +1.558 | 0.1191 |  |
| Age (years) | -0.0924 | 0.0755 | ±0.1510 | -1.223 | 0.2212 |  |
| BMI (kg/m2) | +0.1491 | 0.1127 | ±0.2253 | +1.324 | 0.1856 |  |
| Hypertension | +1.7736 | 1.7794 | ±3.5588 | +0.997 | 0.3189 |  |
| High cholesterol | +1.0939 | 1.6914 | ±3.3829 | +0.647 | 0.5178 |  |
| Kidney disease | -0.8079 | 2.4157 | ±4.8313 | -0.334 | 0.7380 |  |
| Circulatory disease | -0.8218 | 2.2997 | ±4.5994 | -0.357 | 0.7208 |  |
| Time > 180 (%) | -2.4127 | 2.8048 | ±5.6095 | -0.860 | 0.3897 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **384**, R² = **0.0401**, Adj R² = **0.0036**, F-statistic = **1.10** (p = **0.3561**), Residual SE = **14.226** on **369** df, AIC = **3143.5**, BIC = **3202.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2491** | 6.1743 | ±12.3485 | **+20.448** | **6.30e-93** | *** |
| Education: graduate level (vs college) | +0.0074 | 1.5436 | ±3.0873 | +0.005 | 0.9962 |  |
| Education: high school or below (vs college) | +4.2260 | 2.9554 | ±5.9108 | +1.430 | 0.1527 |  |
| Site: UCSD (vs UAB) | -0.4132 | 1.9811 | ±3.9622 | -0.209 | 0.8348 |  |
| Site: UW (vs UAB) | +0.9175 | 1.9806 | ±3.9612 | +0.463 | 0.6432 |  |
| Season: spring (vs autumn) | +1.2284 | 2.1780 | ±4.3559 | +0.564 | 0.5728 |  |
| Season: summer (vs autumn) | +2.1495 | 2.2310 | ±4.4620 | +0.963 | 0.3353 |  |
| Season: winter (vs autumn) | +3.4043 | 2.1807 | ±4.3613 | +1.561 | 0.1185 |  |
| Age (years) | -0.0960 | 0.0757 | ±0.1513 | -1.269 | 0.2043 |  |
| BMI (kg/m2) | +0.1529 | 0.1090 | ±0.2180 | +1.403 | 0.1607 |  |
| Hypertension | +1.7862 | 1.7798 | ±3.5597 | +1.004 | 0.3156 |  |
| High cholesterol | +1.1468 | 1.6970 | ±3.3940 | +0.676 | 0.4992 |  |
| Kidney disease | -0.9358 | 2.4130 | ±4.8260 | -0.388 | 0.6982 |  |
| Circulatory disease | -0.7931 | 2.2822 | ±4.5644 | -0.348 | 0.7282 |  |
| Avg. daily time > 180 (%) | -2.8627 | 2.9162 | ±5.8324 | -0.982 | 0.3263 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 384)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **384**, R² = **0.0378**, Adj R² = **0.0013**, F-statistic = **1.03** (p = **0.4175**), Residual SE = **14.243** on **369** df, AIC = **3144.5**, BIC = **3203.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+124.8187** | 6.1997 | ±12.3993 | **+20.133** | **3.78e-90** | *** |
| Education: graduate level (vs college) | +0.0211 | 1.5633 | ±3.1266 | +0.014 | 0.9892 |  |
| Education: high school or below (vs college) | +4.3463 | 2.9368 | ±5.8736 | +1.480 | 0.1389 |  |
| Site: UCSD (vs UAB) | -0.3341 | 2.0073 | ±4.0147 | -0.166 | 0.8678 |  |
| Site: UW (vs UAB) | +0.8537 | 1.9837 | ±3.9674 | +0.430 | 0.6670 |  |
| Season: spring (vs autumn) | +1.0686 | 2.1661 | ±4.3321 | +0.493 | 0.6218 |  |
| Season: summer (vs autumn) | +2.0067 | 2.1994 | ±4.3988 | +0.912 | 0.3616 |  |
| Season: winter (vs autumn) | +3.2190 | 2.1625 | ±4.3251 | +1.489 | 0.1366 |  |
| Age (years) | -0.0821 | 0.0765 | ±0.1530 | -1.073 | 0.2831 |  |
| BMI (kg/m2) | +0.1492 | 0.1097 | ±0.2193 | +1.361 | 0.1736 |  |
| Hypertension | +1.6556 | 1.7941 | ±3.5882 | +0.923 | 0.3561 |  |
| High cholesterol | +1.0648 | 1.6813 | ±3.3627 | +0.633 | 0.5265 |  |
| Kidney disease | -1.1354 | 2.3606 | ±4.7213 | -0.481 | 0.6305 |  |
| Circulatory disease | -0.8402 | 2.3112 | ±4.6224 | -0.364 | 0.7162 |  |
| Nocturnal time > 180 (%) | +1.3116 | 2.1243 | ±4.2487 | +0.617 | 0.5370 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 344; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **344**, R² = **0.1714**, Adj R² = **0.1465**, F-statistic = **6.89** (p = **8.38e-10**), Residual SE = **3359.536** on **333** df, AIC = **6573.3**, BIC = **6615.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18737.1654** | 1352.8715 | ±2705.7429 | **+13.850** | **1.27e-43** | *** |
| Education: graduate level (vs college) | -608.4617 | 372.7710 | ±745.5420 | -1.632 | 0.1026 |  |
| Education: high school or below (vs college) | +1206.0004 | 903.7020 | ±1807.4039 | +1.335 | 0.1820 |  |
| Site: UCSD (vs UAB) | -228.1382 | 496.6439 | ±993.2878 | -0.459 | 0.6460 |  |
| **Site: UW (vs UAB)** | **-932.5830** | 457.6689 | ±915.3378 | **-2.038** | **0.0416** | * |
| **Age (years)** | **-114.6485** | 17.6928 | ±35.3856 | **-6.480** | **9.17e-11** | *** |
| BMI (kg/m2) | -48.3669 | 25.1795 | ±50.3590 | -1.921 | 0.0547 | . |
| Hypertension | +139.4417 | 428.9198 | ±857.8396 | +0.325 | 0.7451 |  |
| High cholesterol | -78.7601 | 381.6871 | ±763.3742 | -0.206 | 0.8365 |  |
| Kidney disease | -494.6464 | 812.3045 | ±1624.6090 | -0.609 | 0.5426 |  |
| Circulatory disease | -716.8285 | 697.5878 | ±1395.1756 | -1.028 | 0.3041 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **344**, R² = **0.1753**, Adj R² = **0.1479**, F-statistic = **6.41** (p = **1.16e-09**), Residual SE = **3356.744** on **332** df, AIC = **6573.7**, BIC = **6619.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14648.5954** | 3659.3022 | ±7318.6043 | **+4.003** | **6.25e-05** | *** |
| Education: graduate level (vs college) | -594.5043 | 372.0039 | ±744.0078 | -1.598 | 0.1100 |  |
| Education: high school or below (vs college) | +1184.7587 | 900.8461 | ±1801.6922 | +1.315 | 0.1885 |  |
| Site: UCSD (vs UAB) | -185.0097 | 493.6141 | ±987.2282 | -0.375 | 0.7078 |  |
| Site: UW (vs UAB) | -886.6190 | 456.2231 | ±912.4463 | -1.943 | 0.0520 | . |
| **Age (years)** | **-117.1549** | 17.8917 | ±35.7835 | **-6.548** | **5.83e-11** | *** |
| **BMI (kg/m2)** | **-51.7722** | 24.5478 | ±49.0956 | **-2.109** | **0.0349** | * |
| Hypertension | +95.9523 | 428.7355 | ±857.4710 | +0.224 | 0.8229 |  |
| High cholesterol | -187.1493 | 391.2889 | ±782.5778 | -0.478 | 0.6324 |  |
| Kidney disease | -454.7819 | 824.9006 | ±1649.8013 | -0.551 | 0.5814 |  |
| Circulatory disease | -684.2582 | 698.1701 | ±1396.3402 | -0.980 | 0.3270 |  |
| HbA1c (%) | +788.7293 | 651.2510 | ±1302.5019 | +1.211 | 0.2259 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **344**, R² = **0.1716**, Adj R² = **0.1442**, F-statistic = **6.25** (p = **2.20e-09**), Residual SE = **3364.124** on **332** df, AIC = **6575.2**, BIC = **6621.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19582.1597** | 3449.5143 | ±6899.0285 | **+5.677** | **1.37e-08** | *** |
| Education: graduate level (vs college) | -611.4817 | 373.7285 | ±747.4569 | -1.636 | 0.1018 |  |
| Education: high school or below (vs college) | +1197.8873 | 907.0025 | ±1814.0051 | +1.321 | 0.1866 |  |
| Site: UCSD (vs UAB) | -219.7096 | 502.3937 | ±1004.7873 | -0.437 | 0.6619 |  |
| **Site: UW (vs UAB)** | **-924.1300** | 461.8649 | ±923.7298 | **-2.001** | **0.0454** | * |
| **Age (years)** | **-114.9381** | 17.7693 | ±35.5386 | **-6.468** | **9.91e-11** | *** |
| BMI (kg/m2) | -47.6756 | 25.4558 | ±50.9117 | -1.873 | 0.0611 | . |
| Hypertension | +151.2524 | 433.9657 | ±867.9314 | +0.349 | 0.7274 |  |
| High cholesterol | -83.8997 | 385.4173 | ±770.8345 | -0.218 | 0.8277 |  |
| Kidney disease | -492.5171 | 812.6969 | ±1625.3939 | -0.606 | 0.5445 |  |
| Circulatory disease | -717.2150 | 699.0036 | ±1398.0072 | -1.026 | 0.3049 |  |
| Mean glucose (mg/dL) | -7.4751 | 28.0072 | ±56.0144 | -0.267 | 0.7895 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **344**, R² = **0.1716**, Adj R² = **0.1442**, F-statistic = **6.25** (p = **2.20e-09**), Residual SE = **3364.124** on **332** df, AIC = **6575.2**, BIC = **6621.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20616.5541** | 7176.0672 | ±14352.1343 | **+2.873** | **0.0041** | ** |
| Education: graduate level (vs college) | -611.4817 | 373.7285 | ±747.4569 | -1.636 | 0.1018 |  |
| Education: high school or below (vs college) | +1197.8873 | 907.0025 | ±1814.0051 | +1.321 | 0.1866 |  |
| Site: UCSD (vs UAB) | -219.7096 | 502.3937 | ±1004.7873 | -0.437 | 0.6619 |  |
| **Site: UW (vs UAB)** | **-924.1300** | 461.8649 | ±923.7298 | **-2.001** | **0.0454** | * |
| **Age (years)** | **-114.9381** | 17.7693 | ±35.5386 | **-6.468** | **9.91e-11** | *** |
| BMI (kg/m2) | -47.6756 | 25.4558 | ±50.9117 | -1.873 | 0.0611 | . |
| Hypertension | +151.2524 | 433.9657 | ±867.9314 | +0.349 | 0.7274 |  |
| High cholesterol | -83.8997 | 385.4173 | ±770.8345 | -0.218 | 0.8277 |  |
| Kidney disease | -492.5171 | 812.6969 | ±1625.3939 | -0.606 | 0.5445 |  |
| Circulatory disease | -717.2150 | 699.0036 | ±1398.0072 | -1.026 | 0.3049 |  |
| GMI (%) | -312.5059 | 1170.8688 | ±2341.7377 | -0.267 | 0.7895 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **344**, R² = **0.1715**, Adj R² = **0.1440**, F-statistic = **6.25** (p = **2.26e-09**), Residual SE = **3364.397** on **332** df, AIC = **6575.3**, BIC = **6621.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18286.7580** | 2705.1759 | ±5410.3517 | **+6.760** | **1.38e-11** | *** |
| Education: graduate level (vs college) | -602.4163 | 376.2088 | ±752.4175 | -1.601 | 0.1093 |  |
| Education: high school or below (vs college) | +1212.1415 | 906.2013 | ±1812.4027 | +1.338 | 0.1810 |  |
| Site: UCSD (vs UAB) | -239.4538 | 503.0218 | ±1006.0436 | -0.476 | 0.6341 |  |
| **Site: UW (vs UAB)** | **-940.6941** | 460.7530 | ±921.5059 | **-2.042** | **0.0412** | * |
| **Age (years)** | **-114.0664** | 17.9873 | ±35.9747 | **-6.341** | **2.28e-10** | *** |
| BMI (kg/m2) | -49.2783 | 25.7930 | ±51.5860 | -1.911 | 0.0561 | . |
| Hypertension | +134.0156 | 430.8638 | ±861.7276 | +0.311 | 0.7558 |  |
| High cholesterol | -78.6250 | 382.8061 | ±765.6121 | -0.205 | 0.8373 |  |
| Kidney disease | -489.3042 | 814.8305 | ±1629.6610 | -0.600 | 0.5482 |  |
| Circulatory disease | -713.6510 | 699.3265 | ±1398.6530 | -1.020 | 0.3075 |  |
| Nocturnal mean 00-06h (mg/dL) | +3.8864 | 20.3793 | ±40.7586 | +0.191 | 0.8488 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **344**, R² = **0.1769**, Adj R² = **0.1496**, F-statistic = **6.49** (p = **8.69e-10**), Residual SE = **3353.383** on **332** df, AIC = **6573.0**, BIC = **6619.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20785.6273** | 1919.5157 | ±3839.0314 | **+10.829** | **2.52e-27** | *** |
| Education: graduate level (vs college) | -661.8320 | 371.9292 | ±743.8585 | -1.779 | 0.0752 | . |
| Education: high school or below (vs college) | +1165.5124 | 909.3013 | ±1818.6026 | +1.282 | 0.1999 |  |
| Site: UCSD (vs UAB) | -294.6967 | 496.4653 | ±992.9306 | -0.594 | 0.5528 |  |
| **Site: UW (vs UAB)** | **-980.1542** | 464.8356 | ±929.6713 | **-2.109** | **0.0350** | * |
| **Age (years)** | **-114.4057** | 17.7661 | ±35.5322 | **-6.440** | **1.20e-10** | *** |
| BMI (kg/m2) | -46.4564 | 25.2874 | ±50.5747 | -1.837 | 0.0662 | . |
| Hypertension | +152.4517 | 428.2380 | ±856.4760 | +0.356 | 0.7218 |  |
| High cholesterol | -116.3891 | 383.4187 | ±766.8375 | -0.304 | 0.7615 |  |
| Kidney disease | -400.1377 | 776.6371 | ±1553.2742 | -0.515 | 0.6064 |  |
| Circulatory disease | -702.5254 | 699.8377 | ±1399.6754 | -1.004 | 0.3155 |  |
| Glucose SD, pooled (mg/dL) | -121.6274 | 90.1999 | ±180.3998 | -1.348 | 0.1775 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **344**, R² = **0.1788**, Adj R² = **0.1516**, F-statistic = **6.57** (p = **6.23e-10**), Residual SE = **3349.560** on **332** df, AIC = **6572.2**, BIC = **6618.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20914.4973** | 1819.3771 | ±3638.7543 | **+11.495** | **1.39e-30** | *** |
| Education: graduate level (vs college) | -673.3168 | 373.8955 | ±747.7911 | -1.801 | 0.0717 | . |
| Education: high school or below (vs college) | +1147.0393 | 911.0270 | ±1822.0540 | +1.259 | 0.2080 |  |
| Site: UCSD (vs UAB) | -315.4106 | 495.7594 | ±991.5189 | -0.636 | 0.5246 |  |
| **Site: UW (vs UAB)** | **-995.4199** | 463.7502 | ±927.5003 | **-2.146** | **0.0318** | * |
| **Age (years)** | **-114.6894** | 17.7096 | ±35.4192 | **-6.476** | **9.41e-11** | *** |
| BMI (kg/m2) | -44.9812 | 25.5712 | ±51.1423 | -1.759 | 0.0786 | . |
| Hypertension | +138.5167 | 427.7728 | ±855.5457 | +0.324 | 0.7461 |  |
| High cholesterol | -114.1637 | 381.4099 | ±762.8198 | -0.299 | 0.7647 |  |
| Kidney disease | -389.6207 | 774.5108 | ±1549.0215 | -0.503 | 0.6149 |  |
| Circulatory disease | -715.0196 | 700.8412 | ±1401.6825 | -1.020 | 0.3076 |  |
| Avg. daily SD (mg/dL) | -140.7542 | 86.5289 | ±173.0579 | -1.627 | 0.1038 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **344**, R² = **0.1762**, Adj R² = **0.1489**, F-statistic = **6.45** (p = **9.93e-10**), Residual SE = **3354.923** on **332** df, AIC = **6573.3**, BIC = **6619.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20582.4999** | 1815.4154 | ±3630.8308 | **+11.338** | **8.54e-30** | *** |
| Education: graduate level (vs college) | -650.4361 | 372.7479 | ±745.4957 | -1.745 | 0.0810 | . |
| Education: high school or below (vs college) | +1186.1211 | 909.2882 | ±1818.5764 | +1.304 | 0.1921 |  |
| Site: UCSD (vs UAB) | -304.1582 | 497.9874 | ±995.9749 | -0.611 | 0.5413 |  |
| **Site: UW (vs UAB)** | **-993.2339** | 466.1710 | ±932.3421 | **-2.131** | **0.0331** | * |
| **Age (years)** | **-113.8891** | 17.7950 | ±35.5901 | **-6.400** | **1.55e-10** | *** |
| BMI (kg/m2) | -48.0661 | 24.9141 | ±49.8281 | -1.929 | 0.0537 | . |
| Hypertension | +127.1536 | 430.8039 | ±861.6078 | +0.295 | 0.7679 |  |
| High cholesterol | -104.0905 | 381.0229 | ±762.0458 | -0.273 | 0.7847 |  |
| Kidney disease | -417.3190 | 785.4450 | ±1570.8900 | -0.531 | 0.5952 |  |
| Circulatory disease | -701.6015 | 701.4036 | ±1402.8072 | -1.000 | 0.3172 |  |
| CV (%) | -123.3208 | 89.5213 | ±179.0427 | -1.378 | 0.1683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **344**, R² = **0.1764**, Adj R² = **0.1491**, F-statistic = **6.46** (p = **9.50e-10**), Residual SE = **3354.412** on **332** df, AIC = **6573.2**, BIC = **6619.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16966.1817** | 1956.0064 | ±3912.0128 | **+8.674** | **4.18e-18** | *** |
| Education: graduate level (vs college) | -655.3913 | 373.3058 | ±746.6117 | -1.756 | 0.0791 | . |
| Education: high school or below (vs college) | +1191.3727 | 910.6285 | ±1821.2570 | +1.308 | 0.1908 |  |
| Site: UCSD (vs UAB) | -294.4740 | 497.8000 | ±995.6000 | -0.592 | 0.5542 |  |
| **Site: UW (vs UAB)** | **-983.3622** | 465.4183 | ±930.8366 | **-2.113** | **0.0346** | * |
| **Age (years)** | **-114.0105** | 17.7883 | ±35.5767 | **-6.409** | **1.46e-10** | *** |
| BMI (kg/m2) | -48.1649 | 24.8545 | ±49.7089 | -1.938 | 0.0526 | . |
| Hypertension | +134.8162 | 429.7449 | ±859.4899 | +0.314 | 0.7537 |  |
| High cholesterol | -106.9865 | 380.6027 | ±761.2055 | -0.281 | 0.7786 |  |
| Kidney disease | -437.1366 | 787.3809 | ±1574.7618 | -0.555 | 0.5788 |  |
| Circulatory disease | -704.7957 | 701.4233 | ±1402.8465 | -1.005 | 0.3150 |  |
| Mean / SD ratio | +260.6185 | 189.1556 | ±378.3111 | +1.378 | 0.1683 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **344**, R² = **0.1780**, Adj R² = **0.1508**, F-statistic = **6.54** (p = **7.12e-10**), Residual SE = **3351.101** on **332** df, AIC = **6572.5**, BIC = **6618.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16842.2368** | 1872.7416 | ±3745.4833 | **+8.993** | **2.40e-19** | *** |
| Education: graduate level (vs college) | -665.1039 | 375.0919 | ±750.1838 | -1.773 | 0.0762 | . |
| Education: high school or below (vs college) | +1179.1688 | 912.3134 | ±1824.6267 | +1.293 | 0.1962 |  |
| Site: UCSD (vs UAB) | -317.7922 | 496.6461 | ±993.2922 | -0.640 | 0.5223 |  |
| **Site: UW (vs UAB)** | **-996.9237** | 463.8357 | ±927.6714 | **-2.149** | **0.0316** | * |
| **Age (years)** | **-114.2045** | 17.7365 | ±35.4730 | **-6.439** | **1.20e-10** | *** |
| BMI (kg/m2) | -46.3378 | 25.1329 | ±50.2658 | -1.844 | 0.0652 | . |
| Hypertension | +113.6677 | 430.6570 | ±861.3140 | +0.264 | 0.7918 |  |
| High cholesterol | -97.8498 | 379.6652 | ±759.3303 | -0.258 | 0.7966 |  |
| Kidney disease | -418.1708 | 789.1847 | ±1578.3693 | -0.530 | 0.5962 |  |
| Circulatory disease | -715.7875 | 702.4189 | ±1404.8379 | -1.019 | 0.3082 |  |
| Avg. daily mean/SD | +244.6903 | 151.6154 | ±303.2307 | +1.614 | 0.1066 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **344**, R² = **0.1718**, Adj R² = **0.1444**, F-statistic = **6.26** (p = **2.13e-09**), Residual SE = **3363.726** on **332** df, AIC = **6575.1**, BIC = **6621.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18196.7105** | 1831.7983 | ±3663.5965 | **+9.934** | **2.97e-23** | *** |
| Education: graduate level (vs college) | -608.3817 | 373.9138 | ±747.8275 | -1.627 | 0.1037 |  |
| Education: high school or below (vs college) | +1186.1692 | 907.5205 | ±1815.0409 | +1.307 | 0.1912 |  |
| Site: UCSD (vs UAB) | -211.3568 | 495.8400 | ±991.6800 | -0.426 | 0.6699 |  |
| Site: UW (vs UAB) | -907.5477 | 467.3633 | ±934.7265 | -1.942 | 0.0522 | . |
| **Age (years)** | **-113.6816** | 17.6062 | ±35.2123 | **-6.457** | **1.07e-10** | *** |
| BMI (kg/m2) | -47.5728 | 25.0858 | ±50.1715 | -1.896 | 0.0579 | . |
| Hypertension | +150.0064 | 433.0157 | ±866.0314 | +0.346 | 0.7290 |  |
| High cholesterol | -89.6989 | 386.4008 | ±772.8016 | -0.232 | 0.8164 |  |
| Kidney disease | -521.7510 | 816.0054 | ±1632.0108 | -0.639 | 0.5226 |  |
| Circulatory disease | -722.9547 | 699.6959 | ±1399.3919 | -1.033 | 0.3015 |  |
| MAG (mg/dL/h) | +13.1549 | 35.3276 | ±70.6553 | +0.372 | 0.7096 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **344**, R² = **0.1738**, Adj R² = **0.1465**, F-statistic = **6.35** (p = **1.50e-09**), Residual SE = **3359.640** on **332** df, AIC = **6574.3**, BIC = **6620.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20185.0616** | 2062.3884 | ±4124.7768 | **+9.787** | **1.28e-22** | *** |
| Education: graduate level (vs college) | -624.3918 | 375.2091 | ±750.4183 | -1.664 | 0.0961 | . |
| Education: high school or below (vs college) | +1188.8025 | 905.4840 | ±1810.9680 | +1.313 | 0.1892 |  |
| Site: UCSD (vs UAB) | -269.3213 | 495.6429 | ±991.2858 | -0.543 | 0.5869 |  |
| **Site: UW (vs UAB)** | **-967.2025** | 464.8228 | ±929.6456 | **-2.081** | **0.0375** | * |
| **Age (years)** | **-115.1116** | 17.7248 | ±35.4497 | **-6.494** | **8.34e-11** | *** |
| **BMI (kg/m2)** | **-50.3044** | 24.5310 | ±49.0620 | **-2.051** | **0.0403** | * |
| Hypertension | +116.4170 | 433.0267 | ±866.0534 | +0.269 | 0.7880 |  |
| High cholesterol | -79.8803 | 382.0912 | ±764.1824 | -0.209 | 0.8344 |  |
| Kidney disease | -453.9153 | 800.5830 | ±1601.1660 | -0.567 | 0.5707 |  |
| Circulatory disease | -699.0845 | 702.3528 | ±1404.7055 | -0.995 | 0.3196 |  |
| Avg. daily range (mg/dL) | -16.5423 | 19.4258 | ±38.8517 | -0.852 | 0.3945 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **344**, R² = **0.1714**, Adj R² = **0.1440**, F-statistic = **6.24** (p = **2.28e-09**), Residual SE = **3364.526** on **332** df, AIC = **6575.3**, BIC = **6621.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18686.4726** | 1445.3196 | ±2890.6391 | **+12.929** | **3.09e-38** | *** |
| Education: graduate level (vs college) | -609.8053 | 377.0339 | ±754.0678 | -1.617 | 0.1058 |  |
| Education: high school or below (vs college) | +1203.1084 | 912.0263 | ±1824.0527 | +1.319 | 0.1871 |  |
| Site: UCSD (vs UAB) | -227.1350 | 497.8397 | ±995.6794 | -0.456 | 0.6482 |  |
| **Site: UW (vs UAB)** | **-935.0471** | 460.1976 | ±920.3952 | **-2.032** | **0.0422** | * |
| **Age (years)** | **-114.7285** | 17.7710 | ±35.5419 | **-6.456** | **1.08e-10** | *** |
| BMI (kg/m2) | -48.4353 | 25.3718 | ±50.7436 | -1.909 | 0.0563 | . |
| Hypertension | +136.1128 | 430.2899 | ±860.5798 | +0.316 | 0.7518 |  |
| High cholesterol | -78.6710 | 383.5433 | ±767.0866 | -0.205 | 0.8375 |  |
| Kidney disease | -491.9725 | 815.0094 | ±1630.0188 | -0.604 | 0.5461 |  |
| Circulatory disease | -718.4509 | 701.8098 | ±1403.6197 | -1.024 | 0.3060 |  |
| SD of daily means (mg/dL) | +11.7644 | 127.0225 | ±254.0451 | +0.093 | 0.9262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **344**, R² = **0.1776**, Adj R² = **0.1504**, F-statistic = **6.52** (p = **7.64e-10**), Residual SE = **3351.913** on **332** df, AIC = **6572.7**, BIC = **6618.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +115961.9523 | 59974.0515 | ±119948.1029 | +1.934 | 0.0532 | . |
| Education: graduate level (vs college) | -582.6748 | 373.3987 | ±746.7975 | -1.560 | 0.1187 |  |
| Education: high school or below (vs college) | +1242.0377 | 906.3637 | ±1812.7274 | +1.370 | 0.1706 |  |
| Site: UCSD (vs UAB) | -176.2299 | 492.8097 | ±985.6194 | -0.358 | 0.7206 |  |
| **Site: UW (vs UAB)** | **-894.4077** | 454.9862 | ±909.9724 | **-1.966** | **0.0493** | * |
| **Age (years)** | **-113.2784** | 17.6636 | ±35.3272 | **-6.413** | **1.43e-10** | *** |
| BMI (kg/m2) | -46.7964 | 26.3720 | ±52.7440 | -1.774 | 0.0760 | . |
| Hypertension | +132.1466 | 427.1050 | ±854.2100 | +0.309 | 0.7570 |  |
| High cholesterol | -100.2281 | 383.7860 | ±767.5721 | -0.261 | 0.7940 |  |
| Kidney disease | -543.2520 | 844.9977 | ±1689.9954 | -0.643 | 0.5203 |  |
| Circulatory disease | -732.3732 | 700.7281 | ±1401.4562 | -1.045 | 0.2959 |  |
| Time in range 70-180, pooled (%) | -978.3127 | 602.0608 | ±1204.1217 | -1.625 | 0.1042 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **344**, R² = **0.1786**, Adj R² = **0.1514**, F-statistic = **6.56** (p = **6.42e-10**), Residual SE = **3349.916** on **332** df, AIC = **6572.3**, BIC = **6618.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+120237.8992** | 58662.0420 | ±117324.0840 | **+2.050** | **0.0404** | * |
| Education: graduate level (vs college) | -578.0479 | 373.0336 | ±746.0673 | -1.550 | 0.1212 |  |
| Education: high school or below (vs college) | +1262.0507 | 903.9902 | ±1807.9805 | +1.396 | 0.1627 |  |
| Site: UCSD (vs UAB) | -181.6504 | 491.1659 | ±982.3317 | -0.370 | 0.7115 |  |
| **Site: UW (vs UAB)** | **-923.7989** | 454.2565 | ±908.5130 | **-2.034** | **0.0420** | * |
| **Age (years)** | **-112.1763** | 17.5763 | ±35.1526 | **-6.382** | **1.75e-10** | *** |
| BMI (kg/m2) | -47.8915 | 25.6226 | ±51.2453 | -1.869 | 0.0616 | . |
| Hypertension | +168.4396 | 430.4289 | ±860.8578 | +0.391 | 0.6956 |  |
| High cholesterol | -111.2399 | 383.5633 | ±767.1267 | -0.290 | 0.7718 |  |
| Kidney disease | -502.2864 | 838.8868 | ±1677.7736 | -0.599 | 0.5493 |  |
| Circulatory disease | -762.3623 | 697.8074 | ±1395.6148 | -1.093 | 0.2746 |  |
| Avg. daily time in range 70-180 (%) | -1020.9705 | 588.4638 | ±1176.9275 | -1.735 | 0.0827 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **344**, R² = **0.1716**, Adj R² = **0.1442**, F-statistic = **6.25** (p = **2.21e-09**), Residual SE = **3364.158** on **332** df, AIC = **6575.2**, BIC = **6621.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18702.6629** | 1366.1516 | ±2732.3031 | **+13.690** | **1.16e-42** | *** |
| Education: graduate level (vs college) | -606.6034 | 374.8048 | ±749.6097 | -1.618 | 0.1056 |  |
| Education: high school or below (vs college) | +1210.4444 | 905.4979 | ±1810.9958 | +1.337 | 0.1813 |  |
| Site: UCSD (vs UAB) | -206.5460 | 504.1584 | ±1008.3168 | -0.410 | 0.6820 |  |
| **Site: UW (vs UAB)** | **-919.7681** | 460.7663 | ±921.5325 | **-1.996** | **0.0459** | * |
| **Age (years)** | **-114.6765** | 17.7481 | ±35.4963 | **-6.461** | **1.04e-10** | *** |
| BMI (kg/m2) | -48.3633 | 25.2311 | ±50.4622 | -1.917 | 0.0553 | . |
| Hypertension | +131.9833 | 429.9526 | ±859.9051 | +0.307 | 0.7589 |  |
| High cholesterol | -77.4115 | 382.7726 | ±765.5451 | -0.202 | 0.8397 |  |
| Kidney disease | -479.7449 | 819.2997 | ±1638.5993 | -0.586 | 0.5582 |  |
| Circulatory disease | -725.7353 | 699.2793 | ±1398.5586 | -1.038 | 0.2993 |  |
| Any reading < 54 during wear (0/1) | +142.8272 | 460.0967 | ±920.1933 | +0.310 | 0.7562 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **344**, R² = **0.1758**, Adj R² = **0.1485**, F-statistic = **6.44** (p = **1.05e-09**), Residual SE = **3355.578** on **332** df, AIC = **6573.5**, BIC = **6619.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18638.5748** | 1355.1619 | ±2710.3238 | **+13.754** | **4.83e-43** | *** |
| Education: graduate level (vs college) | -601.7974 | 375.1891 | ±750.3782 | -1.604 | 0.1087 |  |
| Education: high school or below (vs college) | +1260.9596 | 907.6630 | ±1815.3260 | +1.389 | 0.1648 |  |
| Site: UCSD (vs UAB) | -155.2007 | 501.1661 | ±1002.3321 | -0.310 | 0.7568 |  |
| Site: UW (vs UAB) | -896.0089 | 459.1868 | ±918.3737 | -1.951 | 0.0510 | . |
| **Age (years)** | **-113.6394** | 17.6768 | ±35.3535 | **-6.429** | **1.29e-10** | *** |
| **BMI (kg/m2)** | **-50.9346** | 24.8998 | ±49.7996 | **-2.046** | **0.0408** | * |
| Hypertension | +98.5600 | 426.1703 | ±852.3406 | +0.231 | 0.8171 |  |
| High cholesterol | -70.2225 | 382.2795 | ±764.5590 | -0.184 | 0.8543 |  |
| Kidney disease | -442.5028 | 815.9602 | ±1631.9204 | -0.542 | 0.5876 |  |
| Circulatory disease | -783.0479 | 710.6022 | ±1421.2044 | -1.102 | 0.2705 |  |
| Time < 54 (%) | +4645.6067 | 5234.6682 | ±10469.3363 | +0.887 | 0.3748 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **344**, R² = **0.1810**, Adj R² = **0.1538**, F-statistic = **6.67** (p = **4.22e-10**), Residual SE = **3345.102** on **332** df, AIC = **6571.3**, BIC = **6617.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18667.5462** | 1349.7046 | ±2699.4093 | **+13.831** | **1.66e-43** | *** |
| Education: graduate level (vs college) | -626.7449 | 371.4647 | ±742.9293 | -1.687 | 0.0916 | . |
| Education: high school or below (vs college) | +1233.8384 | 905.1374 | ±1810.2747 | +1.363 | 0.1728 |  |
| Site: UCSD (vs UAB) | -172.2521 | 493.5083 | ±987.0166 | -0.349 | 0.7271 |  |
| **Site: UW (vs UAB)** | **-920.1367** | 458.3822 | ±916.7644 | **-2.007** | **0.0447** | * |
| **Age (years)** | **-113.7225** | 17.5751 | ±35.1502 | **-6.471** | **9.76e-11** | *** |
| **BMI (kg/m2)** | **-50.9503** | 25.0405 | ±50.0811 | **-2.035** | **0.0419** | * |
| Hypertension | +116.0736 | 426.9673 | ±853.9346 | +0.272 | 0.7857 |  |
| High cholesterol | -61.8489 | 380.9724 | ±761.9448 | -0.162 | 0.8710 |  |
| Kidney disease | -449.1402 | 817.6182 | ±1635.2363 | -0.549 | 0.5828 |  |
| Circulatory disease | -855.8216 | 718.6641 | ±1437.3283 | -1.191 | 0.2337 |  |
| Avg. daily time < 54 (%) | +8155.5683 | 6335.8486 | ±12671.6973 | +1.287 | 0.1980 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **344**, R² = **0.1716**, Adj R² = **0.1442**, F-statistic = **6.25** (p = **2.21e-09**), Residual SE = **3364.151** on **332** df, AIC = **6575.2**, BIC = **6621.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18681.2917** | 1366.7369 | ±2733.4738 | **+13.669** | **1.57e-42** | *** |
| Education: graduate level (vs college) | -603.1738 | 375.2516 | ±750.5033 | -1.607 | 0.1080 |  |
| Education: high school or below (vs college) | +1198.9707 | 910.6560 | ±1821.3120 | +1.317 | 0.1880 |  |
| Site: UCSD (vs UAB) | -218.2468 | 495.5146 | ±991.0292 | -0.440 | 0.6596 |  |
| **Site: UW (vs UAB)** | **-921.5160** | 459.0608 | ±918.1216 | **-2.007** | **0.0447** | * |
| **Age (years)** | **-114.6753** | 17.7446 | ±35.4893 | **-6.463** | **1.03e-10** | *** |
| BMI (kg/m2) | -48.1311 | 25.2919 | ±50.5838 | -1.903 | 0.0570 | . |
| Hypertension | +152.4473 | 433.2053 | ±866.4106 | +0.352 | 0.7249 |  |
| High cholesterol | -93.3002 | 392.6287 | ±785.2574 | -0.238 | 0.8122 |  |
| Kidney disease | -483.4568 | 816.9220 | ±1633.8440 | -0.592 | 0.5540 |  |
| Circulatory disease | -715.9170 | 699.5365 | ±1399.0729 | -1.023 | 0.3061 |  |
| Time 54-69, pooled (%) | +300.2638 | 981.8964 | ±1963.7929 | +0.306 | 0.7598 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **344**, R² = **0.1715**, Adj R² = **0.1440**, F-statistic = **6.25** (p = **2.27e-09**), Residual SE = **3364.469** on **332** df, AIC = **6575.3**, BIC = **6621.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18712.9267** | 1357.0624 | ±2714.1248 | **+13.789** | **2.96e-43** | *** |
| Education: graduate level (vs college) | -604.4449 | 374.7519 | ±749.5038 | -1.613 | 0.1068 |  |
| Education: high school or below (vs college) | +1202.6015 | 909.7291 | ±1819.4583 | +1.322 | 0.1862 |  |
| Site: UCSD (vs UAB) | -225.3172 | 495.5556 | ±991.1112 | -0.455 | 0.6493 |  |
| **Site: UW (vs UAB)** | **-930.5723** | 458.5391 | ±917.0783 | **-2.029** | **0.0424** | * |
| **Age (years)** | **-114.6742** | 17.7341 | ±35.4683 | **-6.466** | **1.00e-10** | *** |
| BMI (kg/m2) | -48.3014 | 25.2655 | ±50.5311 | -1.912 | 0.0559 | . |
| Hypertension | +150.7294 | 440.5055 | ±881.0111 | +0.342 | 0.7322 |  |
| High cholesterol | -84.4423 | 390.1379 | ±780.2758 | -0.216 | 0.8286 |  |
| Kidney disease | -489.5009 | 817.5062 | ±1635.0123 | -0.599 | 0.5493 |  |
| Circulatory disease | -720.0313 | 700.8109 | ±1401.6219 | -1.027 | 0.3042 |  |
| Avg. daily time 54-69 (%) | +160.5898 | 1003.1227 | ±2006.2454 | +0.160 | 0.8728 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **344**, R² = **0.1723**, Adj R² = **0.1449**, F-statistic = **6.28** (p = **1.95e-09**), Residual SE = **3362.726** on **332** df, AIC = **6574.9**, BIC = **6621.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18623.6104** | 1370.6398 | ±2741.2795 | **+13.588** | **4.75e-42** | *** |
| Education: graduate level (vs college) | -598.0292 | 376.3856 | ±752.7713 | -1.589 | 0.1121 |  |
| Education: high school or below (vs college) | +1199.6566 | 909.4485 | ±1818.8971 | +1.319 | 0.1871 |  |
| Site: UCSD (vs UAB) | -201.4932 | 495.4680 | ±990.9360 | -0.407 | 0.6842 |  |
| **Site: UW (vs UAB)** | **-908.0811** | 459.0997 | ±918.1994 | **-1.978** | **0.0479** | * |
| **Age (years)** | **-114.5785** | 17.7604 | ±35.5208 | **-6.451** | **1.11e-10** | *** |
| BMI (kg/m2) | -48.2395 | 25.3316 | ±50.6633 | -1.904 | 0.0569 | . |
| Hypertension | +158.3473 | 433.7404 | ±867.4808 | +0.365 | 0.7151 |  |
| High cholesterol | -104.2788 | 391.9273 | ±783.8546 | -0.266 | 0.7902 |  |
| Kidney disease | -468.0850 | 816.7750 | ±1633.5500 | -0.573 | 0.5666 |  |
| Circulatory disease | -722.9737 | 702.3785 | ±1404.7571 | -1.029 | 0.3033 |  |
| Time < 70 (%) | +547.7692 | 973.3642 | ±1946.7283 | +0.563 | 0.5736 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **344**, R² = **0.1722**, Adj R² = **0.1448**, F-statistic = **6.28** (p = **1.98e-09**), Residual SE = **3362.908** on **332** df, AIC = **6575.0**, BIC = **6621.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18651.7288** | 1358.4484 | ±2716.8968 | **+13.730** | **6.70e-43** | *** |
| Education: graduate level (vs college) | -596.2620 | 376.1917 | ±752.3834 | -1.585 | 0.1130 |  |
| Education: high school or below (vs college) | +1196.4899 | 909.8164 | ±1819.6327 | +1.315 | 0.1885 |  |
| Site: UCSD (vs UAB) | -215.0557 | 494.5150 | ±989.0300 | -0.435 | 0.6636 |  |
| **Site: UW (vs UAB)** | **-925.0574** | 458.4348 | ±916.8696 | **-2.018** | **0.0436** | * |
| **Age (years)** | **-114.6734** | 17.7338 | ±35.4676 | **-6.466** | **1.00e-10** | *** |
| BMI (kg/m2) | -48.3179 | 25.3532 | ±50.7065 | -1.906 | 0.0567 | . |
| Hypertension | +175.5638 | 443.1039 | ±886.2079 | +0.396 | 0.6919 |  |
| High cholesterol | -96.6056 | 389.5020 | ±779.0039 | -0.248 | 0.8041 |  |
| Kidney disease | -474.4912 | 817.0366 | ±1634.0732 | -0.581 | 0.5614 |  |
| Circulatory disease | -736.6441 | 703.9270 | ±1407.8539 | -1.046 | 0.2953 |  |
| Avg. daily time < 70 (%) | +535.7469 | 1016.9479 | ±2033.8958 | +0.527 | 0.5983 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **344**, R² = **0.1756**, Adj R² = **0.1483**, F-statistic = **6.43** (p = **1.10e-09**), Residual SE = **3356.118** on **332** df, AIC = **6573.6**, BIC = **6619.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +467196.3580 | 523788.8656 | ±1047577.7312 | +0.892 | 0.3724 |  |
| Education: graduate level (vs college) | -597.9257 | 376.4560 | ±752.9119 | -1.588 | 0.1122 |  |
| Education: high school or below (vs college) | +1262.1010 | 907.6685 | ±1815.3370 | +1.390 | 0.1644 |  |
| Site: UCSD (vs UAB) | -157.4380 | 501.3149 | ±1002.6298 | -0.314 | 0.7535 |  |
| Site: UW (vs UAB) | -899.8982 | 459.1530 | ±918.3059 | -1.960 | 0.0500 | . |
| **Age (years)** | **-113.5062** | 17.6828 | ±35.3657 | **-6.419** | **1.37e-10** | *** |
| **BMI (kg/m2)** | **-50.6516** | 24.9268 | ±49.8535 | **-2.032** | **0.0422** | * |
| Hypertension | +101.4236 | 426.3395 | ±852.6790 | +0.238 | 0.8120 |  |
| High cholesterol | -75.1943 | 382.7615 | ±765.5230 | -0.196 | 0.8443 |  |
| Kidney disease | -443.7339 | 816.0561 | ±1632.1123 | -0.544 | 0.5866 |  |
| Circulatory disease | -780.4535 | 710.5279 | ±1421.0557 | -1.098 | 0.2720 |  |
| Time 54-250, pooled (%) | -4485.7146 | 5239.1118 | ±10478.2235 | -0.856 | 0.3919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **344**, R² = **0.1804**, Adj R² = **0.1532**, F-statistic = **6.64** (p = **4.70e-10**), Residual SE = **3346.343** on **332** df, AIC = **6571.6**, BIC = **6617.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +800955.0706 | 635699.9652 | ±1271399.9304 | +1.260 | 0.2077 |  |
| Education: graduate level (vs college) | -618.0804 | 372.2763 | ±744.5526 | -1.660 | 0.0969 | . |
| Education: high school or below (vs college) | +1238.5605 | 904.9366 | ±1809.8733 | +1.369 | 0.1711 |  |
| Site: UCSD (vs UAB) | -174.0026 | 493.6892 | ±987.3784 | -0.352 | 0.7245 |  |
| **Site: UW (vs UAB)** | **-925.7235** | 458.7654 | ±917.5307 | **-2.018** | **0.0436** | * |
| **Age (years)** | **-113.4360** | 17.5931 | ±35.1862 | **-6.448** | **1.14e-10** | *** |
| **BMI (kg/m2)** | **-50.4691** | 25.1017 | ±50.2035 | **-2.011** | **0.0444** | * |
| Hypertension | +119.8387 | 427.4094 | ±854.8188 | +0.280 | 0.7792 |  |
| High cholesterol | -71.5712 | 381.5631 | ±763.1263 | -0.188 | 0.8512 |  |
| Kidney disease | -449.9066 | 817.6047 | ±1635.2095 | -0.550 | 0.5821 |  |
| Circulatory disease | -849.5480 | 718.5549 | ±1437.1099 | -1.182 | 0.2371 |  |
| Avg. daily time 54-250 (%) | -7823.1765 | 6357.8014 | ±12715.6028 | -1.230 | 0.2185 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **344**, R² = **0.1753**, Adj R² = **0.1479**, F-statistic = **6.41** (p = **1.16e-09**), Residual SE = **3356.760** on **332** df, AIC = **6573.7**, BIC = **6619.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18403.4322** | 1389.1424 | ±2778.2847 | **+13.248** | **4.63e-40** | *** |
| Education: graduate level (vs college) | -603.2380 | 373.3772 | ±746.7544 | -1.616 | 0.1062 |  |
| Education: high school or below (vs college) | +1244.9737 | 905.0022 | ±1810.0045 | +1.376 | 0.1689 |  |
| Site: UCSD (vs UAB) | -224.5828 | 497.1124 | ±994.2248 | -0.452 | 0.6514 |  |
| **Site: UW (vs UAB)** | **-936.7647** | 456.1395 | ±912.2789 | **-2.054** | **0.0400** | * |
| **Age (years)** | **-113.6402** | 17.6685 | ±35.3369 | **-6.432** | **1.26e-10** | *** |
| BMI (kg/m2) | -47.2818 | 26.1495 | ±52.2991 | -1.808 | 0.0706 | . |
| Hypertension | +104.9141 | 429.1116 | ±858.2232 | +0.244 | 0.8069 |  |
| High cholesterol | -57.7917 | 384.2220 | ±768.4440 | -0.150 | 0.8804 |  |
| Kidney disease | -574.8923 | 847.7857 | ±1695.5714 | -0.678 | 0.4977 |  |
| Circulatory disease | -720.6989 | 697.0071 | ±1394.0141 | -1.034 | 0.3011 |  |
| Time 181-250, pooled (%) | +816.3458 | 669.6591 | ±1339.3183 | +1.219 | 0.2228 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **344**, R² = **0.1766**, Adj R² = **0.1493**, F-statistic = **6.47** (p = **9.24e-10**), Residual SE = **3354.086** on **332** df, AIC = **6573.2**, BIC = **6619.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18345.4732** | 1369.9396 | ±2739.8791 | **+13.391** | **6.78e-41** | *** |
| Education: graduate level (vs college) | -602.8662 | 372.8705 | ±745.7409 | -1.617 | 0.1059 |  |
| Education: high school or below (vs college) | +1272.9950 | 904.9189 | ±1809.8378 | +1.407 | 0.1595 |  |
| Site: UCSD (vs UAB) | -208.5283 | 496.0308 | ±992.0616 | -0.420 | 0.6742 |  |
| **Site: UW (vs UAB)** | **-937.0499** | 455.7060 | ±911.4120 | **-2.056** | **0.0398** | * |
| **Age (years)** | **-112.3878** | 17.6612 | ±35.3224 | **-6.364** | **1.97e-10** | *** |
| BMI (kg/m2) | -48.0631 | 25.4720 | ±50.9439 | -1.887 | 0.0592 | . |
| Hypertension | +102.7486 | 429.3369 | ±858.6738 | +0.239 | 0.8109 |  |
| High cholesterol | -76.2895 | 382.4208 | ±764.8415 | -0.199 | 0.8419 |  |
| Kidney disease | -536.8013 | 839.0482 | ±1678.0964 | -0.640 | 0.5223 |  |
| Circulatory disease | -723.9933 | 694.6965 | ±1389.3929 | -1.042 | 0.2973 |  |
| Avg. daily time 181-250 (%) | +931.7457 | 655.2929 | ±1310.5857 | +1.422 | 0.1551 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **344**, R² = **0.1752**, Adj R² = **0.1479**, F-statistic = **6.41** (p = **1.17e-09**), Residual SE = **3356.857** on **332** df, AIC = **6573.7**, BIC = **6619.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18402.7495** | 1389.8959 | ±2779.7919 | **+13.240** | **5.13e-40** | *** |
| Education: graduate level (vs college) | -602.5346 | 373.4020 | ±746.8040 | -1.614 | 0.1066 |  |
| Education: high school or below (vs college) | +1245.2413 | 904.9953 | ±1809.9906 | +1.376 | 0.1688 |  |
| Site: UCSD (vs UAB) | -224.5590 | 497.1155 | ±994.2311 | -0.452 | 0.6515 |  |
| **Site: UW (vs UAB)** | **-937.2099** | 456.1509 | ±912.3017 | **-2.055** | **0.0399** | * |
| **Age (years)** | **-113.6171** | 17.6700 | ±35.3399 | **-6.430** | **1.28e-10** | *** |
| BMI (kg/m2) | -47.2544 | 26.1511 | ±52.3022 | -1.807 | 0.0708 | . |
| Hypertension | +105.4257 | 429.1017 | ±858.2035 | +0.246 | 0.8059 |  |
| High cholesterol | -58.7878 | 384.1489 | ±768.2978 | -0.153 | 0.8784 |  |
| Kidney disease | -574.2131 | 847.5244 | ±1695.0489 | -0.678 | 0.4981 |  |
| Circulatory disease | -720.6141 | 697.0516 | ±1394.1032 | -1.034 | 0.3012 |  |
| Time > 180 (%) | +810.4722 | 668.2730 | ±1336.5460 | +1.213 | 0.2252 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **344**, R² = **0.1765**, Adj R² = **0.1492**, F-statistic = **6.47** (p = **9.34e-10**), Residual SE = **3354.217** on **332** df, AIC = **6573.2**, BIC = **6619.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18344.5048** | 1370.8939 | ±2741.7878 | **+13.381** | **7.77e-41** | *** |
| Education: graduate level (vs college) | -601.9719 | 372.9253 | ±745.8505 | -1.614 | 0.1065 |  |
| Education: high school or below (vs college) | +1273.1866 | 904.9157 | ±1809.8314 | +1.407 | 0.1594 |  |
| Site: UCSD (vs UAB) | -208.6125 | 496.0384 | ±992.0769 | -0.421 | 0.6741 |  |
| **Site: UW (vs UAB)** | **-937.6169** | 455.7314 | ±911.4627 | **-2.057** | **0.0396** | * |
| **Age (years)** | **-112.3663** | 17.6646 | ±35.3293 | **-6.361** | **2.00e-10** | *** |
| BMI (kg/m2) | -48.0209 | 25.4774 | ±50.9548 | -1.885 | 0.0595 | . |
| Hypertension | +103.3554 | 429.3273 | ±858.6545 | +0.241 | 0.8098 |  |
| High cholesterol | -77.3757 | 382.3926 | ±764.7851 | -0.202 | 0.8396 |  |
| Kidney disease | -536.3576 | 838.8368 | ±1677.6735 | -0.639 | 0.5226 |  |
| Circulatory disease | -723.8677 | 694.7661 | ±1389.5322 | -1.042 | 0.2975 |  |
| Avg. daily time > 180 (%) | +924.7811 | 653.6312 | ±1307.2624 | +1.415 | 0.1571 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 344)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **344**, R² = **0.1727**, Adj R² = **0.1453**, F-statistic = **6.30** (p = **1.82e-09**), Residual SE = **3361.904** on **332** df, AIC = **6574.8**, BIC = **6620.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18604.2241** | 1360.0921 | ±2720.1842 | **+13.679** | **1.36e-42** | *** |
| Education: graduate level (vs college) | -586.3072 | 375.3223 | ±750.6446 | -1.562 | 0.1183 |  |
| Education: high school or below (vs college) | +1204.7133 | 901.0546 | ±1802.1092 | +1.337 | 0.1812 |  |
| Site: UCSD (vs UAB) | -221.2556 | 496.3169 | ±992.6339 | -0.446 | 0.6557 |  |
| **Site: UW (vs UAB)** | **-945.1835** | 457.2677 | ±914.5354 | **-2.067** | **0.0387** | * |
| **Age (years)** | **-112.0033** | 18.0760 | ±36.1521 | **-6.196** | **5.78e-10** | *** |
| **BMI (kg/m2)** | **-50.4995** | 25.0427 | ±50.0854 | **-2.017** | **0.0437** | * |
| Hypertension | +121.0911 | 428.0730 | ±856.1460 | +0.283 | 0.7773 |  |
| High cholesterol | -97.6340 | 380.7022 | ±761.4045 | -0.256 | 0.7976 |  |
| Kidney disease | -524.7631 | 825.4026 | ±1650.8052 | -0.636 | 0.5249 |  |
| Circulatory disease | -712.6061 | 704.3712 | ±1408.7424 | -1.012 | 0.3117 |  |
| Nocturnal time > 180 (%) | +387.5554 | 642.6237 | ±1285.2473 | +0.603 | 0.5465 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 344; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **344**, R² = **0.1751**, Adj R² = **0.1503**, F-statistic = **7.07** (p = **4.34e-10**), Residual SE = **11.394** on **333** df, AIC = **2661.0**, BIC = **2703.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2786** | 4.9053 | ±9.8106 | **+10.250** | **1.19e-24** | *** |
| Education: graduate level (vs college) | -1.6660 | 1.2709 | ±2.5419 | -1.311 | 0.1899 |  |
| Education: high school or below (vs college) | +3.0126 | 2.8710 | ±5.7420 | +1.049 | 0.2940 |  |
| Site: UCSD (vs UAB) | -1.2002 | 1.6694 | ±3.3388 | -0.719 | 0.4722 |  |
| Site: UW (vs UAB) | -2.6139 | 1.5944 | ±3.1889 | -1.639 | 0.1011 |  |
| **Age (years)** | **-0.4087** | 0.0599 | ±0.1198 | **-6.821** | **9.01e-12** | *** |
| BMI (kg/m2) | +0.0039 | 0.0892 | ±0.1784 | +0.044 | 0.9651 |  |
| Hypertension | +0.4195 | 1.4913 | ±2.9826 | +0.281 | 0.7785 |  |
| High cholesterol | -0.3162 | 1.3006 | ±2.6013 | -0.243 | 0.8079 |  |
| Kidney disease | -1.5600 | 2.6180 | ±5.2359 | -0.596 | 0.5512 |  |
| Circulatory disease | -1.8889 | 2.1948 | ±4.3897 | -0.861 | 0.3894 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **344**, R² = **0.1767**, Adj R² = **0.1494**, F-statistic = **6.48** (p = **9.00e-10**), Residual SE = **11.399** on **332** df, AIC = **2662.3**, BIC = **2708.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.2250** | 12.7113 | ±25.4226 | **+3.243** | **0.0012** | ** |
| Education: graduate level (vs college) | -1.6350 | 1.2721 | ±2.5442 | -1.285 | 0.1987 |  |
| Education: high school or below (vs college) | +2.9656 | 2.8578 | ±5.7155 | +1.038 | 0.2994 |  |
| Site: UCSD (vs UAB) | -1.1047 | 1.6585 | ±3.3170 | -0.666 | 0.5053 |  |
| Site: UW (vs UAB) | -2.5121 | 1.5902 | ±3.1804 | -1.580 | 0.1142 |  |
| **Age (years)** | **-0.4142** | 0.0603 | ±0.1206 | **-6.868** | **6.49e-12** | *** |
| BMI (kg/m2) | -0.0036 | 0.0879 | ±0.1758 | -0.041 | 0.9670 |  |
| Hypertension | +0.3232 | 1.4944 | ±2.9888 | +0.216 | 0.8288 |  |
| High cholesterol | -0.5562 | 1.3401 | ±2.6802 | -0.415 | 0.6781 |  |
| Kidney disease | -1.4718 | 2.6327 | ±5.2654 | -0.559 | 0.5761 |  |
| Circulatory disease | -1.8168 | 2.2038 | ±4.4075 | -0.824 | 0.4097 |  |
| HbA1c (%) | +1.7465 | 2.2513 | ±4.5026 | +0.776 | 0.4379 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **344**, R² = **0.1756**, Adj R² = **0.1483**, F-statistic = **6.43** (p = **1.09e-09**), Residual SE = **11.407** on **332** df, AIC = **2662.8**, BIC = **2708.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.8070** | 11.4773 | ±22.9547 | **+4.775** | **1.79e-06** | *** |
| Education: graduate level (vs college) | -1.6821 | 1.2734 | ±2.5468 | -1.321 | 0.1865 |  |
| Education: high school or below (vs college) | +2.9691 | 2.8692 | ±5.7385 | +1.035 | 0.3008 |  |
| Site: UCSD (vs UAB) | -1.1551 | 1.6890 | ±3.3780 | -0.684 | 0.4941 |  |
| Site: UW (vs UAB) | -2.5686 | 1.6120 | ±3.2241 | -1.593 | 0.1111 |  |
| **Age (years)** | **-0.4102** | 0.0600 | ±0.1200 | **-6.837** | **8.10e-12** | *** |
| BMI (kg/m2) | +0.0076 | 0.0906 | ±0.1812 | +0.084 | 0.9331 |  |
| Hypertension | +0.4828 | 1.5061 | ±3.0121 | +0.321 | 0.7486 |  |
| High cholesterol | -0.3438 | 1.3162 | ±2.6323 | -0.261 | 0.7940 |  |
| Kidney disease | -1.5486 | 2.6075 | ±5.2149 | -0.594 | 0.5526 |  |
| Circulatory disease | -1.8910 | 2.1974 | ±4.3948 | -0.861 | 0.3895 |  |
| Mean glucose (mg/dL) | -0.0401 | 0.0944 | ±0.1887 | -0.425 | 0.6712 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **344**, R² = **0.1756**, Adj R² = **0.1483**, F-statistic = **6.43** (p = **1.09e-09**), Residual SE = **11.407** on **332** df, AIC = **2662.8**, BIC = **2708.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.3504** | 23.9371 | ±47.8741 | **+2.521** | **0.0117** | * |
| Education: graduate level (vs college) | -1.6821 | 1.2734 | ±2.5468 | -1.321 | 0.1865 |  |
| Education: high school or below (vs college) | +2.9691 | 2.8692 | ±5.7385 | +1.035 | 0.3008 |  |
| Site: UCSD (vs UAB) | -1.1551 | 1.6890 | ±3.3780 | -0.684 | 0.4941 |  |
| Site: UW (vs UAB) | -2.5686 | 1.6120 | ±3.2241 | -1.593 | 0.1111 |  |
| **Age (years)** | **-0.4102** | 0.0600 | ±0.1200 | **-6.837** | **8.10e-12** | *** |
| BMI (kg/m2) | +0.0076 | 0.0906 | ±0.1812 | +0.084 | 0.9331 |  |
| Hypertension | +0.4828 | 1.5061 | ±3.0121 | +0.321 | 0.7486 |  |
| High cholesterol | -0.3438 | 1.3162 | ±2.6323 | -0.261 | 0.7940 |  |
| Kidney disease | -1.5486 | 2.6075 | ±5.2149 | -0.594 | 0.5526 |  |
| Circulatory disease | -1.8910 | 2.1974 | ±4.3948 | -0.861 | 0.3895 |  |
| GMI (%) | -1.6747 | 3.9449 | ±7.8897 | -0.425 | 0.6712 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **344**, R² = **0.1751**, Adj R² = **0.1477**, F-statistic = **6.41** (p = **1.20e-09**), Residual SE = **11.411** on **332** df, AIC = **2663.0**, BIC = **2709.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.1423** | 9.3159 | ±18.6318 | **+5.382** | **7.35e-08** | *** |
| Education: graduate level (vs college) | -1.6641 | 1.2822 | ±2.5644 | -1.298 | 0.1943 |  |
| Education: high school or below (vs college) | +3.0145 | 2.8722 | ±5.7443 | +1.050 | 0.2939 |  |
| Site: UCSD (vs UAB) | -1.2037 | 1.6977 | ±3.3954 | -0.709 | 0.4783 |  |
| Site: UW (vs UAB) | -2.6163 | 1.6116 | ±3.2233 | -1.623 | 0.1045 |  |
| **Age (years)** | **-0.4085** | 0.0602 | ±0.1204 | **-6.783** | **1.17e-11** | *** |
| BMI (kg/m2) | +0.0036 | 0.0922 | ±0.1845 | +0.039 | 0.9687 |  |
| Hypertension | +0.4178 | 1.4967 | ±2.9934 | +0.279 | 0.7801 |  |
| High cholesterol | -0.3162 | 1.3060 | ±2.6121 | -0.242 | 0.8087 |  |
| Kidney disease | -1.5584 | 2.6225 | ±5.2450 | -0.594 | 0.5523 |  |
| Circulatory disease | -1.8880 | 2.1987 | ±4.3975 | -0.859 | 0.3905 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0012 | 0.0719 | ±0.1438 | +0.016 | 0.9870 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **344**, R² = **0.1757**, Adj R² = **0.1483**, F-statistic = **6.43** (p = **1.09e-09**), Residual SE = **11.407** on **332** df, AIC = **2662.7**, BIC = **2708.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.5353** | 6.6192 | ±13.2383 | **+7.937** | **2.07e-15** | *** |
| Education: graduate level (vs college) | -1.7247 | 1.2668 | ±2.5335 | -1.362 | 0.1733 |  |
| Education: high school or below (vs college) | +2.9680 | 2.8833 | ±5.7667 | +1.029 | 0.3033 |  |
| Site: UCSD (vs UAB) | -1.2736 | 1.6606 | ±3.3213 | -0.767 | 0.4431 |  |
| Site: UW (vs UAB) | -2.6663 | 1.6077 | ±3.2153 | -1.658 | 0.0972 | . |
| **Age (years)** | **-0.4084** | 0.0602 | ±0.1204 | **-6.785** | **1.16e-11** | *** |
| BMI (kg/m2) | +0.0060 | 0.0902 | ±0.1804 | +0.067 | 0.9469 |  |
| Hypertension | +0.4338 | 1.4924 | ±2.9849 | +0.291 | 0.7713 |  |
| High cholesterol | -0.3577 | 1.3176 | ±2.6351 | -0.271 | 0.7860 |  |
| Kidney disease | -1.4559 | 2.6014 | ±5.2029 | -0.560 | 0.5757 |  |
| Circulatory disease | -1.8732 | 2.2012 | ±4.4025 | -0.851 | 0.3948 |  |
| Glucose SD, pooled (mg/dL) | -0.1340 | 0.3048 | ±0.6097 | -0.440 | 0.6603 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **344**, R² = **0.1773**, Adj R² = **0.1500**, F-statistic = **6.50** (p = **8.12e-10**), Residual SE = **11.395** on **332** df, AIC = **2662.1**, BIC = **2708.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.3329** | 6.2184 | ±12.4367 | **+8.737** | **2.38e-18** | *** |
| Education: graduate level (vs college) | -1.7867 | 1.2733 | ±2.5465 | -1.403 | 0.1605 |  |
| Education: high school or below (vs college) | +2.9028 | 2.8895 | ±5.7789 | +1.005 | 0.3151 |  |
| Site: UCSD (vs UAB) | -1.3627 | 1.6568 | ±3.3136 | -0.823 | 0.4108 |  |
| Site: UW (vs UAB) | -2.7309 | 1.6085 | ±3.2169 | -1.698 | 0.0895 | . |
| **Age (years)** | **-0.4087** | 0.0601 | ±0.1201 | **-6.805** | **1.01e-11** | *** |
| BMI (kg/m2) | +0.0102 | 0.0910 | ±0.1821 | +0.112 | 0.9108 |  |
| Hypertension | +0.4177 | 1.4933 | ±2.9867 | +0.280 | 0.7797 |  |
| High cholesterol | -0.3821 | 1.3095 | ±2.6191 | -0.292 | 0.7704 |  |
| Kidney disease | -1.3645 | 2.5818 | ±5.1635 | -0.529 | 0.5972 |  |
| Circulatory disease | -1.8856 | 2.2052 | ±4.4105 | -0.855 | 0.3925 |  |
| Avg. daily SD (mg/dL) | -0.2621 | 0.2852 | ±0.5704 | -0.919 | 0.3581 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **344**, R² = **0.1754**, Adj R² = **0.1481**, F-statistic = **6.42** (p = **1.13e-09**), Residual SE = **11.408** on **332** df, AIC = **2662.8**, BIC = **2708.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.9520** | 6.3313 | ±12.6626 | **+8.206** | **2.30e-16** | *** |
| Education: graduate level (vs college) | -1.7040 | 1.2696 | ±2.5393 | -1.342 | 0.1796 |  |
| Education: high school or below (vs college) | +2.9946 | 2.8858 | ±5.7716 | +1.038 | 0.2994 |  |
| Site: UCSD (vs UAB) | -1.2692 | 1.6656 | ±3.3313 | -0.762 | 0.4461 |  |
| Site: UW (vs UAB) | -2.6689 | 1.6112 | ±3.2223 | -1.656 | 0.0976 | . |
| **Age (years)** | **-0.4080** | 0.0602 | ±0.1205 | **-6.774** | **1.26e-11** | *** |
| BMI (kg/m2) | +0.0042 | 0.0894 | ±0.1787 | +0.047 | 0.9628 |  |
| Hypertension | +0.4083 | 1.5002 | ±3.0004 | +0.272 | 0.7855 |  |
| High cholesterol | -0.3392 | 1.3073 | ±2.6147 | -0.259 | 0.7953 |  |
| Kidney disease | -1.4899 | 2.6074 | ±5.2149 | -0.571 | 0.5677 |  |
| Circulatory disease | -1.8751 | 2.2012 | ±4.4024 | -0.852 | 0.3943 |  |
| CV (%) | -0.1118 | 0.2995 | ±0.5990 | -0.373 | 0.7088 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **344**, R² = **0.1755**, Adj R² = **0.1482**, F-statistic = **6.43** (p = **1.11e-09**), Residual SE = **11.408** on **332** df, AIC = **2662.8**, BIC = **2708.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.4894** | 6.8458 | ±13.6915 | **+7.083** | **1.41e-12** | *** |
| Education: graduate level (vs college) | -1.7134 | 1.2713 | ±2.5426 | -1.348 | 0.1777 |  |
| Education: high school or below (vs college) | +2.9978 | 2.8881 | ±5.7761 | +1.038 | 0.2993 |  |
| Site: UCSD (vs UAB) | -1.2673 | 1.6656 | ±3.3313 | -0.761 | 0.4468 |  |
| Site: UW (vs UAB) | -2.6652 | 1.6099 | ±3.2198 | -1.655 | 0.0978 | . |
| **Age (years)** | **-0.4080** | 0.0602 | ±0.1204 | **-6.779** | **1.21e-11** | *** |
| BMI (kg/m2) | +0.0041 | 0.0892 | ±0.1785 | +0.046 | 0.9633 |  |
| Hypertension | +0.4148 | 1.4968 | ±2.9936 | +0.277 | 0.7817 |  |
| High cholesterol | -0.3447 | 1.3070 | ±2.6141 | -0.264 | 0.7920 |  |
| Kidney disease | -1.5019 | 2.6059 | ±5.2118 | -0.576 | 0.5644 |  |
| Circulatory disease | -1.8768 | 2.2017 | ±4.4034 | -0.852 | 0.3940 |  |
| Mean / SD ratio | +0.2633 | 0.6371 | ±1.2743 | +0.413 | 0.6794 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **344**, R² = **0.1772**, Adj R² = **0.1499**, F-statistic = **6.50** (p = **8.26e-10**), Residual SE = **11.396** on **332** df, AIC = **2662.1**, BIC = **2708.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.6350** | 6.5295 | ±13.0591 | **+7.142** | **9.19e-13** | *** |
| Education: graduate level (vs college) | -1.7749 | 1.2772 | ±2.5545 | -1.390 | 0.1646 |  |
| Education: high school or below (vs college) | +2.9610 | 2.8975 | ±5.7949 | +1.022 | 0.3068 |  |
| Site: UCSD (vs UAB) | -1.3726 | 1.6592 | ±3.3184 | -0.827 | 0.4081 |  |
| Site: UW (vs UAB) | -2.7376 | 1.6074 | ±3.2148 | -1.703 | 0.0885 | . |
| **Age (years)** | **-0.4078** | 0.0601 | ±0.1202 | **-6.788** | **1.14e-11** | *** |
| BMI (kg/m2) | +0.0078 | 0.0898 | ±0.1797 | +0.087 | 0.9308 |  |
| Hypertension | +0.3699 | 1.5016 | ±3.0032 | +0.246 | 0.8054 |  |
| High cholesterol | -0.3529 | 1.3022 | ±2.6043 | -0.271 | 0.7864 |  |
| Kidney disease | -1.4130 | 2.6024 | ±5.2049 | -0.543 | 0.5872 |  |
| Circulatory disease | -1.8869 | 2.2066 | ±4.4132 | -0.855 | 0.3925 |  |
| Avg. daily mean/SD | +0.4705 | 0.4949 | ±0.9897 | +0.951 | 0.3417 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **344**, R² = **0.1820**, Adj R² = **0.1549**, F-statistic = **6.71** (p = **3.52e-10**), Residual SE = **11.363** on **332** df, AIC = **2660.1**, BIC = **2706.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.8820** | 6.4364 | ±12.8729 | **+6.662** | **2.69e-11** | *** |
| Education: graduate level (vs college) | -1.6649 | 1.2725 | ±2.5451 | -1.308 | 0.1908 |  |
| Education: high school or below (vs college) | +2.7412 | 2.8325 | ±5.6650 | +0.968 | 0.3332 |  |
| Site: UCSD (vs UAB) | -0.9706 | 1.6503 | ±3.3006 | -0.588 | 0.5565 |  |
| Site: UW (vs UAB) | -2.2712 | 1.6032 | ±3.2065 | -1.417 | 0.1566 |  |
| **Age (years)** | **-0.3954** | 0.0595 | ±0.1190 | **-6.648** | **2.97e-11** | *** |
| BMI (kg/m2) | +0.0148 | 0.0887 | ±0.1773 | +0.167 | 0.8677 |  |
| Hypertension | +0.5640 | 1.4931 | ±2.9861 | +0.378 | 0.7056 |  |
| High cholesterol | -0.4659 | 1.3067 | ±2.6134 | -0.357 | 0.7214 |  |
| Kidney disease | -1.9310 | 2.6004 | ±5.2008 | -0.743 | 0.4577 |  |
| Circulatory disease | -1.9728 | 2.2110 | ±4.4220 | -0.892 | 0.3723 |  |
| MAG (mg/dL/h) | +0.1800 | 0.1184 | ±0.2368 | +1.521 | 0.1284 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **344**, R² = **0.1752**, Adj R² = **0.1478**, F-statistic = **6.41** (p = **1.18e-09**), Residual SE = **11.410** on **332** df, AIC = **2663.0**, BIC = **2709.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2185** | 7.0022 | ±14.0044 | **+7.315** | **2.58e-13** | *** |
| Education: graduate level (vs college) | -1.6763 | 1.2770 | ±2.5541 | -1.313 | 0.1893 |  |
| Education: high school or below (vs college) | +3.0014 | 2.8818 | ±5.7636 | +1.042 | 0.2976 |  |
| Site: UCSD (vs UAB) | -1.2270 | 1.6547 | ±3.3095 | -0.741 | 0.4584 |  |
| Site: UW (vs UAB) | -2.6363 | 1.6092 | ±3.2184 | -1.638 | 0.1014 |  |
| **Age (years)** | **-0.4090** | 0.0599 | ±0.1198 | **-6.826** | **8.76e-12** | *** |
| BMI (kg/m2) | +0.0026 | 0.0885 | ±0.1770 | +0.030 | 0.9762 |  |
| Hypertension | +0.4045 | 1.5057 | ±3.0113 | +0.269 | 0.7882 |  |
| High cholesterol | -0.3169 | 1.3054 | ±2.6108 | -0.243 | 0.8082 |  |
| Kidney disease | -1.5336 | 2.6125 | ±5.2250 | -0.587 | 0.5572 |  |
| Circulatory disease | -1.8774 | 2.2005 | ±4.4011 | -0.853 | 0.3936 |  |
| Avg. daily range (mg/dL) | -0.0107 | 0.0635 | ±0.1271 | -0.169 | 0.8658 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **344**, R² = **0.1778**, Adj R² = **0.1506**, F-statistic = **6.53** (p = **7.40e-10**), Residual SE = **11.392** on **332** df, AIC = **2661.8**, BIC = **2707.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.6935** | 5.1252 | ±10.2503 | **+9.501** | **2.08e-21** | *** |
| Education: graduate level (vs college) | -1.7080 | 1.2827 | ±2.5654 | -1.332 | 0.1830 |  |
| Education: high school or below (vs college) | +2.9222 | 2.8899 | ±5.7798 | +1.011 | 0.3119 |  |
| Site: UCSD (vs UAB) | -1.1689 | 1.6667 | ±3.3334 | -0.701 | 0.4831 |  |
| Site: UW (vs UAB) | -2.6909 | 1.5964 | ±3.1928 | -1.686 | 0.0919 | . |
| **Age (years)** | **-0.4112** | 0.0599 | ±0.1198 | **-6.861** | **6.82e-12** | *** |
| BMI (kg/m2) | +0.0018 | 0.0895 | ±0.1791 | +0.020 | 0.9843 |  |
| Hypertension | +0.3154 | 1.4884 | ±2.9768 | +0.212 | 0.8322 |  |
| High cholesterol | -0.3134 | 1.3026 | ±2.6052 | -0.241 | 0.8098 |  |
| Kidney disease | -1.4764 | 2.6334 | ±5.2667 | -0.561 | 0.5750 |  |
| Circulatory disease | -1.9397 | 2.1981 | ±4.3962 | -0.882 | 0.3775 |  |
| SD of daily means (mg/dL) | +0.3679 | 0.4303 | ±0.8606 | +0.855 | 0.3926 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **344**, R² = **0.1956**, Adj R² = **0.1690**, F-statistic = **7.34** (p = **2.95e-11**), Residual SE = **11.268** on **332** df, AIC = **2654.3**, BIC = **2700.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+650.4218** | 202.0902 | ±404.1803 | **+3.218** | **0.0013** | ** |
| Education: graduate level (vs college) | -1.5068 | 1.2634 | ±2.5269 | -1.193 | 0.2330 |  |
| Education: high school or below (vs college) | +3.2351 | 2.8155 | ±5.6309 | +1.149 | 0.2505 |  |
| Site: UCSD (vs UAB) | -0.8798 | 1.6383 | ±3.2765 | -0.537 | 0.5912 |  |
| Site: UW (vs UAB) | -2.3782 | 1.5623 | ±3.1247 | -1.522 | 0.1280 |  |
| **Age (years)** | **-0.4002** | 0.0593 | ±0.1186 | **-6.747** | **1.51e-11** | *** |
| BMI (kg/m2) | +0.0136 | 0.0997 | ±0.1994 | +0.136 | 0.8916 |  |
| Hypertension | +0.3744 | 1.4648 | ±2.9296 | +0.256 | 0.7982 |  |
| High cholesterol | -0.4487 | 1.2964 | ±2.5927 | -0.346 | 0.7292 |  |
| Kidney disease | -1.8601 | 2.7308 | ±5.4616 | -0.681 | 0.4958 |  |
| Circulatory disease | -1.9849 | 2.1837 | ±4.3674 | -0.909 | 0.3634 |  |
| **Time in range 70-180, pooled (%)** | **-6.0389** | 2.0288 | ±4.0576 | **-2.977** | **0.0029** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **344**, R² = **0.1961**, Adj R² = **0.1695**, F-statistic = **7.36** (p = **2.69e-11**), Residual SE = **11.264** on **332** df, AIC = **2654.1**, BIC = **2700.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+639.9514** | 196.1649 | ±392.3299 | **+3.262** | **0.0011** | ** |
| Education: graduate level (vs college) | -1.4893 | 1.2575 | ±2.5149 | -1.184 | 0.2363 |  |
| Education: high school or below (vs college) | +3.3382 | 2.8133 | ±5.6265 | +1.187 | 0.2354 |  |
| Site: UCSD (vs UAB) | -0.9302 | 1.6286 | ±3.2572 | -0.571 | 0.5679 |  |
| Site: UW (vs UAB) | -2.5628 | 1.5603 | ±3.1206 | -1.643 | 0.1005 |  |
| **Age (years)** | **-0.3943** | 0.0586 | ±0.1172 | **-6.726** | **1.75e-11** | *** |
| BMI (kg/m2) | +0.0067 | 0.0918 | ±0.1836 | +0.073 | 0.9422 |  |
| Hypertension | +0.5879 | 1.4779 | ±2.9558 | +0.398 | 0.6908 |  |
| High cholesterol | -0.5049 | 1.2935 | ±2.5870 | -0.390 | 0.6963 |  |
| Kidney disease | -1.6044 | 2.7121 | ±5.4243 | -0.592 | 0.5541 |  |
| Circulatory disease | -2.1535 | 2.1688 | ±4.3376 | -0.993 | 0.3207 |  |
| **Avg. daily time in range 70-180 (%)** | **-5.9314** | 1.9659 | ±3.9317 | **-3.017** | **0.0026** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **344**, R² = **0.1757**, Adj R² = **0.1484**, F-statistic = **6.43** (p = **1.08e-09**), Residual SE = **11.406** on **332** df, AIC = **2662.7**, BIC = **2708.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0795** | 4.9586 | ±9.9171 | **+10.100** | **5.55e-24** | *** |
| Education: graduate level (vs college) | -1.6552 | 1.2772 | ±2.5543 | -1.296 | 0.1950 |  |
| Education: high school or below (vs college) | +3.0383 | 2.8792 | ±5.7584 | +1.055 | 0.2913 |  |
| Site: UCSD (vs UAB) | -1.0756 | 1.6771 | ±3.3543 | -0.641 | 0.5213 |  |
| Site: UW (vs UAB) | -2.5399 | 1.5982 | ±3.1964 | -1.589 | 0.1120 |  |
| **Age (years)** | **-0.4088** | 0.0601 | ±0.1202 | **-6.800** | **1.04e-11** | *** |
| BMI (kg/m2) | +0.0039 | 0.0892 | ±0.1784 | +0.044 | 0.9649 |  |
| Hypertension | +0.3764 | 1.4995 | ±2.9990 | +0.251 | 0.8018 |  |
| High cholesterol | -0.3084 | 1.3046 | ±2.6091 | -0.236 | 0.8131 |  |
| Kidney disease | -1.4740 | 2.6383 | ±5.2767 | -0.559 | 0.5764 |  |
| Circulatory disease | -1.9403 | 2.2091 | ±4.4182 | -0.878 | 0.3798 |  |
| Any reading < 54 during wear (0/1) | +0.8244 | 1.6050 | ±3.2100 | +0.514 | 0.6075 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **344**, R² = **0.1816**, Adj R² = **0.1545**, F-statistic = **6.70** (p = **3.78e-10**), Residual SE = **11.366** on **332** df, AIC = **2660.3**, BIC = **2706.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.8725** | 4.8976 | ±9.7953 | **+10.183** | **2.36e-24** | *** |
| Education: graduate level (vs college) | -1.6385 | 1.2769 | ±2.5538 | -1.283 | 0.1994 |  |
| Education: high school or below (vs college) | +3.2390 | 2.8818 | ±5.7637 | +1.124 | 0.2610 |  |
| Site: UCSD (vs UAB) | -0.8998 | 1.6759 | ±3.3518 | -0.537 | 0.5913 |  |
| Site: UW (vs UAB) | -2.4632 | 1.5921 | ±3.1841 | -1.547 | 0.1218 |  |
| **Age (years)** | **-0.4045** | 0.0597 | ±0.1194 | **-6.774** | **1.26e-11** | *** |
| BMI (kg/m2) | -0.0067 | 0.0866 | ±0.1733 | -0.077 | 0.9386 |  |
| Hypertension | +0.2511 | 1.4869 | ±2.9738 | +0.169 | 0.8659 |  |
| High cholesterol | -0.2811 | 1.3005 | ±2.6011 | -0.216 | 0.8289 |  |
| Kidney disease | -1.3453 | 2.6319 | ±5.2638 | -0.511 | 0.6093 |  |
| Circulatory disease | -2.1617 | 2.2610 | ±4.5220 | -0.956 | 0.3390 |  |
| Time < 54 (%) | +19.1344 | 17.7204 | ±35.4407 | +1.080 | 0.2802 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **344**, R² = **0.1865**, Adj R² = **0.1595**, F-statistic = **6.92** (p = **1.58e-10**), Residual SE = **11.332** on **332** df, AIC = **2658.2**, BIC = **2704.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.0206** | 4.8767 | ±9.7534 | **+10.257** | **1.10e-24** | *** |
| Education: graduate level (vs college) | -1.7337 | 1.2632 | ±2.5264 | -1.373 | 0.1699 |  |
| Education: high school or below (vs college) | +3.1158 | 2.8578 | ±5.7157 | +1.090 | 0.2756 |  |
| Site: UCSD (vs UAB) | -0.9931 | 1.6562 | ±3.3123 | -0.600 | 0.5487 |  |
| Site: UW (vs UAB) | -2.5677 | 1.5919 | ±3.1839 | -1.613 | 0.1068 |  |
| **Age (years)** | **-0.4052** | 0.0593 | ±0.1185 | **-6.837** | **8.11e-12** | *** |
| BMI (kg/m2) | -0.0057 | 0.0875 | ±0.1750 | -0.065 | 0.9483 |  |
| Hypertension | +0.3329 | 1.4812 | ±2.9625 | +0.225 | 0.8222 |  |
| High cholesterol | -0.2535 | 1.2940 | ±2.5880 | -0.196 | 0.8447 |  |
| Kidney disease | -1.3914 | 2.6332 | ±5.2663 | -0.528 | 0.5972 |  |
| Circulatory disease | -2.4041 | 2.2917 | ±4.5833 | -1.049 | 0.2942 |  |
| Avg. daily time < 54 (%) | +30.2267 | 21.7597 | ±43.5193 | +1.389 | 0.1648 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **344**, R² = **0.1796**, Adj R² = **0.1524**, F-statistic = **6.61** (p = **5.36e-10**), Residual SE = **11.379** on **332** df, AIC = **2661.1**, BIC = **2707.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4081** | 4.9530 | ±9.9059 | **+9.975** | **1.95e-23** | *** |
| Education: graduate level (vs college) | -1.5836 | 1.2754 | ±2.5507 | -1.242 | 0.2144 |  |
| Education: high school or below (vs college) | +2.9031 | 2.8625 | ±5.7250 | +1.014 | 0.3105 |  |
| Site: UCSD (vs UAB) | -1.0461 | 1.6505 | ±3.3011 | -0.634 | 0.5262 |  |
| Site: UW (vs UAB) | -2.4415 | 1.5896 | ±3.1792 | -1.536 | 0.1246 |  |
| **Age (years)** | **-0.4091** | 0.0598 | ±0.1197 | **-6.835** | **8.19e-12** | *** |
| BMI (kg/m2) | +0.0076 | 0.0897 | ±0.1794 | +0.084 | 0.9327 |  |
| Hypertension | +0.6221 | 1.4911 | ±2.9823 | +0.417 | 0.6765 |  |
| High cholesterol | -0.5427 | 1.3355 | ±2.6709 | -0.406 | 0.6844 |  |
| Kidney disease | -1.3857 | 2.5984 | ±5.1969 | -0.533 | 0.5938 |  |
| Circulatory disease | -1.8747 | 2.2103 | ±4.4206 | -0.848 | 0.3963 |  |
| Time 54-69, pooled (%) | +4.6779 | 3.4353 | ±6.8706 | +1.362 | 0.1733 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **344**, R² = **0.1779**, Adj R² = **0.1506**, F-statistic = **6.53** (p = **7.34e-10**), Residual SE = **11.391** on **332** df, AIC = **2661.8**, BIC = **2707.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.7169** | 4.9136 | ±9.8273 | **+10.118** | **4.59e-24** | *** |
| Education: graduate level (vs college) | -1.5729 | 1.2737 | ±2.5474 | -1.235 | 0.2169 |  |
| Education: high school or below (vs college) | +2.9338 | 2.8711 | ±5.7423 | +1.022 | 0.3069 |  |
| Site: UCSD (vs UAB) | -1.1349 | 1.6572 | ±3.3143 | -0.685 | 0.4935 |  |
| Site: UW (vs UAB) | -2.5673 | 1.5937 | ±3.1874 | -1.611 | 0.1072 |  |
| **Age (years)** | **-0.4092** | 0.0598 | ±0.1196 | **-6.842** | **7.78e-12** | *** |
| BMI (kg/m2) | +0.0054 | 0.0896 | ±0.1793 | +0.060 | 0.9518 |  |
| Hypertension | +0.6810 | 1.5159 | ±3.0318 | +0.449 | 0.6532 |  |
| High cholesterol | -0.4479 | 1.3310 | ±2.6620 | -0.337 | 0.7365 |  |
| Kidney disease | -1.4408 | 2.6193 | ±5.2386 | -0.550 | 0.5823 |  |
| Circulatory disease | -1.9631 | 2.2109 | ±4.4219 | -0.888 | 0.3746 |  |
| Avg. daily time 54-69 (%) | +3.7211 | 3.5306 | ±7.0613 | +1.054 | 0.2919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **344**, R² = **0.1816**, Adj R² = **0.1545**, F-statistic = **6.70** (p = **3.78e-10**), Residual SE = **11.366** on **332** df, AIC = **2660.3**, BIC = **2706.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.2503** | 4.9549 | ±9.9098 | **+9.940** | **2.80e-23** | *** |
| Education: graduate level (vs college) | -1.5715 | 1.2768 | ±2.5535 | -1.231 | 0.2184 |  |
| Education: high school or below (vs college) | +2.9552 | 2.8582 | ±5.7164 | +1.034 | 0.3012 |  |
| Site: UCSD (vs UAB) | -0.9590 | 1.6480 | ±3.2959 | -0.582 | 0.5606 |  |
| Site: UW (vs UAB) | -2.3920 | 1.5871 | ±3.1742 | -1.507 | 0.1318 |  |
| **Age (years)** | **-0.4080** | 0.0598 | ±0.1195 | **-6.826** | **8.71e-12** | *** |
| BMI (kg/m2) | +0.0051 | 0.0891 | ±0.1783 | +0.057 | 0.9548 |  |
| Hypertension | +0.5907 | 1.4906 | ±2.9812 | +0.396 | 0.6919 |  |
| High cholesterol | -0.5473 | 1.3323 | ±2.6645 | -0.411 | 0.6812 |  |
| Kidney disease | -1.3195 | 2.5997 | ±5.1994 | -0.508 | 0.6118 |  |
| Circulatory disease | -1.9446 | 2.2277 | ±4.4554 | -0.873 | 0.3827 |  |
| Time < 70 (%) | +4.9604 | 3.3134 | ±6.6269 | +1.497 | 0.1344 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **344**, R² = **0.1801**, Adj R² = **0.1530**, F-statistic = **6.63** (p = **4.89e-10**), Residual SE = **11.376** on **332** df, AIC = **2660.9**, BIC = **2707.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5601** | 4.9078 | ±9.8155 | **+10.098** | **5.62e-24** | *** |
| Education: graduate level (vs college) | -1.5634 | 1.2764 | ±2.5528 | -1.225 | 0.2206 |  |
| Education: high school or below (vs college) | +2.9326 | 2.8646 | ±5.7293 | +1.024 | 0.3060 |  |
| Site: UCSD (vs UAB) | -1.0902 | 1.6515 | ±3.3030 | -0.660 | 0.5092 |  |
| Site: UW (vs UAB) | -2.5506 | 1.5913 | ±3.1826 | -1.603 | 0.1090 |  |
| **Age (years)** | **-0.4089** | 0.0597 | ±0.1193 | **-6.853** | **7.23e-12** | *** |
| BMI (kg/m2) | +0.0043 | 0.0895 | ±0.1790 | +0.048 | 0.9616 |  |
| Hypertension | +0.7232 | 1.5182 | ±3.0363 | +0.476 | 0.6338 |  |
| High cholesterol | -0.4663 | 1.3266 | ±2.6531 | -0.352 | 0.7252 |  |
| Kidney disease | -1.3905 | 2.6195 | ±5.2391 | -0.531 | 0.5955 |  |
| Circulatory disease | -2.0556 | 2.2276 | ±4.4552 | -0.923 | 0.3561 |  |
| Avg. daily time < 70 (%) | +4.5053 | 3.4745 | ±6.9489 | +1.297 | 0.1947 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **344**, R² = **0.1816**, Adj R² = **0.1545**, F-statistic = **6.70** (p = **3.75e-10**), Residual SE = **11.365** on **332** df, AIC = **2660.2**, BIC = **2706.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1961.2092 | 1757.3670 | ±3514.7339 | +1.116 | 0.2644 |  |
| Education: graduate level (vs college) | -1.6211 | 1.2802 | ±2.5605 | -1.266 | 0.2054 |  |
| Education: high school or below (vs college) | +3.2517 | 2.8828 | ±5.7656 | +1.128 | 0.2593 |  |
| Site: UCSD (vs UAB) | -0.8990 | 1.6768 | ±3.3535 | -0.536 | 0.5919 |  |
| Site: UW (vs UAB) | -2.4746 | 1.5922 | ±3.1845 | -1.554 | 0.1201 |  |
| **Age (years)** | **-0.4038** | 0.0597 | ±0.1195 | **-6.760** | **1.38e-11** | *** |
| BMI (kg/m2) | -0.0058 | 0.0868 | ±0.1736 | -0.067 | 0.9464 |  |
| Hypertension | +0.2575 | 1.4872 | ±2.9743 | +0.173 | 0.8626 |  |
| High cholesterol | -0.3010 | 1.3020 | ±2.6040 | -0.231 | 0.8172 |  |
| Kidney disease | -1.3431 | 2.6320 | ±5.2640 | -0.510 | 0.6098 |  |
| Circulatory disease | -2.1600 | 2.2618 | ±4.5236 | -0.955 | 0.3396 |  |
| Time 54-250, pooled (%) | -19.1141 | 17.5785 | ±35.1571 | -1.087 | 0.2769 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **344**, R² = **0.1864**, Adj R² = **0.1595**, F-statistic = **6.92** (p = **1.58e-10**), Residual SE = **11.332** on **332** df, AIC = **2658.2**, BIC = **2704.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3041.5028 | 2140.6400 | ±4281.2800 | +1.421 | 0.1554 |  |
| Education: graduate level (vs college) | -1.7027 | 1.2653 | ±2.5305 | -1.346 | 0.1784 |  |
| Education: high school or below (vs college) | +3.1371 | 2.8581 | ±5.7162 | +1.098 | 0.2724 |  |
| Site: UCSD (vs UAB) | -0.9932 | 1.6570 | ±3.3139 | -0.599 | 0.5489 |  |
| Site: UW (vs UAB) | -2.5876 | 1.5935 | ±3.1869 | -1.624 | 0.1044 |  |
| **Age (years)** | **-0.4040** | 0.0593 | ±0.1186 | **-6.815** | **9.45e-12** | *** |
| BMI (kg/m2) | -0.0041 | 0.0878 | ±0.1757 | -0.047 | 0.9624 |  |
| Hypertension | +0.3445 | 1.4820 | ±2.9639 | +0.232 | 0.8162 |  |
| High cholesterol | -0.2887 | 1.2956 | ±2.5912 | -0.223 | 0.8237 |  |
| Kidney disease | -1.3889 | 2.6331 | ±5.2662 | -0.527 | 0.5979 |  |
| Circulatory disease | -2.3965 | 2.2920 | ±4.5839 | -1.046 | 0.2958 |  |
| Avg. daily time 54-250 (%) | -29.9161 | 21.4091 | ±42.8181 | -1.397 | 0.1623 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **344**, R² = **0.1838**, Adj R² = **0.1567**, F-statistic = **6.80** (p = **2.55e-10**), Residual SE = **11.350** on **332** df, AIC = **2659.3**, BIC = **2705.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5733** | 5.1450 | ±10.2900 | **+9.441** | **3.70e-21** | *** |
| Education: graduate level (vs college) | -1.6393 | 1.2712 | ±2.5424 | -1.290 | 0.1972 |  |
| Education: high school or below (vs college) | +3.2118 | 2.8535 | ±5.7070 | +1.126 | 0.2604 |  |
| Site: UCSD (vs UAB) | -1.1821 | 1.6712 | ±3.3425 | -0.707 | 0.4794 |  |
| Site: UW (vs UAB) | -2.6352 | 1.5808 | ±3.1616 | -1.667 | 0.0955 | . |
| **Age (years)** | **-0.4035** | 0.0598 | ±0.1196 | **-6.746** | **1.52e-11** | *** |
| BMI (kg/m2) | +0.0094 | 0.0969 | ±0.1939 | +0.097 | 0.9224 |  |
| Hypertension | +0.2430 | 1.4801 | ±2.9602 | +0.164 | 0.8696 |  |
| High cholesterol | -0.2091 | 1.3089 | ±2.6179 | -0.160 | 0.8731 |  |
| Kidney disease | -1.9701 | 2.7240 | ±5.4481 | -0.723 | 0.4695 |  |
| Circulatory disease | -1.9087 | 2.1657 | ±4.3315 | -0.881 | 0.3781 |  |
| Time 181-250, pooled (%) | +4.1714 | 2.2280 | ±4.4560 | +1.872 | 0.0612 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **344**, R² = **0.1865**, Adj R² = **0.1595**, F-statistic = **6.92** (p = **1.57e-10**), Residual SE = **11.332** on **332** df, AIC = **2658.2**, BIC = **2704.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.3009** | 4.9413 | ±9.8826 | **+9.775** | **1.44e-22** | *** |
| Education: graduate level (vs college) | -1.6377 | 1.2668 | ±2.5336 | -1.293 | 0.1961 |  |
| Education: high school or below (vs college) | +3.3509 | 2.8483 | ±5.6966 | +1.176 | 0.2394 |  |
| Site: UCSD (vs UAB) | -1.1012 | 1.6607 | ±3.3213 | -0.663 | 0.5072 |  |
| Site: UW (vs UAB) | -2.6364 | 1.5754 | ±3.1508 | -1.673 | 0.0942 | . |
| **Age (years)** | **-0.3972** | 0.0594 | ±0.1188 | **-6.685** | **2.30e-11** | *** |
| BMI (kg/m2) | +0.0054 | 0.0913 | ±0.1827 | +0.059 | 0.9526 |  |
| Hypertension | +0.2342 | 1.4821 | ±2.9643 | +0.158 | 0.8744 |  |
| High cholesterol | -0.3037 | 1.2987 | ±2.5974 | -0.234 | 0.8151 |  |
| Kidney disease | -1.7729 | 2.6920 | ±5.3840 | -0.659 | 0.5102 |  |
| Circulatory disease | -1.9251 | 2.1541 | ±4.3081 | -0.894 | 0.3715 |  |
| **Avg. daily time 181-250 (%)** | **+4.7044** | 2.1745 | ±4.3490 | **+2.163** | **0.0305** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **344**, R² = **0.1838**, Adj R² = **0.1567**, F-statistic = **6.80** (p = **2.55e-10**), Residual SE = **11.350** on **332** df, AIC = **2659.3**, BIC = **2705.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.5586** | 5.1497 | ±10.2993 | **+9.429** | **4.12e-21** | *** |
| Education: graduate level (vs college) | -1.6355 | 1.2712 | ±2.5423 | -1.287 | 0.1982 |  |
| Education: high school or below (vs college) | +3.2144 | 2.8534 | ±5.7069 | +1.127 | 0.2599 |  |
| Site: UCSD (vs UAB) | -1.1818 | 1.6713 | ±3.3426 | -0.707 | 0.4795 |  |
| Site: UW (vs UAB) | -2.6377 | 1.5808 | ±3.1616 | -1.669 | 0.0952 | . |
| **Age (years)** | **-0.4033** | 0.0598 | ±0.1196 | **-6.743** | **1.55e-11** | *** |
| BMI (kg/m2) | +0.0096 | 0.0970 | ±0.1940 | +0.099 | 0.9210 |  |
| Hypertension | +0.2445 | 1.4801 | ±2.9602 | +0.165 | 0.8688 |  |
| High cholesterol | -0.2135 | 1.3085 | ±2.6169 | -0.163 | 0.8704 |  |
| Kidney disease | -1.9693 | 2.7239 | ±5.4477 | -0.723 | 0.4697 |  |
| Circulatory disease | -1.9084 | 2.1660 | ±4.3319 | -0.881 | 0.3783 |  |
| Time > 180 (%) | +4.1685 | 2.2229 | ±4.4458 | +1.875 | 0.0608 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **344**, R² = **0.1865**, Adj R² = **0.1595**, F-statistic = **6.92** (p = **1.57e-10**), Residual SE = **11.332** on **332** df, AIC = **2658.2**, BIC = **2704.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.2838** | 4.9456 | ±9.8911 | **+9.763** | **1.62e-22** | *** |
| Education: graduate level (vs college) | -1.6330 | 1.2667 | ±2.5335 | -1.289 | 0.1974 |  |
| Education: high school or below (vs college) | +3.3539 | 2.8482 | ±5.6965 | +1.178 | 0.2390 |  |
| Site: UCSD (vs UAB) | -1.1010 | 1.6607 | ±3.3215 | -0.663 | 0.5073 |  |
| Site: UW (vs UAB) | -2.6394 | 1.5754 | ±3.1509 | -1.675 | 0.0939 | . |
| **Age (years)** | **-0.3971** | 0.0594 | ±0.1189 | **-6.681** | **2.37e-11** | *** |
| BMI (kg/m2) | +0.0057 | 0.0914 | ±0.1828 | +0.062 | 0.9506 |  |
| Hypertension | +0.2361 | 1.4822 | ±2.9643 | +0.159 | 0.8734 |  |
| High cholesterol | -0.3092 | 1.2983 | ±2.5967 | -0.238 | 0.8118 |  |
| Kidney disease | -1.7719 | 2.6918 | ±5.3836 | -0.658 | 0.5104 |  |
| Circulatory disease | -1.9247 | 2.1543 | ±4.3087 | -0.893 | 0.3716 |  |
| **Avg. daily time > 180 (%)** | **+4.6981** | 2.1679 | ±4.3359 | **+2.167** | **0.0302** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 344)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **344**, R² = **0.1786**, Adj R² = **0.1514**, F-statistic = **6.56** (p = **6.45e-10**), Residual SE = **11.386** on **332** df, AIC = **2661.5**, BIC = **2707.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.5422** | 4.8325 | ±9.6650 | **+10.252** | **1.16e-24** | *** |
| Education: graduate level (vs college) | -1.5432 | 1.2713 | ±2.5425 | -1.214 | 0.2248 |  |
| Education: high school or below (vs college) | +3.0055 | 2.8396 | ±5.6792 | +1.058 | 0.2899 |  |
| Site: UCSD (vs UAB) | -1.1621 | 1.6660 | ±3.3320 | -0.698 | 0.4855 |  |
| Site: UW (vs UAB) | -2.6837 | 1.5912 | ±3.1823 | -1.687 | 0.0917 | . |
| **Age (years)** | **-0.3940** | 0.0603 | ±0.1207 | **-6.530** | **6.57e-11** | *** |
| BMI (kg/m2) | -0.0079 | 0.0888 | ±0.1776 | -0.089 | 0.9290 |  |
| Hypertension | +0.3178 | 1.4795 | ±2.9590 | +0.215 | 0.8299 |  |
| High cholesterol | -0.4208 | 1.2909 | ±2.5817 | -0.326 | 0.7445 |  |
| Kidney disease | -1.7269 | 2.6441 | ±5.2883 | -0.653 | 0.5137 |  |
| Circulatory disease | -1.8655 | 2.2206 | ±4.4412 | -0.840 | 0.4008 |  |
| Nocturnal time > 180 (%) | +2.1469 | 2.1711 | ±4.3422 | +0.989 | 0.3227 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 346; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1548**, F-statistic = **7.32** (p = **1.70e-10**), Residual SE = **6.667** on **335** df, AIC = **2305.5**, BIC = **2347.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8265** | 3.9998 | ±7.9996 | **+15.707** | **1.35e-55** | *** |
| **Education: graduate level (vs college)** | **-1.7812** | 0.7764 | ±1.5528 | **-2.294** | **0.0218** | * |
| Education: high school or below (vs college) | -1.8761 | 1.3420 | ±2.6841 | -1.398 | 0.1621 |  |
| **Site: UCSD (vs UAB)** | **-1.9760** | 0.9762 | ±1.9524 | **-2.024** | **0.0430** | * |
| **Site: UW (vs UAB)** | **-2.5729** | 0.8831 | ±1.7662 | **-2.913** | **0.0036** | ** |
| **Age (years)** | **-0.1333** | 0.0368 | ±0.0736 | **-3.624** | **2.91e-04** | *** |
| **BMI (kg/m2)** | **+0.2565** | 0.0812 | ±0.1624 | **+3.159** | **0.0016** | ** |
| Hypertension | +0.9457 | 0.8421 | ±1.6841 | +1.123 | 0.2614 |  |
| High cholesterol | -0.2784 | 0.8174 | ±1.6347 | -0.341 | 0.7334 |  |
| Kidney disease | +0.0608 | 2.1902 | ±4.3805 | +0.028 | 0.9779 |  |
| Circulatory disease | -0.6757 | 1.0045 | ±2.0091 | -0.673 | 0.5012 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **346**, R² = **0.1795**, Adj R² = **0.1525**, F-statistic = **6.64** (p = **4.64e-10**), Residual SE = **6.676** on **334** df, AIC = **2307.5**, BIC = **2353.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.0521** | 7.4315 | ±14.8629 | **+8.215** | **2.12e-16** | *** |
| **Education: graduate level (vs college)** | **-1.7737** | 0.7754 | ±1.5508 | **-2.288** | **0.0222** | * |
| Education: high school or below (vs college) | -1.8839 | 1.3441 | ±2.6882 | -1.402 | 0.1610 |  |
| **Site: UCSD (vs UAB)** | **-1.9599** | 0.9729 | ±1.9458 | **-2.015** | **0.0440** | * |
| **Site: UW (vs UAB)** | **-2.5534** | 0.8841 | ±1.7682 | **-2.888** | **0.0039** | ** |
| **Age (years)** | **-0.1343** | 0.0375 | ±0.0750 | **-3.584** | **3.39e-04** | *** |
| **BMI (kg/m2)** | **+0.2548** | 0.0825 | ±0.1650 | **+3.089** | **0.0020** | ** |
| Hypertension | +0.9273 | 0.8464 | ±1.6928 | +1.096 | 0.2732 |  |
| High cholesterol | -0.3247 | 0.8222 | ±1.6443 | -0.395 | 0.6929 |  |
| Kidney disease | +0.0786 | 2.1899 | ±4.3798 | +0.036 | 0.9714 |  |
| Circulatory disease | -0.6616 | 1.0059 | ±2.0118 | -0.658 | 0.5107 |  |
| HbA1c (%) | +0.3423 | 1.3523 | ±2.7046 | +0.253 | 0.8002 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.79e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8864** | 7.3543 | ±14.7085 | **+8.551** | **1.22e-17** | *** |
| **Education: graduate level (vs college)** | **-1.7814** | 0.7777 | ±1.5554 | **-2.291** | **0.0220** | * |
| Education: high school or below (vs college) | -1.8767 | 1.3525 | ±2.7050 | -1.388 | 0.1653 |  |
| **Site: UCSD (vs UAB)** | **-1.9754** | 0.9822 | ±1.9643 | **-2.011** | **0.0443** | * |
| **Site: UW (vs UAB)** | **-2.5723** | 0.8834 | ±1.7668 | **-2.912** | **0.0036** | ** |
| **Age (years)** | **-0.1333** | 0.0372 | ±0.0743 | **-3.588** | **3.34e-04** | *** |
| **BMI (kg/m2)** | **+0.2565** | 0.0815 | ±0.1630 | **+3.147** | **0.0016** | ** |
| Hypertension | +0.9466 | 0.8443 | ±1.6886 | +1.121 | 0.2622 |  |
| High cholesterol | -0.2787 | 0.8264 | ±1.6528 | -0.337 | 0.7359 |  |
| Kidney disease | +0.0609 | 2.2101 | ±4.4202 | +0.028 | 0.9780 |  |
| Circulatory disease | -0.6757 | 1.0061 | ±2.0122 | -0.672 | 0.5018 |  |
| Mean glucose (mg/dL) | -0.0005 | 0.0521 | ±0.1042 | -0.010 | 0.9919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.79e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.9596** | 13.9642 | ±27.9285 | **+4.509** | **6.52e-06** | *** |
| **Education: graduate level (vs college)** | **-1.7814** | 0.7777 | ±1.5554 | **-2.291** | **0.0220** | * |
| Education: high school or below (vs college) | -1.8767 | 1.3525 | ±2.7050 | -1.388 | 0.1653 |  |
| **Site: UCSD (vs UAB)** | **-1.9754** | 0.9822 | ±1.9643 | **-2.011** | **0.0443** | * |
| **Site: UW (vs UAB)** | **-2.5723** | 0.8834 | ±1.7668 | **-2.912** | **0.0036** | ** |
| **Age (years)** | **-0.1333** | 0.0372 | ±0.0743 | **-3.588** | **3.34e-04** | *** |
| **BMI (kg/m2)** | **+0.2565** | 0.0815 | ±0.1630 | **+3.147** | **0.0016** | ** |
| Hypertension | +0.9466 | 0.8443 | ±1.6886 | +1.121 | 0.2622 |  |
| High cholesterol | -0.2787 | 0.8264 | ±1.6528 | -0.337 | 0.7359 |  |
| Kidney disease | +0.0609 | 2.2101 | ±4.4202 | +0.028 | 0.9780 |  |
| Circulatory disease | -0.6757 | 1.0061 | ±2.0122 | -0.672 | 0.5018 |  |
| GMI (%) | -0.0221 | 2.1772 | ±4.3544 | -0.010 | 0.9919 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **346**, R² = **0.1805**, Adj R² = **0.1536**, F-statistic = **6.69** (p = **3.83e-10**), Residual SE = **6.672** on **334** df, AIC = **2307.0**, BIC = **2353.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.5751** | 5.8841 | ±11.7681 | **+10.125** | **4.29e-24** | *** |
| **Education: graduate level (vs college)** | **-1.7401** | 0.7709 | ±1.5418 | **-2.257** | **0.0240** | * |
| Education: high school or below (vs college) | -1.8341 | 1.3428 | ±2.6856 | -1.366 | 0.1720 |  |
| **Site: UCSD (vs UAB)** | **-2.0530** | 0.9932 | ±1.9865 | **-2.067** | **0.0387** | * |
| **Site: UW (vs UAB)** | **-2.6303** | 0.8877 | ±1.7753 | **-2.963** | **0.0030** | ** |
| **Age (years)** | **-0.1292** | 0.0375 | ±0.0749 | **-3.449** | **5.62e-04** | *** |
| **BMI (kg/m2)** | **+0.2502** | 0.0821 | ±0.1642 | **+3.047** | **0.0023** | ** |
| Hypertension | +0.9062 | 0.8372 | ±1.6743 | +1.082 | 0.2791 |  |
| High cholesterol | -0.2789 | 0.8211 | ±1.6421 | -0.340 | 0.7341 |  |
| Kidney disease | +0.0988 | 2.2025 | ±4.4050 | +0.045 | 0.9642 |  |
| Circulatory disease | -0.6525 | 1.0022 | ±2.0045 | -0.651 | 0.5150 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0281 | 0.0410 | ±0.0820 | +0.684 | 0.4937 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **346**, R² = **0.1794**, Adj R² = **0.1523**, F-statistic = **6.64** (p = **4.73e-10**), Residual SE = **6.676** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.3639** | 4.9353 | ±9.8707 | **+12.636** | **1.33e-36** | *** |
| **Education: graduate level (vs college)** | **-1.7688** | 0.7762 | ±1.5525 | **-2.279** | **0.0227** | * |
| Education: high school or below (vs college) | -1.8673 | 1.3444 | ±2.6889 | -1.389 | 0.1649 |  |
| **Site: UCSD (vs UAB)** | **-1.9620** | 0.9779 | ±1.9558 | **-2.006** | **0.0448** | * |
| **Site: UW (vs UAB)** | **-2.5638** | 0.8849 | ±1.7697 | **-2.897** | **0.0038** | ** |
| **Age (years)** | **-0.1334** | 0.0369 | ±0.0738 | **-3.616** | **3.00e-04** | *** |
| **BMI (kg/m2)** | **+0.2561** | 0.0814 | ±0.1628 | **+3.146** | **0.0017** | ** |
| Hypertension | +0.9414 | 0.8427 | ±1.6854 | +1.117 | 0.2640 |  |
| High cholesterol | -0.2689 | 0.8378 | ±1.6756 | -0.321 | 0.7482 |  |
| Kidney disease | +0.0386 | 2.2679 | ±4.5359 | +0.017 | 0.9864 |  |
| Circulatory disease | -0.6797 | 1.0037 | ±2.0073 | -0.677 | 0.4983 |  |
| Glucose SD, pooled (mg/dL) | +0.0274 | 0.1776 | ±0.3552 | +0.154 | 0.8772 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **346**, R² = **0.1794**, Adj R² = **0.1523**, F-statistic = **6.64** (p = **4.72e-10**), Residual SE = **6.676** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.3702** | 4.6800 | ±9.3599 | **+13.327** | **1.61e-40** | *** |
| **Education: graduate level (vs college)** | **-1.7672** | 0.7760 | ±1.5520 | **-2.277** | **0.0228** | * |
| Education: high school or below (vs college) | -1.8641 | 1.3445 | ±2.6891 | -1.386 | 0.1656 |  |
| **Site: UCSD (vs UAB)** | **-1.9590** | 0.9761 | ±1.9523 | **-2.007** | **0.0448** | * |
| **Site: UW (vs UAB)** | **-2.5617** | 0.8848 | ±1.7695 | **-2.895** | **0.0038** | ** |
| **Age (years)** | **-0.1333** | 0.0369 | ±0.0738 | **-3.613** | **3.03e-04** | *** |
| **BMI (kg/m2)** | **+0.2558** | 0.0817 | ±0.1634 | **+3.132** | **0.0017** | ** |
| Hypertension | +0.9443 | 0.8440 | ±1.6880 | +1.119 | 0.2632 |  |
| High cholesterol | -0.2698 | 0.8325 | ±1.6651 | -0.324 | 0.7459 |  |
| Kidney disease | +0.0378 | 2.2562 | ±4.5125 | +0.017 | 0.9866 |  |
| Circulatory disease | -0.6769 | 1.0051 | ±2.0102 | -0.673 | 0.5006 |  |
| Avg. daily SD (mg/dL) | +0.0295 | 0.1719 | ±0.3438 | +0.171 | 0.8639 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.78e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5812** | 4.6178 | ±9.2356 | **+13.552** | **7.69e-42** | *** |
| **Education: graduate level (vs college)** | **-1.7754** | 0.7769 | ±1.5539 | **-2.285** | **0.0223** | * |
| Education: high school or below (vs college) | -1.8736 | 1.3430 | ±2.6861 | -1.395 | 0.1630 |  |
| **Site: UCSD (vs UAB)** | **-1.9666** | 0.9782 | ±1.9564 | **-2.010** | **0.0444** | * |
| **Site: UW (vs UAB)** | **-2.5657** | 0.8824 | ±1.7647 | **-2.908** | **0.0036** | ** |
| **Age (years)** | **-0.1334** | 0.0369 | ±0.0739 | **-3.611** | **3.05e-04** | *** |
| **BMI (kg/m2)** | **+0.2564** | 0.0812 | ±0.1625 | **+3.156** | **0.0016** | ** |
| Hypertension | +0.9467 | 0.8452 | ±1.6904 | +1.120 | 0.2627 |  |
| High cholesterol | -0.2744 | 0.8284 | ±1.6568 | -0.331 | 0.7404 |  |
| Kidney disease | +0.0501 | 2.2350 | ±4.4700 | +0.022 | 0.9821 |  |
| Circulatory disease | -0.6781 | 1.0037 | ±2.0073 | -0.676 | 0.4993 |  |
| CV (%) | +0.0164 | 0.1712 | ±0.3423 | +0.096 | 0.9238 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.79e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.7889** | 4.6964 | ±9.3928 | **+13.370** | **9.11e-41** | *** |
| **Education: graduate level (vs college)** | **-1.7823** | 0.7788 | ±1.5575 | **-2.289** | **0.0221** | * |
| Education: high school or below (vs college) | -1.8765 | 1.3446 | ±2.6892 | -1.396 | 0.1628 |  |
| **Site: UCSD (vs UAB)** | **-1.9772** | 0.9793 | ±1.9586 | **-2.019** | **0.0435** | * |
| **Site: UW (vs UAB)** | **-2.5738** | 0.8836 | ±1.7673 | **-2.913** | **0.0036** | ** |
| **Age (years)** | **-0.1333** | 0.0369 | ±0.0738 | **-3.613** | **3.02e-04** | *** |
| **BMI (kg/m2)** | **+0.2565** | 0.0813 | ±0.1625 | **+3.156** | **0.0016** | ** |
| Hypertension | +0.9458 | 0.8440 | ±1.6881 | +1.121 | 0.2625 |  |
| High cholesterol | -0.2791 | 0.8295 | ±1.6590 | -0.336 | 0.7365 |  |
| Kidney disease | +0.0621 | 2.2236 | ±4.4472 | +0.028 | 0.9777 |  |
| Circulatory disease | -0.6754 | 1.0044 | ±2.0088 | -0.672 | 0.5013 |  |
| Mean / SD ratio | +0.0055 | 0.3430 | ±0.6859 | +0.016 | 0.9871 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.79e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.9665** | 4.6440 | ±9.2879 | **+13.559** | **7.03e-42** | *** |
| **Education: graduate level (vs college)** | **-1.7766** | 0.7785 | ±1.5569 | **-2.282** | **0.0225** | * |
| Education: high school or below (vs college) | -1.8741 | 1.3438 | ±2.6877 | -1.395 | 0.1631 |  |
| **Site: UCSD (vs UAB)** | **-1.9703** | 0.9781 | ±1.9562 | **-2.014** | **0.0440** | * |
| **Site: UW (vs UAB)** | **-2.5691** | 0.8819 | ±1.7639 | **-2.913** | **0.0036** | ** |
| **Age (years)** | **-0.1333** | 0.0369 | ±0.0738 | **-3.615** | **3.00e-04** | *** |
| **BMI (kg/m2)** | **+0.2563** | 0.0815 | ±0.1630 | **+3.145** | **0.0017** | ** |
| Hypertension | +0.9469 | 0.8465 | ±1.6931 | +1.119 | 0.2633 |  |
| High cholesterol | -0.2763 | 0.8249 | ±1.6498 | -0.335 | 0.7377 |  |
| Kidney disease | +0.0547 | 2.2209 | ±4.4418 | +0.025 | 0.9803 |  |
| Circulatory disease | -0.6762 | 1.0056 | ±2.0112 | -0.672 | 0.5013 |  |
| Avg. daily mean/SD | -0.0181 | 0.2705 | ±0.5410 | -0.067 | 0.9466 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **346**, R² = **0.1862**, Adj R² = **0.1594**, F-statistic = **6.95** (p = **1.37e-10**), Residual SE = **6.648** on **334** df, AIC = **2304.6**, BIC = **2350.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.4647** | 4.7913 | ±9.5826 | **+12.202** | **3.02e-34** | *** |
| **Education: graduate level (vs college)** | **-1.7791** | 0.7790 | ±1.5580 | **-2.284** | **0.0224** | * |
| Education: high school or below (vs college) | -2.0366 | 1.3003 | ±2.6007 | -1.566 | 0.1173 |  |
| Site: UCSD (vs UAB) | -1.8442 | 0.9719 | ±1.9438 | -1.898 | 0.0578 | . |
| **Site: UW (vs UAB)** | **-2.3756** | 0.8973 | ±1.7947 | **-2.647** | **0.0081** | ** |
| **Age (years)** | **-0.1254** | 0.0372 | ±0.0743 | **-3.375** | **7.38e-04** | *** |
| **BMI (kg/m2)** | **+0.2629** | 0.0797 | ±0.1594 | **+3.299** | **9.72e-04** | *** |
| Hypertension | +1.0271 | 0.8392 | ±1.6783 | +1.224 | 0.2210 |  |
| High cholesterol | -0.3637 | 0.8160 | ±1.6321 | -0.446 | 0.6559 |  |
| Kidney disease | -0.1601 | 2.2028 | ±4.4056 | -0.073 | 0.9420 |  |
| Circulatory disease | -0.7272 | 1.0048 | ±2.0096 | -0.724 | 0.4693 |  |
| MAG (mg/dL/h) | +0.1061 | 0.0692 | ±0.1384 | +1.534 | 0.1251 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.76e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.1829** | 5.3169 | ±10.6338 | **+11.883** | **1.44e-32** | *** |
| **Education: graduate level (vs college)** | **-1.7855** | 0.7801 | ±1.5602 | **-2.289** | **0.0221** | * |
| Education: high school or below (vs college) | -1.8803 | 1.3496 | ±2.6991 | -1.393 | 0.1635 |  |
| **Site: UCSD (vs UAB)** | **-1.9851** | 0.9823 | ±1.9646 | **-2.021** | **0.0433** | * |
| **Site: UW (vs UAB)** | **-2.5802** | 0.8915 | ±1.7831 | **-2.894** | **0.0038** | ** |
| **Age (years)** | **-0.1335** | 0.0370 | ±0.0739 | **-3.610** | **3.06e-04** | *** |
| **BMI (kg/m2)** | **+0.2560** | 0.0817 | ±0.1635 | **+3.132** | **0.0017** | ** |
| Hypertension | +0.9411 | 0.8504 | ±1.7008 | +1.107 | 0.2684 |  |
| High cholesterol | -0.2794 | 0.8221 | ±1.6442 | -0.340 | 0.7339 |  |
| Kidney disease | +0.0714 | 2.2241 | ±4.4483 | +0.032 | 0.9744 |  |
| Circulatory disease | -0.6708 | 1.0045 | ±2.0089 | -0.668 | 0.5042 |  |
| Avg. daily range (mg/dL) | -0.0041 | 0.0359 | ±0.0718 | -0.113 | 0.9098 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **346**, R² = **0.1888**, Adj R² = **0.1621**, F-statistic = **7.07** (p = **8.50e-11**), Residual SE = **6.638** on **334** df, AIC = **2303.5**, BIC = **2349.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.0891** | 3.9770 | ±7.9539 | **+15.361** | **3.00e-53** | *** |
| **Education: graduate level (vs college)** | **-1.8332** | 0.7729 | ±1.5457 | **-2.372** | **0.0177** | * |
| Education: high school or below (vs college) | -1.9812 | 1.3507 | ±2.7014 | -1.467 | 0.1424 |  |
| **Site: UCSD (vs UAB)** | **-1.9305** | 0.9694 | ±1.9387 | **-1.992** | **0.0464** | * |
| **Site: UW (vs UAB)** | **-2.6553** | 0.8718 | ±1.7437 | **-3.046** | **0.0023** | ** |
| **Age (years)** | **-0.1364** | 0.0361 | ±0.0722 | **-3.776** | **1.59e-04** | *** |
| **BMI (kg/m2)** | **+0.2548** | 0.0801 | ±0.1602 | **+3.181** | **0.0015** | ** |
| Hypertension | +0.8299 | 0.8447 | ±1.6894 | +0.982 | 0.3259 |  |
| High cholesterol | -0.2784 | 0.8120 | ±1.6241 | -0.343 | 0.7317 |  |
| Kidney disease | +0.1506 | 2.1573 | ±4.3146 | +0.070 | 0.9444 |  |
| Circulatory disease | -0.7310 | 1.0149 | ±2.0299 | -0.720 | 0.4714 |  |
| SD of daily means (mg/dL) | +0.4033 | 0.2205 | ±0.4411 | +1.829 | 0.0674 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **346**, R² = **0.1802**, Adj R² = **0.1532**, F-statistic = **6.67** (p = **4.06e-10**), Residual SE = **6.673** on **334** df, AIC = **2307.2**, BIC = **2353.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +137.2208 | 128.5758 | ±257.1516 | +1.067 | 0.2859 |  |
| **Education: graduate level (vs college)** | **-1.7610** | 0.7861 | ±1.5723 | **-2.240** | **0.0251** | * |
| Education: high school or below (vs college) | -1.8495 | 1.3379 | ±2.6759 | -1.382 | 0.1669 |  |
| Site: UCSD (vs UAB) | -1.9380 | 0.9896 | ±1.9793 | -1.958 | 0.0502 | . |
| **Site: UW (vs UAB)** | **-2.5471** | 0.8881 | ±1.7761 | **-2.868** | **0.0041** | ** |
| **Age (years)** | **-0.1322** | 0.0372 | ±0.0744 | **-3.556** | **3.76e-04** | *** |
| **BMI (kg/m2)** | **+0.2578** | 0.0846 | ±0.1693 | **+3.045** | **0.0023** | ** |
| Hypertension | +0.9369 | 0.8402 | ±1.6805 | +1.115 | 0.2648 |  |
| High cholesterol | -0.2928 | 0.8140 | ±1.6280 | -0.360 | 0.7191 |  |
| Kidney disease | +0.0216 | 2.2176 | ±4.4352 | +0.010 | 0.9922 |  |
| Circulatory disease | -0.6892 | 1.0016 | ±2.0032 | -0.688 | 0.4914 |  |
| Time in range 70-180, pooled (%) | -0.7486 | 1.3000 | ±2.5999 | -0.576 | 0.5647 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **346**, R² = **0.1822**, Adj R² = **0.1552**, F-statistic = **6.76** (p = **2.85e-10**), Residual SE = **6.665** on **334** df, AIC = **2306.3**, BIC = **2352.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +190.5311 | 116.3264 | ±232.6528 | +1.638 | 0.1014 |  |
| **Education: graduate level (vs college)** | **-1.7436** | 0.7800 | ±1.5599 | **-2.235** | **0.0254** | * |
| Education: high school or below (vs college) | -1.8086 | 1.3252 | ±2.6504 | -1.365 | 0.1723 |  |
| **Site: UCSD (vs UAB)** | **-1.9175** | 0.9739 | ±1.9477 | **-1.969** | **0.0490** | * |
| **Site: UW (vs UAB)** | **-2.5668** | 0.8822 | ±1.7644 | **-2.909** | **0.0036** | ** |
| **Age (years)** | **-0.1302** | 0.0368 | ±0.0737 | **-3.535** | **4.08e-04** | *** |
| **BMI (kg/m2)** | **+0.2574** | 0.0821 | ±0.1641 | **+3.136** | **0.0017** | ** |
| Hypertension | +0.9768 | 0.8419 | ±1.6837 | +1.160 | 0.2460 |  |
| High cholesterol | -0.3168 | 0.8111 | ±1.6223 | -0.391 | 0.6961 |  |
| Kidney disease | +0.0477 | 2.1982 | ±4.3964 | +0.022 | 0.9827 |  |
| Circulatory disease | -0.7354 | 0.9944 | ±1.9887 | -0.740 | 0.4596 |  |
| Avg. daily time in range 70-180 (%) | -1.2846 | 1.1693 | ±2.3387 | -1.099 | 0.2720 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **346**, R² = **0.1796**, Adj R² = **0.1525**, F-statistic = **6.64** (p = **4.58e-10**), Residual SE = **6.676** on **334** df, AIC = **2307.4**, BIC = **2353.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.7505** | 3.9932 | ±7.9865 | **+15.714** | **1.21e-55** | *** |
| **Education: graduate level (vs college)** | **-1.7769** | 0.7790 | ±1.5580 | **-2.281** | **0.0225** | * |
| Education: high school or below (vs college) | -1.8665 | 1.3472 | ±2.6944 | -1.385 | 0.1659 |  |
| **Site: UCSD (vs UAB)** | **-1.9291** | 0.9818 | ±1.9637 | **-1.965** | **0.0494** | * |
| **Site: UW (vs UAB)** | **-2.5455** | 0.8894 | ±1.7787 | **-2.862** | **0.0042** | ** |
| **Age (years)** | **-0.1334** | 0.0368 | ±0.0737 | **-3.620** | **2.94e-04** | *** |
| **BMI (kg/m2)** | **+0.2565** | 0.0810 | ±0.1621 | **+3.165** | **0.0016** | ** |
| Hypertension | +0.9288 | 0.8469 | ±1.6939 | +1.097 | 0.2728 |  |
| High cholesterol | -0.2750 | 0.8188 | ±1.6375 | -0.336 | 0.7370 |  |
| Kidney disease | +0.0932 | 2.1961 | ±4.3923 | +0.042 | 0.9662 |  |
| Circulatory disease | -0.6956 | 1.0093 | ±2.0187 | -0.689 | 0.4907 |  |
| Any reading < 54 during wear (0/1) | +0.3138 | 0.8932 | ±1.7864 | +0.351 | 0.7254 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **346**, R² = **0.1862**, Adj R² = **0.1594**, F-statistic = **6.95** (p = **1.37e-10**), Residual SE = **6.648** on **334** df, AIC = **2304.6**, BIC = **2350.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5794** | 3.9144 | ±7.8288 | **+15.987** | **1.58e-57** | *** |
| **Education: graduate level (vs college)** | **-1.7652** | 0.7736 | ±1.5473 | **-2.282** | **0.0225** | * |
| Education: high school or below (vs college) | -1.7401 | 1.3498 | ±2.6996 | -1.289 | 0.1973 |  |
| Site: UCSD (vs UAB) | -1.7928 | 0.9778 | ±1.9557 | -1.833 | 0.0667 | . |
| **Site: UW (vs UAB)** | **-2.4830** | 0.8770 | ±1.7539 | **-2.831** | **0.0046** | ** |
| **Age (years)** | **-0.1308** | 0.0366 | ±0.0731 | **-3.579** | **3.45e-04** | *** |
| **BMI (kg/m2)** | **+0.2502** | 0.0793 | ±0.1586 | **+3.155** | **0.0016** | ** |
| Hypertension | +0.8414 | 0.8461 | ±1.6922 | +0.994 | 0.3200 |  |
| High cholesterol | -0.2564 | 0.8157 | ±1.6314 | -0.314 | 0.7533 |  |
| Kidney disease | +0.1899 | 2.1957 | ±4.3914 | +0.086 | 0.9311 |  |
| Circulatory disease | -0.8422 | 1.0181 | ±2.0361 | -0.827 | 0.4081 |  |
| **Time < 54 (%)** | **+11.6204** | 5.7971 | ±11.5942 | **+2.005** | **0.0450** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **346**, R² = **0.1811**, Adj R² = **0.1541**, F-statistic = **6.71** (p = **3.49e-10**), Residual SE = **6.670** on **334** df, AIC = **2306.8**, BIC = **2353.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.7666** | 3.9720 | ±7.9440 | **+15.802** | **3.00e-56** | *** |
| **Education: graduate level (vs college)** | **-1.7971** | 0.7782 | ±1.5563 | **-2.309** | **0.0209** | * |
| Education: high school or below (vs college) | -1.8527 | 1.3384 | ±2.6769 | -1.384 | 0.1663 |  |
| **Site: UCSD (vs UAB)** | **-1.9277** | 0.9781 | ±1.9562 | **-1.971** | **0.0487** | * |
| **Site: UW (vs UAB)** | **-2.5627** | 0.8838 | ±1.7675 | **-2.900** | **0.0037** | ** |
| **Age (years)** | **-0.1325** | 0.0367 | ±0.0734 | **-3.610** | **3.07e-04** | *** |
| **BMI (kg/m2)** | **+0.2543** | 0.0806 | ±0.1612 | **+3.155** | **0.0016** | ** |
| Hypertension | +0.9250 | 0.8428 | ±1.6857 | +1.098 | 0.2724 |  |
| High cholesterol | -0.2636 | 0.8190 | ±1.6380 | -0.322 | 0.7475 |  |
| Kidney disease | +0.0994 | 2.1938 | ±4.3876 | +0.045 | 0.9638 |  |
| Circulatory disease | -0.7953 | 1.0216 | ±2.0433 | -0.778 | 0.4363 |  |
| Avg. daily time < 54 (%) | +7.0047 | 8.5989 | ±17.1978 | +0.815 | 0.4153 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.79e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8465** | 3.9892 | ±7.9785 | **+15.754** | **6.45e-56** | *** |
| **Education: graduate level (vs college)** | **-1.7832** | 0.7834 | ±1.5668 | **-2.276** | **0.0228** | * |
| Education: high school or below (vs college) | -1.8737 | 1.3466 | ±2.6933 | -1.391 | 0.1641 |  |
| **Site: UCSD (vs UAB)** | **-1.9792** | 0.9772 | ±1.9545 | **-2.025** | **0.0428** | * |
| **Site: UW (vs UAB)** | **-2.5767** | 0.8865 | ±1.7730 | **-2.907** | **0.0037** | ** |
| **Age (years)** | **-0.1333** | 0.0369 | ±0.0738 | **-3.615** | **3.00e-04** | *** |
| **BMI (kg/m2)** | **+0.2564** | 0.0812 | ±0.1624 | **+3.158** | **0.0016** | ** |
| Hypertension | +0.9412 | 0.8495 | ±1.6990 | +1.108 | 0.2679 |  |
| High cholesterol | -0.2733 | 0.8255 | ±1.6511 | -0.331 | 0.7406 |  |
| Kidney disease | +0.0569 | 2.2012 | ±4.4023 | +0.026 | 0.9794 |  |
| Circulatory disease | -0.6759 | 1.0070 | ±2.0141 | -0.671 | 0.5021 |  |
| Time 54-69, pooled (%) | -0.1069 | 1.8678 | ±3.7356 | -0.057 | 0.9544 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **346**, R² = **0.1794**, Adj R² = **0.1523**, F-statistic = **6.64** (p = **4.73e-10**), Residual SE = **6.676** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8807** | 3.9834 | ±7.9669 | **+15.785** | **3.92e-56** | *** |
| **Education: graduate level (vs college)** | **-1.7902** | 0.7812 | ±1.5625 | **-2.292** | **0.0219** | * |
| Education: high school or below (vs college) | -1.8684 | 1.3506 | ±2.7012 | -1.383 | 0.1666 |  |
| **Site: UCSD (vs UAB)** | **-1.9821** | 0.9755 | ±1.9510 | **-2.032** | **0.0422** | * |
| **Site: UW (vs UAB)** | **-2.5768** | 0.8855 | ±1.7711 | **-2.910** | **0.0036** | ** |
| **Age (years)** | **-0.1333** | 0.0369 | ±0.0738 | **-3.610** | **3.06e-04** | *** |
| **BMI (kg/m2)** | **+0.2563** | 0.0812 | ±0.1625 | **+3.155** | **0.0016** | ** |
| Hypertension | +0.9212 | 0.8640 | ±1.7281 | +1.066 | 0.2864 |  |
| High cholesterol | -0.2660 | 0.8267 | ±1.6535 | -0.322 | 0.7476 |  |
| Kidney disease | +0.0497 | 2.2050 | ±4.4100 | +0.023 | 0.9820 |  |
| Circulatory disease | -0.6683 | 1.0015 | ±2.0030 | -0.667 | 0.5046 |  |
| Avg. daily time 54-69 (%) | -0.3576 | 1.9303 | ±3.8605 | -0.185 | 0.8530 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **346**, R² = **0.1797**, Adj R² = **0.1526**, F-statistic = **6.65** (p = **4.49e-10**), Residual SE = **6.675** on **334** df, AIC = **2307.4**, BIC = **2353.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6823** | 3.9710 | ±7.9420 | **+15.785** | **3.94e-56** | *** |
| **Education: graduate level (vs college)** | **-1.7672** | 0.7833 | ±1.5665 | **-2.256** | **0.0241** | * |
| Education: high school or below (vs college) | -1.8839 | 1.3430 | ±2.6860 | -1.403 | 0.1607 |  |
| **Site: UCSD (vs UAB)** | **-1.9440** | 0.9753 | ±1.9505 | **-1.993** | **0.0462** | * |
| **Site: UW (vs UAB)** | **-2.5434** | 0.8839 | ±1.7677 | **-2.878** | **0.0040** | ** |
| **Age (years)** | **-0.1332** | 0.0368 | ±0.0736 | **-3.621** | **2.93e-04** | *** |
| **BMI (kg/m2)** | **+0.2566** | 0.0809 | ±0.1619 | **+3.171** | **0.0015** | ** |
| Hypertension | +0.9687 | 0.8459 | ±1.6918 | +1.145 | 0.2522 |  |
| High cholesterol | -0.3096 | 0.8247 | ±1.6495 | -0.375 | 0.7073 |  |
| Kidney disease | +0.0939 | 2.1964 | ±4.3929 | +0.043 | 0.9659 |  |
| Circulatory disease | -0.6841 | 1.0060 | ±2.0119 | -0.680 | 0.4965 |  |
| Time < 70 (%) | +0.6938 | 1.6553 | ±3.3107 | +0.419 | 0.6751 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **346**, R² = **0.1793**, Adj R² = **0.1523**, F-statistic = **6.63** (p = **4.79e-10**), Residual SE = **6.677** on **334** df, AIC = **2307.5**, BIC = **2353.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.8170** | 3.9797 | ±7.9594 | **+15.784** | **3.98e-56** | *** |
| **Education: graduate level (vs college)** | **-1.7799** | 0.7810 | ±1.5619 | **-2.279** | **0.0227** | * |
| Education: high school or below (vs college) | -1.8772 | 1.3480 | ±2.6961 | -1.393 | 0.1637 |  |
| **Site: UCSD (vs UAB)** | **-1.9746** | 0.9745 | ±1.9490 | **-2.026** | **0.0427** | * |
| **Site: UW (vs UAB)** | **-2.5722** | 0.8854 | ±1.7708 | **-2.905** | **0.0037** | ** |
| **Age (years)** | **-0.1333** | 0.0369 | ±0.0738 | **-3.615** | **3.00e-04** | *** |
| **BMI (kg/m2)** | **+0.2565** | 0.0812 | ±0.1624 | **+3.158** | **0.0016** | ** |
| Hypertension | +0.9497 | 0.8596 | ±1.7192 | +1.105 | 0.2693 |  |
| High cholesterol | -0.2803 | 0.8247 | ±1.6493 | -0.340 | 0.7339 |  |
| Kidney disease | +0.0630 | 2.2006 | ±4.4012 | +0.029 | 0.9772 |  |
| Circulatory disease | -0.6780 | 1.0002 | ±2.0004 | -0.678 | 0.4979 |  |
| Avg. daily time < 70 (%) | +0.0595 | 1.7262 | ±3.4524 | +0.034 | 0.9725 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **346**, R² = **0.1847**, Adj R² = **0.1578**, F-statistic = **6.88** (p = **1.82e-10**), Residual SE = **6.655** on **334** df, AIC = **2305.3**, BIC = **2351.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1081.7476 | 607.7249 | ±1215.4498 | +1.780 | 0.0751 | . |
| **Education: graduate level (vs college)** | **-1.7578** | 0.7755 | ±1.5510 | **-2.267** | **0.0234** | * |
| Education: high school or below (vs college) | -1.7499 | 1.3500 | ±2.7000 | -1.296 | 0.1949 |  |
| Site: UCSD (vs UAB) | -1.8147 | 0.9782 | ±1.9563 | -1.855 | 0.0636 | . |
| **Site: UW (vs UAB)** | **-2.5001** | 0.8785 | ±1.7571 | **-2.846** | **0.0044** | ** |
| **Age (years)** | **-0.1308** | 0.0366 | ±0.0732 | **-3.570** | **3.57e-04** | *** |
| **BMI (kg/m2)** | **+0.2514** | 0.0798 | ±0.1596 | **+3.151** | **0.0016** | ** |
| Hypertension | +0.8576 | 0.8464 | ±1.6928 | +1.013 | 0.3110 |  |
| High cholesterol | -0.2697 | 0.8181 | ±1.6362 | -0.330 | 0.7417 |  |
| Kidney disease | +0.1753 | 2.1964 | ±4.3927 | +0.080 | 0.9364 |  |
| Circulatory disease | -0.8210 | 1.0175 | ±2.0349 | -0.807 | 0.4197 |  |
| Time 54-250, pooled (%) | -10.1918 | 6.0748 | ±12.1497 | -1.678 | 0.0934 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **346**, R² = **0.1801**, Adj R² = **0.1531**, F-statistic = **6.67** (p = **4.12e-10**), Residual SE = **6.673** on **334** df, AIC = **2307.2**, BIC = **2353.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +542.3622 | 966.3427 | ±1932.6855 | +0.561 | 0.5746 |  |
| **Education: graduate level (vs college)** | **-1.7873** | 0.7799 | ±1.5598 | **-2.292** | **0.0219** | * |
| Education: high school or below (vs college) | -1.8565 | 1.3401 | ±2.6803 | -1.385 | 0.1660 |  |
| **Site: UCSD (vs UAB)** | **-1.9426** | 0.9781 | ±1.9562 | **-1.986** | **0.0470** | * |
| **Site: UW (vs UAB)** | **-2.5691** | 0.8860 | ±1.7720 | **-2.900** | **0.0037** | ** |
| **Age (years)** | **-0.1326** | 0.0368 | ±0.0735 | **-3.607** | **3.10e-04** | *** |
| **BMI (kg/m2)** | **+0.2552** | 0.0810 | ±0.1619 | **+3.152** | **0.0016** | ** |
| Hypertension | +0.9333 | 0.8445 | ±1.6890 | +1.105 | 0.2691 |  |
| High cholesterol | -0.2738 | 0.8206 | ±1.6411 | -0.334 | 0.7386 |  |
| Kidney disease | +0.0879 | 2.1936 | ±4.3871 | +0.040 | 0.9680 |  |
| Circulatory disease | -0.7572 | 1.0250 | ±2.0499 | -0.739 | 0.4600 |  |
| Avg. daily time 54-250 (%) | -4.7960 | 9.6614 | ±19.3229 | -0.496 | 0.6196 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **346**, R² = **0.1797**, Adj R² = **0.1527**, F-statistic = **6.65** (p = **4.46e-10**), Residual SE = **6.675** on **334** df, AIC = **2307.4**, BIC = **2353.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6102** | 4.2918 | ±8.5836 | **+14.588** | **3.34e-48** | *** |
| **Education: graduate level (vs college)** | **-1.7781** | 0.7814 | ±1.5628 | **-2.275** | **0.0229** | * |
| Education: high school or below (vs college) | -1.8518 | 1.3452 | ±2.6905 | -1.377 | 0.1686 |  |
| **Site: UCSD (vs UAB)** | **-1.9735** | 0.9835 | ±1.9670 | **-2.007** | **0.0448** | * |
| **Site: UW (vs UAB)** | **-2.5769** | 0.8860 | ±1.7721 | **-2.908** | **0.0036** | ** |
| **Age (years)** | **-0.1327** | 0.0374 | ±0.0747 | **-3.552** | **3.83e-04** | *** |
| **BMI (kg/m2)** | **+0.2573** | 0.0848 | ±0.1696 | **+3.034** | **0.0024** | ** |
| Hypertension | +0.9219 | 0.8431 | ±1.6861 | +1.093 | 0.2742 |  |
| High cholesterol | -0.2642 | 0.8315 | ±1.6631 | -0.318 | 0.7507 |  |
| Kidney disease | +0.0079 | 2.2539 | ±4.5077 | +0.003 | 0.9972 |  |
| Circulatory disease | -0.6789 | 1.0033 | ±2.0065 | -0.677 | 0.4986 |  |
| Time 181-250, pooled (%) | +0.5283 | 1.4455 | ±2.8910 | +0.365 | 0.7148 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **346**, R² = **0.1828**, Adj R² = **0.1559**, F-statistic = **6.79** (p = **2.57e-10**), Residual SE = **6.663** on **334** df, AIC = **2306.1**, BIC = **2352.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.1848** | 4.1234 | ±8.2469 | **+15.081** | **2.17e-51** | *** |
| **Education: graduate level (vs college)** | **-1.7729** | 0.7797 | ±1.5593 | **-2.274** | **0.0230** | * |
| Education: high school or below (vs college) | -1.7690 | 1.3305 | ±2.6610 | -1.330 | 0.1837 |  |
| **Site: UCSD (vs UAB)** | **-1.9431** | 0.9780 | ±1.9561 | **-1.987** | **0.0469** | * |
| **Site: UW (vs UAB)** | **-2.5835** | 0.8830 | ±1.7661 | **-2.926** | **0.0034** | ** |
| **Age (years)** | **-0.1297** | 0.0372 | ±0.0744 | **-3.484** | **4.94e-04** | *** |
| **BMI (kg/m2)** | **+0.2572** | 0.0826 | ±0.1652 | **+3.115** | **0.0018** | ** |
| Hypertension | +0.8818 | 0.8397 | ±1.6794 | +1.050 | 0.2937 |  |
| High cholesterol | -0.2729 | 0.8201 | ±1.6402 | -0.333 | 0.7393 |  |
| Kidney disease | -0.0108 | 2.2261 | ±4.4521 | -0.005 | 0.9961 |  |
| Circulatory disease | -0.6891 | 0.9958 | ±1.9916 | -0.692 | 0.4889 |  |
| Avg. daily time 181-250 (%) | +1.5242 | 1.3514 | ±2.7028 | +1.128 | 0.2594 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **346**, R² = **0.1796**, Adj R² = **0.1526**, F-statistic = **6.65** (p = **4.51e-10**), Residual SE = **6.675** on **334** df, AIC = **2307.4**, BIC = **2353.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.6282** | 4.2885 | ±8.5770 | **+14.604** | **2.66e-48** | *** |
| **Education: graduate level (vs college)** | **-1.7779** | 0.7814 | ±1.5629 | **-2.275** | **0.0229** | * |
| Education: high school or below (vs college) | -1.8537 | 1.3460 | ±2.6920 | -1.377 | 0.1684 |  |
| **Site: UCSD (vs UAB)** | **-1.9737** | 0.9834 | ±1.9667 | **-2.007** | **0.0447** | * |
| **Site: UW (vs UAB)** | **-2.5768** | 0.8860 | ±1.7719 | **-2.908** | **0.0036** | ** |
| **Age (years)** | **-0.1327** | 0.0374 | ±0.0747 | **-3.553** | **3.81e-04** | *** |
| **BMI (kg/m2)** | **+0.2572** | 0.0847 | ±0.1694 | **+3.037** | **0.0024** | ** |
| Hypertension | +0.9242 | 0.8433 | ±1.6866 | +1.096 | 0.2731 |  |
| High cholesterol | -0.2660 | 0.8313 | ±1.6625 | -0.320 | 0.7490 |  |
| Kidney disease | +0.0128 | 2.2531 | ±4.5063 | +0.006 | 0.9955 |  |
| Circulatory disease | -0.6785 | 1.0037 | ±2.0073 | -0.676 | 0.4990 |  |
| Time > 180 (%) | +0.4799 | 1.4467 | ±2.8935 | +0.332 | 0.7401 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **346**, R² = **0.1825**, Adj R² = **0.1556**, F-statistic = **6.78** (p = **2.68e-10**), Residual SE = **6.664** on **334** df, AIC = **2306.2**, BIC = **2352.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.2017** | 4.1246 | ±8.2493 | **+15.080** | **2.18e-51** | *** |
| **Education: graduate level (vs college)** | **-1.7717** | 0.7798 | ±1.5595 | **-2.272** | **0.0231** | * |
| Education: high school or below (vs college) | -1.7718 | 1.3314 | ±2.6629 | -1.331 | 0.1833 |  |
| **Site: UCSD (vs UAB)** | **-1.9442** | 0.9781 | ±1.9561 | **-1.988** | **0.0468** | * |
| **Site: UW (vs UAB)** | **-2.5841** | 0.8832 | ±1.7663 | **-2.926** | **0.0034** | ** |
| **Age (years)** | **-0.1297** | 0.0372 | ±0.0745 | **-3.485** | **4.93e-04** | *** |
| **BMI (kg/m2)** | **+0.2573** | 0.0826 | ±0.1652 | **+3.115** | **0.0018** | ** |
| Hypertension | +0.8846 | 0.8400 | ±1.6799 | +1.053 | 0.2923 |  |
| High cholesterol | -0.2748 | 0.8200 | ±1.6401 | -0.335 | 0.7376 |  |
| Kidney disease | -0.0080 | 2.2254 | ±4.4508 | -0.004 | 0.9971 |  |
| Circulatory disease | -0.6885 | 0.9962 | ±1.9923 | -0.691 | 0.4895 |  |
| Avg. daily time > 180 (%) | +1.4694 | 1.3537 | ±2.7073 | +1.086 | 0.2777 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 346)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **346**, R² = **0.1879**, Adj R² = **0.1611**, F-statistic = **7.02** (p = **1.02e-10**), Residual SE = **6.642** on **334** df, AIC = **2303.9**, BIC = **2350.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.1511** | 3.8724 | ±7.7448 | **+16.050** | **5.75e-58** | *** |
| **Education: graduate level (vs college)** | **-1.6725** | 0.7704 | ±1.5409 | **-2.171** | **0.0299** | * |
| Education: high school or below (vs college) | -1.8868 | 1.3200 | ±2.6401 | -1.429 | 0.1529 |  |
| **Site: UCSD (vs UAB)** | **-1.9339** | 0.9723 | ±1.9446 | **-1.989** | **0.0467** | * |
| **Site: UW (vs UAB)** | **-2.6360** | 0.8853 | ±1.7705 | **-2.978** | **0.0029** | ** |
| **Age (years)** | **-0.1201** | 0.0366 | ±0.0733 | **-3.278** | **0.0010** | ** |
| **BMI (kg/m2)** | **+0.2461** | 0.0802 | ±0.1604 | **+3.068** | **0.0022** | ** |
| Hypertension | +0.8509 | 0.8313 | ±1.6626 | +1.024 | 0.3060 |  |
| High cholesterol | -0.3761 | 0.8165 | ±1.6330 | -0.461 | 0.6451 |  |
| Kidney disease | -0.0938 | 2.1656 | ±4.3312 | -0.043 | 0.9655 |  |
| Circulatory disease | -0.6542 | 1.0038 | ±2.0077 | -0.652 | 0.5146 |  |
| Nocturnal time > 180 (%) | +1.9696 | 1.1673 | ±2.3345 | +1.687 | 0.0915 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 349; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **349**, R² = **0.0654**, Adj R² = **0.0377**, F-statistic = **2.36** (p = **0.0103**), Residual SE = **61.297** on **338** df, AIC = **3874.0**, BIC = **3916.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.5655** | 26.4944 | ±52.9889 | **+15.232** | **2.17e-52** | *** |
| Education: graduate level (vs college) | +4.9608 | 6.7860 | ±13.5720 | +0.731 | 0.4648 |  |
| Education: high school or below (vs college) | -7.2421 | 15.1168 | ±30.2336 | -0.479 | 0.6319 |  |
| Site: UCSD (vs UAB) | -10.3084 | 8.3718 | ±16.7436 | -1.231 | 0.2182 |  |
| Site: UW (vs UAB) | -5.2393 | 8.2818 | ±16.5636 | -0.633 | 0.5270 |  |
| Age (years) | +0.1741 | 0.3266 | ±0.6532 | +0.533 | 0.5939 |  |
| **BMI (kg/m2)** | **-1.1462** | 0.4868 | ±0.9735 | **-2.355** | **0.0185** | * |
| **Hypertension** | **-15.4435** | 7.7635 | ±15.5270 | **-1.989** | **0.0467** | * |
| High cholesterol | -1.4694 | 6.9827 | ±13.9653 | -0.210 | 0.8333 |  |
| Kidney disease | -33.4101 | 20.2134 | ±40.4268 | -1.653 | 0.0984 | . |
| Circulatory disease | +10.1124 | 13.3644 | ±26.7287 | +0.757 | 0.4492 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **349**, R² = **0.0952**, Adj R² = **0.0656**, F-statistic = **3.22** (p = **3.42e-04**), Residual SE = **60.401** on **337** df, AIC = **3864.7**, BIC = **3911.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+600.2638** | 62.8621 | ±125.7243 | **+9.549** | **1.31e-21** | *** |
| Education: graduate level (vs college) | +3.8604 | 6.7077 | ±13.4154 | +0.576 | 0.5649 |  |
| Education: high school or below (vs college) | -6.2891 | 14.9340 | ±29.8681 | -0.421 | 0.6737 |  |
| Site: UCSD (vs UAB) | -12.5410 | 8.2591 | ±16.5182 | -1.518 | 0.1289 |  |
| Site: UW (vs UAB) | -7.4743 | 8.1685 | ±16.3370 | -0.915 | 0.3602 |  |
| Age (years) | +0.2905 | 0.3257 | ±0.6514 | +0.892 | 0.3725 |  |
| **BMI (kg/m2)** | **-1.0099** | 0.4436 | ±0.8872 | **-2.276** | **0.0228** | * |
| Hypertension | -13.4699 | 7.7195 | ±15.4391 | -1.745 | 0.0810 | . |
| High cholesterol | +3.6242 | 6.8839 | ±13.7677 | +0.526 | 0.5986 |  |
| Kidney disease | -34.0634 | 18.7868 | ±37.5737 | -1.813 | 0.0698 | . |
| Circulatory disease | +8.6785 | 12.7431 | ±25.4862 | +0.681 | 0.4958 |  |
| **HbA1c (%)** | **-37.7074** | 11.4252 | ±22.8504 | **-3.300** | **9.66e-04** | *** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **349**, R² = **0.0708**, Adj R² = **0.0405**, F-statistic = **2.33** (p = **0.0089**), Residual SE = **61.209** on **337** df, AIC = **3874.0**, BIC = **3920.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+474.4049** | 52.4029 | ±104.8058 | **+9.053** | **1.39e-19** | *** |
| Education: graduate level (vs college) | +4.8245 | 6.7684 | ±13.5368 | +0.713 | 0.4760 |  |
| Education: high school or below (vs college) | -8.0787 | 15.3416 | ±30.6833 | -0.527 | 0.5985 |  |
| Site: UCSD (vs UAB) | -9.7231 | 8.3638 | ±16.7277 | -1.163 | 0.2450 |  |
| Site: UW (vs UAB) | -4.5730 | 8.3035 | ±16.6070 | -0.551 | 0.5818 |  |
| Age (years) | +0.1491 | 0.3247 | ±0.6493 | +0.459 | 0.6461 |  |
| **BMI (kg/m2)** | **-1.0935** | 0.4825 | ±0.9651 | **-2.266** | **0.0234** | * |
| Hypertension | -14.5683 | 7.8244 | ±15.6488 | -1.862 | 0.0626 | . |
| High cholesterol | -1.9568 | 6.9642 | ±13.9283 | -0.281 | 0.7787 |  |
| Kidney disease | -33.2367 | 20.1190 | ±40.2381 | -1.652 | 0.0985 | . |
| Circulatory disease | +9.8547 | 13.3440 | ±26.6880 | +0.739 | 0.4602 |  |
| Mean glucose (mg/dL) | -0.6242 | 0.4121 | ±0.8242 | -1.514 | 0.1299 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **349**, R² = **0.0708**, Adj R² = **0.0405**, F-statistic = **2.33** (p = **0.0089**), Residual SE = **61.209** on **337** df, AIC = **3874.0**, BIC = **3920.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+560.7743** | 105.7091 | ±211.4182 | **+5.305** | **1.13e-07** | *** |
| Education: graduate level (vs college) | +4.8245 | 6.7684 | ±13.5368 | +0.713 | 0.4760 |  |
| Education: high school or below (vs college) | -8.0787 | 15.3416 | ±30.6833 | -0.527 | 0.5985 |  |
| Site: UCSD (vs UAB) | -9.7231 | 8.3638 | ±16.7277 | -1.163 | 0.2450 |  |
| Site: UW (vs UAB) | -4.5730 | 8.3035 | ±16.6070 | -0.551 | 0.5818 |  |
| Age (years) | +0.1491 | 0.3247 | ±0.6493 | +0.459 | 0.6461 |  |
| **BMI (kg/m2)** | **-1.0935** | 0.4825 | ±0.9651 | **-2.266** | **0.0234** | * |
| Hypertension | -14.5683 | 7.8244 | ±15.6488 | -1.862 | 0.0626 | . |
| High cholesterol | -1.9568 | 6.9642 | ±13.9283 | -0.281 | 0.7787 |  |
| Kidney disease | -33.2367 | 20.1190 | ±40.2381 | -1.652 | 0.0985 | . |
| Circulatory disease | +9.8547 | 13.3440 | ±26.6880 | +0.739 | 0.4602 |  |
| GMI (%) | -26.0935 | 17.2292 | ±34.4583 | -1.514 | 0.1299 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **349**, R² = **0.0735**, Adj R² = **0.0432**, F-statistic = **2.43** (p = **0.0064**), Residual SE = **61.122** on **337** df, AIC = **3873.0**, BIC = **3919.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+474.4693** | 45.8950 | ±91.7899 | **+10.338** | **4.74e-25** | *** |
| Education: graduate level (vs college) | +4.1878 | 6.7933 | ±13.5867 | +0.616 | 0.5376 |  |
| Education: high school or below (vs college) | -8.3824 | 15.2378 | ±30.4756 | -0.550 | 0.5822 |  |
| Site: UCSD (vs UAB) | -8.7395 | 8.3584 | ±16.7167 | -1.046 | 0.2957 |  |
| Site: UW (vs UAB) | -3.9692 | 8.3341 | ±16.6682 | -0.476 | 0.6339 |  |
| Age (years) | +0.0821 | 0.3232 | ±0.6465 | +0.254 | 0.7994 |  |
| **BMI (kg/m2)** | **-1.0003** | 0.4657 | ±0.9314 | **-2.148** | **0.0317** | * |
| Hypertension | -14.5908 | 7.8106 | ±15.6212 | -1.868 | 0.0617 | . |
| High cholesterol | -1.5693 | 6.9856 | ±13.9711 | -0.225 | 0.8222 |  |
| Kidney disease | -34.4176 | 20.2110 | ±40.4219 | -1.703 | 0.0886 | . |
| Circulatory disease | +9.3443 | 13.3602 | ±26.7204 | +0.699 | 0.4843 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.6121 | 0.3457 | ±0.6913 | -1.771 | 0.0766 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **349**, R² = **0.0667**, Adj R² = **0.0363**, F-statistic = **2.19** (p = **0.0146**), Residual SE = **61.343** on **337** df, AIC = **3875.5**, BIC = **3921.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+385.8456** | 37.1624 | ±74.3247 | **+10.383** | **2.97e-25** | *** |
| Education: graduate level (vs college) | +5.4285 | 6.8820 | ±13.7640 | +0.789 | 0.4302 |  |
| Education: high school or below (vs college) | -7.1972 | 15.1695 | ±30.3389 | -0.474 | 0.6352 |  |
| Site: UCSD (vs UAB) | -9.6870 | 8.3469 | ±16.6938 | -1.161 | 0.2458 |  |
| Site: UW (vs UAB) | -4.8305 | 8.3567 | ±16.7135 | -0.578 | 0.5632 |  |
| Age (years) | +0.1722 | 0.3269 | ±0.6538 | +0.527 | 0.5985 |  |
| **BMI (kg/m2)** | **-1.1600** | 0.4885 | ±0.9771 | **-2.375** | **0.0176** | * |
| **Hypertension** | **-15.4983** | 7.7875 | ±15.5749 | **-1.990** | **0.0466** | * |
| High cholesterol | -1.1962 | 6.9911 | ±13.9822 | -0.171 | 0.8641 |  |
| Kidney disease | -34.1688 | 20.3139 | ±40.6277 | -1.682 | 0.0926 | . |
| Circulatory disease | +10.0936 | 13.4142 | ±26.8284 | +0.752 | 0.4518 |  |
| Glucose SD, pooled (mg/dL) | +1.0470 | 1.5009 | ±3.0018 | +0.698 | 0.4854 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **349**, R² = **0.0667**, Adj R² = **0.0363**, F-statistic = **2.19** (p = **0.0146**), Residual SE = **61.343** on **337** df, AIC = **3875.5**, BIC = **3921.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+387.5376** | 35.4502 | ±70.9005 | **+10.932** | **8.12e-28** | *** |
| Education: graduate level (vs college) | +5.4462 | 6.8977 | ±13.7955 | +0.790 | 0.4298 |  |
| Education: high school or below (vs college) | -7.0707 | 15.1468 | ±30.2936 | -0.467 | 0.6406 |  |
| Site: UCSD (vs UAB) | -9.6083 | 8.3649 | ±16.7298 | -1.149 | 0.2507 |  |
| Site: UW (vs UAB) | -4.7893 | 8.3255 | ±16.6509 | -0.575 | 0.5651 |  |
| Age (years) | +0.1739 | 0.3275 | ±0.6550 | +0.531 | 0.5954 |  |
| **BMI (kg/m2)** | **-1.1701** | 0.4923 | ±0.9847 | **-2.377** | **0.0175** | * |
| **Hypertension** | **-15.3433** | 7.7942 | ±15.5885 | **-1.969** | **0.0490** | * |
| High cholesterol | -1.2995 | 6.9938 | ±13.9875 | -0.186 | 0.8526 |  |
| Kidney disease | -34.2635 | 20.2836 | ±40.5671 | -1.689 | 0.0912 | . |
| Circulatory disease | +10.1686 | 13.3933 | ±26.7865 | +0.759 | 0.4477 |  |
| Avg. daily SD (mg/dL) | +1.0374 | 1.5346 | ±3.0692 | +0.676 | 0.4991 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **349**, R² = **0.0700**, Adj R² = **0.0396**, F-statistic = **2.30** (p = **0.0099**), Residual SE = **61.237** on **337** df, AIC = **3874.3**, BIC = **3920.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+372.4843** | 36.7878 | ±73.5755 | **+10.125** | **4.27e-24** | *** |
| Education: graduate level (vs college) | +5.7359 | 6.8482 | ±13.6964 | +0.838 | 0.4023 |  |
| Education: high school or below (vs college) | -7.5126 | 15.2811 | ±30.5622 | -0.492 | 0.6230 |  |
| Site: UCSD (vs UAB) | -9.0098 | 8.3380 | ±16.6759 | -1.081 | 0.2799 |  |
| Site: UW (vs UAB) | -4.2460 | 8.4131 | ±16.8263 | -0.505 | 0.6138 |  |
| Age (years) | +0.1610 | 0.3253 | ±0.6506 | +0.495 | 0.6205 |  |
| **BMI (kg/m2)** | **-1.1488** | 0.4886 | ±0.9771 | **-2.351** | **0.0187** | * |
| Hypertension | -15.1746 | 7.8102 | ±15.6205 | -1.943 | 0.0520 | . |
| High cholesterol | -1.1507 | 6.9873 | ±13.9746 | -0.165 | 0.8692 |  |
| Kidney disease | -34.6262 | 20.3126 | ±40.6252 | -1.705 | 0.0883 | . |
| Circulatory disease | +9.9455 | 13.4133 | ±26.8266 | +0.741 | 0.4584 |  |
| CV (%) | +2.0755 | 1.6257 | ±3.2515 | +1.277 | 0.2017 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **349**, R² = **0.0697**, Adj R² = **0.0393**, F-statistic = **2.30** (p = **0.0102**), Residual SE = **61.245** on **337** df, AIC = **3874.4**, BIC = **3920.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+431.8984** | 34.2161 | ±68.4323 | **+12.623** | **1.58e-36** | *** |
| Education: graduate level (vs college) | +5.7771 | 6.8468 | ±13.6936 | +0.844 | 0.3988 |  |
| Education: high school or below (vs college) | -7.5131 | 15.2983 | ±30.5966 | -0.491 | 0.6234 |  |
| Site: UCSD (vs UAB) | -9.1885 | 8.3306 | ±16.6612 | -1.103 | 0.2700 |  |
| Site: UW (vs UAB) | -4.4377 | 8.3858 | ±16.7715 | -0.529 | 0.5967 |  |
| Age (years) | +0.1638 | 0.3252 | ±0.6504 | +0.504 | 0.6144 |  |
| **BMI (kg/m2)** | **-1.1475** | 0.4872 | ±0.9744 | **-2.355** | **0.0185** | * |
| **Hypertension** | **-15.3288** | 7.8025 | ±15.6050 | **-1.965** | **0.0495** | * |
| High cholesterol | -1.1346 | 6.9890 | ±13.9781 | -0.162 | 0.8710 |  |
| Kidney disease | -34.1706 | 20.3005 | ±40.6010 | -1.683 | 0.0923 | . |
| Circulatory disease | +9.9919 | 13.4074 | ±26.8147 | +0.745 | 0.4561 |  |
| Mean / SD ratio | -4.1736 | 3.3293 | ±6.6585 | -1.254 | 0.2100 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **349**, R² = **0.0678**, Adj R² = **0.0374**, F-statistic = **2.23** (p = **0.0128**), Residual SE = **61.307** on **337** df, AIC = **3875.1**, BIC = **3921.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+423.4098** | 34.1544 | ±68.3089 | **+12.397** | **2.72e-35** | *** |
| Education: graduate level (vs college) | +5.6038 | 6.8603 | ±13.7206 | +0.817 | 0.4140 |  |
| Education: high school or below (vs college) | -7.2771 | 15.2783 | ±30.5567 | -0.476 | 0.6339 |  |
| Site: UCSD (vs UAB) | -9.3300 | 8.3950 | ±16.7899 | -1.111 | 0.2664 |  |
| Site: UW (vs UAB) | -4.5946 | 8.3666 | ±16.7333 | -0.549 | 0.5829 |  |
| Age (years) | +0.1695 | 0.3267 | ±0.6534 | +0.519 | 0.6040 |  |
| **BMI (kg/m2)** | **-1.1688** | 0.4904 | ±0.9809 | **-2.383** | **0.0172** | * |
| Hypertension | -15.0993 | 7.8184 | ±15.6369 | -1.931 | 0.0535 | . |
| High cholesterol | -1.4174 | 6.9937 | ±13.9875 | -0.203 | 0.8394 |  |
| Kidney disease | -34.2836 | 20.2185 | ±40.4371 | -1.696 | 0.0900 | . |
| Circulatory disease | +10.1271 | 13.3558 | ±26.7116 | +0.758 | 0.4483 |  |
| Avg. daily mean/SD | -2.5499 | 2.7486 | ±5.4972 | -0.928 | 0.3536 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **349**, R² = **0.0713**, Adj R² = **0.0410**, F-statistic = **2.35** (p = **0.0084**), Residual SE = **61.193** on **337** df, AIC = **3873.8**, BIC = **3920.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+437.8260** | 36.3674 | ±72.7349 | **+12.039** | **2.22e-33** | *** |
| Education: graduate level (vs college) | +4.9246 | 6.7819 | ±13.5638 | +0.726 | 0.4678 |  |
| Education: high school or below (vs college) | -5.6621 | 14.8191 | ±29.6382 | -0.382 | 0.7024 |  |
| Site: UCSD (vs UAB) | -11.3004 | 8.3850 | ±16.7701 | -1.348 | 0.1778 |  |
| Site: UW (vs UAB) | -6.8147 | 8.3349 | ±16.6697 | -0.818 | 0.4136 |  |
| Age (years) | +0.1144 | 0.3302 | ±0.6605 | +0.346 | 0.7290 |  |
| **BMI (kg/m2)** | **-1.1929** | 0.4826 | ±0.9652 | **-2.472** | **0.0134** | * |
| **Hypertension** | **-16.0576** | 7.8262 | ±15.6525 | **-2.052** | **0.0402** | * |
| High cholesterol | -0.5133 | 6.9302 | ±13.8603 | -0.074 | 0.9410 |  |
| Kidney disease | -31.5833 | 20.3110 | ±40.6220 | -1.555 | 0.1199 |  |
| Circulatory disease | +10.2201 | 13.3358 | ±26.6716 | +0.766 | 0.4435 |  |
| MAG (mg/dL/h) | -0.8410 | 0.5881 | ±1.1761 | -1.430 | 0.1527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **349**, R² = **0.0696**, Adj R² = **0.0392**, F-statistic = **2.29** (p = **0.0103**), Residual SE = **61.249** on **337** df, AIC = **3874.4**, BIC = **3920.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+371.0028** | 39.5014 | ±79.0027 | **+9.392** | **5.88e-21** | *** |
| Education: graduate level (vs college) | +5.3148 | 6.8237 | ±13.6474 | +0.779 | 0.4361 |  |
| Education: high school or below (vs college) | -7.2508 | 15.3048 | ±30.6096 | -0.474 | 0.6357 |  |
| Site: UCSD (vs UAB) | -9.2426 | 8.3818 | ±16.7636 | -1.103 | 0.2702 |  |
| Site: UW (vs UAB) | -4.4077 | 8.3608 | ±16.7217 | -0.527 | 0.5981 |  |
| Age (years) | +0.1812 | 0.3264 | ±0.6528 | +0.555 | 0.5787 |  |
| **BMI (kg/m2)** | **-1.0998** | 0.4814 | ±0.9628 | **-2.285** | **0.0223** | * |
| Hypertension | -14.8075 | 7.8521 | ±15.7043 | -1.886 | 0.0593 | . |
| High cholesterol | -1.5693 | 7.0066 | ±14.0133 | -0.224 | 0.8228 |  |
| Kidney disease | -34.4741 | 20.2161 | ±40.4322 | -1.705 | 0.0881 | . |
| Circulatory disease | +9.9149 | 13.3506 | ±26.7012 | +0.743 | 0.4577 |  |
| Avg. daily range (mg/dL) | +0.3728 | 0.3398 | ±0.6795 | +1.097 | 0.2725 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **349**, R² = **0.0655**, Adj R² = **0.0350**, F-statistic = **2.15** (p = **0.0170**), Residual SE = **61.384** on **337** df, AIC = **3876.0**, BIC = **3922.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+401.8047** | 28.2906 | ±56.5812 | **+14.203** | **8.81e-46** | *** |
| Education: graduate level (vs college) | +4.9229 | 6.8090 | ±13.6181 | +0.723 | 0.4697 |  |
| Education: high school or below (vs college) | -7.3847 | 15.1492 | ±30.2983 | -0.487 | 0.6259 |  |
| Site: UCSD (vs UAB) | -10.2321 | 8.3715 | ±16.7431 | -1.222 | 0.2216 |  |
| Site: UW (vs UAB) | -5.3135 | 8.2992 | ±16.5984 | -0.640 | 0.5220 |  |
| Age (years) | +0.1730 | 0.3272 | ±0.6545 | +0.529 | 0.5971 |  |
| **BMI (kg/m2)** | **-1.1487** | 0.4881 | ±0.9762 | **-2.353** | **0.0186** | * |
| **Hypertension** | **-15.5589** | 7.8301 | ±15.6601 | **-1.987** | **0.0469** | * |
| High cholesterol | -1.4791 | 7.0034 | ±14.0068 | -0.211 | 0.8327 |  |
| Kidney disease | -33.2622 | 20.3963 | ±40.7927 | -1.631 | 0.1029 |  |
| Circulatory disease | +10.0305 | 13.4388 | ±26.8775 | +0.746 | 0.4554 |  |
| SD of daily means (mg/dL) | +0.3901 | 1.8296 | ±3.6593 | +0.213 | 0.8312 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **349**, R² = **0.0678**, Adj R² = **0.0374**, F-statistic = **2.23** (p = **0.0128**), Residual SE = **61.308** on **337** df, AIC = **3875.1**, BIC = **3921.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1450.2171 | 1177.7835 | ±2355.5671 | +1.231 | 0.2182 |  |
| Education: graduate level (vs college) | +5.1935 | 6.8251 | ±13.6502 | +0.761 | 0.4467 |  |
| Education: high school or below (vs college) | -7.1870 | 15.2083 | ±30.4166 | -0.473 | 0.6365 |  |
| Site: UCSD (vs UAB) | -9.8249 | 8.3577 | ±16.7154 | -1.176 | 0.2398 |  |
| Site: UW (vs UAB) | -4.8503 | 8.3266 | ±16.6533 | -0.583 | 0.5602 |  |
| Age (years) | +0.1852 | 0.3262 | ±0.6524 | +0.568 | 0.5701 |  |
| **BMI (kg/m2)** | **-1.1227** | 0.4767 | ±0.9534 | **-2.355** | **0.0185** | * |
| **Hypertension** | **-15.4841** | 7.7925 | ±15.5850 | **-1.987** | **0.0469** | * |
| High cholesterol | -1.6426 | 7.0069 | ±14.0137 | -0.234 | 0.8146 |  |
| Kidney disease | -33.6806 | 20.2022 | ±40.4045 | -1.667 | 0.0955 | . |
| Circulatory disease | +10.1337 | 13.4865 | ±26.9730 | +0.751 | 0.4524 |  |
| Time in range 70-180, pooled (%) | -10.5319 | 11.8666 | ±23.7332 | -0.888 | 0.3748 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **349**, R² = **0.0690**, Adj R² = **0.0386**, F-statistic = **2.27** (p = **0.0111**), Residual SE = **61.268** on **337** df, AIC = **3874.7**, BIC = **3920.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1646.6510 | 1146.0906 | ±2292.1811 | +1.437 | 0.1508 |  |
| Education: graduate level (vs college) | +5.2889 | 6.8428 | ±13.6856 | +0.773 | 0.4396 |  |
| Education: high school or below (vs college) | -6.9444 | 15.2098 | ±30.4196 | -0.457 | 0.6480 |  |
| Site: UCSD (vs UAB) | -9.7638 | 8.3520 | ±16.7040 | -1.169 | 0.2424 |  |
| Site: UW (vs UAB) | -5.1308 | 8.3282 | ±16.6563 | -0.616 | 0.5378 |  |
| Age (years) | +0.2017 | 0.3284 | ±0.6567 | +0.614 | 0.5391 |  |
| **BMI (kg/m2)** | **-1.1322** | 0.4845 | ±0.9691 | **-2.337** | **0.0195** | * |
| Hypertension | -14.9707 | 7.8336 | ±15.6671 | -1.911 | 0.0560 | . |
| High cholesterol | -1.8598 | 7.0122 | ±14.0244 | -0.265 | 0.7908 |  |
| Kidney disease | -33.5595 | 20.1916 | ±40.3833 | -1.662 | 0.0965 | . |
| Circulatory disease | +9.5862 | 13.5112 | ±27.0223 | +0.710 | 0.4780 |  |
| Avg. daily time in range 70-180 (%) | -12.5049 | 11.5396 | ±23.0791 | -1.084 | 0.2785 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **349**, R² = **0.0664**, Adj R² = **0.0359**, F-statistic = **2.18** (p = **0.0153**), Residual SE = **61.355** on **337** df, AIC = **3875.7**, BIC = **3921.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+402.3791** | 26.8132 | ±53.6264 | **+15.007** | **6.63e-51** | *** |
| Education: graduate level (vs college) | +5.0000 | 6.8070 | ±13.6140 | +0.735 | 0.4626 |  |
| Education: high school or below (vs college) | -7.1130 | 15.2118 | ±30.4237 | -0.468 | 0.6401 |  |
| Site: UCSD (vs UAB) | -9.4409 | 8.5805 | ±17.1610 | -1.100 | 0.2712 |  |
| Site: UW (vs UAB) | -4.7158 | 8.3441 | ±16.6882 | -0.565 | 0.5720 |  |
| Age (years) | +0.1716 | 0.3264 | ±0.6529 | +0.526 | 0.5991 |  |
| **BMI (kg/m2)** | **-1.1475** | 0.4903 | ±0.9805 | **-2.341** | **0.0193** | * |
| **Hypertension** | **-15.7207** | 7.8213 | ±15.6427 | **-2.010** | **0.0444** | * |
| High cholesterol | -1.4445 | 7.0018 | ±14.0035 | -0.206 | 0.8366 |  |
| Kidney disease | -32.8374 | 20.4036 | ±40.8072 | -1.609 | 0.1075 |  |
| Circulatory disease | +9.8634 | 13.4490 | ±26.8980 | +0.733 | 0.4633 |  |
| Any reading < 54 during wear (0/1) | +5.2781 | 7.9305 | ±15.8609 | +0.666 | 0.5057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **349**, R² = **0.0660**, Adj R² = **0.0355**, F-statistic = **2.16** (p = **0.0160**), Residual SE = **61.368** on **337** df, AIC = **3875.8**, BIC = **3922.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+402.9475** | 26.7842 | ±53.5684 | **+15.044** | **3.77e-51** | *** |
| Education: graduate level (vs college) | +4.9866 | 6.8036 | ±13.6072 | +0.733 | 0.4636 |  |
| Education: high school or below (vs college) | -6.9207 | 15.1378 | ±30.2757 | -0.457 | 0.6475 |  |
| Site: UCSD (vs UAB) | -9.7843 | 8.5303 | ±17.0605 | -1.147 | 0.2514 |  |
| Site: UW (vs UAB) | -4.9773 | 8.3549 | ±16.7098 | -0.596 | 0.5514 |  |
| Age (years) | +0.1799 | 0.3277 | ±0.6554 | +0.549 | 0.5830 |  |
| **BMI (kg/m2)** | **-1.1629** | 0.4944 | ±0.9889 | **-2.352** | **0.0187** | * |
| **Hypertension** | **-15.6966** | 7.8022 | ±15.6045 | **-2.012** | **0.0442** | * |
| High cholesterol | -1.4124 | 6.9971 | ±13.9941 | -0.202 | 0.8400 |  |
| Kidney disease | -33.0589 | 20.2874 | ±40.5747 | -1.630 | 0.1032 |  |
| Circulatory disease | +9.7252 | 13.4378 | ±26.8756 | +0.724 | 0.4692 |  |
| Time < 54 (%) | +30.2259 | 56.4323 | ±112.8646 | +0.536 | 0.5922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **349**, R² = **0.0686**, Adj R² = **0.0382**, F-statistic = **2.26** (p = **0.0116**), Residual SE = **61.281** on **337** df, AIC = **3874.8**, BIC = **3921.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+402.9034** | 26.7291 | ±53.4581 | **+15.074** | **2.42e-51** | *** |
| Education: graduate level (vs college) | +4.7646 | 6.8038 | ±13.6076 | +0.700 | 0.4837 |  |
| Education: high school or below (vs college) | -6.9802 | 15.1381 | ±30.2762 | -0.461 | 0.6447 |  |
| Site: UCSD (vs UAB) | -9.6475 | 8.3939 | ±16.7878 | -1.149 | 0.2504 |  |
| Site: UW (vs UAB) | -5.0512 | 8.2805 | ±16.5610 | -0.610 | 0.5419 |  |
| Age (years) | +0.1813 | 0.3266 | ±0.6532 | +0.555 | 0.5788 |  |
| **BMI (kg/m2)** | **-1.1721** | 0.4962 | ±0.9925 | **-2.362** | **0.0182** | * |
| **Hypertension** | **-15.6524** | 7.7568 | ±15.5136 | **-2.018** | **0.0436** | * |
| High cholesterol | -1.2936 | 7.0138 | ±14.0275 | -0.184 | 0.8537 |  |
| Kidney disease | -32.9638 | 20.3267 | ±40.6534 | -1.622 | 0.1049 |  |
| Circulatory disease | +8.8135 | 13.4496 | ±26.8991 | +0.655 | 0.5123 |  |
| Avg. daily time < 54 (%) | +82.1411 | 60.9515 | ±121.9029 | +1.348 | 0.1778 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **349**, R² = **0.0833**, Adj R² = **0.0534**, F-statistic = **2.78** (p = **0.0018**), Residual SE = **60.796** on **337** df, AIC = **3869.3**, BIC = **3915.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.7782** | 27.2990 | ±54.5980 | **+14.498** | **1.25e-47** | *** |
| Education: graduate level (vs college) | +5.8491 | 6.7634 | ±13.5268 | +0.865 | 0.3871 |  |
| Education: high school or below (vs college) | -9.4947 | 15.4006 | ±30.8013 | -0.617 | 0.5376 |  |
| Site: UCSD (vs UAB) | -9.2692 | 8.3501 | ±16.7002 | -1.110 | 0.2670 |  |
| Site: UW (vs UAB) | -3.8297 | 8.3158 | ±16.6316 | -0.461 | 0.6451 |  |
| Age (years) | +0.1608 | 0.3236 | ±0.6472 | +0.497 | 0.6192 |  |
| **BMI (kg/m2)** | **-1.1142** | 0.4922 | ±0.9844 | **-2.264** | **0.0236** | * |
| Hypertension | -13.4055 | 7.8050 | ±15.6100 | -1.718 | 0.0859 | . |
| High cholesterol | -3.8069 | 6.9477 | ±13.8954 | -0.548 | 0.5837 |  |
| Kidney disease | -31.6168 | 20.4979 | ±40.9958 | -1.542 | 0.1230 |  |
| Circulatory disease | +10.2020 | 13.3119 | ±26.6238 | +0.766 | 0.4435 |  |
| **Time 54-69, pooled (%)** | **+47.2703** | 17.5737 | ±35.1475 | **+2.690** | **0.0071** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **349**, R² = **0.0838**, Adj R² = **0.0539**, F-statistic = **2.80** (p = **0.0017**), Residual SE = **60.780** on **337** df, AIC = **3869.1**, BIC = **3915.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.8980** | 27.1147 | ±54.2294 | **+14.638** | **1.61e-48** | *** |
| Education: graduate level (vs college) | +6.1474 | 6.7671 | ±13.5343 | +0.908 | 0.3637 |  |
| Education: high school or below (vs college) | -9.4665 | 15.5199 | ±31.0397 | -0.610 | 0.5419 |  |
| Site: UCSD (vs UAB) | -9.9138 | 8.3325 | ±16.6651 | -1.190 | 0.2341 |  |
| Site: UW (vs UAB) | -4.8630 | 8.2523 | ±16.5046 | -0.589 | 0.5557 |  |
| Age (years) | +0.1592 | 0.3257 | ±0.6514 | +0.489 | 0.6249 |  |
| **BMI (kg/m2)** | **-1.1250** | 0.4897 | ±0.9795 | **-2.297** | **0.0216** | * |
| Hypertension | -12.0598 | 7.9534 | ±15.9067 | -1.516 | 0.1294 |  |
| High cholesterol | -3.0755 | 6.9312 | ±13.8625 | -0.444 | 0.6572 |  |
| Kidney disease | -31.8140 | 20.4587 | ±40.9175 | -1.555 | 0.1199 |  |
| Circulatory disease | +9.2263 | 13.3194 | ±26.6388 | +0.693 | 0.4885 |  |
| **Avg. daily time 54-69 (%)** | **+48.0658** | 18.3528 | ±36.7056 | **+2.619** | **0.0088** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **349**, R² = **0.0810**, Adj R² = **0.0510**, F-statistic = **2.70** (p = **0.0024**), Residual SE = **60.872** on **337** df, AIC = **3870.1**, BIC = **3916.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.3240** | 27.4157 | ±54.8315 | **+14.456** | **2.30e-47** | *** |
| Education: graduate level (vs college) | +5.7290 | 6.7624 | ±13.5247 | +0.847 | 0.3969 |  |
| Education: high school or below (vs college) | -8.6898 | 15.3548 | ±30.7095 | -0.566 | 0.5714 |  |
| Site: UCSD (vs UAB) | -8.7707 | 8.3629 | ±16.7257 | -1.049 | 0.2943 |  |
| Site: UW (vs UAB) | -3.7343 | 8.3472 | ±16.6945 | -0.447 | 0.6546 |  |
| Age (years) | +0.1706 | 0.3240 | ±0.6479 | +0.526 | 0.5986 |  |
| **BMI (kg/m2)** | **-1.1414** | 0.4969 | ±0.9938 | **-2.297** | **0.0216** | * |
| Hypertension | -14.0850 | 7.7735 | ±15.5470 | -1.812 | 0.0700 | . |
| High cholesterol | -3.3293 | 6.9427 | ±13.8854 | -0.480 | 0.6316 |  |
| Kidney disease | -31.4722 | 20.5045 | ±41.0089 | -1.535 | 0.1248 |  |
| Circulatory disease | +9.6856 | 13.3225 | ±26.6450 | +0.727 | 0.4672 |  |
| **Time < 70 (%)** | **+39.1046** | 15.1458 | ±30.2917 | **+2.582** | **0.0098** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **349**, R² = **0.0835**, Adj R² = **0.0536**, F-statistic = **2.79** (p = **0.0017**), Residual SE = **60.789** on **337** df, AIC = **3869.2**, BIC = **3915.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+397.2696** | 27.1380 | ±54.2761 | **+14.639** | **1.59e-48** | *** |
| Education: graduate level (vs college) | +5.9173 | 6.7503 | ±13.5006 | +0.877 | 0.3807 |  |
| Education: high school or below (vs college) | -9.0904 | 15.4847 | ±30.9693 | -0.587 | 0.5572 |  |
| Site: UCSD (vs UAB) | -9.6111 | 8.3180 | ±16.6360 | -1.155 | 0.2479 |  |
| Site: UW (vs UAB) | -4.8052 | 8.2528 | ±16.5056 | -0.582 | 0.5604 |  |
| Age (years) | +0.1646 | 0.3256 | ±0.6512 | +0.505 | 0.6132 |  |
| **BMI (kg/m2)** | **-1.1409** | 0.4926 | ±0.9851 | **-2.316** | **0.0205** | * |
| Hypertension | -12.5329 | 7.9121 | ±15.8242 | -1.584 | 0.1132 |  |
| High cholesterol | -2.8109 | 6.9323 | ±13.8645 | -0.405 | 0.6851 |  |
| Kidney disease | -31.7527 | 20.4872 | ±40.9743 | -1.550 | 0.1212 |  |
| Circulatory disease | +8.6434 | 13.3287 | ±26.6575 | +0.648 | 0.5167 |  |
| **Avg. daily time < 70 (%)** | **+42.8943** | 16.2583 | ±32.5167 | **+2.638** | **0.0083** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **349**, R² = **0.0657**, Adj R² = **0.0352**, F-statistic = **2.15** (p = **0.0165**), Residual SE = **61.376** on **337** df, AIC = **3875.9**, BIC = **3922.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2677.7952 | 5708.8243 | ±11417.6485 | +0.469 | 0.6390 |  |
| Education: graduate level (vs college) | +5.0003 | 6.8061 | ±13.6122 | +0.735 | 0.4625 |  |
| Education: high school or below (vs college) | -6.9847 | 15.1326 | ±30.2651 | -0.462 | 0.6444 |  |
| Site: UCSD (vs UAB) | -9.9122 | 8.5293 | ±17.0585 | -1.162 | 0.2452 |  |
| Site: UW (vs UAB) | -5.0559 | 8.3482 | ±16.6964 | -0.606 | 0.5448 |  |
| Age (years) | +0.1793 | 0.3280 | ±0.6559 | +0.547 | 0.5846 |  |
| **BMI (kg/m2)** | **-1.1578** | 0.4928 | ±0.9856 | **-2.350** | **0.0188** | * |
| **Hypertension** | **-15.6267** | 7.8008 | ±15.6017 | **-2.003** | **0.0452** | * |
| High cholesterol | -1.4502 | 6.9976 | ±13.9952 | -0.207 | 0.8358 |  |
| Kidney disease | -33.1456 | 20.2772 | ±40.5544 | -1.635 | 0.1021 |  |
| Circulatory disease | +9.8235 | 13.4400 | ±26.8801 | +0.731 | 0.4648 |  |
| Time 54-250, pooled (%) | -22.7478 | 57.1185 | ±114.2371 | -0.398 | 0.6904 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **349**, R² = **0.0677**, Adj R² = **0.0373**, F-statistic = **2.23** (p = **0.0129**), Residual SE = **61.310** on **337** df, AIC = **3875.1**, BIC = **3921.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +7348.7961 | 6215.6607 | ±12431.3214 | +1.182 | 0.2371 |  |
| Education: graduate level (vs college) | +4.8630 | 6.8045 | ±13.6089 | +0.715 | 0.4748 |  |
| Education: high school or below (vs college) | -6.9683 | 15.1306 | ±30.2611 | -0.461 | 0.6451 |  |
| Site: UCSD (vs UAB) | -9.7438 | 8.3973 | ±16.7946 | -1.160 | 0.2459 |  |
| Site: UW (vs UAB) | -5.1266 | 8.2806 | ±16.5611 | -0.619 | 0.5358 |  |
| Age (years) | +0.1829 | 0.3270 | ±0.6540 | +0.559 | 0.5759 |  |
| **BMI (kg/m2)** | **-1.1648** | 0.4938 | ±0.9875 | **-2.359** | **0.0183** | * |
| **Hypertension** | **-15.5956** | 7.7585 | ±15.5171 | **-2.010** | **0.0444** | * |
| High cholesterol | -1.4008 | 7.0129 | ±14.0259 | -0.200 | 0.8417 |  |
| Kidney disease | -33.0322 | 20.3075 | ±40.6150 | -1.627 | 0.1038 |  |
| Circulatory disease | +9.0225 | 13.4533 | ±26.9066 | +0.671 | 0.5024 |  |
| Avg. daily time 54-250 (%) | -69.4607 | 62.1673 | ±124.3347 | -1.117 | 0.2639 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **349**, R² = **0.0667**, Adj R² = **0.0362**, F-statistic = **2.19** (p = **0.0147**), Residual SE = **61.345** on **337** df, AIC = **3875.5**, BIC = **3921.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.0707** | 27.6692 | ±55.3384 | **+14.712** | **5.39e-49** | *** |
| Education: graduate level (vs college) | +4.9481 | 6.8135 | ±13.6271 | +0.726 | 0.4677 |  |
| Education: high school or below (vs college) | -7.5794 | 15.1492 | ±30.2985 | -0.500 | 0.6169 |  |
| Site: UCSD (vs UAB) | -10.3612 | 8.3904 | ±16.7807 | -1.235 | 0.2169 |  |
| Site: UW (vs UAB) | -5.2316 | 8.2840 | ±16.5680 | -0.632 | 0.5277 |  |
| Age (years) | +0.1651 | 0.3278 | ±0.6556 | +0.504 | 0.6144 |  |
| **BMI (kg/m2)** | **-1.1629** | 0.5109 | ±1.0219 | **-2.276** | **0.0228** | * |
| Hypertension | -15.1278 | 7.7747 | ±15.5494 | -1.946 | 0.0517 | . |
| High cholesterol | -1.7303 | 6.9960 | ±13.9921 | -0.247 | 0.8047 |  |
| Kidney disease | -32.7995 | 20.5414 | ±41.0828 | -1.597 | 0.1103 |  |
| Circulatory disease | +10.0082 | 13.3345 | ±26.6690 | +0.751 | 0.4529 |  |
| Time 181-250, pooled (%) | -8.1147 | 12.4197 | ±24.8394 | -0.653 | 0.5135 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **349**, R² = **0.0661**, Adj R² = **0.0357**, F-statistic = **2.17** (p = **0.0157**), Residual SE = **61.362** on **337** df, AIC = **3875.7**, BIC = **3922.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.3196** | 27.0066 | ±54.0132 | **+15.045** | **3.71e-51** | *** |
| Education: graduate level (vs college) | +4.9423 | 6.8052 | ±13.6103 | +0.726 | 0.4677 |  |
| Education: high school or below (vs college) | -7.6548 | 15.1466 | ±30.2933 | -0.505 | 0.6133 |  |
| Site: UCSD (vs UAB) | -10.4781 | 8.3546 | ±16.7093 | -1.254 | 0.2098 |  |
| Site: UW (vs UAB) | -5.2344 | 8.2888 | ±16.5776 | -0.632 | 0.5277 |  |
| Age (years) | +0.1592 | 0.3266 | ±0.6532 | +0.488 | 0.6258 |  |
| **BMI (kg/m2)** | **-1.1520** | 0.4925 | ±0.9849 | **-2.339** | **0.0193** | * |
| Hypertension | -15.2538 | 7.7846 | ±15.5692 | -1.959 | 0.0501 | . |
| High cholesterol | -1.4769 | 6.9928 | ±13.9856 | -0.211 | 0.8327 |  |
| Kidney disease | -33.0944 | 20.4082 | ±40.8165 | -1.622 | 0.1049 |  |
| Circulatory disease | +10.1620 | 13.3569 | ±26.7137 | +0.761 | 0.4468 |  |
| Avg. daily time 181-250 (%) | -6.2396 | 11.7937 | ±23.5874 | -0.529 | 0.5968 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **349**, R² = **0.0668**, Adj R² = **0.0363**, F-statistic = **2.19** (p = **0.0146**), Residual SE = **61.342** on **337** df, AIC = **3875.5**, BIC = **3921.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.2031** | 27.6988 | ±55.3976 | **+14.701** | **6.34e-49** | *** |
| Education: graduate level (vs college) | +4.9403 | 6.8140 | ±13.6280 | +0.725 | 0.4684 |  |
| Education: high school or below (vs college) | -7.5949 | 15.1488 | ±30.2975 | -0.501 | 0.6161 |  |
| Site: UCSD (vs UAB) | -10.3633 | 8.3905 | ±16.7810 | -1.235 | 0.2168 |  |
| Site: UW (vs UAB) | -5.2263 | 8.2840 | ±16.5680 | -0.631 | 0.5281 |  |
| Age (years) | +0.1646 | 0.3278 | ±0.6556 | +0.502 | 0.6156 |  |
| **BMI (kg/m2)** | **-1.1638** | 0.5117 | ±1.0234 | **-2.274** | **0.0229** | * |
| Hypertension | -15.1213 | 7.7745 | ±15.5490 | -1.945 | 0.0518 | . |
| High cholesterol | -1.7292 | 6.9947 | ±13.9893 | -0.247 | 0.8047 |  |
| Kidney disease | -32.7818 | 20.5469 | ±41.0937 | -1.595 | 0.1106 |  |
| Circulatory disease | +10.0043 | 13.3323 | ±26.6646 | +0.750 | 0.4530 |  |
| Time > 180 (%) | -8.3502 | 12.4108 | ±24.8215 | -0.673 | 0.5011 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **349**, R² = **0.0662**, Adj R² = **0.0357**, F-statistic = **2.17** (p = **0.0156**), Residual SE = **61.360** on **337** df, AIC = **3875.7**, BIC = **3922.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.4606** | 27.0188 | ±54.0377 | **+15.044** | **3.80e-51** | *** |
| Education: graduate level (vs college) | +4.9352 | 6.8056 | ±13.6112 | +0.725 | 0.4684 |  |
| Education: high school or below (vs college) | -7.6769 | 15.1459 | ±30.2918 | -0.507 | 0.6123 |  |
| Site: UCSD (vs UAB) | -10.4857 | 8.3542 | ±16.7085 | -1.255 | 0.2094 |  |
| Site: UW (vs UAB) | -5.2299 | 8.2894 | ±16.5788 | -0.631 | 0.5281 |  |
| Age (years) | +0.1584 | 0.3266 | ±0.6531 | +0.485 | 0.6277 |  |
| **BMI (kg/m2)** | **-1.1526** | 0.4928 | ±0.9855 | **-2.339** | **0.0193** | * |
| Hypertension | -15.2483 | 7.7845 | ±15.5690 | -1.959 | 0.0501 | . |
| High cholesterol | -1.4698 | 6.9923 | ±13.9847 | -0.210 | 0.8335 |  |
| Kidney disease | -33.0813 | 20.4130 | ±40.8260 | -1.621 | 0.1051 |  |
| Circulatory disease | +10.1632 | 13.3546 | ±26.7091 | +0.761 | 0.4466 |  |
| Avg. daily time > 180 (%) | -6.4991 | 11.7822 | ±23.5644 | -0.552 | 0.5812 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 349)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **349**, R² = **0.0740**, Adj R² = **0.0438**, F-statistic = **2.45** (p = **0.0059**), Residual SE = **61.103** on **337** df, AIC = **3872.8**, BIC = **3919.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+409.2278** | 26.1377 | ±52.2754 | **+15.657** | **2.99e-55** | *** |
| Education: graduate level (vs college) | +4.0669 | 6.8381 | ±13.6761 | +0.595 | 0.5520 |  |
| Education: high school or below (vs college) | -7.1154 | 15.0949 | ±30.1899 | -0.471 | 0.6374 |  |
| Site: UCSD (vs UAB) | -10.7691 | 8.3637 | ±16.7273 | -1.288 | 0.1979 |  |
| Site: UW (vs UAB) | -4.7032 | 8.2794 | ±16.5589 | -0.568 | 0.5700 |  |
| Age (years) | +0.0624 | 0.3280 | ±0.6561 | +0.190 | 0.8491 |  |
| **BMI (kg/m2)** | **-1.0548** | 0.4770 | ±0.9540 | **-2.211** | **0.0270** | * |
| Hypertension | -14.6620 | 7.7016 | ±15.4032 | -1.904 | 0.0569 | . |
| High cholesterol | -0.6365 | 6.9586 | ±13.9172 | -0.091 | 0.9271 |  |
| Kidney disease | -31.8496 | 19.9102 | ±39.8204 | -1.600 | 0.1097 |  |
| Circulatory disease | +9.8390 | 13.4057 | ±26.8113 | +0.734 | 0.4630 |  |
| Nocturnal time > 180 (%) | -17.1428 | 10.8986 | ±21.7971 | -1.573 | 0.1157 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 346; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **346**, R² = **0.1248**, Adj R² = **0.0987**, F-statistic = **4.78** (p = **2.01e-06**), Residual SE = **16.037** on **335** df, AIC = **2913.0**, BIC = **2955.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.0937** | 8.3045 | ±16.6091 | **+6.755** | **1.43e-11** | *** |
| Education: graduate level (vs college) | -3.5493 | 1.8441 | ±3.6882 | -1.925 | 0.0543 | . |
| Education: high school or below (vs college) | +0.3223 | 3.3631 | ±6.7262 | +0.096 | 0.9237 |  |
| Site: UCSD (vs UAB) | -1.8928 | 2.3291 | ±4.6582 | -0.813 | 0.4164 |  |
| **Site: UW (vs UAB)** | **-4.4324** | 2.1258 | ±4.2516 | **-2.085** | **0.0371** | * |
| **Age (years)** | **-0.2951** | 0.0873 | ±0.1747 | **-3.378** | **7.29e-04** | *** |
| **BMI (kg/m2)** | **+0.4696** | 0.1583 | ±0.3167 | **+2.966** | **0.0030** | ** |
| Hypertension | -0.0692 | 2.1014 | ±4.2029 | -0.033 | 0.9737 |  |
| High cholesterol | -0.6058 | 1.9248 | ±3.8496 | -0.315 | 0.7530 |  |
| Kidney disease | -2.1559 | 5.2242 | ±10.4483 | -0.413 | 0.6798 |  |
| Circulatory disease | -1.7947 | 2.5443 | ±5.0885 | -0.705 | 0.4806 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **346**, R² = **0.1256**, Adj R² = **0.0968**, F-statistic = **4.36** (p = **4.12e-06**), Residual SE = **16.055** on **334** df, AIC = **2914.7**, BIC = **2960.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.9108** | 18.3902 | ±36.7804 | **+2.605** | **0.0092** | ** |
| Education: graduate level (vs college) | -3.5149 | 1.8496 | ±3.6993 | -1.900 | 0.0574 | . |
| Education: high school or below (vs college) | +0.2863 | 3.3539 | ±6.7078 | +0.085 | 0.9320 |  |
| Site: UCSD (vs UAB) | -1.8186 | 2.3287 | ±4.6573 | -0.781 | 0.4348 |  |
| **Site: UW (vs UAB)** | **-4.3425** | 2.1275 | ±4.2551 | **-2.041** | **0.0412** | * |
| **Age (years)** | **-0.2998** | 0.0877 | ±0.1754 | **-3.417** | **6.32e-04** | *** |
| **BMI (kg/m2)** | **+0.4620** | 0.1578 | ±0.3156 | **+2.928** | **0.0034** | ** |
| Hypertension | -0.1541 | 2.1110 | ±4.2221 | -0.073 | 0.9418 |  |
| High cholesterol | -0.8194 | 1.9993 | ±3.9987 | -0.410 | 0.6819 |  |
| Kidney disease | -2.0739 | 5.2332 | ±10.4664 | -0.396 | 0.6919 |  |
| Circulatory disease | -1.7298 | 2.5455 | ±5.0909 | -0.680 | 0.4968 |  |
| HbA1c (%) | +1.5785 | 3.2405 | ±6.4811 | +0.487 | 0.6262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **346**, R² = **0.1277**, Adj R² = **0.0990**, F-statistic = **4.44** (p = **2.94e-06**), Residual SE = **16.035** on **334** df, AIC = **2913.8**, BIC = **2960.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.2412** | 16.1941 | ±32.3881 | **+2.608** | **0.0091** | ** |
| Education: graduate level (vs college) | -3.5050 | 1.8456 | ±3.6913 | -1.899 | 0.0576 | . |
| Education: high school or below (vs college) | +0.4495 | 3.3702 | ±6.7404 | +0.133 | 0.8939 |  |
| Site: UCSD (vs UAB) | -2.0217 | 2.3353 | ±4.6706 | -0.866 | 0.3867 |  |
| **Site: UW (vs UAB)** | **-4.5705** | 2.1136 | ±4.2272 | **-2.162** | **0.0306** | * |
| **Age (years)** | **-0.2906** | 0.0879 | ±0.1757 | **-3.307** | **9.42e-04** | *** |
| **BMI (kg/m2)** | **+0.4589** | 0.1576 | ±0.3152 | **+2.912** | **0.0036** | ** |
| Hypertension | -0.2658 | 2.0827 | ±4.1655 | -0.128 | 0.8985 |  |
| High cholesterol | -0.5235 | 1.9386 | ±3.8773 | -0.270 | 0.7871 |  |
| Kidney disease | -2.1933 | 5.2799 | ±10.5599 | -0.415 | 0.6778 |  |
| Circulatory disease | -1.7888 | 2.5442 | ±5.0883 | -0.703 | 0.4820 |  |
| Mean glucose (mg/dL) | +0.1225 | 0.1208 | ±0.2415 | +1.015 | 0.3103 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **346**, R² = **0.1277**, Adj R² = **0.0990**, F-statistic = **4.44** (p = **2.94e-06**), Residual SE = **16.035** on **334** df, AIC = **2913.8**, BIC = **2960.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +25.2838 | 31.7292 | ±63.4584 | +0.797 | 0.4255 |  |
| Education: graduate level (vs college) | -3.5050 | 1.8456 | ±3.6913 | -1.899 | 0.0576 | . |
| Education: high school or below (vs college) | +0.4495 | 3.3702 | ±6.7404 | +0.133 | 0.8939 |  |
| Site: UCSD (vs UAB) | -2.0217 | 2.3353 | ±4.6706 | -0.866 | 0.3867 |  |
| **Site: UW (vs UAB)** | **-4.5705** | 2.1136 | ±4.2272 | **-2.162** | **0.0306** | * |
| **Age (years)** | **-0.2906** | 0.0879 | ±0.1757 | **-3.307** | **9.42e-04** | *** |
| **BMI (kg/m2)** | **+0.4589** | 0.1576 | ±0.3152 | **+2.912** | **0.0036** | ** |
| Hypertension | -0.2658 | 2.0827 | ±4.1655 | -0.128 | 0.8985 |  |
| High cholesterol | -0.5235 | 1.9386 | ±3.8773 | -0.270 | 0.7871 |  |
| Kidney disease | -2.1933 | 5.2799 | ±10.5599 | -0.415 | 0.6778 |  |
| Circulatory disease | -1.7888 | 2.5442 | ±5.0883 | -0.703 | 0.4820 |  |
| GMI (%) | +5.1231 | 5.0490 | ±10.0979 | +1.015 | 0.3103 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **346**, R² = **0.1300**, Adj R² = **0.1014**, F-statistic = **4.54** (p = **2.03e-06**), Residual SE = **16.014** on **334** df, AIC = **2912.9**, BIC = **2959.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+40.6737** | 13.2113 | ±26.4226 | **+3.079** | **0.0021** | ** |
| Education: graduate level (vs college) | -3.3541 | 1.8373 | ±3.6746 | -1.826 | 0.0679 | . |
| Education: high school or below (vs college) | +0.5215 | 3.3742 | ±6.7485 | +0.155 | 0.8772 |  |
| Site: UCSD (vs UAB) | -2.2580 | 2.3351 | ±4.6703 | -0.967 | 0.3336 |  |
| **Site: UW (vs UAB)** | **-4.7044** | 2.1162 | ±4.2324 | **-2.223** | **0.0262** | * |
| **Age (years)** | **-0.2757** | 0.0879 | ±0.1757 | **-3.138** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.4397** | 0.1539 | ±0.3078 | **+2.857** | **0.0043** | ** |
| Hypertension | -0.2568 | 2.0775 | ±4.1551 | -0.124 | 0.9016 |  |
| High cholesterol | -0.6081 | 1.9259 | ±3.8517 | -0.316 | 0.7522 |  |
| Kidney disease | -1.9757 | 5.2188 | ±10.4375 | -0.379 | 0.7050 |  |
| Circulatory disease | -1.6846 | 2.5228 | ±5.0456 | -0.668 | 0.5043 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.1331 | 0.0960 | ±0.1919 | +1.387 | 0.1656 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **346**, R² = **0.1292**, Adj R² = **0.1006**, F-statistic = **4.51** (p = **2.30e-06**), Residual SE = **16.021** on **334** df, AIC = **2913.2**, BIC = **2959.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6581** | 10.9625 | ±21.9249 | **+4.347** | **1.38e-05** | *** |
| Education: graduate level (vs college) | -3.3233 | 1.8527 | ±3.7053 | -1.794 | 0.0729 | . |
| Education: high school or below (vs college) | +0.4831 | 3.3058 | ±6.6116 | +0.146 | 0.8838 |  |
| Site: UCSD (vs UAB) | -1.6374 | 2.3278 | ±4.6555 | -0.703 | 0.4818 |  |
| **Site: UW (vs UAB)** | **-4.2661** | 2.1173 | ±4.2346 | **-2.015** | **0.0439** | * |
| **Age (years)** | **-0.2956** | 0.0873 | ±0.1747 | **-3.385** | **7.12e-04** | *** |
| **BMI (kg/m2)** | **+0.4622** | 0.1573 | ±0.3147 | **+2.938** | **0.0033** | ** |
| Hypertension | -0.1489 | 2.0956 | ±4.1912 | -0.071 | 0.9433 |  |
| High cholesterol | -0.4331 | 1.9414 | ±3.8827 | -0.223 | 0.8235 |  |
| Kidney disease | -2.5602 | 5.3362 | ±10.6724 | -0.480 | 0.6314 |  |
| Circulatory disease | -1.8669 | 2.5278 | ±5.0556 | -0.739 | 0.4602 |  |
| Glucose SD, pooled (mg/dL) | +0.5004 | 0.4248 | ±0.8496 | +1.178 | 0.2388 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **346**, R² = **0.1288**, Adj R² = **0.1001**, F-statistic = **4.49** (p = **2.48e-06**), Residual SE = **16.025** on **334** df, AIC = **2913.4**, BIC = **2959.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.7962** | 10.3726 | ±20.7452 | **+4.704** | **2.55e-06** | *** |
| Education: graduate level (vs college) | -3.3244 | 1.8548 | ±3.7096 | -1.792 | 0.0731 | . |
| Education: high school or below (vs college) | +0.5149 | 3.3095 | ±6.6190 | +0.156 | 0.8763 |  |
| Site: UCSD (vs UAB) | -1.6216 | 2.3274 | ±4.6549 | -0.697 | 0.4860 |  |
| **Site: UW (vs UAB)** | **-4.2525** | 2.1220 | ±4.2440 | **-2.004** | **0.0451** | * |
| **Age (years)** | **-0.2944** | 0.0874 | ±0.1748 | **-3.370** | **7.53e-04** | *** |
| **BMI (kg/m2)** | **+0.4586** | 0.1561 | ±0.3123 | **+2.937** | **0.0033** | ** |
| Hypertension | -0.0925 | 2.1009 | ±4.2019 | -0.044 | 0.9649 |  |
| High cholesterol | -0.4684 | 1.9363 | ±3.8727 | -0.242 | 0.8089 |  |
| Kidney disease | -2.5229 | 5.3272 | ±10.6544 | -0.474 | 0.6358 |  |
| Circulatory disease | -1.8144 | 2.5493 | ±5.0987 | -0.712 | 0.4766 |  |
| Avg. daily SD (mg/dL) | +0.4712 | 0.4183 | ±0.8367 | +1.126 | 0.2600 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **346**, R² = **0.1264**, Adj R² = **0.0976**, F-statistic = **4.39** (p = **3.60e-06**), Residual SE = **16.047** on **334** df, AIC = **2914.3**, BIC = **2960.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2074** | 10.5237 | ±21.0473 | **+4.866** | **1.14e-06** | *** |
| Education: graduate level (vs college) | -3.4329 | 1.8558 | ±3.7115 | -1.850 | 0.0643 | . |
| Education: high school or below (vs college) | +0.3733 | 3.3330 | ±6.6659 | +0.112 | 0.9108 |  |
| Site: UCSD (vs UAB) | -1.7054 | 2.3319 | ±4.6638 | -0.731 | 0.4646 |  |
| **Site: UW (vs UAB)** | **-4.2893** | 2.1212 | ±4.2425 | **-2.022** | **0.0432** | * |
| **Age (years)** | **-0.2968** | 0.0875 | ±0.1750 | **-3.392** | **6.93e-04** | *** |
| **BMI (kg/m2)** | **+0.4689** | 0.1582 | ±0.3165 | **+2.963** | **0.0030** | ** |
| Hypertension | -0.0511 | 2.1089 | ±4.2178 | -0.024 | 0.9807 |  |
| High cholesterol | -0.5277 | 1.9326 | ±3.8653 | -0.273 | 0.7848 |  |
| Kidney disease | -2.3687 | 5.2901 | ±10.5802 | -0.448 | 0.6543 |  |
| Circulatory disease | -1.8427 | 2.5366 | ±5.0733 | -0.726 | 0.4676 |  |
| CV (%) | +0.3262 | 0.4402 | ±0.8804 | +0.741 | 0.4587 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **346**, R² = **0.1263**, Adj R² = **0.0975**, F-statistic = **4.39** (p = **3.66e-06**), Residual SE = **16.048** on **334** df, AIC = **2914.4**, BIC = **2960.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.4632** | 10.3065 | ±20.6130 | **+5.867** | **4.45e-09** | *** |
| Education: graduate level (vs college) | -3.4244 | 1.8548 | ±3.7097 | -1.846 | 0.0649 | . |
| Education: high school or below (vs college) | +0.3582 | 3.3307 | ±6.6613 | +0.108 | 0.9144 |  |
| Site: UCSD (vs UAB) | -1.7502 | 2.3329 | ±4.6658 | -0.750 | 0.4531 |  |
| **Site: UW (vs UAB)** | **-4.3302** | 2.1251 | ±4.2502 | **-2.038** | **0.0416** | * |
| **Age (years)** | **-0.2961** | 0.0874 | ±0.1748 | **-3.388** | **7.05e-04** | *** |
| **BMI (kg/m2)** | **+0.4690** | 0.1585 | ±0.3170 | **+2.959** | **0.0031** | ** |
| Hypertension | -0.0760 | 2.1066 | ±4.2133 | -0.036 | 0.9712 |  |
| High cholesterol | -0.5206 | 1.9353 | ±3.8706 | -0.269 | 0.7879 |  |
| Kidney disease | -2.3082 | 5.2611 | ±10.5222 | -0.439 | 0.6609 |  |
| Circulatory disease | -1.8346 | 2.5353 | ±5.0706 | -0.724 | 0.4693 |  |
| Mean / SD ratio | -0.6440 | 0.9006 | ±1.8013 | -0.715 | 0.4746 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **346**, R² = **0.1267**, Adj R² = **0.0980**, F-statistic = **4.41** (p = **3.41e-06**), Residual SE = **16.044** on **334** df, AIC = **2914.2**, BIC = **2960.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+60.6903** | 10.1321 | ±20.2641 | **+5.990** | **2.10e-09** | *** |
| Education: graduate level (vs college) | -3.3982 | 1.8569 | ±3.7137 | -1.830 | 0.0672 | . |
| Education: high school or below (vs college) | +0.3888 | 3.3249 | ±6.6498 | +0.117 | 0.9069 |  |
| Site: UCSD (vs UAB) | -1.7061 | 2.3350 | ±4.6700 | -0.731 | 0.4650 |  |
| **Site: UW (vs UAB)** | **-4.3076** | 2.1269 | ±4.2537 | **-2.025** | **0.0428** | * |
| **Age (years)** | **-0.2954** | 0.0874 | ±0.1749 | **-3.378** | **7.30e-04** | *** |
| **BMI (kg/m2)** | **+0.4643** | 0.1577 | ±0.3154 | **+2.945** | **0.0032** | ** |
| Hypertension | -0.0304 | 2.1142 | ±4.2285 | -0.014 | 0.9885 |  |
| High cholesterol | -0.5381 | 1.9299 | ±3.8598 | -0.279 | 0.7804 |  |
| Kidney disease | -2.3549 | 5.2576 | ±10.5152 | -0.448 | 0.6542 |  |
| Circulatory disease | -1.8108 | 2.5510 | ±5.1020 | -0.710 | 0.4778 |  |
| Avg. daily mean/SD | -0.5947 | 0.7337 | ±1.4675 | -0.811 | 0.4176 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **346**, R² = **0.1258**, Adj R² = **0.0970**, F-statistic = **4.37** (p = **3.98e-06**), Residual SE = **16.053** on **334** df, AIC = **2914.6**, BIC = **2960.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.3806** | 10.7306 | ±21.4611 | **+4.881** | **1.05e-06** | *** |
| Education: graduate level (vs college) | -3.5475 | 1.8505 | ±3.7010 | -1.917 | 0.0552 | . |
| Education: high school or below (vs college) | +0.1857 | 3.3903 | ±6.7805 | +0.055 | 0.9563 |  |
| Site: UCSD (vs UAB) | -1.7807 | 2.3560 | ±4.7120 | -0.756 | 0.4498 |  |
| **Site: UW (vs UAB)** | **-4.2644** | 2.1704 | ±4.3408 | **-1.965** | **0.0494** | * |
| **Age (years)** | **-0.2884** | 0.0885 | ±0.1770 | **-3.259** | **0.0011** | ** |
| **BMI (kg/m2)** | **+0.4751** | 0.1580 | ±0.3160 | **+3.007** | **0.0026** | ** |
| Hypertension | +0.0001 | 2.1182 | ±4.2364 | +0.000 | 1.0000 |  |
| High cholesterol | -0.6784 | 1.9376 | ±3.8753 | -0.350 | 0.7263 |  |
| Kidney disease | -2.3439 | 5.2429 | ±10.4858 | -0.447 | 0.6548 |  |
| Circulatory disease | -1.8385 | 2.5640 | ±5.1280 | -0.717 | 0.4733 |  |
| MAG (mg/dL/h) | +0.0904 | 0.1620 | ±0.3240 | +0.558 | 0.5770 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **346**, R² = **0.1263**, Adj R² = **0.0975**, F-statistic = **4.39** (p = **3.69e-06**), Residual SE = **16.048** on **334** df, AIC = **2914.4**, BIC = **2960.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0011** | 11.7394 | ±23.4787 | **+4.344** | **1.40e-05** | *** |
| Education: graduate level (vs college) | -3.4875 | 1.8581 | ±3.7161 | -1.877 | 0.0605 | . |
| Education: high school or below (vs college) | +0.3815 | 3.3381 | ±6.6762 | +0.114 | 0.9090 |  |
| Site: UCSD (vs UAB) | -1.7626 | 2.3488 | ±4.6976 | -0.750 | 0.4530 |  |
| **Site: UW (vs UAB)** | **-4.3284** | 2.1499 | ±4.2998 | **-2.013** | **0.0441** | * |
| **Age (years)** | **-0.2931** | 0.0879 | ±0.1758 | **-3.335** | **8.53e-04** | *** |
| **BMI (kg/m2)** | **+0.4765** | 0.1628 | ±0.3255 | **+2.928** | **0.0034** | ** |
| Hypertension | -0.0028 | 2.1184 | ±4.2369 | -0.001 | 0.9990 |  |
| High cholesterol | -0.5904 | 1.9276 | ±3.8551 | -0.306 | 0.7594 |  |
| Kidney disease | -2.3073 | 5.2754 | ±10.5509 | -0.437 | 0.6618 |  |
| Circulatory disease | -1.8649 | 2.5571 | ±5.1142 | -0.729 | 0.4658 |  |
| Avg. daily range (mg/dL) | +0.0581 | 0.0859 | ±0.1719 | +0.676 | 0.4988 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **346**, R² = **0.1351**, Adj R² = **0.1067**, F-statistic = **4.74** (p = **8.95e-07**), Residual SE = **15.966** on **334** df, AIC = **2910.9**, BIC = **2957.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.8900** | 8.4446 | ±16.8891 | **+6.145** | **8.01e-10** | *** |
| **Education: graduate level (vs college)** | **-3.6752** | 1.8409 | ±3.6818 | **-1.996** | **0.0459** | * |
| Education: high school or below (vs college) | +0.0680 | 3.2913 | ±6.5825 | +0.021 | 0.9835 |  |
| Site: UCSD (vs UAB) | -1.7829 | 2.3144 | ±4.6287 | -0.770 | 0.4411 |  |
| **Site: UW (vs UAB)** | **-4.6317** | 2.1008 | ±4.2017 | **-2.205** | **0.0275** | * |
| **Age (years)** | **-0.3024** | 0.0859 | ±0.1718 | **-3.520** | **4.31e-04** | *** |
| **BMI (kg/m2)** | **+0.4656** | 0.1562 | ±0.3124 | **+2.981** | **0.0029** | ** |
| Hypertension | -0.3496 | 2.1094 | ±4.2187 | -0.166 | 0.8684 |  |
| High cholesterol | -0.6059 | 1.9125 | ±3.8249 | -0.317 | 0.7514 |  |
| Kidney disease | -1.9387 | 5.1677 | ±10.3353 | -0.375 | 0.7075 |  |
| Circulatory disease | -1.9286 | 2.4983 | ±4.9966 | -0.772 | 0.4401 |  |
| **SD of daily means (mg/dL)** | **+0.9758** | 0.4941 | ±0.9881 | **+1.975** | **0.0483** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **346**, R² = **0.1329**, Adj R² = **0.1043**, F-statistic = **4.65** (p = **1.29e-06**), Residual SE = **15.987** on **334** df, AIC = **2911.8**, BIC = **2957.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +567.4436 | 302.4155 | ±604.8309 | +1.876 | 0.0606 | . |
| Education: graduate level (vs college) | -3.4102 | 1.8565 | ±3.7131 | -1.837 | 0.0662 | . |
| Education: high school or below (vs college) | +0.5052 | 3.2861 | ±6.5723 | +0.154 | 0.8778 |  |
| Site: UCSD (vs UAB) | -1.6315 | 2.3478 | ±4.6956 | -0.695 | 0.4871 |  |
| **Site: UW (vs UAB)** | **-4.2551** | 2.1266 | ±4.2532 | **-2.001** | **0.0454** | * |
| **Age (years)** | **-0.2876** | 0.0887 | ±0.1775 | **-3.241** | **0.0012** | ** |
| **BMI (kg/m2)** | **+0.4785** | 0.1729 | ±0.3458 | **+2.767** | **0.0057** | ** |
| Hypertension | -0.1297 | 2.0782 | ±4.1564 | -0.062 | 0.9503 |  |
| High cholesterol | -0.7050 | 1.9156 | ±3.8312 | -0.368 | 0.7129 |  |
| Kidney disease | -2.4249 | 5.2929 | ±10.5858 | -0.458 | 0.6469 |  |
| Circulatory disease | -1.8873 | 2.5100 | ±5.0200 | -0.752 | 0.4521 |  |
| Time in range 70-180, pooled (%) | -5.1455 | 3.0508 | ±6.1015 | -1.687 | 0.0917 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **346**, R² = **0.1371**, Adj R² = **0.1086**, F-statistic = **4.82** (p = **6.55e-07**), Residual SE = **15.949** on **334** df, AIC = **2910.1**, BIC = **2956.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+668.8642** | 286.2631 | ±572.5262 | **+2.337** | **0.0195** | * |
| Education: graduate level (vs college) | -3.3687 | 1.8464 | ±3.6929 | -1.824 | 0.0681 | . |
| Education: high school or below (vs college) | +0.6466 | 3.2589 | ±6.5178 | +0.198 | 0.8427 |  |
| Site: UCSD (vs UAB) | -1.6122 | 2.3207 | ±4.6414 | -0.695 | 0.4872 |  |
| **Site: UW (vs UAB)** | **-4.4027** | 2.1096 | ±4.2192 | **-2.087** | **0.0369** | * |
| **Age (years)** | **-0.2802** | 0.0878 | ±0.1756 | **-3.192** | **0.0014** | ** |
| **BMI (kg/m2)** | **+0.4739** | 0.1618 | ±0.3237 | **+2.929** | **0.0034** | ** |
| Hypertension | +0.0797 | 2.0907 | ±4.1813 | +0.038 | 0.9696 |  |
| High cholesterol | -0.7904 | 1.9092 | ±3.8183 | -0.414 | 0.6789 |  |
| Kidney disease | -2.2188 | 5.3517 | ±10.7033 | -0.415 | 0.6784 |  |
| Circulatory disease | -2.0811 | 2.5379 | ±5.0759 | -0.820 | 0.4122 |  |
| **Avg. daily time in range 70-180 (%)** | **-6.1638** | 2.8804 | ±5.7608 | **-2.140** | **0.0324** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **346**, R² = **0.1248**, Adj R² = **0.0960**, F-statistic = **4.33** (p = **4.61e-06**), Residual SE = **16.061** on **334** df, AIC = **2915.0**, BIC = **2961.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.0935** | 8.3547 | ±16.7094 | **+6.714** | **1.89e-11** | *** |
| Education: graduate level (vs college) | -3.5493 | 1.8521 | ±3.7041 | -1.916 | 0.0553 | . |
| Education: high school or below (vs college) | +0.3223 | 3.3797 | ±6.7594 | +0.095 | 0.9240 |  |
| Site: UCSD (vs UAB) | -1.8927 | 2.3581 | ±4.7161 | -0.803 | 0.4222 |  |
| **Site: UW (vs UAB)** | **-4.4323** | 2.1438 | ±4.2877 | **-2.067** | **0.0387** | * |
| **Age (years)** | **-0.2951** | 0.0876 | ±0.1751 | **-3.370** | **7.51e-04** | *** |
| **BMI (kg/m2)** | **+0.4696** | 0.1586 | ±0.3171 | **+2.962** | **0.0031** | ** |
| Hypertension | -0.0692 | 2.1145 | ±4.2291 | -0.033 | 0.9739 |  |
| High cholesterol | -0.6058 | 1.9281 | ±3.8562 | -0.314 | 0.7534 |  |
| Kidney disease | -2.1558 | 5.2526 | ±10.5052 | -0.410 | 0.6815 |  |
| Circulatory disease | -1.7948 | 2.5510 | ±5.1020 | -0.704 | 0.4817 |  |
| Any reading < 54 during wear (0/1) | +0.0010 | 2.1553 | ±4.3107 | +0.000 | 0.9996 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **346**, R² = **0.1252**, Adj R² = **0.0964**, F-statistic = **4.35** (p = **4.35e-06**), Residual SE = **16.058** on **334** df, AIC = **2914.8**, BIC = **2961.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.9622** | 8.2921 | ±16.5843 | **+6.749** | **1.49e-11** | *** |
| Education: graduate level (vs college) | -3.5408 | 1.8495 | ±3.6990 | -1.914 | 0.0556 | . |
| Education: high school or below (vs college) | +0.3946 | 3.3814 | ±6.7628 | +0.117 | 0.9071 |  |
| Site: UCSD (vs UAB) | -1.7954 | 2.3411 | ±4.6823 | -0.767 | 0.4432 |  |
| **Site: UW (vs UAB)** | **-4.3845** | 2.1340 | ±4.2679 | **-2.055** | **0.0399** | * |
| **Age (years)** | **-0.2937** | 0.0875 | ±0.1751 | **-3.356** | **7.91e-04** | *** |
| **BMI (kg/m2)** | **+0.4663** | 0.1584 | ±0.3168 | **+2.944** | **0.0032** | ** |
| Hypertension | -0.1247 | 2.1220 | ±4.2440 | -0.059 | 0.9532 |  |
| High cholesterol | -0.5941 | 1.9296 | ±3.8593 | -0.308 | 0.7582 |  |
| Kidney disease | -2.0872 | 5.2386 | ±10.4773 | -0.398 | 0.6903 |  |
| Circulatory disease | -1.8833 | 2.5699 | ±5.1399 | -0.733 | 0.4637 |  |
| Time < 54 (%) | +6.1824 | 14.2542 | ±28.5084 | +0.434 | 0.6645 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **346**, R² = **0.1251**, Adj R² = **0.0963**, F-statistic = **4.34** (p = **4.43e-06**), Residual SE = **16.059** on **334** df, AIC = **2914.9**, BIC = **2961.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.0411** | 8.3011 | ±16.6023 | **+6.751** | **1.47e-11** | *** |
| Education: graduate level (vs college) | -3.5633 | 1.8481 | ±3.6961 | -1.928 | 0.0538 | . |
| Education: high school or below (vs college) | +0.3429 | 3.3671 | ±6.7341 | +0.102 | 0.9189 |  |
| Site: UCSD (vs UAB) | -1.8505 | 2.3347 | ±4.6694 | -0.793 | 0.4280 |  |
| **Site: UW (vs UAB)** | **-4.4234** | 2.1336 | ±4.2671 | **-2.073** | **0.0381** | * |
| **Age (years)** | **-0.2944** | 0.0875 | ±0.1750 | **-3.365** | **7.66e-04** | *** |
| **BMI (kg/m2)** | **+0.4677** | 0.1584 | ±0.3168 | **+2.953** | **0.0031** | ** |
| Hypertension | -0.0874 | 2.1101 | ±4.2203 | -0.041 | 0.9670 |  |
| High cholesterol | -0.5929 | 1.9340 | ±3.8681 | -0.307 | 0.7592 |  |
| Kidney disease | -2.1219 | 5.2368 | ±10.4736 | -0.405 | 0.6853 |  |
| Circulatory disease | -1.8997 | 2.5855 | ±5.1710 | -0.735 | 0.4625 |  |
| Avg. daily time < 54 (%) | +6.1488 | 18.7229 | ±37.4457 | +0.328 | 0.7426 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **346**, R² = **0.1250**, Adj R² = **0.0962**, F-statistic = **4.34** (p = **4.48e-06**), Residual SE = **16.060** on **334** df, AIC = **2914.9**, BIC = **2961.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.8586** | 8.3449 | ±16.6898 | **+6.694** | **2.18e-11** | *** |
| Education: graduate level (vs college) | -3.5256 | 1.8632 | ±3.7264 | -1.892 | 0.0585 | . |
| Education: high school or below (vs college) | +0.2934 | 3.3573 | ±6.7145 | +0.087 | 0.9304 |  |
| Site: UCSD (vs UAB) | -1.8546 | 2.3358 | ±4.6716 | -0.794 | 0.4272 |  |
| **Site: UW (vs UAB)** | **-4.3885** | 2.1381 | ±4.2761 | **-2.053** | **0.0401** | * |
| **Age (years)** | **-0.2951** | 0.0876 | ±0.1753 | **-3.368** | **7.58e-04** | *** |
| **BMI (kg/m2)** | **+0.4705** | 0.1583 | ±0.3166 | **+2.972** | **0.0030** | ** |
| Hypertension | -0.0162 | 2.1145 | ±4.2289 | -0.008 | 0.9939 |  |
| High cholesterol | -0.6649 | 1.9696 | ±3.9392 | -0.338 | 0.7357 |  |
| Kidney disease | -2.1097 | 5.2458 | ±10.4916 | -0.402 | 0.6876 |  |
| Circulatory disease | -1.7919 | 2.5549 | ±5.1099 | -0.701 | 0.4831 |  |
| Time 54-69, pooled (%) | +1.2595 | 4.8590 | ±9.7181 | +0.259 | 0.7955 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **346**, R² = **0.1248**, Adj R² = **0.0960**, F-statistic = **4.33** (p = **4.60e-06**), Residual SE = **16.061** on **334** df, AIC = **2915.0**, BIC = **2961.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.1534** | 8.3434 | ±16.6868 | **+6.730** | **1.69e-11** | *** |
| Education: graduate level (vs college) | -3.5592 | 1.8632 | ±3.7264 | -1.910 | 0.0561 | . |
| Education: high school or below (vs college) | +0.3308 | 3.3878 | ±6.7756 | +0.098 | 0.9222 |  |
| Site: UCSD (vs UAB) | -1.8995 | 2.3354 | ±4.6709 | -0.813 | 0.4160 |  |
| **Site: UW (vs UAB)** | **-4.4367** | 2.1322 | ±4.2643 | **-2.081** | **0.0374** | * |
| **Age (years)** | **-0.2950** | 0.0878 | ±0.1755 | **-3.362** | **7.74e-04** | *** |
| **BMI (kg/m2)** | **+0.4694** | 0.1585 | ±0.3170 | **+2.962** | **0.0031** | ** |
| Hypertension | -0.0963 | 2.1347 | ±4.2694 | -0.045 | 0.9640 |  |
| High cholesterol | -0.5922 | 1.9592 | ±3.9185 | -0.302 | 0.7625 |  |
| Kidney disease | -2.1681 | 5.2494 | ±10.4988 | -0.413 | 0.6796 |  |
| Circulatory disease | -1.7866 | 2.5473 | ±5.0946 | -0.701 | 0.4831 |  |
| Avg. daily time 54-69 (%) | -0.3944 | 4.9736 | ±9.9473 | -0.079 | 0.9368 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **346**, R² = **0.1251**, Adj R² = **0.0963**, F-statistic = **4.34** (p = **4.41e-06**), Residual SE = **16.059** on **334** df, AIC = **2914.9**, BIC = **2961.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.8018** | 8.3335 | ±16.6671 | **+6.696** | **2.14e-11** | *** |
| Education: graduate level (vs college) | -3.5210 | 1.8625 | ±3.7251 | -1.890 | 0.0587 | . |
| Education: high school or below (vs college) | +0.3065 | 3.3569 | ±6.7137 | +0.091 | 0.9272 |  |
| Site: UCSD (vs UAB) | -1.8281 | 2.3371 | ±4.6742 | -0.782 | 0.4341 |  |
| **Site: UW (vs UAB)** | **-4.3726** | 2.1383 | ±4.2766 | **-2.045** | **0.0409** | * |
| **Age (years)** | **-0.2948** | 0.0876 | ±0.1751 | **-3.367** | **7.60e-04** | *** |
| **BMI (kg/m2)** | **+0.4699** | 0.1581 | ±0.3161 | **+2.973** | **0.0030** | ** |
| Hypertension | -0.0227 | 2.1069 | ±4.2138 | -0.011 | 0.9914 |  |
| High cholesterol | -0.6691 | 1.9567 | ±3.9133 | -0.342 | 0.7324 |  |
| Kidney disease | -2.0888 | 5.2480 | ±10.4960 | -0.398 | 0.6906 |  |
| Circulatory disease | -1.8117 | 2.5554 | ±5.1108 | -0.709 | 0.4783 |  |
| Time < 70 (%) | +1.4040 | 4.1883 | ±8.3766 | +0.335 | 0.7375 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **346**, R² = **0.1248**, Adj R² = **0.0960**, F-statistic = **4.33** (p = **4.61e-06**), Residual SE = **16.061** on **334** df, AIC = **2915.0**, BIC = **2961.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.0957** | 8.3405 | ±16.6810 | **+6.726** | **1.75e-11** | *** |
| Education: graduate level (vs college) | -3.5496 | 1.8597 | ±3.7195 | -1.909 | 0.0563 | . |
| Education: high school or below (vs college) | +0.3225 | 3.3822 | ±6.7644 | +0.095 | 0.9240 |  |
| Site: UCSD (vs UAB) | -1.8931 | 2.3341 | ±4.6683 | -0.811 | 0.4173 |  |
| **Site: UW (vs UAB)** | **-4.4325** | 2.1327 | ±4.2653 | **-2.078** | **0.0377** | * |
| **Age (years)** | **-0.2951** | 0.0877 | ±0.1754 | **-3.365** | **7.67e-04** | *** |
| **BMI (kg/m2)** | **+0.4696** | 0.1585 | ±0.3170 | **+2.963** | **0.0030** | ** |
| Hypertension | -0.0700 | 2.1236 | ±4.2471 | -0.033 | 0.9737 |  |
| High cholesterol | -0.6054 | 1.9493 | ±3.8986 | -0.311 | 0.7561 |  |
| Kidney disease | -2.1563 | 5.2482 | ±10.4964 | -0.411 | 0.6812 |  |
| Circulatory disease | -1.7942 | 2.5506 | ±5.1012 | -0.703 | 0.4818 |  |
| Avg. daily time < 70 (%) | -0.0127 | 4.3614 | ±8.7228 | -0.003 | 0.9977 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **346**, R² = **0.1251**, Adj R² = **0.0963**, F-statistic = **4.34** (p = **4.40e-06**), Residual SE = **16.059** on **334** df, AIC = **2914.9**, BIC = **2961.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +612.0238 | 1422.0578 | ±2844.1156 | +0.430 | 0.6669 |  |
| Education: graduate level (vs college) | -3.5366 | 1.8513 | ±3.7026 | -1.910 | 0.0561 | . |
| Education: high school or below (vs college) | +0.3911 | 3.3834 | ±6.7668 | +0.116 | 0.9080 |  |
| Site: UCSD (vs UAB) | -1.8048 | 2.3416 | ±4.6833 | -0.771 | 0.4408 |  |
| **Site: UW (vs UAB)** | **-4.3926** | 2.1333 | ±4.2666 | **-2.059** | **0.0395** | * |
| **Age (years)** | **-0.2937** | 0.0876 | ±0.1752 | **-3.352** | **8.02e-04** | *** |
| **BMI (kg/m2)** | **+0.4668** | 0.1584 | ±0.3168 | **+2.947** | **0.0032** | ** |
| Hypertension | -0.1173 | 2.1208 | ±4.2416 | -0.055 | 0.9559 |  |
| High cholesterol | -0.6011 | 1.9290 | ±3.8579 | -0.312 | 0.7553 |  |
| Kidney disease | -2.0934 | 5.2392 | ±10.4783 | -0.400 | 0.6895 |  |
| Circulatory disease | -1.8740 | 2.5694 | ±5.1388 | -0.729 | 0.4658 |  |
| Time 54-250, pooled (%) | -5.5607 | 14.2245 | ±28.4491 | -0.391 | 0.6959 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **346**, R² = **0.1250**, Adj R² = **0.0962**, F-statistic = **4.34** (p = **4.48e-06**), Residual SE = **16.060** on **334** df, AIC = **2914.9**, BIC = **2961.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +570.8282 | 1863.9847 | ±3727.9694 | +0.306 | 0.7594 |  |
| Education: graduate level (vs college) | -3.5558 | 1.8482 | ±3.6965 | -1.924 | 0.0544 | . |
| Education: high school or below (vs college) | +0.3434 | 3.3692 | ±6.7383 | +0.102 | 0.9188 |  |
| Site: UCSD (vs UAB) | -1.8570 | 2.3350 | ±4.6700 | -0.795 | 0.4264 |  |
| **Site: UW (vs UAB)** | **-4.4282** | 2.1329 | ±4.2659 | **-2.076** | **0.0379** | * |
| **Age (years)** | **-0.2943** | 0.0876 | ±0.1752 | **-3.360** | **7.80e-04** | *** |
| **BMI (kg/m2)** | **+0.4683** | 0.1584 | ±0.3168 | **+2.956** | **0.0031** | ** |
| Hypertension | -0.0826 | 2.1096 | ±4.2193 | -0.039 | 0.9688 |  |
| High cholesterol | -0.6009 | 1.9320 | ±3.8639 | -0.311 | 0.7558 |  |
| Kidney disease | -2.1268 | 5.2367 | ±10.4733 | -0.406 | 0.6846 |  |
| Circulatory disease | -1.8823 | 2.5846 | ±5.1692 | -0.728 | 0.4665 |  |
| Avg. daily time 54-250 (%) | -5.1480 | 18.6447 | ±37.2894 | -0.276 | 0.7825 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **346**, R² = **0.1318**, Adj R² = **0.1032**, F-statistic = **4.61** (p = **1.53e-06**), Residual SE = **15.997** on **334** df, AIC = **2912.2**, BIC = **2958.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.0040** | 9.1593 | ±18.3186 | **+5.896** | **3.72e-09** | *** |
| Education: graduate level (vs college) | -3.5191 | 1.8481 | ±3.6962 | -1.904 | 0.0569 | . |
| Education: high school or below (vs college) | +0.5574 | 3.3548 | ±6.7097 | +0.166 | 0.8680 |  |
| Site: UCSD (vs UAB) | -1.8692 | 2.3518 | ±4.7036 | -0.795 | 0.4267 |  |
| **Site: UW (vs UAB)** | **-4.4710** | 2.1224 | ±4.2447 | **-2.107** | **0.0352** | * |
| **Age (years)** | **-0.2888** | 0.0892 | ±0.1783 | **-3.239** | **0.0012** | ** |
| **BMI (kg/m2)** | **+0.4773** | 0.1755 | ±0.3510 | **+2.720** | **0.0065** | ** |
| Hypertension | -0.2995 | 2.0711 | ±4.1423 | -0.145 | 0.8850 |  |
| High cholesterol | -0.4689 | 1.9370 | ±3.8740 | -0.242 | 0.8087 |  |
| Kidney disease | -2.6668 | 5.3587 | ±10.7174 | -0.498 | 0.6187 |  |
| Circulatory disease | -1.8252 | 2.4788 | ±4.9575 | -0.736 | 0.4615 |  |
| Time 181-250, pooled (%) | +5.1023 | 3.3254 | ±6.6508 | +1.534 | 0.1249 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **346**, R² = **0.1393**, Adj R² = **0.1109**, F-statistic = **4.91** (p = **4.59e-07**), Residual SE = **15.928** on **334** df, AIC = **2909.2**, BIC = **2955.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.0476** | 8.6212 | ±17.2424 | **+6.153** | **7.60e-10** | *** |
| Education: graduate level (vs college) | -3.5100 | 1.8373 | ±3.6746 | -1.910 | 0.0561 | . |
| Education: high school or below (vs college) | +0.8307 | 3.3395 | ±6.6790 | +0.249 | 0.8036 |  |
| Site: UCSD (vs UAB) | -1.7369 | 2.3334 | ±4.6667 | -0.744 | 0.4566 |  |
| **Site: UW (vs UAB)** | **-4.4826** | 2.1066 | ±4.2132 | **-2.128** | **0.0333** | * |
| **Age (years)** | **-0.2777** | 0.0883 | ±0.1766 | **-3.145** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.4732** | 0.1634 | ±0.3267 | **+2.896** | **0.0038** | ** |
| Hypertension | -0.3729 | 2.0710 | ±4.1419 | -0.180 | 0.8571 |  |
| High cholesterol | -0.5797 | 1.9134 | ±3.8267 | -0.303 | 0.7619 |  |
| Kidney disease | -2.4955 | 5.3892 | ±10.7784 | -0.463 | 0.6433 |  |
| Circulatory disease | -1.8583 | 2.4900 | ±4.9800 | -0.746 | 0.4555 |  |
| **Avg. daily time 181-250 (%)** | **+7.2347** | 3.1483 | ±6.2965 | **+2.298** | **0.0216** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **346**, R² = **0.1317**, Adj R² = **0.1031**, F-statistic = **4.61** (p = **1.55e-06**), Residual SE = **15.998** on **334** df, AIC = **2912.2**, BIC = **2958.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.9970** | 9.1671 | ±18.3343 | **+5.890** | **3.86e-09** | *** |
| Education: graduate level (vs college) | -3.5147 | 1.8483 | ±3.6965 | -1.902 | 0.0572 | . |
| Education: high school or below (vs college) | +0.5594 | 3.3547 | ±6.7094 | +0.167 | 0.8676 |  |
| Site: UCSD (vs UAB) | -1.8690 | 2.3519 | ±4.7037 | -0.795 | 0.4268 |  |
| **Site: UW (vs UAB)** | **-4.4737** | 2.1223 | ±4.2446 | **-2.108** | **0.0350** | * |
| **Age (years)** | **-0.2887** | 0.0892 | ±0.1784 | **-3.237** | **0.0012** | ** |
| **BMI (kg/m2)** | **+0.4775** | 0.1756 | ±0.3511 | **+2.719** | **0.0065** | ** |
| Hypertension | -0.2965 | 2.0713 | ±4.1427 | -0.143 | 0.8862 |  |
| High cholesterol | -0.4750 | 1.9364 | ±3.8727 | -0.245 | 0.8062 |  |
| Kidney disease | -2.6632 | 5.3585 | ±10.7170 | -0.497 | 0.6192 |  |
| Circulatory disease | -1.8246 | 2.4793 | ±4.9587 | -0.736 | 0.4618 |  |
| Time > 180 (%) | +5.0724 | 3.3199 | ±6.6397 | +1.528 | 0.1265 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **346**, R² = **0.1391**, Adj R² = **0.1108**, F-statistic = **4.91** (p = **4.68e-07**), Residual SE = **15.930** on **334** df, AIC = **2909.3**, BIC = **2955.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.0340** | 8.6313 | ±17.2626 | **+6.144** | **8.03e-10** | *** |
| Education: graduate level (vs college) | -3.5029 | 1.8374 | ±3.6749 | -1.906 | 0.0566 | . |
| Education: high school or below (vs college) | +0.8333 | 3.3395 | ±6.6789 | +0.250 | 0.8030 |  |
| Site: UCSD (vs UAB) | -1.7373 | 2.3335 | ±4.6670 | -0.744 | 0.4566 |  |
| **Site: UW (vs UAB)** | **-4.4870** | 2.1068 | ±4.2135 | **-2.130** | **0.0332** | * |
| **Age (years)** | **-0.2775** | 0.0883 | ±0.1766 | **-3.142** | **0.0017** | ** |
| **BMI (kg/m2)** | **+0.4735** | 0.1635 | ±0.3271 | **+2.896** | **0.0038** | ** |
| Hypertension | -0.3686 | 2.0712 | ±4.1424 | -0.178 | 0.8587 |  |
| High cholesterol | -0.5881 | 1.9133 | ±3.8265 | -0.307 | 0.7586 |  |
| Kidney disease | -2.4927 | 5.3890 | ±10.7781 | -0.463 | 0.6437 |  |
| Circulatory disease | -1.8574 | 2.4906 | ±4.9811 | -0.746 | 0.4558 |  |
| **Avg. daily time > 180 (%)** | **+7.1950** | 3.1410 | ±6.2821 | **+2.291** | **0.0220** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 346)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **346**, R² = **0.1380**, Adj R² = **0.1096**, F-statistic = **4.86** (p = **5.60e-07**), Residual SE = **15.940** on **334** df, AIC = **2909.7**, BIC = **2955.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.1399** | 8.0033 | ±16.0066 | **+6.765** | **1.34e-11** | *** |
| Education: graduate level (vs college) | -3.2349 | 1.8208 | ±3.6416 | -1.777 | 0.0756 | . |
| Education: high school or below (vs college) | +0.2916 | 3.3576 | ±6.7151 | +0.087 | 0.9308 |  |
| Site: UCSD (vs UAB) | -1.7710 | 2.3043 | ±4.6086 | -0.769 | 0.4421 |  |
| **Site: UW (vs UAB)** | **-4.6148** | 2.1009 | ±4.2017 | **-2.197** | **0.0280** | * |
| **Age (years)** | **-0.2567** | 0.0873 | ±0.1745 | **-2.943** | **0.0033** | ** |
| **BMI (kg/m2)** | **+0.4396** | 0.1546 | ±0.3092 | **+2.843** | **0.0045** | ** |
| Hypertension | -0.3435 | 2.0753 | ±4.1506 | -0.165 | 0.8686 |  |
| High cholesterol | -0.8885 | 1.9052 | ±3.8104 | -0.466 | 0.6410 |  |
| Kidney disease | -2.6029 | 5.1433 | ±10.2865 | -0.506 | 0.6128 |  |
| Circulatory disease | -1.7326 | 2.5294 | ±5.0588 | -0.685 | 0.4933 |  |
| **Nocturnal time > 180 (%)** | **+5.6971** | 2.4600 | ±4.9199 | **+2.316** | **0.0206** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
