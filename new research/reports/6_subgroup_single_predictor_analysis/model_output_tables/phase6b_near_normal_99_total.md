# Phase 6b model output tables - Near-normal substitute: >= 99% of readings within 70-180 - Total analysis base

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). The covariates-only reference model precedes each outcome's predictor models.


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


---

### CES-D-10 depressive symptoms (0-30)  (domain: Depression; outcome sample N = 454; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **454**, R² = **0.0815**, Adj R² = **0.0607**, F-statistic = **3.93** (p = **3.82e-05**), Residual SE = **4.589** on **443** df, AIC = **2682.7**, BIC = **2728.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4901** | 1.6991 | ±3.3981 | **+4.408** | **1.04e-05** | *** |
| Education: graduate level (vs college) | -0.7258 | 0.4561 | ±0.9122 | -1.591 | 0.1116 |  |
| Education: high school or below (vs college) | +1.4795 | 0.9883 | ±1.9766 | +1.497 | 0.1344 |  |
| Site: UCSD (vs UAB) | -0.3813 | 0.5508 | ±1.1015 | -0.692 | 0.4888 |  |
| Site: UW (vs UAB) | +0.2832 | 0.5811 | ±1.1622 | +0.487 | 0.6260 |  |
| **Age (years)** | **-0.0692** | 0.0199 | ±0.0399 | **-3.474** | **5.12e-04** | *** |
| **BMI (kg/m2)** | **+0.0675** | 0.0335 | ±0.0669 | **+2.017** | **0.0437** | * |
| Hypertension | +0.3715 | 0.5106 | ±1.0212 | +0.728 | 0.4668 |  |
| High cholesterol | +0.7434 | 0.4680 | ±0.9360 | +1.589 | 0.1122 |  |
| Kidney disease | +1.1321 | 0.9230 | ±1.8459 | +1.227 | 0.2200 |  |
| Circulatory disease | +0.7761 | 0.7968 | ±1.5935 | +0.974 | 0.3300 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **454**, R² = **0.0815**, Adj R² = **0.0586**, F-statistic = **3.56** (p = **8.00e-05**), Residual SE = **4.594** on **442** df, AIC = **2684.7**, BIC = **2734.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +7.5527 | 4.3235 | ±8.6469 | +1.747 | 0.0807 | . |
| Education: graduate level (vs college) | -0.7260 | 0.4558 | ±0.9116 | -1.593 | 0.1112 |  |
| Education: high school or below (vs college) | +1.4804 | 0.9890 | ±1.9780 | +1.497 | 0.1344 |  |
| Site: UCSD (vs UAB) | -0.3814 | 0.5529 | ±1.1058 | -0.690 | 0.4903 |  |
| Site: UW (vs UAB) | +0.2829 | 0.5845 | ±1.1689 | +0.484 | 0.6284 |  |
| **Age (years)** | **-0.0692** | 0.0201 | ±0.0402 | **-3.445** | **5.70e-04** | *** |
| **BMI (kg/m2)** | **+0.0675** | 0.0337 | ±0.0674 | **+2.003** | **0.0452** | * |
| Hypertension | +0.3723 | 0.5084 | ±1.0169 | +0.732 | 0.4640 |  |
| High cholesterol | +0.7449 | 0.4852 | ±0.9703 | +1.535 | 0.1247 |  |
| Kidney disease | +1.1312 | 0.9282 | ±1.8564 | +1.219 | 0.2229 |  |
| Circulatory disease | +0.7759 | 0.8003 | ±1.6006 | +0.970 | 0.3323 |  |
| HbA1c (%) | -0.0120 | 0.7614 | ±1.5228 | -0.016 | 0.9874 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **454**, R² = **0.0815**, Adj R² = **0.0587**, F-statistic = **3.57** (p = **7.93e-05**), Residual SE = **4.594** on **442** df, AIC = **2684.7**, BIC = **2734.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.9567** | 3.4248 | ±6.8496 | **+2.323** | **0.0202** | * |
| Education: graduate level (vs college) | -0.7251 | 0.4576 | ±0.9151 | -1.585 | 0.1131 |  |
| Education: high school or below (vs college) | +1.4759 | 0.9878 | ±1.9757 | +1.494 | 0.1351 |  |
| Site: UCSD (vs UAB) | -0.3775 | 0.5550 | ±1.1099 | -0.680 | 0.4964 |  |
| Site: UW (vs UAB) | +0.2878 | 0.5891 | ±1.1782 | +0.489 | 0.6251 |  |
| **Age (years)** | **-0.0693** | 0.0199 | ±0.0398 | **-3.485** | **4.92e-04** | *** |
| **BMI (kg/m2)** | **+0.0677** | 0.0335 | ±0.0670 | **+2.023** | **0.0431** | * |
| Hypertension | +0.3756 | 0.5106 | ±1.0212 | +0.736 | 0.4620 |  |
| High cholesterol | +0.7405 | 0.4699 | ±0.9397 | +1.576 | 0.1150 |  |
| Kidney disease | +1.1362 | 0.9232 | ±1.8465 | +1.231 | 0.2184 |  |
| Circulatory disease | +0.7788 | 0.7966 | ±1.5932 | +0.978 | 0.3282 |  |
| Mean glucose (mg/dL) | -0.0041 | 0.0283 | ±0.0567 | -0.146 | 0.8837 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **454**, R² = **0.0815**, Adj R² = **0.0587**, F-statistic = **3.57** (p = **7.93e-05**), Residual SE = **4.594** on **442** df, AIC = **2684.7**, BIC = **2734.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +8.5300 | 7.1033 | ±14.2066 | +1.201 | 0.2298 |  |
| Education: graduate level (vs college) | -0.7251 | 0.4576 | ±0.9151 | -1.585 | 0.1131 |  |
| Education: high school or below (vs college) | +1.4759 | 0.9878 | ±1.9757 | +1.494 | 0.1351 |  |
| Site: UCSD (vs UAB) | -0.3775 | 0.5550 | ±1.1099 | -0.680 | 0.4964 |  |
| Site: UW (vs UAB) | +0.2878 | 0.5891 | ±1.1782 | +0.489 | 0.6251 |  |
| **Age (years)** | **-0.0693** | 0.0199 | ±0.0398 | **-3.485** | **4.92e-04** | *** |
| **BMI (kg/m2)** | **+0.0677** | 0.0335 | ±0.0670 | **+2.023** | **0.0431** | * |
| Hypertension | +0.3756 | 0.5106 | ±1.0212 | +0.736 | 0.4620 |  |
| High cholesterol | +0.7405 | 0.4699 | ±0.9397 | +1.576 | 0.1150 |  |
| Kidney disease | +1.1362 | 0.9232 | ±1.8465 | +1.231 | 0.2184 |  |
| Circulatory disease | +0.7788 | 0.7966 | ±1.5932 | +0.978 | 0.3282 |  |
| GMI (%) | -0.1732 | 1.1844 | ±2.3688 | -0.146 | 0.8837 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **454**, R² = **0.0815**, Adj R² = **0.0587**, F-statistic = **3.57** (p = **7.91e-05**), Residual SE = **4.594** on **442** df, AIC = **2684.7**, BIC = **2734.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.9343** | 2.9760 | ±5.9519 | **+2.666** | **0.0077** | ** |
| Education: graduate level (vs college) | -0.7277 | 0.4565 | ±0.9131 | -1.594 | 0.1109 |  |
| Education: high school or below (vs college) | +1.4743 | 0.9872 | ±1.9743 | +1.493 | 0.1353 |  |
| Site: UCSD (vs UAB) | -0.3730 | 0.5559 | ±1.1119 | -0.671 | 0.5023 |  |
| Site: UW (vs UAB) | +0.2909 | 0.5916 | ±1.1832 | +0.492 | 0.6229 |  |
| **Age (years)** | **-0.0697** | 0.0198 | ±0.0395 | **-3.527** | **4.20e-04** | *** |
| **BMI (kg/m2)** | **+0.0683** | 0.0337 | ±0.0674 | **+2.025** | **0.0428** | * |
| Hypertension | +0.3762 | 0.5088 | ±1.0176 | +0.739 | 0.4596 |  |
| High cholesterol | +0.7422 | 0.4693 | ±0.9385 | +1.582 | 0.1137 |  |
| Kidney disease | +1.1295 | 0.9266 | ±1.8531 | +1.219 | 0.2228 |  |
| Circulatory disease | +0.7773 | 0.7978 | ±1.5955 | +0.974 | 0.3299 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0039 | 0.0225 | ±0.0450 | -0.172 | 0.8637 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **454**, R² = **0.0850**, Adj R² = **0.0622**, F-statistic = **3.73** (p = **4.09e-05**), Residual SE = **4.585** on **442** df, AIC = **2682.9**, BIC = **2732.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.5084** | 2.2907 | ±4.5814 | **+2.405** | **0.0162** | * |
| Education: graduate level (vs college) | -0.6852 | 0.4569 | ±0.9138 | -1.500 | 0.1337 |  |
| Education: high school or below (vs college) | +1.4681 | 0.9955 | ±1.9910 | +1.475 | 0.1403 |  |
| Site: UCSD (vs UAB) | -0.3460 | 0.5529 | ±1.1058 | -0.626 | 0.5314 |  |
| Site: UW (vs UAB) | +0.3234 | 0.5807 | ±1.1615 | +0.557 | 0.5776 |  |
| **Age (years)** | **-0.0696** | 0.0200 | ±0.0399 | **-3.490** | **4.83e-04** | *** |
| **BMI (kg/m2)** | **+0.0658** | 0.0334 | ±0.0669 | **+1.969** | **0.0490** | * |
| Hypertension | +0.3309 | 0.5052 | ±1.0104 | +0.655 | 0.5125 |  |
| High cholesterol | +0.7810 | 0.4696 | ±0.9393 | +1.663 | 0.0963 | . |
| Kidney disease | +1.0118 | 0.9043 | ±1.8086 | +1.119 | 0.2632 |  |
| Circulatory disease | +0.7444 | 0.7936 | ±1.5872 | +0.938 | 0.3483 |  |
| Glucose SD, pooled (mg/dL) | +0.1205 | 0.0966 | ±0.1931 | +1.248 | 0.2121 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **454**, R² = **0.0843**, Adj R² = **0.0615**, F-statistic = **3.70** (p = **4.71e-05**), Residual SE = **4.587** on **442** df, AIC = **2683.3**, BIC = **2732.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.9376** | 2.1586 | ±4.3171 | **+2.751** | **0.0059** | ** |
| Education: graduate level (vs college) | -0.6867 | 0.4556 | ±0.9111 | -1.507 | 0.1317 |  |
| Education: high school or below (vs college) | +1.4844 | 0.9906 | ±1.9812 | +1.499 | 0.1340 |  |
| Site: UCSD (vs UAB) | -0.3559 | 0.5522 | ±1.1045 | -0.644 | 0.5193 |  |
| Site: UW (vs UAB) | +0.3141 | 0.5798 | ±1.1596 | +0.542 | 0.5880 |  |
| **Age (years)** | **-0.0699** | 0.0200 | ±0.0399 | **-3.501** | **4.63e-04** | *** |
| BMI (kg/m2) | +0.0649 | 0.0334 | ±0.0668 | +1.943 | 0.0520 | . |
| Hypertension | +0.3492 | 0.5082 | ±1.0164 | +0.687 | 0.4920 |  |
| High cholesterol | +0.7737 | 0.4703 | ±0.9405 | +1.645 | 0.0999 | . |
| Kidney disease | +1.0297 | 0.9091 | ±1.8182 | +1.133 | 0.2573 |  |
| Circulatory disease | +0.7660 | 0.7918 | ±1.5836 | +0.967 | 0.3333 |  |
| Avg. daily SD (mg/dL) | +0.1063 | 0.0989 | ±0.1978 | +1.075 | 0.2824 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **454**, R² = **0.0850**, Adj R² = **0.0623**, F-statistic = **3.73** (p = **4.07e-05**), Residual SE = **4.585** on **442** df, AIC = **2682.9**, BIC = **2732.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+5.5351** | 2.2948 | ±4.5895 | **+2.412** | **0.0159** | * |
| Education: graduate level (vs college) | -0.6830 | 0.4577 | ±0.9155 | -1.492 | 0.1357 |  |
| Education: high school or below (vs college) | +1.4552 | 0.9911 | ±1.9821 | +1.468 | 0.1420 |  |
| Site: UCSD (vs UAB) | -0.3320 | 0.5555 | ±1.1110 | -0.598 | 0.5501 |  |
| Site: UW (vs UAB) | +0.3416 | 0.5852 | ±1.1705 | +0.584 | 0.5594 |  |
| **Age (years)** | **-0.0699** | 0.0199 | ±0.0399 | **-3.505** | **4.57e-04** | *** |
| **BMI (kg/m2)** | **+0.0670** | 0.0333 | ±0.0665 | **+2.015** | **0.0439** | * |
| Hypertension | +0.3499 | 0.5077 | ±1.0154 | +0.689 | 0.4908 |  |
| High cholesterol | +0.7697 | 0.4684 | ±0.9367 | +1.643 | 0.1003 |  |
| Kidney disease | +1.0341 | 0.9076 | ±1.8152 | +1.139 | 0.2545 |  |
| Circulatory disease | +0.7544 | 0.7953 | ±1.5906 | +0.949 | 0.3428 |  |
| CV (%) | +0.1331 | 0.1021 | ±0.2041 | +1.304 | 0.1922 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **454**, R² = **0.0854**, Adj R² = **0.0627**, F-statistic = **3.75** (p = **3.78e-05**), Residual SE = **4.584** on **442** df, AIC = **2682.7**, BIC = **2732.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+9.4561** | 2.1634 | ±4.3267 | **+4.371** | **1.24e-05** | *** |
| Education: graduate level (vs college) | -0.6744 | 0.4586 | ±0.9173 | -1.471 | 0.1414 |  |
| Education: high school or below (vs college) | +1.4497 | 0.9900 | ±1.9799 | +1.464 | 0.1431 |  |
| Site: UCSD (vs UAB) | -0.3422 | 0.5534 | ±1.1068 | -0.618 | 0.5364 |  |
| Site: UW (vs UAB) | +0.3328 | 0.5828 | ±1.1655 | +0.571 | 0.5680 |  |
| **Age (years)** | **-0.0697** | 0.0199 | ±0.0399 | **-3.493** | **4.78e-04** | *** |
| **BMI (kg/m2)** | **+0.0671** | 0.0333 | ±0.0666 | **+2.015** | **0.0440** | * |
| Hypertension | +0.3469 | 0.5074 | ±1.0148 | +0.684 | 0.4943 |  |
| High cholesterol | +0.7750 | 0.4686 | ±0.9372 | +1.654 | 0.0982 | . |
| Kidney disease | +1.0546 | 0.9064 | ±1.8127 | +1.164 | 0.2446 |  |
| Circulatory disease | +0.7627 | 0.7928 | ±1.5856 | +0.962 | 0.3360 |  |
| Mean / SD ratio | -0.2848 | 0.1988 | ±0.3977 | -1.432 | 0.1521 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **454**, R² = **0.0841**, Adj R² = **0.0613**, F-statistic = **3.69** (p = **4.84e-05**), Residual SE = **4.587** on **442** df, AIC = **2683.4**, BIC = **2732.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+8.9635** | 2.2114 | ±4.4228 | **+4.053** | **5.05e-05** | *** |
| Education: graduate level (vs college) | -0.6823 | 0.4574 | ±0.9148 | -1.492 | 0.1358 |  |
| Education: high school or below (vs college) | +1.4662 | 0.9867 | ±1.9734 | +1.486 | 0.1373 |  |
| Site: UCSD (vs UAB) | -0.3558 | 0.5520 | ±1.1041 | -0.644 | 0.5193 |  |
| Site: UW (vs UAB) | +0.3182 | 0.5812 | ±1.1624 | +0.547 | 0.5841 |  |
| **Age (years)** | **-0.0700** | 0.0200 | ±0.0399 | **-3.506** | **4.55e-04** | *** |
| **BMI (kg/m2)** | **+0.0659** | 0.0334 | ±0.0667 | **+1.974** | **0.0483** | * |
| Hypertension | +0.3646 | 0.5107 | ±1.0215 | +0.714 | 0.4753 |  |
| High cholesterol | +0.7621 | 0.4695 | ±0.9389 | +1.623 | 0.1045 |  |
| Kidney disease | +1.0679 | 0.9135 | ±1.8271 | +1.169 | 0.2424 |  |
| Circulatory disease | +0.7889 | 0.7911 | ±1.5821 | +0.997 | 0.3186 |  |
| Avg. daily mean/SD | -0.1807 | 0.1664 | ±0.3329 | -1.086 | 0.2775 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **454**, R² = **0.0983**, Adj R² = **0.0758**, F-statistic = **4.38** (p = **3.00e-06**), Residual SE = **4.552** on **442** df, AIC = **2676.3**, BIC = **2725.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +3.3873 | 2.1457 | ±4.2913 | +1.579 | 0.1144 |  |
| Education: graduate level (vs college) | -0.7277 | 0.4562 | ±0.9123 | -1.595 | 0.1107 |  |
| Education: high school or below (vs college) | +1.3113 | 0.9682 | ±1.9364 | +1.354 | 0.1756 |  |
| Site: UCSD (vs UAB) | -0.3392 | 0.5408 | ±1.0817 | -0.627 | 0.5306 |  |
| Site: UW (vs UAB) | +0.4287 | 0.5672 | ±1.1345 | +0.756 | 0.4498 |  |
| **Age (years)** | **-0.0643** | 0.0199 | ±0.0399 | **-3.225** | **0.0013** | ** |
| **BMI (kg/m2)** | **+0.0720** | 0.0322 | ±0.0645 | **+2.234** | **0.0255** | * |
| Hypertension | +0.4147 | 0.5076 | ±1.0151 | +0.817 | 0.4139 |  |
| High cholesterol | +0.7024 | 0.4687 | ±0.9375 | +1.498 | 0.1340 |  |
| Kidney disease | +1.0071 | 0.8942 | ±1.7884 | +1.126 | 0.2601 |  |
| Circulatory disease | +0.8406 | 0.7737 | ±1.5474 | +1.087 | 0.2772 |  |
| **MAG (mg/dL/h)** | **+0.1064** | 0.0382 | ±0.0765 | **+2.783** | **0.0054** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **454**, R² = **0.0867**, Adj R² = **0.0639**, F-statistic = **3.81** (p = **2.96e-05**), Residual SE = **4.581** on **442** df, AIC = **2682.1**, BIC = **2731.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+4.9376** | 2.2795 | ±4.5590 | **+2.166** | **0.0303** | * |
| Education: graduate level (vs college) | -0.6935 | 0.4556 | ±0.9112 | -1.522 | 0.1280 |  |
| Education: high school or below (vs college) | +1.4746 | 0.9799 | ±1.9599 | +1.505 | 0.1324 |  |
| Site: UCSD (vs UAB) | -0.3460 | 0.5504 | ±1.1009 | -0.629 | 0.5296 |  |
| Site: UW (vs UAB) | +0.3289 | 0.5769 | ±1.1539 | +0.570 | 0.5687 |  |
| **Age (years)** | **-0.0699** | 0.0200 | ±0.0400 | **-3.494** | **4.76e-04** | *** |
| **BMI (kg/m2)** | **+0.0712** | 0.0338 | ±0.0677 | **+2.103** | **0.0355** | * |
| Hypertension | +0.3915 | 0.5113 | ±1.0225 | +0.766 | 0.4438 |  |
| High cholesterol | +0.7466 | 0.4689 | ±0.9378 | +1.592 | 0.1113 |  |
| Kidney disease | +1.0516 | 0.8936 | ±1.7872 | +1.177 | 0.2393 |  |
| Circulatory disease | +0.7743 | 0.7889 | ±1.5778 | +0.981 | 0.3264 |  |
| Avg. daily range (mg/dL) | +0.0307 | 0.0196 | ±0.0393 | +1.561 | 0.1186 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **454**, R² = **0.0835**, Adj R² = **0.0607**, F-statistic = **3.66** (p = **5.47e-05**), Residual SE = **4.589** on **442** df, AIC = **2683.7**, BIC = **2733.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.9137** | 1.8080 | ±3.6160 | **+3.824** | **1.31e-04** | *** |
| Education: graduate level (vs college) | -0.7384 | 0.4551 | ±0.9102 | -1.622 | 0.1047 |  |
| Education: high school or below (vs college) | +1.4277 | 1.0106 | ±2.0211 | +1.413 | 0.1577 |  |
| Site: UCSD (vs UAB) | -0.3592 | 0.5520 | ±1.1040 | -0.651 | 0.5152 |  |
| Site: UW (vs UAB) | +0.2747 | 0.5826 | ±1.1652 | +0.472 | 0.6373 |  |
| **Age (years)** | **-0.0688** | 0.0201 | ±0.0402 | **-3.426** | **6.13e-04** | *** |
| **BMI (kg/m2)** | **+0.0671** | 0.0335 | ±0.0670 | **+2.004** | **0.0450** | * |
| Hypertension | +0.3327 | 0.5051 | ±1.0103 | +0.659 | 0.5102 |  |
| High cholesterol | +0.7251 | 0.4709 | ±0.9418 | +1.540 | 0.1236 |  |
| Kidney disease | +1.1302 | 0.9236 | ±1.8472 | +1.224 | 0.2211 |  |
| Circulatory disease | +0.7245 | 0.7991 | ±1.5983 | +0.907 | 0.3646 |  |
| SD of daily means (mg/dL) | +0.1153 | 0.1285 | ±0.2569 | +0.897 | 0.3695 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **454**, R² = **0.0818**, Adj R² = **0.0590**, F-statistic = **3.58** (p = **7.48e-05**), Residual SE = **4.593** on **442** df, AIC = **2684.5**, BIC = **2733.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +37.0349 | 65.3169 | ±130.6337 | +0.567 | 0.5707 |  |
| Education: graduate level (vs college) | -0.7187 | 0.4557 | ±0.9115 | -1.577 | 0.1148 |  |
| Education: high school or below (vs college) | +1.4859 | 0.9872 | ±1.9744 | +1.505 | 0.1323 |  |
| Site: UCSD (vs UAB) | -0.3706 | 0.5517 | ±1.1034 | -0.672 | 0.5018 |  |
| Site: UW (vs UAB) | +0.2927 | 0.5821 | ±1.1643 | +0.503 | 0.6151 |  |
| **Age (years)** | **-0.0690** | 0.0200 | ±0.0399 | **-3.456** | **5.49e-04** | *** |
| **BMI (kg/m2)** | **+0.0681** | 0.0339 | ±0.0678 | **+2.010** | **0.0444** | * |
| Hypertension | +0.3675 | 0.5106 | ±1.0211 | +0.720 | 0.4716 |  |
| High cholesterol | +0.7377 | 0.4697 | ±0.9394 | +1.570 | 0.1163 |  |
| Kidney disease | +1.1086 | 0.9150 | ±1.8301 | +1.211 | 0.2257 |  |
| Circulatory disease | +0.7804 | 0.7975 | ±1.5950 | +0.978 | 0.3278 |  |
| Time in range 70-180, pooled (%) | -0.2972 | 0.6568 | ±1.3135 | -0.452 | 0.6509 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **454**, R² = **0.0824**, Adj R² = **0.0596**, F-statistic = **3.61** (p = **6.70e-05**), Residual SE = **4.592** on **442** df, AIC = **2684.2**, BIC = **2733.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +54.3649 | 67.2073 | ±134.4146 | +0.809 | 0.4186 |  |
| Education: graduate level (vs college) | -0.7116 | 0.4540 | ±0.9079 | -1.567 | 0.1170 |  |
| Education: high school or below (vs college) | +1.4933 | 0.9861 | ±1.9723 | +1.514 | 0.1300 |  |
| Site: UCSD (vs UAB) | -0.3776 | 0.5523 | ±1.1046 | -0.684 | 0.4942 |  |
| Site: UW (vs UAB) | +0.2824 | 0.5809 | ±1.1617 | +0.486 | 0.6269 |  |
| **Age (years)** | **-0.0688** | 0.0199 | ±0.0399 | **-3.451** | **5.58e-04** | *** |
| **BMI (kg/m2)** | **+0.0679** | 0.0336 | ±0.0671 | **+2.022** | **0.0432** | * |
| Hypertension | +0.3817 | 0.5133 | ±1.0265 | +0.744 | 0.4571 |  |
| High cholesterol | +0.7276 | 0.4710 | ±0.9421 | +1.545 | 0.1224 |  |
| Kidney disease | +1.1150 | 0.9118 | ±1.8236 | +1.223 | 0.2214 |  |
| Circulatory disease | +0.7702 | 0.7950 | ±1.5899 | +0.969 | 0.3327 |  |
| Avg. daily time in range 70-180 (%) | -0.4710 | 0.6745 | ±1.3491 | -0.698 | 0.4850 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **454**, R² = **0.0869**, Adj R² = **0.0641**, F-statistic = **3.82** (p = **2.86e-05**), Residual SE = **4.580** on **442** df, AIC = **2682.0**, BIC = **2731.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.7566** | 1.7051 | ±3.4101 | **+4.549** | **5.39e-06** | *** |
| Education: graduate level (vs college) | -0.7387 | 0.4559 | ±0.9117 | -1.621 | 0.1051 |  |
| Education: high school or below (vs college) | +1.4243 | 0.9969 | ±1.9939 | +1.429 | 0.1531 |  |
| Site: UCSD (vs UAB) | -0.5339 | 0.5603 | ±1.1205 | -0.953 | 0.3406 |  |
| Site: UW (vs UAB) | +0.1938 | 0.5835 | ±1.1670 | +0.332 | 0.7397 |  |
| **Age (years)** | **-0.0698** | 0.0199 | ±0.0398 | **-3.511** | **4.46e-04** | *** |
| **BMI (kg/m2)** | **+0.0677** | 0.0335 | ±0.0671 | **+2.020** | **0.0434** | * |
| Hypertension | +0.4223 | 0.5110 | ±1.0221 | +0.826 | 0.4086 |  |
| High cholesterol | +0.7468 | 0.4667 | ±0.9334 | +1.600 | 0.1095 |  |
| Kidney disease | +1.0255 | 0.9211 | ±1.8423 | +1.113 | 0.2656 |  |
| Circulatory disease | +0.8039 | 0.7992 | ±1.5984 | +1.006 | 0.3145 |  |
| Any reading < 54 during wear (0/1) | -0.9512 | 0.5628 | ±1.1257 | -1.690 | 0.0910 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **454**, R² = **0.0884**, Adj R² = **0.0657**, F-statistic = **3.90** (p = **2.13e-05**), Residual SE = **4.577** on **442** df, AIC = **2681.3**, BIC = **2730.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.7123** | 1.7243 | ±3.4487 | **+4.473** | **7.73e-06** | *** |
| Education: graduate level (vs college) | -0.7350 | 0.4548 | ±0.9096 | -1.616 | 0.1061 |  |
| Education: high school or below (vs college) | +1.3744 | 0.9905 | ±1.9810 | +1.388 | 0.1653 |  |
| Site: UCSD (vs UAB) | -0.5175 | 0.5558 | ±1.1117 | -0.931 | 0.3518 |  |
| Site: UW (vs UAB) | +0.2169 | 0.5809 | ±1.1618 | +0.373 | 0.7089 |  |
| **Age (years)** | **-0.0718** | 0.0200 | ±0.0400 | **-3.590** | **3.31e-04** | *** |
| **BMI (kg/m2)** | **+0.0720** | 0.0341 | ±0.0682 | **+2.112** | **0.0347** | * |
| Hypertension | +0.4520 | 0.5131 | ±1.0262 | +0.881 | 0.3784 |  |
| High cholesterol | +0.7180 | 0.4658 | ±0.9317 | +1.541 | 0.1233 |  |
| Kidney disease | +1.0444 | 0.9197 | ±1.8394 | +1.136 | 0.2561 |  |
| Circulatory disease | +0.8365 | 0.8051 | ±1.6101 | +1.039 | 0.2988 |  |
| **Time < 54 (%)** | **-7.5735** | 3.5157 | ±7.0313 | **-2.154** | **0.0312** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **454**, R² = **0.0850**, Adj R² = **0.0623**, F-statistic = **3.74** (p = **4.05e-05**), Residual SE = **4.585** on **442** df, AIC = **2682.9**, BIC = **2732.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.5551** | 1.7060 | ±3.4120 | **+4.429** | **9.49e-06** | *** |
| Education: graduate level (vs college) | -0.7310 | 0.4555 | ±0.9111 | -1.605 | 0.1086 |  |
| Education: high school or below (vs college) | +1.4413 | 0.9876 | ±1.9752 | +1.459 | 0.1445 |  |
| Site: UCSD (vs UAB) | -0.4231 | 0.5496 | ±1.0992 | -0.770 | 0.4414 |  |
| Site: UW (vs UAB) | +0.2763 | 0.5817 | ±1.1633 | +0.475 | 0.6347 |  |
| **Age (years)** | **-0.0697** | 0.0199 | ±0.0398 | **-3.502** | **4.62e-04** | *** |
| **BMI (kg/m2)** | **+0.0689** | 0.0336 | ±0.0673 | **+2.049** | **0.0405** | * |
| Hypertension | +0.3889 | 0.5112 | ±1.0223 | +0.761 | 0.4468 |  |
| High cholesterol | +0.7438 | 0.4675 | ±0.9351 | +1.591 | 0.1116 |  |
| Kidney disease | +1.0852 | 0.9222 | ±1.8443 | +1.177 | 0.2393 |  |
| Circulatory disease | +0.8464 | 0.8101 | ±1.6202 | +1.045 | 0.2961 |  |
| Avg. daily time < 54 (%) | -7.1025 | 5.5763 | ±11.1527 | -1.274 | 0.2028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **454**, R² = **0.0827**, Adj R² = **0.0599**, F-statistic = **3.62** (p = **6.33e-05**), Residual SE = **4.591** on **442** df, AIC = **2684.1**, BIC = **2733.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3345** | 1.7220 | ±3.4440 | **+4.259** | **2.05e-05** | *** |
| Education: graduate level (vs college) | -0.7111 | 0.4570 | ±0.9139 | -1.556 | 0.1197 |  |
| Education: high school or below (vs college) | +1.4440 | 0.9860 | ±1.9719 | +1.465 | 0.1430 |  |
| Site: UCSD (vs UAB) | -0.3591 | 0.5529 | ±1.1057 | -0.649 | 0.5160 |  |
| Site: UW (vs UAB) | +0.3146 | 0.5857 | ±1.1714 | +0.537 | 0.5912 |  |
| **Age (years)** | **-0.0692** | 0.0200 | ±0.0399 | **-3.465** | **5.31e-04** | *** |
| **BMI (kg/m2)** | **+0.0676** | 0.0333 | ±0.0665 | **+2.033** | **0.0420** | * |
| Hypertension | +0.3943 | 0.5113 | ±1.0226 | +0.771 | 0.4406 |  |
| High cholesterol | +0.7085 | 0.4720 | ±0.9440 | +1.501 | 0.1333 |  |
| Kidney disease | +1.1767 | 0.9230 | ±1.8461 | +1.275 | 0.2024 |  |
| Circulatory disease | +0.7881 | 0.7963 | ±1.5926 | +0.990 | 0.3223 |  |
| Time 54-69, pooled (%) | +0.9260 | 1.2035 | ±2.4069 | +0.769 | 0.4416 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **454**, R² = **0.0823**, Adj R² = **0.0595**, F-statistic = **3.60** (p = **6.82e-05**), Residual SE = **4.592** on **442** df, AIC = **2684.3**, BIC = **2733.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3929** | 1.7129 | ±3.4257 | **+4.316** | **1.59e-05** | *** |
| Education: graduate level (vs college) | -0.7065 | 0.4560 | ±0.9121 | -1.549 | 0.1213 |  |
| Education: high school or below (vs college) | +1.4510 | 0.9878 | ±1.9756 | +1.469 | 0.1418 |  |
| Site: UCSD (vs UAB) | -0.3749 | 0.5524 | ±1.1048 | -0.679 | 0.4973 |  |
| Site: UW (vs UAB) | +0.2955 | 0.5835 | ±1.1670 | +0.506 | 0.6125 |  |
| **Age (years)** | **-0.0695** | 0.0199 | ±0.0398 | **-3.487** | **4.89e-04** | *** |
| **BMI (kg/m2)** | **+0.0675** | 0.0333 | ±0.0667 | **+2.026** | **0.0427** | * |
| Hypertension | +0.4085 | 0.5146 | ±1.0293 | +0.794 | 0.4274 |  |
| High cholesterol | +0.7181 | 0.4727 | ±0.9455 | +1.519 | 0.1287 |  |
| Kidney disease | +1.1659 | 0.9220 | ±1.8440 | +1.265 | 0.2060 |  |
| Circulatory disease | +0.7731 | 0.7974 | ±1.5948 | +0.970 | 0.3323 |  |
| Avg. daily time 54-69 (%) | +0.7791 | 1.2581 | ±2.5161 | +0.619 | 0.5357 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **454**, R² = **0.0816**, Adj R² = **0.0587**, F-statistic = **3.57** (p = **7.85e-05**), Residual SE = **4.594** on **442** df, AIC = **2684.6**, BIC = **2734.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4447** | 1.7284 | ±3.4567 | **+4.307** | **1.65e-05** | *** |
| Education: graduate level (vs college) | -0.7219 | 0.4577 | ±0.9154 | -1.577 | 0.1148 |  |
| Education: high school or below (vs college) | +1.4739 | 0.9896 | ±1.9793 | +1.489 | 0.1364 |  |
| Site: UCSD (vs UAB) | -0.3716 | 0.5533 | ±1.1067 | -0.672 | 0.5019 |  |
| Site: UW (vs UAB) | +0.2930 | 0.5868 | ±1.1735 | +0.499 | 0.6175 |  |
| **Age (years)** | **-0.0691** | 0.0200 | ±0.0400 | **-3.456** | **5.48e-04** | *** |
| **BMI (kg/m2)** | **+0.0674** | 0.0334 | ±0.0668 | **+2.016** | **0.0438** | * |
| Hypertension | +0.3747 | 0.5116 | ±1.0231 | +0.733 | 0.4638 |  |
| High cholesterol | +0.7355 | 0.4715 | ±0.9431 | +1.560 | 0.1188 |  |
| Kidney disease | +1.1458 | 0.9271 | ±1.8542 | +1.236 | 0.2165 |  |
| Circulatory disease | +0.7773 | 0.7975 | ±1.5951 | +0.975 | 0.3298 |  |
| Time < 70 (%) | +0.2302 | 1.0556 | ±2.1112 | +0.218 | 0.8274 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **454**, R² = **0.0817**, Adj R² = **0.0588**, F-statistic = **3.57** (p = **7.70e-05**), Residual SE = **4.593** on **442** df, AIC = **2684.6**, BIC = **2734.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4439** | 1.7150 | ±3.4299 | **+4.341** | **1.42e-05** | *** |
| Education: graduate level (vs college) | -0.7170 | 0.4572 | ±0.9143 | -1.568 | 0.1168 |  |
| Education: high school or below (vs college) | +1.4687 | 0.9898 | ±1.9797 | +1.484 | 0.1379 |  |
| Site: UCSD (vs UAB) | -0.3764 | 0.5519 | ±1.1038 | -0.682 | 0.4952 |  |
| Site: UW (vs UAB) | +0.2890 | 0.5840 | ±1.1679 | +0.495 | 0.6207 |  |
| **Age (years)** | **-0.0693** | 0.0199 | ±0.0399 | **-3.475** | **5.11e-04** | *** |
| **BMI (kg/m2)** | **+0.0674** | 0.0334 | ±0.0669 | **+2.017** | **0.0437** | * |
| Hypertension | +0.3871 | 0.5143 | ±1.0286 | +0.753 | 0.4517 |  |
| High cholesterol | +0.7322 | 0.4731 | ±0.9462 | +1.548 | 0.1217 |  |
| Kidney disease | +1.1493 | 0.9257 | ±1.8513 | +1.242 | 0.2144 |  |
| Circulatory disease | +0.7714 | 0.7985 | ±1.5969 | +0.966 | 0.3340 |  |
| Avg. daily time < 70 (%) | +0.3454 | 1.1415 | ±2.2831 | +0.303 | 0.7622 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **454**, R² = **0.0883**, Adj R² = **0.0656**, F-statistic = **3.89** (p = **2.17e-05**), Residual SE = **4.577** on **442** df, AIC = **2681.3**, BIC = **2730.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-726.0633** | 338.4206 | ±676.8412 | **-2.145** | **0.0319** | * |
| Education: graduate level (vs college) | -0.7342 | 0.4548 | ±0.9095 | -1.614 | 0.1064 |  |
| Education: high school or below (vs college) | +1.3738 | 0.9906 | ±1.9813 | +1.387 | 0.1655 |  |
| Site: UCSD (vs UAB) | -0.5227 | 0.5567 | ±1.1134 | -0.939 | 0.3478 |  |
| Site: UW (vs UAB) | +0.2117 | 0.5813 | ±1.1626 | +0.364 | 0.7157 |  |
| **Age (years)** | **-0.0722** | 0.0200 | ±0.0401 | **-3.602** | **3.16e-04** | *** |
| **BMI (kg/m2)** | **+0.0714** | 0.0340 | ±0.0679 | **+2.103** | **0.0355** | * |
| Hypertension | +0.4454 | 0.5122 | ±1.0245 | +0.870 | 0.3845 |  |
| High cholesterol | +0.7209 | 0.4658 | ±0.9316 | +1.548 | 0.1217 |  |
| Kidney disease | +1.0474 | 0.9194 | ±1.8388 | +1.139 | 0.2546 |  |
| Circulatory disease | +0.8347 | 0.8048 | ±1.6096 | +1.037 | 0.2997 |  |
| **Time 54-250, pooled (%)** | **+7.3382** | 3.3866 | ±6.7732 | **+2.167** | **0.0302** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **454**, R² = **0.0851**, Adj R² = **0.0624**, F-statistic = **3.74** (p = **4.00e-05**), Residual SE = **4.585** on **442** df, AIC = **2682.9**, BIC = **2732.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -694.7327 | 531.1671 | ±1062.3343 | -1.308 | 0.1909 |  |
| Education: graduate level (vs college) | -0.7304 | 0.4554 | ±0.9107 | -1.604 | 0.1087 |  |
| Education: high school or below (vs college) | +1.4377 | 0.9878 | ±1.9756 | +1.455 | 0.1455 |  |
| Site: UCSD (vs UAB) | -0.4325 | 0.5501 | ±1.1002 | -0.786 | 0.4317 |  |
| Site: UW (vs UAB) | +0.2689 | 0.5816 | ±1.1633 | +0.462 | 0.6439 |  |
| **Age (years)** | **-0.0701** | 0.0199 | ±0.0399 | **-3.519** | **4.34e-04** | *** |
| **BMI (kg/m2)** | **+0.0685** | 0.0336 | ±0.0671 | **+2.039** | **0.0414** | * |
| Hypertension | +0.3844 | 0.5107 | ±1.0214 | +0.753 | 0.4516 |  |
| High cholesterol | +0.7462 | 0.4676 | ±0.9352 | +1.596 | 0.1106 |  |
| Kidney disease | +1.0860 | 0.9218 | ±1.8436 | +1.178 | 0.2387 |  |
| Circulatory disease | +0.8456 | 0.8098 | ±1.6197 | +1.044 | 0.2964 |  |
| Avg. daily time 54-250 (%) | +7.0234 | 5.3137 | ±10.6273 | +1.322 | 0.1862 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **454**, R² = **0.0817**, Adj R² = **0.0588**, F-statistic = **3.57** (p = **7.74e-05**), Residual SE = **4.593** on **442** df, AIC = **2684.6**, BIC = **2734.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4044** | 1.7201 | ±3.4402 | **+4.305** | **1.67e-05** | *** |
| Education: graduate level (vs college) | -0.7242 | 0.4566 | ±0.9132 | -1.586 | 0.1127 |  |
| Education: high school or below (vs college) | +1.4898 | 0.9881 | ±1.9763 | +1.508 | 0.1316 |  |
| Site: UCSD (vs UAB) | -0.3829 | 0.5524 | ±1.1049 | -0.693 | 0.4882 |  |
| Site: UW (vs UAB) | +0.2805 | 0.5826 | ±1.1652 | +0.482 | 0.6301 |  |
| **Age (years)** | **-0.0692** | 0.0200 | ±0.0399 | **-3.466** | **5.29e-04** | *** |
| **BMI (kg/m2)** | **+0.0680** | 0.0339 | ±0.0678 | **+2.008** | **0.0447** | * |
| Hypertension | +0.3652 | 0.5090 | ±1.0181 | +0.717 | 0.4731 |  |
| High cholesterol | +0.7469 | 0.4691 | ±0.9382 | +1.592 | 0.1113 |  |
| Kidney disease | +1.1005 | 0.9202 | ±1.8404 | +1.196 | 0.2317 |  |
| Circulatory disease | +0.7782 | 0.7984 | ±1.5967 | +0.975 | 0.3297 |  |
| Time 181-250, pooled (%) | +0.2273 | 0.7351 | ±1.4703 | +0.309 | 0.7572 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **454**, R² = **0.0821**, Adj R² = **0.0592**, F-statistic = **3.59** (p = **7.15e-05**), Residual SE = **4.592** on **442** df, AIC = **2684.4**, BIC = **2733.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3517** | 1.7054 | ±3.4109 | **+4.311** | **1.63e-05** | *** |
| Education: graduate level (vs college) | -0.7238 | 0.4564 | ±0.9129 | -1.586 | 0.1128 |  |
| Education: high school or below (vs college) | +1.5043 | 0.9882 | ±1.9763 | +1.522 | 0.1279 |  |
| Site: UCSD (vs UAB) | -0.3844 | 0.5524 | ±1.1047 | -0.696 | 0.4865 |  |
| Site: UW (vs UAB) | +0.2751 | 0.5823 | ±1.1647 | +0.472 | 0.6367 |  |
| **Age (years)** | **-0.0688** | 0.0199 | ±0.0398 | **-3.457** | **5.46e-04** | *** |
| **BMI (kg/m2)** | **+0.0679** | 0.0337 | ±0.0673 | **+2.015** | **0.0439** | * |
| Hypertension | +0.3616 | 0.5081 | ±1.0163 | +0.712 | 0.4767 |  |
| High cholesterol | +0.7431 | 0.4693 | ±0.9386 | +1.584 | 0.1133 |  |
| Kidney disease | +1.0964 | 0.9153 | ±1.8306 | +1.198 | 0.2310 |  |
| Circulatory disease | +0.7766 | 0.7970 | ±1.5941 | +0.974 | 0.3299 |  |
| Avg. daily time 181-250 (%) | +0.4139 | 0.7510 | ±1.5019 | +0.551 | 0.5816 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **454**, R² = **0.0816**, Adj R² = **0.0588**, F-statistic = **3.57** (p = **7.75e-05**), Residual SE = **4.593** on **442** df, AIC = **2684.6**, BIC = **2734.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.4047** | 1.7212 | ±3.4425 | **+4.302** | **1.69e-05** | *** |
| Education: graduate level (vs college) | -0.7243 | 0.4566 | ±0.9132 | -1.586 | 0.1127 |  |
| Education: high school or below (vs college) | +1.4897 | 0.9881 | ±1.9762 | +1.508 | 0.1316 |  |
| Site: UCSD (vs UAB) | -0.3826 | 0.5524 | ±1.1047 | -0.693 | 0.4885 |  |
| Site: UW (vs UAB) | +0.2808 | 0.5825 | ±1.1650 | +0.482 | 0.6298 |  |
| **Age (years)** | **-0.0692** | 0.0200 | ±0.0399 | **-3.465** | **5.29e-04** | *** |
| **BMI (kg/m2)** | **+0.0680** | 0.0339 | ±0.0678 | **+2.008** | **0.0447** | * |
| Hypertension | +0.3654 | 0.5091 | ±1.0181 | +0.718 | 0.4728 |  |
| High cholesterol | +0.7468 | 0.4691 | ±0.9382 | +1.592 | 0.1114 |  |
| Kidney disease | +1.1012 | 0.9203 | ±1.8406 | +1.197 | 0.2315 |  |
| Circulatory disease | +0.7782 | 0.7984 | ±1.5967 | +0.975 | 0.3297 |  |
| Time > 180 (%) | +0.2223 | 0.7328 | ±1.4656 | +0.303 | 0.7616 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **454**, R² = **0.0821**, Adj R² = **0.0592**, F-statistic = **3.59** (p = **7.17e-05**), Residual SE = **4.592** on **442** df, AIC = **2684.4**, BIC = **2733.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+7.3509** | 1.7066 | ±3.4132 | **+4.307** | **1.65e-05** | *** |
| Education: graduate level (vs college) | -0.7238 | 0.4564 | ±0.9129 | -1.586 | 0.1128 |  |
| Education: high school or below (vs college) | +1.5041 | 0.9881 | ±1.9763 | +1.522 | 0.1280 |  |
| Site: UCSD (vs UAB) | -0.3838 | 0.5523 | ±1.1046 | -0.695 | 0.4871 |  |
| Site: UW (vs UAB) | +0.2757 | 0.5823 | ±1.1646 | +0.473 | 0.6359 |  |
| **Age (years)** | **-0.0688** | 0.0199 | ±0.0398 | **-3.456** | **5.48e-04** | *** |
| **BMI (kg/m2)** | **+0.0679** | 0.0337 | ±0.0673 | **+2.016** | **0.0438** | * |
| Hypertension | +0.3620 | 0.5082 | ±1.0164 | +0.712 | 0.4762 |  |
| High cholesterol | +0.7430 | 0.4693 | ±0.9386 | +1.583 | 0.1134 |  |
| Kidney disease | +1.0970 | 0.9154 | ±1.8308 | +1.198 | 0.2308 |  |
| Circulatory disease | +0.7766 | 0.7970 | ±1.5941 | +0.974 | 0.3299 |  |
| Avg. daily time > 180 (%) | +0.4073 | 0.7474 | ±1.4948 | +0.545 | 0.5858 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **454**, R² = **0.0999**, Adj R² = **0.0775**, F-statistic = **4.46** (p = **2.15e-06**), Residual SE = **4.548** on **442** df, AIC = **2675.5**, BIC = **2724.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+6.9564** | 1.6840 | ±3.3680 | **+4.131** | **3.61e-05** | *** |
| Education: graduate level (vs college) | -0.6454 | 0.4504 | ±0.9008 | -1.433 | 0.1519 |  |
| Education: high school or below (vs college) | +1.5083 | 1.0000 | ±1.9999 | +1.508 | 0.1315 |  |
| Site: UCSD (vs UAB) | -0.3864 | 0.5495 | ±1.0990 | -0.703 | 0.4820 |  |
| Site: UW (vs UAB) | +0.2202 | 0.5807 | ±1.1615 | +0.379 | 0.7045 |  |
| **Age (years)** | **-0.0597** | 0.0195 | ±0.0390 | **-3.064** | **0.0022** | ** |
| BMI (kg/m2) | +0.0607 | 0.0340 | ±0.0679 | +1.788 | 0.0738 | . |
| Hypertension | +0.2479 | 0.5000 | ±1.0001 | +0.496 | 0.6201 |  |
| High cholesterol | +0.6973 | 0.4647 | ±0.9294 | +1.501 | 0.1335 |  |
| Kidney disease | +1.0565 | 0.9185 | ±1.8369 | +1.150 | 0.2500 |  |
| Circulatory disease | +0.8756 | 0.7822 | ±1.5645 | +1.119 | 0.2630 |  |
| **Nocturnal time > 180 (%)** | **+1.8489** | 0.7902 | ±1.5804 | **+2.340** | **0.0193** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Clinically relevant depressive symptoms (CES-D-10 >= 10)  (domain: Depression; outcome sample N = 454; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0727**, LLR χ² = **31.17** (p = **5.49e-04**), AUC = **0.6723**, AIC = **419.7**, BIC = **465.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6675 | 0.9584 | ±1.9167 | -0.696 | 0.4861 | 0.5130 |  |
| Education: graduate level (vs college) | -0.3484 | 0.2760 | ±0.5519 | -1.263 | 0.2068 | 0.7058 |  |
| Education: high school or below (vs college) | +0.3263 | 0.4186 | ±0.8373 | +0.779 | 0.4357 | 1.3858 |  |
| Site: UCSD (vs UAB) | -0.0232 | 0.3406 | ±0.6813 | -0.068 | 0.9457 | 0.9771 |  |
| Site: UW (vs UAB) | +0.3928 | 0.3257 | ±0.6515 | +1.206 | 0.2279 | 1.4811 |  |
| **Age (years)** | **-0.0408** | 0.0128 | ±0.0257 | **-3.183** | **0.0015** | 0.9600 | ** |
| **BMI (kg/m2)** | **+0.0367** | 0.0167 | ±0.0335 | **+2.196** | **0.0281** | 1.0374 | * |
| Hypertension | +0.1940 | 0.2818 | ±0.5637 | +0.688 | 0.4912 | 1.2141 |  |
| High cholesterol | +0.4526 | 0.2693 | ±0.5386 | +1.681 | 0.0928 | 1.5724 | . |
| Kidney disease | +0.5026 | 0.5155 | ±1.0310 | +0.975 | 0.3296 | 1.6529 |  |
| Circulatory disease | +0.5851 | 0.3833 | ±0.7665 | +1.527 | 0.1269 | 1.7951 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0730**, LLR χ² = **31.30** (p = **9.88e-04**), AUC = **0.6715**, AIC = **421.6**, BIC = **471.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.4200 | 2.3442 | ±4.6884 | -0.606 | 0.5447 | 0.2417 |  |
| Education: graduate level (vs college) | -0.3423 | 0.2764 | ±0.5528 | -1.238 | 0.2156 | 0.7101 |  |
| Education: high school or below (vs college) | +0.3149 | 0.4205 | ±0.8411 | +0.749 | 0.4539 | 1.3702 |  |
| Site: UCSD (vs UAB) | -0.0150 | 0.3416 | ±0.6832 | -0.044 | 0.9649 | 0.9851 |  |
| Site: UW (vs UAB) | +0.3987 | 0.3265 | ±0.6531 | +1.221 | 0.2221 | 1.4899 |  |
| **Age (years)** | **-0.0412** | 0.0129 | ±0.0257 | **-3.198** | **0.0014** | 0.9597 | ** |
| **BMI (kg/m2)** | **+0.0360** | 0.0169 | ±0.0338 | **+2.127** | **0.0334** | 1.0366 | * |
| Hypertension | +0.1839 | 0.2833 | ±0.5667 | +0.649 | 0.5162 | 1.2019 |  |
| High cholesterol | +0.4344 | 0.2743 | ±0.5487 | +1.583 | 0.1133 | 1.5440 |  |
| Kidney disease | +0.5093 | 0.5169 | ±1.0337 | +0.985 | 0.3245 | 1.6641 |  |
| Circulatory disease | +0.5895 | 0.3839 | ±0.7677 | +1.536 | 0.1246 | 1.8031 |  |
| HbA1c (%) | +0.1437 | 0.4082 | ±0.8165 | +0.352 | 0.7248 | 1.1546 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0728**, LLR χ² = **31.23** (p = **0.0010**), AUC = **0.6732**, AIC = **421.6**, BIC = **471.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.1340 | 2.1404 | ±4.2807 | -0.530 | 0.5962 | 0.3217 |  |
| Education: graduate level (vs college) | -0.3473 | 0.2760 | ±0.5520 | -1.259 | 0.2082 | 0.7066 |  |
| Education: high school or below (vs college) | +0.3314 | 0.4192 | ±0.8384 | +0.791 | 0.4291 | 1.3930 |  |
| Site: UCSD (vs UAB) | -0.0233 | 0.3407 | ±0.6814 | -0.068 | 0.9455 | 0.9770 |  |
| Site: UW (vs UAB) | +0.3897 | 0.3261 | ±0.6523 | +1.195 | 0.2321 | 1.4765 |  |
| **Age (years)** | **-0.0407** | 0.0128 | ±0.0257 | **-3.172** | **0.0015** | 0.9601 | ** |
| **BMI (kg/m2)** | **+0.0365** | 0.0168 | ±0.0335 | **+2.177** | **0.0294** | 1.0372 | * |
| Hypertension | +0.1909 | 0.2822 | ±0.5644 | +0.676 | 0.4988 | 1.2103 |  |
| High cholesterol | +0.4548 | 0.2696 | ±0.5391 | +1.687 | 0.0916 | 1.5759 | . |
| Kidney disease | +0.4951 | 0.5165 | ±1.0330 | +0.959 | 0.3377 | 1.6407 |  |
| Circulatory disease | +0.5841 | 0.3832 | ±0.7663 | +1.524 | 0.1274 | 1.7933 |  |
| Mean glucose (mg/dL) | +0.0041 | 0.0168 | ±0.0335 | +0.244 | 0.8073 | 1.0041 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0728**, LLR χ² = **31.23** (p = **0.0010**), AUC = **0.6732**, AIC = **421.6**, BIC = **471.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.6997 | 4.3402 | ±8.6803 | -0.392 | 0.6953 | 0.1827 |  |
| Education: graduate level (vs college) | -0.3473 | 0.2760 | ±0.5520 | -1.259 | 0.2082 | 0.7066 |  |
| Education: high school or below (vs college) | +0.3314 | 0.4192 | ±0.8384 | +0.791 | 0.4291 | 1.3930 |  |
| Site: UCSD (vs UAB) | -0.0233 | 0.3407 | ±0.6814 | -0.068 | 0.9455 | 0.9770 |  |
| Site: UW (vs UAB) | +0.3897 | 0.3261 | ±0.6523 | +1.195 | 0.2321 | 1.4765 |  |
| **Age (years)** | **-0.0407** | 0.0128 | ±0.0257 | **-3.172** | **0.0015** | 0.9601 | ** |
| **BMI (kg/m2)** | **+0.0365** | 0.0168 | ±0.0335 | **+2.177** | **0.0294** | 1.0372 | * |
| Hypertension | +0.1909 | 0.2822 | ±0.5644 | +0.676 | 0.4988 | 1.2103 |  |
| High cholesterol | +0.4548 | 0.2696 | ±0.5391 | +1.687 | 0.0916 | 1.5759 | . |
| Kidney disease | +0.4951 | 0.5165 | ±1.0330 | +0.959 | 0.3377 | 1.6407 |  |
| Circulatory disease | +0.5841 | 0.3832 | ±0.7663 | +1.524 | 0.1274 | 1.7933 |  |
| GMI (%) | +0.1709 | 0.7006 | ±1.4013 | +0.244 | 0.8073 | 1.1864 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0731**, LLR χ² = **31.35** (p = **9.70e-04**), AUC = **0.6739**, AIC = **421.5**, BIC = **470.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3256 | 1.8396 | ±3.6792 | -0.721 | 0.4712 | 0.2656 |  |
| Education: graduate level (vs college) | -0.3443 | 0.2761 | ±0.5521 | -1.247 | 0.2123 | 0.7087 |  |
| Education: high school or below (vs college) | +0.3339 | 0.4195 | ±0.8390 | +0.796 | 0.4261 | 1.3964 |  |
| Site: UCSD (vs UAB) | -0.0286 | 0.3411 | ±0.6822 | -0.084 | 0.9332 | 0.9718 |  |
| Site: UW (vs UAB) | +0.3853 | 0.3266 | ±0.6532 | +1.180 | 0.2381 | 1.4700 |  |
| **Age (years)** | **-0.0400** | 0.0130 | ±0.0260 | **-3.075** | **0.0021** | 0.9608 | ** |
| **BMI (kg/m2)** | **+0.0358** | 0.0169 | ±0.0338 | **+2.117** | **0.0343** | 1.0364 | * |
| Hypertension | +0.1862 | 0.2826 | ±0.5651 | +0.659 | 0.5098 | 1.2047 |  |
| High cholesterol | +0.4531 | 0.2695 | ±0.5390 | +1.681 | 0.0927 | 1.5731 | . |
| Kidney disease | +0.5026 | 0.5157 | ±1.0314 | +0.975 | 0.3298 | 1.6530 |  |
| Circulatory disease | +0.5875 | 0.3829 | ±0.7659 | +1.534 | 0.1250 | 1.7995 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0055 | 0.0132 | ±0.0263 | +0.420 | 0.6745 | 1.0055 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0777**, LLR χ² = **33.33** (p = **4.65e-04**), AUC = **0.6792**, AIC = **419.5**, BIC = **469.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.0293 | 1.3382 | ±2.6763 | -1.517 | 0.1294 | 0.1314 |  |
| Education: graduate level (vs college) | -0.3201 | 0.2768 | ±0.5536 | -1.157 | 0.2474 | 0.7261 |  |
| Education: high school or below (vs college) | +0.3168 | 0.4215 | ±0.8431 | +0.752 | 0.4523 | 1.3727 |  |
| Site: UCSD (vs UAB) | +0.0157 | 0.3428 | ±0.6856 | +0.046 | 0.9635 | 1.0158 |  |
| Site: UW (vs UAB) | +0.4435 | 0.3292 | ±0.6584 | +1.347 | 0.1779 | 1.5581 |  |
| **Age (years)** | **-0.0412** | 0.0128 | ±0.0256 | **-3.215** | **0.0013** | 0.9596 | ** |
| **BMI (kg/m2)** | **+0.0362** | 0.0168 | ±0.0337 | **+2.147** | **0.0318** | 1.0368 | * |
| Hypertension | +0.1610 | 0.2843 | ±0.5686 | +0.566 | 0.5711 | 1.1747 |  |
| High cholesterol | +0.4747 | 0.2710 | ±0.5420 | +1.752 | 0.0798 | 1.6075 | . |
| Kidney disease | +0.3885 | 0.5299 | ±1.0598 | +0.733 | 0.4635 | 1.4747 |  |
| Circulatory disease | +0.5859 | 0.3845 | ±0.7690 | +1.524 | 0.1275 | 1.7967 |  |
| Glucose SD, pooled (mg/dL) | +0.0808 | 0.0553 | ±0.1106 | +1.462 | 0.1438 | 1.0842 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0783**, LLR χ² = **33.59** (p = **4.22e-04**), AUC = **0.6790**, AIC = **419.3**, BIC = **468.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.9462 | 1.2690 | ±2.5380 | -1.534 | 0.1251 | 0.1428 |  |
| Education: graduate level (vs college) | -0.3157 | 0.2769 | ±0.5539 | -1.140 | 0.2543 | 0.7293 |  |
| Education: high school or below (vs college) | +0.3325 | 0.4212 | ±0.8424 | +0.789 | 0.4298 | 1.3945 |  |
| Site: UCSD (vs UAB) | +0.0057 | 0.3421 | ±0.6841 | +0.017 | 0.9867 | 1.0057 |  |
| Site: UW (vs UAB) | +0.4380 | 0.3285 | ±0.6570 | +1.333 | 0.1824 | 1.5496 |  |
| **Age (years)** | **-0.0416** | 0.0129 | ±0.0257 | **-3.237** | **0.0012** | 0.9592 | ** |
| **BMI (kg/m2)** | **+0.0353** | 0.0169 | ±0.0339 | **+2.082** | **0.0373** | 1.0359 | * |
| Hypertension | +0.1719 | 0.2838 | ±0.5675 | +0.606 | 0.5447 | 1.1875 |  |
| High cholesterol | +0.4773 | 0.2714 | ±0.5428 | +1.759 | 0.0786 | 1.6117 | . |
| Kidney disease | +0.3854 | 0.5301 | ±1.0603 | +0.727 | 0.4672 | 1.4703 |  |
| Circulatory disease | +0.6011 | 0.3844 | ±0.7687 | +1.564 | 0.1179 | 1.8240 |  |
| Avg. daily SD (mg/dL) | +0.0855 | 0.0553 | ±0.1106 | +1.546 | 0.1221 | 1.0893 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0769**, LLR χ² = **32.96** (p = **5.33e-04**), AUC = **0.6763**, AIC = **419.9**, BIC = **469.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.8671 | 1.3166 | ±2.6331 | -1.418 | 0.1561 | 0.1546 |  |
| Education: graduate level (vs college) | -0.3245 | 0.2767 | ±0.5535 | -1.173 | 0.2410 | 0.7229 |  |
| Education: high school or below (vs college) | +0.3067 | 0.4213 | ±0.8426 | +0.728 | 0.4666 | 1.3589 |  |
| Site: UCSD (vs UAB) | +0.0113 | 0.3425 | ±0.6850 | +0.033 | 0.9738 | 1.0113 |  |
| Site: UW (vs UAB) | +0.4451 | 0.3292 | ±0.6584 | +1.352 | 0.1763 | 1.5607 |  |
| **Age (years)** | **-0.0414** | 0.0128 | ±0.0257 | **-3.224** | **0.0013** | 0.9594 | ** |
| **BMI (kg/m2)** | **+0.0369** | 0.0168 | ±0.0337 | **+2.189** | **0.0286** | 1.0375 | * |
| Hypertension | +0.1746 | 0.2834 | ±0.5669 | +0.616 | 0.5380 | 1.1907 |  |
| High cholesterol | +0.4678 | 0.2704 | ±0.5408 | +1.730 | 0.0836 | 1.5965 | . |
| Kidney disease | +0.4213 | 0.5266 | ±1.0533 | +0.800 | 0.4237 | 1.5240 |  |
| Circulatory disease | +0.5872 | 0.3847 | ±0.7693 | +1.526 | 0.1269 | 1.7989 |  |
| CV (%) | +0.0806 | 0.0604 | ±0.1207 | +1.336 | 0.1817 | 1.0840 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0764**, LLR χ² = **32.78** (p = **5.72e-04**), AUC = **0.6756**, AIC = **420.1**, BIC = **469.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.4295 | 1.2977 | ±2.5954 | +0.331 | 0.7407 | 1.5365 |  |
| Education: graduate level (vs college) | -0.3246 | 0.2767 | ±0.5534 | -1.173 | 0.2407 | 0.7228 |  |
| Education: high school or below (vs college) | +0.3023 | 0.4214 | ±0.8428 | +0.717 | 0.4731 | 1.3530 |  |
| Site: UCSD (vs UAB) | -0.0010 | 0.3416 | ±0.6832 | -0.003 | 0.9978 | 0.9990 |  |
| Site: UW (vs UAB) | +0.4324 | 0.3280 | ±0.6560 | +1.318 | 0.1874 | 1.5410 |  |
| **Age (years)** | **-0.0413** | 0.0128 | ±0.0257 | **-3.216** | **0.0013** | 0.9596 | ** |
| **BMI (kg/m2)** | **+0.0369** | 0.0168 | ±0.0336 | **+2.196** | **0.0281** | 1.0376 | * |
| Hypertension | +0.1766 | 0.2832 | ±0.5664 | +0.624 | 0.5329 | 1.1932 |  |
| High cholesterol | +0.4662 | 0.2702 | ±0.5403 | +1.726 | 0.0844 | 1.5939 | . |
| Kidney disease | +0.4454 | 0.5236 | ±1.0471 | +0.851 | 0.3949 | 1.5612 |  |
| Circulatory disease | +0.5923 | 0.3845 | ±0.7690 | +1.540 | 0.1235 | 1.8081 |  |
| Mean / SD ratio | -0.1601 | 0.1281 | ±0.2562 | -1.250 | 0.2113 | 0.8521 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0763**, LLR χ² = **32.73** (p = **5.83e-04**), AUC = **0.6759**, AIC = **420.1**, BIC = **469.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.3294 | 1.2585 | ±2.5170 | +0.262 | 0.7935 | 1.3902 |  |
| Education: graduate level (vs college) | -0.3226 | 0.2768 | ±0.5535 | -1.166 | 0.2438 | 0.7243 |  |
| Education: high school or below (vs college) | +0.3127 | 0.4207 | ±0.8413 | +0.743 | 0.4572 | 1.3671 |  |
| Site: UCSD (vs UAB) | -0.0123 | 0.3411 | ±0.6822 | -0.036 | 0.9713 | 0.9878 |  |
| Site: UW (vs UAB) | +0.4248 | 0.3272 | ±0.6545 | +1.298 | 0.1942 | 1.5293 |  |
| **Age (years)** | **-0.0416** | 0.0129 | ±0.0257 | **-3.233** | **0.0012** | 0.9593 | ** |
| **BMI (kg/m2)** | **+0.0361** | 0.0168 | ±0.0337 | **+2.141** | **0.0322** | 1.0367 | * |
| Hypertension | +0.1879 | 0.2829 | ±0.5658 | +0.664 | 0.5065 | 1.2068 |  |
| High cholesterol | +0.4631 | 0.2703 | ±0.5405 | +1.713 | 0.0866 | 1.5890 | . |
| Kidney disease | +0.4472 | 0.5228 | ±1.0457 | +0.855 | 0.3924 | 1.5639 |  |
| Circulatory disease | +0.6100 | 0.3844 | ±0.7689 | +1.587 | 0.1126 | 1.8404 |  |
| Avg. daily mean/SD | -0.1235 | 0.1012 | ±0.2023 | -1.221 | 0.2222 | 0.8838 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0983**, LLR χ² = **42.15** (p = **1.53e-05**), AUC = **0.7015**, AIC = **410.7**, BIC = **460.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.5854** | 1.3207 | ±2.6413 | **-2.715** | **0.0066** | 0.0277 | ** |
| Education: graduate level (vs college) | -0.3337 | 0.2797 | ±0.5595 | -1.193 | 0.2328 | 0.7162 |  |
| Education: high school or below (vs college) | +0.2176 | 0.4286 | ±0.8571 | +0.508 | 0.6117 | 1.2431 |  |
| Site: UCSD (vs UAB) | +0.0128 | 0.3444 | ±0.6889 | +0.037 | 0.9703 | 1.0129 |  |
| Site: UW (vs UAB) | +0.5094 | 0.3323 | ±0.6646 | +1.533 | 0.1253 | 1.6643 |  |
| **Age (years)** | **-0.0380** | 0.0129 | ±0.0257 | **-2.954** | **0.0031** | 0.9627 | ** |
| **BMI (kg/m2)** | **+0.0416** | 0.0173 | ±0.0345 | **+2.410** | **0.0159** | 1.0425 | * |
| Hypertension | +0.2476 | 0.2863 | ±0.5726 | +0.865 | 0.3871 | 1.2810 |  |
| High cholesterol | +0.4337 | 0.2730 | ±0.5459 | +1.589 | 0.1121 | 1.5429 |  |
| Kidney disease | +0.4400 | 0.5252 | ±1.0503 | +0.838 | 0.4021 | 1.5528 |  |
| Circulatory disease | +0.6625 | 0.3904 | ±0.7808 | +1.697 | 0.0897 | 1.9397 | . |
| **MAG (mg/dL/h)** | **+0.0728** | 0.0222 | ±0.0444 | **+3.283** | **0.0010** | 1.0755 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0813**, LLR χ² = **34.86** (p = **2.62e-04**), AUC = **0.6821**, AIC = **418.0**, BIC = **467.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.5277 | 1.3675 | ±2.7349 | -1.849 | 0.0645 | 0.0798 | . |
| Education: graduate level (vs college) | -0.3294 | 0.2770 | ±0.5540 | -1.189 | 0.2344 | 0.7194 |  |
| Education: high school or below (vs college) | +0.3109 | 0.4232 | ±0.8465 | +0.735 | 0.4626 | 1.3647 |  |
| Site: UCSD (vs UAB) | +0.0125 | 0.3423 | ±0.6847 | +0.037 | 0.9708 | 1.0126 |  |
| Site: UW (vs UAB) | +0.4466 | 0.3287 | ±0.6574 | +1.359 | 0.1743 | 1.5629 |  |
| **Age (years)** | **-0.0424** | 0.0129 | ±0.0259 | **-3.277** | **0.0010** | 0.9585 | ** |
| **BMI (kg/m2)** | **+0.0395** | 0.0168 | ±0.0336 | **+2.351** | **0.0187** | 1.0403 | * |
| Hypertension | +0.2147 | 0.2843 | ±0.5686 | +0.755 | 0.4502 | 1.2395 |  |
| High cholesterol | +0.4585 | 0.2715 | ±0.5429 | +1.689 | 0.0912 | 1.5818 | . |
| Kidney disease | +0.4237 | 0.5256 | ±1.0512 | +0.806 | 0.4202 | 1.5276 |  |
| Circulatory disease | +0.6095 | 0.3853 | ±0.7705 | +1.582 | 0.1136 | 1.8395 |  |
| Avg. daily range (mg/dL) | +0.0227 | 0.0119 | ±0.0239 | +1.900 | 0.0575 | 1.0229 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0750**, LLR χ² = **32.17** (p = **7.17e-04**), AUC = **0.6769**, AIC = **420.7**, BIC = **470.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.0396 | 1.0290 | ±2.0579 | -1.010 | 0.3124 | 0.3536 |  |
| Education: graduate level (vs college) | -0.3501 | 0.2763 | ±0.5526 | -1.267 | 0.2051 | 0.7046 |  |
| Education: high school or below (vs college) | +0.2991 | 0.4207 | ±0.8414 | +0.711 | 0.4771 | 1.3487 |  |
| Site: UCSD (vs UAB) | +0.0000 | 0.3422 | ±0.6845 | +0.000 | 0.9999 | 1.0000 |  |
| Site: UW (vs UAB) | +0.3961 | 0.3270 | ±0.6541 | +1.211 | 0.2258 | 1.4860 |  |
| **Age (years)** | **-0.0403** | 0.0128 | ±0.0256 | **-3.147** | **0.0016** | 0.9605 | ** |
| **BMI (kg/m2)** | **+0.0369** | 0.0168 | ±0.0335 | **+2.203** | **0.0276** | 1.0376 | * |
| Hypertension | +0.1654 | 0.2843 | ±0.5686 | +0.582 | 0.5608 | 1.1798 |  |
| High cholesterol | +0.4378 | 0.2701 | ±0.5401 | +1.621 | 0.1050 | 1.5493 |  |
| Kidney disease | +0.4905 | 0.5181 | ±1.0362 | +0.947 | 0.3438 | 1.6331 |  |
| Circulatory disease | +0.5665 | 0.3846 | ±0.7693 | +1.473 | 0.1408 | 1.7621 |  |
| SD of daily means (mg/dL) | +0.0666 | 0.0663 | ±0.1325 | +1.005 | 0.3149 | 1.0689 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0730**, LLR χ² = **31.31** (p = **9.84e-04**), AUC = **0.6727**, AIC = **421.6**, BIC = **471.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -16.2666 | 42.5670 | ±85.1340 | -0.382 | 0.7024 | 0.0000 |  |
| Education: graduate level (vs college) | -0.3520 | 0.2762 | ±0.5524 | -1.274 | 0.2025 | 0.7033 |  |
| Education: high school or below (vs college) | +0.3218 | 0.4191 | ±0.8383 | +0.768 | 0.4426 | 1.3796 |  |
| Site: UCSD (vs UAB) | -0.0300 | 0.3412 | ±0.6825 | -0.088 | 0.9300 | 0.9705 |  |
| Site: UW (vs UAB) | +0.3873 | 0.3264 | ±0.6527 | +1.187 | 0.2353 | 1.4730 |  |
| **Age (years)** | **-0.0408** | 0.0128 | ±0.0257 | **-3.180** | **0.0015** | 0.9600 | ** |
| **BMI (kg/m2)** | **+0.0365** | 0.0168 | ±0.0336 | **+2.177** | **0.0295** | 1.0372 | * |
| Hypertension | +0.1958 | 0.2819 | ±0.5638 | +0.695 | 0.4873 | 1.2163 |  |
| High cholesterol | +0.4549 | 0.2694 | ±0.5388 | +1.689 | 0.0913 | 1.5760 | . |
| Kidney disease | +0.5178 | 0.5169 | ±1.0338 | +1.002 | 0.3165 | 1.6783 |  |
| Circulatory disease | +0.5784 | 0.3838 | ±0.7676 | +1.507 | 0.1318 | 1.7832 |  |
| Time in range 70-180, pooled (%) | +0.1568 | 0.4277 | ±0.8555 | +0.367 | 0.7139 | 1.1697 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0732**, LLR χ² = **31.39** (p = **9.54e-04**), AUC = **0.6723**, AIC = **421.5**, BIC = **470.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +18.4090 | 40.5270 | ±81.0540 | +0.454 | 0.6497 | 98837030.4365 |  |
| Education: graduate level (vs college) | -0.3427 | 0.2762 | ±0.5525 | -1.241 | 0.2147 | 0.7099 |  |
| Education: high school or below (vs college) | +0.3318 | 0.4189 | ±0.8377 | +0.792 | 0.4283 | 1.3934 |  |
| Site: UCSD (vs UAB) | -0.0187 | 0.3407 | ±0.6815 | -0.055 | 0.9562 | 0.9815 |  |
| Site: UW (vs UAB) | +0.3951 | 0.3257 | ±0.6513 | +1.213 | 0.2250 | 1.4845 |  |
| **Age (years)** | **-0.0409** | 0.0128 | ±0.0257 | **-3.184** | **0.0015** | 0.9599 | ** |
| **BMI (kg/m2)** | **+0.0370** | 0.0167 | ±0.0335 | **+2.210** | **0.0271** | 1.0377 | * |
| Hypertension | +0.2005 | 0.2823 | ±0.5646 | +0.710 | 0.4776 | 1.2220 |  |
| High cholesterol | +0.4484 | 0.2696 | ±0.5392 | +1.663 | 0.0963 | 1.5658 | . |
| Kidney disease | +0.4911 | 0.5167 | ±1.0334 | +0.950 | 0.3419 | 1.6341 |  |
| Circulatory disease | +0.5884 | 0.3834 | ±0.7668 | +1.535 | 0.1249 | 1.8011 |  |
| Avg. daily time in range 70-180 (%) | -0.1916 | 0.4070 | ±0.8141 | -0.471 | 0.6378 | 0.8256 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0755**, LLR χ² = **32.39** (p = **6.61e-04**), AUC = **0.6782**, AIC = **420.5**, BIC = **469.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5665 | 0.9630 | ±1.9260 | -0.588 | 0.5564 | 0.5675 |  |
| Education: graduate level (vs college) | -0.3563 | 0.2765 | ±0.5530 | -1.289 | 0.1975 | 0.7003 |  |
| Education: high school or below (vs college) | +0.2950 | 0.4216 | ±0.8431 | +0.700 | 0.4841 | 1.3431 |  |
| Site: UCSD (vs UAB) | -0.0755 | 0.3444 | ±0.6888 | -0.219 | 0.8265 | 0.9273 |  |
| Site: UW (vs UAB) | +0.3649 | 0.3277 | ±0.6554 | +1.113 | 0.2656 | 1.4403 |  |
| **Age (years)** | **-0.0412** | 0.0129 | ±0.0257 | **-3.205** | **0.0014** | 0.9596 | ** |
| **BMI (kg/m2)** | **+0.0369** | 0.0167 | ±0.0334 | **+2.213** | **0.0269** | 1.0376 | * |
| Hypertension | +0.2207 | 0.2836 | ±0.5672 | +0.778 | 0.4365 | 1.2469 |  |
| High cholesterol | +0.4544 | 0.2702 | ±0.5404 | +1.682 | 0.0926 | 1.5752 | . |
| Kidney disease | +0.4605 | 0.5179 | ±1.0358 | +0.889 | 0.3739 | 1.5849 |  |
| Circulatory disease | +0.5935 | 0.3841 | ±0.7683 | +1.545 | 0.1224 | 1.8103 |  |
| Any reading < 54 during wear (0/1) | -0.3968 | 0.3700 | ±0.7400 | -1.073 | 0.2835 | 0.6724 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0774**, LLR χ² = **33.19** (p = **4.90e-04**), AUC = **0.6797**, AIC = **419.7**, BIC = **469.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5712 | 0.9584 | ±1.9167 | -0.596 | 0.5511 | 0.5648 |  |
| Education: graduate level (vs college) | -0.3576 | 0.2770 | ±0.5539 | -1.291 | 0.1967 | 0.6994 |  |
| Education: high school or below (vs college) | +0.2719 | 0.4223 | ±0.8446 | +0.644 | 0.5196 | 1.3125 |  |
| Site: UCSD (vs UAB) | -0.0788 | 0.3428 | ±0.6856 | -0.230 | 0.8181 | 0.9242 |  |
| Site: UW (vs UAB) | +0.3736 | 0.3273 | ±0.6545 | +1.142 | 0.2536 | 1.4530 |  |
| **Age (years)** | **-0.0420** | 0.0129 | ±0.0258 | **-3.258** | **0.0011** | 0.9589 | ** |
| **BMI (kg/m2)** | **+0.0385** | 0.0167 | ±0.0334 | **+2.302** | **0.0214** | 1.0392 | * |
| Hypertension | +0.2339 | 0.2843 | ±0.5685 | +0.823 | 0.4107 | 1.2635 |  |
| High cholesterol | +0.4401 | 0.2701 | ±0.5402 | +1.629 | 0.1032 | 1.5529 |  |
| Kidney disease | +0.4649 | 0.5179 | ±1.0358 | +0.898 | 0.3694 | 1.5919 |  |
| Circulatory disease | +0.6104 | 0.3846 | ±0.7692 | +1.587 | 0.1125 | 1.8412 |  |
| Time < 54 (%) | -3.6716 | 2.8489 | ±5.6977 | -1.289 | 0.1975 | 0.0254 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0733**, LLR χ² = **31.44** (p = **9.37e-04**), AUC = **0.6731**, AIC = **421.4**, BIC = **470.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6568 | 0.9578 | ±1.9156 | -0.686 | 0.4929 | 0.5185 |  |
| Education: graduate level (vs college) | -0.3491 | 0.2762 | ±0.5524 | -1.264 | 0.2063 | 0.7054 |  |
| Education: high school or below (vs college) | +0.3159 | 0.4196 | ±0.8392 | +0.753 | 0.4515 | 1.3715 |  |
| Site: UCSD (vs UAB) | -0.0319 | 0.3411 | ±0.6822 | -0.093 | 0.9256 | 0.9686 |  |
| Site: UW (vs UAB) | +0.3934 | 0.3262 | ±0.6523 | +1.206 | 0.2277 | 1.4820 |  |
| **Age (years)** | **-0.0409** | 0.0128 | ±0.0257 | **-3.186** | **0.0014** | 0.9599 | ** |
| **BMI (kg/m2)** | **+0.0371** | 0.0167 | ±0.0335 | **+2.217** | **0.0266** | 1.0378 | * |
| Hypertension | +0.1966 | 0.2822 | ±0.5643 | +0.697 | 0.4859 | 1.2173 |  |
| High cholesterol | +0.4509 | 0.2695 | ±0.5390 | +1.673 | 0.0943 | 1.5697 | . |
| Kidney disease | +0.4924 | 0.5162 | ±1.0325 | +0.954 | 0.3401 | 1.6363 |  |
| Circulatory disease | +0.6008 | 0.3845 | ±0.7690 | +1.563 | 0.1181 | 1.8236 |  |
| Avg. daily time < 54 (%) | -1.6434 | 3.3372 | ±6.6745 | -0.492 | 0.6224 | 0.1933 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0762**, LLR χ² = **32.67** (p = **5.95e-04**), AUC = **0.6802**, AIC = **420.2**, BIC = **469.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7946 | 0.9673 | ±1.9345 | -0.821 | 0.4114 | 0.4518 |  |
| Education: graduate level (vs college) | -0.3405 | 0.2765 | ±0.5531 | -1.231 | 0.2182 | 0.7114 |  |
| Education: high school or below (vs college) | +0.2904 | 0.4212 | ±0.8424 | +0.690 | 0.4905 | 1.3370 |  |
| Site: UCSD (vs UAB) | -0.0121 | 0.3410 | ±0.6819 | -0.035 | 0.9717 | 0.9880 |  |
| Site: UW (vs UAB) | +0.4218 | 0.3271 | ±0.6542 | +1.289 | 0.1972 | 1.5247 |  |
| **Age (years)** | **-0.0412** | 0.0129 | ±0.0257 | **-3.202** | **0.0014** | 0.9596 | ** |
| **BMI (kg/m2)** | **+0.0371** | 0.0168 | ±0.0337 | **+2.204** | **0.0275** | 1.0378 | * |
| Hypertension | +0.2163 | 0.2831 | ±0.5662 | +0.764 | 0.4450 | 1.2414 |  |
| High cholesterol | +0.4244 | 0.2706 | ±0.5413 | +1.568 | 0.1169 | 1.5286 |  |
| Kidney disease | +0.5455 | 0.5200 | ±1.0400 | +1.049 | 0.2942 | 1.7255 |  |
| Circulatory disease | +0.6002 | 0.3843 | ±0.7685 | +1.562 | 0.1183 | 1.8224 |  |
| Time 54-69, pooled (%) | +0.8272 | 0.6639 | ±1.3278 | +1.246 | 0.2128 | 2.2868 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0754**, LLR χ² = **32.33** (p = **6.75e-04**), AUC = **0.6768**, AIC = **420.5**, BIC = **470.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7471 | 0.9627 | ±1.9255 | -0.776 | 0.4378 | 0.4737 |  |
| Education: graduate level (vs college) | -0.3381 | 0.2765 | ±0.5530 | -1.223 | 0.2213 | 0.7131 |  |
| Education: high school or below (vs college) | +0.2890 | 0.4214 | ±0.8429 | +0.686 | 0.4929 | 1.3351 |  |
| Site: UCSD (vs UAB) | -0.0217 | 0.3408 | ±0.6816 | -0.064 | 0.9492 | 0.9785 |  |
| Site: UW (vs UAB) | +0.4096 | 0.3265 | ±0.6530 | +1.255 | 0.2096 | 1.5062 |  |
| **Age (years)** | **-0.0415** | 0.0129 | ±0.0258 | **-3.223** | **0.0013** | 0.9593 | ** |
| **BMI (kg/m2)** | **+0.0370** | 0.0168 | ±0.0336 | **+2.205** | **0.0274** | 1.0377 | * |
| Hypertension | +0.2353 | 0.2853 | ±0.5706 | +0.825 | 0.4094 | 1.2653 |  |
| High cholesterol | +0.4314 | 0.2704 | ±0.5407 | +1.596 | 0.1106 | 1.5395 |  |
| Kidney disease | +0.5390 | 0.5184 | ±1.0368 | +1.040 | 0.2985 | 1.7144 |  |
| Circulatory disease | +0.5842 | 0.3839 | ±0.7679 | +1.522 | 0.1281 | 1.7936 |  |
| Avg. daily time 54-69 (%) | +0.7435 | 0.6789 | ±1.3578 | +1.095 | 0.2735 | 2.1033 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0739**, LLR χ² = **31.68** (p = **8.59e-04**), AUC = **0.6757**, AIC = **421.2**, BIC = **470.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7453 | 0.9668 | ±1.9335 | -0.771 | 0.4407 | 0.4746 |  |
| Education: graduate level (vs college) | -0.3437 | 0.2762 | ±0.5524 | -1.244 | 0.2134 | 0.7091 |  |
| Education: high school or below (vs college) | +0.3164 | 0.4191 | ±0.8382 | +0.755 | 0.4504 | 1.3721 |  |
| Site: UCSD (vs UAB) | -0.0086 | 0.3413 | ±0.6826 | -0.025 | 0.9798 | 0.9914 |  |
| Site: UW (vs UAB) | +0.4107 | 0.3269 | ±0.6538 | +1.256 | 0.2090 | 1.5079 |  |
| **Age (years)** | **-0.0408** | 0.0128 | ±0.0257 | **-3.179** | **0.0015** | 0.9600 | ** |
| **BMI (kg/m2)** | **+0.0366** | 0.0168 | ±0.0336 | **+2.180** | **0.0292** | 1.0373 | * |
| Hypertension | +0.1985 | 0.2821 | ±0.5642 | +0.704 | 0.4815 | 1.2196 |  |
| High cholesterol | +0.4405 | 0.2699 | ±0.5398 | +1.632 | 0.1027 | 1.5535 |  |
| Kidney disease | +0.5283 | 0.5181 | ±1.0362 | +1.020 | 0.3079 | 1.6961 |  |
| Circulatory disease | +0.5896 | 0.3836 | ±0.7672 | +1.537 | 0.1243 | 1.8032 |  |
| Time < 70 (%) | +0.4260 | 0.5922 | ±1.1844 | +0.719 | 0.4719 | 1.5312 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0744**, LLR χ² = **31.92** (p = **7.85e-04**), AUC = **0.6756**, AIC = **421.0**, BIC = **470.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.7291 | 0.9624 | ±1.9249 | -0.758 | 0.4487 | 0.4824 |  |
| Education: graduate level (vs college) | -0.3414 | 0.2763 | ±0.5526 | -1.235 | 0.2167 | 0.7108 |  |
| Education: high school or below (vs college) | +0.3035 | 0.4201 | ±0.8402 | +0.722 | 0.4700 | 1.3546 |  |
| Site: UCSD (vs UAB) | -0.0182 | 0.3408 | ±0.6815 | -0.053 | 0.9575 | 0.9820 |  |
| Site: UW (vs UAB) | +0.4051 | 0.3263 | ±0.6525 | +1.242 | 0.2143 | 1.4995 |  |
| **Age (years)** | **-0.0413** | 0.0129 | ±0.0257 | **-3.209** | **0.0013** | 0.9595 | ** |
| **BMI (kg/m2)** | **+0.0368** | 0.0168 | ±0.0336 | **+2.192** | **0.0284** | 1.0375 | * |
| Hypertension | +0.2222 | 0.2842 | ±0.5684 | +0.782 | 0.4343 | 1.2488 |  |
| High cholesterol | +0.4380 | 0.2700 | ±0.5400 | +1.622 | 0.1048 | 1.5496 |  |
| Kidney disease | +0.5323 | 0.5178 | ±1.0355 | +1.028 | 0.3039 | 1.7029 |  |
| Circulatory disease | +0.5785 | 0.3838 | ±0.7677 | +1.507 | 0.1318 | 1.7834 |  |
| Avg. daily time < 70 (%) | +0.5432 | 0.6183 | ±1.2365 | +0.879 | 0.3796 | 1.7215 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0781**, LLR χ² = **33.49** (p = **4.39e-04**), AUC = **0.6805**, AIC = **419.4**, BIC = **468.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -392.0423 | 285.9276 | ±571.8551 | -1.371 | 0.1703 | 0.0000 |  |
| Education: graduate level (vs college) | -0.3608 | 0.2773 | ±0.5545 | -1.301 | 0.1932 | 0.6971 |  |
| Education: high school or below (vs college) | +0.2661 | 0.4226 | ±0.8451 | +0.630 | 0.5288 | 1.3049 |  |
| Site: UCSD (vs UAB) | -0.0840 | 0.3430 | ±0.6859 | -0.245 | 0.8066 | 0.9195 |  |
| Site: UW (vs UAB) | +0.3732 | 0.3276 | ±0.6551 | +1.139 | 0.2546 | 1.4524 |  |
| **Age (years)** | **-0.0422** | 0.0129 | ±0.0258 | **-3.274** | **0.0011** | 0.9587 | ** |
| **BMI (kg/m2)** | **+0.0384** | 0.0167 | ±0.0334 | **+2.295** | **0.0218** | 1.0391 | * |
| Hypertension | +0.2337 | 0.2842 | ±0.5684 | +0.822 | 0.4109 | 1.2633 |  |
| High cholesterol | +0.4432 | 0.2703 | ±0.5406 | +1.640 | 0.1011 | 1.5576 |  |
| Kidney disease | +0.4625 | 0.5180 | ±1.0360 | +0.893 | 0.3719 | 1.5880 |  |
| Circulatory disease | +0.6116 | 0.3847 | ±0.7694 | +1.590 | 0.1119 | 1.8435 |  |
| Time 54-250, pooled (%) | +3.9150 | 2.8599 | ±5.7199 | +1.369 | 0.1710 | 50.1472 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0738**, LLR χ² = **31.64** (p = **8.72e-04**), AUC = **0.6738**, AIC = **421.2**, BIC = **470.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -218.7709 | 342.3242 | ±684.6483 | -0.639 | 0.5228 | 0.0000 |  |
| Education: graduate level (vs college) | -0.3508 | 0.2765 | ±0.5530 | -1.269 | 0.2045 | 0.7041 |  |
| Education: high school or below (vs college) | +0.3110 | 0.4199 | ±0.8397 | +0.741 | 0.4588 | 1.3649 |  |
| Site: UCSD (vs UAB) | -0.0364 | 0.3413 | ±0.6826 | -0.107 | 0.9152 | 0.9643 |  |
| Site: UW (vs UAB) | +0.3933 | 0.3265 | ±0.6530 | +1.205 | 0.2284 | 1.4818 |  |
| **Age (years)** | **-0.0410** | 0.0128 | ±0.0257 | **-3.196** | **0.0014** | 0.9598 | ** |
| **BMI (kg/m2)** | **+0.0370** | 0.0167 | ±0.0335 | **+2.214** | **0.0268** | 1.0377 | * |
| Hypertension | +0.1955 | 0.2822 | ±0.5645 | +0.693 | 0.4885 | 1.2159 |  |
| High cholesterol | +0.4523 | 0.2696 | ±0.5393 | +1.677 | 0.0935 | 1.5719 | . |
| Kidney disease | +0.4895 | 0.5163 | ±1.0326 | +0.948 | 0.3432 | 1.6314 |  |
| Circulatory disease | +0.6054 | 0.3845 | ±0.7690 | +1.574 | 0.1154 | 1.8319 |  |
| Avg. daily time 54-250 (%) | +2.1813 | 3.4236 | ±6.8472 | +0.637 | 0.5240 | 8.8580 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0747**, LLR χ² = **32.02** (p = **7.58e-04**), AUC = **0.6782**, AIC = **420.9**, BIC = **470.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5280 | 0.9807 | ±1.9613 | -0.538 | 0.5903 | 0.5898 |  |
| Education: graduate level (vs college) | -0.3541 | 0.2763 | ±0.5526 | -1.281 | 0.2001 | 0.7018 |  |
| Education: high school or below (vs college) | +0.3054 | 0.4202 | ±0.8404 | +0.727 | 0.4673 | 1.3572 |  |
| Site: UCSD (vs UAB) | -0.0270 | 0.3410 | ±0.6819 | -0.079 | 0.9370 | 0.9734 |  |
| Site: UW (vs UAB) | +0.3951 | 0.3266 | ±0.6532 | +1.210 | 0.2264 | 1.4845 |  |
| **Age (years)** | **-0.0408** | 0.0129 | ±0.0257 | **-3.172** | **0.0015** | 0.9601 | ** |
| **BMI (kg/m2)** | **+0.0361** | 0.0169 | ±0.0339 | **+2.128** | **0.0333** | 1.0367 | * |
| Hypertension | +0.2039 | 0.2823 | ±0.5645 | +0.722 | 0.4701 | 1.2262 |  |
| High cholesterol | +0.4468 | 0.2695 | ±0.5389 | +1.658 | 0.0973 | 1.5633 | . |
| Kidney disease | +0.5676 | 0.5210 | ±1.0421 | +1.089 | 0.2760 | 1.7641 |  |
| Circulatory disease | +0.5717 | 0.3841 | ±0.7683 | +1.488 | 0.1367 | 1.7712 |  |
| Time 181-250, pooled (%) | -0.4291 | 0.4705 | ±0.9410 | -0.912 | 0.3618 | 0.6511 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0727**, LLR χ² = **31.18** (p = **0.0010**), AUC = **0.6725**, AIC = **421.7**, BIC = **471.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6571 | 0.9711 | ±1.9421 | -0.677 | 0.4986 | 0.5184 |  |
| Education: graduate level (vs college) | -0.3489 | 0.2761 | ±0.5522 | -1.264 | 0.2063 | 0.7055 |  |
| Education: high school or below (vs college) | +0.3243 | 0.4197 | ±0.8394 | +0.773 | 0.4396 | 1.3831 |  |
| Site: UCSD (vs UAB) | -0.0236 | 0.3407 | ±0.6814 | -0.069 | 0.9449 | 0.9767 |  |
| Site: UW (vs UAB) | +0.3930 | 0.3258 | ±0.6516 | +1.206 | 0.2277 | 1.4815 |  |
| **Age (years)** | **-0.0409** | 0.0128 | ±0.0257 | **-3.183** | **0.0015** | 0.9600 | ** |
| **BMI (kg/m2)** | **+0.0367** | 0.0167 | ±0.0335 | **+2.192** | **0.0284** | 1.0374 | * |
| Hypertension | +0.1945 | 0.2819 | ±0.5639 | +0.690 | 0.4902 | 1.2147 |  |
| High cholesterol | +0.4525 | 0.2693 | ±0.5386 | +1.680 | 0.0929 | 1.5722 | . |
| Kidney disease | +0.5059 | 0.5178 | ±1.0357 | +0.977 | 0.3286 | 1.6585 |  |
| Circulatory disease | +0.5842 | 0.3835 | ±0.7670 | +1.523 | 0.1277 | 1.7935 |  |
| Avg. daily time 181-250 (%) | -0.0306 | 0.4548 | ±0.9097 | -0.067 | 0.9463 | 0.9698 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0747**, LLR χ² = **32.06** (p = **7.47e-04**), AUC = **0.6780**, AIC = **420.8**, BIC = **470.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.5222 | 0.9815 | ±1.9630 | -0.532 | 0.5947 | 0.5932 |  |
| Education: graduate level (vs college) | -0.3544 | 0.2763 | ±0.5527 | -1.282 | 0.1997 | 0.7016 |  |
| Education: high school or below (vs college) | +0.3046 | 0.4202 | ±0.8405 | +0.725 | 0.4685 | 1.3561 |  |
| Site: UCSD (vs UAB) | -0.0275 | 0.3410 | ±0.6820 | -0.081 | 0.9357 | 0.9729 |  |
| Site: UW (vs UAB) | +0.3950 | 0.3266 | ±0.6533 | +1.209 | 0.2266 | 1.4843 |  |
| **Age (years)** | **-0.0408** | 0.0129 | ±0.0257 | **-3.174** | **0.0015** | 0.9600 | ** |
| **BMI (kg/m2)** | **+0.0360** | 0.0170 | ±0.0339 | **+2.125** | **0.0336** | 1.0367 | * |
| Hypertension | +0.2038 | 0.2822 | ±0.5645 | +0.722 | 0.4702 | 1.2261 |  |
| High cholesterol | +0.4470 | 0.2695 | ±0.5389 | +1.659 | 0.0972 | 1.5636 | . |
| Kidney disease | +0.5690 | 0.5211 | ±1.0421 | +1.092 | 0.2748 | 1.7666 |  |
| Circulatory disease | +0.5714 | 0.3842 | ±0.7683 | +1.487 | 0.1369 | 1.7707 |  |
| Time > 180 (%) | -0.4384 | 0.4698 | ±0.9397 | -0.933 | 0.3508 | 0.6451 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0727**, LLR χ² = **31.18** (p = **0.0010**), AUC = **0.6726**, AIC = **421.7**, BIC = **471.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.6530 | 0.9717 | ±1.9433 | -0.672 | 0.5016 | 0.5205 |  |
| Education: graduate level (vs college) | -0.3491 | 0.2761 | ±0.5522 | -1.265 | 0.2061 | 0.7053 |  |
| Education: high school or below (vs college) | +0.3236 | 0.4197 | ±0.8394 | +0.771 | 0.4407 | 1.3821 |  |
| Site: UCSD (vs UAB) | -0.0237 | 0.3407 | ±0.6814 | -0.070 | 0.9445 | 0.9765 |  |
| Site: UW (vs UAB) | +0.3931 | 0.3258 | ±0.6516 | +1.207 | 0.2276 | 1.4816 |  |
| **Age (years)** | **-0.0409** | 0.0128 | ±0.0257 | **-3.184** | **0.0015** | 0.9600 | ** |
| **BMI (kg/m2)** | **+0.0367** | 0.0167 | ±0.0335 | **+2.191** | **0.0284** | 1.0374 | * |
| Hypertension | +0.1947 | 0.2819 | ±0.5639 | +0.691 | 0.4899 | 1.2149 |  |
| High cholesterol | +0.4524 | 0.2693 | ±0.5385 | +1.680 | 0.0929 | 1.5722 | . |
| Kidney disease | +0.5071 | 0.5178 | ±1.0356 | +0.979 | 0.3274 | 1.6605 |  |
| Circulatory disease | +0.5838 | 0.3835 | ±0.7671 | +1.522 | 0.1280 | 1.7929 |  |
| Avg. daily time > 180 (%) | -0.0418 | 0.4540 | ±0.9079 | -0.092 | 0.9265 | 0.9590 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 454)
**Regression Call / Formula**: `cesd10_ge10 ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **454**, events = **82**, McFadden pseudo-R² = **0.0787**, LLR χ² = **33.75** (p = **3.98e-04**), AUC = **0.6815**, AIC = **419.1**, BIC = **468.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -0.8933 | 0.9719 | ±1.9437 | -0.919 | 0.3580 | 0.4093 |  |
| Education: graduate level (vs college) | -0.3301 | 0.2776 | ±0.5552 | -1.189 | 0.2344 | 0.7188 |  |
| Education: high school or below (vs college) | +0.3345 | 0.4218 | ±0.8435 | +0.793 | 0.4277 | 1.3973 |  |
| Site: UCSD (vs UAB) | -0.0214 | 0.3415 | ±0.6831 | -0.063 | 0.9500 | 0.9788 |  |
| Site: UW (vs UAB) | +0.3823 | 0.3276 | ±0.6552 | +1.167 | 0.2432 | 1.4657 |  |
| **Age (years)** | **-0.0370** | 0.0130 | ±0.0260 | **-2.853** | **0.0043** | 0.9637 | ** |
| **BMI (kg/m2)** | **+0.0352** | 0.0169 | ±0.0337 | **+2.089** | **0.0367** | 1.0358 | * |
| Hypertension | +0.1494 | 0.2842 | ±0.5684 | +0.526 | 0.5991 | 1.1611 |  |
| High cholesterol | +0.4348 | 0.2701 | ±0.5403 | +1.609 | 0.1075 | 1.5446 |  |
| Kidney disease | +0.4667 | 0.5201 | ±1.0403 | +0.897 | 0.3695 | 1.5948 |  |
| Circulatory disease | +0.6224 | 0.3848 | ±0.7696 | +1.617 | 0.1058 | 1.8633 |  |
| Nocturnal time > 180 (%) | +0.4865 | 0.2969 | ±0.5938 | +1.639 | 0.1013 | 1.6266 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor PM2.5, log(1 + mean ug/m3)  (domain: Home environment; outcome sample N = 443; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **443**, R² = **0.1362**, Adj R² = **0.1101**, F-statistic = **5.21** (p = **1.17e-08**), Residual SE = **0.854** on **429** df, AIC = **1130.8**, BIC = **1188.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7378** | 0.2737 | ±0.5474 | **+6.349** | **2.16e-10** | *** |
| Education: graduate level (vs college) | -0.1039 | 0.0874 | ±0.1747 | -1.189 | 0.2344 |  |
| Education: high school or below (vs college) | +0.3335 | 0.1766 | ±0.3532 | +1.888 | 0.0590 | . |
| Site: UCSD (vs UAB) | +0.0536 | 0.1065 | ±0.2129 | +0.504 | 0.6143 |  |
| **Site: UW (vs UAB)** | **-0.3188** | 0.1156 | ±0.2313 | **-2.757** | **0.0058** | ** |
| Season: spring (vs autumn) | -0.1062 | 0.1119 | ±0.2238 | -0.949 | 0.3426 |  |
| Season: summer (vs autumn) | +0.2150 | 0.1294 | ±0.2589 | +1.661 | 0.0968 | . |
| Season: winter (vs autumn) | -0.0103 | 0.1180 | ±0.2359 | -0.087 | 0.9305 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0070 | **-2.018** | **0.0436** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0132 | **+3.160** | **0.0016** | ** |
| Hypertension | +0.0847 | 0.0947 | ±0.1894 | +0.894 | 0.3711 |  |
| High cholesterol | -0.0542 | 0.0818 | ±0.1635 | -0.663 | 0.5075 |  |
| Kidney disease | -0.1076 | 0.1694 | ±0.3388 | -0.635 | 0.5254 |  |
| Circulatory disease | +0.2827 | 0.1624 | ±0.3247 | +1.741 | 0.0817 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **443**, R² = **0.1383**, Adj R² = **0.1101**, F-statistic = **4.91** (p = **1.81e-08**), Residual SE = **0.854** on **428** df, AIC = **1131.8**, BIC = **1193.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.9996 | 0.8884 | ±1.7768 | +1.125 | 0.2605 |  |
| Education: graduate level (vs college) | -0.1004 | 0.0875 | ±0.1749 | -1.149 | 0.2507 |  |
| Education: high school or below (vs college) | +0.3232 | 0.1771 | ±0.3541 | +1.826 | 0.0679 | . |
| Site: UCSD (vs UAB) | +0.0520 | 0.1069 | ±0.2138 | +0.486 | 0.6267 |  |
| **Site: UW (vs UAB)** | **-0.3170** | 0.1157 | ±0.2314 | **-2.739** | **0.0062** | ** |
| Season: spring (vs autumn) | -0.0878 | 0.1117 | ±0.2234 | -0.786 | 0.4317 |  |
| Season: summer (vs autumn) | +0.2080 | 0.1307 | ±0.2614 | +1.592 | 0.1114 |  |
| Season: winter (vs autumn) | -0.0036 | 0.1180 | ±0.2361 | -0.030 | 0.9760 |  |
| **Age (years)** | **-0.0075** | 0.0036 | ±0.0072 | **-2.083** | **0.0372** | * |
| **BMI (kg/m2)** | **+0.0202** | 0.0066 | ±0.0132 | **+3.051** | **0.0023** | ** |
| Hypertension | +0.0766 | 0.0958 | ±0.1916 | +0.799 | 0.4242 |  |
| High cholesterol | -0.0728 | 0.0840 | ±0.1679 | -0.867 | 0.3862 |  |
| Kidney disease | -0.0986 | 0.1728 | ±0.3455 | -0.571 | 0.5680 |  |
| Circulatory disease | +0.2902 | 0.1633 | ±0.3266 | +1.777 | 0.0756 | . |
| HbA1c (%) | +0.1418 | 0.1634 | ±0.3267 | +0.868 | 0.3856 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **443**, R² = **0.1403**, Adj R² = **0.1121**, F-statistic = **4.99** (p = **1.21e-08**), Residual SE = **0.853** on **428** df, AIC = **1130.8**, BIC = **1192.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.6155** | 0.7110 | ±1.4219 | **+3.679** | **2.34e-04** | *** |
| Education: graduate level (vs college) | -0.1021 | 0.0875 | ±0.1749 | -1.168 | 0.2428 |  |
| Education: high school or below (vs college) | +0.3258 | 0.1751 | ±0.3502 | +1.861 | 0.0627 | . |
| Site: UCSD (vs UAB) | +0.0607 | 0.1070 | ±0.2141 | +0.567 | 0.5705 |  |
| **Site: UW (vs UAB)** | **-0.3104** | 0.1158 | ±0.2317 | **-2.679** | **0.0074** | ** |
| Season: spring (vs autumn) | -0.1136 | 0.1119 | ±0.2238 | -1.015 | 0.3099 |  |
| Season: summer (vs autumn) | +0.2139 | 0.1290 | ±0.2579 | +1.659 | 0.0971 | . |
| Season: winter (vs autumn) | -0.0158 | 0.1182 | ±0.2365 | -0.134 | 0.8935 |  |
| **Age (years)** | **-0.0073** | 0.0036 | ±0.0071 | **-2.035** | **0.0418** | * |
| **BMI (kg/m2)** | **+0.0214** | 0.0066 | ±0.0132 | **+3.255** | **0.0011** | ** |
| Hypertension | +0.0923 | 0.0956 | ±0.1912 | +0.965 | 0.3344 |  |
| High cholesterol | -0.0589 | 0.0820 | ±0.1641 | -0.718 | 0.4725 |  |
| Kidney disease | -0.0995 | 0.1705 | ±0.3410 | -0.584 | 0.5595 |  |
| Circulatory disease | +0.2837 | 0.1626 | ±0.3252 | +1.745 | 0.0810 | . |
| Mean glucose (mg/dL) | -0.0077 | 0.0054 | ±0.0107 | -1.447 | 0.1478 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **443**, R² = **0.1403**, Adj R² = **0.1121**, F-statistic = **4.99** (p = **1.21e-08**), Residual SE = **0.853** on **428** df, AIC = **1130.8**, BIC = **1192.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+3.6879** | 1.4243 | ±2.8487 | **+2.589** | **0.0096** | ** |
| Education: graduate level (vs college) | -0.1021 | 0.0875 | ±0.1749 | -1.168 | 0.2428 |  |
| Education: high school or below (vs college) | +0.3258 | 0.1751 | ±0.3502 | +1.861 | 0.0627 | . |
| Site: UCSD (vs UAB) | +0.0607 | 0.1070 | ±0.2141 | +0.567 | 0.5705 |  |
| **Site: UW (vs UAB)** | **-0.3104** | 0.1158 | ±0.2317 | **-2.679** | **0.0074** | ** |
| Season: spring (vs autumn) | -0.1136 | 0.1119 | ±0.2238 | -1.015 | 0.3099 |  |
| Season: summer (vs autumn) | +0.2139 | 0.1290 | ±0.2579 | +1.659 | 0.0971 | . |
| Season: winter (vs autumn) | -0.0158 | 0.1182 | ±0.2365 | -0.134 | 0.8935 |  |
| **Age (years)** | **-0.0073** | 0.0036 | ±0.0071 | **-2.035** | **0.0418** | * |
| **BMI (kg/m2)** | **+0.0214** | 0.0066 | ±0.0132 | **+3.255** | **0.0011** | ** |
| Hypertension | +0.0923 | 0.0956 | ±0.1912 | +0.965 | 0.3344 |  |
| High cholesterol | -0.0589 | 0.0820 | ±0.1641 | -0.718 | 0.4725 |  |
| Kidney disease | -0.0995 | 0.1705 | ±0.3410 | -0.584 | 0.5595 |  |
| Circulatory disease | +0.2837 | 0.1626 | ±0.3252 | +1.745 | 0.0810 | . |
| GMI (%) | -0.3240 | 0.2238 | ±0.4477 | -1.447 | 0.1478 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **443**, R² = **0.1378**, Adj R² = **0.1096**, F-statistic = **4.89** (p = **2.00e-08**), Residual SE = **0.854** on **428** df, AIC = **1132.0**, BIC = **1193.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+2.1820** | 0.5934 | ±1.1868 | **+3.677** | **2.36e-04** | *** |
| Education: graduate level (vs college) | -0.1062 | 0.0880 | ±0.1760 | -1.207 | 0.2273 |  |
| Education: high school or below (vs college) | +0.3273 | 0.1767 | ±0.3533 | +1.853 | 0.0639 | . |
| Site: UCSD (vs UAB) | +0.0627 | 0.1084 | ±0.2168 | +0.579 | 0.5629 |  |
| **Site: UW (vs UAB)** | **-0.3107** | 0.1168 | ±0.2335 | **-2.661** | **0.0078** | ** |
| Season: spring (vs autumn) | -0.1094 | 0.1123 | ±0.2245 | -0.975 | 0.3298 |  |
| Season: summer (vs autumn) | +0.2150 | 0.1294 | ±0.2587 | +1.662 | 0.0965 | . |
| Season: winter (vs autumn) | -0.0120 | 0.1184 | ±0.2368 | -0.101 | 0.9196 |  |
| **Age (years)** | **-0.0076** | 0.0037 | ±0.0074 | **-2.062** | **0.0392** | * |
| **BMI (kg/m2)** | **+0.0217** | 0.0066 | ±0.0132 | **+3.300** | **9.68e-04** | *** |
| Hypertension | +0.0895 | 0.0958 | ±0.1916 | +0.934 | 0.3501 |  |
| High cholesterol | -0.0551 | 0.0820 | ±0.1641 | -0.671 | 0.5021 |  |
| Kidney disease | -0.1108 | 0.1695 | ±0.3390 | -0.654 | 0.5133 |  |
| Circulatory disease | +0.2814 | 0.1635 | ±0.3269 | +1.721 | 0.0852 | . |
| Nocturnal mean 00-06h (mg/dL) | -0.0039 | 0.0042 | ±0.0084 | -0.921 | 0.3573 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **443**, R² = **0.1364**, Adj R² = **0.1082**, F-statistic = **4.83** (p = **2.67e-08**), Residual SE = **0.855** on **428** df, AIC = **1132.7**, BIC = **1194.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8229** | 0.3992 | ±0.7984 | **+4.566** | **4.96e-06** | *** |
| Education: graduate level (vs college) | -0.1053 | 0.0881 | ±0.1762 | -1.196 | 0.2319 |  |
| Education: high school or below (vs college) | +0.3340 | 0.1767 | ±0.3534 | +1.891 | 0.0587 | . |
| Site: UCSD (vs UAB) | +0.0517 | 0.1066 | ±0.2132 | +0.485 | 0.6275 |  |
| **Site: UW (vs UAB)** | **-0.3208** | 0.1156 | ±0.2313 | **-2.775** | **0.0055** | ** |
| Season: spring (vs autumn) | -0.1047 | 0.1125 | ±0.2251 | -0.931 | 0.3521 |  |
| Season: summer (vs autumn) | +0.2154 | 0.1296 | ±0.2593 | +1.662 | 0.0966 | . |
| Season: winter (vs autumn) | -0.0082 | 0.1197 | ±0.2394 | -0.069 | 0.9453 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0071 | **-2.006** | **0.0449** | * |
| **BMI (kg/m2)** | **+0.0210** | 0.0066 | ±0.0132 | **+3.176** | **0.0015** | ** |
| Hypertension | +0.0865 | 0.0954 | ±0.1907 | +0.906 | 0.3647 |  |
| High cholesterol | -0.0557 | 0.0825 | ±0.1650 | -0.675 | 0.4995 |  |
| Kidney disease | -0.1030 | 0.1690 | ±0.3380 | -0.609 | 0.5422 |  |
| Circulatory disease | +0.2841 | 0.1626 | ±0.3253 | +1.747 | 0.0807 | . |
| Glucose SD, pooled (mg/dL) | -0.0053 | 0.0172 | ±0.0344 | -0.306 | 0.7593 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **443**, R² = **0.1363**, Adj R² = **0.1081**, F-statistic = **4.83** (p = **2.73e-08**), Residual SE = **0.855** on **428** df, AIC = **1132.8**, BIC = **1194.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7868** | 0.3712 | ±0.7424 | **+4.814** | **1.48e-06** | *** |
| Education: graduate level (vs college) | -0.1050 | 0.0884 | ±0.1767 | -1.189 | 0.2346 |  |
| Education: high school or below (vs college) | +0.3332 | 0.1766 | ±0.3532 | +1.887 | 0.0592 | . |
| Site: UCSD (vs UAB) | +0.0527 | 0.1067 | ±0.2134 | +0.494 | 0.6211 |  |
| **Site: UW (vs UAB)** | **-0.3199** | 0.1156 | ±0.2313 | **-2.766** | **0.0057** | ** |
| Season: spring (vs autumn) | -0.1056 | 0.1124 | ±0.2249 | -0.939 | 0.3477 |  |
| Season: summer (vs autumn) | +0.2150 | 0.1297 | ±0.2593 | +1.658 | 0.0973 | . |
| Season: winter (vs autumn) | -0.0097 | 0.1188 | ±0.2376 | -0.082 | 0.9347 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0071 | **-2.003** | **0.0452** | * |
| **BMI (kg/m2)** | **+0.0210** | 0.0066 | ±0.0132 | **+3.188** | **0.0014** | ** |
| Hypertension | +0.0854 | 0.0952 | ±0.1905 | +0.896 | 0.3700 |  |
| High cholesterol | -0.0551 | 0.0825 | ±0.1649 | -0.668 | 0.5044 |  |
| Kidney disease | -0.1047 | 0.1688 | ±0.3376 | -0.620 | 0.5352 |  |
| Circulatory disease | +0.2828 | 0.1628 | ±0.3256 | +1.737 | 0.0823 | . |
| Avg. daily SD (mg/dL) | -0.0034 | 0.0166 | ±0.0332 | -0.205 | 0.8373 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **443**, R² = **0.1365**, Adj R² = **0.1082**, F-statistic = **4.83** (p = **2.63e-08**), Residual SE = **0.855** on **428** df, AIC = **1132.7**, BIC = **1194.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6404** | 0.3798 | ±0.7597 | **+4.319** | **1.57e-05** | *** |
| Education: graduate level (vs college) | -0.1020 | 0.0879 | ±0.1759 | -1.160 | 0.2460 |  |
| Education: high school or below (vs college) | +0.3320 | 0.1768 | ±0.3536 | +1.878 | 0.0604 | . |
| Site: UCSD (vs UAB) | +0.0566 | 0.1071 | ±0.2142 | +0.529 | 0.5971 |  |
| **Site: UW (vs UAB)** | **-0.3155** | 0.1159 | ±0.2319 | **-2.722** | **0.0065** | ** |
| Season: spring (vs autumn) | -0.1088 | 0.1121 | ±0.2242 | -0.970 | 0.3319 |  |
| Season: summer (vs autumn) | +0.2141 | 0.1297 | ±0.2595 | +1.650 | 0.0989 | . |
| Season: winter (vs autumn) | -0.0133 | 0.1198 | ±0.2396 | -0.111 | 0.9114 |  |
| **Age (years)** | **-0.0072** | 0.0035 | ±0.0071 | **-2.015** | **0.0439** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0133 | **+3.154** | **0.0016** | ** |
| Hypertension | +0.0837 | 0.0947 | ±0.1895 | +0.883 | 0.3772 |  |
| High cholesterol | -0.0529 | 0.0823 | ±0.1646 | -0.643 | 0.5202 |  |
| Kidney disease | -0.1118 | 0.1684 | ±0.3369 | -0.663 | 0.5070 |  |
| Circulatory disease | +0.2811 | 0.1626 | ±0.3253 | +1.728 | 0.0839 | . |
| CV (%) | +0.0068 | 0.0191 | ±0.0381 | +0.356 | 0.7220 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **443**, R² = **0.1363**, Adj R² = **0.1080**, F-statistic = **4.82** (p = **2.74e-08**), Residual SE = **0.855** on **428** df, AIC = **1132.8**, BIC = **1194.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7843** | 0.3907 | ±0.7814 | **+4.567** | **4.95e-06** | *** |
| Education: graduate level (vs college) | -0.1029 | 0.0880 | ±0.1761 | -1.168 | 0.2427 |  |
| Education: high school or below (vs college) | +0.3326 | 0.1768 | ±0.3536 | +1.881 | 0.0599 | . |
| Site: UCSD (vs UAB) | +0.0548 | 0.1071 | ±0.2141 | +0.512 | 0.6086 |  |
| **Site: UW (vs UAB)** | **-0.3175** | 0.1160 | ±0.2320 | **-2.736** | **0.0062** | ** |
| Season: spring (vs autumn) | -0.1075 | 0.1123 | ±0.2245 | -0.958 | 0.3381 |  |
| Season: summer (vs autumn) | +0.2146 | 0.1297 | ±0.2594 | +1.655 | 0.0980 | . |
| Season: winter (vs autumn) | -0.0117 | 0.1196 | ±0.2391 | -0.098 | 0.9220 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0071 | **-2.012** | **0.0442** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0133 | **+3.155** | **0.0016** | ** |
| Hypertension | +0.0842 | 0.0948 | ±0.1896 | +0.888 | 0.3745 |  |
| High cholesterol | -0.0535 | 0.0823 | ±0.1645 | -0.651 | 0.5153 |  |
| Kidney disease | -0.1090 | 0.1690 | ±0.3380 | -0.645 | 0.5189 |  |
| Circulatory disease | +0.2822 | 0.1626 | ±0.3253 | +1.735 | 0.0827 | . |
| Mean / SD ratio | -0.0066 | 0.0378 | ±0.0757 | -0.174 | 0.8619 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **443**, R² = **0.1368**, Adj R² = **0.1085**, F-statistic = **4.84** (p = **2.49e-08**), Residual SE = **0.854** on **428** df, AIC = **1132.6**, BIC = **1194.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8670** | 0.3754 | ±0.7507 | **+4.974** | **6.57e-07** | *** |
| Education: graduate level (vs college) | -0.1002 | 0.0883 | ±0.1765 | -1.136 | 0.2561 |  |
| Education: high school or below (vs college) | +0.3322 | 0.1769 | ±0.3539 | +1.877 | 0.0605 | . |
| Site: UCSD (vs UAB) | +0.0561 | 0.1069 | ±0.2139 | +0.524 | 0.6000 |  |
| **Site: UW (vs UAB)** | **-0.3157** | 0.1158 | ±0.2317 | **-2.725** | **0.0064** | ** |
| Season: spring (vs autumn) | -0.1099 | 0.1121 | ±0.2242 | -0.981 | 0.3267 |  |
| Season: summer (vs autumn) | +0.2136 | 0.1297 | ±0.2595 | +1.646 | 0.0997 | . |
| Season: winter (vs autumn) | -0.0130 | 0.1191 | ±0.2382 | -0.109 | 0.9129 |  |
| **Age (years)** | **-0.0072** | 0.0036 | ±0.0071 | **-2.026** | **0.0428** | * |
| **BMI (kg/m2)** | **+0.0208** | 0.0066 | ±0.0132 | **+3.141** | **0.0017** | ** |
| Hypertension | +0.0842 | 0.0948 | ±0.1895 | +0.889 | 0.3742 |  |
| High cholesterol | -0.0528 | 0.0821 | ±0.1643 | -0.643 | 0.5205 |  |
| Kidney disease | -0.1120 | 0.1685 | ±0.3371 | -0.665 | 0.5063 |  |
| Circulatory disease | +0.2837 | 0.1624 | ±0.3248 | +1.747 | 0.0807 | . |
| Avg. daily mean/SD | -0.0154 | 0.0291 | ±0.0582 | -0.530 | 0.5958 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **443**, R² = **0.1393**, Adj R² = **0.1111**, F-statistic = **4.95** (p = **1.48e-08**), Residual SE = **0.853** on **428** df, AIC = **1131.3**, BIC = **1192.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.4013** | 0.3789 | ±0.7578 | **+3.699** | **2.17e-04** | *** |
| Education: graduate level (vs college) | -0.1060 | 0.0873 | ±0.1745 | -1.215 | 0.2244 |  |
| Education: high school or below (vs college) | +0.3187 | 0.1778 | ±0.3556 | +1.792 | 0.0731 | . |
| Site: UCSD (vs UAB) | +0.0592 | 0.1063 | ±0.2126 | +0.556 | 0.5779 |  |
| **Site: UW (vs UAB)** | **-0.3054** | 0.1165 | ±0.2329 | **-2.622** | **0.0087** | ** |
| Season: spring (vs autumn) | -0.1063 | 0.1115 | ±0.2230 | -0.953 | 0.3405 |  |
| Season: summer (vs autumn) | +0.2192 | 0.1299 | ±0.2598 | +1.687 | 0.0916 | . |
| Season: winter (vs autumn) | -0.0129 | 0.1176 | ±0.2352 | -0.110 | 0.9126 |  |
| Age (years) | -0.0067 | 0.0035 | ±0.0071 | -1.882 | 0.0599 | . |
| **BMI (kg/m2)** | **+0.0213** | 0.0066 | ±0.0132 | **+3.221** | **0.0013** | ** |
| Hypertension | +0.0868 | 0.0945 | ±0.1891 | +0.919 | 0.3583 |  |
| High cholesterol | -0.0567 | 0.0816 | ±0.1632 | -0.695 | 0.4870 |  |
| Kidney disease | -0.1189 | 0.1666 | ±0.3333 | -0.714 | 0.4754 |  |
| Circulatory disease | +0.2890 | 0.1620 | ±0.3240 | +1.784 | 0.0744 | . |
| MAG (mg/dL/h) | +0.0087 | 0.0066 | ±0.0133 | +1.303 | 0.1926 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **443**, R² = **0.1365**, Adj R² = **0.1083**, F-statistic = **4.83** (p = **2.61e-08**), Residual SE = **0.855** on **428** df, AIC = **1132.7**, BIC = **1194.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8531** | 0.4100 | ±0.8199 | **+4.520** | **6.18e-06** | *** |
| Education: graduate level (vs college) | -0.1049 | 0.0879 | ±0.1757 | -1.194 | 0.2327 |  |
| Education: high school or below (vs college) | +0.3340 | 0.1766 | ±0.3532 | +1.891 | 0.0586 | . |
| Site: UCSD (vs UAB) | +0.0515 | 0.1068 | ±0.2136 | +0.483 | 0.6294 |  |
| **Site: UW (vs UAB)** | **-0.3212** | 0.1158 | ±0.2316 | **-2.773** | **0.0055** | ** |
| Season: spring (vs autumn) | -0.1047 | 0.1125 | ±0.2249 | -0.931 | 0.3520 |  |
| Season: summer (vs autumn) | +0.2152 | 0.1296 | ±0.2591 | +1.661 | 0.0968 | . |
| Season: winter (vs autumn) | -0.0084 | 0.1195 | ±0.2389 | -0.070 | 0.9440 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0071 | **-2.005** | **0.0449** | * |
| **BMI (kg/m2)** | **+0.0208** | 0.0067 | ±0.0133 | **+3.114** | **0.0018** | ** |
| Hypertension | +0.0839 | 0.0947 | ±0.1893 | +0.886 | 0.3755 |  |
| High cholesterol | -0.0544 | 0.0820 | ±0.1639 | -0.663 | 0.5072 |  |
| Kidney disease | -0.1043 | 0.1699 | ±0.3398 | -0.614 | 0.5395 |  |
| Circulatory disease | +0.2826 | 0.1628 | ±0.3256 | +1.736 | 0.0826 | . |
| Avg. daily range (mg/dL) | -0.0014 | 0.0036 | ±0.0072 | -0.389 | 0.6976 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **443**, R² = **0.1372**, Adj R² = **0.1090**, F-statistic = **4.86** (p = **2.27e-08**), Residual SE = **0.854** on **428** df, AIC = **1132.3**, BIC = **1193.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6638** | 0.3002 | ±0.6004 | **+5.542** | **2.99e-08** | *** |
| Education: graduate level (vs college) | -0.1059 | 0.0875 | ±0.1749 | -1.211 | 0.2259 |  |
| Education: high school or below (vs college) | +0.3263 | 0.1760 | ±0.3521 | +1.854 | 0.0638 | . |
| Site: UCSD (vs UAB) | +0.0579 | 0.1061 | ±0.2121 | +0.546 | 0.5851 |  |
| **Site: UW (vs UAB)** | **-0.3190** | 0.1157 | ±0.2315 | **-2.757** | **0.0058** | ** |
| Season: spring (vs autumn) | -0.1112 | 0.1117 | ±0.2233 | -0.995 | 0.3196 |  |
| Season: summer (vs autumn) | +0.2107 | 0.1312 | ±0.2623 | +1.607 | 0.1082 |  |
| Season: winter (vs autumn) | -0.0166 | 0.1185 | ±0.2371 | -0.140 | 0.8889 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0071 | **-1.987** | **0.0469** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0133 | **+3.150** | **0.0016** | ** |
| Hypertension | +0.0788 | 0.0953 | ±0.1907 | +0.827 | 0.4085 |  |
| High cholesterol | -0.0562 | 0.0821 | ±0.1642 | -0.685 | 0.4935 |  |
| Kidney disease | -0.1064 | 0.1697 | ±0.3394 | -0.627 | 0.5305 |  |
| Circulatory disease | +0.2747 | 0.1612 | ±0.3224 | +1.704 | 0.0883 | . |
| SD of daily means (mg/dL) | +0.0154 | 0.0220 | ±0.0440 | +0.701 | 0.4830 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **443**, R² = **0.1363**, Adj R² = **0.1080**, F-statistic = **4.82** (p = **2.76e-08**), Residual SE = **0.855** on **428** df, AIC = **1132.8**, BIC = **1194.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2.8346 | 14.3314 | ±28.6627 | +0.198 | 0.8432 |  |
| Education: graduate level (vs college) | -0.1037 | 0.0876 | ±0.1751 | -1.185 | 0.2361 |  |
| Education: high school or below (vs college) | +0.3336 | 0.1774 | ±0.3548 | +1.880 | 0.0600 | . |
| Site: UCSD (vs UAB) | +0.0542 | 0.1079 | ±0.2158 | +0.502 | 0.6154 |  |
| **Site: UW (vs UAB)** | **-0.3184** | 0.1169 | ±0.2337 | **-2.724** | **0.0064** | ** |
| Season: spring (vs autumn) | -0.1063 | 0.1121 | ±0.2243 | -0.948 | 0.3433 |  |
| Season: summer (vs autumn) | +0.2147 | 0.1300 | ±0.2599 | +1.653 | 0.0984 | . |
| Season: winter (vs autumn) | -0.0107 | 0.1195 | ±0.2389 | -0.090 | 0.9285 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0071 | **-2.005** | **0.0450** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0132 | **+3.166** | **0.0015** | ** |
| Hypertension | +0.0846 | 0.0951 | ±0.1901 | +0.890 | 0.3735 |  |
| High cholesterol | -0.0544 | 0.0819 | ±0.1639 | -0.664 | 0.5067 |  |
| Kidney disease | -0.1084 | 0.1689 | ±0.3378 | -0.642 | 0.5211 |  |
| Circulatory disease | +0.2828 | 0.1629 | ±0.3258 | +1.736 | 0.0825 | . |
| Time in range 70-180, pooled (%) | -0.0110 | 0.1441 | ±0.2882 | -0.077 | 0.9390 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **443**, R² = **0.1362**, Adj R² = **0.1080**, F-statistic = **4.82** (p = **2.77e-08**), Residual SE = **0.855** on **428** df, AIC = **1132.8**, BIC = **1194.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2.6231 | 13.9389 | ±27.8779 | +0.188 | 0.8507 |  |
| Education: graduate level (vs college) | -0.1037 | 0.0877 | ±0.1755 | -1.182 | 0.2372 |  |
| Education: high school or below (vs college) | +0.3337 | 0.1777 | ±0.3554 | +1.878 | 0.0604 | . |
| Site: UCSD (vs UAB) | +0.0539 | 0.1072 | ±0.2145 | +0.502 | 0.6155 |  |
| **Site: UW (vs UAB)** | **-0.3187** | 0.1161 | ±0.2323 | **-2.745** | **0.0061** | ** |
| Season: spring (vs autumn) | -0.1061 | 0.1121 | ±0.2243 | -0.946 | 0.3440 |  |
| Season: summer (vs autumn) | +0.2152 | 0.1294 | ±0.2587 | +1.663 | 0.0963 | . |
| Season: winter (vs autumn) | -0.0104 | 0.1185 | ±0.2371 | -0.088 | 0.9301 |  |
| **Age (years)** | **-0.0071** | 0.0035 | ±0.0071 | **-2.004** | **0.0450** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0133 | **+3.156** | **0.0016** | ** |
| Hypertension | +0.0849 | 0.0947 | ±0.1894 | +0.896 | 0.3700 |  |
| High cholesterol | -0.0545 | 0.0820 | ±0.1640 | -0.665 | 0.5063 |  |
| Kidney disease | -0.1080 | 0.1692 | ±0.3383 | -0.638 | 0.5233 |  |
| Circulatory disease | +0.2826 | 0.1629 | ±0.3258 | +1.735 | 0.0828 | . |
| Avg. daily time in range 70-180 (%) | -0.0089 | 0.1400 | ±0.2801 | -0.064 | 0.9493 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.1380**, Adj R² = **0.1098**, F-statistic = **4.89** (p = **1.93e-08**), Residual SE = **0.854** on **428** df, AIC = **1131.9**, BIC = **1193.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7142** | 0.2804 | ±0.5608 | **+6.114** | **9.74e-10** | *** |
| Education: graduate level (vs college) | -0.1030 | 0.0873 | ±0.1746 | -1.180 | 0.2382 |  |
| Education: high school or below (vs college) | +0.3375 | 0.1782 | ±0.3564 | +1.894 | 0.0583 | . |
| Site: UCSD (vs UAB) | +0.0722 | 0.1106 | ±0.2213 | +0.653 | 0.5140 |  |
| **Site: UW (vs UAB)** | **-0.3083** | 0.1182 | ±0.2363 | **-2.609** | **0.0091** | ** |
| Season: spring (vs autumn) | -0.1187 | 0.1139 | ±0.2279 | -1.042 | 0.2974 |  |
| Season: summer (vs autumn) | +0.2073 | 0.1298 | ±0.2596 | +1.597 | 0.1104 |  |
| Season: winter (vs autumn) | -0.0213 | 0.1187 | ±0.2375 | -0.179 | 0.8576 |  |
| **Age (years)** | **-0.0070** | 0.0036 | ±0.0071 | **-1.979** | **0.0478** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0133 | **+3.157** | **0.0016** | ** |
| Hypertension | +0.0782 | 0.0955 | ±0.1910 | +0.818 | 0.4131 |  |
| High cholesterol | -0.0541 | 0.0822 | ±0.1645 | -0.658 | 0.5104 |  |
| Kidney disease | -0.0954 | 0.1700 | ±0.3401 | -0.561 | 0.5747 |  |
| Circulatory disease | +0.2791 | 0.1623 | ±0.3246 | +1.719 | 0.0855 | . |
| Any reading < 54 during wear (0/1) | +0.1051 | 0.1312 | ±0.2624 | +0.801 | 0.4231 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.1422**, Adj R² = **0.1141**, F-statistic = **5.07** (p = **8.08e-09**), Residual SE = **0.852** on **428** df, AIC = **1129.8**, BIC = **1191.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6948** | 0.2805 | ±0.5609 | **+6.043** | **1.51e-09** | *** |
| Education: graduate level (vs college) | -0.1044 | 0.0873 | ±0.1745 | -1.196 | 0.2318 |  |
| **Education: high school or below (vs college)** | **+0.3503** | 0.1778 | ±0.3556 | **+1.970** | **0.0488** | * |
| Site: UCSD (vs UAB) | +0.0790 | 0.1099 | ±0.2199 | +0.719 | 0.4721 |  |
| **Site: UW (vs UAB)** | **-0.3061** | 0.1175 | ±0.2349 | **-2.606** | **0.0092** | ** |
| Season: spring (vs autumn) | -0.1040 | 0.1117 | ±0.2233 | -0.931 | 0.3516 |  |
| Season: summer (vs autumn) | +0.2131 | 0.1293 | ±0.2587 | +1.648 | 0.0994 | . |
| Season: winter (vs autumn) | -0.0170 | 0.1169 | ±0.2339 | -0.145 | 0.8846 |  |
| Age (years) | -0.0066 | 0.0036 | ±0.0072 | -1.820 | 0.0688 | . |
| **BMI (kg/m2)** | **+0.0202** | 0.0067 | ±0.0134 | **+3.016** | **0.0026** | ** |
| Hypertension | +0.0691 | 0.0953 | ±0.1907 | +0.724 | 0.4689 |  |
| High cholesterol | -0.0492 | 0.0825 | ±0.1650 | -0.596 | 0.5510 |  |
| Kidney disease | -0.0932 | 0.1699 | ±0.3399 | -0.548 | 0.5834 |  |
| Circulatory disease | +0.2742 | 0.1606 | ±0.3212 | +1.707 | 0.0879 | . |
| Time < 54 (%) | +1.3438 | 0.9108 | ±1.8216 | +1.475 | 0.1401 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.1462**, Adj R² = **0.1183**, F-statistic = **5.24** (p = **3.46e-09**), Residual SE = **0.850** on **428** df, AIC = **1127.7**, BIC = **1189.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.7037** | 0.2757 | ±0.5514 | **+6.180** | **6.42e-10** | *** |
| Education: graduate level (vs college) | -0.1060 | 0.0876 | ±0.1751 | -1.211 | 0.2260 |  |
| Education: high school or below (vs college) | +0.3430 | 0.1761 | ±0.3523 | +1.947 | 0.0515 | . |
| Site: UCSD (vs UAB) | +0.0682 | 0.1082 | ±0.2164 | +0.630 | 0.5285 |  |
| **Site: UW (vs UAB)** | **-0.3161** | 0.1156 | ±0.2313 | **-2.733** | **0.0063** | ** |
| Season: spring (vs autumn) | -0.0988 | 0.1123 | ±0.2247 | -0.879 | 0.3793 |  |
| Season: summer (vs autumn) | +0.2318 | 0.1294 | ±0.2588 | +1.791 | 0.0733 | . |
| Season: winter (vs autumn) | -0.0078 | 0.1178 | ±0.2355 | -0.067 | 0.9469 |  |
| Age (years) | -0.0068 | 0.0036 | ±0.0071 | -1.928 | 0.0539 | . |
| **BMI (kg/m2)** | **+0.0205** | 0.0066 | ±0.0133 | **+3.090** | **0.0020** | ** |
| Hypertension | +0.0771 | 0.0934 | ±0.1868 | +0.826 | 0.4090 |  |
| High cholesterol | -0.0542 | 0.0822 | ±0.1644 | -0.659 | 0.5098 |  |
| Kidney disease | -0.0973 | 0.1707 | ±0.3414 | -0.570 | 0.5686 |  |
| Circulatory disease | +0.2656 | 0.1613 | ±0.3225 | +1.647 | 0.0996 | . |
| Avg. daily time < 54 (%) | +2.3039 | 1.3775 | ±2.7550 | +1.673 | 0.0944 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.1430**, Adj R² = **0.1149**, F-statistic = **5.10** (p = **6.85e-09**), Residual SE = **0.851** on **428** df, AIC = **1129.4**, BIC = **1190.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6749** | 0.2760 | ±0.5520 | **+6.069** | **1.29e-09** | *** |
| Education: graduate level (vs college) | -0.0998 | 0.0869 | ±0.1739 | -1.148 | 0.2510 |  |
| Education: high school or below (vs college) | +0.3173 | 0.1758 | ±0.3515 | +1.805 | 0.0710 | . |
| Site: UCSD (vs UAB) | +0.0662 | 0.1077 | ±0.2153 | +0.615 | 0.5387 |  |
| **Site: UW (vs UAB)** | **-0.3039** | 0.1163 | ±0.2326 | **-2.613** | **0.0090** | ** |
| Season: spring (vs autumn) | -0.1107 | 0.1113 | ±0.2225 | -0.995 | 0.3196 |  |
| Season: summer (vs autumn) | +0.2112 | 0.1304 | ±0.2608 | +1.620 | 0.1053 |  |
| Season: winter (vs autumn) | -0.0212 | 0.1186 | ±0.2373 | -0.178 | 0.8585 |  |
| **Age (years)** | **-0.0071** | 0.0036 | ±0.0071 | **-1.995** | **0.0460** | * |
| **BMI (kg/m2)** | **+0.0210** | 0.0066 | ±0.0132 | **+3.173** | **0.0015** | ** |
| Hypertension | +0.0945 | 0.0947 | ±0.1895 | +0.997 | 0.3186 |  |
| High cholesterol | -0.0674 | 0.0819 | ±0.1637 | -0.824 | 0.4101 |  |
| Kidney disease | -0.0838 | 0.1696 | ±0.3393 | -0.494 | 0.6213 |  |
| Circulatory disease | +0.2859 | 0.1632 | ±0.3264 | +1.752 | 0.0797 | . |
| Time 54-69, pooled (%) | +0.4151 | 0.2466 | ±0.4931 | +1.684 | 0.0922 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **443**, R² = **0.1423**, Adj R² = **0.1143**, F-statistic = **5.07** (p = **7.84e-09**), Residual SE = **0.852** on **428** df, AIC = **1129.7**, BIC = **1191.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6852** | 0.2750 | ±0.5500 | **+6.128** | **8.89e-10** | *** |
| Education: graduate level (vs college) | -0.0970 | 0.0869 | ±0.1738 | -1.116 | 0.2644 |  |
| Education: high school or below (vs college) | +0.3169 | 0.1752 | ±0.3504 | +1.809 | 0.0705 | . |
| Site: UCSD (vs UAB) | +0.0595 | 0.1072 | ±0.2144 | +0.555 | 0.5786 |  |
| **Site: UW (vs UAB)** | **-0.3107** | 0.1158 | ±0.2317 | **-2.683** | **0.0073** | ** |
| Season: spring (vs autumn) | -0.1015 | 0.1115 | ±0.2230 | -0.910 | 0.3629 |  |
| Season: summer (vs autumn) | +0.2222 | 0.1306 | ±0.2612 | +1.701 | 0.0889 | . |
| Season: winter (vs autumn) | -0.0161 | 0.1184 | ±0.2368 | -0.136 | 0.8915 |  |
| **Age (years)** | **-0.0072** | 0.0036 | ±0.0071 | **-2.021** | **0.0432** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0132 | **+3.168** | **0.0015** | ** |
| Hypertension | +0.1033 | 0.0959 | ±0.1918 | +1.077 | 0.2814 |  |
| High cholesterol | -0.0656 | 0.0819 | ±0.1638 | -0.801 | 0.4229 |  |
| Kidney disease | -0.0920 | 0.1698 | ±0.3396 | -0.542 | 0.5881 |  |
| Circulatory disease | +0.2804 | 0.1636 | ±0.3271 | +1.714 | 0.0865 | . |
| Avg. daily time 54-69 (%) | +0.4010 | 0.2560 | ±0.5121 | +1.566 | 0.1173 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **443**, R² = **0.1449**, Adj R² = **0.1169**, F-statistic = **5.18** (p = **4.59e-09**), Residual SE = **0.850** on **428** df, AIC = **1128.4**, BIC = **1189.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6610** | 0.2787 | ±0.5574 | **+5.960** | **2.52e-09** | *** |
| Education: graduate level (vs college) | -0.0999 | 0.0868 | ±0.1735 | -1.152 | 0.2495 |  |
| Education: high school or below (vs college) | +0.3224 | 0.1764 | ±0.3527 | +1.828 | 0.0675 | . |
| Site: UCSD (vs UAB) | +0.0742 | 0.1085 | ±0.2170 | +0.684 | 0.4940 |  |
| **Site: UW (vs UAB)** | **-0.2998** | 0.1168 | ±0.2335 | **-2.568** | **0.0102** | * |
| Season: spring (vs autumn) | -0.1101 | 0.1111 | ±0.2223 | -0.991 | 0.3219 |  |
| Season: summer (vs autumn) | +0.2106 | 0.1303 | ±0.2606 | +1.616 | 0.1060 |  |
| Season: winter (vs autumn) | -0.0233 | 0.1182 | ±0.2364 | -0.197 | 0.8435 |  |
| Age (years) | -0.0069 | 0.0036 | ±0.0071 | -1.947 | 0.0515 | . |
| **BMI (kg/m2)** | **+0.0207** | 0.0066 | ±0.0132 | **+3.136** | **0.0017** | ** |
| Hypertension | +0.0897 | 0.0942 | ±0.1885 | +0.952 | 0.3413 |  |
| High cholesterol | -0.0660 | 0.0819 | ±0.1639 | -0.806 | 0.4205 |  |
| Kidney disease | -0.0791 | 0.1698 | ±0.3395 | -0.466 | 0.6412 |  |
| Circulatory disease | +0.2833 | 0.1626 | ±0.3252 | +1.742 | 0.0814 | . |
| Time < 70 (%) | +0.4188 | 0.2279 | ±0.4559 | +1.837 | 0.0662 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **443**, R² = **0.1447**, Adj R² = **0.1167**, F-statistic = **5.17** (p = **4.82e-09**), Residual SE = **0.851** on **428** df, AIC = **1128.5**, BIC = **1189.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.6750** | 0.2757 | ±0.5514 | **+6.075** | **1.24e-09** | *** |
| Education: graduate level (vs college) | -0.0969 | 0.0866 | ±0.1733 | -1.118 | 0.2635 |  |
| Education: high school or below (vs college) | +0.3175 | 0.1755 | ±0.3510 | +1.809 | 0.0705 | . |
| Site: UCSD (vs UAB) | +0.0627 | 0.1075 | ±0.2150 | +0.583 | 0.5598 |  |
| **Site: UW (vs UAB)** | **-0.3096** | 0.1159 | ±0.2317 | **-2.673** | **0.0075** | ** |
| Season: spring (vs autumn) | -0.0997 | 0.1114 | ±0.2228 | -0.895 | 0.3708 |  |
| Season: summer (vs autumn) | +0.2259 | 0.1305 | ±0.2611 | +1.730 | 0.0835 | . |
| Season: winter (vs autumn) | -0.0161 | 0.1181 | ±0.2362 | -0.136 | 0.8914 |  |
| **Age (years)** | **-0.0072** | 0.0036 | ±0.0071 | **-2.009** | **0.0445** | * |
| **BMI (kg/m2)** | **+0.0209** | 0.0066 | ±0.0132 | **+3.159** | **0.0016** | ** |
| Hypertension | +0.1033 | 0.0956 | ±0.1911 | +1.081 | 0.2798 |  |
| High cholesterol | -0.0665 | 0.0819 | ±0.1638 | -0.812 | 0.4169 |  |
| Kidney disease | -0.0889 | 0.1700 | ±0.3400 | -0.523 | 0.6009 |  |
| Circulatory disease | +0.2770 | 0.1633 | ±0.3266 | +1.696 | 0.0898 | . |
| Avg. daily time < 70 (%) | +0.4306 | 0.2449 | ±0.4897 | +1.759 | 0.0786 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.1410**, Adj R² = **0.1129**, F-statistic = **5.02** (p = **1.05e-08**), Residual SE = **0.852** on **428** df, AIC = **1130.4**, BIC = **1191.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +118.4699 | 89.5473 | ±179.0946 | +1.323 | 0.1858 |  |
| Education: graduate level (vs college) | -0.1044 | 0.0874 | ±0.1747 | -1.195 | 0.2320 |  |
| **Education: high school or below (vs college)** | **+0.3486** | 0.1778 | ±0.3555 | **+1.961** | **0.0499** | * |
| Site: UCSD (vs UAB) | +0.0774 | 0.1101 | ±0.2203 | +0.703 | 0.4822 |  |
| **Site: UW (vs UAB)** | **-0.3065** | 0.1178 | ±0.2356 | **-2.601** | **0.0093** | ** |
| Season: spring (vs autumn) | -0.1055 | 0.1118 | ±0.2236 | -0.943 | 0.3455 |  |
| Season: summer (vs autumn) | +0.2135 | 0.1293 | ±0.2586 | +1.651 | 0.0987 | . |
| Season: winter (vs autumn) | -0.0171 | 0.1172 | ±0.2344 | -0.146 | 0.8842 |  |
| Age (years) | -0.0066 | 0.0036 | ±0.0073 | -1.810 | 0.0703 | . |
| **BMI (kg/m2)** | **+0.0203** | 0.0067 | ±0.0133 | **+3.049** | **0.0023** | ** |
| Hypertension | +0.0717 | 0.0953 | ±0.1907 | +0.752 | 0.4522 |  |
| High cholesterol | -0.0502 | 0.0824 | ±0.1649 | -0.609 | 0.5428 |  |
| Kidney disease | -0.0952 | 0.1699 | ±0.3399 | -0.560 | 0.5754 |  |
| Circulatory disease | +0.2750 | 0.1608 | ±0.3217 | +1.710 | 0.0873 | . |
| Time 54-250, pooled (%) | -1.1678 | 0.8960 | ±1.7921 | -1.303 | 0.1925 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.1440**, Adj R² = **0.1160**, F-statistic = **5.14** (p = **5.53e-09**), Residual SE = **0.851** on **428** df, AIC = **1128.8**, BIC = **1190.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +200.3425 | 128.7187 | ±257.4374 | +1.556 | 0.1196 |  |
| Education: graduate level (vs college) | -0.1059 | 0.0877 | ±0.1753 | -1.209 | 0.2268 |  |
| Education: high school or below (vs college) | +0.3425 | 0.1763 | ±0.3527 | +1.943 | 0.0521 | . |
| Site: UCSD (vs UAB) | +0.0693 | 0.1087 | ±0.2173 | +0.638 | 0.5233 |  |
| **Site: UW (vs UAB)** | **-0.3141** | 0.1162 | ±0.2324 | **-2.702** | **0.0069** | ** |
| Season: spring (vs autumn) | -0.1019 | 0.1122 | ±0.2244 | -0.909 | 0.3636 |  |
| Season: summer (vs autumn) | +0.2298 | 0.1293 | ±0.2586 | +1.777 | 0.0755 | . |
| Season: winter (vs autumn) | -0.0100 | 0.1177 | ±0.2353 | -0.085 | 0.9322 |  |
| Age (years) | -0.0067 | 0.0036 | ±0.0071 | -1.891 | 0.0586 | . |
| **BMI (kg/m2)** | **+0.0207** | 0.0066 | ±0.0133 | **+3.129** | **0.0018** | ** |
| Hypertension | +0.0792 | 0.0936 | ±0.1871 | +0.846 | 0.3974 |  |
| High cholesterol | -0.0548 | 0.0822 | ±0.1644 | -0.667 | 0.5049 |  |
| Kidney disease | -0.0989 | 0.1707 | ±0.3413 | -0.580 | 0.5621 |  |
| Circulatory disease | +0.2675 | 0.1614 | ±0.3229 | +1.657 | 0.0975 | . |
| Avg. daily time 54-250 (%) | -1.9865 | 1.2874 | ±2.5747 | -1.543 | 0.1228 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **443**, R² = **0.1401**, Adj R² = **0.1120**, F-statistic = **4.98** (p = **1.24e-08**), Residual SE = **0.853** on **428** df, AIC = **1130.8**, BIC = **1192.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8131** | 0.2863 | ±0.5726 | **+6.333** | **2.40e-10** | *** |
| Education: graduate level (vs college) | -0.1042 | 0.0874 | ±0.1749 | -1.192 | 0.2331 |  |
| Education: high school or below (vs college) | +0.3252 | 0.1770 | ±0.3541 | +1.837 | 0.0662 | . |
| Site: UCSD (vs UAB) | +0.0536 | 0.1060 | ±0.2120 | +0.506 | 0.6128 |  |
| **Site: UW (vs UAB)** | **-0.3175** | 0.1149 | ±0.2297 | **-2.764** | **0.0057** | ** |
| Season: spring (vs autumn) | -0.1068 | 0.1123 | ±0.2246 | -0.952 | 0.3413 |  |
| Season: summer (vs autumn) | +0.2167 | 0.1297 | ±0.2593 | +1.672 | 0.0946 | . |
| Season: winter (vs autumn) | -0.0089 | 0.1179 | ±0.2357 | -0.075 | 0.9399 |  |
| **Age (years)** | **-0.0072** | 0.0035 | ±0.0071 | **-2.025** | **0.0429** | * |
| **BMI (kg/m2)** | **+0.0205** | 0.0067 | ±0.0134 | **+3.056** | **0.0022** | ** |
| Hypertension | +0.0891 | 0.0948 | ±0.1896 | +0.940 | 0.3472 |  |
| High cholesterol | -0.0561 | 0.0819 | ±0.1639 | -0.685 | 0.4935 |  |
| Kidney disease | -0.0788 | 0.1743 | ±0.3485 | -0.452 | 0.6512 |  |
| Circulatory disease | +0.2803 | 0.1615 | ±0.3229 | +1.736 | 0.0825 | . |
| Time 181-250, pooled (%) | -0.2043 | 0.1470 | ±0.2940 | -1.390 | 0.1646 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **443**, R² = **0.1397**, Adj R² = **0.1115**, F-statistic = **4.96** (p = **1.37e-08**), Residual SE = **0.853** on **428** df, AIC = **1131.1**, BIC = **1192.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8006** | 0.2829 | ±0.5659 | **+6.364** | **1.97e-10** | *** |
| Education: graduate level (vs college) | -0.1044 | 0.0875 | ±0.1750 | -1.194 | 0.2326 |  |
| Education: high school or below (vs college) | +0.3223 | 0.1768 | ±0.3535 | +1.823 | 0.0683 | . |
| Site: UCSD (vs UAB) | +0.0534 | 0.1061 | ±0.2122 | +0.504 | 0.6145 |  |
| **Site: UW (vs UAB)** | **-0.3164** | 0.1149 | ±0.2298 | **-2.754** | **0.0059** | ** |
| Season: spring (vs autumn) | -0.1052 | 0.1126 | ±0.2251 | -0.934 | 0.3502 |  |
| Season: summer (vs autumn) | +0.2152 | 0.1295 | ±0.2590 | +1.662 | 0.0965 | . |
| Season: winter (vs autumn) | -0.0108 | 0.1179 | ±0.2358 | -0.091 | 0.9273 |  |
| **Age (years)** | **-0.0073** | 0.0035 | ±0.0071 | **-2.059** | **0.0395** | * |
| **BMI (kg/m2)** | **+0.0208** | 0.0066 | ±0.0132 | **+3.152** | **0.0016** | ** |
| Hypertension | +0.0887 | 0.0949 | ±0.1898 | +0.935 | 0.3499 |  |
| High cholesterol | -0.0534 | 0.0819 | ±0.1637 | -0.653 | 0.5139 |  |
| Kidney disease | -0.0911 | 0.1741 | ±0.3482 | -0.523 | 0.6008 |  |
| Circulatory disease | +0.2816 | 0.1614 | ±0.3228 | +1.745 | 0.0810 | . |
| Avg. daily time 181-250 (%) | -0.1892 | 0.1426 | ±0.2852 | -1.327 | 0.1846 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **443**, R² = **0.1403**, Adj R² = **0.1122**, F-statistic = **4.99** (p = **1.20e-08**), Residual SE = **0.853** on **428** df, AIC = **1130.8**, BIC = **1192.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8158** | 0.2867 | ±0.5733 | **+6.334** | **2.39e-10** | *** |
| Education: graduate level (vs college) | -0.1042 | 0.0874 | ±0.1748 | -1.192 | 0.2331 |  |
| Education: high school or below (vs college) | +0.3250 | 0.1770 | ±0.3540 | +1.836 | 0.0664 | . |
| Site: UCSD (vs UAB) | +0.0533 | 0.1060 | ±0.2120 | +0.503 | 0.6148 |  |
| **Site: UW (vs UAB)** | **-0.3177** | 0.1148 | ±0.2297 | **-2.766** | **0.0057** | ** |
| Season: spring (vs autumn) | -0.1066 | 0.1123 | ±0.2246 | -0.950 | 0.3422 |  |
| Season: summer (vs autumn) | +0.2167 | 0.1297 | ±0.2593 | +1.672 | 0.0946 | . |
| Season: winter (vs autumn) | -0.0087 | 0.1179 | ±0.2358 | -0.074 | 0.9412 |  |
| **Age (years)** | **-0.0072** | 0.0035 | ±0.0071 | **-2.029** | **0.0425** | * |
| **BMI (kg/m2)** | **+0.0204** | 0.0067 | ±0.0134 | **+3.052** | **0.0023** | ** |
| Hypertension | +0.0891 | 0.0948 | ±0.1895 | +0.940 | 0.3472 |  |
| High cholesterol | -0.0561 | 0.0819 | ±0.1639 | -0.685 | 0.4936 |  |
| Kidney disease | -0.0783 | 0.1744 | ±0.3487 | -0.449 | 0.6535 |  |
| Circulatory disease | +0.2803 | 0.1614 | ±0.3229 | +1.736 | 0.0825 | . |
| Time > 180 (%) | -0.2078 | 0.1467 | ±0.2933 | -1.417 | 0.1566 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **443**, R² = **0.1398**, Adj R² = **0.1117**, F-statistic = **4.97** (p = **1.33e-08**), Residual SE = **0.853** on **428** df, AIC = **1131.0**, BIC = **1192.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8032** | 0.2832 | ±0.5665 | **+6.366** | **1.93e-10** | *** |
| Education: graduate level (vs college) | -0.1044 | 0.0875 | ±0.1749 | -1.194 | 0.2326 |  |
| Education: high school or below (vs college) | +0.3220 | 0.1767 | ±0.3535 | +1.822 | 0.0685 | . |
| Site: UCSD (vs UAB) | +0.0531 | 0.1061 | ±0.2122 | +0.501 | 0.6165 |  |
| **Site: UW (vs UAB)** | **-0.3166** | 0.1149 | ±0.2297 | **-2.757** | **0.0058** | ** |
| Season: spring (vs autumn) | -0.1049 | 0.1126 | ±0.2252 | -0.932 | 0.3513 |  |
| Season: summer (vs autumn) | +0.2152 | 0.1295 | ±0.2590 | +1.662 | 0.0965 | . |
| Season: winter (vs autumn) | -0.0106 | 0.1179 | ±0.2359 | -0.090 | 0.9285 |  |
| **Age (years)** | **-0.0073** | 0.0035 | ±0.0071 | **-2.064** | **0.0391** | * |
| **BMI (kg/m2)** | **+0.0208** | 0.0066 | ±0.0132 | **+3.149** | **0.0016** | ** |
| Hypertension | +0.0887 | 0.0949 | ±0.1897 | +0.935 | 0.3499 |  |
| High cholesterol | -0.0534 | 0.0819 | ±0.1637 | -0.652 | 0.5145 |  |
| Kidney disease | -0.0908 | 0.1742 | ±0.3484 | -0.521 | 0.6023 |  |
| Circulatory disease | +0.2816 | 0.1614 | ±0.3227 | +1.745 | 0.0809 | . |
| Avg. daily time > 180 (%) | -0.1928 | 0.1421 | ±0.2842 | -1.357 | 0.1749 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 443)
**Regression Call / Formula**: `log_pm25_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **443**, R² = **0.1438**, Adj R² = **0.1157**, F-statistic = **5.13** (p = **5.83e-09**), Residual SE = **0.851** on **428** df, AIC = **1129.0**, BIC = **1190.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1.8023** | 0.2761 | ±0.5522 | **+6.528** | **6.67e-11** | *** |
| Education: graduate level (vs college) | -0.1126 | 0.0882 | ±0.1764 | -1.276 | 0.2019 |  |
| Education: high school or below (vs college) | +0.3279 | 0.1751 | ±0.3502 | +1.873 | 0.0611 | . |
| Site: UCSD (vs UAB) | +0.0541 | 0.1061 | ±0.2122 | +0.510 | 0.6102 |  |
| **Site: UW (vs UAB)** | **-0.3127** | 0.1149 | ±0.2298 | **-2.721** | **0.0065** | ** |
| Season: spring (vs autumn) | -0.1017 | 0.1126 | ±0.2251 | -0.903 | 0.3664 |  |
| Season: summer (vs autumn) | +0.2105 | 0.1282 | ±0.2564 | +1.642 | 0.1006 |  |
| Season: winter (vs autumn) | +0.0102 | 0.1199 | ±0.2399 | +0.085 | 0.9319 |  |
| **Age (years)** | **-0.0083** | 0.0036 | ±0.0073 | **-2.281** | **0.0225** | * |
| **BMI (kg/m2)** | **+0.0217** | 0.0065 | ±0.0131 | **+3.316** | **9.13e-04** | *** |
| Hypertension | +0.1016 | 0.0954 | ±0.1908 | +1.065 | 0.2868 |  |
| High cholesterol | -0.0496 | 0.0817 | ±0.1633 | -0.607 | 0.5440 |  |
| Kidney disease | -0.1056 | 0.1827 | ±0.3654 | -0.578 | 0.5635 |  |
| Circulatory disease | +0.2729 | 0.1617 | ±0.3235 | +1.688 | 0.0915 | . |
| Nocturnal time > 180 (%) | -0.2262 | 0.1273 | ±0.2547 | -1.776 | 0.0757 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor temperature, mean (deg C)  (domain: Home environment; outcome sample N = 443; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **443**, R² = **0.3401**, Adj R² = **0.3201**, F-statistic = **17.01** (p = **1.31e-31**), Residual SE = **1.892** on **429** df, AIC = **1836.0**, BIC = **1893.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9350** | 0.8204 | ±1.6407 | **+29.177** | **3.85e-187** | *** |
| Education: graduate level (vs college) | +0.0519 | 0.1979 | ±0.3959 | +0.262 | 0.7930 |  |
| Education: high school or below (vs college) | +0.2979 | 0.3608 | ±0.7217 | +0.826 | 0.4090 |  |
| Site: UCSD (vs UAB) | -0.2705 | 0.2355 | ±0.4711 | -1.149 | 0.2507 |  |
| **Site: UW (vs UAB)** | **-1.0842** | 0.2344 | ±0.4688 | **-4.625** | **3.74e-06** | *** |
| Season: spring (vs autumn) | -0.2108 | 0.2729 | ±0.5459 | -0.772 | 0.4400 |  |
| **Season: summer (vs autumn)** | **+1.7948** | 0.3201 | ±0.6403 | **+5.606** | **2.07e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5259** | 0.2809 | ±0.5618 | **-5.432** | **5.57e-08** | *** |
| Age (years) | +0.0078 | 0.0085 | ±0.0171 | +0.911 | 0.3621 |  |
| BMI (kg/m2) | +0.0208 | 0.0156 | ±0.0313 | +1.331 | 0.1832 |  |
| Hypertension | -0.0935 | 0.2118 | ±0.4235 | -0.442 | 0.6588 |  |
| High cholesterol | -0.3404 | 0.1909 | ±0.3819 | -1.783 | 0.0746 | . |
| **Kidney disease** | **+0.9283** | 0.3632 | ±0.7264 | **+2.556** | **0.0106** | * |
| **Circulatory disease** | **+0.8075** | 0.3573 | ±0.7146 | **+2.260** | **0.0238** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **443**, R² = **0.3409**, Adj R² = **0.3194**, F-statistic = **15.81** (p = **4.36e-31**), Residual SE = **1.893** on **428** df, AIC = **1837.5**, BIC = **1898.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0863** | 1.8507 | ±3.7014 | **+13.555** | **7.39e-42** | *** |
| Education: graduate level (vs college) | +0.0466 | 0.1971 | ±0.3942 | +0.236 | 0.8131 |  |
| Education: high school or below (vs college) | +0.3139 | 0.3639 | ±0.7279 | +0.862 | 0.3884 |  |
| Site: UCSD (vs UAB) | -0.2679 | 0.2364 | ±0.4728 | -1.133 | 0.2570 |  |
| **Site: UW (vs UAB)** | **-1.0871** | 0.2351 | ±0.4702 | **-4.624** | **3.77e-06** | *** |
| Season: spring (vs autumn) | -0.2394 | 0.2739 | ±0.5478 | -0.874 | 0.3820 |  |
| **Season: summer (vs autumn)** | **+1.8056** | 0.3195 | ±0.6391 | **+5.651** | **1.60e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5364** | 0.2815 | ±0.5630 | **-5.458** | **4.81e-08** | *** |
| Age (years) | +0.0084 | 0.0088 | ±0.0175 | +0.963 | 0.3358 |  |
| BMI (kg/m2) | +0.0220 | 0.0162 | ±0.0324 | +1.353 | 0.1760 |  |
| Hypertension | -0.0808 | 0.2143 | ±0.4285 | -0.377 | 0.7060 |  |
| High cholesterol | -0.3114 | 0.1994 | ±0.3988 | -1.562 | 0.1183 |  |
| **Kidney disease** | **+0.9144** | 0.3611 | ±0.7222 | **+2.532** | **0.0113** | * |
| **Circulatory disease** | **+0.7958** | 0.3589 | ±0.7179 | **+2.217** | **0.0266** | * |
| HbA1c (%) | -0.2211 | 0.3438 | ±0.6876 | -0.643 | 0.5201 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **443**, R² = **0.3401**, Adj R² = **0.3186**, F-statistic = **15.76** (p = **5.53e-31**), Residual SE = **1.895** on **428** df, AIC = **1838.0**, BIC = **1899.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9690** | 1.5979 | ±3.1957 | **+15.001** | **7.27e-51** | *** |
| Education: graduate level (vs college) | +0.0520 | 0.1983 | ±0.3967 | +0.262 | 0.7931 |  |
| Education: high school or below (vs college) | +0.2976 | 0.3615 | ±0.7230 | +0.823 | 0.4103 |  |
| Site: UCSD (vs UAB) | -0.2702 | 0.2361 | ±0.4721 | -1.145 | 0.2523 |  |
| **Site: UW (vs UAB)** | **-1.0839** | 0.2350 | ±0.4701 | **-4.612** | **3.99e-06** | *** |
| Season: spring (vs autumn) | -0.2111 | 0.2724 | ±0.5448 | -0.775 | 0.4384 |  |
| **Season: summer (vs autumn)** | **+1.7948** | 0.3208 | ±0.6415 | **+5.595** | **2.20e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5262** | 0.2812 | ±0.5625 | **-5.426** | **5.75e-08** | *** |
| Age (years) | +0.0078 | 0.0086 | ±0.0171 | +0.909 | 0.3636 |  |
| BMI (kg/m2) | +0.0208 | 0.0158 | ±0.0315 | +1.323 | 0.1859 |  |
| Hypertension | -0.0932 | 0.2127 | ±0.4254 | -0.438 | 0.6612 |  |
| High cholesterol | -0.3406 | 0.1917 | ±0.3833 | -1.777 | 0.0756 | . |
| **Kidney disease** | **+0.9286** | 0.3638 | ±0.7275 | **+2.553** | **0.0107** | * |
| **Circulatory disease** | **+0.8076** | 0.3579 | ±0.7158 | **+2.256** | **0.0241** | * |
| Mean glucose (mg/dL) | -0.0003 | 0.0125 | ±0.0250 | -0.024 | 0.9809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **443**, R² = **0.3401**, Adj R² = **0.3186**, F-statistic = **15.76** (p = **5.53e-31**), Residual SE = **1.895** on **428** df, AIC = **1838.0**, BIC = **1899.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0105** | 3.2072 | ±6.4144 | **+7.486** | **7.08e-14** | *** |
| Education: graduate level (vs college) | +0.0520 | 0.1983 | ±0.3967 | +0.262 | 0.7931 |  |
| Education: high school or below (vs college) | +0.2976 | 0.3615 | ±0.7230 | +0.823 | 0.4103 |  |
| Site: UCSD (vs UAB) | -0.2702 | 0.2361 | ±0.4721 | -1.145 | 0.2523 |  |
| **Site: UW (vs UAB)** | **-1.0839** | 0.2350 | ±0.4701 | **-4.612** | **3.99e-06** | *** |
| Season: spring (vs autumn) | -0.2111 | 0.2724 | ±0.5448 | -0.775 | 0.4384 |  |
| **Season: summer (vs autumn)** | **+1.7948** | 0.3208 | ±0.6415 | **+5.595** | **2.20e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5262** | 0.2812 | ±0.5625 | **-5.426** | **5.75e-08** | *** |
| Age (years) | +0.0078 | 0.0086 | ±0.0171 | +0.909 | 0.3636 |  |
| BMI (kg/m2) | +0.0208 | 0.0158 | ±0.0315 | +1.323 | 0.1859 |  |
| Hypertension | -0.0932 | 0.2127 | ±0.4254 | -0.438 | 0.6612 |  |
| High cholesterol | -0.3406 | 0.1917 | ±0.3833 | -1.777 | 0.0756 | . |
| **Kidney disease** | **+0.9286** | 0.3638 | ±0.7275 | **+2.553** | **0.0107** | * |
| **Circulatory disease** | **+0.8076** | 0.3579 | ±0.7158 | **+2.256** | **0.0241** | * |
| GMI (%) | -0.0125 | 0.5225 | ±1.0450 | -0.024 | 0.9809 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **443**, R² = **0.3419**, Adj R² = **0.3203**, F-statistic = **15.88** (p = **3.27e-31**), Residual SE = **1.892** on **428** df, AIC = **1836.9**, BIC = **1898.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.1050** | 1.3521 | ±2.7041 | **+18.568** | **5.86e-77** | *** |
| Education: graduate level (vs college) | +0.0457 | 0.1987 | ±0.3974 | +0.230 | 0.8180 |  |
| Education: high school or below (vs college) | +0.2818 | 0.3641 | ±0.7282 | +0.774 | 0.4390 |  |
| Site: UCSD (vs UAB) | -0.2466 | 0.2382 | ±0.4764 | -1.035 | 0.3005 |  |
| **Site: UW (vs UAB)** | **-1.0630** | 0.2362 | ±0.4723 | **-4.501** | **6.77e-06** | *** |
| Season: spring (vs autumn) | -0.2193 | 0.2727 | ±0.5455 | -0.804 | 0.4215 |  |
| **Season: summer (vs autumn)** | **+1.7950** | 0.3206 | ±0.6413 | **+5.598** | **2.17e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5303** | 0.2811 | ±0.5622 | **-5.444** | **5.20e-08** | *** |
| Age (years) | +0.0065 | 0.0086 | ±0.0173 | +0.756 | 0.4498 |  |
| BMI (kg/m2) | +0.0230 | 0.0165 | ±0.0330 | +1.393 | 0.1637 |  |
| Hypertension | -0.0809 | 0.2126 | ±0.4253 | -0.380 | 0.7038 |  |
| High cholesterol | -0.3427 | 0.1909 | ±0.3819 | -1.795 | 0.0727 | . |
| **Kidney disease** | **+0.9198** | 0.3586 | ±0.7173 | **+2.565** | **0.0103** | * |
| **Circulatory disease** | **+0.8041** | 0.3569 | ±0.7138 | **+2.253** | **0.0243** | * |
| Nocturnal mean 00-06h (mg/dL) | -0.0102 | 0.0098 | ±0.0196 | -1.034 | 0.3012 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **443**, R² = **0.3441**, Adj R² = **0.3227**, F-statistic = **16.04** (p = **1.62e-31**), Residual SE = **1.889** on **428** df, AIC = **1835.3**, BIC = **1896.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9437** | 1.0674 | ±2.1347 | **+23.370** | **8.72e-121** | *** |
| Education: graduate level (vs college) | +0.0347 | 0.1997 | ±0.3995 | +0.174 | 0.8620 |  |
| Education: high school or below (vs college) | +0.3049 | 0.3590 | ±0.7181 | +0.849 | 0.3957 |  |
| Site: UCSD (vs UAB) | -0.2933 | 0.2352 | ±0.4705 | -1.247 | 0.2124 |  |
| **Site: UW (vs UAB)** | **-1.1085** | 0.2340 | ±0.4681 | **-4.736** | **2.18e-06** | *** |
| Season: spring (vs autumn) | -0.1934 | 0.2733 | ±0.5466 | -0.708 | 0.4791 |  |
| **Season: summer (vs autumn)** | **+1.8002** | 0.3185 | ±0.6370 | **+5.652** | **1.59e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5015** | 0.2821 | ±0.5642 | **-5.322** | **1.03e-07** | *** |
| Age (years) | +0.0081 | 0.0085 | ±0.0170 | +0.947 | 0.3434 |  |
| BMI (kg/m2) | +0.0217 | 0.0158 | ±0.0316 | +1.372 | 0.1700 |  |
| Hypertension | -0.0728 | 0.2122 | ±0.4244 | -0.343 | 0.7317 |  |
| High cholesterol | -0.3584 | 0.1915 | ±0.3831 | -1.871 | 0.0613 | . |
| **Kidney disease** | **+0.9827** | 0.3793 | ±0.7586 | **+2.591** | **0.0096** | ** |
| **Circulatory disease** | **+0.8241** | 0.3633 | ±0.7265 | **+2.269** | **0.0233** | * |
| Glucose SD, pooled (mg/dL) | -0.0623 | 0.0408 | ±0.0815 | -1.529 | 0.1262 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **443**, R² = **0.3464**, Adj R² = **0.3250**, F-statistic = **16.20** (p = **8.01e-32**), Residual SE = **1.886** on **428** df, AIC = **1833.8**, BIC = **1895.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.0452** | 1.0449 | ±2.0898 | **+23.969** | **5.87e-127** | *** |
| Education: graduate level (vs college) | +0.0258 | 0.2003 | ±0.4007 | +0.129 | 0.8975 |  |
| Education: high school or below (vs college) | +0.2932 | 0.3636 | ±0.7273 | +0.806 | 0.4200 |  |
| Site: UCSD (vs UAB) | -0.2911 | 0.2345 | ±0.4690 | -1.242 | 0.2144 |  |
| **Site: UW (vs UAB)** | **-1.1086** | 0.2326 | ±0.4652 | **-4.766** | **1.88e-06** | *** |
| Season: spring (vs autumn) | -0.1970 | 0.2730 | ±0.5461 | -0.722 | 0.4706 |  |
| **Season: summer (vs autumn)** | **+1.7956** | 0.3183 | ±0.6366 | **+5.641** | **1.69e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5135** | 0.2793 | ±0.5587 | **-5.418** | **6.02e-08** | *** |
| Age (years) | +0.0084 | 0.0085 | ±0.0169 | +0.991 | 0.3218 |  |
| BMI (kg/m2) | +0.0227 | 0.0161 | ±0.0322 | +1.414 | 0.1574 |  |
| Hypertension | -0.0781 | 0.2121 | ±0.4242 | -0.368 | 0.7129 |  |
| High cholesterol | -0.3601 | 0.1913 | ±0.3827 | -1.882 | 0.0598 | . |
| **Kidney disease** | **+0.9939** | 0.3830 | ±0.7660 | **+2.595** | **0.0095** | ** |
| **Circulatory disease** | **+0.8109** | 0.3633 | ±0.7265 | **+2.232** | **0.0256** | * |
| Avg. daily SD (mg/dL) | -0.0770 | 0.0420 | ±0.0840 | -1.834 | 0.0666 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **443**, R² = **0.3442**, Adj R² = **0.3228**, F-statistic = **16.05** (p = **1.57e-31**), Residual SE = **1.889** on **428** df, AIC = **1835.3**, BIC = **1896.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.9306** | 1.0652 | ±2.1304 | **+23.405** | **3.81e-121** | *** |
| Education: graduate level (vs college) | +0.0330 | 0.1997 | ±0.3993 | +0.165 | 0.8687 |  |
| Education: high school or below (vs college) | +0.3128 | 0.3570 | ±0.7140 | +0.876 | 0.3809 |  |
| Site: UCSD (vs UAB) | -0.3009 | 0.2354 | ±0.4707 | -1.278 | 0.2011 |  |
| **Site: UW (vs UAB)** | **-1.1177** | 0.2340 | ±0.4679 | **-4.777** | **1.78e-06** | *** |
| Season: spring (vs autumn) | -0.1844 | 0.2727 | ±0.5455 | -0.676 | 0.4990 |  |
| **Season: summer (vs autumn)** | **+1.8037** | 0.3185 | ±0.6371 | **+5.663** | **1.49e-08** | *** |
| **Season: winter (vs autumn)** | **-1.4949** | 0.2825 | ±0.5649 | **-5.292** | **1.21e-07** | *** |
| Age (years) | +0.0082 | 0.0085 | ±0.0170 | +0.966 | 0.3342 |  |
| BMI (kg/m2) | +0.0211 | 0.0158 | ±0.0315 | +1.337 | 0.1813 |  |
| Hypertension | -0.0829 | 0.2118 | ±0.4236 | -0.391 | 0.6956 |  |
| High cholesterol | -0.3534 | 0.1916 | ±0.3832 | -1.844 | 0.0652 | . |
| **Kidney disease** | **+0.9711** | 0.3792 | ±0.7584 | **+2.561** | **0.0104** | * |
| **Circulatory disease** | **+0.8237** | 0.3634 | ±0.7268 | **+2.267** | **0.0234** | * |
| CV (%) | -0.0694 | 0.0449 | ±0.0897 | -1.546 | 0.1222 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **443**, R² = **0.3434**, Adj R² = **0.3220**, F-statistic = **15.99** (p = **2.01e-31**), Residual SE = **1.890** on **428** df, AIC = **1835.8**, BIC = **1897.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.0402** | 1.0217 | ±2.0434 | **+22.551** | **1.33e-112** | *** |
| Education: graduate level (vs college) | +0.0324 | 0.2003 | ±0.4007 | +0.162 | 0.8714 |  |
| Education: high school or below (vs college) | +0.3138 | 0.3572 | ±0.7143 | +0.879 | 0.3796 |  |
| Site: UCSD (vs UAB) | -0.2931 | 0.2349 | ±0.4699 | -1.247 | 0.2122 |  |
| **Site: UW (vs UAB)** | **-1.1098** | 0.2334 | ±0.4668 | **-4.755** | **1.98e-06** | *** |
| Season: spring (vs autumn) | -0.1850 | 0.2725 | ±0.5450 | -0.679 | 0.4972 |  |
| **Season: summer (vs autumn)** | **+1.8021** | 0.3190 | ±0.6379 | **+5.650** | **1.61e-08** | *** |
| **Season: winter (vs autumn)** | **-1.4987** | 0.2821 | ±0.5641 | **-5.313** | **1.08e-07** | *** |
| Age (years) | +0.0080 | 0.0085 | ±0.0170 | +0.948 | 0.3431 |  |
| BMI (kg/m2) | +0.0210 | 0.0157 | ±0.0314 | +1.339 | 0.1804 |  |
| Hypertension | -0.0834 | 0.2118 | ±0.4236 | -0.394 | 0.6936 |  |
| High cholesterol | -0.3532 | 0.1915 | ±0.3830 | -1.844 | 0.0651 | . |
| **Kidney disease** | **+0.9561** | 0.3749 | ±0.7497 | **+2.551** | **0.0108** | * |
| **Circulatory disease** | **+0.8172** | 0.3622 | ±0.7245 | **+2.256** | **0.0241** | * |
| Mean / SD ratio | +0.1265 | 0.0939 | ±0.1877 | +1.348 | 0.1776 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **443**, R² = **0.3451**, Adj R² = **0.3236**, F-statistic = **16.11** (p = **1.22e-31**), Residual SE = **1.887** on **428** df, AIC = **1834.7**, BIC = **1896.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+22.9383** | 1.0102 | ±2.0204 | **+22.707** | **3.81e-114** | *** |
| Education: graduate level (vs college) | +0.0239 | 0.2023 | ±0.4046 | +0.118 | 0.9058 |  |
| Education: high school or below (vs college) | +0.3078 | 0.3604 | ±0.7208 | +0.854 | 0.3930 |  |
| Site: UCSD (vs UAB) | -0.2893 | 0.2342 | ±0.4685 | -1.235 | 0.2169 |  |
| **Site: UW (vs UAB)** | **-1.1084** | 0.2318 | ±0.4636 | **-4.781** | **1.74e-06** | *** |
| Season: spring (vs autumn) | -0.1819 | 0.2726 | ±0.5452 | -0.667 | 0.5046 |  |
| **Season: summer (vs autumn)** | **+1.8054** | 0.3191 | ±0.6382 | **+5.658** | **1.53e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5048** | 0.2803 | ±0.5606 | **-5.368** | **7.95e-08** | *** |
| Age (years) | +0.0084 | 0.0084 | ±0.0169 | +1.001 | 0.3170 |  |
| BMI (kg/m2) | +0.0219 | 0.0158 | ±0.0316 | +1.386 | 0.1658 |  |
| Hypertension | -0.0897 | 0.2115 | ±0.4231 | -0.424 | 0.6717 |  |
| High cholesterol | -0.3513 | 0.1916 | ±0.3832 | -1.833 | 0.0667 | . |
| **Kidney disease** | **+0.9626** | 0.3753 | ±0.7506 | **+2.565** | **0.0103** | * |
| **Circulatory disease** | **+0.7998** | 0.3601 | ±0.7203 | **+2.221** | **0.0264** | * |
| Avg. daily mean/SD | +0.1191 | 0.0796 | ±0.1592 | +1.497 | 0.1345 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **443**, R² = **0.3418**, Adj R² = **0.3203**, F-statistic = **15.88** (p = **3.33e-31**), Residual SE = **1.892** on **428** df, AIC = **1836.9**, BIC = **1898.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.5645** | 1.0729 | ±2.1458 | **+22.895** | **5.16e-116** | *** |
| Education: graduate level (vs college) | +0.0559 | 0.1980 | ±0.3960 | +0.283 | 0.7775 |  |
| Education: high school or below (vs college) | +0.3255 | 0.3608 | ±0.7215 | +0.902 | 0.3669 |  |
| Site: UCSD (vs UAB) | -0.2808 | 0.2356 | ±0.4712 | -1.192 | 0.2332 |  |
| **Site: UW (vs UAB)** | **-1.1092** | 0.2348 | ±0.4696 | **-4.724** | **2.32e-06** | *** |
| Season: spring (vs autumn) | -0.2107 | 0.2733 | ±0.5466 | -0.771 | 0.4409 |  |
| **Season: summer (vs autumn)** | **+1.7869** | 0.3225 | ±0.6451 | **+5.540** | **3.02e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5210** | 0.2814 | ±0.5627 | **-5.406** | **6.44e-08** | *** |
| Age (years) | +0.0070 | 0.0086 | ±0.0172 | +0.810 | 0.4180 |  |
| BMI (kg/m2) | +0.0201 | 0.0159 | ±0.0318 | +1.267 | 0.2053 |  |
| Hypertension | -0.0975 | 0.2117 | ±0.4235 | -0.461 | 0.6451 |  |
| High cholesterol | -0.3356 | 0.1921 | ±0.3841 | -1.747 | 0.0806 | . |
| **Kidney disease** | **+0.9496** | 0.3668 | ±0.7335 | **+2.589** | **0.0096** | ** |
| **Circulatory disease** | **+0.7957** | 0.3580 | ±0.7160 | **+2.223** | **0.0262** | * |
| MAG (mg/dL/h) | -0.0162 | 0.0164 | ±0.0327 | -0.990 | 0.3222 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **443**, R² = **0.3508**, Adj R² = **0.3296**, F-statistic = **16.52** (p = **2.05e-32**), Residual SE = **1.879** on **428** df, AIC = **1830.8**, BIC = **1892.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.6899** | 1.0981 | ±2.1962 | **+23.395** | **4.82e-121** | *** |
| Education: graduate level (vs college) | +0.0369 | 0.1972 | ±0.3944 | +0.187 | 0.8518 |  |
| Education: high school or below (vs college) | +0.3056 | 0.3683 | ±0.7365 | +0.830 | 0.4066 |  |
| Site: UCSD (vs UAB) | -0.3027 | 0.2325 | ±0.4651 | -1.302 | 0.1931 |  |
| **Site: UW (vs UAB)** | **-1.1204** | 0.2323 | ±0.4646 | **-4.823** | **1.41e-06** | *** |
| Season: spring (vs autumn) | -0.1874 | 0.2712 | ±0.5425 | -0.691 | 0.4896 |  |
| **Season: summer (vs autumn)** | **+1.7982** | 0.3179 | ±0.6358 | **+5.657** | **1.54e-08** | *** |
| **Season: winter (vs autumn)** | **-1.4972** | 0.2777 | ±0.5555 | **-5.391** | **7.01e-08** | *** |
| Age (years) | +0.0082 | 0.0083 | ±0.0167 | +0.986 | 0.3242 |  |
| BMI (kg/m2) | +0.0183 | 0.0152 | ±0.0304 | +1.203 | 0.2292 |  |
| Hypertension | -0.1057 | 0.2109 | ±0.4219 | -0.501 | 0.6163 |  |
| High cholesterol | -0.3429 | 0.1903 | ±0.3806 | -1.802 | 0.0715 | . |
| **Kidney disease** | **+0.9788** | 0.3822 | ±0.7644 | **+2.561** | **0.0104** | * |
| **Circulatory disease** | **+0.8058** | 0.3596 | ±0.7192 | **+2.241** | **0.0250** | * |
| **Avg. daily range (mg/dL)** | **-0.0213** | 0.0085 | ±0.0170 | **-2.505** | **0.0122** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **443**, R² = **0.3419**, Adj R² = **0.3204**, F-statistic = **15.88** (p = **3.22e-31**), Residual SE = **1.892** on **428** df, AIC = **1836.9**, BIC = **1898.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.6831** | 0.8496 | ±1.6992 | **+27.876** | **5.19e-171** | *** |
| Education: graduate level (vs college) | +0.0450 | 0.1980 | ±0.3960 | +0.227 | 0.8203 |  |
| Education: high school or below (vs college) | +0.2737 | 0.3643 | ±0.7286 | +0.751 | 0.4524 |  |
| Site: UCSD (vs UAB) | -0.2560 | 0.2353 | ±0.4706 | -1.088 | 0.2765 |  |
| **Site: UW (vs UAB)** | **-1.0850** | 0.2346 | ±0.4693 | **-4.624** | **3.76e-06** | *** |
| Season: spring (vs autumn) | -0.2277 | 0.2729 | ±0.5458 | -0.834 | 0.4041 |  |
| **Season: summer (vs autumn)** | **+1.7804** | 0.3216 | ±0.6433 | **+5.536** | **3.10e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5473** | 0.2823 | ±0.5646 | **-5.481** | **4.23e-08** | *** |
| Age (years) | +0.0080 | 0.0085 | ±0.0171 | +0.936 | 0.3494 |  |
| BMI (kg/m2) | +0.0207 | 0.0156 | ±0.0311 | +1.326 | 0.1848 |  |
| Hypertension | -0.1136 | 0.2147 | ±0.4293 | -0.529 | 0.5966 |  |
| High cholesterol | -0.3473 | 0.1905 | ±0.3811 | -1.823 | 0.0683 | . |
| **Kidney disease** | **+0.9322** | 0.3636 | ±0.7271 | **+2.564** | **0.0103** | * |
| **Circulatory disease** | **+0.7804** | 0.3535 | ±0.7071 | **+2.207** | **0.0273** | * |
| SD of daily means (mg/dL) | +0.0526 | 0.0459 | ±0.0919 | +1.144 | 0.2527 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **443**, R² = **0.3430**, Adj R² = **0.3215**, F-statistic = **15.96** (p = **2.30e-31**), Residual SE = **1.890** on **428** df, AIC = **1836.1**, BIC = **1897.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -17.1394 | 30.1737 | ±60.3473 | -0.568 | 0.5700 |  |
| Education: graduate level (vs college) | +0.0473 | 0.1979 | ±0.3958 | +0.239 | 0.8110 |  |
| Education: high school or below (vs college) | +0.2919 | 0.3622 | ±0.7243 | +0.806 | 0.4202 |  |
| Site: UCSD (vs UAB) | -0.2914 | 0.2342 | ±0.4683 | -1.244 | 0.2134 |  |
| **Site: UW (vs UAB)** | **-1.1007** | 0.2354 | ±0.4709 | **-4.675** | **2.94e-06** | *** |
| Season: spring (vs autumn) | -0.2078 | 0.2734 | ±0.5469 | -0.760 | 0.4472 |  |
| **Season: summer (vs autumn)** | **+1.8027** | 0.3219 | ±0.6439 | **+5.599** | **2.15e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5099** | 0.2804 | ±0.5608 | **-5.385** | **7.24e-08** | *** |
| Age (years) | +0.0075 | 0.0085 | ±0.0170 | +0.878 | 0.3802 |  |
| BMI (kg/m2) | +0.0201 | 0.0152 | ±0.0305 | +1.317 | 0.1879 |  |
| Hypertension | -0.0897 | 0.2120 | ±0.4240 | -0.423 | 0.6721 |  |
| High cholesterol | -0.3325 | 0.1924 | ±0.3848 | -1.728 | 0.0839 | . |
| **Kidney disease** | **+0.9585** | 0.3758 | ±0.7516 | **+2.551** | **0.0108** | * |
| **Circulatory disease** | **+0.8022** | 0.3608 | ±0.7216 | **+2.223** | **0.0262** | * |
| Time in range 70-180, pooled (%) | +0.4131 | 0.3034 | ±0.6068 | +1.361 | 0.1734 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **443**, R² = **0.3419**, Adj R² = **0.3204**, F-statistic = **15.88** (p = **3.20e-31**), Residual SE = **1.892** on **428** df, AIC = **1836.8**, BIC = **1898.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -7.3655 | 29.8300 | ±59.6600 | -0.247 | 0.8050 |  |
| Education: graduate level (vs college) | +0.0459 | 0.1985 | ±0.3970 | +0.232 | 0.8169 |  |
| Education: high school or below (vs college) | +0.2909 | 0.3629 | ±0.7257 | +0.802 | 0.4228 |  |
| Site: UCSD (vs UAB) | -0.2779 | 0.2349 | ±0.4698 | -1.183 | 0.2367 |  |
| **Site: UW (vs UAB)** | **-1.0873** | 0.2352 | ±0.4705 | **-4.622** | **3.79e-06** | *** |
| Season: spring (vs autumn) | -0.2135 | 0.2734 | ±0.5469 | -0.781 | 0.4350 |  |
| **Season: summer (vs autumn)** | **+1.7872** | 0.3217 | ±0.6433 | **+5.556** | **2.76e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5222** | 0.2808 | ±0.5617 | **-5.420** | **5.95e-08** | *** |
| Age (years) | +0.0075 | 0.0086 | ±0.0171 | +0.872 | 0.3830 |  |
| BMI (kg/m2) | +0.0206 | 0.0157 | ±0.0313 | +1.319 | 0.1872 |  |
| Hypertension | -0.1006 | 0.2125 | ±0.4249 | -0.473 | 0.6359 |  |
| High cholesterol | -0.3301 | 0.1930 | ±0.3860 | -1.710 | 0.0872 | . |
| **Kidney disease** | **+0.9421** | 0.3758 | ±0.7515 | **+2.507** | **0.0122** | * |
| **Circulatory disease** | **+0.8099** | 0.3607 | ±0.7214 | **+2.245** | **0.0247** | * |
| Avg. daily time in range 70-180 (%) | +0.3145 | 0.2999 | ±0.5998 | +1.049 | 0.2943 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.3405**, Adj R² = **0.3189**, F-statistic = **15.78** (p = **5.01e-31**), Residual SE = **1.894** on **428** df, AIC = **1837.8**, BIC = **1899.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9606** | 0.8245 | ±1.6490 | **+29.061** | **1.12e-185** | *** |
| Education: graduate level (vs college) | +0.0510 | 0.1983 | ±0.3966 | +0.257 | 0.7970 |  |
| Education: high school or below (vs college) | +0.2936 | 0.3596 | ±0.7192 | +0.816 | 0.4143 |  |
| Site: UCSD (vs UAB) | -0.2907 | 0.2416 | ±0.4832 | -1.203 | 0.2290 |  |
| **Site: UW (vs UAB)** | **-1.0956** | 0.2407 | ±0.4815 | **-4.551** | **5.34e-06** | *** |
| Season: spring (vs autumn) | -0.1972 | 0.2746 | ±0.5492 | -0.718 | 0.4728 |  |
| **Season: summer (vs autumn)** | **+1.8032** | 0.3197 | ±0.6394 | **+5.640** | **1.70e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5140** | 0.2809 | ±0.5618 | **-5.389** | **7.07e-08** | *** |
| Age (years) | +0.0077 | 0.0085 | ±0.0171 | +0.901 | 0.3678 |  |
| BMI (kg/m2) | +0.0208 | 0.0157 | ±0.0314 | +1.324 | 0.1854 |  |
| Hypertension | -0.0864 | 0.2092 | ±0.4184 | -0.413 | 0.6796 |  |
| High cholesterol | -0.3405 | 0.1914 | ±0.3828 | -1.779 | 0.0753 | . |
| **Kidney disease** | **+0.9151** | 0.3636 | ±0.7273 | **+2.517** | **0.0118** | * |
| **Circulatory disease** | **+0.8115** | 0.3589 | ±0.7179 | **+2.261** | **0.0238** | * |
| Any reading < 54 during wear (0/1) | -0.1142 | 0.2647 | ±0.5294 | -0.432 | 0.6660 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.3403**, Adj R² = **0.3187**, F-statistic = **15.77** (p = **5.32e-31**), Residual SE = **1.894** on **428** df, AIC = **1838.0**, BIC = **1899.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9511** | 0.8237 | ±1.6474 | **+29.077** | **7.04e-186** | *** |
| Education: graduate level (vs college) | +0.0521 | 0.1992 | ±0.3983 | +0.262 | 0.7935 |  |
| Education: high school or below (vs college) | +0.2916 | 0.3602 | ±0.7203 | +0.810 | 0.4181 |  |
| Site: UCSD (vs UAB) | -0.2800 | 0.2376 | ±0.4752 | -1.178 | 0.2386 |  |
| **Site: UW (vs UAB)** | **-1.0889** | 0.2376 | ±0.4752 | **-4.583** | **4.59e-06** | *** |
| Season: spring (vs autumn) | -0.2116 | 0.2740 | ±0.5479 | -0.772 | 0.4399 |  |
| **Season: summer (vs autumn)** | **+1.7955** | 0.3218 | ±0.6435 | **+5.580** | **2.40e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5235** | 0.2813 | ±0.5627 | **-5.415** | **6.13e-08** | *** |
| Age (years) | +0.0076 | 0.0085 | ±0.0170 | +0.892 | 0.3724 |  |
| BMI (kg/m2) | +0.0211 | 0.0158 | ±0.0315 | +1.338 | 0.1808 |  |
| Hypertension | -0.0877 | 0.2077 | ±0.4154 | -0.422 | 0.6730 |  |
| High cholesterol | -0.3423 | 0.1910 | ±0.3819 | -1.792 | 0.0731 | . |
| **Kidney disease** | **+0.9229** | 0.3639 | ±0.7279 | **+2.536** | **0.0112** | * |
| **Circulatory disease** | **+0.8107** | 0.3590 | ±0.7180 | **+2.258** | **0.0239** | * |
| Time < 54 (%) | -0.5017 | 2.5207 | ±5.0414 | -0.199 | 0.8422 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.3402**, Adj R² = **0.3186**, F-statistic = **15.76** (p = **5.52e-31**), Residual SE = **1.894** on **428** df, AIC = **1838.0**, BIC = **1899.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9378** | 0.8222 | ±1.6444 | **+29.114** | **2.42e-186** | *** |
| Education: graduate level (vs college) | +0.0521 | 0.1990 | ±0.3981 | +0.262 | 0.7934 |  |
| Education: high school or below (vs college) | +0.2971 | 0.3608 | ±0.7216 | +0.824 | 0.4102 |  |
| Site: UCSD (vs UAB) | -0.2717 | 0.2363 | ±0.4727 | -1.150 | 0.2503 |  |
| **Site: UW (vs UAB)** | **-1.0844** | 0.2360 | ±0.4719 | **-4.596** | **4.31e-06** | *** |
| Season: spring (vs autumn) | -0.2114 | 0.2745 | ±0.5489 | -0.770 | 0.4412 |  |
| **Season: summer (vs autumn)** | **+1.7934** | 0.3214 | ±0.6429 | **+5.579** | **2.41e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5262** | 0.2821 | ±0.5643 | **-5.409** | **6.32e-08** | *** |
| Age (years) | +0.0078 | 0.0086 | ±0.0172 | +0.905 | 0.3654 |  |
| BMI (kg/m2) | +0.0209 | 0.0157 | ±0.0314 | +1.328 | 0.1840 |  |
| Hypertension | -0.0929 | 0.2124 | ±0.4247 | -0.437 | 0.6618 |  |
| High cholesterol | -0.3404 | 0.1914 | ±0.3829 | -1.778 | 0.0754 | . |
| **Kidney disease** | **+0.9275** | 0.3637 | ±0.7275 | **+2.550** | **0.0108** | * |
| **Circulatory disease** | **+0.8090** | 0.3592 | ±0.7184 | **+2.252** | **0.0243** | * |
| Avg. daily time < 54 (%) | -0.1901 | 2.8160 | ±5.6320 | -0.068 | 0.9462 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.3447**, Adj R² = **0.3233**, F-statistic = **16.08** (p = **1.35e-31**), Residual SE = **1.888** on **428** df, AIC = **1835.0**, BIC = **1896.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0663** | 0.8295 | ±1.6591 | **+29.012** | **4.64e-185** | *** |
| Education: graduate level (vs college) | +0.0434 | 0.1980 | ±0.3959 | +0.219 | 0.8263 |  |
| Education: high school or below (vs college) | +0.3317 | 0.3584 | ±0.7168 | +0.925 | 0.3547 |  |
| Site: UCSD (vs UAB) | -0.2967 | 0.2354 | ±0.4708 | -1.260 | 0.2075 |  |
| **Site: UW (vs UAB)** | **-1.1154** | 0.2340 | ±0.4680 | **-4.767** | **1.87e-06** | *** |
| Season: spring (vs autumn) | -0.2013 | 0.2742 | ±0.5485 | -0.734 | 0.4629 |  |
| **Season: summer (vs autumn)** | **+1.8026** | 0.3228 | ±0.6457 | **+5.584** | **2.36e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5032** | 0.2816 | ±0.5633 | **-5.338** | **9.42e-08** | *** |
| Age (years) | +0.0078 | 0.0085 | ±0.0171 | +0.911 | 0.3624 |  |
| BMI (kg/m2) | +0.0207 | 0.0159 | ±0.0318 | +1.304 | 0.1923 |  |
| Hypertension | -0.1139 | 0.2122 | ±0.4245 | -0.537 | 0.5914 |  |
| High cholesterol | -0.3127 | 0.1912 | ±0.3824 | -1.635 | 0.1020 |  |
| **Kidney disease** | **+0.8787** | 0.3678 | ±0.7356 | **+2.389** | **0.0169** | * |
| **Circulatory disease** | **+0.8007** | 0.3582 | ±0.7164 | **+2.235** | **0.0254** | * |
| Time 54-69, pooled (%) | -0.8674 | 0.4949 | ±0.9898 | -1.753 | 0.0796 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **443**, R² = **0.3425**, Adj R² = **0.3210**, F-statistic = **15.93** (p = **2.65e-31**), Residual SE = **1.891** on **428** df, AIC = **1836.4**, BIC = **1897.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0185** | 0.8256 | ±1.6513 | **+29.091** | **4.68e-186** | *** |
| Education: graduate level (vs college) | +0.0410 | 0.1984 | ±0.3968 | +0.207 | 0.8363 |  |
| Education: high school or below (vs college) | +0.3242 | 0.3575 | ±0.7150 | +0.907 | 0.3645 |  |
| Site: UCSD (vs UAB) | -0.2799 | 0.2354 | ±0.4708 | -1.189 | 0.2345 |  |
| **Site: UW (vs UAB)** | **-1.0970** | 0.2341 | ±0.4682 | **-4.686** | **2.79e-06** | *** |
| Season: spring (vs autumn) | -0.2183 | 0.2736 | ±0.5471 | -0.798 | 0.4249 |  |
| **Season: summer (vs autumn)** | **+1.7833** | 0.3221 | ±0.6441 | **+5.537** | **3.07e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5166** | 0.2823 | ±0.5645 | **-5.373** | **7.75e-08** | *** |
| Age (years) | +0.0079 | 0.0085 | ±0.0171 | +0.928 | 0.3534 |  |
| BMI (kg/m2) | +0.0208 | 0.0158 | ±0.0316 | +1.319 | 0.1873 |  |
| Hypertension | -0.1231 | 0.2115 | ±0.4229 | -0.582 | 0.5606 |  |
| High cholesterol | -0.3222 | 0.1919 | ±0.3837 | -1.679 | 0.0931 | . |
| **Kidney disease** | **+0.9035** | 0.3677 | ±0.7354 | **+2.457** | **0.0140** | * |
| **Circulatory disease** | **+0.8112** | 0.3582 | ±0.7165 | **+2.264** | **0.0235** | * |
| Avg. daily time 54-69 (%) | -0.6371 | 0.4792 | ±0.9584 | -1.329 | 0.1837 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **443**, R² = **0.3441**, Adj R² = **0.3227**, F-statistic = **16.04** (p = **1.62e-31**), Residual SE = **1.889** on **428** df, AIC = **1835.4**, BIC = **1896.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0672** | 0.8316 | ±1.6631 | **+28.942** | **3.56e-184** | *** |
| Education: graduate level (vs college) | +0.0451 | 0.1984 | ±0.3968 | +0.227 | 0.8201 |  |
| Education: high school or below (vs college) | +0.3169 | 0.3580 | ±0.7161 | +0.885 | 0.3761 |  |
| Site: UCSD (vs UAB) | -0.3059 | 0.2351 | ±0.4703 | -1.301 | 0.1933 |  |
| **Site: UW (vs UAB)** | **-1.1169** | 0.2349 | ±0.4698 | **-4.754** | **1.99e-06** | *** |
| Season: spring (vs autumn) | -0.2041 | 0.2742 | ±0.5485 | -0.744 | 0.4568 |  |
| **Season: summer (vs autumn)** | **+1.8023** | 0.3230 | ±0.6459 | **+5.581** | **2.40e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5035** | 0.2815 | ±0.5629 | **-5.342** | **9.20e-08** | *** |
| Age (years) | +0.0075 | 0.0085 | ±0.0171 | +0.876 | 0.3808 |  |
| BMI (kg/m2) | +0.0212 | 0.0160 | ±0.0319 | +1.325 | 0.1852 |  |
| Hypertension | -0.1021 | 0.2129 | ±0.4257 | -0.480 | 0.6315 |  |
| High cholesterol | -0.3201 | 0.1917 | ±0.3834 | -1.669 | 0.0950 | . |
| **Kidney disease** | **+0.8793** | 0.3671 | ±0.7342 | **+2.395** | **0.0166** | * |
| **Circulatory disease** | **+0.8065** | 0.3585 | ±0.7169 | **+2.250** | **0.0245** | * |
| Time < 70 (%) | -0.7209 | 0.4632 | ±0.9264 | -1.556 | 0.1196 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **443**, R² = **0.3422**, Adj R² = **0.3207**, F-statistic = **15.90** (p = **2.94e-31**), Residual SE = **1.892** on **428** df, AIC = **1836.7**, BIC = **1898.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.0138** | 0.8262 | ±1.6523 | **+29.067** | **9.51e-186** | *** |
| Education: graduate level (vs college) | +0.0432 | 0.1985 | ±0.3970 | +0.218 | 0.8278 |  |
| Education: high school or below (vs college) | +0.3180 | 0.3581 | ±0.7162 | +0.888 | 0.3745 |  |
| Site: UCSD (vs UAB) | -0.2819 | 0.2353 | ±0.4707 | -1.198 | 0.2310 |  |
| **Site: UW (vs UAB)** | **-1.0957** | 0.2345 | ±0.4691 | **-4.672** | **2.99e-06** | *** |
| Season: spring (vs autumn) | -0.2189 | 0.2736 | ±0.5473 | -0.800 | 0.4237 |  |
| **Season: summer (vs autumn)** | **+1.7811** | 0.3223 | ±0.6445 | **+5.527** | **3.26e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5186** | 0.2821 | ±0.5641 | **-5.384** | **7.28e-08** | *** |
| Age (years) | +0.0078 | 0.0085 | ±0.0171 | +0.917 | 0.3592 |  |
| BMI (kg/m2) | +0.0209 | 0.0158 | ±0.0316 | +1.324 | 0.1857 |  |
| Hypertension | -0.1168 | 0.2118 | ±0.4236 | -0.551 | 0.5813 |  |
| High cholesterol | -0.3250 | 0.1919 | ±0.3839 | -1.693 | 0.0904 | . |
| **Kidney disease** | **+0.9049** | 0.3673 | ±0.7345 | **+2.464** | **0.0137** | * |
| **Circulatory disease** | **+0.8147** | 0.3586 | ±0.7171 | **+2.272** | **0.0231** | * |
| Avg. daily time < 70 (%) | -0.5401 | 0.4387 | ±0.8775 | -1.231 | 0.2183 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.3403**, Adj R² = **0.3188**, F-statistic = **15.77** (p = **5.22e-31**), Residual SE = **1.894** on **428** df, AIC = **1837.9**, BIC = **1899.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -35.8153 | 239.6112 | ±479.2223 | -0.149 | 0.8812 |  |
| Education: graduate level (vs college) | +0.0522 | 0.1992 | ±0.3983 | +0.262 | 0.7932 |  |
| Education: high school or below (vs college) | +0.2902 | 0.3601 | ±0.7202 | +0.806 | 0.4203 |  |
| Site: UCSD (vs UAB) | -0.2827 | 0.2380 | ±0.4760 | -1.188 | 0.2350 |  |
| **Site: UW (vs UAB)** | **-1.0905** | 0.2379 | ±0.4757 | **-4.585** | **4.54e-06** | *** |
| Season: spring (vs autumn) | -0.2112 | 0.2739 | ±0.5478 | -0.771 | 0.4408 |  |
| **Season: summer (vs autumn)** | **+1.7956** | 0.3218 | ±0.6436 | **+5.580** | **2.40e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5225** | 0.2813 | ±0.5625 | **-5.413** | **6.19e-08** | *** |
| Age (years) | +0.0075 | 0.0085 | ±0.0170 | +0.883 | 0.3775 |  |
| BMI (kg/m2) | +0.0211 | 0.0158 | ±0.0315 | +1.341 | 0.1800 |  |
| Hypertension | -0.0868 | 0.2080 | ±0.4159 | -0.418 | 0.6763 |  |
| High cholesterol | -0.3425 | 0.1910 | ±0.3820 | -1.793 | 0.0730 | . |
| **Kidney disease** | **+0.9220** | 0.3638 | ±0.7276 | **+2.534** | **0.0113** | * |
| **Circulatory disease** | **+0.8115** | 0.3590 | ±0.7180 | **+2.260** | **0.0238** | * |
| Time 54-250, pooled (%) | +0.5977 | 2.3966 | ±4.7932 | +0.249 | 0.8030 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.3402**, Adj R² = **0.3186**, F-statistic = **15.76** (p = **5.45e-31**), Residual SE = **1.894** on **428** df, AIC = **1838.0**, BIC = **1899.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -17.3252 | 274.3416 | ±548.6832 | -0.063 | 0.9496 |  |
| Education: graduate level (vs college) | +0.0524 | 0.1990 | ±0.3981 | +0.263 | 0.7925 |  |
| Education: high school or below (vs college) | +0.2960 | 0.3608 | ±0.7216 | +0.821 | 0.4119 |  |
| Site: UCSD (vs UAB) | -0.2738 | 0.2366 | ±0.4733 | -1.157 | 0.2473 |  |
| **Site: UW (vs UAB)** | **-1.0852** | 0.2361 | ±0.4722 | **-4.596** | **4.30e-06** | *** |
| Season: spring (vs autumn) | -0.2117 | 0.2745 | ±0.5490 | -0.771 | 0.4407 |  |
| **Season: summer (vs autumn)** | **+1.7917** | 0.3215 | ±0.6431 | **+5.572** | **2.51e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5260** | 0.2823 | ±0.5646 | **-5.406** | **6.46e-08** | *** |
| Age (years) | +0.0077 | 0.0086 | ±0.0172 | +0.898 | 0.3691 |  |
| BMI (kg/m2) | +0.0209 | 0.0157 | ±0.0314 | +1.329 | 0.1839 |  |
| Hypertension | -0.0924 | 0.2123 | ±0.4247 | -0.435 | 0.6636 |  |
| High cholesterol | -0.3403 | 0.1915 | ±0.3830 | -1.777 | 0.0756 | . |
| **Kidney disease** | **+0.9265** | 0.3638 | ±0.7276 | **+2.547** | **0.0109** | * |
| **Circulatory disease** | **+0.8107** | 0.3593 | ±0.7186 | **+2.256** | **0.0241** | * |
| Avg. daily time 54-250 (%) | +0.4127 | 2.7438 | ±5.4877 | +0.150 | 0.8804 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **443**, R² = **0.3403**, Adj R² = **0.3187**, F-statistic = **15.77** (p = **5.34e-31**), Residual SE = **1.894** on **428** df, AIC = **1838.0**, BIC = **1899.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9685** | 0.8328 | ±1.6656 | **+28.780** | **3.76e-182** | *** |
| Education: graduate level (vs college) | +0.0518 | 0.1983 | ±0.3966 | +0.261 | 0.7940 |  |
| Education: high school or below (vs college) | +0.2943 | 0.3632 | ±0.7264 | +0.810 | 0.4178 |  |
| Site: UCSD (vs UAB) | -0.2705 | 0.2358 | ±0.4716 | -1.147 | 0.2513 |  |
| **Site: UW (vs UAB)** | **-1.0836** | 0.2351 | ±0.4701 | **-4.610** | **4.03e-06** | *** |
| Season: spring (vs autumn) | -0.2111 | 0.2733 | ±0.5467 | -0.772 | 0.4400 |  |
| **Season: summer (vs autumn)** | **+1.7956** | 0.3209 | ±0.6418 | **+5.596** | **2.20e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5253** | 0.2814 | ±0.5628 | **-5.421** | **5.93e-08** | *** |
| Age (years) | +0.0078 | 0.0086 | ±0.0171 | +0.906 | 0.3648 |  |
| BMI (kg/m2) | +0.0206 | 0.0156 | ±0.0312 | +1.320 | 0.1870 |  |
| Hypertension | -0.0916 | 0.2117 | ±0.4234 | -0.433 | 0.6654 |  |
| High cholesterol | -0.3413 | 0.1908 | ±0.3815 | -1.789 | 0.0736 | . |
| **Kidney disease** | **+0.9411** | 0.3653 | ±0.7306 | **+2.576** | **0.0100** | ** |
| **Circulatory disease** | **+0.8065** | 0.3582 | ±0.7165 | **+2.251** | **0.0244** | * |
| Time 181-250, pooled (%) | -0.0906 | 0.3278 | ±0.6556 | -0.276 | 0.7822 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **443**, R² = **0.3404**, Adj R² = **0.3188**, F-statistic = **15.77** (p = **5.19e-31**), Residual SE = **1.894** on **428** df, AIC = **1837.9**, BIC = **1899.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9746** | 0.8314 | ±1.6628 | **+28.836** | **7.60e-183** | *** |
| Education: graduate level (vs college) | +0.0516 | 0.1983 | ±0.3966 | +0.260 | 0.7947 |  |
| Education: high school or below (vs college) | +0.2909 | 0.3644 | ±0.7288 | +0.798 | 0.4247 |  |
| Site: UCSD (vs UAB) | -0.2706 | 0.2358 | ±0.4715 | -1.148 | 0.2510 |  |
| **Site: UW (vs UAB)** | **-1.0827** | 0.2351 | ±0.4702 | **-4.605** | **4.12e-06** | *** |
| Season: spring (vs autumn) | -0.2101 | 0.2734 | ±0.5468 | -0.769 | 0.4421 |  |
| **Season: summer (vs autumn)** | **+1.7950** | 0.3208 | ±0.6415 | **+5.596** | **2.20e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5262** | 0.2812 | ±0.5624 | **-5.427** | **5.72e-08** | *** |
| Age (years) | +0.0077 | 0.0086 | ±0.0172 | +0.892 | 0.3722 |  |
| BMI (kg/m2) | +0.0207 | 0.0156 | ±0.0313 | +1.327 | 0.1846 |  |
| Hypertension | -0.0910 | 0.2121 | ±0.4243 | -0.429 | 0.6680 |  |
| High cholesterol | -0.3399 | 0.1915 | ±0.3830 | -1.775 | 0.0759 | . |
| **Kidney disease** | **+0.9387** | 0.3673 | ±0.7346 | **+2.555** | **0.0106** | * |
| **Circulatory disease** | **+0.8068** | 0.3585 | ±0.7170 | **+2.251** | **0.0244** | * |
| Avg. daily time 181-250 (%) | -0.1193 | 0.3266 | ±0.6532 | -0.365 | 0.7150 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **443**, R² = **0.3403**, Adj R² = **0.3187**, F-statistic = **15.77** (p = **5.32e-31**), Residual SE = **1.894** on **428** df, AIC = **1838.0**, BIC = **1899.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9706** | 0.8332 | ±1.6663 | **+28.771** | **4.98e-182** | *** |
| Education: graduate level (vs college) | +0.0518 | 0.1983 | ±0.3966 | +0.261 | 0.7940 |  |
| Education: high school or below (vs college) | +0.2941 | 0.3632 | ±0.7265 | +0.810 | 0.4182 |  |
| Site: UCSD (vs UAB) | -0.2706 | 0.2358 | ±0.4716 | -1.148 | 0.2511 |  |
| **Site: UW (vs UAB)** | **-1.0837** | 0.2351 | ±0.4701 | **-4.610** | **4.02e-06** | *** |
| Season: spring (vs autumn) | -0.2110 | 0.2733 | ±0.5467 | -0.772 | 0.4402 |  |
| **Season: summer (vs autumn)** | **+1.7956** | 0.3209 | ±0.6418 | **+5.596** | **2.20e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5252** | 0.2814 | ±0.5627 | **-5.421** | **5.94e-08** | *** |
| Age (years) | +0.0078 | 0.0086 | ±0.0171 | +0.905 | 0.3653 |  |
| BMI (kg/m2) | +0.0206 | 0.0156 | ±0.0312 | +1.319 | 0.1871 |  |
| Hypertension | -0.0915 | 0.2117 | ±0.4234 | -0.432 | 0.6655 |  |
| High cholesterol | -0.3413 | 0.1908 | ±0.3815 | -1.789 | 0.0736 | . |
| **Kidney disease** | **+0.9417** | 0.3654 | ±0.7308 | **+2.577** | **0.0100** | ** |
| **Circulatory disease** | **+0.8065** | 0.3583 | ±0.7165 | **+2.251** | **0.0244** | * |
| Time > 180 (%) | -0.0947 | 0.3268 | ±0.6537 | -0.290 | 0.7720 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **443**, R² = **0.3404**, Adj R² = **0.3188**, F-statistic = **15.78** (p = **5.16e-31**), Residual SE = **1.894** on **428** df, AIC = **1837.9**, BIC = **1899.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.9769** | 0.8319 | ±1.6638 | **+28.822** | **1.15e-182** | *** |
| Education: graduate level (vs college) | +0.0516 | 0.1983 | ±0.3966 | +0.260 | 0.7947 |  |
| Education: high school or below (vs college) | +0.2906 | 0.3644 | ±0.7289 | +0.797 | 0.4252 |  |
| Site: UCSD (vs UAB) | -0.2708 | 0.2357 | ±0.4715 | -1.149 | 0.2506 |  |
| **Site: UW (vs UAB)** | **-1.0828** | 0.2351 | ±0.4702 | **-4.606** | **4.11e-06** | *** |
| Season: spring (vs autumn) | -0.2100 | 0.2734 | ±0.5468 | -0.768 | 0.4425 |  |
| **Season: summer (vs autumn)** | **+1.7950** | 0.3208 | ±0.6415 | **+5.596** | **2.20e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5261** | 0.2812 | ±0.5624 | **-5.427** | **5.72e-08** | *** |
| Age (years) | +0.0077 | 0.0086 | ±0.0172 | +0.891 | 0.3731 |  |
| BMI (kg/m2) | +0.0207 | 0.0156 | ±0.0313 | +1.326 | 0.1848 |  |
| Hypertension | -0.0910 | 0.2121 | ±0.4243 | -0.429 | 0.6681 |  |
| High cholesterol | -0.3399 | 0.1915 | ±0.3830 | -1.775 | 0.0759 | . |
| **Kidney disease** | **+0.9391** | 0.3675 | ±0.7349 | **+2.556** | **0.0106** | * |
| **Circulatory disease** | **+0.8068** | 0.3585 | ±0.7170 | **+2.251** | **0.0244** | * |
| Avg. daily time > 180 (%) | -0.1234 | 0.3252 | ±0.6503 | -0.380 | 0.7043 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 443)
**Regression Call / Formula**: `env_temp_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **443**, R² = **0.3408**, Adj R² = **0.3192**, F-statistic = **15.80** (p = **4.54e-31**), Residual SE = **1.894** on **428** df, AIC = **1837.6**, BIC = **1899.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+23.8870** | 0.8228 | ±1.6455 | **+29.033** | **2.53e-185** | *** |
| Education: graduate level (vs college) | +0.0584 | 0.1990 | ±0.3981 | +0.293 | 0.7691 |  |
| Education: high school or below (vs college) | +0.3020 | 0.3602 | ±0.7204 | +0.839 | 0.4017 |  |
| Site: UCSD (vs UAB) | -0.2708 | 0.2356 | ±0.4712 | -1.150 | 0.2503 |  |
| **Site: UW (vs UAB)** | **-1.0888** | 0.2346 | ±0.4692 | **-4.641** | **3.46e-06** | *** |
| Season: spring (vs autumn) | -0.2141 | 0.2728 | ±0.5455 | -0.785 | 0.4324 |  |
| **Season: summer (vs autumn)** | **+1.7981** | 0.3205 | ±0.6410 | **+5.610** | **2.02e-08** | *** |
| **Season: winter (vs autumn)** | **-1.5412** | 0.2820 | ±0.5640 | **-5.465** | **4.62e-08** | *** |
| Age (years) | +0.0087 | 0.0087 | ±0.0175 | +0.995 | 0.3198 |  |
| BMI (kg/m2) | +0.0203 | 0.0156 | ±0.0313 | +1.297 | 0.1945 |  |
| Hypertension | -0.1061 | 0.2138 | ±0.4276 | -0.496 | 0.6198 |  |
| High cholesterol | -0.3438 | 0.1911 | ±0.3822 | -1.800 | 0.0719 | . |
| **Kidney disease** | **+0.9268** | 0.3641 | ±0.7281 | **+2.546** | **0.0109** | * |
| **Circulatory disease** | **+0.8148** | 0.3565 | ±0.7131 | **+2.285** | **0.0223** | * |
| Nocturnal time > 180 (%) | +0.1683 | 0.2121 | ±0.4242 | +0.793 | 0.4276 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor relative humidity, mean (%)  (domain: Home environment; outcome sample N = 443; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **443**, R² = **0.2738**, Adj R² = **0.2518**, F-statistic = **12.44** (p = **3.37e-23**), Residual SE = **5.773** on **429** df, AIC = **2824.3**, BIC = **2881.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.7088** | 2.0049 | ±4.0098 | **+23.796** | **3.65e-125** | *** |
| Education: graduate level (vs college) | +0.8567 | 0.5853 | ±1.1707 | +1.464 | 0.1433 |  |
| Education: high school or below (vs college) | -0.9511 | 1.1068 | ±2.2137 | -0.859 | 0.3902 |  |
| **Site: UCSD (vs UAB)** | **+4.2304** | 0.7382 | ±1.4764 | **+5.731** | **9.99e-09** | *** |
| Site: UW (vs UAB) | -0.6757 | 0.7286 | ±1.4572 | -0.927 | 0.3537 |  |
| Season: spring (vs autumn) | -1.3297 | 0.7771 | ±1.5542 | -1.711 | 0.0871 | . |
| **Season: summer (vs autumn)** | **+3.1606** | 0.8448 | ±1.6896 | **+3.741** | **1.83e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5582** | 0.8665 | ±1.7330 | **-5.260** | **1.44e-07** | *** |
| Age (years) | -0.0344 | 0.0256 | ±0.0512 | -1.342 | 0.1797 |  |
| BMI (kg/m2) | -0.0302 | 0.0379 | ±0.0758 | -0.796 | 0.4263 |  |
| Hypertension | +0.2675 | 0.6471 | ±1.2942 | +0.413 | 0.6794 |  |
| High cholesterol | -0.8454 | 0.5921 | ±1.1841 | -1.428 | 0.1533 |  |
| Kidney disease | -1.1618 | 1.1552 | ±2.3105 | -1.006 | 0.3146 |  |
| Circulatory disease | -0.5109 | 0.8237 | ±1.6475 | -0.620 | 0.5351 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **443**, R² = **0.2761**, Adj R² = **0.2524**, F-statistic = **11.66** (p = **6.66e-23**), Residual SE = **5.771** on **428** df, AIC = **2825.0**, BIC = **2886.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.0700** | 5.1759 | ±10.3517 | **+8.128** | **4.36e-16** | *** |
| Education: graduate level (vs college) | +0.8829 | 0.5852 | ±1.1704 | +1.509 | 0.1313 |  |
| Education: high school or below (vs college) | -1.0292 | 1.1041 | ±2.2083 | -0.932 | 0.3513 |  |
| **Site: UCSD (vs UAB)** | **+4.2177** | 0.7387 | ±1.4774 | **+5.710** | **1.13e-08** | *** |
| Site: UW (vs UAB) | -0.6616 | 0.7252 | ±1.4503 | -0.912 | 0.3616 |  |
| Season: spring (vs autumn) | -1.1894 | 0.7800 | ±1.5601 | -1.525 | 0.1273 |  |
| **Season: summer (vs autumn)** | **+3.1077** | 0.8462 | ±1.6925 | **+3.672** | **2.40e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5068** | 0.8669 | ±1.7337 | **-5.199** | **2.00e-07** | *** |
| Age (years) | -0.0375 | 0.0263 | ±0.0526 | -1.427 | 0.1537 |  |
| BMI (kg/m2) | -0.0357 | 0.0383 | ±0.0765 | -0.934 | 0.3505 |  |
| Hypertension | +0.2053 | 0.6500 | ±1.3001 | +0.316 | 0.7522 |  |
| High cholesterol | -0.9872 | 0.6022 | ±1.2043 | -1.639 | 0.1011 |  |
| Kidney disease | -1.0936 | 1.1696 | ±2.3392 | -0.935 | 0.3498 |  |
| Circulatory disease | -0.4533 | 0.8171 | ±1.6343 | -0.555 | 0.5791 |  |
| HbA1c (%) | +1.0829 | 0.9541 | ±1.9081 | +1.135 | 0.2564 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **443**, R² = **0.2745**, Adj R² = **0.2508**, F-statistic = **11.57** (p = **1.02e-22**), Residual SE = **5.777** on **428** df, AIC = **2825.9**, BIC = **2887.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.1019** | 4.8596 | ±9.7191 | **+9.281** | **1.68e-20** | *** |
| Education: graduate level (vs college) | +0.8516 | 0.5853 | ±1.1705 | +1.455 | 0.1456 |  |
| Education: high school or below (vs college) | -0.9286 | 1.1189 | ±2.2377 | -0.830 | 0.4066 |  |
| **Site: UCSD (vs UAB)** | **+4.2094** | 0.7389 | ±1.4778 | **+5.697** | **1.22e-08** | *** |
| Site: UW (vs UAB) | -0.7007 | 0.7302 | ±1.4604 | -0.960 | 0.3373 |  |
| Season: spring (vs autumn) | -1.3076 | 0.7790 | ±1.5579 | -1.679 | 0.0932 | . |
| **Season: summer (vs autumn)** | **+3.1636** | 0.8482 | ±1.6965 | **+3.730** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5417** | 0.8674 | ±1.7349 | **-5.236** | **1.64e-07** | *** |
| Age (years) | -0.0339 | 0.0257 | ±0.0513 | -1.320 | 0.1867 |  |
| BMI (kg/m2) | -0.0317 | 0.0379 | ±0.0757 | -0.837 | 0.4028 |  |
| Hypertension | +0.2449 | 0.6553 | ±1.3105 | +0.374 | 0.7086 |  |
| High cholesterol | -0.8313 | 0.5941 | ±1.1882 | -1.399 | 0.1618 |  |
| Kidney disease | -1.1858 | 1.1552 | ±2.3104 | -1.026 | 0.3047 |  |
| Circulatory disease | -0.5139 | 0.8232 | ±1.6463 | -0.624 | 0.5324 |  |
| Mean glucose (mg/dL) | +0.0230 | 0.0368 | ±0.0735 | +0.626 | 0.5311 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **443**, R² = **0.2745**, Adj R² = **0.2508**, F-statistic = **11.57** (p = **1.02e-22**), Residual SE = **5.777** on **428** df, AIC = **2825.9**, BIC = **2887.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+41.9167** | 9.7261 | ±19.4522 | **+4.310** | **1.63e-05** | *** |
| Education: graduate level (vs college) | +0.8516 | 0.5853 | ±1.1705 | +1.455 | 0.1456 |  |
| Education: high school or below (vs college) | -0.9286 | 1.1189 | ±2.2377 | -0.830 | 0.4066 |  |
| **Site: UCSD (vs UAB)** | **+4.2094** | 0.7389 | ±1.4778 | **+5.697** | **1.22e-08** | *** |
| Site: UW (vs UAB) | -0.7007 | 0.7302 | ±1.4604 | -0.960 | 0.3373 |  |
| Season: spring (vs autumn) | -1.3076 | 0.7790 | ±1.5579 | -1.679 | 0.0932 | . |
| **Season: summer (vs autumn)** | **+3.1636** | 0.8482 | ±1.6965 | **+3.730** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5417** | 0.8674 | ±1.7349 | **-5.236** | **1.64e-07** | *** |
| Age (years) | -0.0339 | 0.0257 | ±0.0513 | -1.320 | 0.1867 |  |
| BMI (kg/m2) | -0.0317 | 0.0379 | ±0.0757 | -0.837 | 0.4028 |  |
| Hypertension | +0.2449 | 0.6553 | ±1.3105 | +0.374 | 0.7086 |  |
| High cholesterol | -0.8313 | 0.5941 | ±1.1882 | -1.399 | 0.1618 |  |
| Kidney disease | -1.1858 | 1.1552 | ±2.3104 | -1.026 | 0.3047 |  |
| Circulatory disease | -0.5139 | 0.8232 | ±1.6463 | -0.624 | 0.5324 |  |
| GMI (%) | +0.9623 | 1.5365 | ±3.0729 | +0.626 | 0.5311 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **443**, R² = **0.2773**, Adj R² = **0.2536**, F-statistic = **11.73** (p = **4.77e-23**), Residual SE = **5.766** on **428** df, AIC = **2824.2**, BIC = **2885.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+42.8934** | 4.0928 | ±8.1857 | **+10.480** | **1.07e-25** | *** |
| Education: graduate level (vs college) | +0.8823 | 0.5870 | ±1.1740 | +1.503 | 0.1328 |  |
| Education: high school or below (vs college) | -0.8848 | 1.1264 | ±2.2528 | -0.785 | 0.4322 |  |
| **Site: UCSD (vs UAB)** | **+4.1322** | 0.7399 | ±1.4799 | **+5.585** | **2.34e-08** | *** |
| Site: UW (vs UAB) | -0.7631 | 0.7291 | ±1.4582 | -1.047 | 0.2953 |  |
| Season: spring (vs autumn) | -1.2948 | 0.7781 | ±1.5562 | -1.664 | 0.0961 | . |
| **Season: summer (vs autumn)** | **+3.1597** | 0.8491 | ±1.6982 | **+3.721** | **1.98e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5401** | 0.8691 | ±1.7382 | **-5.224** | **1.75e-07** | *** |
| Age (years) | -0.0292 | 0.0261 | ±0.0522 | -1.118 | 0.2635 |  |
| BMI (kg/m2) | -0.0390 | 0.0382 | ±0.0764 | -1.020 | 0.3079 |  |
| Hypertension | +0.2154 | 0.6517 | ±1.3033 | +0.330 | 0.7410 |  |
| High cholesterol | -0.8359 | 0.5921 | ±1.1842 | -1.412 | 0.1580 |  |
| Kidney disease | -1.1268 | 1.1556 | ±2.3112 | -0.975 | 0.3295 |  |
| Circulatory disease | -0.4966 | 0.8138 | ±1.6277 | -0.610 | 0.5417 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0418 | 0.0284 | ±0.0567 | +1.473 | 0.1408 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **443**, R² = **0.2747**, Adj R² = **0.2509**, F-statistic = **11.58** (p = **9.75e-23**), Residual SE = **5.777** on **428** df, AIC = **2825.8**, BIC = **2887.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.0345** | 2.7877 | ±5.5754 | **+17.590** | **2.95e-69** | *** |
| Education: graduate level (vs college) | +0.8341 | 0.5887 | ±1.1775 | +1.417 | 0.1566 |  |
| Education: high school or below (vs college) | -0.9419 | 1.1041 | ±2.2081 | -0.853 | 0.3936 |  |
| **Site: UCSD (vs UAB)** | **+4.2004** | 0.7419 | ±1.4839 | **+5.661** | **1.50e-08** | *** |
| Site: UW (vs UAB) | -0.7076 | 0.7343 | ±1.4685 | -0.964 | 0.3352 |  |
| Season: spring (vs autumn) | -1.3069 | 0.7788 | ±1.5576 | -1.678 | 0.0933 | . |
| **Season: summer (vs autumn)** | **+3.1676** | 0.8481 | ±1.6962 | **+3.735** | **1.88e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5260** | 0.8703 | ±1.7406 | **-5.201** | **1.99e-07** | *** |
| Age (years) | -0.0340 | 0.0257 | ±0.0515 | -1.321 | 0.1864 |  |
| BMI (kg/m2) | -0.0290 | 0.0380 | ±0.0760 | -0.763 | 0.4456 |  |
| Hypertension | +0.2947 | 0.6560 | ±1.3120 | +0.449 | 0.6532 |  |
| High cholesterol | -0.8691 | 0.5989 | ±1.1977 | -1.451 | 0.1467 |  |
| Kidney disease | -1.0903 | 1.1611 | ±2.3221 | -0.939 | 0.3477 |  |
| Circulatory disease | -0.4891 | 0.8255 | ±1.6511 | -0.592 | 0.5536 |  |
| Glucose SD, pooled (mg/dL) | -0.0819 | 0.1228 | ±0.2456 | -0.667 | 0.5046 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **443**, R² = **0.2739**, Adj R² = **0.2502**, F-statistic = **11.53** (p = **1.19e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.3**, BIC = **2887.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.1134** | 2.6831 | ±5.3661 | **+17.932** | **6.60e-72** | *** |
| Education: graduate level (vs college) | +0.8472 | 0.5889 | ±1.1777 | +1.439 | 0.1502 |  |
| Education: high school or below (vs college) | -0.9529 | 1.1063 | ±2.2126 | -0.861 | 0.3891 |  |
| **Site: UCSD (vs UAB)** | **+4.2229** | 0.7406 | ±1.4811 | **+5.702** | **1.18e-08** | *** |
| Site: UW (vs UAB) | -0.6846 | 0.7316 | ±1.4632 | -0.936 | 0.3494 |  |
| Season: spring (vs autumn) | -1.3247 | 0.7792 | ±1.5584 | -1.700 | 0.0891 | . |
| **Season: summer (vs autumn)** | **+3.1609** | 0.8476 | ±1.6952 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5537** | 0.8690 | ±1.7380 | **-5.240** | **1.60e-07** | *** |
| Age (years) | -0.0341 | 0.0257 | ±0.0514 | -1.328 | 0.1843 |  |
| BMI (kg/m2) | -0.0295 | 0.0380 | ±0.0761 | -0.774 | 0.4387 |  |
| Hypertension | +0.2731 | 0.6536 | ±1.3072 | +0.418 | 0.6761 |  |
| High cholesterol | -0.8526 | 0.5982 | ±1.1964 | -1.425 | 0.1541 |  |
| Kidney disease | -1.1379 | 1.1584 | ±2.3168 | -0.982 | 0.3259 |  |
| Circulatory disease | -0.5097 | 0.8259 | ±1.6518 | -0.617 | 0.5372 |  |
| Avg. daily SD (mg/dL) | -0.0281 | 0.1241 | ±0.2481 | -0.226 | 0.8210 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **443**, R² = **0.2751**, Adj R² = **0.2514**, F-statistic = **11.60** (p = **8.72e-23**), Residual SE = **5.775** on **428** df, AIC = **2825.6**, BIC = **2887.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.2931** | 2.6935 | ±5.3870 | **+18.301** | **8.16e-75** | *** |
| Education: graduate level (vs college) | +0.8266 | 0.5874 | ±1.1747 | +1.407 | 0.1593 |  |
| Education: high school or below (vs college) | -0.9274 | 1.1079 | ±2.2159 | -0.837 | 0.4026 |  |
| **Site: UCSD (vs UAB)** | **+4.1821** | 0.7418 | ±1.4836 | **+5.638** | **1.72e-08** | *** |
| Site: UW (vs UAB) | -0.7291 | 0.7360 | ±1.4720 | -0.991 | 0.3219 |  |
| Season: spring (vs autumn) | -1.2877 | 0.7789 | ±1.5579 | -1.653 | 0.0983 | . |
| **Season: summer (vs autumn)** | **+3.1747** | 0.8493 | ±1.6986 | **+3.738** | **1.85e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5087** | 0.8697 | ±1.7394 | **-5.184** | **2.17e-07** | *** |
| Age (years) | -0.0337 | 0.0258 | ±0.0515 | -1.308 | 0.1907 |  |
| BMI (kg/m2) | -0.0297 | 0.0380 | ±0.0760 | -0.782 | 0.4342 |  |
| Hypertension | +0.2844 | 0.6519 | ±1.3038 | +0.436 | 0.6627 |  |
| High cholesterol | -0.8660 | 0.5968 | ±1.1936 | -1.451 | 0.1467 |  |
| Kidney disease | -1.0938 | 1.1599 | ±2.3199 | -0.943 | 0.3457 |  |
| Circulatory disease | -0.4851 | 0.8254 | ±1.6508 | -0.588 | 0.5567 |  |
| CV (%) | -0.1104 | 0.1376 | ±0.2752 | -0.802 | 0.4225 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **443**, R² = **0.2754**, Adj R² = **0.2517**, F-statistic = **11.62** (p = **8.00e-23**), Residual SE = **5.774** on **428** df, AIC = **2825.4**, BIC = **2886.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.9282** | 2.8843 | ±5.7686 | **+15.924** | **4.35e-57** | *** |
| Education: graduate level (vs college) | +0.8179 | 0.5871 | ±1.1742 | +1.393 | 0.1636 |  |
| Education: high school or below (vs college) | -0.9195 | 1.1077 | ±2.2154 | -0.830 | 0.4065 |  |
| **Site: UCSD (vs UAB)** | **+4.1855** | 0.7420 | ±1.4840 | **+5.641** | **1.69e-08** | *** |
| Site: UW (vs UAB) | -0.7266 | 0.7356 | ±1.4713 | -0.988 | 0.3233 |  |
| Season: spring (vs autumn) | -1.2785 | 0.7784 | ±1.5569 | -1.642 | 0.1005 |  |
| **Season: summer (vs autumn)** | **+3.1750** | 0.8488 | ±1.6976 | **+3.741** | **1.84e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5040** | 0.8691 | ±1.7383 | **-5.182** | **2.19e-07** | *** |
| Age (years) | -0.0338 | 0.0257 | ±0.0515 | -1.315 | 0.1884 |  |
| BMI (kg/m2) | -0.0297 | 0.0380 | ±0.0760 | -0.783 | 0.4337 |  |
| Hypertension | +0.2875 | 0.6520 | ±1.3040 | +0.441 | 0.6592 |  |
| High cholesterol | -0.8708 | 0.5963 | ±1.1926 | -1.460 | 0.1442 |  |
| Kidney disease | -1.1065 | 1.1563 | ±2.3126 | -0.957 | 0.3386 |  |
| Circulatory disease | -0.4917 | 0.8257 | ±1.6514 | -0.595 | 0.5515 |  |
| Mean / SD ratio | +0.2518 | 0.2753 | ±0.5505 | +0.915 | 0.3603 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **443**, R² = **0.2739**, Adj R² = **0.2501**, F-statistic = **11.53** (p = **1.20e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.3**, BIC = **2887.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4391** | 2.7523 | ±5.5045 | **+17.236** | **1.41e-66** | *** |
| Education: graduate level (vs college) | +0.8492 | 0.5877 | ±1.1753 | +1.445 | 0.1485 |  |
| Education: high school or below (vs college) | -0.9485 | 1.1095 | ±2.2190 | -0.855 | 0.3926 |  |
| **Site: UCSD (vs UAB)** | **+4.2254** | 0.7390 | ±1.4780 | **+5.718** | **1.08e-08** | *** |
| Site: UW (vs UAB) | -0.6822 | 0.7315 | ±1.4629 | -0.933 | 0.3510 |  |
| Season: spring (vs autumn) | -1.3219 | 0.7759 | ±1.5519 | -1.704 | 0.0885 | . |
| **Season: summer (vs autumn)** | **+3.1635** | 0.8472 | ±1.6944 | **+3.734** | **1.89e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5525** | 0.8678 | ±1.7356 | **-5.246** | **1.55e-07** | *** |
| Age (years) | -0.0342 | 0.0257 | ±0.0515 | -1.328 | 0.1842 |  |
| BMI (kg/m2) | -0.0299 | 0.0380 | ±0.0760 | -0.785 | 0.4323 |  |
| Hypertension | +0.2685 | 0.6503 | ±1.3006 | +0.413 | 0.6797 |  |
| High cholesterol | -0.8483 | 0.5960 | ±1.1920 | -1.423 | 0.1546 |  |
| Kidney disease | -1.1525 | 1.1567 | ±2.3134 | -0.996 | 0.3191 |  |
| Circulatory disease | -0.5130 | 0.8275 | ±1.6551 | -0.620 | 0.5353 |  |
| Avg. daily mean/SD | +0.0322 | 0.2196 | ±0.4392 | +0.147 | 0.8833 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **443**, R² = **0.2741**, Adj R² = **0.2504**, F-statistic = **11.54** (p = **1.14e-22**), Residual SE = **5.779** on **428** df, AIC = **2826.2**, BIC = **2887.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+46.9820** | 2.8788 | ±5.7577 | **+16.320** | **7.13e-60** | *** |
| Education: graduate level (vs college) | +0.8521 | 0.5859 | ±1.1718 | +1.454 | 0.1458 |  |
| Education: high school or below (vs college) | -0.9830 | 1.1171 | ±2.2341 | -0.880 | 0.3789 |  |
| **Site: UCSD (vs UAB)** | **+4.2423** | 0.7403 | ±1.4805 | **+5.731** | **9.99e-09** | *** |
| Site: UW (vs UAB) | -0.6468 | 0.7344 | ±1.4687 | -0.881 | 0.3784 |  |
| Season: spring (vs autumn) | -1.3299 | 0.7782 | ±1.5565 | -1.709 | 0.0875 | . |
| **Season: summer (vs autumn)** | **+3.1697** | 0.8491 | ±1.6981 | **+3.733** | **1.89e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5638** | 0.8697 | ±1.7394 | **-5.248** | **1.54e-07** | *** |
| Age (years) | -0.0334 | 0.0259 | ±0.0518 | -1.289 | 0.1973 |  |
| BMI (kg/m2) | -0.0294 | 0.0381 | ±0.0762 | -0.770 | 0.4412 |  |
| Hypertension | +0.2721 | 0.6468 | ±1.2936 | +0.421 | 0.6740 |  |
| High cholesterol | -0.8509 | 0.5935 | ±1.1869 | -1.434 | 0.1516 |  |
| Kidney disease | -1.1864 | 1.1592 | ±2.3185 | -1.023 | 0.3061 |  |
| Circulatory disease | -0.4972 | 0.8276 | ±1.6553 | -0.601 | 0.5480 |  |
| MAG (mg/dL/h) | +0.0187 | 0.0490 | ±0.0980 | +0.382 | 0.7028 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **443**, R² = **0.2738**, Adj R² = **0.2501**, F-statistic = **11.53** (p = **1.22e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.3**, BIC = **2887.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.7670** | 2.9464 | ±5.8928 | **+16.212** | **4.16e-59** | *** |
| Education: graduate level (vs college) | +0.8562 | 0.5876 | ±1.1753 | +1.457 | 0.1451 |  |
| Education: high school or below (vs college) | -0.9509 | 1.1101 | ±2.2202 | -0.857 | 0.3917 |  |
| **Site: UCSD (vs UAB)** | **+4.2294** | 0.7394 | ±1.4787 | **+5.720** | **1.06e-08** | *** |
| Site: UW (vs UAB) | -0.6769 | 0.7288 | ±1.4576 | -0.929 | 0.3530 |  |
| Season: spring (vs autumn) | -1.3289 | 0.7795 | ±1.5589 | -1.705 | 0.0882 | . |
| **Season: summer (vs autumn)** | **+3.1607** | 0.8476 | ±1.6951 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5572** | 0.8706 | ±1.7412 | **-5.235** | **1.65e-07** | *** |
| Age (years) | -0.0344 | 0.0257 | ±0.0514 | -1.338 | 0.1809 |  |
| BMI (kg/m2) | -0.0302 | 0.0380 | ±0.0760 | -0.796 | 0.4260 |  |
| Hypertension | +0.2670 | 0.6471 | ±1.2943 | +0.413 | 0.6799 |  |
| High cholesterol | -0.8455 | 0.5938 | ±1.1875 | -1.424 | 0.1545 |  |
| Kidney disease | -1.1601 | 1.1568 | ±2.3135 | -1.003 | 0.3159 |  |
| Circulatory disease | -0.5109 | 0.8262 | ±1.6523 | -0.618 | 0.5363 |  |
| Avg. daily range (mg/dL) | -0.0007 | 0.0269 | ±0.0538 | -0.026 | 0.9791 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **443**, R² = **0.2739**, Adj R² = **0.2502**, F-statistic = **11.53** (p = **1.20e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.3**, BIC = **2887.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.8543** | 2.0879 | ±4.1758 | **+22.920** | **2.96e-116** | *** |
| Education: graduate level (vs college) | +0.8608 | 0.5875 | ±1.1751 | +1.465 | 0.1429 |  |
| Education: high school or below (vs college) | -0.9372 | 1.1131 | ±2.2263 | -0.842 | 0.3998 |  |
| **Site: UCSD (vs UAB)** | **+4.2221** | 0.7435 | ±1.4870 | **+5.679** | **1.36e-08** | *** |
| Site: UW (vs UAB) | -0.6752 | 0.7311 | ±1.4622 | -0.924 | 0.3557 |  |
| Season: spring (vs autumn) | -1.3200 | 0.7812 | ±1.5624 | -1.690 | 0.0911 | . |
| **Season: summer (vs autumn)** | **+3.1689** | 0.8476 | ±1.6952 | **+3.739** | **1.85e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5459** | 0.8770 | ±1.7539 | **-5.184** | **2.18e-07** | *** |
| Age (years) | -0.0345 | 0.0257 | ±0.0513 | -1.344 | 0.1790 |  |
| BMI (kg/m2) | -0.0301 | 0.0381 | ±0.0762 | -0.788 | 0.4305 |  |
| Hypertension | +0.2791 | 0.6471 | ±1.2942 | +0.431 | 0.6663 |  |
| High cholesterol | -0.8414 | 0.5910 | ±1.1820 | -1.424 | 0.1545 |  |
| Kidney disease | -1.1640 | 1.1531 | ±2.3062 | -1.009 | 0.3127 |  |
| Circulatory disease | -0.4952 | 0.8343 | ±1.6685 | -0.594 | 0.5528 |  |
| SD of daily means (mg/dL) | -0.0303 | 0.1603 | ±0.3206 | -0.189 | 0.8499 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **443**, R² = **0.2756**, Adj R² = **0.2519**, F-statistic = **11.63** (p = **7.64e-23**), Residual SE = **5.773** on **428** df, AIC = **2825.3**, BIC = **2886.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +140.1632 | 94.7383 | ±189.4766 | +1.479 | 0.1390 |  |
| Education: graduate level (vs college) | +0.8671 | 0.5856 | ±1.1712 | +1.481 | 0.1387 |  |
| Education: high school or below (vs college) | -0.9376 | 1.1094 | ±2.2189 | -0.845 | 0.3980 |  |
| **Site: UCSD (vs UAB)** | **+4.2774** | 0.7389 | ±1.4778 | **+5.789** | **7.09e-09** | *** |
| Site: UW (vs UAB) | -0.6385 | 0.7290 | ±1.4580 | -0.876 | 0.3811 |  |
| Season: spring (vs autumn) | -1.3364 | 0.7762 | ±1.5525 | -1.722 | 0.0851 | . |
| **Season: summer (vs autumn)** | **+3.1430** | 0.8479 | ±1.6958 | **+3.707** | **2.10e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5943** | 0.8717 | ±1.7434 | **-5.271** | **1.36e-07** | *** |
| Age (years) | -0.0337 | 0.0255 | ±0.0511 | -1.318 | 0.1875 |  |
| BMI (kg/m2) | -0.0284 | 0.0379 | ±0.0758 | -0.750 | 0.4532 |  |
| Hypertension | +0.2589 | 0.6450 | ±1.2899 | +0.401 | 0.6881 |  |
| High cholesterol | -0.8631 | 0.5923 | ±1.1847 | -1.457 | 0.1451 |  |
| Kidney disease | -1.2298 | 1.1551 | ±2.3103 | -1.065 | 0.2871 |  |
| Circulatory disease | -0.4989 | 0.8217 | ±1.6433 | -0.607 | 0.5438 |  |
| Time in range 70-180, pooled (%) | -0.9297 | 0.9516 | ±1.9031 | -0.977 | 0.3285 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **443**, R² = **0.2748**, Adj R² = **0.2511**, F-statistic = **11.58** (p = **9.36e-23**), Residual SE = **5.776** on **428** df, AIC = **2825.7**, BIC = **2887.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +114.8316 | 93.3497 | ±186.6995 | +1.230 | 0.2187 |  |
| Education: graduate level (vs college) | +0.8696 | 0.5866 | ±1.1732 | +1.482 | 0.1382 |  |
| Education: high school or below (vs college) | -0.9360 | 1.1133 | ±2.2266 | -0.841 | 0.4005 |  |
| **Site: UCSD (vs UAB)** | **+4.2464** | 0.7406 | ±1.4812 | **+5.734** | **9.82e-09** | *** |
| Site: UW (vs UAB) | -0.6689 | 0.7302 | ±1.4604 | -0.916 | 0.3596 |  |
| Season: spring (vs autumn) | -1.3240 | 0.7774 | ±1.5548 | -1.703 | 0.0886 | . |
| **Season: summer (vs autumn)** | **+3.1769** | 0.8479 | ±1.6957 | **+3.747** | **1.79e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5663** | 0.8704 | ±1.7409 | **-5.246** | **1.55e-07** | *** |
| Age (years) | -0.0337 | 0.0256 | ±0.0513 | -1.314 | 0.1889 |  |
| BMI (kg/m2) | -0.0298 | 0.0380 | ±0.0761 | -0.783 | 0.4337 |  |
| Hypertension | +0.2826 | 0.6462 | ±1.2924 | +0.437 | 0.6619 |  |
| High cholesterol | -0.8675 | 0.5920 | ±1.1840 | -1.465 | 0.1428 |  |
| Kidney disease | -1.1913 | 1.1578 | ±2.3157 | -1.029 | 0.3035 |  |
| Circulatory disease | -0.5160 | 0.8196 | ±1.6391 | -0.630 | 0.5290 |  |
| Avg. daily time in range 70-180 (%) | -0.6745 | 0.9375 | ±1.8751 | -0.719 | 0.4719 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.2744**, Adj R² = **0.2507**, F-statistic = **11.56** (p = **1.05e-22**), Residual SE = **5.778** on **428** df, AIC = **2826.0**, BIC = **2887.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6106** | 2.0192 | ±4.0385 | **+23.579** | **6.39e-123** | *** |
| Education: graduate level (vs college) | +0.8603 | 0.5860 | ±1.1721 | +1.468 | 0.1421 |  |
| Education: high school or below (vs college) | -0.9345 | 1.1090 | ±2.2180 | -0.843 | 0.3994 |  |
| **Site: UCSD (vs UAB)** | **+4.3078** | 0.7407 | ±1.4815 | **+5.816** | **6.04e-09** | *** |
| Site: UW (vs UAB) | -0.6319 | 0.7322 | ±1.4643 | -0.863 | 0.3881 |  |
| Season: spring (vs autumn) | -1.3820 | 0.7775 | ±1.5550 | -1.777 | 0.0755 | . |
| **Season: summer (vs autumn)** | **+3.1285** | 0.8480 | ±1.6960 | **+3.689** | **2.25e-04** | *** |
| **Season: winter (vs autumn)** | **-4.6041** | 0.8670 | ±1.7340 | **-5.310** | **1.09e-07** | *** |
| Age (years) | -0.0340 | 0.0256 | ±0.0512 | -1.328 | 0.1841 |  |
| BMI (kg/m2) | -0.0301 | 0.0380 | ±0.0760 | -0.792 | 0.4283 |  |
| Hypertension | +0.2401 | 0.6457 | ±1.2913 | +0.372 | 0.7099 |  |
| High cholesterol | -0.8451 | 0.5937 | ±1.1874 | -1.424 | 0.1546 |  |
| Kidney disease | -1.1111 | 1.1620 | ±2.3241 | -0.956 | 0.3390 |  |
| Circulatory disease | -0.5260 | 0.8225 | ±1.6450 | -0.640 | 0.5225 |  |
| Any reading < 54 during wear (0/1) | +0.4382 | 0.8105 | ±1.6210 | +0.541 | 0.5887 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.2772**, Adj R² = **0.2535**, F-statistic = **11.72** (p = **4.89e-23**), Residual SE = **5.767** on **428** df, AIC = **2824.3**, BIC = **2885.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4716** | 2.0082 | ±4.0165 | **+23.638** | **1.55e-123** | *** |
| Education: graduate level (vs college) | +0.8541 | 0.5891 | ±1.1781 | +1.450 | 0.1471 |  |
| Education: high school or below (vs college) | -0.8579 | 1.1062 | ±2.2123 | -0.776 | 0.4380 |  |
| **Site: UCSD (vs UAB)** | **+4.3706** | 0.7321 | ±1.4641 | **+5.970** | **2.37e-09** | *** |
| Site: UW (vs UAB) | -0.6055 | 0.7248 | ±1.4495 | -0.835 | 0.4035 |  |
| Season: spring (vs autumn) | -1.3177 | 0.7842 | ±1.5683 | -1.680 | 0.0929 | . |
| **Season: summer (vs autumn)** | **+3.1504** | 0.8544 | ±1.7088 | **+3.687** | **2.27e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5951** | 0.8705 | ±1.7410 | **-5.279** | **1.30e-07** | *** |
| Age (years) | -0.0314 | 0.0255 | ±0.0510 | -1.232 | 0.2180 |  |
| BMI (kg/m2) | -0.0343 | 0.0380 | ±0.0760 | -0.902 | 0.3670 |  |
| Hypertension | +0.1811 | 0.6369 | ±1.2738 | +0.284 | 0.7762 |  |
| High cholesterol | -0.8177 | 0.5904 | ±1.1807 | -1.385 | 0.1660 |  |
| Kidney disease | -1.0824 | 1.1634 | ±2.3268 | -0.930 | 0.3522 |  |
| Circulatory disease | -0.5580 | 0.8223 | ±1.6447 | -0.679 | 0.4974 |  |
| Time < 54 (%) | +7.4186 | 7.6314 | ±15.2628 | +0.972 | 0.3310 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.2740**, Adj R² = **0.2503**, F-statistic = **11.54** (p = **1.15e-22**), Residual SE = **5.779** on **428** df, AIC = **2826.2**, BIC = **2887.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6734** | 2.0084 | ±4.0168 | **+23.737** | **1.49e-124** | *** |
| Education: graduate level (vs college) | +0.8545 | 0.5884 | ±1.1769 | +1.452 | 0.1465 |  |
| Education: high school or below (vs college) | -0.9412 | 1.1093 | ±2.2186 | -0.848 | 0.3962 |  |
| **Site: UCSD (vs UAB)** | **+4.2456** | 0.7404 | ±1.4808 | **+5.734** | **9.80e-09** | *** |
| Site: UW (vs UAB) | -0.6729 | 0.7328 | ±1.4656 | -0.918 | 0.3585 |  |
| Season: spring (vs autumn) | -1.3220 | 0.7818 | ±1.5635 | -1.691 | 0.0908 | . |
| **Season: summer (vs autumn)** | **+3.1781** | 0.8504 | ±1.7008 | **+3.737** | **1.86e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5556** | 0.8703 | ±1.7407 | **-5.234** | **1.66e-07** | *** |
| Age (years) | -0.0341 | 0.0257 | ±0.0514 | -1.326 | 0.1850 |  |
| BMI (kg/m2) | -0.0306 | 0.0381 | ±0.0763 | -0.801 | 0.4230 |  |
| Hypertension | +0.2595 | 0.6497 | ±1.2995 | +0.399 | 0.6896 |  |
| High cholesterol | -0.8454 | 0.5935 | ±1.1870 | -1.424 | 0.1543 |  |
| Kidney disease | -1.1512 | 1.1579 | ±2.3157 | -0.994 | 0.3201 |  |
| Circulatory disease | -0.5287 | 0.8252 | ±1.6503 | -0.641 | 0.5217 |  |
| Avg. daily time < 54 (%) | +2.4000 | 8.4128 | ±16.8256 | +0.285 | 0.7754 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.2750**, Adj R² = **0.2512**, F-statistic = **11.59** (p = **9.00e-23**), Residual SE = **5.776** on **428** df, AIC = **2825.7**, BIC = **2887.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.5208** | 2.0162 | ±4.0324 | **+23.569** | **7.98e-123** | *** |
| Education: graduate level (vs college) | +0.8689 | 0.5849 | ±1.1698 | +1.486 | 0.1374 |  |
| Education: high school or below (vs college) | -0.9995 | 1.1212 | ±2.2424 | -0.891 | 0.3727 |  |
| **Site: UCSD (vs UAB)** | **+4.2680** | 0.7400 | ±1.4801 | **+5.767** | **8.06e-09** | *** |
| Site: UW (vs UAB) | -0.6310 | 0.7359 | ±1.4719 | -0.857 | 0.3912 |  |
| Season: spring (vs autumn) | -1.3433 | 0.7760 | ±1.5521 | -1.731 | 0.0835 | . |
| **Season: summer (vs autumn)** | **+3.1494** | 0.8464 | ±1.6928 | **+3.721** | **1.98e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5907** | 0.8663 | ±1.7326 | **-5.299** | **1.16e-07** | *** |
| Age (years) | -0.0343 | 0.0257 | ±0.0514 | -1.337 | 0.1813 |  |
| BMI (kg/m2) | -0.0301 | 0.0379 | ±0.0758 | -0.793 | 0.4275 |  |
| Hypertension | +0.2967 | 0.6535 | ±1.3071 | +0.454 | 0.6498 |  |
| High cholesterol | -0.8851 | 0.5959 | ±1.1917 | -1.485 | 0.1375 |  |
| Kidney disease | -1.0907 | 1.1630 | ±2.3259 | -0.938 | 0.3483 |  |
| Circulatory disease | -0.5011 | 0.8239 | ±1.6478 | -0.608 | 0.5430 |  |
| Time 54-69, pooled (%) | +1.2428 | 1.6368 | ±3.2736 | +0.759 | 0.4477 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **443**, R² = **0.2739**, Adj R² = **0.2501**, F-statistic = **11.53** (p = **1.20e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.3**, BIC = **2887.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6739** | 2.0084 | ±4.0167 | **+23.738** | **1.47e-124** | *** |
| Education: graduate level (vs college) | +0.8613 | 0.5879 | ±1.1758 | +1.465 | 0.1429 |  |
| Education: high school or below (vs college) | -0.9621 | 1.1166 | ±2.2331 | -0.862 | 0.3889 |  |
| **Site: UCSD (vs UAB)** | **+4.2343** | 0.7408 | ±1.4816 | **+5.716** | **1.09e-08** | *** |
| Site: UW (vs UAB) | -0.6703 | 0.7325 | ±1.4650 | -0.915 | 0.3601 |  |
| Season: spring (vs autumn) | -1.3266 | 0.7808 | ±1.5615 | -1.699 | 0.0893 | . |
| **Season: summer (vs autumn)** | **+3.1654** | 0.8474 | ±1.6948 | **+3.735** | **1.87e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5621** | 0.8681 | ±1.7362 | **-5.255** | **1.48e-07** | *** |
| Age (years) | -0.0344 | 0.0257 | ±0.0514 | -1.338 | 0.1808 |  |
| BMI (kg/m2) | -0.0302 | 0.0380 | ±0.0759 | -0.794 | 0.4269 |  |
| Hypertension | +0.2798 | 0.6546 | ±1.3091 | +0.427 | 0.6690 |  |
| High cholesterol | -0.8530 | 0.5933 | ±1.1866 | -1.438 | 0.1505 |  |
| Kidney disease | -1.1515 | 1.1586 | ±2.3172 | -0.994 | 0.3203 |  |
| Circulatory disease | -0.5124 | 0.8248 | ±1.6495 | -0.621 | 0.5344 |  |
| Avg. daily time 54-69 (%) | +0.2665 | 1.6684 | ±3.3369 | +0.160 | 0.8731 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **443**, R² = **0.2758**, Adj R² = **0.2521**, F-statistic = **11.64** (p = **7.07e-23**), Residual SE = **5.772** on **428** df, AIC = **2825.1**, BIC = **2886.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4374** | 2.0171 | ±4.0342 | **+23.518** | **2.67e-122** | *** |
| Education: graduate level (vs college) | +0.8707 | 0.5847 | ±1.1694 | +1.489 | 0.1364 |  |
| Education: high school or below (vs college) | -0.9901 | 1.1190 | ±2.2380 | -0.885 | 0.3763 |  |
| **Site: UCSD (vs UAB)** | **+4.3031** | 0.7383 | ±1.4767 | **+5.828** | **5.60e-09** | *** |
| Site: UW (vs UAB) | -0.6085 | 0.7337 | ±1.4675 | -0.829 | 0.4069 |  |
| Season: spring (vs autumn) | -1.3435 | 0.7768 | ±1.5536 | -1.730 | 0.0837 | . |
| **Season: summer (vs autumn)** | **+3.1452** | 0.8476 | ±1.6952 | **+3.711** | **2.07e-04** | *** |
| **Season: winter (vs autumn)** | **-4.6043** | 0.8658 | ±1.7317 | **-5.318** | **1.05e-07** | *** |
| Age (years) | -0.0337 | 0.0256 | ±0.0513 | -1.316 | 0.1880 |  |
| BMI (kg/m2) | -0.0309 | 0.0379 | ±0.0758 | -0.814 | 0.4155 |  |
| Hypertension | +0.2851 | 0.6495 | ±1.2989 | +0.439 | 0.6607 |  |
| High cholesterol | -0.8871 | 0.5964 | ±1.1928 | -1.487 | 0.1369 |  |
| Kidney disease | -1.0612 | 1.1657 | ±2.3313 | -0.910 | 0.3626 |  |
| Circulatory disease | -0.5086 | 0.8224 | ±1.6448 | -0.618 | 0.5363 |  |
| Time < 70 (%) | +1.4805 | 1.5393 | ±3.0786 | +0.962 | 0.3361 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **443**, R² = **0.2739**, Adj R² = **0.2502**, F-statistic = **11.53** (p = **1.19e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.3**, BIC = **2887.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6619** | 2.0089 | ±4.0177 | **+23.726** | **1.95e-124** | *** |
| Education: graduate level (vs college) | +0.8620 | 0.5873 | ±1.1745 | +1.468 | 0.1422 |  |
| Education: high school or below (vs college) | -0.9631 | 1.1156 | ±2.2311 | -0.863 | 0.3879 |  |
| **Site: UCSD (vs UAB)** | **+4.2372** | 0.7411 | ±1.4822 | **+5.718** | **1.08e-08** | *** |
| Site: UW (vs UAB) | -0.6688 | 0.7327 | ±1.4654 | -0.913 | 0.3613 |  |
| Season: spring (vs autumn) | -1.3249 | 0.7812 | ±1.5624 | -1.696 | 0.0899 | . |
| **Season: summer (vs autumn)** | **+3.1688** | 0.8483 | ±1.6966 | **+3.736** | **1.87e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5626** | 0.8685 | ±1.7371 | **-5.253** | **1.50e-07** | *** |
| Age (years) | -0.0344 | 0.0257 | ±0.0514 | -1.338 | 0.1809 |  |
| BMI (kg/m2) | -0.0302 | 0.0380 | ±0.0760 | -0.795 | 0.4265 |  |
| Hypertension | +0.2813 | 0.6523 | ±1.3046 | +0.431 | 0.6662 |  |
| High cholesterol | -0.8546 | 0.5933 | ±1.1865 | -1.440 | 0.1497 |  |
| Kidney disease | -1.1479 | 1.1591 | ±2.3182 | -0.990 | 0.3220 |  |
| Circulatory disease | -0.5151 | 0.8243 | ±1.6486 | -0.625 | 0.5320 |  |
| Avg. daily time < 70 (%) | +0.3222 | 1.5282 | ±3.0565 | +0.211 | 0.8330 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.2777**, Adj R² = **0.2541**, F-statistic = **11.75** (p = **4.21e-23**), Residual SE = **5.765** on **428** df, AIC = **2824.0**, BIC = **2885.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +828.1423 | 724.7309 | ±1449.4618 | +1.143 | 0.2532 |  |
| Education: graduate level (vs college) | +0.8531 | 0.5888 | ±1.1775 | +1.449 | 0.1473 |  |
| Education: high school or below (vs college) | -0.8501 | 1.1065 | ±2.2130 | -0.768 | 0.4423 |  |
| **Site: UCSD (vs UAB)** | **+4.3892** | 0.7333 | ±1.4666 | **+5.986** | **2.15e-09** | *** |
| Site: UW (vs UAB) | -0.5931 | 0.7244 | ±1.4487 | -0.819 | 0.4129 |  |
| Season: spring (vs autumn) | -1.3248 | 0.7844 | ±1.5688 | -1.689 | 0.0912 | . |
| **Season: summer (vs autumn)** | **+3.1511** | 0.8546 | ±1.7093 | **+3.687** | **2.27e-04** | *** |
| **Season: winter (vs autumn)** | **-4.6035** | 0.8705 | ±1.7410 | **-5.288** | **1.24e-07** | *** |
| Age (years) | -0.0308 | 0.0255 | ±0.0510 | -1.207 | 0.2276 |  |
| BMI (kg/m2) | -0.0340 | 0.0380 | ±0.0759 | -0.896 | 0.3701 |  |
| Hypertension | +0.1803 | 0.6369 | ±1.2738 | +0.283 | 0.7771 |  |
| High cholesterol | -0.8185 | 0.5902 | ±1.1804 | -1.387 | 0.1655 |  |
| Kidney disease | -1.0789 | 1.1636 | ±2.3272 | -0.927 | 0.3538 |  |
| Circulatory disease | -0.5619 | 0.8221 | ±1.6442 | -0.684 | 0.4943 |  |
| Time 54-250, pooled (%) | -7.8073 | 7.2479 | ±14.4957 | -1.077 | 0.2814 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.2743**, Adj R² = **0.2506**, F-statistic = **11.56** (p = **1.06e-22**), Residual SE = **5.778** on **428** df, AIC = **2826.0**, BIC = **2887.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +419.7506 | 838.8309 | ±1677.6619 | +0.500 | 0.6168 |  |
| Education: graduate level (vs college) | +0.8529 | 0.5885 | ±1.1769 | +1.449 | 0.1472 |  |
| Education: high school or below (vs college) | -0.9342 | 1.1097 | ±2.2193 | -0.842 | 0.3999 |  |
| **Site: UCSD (vs UAB)** | **+4.2598** | 0.7414 | ±1.4829 | **+5.745** | **9.17e-09** | *** |
| Site: UW (vs UAB) | -0.6668 | 0.7329 | ±1.4657 | -0.910 | 0.3629 |  |
| Season: spring (vs autumn) | -1.3217 | 0.7824 | ±1.5648 | -1.689 | 0.0912 | . |
| **Season: summer (vs autumn)** | **+3.1884** | 0.8508 | ±1.7017 | **+3.747** | **1.79e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5577** | 0.8712 | ±1.7424 | **-5.231** | **1.68e-07** | *** |
| Age (years) | -0.0337 | 0.0257 | ±0.0515 | -1.309 | 0.1907 |  |
| BMI (kg/m2) | -0.0305 | 0.0381 | ±0.0762 | -0.801 | 0.4230 |  |
| Hypertension | +0.2571 | 0.6491 | ±1.2981 | +0.396 | 0.6920 |  |
| High cholesterol | -0.8466 | 0.5936 | ±1.1872 | -1.426 | 0.1538 |  |
| Kidney disease | -1.1456 | 1.1588 | ±2.3176 | -0.989 | 0.3228 |  |
| Circulatory disease | -0.5393 | 0.8243 | ±1.6486 | -0.654 | 0.5129 |  |
| Avg. daily time 54-250 (%) | -3.7212 | 8.3886 | ±16.7773 | -0.444 | 0.6573 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **443**, R² = **0.2740**, Adj R² = **0.2502**, F-statistic = **11.54** (p = **1.18e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.3**, BIC = **2887.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6123** | 2.0474 | ±4.0949 | **+23.254** | **1.28e-119** | *** |
| Education: graduate level (vs college) | +0.8572 | 0.5868 | ±1.1736 | +1.461 | 0.1441 |  |
| Education: high school or below (vs college) | -0.9405 | 1.1090 | ±2.2181 | -0.848 | 0.3964 |  |
| **Site: UCSD (vs UAB)** | **+4.2304** | 0.7399 | ±1.4798 | **+5.718** | **1.08e-08** | *** |
| Site: UW (vs UAB) | -0.6774 | 0.7309 | ±1.4619 | -0.927 | 0.3541 |  |
| Season: spring (vs autumn) | -1.3289 | 0.7790 | ±1.5581 | -1.706 | 0.0880 | . |
| **Season: summer (vs autumn)** | **+3.1583** | 0.8469 | ±1.6939 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5600** | 0.8697 | ±1.7394 | **-5.243** | **1.58e-07** | *** |
| Age (years) | -0.0343 | 0.0257 | ±0.0513 | -1.337 | 0.1813 |  |
| BMI (kg/m2) | -0.0296 | 0.0381 | ±0.0761 | -0.777 | 0.4372 |  |
| Hypertension | +0.2618 | 0.6507 | ±1.3013 | +0.402 | 0.6874 |  |
| High cholesterol | -0.8429 | 0.5935 | ±1.1870 | -1.420 | 0.1555 |  |
| Kidney disease | -1.1987 | 1.1622 | ±2.3243 | -1.031 | 0.3023 |  |
| Circulatory disease | -0.5078 | 0.8267 | ±1.6534 | -0.614 | 0.5390 |  |
| Time 181-250, pooled (%) | +0.2617 | 1.0236 | ±2.0472 | +0.256 | 0.7982 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **443**, R² = **0.2745**, Adj R² = **0.2508**, F-statistic = **11.57** (p = **1.01e-22**), Residual SE = **5.777** on **428** df, AIC = **2825.9**, BIC = **2887.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4984** | 2.0467 | ±4.0934 | **+23.207** | **3.84e-119** | *** |
| Education: graduate level (vs college) | +0.8586 | 0.5867 | ±1.1734 | +1.463 | 0.1434 |  |
| Education: high school or below (vs college) | -0.9137 | 1.1136 | ±2.2272 | -0.820 | 0.4120 |  |
| **Site: UCSD (vs UAB)** | **+4.2311** | 0.7399 | ±1.4798 | **+5.719** | **1.07e-08** | *** |
| Site: UW (vs UAB) | -0.6836 | 0.7310 | ±1.4619 | -0.935 | 0.3497 |  |
| Season: spring (vs autumn) | -1.3332 | 0.7779 | ±1.5559 | -1.714 | 0.0866 | . |
| **Season: summer (vs autumn)** | **+3.1597** | 0.8479 | ±1.6958 | **+3.727** | **1.94e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5566** | 0.8689 | ±1.7378 | **-5.244** | **1.57e-07** | *** |
| Age (years) | -0.0337 | 0.0257 | ±0.0514 | -1.313 | 0.1890 |  |
| BMI (kg/m2) | -0.0297 | 0.0381 | ±0.0763 | -0.779 | 0.4358 |  |
| Hypertension | +0.2541 | 0.6501 | ±1.3002 | +0.391 | 0.6959 |  |
| High cholesterol | -0.8479 | 0.5925 | ±1.1850 | -1.431 | 0.1524 |  |
| Kidney disease | -1.2169 | 1.1571 | ±2.3141 | -1.052 | 0.2929 |  |
| Circulatory disease | -0.5072 | 0.8235 | ±1.6470 | -0.616 | 0.5380 |  |
| Avg. daily time 181-250 (%) | +0.6336 | 1.0514 | ±2.1028 | +0.603 | 0.5468 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **443**, R² = **0.2740**, Adj R² = **0.2502**, F-statistic = **11.54** (p = **1.17e-22**), Residual SE = **5.780** on **428** df, AIC = **2826.2**, BIC = **2887.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.6007** | 2.0486 | ±4.0971 | **+23.236** | **1.96e-119** | *** |
| Education: graduate level (vs college) | +0.8572 | 0.5868 | ±1.1735 | +1.461 | 0.1440 |  |
| Education: high school or below (vs college) | -0.9394 | 1.1090 | ±2.2181 | -0.847 | 0.3970 |  |
| **Site: UCSD (vs UAB)** | **+4.2309** | 0.7399 | ±1.4798 | **+5.718** | **1.08e-08** | *** |
| Site: UW (vs UAB) | -0.6772 | 0.7308 | ±1.4616 | -0.927 | 0.3541 |  |
| Season: spring (vs autumn) | -1.3291 | 0.7789 | ±1.5578 | -1.706 | 0.0879 | . |
| **Season: summer (vs autumn)** | **+3.1581** | 0.8469 | ±1.6939 | **+3.729** | **1.92e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5604** | 0.8699 | ±1.7397 | **-5.243** | **1.58e-07** | *** |
| Age (years) | -0.0343 | 0.0257 | ±0.0513 | -1.336 | 0.1816 |  |
| BMI (kg/m2) | -0.0295 | 0.0381 | ±0.0761 | -0.775 | 0.4385 |  |
| Hypertension | +0.2614 | 0.6505 | ±1.3011 | +0.402 | 0.6878 |  |
| High cholesterol | -0.8428 | 0.5934 | ±1.1869 | -1.420 | 0.1556 |  |
| Kidney disease | -1.2024 | 1.1620 | ±2.3240 | -1.035 | 0.3008 |  |
| Circulatory disease | -0.5076 | 0.8265 | ±1.6531 | -0.614 | 0.5391 |  |
| Time > 180 (%) | +0.2880 | 1.0208 | ±2.0416 | +0.282 | 0.7779 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **443**, R² = **0.2746**, Adj R² = **0.2509**, F-statistic = **11.57** (p = **9.88e-23**), Residual SE = **5.777** on **428** df, AIC = **2825.9**, BIC = **2887.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+47.4850** | 2.0480 | ±4.0960 | **+23.186** | **6.27e-119** | *** |
| Education: graduate level (vs college) | +0.8586 | 0.5867 | ±1.1734 | +1.463 | 0.1433 |  |
| Education: high school or below (vs college) | -0.9118 | 1.1137 | ±2.2275 | -0.819 | 0.4130 |  |
| **Site: UCSD (vs UAB)** | **+4.2322** | 0.7399 | ±1.4798 | **+5.720** | **1.07e-08** | *** |
| Site: UW (vs UAB) | -0.6831 | 0.7307 | ±1.4615 | -0.935 | 0.3499 |  |
| Season: spring (vs autumn) | -1.3340 | 0.7779 | ±1.5558 | -1.715 | 0.0864 | . |
| **Season: summer (vs autumn)** | **+3.1598** | 0.8479 | ±1.6959 | **+3.726** | **1.94e-04** | *** |
| **Season: winter (vs autumn)** | **-4.5572** | 0.8690 | ±1.7380 | **-5.244** | **1.57e-07** | *** |
| Age (years) | -0.0337 | 0.0257 | ±0.0514 | -1.310 | 0.1900 |  |
| BMI (kg/m2) | -0.0297 | 0.0382 | ±0.0763 | -0.777 | 0.4369 |  |
| Hypertension | +0.2538 | 0.6500 | ±1.2999 | +0.391 | 0.6961 |  |
| High cholesterol | -0.8482 | 0.5924 | ±1.1849 | -1.432 | 0.1522 |  |
| Kidney disease | -1.2193 | 1.1570 | ±2.3139 | -1.054 | 0.2919 |  |
| Circulatory disease | -0.5071 | 0.8233 | ±1.6466 | -0.616 | 0.5379 |  |
| Avg. daily time > 180 (%) | +0.6597 | 1.0472 | ±2.0945 | +0.630 | 0.5288 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 443)
**Regression Call / Formula**: `env_hum_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **443**, R² = **0.2770**, Adj R² = **0.2534**, F-statistic = **11.72** (p = **5.07e-23**), Residual SE = **5.767** on **428** df, AIC = **2824.4**, BIC = **2885.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+48.0196** | 2.0339 | ±4.0678 | **+23.610** | **3.06e-123** | *** |
| Education: graduate level (vs college) | +0.8149 | 0.5909 | ±1.1818 | +1.379 | 0.1679 |  |
| Education: high school or below (vs college) | -0.9778 | 1.0988 | ±2.1976 | -0.890 | 0.3736 |  |
| **Site: UCSD (vs UAB)** | **+4.2326** | 0.7345 | ±1.4690 | **+5.762** | **8.29e-09** | *** |
| Site: UW (vs UAB) | -0.6461 | 0.7295 | ±1.4590 | -0.886 | 0.3758 |  |
| Season: spring (vs autumn) | -1.3079 | 0.7781 | ±1.5562 | -1.681 | 0.0928 | . |
| **Season: summer (vs autumn)** | **+3.1392** | 0.8394 | ±1.6787 | **+3.740** | **1.84e-04** | *** |
| **Season: winter (vs autumn)** | **-4.4594** | 0.8690 | ±1.7381 | **-5.131** | **2.88e-07** | *** |
| Age (years) | -0.0402 | 0.0261 | ±0.0521 | -1.542 | 0.1231 |  |
| BMI (kg/m2) | -0.0266 | 0.0370 | ±0.0740 | -0.720 | 0.4717 |  |
| Hypertension | +0.3489 | 0.6528 | ±1.3057 | +0.534 | 0.5931 |  |
| High cholesterol | -0.8231 | 0.5916 | ±1.1832 | -1.391 | 0.1641 |  |
| Kidney disease | -1.1521 | 1.1445 | ±2.2890 | -1.007 | 0.3141 |  |
| Circulatory disease | -0.5578 | 0.8281 | ±1.6561 | -0.674 | 0.5006 |  |
| Nocturnal time > 180 (%) | -1.0888 | 0.8389 | ±1.6779 | -1.298 | 0.1943 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Indoor VOC index, mean  (domain: Home environment; outcome sample N = 443; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season)`  
**Model Diagnostics**: N = **443**, R² = **0.0420**, Adj R² = **0.0130**, F-statistic = **1.45** (p = **0.1348**), Residual SE = **14.204** on **429** df, AIC = **3622.0**, BIC = **3679.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2064** | 5.6584 | ±11.3169 | **+22.304** | **3.37e-110** | *** |
| Education: graduate level (vs college) | -1.3171 | 1.4240 | ±2.8480 | -0.925 | 0.3550 |  |
| Education: high school or below (vs college) | +3.5906 | 2.6867 | ±5.3734 | +1.336 | 0.1814 |  |
| Site: UCSD (vs UAB) | +0.9079 | 1.8453 | ±3.6907 | +0.492 | 0.6227 |  |
| Site: UW (vs UAB) | +1.4580 | 1.8087 | ±3.6175 | +0.806 | 0.4202 |  |
| Season: spring (vs autumn) | +1.7470 | 1.9469 | ±3.8938 | +0.897 | 0.3696 |  |
| Season: summer (vs autumn) | +1.8866 | 2.0072 | ±4.0144 | +0.940 | 0.3473 |  |
| Season: winter (vs autumn) | +3.4614 | 2.0035 | ±4.0069 | +1.728 | 0.0840 | . |
| Age (years) | -0.1098 | 0.0708 | ±0.1415 | -1.552 | 0.1207 |  |
| BMI (kg/m2) | +0.1534 | 0.0992 | ±0.1983 | +1.547 | 0.1218 |  |
| Hypertension | +2.1145 | 1.5790 | ±3.1581 | +1.339 | 0.1805 |  |
| High cholesterol | -0.0361 | 1.4994 | ±2.9989 | -0.024 | 0.9808 |  |
| Kidney disease | -0.9878 | 2.5855 | ±5.1710 | -0.382 | 0.7024 |  |
| Circulatory disease | -1.0644 | 2.1839 | ±4.3678 | -0.487 | 0.6260 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + hba1c`  
**Model Diagnostics**: N = **443**, R² = **0.0445**, Adj R² = **0.0133**, F-statistic = **1.42** (p = **0.1380**), Residual SE = **14.202** on **428** df, AIC = **3622.8**, BIC = **3684.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+139.0996** | 14.0380 | ±28.0761 | **+9.909** | **3.81e-23** | *** |
| Education: graduate level (vs college) | -1.3770 | 1.4361 | ±2.8722 | -0.959 | 0.3376 |  |
| Education: high school or below (vs college) | +3.7690 | 2.6912 | ±5.3824 | +1.400 | 0.1614 |  |
| Site: UCSD (vs UAB) | +0.9369 | 1.8498 | ±3.6997 | +0.506 | 0.6125 |  |
| Site: UW (vs UAB) | +1.4259 | 1.8197 | ±3.6394 | +0.784 | 0.4333 |  |
| Season: spring (vs autumn) | +1.4262 | 1.9865 | ±3.9730 | +0.718 | 0.4728 |  |
| Season: summer (vs autumn) | +2.0076 | 2.0130 | ±4.0260 | +0.997 | 0.3186 |  |
| Season: winter (vs autumn) | +3.3438 | 2.0295 | ±4.0590 | +1.648 | 0.0994 | . |
| Age (years) | -0.1027 | 0.0718 | ±0.1436 | -1.430 | 0.1527 |  |
| BMI (kg/m2) | +0.1662 | 0.0988 | ±0.1976 | +1.682 | 0.0925 | . |
| Hypertension | +2.2567 | 1.5701 | ±3.1402 | +1.437 | 0.1506 |  |
| High cholesterol | +0.2882 | 1.5691 | ±3.1382 | +0.184 | 0.8543 |  |
| Kidney disease | -1.1438 | 2.6019 | ±5.2039 | -0.440 | 0.6602 |  |
| Circulatory disease | -1.1962 | 2.2248 | ±4.4497 | -0.538 | 0.5908 |  |
| HbA1c (%) | -2.4761 | 2.5141 | ±5.0281 | -0.985 | 0.3247 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_glucose`  
**Model Diagnostics**: N = **443**, R² = **0.0499**, Adj R² = **0.0188**, F-statistic = **1.60** (p = **0.0748**), Residual SE = **14.163** on **428** df, AIC = **3620.4**, BIC = **3681.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+145.5802** | 12.2054 | ±24.4108 | **+11.928** | **8.51e-33** | *** |
| Education: graduate level (vs college) | -1.2790 | 1.4166 | ±2.8333 | -0.903 | 0.3666 |  |
| Education: high school or below (vs college) | +3.4227 | 2.6707 | ±5.3415 | +1.282 | 0.2000 |  |
| Site: UCSD (vs UAB) | +1.0640 | 1.8454 | ±3.6908 | +0.577 | 0.5642 |  |
| Site: UW (vs UAB) | +1.6437 | 1.8262 | ±3.6523 | +0.900 | 0.3681 |  |
| Season: spring (vs autumn) | +1.5827 | 1.9390 | ±3.8781 | +0.816 | 0.4144 |  |
| Season: summer (vs autumn) | +1.8642 | 2.0255 | ±4.0511 | +0.920 | 0.3574 |  |
| Season: winter (vs autumn) | +3.3390 | 2.0275 | ±4.0549 | +1.647 | 0.0996 | . |
| Age (years) | -0.1134 | 0.0708 | ±0.1417 | -1.601 | 0.1094 |  |
| BMI (kg/m2) | +0.1648 | 0.0988 | ±0.1976 | +1.668 | 0.0953 | . |
| Hypertension | +2.2820 | 1.5674 | ±3.1349 | +1.456 | 0.1454 |  |
| High cholesterol | -0.1409 | 1.5009 | ±3.0019 | -0.094 | 0.9252 |  |
| Kidney disease | -0.8096 | 2.6031 | ±5.2063 | -0.311 | 0.7558 |  |
| Circulatory disease | -1.0422 | 2.2058 | ±4.4116 | -0.472 | 0.6366 |  |
| Mean glucose (mg/dL) | -0.1711 | 0.0935 | ±0.1871 | -1.829 | 0.0675 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + gmi`  
**Model Diagnostics**: N = **443**, R² = **0.0499**, Adj R² = **0.0188**, F-statistic = **1.60** (p = **0.0748**), Residual SE = **14.163** on **428** df, AIC = **3620.4**, BIC = **3681.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+169.2510** | 24.4358 | ±48.8716 | **+6.926** | **4.32e-12** | *** |
| Education: graduate level (vs college) | -1.2790 | 1.4166 | ±2.8333 | -0.903 | 0.3666 |  |
| Education: high school or below (vs college) | +3.4227 | 2.6707 | ±5.3415 | +1.282 | 0.2000 |  |
| Site: UCSD (vs UAB) | +1.0640 | 1.8454 | ±3.6908 | +0.577 | 0.5642 |  |
| Site: UW (vs UAB) | +1.6437 | 1.8262 | ±3.6523 | +0.900 | 0.3681 |  |
| Season: spring (vs autumn) | +1.5827 | 1.9390 | ±3.8781 | +0.816 | 0.4144 |  |
| Season: summer (vs autumn) | +1.8642 | 2.0255 | ±4.0511 | +0.920 | 0.3574 |  |
| Season: winter (vs autumn) | +3.3390 | 2.0275 | ±4.0549 | +1.647 | 0.0996 | . |
| Age (years) | -0.1134 | 0.0708 | ±0.1417 | -1.601 | 0.1094 |  |
| BMI (kg/m2) | +0.1648 | 0.0988 | ±0.1976 | +1.668 | 0.0953 | . |
| Hypertension | +2.2820 | 1.5674 | ±3.1349 | +1.456 | 0.1454 |  |
| High cholesterol | -0.1409 | 1.5009 | ±3.0019 | -0.094 | 0.9252 |  |
| Kidney disease | -0.8096 | 2.6031 | ±5.2063 | -0.311 | 0.7558 |  |
| Circulatory disease | -1.0422 | 2.2058 | ±4.4116 | -0.472 | 0.6366 |  |
| GMI (%) | -7.1513 | 3.9109 | ±7.8217 | -1.829 | 0.0675 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_mean`  
**Model Diagnostics**: N = **443**, R² = **0.0461**, Adj R² = **0.0149**, F-statistic = **1.48** (p = **0.1160**), Residual SE = **14.191** on **428** df, AIC = **3622.1**, BIC = **3683.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+137.4767** | 10.1588 | ±20.3175 | **+13.533** | **1.00e-41** | *** |
| Education: graduate level (vs college) | -1.3769 | 1.4294 | ±2.8588 | -0.963 | 0.3354 |  |
| Education: high school or below (vs college) | +3.4352 | 2.6886 | ±5.3772 | +1.278 | 0.2014 |  |
| Site: UCSD (vs UAB) | +1.1378 | 1.8644 | ±3.7289 | +0.610 | 0.5417 |  |
| Site: UW (vs UAB) | +1.6626 | 1.8380 | ±3.6759 | +0.905 | 0.3657 |  |
| Season: spring (vs autumn) | +1.6652 | 1.9462 | ±3.8923 | +0.856 | 0.3922 |  |
| Season: summer (vs autumn) | +1.8887 | 2.0228 | ±4.0456 | +0.934 | 0.3505 |  |
| Season: winter (vs autumn) | +3.4191 | 2.0173 | ±4.0345 | +1.695 | 0.0901 | . |
| Age (years) | -0.1220 | 0.0722 | ±0.1443 | -1.690 | 0.0910 | . |
| BMI (kg/m2) | +0.1741 | 0.0970 | ±0.1939 | +1.795 | 0.0726 | . |
| Hypertension | +2.2364 | 1.5762 | ±3.1523 | +1.419 | 0.1559 |  |
| High cholesterol | -0.0582 | 1.5024 | ±3.0049 | -0.039 | 0.9691 |  |
| Kidney disease | -1.0698 | 2.5753 | ±5.1506 | -0.415 | 0.6778 |  |
| Circulatory disease | -1.0978 | 2.1937 | ±4.3873 | -0.500 | 0.6168 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0978 | 0.0707 | ±0.1414 | -1.383 | 0.1666 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_sd`  
**Model Diagnostics**: N = **443**, R² = **0.0420**, Adj R² = **0.0107**, F-statistic = **1.34** (p = **0.1802**), Residual SE = **14.221** on **428** df, AIC = **3624.0**, BIC = **3685.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.3365** | 7.2632 | ±14.5265 | **+17.394** | **9.16e-68** | *** |
| Education: graduate level (vs college) | -1.3193 | 1.4312 | ±2.8623 | -0.922 | 0.3566 |  |
| Education: high school or below (vs college) | +3.5915 | 2.6891 | ±5.3782 | +1.336 | 0.1817 |  |
| Site: UCSD (vs UAB) | +0.9049 | 1.8552 | ±3.7103 | +0.488 | 0.6257 |  |
| Site: UW (vs UAB) | +1.4548 | 1.8188 | ±3.6377 | +0.800 | 0.4238 |  |
| Season: spring (vs autumn) | +1.7492 | 1.9688 | ±3.9375 | +0.888 | 0.3743 |  |
| Season: summer (vs autumn) | +1.8873 | 2.0137 | ±4.0273 | +0.937 | 0.3486 |  |
| Season: winter (vs autumn) | +3.4645 | 2.0171 | ±4.0342 | +1.718 | 0.0859 | . |
| Age (years) | -0.1098 | 0.0712 | ±0.1423 | -1.543 | 0.1228 |  |
| BMI (kg/m2) | +0.1535 | 0.0993 | ±0.1985 | +1.547 | 0.1220 |  |
| Hypertension | +2.1172 | 1.5801 | ±3.1603 | +1.340 | 0.1803 |  |
| High cholesterol | -0.0384 | 1.4975 | ±2.9950 | -0.026 | 0.9795 |  |
| Kidney disease | -0.9808 | 2.5509 | ±5.1019 | -0.384 | 0.7006 |  |
| Circulatory disease | -1.0623 | 2.2000 | ±4.3999 | -0.483 | 0.6292 |  |
| Glucose SD, pooled (mg/dL) | -0.0080 | 0.3162 | ±0.6323 | -0.025 | 0.9797 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_sd`  
**Model Diagnostics**: N = **443**, R² = **0.0421**, Adj R² = **0.0108**, F-statistic = **1.34** (p = **0.1784**), Residual SE = **14.220** on **428** df, AIC = **3624.0**, BIC = **3685.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+127.0756** | 6.8990 | ±13.7980 | **+18.419** | **9.17e-76** | *** |
| Education: graduate level (vs college) | -1.3376 | 1.4353 | ±2.8706 | -0.932 | 0.3514 |  |
| Education: high school or below (vs college) | +3.5869 | 2.6911 | ±5.3822 | +1.333 | 0.1826 |  |
| Site: UCSD (vs UAB) | +0.8917 | 1.8520 | ±3.7039 | +0.482 | 0.6302 |  |
| Site: UW (vs UAB) | +1.4389 | 1.8170 | ±3.6339 | +0.792 | 0.4284 |  |
| Season: spring (vs autumn) | +1.7577 | 1.9623 | ±3.9246 | +0.896 | 0.3704 |  |
| Season: summer (vs autumn) | +1.8872 | 2.0118 | ±4.0237 | +0.938 | 0.3482 |  |
| Season: winter (vs autumn) | +3.4711 | 2.0103 | ±4.0205 | +1.727 | 0.0842 | . |
| Age (years) | -0.1094 | 0.0715 | ±0.1429 | -1.530 | 0.1260 |  |
| BMI (kg/m2) | +0.1549 | 0.0992 | ±0.1985 | +1.561 | 0.1185 |  |
| Hypertension | +2.1266 | 1.5774 | ±3.1548 | +1.348 | 0.1776 |  |
| High cholesterol | -0.0515 | 1.4966 | ±2.9932 | -0.034 | 0.9725 |  |
| Kidney disease | -0.9365 | 2.5567 | ±5.1134 | -0.366 | 0.7142 |  |
| Circulatory disease | -1.0618 | 2.1929 | ±4.3859 | -0.484 | 0.6283 |  |
| Avg. daily SD (mg/dL) | -0.0603 | 0.3189 | ±0.6378 | -0.189 | 0.8500 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + glucose_cv`  
**Model Diagnostics**: N = **443**, R² = **0.0434**, Adj R² = **0.0121**, F-statistic = **1.39** (p = **0.1556**), Residual SE = **14.211** on **428** df, AIC = **3623.4**, BIC = **3684.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+122.5772** | 7.2482 | ±14.4965 | **+16.911** | **3.71e-64** | *** |
| Education: graduate level (vs college) | -1.2481 | 1.4256 | ±2.8512 | -0.875 | 0.3813 |  |
| Education: high school or below (vs college) | +3.5362 | 2.6786 | ±5.3572 | +1.320 | 0.1868 |  |
| Site: UCSD (vs UAB) | +1.0187 | 1.8673 | ±3.7346 | +0.546 | 0.5854 |  |
| Site: UW (vs UAB) | +1.5803 | 1.8345 | ±3.6689 | +0.861 | 0.3890 |  |
| Season: spring (vs autumn) | +1.6507 | 1.9706 | ±3.9411 | +0.838 | 0.4022 |  |
| Season: summer (vs autumn) | +1.8543 | 2.0174 | ±4.0348 | +0.919 | 0.3580 |  |
| Season: winter (vs autumn) | +3.3481 | 2.0270 | ±4.0540 | +1.652 | 0.0986 | . |
| Age (years) | -0.1114 | 0.0712 | ±0.1425 | -1.563 | 0.1180 |  |
| BMI (kg/m2) | +0.1524 | 0.0996 | ±0.1992 | +1.531 | 0.1259 |  |
| Hypertension | +2.0758 | 1.5809 | ±3.1617 | +1.313 | 0.1892 |  |
| High cholesterol | +0.0113 | 1.4990 | ±2.9980 | +0.008 | 0.9940 |  |
| Kidney disease | -1.1436 | 2.5537 | ±5.1073 | -0.448 | 0.6543 |  |
| Circulatory disease | -1.1234 | 2.2003 | ±4.4007 | -0.511 | 0.6097 |  |
| CV (%) | +0.2528 | 0.3572 | ±0.7144 | +0.708 | 0.4791 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mean_to_sd_ratio`  
**Model Diagnostics**: N = **443**, R² = **0.0434**, Adj R² = **0.0121**, F-statistic = **1.39** (p = **0.1562**), Residual SE = **14.211** on **428** df, AIC = **3623.4**, BIC = **3684.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.7977** | 8.0514 | ±16.1029 | **+16.121** | **1.81e-58** | *** |
| Education: graduate level (vs college) | -1.2387 | 1.4250 | ±2.8500 | -0.869 | 0.3847 |  |
| Education: high school or below (vs college) | +3.5268 | 2.6764 | ±5.3527 | +1.318 | 0.1876 |  |
| Site: UCSD (vs UAB) | +0.9984 | 1.8636 | ±3.7271 | +0.536 | 0.5921 |  |
| Site: UW (vs UAB) | +1.5606 | 1.8321 | ±3.6641 | +0.852 | 0.3943 |  |
| Season: spring (vs autumn) | +1.6436 | 1.9731 | ±3.9462 | +0.833 | 0.4049 |  |
| Season: summer (vs autumn) | +1.8576 | 2.0156 | ±4.0312 | +0.922 | 0.3567 |  |
| Season: winter (vs autumn) | +3.3521 | 2.0280 | ±4.0559 | +1.653 | 0.0983 | . |
| Age (years) | -0.1109 | 0.0711 | ±0.1422 | -1.560 | 0.1188 |  |
| BMI (kg/m2) | +0.1526 | 0.0995 | ±0.1990 | +1.534 | 0.1251 |  |
| Hypertension | +2.0741 | 1.5813 | ±3.1625 | +1.312 | 0.1896 |  |
| High cholesterol | +0.0153 | 1.4978 | ±2.9956 | +0.010 | 0.9919 |  |
| Kidney disease | -1.0993 | 2.5584 | ±5.1167 | -0.430 | 0.6674 |  |
| Circulatory disease | -1.1031 | 2.1980 | ±4.3960 | -0.502 | 0.6158 |  |
| Mean / SD ratio | -0.5079 | 0.7254 | ±1.4509 | -0.700 | 0.4839 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **443**, R² = **0.0434**, Adj R² = **0.0121**, F-statistic = **1.39** (p = **0.1557**), Residual SE = **14.211** on **428** df, AIC = **3623.4**, BIC = **3684.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+129.5213** | 7.8551 | ±15.7103 | **+16.489** | **4.42e-61** | *** |
| Education: graduate level (vs college) | -1.2239 | 1.4271 | ±2.8542 | -0.858 | 0.3911 |  |
| Education: high school or below (vs college) | +3.5576 | 2.6843 | ±5.3687 | +1.325 | 0.1851 |  |
| Site: UCSD (vs UAB) | +0.9702 | 1.8581 | ±3.7161 | +0.522 | 0.6016 |  |
| Site: UW (vs UAB) | +1.5384 | 1.8254 | ±3.6508 | +0.843 | 0.3994 |  |
| Season: spring (vs autumn) | +1.6508 | 1.9715 | ±3.9430 | +0.837 | 0.4024 |  |
| Season: summer (vs autumn) | +1.8514 | 2.0152 | ±4.0304 | +0.919 | 0.3582 |  |
| Season: winter (vs autumn) | +3.3911 | 2.0199 | ±4.0399 | +1.679 | 0.0932 | . |
| Age (years) | -0.1120 | 0.0715 | ±0.1431 | -1.566 | 0.1172 |  |
| BMI (kg/m2) | +0.1498 | 0.0998 | ±0.1997 | +1.501 | 0.1334 |  |
| Hypertension | +2.1017 | 1.5798 | ±3.1596 | +1.330 | 0.1834 |  |
| High cholesterol | +0.0003 | 1.4980 | ±2.9959 | +0.000 | 0.9999 |  |
| Kidney disease | -1.1018 | 2.5637 | ±5.1275 | -0.430 | 0.6674 |  |
| Circulatory disease | -1.0387 | 2.1911 | ±4.3822 | -0.474 | 0.6355 |  |
| Avg. daily mean/SD | -0.3962 | 0.5618 | ±1.1235 | -0.705 | 0.4807 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **443**, R² = **0.0528**, Adj R² = **0.0218**, F-statistic = **1.70** (p = **0.0519**), Residual SE = **14.140** on **428** df, AIC = **3619.0**, BIC = **3680.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+116.1585** | 7.3782 | ±14.7564 | **+15.743** | **7.62e-56** | *** |
| Education: graduate level (vs college) | -1.3809 | 1.4219 | ±2.8439 | -0.971 | 0.3315 |  |
| Education: high school or below (vs college) | +3.1503 | 2.6824 | ±5.3647 | +1.174 | 0.2402 |  |
| Site: UCSD (vs UAB) | +1.0724 | 1.8310 | ±3.6620 | +0.586 | 0.5581 |  |
| Site: UW (vs UAB) | +1.8568 | 1.7900 | ±3.5801 | +1.037 | 0.2996 |  |
| Season: spring (vs autumn) | +1.7451 | 1.9419 | ±3.8839 | +0.899 | 0.3689 |  |
| Season: summer (vs autumn) | +2.0131 | 1.9828 | ±3.9656 | +1.015 | 0.3100 |  |
| Season: winter (vs autumn) | +3.3832 | 1.9767 | ±3.9534 | +1.712 | 0.0870 | . |
| Age (years) | -0.0967 | 0.0708 | ±0.1415 | -1.366 | 0.1719 |  |
| BMI (kg/m2) | +0.1644 | 0.1001 | ±0.2001 | +1.642 | 0.1005 |  |
| Hypertension | +2.1784 | 1.5825 | ±3.1650 | +1.377 | 0.1686 |  |
| High cholesterol | -0.1121 | 1.5044 | ±3.0088 | -0.075 | 0.9406 |  |
| Kidney disease | -1.3270 | 2.5729 | ±5.1458 | -0.516 | 0.6060 |  |
| Circulatory disease | -0.8759 | 2.1582 | ±4.3165 | -0.406 | 0.6849 |  |
| **MAG (mg/dL/h)** | **+0.2585** | 0.1276 | ±0.2552 | **+2.026** | **0.0428** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_range`  
**Model Diagnostics**: N = **443**, R² = **0.0428**, Adj R² = **0.0115**, F-statistic = **1.37** (p = **0.1655**), Residual SE = **14.215** on **428** df, AIC = **3623.6**, BIC = **3685.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+123.1777** | 7.6144 | ±15.2288 | **+16.177** | **7.33e-59** | *** |
| Education: graduate level (vs college) | -1.2910 | 1.4308 | ±2.8616 | -0.902 | 0.3669 |  |
| Education: high school or below (vs college) | +3.5773 | 2.6858 | ±5.3716 | +1.332 | 0.1829 |  |
| Site: UCSD (vs UAB) | +0.9634 | 1.8558 | ±3.7115 | +0.519 | 0.6037 |  |
| Site: UW (vs UAB) | +1.5204 | 1.8199 | ±3.6399 | +0.835 | 0.4035 |  |
| Season: spring (vs autumn) | +1.7067 | 1.9677 | ±3.9355 | +0.867 | 0.3858 |  |
| Season: summer (vs autumn) | +1.8808 | 2.0118 | ±4.0236 | +0.935 | 0.3498 |  |
| Season: winter (vs autumn) | +3.4118 | 2.0140 | ±4.0279 | +1.694 | 0.0902 | . |
| Age (years) | -0.1106 | 0.0711 | ±0.1422 | -1.556 | 0.1198 |  |
| BMI (kg/m2) | +0.1578 | 0.0993 | ±0.1985 | +1.590 | 0.1119 |  |
| Hypertension | +2.1356 | 1.5896 | ±3.1793 | +1.343 | 0.1791 |  |
| High cholesterol | -0.0317 | 1.5024 | ±3.0048 | -0.021 | 0.9832 |  |
| Kidney disease | -1.0750 | 2.5733 | ±5.1466 | -0.418 | 0.6761 |  |
| Circulatory disease | -1.0614 | 2.1911 | ±4.3822 | -0.484 | 0.6281 |  |
| Avg. daily range (mg/dL) | +0.0367 | 0.0716 | ±0.1432 | +0.513 | 0.6081 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + sd_of_daily_means`  
**Model Diagnostics**: N = **443**, R² = **0.0420**, Adj R² = **0.0107**, F-statistic = **1.34** (p = **0.1800**), Residual SE = **14.221** on **428** df, AIC = **3624.0**, BIC = **3685.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.0764** | 5.8438 | ±11.6876 | **+21.574** | **3.13e-103** | *** |
| Education: graduate level (vs college) | -1.3207 | 1.4308 | ±2.8616 | -0.923 | 0.3560 |  |
| Education: high school or below (vs college) | +3.5781 | 2.6874 | ±5.3749 | +1.331 | 0.1831 |  |
| Site: UCSD (vs UAB) | +0.9153 | 1.8485 | ±3.6971 | +0.495 | 0.6205 |  |
| Site: UW (vs UAB) | +1.4575 | 1.8133 | ±3.6266 | +0.804 | 0.4215 |  |
| Season: spring (vs autumn) | +1.7382 | 1.9748 | ±3.9495 | +0.880 | 0.3787 |  |
| Season: summer (vs autumn) | +1.8792 | 2.0284 | ±4.0568 | +0.926 | 0.3542 |  |
| Season: winter (vs autumn) | +3.4504 | 2.0322 | ±4.0643 | +1.698 | 0.0895 | . |
| Age (years) | -0.1097 | 0.0709 | ±0.1418 | -1.547 | 0.1218 |  |
| BMI (kg/m2) | +0.1533 | 0.0992 | ±0.1985 | +1.545 | 0.1223 |  |
| Hypertension | +2.1042 | 1.6010 | ±3.2020 | +1.314 | 0.1888 |  |
| High cholesterol | -0.0396 | 1.5035 | ±3.0069 | -0.026 | 0.9790 |  |
| Kidney disease | -0.9858 | 2.6008 | ±5.2016 | -0.379 | 0.7047 |  |
| Circulatory disease | -1.0784 | 2.2039 | ±4.4078 | -0.489 | 0.6246 |  |
| SD of daily means (mg/dL) | +0.0271 | 0.3513 | ±0.7025 | +0.077 | 0.9385 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tir_overall`  
**Model Diagnostics**: N = **443**, R² = **0.0429**, Adj R² = **0.0116**, F-statistic = **1.37** (p = **0.1642**), Residual SE = **14.214** on **428** df, AIC = **3623.6**, BIC = **3685.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +269.4891 | 241.0365 | ±482.0730 | +1.118 | 0.2635 |  |
| Education: graduate level (vs college) | -1.3010 | 1.4294 | ±2.8588 | -0.910 | 0.3627 |  |
| Education: high school or below (vs college) | +3.6115 | 2.6982 | ±5.3964 | +1.338 | 0.1807 |  |
| Site: UCSD (vs UAB) | +0.9807 | 1.8604 | ±3.7208 | +0.527 | 0.5981 |  |
| Site: UW (vs UAB) | +1.5156 | 1.8184 | ±3.6368 | +0.833 | 0.4046 |  |
| Season: spring (vs autumn) | +1.7367 | 1.9527 | ±3.9053 | +0.889 | 0.3738 |  |
| Season: summer (vs autumn) | +1.8593 | 2.0127 | ±4.0254 | +0.924 | 0.3556 |  |
| Season: winter (vs autumn) | +3.4055 | 2.0163 | ±4.0325 | +1.689 | 0.0912 | . |
| Age (years) | -0.1087 | 0.0707 | ±0.1415 | -1.537 | 0.1243 |  |
| BMI (kg/m2) | +0.1561 | 0.0978 | ±0.1957 | +1.595 | 0.1107 |  |
| Hypertension | +2.1013 | 1.5834 | ±3.1668 | +1.327 | 0.1845 |  |
| High cholesterol | -0.0636 | 1.5103 | ±3.0206 | -0.042 | 0.9664 |  |
| Kidney disease | -1.0931 | 2.5477 | ±5.0953 | -0.429 | 0.6679 |  |
| Circulatory disease | -1.0458 | 2.1809 | ±4.3619 | -0.480 | 0.6316 |  |
| Time in range 70-180, pooled (%) | -1.4409 | 2.4167 | ±4.8334 | -0.596 | 0.5510 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tir`  
**Model Diagnostics**: N = **443**, R² = **0.0425**, Adj R² = **0.0112**, F-statistic = **1.36** (p = **0.1710**), Residual SE = **14.217** on **428** df, AIC = **3623.8**, BIC = **3685.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +230.3051 | 242.0863 | ±484.1726 | +0.951 | 0.3414 |  |
| Education: graduate level (vs college) | -1.2971 | 1.4336 | ±2.8672 | -0.905 | 0.3656 |  |
| Education: high school or below (vs college) | +3.6141 | 2.7007 | ±5.4015 | +1.338 | 0.1808 |  |
| Site: UCSD (vs UAB) | +0.9326 | 1.8568 | ±3.7136 | +0.502 | 0.6155 |  |
| Site: UW (vs UAB) | +1.4684 | 1.8149 | ±3.6297 | +0.809 | 0.4185 |  |
| Season: spring (vs autumn) | +1.7558 | 1.9485 | ±3.8969 | +0.901 | 0.3675 |  |
| Season: summer (vs autumn) | +1.9119 | 2.0059 | ±4.0117 | +0.953 | 0.3405 |  |
| Season: winter (vs autumn) | +3.4489 | 2.0115 | ±4.0230 | +1.715 | 0.0864 | . |
| Age (years) | -0.1088 | 0.0708 | ±0.1417 | -1.536 | 0.1246 |  |
| BMI (kg/m2) | +0.1540 | 0.0990 | ±0.1980 | +1.555 | 0.1199 |  |
| Hypertension | +2.1381 | 1.5917 | ±3.1833 | +1.343 | 0.1792 |  |
| High cholesterol | -0.0704 | 1.5166 | ±3.0333 | -0.046 | 0.9630 |  |
| Kidney disease | -1.0336 | 2.5762 | ±5.1525 | -0.401 | 0.6883 |  |
| Circulatory disease | -1.0723 | 2.1932 | ±4.3865 | -0.489 | 0.6249 |  |
| Avg. daily time in range 70-180 (%) | -1.0461 | 2.4265 | ±4.8531 | -0.431 | 0.6664 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + any_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.0420**, Adj R² = **0.0107**, F-statistic = **1.34** (p = **0.1802**), Residual SE = **14.221** on **428** df, AIC = **3624.0**, BIC = **3685.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.2172** | 5.6183 | ±11.2365 | **+22.466** | **9.02e-112** | *** |
| Education: graduate level (vs college) | -1.3175 | 1.4252 | ±2.8504 | -0.924 | 0.3553 |  |
| Education: high school or below (vs college) | +3.5887 | 2.6926 | ±5.3852 | +1.333 | 0.1826 |  |
| Site: UCSD (vs UAB) | +0.8994 | 1.8611 | ±3.7223 | +0.483 | 0.6289 |  |
| Site: UW (vs UAB) | +1.4532 | 1.8059 | ±3.6119 | +0.805 | 0.4210 |  |
| Season: spring (vs autumn) | +1.7527 | 1.9637 | ±3.9273 | +0.893 | 0.3721 |  |
| Season: summer (vs autumn) | +1.8901 | 2.0104 | ±4.0209 | +0.940 | 0.3471 |  |
| Season: winter (vs autumn) | +3.4664 | 2.0218 | ±4.0436 | +1.715 | 0.0864 | . |
| Age (years) | -0.1099 | 0.0707 | ±0.1415 | -1.553 | 0.1204 |  |
| BMI (kg/m2) | +0.1534 | 0.0993 | ±0.1986 | +1.545 | 0.1224 |  |
| Hypertension | +2.1175 | 1.5837 | ±3.1674 | +1.337 | 0.1812 |  |
| High cholesterol | -0.0361 | 1.5028 | ±3.0056 | -0.024 | 0.9808 |  |
| Kidney disease | -0.9933 | 2.5935 | ±5.1870 | -0.383 | 0.7017 |  |
| Circulatory disease | -1.0628 | 2.1908 | ±4.3816 | -0.485 | 0.6276 |  |
| Any reading < 54 during wear (0/1) | -0.0479 | 1.8803 | ±3.7606 | -0.025 | 0.9797 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_severe_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.0429**, Adj R² = **0.0116**, F-statistic = **1.37** (p = **0.1644**), Residual SE = **14.214** on **428** df, AIC = **3623.6**, BIC = **3685.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.9450** | 5.6752 | ±11.3505 | **+22.192** | **4.10e-109** | *** |
| Education: graduate level (vs college) | -1.3200 | 1.4269 | ±2.8538 | -0.925 | 0.3549 |  |
| Education: high school or below (vs college) | +3.6932 | 2.6947 | ±5.3894 | +1.371 | 0.1705 |  |
| Site: UCSD (vs UAB) | +1.0623 | 1.8636 | ±3.7272 | +0.570 | 0.5687 |  |
| Site: UW (vs UAB) | +1.5353 | 1.8130 | ±3.6259 | +0.847 | 0.3971 |  |
| Season: spring (vs autumn) | +1.7602 | 1.9503 | ±3.9006 | +0.903 | 0.3668 |  |
| Season: summer (vs autumn) | +1.8754 | 2.0101 | ±4.0201 | +0.933 | 0.3508 |  |
| Season: winter (vs autumn) | +3.4208 | 2.0099 | ±4.0198 | +1.702 | 0.0888 | . |
| Age (years) | -0.1066 | 0.0708 | ±0.1416 | -1.505 | 0.1322 |  |
| BMI (kg/m2) | +0.1488 | 0.1004 | ±0.2008 | +1.483 | 0.1381 |  |
| Hypertension | +2.0194 | 1.5959 | ±3.1918 | +1.265 | 0.2057 |  |
| High cholesterol | -0.0056 | 1.5034 | ±3.0067 | -0.004 | 0.9970 |  |
| Kidney disease | -0.9003 | 2.5897 | ±5.1795 | -0.348 | 0.7281 |  |
| Circulatory disease | -1.1163 | 2.1764 | ±4.3528 | -0.513 | 0.6080 |  |
| Time < 54 (%) | +8.1730 | 12.8277 | ±25.6554 | +0.637 | 0.5240 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **443**, R² = **0.0480**, Adj R² = **0.0168**, F-statistic = **1.54** (p = **0.0934**), Residual SE = **14.177** on **428** df, AIC = **3621.2**, BIC = **3682.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.7905** | 5.6677 | ±11.3354 | **+22.194** | **3.90e-109** | *** |
| Education: graduate level (vs college) | -1.3433 | 1.4204 | ±2.8409 | -0.946 | 0.3443 |  |
| Education: high school or below (vs college) | +3.7075 | 2.6954 | ±5.3907 | +1.376 | 0.1690 |  |
| Site: UCSD (vs UAB) | +1.0859 | 1.8445 | ±3.6890 | +0.589 | 0.5560 |  |
| Site: UW (vs UAB) | +1.4911 | 1.8016 | ±3.6032 | +0.828 | 0.4079 |  |
| Season: spring (vs autumn) | +1.8379 | 1.9395 | ±3.8790 | +0.948 | 0.3433 |  |
| Season: summer (vs autumn) | +2.0925 | 1.9980 | ±3.9959 | +1.047 | 0.2949 |  |
| Season: winter (vs autumn) | +3.4913 | 1.9935 | ±3.9871 | +1.751 | 0.0799 | . |
| Age (years) | -0.1066 | 0.0707 | ±0.1415 | -1.507 | 0.1318 |  |
| BMI (kg/m2) | +0.1486 | 0.0994 | ±0.1988 | +1.495 | 0.1348 |  |
| Hypertension | +2.0217 | 1.5703 | ±3.1406 | +1.287 | 0.1979 |  |
| High cholesterol | -0.0361 | 1.5033 | ±3.0065 | -0.024 | 0.9809 |  |
| Kidney disease | -0.8626 | 2.5877 | ±5.1754 | -0.333 | 0.7389 |  |
| Circulatory disease | -1.2738 | 2.1574 | ±4.3148 | -0.590 | 0.5549 |  |
| Avg. daily time < 54 (%) | +28.1690 | 15.0602 | ±30.1203 | +1.870 | 0.0614 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hypo`  
**Model Diagnostics**: N = **443**, R² = **0.0451**, Adj R² = **0.0138**, F-statistic = **1.44** (p = **0.1297**), Residual SE = **14.198** on **428** df, AIC = **3622.6**, BIC = **3684.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.5349** | 5.6328 | ±11.2656 | **+22.286** | **5.00e-110** | *** |
| Education: graduate level (vs college) | -1.2736 | 1.4165 | ±2.8331 | -0.899 | 0.3686 |  |
| Education: high school or below (vs college) | +3.4180 | 2.7142 | ±5.4284 | +1.259 | 0.2079 |  |
| Site: UCSD (vs UAB) | +1.0419 | 1.8485 | ±3.6970 | +0.564 | 0.5730 |  |
| Site: UW (vs UAB) | +1.6174 | 1.8107 | ±3.6214 | +0.893 | 0.3717 |  |
| Season: spring (vs autumn) | +1.6985 | 1.9444 | ±3.8887 | +0.874 | 0.3823 |  |
| Season: summer (vs autumn) | +1.8467 | 2.0163 | ±4.0326 | +0.916 | 0.3597 |  |
| Season: winter (vs autumn) | +3.3452 | 2.0162 | ±4.0325 | +1.659 | 0.0971 | . |
| Age (years) | -0.1097 | 0.0710 | ±0.1420 | -1.546 | 0.1221 |  |
| BMI (kg/m2) | +0.1538 | 0.0995 | ±0.1990 | +1.546 | 0.1222 |  |
| Hypertension | +2.2190 | 1.5810 | ±3.1619 | +1.404 | 0.1605 |  |
| High cholesterol | -0.1778 | 1.5234 | ±3.0467 | -0.117 | 0.9071 |  |
| Kidney disease | -0.7338 | 2.6362 | ±5.2723 | -0.278 | 0.7807 |  |
| Circulatory disease | -1.0295 | 2.1859 | ±4.3717 | -0.471 | 0.6376 |  |
| Time 54-69, pooled (%) | +4.4375 | 3.7906 | ±7.5811 | +1.171 | 0.2417 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **443**, R² = **0.0451**, Adj R² = **0.0139**, F-statistic = **1.45** (p = **0.1286**), Residual SE = **14.198** on **428** df, AIC = **3622.5**, BIC = **3683.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.6088** | 5.6266 | ±11.2531 | **+22.324** | **2.15e-110** | *** |
| Education: graduate level (vs college) | -1.2387 | 1.4126 | ±2.8253 | -0.877 | 0.3806 |  |
| Education: high school or below (vs college) | +3.4022 | 2.7138 | ±5.4277 | +1.254 | 0.2100 |  |
| Site: UCSD (vs UAB) | +0.9749 | 1.8467 | ±3.6933 | +0.528 | 0.5976 |  |
| Site: UW (vs UAB) | +1.5497 | 1.8050 | ±3.6100 | +0.859 | 0.3906 |  |
| Season: spring (vs autumn) | +1.8008 | 1.9389 | ±3.8779 | +0.929 | 0.3530 |  |
| Season: summer (vs autumn) | +1.9691 | 2.0189 | ±4.0378 | +0.975 | 0.3294 |  |
| Season: winter (vs autumn) | +3.3948 | 2.0146 | ±4.0292 | +1.685 | 0.0920 | . |
| Age (years) | -0.1108 | 0.0711 | ±0.1421 | -1.559 | 0.1190 |  |
| BMI (kg/m2) | +0.1534 | 0.0993 | ±0.1986 | +1.544 | 0.1225 |  |
| Hypertension | +2.3263 | 1.5926 | ±3.1853 | +1.461 | 0.1441 |  |
| High cholesterol | -0.1664 | 1.5222 | ±3.0444 | -0.109 | 0.9130 |  |
| Kidney disease | -0.8103 | 2.6323 | ±5.2645 | -0.308 | 0.7582 |  |
| Circulatory disease | -1.0909 | 2.1852 | ±4.3703 | -0.499 | 0.6176 |  |
| Avg. daily time 54-69 (%) | +4.5622 | 3.7603 | ±7.5206 | +1.213 | 0.2250 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tbr_below_70`  
**Model Diagnostics**: N = **443**, R² = **0.0453**, Adj R² = **0.0140**, F-statistic = **1.45** (p = **0.1272**), Residual SE = **14.197** on **428** df, AIC = **3622.5**, BIC = **3683.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.4617** | 5.6423 | ±11.2846 | **+22.236** | **1.54e-109** | *** |
| Education: graduate level (vs college) | -1.2787 | 1.4174 | ±2.8348 | -0.902 | 0.3670 |  |
| Education: high school or below (vs college) | +3.4836 | 2.7128 | ±5.4257 | +1.284 | 0.1991 |  |
| Site: UCSD (vs UAB) | +1.1073 | 1.8525 | ±3.7049 | +0.598 | 0.5500 |  |
| Site: UW (vs UAB) | +1.6423 | 1.8113 | ±3.6227 | +0.907 | 0.3646 |  |
| Season: spring (vs autumn) | +1.7092 | 1.9425 | ±3.8851 | +0.880 | 0.3789 |  |
| Season: summer (vs autumn) | +1.8445 | 2.0130 | ±4.0260 | +0.916 | 0.3595 |  |
| Season: winter (vs autumn) | +3.3348 | 2.0149 | ±4.0299 | +1.655 | 0.0979 | . |
| Age (years) | -0.1081 | 0.0709 | ±0.1418 | -1.525 | 0.1273 |  |
| BMI (kg/m2) | +0.1515 | 0.0999 | ±0.1997 | +1.517 | 0.1293 |  |
| Hypertension | +2.1628 | 1.5798 | ±3.1596 | +1.369 | 0.1710 |  |
| High cholesterol | -0.1507 | 1.5183 | ±3.0366 | -0.099 | 0.9210 |  |
| Kidney disease | -0.7117 | 2.6331 | ±5.2662 | -0.270 | 0.7869 |  |
| Circulatory disease | -1.0583 | 2.1807 | ±4.3615 | -0.485 | 0.6275 |  |
| Time < 70 (%) | +4.0626 | 3.3479 | ±6.6958 | +1.213 | 0.2250 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tbr`  
**Model Diagnostics**: N = **443**, R² = **0.0465**, Adj R² = **0.0153**, F-statistic = **1.49** (p = **0.1106**), Residual SE = **14.187** on **428** df, AIC = **3621.9**, BIC = **3683.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.4805** | 5.6244 | ±11.2488 | **+22.310** | **2.95e-110** | *** |
| Education: graduate level (vs college) | -1.2362 | 1.4119 | ±2.8237 | -0.876 | 0.3813 |  |
| Education: high school or below (vs college) | +3.4057 | 2.7176 | ±5.4353 | +1.253 | 0.2101 |  |
| Site: UCSD (vs UAB) | +1.0125 | 1.8452 | ±3.6904 | +0.549 | 0.5832 |  |
| Site: UW (vs UAB) | +1.5640 | 1.8023 | ±3.6046 | +0.868 | 0.3855 |  |
| Season: spring (vs autumn) | +1.8219 | 1.9355 | ±3.8710 | +0.941 | 0.3466 |  |
| Season: summer (vs autumn) | +2.0130 | 2.0161 | ±4.0323 | +0.998 | 0.3181 |  |
| Season: winter (vs autumn) | +3.3939 | 2.0120 | ±4.0240 | +1.687 | 0.0916 | . |
| Age (years) | -0.1103 | 0.0710 | ±0.1421 | -1.553 | 0.1205 |  |
| BMI (kg/m2) | +0.1525 | 0.0993 | ±0.1987 | +1.536 | 0.1246 |  |
| Hypertension | +2.3293 | 1.5865 | ±3.1731 | +1.468 | 0.1421 |  |
| High cholesterol | -0.1783 | 1.5208 | ±3.0417 | -0.117 | 0.9067 |  |
| Kidney disease | -0.7719 | 2.6318 | ±5.2636 | -0.293 | 0.7693 |  |
| Circulatory disease | -1.1303 | 2.1794 | ±4.3588 | -0.519 | 0.6040 |  |
| Avg. daily time < 70 (%) | +4.9804 | 3.4454 | ±6.8909 | +1.446 | 0.1483 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.0422**, Adj R² = **0.0109**, F-statistic = **1.35** (p = **0.1755**), Residual SE = **14.219** on **428** df, AIC = **3623.9**, BIC = **3685.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +556.8655 | 1324.3762 | ±2648.7524 | +0.420 | 0.6741 |  |
| Education: graduate level (vs college) | -1.3191 | 1.4286 | ±2.8572 | -0.923 | 0.3558 |  |
| Education: high school or below (vs college) | +3.6463 | 2.6945 | ±5.3889 | +1.353 | 0.1760 |  |
| Site: UCSD (vs UAB) | +0.9955 | 1.8645 | ±3.7290 | +0.534 | 0.5934 |  |
| Site: UW (vs UAB) | +1.5035 | 1.8141 | ±3.6282 | +0.829 | 0.4072 |  |
| Season: spring (vs autumn) | +1.7497 | 1.9533 | ±3.9065 | +0.896 | 0.3704 |  |
| Season: summer (vs autumn) | +1.8814 | 2.0146 | ±4.0291 | +0.934 | 0.3504 |  |
| Season: winter (vs autumn) | +3.4364 | 2.0152 | ±4.0304 | +1.705 | 0.0881 | . |
| Age (years) | -0.1078 | 0.0708 | ±0.1415 | -1.524 | 0.1275 |  |
| BMI (kg/m2) | +0.1513 | 0.1000 | ±0.2000 | +1.513 | 0.1304 |  |
| Hypertension | +2.0664 | 1.5945 | ±3.1891 | +1.296 | 0.1950 |  |
| High cholesterol | -0.0213 | 1.5026 | ±3.0052 | -0.014 | 0.9887 |  |
| Kidney disease | -0.9420 | 2.5902 | ±5.1803 | -0.364 | 0.7161 |  |
| Circulatory disease | -1.0926 | 2.1818 | ±4.3635 | -0.501 | 0.6165 |  |
| Time 54-250, pooled (%) | -4.3083 | 13.2439 | ±26.4879 | -0.325 | 0.7450 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **443**, R² = **0.0452**, Adj R² = **0.0140**, F-statistic = **1.45** (p = **0.1277**), Residual SE = **14.197** on **428** df, AIC = **3622.5**, BIC = **3683.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2148.4726 | 1758.0223 | ±3516.0446 | +1.222 | 0.2217 |  |
| Education: graduate level (vs college) | -1.3380 | 1.4250 | ±2.8500 | -0.939 | 0.3477 |  |
| Education: high school or below (vs college) | +3.6829 | 2.6928 | ±5.3855 | +1.368 | 0.1714 |  |
| Site: UCSD (vs UAB) | +1.0677 | 1.8486 | ±3.6973 | +0.578 | 0.5635 |  |
| Site: UW (vs UAB) | +1.5063 | 1.8095 | ±3.6190 | +0.832 | 0.4052 |  |
| Season: spring (vs autumn) | +1.7903 | 1.9446 | ±3.8892 | +0.921 | 0.3572 |  |
| Season: summer (vs autumn) | +2.0378 | 2.0008 | ±4.0017 | +1.018 | 0.3084 |  |
| Season: winter (vs autumn) | +3.4643 | 1.9993 | ±3.9987 | +1.733 | 0.0832 | . |
| Age (years) | -0.1061 | 0.0708 | ±0.1415 | -1.499 | 0.1338 |  |
| BMI (kg/m2) | +0.1514 | 0.0992 | ±0.1985 | +1.525 | 0.1271 |  |
| Hypertension | +2.0585 | 1.5727 | ±3.1455 | +1.309 | 0.1906 |  |
| High cholesterol | -0.0425 | 1.5049 | ±3.0098 | -0.028 | 0.9775 |  |
| Kidney disease | -0.8998 | 2.5872 | ±5.1744 | -0.348 | 0.7280 |  |
| Circulatory disease | -1.2191 | 2.1674 | ±4.3349 | -0.562 | 0.5738 |  |
| Avg. daily time 54-250 (%) | -20.2271 | 17.5788 | ±35.1575 | -1.151 | 0.2499 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + pct_mod_hyper`  
**Model Diagnostics**: N = **443**, R² = **0.0420**, Adj R² = **0.0107**, F-statistic = **1.34** (p = **0.1793**), Residual SE = **14.221** on **428** df, AIC = **3624.0**, BIC = **3685.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.3382** | 5.7163 | ±11.4327 | **+22.101** | **3.08e-108** | *** |
| Education: graduate level (vs college) | -1.3177 | 1.4283 | ±2.8567 | -0.923 | 0.3562 |  |
| Education: high school or below (vs college) | +3.5761 | 2.6939 | ±5.3878 | +1.327 | 0.1844 |  |
| Site: UCSD (vs UAB) | +0.9079 | 1.8481 | ±3.6961 | +0.491 | 0.6233 |  |
| Site: UW (vs UAB) | +1.4603 | 1.8117 | ±3.6234 | +0.806 | 0.4202 |  |
| Season: spring (vs autumn) | +1.7458 | 1.9507 | ±3.9013 | +0.895 | 0.3708 |  |
| Season: summer (vs autumn) | +1.8898 | 2.0147 | ±4.0294 | +0.938 | 0.3483 |  |
| Season: winter (vs autumn) | +3.4638 | 2.0087 | ±4.0173 | +1.724 | 0.0846 | . |
| Age (years) | -0.1099 | 0.0709 | ±0.1419 | -1.549 | 0.1213 |  |
| BMI (kg/m2) | +0.1526 | 0.1001 | ±0.2001 | +1.525 | 0.1272 |  |
| Hypertension | +2.1222 | 1.5784 | ±3.1568 | +1.345 | 0.1788 |  |
| High cholesterol | -0.0394 | 1.5024 | ±3.0048 | -0.026 | 0.9791 |  |
| Kidney disease | -0.9375 | 2.5751 | ±5.1502 | -0.364 | 0.7158 |  |
| Circulatory disease | -1.0686 | 2.1857 | ±4.3713 | -0.489 | 0.6249 |  |
| Time 181-250, pooled (%) | -0.3571 | 2.5811 | ±5.1622 | -0.138 | 0.8900 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **443**, R² = **0.0423**, Adj R² = **0.0110**, F-statistic = **1.35** (p = **0.1737**), Residual SE = **14.218** on **428** df, AIC = **3623.8**, BIC = **3685.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.5254** | 5.7094 | ±11.4189 | **+22.161** | **8.22e-109** | *** |
| Education: graduate level (vs college) | -1.3199 | 1.4283 | ±2.8566 | -0.924 | 0.3554 |  |
| Education: high school or below (vs college) | +3.5337 | 2.7031 | ±5.4063 | +1.307 | 0.1911 |  |
| Site: UCSD (vs UAB) | +0.9069 | 1.8446 | ±3.6891 | +0.492 | 0.6230 |  |
| Site: UW (vs UAB) | +1.4700 | 1.8093 | ±3.6185 | +0.812 | 0.4165 |  |
| Season: spring (vs autumn) | +1.7522 | 1.9536 | ±3.9073 | +0.897 | 0.3698 |  |
| Season: summer (vs autumn) | +1.8880 | 2.0147 | ±4.0294 | +0.937 | 0.3487 |  |
| Season: winter (vs autumn) | +3.4590 | 2.0084 | ±4.0167 | +1.722 | 0.0850 | . |
| Age (years) | -0.1108 | 0.0709 | ±0.1418 | -1.563 | 0.1181 |  |
| BMI (kg/m2) | +0.1528 | 0.0995 | ±0.1991 | +1.535 | 0.1249 |  |
| Hypertension | +2.1349 | 1.5782 | ±3.1564 | +1.353 | 0.1761 |  |
| High cholesterol | -0.0323 | 1.5056 | ±3.0112 | -0.021 | 0.9829 |  |
| Kidney disease | -0.9042 | 2.5815 | ±5.1630 | -0.350 | 0.7261 |  |
| Circulatory disease | -1.0700 | 2.1841 | ±4.3683 | -0.490 | 0.6242 |  |
| Avg. daily time 181-250 (%) | -0.9606 | 2.6811 | ±5.3622 | -0.358 | 0.7201 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + tar_above_180`  
**Model Diagnostics**: N = **443**, R² = **0.0421**, Adj R² = **0.0107**, F-statistic = **1.34** (p = **0.1786**), Residual SE = **14.220** on **428** df, AIC = **3624.0**, BIC = **3685.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.3883** | 5.7211 | ±11.4422 | **+22.092** | **3.80e-108** | *** |
| Education: graduate level (vs college) | -1.3179 | 1.4282 | ±2.8564 | -0.923 | 0.3561 |  |
| Education: high school or below (vs college) | +3.5708 | 2.6940 | ±5.3880 | +1.325 | 0.1850 |  |
| Site: UCSD (vs UAB) | +0.9072 | 1.8477 | ±3.6954 | +0.491 | 0.6234 |  |
| Site: UW (vs UAB) | +1.4606 | 1.8116 | ±3.6232 | +0.806 | 0.4201 |  |
| Season: spring (vs autumn) | +1.7459 | 1.9507 | ±3.9014 | +0.895 | 0.3708 |  |
| Season: summer (vs autumn) | +1.8908 | 2.0150 | ±4.0300 | +0.938 | 0.3481 |  |
| Season: winter (vs autumn) | +3.4651 | 2.0087 | ±4.0174 | +1.725 | 0.0845 | . |
| Age (years) | -0.1100 | 0.0709 | ±0.1419 | -1.551 | 0.1210 |  |
| BMI (kg/m2) | +0.1523 | 0.1002 | ±0.2005 | +1.519 | 0.1287 |  |
| Hypertension | +2.1248 | 1.5783 | ±3.1566 | +1.346 | 0.1782 |  |
| High cholesterol | -0.0405 | 1.5025 | ±3.0050 | -0.027 | 0.9785 |  |
| Kidney disease | -0.9195 | 2.5772 | ±5.1543 | -0.357 | 0.7213 |  |
| Circulatory disease | -1.0699 | 2.1860 | ±4.3721 | -0.489 | 0.6245 |  |
| Time > 180 (%) | -0.4844 | 2.5785 | ±5.1570 | -0.188 | 0.8510 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + avg_daily_tar`  
**Model Diagnostics**: N = **443**, R² = **0.0424**, Adj R² = **0.0111**, F-statistic = **1.36** (p = **0.1718**), Residual SE = **14.218** on **428** df, AIC = **3623.8**, BIC = **3685.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+126.5777** | 5.7102 | ±11.4203 | **+22.167** | **7.13e-109** | *** |
| Education: graduate level (vs college) | -1.3202 | 1.4280 | ±2.8560 | -0.924 | 0.3552 |  |
| Education: high school or below (vs college) | +3.5254 | 2.7032 | ±5.4064 | +1.304 | 0.1922 |  |
| Site: UCSD (vs UAB) | +0.9050 | 1.8439 | ±3.6878 | +0.491 | 0.6236 |  |
| Site: UW (vs UAB) | +1.4703 | 1.8090 | ±3.6180 | +0.813 | 0.4164 |  |
| Season: spring (vs autumn) | +1.7541 | 1.9538 | ±3.9076 | +0.898 | 0.3693 |  |
| Season: summer (vs autumn) | +1.8880 | 2.0150 | ±4.0300 | +0.937 | 0.3488 |  |
| Season: winter (vs autumn) | +3.4597 | 2.0084 | ±4.0168 | +1.723 | 0.0850 | . |
| Age (years) | -0.1110 | 0.0709 | ±0.1418 | -1.566 | 0.1174 |  |
| BMI (kg/m2) | +0.1526 | 0.0996 | ±0.1992 | +1.532 | 0.1254 |  |
| Hypertension | +2.1371 | 1.5781 | ±3.1562 | +1.354 | 0.1757 |  |
| High cholesterol | -0.0314 | 1.5057 | ±3.0114 | -0.021 | 0.9834 |  |
| Kidney disease | -0.8925 | 2.5829 | ±5.1658 | -0.346 | 0.7297 |  |
| Circulatory disease | -1.0706 | 2.1840 | ±4.3681 | -0.490 | 0.6240 |  |
| Avg. daily time > 180 (%) | -1.0940 | 2.6758 | ±5.3516 | -0.409 | 0.6827 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 443)
**Regression Call / Formula**: `env_voc_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + C(visit_season) + nocturnal_tar`  
**Model Diagnostics**: N = **443**, R² = **0.0431**, Adj R² = **0.0118**, F-statistic = **1.38** (p = **0.1598**), Residual SE = **14.212** on **428** df, AIC = **3623.5**, BIC = **3684.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+125.8066** | 5.7513 | ±11.5027 | **+21.874** | **4.56e-106** | *** |
| Education: graduate level (vs college) | -1.2632 | 1.4294 | ±2.8587 | -0.884 | 0.3768 |  |
| Education: high school or below (vs college) | +3.6248 | 2.6836 | ±5.3672 | +1.351 | 0.1768 |  |
| Site: UCSD (vs UAB) | +0.9051 | 1.8518 | ±3.7036 | +0.489 | 0.6250 |  |
| Site: UW (vs UAB) | +1.4199 | 1.8064 | ±3.6127 | +0.786 | 0.4318 |  |
| Season: spring (vs autumn) | +1.7189 | 1.9490 | ±3.8979 | +0.882 | 0.3778 |  |
| Season: summer (vs autumn) | +1.9141 | 2.0070 | ±4.0141 | +0.954 | 0.3402 |  |
| Season: winter (vs autumn) | +3.3342 | 2.0014 | ±4.0028 | +1.666 | 0.0957 | . |
| Age (years) | -0.1024 | 0.0714 | ±0.1428 | -1.434 | 0.1516 |  |
| BMI (kg/m2) | +0.1489 | 0.1005 | ±0.2010 | +1.482 | 0.1385 |  |
| Hypertension | +2.0098 | 1.5872 | ±3.1744 | +1.266 | 0.2054 |  |
| High cholesterol | -0.0648 | 1.4974 | ±2.9948 | -0.043 | 0.9655 |  |
| Kidney disease | -1.0003 | 2.5927 | ±5.1855 | -0.386 | 0.6996 |  |
| Circulatory disease | -1.0041 | 2.1877 | ±4.3754 | -0.459 | 0.6463 |  |
| Nocturnal time > 180 (%) | +1.4009 | 1.8332 | ±3.6664 | +0.764 | 0.4447 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Steps per wear-day  (domain: Wearable activity; outcome sample N = 401; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **401**, R² = **0.1509**, Adj R² = **0.1291**, F-statistic = **6.93** (p = **5.17e-10**), Residual SE = **3608.410** on **390** df, AIC = **7718.0**, BIC = **7762.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19101.4172** | 1443.8136 | ±2887.6271 | **+13.230** | **5.90e-40** | *** |
| **Education: graduate level (vs college)** | **-812.1959** | 369.3449 | ±738.6898 | **-2.199** | **0.0279** | * |
| Education: high school or below (vs college) | +579.0916 | 857.3039 | ±1714.6078 | +0.675 | 0.4994 |  |
| Site: UCSD (vs UAB) | -348.0806 | 496.0577 | ±992.1153 | -0.702 | 0.4829 |  |
| Site: UW (vs UAB) | -845.5695 | 456.1415 | ±912.2830 | -1.854 | 0.0638 | . |
| **Age (years)** | **-113.0683** | 19.0635 | ±38.1271 | **-5.931** | **3.01e-09** | *** |
| **BMI (kg/m2)** | **-55.6804** | 24.5643 | ±49.1287 | **-2.267** | **0.0234** | * |
| Hypertension | +795.5484 | 450.6364 | ±901.2728 | +1.765 | 0.0775 | . |
| High cholesterol | -420.9695 | 388.7029 | ±777.4058 | -1.083 | 0.2788 |  |
| Kidney disease | -582.1246 | 756.8236 | ±1513.6473 | -0.769 | 0.4418 |  |
| Circulatory disease | -981.1135 | 643.0391 | ±1286.0782 | -1.526 | 0.1271 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **401**, R² = **0.1538**, Adj R² = **0.1299**, F-statistic = **6.43** (p = **7.89e-10**), Residual SE = **3606.812** on **389** df, AIC = **7718.7**, BIC = **7766.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15371.8000** | 3444.4295 | ±6888.8591 | **+4.463** | **8.09e-06** | *** |
| **Education: graduate level (vs college)** | **-789.8550** | 368.6381 | ±737.2762 | **-2.143** | **0.0321** | * |
| Education: high school or below (vs college) | +536.7820 | 859.3253 | ±1718.6507 | +0.625 | 0.5322 |  |
| Site: UCSD (vs UAB) | -316.4580 | 495.5244 | ±991.0489 | -0.639 | 0.5231 |  |
| Site: UW (vs UAB) | -809.5543 | 455.6139 | ±911.2279 | -1.777 | 0.0756 | . |
| **Age (years)** | **-115.1302** | 19.3007 | ±38.6014 | **-5.965** | **2.45e-09** | *** |
| **BMI (kg/m2)** | **-59.0868** | 23.9197 | ±47.8394 | **-2.470** | **0.0135** | * |
| Hypertension | +755.8718 | 450.5498 | ±901.0996 | +1.678 | 0.0934 | . |
| High cholesterol | -528.6720 | 396.5169 | ±793.0338 | -1.333 | 0.1824 |  |
| Kidney disease | -521.7083 | 766.3973 | ±1532.7946 | -0.681 | 0.4960 |  |
| Circulatory disease | -954.0728 | 645.0540 | ±1290.1080 | -1.479 | 0.1391 |  |
| HbA1c (%) | +718.0817 | 600.2386 | ±1200.4772 | +1.196 | 0.2316 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **401**, R² = **0.1513**, Adj R² = **0.1273**, F-statistic = **6.30** (p = **1.32e-09**), Residual SE = **3612.228** on **389** df, AIC = **7719.9**, BIC = **7767.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17940.4760** | 3295.8092 | ±6591.6185 | **+5.443** | **5.23e-08** | *** |
| **Education: graduate level (vs college)** | **-807.1641** | 369.7909 | ±739.5817 | **-2.183** | **0.0291** | * |
| Education: high school or below (vs college) | +593.3343 | 859.5789 | ±1719.1579 | +0.690 | 0.4900 |  |
| Site: UCSD (vs UAB) | -357.3731 | 498.3359 | ±996.6718 | -0.717 | 0.4733 |  |
| Site: UW (vs UAB) | -856.1279 | 459.0762 | ±918.1524 | -1.865 | 0.0622 | . |
| **Age (years)** | **-112.7654** | 19.1042 | ±38.2085 | **-5.903** | **3.58e-09** | *** |
| **BMI (kg/m2)** | **-56.4131** | 24.5127 | ±49.0254 | **-2.301** | **0.0214** | * |
| Hypertension | +781.9682 | 452.1798 | ±904.3596 | +1.729 | 0.0837 | . |
| High cholesterol | -415.6585 | 391.3484 | ±782.6968 | -1.062 | 0.2882 |  |
| Kidney disease | -582.8490 | 767.7277 | ±1535.4554 | -0.759 | 0.4477 |  |
| Circulatory disease | -984.9572 | 645.1277 | ±1290.2553 | -1.527 | 0.1268 |  |
| Mean glucose (mg/dL) | +10.2502 | 26.1080 | ±52.2160 | +0.393 | 0.6946 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **401**, R² = **0.1513**, Adj R² = **0.1273**, F-statistic = **6.30** (p = **1.32e-09**), Residual SE = **3612.228** on **389** df, AIC = **7719.9**, BIC = **7767.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16522.0736** | 6731.2193 | ±13462.4386 | **+2.455** | **0.0141** | * |
| **Education: graduate level (vs college)** | **-807.1641** | 369.7909 | ±739.5817 | **-2.183** | **0.0291** | * |
| Education: high school or below (vs college) | +593.3343 | 859.5789 | ±1719.1579 | +0.690 | 0.4900 |  |
| Site: UCSD (vs UAB) | -357.3731 | 498.3359 | ±996.6718 | -0.717 | 0.4733 |  |
| Site: UW (vs UAB) | -856.1279 | 459.0762 | ±918.1524 | -1.865 | 0.0622 | . |
| **Age (years)** | **-112.7654** | 19.1042 | ±38.2085 | **-5.903** | **3.58e-09** | *** |
| **BMI (kg/m2)** | **-56.4131** | 24.5127 | ±49.0254 | **-2.301** | **0.0214** | * |
| Hypertension | +781.9682 | 452.1798 | ±904.3596 | +1.729 | 0.0837 | . |
| High cholesterol | -415.6585 | 391.3484 | ±782.6968 | -1.062 | 0.2882 |  |
| Kidney disease | -582.8490 | 767.7277 | ±1535.4554 | -0.759 | 0.4477 |  |
| Circulatory disease | -984.9572 | 645.1277 | ±1290.2553 | -1.527 | 0.1268 |  |
| GMI (%) | +428.5203 | 1091.4721 | ±2182.9442 | +0.393 | 0.6946 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **401**, R² = **0.1561**, Adj R² = **0.1322**, F-statistic = **6.54** (p = **5.03e-10**), Residual SE = **3602.059** on **389** df, AIC = **7717.6**, BIC = **7765.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15639.1422** | 2811.5559 | ±5623.1118 | **+5.562** | **2.66e-08** | *** |
| **Education: graduate level (vs college)** | **-776.7281** | 370.8631 | ±741.7263 | **-2.094** | **0.0362** | * |
| Education: high school or below (vs college) | +627.4198 | 857.7357 | ±1715.4714 | +0.731 | 0.4645 |  |
| Site: UCSD (vs UAB) | -422.1595 | 493.4946 | ±986.9892 | -0.855 | 0.3923 |  |
| **Site: UW (vs UAB)** | **-902.8418** | 452.1841 | ±904.3681 | **-1.997** | **0.0459** | * |
| **Age (years)** | **-108.6941** | 19.5353 | ±39.0707 | **-5.564** | **2.64e-08** | *** |
| **BMI (kg/m2)** | **-61.8070** | 24.1193 | ±48.2385 | **-2.563** | **0.0104** | * |
| Hypertension | +743.4495 | 442.6630 | ±885.3260 | +1.679 | 0.0931 | . |
| High cholesterol | -418.2443 | 387.1745 | ±774.3490 | -1.080 | 0.2800 |  |
| Kidney disease | -518.4573 | 772.4589 | ±1544.9178 | -0.671 | 0.5021 |  |
| Circulatory disease | -968.0467 | 643.2632 | ±1286.5264 | -1.505 | 0.1323 |  |
| Nocturnal mean 00-06h (mg/dL) | +29.7234 | 19.7440 | ±39.4880 | +1.505 | 0.1322 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **401**, R² = **0.1516**, Adj R² = **0.1276**, F-statistic = **6.32** (p = **1.23e-09**), Residual SE = **3611.513** on **389** df, AIC = **7719.7**, BIC = **7767.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19826.7034** | 2117.3870 | ±4234.7739 | **+9.364** | **7.69e-21** | *** |
| **Education: graduate level (vs college)** | **-830.7556** | 374.4271 | ±748.8542 | **-2.219** | **0.0265** | * |
| Education: high school or below (vs college) | +568.7302 | 857.9425 | ±1715.8850 | +0.663 | 0.5074 |  |
| Site: UCSD (vs UAB) | -363.1286 | 499.4295 | ±998.8590 | -0.727 | 0.4672 |  |
| Site: UW (vs UAB) | -864.1048 | 467.3144 | ±934.6289 | -1.849 | 0.0644 | . |
| **Age (years)** | **-112.8479** | 19.1403 | ±38.2806 | **-5.896** | **3.73e-09** | *** |
| **BMI (kg/m2)** | **-55.0361** | 24.6748 | ±49.3495 | **-2.230** | **0.0257** | * |
| Hypertension | +810.3104 | 446.1984 | ±892.3968 | +1.816 | 0.0694 | . |
| High cholesterol | -436.4135 | 388.7730 | ±777.5460 | -1.123 | 0.2616 |  |
| Kidney disease | -531.5888 | 759.8074 | ±1519.6148 | -0.700 | 0.4842 |  |
| Circulatory disease | -971.1691 | 646.9602 | ±1293.9203 | -1.501 | 0.1333 |  |
| Glucose SD, pooled (mg/dL) | -43.9526 | 86.7836 | ±173.5672 | -0.506 | 0.6125 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **401**, R² = **0.1519**, Adj R² = **0.1279**, F-statistic = **6.33** (p = **1.16e-09**), Residual SE = **3610.939** on **389** df, AIC = **7719.6**, BIC = **7767.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19864.5556** | 2026.1894 | ±4052.3789 | **+9.804** | **1.08e-22** | *** |
| **Education: graduate level (vs college)** | **-836.4183** | 376.7328 | ±753.4657 | **-2.220** | **0.0264** | * |
| Education: high school or below (vs college) | +561.1172 | 858.7534 | ±1717.5069 | +0.653 | 0.5135 |  |
| Site: UCSD (vs UAB) | -363.7308 | 498.5702 | ±997.1404 | -0.730 | 0.4657 |  |
| Site: UW (vs UAB) | -866.3103 | 466.5564 | ±933.1127 | -1.857 | 0.0633 | . |
| **Age (years)** | **-112.7082** | 19.1489 | ±38.2978 | **-5.886** | **3.96e-09** | *** |
| **BMI (kg/m2)** | **-54.5694** | 24.7562 | ±49.5125 | **-2.204** | **0.0275** | * |
| Hypertension | +805.8953 | 448.1778 | ±896.3555 | +1.798 | 0.0722 | . |
| High cholesterol | -437.3766 | 388.2555 | ±776.5110 | -1.127 | 0.2599 |  |
| Kidney disease | -525.5178 | 757.5389 | ±1515.0778 | -0.694 | 0.4879 |  |
| Circulatory disease | -978.7882 | 647.9175 | ±1295.8350 | -1.511 | 0.1309 |  |
| Avg. daily SD (mg/dL) | -51.3157 | 86.0827 | ±172.1654 | -0.596 | 0.5511 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **401**, R² = **0.1524**, Adj R² = **0.1285**, F-statistic = **6.36** (p = **1.04e-09**), Residual SE = **3609.781** on **389** df, AIC = **7719.3**, BIC = **7767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+20139.0642** | 2039.3795 | ±4078.7590 | **+9.875** | **5.34e-23** | *** |
| **Education: graduate level (vs college)** | **-834.3579** | 373.7362 | ±747.4724 | **-2.232** | **0.0256** | * |
| Education: high school or below (vs college) | +576.1801 | 858.6817 | ±1717.3635 | +0.671 | 0.5022 |  |
| Site: UCSD (vs UAB) | -377.3052 | 499.8729 | ±999.7458 | -0.755 | 0.4504 |  |
| Site: UW (vs UAB) | -881.0845 | 471.1860 | ±942.3719 | -1.870 | 0.0615 | . |
| **Age (years)** | **-112.5227** | 19.1303 | ±38.2606 | **-5.882** | **4.06e-09** | *** |
| **BMI (kg/m2)** | **-55.4284** | 24.4916 | ±48.9832 | **-2.263** | **0.0236** | * |
| Hypertension | +804.0900 | 449.9806 | ±899.9611 | +1.787 | 0.0739 | . |
| High cholesterol | -439.1486 | 387.1757 | ±774.3514 | -1.134 | 0.2567 |  |
| Kidney disease | -511.8392 | 751.2670 | ±1502.5339 | -0.681 | 0.4957 |  |
| Circulatory disease | -969.3311 | 647.8608 | ±1295.7217 | -1.496 | 0.1346 |  |
| CV (%) | -70.8332 | 88.3599 | ±176.7198 | -0.802 | 0.4228 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **401**, R² = **0.1526**, Adj R² = **0.1286**, F-statistic = **6.37** (p = **1.01e-09**), Residual SE = **3609.444** on **389** df, AIC = **7719.2**, BIC = **7767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18049.8742** | 1823.6816 | ±3647.3633 | **+9.897** | **4.27e-23** | *** |
| **Education: graduate level (vs college)** | **-838.2429** | 373.3250 | ±746.6500 | **-2.245** | **0.0247** | * |
| Education: high school or below (vs college) | +581.5853 | 859.6115 | ±1719.2230 | +0.677 | 0.4987 |  |
| Site: UCSD (vs UAB) | -374.7870 | 498.9595 | ±997.9190 | -0.751 | 0.4526 |  |
| Site: UW (vs UAB) | -878.7875 | 468.2257 | ±936.4514 | -1.877 | 0.0605 | . |
| **Age (years)** | **-112.5713** | 19.1382 | ±38.2764 | **-5.882** | **4.05e-09** | *** |
| **BMI (kg/m2)** | **-55.4574** | 24.4519 | ±48.9037 | **-2.268** | **0.0233** | * |
| Hypertension | +803.9728 | 450.0505 | ±900.1010 | +1.786 | 0.0740 | . |
| High cholesterol | -441.7956 | 387.1657 | ±774.3315 | -1.141 | 0.2538 |  |
| Kidney disease | -526.2434 | 748.1382 | ±1496.2763 | -0.703 | 0.4818 |  |
| Circulatory disease | -975.2500 | 647.3513 | ±1294.7026 | -1.507 | 0.1319 |  |
| Mean / SD ratio | +151.5161 | 175.0364 | ±350.0728 | +0.866 | 0.3867 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **401**, R² = **0.1525**, Adj R² = **0.1285**, F-statistic = **6.36** (p = **1.03e-09**), Residual SE = **3609.653** on **389** df, AIC = **7719.3**, BIC = **7767.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18178.3672** | 1747.5301 | ±3495.0603 | **+10.402** | **2.42e-25** | *** |
| **Education: graduate level (vs college)** | **-839.5560** | 374.5158 | ±749.0316 | **-2.242** | **0.0250** | * |
| Education: high school or below (vs college) | +577.8222 | 860.3634 | ±1720.7269 | +0.672 | 0.5018 |  |
| Site: UCSD (vs UAB) | -370.4445 | 497.5374 | ±995.0747 | -0.745 | 0.4565 |  |
| Site: UW (vs UAB) | -876.6372 | 466.1166 | ±932.2333 | -1.881 | 0.0600 | . |
| **Age (years)** | **-112.4000** | 19.1423 | ±38.2846 | **-5.872** | **4.31e-09** | *** |
| **BMI (kg/m2)** | **-54.9459** | 24.5719 | ±49.1438 | **-2.236** | **0.0253** | * |
| Hypertension | +796.4802 | 451.9645 | ±903.9290 | +1.762 | 0.0780 | . |
| High cholesterol | -435.3898 | 387.4963 | ±774.9925 | -1.124 | 0.2612 |  |
| Kidney disease | -526.8860 | 750.9918 | ±1501.9836 | -0.702 | 0.4829 |  |
| Circulatory disease | -991.6395 | 648.1465 | ±1296.2930 | -1.530 | 0.1260 |  |
| Avg. daily mean/SD | +114.5108 | 133.3499 | ±266.6998 | +0.859 | 0.3905 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **401**, R² = **0.1551**, Adj R² = **0.1312**, F-statistic = **6.49** (p = **6.12e-10**), Residual SE = **3604.132** on **389** df, AIC = **7718.1**, BIC = **7766.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17432.0582** | 2081.8272 | ±4163.6543 | **+8.373** | **5.60e-17** | *** |
| **Education: graduate level (vs college)** | **-806.6450** | 370.5338 | ±741.0676 | **-2.177** | **0.0295** | * |
| Education: high school or below (vs college) | +510.1064 | 859.3773 | ±1718.7546 | +0.594 | 0.5528 |  |
| Site: UCSD (vs UAB) | -321.1410 | 496.1677 | ±992.3355 | -0.647 | 0.5175 |  |
| Site: UW (vs UAB) | -781.6477 | 469.0526 | ±938.1052 | -1.666 | 0.0956 | . |
| **Age (years)** | **-110.8887** | 19.2142 | ±38.4285 | **-5.771** | **7.87e-09** | *** |
| **BMI (kg/m2)** | **-54.0433** | 24.6333 | ±49.2667 | **-2.194** | **0.0282** | * |
| Hypertension | +817.6605 | 454.0104 | ±908.0208 | +1.801 | 0.0717 | . |
| High cholesterol | -438.0272 | 392.1328 | ±784.2656 | -1.117 | 0.2640 |  |
| Kidney disease | -669.0389 | 769.8659 | ±1539.7318 | -0.869 | 0.3848 |  |
| Circulatory disease | -971.6631 | 642.4045 | ±1284.8089 | -1.513 | 0.1304 |  |
| MAG (mg/dL/h) | +43.0031 | 36.6039 | ±73.2079 | +1.175 | 0.2401 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **401**, R² = **0.1510**, Adj R² = **0.1270**, F-statistic = **6.29** (p = **1.39e-09**), Residual SE = **3612.849** on **389** df, AIC = **7720.0**, BIC = **7767.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19378.5965** | 2179.8366 | ±4359.6732 | **+8.890** | **6.11e-19** | *** |
| **Education: graduate level (vs college)** | **-816.2970** | 373.8453 | ±747.6906 | **-2.184** | **0.0290** | * |
| Education: high school or below (vs college) | +577.9933 | 858.9147 | ±1717.8294 | +0.673 | 0.5010 |  |
| Site: UCSD (vs UAB) | -352.4134 | 498.9680 | ±997.9359 | -0.706 | 0.4800 |  |
| Site: UW (vs UAB) | -851.5448 | 465.9616 | ±931.9232 | -1.827 | 0.0676 | . |
| **Age (years)** | **-113.0115** | 19.1542 | ±38.3083 | **-5.900** | **3.63e-09** | *** |
| **BMI (kg/m2)** | **-56.0521** | 24.5796 | ±49.1592 | **-2.280** | **0.0226** | * |
| Hypertension | +792.4093 | 456.8321 | ±913.6642 | +1.735 | 0.0828 | . |
| High cholesterol | -422.4641 | 389.5121 | ±779.0243 | -1.085 | 0.2781 |  |
| Kidney disease | -569.8180 | 762.3867 | ±1524.7734 | -0.747 | 0.4548 |  |
| Circulatory disease | -979.6115 | 645.6542 | ±1291.3085 | -1.517 | 0.1292 |  |
| Avg. daily range (mg/dL) | -3.2994 | 18.6530 | ±37.3061 | -0.177 | 0.8596 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **401**, R² = **0.1509**, Adj R² = **0.1269**, F-statistic = **6.29** (p = **1.42e-09**), Residual SE = **3613.045** on **389** df, AIC = **7720.0**, BIC = **7768.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19100.7284** | 1516.0609 | ±3032.1218 | **+12.599** | **2.14e-36** | *** |
| **Education: graduate level (vs college)** | **-812.2124** | 372.3333 | ±744.6667 | **-2.181** | **0.0292** | * |
| Education: high school or below (vs college) | +579.0456 | 865.5825 | ±1731.1650 | +0.669 | 0.5035 |  |
| Site: UCSD (vs UAB) | -348.0528 | 496.9053 | ±993.8105 | -0.700 | 0.4837 |  |
| Site: UW (vs UAB) | -845.5783 | 457.6862 | ±915.3725 | -1.848 | 0.0647 | . |
| **Age (years)** | **-113.0681** | 19.1343 | ±38.2686 | **-5.909** | **3.44e-09** | *** |
| **BMI (kg/m2)** | **-55.6811** | 24.6891 | ±49.3782 | **-2.255** | **0.0241** | * |
| Hypertension | +795.4974 | 453.4651 | ±906.9303 | +1.754 | 0.0794 | . |
| High cholesterol | -420.9792 | 389.5108 | ±779.0216 | -1.081 | 0.2798 |  |
| Kidney disease | -582.1308 | 758.0705 | ±1516.1410 | -0.768 | 0.4425 |  |
| Circulatory disease | -981.1651 | 648.0670 | ±1296.1340 | -1.514 | 0.1300 |  |
| SD of daily means (mg/dL) | +0.1419 | 107.0074 | ±214.0149 | +0.001 | 0.9989 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **401**, R² = **0.1587**, Adj R² = **0.1349**, F-statistic = **6.67** (p = **2.92e-10**), Residual SE = **3596.357** on **389** df, AIC = **7716.3**, BIC = **7764.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+133600.6138** | 59427.8562 | ±118855.7125 | **+2.248** | **0.0246** | * |
| **Education: graduate level (vs college)** | **-775.8487** | 371.6431 | ±743.2863 | **-2.088** | **0.0368** | * |
| Education: high school or below (vs college) | +620.7344 | 859.3958 | ±1718.7916 | +0.722 | 0.4701 |  |
| Site: UCSD (vs UAB) | -295.9307 | 495.1461 | ±990.2922 | -0.598 | 0.5501 |  |
| Site: UW (vs UAB) | -813.1291 | 454.8706 | ±909.7411 | -1.788 | 0.0738 | . |
| **Age (years)** | **-112.0086** | 19.0139 | ±38.0277 | **-5.891** | **3.84e-09** | *** |
| **BMI (kg/m2)** | **-54.6911** | 25.6804 | ±51.3607 | **-2.130** | **0.0332** | * |
| Hypertension | +784.3496 | 448.0556 | ±896.1113 | +1.751 | 0.0800 | . |
| High cholesterol | -429.4102 | 389.3858 | ±778.7716 | -1.103 | 0.2701 |  |
| Kidney disease | -686.3348 | 797.5094 | ±1595.0188 | -0.861 | 0.3895 |  |
| Circulatory disease | -975.4175 | 641.8190 | ±1283.6379 | -1.520 | 0.1286 |  |
| Time in range 70-180, pooled (%) | -1151.5188 | 598.5569 | ±1197.1138 | -1.924 | 0.0544 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **401**, R² = **0.1577**, Adj R² = **0.1339**, F-statistic = **6.62** (p = **3.63e-10**), Residual SE = **3598.625** on **389** df, AIC = **7716.8**, BIC = **7764.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+121810.7804** | 60026.0517 | ±120052.1035 | **+2.029** | **0.0424** | * |
| **Education: graduate level (vs college)** | **-768.5902** | 373.3644 | ±746.7289 | **-2.059** | **0.0395** | * |
| Education: high school or below (vs college) | +627.9809 | 858.8032 | ±1717.6063 | +0.731 | 0.4646 |  |
| Site: UCSD (vs UAB) | -318.3323 | 495.0681 | ±990.1362 | -0.643 | 0.5202 |  |
| Site: UW (vs UAB) | -845.4835 | 453.1142 | ±906.2284 | -1.866 | 0.0620 | . |
| **Age (years)** | **-112.0028** | 19.0260 | ±38.0520 | **-5.887** | **3.94e-09** | *** |
| **BMI (kg/m2)** | **-55.6780** | 24.9104 | ±49.8209 | **-2.235** | **0.0254** | * |
| Hypertension | +828.6250 | 453.8469 | ±907.6937 | +1.826 | 0.0679 | . |
| High cholesterol | -442.5252 | 390.1082 | ±780.2165 | -1.134 | 0.2566 |  |
| Kidney disease | -639.6173 | 786.5672 | ±1573.1345 | -0.813 | 0.4161 |  |
| Circulatory disease | -1004.3856 | 640.2535 | ±1280.5069 | -1.569 | 0.1167 |  |
| Avg. daily time in range 70-180 (%) | -1032.1091 | 604.3881 | ±1208.7762 | -1.708 | 0.0877 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **401**, R² = **0.1510**, Adj R² = **0.1270**, F-statistic = **6.29** (p = **1.40e-09**), Residual SE = **3612.923** on **389** df, AIC = **7720.0**, BIC = **7767.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19077.8958** | 1455.0139 | ±2910.0278 | **+13.112** | **2.82e-39** | *** |
| **Education: graduate level (vs college)** | **-811.5551** | 370.6549 | ±741.3098 | **-2.190** | **0.0286** | * |
| Education: high school or below (vs college) | +583.0088 | 858.4565 | ±1716.9130 | +0.679 | 0.4971 |  |
| Site: UCSD (vs UAB) | -336.6834 | 501.1887 | ±1002.3774 | -0.672 | 0.5017 |  |
| Site: UW (vs UAB) | -839.5041 | 457.5806 | ±915.1612 | -1.835 | 0.0666 | . |
| **Age (years)** | **-113.0003** | 19.0658 | ±38.1317 | **-5.927** | **3.09e-09** | *** |
| **BMI (kg/m2)** | **-55.6815** | 24.6176 | ±49.2351 | **-2.262** | **0.0237** | * |
| Hypertension | +791.8182 | 453.8990 | ±907.7981 | +1.744 | 0.0811 | . |
| High cholesterol | -420.3300 | 389.7867 | ±779.5734 | -1.078 | 0.2809 |  |
| Kidney disease | -573.6825 | 763.5632 | ±1527.1264 | -0.751 | 0.4525 |  |
| Circulatory disease | -984.5085 | 643.7624 | ±1287.5249 | -1.529 | 0.1262 |  |
| Any reading < 54 during wear (0/1) | +77.6735 | 440.3772 | ±880.7544 | +0.176 | 0.8600 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **401**, R² = **0.1560**, Adj R² = **0.1321**, F-statistic = **6.54** (p = **5.12e-10**), Residual SE = **3602.244** on **389** df, AIC = **7717.6**, BIC = **7765.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18940.1113** | 1446.5647 | ±2893.1294 | **+13.093** | **3.60e-39** | *** |
| **Education: graduate level (vs college)** | **-807.9931** | 369.7976 | ±739.5952 | **-2.185** | **0.0289** | * |
| Education: high school or below (vs college) | +652.7703 | 859.8852 | ±1719.7703 | +0.759 | 0.4478 |  |
| Site: UCSD (vs UAB) | -263.9821 | 498.2131 | ±996.4262 | -0.530 | 0.5962 |  |
| Site: UW (vs UAB) | -808.0082 | 455.9219 | ±911.8438 | -1.772 | 0.0764 | . |
| **Age (years)** | **-111.0265** | 18.9563 | ±37.9125 | **-5.857** | **4.71e-09** | *** |
| **BMI (kg/m2)** | **-58.8027** | 24.2102 | ±48.4204 | **-2.429** | **0.0151** | * |
| Hypertension | +737.3744 | 452.3169 | ±904.6338 | +1.630 | 0.1031 |  |
| High cholesterol | -398.5974 | 389.6348 | ±779.2696 | -1.023 | 0.3063 |  |
| Kidney disease | -523.9172 | 761.0841 | ±1522.1683 | -0.688 | 0.4912 |  |
| Circulatory disease | -1029.3565 | 652.4372 | ±1304.8744 | -1.578 | 0.1146 |  |
| Time < 54 (%) | +5028.1461 | 4314.3281 | ±8628.6562 | +1.165 | 0.2438 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **401**, R² = **0.1558**, Adj R² = **0.1319**, F-statistic = **6.53** (p = **5.32e-10**), Residual SE = **3602.652** on **389** df, AIC = **7717.7**, BIC = **7765.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19040.6409** | 1444.4180 | ±2888.8360 | **+13.182** | **1.11e-39** | *** |
| **Education: graduate level (vs college)** | **-813.7213** | 370.1590 | ±740.3179 | **-2.198** | **0.0279** | * |
| Education: high school or below (vs college) | +608.4122 | 856.9782 | ±1713.9564 | +0.710 | 0.4777 |  |
| Site: UCSD (vs UAB) | -314.7492 | 495.1912 | ±990.3824 | -0.636 | 0.5250 |  |
| Site: UW (vs UAB) | -847.7718 | 458.2825 | ±916.5650 | -1.850 | 0.0643 | . |
| **Age (years)** | **-112.4893** | 19.0159 | ±38.0319 | **-5.916** | **3.31e-09** | *** |
| **BMI (kg/m2)** | **-57.1689** | 24.5495 | ±49.0991 | **-2.329** | **0.0199** | * |
| Hypertension | +782.6857 | 452.0221 | ±904.0442 | +1.732 | 0.0834 | . |
| High cholesterol | -415.6809 | 389.0628 | ±778.1257 | -1.068 | 0.2853 |  |
| Kidney disease | -542.7620 | 762.1471 | ±1524.2942 | -0.712 | 0.4764 |  |
| Circulatory disease | -1059.0234 | 654.0814 | ±1308.1627 | -1.619 | 0.1054 |  |
| Avg. daily time < 54 (%) | +6477.0577 | 6181.5890 | ±12363.1779 | +1.048 | 0.2947 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **401**, R² = **0.1509**, Adj R² = **0.1269**, F-statistic = **6.29** (p = **1.42e-09**), Residual SE = **3613.020** on **389** df, AIC = **7720.0**, BIC = **7768.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19088.0517** | 1477.8511 | ±2955.7023 | **+12.916** | **3.65e-38** | *** |
| **Education: graduate level (vs college)** | **-811.3459** | 371.7726 | ±743.5453 | **-2.182** | **0.0291** | * |
| Education: high school or below (vs college) | +576.0881 | 864.4729 | ±1728.9458 | +0.666 | 0.5052 |  |
| Site: UCSD (vs UAB) | -345.9909 | 495.7078 | ±991.4156 | -0.698 | 0.4852 |  |
| Site: UW (vs UAB) | -843.3176 | 459.7280 | ±919.4559 | -1.834 | 0.0666 | . |
| **Age (years)** | **-113.0570** | 19.1195 | ±38.2391 | **-5.913** | **3.36e-09** | *** |
| **BMI (kg/m2)** | **-55.6562** | 24.6497 | ±49.2993 | **-2.258** | **0.0240** | * |
| Hypertension | +797.9438 | 452.9008 | ±905.8015 | +1.762 | 0.0781 | . |
| High cholesterol | -423.6817 | 396.1855 | ±792.3710 | -1.069 | 0.2849 |  |
| Kidney disease | -580.0687 | 760.0674 | ±1520.1348 | -0.763 | 0.4454 |  |
| Circulatory disease | -980.4200 | 643.2379 | ±1286.4758 | -1.524 | 0.1275 |  |
| Time 54-69, pooled (%) | +74.1497 | 953.5028 | ±1907.0057 | +0.078 | 0.9380 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **401**, R² = **0.1511**, Adj R² = **0.1271**, F-statistic = **6.29** (p = **1.38e-09**), Residual SE = **3612.712** on **389** df, AIC = **7720.0**, BIC = **7767.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19137.4833** | 1469.8458 | ±2939.6915 | **+13.020** | **9.41e-39** | *** |
| **Education: graduate level (vs college)** | **-817.9046** | 373.0929 | ±746.1858 | **-2.192** | **0.0284** | * |
| Education: high school or below (vs college) | +589.0735 | 862.7151 | ±1725.4302 | +0.683 | 0.4947 |  |
| Site: UCSD (vs UAB) | -352.1885 | 495.6456 | ±991.2912 | -0.711 | 0.4774 |  |
| Site: UW (vs UAB) | -848.9792 | 458.7847 | ±917.5694 | -1.850 | 0.0642 | . |
| **Age (years)** | **-113.0106** | 19.0906 | ±38.1811 | **-5.920** | **3.23e-09** | *** |
| **BMI (kg/m2)** | **-55.6780** | 24.5739 | ±49.1478 | **-2.266** | **0.0235** | * |
| Hypertension | +779.1709 | 458.6941 | ±917.3882 | +1.699 | 0.0894 | . |
| High cholesterol | -412.4068 | 396.0297 | ±792.0595 | -1.041 | 0.2977 |  |
| Kidney disease | -588.1078 | 759.7688 | ±1519.5377 | -0.774 | 0.4389 |  |
| Circulatory disease | -977.3979 | 645.8491 | ±1291.6983 | -1.513 | 0.1302 |  |
| Avg. daily time 54-69 (%) | -274.7874 | 982.0377 | ±1964.0753 | -0.280 | 0.7796 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **401**, R² = **0.1514**, Adj R² = **0.1274**, F-statistic = **6.31** (p = **1.29e-09**), Residual SE = **3612.010** on **389** df, AIC = **7719.8**, BIC = **7767.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19013.2290** | 1478.2677 | ±2956.5354 | **+12.862** | **7.38e-38** | *** |
| **Education: graduate level (vs college)** | **-807.0876** | 372.0105 | ±744.0211 | **-2.170** | **0.0300** | * |
| Education: high school or below (vs college) | +568.3542 | 863.4215 | ±1726.8430 | +0.658 | 0.5104 |  |
| Site: UCSD (vs UAB) | -329.4288 | 495.7493 | ±991.4986 | -0.665 | 0.5064 |  |
| Site: UW (vs UAB) | -829.8533 | 458.9126 | ±917.8253 | -1.808 | 0.0706 | . |
| **Age (years)** | **-112.8368** | 19.1276 | ±38.2551 | **-5.899** | **3.65e-09** | *** |
| **BMI (kg/m2)** | **-55.8027** | 24.6448 | ±49.2896 | **-2.264** | **0.0236** | * |
| Hypertension | +804.1602 | 452.7826 | ±905.5652 | +1.776 | 0.0757 | . |
| High cholesterol | -434.3135 | 394.6886 | ±789.3772 | -1.100 | 0.2712 |  |
| Kidney disease | -565.8005 | 760.3679 | ±1520.7359 | -0.744 | 0.4568 |  |
| Circulatory disease | -981.2139 | 645.3174 | ±1290.6347 | -1.521 | 0.1284 |  |
| Time < 70 (%) | +415.3355 | 932.6231 | ±1865.2463 | +0.445 | 0.6561 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **401**, R² = **0.1509**, Adj R² = **0.1269**, F-statistic = **6.29** (p = **1.42e-09**), Residual SE = **3613.017** on **389** df, AIC = **7720.0**, BIC = **7768.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19091.2664** | 1467.2293 | ±2934.4587 | **+13.012** | **1.05e-38** | *** |
| **Education: graduate level (vs college)** | **-810.7133** | 374.0660 | ±748.1320 | **-2.167** | **0.0302** | * |
| Education: high school or below (vs college) | +576.7964 | 862.6142 | ±1725.2283 | +0.669 | 0.5037 |  |
| Site: UCSD (vs UAB) | -346.6301 | 495.7843 | ±991.5686 | -0.699 | 0.4845 |  |
| Site: UW (vs UAB) | -844.6984 | 458.3159 | ±916.6318 | -1.843 | 0.0653 | . |
| **Age (years)** | **-113.0770** | 19.0938 | ±38.1876 | **-5.922** | **3.18e-09** | *** |
| **BMI (kg/m2)** | **-55.6976** | 24.6349 | ±49.2699 | **-2.261** | **0.0238** | * |
| Hypertension | +799.7070 | 459.3524 | ±918.7049 | +1.741 | 0.0817 | . |
| High cholesterol | -423.1597 | 395.1551 | ±790.3101 | -1.071 | 0.2842 |  |
| Kidney disease | -580.1144 | 760.0402 | ±1520.0805 | -0.763 | 0.4453 |  |
| Circulatory disease | -982.9577 | 647.2370 | ±1294.4740 | -1.519 | 0.1288 |  |
| Avg. daily time < 70 (%) | +72.1785 | 962.2243 | ±1924.4486 | +0.075 | 0.9402 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **401**, R² = **0.1556**, Adj R² = **0.1317**, F-statistic = **6.51** (p = **5.57e-10**), Residual SE = **3603.140** on **389** df, AIC = **7717.8**, BIC = **7765.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +489099.0439 | 415449.5913 | ±830899.1826 | +1.177 | 0.2391 |  |
| **Education: graduate level (vs college)** | **-808.1648** | 369.9693 | ±739.9386 | **-2.184** | **0.0289** | * |
| Education: high school or below (vs college) | +650.9342 | 859.8454 | ±1719.6909 | +0.757 | 0.4490 |  |
| Site: UCSD (vs UAB) | -263.1727 | 498.9457 | ±997.8913 | -0.527 | 0.5979 |  |
| Site: UW (vs UAB) | -805.4139 | 456.2218 | ±912.4436 | -1.765 | 0.0775 | . |
| **Age (years)** | **-110.8326** | 18.9795 | ±37.9590 | **-5.840** | **5.23e-09** | *** |
| **BMI (kg/m2)** | **-58.2699** | 24.2480 | ±48.4959 | **-2.403** | **0.0163** | * |
| Hypertension | +744.2866 | 451.8445 | ±903.6891 | +1.647 | 0.0995 | . |
| High cholesterol | -401.6299 | 389.6080 | ±779.2160 | -1.031 | 0.3026 |  |
| Kidney disease | -528.4706 | 760.9188 | ±1521.8376 | -0.695 | 0.4874 |  |
| Circulatory disease | -1026.4918 | 652.0686 | ±1304.1372 | -1.574 | 0.1154 |  |
| Time 54-250, pooled (%) | -4701.8495 | 4156.0896 | ±8312.1791 | -1.131 | 0.2579 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **401**, R² = **0.1553**, Adj R² = **0.1314**, F-statistic = **6.50** (p = **5.85e-10**), Residual SE = **3603.653** on **389** df, AIC = **7717.9**, BIC = **7765.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +621597.1703 | 601635.8357 | ±1203271.6714 | +1.033 | 0.3015 |  |
| **Education: graduate level (vs college)** | **-813.4146** | 370.4072 | ±740.8144 | **-2.196** | **0.0281** | * |
| Education: high school or below (vs college) | +610.5498 | 857.0470 | ±1714.0940 | +0.712 | 0.4762 |  |
| Site: UCSD (vs UAB) | -308.2692 | 495.7689 | ±991.5378 | -0.622 | 0.5341 |  |
| Site: UW (vs UAB) | -840.5928 | 458.1122 | ±916.2244 | -1.835 | 0.0665 | . |
| **Age (years)** | **-112.0689** | 19.0272 | ±38.0545 | **-5.890** | **3.86e-09** | *** |
| **BMI (kg/m2)** | **-56.5988** | 24.6199 | ±49.2397 | **-2.299** | **0.0215** | * |
| Hypertension | +788.0062 | 452.1567 | ±904.3134 | +1.743 | 0.0814 | . |
| High cholesterol | -418.3292 | 389.2886 | ±778.5772 | -1.075 | 0.2826 |  |
| Kidney disease | -546.5896 | 762.0080 | ±1524.0161 | -0.717 | 0.4732 |  |
| Circulatory disease | -1053.9707 | 653.8853 | ±1307.7707 | -1.612 | 0.1070 |  |
| Avg. daily time 54-250 (%) | -6026.0377 | 6017.6552 | ±12035.3105 | -1.001 | 0.3166 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **401**, R² = **0.1572**, Adj R² = **0.1333**, F-statistic = **6.60** (p = **4.01e-10**), Residual SE = **3599.683** on **389** df, AIC = **7717.1**, BIC = **7765.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18716.3526** | 1500.4408 | ±3000.8817 | **+12.474** | **1.04e-35** | *** |
| **Education: graduate level (vs college)** | **-790.8230** | 370.1401 | ±740.2801 | **-2.137** | **0.0326** | * |
| Education: high school or below (vs college) | +647.2725 | 856.6858 | ±1713.3715 | +0.756 | 0.4499 |  |
| Site: UCSD (vs UAB) | -349.1387 | 494.5726 | ±989.1451 | -0.706 | 0.4802 |  |
| Site: UW (vs UAB) | -857.4955 | 453.4844 | ±906.9688 | -1.891 | 0.0586 | . |
| **Age (years)** | **-112.7424** | 19.0514 | ±38.1029 | **-5.918** | **3.26e-09** | *** |
| **BMI (kg/m2)** | **-54.4772** | 25.6472 | ±51.2943 | **-2.124** | **0.0337** | * |
| Hypertension | +760.9780 | 446.9573 | ±893.9146 | +1.703 | 0.0886 | . |
| High cholesterol | -393.0546 | 388.9976 | ±777.9952 | -1.010 | 0.3123 |  |
| Kidney disease | -726.1030 | 806.1166 | ±1612.2331 | -0.901 | 0.3677 |  |
| Circulatory disease | -975.2885 | 639.2231 | ±1278.4461 | -1.526 | 0.1271 |  |
| Time 181-250, pooled (%) | +1110.6310 | 668.8404 | ±1337.6807 | +1.661 | 0.0968 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **401**, R² = **0.1587**, Adj R² = **0.1349**, F-statistic = **6.67** (p = **2.97e-10**), Residual SE = **3596.543** on **389** df, AIC = **7716.4**, BIC = **7764.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18693.7474** | 1478.0890 | ±2956.1781 | **+12.647** | **1.16e-36** | *** |
| **Education: graduate level (vs college)** | **-785.9559** | 369.9662 | ±739.9324 | **-2.124** | **0.0336** | * |
| Education: high school or below (vs college) | +674.0882 | 856.4493 | ±1712.8987 | +0.787 | 0.4312 |  |
| Site: UCSD (vs UAB) | -339.2838 | 494.5095 | ±989.0190 | -0.686 | 0.4926 |  |
| Site: UW (vs UAB) | -861.4895 | 452.3940 | ±904.7880 | -1.904 | 0.0569 | . |
| **Age (years)** | **-111.7654** | 19.0445 | ±38.0891 | **-5.869** | **4.39e-09** | *** |
| **BMI (kg/m2)** | **-55.4824** | 24.8246 | ±49.6492 | **-2.235** | **0.0254** | * |
| Hypertension | +763.7092 | 446.4831 | ±892.9663 | +1.710 | 0.0872 | . |
| High cholesterol | -409.0603 | 388.1647 | ±776.3295 | -1.054 | 0.2920 |  |
| Kidney disease | -683.0541 | 794.9912 | ±1589.9824 | -0.859 | 0.3902 |  |
| Circulatory disease | -977.4040 | 637.2678 | ±1274.5356 | -1.534 | 0.1251 |  |
| Avg. daily time 181-250 (%) | +1210.5512 | 663.2355 | ±1326.4709 | +1.825 | 0.0680 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **401**, R² = **0.1571**, Adj R² = **0.1333**, F-statistic = **6.59** (p = **4.07e-10**), Residual SE = **3599.828** on **389** df, AIC = **7717.1**, BIC = **7765.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18710.6284** | 1502.1901 | ±3004.3803 | **+12.456** | **1.30e-35** | *** |
| **Education: graduate level (vs college)** | **-790.9565** | 370.1712 | ±740.3424 | **-2.137** | **0.0326** | * |
| Education: high school or below (vs college) | +647.4617 | 856.6974 | ±1713.3948 | +0.756 | 0.4498 |  |
| Site: UCSD (vs UAB) | -347.6615 | 494.6294 | ±989.2588 | -0.703 | 0.4821 |  |
| Site: UW (vs UAB) | -856.2280 | 453.5679 | ±907.1358 | -1.888 | 0.0591 | . |
| **Age (years)** | **-112.6682** | 19.0541 | ±38.1082 | **-5.913** | **3.36e-09** | *** |
| **BMI (kg/m2)** | **-54.4087** | 25.6536 | ±51.3071 | **-2.121** | **0.0339** | * |
| Hypertension | +761.9677 | 447.0148 | ±894.0295 | +1.705 | 0.0883 | . |
| High cholesterol | -393.6305 | 389.0112 | ±778.0223 | -1.012 | 0.3116 |  |
| Kidney disease | -725.2263 | 805.8678 | ±1611.7356 | -0.900 | 0.3682 |  |
| Circulatory disease | -975.3937 | 639.2849 | ±1278.5698 | -1.526 | 0.1271 |  |
| Time > 180 (%) | +1102.4641 | 666.4012 | ±1332.8024 | +1.654 | 0.0981 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **401**, R² = **0.1586**, Adj R² = **0.1348**, F-statistic = **6.66** (p = **3.03e-10**), Residual SE = **3596.742** on **389** df, AIC = **7716.4**, BIC = **7764.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18687.0379** | 1480.0788 | ±2960.1577 | **+12.626** | **1.52e-36** | *** |
| **Education: graduate level (vs college)** | **-786.1439** | 370.0041 | ±740.0081 | **-2.125** | **0.0336** | * |
| Education: high school or below (vs college) | +674.0953 | 856.4624 | ±1712.9248 | +0.787 | 0.4312 |  |
| Site: UCSD (vs UAB) | -337.6075 | 494.5501 | ±989.1003 | -0.683 | 0.4948 |  |
| Site: UW (vs UAB) | -859.9521 | 452.4877 | ±904.9754 | -1.900 | 0.0574 | . |
| **Age (years)** | **-111.6850** | 19.0510 | ±38.1021 | **-5.862** | **4.56e-09** | *** |
| **BMI (kg/m2)** | **-55.3912** | 24.8343 | ±49.6686 | **-2.230** | **0.0257** | * |
| Hypertension | +764.8669 | 446.5700 | ±893.1399 | +1.713 | 0.0868 | . |
| High cholesterol | -409.6178 | 388.2044 | ±776.4087 | -1.055 | 0.2914 |  |
| Kidney disease | -682.3938 | 794.7392 | ±1589.4785 | -0.859 | 0.3905 |  |
| Circulatory disease | -977.5104 | 637.3538 | ±1274.7076 | -1.534 | 0.1251 |  |
| Avg. daily time > 180 (%) | +1200.0358 | 659.9183 | ±1319.8366 | +1.818 | 0.0690 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 401)
**Regression Call / Formula**: `steps_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **401**, R² = **0.1661**, Adj R² = **0.1425**, F-statistic = **7.04** (p = **6.49e-11**), Residual SE = **3580.674** on **389** df, AIC = **7712.8**, BIC = **7760.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18668.2938** | 1488.8503 | ±2977.7006 | **+12.539** | **4.58e-36** | *** |
| Education: graduate level (vs college) | -739.7890 | 378.3184 | ±756.6367 | -1.955 | 0.0505 | . |
| Education: high school or below (vs college) | +593.6335 | 842.6476 | ±1685.2951 | +0.704 | 0.4811 |  |
| Site: UCSD (vs UAB) | -393.7234 | 489.0143 | ±978.0286 | -0.805 | 0.4207 |  |
| **Site: UW (vs UAB)** | **-907.0915** | 442.1234 | ±884.2467 | **-2.052** | **0.0402** | * |
| **Age (years)** | **-105.2058** | 20.3606 | ±40.7211 | **-5.167** | **2.38e-07** | *** |
| **BMI (kg/m2)** | **-60.5997** | 23.8158 | ±47.6316 | **-2.545** | **0.0109** | * |
| Hypertension | +692.0867 | 425.9979 | ±851.9957 | +1.625 | 0.1042 |  |
| High cholesterol | -454.5851 | 391.0667 | ±782.1333 | -1.162 | 0.2451 |  |
| Kidney disease | -655.0001 | 795.4809 | ±1590.9617 | -0.823 | 0.4103 |  |
| Circulatory disease | -910.6137 | 651.0573 | ±1302.1147 | -1.399 | 0.1619 |  |
| Nocturnal time > 180 (%) | +1304.9622 | 922.5774 | ±1845.1548 | +1.414 | 0.1572 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Brisk-cadence minutes per day (>= 100 steps/min)  (domain: Wearable activity; outcome sample N = 401; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **401**, R² = **0.1728**, Adj R² = **0.1516**, F-statistic = **8.15** (p = **5.40e-12**), Residual SE = **11.595** on **390** df, AIC = **3114.2**, BIC = **3158.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.8490** | 4.6965 | ±9.3930 | **+11.040** | **2.45e-28** | *** |
| Education: graduate level (vs college) | -2.3269 | 1.1940 | ±2.3879 | -1.949 | 0.0513 | . |
| Education: high school or below (vs college) | +1.5104 | 2.6985 | ±5.3970 | +0.560 | 0.5757 |  |
| Site: UCSD (vs UAB) | -1.6998 | 1.5772 | ±3.1544 | -1.078 | 0.2811 |  |
| Site: UW (vs UAB) | -2.8682 | 1.4851 | ±2.9702 | -1.931 | 0.0534 | . |
| **Age (years)** | **-0.4123** | 0.0567 | ±0.1134 | **-7.271** | **3.57e-13** | *** |
| BMI (kg/m2) | -0.0107 | 0.0836 | ±0.1671 | -0.128 | 0.8984 |  |
| Hypertension | +1.8324 | 1.3874 | ±2.7747 | +1.321 | 0.1866 |  |
| High cholesterol | -0.7472 | 1.2253 | ±2.4505 | -0.610 | 0.5420 |  |
| Kidney disease | -1.4715 | 2.3974 | ±4.7947 | -0.614 | 0.5393 |  |
| Circulatory disease | -2.7913 | 1.9547 | ±3.9094 | -1.428 | 0.1533 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **401**, R² = **0.1740**, Adj R² = **0.1506**, F-statistic = **7.45** (p = **1.25e-11**), Residual SE = **11.602** on **389** df, AIC = **3115.6**, BIC = **3163.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.1148** | 11.6776 | ±23.3553 | **+3.778** | **1.58e-04** | *** |
| Education: graduate level (vs college) | -2.2805 | 1.1957 | ±2.3914 | -1.907 | 0.0565 | . |
| Education: high school or below (vs college) | +1.4227 | 2.6962 | ±5.3925 | +0.528 | 0.5977 |  |
| Site: UCSD (vs UAB) | -1.6343 | 1.5725 | ±3.1451 | -1.039 | 0.2987 |  |
| Site: UW (vs UAB) | -2.7935 | 1.4838 | ±2.9677 | -1.883 | 0.0597 | . |
| **Age (years)** | **-0.4166** | 0.0572 | ±0.1144 | **-7.282** | **3.28e-13** | *** |
| BMI (kg/m2) | -0.0177 | 0.0824 | ±0.1648 | -0.215 | 0.8296 |  |
| Hypertension | +1.7501 | 1.3912 | ±2.7824 | +1.258 | 0.2084 |  |
| High cholesterol | -0.9705 | 1.2592 | ±2.5183 | -0.771 | 0.4408 |  |
| Kidney disease | -1.3462 | 2.4099 | ±4.8197 | -0.559 | 0.5764 |  |
| Circulatory disease | -2.7352 | 1.9681 | ±3.9362 | -1.390 | 0.1646 |  |
| HbA1c (%) | +1.4891 | 2.0406 | ±4.0812 | +0.730 | 0.4656 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **401**, R² = **0.1728**, Adj R² = **0.1494**, F-statistic = **7.39** (p = **1.60e-11**), Residual SE = **11.610** on **389** df, AIC = **3116.2**, BIC = **3164.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.1707** | 10.6550 | ±21.3099 | **+4.803** | **1.57e-06** | *** |
| Education: graduate level (vs college) | -2.3239 | 1.1955 | ±2.3909 | -1.944 | 0.0519 | . |
| Education: high school or below (vs college) | +1.5188 | 2.6955 | ±5.3910 | +0.563 | 0.5731 |  |
| Site: UCSD (vs UAB) | -1.7053 | 1.5892 | ±3.1785 | -1.073 | 0.2833 |  |
| Site: UW (vs UAB) | -2.8744 | 1.4982 | ±2.9963 | -1.919 | 0.0550 | . |
| **Age (years)** | **-0.4121** | 0.0567 | ±0.1135 | **-7.264** | **3.77e-13** | *** |
| BMI (kg/m2) | -0.0111 | 0.0839 | ±0.1679 | -0.132 | 0.8948 |  |
| Hypertension | +1.8245 | 1.3914 | ±2.7828 | +1.311 | 0.1898 |  |
| High cholesterol | -0.7441 | 1.2367 | ±2.4734 | -0.602 | 0.5474 |  |
| Kidney disease | -1.4719 | 2.4085 | ±4.8169 | -0.611 | 0.5411 |  |
| Circulatory disease | -2.7935 | 1.9610 | ±3.9219 | -1.425 | 0.1543 |  |
| Mean glucose (mg/dL) | +0.0060 | 0.0864 | ±0.1728 | +0.069 | 0.9447 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **401**, R² = **0.1728**, Adj R² = **0.1494**, F-statistic = **7.39** (p = **1.60e-11**), Residual SE = **11.610** on **389** df, AIC = **3116.2**, BIC = **3164.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3419** | 22.0223 | ±44.0446 | **+2.286** | **0.0223** | * |
| Education: graduate level (vs college) | -2.3239 | 1.1955 | ±2.3909 | -1.944 | 0.0519 | . |
| Education: high school or below (vs college) | +1.5188 | 2.6955 | ±5.3910 | +0.563 | 0.5731 |  |
| Site: UCSD (vs UAB) | -1.7053 | 1.5892 | ±3.1785 | -1.073 | 0.2833 |  |
| Site: UW (vs UAB) | -2.8744 | 1.4982 | ±2.9963 | -1.919 | 0.0550 | . |
| **Age (years)** | **-0.4121** | 0.0567 | ±0.1135 | **-7.264** | **3.77e-13** | *** |
| BMI (kg/m2) | -0.0111 | 0.0839 | ±0.1679 | -0.132 | 0.8948 |  |
| Hypertension | +1.8245 | 1.3914 | ±2.7828 | +1.311 | 0.1898 |  |
| High cholesterol | -0.7441 | 1.2367 | ±2.4734 | -0.602 | 0.5474 |  |
| Kidney disease | -1.4719 | 2.4085 | ±4.8169 | -0.611 | 0.5411 |  |
| Circulatory disease | -2.7935 | 1.9610 | ±3.9219 | -1.425 | 0.1543 |  |
| GMI (%) | +0.2504 | 3.6113 | ±7.2226 | +0.069 | 0.9447 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **401**, R² = **0.1744**, Adj R² = **0.1511**, F-statistic = **7.47** (p = **1.13e-11**), Residual SE = **11.598** on **389** df, AIC = **3115.4**, BIC = **3163.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+45.4474** | 8.6205 | ±17.2409 | **+5.272** | **1.35e-07** | *** |
| Education: graduate level (vs college) | -2.2613 | 1.1968 | ±2.3936 | -1.889 | 0.0588 | . |
| Education: high school or below (vs college) | +1.5998 | 2.7006 | ±5.4013 | +0.592 | 0.5536 |  |
| Site: UCSD (vs UAB) | -1.8368 | 1.5843 | ±3.1687 | -1.159 | 0.2463 |  |
| **Site: UW (vs UAB)** | **-2.9741** | 1.4908 | ±2.9816 | **-1.995** | **0.0460** | * |
| **Age (years)** | **-0.4042** | 0.0571 | ±0.1142 | **-7.079** | **1.45e-12** | *** |
| BMI (kg/m2) | -0.0220 | 0.0831 | ±0.1662 | -0.265 | 0.7912 |  |
| Hypertension | +1.7361 | 1.3803 | ±2.7607 | +1.258 | 0.2085 |  |
| High cholesterol | -0.7421 | 1.2267 | ±2.4535 | -0.605 | 0.5452 |  |
| Kidney disease | -1.3538 | 2.4316 | ±4.8632 | -0.557 | 0.5777 |  |
| Circulatory disease | -2.7671 | 1.9641 | ±3.9283 | -1.409 | 0.1589 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0550 | 0.0640 | ±0.1280 | +0.859 | 0.3904 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **401**, R² = **0.1729**, Adj R² = **0.1495**, F-statistic = **7.39** (p = **1.57e-11**), Residual SE = **11.609** on **389** df, AIC = **3116.2**, BIC = **3164.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.7804** | 6.1423 | ±12.2846 | **+8.593** | **8.48e-18** | *** |
| **Education: graduate level (vs college)** | **-2.3507** | 1.1946 | ±2.3892 | **-1.968** | **0.0491** | * |
| Education: high school or below (vs college) | +1.4971 | 2.7024 | ±5.4048 | +0.554 | 0.5796 |  |
| Site: UCSD (vs UAB) | -1.7192 | 1.5783 | ±3.1566 | -1.089 | 0.2760 |  |
| Site: UW (vs UAB) | -2.8920 | 1.4983 | ±2.9965 | -1.930 | 0.0536 | . |
| **Age (years)** | **-0.4120** | 0.0570 | ±0.1140 | **-7.229** | **4.86e-13** | *** |
| BMI (kg/m2) | -0.0098 | 0.0841 | ±0.1683 | -0.117 | 0.9068 |  |
| Hypertension | +1.8514 | 1.3816 | ±2.7632 | +1.340 | 0.1802 |  |
| High cholesterol | -0.7670 | 1.2394 | ±2.4789 | -0.619 | 0.5360 |  |
| Kidney disease | -1.4066 | 2.4177 | ±4.8354 | -0.582 | 0.5607 |  |
| Circulatory disease | -2.7785 | 1.9597 | ±3.9194 | -1.418 | 0.1562 |  |
| Glucose SD, pooled (mg/dL) | -0.0564 | 0.2597 | ±0.5193 | -0.217 | 0.8279 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **401**, R² = **0.1735**, Adj R² = **0.1501**, F-statistic = **7.42** (p = **1.38e-11**), Residual SE = **11.605** on **389** df, AIC = **3115.9**, BIC = **3163.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.9780** | 5.7893 | ±11.5785 | **+9.324** | **1.12e-20** | *** |
| **Education: graduate level (vs college)** | **-2.3944** | 1.1995 | ±2.3989 | **-1.996** | **0.0459** | * |
| Education: high school or below (vs college) | +1.4603 | 2.7043 | ±5.4087 | +0.540 | 0.5892 |  |
| Site: UCSD (vs UAB) | -1.7435 | 1.5764 | ±3.1528 | -1.106 | 0.2687 |  |
| Site: UW (vs UAB) | -2.9261 | 1.4965 | ±2.9931 | -1.955 | 0.0506 | . |
| **Age (years)** | **-0.4113** | 0.0571 | ±0.1142 | **-7.201** | **5.98e-13** | *** |
| BMI (kg/m2) | -0.0076 | 0.0845 | ±0.1689 | -0.090 | 0.9285 |  |
| Hypertension | +1.8613 | 1.3841 | ±2.7681 | +1.345 | 0.1787 |  |
| High cholesterol | -0.7930 | 1.2359 | ±2.4719 | -0.642 | 0.5211 |  |
| Kidney disease | -1.3136 | 2.4014 | ±4.8028 | -0.547 | 0.5844 |  |
| Circulatory disease | -2.7848 | 1.9670 | ±3.9339 | -1.416 | 0.1568 |  |
| Avg. daily SD (mg/dL) | -0.1432 | 0.2483 | ±0.4965 | -0.577 | 0.5642 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **401**, R² = **0.1731**, Adj R² = **0.1497**, F-statistic = **7.40** (p = **1.50e-11**), Residual SE = **11.608** on **389** df, AIC = **3116.1**, BIC = **3164.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.3819** | 5.9485 | ±11.8970 | **+8.974** | **2.86e-19** | *** |
| **Education: graduate level (vs college)** | **-2.3596** | 1.1967 | ±2.3935 | **-1.972** | **0.0486** | * |
| Education: high school or below (vs college) | +1.5061 | 2.7080 | ±5.4159 | +0.556 | 0.5781 |  |
| Site: UCSD (vs UAB) | -1.7430 | 1.5804 | ±3.1607 | -1.103 | 0.2701 |  |
| Site: UW (vs UAB) | -2.9207 | 1.5056 | ±3.0112 | -1.940 | 0.0524 | . |
| **Age (years)** | **-0.4115** | 0.0570 | ±0.1140 | **-7.218** | **5.27e-13** | *** |
| BMI (kg/m2) | -0.0103 | 0.0837 | ±0.1675 | -0.123 | 0.9021 |  |
| Hypertension | +1.8450 | 1.3873 | ±2.7747 | +1.330 | 0.1835 |  |
| High cholesterol | -0.7740 | 1.2303 | ±2.4606 | -0.629 | 0.5293 |  |
| Kidney disease | -1.3677 | 2.4099 | ±4.8199 | -0.568 | 0.5704 |  |
| Circulatory disease | -2.7739 | 1.9620 | ±3.9239 | -1.414 | 0.1574 |  |
| CV (%) | -0.1046 | 0.2607 | ±0.5214 | -0.401 | 0.6881 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **401**, R² = **0.1731**, Adj R² = **0.1497**, F-statistic = **7.40** (p = **1.51e-11**), Residual SE = **11.608** on **389** df, AIC = **3116.1**, BIC = **3164.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.4058** | 6.1173 | ±12.2346 | **+8.240** | **1.72e-16** | *** |
| **Education: graduate level (vs college)** | **-2.3626** | 1.1971 | ±2.3942 | **-1.974** | **0.0484** | * |
| Education: high school or below (vs college) | +1.5139 | 2.7087 | ±5.4173 | +0.559 | 0.5762 |  |
| Site: UCSD (vs UAB) | -1.7365 | 1.5788 | ±3.1575 | -1.100 | 0.2714 |  |
| Site: UW (vs UAB) | -2.9138 | 1.5030 | ±3.0059 | -1.939 | 0.0525 | . |
| **Age (years)** | **-0.4116** | 0.0570 | ±0.1139 | **-7.225** | **5.02e-13** | *** |
| BMI (kg/m2) | -0.0104 | 0.0837 | ±0.1673 | -0.124 | 0.9014 |  |
| Hypertension | +1.8440 | 1.3871 | ±2.7741 | +1.329 | 0.1837 |  |
| High cholesterol | -0.7758 | 1.2312 | ±2.4624 | -0.630 | 0.5286 |  |
| Kidney disease | -1.3948 | 2.4006 | ±4.8012 | -0.581 | 0.5612 |  |
| Circulatory disease | -2.7832 | 1.9620 | ±3.9240 | -1.419 | 0.1560 |  |
| Mean / SD ratio | +0.2079 | 0.5319 | ±1.0639 | +0.391 | 0.6959 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **401**, R² = **0.1738**, Adj R² = **0.1504**, F-statistic = **7.44** (p = **1.29e-11**), Residual SE = **11.603** on **389** df, AIC = **3115.7**, BIC = **3163.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+49.4293** | 5.8394 | ±11.6788 | **+8.465** | **2.57e-17** | *** |
| **Education: graduate level (vs college)** | **-2.3986** | 1.1996 | ±2.3993 | **-1.999** | **0.0456** | * |
| Education: high school or below (vs college) | +1.5071 | 2.7134 | ±5.4268 | +0.555 | 0.5786 |  |
| Site: UCSD (vs UAB) | -1.7585 | 1.5742 | ±3.1485 | -1.117 | 0.2640 |  |
| **Site: UW (vs UAB)** | **-2.9497** | 1.4967 | ±2.9934 | **-1.971** | **0.0488** | * |
| **Age (years)** | **-0.4106** | 0.0571 | ±0.1142 | **-7.189** | **6.54e-13** | *** |
| BMI (kg/m2) | -0.0087 | 0.0839 | ±0.1677 | -0.104 | 0.9169 |  |
| Hypertension | +1.8349 | 1.3899 | ±2.7798 | +1.320 | 0.1868 |  |
| High cholesterol | -0.7850 | 1.2285 | ±2.4570 | -0.639 | 0.5228 |  |
| Kidney disease | -1.3267 | 2.3996 | ±4.7993 | -0.553 | 0.5803 |  |
| Circulatory disease | -2.8189 | 1.9706 | ±3.9412 | -1.430 | 0.1526 |  |
| Avg. daily mean/SD | +0.3002 | 0.3900 | ±0.7799 | +0.770 | 0.4415 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **401**, R² = **0.1805**, Adj R² = **0.1574**, F-statistic = **7.79** (p = **3.10e-12**), Residual SE = **11.555** on **389** df, AIC = **3112.4**, BIC = **3160.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.4446** | 5.8474 | ±11.6949 | **+7.601** | **2.95e-14** | *** |
| Education: graduate level (vs college) | -2.3022 | 1.1943 | ±2.3886 | -1.928 | 0.0539 | . |
| Education: high school or below (vs college) | +1.2044 | 2.6653 | ±5.3305 | +0.452 | 0.6513 |  |
| Site: UCSD (vs UAB) | -1.5804 | 1.5669 | ±3.1339 | -1.009 | 0.3132 |  |
| Site: UW (vs UAB) | -2.5847 | 1.4851 | ±2.9702 | -1.740 | 0.0818 | . |
| **Age (years)** | **-0.4026** | 0.0559 | ±0.1118 | **-7.202** | **5.94e-13** | *** |
| BMI (kg/m2) | -0.0034 | 0.0828 | ±0.1657 | -0.041 | 0.9671 |  |
| Hypertension | +1.9305 | 1.3834 | ±2.7668 | +1.395 | 0.1629 |  |
| High cholesterol | -0.8228 | 1.2250 | ±2.4500 | -0.672 | 0.5018 |  |
| Kidney disease | -1.8570 | 2.3865 | ±4.7729 | -0.778 | 0.4365 |  |
| Circulatory disease | -2.7493 | 1.9503 | ±3.9005 | -1.410 | 0.1586 |  |
| MAG (mg/dL/h) | +0.1907 | 0.1055 | ±0.2110 | +1.808 | 0.0706 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **401**, R² = **0.1728**, Adj R² = **0.1494**, F-statistic = **7.39** (p = **1.60e-11**), Residual SE = **11.610** on **389** df, AIC = **3116.2**, BIC = **3164.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.7028** | 6.4218 | ±12.8435 | **+8.051** | **8.20e-16** | *** |
| Education: graduate level (vs college) | -2.3247 | 1.2001 | ±2.4001 | -1.937 | 0.0527 | . |
| Education: high school or below (vs college) | +1.5110 | 2.7040 | ±5.4080 | +0.559 | 0.5763 |  |
| Site: UCSD (vs UAB) | -1.6976 | 1.5764 | ±3.1527 | -1.077 | 0.2815 |  |
| Site: UW (vs UAB) | -2.8651 | 1.4977 | ±2.9955 | -1.913 | 0.0558 | . |
| **Age (years)** | **-0.4123** | 0.0570 | ±0.1139 | **-7.237** | **4.58e-13** | *** |
| BMI (kg/m2) | -0.0105 | 0.0838 | ±0.1676 | -0.125 | 0.9005 |  |
| Hypertension | +1.8341 | 1.3985 | ±2.7970 | +1.311 | 0.1897 |  |
| High cholesterol | -0.7464 | 1.2313 | ±2.4627 | -0.606 | 0.5444 |  |
| Kidney disease | -1.4780 | 2.4031 | ±4.8062 | -0.615 | 0.5385 |  |
| Circulatory disease | -2.7921 | 1.9567 | ±3.9134 | -1.427 | 0.1536 |  |
| Avg. daily range (mg/dL) | +0.0017 | 0.0564 | ±0.1127 | +0.031 | 0.9754 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **401**, R² = **0.1742**, Adj R² = **0.1509**, F-statistic = **7.46** (p = **1.18e-11**), Residual SE = **11.600** on **389** df, AIC = **3115.5**, BIC = **3163.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.6068** | 4.9629 | ±9.9259 | **+10.197** | **2.05e-24** | *** |
| **Education: graduate level (vs college)** | **-2.3568** | 1.2010 | ±2.4020 | **-1.962** | **0.0497** | * |
| Education: high school or below (vs college) | +1.4274 | 2.7289 | ±5.4579 | +0.523 | 0.6009 |  |
| Site: UCSD (vs UAB) | -1.6497 | 1.5754 | ±3.1508 | -1.047 | 0.2950 |  |
| Site: UW (vs UAB) | -2.8841 | 1.4854 | ±2.9709 | -1.942 | 0.0522 | . |
| **Age (years)** | **-0.4120** | 0.0569 | ±0.1138 | **-7.243** | **4.37e-13** | *** |
| BMI (kg/m2) | -0.0118 | 0.0838 | ±0.1677 | -0.141 | 0.8881 |  |
| Hypertension | +1.7403 | 1.3942 | ±2.7884 | +1.248 | 0.2119 |  |
| High cholesterol | -0.7647 | 1.2252 | ±2.4503 | -0.624 | 0.5325 |  |
| Kidney disease | -1.4826 | 2.4027 | ±4.8053 | -0.617 | 0.5372 |  |
| Circulatory disease | -2.8843 | 1.9706 | ±3.9412 | -1.464 | 0.1433 |  |
| SD of daily means (mg/dL) | +0.2559 | 0.3566 | ±0.7133 | +0.718 | 0.4730 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **401**, R² = **0.1893**, Adj R² = **0.1664**, F-statistic = **8.26** (p = **4.67e-13**), Residual SE = **11.493** on **389** df, AIC = **3108.1**, BIC = **3156.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+594.3739** | 186.8112 | ±373.6224 | **+3.182** | **0.0015** | ** |
| Education: graduate level (vs college) | -2.1546 | 1.1933 | ±2.3867 | -1.806 | 0.0710 | . |
| Education: high school or below (vs college) | +1.7077 | 2.6471 | ±5.2943 | +0.645 | 0.5188 |  |
| Site: UCSD (vs UAB) | -1.4528 | 1.5587 | ±3.1173 | -0.932 | 0.3513 |  |
| Site: UW (vs UAB) | -2.7145 | 1.4618 | ±2.9236 | -1.857 | 0.0633 | . |
| **Age (years)** | **-0.4073** | 0.0560 | ±0.1121 | **-7.269** | **3.63e-13** | *** |
| BMI (kg/m2) | -0.0060 | 0.0904 | ±0.1809 | -0.066 | 0.9472 |  |
| Hypertension | +1.7794 | 1.3716 | ±2.7433 | +1.297 | 0.1945 |  |
| High cholesterol | -0.7872 | 1.2207 | ±2.4414 | -0.645 | 0.5190 |  |
| Kidney disease | -1.9653 | 2.4871 | ±4.9741 | -0.790 | 0.4294 |  |
| Circulatory disease | -2.7643 | 1.9249 | ±3.8497 | -1.436 | 0.1510 |  |
| **Time in range 70-180, pooled (%)** | **-5.4562** | 1.8760 | ±3.7520 | **-2.908** | **0.0036** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **401**, R² = **0.1875**, Adj R² = **0.1645**, F-statistic = **8.16** (p = **6.98e-13**), Residual SE = **11.506** on **389** df, AIC = **3109.0**, BIC = **3156.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+545.0446** | 181.5752 | ±363.1504 | **+3.002** | **0.0027** | ** |
| Education: graduate level (vs college) | -2.1175 | 1.1912 | ±2.3825 | -1.778 | 0.0755 | . |
| Education: high school or below (vs college) | +1.7452 | 2.6557 | ±5.3114 | +0.657 | 0.5111 |  |
| Site: UCSD (vs UAB) | -1.5570 | 1.5580 | ±3.1160 | -0.999 | 0.3176 |  |
| **Site: UW (vs UAB)** | **-2.8678** | 1.4627 | ±2.9253 | **-1.961** | **0.0499** | * |
| **Age (years)** | **-0.4072** | 0.0557 | ±0.1115 | **-7.305** | **2.76e-13** | *** |
| BMI (kg/m2) | -0.0107 | 0.0852 | ±0.1703 | -0.125 | 0.9004 |  |
| Hypertension | +1.9912 | 1.3832 | ±2.7663 | +1.440 | 0.1500 |  |
| High cholesterol | -0.8507 | 1.2178 | ±2.4356 | -0.699 | 0.4848 |  |
| Kidney disease | -1.7476 | 2.4615 | ±4.9231 | -0.710 | 0.4777 |  |
| Circulatory disease | -2.9030 | 1.9161 | ±3.8321 | -1.515 | 0.1297 |  |
| **Avg. daily time in range 70-180 (%)** | **-4.9560** | 1.8203 | ±3.6406 | **-2.723** | **0.0065** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **401**, R² = **0.1731**, Adj R² = **0.1497**, F-statistic = **7.40** (p = **1.49e-11**), Residual SE = **11.608** on **389** df, AIC = **3116.0**, BIC = **3164.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6570** | 4.7498 | ±9.4996 | **+10.876** | **1.51e-27** | *** |
| Education: graduate level (vs college) | -2.3216 | 1.1982 | ±2.3965 | -1.938 | 0.0527 | . |
| Education: high school or below (vs college) | +1.5424 | 2.7069 | ±5.4138 | +0.570 | 0.5688 |  |
| Site: UCSD (vs UAB) | -1.6068 | 1.5888 | ±3.1775 | -1.011 | 0.3118 |  |
| Site: UW (vs UAB) | -2.8187 | 1.4899 | ±2.9798 | -1.892 | 0.0585 | . |
| **Age (years)** | **-0.4118** | 0.0568 | ±0.1136 | **-7.251** | **4.14e-13** | *** |
| BMI (kg/m2) | -0.0107 | 0.0836 | ±0.1673 | -0.128 | 0.8984 |  |
| Hypertension | +1.8020 | 1.3975 | ±2.7950 | +1.289 | 0.1972 |  |
| High cholesterol | -0.7420 | 1.2285 | ±2.4570 | -0.604 | 0.5459 |  |
| Kidney disease | -1.4026 | 2.4160 | ±4.8320 | -0.581 | 0.5615 |  |
| Circulatory disease | -2.8190 | 1.9642 | ±3.9283 | -1.435 | 0.1512 |  |
| Any reading < 54 during wear (0/1) | +0.6340 | 1.4860 | ±2.9720 | +0.427 | 0.6696 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **401**, R² = **0.1797**, Adj R² = **0.1566**, F-statistic = **7.75** (p = **3.67e-12**), Residual SE = **11.561** on **389** df, AIC = **3112.8**, BIC = **3160.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.2328** | 4.6963 | ±9.3926 | **+10.909** | **1.04e-27** | *** |
| Education: graduate level (vs college) | -2.3108 | 1.1939 | ±2.3878 | -1.936 | 0.0529 | . |
| Education: high school or below (vs college) | +1.7919 | 2.7046 | ±5.4092 | +0.663 | 0.5076 |  |
| Site: UCSD (vs UAB) | -1.3786 | 1.5842 | ±3.1685 | -0.870 | 0.3842 |  |
| Site: UW (vs UAB) | -2.7247 | 1.4806 | ±2.9613 | -1.840 | 0.0657 | . |
| **Age (years)** | **-0.4045** | 0.0563 | ±0.1126 | **-7.185** | **6.71e-13** | *** |
| BMI (kg/m2) | -0.0226 | 0.0812 | ±0.1624 | -0.278 | 0.7807 |  |
| Hypertension | +1.6102 | 1.3921 | ±2.7843 | +1.157 | 0.2474 |  |
| High cholesterol | -0.6617 | 1.2240 | ±2.4481 | -0.541 | 0.5888 |  |
| Kidney disease | -1.2492 | 2.4128 | ±4.8257 | -0.518 | 0.6047 |  |
| Circulatory disease | -2.9755 | 2.0001 | ±4.0003 | -1.488 | 0.1368 |  |
| Time < 54 (%) | +19.2074 | 13.8891 | ±27.7781 | +1.383 | 0.1667 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **401**, R² = **0.1794**, Adj R² = **0.1562**, F-statistic = **7.73** (p = **3.92e-12**), Residual SE = **11.563** on **389** df, AIC = **3113.0**, BIC = **3160.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6176** | 4.6898 | ±9.3796 | **+11.006** | **3.56e-28** | *** |
| Education: graduate level (vs college) | -2.3327 | 1.1954 | ±2.3907 | -1.951 | 0.0510 | . |
| Education: high school or below (vs college) | +1.6220 | 2.6872 | ±5.3744 | +0.604 | 0.5461 |  |
| Site: UCSD (vs UAB) | -1.5730 | 1.5731 | ±3.1462 | -1.000 | 0.3174 |  |
| Site: UW (vs UAB) | -2.8766 | 1.4913 | ±2.9827 | -1.929 | 0.0537 | . |
| **Age (years)** | **-0.4101** | 0.0564 | ±0.1127 | **-7.276** | **3.43e-13** | *** |
| BMI (kg/m2) | -0.0163 | 0.0828 | ±0.1656 | -0.197 | 0.8435 |  |
| Hypertension | +1.7835 | 1.3896 | ±2.7792 | +1.283 | 0.1993 |  |
| High cholesterol | -0.7271 | 1.2238 | ±2.4476 | -0.594 | 0.5525 |  |
| Kidney disease | -1.3217 | 2.4130 | ±4.8261 | -0.548 | 0.5839 |  |
| Circulatory disease | -3.0878 | 2.0112 | ±4.0225 | -1.535 | 0.1247 |  |
| Avg. daily time < 54 (%) | +24.6560 | 21.4509 | ±42.9017 | +1.149 | 0.2504 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **401**, R² = **0.1745**, Adj R² = **0.1512**, F-statistic = **7.48** (p = **1.11e-11**), Residual SE = **11.598** on **389** df, AIC = **3115.4**, BIC = **3163.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.3274** | 4.7507 | ±9.5013 | **+10.804** | **3.29e-27** | *** |
| Education: graduate level (vs college) | -2.2937 | 1.1998 | ±2.3995 | -1.912 | 0.0559 | . |
| Education: high school or below (vs college) | +1.3932 | 2.7014 | ±5.4029 | +0.516 | 0.6060 |  |
| Site: UCSD (vs UAB) | -1.6183 | 1.5723 | ±3.1447 | -1.029 | 0.3034 |  |
| Site: UW (vs UAB) | -2.7803 | 1.4831 | ±2.9663 | -1.875 | 0.0608 | . |
| **Age (years)** | **-0.4119** | 0.0566 | ±0.1133 | **-7.273** | **3.51e-13** | *** |
| BMI (kg/m2) | -0.0097 | 0.0838 | ±0.1675 | -0.116 | 0.9075 |  |
| Hypertension | +1.9259 | 1.3865 | ±2.7730 | +1.389 | 0.1648 |  |
| High cholesterol | -0.8530 | 1.2460 | ±2.4920 | -0.685 | 0.4936 |  |
| Kidney disease | -1.3913 | 2.3878 | ±4.7755 | -0.583 | 0.5601 |  |
| Circulatory disease | -2.7642 | 1.9573 | ±3.9145 | -1.412 | 0.1579 |  |
| Time 54-69, pooled (%) | +2.8938 | 3.1263 | ±6.2526 | +0.926 | 0.3546 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **401**, R² = **0.1733**, Adj R² = **0.1499**, F-statistic = **7.41** (p = **1.43e-11**), Residual SE = **11.606** on **389** df, AIC = **3115.9**, BIC = **3163.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.6284** | 4.7215 | ±9.4429 | **+10.935** | **7.86e-28** | *** |
| Education: graduate level (vs college) | -2.2920 | 1.2011 | ±2.4022 | -1.908 | 0.0564 | . |
| Education: high school or below (vs college) | +1.4494 | 2.7093 | ±5.4187 | +0.535 | 0.5927 |  |
| Site: UCSD (vs UAB) | -1.6747 | 1.5751 | ±3.1503 | -1.063 | 0.2877 |  |
| Site: UW (vs UAB) | -2.8474 | 1.4858 | ±2.9717 | -1.916 | 0.0553 | . |
| **Age (years)** | **-0.4127** | 0.0567 | ±0.1133 | **-7.283** | **3.27e-13** | *** |
| BMI (kg/m2) | -0.0107 | 0.0837 | ±0.1675 | -0.128 | 0.8984 |  |
| Hypertension | +1.9326 | 1.3982 | ±2.7964 | +1.382 | 0.1669 |  |
| High cholesterol | -0.7995 | 1.2466 | ±2.4931 | -0.641 | 0.5213 |  |
| Kidney disease | -1.4349 | 2.3992 | ±4.7983 | -0.598 | 0.5498 |  |
| Circulatory disease | -2.8140 | 1.9613 | ±3.9227 | -1.435 | 0.1514 |  |
| Avg. daily time 54-69 (%) | +1.6802 | 3.2212 | ±6.4424 | +0.522 | 0.6019 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **401**, R² = **0.1763**, Adj R² = **0.1530**, F-statistic = **7.57** (p = **7.69e-12**), Residual SE = **11.586** on **389** df, AIC = **3114.5**, BIC = **3162.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.0801** | 4.7528 | ±9.5056 | **+10.747** | **6.10e-27** | *** |
| Education: graduate level (vs college) | -2.2823 | 1.1999 | ±2.3998 | -1.902 | 0.0572 | . |
| Education: high school or below (vs college) | +1.4168 | 2.6936 | ±5.3871 | +0.526 | 0.5989 |  |
| Site: UCSD (vs UAB) | -1.5372 | 1.5703 | ±3.1407 | -0.979 | 0.3276 |  |
| Site: UW (vs UAB) | -2.7312 | 1.4804 | ±2.9607 | -1.845 | 0.0650 | . |
| **Age (years)** | **-0.4103** | 0.0565 | ±0.1130 | **-7.262** | **3.82e-13** | *** |
| BMI (kg/m2) | -0.0117 | 0.0833 | ±0.1666 | -0.141 | 0.8879 |  |
| Hypertension | +1.9075 | 1.3886 | ±2.7771 | +1.374 | 0.1695 |  |
| High cholesterol | -0.8635 | 1.2424 | ±2.4848 | -0.695 | 0.4870 |  |
| Kidney disease | -1.3292 | 2.3867 | ±4.7734 | -0.557 | 0.5776 |  |
| Circulatory disease | -2.7921 | 1.9680 | ±3.9360 | -1.419 | 0.1560 |  |
| Time < 70 (%) | +3.6209 | 3.0107 | ±6.0214 | +1.203 | 0.2291 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **401**, R² = **0.1743**, Adj R² = **0.1509**, F-statistic = **7.46** (p = **1.17e-11**), Residual SE = **11.600** on **389** df, AIC = **3115.5**, BIC = **3163.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+51.4958** | 4.7157 | ±9.4313 | **+10.920** | **9.23e-28** | *** |
| Education: graduate level (vs college) | -2.2753 | 1.2043 | ±2.4087 | -1.889 | 0.0589 | . |
| Education: high school or below (vs college) | +1.4306 | 2.7030 | ±5.4059 | +0.529 | 0.5966 |  |
| Site: UCSD (vs UAB) | -1.6494 | 1.5732 | ±3.1464 | -1.048 | 0.2944 |  |
| Site: UW (vs UAB) | -2.8379 | 1.4850 | ±2.9700 | -1.911 | 0.0560 | . |
| **Age (years)** | **-0.4126** | 0.0566 | ±0.1132 | **-7.293** | **3.04e-13** | *** |
| BMI (kg/m2) | -0.0113 | 0.0837 | ±0.1673 | -0.135 | 0.8928 |  |
| Hypertension | +1.9771 | 1.4029 | ±2.8058 | +1.409 | 0.1587 |  |
| High cholesterol | -0.8234 | 1.2447 | ±2.4895 | -0.661 | 0.5083 |  |
| Kidney disease | -1.4016 | 2.3990 | ±4.7979 | -0.584 | 0.5591 |  |
| Circulatory disease | -2.8554 | 1.9687 | ±3.9374 | -1.450 | 0.1469 |  |
| Avg. daily time < 70 (%) | +2.5112 | 3.1656 | ±6.3311 | +0.793 | 0.4276 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **401**, R² = **0.1800**, Adj R² = **0.1568**, F-statistic = **7.76** (p = **3.49e-12**), Residual SE = **11.559** on **389** df, AIC = **3112.7**, BIC = **3160.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1956.8131 | 1317.4937 | ±2634.9875 | +1.485 | 0.1375 |  |
| Education: graduate level (vs college) | -2.3105 | 1.1934 | ±2.3867 | -1.936 | 0.0529 | . |
| Education: high school or below (vs college) | +1.8016 | 2.7050 | ±5.4099 | +0.666 | 0.5054 |  |
| Site: UCSD (vs UAB) | -1.3557 | 1.5868 | ±3.1735 | -0.854 | 0.3929 |  |
| Site: UW (vs UAB) | -2.7055 | 1.4808 | ±2.9615 | -1.827 | 0.0677 | . |
| **Age (years)** | **-0.4032** | 0.0564 | ±0.1128 | **-7.152** | **8.54e-13** | *** |
| BMI (kg/m2) | -0.0212 | 0.0814 | ±0.1628 | -0.260 | 0.7948 |  |
| Hypertension | +1.6246 | 1.3908 | ±2.7817 | +1.168 | 0.2428 |  |
| High cholesterol | -0.6688 | 1.2239 | ±2.4479 | -0.546 | 0.5848 |  |
| Kidney disease | -1.2540 | 2.4123 | ±4.8245 | -0.520 | 0.6032 |  |
| Circulatory disease | -2.9752 | 2.0002 | ±4.0004 | -1.487 | 0.1369 |  |
| Time 54-250, pooled (%) | -19.0572 | 13.1816 | ±26.3633 | -1.446 | 0.1482 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **401**, R² = **0.1799**, Adj R² = **0.1568**, F-statistic = **7.76** (p = **3.52e-12**), Residual SE = **11.560** on **389** df, AIC = **3112.7**, BIC = **3160.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +2553.9345 | 1998.0592 | ±3996.1183 | +1.278 | 0.2012 |  |
| Education: graduate level (vs college) | -2.3319 | 1.1943 | ±2.3885 | -1.953 | 0.0509 | . |
| Education: high school or below (vs college) | +1.6411 | 2.6875 | ±5.3751 | +0.611 | 0.5414 |  |
| Site: UCSD (vs UAB) | -1.5345 | 1.5735 | ±3.1469 | -0.975 | 0.3294 |  |
| Site: UW (vs UAB) | -2.8475 | 1.4869 | ±2.9738 | -1.915 | 0.0555 | . |
| **Age (years)** | **-0.4082** | 0.0563 | ±0.1127 | **-7.246** | **4.30e-13** | *** |
| BMI (kg/m2) | -0.0145 | 0.0832 | ±0.1663 | -0.174 | 0.8617 |  |
| Hypertension | +1.8011 | 1.3898 | ±2.7796 | +1.296 | 0.1950 |  |
| High cholesterol | -0.7362 | 1.2239 | ±2.4478 | -0.602 | 0.5475 |  |
| Kidney disease | -1.3239 | 2.4131 | ±4.8261 | -0.549 | 0.5832 |  |
| Circulatory disease | -3.0938 | 2.0109 | ±4.0218 | -1.539 | 0.1239 |  |
| Avg. daily time 54-250 (%) | -25.0253 | 19.9850 | ±39.9699 | -1.252 | 0.2105 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **401**, R² = **0.1816**, Adj R² = **0.1585**, F-statistic = **7.85** (p = **2.46e-12**), Residual SE = **11.548** on **389** df, AIC = **3111.9**, BIC = **3159.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3593** | 4.9131 | ±9.8261 | **+10.250** | **1.18e-24** | *** |
| Education: graduate level (vs college) | -2.2442 | 1.1935 | ±2.3870 | -1.880 | 0.0601 | . |
| Education: high school or below (vs college) | +1.7742 | 2.6757 | ±5.3514 | +0.663 | 0.5073 |  |
| Site: UCSD (vs UAB) | -1.7039 | 1.5734 | ±3.1468 | -1.083 | 0.2788 |  |
| **Site: UW (vs UAB)** | **-2.9143** | 1.4735 | ±2.9469 | **-1.978** | **0.0479** | * |
| **Age (years)** | **-0.4110** | 0.0568 | ±0.1135 | **-7.241** | **4.47e-13** | *** |
| BMI (kg/m2) | -0.0060 | 0.0898 | ±0.1796 | -0.067 | 0.9465 |  |
| Hypertension | +1.6987 | 1.3747 | ±2.7493 | +1.236 | 0.2166 |  |
| High cholesterol | -0.6392 | 1.2325 | ±2.4651 | -0.519 | 0.6040 |  |
| Kidney disease | -2.0285 | 2.5014 | ±5.0027 | -0.811 | 0.4174 |  |
| Circulatory disease | -2.7687 | 1.9192 | ±3.8384 | -1.443 | 0.1491 |  |
| **Time 181-250, pooled (%)** | **+4.2965** | 2.1129 | ±4.2258 | **+2.033** | **0.0420** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **401**, R² = **0.1839**, Adj R² = **0.1608**, F-statistic = **7.97** (p = **1.52e-12**), Residual SE = **11.532** on **389** df, AIC = **3110.8**, BIC = **3158.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2582** | 4.7409 | ±9.4818 | **+10.601** | **2.95e-26** | *** |
| Education: graduate level (vs college) | -2.2245 | 1.1891 | ±2.3782 | -1.871 | 0.0614 | . |
| Education: high school or below (vs college) | +1.8811 | 2.6716 | ±5.3431 | +0.704 | 0.4814 |  |
| Site: UCSD (vs UAB) | -1.6655 | 1.5676 | ±3.1352 | -1.062 | 0.2880 |  |
| **Site: UW (vs UAB)** | **-2.9303** | 1.4685 | ±2.9371 | **-1.995** | **0.0460** | * |
| **Age (years)** | **-0.4072** | 0.0563 | ±0.1126 | **-7.230** | **4.83e-13** | *** |
| BMI (kg/m2) | -0.0099 | 0.0853 | ±0.1705 | -0.116 | 0.9075 |  |
| Hypertension | +1.7082 | 1.3749 | ±2.7498 | +1.242 | 0.2141 |  |
| High cholesterol | -0.7007 | 1.2259 | ±2.4518 | -0.572 | 0.5676 |  |
| Kidney disease | -1.8653 | 2.4668 | ±4.9337 | -0.756 | 0.4495 |  |
| Circulatory disease | -2.7768 | 1.9107 | ±3.8214 | -1.453 | 0.1461 |  |
| **Avg. daily time 181-250 (%)** | **+4.7236** | 2.0625 | ±4.1251 | **+2.290** | **0.0220** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **401**, R² = **0.1817**, Adj R² = **0.1586**, F-statistic = **7.85** (p = **2.41e-12**), Residual SE = **11.547** on **389** df, AIC = **3111.9**, BIC = **3159.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.3211** | 4.9199 | ±9.8398 | **+10.228** | **1.48e-24** | *** |
| Education: graduate level (vs college) | -2.2438 | 1.1935 | ±2.3870 | -1.880 | 0.0601 | . |
| Education: high school or below (vs college) | +1.7777 | 2.6757 | ±5.3513 | +0.664 | 0.5064 |  |
| Site: UCSD (vs UAB) | -1.6982 | 1.5732 | ±3.1464 | -1.079 | 0.2804 |  |
| **Site: UW (vs UAB)** | **-2.9099** | 1.4732 | ±2.9464 | **-1.975** | **0.0482** | * |
| **Age (years)** | **-0.4107** | 0.0568 | ±0.1135 | **-7.236** | **4.62e-13** | *** |
| BMI (kg/m2) | -0.0057 | 0.0899 | ±0.1797 | -0.063 | 0.9494 |  |
| Hypertension | +1.7011 | 1.3748 | ±2.7495 | +1.237 | 0.2159 |  |
| High cholesterol | -0.6403 | 1.2323 | ±2.4647 | -0.520 | 0.6034 |  |
| Kidney disease | -2.0310 | 2.5018 | ±5.0036 | -0.812 | 0.4169 |  |
| Circulatory disease | -2.7689 | 1.9192 | ±3.8385 | -1.443 | 0.1491 |  |
| **Time > 180 (%)** | **+4.3103** | 2.1049 | ±4.2097 | **+2.048** | **0.0406** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **401**, R² = **0.1840**, Adj R² = **0.1609**, F-statistic = **7.97** (p = **1.49e-12**), Residual SE = **11.531** on **389** df, AIC = **3110.7**, BIC = **3158.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.2155** | 4.7461 | ±9.4923 | **+10.580** | **3.68e-26** | *** |
| Education: graduate level (vs college) | -2.2242 | 1.1890 | ±2.3781 | -1.871 | 0.0614 | . |
| Education: high school or below (vs college) | +1.8849 | 2.6716 | ±5.3432 | +0.706 | 0.4805 |  |
| Site: UCSD (vs UAB) | -1.6586 | 1.5673 | ±3.1345 | -1.058 | 0.2899 |  |
| **Site: UW (vs UAB)** | **-2.9249** | 1.4682 | ±2.9363 | **-1.992** | **0.0463** | * |
| **Age (years)** | **-0.4069** | 0.0563 | ±0.1126 | **-7.224** | **5.06e-13** | *** |
| BMI (kg/m2) | -0.0095 | 0.0853 | ±0.1706 | -0.112 | 0.9110 |  |
| Hypertension | +1.7115 | 1.3750 | ±2.7501 | +1.245 | 0.2133 |  |
| High cholesterol | -0.7024 | 1.2257 | ±2.4514 | -0.573 | 0.5666 |  |
| Kidney disease | -1.8668 | 2.4670 | ±4.9341 | -0.757 | 0.4492 |  |
| Circulatory disease | -2.7771 | 1.9108 | ±3.8216 | -1.453 | 0.1461 |  |
| **Avg. daily time > 180 (%)** | **+4.7306** | 2.0511 | ±4.1022 | **+2.306** | **0.0211** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 401)
**Regression Call / Formula**: `mvpa_min_per_day ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **401**, R² = **0.1819**, Adj R² = **0.1588**, F-statistic = **7.86** (p = **2.32e-12**), Residual SE = **11.546** on **389** df, AIC = **3111.8**, BIC = **3159.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+50.7546** | 4.6041 | ±9.2082 | **+11.024** | **2.93e-28** | *** |
| Education: graduate level (vs college) | -2.1439 | 1.1939 | ±2.3878 | -1.796 | 0.0725 | . |
| Education: high school or below (vs college) | +1.5472 | 2.6471 | ±5.2942 | +0.584 | 0.5589 |  |
| Site: UCSD (vs UAB) | -1.8152 | 1.5649 | ±3.1299 | -1.160 | 0.2461 |  |
| **Site: UW (vs UAB)** | **-3.0237** | 1.4703 | ±2.9406 | **-2.056** | **0.0397** | * |
| **Age (years)** | **-0.3924** | 0.0562 | ±0.1124 | **-6.985** | **2.85e-12** | *** |
| BMI (kg/m2) | -0.0231 | 0.0819 | ±0.1637 | -0.282 | 0.7778 |  |
| Hypertension | +1.5710 | 1.3572 | ±2.7144 | +1.158 | 0.2471 |  |
| High cholesterol | -0.8321 | 1.2169 | ±2.4338 | -0.684 | 0.4941 |  |
| Kidney disease | -1.6556 | 2.4416 | ±4.8832 | -0.678 | 0.4977 |  |
| Circulatory disease | -2.6131 | 1.9786 | ±3.9573 | -1.321 | 0.1866 |  |
| Nocturnal time > 180 (%) | +3.2972 | 2.0228 | ±4.0455 | +1.630 | 0.1031 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Resting heart-rate proxy (daily 5th pct, bpm)  (domain: Wearable activity; outcome sample N = 403; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1824**, F-statistic = **9.97** (p = **6.09e-15**), Residual SE = **6.960** on **392** df, AIC = **2718.3**, BIC = **2762.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.9407** | 3.8694 | ±7.7387 | **+16.525** | **2.43e-61** | *** |
| **Education: graduate level (vs college)** | **-1.9757** | 0.7628 | ±1.5255 | **-2.590** | **0.0096** | ** |
| **Education: high school or below (vs college)** | **-2.8025** | 1.2822 | ±2.5644 | **-2.186** | **0.0288** | * |
| **Site: UCSD (vs UAB)** | **-1.9532** | 0.9505 | ±1.9009 | **-2.055** | **0.0399** | * |
| **Site: UW (vs UAB)** | **-2.7252** | 0.8541 | ±1.7081 | **-3.191** | **0.0014** | ** |
| **Age (years)** | **-0.1448** | 0.0361 | ±0.0722 | **-4.008** | **6.11e-05** | *** |
| **BMI (kg/m2)** | **+0.2578** | 0.0761 | ±0.1521 | **+3.389** | **7.02e-04** | *** |
| **Hypertension** | **+2.0570** | 0.8072 | ±1.6144 | **+2.548** | **0.0108** | * |
| High cholesterol | -0.3663 | 0.7573 | ±1.5146 | -0.484 | 0.6286 |  |
| Kidney disease | -0.3222 | 2.0209 | ±4.0418 | -0.159 | 0.8733 |  |
| Circulatory disease | -1.7166 | 0.9110 | ±1.8220 | -1.884 | 0.0595 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1803**, F-statistic = **9.04** (p = **1.99e-14**), Residual SE = **6.969** on **391** df, AIC = **2720.3**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.5952** | 6.9779 | ±13.9557 | **+9.114** | **7.95e-20** | *** |
| **Education: graduate level (vs college)** | **-1.9734** | 0.7621 | ±1.5242 | **-2.589** | **0.0096** | ** |
| **Education: high school or below (vs college)** | **-2.8062** | 1.2860 | ±2.5720 | **-2.182** | **0.0291** | * |
| **Site: UCSD (vs UAB)** | **-1.9507** | 0.9490 | ±1.8980 | **-2.055** | **0.0398** | * |
| **Site: UW (vs UAB)** | **-2.7220** | 0.8541 | ±1.7082 | **-3.187** | **0.0014** | ** |
| **Age (years)** | **-0.1449** | 0.0368 | ±0.0737 | **-3.933** | **8.38e-05** | *** |
| **BMI (kg/m2)** | **+0.2574** | 0.0778 | ±0.1556 | **+3.309** | **9.35e-04** | *** |
| **Hypertension** | **+2.0534** | 0.8132 | ±1.6264 | **+2.525** | **0.0116** | * |
| High cholesterol | -0.3762 | 0.7727 | ±1.5454 | -0.487 | 0.6264 |  |
| Kidney disease | -0.3166 | 2.0203 | ±4.0406 | -0.157 | 0.8755 |  |
| Circulatory disease | -1.7141 | 0.9174 | ±1.8349 | -1.868 | 0.0617 | . |
| HbA1c (%) | +0.0665 | 1.2603 | ±2.5206 | +0.053 | 0.9579 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **403**, R² = **0.2030**, Adj R² = **0.1806**, F-statistic = **9.06** (p = **1.87e-14**), Residual SE = **6.967** on **391** df, AIC = **2720.1**, BIC = **2768.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.9736** | 7.0046 | ±14.0092 | **+8.848** | **8.94e-19** | *** |
| **Education: graduate level (vs college)** | **-1.9676** | 0.7626 | ±1.5252 | **-2.580** | **0.0099** | ** |
| **Education: high school or below (vs college)** | **-2.7790** | 1.2865 | ±2.5731 | **-2.160** | **0.0308** | * |
| **Site: UCSD (vs UAB)** | **-1.9680** | 0.9546 | ±1.9093 | **-2.062** | **0.0393** | * |
| **Site: UW (vs UAB)** | **-2.7431** | 0.8583 | ±1.7166 | **-3.196** | **0.0014** | ** |
| **Age (years)** | **-0.1443** | 0.0363 | ±0.0727 | **-3.969** | **7.20e-05** | *** |
| **BMI (kg/m2)** | **+0.2566** | 0.0762 | ±0.1523 | **+3.369** | **7.55e-04** | *** |
| **Hypertension** | **+2.0336** | 0.8061 | ±1.6123 | **+2.523** | **0.0116** | * |
| High cholesterol | -0.3575 | 0.7650 | ±1.5300 | -0.467 | 0.6403 |  |
| Kidney disease | -0.3238 | 2.0431 | ±4.0862 | -0.158 | 0.8741 |  |
| Circulatory disease | -1.7232 | 0.9132 | ±1.8263 | -1.887 | 0.0592 | . |
| Mean glucose (mg/dL) | +0.0174 | 0.0493 | ±0.0986 | +0.352 | 0.7247 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **403**, R² = **0.2030**, Adj R² = **0.1806**, F-statistic = **9.06** (p = **1.87e-14**), Residual SE = **6.967** on **391** df, AIC = **2720.1**, BIC = **2768.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.5701** | 13.2421 | ±26.4841 | **+4.499** | **6.84e-06** | *** |
| **Education: graduate level (vs college)** | **-1.9676** | 0.7626 | ±1.5252 | **-2.580** | **0.0099** | ** |
| **Education: high school or below (vs college)** | **-2.7790** | 1.2865 | ±2.5731 | **-2.160** | **0.0308** | * |
| **Site: UCSD (vs UAB)** | **-1.9680** | 0.9546 | ±1.9093 | **-2.062** | **0.0393** | * |
| **Site: UW (vs UAB)** | **-2.7431** | 0.8583 | ±1.7166 | **-3.196** | **0.0014** | ** |
| **Age (years)** | **-0.1443** | 0.0363 | ±0.0727 | **-3.969** | **7.20e-05** | *** |
| **BMI (kg/m2)** | **+0.2566** | 0.0762 | ±0.1523 | **+3.369** | **7.55e-04** | *** |
| **Hypertension** | **+2.0336** | 0.8061 | ±1.6123 | **+2.523** | **0.0116** | * |
| High cholesterol | -0.3575 | 0.7650 | ±1.5300 | -0.467 | 0.6403 |  |
| Kidney disease | -0.3238 | 2.0431 | ±4.0862 | -0.158 | 0.8741 |  |
| Circulatory disease | -1.7232 | 0.9132 | ±1.8263 | -1.887 | 0.0592 | . |
| GMI (%) | +0.7261 | 2.0616 | ±4.1233 | +0.352 | 0.7247 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **403**, R² = **0.2051**, Adj R² = **0.1827**, F-statistic = **9.17** (p = **1.18e-14**), Residual SE = **6.958** on **391** df, AIC = **2719.1**, BIC = **2767.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.3044** | 5.5368 | ±11.0736 | **+10.711** | **9.04e-27** | *** |
| **Education: graduate level (vs college)** | **-1.9307** | 0.7543 | ±1.5086 | **-2.560** | **0.0105** | * |
| **Education: high school or below (vs college)** | **-2.7401** | 1.2816 | ±2.5633 | **-2.138** | **0.0325** | * |
| **Site: UCSD (vs UAB)** | **-2.0473** | 0.9574 | ±1.9148 | **-2.138** | **0.0325** | * |
| **Site: UW (vs UAB)** | **-2.8005** | 0.8604 | ±1.7207 | **-3.255** | **0.0011** | ** |
| **Age (years)** | **-0.1390** | 0.0365 | ±0.0730 | **-3.810** | **1.39e-04** | *** |
| **BMI (kg/m2)** | **+0.2499** | 0.0756 | ±0.1511 | **+3.307** | **9.43e-04** | *** |
| **Hypertension** | **+1.9866** | 0.8041 | ±1.6082 | **+2.470** | **0.0135** | * |
| High cholesterol | -0.3642 | 0.7609 | ±1.5219 | -0.479 | 0.6322 |  |
| Kidney disease | -0.2376 | 2.0312 | ±4.0624 | -0.117 | 0.9069 |  |
| Circulatory disease | -1.6989 | 0.9102 | ±1.8204 | -1.867 | 0.0620 | . |
| Nocturnal mean 00-06h (mg/dL) | +0.0398 | 0.0375 | ±0.0749 | +1.062 | 0.2881 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1803**, F-statistic = **9.04** (p = **1.99e-14**), Residual SE = **6.969** on **391** df, AIC = **2720.3**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.0050** | 4.4760 | ±8.9520 | **+14.300** | **2.20e-46** | *** |
| **Education: graduate level (vs college)** | **-1.9774** | 0.7620 | ±1.5240 | **-2.595** | **0.0095** | ** |
| **Education: high school or below (vs college)** | **-2.8034** | 1.2855 | ±2.5710 | **-2.181** | **0.0292** | * |
| **Site: UCSD (vs UAB)** | **-1.9544** | 0.9523 | ±1.9045 | **-2.052** | **0.0401** | * |
| **Site: UW (vs UAB)** | **-2.7267** | 0.8534 | ±1.7067 | **-3.195** | **0.0014** | ** |
| **Age (years)** | **-0.1447** | 0.0362 | ±0.0725 | **-3.994** | **6.50e-05** | *** |
| **BMI (kg/m2)** | **+0.2578** | 0.0763 | ±0.1527 | **+3.378** | **7.31e-04** | *** |
| **Hypertension** | **+2.0585** | 0.8054 | ±1.6109 | **+2.556** | **0.0106** | * |
| High cholesterol | -0.3678 | 0.7723 | ±1.5446 | -0.476 | 0.6339 |  |
| Kidney disease | -0.3177 | 2.1061 | ±4.2122 | -0.151 | 0.8801 |  |
| Circulatory disease | -1.7156 | 0.9091 | ±1.8183 | -1.887 | 0.0592 | . |
| Glucose SD, pooled (mg/dL) | -0.0039 | 0.1518 | ±0.3036 | -0.026 | 0.9795 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1803**, F-statistic = **9.04** (p = **1.99e-14**), Residual SE = **6.969** on **391** df, AIC = **2720.3**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.0552** | 4.2939 | ±8.5877 | **+14.918** | **2.52e-50** | *** |
| **Education: graduate level (vs college)** | **-1.9794** | 0.7620 | ±1.5240 | **-2.598** | **0.0094** | ** |
| **Education: high school or below (vs college)** | **-2.8051** | 1.2857 | ±2.5715 | **-2.182** | **0.0291** | * |
| **Site: UCSD (vs UAB)** | **-1.9552** | 0.9510 | ±1.9021 | **-2.056** | **0.0398** | * |
| **Site: UW (vs UAB)** | **-2.7279** | 0.8526 | ±1.7052 | **-3.200** | **0.0014** | ** |
| **Age (years)** | **-0.1447** | 0.0363 | ±0.0725 | **-3.990** | **6.61e-05** | *** |
| **BMI (kg/m2)** | **+0.2579** | 0.0767 | ±0.1534 | **+3.363** | **7.71e-04** | *** |
| **Hypertension** | **+2.0590** | 0.8060 | ±1.6120 | **+2.555** | **0.0106** | * |
| High cholesterol | -0.3690 | 0.7692 | ±1.5383 | -0.480 | 0.6314 |  |
| Kidney disease | -0.3135 | 2.0937 | ±4.1874 | -0.150 | 0.8810 |  |
| Circulatory disease | -1.7160 | 0.9117 | ±1.8235 | -1.882 | 0.0598 | . |
| Avg. daily SD (mg/dL) | -0.0077 | 0.1497 | ±0.2995 | -0.051 | 0.9590 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **403**, R² = **0.2029**, Adj R² = **0.1805**, F-statistic = **9.05** (p = **1.93e-14**), Residual SE = **6.968** on **391** df, AIC = **2720.2**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.5642** | 4.2849 | ±8.5697 | **+15.068** | **2.63e-51** | *** |
| **Education: graduate level (vs college)** | **-1.9896** | 0.7643 | ±1.5286 | **-2.603** | **0.0092** | ** |
| **Education: high school or below (vs college)** | **-2.8040** | 1.2858 | ±2.5716 | **-2.181** | **0.0292** | * |
| **Site: UCSD (vs UAB)** | **-1.9693** | 0.9532 | ±1.9065 | **-2.066** | **0.0388** | * |
| **Site: UW (vs UAB)** | **-2.7446** | 0.8535 | ±1.7070 | **-3.216** | **0.0013** | ** |
| **Age (years)** | **-0.1445** | 0.0363 | ±0.0727 | **-3.977** | **6.99e-05** | *** |
| **BMI (kg/m2)** | **+0.2579** | 0.0763 | ±0.1526 | **+3.379** | **7.27e-04** | *** |
| **Hypertension** | **+2.0638** | 0.8075 | ±1.6149 | **+2.556** | **0.0106** | * |
| High cholesterol | -0.3783 | 0.7656 | ±1.5313 | -0.494 | 0.6213 |  |
| Kidney disease | -0.2792 | 2.0803 | ±4.1605 | -0.134 | 0.8932 |  |
| Circulatory disease | -1.7087 | 0.9092 | ±1.8185 | -1.879 | 0.0602 | . |
| CV (%) | -0.0425 | 0.1520 | ±0.3040 | -0.280 | 0.7797 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **403**, R² = **0.2030**, Adj R² = **0.1806**, F-statistic = **9.06** (p = **1.88e-14**), Residual SE = **6.967** on **391** df, AIC = **2720.1**, BIC = **2768.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.1212** | 4.5283 | ±9.0566 | **+13.939** | **3.66e-44** | *** |
| **Education: graduate level (vs college)** | **-1.9975** | 0.7654 | ±1.5307 | **-2.610** | **0.0091** | ** |
| **Education: high school or below (vs college)** | **-2.8004** | 1.2872 | ±2.5744 | **-2.176** | **0.0296** | * |
| **Site: UCSD (vs UAB)** | **-1.9707** | 0.9534 | ±1.9069 | **-2.067** | **0.0387** | * |
| **Site: UW (vs UAB)** | **-2.7474** | 0.8540 | ±1.7079 | **-3.217** | **0.0013** | ** |
| **Age (years)** | **-0.1445** | 0.0363 | ±0.0725 | **-3.983** | **6.81e-05** | *** |
| **BMI (kg/m2)** | **+0.2580** | 0.0763 | ±0.1525 | **+3.383** | **7.18e-04** | *** |
| **Hypertension** | **+2.0665** | 0.8071 | ±1.6142 | **+2.560** | **0.0105** | * |
| High cholesterol | -0.3847 | 0.7663 | ±1.5326 | -0.502 | 0.6157 |  |
| Kidney disease | -0.2772 | 2.0652 | ±4.1304 | -0.134 | 0.8932 |  |
| Circulatory disease | -1.7105 | 0.9116 | ±1.8232 | -1.876 | 0.0606 | . |
| Mean / SD ratio | +0.1182 | 0.3001 | ±0.6002 | +0.394 | 0.6936 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **403**, R² = **0.2029**, Adj R² = **0.1805**, F-statistic = **9.05** (p = **1.92e-14**), Residual SE = **6.968** on **391** df, AIC = **2720.2**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.3668** | 4.4440 | ±8.8879 | **+14.259** | **3.94e-46** | *** |
| **Education: graduate level (vs college)** | **-1.9942** | 0.7651 | ±1.5303 | **-2.606** | **0.0092** | ** |
| **Education: high school or below (vs college)** | **-2.8033** | 1.2873 | ±2.5746 | **-2.178** | **0.0294** | * |
| **Site: UCSD (vs UAB)** | **-1.9639** | 0.9518 | ±1.9037 | **-2.063** | **0.0391** | * |
| **Site: UW (vs UAB)** | **-2.7412** | 0.8517 | ±1.7035 | **-3.218** | **0.0013** | ** |
| **Age (years)** | **-0.1444** | 0.0363 | ±0.0725 | **-3.982** | **6.85e-05** | *** |
| **BMI (kg/m2)** | **+0.2583** | 0.0765 | ±0.1529 | **+3.378** | **7.31e-04** | *** |
| **Hypertension** | **+2.0601** | 0.8080 | ±1.6159 | **+2.550** | **0.0108** | * |
| High cholesterol | -0.3772 | 0.7628 | ±1.5256 | -0.495 | 0.6209 |  |
| Kidney disease | -0.2866 | 2.0578 | ±4.1156 | -0.139 | 0.8892 |  |
| Circulatory disease | -1.7218 | 0.9151 | ±1.8302 | -1.882 | 0.0599 | . |
| Avg. daily mean/SD | +0.0713 | 0.2279 | ±0.4558 | +0.313 | 0.7543 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **403**, R² = **0.2106**, Adj R² = **0.1883**, F-statistic = **9.48** (p = **3.46e-15**), Residual SE = **6.934** on **391** df, AIC = **2716.3**, BIC = **2764.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.3990** | 4.2820 | ±8.5640 | **+13.872** | **9.39e-44** | *** |
| **Education: graduate level (vs college)** | **-1.9596** | 0.7619 | ±1.5238 | **-2.572** | **0.0101** | * |
| **Education: high school or below (vs college)** | **-2.9910** | 1.2484 | ±2.4968 | **-2.396** | **0.0166** | * |
| **Site: UCSD (vs UAB)** | **-1.8823** | 0.9409 | ±1.8818 | **-2.001** | **0.0454** | * |
| **Site: UW (vs UAB)** | **-2.5553** | 0.8580 | ±1.7160 | **-2.978** | **0.0029** | ** |
| **Age (years)** | **-0.1388** | 0.0359 | ±0.0717 | **-3.868** | **1.10e-04** | *** |
| **BMI (kg/m2)** | **+0.2623** | 0.0738 | ±0.1476 | **+3.555** | **3.78e-04** | *** |
| **Hypertension** | **+2.1136** | 0.8011 | ±1.6022 | **+2.638** | **0.0083** | ** |
| High cholesterol | -0.4108 | 0.7541 | ±1.5083 | -0.545 | 0.5860 |  |
| Kidney disease | -0.5605 | 2.0231 | ±4.0462 | -0.277 | 0.7818 |  |
| Circulatory disease | -1.6926 | 0.9013 | ±1.8027 | -1.878 | 0.0604 | . |
| MAG (mg/dL/h) | +0.1170 | 0.0614 | ±0.1228 | +1.905 | 0.0568 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1804**, F-statistic = **9.04** (p = **1.99e-14**), Residual SE = **6.968** on **391** df, AIC = **2720.2**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.7273** | 4.8079 | ±9.6157 | **+13.255** | **4.23e-40** | *** |
| **Education: graduate level (vs college)** | **-1.9723** | 0.7659 | ±1.5317 | **-2.575** | **0.0100** | * |
| **Education: high school or below (vs college)** | **-2.8018** | 1.2844 | ±2.5687 | **-2.181** | **0.0292** | * |
| **Site: UCSD (vs UAB)** | **-1.9504** | 0.9541 | ±1.9083 | **-2.044** | **0.0409** | * |
| **Site: UW (vs UAB)** | **-2.7213** | 0.8584 | ±1.7168 | **-3.170** | **0.0015** | ** |
| **Age (years)** | **-0.1448** | 0.0362 | ±0.0724 | **-3.997** | **6.41e-05** | *** |
| **BMI (kg/m2)** | **+0.2581** | 0.0767 | ±0.1534 | **+3.365** | **7.65e-04** | *** |
| **Hypertension** | **+2.0589** | 0.8121 | ±1.6242 | **+2.535** | **0.0112** | * |
| High cholesterol | -0.3648 | 0.7619 | ±1.5239 | -0.479 | 0.6321 |  |
| Kidney disease | -0.3320 | 2.0647 | ±4.1293 | -0.161 | 0.8723 |  |
| Circulatory disease | -1.7180 | 0.9113 | ±1.8226 | -1.885 | 0.0594 | . |
| Avg. daily range (mg/dL) | +0.0025 | 0.0318 | ±0.0636 | +0.080 | 0.9364 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **403**, R² = **0.2075**, Adj R² = **0.1853**, F-statistic = **9.31** (p = **6.82e-15**), Residual SE = **6.948** on **391** df, AIC = **2717.8**, BIC = **2765.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+62.5688** | 3.8786 | ±7.7573 | **+16.132** | **1.53e-58** | *** |
| **Education: graduate level (vs college)** | **-2.0121** | 0.7622 | ±1.5245 | **-2.640** | **0.0083** | ** |
| **Education: high school or below (vs college)** | **-2.8976** | 1.3003 | ±2.6006 | **-2.228** | **0.0259** | * |
| **Site: UCSD (vs UAB)** | **-1.8912** | 0.9464 | ±1.8929 | **-1.998** | **0.0457** | * |
| **Site: UW (vs UAB)** | **-2.7414** | 0.8479 | ±1.6958 | **-3.233** | **0.0012** | ** |
| **Age (years)** | **-0.1446** | 0.0358 | ±0.0716 | **-4.042** | **5.30e-05** | *** |
| **BMI (kg/m2)** | **+0.2569** | 0.0756 | ±0.1513 | **+3.397** | **6.81e-04** | *** |
| **Hypertension** | **+1.9538** | 0.8140 | ±1.6280 | **+2.400** | **0.0164** | * |
| High cholesterol | -0.3875 | 0.7543 | ±1.5086 | -0.514 | 0.6074 |  |
| Kidney disease | -0.3357 | 2.0036 | ±4.0072 | -0.168 | 0.8669 |  |
| **Circulatory disease** | **-1.8194** | 0.9253 | ±1.8505 | **-1.966** | **0.0493** | * |
| SD of daily means (mg/dL) | +0.2828 | 0.1934 | ±0.3868 | +1.462 | 0.1437 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **403**, R² = **0.2032**, Adj R² = **0.1808**, F-statistic = **9.07** (p = **1.80e-14**), Residual SE = **6.967** on **391** df, AIC = **2720.0**, BIC = **2768.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +119.5255 | 119.1548 | ±238.3096 | +1.003 | 0.3158 |  |
| **Education: graduate level (vs college)** | **-1.9576** | 0.7718 | ±1.5436 | **-2.536** | **0.0112** | * |
| **Education: high school or below (vs college)** | **-2.7830** | 1.2792 | ±2.5584 | **-2.176** | **0.0296** | * |
| **Site: UCSD (vs UAB)** | **-1.9288** | 0.9583 | ±1.9166 | **-2.013** | **0.0441** | * |
| **Site: UW (vs UAB)** | **-2.7117** | 0.8570 | ±1.7141 | **-3.164** | **0.0016** | ** |
| **Age (years)** | **-0.1442** | 0.0363 | ±0.0726 | **-3.974** | **7.05e-05** | *** |
| **BMI (kg/m2)** | **+0.2583** | 0.0780 | ±0.1560 | **+3.311** | **9.29e-04** | *** |
| **Hypertension** | **+2.0494** | 0.8069 | ±1.6139 | **+2.540** | **0.0111** | * |
| High cholesterol | -0.3694 | 0.7576 | ±1.5152 | -0.488 | 0.6258 |  |
| Kidney disease | -0.3740 | 2.0566 | ±4.1131 | -0.182 | 0.8557 |  |
| Circulatory disease | -1.7148 | 0.9101 | ±1.8201 | -1.884 | 0.0595 | . |
| Time in range 70-180, pooled (%) | -0.5590 | 1.2020 | ±2.4041 | -0.465 | 0.6419 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **403**, R² = **0.2034**, Adj R² = **0.1810**, F-statistic = **9.08** (p = **1.73e-14**), Residual SE = **6.966** on **391** df, AIC = **2719.9**, BIC = **2767.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +125.9651 | 107.3670 | ±214.7339 | +1.173 | 0.2407 |  |
| **Education: graduate level (vs college)** | **-1.9494** | 0.7650 | ±1.5301 | **-2.548** | **0.0108** | * |
| **Education: high school or below (vs college)** | **-2.7742** | 1.2752 | ±2.5504 | **-2.176** | **0.0296** | * |
| **Site: UCSD (vs UAB)** | **-1.9352** | 0.9486 | ±1.8972 | **-2.040** | **0.0413** | * |
| **Site: UW (vs UAB)** | **-2.7272** | 0.8548 | ±1.7096 | **-3.190** | **0.0014** | ** |
| **Age (years)** | **-0.1441** | 0.0361 | ±0.0722 | **-3.992** | **6.55e-05** | *** |
| **BMI (kg/m2)** | **+0.2579** | 0.0763 | ±0.1527 | **+3.379** | **7.28e-04** | *** |
| **Hypertension** | **+2.0746** | 0.8096 | ±1.6192 | **+2.562** | **0.0104** | * |
| High cholesterol | -0.3786 | 0.7545 | ±1.5091 | -0.502 | 0.6159 |  |
| Kidney disease | -0.3583 | 2.0352 | ±4.0703 | -0.176 | 0.8603 |  |
| Circulatory disease | -1.7317 | 0.9066 | ±1.8133 | -1.910 | 0.0561 | . |
| Avg. daily time in range 70-180 (%) | -0.6233 | 1.0769 | ±2.1539 | -0.579 | 0.5628 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **403**, R² = **0.2041**, Adj R² = **0.1817**, F-statistic = **9.12** (p = **1.47e-14**), Residual SE = **6.963** on **391** df, AIC = **2719.6**, BIC = **2767.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.7110** | 3.8556 | ±7.7112 | **+16.524** | **2.45e-61** | *** |
| **Education: graduate level (vs college)** | **-1.9691** | 0.7640 | ±1.5280 | **-2.577** | **0.0100** | ** |
| **Education: high school or below (vs college)** | **-2.7647** | 1.2874 | ±2.5749 | **-2.147** | **0.0318** | * |
| Site: UCSD (vs UAB) | -1.8429 | 0.9593 | ±1.9186 | -1.921 | 0.0547 | . |
| **Site: UW (vs UAB)** | **-2.6675** | 0.8632 | ±1.7265 | **-3.090** | **0.0020** | ** |
| **Age (years)** | **-0.1441** | 0.0360 | ±0.0720 | **-4.002** | **6.28e-05** | *** |
| **BMI (kg/m2)** | **+0.2578** | 0.0757 | ±0.1514 | **+3.405** | **6.61e-04** | *** |
| **Hypertension** | **+2.0193** | 0.8074 | ±1.6148 | **+2.501** | **0.0124** | * |
| High cholesterol | -0.3594 | 0.7583 | ±1.5167 | -0.474 | 0.6356 |  |
| Kidney disease | -0.2406 | 2.0287 | ±4.0574 | -0.119 | 0.9056 |  |
| Circulatory disease | -1.7503 | 0.9113 | ±1.8227 | -1.921 | 0.0548 | . |
| Any reading < 54 during wear (0/1) | +0.7574 | 0.8861 | ±1.7722 | +0.855 | 0.3927 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **403**, R² = **0.2110**, Adj R² = **0.1888**, F-statistic = **9.50** (p = **3.15e-15**), Residual SE = **6.933** on **391** df, AIC = **2716.1**, BIC = **2764.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.5314** | 3.7673 | ±7.5346 | **+16.864** | **8.29e-64** | *** |
| **Education: graduate level (vs college)** | **-1.9659** | 0.7587 | ±1.5175 | **-2.591** | **0.0096** | ** |
| **Education: high school or below (vs college)** | **-2.6174** | 1.2865 | ±2.5731 | **-2.034** | **0.0419** | * |
| Site: UCSD (vs UAB) | -1.7383 | 0.9523 | ±1.9047 | -1.825 | 0.0680 | . |
| **Site: UW (vs UAB)** | **-2.6311** | 0.8505 | ±1.7011 | **-3.093** | **0.0020** | ** |
| **Age (years)** | **-0.1396** | 0.0357 | ±0.0714 | **-3.913** | **9.12e-05** | *** |
| **BMI (kg/m2)** | **+0.2501** | 0.0741 | ±0.1482 | **+3.375** | **7.38e-04** | *** |
| **Hypertension** | **+1.9074** | 0.8084 | ±1.6168 | **+2.360** | **0.0183** | * |
| High cholesterol | -0.3095 | 0.7560 | ±1.5120 | -0.409 | 0.6822 |  |
| Kidney disease | -0.1759 | 2.0255 | ±4.0509 | -0.087 | 0.9308 |  |
| **Circulatory disease** | **-1.8396** | 0.9132 | ±1.8263 | **-2.015** | **0.0439** | * |
| **Time < 54 (%)** | **+12.7485** | 4.9881 | ±9.9763 | **+2.556** | **0.0106** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **403**, R² = **0.2035**, Adj R² = **0.1811**, F-statistic = **9.08** (p = **1.71e-14**), Residual SE = **6.965** on **391** df, AIC = **2719.9**, BIC = **2767.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.8948** | 3.8558 | ±7.7116 | **+16.571** | **1.13e-61** | *** |
| **Education: graduate level (vs college)** | **-1.9769** | 0.7646 | ±1.5293 | **-2.585** | **0.0097** | ** |
| **Education: high school or below (vs college)** | **-2.7806** | 1.2799 | ±2.5598 | **-2.173** | **0.0298** | * |
| **Site: UCSD (vs UAB)** | **-1.9279** | 0.9516 | ±1.9033 | **-2.026** | **0.0428** | * |
| **Site: UW (vs UAB)** | **-2.7272** | 0.8557 | ±1.7114 | **-3.187** | **0.0014** | ** |
| **Age (years)** | **-0.1443** | 0.0361 | ±0.0721 | **-4.001** | **6.31e-05** | *** |
| **BMI (kg/m2)** | **+0.2567** | 0.0758 | ±0.1517 | **+3.384** | **7.14e-04** | *** |
| **Hypertension** | **+2.0469** | 0.8084 | ±1.6168 | **+2.532** | **0.0113** | * |
| High cholesterol | -0.3622 | 0.7590 | ±1.5181 | -0.477 | 0.6332 |  |
| Kidney disease | -0.2927 | 2.0233 | ±4.0467 | -0.145 | 0.8850 |  |
| Circulatory disease | -1.7756 | 0.9190 | ±1.8380 | -1.932 | 0.0534 | . |
| Avg. daily time < 54 (%) | +4.8921 | 8.0373 | ±16.0745 | +0.609 | 0.5427 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1803**, F-statistic = **9.04** (p = **1.99e-14**), Residual SE = **6.969** on **391** df, AIC = **2720.3**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.9269** | 3.8473 | ±7.6946 | **+16.616** | **5.34e-62** | *** |
| **Education: graduate level (vs college)** | **-1.9747** | 0.7676 | ±1.5352 | **-2.573** | **0.0101** | * |
| **Education: high school or below (vs college)** | **-2.8056** | 1.2868 | ±2.5736 | **-2.180** | **0.0292** | * |
| **Site: UCSD (vs UAB)** | **-1.9512** | 0.9499 | ±1.8999 | **-2.054** | **0.0400** | * |
| **Site: UW (vs UAB)** | **-2.7230** | 0.8587 | ±1.7174 | **-3.171** | **0.0015** | ** |
| **Age (years)** | **-0.1447** | 0.0361 | ±0.0723 | **-4.006** | **6.17e-05** | *** |
| **BMI (kg/m2)** | **+0.2578** | 0.0761 | ±0.1521 | **+3.389** | **7.00e-04** | *** |
| **Hypertension** | **+2.0594** | 0.8125 | ±1.6251 | **+2.535** | **0.0113** | * |
| High cholesterol | -0.3690 | 0.7630 | ±1.5261 | -0.484 | 0.6286 |  |
| Kidney disease | -0.3201 | 2.0263 | ±4.0526 | -0.158 | 0.8745 |  |
| Circulatory disease | -1.7159 | 0.9143 | ±1.8285 | -1.877 | 0.0605 | . |
| Time 54-69, pooled (%) | +0.0763 | 1.8066 | ±3.6132 | +0.042 | 0.9663 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **403**, R² = **0.2031**, Adj R² = **0.1806**, F-statistic = **9.06** (p = **1.87e-14**), Residual SE = **6.967** on **391** df, AIC = **2720.1**, BIC = **2768.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+64.0404** | 3.8583 | ±7.7167 | **+16.598** | **7.22e-62** | *** |
| **Education: graduate level (vs college)** | **-1.9915** | 0.7661 | ±1.5322 | **-2.600** | **0.0093** | ** |
| **Education: high school or below (vs college)** | **-2.7746** | 1.2936 | ±2.5871 | **-2.145** | **0.0320** | * |
| **Site: UCSD (vs UAB)** | **-1.9642** | 0.9495 | ±1.8989 | **-2.069** | **0.0386** | * |
| **Site: UW (vs UAB)** | **-2.7336** | 0.8560 | ±1.7121 | **-3.193** | **0.0014** | ** |
| **Age (years)** | **-0.1446** | 0.0362 | ±0.0725 | **-3.990** | **6.62e-05** | *** |
| **BMI (kg/m2)** | **+0.2577** | 0.0763 | ±0.1526 | **+3.379** | **7.29e-04** | *** |
| **Hypertension** | **+2.0130** | 0.8153 | ±1.6307 | **+2.469** | **0.0136** | * |
| High cholesterol | -0.3432 | 0.7629 | ±1.5258 | -0.450 | 0.6528 |  |
| Kidney disease | -0.3381 | 2.0350 | ±4.0700 | -0.166 | 0.8680 |  |
| Circulatory disease | -1.7059 | 0.9100 | ±1.8201 | -1.875 | 0.0609 | . |
| Avg. daily time 54-69 (%) | -0.7573 | 1.7484 | ±3.4968 | -0.433 | 0.6649 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **403**, R² = **0.2034**, Adj R² = **0.1810**, F-statistic = **9.08** (p = **1.72e-14**), Residual SE = **6.966** on **391** df, AIC = **2719.9**, BIC = **2767.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.7355** | 3.8239 | ±7.6478 | **+16.668** | **2.25e-62** | *** |
| **Education: graduate level (vs college)** | **-1.9630** | 0.7669 | ±1.5337 | **-2.560** | **0.0105** | * |
| **Education: high school or below (vs college)** | **-2.8273** | 1.2818 | ±2.5636 | **-2.206** | **0.0274** | * |
| **Site: UCSD (vs UAB)** | **-1.9117** | 0.9489 | ±1.8978 | **-2.015** | **0.0439** | * |
| **Site: UW (vs UAB)** | **-2.6904** | 0.8574 | ±1.7148 | **-3.138** | **0.0017** | ** |
| **Age (years)** | **-0.1442** | 0.0359 | ±0.0719 | **-4.011** | **6.04e-05** | *** |
| **BMI (kg/m2)** | **+0.2575** | 0.0757 | ±0.1514 | **+3.401** | **6.72e-04** | *** |
| **Hypertension** | **+2.0759** | 0.8089 | ±1.6178 | **+2.566** | **0.0103** | * |
| High cholesterol | -0.3963 | 0.7607 | ±1.5214 | -0.521 | 0.6024 |  |
| Kidney disease | -0.2849 | 2.0208 | ±4.0416 | -0.141 | 0.8879 |  |
| Circulatory disease | -1.7174 | 0.9118 | ±1.8235 | -1.884 | 0.0596 | . |
| Time < 70 (%) | +0.9646 | 1.5908 | ±3.1815 | +0.606 | 0.5443 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **403**, R² = **0.2029**, Adj R² = **0.1804**, F-statistic = **9.05** (p = **1.95e-14**), Residual SE = **6.968** on **391** df, AIC = **2720.2**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.9968** | 3.8559 | ±7.7117 | **+16.597** | **7.30e-62** | *** |
| **Education: graduate level (vs college)** | **-1.9839** | 0.7658 | ±1.5315 | **-2.591** | **0.0096** | ** |
| **Education: high school or below (vs college)** | **-2.7897** | 1.2908 | ±2.5816 | **-2.161** | **0.0307** | * |
| **Site: UCSD (vs UAB)** | **-1.9610** | 0.9488 | ±1.8976 | **-2.067** | **0.0387** | * |
| **Site: UW (vs UAB)** | **-2.7295** | 0.8562 | ±1.7124 | **-3.188** | **0.0014** | ** |
| **Age (years)** | **-0.1447** | 0.0362 | ±0.0724 | **-3.996** | **6.44e-05** | *** |
| **BMI (kg/m2)** | **+0.2578** | 0.0763 | ±0.1526 | **+3.380** | **7.24e-04** | *** |
| **Hypertension** | **+2.0347** | 0.8143 | ±1.6285 | **+2.499** | **0.0125** | * |
| High cholesterol | -0.3545 | 0.7615 | ±1.5231 | -0.466 | 0.6416 |  |
| Kidney disease | -0.3330 | 2.0315 | ±4.0630 | -0.164 | 0.8698 |  |
| Circulatory disease | -1.7062 | 0.9086 | ±1.8173 | -1.878 | 0.0604 | . |
| Avg. daily time < 70 (%) | -0.3972 | 1.5732 | ±3.1463 | -0.252 | 0.8007 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **403**, R² = **0.2100**, Adj R² = **0.1878**, F-statistic = **9.45** (p = **3.89e-15**), Residual SE = **6.937** on **391** df, AIC = **2716.6**, BIC = **2764.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+1235.7093** | 488.5746 | ±977.1491 | **+2.529** | **0.0114** | * |
| **Education: graduate level (vs college)** | **-1.9664** | 0.7600 | ±1.5200 | **-2.587** | **0.0097** | ** |
| **Education: high school or below (vs college)** | **-2.6250** | 1.2865 | ±2.5729 | **-2.040** | **0.0413** | * |
| Site: UCSD (vs UAB) | -1.7401 | 0.9536 | ±1.9072 | -1.825 | 0.0680 | . |
| **Site: UW (vs UAB)** | **-2.6262** | 0.8521 | ±1.7043 | **-3.082** | **0.0021** | ** |
| **Age (years)** | **-0.1392** | 0.0358 | ±0.0715 | **-3.893** | **9.89e-05** | *** |
| **BMI (kg/m2)** | **+0.2515** | 0.0745 | ±0.1489 | **+3.377** | **7.32e-04** | *** |
| **Hypertension** | **+1.9272** | 0.8084 | ±1.6169 | **+2.384** | **0.0171** | * |
| High cholesterol | -0.3179 | 0.7579 | ±1.5159 | -0.419 | 0.6749 |  |
| Kidney disease | -0.1897 | 2.0263 | ±4.0526 | -0.094 | 0.9254 |  |
| **Circulatory disease** | **-1.8304** | 0.9133 | ±1.8266 | **-2.004** | **0.0451** | * |
| **Time 54-250, pooled (%)** | **-11.7224** | 4.8841 | ±9.7681 | **-2.400** | **0.0164** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **403**, R² = **0.2032**, Adj R² = **0.1808**, F-statistic = **9.07** (p = **1.80e-14**), Residual SE = **6.967** on **391** df, AIC = **2720.0**, BIC = **2768.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +448.1619 | 823.8648 | ±1647.7296 | +0.544 | 0.5865 |  |
| **Education: graduate level (vs college)** | **-1.9765** | 0.7653 | ±1.5307 | **-2.583** | **0.0098** | ** |
| **Education: high school or below (vs college)** | **-2.7827** | 1.2806 | ±2.5611 | **-2.173** | **0.0298** | * |
| **Site: UCSD (vs UAB)** | **-1.9278** | 0.9522 | ±1.9045 | **-2.024** | **0.0429** | * |
| **Site: UW (vs UAB)** | **-2.7223** | 0.8562 | ±1.7124 | **-3.179** | **0.0015** | ** |
| **Age (years)** | **-0.1441** | 0.0361 | ±0.0722 | **-3.995** | **6.47e-05** | *** |
| **BMI (kg/m2)** | **+0.2572** | 0.0760 | ±0.1520 | **+3.385** | **7.11e-04** | *** |
| **Hypertension** | **+2.0519** | 0.8088 | ±1.6176 | **+2.537** | **0.0112** | * |
| High cholesterol | -0.3645 | 0.7597 | ±1.5194 | -0.480 | 0.6313 |  |
| Kidney disease | -0.2998 | 2.0234 | ±4.0467 | -0.148 | 0.8822 |  |
| Circulatory disease | -1.7632 | 0.9201 | ±1.8401 | -1.916 | 0.0553 | . |
| Avg. daily time 54-250 (%) | -3.8429 | 8.2378 | ±16.4756 | -0.466 | 0.6409 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1804**, F-statistic = **9.04** (p = **1.98e-14**), Residual SE = **6.968** on **391** df, AIC = **2720.2**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.8937** | 4.0447 | ±8.0893 | **+15.797** | **3.26e-56** | *** |
| **Education: graduate level (vs college)** | **-1.9731** | 0.7675 | ±1.5350 | **-2.571** | **0.0101** | * |
| **Education: high school or below (vs college)** | **-2.7944** | 1.2905 | ±2.5811 | **-2.165** | **0.0304** | * |
| **Site: UCSD (vs UAB)** | **-1.9533** | 0.9540 | ±1.9079 | **-2.048** | **0.0406** | * |
| **Site: UW (vs UAB)** | **-2.7270** | 0.8567 | ±1.7134 | **-3.183** | **0.0015** | ** |
| **Age (years)** | **-0.1447** | 0.0363 | ±0.0727 | **-3.982** | **6.84e-05** | *** |
| **BMI (kg/m2)** | **+0.2579** | 0.0778 | ±0.1557 | **+3.314** | **9.19e-04** | *** |
| **Hypertension** | **+2.0525** | 0.8101 | ±1.6201 | **+2.534** | **0.0113** | * |
| High cholesterol | -0.3628 | 0.7680 | ±1.5360 | -0.472 | 0.6366 |  |
| Kidney disease | -0.3400 | 2.0877 | ±4.1755 | -0.163 | 0.8706 |  |
| Circulatory disease | -1.7160 | 0.9128 | ±1.8255 | -1.880 | 0.0601 | . |
| Time 181-250, pooled (%) | +0.1355 | 1.3650 | ±2.7299 | +0.099 | 0.9209 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **403**, R² = **0.2040**, Adj R² = **0.1816**, F-statistic = **9.11** (p = **1.51e-14**), Residual SE = **6.963** on **391** df, AIC = **2719.6**, BIC = **2767.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.6162** | 3.9353 | ±7.8706 | **+16.165** | **8.83e-59** | *** |
| **Education: graduate level (vs college)** | **-1.9551** | 0.7646 | ±1.5291 | **-2.557** | **0.0106** | * |
| **Education: high school or below (vs college)** | **-2.7283** | 1.2783 | ±2.5565 | **-2.134** | **0.0328** | * |
| **Site: UCSD (vs UAB)** | **-1.9458** | 0.9514 | ±1.9027 | **-2.045** | **0.0408** | * |
| **Site: UW (vs UAB)** | **-2.7397** | 0.8558 | ±1.7117 | **-3.201** | **0.0014** | ** |
| **Age (years)** | **-0.1437** | 0.0362 | ±0.0725 | **-3.967** | **7.29e-05** | *** |
| **BMI (kg/m2)** | **+0.2581** | 0.0768 | ±0.1536 | **+3.361** | **7.76e-04** | *** |
| **Hypertension** | **+2.0294** | 0.8075 | ±1.6149 | **+2.513** | **0.0120** | * |
| High cholesterol | -0.3562 | 0.7615 | ±1.5231 | -0.468 | 0.6399 |  |
| Kidney disease | -0.4038 | 2.0612 | ±4.1224 | -0.196 | 0.8447 |  |
| Circulatory disease | -1.7146 | 0.9076 | ±1.8152 | -1.889 | 0.0589 | . |
| Avg. daily time 181-250 (%) | +0.9622 | 1.2802 | ±2.5603 | +0.752 | 0.4523 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **403**, R² = **0.2028**, Adj R² = **0.1804**, F-statistic = **9.04** (p = **1.99e-14**), Residual SE = **6.968** on **391** df, AIC = **2720.2**, BIC = **2768.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.8991** | 4.0466 | ±8.0933 | **+15.791** | **3.61e-56** | *** |
| **Education: graduate level (vs college)** | **-1.9734** | 0.7674 | ±1.5349 | **-2.571** | **0.0101** | * |
| **Education: high school or below (vs college)** | **-2.7954** | 1.2908 | ±2.5816 | **-2.166** | **0.0303** | * |
| **Site: UCSD (vs UAB)** | **-1.9531** | 0.9541 | ±1.9083 | **-2.047** | **0.0407** | * |
| **Site: UW (vs UAB)** | **-2.7266** | 0.8567 | ±1.7133 | **-3.183** | **0.0015** | ** |
| **Age (years)** | **-0.1447** | 0.0364 | ±0.0727 | **-3.981** | **6.86e-05** | *** |
| **BMI (kg/m2)** | **+0.2579** | 0.0778 | ±0.1556 | **+3.314** | **9.19e-04** | *** |
| **Hypertension** | **+2.0531** | 0.8101 | ±1.6202 | **+2.534** | **0.0113** | * |
| High cholesterol | -0.3633 | 0.7680 | ±1.5359 | -0.473 | 0.6361 |  |
| Kidney disease | -0.3376 | 2.0875 | ±4.1750 | -0.162 | 0.8715 |  |
| Circulatory disease | -1.7161 | 0.9129 | ±1.8257 | -1.880 | 0.0601 | . |
| Time > 180 (%) | +0.1172 | 1.3645 | ±2.7290 | +0.086 | 0.9315 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **403**, R² = **0.2039**, Adj R² = **0.1816**, F-statistic = **9.11** (p = **1.53e-14**), Residual SE = **6.963** on **391** df, AIC = **2719.7**, BIC = **2767.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.6164** | 3.9378 | ±7.8756 | **+16.155** | **1.04e-58** | *** |
| **Education: graduate level (vs college)** | **-1.9556** | 0.7646 | ±1.5292 | **-2.558** | **0.0105** | * |
| **Education: high school or below (vs college)** | **-2.7295** | 1.2786 | ±2.5572 | **-2.135** | **0.0328** | * |
| **Site: UCSD (vs UAB)** | **-1.9447** | 0.9513 | ±1.9026 | **-2.044** | **0.0409** | * |
| **Site: UW (vs UAB)** | **-2.7382** | 0.8556 | ±1.7113 | **-3.200** | **0.0014** | ** |
| **Age (years)** | **-0.1437** | 0.0362 | ±0.0725 | **-3.964** | **7.37e-05** | *** |
| **BMI (kg/m2)** | **+0.2581** | 0.0768 | ±0.1536 | **+3.361** | **7.76e-04** | *** |
| **Hypertension** | **+2.0308** | 0.8076 | ±1.6151 | **+2.515** | **0.0119** | * |
| High cholesterol | -0.3568 | 0.7616 | ±1.5232 | -0.469 | 0.6394 |  |
| Kidney disease | -0.4019 | 2.0610 | ±4.1220 | -0.195 | 0.8454 |  |
| Circulatory disease | -1.7147 | 0.9078 | ±1.8155 | -1.889 | 0.0589 | . |
| Avg. daily time > 180 (%) | +0.9379 | 1.2791 | ±2.5582 | +0.733 | 0.4634 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 403)
**Regression Call / Formula**: `hr_resting_proxy ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **403**, R² = **0.2099**, Adj R² = **0.1876**, F-statistic = **9.44** (p = **4.05e-15**), Residual SE = **6.938** on **391** df, AIC = **2716.7**, BIC = **2764.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+63.3503** | 3.7715 | ±7.5429 | **+16.797** | **2.55e-63** | *** |
| **Education: graduate level (vs college)** | **-1.8798** | 0.7559 | ±1.5118 | **-2.487** | **0.0129** | * |
| **Education: high school or below (vs college)** | **-2.7856** | 1.2628 | ±2.5256 | **-2.206** | **0.0274** | * |
| **Site: UCSD (vs UAB)** | **-2.0097** | 0.9432 | ±1.8864 | **-2.131** | **0.0331** | * |
| **Site: UW (vs UAB)** | **-2.8081** | 0.8584 | ±1.7168 | **-3.271** | **0.0011** | ** |
| **Age (years)** | **-0.1342** | 0.0354 | ±0.0709 | **-3.787** | **1.53e-04** | *** |
| **BMI (kg/m2)** | **+0.2514** | 0.0750 | ±0.1499 | **+3.354** | **7.96e-04** | *** |
| **Hypertension** | **+1.9145** | 0.8018 | ±1.6037 | **+2.388** | **0.0170** | * |
| High cholesterol | -0.4137 | 0.7583 | ±1.5165 | -0.546 | 0.5854 |  |
| Kidney disease | -0.4227 | 1.9953 | ±3.9907 | -0.212 | 0.8322 |  |
| Circulatory disease | -1.6205 | 0.9101 | ±1.8202 | -1.781 | 0.0750 | . |
| Nocturnal time > 180 (%) | +1.7799 | 1.0782 | ±2.1563 | +1.651 | 0.0988 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Total sleep time per night (min)  (domain: Wearable activity; outcome sample N = 409; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **409**, R² = **0.0820**, Adj R² = **0.0590**, F-statistic = **3.56** (p = **1.58e-04**), Residual SE = **64.885** on **398** df, AIC = **4584.7**, BIC = **4628.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.9589** | 26.5970 | ±53.1940 | **+15.075** | **2.35e-51** | *** |
| Education: graduate level (vs college) | +7.2130 | 6.6967 | ±13.3934 | +1.077 | 0.2814 |  |
| Education: high school or below (vs college) | -3.1173 | 14.6166 | ±29.2333 | -0.213 | 0.8311 |  |
| Site: UCSD (vs UAB) | -10.9041 | 8.4979 | ±16.9959 | -1.283 | 0.1994 |  |
| Site: UW (vs UAB) | -5.9147 | 7.9186 | ±15.8371 | -0.747 | 0.4551 |  |
| Age (years) | +0.2558 | 0.3261 | ±0.6522 | +0.784 | 0.4328 |  |
| **BMI (kg/m2)** | **-1.1942** | 0.4800 | ±0.9599 | **-2.488** | **0.0128** | * |
| **Hypertension** | **-23.6810** | 7.3750 | ±14.7501 | **-3.211** | **0.0013** | ** |
| High cholesterol | -0.4049 | 6.7928 | ±13.5855 | -0.060 | 0.9525 |  |
| **Kidney disease** | **-36.9225** | 18.7213 | ±37.4427 | **-1.972** | **0.0486** | * |
| Circulatory disease | +10.6704 | 12.0313 | ±24.0627 | +0.887 | 0.3751 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **409**, R² = **0.1036**, Adj R² = **0.0787**, F-statistic = **4.17** (p = **7.57e-06**), Residual SE = **64.199** on **397** df, AIC = **4577.0**, BIC = **4625.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+575.5814** | 58.9663 | ±117.9325 | **+9.761** | **1.65e-22** | *** |
| Education: graduate level (vs college) | +5.8111 | 6.6544 | ±13.3088 | +0.873 | 0.3825 |  |
| Education: high school or below (vs college) | -1.3205 | 14.4665 | ±28.9330 | -0.091 | 0.9273 |  |
| Site: UCSD (vs UAB) | -12.2613 | 8.4295 | ±16.8589 | -1.455 | 0.1458 |  |
| Site: UW (vs UAB) | -7.5798 | 7.8358 | ±15.6715 | -0.967 | 0.3334 |  |
| Age (years) | +0.3488 | 0.3243 | ±0.6485 | +1.076 | 0.2821 |  |
| **BMI (kg/m2)** | **-1.0583** | 0.4461 | ±0.8922 | **-2.372** | **0.0177** | * |
| **Hypertension** | **-21.5882** | 7.3824 | ±14.7647 | **-2.924** | **0.0035** | ** |
| High cholesterol | +4.5570 | 6.8286 | ±13.6572 | +0.667 | 0.5046 |  |
| **Kidney disease** | **-38.9595** | 17.8352 | ±35.6704 | **-2.184** | **0.0289** | * |
| Circulatory disease | +9.2986 | 11.5178 | ±23.0356 | +0.807 | 0.4195 |  |
| **HbA1c (%)** | **-33.4365** | 10.3429 | ±20.6858 | **-3.233** | **0.0012** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **409**, R² = **0.0917**, Adj R² = **0.0665**, F-statistic = **3.64** (p = **6.15e-05**), Residual SE = **64.623** on **397** df, AIC = **4582.4**, BIC = **4630.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+502.3269** | 53.6770 | ±107.3540 | **+9.358** | **8.10e-21** | *** |
| Education: graduate level (vs college) | +6.9460 | 6.6742 | ±13.3484 | +1.041 | 0.2980 |  |
| Education: high school or below (vs college) | -4.5567 | 14.8940 | ±29.7881 | -0.306 | 0.7597 |  |
| Site: UCSD (vs UAB) | -10.2376 | 8.4206 | ±16.8412 | -1.216 | 0.2241 |  |
| Site: UW (vs UAB) | -5.0624 | 7.8910 | ±15.7819 | -0.642 | 0.5212 |  |
| Age (years) | +0.2280 | 0.3218 | ±0.6436 | +0.708 | 0.4787 |  |
| **BMI (kg/m2)** | **-1.1358** | 0.4768 | ±0.9536 | **-2.382** | **0.0172** | * |
| **Hypertension** | **-22.6211** | 7.3650 | ±14.7301 | **-3.071** | **0.0021** | ** |
| High cholesterol | -0.9597 | 6.7658 | ±13.5316 | -0.142 | 0.8872 |  |
| **Kidney disease** | **-36.8159** | 18.6439 | ±37.2878 | **-1.975** | **0.0483** | * |
| Circulatory disease | +10.7409 | 11.9756 | ±23.9512 | +0.897 | 0.3698 |  |
| **Mean glucose (mg/dL)** | **-0.8919** | 0.4252 | ±0.8503 | **-2.098** | **0.0359** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **409**, R² = **0.0917**, Adj R² = **0.0665**, F-statistic = **3.64** (p = **6.15e-05**), Residual SE = **64.623** on **397** df, AIC = **4582.4**, BIC = **4630.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+625.7418** | 108.8455 | ±217.6911 | **+5.749** | **8.98e-09** | *** |
| Education: graduate level (vs college) | +6.9460 | 6.6742 | ±13.3484 | +1.041 | 0.2980 |  |
| Education: high school or below (vs college) | -4.5567 | 14.8940 | ±29.7881 | -0.306 | 0.7597 |  |
| Site: UCSD (vs UAB) | -10.2376 | 8.4206 | ±16.8412 | -1.216 | 0.2241 |  |
| Site: UW (vs UAB) | -5.0624 | 7.8910 | ±15.7819 | -0.642 | 0.5212 |  |
| Age (years) | +0.2280 | 0.3218 | ±0.6436 | +0.708 | 0.4787 |  |
| **BMI (kg/m2)** | **-1.1358** | 0.4768 | ±0.9536 | **-2.382** | **0.0172** | * |
| **Hypertension** | **-22.6211** | 7.3650 | ±14.7301 | **-3.071** | **0.0021** | ** |
| High cholesterol | -0.9597 | 6.7658 | ±13.5316 | -0.142 | 0.8872 |  |
| **Kidney disease** | **-36.8159** | 18.6439 | ±37.2878 | **-1.975** | **0.0483** | * |
| Circulatory disease | +10.7409 | 11.9756 | ±23.9512 | +0.897 | 0.3698 |  |
| **GMI (%)** | **-37.2855** | 17.7746 | ±35.5491 | **-2.098** | **0.0359** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **409**, R² = **0.0946**, Adj R² = **0.0695**, F-statistic = **3.77** (p = **3.71e-05**), Residual SE = **64.519** on **397** df, AIC = **4581.1**, BIC = **4629.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+494.5796** | 45.7576 | ±91.5153 | **+10.809** | **3.13e-27** | *** |
| Education: graduate level (vs college) | +6.4574 | 6.6974 | ±13.3948 | +0.964 | 0.3350 |  |
| Education: high school or below (vs college) | -4.6226 | 14.7669 | ±29.5337 | -0.313 | 0.7543 |  |
| Site: UCSD (vs UAB) | -9.1104 | 8.4328 | ±16.8655 | -1.080 | 0.2800 |  |
| Site: UW (vs UAB) | -4.3834 | 7.9184 | ±15.8369 | -0.554 | 0.5799 |  |
| Age (years) | +0.1363 | 0.3186 | ±0.6372 | +0.428 | 0.6689 |  |
| **BMI (kg/m2)** | **-1.0239** | 0.4574 | ±0.9149 | **-2.238** | **0.0252** | * |
| **Hypertension** | **-22.2357** | 7.3657 | ±14.7314 | **-3.019** | **0.0025** | ** |
| High cholesterol | -0.5549 | 6.7810 | ±13.5620 | -0.082 | 0.9348 |  |
| **Kidney disease** | **-38.9327** | 18.8320 | ±37.6640 | **-2.067** | **0.0387** | * |
| Circulatory disease | +9.9938 | 12.0296 | ±24.0592 | +0.831 | 0.4061 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.8042** | 0.3465 | ±0.6929 | **-2.321** | **0.0203** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **409**, R² = **0.0821**, Adj R² = **0.0566**, F-statistic = **3.23** (p = **3.14e-04**), Residual SE = **64.965** on **397** df, AIC = **4586.7**, BIC = **4634.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.0020** | 34.8858 | ±69.7717 | **+11.581** | **5.16e-31** | *** |
| Education: graduate level (vs college) | +7.1320 | 6.8646 | ±13.7292 | +1.039 | 0.2988 |  |
| Education: high school or below (vs college) | -3.1180 | 14.6374 | ±29.2749 | -0.213 | 0.8313 |  |
| Site: UCSD (vs UAB) | -10.9688 | 8.4671 | ±16.9341 | -1.295 | 0.1952 |  |
| Site: UW (vs UAB) | -5.9921 | 7.9899 | ±15.9799 | -0.750 | 0.4533 |  |
| Age (years) | +0.2566 | 0.3284 | ±0.6567 | +0.782 | 0.4345 |  |
| **BMI (kg/m2)** | **-1.1919** | 0.4803 | ±0.9606 | **-2.482** | **0.0131** | * |
| **Hypertension** | **-23.6226** | 7.3469 | ±14.6937 | **-3.215** | **0.0013** | ** |
| High cholesterol | -0.4624 | 6.8043 | ±13.6086 | -0.068 | 0.9458 |  |
| Kidney disease | -36.7146 | 18.7827 | ±37.5654 | -1.955 | 0.0506 | . |
| Circulatory disease | +10.6941 | 12.0259 | ±24.0518 | +0.889 | 0.3739 |  |
| Glucose SD, pooled (mg/dL) | -0.1834 | 1.4635 | ±2.9270 | -0.125 | 0.9003 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **409**, R² = **0.0821**, Adj R² = **0.0566**, F-statistic = **3.23** (p = **3.14e-04**), Residual SE = **64.965** on **397** df, AIC = **4586.7**, BIC = **4634.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+403.7727** | 32.8701 | ±65.7402 | **+12.284** | **1.11e-34** | *** |
| Education: graduate level (vs college) | +7.1207 | 6.8744 | ±13.7488 | +1.036 | 0.3003 |  |
| Education: high school or below (vs college) | -3.1476 | 14.6261 | ±29.2522 | -0.215 | 0.8296 |  |
| Site: UCSD (vs UAB) | -10.9636 | 8.4738 | ±16.9475 | -1.294 | 0.1957 |  |
| Site: UW (vs UAB) | -5.9889 | 7.9627 | ±15.9255 | -0.752 | 0.4520 |  |
| Age (years) | +0.2571 | 0.3288 | ±0.6577 | +0.782 | 0.4343 |  |
| **BMI (kg/m2)** | **-1.1903** | 0.4805 | ±0.9610 | **-2.477** | **0.0132** | * |
| **Hypertension** | **-23.6502** | 7.3666 | ±14.7333 | **-3.210** | **0.0013** | ** |
| High cholesterol | -0.4525 | 6.8111 | ±13.6222 | -0.066 | 0.9470 |  |
| Kidney disease | -36.6947 | 18.8098 | ±37.6197 | -1.951 | 0.0511 | . |
| Circulatory disease | +10.6656 | 12.0530 | ±24.1060 | +0.885 | 0.3762 |  |
| Avg. daily SD (mg/dL) | -0.1891 | 1.4339 | ±2.8677 | -0.132 | 0.8951 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **409**, R² = **0.0833**, Adj R² = **0.0579**, F-statistic = **3.28** (p = **2.56e-04**), Residual SE = **64.922** on **397** df, AIC = **4586.2**, BIC = **4634.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+384.6354** | 34.4013 | ±68.8026 | **+11.181** | **5.06e-29** | *** |
| Education: graduate level (vs college) | +7.6092 | 6.8124 | ±13.6248 | +1.117 | 0.2640 |  |
| Education: high school or below (vs college) | -3.3340 | 14.7134 | ±29.4269 | -0.227 | 0.8207 |  |
| Site: UCSD (vs UAB) | -10.4627 | 8.4603 | ±16.9206 | -1.237 | 0.2162 |  |
| Site: UW (vs UAB) | -5.3712 | 8.0329 | ±16.0658 | -0.669 | 0.5037 |  |
| Age (years) | +0.2472 | 0.3274 | ±0.6549 | +0.755 | 0.4503 |  |
| **BMI (kg/m2)** | **-1.1967** | 0.4824 | ±0.9647 | **-2.481** | **0.0131** | * |
| **Hypertension** | **-23.8118** | 7.3813 | ±14.7626 | **-3.226** | **0.0013** | ** |
| High cholesterol | -0.1688 | 6.8070 | ±13.6139 | -0.025 | 0.9802 |  |
| **Kidney disease** | **-38.0100** | 18.8914 | ±37.7828 | **-2.012** | **0.0442** | * |
| Circulatory disease | +10.5381 | 12.1051 | ±24.2103 | +0.871 | 0.3840 |  |
| CV (%) | +1.1124 | 1.5570 | ±3.1140 | +0.714 | 0.4749 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **409**, R² = **0.0833**, Adj R² = **0.0579**, F-statistic = **3.28** (p = **2.54e-04**), Residual SE = **64.920** on **397** df, AIC = **4586.2**, BIC = **4634.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+417.0004** | 35.4017 | ±70.8033 | **+11.779** | **5.00e-32** | *** |
| Education: graduate level (vs college) | +7.6569 | 6.8240 | ±13.6480 | +1.122 | 0.2618 |  |
| Education: high school or below (vs college) | -3.3789 | 14.7219 | ±29.4438 | -0.230 | 0.8185 |  |
| Site: UCSD (vs UAB) | -10.5004 | 8.4529 | ±16.9058 | -1.242 | 0.2142 |  |
| Site: UW (vs UAB) | -5.4146 | 8.0157 | ±16.0313 | -0.676 | 0.4994 |  |
| Age (years) | +0.2483 | 0.3272 | ±0.6544 | +0.759 | 0.4479 |  |
| **BMI (kg/m2)** | **-1.1963** | 0.4817 | ±0.9633 | **-2.484** | **0.0130** | * |
| **Hypertension** | **-23.8214** | 7.3795 | ±14.7590 | **-3.228** | **0.0012** | ** |
| High cholesterol | -0.1407 | 6.8153 | ±13.6306 | -0.021 | 0.9835 |  |
| **Kidney disease** | **-37.7068** | 18.8152 | ±37.6304 | **-2.004** | **0.0451** | * |
| Circulatory disease | +10.6262 | 12.1140 | ±24.2280 | +0.877 | 0.3804 |  |
| Mean / SD ratio | -2.3162 | 3.1876 | ±6.3752 | -0.727 | 0.4675 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **409**, R² = **0.0823**, Adj R² = **0.0569**, F-statistic = **3.24** (p = **3.03e-04**), Residual SE = **64.957** on **397** df, AIC = **4586.6**, BIC = **4634.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+407.4599** | 34.0927 | ±68.1854 | **+11.952** | **6.37e-33** | *** |
| Education: graduate level (vs college) | +7.4248 | 6.8254 | ±13.6509 | +1.088 | 0.2767 |  |
| Education: high school or below (vs college) | -3.1826 | 14.6892 | ±29.3785 | -0.217 | 0.8285 |  |
| Site: UCSD (vs UAB) | -10.7505 | 8.4752 | ±16.9504 | -1.268 | 0.2046 |  |
| Site: UW (vs UAB) | -5.7050 | 7.9958 | ±15.9916 | -0.714 | 0.4755 |  |
| Age (years) | +0.2512 | 0.3286 | ±0.6572 | +0.765 | 0.4445 |  |
| **BMI (kg/m2)** | **-1.1996** | 0.4823 | ±0.9646 | **-2.487** | **0.0129** | * |
| **Hypertension** | **-23.6823** | 7.3932 | ±14.7865 | **-3.203** | **0.0014** | ** |
| High cholesterol | -0.3416 | 6.8145 | ±13.6289 | -0.050 | 0.9600 |  |
| **Kidney disease** | **-37.3377** | 18.7542 | ±37.5084 | **-1.991** | **0.0465** | * |
| Circulatory disease | +10.7557 | 12.1018 | ±24.2037 | +0.889 | 0.3741 |  |
| Avg. daily mean/SD | -0.8044 | 2.4194 | ±4.8388 | -0.332 | 0.7395 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **409**, R² = **0.0947**, Adj R² = **0.0697**, F-statistic = **3.78** (p = **3.64e-05**), Residual SE = **64.515** on **397** df, AIC = **4581.0**, BIC = **4629.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+450.8336** | 34.0157 | ±68.0314 | **+13.254** | **4.30e-40** | *** |
| Education: graduate level (vs college) | +7.1015 | 6.6611 | ±13.3223 | +1.066 | 0.2864 |  |
| Education: high school or below (vs college) | -0.5440 | 14.2306 | ±28.4612 | -0.038 | 0.9695 |  |
| Site: UCSD (vs UAB) | -11.6596 | 8.4376 | ±16.8753 | -1.382 | 0.1670 |  |
| Site: UW (vs UAB) | -7.8184 | 7.9167 | ±15.8334 | -0.988 | 0.3234 |  |
| Age (years) | +0.1929 | 0.3247 | ±0.6494 | +0.594 | 0.5525 |  |
| **BMI (kg/m2)** | **-1.2391** | 0.4671 | ±0.9342 | **-2.653** | **0.0080** | ** |
| **Hypertension** | **-24.3127** | 7.3947 | ±14.7894 | **-3.288** | **0.0010** | ** |
| High cholesterol | +0.3318 | 6.7390 | ±13.4780 | +0.049 | 0.9607 |  |
| Kidney disease | -34.1588 | 18.8238 | ±37.6475 | -1.815 | 0.0696 | . |
| Circulatory disease | +10.0733 | 11.9085 | ±23.8169 | +0.846 | 0.3976 |  |
| **MAG (mg/dL/h)** | **-1.2941** | 0.5594 | ±1.1187 | **-2.314** | **0.0207** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **409**, R² = **0.0821**, Adj R² = **0.0567**, F-statistic = **3.23** (p = **3.13e-04**), Residual SE = **64.964** on **397** df, AIC = **4586.7**, BIC = **4634.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+396.9038** | 37.6347 | ±75.2694 | **+10.546** | **5.29e-26** | *** |
| Education: graduate level (vs college) | +7.2735 | 6.8045 | ±13.6091 | +1.069 | 0.2851 |  |
| Education: high school or below (vs college) | -3.1419 | 14.6676 | ±29.3352 | -0.214 | 0.8304 |  |
| Site: UCSD (vs UAB) | -10.8297 | 8.5146 | ±17.0292 | -1.272 | 0.2034 |  |
| Site: UW (vs UAB) | -5.8211 | 8.0000 | ±16.0000 | -0.728 | 0.4668 |  |
| Age (years) | +0.2546 | 0.3281 | ±0.6561 | +0.776 | 0.4377 |  |
| **BMI (kg/m2)** | **-1.1884** | 0.4840 | ±0.9680 | **-2.455** | **0.0141** | * |
| **Hypertension** | **-23.6264** | 7.4701 | ±14.9401 | **-3.163** | **0.0016** | ** |
| High cholesterol | -0.3948 | 6.8152 | ±13.6304 | -0.058 | 0.9538 |  |
| **Kidney disease** | **-37.1259** | 18.8351 | ±37.6703 | **-1.971** | **0.0487** | * |
| Circulatory disease | +10.6703 | 12.0707 | ±24.1413 | +0.884 | 0.3767 |  |
| Avg. daily range (mg/dL) | +0.0483 | 0.3252 | ±0.6505 | +0.149 | 0.8819 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **409**, R² = **0.0820**, Adj R² = **0.0566**, F-statistic = **3.22** (p = **3.16e-04**), Residual SE = **64.967** on **397** df, AIC = **4586.7**, BIC = **4634.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.6042** | 27.6921 | ±55.3842 | **+14.466** | **1.98e-47** | *** |
| Education: graduate level (vs college) | +7.2081 | 6.7091 | ±13.4181 | +1.074 | 0.2827 |  |
| Education: high school or below (vs college) | -3.1461 | 14.7058 | ±29.4116 | -0.214 | 0.8306 |  |
| Site: UCSD (vs UAB) | -10.8846 | 8.4902 | ±16.9804 | -1.282 | 0.1998 |  |
| Site: UW (vs UAB) | -5.9184 | 7.9399 | ±15.8798 | -0.745 | 0.4560 |  |
| Age (years) | +0.2561 | 0.3268 | ±0.6536 | +0.784 | 0.4333 |  |
| **BMI (kg/m2)** | **-1.1945** | 0.4812 | ±0.9623 | **-2.483** | **0.0130** | * |
| **Hypertension** | **-23.7075** | 7.4115 | ±14.8229 | **-3.199** | **0.0014** | ** |
| High cholesterol | -0.4136 | 6.8336 | ±13.6673 | -0.061 | 0.9517 |  |
| **Kidney disease** | **-36.9173** | 18.7782 | ±37.5563 | **-1.966** | **0.0493** | * |
| Circulatory disease | +10.6418 | 12.0861 | ±24.1723 | +0.880 | 0.3786 |  |
| SD of daily means (mg/dL) | +0.0704 | 1.6248 | ±3.2496 | +0.043 | 0.9654 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **409**, R² = **0.0829**, Adj R² = **0.0575**, F-statistic = **3.26** (p = **2.74e-04**), Residual SE = **64.936** on **397** df, AIC = **4586.4**, BIC = **4634.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1062.0916 | 1150.7598 | ±2301.5195 | +0.923 | 0.3560 |  |
| Education: graduate level (vs college) | +7.4185 | 6.7988 | ±13.5976 | +1.091 | 0.2752 |  |
| Education: high school or below (vs college) | -3.0488 | 14.6731 | ±29.3462 | -0.208 | 0.8354 |  |
| Site: UCSD (vs UAB) | -10.6574 | 8.4674 | ±16.9348 | -1.259 | 0.2082 |  |
| Site: UW (vs UAB) | -5.7381 | 7.9483 | ±15.8966 | -0.722 | 0.4703 |  |
| Age (years) | +0.2599 | 0.3252 | ±0.6503 | +0.799 | 0.4241 |  |
| **BMI (kg/m2)** | **-1.1852** | 0.4753 | ±0.9507 | **-2.494** | **0.0126** | * |
| **Hypertension** | **-23.7306** | 7.3860 | ±14.7720 | **-3.213** | **0.0013** | ** |
| High cholesterol | -0.4338 | 6.8098 | ±13.6196 | -0.064 | 0.9492 |  |
| **Kidney disease** | **-37.3901** | 18.8019 | ±37.6038 | **-1.989** | **0.0467** | * |
| Circulatory disease | +10.7962 | 12.1528 | ±24.3056 | +0.888 | 0.3743 |  |
| Time in range 70-180, pooled (%) | -6.6490 | 11.5672 | ±23.1344 | -0.575 | 0.5654 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **409**, R² = **0.0833**, Adj R² = **0.0579**, F-statistic = **3.28** (p = **2.56e-04**), Residual SE = **64.921** on **397** df, AIC = **4586.2**, BIC = **4634.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1176.2689 | 1087.3562 | ±2174.7123 | +1.082 | 0.2794 |  |
| Education: graduate level (vs college) | +7.5541 | 6.8262 | ±13.6525 | +1.107 | 0.2685 |  |
| Education: high school or below (vs college) | -2.9217 | 14.6717 | ±29.3434 | -0.199 | 0.8422 |  |
| Site: UCSD (vs UAB) | -10.7359 | 8.4872 | ±16.9744 | -1.265 | 0.2059 |  |
| Site: UW (vs UAB) | -5.9179 | 7.9553 | ±15.9107 | -0.744 | 0.4569 |  |
| Age (years) | +0.2627 | 0.3258 | ±0.6516 | +0.806 | 0.4202 |  |
| **BMI (kg/m2)** | **-1.1897** | 0.4796 | ±0.9591 | **-2.481** | **0.0131** | * |
| **Hypertension** | **-23.3985** | 7.4549 | ±14.9097 | **-3.139** | **0.0017** | ** |
| High cholesterol | -0.5823 | 6.7995 | ±13.5990 | -0.086 | 0.9318 |  |
| **Kidney disease** | **-37.4094** | 18.7974 | ±37.5949 | **-1.990** | **0.0466** | * |
| Circulatory disease | +10.5156 | 12.1452 | ±24.2904 | +0.866 | 0.3866 |  |
| Avg. daily time in range 70-180 (%) | -7.7917 | 10.9199 | ±21.8398 | -0.714 | 0.4755 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **409**, R² = **0.0824**, Adj R² = **0.0570**, F-statistic = **3.24** (p = **2.97e-04**), Residual SE = **64.953** on **397** df, AIC = **4586.6**, BIC = **4634.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+399.9777** | 26.9082 | ±53.8165 | **+14.865** | **5.60e-50** | *** |
| Education: graduate level (vs college) | +7.2182 | 6.7106 | ±13.4213 | +1.076 | 0.2821 |  |
| Education: high school or below (vs college) | -2.9679 | 14.6708 | ±29.3416 | -0.202 | 0.8397 |  |
| Site: UCSD (vs UAB) | -10.3446 | 8.6834 | ±17.3667 | -1.191 | 0.2335 |  |
| Site: UW (vs UAB) | -5.6149 | 7.9897 | ±15.9795 | -0.703 | 0.4822 |  |
| Age (years) | +0.2577 | 0.3264 | ±0.6528 | +0.790 | 0.4298 |  |
| **BMI (kg/m2)** | **-1.1953** | 0.4816 | ±0.9631 | **-2.482** | **0.0131** | * |
| **Hypertension** | **-23.8356** | 7.3961 | ±14.7923 | **-3.223** | **0.0013** | ** |
| High cholesterol | -0.3847 | 6.8045 | ±13.6090 | -0.057 | 0.9549 |  |
| Kidney disease | -36.5334 | 18.8353 | ±37.6705 | -1.940 | 0.0524 | . |
| Circulatory disease | +10.5587 | 12.0622 | ±24.1243 | +0.875 | 0.3814 |  |
| Any reading < 54 during wear (0/1) | +3.4669 | 7.4397 | ±14.8795 | +0.466 | 0.6412 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **409**, R² = **0.0821**, Adj R² = **0.0567**, F-statistic = **3.23** (p = **3.11e-04**), Residual SE = **64.963** on **397** df, AIC = **4586.7**, BIC = **4634.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.5646** | 26.8211 | ±53.6422 | **+14.935** | **1.96e-50** | *** |
| Education: graduate level (vs college) | +7.2141 | 6.7123 | ±13.4246 | +1.075 | 0.2825 |  |
| Education: high school or below (vs college) | -2.9474 | 14.6460 | ±29.2920 | -0.201 | 0.8405 |  |
| Site: UCSD (vs UAB) | -10.6678 | 8.6345 | ±17.2691 | -1.235 | 0.2167 |  |
| Site: UW (vs UAB) | -5.8096 | 7.9711 | ±15.9421 | -0.729 | 0.4661 |  |
| Age (years) | +0.2606 | 0.3275 | ±0.6550 | +0.796 | 0.4262 |  |
| **BMI (kg/m2)** | **-1.2022** | 0.4835 | ±0.9669 | **-2.487** | **0.0129** | * |
| **Hypertension** | **-23.8195** | 7.4057 | ±14.8115 | **-3.216** | **0.0013** | ** |
| High cholesterol | -0.3464 | 6.8039 | ±13.6078 | -0.051 | 0.9594 |  |
| Kidney disease | -36.7636 | 18.7680 | ±37.5360 | -1.959 | 0.0501 | . |
| Circulatory disease | +10.5616 | 12.0572 | ±24.1144 | +0.876 | 0.3811 |  |
| Time < 54 (%) | +12.7256 | 52.9914 | ±105.9829 | +0.240 | 0.8102 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **409**, R² = **0.0836**, Adj R² = **0.0582**, F-statistic = **3.29** (p = **2.42e-04**), Residual SE = **64.909** on **397** df, AIC = **4586.0**, BIC = **4634.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+400.3898** | 26.7431 | ±53.4863 | **+14.972** | **1.12e-50** | *** |
| Education: graduate level (vs college) | +7.1874 | 6.7045 | ±13.4090 | +1.072 | 0.2837 |  |
| Education: high school or below (vs college) | -2.8365 | 14.6359 | ±29.2718 | -0.194 | 0.8463 |  |
| Site: UCSD (vs UAB) | -10.4951 | 8.5207 | ±17.0414 | -1.232 | 0.2181 |  |
| Site: UW (vs UAB) | -5.8945 | 7.9213 | ±15.8427 | -0.744 | 0.4568 |  |
| Age (years) | +0.2599 | 0.3262 | ±0.6524 | +0.797 | 0.4255 |  |
| **BMI (kg/m2)** | **-1.2093** | 0.4846 | ±0.9691 | **-2.496** | **0.0126** | * |
| **Hypertension** | **-23.7823** | 7.3809 | ±14.7619 | **-3.222** | **0.0013** | ** |
| High cholesterol | -0.3453 | 6.8061 | ±13.6121 | -0.051 | 0.9595 |  |
| Kidney disease | -36.5471 | 18.7888 | ±37.5775 | -1.945 | 0.0518 | . |
| Circulatory disease | +9.9452 | 12.0700 | ±24.1400 | +0.824 | 0.4100 |  |
| Avg. daily time < 54 (%) | +64.9196 | 62.5331 | ±125.0661 | +1.038 | 0.2992 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **409**, R² = **0.1004**, Adj R² = **0.0754**, F-statistic = **4.03** (p = **1.35e-05**), Residual SE = **64.314** on **397** df, AIC = **4578.5**, BIC = **4626.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+392.9195** | 27.1176 | ±54.2352 | **+14.489** | **1.41e-47** | *** |
| Education: graduate level (vs college) | +7.9489 | 6.6737 | ±13.3473 | +1.191 | 0.2336 |  |
| Education: high school or below (vs college) | -6.1101 | 14.7562 | ±29.5125 | -0.414 | 0.6788 |  |
| Site: UCSD (vs UAB) | -10.1144 | 8.4316 | ±16.8632 | -1.200 | 0.2303 |  |
| Site: UW (vs UAB) | -4.7305 | 7.9000 | ±15.8001 | -0.599 | 0.5493 |  |
| Age (years) | +0.2550 | 0.3240 | ±0.6481 | +0.787 | 0.4313 |  |
| **BMI (kg/m2)** | **-1.1840** | 0.4865 | ±0.9729 | **-2.434** | **0.0149** | * |
| **Hypertension** | **-22.2120** | 7.3470 | ±14.6939 | **-3.023** | **0.0025** | ** |
| High cholesterol | -2.3640 | 6.6943 | ±13.3887 | -0.353 | 0.7240 |  |
| Kidney disease | -35.3093 | 19.0061 | ±38.0121 | -1.858 | 0.0632 | . |
| Circulatory disease | +11.1881 | 12.0568 | ±24.1136 | +0.928 | 0.3534 |  |
| **Time 54-69, pooled (%)** | **+50.0786** | 17.2263 | ±34.4526 | **+2.907** | **0.0036** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **409**, R² = **0.0987**, Adj R² = **0.0737**, F-statistic = **3.95** (p = **1.81e-05**), Residual SE = **64.373** on **397** df, AIC = **4579.2**, BIC = **4627.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.0703** | 26.9885 | ±53.9770 | **+14.638** | **1.60e-48** | *** |
| Education: graduate level (vs college) | +8.3527 | 6.6881 | ±13.3761 | +1.249 | 0.2117 |  |
| Education: high school or below (vs college) | -5.8212 | 14.8233 | ±29.6466 | -0.393 | 0.6945 |  |
| Site: UCSD (vs UAB) | -10.7798 | 8.4386 | ±16.8772 | -1.277 | 0.2014 |  |
| Site: UW (vs UAB) | -5.5393 | 7.8719 | ±15.7437 | -0.704 | 0.4816 |  |
| Age (years) | +0.2403 | 0.3259 | ±0.6518 | +0.737 | 0.4610 |  |
| **BMI (kg/m2)** | **-1.1932** | 0.4843 | ±0.9687 | **-2.463** | **0.0138** | * |
| **Hypertension** | **-20.9835** | 7.4710 | ±14.9420 | **-2.809** | **0.0050** | ** |
| High cholesterol | -1.9334 | 6.6986 | ±13.3971 | -0.289 | 0.7729 |  |
| Kidney disease | -35.6575 | 19.0144 | ±38.0289 | -1.875 | 0.0608 | . |
| Circulatory disease | +10.1970 | 12.0726 | ±24.1453 | +0.845 | 0.3983 |  |
| **Avg. daily time 54-69 (%)** | **+48.4532** | 17.9374 | ±35.8748 | **+2.701** | **0.0069** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **409**, R² = **0.0970**, Adj R² = **0.0720**, F-statistic = **3.88** (p = **2.45e-05**), Residual SE = **64.434** on **397** df, AIC = **4580.0**, BIC = **4628.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+393.2998** | 27.2650 | ±54.5300 | **+14.425** | **3.60e-47** | *** |
| Education: graduate level (vs college) | +7.8043 | 6.6753 | ±13.3507 | +1.169 | 0.2424 |  |
| Education: high school or below (vs college) | -4.9735 | 14.7379 | ±29.4759 | -0.337 | 0.7358 |  |
| Site: UCSD (vs UAB) | -9.5311 | 8.4240 | ±16.8480 | -1.131 | 0.2579 |  |
| Site: UW (vs UAB) | -4.6389 | 7.9292 | ±15.8583 | -0.585 | 0.5585 |  |
| Age (years) | +0.2703 | 0.3248 | ±0.6495 | +0.832 | 0.4052 |  |
| **BMI (kg/m2)** | **-1.2113** | 0.4906 | ±0.9811 | **-2.469** | **0.0135** | * |
| **Hypertension** | **-22.9432** | 7.3382 | ±14.6765 | **-3.127** | **0.0018** | ** |
| High cholesterol | -1.7855 | 6.7106 | ±13.4212 | -0.266 | 0.7902 |  |
| Kidney disease | -35.1349 | 18.9855 | ±37.9711 | -1.851 | 0.0642 | . |
| Circulatory disease | +10.7417 | 12.0260 | ±24.0520 | +0.893 | 0.3717 |  |
| **Time < 70 (%)** | **+39.9914** | 14.8149 | ±29.6298 | **+2.699** | **0.0069** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **409**, R² = **0.0979**, Adj R² = **0.0729**, F-statistic = **3.92** (p = **2.10e-05**), Residual SE = **64.403** on **397** df, AIC = **4579.6**, BIC = **4627.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+395.3686** | 27.0182 | ±54.0363 | **+14.633** | **1.72e-48** | *** |
| Education: graduate level (vs college) | +8.2053 | 6.6798 | ±13.3597 | +1.228 | 0.2193 |  |
| Education: high school or below (vs college) | -5.3260 | 14.8101 | ±29.6201 | -0.360 | 0.7191 |  |
| Site: UCSD (vs UAB) | -10.5238 | 8.4206 | ±16.8413 | -1.250 | 0.2114 |  |
| Site: UW (vs UAB) | -5.5690 | 7.8748 | ±15.7495 | -0.707 | 0.4794 |  |
| Age (years) | +0.2448 | 0.3257 | ±0.6514 | +0.752 | 0.4523 |  |
| **BMI (kg/m2)** | **-1.2033** | 0.4860 | ±0.9720 | **-2.476** | **0.0133** | * |
| **Hypertension** | **-21.3593** | 7.4558 | ±14.9115 | **-2.865** | **0.0042** | ** |
| High cholesterol | -1.7190 | 6.7095 | ±13.4190 | -0.256 | 0.7978 |  |
| Kidney disease | -35.5543 | 19.0155 | ±38.0310 | -1.870 | 0.0615 | . |
| Circulatory disease | +9.7720 | 12.0603 | ±24.1206 | +0.810 | 0.4178 |  |
| **Avg. daily time < 70 (%)** | **+42.9042** | 15.8537 | ±31.7075 | **+2.706** | **0.0068** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **409**, R² = **0.0820**, Adj R² = **0.0566**, F-statistic = **3.23** (p = **3.16e-04**), Residual SE = **64.966** on **397** df, AIC = **4586.7**, BIC = **4634.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +754.0243 | 5140.7960 | ±10281.5920 | +0.147 | 0.8834 |  |
| Education: graduate level (vs college) | +7.2132 | 6.7135 | ±13.4270 | +1.074 | 0.2826 |  |
| Education: high school or below (vs college) | -3.0679 | 14.6414 | ±29.2829 | -0.210 | 0.8340 |  |
| Site: UCSD (vs UAB) | -10.8337 | 8.6499 | ±17.2998 | -1.252 | 0.2104 |  |
| Site: UW (vs UAB) | -5.8817 | 7.9772 | ±15.9543 | -0.737 | 0.4609 |  |
| Age (years) | +0.2573 | 0.3278 | ±0.6555 | +0.785 | 0.4324 |  |
| **BMI (kg/m2)** | **-1.1962** | 0.4818 | ±0.9636 | **-2.483** | **0.0130** | * |
| **Hypertension** | **-23.7172** | 7.4025 | ±14.8049 | **-3.204** | **0.0014** | ** |
| High cholesterol | -0.3899 | 6.8049 | ±13.6098 | -0.057 | 0.9543 |  |
| **Kidney disease** | **-36.8791** | 18.7567 | ±37.5133 | **-1.966** | **0.0493** | * |
| Circulatory disease | +10.6401 | 12.0631 | ±24.1261 | +0.882 | 0.3778 |  |
| Time 54-250, pooled (%) | -3.5320 | 51.4408 | ±102.8816 | -0.069 | 0.9453 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **409**, R² = **0.0829**, Adj R² = **0.0575**, F-statistic = **3.26** (p = **2.75e-04**), Residual SE = **64.937** on **397** df, AIC = **4586.4**, BIC = **4634.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +4986.3337 | 6558.4641 | ±13116.9281 | +0.760 | 0.4471 |  |
| Education: graduate level (vs college) | +7.1935 | 6.7111 | ±13.4222 | +1.072 | 0.2838 |  |
| Education: high school or below (vs college) | -2.8865 | 14.6290 | ±29.2580 | -0.197 | 0.8436 |  |
| Site: UCSD (vs UAB) | -10.5471 | 8.5420 | ±17.0839 | -1.235 | 0.2169 |  |
| Site: UW (vs UAB) | -5.8469 | 7.9327 | ±15.8654 | -0.737 | 0.4611 |  |
| Age (years) | +0.2622 | 0.3267 | ±0.6535 | +0.802 | 0.4223 |  |
| **BMI (kg/m2)** | **-1.2013** | 0.4825 | ±0.9650 | **-2.490** | **0.0128** | * |
| **Hypertension** | **-23.7201** | 7.3844 | ±14.7687 | **-3.212** | **0.0013** | ** |
| High cholesterol | -0.3804 | 6.8082 | ±13.6165 | -0.056 | 0.9554 |  |
| Kidney disease | -36.6678 | 18.7704 | ±37.5409 | -1.953 | 0.0508 | . |
| Circulatory disease | +10.1572 | 12.0776 | ±24.1551 | +0.841 | 0.4004 |  |
| Avg. daily time 54-250 (%) | -45.8616 | 65.6045 | ±131.2091 | -0.699 | 0.4845 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **409**, R² = **0.0853**, Adj R² = **0.0599**, F-statistic = **3.36** (p = **1.84e-04**), Residual SE = **64.851** on **397** df, AIC = **4585.3**, BIC = **4633.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.0233** | 27.7277 | ±55.4554 | **+14.643** | **1.49e-48** | *** |
| Education: graduate level (vs college) | +6.9906 | 6.7506 | ±13.5012 | +1.036 | 0.3004 |  |
| Education: high school or below (vs college) | -3.8894 | 14.6370 | ±29.2739 | -0.266 | 0.7905 |  |
| Site: UCSD (vs UAB) | -10.9235 | 8.4935 | ±16.9870 | -1.286 | 0.1984 |  |
| Site: UW (vs UAB) | -5.8264 | 7.9097 | ±15.8194 | -0.737 | 0.4614 |  |
| Age (years) | +0.2531 | 0.3281 | ±0.6563 | +0.771 | 0.4405 |  |
| **BMI (kg/m2)** | **-1.2176** | 0.5081 | ±1.0162 | **-2.396** | **0.0166** | * |
| **Hypertension** | **-23.3154** | 7.3434 | ±14.6868 | **-3.175** | **0.0015** | ** |
| High cholesterol | -0.8252 | 6.7877 | ±13.5754 | -0.122 | 0.9032 |  |
| Kidney disease | -35.3413 | 19.1266 | ±38.2533 | -1.848 | 0.0646 | . |
| Circulatory disease | +10.4342 | 11.9359 | ±23.8717 | +0.874 | 0.3820 |  |
| Time 181-250, pooled (%) | -13.7714 | 12.1082 | ±24.2163 | -1.137 | 0.2554 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **409**, R² = **0.0843**, Adj R² = **0.0589**, F-statistic = **3.32** (p = **2.18e-04**), Residual SE = **64.888** on **397** df, AIC = **4585.7**, BIC = **4633.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+404.9866** | 26.8518 | ±53.7036 | **+15.082** | **2.12e-51** | *** |
| Education: graduate level (vs college) | +6.9798 | 6.7452 | ±13.4903 | +1.035 | 0.3008 |  |
| Education: high school or below (vs college) | -3.9725 | 14.6294 | ±29.2589 | -0.272 | 0.7860 |  |
| Site: UCSD (vs UAB) | -11.0307 | 8.4706 | ±16.9413 | -1.302 | 0.1928 |  |
| Site: UW (vs UAB) | -5.8061 | 7.9191 | ±15.8383 | -0.733 | 0.4635 |  |
| Age (years) | +0.2438 | 0.3253 | ±0.6506 | +0.749 | 0.4537 |  |
| **BMI (kg/m2)** | **-1.2022** | 0.4853 | ±0.9706 | **-2.477** | **0.0132** | * |
| **Hypertension** | **-23.4718** | 7.3597 | ±14.7194 | **-3.189** | **0.0014** | ** |
| High cholesterol | -0.4979 | 6.7902 | ±13.5805 | -0.073 | 0.9415 |  |
| Kidney disease | -35.8612 | 18.9601 | ±37.9203 | -1.891 | 0.0586 | . |
| Circulatory disease | +10.6582 | 11.9546 | ±23.9092 | +0.892 | 0.3726 |  |
| Avg. daily time 181-250 (%) | -11.2727 | 11.3024 | ±22.6048 | -0.997 | 0.3186 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **409**, R² = **0.0854**, Adj R² = **0.0601**, F-statistic = **3.37** (p = **1.79e-04**), Residual SE = **64.846** on **397** df, AIC = **4585.2**, BIC = **4633.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+406.2391** | 27.7716 | ±55.5432 | **+14.628** | **1.87e-48** | *** |
| Education: graduate level (vs college) | +6.9863 | 6.7495 | ±13.4991 | +1.035 | 0.3006 |  |
| Education: high school or below (vs college) | -3.9149 | 14.6361 | ±29.2722 | -0.267 | 0.7891 |  |
| Site: UCSD (vs UAB) | -10.9430 | 8.4916 | ±16.9833 | -1.289 | 0.1975 |  |
| Site: UW (vs UAB) | -5.8396 | 7.9071 | ±15.8142 | -0.739 | 0.4602 |  |
| Age (years) | +0.2521 | 0.3280 | ±0.6561 | +0.769 | 0.4422 |  |
| **BMI (kg/m2)** | **-1.2191** | 0.5090 | ±1.0180 | **-2.395** | **0.0166** | * |
| **Hypertension** | **-23.3166** | 7.3436 | ±14.6872 | **-3.175** | **0.0015** | ** |
| High cholesterol | -0.8293 | 6.7865 | ±13.5730 | -0.122 | 0.9027 |  |
| Kidney disease | -35.3046 | 19.1324 | ±38.2648 | -1.845 | 0.0650 | . |
| Circulatory disease | +10.4294 | 11.9331 | ±23.8661 | +0.874 | 0.3821 |  |
| Time > 180 (%) | -14.0650 | 12.0728 | ±24.1456 | -1.165 | 0.2440 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **409**, R² = **0.0844**, Adj R² = **0.0590**, F-statistic = **3.33** (p = **2.13e-04**), Residual SE = **64.883** on **397** df, AIC = **4585.7**, BIC = **4633.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+405.1964** | 26.8735 | ±53.7469 | **+15.078** | **2.26e-51** | *** |
| Education: graduate level (vs college) | +6.9737 | 6.7435 | ±13.4871 | +1.034 | 0.3011 |  |
| Education: high school or below (vs college) | -4.0045 | 14.6283 | ±29.2566 | -0.274 | 0.7843 |  |
| Site: UCSD (vs UAB) | -11.0514 | 8.4683 | ±16.9366 | -1.305 | 0.1919 |  |
| Site: UW (vs UAB) | -5.8166 | 7.9153 | ±15.8306 | -0.735 | 0.4624 |  |
| Age (years) | +0.2426 | 0.3252 | ±0.6504 | +0.746 | 0.4558 |  |
| **BMI (kg/m2)** | **-1.2033** | 0.4857 | ±0.9714 | **-2.477** | **0.0132** | * |
| **Hypertension** | **-23.4742** | 7.3600 | ±14.7200 | **-3.189** | **0.0014** | ** |
| High cholesterol | -0.4961 | 6.7893 | ±13.5785 | -0.073 | 0.9418 |  |
| Kidney disease | -35.8290 | 18.9644 | ±37.9287 | -1.889 | 0.0589 | . |
| Circulatory disease | +10.6581 | 11.9516 | ±23.9032 | +0.892 | 0.3725 |  |
| Avg. daily time > 180 (%) | -11.5864 | 11.2535 | ±22.5070 | -1.030 | 0.3032 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 409)
**Regression Call / Formula**: `sleep_tst_min ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **409**, R² = **0.0875**, Adj R² = **0.0623**, F-statistic = **3.46** (p = **1.25e-04**), Residual SE = **64.771** on **397** df, AIC = **4584.3**, BIC = **4632.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+405.2824** | 26.6286 | ±53.2572 | **+15.220** | **2.61e-52** | *** |
| Education: graduate level (vs college) | +6.5304 | 6.7511 | ±13.5021 | +0.967 | 0.3334 |  |
| Education: high school or below (vs college) | -3.1994 | 14.5703 | ±29.1406 | -0.220 | 0.8262 |  |
| Site: UCSD (vs UAB) | -10.6232 | 8.4448 | ±16.8897 | -1.258 | 0.2084 |  |
| Site: UW (vs UAB) | -5.2888 | 7.9295 | ±15.8591 | -0.667 | 0.5048 |  |
| Age (years) | +0.1770 | 0.3327 | ±0.6654 | +0.532 | 0.5947 |  |
| **BMI (kg/m2)** | **-1.1418** | 0.4712 | ±0.9424 | **-2.423** | **0.0154** | * |
| **Hypertension** | **-22.6884** | 7.3480 | ±14.6960 | **-3.088** | **0.0020** | ** |
| High cholesterol | -0.0578 | 6.8106 | ±13.6212 | -0.008 | 0.9932 |  |
| Kidney disease | -35.9514 | 18.4632 | ±36.9263 | -1.947 | 0.0515 | . |
| Circulatory disease | +9.9102 | 12.0542 | ±24.1084 | +0.822 | 0.4110 |  |
| Nocturnal time > 180 (%) | -13.7339 | 9.9101 | ±19.8202 | -1.386 | 0.1658 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Garmin stress score, mean (0-100)  (domain: Wearable activity; outcome sample N = 403; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **403**, R² = **0.1408**, Adj R² = **0.1189**, F-statistic = **6.43** (p = **3.47e-09**), Residual SE = **16.382** on **392** df, AIC = **3408.2**, BIC = **3452.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6403** | 7.8668 | ±15.7337 | **+7.454** | **9.05e-14** | *** |
| **Education: graduate level (vs college)** | **-4.7783** | 1.7654 | ±3.5307 | **-2.707** | **0.0068** | ** |
| Education: high school or below (vs college) | -1.6751 | 3.1922 | ±6.3844 | -0.525 | 0.5998 |  |
| Site: UCSD (vs UAB) | -0.9144 | 2.1951 | ±4.3902 | -0.417 | 0.6770 |  |
| **Site: UW (vs UAB)** | **-4.2796** | 2.0120 | ±4.0240 | **-2.127** | **0.0334** | * |
| **Age (years)** | **-0.3240** | 0.0822 | ±0.1643 | **-3.944** | **8.03e-05** | *** |
| **BMI (kg/m2)** | **+0.4654** | 0.1472 | ±0.2944 | **+3.162** | **0.0016** | ** |
| Hypertension | +2.0906 | 1.9211 | ±3.8422 | +1.088 | 0.2765 |  |
| High cholesterol | -0.9807 | 1.7797 | ±3.5594 | -0.551 | 0.5816 |  |
| Kidney disease | -2.1739 | 4.8814 | ±9.7627 | -0.445 | 0.6561 |  |
| Circulatory disease | -3.0018 | 2.2729 | ±4.5457 | -1.321 | 0.1866 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **403**, R² = **0.1409**, Adj R² = **0.1167**, F-statistic = **5.83** (p = **9.09e-09**), Residual SE = **16.402** on **391** df, AIC = **3410.2**, BIC = **3458.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.5056** | 17.0337 | ±34.0673 | **+3.317** | **9.09e-04** | *** |
| **Education: graduate level (vs college)** | **-4.7642** | 1.7746 | ±3.5492 | **-2.685** | **0.0073** | ** |
| Education: high school or below (vs college) | -1.6980 | 3.1877 | ±6.3755 | -0.533 | 0.5943 |  |
| Site: UCSD (vs UAB) | -0.8989 | 2.1993 | ±4.3987 | -0.409 | 0.6827 |  |
| **Site: UW (vs UAB)** | **-4.2595** | 2.0171 | ±4.0342 | **-2.112** | **0.0347** | * |
| **Age (years)** | **-0.3251** | 0.0826 | ±0.1653 | **-3.935** | **8.33e-05** | *** |
| **BMI (kg/m2)** | **+0.4633** | 0.1487 | ±0.2973 | **+3.117** | **0.0018** | ** |
| Hypertension | +2.0684 | 1.9421 | ±3.8842 | +1.065 | 0.2869 |  |
| High cholesterol | -1.0416 | 1.8710 | ±3.7420 | -0.557 | 0.5777 |  |
| Kidney disease | -2.1388 | 4.9039 | ±9.8079 | -0.436 | 0.6627 |  |
| Circulatory disease | -2.9863 | 2.2806 | ±4.5613 | -1.309 | 0.1904 |  |
| HbA1c (%) | +0.4110 | 2.9489 | ±5.8979 | +0.139 | 0.8892 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **403**, R² = **0.1439**, Adj R² = **0.1198**, F-statistic = **5.98** (p = **4.99e-09**), Residual SE = **16.373** on **391** df, AIC = **3408.8**, BIC = **3456.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+43.7676** | 15.3355 | ±30.6710 | **+2.854** | **0.0043** | ** |
| **Education: graduate level (vs college)** | **-4.7175** | 1.7638 | ±3.5276 | **-2.675** | **0.0075** | ** |
| Education: high school or below (vs college) | -1.4970 | 3.2026 | ±6.4052 | -0.467 | 0.6402 |  |
| Site: UCSD (vs UAB) | -1.0263 | 2.1955 | ±4.3909 | -0.467 | 0.6402 |  |
| **Site: UW (vs UAB)** | **-4.4149** | 2.0060 | ±4.0120 | **-2.201** | **0.0277** | * |
| **Age (years)** | **-0.3203** | 0.0826 | ±0.1651 | **-3.880** | **1.05e-04** | *** |
| **BMI (kg/m2)** | **+0.4566** | 0.1471 | ±0.2941 | **+3.104** | **0.0019** | ** |
| Hypertension | +1.9132 | 1.9092 | ±3.8184 | +1.002 | 0.3163 |  |
| High cholesterol | -0.9140 | 1.7900 | ±3.5800 | -0.511 | 0.6096 |  |
| Kidney disease | -2.1854 | 4.9367 | ±9.8735 | -0.443 | 0.6580 |  |
| Circulatory disease | -3.0519 | 2.2843 | ±4.5686 | -1.336 | 0.1815 |  |
| Mean glucose (mg/dL) | +0.1313 | 0.1136 | ±0.2272 | +1.156 | 0.2477 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **403**, R² = **0.1439**, Adj R² = **0.1198**, F-statistic = **5.98** (p = **4.99e-09**), Residual SE = **16.373** on **391** df, AIC = **3408.8**, BIC = **3456.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +25.5966 | 29.9369 | ±59.8738 | +0.855 | 0.3925 |  |
| **Education: graduate level (vs college)** | **-4.7175** | 1.7638 | ±3.5276 | **-2.675** | **0.0075** | ** |
| Education: high school or below (vs college) | -1.4970 | 3.2026 | ±6.4052 | -0.467 | 0.6402 |  |
| Site: UCSD (vs UAB) | -1.0263 | 2.1955 | ±4.3909 | -0.467 | 0.6402 |  |
| **Site: UW (vs UAB)** | **-4.4149** | 2.0060 | ±4.0120 | **-2.201** | **0.0277** | * |
| **Age (years)** | **-0.3203** | 0.0826 | ±0.1651 | **-3.880** | **1.05e-04** | *** |
| **BMI (kg/m2)** | **+0.4566** | 0.1471 | ±0.2941 | **+3.104** | **0.0019** | ** |
| Hypertension | +1.9132 | 1.9092 | ±3.8184 | +1.002 | 0.3163 |  |
| High cholesterol | -0.9140 | 1.7900 | ±3.5800 | -0.511 | 0.6096 |  |
| Kidney disease | -2.1854 | 4.9367 | ±9.8735 | -0.443 | 0.6580 |  |
| Circulatory disease | -3.0519 | 2.2843 | ±4.5686 | -1.336 | 0.1815 |  |
| GMI (%) | +5.4897 | 4.7495 | ±9.4991 | +1.156 | 0.2477 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **403**, R² = **0.1449**, Adj R² = **0.1209**, F-statistic = **6.02** (p = **4.10e-09**), Residual SE = **16.364** on **391** df, AIC = **3408.3**, BIC = **3456.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+44.7279** | 12.6288 | ±25.2576 | **+3.542** | **3.97e-04** | *** |
| **Education: graduate level (vs college)** | **-4.6434** | 1.7548 | ±3.5096 | **-2.646** | **0.0081** | ** |
| Education: high school or below (vs college) | -1.4878 | 3.2104 | ±6.4209 | -0.463 | 0.6431 |  |
| Site: UCSD (vs UAB) | -1.1967 | 2.1883 | ±4.3766 | -0.547 | 0.5845 |  |
| **Site: UW (vs UAB)** | **-4.5054** | 2.0106 | ±4.0211 | **-2.241** | **0.0250** | * |
| **Age (years)** | **-0.3069** | 0.0828 | ±0.1656 | **-3.705** | **2.11e-04** | *** |
| **BMI (kg/m2)** | **+0.4417** | 0.1439 | ±0.2877 | **+3.070** | **0.0021** | ** |
| Hypertension | +1.8791 | 1.9119 | ±3.8238 | +0.983 | 0.3257 |  |
| High cholesterol | -0.9743 | 1.7832 | ±3.5664 | -0.546 | 0.5848 |  |
| Kidney disease | -1.9200 | 4.9048 | ±9.8096 | -0.391 | 0.6955 |  |
| Circulatory disease | -2.9488 | 2.2787 | ±4.5574 | -1.294 | 0.1956 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.1194 | 0.0896 | ±0.1792 | +1.333 | 0.1824 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **403**, R² = **0.1433**, Adj R² = **0.1192**, F-statistic = **5.95** (p = **5.65e-09**), Residual SE = **16.379** on **391** df, AIC = **3409.1**, BIC = **3457.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.6327** | 9.8766 | ±19.7532 | **+5.329** | **9.87e-08** | *** |
| **Education: graduate level (vs college)** | **-4.6197** | 1.7685 | ±3.5369 | **-2.612** | **0.0090** | ** |
| Education: high school or below (vs college) | -1.5933 | 3.1640 | ±6.3279 | -0.504 | 0.6146 |  |
| Site: UCSD (vs UAB) | -0.8012 | 2.1927 | ±4.3854 | -0.365 | 0.7148 |  |
| **Site: UW (vs UAB)** | **-4.1449** | 2.0085 | ±4.0171 | **-2.064** | **0.0391** | * |
| **Age (years)** | **-0.3255** | 0.0822 | ±0.1645 | **-3.959** | **7.54e-05** | *** |
| **BMI (kg/m2)** | **+0.4604** | 0.1465 | ±0.2930 | **+3.143** | **0.0017** | ** |
| Hypertension | +1.9515 | 1.9151 | ±3.8302 | +1.019 | 0.3082 |  |
| High cholesterol | -0.8435 | 1.7927 | ±3.5854 | -0.471 | 0.6380 |  |
| Kidney disease | -2.6008 | 4.9886 | ±9.9771 | -0.521 | 0.6021 |  |
| Circulatory disease | -3.0922 | 2.2580 | ±4.5159 | -1.369 | 0.1709 |  |
| Glucose SD, pooled (mg/dL) | +0.3637 | 0.3634 | ±0.7268 | +1.001 | 0.3169 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **403**, R² = **0.1435**, Adj R² = **0.1194**, F-statistic = **5.96** (p = **5.40e-09**), Residual SE = **16.377** on **391** df, AIC = **3409.0**, BIC = **3456.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+53.0094** | 9.3960 | ±18.7919 | **+5.642** | **1.68e-08** | *** |
| **Education: graduate level (vs college)** | **-4.5934** | 1.7708 | ±3.5416 | **-2.594** | **0.0095** | ** |
| Education: high school or below (vs college) | -1.5463 | 3.1563 | ±6.3127 | -0.490 | 0.6242 |  |
| Site: UCSD (vs UAB) | -0.8134 | 2.1882 | ±4.3763 | -0.372 | 0.7101 |  |
| **Site: UW (vs UAB)** | **-4.1480** | 2.0097 | ±4.0193 | **-2.064** | **0.0390** | * |
| **Age (years)** | **-0.3263** | 0.0823 | ±0.1646 | **-3.964** | **7.37e-05** | *** |
| **BMI (kg/m2)** | **+0.4575** | 0.1457 | ±0.2914 | **+3.140** | **0.0017** | ** |
| Hypertension | +1.9957 | 1.9141 | ±3.8283 | +1.043 | 0.2971 |  |
| High cholesterol | -0.8488 | 1.7905 | ±3.5809 | -0.474 | 0.6355 |  |
| Kidney disease | -2.6006 | 4.9762 | ±9.9525 | -0.523 | 0.6012 |  |
| Circulatory disease | -3.0281 | 2.2655 | ±4.5309 | -1.337 | 0.1813 |  |
| Avg. daily SD (mg/dL) | +0.3782 | 0.3626 | ±0.7251 | +1.043 | 0.2969 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **403**, R² = **0.1414**, Adj R² = **0.1173**, F-statistic = **5.85** (p = **8.17e-09**), Residual SE = **16.397** on **391** df, AIC = **3409.9**, BIC = **3457.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.7559** | 9.5509 | ±19.1019 | **+5.838** | **5.29e-09** | *** |
| **Education: graduate level (vs college)** | **-4.7137** | 1.7726 | ±3.5451 | **-2.659** | **0.0078** | ** |
| Education: high school or below (vs college) | -1.6681 | 3.1809 | ±6.3618 | -0.524 | 0.6000 |  |
| Site: UCSD (vs UAB) | -0.8401 | 2.1969 | ±4.3937 | -0.382 | 0.7022 |  |
| **Site: UW (vs UAB)** | **-4.1900** | 2.0108 | ±4.0216 | **-2.084** | **0.0372** | * |
| **Age (years)** | **-0.3253** | 0.0823 | ±0.1647 | **-3.952** | **7.76e-05** | *** |
| **BMI (kg/m2)** | **+0.4648** | 0.1470 | ±0.2941 | **+3.161** | **0.0016** | ** |
| Hypertension | +2.0592 | 1.9225 | ±3.8450 | +1.071 | 0.2841 |  |
| High cholesterol | -0.9254 | 1.7848 | ±3.5696 | -0.518 | 0.6041 |  |
| Kidney disease | -2.3729 | 4.9620 | ±9.9241 | -0.478 | 0.6325 |  |
| Circulatory disease | -3.0383 | 2.2640 | ±4.5280 | -1.342 | 0.1796 |  |
| CV (%) | +0.1967 | 0.3804 | ±0.7608 | +0.517 | 0.6051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **403**, R² = **0.1413**, Adj R² = **0.1171**, F-statistic = **5.85** (p = **8.36e-09**), Residual SE = **16.398** on **391** df, AIC = **3410.0**, BIC = **3458.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.1085** | 9.4925 | ±18.9850 | **+6.438** | **1.21e-10** | *** |
| **Education: graduate level (vs college)** | **-4.7125** | 1.7716 | ±3.5433 | **-2.660** | **0.0078** | ** |
| Education: high school or below (vs college) | -1.6815 | 3.1820 | ±6.3641 | -0.528 | 0.5972 |  |
| Site: UCSD (vs UAB) | -0.8616 | 2.1979 | ±4.3958 | -0.392 | 0.6951 |  |
| **Site: UW (vs UAB)** | **-4.2129** | 2.0135 | ±4.0269 | **-2.092** | **0.0364** | * |
| **Age (years)** | **-0.3249** | 0.0823 | ±0.1646 | **-3.949** | **7.85e-05** | *** |
| **BMI (kg/m2)** | **+0.4648** | 0.1472 | ±0.2944 | **+3.158** | **0.0016** | ** |
| Hypertension | +2.0619 | 1.9221 | ±3.8441 | +1.073 | 0.2834 |  |
| High cholesterol | -0.9255 | 1.7870 | ±3.5740 | -0.518 | 0.6045 |  |
| Kidney disease | -2.3096 | 4.9334 | ±9.8669 | -0.468 | 0.6397 |  |
| Circulatory disease | -3.0202 | 2.2653 | ±4.5306 | -1.333 | 0.1825 |  |
| Mean / SD ratio | -0.3561 | 0.7613 | ±1.5225 | -0.468 | 0.6399 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **403**, R² = **0.1417**, Adj R² = **0.1176**, F-statistic = **5.87** (p = **7.73e-09**), Residual SE = **16.394** on **391** df, AIC = **3409.8**, BIC = **3457.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+61.6679** | 9.2442 | ±18.4884 | **+6.671** | **2.54e-11** | *** |
| **Education: graduate level (vs college)** | **-4.6805** | 1.7734 | ±3.5469 | **-2.639** | **0.0083** | ** |
| Education: high school or below (vs college) | -1.6709 | 3.1726 | ±6.3452 | -0.527 | 0.5984 |  |
| Site: UCSD (vs UAB) | -0.8579 | 2.1938 | ±4.3876 | -0.391 | 0.6958 |  |
| **Site: UW (vs UAB)** | **-4.1952** | 2.0134 | ±4.0268 | **-2.084** | **0.0372** | * |
| **Age (years)** | **-0.3258** | 0.0824 | ±0.1647 | **-3.955** | **7.65e-05** | *** |
| **BMI (kg/m2)** | **+0.4628** | 0.1469 | ±0.2937 | **+3.151** | **0.0016** | ** |
| Hypertension | +2.0745 | 1.9225 | ±3.8450 | +1.079 | 0.2806 |  |
| High cholesterol | -0.9233 | 1.7831 | ±3.5662 | -0.518 | 0.6046 |  |
| Kidney disease | -2.3617 | 4.9194 | ±9.8388 | -0.480 | 0.6312 |  |
| Circulatory disease | -2.9742 | 2.2733 | ±4.5466 | -1.308 | 0.1908 |  |
| Avg. daily mean/SD | -0.3762 | 0.5834 | ±1.1669 | -0.645 | 0.5190 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **403**, R² = **0.1423**, Adj R² = **0.1181**, F-statistic = **5.90** (p = **6.92e-09**), Residual SE = **16.389** on **391** df, AIC = **3409.5**, BIC = **3457.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+54.2177** | 9.5294 | ±19.0589 | **+5.689** | **1.27e-08** | *** |
| **Education: graduate level (vs college)** | **-4.7626** | 1.7682 | ±3.5363 | **-2.694** | **0.0071** | ** |
| Education: high school or below (vs college) | -1.8586 | 3.2115 | ±6.4231 | -0.579 | 0.5628 |  |
| Site: UCSD (vs UAB) | -0.8454 | 2.1986 | ±4.3973 | -0.385 | 0.7006 |  |
| **Site: UW (vs UAB)** | **-4.1141** | 2.0364 | ±4.0727 | **-2.020** | **0.0433** | * |
| **Age (years)** | **-0.3182** | 0.0826 | ±0.1652 | **-3.851** | **1.18e-04** | *** |
| **BMI (kg/m2)** | **+0.4698** | 0.1457 | ±0.2914 | **+3.224** | **0.0013** | ** |
| Hypertension | +2.1456 | 1.9249 | ±3.8498 | +1.115 | 0.2650 |  |
| High cholesterol | -1.0239 | 1.7839 | ±3.5679 | -0.574 | 0.5660 |  |
| Kidney disease | -2.4059 | 4.8960 | ±9.7920 | -0.491 | 0.6231 |  |
| Circulatory disease | -2.9784 | 2.2765 | ±4.5530 | -1.308 | 0.1908 |  |
| MAG (mg/dL/h) | +0.1139 | 0.1424 | ±0.2848 | +0.800 | 0.4238 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **403**, R² = **0.1429**, Adj R² = **0.1188**, F-statistic = **5.92** (p = **6.14e-09**), Residual SE = **16.383** on **391** df, AIC = **3409.3**, BIC = **3457.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+52.8026** | 10.4895 | ±20.9791 | **+5.034** | **4.81e-07** | *** |
| **Education: graduate level (vs college)** | **-4.6853** | 1.7760 | ±3.5520 | **-2.638** | **0.0083** | ** |
| Education: high school or below (vs college) | -1.6538 | 3.1691 | ±6.3382 | -0.522 | 0.6018 |  |
| Site: UCSD (vs UAB) | -0.8380 | 2.2008 | ±4.4016 | -0.381 | 0.7034 |  |
| **Site: UW (vs UAB)** | **-4.1725** | 2.0272 | ±4.0544 | **-2.058** | **0.0396** | * |
| **Age (years)** | **-0.3248** | 0.0826 | ±0.1653 | **-3.931** | **8.47e-05** | *** |
| **BMI (kg/m2)** | **+0.4733** | 0.1509 | ±0.3017 | **+3.137** | **0.0017** | ** |
| Hypertension | +2.1414 | 1.9266 | ±3.8531 | +1.112 | 0.2663 |  |
| High cholesterol | -0.9392 | 1.7816 | ±3.5633 | -0.527 | 0.5981 |  |
| Kidney disease | -2.4404 | 4.9388 | ±9.8777 | -0.494 | 0.6212 |  |
| Circulatory disease | -3.0411 | 2.2737 | ±4.5474 | -1.338 | 0.1811 |  |
| Avg. daily range (mg/dL) | +0.0694 | 0.0754 | ±0.1508 | +0.921 | 0.3571 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **403**, R² = **0.1447**, Adj R² = **0.1207**, F-statistic = **6.02** (p = **4.23e-09**), Residual SE = **16.365** on **391** df, AIC = **3408.4**, BIC = **3456.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+55.8251** | 8.0951 | ±16.1901 | **+6.896** | **5.34e-12** | *** |
| **Education: graduate level (vs college)** | **-4.8529** | 1.7668 | ±3.5336 | **-2.747** | **0.0060** | ** |
| Education: high school or below (vs college) | -1.8701 | 3.1895 | ±6.3791 | -0.586 | 0.5577 |  |
| Site: UCSD (vs UAB) | -0.7871 | 2.1892 | ±4.3784 | -0.360 | 0.7192 |  |
| **Site: UW (vs UAB)** | **-4.3128** | 2.0032 | ±4.0065 | **-2.153** | **0.0313** | * |
| **Age (years)** | **-0.3238** | 0.0816 | ±0.1631 | **-3.969** | **7.21e-05** | *** |
| **BMI (kg/m2)** | **+0.4637** | 0.1466 | ±0.2932 | **+3.164** | **0.0016** | ** |
| Hypertension | +1.8787 | 1.9409 | ±3.8818 | +0.968 | 0.3331 |  |
| High cholesterol | -1.0241 | 1.7784 | ±3.5568 | -0.576 | 0.5647 |  |
| Kidney disease | -2.2015 | 4.8476 | ±9.6952 | -0.454 | 0.6497 |  |
| Circulatory disease | -3.2128 | 2.2663 | ±4.5326 | -1.418 | 0.1563 |  |
| SD of daily means (mg/dL) | +0.5802 | 0.4265 | ±0.8530 | +1.360 | 0.1737 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **403**, R² = **0.1447**, Adj R² = **0.1206**, F-statistic = **6.01** (p = **4.28e-09**), Residual SE = **16.366** on **391** df, AIC = **3408.4**, BIC = **3456.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +420.8882 | 274.6157 | ±549.2315 | +1.533 | 0.1254 |  |
| **Education: graduate level (vs college)** | **-4.6607** | 1.7792 | ±3.5583 | **-2.620** | **0.0088** | ** |
| Education: high school or below (vs college) | -1.5478 | 3.1455 | ±6.2911 | -0.492 | 0.6227 |  |
| Site: UCSD (vs UAB) | -0.7557 | 2.2075 | ±4.4150 | -0.342 | 0.7321 |  |
| **Site: UW (vs UAB)** | **-4.1912** | 2.0124 | ±4.0248 | **-2.083** | **0.0373** | * |
| **Age (years)** | **-0.3205** | 0.0829 | ±0.1657 | **-3.868** | **1.10e-04** | *** |
| **BMI (kg/m2)** | **+0.4689** | 0.1551 | ±0.3102 | **+3.023** | **0.0025** | ** |
| Hypertension | +2.0411 | 1.9121 | ±3.8242 | +1.067 | 0.2858 |  |
| High cholesterol | -1.0007 | 1.7767 | ±3.5534 | -0.563 | 0.5733 |  |
| Kidney disease | -2.5110 | 4.9360 | ±9.8720 | -0.509 | 0.6110 |  |
| Circulatory disease | -2.9902 | 2.2396 | ±4.4791 | -1.335 | 0.1818 |  |
| Time in range 70-180, pooled (%) | -3.6432 | 2.7666 | ±5.5331 | -1.317 | 0.1879 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **403**, R² = **0.1452**, Adj R² = **0.1211**, F-statistic = **6.04** (p = **3.90e-09**), Residual SE = **16.361** on **391** df, AIC = **3408.2**, BIC = **3456.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +428.9533 | 260.4543 | ±520.9086 | +1.647 | 0.0996 | . |
| **Education: graduate level (vs college)** | **-4.6216** | 1.7700 | ±3.5401 | **-2.611** | **0.0090** | ** |
| Education: high school or below (vs college) | -1.5059 | 3.1425 | ±6.2850 | -0.479 | 0.6318 |  |
| Site: UCSD (vs UAB) | -0.8072 | 2.1909 | ±4.3819 | -0.368 | 0.7126 |  |
| **Site: UW (vs UAB)** | **-4.2915** | 2.0076 | ±4.0152 | **-2.138** | **0.0325** | * |
| **Age (years)** | **-0.3202** | 0.0824 | ±0.1647 | **-3.888** | **1.01e-04** | *** |
| **BMI (kg/m2)** | **+0.4662** | 0.1486 | ±0.2973 | **+3.136** | **0.0017** | ** |
| Hypertension | +2.1953 | 1.9261 | ±3.8523 | +1.140 | 0.2544 |  |
| High cholesterol | -1.0536 | 1.7743 | ±3.5487 | -0.594 | 0.5526 |  |
| Kidney disease | -2.3892 | 4.9476 | ±9.8952 | -0.483 | 0.6292 |  |
| Circulatory disease | -3.0919 | 2.2514 | ±4.5027 | -1.373 | 0.1696 |  |
| Avg. daily time in range 70-180 (%) | -3.7212 | 2.6176 | ±5.2351 | -1.422 | 0.1551 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading < 54 during wear (0/1)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_below_54`  
**Model Diagnostics**: N = **403**, R² = **0.1410**, Adj R² = **0.1168**, F-statistic = **5.83** (p = **8.88e-09**), Residual SE = **16.401** on **391** df, AIC = **3410.1**, BIC = **3458.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.4568** | 7.9135 | ±15.8270 | **+7.387** | **1.50e-13** | *** |
| **Education: graduate level (vs college)** | **-4.7730** | 1.7705 | ±3.5411 | **-2.696** | **0.0070** | ** |
| Education: high school or below (vs college) | -1.6448 | 3.2041 | ±6.4081 | -0.513 | 0.6077 |  |
| Site: UCSD (vs UAB) | -0.8263 | 2.2238 | ±4.4475 | -0.372 | 0.7102 |  |
| **Site: UW (vs UAB)** | **-4.2335** | 2.0318 | ±4.0636 | **-2.084** | **0.0372** | * |
| **Age (years)** | **-0.3235** | 0.0823 | ±0.1645 | **-3.932** | **8.44e-05** | *** |
| **BMI (kg/m2)** | **+0.4654** | 0.1472 | ±0.2944 | **+3.162** | **0.0016** | ** |
| Hypertension | +2.0605 | 1.9257 | ±3.8515 | +1.070 | 0.2846 |  |
| High cholesterol | -0.9751 | 1.7825 | ±3.5650 | -0.547 | 0.5843 |  |
| Kidney disease | -2.1087 | 4.9164 | ±9.8328 | -0.429 | 0.6680 |  |
| Circulatory disease | -3.0287 | 2.2791 | ±4.5582 | -1.329 | 0.1839 |  |
| Any reading < 54 during wear (0/1) | +0.6049 | 2.0390 | ±4.0780 | +0.297 | 0.7667 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **403**, R² = **0.1419**, Adj R² = **0.1177**, F-statistic = **5.88** (p = **7.51e-09**), Residual SE = **16.393** on **391** df, AIC = **3409.7**, BIC = **3457.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.3126** | 7.8224 | ±15.6447 | **+7.455** | **9.01e-14** | *** |
| **Education: graduate level (vs college)** | **-4.7705** | 1.7674 | ±3.5347 | **-2.699** | **0.0070** | ** |
| Education: high school or below (vs college) | -1.5269 | 3.2054 | ±6.4107 | -0.476 | 0.6338 |  |
| Site: UCSD (vs UAB) | -0.7424 | 2.2088 | ±4.4176 | -0.336 | 0.7368 |  |
| **Site: UW (vs UAB)** | **-4.2042** | 2.0219 | ±4.0438 | **-2.079** | **0.0376** | * |
| **Age (years)** | **-0.3199** | 0.0821 | ±0.1643 | **-3.895** | **9.84e-05** | *** |
| **BMI (kg/m2)** | **+0.4592** | 0.1466 | ±0.2933 | **+3.132** | **0.0017** | ** |
| Hypertension | +1.9708 | 1.9360 | ±3.8720 | +1.018 | 0.3087 |  |
| High cholesterol | -0.9352 | 1.7859 | ±3.5718 | -0.524 | 0.6005 |  |
| Kidney disease | -2.0567 | 4.8980 | ±9.7959 | -0.420 | 0.6746 |  |
| Circulatory disease | -3.1003 | 2.2889 | ±4.5778 | -1.355 | 0.1756 |  |
| Time < 54 (%) | +10.2072 | 12.2748 | ±24.5496 | +0.832 | 0.4057 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **403**, R² = **0.1408**, Adj R² = **0.1167**, F-statistic = **5.83** (p = **9.17e-09**), Residual SE = **16.402** on **391** df, AIC = **3410.2**, BIC = **3458.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.6324** | 7.8769 | ±15.7538 | **+7.444** | **9.80e-14** | *** |
| **Education: graduate level (vs college)** | **-4.7785** | 1.7701 | ±3.5401 | **-2.700** | **0.0069** | ** |
| Education: high school or below (vs college) | -1.6713 | 3.1994 | ±6.3988 | -0.522 | 0.6014 |  |
| Site: UCSD (vs UAB) | -0.9101 | 2.1994 | ±4.3988 | -0.414 | 0.6790 |  |
| **Site: UW (vs UAB)** | **-4.2799** | 2.0175 | ±4.0351 | **-2.121** | **0.0339** | * |
| **Age (years)** | **-0.3239** | 0.0823 | ±0.1646 | **-3.936** | **8.27e-05** | *** |
| **BMI (kg/m2)** | **+0.4652** | 0.1475 | ±0.2950 | **+3.154** | **0.0016** | ** |
| Hypertension | +2.0888 | 1.9263 | ±3.8526 | +1.084 | 0.2782 |  |
| High cholesterol | -0.9800 | 1.7864 | ±3.5728 | -0.549 | 0.5833 |  |
| Kidney disease | -2.1688 | 4.8886 | ±9.7773 | -0.444 | 0.6573 |  |
| Circulatory disease | -3.0119 | 2.2949 | ±4.5898 | -1.312 | 0.1894 |  |
| Avg. daily time < 54 (%) | +0.8371 | 19.3271 | ±38.6543 | +0.043 | 0.9655 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **403**, R² = **0.1409**, Adj R² = **0.1167**, F-statistic = **5.83** (p = **9.14e-09**), Residual SE = **16.402** on **391** df, AIC = **3410.2**, BIC = **3458.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.7246** | 7.8882 | ±15.7764 | **+7.445** | **9.72e-14** | *** |
| **Education: graduate level (vs college)** | **-4.7841** | 1.7762 | ±3.5525 | **-2.693** | **0.0071** | ** |
| Education: high school or below (vs college) | -1.6563 | 3.1998 | ±6.3995 | -0.518 | 0.6047 |  |
| Site: UCSD (vs UAB) | -0.9266 | 2.1988 | ±4.3976 | -0.421 | 0.6734 |  |
| **Site: UW (vs UAB)** | **-4.2930** | 2.0219 | ±4.0439 | **-2.123** | **0.0337** | * |
| **Age (years)** | **-0.3241** | 0.0824 | ±0.1649 | **-3.931** | **8.46e-05** | *** |
| **BMI (kg/m2)** | **+0.4653** | 0.1475 | ±0.2949 | **+3.155** | **0.0016** | ** |
| Hypertension | +2.0760 | 1.9291 | ±3.8582 | +1.076 | 0.2819 |  |
| High cholesterol | -0.9641 | 1.8082 | ±3.6163 | -0.533 | 0.5939 |  |
| Kidney disease | -2.1866 | 4.8967 | ±9.7933 | -0.447 | 0.6552 |  |
| Circulatory disease | -3.0059 | 2.2780 | ±4.5560 | -1.320 | 0.1870 |  |
| Time 54-69, pooled (%) | -0.4664 | 4.4718 | ±8.9436 | -0.104 | 0.9169 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **403**, R² = **0.1421**, Adj R² = **0.1180**, F-statistic = **5.89** (p = **7.17e-09**), Residual SE = **16.391** on **391** df, AIC = **3409.6**, BIC = **3457.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.1024** | 7.9102 | ±15.8204 | **+7.472** | **7.92e-14** | *** |
| **Education: graduate level (vs college)** | **-4.8517** | 1.7744 | ±3.5488 | **-2.734** | **0.0063** | ** |
| Education: high school or below (vs college) | -1.5457 | 3.2444 | ±6.4889 | -0.476 | 0.6338 |  |
| Site: UCSD (vs UAB) | -0.9655 | 2.2008 | ±4.4015 | -0.439 | 0.6609 |  |
| **Site: UW (vs UAB)** | **-4.3184** | 2.0144 | ±4.0289 | **-2.144** | **0.0321** | * |
| **Age (years)** | **-0.3233** | 0.0827 | ±0.1654 | **-3.910** | **9.22e-05** | *** |
| **BMI (kg/m2)** | **+0.4653** | 0.1479 | ±0.2958 | **+3.146** | **0.0017** | ** |
| Hypertension | +1.8863 | 1.9315 | ±3.8629 | +0.977 | 0.3288 |  |
| High cholesterol | -0.8734 | 1.8047 | ±3.6093 | -0.484 | 0.6284 |  |
| Kidney disease | -2.2476 | 4.8994 | ±9.7989 | -0.459 | 0.6464 |  |
| Circulatory disease | -2.9521 | 2.2731 | ±4.5462 | -1.299 | 0.1940 |  |
| Avg. daily time 54-69 (%) | -3.5106 | 4.5069 | ±9.0137 | -0.779 | 0.4360 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **403**, R² = **0.1409**, Adj R² = **0.1167**, F-statistic = **5.83** (p = **9.15e-09**), Residual SE = **16.402** on **391** df, AIC = **3410.2**, BIC = **3458.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+58.5635** | 7.8772 | ±15.7543 | **+7.435** | **1.05e-13** | *** |
| **Education: graduate level (vs college)** | **-4.7735** | 1.7758 | ±3.5517 | **-2.688** | **0.0072** | ** |
| Education: high school or below (vs college) | -1.6844 | 3.1927 | ±6.3855 | -0.528 | 0.5978 |  |
| Site: UCSD (vs UAB) | -0.8989 | 2.1992 | ±4.3984 | -0.409 | 0.6827 |  |
| **Site: UW (vs UAB)** | **-4.2666** | 2.0240 | ±4.0480 | **-2.108** | **0.0350** | * |
| **Age (years)** | **-0.3238** | 0.0823 | ±0.1646 | **-3.934** | **8.35e-05** | *** |
| **BMI (kg/m2)** | **+0.4653** | 0.1474 | ±0.2947 | **+3.157** | **0.0016** | ** |
| Hypertension | +2.0976 | 1.9258 | ±3.8516 | +1.089 | 0.2761 |  |
| High cholesterol | -0.9919 | 1.7975 | ±3.5950 | -0.552 | 0.5811 |  |
| Kidney disease | -2.1599 | 4.8959 | ±9.7919 | -0.441 | 0.6591 |  |
| Circulatory disease | -3.0021 | 2.2771 | ±4.5543 | -1.318 | 0.1874 |  |
| Time < 70 (%) | +0.3610 | 3.8696 | ±7.7392 | +0.093 | 0.9257 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **403**, R² = **0.1418**, Adj R² = **0.1177**, F-statistic = **5.87** (p = **7.53e-09**), Residual SE = **16.393** on **391** df, AIC = **3409.7**, BIC = **3457.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+59.0412** | 7.9121 | ±15.8241 | **+7.462** | **8.51e-14** | *** |
| **Education: graduate level (vs college)** | **-4.8370** | 1.7733 | ±3.5466 | **-2.728** | **0.0064** | ** |
| Education: high school or below (vs college) | -1.5830 | 3.2403 | ±6.4806 | -0.489 | 0.6252 |  |
| Site: UCSD (vs UAB) | -0.9705 | 2.1996 | ±4.3993 | -0.441 | 0.6591 |  |
| **Site: UW (vs UAB)** | **-4.3099** | 2.0156 | ±4.0312 | **-2.138** | **0.0325** | * |
| **Age (years)** | **-0.3237** | 0.0827 | ±0.1653 | **-3.916** | **9.01e-05** | *** |
| **BMI (kg/m2)** | **+0.4659** | 0.1480 | ±0.2960 | **+3.148** | **0.0016** | ** |
| Hypertension | +1.9311 | 1.9294 | ±3.8588 | +1.001 | 0.3169 |  |
| High cholesterol | -0.8962 | 1.7986 | ±3.5972 | -0.498 | 0.6183 |  |
| Kidney disease | -2.2507 | 4.8959 | ±9.7917 | -0.460 | 0.6457 |  |
| Circulatory disease | -2.9273 | 2.2724 | ±4.5448 | -1.288 | 0.1977 |  |
| Avg. daily time < 70 (%) | -2.8422 | 4.0433 | ±8.0867 | -0.703 | 0.4821 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **403**, R² = **0.1420**, Adj R² = **0.1179**, F-statistic = **5.88** (p = **7.24e-09**), Residual SE = **16.391** on **391** df, AIC = **3409.6**, BIC = **3457.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1140.7157 | 1187.2124 | ±2374.4247 | +0.961 | 0.3366 |  |
| **Education: graduate level (vs college)** | **-4.7697** | 1.7673 | ±3.5346 | **-2.699** | **0.0070** | ** |
| Education: high school or below (vs college) | -1.5111 | 3.2056 | ±6.4111 | -0.471 | 0.6374 |  |
| Site: UCSD (vs UAB) | -0.7176 | 2.2109 | ±4.4219 | -0.325 | 0.7455 |  |
| **Site: UW (vs UAB)** | **-4.1882** | 2.0224 | ±4.0449 | **-2.071** | **0.0384** | * |
| **Age (years)** | **-0.3189** | 0.0823 | ±0.1645 | **-3.877** | **1.06e-04** | *** |
| **BMI (kg/m2)** | **+0.4596** | 0.1465 | ±0.2930 | **+3.138** | **0.0017** | ** |
| Hypertension | +1.9707 | 1.9342 | ±3.8684 | +1.019 | 0.3083 |  |
| High cholesterol | -0.9360 | 1.7851 | ±3.5703 | -0.524 | 0.6001 |  |
| Kidney disease | -2.0514 | 4.8992 | ±9.7983 | -0.419 | 0.6754 |  |
| Circulatory disease | -3.1070 | 2.2899 | ±4.5797 | -1.357 | 0.1748 |  |
| Time 54-250, pooled (%) | -10.8251 | 11.8765 | ±23.7530 | -0.911 | 0.3620 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **403**, R² = **0.1409**, Adj R² = **0.1167**, F-statistic = **5.83** (p = **9.09e-09**), Residual SE = **16.402** on **391** df, AIC = **3410.2**, BIC = **3458.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +345.1921 | 1813.2162 | ±3626.4324 | +0.190 | 0.8490 |  |
| **Education: graduate level (vs college)** | **-4.7789** | 1.7699 | ±3.5397 | **-2.700** | **0.0069** | ** |
| Education: high school or below (vs college) | -1.6603 | 3.1984 | ±6.3968 | -0.519 | 0.6037 |  |
| Site: UCSD (vs UAB) | -0.8954 | 2.2012 | ±4.4025 | -0.407 | 0.6842 |  |
| **Site: UW (vs UAB)** | **-4.2774** | 2.0189 | ±4.0378 | **-2.119** | **0.0341** | * |
| **Age (years)** | **-0.3235** | 0.0824 | ±0.1647 | **-3.929** | **8.54e-05** | *** |
| **BMI (kg/m2)** | **+0.4650** | 0.1473 | ±0.2946 | **+3.157** | **0.0016** | ** |
| Hypertension | +2.0867 | 1.9258 | ±3.8516 | +1.084 | 0.2786 |  |
| High cholesterol | -0.9794 | 1.7853 | ±3.5705 | -0.549 | 0.5833 |  |
| Kidney disease | -2.1571 | 4.8910 | ±9.7820 | -0.441 | 0.6592 |  |
| Circulatory disease | -3.0366 | 2.2948 | ±4.5896 | -1.323 | 0.1858 |  |
| Avg. daily time 54-250 (%) | -2.8660 | 18.1378 | ±36.2756 | -0.158 | 0.8744 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **403**, R² = **0.1448**, Adj R² = **0.1208**, F-statistic = **6.02** (p = **4.17e-09**), Residual SE = **16.364** on **391** df, AIC = **3408.3**, BIC = **3456.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.2506** | 8.4644 | ±16.9288 | **+6.764** | **1.35e-11** | *** |
| **Education: graduate level (vs college)** | **-4.7020** | 1.7703 | ±3.5406 | **-2.656** | **0.0079** | ** |
| Education: high school or below (vs college) | -1.4349 | 3.1819 | ±6.3637 | -0.451 | 0.6520 |  |
| Site: UCSD (vs UAB) | -0.9177 | 2.2058 | ±4.4117 | -0.416 | 0.6774 |  |
| **Site: UW (vs UAB)** | **-4.3312** | 2.0110 | ±4.0219 | **-2.154** | **0.0313** | * |
| **Age (years)** | **-0.3229** | 0.0834 | ±0.1669 | **-3.870** | **1.09e-04** | *** |
| **BMI (kg/m2)** | **+0.4703** | 0.1585 | ±0.3170 | **+2.967** | **0.0030** | ** |
| Hypertension | +1.9554 | 1.9114 | ±3.8228 | +1.023 | 0.3063 |  |
| High cholesterol | -0.8769 | 1.7928 | ±3.5856 | -0.489 | 0.6248 |  |
| Kidney disease | -2.6984 | 4.9952 | ±9.9905 | -0.540 | 0.5891 |  |
| Circulatory disease | -2.9852 | 2.2234 | ±4.4467 | -1.343 | 0.1794 |  |
| Time 181-250, pooled (%) | +4.0009 | 3.1265 | ±6.2529 | +1.280 | 0.2006 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **403**, R² = **0.1496**, Adj R² = **0.1256**, F-statistic = **6.25** (p = **1.62e-09**), Residual SE = **16.319** on **391** df, AIC = **3406.1**, BIC = **3454.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.6813** | 8.0865 | ±16.1730 | **+7.009** | **2.39e-12** | *** |
| **Education: graduate level (vs college)** | **-4.6540** | 1.7581 | ±3.5163 | **-2.647** | **0.0081** | ** |
| Education: high school or below (vs college) | -1.2270 | 3.1720 | ±6.3441 | -0.387 | 0.6989 |  |
| Site: UCSD (vs UAB) | -0.8700 | 2.1932 | ±4.3865 | -0.397 | 0.6916 |  |
| **Site: UW (vs UAB)** | **-4.3668** | 2.0022 | ±4.0043 | **-2.181** | **0.0292** | * |
| **Age (years)** | **-0.3178** | 0.0827 | ±0.1654 | **-3.842** | **1.22e-04** | *** |
| **BMI (kg/m2)** | **+0.4672** | 0.1506 | ±0.3011 | **+3.103** | **0.0019** | ** |
| Hypertension | +1.9238 | 1.9090 | ±3.8179 | +1.008 | 0.3135 |  |
| High cholesterol | -0.9197 | 1.7789 | ±3.5577 | -0.517 | 0.6051 |  |
| Kidney disease | -2.6660 | 4.9992 | ±9.9984 | -0.533 | 0.5938 |  |
| Circulatory disease | -2.9897 | 2.2186 | ±4.4372 | -1.348 | 0.1778 |  |
| Avg. daily time 181-250 (%) | +5.8078 | 2.9850 | ±5.9700 | +1.946 | 0.0517 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **403**, R² = **0.1449**, Adj R² = **0.1208**, F-statistic = **6.02** (p = **4.11e-09**), Residual SE = **16.364** on **391** df, AIC = **3408.3**, BIC = **3456.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+57.2092** | 8.4795 | ±16.9590 | **+6.747** | **1.51e-11** | *** |
| **Education: graduate level (vs college)** | **-4.7013** | 1.7704 | ±3.5408 | **-2.655** | **0.0079** | ** |
| Education: high school or below (vs college) | -1.4306 | 3.1819 | ±6.3638 | -0.450 | 0.6530 |  |
| Site: UCSD (vs UAB) | -0.9124 | 2.2061 | ±4.4122 | -0.414 | 0.6792 |  |
| **Site: UW (vs UAB)** | **-4.3273** | 2.0107 | ±4.0213 | **-2.152** | **0.0314** | * |
| **Age (years)** | **-0.3226** | 0.0835 | ±0.1669 | **-3.865** | **1.11e-04** | *** |
| **BMI (kg/m2)** | **+0.4706** | 0.1588 | ±0.3175 | **+2.964** | **0.0030** | ** |
| Hypertension | +1.9571 | 1.9114 | ±3.8228 | +1.024 | 0.3059 |  |
| High cholesterol | -0.8774 | 1.7925 | ±3.5851 | -0.489 | 0.6245 |  |
| Kidney disease | -2.7029 | 4.9957 | ±9.9915 | -0.541 | 0.5885 |  |
| Circulatory disease | -2.9854 | 2.2232 | ±4.4464 | -1.343 | 0.1793 |  |
| Time > 180 (%) | +4.0300 | 3.1184 | ±6.2368 | +1.292 | 0.1962 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **403**, R² = **0.1497**, Adj R² = **0.1257**, F-statistic = **6.26** (p = **1.59e-09**), Residual SE = **16.318** on **391** df, AIC = **3406.1**, BIC = **3454.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.6261** | 8.0981 | ±16.1961 | **+6.993** | **2.70e-12** | *** |
| **Education: graduate level (vs college)** | **-4.6534** | 1.7582 | ±3.5164 | **-2.647** | **0.0081** | ** |
| Education: high school or below (vs college) | -1.2217 | 3.1721 | ±6.3442 | -0.385 | 0.7001 |  |
| Site: UCSD (vs UAB) | -0.8615 | 2.1932 | ±4.3863 | -0.393 | 0.6945 |  |
| **Site: UW (vs UAB)** | **-4.3603** | 2.0014 | ±4.0028 | **-2.179** | **0.0294** | * |
| **Age (years)** | **-0.3174** | 0.0827 | ±0.1655 | **-3.836** | **1.25e-04** | *** |
| **BMI (kg/m2)** | **+0.4676** | 0.1507 | ±0.3015 | **+3.102** | **0.0019** | ** |
| Hypertension | +1.9276 | 1.9091 | ±3.8182 | +1.010 | 0.3126 |  |
| High cholesterol | -0.9217 | 1.7788 | ±3.5576 | -0.518 | 0.6043 |  |
| Kidney disease | -2.6684 | 5.0000 | ±10.0000 | -0.534 | 0.5936 |  |
| Circulatory disease | -2.9901 | 2.2188 | ±4.4376 | -1.348 | 0.1778 |  |
| Avg. daily time > 180 (%) | +5.8238 | 2.9728 | ±5.9456 | +1.959 | 0.0501 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 403)
**Regression Call / Formula**: `stress_mean ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **403**, R² = **0.1523**, Adj R² = **0.1284**, F-statistic = **6.39** (p = **9.33e-10**), Residual SE = **16.293** on **391** df, AIC = **3404.8**, BIC = **3452.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+56.9379** | 7.7197 | ±15.4395 | **+7.376** | **1.64e-13** | *** |
| **Education: graduate level (vs college)** | **-4.5018** | 1.7463 | ±3.4926 | **-2.578** | **0.0099** | ** |
| Education: high school or below (vs college) | -1.6262 | 3.1751 | ±6.3502 | -0.512 | 0.6085 |  |
| Site: UCSD (vs UAB) | -1.0774 | 2.1593 | ±4.3187 | -0.499 | 0.6178 |  |
| **Site: UW (vs UAB)** | **-4.5184** | 2.0041 | ±4.0082 | **-2.255** | **0.0242** | * |
| **Age (years)** | **-0.2935** | 0.0836 | ±0.1672 | **-3.512** | **4.45e-04** | *** |
| **BMI (kg/m2)** | **+0.4471** | 0.1437 | ±0.2873 | **+3.112** | **0.0019** | ** |
| Hypertension | +1.6796 | 1.8998 | ±3.7996 | +0.884 | 0.3766 |  |
| High cholesterol | -1.1172 | 1.7771 | ±3.5543 | -0.629 | 0.5296 |  |
| Kidney disease | -2.4636 | 4.8013 | ±9.6027 | -0.513 | 0.6079 |  |
| Circulatory disease | -2.7249 | 2.2549 | ±4.5098 | -1.208 | 0.2269 |  |
| **Nocturnal time > 180 (%)** | **+5.1317** | 2.4878 | ±4.9756 | **+2.063** | **0.0391** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*
