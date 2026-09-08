# Phase 6b model output tables - Near-normal substitute: >= 99% of readings within 70-180 - Healthy group (no diabetes + pre-diabetes / lifestyle) - Cognition

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


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


## Interpretation - Healthy group (no diabetes + pre-diabetes / lifestyle) - Cognition

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 84 single-predictor tests; 1 with raw p < 0.05 (about 4 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 393): best single predictor out of sample is **SD of daily means** (CV R² 0.029 vs 0.021 for covariates alone, gain +0.009; -0.264 per SD, p = 0.129). No glycaemic measure is associated with this outcome (all p > 0.05).
- **Cognitive impairment (MoCA < 26)** (n = 393): best single predictor out of sample is **MAG** (CV AUC 0.634 vs 0.630 for covariates alone, gain +0.004; OR 1.18 per SD, p = 0.147). No glycaemic measure is associated with this outcome (all p > 0.05).
- **MoCA memory index score (0-15)** (n = 393): best single predictor out of sample is **SD of daily means** (CV R² -0.039 vs -0.047 for covariates alone, gain +0.008; -0.285 per SD, p = 0.036). Raw p < 0.05 (FDR not applicable here): SD of daily means (p = 0.036).

**Most predictable outcomes (largest out-of-sample gain over covariates):** MoCA total score (0-30) (+0.009, via SD of daily means); MoCA memory index score (0-15) (+0.008, via SD of daily means); Cognitive impairment (MoCA < 26) (+0.004, via MAG). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (0 FDR-significant / 1 raw-significant of 24); HbA1c (0 FDR-significant / 0 raw-significant of 3); CGM level (0 FDR-significant / 0 raw-significant of 9).
Level metrics: 0 FDR-significant (0 raw); variability metrics: 0 FDR-significant (1 raw); HbA1c alone: 0 FDR-significant (0 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** MoCA total score (SD of daily means, ΔAIC -2.1); MoCA memory index score (SD of daily means, ΔAIC -4.9).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
