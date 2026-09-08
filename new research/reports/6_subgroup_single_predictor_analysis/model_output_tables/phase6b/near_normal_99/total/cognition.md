# Phase 6b model output tables - Near-normal substitute: >= 99% of readings within 70-180 - Total analysis base - Cognition

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 454; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **454**, R² = **0.1361**, Adj R² = **0.1166**, F-statistic = **6.98** (p = **3.42e-10**), Residual SE = **2.630** on **443** df, AIC = **2177.4**, BIC = **2222.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.4490** | 1.0197 | ±2.0393 | **+30.842** | **7.06e-209** | *** |
| **Education: graduate level (vs college)** | **+0.7983** | 0.2590 | ±0.5180 | **+3.082** | **0.0021** | ** |
| Education: high school or below (vs college) | -0.8492 | 0.5866 | ±1.1732 | -1.448 | 0.1477 |  |
| Site: UCSD (vs UAB) | -0.6530 | 0.3360 | ±0.6719 | -1.944 | 0.0519 | . |
| Site: UW (vs UAB) | -0.5189 | 0.3264 | ±0.6528 | -1.590 | 0.1119 |  |
| **Age (years)** | **-0.0552** | 0.0124 | ±0.0248 | **-4.458** | **8.26e-06** | *** |
| **BMI (kg/m2)** | **-0.0517** | 0.0176 | ±0.0352 | **-2.938** | **0.0033** | ** |
| Hypertension | -0.4137 | 0.2947 | ±0.5895 | -1.404 | 0.1604 |  |
| High cholesterol | -0.2030 | 0.2723 | ±0.5446 | -0.745 | 0.4561 |  |
| Kidney disease | +0.5433 | 0.5353 | ±1.0706 | +1.015 | 0.3101 |  |
| Circulatory disease | -0.6676 | 0.4739 | ±0.9479 | -1.409 | 0.1590 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **454**, R² = **0.1379**, Adj R² = **0.1165**, F-statistic = **6.43** (p = **6.27e-10**), Residual SE = **2.630** on **442** df, AIC = **2178.4**, BIC = **2227.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.5214** | 2.4356 | ±4.8713 | **+13.763** | **4.27e-43** | *** |
| **Education: graduate level (vs college)** | **+0.7903** | 0.2604 | ±0.5207 | **+3.035** | **0.0024** | ** |
| Education: high school or below (vs college) | -0.8189 | 0.5847 | ±1.1695 | -1.400 | 0.1614 |  |
| **Site: UCSD (vs UAB)** | **-0.6586** | 0.3348 | ±0.6697 | **-1.967** | **0.0492** | * |
| Site: UW (vs UAB) | -0.5301 | 0.3245 | ±0.6491 | -1.633 | 0.1024 |  |
| **Age (years)** | **-0.0542** | 0.0125 | ±0.0249 | **-4.348** | **1.37e-05** | *** |
| **BMI (kg/m2)** | **-0.0496** | 0.0173 | ±0.0347 | **-2.860** | **0.0042** | ** |
| Hypertension | -0.3884 | 0.2947 | ±0.5894 | -1.318 | 0.1875 |  |
| High cholesterol | -0.1550 | 0.2742 | ±0.5484 | -0.565 | 0.5719 |  |
| Kidney disease | +0.5158 | 0.5303 | ±1.0605 | +0.973 | 0.3307 |  |
| Circulatory disease | -0.6741 | 0.4740 | ±0.9479 | -1.422 | 0.1550 |  |
| HbA1c (%) | -0.3988 | 0.4320 | ±0.8641 | -0.923 | 0.3560 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **454**, R² = **0.1423**, Adj R² = **0.1209**, F-statistic = **6.67** (p = **2.33e-10**), Residual SE = **2.624** on **442** df, AIC = **2176.1**, BIC = **2225.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+34.7789** | 2.1973 | ±4.3945 | **+15.828** | **1.99e-56** | *** |
| **Education: graduate level (vs college)** | **+0.8035** | 0.2589 | ±0.5179 | **+3.103** | **0.0019** | ** |
| Education: high school or below (vs college) | -0.8746 | 0.5817 | ±1.1633 | -1.504 | 0.1327 |  |
| Site: UCSD (vs UAB) | -0.6263 | 0.3389 | ±0.6777 | -1.848 | 0.0646 | . |
| Site: UW (vs UAB) | -0.4859 | 0.3278 | ±0.6555 | -1.482 | 0.1382 |  |
| **Age (years)** | **-0.0558** | 0.0123 | ±0.0246 | **-4.524** | **6.08e-06** | *** |
| **BMI (kg/m2)** | **-0.0497** | 0.0174 | ±0.0348 | **-2.855** | **0.0043** | ** |
| Hypertension | -0.3849 | 0.2955 | ±0.5909 | -1.303 | 0.1927 |  |
| High cholesterol | -0.2238 | 0.2739 | ±0.5478 | -0.817 | 0.4138 |  |
| Kidney disease | +0.5731 | 0.5250 | ±1.0501 | +1.092 | 0.2750 |  |
| Circulatory disease | -0.6485 | 0.4711 | ±0.9422 | -1.377 | 0.1686 |  |
| Mean glucose (mg/dL) | -0.0296 | 0.0172 | ±0.0345 | -1.716 | 0.0862 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **454**, R² = **0.1423**, Adj R² = **0.1209**, F-statistic = **6.67** (p = **2.33e-10**), Residual SE = **2.624** on **442** df, AIC = **2176.1**, BIC = **2225.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+38.8701** | 4.4528 | ±8.9055 | **+8.729** | **2.56e-18** | *** |
| **Education: graduate level (vs college)** | **+0.8035** | 0.2589 | ±0.5179 | **+3.103** | **0.0019** | ** |
| Education: high school or below (vs college) | -0.8746 | 0.5817 | ±1.1633 | -1.504 | 0.1327 |  |
| Site: UCSD (vs UAB) | -0.6263 | 0.3389 | ±0.6777 | -1.848 | 0.0646 | . |
| Site: UW (vs UAB) | -0.4859 | 0.3278 | ±0.6555 | -1.482 | 0.1382 |  |
| **Age (years)** | **-0.0558** | 0.0123 | ±0.0246 | **-4.524** | **6.08e-06** | *** |
| **BMI (kg/m2)** | **-0.0497** | 0.0174 | ±0.0348 | **-2.855** | **0.0043** | ** |
| Hypertension | -0.3849 | 0.2955 | ±0.5909 | -1.303 | 0.1927 |  |
| High cholesterol | -0.2238 | 0.2739 | ±0.5478 | -0.817 | 0.4138 |  |
| Kidney disease | +0.5731 | 0.5250 | ±1.0501 | +1.092 | 0.2750 |  |
| Circulatory disease | -0.6485 | 0.4711 | ±0.9422 | -1.377 | 0.1686 |  |
| GMI (%) | -1.2360 | 0.7203 | ±1.4406 | -1.716 | 0.0862 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **454**, R² = **0.1378**, Adj R² = **0.1164**, F-statistic = **6.42** (p = **6.39e-10**), Residual SE = **2.631** on **442** df, AIC = **2178.5**, BIC = **2227.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.8692** | 1.8654 | ±3.7307 | **+17.621** | **1.70e-69** | *** |
| **Education: graduate level (vs college)** | **+0.7921** | 0.2601 | ±0.5201 | **+3.046** | **0.0023** | ** |
| Education: high school or below (vs college) | -0.8660 | 0.5884 | ±1.1767 | -1.472 | 0.1411 |  |
| Site: UCSD (vs UAB) | -0.6265 | 0.3426 | ±0.6852 | -1.829 | 0.0675 | . |
| Site: UW (vs UAB) | -0.4944 | 0.3303 | ±0.6607 | -1.497 | 0.1345 |  |
| **Age (years)** | **-0.0568** | 0.0125 | ±0.0250 | **-4.546** | **5.46e-06** | *** |
| **BMI (kg/m2)** | **-0.0490** | 0.0176 | ±0.0353 | **-2.780** | **0.0054** | ** |
| Hypertension | -0.3987 | 0.2950 | ±0.5899 | -1.352 | 0.1764 |  |
| High cholesterol | -0.2069 | 0.2734 | ±0.5467 | -0.757 | 0.4491 |  |
| Kidney disease | +0.5350 | 0.5322 | ±1.0643 | +1.005 | 0.3147 |  |
| Circulatory disease | -0.6637 | 0.4736 | ±0.9471 | -1.402 | 0.1611 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0123 | 0.0137 | ±0.0275 | -0.898 | 0.3690 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **454**, R² = **0.1361**, Adj R² = **0.1146**, F-statistic = **6.33** (p = **9.40e-10**), Residual SE = **2.633** on **442** df, AIC = **2179.4**, BIC = **2228.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.4817** | 1.2999 | ±2.5997 | **+24.219** | **1.39e-129** | *** |
| **Education: graduate level (vs college)** | **+0.7976** | 0.2587 | ±0.5174 | **+3.083** | **0.0020** | ** |
| Education: high school or below (vs college) | -0.8490 | 0.5877 | ±1.1754 | -1.445 | 0.1486 |  |
| Site: UCSD (vs UAB) | -0.6536 | 0.3336 | ±0.6672 | -1.959 | 0.0501 | . |
| Site: UW (vs UAB) | -0.5196 | 0.3254 | ±0.6508 | -1.597 | 0.1103 |  |
| **Age (years)** | **-0.0552** | 0.0124 | ±0.0248 | **-4.443** | **8.88e-06** | *** |
| **BMI (kg/m2)** | **-0.0516** | 0.0178 | ±0.0355 | **-2.905** | **0.0037** | ** |
| Hypertension | -0.4131 | 0.2949 | ±0.5897 | -1.401 | 0.1613 |  |
| High cholesterol | -0.2036 | 0.2755 | ±0.5510 | -0.739 | 0.4599 |  |
| Kidney disease | +0.5453 | 0.5386 | ±1.0773 | +1.012 | 0.3114 |  |
| Circulatory disease | -0.6670 | 0.4749 | ±0.9497 | -1.405 | 0.1601 |  |
| Glucose SD, pooled (mg/dL) | -0.0020 | 0.0582 | ±0.1164 | -0.034 | 0.9727 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **454**, R² = **0.1376**, Adj R² = **0.1162**, F-statistic = **6.41** (p = **6.69e-10**), Residual SE = **2.631** on **442** df, AIC = **2178.6**, BIC = **2228.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.7721** | 1.2492 | ±2.4983 | **+24.634** | **5.47e-134** | *** |
| **Education: graduate level (vs college)** | **+0.8153** | 0.2599 | ±0.5199 | **+3.137** | **0.0017** | ** |
| Education: high school or below (vs college) | -0.8470 | 0.5903 | ±1.1805 | -1.435 | 0.1513 |  |
| Site: UCSD (vs UAB) | -0.6419 | 0.3345 | ±0.6689 | -1.919 | 0.0549 | . |
| Site: UW (vs UAB) | -0.5054 | 0.3264 | ±0.6528 | -1.548 | 0.1215 |  |
| **Age (years)** | **-0.0555** | 0.0124 | ±0.0248 | **-4.472** | **7.74e-06** | *** |
| **BMI (kg/m2)** | **-0.0528** | 0.0180 | ±0.0360 | **-2.935** | **0.0033** | ** |
| Hypertension | -0.4235 | 0.2960 | ±0.5921 | -1.430 | 0.1526 |  |
| High cholesterol | -0.1898 | 0.2739 | ±0.5478 | -0.693 | 0.4884 |  |
| Kidney disease | +0.4987 | 0.5359 | ±1.0718 | +0.931 | 0.3521 |  |
| Circulatory disease | -0.6720 | 0.4786 | ±0.9571 | -1.404 | 0.1603 |  |
| Avg. daily SD (mg/dL) | +0.0463 | 0.0558 | ±0.1115 | +0.831 | 0.4059 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **454**, R² = **0.1371**, Adj R² = **0.1156**, F-statistic = **6.38** (p = **7.52e-10**), Residual SE = **2.632** on **442** df, AIC = **2178.8**, BIC = **2228.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.8350** | 1.2648 | ±2.5296 | **+24.379** | **2.84e-131** | *** |
| **Education: graduate level (vs college)** | **+0.8117** | 0.2580 | ±0.5160 | **+3.146** | **0.0017** | ** |
| Education: high school or below (vs college) | -0.8568 | 0.5892 | ±1.1785 | -1.454 | 0.1459 |  |
| Site: UCSD (vs UAB) | -0.6375 | 0.3335 | ±0.6670 | -1.912 | 0.0559 | . |
| Site: UW (vs UAB) | -0.5006 | 0.3263 | ±0.6526 | -1.534 | 0.1250 |  |
| **Age (years)** | **-0.0554** | 0.0124 | ±0.0248 | **-4.460** | **8.18e-06** | *** |
| **BMI (kg/m2)** | **-0.0518** | 0.0176 | ±0.0353 | **-2.939** | **0.0033** | ** |
| Hypertension | -0.4205 | 0.2952 | ±0.5904 | -1.425 | 0.1543 |  |
| High cholesterol | -0.1947 | 0.2740 | ±0.5481 | -0.711 | 0.4774 |  |
| Kidney disease | +0.5126 | 0.5334 | ±1.0668 | +0.961 | 0.3366 |  |
| Circulatory disease | -0.6744 | 0.4778 | ±0.9555 | -1.412 | 0.1581 |  |
| CV (%) | +0.0418 | 0.0608 | ±0.1216 | +0.688 | 0.4917 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **454**, R² = **0.1376**, Adj R² = **0.1161**, F-statistic = **6.41** (p = **6.75e-10**), Residual SE = **2.631** on **442** df, AIC = **2178.6**, BIC = **2228.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.1621** | 1.4001 | ±2.8002 | **+22.971** | **9.02e-117** | *** |
| **Education: graduate level (vs college)** | **+0.8169** | 0.2577 | ±0.5155 | **+3.170** | **0.0015** | ** |
| Education: high school or below (vs college) | -0.8600 | 0.5896 | ±1.1793 | -1.458 | 0.1447 |  |
| Site: UCSD (vs UAB) | -0.6388 | 0.3343 | ±0.6686 | -1.911 | 0.0560 | . |
| Site: UW (vs UAB) | -0.5009 | 0.3266 | ±0.6532 | -1.534 | 0.1251 |  |
| **Age (years)** | **-0.0554** | 0.0124 | ±0.0248 | **-4.463** | **8.07e-06** | *** |
| **BMI (kg/m2)** | **-0.0518** | 0.0176 | ±0.0352 | **-2.943** | **0.0033** | ** |
| Hypertension | -0.4227 | 0.2951 | ±0.5903 | -1.432 | 0.1521 |  |
| High cholesterol | -0.1915 | 0.2739 | ±0.5477 | -0.699 | 0.4843 |  |
| Kidney disease | +0.5152 | 0.5335 | ±1.0671 | +0.966 | 0.3342 |  |
| Circulatory disease | -0.6724 | 0.4782 | ±0.9563 | -1.406 | 0.1596 |  |
| Mean / SD ratio | -0.1033 | 0.1219 | ±0.2438 | -0.847 | 0.3967 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **454**, R² = **0.1396**, Adj R² = **0.1182**, F-statistic = **6.52** (p = **4.28e-10**), Residual SE = **2.628** on **442** df, AIC = **2177.5**, BIC = **2226.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.4509** | 1.3453 | ±2.6906 | **+24.122** | **1.49e-128** | *** |
| **Education: graduate level (vs college)** | **+0.8278** | 0.2593 | ±0.5186 | **+3.193** | **0.0014** | ** |
| Education: high school or below (vs college) | -0.8582 | 0.5891 | ±1.1781 | -1.457 | 0.1451 |  |
| Site: UCSD (vs UAB) | -0.6357 | 0.3352 | ±0.6705 | -1.896 | 0.0579 | . |
| Site: UW (vs UAB) | -0.4951 | 0.3263 | ±0.6526 | -1.517 | 0.1292 |  |
| **Age (years)** | **-0.0557** | 0.0124 | ±0.0247 | **-4.506** | **6.62e-06** | *** |
| **BMI (kg/m2)** | **-0.0528** | 0.0178 | ±0.0356 | **-2.961** | **0.0031** | ** |
| Hypertension | -0.4184 | 0.2957 | ±0.5914 | -1.415 | 0.1571 |  |
| High cholesterol | -0.1903 | 0.2731 | ±0.5461 | -0.697 | 0.4859 |  |
| Kidney disease | +0.4997 | 0.5309 | ±1.0619 | +0.941 | 0.3467 |  |
| Circulatory disease | -0.6589 | 0.4801 | ±0.9601 | -1.372 | 0.1699 |  |
| Avg. daily mean/SD | -0.1229 | 0.0967 | ±0.1933 | -1.271 | 0.2036 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **454**, R² = **0.1365**, Adj R² = **0.1150**, F-statistic = **6.35** (p = **8.61e-10**), Residual SE = **2.633** on **442** df, AIC = **2179.2**, BIC = **2228.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.8215** | 1.3140 | ±2.6279 | **+24.218** | **1.45e-129** | *** |
| **Education: graduate level (vs college)** | **+0.7984** | 0.2595 | ±0.5191 | **+3.077** | **0.0021** | ** |
| Education: high school or below (vs college) | -0.8339 | 0.5825 | ±1.1650 | -1.432 | 0.1522 |  |
| Site: UCSD (vs UAB) | -0.6568 | 0.3364 | ±0.6728 | -1.953 | 0.0509 | . |
| Site: UW (vs UAB) | -0.5321 | 0.3284 | ±0.6569 | -1.620 | 0.1052 |  |
| **Age (years)** | **-0.0557** | 0.0125 | ±0.0251 | **-4.442** | **8.93e-06** | *** |
| **BMI (kg/m2)** | **-0.0521** | 0.0175 | ±0.0351 | **-2.970** | **0.0030** | ** |
| Hypertension | -0.4176 | 0.2947 | ±0.5893 | -1.417 | 0.1564 |  |
| High cholesterol | -0.1992 | 0.2733 | ±0.5467 | -0.729 | 0.4661 |  |
| Kidney disease | +0.5547 | 0.5375 | ±1.0750 | +1.032 | 0.3021 |  |
| Circulatory disease | -0.6734 | 0.4744 | ±0.9489 | -1.419 | 0.1558 |  |
| MAG (mg/dL/h) | -0.0097 | 0.0208 | ±0.0416 | -0.465 | 0.6423 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **454**, R² = **0.1376**, Adj R² = **0.1161**, F-statistic = **6.41** (p = **6.78e-10**), Residual SE = **2.631** on **442** df, AIC = **2178.6**, BIC = **2228.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.6489** | 1.3515 | ±2.7030 | **+22.677** | **7.48e-114** | *** |
| **Education: graduate level (vs college)** | **+0.8084** | 0.2594 | ±0.5188 | **+3.116** | **0.0018** | ** |
| Education: high school or below (vs college) | -0.8507 | 0.5915 | ±1.1830 | -1.438 | 0.1503 |  |
| Site: UCSD (vs UAB) | -0.6420 | 0.3351 | ±0.6701 | -1.916 | 0.0554 | . |
| Site: UW (vs UAB) | -0.5046 | 0.3280 | ±0.6561 | -1.538 | 0.1240 |  |
| **Age (years)** | **-0.0554** | 0.0124 | ±0.0248 | **-4.475** | **7.63e-06** | *** |
| **BMI (kg/m2)** | **-0.0505** | 0.0173 | ±0.0347 | **-2.914** | **0.0036** | ** |
| Hypertension | -0.4075 | 0.2947 | ±0.5894 | -1.383 | 0.1668 |  |
| High cholesterol | -0.2020 | 0.2727 | ±0.5454 | -0.741 | 0.4590 |  |
| Kidney disease | +0.5181 | 0.5347 | ±1.0693 | +0.969 | 0.3325 |  |
| Circulatory disease | -0.6681 | 0.4757 | ±0.9514 | -1.405 | 0.1602 |  |
| Avg. daily range (mg/dL) | +0.0096 | 0.0115 | ±0.0231 | +0.833 | 0.4049 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **454**, R² = **0.1470**, Adj R² = **0.1257**, F-statistic = **6.92** (p = **8.04e-11**), Residual SE = **2.617** on **442** df, AIC = **2173.6**, BIC = **2223.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+32.2414** | 1.0391 | ±2.0783 | **+31.027** | **2.30e-211** | *** |
| **Education: graduate level (vs college)** | **+0.8156** | 0.2602 | ±0.5204 | **+3.135** | **0.0017** | ** |
| Education: high school or below (vs college) | -0.7779 | 0.5772 | ±1.1544 | -1.348 | 0.1777 |  |
| **Site: UCSD (vs UAB)** | **-0.6833** | 0.3315 | ±0.6631 | **-2.061** | **0.0393** | * |
| Site: UW (vs UAB) | -0.5072 | 0.3242 | ±0.6484 | -1.564 | 0.1177 |  |
| **Age (years)** | **-0.0558** | 0.0122 | ±0.0244 | **-4.581** | **4.63e-06** | *** |
| **BMI (kg/m2)** | **-0.0512** | 0.0175 | ±0.0350 | **-2.921** | **0.0035** | ** |
| Hypertension | -0.3603 | 0.2923 | ±0.5847 | -1.233 | 0.2178 |  |
| High cholesterol | -0.1777 | 0.2694 | ±0.5389 | -0.660 | 0.5096 |  |
| Kidney disease | +0.5459 | 0.5204 | ±1.0407 | +1.049 | 0.2942 |  |
| Circulatory disease | -0.5966 | 0.4647 | ±0.9294 | -1.284 | 0.1992 |  |
| SD of daily means (mg/dL) | -0.1585 | 0.0814 | ±0.1629 | -1.946 | 0.0517 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **454**, R² = **0.1364**, Adj R² = **0.1149**, F-statistic = **6.35** (p = **8.84e-10**), Residual SE = **2.633** on **442** df, AIC = **2179.2**, BIC = **2228.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +15.8967 | 41.5639 | ±83.1278 | +0.382 | 0.7021 |  |
| **Education: graduate level (vs college)** | **+0.7945** | 0.2595 | ±0.5191 | **+3.061** | **0.0022** | ** |
| Education: high school or below (vs college) | -0.8525 | 0.5870 | ±1.1741 | -1.452 | 0.1464 |  |
| **Site: UCSD (vs UAB)** | **-0.6586** | 0.3354 | ±0.6709 | **-1.964** | **0.0496** | * |
| Site: UW (vs UAB) | -0.5239 | 0.3271 | ±0.6542 | -1.602 | 0.1092 |  |
| **Age (years)** | **-0.0553** | 0.0124 | ±0.0249 | **-4.451** | **8.53e-06** | *** |
| **BMI (kg/m2)** | **-0.0520** | 0.0176 | ±0.0353 | **-2.947** | **0.0032** | ** |
| Hypertension | -0.4116 | 0.2950 | ±0.5899 | -1.395 | 0.1629 |  |
| High cholesterol | -0.1999 | 0.2724 | ±0.5448 | -0.734 | 0.4630 |  |
| Kidney disease | +0.5557 | 0.5344 | ±1.0688 | +1.040 | 0.2984 |  |
| Circulatory disease | -0.6698 | 0.4754 | ±0.9509 | -1.409 | 0.1589 |  |
| Time in range 70-180, pooled (%) | +0.1564 | 0.4175 | ±0.8349 | +0.375 | 0.7079 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **454**, R² = **0.1367**, Adj R² = **0.1153**, F-statistic = **6.36** (p = **8.16e-10**), Residual SE = **2.632** on **442** df, AIC = **2179.0**, BIC = **2228.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +54.2156 | 43.0316 | ±86.0631 | +1.260 | 0.2077 |  |
| **Education: graduate level (vs college)** | **+0.8052** | 0.2594 | ±0.5188 | **+3.104** | **0.0019** | ** |
| Education: high school or below (vs college) | -0.8425 | 0.5904 | ±1.1807 | -1.427 | 0.1536 |  |
| Site: UCSD (vs UAB) | -0.6512 | 0.3363 | ±0.6725 | -1.937 | 0.0528 | . |
| Site: UW (vs UAB) | -0.5193 | 0.3281 | ±0.6562 | -1.583 | 0.1135 |  |
| **Age (years)** | **-0.0550** | 0.0124 | ±0.0249 | **-4.421** | **9.84e-06** | *** |
| **BMI (kg/m2)** | **-0.0515** | 0.0175 | ±0.0351 | **-2.933** | **0.0034** | ** |
| Hypertension | -0.4088 | 0.2958 | ±0.5915 | -1.382 | 0.1669 |  |
| High cholesterol | -0.2107 | 0.2724 | ±0.5449 | -0.773 | 0.4394 |  |
| Kidney disease | +0.5350 | 0.5408 | ±1.0817 | +0.989 | 0.3225 |  |
| Circulatory disease | -0.6705 | 0.4753 | ±0.9507 | -1.411 | 0.1584 |  |
| Avg. daily time in range 70-180 (%) | -0.2288 | 0.4316 | ±0.8631 | -0.530 | 0.5961 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **454**, R² = **0.1395**, Adj R² = **0.1180**, F-statistic = **6.51** (p = **4.42e-10**), Residual SE = **2.628** on **442** df, AIC = **2177.6**, BIC = **2227.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.3245** | 1.0266 | ±2.0531 | **+30.514** | **1.71e-204** | *** |
| **Education: graduate level (vs college)** | **+0.8043** | 0.2593 | ±0.5185 | **+3.102** | **0.0019** | ** |
| Education: high school or below (vs college) | -0.8234 | 0.5835 | ±1.1671 | -1.411 | 0.1582 |  |
| Site: UCSD (vs UAB) | -0.5817 | 0.3477 | ±0.6953 | -1.673 | 0.0943 | . |
| Site: UW (vs UAB) | -0.4772 | 0.3359 | ±0.6719 | -1.420 | 0.1555 |  |
| **Age (years)** | **-0.0549** | 0.0123 | ±0.0247 | **-4.452** | **8.49e-06** | *** |
| **BMI (kg/m2)** | **-0.0518** | 0.0176 | ±0.0353 | **-2.937** | **0.0033** | ** |
| Hypertension | -0.4375 | 0.2940 | ±0.5880 | -1.488 | 0.1368 |  |
| High cholesterol | -0.2045 | 0.2722 | ±0.5444 | -0.751 | 0.4524 |  |
| Kidney disease | +0.5931 | 0.5373 | ±1.0745 | +1.104 | 0.2696 |  |
| Circulatory disease | -0.6805 | 0.4744 | ±0.9488 | -1.435 | 0.1514 |  |
| Any reading < 54 during wear (0/1) | +0.4445 | 0.3254 | ±0.6509 | +1.366 | 0.1720 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **454**, R² = **0.1368**, Adj R² = **0.1154**, F-statistic = **6.37** (p = **7.96e-10**), Residual SE = **2.632** on **442** df, AIC = **2179.0**, BIC = **2228.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.4058** | 1.0279 | ±2.0557 | **+30.555** | **4.87e-205** | *** |
| **Education: graduate level (vs college)** | **+0.8001** | 0.2600 | ±0.5200 | **+3.077** | **0.0021** | ** |
| Education: high school or below (vs college) | -0.8287 | 0.5874 | ±1.1748 | -1.411 | 0.1583 |  |
| Site: UCSD (vs UAB) | -0.6265 | 0.3456 | ±0.6911 | -1.813 | 0.0698 | . |
| Site: UW (vs UAB) | -0.5060 | 0.3326 | ±0.6653 | -1.521 | 0.1282 |  |
| **Age (years)** | **-0.0547** | 0.0124 | ±0.0248 | **-4.408** | **1.04e-05** | *** |
| **BMI (kg/m2)** | **-0.0525** | 0.0177 | ±0.0354 | **-2.965** | **0.0030** | ** |
| Hypertension | -0.4294 | 0.2946 | ±0.5891 | -1.458 | 0.1450 |  |
| High cholesterol | -0.1980 | 0.2722 | ±0.5445 | -0.727 | 0.4670 |  |
| Kidney disease | +0.5603 | 0.5358 | ±1.0716 | +1.046 | 0.2956 |  |
| Circulatory disease | -0.6793 | 0.4746 | ±0.9491 | -1.431 | 0.1523 |  |
| Time < 54 (%) | +1.4719 | 2.5156 | ±5.0313 | +0.585 | 0.5585 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **454**, R² = **0.1377**, Adj R² = **0.1162**, F-statistic = **6.42** (p = **6.59e-10**), Residual SE = **2.631** on **442** df, AIC = **2178.5**, BIC = **2228.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.4234** | 1.0224 | ±2.0448 | **+30.735** | **1.92e-207** | *** |
| **Education: graduate level (vs college)** | **+0.8003** | 0.2597 | ±0.5194 | **+3.082** | **0.0021** | ** |
| Education: high school or below (vs college) | -0.8341 | 0.5849 | ±1.1698 | -1.426 | 0.1538 |  |
| Site: UCSD (vs UAB) | -0.6365 | 0.3385 | ±0.6769 | -1.881 | 0.0600 | . |
| Site: UW (vs UAB) | -0.5162 | 0.3280 | ±0.6561 | -1.574 | 0.1156 |  |
| **Age (years)** | **-0.0550** | 0.0124 | ±0.0248 | **-4.435** | **9.22e-06** | *** |
| **BMI (kg/m2)** | **-0.0522** | 0.0177 | ±0.0354 | **-2.950** | **0.0032** | ** |
| Hypertension | -0.4206 | 0.2950 | ±0.5901 | -1.425 | 0.1540 |  |
| High cholesterol | -0.2031 | 0.2729 | ±0.5458 | -0.744 | 0.4567 |  |
| Kidney disease | +0.5618 | 0.5349 | ±1.0698 | +1.050 | 0.2936 |  |
| Circulatory disease | -0.6952 | 0.4739 | ±0.9479 | -1.467 | 0.1424 |  |
| Avg. daily time < 54 (%) | +2.7971 | 3.1799 | ±6.3598 | +0.880 | 0.3791 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **454**, R² = **0.1386**, Adj R² = **0.1172**, F-statistic = **6.47** (p = **5.34e-10**), Residual SE = **2.629** on **442** df, AIC = **2178.0**, BIC = **2227.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.3175** | 1.0373 | ±2.0747 | **+30.190** | **3.16e-200** | *** |
| **Education: graduate level (vs college)** | **+0.8107** | 0.2598 | ±0.5196 | **+3.120** | **0.0018** | ** |
| Education: high school or below (vs college) | -0.8792 | 0.5866 | ±1.1733 | -1.499 | 0.1340 |  |
| Site: UCSD (vs UAB) | -0.6343 | 0.3376 | ±0.6751 | -1.879 | 0.0603 | . |
| Site: UW (vs UAB) | -0.4924 | 0.3297 | ±0.6593 | -1.494 | 0.1353 |  |
| **Age (years)** | **-0.0551** | 0.0124 | ±0.0249 | **-4.434** | **9.23e-06** | *** |
| **BMI (kg/m2)** | **-0.0515** | 0.0177 | ±0.0353 | **-2.916** | **0.0035** | ** |
| Hypertension | -0.3945 | 0.2965 | ±0.5930 | -1.330 | 0.1834 |  |
| High cholesterol | -0.2325 | 0.2755 | ±0.5509 | -0.844 | 0.3986 |  |
| Kidney disease | +0.5811 | 0.5406 | ±1.0811 | +1.075 | 0.2824 |  |
| Circulatory disease | -0.6575 | 0.4742 | ±0.9484 | -1.387 | 0.1656 |  |
| Time 54-69, pooled (%) | +0.7826 | 0.6764 | ±1.3529 | +1.157 | 0.2473 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **454**, R² = **0.1406**, Adj R² = **0.1192**, F-statistic = **6.57** (p = **3.43e-10**), Residual SE = **2.626** on **442** df, AIC = **2177.0**, BIC = **2226.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.3163** | 1.0298 | ±2.0596 | **+30.410** | **4.06e-203** | *** |
| **Education: graduate level (vs college)** | **+0.8246** | 0.2599 | ±0.5198 | **+3.173** | **0.0015** | ** |
| Education: high school or below (vs college) | -0.8881 | 0.5839 | ±1.1677 | -1.521 | 0.1282 |  |
| Site: UCSD (vs UAB) | -0.6443 | 0.3365 | ±0.6730 | -1.915 | 0.0555 | . |
| Site: UW (vs UAB) | -0.5021 | 0.3287 | ±0.6574 | -1.528 | 0.1266 |  |
| **Age (years)** | **-0.0555** | 0.0124 | ±0.0248 | **-4.475** | **7.64e-06** | *** |
| **BMI (kg/m2)** | **-0.0516** | 0.0176 | ±0.0353 | **-2.923** | **0.0035** | ** |
| Hypertension | -0.3633 | 0.2971 | ±0.5943 | -1.223 | 0.2214 |  |
| High cholesterol | -0.2375 | 0.2738 | ±0.5476 | -0.867 | 0.3857 |  |
| Kidney disease | +0.5895 | 0.5430 | ±1.0859 | +1.086 | 0.2776 |  |
| Circulatory disease | -0.6717 | 0.4736 | ±0.9473 | -1.418 | 0.1561 |  |
| Avg. daily time 54-69 (%) | +1.0638 | 0.6583 | ±1.3165 | +1.616 | 0.1061 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **454**, R² = **0.1388**, Adj R² = **0.1173**, F-statistic = **6.47** (p = **5.16e-10**), Residual SE = **2.629** on **442** df, AIC = **2178.0**, BIC = **2227.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.3076** | 1.0390 | ±2.0780 | **+30.133** | **1.81e-199** | *** |
| **Education: graduate level (vs college)** | **+0.8105** | 0.2601 | ±0.5202 | **+3.116** | **0.0018** | ** |
| Education: high school or below (vs college) | -0.8667 | 0.5854 | ±1.1707 | -1.481 | 0.1387 |  |
| Site: UCSD (vs UAB) | -0.6230 | 0.3391 | ±0.6782 | -1.837 | 0.0662 | . |
| Site: UW (vs UAB) | -0.4884 | 0.3313 | ±0.6627 | -1.474 | 0.1405 |  |
| **Age (years)** | **-0.0549** | 0.0124 | ±0.0249 | **-4.413** | **1.02e-05** | *** |
| **BMI (kg/m2)** | **-0.0520** | 0.0177 | ±0.0354 | **-2.935** | **0.0033** | ** |
| Hypertension | -0.4037 | 0.2964 | ±0.5928 | -1.362 | 0.1731 |  |
| High cholesterol | -0.2276 | 0.2749 | ±0.5499 | -0.828 | 0.4078 |  |
| Kidney disease | +0.5862 | 0.5403 | ±1.0807 | +1.085 | 0.2780 |  |
| Circulatory disease | -0.6640 | 0.4739 | ±0.9479 | -1.401 | 0.1612 |  |
| Time < 70 (%) | +0.7164 | 0.6024 | ±1.2047 | +1.189 | 0.2343 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **454**, R² = **0.1409**, Adj R² = **0.1195**, F-statistic = **6.59** (p = **3.20e-10**), Residual SE = **2.626** on **442** df, AIC = **2176.8**, BIC = **2226.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.3149** | 1.0299 | ±2.0598 | **+30.406** | **4.52e-203** | *** |
| **Education: graduate level (vs college)** | **+0.8238** | 0.2599 | ±0.5198 | **+3.169** | **0.0015** | ** |
| Education: high school or below (vs college) | -0.8804 | 0.5826 | ±1.1651 | -1.511 | 0.1307 |  |
| Site: UCSD (vs UAB) | -0.6389 | 0.3366 | ±0.6732 | -1.898 | 0.0577 | . |
| Site: UW (vs UAB) | -0.5021 | 0.3290 | ±0.6580 | -1.526 | 0.1269 |  |
| **Age (years)** | **-0.0554** | 0.0124 | ±0.0248 | **-4.469** | **7.85e-06** | *** |
| **BMI (kg/m2)** | **-0.0518** | 0.0177 | ±0.0354 | **-2.930** | **0.0034** | ** |
| Hypertension | -0.3687 | 0.2965 | ±0.5930 | -1.244 | 0.2137 |  |
| High cholesterol | -0.2356 | 0.2735 | ±0.5471 | -0.861 | 0.3892 |  |
| Kidney disease | +0.5934 | 0.5424 | ±1.0848 | +1.094 | 0.2739 |  |
| Circulatory disease | -0.6814 | 0.4734 | ±0.9467 | -1.439 | 0.1500 |  |
| Avg. daily time < 70 (%) | +1.0018 | 0.5973 | ±1.1947 | +1.677 | 0.0935 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **454**, R² = **0.1366**, Adj R² = **0.1151**, F-statistic = **6.36** (p = **8.39e-10**), Residual SE = **2.632** on **442** df, AIC = **2179.1**, BIC = **2228.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +150.1387 | 248.8431 | ±497.6863 | +0.603 | 0.5463 |  |
| **Education: graduate level (vs college)** | **+0.7996** | 0.2600 | ±0.5201 | **+3.075** | **0.0021** | ** |
| Education: high school or below (vs college) | -0.8321 | 0.5876 | ±1.1752 | -1.416 | 0.1567 |  |
| Site: UCSD (vs UAB) | -0.6301 | 0.3460 | ±0.6921 | -1.821 | 0.0686 | . |
| Site: UW (vs UAB) | -0.5074 | 0.3329 | ±0.6659 | -1.524 | 0.1275 |  |
| **Age (years)** | **-0.0547** | 0.0124 | ±0.0248 | **-4.405** | **1.06e-05** | *** |
| **BMI (kg/m2)** | **-0.0523** | 0.0177 | ±0.0354 | **-2.956** | **0.0031** | ** |
| Hypertension | -0.4257 | 0.2947 | ±0.5894 | -1.444 | 0.1486 |  |
| High cholesterol | -0.1993 | 0.2722 | ±0.5444 | -0.732 | 0.4641 |  |
| Kidney disease | +0.5570 | 0.5359 | ±1.0717 | +1.039 | 0.2986 |  |
| Circulatory disease | -0.6770 | 0.4747 | ±0.9493 | -1.426 | 0.1538 |  |
| Time 54-250, pooled (%) | -1.1873 | 2.4897 | ±4.9794 | -0.477 | 0.6334 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **454**, R² = **0.1372**, Adj R² = **0.1157**, F-statistic = **6.39** (p = **7.36e-10**), Residual SE = **2.632** on **442** df, AIC = **2178.8**, BIC = **2228.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +259.2241 | 298.7602 | ±597.5204 | +0.868 | 0.3856 |  |
| **Education: graduate level (vs college)** | **+0.7998** | 0.2597 | ±0.5193 | **+3.080** | **0.0021** | ** |
| Education: high school or below (vs college) | -0.8356 | 0.5853 | ±1.1706 | -1.428 | 0.1534 |  |
| Site: UCSD (vs UAB) | -0.6364 | 0.3394 | ±0.6789 | -1.875 | 0.0608 | . |
| Site: UW (vs UAB) | -0.5143 | 0.3285 | ±0.6569 | -1.566 | 0.1174 |  |
| **Age (years)** | **-0.0549** | 0.0124 | ±0.0248 | **-4.420** | **9.88e-06** | *** |
| **BMI (kg/m2)** | **-0.0520** | 0.0177 | ±0.0353 | **-2.943** | **0.0033** | ** |
| Hypertension | -0.4179 | 0.2950 | ±0.5900 | -1.417 | 0.1566 |  |
| High cholesterol | -0.2038 | 0.2727 | ±0.5455 | -0.747 | 0.4548 |  |
| Kidney disease | +0.5582 | 0.5351 | ±1.0701 | +1.043 | 0.2968 |  |
| Circulatory disease | -0.6901 | 0.4740 | ±0.9479 | -1.456 | 0.1454 |  |
| Avg. daily time 54-250 (%) | -2.2781 | 2.9885 | ±5.9771 | -0.762 | 0.4459 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **454**, R² = **0.1391**, Adj R² = **0.1177**, F-statistic = **6.49** (p = **4.78e-10**), Residual SE = **2.629** on **442** df, AIC = **2177.8**, BIC = **2227.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.6584** | 1.0370 | ±2.0740 | **+30.529** | **1.07e-204** | *** |
| **Education: graduate level (vs college)** | **+0.7944** | 0.2597 | ±0.5195 | **+3.058** | **0.0022** | ** |
| Education: high school or below (vs college) | -0.8744 | 0.5815 | ±1.1629 | -1.504 | 0.1326 |  |
| Site: UCSD (vs UAB) | -0.6489 | 0.3379 | ±0.6758 | -1.920 | 0.0548 | . |
| Site: UW (vs UAB) | -0.5124 | 0.3265 | ±0.6530 | -1.569 | 0.1166 |  |
| **Age (years)** | **-0.0554** | 0.0124 | ±0.0249 | **-4.452** | **8.51e-06** | *** |
| **BMI (kg/m2)** | **-0.0530** | 0.0180 | ±0.0361 | **-2.940** | **0.0033** | ** |
| Hypertension | -0.3982 | 0.2949 | ±0.5898 | -1.350 | 0.1769 |  |
| High cholesterol | -0.2114 | 0.2733 | ±0.5465 | -0.774 | 0.4391 |  |
| Kidney disease | +0.6204 | 0.5351 | ±1.0702 | +1.159 | 0.2463 |  |
| Circulatory disease | -0.6727 | 0.4750 | ±0.9500 | -1.416 | 0.1567 |  |
| Time 181-250, pooled (%) | -0.5550 | 0.4597 | ±0.9194 | -1.207 | 0.2273 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **454**, R² = **0.1365**, Adj R² = **0.1150**, F-statistic = **6.35** (p = **8.65e-10**), Residual SE = **2.633** on **442** df, AIC = **2179.2**, BIC = **2228.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.5140** | 1.0200 | ±2.0399 | **+30.897** | **1.29e-209** | *** |
| **Education: graduate level (vs college)** | **+0.7973** | 0.2598 | ±0.5196 | **+3.069** | **0.0021** | ** |
| Education: high school or below (vs college) | -0.8608 | 0.5874 | ±1.1748 | -1.465 | 0.1428 |  |
| Site: UCSD (vs UAB) | -0.6515 | 0.3376 | ±0.6752 | -1.930 | 0.0536 | . |
| Site: UW (vs UAB) | -0.5151 | 0.3280 | ±0.6559 | -1.571 | 0.1163 |  |
| **Age (years)** | **-0.0554** | 0.0124 | ±0.0249 | **-4.455** | **8.38e-06** | *** |
| **BMI (kg/m2)** | **-0.0518** | 0.0176 | ±0.0352 | **-2.948** | **0.0032** | ** |
| Hypertension | -0.4091 | 0.2960 | ±0.5920 | -1.382 | 0.1670 |  |
| High cholesterol | -0.2028 | 0.2729 | ±0.5458 | -0.743 | 0.4574 |  |
| Kidney disease | +0.5600 | 0.5352 | ±1.0705 | +1.046 | 0.2954 |  |
| Circulatory disease | -0.6678 | 0.4755 | ±0.9511 | -1.404 | 0.1602 |  |
| Avg. daily time 181-250 (%) | -0.1943 | 0.4803 | ±0.9607 | -0.405 | 0.6858 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **454**, R² = **0.1392**, Adj R² = **0.1178**, F-statistic = **6.50** (p = **4.70e-10**), Residual SE = **2.629** on **442** df, AIC = **2177.7**, BIC = **2227.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.6645** | 1.0376 | ±2.0751 | **+30.519** | **1.48e-204** | *** |
| **Education: graduate level (vs college)** | **+0.7944** | 0.2597 | ±0.5195 | **+3.058** | **0.0022** | ** |
| Education: high school or below (vs college) | -0.8750 | 0.5814 | ±1.1628 | -1.505 | 0.1323 |  |
| Site: UCSD (vs UAB) | -0.6496 | 0.3378 | ±0.6755 | -1.923 | 0.0544 | . |
| Site: UW (vs UAB) | -0.5129 | 0.3264 | ±0.6528 | -1.571 | 0.1161 |  |
| **Age (years)** | **-0.0554** | 0.0124 | ±0.0249 | **-4.455** | **8.40e-06** | *** |
| **BMI (kg/m2)** | **-0.0531** | 0.0181 | ±0.0361 | **-2.941** | **0.0033** | ** |
| Hypertension | -0.3983 | 0.2949 | ±0.5898 | -1.351 | 0.1767 |  |
| High cholesterol | -0.2114 | 0.2732 | ±0.5465 | -0.774 | 0.4392 |  |
| Kidney disease | +0.6212 | 0.5350 | ±1.0700 | +1.161 | 0.2456 |  |
| Circulatory disease | -0.6728 | 0.4750 | ±0.9500 | -1.416 | 0.1567 |  |
| Time > 180 (%) | -0.5611 | 0.4586 | ±0.9173 | -1.223 | 0.2211 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **454**, R² = **0.1365**, Adj R² = **0.1150**, F-statistic = **6.35** (p = **8.59e-10**), Residual SE = **2.633** on **442** df, AIC = **2179.2**, BIC = **2228.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.5181** | 1.0202 | ±2.0404 | **+30.894** | **1.42e-209** | *** |
| **Education: graduate level (vs college)** | **+0.7973** | 0.2598 | ±0.5196 | **+3.069** | **0.0021** | ** |
| Education: high school or below (vs college) | -0.8614 | 0.5873 | ±1.1746 | -1.467 | 0.1425 |  |
| Site: UCSD (vs UAB) | -0.6517 | 0.3374 | ±0.6749 | -1.931 | 0.0534 | . |
| Site: UW (vs UAB) | -0.5152 | 0.3279 | ±0.6557 | -1.571 | 0.1161 |  |
| **Age (years)** | **-0.0554** | 0.0124 | ±0.0249 | **-4.456** | **8.33e-06** | *** |
| **BMI (kg/m2)** | **-0.0519** | 0.0176 | ±0.0352 | **-2.949** | **0.0032** | ** |
| Hypertension | -0.4090 | 0.2960 | ±0.5920 | -1.382 | 0.1670 |  |
| High cholesterol | -0.2027 | 0.2729 | ±0.5458 | -0.743 | 0.4576 |  |
| Kidney disease | +0.5607 | 0.5351 | ±1.0702 | +1.048 | 0.2947 |  |
| Circulatory disease | -0.6678 | 0.4755 | ±0.9511 | -1.404 | 0.1602 |  |
| Avg. daily time > 180 (%) | -0.2020 | 0.4788 | ±0.9576 | -0.422 | 0.6732 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 454)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **454**, R² = **0.1386**, Adj R² = **0.1172**, F-statistic = **6.47** (p = **5.33e-10**), Residual SE = **2.629** on **442** df, AIC = **2178.0**, BIC = **2227.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.5659** | 1.0165 | ±2.0331 | **+31.053** | **1.05e-211** | *** |
| **Education: graduate level (vs college)** | **+0.7807** | 0.2593 | ±0.5187 | **+3.010** | **0.0026** | ** |
| Education: high school or below (vs college) | -0.8555 | 0.5873 | ±1.1746 | -1.457 | 0.1452 |  |
| Site: UCSD (vs UAB) | -0.6519 | 0.3373 | ±0.6746 | -1.933 | 0.0533 | . |
| Site: UW (vs UAB) | -0.5051 | 0.3285 | ±0.6571 | -1.538 | 0.1242 |  |
| **Age (years)** | **-0.0573** | 0.0125 | ±0.0250 | **-4.587** | **4.49e-06** | *** |
| **BMI (kg/m2)** | **-0.0502** | 0.0177 | ±0.0353 | **-2.840** | **0.0045** | ** |
| Hypertension | -0.3867 | 0.2914 | ±0.5827 | -1.327 | 0.1845 |  |
| High cholesterol | -0.1928 | 0.2710 | ±0.5420 | -0.712 | 0.4767 |  |
| Kidney disease | +0.5598 | 0.5426 | ±1.0853 | +1.032 | 0.3022 |  |
| Circulatory disease | -0.6893 | 0.4741 | ±0.9482 | -1.454 | 0.1460 |  |
| Nocturnal time > 180 (%) | -0.4047 | 0.4785 | ±0.9570 | -0.846 | 0.3977 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 454; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0756**, LLR χ² = **43.31** (p = **4.38e-06**), AUC = **0.6756**, AIC = **551.9**, BIC = **597.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.8921** | 0.8867 | ±1.7734 | **-4.389** | **1.14e-05** | 0.0204 | *** |
| **Education: graduate level (vs college)** | **-0.5981** | 0.2262 | ±0.4524 | **-2.644** | **0.0082** | 0.5499 | ** |
| **Education: high school or below (vs college)** | **+0.7437** | 0.3659 | ±0.7317 | **+2.033** | **0.0421** | 2.1037 | * |
| Site: UCSD (vs UAB) | +0.4152 | 0.2703 | ±0.5405 | +1.536 | 0.1245 | 1.5147 |  |
| Site: UW (vs UAB) | +0.3762 | 0.2799 | ±0.5599 | +1.344 | 0.1790 | 1.4567 |  |
| **Age (years)** | **+0.0290** | 0.0100 | ±0.0200 | **+2.898** | **0.0038** | 1.0294 | ** |
| **BMI (kg/m2)** | **+0.0389** | 0.0164 | ±0.0327 | **+2.380** | **0.0173** | 1.0397 | * |
| Hypertension | +0.3229 | 0.2284 | ±0.4569 | +1.414 | 0.1574 | 1.3812 |  |
| High cholesterol | +0.0987 | 0.2195 | ±0.4391 | +0.450 | 0.6530 | 1.1037 |  |
| Kidney disease | -0.3809 | 0.4846 | ±0.9693 | -0.786 | 0.4319 | 0.6832 |  |
| Circulatory disease | +0.4538 | 0.3208 | ±0.6416 | +1.415 | 0.1572 | 1.5743 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0756**, LLR χ² = **43.33** (p = **9.51e-06**), AUC = **0.6758**, AIC = **553.9**, BIC = **603.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.1666** | 2.0358 | ±4.0716 | **-2.047** | **0.0407** | 0.0155 | * |
| **Education: graduate level (vs college)** | **-0.5976** | 0.2262 | ±0.4524 | **-2.642** | **0.0082** | 0.5501 | ** |
| **Education: high school or below (vs college)** | **+0.7400** | 0.3667 | ±0.7335 | **+2.018** | **0.0436** | 2.0959 | * |
| Site: UCSD (vs UAB) | +0.4164 | 0.2704 | ±0.5407 | +1.540 | 0.1235 | 1.5165 |  |
| Site: UW (vs UAB) | +0.3783 | 0.2804 | ±0.5608 | +1.349 | 0.1773 | 1.4597 |  |
| **Age (years)** | **+0.0289** | 0.0100 | ±0.0201 | **+2.878** | **0.0040** | 1.0293 | ** |
| **BMI (kg/m2)** | **+0.0386** | 0.0165 | ±0.0329 | **+2.345** | **0.0190** | 1.0394 | * |
| Hypertension | +0.3201 | 0.2292 | ±0.4585 | +1.396 | 0.1627 | 1.3772 |  |
| High cholesterol | +0.0921 | 0.2240 | ±0.4479 | +0.411 | 0.6810 | 1.0964 |  |
| Kidney disease | -0.3768 | 0.4857 | ±0.9714 | -0.776 | 0.4379 | 0.6861 |  |
| Circulatory disease | +0.4548 | 0.3209 | ±0.6417 | +1.418 | 0.1563 | 1.5759 |  |
| HbA1c (%) | +0.0528 | 0.3520 | ±0.7039 | +0.150 | 0.8808 | 1.0542 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0798**, LLR χ² = **45.73** (p = **3.61e-06**), AUC = **0.6826**, AIC = **551.5**, BIC = **600.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-6.3940** | 1.8500 | ±3.7000 | **-3.456** | **5.48e-04** | 0.0017 | *** |
| **Education: graduate level (vs college)** | **-0.6101** | 0.2271 | ±0.4541 | **-2.687** | **0.0072** | 0.5433 | ** |
| **Education: high school or below (vs college)** | **+0.7661** | 0.3678 | ±0.7356 | **+2.083** | **0.0372** | 2.1515 | * |
| Site: UCSD (vs UAB) | +0.4018 | 0.2713 | ±0.5427 | +1.481 | 0.1386 | 1.4945 |  |
| Site: UW (vs UAB) | +0.3554 | 0.2813 | ±0.5627 | +1.263 | 0.2065 | 1.4267 |  |
| **Age (years)** | **+0.0295** | 0.0100 | ±0.0200 | **+2.940** | **0.0033** | 1.0299 | ** |
| **BMI (kg/m2)** | **+0.0376** | 0.0164 | ±0.0328 | **+2.290** | **0.0220** | 1.0383 | * |
| Hypertension | +0.3033 | 0.2294 | ±0.4589 | +1.322 | 0.1861 | 1.3544 |  |
| High cholesterol | +0.1186 | 0.2207 | ±0.4414 | +0.538 | 0.5908 | 1.1260 |  |
| Kidney disease | -0.4021 | 0.4847 | ±0.9695 | -0.829 | 0.4069 | 0.6689 |  |
| Circulatory disease | +0.4450 | 0.3208 | ±0.6415 | +1.387 | 0.1653 | 1.5605 |  |
| Mean glucose (mg/dL) | +0.0221 | 0.0142 | ±0.0284 | +1.555 | 0.1200 | 1.0223 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0798**, LLR χ² = **45.73** (p = **3.61e-06**), AUC = **0.6826**, AIC = **551.5**, BIC = **600.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-9.4482** | 3.6956 | ±7.3913 | **-2.557** | **0.0106** | 0.0001 | * |
| **Education: graduate level (vs college)** | **-0.6101** | 0.2271 | ±0.4541 | **-2.687** | **0.0072** | 0.5433 | ** |
| **Education: high school or below (vs college)** | **+0.7661** | 0.3678 | ±0.7356 | **+2.083** | **0.0372** | 2.1515 | * |
| Site: UCSD (vs UAB) | +0.4018 | 0.2713 | ±0.5427 | +1.481 | 0.1386 | 1.4945 |  |
| Site: UW (vs UAB) | +0.3554 | 0.2813 | ±0.5627 | +1.263 | 0.2065 | 1.4267 |  |
| **Age (years)** | **+0.0295** | 0.0100 | ±0.0200 | **+2.940** | **0.0033** | 1.0299 | ** |
| **BMI (kg/m2)** | **+0.0376** | 0.0164 | ±0.0328 | **+2.290** | **0.0220** | 1.0383 | * |
| Hypertension | +0.3033 | 0.2294 | ±0.4589 | +1.322 | 0.1861 | 1.3544 |  |
| High cholesterol | +0.1186 | 0.2207 | ±0.4414 | +0.538 | 0.5908 | 1.1260 |  |
| Kidney disease | -0.4021 | 0.4847 | ±0.9695 | -0.829 | 0.4069 | 0.6689 |  |
| Circulatory disease | +0.4450 | 0.3208 | ±0.6415 | +1.387 | 0.1653 | 1.5605 |  |
| GMI (%) | +0.9227 | 0.5935 | ±1.1869 | +1.555 | 0.1200 | 2.5161 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0770**, LLR χ² = **44.12** (p = **6.91e-06**), AUC = **0.6802**, AIC = **553.1**, BIC = **602.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-5.0679** | 1.5812 | ±3.1625 | **-3.205** | **0.0014** | 0.0063 | ** |
| **Education: graduate level (vs college)** | **-0.5990** | 0.2264 | ±0.4527 | **-2.646** | **0.0081** | 0.5493 | ** |
| **Education: high school or below (vs college)** | **+0.7578** | 0.3667 | ±0.7334 | **+2.067** | **0.0388** | 2.1336 | * |
| Site: UCSD (vs UAB) | +0.3977 | 0.2711 | ±0.5422 | +1.467 | 0.1424 | 1.4884 |  |
| Site: UW (vs UAB) | +0.3579 | 0.2811 | ±0.5622 | +1.273 | 0.2029 | 1.4304 |  |
| **Age (years)** | **+0.0303** | 0.0101 | ±0.0202 | **+2.997** | **0.0027** | 1.0307 | ** |
| **BMI (kg/m2)** | **+0.0368** | 0.0164 | ±0.0329 | **+2.236** | **0.0253** | 1.0374 | * |
| Hypertension | +0.3115 | 0.2290 | ±0.4579 | +1.360 | 0.1737 | 1.3654 |  |
| High cholesterol | +0.1051 | 0.2199 | ±0.4399 | +0.478 | 0.6327 | 1.1108 |  |
| Kidney disease | -0.3717 | 0.4841 | ±0.9683 | -0.768 | 0.4426 | 0.6895 |  |
| Circulatory disease | +0.4544 | 0.3204 | ±0.6408 | +1.418 | 0.1561 | 1.5753 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0102 | 0.0113 | ±0.0226 | +0.903 | 0.3664 | 1.0102 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0756**, LLR χ² = **43.31** (p = **9.58e-06**), AUC = **0.6756**, AIC = **553.9**, BIC = **603.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.9279** | 1.1496 | ±2.2992 | **-3.417** | **6.34e-04** | 0.0197 | *** |
| **Education: graduate level (vs college)** | **-0.5974** | 0.2266 | ±0.4531 | **-2.637** | **0.0084** | 0.5502 | ** |
| **Education: high school or below (vs college)** | **+0.7435** | 0.3659 | ±0.7318 | **+2.032** | **0.0422** | 2.1033 | * |
| Site: UCSD (vs UAB) | +0.4157 | 0.2704 | ±0.5408 | +1.537 | 0.1242 | 1.5154 |  |
| Site: UW (vs UAB) | +0.3768 | 0.2803 | ±0.5605 | +1.345 | 0.1787 | 1.4577 |  |
| **Age (years)** | **+0.0290** | 0.0100 | ±0.0200 | **+2.897** | **0.0038** | 1.0294 | ** |
| **BMI (kg/m2)** | **+0.0389** | 0.0164 | ±0.0327 | **+2.376** | **0.0175** | 1.0397 | * |
| Hypertension | +0.3221 | 0.2291 | ±0.4581 | +1.406 | 0.1596 | 1.3801 |  |
| High cholesterol | +0.0994 | 0.2201 | ±0.4401 | +0.452 | 0.6513 | 1.1046 |  |
| Kidney disease | -0.3836 | 0.4879 | ±0.9757 | -0.786 | 0.4317 | 0.6814 |  |
| Circulatory disease | +0.4533 | 0.3210 | ±0.6420 | +1.412 | 0.1579 | 1.5734 |  |
| Glucose SD, pooled (mg/dL) | +0.0022 | 0.0450 | ±0.0900 | +0.049 | 0.9610 | 1.0022 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0757**, LLR χ² = **43.42** (p = **9.18e-06**), AUC = **0.6759**, AIC = **553.8**, BIC = **603.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.6817** | 1.0900 | ±2.1799 | **-3.378** | **7.31e-04** | 0.0252 | *** |
| **Education: graduate level (vs college)** | **-0.6029** | 0.2267 | ±0.4535 | **-2.659** | **0.0078** | 0.5472 | ** |
| **Education: high school or below (vs college)** | **+0.7431** | 0.3658 | ±0.7316 | **+2.031** | **0.0422** | 2.1025 | * |
| Site: UCSD (vs UAB) | +0.4133 | 0.2705 | ±0.5409 | +1.528 | 0.1265 | 1.5118 |  |
| Site: UW (vs UAB) | +0.3727 | 0.2803 | ±0.5605 | +1.330 | 0.1836 | 1.4516 |  |
| **Age (years)** | **+0.0291** | 0.0100 | ±0.0200 | **+2.907** | **0.0037** | 1.0295 | ** |
| **BMI (kg/m2)** | **+0.0394** | 0.0164 | ±0.0329 | **+2.395** | **0.0166** | 1.0402 | * |
| Hypertension | +0.3264 | 0.2287 | ±0.4573 | +1.428 | 0.1534 | 1.3860 |  |
| High cholesterol | +0.0945 | 0.2198 | ±0.4397 | +0.430 | 0.6672 | 1.0991 |  |
| Kidney disease | -0.3645 | 0.4864 | ±0.9727 | -0.749 | 0.4536 | 0.6945 |  |
| Circulatory disease | +0.4549 | 0.3208 | ±0.6417 | +1.418 | 0.1562 | 1.5761 |  |
| Avg. daily SD (mg/dL) | -0.0148 | 0.0445 | ±0.0890 | -0.332 | 0.7402 | 0.9853 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0762**, LLR χ² = **43.66** (p = **8.32e-06**), AUC = **0.6772**, AIC = **553.6**, BIC = **603.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4650** | 1.1398 | ±2.2797 | **-3.040** | **0.0024** | 0.0313 | ** |
| **Education: graduate level (vs college)** | **-0.6080** | 0.2270 | ±0.4539 | **-2.679** | **0.0074** | 0.5445 | ** |
| **Education: high school or below (vs college)** | **+0.7494** | 0.3660 | ±0.7320 | **+2.047** | **0.0406** | 2.1157 | * |
| Site: UCSD (vs UAB) | +0.4077 | 0.2708 | ±0.5417 | +1.506 | 0.1322 | 1.5034 |  |
| Site: UW (vs UAB) | +0.3651 | 0.2808 | ±0.5616 | +1.300 | 0.1935 | 1.4407 |  |
| **Age (years)** | **+0.0291** | 0.0100 | ±0.0200 | **+2.912** | **0.0036** | 1.0296 | ** |
| **BMI (kg/m2)** | **+0.0391** | 0.0164 | ±0.0328 | **+2.387** | **0.0170** | 1.0399 | * |
| Hypertension | +0.3291 | 0.2287 | ±0.4574 | +1.439 | 0.1502 | 1.3897 |  |
| High cholesterol | +0.0928 | 0.2198 | ±0.4396 | +0.422 | 0.6729 | 1.0972 |  |
| Kidney disease | -0.3533 | 0.4851 | ±0.9703 | -0.728 | 0.4665 | 0.7024 |  |
| Circulatory disease | +0.4594 | 0.3207 | ±0.6415 | +1.432 | 0.1520 | 1.5832 |  |
| CV (%) | -0.0296 | 0.0498 | ±0.0996 | -0.594 | 0.5526 | 0.9709 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0766**, LLR χ² = **43.92** (p = **7.52e-06**), AUC = **0.6779**, AIC = **553.3**, BIC = **602.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.4457** | 1.1404 | ±2.2809 | **-3.898** | **9.69e-05** | 0.0117 | *** |
| **Education: graduate level (vs college)** | **-0.6134** | 0.2274 | ±0.4547 | **-2.698** | **0.0070** | 0.5415 | ** |
| **Education: high school or below (vs college)** | **+0.7523** | 0.3660 | ±0.7320 | **+2.055** | **0.0398** | 2.1218 | * |
| Site: UCSD (vs UAB) | +0.4090 | 0.2708 | ±0.5416 | +1.510 | 0.1309 | 1.5053 |  |
| Site: UW (vs UAB) | +0.3653 | 0.2807 | ±0.5613 | +1.301 | 0.1931 | 1.4409 |  |
| **Age (years)** | **+0.0292** | 0.0100 | ±0.0200 | **+2.912** | **0.0036** | 1.0296 | ** |
| **BMI (kg/m2)** | **+0.0391** | 0.0164 | ±0.0328 | **+2.388** | **0.0169** | 1.0399 | * |
| Hypertension | +0.3313 | 0.2288 | ±0.4575 | +1.448 | 0.1476 | 1.3927 |  |
| High cholesterol | +0.0901 | 0.2199 | ±0.4398 | +0.410 | 0.6820 | 1.0943 |  |
| Kidney disease | -0.3533 | 0.4840 | ±0.9681 | -0.730 | 0.4655 | 0.7024 |  |
| Circulatory disease | +0.4585 | 0.3208 | ±0.6416 | +1.429 | 0.1529 | 1.5817 |  |
| Mean / SD ratio | +0.0786 | 0.1008 | ±0.2015 | +0.780 | 0.4353 | 1.0818 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0768**, LLR χ² = **44.02** (p = **7.20e-06**), AUC = **0.6778**, AIC = **553.2**, BIC = **602.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.4414** | 1.1037 | ±2.2073 | **-4.024** | **5.72e-05** | 0.0118 | *** |
| **Education: graduate level (vs college)** | **-0.6144** | 0.2274 | ±0.4547 | **-2.702** | **0.0069** | 0.5410 | ** |
| **Education: high school or below (vs college)** | **+0.7491** | 0.3659 | ±0.7319 | **+2.047** | **0.0406** | 2.1151 | * |
| Site: UCSD (vs UAB) | +0.4108 | 0.2708 | ±0.5416 | +1.517 | 0.1292 | 1.5081 |  |
| Site: UW (vs UAB) | +0.3660 | 0.2807 | ±0.5614 | +1.304 | 0.1923 | 1.4419 |  |
| **Age (years)** | **+0.0293** | 0.0100 | ±0.0200 | **+2.926** | **0.0034** | 1.0298 | ** |
| **BMI (kg/m2)** | **+0.0397** | 0.0164 | ±0.0329 | **+2.415** | **0.0157** | 1.0405 | * |
| Hypertension | +0.3262 | 0.2285 | ±0.4571 | +1.427 | 0.1535 | 1.3857 |  |
| High cholesterol | +0.0929 | 0.2197 | ±0.4394 | +0.423 | 0.6723 | 1.0974 |  |
| Kidney disease | -0.3528 | 0.4841 | ±0.9682 | -0.729 | 0.4661 | 0.7027 |  |
| Circulatory disease | +0.4496 | 0.3211 | ±0.6423 | +1.400 | 0.1615 | 1.5677 |  |
| Avg. daily mean/SD | +0.0657 | 0.0775 | ±0.1550 | +0.847 | 0.3968 | 1.0679 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0786**, LLR χ² = **45.03** (p = **4.79e-06**), AUC = **0.6814**, AIC = **552.2**, BIC = **601.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.8080** | 1.1344 | ±2.2688 | **-4.238** | **2.25e-05** | 0.0082 | *** |
| **Education: graduate level (vs college)** | **-0.6061** | 0.2268 | ±0.4536 | **-2.672** | **0.0075** | 0.5455 | ** |
| Education: high school or below (vs college) | +0.7077 | 0.3675 | ±0.7350 | +1.926 | 0.0542 | 2.0293 | . |
| Site: UCSD (vs UAB) | +0.4220 | 0.2704 | ±0.5408 | +1.561 | 0.1186 | 1.5251 |  |
| Site: UW (vs UAB) | +0.4043 | 0.2810 | ±0.5621 | +1.439 | 0.1503 | 1.4983 |  |
| **Age (years)** | **+0.0300** | 0.0100 | ±0.0201 | **+2.994** | **0.0028** | 1.0305 | ** |
| **BMI (kg/m2)** | **+0.0398** | 0.0163 | ±0.0327 | **+2.433** | **0.0150** | 1.0406 | * |
| Hypertension | +0.3341 | 0.2292 | ±0.4583 | +1.458 | 0.1449 | 1.3966 |  |
| High cholesterol | +0.0899 | 0.2201 | ±0.4402 | +0.408 | 0.6829 | 1.0941 |  |
| Kidney disease | -0.4087 | 0.4871 | ±0.9742 | -0.839 | 0.4015 | 0.6645 |  |
| Circulatory disease | +0.4718 | 0.3222 | ±0.6444 | +1.464 | 0.1431 | 1.6029 |  |
| MAG (mg/dL/h) | +0.0240 | 0.0183 | ±0.0366 | +1.313 | 0.1893 | 1.0243 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0756**, LLR χ² = **43.35** (p = **9.44e-06**), AUC = **0.6758**, AIC = **553.9**, BIC = **603.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.0476** | 1.1861 | ±2.3721 | **-3.413** | **6.43e-04** | 0.0175 | *** |
| **Education: graduate level (vs college)** | **-0.5966** | 0.2263 | ±0.4526 | **-2.636** | **0.0084** | 0.5507 | ** |
| **Education: high school or below (vs college)** | **+0.7435** | 0.3659 | ±0.7318 | **+2.032** | **0.0422** | 2.1033 | * |
| Site: UCSD (vs UAB) | +0.4168 | 0.2704 | ±0.5408 | +1.542 | 0.1232 | 1.5171 |  |
| Site: UW (vs UAB) | +0.3787 | 0.2802 | ±0.5605 | +1.352 | 0.1765 | 1.4605 |  |
| **Age (years)** | **+0.0289** | 0.0100 | ±0.0200 | **+2.893** | **0.0038** | 1.0294 | ** |
| **BMI (kg/m2)** | **+0.0392** | 0.0164 | ±0.0329 | **+2.385** | **0.0171** | 1.0400 | * |
| Hypertension | +0.3239 | 0.2285 | ±0.4571 | +1.417 | 0.1564 | 1.3825 |  |
| High cholesterol | +0.0988 | 0.2196 | ±0.4391 | +0.450 | 0.6527 | 1.1039 |  |
| Kidney disease | -0.3867 | 0.4859 | ±0.9719 | -0.796 | 0.4261 | 0.6793 |  |
| Circulatory disease | +0.4537 | 0.3209 | ±0.6417 | +1.414 | 0.1573 | 1.5742 |  |
| Avg. daily range (mg/dL) | +0.0019 | 0.0095 | ±0.0189 | +0.198 | 0.8432 | 1.0019 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0780**, LLR χ² = **44.69** (p = **5.51e-06**), AUC = **0.6753**, AIC = **552.5**, BIC = **602.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.2414** | 0.9395 | ±1.8791 | **-4.514** | **6.35e-06** | 0.0144 | *** |
| **Education: graduate level (vs college)** | **-0.6102** | 0.2269 | ±0.4539 | **-2.689** | **0.0072** | 0.5432 | ** |
| Education: high school or below (vs college) | +0.7159 | 0.3672 | ±0.7344 | +1.950 | 0.0512 | 2.0461 | . |
| Site: UCSD (vs UAB) | +0.4326 | 0.2712 | ±0.5424 | +1.595 | 0.1107 | 1.5412 |  |
| Site: UW (vs UAB) | +0.3763 | 0.2810 | ±0.5619 | +1.339 | 0.1804 | 1.4569 |  |
| **Age (years)** | **+0.0293** | 0.0100 | ±0.0200 | **+2.928** | **0.0034** | 1.0298 | ** |
| **BMI (kg/m2)** | **+0.0389** | 0.0164 | ±0.0327 | **+2.376** | **0.0175** | 1.0397 | * |
| Hypertension | +0.2973 | 0.2300 | ±0.4601 | +1.292 | 0.1962 | 1.3462 |  |
| High cholesterol | +0.0937 | 0.2198 | ±0.4397 | +0.426 | 0.6699 | 1.0983 |  |
| Kidney disease | -0.3872 | 0.4869 | ±0.9738 | -0.795 | 0.4265 | 0.6790 |  |
| Circulatory disease | +0.4273 | 0.3229 | ±0.6458 | +1.323 | 0.1858 | 1.5331 |  |
| SD of daily means (mg/dL) | +0.0668 | 0.0568 | ±0.1135 | +1.176 | 0.2394 | 1.0691 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0758**, LLR χ² = **43.48** (p = **8.97e-06**), AUC = **0.6759**, AIC = **553.7**, BIC = **603.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +10.4442 | 35.1609 | ±70.3218 | +0.297 | 0.7664 | 34345.0360 |  |
| **Education: graduate level (vs college)** | **-0.5932** | 0.2265 | ±0.4530 | **-2.619** | **0.0088** | 0.5526 | ** |
| **Education: high school or below (vs college)** | **+0.7471** | 0.3659 | ±0.7318 | **+2.042** | **0.0412** | 2.1110 | * |
| Site: UCSD (vs UAB) | +0.4188 | 0.2704 | ±0.5409 | +1.549 | 0.1215 | 1.5201 |  |
| Site: UW (vs UAB) | +0.3790 | 0.2800 | ±0.5600 | +1.353 | 0.1759 | 1.4608 |  |
| **Age (years)** | **+0.0291** | 0.0100 | ±0.0200 | **+2.903** | **0.0037** | 1.0295 | ** |
| **BMI (kg/m2)** | **+0.0394** | 0.0165 | ±0.0329 | **+2.392** | **0.0168** | 1.0402 | * |
| Hypertension | +0.3206 | 0.2286 | ±0.4571 | +1.403 | 0.1607 | 1.3780 |  |
| High cholesterol | +0.0963 | 0.2196 | ±0.4393 | +0.438 | 0.6612 | 1.1010 |  |
| Kidney disease | -0.3933 | 0.4859 | ±0.9718 | -0.809 | 0.4183 | 0.6748 |  |
| Circulatory disease | +0.4556 | 0.3210 | ±0.6420 | +1.419 | 0.1558 | 1.5772 |  |
| Time in range 70-180, pooled (%) | -0.1442 | 0.3536 | ±0.7072 | -0.408 | 0.6834 | 0.8657 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0757**, LLR χ² = **43.41** (p = **9.20e-06**), AUC = **0.6760**, AIC = **553.8**, BIC = **603.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -14.8268 | 34.0446 | ±68.0893 | -0.436 | 0.6632 | 0.0000 |  |
| **Education: graduate level (vs college)** | **-0.6017** | 0.2265 | ±0.4531 | **-2.656** | **0.0079** | 0.5479 | ** |
| **Education: high school or below (vs college)** | **+0.7409** | 0.3661 | ±0.7322 | **+2.024** | **0.0430** | 2.0978 | * |
| Site: UCSD (vs UAB) | +0.4161 | 0.2704 | ±0.5407 | +1.539 | 0.1238 | 1.5160 |  |
| Site: UW (vs UAB) | +0.3780 | 0.2801 | ±0.5602 | +1.349 | 0.1772 | 1.4593 |  |
| **Age (years)** | **+0.0290** | 0.0100 | ±0.0200 | **+2.896** | **0.0038** | 1.0294 | ** |
| **BMI (kg/m2)** | **+0.0388** | 0.0164 | ±0.0327 | **+2.375** | **0.0176** | 1.0396 | * |
| Hypertension | +0.3212 | 0.2285 | ±0.4570 | +1.406 | 0.1598 | 1.3788 |  |
| High cholesterol | +0.1023 | 0.2198 | ±0.4396 | +0.465 | 0.6418 | 1.1077 |  |
| Kidney disease | -0.3775 | 0.4848 | ±0.9696 | -0.779 | 0.4362 | 0.6856 |  |
| Circulatory disease | +0.4551 | 0.3209 | ±0.6417 | +1.418 | 0.1561 | 1.5763 |  |
| Avg. daily time in range 70-180 (%) | +0.1098 | 0.3417 | ±0.6835 | +0.321 | 0.7480 | 1.1161 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0761**, LLR χ² = **43.60** (p = **8.54e-06**), AUC = **0.6765**, AIC = **553.6**, BIC = **603.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.8559** | 0.8901 | ±1.7801 | **-4.332** | **1.48e-05** | 0.0212 | *** |
| **Education: graduate level (vs college)** | **-0.6009** | 0.2263 | ±0.4526 | **-2.655** | **0.0079** | 0.5483 | ** |
| **Education: high school or below (vs college)** | **+0.7341** | 0.3665 | ±0.7329 | **+2.003** | **0.0452** | 2.0836 | * |
| Site: UCSD (vs UAB) | +0.3930 | 0.2735 | ±0.5470 | +1.437 | 0.1507 | 1.4814 |  |
| Site: UW (vs UAB) | +0.3646 | 0.2811 | ±0.5621 | +1.297 | 0.1945 | 1.4400 |  |
| **Age (years)** | **+0.0289** | 0.0100 | ±0.0200 | **+2.890** | **0.0038** | 1.0293 | ** |
| **BMI (kg/m2)** | **+0.0391** | 0.0164 | ±0.0328 | **+2.385** | **0.0171** | 1.0398 | * |
| Hypertension | +0.3330 | 0.2292 | ±0.4585 | +1.452 | 0.1464 | 1.3951 |  |
| High cholesterol | +0.0991 | 0.2196 | ±0.4393 | +0.451 | 0.6518 | 1.1042 |  |
| Kidney disease | -0.3975 | 0.4852 | ±0.9704 | -0.819 | 0.4127 | 0.6720 |  |
| Circulatory disease | +0.4583 | 0.3209 | ±0.6419 | +1.428 | 0.1533 | 1.5814 |  |
| Any reading < 54 during wear (0/1) | -0.1563 | 0.2917 | ±0.5834 | -0.536 | 0.5920 | 0.8553 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0757**, LLR χ² = **43.40** (p = **9.26e-06**), AUC = **0.6761**, AIC = **553.8**, BIC = **603.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.8775** | 0.8885 | ±1.7771 | **-4.364** | **1.28e-05** | 0.0207 | *** |
| **Education: graduate level (vs college)** | **-0.5996** | 0.2263 | ±0.4526 | **-2.649** | **0.0081** | 0.5490 | ** |
| **Education: high school or below (vs college)** | **+0.7351** | 0.3671 | ±0.7342 | **+2.003** | **0.0452** | 2.0857 | * |
| Site: UCSD (vs UAB) | +0.4053 | 0.2723 | ±0.5446 | +1.488 | 0.1366 | 1.4998 |  |
| Site: UW (vs UAB) | +0.3723 | 0.2804 | ±0.5607 | +1.328 | 0.1842 | 1.4510 |  |
| **Age (years)** | **+0.0288** | 0.0100 | ±0.0200 | **+2.875** | **0.0040** | 1.0292 | ** |
| **BMI (kg/m2)** | **+0.0393** | 0.0164 | ±0.0329 | **+2.393** | **0.0167** | 1.0401 | * |
| Hypertension | +0.3289 | 0.2293 | ±0.4587 | +1.434 | 0.1515 | 1.3894 |  |
| High cholesterol | +0.0970 | 0.2196 | ±0.4393 | +0.441 | 0.6589 | 1.1018 |  |
| Kidney disease | -0.3881 | 0.4853 | ±0.9706 | -0.800 | 0.4239 | 0.6783 |  |
| Circulatory disease | +0.4590 | 0.3212 | ±0.6425 | +1.429 | 0.1531 | 1.5825 |  |
| Time < 54 (%) | -0.6017 | 2.0627 | ±4.1255 | -0.292 | 0.7705 | 0.5479 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0768**, LLR χ² = **44.02** (p = **7.20e-06**), AUC = **0.6775**, AIC = **553.2**, BIC = **602.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.8819** | 0.8878 | ±1.7756 | **-4.372** | **1.23e-05** | 0.0206 | *** |
| **Education: graduate level (vs college)** | **-0.6039** | 0.2267 | ±0.4534 | **-2.664** | **0.0077** | 0.5467 | ** |
| **Education: high school or below (vs college)** | **+0.7315** | 0.3668 | ±0.7335 | **+1.994** | **0.0461** | 2.0782 | * |
| Site: UCSD (vs UAB) | +0.4076 | 0.2707 | ±0.5413 | +1.506 | 0.1321 | 1.5032 |  |
| Site: UW (vs UAB) | +0.3804 | 0.2807 | ±0.5613 | +1.355 | 0.1753 | 1.4629 |  |
| **Age (years)** | **+0.0290** | 0.0100 | ±0.0200 | **+2.898** | **0.0038** | 1.0294 | ** |
| **BMI (kg/m2)** | **+0.0394** | 0.0164 | ±0.0328 | **+2.400** | **0.0164** | 1.0402 | * |
| Hypertension | +0.3267 | 0.2286 | ±0.4572 | +1.429 | 0.1530 | 1.3864 |  |
| High cholesterol | +0.0995 | 0.2198 | ±0.4396 | +0.452 | 0.6509 | 1.1046 |  |
| Kidney disease | -0.3964 | 0.4850 | ±0.9699 | -0.817 | 0.4137 | 0.6728 |  |
| Circulatory disease | +0.4818 | 0.3227 | ±0.6454 | +1.493 | 0.1354 | 1.6190 |  |
| Avg. daily time < 54 (%) | -2.4465 | 3.0437 | ±6.0874 | -0.804 | 0.4215 | 0.0866 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0784**, LLR χ² = **44.96** (p = **4.94e-06**), AUC = **0.6809**, AIC = **552.3**, BIC = **601.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.8053** | 0.8924 | ±1.7847 | **-4.264** | **2.01e-05** | 0.0223 | *** |
| **Education: graduate level (vs college)** | **-0.6160** | 0.2272 | ±0.4543 | **-2.712** | **0.0067** | 0.5401 | ** |
| **Education: high school or below (vs college)** | **+0.7744** | 0.3681 | ±0.7362 | **+2.104** | **0.0354** | 2.1692 | * |
| Site: UCSD (vs UAB) | +0.4061 | 0.2713 | ±0.5425 | +1.497 | 0.1344 | 1.5010 |  |
| Site: UW (vs UAB) | +0.3570 | 0.2809 | ±0.5617 | +1.271 | 0.2037 | 1.4290 |  |
| **Age (years)** | **+0.0293** | 0.0100 | ±0.0200 | **+2.919** | **0.0035** | 1.0297 | ** |
| **BMI (kg/m2)** | **+0.0393** | 0.0164 | ±0.0329 | **+2.392** | **0.0168** | 1.0401 | * |
| Hypertension | +0.3054 | 0.2292 | ±0.4584 | +1.333 | 0.1826 | 1.3572 |  |
| High cholesterol | +0.1282 | 0.2213 | ±0.4426 | +0.580 | 0.5622 | 1.1368 |  |
| Kidney disease | -0.4157 | 0.4840 | ±0.9681 | -0.859 | 0.3905 | 0.6599 |  |
| Circulatory disease | +0.4445 | 0.3205 | ±0.6409 | +1.387 | 0.1654 | 1.5597 |  |
| Time 54-69, pooled (%) | -0.7721 | 0.6110 | ±1.2220 | -1.264 | 0.2063 | 0.4620 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0810**, LLR χ² = **46.44** (p = **2.70e-06**), AUC = **0.6849**, AIC = **550.8**, BIC = **600.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.8208** | 0.8937 | ±1.7874 | **-4.275** | **1.91e-05** | 0.0219 | *** |
| **Education: graduate level (vs college)** | **-0.6327** | 0.2281 | ±0.4561 | **-2.774** | **0.0055** | 0.5311 | ** |
| **Education: high school or below (vs college)** | **+0.7856** | 0.3696 | ±0.7391 | **+2.126** | **0.0335** | 2.1937 | * |
| Site: UCSD (vs UAB) | +0.4196 | 0.2716 | ±0.5433 | +1.545 | 0.1224 | 1.5213 |  |
| Site: UW (vs UAB) | +0.3675 | 0.2809 | ±0.5618 | +1.308 | 0.1908 | 1.4441 |  |
| **Age (years)** | **+0.0299** | 0.0101 | ±0.0201 | **+2.970** | **0.0030** | 1.0303 | ** |
| **BMI (kg/m2)** | **+0.0395** | 0.0165 | ±0.0329 | **+2.397** | **0.0165** | 1.0403 | * |
| Hypertension | +0.2769 | 0.2304 | ±0.4608 | +1.202 | 0.2294 | 1.3190 |  |
| High cholesterol | +0.1334 | 0.2213 | ±0.4427 | +0.603 | 0.5468 | 1.1427 |  |
| Kidney disease | -0.4288 | 0.4852 | ±0.9704 | -0.884 | 0.3769 | 0.6513 |  |
| Circulatory disease | +0.4603 | 0.3208 | ±0.6416 | +1.435 | 0.1513 | 1.5846 |  |
| Avg. daily time 54-69 (%) | -1.1008 | 0.6387 | ±1.2774 | -1.724 | 0.0848 | 0.3326 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0781**, LLR χ² = **44.78** (p = **5.30e-06**), AUC = **0.6805**, AIC = **552.4**, BIC = **601.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.8039** | 0.8927 | ±1.7854 | **-4.261** | **2.03e-05** | 0.0223 | *** |
| **Education: graduate level (vs college)** | **-0.6147** | 0.2271 | ±0.4543 | **-2.706** | **0.0068** | 0.5408 | ** |
| **Education: high school or below (vs college)** | **+0.7603** | 0.3673 | ±0.7346 | **+2.070** | **0.0385** | 2.1389 | * |
| Site: UCSD (vs UAB) | +0.3972 | 0.2714 | ±0.5429 | +1.464 | 0.1433 | 1.4877 |  |
| Site: UW (vs UAB) | +0.3560 | 0.2810 | ±0.5620 | +1.267 | 0.2051 | 1.4277 |  |
| **Age (years)** | **+0.0290** | 0.0100 | ±0.0200 | **+2.898** | **0.0038** | 1.0295 | ** |
| **BMI (kg/m2)** | **+0.0396** | 0.0165 | ±0.0329 | **+2.409** | **0.0160** | 1.0404 | * |
| Hypertension | +0.3141 | 0.2289 | ±0.4579 | +1.372 | 0.1700 | 1.3690 |  |
| High cholesterol | +0.1218 | 0.2209 | ±0.4418 | +0.551 | 0.5813 | 1.1295 |  |
| Kidney disease | -0.4177 | 0.4844 | ±0.9689 | -0.862 | 0.3886 | 0.6586 |  |
| Circulatory disease | +0.4517 | 0.3204 | ±0.6409 | +1.410 | 0.1587 | 1.5709 |  |
| Time < 70 (%) | -0.6457 | 0.5398 | ±1.0797 | -1.196 | 0.2317 | 0.5243 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0811**, LLR χ² = **46.47** (p = **2.66e-06**), AUC = **0.6847**, AIC = **550.7**, BIC = **600.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.8222** | 0.8936 | ±1.7872 | **-4.277** | **1.89e-05** | 0.0219 | *** |
| **Education: graduate level (vs college)** | **-0.6319** | 0.2281 | ±0.4562 | **-2.770** | **0.0056** | 0.5316 | ** |
| **Education: high school or below (vs college)** | **+0.7769** | 0.3693 | ±0.7386 | **+2.104** | **0.0354** | 2.1746 | * |
| Site: UCSD (vs UAB) | +0.4161 | 0.2716 | ±0.5433 | +1.532 | 0.1256 | 1.5160 |  |
| Site: UW (vs UAB) | +0.3699 | 0.2811 | ±0.5621 | +1.316 | 0.1881 | 1.4476 |  |
| **Age (years)** | **+0.0298** | 0.0101 | ±0.0201 | **+2.963** | **0.0030** | 1.0302 | ** |
| **BMI (kg/m2)** | **+0.0396** | 0.0165 | ±0.0330 | **+2.404** | **0.0162** | 1.0404 | * |
| Hypertension | +0.2821 | 0.2302 | ±0.4603 | +1.225 | 0.2204 | 1.3259 |  |
| High cholesterol | +0.1308 | 0.2213 | ±0.4425 | +0.591 | 0.5543 | 1.1398 |  |
| Kidney disease | -0.4310 | 0.4852 | ±0.9705 | -0.888 | 0.3744 | 0.6499 |  |
| Circulatory disease | +0.4709 | 0.3210 | ±0.6420 | +1.467 | 0.1424 | 1.6015 |  |
| Avg. daily time < 70 (%) | -1.0080 | 0.5823 | ±1.1646 | -1.731 | 0.0834 | 0.3649 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0756**, LLR χ² = **43.32** (p = **9.57e-06**), AUC = **0.6759**, AIC = **553.9**, BIC = **603.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -20.3941 | 199.7910 | ±399.5821 | -0.102 | 0.9187 | 0.0000 |  |
| **Education: graduate level (vs college)** | **-0.5984** | 0.2262 | ±0.4525 | **-2.645** | **0.0082** | 0.5497 | ** |
| **Education: high school or below (vs college)** | **+0.7412** | 0.3671 | ±0.7342 | **+2.019** | **0.0435** | 2.0985 | * |
| Site: UCSD (vs UAB) | +0.4123 | 0.2725 | ±0.5450 | +1.513 | 0.1303 | 1.5103 |  |
| Site: UW (vs UAB) | +0.3750 | 0.2803 | ±0.5607 | +1.338 | 0.1810 | 1.4550 |  |
| **Age (years)** | **+0.0289** | 0.0100 | ±0.0200 | **+2.885** | **0.0039** | 1.0293 | ** |
| **BMI (kg/m2)** | **+0.0390** | 0.0164 | ±0.0328 | **+2.379** | **0.0174** | 1.0398 | * |
| Hypertension | +0.3246 | 0.2293 | ±0.4585 | +1.416 | 0.1569 | 1.3834 |  |
| High cholesterol | +0.0983 | 0.2196 | ±0.4392 | +0.447 | 0.6546 | 1.1032 |  |
| Kidney disease | -0.3829 | 0.4852 | ±0.9705 | -0.789 | 0.4301 | 0.6819 |  |
| Circulatory disease | +0.4552 | 0.3212 | ±0.6424 | +1.417 | 0.1564 | 1.5765 |  |
| Time 54-250, pooled (%) | +0.1651 | 1.9985 | ±3.9970 | +0.083 | 0.9342 | 1.1795 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0760**, LLR χ² = **43.58** (p = **8.62e-06**), AUC = **0.6772**, AIC = **553.6**, BIC = **603.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -145.4125 | 282.2386 | ±564.4773 | -0.515 | 0.6064 | 0.0000 |  |
| **Education: graduate level (vs college)** | **-0.6009** | 0.2265 | ±0.4530 | **-2.653** | **0.0080** | 0.5483 | ** |
| **Education: high school or below (vs college)** | **+0.7356** | 0.3665 | ±0.7330 | **+2.007** | **0.0447** | 2.0868 | * |
| Site: UCSD (vs UAB) | +0.4091 | 0.2706 | ±0.5412 | +1.512 | 0.1306 | 1.5055 |  |
| Site: UW (vs UAB) | +0.3776 | 0.2803 | ±0.5607 | +1.347 | 0.1780 | 1.4588 |  |
| **Age (years)** | **+0.0289** | 0.0100 | ±0.0200 | **+2.888** | **0.0039** | 1.0293 | ** |
| **BMI (kg/m2)** | **+0.0391** | 0.0164 | ±0.0328 | **+2.389** | **0.0169** | 1.0399 | * |
| Hypertension | +0.3249 | 0.2285 | ±0.4570 | +1.422 | 0.1551 | 1.3839 |  |
| High cholesterol | +0.0996 | 0.2197 | ±0.4394 | +0.453 | 0.6504 | 1.1047 |  |
| Kidney disease | -0.3899 | 0.4848 | ±0.9696 | -0.804 | 0.4213 | 0.6772 |  |
| Circulatory disease | +0.4697 | 0.3222 | ±0.6444 | +1.458 | 0.1449 | 1.5995 |  |
| Avg. daily time 54-250 (%) | +1.4154 | 2.8226 | ±5.6452 | +0.501 | 0.6161 | 4.1179 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0785**, LLR χ² = **44.97** (p = **4.91e-06**), AUC = **0.6793**, AIC = **552.3**, BIC = **601.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.1141** | 0.9142 | ±1.8284 | **-4.500** | **6.79e-06** | 0.0163 | *** |
| **Education: graduate level (vs college)** | **-0.5945** | 0.2267 | ±0.4535 | **-2.622** | **0.0087** | 0.5518 | ** |
| **Education: high school or below (vs college)** | **+0.7681** | 0.3667 | ±0.7333 | **+2.095** | **0.0362** | 2.1557 | * |
| Site: UCSD (vs UAB) | +0.4135 | 0.2709 | ±0.5418 | +1.526 | 0.1269 | 1.5121 |  |
| Site: UW (vs UAB) | +0.3694 | 0.2804 | ±0.5607 | +1.318 | 0.1876 | 1.4469 |  |
| **Age (years)** | **+0.0292** | 0.0100 | ±0.0201 | **+2.913** | **0.0036** | 1.0297 | ** |
| **BMI (kg/m2)** | **+0.0411** | 0.0167 | ±0.0335 | **+2.455** | **0.0141** | 1.0419 | * |
| Hypertension | +0.3082 | 0.2292 | ±0.4584 | +1.345 | 0.1787 | 1.3610 |  |
| High cholesterol | +0.1083 | 0.2202 | ±0.4404 | +0.492 | 0.6229 | 1.1144 |  |
| Kidney disease | -0.4546 | 0.4886 | ±0.9772 | -0.930 | 0.3521 | 0.6347 |  |
| Circulatory disease | +0.4579 | 0.3212 | ±0.6423 | +1.426 | 0.1540 | 1.5807 |  |
| Time 181-250, pooled (%) | +0.4937 | 0.3827 | ±0.7655 | +1.290 | 0.1970 | 1.6384 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0767**, LLR χ² = **43.98** (p = **7.32e-06**), AUC = **0.6766**, AIC = **553.2**, BIC = **602.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.9984** | 0.8978 | ±1.7956 | **-4.454** | **8.45e-06** | 0.0183 | *** |
| **Education: graduate level (vs college)** | **-0.5984** | 0.2264 | ±0.4527 | **-2.644** | **0.0082** | 0.5497 | ** |
| **Education: high school or below (vs college)** | **+0.7629** | 0.3669 | ±0.7337 | **+2.080** | **0.0376** | 2.1445 | * |
| Site: UCSD (vs UAB) | +0.4133 | 0.2705 | ±0.5409 | +1.528 | 0.1265 | 1.5118 |  |
| Site: UW (vs UAB) | +0.3688 | 0.2802 | ±0.5604 | +1.316 | 0.1881 | 1.4460 |  |
| **Age (years)** | **+0.0292** | 0.0100 | ±0.0200 | **+2.920** | **0.0035** | 1.0297 | ** |
| **BMI (kg/m2)** | **+0.0394** | 0.0164 | ±0.0328 | **+2.399** | **0.0164** | 1.0402 | * |
| Hypertension | +0.3149 | 0.2288 | ±0.4577 | +1.376 | 0.1689 | 1.3701 |  |
| High cholesterol | +0.0990 | 0.2198 | ±0.4396 | +0.451 | 0.6523 | 1.1041 |  |
| Kidney disease | -0.4085 | 0.4859 | ±0.9717 | -0.841 | 0.4005 | 0.6647 |  |
| Circulatory disease | +0.4553 | 0.3207 | ±0.6415 | +1.419 | 0.1558 | 1.5766 |  |
| Avg. daily time 181-250 (%) | +0.3105 | 0.3779 | ±0.7557 | +0.822 | 0.4112 | 1.3642 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0786**, LLR χ² = **45.07** (p = **4.72e-06**), AUC = **0.6794**, AIC = **552.2**, BIC = **601.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.1239** | 0.9150 | ±1.8301 | **-4.507** | **6.58e-06** | 0.0162 | *** |
| **Education: graduate level (vs college)** | **-0.5945** | 0.2268 | ±0.4535 | **-2.622** | **0.0087** | 0.5518 | ** |
| **Education: high school or below (vs college)** | **+0.7692** | 0.3667 | ±0.7334 | **+2.098** | **0.0359** | 2.1580 | * |
| Site: UCSD (vs UAB) | +0.4139 | 0.2709 | ±0.5418 | +1.528 | 0.1265 | 1.5127 |  |
| Site: UW (vs UAB) | +0.3695 | 0.2804 | ±0.5607 | +1.318 | 0.1875 | 1.4471 |  |
| **Age (years)** | **+0.0293** | 0.0100 | ±0.0201 | **+2.916** | **0.0035** | 1.0297 | ** |
| **BMI (kg/m2)** | **+0.0412** | 0.0167 | ±0.0335 | **+2.459** | **0.0139** | 1.0420 | * |
| Hypertension | +0.3080 | 0.2292 | ±0.4584 | +1.344 | 0.1790 | 1.3607 |  |
| High cholesterol | +0.1084 | 0.2202 | ±0.4405 | +0.492 | 0.6226 | 1.1145 |  |
| Kidney disease | -0.4569 | 0.4887 | ±0.9773 | -0.935 | 0.3498 | 0.6332 |  |
| Circulatory disease | +0.4580 | 0.3212 | ±0.6424 | +1.426 | 0.1539 | 1.5810 |  |
| Time > 180 (%) | +0.5079 | 0.3824 | ±0.7647 | +1.328 | 0.1841 | 1.6617 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0768**, LLR χ² = **44.05** (p = **7.12e-06**), AUC = **0.6766**, AIC = **553.2**, BIC = **602.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.0059** | 0.8983 | ±1.7966 | **-4.459** | **8.22e-06** | 0.0182 | *** |
| **Education: graduate level (vs college)** | **-0.5985** | 0.2264 | ±0.4528 | **-2.644** | **0.0082** | 0.5496 | ** |
| **Education: high school or below (vs college)** | **+0.7641** | 0.3669 | ±0.7338 | **+2.082** | **0.0373** | 2.1470 | * |
| Site: UCSD (vs UAB) | +0.4135 | 0.2705 | ±0.5410 | +1.529 | 0.1263 | 1.5122 |  |
| Site: UW (vs UAB) | +0.3686 | 0.2802 | ±0.5604 | +1.316 | 0.1883 | 1.4457 |  |
| **Age (years)** | **+0.0293** | 0.0100 | ±0.0200 | **+2.923** | **0.0035** | 1.0297 | ** |
| **BMI (kg/m2)** | **+0.0395** | 0.0164 | ±0.0329 | **+2.401** | **0.0163** | 1.0402 | * |
| Hypertension | +0.3146 | 0.2289 | ±0.4577 | +1.375 | 0.1692 | 1.3698 |  |
| High cholesterol | +0.0989 | 0.2198 | ±0.4397 | +0.450 | 0.6527 | 1.1040 |  |
| Kidney disease | -0.4099 | 0.4859 | ±0.9718 | -0.844 | 0.3989 | 0.6637 |  |
| Circulatory disease | +0.4554 | 0.3208 | ±0.6415 | +1.420 | 0.1557 | 1.5768 |  |
| Avg. daily time > 180 (%) | +0.3257 | 0.3772 | ±0.7544 | +0.863 | 0.3879 | 1.3850 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 454)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **454**, events = **148**, McFadden pseudo-R² = **0.0782**, LLR χ² = **44.81** (p = **5.25e-06**), AUC = **0.6798**, AIC = **552.4**, BIC = **601.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.0083** | 0.8912 | ±1.7823 | **-4.498** | **6.87e-06** | 0.0182 | *** |
| **Education: graduate level (vs college)** | **-0.5873** | 0.2269 | ±0.4537 | **-2.589** | **0.0096** | 0.5558 | ** |
| **Education: high school or below (vs college)** | **+0.7499** | 0.3666 | ±0.7333 | **+2.045** | **0.0408** | 2.1168 | * |
| Site: UCSD (vs UAB) | +0.4142 | 0.2702 | ±0.5405 | +1.533 | 0.1254 | 1.5131 |  |
| Site: UW (vs UAB) | +0.3639 | 0.2806 | ±0.5611 | +1.297 | 0.1946 | 1.4389 |  |
| **Age (years)** | **+0.0310** | 0.0102 | ±0.0203 | **+3.053** | **0.0023** | 1.0315 | ** |
| **BMI (kg/m2)** | **+0.0376** | 0.0163 | ±0.0327 | **+2.303** | **0.0213** | 1.0383 | * |
| Hypertension | +0.2979 | 0.2296 | ±0.4592 | +1.298 | 0.1945 | 1.3471 |  |
| High cholesterol | +0.0944 | 0.2199 | ±0.4398 | +0.429 | 0.6677 | 1.0990 |  |
| Kidney disease | -0.3910 | 0.4835 | ±0.9670 | -0.809 | 0.4187 | 0.6764 |  |
| Circulatory disease | +0.4737 | 0.3210 | ±0.6420 | +1.476 | 0.1400 | 1.6060 |  |
| Nocturnal time > 180 (%) | +0.3540 | 0.2856 | ±0.5713 | +1.239 | 0.2152 | 1.4248 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 454; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **454**, R² = **0.0873**, Adj R² = **0.0667**, F-statistic = **4.24** (p = **1.20e-05**), Residual SE = **2.576** on **443** df, AIC = **2158.5**, BIC = **2203.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4515** | 1.0446 | ±2.0892 | **+15.749** | **6.96e-56** | *** |
| Education: graduate level (vs college) | +0.3106 | 0.2588 | ±0.5177 | +1.200 | 0.2302 |  |
| **Education: high school or below (vs college)** | **-1.1913** | 0.5936 | ±1.1872 | **-2.007** | **0.0448** | * |
| Site: UCSD (vs UAB) | -0.1771 | 0.3172 | ±0.6343 | -0.558 | 0.5767 |  |
| Site: UW (vs UAB) | -0.0378 | 0.3397 | ±0.6793 | -0.111 | 0.9113 |  |
| **Age (years)** | **-0.0398** | 0.0125 | ±0.0250 | **-3.187** | **0.0014** | ** |
| **BMI (kg/m2)** | **-0.0336** | 0.0169 | ±0.0338 | **-1.989** | **0.0467** | * |
| Hypertension | -0.5044 | 0.2861 | ±0.5723 | -1.763 | 0.0780 | . |
| High cholesterol | -0.1224 | 0.2705 | ±0.5410 | -0.452 | 0.6511 |  |
| Kidney disease | -0.0625 | 0.6865 | ±1.3730 | -0.091 | 0.9275 |  |
| Circulatory disease | -0.2206 | 0.4129 | ±0.8257 | -0.534 | 0.5931 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **454**, R² = **0.0873**, Adj R² = **0.0646**, F-statistic = **3.85** (p = **2.61e-05**), Residual SE = **2.579** on **442** df, AIC = **2160.5**, BIC = **2209.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.2507** | 2.6751 | ±5.3503 | **+6.075** | **1.24e-09** | *** |
| Education: graduate level (vs college) | +0.3114 | 0.2598 | ±0.5197 | +1.198 | 0.2308 |  |
| **Education: high school or below (vs college)** | **-1.1942** | 0.6011 | ±1.2021 | **-1.987** | **0.0469** | * |
| Site: UCSD (vs UAB) | -0.1765 | 0.3179 | ±0.6358 | -0.555 | 0.5787 |  |
| Site: UW (vs UAB) | -0.0368 | 0.3409 | ±0.6817 | -0.108 | 0.9141 |  |
| **Age (years)** | **-0.0399** | 0.0126 | ±0.0253 | **-3.157** | **0.0016** | ** |
| **BMI (kg/m2)** | **-0.0338** | 0.0165 | ±0.0331 | **-2.042** | **0.0411** | * |
| Hypertension | -0.5068 | 0.2862 | ±0.5724 | -1.771 | 0.0766 | . |
| High cholesterol | -0.1270 | 0.2664 | ±0.5327 | -0.477 | 0.6335 |  |
| Kidney disease | -0.0598 | 0.6902 | ±1.3803 | -0.087 | 0.9309 |  |
| Circulatory disease | -0.2200 | 0.4156 | ±0.8313 | -0.529 | 0.5966 |  |
| HbA1c (%) | +0.0387 | 0.4536 | ±0.9072 | +0.085 | 0.9321 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **454**, R² = **0.0889**, Adj R² = **0.0663**, F-statistic = **3.92** (p = **1.91e-05**), Residual SE = **2.577** on **442** df, AIC = **2159.7**, BIC = **2209.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.0703** | 2.1169 | ±4.2337 | **+8.536** | **1.38e-17** | *** |
| Education: graduate level (vs college) | +0.3131 | 0.2595 | ±0.5190 | +1.207 | 0.2275 |  |
| **Education: high school or below (vs college)** | **-1.2036** | 0.5940 | ±1.1881 | **-2.026** | **0.0427** | * |
| Site: UCSD (vs UAB) | -0.1641 | 0.3185 | ±0.6369 | -0.515 | 0.6064 |  |
| Site: UW (vs UAB) | -0.0218 | 0.3398 | ±0.6796 | -0.064 | 0.9489 |  |
| **Age (years)** | **-0.0401** | 0.0124 | ±0.0249 | **-3.219** | **0.0013** | ** |
| BMI (kg/m2) | -0.0326 | 0.0169 | ±0.0337 | -1.935 | 0.0530 | . |
| Hypertension | -0.4903 | 0.2874 | ±0.5747 | -1.706 | 0.0879 | . |
| High cholesterol | -0.1325 | 0.2720 | ±0.5441 | -0.487 | 0.6262 |  |
| Kidney disease | -0.0480 | 0.6868 | ±1.3736 | -0.070 | 0.9443 |  |
| Circulatory disease | -0.2113 | 0.4115 | ±0.8230 | -0.514 | 0.6076 |  |
| Mean glucose (mg/dL) | -0.0144 | 0.0169 | ±0.0339 | -0.849 | 0.3958 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **454**, R² = **0.0889**, Adj R² = **0.0663**, F-statistic = **3.92** (p = **1.91e-05**), Residual SE = **2.577** on **442** df, AIC = **2159.7**, BIC = **2209.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20.0593** | 4.3124 | ±8.6249 | **+4.651** | **3.30e-06** | *** |
| Education: graduate level (vs college) | +0.3131 | 0.2595 | ±0.5190 | +1.207 | 0.2275 |  |
| **Education: high school or below (vs college)** | **-1.2036** | 0.5940 | ±1.1881 | **-2.026** | **0.0427** | * |
| Site: UCSD (vs UAB) | -0.1641 | 0.3185 | ±0.6369 | -0.515 | 0.6064 |  |
| Site: UW (vs UAB) | -0.0218 | 0.3398 | ±0.6796 | -0.064 | 0.9489 |  |
| **Age (years)** | **-0.0401** | 0.0124 | ±0.0249 | **-3.219** | **0.0013** | ** |
| BMI (kg/m2) | -0.0326 | 0.0169 | ±0.0337 | -1.935 | 0.0530 | . |
| Hypertension | -0.4903 | 0.2874 | ±0.5747 | -1.706 | 0.0879 | . |
| High cholesterol | -0.1325 | 0.2720 | ±0.5441 | -0.487 | 0.6262 |  |
| Kidney disease | -0.0480 | 0.6868 | ±1.3736 | -0.070 | 0.9443 |  |
| Circulatory disease | -0.2113 | 0.4115 | ±0.8230 | -0.514 | 0.6076 |  |
| GMI (%) | -0.6009 | 0.7076 | ±1.4152 | -0.849 | 0.3958 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **454**, R² = **0.0888**, Adj R² = **0.0661**, F-statistic = **3.92** (p = **1.97e-05**), Residual SE = **2.577** on **442** df, AIC = **2159.8**, BIC = **2209.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.6958** | 1.7572 | ±3.5144 | **+10.070** | **7.47e-24** | *** |
| Education: graduate level (vs college) | +0.3052 | 0.2595 | ±0.5190 | +1.176 | 0.2396 |  |
| **Education: high school or below (vs college)** | **-1.2060** | 0.5952 | ±1.1905 | **-2.026** | **0.0428** | * |
| Site: UCSD (vs UAB) | -0.1539 | 0.3190 | ±0.6380 | -0.482 | 0.6296 |  |
| Site: UW (vs UAB) | -0.0164 | 0.3404 | ±0.6808 | -0.048 | 0.9617 |  |
| **Age (years)** | **-0.0412** | 0.0124 | ±0.0247 | **-3.330** | **8.69e-04** | *** |
| BMI (kg/m2) | -0.0313 | 0.0171 | ±0.0342 | -1.828 | 0.0675 | . |
| Hypertension | -0.4912 | 0.2875 | ±0.5751 | -1.708 | 0.0876 | . |
| High cholesterol | -0.1258 | 0.2720 | ±0.5441 | -0.462 | 0.6438 |  |
| Kidney disease | -0.0697 | 0.6889 | ±1.3779 | -0.101 | 0.9194 |  |
| Circulatory disease | -0.2172 | 0.4119 | ±0.8239 | -0.527 | 0.5980 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0108 | 0.0131 | ±0.0263 | -0.824 | 0.4097 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **454**, R² = **0.0873**, Adj R² = **0.0646**, F-statistic = **3.84** (p = **2.61e-05**), Residual SE = **2.579** on **442** df, AIC = **2160.5**, BIC = **2209.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4184** | 1.2595 | ±2.5189 | **+13.036** | **7.65e-39** | *** |
| Education: graduate level (vs college) | +0.3113 | 0.2600 | ±0.5200 | +1.197 | 0.2312 |  |
| **Education: high school or below (vs college)** | **-1.1915** | 0.5945 | ±1.1890 | **-2.004** | **0.0451** | * |
| Site: UCSD (vs UAB) | -0.1765 | 0.3172 | ±0.6343 | -0.556 | 0.5780 |  |
| Site: UW (vs UAB) | -0.0372 | 0.3394 | ±0.6788 | -0.110 | 0.9128 |  |
| **Age (years)** | **-0.0398** | 0.0125 | ±0.0250 | **-3.179** | **0.0015** | ** |
| **BMI (kg/m2)** | **-0.0336** | 0.0170 | ±0.0339 | **-1.982** | **0.0475** | * |
| Hypertension | -0.5050 | 0.2859 | ±0.5717 | -1.767 | 0.0773 | . |
| High cholesterol | -0.1217 | 0.2719 | ±0.5439 | -0.448 | 0.6544 |  |
| Kidney disease | -0.0645 | 0.6921 | ±1.3841 | -0.093 | 0.9257 |  |
| Circulatory disease | -0.2211 | 0.4126 | ±0.8253 | -0.536 | 0.5920 |  |
| Glucose SD, pooled (mg/dL) | +0.0020 | 0.0477 | ±0.0953 | +0.042 | 0.9663 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **454**, R² = **0.0885**, Adj R² = **0.0658**, F-statistic = **3.90** (p = **2.08e-05**), Residual SE = **2.577** on **442** df, AIC = **2159.9**, BIC = **2209.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.8812** | 1.2240 | ±2.4479 | **+12.975** | **1.69e-38** | *** |
| Education: graduate level (vs college) | +0.3250 | 0.2601 | ±0.5202 | +1.249 | 0.2116 |  |
| **Education: high school or below (vs college)** | **-1.1895** | 0.5963 | ±1.1925 | **-1.995** | **0.0461** | * |
| Site: UCSD (vs UAB) | -0.1677 | 0.3174 | ±0.6347 | -0.529 | 0.5971 |  |
| Site: UW (vs UAB) | -0.0265 | 0.3390 | ±0.6780 | -0.078 | 0.9377 |  |
| **Age (years)** | **-0.0400** | 0.0125 | ±0.0251 | **-3.196** | **0.0014** | ** |
| **BMI (kg/m2)** | **-0.0345** | 0.0169 | ±0.0339 | **-2.040** | **0.0414** | * |
| Hypertension | -0.5126 | 0.2864 | ±0.5727 | -1.790 | 0.0735 | . |
| High cholesterol | -0.1112 | 0.2723 | ±0.5447 | -0.408 | 0.6829 |  |
| Kidney disease | -0.1001 | 0.6900 | ±1.3800 | -0.145 | 0.8846 |  |
| Circulatory disease | -0.2243 | 0.4164 | ±0.8328 | -0.539 | 0.5901 |  |
| Avg. daily SD (mg/dL) | +0.0390 | 0.0472 | ±0.0943 | +0.828 | 0.4077 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **454**, R² = **0.0876**, Adj R² = **0.0649**, F-statistic = **3.86** (p = **2.49e-05**), Residual SE = **2.579** on **442** df, AIC = **2160.4**, BIC = **2209.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1594** | 1.2981 | ±2.5962 | **+12.448** | **1.43e-35** | *** |
| Education: graduate level (vs college) | +0.3170 | 0.2599 | ±0.5198 | +1.220 | 0.2226 |  |
| **Education: high school or below (vs college)** | **-1.1949** | 0.5952 | ±1.1905 | **-2.007** | **0.0447** | * |
| Site: UCSD (vs UAB) | -0.1697 | 0.3174 | ±0.6348 | -0.535 | 0.5929 |  |
| Site: UW (vs UAB) | -0.0291 | 0.3391 | ±0.6781 | -0.086 | 0.9316 |  |
| **Age (years)** | **-0.0399** | 0.0125 | ±0.0250 | **-3.187** | **0.0014** | ** |
| **BMI (kg/m2)** | **-0.0336** | 0.0169 | ±0.0338 | **-1.990** | **0.0465** | * |
| Hypertension | -0.5076 | 0.2863 | ±0.5726 | -1.773 | 0.0762 | . |
| High cholesterol | -0.1184 | 0.2718 | ±0.5436 | -0.436 | 0.6631 |  |
| Kidney disease | -0.0771 | 0.6901 | ±1.3803 | -0.112 | 0.9110 |  |
| Circulatory disease | -0.2238 | 0.4141 | ±0.8282 | -0.541 | 0.5888 |  |
| CV (%) | +0.0199 | 0.0549 | ±0.1098 | +0.362 | 0.7171 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **454**, R² = **0.0875**, Adj R² = **0.0648**, F-statistic = **3.85** (p = **2.51e-05**), Residual SE = **2.579** on **442** df, AIC = **2160.4**, BIC = **2209.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.7049** | 1.3342 | ±2.6685 | **+12.520** | **5.78e-36** | *** |
| Education: graduate level (vs college) | +0.3172 | 0.2602 | ±0.5204 | +1.219 | 0.2228 |  |
| **Education: high school or below (vs college)** | **-1.1951** | 0.5950 | ±1.1899 | **-2.009** | **0.0446** | * |
| Site: UCSD (vs UAB) | -0.1720 | 0.3171 | ±0.6341 | -0.543 | 0.5874 |  |
| Site: UW (vs UAB) | -0.0315 | 0.3389 | ±0.6778 | -0.093 | 0.9260 |  |
| **Age (years)** | **-0.0399** | 0.0125 | ±0.0250 | **-3.185** | **0.0014** | ** |
| **BMI (kg/m2)** | **-0.0336** | 0.0169 | ±0.0338 | **-1.988** | **0.0468** | * |
| Hypertension | -0.5075 | 0.2863 | ±0.5725 | -1.773 | 0.0762 | . |
| High cholesterol | -0.1183 | 0.2716 | ±0.5432 | -0.436 | 0.6632 |  |
| Kidney disease | -0.0725 | 0.6886 | ±1.3772 | -0.105 | 0.9162 |  |
| Circulatory disease | -0.2223 | 0.4142 | ±0.8284 | -0.537 | 0.5914 |  |
| Mean / SD ratio | -0.0367 | 0.1100 | ±0.2201 | -0.334 | 0.7387 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **454**, R² = **0.0884**, Adj R² = **0.0657**, F-statistic = **3.90** (p = **2.13e-05**), Residual SE = **2.578** on **442** df, AIC = **2160.0**, BIC = **2209.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9782** | 1.2565 | ±2.5131 | **+13.512** | **1.33e-41** | *** |
| Education: graduate level (vs college) | +0.3261 | 0.2603 | ±0.5206 | +1.253 | 0.2102 |  |
| **Education: high school or below (vs college)** | **-1.1960** | 0.5956 | ±1.1911 | **-2.008** | **0.0446** | * |
| Site: UCSD (vs UAB) | -0.1679 | 0.3180 | ±0.6359 | -0.528 | 0.5974 |  |
| Site: UW (vs UAB) | -0.0253 | 0.3395 | ±0.6790 | -0.075 | 0.9405 |  |
| **Age (years)** | **-0.0401** | 0.0125 | ±0.0250 | **-3.207** | **0.0013** | ** |
| **BMI (kg/m2)** | **-0.0341** | 0.0169 | ±0.0338 | **-2.019** | **0.0435** | * |
| Hypertension | -0.5068 | 0.2868 | ±0.5736 | -1.767 | 0.0772 | . |
| High cholesterol | -0.1157 | 0.2721 | ±0.5442 | -0.425 | 0.6707 |  |
| Kidney disease | -0.0854 | 0.6874 | ±1.3748 | -0.124 | 0.9011 |  |
| Circulatory disease | -0.2160 | 0.4157 | ±0.8314 | -0.520 | 0.6033 |  |
| Avg. daily mean/SD | -0.0646 | 0.0862 | ±0.1724 | -0.750 | 0.4536 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **454**, R² = **0.0880**, Adj R² = **0.0653**, F-statistic = **3.88** (p = **2.31e-05**), Residual SE = **2.578** on **442** df, AIC = **2160.2**, BIC = **2209.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9014** | 1.2565 | ±2.5130 | **+13.451** | **3.03e-41** | *** |
| Education: graduate level (vs college) | +0.3108 | 0.2594 | ±0.5188 | +1.198 | 0.2309 |  |
| **Education: high school or below (vs college)** | **-1.1728** | 0.5892 | ±1.1785 | **-1.990** | **0.0465** | * |
| Site: UCSD (vs UAB) | -0.1817 | 0.3177 | ±0.6354 | -0.572 | 0.5674 |  |
| Site: UW (vs UAB) | -0.0538 | 0.3408 | ±0.6816 | -0.158 | 0.8746 |  |
| **Age (years)** | **-0.0403** | 0.0125 | ±0.0249 | **-3.234** | **0.0012** | ** |
| **BMI (kg/m2)** | **-0.0341** | 0.0168 | ±0.0336 | **-2.025** | **0.0429** | * |
| Hypertension | -0.5091 | 0.2872 | ±0.5745 | -1.772 | 0.0763 | . |
| High cholesterol | -0.1178 | 0.2713 | ±0.5426 | -0.434 | 0.6640 |  |
| Kidney disease | -0.0488 | 0.6889 | ±1.3778 | -0.071 | 0.9435 |  |
| Circulatory disease | -0.2277 | 0.4122 | ±0.8243 | -0.552 | 0.5807 |  |
| MAG (mg/dL/h) | -0.0117 | 0.0219 | ±0.0438 | -0.533 | 0.5942 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **454**, R² = **0.0876**, Adj R² = **0.0649**, F-statistic = **3.86** (p = **2.47e-05**), Residual SE = **2.579** on **442** df, AIC = **2160.3**, BIC = **2209.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.1107** | 1.2429 | ±2.4858 | **+12.962** | **2.01e-38** | *** |
| Education: graduate level (vs college) | +0.3149 | 0.2601 | ±0.5202 | +1.211 | 0.2261 |  |
| **Education: high school or below (vs college)** | **-1.1919** | 0.5963 | ±1.1927 | **-1.999** | **0.0456** | * |
| Site: UCSD (vs UAB) | -0.1724 | 0.3168 | ±0.6335 | -0.544 | 0.5864 |  |
| Site: UW (vs UAB) | -0.0318 | 0.3392 | ±0.6784 | -0.094 | 0.9254 |  |
| **Age (years)** | **-0.0399** | 0.0125 | ±0.0250 | **-3.185** | **0.0014** | ** |
| **BMI (kg/m2)** | **-0.0331** | 0.0168 | ±0.0336 | **-1.969** | **0.0490** | * |
| Hypertension | -0.5017 | 0.2868 | ±0.5736 | -1.749 | 0.0802 | . |
| High cholesterol | -0.1219 | 0.2710 | ±0.5420 | -0.450 | 0.6528 |  |
| Kidney disease | -0.0732 | 0.6886 | ±1.3771 | -0.106 | 0.9153 |  |
| Circulatory disease | -0.2208 | 0.4139 | ±0.8279 | -0.534 | 0.5937 |  |
| Avg. daily range (mg/dL) | +0.0041 | 0.0103 | ±0.0205 | +0.399 | 0.6898 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **454**, R² = **0.1029**, Adj R² = **0.0805**, F-statistic = **4.61** (p = **1.18e-06**), Residual SE = **2.557** on **442** df, AIC = **2152.7**, BIC = **2202.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.3549** | 1.0504 | ±2.1007 | **+16.523** | **2.51e-61** | *** |
| Education: graduate level (vs college) | +0.3304 | 0.2576 | ±0.5152 | +1.283 | 0.1997 |  |
| Education: high school or below (vs college) | -1.1100 | 0.5813 | ±1.1625 | -1.910 | 0.0562 | . |
| Site: UCSD (vs UAB) | -0.2116 | 0.3126 | ±0.6252 | -0.677 | 0.4986 |  |
| Site: UW (vs UAB) | -0.0245 | 0.3363 | ±0.6726 | -0.073 | 0.9419 |  |
| **Age (years)** | **-0.0405** | 0.0123 | ±0.0246 | **-3.292** | **9.93e-04** | *** |
| BMI (kg/m2) | -0.0330 | 0.0169 | ±0.0338 | -1.950 | 0.0511 | . |
| Hypertension | -0.4435 | 0.2894 | ±0.5788 | -1.532 | 0.1254 |  |
| High cholesterol | -0.0936 | 0.2695 | ±0.5390 | -0.347 | 0.7285 |  |
| Kidney disease | -0.0596 | 0.6766 | ±1.3531 | -0.088 | 0.9298 |  |
| Circulatory disease | -0.1397 | 0.4060 | ±0.8121 | -0.344 | 0.7308 |  |
| **SD of daily means (mg/dL)** | **-0.1806** | 0.0676 | ±0.1351 | **-2.674** | **0.0075** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **454**, R² = **0.0874**, Adj R² = **0.0647**, F-statistic = **3.85** (p = **2.55e-05**), Residual SE = **2.579** on **442** df, AIC = **2160.4**, BIC = **2209.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +26.2440 | 40.3750 | ±80.7499 | +0.650 | 0.5157 |  |
| Education: graduate level (vs college) | +0.3130 | 0.2599 | ±0.5199 | +1.204 | 0.2286 |  |
| **Education: high school or below (vs college)** | **-1.1891** | 0.5949 | ±1.1897 | **-1.999** | **0.0456** | * |
| Site: UCSD (vs UAB) | -0.1735 | 0.3145 | ±0.6289 | -0.552 | 0.5811 |  |
| Site: UW (vs UAB) | -0.0347 | 0.3383 | ±0.6766 | -0.103 | 0.9183 |  |
| **Age (years)** | **-0.0397** | 0.0124 | ±0.0249 | **-3.191** | **0.0014** | ** |
| **BMI (kg/m2)** | **-0.0334** | 0.0168 | ±0.0336 | **-1.988** | **0.0468** | * |
| Hypertension | -0.5057 | 0.2870 | ±0.5740 | -1.762 | 0.0781 | . |
| High cholesterol | -0.1243 | 0.2714 | ±0.5429 | -0.458 | 0.6471 |  |
| Kidney disease | -0.0703 | 0.6871 | ±1.3742 | -0.102 | 0.9185 |  |
| Circulatory disease | -0.2192 | 0.4140 | ±0.8280 | -0.529 | 0.5965 |  |
| Time in range 70-180, pooled (%) | -0.0985 | 0.4032 | ±0.8065 | -0.244 | 0.8070 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **454**, R² = **0.0887**, Adj R² = **0.0660**, F-statistic = **3.91** (p = **2.02e-05**), Residual SE = **2.577** on **442** df, AIC = **2159.8**, BIC = **2209.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +47.9059 | 37.3740 | ±74.7480 | +1.282 | 0.1999 |  |
| Education: graduate level (vs college) | +0.3201 | 0.2604 | ±0.5208 | +1.229 | 0.2189 |  |
| **Education: high school or below (vs college)** | **-1.1820** | 0.5947 | ±1.1894 | **-1.988** | **0.0469** | * |
| Site: UCSD (vs UAB) | -0.1746 | 0.3178 | ±0.6356 | -0.549 | 0.5827 |  |
| Site: UW (vs UAB) | -0.0384 | 0.3418 | ±0.6836 | -0.112 | 0.9105 |  |
| **Age (years)** | **-0.0395** | 0.0124 | ±0.0248 | **-3.184** | **0.0015** | ** |
| **BMI (kg/m2)** | **-0.0333** | 0.0169 | ±0.0338 | **-1.972** | **0.0486** | * |
| Hypertension | -0.4975 | 0.2858 | ±0.5717 | -1.741 | 0.0818 | . |
| High cholesterol | -0.1330 | 0.2714 | ±0.5427 | -0.490 | 0.6241 |  |
| Kidney disease | -0.0739 | 0.6921 | ±1.3843 | -0.107 | 0.9149 |  |
| Circulatory disease | -0.2246 | 0.4140 | ±0.8279 | -0.543 | 0.5874 |  |
| Avg. daily time in range 70-180 (%) | -0.3160 | 0.3730 | ±0.7459 | -0.847 | 0.3968 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **454**, R² = **0.0873**, Adj R² = **0.0646**, F-statistic = **3.85** (p = **2.60e-05**), Residual SE = **2.579** on **442** df, AIC = **2160.5**, BIC = **2209.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4423** | 1.0364 | ±2.0727 | **+15.865** | **1.10e-56** | *** |
| Education: graduate level (vs college) | +0.3110 | 0.2601 | ±0.5202 | +1.196 | 0.2317 |  |
| **Education: high school or below (vs college)** | **-1.1893** | 0.5918 | ±1.1835 | **-2.010** | **0.0444** | * |
| Site: UCSD (vs UAB) | -0.1718 | 0.3150 | ±0.6300 | -0.545 | 0.5855 |  |
| Site: UW (vs UAB) | -0.0348 | 0.3360 | ±0.6720 | -0.103 | 0.9176 |  |
| **Age (years)** | **-0.0398** | 0.0125 | ±0.0250 | **-3.185** | **0.0014** | ** |
| **BMI (kg/m2)** | **-0.0336** | 0.0169 | ±0.0339 | **-1.982** | **0.0475** | * |
| Hypertension | -0.5061 | 0.2854 | ±0.5707 | -1.774 | 0.0761 | . |
| High cholesterol | -0.1225 | 0.2715 | ±0.5429 | -0.451 | 0.6519 |  |
| Kidney disease | -0.0588 | 0.6948 | ±1.3896 | -0.085 | 0.9325 |  |
| Circulatory disease | -0.2216 | 0.4130 | ±0.8259 | -0.537 | 0.5916 |  |
| Any reading < 54 during wear (0/1) | +0.0330 | 0.3770 | ±0.7540 | +0.087 | 0.9303 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **454**, R² = **0.0874**, Adj R² = **0.0646**, F-statistic = **3.85** (p = **2.60e-05**), Residual SE = **2.579** on **442** df, AIC = **2160.5**, BIC = **2209.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4425** | 1.0386 | ±2.0773 | **+15.831** | **1.91e-56** | *** |
| Education: graduate level (vs college) | +0.3110 | 0.2597 | ±0.5194 | +1.197 | 0.2311 |  |
| **Education: high school or below (vs college)** | **-1.1870** | 0.5935 | ±1.1870 | **-2.000** | **0.0455** | * |
| Site: UCSD (vs UAB) | -0.1715 | 0.3155 | ±0.6310 | -0.544 | 0.5867 |  |
| Site: UW (vs UAB) | -0.0352 | 0.3384 | ±0.6768 | -0.104 | 0.9173 |  |
| **Age (years)** | **-0.0397** | 0.0125 | ±0.0249 | **-3.184** | **0.0015** | ** |
| **BMI (kg/m2)** | **-0.0338** | 0.0171 | ±0.0343 | **-1.971** | **0.0488** | * |
| Hypertension | -0.5076 | 0.2877 | ±0.5755 | -1.764 | 0.0777 | . |
| High cholesterol | -0.1213 | 0.2699 | ±0.5397 | -0.450 | 0.6530 |  |
| Kidney disease | -0.0589 | 0.6894 | ±1.3787 | -0.085 | 0.9319 |  |
| Circulatory disease | -0.2230 | 0.4126 | ±0.8252 | -0.541 | 0.5888 |  |
| Time < 54 (%) | +0.3076 | 2.2098 | ±4.4195 | +0.139 | 0.8893 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **454**, R² = **0.0885**, Adj R² = **0.0658**, F-statistic = **3.90** (p = **2.08e-05**), Residual SE = **2.577** on **442** df, AIC = **2159.9**, BIC = **2209.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4304** | 1.0475 | ±2.0949 | **+15.686** | **1.88e-55** | *** |
| Education: graduate level (vs college) | +0.3123 | 0.2600 | ±0.5199 | +1.201 | 0.2297 |  |
| **Education: high school or below (vs college)** | **-1.1789** | 0.5918 | ±1.1835 | **-1.992** | **0.0464** | * |
| Site: UCSD (vs UAB) | -0.1635 | 0.3175 | ±0.6350 | -0.515 | 0.6066 |  |
| Site: UW (vs UAB) | -0.0356 | 0.3412 | ±0.6825 | -0.104 | 0.9169 |  |
| **Age (years)** | **-0.0397** | 0.0125 | ±0.0250 | **-3.174** | **0.0015** | ** |
| **BMI (kg/m2)** | **-0.0340** | 0.0171 | ±0.0341 | **-1.996** | **0.0460** | * |
| Hypertension | -0.5100 | 0.2860 | ±0.5720 | -1.783 | 0.0745 | . |
| High cholesterol | -0.1225 | 0.2710 | ±0.5419 | -0.452 | 0.6513 |  |
| Kidney disease | -0.0473 | 0.6915 | ±1.3831 | -0.068 | 0.9455 |  |
| Circulatory disease | -0.2434 | 0.4106 | ±0.8213 | -0.593 | 0.5534 |  |
| Avg. daily time < 54 (%) | +2.3035 | 2.9350 | ±5.8701 | +0.785 | 0.4326 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **454**, R² = **0.0880**, Adj R² = **0.0653**, F-statistic = **3.88** (p = **2.30e-05**), Residual SE = **2.578** on **442** df, AIC = **2160.2**, BIC = **2209.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.5157** | 1.0401 | ±2.0803 | **+15.878** | **8.97e-57** | *** |
| Education: graduate level (vs college) | +0.3045 | 0.2597 | ±0.5194 | +1.173 | 0.2409 |  |
| **Education: high school or below (vs college)** | **-1.1766** | 0.5963 | ±1.1925 | **-1.973** | **0.0485** | * |
| Site: UCSD (vs UAB) | -0.1862 | 0.3151 | ±0.6302 | -0.591 | 0.5546 |  |
| Site: UW (vs UAB) | -0.0508 | 0.3357 | ±0.6715 | -0.151 | 0.8797 |  |
| **Age (years)** | **-0.0398** | 0.0125 | ±0.0251 | **-3.179** | **0.0015** | ** |
| **BMI (kg/m2)** | **-0.0336** | 0.0169 | ±0.0338 | **-1.992** | **0.0464** | * |
| Hypertension | -0.5137 | 0.2854 | ±0.5708 | -1.800 | 0.0719 | . |
| High cholesterol | -0.1079 | 0.2703 | ±0.5406 | -0.399 | 0.6897 |  |
| Kidney disease | -0.0809 | 0.6873 | ±1.3746 | -0.118 | 0.9063 |  |
| Circulatory disease | -0.2255 | 0.4137 | ±0.8274 | -0.545 | 0.5857 |  |
| Time 54-69, pooled (%) | -0.3818 | 0.7454 | ±1.4908 | -0.512 | 0.6085 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **454**, R² = **0.0874**, Adj R² = **0.0647**, F-statistic = **3.85** (p = **2.56e-05**), Residual SE = **2.579** on **442** df, AIC = **2160.4**, BIC = **2209.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4326** | 1.0426 | ±2.0852 | **+15.761** | **5.77e-56** | *** |
| Education: graduate level (vs college) | +0.3143 | 0.2603 | ±0.5206 | +1.208 | 0.2272 |  |
| **Education: high school or below (vs college)** | **-1.1968** | 0.5951 | ±1.1902 | **-2.011** | **0.0443** | * |
| Site: UCSD (vs UAB) | -0.1758 | 0.3174 | ±0.6348 | -0.554 | 0.5796 |  |
| Site: UW (vs UAB) | -0.0355 | 0.3390 | ±0.6779 | -0.105 | 0.9167 |  |
| **Age (years)** | **-0.0398** | 0.0125 | ±0.0251 | **-3.181** | **0.0015** | ** |
| **BMI (kg/m2)** | **-0.0336** | 0.0169 | ±0.0338 | **-1.983** | **0.0474** | * |
| Hypertension | -0.4972 | 0.2847 | ±0.5693 | -1.747 | 0.0807 | . |
| High cholesterol | -0.1273 | 0.2706 | ±0.5413 | -0.470 | 0.6382 |  |
| Kidney disease | -0.0559 | 0.6908 | ±1.3815 | -0.081 | 0.9355 |  |
| Circulatory disease | -0.2212 | 0.4131 | ±0.8262 | -0.535 | 0.5924 |  |
| Avg. daily time 54-69 (%) | +0.1514 | 0.6978 | ±1.3956 | +0.217 | 0.8282 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **454**, R² = **0.0878**, Adj R² = **0.0651**, F-statistic = **3.87** (p = **2.39e-05**), Residual SE = **2.578** on **442** df, AIC = **2160.3**, BIC = **2209.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.5071** | 1.0372 | ±2.0743 | **+15.915** | **4.95e-57** | *** |
| Education: graduate level (vs college) | +0.3058 | 0.2598 | ±0.5197 | +1.177 | 0.2392 |  |
| **Education: high school or below (vs college)** | **-1.1844** | 0.5961 | ±1.1923 | **-1.987** | **0.0470** | * |
| Site: UCSD (vs UAB) | -0.1889 | 0.3137 | ±0.6274 | -0.602 | 0.5472 |  |
| Site: UW (vs UAB) | -0.0499 | 0.3350 | ±0.6701 | -0.149 | 0.8817 |  |
| **Age (years)** | **-0.0399** | 0.0125 | ±0.0250 | **-3.189** | **0.0014** | ** |
| **BMI (kg/m2)** | **-0.0334** | 0.0169 | ±0.0338 | **-1.978** | **0.0479** | * |
| Hypertension | -0.5083 | 0.2860 | ±0.5720 | -1.777 | 0.0755 | . |
| High cholesterol | -0.1127 | 0.2711 | ±0.5422 | -0.416 | 0.6777 |  |
| Kidney disease | -0.0793 | 0.6883 | ±1.3766 | -0.115 | 0.9082 |  |
| Circulatory disease | -0.2220 | 0.4142 | ±0.8285 | -0.536 | 0.5920 |  |
| Time < 70 (%) | -0.2815 | 0.6538 | ±1.3077 | -0.431 | 0.6668 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **454**, R² = **0.0876**, Adj R² = **0.0649**, F-statistic = **3.86** (p = **2.49e-05**), Residual SE = **2.579** on **442** df, AIC = **2160.4**, BIC = **2209.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4216** | 1.0437 | ±2.0873 | **+15.735** | **8.75e-56** | *** |
| Education: graduate level (vs college) | +0.3163 | 0.2605 | ±0.5210 | +1.214 | 0.2247 |  |
| **Education: high school or below (vs college)** | **-1.1982** | 0.5941 | ±1.1882 | **-2.017** | **0.0437** | * |
| Site: UCSD (vs UAB) | -0.1739 | 0.3171 | ±0.6341 | -0.549 | 0.5833 |  |
| Site: UW (vs UAB) | -0.0341 | 0.3394 | ±0.6789 | -0.100 | 0.9200 |  |
| **Age (years)** | **-0.0399** | 0.0125 | ±0.0250 | **-3.184** | **0.0015** | ** |
| **BMI (kg/m2)** | **-0.0336** | 0.0169 | ±0.0339 | **-1.983** | **0.0474** | * |
| Hypertension | -0.4943 | 0.2852 | ±0.5705 | -1.733 | 0.0831 | . |
| High cholesterol | -0.1296 | 0.2712 | ±0.5424 | -0.478 | 0.6327 |  |
| Kidney disease | -0.0513 | 0.6921 | ±1.3843 | -0.074 | 0.9409 |  |
| Circulatory disease | -0.2237 | 0.4131 | ±0.8262 | -0.541 | 0.5882 |  |
| Avg. daily time < 70 (%) | +0.2234 | 0.6440 | ±1.2880 | +0.347 | 0.7286 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **454**, R² = **0.0876**, Adj R² = **0.0649**, F-statistic = **3.86** (p = **2.49e-05**), Residual SE = **2.579** on **442** df, AIC = **2160.4**, BIC = **2209.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -62.8546 | 284.5178 | ±569.0356 | -0.221 | 0.8252 |  |
| Education: graduate level (vs college) | +0.3097 | 0.2602 | ±0.5204 | +1.190 | 0.2340 |  |
| **Education: high school or below (vs college)** | **-1.2027** | 0.5951 | ±1.1902 | **-2.021** | **0.0433** | * |
| Site: UCSD (vs UAB) | -0.1923 | 0.3122 | ±0.6244 | -0.616 | 0.5378 |  |
| Site: UW (vs UAB) | -0.0456 | 0.3358 | ±0.6716 | -0.136 | 0.8920 |  |
| **Age (years)** | **-0.0401** | 0.0124 | ±0.0249 | **-3.226** | **0.0013** | ** |
| BMI (kg/m2) | -0.0331 | 0.0172 | ±0.0343 | -1.931 | 0.0535 | . |
| Hypertension | -0.4964 | 0.2892 | ±0.5784 | -1.716 | 0.0861 | . |
| High cholesterol | -0.1248 | 0.2698 | ±0.5395 | -0.463 | 0.6437 |  |
| Kidney disease | -0.0717 | 0.6889 | ±1.3778 | -0.104 | 0.9172 |  |
| Circulatory disease | -0.2143 | 0.4134 | ±0.8268 | -0.518 | 0.6043 |  |
| Time 54-250, pooled (%) | +0.7933 | 2.8439 | ±5.6878 | +0.279 | 0.7803 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **454**, R² = **0.0873**, Adj R² = **0.0646**, F-statistic = **3.84** (p = **2.61e-05**), Residual SE = **2.579** on **442** df, AIC = **2160.5**, BIC = **2209.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +33.6206 | 322.9269 | ±645.8538 | +0.104 | 0.9171 |  |
| Education: graduate level (vs college) | +0.3107 | 0.2601 | ±0.5202 | +1.195 | 0.2323 |  |
| **Education: high school or below (vs college)** | **-1.1902** | 0.5936 | ±1.1872 | **-2.005** | **0.0450** | * |
| Site: UCSD (vs UAB) | -0.1758 | 0.3151 | ±0.6303 | -0.558 | 0.5769 |  |
| Site: UW (vs UAB) | -0.0375 | 0.3401 | ±0.6802 | -0.110 | 0.9122 |  |
| **Age (years)** | **-0.0398** | 0.0125 | ±0.0250 | **-3.185** | **0.0014** | ** |
| **BMI (kg/m2)** | **-0.0336** | 0.0170 | ±0.0340 | **-1.977** | **0.0481** | * |
| Hypertension | -0.5047 | 0.2866 | ±0.5732 | -1.761 | 0.0782 | . |
| High cholesterol | -0.1224 | 0.2712 | ±0.5424 | -0.451 | 0.6517 |  |
| Kidney disease | -0.0614 | 0.6895 | ±1.3789 | -0.089 | 0.9291 |  |
| Circulatory disease | -0.2223 | 0.4111 | ±0.8222 | -0.541 | 0.5887 |  |
| Avg. daily time 54-250 (%) | -0.1717 | 3.2279 | ±6.4558 | -0.053 | 0.9576 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **454**, R² = **0.0883**, Adj R² = **0.0656**, F-statistic = **3.89** (p = **2.15e-05**), Residual SE = **2.578** on **442** df, AIC = **2160.0**, BIC = **2209.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3366** | 1.0285 | ±2.0571 | **+15.883** | **8.26e-57** | *** |
| Education: graduate level (vs college) | +0.3127 | 0.2589 | ±0.5177 | +1.208 | 0.2271 |  |
| **Education: high school or below (vs college)** | **-1.1774** | 0.5965 | ±1.1931 | **-1.974** | **0.0484** | * |
| Site: UCSD (vs UAB) | -0.1793 | 0.3182 | ±0.6364 | -0.563 | 0.5731 |  |
| Site: UW (vs UAB) | -0.0414 | 0.3407 | ±0.6815 | -0.122 | 0.9032 |  |
| **Age (years)** | **-0.0397** | 0.0124 | ±0.0249 | **-3.191** | **0.0014** | ** |
| BMI (kg/m2) | -0.0328 | 0.0168 | ±0.0335 | -1.957 | 0.0504 | . |
| Hypertension | -0.5129 | 0.2864 | ±0.5727 | -1.791 | 0.0733 | . |
| High cholesterol | -0.1177 | 0.2704 | ±0.5409 | -0.435 | 0.6634 |  |
| Kidney disease | -0.1048 | 0.6895 | ±1.3789 | -0.152 | 0.8792 |  |
| Circulatory disease | -0.2178 | 0.4155 | ±0.8309 | -0.524 | 0.6002 |  |
| Time 181-250, pooled (%) | +0.3045 | 0.4214 | ±0.8428 | +0.722 | 0.4700 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **454**, R² = **0.0885**, Adj R² = **0.0658**, F-statistic = **3.90** (p = **2.10e-05**), Residual SE = **2.577** on **442** df, AIC = **2159.9**, BIC = **2209.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3438** | 1.0334 | ±2.0668 | **+15.816** | **2.43e-56** | *** |
| Education: graduate level (vs college) | +0.3122 | 0.2589 | ±0.5178 | +1.206 | 0.2280 |  |
| Education: high school or below (vs college) | -1.1720 | 0.5985 | ±1.1969 | -1.958 | 0.0502 | . |
| Site: UCSD (vs UAB) | -0.1795 | 0.3185 | ±0.6370 | -0.564 | 0.5730 |  |
| Site: UW (vs UAB) | -0.0442 | 0.3416 | ±0.6832 | -0.129 | 0.8971 |  |
| **Age (years)** | **-0.0395** | 0.0124 | ±0.0249 | **-3.175** | **0.0015** | ** |
| **BMI (kg/m2)** | **-0.0333** | 0.0169 | ±0.0337 | **-1.973** | **0.0486** | * |
| Hypertension | -0.5121 | 0.2869 | ±0.5738 | -1.785 | 0.0743 | . |
| High cholesterol | -0.1226 | 0.2708 | ±0.5415 | -0.453 | 0.6507 |  |
| Kidney disease | -0.0902 | 0.6902 | ±1.3803 | -0.131 | 0.8960 |  |
| Circulatory disease | -0.2202 | 0.4150 | ±0.8300 | -0.531 | 0.5956 |  |
| Avg. daily time 181-250 (%) | +0.3221 | 0.4239 | ±0.8477 | +0.760 | 0.4473 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **454**, R² = **0.0881**, Adj R² = **0.0654**, F-statistic = **3.88** (p = **2.26e-05**), Residual SE = **2.578** on **442** df, AIC = **2160.1**, BIC = **2209.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3504** | 1.0259 | ±2.0519 | **+15.937** | **3.50e-57** | *** |
| Education: graduate level (vs college) | +0.3124 | 0.2591 | ±0.5181 | +1.206 | 0.2278 |  |
| **Education: high school or below (vs college)** | **-1.1792** | 0.5963 | ±1.1927 | **-1.977** | **0.0480** | * |
| Site: UCSD (vs UAB) | -0.1786 | 0.3183 | ±0.6366 | -0.561 | 0.5746 |  |
| Site: UW (vs UAB) | -0.0407 | 0.3410 | ±0.6820 | -0.119 | 0.9050 |  |
| **Age (years)** | **-0.0397** | 0.0124 | ±0.0249 | **-3.190** | **0.0014** | ** |
| **BMI (kg/m2)** | **-0.0329** | 0.0168 | ±0.0335 | **-1.963** | **0.0496** | * |
| Hypertension | -0.5116 | 0.2864 | ±0.5729 | -1.786 | 0.0741 | . |
| High cholesterol | -0.1184 | 0.2704 | ±0.5408 | -0.438 | 0.6615 |  |
| Kidney disease | -0.0991 | 0.6893 | ±1.3786 | -0.144 | 0.8857 |  |
| Circulatory disease | -0.2182 | 0.4153 | ±0.8305 | -0.525 | 0.5993 |  |
| Time > 180 (%) | +0.2634 | 0.4268 | ±0.8536 | +0.617 | 0.5372 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **454**, R² = **0.0882**, Adj R² = **0.0655**, F-statistic = **3.89** (p = **2.22e-05**), Residual SE = **2.578** on **442** df, AIC = **2160.1**, BIC = **2209.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.3567** | 1.0309 | ±2.0618 | **+15.866** | **1.08e-56** | *** |
| Education: graduate level (vs college) | +0.3119 | 0.2591 | ±0.5182 | +1.204 | 0.2287 |  |
| **Education: high school or below (vs college)** | **-1.1745** | 0.5981 | ±1.1962 | **-1.964** | **0.0496** | * |
| Site: UCSD (vs UAB) | -0.1788 | 0.3186 | ±0.6373 | -0.561 | 0.5747 |  |
| Site: UW (vs UAB) | -0.0430 | 0.3420 | ±0.6840 | -0.126 | 0.8999 |  |
| **Age (years)** | **-0.0395** | 0.0124 | ±0.0249 | **-3.177** | **0.0015** | ** |
| **BMI (kg/m2)** | **-0.0333** | 0.0169 | ±0.0337 | **-1.974** | **0.0483** | * |
| Hypertension | -0.5108 | 0.2870 | ±0.5739 | -1.780 | 0.0751 | . |
| High cholesterol | -0.1227 | 0.2708 | ±0.5416 | -0.453 | 0.6506 |  |
| Kidney disease | -0.0864 | 0.6897 | ±1.3794 | -0.125 | 0.9003 |  |
| Circulatory disease | -0.2203 | 0.4148 | ±0.8296 | -0.531 | 0.5954 |  |
| Avg. daily time > 180 (%) | +0.2773 | 0.4316 | ±0.8632 | +0.643 | 0.5205 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 454)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **454**, R² = **0.0875**, Adj R² = **0.0648**, F-statistic = **3.85** (p = **2.53e-05**), Residual SE = **2.579** on **442** df, AIC = **2160.4**, BIC = **2209.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.4220** | 1.0559 | ±2.1118 | **+15.553** | **1.53e-54** | *** |
| Education: graduate level (vs college) | +0.3150 | 0.2606 | ±0.5212 | +1.209 | 0.2267 |  |
| **Education: high school or below (vs college)** | **-1.1897** | 0.5933 | ±1.1865 | **-2.005** | **0.0449** | * |
| Site: UCSD (vs UAB) | -0.1773 | 0.3175 | ±0.6349 | -0.559 | 0.5764 |  |
| Site: UW (vs UAB) | -0.0413 | 0.3387 | ±0.6773 | -0.122 | 0.9029 |  |
| **Age (years)** | **-0.0393** | 0.0126 | ±0.0252 | **-3.121** | **0.0018** | ** |
| **BMI (kg/m2)** | **-0.0339** | 0.0169 | ±0.0337 | **-2.013** | **0.0441** | * |
| Hypertension | -0.5112 | 0.2881 | ±0.5763 | -1.774 | 0.0760 | . |
| High cholesterol | -0.1249 | 0.2705 | ±0.5410 | -0.462 | 0.6442 |  |
| Kidney disease | -0.0667 | 0.6878 | ±1.3756 | -0.097 | 0.9228 |  |
| Circulatory disease | -0.2151 | 0.4142 | ±0.8283 | -0.519 | 0.6035 |  |
| Nocturnal time > 180 (%) | +0.1021 | 0.3152 | ±0.6304 | +0.324 | 0.7460 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
