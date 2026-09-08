# Phase 6b model output tables - Hypoglycaemia exposure: at least one reading < 54 - Non-healthy group (T2D non-insulin + T2D insulin) - Cognition

Each glycaemic measure is entered alone with the Phase 5 covariates; all terms shown in the standard OLS-output format (HC3-robust SEs for OLS; z values and odds ratios for logistic models). [Index of all model-output files](../../../README.md)


---

### MoCA total score (0-30)  (domain: Cognition; outcome sample N = 230; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **230**, R² = **0.1833**, Adj R² = **0.1460**, F-statistic = **4.92** (p = **2.05e-06**), Residual SE = **3.256** on **219** df, AIC = **1206.5**, BIC = **1244.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.3547** | 1.9736 | ±3.9473 | **+15.887** | **7.82e-57** | *** |
| Education: graduate level (vs college) | +0.7762 | 0.4671 | ±0.9342 | +1.662 | 0.0966 | . |
| **Education: high school or below (vs college)** | **-2.8503** | 0.9740 | ±1.9480 | **-2.926** | **0.0034** | ** |
| Site: UCSD (vs UAB) | -0.4450 | 0.5397 | ±1.0793 | -0.825 | 0.4097 |  |
| Site: UW (vs UAB) | -0.7217 | 0.6678 | ±1.3355 | -1.081 | 0.2798 |  |
| **Age (years)** | **-0.0842** | 0.0260 | ±0.0520 | **-3.238** | **0.0012** | ** |
| BMI (kg/m2) | -0.0367 | 0.0268 | ±0.0535 | -1.373 | 0.1699 |  |
| Hypertension | -0.2532 | 0.5054 | ±1.0109 | -0.501 | 0.6165 |  |
| High cholesterol | +0.9235 | 0.5069 | ±1.0137 | +1.822 | 0.0684 | . |
| Kidney disease | +0.8431 | 0.5888 | ±1.1777 | +1.432 | 0.1522 |  |
| Circulatory disease | +0.6298 | 0.5120 | ±1.0240 | +1.230 | 0.2186 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **230**, R² = **0.2056**, Adj R² = **0.1655**, F-statistic = **5.13** (p = **3.84e-07**), Residual SE = **3.219** on **218** df, AIC = **1202.1**, BIC = **1243.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.9782** | 2.1730 | ±4.3459 | **+15.637** | **4.08e-55** | *** |
| Education: graduate level (vs college) | +0.6309 | 0.4726 | ±0.9452 | +1.335 | 0.1819 |  |
| **Education: high school or below (vs college)** | **-2.7025** | 0.9635 | ±1.9270 | **-2.805** | **0.0050** | ** |
| Site: UCSD (vs UAB) | -0.4709 | 0.5329 | ±1.0658 | -0.884 | 0.3769 |  |
| Site: UW (vs UAB) | -0.7868 | 0.6660 | ±1.3320 | -1.181 | 0.2374 |  |
| **Age (years)** | **-0.0767** | 0.0266 | ±0.0533 | **-2.879** | **0.0040** | ** |
| BMI (kg/m2) | -0.0345 | 0.0262 | ±0.0524 | -1.315 | 0.1886 |  |
| Hypertension | -0.1942 | 0.5029 | ±1.0058 | -0.386 | 0.6994 |  |
| High cholesterol | +0.8740 | 0.5061 | ±1.0123 | +1.727 | 0.0842 | . |
| Kidney disease | +0.8858 | 0.5526 | ±1.1052 | +1.603 | 0.1089 |  |
| Circulatory disease | +0.6334 | 0.5003 | ±1.0005 | +1.266 | 0.2054 |  |
| **HbA1c (%)** | **-0.4864** | 0.1995 | ±0.3990 | **-2.438** | **0.0148** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **230**, R² = **0.2006**, Adj R² = **0.1603**, F-statistic = **4.97** (p = **6.80e-07**), Residual SE = **3.229** on **218** df, AIC = **1203.5**, BIC = **1244.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.3562** | 2.1012 | ±4.2023 | **+15.875** | **9.43e-57** | *** |
| Education: graduate level (vs college) | +0.7417 | 0.4673 | ±0.9347 | +1.587 | 0.1125 |  |
| **Education: high school or below (vs college)** | **-2.7335** | 0.9713 | ±1.9427 | **-2.814** | **0.0049** | ** |
| Site: UCSD (vs UAB) | -0.4472 | 0.5228 | ±1.0455 | -0.855 | 0.3923 |  |
| Site: UW (vs UAB) | -0.7742 | 0.6700 | ±1.3399 | -1.156 | 0.2479 |  |
| **Age (years)** | **-0.0841** | 0.0265 | ±0.0531 | **-3.167** | **0.0015** | ** |
| BMI (kg/m2) | -0.0371 | 0.0263 | ±0.0527 | -1.408 | 0.1593 |  |
| Hypertension | -0.2196 | 0.5010 | ±1.0019 | -0.438 | 0.6612 |  |
| High cholesterol | +0.9039 | 0.5081 | ±1.0162 | +1.779 | 0.0752 | . |
| Kidney disease | +0.9653 | 0.5829 | ±1.1658 | +1.656 | 0.0977 | . |
| Circulatory disease | +0.6689 | 0.4958 | ±0.9916 | +1.349 | 0.1773 |  |
| **Mean glucose (mg/dL)** | **-0.0149** | 0.0076 | ±0.0152 | **-1.971** | **0.0487** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **230**, R² = **0.2006**, Adj R² = **0.1603**, F-statistic = **4.97** (p = **6.80e-07**), Residual SE = **3.229** on **218** df, AIC = **1203.5**, BIC = **1244.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+35.4248** | 2.6509 | ±5.3018 | **+13.363** | **9.91e-41** | *** |
| Education: graduate level (vs college) | +0.7417 | 0.4673 | ±0.9347 | +1.587 | 0.1125 |  |
| **Education: high school or below (vs college)** | **-2.7335** | 0.9713 | ±1.9427 | **-2.814** | **0.0049** | ** |
| Site: UCSD (vs UAB) | -0.4472 | 0.5228 | ±1.0455 | -0.855 | 0.3923 |  |
| Site: UW (vs UAB) | -0.7742 | 0.6700 | ±1.3399 | -1.156 | 0.2479 |  |
| **Age (years)** | **-0.0841** | 0.0265 | ±0.0531 | **-3.167** | **0.0015** | ** |
| BMI (kg/m2) | -0.0371 | 0.0263 | ±0.0527 | -1.408 | 0.1593 |  |
| Hypertension | -0.2196 | 0.5010 | ±1.0019 | -0.438 | 0.6612 |  |
| High cholesterol | +0.9039 | 0.5081 | ±1.0162 | +1.779 | 0.0752 | . |
| Kidney disease | +0.9653 | 0.5829 | ±1.1658 | +1.656 | 0.0977 | . |
| Circulatory disease | +0.6689 | 0.4958 | ±0.9916 | +1.349 | 0.1773 |  |
| **GMI (%)** | **-0.6249** | 0.3170 | ±0.6341 | **-1.971** | **0.0487** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **230**, R² = **0.2021**, Adj R² = **0.1618**, F-statistic = **5.02** (p = **5.74e-07**), Residual SE = **3.226** on **218** df, AIC = **1203.1**, BIC = **1244.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+33.3954** | 2.0812 | ±4.1624 | **+16.046** | **6.06e-58** | *** |
| Education: graduate level (vs college) | +0.7894 | 0.4708 | ±0.9416 | +1.677 | 0.0936 | . |
| **Education: high school or below (vs college)** | **-2.7363** | 0.9673 | ±1.9345 | **-2.829** | **0.0047** | ** |
| Site: UCSD (vs UAB) | -0.4463 | 0.5202 | ±1.0404 | -0.858 | 0.3909 |  |
| Site: UW (vs UAB) | -0.7609 | 0.6731 | ±1.3462 | -1.130 | 0.2583 |  |
| **Age (years)** | **-0.0866** | 0.0262 | ±0.0525 | **-3.299** | **9.69e-04** | *** |
| BMI (kg/m2) | -0.0360 | 0.0263 | ±0.0526 | -1.370 | 0.1708 |  |
| Hypertension | -0.1917 | 0.4970 | ±0.9940 | -0.386 | 0.6997 |  |
| High cholesterol | +0.9444 | 0.5043 | ±1.0086 | +1.873 | 0.0611 | . |
| Kidney disease | +0.8579 | 0.5818 | ±1.1636 | +1.475 | 0.1403 |  |
| Circulatory disease | +0.6721 | 0.4951 | ±0.9901 | +1.358 | 0.1746 |  |
| **Nocturnal mean 00-06h (mg/dL)** | **-0.0153** | 0.0070 | ±0.0139 | **-2.195** | **0.0282** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **230**, R² = **0.1955**, Adj R² = **0.1549**, F-statistic = **4.82** (p = **1.22e-06**), Residual SE = **3.239** on **218** df, AIC = **1205.0**, BIC = **1246.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.9959** | 1.9761 | ±3.9522 | **+16.191** | **5.79e-59** | *** |
| Education: graduate level (vs college) | +0.6810 | 0.4647 | ±0.9294 | +1.465 | 0.1428 |  |
| **Education: high school or below (vs college)** | **-2.6534** | 0.9677 | ±1.9353 | **-2.742** | **0.0061** | ** |
| Site: UCSD (vs UAB) | -0.4696 | 0.5304 | ±1.0607 | -0.885 | 0.3760 |  |
| Site: UW (vs UAB) | -0.7910 | 0.6689 | ±1.3378 | -1.182 | 0.2370 |  |
| **Age (years)** | **-0.0785** | 0.0275 | ±0.0549 | **-2.857** | **0.0043** | ** |
| BMI (kg/m2) | -0.0395 | 0.0267 | ±0.0533 | -1.481 | 0.1385 |  |
| Hypertension | -0.2329 | 0.5052 | ±1.0104 | -0.461 | 0.6449 |  |
| High cholesterol | +0.8884 | 0.5112 | ±1.0224 | +1.738 | 0.0822 | . |
| Kidney disease | +1.1034 | 0.5838 | ±1.1676 | +1.890 | 0.0587 | . |
| Circulatory disease | +0.6225 | 0.5010 | ±1.0019 | +1.243 | 0.2140 |  |
| Glucose SD, pooled (mg/dL) | -0.0267 | 0.0149 | ±0.0297 | -1.796 | 0.0724 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **230**, R² = **0.1930**, Adj R² = **0.1523**, F-statistic = **4.74** (p = **1.62e-06**), Residual SE = **3.244** on **218** df, AIC = **1205.7**, BIC = **1247.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.9731** | 1.9772 | ±3.9543 | **+16.171** | **8.04e-59** | *** |
| Education: graduate level (vs college) | +0.6876 | 0.4638 | ±0.9276 | +1.483 | 0.1382 |  |
| **Education: high school or below (vs college)** | **-2.6457** | 0.9679 | ±1.9357 | **-2.733** | **0.0063** | ** |
| Site: UCSD (vs UAB) | -0.4657 | 0.5338 | ±1.0676 | -0.872 | 0.3830 |  |
| Site: UW (vs UAB) | -0.7730 | 0.6699 | ±1.3399 | -1.154 | 0.2486 |  |
| **Age (years)** | **-0.0790** | 0.0274 | ±0.0548 | **-2.881** | **0.0040** | ** |
| BMI (kg/m2) | -0.0398 | 0.0267 | ±0.0534 | -1.493 | 0.1354 |  |
| Hypertension | -0.2496 | 0.5078 | ±1.0156 | -0.492 | 0.6231 |  |
| High cholesterol | +0.8994 | 0.5113 | ±1.0226 | +1.759 | 0.0786 | . |
| Kidney disease | +1.0828 | 0.5822 | ±1.1643 | +1.860 | 0.0629 | . |
| Circulatory disease | +0.6117 | 0.5038 | ±1.0077 | +1.214 | 0.2248 |  |
| Avg. daily SD (mg/dL) | -0.0280 | 0.0180 | ±0.0360 | -1.557 | 0.1195 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **230**, R² = **0.1868**, Adj R² = **0.1457**, F-statistic = **4.55** (p = **3.26e-06**), Residual SE = **3.256** on **218** df, AIC = **1207.5**, BIC = **1248.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.8891** | 1.9448 | ±3.8896 | **+16.397** | **2.00e-60** | *** |
| Education: graduate level (vs college) | +0.7100 | 0.4638 | ±0.9277 | +1.531 | 0.1258 |  |
| **Education: high school or below (vs college)** | **-2.7266** | 0.9659 | ±1.9317 | **-2.823** | **0.0048** | ** |
| Site: UCSD (vs UAB) | -0.4600 | 0.5397 | ±1.0794 | -0.852 | 0.3940 |  |
| Site: UW (vs UAB) | -0.7576 | 0.6682 | ±1.3364 | -1.134 | 0.2569 |  |
| **Age (years)** | **-0.0787** | 0.0278 | ±0.0555 | **-2.835** | **0.0046** | ** |
| BMI (kg/m2) | -0.0388 | 0.0268 | ±0.0536 | -1.449 | 0.1475 |  |
| Hypertension | -0.2510 | 0.5079 | ±1.0158 | -0.494 | 0.6212 |  |
| High cholesterol | +0.9070 | 0.5111 | ±1.0222 | +1.774 | 0.0760 | . |
| Kidney disease | +1.0157 | 0.5791 | ±1.1581 | +1.754 | 0.0794 | . |
| Circulatory disease | +0.6197 | 0.5100 | ±1.0201 | +1.215 | 0.2243 |  |
| CV (%) | -0.0329 | 0.0278 | ±0.0556 | -1.183 | 0.2368 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **230**, R² = **0.1868**, Adj R² = **0.1457**, F-statistic = **4.55** (p = **3.26e-06**), Residual SE = **3.256** on **218** df, AIC = **1207.5**, BIC = **1248.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.2902** | 2.3315 | ±4.6630 | **+12.992** | **1.36e-38** | *** |
| Education: graduate level (vs college) | +0.7102 | 0.4620 | ±0.9240 | +1.537 | 0.1242 |  |
| **Education: high school or below (vs college)** | **-2.7243** | 0.9621 | ±1.9242 | **-2.832** | **0.0046** | ** |
| Site: UCSD (vs UAB) | -0.4409 | 0.5385 | ±1.0770 | -0.819 | 0.4129 |  |
| Site: UW (vs UAB) | -0.7443 | 0.6674 | ±1.3347 | -1.115 | 0.2647 |  |
| **Age (years)** | **-0.0783** | 0.0275 | ±0.0550 | **-2.849** | **0.0044** | ** |
| BMI (kg/m2) | -0.0379 | 0.0269 | ±0.0537 | -1.411 | 0.1582 |  |
| Hypertension | -0.2628 | 0.5080 | ±1.0160 | -0.517 | 0.6049 |  |
| High cholesterol | +0.9058 | 0.5122 | ±1.0244 | +1.769 | 0.0770 | . |
| Kidney disease | +0.9654 | 0.5811 | ±1.1623 | +1.661 | 0.0967 | . |
| Circulatory disease | +0.6433 | 0.5110 | ±1.0221 | +1.259 | 0.2081 |  |
| Mean / SD ratio | +0.1666 | 0.1442 | ±0.2883 | +1.156 | 0.2478 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **230**, R² = **0.1837**, Adj R² = **0.1426**, F-statistic = **4.46** (p = **4.56e-06**), Residual SE = **3.262** on **218** df, AIC = **1208.3**, BIC = **1249.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+30.9850** | 2.3036 | ±4.6072 | **+13.451** | **3.05e-41** | *** |
| Education: graduate level (vs college) | +0.7498 | 0.4623 | ±0.9247 | +1.622 | 0.1049 |  |
| **Education: high school or below (vs college)** | **-2.8048** | 0.9611 | ±1.9223 | **-2.918** | **0.0035** | ** |
| Site: UCSD (vs UAB) | -0.4396 | 0.5403 | ±1.0806 | -0.814 | 0.4159 |  |
| Site: UW (vs UAB) | -0.7253 | 0.6694 | ±1.3388 | -1.083 | 0.2786 |  |
| **Age (years)** | **-0.0820** | 0.0274 | ±0.0548 | **-2.994** | **0.0028** | ** |
| BMI (kg/m2) | -0.0373 | 0.0268 | ±0.0537 | -1.389 | 0.1647 |  |
| Hypertension | -0.2622 | 0.5073 | ±1.0146 | -0.517 | 0.6053 |  |
| High cholesterol | +0.9214 | 0.5101 | ±1.0201 | +1.806 | 0.0709 | . |
| Kidney disease | +0.8766 | 0.5821 | ±1.1643 | +1.506 | 0.1321 |  |
| Circulatory disease | +0.6309 | 0.5126 | ±1.0252 | +1.231 | 0.2184 |  |
| Avg. daily mean/SD | +0.0488 | 0.1217 | ±0.2434 | +0.401 | 0.6886 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **230**, R² = **0.1838**, Adj R² = **0.1426**, F-statistic = **4.46** (p = **4.56e-06**), Residual SE = **3.262** on **218** df, AIC = **1208.3**, BIC = **1249.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.6222** | 2.0491 | ±4.0982 | **+15.432** | **9.92e-54** | *** |
| Education: graduate level (vs college) | +0.7628 | 0.4670 | ±0.9341 | +1.633 | 0.1024 |  |
| **Education: high school or below (vs college)** | **-2.8092** | 0.9724 | ±1.9447 | **-2.889** | **0.0039** | ** |
| Site: UCSD (vs UAB) | -0.4359 | 0.5393 | ±1.0786 | -0.808 | 0.4189 |  |
| Site: UW (vs UAB) | -0.7374 | 0.6692 | ±1.3384 | -1.102 | 0.2705 |  |
| **Age (years)** | **-0.0838** | 0.0264 | ±0.0529 | **-3.167** | **0.0015** | ** |
| BMI (kg/m2) | -0.0360 | 0.0271 | ±0.0543 | -1.326 | 0.1850 |  |
| Hypertension | -0.2596 | 0.5107 | ±1.0214 | -0.508 | 0.6113 |  |
| High cholesterol | +0.9266 | 0.5089 | ±1.0177 | +1.821 | 0.0686 | . |
| Kidney disease | +0.8460 | 0.5920 | ±1.1840 | +1.429 | 0.1530 |  |
| Circulatory disease | +0.6292 | 0.5143 | ±1.0286 | +1.224 | 0.2211 |  |
| MAG (mg/dL/h) | -0.0071 | 0.0217 | ±0.0435 | -0.325 | 0.7452 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **230**, R² = **0.1873**, Adj R² = **0.1463**, F-statistic = **4.57** (p = **3.07e-06**), Residual SE = **3.255** on **218** df, AIC = **1207.3**, BIC = **1248.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.9310** | 1.9751 | ±3.9503 | **+16.167** | **8.68e-59** | *** |
| Education: graduate level (vs college) | +0.7148 | 0.4632 | ±0.9264 | +1.543 | 0.1228 |  |
| **Education: high school or below (vs college)** | **-2.7053** | 0.9741 | ±1.9482 | **-2.777** | **0.0055** | ** |
| Site: UCSD (vs UAB) | -0.4565 | 0.5381 | ±1.0761 | -0.848 | 0.3962 |  |
| Site: UW (vs UAB) | -0.7453 | 0.6708 | ±1.3417 | -1.111 | 0.2666 |  |
| **Age (years)** | **-0.0811** | 0.0273 | ±0.0546 | **-2.969** | **0.0030** | ** |
| BMI (kg/m2) | -0.0391 | 0.0267 | ±0.0534 | -1.464 | 0.1433 |  |
| Hypertension | -0.2641 | 0.5110 | ±1.0221 | -0.517 | 0.6053 |  |
| High cholesterol | +0.9169 | 0.5115 | ±1.0230 | +1.793 | 0.0730 | . |
| Kidney disease | +0.9932 | 0.5829 | ±1.1658 | +1.704 | 0.0884 | . |
| Circulatory disease | +0.6363 | 0.5085 | ±1.0170 | +1.251 | 0.2109 |  |
| Avg. daily range (mg/dL) | -0.0051 | 0.0053 | ±0.0105 | -0.971 | 0.3318 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **230**, R² = **0.1988**, Adj R² = **0.1584**, F-statistic = **4.92** (p = **8.39e-07**), Residual SE = **3.232** on **218** df, AIC = **1204.0**, BIC = **1245.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.7710** | 1.9869 | ±3.9737 | **+15.990** | **1.49e-57** | *** |
| Education: graduate level (vs college) | +0.6738 | 0.4671 | ±0.9342 | +1.442 | 0.1492 |  |
| **Education: high school or below (vs college)** | **-2.7933** | 0.9604 | ±1.9208 | **-2.908** | **0.0036** | ** |
| Site: UCSD (vs UAB) | -0.4501 | 0.5227 | ±1.0453 | -0.861 | 0.3892 |  |
| Site: UW (vs UAB) | -0.8033 | 0.6676 | ±1.3351 | -1.203 | 0.2288 |  |
| **Age (years)** | **-0.0810** | 0.0269 | ±0.0537 | **-3.014** | **0.0026** | ** |
| BMI (kg/m2) | -0.0390 | 0.0266 | ±0.0532 | -1.468 | 0.1421 |  |
| Hypertension | -0.1537 | 0.4988 | ±0.9975 | -0.308 | 0.7580 |  |
| High cholesterol | +0.8887 | 0.5086 | ±1.0173 | +1.747 | 0.0806 | . |
| Kidney disease | +1.0385 | 0.5887 | ±1.1774 | +1.764 | 0.0777 | . |
| Circulatory disease | +0.6995 | 0.5045 | ±1.0089 | +1.387 | 0.1656 |  |
| **SD of daily means (mg/dL)** | **-0.0473** | 0.0222 | ±0.0444 | **-2.133** | **0.0329** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **230**, R² = **0.2064**, Adj R² = **0.1663**, F-statistic = **5.15** (p = **3.49e-07**), Residual SE = **3.217** on **218** df, AIC = **1201.9**, BIC = **1243.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.6832** | 2.3990 | ±4.7979 | **+11.957** | **6.00e-33** | *** |
| Education: graduate level (vs college) | +0.6486 | 0.4628 | ±0.9255 | +1.402 | 0.1611 |  |
| **Education: high school or below (vs college)** | **-2.7043** | 0.9692 | ±1.9384 | **-2.790** | **0.0053** | ** |
| Site: UCSD (vs UAB) | -0.4771 | 0.5178 | ±1.0356 | -0.921 | 0.3569 |  |
| Site: UW (vs UAB) | -0.8151 | 0.6677 | ±1.3354 | -1.221 | 0.2222 |  |
| **Age (years)** | **-0.0811** | 0.0268 | ±0.0535 | **-3.029** | **0.0025** | ** |
| BMI (kg/m2) | -0.0391 | 0.0262 | ±0.0523 | -1.495 | 0.1348 |  |
| Hypertension | -0.2533 | 0.4972 | ±0.9943 | -0.510 | 0.6104 |  |
| High cholesterol | +0.9433 | 0.5075 | ±1.0149 | +1.859 | 0.0630 | . |
| Kidney disease | +1.0737 | 0.5823 | ±1.1645 | +1.844 | 0.0652 | . |
| Circulatory disease | +0.6969 | 0.4927 | ±0.9855 | +1.414 | 0.1572 |  |
| **Time in range 70-180, pooled (%)** | **+0.0305** | 0.0132 | ±0.0263 | **+2.315** | **0.0206** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **230**, R² = **0.2059**, Adj R² = **0.1658**, F-statistic = **5.14** (p = **3.69e-07**), Residual SE = **3.218** on **218** df, AIC = **1202.0**, BIC = **1243.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+28.7212** | 2.3934 | ±4.7867 | **+12.000** | **3.54e-33** | *** |
| Education: graduate level (vs college) | +0.6507 | 0.4628 | ±0.9257 | +1.406 | 0.1597 |  |
| **Education: high school or below (vs college)** | **-2.6918** | 0.9695 | ±1.9390 | **-2.776** | **0.0055** | ** |
| Site: UCSD (vs UAB) | -0.4805 | 0.5187 | ±1.0374 | -0.926 | 0.3543 |  |
| Site: UW (vs UAB) | -0.8212 | 0.6681 | ±1.3363 | -1.229 | 0.2190 |  |
| **Age (years)** | **-0.0811** | 0.0267 | ±0.0535 | **-3.034** | **0.0024** | ** |
| BMI (kg/m2) | -0.0395 | 0.0262 | ±0.0524 | -1.507 | 0.1317 |  |
| Hypertension | -0.2596 | 0.4973 | ±0.9946 | -0.522 | 0.6016 |  |
| High cholesterol | +0.9449 | 0.5075 | ±1.0151 | +1.862 | 0.0626 | . |
| Kidney disease | +1.0785 | 0.5808 | ±1.1617 | +1.857 | 0.0633 | . |
| Circulatory disease | +0.6965 | 0.4930 | ±0.9861 | +1.413 | 0.1578 |  |
| **Avg. daily time in range 70-180 (%)** | **+0.0301** | 0.0132 | ±0.0264 | **+2.277** | **0.0228** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **230**, R² = **0.1834**, Adj R² = **0.1422**, F-statistic = **4.45** (p = **4.72e-06**), Residual SE = **3.263** on **218** df, AIC = **1208.4**, BIC = **1249.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.3736** | 1.9738 | ±3.9476 | **+15.895** | **6.84e-57** | *** |
| Education: graduate level (vs college) | +0.7713 | 0.4686 | ±0.9372 | +1.646 | 0.0997 | . |
| **Education: high school or below (vs college)** | **-2.8581** | 0.9762 | ±1.9524 | **-2.928** | **0.0034** | ** |
| Site: UCSD (vs UAB) | -0.4586 | 0.5457 | ±1.0913 | -0.840 | 0.4007 |  |
| Site: UW (vs UAB) | -0.7382 | 0.6750 | ±1.3500 | -1.094 | 0.2741 |  |
| **Age (years)** | **-0.0841** | 0.0261 | ±0.0521 | **-3.226** | **0.0013** | ** |
| BMI (kg/m2) | -0.0366 | 0.0272 | ±0.0543 | -1.350 | 0.1772 |  |
| Hypertension | -0.2506 | 0.5073 | ±1.0147 | -0.494 | 0.6213 |  |
| High cholesterol | +0.9252 | 0.5087 | ±1.0174 | +1.819 | 0.0689 | . |
| Kidney disease | +0.8403 | 0.5905 | ±1.1810 | +1.423 | 0.1547 |  |
| Circulatory disease | +0.6390 | 0.5180 | ±1.0361 | +1.233 | 0.2174 |  |
| Time < 54 (%) | -0.0567 | 0.5078 | ±1.0155 | -0.112 | 0.9111 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **230**, R² = **0.1835**, Adj R² = **0.1423**, F-statistic = **4.45** (p = **4.67e-06**), Residual SE = **3.263** on **218** df, AIC = **1208.4**, BIC = **1249.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.3606** | 1.9763 | ±3.9526 | **+15.868** | **1.05e-56** | *** |
| Education: graduate level (vs college) | +0.7672 | 0.4669 | ±0.9338 | +1.643 | 0.1004 |  |
| **Education: high school or below (vs college)** | **-2.8594** | 0.9764 | ±1.9528 | **-2.928** | **0.0034** | ** |
| Site: UCSD (vs UAB) | -0.4589 | 0.5445 | ±1.0891 | -0.843 | 0.3994 |  |
| Site: UW (vs UAB) | -0.7374 | 0.6712 | ±1.3424 | -1.099 | 0.2719 |  |
| **Age (years)** | **-0.0838** | 0.0261 | ±0.0522 | **-3.208** | **0.0013** | ** |
| BMI (kg/m2) | -0.0367 | 0.0269 | ±0.0538 | -1.364 | 0.1726 |  |
| Hypertension | -0.2518 | 0.5070 | ±1.0140 | -0.497 | 0.6194 |  |
| High cholesterol | +0.9207 | 0.5105 | ±1.0210 | +1.803 | 0.0713 | . |
| Kidney disease | +0.8442 | 0.5910 | ±1.1820 | +1.428 | 0.1532 |  |
| Circulatory disease | +0.6406 | 0.5165 | ±1.0329 | +1.240 | 0.2149 |  |
| Avg. daily time < 54 (%) | -0.0667 | 0.3524 | ±0.7048 | -0.189 | 0.8499 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **230**, R² = **0.1837**, Adj R² = **0.1425**, F-statistic = **4.46** (p = **4.60e-06**), Residual SE = **3.263** on **218** df, AIC = **1208.3**, BIC = **1249.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.3580** | 1.9864 | ±3.9728 | **+15.786** | **3.86e-56** | *** |
| Education: graduate level (vs college) | +0.7539 | 0.4763 | ±0.9525 | +1.583 | 0.1134 |  |
| **Education: high school or below (vs college)** | **-2.8437** | 0.9800 | ±1.9600 | **-2.902** | **0.0037** | ** |
| Site: UCSD (vs UAB) | -0.4550 | 0.5450 | ±1.0900 | -0.835 | 0.4038 |  |
| Site: UW (vs UAB) | -0.7279 | 0.6715 | ±1.3429 | -1.084 | 0.2784 |  |
| **Age (years)** | **-0.0833** | 0.0260 | ±0.0521 | **-3.197** | **0.0014** | ** |
| BMI (kg/m2) | -0.0369 | 0.0269 | ±0.0538 | -1.372 | 0.1700 |  |
| Hypertension | -0.2594 | 0.5048 | ±1.0097 | -0.514 | 0.6073 |  |
| High cholesterol | +0.9312 | 0.5095 | ±1.0190 | +1.828 | 0.0676 | . |
| Kidney disease | +0.8501 | 0.5930 | ±1.1860 | +1.434 | 0.1517 |  |
| Circulatory disease | +0.6326 | 0.5158 | ±1.0316 | +1.226 | 0.2201 |  |
| Time 54-69, pooled (%) | -0.0277 | 0.0994 | ±0.1987 | -0.279 | 0.7805 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **230**, R² = **0.1836**, Adj R² = **0.1424**, F-statistic = **4.46** (p = **4.65e-06**), Residual SE = **3.263** on **218** df, AIC = **1208.4**, BIC = **1249.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.3468** | 1.9835 | ±3.9670 | **+15.804** | **2.92e-56** | *** |
| Education: graduate level (vs college) | +0.7573 | 0.4775 | ±0.9550 | +1.586 | 0.1127 |  |
| **Education: high school or below (vs college)** | **-2.8427** | 0.9813 | ±1.9627 | **-2.897** | **0.0038** | ** |
| Site: UCSD (vs UAB) | -0.4527 | 0.5455 | ±1.0910 | -0.830 | 0.4067 |  |
| Site: UW (vs UAB) | -0.7274 | 0.6724 | ±1.3448 | -1.082 | 0.2794 |  |
| **Age (years)** | **-0.0833** | 0.0260 | ±0.0521 | **-3.199** | **0.0014** | ** |
| BMI (kg/m2) | -0.0368 | 0.0269 | ±0.0538 | -1.370 | 0.1707 |  |
| Hypertension | -0.2584 | 0.5053 | ±1.0106 | -0.511 | 0.6090 |  |
| High cholesterol | +0.9289 | 0.5099 | ±1.0198 | +1.822 | 0.0685 | . |
| Kidney disease | +0.8478 | 0.5922 | ±1.1844 | +1.432 | 0.1523 |  |
| Circulatory disease | +0.6306 | 0.5166 | ±1.0331 | +1.221 | 0.2222 |  |
| Avg. daily time 54-69 (%) | -0.0222 | 0.0988 | ±0.1977 | -0.225 | 0.8223 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **230**, R² = **0.1837**, Adj R² = **0.1425**, F-statistic = **4.46** (p = **4.61e-06**), Residual SE = **3.263** on **218** df, AIC = **1208.4**, BIC = **1249.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.3648** | 1.9855 | ±3.9709 | **+15.797** | **3.25e-56** | *** |
| Education: graduate level (vs college) | +0.7562 | 0.4744 | ±0.9488 | +1.594 | 0.1110 |  |
| **Education: high school or below (vs college)** | **-2.8481** | 0.9786 | ±1.9571 | **-2.910** | **0.0036** | ** |
| Site: UCSD (vs UAB) | -0.4585 | 0.5457 | ±1.0913 | -0.840 | 0.4008 |  |
| Site: UW (vs UAB) | -0.7332 | 0.6704 | ±1.3409 | -1.094 | 0.2741 |  |
| **Age (years)** | **-0.0834** | 0.0261 | ±0.0522 | **-3.197** | **0.0014** | ** |
| BMI (kg/m2) | -0.0368 | 0.0269 | ±0.0538 | -1.370 | 0.1708 |  |
| Hypertension | -0.2572 | 0.5057 | ±1.0114 | -0.509 | 0.6110 |  |
| High cholesterol | +0.9304 | 0.5090 | ±1.0179 | +1.828 | 0.0675 | . |
| Kidney disease | +0.8477 | 0.5924 | ±1.1849 | +1.431 | 0.1525 |  |
| Circulatory disease | +0.6357 | 0.5156 | ±1.0312 | +1.233 | 0.2176 |  |
| Time < 70 (%) | -0.0225 | 0.0842 | ±0.1684 | -0.267 | 0.7896 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **230**, R² = **0.1836**, Adj R² = **0.1424**, F-statistic = **4.46** (p = **4.64e-06**), Residual SE = **3.263** on **218** df, AIC = **1208.4**, BIC = **1249.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.3496** | 1.9832 | ±3.9663 | **+15.808** | **2.74e-56** | *** |
| Education: graduate level (vs college) | +0.7573 | 0.4744 | ±0.9489 | +1.596 | 0.1105 |  |
| **Education: high school or below (vs college)** | **-2.8463** | 0.9791 | ±1.9582 | **-2.907** | **0.0036** | ** |
| Site: UCSD (vs UAB) | -0.4556 | 0.5461 | ±1.0922 | -0.834 | 0.4041 |  |
| Site: UW (vs UAB) | -0.7312 | 0.6715 | ±1.3430 | -1.089 | 0.2762 |  |
| **Age (years)** | **-0.0833** | 0.0261 | ±0.0522 | **-3.194** | **0.0014** | ** |
| BMI (kg/m2) | -0.0368 | 0.0269 | ±0.0538 | -1.370 | 0.1708 |  |
| Hypertension | -0.2573 | 0.5061 | ±1.0123 | -0.508 | 0.6111 |  |
| High cholesterol | +0.9274 | 0.5092 | ±1.0183 | +1.821 | 0.0685 | . |
| Kidney disease | +0.8475 | 0.5918 | ±1.1835 | +1.432 | 0.1521 |  |
| Circulatory disease | +0.6336 | 0.5156 | ±1.0311 | +1.229 | 0.2191 |  |
| Avg. daily time < 70 (%) | -0.0192 | 0.0791 | ±0.1581 | -0.243 | 0.8079 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **230**, R² = **0.2071**, Adj R² = **0.1670**, F-statistic = **5.18** (p = **3.23e-07**), Residual SE = **3.216** on **218** df, AIC = **1201.7**, BIC = **1242.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+25.6350** | 3.4952 | ±6.9905 | **+7.334** | **2.23e-13** | *** |
| Education: graduate level (vs college) | +0.6915 | 0.4668 | ±0.9336 | +1.481 | 0.1385 |  |
| **Education: high school or below (vs college)** | **-2.6917** | 0.9760 | ±1.9520 | **-2.758** | **0.0058** | ** |
| Site: UCSD (vs UAB) | -0.4973 | 0.5193 | ±1.0387 | -0.957 | 0.3383 |  |
| Site: UW (vs UAB) | -0.8631 | 0.6676 | ±1.3351 | -1.293 | 0.1960 |  |
| **Age (years)** | **-0.0852** | 0.0264 | ±0.0528 | **-3.230** | **0.0012** | ** |
| BMI (kg/m2) | -0.0395 | 0.0266 | ±0.0532 | -1.485 | 0.1375 |  |
| Hypertension | -0.2103 | 0.5064 | ±1.0128 | -0.415 | 0.6779 |  |
| High cholesterol | +0.8581 | 0.5101 | ±1.0202 | +1.682 | 0.0925 | . |
| Kidney disease | +0.9528 | 0.5895 | ±1.1790 | +1.616 | 0.1060 |  |
| Circulatory disease | +0.7058 | 0.4903 | ±0.9805 | +1.440 | 0.1500 |  |
| **Time 54-250, pooled (%)** | **+0.0612** | 0.0283 | ±0.0566 | **+2.165** | **0.0304** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **230**, R² = **0.2111**, Adj R² = **0.1713**, F-statistic = **5.30** (p = **2.01e-07**), Residual SE = **3.207** on **218** df, AIC = **1200.5**, BIC = **1241.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+24.4265** | 3.6888 | ±7.3776 | **+6.622** | **3.55e-11** | *** |
| Education: graduate level (vs college) | +0.6761 | 0.4671 | ±0.9343 | +1.447 | 0.1478 |  |
| **Education: high school or below (vs college)** | **-2.6456** | 0.9720 | ±1.9441 | **-2.722** | **0.0065** | ** |
| Site: UCSD (vs UAB) | -0.4890 | 0.5146 | ±1.0293 | -0.950 | 0.3420 |  |
| Site: UW (vs UAB) | -0.8629 | 0.6684 | ±1.3368 | -1.291 | 0.1967 |  |
| **Age (years)** | **-0.0846** | 0.0264 | ±0.0529 | **-3.199** | **0.0014** | ** |
| BMI (kg/m2) | -0.0408 | 0.0266 | ±0.0532 | -1.535 | 0.1247 |  |
| Hypertension | -0.2041 | 0.5050 | ±1.0100 | -0.404 | 0.6862 |  |
| High cholesterol | +0.8553 | 0.5090 | ±1.0180 | +1.680 | 0.0929 | . |
| Kidney disease | +0.9887 | 0.5867 | ±1.1735 | +1.685 | 0.0920 | . |
| Circulatory disease | +0.7332 | 0.4895 | ±0.9791 | +1.498 | 0.1342 |  |
| **Avg. daily time 54-250 (%)** | **+0.0733** | 0.0306 | ±0.0612 | **+2.398** | **0.0165** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **230**, R² = **0.1945**, Adj R² = **0.1538**, F-statistic = **4.78** (p = **1.37e-06**), Residual SE = **3.241** on **218** df, AIC = **1205.3**, BIC = **1246.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.5318** | 1.9694 | ±3.9389 | **+16.011** | **1.08e-57** | *** |
| Education: graduate level (vs college) | +0.7134 | 0.4625 | ±0.9251 | +1.542 | 0.1230 |  |
| **Education: high school or below (vs college)** | **-2.7886** | 0.9681 | ±1.9362 | **-2.880** | **0.0040** | ** |
| Site: UCSD (vs UAB) | -0.4398 | 0.5276 | ±1.0552 | -0.834 | 0.4045 |  |
| Site: UW (vs UAB) | -0.7384 | 0.6679 | ±1.3357 | -1.106 | 0.2689 |  |
| **Age (years)** | **-0.0815** | 0.0267 | ±0.0534 | **-3.053** | **0.0023** | ** |
| BMI (kg/m2) | -0.0376 | 0.0262 | ±0.0525 | -1.432 | 0.1520 |  |
| Hypertension | -0.2682 | 0.5010 | ±1.0020 | -0.535 | 0.5924 |  |
| High cholesterol | +0.9687 | 0.5094 | ±1.0189 | +1.902 | 0.0572 | . |
| Kidney disease | +1.0165 | 0.5822 | ±1.1645 | +1.746 | 0.0808 | . |
| Circulatory disease | +0.6569 | 0.5060 | ±1.0121 | +1.298 | 0.1943 |  |
| Time 181-250, pooled (%) | -0.0314 | 0.0194 | ±0.0388 | -1.621 | 0.1051 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **230**, R² = **0.1940**, Adj R² = **0.1534**, F-statistic = **4.77** (p = **1.44e-06**), Residual SE = **3.242** on **218** df, AIC = **1205.4**, BIC = **1246.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.5734** | 1.9697 | ±3.9395 | **+16.029** | **7.99e-58** | *** |
| Education: graduate level (vs college) | +0.7179 | 0.4626 | ±0.9252 | +1.552 | 0.1207 |  |
| **Education: high school or below (vs college)** | **-2.7867** | 0.9696 | ±1.9392 | **-2.874** | **0.0041** | ** |
| Site: UCSD (vs UAB) | -0.4519 | 0.5294 | ±1.0588 | -0.854 | 0.3933 |  |
| Site: UW (vs UAB) | -0.7552 | 0.6676 | ±1.3352 | -1.131 | 0.2580 |  |
| **Age (years)** | **-0.0822** | 0.0266 | ±0.0532 | **-3.092** | **0.0020** | ** |
| BMI (kg/m2) | -0.0377 | 0.0263 | ±0.0526 | -1.434 | 0.1516 |  |
| Hypertension | -0.2724 | 0.5013 | ±1.0026 | -0.543 | 0.5868 |  |
| High cholesterol | +0.9651 | 0.5092 | ±1.0184 | +1.895 | 0.0580 | . |
| Kidney disease | +1.0107 | 0.5821 | ±1.1641 | +1.736 | 0.0825 | . |
| Circulatory disease | +0.6528 | 0.5057 | ±1.0113 | +1.291 | 0.1967 |  |
| Avg. daily time 181-250 (%) | -0.0298 | 0.0185 | ±0.0370 | -1.613 | 0.1068 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **230**, R² = **0.2046**, Adj R² = **0.1645**, F-statistic = **5.10** (p = **4.30e-07**), Residual SE = **3.221** on **218** df, AIC = **1202.4**, BIC = **1243.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.6957** | 1.9751 | ±3.9501 | **+16.048** | **5.91e-58** | *** |
| Education: graduate level (vs college) | +0.6815 | 0.4636 | ±0.9272 | +1.470 | 0.1415 |  |
| **Education: high school or below (vs college)** | **-2.7156** | 0.9689 | ±1.9378 | **-2.803** | **0.0051** | ** |
| Site: UCSD (vs UAB) | -0.4579 | 0.5180 | ±1.0359 | -0.884 | 0.3767 |  |
| Site: UW (vs UAB) | -0.7950 | 0.6682 | ±1.3364 | -1.190 | 0.2342 |  |
| **Age (years)** | **-0.0823** | 0.0266 | ±0.0533 | **-3.088** | **0.0020** | ** |
| BMI (kg/m2) | -0.0388 | 0.0262 | ±0.0523 | -1.485 | 0.1375 |  |
| Hypertension | -0.2481 | 0.4980 | ±0.9960 | -0.498 | 0.6183 |  |
| High cholesterol | +0.9333 | 0.5073 | ±1.0145 | +1.840 | 0.0658 | . |
| Kidney disease | +1.0544 | 0.5820 | ±1.1640 | +1.812 | 0.0700 | . |
| Circulatory disease | +0.6855 | 0.4940 | ±0.9881 | +1.388 | 0.1652 |  |
| **Time > 180 (%)** | **-0.0287** | 0.0132 | ±0.0264 | **-2.176** | **0.0296** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **230**, R² = **0.2044**, Adj R² = **0.1643**, F-statistic = **5.09** (p = **4.38e-07**), Residual SE = **3.221** on **218** df, AIC = **1202.4**, BIC = **1243.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.7219** | 1.9753 | ±3.9505 | **+16.059** | **4.91e-58** | *** |
| Education: graduate level (vs college) | +0.6847 | 0.4634 | ±0.9269 | +1.478 | 0.1395 |  |
| **Education: high school or below (vs college)** | **-2.7050** | 0.9691 | ±1.9383 | **-2.791** | **0.0053** | ** |
| Site: UCSD (vs UAB) | -0.4629 | 0.5186 | ±1.0371 | -0.893 | 0.3721 |  |
| Site: UW (vs UAB) | -0.8025 | 0.6681 | ±1.3362 | -1.201 | 0.2297 |  |
| **Age (years)** | **-0.0826** | 0.0266 | ±0.0532 | **-3.105** | **0.0019** | ** |
| BMI (kg/m2) | -0.0393 | 0.0262 | ±0.0524 | -1.499 | 0.1339 |  |
| Hypertension | -0.2531 | 0.4976 | ±0.9953 | -0.509 | 0.6110 |  |
| High cholesterol | +0.9381 | 0.5073 | ±1.0145 | +1.849 | 0.0644 | . |
| Kidney disease | +1.0612 | 0.5812 | ±1.1624 | +1.826 | 0.0679 | . |
| Circulatory disease | +0.6878 | 0.4941 | ±0.9882 | +1.392 | 0.1639 |  |
| **Avg. daily time > 180 (%)** | **-0.0287** | 0.0134 | ±0.0267 | **-2.148** | **0.0317** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **230**, R² = **0.2066**, Adj R² = **0.1666**, F-statistic = **5.16** (p = **3.40e-07**), Residual SE = **3.216** on **218** df, AIC = **1201.8**, BIC = **1243.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.6615** | 1.9662 | ±3.9323 | **+16.103** | **2.42e-58** | *** |
| Education: graduate level (vs college) | +0.6970 | 0.4659 | ±0.9319 | +1.496 | 0.1347 |  |
| **Education: high school or below (vs college)** | **-2.7611** | 0.9653 | ±1.9305 | **-2.860** | **0.0042** | ** |
| Site: UCSD (vs UAB) | -0.4790 | 0.5153 | ±1.0306 | -0.929 | 0.3526 |  |
| Site: UW (vs UAB) | -0.8000 | 0.6724 | ±1.3448 | -1.190 | 0.2341 |  |
| **Age (years)** | **-0.0847** | 0.0262 | ±0.0524 | **-3.235** | **0.0012** | ** |
| BMI (kg/m2) | -0.0376 | 0.0261 | ±0.0522 | -1.438 | 0.1503 |  |
| Hypertension | -0.2016 | 0.4916 | ±0.9832 | -0.410 | 0.6817 |  |
| High cholesterol | +0.9680 | 0.5042 | ±1.0085 | +1.920 | 0.0549 | . |
| Kidney disease | +0.9233 | 0.5835 | ±1.1670 | +1.582 | 0.1136 |  |
| Circulatory disease | +0.7195 | 0.4929 | ±0.9857 | +1.460 | 0.1443 |  |
| **Nocturnal time > 180 (%)** | **-0.0302** | 0.0130 | ±0.0259 | **-2.326** | **0.0200** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **230**, R² = **0.1889**, Adj R² = **0.1480**, F-statistic = **4.62** (p = **2.56e-06**), Residual SE = **3.252** on **218** df, AIC = **1206.9**, BIC = **1248.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.5162** | 1.9669 | ±3.9338 | **+16.023** | **8.78e-58** | *** |
| Education: graduate level (vs college) | +0.7088 | 0.4615 | ±0.9230 | +1.536 | 0.1246 |  |
| **Education: high school or below (vs college)** | **-2.7890** | 0.9659 | ±1.9318 | **-2.887** | **0.0039** | ** |
| Site: UCSD (vs UAB) | -0.4441 | 0.5353 | ±1.0705 | -0.830 | 0.4067 |  |
| Site: UW (vs UAB) | -0.6740 | 0.6769 | ±1.3538 | -0.996 | 0.3194 |  |
| **Age (years)** | **-0.0802** | 0.0278 | ±0.0556 | **-2.884** | **0.0039** | ** |
| BMI (kg/m2) | -0.0410 | 0.0264 | ±0.0527 | -1.554 | 0.1203 |  |
| Hypertension | -0.2396 | 0.5075 | ±1.0149 | -0.472 | 0.6368 |  |
| High cholesterol | +0.9105 | 0.5130 | ±1.0259 | +1.775 | 0.0759 | . |
| Kidney disease | +0.9866 | 0.5876 | ±1.1752 | +1.679 | 0.0932 | . |
| Circulatory disease | +0.6435 | 0.5099 | ±1.0199 | +1.262 | 0.2070 |  |
| Any reading > 250 during wear (0/1) | -0.5581 | 0.4708 | ±0.9416 | -1.185 | 0.2359 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **230**, R² = **0.2070**, Adj R² = **0.1670**, F-statistic = **5.17** (p = **3.24e-07**), Residual SE = **3.216** on **218** df, AIC = **1201.7**, BIC = **1242.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.7386** | 1.9881 | ±3.9761 | **+15.965** | **2.26e-57** | *** |
| Education: graduate level (vs college) | +0.6963 | 0.4669 | ±0.9339 | +1.491 | 0.1359 |  |
| **Education: high school or below (vs college)** | **-2.6824** | 0.9753 | ±1.9505 | **-2.750** | **0.0060** | ** |
| Site: UCSD (vs UAB) | -0.4828 | 0.5184 | ±1.0368 | -0.931 | 0.3517 |  |
| Site: UW (vs UAB) | -0.8460 | 0.6682 | ±1.3364 | -1.266 | 0.2055 |  |
| **Age (years)** | **-0.0854** | 0.0264 | ±0.0528 | **-3.236** | **0.0012** | ** |
| BMI (kg/m2) | -0.0396 | 0.0266 | ±0.0531 | -1.490 | 0.1363 |  |
| Hypertension | -0.2129 | 0.5066 | ±1.0131 | -0.420 | 0.6743 |  |
| High cholesterol | +0.8560 | 0.5101 | ±1.0203 | +1.678 | 0.0934 | . |
| Kidney disease | +0.9563 | 0.5889 | ±1.1779 | +1.624 | 0.1044 |  |
| Circulatory disease | +0.6963 | 0.4902 | ±0.9805 | +1.420 | 0.1555 |  |
| **Time > 250 (%)** | **-0.0615** | 0.0287 | ±0.0573 | **-2.146** | **0.0319** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 230)
**Regression Call / Formula**: `moca_total ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **230**, R² = **0.2112**, Adj R² = **0.1714**, F-statistic = **5.31** (p = **1.98e-07**), Residual SE = **3.207** on **218** df, AIC = **1200.4**, BIC = **1241.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+31.7599** | 1.9882 | ±3.9764 | **+15.974** | **1.93e-57** | *** |
| Education: graduate level (vs college) | +0.6848 | 0.4669 | ±0.9338 | +1.467 | 0.1424 |  |
| **Education: high school or below (vs college)** | **-2.6326** | 0.9718 | ±1.9437 | **-2.709** | **0.0068** | ** |
| Site: UCSD (vs UAB) | -0.4740 | 0.5133 | ±1.0266 | -0.923 | 0.3558 |  |
| Site: UW (vs UAB) | -0.8474 | 0.6688 | ±1.3375 | -1.267 | 0.2051 |  |
| **Age (years)** | **-0.0850** | 0.0264 | ±0.0528 | **-3.219** | **0.0013** | ** |
| BMI (kg/m2) | -0.0409 | 0.0266 | ±0.0531 | -1.538 | 0.1240 |  |
| Hypertension | -0.2049 | 0.5049 | ±1.0097 | -0.406 | 0.6848 |  |
| High cholesterol | +0.8576 | 0.5086 | ±1.0173 | +1.686 | 0.0918 | . |
| Kidney disease | +0.9896 | 0.5863 | ±1.1727 | +1.688 | 0.0915 | . |
| Circulatory disease | +0.7226 | 0.4894 | ±0.9789 | +1.476 | 0.1398 |  |
| **Avg. daily time > 250 (%)** | **-0.0743** | 0.0314 | ±0.0627 | **-2.371** | **0.0177** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### Cognitive impairment (MoCA < 26)  (domain: Cognition; outcome sample N = 230; logistic regression)

#### Reference: covariates only
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0696**, LLR χ² = **22.08** (p = **0.0147**), AUC = **0.6786**, AIC = **317.0**, BIC = **354.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.9586** | 1.2099 | ±2.4197 | **-2.445** | **0.0145** | 0.0519 | * |
| **Education: graduate level (vs college)** | **-0.7360** | 0.3369 | ±0.6738 | **-2.184** | **0.0289** | 0.4790 | * |
| Education: high school or below (vs college) | +0.7260 | 0.4192 | ±0.8384 | +1.732 | 0.0833 | 2.0669 | . |
| Site: UCSD (vs UAB) | +0.1584 | 0.3476 | ±0.6953 | +0.456 | 0.6486 | 1.1717 |  |
| Site: UW (vs UAB) | -0.0851 | 0.3650 | ±0.7299 | -0.233 | 0.8157 | 0.9184 |  |
| **Age (years)** | **+0.0413** | 0.0146 | ±0.0291 | **+2.837** | **0.0046** | 1.0422 | ** |
| BMI (kg/m2) | +0.0231 | 0.0189 | ±0.0377 | +1.226 | 0.2202 | 1.0234 |  |
| Hypertension | -0.0572 | 0.3360 | ±0.6720 | -0.170 | 0.8648 | 0.9444 |  |
| High cholesterol | -0.2951 | 0.2937 | ±0.5874 | -1.005 | 0.3151 | 0.7445 |  |
| Kidney disease | -0.4255 | 0.4133 | ±0.8266 | -1.030 | 0.3032 | 0.6534 |  |
| Circulatory disease | -0.3711 | 0.3346 | ±0.6692 | -1.109 | 0.2674 | 0.6900 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0934**, LLR χ² = **29.63** (p = **0.0018**), AUC = **0.7051**, AIC = **311.5**, BIC = **352.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-5.0801** | 1.4998 | ±2.9996 | **-3.387** | **7.06e-04** | 0.0062 | *** |
| Education: graduate level (vs college) | -0.6435 | 0.3436 | ±0.6872 | -1.873 | 0.0611 | 0.5255 | . |
| Education: high school or below (vs college) | +0.6189 | 0.4297 | ±0.8594 | +1.440 | 0.1497 | 1.8570 |  |
| Site: UCSD (vs UAB) | +0.1735 | 0.3520 | ±0.7041 | +0.493 | 0.6221 | 1.1895 |  |
| Site: UW (vs UAB) | -0.0349 | 0.3705 | ±0.7410 | -0.094 | 0.9250 | 0.9657 |  |
| **Age (years)** | **+0.0371** | 0.0150 | ±0.0300 | **+2.478** | **0.0132** | 1.0378 | * |
| BMI (kg/m2) | +0.0223 | 0.0192 | ±0.0384 | +1.158 | 0.2467 | 1.0225 |  |
| Hypertension | -0.0971 | 0.3408 | ±0.6817 | -0.285 | 0.7757 | 0.9075 |  |
| High cholesterol | -0.2737 | 0.3001 | ±0.6002 | -0.912 | 0.3618 | 0.7606 |  |
| Kidney disease | -0.4741 | 0.4251 | ±0.8503 | -1.115 | 0.2647 | 0.6224 |  |
| Circulatory disease | -0.3867 | 0.3445 | ±0.6889 | -1.123 | 0.2616 | 0.6793 |  |
| **HbA1c (%)** | **+0.3740** | 0.1445 | ±0.2890 | **+2.588** | **0.0097** | 1.4535 | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0823**, LLR χ² = **26.11** (p = **0.0062**), AUC = **0.6945**, AIC = **315.0**, BIC = **356.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.2115** | 1.3815 | ±2.7629 | **-3.049** | **0.0023** | 0.0148 | ** |
| **Education: graduate level (vs college)** | **-0.7218** | 0.3393 | ±0.6785 | **-2.128** | **0.0334** | 0.4859 | * |
| Education: high school or below (vs college) | +0.6650 | 0.4236 | ±0.8472 | +1.570 | 0.1164 | 1.9445 |  |
| Site: UCSD (vs UAB) | +0.1642 | 0.3513 | ±0.7027 | +0.467 | 0.6402 | 1.1785 |  |
| Site: UW (vs UAB) | -0.0507 | 0.3670 | ±0.7340 | -0.138 | 0.8901 | 0.9505 |  |
| **Age (years)** | **+0.0416** | 0.0147 | ±0.0293 | **+2.835** | **0.0046** | 1.0424 | ** |
| BMI (kg/m2) | +0.0236 | 0.0190 | ±0.0381 | +1.238 | 0.2156 | 1.0239 |  |
| Hypertension | -0.0732 | 0.3387 | ±0.6775 | -0.216 | 0.8289 | 0.9294 |  |
| High cholesterol | -0.2896 | 0.2972 | ±0.5944 | -0.974 | 0.3299 | 0.7486 |  |
| Kidney disease | -0.5055 | 0.4195 | ±0.8389 | -1.205 | 0.2281 | 0.6032 |  |
| Circulatory disease | -0.4052 | 0.3413 | ±0.6825 | -1.187 | 0.2351 | 0.6669 |  |
| Mean glucose (mg/dL) | +0.0092 | 0.0047 | ±0.0094 | +1.950 | 0.0512 | 1.0092 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0823**, LLR χ² = **26.11** (p = **0.0062**), AUC = **0.6945**, AIC = **315.0**, BIC = **356.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-5.4791** | 1.7829 | ±3.5658 | **-3.073** | **0.0021** | 0.0042 | ** |
| **Education: graduate level (vs college)** | **-0.7218** | 0.3393 | ±0.6785 | **-2.128** | **0.0334** | 0.4859 | * |
| Education: high school or below (vs college) | +0.6650 | 0.4236 | ±0.8472 | +1.570 | 0.1164 | 1.9445 |  |
| Site: UCSD (vs UAB) | +0.1642 | 0.3513 | ±0.7027 | +0.467 | 0.6402 | 1.1785 |  |
| Site: UW (vs UAB) | -0.0507 | 0.3670 | ±0.7340 | -0.138 | 0.8901 | 0.9505 |  |
| **Age (years)** | **+0.0416** | 0.0147 | ±0.0293 | **+2.835** | **0.0046** | 1.0424 | ** |
| BMI (kg/m2) | +0.0236 | 0.0190 | ±0.0381 | +1.238 | 0.2156 | 1.0239 |  |
| Hypertension | -0.0732 | 0.3387 | ±0.6775 | -0.216 | 0.8289 | 0.9294 |  |
| High cholesterol | -0.2896 | 0.2972 | ±0.5944 | -0.974 | 0.3299 | 0.7486 |  |
| Kidney disease | -0.5055 | 0.4195 | ±0.8389 | -1.205 | 0.2281 | 0.6032 |  |
| Circulatory disease | -0.4052 | 0.3413 | ±0.6825 | -1.187 | 0.2351 | 0.6669 |  |
| GMI (%) | +0.3830 | 0.1964 | ±0.3928 | +1.950 | 0.0512 | 1.4666 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0815**, LLR χ² = **25.84** (p = **0.0069**), AUC = **0.6894**, AIC = **315.3**, BIC = **356.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-4.1441** | 1.3752 | ±2.7505 | **-3.013** | **0.0026** | 0.0159 | ** |
| **Education: graduate level (vs college)** | **-0.7531** | 0.3396 | ±0.6792 | **-2.218** | **0.0266** | 0.4709 | * |
| Education: high school or below (vs college) | +0.6677 | 0.4229 | ±0.8458 | +1.579 | 0.1143 | 1.9497 |  |
| Site: UCSD (vs UAB) | +0.1662 | 0.3510 | ±0.7019 | +0.474 | 0.6359 | 1.1808 |  |
| Site: UW (vs UAB) | -0.0607 | 0.3667 | ±0.7335 | -0.166 | 0.8685 | 0.9411 |  |
| **Age (years)** | **+0.0430** | 0.0147 | ±0.0294 | **+2.930** | **0.0034** | 1.0439 | ** |
| BMI (kg/m2) | +0.0232 | 0.0190 | ±0.0381 | +1.217 | 0.2235 | 1.0234 |  |
| Hypertension | -0.0904 | 0.3382 | ±0.6763 | -0.267 | 0.7893 | 0.9136 |  |
| High cholesterol | -0.3121 | 0.2970 | ±0.5941 | -1.051 | 0.2934 | 0.7319 |  |
| Kidney disease | -0.4432 | 0.4177 | ±0.8354 | -1.061 | 0.2887 | 0.6420 |  |
| Circulatory disease | -0.4048 | 0.3414 | ±0.6829 | -1.186 | 0.2358 | 0.6671 |  |
| Nocturnal mean 00-06h (mg/dL) | +0.0086 | 0.0046 | ±0.0092 | +1.882 | 0.0598 | 1.0087 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0833**, LLR χ² = **26.40** (p = **0.0057**), AUC = **0.6934**, AIC = **314.7**, BIC = **356.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4832** | 1.2526 | ±2.5052 | **-2.781** | **0.0054** | 0.0307 | ** |
| **Education: graduate level (vs college)** | **-0.6722** | 0.3409 | ±0.6818 | **-1.972** | **0.0486** | 0.5106 | * |
| Education: high school or below (vs college) | +0.5777 | 0.4278 | ±0.8555 | +1.351 | 0.1769 | 1.7819 |  |
| Site: UCSD (vs UAB) | +0.1770 | 0.3523 | ±0.7046 | +0.502 | 0.6153 | 1.1937 |  |
| Site: UW (vs UAB) | -0.0266 | 0.3678 | ±0.7355 | -0.072 | 0.9422 | 0.9737 |  |
| **Age (years)** | **+0.0374** | 0.0148 | ±0.0296 | **+2.532** | **0.0113** | 1.0381 | * |
| BMI (kg/m2) | +0.0255 | 0.0191 | ±0.0382 | +1.337 | 0.1813 | 1.0258 |  |
| Hypertension | -0.0714 | 0.3387 | ±0.6775 | -0.211 | 0.8330 | 0.9311 |  |
| High cholesterol | -0.2746 | 0.2974 | ±0.5948 | -0.923 | 0.3558 | 0.7599 |  |
| Kidney disease | -0.6315 | 0.4314 | ±0.8629 | -1.464 | 0.1433 | 0.5318 |  |
| Circulatory disease | -0.3704 | 0.3389 | ±0.6778 | -1.093 | 0.2745 | 0.6905 |  |
| **Glucose SD, pooled (mg/dL)** | **+0.0205** | 0.0102 | ±0.0204 | **+2.011** | **0.0444** | 1.0207 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0791**, LLR χ² = **25.09** (p = **0.0088**), AUC = **0.6907**, AIC = **316.0**, BIC = **357.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.4122** | 1.2483 | ±2.4965 | **-2.734** | **0.0063** | 0.0330 | ** |
| **Education: graduate level (vs college)** | **-0.6780** | 0.3404 | ±0.6807 | **-1.992** | **0.0464** | 0.5076 | * |
| Education: high school or below (vs college) | +0.5840 | 0.4285 | ±0.8570 | +1.363 | 0.1729 | 1.7932 |  |
| Site: UCSD (vs UAB) | +0.1744 | 0.3508 | ±0.7017 | +0.497 | 0.6190 | 1.1906 |  |
| Site: UW (vs UAB) | -0.0453 | 0.3670 | ±0.7341 | -0.123 | 0.9017 | 0.9557 |  |
| **Age (years)** | **+0.0378** | 0.0147 | ±0.0295 | **+2.564** | **0.0104** | 1.0385 | * |
| BMI (kg/m2) | +0.0254 | 0.0190 | ±0.0381 | +1.335 | 0.1820 | 1.0257 |  |
| Hypertension | -0.0592 | 0.3382 | ±0.6763 | -0.175 | 0.8610 | 0.9425 |  |
| High cholesterol | -0.2796 | 0.2962 | ±0.5924 | -0.944 | 0.3451 | 0.7560 |  |
| Kidney disease | -0.6016 | 0.4307 | ±0.8613 | -1.397 | 0.1625 | 0.5480 |  |
| Circulatory disease | -0.3578 | 0.3374 | ±0.6748 | -1.060 | 0.2889 | 0.6992 |  |
| Avg. daily SD (mg/dL) | +0.0200 | 0.0119 | ±0.0237 | +1.686 | 0.0919 | 1.0202 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0783**, LLR χ² = **24.83** (p = **0.0097**), AUC = **0.6876**, AIC = **316.3**, BIC = **357.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.5948** | 1.2878 | ±2.5756 | **-2.791** | **0.0052** | 0.0275 | ** |
| Education: graduate level (vs college) | -0.6669 | 0.3414 | ±0.6828 | -1.953 | 0.0508 | 0.5133 | . |
| Education: high school or below (vs college) | +0.5848 | 0.4285 | ±0.8569 | +1.365 | 0.1723 | 1.7947 |  |
| Site: UCSD (vs UAB) | +0.1753 | 0.3508 | ±0.7016 | +0.500 | 0.6173 | 1.1916 |  |
| Site: UW (vs UAB) | -0.0383 | 0.3674 | ±0.7349 | -0.104 | 0.9169 | 0.9624 |  |
| **Age (years)** | **+0.0355** | 0.0150 | ±0.0300 | **+2.370** | **0.0178** | 1.0362 | * |
| BMI (kg/m2) | +0.0256 | 0.0191 | ±0.0381 | +1.343 | 0.1792 | 1.0259 |  |
| Hypertension | -0.0618 | 0.3377 | ±0.6754 | -0.183 | 0.8549 | 0.9401 |  |
| High cholesterol | -0.2772 | 0.2960 | ±0.5920 | -0.936 | 0.3491 | 0.7579 |  |
| Kidney disease | -0.6262 | 0.4357 | ±0.8715 | -1.437 | 0.1507 | 0.5346 |  |
| Circulatory disease | -0.3576 | 0.3359 | ±0.6717 | -1.065 | 0.2870 | 0.6994 |  |
| CV (%) | +0.0374 | 0.0229 | ±0.0458 | +1.635 | 0.1021 | 1.0381 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0754**, LLR χ² = **23.91** (p = **0.0131**), AUC = **0.6885**, AIC = **317.2**, BIC = **358.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.9747 | 1.4076 | ±2.8152 | -1.403 | 0.1606 | 0.1388 |  |
| **Education: graduate level (vs college)** | **-0.6766** | 0.3412 | ±0.6824 | **-1.983** | **0.0474** | 0.5083 | * |
| Education: high school or below (vs college) | +0.6091 | 0.4280 | ±0.8560 | +1.423 | 0.1547 | 1.8387 |  |
| Site: UCSD (vs UAB) | +0.1566 | 0.3492 | ±0.6984 | +0.449 | 0.6537 | 1.1696 |  |
| Site: UW (vs UAB) | -0.0607 | 0.3667 | ±0.7333 | -0.166 | 0.8685 | 0.9411 |  |
| **Age (years)** | **+0.0359** | 0.0151 | ±0.0301 | **+2.387** | **0.0170** | 1.0366 | * |
| BMI (kg/m2) | +0.0242 | 0.0189 | ±0.0378 | +1.283 | 0.1996 | 1.0245 |  |
| Hypertension | -0.0497 | 0.3369 | ±0.6738 | -0.148 | 0.8827 | 0.9515 |  |
| High cholesterol | -0.2763 | 0.2955 | ±0.5911 | -0.935 | 0.3498 | 0.7586 |  |
| Kidney disease | -0.5420 | 0.4256 | ±0.8513 | -1.273 | 0.2029 | 0.5816 |  |
| Circulatory disease | -0.3769 | 0.3352 | ±0.6704 | -1.124 | 0.2608 | 0.6860 |  |
| Mean / SD ratio | -0.1565 | 0.1177 | ±0.2354 | -1.330 | 0.1836 | 0.8551 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0708**, LLR χ² = **22.44** (p = **0.0212**), AUC = **0.6805**, AIC = **318.7**, BIC = **359.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -2.5350 | 1.4012 | ±2.8024 | -1.809 | 0.0704 | 0.0793 | . |
| **Education: graduate level (vs college)** | **-0.7066** | 0.3408 | ±0.6817 | **-2.073** | **0.0382** | 0.4933 | * |
| Education: high school or below (vs college) | +0.6732 | 0.4281 | ±0.8563 | +1.572 | 0.1159 | 1.9605 |  |
| Site: UCSD (vs UAB) | +0.1532 | 0.3480 | ±0.6961 | +0.440 | 0.6598 | 1.1656 |  |
| Site: UW (vs UAB) | -0.0796 | 0.3655 | ±0.7310 | -0.218 | 0.8275 | 0.9235 |  |
| **Age (years)** | **+0.0388** | 0.0151 | ±0.0302 | **+2.567** | **0.0103** | 1.0396 | * |
| BMI (kg/m2) | +0.0237 | 0.0189 | ±0.0378 | +1.253 | 0.2103 | 1.0239 |  |
| Hypertension | -0.0468 | 0.3367 | ±0.6734 | -0.139 | 0.8895 | 0.9543 |  |
| High cholesterol | -0.2902 | 0.2942 | ±0.5883 | -0.987 | 0.3238 | 0.7481 |  |
| Kidney disease | -0.4634 | 0.4192 | ±0.8383 | -1.106 | 0.2689 | 0.6291 |  |
| Circulatory disease | -0.3674 | 0.3345 | ±0.6691 | -1.098 | 0.2720 | 0.6925 |  |
| Avg. daily mean/SD | -0.0558 | 0.0946 | ±0.1892 | -0.590 | 0.5552 | 0.9457 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0701**, LLR χ² = **22.22** (p = **0.0227**), AUC = **0.6782**, AIC = **318.9**, BIC = **360.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1480** | 1.3141 | ±2.6282 | **-2.396** | **0.0166** | 0.0429 | * |
| **Education: graduate level (vs college)** | **-0.7275** | 0.3379 | ±0.6758 | **-2.153** | **0.0313** | 0.4831 | * |
| Education: high school or below (vs college) | +0.6951 | 0.4267 | ±0.8534 | +1.629 | 0.1033 | 2.0040 |  |
| Site: UCSD (vs UAB) | +0.1521 | 0.3484 | ±0.6967 | +0.437 | 0.6625 | 1.1642 |  |
| Site: UW (vs UAB) | -0.0733 | 0.3662 | ±0.7324 | -0.200 | 0.8414 | 0.9293 |  |
| **Age (years)** | **+0.0410** | 0.0146 | ±0.0292 | **+2.813** | **0.0049** | 1.0419 | ** |
| BMI (kg/m2) | +0.0226 | 0.0189 | ±0.0379 | +1.196 | 0.2317 | 1.0229 |  |
| Hypertension | -0.0524 | 0.3365 | ±0.6729 | -0.156 | 0.8762 | 0.9489 |  |
| High cholesterol | -0.2970 | 0.2940 | ±0.5880 | -1.010 | 0.3124 | 0.7431 |  |
| Kidney disease | -0.4263 | 0.4135 | ±0.8270 | -1.031 | 0.3025 | 0.6529 |  |
| Circulatory disease | -0.3691 | 0.3347 | ±0.6693 | -1.103 | 0.2701 | 0.6914 |  |
| MAG (mg/dL/h) | +0.0049 | 0.0132 | ±0.0264 | +0.373 | 0.7089 | 1.0049 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0738**, LLR χ² = **23.41** (p = **0.0155**), AUC = **0.6849**, AIC = **317.7**, BIC = **359.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3839** | 1.2721 | ±2.5441 | **-2.660** | **0.0078** | 0.0339 | ** |
| **Education: graduate level (vs college)** | **-0.6948** | 0.3397 | ±0.6794 | **-2.045** | **0.0408** | 0.4992 | * |
| Education: high school or below (vs college) | +0.6222 | 0.4286 | ±0.8573 | +1.452 | 0.1466 | 1.8629 |  |
| Site: UCSD (vs UAB) | +0.1680 | 0.3493 | ±0.6986 | +0.481 | 0.6305 | 1.1830 |  |
| Site: UW (vs UAB) | -0.0659 | 0.3659 | ±0.7317 | -0.180 | 0.8571 | 0.9363 |  |
| **Age (years)** | **+0.0392** | 0.0147 | ±0.0294 | **+2.666** | **0.0077** | 1.0399 | ** |
| BMI (kg/m2) | +0.0248 | 0.0190 | ±0.0380 | +1.308 | 0.1908 | 1.0251 |  |
| Hypertension | -0.0497 | 0.3372 | ±0.6744 | -0.148 | 0.8827 | 0.9515 |  |
| High cholesterol | -0.2889 | 0.2949 | ±0.5898 | -0.980 | 0.3273 | 0.7491 |  |
| Kidney disease | -0.5355 | 0.4264 | ±0.8528 | -1.256 | 0.2091 | 0.5854 |  |
| Circulatory disease | -0.3739 | 0.3358 | ±0.6716 | -1.114 | 0.2655 | 0.6880 |  |
| Avg. daily range (mg/dL) | +0.0037 | 0.0032 | ±0.0065 | +1.139 | 0.2547 | 1.0037 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0853**, LLR χ² = **27.05** (p = **0.0045**), AUC = **0.6953**, AIC = **314.1**, BIC = **355.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.3278** | 1.2395 | ±2.4791 | **-2.685** | **0.0073** | 0.0359 | ** |
| **Education: graduate level (vs college)** | **-0.6723** | 0.3410 | ±0.6820 | **-1.972** | **0.0486** | 0.5105 | * |
| Education: high school or below (vs college) | +0.6834 | 0.4238 | ±0.8477 | +1.612 | 0.1069 | 1.9805 |  |
| Site: UCSD (vs UAB) | +0.1680 | 0.3534 | ±0.7067 | +0.475 | 0.6345 | 1.1829 |  |
| Site: UW (vs UAB) | -0.0113 | 0.3686 | ±0.7372 | -0.031 | 0.9755 | 0.9888 |  |
| **Age (years)** | **+0.0398** | 0.0147 | ±0.0295 | **+2.702** | **0.0069** | 1.0406 | ** |
| BMI (kg/m2) | +0.0250 | 0.0191 | ±0.0382 | +1.309 | 0.1905 | 1.0253 |  |
| Hypertension | -0.1227 | 0.3394 | ±0.6788 | -0.362 | 0.7177 | 0.8845 |  |
| High cholesterol | -0.2914 | 0.2981 | ±0.5962 | -0.978 | 0.3283 | 0.7472 |  |
| Kidney disease | -0.5718 | 0.4252 | ±0.8504 | -1.345 | 0.1787 | 0.5645 |  |
| Circulatory disease | -0.4361 | 0.3429 | ±0.6859 | -1.272 | 0.2034 | 0.6465 |  |
| **SD of daily means (mg/dL)** | **+0.0363** | 0.0173 | ±0.0346 | **+2.104** | **0.0354** | 1.0370 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0872**, LLR χ² = **27.66** (p = **0.0037**), AUC = **0.7010**, AIC = **313.4**, BIC = **354.7**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3033 | 1.4112 | ±2.8225 | -0.924 | 0.3557 | 0.2716 |  |
| **Education: graduate level (vs college)** | **-0.6692** | 0.3413 | ±0.6825 | **-1.961** | **0.0499** | 0.5121 | * |
| Education: high school or below (vs college) | +0.6471 | 0.4259 | ±0.8517 | +1.520 | 0.1286 | 1.9101 |  |
| Site: UCSD (vs UAB) | +0.1821 | 0.3536 | ±0.7071 | +0.515 | 0.6066 | 1.1997 |  |
| Site: UW (vs UAB) | -0.0231 | 0.3681 | ±0.7362 | -0.063 | 0.9499 | 0.9771 |  |
| **Age (years)** | **+0.0398** | 0.0147 | ±0.0294 | **+2.708** | **0.0068** | 1.0406 | ** |
| BMI (kg/m2) | +0.0248 | 0.0191 | ±0.0382 | +1.299 | 0.1939 | 1.0251 |  |
| Hypertension | -0.0510 | 0.3394 | ±0.6788 | -0.150 | 0.8805 | 0.9503 |  |
| High cholesterol | -0.3186 | 0.2987 | ±0.5974 | -1.067 | 0.2861 | 0.7271 |  |
| Kidney disease | -0.5786 | 0.4242 | ±0.8485 | -1.364 | 0.1727 | 0.5607 |  |
| Circulatory disease | -0.4264 | 0.3430 | ±0.6860 | -1.243 | 0.2138 | 0.6528 |  |
| **Time in range 70-180, pooled (%)** | **-0.0192** | 0.0084 | ±0.0168 | **-2.283** | **0.0224** | 0.9810 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0870**, LLR χ² = **27.58** (p = **0.0038**), AUC = **0.7018**, AIC = **313.5**, BIC = **354.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | -1.3277 | 1.4072 | ±2.8145 | -0.943 | 0.3455 | 0.2651 |  |
| **Education: graduate level (vs college)** | **-0.6711** | 0.3413 | ±0.6827 | **-1.966** | **0.0493** | 0.5111 | * |
| Education: high school or below (vs college) | +0.6401 | 0.4260 | ±0.8519 | +1.503 | 0.1329 | 1.8966 |  |
| Site: UCSD (vs UAB) | +0.1854 | 0.3535 | ±0.7069 | +0.525 | 0.5999 | 1.2037 |  |
| Site: UW (vs UAB) | -0.0193 | 0.3684 | ±0.7367 | -0.052 | 0.9583 | 0.9809 |  |
| **Age (years)** | **+0.0398** | 0.0147 | ±0.0294 | **+2.710** | **0.0067** | 1.0406 | ** |
| BMI (kg/m2) | +0.0250 | 0.0191 | ±0.0382 | +1.309 | 0.1904 | 1.0253 |  |
| Hypertension | -0.0473 | 0.3394 | ±0.6788 | -0.139 | 0.8891 | 0.9538 |  |
| High cholesterol | -0.3191 | 0.2986 | ±0.5972 | -1.069 | 0.2852 | 0.7268 |  |
| Kidney disease | -0.5829 | 0.4251 | ±0.8503 | -1.371 | 0.1703 | 0.5583 |  |
| Circulatory disease | -0.4256 | 0.3429 | ±0.6859 | -1.241 | 0.2146 | 0.6534 |  |
| **Avg. daily time in range 70-180 (%)** | **-0.0189** | 0.0083 | ±0.0166 | **-2.275** | **0.0229** | 0.9813 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0702**, LLR χ² = **22.28** (p = **0.0223**), AUC = **0.6792**, AIC = **318.8**, BIC = **360.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.9864** | 1.2120 | ±2.4240 | **-2.464** | **0.0137** | 0.0505 | * |
| **Education: graduate level (vs college)** | **-0.7286** | 0.3374 | ±0.6748 | **-2.160** | **0.0308** | 0.4826 | * |
| Education: high school or below (vs college) | +0.7387 | 0.4206 | ±0.8413 | +1.756 | 0.0791 | 2.0931 | . |
| Site: UCSD (vs UAB) | +0.1780 | 0.3506 | ±0.7012 | +0.508 | 0.6116 | 1.1949 |  |
| Site: UW (vs UAB) | -0.0609 | 0.3691 | ±0.7383 | -0.165 | 0.8689 | 0.9409 |  |
| **Age (years)** | **+0.0411** | 0.0146 | ±0.0291 | **+2.825** | **0.0047** | 1.0420 | ** |
| BMI (kg/m2) | +0.0230 | 0.0189 | ±0.0377 | +1.221 | 0.2221 | 1.0233 |  |
| Hypertension | -0.0609 | 0.3360 | ±0.6719 | -0.181 | 0.8561 | 0.9409 |  |
| High cholesterol | -0.2977 | 0.2939 | ±0.5877 | -1.013 | 0.3111 | 0.7425 |  |
| Kidney disease | -0.4214 | 0.4133 | ±0.8266 | -1.020 | 0.3079 | 0.6561 |  |
| Circulatory disease | -0.3863 | 0.3367 | ±0.6735 | -1.147 | 0.2513 | 0.6796 |  |
| Time < 54 (%) | +0.0826 | 0.1906 | ±0.3813 | +0.433 | 0.6649 | 1.0861 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0708**, LLR χ² = **22.44** (p = **0.0212**), AUC = **0.6802**, AIC = **318.7**, BIC = **359.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.9684** | 1.2106 | ±2.4212 | **-2.452** | **0.0142** | 0.0514 | * |
| **Education: graduate level (vs college)** | **-0.7228** | 0.3378 | ±0.6756 | **-2.140** | **0.0324** | 0.4854 | * |
| Education: high school or below (vs college) | +0.7410 | 0.4203 | ±0.8406 | +1.763 | 0.0779 | 2.0980 | . |
| Site: UCSD (vs UAB) | +0.1798 | 0.3495 | ±0.6991 | +0.514 | 0.6069 | 1.1970 |  |
| Site: UW (vs UAB) | -0.0603 | 0.3673 | ±0.7347 | -0.164 | 0.8696 | 0.9415 |  |
| **Age (years)** | **+0.0407** | 0.0146 | ±0.0292 | **+2.793** | **0.0052** | 1.0416 | ** |
| BMI (kg/m2) | +0.0231 | 0.0189 | ±0.0378 | +1.223 | 0.2212 | 1.0234 |  |
| Hypertension | -0.0584 | 0.3360 | ±0.6719 | -0.174 | 0.8619 | 0.9432 |  |
| High cholesterol | -0.2912 | 0.2940 | ±0.5881 | -0.990 | 0.3219 | 0.7473 |  |
| Kidney disease | -0.4272 | 0.4133 | ±0.8267 | -1.034 | 0.3013 | 0.6523 |  |
| Circulatory disease | -0.3894 | 0.3366 | ±0.6732 | -1.157 | 0.2473 | 0.6774 |  |
| Avg. daily time < 54 (%) | +0.1021 | 0.1745 | ±0.3491 | +0.585 | 0.5584 | 1.1075 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0725**, LLR χ² = **23.00** (p = **0.0176**), AUC = **0.6830**, AIC = **318.1**, BIC = **359.4**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.9662** | 1.2111 | ±2.4221 | **-2.449** | **0.0143** | 0.0515 | * |
| **Education: graduate level (vs college)** | **-0.6913** | 0.3407 | ±0.6815 | **-2.029** | **0.0425** | 0.5009 | * |
| Education: high school or below (vs college) | +0.7181 | 0.4208 | ±0.8415 | +1.707 | 0.0879 | 2.0505 | . |
| Site: UCSD (vs UAB) | +0.1802 | 0.3491 | ±0.6981 | +0.516 | 0.6057 | 1.1975 |  |
| Site: UW (vs UAB) | -0.0681 | 0.3662 | ±0.7324 | -0.186 | 0.8524 | 0.9341 |  |
| **Age (years)** | **+0.0395** | 0.0147 | ±0.0293 | **+2.695** | **0.0070** | 1.0403 | ** |
| BMI (kg/m2) | +0.0234 | 0.0189 | ±0.0378 | +1.237 | 0.2160 | 1.0236 |  |
| Hypertension | -0.0453 | 0.3369 | ±0.6738 | -0.134 | 0.8931 | 0.9557 |  |
| High cholesterol | -0.3118 | 0.2948 | ±0.5897 | -1.057 | 0.2903 | 0.7322 |  |
| Kidney disease | -0.4403 | 0.4137 | ±0.8273 | -1.064 | 0.2872 | 0.6438 |  |
| Circulatory disease | -0.3777 | 0.3353 | ±0.6707 | -1.126 | 0.2600 | 0.6854 |  |
| Time 54-69, pooled (%) | +0.0551 | 0.0581 | ±0.1162 | +0.948 | 0.3433 | 1.0566 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0732**, LLR χ² = **23.22** (p = **0.0165**), AUC = **0.6835**, AIC = **317.9**, BIC = **359.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.9431** | 1.2112 | ±2.4224 | **-2.430** | **0.0151** | 0.0527 | * |
| **Education: graduate level (vs college)** | **-0.6868** | 0.3409 | ±0.6818 | **-2.015** | **0.0439** | 0.5032 | * |
| Education: high school or below (vs college) | +0.7125 | 0.4210 | ±0.8419 | +1.693 | 0.0905 | 2.0390 | . |
| Site: UCSD (vs UAB) | +0.1810 | 0.3490 | ±0.6980 | +0.519 | 0.6040 | 1.1984 |  |
| Site: UW (vs UAB) | -0.0648 | 0.3666 | ±0.7332 | -0.177 | 0.8598 | 0.9373 |  |
| **Age (years)** | **+0.0391** | 0.0147 | ±0.0294 | **+2.660** | **0.0078** | 1.0399 | ** |
| BMI (kg/m2) | +0.0233 | 0.0189 | ±0.0378 | +1.234 | 0.2172 | 1.0236 |  |
| Hypertension | -0.0444 | 0.3370 | ±0.6740 | -0.132 | 0.8953 | 0.9566 |  |
| High cholesterol | -0.3107 | 0.2948 | ±0.5897 | -1.054 | 0.2919 | 0.7329 |  |
| Kidney disease | -0.4402 | 0.4138 | ±0.8276 | -1.064 | 0.2874 | 0.6439 |  |
| Circulatory disease | -0.3754 | 0.3356 | ±0.6712 | -1.119 | 0.2633 | 0.6870 |  |
| Avg. daily time 54-69 (%) | +0.0586 | 0.0560 | ±0.1119 | +1.047 | 0.2953 | 1.0603 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0722**, LLR χ² = **22.90** (p = **0.0183**), AUC = **0.6823**, AIC = **318.2**, BIC = **359.5**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.9778** | 1.2111 | ±2.4222 | **-2.459** | **0.0139** | 0.0509 | * |
| **Education: graduate level (vs college)** | **-0.6976** | 0.3401 | ±0.6801 | **-2.051** | **0.0402** | 0.4978 | * |
| Education: high school or below (vs college) | +0.7260 | 0.4206 | ±0.8412 | +1.726 | 0.0843 | 2.0668 | . |
| Site: UCSD (vs UAB) | +0.1852 | 0.3494 | ±0.6989 | +0.530 | 0.5962 | 1.2034 |  |
| Site: UW (vs UAB) | -0.0597 | 0.3666 | ±0.7333 | -0.163 | 0.8707 | 0.9421 |  |
| **Age (years)** | **+0.0398** | 0.0146 | ±0.0293 | **+2.720** | **0.0065** | 1.0406 | ** |
| BMI (kg/m2) | +0.0232 | 0.0189 | ±0.0378 | +1.231 | 0.2182 | 1.0235 |  |
| Hypertension | -0.0496 | 0.3366 | ±0.6731 | -0.147 | 0.8829 | 0.9516 |  |
| High cholesterol | -0.3092 | 0.2946 | ±0.5893 | -1.049 | 0.2940 | 0.7341 |  |
| Kidney disease | -0.4347 | 0.4133 | ±0.8266 | -1.052 | 0.2930 | 0.6475 |  |
| Circulatory disease | -0.3838 | 0.3357 | ±0.6713 | -1.143 | 0.2529 | 0.6813 |  |
| Time < 70 (%) | +0.0427 | 0.0482 | ±0.0963 | +0.887 | 0.3750 | 1.0436 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0729**, LLR χ² = **23.13** (p = **0.0170**), AUC = **0.6843**, AIC = **318.0**, BIC = **359.2**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-2.9496** | 1.2111 | ±2.4222 | **-2.435** | **0.0149** | 0.0524 | * |
| **Education: graduate level (vs college)** | **-0.6919** | 0.3404 | ±0.6807 | **-2.033** | **0.0421** | 0.5006 | * |
| Education: high school or below (vs college) | +0.7215 | 0.4206 | ±0.8413 | +1.715 | 0.0863 | 2.0576 | . |
| Site: UCSD (vs UAB) | +0.1852 | 0.3492 | ±0.6984 | +0.530 | 0.5958 | 1.2035 |  |
| Site: UW (vs UAB) | -0.0585 | 0.3667 | ±0.7335 | -0.160 | 0.8732 | 0.9432 |  |
| **Age (years)** | **+0.0393** | 0.0147 | ±0.0294 | **+2.677** | **0.0074** | 1.0401 | ** |
| BMI (kg/m2) | +0.0232 | 0.0189 | ±0.0378 | +1.231 | 0.2185 | 1.0235 |  |
| Hypertension | -0.0473 | 0.3367 | ±0.6735 | -0.141 | 0.8882 | 0.9538 |  |
| High cholesterol | -0.3054 | 0.2946 | ±0.5891 | -1.037 | 0.2998 | 0.7368 |  |
| Kidney disease | -0.4376 | 0.4136 | ±0.8272 | -1.058 | 0.2900 | 0.6456 |  |
| Circulatory disease | -0.3824 | 0.3359 | ±0.6717 | -1.139 | 0.2548 | 0.6822 |  |
| Avg. daily time < 70 (%) | +0.0457 | 0.0456 | ±0.0913 | +1.002 | 0.3164 | 1.0468 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0838**, LLR χ² = **26.59** (p = **0.0053**), AUC = **0.6929**, AIC = **314.5**, BIC = **355.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +0.6688 | 2.3676 | ±4.7352 | +0.282 | 0.7776 | 1.9518 |  |
| **Education: graduate level (vs college)** | **-0.6896** | 0.3386 | ±0.6772 | **-2.036** | **0.0417** | 0.5018 | * |
| Education: high school or below (vs college) | +0.6331 | 0.4273 | ±0.8546 | +1.482 | 0.1384 | 1.8834 |  |
| Site: UCSD (vs UAB) | +0.1888 | 0.3523 | ±0.7046 | +0.536 | 0.5921 | 1.2078 |  |
| Site: UW (vs UAB) | -0.0041 | 0.3673 | ±0.7347 | -0.011 | 0.9912 | 0.9960 |  |
| **Age (years)** | **+0.0415** | 0.0146 | ±0.0293 | **+2.839** | **0.0045** | 1.0424 | ** |
| BMI (kg/m2) | +0.0245 | 0.0190 | ±0.0380 | +1.292 | 0.1965 | 1.0248 |  |
| Hypertension | -0.0742 | 0.3385 | ±0.6769 | -0.219 | 0.8264 | 0.9285 |  |
| High cholesterol | -0.2678 | 0.2978 | ±0.5957 | -0.899 | 0.3685 | 0.7650 |  |
| Kidney disease | -0.4975 | 0.4183 | ±0.8367 | -1.189 | 0.2343 | 0.6080 |  |
| Circulatory disease | -0.4143 | 0.3415 | ±0.6830 | -1.213 | 0.2251 | 0.6608 |  |
| Time 54-250, pooled (%) | -0.0383 | 0.0211 | ±0.0422 | -1.814 | 0.0697 | 0.9624 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0838**, LLR χ² = **26.58** (p = **0.0053**), AUC = **0.6929**, AIC = **314.5**, BIC = **355.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Intercept | +1.0689 | 2.5342 | ±5.0684 | +0.422 | 0.6732 | 2.9122 |  |
| **Education: graduate level (vs college)** | **-0.6847** | 0.3388 | ±0.6777 | **-2.021** | **0.0433** | 0.5042 | * |
| Education: high school or below (vs college) | +0.6188 | 0.4283 | ±0.8566 | +1.445 | 0.1485 | 1.8567 |  |
| Site: UCSD (vs UAB) | +0.1864 | 0.3526 | ±0.7052 | +0.529 | 0.5971 | 1.2049 |  |
| Site: UW (vs UAB) | -0.0099 | 0.3672 | ±0.7343 | -0.027 | 0.9785 | 0.9902 |  |
| **Age (years)** | **+0.0411** | 0.0146 | ±0.0292 | **+2.814** | **0.0049** | 1.0420 | ** |
| BMI (kg/m2) | +0.0249 | 0.0190 | ±0.0380 | +1.311 | 0.1899 | 1.0252 |  |
| Hypertension | -0.0739 | 0.3384 | ±0.6768 | -0.218 | 0.8272 | 0.9288 |  |
| High cholesterol | -0.2694 | 0.2978 | ±0.5956 | -0.905 | 0.3656 | 0.7638 |  |
| Kidney disease | -0.5135 | 0.4203 | ±0.8405 | -1.222 | 0.2218 | 0.5984 |  |
| Circulatory disease | -0.4201 | 0.3420 | ±0.6841 | -1.228 | 0.2194 | 0.6570 |  |
| Avg. daily time 54-250 (%) | -0.0421 | 0.0230 | ±0.0459 | -1.835 | 0.0666 | 0.9588 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0791**, LLR χ² = **25.09** (p = **0.0088**), AUC = **0.6940**, AIC = **316.0**, BIC = **357.3**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1036** | 1.2196 | ±2.4392 | **-2.545** | **0.0109** | 0.0449 | * |
| **Education: graduate level (vs college)** | **-0.7050** | 0.3397 | ±0.6794 | **-2.075** | **0.0379** | 0.4941 | * |
| Education: high school or below (vs college) | +0.6944 | 0.4220 | ±0.8440 | +1.646 | 0.0999 | 2.0026 | . |
| Site: UCSD (vs UAB) | +0.1558 | 0.3508 | ±0.7016 | +0.444 | 0.6569 | 1.1686 |  |
| Site: UW (vs UAB) | -0.0724 | 0.3666 | ±0.7333 | -0.197 | 0.8435 | 0.9302 |  |
| **Age (years)** | **+0.0401** | 0.0147 | ±0.0293 | **+2.734** | **0.0063** | 1.0409 | ** |
| BMI (kg/m2) | +0.0238 | 0.0190 | ±0.0380 | +1.253 | 0.2102 | 1.0241 |  |
| Hypertension | -0.0462 | 0.3378 | ±0.6755 | -0.137 | 0.8912 | 0.9549 |  |
| High cholesterol | -0.3314 | 0.2970 | ±0.5940 | -1.116 | 0.2644 | 0.7179 |  |
| Kidney disease | -0.5446 | 0.4230 | ±0.8461 | -1.287 | 0.1980 | 0.5801 |  |
| Circulatory disease | -0.3966 | 0.3390 | ±0.6779 | -1.170 | 0.2420 | 0.6726 |  |
| Time 181-250, pooled (%) | +0.0203 | 0.0118 | ±0.0235 | +1.724 | 0.0847 | 1.0205 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0797**, LLR χ² = **25.26** (p = **0.0084**), AUC = **0.6944**, AIC = **315.8**, BIC = **357.1**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1375** | 1.2216 | ±2.4432 | **-2.568** | **0.0102** | 0.0434 | * |
| **Education: graduate level (vs college)** | **-0.7071** | 0.3398 | ±0.6796 | **-2.081** | **0.0374** | 0.4931 | * |
| Education: high school or below (vs college) | +0.6911 | 0.4220 | ±0.8441 | +1.638 | 0.1015 | 1.9959 |  |
| Site: UCSD (vs UAB) | +0.1641 | 0.3508 | ±0.7017 | +0.468 | 0.6400 | 1.1783 |  |
| Site: UW (vs UAB) | -0.0605 | 0.3671 | ±0.7341 | -0.165 | 0.8691 | 0.9413 |  |
| **Age (years)** | **+0.0405** | 0.0147 | ±0.0293 | **+2.761** | **0.0058** | 1.0413 | ** |
| BMI (kg/m2) | +0.0239 | 0.0190 | ±0.0380 | +1.257 | 0.2087 | 1.0242 |  |
| Hypertension | -0.0429 | 0.3380 | ±0.6760 | -0.127 | 0.8989 | 0.9580 |  |
| High cholesterol | -0.3303 | 0.2970 | ±0.5941 | -1.112 | 0.2661 | 0.7187 |  |
| Kidney disease | -0.5469 | 0.4232 | ±0.8464 | -1.292 | 0.1963 | 0.5787 |  |
| Circulatory disease | -0.3947 | 0.3389 | ±0.6779 | -1.164 | 0.2443 | 0.6739 |  |
| Avg. daily time 181-250 (%) | +0.0202 | 0.0114 | ±0.0227 | +1.773 | 0.0762 | 1.0204 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0843**, LLR χ² = **26.74** (p = **0.0050**), AUC = **0.6981**, AIC = **314.4**, BIC = **355.6**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1837** | 1.2240 | ±2.4481 | **-2.601** | **0.0093** | 0.0414 | ** |
| **Education: graduate level (vs college)** | **-0.6905** | 0.3402 | ±0.6805 | **-2.029** | **0.0424** | 0.5013 | * |
| Education: high school or below (vs college) | +0.6576 | 0.4247 | ±0.8494 | +1.548 | 0.1215 | 1.9302 |  |
| Site: UCSD (vs UAB) | +0.1695 | 0.3525 | ±0.7050 | +0.481 | 0.6307 | 1.1847 |  |
| Site: UW (vs UAB) | -0.0390 | 0.3675 | ±0.7349 | -0.106 | 0.9155 | 0.9618 |  |
| **Age (years)** | **+0.0406** | 0.0147 | ±0.0294 | **+2.764** | **0.0057** | 1.0414 | ** |
| BMI (kg/m2) | +0.0245 | 0.0190 | ±0.0381 | +1.285 | 0.1988 | 1.0248 |  |
| Hypertension | -0.0553 | 0.3387 | ±0.6775 | -0.163 | 0.8703 | 0.9462 |  |
| High cholesterol | -0.3088 | 0.2978 | ±0.5955 | -1.037 | 0.2996 | 0.7343 |  |
| Kidney disease | -0.5579 | 0.4231 | ±0.8462 | -1.318 | 0.1874 | 0.5724 |  |
| Circulatory disease | -0.4145 | 0.3419 | ±0.6837 | -1.212 | 0.2253 | 0.6607 |  |
| **Time > 180 (%)** | **+0.0170** | 0.0081 | ±0.0162 | **+2.102** | **0.0356** | 1.0172 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0839**, LLR χ² = **26.61** (p = **0.0053**), AUC = **0.6964**, AIC = **314.5**, BIC = **355.8**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1946** | 1.2244 | ±2.4487 | **-2.609** | **0.0091** | 0.0410 | ** |
| **Education: graduate level (vs college)** | **-0.6932** | 0.3402 | ±0.6805 | **-2.037** | **0.0416** | 0.5000 | * |
| Education: high school or below (vs college) | +0.6534 | 0.4248 | ±0.8495 | +1.538 | 0.1240 | 1.9221 |  |
| Site: UCSD (vs UAB) | +0.1731 | 0.3524 | ±0.7047 | +0.491 | 0.6233 | 1.1890 |  |
| Site: UW (vs UAB) | -0.0353 | 0.3677 | ±0.7353 | -0.096 | 0.9235 | 0.9653 |  |
| **Age (years)** | **+0.0407** | 0.0147 | ±0.0293 | **+2.776** | **0.0055** | 1.0416 | ** |
| BMI (kg/m2) | +0.0247 | 0.0190 | ±0.0381 | +1.295 | 0.1952 | 1.0250 |  |
| Hypertension | -0.0527 | 0.3387 | ±0.6774 | -0.156 | 0.8764 | 0.9487 |  |
| High cholesterol | -0.3109 | 0.2976 | ±0.5952 | -1.045 | 0.2962 | 0.7328 |  |
| Kidney disease | -0.5609 | 0.4238 | ±0.8476 | -1.323 | 0.1857 | 0.5707 |  |
| Circulatory disease | -0.4148 | 0.3417 | ±0.6835 | -1.214 | 0.2249 | 0.6605 |  |
| **Avg. daily time > 180 (%)** | **+0.0168** | 0.0081 | ±0.0162 | **+2.077** | **0.0378** | 1.0170 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0833**, LLR χ² = **26.40** (p = **0.0057**), AUC = **0.6962**, AIC = **314.7**, BIC = **356.0**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1425** | 1.2220 | ±2.4439 | **-2.572** | **0.0101** | 0.0432 | * |
| **Education: graduate level (vs college)** | **-0.7041** | 0.3399 | ±0.6797 | **-2.072** | **0.0383** | 0.4946 | * |
| Education: high school or below (vs college) | +0.6809 | 0.4231 | ±0.8461 | +1.609 | 0.1075 | 1.9756 |  |
| Site: UCSD (vs UAB) | +0.1860 | 0.3525 | ±0.7051 | +0.528 | 0.5978 | 1.2044 |  |
| Site: UW (vs UAB) | -0.0394 | 0.3672 | ±0.7345 | -0.107 | 0.9145 | 0.9613 |  |
| **Age (years)** | **+0.0418** | 0.0146 | ±0.0293 | **+2.855** | **0.0043** | 1.0427 | ** |
| BMI (kg/m2) | +0.0238 | 0.0191 | ±0.0381 | +1.250 | 0.2113 | 1.0241 |  |
| Hypertension | -0.0812 | 0.3377 | ±0.6753 | -0.240 | 0.8101 | 0.9220 |  |
| High cholesterol | -0.3249 | 0.2976 | ±0.5951 | -1.092 | 0.2749 | 0.7226 |  |
| Kidney disease | -0.4788 | 0.4188 | ±0.8376 | -1.143 | 0.2529 | 0.6195 |  |
| Circulatory disease | -0.4278 | 0.3426 | ±0.6851 | -1.249 | 0.2118 | 0.6520 |  |
| **Nocturnal time > 180 (%)** | **+0.0165** | 0.0082 | ±0.0164 | **+2.006** | **0.0449** | 1.0166 | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0739**, LLR χ² = **23.42** (p = **0.0154**), AUC = **0.6846**, AIC = **317.7**, BIC = **358.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.0793** | 1.2179 | ±2.4357 | **-2.528** | **0.0115** | 0.0460 | * |
| **Education: graduate level (vs college)** | **-0.7000** | 0.3392 | ±0.6784 | **-2.064** | **0.0391** | 0.4966 | * |
| Education: high school or below (vs college) | +0.6905 | 0.4210 | ±0.8420 | +1.640 | 0.1010 | 1.9947 |  |
| Site: UCSD (vs UAB) | +0.1577 | 0.3490 | ±0.6981 | +0.452 | 0.6513 | 1.1708 |  |
| Site: UW (vs UAB) | -0.1132 | 0.3668 | ±0.7336 | -0.309 | 0.7576 | 0.8930 |  |
| **Age (years)** | **+0.0392** | 0.0147 | ±0.0294 | **+2.666** | **0.0077** | 1.0400 | ** |
| BMI (kg/m2) | +0.0258 | 0.0191 | ±0.0381 | +1.354 | 0.1757 | 1.0261 |  |
| Hypertension | -0.0675 | 0.3375 | ±0.6749 | -0.200 | 0.8414 | 0.9347 |  |
| High cholesterol | -0.2876 | 0.2951 | ±0.5903 | -0.974 | 0.3299 | 0.7501 |  |
| Kidney disease | -0.5110 | 0.4210 | ±0.8419 | -1.214 | 0.2248 | 0.5999 |  |
| Circulatory disease | -0.3790 | 0.3358 | ±0.6717 | -1.128 | 0.2591 | 0.6846 |  |
| Any reading > 250 during wear (0/1) | +0.3375 | 0.2924 | ±0.5848 | +1.154 | 0.2484 | 1.4014 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0834**, LLR χ² = **26.46** (p = **0.0055**), AUC = **0.6938**, AIC = **314.6**, BIC = **355.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1450** | 1.2196 | ±2.4391 | **-2.579** | **0.0099** | 0.0431 | ** |
| **Education: graduate level (vs college)** | **-0.6933** | 0.3385 | ±0.6770 | **-2.048** | **0.0405** | 0.4999 | * |
| Education: high school or below (vs college) | +0.6291 | 0.4273 | ±0.8545 | +1.472 | 0.1409 | 1.8759 |  |
| Site: UCSD (vs UAB) | +0.1801 | 0.3521 | ±0.7042 | +0.511 | 0.6091 | 1.1973 |  |
| Site: UW (vs UAB) | -0.0156 | 0.3669 | ±0.7338 | -0.043 | 0.9660 | 0.9845 |  |
| **Age (years)** | **+0.0416** | 0.0146 | ±0.0293 | **+2.845** | **0.0044** | 1.0425 | ** |
| BMI (kg/m2) | +0.0245 | 0.0190 | ±0.0380 | +1.290 | 0.1970 | 1.0248 |  |
| Hypertension | -0.0725 | 0.3385 | ±0.6770 | -0.214 | 0.8305 | 0.9301 |  |
| High cholesterol | -0.2663 | 0.2978 | ±0.5956 | -0.894 | 0.3712 | 0.7662 |  |
| Kidney disease | -0.4979 | 0.4184 | ±0.8367 | -1.190 | 0.2340 | 0.6078 |  |
| Circulatory disease | -0.4060 | 0.3412 | ±0.6825 | -1.190 | 0.2342 | 0.6663 |  |
| Time > 250 (%) | +0.0377 | 0.0210 | ±0.0420 | +1.798 | 0.0722 | 1.0385 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 230)
**Regression Call / Formula**: `cognitive_impairment ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **230**, events = **105**, McFadden pseudo-R² = **0.0833**, LLR χ² = **26.42** (p = **0.0056**), AUC = **0.6930**, AIC = **314.7**, BIC = **355.9**

| Term / Variable | Coef Estimate (log-odds β) | Std. Error (SE) | 2 * SE (95% CI Margin) | z value | Pr(>\|z\|) | Odds Ratio | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **-3.1372** | 1.2189 | ±2.4377 | **-2.574** | **0.0101** | 0.0434 | * |
| **Education: graduate level (vs college)** | **-0.6903** | 0.3386 | ±0.6773 | **-2.038** | **0.0415** | 0.5014 | * |
| Education: high school or below (vs college) | +0.6141 | 0.4285 | ±0.8569 | +1.433 | 0.1518 | 1.8479 |  |
| Site: UCSD (vs UAB) | +0.1781 | 0.3524 | ±0.7049 | +0.505 | 0.6134 | 1.1949 |  |
| Site: UW (vs UAB) | -0.0200 | 0.3668 | ±0.7336 | -0.055 | 0.9564 | 0.9802 |  |
| **Age (years)** | **+0.0414** | 0.0146 | ±0.0292 | **+2.830** | **0.0047** | 1.0422 | ** |
| BMI (kg/m2) | +0.0249 | 0.0190 | ±0.0380 | +1.309 | 0.1907 | 1.0252 |  |
| Hypertension | -0.0733 | 0.3384 | ±0.6768 | -0.217 | 0.8284 | 0.9293 |  |
| High cholesterol | -0.2702 | 0.2976 | ±0.5953 | -0.908 | 0.3639 | 0.7632 |  |
| Kidney disease | -0.5120 | 0.4202 | ±0.8404 | -1.218 | 0.2231 | 0.5993 |  |
| Circulatory disease | -0.4111 | 0.3418 | ±0.6835 | -1.203 | 0.2290 | 0.6629 |  |
| Avg. daily time > 250 (%) | +0.0419 | 0.0232 | ±0.0464 | +1.803 | 0.0714 | 1.0427 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


---

### MoCA memory index score (0-15)  (domain: Cognition; outcome sample N = 230; OLS, HC3 SEs)

#### Reference: covariates only
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems`  
**Model Diagnostics**: N = **230**, R² = **0.1168**, Adj R² = **0.0765**, F-statistic = **2.90** (p = **0.0020**), Residual SE = **2.708** on **219** df, AIC = **1121.7**, BIC = **1159.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.8779** | 1.8680 | ±3.7359 | **+9.035** | **1.63e-19** | *** |
| Education: graduate level (vs college) | +0.3281 | 0.4171 | ±0.8343 | +0.787 | 0.4315 |  |
| **Education: high school or below (vs college)** | **-1.3549** | 0.5761 | ±1.1523 | **-2.352** | **0.0187** | * |
| Site: UCSD (vs UAB) | +0.2197 | 0.4871 | ±0.9743 | +0.451 | 0.6519 |  |
| Site: UW (vs UAB) | -0.0942 | 0.4956 | ±0.9912 | -0.190 | 0.8492 |  |
| **Age (years)** | **-0.0663** | 0.0227 | ±0.0454 | **-2.923** | **0.0035** | ** |
| BMI (kg/m2) | -0.0265 | 0.0295 | ±0.0590 | -0.899 | 0.3689 |  |
| Hypertension | -0.3155 | 0.4107 | ±0.8215 | -0.768 | 0.4423 |  |
| High cholesterol | +0.5923 | 0.4265 | ±0.8530 | +1.389 | 0.1649 |  |
| **Kidney disease** | **+0.9007** | 0.4326 | ±0.8653 | **+2.082** | **0.0374** | * |
| Circulatory disease | +0.5833 | 0.4148 | ±0.8296 | +1.406 | 0.1597 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: HbA1c (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + hba1c`  
**Model Diagnostics**: N = **230**, R² = **0.1368**, Adj R² = **0.0932**, F-statistic = **3.14** (p = **5.84e-04**), Residual SE = **2.683** on **218** df, AIC = **1118.4**, BIC = **1159.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.8650** | 2.0248 | ±4.0497 | **+9.317** | **1.20e-20** | *** |
| Education: graduate level (vs college) | +0.2180 | 0.4165 | ±0.8329 | +0.524 | 0.6006 |  |
| **Education: high school or below (vs college)** | **-1.2430** | 0.5951 | ±1.1902 | **-2.089** | **0.0367** | * |
| Site: UCSD (vs UAB) | +0.2001 | 0.4784 | ±0.9567 | +0.418 | 0.6757 |  |
| Site: UW (vs UAB) | -0.1435 | 0.5026 | ±1.0052 | -0.285 | 0.7753 |  |
| **Age (years)** | **-0.0606** | 0.0231 | ±0.0463 | **-2.621** | **0.0088** | ** |
| BMI (kg/m2) | -0.0248 | 0.0287 | ±0.0574 | -0.864 | 0.3878 |  |
| Hypertension | -0.2709 | 0.4068 | ±0.8137 | -0.666 | 0.5056 |  |
| High cholesterol | +0.5548 | 0.4267 | ±0.8535 | +1.300 | 0.1936 |  |
| **Kidney disease** | **+0.9330** | 0.4253 | ±0.8506 | **+2.194** | **0.0282** | * |
| Circulatory disease | +0.5860 | 0.4012 | ±0.8024 | +1.461 | 0.1441 |  |
| **HbA1c (%)** | **-0.3684** | 0.1588 | ±0.3176 | **-2.320** | **0.0203** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean glucose (mg/dL)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_glucose`  
**Model Diagnostics**: N = **230**, R² = **0.1287**, Adj R² = **0.0847**, F-statistic = **2.93** (p = **0.0013**), Residual SE = **2.696** on **218** df, AIC = **1120.6**, BIC = **1161.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.2018** | 1.9740 | ±3.9481 | **+9.221** | **2.95e-20** | *** |
| Education: graduate level (vs college) | +0.3053 | 0.4167 | ±0.8335 | +0.733 | 0.4638 |  |
| **Education: high school or below (vs college)** | **-1.2777** | 0.5894 | ±1.1788 | **-2.168** | **0.0302** | * |
| Site: UCSD (vs UAB) | +0.2183 | 0.4765 | ±0.9530 | +0.458 | 0.6469 |  |
| Site: UW (vs UAB) | -0.1289 | 0.5018 | ±1.0036 | -0.257 | 0.7973 |  |
| **Age (years)** | **-0.0662** | 0.0230 | ±0.0460 | **-2.881** | **0.0040** | ** |
| BMI (kg/m2) | -0.0267 | 0.0292 | ±0.0584 | -0.914 | 0.3606 |  |
| Hypertension | -0.2933 | 0.4108 | ±0.8216 | -0.714 | 0.4752 |  |
| High cholesterol | +0.5793 | 0.4285 | ±0.8570 | +1.352 | 0.1764 |  |
| **Kidney disease** | **+0.9815** | 0.4343 | ±0.8685 | **+2.260** | **0.0238** | * |
| Circulatory disease | +0.6092 | 0.3985 | ±0.7971 | +1.529 | 0.1264 |  |
| Mean glucose (mg/dL) | -0.0099 | 0.0066 | ±0.0131 | -1.506 | 0.1322 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: GMI (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + gmi`  
**Model Diagnostics**: N = **230**, R² = **0.1287**, Adj R² = **0.0847**, F-statistic = **2.93** (p = **0.0013**), Residual SE = **2.696** on **218** df, AIC = **1120.6**, BIC = **1161.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+19.5701** | 2.4258 | ±4.8517 | **+8.067** | **7.18e-16** | *** |
| Education: graduate level (vs college) | +0.3053 | 0.4167 | ±0.8335 | +0.733 | 0.4638 |  |
| **Education: high school or below (vs college)** | **-1.2777** | 0.5894 | ±1.1788 | **-2.168** | **0.0302** | * |
| Site: UCSD (vs UAB) | +0.2183 | 0.4765 | ±0.9530 | +0.458 | 0.6469 |  |
| Site: UW (vs UAB) | -0.1289 | 0.5018 | ±1.0036 | -0.257 | 0.7973 |  |
| **Age (years)** | **-0.0662** | 0.0230 | ±0.0460 | **-2.881** | **0.0040** | ** |
| BMI (kg/m2) | -0.0267 | 0.0292 | ±0.0584 | -0.914 | 0.3606 |  |
| Hypertension | -0.2933 | 0.4108 | ±0.8216 | -0.714 | 0.4752 |  |
| High cholesterol | +0.5793 | 0.4285 | ±0.8570 | +1.352 | 0.1764 |  |
| **Kidney disease** | **+0.9815** | 0.4343 | ±0.8685 | **+2.260** | **0.0238** | * |
| Circulatory disease | +0.6092 | 0.3985 | ±0.7971 | +1.529 | 0.1264 |  |
| GMI (%) | -0.4134 | 0.2746 | ±0.5491 | -1.506 | 0.1322 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal mean 00-06h (mg/dL)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_mean`  
**Model Diagnostics**: N = **230**, R² = **0.1302**, Adj R² = **0.0863**, F-statistic = **2.97** (p = **0.0011**), Residual SE = **2.694** on **218** df, AIC = **1120.2**, BIC = **1161.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.2521** | 1.9491 | ±3.8983 | **+9.364** | **7.66e-21** | *** |
| Education: graduate level (vs college) | +0.3370 | 0.4193 | ±0.8387 | +0.804 | 0.4216 |  |
| **Education: high school or below (vs college)** | **-1.2782** | 0.5885 | ±1.1769 | **-2.172** | **0.0298** | * |
| Site: UCSD (vs UAB) | +0.2188 | 0.4770 | ±0.9540 | +0.459 | 0.6464 |  |
| Site: UW (vs UAB) | -0.1206 | 0.5023 | ±1.0046 | -0.240 | 0.8103 |  |
| **Age (years)** | **-0.0679** | 0.0228 | ±0.0457 | **-2.975** | **0.0029** | ** |
| BMI (kg/m2) | -0.0260 | 0.0293 | ±0.0585 | -0.889 | 0.3742 |  |
| Hypertension | -0.2742 | 0.4083 | ±0.8167 | -0.671 | 0.5020 |  |
| High cholesterol | +0.6064 | 0.4278 | ±0.8555 | +1.417 | 0.1563 |  |
| **Kidney disease** | **+0.9107** | 0.4326 | ±0.8651 | **+2.105** | **0.0353** | * |
| Circulatory disease | +0.6117 | 0.3989 | ±0.7979 | +1.533 | 0.1252 |  |
| Nocturnal mean 00-06h (mg/dL) | -0.0103 | 0.0067 | ±0.0134 | -1.540 | 0.1237 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Glucose SD, pooled (mg/dL)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_sd`  
**Model Diagnostics**: N = **230**, R² = **0.1465**, Adj R² = **0.1034**, F-statistic = **3.40** (p = **2.28e-04**), Residual SE = **2.668** on **218** df, AIC = **1115.9**, BIC = **1157.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.6761** | 1.8764 | ±3.7529 | **+9.420** | **4.51e-21** | *** |
| Education: graduate level (vs college) | +0.2096 | 0.4135 | ±0.8269 | +0.507 | 0.6122 |  |
| Education: high school or below (vs college) | -1.1099 | 0.5847 | ±1.1693 | -1.898 | 0.0577 | . |
| Site: UCSD (vs UAB) | +0.1891 | 0.4703 | ±0.9407 | +0.402 | 0.6877 |  |
| Site: UW (vs UAB) | -0.1804 | 0.5045 | ±1.0089 | -0.358 | 0.7206 |  |
| **Age (years)** | **-0.0592** | 0.0236 | ±0.0472 | **-2.508** | **0.0121** | * |
| BMI (kg/m2) | -0.0299 | 0.0287 | ±0.0574 | -1.043 | 0.2969 |  |
| Hypertension | -0.2903 | 0.4097 | ±0.8194 | -0.708 | 0.4786 |  |
| High cholesterol | +0.5486 | 0.4303 | ±0.8606 | +1.275 | 0.2024 |  |
| **Kidney disease** | **+1.2247** | 0.4402 | ±0.8805 | **+2.782** | **0.0054** | ** |
| Circulatory disease | +0.5741 | 0.3958 | ±0.7916 | +1.451 | 0.1469 |  |
| **Glucose SD, pooled (mg/dL)** | **-0.0332** | 0.0127 | ±0.0254 | **-2.613** | **0.0090** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily SD (mg/dL)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_sd`  
**Model Diagnostics**: N = **230**, R² = **0.1394**, Adj R² = **0.0960**, F-statistic = **3.21** (p = **4.54e-04**), Residual SE = **2.679** on **218** df, AIC = **1117.7**, BIC = **1159.0**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.6330** | 1.8983 | ±3.7966 | **+9.289** | **1.56e-20** | *** |
| Education: graduate level (vs college) | +0.2199 | 0.4134 | ±0.8268 | +0.532 | 0.5948 |  |
| Education: high school or below (vs college) | -1.1051 | 0.5816 | ±1.1631 | -1.900 | 0.0574 | . |
| Site: UCSD (vs UAB) | +0.1944 | 0.4751 | ±0.9503 | +0.409 | 0.6824 |  |
| Site: UW (vs UAB) | -0.1568 | 0.5035 | ±1.0070 | -0.311 | 0.7555 |  |
| **Age (years)** | **-0.0600** | 0.0235 | ±0.0470 | **-2.550** | **0.0108** | * |
| BMI (kg/m2) | -0.0303 | 0.0291 | ±0.0582 | -1.040 | 0.2982 |  |
| Hypertension | -0.3112 | 0.4128 | ±0.8256 | -0.754 | 0.4509 |  |
| High cholesterol | +0.5628 | 0.4309 | ±0.8617 | +1.306 | 0.1915 |  |
| **Kidney disease** | **+1.1933** | 0.4344 | ±0.8688 | **+2.747** | **0.0060** | ** |
| Circulatory disease | +0.5611 | 0.4022 | ±0.8043 | +1.395 | 0.1629 |  |
| **Avg. daily SD (mg/dL)** | **-0.0342** | 0.0141 | ±0.0282 | **-2.430** | **0.0151** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: CV (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + glucose_cv`  
**Model Diagnostics**: N = **230**, R² = **0.1466**, Adj R² = **0.1036**, F-statistic = **3.41** (p = **2.24e-04**), Residual SE = **2.668** on **218** df, AIC = **1115.8**, BIC = **1157.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+18.1306** | 1.9267 | ±3.8533 | **+9.410** | **4.94e-21** | *** |
| Education: graduate level (vs college) | +0.1730 | 0.4123 | ±0.8246 | +0.420 | 0.6748 |  |
| Education: high school or below (vs college) | -1.0650 | 0.5710 | ±1.1419 | -1.865 | 0.0621 | . |
| Site: UCSD (vs UAB) | +0.1844 | 0.4779 | ±0.9559 | +0.386 | 0.6997 |  |
| Site: UW (vs UAB) | -0.1783 | 0.5020 | ±1.0039 | -0.355 | 0.7225 |  |
| **Age (years)** | **-0.0535** | 0.0236 | ±0.0472 | **-2.269** | **0.0233** | * |
| BMI (kg/m2) | -0.0313 | 0.0289 | ±0.0578 | -1.084 | 0.2785 |  |
| Hypertension | -0.3105 | 0.4108 | ±0.8217 | -0.756 | 0.4497 |  |
| High cholesterol | +0.5535 | 0.4293 | ±0.8585 | +1.289 | 0.1973 |  |
| **Kidney disease** | **+1.3053** | 0.4351 | ±0.8701 | **+3.000** | **0.0027** | ** |
| Circulatory disease | +0.5597 | 0.4061 | ±0.8122 | +1.378 | 0.1682 |  |
| **CV (%)** | **-0.0771** | 0.0258 | ±0.0516 | **-2.991** | **0.0028** | ** |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Mean / SD ratio  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mean_to_sd_ratio`  
**Model Diagnostics**: N = **230**, R² = **0.1330**, Adj R² = **0.0893**, F-statistic = **3.04** (p = **8.37e-04**), Residual SE = **2.689** on **218** df, AIC = **1119.4**, BIC = **1160.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.0357** | 1.9664 | ±3.9328 | **+7.646** | **2.07e-14** | *** |
| Education: graduate level (vs college) | +0.2140 | 0.4104 | ±0.8208 | +0.521 | 0.6021 |  |
| **Education: high school or below (vs college)** | **-1.1369** | 0.5779 | ±1.1558 | **-1.967** | **0.0492** | * |
| Site: UCSD (vs UAB) | +0.2268 | 0.4811 | ±0.9622 | +0.471 | 0.6373 |  |
| Site: UW (vs UAB) | -0.1333 | 0.5006 | ±1.0012 | -0.266 | 0.7901 |  |
| **Age (years)** | **-0.0561** | 0.0232 | ±0.0464 | **-2.422** | **0.0155** | * |
| BMI (kg/m2) | -0.0285 | 0.0293 | ±0.0586 | -0.974 | 0.3301 |  |
| Hypertension | -0.3323 | 0.4144 | ±0.8287 | -0.802 | 0.4226 |  |
| High cholesterol | +0.5616 | 0.4317 | ±0.8634 | +1.301 | 0.1933 |  |
| **Kidney disease** | **+1.1124** | 0.4281 | ±0.8561 | **+2.599** | **0.0094** | ** |
| Circulatory disease | +0.6066 | 0.4091 | ±0.8183 | +1.483 | 0.1382 |  |
| **Mean / SD ratio** | **+0.2884** | 0.1384 | ±0.2768 | **+2.084** | **0.0372** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily mean / SD  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_mean_to_sd`  
**Model Diagnostics**: N = **230**, R² = **0.1232**, Adj R² = **0.0789**, F-statistic = **2.78** (p = **0.0021**), Residual SE = **2.704** on **218** df, AIC = **1122.0**, BIC = **1163.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+15.7550** | 1.9012 | ±3.8025 | **+8.287** | **1.16e-16** | *** |
| Education: graduate level (vs college) | +0.2480 | 0.4081 | ±0.8162 | +0.608 | 0.5434 |  |
| **Education: high school or below (vs college)** | **-1.2167** | 0.5777 | ±1.1553 | **-2.106** | **0.0352** | * |
| Site: UCSD (vs UAB) | +0.2361 | 0.4845 | ±0.9690 | +0.487 | 0.6260 |  |
| Site: UW (vs UAB) | -0.1050 | 0.5009 | ±1.0019 | -0.210 | 0.8340 |  |
| **Age (years)** | **-0.0597** | 0.0229 | ±0.0459 | **-2.603** | **0.0092** | ** |
| BMI (kg/m2) | -0.0281 | 0.0298 | ±0.0596 | -0.945 | 0.3448 |  |
| Hypertension | -0.3430 | 0.4187 | ±0.8375 | -0.819 | 0.4126 |  |
| High cholesterol | +0.5857 | 0.4307 | ±0.8615 | +1.360 | 0.1739 |  |
| **Kidney disease** | **+1.0024** | 0.4281 | ±0.8561 | **+2.342** | **0.0192** | * |
| Circulatory disease | +0.5867 | 0.4133 | ±0.8265 | +1.420 | 0.1557 |  |
| Avg. daily mean/SD | +0.1481 | 0.1261 | ±0.2521 | +1.175 | 0.2400 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: MAG (mg/dL/h)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + mag_mg_dl_per_h`  
**Model Diagnostics**: N = **230**, R² = **0.1187**, Adj R² = **0.0743**, F-statistic = **2.67** (p = **0.0031**), Residual SE = **2.711** on **218** df, AIC = **1123.2**, BIC = **1164.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.3199** | 2.0416 | ±4.0831 | **+8.484** | **2.18e-17** | *** |
| Education: graduate level (vs college) | +0.3060 | 0.4177 | ±0.8354 | +0.733 | 0.4638 |  |
| **Education: high school or below (vs college)** | **-1.2870** | 0.5765 | ±1.1531 | **-2.232** | **0.0256** | * |
| Site: UCSD (vs UAB) | +0.2347 | 0.4897 | ±0.9793 | +0.479 | 0.6318 |  |
| Site: UW (vs UAB) | -0.1201 | 0.4978 | ±0.9957 | -0.241 | 0.8094 |  |
| **Age (years)** | **-0.0656** | 0.0229 | ±0.0458 | **-2.867** | **0.0041** | ** |
| BMI (kg/m2) | -0.0253 | 0.0294 | ±0.0589 | -0.858 | 0.3910 |  |
| Hypertension | -0.3262 | 0.4132 | ±0.8264 | -0.789 | 0.4299 |  |
| High cholesterol | +0.5973 | 0.4280 | ±0.8560 | +1.396 | 0.1628 |  |
| **Kidney disease** | **+0.9055** | 0.4368 | ±0.8736 | **+2.073** | **0.0382** | * |
| Circulatory disease | +0.5823 | 0.4156 | ±0.8311 | +1.401 | 0.1611 |  |
| MAG (mg/dL/h) | -0.0117 | 0.0178 | ±0.0357 | -0.654 | 0.5129 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily range (mg/dL)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_range`  
**Model Diagnostics**: N = **230**, R² = **0.1333**, Adj R² = **0.0896**, F-statistic = **3.05** (p = **8.13e-04**), Residual SE = **2.689** on **218** df, AIC = **1119.4**, BIC = **1160.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.8144** | 1.9229 | ±3.8458 | **+9.264** | **1.96e-20** | *** |
| Education: graduate level (vs college) | +0.2284 | 0.4140 | ±0.8280 | +0.552 | 0.5812 |  |
| Education: high school or below (vs college) | -1.1193 | 0.5803 | ±1.1605 | -1.929 | 0.0537 | . |
| Site: UCSD (vs UAB) | +0.2010 | 0.4793 | ±0.9587 | +0.419 | 0.6750 |  |
| Site: UW (vs UAB) | -0.1324 | 0.5029 | ±1.0059 | -0.263 | 0.7923 |  |
| **Age (years)** | **-0.0613** | 0.0236 | ±0.0471 | **-2.599** | **0.0094** | ** |
| BMI (kg/m2) | -0.0304 | 0.0294 | ±0.0587 | -1.034 | 0.3012 |  |
| Hypertension | -0.3333 | 0.4151 | ±0.8301 | -0.803 | 0.4220 |  |
| High cholesterol | +0.5815 | 0.4301 | ±0.8603 | +1.352 | 0.1764 |  |
| **Kidney disease** | **+1.1446** | 0.4420 | ±0.8840 | **+2.589** | **0.0096** | ** |
| Circulatory disease | +0.5938 | 0.4032 | ±0.8065 | +1.473 | 0.1409 |  |
| **Avg. daily range (mg/dL)** | **-0.0083** | 0.0041 | ±0.0083 | **-2.006** | **0.0448** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: SD of daily means (mg/dL)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + sd_of_daily_means`  
**Model Diagnostics**: N = **230**, R² = **0.1491**, Adj R² = **0.1062**, F-statistic = **3.47** (p = **1.74e-04**), Residual SE = **2.664** on **218** df, AIC = **1115.1**, BIC = **1156.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.3587** | 1.8390 | ±3.6780 | **+9.439** | **3.76e-21** | *** |
| Education: graduate level (vs college) | +0.2098 | 0.4165 | ±0.8330 | +0.504 | 0.6144 |  |
| **Education: high school or below (vs college)** | **-1.2891** | 0.5874 | ±1.1748 | **-2.194** | **0.0282** | * |
| Site: UCSD (vs UAB) | +0.2138 | 0.4649 | ±0.9298 | +0.460 | 0.6456 |  |
| Site: UW (vs UAB) | -0.1885 | 0.5038 | ±1.0077 | -0.374 | 0.7084 |  |
| **Age (years)** | **-0.0626** | 0.0233 | ±0.0466 | **-2.685** | **0.0072** | ** |
| BMI (kg/m2) | -0.0292 | 0.0283 | ±0.0567 | -1.028 | 0.3038 |  |
| Hypertension | -0.2007 | 0.4020 | ±0.8040 | -0.499 | 0.6177 |  |
| High cholesterol | +0.5520 | 0.4263 | ±0.8527 | +1.295 | 0.1954 |  |
| **Kidney disease** | **+1.1263** | 0.4386 | ±0.8772 | **+2.568** | **0.0102** | * |
| Circulatory disease | +0.6638 | 0.3893 | ±0.7787 | +1.705 | 0.0882 | . |
| **SD of daily means (mg/dL)** | **-0.0546** | 0.0225 | ±0.0451 | **-2.423** | **0.0154** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time in range 70-180, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tir_overall`  
**Model Diagnostics**: N = **230**, R² = **0.1372**, Adj R² = **0.0936**, F-statistic = **3.15** (p = **5.64e-04**), Residual SE = **2.683** on **218** df, AIC = **1118.3**, BIC = **1159.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.8723** | 2.1982 | ±4.3963 | **+6.766** | **1.33e-11** | *** |
| Education: graduate level (vs college) | +0.2323 | 0.4158 | ±0.8316 | +0.559 | 0.5764 |  |
| **Education: high school or below (vs college)** | **-1.2453** | 0.5899 | ±1.1797 | **-2.111** | **0.0348** | * |
| Site: UCSD (vs UAB) | +0.1956 | 0.4723 | ±0.9447 | +0.414 | 0.6787 |  |
| Site: UW (vs UAB) | -0.1643 | 0.5024 | ±1.0048 | -0.327 | 0.7436 |  |
| **Age (years)** | **-0.0640** | 0.0231 | ±0.0461 | **-2.772** | **0.0056** | ** |
| BMI (kg/m2) | -0.0283 | 0.0288 | ±0.0576 | -0.982 | 0.3263 |  |
| Hypertension | -0.3157 | 0.4073 | ±0.8145 | -0.775 | 0.4383 |  |
| High cholesterol | +0.6071 | 0.4276 | ±0.8551 | +1.420 | 0.1556 |  |
| **Kidney disease** | **+1.0738** | 0.4323 | ±0.8646 | **+2.484** | **0.0130** | * |
| Circulatory disease | +0.6337 | 0.3929 | ±0.7857 | +1.613 | 0.1067 |  |
| **Time in range 70-180, pooled (%)** | **+0.0229** | 0.0116 | ±0.0231 | **+1.978** | **0.0479** | * |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time in range 70-180 (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tir`  
**Model Diagnostics**: N = **230**, R² = **0.1360**, Adj R² = **0.0924**, F-statistic = **3.12** (p = **6.29e-04**), Residual SE = **2.685** on **218** df, AIC = **1118.7**, BIC = **1159.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+14.9376** | 2.1986 | ±4.3972 | **+6.794** | **1.09e-11** | *** |
| Education: graduate level (vs college) | +0.2357 | 0.4161 | ±0.8322 | +0.566 | 0.5711 |  |
| **Education: high school or below (vs college)** | **-1.2382** | 0.5914 | ±1.1828 | **-2.094** | **0.0363** | * |
| Site: UCSD (vs UAB) | +0.1936 | 0.4737 | ±0.9473 | +0.409 | 0.6828 |  |
| Site: UW (vs UAB) | -0.1675 | 0.5026 | ±1.0052 | -0.333 | 0.7390 |  |
| **Age (years)** | **-0.0640** | 0.0231 | ±0.0461 | **-2.776** | **0.0055** | ** |
| BMI (kg/m2) | -0.0285 | 0.0289 | ±0.0578 | -0.988 | 0.3232 |  |
| Hypertension | -0.3203 | 0.4077 | ±0.8155 | -0.786 | 0.4321 |  |
| High cholesterol | +0.6080 | 0.4278 | ±0.8556 | +1.421 | 0.1553 |  |
| **Kidney disease** | **+1.0741** | 0.4303 | ±0.8605 | **+2.496** | **0.0125** | * |
| Circulatory disease | +0.6324 | 0.3937 | ±0.7874 | +1.606 | 0.1082 |  |
| Avg. daily time in range 70-180 (%) | +0.0222 | 0.0116 | ±0.0232 | +1.911 | 0.0560 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 54, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hypo`  
**Model Diagnostics**: N = **230**, R² = **0.1182**, Adj R² = **0.0738**, F-statistic = **2.66** (p = **0.0032**), Residual SE = **2.712** on **218** df, AIC = **1123.3**, BIC = **1164.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9271** | 1.8702 | ±3.7404 | **+9.051** | **1.42e-19** | *** |
| Education: graduate level (vs college) | +0.3156 | 0.4172 | ±0.8344 | +0.756 | 0.4494 |  |
| **Education: high school or below (vs college)** | **-1.3753** | 0.5794 | ±1.1589 | **-2.374** | **0.0176** | * |
| Site: UCSD (vs UAB) | +0.1844 | 0.4888 | ±0.9777 | +0.377 | 0.7061 |  |
| Site: UW (vs UAB) | -0.1371 | 0.4993 | ±0.9986 | -0.275 | 0.7836 |  |
| **Age (years)** | **-0.0660** | 0.0227 | ±0.0454 | **-2.911** | **0.0036** | ** |
| BMI (kg/m2) | -0.0263 | 0.0294 | ±0.0589 | -0.892 | 0.3724 |  |
| Hypertension | -0.3089 | 0.4114 | ±0.8229 | -0.751 | 0.4527 |  |
| High cholesterol | +0.5966 | 0.4269 | ±0.8538 | +1.398 | 0.1622 |  |
| **Kidney disease** | **+0.8935** | 0.4335 | ±0.8671 | **+2.061** | **0.0393** | * |
| Circulatory disease | +0.6071 | 0.4209 | ±0.8418 | +1.442 | 0.1492 |  |
| Time < 54 (%) | -0.1475 | 0.1716 | ±0.3432 | -0.860 | 0.3900 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 54 (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_below_54`  
**Model Diagnostics**: N = **230**, R² = **0.1217**, Adj R² = **0.0774**, F-statistic = **2.75** (p = **0.0024**), Residual SE = **2.707** on **218** df, AIC = **1122.4**, BIC = **1163.7**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.8999** | 1.8659 | ±3.7318 | **+9.057** | **1.34e-19** | *** |
| Education: graduate level (vs college) | +0.2947 | 0.4177 | ±0.8354 | +0.705 | 0.4805 |  |
| **Education: high school or below (vs college)** | **-1.3890** | 0.5780 | ±1.1561 | **-2.403** | **0.0163** | * |
| Site: UCSD (vs UAB) | +0.1680 | 0.4906 | ±0.9813 | +0.342 | 0.7321 |  |
| Site: UW (vs UAB) | -0.1524 | 0.4985 | ±0.9970 | -0.306 | 0.7599 |  |
| **Age (years)** | **-0.0649** | 0.0227 | ±0.0454 | **-2.857** | **0.0043** | ** |
| BMI (kg/m2) | -0.0265 | 0.0293 | ±0.0587 | -0.902 | 0.3670 |  |
| Hypertension | -0.3105 | 0.4123 | ±0.8246 | -0.753 | 0.4514 |  |
| High cholesterol | +0.5817 | 0.4270 | ±0.8540 | +1.362 | 0.1731 |  |
| **Kidney disease** | **+0.9046** | 0.4326 | ±0.8651 | **+2.091** | **0.0365** | * |
| Circulatory disease | +0.6232 | 0.4194 | ±0.8388 | +1.486 | 0.1373 |  |
| Avg. daily time < 54 (%) | -0.2478 | 0.1673 | ±0.3346 | -1.481 | 0.1386 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-69, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hypo`  
**Model Diagnostics**: N = **230**, R² = **0.1246**, Adj R² = **0.0804**, F-statistic = **2.82** (p = **0.0018**), Residual SE = **2.702** on **218** df, AIC = **1121.7**, BIC = **1162.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.8901** | 1.8705 | ±3.7411 | **+9.030** | **1.72e-19** | *** |
| Education: graduate level (vs college) | +0.2460 | 0.4158 | ±0.8316 | +0.592 | 0.5541 |  |
| **Education: high school or below (vs college)** | **-1.3309** | 0.5810 | ±1.1620 | **-2.291** | **0.0220** | * |
| Site: UCSD (vs UAB) | +0.1826 | 0.4877 | ±0.9753 | +0.375 | 0.7080 |  |
| Site: UW (vs UAB) | -0.1168 | 0.4976 | ±0.9951 | -0.235 | 0.8144 |  |
| **Age (years)** | **-0.0629** | 0.0229 | ±0.0458 | **-2.744** | **0.0061** | ** |
| BMI (kg/m2) | -0.0271 | 0.0294 | ±0.0588 | -0.922 | 0.3565 |  |
| Hypertension | -0.3386 | 0.4081 | ±0.8161 | -0.830 | 0.4066 |  |
| High cholesterol | +0.6207 | 0.4259 | ±0.8518 | +1.457 | 0.1450 |  |
| **Kidney disease** | **+0.9264** | 0.4337 | ±0.8674 | **+2.136** | **0.0327** | * |
| Circulatory disease | +0.5934 | 0.4212 | ±0.8423 | +1.409 | 0.1588 |  |
| Time 54-69, pooled (%) | -0.1020 | 0.0700 | ±0.1400 | -1.457 | 0.1452 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-69 (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_69`  
**Model Diagnostics**: N = **230**, R² = **0.1288**, Adj R² = **0.0848**, F-statistic = **2.93** (p = **0.0012**), Residual SE = **2.696** on **218** df, AIC = **1120.6**, BIC = **1161.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.8353** | 1.8708 | ±3.7417 | **+8.999** | **2.28e-19** | *** |
| Education: graduate level (vs college) | +0.2256 | 0.4152 | ±0.8305 | +0.543 | 0.5870 |  |
| **Education: high school or below (vs college)** | **-1.3136** | 0.5813 | ±1.1627 | **-2.260** | **0.0238** | * |
| Site: UCSD (vs UAB) | +0.1778 | 0.4871 | ±0.9742 | +0.365 | 0.7151 |  |
| Site: UW (vs UAB) | -0.1251 | 0.4981 | ±0.9962 | -0.251 | 0.8018 |  |
| **Age (years)** | **-0.0614** | 0.0230 | ±0.0460 | **-2.674** | **0.0075** | ** |
| BMI (kg/m2) | -0.0270 | 0.0293 | ±0.0587 | -0.921 | 0.3571 |  |
| Hypertension | -0.3443 | 0.4076 | ±0.8153 | -0.845 | 0.3983 |  |
| High cholesterol | +0.6217 | 0.4249 | ±0.8498 | +1.463 | 0.1434 |  |
| **Kidney disease** | **+0.9261** | 0.4334 | ±0.8669 | **+2.137** | **0.0326** | * |
| Circulatory disease | +0.5874 | 0.4219 | ±0.8438 | +1.392 | 0.1638 |  |
| Avg. daily time 54-69 (%) | -0.1209 | 0.0680 | ±0.1360 | -1.778 | 0.0754 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time < 70, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tbr_below_70`  
**Model Diagnostics**: N = **230**, R² = **0.1236**, Adj R² = **0.0794**, F-statistic = **2.80** (p = **0.0020**), Residual SE = **2.704** on **218** df, AIC = **1121.9**, BIC = **1163.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9137** | 1.8685 | ±3.7370 | **+9.052** | **1.40e-19** | *** |
| Education: graduate level (vs college) | +0.2577 | 0.4159 | ±0.8318 | +0.620 | 0.5355 |  |
| **Education: high school or below (vs college)** | **-1.3472** | 0.5801 | ±1.1603 | **-2.322** | **0.0202** | * |
| Site: UCSD (vs UAB) | +0.1720 | 0.4885 | ±0.9770 | +0.352 | 0.7248 |  |
| Site: UW (vs UAB) | -0.1347 | 0.4970 | ±0.9941 | -0.271 | 0.7864 |  |
| **Age (years)** | **-0.0635** | 0.0228 | ±0.0456 | **-2.782** | **0.0054** | ** |
| BMI (kg/m2) | -0.0268 | 0.0294 | ±0.0587 | -0.914 | 0.3608 |  |
| Hypertension | -0.3299 | 0.4085 | ±0.8171 | -0.807 | 0.4194 |  |
| High cholesterol | +0.6166 | 0.4260 | ±0.8520 | +1.448 | 0.1478 |  |
| **Kidney disease** | **+0.9168** | 0.4330 | ±0.8661 | **+2.117** | **0.0343** | * |
| Circulatory disease | +0.6039 | 0.4214 | ±0.8428 | +1.433 | 0.1518 |  |
| Time < 70 (%) | -0.0791 | 0.0541 | ±0.1082 | -1.462 | 0.1438 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time < 70 (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tbr`  
**Model Diagnostics**: N = **230**, R² = **0.1284**, Adj R² = **0.0844**, F-statistic = **2.92** (p = **0.0013**), Residual SE = **2.696** on **218** df, AIC = **1120.7**, BIC = **1161.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.8523** | 1.8679 | ±3.7359 | **+9.022** | **1.85e-19** | *** |
| Education: graduate level (vs college) | +0.2326 | 0.4157 | ±0.8313 | +0.560 | 0.5758 |  |
| **Education: high school or below (vs college)** | **-1.3351** | 0.5794 | ±1.1589 | **-2.304** | **0.0212** | * |
| Site: UCSD (vs UAB) | +0.1657 | 0.4882 | ±0.9764 | +0.339 | 0.7343 |  |
| Site: UW (vs UAB) | -0.1418 | 0.4976 | ±0.9951 | -0.285 | 0.7756 |  |
| **Age (years)** | **-0.0618** | 0.0229 | ±0.0458 | **-2.701** | **0.0069** | ** |
| BMI (kg/m2) | -0.0269 | 0.0293 | ±0.0586 | -0.918 | 0.3584 |  |
| Hypertension | -0.3367 | 0.4084 | ±0.8169 | -0.824 | 0.4097 |  |
| High cholesterol | +0.6118 | 0.4250 | ±0.8500 | +1.440 | 0.1500 |  |
| **Kidney disease** | **+0.9226** | 0.4326 | ±0.8652 | **+2.133** | **0.0329** | * |
| Circulatory disease | +0.6022 | 0.4215 | ±0.8431 | +1.429 | 0.1531 |  |
| Avg. daily time < 70 (%) | -0.0972 | 0.0523 | ±0.1046 | -1.859 | 0.0631 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 54-250, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_54_250`  
**Model Diagnostics**: N = **230**, R² = **0.1379**, Adj R² = **0.0944**, F-statistic = **3.17** (p = **5.23e-04**), Residual SE = **2.682** on **218** df, AIC = **1118.1**, BIC = **1159.4**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.5659** | 3.3856 | ±6.7712 | **+3.712** | **2.06e-04** | *** |
| Education: graduate level (vs college) | +0.2643 | 0.4149 | ±0.8299 | +0.637 | 0.5242 |  |
| **Education: high school or below (vs college)** | **-1.2354** | 0.5941 | ±1.1881 | **-2.080** | **0.0376** | * |
| Site: UCSD (vs UAB) | +0.1803 | 0.4763 | ±0.9525 | +0.379 | 0.7050 |  |
| Site: UW (vs UAB) | -0.2008 | 0.5006 | ±1.0013 | -0.401 | 0.6883 |  |
| **Age (years)** | **-0.0671** | 0.0227 | ±0.0454 | **-2.953** | **0.0031** | ** |
| BMI (kg/m2) | -0.0286 | 0.0290 | ±0.0581 | -0.984 | 0.3253 |  |
| Hypertension | -0.2833 | 0.4126 | ±0.8251 | -0.687 | 0.4923 |  |
| High cholesterol | +0.5430 | 0.4317 | ±0.8635 | +1.258 | 0.2085 |  |
| **Kidney disease** | **+0.9833** | 0.4436 | ±0.8871 | **+2.217** | **0.0266** | * |
| Circulatory disease | +0.6406 | 0.3943 | ±0.7886 | +1.625 | 0.1042 |  |
| Time 54-250, pooled (%) | +0.0462 | 0.0274 | ±0.0548 | +1.685 | 0.0919 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 54-250 (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_54_250`  
**Model Diagnostics**: N = **230**, R² = **0.1375**, Adj R² = **0.0939**, F-statistic = **3.16** (p = **5.48e-04**), Residual SE = **2.682** on **218** df, AIC = **1118.3**, BIC = **1159.5**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+12.1052** | 3.6984 | ±7.3968 | **+3.273** | **0.0011** | ** |
| Education: graduate level (vs college) | +0.2592 | 0.4153 | ±0.8305 | +0.624 | 0.5325 |  |
| **Education: high school or below (vs college)** | **-1.2139** | 0.5970 | ±1.1939 | **-2.034** | **0.0420** | * |
| Site: UCSD (vs UAB) | +0.1894 | 0.4752 | ±0.9503 | +0.399 | 0.6901 |  |
| Site: UW (vs UAB) | -0.1915 | 0.5006 | ±1.0011 | -0.382 | 0.7021 |  |
| **Age (years)** | **-0.0666** | 0.0227 | ±0.0455 | **-2.926** | **0.0034** | ** |
| BMI (kg/m2) | -0.0293 | 0.0291 | ±0.0581 | -1.008 | 0.3132 |  |
| Hypertension | -0.2817 | 0.4114 | ±0.8228 | -0.685 | 0.4934 |  |
| High cholesterol | +0.5453 | 0.4309 | ±0.8619 | +1.265 | 0.2057 |  |
| **Kidney disease** | **+1.0010** | 0.4456 | ±0.8911 | **+2.247** | **0.0247** | * |
| Circulatory disease | +0.6545 | 0.3944 | ±0.7888 | +1.659 | 0.0970 | . |
| Avg. daily time 54-250 (%) | +0.0505 | 0.0311 | ±0.0622 | +1.624 | 0.1044 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time 181-250, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_mod_hyper`  
**Model Diagnostics**: N = **230**, R² = **0.1240**, Adj R² = **0.0798**, F-statistic = **2.80** (p = **0.0019**), Residual SE = **2.703** on **218** df, AIC = **1121.8**, BIC = **1163.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+16.9910** | 1.8725 | ±3.7451 | **+9.074** | **1.15e-19** | *** |
| Education: graduate level (vs college) | +0.2880 | 0.4176 | ±0.8351 | +0.690 | 0.4904 |  |
| **Education: high school or below (vs college)** | **-1.3155** | 0.5814 | ±1.1628 | **-2.263** | **0.0237** | * |
| Site: UCSD (vs UAB) | +0.2230 | 0.4790 | ±0.9580 | +0.466 | 0.6415 |  |
| Site: UW (vs UAB) | -0.1049 | 0.5003 | ±1.0006 | -0.210 | 0.8339 |  |
| **Age (years)** | **-0.0646** | 0.0231 | ±0.0462 | **-2.796** | **0.0052** | ** |
| BMI (kg/m2) | -0.0270 | 0.0292 | ±0.0584 | -0.927 | 0.3541 |  |
| Hypertension | -0.3251 | 0.4107 | ±0.8215 | -0.792 | 0.4286 |  |
| High cholesterol | +0.6212 | 0.4283 | ±0.8567 | +1.450 | 0.1470 |  |
| **Kidney disease** | **+1.0114** | 0.4248 | ±0.8495 | **+2.381** | **0.0173** | * |
| Circulatory disease | +0.6006 | 0.4058 | ±0.8116 | +1.480 | 0.1389 |  |
| Time 181-250, pooled (%) | -0.0201 | 0.0154 | ±0.0308 | -1.301 | 0.1933 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time 181-250 (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_181_250`  
**Model Diagnostics**: N = **230**, R² = **0.1236**, Adj R² = **0.0794**, F-statistic = **2.80** (p = **0.0020**), Residual SE = **2.704** on **218** df, AIC = **1121.9**, BIC = **1163.2**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.0169** | 1.8740 | ±3.7479 | **+9.081** | **1.08e-19** | *** |
| Education: graduate level (vs college) | +0.2911 | 0.4177 | ±0.8354 | +0.697 | 0.4859 |  |
| **Education: high school or below (vs college)** | **-1.3145** | 0.5828 | ±1.1656 | **-2.256** | **0.0241** | * |
| Site: UCSD (vs UAB) | +0.2153 | 0.4811 | ±0.9622 | +0.448 | 0.6544 |  |
| Site: UW (vs UAB) | -0.1155 | 0.5003 | ±1.0005 | -0.231 | 0.8174 |  |
| **Age (years)** | **-0.0650** | 0.0230 | ±0.0461 | **-2.824** | **0.0047** | ** |
| BMI (kg/m2) | -0.0271 | 0.0292 | ±0.0584 | -0.927 | 0.3537 |  |
| Hypertension | -0.3278 | 0.4113 | ±0.8226 | -0.797 | 0.4255 |  |
| High cholesterol | +0.6187 | 0.4284 | ±0.8568 | +1.444 | 0.1487 |  |
| **Kidney disease** | **+1.0072** | 0.4237 | ±0.8474 | **+2.377** | **0.0175** | * |
| Circulatory disease | +0.5979 | 0.4061 | ±0.8121 | +1.472 | 0.1409 |  |
| Avg. daily time 181-250 (%) | -0.0189 | 0.0151 | ±0.0302 | -1.255 | 0.2097 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 180, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + tar_above_180`  
**Model Diagnostics**: N = **230**, R² = **0.1328**, Adj R² = **0.0890**, F-statistic = **3.03** (p = **8.54e-04**), Residual SE = **2.690** on **218** df, AIC = **1119.5**, BIC = **1160.8**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.1141** | 1.8683 | ±3.7366 | **+9.160** | **5.18e-20** | *** |
| Education: graduate level (vs college) | +0.2626 | 0.4162 | ±0.8324 | +0.631 | 0.5281 |  |
| **Education: high school or below (vs college)** | **-1.2616** | 0.5889 | ±1.1777 | **-2.142** | **0.0322** | * |
| Site: UCSD (vs UAB) | +0.2108 | 0.4734 | ±0.9468 | +0.445 | 0.6561 |  |
| Site: UW (vs UAB) | -0.1449 | 0.5019 | ±1.0038 | -0.289 | 0.7728 |  |
| **Age (years)** | **-0.0650** | 0.0230 | ±0.0460 | **-2.826** | **0.0047** | ** |
| BMI (kg/m2) | -0.0280 | 0.0290 | ±0.0579 | -0.965 | 0.3343 |  |
| Hypertension | -0.3120 | 0.4087 | ±0.8174 | -0.764 | 0.4452 |  |
| High cholesterol | +0.5991 | 0.4280 | ±0.8561 | +1.400 | 0.1616 |  |
| **Kidney disease** | **+1.0470** | 0.4340 | ±0.8681 | **+2.412** | **0.0159** | * |
| Circulatory disease | +0.6219 | 0.3954 | ±0.7909 | +1.573 | 0.1158 |  |
| Time > 180 (%) | -0.0199 | 0.0114 | ±0.0229 | -1.737 | 0.0824 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 180 (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_tar`  
**Model Diagnostics**: N = **230**, R² = **0.1307**, Adj R² = **0.0869**, F-statistic = **2.98** (p = **0.0010**), Residual SE = **2.693** on **218** df, AIC = **1120.1**, BIC = **1161.3**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.1161** | 1.8688 | ±3.7376 | **+9.159** | **5.25e-20** | *** |
| Education: graduate level (vs college) | +0.2688 | 0.4164 | ±0.8329 | +0.645 | 0.5186 |  |
| **Education: high school or below (vs college)** | **-1.2607** | 0.5904 | ±1.1809 | **-2.135** | **0.0328** | * |
| Site: UCSD (vs UAB) | +0.2081 | 0.4754 | ±0.9509 | +0.438 | 0.6616 |  |
| Site: UW (vs UAB) | -0.1466 | 0.5019 | ±1.0038 | -0.292 | 0.7702 |  |
| **Age (years)** | **-0.0653** | 0.0230 | ±0.0459 | **-2.841** | **0.0045** | ** |
| BMI (kg/m2) | -0.0281 | 0.0290 | ±0.0581 | -0.968 | 0.3329 |  |
| Hypertension | -0.3155 | 0.4091 | ±0.8183 | -0.771 | 0.4406 |  |
| High cholesterol | +0.6017 | 0.4284 | ±0.8568 | +1.405 | 0.1601 |  |
| **Kidney disease** | **+1.0421** | 0.4327 | ±0.8653 | **+2.409** | **0.0160** | * |
| Circulatory disease | +0.6209 | 0.3967 | ±0.7935 | +1.565 | 0.1176 |  |
| Avg. daily time > 180 (%) | -0.0186 | 0.0116 | ±0.0232 | -1.605 | 0.1085 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Nocturnal time > 180 (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + nocturnal_tar`  
**Model Diagnostics**: N = **230**, R² = **0.1360**, Adj R² = **0.0924**, F-statistic = **3.12** (p = **6.33e-04**), Residual SE = **2.685** on **218** df, AIC = **1118.7**, BIC = **1159.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.1001** | 1.8628 | ±3.7256 | **+9.180** | **4.32e-20** | *** |
| Education: graduate level (vs college) | +0.2708 | 0.4158 | ±0.8317 | +0.651 | 0.5150 |  |
| **Education: high school or below (vs college)** | **-1.2903** | 0.5848 | ±1.1697 | **-2.206** | **0.0274** | * |
| Site: UCSD (vs UAB) | +0.1951 | 0.4757 | ±0.9515 | +0.410 | 0.6817 |  |
| Site: UW (vs UAB) | -0.1509 | 0.5009 | ±1.0017 | -0.301 | 0.7632 |  |
| **Age (years)** | **-0.0667** | 0.0228 | ±0.0455 | **-2.930** | **0.0034** | ** |
| BMI (kg/m2) | -0.0271 | 0.0289 | ±0.0578 | -0.938 | 0.3484 |  |
| Hypertension | -0.2782 | 0.4030 | ±0.8059 | -0.691 | 0.4899 |  |
| High cholesterol | +0.6245 | 0.4279 | ±0.8558 | +1.459 | 0.1445 |  |
| **Kidney disease** | **+0.9588** | 0.4357 | ±0.8714 | **+2.201** | **0.0278** | * |
| Circulatory disease | +0.6483 | 0.3922 | ±0.7844 | +1.653 | 0.0984 | . |
| Nocturnal time > 180 (%) | -0.0218 | 0.0121 | ±0.0243 | -1.802 | 0.0716 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Any reading > 250 during wear (0/1)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + any_above_250`  
**Model Diagnostics**: N = **230**, R² = **0.1352**, Adj R² = **0.0916**, F-statistic = **3.10** (p = **6.80e-04**), Residual SE = **2.686** on **218** df, AIC = **1118.9**, BIC = **1160.1**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.1110** | 1.8348 | ±3.6696 | **+9.326** | **1.10e-20** | *** |
| Education: graduate level (vs college) | +0.2308 | 0.4181 | ±0.8362 | +0.552 | 0.5809 |  |
| **Education: high school or below (vs college)** | **-1.2665** | 0.5709 | ±1.1418 | **-2.218** | **0.0265** | * |
| Site: UCSD (vs UAB) | +0.2210 | 0.4771 | ±0.9542 | +0.463 | 0.6432 |  |
| Site: UW (vs UAB) | -0.0253 | 0.5153 | ±1.0307 | -0.049 | 0.9609 |  |
| **Age (years)** | **-0.0605** | 0.0244 | ±0.0488 | **-2.479** | **0.0132** | * |
| BMI (kg/m2) | -0.0326 | 0.0287 | ±0.0574 | -1.136 | 0.2559 |  |
| Hypertension | -0.2960 | 0.4121 | ±0.8243 | -0.718 | 0.4726 |  |
| High cholesterol | +0.5735 | 0.4299 | ±0.8597 | +1.334 | 0.1822 |  |
| **Kidney disease** | **+1.1077** | 0.4356 | ±0.8711 | **+2.543** | **0.0110** | * |
| Circulatory disease | +0.6030 | 0.4052 | ±0.8104 | +1.488 | 0.1367 |  |
| Any reading > 250 during wear (0/1) | -0.8052 | 0.4168 | ±0.8336 | -1.932 | 0.0534 | . |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Time > 250, pooled (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + pct_severe_hyper`  
**Model Diagnostics**: N = **230**, R² = **0.1373**, Adj R² = **0.0938**, F-statistic = **3.15** (p = **5.57e-04**), Residual SE = **2.683** on **218** df, AIC = **1118.3**, BIC = **1159.6**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.1630** | 1.8622 | ±3.7244 | **+9.217** | **3.07e-20** | *** |
| Education: graduate level (vs college) | +0.2688 | 0.4150 | ±0.8300 | +0.648 | 0.5172 |  |
| **Education: high school or below (vs college)** | **-1.2302** | 0.5938 | ±1.1876 | **-2.072** | **0.0383** | * |
| Site: UCSD (vs UAB) | +0.1917 | 0.4754 | ±0.9508 | +0.403 | 0.6868 |  |
| Site: UW (vs UAB) | -0.1865 | 0.5003 | ±1.0006 | -0.373 | 0.7094 |  |
| **Age (years)** | **-0.0672** | 0.0227 | ±0.0454 | **-2.956** | **0.0031** | ** |
| BMI (kg/m2) | -0.0286 | 0.0291 | ±0.0581 | -0.984 | 0.3251 |  |
| Hypertension | -0.2856 | 0.4128 | ±0.8255 | -0.692 | 0.4889 |  |
| High cholesterol | +0.5421 | 0.4321 | ±0.8641 | +1.255 | 0.2096 |  |
| **Kidney disease** | **+0.9847** | 0.4443 | ±0.8885 | **+2.216** | **0.0267** | * |
| Circulatory disease | +0.6326 | 0.3952 | ±0.7905 | +1.601 | 0.1095 |  |
| Time > 250 (%) | -0.0457 | 0.0279 | ±0.0559 | -1.636 | 0.1019 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*

#### Predictor entered alone: Avg. daily time > 250 (%)  (N = 230)
**Regression Call / Formula**: `moca_memory_index ~ age + bmi + C(education_level) + C(clinical_site) + hypertension + high_cholesterol + kidney_disease + circulatory_problems + avg_daily_pct_above_250`  
**Model Diagnostics**: N = **230**, R² = **0.1359**, Adj R² = **0.0923**, F-statistic = **3.12** (p = **6.34e-04**), Residual SE = **2.685** on **218** df, AIC = **1118.7**, BIC = **1159.9**  (standard errors: HC3-robust)

| Term / Variable | Coef Estimate (β) | Std. Error (SE) | 2 * SE (95% CI Margin) | t value | Pr(>\|t\|) | Signif |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | **+17.1460** | 1.8617 | ±3.7234 | **+9.210** | **3.26e-20** | *** |
| Education: graduate level (vs college) | +0.2676 | 0.4151 | ±0.8303 | +0.645 | 0.5191 |  |
| **Education: high school or below (vs college)** | **-1.2109** | 0.5977 | ±1.1953 | **-2.026** | **0.0428** | * |
| Site: UCSD (vs UAB) | +0.2005 | 0.4749 | ±0.9498 | +0.422 | 0.6729 |  |
| Site: UW (vs UAB) | -0.1773 | 0.5003 | ±1.0006 | -0.354 | 0.7230 |  |
| **Age (years)** | **-0.0668** | 0.0227 | ±0.0455 | **-2.940** | **0.0033** | ** |
| BMI (kg/m2) | -0.0292 | 0.0291 | ±0.0582 | -1.004 | 0.3153 |  |
| Hypertension | -0.2836 | 0.4114 | ±0.8228 | -0.689 | 0.4906 |  |
| High cholesterol | +0.5486 | 0.4309 | ±0.8617 | +1.273 | 0.2029 |  |
| **Kidney disease** | **+0.9976** | 0.4460 | ±0.8920 | **+2.237** | **0.0253** | * |
| Circulatory disease | +0.6447 | 0.3958 | ±0.7915 | +1.629 | 0.1033 |  |
| Avg. daily time > 250 (%) | -0.0492 | 0.0321 | ±0.0641 | -1.534 | 0.1251 |  |

*Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1*


## Interpretation - Non-healthy group (T2D non-insulin + T2D insulin) - Cognition

Computed from the same models as the tables above (summary statistics in `data/`); bold rows in the tables above mark terms with p < 0.05.

**Scope.** 90 single-predictor tests; 30 with raw p < 0.05 (about 4 expected by chance); FDR rule applied to 0 tests (samples with n >= 500), of which **0** are significant at BH q < 0.05 in the all-tests family; no test met the FDR rule, so only raw p-values are available.

**By outcome (best out-of-sample predictor, then the associations that survive FDR):**

- **MoCA total score (0-30)** (n = 230): best single predictor out of sample is **HbA1c** (CV R² 0.030 vs 0.023 for covariates alone, gain +0.007; -0.543 per SD, p = 0.015). Raw p < 0.05 (FDR not applicable here): HbA1c (p = 0.015), %54-250 (daily avg) (p = 0.016), %>250 (daily avg) (p = 0.018), %>180 nocturnal (p = 0.020), TIR 70-180 (pooled) (p = 0.021).
- **Cognitive impairment (MoCA < 26)** (n = 230): best single predictor out of sample is **HbA1c** (CV AUC 0.640 vs 0.613 for covariates alone, gain +0.027; OR 1.52 per SD, p = 0.010). Raw p < 0.05 (FDR not applicable here): HbA1c (p = 0.010), TIR 70-180 (pooled) (p = 0.022), TIR 70-180 (daily avg) (p = 0.023), SD of daily means (p = 0.035), %>180 (pooled) (p = 0.036).
- **MoCA memory index score (0-15)** (n = 230): best single predictor out of sample is **SD (pooled)** (CV R² 0.032 vs 0.003 for covariates alone, gain +0.028; -0.519 per SD, p = 0.009). Raw p < 0.05 (FDR not applicable here): CV (p = 0.003), SD (pooled) (p = 0.009), SD (daily avg) (p = 0.015), SD of daily means (p = 0.015), HbA1c (p = 0.020).

**Most predictable outcomes (largest out-of-sample gain over covariates):** MoCA memory index score (0-15) (+0.028, via SD (pooled)); Cognitive impairment (MoCA < 26) (+0.027, via HbA1c); MoCA total score (0-30) (+0.007, via HbA1c). Gains below about 0.01 are negligible for individual-level prediction even when statistically significant.

**Predictor families carrying the signal:** CGM variability (0 FDR-significant / 9 raw-significant of 24); Band > 180 (0 FDR-significant / 6 raw-significant of 9); Range 70-180 (0 FDR-significant / 5 raw-significant of 6).
Level metrics: 0 FDR-significant (3 raw); variability metrics: 0 FDR-significant (9 raw); HbA1c alone: 0 FDR-significant (3 raw) across the outcomes in this file.

**Where a CGM metric beats HbA1c by more than 2 AIC on the same rows:** MoCA memory index score (SD of daily means, ΔAIC -3.3).

_Interpretation note: all models are cross-sectional and covariate-adjusted (age, BMI, education, site, hypertension, high cholesterol, kidney disease, circulatory disease; season for environmental outcomes). Effects are per 1 SD of the predictor in this sample. Bold cells in the tables mark raw p < 0.05; q-values follow the FDR rule (BH applied when n >= 500)._
